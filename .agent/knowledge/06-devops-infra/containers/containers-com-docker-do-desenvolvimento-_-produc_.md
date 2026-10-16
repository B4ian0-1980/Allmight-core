---json
{
  "id": "containers-com-docker-do-desenvolvimento-_-produc_",
  "title": "Microsoft Word - containers-com-docker-do-desenvolvimento-a-producao.docx",
  "categoria": "06-devops-infra",
  "subcategoria": "containers",
  "resumo": "**Arquivo Original:** `Containers com Docker Do desenvolvimento à producão.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "com",
    "containers",
    "containers-com-docker-do-desenvolvimento-a-producao",
    "desenvolvimento",
    "devops",
    "docker",
    "docx",
    "infra"
  ],
  "perguntas_tipo": [
    "Como utilizar Microsoft Word - containers-com-docker-do-desenvolvimento-a-producao.docx?",
    "Quais as boas praticas de containers?"
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
  "dono": "stack-containers",
  "prioridade": 2
}
---

# Microsoft Word - containers-com-docker-do-desenvolvimento-a-producao.docx

> **Arquivo Original:** `Containers com Docker Do desenvolvimento à producão.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
63214
 

## Página 2

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Página 3

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Página 4

 
 
 
Casa do Código 
 
Prefácio 
 
 
T raduçã o 
Em março de 2013, durante a PyCon US em Santa Clara, nós fizemos a 
primeira demonstração pública do Docker. Não tínhamos ideia de que está- 
vamos prestes a começar a “revolução do container”. 
O que seria essa “revolução do container"? Seria mesmo uma revolução, 
ou um exagero? Afinal, containers têm estado conosco por muito tempo, en- 
tão, por que só agora estamos falando sobre uma revolução? 
Eu gostaria de responder essas questões com uma pequena história. Mais 
de 10 anos atrás, descobri um projeto chamado Xen. V ocê provavelmente já 
ouviu falar sobre ele. Na verdade, se você já usou a Amazon EC2, você com 
certeza o usou. 
Xen é um hypervisor. Ele permite que você rode múltiplas máquinas vir- 
tuais em apenas uma única máquina física. Em 2004, o Xen tinha várias li- 
mitações: só funcionava no Linux, e requeria kernels personalizados. 
Xen podia fazer algo incrível: ele era capaz de fazer live migration (mi- 
gração em tempo real), ou seja, você podia mover uma máquina virtual fun- 
cionando para outra máquina física, sem parar (ou mesmo reinicializar) a 
máquina virtual. 
Eu achei isso bastante impressionante. Mais importante ainda, máquinas 
virtuais Xen podiam iniciar em alguns segundos, e suas perfomances eram 
ótimas. Foi difícil dizer a diferença entre uma máquina física e uma máquina 
virtual. Essas máquinas virtuais eram quase tão boas quando as reais, mas 
elas eram muito mais fáceis de serem instaladas, movidas de lugar, de debug- 
gar e elas eram mais baratas, porque nós podíamos colocar várias máquinas 
virtuais em um único servidor. 
Isso me convenceu de que as máquinas virtuais poderiam ser a base para 
uma hospedagem melhor e mais barata, e eu comecei minha própria compa- 
nhia para vender servidores baseados em máquinas virtuais. 
A tecnologia era boa, porém muitas pessoas eram céticas e queriam os 
servidores de verdade. Lembre-se de que isso foi poucos anos antes da Ama- 
zon Web Services lançar a EC2. 

## Página 5

Dez anos depois, o sentimento havia mudado. Claro que ainda havia apli- 
cações que não podiam ser rodadas “na nuvem” por diversos motivos; mas a 
maioria dos novos d e p l o ys agora envolviam IAAS (Infrastructure as a Service) 
ou P AAS (Platform as a Service) em algum ponto. 
Qual foi a razão para essa mudança? Seria essa feature mágica de migra- 
ção em tempo real? Não. Seria porque máquinas virtuais são mais baratas que 
as físicas? Não. A verdadeira razão é a automatização. Agora, nós podemos 
escrever programas e scripts para criar servidores, implantar nossas aplica- 
ções neles, e escalá-las verticalmente de forma fácil. Em nossos repositórios, 
nós temos arquivos infrastructure as c o d e (infraestrutura como código), des- 
crevendo arquiteturas complexas compostas por dezenas, centenas, milhares 
de servidores; e quando nós mudamos esses arquivos, as máquinas são provi- 
 
v 
 

## Página 6

 
Casa do Código 
 
sionadas e destruídas da forma correta. Essa é a revolução que a virtualização 
tornou possível. 
Com containers, nós vamos ver uma revolução similar. Muitas coisas 
que eram consideradas impossíveis ou impraticáveis estão se tornando não 
só possíveis, como fáceis. Teste e integração contínua; infraestrutura imutá- 
vel; bl ue /g r een e canary r eleases; g o l d e n i m ag es...  Todas essas técnicas (e mais) 
estão agora disponíveis para a maioria dos desenvolvedores, em vez de se- 
rem um luxo ou um privilégio das maiores e modernas organizações como 
Amazon, Google, ou Netflix. 
Hoje, quando eu ouço alguém dizer “containers não vão trabalhar para 
nós”, eu ouço a mesma voz que diziam “máquinas virtuais não vão trabalhar 
para nós” há dez anos. Não seja essa voz. Não estou pedindo para você abraçar 
os containers para todos os usos e propósitos. Porém, neste livro, você verá 
muitas formas nas quais o Docker e os containers podem melhorar o desen- 
volvimento e d e p l o y de sua aplicação. Com certeza você achará pelo menos 
uma que fará o seu trabalho e sua vida mais fáceis! 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
vi 
  

## Página 7

 
Casa do Código Sumário 
 
 
 
 
 
 
 
Sumário 
 
 
 
 
1 Introdução 1 
1.1 O que é Docker? . . . . . . . . . . . . . . . . . . . . . . . . . . 3 
1.2 O que diferencia um container de uma máquina virtual? . . 4 
1.3 O que são Namespaces? . . . . . . . . . . . . . . . . . . . . . . 5 
1.4 Para que serve o Cgroups? . . . . . . . . . . . . . . . . . . . . 6 
1.5 O que é Union file systems? . . . . . . . . . . . . . . . . . . . 6 
 
2 Explorando o Docker 7 
2.1 Instalação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 
2.2 Hello, Docker! . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 
2.3 Um pouco de interatividade . . . . . . . . . . . . . . . . . . . 9 
2.4 Controlando containers . . . . . . . . . . . . . . . . . . . . . . 11 
2.5 Destruindo imagens e containers . . . . . . . . . . . . . . . . 14 
 
3 Construindo minha primeira im agem 17 
3.1 Como funciona a construção de uma imagem? . . . . . . . . 18 
3.2 Explorando o Dockerfile . . . . . . . . . . . . . . . . . . . . . 19 
3.3 Mapeando portas . . . . . . . . . . . . . . . . . . . . . . . . . 21 
3.4 Copiando arquivos . . . . . . . . . . . . . . . . . . . . . . . . . 23 
3.5 Definindo o diretório de trabalho . . . . . . . . . . . . . . . . 26 
3.6 Inicializando serviços . . . . . . . . . . . . . . . . . . . . . . . 28 
3.7 Tratando logs . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 
3.8 Exportação e importação de containers . . . . . . . . . . . . . 31 
 
vii 
  

## Página 8

 
Sumário Casa do Código 
 
4 T rabalhando com volumes 33 
4.1 Gerenciando os dados . . . . . . . . . . . . . . . . . . . . . . . 34 
4.2 Utilizando volumes no Dockerfile . . . . . . . . . . . . . . . . 35 
4.3 Backup e restore de volumes . . . . . . . . . . . . . . . . . . . 38 
 
5 Configurações d e rede 4 3 
5.1 Comunicação entre containers . . . . . . . . . . . . . . . . . . 43 
5.2 Alterando a configuração default . . . . . . . . . . . . . . . . 45 
5.3 Comunicação de containers no mesmo host . . . . . . . . . . 47 
5.4 Comunicação de containers em hosts diferentes . . . . . . . . 49 
5.5 Comunicação com automação . . . . . . . . . . . . . . . . . . 51 
 
6 Docker Hub 53 
6.1 Buscando e puxando imagens . . . . . . . . . . . . . . . . . . 53 
6.2 Enviando imagens para um repositório . . . . . . . . . . . . . 54 
 
7 T rabalhando com Docker 57 
7.1 Preparando o ambiente . . . . . . . . . . . . . . . . . . . . . . 58 
7.2 Entendendo como funciona . . . . . . . . . . . . . . . . . . . 61 
7.3 Executando em produção . . . . . . . . . . . . . . . . . . . . . 61 
7.4 Um pouco de integração contínua . . . . . . . . . . . . . . . . 65 
7.5 Limitando o uso de recursos . . . . . . . . . . . . . . . . . . . 68 
7.6 Orquestrando containers . . . . . . . . . . . . . . . . . . . . . 70 
 
8 Explorando um pou co mais 81 
8.1 Docker Remote API . . . . . . . . . . . . . . . . . . . . . . . . 81 
8.2 TDD para Docker . . . . . . . . . . . . . . . . . . . . . . . . . 86 
8.3 Docker no desktop . . . . . . . . . . . . . . . . . . . . . . . . . 90 
 
9 Um pouco sobre CoreOS Linux 9 3 
9.1 Principais diferenças . . . . . . . . . . . . . . . . . . . . . . . . 93 
9.2 ETCD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94 
9.3 Fleet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96 
 
viii 
 

## Página 9

 
Casa do Código Sumário 
 
9.4 Criando um cluster . . . . . . . . . . . . . . . . . . . . . . . . 97 
9.5 Criando um serviço . . . . . . . . . . . . . . . . . . . . . . . . 101 
9.6 Registrando um serviço . . . . . . . . . . . . . . . . . . . . . . 102 
9.7 Inicializando o cluster . . . . . . . . . . . . . . . . . . . . . . . 103 
 
10 O qu e estudar além? 107 
10.1 A alternativa ao Docker Compose, o azk . . . . . . . . . . . . 107 
10.2 Docker Machine . . . . . . . . . . . . . . . . . . . . . . . . . . 108 
10.3 Docker Swarm . . . . . . . . . . . . . . . . . . . . . . . . . . . 109 
10.4 Alpine Linux . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111 
10.5 Dúvidas? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113 
V ersão: 18.9.4 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Página 10

 
 
Capítulo 1 
Introdução 
 
 
V ocê finalizou um longo processo de desenvolvimento de um software. 
Agora, é necessário configurar e organizar a infraestrutura para fazer o de- 
ploy de sua aplicação e pôr em produção. 
De modo geral, você segue um roteiro com vários passos para realizar essa 
tarefa: instalação e configuração dos servidores, ajustes na aplicação para ser 
disponibilizada por um w e b server, estabelecer comunicação com o banco de 
dados, e outras dezenas de configurações até que a aplicação seja publicada e 
comece a funcionar. 
É muito grande o tempo gasto na etapa de configuração. Mesmo utili- 
zando automatizadores como Puppet, Chef ou Ansible, você ainda enfrenta 
alguns problemas para manter a infraestrutura. 
Agora, imagine que a sua aplicação está separada em várias camadas – por 
exemplo, front-end, back-end, banco de dados, workers etc. –, e você precisa 
 
 
 

## Página 11

 
Casa do Código 
 
fazer a aplicação funcionar em diferentes ambientes – desenvolvimento, pro- 
dução ou algum servidor customizado. Tudo isso sai fora de controle, pois 
você acaba instalando a mesma aplicação de diferentes formas em vários am- 
bientes. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 1.1: Matrix from hell 
 
 
Além dos problemas citados, ainda temos o alto custo se cada camada es- 
tiver alocada em um servidor. Esses e outros problemas podem ser resolvidos 
com Docker, uma vez que podemos isolar e manter a mesma configuração de 
cada serviço, ou camada da nossa aplicação, em diferentes ambientes: 
 
 
 
 
 
 
 
 
2 
  

## Página 12

 
Casa do Código Capítulo 1. Introduç ão 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 1.2: Resolvendo o problema com Docker 
 
 
1.1 O que é Docker? 
Imagine que o servidor é um navio cargueiro e que cada container leva várias 
mercadorias. Docker é uma ferramenta para criar e manter containers, ou 
seja, ele é responsável por armazenar vários serviços de forma isolada do SO 
ho st, como: web server, banco de dados, aplicação, memcached etc. O seu 
back-end é baseado em LXC (LinuX Containers). 
LXC funciona isolando processos do sistema operacional host. É uma es- 
pécie de virtualização bastante leve, pois não faz uso de emulação ou suporte 
a hardware, apenas proporciona a execução de vários sistemas Linux de forma 
isolada – daí vem a palavra container. Além disso, ele utiliza o mesmo Linux 
Kernel do servidor host, o que torna tudo muito rápido. 
Em outras palavras, o Docker é uma alternativa para virtualização com- 
pleta e leve se comparada aos hypervisors KVM, Xen e VMware ESXi. 
 
3 
  

## Página 13

 
1.2. O que diferencia um container de uma máquina virtual? Casa do Código 
 
1 . 2 O que diferencia u m container de uma má- 
quina virtual? 
Para entender melhor a diferença entre virtualização e containers, vamos re- 
lembrar primeiro os tipos de virtualização. 
Em resumo, temos os seguintes tipos: 
 
• Bare Metal 
• Hosted 
 
No Bare Metal, o software que proporciona a virtualização é instalado 
diretamente sobre o hardware, por exemplo, Xen, VMware ESXi e Hyper-V. 
Esse tipo de virtualização proporciona um isolamento maior e, ao mesmo 
tempo, uma sobrecarga, pois cada máquina virtual que é criada executará seu 
próprio kernel e instância do sistema operacional. Já o tipo h o s t e d, o software 
que proporciona a virtualização é executado sobre um sistema operacional, 
por exemplo, o VirtualBox. 
A virtualização por containers, proposta pelo LXC, ocorre de forma me- 
nos isolada, pois compartilha algumas partes do kernel do host, fazendo com 
que a sobrecarga seja menor. 
Na figura a seguir, veja a comparação entre máquinas virtuais e Docker 
containers: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
4 
  

## Página 14

 
Casa do Código Capítulo 1. Introduç ão 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 1.3: Diferença entre Docker e máquinas virtuais 
 
 
O Linux Kernel possui um recurso chamado de Cg r oups (control g r o u p s), 
que é usado para limitar e isolar o uso de CPU, memória, disco, rede etc. Um 
outro recurso são os N am e sp ac es, responsáveis por isolar grupos de processos, 
de modo que eles não enxerguem os processos de outros grupos, em outros 
containers ou no sistema host. 
Resumindo, containers são mais leves, já que não precisam de um ambi- 
ente virtual completo, pois o kernel do host proporciona total gerenciamento 
de memória, I/O, CPU etc. Isso significa que o processo total de inicialização 
pode levar poucos segundos. 
 
1.3 O que são Namespaces? 
Como vimos na seção anterior, o Docker tira proveito do recurso de N am e s- 
p a c e s para prover um espaço de trabalho isolado para os containers. Sendo 
assim, quando um container é criado, automaticamente um conjunto de na- 
mespaces também é criado para ele. 
N am e sp ac es cria uma camada de isolamento para grupos de processos. 
No caso do Docker, são estes:  
• pid – isolamento de processos (PID); 
 
5 
  

## Página 15

 
1.4. Para que serve o Cgroups? Casa do Código 
 
• net – controle de interfaces de rede; 
• ipc – controle dos recursos de IPC (InterProcess Communication); 
• mnt – gestão de pontos de montagem; 
• uts – UTS (Unix Timesharing S yst em) isolar recursos do kernel; 
 
1 . 4 Pa r a que serve o Cgroups? 
O segredo para executar aplicações de forma isolada é liberar apenas os recur- 
sos que você deseja. O Cgr ou ps permite que o Docker compartilhe os recursos 
de hardware existentes no host com os containers e, caso seja necessário, pode 
definir limites de uso e algumas restrições. 
Por exemplo, veremos como limitar o uso de memória para um container 
específico. 
 
1.5 O que é Union f ile systems? 
Union file syst em s (ou UnionFS) são sistemas de arquivos que funcionam por 
meio da criação de camadas. Eles são leves e muito rápidos. 
O Docker utiliza sistemas de arquivos em camadas para a construção de 
imagens que serão usadas na criação de containers. 
 
 
Todos os códigos-fontes do livro podem ser encontrados em: https: 
//github.com/infoslack/docker-exemplos. 
V ocê também pode participar ativamente do grupo de discussão so- 
bre o livro, em: docker.infoslack.com 
Boa leitura! 
 
 
 
 
 
 
 
 
6 
  

## Página 16

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Capítulo 2 
Explorando o Docker 
 
 
Por ser baseado em LXC, o Docker funciona somente no Linux. Para que o 
Docker funcione em outros sistemas operacionais, é necessário ter uma má- 
quina virtual com Linux. Na seção a seguir, veremos algumas opções para 
instalação. 
 
2 . 1 Instalação 
 
Instalando no Linux 
No Ubuntu, para instalar e começar a utilizar o Docker é muito simples. Pri- 
meiro, vamos precisar de alguns pacotes adicionais: 
 
 
 
 
 
  

## Página 17

 
2.2. Hello, Docker! Casa do Código 
 
 
 
Em seguida, é necessário incluir o repositório oficial do Docker ao nosso 
gerenciador de pacotes – pois queremos instalar a última versão estável – e 
atualizar a nossa lista de pacotes para executar a instalação: 
 
 
 
 
 
 
 
 
Pronto, o Docker está instalado e agora podemos executar o nosso pri- 
meiro teste. 
 
2 .2 He l l o , Docker! 
Para o nosso primeiro exemplo, vamos criar um container e solicitar para que 
ele execute algum comando: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
V amos entender por partes o que aconteceu. Primeiro, o Docker fez o 
download de uma imagem base, no caso do repositório oficial do Ubuntu, 
na última versão estável 1 4 . 0 4 LTS. Assim, ele instanciou um novo contai- 
ner, configurou a interface de rede e escolheu um IP dinâmico para ele. Em 
 
8 
  

## Página 18

 
Casa do Código Capítulo 2. Explorando o Docker 
 
seguida, selecionou um sistema de arquivos para esse novo container, e exe- 
cutou o comando /b i n / ec h o graças ao run, que é uma opção utilizada pelo 
Docker para enviar comandos ao container. No final da execução, o Docker 
capturou a saída do comando que injetamos. 
Não se preocupe se você não entendeu todos os detalhes neste momento. 
V eremos com calma todas as opções oferecidas. 
 
2 . 3 Um pouco de interatividade 
O Docker oferece um leque de opções que o torna bastante interativo com 
os containers. Por exemplo, podemos verificar a existência de containers em 
execução com o comando do cker ps: 
 
 
 
Como não possuímos nenhum container em execução ainda, a saída do 
comando foi apenas o cabeçalho. Para o próximo exemplo, vamos criar um 
container e acessar o seu shell interativo: 
 
 
 
Desta vez, utilizamos outras opções: -i e -t em conjunto com a run. O 
parâmetro -i diz ao Docker que queremos ter interatividade com o contai- 
ner, e o -t que queremos nos linkar ao terminal do container. Em seguida, 
informamos o nome da imagem usada, no caso Ubuntu, e passamos o co- 
mando / b i n / b a s h como argumento. 
Agora que temos acesso ao shell do container, vamos conferir algumas 
informações para entender melhor o que está acontecendo. Por exemplo, ao 
verificarmos o arquivo /etc/lsb-release, podemos ter certeza de que 
este shell está sendo executado em um sistema diferente: 
 
 
 
 
 
 
9 
  

## Página 19

 
2.3. Um pouco de interatividade Casa do Código 
 
 
 
 
Ou ainda, podemos conferir que o container que estamos acessando pos- 
sui um IP diferente da faixa utilizada pelo host: 
 
 
 
 
 
 
Explore mais um pouco antes de sair do container. Navegue em seus di- 
retórios e confira alguns arquivos. Eu espero! 
 
 
Agora que você já fez um tour, podemos continuar! 
Ao sair do container, ele será colocado em estado de pausa pelo Docker. 
V amos conferir usando o complemento -a ao parâmetro ps; isso significa 
que queremos listar todos os containers que foram inicializados ou pausados. 
Para melhor visualização, formatei de uma forma diferente: 
 
 
 
 
 
 
 
 
 
 
Note o status que informa quando o container foi finalizado. Entretanto, 
o seu processo ainda existe e está pausado. 
Uma outra opção que utilizaremos bastante é a -q, que retorna apenas o 
ID do container: 
 
 
 
 
 
10 
  

## Página 20

 
Casa do Código Capítulo 2. Explorando o Docker 
 
A partir da versão 1.5, o Docker possui a feature stats, que informa, 
em tempo de execução, detalhes sobre o nível de consumo de recursos na 
máquina host, feito pelos containers. V eja em código: 
 
 
 
 
 
 
No primeiro exemplo, quando criamos o container, junto a ele geramos 
uma imagem. Imagens podem ser listadas com a opção images: 
 
 
 
 
V oltando à listagem de containers, removeremos o container criado com 
a opção rm – isso mesmo, igual ao comando do Linux! Junto ao comando, é 
necessário informar o nome ou ID: 
 
 
 
 
 
 
 
 
2.4 Controlando containers 
Ainda utilizando a imagem que foi construída no primeiro exemplo, vere- 
mos agora como vamos controlar o funcionamento dos containers. Para isso, 
vamos criar um novo container e fazer a instalação do web server Nginx: 
 
 
 
Perceba o uso da opção --name, onde foi informado um apelido para o 
novo container criado. Agora que estamos no shell da nova instância, vamos 
atualizar os pacotes e, em seguida, instalar o Nginx: 
 
11 
  

## Página 21

 
2.4. Controlando containers Casa do Código 
 
 
 
 
 
 
 
 
É importante saber que toda e qualquer alteração realizada dentro de um 
container é volátil. Ou seja, se o finalizarmos, ao iniciar novamente essa ins- 
talação do Nginx, a alteração não vai permanecer. 
Para tornar as alterações permanentes, é necessário commitar o container 
– sim, o Docker possui um recurso para versionamento igual ao Git. Sempre 
que um commit for feito, estaremos salvando o estado atual do container na 
imagem utilizada. 
Para isso, basta usarmos o ID ou o apelido do container: 
 
 
 
Ao executar o commit, estamos criando uma nova imagem baseada na 
inicial. A nomenclatura utilizada ubuntu/nginx é o nome da nova imagem. 
V erifique com o do cker images: 
 
 
 
 
 
Com a nova imagem gerada contendo o Nginx instalado, agora vamos 
explorar um pouco mais. É possível criar containers autodestrutivos com o 
uso da opção --rm. Isso significa que, ao finalizar a execução do container, 
ele será excluído automaticamente. Para exemplificar, vamos criar uma nova 
instância com os seguintes argumentos: 
 
 
 
 
Observe o uso da opção -p. Com ela, estamos informando ao Docker que 
a porta 8080 no host será aberta e mapeada para a porta 80 no container, 
 
1 2 
  

## Página 22

 
Casa do Código Capítulo 2. Explorando o Docker 
 
estabelecendo uma conexão entre eles. Dentro da nova instância, executei o 
comando service n g i n x start, para inicializar o Nginx. 
Para entender melhor o -p 8080:80, podemos abrir o b r owser e acessar 
o seguinte endereço: http://localhost:8080/. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 2.1: Nginx funcionando em um container 
 
 
O acesso ao Nginx dentro do container está passando para a porta 8080 
no host local. 
De volta à nossa instância, vamos finalizar saindo do container, e ver o 
que o parâmetro --rm pode fazer: 
 
 
 
 
 
O container só existiu enquanto estávamos dentro dele. Outra opção bas- 
tante usada é o -d, pois envia toda a execução para b ack gr ound. Para testar, 
execute o código: 
 
 
 
 
 
 
13 
  

## Página 23

 
2.5. Destruindo imagens e containers Casa do Código 
 
O processo do novo container foi enviado para background, e o Docker 
retornou o ID da nova instância. 
Podemos conferir se o container está em execução, ao executarmos o co- 
mando ps -q: 
 
 
 
Ou simplesmente acessando no browser o endereço http://localhost: 
8080/. 
Já temos uma instância em plano de fundo com o Nginx funcionando. 
Agora, vamos manipular o seu funcionamento utilizando as opções s to p e 
start. Para isso, basta indicar o nome do container ou o seu ID: 
 
 
 
 
 
 
 
 
 
 
Note que, ao executar o s to p, quando verificamos se o processo que faz 
referência ao container existe, nada é retornado. Isso acontece, pois o pro- 
cesso está em pausa. 
 
2 . 5 Destruindo imagens e containers 
Já vimos como destruir containers utilizando a opção rm. Para destruir ima- 
gens, usamos o r mi, ao indicarmos o ID da imagem que queremos apagar: 
 
 
. 
É possível apagar todos os containers e imagens de uma só vez. Para isso, 
basta um pouco de shell script: 
 
14 
  

## Página 24

 
Casa do Código Capítulo 2. Explorando o Docker 
 
 
 
 
O mesmo serve para apagar imagens: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
No próximo capítulo, veremos como podemos criar e gerenciar nossas 
imagens de forma programada. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
15 
  

## Página 25

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Página 26

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Capítulo 3 
Construindo minha primeira 
imagem 
 
 
Antes de começar a executar comandos e partir para o ataque criando a sua 
primeira imagem, é preciso conhecer sobre o Dockerfile. Ele é um recurso 
feito para automatizar o processo de execução de tarefas no Docker. 
Com este recurso, podemos descrever o que queremos inserir em nossa 
imagem. Desta forma, quando geramos um build, o Docker cria um snapsh ot 
com toda a instalação que elaboramos no Dockerfile. 
 
 
 
 
 
 
 
 
 
  

## Página 27

 
3.1. Como funciona a construç ão de uma imagem? Casa do Código 
 
3.1 Como funciona a construção de uma ima- 
gem? 
Antes de prosseguir, vamos entender como o Docker trabalha durante a etapa 
de construção de uma imagem. Quando criamos um container, o Docker 
monta o r ootfs em modo read-only, igual ao processo de b o o t tradicional em 
qualquer Linux. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 3.1: Layers durante criação de container 
 
 
O r ootfs (ou r oot file syst em) inclui a estrutura típica de diretórios ( /dev, 
/ p r o c, /bin, /etc, /lib, /usr e /tmp), além de todos os arquivos 
de configuração, binários e bibliotecas necessários, para o funcionamento de 
programas. 
Em vez de alterar o sistema de arquivos para o modo read-write, o Docker 
tira proveito do unionfs, criando uma camada com permissões de read-write 
sobre a camada de read-only. 
 
 
18 
  

## Página 28

 
Casa do Código Capítulo 3. Construindo minha primeira imagem 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 3.2: Modos de read-write e read-only na construção da imagem 
 
 
Desta forma, a camada do topo é criada em modo read-write quando ini- 
cializamos um container. Se um programa for instalado, ele não vai existir 
na imagem base. Em vez disso, será criada uma nova camada sobre a base, 
contendo a instalação do programa. 
Agora que ficou clara a forma como o Docker trabalha para construir uma 
imagem, podemos prosseguir. 
 
3 . 2 Explorando o Dockerfile 
O Dockerfile é um arquivo que aceita rotinas em shell script para serem exe- 
cutadas. V eja a seguir como ficaria o processo de instalação do Nginx, que 
 
19 
  

## Página 29

 
3.2. Explorando o Dockerfile Casa do Código 
 
fizemos no capítulo anterior, em um script Dockerfile: 
 
 
 
 
 
 
 
 
 
V amos por partes: 
 
• F R O M – estamos escolhendo a imagem base para criar o container; 
• MAINTAINER – especifica o nome de quem vai manter a imagem; 
• RU N – permite a execução de um comando no container. 
 
Note a simplicidade! Com apenas 4 linhas no nosso script, podemos gerar 
a nova imagem e instalar o Nginx. 
V amos continuar o processo e gerar a nossa primeira imagem com a op- 
ção build: 
 
 
O ponto no final indica o path do script de Dockerfile para gerar a ima- 
gem, supondo que você está executando o comando no mesmo diretório onde 
o Dockerfile se encontra. 
V amos conferir se a imagem realmente foi gerada da seguinte forma: 
 
 
 
 
 
 
O próximo passo é testarmos a imagem que foi gerada criando um con- 
tainer, e dizer que queremos utilizar a porta 8080 no nosso host, assim como 
fizemos no capítulo anterior. 
 
 
20 
  

## Página 30

 
Casa do Código Capítulo 3. Construindo minha primeira imagem 
 
 
 
 
 
Mais uma vez, teste entrando em http://localhost:8080/, para garantir que 
está tudo funcionando. 
Se preferir, teste direto no console utilizando o curl, para acessar a URL 
enviando um r equ est. Assim, só precisamos observar o status c o d e: 
 
 
 
 
 
 
 
 
 
 
 
 
 
3 . 3 Mapeando portas 
O comando para execução de um container com Nginx está um pouco 
grande. V amos reduzir a instrução de inicialização inserindo a opção 
EXPOSE no nosso Dockerfile. Além disso, faremos uso de um atalho para 
mapeamento de portas, o parâmetro -P. 
No Dockerfile, adicionamos a instrução EXPOSE: 
 
 
 
 
 
 
 
 
 
 
 
Em seguida, nós atualizamos a imagem executando o build novamente: 
 
21 
  

## Página 31

 
3.3. Mapeando portas Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Note que o Docker apenas atualizou a imagem que já existia, acrescen- 
tando a instrução para expor a porta 80 sempre que um novo container for 
criado. 
Agora, podemos testar criando uma nova instância: 
 
 
 
Ao criar um container passando a instrução -P, estamos permitindo 
que o Docker faça o mapeamento de qualquer porta utilizada no container, 
para alguma outra porta no host. Conferiremos isso com o do cker ps, ou 
usando o seguinte atalho: 
 
 
 
Ou podemos utilizar especificando a porta do container: 
 
 
 
 
22 
  

## Página 32

 
Casa do Código Capítulo 3. Construindo minha primeira imagem 
 
Sempre que um container for criado desta forma, o retorno da instrução 
- P será uma porta aleatória criada no host. Se testarmos o acesso ao Nginx 
na porta criada, teremos o seguinte retorno: 
 
 
 
 
 
3 .4 Copiando arquivos 
Temos um pequeno problema ao utilizar a porta 8080, pois o Nginx está 
configurado para utilizar a porta 80. Podemos criar um container acessando 
o seu shell, atualizar a sua configuração, sair e commitar a imagem. 
Imagine se você precisar fazer várias alterações nos arquivos de configu- 
ração do web server, a produtividade pode ser comprometida. Para resolver 
isso, vamos utilizar a opção A DD no Dockerfile. Desta forma, vamos refe- 
renciar o arquivo que queremos copiar e o local de destino para a imagem 
durante o processo de build. 
 
 
 
 
 
 
 
 
 
 
 
 
 
Com a instrução A DD, o arquivo chamado exemplo será copiado para 
o diretório /etc/nginx/sites-enabled, e será chamado de default. 
O arquivo exemplo deve existir no mesmo contexto do Dockerfile. O seu 
conteúdo é bem simples e foi alterado apenas para o Nginx utilizar a nova 
porta, no nosso caso, a 8080. 
 
 
23 
  

## Página 33

 
3.4. Copiando arquivos Casa do Código 
 
 
 
 
 
 
 
 
 
 
Agora, podemos executar o nosso processo de build e gerar a nova ima- 
gem, e o arquivo será copiado para as configurações do Nginx: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Observe as etapas, estão na ordem em que colocamos no Dockerfile. En- 
tão, vamos criar um novo container, sem informar instruções de portas, e 
testar para ver se está tudo certo: 
 
 
 
24 
  

## Página 34

 
Casa do Código Capítulo 3. Construindo minha primeira imagem 
 
 
 
 
Como resposta, recebemos um erro em nosso teste. Será que esquecemos 
alguma coisa? Não, não esquecemos de nada. 
Quando utilizamos o -p ou o -P, estamos mapeando uma porta interna 
do container para uma porta em nosso host local. Agora verificaremos o fun- 
cionamento do Nginx acessando o diretamente o IP do container. 
Para capturar informações do container, podemos fazer uso da opção 
inspect, que retorna informações low-level de um container, ou de uma 
imagem. 
V eremos em um capítulo posterior mais detalhes sobre a API do Docker. 
Por enquanto, vamos apenas analisar o retorno do seguinte comando: 
 
 
Como o retorno do comando é muito grande, você pode consultá-lo em 
http://bit.ly/docker-inspect. 
Para continuarmos, vamos filtrar a saída usando o grep: 
 
 
 
Aí está o IP do nosso container. Outra opção seria executar o comando 
ifconfig diretamente no container. A partir da versão 1.3 do Docker, temos 
a opção exec justamente para facilitar testes rápidos nos containers: 
 
 
 
 
 
 
 
 
 
 
 
Bem, já temos o IP que está sendo utilizado, então podemos refazer o teste 
de r eq uest na porta 8080, e verificar o funcionamento: 
 
25 
  

## Página 35

 
3.5. Definindo o diretório de trabalho Casa do Código 
 
 
 
 
 
3 . 5 Definindo o diretório de trabalho 
A área de trabalho padrão do Docker é o diretório raiz /. Podemos alterar 
isso durante a criação de um container ao usarmos a opção -w, ou tornando 
padrão usando a diretiva WORKDIR no Dockerfile. 
Imagine que queremos utilizar um container para desenvolvimento de 
um projeto Ruby on Rails. O Dockerfile poderia ser adicionado dentro do 
diretório do projeto e teria as seguintes configurações: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Com o diretório de trabalho definido em WORKDIR, temos antes dele o 
A DD ./ /rails, que copia os arquivos a partir do contexto no qual foi exe- 
cutado para o filesystem do container. 
Lembre-se de que este arquivo Dockerfile, neste exemplo, está dentro do 
projeto Rails: 
 
26 
  

## Página 36

 
Casa do Código Capítulo 3. Construindo minha primeira imagem 
 
 
 
 
 
 
 
 
Com a nova imagem gerada, vamos criar um novo container: 
 
 
Para entendermos o que de fato aconteceu nas instruções A DD e 
WORKDIR, que foram adicionadas ao Dockerfile, podemos acessar o container 
utilizando o exec: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
27 
  

## Página 37

 
3.6. Inicializando serviços Casa do Código 
 
Basicamente agora a área de trabalho principal dentro deste container é 
a própria aplicação Rails. Desta forma, poderíamos usar este container como 
ambiente de desenvolvimento. 
 
3.6 Inicializando serviços 
O comando utilizado para geração de containers ficou bem menor. Entre- 
tanto, podemos reduzi-lo um pouco mais, informando no Dockerfile a ins- 
trução CMD, para que ele possa inicializar o Nginx sempre que um container 
novo for criado. V amos à edição: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Recrie a imagem, inicialize um container e faça o teste de r eq ues t: 
 
 
 
 
 
 
Existe outra forma de inicializar serviços, utilizando ENTRYPOINT. Sem- 
pre que usamos CMD em seu background, ele está chamando o b ash assim: 
/bin/sh -c. Em seguida, envia como parâmetro o comando ou instrução 
que especificamos. 
 
28 
  

## Página 38

 
Casa do Código Capítulo 3. Construindo minha primeira imagem 
 
A diferença em usar ENTRYPOINT é que ele chama o comando ou script 
diretamente, por exemplo: 
 
 
 
 
 
 
Quando utilizamos ENTRYPOINT, tudo o que for especificado em CMD 
será enviado como complemento para ENTRYPOINT: 
 
 
 
 
 
 
V eremos mais detalhes sobre inicialização de serviços em outro capítulo. 
 
3 . 7 Tratando logs 
O Docker possui um recurso para visualizar os logs de saída e de erro pa- 
drão ( s td o u t e stderr). Isso é interessante para verificarmos o que está 
acontecendo dentro de um container, sem a necessidade de conferir um de- 
terminado arquivo de log. 
Para este exemplo, vamos utilizar o Dockerfile da seção anterior e redire- 
cionar os logs do Nginx para s td o u t e stderr. O Dockerfile ficará assim: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
29 
  

## Página 39

 
3.7. Tratando logs Casa do Código 
 
 
 
 
 
 
 
 
Recrie a imagem com build e, em seguida, um container: 
 
 
 
Faça alguns r eq uests para gerar registros nos logs: 
 
 
 
 
 
 
Agora, podemos conferir os logs utilizando o comando do cker l o g s e 
a identificação do nosso container: 
 
 
 
 
 
 
 
 
 
 
 
 
 
Desta forma, conseguimos capturar os logs do serviço Nginx de dentro 
do container sem precisar abrir os arquivos de log, pois todo o log está sendo 
redirecionado de forma que a opção l o g s do Docker consiga acompanhar. 
 
 
 
 
 
30 
  

## Página 40

 
Casa do Código Capítulo 3. Construindo minha primeira imagem 
 
3 .8 Exportação e importação de containers 
Imagine que temos um container em execução e queremos exportá-lo para 
outro host. Outra situação parecida é um container funcionando localmente, 
porém queremos levá-lo para um host em produção. 
Podemos criar uma imagem partindo de um container que está funcio- 
nando, e gerar um arquivo .tar usando a opção s av e. Para criar a nova 
imagem, basta fazer um commit no container em execução: 
 
 
 
 
 
 
De posse da nova imagem que foi gerada, faremos a exportação criando 
um arquivo: 
 
 
Agora o arquivo .tar que foi criado pode ser enviado para o outro host, 
via SCP, por exemplo. Para fazer a importação desse arquivo, utilizamos a 
opção l oad: 
 
 
Este fluxo pode ser usado em operações para projetos privados. V eremos 
outras opções no capítulo 6. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
31 
  

## Página 41

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Página 42

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Capítulo 4 
Trabalhando com volumes 
 
 
Um volume pode ser um diretório localizado fora do sistema de arquivos de 
um container. O Docker permite especificar diretórios no container para que 
possam ser mapeados no sistema de arquivos do host. Com isso, temos a 
capacidade de manipular dados no container sem que tenham relação alguma 
com as informações da imagem. Um volume pode ser compartilhado entre 
vários containers. A figura a seguir ilustra como os volumes funcionam: 
 
 
 
 
 
 
 
 
 
 
 
  

## Página 43

 
4.1. Gerenciando os dados Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 4.1: O funcionamento de Docker V olumes 
 
 
4 . 1 Gerenciando os dados 
V olumes são diretórios configurados dentro de um container que fornecem 
o recurso de compartilhamento e persistência de dados. 
Antes de continuar, precisamos entender três coisas: 
 
• Os volumes podem ser compartilhados ou reutilizados entre contai- 
ners; 
• Toda alteração feita em um volume é de forma direta; 
• V olumes alterados não são incluídos quando atualizamos uma imagem. 
 
Ainda utilizando a imagem criada para o Nginx, podemos testar o uso de 
volumes com a opção -v. Com ela, é possível informar um diretório no host 
local que poderá ser acessado no container, funcionando de forma parecida 
com um mapeamento. Além disso, vamos informar o tipo de permissão que 
o container terá sob o diretório local, sendo: r o para somente leitura, e rw 
para leitura e escrita. 
Utilizando a opção -v, veja na prática como isso funciona: 
 
34 
  

## Página 44

 
Casa do Código Capítulo 4. Trabalhando com volumes 
 
 
 
 
 
O diretório /tmp/nginx pertence ao host local, e quero que ele seja ma- 
peado para / u s r / s h a r e / n g i n x / h t m l dentro do container que está sendo 
inicializado. Além disso, estou passando a instrução r o no final para infor- 
mar ao container que ele só poderá ler o conteúdo em /tmp/nginx. 
Para testar o volume criado, vamos gerar um arquivo em /tmp/nginx 
e inserir algum texto. Entretanto, antes note o retorno de um r eq ues t feito ao 
acessarmos o web server: 
 
 
 
 
 
Agora, criando o arquivo no host e testando novamente: 
 
 
 
 
 
4.2 Utilizando volumes no Dockerfile 
Imagine que temos um container com um banco de dados em execução. Nele, 
é possível controlar os dados que são armazenados em disco para fazer bac- 
kups e até restaurações. 
Para isso, devemos separar a construção deste novo Dockerfile. Antes de 
começar, crie uma pasta chamada mysql e um novo arquivo Dockerfile com 
as seguintes instruções de instalação: 
 
 
 
 
 
 
 
 
 
35 
  

## Página 45

 
4.2. Utilizando volumes no Dockerfile Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
Não se preocupe com os arquivos run e my. cn f; eles estão sendo adici- 
onados ao Dockerfile apenas para tornar a instalação e execução do MySQL 
mais simples. 
Bem, aqui temos duas novidades. A primeira é o uso da opção ENV para 
declarar uma variável ambiente, que neste caso será utilizada no processo de 
instalação do MySQL, a fim de evitar telas interativas que são exibidas durante 
a instalação para cadastrar usuários e configurar o banco de dados. 
E a segunda é que estamos informando que o diretório 
/var/lib/mysql será um VOLUME; assim, poderemos manipular os 
arquivos de dados salvos pelo MySQL. 
Agora, vamos gerar uma nova imagem chamada mysql, e inicializar um 
container: 
 
 
 
 
 
A variável MYSQL_ROOT_P ASSWORD existe no script de execução run, 
que foi copiado quando geramos a imagem. A opção - e serve para designar 
valores a variáveis ambiente – neste caso, o valor que ela recebe é a senha de 
r o o t para o acesso ao MySQL. 
Para testar se o container está funcionando perfeitamente, podemos aces- 
sar o MySQL partindo do host local: 
 
 
 
 
36 
  

## Página 46

 
Casa do Código Capítulo 4. Trabalhando com volumes 
 
 
 
 
 
 
 
 
 
 
 
 
 
Agora, com o container em execução e o teste feito, vamos focar no uso 
de volumes. 
Por padrão, os dados armazenados pelo MySQL residem em 
/var/lib/mysql , justamente onde inicializamos o nosso volume. 
Assim, é possível criarmos um novo container que terá acesso a esses dados. 
Para isso, podemos utilizar a opção --volumes-from, que recebe como 
argumento o ID ou nome do container a cujos dados queremos ter acesso. 
No exemplo a seguir, usaremos uma imagem mínima chamada busybox 
para ter acesso aos dados do container que está em execução com MySQL: 
 
 
 
 
 
 
 
 
 
 
 
 
O Docker inicializou o novo container utilizando a imagem busybox, e 
mapeou o volume do container mysql para a nova instância que foi criada. 
Isso pode ser visto ao acessarmos o diretório do mysql no novo container: 
 
 
 
 
37 
  

## Página 47

 
4.3. Backup e restore de volumes Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
Temos acesso aos dados que estão sendo gravados em disco pelo mysql. 
O mesmo poderia ser feito com arquivos de logs, por exemplo. Além disso, a 
opção --volumes-from pode ser usada para replicar esse volume em múl- 
tiplos containers. 
É interessante saber que se você remover o container que monta o volume 
inicial – ou seja, o do mysql –, os posteriores que foram inicializados com a 
opção --volumes-from não serão excluídos. 
Para remover o volume do disco, você pode utilizar a opção -v combi- 
nada com o rm, como do cker rm -v volume_name. 
 
4 .3 Backup e restore de volumes 
Outra forma de uso para --volumes-from pode ser para a constru- 
ção de backups. Imagine que você queira realizar um backup do diretório 
/var/lib/mysql do container para o seu host local: 
 
 
 
 
 
 
 
 
 
Por partes: primeiro estamos criando um novo container com acesso ao 
volume de dados do mysql e, em seguida, estamos criando um mapeamento 
entre o nosso host local e o novo container, de forma que tudo o que for criado 
 
38 
  

## Página 48

 
Casa do Código Capítulo 4. Trabalhando com volumes 
 
no diretório mapeado dentro deste novo container esteja disponível para o 
nosso host local. Observe a figura a seguir: 
 
 
 
 
 
 
 
 
 
 
Fig. 4.2: Realizando backup de volumes 
 
 
O container intermediário é criado usando a imagem base do Ubuntu 
e, por último, executamos a compactação e cópia dos dados. Resumindo: 
o novo container copia os dados da instância que está com o mysql ativo, 
compacta tudo e disponibiliza para o nosso host local. 
Para entender como o r est or e funciona, faremos um pequeno teste, cri- 
ando um banco no mysql: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
39 
  

## Página 49

 
4.3. Backup e restore de volumes Casa do Código 
 
Agora que temos uma estrutura de exemplo, se destruirmos o container 
que está executando o mysql sem salvar os dados persistidos no volume, per- 
deremos o exemplo criado. Antes de destruir esse container, vamos executar 
o backup novamente: 
 
 
 
V amos remover o container do mysql e criar um novo, para ver o que 
acontece com os dados no volume /var/lib/mysql: 
 
 
A opção -f serve para forçar a remoção do container que está em exe- 
cução. Isso funciona como um atalho para evitar a instrução s to p antes de 
remover. 
Com o container excluído, podemos gerar um novo, acessar o mysql e 
conferir se o exemplo criado ainda existe: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
O banco example não existe mais. Então, vamos restaurar o último bac- 
kup realizado e ver o que acontece. Para isso, faremos o caminho inverso, 
informando que o container criado utilizará o diretório mapeado em nosso 
host local para descompactar o arquivo b a c k u p . t a r, dentro do volume ma- 
peado no container do mysql: 
 
40 
  

## Página 50

 
Casa do Código Capítulo 4. Trabalhando com volumes 
 
 
 
 
Desta vez, usamos a imagem busybox apenas para diferenciar; o efeito 
é o mesmo. 
V oltando ao mysql, podemos verificar se o banco example existe: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Tudo funciona! Podemos utilizar estas opções para automatizar backups, 
migrações e restaurações com qualquer ferramenta de nossa preferência. 
 
 
 
 
 
 
 
 
 
 
 
41 
  

## Página 51

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Página 52

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Capítulo 5 
Configurações de rede 
 
 
Por padrão, sempre que o Docker é inicializado, uma interface de rede virtual 
chamada do cker0 é criada na máquina host. Então, de forma aleatória, o 
Docker escolhe um endereço privado de IP e uma máscara de sub-rede, e os 
configura na interface virtual docker0. 
Essa interface virtual nada mais é que uma ponte virtual que encaminha 
os pacotes de forma automática para quaisquer outras interfaces que estejam 
conectadas. Ou seja, os containers conseguem estabelecer comunicação com 
o host e entre si. 
 
5.1 Comunicação entre containers 
Para a comunicação entre containers funcionar, vai depender de dois fatores: 
 
 
 
 
 

## Página 53

 
5.1. Comunicaç ão entre containers Casa do Código 
 
• A topologia de rede do host deve permitir a conexão das interfaces de 
rede dos containers, usando a ponte docker0; 
• O iptables deve permitir as ligações especiais que serão feitas – nor- 
malmente, são regras de redirecionamento de pacotes. 
 
Na sua configuração padrão, o Docker utiliza apenas uma interface ponte 
para concentrar todas as comunicações. Além disso, ele providencia as re- 
gras de firewall no iptables para prover as rotas de tráfego. Isso pode ser 
conferido ao inicializarmos dois containers: 
 
 
 
 
 
 
 
Agora, na máquina host, podemos verificar as regras criadas pelo Docker 
no iptables: 
 
 
 
 
 
 
 
 
O retorno da verificação no iptables exibe o envio de pacotes do host 
local para os IPs de destino, em suas respectivas portas. Podemos, assim, 
realizar alguns testes de um container para outro, utilizando a opção exec. 
V eremos a seguir a comunicação entre os dois containers criados: 
 
 
 
 
 
 
 
 
 
44 
  

## Página 54

 
Casa do Código Capítulo 5. Configuraç ões de rede 
 
 
 
 
Ao usarmos a opção exec, foi solicitado para que o container n g i n x 
realizasse um ping no IP do container mysql, apenas para confirmar a co- 
municação estabelecida entre eles. V eremos na seção 5.3 o comportamento 
desta comunicação em uma aplicação real. 
 
5 . 2 Alterando a configuração default 
Como vimos, por padrão o Docker inicializa e configura a interface de rede 
virtual docker0. V eremos agora como alterar essas configurações no pro- 
cesso da sua inicialização. 
V amos especificar uma faixa IP e uma máscara de rede de nossa preferên- 
cia para serem usadas na interface docker0. Para isso, o parâmetro -- bi p = 
pode ser usado antes de inicializar o Docker. Outra opção é a de restringir um 
range de IPs privados utilizando --fixed-cidr=. 
V erificaremos a comunicação da interface virtual docker0 bridge 
(ponte) com as interfaces virtuais dos containers, utilizando o comando 
brctl show: 
 
 
 
 
 
 
Com o brctl, vemos que, cada vez que um novo container é criado, o 
Docker seleciona um IP disponível em bridge, configura o IP escolhido na 
interface et h 0 do container, e define todo o mapeamento. 
Todo esse comportamento pode ser alterado, até mesmo o nome da bridge 
pode ser escolhido. Para alterar, vamos utilizar a opção -b, ou -- br i dg e =. 
Para definir estas configurações, primeiro temos de parar o serviço do Docker 
e, em seguida, eliminar a interface docker0. V eja em código: 
 
 
 
 
45 
  

## Página 55

 
5.2. Alterando a configuraç ão default Casa do Código 
 
Note que, antes de remover a interface docker0 com o comando brctl, 
ela foi desligada. Agora, podemos criar a nossa própria b ridge: 
 
 
 
 
 
O resultado da nossa nova configuração deve ficar parecido com o se- 
guinte no nosso host: 
 
 
 
 
 
 
 
 
 
 
 
 
Agora, só precisamos informar ao Docker que ele deve usar a nova in- 
terface virtual criada antes de ser inicializado novamente. Para isso, vamos 
adicionar as opções que vimos no arquivo de configurações do Docker. Ge- 
ralmente, esse arquivo reside em /etc/default/docker: 
 
 
Com a nova configuração, agora vamos inicializar o Docker, criar alguns 
containers e verificar se estão utilizando os novos endereços IP que definimos: 
 
 
 
 
 
 
 
 
 
 
 
46 
  

## Página 56

 
Casa do Código Capítulo 5. Configuraç ões de rede 
 
E o novo IP atribuído ao container n g i n x faz uso da faixa que definimos 
manualmente apenas para verificar se está tudo funcionando. Teste a comu- 
nicação entre ele e o container mysql: 
 
 
 
 
 
 
O resultado da nossa configuração é que o Docker agora está preparado 
para operar com a nova bridge e delegar os IPs para os containers com a faixa 
que optamos. 
 
5 . 3 Comunicação de containers no mesmo host 
Vimos na primeira seção deste capítulo um pouco sobre a comunicação de 
containers. Agora veremos, de forma prática, como uma aplicação faz uso 
dessa comunicação. 
No exemplo, vamos criar dois containers: um para Nginx, que chama- 
remos de app, e outro para MySQL, que nomearemos como db apenas. O 
objetivo é estabelecer acesso entre os containers de forma que app possa exe- 
cutar instruções em db. 
Antes de tudo, precisamos criar os dois containers: 
 
 
 
 
 
Agora podemos acessar o shell do container app usando a opção exec 
e, em seguida, instalar o pacote mysql-client-5.5: 
 
 
 
Com o mysql-client-5.5 instalado no container app, agora pode- 
mos testar o acesso ao MySQL no container db: 
 
 
47 
  

## Página 57

 
5.3. Comunicaç ão de containers no mesmo host Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Lembre-se apenas de verificar os IPs atribuídos aos containers. 
 
Linkando containers 
Uma outra forma de estabelecer comunicação entre containers no mesmo 
host é utilizando a opção link. Essa opção providencia o mapeamento de 
rede entre os containers que estão sendo linkados. 
Refazendo o último exemplo, teríamos o mesmo resultado desta forma: 
 
 
 
 
Note que na opção link é informado o nome do container que queremos 
linkar e um apelido para ele – neste caso, mysql é o nome do container, e db 
o seu apelido. 
V erificaremos se o link está funcionando entrando no container app e 
testando a comunicação com o container mysql, através do apelido que cri- 
amos: 
 
 
 
48 
  

## Página 58

 
Casa do Código Capítulo 5. Configuraç ões de rede 
 
 
 
 
 
 
 
 
 
 
 
 
V eremos mais detalhes sobre o uso da opção link em outro capítulo, 
mais à frente. 
 
5 . 4 Comunicação de containers e m hosts dife- 
rentes 
Até agora, vimos como funciona a comunicação entre containers no mesmo 
host. Agora, imagine que temos vários containers funcionando e estes estão 
espalhados em diferentes hosts, e precisamos estabelecer a comunicação de 
rede entre eles. 
Supondo que temos dois hosts com IPs diferentes, em um dos hosts temos 
o container app e, no outro, o db. Precisamos configurar o Docker de forma 
que ele mantenha uma rota direta entre os containers. Para isso, criaremos 
uma rota entre as interfaces privadas dos hosts. A configuração será parecida 
com o seguinte esquema: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
49 
  

## Página 59

 
5.4. Comunicaç ão de containers em hosts diferentes Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 5.1: Comunicando containers de hosts diferentes 
 
 
Em cada uma das instâncias, vamos configurar uma faixa IP diferente 
para ser usada por bridge. Então, na instância de app, pode ser feito da se- 
guinte forma: 
 
 
 
 
 
 
Já na instância de db, vamos criar a bridge com outra faixa IP: 
 
 
 
 
 
 
Agora, precisaremos adicionar as rotas em cada uma das instâncias, de 
forma que exista conexão entre os IPs 1 9 2 . 1 6 8 . 1 3 . 1 e 1 9 2 . 1 6 8 . 1 4 . 1. 
A rota que será adicionada deve trafegar os pacotes usando a rede privada. 
No host app, vamos criar a rota desta forma: 
 
 
 
 
50 
  

## Página 60

 
Casa do Código Capítulo 5. Configuraç ões de rede 
 
Já no host de db, podemos adicionar a outra rota: 
 
 
 
Em um teste rápido, verificamos a comunicação funcionando entre os 
containers: 
 
 
 
 
 
 
5 . 5 Comunicação com automação 
Na seção anterior, foi possível notar que estabelecer a comunicação entre con- 
tainers existentes em hosts separados não é uma tarefa muito trivial. Todo 
esse trabalho pode ser minimizado utilizando o W e a v e, um serviço projetado 
para automatizar o processo de configuração de redes entre os hosts, e prover 
a comunicação entre containers. 
A instalação é simples e pode ser feita desta forma: 
 
 
 
 
 
Seguindo o exemplo da seção anterior, após instalar o W eave em ambos 
hosts, poderíamos inicializá-lo primeiro no host do container app ( h o s t1): 
 
 
 
 
O primeiro comando inicia o weave em um novo container e já baixa 
a do cker image, caso seja necessário. O segundo roda o nosso container 
app, usando o comando weave r un, que basicamente roda o do cker run 
-d, mas já passando os parâmetros de IP automaticamente. 
Em seguida, devemos fazer o mesmo no host do container db( ho s t2), 
informando a outra faixa IP: 
 
51 
  

## Página 61

 
5.5. Comunicaç ão com automaç ão Casa do Código 
 
 
 
 
 
 
O 1 7 2 . 3 1 . 1 0 . 1 1 é o IP de h o s t1 e, no lugar dele, também podería- 
mos ter colocado o hostname. Precisamos fazer isso para que o weave do 
h o s t2 saiba que precisa se comunicar com o weave do h o s t1. Note que 
isso poderia ser feito ao contrário também, iniciando primeiro o weave no 
h o s t2 e, depois, no ho s t1, passando o IP do h o st2. 
Para testar, vamos entrar no container app do h o s t1 e enviar um ping 
para o IP do container db que está rodando no ho s t2: 
 
 
 
 
 
 
 
 
É importante citar que os dois hosts ( h o s t1 e ho s t2) precisam ter a 
porta 6783 acessível para TCP e UDP, para que o weave funcione. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
52 
  

## Página 62

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Capítulo 6 
Docker Hub 
 
 
Até agora, vimos como usar a linha de comando para executar o Docker no 
host local e remoto. Aprendemos a utilizar imagens prontas e como criar 
imagens próprias. 
O Docker Hub (http://hub.docker.com) é um registro público que contém 
milhares de imagens para baixar e usar na construção de containers. Ele conta 
com autenticação, organização de grupos de trabalho e ferramentas para me- 
lhorar o fluxo de trabalho, além de repositórios privados para armazenar ima- 
gens que você não deseja compartilhar publicamente. 
 
6 . 1 Buscando e puxando imagens 
Por padrão, o Docker vem configurado com acesso somente leitura ao Docker 
Hub, e podemos pesquisar na linha de comando por imagens nele ao usarmos 
a opção s e a r c h: 
 
 
 

## Página 63

 
6.2. Enviando imagens para um repositório Casa do Código 
 
 
 
 
 
 
 
 
Uma vez que encontramos a imagem que estávamos a procura, vamos 
baixá-la com o comando pull: 
 
 
 
 
 
 
 
 
 
 
 
Perceba que, anteriormente, quando usamos a imagem do Ubuntu no 
nosso primeiro exemplo do livro, o que o Docker fez por baixo dos panos 
para nós foi: verificar que não tínhamos a imagem localmente, procurar por 
uma imagem no Docker Hub que possuía o nome ubuntu, baixá-la (fazendo 
pull) automaticamente, e aí sim criar o nosso container. 
 
6.2 Enviando imagens para u m repositório 
Para que possamos enviar nossas imagens para o Docker Hub, precisamos 
criar uma nova conta (caso você ainda não possua), ou fazer login em uma já 
existente: 
 
 
 
 
 
 
Com o login feito, vamos enviar nossas imagens geradas para Docker Hub 
e fazer uso delas nos projetos em produção. 
 
54 
  

## Página 64

 
Casa do Código Capítulo 6. Docker Hub 
 
Para enviar um repositório para o Docker Hub, usamos a opção push. O 
formato deve obedecer a seguinte regra: username/image. Esse formato é 
elaborado durante o processo de build da imagem, utilizando a opção -t: 
 
 
Observe a identificação da imagem usando o nome do usuário. A 
opção :v1 no final é uma tag – no exemplo, a nova imagem gerada 
infoslack/mysql está marcada como v1: 
 
 
 
 
 
 
Também podemos adicionar e alterar tags em imagens já criadas. Para 
isso, basta usar a opção ta g e o ID da imagem: 
 
 
 
 
 
 
 
 
Por fim, vamos enviar a imagem ao repositório do Docker Hub com a 
opção push: 
 
 
 
 
 
 
 
Agora, temos disponível a imagem infoslack/mysql publicamente, 
que pode ser usada em qualquer Dockerfile. 
 
 
 
 
55 
  

## Página 65

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Página 66

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Capítulo 7 
Trabalhando com Docker 
 
 
No processo de desenvolvimento de software, a agilidade e a automação fa- 
zem parte do cotidiano, e com Docker não é diferente. Até aqui, vimos vários 
comandos para utilizar a ferramenta. Agora veremos na prática como auto- 
matizar boa parte das funcionalidades que aprendemos. 
Em nossos exemplos, usaremos uma aplicação Ruby on Rails. No pri- 
meiro momento, o foco será configurar o ambiente de desenvolvimento. 
Para automatizar a criação e a gestão de containers, vamos utilizar o 
Docker Compose, que é uma ferramenta elaborada para reduzir a complexi- 
dade de configuração e isolamento de ambientes de execução para aplicações 
com Docker. 
 
 
 
 
 
 
  

## Página 67

 
7.1. Preparando o ambiente Casa do Código 
 
7.1 Preparando o ambiente 
Antes de começar, precisamos instalar o Compose. A instalação é muito sim- 
ples e pode ser feita com apenas um comando: 
 
 
Podemos prosseguir com a configuração do nosso environment de de- 
senvolvimento. 
O uso do compose consiste em 3 passos: 
 
• Definição do Dockerfile da aplicação; 
• Definição dos serviços em um arquivo de configuração; 
• Execução do compose para iniciar os serviços. 
 
Neste exemplo, precisamos definir no Dockerfile a imagem base que será 
usada. Neste caso, utilizaremos uma imagem oficial do Ruby . Além disso, é 
necessário resolver algumas dependências para o projeto Rails, como a ins- 
talação de alguns pacotes: build-essential, postgresql-client e 
n o d ej s. 
Algumas tarefas não devem ser executadas sempre que a imagem for 
recriada, como por exemplo, o bundle install. Para evitar isso, fa- 
remos uso de uma estratégia de cache, copiando os arquivos Ge mf i l e e 
Gemfile.lock para o diretório /tmp e, em seguida, executando o bundle 
install. Não se preocupe com isso, pois veremos formas melhores de re- 
solver esse problema mais adiante. 
Também é preciso dizer que queremos os arquivos do projeto dentro do 
container, quando ele for criado e, por fim, definimos o comando para dar 
start em nosso projeto. O nosso Dockerfile de exemplo ficará assim: 
 
 
 
 
 
 
 
 
58 
  

## Página 68

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Ainda no diretório da aplicação, precisamos criar um arquivo de confi- 
guração indicando os serviços que deverão ser inicializados pelo compose. 
Então, teremos um arquivo chamado docker-compose.yml: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Finalmente, podemos executar o comando docker-compose up e ver 
a aplicação funcionando: 
 
 
 
 
59 
  

## Página 69

 
7.1. Preparando o ambiente Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Para testar rapidamente, utilizaremos o curl ou o browser, e acessar o 
endereço http://localhost:8080: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
60 
  

## Página 70

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
7.2 Entendendo como funciona 
V amos entender agora o que aconteceu e como os containers de app e db 
estabeleceram comunicação. 
Olhando para o arquivo de configuração docker-compose.yml, na 
primeira instrução temos um bloco chamado db que faz referência ao serviço 
que será iniciado – neste caso, o PostgreSQL. 
Observe os detalhes da configuração. Em image, estou informando o 
nome da imagem que será usada e, caso ela não exista no host local, um pull 
será feito no Docker Registry, que vimos no capítulo anterior. 
Em seguida, na declaração volumes, é informado o path local que será 
mapeado com um diretório do container e, por fim, temos a opção expose, 
onde a porta 5432 está sendo liberada de forma privada, somente para co- 
municação entre containers. 
Já em app, é iniciado com a opção build, onde é informado que a ima- 
gem que será usada por este serviço vem de um Dockerfile local. A instrução 
para iniciar o web server padrão do Rails na porta 3000 ficou definido no 
próprio Dockerfile do projeto, na opção CMD. 
Como tudo está sendo mantido dentro do diretório do projeto Rails, a 
configuração de volumes é declarada partindo do local corrente e mape- 
ada para um diretório dentro do container, de forma que toda alteração nos 
arquivos do projeto seja refletida no container, em tempo de execução. 
Note que em app não estamos usando a opção expose, em vez disso 
usamos ports, pois queremos mapear a porta 3000 do container para 8080 
no host local; assim, acessaremos a aplicação. 
A última opção links é bastante interessante, pois, como já vimos no 
capítulo 5, ela efetiva a comunicação entre os containers – neste caso, entre 
db e app –, sem a necessidade de trabalharmos com configurações de rede. 
 
7.3 Executando e m produção 
Imagine que finalizamos o desenvolvimento de uma nova aplicação e agora 
queremos enviá-la para o ambiente de produção. Seguindo a mesma linha de 
raciocínio da seção anterior, o Dockerfile será algo como: 
 
61 
 

## Página 71

 
7.3. Executando em produç ão Casa do Código 
 
 
 
Nesta etapa, estamos utilizando a imagem oficial do Ruby – neste caso, 
com regras que funcionam como gatilhos chamados de ONBUILD. Anali- 
sando as instruções que criaram a imagem que estamos chamando no Doc- 
kerfile, podemos ver o seguinte: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
As instruções que apresentam ONBUILD não serão executadas quando a 
imagem for gerada, todas serão adiadas. Esses gatilhos serão disparados ape- 
nas quando essa imagem for herdada em outro Dockerfile. Esta abordagem é 
ideal para a criação de imagens s t a n d - a l o n e para um projeto. 
Pensando ainda no ambiente de produção, não precisamos alterar a re- 
ceita existente em docker-compose.yml, pois o docker-compose per- 
mite a definição de um arquivo separado com as configurações apropriadas 
para o ambiente de produção, neste caso, p ro d u c t i o n .y m l. 
Antes de continuar, vamos sobrescrever o nosso Dockerfile para ins- 
talar duas coisas necessárias para funcionamento da nossa aplicação: o 
NodeJS como engin e JavaScript para o Rails, e o client de conexão para o 
p o s t g r e s q l: 
 
 
 
Como não queremos que a nossa aplicação funcione sob a porta 3000, 
vamos adicionar o servidor web n g i n x para trabalharmos com a porta pa- 
drão 80. A configuração de produção será como a seguir: 
 
62 
  

## Página 72

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Agora, temos mais um serviço sendo criado, chamado de web, que es- 
tabelece comunicação com o container de app e aplica o mapeamento de 
portas entre o host utilizando a porta padrão 80. 
Note a opção command; ela será responsável por executar o servidor de 
aplicações Rails Puma na porta 9000. Na opção environment, estamos 
indicando que a aplicação deve funcionar em modo de produção. 
Para que tudo funcione, é necessário configurar o n g i n x de modo que 
ele tenha conectividade com o servidor de aplicações Rails. Ou seja, devemos 
inserir o bloco upstream nas configurações do n g i n x, informando o host 
e a porta que será utilizada na aplicação Rails: 
 
63 
  

## Página 73

 
7.3. Executando em produç ão Casa do Código 
 
 
 
 
 
 
Felizmente, isso já foi aplicado na construção da imagem e está disponível 
no Docker Hub. 
É importante notar a diretiva volumes_from no container web, pois, 
sem ela, o n g i n x não saberá o path para a aplicação Rails e, portanto, não 
funcionará. 
Com o arquivo de configuração alternativo ( p ro d u c t io n . y m l), pode- 
mos definir uma variável ambiente chamada COMPOSE_FILE. Isso faz com 
que o compose use o arquivo que definimos como padrão: 
 
 
 
Ou podemos utilizar o parâmetro -f para especificar o arquivo durante 
a execução: 
 
 
Agora, vamos pensar em estratégias de deploy para nossa aplicação. No 
momento, a forma mais simples seria clonar o projeto direto no servidor de 
produção e criar os containers com docker-compose: 
 
 
 
 
 
 
 
O resultado deste projeto no browser será algo como: 
 
 
 
 
 
 
 
 
64 
  

## Página 74

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.1: Demo Rails com Docker em produção 
 
 
7 . 4 Um pouco de integração contínua 
Agora que concluímos os ajustes para produção e providenciamos o deploy, 
veremos algumas formas de melhorar e automatizar o processo. Para isso, fa- 
remos uso da integração contínua e elaborar uma forma melhor de implantar 
nossos containers. 
Neste exemplo, faremos uso do CircleCI (https://circleci.com/) , um ser- 
viço de integração contínua e deploy, bastante rápido e simples de se usar e 
que fornece um ótimo suporte para usuários Docker. 
Inicialmente, vamos refazer o deploy da seção anterior, desta vez de forma 
automática. A primeira coisa a ser feita é criar um arquivo de configuração 
na raiz do projeto para o CircleCI, chamado circle.yml: 
 
 
 
 
 
65 
  

## Página 75

 
7.4. Um pouco de integraç ão contínua Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
Em machine, definimos que o serviço utilizado no CI é para Docker. Em 
seguida, na opção dependencies, informamos que desejamos construir 
uma imagem, partindo do Dockerfile existente no projeto. Por fim, na opção 
deployment, executamos um script para o deploy. 
O script d e p l o y. s h contém as seguintes informações: 
 
 
 
 
 
 
 
 
Ao rodar o script, o CI entra no servidor de produção via SSH, executa 
uma sequência de comandos, realiza o clone do projeto, entra em seu diretó- 
rio e cria os containers utilizando docker-compose. 
Para que tudo funcione, é necessário configurar o CircleCI de forma que 
ele possa acessar o servidor via SSH. Essa configuração pode ser feita com 
troca de chaves entre o servidor e o CI: 
 
 
 
 
 
 
 
 
 
 
66 
  

## Página 76

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.2: Configurando o CircleCI para acesso SSH 
 
 
Clicando nas configurações do projeto ( Project Settings) e em per- 
missões de SSH ( SSH Pe r m i s s i o n s), podemos adicionar a chave privada 
para o CI; a chave pública deve ser inserida no servidor. Desta forma, sempre 
que o projeto for atualizado no GitHub, o CI entra em ação executando as 
tarefas, e realiza o deploy para produção. 
Agora, note que estamos pedindo ao CI para gerar uma imagem, partindo 
do nosso Dockerfile na task dependencies em circle.yml, mas não 
estamos usando para nada. V amos melhorar isso com o docker-compose, 
aplicar um teste no CI para criar os containers com base na imagem gerada e 
verificar se tudo está funcionando, antes de realizar o deploy. 
O arquivo circle.yml ficará assim: 
 
 
 
 
 
 
 
 
 
67 
  

## Página 77

 
7.5. Limitando o uso de recursos Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Em dependencies, mudamos para que o CI instale o 
docker-compose e adicionamos a task test que cria somente o 
container de app via compose. Assim, não precisamos criar todos os 
containers, pois o CI providencia o Po s t g r e s q l automaticamente. 
Em seguida, temos uma instrução curl que verifica rapidamente se a 
aplicação está respondendo, e finalmente realiza o deploy. 
V eremos mais adiante outra forma de trabalhar com o CircleCI. 
 
7.5 Limitando o uso de recursos 
Até agora, todos os containers que criamos estão utilizando o total de recursos 
do host: CPU, RAM, I/O etc. Este é o padrão do Docker; entretanto, podemos 
controlar o consumo ao definirmos limites aos containers. 
Imagine que temo um container com o web server n g i n x em ação: 
 
 
V amos acompanhar o consumo de recursos desse container usando a op- 
ção stats. O resultado seria algo como: 
 
 
 
 
 
 
 
 
68 
  

## Página 78

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
Por padrão, o container criado é preparado para fazer uso de toda a me- 
mória RAM disponível no host; o mesmo ocorre com a CPU. Podemos recriar 
o container n g i n x, mas, desta vez, limitando o uso de CPU e RAM com as 
opções -c e -m e, em seguida, verificar com stats: 
 
 
 
 
 
 
 
Perceba que, ao utilizarmos os limites para memória -m 1024m, o con- 
tainer agora está limitado a um total de 1Gb de RAM em vez do total do exis- 
tente no host. A opção -c 512 indica que estamos limitando o uso de CPU 
neste container a 50% da capacidade total contida no host. Por padrão, o Doc- 
ker usa 1024 nesta diretiva, que representa 100%. 
Fazendo uma pequena análise nos cgroups, é possível verificar que a 
opção -c 512 realmente está configurando o container para utilizar apenas 
50% do total de CPU existente no host. Porém, primeiro vamos listar o total: 
 
 
 
 
 
 
 
 
 
O comando lscpu retorna as informações da CPU. Neste exemplo, o 
meu host possui 4 núcleos, que vão de 0 a 3. Agora, verificando os cgroups, 
notamos a utilização de apenas 50% do total pelo container: 
 
 
 
A diretiva responsável por controlar o uso de CPU neste container é 
c p u s e t . c p u s, e o seu limite está setado para usar os núcleos 0 e 1. Ou seja, 
apenas 50%. 
 
69 
  

## Página 79

 
7.6. Orquestrando containers Casa do Código 
 
Não se preocupe sobre limitar os recursos. V eremos na sequência que isso 
pode ser automatizado. 
 
7 . 6 Orquestrando containers 
Chegou o momento de automatizar a construção e a manutenção de contai- 
ners. Para isso, vamos conhecer uma excelente opção: o projeto Rancher. 
O Rancher é uma plataforma de gestão de containers para a execução de 
Docker em grande escala. Ele é ideal para trabalhar com Docker em produ- 
ção. 
O projeto foi construído para reduzir a complexidade de manter projetos 
e infraestrutura em execução, em qualquer lugar, com o uso de APIs e ferra- 
mentas nativas do Docker. V eremos mais detalhes sobre a API do Docker no 
próximo capítulo. 
A instalação é bem simples. Tudo o que precisamos fazer é criar um con- 
tainer que utilize a imagem base do projeto r a n c h e r: 
 
 
 
 
 
 
 
 
 
A porta 8080 é definida para termos acesso à interface web que usaremos 
para orquestrar os containers. Após concluir a etapa de instalação, vamos 
acessar a interface do Rancher – neste exemplo, ficou http://localhost:8080: 
 
 
 
 
 
 
 
 
 
 
70 
  

## Página 80

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.3: Rancher UI 
 
 
Para começar, é preciso adicionar um host. Para obtermos o melhor po- 
tencial desta ferramenta, vamos escolher a opção Amazon EC2 e informar 
os detalhes, para que o Rancher possa fazer isso de forma automática: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.4: Preenchendo os dados 
 
 
As informações mais importantes são o ACCESS KEY e o SECRET KEY, 
 
71 
  

## Página 81

 
7.6. Orquestrando containers Casa do Código 
 
chaves de API da Amazon, pois é por meio delas que o Rancher realizará 
a autenticação para criar o nosso host. Esses dados podem ser obtidos no 
console da Amazon: 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.5: A WS API Keys 
 
 
Depois de preencher os campos, podemos solicitar ao Rancher que crie o 
host. Esta etapa pode demorar alguns minutos. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.6: Rancher criando um novo host 
 
 
Finalmente, o host foi criado com sucesso. Note as informações sobre a 
instância que foi criada na Amazon: 
 
72 
  

## Página 82

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.7: Host criado com sucesso! 
 
 
Com o host configurado, vamos criar alguns containers e ver as facilida- 
des fornecidas pelo Rancher. Neste exemplo, usaremos imagens oficiais do 
Docker Hub, uma do MySQL e outra do WordPress. 
Primeiro criaremos um container para o MySQL, onde é necessário in- 
formar apenas 2 opções, a imagem oficial e a variável de ambiente que define 
a senha de r o o t para acesso: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
73 
  

## Página 83

 
7.6. Orquestrando containers Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.8: Criando container MySQL 
 
 
Em seguida, criamos um container para o WordPress, fazendo uso tam- 
bém de sua imagem oficial. Para este container, precisamos mapear a porta 
80 para o host e definir a variável ambiente para ter acesso ao banco. Nas 
opções de rede, criamos um link entre os containers do WordPress e MySQL. 
Confira as figuras a seguir: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
74 
  

## Página 84

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.9: Criando container WordPress 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.10: Linkando os containers WordPress e MySQL 
 
 
Com os containers criados, vamos verificar se tudo está funcionando. Ao 
acessarmos o IP do host, devemos ter como resposta a página de instalação 
do WordPress: 
 
 
 
 
75 
  

## Página 85

 
7.6. Orquestrando containers Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.11: WordPress instalação 
 
 
Explorando um pouco mais o Rancher, é possível ter acesso a um web 
shell nos containers. Isso pode ajudar em operações de debug, por exemplo. 
Clicando na lista de opções de um container, podemos ter acesso ao shell: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
76 
  

## Página 86

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.12: Lista de opções de um container 
 
 
Clicando na opção, temos o seguinte resultado: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7.13: Web shell de um container 
 
 
77 
  

## Página 87

 
7.6. Orquestrando containers Casa do Código 
 
É possível também limitar o uso de recursos como CPU e memória por 
cada container de forma prática: 
 
 
 
 
 
 
Fig. 7.14: Limitando CPU/RAM em um container 
 
 
Além disso, vamos monitorar o uso desses recursos em cada host adicio- 
nado e container criado: 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 7. 15 : Monitorando o consumo de recursos 
 
 
Como vimos ao criar um container, o Rancher busca as imagens direto 
no Docker Hub. Em um projeto real, teríamos uma conta privada no Docker 
Hub integrada a um CI para gerar a imagem do projeto, que, por sua vez, 
poderia ser chamada no Rancher. Neste caso, o nosso circle.yml seria 
alterado para: 
 
 
 
 
 
78 
  

## Página 88

 
Casa do Código Capítulo 7. Trabalhando com Docker 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Em vez de enviar direto para produção como fizemos anteriormente, a 
task deployment está fazendo o deploy no Docker Hub. A novidade aqui 
são as opções de login e push, que recebem variáveis ambiente que foram 
configuradas no CI. 
Com esta abordagem, teríamos a imagem i n f o s l a c k / d o c ke r - b o o k 
disponível no Docker Hub, pronta para ser usada. 
O Rancher é uma das várias opções que pode ser usada para orquestrar 
containers. V ale a pena explorar todo o potencial da ferramenta. 
No próximo capítulo, veremos mais detalhes sobre como a API do Docker 
funciona e é utilizada por ferramentas, como a que acabamos de ver. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
79 
  

## Página 89

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Página 90

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Capítulo 8 
Explorando um pouco mais 
 
 
Este capítulo destina-se a apresentar recursos mais avançados para você conti- 
nuar explorando o Docker. V eremos um pouco sobre API, TDD (T est-Driven 
Dev elopment) e formas de uso não convencionais, como isolamento de pro- 
gramas desktop em containers. 
 
8 . 1 Docker Remote API 
No final do capítulo anterior, vimos como orquestrar containers utilizando 
a plataforma Rancher, que faz uso da API padrão do Docker em seu back- 
ground. Agora, vamos explorar essa API e entender um pouco sobre como 
ela funciona. 
A API REST que o Docker possui nos permite executar comandos remo- 
tamente, ou seja, podemos gerar imagens, criar containers e estabelecer total 
controle de forma remota. Para isso, é preciso alterar a configuração padrão 
 
 
 

## Página 91

 
8.1. Docker Remote API Casa do Código 
 
do Docker em /etc/default/docker e adicionar os parâmetros de uso 
da API, a variável DOCKER_OPTS: 
 
 
 
 
 
 
Por padrão, o Docker funciona via unix so c k et. O que fizemos foi adicio- 
nar na configuração a opção para que ele responda via HTTP , em sua porta 
padrão TC P/I P 2375. 
Utilizando o curl, podemos testar e verificar como a API funciona, e 
listar as imagens da seguinte forma: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
82 
  

## Página 92

 
Casa do Código Capítulo 8. Explorando um pouco mais 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Ou simplesmente verificar a versão do Docker: 
 
 
 
 
 
 
 
 
 
 
 
 
 
Manipulando containers 
A API do Docker suporta todas as opções que usamos no terminal de co- 
mandos para criar e controlar containers. Utilizando o método POST HTTP , 
vamos inicializar um container desta forma: 
 
 
 
 
 
 
 
 
 
 
83 
  

## Página 93

 
8.1. Docker Remote API Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Como resposta, a API retornou o Id 3e9879113012, indicando que 
o container foi criado com sucesso. Com o Id do container criado, pode- 
mos inicializá-lo de forma bem simples, ao enviarmos a opção start como 
parâmetro na URL: 
 
 
 
Agora, vamos conferir se o container foi inicializado, listando todos que 
estão em execução: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
84 
  

## Página 94

 
Casa do Código Capítulo 8. Explorando um pouco mais 
 
Da mesma forma como usamos o método start, podemos enviar o 
s to p para finalizar as atividades do container, e a opção DELETE para re- 
mover o container: 
 
 
 
 
DockerUI 
Caso você queira se aprofundar um pouco mais nos estudos sobre a API 
do Docker, é interessante explorar o projeto DockerUI, uma interface web de 
manipulação da API. O projeto é aberto e está disponível em https://github. 
com/crosbymichael/dockerui. 
A instalação é simples e lembra um pouco o Rancher. V eja como funci- 
ona: 
 
 
 
Um container foi criado, e a porta 9000 foi mapeada para o host local. 
Agora, basta acessar a interface web em http://localhost:9000 e explorar. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
85 
  

## Página 95

 
8.2. TDD para Docker Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 8.1: DockerUI web interface para API 
 
 
8.2 TDD para Docker 
TDD (T est-Driven Dev elopm ent) é uma boa prática em desenvolvimento de 
software, pois garante a qualidade do software que está sendo desenvolvido. 
Isso porque todas as funcionalidades têm testes para garantir que o que foi 
desenvolvido está funcionando conforme esperado, e também aumenta a se- 
gurança para modificações posteriores no software. 
Quando seu software tem testes, você pode adicionar novas funcionali- 
dades e, por meio dos testes, garantir que ele continue com o comportamento 
esperado em todas as situações previstas e cobertas pelos testes. Calma, este 
ainda é um livro sobre Docker! 
Agora, imagine poder aplicar a mesma prática de TDD nos seus Docker- 
files para testar o comportamento dos containers. Isto é possível utilizando 
uma ferramenta chamada Serverspec, que permite a escrita de testes R Sp ec 
(Ruby) para verificar a configuração de servidores. A verificação normal- 
mente é feita via SSH – no caso do Docker, tudo é realizado via API. 
 
86 
  

## Página 96

 
Casa do Código Capítulo 8. Explorando um pouco mais 
 
Se você não está familiarizado com a ferramenta RSpec ou com a prá- 
tica de TDD, recomendo a leitura do livro T est-Driven Development: t e st e e 
d e si g n n o mundo real c o m Ruby, disponível na Casa do Código (http://www. 
casadocodigo.com.br/products/livro-tdd-ruby) . 
Antes de começarmos, é necessário ter o Ruby instalado e as gems r s p e c 
e s e r v e r s p e c: 
 
 
 
Com as dependências resolvidas, vamos ao exemplo prático de TDD para 
Docker. Primeiro, vamos escrever um teste e vê-lo falhar. Crie um arquivo 
chamado Dockerfile_spec.rb com o código a seguir: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
O nosso primeiro teste está verificando antes de tudo se a imagem existe. 
Durante sua execução, ele cria um container que captura a saída do programa 
lsb_release -a, que no nosso exemplo serve para verificar a versão insta- 
 
87 
  

## Página 97

 
8.2. TDD para Docker Casa do Código 
 
lada do Ubuntu. Caso a versão seja igual a descrita no teste – ou seja, Ubuntu 
14 –, o teste passará. 
Agora, vamos executar o teste e vê-lo falhar: 
 
 
 
 
 
 
 
 
 
 
 
 
 
A mensagem acusa que não encontrou um Dockerfile para gerar a ima- 
gem, criar um container e testar a versão. Para fazer o teste passar, precisamos 
criar o Dockerfile com a versão da imagem base do Ubuntu: 
 
 
Agora rodamos o teste novamente para vê-lo funcionar: 
 
 
 
 
 
 
 
Esse foi um teste muito simples apenas para explicar o fluxo. V amos es- 
crever um novo teste, mas desta vez para verificar se um pacote foi instalado 
e estará presente quando um container for criado: 
 
 
 
 
 
 
 
 
88 
  

## Página 98

 
Casa do Código Capítulo 8. Explorando um pouco mais 
 
 
 
 
 
O novo teste verifica se o pacote do n g i n x está presente no container. 
Ao executá-lo, veremos que ele falha novamente: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
O teste falha pois não temos o Nginx instalado. Para resolver o problema, 
basta alterar o Dockerfile para que instale o nosso pacote: 
 
 
 
 
Com isso, veremos o teste passar novamente: 
 
 
 
 
 
 
 
O Serverspec facilita bastante a escrita dos testes, você pode testar muito 
mais coisas além dos exemplos mostrados aqui, como: verificar o mapea- 
mento de portas, a conectividade entre containers e realizar testes específicos 
 
89 
  

## Página 99

 
8.3. Docker no desktop Casa do Código 
 
para uma aplicação. Dedique um tempo para explorar com mais detalhes essa 
ferramenta. 
 
8 .3 Docker no desktop 
Além do uso convencional, o Docker pode ser usado para isolar aplicações 
desktop em containers. Não estou falando só de aplicações modo texto, estou 
falando de aplicações GUI. 
Imagine limitar a quantidade de CPU e RAM para o Google Chrome, e 
continuar usando ele normalmente. 
Para que isso funcione, tudo o que precisamos fazer é mapear o volume 
do container, para que use o so c k et gráfico X11 do Linux. V eja o exemplo: 
 
 
 
 
 
 
 
 
 
 
A resposta ao criar o container para o Google Chrome será a sua janela 
de abertura. Note a configuração mapeando o volume para utilizar o so c k et 
/ t m p / . X 1 1 - u n i x. 
Além disso, a variável ambiente DISPLAY é definida para o container 
com o mesmo valor que é usado no host local. Confira o resultado: 
 
 
 
 
 
 
 
 
 
 
 
 
90 
  

## Página 100

 
Casa do Código Capítulo 8. Explorando um pouco mais 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 8.2: Google Chrome com Docker 
 
 
Além disso, observe as configurações para limitar o uso do processador 
e o consumo de memória - - c p u s e t 0 e -m 512mb. Com essas opções, 
estou limitando o uso de apenas 1 núcleo de CPU e disponibilizando um total 
de 512mb para o container. Podemos acompanhar o consumo com do cker 
stats: 
 
 
 
 
 
Existe ainda outros complementos para esse container, como por exem- 
plo, o uso da placa de áudio do host. Da mesma forma como mapeamos o 
so c k et para o servidor X criando um volume, podemos fazer com o disposi- 
tivo de áudio. Basta adicionar mais um volume na nossa receita: 
 
 
 
 
 
 
 
 
 
 
91 
  

## Página 101

 
8.3. Docker no desktop Casa do Código 
 
 
 
 
Com o volume -v / d e v / s n d : / d e v / s n d --privileged, estamos 
criando um compartilhamento de vários devices do host com o container, isso 
inclui a placa de áudio, a w e b c a m e o microfone. 
Imagine as possibilidades de uso para outros aplicativos, como Skype, 
Spotify e até mesmo o Steam. Além do controle fornecido para limitar o con- 
sumo de recursos, você tem a flexibilidade de adicionar, remover e manter 
aplicações em várias versões diferentes, sem a preocupação de poluir o sis- 
tema operacional base, pois está tudo em containers. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
92 
  

## Página 102

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Capítulo 9 
Um pouco sobre CoreOS Linux 
 
 
CoreOS é uma distribuição Linux totalmente repensada para fornecer os re- 
cursos necessários a uma infraestrutura moderna, de fácil gerenciamento e 
altamente escalável. Calma, este ainda é um livro sobre Docker. 
Neste capítulo, veremos um pouco sobre esse sistema projetado para tra- 
balhar com containers. 
 
9 . 1 Principais diferenças 
Ao contrário de distribuição Linux, como Ubuntu ou Debian, o CoreOS não 
possui um gerenciador de pacotes. Portanto, todo e qualquer software que for 
instalado será um container Docker por padrão. 
Outra grande diferença entre o CoreOS e a maioria das distribuições é 
que o sistema é mantido como um todo, ou seja, não teremos atualizações 
independentes de partes do sistema. Por possuir uma dupla partição raiz, 
 
 
 

## Página 103

 
9.2. ETCD Casa do Código 
 
significa que uma atualização pode ser instalada em uma partição diferente 
da que está em uso. 
Por exemplo, o sistema é inicializado na partição A; o CoreOS verifica 
se existe atualizações disponíveis e, então, faz o download da atualização e a 
instala na partição B: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 9.1: CoreOS update inteligente 
 
 
Desta forma, o sistema garante que se houver algum problema na atuali- 
zação, tudo poderá ser desfeito. Além disso, as taxas de limites d e r e d e e I/O 
não provocam sobrecarga em aplicações que estejam funcionando, pois esse 
procedimento é isolado com cgroups. 
No final do update, a máquina deve ser reiniciada para que o sistema uti- 
lize a partição B. Caso ocorra algum problema, o CoreOS vai realizar uma 
tarefa de rollback, voltando a fazer uso da partição A novamente. 
 
9.2 ETCD 
Um dos principais requisitos para o funcionamento de um cluster é a ca- 
pacidade de estabelecer comunicação entre os nós. O CoreOS faz isso muito 
bem através do ETCD, um esquema global de chave-valor, responsável pela 
gestão de descoberta de serviços. 
A configuração do ETCD no CoreOS é feita por meio de um arquivo 
 
94 
  

## Página 104

 
Casa do Código Capítulo 9. Um pouco sobre CoreOS Linux 
 
chamado c l o u d - c o n f i g. Nele, é possível personalizar as configurações de 
rede, scripts para S yst e m d e demais opções de nível de sistema operacional. 
O arquivo c l o u d - c o n f i g é salvo utilizando o formato Y AML e sempre é 
processado durante a inicialização da máquina. Além disso, é responsável por 
armazenar as configurações que permitem ao ETCD ter o controle de entrada 
de novas máquinas ao cluster. Um exemplo do arquivo de configuração 
c l o u d - c o n f i g seria assim: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Cada host possui o seu ETCD configurado para manter comunicação com 
os demais hosts que integram o cluster: 
 
 
 
 
 
 
 
 
 
 
 
 
95 
  

## Página 105

 
9.3. Fleet Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 9.2: Cluster CoreOS, ETCD em ação 
 
 
Todas as operações realizadas por ETCD, para compartilhar os dados de 
configuração entre os nós do cluster, são baseadas em uma API/REST. Outro 
fato interessante é a forma como os containers Docker são tratados, pois um 
container pode ser replicado em diferentes partes do cluster. 
 
9.3 Fleet 
Para o controle de clusters, o sistema conta com uma ferramenta chamada 
Fleet, que funciona como um gestor de processos para facilitar a configuração 
de aplicações no cluster, partindo de um único nó. 
Em um cluster, cada nó possui o seu próprio sistema de inicialização e 
gestão de serviços locais, conhecido por sys t em d. O Fleet nos fornece uma 
interface controladora para cada systemd presente nos nós do cluster. Isso 
torna possível a inicialização (ou a parada) de serviços e coleta de informações 
de processos em execução, em todo o cluster. 
Uma outra responsabilidade importante delegada ao Fleet é o controle do 
mecanismo de distribuição de processos, pois ele escolhe os nós de menor 
carga para inicializar os serviços. Isso garante a distribuição das tarefas no 
cluster de forma equilibrada: 
 
96 
  

## Página 106

 
Casa do Código Capítulo 9. Um pouco sobre CoreOS Linux 
 
 
 
 
 
 
 
 
 
 
Fig. 9.3: CoreOS, controle do cluster com Fleet 
 
 
9.4 Criando u m clu ster 
Neste exemplo, veremos como criar um cluster de duas máquinas CoreOS 
para trabalhar com alguns containers Docker. Para isso, usaremos como cloud 
provider a Amazon. 
A primeira coisa a ser feita é criar as duas instâncias CoreOS, neste caso, 
com a AMI (Amazon Machine I mage) estável mais recente: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
97 
  

## Página 107

 
9.4. Criando um cluster Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 9.4: AMI CoreOS 
 
 
Prosseguindo com a criação, é necessário indicar a quantidade de instân- 
cias que vamos construir: 
 
 
 
 
 
 
 
 
 
 
 
 
98 
  

## Página 108

 
Casa do Código Capítulo 9. Um pouco sobre CoreOS Linux 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Fig. 9.5: CoreOS quantidade de instâncias 
 
 
Para a criação do cluster, é preciso armazenar os endereços dos nós do 
CoreOS e os metadados. Como vimos anteriormente, essa responsabilidade 
pertence ao ETCD. Seu uso é simples, e tudo o que precisamos fazer é gerar 
um token acessando a sua URL: 
 
 
 
Ainda precisamos personalizar a inicialização das novas instâncias (para 
configurar detalhes de rede), a comunicação com o serviço de descobertas 
ETCD e o gerenciador de cluster fleet. 
No painel de configuração, podemos inserir o arquivo c l o u d - c o n f i g 
que, como vimos no início deste capítulo, é responsável por carregar essas 
configurações na inicialização do CoreOS: 
 
 
 
 
 
 
 
 
99 
  

## Página 109

 
9.4. Criando um cluster Casa do Código 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
As informações do c l o u d - c o n f i g devem ser inseridas na opção User 
d ata. 
 
 
 
 
 
 
 
 
 
Fig. 9.6: CoreOS adicionando cloud-config 
 
 
Finalizando a configuração e com as instâncias criadas, podemos testar o 
cluster acessando qualquer um dos nós. Com o utilitário fleetctl, vamos 
listar todas as máquinas que pertencem ao cluster: 
 
 
 
 
 
 
 
 
 
 
 
 
100 
  

## Página 110

 
Casa do Código Capítulo 9. Um pouco sobre CoreOS Linux 
 
9 .5 Criando u m serviço 
Como sabemos, o fleet é responsável por gerenciar o agendamento de ser- 
viços para todo o cluster, funcionando como uma interface centralizada de 
controle que manipula o sys t e md de cada nó do cluster. 
Para começar, podemos criar o primeiro arquivo de serviço 
n g i n x @ . s e r v i c e. O @ na descrição do arquivo indica que ele é ape- 
nas um modelo: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Analisando por partes, temos um cabeçalho de seção representado por 
[Unit] e, logo em seguida, alguns metadados sobre a unidade criada. 
Em Description, estamos informando a descrição do serviço e verifi- 
cando as dependências, que, neste caso, está conferindo se os serviços ETCD 
e Docker estão disponíveis antes de prosseguir. 
Na sequência, um outro arquivo de serviços é adicionado, o 
n g i n x - d i s c o v e r y @ % i . s e r v i c e. Ele será responsável por atualizar 
o ETCD com as informações sobre o container Docker. O sufixo %i no final 
de alguns nomes serve como variável para receber parâmetros enviados pelo 
fleet. 
É preciso informar que serviços devem ser executados, e isso está sendo 
definido na seção [Service]. Como queremos controlar containers Doc- 
 
101 
  

## Página 111

 
9.6. Registrando um serviço Casa do Código 
 
ker, primeiro é preciso desativar o serviço de tempo limite, pois levará um 
tempo maior que o padrão durante a primeira inicialização do container em 
cada nó do cluster. 
Um outro detalhe importante é o controle das ações de start e s to p do 
nosso serviço. O sys t em d precisa ser informado que queremos ter o controle 
e, então, é preciso definir o modo Ki l l Mo d e para none. 
Antes de inicializar o serviço, é necessário ter certeza de que o ambiente 
está limpo, porque o serviço será inicializado pelo nome e, como sabemos, o 
Docker só permite um nome único por container. 
Note que as instruções ExecStartPre possuem =- em sua sintaxe. Isso 
indica que essas rotinas podem falhar e, mesmo assim, a execução do arquivo 
deve prosseguir. Ou seja, caso exista um container com o nome n g i n x, essas 
tarefas vão obter êxito. Nas duas últimas instruções, serão executados o pull 
da imagem utilizada e o run para a criação do container. 
Por fim, queremos que o serviço seja executado somente em nós que não 
possuam um container Nginx. É isso que a chamada na seção [X-Fleet] 
faz: armazena as instruções de comportamento do fleet. Neste caso, esta- 
mos inserindo uma restrição e garantindo a execução de apenas um container 
Nginx, por cada nó em todo o cluster. Essa configuração fica interessante em 
clusters maiores. 
 
9.6 Registrando u m serviço 
É preciso registrar o estado atual dos serviços inicializados no clus- 
ter. Para isso, criaremos um outro arquivo de serviço chamado 
n g i n x - d i s c o v e r y @ . s e r v i c e. O novo arquivo é bastante parecido com 
o anterior, porém este novo serviço é de acompanhamento para atualizar o 
ETCD, informando sobre a disponibilidade do servidor: 
 
 
 
 
 
 
 
 
102 
  

## Página 112

 
Casa do Código Capítulo 9. Um pouco sobre CoreOS Linux 
 
 
 
 
 
 
 
 
 
 
 
 
Aqui temos a diretiva BindsTo, que é uma dependência para verificar o 
estado do serviço e coletar informações. Caso o serviço listado seja interrom- 
pido, o nosso serviço de acompanhamento parará também, porém estamos 
modificando isso. Caso o container falhe de forma inesperada, as informa- 
ções no ETCD serão atualizadas. 
Para manter as informações sempre atualizadas, temos um loop infi- 
nito e, dentro do loop, estamos executando o etcdctl, que é respon- 
sável por alterar os valores em e tcd que estão sendo armazenados em 
/ a n n o u n ce / s e r v i c e s / n g in x% i. 
Finalmente, na última instrução, estamos garantindo que esse serviço seja 
inicializado na mesma máquina onde o container estiver em execução. 
 
9.7 Inicializando o cluster 
De posse dos dois modelos de serviços, vamos enviá-los para o cluster utili- 
zando o comando fleetctl: 
 
 
 
Após o envio, podemos verificar se os arquivos de serviço estão disponí- 
veis para o cluster: 
 
 
 
 
 
 
 
103 
  

## Página 113

 
9.7. Inicializando o cluster Casa do Código 
 
Agora que os modelos estão registrados no sistema de inicialização para 
todo o cluster, precisamos carregá-los especificando o novo nome para cada 
serviço. No caso, a referência da porta 80 será usada indicando que o con- 
tainer está funcionando nesta porta: 
 
 
 
Com isso, podemos conferir em quais nós do cluster o serviço foi carre- 
gado: 
 
 
 
 
 
 
 
 
 
Como os serviços foram todos carregados nas máquinas do cluster, vamos 
finalmente iniciar, para que tudo funcione: 
 
 
Para saber rapidamente se o container do Nginx foi inicializado e está 
funcionando corretamente nos nós do cluster, podemos realizar requisições 
no endereço IP público de cada host: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
104 
  

## Página 114

 
Casa do Código Capítulo 9. Um pouco sobre CoreOS Linux 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Gerenciar containers Docker no CoreOS e distribuí-los em um cluster é 
bastante interessante, mesmo que possa levar um pouco de tempo até você 
ficar bastante familiarizado com todo o sistema e suas regras. 
O projeto CoreOS tem um futuro promissor na gestão e distribuição de 
aplicações em containers. Dedique um tempo para compreendê-lo melhor. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
105 
  

## Página 115

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Página 116

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Capítulo 10 
O que estudar além? 
 
 
Estamos na reta final! Nas próximas seções, veremos algumas recomendações 
de tecnologias complementares, para que você siga descobrindo mais sobre o 
ecossistema Docker. 
 
10.1 A alternativa ao Docker Compose, o azk 
Assim como o C o m p o s e, azk é uma ferramenta de orquestração de ambientes 
de desenvolvimento que, por meio de um arquivo manifesto Azkfile.js, 
ajuda o desenvolvedor a instalar, configurar e executar ferramentas comu- 
mente utilizadas para desenvolver aplicações web de forma rápida. 
 
 
 
 
 
 
  

## Página 117

 
10.2. Docker Machine Casa do Código 
 
1 0 .2 Docker Machine 
Docker Machine é um facilitador para criar hosts configurados com Docker 
partindo da nossa máquina local. Com ele, podemos estabelecer uma ligação 
com os provedores de Cloud via API, e solicitar a criação de novos servidores 
com Docker instalado. 
Por ser um projeto complementar, sua instalação é independente. No caso 
do Linux, pode ser instalado da seguinte forma: 
 
 
 
 
 
 
 
 
No momento em que escrevo este livro, o Docker Machine ainda é uma 
versão beta e significa que poderá sofrer mudanças. Para exemplificar o seu 
uso, vamos criar uma máquina local com VirtualBox. Desta forma, tudo o que 
precisamos fazer é informar ao docker-machine, com a opção --driver, 
que o provedor onde queremos criar o novo host é, na verdade, uma máquina 
virtual local. V eja em código: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
108 
  

## Página 118

 
Casa do Código Capítulo 10. O que estudar além? 
 
Concluída a etapa de criação, podemos observar que foi feito o down- 
load de uma imagem pequena e customizada chamada boot2docker. Essa 
imagem foi utilizada pelo Virtualbox para gerar o host. V erificaremos o host 
criado com a opção ls: 
 
 
 
 
 
 
Outro detalhe importante é que devemos dizer ao Docker Machine qual 
máquina vamos trabalhar. Para isso, vamos apontar o nosso client Docker 
local, para fixar a comunicação com o host criado: 
 
 
Agora, toda operação com containers realizada será aplicada no novo host 
existente no Virtualbox: 
 
 
 
 
 
 
 
 
 
 
 
 
 
A documentação do projeto conta com exemplos de uso em VPS e no 
Cloud da Amazon. Acesse https://docs.docker.com/machine/, verifique e faça 
alguns testes. 
 
1 0 . 3 Docker Swarm 
Swarm é um sistema de cluster nativo para Docker que utiliza a API padrão. 
Ou seja, qualquer ferramenta que fizer uso da API Docker poderá usar Swarm 
 
109 
  

## Página 119

 
10.3. Docker Swarm Casa do Código 
 
para escalar containers, de forma transparente, entre vários hosts. Assim 
como o Docker Machine, Swarm encontra-se em versão beta no momento 
em que este livro é escrito. 
Tudo o que precisamos para usar Swarm é fazer o pull de sua imagem 
e, em seguida, criar um container de gestão do cluster: 
 
 
 
 
 
A opção create nos retorna um t ok en que serve de autenticação para 
cada nó de um cluster. Um agente será instalado em cada ponto referenciando 
no host gestor, de forma que mantenha atualizado as informações sobre os 
containers em execução. O token pode ser chamado de cluster_id. 
Podemos fazer login em cada nó e inicializar o Docker com suporte para 
uso de sua API via HTTP, lembre-se apenas das opções: 
 
 
Agora, só precisamos registrar o agente Swarm que realiza o serviço de 
descoberta de nós para o cluster. Para isso, o IP do nó deve ser acessível ao 
nosso gestor. O seguinte comando vai criar o agente: 
 
 
 
 
 
 
Note que foi informado o IP do nó e o token que geramos com create 
para estabelecer a autenticação entre o gestor do cluster e a nova máquina. 
Assim, podemos inicializar o gestor Swarm com o seguinte comando: 
 
 
 
Observe o mapeamento de portas. Nele estou informando uma porta para 
Swarm que seja direcionada para a porta da API do Docker. Além disso, o 
token também é informado. 
 
1 10 
  

## Página 120

 
Casa do Código Capítulo 10. O que estudar além? 
 
Agora podemos testar e ver se o cluster está funcionando. No exemplo a 
seguir, podemos coletar informações dos d a em o n s Docker presentes no clus- 
ter, no caso apenas do nó: 
 
 
 
 
 
 
 
 
 
 
 
 
Nesta consulta, foi necessário informar o endereço do host responsável 
pela gestão, para que ele colete as informações usando a opção info. Como 
resposta, temos a informação de que, no cluster, existe apenas 1 nó presente 
e 11 containers criados. Outros comandos podem ser utilizados dessa mesma 
forma para listar e criar containers, verificar logs e trabalhar com imagens. 
Também é possível solicitar ao Swarm que liste apenas os nós do cluster, 
com a opção swarm list: 
 
 
 
 
 
 
 
Docker Swarm também pode ser usado em conjunto com Docker Machine 
para integrar a um cluster cada novo host criado. Para saber mais, consulte a 
documentação https://docs.docker.com/swarm/. 
 
1 0.4 Alpine Linux 
Ao construir imagens Docker, não nos preocupamos com o seu tamanho. 
Porém, depois de um tempo, isso pode ser um problema, pois quanto maior 
a imagem maior será o tempo para pull e push no Docker Hub. 
 
111 
  

## Página 121

 
10.4. Alpine Linux Casa do Código 
 
Pensando nisso, o time da Glider Labs vem se empenhando no projeto 
Alpine Linux, um sistema operacional projetado para ser pequeno, simples e 
seguro. Focaremos apenas em seu tamanho para comparar com as imagens 
base mais comuns. 
Para esse exemplo, podemos fazer uso da imagem oficial do n g i n x: 
 
 
Criaremos agora um Dockerfile usando o Alpine como imagem base, e 
instalaremos o Nginx: 
 
 
 
 
 
 
 
 
 
Note que a diferença está apenas no gerenciador de pacotes do Alpine, 
que no caso se chama apk. Assim, criaremos nossa imagem para comparar 
o tamanho com a oficial do Nginx, que é baseada em Debian: 
 
 
Agora, comparando os tamanhos das imagens, note a diferença. 
 
 
 
 
 
 
 
Dedique um tempo para estudar mais sobre a gestão de pacotes do Alpine 
Linux. Este projeto é promissor e deve contribuir bastante com a comunidade 
Docker. 
 
 
 
 
112 
  

## Página 122

 
Casa do Código Capítulo 10. O que estudar além? 
 
1 0 . 5 Dúvidas? 
V ocê pode encontrar todos os códigos-fontes utilizados aqui em: https:// 
github.com/infoslack/docker-exemplos 
Se você tiver alguma dúvida sobre este livro, junte-se à lista em http:// 
docker.infoslack.com. 
Lá, você pode enviar a sua pergunta! Eu e os participantes do grupo ten- 
taremos ajudar. 
Muito obrigado! 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
113 
  

## Página 123

 
Índice Remissivo Casa do Código 
 
 
 
 
 
Índice Remissivo 
 
 
–bip, 45 
–fixed-cidr, 45 
–name, 11 
–volumes-from, 35 
-P , 21 
-it, 9 
-v , 34 
-w, 26 
 
ADD, 23 
 
backup, 38 
bash, 9 
brctl, 45 
bridge0, 49 
build, 19 
 
CMD, 28 
command, 8 
commit, 11 
container, 3 
 
Docker, 7 
Docker Hub, 53 
docker0, 45 
Dockerfile, 19 
 
echo, 8 
ENTRYPOINT, 28 
 
114 
ENV , 35 
exec, 23 
EXPOSE, 21  
FROM, 19  
images, 11 
inspect, 23  
load, 31 
login, 53 
logs, 29  
máquina virtual, 4 
MAINTAINER, 19  
netmask, 49 
network, 43  
port, 11 
ps, 9 
pull, 53 
push, 53  
remove, 14 
restore, 38 
ro, 34 
route, 49 
run, 8 
rw, 34 
  

## Página 124

 
Casa do Código Índice Remissivo 
 
save, 31 
search, 53 
 
tags, 53 
 
Ubuntu, 7 
 
VOLUME, 3 5 
volumes, 33 
 
WORKDIR, 26 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
115 
  