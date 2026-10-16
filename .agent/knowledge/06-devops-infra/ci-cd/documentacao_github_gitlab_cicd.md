---json
{
  "id": "documentacao_github_gitlab_cicd",
  "title": "GitHub REST API & GitLab CI/CD — Guia Completo",
  "categoria": "06-devops-infra",
  "subcategoria": "ci-cd",
  "resumo": "Guia tecnico e referencias sobre GitHub REST API & GitLab CI/CD — Guia Completo.",
  "gatilhos": [
    "api",
    "cicd",
    "completo",
    "devops",
    "documentacao",
    "github",
    "gitlab",
    "guia"
  ],
  "perguntas_tipo": [
    "Como utilizar GitHub REST API & GitLab CI/CD — Guia Completo?",
    "Quais as boas praticas de ci-cd?"
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
  "dono": "stack-ci-cd",
  "prioridade": 2
}
---

# GitHub REST API & GitLab CI/CD — Guia Completo

**Fontes:**
- [docs.github.com/en/rest](https://docs.github.com/en/rest?apiVersion=2022-11-28)
- [docs.gitlab.com/ci](https://docs.gitlab.com/ci/)

**Versão:** GitHub API v2022-11-28 · GitLab CI latest  
**Categoria:** CI/CD · APIs · DevOps  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

# Parte 1: GitHub REST API

## 1. Autenticação

### Personal Access Token (PAT)
```bash
# Header Authorization
curl -H "Authorization: Bearer ghp_SEU_TOKEN_AQUI" \
     -H "Accept: application/vnd.github+json" \
     -H "X-GitHub-Api-Version: 2022-11-28" \
     https://api.github.com/user
```

### Via JavaScript (fetch)
```javascript
const GITHUB_TOKEN = process.env.GITHUB_TOKEN

async function githubApi(endpoint, options = {}) {
  const res = await fetch(`https://api.github.com${endpoint}`, {
    headers: {
      'Authorization': `Bearer ${GITHUB_TOKEN}`,
      'Accept': 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
      ...options.headers,
    },
    ...options,
  })

  if (!res.ok) throw new Error(`GitHub API: ${res.status}`)
  return res.json()
}
```

---

## 2. Endpoints Principais

### Repositórios
```bash
# Listar repos do usuário autenticado
GET /user/repos?sort=updated&per_page=30

# Listar repos de um usuário
GET /users/{username}/repos

# Detalhes de um repo
GET /repos/{owner}/{repo}

# Criar repo
POST /user/repos
{
  "name": "meu-projeto",
  "description": "Descrição do projeto",
  "private": true
}

# Listar branches
GET /repos/{owner}/{repo}/branches

# Listar commits
GET /repos/{owner}/{repo}/commits?per_page=10
```

### Issues
```bash
# Listar issues
GET /repos/{owner}/{repo}/issues?state=open

# Criar issue
POST /repos/{owner}/{repo}/issues
{
  "title": "Bug no login",
  "body": "Descrição detalhada...",
  "labels": ["bug", "priority-high"]
}

# Fechar issue
PATCH /repos/{owner}/{repo}/issues/{issue_number}
{ "state": "closed" }
```

### Pull Requests
```bash
# Listar PRs
GET /repos/{owner}/{repo}/pulls?state=open

# Criar PR
POST /repos/{owner}/{repo}/pulls
{
  "title": "feat: adiciona login",
  "body": "Implementa login com JWT",
  "head": "feature/login",
  "base": "main"
}

# Merge PR
PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge
{ "merge_method": "squash" }
```

### Releases
```bash
# Listar releases
GET /repos/{owner}/{repo}/releases

# Criar release
POST /repos/{owner}/{repo}/releases
{
  "tag_name": "v1.0.0",
  "name": "Release 1.0.0",
  "body": "## Changelog\n- feat: login\n- fix: validação",
  "draft": false,
  "prerelease": false
}
```

### GitHub Actions (Workflows)
```bash
# Listar workflows
GET /repos/{owner}/{repo}/actions/workflows

# Listar runs de um workflow
GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs

# Disparar workflow manualmente
POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches
{ "ref": "main" }

