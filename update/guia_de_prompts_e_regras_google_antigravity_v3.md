# Guia de Prompts e Regras do Google Antigravity

**Economia de tokens e fluxo híbrido (Agente + Tab + Ctrl+I)**

> Versão 3, revisada em 15/10/2026 com base nas páginas oficiais (Rules, Skills, CLI reference, IDE Tab) e em guias da comunidade. Pastas e comandos mudam entre versões; onde a documentação e a comunidade divergem, o texto avisa. Se algo não funcionar, veja a seção 9.
>
> Este arquivo é material de leitura. Não o guarde em `AGENTS.md`, `GEMINI.md` nem em uma regra `always_on`: esses entram no prompt em toda mensagem.

## Objetivo

Gastar menos cota do agente sem perder qualidade, deixando cada ferramenta fazer o que faz melhor:

- **Tab** (Supercomplete, Tab-to-Jump, Tab-to-Import): completa e propaga edições enquanto você digita.
- **`Ctrl+I` (`Cmd+I`):** edição pontual em um trecho, ou comando de terminal em linguagem natural.
- **Agente (`Ctrl+L` / `Cmd+L`):** mudanças em vários arquivos, investigação de bugs, testes.

A economia vem de três alavancas, e o guia segue esta ordem:

1. **Contexto sob demanda (seções 1 a 5):** em vez de repetir instruções em todo chat, use **Rules** e **Skills**. O Antigravity as carrega sozinho e, se você escolher o modo certo, só quando fazem diferença.
2. **Ferramenta certa para cada tarefa (seção 6):** o que cabe no editor não precisa virar tarefa de agente.
3. **Prompts com escopo e hábitos de sessão (seções 7 e 8):** arquivo, linhas, formato da saída, limite, e uma conversa por tarefa.

| Recurso | IDE | CLI (`agy`) |
|---|---|---|
| Rules e Skills (seções 1 a 5) | Sim | Sim |
| Tab e `Ctrl+I` (seção 6) | Sim | Não |
| `/usage`, `/credits`, `/context`, `/clear`, `/effort` (seção 8) | Confirme na interface | Sim |

## Comece em 5 minutos

1. **`AGENTS.md` na raiz do projeto:** copie o bloco da seção 3.
2. **`.agents/rules/esqueleto.md`:** copie o exemplo C da seção 4 (regra `manual`, custo zero até você chamar).
3. **Regras por assunto (opcional):** use os exemplos A e B da seção 4 como modelo e troque o conteúdo pela sua stack.
4. **Skill `fast-check` (opcional):** seção 5; adapte o `check.sh` à sua stack.
5. **Teste:** peça algo trivial, como renomear uma variável em um arquivo. A resposta deve vir em até 3 linhas e sem mexer em outros arquivos. Se não vier assim, veja a seção 9.

## 1. Quanto cada mecanismo custa em tokens

| Mecanismo | O que entra no contexto | Custo | Use para |
|---|---|---|---|
| `AGENTS.md` / `GEMINI.md` na raiz | Conteúdo inteiro, em todo turno | Alto se for longo | Só o essencial (10 a 20 linhas) |
| `AGENTS.md` / `GEMINI.md` em subpasta | Conteúdo inteiro, quando o agente lê ou edita arquivos daquela pasta | Médio | Convenções de um módulo (por exemplo, `src/api/`) |
| Regra `always_on` | Conteúdo inteiro, em todo turno | Alto se for longa | Idem |
| Regra `model_decision` | Só o caminho e a `description`; o agente abre o arquivo se a tarefa combinar | Baixo | Guias detalhados por domínio |
| Regra `glob` | Quando o agente mexe em arquivos que casam com o padrão | Baixo | Padrões por linguagem ou tipo de arquivo |
| Regra `manual` | Só quando você a menciona com `@` no chat | Zero | Checklists raros (revisão, release, esqueleto) |
| Skill | Nome e descrição ficam indexados; o corpo só entra quando a tarefa combina | Baixo | Procedimentos repetíveis, com scripts |

