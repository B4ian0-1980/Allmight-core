---json
{
  "id": "free_llm_apis",
  "title": "🆓 Catálogo de Provedores e APIs Gratuitas de LLM",
  "categoria": "02-arquitetura-ia",
  "subcategoria": "llms-gratuitos",
  "resumo": "**Origem:** Baseado no repositório [`raullenchai/free-llm-api-resources`](https://github.com/raullenchai/free-llm-api-resources) **Finalidade:** Servir como referência de provedores sem custo para testes, prototipação, ambientes de desenvolvimento...",
  "gatilhos": [
    "apis",
    "arquitetura",
    "free",
    "gratuitas",
    "gratuitos",
    "llm",
    "llms",
    "provedores"
  ],
  "perguntas_tipo": [
    "Como utilizar 🆓 Catálogo de Provedores e APIs Gratuitas de LLM?",
    "Quais as boas praticas de llms-gratuitos?"
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
  "dono": "stack-llms-gratuitos",
  "prioridade": 2
}
---

# 🆓 Catálogo de Provedores e APIs Gratuitas de LLM

> **Origem:** Baseado no repositório [`raullenchai/free-llm-api-resources`](https://github.com/raullenchai/free-llm-api-resources)
> **Finalidade:** Servir como referência de provedores sem custo para testes, prototipação, ambientes de desenvolvimento e fallbacks resilientes.

---

## 📋 Provedores com Tiers Gratuitos Permanentes

| Provedor | Modelos Destacados | Limites Gratuitos | Casos de Uso Recomendados |
| :--- | :--- | :--- | :--- |
| **Google AI Studio** | Gemini 2.5 Pro, Gemini 2.5 Flash | 15 RPM / 1M TPM / 1.500 RPD | Projetos com contexto longo (até 2M tokens), tarefas multimodais e raciocínio. |
| **Groq Cloud** | Llama 3.3 70B, DeepSeek R1 Distill | 30 RPM / 6.000 TPM | Inferência em ultra-alta velocidade (500+ tokens/s), ideal para streaming e validações rápidas. |
| **Cerebras** | Llama 3.1 8B, Llama 3.3 70B | 30 RPM / 60.000 TPM | Menor latência do mercado em inferência direta. |
| **OpenRouter** | DeepSeek V3, Llama 3.3 70B Free | 20 RPM / 50-1.000 RPD | Roteador universal com catálogo de modelos tagged `:free`. |
| **NVIDIA NIM** | Llama 3.1 405B, Mixtral, Nemotron | 1.000 créditos free | Testes com modelos massivos (405B) e embeddings corporativos. |
| **GitHub Models** | GPT-4o, Claude 3.5 Sonnet, Llama 3 | 15 RPM / 150 RPD | Testes no ecossistema GitHub usando token pessoal (`ghp_...`). |
| **Mistral AI** | Codestral, Mistral Small/Large | Tier de desenvolvedor gratuito | Geração de código e preenchimento FIM (Fill-in-the-Middle). |
| **Cloudflare Workers AI**| Llama 3, Qwen, Mistral | 10.000 Neurons/dia | Edge AI rodando diretamente na infraestrutura da Cloudflare. |

---

## 🛠️ Como Integrar nos Sistemas em Desenvolvimento

### Exemplo Universal (Padrão OpenAI / cURL / Fetch)
A maioria desses serviços expõe rotas compatíveis com a API OpenAI:

```javascript
// Exemplo com Groq Cloud (API Key gratuita em console.groq.com)
const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.GROQ_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "llama-3.3-70b-versatile",
    messages: [{ role: "user", content: "Sua pergunta" }]
  })
});
```

---

## 💡 Quando o Agente Deve Sugerir Este Catálogo:
- Usuário precisa prototipar uma nova funcionalidade de IA sem gastar saldo ou cadastrar cartão.
- APIs pagas atingiram limite de cota (429 Too Many Requests).
- Necessidade de um modelo com altíssima velocidade para tarefas repetitivas (Groq/Cerebras).
