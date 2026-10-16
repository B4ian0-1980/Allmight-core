# 🏗️ Blueprint Consolidado: Knowledge v5.0 (`.agent/knowledge`)
**Roteamento hierárquico + `---json` Front Matter + busca por SQLite + migração por swap**

> **Destino:** `d:\xampp\htdocs\0-fonte\.agent\knowledge` (construído em `knowledge_v4/` e trocado no final)
> **Base:** diagnóstico real do disco (170.075 arquivos, ~1,86 GB) → meta de ~6.450 arquivos, < 40 MB.
> **Esta versão funde:** a arquitetura de índices em níveis (v2/v4), os 8 macrodomínios e a estratégia de migração do Dossiê, e as decisões confirmadas pela auditoria.

---

## 1. Decisões Consolidadas

| Tema | Decisão | Base |
|---|---|---|
| Formato do front matter dos manuais | **`---json`** (JSON estrito, gerado por script) | Decisão do projeto; ver seção 5.3 para as condições |
| Formato dos `_index.md` (lidos pelo modelo) | **YAML compacto**, gerado pelo build | Menos tokens que JSON quando o modelo lê o arquivo |
| Segurança | **Subpasta** `06-devops-infra/seguranca/` | Auditoria: não há acervo teórico de OWASP/SIEM; JWT só em código clonado |
| OWASP Top 10 e autenticação JWT | **Backlog de conteúdo a escrever** (não são pastas vazias) | Ver `_dados/csv/backlog_conteudo.csv` |
| HTML | **Descartar ~99%** (1.006 arquivos); converter só os < 15 manuais reais via AnyDoc | Auditoria: são templates, entradas de build e páginas de teste |
| Binários | Converter `Core Java 2 Vol. 1.pdf` e `sdk.docx` para `.md` por capítulo/seção | Dossiê |
| Executáveis e servidores MCP | Ficam em `apps/` (já criada), fora de `knowledge/` | Dossiê |
| Arquivo morto | `99_ARQUIVO` **não migra** e não é indexado | Triagem e obsoletos |
| Virada | Construir em `knowledge_v4/`, validar, depois trocar nomes mantendo `knowledge_old` para rollback | Dossiê |

---

## 2. Princípios

1. **Carregar o mínimo, no nível mais raso possível.** Cada índice só é aberto se o nível acima bater.
2. **Índices dinâmicos e limitados:** no máximo **40 rotas por `_index.md`**. Passou disso, subdivide-se a pasta (o build falha e avisa).
3. **Dois caminhos até o manual:** navegação (Mestre → Domínio → Stack → Manual) e atalho por busca (`buscar_rota`).
4. **Granularidade endereçável:** a IA lê a **seção** (`arquivo.md#secao`) ou a **linha** (SQL), não o arquivo inteiro.
5. **Índices nunca à mão.** Cada manual declara seus metadados; o build gera tudo.
6. **Sem pastas vazias.** Pasta só existe quando há conteúdo; o que falta vai para o backlog.
7. **Medir, não estimar:** as economias de tokens são ordens de grandeza até o `medir_tokens.py` rodar nos seus arquivos.

---

## 3. Níveis de Contexto

Como cada domínio lista **stacks diretamente** (não há camada de "grupo"), o caminho típico tem poucos saltos:

| Nível | Arquivo | Conteúdo | Orçamento |
|---|---|---|---|
| 0 — Mestre | `_meta/00_MASTER_ROUTER.md` | 8 domínios + regras do agente | ≤ 700 tokens |
| 1 — Domínio | `<dominio>/_index.md` | Stacks / temas do domínio | ≤ 800 tokens |
| 2 — Stack/Tema | `<dominio>/<stack>/_index.md` | Manuais com seções e tokens | ≤ 1.200 tokens |
| 3 — Subtema (só se a stack passar de 40 manuais) | `<stack>/<subtema>/_index.md` | Manuais do subtema | ≤ 1.200 tokens |
| Conteúdo | `.md` / `.csv` | Manual final | ≤ 2.000 tokens por arquivo |

O gerador cria níveis conforme a profundidade real das pastas; não é preciso configurar nada.

---

## 4. Árvore de Diretórios (8 Domínios)

