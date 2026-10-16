---json
{
  "id": "solicitacao_informacoes",
  "title": "Solicitação de Informações: Prisma ORM",
  "categoria": "05-banco-dados",
  "subcategoria": "prisma",
  "resumo": "Guia tecnico e referencias sobre Solicitação de Informações: Prisma ORM.",
  "gatilhos": [
    "banco",
    "dados",
    "informacoes",
    "orm",
    "prisma",
    "solicitacao"
  ],
  "perguntas_tipo": [
    "Como utilizar Solicitação de Informações: Prisma ORM?",
    "Quais as boas praticas de prisma?"
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
  "dono": "stack-prisma",
  "prioridade": 2
}
---

# Solicitação de Informações: Prisma ORM

## 1. Identificação
- **Tecnologia**: Prisma ORM
- **Versão**: 6.x
- **Categoria**: ORM (Object-Relational Mapping) / Database Tool
- **Site Oficial**: [prisma.io](https://www.prisma.io)

## 2. Contexto de Uso
- **Sistema Origem**: Frequência Digital (`sys/frequencia`)
- **Justificativa**: Prisma é o ORM utilizado para comunicação com MySQL no sistema Frequência. A base atual foca em Eloquent (Laravel) e não possui guias para Prisma, schema.prisma ou migrations do Prisma.
- **Prioridade**: **ALTA**

## 3. Informações Necessárias

### A. Conceitos Chave
- [ ] Arquivo `schema.prisma` (Modelagem de dados)
- [ ] Prisma Client (Gerado automaticamente)
- [ ] Prisma Migrate (Gestão de schema)
- [ ] Introspection (Banco existente para Código)

### B. Práticas Recomendadas
- [ ] Como gerenciar conexões em ambiente Serverless/Next.js
- [ ] Uso de índices e relações (1:1, 1:N, N:N)
- [ ] Seeders e Testes com Prisma

## 4. Plano de Ação
1. [ ] Documentar comandos essenciais (`generate`, `migrate`, `studio`)
2. [ ] Criar guia de "Eloquent vs Prisma" para desenvolvedores Laravel
3. [ ] Extrair esquema do `sys/frequencia/prisma/schema.prisma` como exemplo real

## 5. Materiais Já Disponíveis
- `prisma/schema.prisma` (Schema completo do sistema de RH)
- `lib/prisma.ts` (Implementação do Singleton pattern)
