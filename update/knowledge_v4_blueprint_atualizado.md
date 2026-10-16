# 🏗️ Blueprint Oficial: Knowledge v4.0 (`.agent/knowledge`)
**Roteamento Hierárquico, Busca Híbrida e Eficiência Máxima de Tokens — Construção do Zero**

> **Destino:** `d:\xampp\htdocs\0-fonte\.agent\knowledge` (reconstrução limpa)
> **Diagnóstico anterior:** 170.075 arquivos (~1,86 GB) contaminados por `node_modules`, `.venv`, `.pyc` e repositórios clonados em `02_ESTRUTURA_IA`, `03_CONHECIMENTO` e `06_LAB_EXEMPLOS`.
> **Meta:** ~6.450 arquivos essenciais (~35 MB), 0% de código executável ou dependências, e leitura inicial da IA de **centenas de tokens** (antes: ~20.000 do `INDICE_GERAL.md`).
> **O que muda em relação ao rascunho anterior:** o modelo de 3 camadas fixas não comporta 6.421 manuais. Esta versão usa **índices hierárquicos gerados por código**, **busca híbrida** que devolve só os 3 melhores candidatos, **seções endereçáveis**, **dados tabulares em SQLite** e **CI de validação**.

---

## 1. Princípios de Engenharia

1. **Carregar o mínimo, no nível mais raso possível.** Cada índice só é aberto se o nível acima bater.
2. **Custo O(log N).** Nenhum índice lista mais de ~40 rotas; acima disso, divide-se em subpastas.
3. **Dois caminhos para chegar ao manual:**
   * **Navegação:** Mestre → Domínio → Grupo → Stack → Manual.
   * **Atalho por busca:** `buscar_rota(pergunta)` devolve o top-3 e pula direto para o nível certo.
4. **Granularidade endereçável.** A IA carrega a **seção** (`arquivo.md#secao`) ou a **linha** (consulta SQL), não o arquivo inteiro.
5. **Índices nunca são escritos à mão.** Cada manual declara seus metadados no front matter e o build gera todos os `_index.md`.
6. **Formato pelo menor consumo de tokens**, medido com os seus dados reais (seção 8).

---

## 2. Os Níveis de Contexto

| Nível | Arquivo | Conteúdo | Quando é lido | Orçamento |
|---|---|---|---|---|
| **0 — Mestre** | `_meta/00_MASTER_ROUTER.md` | Só os 6 domínios + regras do agente | Sempre (prefixo cacheável) | ≤ 700 tokens |
| **1 — Domínio** | `<dominio>/_index.md` | Grupos do domínio | Se o domínio bater | ≤ 600 tokens |
| **2 — Grupo** | `<dominio>/<grupo>/_index.md` | Stacks / temas do grupo | Se o grupo bater | ≤ 800 tokens |
| **3 — Stack/Tema** | `<grupo>/<stack>/_index.md` | Manuais da stack (com seções e `tokens_estimados`) | Só quando a pasta tem > 8 manuais | ≤ 1.200 tokens |
| **4 — Conteúdo** | `.md` / `.csv` / `.yaml` | Manual final | Só a **seção** ou **linha** necessária | ≤ 2.000 tokens por arquivo |

> **Correção do rascunho anterior:** o Roteador Mestre com 6 domínios e listas de gatilhos pesa de 400 a 700 tokens, não ~85. Continua ~97% menor que o `INDICE_GERAL.md` de 78 KB, mas o número deve ser **medido** (seção 8), não estimado.

**Regra de ouro dos índices:** máximo de **40 rotas por `_index.md`**. Passou disso, o build falha e a pasta deve ser subdividida.

---

## 3. Nova Árvore de Diretórios (Nova Divisão)

Convenção: pastas com **prefixo `_`** são infraestrutura (governança, dados, build); pastas **numeradas** são conteúdo.

