---
name: fast-check
description: "Use esta skill para validar rapidamente tipagem, lint e testes locais sem poluir a janela de contexto com logs gigantes."
---

# Validação Rápida e Econômica (Fast-Check)

1. **Validação Silenciosa:** Ao verificar alterações no código, execute `powershell -File .agent/skills/fast-check/scripts/check.ps1 <caminho_do_modulo>` da raiz. O script valida a compilação/sintaxe sem poluir a janela de contexto.
2. **Flags de Output Mínimo:** Se rodar comandos avulsos manualmente, use flags concisas:
   - TypeScript: `npx tsc --noEmit --pretty false`
   - Python: `python -m py_compile arquivo.py` ou `ruff check --quiet`
   - Node: `node --check arquivo.js`
   - PHP: `php -l arquivo.php`
3. **Resolução Cirúrgica:** Corrija os erros apontados diretamente nos números de linha informados pelo compilador/linter e pare assim que o comando retornar código 0.
