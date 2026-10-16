# Roadmap de Melhorias — Sistema Operacional Cognitivo (Antigravity)

Oct 11, 2026 · @Robson

## Resumo executivo

O maior risco do ecossistema hoje não é falta de capacidade — são 103 skills — é **sobrecarga de descoberta**: tudo é anunciado ao modelo antes de qualquer palavra do usuário, diluindo precisão e consumindo contexto. As quatro frentes abaixo (P4, P1, P0, P2) atacam isso em ordem de dependência: primeiro medir o que existe (healthcheck), depois comprimir o que é anunciado (manifest/lazy-loading), depois padronizar como se executa (CLI), e por fim automatizar para que as três primeiras não se desalinhem com o tempo (sync de catálogo).

## Descobertas nos arquivos reais — isso muda o diagnóstico

Os arquivos que você anexou (`painel_sistema.html`, `01_routing.md`, `02_coding_standards.md`, `03_execution_protocols.md`, `GEMINI.md`) revelam coisas que o dossiê original não deixava claras. Resumindo os quatro achados que mais importam:

**1. O carregamento de skills já é lazy — o gargalo é outro.** O `GEMINI.md` descreve explicitamente: "Agent activated → Check frontmatter 'skills:' → Read SKILL.md (INDEX) → Read specific sections", com leitura seletiva. Isso significa que a P1 (manifest/lazy-loading) não resolve um problema de "skills sempre carregadas" — isso já não acontece no nível de skill. O que provavelmente pesa no contexto são os 21 arquivos de agente (lidos ao ativar cada persona) e a leitura obrigatória de `ARCHITECTURE.md` no início de toda sessão (regra 🔴 MANDATORY do `GEMINI.md`). **Isso muda o foco da P1**: em vez de comprimir a lista de skills, o ganho maior pode estar em auditar o tamanho dos arquivos de agente e repensar o que é lido obrigatoriamente a cada sessão.

**2. `painel_sistema.html` confirma a hipótese da P2.** Os dados dos cards (nome, tag, descrição, path, link do GitHub) estão 100% hardcoded como HTML — não há nenhuma fonte de dados externa (JSON/JS) sendo lida. O JavaScript do painel só faz busca/filtro no DOM já renderizado. Isso confirma: qualquer atualização de skill exige editar esse HTML manualmente, exatamente o risco de divergência que o dossiê apontou. A recomendação de separar dados de apresentação (P2) se confirma necessária, não é só suposição.

**3. Existe uma convenção real de scripts por skill — sinal melhor para o healthcheck.** O `03_execution_protocols.md` lista scripts como `security_scan.py`, `lint_runner.py`, `ux_audit.py` etc., invocados via `python .agent/skills/<skill>/scripts/<script>.py`. Isso é mais confiável como critério de `READY` do que adivinhar pela extensão de arquivo solta na pasta: a regra correta para o healthcheck é checar se existe `skills/<nome>/scripts/*.py` (ou `.js`), não só qualquer arquivo de código na pasta.

**4. Achado crítico — pode haver um sistema paralelo não catalogado.** A tabela "CONTEXT-AWARE RESOURCE SUGGESTIONS" dentro de `01_routing.md` referencia ferramentas como `OmniRoute`, `Graft`, `Clodfarm`, `Graphiti (Zep)`, `OpenClaw`, `OpenMontage`, `AnyDoc Parser`, `YouTube Automation Agent` e `Agency Agents Roster` — todas apontando para caminhos em `knowledge/allmight/...`, **nenhuma delas presente nas 103 skills do catálogo nem no painel**. Ou seja: parece existir uma segunda base de conhecimento (`knowledge/allmight/`) com ferramentas próprias, promovida pela mesma regra de roteamento, mas fora do escopo que o dossiê original mapeou. Preciso que você esclareça isso antes de eu desenhar o manifest final — ver pergunta abaixo.

## Resolução: escopo da P1/P4/P0 é só `skills/`

