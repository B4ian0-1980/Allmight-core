## CI/CD: GitHub Actions

Two paths, depending on how much glue you want.

### Path A: roll your own

```yaml
# .github/workflows/push.yaml
name: Push to Replicate
on:
  workflow_dispatch:
    inputs:
      no_push:
        type: boolean
        default: false

jobs:
  push:
    runs-on: ubuntu-latest-4-cores       # builds need disk + cores
    steps:
      - uses: actions/checkout@v4
      - uses: jlumbroso/free-disk-space@v1.3.1
        with:
          tool-cache: false
          docker-images: false
      - uses: replicate/setup-cog@v2
        with:
          token: ${{ secrets.REPLICATE_API_TOKEN }}
      - run: pip install git+https://github.com/replicate/cog-safe-push.git
      - env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          REPLICATE_API_TOKEN: ${{ secrets.REPLICATE_API_TOKEN }}
        run: |
          cog-safe-push -vv ${{ inputs.no_push && '--no-push' || '' }}
```

Add a `concurrency:` block so PR builds cancel each other while main-branch pushes queue:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}
```

### Path B: reusable workflow from model-ci-template

For Replicate-style multi-model repos, drop in:

```yaml
# .github/workflows/ci.yaml
name: CI
on:
  pull_request: { branches: [main] }
  push: { branches: [main] }
  workflow_dispatch:
    inputs:
      models: { type: string, default: "all" }
      ignore_schema_checks: { type: boolean, default: false }
      cog_version: { type: string, default: "latest" }
      test_only: { type: boolean, default: false }

jobs:
  ci:
    uses: replicate/model-ci-template/.github/workflows/template.yaml@main
    with:
      trigger_type: ${{ github.event_name }}
      models: ${{ inputs.models || 'all' }}
      ignore_schema_checks: ${{ inputs.ignore_schema_checks || false }}
      cog_version: ${{ inputs.cog_version || 'latest' }}
      test_only: ${{ inputs.test_only || false }}
    secrets: inherit
```

The reusable workflow expects:

- `cog-safe-push-configs/<model>.yaml` — one per model variant.
- `script/select-model` — bash file with `if/elif [[ "$MODEL" == "..." ]]` blocks listing valid model names.
- Secrets: `COG_TOKEN`, `REPLICATE_API_TOKEN`, `ANTHROPIC_API_KEY`.

## Multi-model matrix pushes

Pattern from `replicate/cog-flux`: one repo, N variants, push them in parallel.

```yaml
jobs:
  prepare:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set.outputs.matrix }}
    steps:
      - id: set
        run: |
          if [ "${{ inputs.models }}" = "all" ]; then
            echo 'matrix={"model":["schnell","dev","krea-dev"]}' >> "$GITHUB_OUTPUT"
          else
            list=$(echo "${{ inputs.models }}" | jq -Rc 'split(",")')
            echo "matrix={\"model\":$list}" >> "$GITHUB_OUTPUT"
          fi

  push:
    needs: prepare
    runs-on: ubuntu-latest-4-cores
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.prepare.outputs.matrix) }}
    steps:
      - uses: actions/checkout@v4
      - run: ./script/select.sh ${{ matrix.model }}     # produces cog.yaml from a template
      - run: cog-safe-push --config cog-safe-push-configs/${{ matrix.model }}.yaml -vv
```

## Two-pass push for proxy / official models

When you maintain a proxy that wraps a third-party API, you push to a private wrapper first, then update the public-facing official model card. Pattern from `replicate/cog-official-template`:

```bash
./script/write-api-key                                              # bake API key into config
cog-safe-push --config cog-safe-push-configs/${MODEL}.yaml -vv

./script/delete-api-key                                             # strip the key
cog-safe-push --push-official-model --config cog-safe-push-configs/${MODEL}.yaml -vv
```

Set `official_model: owner/name` in the config so `--push-official-model` knows where to publish.

## Deployments

Add a `deployment` block to `cog-safe-push.yaml` to create or update a Replicate deployment automatically on each push:

```yaml
deployment:
  name: my-model
  owner: owner
  hardware: gpu-l40s
```

Scaling defaults: CPU deployments scale 1-20 instances, GPU deployments scale 0-2. Adjust manually via the API or web UI when needed.

## Monitoring published models

Run an hourly canary that exercises the registry path. Pattern from `replicate/cog-pagerduty-check`:

```yaml
name: Hourly cog push check
on:
  schedule:
    - cron: "0 * * * *"
  workflow_dispatch:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - run: |
          # generate a tiny model with a unique uuid, push it, run a prediction
          # by digest, fail loudly if anything breaks.
          ./script/canary.sh
```

Worth doing for any production-critical model, especially when revenue depends on the registry being up.

## Guidelines

- Don't break schema compatibility unless you mean to. cog-safe-push catches it; `--ignore-schema-compatibility` is the opt-out.
- Pin `test_hardware` so test pushes are reproducible.
- Use `--no-push` for dry runs in PR CI; full push on merge to main or on version tags.
- Push from CI rather than laptops once you have users.
- Use `compare_outputs: false` for stochastic models. Use `match_prompt:` for image/video outputs (VLM judgment), `match_url:` for binary outputs you control, `jq_query:` for JSON, `error_contains:` for negative tests.
- Never commit `REPLICATE_API_TOKEN` or `ANTHROPIC_API_KEY`. Use repo secrets.
- For models with weights > 1GB, push with `--separate-weights`.

## Production references

- <https://github.com/replicate/cog-safe-push> — the tool itself, plus its config schema.
- <https://github.com/replicate/model-ci-template> — reusable GitHub Actions workflow.
- <https://github.com/replicate/cog-official-template> — proxy/official model template.
- <https://github.com/replicate/cog-flux/blob/main/.github/workflows/push.yaml> — matrix push across FLUX variants.
- <https://github.com/replicate/cog-comfyui/blob/main/.github/workflows/ci.yaml> — ComfyUI model CI with custom-node install step.
- <https://github.com/replicate/cog-pagerduty-check> — hourly canary pattern.