**Regra de ouro:** o que não precisa estar em *toda* mensagem sai do `always_on`.

**Limites da página de Rules:** um arquivo de regra acima de 24.000 bytes é truncado, e as regras globais e `always_on` ativas dividem um orçamento de 20.000 tokens (separado do das skills e MCP). Se o total passar disso, o Antigravity troca os maiores arquivos por ponteiros leves (caminho e `description`), e o agente os lê só quando precisa. É um teto de segurança, não uma meta: quanto menor o `always_on`, menos você paga por mensagem. Por isso, dê uma `description` curta até às regras sempre ativas.

## 2. Onde ficam os arquivos

| Escopo | Regras | Skills |
|---|---|---|
| **Global** (todos os projetos) | `~/.gemini/GEMINI.md`, `~/.gemini/AGENTS.md` ou `~/.gemini/config/rules/*.md`, nos três produtos (app, IDE e CLI). Só a CLI lê também `~/.gemini/antigravity-cli/rules/*.md` | App e IDE: `~/.gemini/config/skills/`. CLI: `~/.gemini/antigravity-cli/skills/`. Legado do IDE: `~/.gemini/antigravity/skills/` |
| **Workspace** (projeto atual) | `AGENTS.md`, `GEMINI.md` ou `.agents/rules/*.md`, na raiz ou em subpastas (o `AGENTS.md` é um formato compartilhado com outras ferramentas, como o Cursor) | `.agents/skills/<nome>/SKILL.md` |

- As pastas no singular (`.agent/rules`, `.agent/skills`) seguem aceitas por compatibilidade com versões antigas.
- O codelab do Google diz que `~/.gemini/config/skills/` vale para os três produtos, enquanto a página oficial de Skills lista outra pasta para a CLI. Se uma skill global não aparecer na CLI, tente a outra.
- Para criar regras pela interface: no IDE, menu `…` do painel do agente, depois **Customizations**, aba **Rules** e **+ Global** ou **+ Workspace**; no app, painel **Customizations**, aba **Rules**. Na CLI, só por arquivo. Os nomes dos menus podem variar por versão.
- Faça commit de `AGENTS.md` e `.agents/`: o time inteiro herda a economia.

## 3. `AGENTS.md` enxuto (sempre ativo)

O `AGENTS.md` é cobrado em **toda** mensagem. Mantenha-o curto e só com o que vale para qualquer tarefa. Ele é Markdown puro, sem frontmatter:

~~~markdown
# Eficiência de tokens

## Contexto
- Busque por texto (grep) e leia por intervalo de linhas antes de abrir arquivos com mais de ~300 linhas.
- Ignore `docs/`, logs, `node_modules/`, builds e lockfiles, a menos que a tarefa dependa deles.
- Cite arquivos como `@caminho/arquivo`; não cole no chat código que já está no arquivo.

## Respostas
- Tarefa simples: aplique a mudança e responda em até 3 linhas (o que mudou e onde).
- Não explique conceitos básicos nem repita o código já aplicado.
- Pergunte só se faltar uma informação que muda o resultado ou se a ação for destrutiva. Uma pergunta por vez.
- Se eu pedir explicação, análise ou detalhes, ignore os limites de tamanho acima.

## Comandos
- Em testes, lint ou build, rode só o escopo afetado e limite a saída (por exemplo, `| tail -n 30`).
- Pare quando o comando passar; não rode a suíte inteira "por garantia".

## Escopo
- Faça só o que foi pedido. Não apague nem reescreva código fora do pedido; sugira em 1 linha.
~~~