Os dois documentos que você anexou depois (`LEVANTAMENTO_TECNICO_SKILLS.md` e `RELATORIO_ALLMIGHT_VS_SKILLS.md`) resolvem a dúvida: não é divergência, é arquitetura intencional. `knowledge/allmight/` é uma **camada de conhecimento** (blueprints densos, consultados sob demanda via `/kb`), separada da **camada operacional** (`skills/`, leve, invocada diretamente pelos agentes). O radar em `01_routing.md` existe justamente para não carregar a AllMight inteira — ele aponta para o arquivo certo só quando o contexto pede.

**Decisão adotada:** healthcheck (P4), manifest (P1) e `agent-cli.py` (P0) ficam restritos a `skills/` — é a camada operacional, é onde mora o problema de contexto. `knowledge/allmight/` não entra nesse escopo agora. A "Promoção de Classe" sugerida no relatório (migrar OmniRoute, Graft, OpenClaw e AnyDoc Parser de blueprint para skill executável) é uma iniciativa separada e opcional — pergunto sobre ela no final do doc \*\*Achado 5 — o pior caso de divergência está no arquivo mais carregado de todos.\*\* Os 20 arquivos de \`agents/\` que você mandou confirmam a hipótese do achado 1: \`frontend-specialist.md\` e \`orchestrator.md\` são muito mais pesados que qualquer \`SKILL.md\` — \`frontend-specialist.md\` sozinho tem dezenas de seções (Deep Design Thinking, Maestro Auditor, Reality Check, tabelas de anti-padrões repetidas) e deve passar de 3000+ tokens. Mas o achado mais grave está no \`ARCHITECTURE.md\`: ele declara \*\*"20 Specialist Agents, 37 Skills, 12 Workflows"\*\*, enquanto o catálogo real e o painel mostram \*\*21 agentes, 103 skills, 17 workflows\*\*. Pior: \`ARCHITECTURE.md\` lista skills que não existem no catálogo atual (\`react-best-practices\`, \`prisma-expert\`, \`docker-expert\`, \`nestjs-expert\`, \`typescript-expert\`, \`ui-ux-pro-max\`) e omite dezenas que existem (todo o cluster \`claude-red-offensive-\*\`, \`freellmapi\`, \`ponytail-\*\` etc.). E pelo \`GEMINI.md\`, esse é o arquivo de leitura \*\*obrigatória a cada sessão\*\* — é o único documento de todo o ecossistema que está garantidamente errado E garantidamente carregado toda vez. Isso é mais urgente que o \`painel\_sistema.html\`: eu moveria a regeneração automática do bloco de estatísticas do \`ARCHITECTURE.md\` para o primeiro entregável de P2, antes até do \`sync\_catalog.py\` completo — é uma correção isolada e barata (reescrever só a tabela de contagens a partir do manifest) com o maior retorno imediato de todo o roadmap. \*\*Atualização:\*\* você esclareceu que a AllMight é, na prática, uma biblioteca de referência — PDFs e livros convertidos para Markdown — não um conjunto de ferramentas executáveis esperando promoção. Isso reforça a decisão: ela não entra no escopo de P4/P1/P0 (que lidam com código que roda), fica fora por natureza, não só por prioridade..

## ✅ Entregue: ARCHITECTURE.md corrigido + rotina automática de sincronização

Seguindo sua instrução ("Corrigir o ARCHITECTURE.md e criar uma rotina para atualizar quando for incluído novas skills"), entreguei dois arquivos:

1. **`sync_architecture.py`** — script Python (só biblioteca padrão, sem PyYAML) para colocar em `.agent/scripts/`. Ele varre `agents/*.md`, `skills/*/SKILL.md`, `workflows/*.md` e `scripts/*.py` direto no disco, nunca confia em números fixos, e regenera o `ARCHITECTURE.md` inteiro (tabela de agentes, tabela de skills em ordem alfabética, tabela de workflows, contagem de scripts e o bloco de estatísticas). Roda com `python .agent/scripts/sync_architecture.py` sempre que uma skill/agente/workflow for criado, removido ou renomeado. Também aceita `--check` (sai com código 1 se o arquivo estiver desatualizado — útil num hook de pre-commit).
2. **`ARCHITECTURE.md` corrigido** — já gerado pelo próprio script, usando os dados reais que você forneceu: **21 agentes**, **103 skills** (contra os 37 que o arquivo antigo listava), **17 workflows** e **6 scripts mestres**, com a tabela de skills vindo direto de `CATALOGO_SKILLS.md` (as mesmas 103 entradas, nomes batidos um a um) em vez de categorias ad-hoc que omitiam clusters inteiros como `claude-red-offensive-*`.

**Validação antes da entrega:** montei uma árvore de fixtures local espelhando `.agent/` (os 19 arquivos reais de agente que você mandou + stubs de frontmatter para os outros 103 skills/17 workflows/6 scripts a partir do catálogo) e rodei o script contra ela. Encontrei e corrigi dois bugs reais nesse processo: (a) o parser de frontmatter quebrava descrições de agente que continham vírgula (ex.: "Node.js, Python") porque tratava qualquer vírgula como lista — corrigido para só tratar `tools:` e `skills:` como listas; (b) o resumo de uma frase cortava no primeiro `.` literal, o que truncava `Node.js` para `Node` — corrigido para só quebrar em ` .  ` (ponto + espaço). Também testei o `--check` simulando uma skill nova (detectou divergência corretamente) e um `--root` inexistente (erro claro, não trace cru).

**O que ficou sinalizado como não verificado:** `mobile-developer.md` e `game-developer.md` não estavam entre os 19 arquivos de agente reais que você enviou — usei as descrições curtas do `painel_sistema.html` como aproximação. Quando você mandar os `.md` reais desses dois, é só rodar o script de novo que ele substitui a aproximação pelos dados reais automaticamente.

## P4 — healthcheck.py (auditor de prontidão)

Objetivo: varrer as 103 pastas em `skills/` e classificar cada uma automaticamente, gerando dados reais para priorizar P0 e P1 — hoje essa classificação só existe como impressão qualitativa no dossiê.

**Critérios de classificação por skill:**

| Status | Heurística real (confirmada em `LEVANTAMENTO_TECNICO_SKILLS.md`) |
| --- | --- |
| `READY` | A pasta contém um arquivo executável reconhecido (`package.json`, `generate.py`, `cli.py`, `run.py`, `main.py`) **e** o runtime correspondente (`node`, `python`) está disponível no host |
| `PLAYBOOK` | A pasta só tem `SKILL.md` (e talvez `references/`) — metodologia pura, sem código para rodar |
| `BLOCKED` | O `SKILL.md` ou as dependências exigem compilador/runtime ausente no Windows (`crystal`, `cargo`, `docker`, `go`) |
| `BROKEN` | `SKILL.md` ausente ou malformado, ou caminho no catálogo não bate com a pasta real |

**Saída proposta:** um `skills_status.json` versionado, formato `{ "skill": nome, "status": READY|PLAYBOOK|BLOCKED|BROKEN, "reason": string, "checked_at": data }`, mais um resumo tabular impresso no terminal. Esse JSON vira a fonte de dados do manifest leve da P1 (abaixo) e do hook de sincronização da P2.

**Próximo passo — resolvido:** os exemplos reais de `SKILL.md` que você anexou (`freellmapi` = READY, `claude-red-offensive-jwt` = PLAYBOOK, `manual-generator` = BLOCKED) confirmam a heurística da tabela acima. Não preciso de mais nada aqui para implementar o `healthcheck.py`.

## P1 — manifest.json e lazy-loading

Este é o item que mais diretamente ataca o "Paradoxo da Janela de Contexto" descrito no dossiê. A ideia central: o prompt de sistema não deveria carregar os 103 `SKILL.md` inteiros — deveria carregar só um índice compacto, e puxar o conteúdo completo de UMA skill apenas quando ela for de fato selecionada.

**Schema do manifest (gerado a partir do `skills_status.json` do healthcheck):**

```
{
 "skill": "claude-red-offensive-jwt",
 "cluster": 5,
 "status": "PLAYBOOK",
 "summary": "JWT attack methodology: alg confusion, kid injection, jku/x5u abuse, JWKS poisoning",
 "triggers": ["jwt", "json web token", "auth bypass", "kid injection"],
 "path": "skills/claude-red-offensive-jwt/SKILL.md"
}
```

**Fluxo em dois estágios:**

1. **Estágio 1 (sempre carregado):** o manifest inteiro — \~103 entradas × \~150 bytes ≈ 15KB, versus os `SKILL.md` completos que somados provavelmente passam de 300–500KB. O `rules/01_routing.md` classifica a requisição contra os campos `summary` + `triggers` do manifest, não contra o conteúdo integral.
2. **Estágio 2 (sob demanda):** uma vez que o roteador decide que a skill X é relevante, só então o agente lê `path` e carrega o `SKILL.md` completo daquela skill específica — exatamente o comportamento "leitura cirúrgica" que o dossiê já descreve informalmente no passo 3 do mecanismo, só que hoje sem o filtro do estágio 1 na frente.

**Estimativa de redução:** se os `SKILL.md` médios têm 3–5KB, carregar os 103 de uma vez custa \~300–500KB de contexto só em skills (fora agents/ e workflows/). Com o manifest, isso cai para \~15KB + o(s) `SKILL.md` efetivamente usado(s) por requisição — uma redução de contexto plausível na faixa de 90%+ no pior caso (requisição simples que usa 1 skill).

**Observação de acoplamento:** este manifest deveria ser gerado automaticamente a partir dos resultados do healthcheck (P4) — cada entrada herda `status`; uma skill `BLOCKED` pode opcionalmente ficar fora do manifest ativo até ser destravada, evitando que o roteador selecione algo que não vai funcionar.

## P0 — agent-cli.py (runner unificado)

Este é o item de maior esforço porque depende diretamente do healthcheck (P4): só dá para rotear a execução corretamente se o sistema souber, por skill, qual é o `runtime` (python/node/bash/playbook). Proposta: adicionar esse campo ao manifest e fazer o CLI ser uma camada fina de despacho, não um reimplementador de cada ferramenta.

**Mapeamento de tipos de execução observados no catálogo:**

| Tipo | Exemplos | Como o CLI despacha |
| --- | --- | --- |
| `python` | `LlamaFactory`, `airllm`, `media-inference-worker` | `subprocess` para o entrypoint declarado, env isolado se houver `requirements.txt` |
| `node` | `laya`, `musica`, `ruflo` | `npm run <script>` ou `node <entry>`, respeitando `package.json` |
| `bash` | utilitários de `bash-linux`, `deployment-procedures` | shell direto, com `set -e` |
| `playbook` | a maioria de `claude-red-offensive-*`, `red-team-tactics` | CLI recusa "rodar" e em vez disso imprime/abre o `SKILL.md` — não é um bug, é o comportamento correto para metodologia sem binário |
| `blocked` | `manual-generator` (depende de compilador Crystal ausente) | CLI recusa com mensagem clara da dependência faltante, apontando para o healthcheck |

**Estrutura de comandos (conforme já esboçado no dossiê, refinada):**

```
python .agent/cli.py run <skill> [-- args livres para a skill]
python .agent/cli.py audit --target <path>
python .agent/cli.py skills list [--status READY|PLAYBOOK|BLOCKED] [--cluster N]
python .agent/cli.py skills show <skill>   # imprime o SKILL.md
python .agent/cli.py healthcheck [--skill <nome>]  # roda P4 sob demanda
```

**Decisão de design — resolvida:** os exemplos reais de pastas (`freellmapi` = monorepo Node/Fastify com `package.json`, comando `npm run dev`; `media-inference-worker` = script Python direto, `python generate.py <model> "<prompt>"`) mostram que um despacho genérico funciona sem precisar de `run.yaml` por skill: se existe `package.json`, roda o script `dev` (ou o primeiro definido em `scripts`); se existe `generate.py`/`main.py`/`run.py`/`cli.py`, roda via `python <arquivo> [args]`. Isso cobre os dois padrões reais observados; um `run.yaml` manual só vira necessário se aparecer uma skill com múltiplos entrypoints ambíguos — tratamos isso como exceção, não como regra geral.

## P2 — sincronização automática de catálogo

O problema descrito no dossiê é concreto: hoje, clonar uma skill nova exige atualizar manualmente três lugares (`SKILL.md` da skill, `CATALOGO_SKILLS.md`, `painel_sistema.html`), com risco real de divergência entre disco e documentação.

Como P4 e P1 já produzem `skills_status.json` e `manifest.json` de forma automatizada, o hook de P2 é essencially o último elo: um script (`sync_catalog.py`) disparado manualmente ou via git hook (`post-checkout`/`post-merge` em `skills/`) que:

1. Roda o healthcheck incremental só nas pastas novas/alteradas desde a última sincronização.
2. Regenera as entradas correspondentes do `manifest.json`.
3. Reescreve a tabela do `CATALOGO_SKILLS.md` a partir do manifest (template fixo, dados variáveis) — elimina edição manual do markdown.
4. Regenera os dados que alimentam `painel_sistema.html` (se o painel já lê de um JSON/JS separado, só esse arquivo precisa ser tocado; se o HTML é estático com dados embutidos, vale considerar separar dados de apresentação nesse momento).

Não depende de P0 para funcionar — pode ser implementado assim que P4 e P1 existirem.

**Validação:** o próprio `painel_sistema.html` já antecipa esse caminho de evolução — trocar as \~2.400 linhas estáticas por um `skills_manifest.json` carregado via `fetch()`, com indicador visual de status (🟢 READY, 📘 PLAYBOOK, 🔴 BLOCKED). Isso bate exatamente com o desenho de P1 + P2 acima — não é mais só uma proposta minha, é um plano que o próprio painel já previa.

## Ordem de implementação e dependências

&#91;embedded content: dependências entre as 4 frentes\]

P4 é o único bloco sem pré-requisito e deve vir primeiro — sem dados reais de status, qualquer decisão de priorização em P1/P0/P2 é especulação. P1 consome a saída de P4 diretamente (o campo `status` entra no manifest). A partir daí, P0 e P2 podem avançar em paralelo: P0 depende do campo `runtime` (adicionável ao manifest de P1), e P2 depende apenas dos artefatos já gerados por P4 e P1 — nenhum dos dois depende do outro.

## O que preciso para avançar para código

Com os anexos de hoje, a maior parte de P4, P0 e P2 já está especificada com base em arquivos reais. O que falta agora é mais objetivo:

1. **Decisão sobre a AllMight** — incluir a "Promoção de Classe" (OmniRoute, Graft, OpenClaw, AnyDoc Parser) no escopo agora, ou deixar só pra depois? (pergunto isso também fora do doc)
2. Um exemplo real de `agents/*.md` (ex.: `orchestrator.md` ou `frontend-specialist.md`) — para confirmar a hipótese do achado 1: que os arquivos de agente pesam mais no contexto do que as skills em si.
3. **Resolvido:** priorizamos a correção do `ARCHITECTURE.md` antes do `healthcheck.py` (ver seção "Entregue" acima), por ser a correção mais barata com o maior retorno imediato — já está feita e entregue. Próximo passo natural é começar o `healthcheck.py` (P4) propriamente dito, que agora tem a heurística de status (READY/PLAYBOOK/BLOCKED/BROKEN) já validada.

## 🔍 Análise dos 7 scripts de execução (`healthcheck.py`, `safety_gate.py`, `session_manager.py`, `updater.py`, `verify_all.py`, `auto_preview.py`, `checklist.py`)

Você mandou os 7 scripts reais de `.agent/scripts/`. Acham achados concretos de duplicação e de desalinhamento com o resto do sistema (SKILL.md reais, a convenção `skills/<nome>/scripts/*.py` do `03_execution_protocols.md`, e o `CATALOGO_SKILLS.md`):

1. **`checklist.py` e `verify_all.py` são quase cópia um do outro.** `Colors`, `print_header/step/success/warning/error` e a função `run_script()` estão duplicados quase byte a byte entre os dois arquivos — a única diferença real é a lista de checks (`verify_all.py` tem 13 contra 8 de `checklist.py`).
2. **Nenhum dos dois lê o manifesto que `healthcheck.py` já gera.** Ambos apontam para \~14 caminhos fixos como `.agent/skills/vulnerability-scanner/scripts/security_scan.py`, mas a existência real desses scripts nunca é confirmada por `healthcheck.py` — ele audita a skill inteira (READY/PLAYBOOK/BLOCKED), não os scripts individuais dela. Resultado: os dois orquestradores "avisam e pulam" silenciosamente quando um script não existe, sem isso aparecer em lugar nenhum do healthcheck.
3. **`healthcheck.py` não olha dentro de `skills/<skill>/scripts/`.** `audit_skill()` só varre os arquivos no nível raiz da pasta (`skill_path.iterdir()`). A convenção documentada em `03_execution_protocols.md` é justamente `skills/<skill>/scripts/<script>.py` — uma skill cujo único asset executável está nessa subpasta pode estar sendo classificada errado.
4. **`healthcheck.py` não tem o status `BROKEN`** que o próprio roadmap já havia definido (SKILL.md ausente ou malformado) — só implementa READY/PLAYBOOK/BLOCKED.
5. **`updater.py` procura campos de frontmatter que não existem.** Ele lê `upstream_source` e `last_updated` de cada `SKILL.md`, mas nenhum dos SKILL.md reais que você mandou (nem os do `LEVANTAMENTO_TECNICO_SKILLS.md`) tem esses campos — só o `CATALOGO_SKILLS.md` tem o link do GitHub (coluna "Repositório Oficial"). Hoje esse script provavelmente roda e não encontra nada pra verificar.
6. **`safety_gate.py` só cobre comandos Unix.** A lista `dangerous` tem `rm -rf`, `drop table` etc., mas o kit roda em Windows (`xampp/htdocs`) e tem um agente `devops-engineer` marcado **HIGH RISK** e uma skill `powershell-windows` dedicada — e nenhum equivalente PowerShell/cmd (`Remove-Item -Recurse -Force`, `rd /s /q`, `git push --force`, `git reset --hard`) está coberto.
7. **`session_manager.py` e `auto_preview.py` só reconhecem Node.js.** `analyze_package_json` só detecta stacks via `package.json` (Next/React/Vue/Express/NestJS); não há detecção de `requirements.txt`/`pyproject.toml` (Python/FastAPI/Django) nem `pubspec.yaml` (Flutter) — inconsistente com os agentes `backend-specialist` (skill `python-patterns`) e `mobile-developer` que o próprio sistema já tem. `auto_preview.py` tem o mesmo viés: só tenta `npm run dev`/`npm start`.
8. **`auto_preview.py` "adivinha" a porta no `status`** em vez de persistir a porta real usada no `start` — sempre mostra `localhost:3000 (Likely)` mesmo se o servidor subiu em outra porta.

Nenhum desses scripts hoje chama o outro ou compartilha dados — confirma na prática a necessidade do `agent-cli.py` unificado (P0), e dá a esse item um alvo bem mais concreto do que antes.

### Prompt de implementação (pronto pra usar)

```
Você vai consolidar e corrigir os scripts de execução do Sistema Operacional
Cognitivo (.agent/scripts/). Contexto: healthcheck.py, safety_gate.py,
session_manager.py, updater.py, verify_all.py, auto_preview.py e
checklist.py já existem e funcionam isoladamente, mas têm duplicação de
código e desalinhamentos reais com o resto do sistema (SKILL.md reais, a
convenção skills/<nome>/scripts/*.py de 03_execution_protocols.md,
ARCHITECTURE.md/sync_architecture.py e CATALOGO_SKILLS.md). Faça o
seguinte, nesta ordem:

1. Criar .agent/scripts/_common.py com Colors, print_header/step/success/
   warning/error e run_script(name, script_path, project_path, url,
   timeout) — hoje esse código está duplicado quase byte a byte em
   checklist.py e verify_all.py.

2. Fundir checklist.py e verify_all.py em um único script (checklist.py)
   com uma flag --full que adiciona as categorias extras (SEO/GEO, Mobile,
   i18n, Bundle Analysis) que hoje só existem em verify_all.py. Remover
   verify_all.py depois de migrar tudo.

3. Fazer checklist.py ler a lista de checks a partir do skills_manifest.json
   gerado por healthcheck.py (novo campo "scripts": [...] por skill, a
   criar no passo 4) em vez da lista Python hardcoded de ~14 caminhos
   (security_scan.py, lint_runner.py, schema_validator.py, test_runner.py,
   ux_audit.py, accessibility_checker.py, seo_checker.py, geo_checker.py,
   lighthouse_audit.py, bundle_analyzer.py, playwright_runner.py,
   mobile_audit.py, i18n_checker.py, type_coverage.py,
   dependency_analyzer.py) cuja existência real no disco nunca foi
   confirmada pelo healthcheck.

4. Corrigir audit_skill() em healthcheck.py: hoje só olha os arquivos no
   nível raiz da pasta da skill (skill_path.iterdir()). Adicionar a
   varredura de skill_path / "scripts" (glob *.py e *.js) e registrar cada
   script encontrado no manifesto, alimentando o passo 3. Adicionar também
   o status BROKEN (SKILL.md ausente ou malformado), que falta nas 3
   categorias atuais (hoje só READY/PLAYBOOK/BLOCKED).

5. Corrigir updater.py: ele procura upstream_source e last_updated no
   frontmatter de cada SKILL.md, mas nenhum SKILL.md real tem esses
   campos — só CATALOGO_SKILLS.md tem o link do GitHub (coluna
   "Repositório Oficial"). Fazer updater.py ler o repositório direto de
   CATALOGO_SKILLS.md via regex (não-destrutivo, não exige editar 103
   arquivos). Adicionar suporte a um token via variável de ambiente
   GITHUB_TOKEN no header da requisição — mais de 60 skills com link do
   GitHub estouram o limite de 60 req/hora sem autenticação.

6. Expandir safety_gate.py: a lista "dangerous" atual só cobre comandos
   Unix (rm -rf, drop table etc.), mas o kit roda em Windows e tem um
   agente devops-engineer marcado HIGH RISK e uma skill powershell-windows
   dedicada. Adicionar equivalentes PowerShell/cmd: remove-item -recurse
   -force, rd /s /q, del /f /s /q, format-volume, stop-computer, git push
   --force, git reset --hard, kubectl delete, e comandos de nuvem além de
   gcloud (aws, az).

7. Expandir session_manager.py e auto_preview.py para Python e Flutter, não
   só Node: analyze_package_json hoje só reconhece stacks via
   package.json; adicionar detecção de requirements.txt/pyproject.toml
   (FastAPI/Django/Flask) e pubspec.yaml (Flutter) — o kit tem agentes
   backend-specialist (skill python-patterns) e mobile-developer que esse
   script hoje ignora. Em auto_preview.py, get_start_command hoje só tenta
   npm run dev/npm start; adicionar fallback para uvicorn/flask
   run/python manage.py runserver quando não há package.json. Parar de
   "adivinhar" a porta 3000 em status_server(): persistir a porta real
   usada no start num arquivo de estado (.agent/preview.json) e ler de lá.

8. Depois dos passos 1–7, os 7 scripts (+ healthcheck.py) ficam prontos
   para virar os subcomandos do agent-cli.py unificado (P0 do roadmap) —
   já vão compartilhar _common.py e já vão ler do mesmo manifest. Esse é o
   próximo passo natural depois desta consolidação.

Não altere a lógica de negócio de nenhum check individual (security_scan.py
etc.) — eles não foram fornecidos nesta rodada; o escopo aqui é só os 7
scripts orquestradores + healthcheck.py.
```