# Ver logs de um run
GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs
```

---

## 3. Paginação

```javascript
// A API retorna no máximo 30 itens por padrão (max 100)
// Use per_page e page para paginar

async function getAllRepos(username) {
  let page = 1
  let allRepos = []

  while (true) {
    const repos = await githubApi(
      `/users/${username}/repos?per_page=100&page=${page}`
    )
    if (repos.length === 0) break
    allRepos = allRepos.concat(repos)
    page++
  }

  return allRepos
}
```

---

## 4. Rate Limits

```bash
# Verificar rate limit
GET /rate_limit

# Resposta:
# - 5000 requests/hora (autenticado)
# - 60 requests/hora (não autenticado)
```

---

## 5. Exemplo Prático: Script Node.js

```javascript
// scripts/github-summary.js
const token = process.env.GITHUB_TOKEN
const owner = 'meu-usuario'
const repo = 'meu-projeto'

async function api(path) {
  const res = await fetch(`https://api.github.com${path}`, {
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: 'application/vnd.github+json',
    },
  })
  return res.json()
}

async function main() {
  // Info do repo
  const repoInfo = await api(`/repos/${owner}/${repo}`)
  console.log(`⭐ Stars: ${repoInfo.stargazers_count}`)
  console.log(`🍴 Forks: ${repoInfo.forks_count}`)

  // Issues abertas
  const issues = await api(`/repos/${owner}/${repo}/issues?state=open`)
  console.log(`🐛 Issues abertas: ${issues.length}`)

  // PRs abertos
  const prs = await api(`/repos/${owner}/${repo}/pulls?state=open`)
  console.log(`🔀 PRs abertos: ${prs.length}`)

  // Última release
  const releases = await api(`/repos/${owner}/${repo}/releases?per_page=1`)
  if (releases.length > 0) {
    console.log(`📦 Última release: ${releases[0].tag_name}`)
  }
}

main()
```

---

# Parte 2: GitLab CI/CD

## 1. O que é GitLab CI/CD?

Sistema de **integração e deploy contínuo** integrado ao GitLab. Definido por um arquivo `.gitlab-ci.yml` na raiz do projeto.

---

## 2. Exemplo Básico

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy

# ==============================
# BUILD
# ==============================
build_app:
  stage: build
  image: node:20-alpine
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour

# ==============================
# TESTS
# ==============================
unit_tests:
  stage: test
  image: node:20-alpine
  script:
    - npm ci
    - npm test -- --coverage
  coverage: '/All files\s*\|\s*([\d.]+)/'
  artifacts:
    reports:
      junit: test-results.xml

lint:
  stage: test
  image: node:20-alpine
  script:
    - npm ci
    - npm run lint

# ==============================
# DEPLOY
# ==============================
deploy_staging:
  stage: deploy
  image: alpine
  script:
    - echo "Deploying to staging..."
    - ./deploy.sh staging
  environment:
    name: staging
    url: https://staging.meuapp.com
  only:
    - develop

deploy_production:
  stage: deploy
  image: alpine
  script:
    - echo "Deploying to production..."
    - ./deploy.sh production
  environment:
    name: production
    url: https://meuapp.com
  only:
    - main
  when: manual   # Requer clique manual para deploy
```

---

## 3. Variáveis CI/CD

```yaml
variables:
  NODE_ENV: production
  DATABASE_URL: $DB_URL   # Do GitLab Settings > CI/CD > Variables

job_name:
  script:
    - echo $CI_COMMIT_SHA            # Hash do commit
    - echo $CI_COMMIT_BRANCH         # Nome da branch
    - echo $CI_PIPELINE_ID           # ID do pipeline
    - echo $CI_PROJECT_NAME          # Nome do projeto
    - echo $CI_MERGE_REQUEST_IID     # ID do MR
```

### Variáveis Predefinidas Úteis

| Variável | Valor |
|---|---|
| `CI_COMMIT_SHA` | Hash completo do commit |
| `CI_COMMIT_SHORT_SHA` | Hash curto (8 chars) |
| `CI_COMMIT_BRANCH` | Nome da branch |
| `CI_COMMIT_TAG` | Nome da tag (se tag) |
| `CI_PIPELINE_ID` | ID do pipeline |
| `CI_PROJECT_NAME` | Nome do projeto |
| `CI_MERGE_REQUEST_IID` | ID do Merge Request |
| `CI_JOB_TOKEN` | Token temporário do job |