Convenções que valem só para um módulo podem ir em um `AGENTS.md` dentro da pasta dele (por exemplo, `src/api/AGENTS.md`). Segundo a documentação, ao ler ou editar um arquivo, o Antigravity sobe a árvore de pastas até a raiz do workspace e carrega o `AGENTS.md` (ou `GEMINI.md`) de cada nível; em conflito, vale a regra do diretório mais específico.

Não coloque regras sobre Tab ou `Ctrl+I` aqui. Esses recursos rodam no editor, e uma instrução permanente só aumentaria o custo de todo turno. Para o modo "só o esqueleto", use a regra `manual` do exemplo C, na próxima seção.

## 4. Regras sob demanda (`.agents/rules/`)

Cada arquivo `.md` em `.agents/rules/` precisa começar com um bloco de frontmatter com um `trigger` válido; sem isso, o Antigravity descarta a regra em silêncio. Só valem os arquivos diretamente nessa pasta: subpastas são ignoradas, a menos que registradas em `.agents/rules.json`.

| Campo | Obrigatório | Função |
|---|---|---|
| `trigger` | Sim | `always_on`, `model_decision`, `glob` ou `manual` |
| `description` | Em `model_decision` (recomendado nas demais) | Resumo que o agente vê para decidir se abre a regra |
| `globs` | Em `glob` | Padrões separados por vírgula, como `"*.py, *_test.py"`. Padrão que começa com `*` precisa de aspas (`glob:` no singular também é aceito) |

**Dica:** escreva a `description` dizendo *quando* a regra se aplica. Uma descrição vaga ("regras do projeto") faz o agente abrir a regra à toa ou ignorá-la.

Os exemplos A e B são ilustrativos (PostgreSQL e Python); troque o conteúdo pelo da sua stack.

### Exemplo A: carregamento por decisão do modelo

`.agents/rules/database-migrations.md`

~~~markdown
---
trigger: model_decision
description: "Use ao criar, revisar ou alterar migrações SQL, schemas de banco de dados ou queries complexas."
---

# Regras de banco de dados
1. Nunca remova ou renomeie colunas em um único deploy; use o padrão expand-and-contract.
2. Em PostgreSQL, crie índices em tabelas existentes com `CONCURRENTLY`.
3. Valide os tipos de dados antes de gerar a migration.
~~~

### Exemplo B: ativação por tipo de arquivo

`.agents/rules/python-tests.md`

~~~markdown
---
trigger: glob
globs: "*_test.py, test_*.py"
description: "Padrões para escrever e executar testes em Python."
---

# Padrões de teste
- Use `pytest` com fixtures enxutas.
- Rode só o arquivo ou a função afetada, com saída curta: `pytest caminho/arquivo.py -k nome_do_teste -x -q`.
~~~

### Exemplo C: regra manual, custo zero até você chamar

`.agents/rules/esqueleto.md`. Para usar, mencione `@esqueleto` no prompt (se não aparecer na lista do `@`, confira o frontmatter).

~~~markdown
---
trigger: manual
description: "Gera só o esqueleto (tipos, interfaces, assinaturas) para eu completar com Tab."
---

# Modo esqueleto
- Crie apenas tipos, interfaces, assinaturas e pontos de entrada, com nomes e padrões consistentes.
- Deixe os corpos vazios (`TODO`) e não explique; vou completar com Tab.
- Responda em 1 linha dizendo o que foi criado e onde.
~~~

### Referenciar sem incorporar (`@`)

Dentro de uma regra, o `@` tem duas formas com custos diferentes, segundo a página de Rules:

| Forma | O que acontece | Custo |
|---|---|---|
| `@../../docs/api.md` | Só referencia o arquivo: o caminho entra na regra e o agente pode abri-lo quando precisar | Baixo |
| `@[API](../../docs/api.md)` | Insere o conteúdo do arquivo dentro da regra, antes da checagem de tamanho | O mesmo de colar o texto na regra |

