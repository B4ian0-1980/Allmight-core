---json
{
  "id": "comandos_linux",
  "title": "sumário",
  "categoria": "06-devops-infra",
  "subcategoria": "linux",
  "resumo": "Guia tecnico e referencias sobre sumário.",
  "gatilhos": [
    "comandos",
    "devops",
    "infra",
    "linux"
  ],
  "perguntas_tipo": [
    "Como utilizar sumário?",
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


--------------------------------------------------

**CLIQUE PARA NOS SEGUIR**

# sumário

# Apresentação ..................................................................... 
# Distros Derivadas .............................................................. 
# Instalado o Linux na VM ................................................. 
#     6.1 Preparando a VM ...................................................  
#  
# Instalação do Ubuntu .......................................................
# Entendendo o Linux ......................................................... 
#     13.1 Estrutura do Linux/Windows ...........................
#     13.2 Repositórios e Pacotes .......................................
#  
# Manipulado Pacotes com o DPKG .................................
# Repositórios .........................................................................
# Comandos para manipulação de diretório...................
#  
# Comandos para manipulação de Arquivos .................
# Comandos Diversos ...........................................................
# Comandos de Rede ...........................................................
#  
# Comandos para Manipulação de Contas .....................
# Arquivos Compactador .....................................................
# Mapas Mentais ...................................................................
#  
#  
#  
#  

# 1
# 3
# 6
# 7
#  
# 10
# 13
# 14
# 15
#  
# 17
# 18
# 20
#  
# 21
# 22
# 24
#  
# 26
# 27
# 28


--------------------------------------------------

# apresentação

**# 01**

# Linux é o **# kernel**#  de um sistema operacional, você provavelmente já ouviu falar do
# UNIX, então, o Linux é um clone do UNIX. Que na verdade foi criado por **# Linus**
**# Torvalds**#  no Scratch. 
#  
# O Linux é gratuito e tem seu código aberto, o que significa que você pode
# simplesmente mudar qualquer coisa no Linux e redistribuí-lo em seu próprio nome
#  
# Existem várias **# distribuições**# (distros) Linux, cada uma tem suas próprias
# características


--------------------------------------------------

**# 02**

# Linux é usado principalmente em servidores, cerca de **# 90%**#  da internet é
# alimentada por **# servidores Linux**# . Isso ocorre porque o Linux é **# rápido**# , **# seguro**#  e
**# gratuito. **# A maioria dos vírus é criado para rodar no **# WINDOWS****# ,****#  **# e não no Linux
# esse é um dos motivos para o **# S.O**#  ser mais rápido e seguro. 
#  
# Como o Linux não possui custos com **# licenças **# e também é muito mais seguro,
# muitas empresas utilizam o sistema operacional,  então o profissional  que estuda
# e **# manja de verdade**#  certamente está preparado para trabalhar em qualquer
# empresa de **# T.I**#  falta muitos profissionais nessa área ainda, as **# faculdades**#  não tem
# ensinado muito Linux ou tem pouco, muito pouco na prática, grandes empresas
# que **# vendem**#  softwares fecham acordos para seus **# softwares**#  e **# linguagens**#  serem
# utilizado como forma de ensino e no final falta profissionais de **# Linux**# , e outros
# Softwares livres no **# mercado**#  de trabalho.


--------------------------------------------------

**# 03**
# distros
# derivadas

# Uma distribuição derivada é **# baseada**#  no trabalho feito em outra DISTRIBUIÇÃO,
# mas que tem seus próprios **# objetivos**# , **# identidade**#  e **# audiência**# , e que foi criada por
# uma entidade independente. As distribuições derivadas **# modificam**#  a "ORIGINAL"
# para atingir seus próprios objetivos.
#  
#  
**# POR QUE USAR UM DERIVADO?**
# Para atender uma necessidade específica sua, uma distribuição derivada pode já
# vim com as ferramentas que te atendam melhor de acordo com seu perfil. Muitas
# distribuições usam o **# DEBIAN**#  como base, mas tem suas próprias características.
#  
#  


--------------------------------------------------

**# 04**


--------------------------------------------------

**# 05**


--------------------------------------------------

# instalando#  # o

# linux#  # na#  # vm

**# 06**

# D O W N L O A D S

# V i r t u a l B o x :#   # h t t p s : / / w w w . v i r t u a l b o x . o r g / w i k i / D o w n l o a d s
# U b u n t u :#   # h t t p s : / / w w w . u b u n t u . c o m / d o w n l o a d / d e s k t o p

# VERSÃO ATUALIZADA, CLIQUE AQUI.

### CLIQUE PARA NOS SEGUIR

## Se você não tem o Linux Instalado agora e quer brincar com alguns comandos

## clique aqui para rodar um emulador no seu navegador


--------------------------------------------------

# preparando#  # a

# vm

**# 07**

**## COMO GANHAR DINHEIRO COM O LINUX - CLIQUE AQUI**


--------------------------------------------------

**# 08**


--------------------------------------------------

**# 09**


--------------------------------------------------

# instalação#  # do

# ubuntu

**# 10**

**## COMO GANHAR DINHEIRO COM O LINUX - CLIQUE AQUI**


--------------------------------------------------

**# 11**


--------------------------------------------------

**# 12**

# PRONTO


--------------------------------------------------

# entendendo#  # o
# linux

# VERSÃO ATUALIZADA, CLIQUE AQUI.

**# 13**

### CLIQUE PARA NOS SEGUIR


--------------------------------------------------

# Estrutura#  # do#  # linux/windows

**# 14**

**## DIRETÓRIOS**

##  
## No **## LINUX**##  a organização é feita em

## formato **## ÁRVORE**## .

##  
## No **## WINDOWS**##  a organização é feita

## dentro de uma única pasta, que

## normalmente fica dentro **## C:**

## @linux.gnu


--------------------------------------------------

**## /bin **## Binários dos usuários
**## /boot **## Arquivos do sistema de Boot (Grub)
**## /dev **## Arquivos de dispositivos
##  
**## /etc **## Arquivos de configuração do sistema
**## /home **## Diretório dos usuários
**## /proc**##  Informações de processos ativos e de hardware
##  
**## /root **## Diretório do usuário root (Tem poder total)
**## /var **## Logs, filas de e-mail, impressão, banco de dados
##  
##  
##  
##  
##  
##  
**## /usr **## Programas, código-fonte, documentação
**## /lib **## Bibliotecas e Módulos do Kernel
##  
**## /tmp **## Diretório para arquivos temporários
**## /srv **## Dados de serviços fornecidos pelo sistema
**## /sbin **## Armazena arquivos executáveis que representam
##  
**## /opt **## Instalação de programas não oficiais da distribuição
**## /mnt **## Diretório de montagem de dispositivos
**## /media **## Diretório de montagem de dispositivos
##  

## @linux.gnu

# Estrutura#  # do#  # linux#  # -#  # Diretórios

**# 14.1**


--------------------------------------------------

#  
# o#  # que#  # são
# Repositórios#  # e#  # pacotes#  # ?

**# 15**

**# Repositórios: **# servidores que armazena os pacotes, o repositório também
# pode estar em outro local, tipo um cd-rom.
#  
**# Pacotes:****#  **# são programas, bibliotecas, papeis de parede, icones, um pacote
# pode conter várias coisas. Os pacotes ficam dentro dos repositórios.


--------------------------------------------------

# TIPOS#  # DE#  # REPOSITÓRIO

**# 16**


--------------------------------------------------

# Manipulando#  # Pacotes#  # com#  # o#  # dpkg

**# 17**

# O dpkg é o comando básico para lidar com pacotes Debian no sistema.
# Se você tem **# pacotes .deb**# , é com o **# dpkg**#  que você instala ou analisa
# seu conteúdo. Mas este programa tem apenas uma **# visão parcial **# do
# universo, ele sabe o que está instalado no sistema, e o que for dado na
# linha de comando, mas não sabe nada dos outros pacotes disponíveis.
# Assim, ele vai **# falhar se uma dependência **# não for satisfeita.
# Ferramentas como o apt, ao contrário, criará uma lista de dependências
# para instalar tudo o mais automaticamente possível.
#  
**# dpkg**#  deve ser vista como uma ferramenta de sistema (nos bastidores),
# e **# apt**#  como uma ferramenta mais próxima do usuário, que supera as
# limitações das antigas. Estas ferramentas trabalham juntas, cada uma
# com suas particularidades, **# adequadas para tarefas específicas**# .

**# # dpkg -i NomePacote.deb:**#  Instala um Pacote já baixa na máquina
**# # dpkg -l Pacote.deb: **# Estado do Pacote (Instalação/Problemas).
**# # dpkg -S Arquivo: **# Qual pacote instalou o arquivo
#  
**# # dpkg -L Pacote.deb: **# Lista os arquivos instalados pelo pacote
**# # dpkg --contens Pacote.deb: **# Exibi o conteúdo do pacote
**# # dpkg -P NomePacote.deb: **# Para remover completamente um pacote

Pacote.deb

VirtualBox.deb


--------------------------------------------------

**# apt update: **# Atualiza a lista do repositório
**# apt upgrade: **# Atualiza seus pacotes
**# apt dist-upgrade:**#  Atualiza sua Distribuição
#  
**# cat /etc/apt/sources.list **# Exibe a lista dentro do repositório
#  
**# apt autoclean: **# Apaga os pacotes que não existem mais
**# apt autoremove: **# Apaga os pacotes abandonados
**# apt remove NomePac: **# Remove um pacote

**# 18**

# repositórios

## @linux.gnu

**# pacote.deb**

**# nettools**

**# hwinfo**

**## Pacote**
**## abandonado**


--------------------------------------------------

**# yum install N*****# omePacote*****# :**#  Baixa e instala um pacote rpm
**# yum localinstall N*****# omePacote.rpm*****# :**#  Instalar um RPM e vai tentar resolver
# todas as dependências para você, usando seus repositórios
#  
**# yum update NomePacote:**#  Atualiza todos os pacotes instalados no sistema
**# yum remove NomePacote:**#  Remove um pacote RPM
#  
**# yum list:**#  *# Lista todos os pacotes instalados no sistema*
**# yum search NomePacote: **# Encontra um pacote no repositório rpm
#  
#  
**# yum clean packages: **# Limpa um cache de rpm, apagando os pacotes
# baixados
**# yum clean all: **# Remove os arquivos de cache e o cabeçalho do pacote
#  
#  
#  
#  
#  

**# 19**

# pacotes#  # RedHat,#  # fedora,#  # centos#  # ...


--------------------------------------------------

# Comandos#  # para#  # manipulação#  # de
# diretório

**# ls: **# Lista os arquivos do diretório atual
**# ls *****# /bin /sbin*****# : **# Lista os arquivos do diretório /bin e /sbin
**# ls -al**# : Exibição de todos arquivos até os ocultos
**# ls -f:**#  Não classifica a listagem
**# ls -n:**#  Usa a identificação de usuário e grupo numérica
**# ls -R: **# Lista diretórios e sub-diretórios recursivamente
#  
**# cd *****# home*****# : **# Entra no Diretório home
**# cd ~:**#  Diretório HOME
**# cd /:**#  Retornará ao diretório raíz
**# cd -: **# Retornará ao diretório anteriormente acessado
**# cd ..: **# Sobe um diretório
**# pwd: **# Mostra o diretório atual
#  
#  
**# mkdir *****# NovoDiretório*****# : **# Cria um diretório (No Windows seria chamado de pasta)
**# rmdir *****# NovoDiretório*****# : **# Remove um diretório
#  
**# cat *****# arquivo.txt*****# : **# Mostra o conteúdo de um arquivo de texto
**# cat *****# -n Exemplo.txt*****# : **# Mostra o número das linhas
**# tac *****# arquivo.txt*****# :**#  Quase a mesma coisa só que, mostra o conteúdo inverso
#  
#  

**# 20**

## @linux.gnu


--------------------------------------------------

**# rm: **# Apaga arquivos
**# rm -i: **# Pergunta antes de remover, esta é ativada por padrão
**# rm -v:**#  Mostra os arquivos na medida que são removidos
**# rm -r: **# Usado para remover arquivos em sub-diretórios
**# rm -f:**#  Remove os arquivos sem perguntar
#  
**# rm *****# teste.txt*****# :**#  Apaga o arquivo ***# teste.txt*****#  **# no diretório atual
#  
**# rm ******# .txt*****# :**#  Apaga todos os arquivos do diretório atual que terminam com *# .****# txt***
**# rm *****# *.txt*****#  *****# teste.novo*****# : **# Apaga todos os arquivos do diretório atual que terminam
# com ***# .txt*****#  **# e também o arquivo ***# teste.novo***
#  
**# cp: **# Copia arquivos
**# cp -i:**#  Pergunta antes de substituir um arquivo existente
**# cp -f:**#  Não pergunta, substitui todos os arquivos caso já exista
#  
**# cp *****# teste.txt teste1.txt*****# : **# Copia o arquivo ***# teste.txt***#  para ***# teste1.txt***
**# cp*****#  teste.txt /tmp*****# : **# Copia o arquivo ***# teste.txt***#  para dentro do diretório ***# /tmp***
**# cp *****# * /tmp*****# : **# Copia todos os arquivos do diretório atual para ***# /tmp***
**# cp *****# -R /bin /tmp*****# : **# Copia todos os arquivos e o diretório ***# /bin***#  para ***# /tmp***
#  
**# mv: **# Move ou renomeia arquivos e diretório
**# mv -f:**#  Substitui o arquivo de destino sem perguntar
**# mv -i:**#  Pergunta antes de substituir. É o padrão
**# mv -v: **# Mostra os arquivos que estão sendo movido
#  
**# mv *****# teste.txt teste1.txt*****# :**#  Muda o nome do arquivo ***# teste.txt***#  para ***# teste1.txt***
**# mv *****# teste.txt /tmp*****# : **# Move o arquivo ***# teste.txt****#  *# para ***# /tmp***

**# 21**

# Comandos#  # para#  # manipulação#  # de
# Arquivos


--------------------------------------------------

# Comandos#  # Diversos

**# 1: Comandos específicos (facilita)**
**# lspci:  **# O que está conectado no barramento PCI
**# lspci -s 01:01.0 -v: **# Detalhes do dispositivo, como módelo e módulo
#  
**# lsusb: **# Dispositivos conectados as saídas USB do computador
**# lsusb -v -d 12d1:1002: **# Detalhes do que está conectado
#  
**# # lsmod: **# Módulos do sistema (Módulos é como os Drivers do Windows)
#  
#  
#  
**# 2: Lendo arquivos do sistema (Arquivos dos diretórios)**
**# cat /proc/cpuinfo: **# Exibe informações da CPU
**# cat /proc/meminfo: **# Exibe informações da memória
#  

## @linux.gnu

**# 22**

**### PS:**###  Agora que você já entendeu, os comandos serão apenas listados.

**# Dois Jeitos básicos de identificar recursos do hardware**


--------------------------------------------------

**# 22.1**

# Comandos#  # Diversos

**# df: **# Mostra o espaço livre/ocupado de cada partição
**# df -h: **# Tamanho dos arquivos e diretórios em GB
**# df -m:**#  Tamanhos em Mb
**# df -hT *****# /home*****# : **# Específico
**# df -T: **# Tipo de sistema de arquivos
#  
**# free:**#  Mostra detalhes sobre a utilização da memória RAM do sistema
**# free -m:**#  Mostra o resultado em Mbytes
**# free -t:**#  Mostra uma linha contendo o total
#  
**# grep: **# Procura por um texto dentro de um arquivo
**# grep **# “capitulo” texto.txt, ps ax | grep inetd, grep “capitulo” texto.txt -A 2 -B 2
#  
**# nl *****# teste.txt*****# : **# Mostra o número de linhas junto com o conteúdo de um arquivo
**# tail: **# Mostra as linhas finais de um arquivo texto
**# tail -n *****# 10 teste.txt*****# :**#  Mostra as 10 ultimas linhas do arquivo ***# teste.txt***
#  
#  
**# touch *****# teste.txt*****# :**#  Cria o arquivo
**# touch -a *****# teste.txt*****# : **# Muda somente a data e hora do **# acesso**#  ao arquivo
**# touch -m:**#  Muda somente a data e hora da **# modificação**
**# touch -t *****# 10011230 teste*****# : **# Altera da data e hora do arquivo para 01/10 e 12:30

## @linux.gnu


--------------------------------------------------

**# uname -a:**#  Exibe informações do kernel
**# echo: **# Mostra mensagens
**# echo**#  teste: Este comando é útil na construção de scripts
**# uptime: **# Tempo de execução do sistema desde que o computador foi ligado
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
**# reboot: **# Reinicia o computador
**# shutdown:**#  Desliga/Programável
#  
**# shutdown -r *****# 20*****# :**#  Faz o sistema ser reiniciado após 20 minutos.
**# shutdown -c:**#  Cancela a execução do shutdown
**# shutdown -h *****# now*****# :**#  Desligar o computador imediatamente
**# shutdown -r *****# now*****# : **# Reinicia o computador imediatamente
#  
**### shutdown 19:00 A manutenção do servidor será iniciada às 19:00”: **### Faz o computador entrar
### em modo monousuário (init 1) às 19:00 enviando a mensagem ***### "A manutenção do servidor será***
***### iniciada às 19:00 a todos os usuários conectados ao sistema"***
#  

**# 22.2**

## @linux.gnu


--------------------------------------------------

**# 23**

# Comandos#  # Diversos

**# O Systemd é um gerenciador de sistema e serviços. **# Ele da início e supervisio-
# na todo os sistema e é baseado no conceito de unidades (httpd.service).
#  
**# Existe 7 tipos de unidades.**
# - Service
# - Socket
# - Device
#  
# - Mount
# - Automount
# - Target
# - Snapshot
#  
#  
**# systemctl start httpd.service:**#  Inicia um serviço
**# systemctl stop httpd.service: **# Para**#  **# um serviço
**# systemctl restart httpd.service:**#  Reinicia um serviço
#  
**# systemctl status httpd.service:**#  Estado de um serviço, ativou ou não
**# systemctl enable httpd.service: **# Inicia o serviço no Boot
**# systemctl disable httpd.service:**#  Remove o serviço do Boot

## @linux.gnu

**# SystemD**


--------------------------------------------------

**# /etc/network/interfaces: **# Arquivo de configuração da interface de rede
#  
**# Modo DHCP**
# dhcp
# auto eth0
# iface eth0 inet dhcp
#  
#  
**# Modo estático**
# static
# iface eth0 inet static
# address 192.168.1.10
# netmask 255.255.255.0
# network 192.168.1.0
# broadcast 192.168.1.255
#  
#  
#  
#  
#  
#  
#  
#  
**# ping 127.0.0.1:**#  Testa a interface local
**# ping -c 3 127.0.0.1:**#  Envia  3 pacotes
#  
**# ping -i 2 127.0.0.1:**#  Envia  a cada 2 seg
**# ping -s 12 127.0.0.1: **# Tamanho do pacote
#  

## @linux.gnu

# Comandos#  # de#  # rede

**# 24**


--------------------------------------------------

# Comandos#  # de#  # rede

**# ifconfig: **# Verificar seu endereço IP
**# ifconfig eth0: **# Exibe a configuração de uma placa de rede eth0
**# ifup eth0:**#  Ativa uma interface ‘eth0’
**# ifdown eth0:**#  Desabilita
#  
**# ifconfig eth0 192.168.0.1 netmask 255.255.255.0:**#  Configura IP
**# dhclient eth0:**#  Ativa a interface ‘eth0’ em modo dhcp
**# route**#  **# -n:**#  Exibe tabela de rota
#  
**# host *****# www.google.com*****# : **# Descobrir o endereço IP de um host
**# iwconfig eth1:**#  Exibe a configuração de uma placa de rede sem fio
**# iwlist scan: **# Exibe as redes sem fio
#  
**# who: **# Mostra quem está atualmente conectado no computador
**# who -b: **# Mostra o horário do último boot do sistema
**# who -q: **# Mostra o total de usuários conectados aos terminais
**# who -r: **# Mostra o nível de execução atual do sistema
**# who -H: **# Mostra o cabeçalho das colunas
#  
**# whoami:**#  Mostra o nome que usou para se conectar ao sistema
**# dnsdomainname: **# Mostra o nome do domínio de seu sistema
**# hostname: **# Mostra ou muda o nome de seu computador na rede
#  
**# traceroute: **# Mostra na tela o caminho percorrido entre os Gateways da rede
**# traceroute -n:**#  Endereços numericamente ao invés de usar resolução DNS
**# traceroute *****# www.debian.org*****# : **# Caminho percorrido por um pacote
#  
**# tracepath *****# www.google.com*****# : **# Parecido ao comando traceroute

**# 24.1**

## @linux.gnu


--------------------------------------------------

**# netstat: **# Mostra conexões de rede, tabela de roteamento, estatísticas...
**# netstat -i eth0:**#  Estatísticas da interface de rede
**# netstat -t eth0: **# Lista conexões TCP
**# netstat -u eth0:**#  Lista conexões UD
#  
**# wall:**#  Faz a leitura de um arquivo e escreve o resultado em todos os terminais
**# wall*****#  teste.txt*****# :**#  Somente o usuário root pode utilizar este comando
#  
**# Exemplo:**#  wall /tmp/mensagem.txt, echo Teste de mensagem enviada a todos
# os usuários conectados ao sistema | wall
#  
#  
**# Acesso Remoto com ssh**
**# apt install ssh:**#  Instalando SSH
**# nano/etc/ssh/sshd_config: **# Arquivo de configuração
***# PermitRootLogin yes***#  (Editar Linha ***# #PermitRootLogin prohibit-password*****# )**
***# Port 22***#  (Linha vai está comentada, é só tirar o comentário)
#  
**# ssh -l root@IP-Servidor: **# Conectar como usuário ***# ROOT***

**# 25**

## @linux.gnu


--------------------------------------------------

**# adduser *****# Nome-Usuário*****# : **# Adiciona um usuário ou grupo no sistema
**# adduser -group *****# Nome-Grupo*****# : **# Cria um novo grupo ao invés de um novo usuário
#  
**# userdel -r *****# Nome-Usuário*****# :**#  Força a remoção dos dados do usuário
**# userdel -f *****# Nome-Usuário*****# :**#  Remove o diretório HOME
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
**# groups:**#  Mostra os grupos que o usuário pertence
**# addgroup*****#  Novo-Grupo*****# : **# Adiciona um novo grupo de usuários no sistema
**# groupdel *****# Novo-Grupo*****# : **# Apaga um grupo do sistema
#  
#  
**# passwd *****# Novo-Usuário*****# :**#  Muda a senha
**# passwd -i *****# Novo-Usuário*****# :**#  Mínimo de dias para a senha ser alterada
**# passwd -l *****# Novo-Usuário*****# :**#  Bloqueia a conta do usuário
**# passwd -u *****# Novo-Usuário*****# : **# Desbloqueia a conta de um usuário
**# passwd -x *****# Novo-Usuário*****# :**#  Especifica o número de dias que a senha poderá ser
# usada

**# 26**

# Comandos#  # para#  # manipulação#  # de
# contas


--------------------------------------------------

**# tar -cvzf Arquivos.tar.gz /home: **# Diretório home compactado e arquivo criado
**# tar -cvjf Arquivos.tar.bz2 /home:**#  Compressão maior que o **# gzip**
#  
#  
#  
**# c:**#  Cria novo arquivo
**# v:**#  Exibe o processo
**# z: **# Compressão .gzip
#  
#  
#  
#  
**# tar -xvf Arquivos.tar.gz : **# Descompactado .gz
**# tar -xvf Arquivos.tar.bz2: **# Descompactado .bz2
#  
**# tar -tvf Arquivos.tar.gz: **# Listar conteúdos do arquivo compactado .gz
**# tar -tvf Arquivos.tar.bz2:**#  Listar conteúdos do arquivo compactado .bz2
###  

**# 27**

# arquivos#  # COMPACTAdos

**# j: **# Compressão .bz2
**# f: **# Nome do arquivo
**# x: **# Extrair
###  


--------------------------------------------------

# Você pode usar o Linux para ganhar uma **# RENDA EXTRA**#  ou se destacar como
# um excelente profissional de TI. Um jeito simples que utilizamos é
# substituindo#  **# Servidores Pagos**# (Windows Server)#  por Linux que é 100%
# gratuito, então o VALOR que seria gastos com Licenças é convertido para o
# profissional, que é um ótimo valor, já que as licenças que seriam compradas
# são bem caras.
#  
#  
#  
#  
#  
#  
#  
#  
#  
# O mercado  de TI sempre está aquecido para profissionais que realmente
# sabem Linux. **# As maiores empresas utilizam Linux em seus servidores**# , mas
# existem poucos profissionais no mercado que realmente sabem trabalhar com
# o Linux de forma profissional. Os que sabem estão sendo muito bem
# valorizados.
#  
**# Agora para você aprender Linux de forma profissional de forma estruturada,**
# passo a passo com suporte de um especialista, e aprender esse jeito simples
# de **# FATURAR **# com o Linux clique no botão abaixo AGORA.
#  
###  

**# Quero aprender a FATURAR com o Linux agora**

# Como#  # ganhar#  # dinheiro#  # com#  # o#  # Linux#  # em

# média#  # de#  # 1.500#  # a#  # 3.000#  # por#  # projeto

# implementado


--------------------------------------------------

# instalação

**# 28**

**### I*****### nstagram***
***### @linux.gnu***


--------------------------------------------------

# Administração

**# 29**

**### I*****### nstagram***
***### @linux.gnu***


--------------------------------------------------

# gerenciamento#  # básico

**# 30**

**### I*****### nstagram***
***### @linux.gnu***


--------------------------------------------------

# sistema#  # de#  # arquivos#  # e#  # Disco

**# 31**

**### I*****### nstagram***
***### @linux.gnu***


--------------------------------------------------

# pacotes#  # rpm

**# 32**

**### I*****### nstagram***
***### @linux.gnu***


--------------------------------------------------

# redes

**# 33**

**### I*****### nstagram***
***### @linux.gnu***


--------------------------------------------------

# sistemas#  # de#  # arquivos

**# 34**

**### I*****### nstagram***
***### @linux.gnu***


--------------------------------------------------

# Filtros#  # de#  # texto

**# 35**

**### I*****### nstagram***
***### @linux.gnu***


--------------------------------------------------

# Permissões

**# 36**

**### I*****### nstagram***
***### @linux.gnu***


--------------------------------------------------

# quotas#  # de#  # disco

**# 37**

**### I*****### nstagram***
***### @linux.gnu***