```plaintext
d:\xampp\htdocs\0-fonte\.agent\knowledge\
│
├── .ignore                                   # bloqueio rigoroso (ver seção 9)
│
├── _meta/                                    # GOVERNANÇA E CONTROLE
│   ├── 00_MASTER_ROUTER.md                   # Nível 0 (GERADO pelo build)
│   ├── schema_frontmatter.md                 # padrão obrigatório de metadados dos manuais
│   ├── orcamento_contexto.yaml               # limites de tokens por nível e por pergunta
│   ├── build/
│   │   ├── gerar_indices.py                  # gera todos os _index.md + MASTER_ROUTER
│   │   ├── validar.py                        # CI: links, órfãos, duplicatas, tamanho
│   │   ├── medir_tokens.py                   # mede tokens reais por formato/arquivo
│   │   └── indexar_busca.py                  # popula o índice FTS5 (e embeddings, opcional)
│   ├── logs/
│   │   └── consultas.csv                     # rota escolhida, tokens carregados, houve resposta?
│   └── scripts/                              # utilitários MCP (apenas scripts leves)
│       ├── mcp_doctor.ps1
│       ├── mcp_status.ps1
│       └── start_mcp_factory.ps1
│
├── _dados/                                   # DADOS TABULARES (nunca lidos inteiros)
│   ├── csv/
│   │   ├── catalogo_stacks.csv               # as 46 tecnologias Tier 1 e Tier 2
│   │   ├── registro_fontes.csv               # antigo REGISTRO_FONTES.md
│   │   ├── codigos_http.csv
│   │   └── catalogo_erros.csv
│   └── knowledge.sqlite                      # GERADO: tabelas dos CSVs + índice FTS5 das rotas
│
├── 01_gestao_produto/                        # DOMÍNIO 1: produto, processos e liderança
│   ├── _index.md
│   ├── startup_produto/                      # GStack, discovery, tração, métricas
│   ├── sdlc_agil/                            # ciclo de vida, rituais, revisão de código
│   ├── arquitetura_software/                 # padrões, ADRs, trade-offs
│   └── lideranca_engenharia/                 # padrões e práticas (Addy Osmani)
│
├── 02_arquitetura_ia/                        # DOMÍNIO 2: agentes e contexto (SEM SERVIDORES INSTALADOS)
│   ├── _index.md
│   ├── mcp/                                  # protocolo, schemas leves, boas práticas
│   ├── memoria_agentes/                      # Graphiti, Claude-Mem, Codebase Memory
│   ├── gateways_cli/                         # OmniRoute, AnyDoc Parser, Plandex
│   ├── prompts_contexto/                     # engenharia de contexto, system prompts
│   └── rag_busca/                            # embeddings, FTS, chunking, ranking híbrido
│
├── 03_linguagens_frameworks/                 # DOMÍNIO 3: manuais Tier 1 e Tier 2 (SEM PROJETOS CLONADOS)
│   ├── _index.md                             # lista só os 4 grupos
│   ├── backend/
│   │   ├── _index.md                         # lista as stacks do grupo
│   │   ├── php_laravel/   (_index.md + manuais por tema)
│   │   ├── python/
│   │   ├── nodejs/
│   │   ├── go/
│   │   ├── java/
│   │   ├── rust/
│   │   └── csharp_dotnet/
│   ├── frontend/
│   │   ├── _index.md
│   │   ├── react/
│   │   ├── nextjs/
│   │   ├── vue/
│   │   ├── angular/
│   │   ├── tailwind/
│   │   └── typescript/
│   ├── mobile/
│   │   ├── _index.md
│   │   ├── flutter/
│   │   ├── react_native/
│   │   ├── swift/
│   │   └── kotlin/
│   └── dados/
│       ├── _index.md
│       ├── postgresql/
│       ├── mongodb/
│       ├── redis/
│       ├── prisma/
│       └── sql_geral/
│
├── 04_infra_devops/                          # DOMÍNIO 4: containers, servidores, observabilidade
│   ├── _index.md
│   ├── containers/                           # Docker, Compose, Kubernetes
│   ├── ci_cd/                                # GitHub Actions, GitLab CI, estratégias de deploy
│   ├── cloud/                                # conceitos e receitas por provedor
│   ├── servidores_linux/                     # Nginx, proxy reverso, Linux, systemd
│   ├── observabilidade/                      # Zabbix, logs, métricas, alertas
│   └── ambiente_local/                       # XAMPP, Windows, PowerShell, WSL
│
├── 05_seguranca/                             # DOMÍNIO 5: AppSec, hardening e auditoria
│   ├── _index.md
│   ├── appsec_owasp/                         # OWASP Top 10, mitigações
│   ├── autenticacao_autorizacao/             # JWT, OAuth2, sessões, RBAC
│   ├── hardening/                            # servidores, containers, banco
│   ├── siem_auditoria/                       # Wazuh, logs de auditoria, detecção
│   └── checklists_defensivos/                # revisões de segurança por tipo de projeto
│
└── 06_exemplos_receitas/                     # DOMÍNIO 6: snippets e integrações (SEM REPOSITÓRIOS CLONADOS)
    ├── _index.md
    ├── integracoes_apis/                     # Evolution API, webhooks, REST
    ├── snippets/                             # padrões curtos por linguagem
    └── receitas_ponta_a_ponta/               # passo a passo completo (ex.: webhook → fila → resposta)
```

