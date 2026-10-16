---json
{
  "id": "solicitacao_informacoes",
  "title": "Solicitação de Informações: Next.js 14",
  "categoria": "04-frameworks",
  "subcategoria": "nextjs",
  "resumo": "Guia tecnico e referencias sobre Solicitação de Informações: Next.js 14.",
  "gatilhos": [
    "frameworks",
    "informacoes",
    "next",
    "nextjs",
    "solicitacao"
  ],
  "perguntas_tipo": [
    "Como utilizar Solicitação de Informações: Next.js 14?",
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

# Solicitação de Informações: Next.js 14

## 1. Identificação
- **Tecnologia**: Next.js
- **Versão**: 14+ (Evolutiva)
- **Categoria**: Framework Fullstack React
- **Site Oficial**: [nextjs.org](https://nextjs.org)

## 2. Contexto de Uso
- **Sistema Origem**: Frequência Digital (`sys/frequencia`)
- **Justificativa**: O sistema Frequência utiliza Next.js 14 com App Router como base principal. A base de conhecimento atual foca em Laravel e React "puro", faltando padrões específicos para Server Components, Server Actions e a nova arquitetura do Next.js.
- **Prioridade**: **ALTA** (Tecnologia Core do novo sistema)

## 3. Informações Necessárias

### A. Documentação Fundamental
- [ ] Ciclo de vida dos Server Components vs Client Components
- [ ] Sistema de Roteamento (App Router)
- [ ] Data Fetching e Caching
- [ ] Otimização de Imagens e Fontes

### B. Padrões Arquiteturais
- [ ] Como organizar pastas no App Router (features vs routes)
- [ ] Padrões para Server Actions (substituindo API Routes)
- [ ] Middlewares e Autenticação

### C. Exemplos Práticos
- [ ] CRUD completo com Server Actions
- [ ] Autenticação com Cookies HttpOnly
- [ ] Integração com APIs externas

## 4. Plano de Ação
1. [ ] Coletar documentação oficial do Next.js 14
2. [ ] Extrair padrões utilizados no projeto `sys/frequencia`
3. [ ] Criar guia `PADROES_NEXTJS14.md` em `docs/01-arquitetura`
4. [ ] Classificar como tecnologia padrão para novos projetos fullstack JS

## 5. Materiais Já Disponíveis (no projeto Frequência)
- `app/layout.tsx` (Exemplo de Root Layout)
- `app/api/` (Exemplo de API Routes)
- `lib/auth.ts` (Exemplo de Auth manual)