Os exemplos supõem uma regra em `.agents/rules/`; caminhos relativos partem da pasta da regra. Em regra `always_on`, prefira a primeira forma. Um changelog da comunidade cita suporte a `@caminho/arquivo` também dentro do `AGENTS.md`; confirme na sua versão se o conteúdo é inserido e meça com `/context`.

## 5. Skills para processos repetitivos

Uma skill é uma pasta com um `SKILL.md`. No início da conversa o agente vê só o nome e a descrição; se a tarefa combinar, ele lê o `SKILL.md` inteiro. Você também pode pedir pelo nome ("use a skill fast-check").

A economia vem de **separar instrução e lógica**: o `SKILL.md` diz *o que* fazer, e um script executa e devolve só um resumo, sem que o agente leia logs ou código. A documentação recomenda tratar os scripts como caixas-pretas: o agente roda com `--help` antes de abrir o código-fonte.

~~~text
.agents/skills/fast-check/
├── SKILL.md
└── scripts/
    └── check.sh
~~~

`SKILL.md`:

~~~markdown
---
name: fast-check
description: "Valida lint, tipos e testes e devolve só um resumo curto. Use depois de alterar código."
---

# Validação rápida
1. Na raiz do projeto, rode `bash .agents/skills/fast-check/scripts/check.sh`. Não abra o script nem leia a saída completa; use só o resumo impresso.
2. Se o código de saída for diferente de 0, corrija os erros nas linhas indicadas e rode de novo.
3. Pare ao obter código 0. Só rode a suíte completa se eu pedir.
~~~

`scripts/check.sh` (exemplo para Python; adapte à sua stack):

~~~bash
#!/usr/bin/env bash
# Valida o projeto e imprime só um resumo curto. Rode da raiz do projeto.
set -u

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  echo "Uso: bash check.sh  (da raiz do projeto; imprime só o resumo de lint e testes)"
  exit 0
fi

status=0

run() {  # run <rótulo> <comando...>
  local label="$1"; shift
  local out
  if out=$("$@" 2>&1); then
    echo "OK    $label"
  else
    echo "FALHA $label"
    echo "$out" | head -n 20
    status=1
  fi
}

run "lint"   ruff check --quiet .
run "testes" pytest -x -q
# TypeScript: run "tipos" npx tsc --noEmit --pretty false

exit "$status"
~~~

Cuidados:

- Só a `description` é obrigatória. O `name` é opcional (minúsculas, com hífens; sem ele vale o nome da pasta) e, por segurança, mantenha-o igual ao da pasta.
- Escreva a descrição em terceira pessoa, com palavras-chave de quando usar a skill, e curta: todas as descrições ficam no índice, então descrições longas custam tokens em toda conversa.
- O exemplo roda da raiz do projeto. Em skill global, troque o caminho pelo da pasta da skill (seção 2).
- No Windows, o `bash` precisa estar no PATH (Git Bash ou WSL); sem ele, converta o script para PowerShell.
- Na CLI, `/skills` lista as skills carregadas.

## 6. Fluxo híbrido: qual ferramenta usar

| Situação | Ferramenta | Por quê |
|---|---|---|
| Completar o corpo de uma função ou boilerplate repetitivo | `Tab` (Supercomplete) | Rápido, no próprio editor, sem abrir uma tarefa de agente |
| Aplicar a mesma mudança em vários pontos do arquivo (renomear, ajustar assinatura) | `Tab` com Tab-to-Jump | Pula para o próximo ponto lógico de edição |
| Import faltando | Tab-to-Import | Adiciona o import ao completar o nome |
| Editar um trecho selecionado, ou pedir um comando de terminal em linguagem natural | `Ctrl+I` (`Cmd+I`) | Escopo mínimo e resposta direta |
| Mudança em vários arquivos, investigação de bug, rodar testes | Agente (`Ctrl+L`) com `@arquivos` | Precisa de contexto e de ferramentas |
| Tarefas longas ou paralelas | Agent Manager (`Ctrl+E` alterna com o editor) | Delega sem travar o editor |