### O que mudou na divisão (e por quê)

| Mudança | Motivo |
|---|---|
| `03` passa a ter **uma pasta por stack**, cada uma com seu `_index.md` | Com ~46 stacks e milhares de manuais, um único `_index.md` do domínio passaria de 40 rotas e estouraria o orçamento |
| Nome dos domínios simplificado (`05_seguranca`, `06_exemplos_receitas`) | Curtos e sem ambiguidade para gatilhos e caminhos |
| Novo grupo `02/rag_busca` | A própria base usa busca híbrida; a documentação do mecanismo deve estar nela |
| Novo grupo `04/ambiente_local` | O cenário real é Windows + XAMPP + PowerShell, que merecem manuais próprios |
| Novas pastas `_meta/build`, `_dados`, `_meta/logs` | Separam infraestrutura de conteúdo; só o conteúdo numerado é indexado como manual |
| `catalogo_46_stacks.csv` e `registro_fontes.csv` movidos para `_dados/csv/` | Dados tabulares ficam num lugar só e viram tabelas SQLite, consultadas por filtro |

---

## 4. Padrão de Metadados (Front Matter dos Manuais)

Cada manual `.md` declara seus próprios metadados. **É a única fonte de verdade**: o build lê isso e gera todos os índices.

```markdown
---
id: laravel_eloquent_relacoes
resumo: Relacionamentos Eloquent (hasMany, belongsTo, morph) e eager loading.
gatilhos: [eloquent, relacionamento, hasmany, belongsto, with, eager loading, n+1]
perguntas_tipo:
  - "Como evitar o problema N+1 no Laravel?"
  - "Como definir um relacionamento muitos-para-muitos?"
nao_cobre: [migrations, filas, cache]
tier: 1
versao_tecnologia: "12.x"
atualizado_em: 2026-09-20
fonte: docs oficiais Laravel
dono: stack-backend
prioridade: 1
depende_de: [laravel_eloquent_basico]
---
# Relacionamentos Eloquent
> Resumo: tipos de relação, eager loading e prevenção de N+1.
> Seções: tipos-de-relacao · eager-loading · constraints · morph

## Tipos de relação
...
```

| Campo | Obrigatório | Função |
|---|---|---|
| `id` | ✅ | Identificador único e estável |
| `resumo` | ✅ | 1 linha; base do roteamento |
| `gatilhos` | ✅ | Palavras-chave **e sinônimos** (inclua termos em PT-BR e EN) |
| `perguntas_tipo` | recomendado | 2–3 perguntas reais; melhora a busca semântica |
| `nao_cobre` | recomendado | Exclusões que evitam falsos positivos entre manuais parecidos |
| `tier` | ✅ (domínio 03) | 1 = Deep Dive, 2 = referência |
| `versao_tecnologia` | recomendado | Versão da tecnologia documentada |
| `atualizado_em` | ✅ | Detecta conteúdo velho |
| `dono` | ✅ | Responsável pela correção |
| `prioridade` / `depende_de` | opcional | Desempate e carga em cadeia |
| `tokens_estimados`, `secoes` | **gerados** pelo build | Não preencher à mão |

**Mini-sumário no topo do corpo** (3 linhas) é obrigatório em manuais acima de 800 tokens: permite à IA decidir se continua lendo.

---

## 5. Templates Reais

### Template 1 — Roteador Mestre (`_meta/00_MASTER_ROUTER.md`) — GERADO