Convenção: prefixo `_` = infraestrutura; prefixo numérico = conteúdo.

```plaintext
d:\xampp\htdocs\0-fonte\
├── apps\                                  # [JÁ CRIADO] executáveis e MCP Servers (fora do knowledge)
└── .agent\
    ├── knowledge_old\                     # backup da base antiga (rollback, depois descartar)
    └── knowledge\                         # BASE NOVA (construída em knowledge_v4\ e trocada)
        │
        ├── .ignore
        │
        ├── _meta\                         # GOVERNANÇA
        │   ├── 00_MASTER_ROUTER.md        # Nível 0 (GERADO)
        │   ├── schema_frontmatter.md      # padrão obrigatório dos manuais
        │   ├── orcamento_contexto.yaml
        │   ├── build\
        │   │   ├── inventario.py          # classifica e conta o que vai migrar
        │   │   ├── converter_binarios.py  # PDF/DOCX/HTML → .md (via AnyDoc)
        │   │   ├── enriquecer_frontmatter.py   # gera o bloco ---json
        │   │   ├── gerar_indices.py       # gera todos os _index.md + MASTER_ROUTER
        │   │   ├── validar.py             # CI
        │   │   ├── indexar_busca.py       # popula o SQLite/FTS5
        │   │   └── medir_tokens.py
        │   ├── logs\
        │   │   └── consultas.csv
        │   └── scripts\                   # utilitários MCP (leves)
        │       ├── mcp_doctor.ps1
        │       ├── mcp_status.ps1
        │       └── start_mcp_factory.ps1
        │
        ├── _dados\                        # DADOS TABULARES (nunca lidos inteiros)
        │   ├── csv\
        │   │   ├── catalogo_stacks.csv    # as 46 tecnologias
        │   │   ├── registro_fontes.csv
        │   │   ├── de_para_migracao.csv   # pasta antiga → pasta nova
        │   │   └── backlog_conteudo.csv   # guias a escrever (OWASP, JWT...)
        │   └── knowledge.sqlite           # GERADO: rotas (FTS5) + tabelas dos CSVs
        │
        ├── 01-gestao\
        │   ├── _index.md
        │   ├── startup-produto\           # GStack, MVP, validação de hipóteses
        │   ├── sdlc-agil\                 # sprints, histórias de usuário, cerimônias, PMBOK/Scrum
        │   ├── arquitetura-software\      # padrões, ADRs, trade-offs
        │   └── lideranca-engenharia\      # Addy Osmani e práticas de engenharia
        │
        ├── 02-arquitetura-ia\
        │   ├── _index.md
        │   ├── mcp\                       # protocolo, schemas leves, catálogo de servers (docs, não instalação)
        │   ├── memoria-agentes\           # Claude-Mem, Graphiti
        │   ├── llms-gratuitos\            # catálogo de APIs e fallbacks (FREE_LLM_APIS)
        │   ├── prompts-contexto\          # engenharia de contexto, system prompts
        │   └── rag-busca\                 # FTS, embeddings, chunking, ranking híbrido
        │
        ├── 03-linguagens\                 # linguagens e runtimes
        │   ├── _index.md
        │   ├── python\   java\   go\   rust\   csharp\   php\   nodejs\   typescript\
        │   └── (cada pasta: _index.md + manuais por tema)
        │
        ├── 04-frameworks\
        │   ├── _index.md
        │   ├── laravel\  nextjs\  react\  vue\  angular\  tailwind\
        │   └── (acrescentar mobile ou outros SOMENTE se existirem entre as 46 tecnologias)
        │
        ├── 05-banco-dados\
        │   ├── _index.md
        │   ├── postgresql\  mysql\  redis\  sqlite\  prisma\  (mongodb se existir)
        │
        ├── 06-devops-infra\
        │   ├── _index.md
        │   ├── containers\                # Docker, Docker Compose
        │   ├── ci-cd\                     # pipelines e estratégias de deploy
        │   ├── nginx-gateways\            # Nginx, proxy reverso, OmniRoute Gateway
        │   ├── linux\                     # administração, hardening de SO, systemd
        │   ├── seguranca\                 # SSL/TLS, Nginx hardening, firewall, Docker security
        │   └── ambiente-local\            # XAMPP, Windows, PowerShell
        │
        ├── 07-design-hardware\
        │   ├── _index.md
        │   ├── ux\                        # leis de UX (Fitts, Hick, Miller), heurísticas
        │   ├── acessibilidade\            # WCAG, contraste, paletas semânticas
        │   ├── design-systems\            # tokens, componentes, OpenMontage (diretrizes visuais)
        │   └── iot\                       # ESP32, Arduino, MQTT
        │
        └── 08-automacao\
            ├── _index.md
            ├── n8n\                       # playbooks e fluxos
            ├── evolution-api\             # 1 guia no lugar de 5.265 arquivos clonados
            ├── context-engines\           # AnyDoc Parser, Graft Context Engine
            ├── cli-agentes\               # Plandex e execução concorrente
            └── webhooks-bots\             # Zap Guardian, webhooks, bots
```

