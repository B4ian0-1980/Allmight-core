---json
{
  "id": "minicursodjango",
  "title": "10º WTADS - IFRN",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "Guia tecnico e referencias sobre 10º WTADS - IFRN.",
  "gatilhos": [
    "ifrn",
    "linguagens",
    "minicursodjango",
    "python",
    "wtads"
  ],
  "perguntas_tipo": [
    "Como utilizar 10º WTADS - IFRN?",
    "Quais as boas praticas de python?"
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
  "dono": "stack-python",
  "prioridade": 2
}
---

**# Mini Curso de Django**

# 10º WTADS - IFRN


--------------------------------------------------

**# Material deste mini curso**

# Código-fonte

# Esta apresentação


--------------------------------------------------

**# Objetivos**

# ●
# Mostrar o que é o Django e seus principais conceitos.
# ●
# Como fazer sua instalação e conﬁguração;
# ●
# Apresentar o modelo MVT (Model, View, Template);
# ●
# Por a mão na massa (Aí sim!).


--------------------------------------------------

**# Pré-Requisitos**

# ●
# Conhecimento básico de programação orientação a objetos (POO);
# ●
# Conhecimento básico em Python.


--------------------------------------------------

**# POO no modo "caldo de cana + **
**# pastel"**


--------------------------------------------------

**# O que é?**

# Classiﬁcar, organizar e abstrair as coisas do mundo real (classes) em uma 
# coleção de objetos que possuem características (dados) e realizam ações 
# (métodos).

### POO no modo "caldo de cana + pastel"


--------------------------------------------------

**# Como fazer isso?**

# É bem simples:

# ●
# Primeiro classiﬁque;
# ●
# Depois organize;
# ●
# E por ﬁm, abstraia (aqui começa a viagem...).

### POO no modo "caldo de cana + pastel"


--------------------------------------------------

**# Cenário exemplo**

# João foi ao supermercado e botou na cesta 1 kg de arroz, 1kg de feijão 
# preto, um pacote de 500g de linguiça toscana e 6 garrafas de cerveja. Ao 
# ﬁnal, foi ao caixa e pagou um total de 25 reais.

### POO no modo "caldo de cana + pastel"


--------------------------------------------------

**# Classiﬁcando e organizando...**

## ●
## João é um cliente do supermercado;
## ●
## 1 kg de arroz, … 6 garrafas de cerveja são produtos;
## ●
## No caso há 2 tipos de produto no exemplo: alimentos e bebidas;
## ●
## João pagou pelos produtos no supermercado. No caso trata-se de uma compra 
## na perspectiva de João e de uma venda na perspetiva do supermercado;
## ●
## Os itens comprados por João já não podem ser vendidos a outro cliente.

### POO no modo "caldo de cana + pastel"


--------------------------------------------------

**# O que abstrair daí?**

# A intensidade da viagem vai depender da necessidade do demandante do 
# sistema, ou seja, do que ele deseja controlar. 

# Atenção: Cuidado com a palavra SISTEMINHA! É mentira!

### POO no modo "caldo de cana + pastel"


--------------------------------------------------

**# O que abstrair daí?**

## ●
## Classes:

## ○
## Cliente, Produto, TipoProduto,  Venda e Estoque.
## ●
## Objetos:

## ○
## do tipo Cliente: João;
## ○
## do tipo Produto: Arroz, feijão, linguiça e cerveja;
## ○
## do tipo TipoProduto: Alimento e bebida.
## ○
## do tipo Venda: A venda realizada pelo supermercado a João;
## ○
## do tipo Estoque: A baixa dos itens vendidos a João.

### POO no modo "caldo de cana + pastel"


--------------------------------------------------

**# O que abstrair daí?**

## Modelagem básica:

## ●
## Cliente (nome, cpf, estado_civil, data_nascimento, e-mail, fone);
## ●
## Produto (descricao, preco);
## ●
## TipoProduto (descricao)
## ●
## Venda (data, cliente);
## ●
## VendaItem (venda, produto, quantidade, preco);
## ●
## Estoque (produto, quantidade, tipo_registro).

### POO no modo "caldo de cana + pastel"


--------------------------------------------------

**# Python no modo "caldo de cana"**


--------------------------------------------------

**# O que é?**

# É uma linguagem orientada a objetos, com tipagem dinâmica e fortemente 
# tipada.

### Python no modo "caldo de cana"


--------------------------------------------------

**# O que eu faço com ela?**

# Faz muita coisa, nas mais diversas áreas, mas hoje vamos nos focar no 
# Django e em escrever uma aplicação usando a abstração deﬁnida nos slides 
# anteriores.

### Python no modo "caldo de cana"


--------------------------------------------------

**# Como instalar?**

# ●
# Linux (Debian):

# ○
# $ apt-get install python3
# ●
# Mac OS:

# ○
# $ brew install python3
# ●
# Windows:

# ○
# Baixar o instalador e execute-o:

# ■
# https://www.python.org/downloads/

### Python no modo "caldo de cana"


--------------------------------------------------

**# Como instalar?**

# Além do python, precisamos instalar o pip, que é um gerenciador de pacotes 
# python.

# ●
# Linux (Debian), Mac OS ou Windows:

# ○
# $ curl https://bootstrap.pypa.io/get-pip.py | python3

### Python no modo "caldo de cana"


--------------------------------------------------

**# Houston, are you there?**

**# $ python3 --version**
**# $ pip3 --version**


--------------------------------------------------

**# O que é o Django?**

# ●
# É um framework python voltado para a criação de aplicações web, de 
# maneira simples e ágil.
# ●
# Trabalha com o conceito de aplicações plugáveis, ou seja, reutilizáveis.
# ●
# Utiliza o padrão # MVC# , através da sigla # MVT (model, view, template)# ;

# ○
# model#  = # model
# ○
# view#  = # template
# ○
# controller#  = # view


--------------------------------------------------

**# O que é o Django?**

# ●
# Tem uma poderosa ORM;
# ●
# Oferece uma aplicação "Django Admin" bem legal e que e pode ser 
# customizada.
# ●
# Oferece um servidor de aplicação interno (*# runserver*# ), muito útil na fase 
# de desenvolvimento e testes. # Atenção: Ele não foi projetado para ser 
# usado em produção, então não faça isso!


--------------------------------------------------

**# Ciclo de vida**

Fonte da Imagem 


--------------------------------------------------

**# Como instalar?**

**# $ pip3 install django**

# ●
# Caso queira especiﬁcar uma versão: 

**# ○**
**# $ pip3 install django==2.2.2**
# ●
# Veriﬁcando os pacote que foram instalados:

**# ○**
**# $ pip freeze**

# Obs: No caso estamos fazendo uma instalação básica. Em casa, estude sobre 
# como criar ambiente isolados: # VirtualEnv & VirtualEnvWrapper# .


--------------------------------------------------

**# Houston, do you hear me?**

**# $ python3 -c "import django; **
**# print(django.get_version())"**


--------------------------------------------------

**# Projeto**

# O Django trabalha com o conceito de projetos e aplicações.

# Um projeto pode conter "n" aplicações.

# A ideia é de que cada aplicação possa ser plugável, ou seja, reutilizável.

# É no projeto que ﬁcam as conﬁgurações "globais".


--------------------------------------------------

**# Criando um projeto**

**### $ django-admin startproject mini_curso_django**
**### $ cd mini_curso_django**
**### $ tree**
### .
### ├──###  manage.py   ### <<<   Utilitário de linha de comando do Django.
### └──###  mini_curso_django###        <<<   Diretório com as conﬁgurações do projeto.

### ├──###  __init__.py  ###  <<<   Arquivo vazio que indica ao Python que esse diretório é um pacote.
### ├──###  settings.py   ### <<<   Arquivo de conﬁguração do projeto.
### ├──###  urls.py   ### <<<   Arquivo com as urls do projeto.
### └──###  wsgi.py  ###  ### <<<   Um ponto de integração para servidores WEB compatíveis com WSGI.


--------------------------------------------------

**# Criando um projeto**

# Principais conﬁgurações...


--------------------------------------------------

**# Criando um projeto**

### Antes de fazer o primeiro teste com o projeto, vamos criar toda a estrutura de banco necessária 
### para as aplicações que já vêm deﬁnidas, por padrãom em settings.INSTALLED_APPS:

**### $ python3 manage.py migrate**


--------------------------------------------------

**# … three, two, one! Go!**

**# $ python3 manage.py runserver 8000**


--------------------------------------------------


--------------------------------------------------

**# Aplicação**

## Como já foi dito, a ideia é que cada aplicação seja plugável, ou seja, possa ser 

## utilizando em conjunto com outras aplicações.

## Levando em conta a nossa abstração, poderíamos imaginar, por exemplo, 3 

## aplicações:

## ●
## Atendimento:  Módulo voltando inicialmente ao controle dos clientes;

## ●
## Vendas: Módulo focado na parte do registro das vendas;

## ●
## Estoque: Módulo focado no controle dos produtos e seus estoques.


--------------------------------------------------

**# Criando uma aplicação**

Uma vez dentro do diretório do projeto **mini_curso_django**, execute:
**$ django-admin startapp atendimento**
**$ tree**
.
├── atendimento
│   ├── __init__.py
│   ├── admin.py       <<<   Local aonde ﬁcam as deﬁnições de admin sobre cada modelo.
│   ├── apps.py       <<<   Local aonde ﬁca a classe de conﬁguração da aplicação.
│   ├── migrations       <<<   Aqui ﬁcam todas os "scripts" acerca do banco de dados da aplicação.
│   │   └── __init__.py
│   ├── models.py       <<<   Local aonde ﬁcam as classes do modelo.
│   ├── tests.py
│   └── views.py       <<<   Aqui ﬁca os métodos do controle da aplicação.
├── db.sqlite3       <<<   Banco de dados do projeto, utilizando, no caso, SQLite.
├── manage.py
└── mini_curso_django       <<<   Diretório com as conﬁgurações do projeto.

├── ...


--------------------------------------------------

**# Criando uma aplicação**

Uma vez criada a aplicação, se faz necessário informar ao Django que esta aplicação existe e que ela vai ser 
"plugada" ao projeto. 

**mini_curso_django/mini_curso_django/settings.py**


--------------------------------------------------

**# Criando e entendendo uma view**

Como já dissemos anteriormente, a camada **view** do Django (modelo MVT) equivale a camada **controller** do 

modelo MVC.  Abaixo segue exemplos de duas views bem simples:

**mini_curso_django/atendimento/views.py**


--------------------------------------------------

**# Criando e entendendo uma view**

Para que o Django saiba onde está o recurso solicitado na requisição, é preciso fazer o devido mapeamento da url.

**mini_curso_django/urls.py **
**mini_curso_django/atendimento/urls.py**


--------------------------------------------------

**# Let's view the view?**

**# $ python3 manage.py runserver 8000**


--------------------------------------------------

**# http://localhost:8000/atendimento/**


--------------------------------------------------

**# http://localhost:8000/atendimento/index2**


--------------------------------------------------

**# Fixando o funcionamento de uma view**

### ●
### Browser dispara a requisição (HttpRequest) para determinada url do servidor;

### ●
### A engine do Django faz o direcionamento para a view correta, de acordo com o urls.py do 

### projeto e da aplicação;

### ●
### A view é processada;

### ●
### A resposta (HttpResponse) é retornada. No nosso exemplo um retorno foi um texto simples 

### e outro retorno foi um html. 

### ●
### Uma view pode ou não estar associada a um template.


--------------------------------------------------

**# Todo mundo tranquilo? **

**# $ telnet myhead 8000**
# Trying 127.0.0.1…
# 6 x 9 = 54...
# Connected e entendendo....
# Escape character is '^]'.


--------------------------------------------------

**# Criando e entendendo uma template**

# No caso do Django (modelo MVT), a camada **# template**#  equivale a camada 

**# view**#  do modelo MVC. 

# Um template nada mais é que um arquivo texto (geralmente .html) que 

# possui variáveis e um conjunto de # template tags#  que podem ser usadas.


--------------------------------------------------

**# Criando e entendendo uma template**

**# Variáveis:**

# {{ current_date  }}

# {{ idade }}

**# Template Tags:**

# {% if  %}


--------------------------------------------------

**# Criando e entendendo uma template**

**mini_curso_django/atendimento/views.py**


--------------------------------------------------

**# Criando e entendendo uma template**

**mini_curso_django/atendimento/views.py**


--------------------------------------------------

**# Criando e entendendo uma template**

**mini_curso_django/atendimento/urls.py**


--------------------------------------------------

**# Criando e entendendo uma template**

**mini_curso_django/atendimento/templates/atendimento/index4.html**


--------------------------------------------------

**# View + Template… **
**# "Juntos e shallow now..."**

**# $ python3 manage.py runserver 8000**


--------------------------------------------------

**# http://localhost:8000/atendimento/index3**


--------------------------------------------------

**# http://localhost:8000/atendimento/index4a**


--------------------------------------------------

**# http://localhost:8000/atendimento/index4b/?**


--------------------------------------------------

**# Fixando o funcionamento de uma template**

### ●
### Browser dispara a requisição (HttpRequest) para determinada url do servidor;

### ●
### A engine do Django faz o direcionamento para a view correta, de acordo com o urls.py do 

### projeto e da aplicação;

### ●
### Inicia-se o processamento da view.

### ●
### Durante o processamento da view, o template que será utilizado é identiﬁcado, um conjunto 

### de variáveis é fornecido, ele é processado e retorna um html.

### ●
### A resposta (HttpResponse) é retornada. No caso é html gerado via template.


--------------------------------------------------

**# Fixando o funcionamento de uma template**

### ●
### Os templates podem ser ### criados em tempo de execução (não recomendado)###  ou ### carregados a 

### partir de arquivos (recomendado)### .

### ●
### Além de podermos criar templates, o Django nos permite sobrescrever os templates de 

### outras aplicações, como por exemplo os do "Django Admin" (django.contrib.admin) que 

### veremos mais à frente.


--------------------------------------------------

**# Mas e aí major? Entendi bem o **
**# conceito da view, do template, **
**# mas…**

**# Cadê o meu sistema, rodando, de **
**# maneira simples é ágil?**


--------------------------------------------------

**# Calma aí "dezanos"! Ainda falta a **
**# camada dos modelos. Rapadura é doce **
**# mas né mole não!**


--------------------------------------------------

**# Criando e entendendo um model**

# No caso do Django (modelo MVT), a camada **# model**#  equivale a camada 

**# model**#  do modelo MVC.  *# Essa foi fácil hein?*

# É nessa camada que iremos deﬁnir todas as classes do domínio do negócio 

# da aplicação.


--------------------------------------------------

**# Criando e entendendo um model**

**mini_curso_django/atendimento/models.py**


--------------------------------------------------

**# Criando e entendendo um model**

### Uma vez deﬁnido o model, precisamos criar o "script" que cria a tabela do banco de dados que irá 

### armazenar suas informações. Para isso basta executar:

**### $ python3 manage.py makemigrations atendimento**

### Uma vez executado o comando acima,  o Django vai detectar as mudanças realizadas no *### models.py*###  

### da aplicação e gerar o devido "script" (migration).  A ORM do Django se encarregará de traduzir 

### esses scripts em SQLs, de acordo com o banco utilizado. Ex: SQLite, PostgreSql, MySql, Microsoft 

### Sql Server, Oracle.


--------------------------------------------------

**# Criando e entendendo um model**


--------------------------------------------------

**# Criando e entendendo um model**

### Para ver o SQL que será executado, quando a migration for aplicada, use o comando:

**### $ python3 manage.py sqlmigrate atendimento 0001**

*### Sintaxe:  $ python3 manage.py sqlmigrate [aplicacao] [número ou nome da migration]*

### Para aplicar as alterações no banco, execute:

**### $ python3 manage.py migrate**

### Pronto, a partir de agora temos o nosso modelo pronto para ser usado!


--------------------------------------------------

**# Cadastrando um cliente via terminal**

### Agora que o *### model*###  Cliente está pronto, vamos fazer o nosso primeiro cadastro, via terminal, já 

### utilizando um pouco do poderio da ORM  do Django.

### Obs: Para entender mais sobre a ORM do Django, como fazer consultas, inserts, updates, deletes 

### etc, procure  sobre *### Querysets*### :

### https://docs.djangoproject.com/en/2.2/topics/db/queries/

### https://docs.djangoproject.com/en/2.2/ref/models/querysets/

### https://docs.djangoproject.com/en/2.2/ref/models/lookups/


--------------------------------------------------

**# Cadastrando um cliente via terminal**

**### $ python3 manage.py shell**

### Python 3.7.3 (default, Mar 27 2019, 09:23:39)

### [Clang 10.0.0 (clang-1000.11.45.5)] on darwin

### Type "help", "copyright", "credits" or "license" for more information.

### (InteractiveConsole)

### >>> from atendimento.models import Cliente

### >>> Cliente.objects.all()

### <QuerySet []>


--------------------------------------------------

**# Cadastrando um cliente via terminal**

**### …**

### >>> c = Cliente(nome='Jhon Rambo', estado_civil='SOLTEIRO', cpf='871.536.330-90')

### >>> type(c)

### <class 'atendimento.models.Cliente'>

### >>> c.id

### (Não retorna nada pois o objeto ainda não foi persistido)


--------------------------------------------------

**# Cadastrando um cliente via terminal**

**### …**

### >>> c.save()

### >>> c.id

### 1

### >>> Cliente.objects.all()

### <QuerySet [<Cliente: Jhon Rambo>]>


--------------------------------------------------

**# Cadastrando um cliente via terminal**

# Depois de executado o método "save()", o objeto cliente foi persistindo no 

# banco de dados:


--------------------------------------------------

**# Major, cadê o sistema? "Avie homi" **
**# que eu tô com fome e ainda vou **
**# pegar o "buzão"...**


--------------------------------------------------

**# Deixe de aperreio "dezanos"! Se **
**# aquete que vou te mostrar agora!**


--------------------------------------------------

**# Django Admin**

### Trata-se de uma aplicação web (site) através do qual será possível gerenciar os seus modelos. Esta 

### aplicação, associada a outras, também oferecidas pelo Django, irão disponibilizar a você:

### ●
### Um site administrativo (django.contrib.admin);

### ●
### Um sistema de autenticação (django.contrib.auth);

### ●
### Um framework para tipos de conteúdo (django.contrib.contenttypes);

### ●
### Um framework de sessão (django.contrib.sessions);

### ●
### Um framework de envio de mensagem (django.contrib.messages);

### ●
### Um framework para gerenciamento de arquivos estáticos (django.contrib.staticﬁles).


--------------------------------------------------

**# Django Admin**

Por padrão ele já vem plugado, ou seja, já está deﬁnido em settings.INSTALLED_APPS, logo para poder utilizá-lo basta criar 

um superusuário (administrador geral do projeto):

**$ python3 manage.py createsuperuser**

Username (leave blank to use 'so_username'): admin

Email address:

Password: senha

Password (again): senha

This password is too short. It must contain at least 8 characters.

This password is too common.

Bypass password validation and create user anyway? [y/N]: y


--------------------------------------------------

**# Run as administrator...**

**# $ python3 manage.py runserver 8000**


--------------------------------------------------

**# http://localhost:8000/admin/**


--------------------------------------------------

**# http://localhost:8000/admin/**


--------------------------------------------------

**# http://localhost:8000/admin/auth/user/**


--------------------------------------------------

**# http://localhost:8000/admin/auth/user/1/change/**


--------------------------------------------------

**# Django Admin**

### De cara, ganhamos uma autenticação via banco. Caso queira, outros tipos de autenticação podem 

### ser realizadas, com por exemplo via LDAP (Active Directory, OpenLDAP, Apache Directory 

### Server...) ou integrado com outras aplicações, como por exemplo o "social login" (Facebook, 

### Instagram, Twitter, Github, Linkedin...).

### Quanto à autorização, ou seja, o que o usuário poderá fazer em cada aplicação, o Django  Admin 

### oferece um controle de grupos e usuários muito bom e fácil de utilizar. Além das permissões 

### padrão de cada modelo (add, change, delete e view), é possível criar permissões personalizadas 

### (Ex: usuario_pode_extornar_cobranca).


--------------------------------------------------

**# Gerenciando um model no "Django Admin"**

Para que possamos utilizar o Django Admin para gerenciar os nossos models, precisamos primeiro informar a ele 

que models queremos que ele gerencie. Para isso, basta registrar o respectivo model junto ao Django Admin.

**mini_curso_django/atendimento/admin.py**


--------------------------------------------------

**# http://localhost:8000/admin/**


--------------------------------------------------

**# http://localhost:8000/admin/atendimento/cliente/**


--------------------------------------------------

**# http://localhost:8000/admin/atendimento/cliente/1/change/**


--------------------------------------------------

**# http://localhost:8000/admin/atendimento/cliente/add/**


--------------------------------------------------

**# Ah major! Agora sim, eu vi vantagem! **

**# Mas major, e se eu quiser fazer alguma **
**# customização, eu posso?**


--------------------------------------------------

**# "Oxe", é claro "dezanos"! Espia aí...**


--------------------------------------------------

**# Gerenciando um model no "Django Admin"**

### Com o Django Admin é possível realizar diversos níveis de customização, desde de alterar a disposição 

### das informações, deﬁnir o que deve ou não ser exibido, ﬁltros, quais campos devem ser utilizados na 

### busca, até a nível de apresentação do site (html, css).

### A seguir vamos apresentar o primeiro nível de customização, realizado através de uma simples classe que 

### herda de *### admin.ModelAdmin*### .

### Para ver mais mais opções de customização via *### admin.ModelAdmin*### , acesse:

### https://docs.djangoproject.com/en/2.2/intro/tutorial07/


--------------------------------------------------

**# Gerenciando um model no "Django Admin"**

**mini_curso_django/atendimento/admin.py**


--------------------------------------------------

**# http://localhost:8000/admin/atendimento/cliente/**


--------------------------------------------------

**# http://localhost:8000/admin/atendimento/cliente/1/change/**


--------------------------------------------------

**# Gerenciando um model no "Django Admin"**

### Além das validações básicas, como campos obrigatórios, únicos, é possível também realizar 

### validações customizadas. Abaixo temos um exemplo disso:

**Classe Cliente - mini_curso_django/atendimento/models.py**


--------------------------------------------------

**# http://localhost:8000/admin/atendimento/cliente/2/change/**


--------------------------------------------------

**# http://localhost:8000/admin/atendimento/cliente/2/change/**


--------------------------------------------------

### A seguir segue um exemplo de customização a nível de templates. No caso vamos personalizar a 

### tela de login do Django Admin. Para isso, basta:

### ●
### Deﬁnir uma pasta para armazenar os templates do Django Admin que serão sobrescritos.

### ○
### Ex: mini_curso_django/templates/admin/

### ●
### Criar a devida entrada na conﬁguração  settings.TEMPLATES ('DIRS'):

**# Customizando templates do "Django Admin"**


--------------------------------------------------

**# Customizando templates do "Django Admin"**

### ●
### Descobrir onde está instalado o Django, para poder realizar uma cópia dos templates que serão 

### sobrescritos:

### ○
### $ python -c "import django; print(django.__path__)"

### ■
### Ex: ['/Users/misael/.../python3.7/site-packages/django']

### ○
### Arquivos copiados:

### ■
### .../python3.7/site-packages/django/contrib/admin/templates/admin/base_site.html

### ■
### .../python3.7/site-packages/django/contrib/admin/templates/admin/login.html

### https://docs.djangoproject.com/en/2.2/intro/tutorial07/#customize-the-admin-look-and-feel


--------------------------------------------------

**# Customizando templates do "Django Admin"**


--------------------------------------------------

**# http://localhost:8000/admin/**


--------------------------------------------------

**# Phuderoso major! Mermão dá pra fazer **
**# "misera" com esse Django...**


--------------------------------------------------

**# Dá sim "dezanos"! E olhe que tem coisa **
**# que eu ainda que nem te mostrei! **


--------------------------------------------------

**# Outros recursos interessantes do Django**

O foco desta apresentação foi passar o essencial acerca dos pilares do Django. Devido ao tempo escasso, vários 

recursos muito interessantes não puderam abordados, mas merecem ser vistos em casa e acreditamos que serão 

alvo de futuras apresentações.  Recomendamos que dêem uma estudada sobre:

●
Forms;

●
ModelForms;

●
Class Based Views;

●
Managers;

A página abaixo trata desses itens e muito mais:

https://docs.djangoproject.com/en/2.2/


--------------------------------------------------

**# Código fonte do Mini Curso Django**

●
Disponível em:

○
https://github.com/misaelbarreto/mini_curso_django

●
Nele você vai encontrar o projeto completo, ou seja, com as três aplicações criadas e rodando.


--------------------------------------------------

**# OBRIGADO!**

**# :-)**

