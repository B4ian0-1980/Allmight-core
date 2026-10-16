---json
{
  "id": "plandex_cli",
  "title": "💻 Plandex — Terminal-Based AI Coding Engine",
  "categoria": "08-automacao",
  "subcategoria": "cli-agentes",
  "resumo": "**Origem:** Baseado no repositório [`plandex-ai/plandex`](https://github.com/plandex-ai/plandex) **Finalidade:** Motor de desenvolvimento autônomo para o terminal voltado a tarefas massivas, projetos grandes e refatorações em dezenas de arquivos c...",
  "gatilhos": [
    "agentes",
    "automacao",
    "cli",
    "coding",
    "engine",
    "plandex",
    "terminal-based"
  ],
  "perguntas_tipo": [
    "Como utilizar 💻 Plandex — Terminal-Based AI Coding Engine?",
    "Quais as boas praticas de cli-agentes?"
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
  "dono": "stack-cli-agentes",
  "prioridade": 2
}
---

# 💻 Plandex — Terminal-Based AI Coding Engine

> **Origem:** Baseado no repositório [`plandex-ai/plandex`](https://github.com/plandex-ai/plandex)
> **Finalidade:** Motor de desenvolvimento autônomo para o terminal voltado a tarefas massivas, projetos grandes e refatorações em dezenas de arquivos com sandbox cumulativo de diffs.

---

## 📋 Principais Recursos

- **Janela de Contexto Efetiva de 2M Tokens:** Capaz de lidar com ~100k tokens por arquivo.
- **Indexação Tree-sitter de 20M+ Tokens:** Mapeia arquiteturas complexas sem explodir a memória do contexto.
- **Sandbox Cumulativo de Diffs:** Todas as alterações feitas pela IA ficam isoladas em uma sandbox de revisão até que o desenvolvedor aprove explicitamente o merge para o repositório (`plandex diff` -> `plandex apply`).
- **Histórico e Rollback Total:** Permite voltar passos específicos no terminal sem poluir o histórico do Git.
- **Suporte Multi-modelo:** Permite intercalar Claude, GPT-4o, Gemini e modelos locais (Ollama).

---

## ⚡ Instalação e Comandos Essenciais

### Instalação (Windows / PowerShell)
```powershell
# Execução via container ou binário oficial
curl -sL https://plandex.ai/install.sh | bash
```

### Ciclo de Trabalho Recomendado:
1. **Iniciar plano de tarefa:**
   ```bash
   plandex new "Refatorar sistema de autenticação para JWT com refresh token"
   ```
2. **Carregar arquivos de contexto relevantes:**
   ```bash
   plandex load src/auth/ src/controllers/ package.json
   ```
3. **Instruir o agente:**
   ```bash
   plandex tell "Implemente o suporte a cookies HttpOnly e rota de refresh"
   ```
4. **Revisar o diff acumulado:**
   ```bash
   plandex diff
   ```
5. **Aplicar ou descartar:**
   ```bash
   plandex apply    # Aplica ao projeto
   # ou
   plandex rewind   # Desfaz alterações do último passo
   ```

---

## 💡 Quando o Agente Deve Sugerir o Plandex:
1. O usuário precisa de uma **refatoração estrutural profunda** que envolve mais de 10 a 20 arquivos simultâneos.
2. O usuário quer autonomia no terminal para rodar testes, depurar e acumular diffs antes de decidir aceitá-los.
3. Projetos legados extensos onde as ferramentas convencionais perdem contexto pelo tamanho excessivo do codebase.