---

## 4. Pipeline Laravel + Next.js

```yaml
# .gitlab-ci.yml — Stack completa
stages:
  - install
  - test
  - build
  - deploy

variables:
  MYSQL_ROOT_PASSWORD: root
  MYSQL_DATABASE: test_db

# ======= BACKEND LARAVEL =======
backend_install:
  stage: install
  image: php:8.3-fpm
  script:
    - apt-get update && apt-get install -y git zip
    - curl -sS https://getcomposer.org/installer | php
    - php composer.phar install --no-dev
  artifacts:
    paths:
      - vendor/

backend_test:
  stage: test
  image: php:8.3-fpm
  services:
    - mysql:8.0
  variables:
    DB_HOST: mysql
    DB_DATABASE: test_db
    DB_USERNAME: root
    DB_PASSWORD: root
  script:
    - php artisan migrate --force
    - php artisan test --parallel
  dependencies:
    - backend_install

# ======= FRONTEND NEXT.JS =======
frontend_install:
  stage: install
  image: node:20-alpine
  script:
    - cd frontend
    - npm ci
  artifacts:
    paths:
      - frontend/node_modules/

frontend_test:
  stage: test
  image: node:20-alpine
  script:
    - cd frontend
    - npm test -- --coverage
  dependencies:
    - frontend_install

frontend_build:
  stage: build
  image: node:20-alpine
  script:
    - cd frontend
    - npm run build
  artifacts:
    paths:
      - frontend/.next/
  dependencies:
    - frontend_install

# ======= DEPLOY =======
deploy:
  stage: deploy
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker compose -f docker-compose.prod.yml build
    - docker compose -f docker-compose.prod.yml push
    - ssh deploy@server "cd /app && docker compose pull && docker compose up -d"
  only:
    - main
  when: manual
```

---

## 5. Cache e Artifacts

```yaml
# Cache: reutiliza entre pipelines (dependências)
frontend_test:
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
  script:
    - npm ci
    - npm test

# Artifacts: passa entre jobs do MESMO pipeline
build:
  artifacts:
    paths:
      - dist/
    expire_in: 1 week
    reports:
      junit: test-results.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura.xml
```

---

## 6. Rules (Controle de Execução)

```yaml
# Só roda em merge requests
test:
  rules:
    - if: $CI_MERGE_REQUEST_IID
      when: always
    - when: never

# Só roda quando tem mudanças em pasta específica
backend_test:
  rules:
    - changes:
        - backend/**/*
        - composer.json
      when: always
    - when: never

# Só roda em tags
deploy:
  rules:
    - if: $CI_COMMIT_TAG
      when: manual
```

---

## 7. GitHub Actions vs GitLab CI — Comparação

| Aspecto | GitHub Actions | GitLab CI |
|---|---|---|
| **Arquivo** | `.github/workflows/*.yml` | `.gitlab-ci.yml` |
| **Nome de etapa** | `jobs` | `stages` + `jobs` |
| **Trigger** | `on: push, pull_request` | `only/except` ou `rules` |
| **Variáveis** | `${{ secrets.TOKEN }}` | `$TOKEN` |
| **Cache** | `actions/cache@v3` | `cache:` nativo |
| **Artifacts** | `actions/upload-artifact` | `artifacts:` nativo |
| **Deploy manual** | `environment:` | `when: manual` |
| **Services** | `services:` em jobs | `services:` nativo |

---

## 8. GitHub Actions — Exemplo Equivalente

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: root
          MYSQL_DATABASE: test_db
        ports:
          - 3306:3306

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm

      - name: Install & Test
        run: |
          npm ci
          npm test -- --coverage

      - name: Setup PHP
        uses: shivammathur/setup-php@v2
        with:
          php-version: 8.3

      - name: Laravel Tests
        run: |
          composer install --no-dev
          php artisan test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        run: ./deploy.sh production
```

---

*Fontes: [docs.github.com/en/rest](https://docs.github.com/en/rest?apiVersion=2022-11-28) · [docs.gitlab.com/ci](https://docs.gitlab.com/ci/) — Acessado em 2026-02-14*