```markdown
---
ecossistema: AllMight Knowledge v4.0
caminho_raiz: d:/xampp/htdocs/0-fonte/.agent/knowledge
regra_agente: >
  NUNCA faça varredura cega de pastas.
  Passo 1: tente buscar_rota(pergunta). Se devolver candidatos, escolha entre eles.
  Passo 2: sem a ferramenta, identifique o domínio pelos gatilhos abaixo.
  Passo 3: leia APENAS o indice do domínio e desça um nível por vez.
  Passo 4: carregue só a SEÇÃO (arquivo.md#secao) ou a LINHA (consultar_dados).
  Se a pergunta não exigir nenhum domínio, responda direto.
orcamento: {max_arquivos: 3, max_tokens_carga: 6000}
dominios:
  - id: dom_01_gestao
    resumo: Produto, startup, SDLC ágil, arquitetura de software e liderança.
    gatilhos: [sdlc, produto, startup, gstack, agilidade, adr, code review, addy osmani]
    indice: ./01_gestao_produto/_index.md

  - id: dom_02_ia
    resumo: MCP, memória de agentes, gateways, prompts, RAG e busca.
    gatilhos: [mcp, memoria, graphiti, claude-mem, omniroute, plandex, prompt, agente, rag, embeddings]
    indice: ./02_arquitetura_ia/_index.md

  - id: dom_03_stacks
    resumo: Manuais de linguagens, frameworks e bancos (46 stacks).
    gatilhos: [laravel, php, python, node, go, java, rust, react, nextjs, vue, tailwind, typescript, flutter, postgres, redis, prisma]
    indice: ./03_linguagens_frameworks/_index.md

  - id: dom_04_infra
    resumo: Containers, CI/CD, cloud, servidores Linux, observabilidade, ambiente local.
    gatilhos: [docker, kubernetes, nginx, zabbix, ci/cd, deploy, linux, xampp, powershell]
    indice: ./04_infra_devops/_index.md

  - id: dom_05_seguranca
    resumo: OWASP, autenticação, hardening, SIEM e checklists defensivos.
    gatilhos: [owasp, seguranca, vulnerabilidade, jwt, oauth2, hardening, wazuh]
    indice: ./05_seguranca/_index.md

  - id: dom_06_receitas
    resumo: Integrações de API, snippets e receitas ponta a ponta.
    gatilhos: [evolution api, whatsapp, webhook, snippet, exemplo, integracao]
    indice: ./06_exemplos_receitas/_index.md

dados_tabulares:
  banco: ./_dados/knowledge.sqlite
  tabelas: [catalogo_stacks, registro_fontes, codigos_http, catalogo_erros]
manutencao_mcp:
  diagnostico: ./_meta/scripts/mcp_doctor.ps1
  status: ./_meta/scripts/mcp_status.ps1
  inicializador: ./_meta/scripts/start_mcp_factory.ps1
---
```

### Template 2 — Índice de Domínio (`03_linguagens_frameworks/_index.md`) — GERADO
Lista **só os grupos**, não as stacks. O detalhe das stacks fica um nível abaixo.

```markdown
---
dominio: 03_linguagens_frameworks
resumo: Manuais Tier 1 (Deep Dive) e Tier 2 de linguagens, frameworks e bancos.
regra: Escolha o grupo e abra o seu _index.md.
grupos:
  - id: g03_backend
    resumo: PHP/Laravel, Python, Node.js, Go, Java, Rust, C#/.NET.
    gatilhos: [laravel, php, python, fastapi, node, nestjs, go, java, rust, csharp, dotnet]
    indice: ./backend/_index.md

  - id: g03_frontend
    resumo: React, Next.js, Vue, Angular, Tailwind, TypeScript.
    gatilhos: [react, nextjs, vue, angular, tailwind, typescript, css, ssr]
    indice: ./frontend/_index.md

  - id: g03_mobile
    resumo: Flutter, React Native, Swift, Kotlin.
    gatilhos: [flutter, dart, react native, swift, kotlin, android, ios]
    indice: ./mobile/_index.md

  - id: g03_dados
    resumo: PostgreSQL, MongoDB, Redis, Prisma, SQL geral.
    gatilhos: [postgres, mongodb, redis, prisma, sql, query, indice, migration]
    indice: ./dados/_index.md
---
```

### Template 3 — Índice de Grupo (`03_linguagens_frameworks/backend/_index.md`) — GERADO

```markdown
---
grupo: backend
resumo: Linguagens e frameworks de servidor.
stacks:
  - id: s_laravel
    stack: PHP / Laravel
    tier: 1
    resumo: Eloquent, filas, service container, Octane, testes.
    gatilhos: [laravel, eloquent, blade, artisan, middleware, fila, octane]
    indice: ./php_laravel/_index.md
    manuais: 142

  - id: s_python
    stack: Python
    tier: 1
    resumo: FastAPI, asyncio, tipagem, Pydantic, packaging.
    gatilhos: [python, fastapi, asyncio, pydantic, venv, pip]
    indice: ./python/_index.md
    manuais: 118
---
```