**Combinação típica:**

1. O agente cria o esqueleto (`@esqueleto`).
2. Você completa os corpos com `Tab`.
3. `Ctrl+I` ajusta trechos pontuais.
4. O agente roda a skill `fast-check` e corrige o que falhar.

Sobre as configurações de Tab: é possível ligar ou desligar cada recurso (Autocomplete, Supercomplete, Tab-to-Jump, Tab-to-Import), ajustar a velocidade (Tab Speed) e destacar o texto inserido pelo Tab (Highlight Inserted Text), o que ajuda a revisar o que foi completado. Por padrão, o Tab não atua em arquivos listados no `.gitignore` (isso só vale com o git instalado); para mudar, ative **Allow Gitignored Files**.

## 7. Prompts curtos para o dia a dia

**Formato:** objetivo + escopo (`@arquivo`, linhas) + saída esperada + limite.

- **Esqueleto para completar com Tab:**
  > `@esqueleto` Em `@src/services/pagamento.ts`, crie as interfaces e as assinaturas dos métodos de estorno. Sem corpo e sem explicação.

- **Diagnóstico cirúrgico:**
  > Analise só as linhas 45-90 de `@src/api/auth.py` com base no erro abaixo. Diga a causa em 2 linhas e aplique o fix.

- **Refatoração local de um arquivo:**
  > Em `@src/utils/date.ts`, renomeie `parseDate` para `parseISODate` apenas neste arquivo. Liste em 1 linha o que fica pendente em outros arquivos.

- **Planejar antes de executar (tarefas grandes):**
  > Antes de alterar qualquer arquivo, liste em até 8 linhas o que será tocado e em que ordem. Espere meu OK.

- **Revisão do diff:**
  > Revise só o `git diff` atual atrás de bugs e casos de borda. No máximo 5 itens, sem elogios.

## 8. Acompanhar e segurar o consumo

Comandos da **CLI** (`agy`), conforme a página oficial de referência:

| Comando | Para quê |
|---|---|
| `/usage` (ou `/quota`) | Ver o uso da cota por modelo |
| `/credits` | Ver créditos G1 restantes e links de compra |
| `/context` | Ver o que ocupa a janela de contexto |
| `/clear` (ou `/new`) | Limpar a conversa e começar a próxima tarefa do zero |
| `/model` | Escolher o modelo (a escolha persiste entre sessões) |
| `/effort [nível]` | Definir ou consultar o esforço de raciocínio, de `low` a `max`, conforme o modelo |
| `/skills` | Listar as skills carregadas |

**Planejamento:** a tabela oficial lista `/planning` (plano em vários turnos) e `/fast` (modo rápido, que ignora planos de raciocínio), e o menu lateral da página cita `/plan`. Guias da comunidade dizem que `/plan` substituiu `/planning` e que `/fast` foi removido. Digite `/` na CLI para ver o que a sua versão oferece; sem comando, o prompt de planejamento da seção 7 cumpre o mesmo papel. A referência oficial não traz comando de compactação de contexto.

No IDE e no Antigravity 2.0, confirme na interface onde ver cota e créditos; os comandos podem diferir.

**Crédito automático (CLI):** a chave `useG1Credits` do `settings.json` (padrão `false`) faz o uso continuar com créditos pessoais quando a cota do plano acaba. Deixe desligada se não quiser gastar créditos sem perceber.

**Como medir:** para saber se uma mudança nas regras funcionou, rode a mesma tarefa pequena antes e depois e compare `/context` e `/usage`.

Hábitos que mais seguram a cota:

