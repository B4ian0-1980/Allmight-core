---json
{
  "id": "omniroute_gateway",
  "title": "🚀 OmniRoute — The Free AI Gateway",
  "categoria": "06-devops-infra",
  "subcategoria": "nginx-gateways",
  "resumo": "**Origem:** Baseado no repositório [`diegosouzapw/OmniRoute`](https://github.com/diegosouzapw/OmniRoute) **Finalidade:** Gateway unificado de IA para desenvolvedores com roteamento em múltiplos provedores gratuitos, fallback automático e compressã...",
  "gatilhos": [
    "devops",
    "free",
    "gateway",
    "gateways",
    "infra",
    "nginx",
    "omniroute",
    "the"
  ],
  "perguntas_tipo": [
    "Como utilizar 🚀 OmniRoute — The Free AI Gateway?",
    "Quais as boas praticas de nginx-gateways?"
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
  "dono": "stack-nginx-gateways",
  "prioridade": 2
}
---

# 🚀 OmniRoute — The Free AI Gateway

> **Origem:** Baseado no repositório [`diegosouzapw/OmniRoute`](https://github.com/diegosouzapw/OmniRoute)
> **Finalidade:** Gateway unificado de IA para desenvolvedores com roteamento em múltiplos provedores gratuitos, fallback automático e compressão de tokens.

---

## 📋 Visão Geral

O OmniRoute é um proxy/gateway local ou auto-hospedado compatível com a API OpenAI (`/v1/chat/completions`) que conecta:
- **358 provedores de IA** mapeados.
- **150+ planos/tiers gratuitos** agregados (~1.62B de tokens gratuitos por mês).
- **Auto-fallback & Failover:** Se o provedor A falhar ou atingir cota, ele tenta o provedor B instantaneamente.
- **Compressão de Tokens (RTK + Caveman):** Reduz o consumo de tokens de contexto entre 15% e 95% (média ~89%), evitando estourar limites de contexto.
- **Compatibilidade nativa:** Funciona como backend para Antigravity, Cursor, Cline, Claude Code, Copilot, além de qualquer aplicação Web/Backend em PHP, Node.js, Python ou Go.

---

## 🐳 Inicialização Rápida

### Via Docker
```bash
docker run -d -p 8080:8080 --name omniroute diegosouzapw/omniroute:latest
```

### Via Node.js
```bash
git clone https://github.com/diegosouzapw/OmniRoute.git
cd OmniRoute
npm install
npm run start
```

---

## 💻 Como Configurar nos Sistemas Desenvolvidos

Em qualquer sistema (PHP, Python, Node, Next.js), basta trocar a `BASE_URL` da OpenAI para o endpoint do OmniRoute:

```env
OPENAI_BASE_URL="http://localhost:8080/v1"
OPENAI_API_KEY="omniroute-key" # ou token configurado no gateway
```

Assim, qualquer biblioteca oficial (ex: `openai-node`, `openai-python`, ou chamadas cURL em PHP) continuará funcionando normalmente, sem custo de chamadas.

---

## 💡 Quando o Agente Deve Sugerir o OmniRoute:
1. O usuário está desenvolvendo um backend/sistema que precisa integrar LLMs mas quer custo zero de infraestrutura.
2. O usuário relata problemas de instabilidade, quedas de provedor ou limites de taxa (rate-limit 429) em APIs de IA.
3. Projetos que necessitam de processamento de grande volume de texto onde a compressão RTK/Caveman do OmniRoute pode economizar tokens críticos.
