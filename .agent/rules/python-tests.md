---
trigger: glob
globs: "*_test.py, test_*.py, *.test.ts, *.test.js, *.test.mjs"
description: "Padrões para escrita e execução de testes automatizados."
---

# Padrões de Testes Rápidos e Econômicos

1. **Execução Direcionada:** Ao rodar testes no terminal, execute apenas o arquivo ou a suíte afetada diretamente (ex: `pytest caminho/arquivo.py -k nome_do_teste` ou `npm test -- test/fluxo.test.mjs`), em vez da suíte completa de todos os sistemas, para economizar tempo e janela de tokens.
2. **Fixtures e Mocks Enxutos:** Utilize mocks focados apenas nas bordas externas (APIs de terceiros, gateways de mensageria).
3. **Padrão AAA:** Todo teste deve estruturar claramente Arrange, Act e Assert.