- **Uma conversa por tarefa.** Sessões longas perdem contexto e arrastam histórico desnecessário. Na CLI, use `/clear` entre tarefas.
- **Tarefas pequenas, com escopo explícito** (`@arquivo`, intervalo de linhas) e plano antes de mudanças grandes, para evitar retrabalho.
- **Modelo e esforço proporcionais à tarefa:** modelo mais leve e `/effort` baixo em tarefas simples; reserve o mais forte para raciocínio e refatorações grandes. Evite comandos de raciocínio profundo ou multiagente, como `/boost`, em tarefas simples.

## 9. Se algo não funcionar

- **Regra não é aplicada:** confira o bloco `---` no topo (sem frontmatter válido a regra é descartada em silêncio), o valor de `trigger`, a `description` em `model_decision` e o `globs` em `glob` (entre aspas se começar com `*`). Confirme também que o arquivo está diretamente em `.agents/rules/`, não em subpasta. Em versões antigas, tente `.agent/rules/`.
- **A regra existe, mas as respostas continuam longas:** confirme que o `AGENTS.md` está na raiz do workspace aberto (na CLI, rode dentro do projeto) e procure instruções opostas em `GEMINI.md`, em regras `always_on` ou em um `AGENTS.md` de subpasta. As regras se acumulam, e a do diretório mais específico vence.
- **`AGENTS.md` e `GEMINI.md` com instruções diferentes:** a documentação oficial não define qual dos dois vence. Um guia da comunidade afirma que o `GEMINI.md` prevalece, sem confirmação oficial. Elimine a contradição em vez de depender de precedência.
- **`AGENTS.md` de subpasta não carrega:** a documentação diz que ele é carregado quando o agente lê ou edita arquivos da pasta. Alguns guias citam a opção *Settings → Agent → Load nested AGENTS.md files*, que a documentação oficial não descreve. Se não funcionar na sua versão, use regras `glob`.
- **`AGENTS.md` não é lido em lugar nenhum:** segundo guias da comunidade, versões antigas do IDE só liam o `GEMINI.md`. Atualize o IDE, ou use `GEMINI.md` ou `.agents/rules/`.
- **Skill não aparece:** confira `.agents/skills/<nome>/SKILL.md` (ou a pasta global do seu produto, seção 2), a `description` no frontmatter e, se houver `name`, se é igual ao da pasta. Na CLI, rode `/skills`. Teste também `.agent/skills/` e abra uma conversa nova.
- **Consumo ainda alto:** na CLI, use `/context` para ver o que ocupa a janela. Mova regras `always_on` longas para `model_decision` ou `glob`, troque arquivos incorporados com `@[rótulo](caminho)` por referências, e use `/clear` entre tarefas.

## 10. Fontes

Documentação oficial:

- [Rules](https://www.antigravity.google/docs/rules/)
- [Skills](https://antigravity.google/docs/skills)
- [CLI reference](https://www.antigravity.google/docs/cli/reference)
- [IDE: Tab e navegação](https://www.antigravity.google/docs/ide/tab)
- [Codelab: Authoring Google Antigravity Skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills)

Comunidade:

- [Antigravity CLI cheat sheet](https://computingforgeeks.com/antigravity-cli-cheat-sheet/)
- [Comandos da CLI (cita `/plan` no lugar de `/planning`)](https://toolsbase.dev/en/reference/antigravity-cli-commands)
- [Atalhos do Antigravity](https://fastshortcuts.com/shortcuts/antigravity/)
- [AGENTS.md não funciona? (AGENTS.md vs GEMINI.md)](https://agentpedia.codes/blog/antigravity-agents-md-not-working-fix)
- [Guia de AGENTS.md no Antigravity (cita GEMINI.md como prioritário e a opção de AGENTS.md aninhado)](https://agentpedia.codes/blog/antigravity-agents-md-guide)
- [Regras e AGENTS.md no Antigravity (cita versões antigas do IDE lendo só GEMINI.md)](https://thepromptshelf.dev/blog/google-antigravity-agents-md-rules-guide-2026)
- [Changelog do Antigravity](https://www.gradually.ai/en/changelogs/antigravity/)