### O que mudou em relação à v4 anterior

| Mudança | Motivo |
|---|---|
| `03-linguagens`, `04-frameworks` e `05-banco-dados` separados | Alinha com o Dossiê e mantém cada índice de domínio abaixo de 40 rotas |
| Sem camada de "grupo" (backend/frontend) | Menos um salto; o domínio lista as stacks direto |
| `07-design-hardware` e `08-automacao` | Domínios reais do disco que a v4 não previa |
| `seguranca/` dentro de `06-devops-infra` | Conteúdo real é SSL, Nginx hardening, firewall, Docker security |
| OmniRoute em `nginx-gateways/` | O Dossiê o classifica em INFRA_OPS, não em IA |
| Sem pastas OWASP/JWT/SIEM por enquanto | Não existe acervo; viram backlog e entram quando forem escritos |
| `_dados/` e `_meta/build/` | Separam dados e ferramentas do conteúdo |

---

## 5. Front Matter `---json`

### 5.1 Exemplo canônico

```markdown
---json
{
  "id": "laravel-architecture-11",
  "title": "Laravel 11 Architecture & Best Practices",
  "categoria": "frameworks",
  "subcategoria": "laravel",
  "resumo": "Service providers, middlewares, form requests e repositórios no Laravel 11.",
  "gatilhos": ["laravel", "eloquent", "service provider", "form request", "clean architecture", "repositório"],
  "perguntas_tipo": ["Como organizo repositórios no Laravel 11?", "Onde validar entrada: controller ou form request?"],
  "nao_cobre": ["filas", "migrations", "testes"],
  "target_agent": ["backend-developer", "api-designer"],
  "compatibility": {"php": ">=8.2", "laravel": "^11.0"},
  "source": {"origin": "Laravel Official Docs", "original_format": "markdown"},
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-backend",
  "prioridade": 1,
  "depende_de": []
}
---
# Laravel 11 Architecture & Best Practices
> Resumo: organização em camadas, form requests e repositórios.
> Seções: service-providers · middlewares · form-requests · repositorios

## Service providers
...
```

### 5.2 Campos

| Campo | Obrigatório | Observação |
|---|---|---|
| `id` | ✅ | Único em toda a base |
| `title` | ✅ | Deve coincidir com o H1 |
| `resumo` | ✅ | 1 linha; base do roteamento |
| `gatilhos` | ✅ | Substitui `tags`: termos técnicos **e sinônimos** (PT-BR e EN) |
| `perguntas_tipo` | recomendado | 2–3 perguntas reais; alimenta a busca |
| `nao_cobre` | recomendado | Evita falsos positivos entre manuais parecidos |
| `categoria` / `subcategoria` | ✅ | Espelham a pasta |
| `target_agent` | opcional | Filtra candidatos por papel do agente |
| `compatibility` | opcional | Versões da tecnologia documentada |
| `source` | ✅ | Origem e formato original (`markdown`, `pdf`, `docx`, `html`) |
| `atualizado_em` | ✅ | Quando o arquivo mudou |
| `verificado_em` | ✅ | Quando alguém confirmou que o conteúdo está correto (diferente de `atualizado_em`) |
| `dono` | ✅ | Responsável pela correção |
| `prioridade` | opcional | **1 a 3** (desempate). Substitui `search_boost`, que envelhece mal; o peso real vem dos logs |
| `depende_de` | opcional | Ids carregados em cadeia, só se a pergunta exigir |
| `tokens_estimados`, `secoes` | **gerados** | Ficam nos índices, não no arquivo |

