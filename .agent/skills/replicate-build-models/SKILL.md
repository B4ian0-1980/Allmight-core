---
name: build-models
description: >
  Package and build custom AI models with Cog for deployment on Replicate.
  Use when creating a cog.yaml or predict.py, defining model inputs and
  outputs, loading model weights at setup time, building Docker images for
  ML models, serving locally with cog serve or cog predict, or porting a
  HuggingFace, GitHub, or ComfyUI model to run on Replicate. Trigger on
  phrases like "build a model", "package a model", "create a Cog model",
  "wrap a model", "containerize an AI model", "predict.py", "cog.yaml",
  "BasePredictor", or "Cog container", and when referencing cog.run,
  github.com/replicate/cog, or github.com/replicate/cog-examples. Covers
  GPU and CUDA setup, pget for fast weight downloads, async predictors
  with continuous batching, streaming outputs, and cold-boot optimization
  for image, video, audio, and LLM models. For pushing built models to
  Replicate, see publish-models. For running existing models, see
  run-models.
---

## Docs

- Cog reference (single file): <https://cog.run/llms.txt>
- `cog.yaml` reference: <https://cog.run/yaml>
- Python predictor reference: <https://cog.run/python>
- Examples: <https://github.com/replicate/cog-examples>
- Template: <https://github.com/replicate/cog-template>

## When to use this skill

- You have model code, weights, or a HuggingFace/GitHub project you want to host on Replicate.
- You're writing or editing a `cog.yaml`, `predict.py`, or `train.py`.
- For pushing a built model to Replicate, see `publish-models`.
- For running existing Replicate models, see `run-models`.

## Prerequisites

- Docker running locally.
- Cog installed: `brew install replicate/tap/cog` or `sh <(curl -fsSL https://cog.run/install.sh)`.
- Optional: `cog init` to scaffold `cog.yaml` and `predict.py`.

## Project layout

The canonical Replicate model layout:

```
cog.yaml
predict.py
weights.py                 # optional download helpers
requirements.txt
cog-safe-push-configs/
  default.yaml             # see publish-models skill
.github/workflows/
  ci.yaml
script/                    # github.com/github/scripts-to-rule-them-all
  lint
  test
  push
```

## cog.yaml essentials

A modern config for a GPU model:

```yaml
build:
  gpu: true
  cuda: "12.8"
  python_version: "3.12"
  python_requirements: requirements.txt
  system_packages:
    - libgl1
    - libglib2.0-0
predict: predict.py:Predictor
```

Notes:

- Pin Python to a specific minor version, and pin every line in `requirements.txt`. Floating versions break cold boots.
- Use `python_requirements` over inline `python_packages` once the list grows.
- `cuda` follows your torch wheel (e.g. `12.8` paired with `torch==2.7.1+cu128`).
- Add `train: train.py:train` if your model is fine-tunable.
- Add `image: r8.im/owner/name` to enable bare `cog push`.

For async predictors with continuous batching:

```yaml
concurrency:
  max: 32
```

## predict.py essentials

```python
from cog import BasePredictor, Input, Path

class Predictor(BasePredictor):
    def setup(self) -> None:
        """One-time loads. Heavy work goes here, not in predict()."""
        self.model = load_model("weights/")

    def predict(
        self,
        prompt: str = Input(description="Text prompt for generation"),
        seed: int = Input(description="Random seed; leave blank for random", default=None),
        num_steps: int = Input(description="Number of denoising steps", ge=1, le=50, default=20),
        output_format: str = Input(description="Output image format", choices=["webp", "jpg", "png"], default="webp"),
    ) -> Path:
        """Run a single prediction."""
        if not prompt.strip():
            raise ValueError("prompt cannot be empty")
        out = self.model.generate(prompt, seed=seed, steps=num_steps)
        return Path(out)
```

Input rules:

- Every input needs a `description`. The description shows up in the model schema and on Replicate's web UI.
- Use `ge`/`le` for numeric bounds, `choices=[...]` for enums, `regex=` for strings.
- Use `cog.Path` for file inputs and outputs, never raw bytes.
- Use `cog.Secret` for any token-like input (HF tokens, API keys), never plain `str`.
- Provide a default that's inside `choices` for categorical inputs.
- Validate inputs early in `predict()` and raise `ValueError`.

Streaming text output (for LLMs):

```python
from cog import BasePredictor, Input, ConcatenateIterator

class Predictor(BasePredictor):
    def predict(self, prompt: str = Input(description="Prompt")) -> ConcatenateIterator[str]:
        for token in self.model.stream(prompt):
            yield token
```

Async predictor with continuous batching (paired with `concurrency.max` in cog.yaml):

```python
from cog import BasePredictor, Input, AsyncConcatenateIterator

class Predictor(BasePredictor):
    async def setup(self) -> None:
        self.engine = await load_async_engine()

    async def predict(
        self,
        prompt: str = Input(description="Prompt"),
    ) -> AsyncConcatenateIterator[str]:
        async for token in self.engine.generate(prompt):
            yield token
```

Dynamic `choices` from on-disk assets (e.g. a `voices/` directory of audio samples):

```python
from pathlib import Path as _P
AVAILABLE_VOICES = sorted(p.stem for p in _P("voices").glob("*.wav"))

class Predictor(BasePredictor):
    def predict(
        self,
        speaker: str = Input(description="Voice", choices=AVAILABLE_VOICES, default=AVAILABLE_VOICES[0]),
    ) -> Path: ...
```


---

## 📚 Deep Reference (Progressive Disclosure)

> ⚠️ **CONTEXT OPTIMIZATION:** The detailed methodology, edge cases, attack vectors, and advanced configurations for this skill are stored externally to save tokens.

To access the full technical reference, you MUST use your iew_file tool to read:

d:\xampp\htdocs\0-fonte\.agent\skills\replicate-build-models\references\reference.md
