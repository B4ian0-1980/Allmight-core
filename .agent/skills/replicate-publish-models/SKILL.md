---
name: publish-models
description: >
  Push and publish custom AI models to Replicate, and set up CI/CD for
  releasing new model versions safely. Use when running cog push,
  deploying a model to Replicate, releasing a new version, validating
  a model with cog-safe-push before publishing, configuring a Replicate
  deployment, setting up GitHub Actions for model releases, or porting a
  community model to an official one. Trigger on phrases like "push a
  model to Replicate", "publish a model", "deploy a model", "release a
  new version", "cog push", "cog-safe-push", "model CI", "r8.im", or
  "schema compatibility", and when referencing
  github.com/replicate/cog-safe-push or
  github.com/replicate/model-ci-template. Covers cog push, the full
  cog-safe-push config (test cases, fuzz, deployment, official_model),
  GitHub Actions patterns, multi-model matrix pushes, and post-publish
  monitoring. Assumes you already have a working Cog project; see
  build-models if you need to package one first.
---

## Docs

- Cog reference: <https://cog.run/llms.txt>
- `cog push` reference: <https://cog.run/cli#cog-push>
- cog-safe-push: <https://github.com/replicate/cog-safe-push>
- Model CI template: <https://github.com/replicate/model-ci-template>
- Continuous deployment guide: <https://replicate.com/docs/guides/continuous-model-deployment>

## When to use this skill

- You have a working Cog project (see `build-models` if you don't yet).
- You want to publish a private or public model on Replicate.
- You're releasing a new version of an existing model and want to avoid breaking changes.
- You're setting up CI/CD for model releases.

## Prerequisites

- Cog installed and `cog login` against `r8.im` (or `echo $TOKEN | cog login --token-stdin`).
- A model created at `replicate.com/{owner}/{name}` via the API, web UI, or `r8-model` CLI.
- `REPLICATE_API_TOKEN` set in your environment.

## Plain `cog push`

The simplest path. Build and upload a new version:

```
cog push r8.im/owner/my-model
```

Or set `image: r8.im/owner/my-model` in `cog.yaml` and run a bare:

```
cog push
```

Useful flags:

- `--separate-weights` — store weights in a separate layer; faster cold boots and pushes for models with > 1GB of weights.
- `--x-fast` — faster pushes during iteration (skips some validation).
- `--secret id=hf,src=$HOME/.hf_token` — pass build-time secrets without baking them into image history.

## cog-safe-push (recommended for any model with users)

`cog-safe-push` pushes to a private `-test` model first, checks schema compatibility against the live version, runs prediction comparisons, and fuzzes inputs. Catches breaking changes before they reach users.

Install:

```
pip install git+https://github.com/replicate/cog-safe-push.git
```

Required env vars:

- `REPLICATE_API_TOKEN`
- `ANTHROPIC_API_KEY` (Claude judges output similarity for stochastic models)

Basic usage:

```
cog-safe-push --test-hardware=gpu-l40s owner/my-model
```

This will:

1. Lint `predict.py` with ruff.
2. Create a private test model `owner/my-model-test` if missing.
3. Push the local Cog model to the test model.
4. Lint the schema (descriptions, defaults, etc.).
5. Check schema compatibility against the live `owner/my-model` version.
6. Run prediction comparisons between live and test versions.
7. Fuzz the test model with AI-generated inputs.
8. If everything passes, push to `owner/my-model`.

## cog-safe-push.yaml schema

Drop a `cog-safe-push.yaml` in your project root (or `cog-safe-push-configs/<variant>.yaml` for multi-model repos). All five test-case checker types in one example:

```yaml
model: owner/my-model
test_model: owner/my-model-test
test_hardware: gpu-l40s

predict:
  compare_outputs: false              # set false for stochastic models
  predict_timeout: 600
  test_cases:
    - inputs:
        prompt: "a serene mountain landscape"
      match_prompt: "a landscape photo of mountains"   # AI-judged via Claude
    - inputs:
        prompt: "a cat"
      match_url: "https://example.com/reference-cat.png"   # binary/image match
    - inputs:
        prompt: ""
      error_contains: "prompt cannot be empty"           # negative test
    - inputs:
        mode: "json"
      jq_query: '.confidence > 0.8 and .status == "success"'   # JSON output
    - inputs:
        prompt: "echo this"
      exact_string: "echo this"                          # exact string match
  fuzz:
    fixed_inputs:
      seed: 42
    disabled_inputs:
      - debug
    iterations: 10
    prompt: "Generate creative and diverse prompts"

train:                                  # if your model has a trainer
  destination: owner/my-model-trained
  destination_hardware: gpu-l40s
  train_timeout: 1800
  test_cases:
    - inputs:
        input_images: "https://.../training.zip"
        steps: 10

deployment:                             # auto-create or update on push
  name: my-model
  owner: owner
  hardware: gpu-l40s

parallel: 4
fast_push: false
ignore_schema_compatibility: false
official_model: owner/my-model         # for proxy/wrapper models, see below
```

Test case checkers are mutually exclusive: pick exactly one of `match_prompt`, `match_url`, `error_contains`, `jq_query`, or `exact_string` per case. Use `compare_outputs: false` for any stochastic model (diffusion, LLMs); the default `true` is brittle.


---

## 📚 Deep Reference (Progressive Disclosure)

> ⚠️ **CONTEXT OPTIMIZATION:** The detailed methodology, edge cases, attack vectors, and advanced configurations for this skill are stored externally to save tokens.

To access the full technical reference, you MUST use your iew_file tool to read:

d:\xampp\htdocs\0-fonte\.agent\skills\replicate-publish-models\references\reference.md