### 5.3 Por que `---json`, e as condições para funcionar

**Boas razões:** JSON é estrito (erro de sintaxe falha na hora, sem ambiguidade), o parse usa só a biblioteca padrão (`json`) e o front matter é sempre escrito por script, então ninguém edita à mão.

**Pontos a ter em conta (e como o projeto os trata):**

| Ponto | Tratamento |
|---|---|
| Custo de tokens: o JSON gasta mais que YAML (aspas, chaves, vírgulas) quando o modelo lê o arquivo | A ferramenta `ler_secao` **remove o front matter** antes de entregar o conteúdo. Os `_index.md`, que o modelo lê direto, ficam em YAML |
| `---json` não é um padrão universal | Obsidian e a maioria dos editores não reconhecem; a `gray-matter` tem engine JSON, mas **confirme com um teste de 2 linhas** antes de depender dela. Qualquer parser próprio de 3 linhas resolve (seção 7) |
| Windows | O risco real é o **BOM** (arquivo salvo como UTF-8 com BOM) e o CRLF. O parser usa `utf-8-sig` e normaliza `\r\n`; o `validar.py` rejeita arquivos que não abrem |
| Edição manual | JSON não aceita vírgula sobrando nem aspas sem escape. Regra: **só o script escreve** o bloco; o humano corrige o campo e roda `enriquecer_frontmatter.py --validar` |
| A velocidade do `json.loads` | Irrelevante nesta escala (6.400 arquivos já são rápidos em qualquer formato); não é argumento a favor |

Regras de forma: a **primeira linha** é `---json`; o bloco termina numa linha contendo apenas `---`; JSON válido (aspas duplas, sem vírgula final).

---

## 6. Templates de Índice (gerados, em YAML)

### Roteador Mestre (`_meta/00_MASTER_ROUTER.md`)

```markdown
---
ecossistema: AllMight Knowledge v5.0
caminho_raiz: d:/xampp/htdocs/0-fonte/.agent/knowledge
regra_agente: >
  NUNCA varra pastas. Passo 1: use buscar_rota(pergunta); se devolver candidatos, escolha entre eles.
  Passo 2: sem a ferramenta, ache o domínio pelos gatilhos e abra só o seu _index.md.
  Passo 3: desça um nível por vez. Passo 4: carregue só a seção (arquivo.md#secao) ou a linha (consultar_dados).
  Se a pergunta não exigir nenhum domínio, responda direto.
orcamento: {max_arquivos: 3, max_tokens_carga: 6000}
dominios:
  - {id: idx_01-gestao, resumo: "Produto, SDLC ágil, arquitetura de software, liderança.", gatilhos: [sdlc, scrum, pmbok, mvp, gstack, adr], indice: ../01-gestao/_index.md}
  - {id: idx_02-arquitetura-ia, resumo: "MCP, memória de agentes, LLMs gratuitos, prompts, RAG.", gatilhos: [mcp, memoria, graphiti, claude-mem, prompt, rag, embeddings], indice: ../02-arquitetura-ia/_index.md}
  - {id: idx_03-linguagens, resumo: "Linguagens e runtimes.", gatilhos: [python, java, go, rust, csharp, php, node, typescript], indice: ../03-linguagens/_index.md}
  - {id: idx_04-frameworks, resumo: "Frameworks web.", gatilhos: [laravel, nextjs, react, vue, angular, tailwind], indice: ../04-frameworks/_index.md}
  - {id: idx_05-banco-dados, resumo: "Bancos de dados e ORMs.", gatilhos: [postgres, mysql, redis, sqlite, prisma, query, indice], indice: ../05-banco-dados/_index.md}
  - {id: idx_06-devops-infra, resumo: "Containers, CI/CD, Nginx, Linux, segurança de infra, ambiente local.", gatilhos: [docker, nginx, ssl, firewall, hardening, ci/cd, xampp, powershell], indice: ../06-devops-infra/_index.md}
  - {id: idx_07-design-hardware, resumo: "UX, acessibilidade, design systems, IoT.", gatilhos: [ux, wcag, fitts, hick, esp32, arduino, mqtt], indice: ../07-design-hardware/_index.md}
  - {id: idx_08-automacao, resumo: "n8n, Evolution API, parsers de contexto, CLIs de agentes, webhooks.", gatilhos: [n8n, evolution api, whatsapp, anydoc, graft, plandex, webhook], indice: ../08-automacao/_index.md}
dados_tabulares: {banco: ../_dados/knowledge.sqlite, tabelas: [catalogo_stacks, registro_fontes, backlog_conteudo]}
---
```

