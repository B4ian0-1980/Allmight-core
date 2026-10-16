---
trigger: manual
description: "Gera apenas o esqueleto (tipos, interfaces, assinaturas e contratos) para expansão com Tab (Supercomplete)."
---

# Modo Esqueleto (Fluxo Híbrido com Tab)

Ao ser acionado pelo usuário (via `@esqueleto`):

1. **Assinaturas e Contratos:** Crie apenas interfaces, tipos, DTOs, classes abstratas e assinaturas tipadas de funções/métodos.
2. **Sem Implementação de Corpo:** Deixe os corpos dos métodos/funções vazios (`pass`, `return null;`, `throw new NotImplementedError();` ou `// TODO: expand via Tab`).
3. **Sem Explicações Verbosas:** Não explique a sintaxe da linguagem. Responda em no máximo 1 a 2 linhas informando o que foi criado e em qual arquivo.
4. **Pronto para o Editor:** O objetivo é permitir que o desenvolvedor utilize `Tab` (Supercomplete) e `Ctrl + I` no editor para preencher o código instantaneamente, com custo zero de tokens de geração no agente.