### Template 4 — Índice de Stack (`.../php_laravel/_index.md`) — GERADO
Só existe quando a pasta tem mais de 8 manuais. Cada rota já traz o tamanho e as seções.

```markdown
---
stack: PHP / Laravel
rotas:
  - id: laravel_eloquent_relacoes
    resumo: Relacionamentos Eloquent e eager loading.
    gatilhos: [eloquent, relacionamento, hasmany, with, n+1]
    nao_cobre: [migrations, filas]
    arquivo: ./eloquent_relacoes.md
    secoes: [tipos-de-relacao, eager-loading, constraints, morph]
    tokens_estimados: 1150
    atualizado_em: 2026-09-20
    depende_de: [laravel_eloquent_basico]

  - id: laravel_filas_horizon
    resumo: Filas, workers, retries e Horizon.
    gatilhos: [queue, job, worker, horizon, retry, failed_jobs]
    arquivo: ./filas_horizon.md
    secoes: [drivers, jobs, retries, horizon]
    tokens_estimados: 980
    atualizado_em: 2026-08-14
---
```

### Template 5 — CSV de catálogo (`_dados/csv/catalogo_stacks.csv`)
Textos curtos, sem vírgulas internas (usar `;` dentro dos campos). Acima de ~200 linhas **não é lido inteiro**: vira tabela SQLite.

```csv
id,tecnologia,categoria,tier,indice,topicos_principais
stk_01,Next.js,frontend,1,./03_linguagens_frameworks/frontend/nextjs/_index.md,App Router;RSC;Server Actions;Caching
stk_02,Node.js,backend,1,./03_linguagens_frameworks/backend/nodejs/_index.md,Event Loop;Streams;Cluster;Performance
stk_03,Laravel,backend,1,./03_linguagens_frameworks/backend/php_laravel/_index.md,Eloquent;Queues;Service Container;Octane
stk_04,Prisma,dados,1,./03_linguagens_frameworks/dados/prisma/_index.md,Schema;Migrations;Client;Otimizacao
stk_05,Tailwind v4,frontend,1,./03_linguagens_frameworks/frontend/tailwind/_index.md,Oxide;CSS-first config;Design Tokens
```

### Template 6 — Manual final (`06_exemplos_receitas/integracoes_apis/evolution_api_guia.md`)
Substitui os **5.265 arquivos** do repositório clonado da Evolution API por **1 arquivo** de ~200 tokens.

````markdown
---
id: rec_evolution_api_v2
resumo: Endpoints essenciais, payload mínimo e webhooks da Evolution API v2.
gatilhos: [evolution api, whatsapp, instancia, qr code, sendtext, webhook]
nao_cobre: [deploy do servidor da Evolution, banco de dados interno]
atualizado_em: 2026-09-01
dono: integracoes
---
# Guia Prático: Evolution API (v2)
> Seções: endpoints-essenciais · payload-minimo · webhooks

## Endpoints essenciais
- **Criar instância:** `POST /instance/create`
- **Conectar / QR Code:** `GET /instance/connect/{instance}`
- **Enviar texto:** `POST /message/sendText/{instance}`

## Payload mínimo
```json
{ "number": "5511999999999", "text": "Mensagem automática do agente" }
```

## Webhooks
Ative só o necessário para não sobrecarregar a fila:
- `MESSAGES_UPSERT` (mensagens recebidas)
- `CONNECTION_UPDATE` (queda ou reconexão de sessão)
````

---

## 6. Camada de Acesso: Ferramentas MCP da Base

