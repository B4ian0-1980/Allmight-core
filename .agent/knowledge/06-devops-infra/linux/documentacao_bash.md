---json
{
  "id": "documentacao_bash",
  "title": "Documentação Bash — Guia Completo",
  "categoria": "06-devops-infra",
  "subcategoria": "linux",
  "resumo": "**Fonte:** [W3Schools Bash](https://www.w3schools.com/bash/index.php) · [GNU Bash Manual](https://www.gnu.org/software/bash/manual/) **Versão:** Bash 5.x",
  "gatilhos": [
    "bash",
    "completo",
    "devops",
    "documentacao",
    "guia",
    "infra",
    "linux"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Bash — Guia Completo?",
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

# Documentação Bash — Guia Completo

> **Fonte:** [W3Schools Bash](https://www.w3schools.com/bash/index.php) · [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)
> **Versão:** Bash 5.x
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Variáveis](#variáveis)
3. [Controle de Fluxo](#controle-de-fluxo)
4. [Funções](#funções)
5. [Strings e Arrays](#strings-e-arrays)
6. [Redirecionamento e Pipes](#redirecionamento-e-pipes)
7. [Manipulação de Arquivos](#manipulação-de-arquivos)
8. [Processos e Jobs](#processos-e-jobs)
9. [sed, awk, grep](#sed-awk-grep)
10. [Boas Práticas e Scripts Comuns](#boas-práticas)

---

## Fundamentos

```bash
#!/bin/bash
# Shebang na primeira linha

echo "Hello, World!"
printf "Nome: %s, Idade: %d\n" "Maria" 30
```

### Executar

```bash
chmod +x script.sh
./script.sh

# ou
bash script.sh
```

### Comentários

```bash
# Comentário de linha

: '
Comentário
multi-linha
'
```

---

## Variáveis

```bash
# Atribuição (SEM espaços ao redor do =)
nome="Maria"
idade=30
readonly PI=3.14159  # Constante

# Usar variável
echo "Nome: $nome"
echo "Nome: ${nome}"
echo "Path: ${HOME}/documentos"

# Variáveis especiais
$0          # Nome do script
$1 $2 $3    # Argumentos posicionais
$#          # Número de argumentos
$@          # Todos os argumentos (como array)
$*          # Todos os argumentos (como string)
$?          # Código de saída do último comando
$$          # PID do processo atual
$!          # PID do último background job

# Variáveis de ambiente
export MINHA_VAR="valor"
echo $PATH
echo $HOME
echo $USER
echo $PWD

# Substituição de comando
data=$(date +%Y-%m-%d)
arquivos=$(ls -1 | wc -l)
data=`date`  # Legado (usar $() )

# Input do usuário
read -p "Nome: " nome
read -sp "Senha: " senha  # Silencioso
read -t 5 input            # Timeout 5s
read -a array              # Array

# Aritmética
resultado=$((5 + 3))
resultado=$((x * y + z))
((contador++))
((total += 10))
```

---

## Controle de Fluxo

### if-else

```bash
# Comparação numérica: -eq -ne -gt -lt -ge -le
if [ "$idade" -ge 18 ]; then
    echo "Adulto"
elif [ "$idade" -ge 12 ]; then
    echo "Adolescente"
else
    echo "Criança"
fi

# Comparação de string: = != -z (vazio) -n (não vazio)
if [ "$nome" = "Maria" ]; then echo "Olá Maria"; fi
if [ -z "$var" ]; then echo "Variável vazia"; fi

# [[ ]] — Bash estendido (mais seguro, suporta regex)
if [[ "$email" =~ ^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$ ]]; then
    echo "Email válido"
fi

# Testes de arquivo
if [ -f "arquivo.txt" ]; then echo "Existe (arquivo)"; fi
if [ -d "diretorio" ]; then echo "Existe (diretório)"; fi
if [ -r "arquivo" ]; then echo "Legível"; fi
if [ -w "arquivo" ]; then echo "Gravável"; fi
if [ -x "arquivo" ]; then echo "Executável"; fi
if [ -s "arquivo" ]; then echo "Não está vazio"; fi

# Operadores lógicos
if [ "$a" -gt 0 ] && [ "$b" -gt 0 ]; then echo "Ambos positivos"; fi
if [[ "$a" -gt 0 || "$b" -gt 0 ]]; then echo "Pelo menos um positivo"; fi
```

### case

```bash
case "$opcao" in
    start|iniciar)
        echo "Iniciando..."
        ;;
    stop|parar)
        echo "Parando..."
        ;;
    restart)
        echo "Reiniciando..."
        ;;
    *)
        echo "Uso: $0 {start|stop|restart}"
        exit 1
        ;;
esac
```

### Loops

```bash
# for
for i in 1 2 3 4 5; do echo $i; done
for i in {1..10}; do echo $i; done
for i in {0..100..5}; do echo $i; done   # Step 5
for file in *.txt; do echo "$file"; done
for ((i=0; i<10; i++)); do echo $i; done

# while
count=0
while [ $count -lt 10 ]; do
    echo $count
    ((count++))
done

# Ler arquivo linha por linha
while IFS= read -r linha; do
    echo "$linha"
done < arquivo.txt

# until
until [ "$resposta" = "sim" ]; do
    read -p "Continuar? " resposta
done

# break e continue
for i in {1..100}; do
    [ $i -eq 50 ] && break
    [ $((i % 2)) -eq 0 ] && continue
    echo $i
done
```

---

## Funções

```bash
# Definição
minha_funcao() {
    echo "Argumento 1: $1"
    echo "Argumento 2: $2"
    return 0  # Código de saída (0-255)
}
minha_funcao "hello" "world"

# Retornar valor (via echo + subshell)
somar() {
    echo $(( $1 + $2 ))
}
resultado=$(somar 5 3)  # 8

# Variáveis locais
processar() {
    local temp="valor local"
    echo "$temp"
}

# Tratamento de erros
set -e         # Sair ao primeiro erro
set -u         # Erro em variável não definida
set -o pipefail # Erro em qualquer comando do pipe
set -euo pipefail  # Combinação recomendada

trap 'echo "Erro na linha $LINENO"; exit 1' ERR
trap 'cleanup' EXIT  # Executar ao sair
```

---

## Strings e Arrays

### Strings

```bash
s="Hello World"
${#s}               # 11 (comprimento)
${s:0:5}            # "Hello" (substring)
${s/World/Bash}     # "Hello Bash" (substituir primeiro)
${s//o/0}           # "Hell0 W0rld" (substituir todos)
${s^^}              # "HELLO WORLD" (upper)
${s,,}              # "hello world" (lower)
${s% *}             # "Hello" (remover do final)
${s#* }             # "World" (remover do início)

# Variável com default
${var:-"default"}   # Usar default se não definida
${var:="default"}   # Definir e usar default se não definida
```

### Arrays

```bash
# Indexed arrays
frutas=("maçã" "banana" "laranja")
frutas+=("uva")
echo ${frutas[0]}          # maçã
echo ${frutas[@]}          # Todos
echo ${#frutas[@]}         # Tamanho
echo ${!frutas[@]}         # Índices
unset frutas[1]            # Remover

# Iterar
for f in "${frutas[@]}"; do echo "$f"; done

# Associative arrays (bash 4+)
declare -A capitais
capitais[Brasil]="Brasília"
capitais[Portugal]="Lisboa"
echo ${capitais[Brasil]}

for pais in "${!capitais[@]}"; do
    echo "$pais: ${capitais[$pais]}"
done
```

---

## Redirecionamento e Pipes

```bash
# Redirecionamento
comando > arquivo.txt       # Sobrescrever stdout
comando >> arquivo.txt      # Append stdout
comando 2> erros.txt        # Stderr
comando &> tudo.txt         # Stdout + stderr
comando > /dev/null 2>&1    # Descartar tudo

# Pipes
cat dados.txt | grep "erro" | sort | uniq -c | sort -rn | head -10

# Here document
cat <<EOF
Nome: $nome
Idade: $idade
EOF

# Here string
grep "padrão" <<< "texto para buscar"

# Process substitution
diff <(ls dir1) <(ls dir2)

# tee (stdout + arquivo)
comando | tee log.txt          # Exibir e salvar
comando | tee -a log.txt       # Append
```

---

## Manipulação de Arquivos

```bash
# Navegação
cd /caminho
pwd
ls -la
ls -lh --sort=time

# Criar
mkdir -p pasta/subpasta
touch arquivo.txt

# Copiar, Mover, Remover
cp -r origem destino
mv arquivo.txt novo_nome.txt
rm -rf diretorio/

# Encontrar
find . -name "*.log" -mtime +30 -delete   # Logs > 30 dias
find . -type f -size +100M                  # Arquivos > 100MB
find . -name "*.py" -exec grep "TODO" {} \;

# Permissões
chmod 755 script.sh    # rwxr-xr-x
chmod +x script.sh     # Adicionar execução
chown user:group arquivo

# Disco
df -h          # Espaço livre
du -sh *       # Tamanho por diretório
```

---

## Processos e Jobs

```bash
# Background
comando &
jobs          # Listar jobs
fg %1         # Trazer para foreground
bg %1         # Enviar para background
wait          # Esperar todos os jobs

# Processos
ps aux | grep nome
kill PID
kill -9 PID       # Forçar
killall nome
top / htop

# Execução paralela
for url in "${urls[@]}"; do
    curl -s "$url" > "output_${url##*/}" &
done
wait
echo "Todos completos"

# xargs (paralelismo)
find . -name "*.jpg" | xargs -P 4 -I {} convert {} -resize 50% "thumb_{}"

# Cron (agendamento)
# crontab -e
# MIN HORA DIA MÊS DIASEM COMANDO
# 0    3    *   *   *      /scripts/backup.sh
# */5  *    *   *   *      /scripts/check.sh
```

---

## sed, awk, grep

```bash
# grep (buscar padrões)
grep "erro" log.txt
grep -i "erro" log.txt        # Case insensitive
grep -r "TODO" src/            # Recursivo
grep -c "padrão" arquivo       # Contar
grep -n "padrão" arquivo       # Com número de linha
grep -v "excluir" arquivo      # Inverter (excluir padrão)
grep -E "regex|pattern" arquivo # Extended regex

# sed (stream editor)
sed 's/antigo/novo/' arquivo              # Substituir primeiro
sed 's/antigo/novo/g' arquivo             # Substituir todos
sed -i 's/antigo/novo/g' arquivo          # In-place
sed -n '5,10p' arquivo                     # Linhas 5-10
sed '/padrão/d' arquivo                    # Deletar linhas
sed 's/^[ \t]*//' arquivo                  # Remover leading spaces

# awk (processamento de texto)
awk '{print $1, $3}' arquivo              # Colunas 1 e 3
awk -F',' '{print $2}' dados.csv          # Separador vírgula
awk '$3 > 1000 {print $1, $3}' dados.txt  # Filtro
awk '{sum+=$2} END {print sum}' dados     # Somatório
awk 'NR>1 {print NR, $0}' arquivo         # Com nº linha (pular header)
```

---

## Boas Práticas

```bash
#!/bin/bash
set -euo pipefail   # Erros estritos
IFS=$'\n\t'         # Separador seguro

# Sempre usar aspas em variáveis
echo "$variavel"     # ✅
# echo $variavel     # ❌ word splitting

# Verificar dependências
command -v docker >/dev/null 2>&1 || {
    echo "Docker não encontrado" >&2
    exit 1
}

# Logging
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >&2; }
log "INFO" "Script iniciado"

# Cleanup com trap
tmpdir=$(mktemp -d)
trap "rm -rf $tmpdir" EXIT

# Usar funções main
main() {
    log "Iniciando..."
    processar_dados
    gerar_relatorio
    log "Concluído!"
}
main "$@"
```

---

*Fonte: [W3Schools Bash](https://www.w3schools.com/bash/) · [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)*
