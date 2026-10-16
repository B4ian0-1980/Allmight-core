---json
{
  "id": "documentacao_git",
  "title": "Git — Guia Completo & Cheatsheet",
  "categoria": "06-devops-infra",
  "subcategoria": "linux",
  "resumo": "Guia tecnico e referencias sobre Git — Guia Completo & Cheatsheet.",
  "gatilhos": [
    "cheatsheet",
    "completo",
    "devops",
    "documentacao",
    "git",
    "guia",
    "infra",
    "linux"
  ],
  "perguntas_tipo": [
    "Como utilizar Git — Guia Completo & Cheatsheet?",
    "Quais as boas praticas de linux?"
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
  "dono": "stack-linux",
  "prioridade": 2
}
---

# Git — Guia Completo & Cheatsheet

**Fonte:** [git-scm.com/docs](https://git-scm.com/docs) | **Versão:** 2.x  
**Categoria:** Controle de Versão Distribuído

---

## 1. Configuração Inicial

```bash
# Identidade (obrigatório)
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# Editor padrão
git config --global core.editor "code --wait"    # VS Code
git config --global core.editor "nano"           # Nano

# Branch padrão
git config --global init.defaultBranch main

# Alias úteis
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all --decorate"

# Ver configurações
git config --list
```

---

## 2. Workflow Básico (Dia a Dia)

```bash
# 1. Ver o estado
git status

# 2. Adicionar mudanças
git add arquivo.txt          # Arquivo específico
git add .                    # Tudo no diretório
git add -A                   # Tudo (incluindo removidos)
git add -p                   # Interativo (escolhe por pedaço)

# 3. Commitar
git commit -m "feat: adiciona login"
git commit -am "fix: corrige bug"    # add + commit (só tracked)

# 4. Enviar para remoto
git push origin main

# 5. Atualizar do remoto
git pull origin main
```

---

## 3. Comandos por Categoria

### 📁 Criar e Clonar

```bash
# Iniciar repositório novo
git init
git init meu-projeto         # Cria pasta + init

# Clonar existente
git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git pasta-destino
git clone --depth 1 https://github.com/user/repo.git  # Shallow (sem histórico)
```

### 📸 Snapshots (add, commit, reset)

```bash
# Adicionar
git add .                     # Tudo
git add src/                  # Uma pasta
git add *.js                  # Por padrão

# Commit
git commit -m "mensagem"
git commit --amend            # Editar último commit
git commit --amend --no-edit  # Alterar arquivos sem mudar mensagem

# Desfazer
git restore arquivo.txt       # Descartar mudanças locais (não commitadas)
git restore --staged arq.txt  # Remover do staging (undo add)

# Reset
git reset HEAD~1              # Desfaz último commit (mantém mudanças)
git reset --soft HEAD~1       # Desfaz commit (mantém staging)
git reset --hard HEAD~1       # ⚠️ Desfaz commit E descarta mudanças
git reset --hard origin/main  # ⚠️ Força igualar ao remoto

# Remover arquivo do rastreamento
git rm --cached arquivo.txt   # Remove do Git, mantém no disco
git rm arquivo.txt            # Remove do Git E do disco
```

### 🌿 Branches

```bash
# Listar
git branch                   # Locais
git branch -a                # Locais + Remotos
git branch -v                # Com último commit

# Criar
git branch feature/login
git switch -c feature/login     # Criar e mudar (RECOMENDADO)
git checkout -b feature/login   # Criar e mudar (antigo)

# Mudar de branch
git switch main              # RECOMENDADO
git checkout main            # Antigo

# Renomear
git branch -m nome-antigo nome-novo

# Deletar
git branch -d feature/login       # Seguro (só se merged)
git branch -D feature/login       # ⚠️ Forçar deleção
git push origin --delete feature/login  # Deletar no remoto
```

### 🔀 Merge e Rebase

```bash
# Merge (cria commit de merge)
git switch main
git merge feature/login

# Merge sem fast-forward (sempre cria commit de merge)
git merge --no-ff feature/login

# Rebase (reescreve histórico — mais limpo)
git switch feature/login
git rebase main

# Rebase interativo (editar, squash, reordenar commits)
git rebase -i HEAD~3         # Últimos 3 commits

# Abortar merge/rebase com conflito
git merge --abort
git rebase --abort

# Resolver conflitos
# 1. Editar arquivos com conflito
# 2. git add .
# 3. git merge --continue (ou git rebase --continue)
```

### 📡 Remotos (push, pull, fetch)

```bash
# Ver remotos
git remote -v

# Adicionar remoto
git remote add origin https://github.com/user/repo.git

# Buscar atualizações (sem aplicar)
git fetch origin
git fetch --all              # Todos os remotos

# Puxar e aplicar
git pull origin main
git pull --rebase origin main   # Pull com rebase (mais limpo)

# Enviar
git push origin main
git push -u origin main      # Definir upstream (primeira vez)
git push --force-with-lease   # ⚠️ Force push seguro
```

### 📋 Stash (Guardando Mudanças Temporárias)

```bash
# Guardar mudanças atuais
git stash
git stash -m "WIP: trabalhando no login"

# Listar stashes
git stash list

# Aplicar e remover
git stash pop                # Aplica o último e remove
git stash apply              # Aplica o último (mantém na lista)
git stash apply stash@{2}    # Aplica um específico

# Deletar
git stash drop               # Remove o último
git stash clear              # Remove todos
```

### 🏷️ Tags (Versionamento)

```bash
# Criar tag
git tag v1.0.0                          # Tag leve
git tag -a v1.0.0 -m "Release 1.0.0"   # Tag anotada (RECOMENDADO)

# Listar
git tag
git tag -l "v1.*"

# Enviar para remoto
git push origin v1.0.0
git push origin --tags        # Todas

# Deletar
git tag -d v1.0.0
git push origin --delete v1.0.0
```

### 🔍 Inspecção (log, diff, show)

```bash
# Log
git log                       # Completo
git log --oneline             # Resumido
git log --graph --all         # Visual com branches
git log -n 5                  # Últimos 5
git log --author="João"       # Por autor
git log --since="2024-01-01"  # Por data
git log -- arquivo.txt        # De um arquivo específico
git log -p                    # Com diff de cada commit

# Diff
git diff                      # Mudanças não staged
git diff --staged             # Mudanças staged (prontas para commit)
git diff main..feature        # Diferença entre branches
git diff HEAD~3               # Últimos 3 commits

# Show
git show abc1234              # Detalhes de um commit
git show HEAD                 # Último commit
git show v1.0.0               # Detalhes de uma tag

# Blame (quem mudou cada linha)
git blame arquivo.txt
git blame -L 10,20 arquivo.txt  # Apenas linhas 10-20

# Buscar nos arquivos
git grep "TODO"               # Busca texto nos arquivos
git grep -n "function"        # Com número da linha
```

---

## 4. `.gitignore`

```gitignore
# Dependências
node_modules/
vendor/
__pycache__/
venv/

# Build
dist/
build/
.next/

# Ambiente
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*

# Cache
.cache/
*.pyc

# Uploads/Storage
storage/app/public/
uploads/
```

```bash
# Verificar o que seria ignorado
git status --ignored

# Forçar adicionar arquivo ignorado
git add -f arquivo-ignorado.env

# Remover arquivo já rastreado (depois de adicionar ao .gitignore)
git rm --cached arquivo.env
git commit -m "chore: remove arquivo do rastreamento"
```

---

## 5. Workflows (Estratégias de Branch)

### Git Flow (Projetos maiores)
```
main          ─────●─────────────────────●──── (produção)
                   │                     │
hotfix/fix-x      │  ●──●               │
                   │                     │
release/1.0       │     ●──●──●         │
                   │                     │
develop       ────●──●──●──●──●──●──●───●──── (integração)
                   │     │        │
feature/login     ●──●──●        │
feature/dashboard               ●──●──●
```

### GitHub Flow (Projetos menores — RECOMENDADO)
```bash
# 1. Criar branch da feature
git switch -c feature/login

# 2. Trabalhar e commitar
git add .
git commit -m "feat: adiciona tela de login"

# 3. Push para o remoto
git push -u origin feature/login

# 4. Abrir Pull Request no GitHub

# 5. Após aprovação, merge via GitHub

# 6. Atualizar local
git switch main
git pull origin main
git branch -d feature/login
```

### Trunk-Based (Times com CI/CD)
```bash
# Trabalhar direto na main com commits pequenos e frequentes
git switch main
git pull
# ... trabalhar ...
git commit -m "feat: botão de logout"
git push
```

---

## 6. Convenção de Commits (Conventional Commits)

```
<tipo>(<escopo>): <descrição>

[corpo opcional]

[rodapé opcional]
```

### Tipos
| Tipo | Quando usar |
|---|---|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Documentação |
| `style` | Formatação (espaços, semicolons, etc.) |
| `refactor` | Refatoração (sem mudar funcionalidade) |
| `test` | Adicionar/corrigir testes |
| `chore` | Build, CI, dependências, configs |
| `perf` | Melhoria de performance |
| `ci` | Alterações no CI/CD |

### Exemplos
```bash
git commit -m "feat: adiciona autenticação JWT"
git commit -m "fix: corrige validação de email no cadastro"
git commit -m "docs: atualiza README com instruções de deploy"
git commit -m "refactor: extrai lógica de validação para service"
git commit -m "chore: atualiza dependências do npm"
git commit -m "test: adiciona testes unitários para UserService"
git commit -m "feat(auth): implementa login com Google OAuth"
git commit -m "fix(api): corrige paginação na listagem de usuários"
```

---

## 7. Resolução de Conflitos

```bash
# Após merge/rebase com conflito
git status  # Mostra arquivos com conflito

# Abrir arquivo com conflito — vai ter:
<<<<<<< HEAD
código da sua branch
=======
código da outra branch
>>>>>>> feature/outra

# Resolver:
# 1. Editar o arquivo (remover marcadores e manter o código correto)
# 2. git add arquivo.txt
# 3. git merge --continue   (ou git rebase --continue)
```

---

## 8. Desfazendo Coisas (Receitas de Emergência)

```bash
# ❌ "Commitei na branch errada"
git switch branch-correta
git cherry-pick abc1234          # Copiar commit
git switch branch-errada
git reset --hard HEAD~1          # Remover da branch errada

# ❌ "Quero desfazer o último commit mas manter as mudanças"
git reset --soft HEAD~1

# ❌ "Quero desfazer TUDO e voltar ao último commit"
git reset --hard HEAD
git clean -fd                    # Remove arquivos não rastreados

# ❌ "Fiz push de algo errado"
git revert abc1234               # Cria commit invertido (seguro)
git push origin main

# ❌ "Deletei uma branch sem querer"
git reflog                       # Encontrar o hash
git switch -c branch-recuperada abc1234

# ❌ "Preciso voltar a um commit antigo temporariamente"
git switch --detach abc1234       # Modo detached HEAD
git switch main                   # Voltar

# ❌ "Quero ignorar um arquivo que já está no Git"
git rm --cached config.env
echo "config.env" >> .gitignore
git commit -m "chore: remove config.env do rastreamento"
```

---

## 9. Hooks (Automação)

```bash
# Hooks ficam em .git/hooks/
# Exemplos úteis:

# pre-commit — Roda antes do commit
#!/bin/sh
npm run lint && npm test
# Se falhar, o commit é cancelado

# commit-msg — Valida mensagem
#!/bin/sh
if ! grep -qE "^(feat|fix|docs|style|refactor|test|chore|perf|ci)" "$1"; then
  echo "❌ Mensagem deve seguir Conventional Commits"
  exit 1
fi
```

### Husky (Hooks fáceis via npm)
```bash
npm install -D husky
npx husky init

# Criar hook
echo "npm test" > .husky/pre-commit
echo "npx commitlint --edit \$1" > .husky/commit-msg
```

---

## 10. Cheatsheet Rápido

| Ação | Comando |
|---|---|
| Ver estado | `git status` |
| Adicionar tudo | `git add .` |
| Commitar | `git commit -m "msg"` |
| Push | `git push` |
| Pull | `git pull` |
| Nova branch | `git switch -c nome` |
| Mudar branch | `git switch nome` |
| Merge | `git merge nome` |
| Log bonito | `git log --oneline --graph --all` |
| Desfazer mudanças | `git restore arquivo` |
| Desfazer add | `git restore --staged arquivo` |
| Desfazer commit (manter mudanças) | `git reset --soft HEAD~1` |
| Guardar temporário | `git stash` |
| Recuperar stash | `git stash pop` |
| Ver diferenças | `git diff` |
| Quem mudou | `git blame arquivo` |
| Buscar texto | `git grep "texto"` |

---

*Fonte: [git-scm.com/docs](https://git-scm.com/docs) — Consultado em 2026-02-14*