A IA não deveria abrir pastas manualmente. Exponha 4 ferramentas no seu servidor MCP (fica **fora** de `knowledge/`, em `d:\xampp\htdocs\0-fonte\mcp-servers\`):

| Ferramenta | Entrada | Saída | Custo típico |
|---|---|---|---|
| `buscar_rota` | `pergunta`, `dominio?` | Top-3: `id`, `resumo`, `nao_cobre`, `caminho`, `tokens_estimados` | ~150 tokens |
| `ler_secao` | `arquivo`, `secao?` | Só a seção pedida (ou o mini-sumário se omitida) | Variável (≤ 2.000) |
| `consultar_dados` | `tabela`, `filtro` | Linhas filtradas do SQLite | 20–200 tokens |
| `registrar_consulta` | `rota`, `tokens`, `util` | Grava em `_meta/logs/consultas.csv` | ~0 |

### Busca híbrida (SQLite FTS5 + embeddings opcionais)

```sql
-- indexar_busca.py cria uma vez; 'remove_diacritics 2' trata acentos do PT-BR
CREATE VIRTUAL TABLE rotas USING fts5(
  id, resumo, gatilhos, perguntas_tipo, caminho UNINDEXED, nao_cobre UNINDEXED,
  tokenize = 'unicode61 remove_diacritics 2'
);

-- consulta usada por buscar_rota
SELECT id, caminho, bm25(rotas) AS score
FROM rotas WHERE rotas MATCH ?
ORDER BY score LIMIT 3;
```

* **Fase 1 (suficiente para começar):** só BM25/FTS5, que já resolve a maioria das consultas por termo técnico.
* **Fase 2 (quando houver falhas por sinônimo):** embeddings sobre `resumo + perguntas_tipo` das rotas (não do corpo dos manuais) e fusão de rankings (Reciprocal Rank Fusion) com o BM25.
* Os embeddings cobrem "não consigo entrar" → autenticação, algo que gatilhos exatos não pegam.

---

## 7. Geração e Validação Automáticas

### 7.1 `gerar_indices.py` (esqueleto)

```python
from pathlib import Path
from collections import Counter
import re, yaml

RAIZ = Path("d:/xampp/htdocs/0-fonte/.agent/knowledge")
FM = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
MAX_ROTAS = 40

def ler(p: Path):
    t = p.read_text(encoding="utf-8")
    m = FM.match(t)
    meta = yaml.safe_load(m.group(1)) if m else {}
    return meta, (t[m.end():] if m else t)

def tokens(texto: str) -> int:           # estimativa; troque por tiktoken se quiser
    return max(1, len(texto) // 4)

def secoes(corpo: str):
    return [re.sub(r"[^\w\- ]", "", h).strip().lower().replace(" ", "-")
            for h in re.findall(r"^## (.+)$", corpo, re.M)]

def gerar(pasta: Path):
    rotas, filhos = [], []
    for sub in sorted(p for p in pasta.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))):
        idx = gerar(sub)                  # bottom-up: filhos primeiro
        if idx:
            filhos.append({"id": idx["id"], "resumo": idx["resumo"],
                           "gatilhos": idx["gatilhos"], "indice": f"./{sub.name}/_index.md"})
    for md in sorted(pasta.glob("*.md")):
        if md.name.startswith("_"):
            continue
        meta, corpo = ler(md)
        if not meta.get("id"):
            print(f"AVISO: sem front matter -> {md}")
            continue
        rotas.append({**{k: meta[k] for k in ("id", "resumo", "gatilhos") if k in meta},
                      **{k: meta[k] for k in ("nao_cobre", "atualizado_em", "depende_de") if k in meta},
                      "arquivo": f"./{md.name}", "secoes": secoes(corpo),
                      "tokens_estimados": tokens(corpo)})
    entradas = filhos + rotas
    if not entradas:
        return None
    if len(entradas) > MAX_ROTAS:
        raise SystemExit(f"{pasta}: {len(entradas)} rotas (> {MAX_ROTAS}). Subdivida a pasta.")
    gat = Counter(g for e in entradas for g in e.get("gatilhos", []))
    idx = {"id": f"idx_{pasta.name}", "resumo": f"Índice de {pasta.name}",
           "gatilhos": [g for g, _ in gat.most_common(12)],
           ("grupos" if filhos else "rotas"): entradas}
    (pasta / "_index.md").write_text(
        "---\n" + yaml.safe_dump(idx, allow_unicode=True, sort_keys=False) + "---\n", encoding="utf-8")
    return idx