### Índice de domínio (`04-frameworks/_index.md`)

```markdown
---
id: idx_04-frameworks
resumo: Frameworks web.
gatilhos: [laravel, nextjs, react, vue, angular, tailwind]
subpastas:
  - {id: idx_laravel, resumo: "Arquitetura, Eloquent, filas, testes, Octane.", gatilhos: [laravel, eloquent, artisan, fila], indice: ./laravel/_index.md}
  - {id: idx_nextjs, resumo: "App Router, RSC, Server Actions, cache.", gatilhos: [nextjs, app router, ssr, isr], indice: ./nextjs/_index.md}
---
```

### Índice de stack (`04-frameworks/laravel/_index.md`)

```markdown
---
id: idx_laravel
resumo: Arquitetura, Eloquent, filas, testes, Octane.
gatilhos: [laravel, eloquent, artisan, fila]
rotas:
  - id: laravel-architecture-11
    resumo: Service providers, middlewares, form requests e repositórios no Laravel 11.
    gatilhos: [laravel, service provider, form request, clean architecture]
    nao_cobre: [filas, migrations]
    arquivo: ./laravel-architecture-11.md
    secoes: [service-providers, middlewares, form-requests, repositorios]
    tokens_estimados: 1150
    atualizado_em: "2026-10-15"
---
```

### Catálogo e backlog (CSV puro, `_dados/csv/`)

```csv
id,tema,dominio,destino,prioridade,status
bl_01,OWASP Top 10 (guia consolidado),06-devops-infra,seguranca/owasp-top10.md,1,a escrever
bl_02,Autenticação JWT e OAuth2,06-devops-infra,seguranca/autenticacao-jwt.md,1,a escrever
bl_03,SIEM e detecção (Wazuh),06-devops-infra,seguranca/siem-wazuh.md,3,a escrever
```

---

## 7. Scripts de Build

### 7.1 Leitura do front matter (usada por todos os scripts)

```python
import json, re
from pathlib import Path

FM = re.compile(r"\A---json\n(.*?)\n---\n", re.S)

def ler(p: Path):
    t = p.read_text(encoding="utf-8-sig").replace("\r\n", "\n")   # tolera BOM e CRLF do Windows
    m = FM.match(t)
    if not m:
        return None, t
    return json.loads(m.group(1)), t[m.end():]                     # erro de JSON falha aqui, alto e claro
```

### 7.2 `gerar_indices.py` (esqueleto funcional)

