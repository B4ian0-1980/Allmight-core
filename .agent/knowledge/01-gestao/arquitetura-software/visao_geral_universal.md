---json
{
  "id": "visao_geral_universal",
  "title": "🌍 Visão Geral - Base Universal para Desenvolvimento",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🌍 Visão Geral - Base Universal para Desenvolvimento.",
  "gatilhos": [
    "arquitetura",
    "base",
    "desenvolvimento",
    "geral",
    "gestao",
    "para",
    "software",
    "universal"
  ],
  "perguntas_tipo": [
    "Como utilizar 🌍 Visão Geral - Base Universal para Desenvolvimento?",
    "Quais as boas praticas de arquitetura-software?"
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
  "dono": "stack-arquitetura-software",
  "prioridade": 2
}
---

# 🌍 Visão Geral - Base Universal para Desenvolvimento

**Versão:** 1.3.0
**Status:** Estrutura Genérica e Modular

---

## 🎯 Filosofia da Base

Esta estrutura base foi criada para ser **100% universal e genérica**, servindo para:

- ✅ **Qualquer linguagem de programação**
- ✅ **Qualquer framework ou biblioteca**
- ✅ **Qualquer tipo de projeto**

---

## 🔄 Organização da Arquitetura

A pasta `docs/01-arquitetura` contém agora **APENAS TEMPLATES GENÉRICOS**.
Documentação específica de tecnologias (Laravel, React, etc.) foi movida para `docs/referencias-tecnicas`.

### Estrutura Atual:

```
docs/
├── 00-base/             # Templates administrativos (Gestão)
├── 01-arquitetura/      # Templates técnicos (Arquitetura, Padrões)
├── 02-ui-ux/            # Templates visuais (Design System)
├── 03-sdlc/             # Processo de desenvolvimento
├── 04-funcionalidades/  # Especificação de requisitos
├── 05-analises/         # Relatórios e auditorias
├── 06-referencias-tecnicas/ # Guias específicos (Laravel, React, etc.)
└── 07-exemplos-por-dominio/ # Padrões de negócio (Saúde, E-commerce)
```

---

## 🚀 Como Adicionar Nova Tecnologia

1. **Crie a documentação:** Use o `TEMPLATE_PADROES_CODIGO.md`.
2. **Salve em:** `docs/referencias-tecnicas/[sua-tecnologia]/`.
3. **Atualize o índice:** Linke no README de Referências Técnicas.

Isso mantém a raiz da arquitetura limpa e focada em decisões de alto nível.