```

> Este esqueleto cobre o essencial. O resumo de cada pasta pode vir do front matter de um `_pasta.md` opcional, ou ser gerado por LLM no build e revisado por humano.

### 7.2 `validar.py` — regras de CI

| Verificação | Falha quando... |
|---|---|
| Links quebrados | `arquivo` ou `indice` aponta para algo inexistente |
| Órfãos | Há `.md` de conteúdo que nenhum índice referencia |
| Front matter | Falta `id`, `resumo`, `gatilhos`, `atualizado_em` ou `dono` |
| `id` duplicado | Dois manuais com o mesmo `id` |
| Gatilho em conflito | O mesmo gatilho em dois manuais irmãos sem `prioridade` ou `nao_cobre` |
| Tamanho do manual | Mais de 2.000 tokens (dividir por seção) |
| Tamanho do índice | Orçamento do nível excedido ou mais de 40 rotas |
| Extensões proibidas | Aparece `.js`, `.py`, `.pyc`, `.map`, `.lock`, `node_modules`, `.venv`, `.git` dentro de `knowledge/` |
| Conteúdo velho | `atualizado_em` mais antigo que o prazo do domínio |
| MDX residual | Sobrou `.mdx` ou tag JSX (`<Component />`) em `.md` |

---

## 8. Orçamento de Contexto, Cache e Medição

### `_meta/orcamento_contexto.yaml`

```yaml
por_pergunta:
  max_arquivos: 3
  max_tokens_carga: 6000
  se_estourar: carregar_apenas_secoes   # depois resumir ou pedir refinamento
por_nivel:
  mestre: 700
  dominio: 600
  grupo: 800
  stack: 1200
  manual: 2000
sessao:
  nao_recarregar_ids_ja_lidos: true
```

* **Cache de prompt:** o `00_MASTER_ROUTER.md` é estável; mantenha-o no início do prompt como prefixo cacheável e o conteúdo variável (pergunta, seções carregadas) no fim.
* **Memória de sessão:** guarde os `id` já carregados e referencie-os em vez de recarregar.
* **`depende_de`:** só carregue dependências se a pergunta exigir e o orçamento permitir.

### Meça antes de afirmar (`medir_tokens.py`)

As porcentagens do rascunho anterior (35% YAML vs JSON, 50% CSV vs JSON, 28% Markdown) são **ordens de grandeza**. Rode o medidor sobre uma amostra de ~50 arquivos reais e grave o resultado em `_meta/logs/`. Duas ressalvas conhecidas:

* CSV com campos de texto longo perde a vantagem (aspas e vírgulas escapadas).
* Para listas pequenas e heterogêneas, lista Markdown pode ser mais legível para o modelo com custo quase igual.

### Fluxo completo da consulta

```
1. Pergunta do usuário
2. Master Router (cacheado)  ou  buscar_rota(pergunta) → top-3
   └─ nenhum bate? → responder direto
3. Descer níveis: domínio → grupo → stack (só o que for necessário)
4. Escolher rota (gatilhos, perguntas_tipo, nao_cobre, prioridade)
5. ler_secao(arquivo, secao)  |  consultar_dados(tabela, filtro)
6. Conferir orçamento (≤ 3 arquivos / ~6k tokens)
7. Responder → registrar_consulta(rota, tokens, util)
```

---

## 9. Plano de Migração (170.075 → ~6.450 arquivos)

### Fase 0 — Segurança
1. Backup do `knowledge` antigo (ou renomear para `knowledge_old`).
2. Criar o `knowledge` novo **vazio**, só com a estrutura da seção 3.

### Fase 1 — `.ignore` (e também usar como lista de exclusão)

```plaintext
node_modules/
.venv/
venv/
__pycache__/
.git/
dist/
build/
*.pyc
*.map
*.lock
*.log
*.exe
*.dll
*.so
```

### Fase 2 — Cópia seletiva (simulação primeiro)
Copia **só** documentação, ignorando dependências. O `/L` apenas lista, sem copiar; remova-o quando o resultado estiver correto.

```powershell
robocopy "knowledge_old\03_CONHECIMENTO" "knowledge_staging\03" *.md *.mdx *.csv *.yaml `
  /S /L /NFL /NDL /XD node_modules .venv venv __pycache__ .git dist build
```

### Fase 3 — Classificação
* Mapear cada pasta antiga → nova pasta da seção 3 (tabela de-para em `_dados/csv/`).
* Repositórios clonados (ex.: Evolution API, 5.265 arquivos): **não migrar**; escrever 1 guia de receita (Template 6).
* Servidores MCP de `02_ESTRUTURA_IA` (116.660 arquivos): mover para `d:\xampp\htdocs\0-fonte\mcp-servers\`; em `02_arquitetura_ia/mcp/` ficam só os `.md` de documentação.

### Fase 4 — Normalização
* `.mdx` → `.md` (remover imports e tags JSX; preservar texto e blocos de código).
* Quebrar manuais acima de 2.000 tokens por seção `##`.
* Adicionar front matter (seção 4). Pode ser feito em lote: LLM propõe `resumo`, `gatilhos` e `perguntas_tipo`; humano revisa por amostragem.
* Converter `REGISTRO_FONTES.md` e `folder_map.json` úteis para CSV; descartar os demais `.json`.