```python
from collections import Counter
import re, yaml                       # PyYAML só no build; a leitura em produção não precisa dele

RAIZ = Path(r"d:\xampp\htdocs\0-fonte\.agent\knowledge_v4")
MAX_ROTAS, ERROS = 40, []

def tokens(txt):                      # estimativa; troque por tiktoken e valide com medir_tokens.py
    return max(1, len(txt) // 4)

def secoes(corpo):
    return [re.sub(r"[^\w\- ]", "", h).strip().lower().replace(" ", "-")
            for h in re.findall(r"^## (.+)$", corpo, re.M)]

def pasta_meta(pasta):                # resumo opcional da pasta em _pasta.json
    f = pasta / "_pasta.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}

def gerar(pasta: Path, raiz=False):
    filhos, rotas = [], []
    for sub in sorted(p for p in pasta.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))):
        idx = gerar(sub)              # bottom-up: filhos primeiro
        if idx:
            filhos.append({"id": idx["id"], "resumo": idx["resumo"], "gatilhos": idx["gatilhos"],
                           "indice": f"{'../' if raiz else './'}{sub.name}/_index.md"})
    for md in sorted(pasta.glob("*.md")):
        if md.name.startswith("_"):
            continue
        meta, corpo = ler(md)
        if not meta or not all(k in meta for k in ("id", "resumo", "gatilhos")):
            ERROS.append(f"front matter ausente/incompleto: {md}")
            continue
        rotas.append({"id": meta["id"], "resumo": meta["resumo"], "gatilhos": meta["gatilhos"],
                      **{k: meta[k] for k in ("nao_cobre", "depende_de", "atualizado_em") if k in meta},
                      "arquivo": f"./{md.name}", "secoes": secoes(corpo), "tokens_estimados": tokens(corpo)})
    total = len(filhos) + len(rotas)
    if total == 0:
        return None
    if total > MAX_ROTAS:
        ERROS.append(f"{pasta}: {total} entradas (> {MAX_ROTAS}). Subdivida a pasta.")
    gat = Counter(g for e in filhos + rotas for g in e.get("gatilhos", []))
    idx = {"id": f"idx_{pasta.name}", "resumo": pasta_meta(pasta).get("resumo", f"Índice de {pasta.name}"),
           "gatilhos": [g for g, _ in gat.most_common(12)]}
    if filhos: idx["dominios" if raiz else "subpastas"] = filhos
    if rotas:  idx["rotas"] = rotas
    destino = RAIZ / "_meta" / "00_MASTER_ROUTER.md" if raiz else pasta / "_index.md"
    destino.write_text("---\n" + yaml.safe_dump(idx, allow_unicode=True, sort_keys=False) + "---\n",
                       encoding="utf-8")
    return idx

if __name__ == "__main__":
    gerar(RAIZ, raiz=True)
    if ERROS:
        print("\n".join(ERROS)); raise SystemExit(1)
```

### 7.3 `validar.py` — regras de CI

| Verificação | Falha quando... |
|---|---|
| JSON inválido | O bloco `---json` não parseia |
| Campos obrigatórios | Falta `id`, `title`, `resumo`, `gatilhos`, `source`, `atualizado_em`, `verificado_em` ou `dono` |
| `id` duplicado | Dois manuais com o mesmo `id` |
| Links quebrados / órfãos | `arquivo` ou `indice` inexistente; `.md` fora de qualquer índice |
| Tamanho | Manual > 2.000 tokens; índice acima do orçamento ou com > 40 rotas |
| Pasta vazia | Há pasta de conteúdo sem manuais |
| Extensões proibidas | `.js`, `.py`, `.pyc`, `.json`, `.html`, `.map`, `.lock`, `node_modules`, `.venv`, `.git` dentro de `knowledge/` (exceto `_meta/build` e `_dados`) |
| Origem de terceiros | Caminho contém clones ou skills de terceiros (ex.: `ruflo/`) |
| Título | `title` diferente do H1 |
| Conteúdo velho | `verificado_em` além do prazo definido por domínio |
| Gatilhos em conflito | Mesmo gatilho em manuais irmãos sem `prioridade` ou `nao_cobre` |

---

## 8. Camada de Acesso (Ferramentas MCP, hospedadas em `apps/`)

| Ferramenta | Entrada | Saída | Custo típico |
|---|---|---|---|
| `buscar_rota` | `pergunta`, `dominio?`, `target_agent?` | Top-3: `id`, `resumo`, `nao_cobre`, `caminho`, `tokens_estimados` | ~150 tokens |
| `ler_secao` | `arquivo`, `secao?` | **Só a seção** (sem front matter); sem `secao`, devolve o mini-sumário | ≤ 2.000 |
| `consultar_dados` | `tabela`, `filtro` | Linhas do SQLite | 20–200 |
| `registrar_consulta` | `rota`, `tokens`, `util` | Grava em `consultas.csv` | ~0 |

```sql
-- indexar_busca.py: popula a partir do front matter dos manuais (resumo + gatilhos + perguntas_tipo)
CREATE VIRTUAL TABLE rotas USING fts5(
  id, resumo, gatilhos, perguntas_tipo, caminho UNINDEXED, nao_cobre UNINDEXED,
  tokenize = 'unicode61 remove_diacritics 2'            -- trata acentos do PT-BR
);
-- consulta de buscar_rota
SELECT id, caminho, bm25(rotas) AS score FROM rotas WHERE rotas MATCH ? ORDER BY score LIMIT 3;
```

