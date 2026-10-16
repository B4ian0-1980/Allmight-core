---json
{
  "id": "agents_1",
  "title": "AI SDK Usage",
  "categoria": "04-frameworks",
  "subcategoria": "nextjs",
  "resumo": "Guia tecnico e referencias sobre AI SDK Usage.",
  "gatilhos": [
    "agents",
    "frameworks",
    "nextjs",
    "sdk",
    "usage"
  ],
  "perguntas_tipo": [
    "Como utilizar AI SDK Usage?",
    "Quais as boas praticas de nextjs?"
  ],
  "nao_cobre": [],
  "target_agent": [
    "general-assistant"
  ],
  "source": {
    "origin": "AllMight Knowledge Base",
    "original_format": "markdown"
  },
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-nextjs",
  "prioridade": 2
}
---

# AI SDK Usage

## Use Cases

### Generating Text

#### text prompt

```ts
import { generateText } from 'ai';

const result = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Invent a new holiday.', // text prompt
});

const text = result.text; // access generated text
```

#### Specifying the maximum number of tokens to generate

```ts
import { generateText } from 'ai';

const result = await generateText({
  model: 'openai/gpt-5',
  prompt: 'Invent a new holiday.',
  maxOutputTokens: 100, // maximum number of tokens to generate
});
```

### Streaming Text

#### text prompt and text stream

```ts
import { streamText } from 'ai';

const result = streamText({
  model: 'openai/gpt-5',
  prompt: 'Invent a new holiday.', // text prompt
});

const textStream = result.textStream; // access text stream
```

#### Specifying the maximum number of tokens to generate

```ts
import { streamText } from 'ai';

const result = await streamText({
  model: 'openai/gpt-5',
  prompt: 'Invent a new holiday.',
  maxOutputTokens: 100, // maximum number of tokens to generate
});
```