### Fase 5 — Build e validação
`gerar_indices.py` → `validar.py` → `indexar_busca.py` → `medir_tokens.py`. Só promover para produção com o CI verde.

### Fase 6 — Virada
Apontar o agente para `00_MASTER_ROUTER.md` e para as 4 ferramentas MCP; ligar `registrar_consulta`.

### Fase 7 — Operação contínua
Revisar semanalmente: perguntas sem rota (gatilhos faltando), rotas nunca usadas (remover ou fundir), colisões (adicionar `nao_cobre`).

---

## 10. Regra de Conversão: Cenário Antigo → Knowledge v4.0

| No AllMight antigo | No Knowledge v4.0 | Efeito |
|---|---|---|
| `INDICE_GERAL.md` (78 KB, ~20.000 tokens) | `00_MASTER_ROUTER.md` gerado (≤ 700 tokens) + índices por nível | ~97% menos tokens na leitura inicial |
| `folder_map.json` (e demais JSON de mapa) | `_index.md` com YAML front matter, **gerados** pelo build | Menos tokens que JSON e zero manutenção manual |
| 7.297 arquivos `.json` | Mantidos só se forem dados úteis (viram CSV/SQLite); o resto é descartado | Menos ruído e menos arquivos |
| `REGISTRO_FONTES.md` | `_dados/csv/registro_fontes.csv` + tabela SQLite | Consulta por filtro, não leitura inteira |
| 6.421 `.md` + 1.067 `.mdx` | `.md` puro, ≤ 2.000 tokens, com front matter, organizados nas pastas da seção 3 | Roteáveis, endereçáveis por seção |
| Servidores MCP em `02_ESTRUTURA_IA` (116.660 arquivos) | Movidos para `mcp-servers/` fora de `knowledge/` | −1,12 GB removido da base de leitura |
| Repositórios clonados em `03_CONHECIMENTO` e `06_LAB_EXEMPLOS` (ex.: Evolution API, 5.265 arquivos) | 1 receita `.md` por integração | Milhares de arquivos viram um |
| `node_modules`, `.venv`, `.pyc` | Bloqueados por `.ignore` e pela regra de CI | 0% de dependências |
| Sem controle de consumo | `orcamento_contexto.yaml`, cache de prompt, memória de sessão, logs | Consumo previsível e auditável |

---

## 11. Checklist de Implantação

- [ ] Backup do `knowledge` antigo e criação da árvore nova (seção 3)
- [ ] `.ignore` e regra de extensões proibidas no CI
- [ ] Padrão de front matter publicado em `_meta/schema_frontmatter.md`
- [ ] Cópia seletiva (simulação com `/L` primeiro) e tabela de-para antigo → novo
- [ ] Conversão `.mdx` → `.md` e divisão dos manuais acima de 2.000 tokens
- [ ] Front matter em todos os manuais (em lote, com revisão por amostragem)
- [ ] `gerar_indices.py`, `validar.py`, `indexar_busca.py` e `medir_tokens.py` rodando
- [ ] CSVs grandes carregados no `knowledge.sqlite`
- [ ] Ferramentas MCP `buscar_rota`, `ler_secao`, `consultar_dados`, `registrar_consulta`
- [ ] Prompt caching ativo no `00_MASTER_ROUTER.md`
- [ ] Medição real de tokens por formato e por nível registrada
- [ ] Revisão semanal dos logs de consulta

---

## 12. Pontos a Confirmar com Você

1. **Distribuição dos 6.421 manuais:** os nomes de pastas e stacks acima são uma proposta. A contagem exata por stack define onde o índice de stack (nível 3) é necessário.
2. **Conteúdo útil dos 7.297 `.json`:** se são só `folder_map.json` por pasta, todos somem; se há dados de verdade, viram CSV ou tabelas SQLite.
3. **Embeddings:** começar só com FTS5 e adicionar embeddings quando os logs mostrarem falhas por sinônimo.
