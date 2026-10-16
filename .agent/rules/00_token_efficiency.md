---
trigger: always_on
description: "Diretrizes obrigatórias de eficiência de tokens, leitura cirúrgica de arquivos e fluxo híbrido com Supercomplete (Tab) e Ctrl+I."
---

# Diretrizes de Eficiência de Tokens e Fluxo Híbrido

## 1. Economia de Contexto e Leitura Cirúrgica de Arquivos
- **NUNCA** leia arquivos inteiros grandes se puder buscar o trecho exato primeiro.
- Priorize `grep_search` ou leitura por intervalo estrito de linhas (`StartLine` e `EndLine`) antes de carregar arquivos completos no contexto.
- Não leia arquivos da pasta `docs/`, logs extensos ou dependências a menos que seja estritamente necessário para a tarefa atual.
- Referencie caminhos de arquivos usando `@caminho/do/arquivo` sem duplicar o código inteiro na resposta do chat.

## 2. Concisão de Output (Zero Enrolação)
- Seja direto, técnico e conciso. Não explique conceitos básicos da linguagem nem repita blocos de código já modificados pelas ferramentas.
- Em tarefas simples e cirúrgicas, responda apenas com o diff/resumo de 1 a 2 linhas do que foi alterado.

## 3. Sinergia com Autocomplete (Tab / Supercomplete) e Comandos Inline
- Quando o usuário pedir apenas a "estrutura", "interface" ou "esqueleto" de um módulo, crie as assinaturas tipadas, contratos e os pontos de entrada principais; deixe implementações repetitivas limpas e padronizadas para que possam ser expandidas via Supercomplete (`Tab`).
- Ao alterar a assinatura de uma função em um único arquivo onde a refatoração local é óbvia, avise em 1 linha caso o usuário prefira finalizar com `Tab-to-Jump`, a menos que uma refatoração completa multi-arquivo seja solicitada.