* **Fase 1:** só FTS5/BM25.
* **Fase 2:** embeddings sobre `resumo + perguntas_tipo` das rotas (não do corpo) + fusão de rankings (RRF), quando os logs mostrarem falhas por sinônimo.
* **O `index.json` global do Dossiê** pode existir como artefato de máquina (alimenta o SQLite), mas **nunca é lido pela IA**: com ~6.400 entradas seria enorme.

---

## 9. Pipeline de Migração (170.075 → ~6.450 arquivos)

```
knowledge (atual) ─► inventario.py ─► cópia seletiva ─► conversão de binários
        ─► enriquecimento (---json) ─► gerar_indices ─► validar ─► indexar_busca ─► medir
        ─► knowledge_v4/ ─► SWAP (knowledge → knowledge_old; knowledge_v4 → knowledge)
```

### Fase 0 — Inventário (antes de copiar)
Rodar `inventario.py` e gerar um relatório por pasta antiga: contagem por extensão, caminhos de terceiros e duplicatas por hash. **Atenção:** o número de 6.421 `.md` deve ser **recontado depois de excluir** `node_modules`, `.venv`, clones e skills de terceiros. Essas pastas têm milhares de `README.md`, `CHANGELOG.md` e `LICENSE.md` que não são manuais. Se a contagem pós-filtro for menor, o ganho será ainda maior.

### Fase 1 — Cópia seletiva (simulação primeiro; `/L` só lista)

```powershell
robocopy "D:\xampp\htdocs\0-fonte\.agent\knowledge" "D:\xampp\htdocs\0-fonte\.agent\knowledge_staging" *.md `
  /S /L /NFL /NDL /XD node_modules .venv venv __pycache__ .git dist build ruflo servers 06_LAB_EXEMPLOS 99_ARQUIVO `
  /XF README.md CHANGELOG.md LICENSE.md CONTRIBUTING.md
```

Revise a lista, remova o `/L` e rode de verdade. Depois mapeie cada pasta antiga para a nova em `de_para_migracao.csv`.

### Fase 2 — Binários e HTML

| Origem | Ação |
|---|---|
| `Core Java 2, Volume 1.pdf` | Converter por capítulo (≤ 2.000 tokens por arquivo). O título indica **edição antiga**: confira a versão e preencha `compatibility`; se for Java 5/6, classifique como Tier 2 ou arquive |
| `sdk.docx` | Converter para `.md` por seção |
| < 15 manuais HTML reais | Converter via AnyDoc para `.md` |
| ~990 HTML restantes (templates, `index.html` de build, páginas de teste) | **Descartar** |
| 7.297 `.json` | **Descartar** (exceto dados úteis, que viram CSV/SQLite) |
| Clones (Evolution API etc.) | **Não migrar**; escrever 1 guia em `08-automacao/evolution-api/` |

### Fase 3 — Enriquecimento do front matter
`enriquecer_frontmatter.py` extrai H1, títulos `##` e os primeiros ~1.000 tokens de cada manual, pede a um modelo pequeno que preencha `resumo`, `gatilhos` (com sinônimos), `perguntas_tipo` e `nao_cobre` **dentro de um schema JSON**, valida e grava o bloco `---json`. Estimativa de custo: ~6 milhões de tokens de entrada para ~6.400 manuais (a medir). Revisão humana por amostragem (~5%), priorizando Tier 1. Heurística local (tags a partir do H1) só serve de fallback: gera gatilhos pobres, sem sinônimos.

### Fase 4 — Build e validação
`gerar_indices.py` → `validar.py` → `indexar_busca.py` → `medir_tokens.py`. Só segue com tudo verde.

### Fase 5 — Swap com rollback

```powershell
Rename-Item "D:\xampp\htdocs\0-fonte\.agent\knowledge"    "knowledge_old"
Rename-Item "D:\xampp\htdocs\0-fonte\.agent\knowledge_v4" "knowledge"
# rollback, se preciso: inverter os dois nomes
```

> Não é uma operação atômica de verdade (são dois renomeios em sequência), mas o intervalo é de milissegundos e o rollback é imediato. Mantenha `knowledge_old` até a base nova rodar bem por alguns dias.

### Fase 6 — Operação contínua
Ligar `registrar_consulta`; revisar semanalmente perguntas sem rota, rotas nunca usadas e colisões; escrever o backlog (OWASP, JWT, SIEM) conforme a demanda.

---

## 10. Orçamento de Contexto

```yaml
# _meta/orcamento_contexto.yaml
por_pergunta:
  max_arquivos: 3
  max_tokens_carga: 6000
  se_estourar: carregar_apenas_secoes
por_nivel: {mestre: 700, dominio: 800, stack: 1200, manual: 2000}
sessao: {nao_recarregar_ids_ja_lidos: true}
```

* **Cache de prompt:** o `00_MASTER_ROUTER.md` é estável; deixe-o no início do prompt como prefixo cacheável.
* **Memória de sessão:** guarde os `id` já carregados e referencie-os em vez de recarregar.

### Fluxo da consulta

```
1. Pergunta  →  buscar_rota (top-3)  ou  Master Router (cacheado)
   └─ nenhum bate? → responder direto
2. Descer: domínio → stack → (subtema)
3. Escolher rota (gatilhos, perguntas_tipo, nao_cobre, prioridade)
4. ler_secao(arquivo, secao)  |  consultar_dados(tabela, filtro)
5. Conferir orçamento (≤ 3 arquivos / ~6k tokens)
6. Responder → registrar_consulta(rota, tokens, util)
```

---

## 11. Antes e Depois

| Item | Antes | Depois |
|---|---|---|
| Arquivos | 170.075 | ~6.450 (a confirmar após o filtro da Fase 0) |
| Tamanho | ~1,86 GB | < 40 MB |
| Leitura inicial da IA | `INDICE_GERAL.md` (~20.000 tokens) | Mestre ≤ 700 tokens (ou top-3 por busca, ~150) |
| `node_modules` / `.venv` / `.pyc` | ~117.000+ arquivos | 0 (`.ignore` + CI) |
| Servidores MCP | Dentro de `knowledge/` | `apps/` |
| Repositório clonado da Evolution API | 5.265 arquivos | 1 guia `.md` |
| HTML | 1.006 arquivos | < 15 manuais convertidos |
| JSON | 7.297 arquivos | 0 (dados úteis → CSV/SQLite) |
| Metadados | Inconsistentes | `---json` validado em todo manual |
| Índices | Manual, 78 KB | Gerados, ≤ 40 rotas cada |
| Segurança | Não documentada | Subpasta + backlog explícito |

---

## 12. Checklist de Implantação

- [ ] Backup do `knowledge` atual (`knowledge_old`) e criação de `knowledge_v4/` com a árvore da seção 4
- [ ] `.ignore` e regras de extensões proibidas no CI
- [ ] `schema_frontmatter.md` publicado (seção 5)
- [ ] **Teste de 2 linhas** do parser `---json` (e da `gray-matter`, se for usá-la)
- [ ] `inventario.py` rodado e contagem real de manuais pós-filtro registrada
- [ ] Cópia seletiva (simulação com `/L` primeiro) e `de_para_migracao.csv`
- [ ] Conversão do PDF do Java, do `sdk.docx` e dos < 15 HTML; conferência da edição do livro
- [ ] Divisão dos manuais acima de 2.000 tokens por seção `##`
- [ ] Front matter em todos os manuais (lote com modelo + revisão por amostragem)
- [ ] `gerar_indices.py`, `validar.py`, `indexar_busca.py`, `medir_tokens.py` verdes
- [ ] Ferramentas MCP em `apps/` (`buscar_rota`, `ler_secao`, `consultar_dados`, `registrar_consulta`)
- [ ] Prompt caching no `00_MASTER_ROUTER.md`
- [ ] Swap com `knowledge_old` guardado para rollback
- [ ] Backlog de conteúdo (OWASP, JWT, SIEM) cadastrado em `_dados/csv/backlog_conteudo.csv`

---

## 13. Pontos em Aberto

1. **Contagem real de manuais** após excluir READMEs e arquivos de terceiros (Fase 0).
2. **Edição do "Core Java 2 Vol. 1"**: define se vira Tier 1 ou Tier 2.
3. **Quais das 46 tecnologias existem de fato** em mobile, MongoDB e outras: só viram pasta se houver conteúdo.
4. **Compatibilidade do `---json`** com as ferramentas que vocês usam (teste da Fase 0).
