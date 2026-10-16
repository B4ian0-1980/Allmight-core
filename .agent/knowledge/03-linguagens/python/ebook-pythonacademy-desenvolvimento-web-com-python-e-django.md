---json
{
  "id": "ebook-pythonacademy-desenvolvimento-web-com-python-e-django",
  "title": "EBOOK-PythonAcademy-Desenvolvimento-Web-com-Python-e-Django",
  "categoria": "03-linguagens",
  "subcategoria": "python",
  "resumo": "**Arquivo Original:** `EBOOK-PythonAcademy-Desenvolvimento-Web-com-Python-e-Django.pdf` **Data Conversão:** 1770993301.7615688",
  "gatilhos": [
    "com",
    "desenvolvimento",
    "django",
    "ebook",
    "ebook-pythonacademy-desenvolvimento-web-com-python-e-django",
    "linguagens",
    "python",
    "pythonacademy"
  ],
  "perguntas_tipo": [
    "Como utilizar EBOOK-PythonAcademy-Desenvolvimento-Web-com-Python-e-Django?",
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

# EBOOK-PythonAcademy-Desenvolvimento-Web-com-Python-e-Django

> **Arquivo Original:** `EBOOK-PythonAcademy-Desenvolvimento-Web-com-Python-e-Django.pdf`
> **Data Conversão:** 1770993301.7615688

---


## Página 2

E B O O K
DESENVOLVIMENTO WEBCOM PYTHON E DJANGO


## Página 4

SUMÁRIO
CAPÍTULO 1: INTRODUÇÃO 4FLUXO DE UMA REQUISIÇÃO 6
CAPÍTULO 2: INSTALAÇÃO 8HELLO WORLD, DJANGO! 9
CAPÍTULO 3: CAMADA MODEL 15ONDE ESTAMOS… 15CAMADA MODEL 16DB BROWSER FOR SQLITE 22API DE ACESSO A DADOS 23
CAPÍTULO 4: CAMADA VIEW 27ONDE ESTAMOS… 27CAMADA VIEW 28FUNÇÕES vs CLASS BASED VIEWS 30CLASS BASED VIEWS 31FUNÇÕES (FUNCTION BASED VIEWS) 33DEBUGANDO UMA REQUISIÇÃO NO PYCHARM 34AS PRINCIPAIS CLASS BASED VIEWS 36FORMS NO DJANGO 42MIDDLEWARES 48
CAPÍTULO 5: CAMADA TEMPLATE 53ONDE ESTAMOS… 54DEFINIÇÃO DE TEMPLATE 55CONFIGURAÇÃO 57DJANGO TEMPLATE LANGUAGE (DTL) 57CONSTRUINDO A BASE DO TEMPLATE 58TAGS E FILTROS CUSTOMIZADOS 72FILTROS DO DJANGO 79

## Página 5

C A P Í T U L O   1
INTRODUÇÃO
Django é um framework web de alto nível, escrito em Python queencoraja o desenvolvimento limpo de aplicações web.
E antes de mergulharmos no Django, vamos entender primeiro sobre oDesenvolvimentoWeb! NonichodeDesenvolvimentoWeb, oPythonistatemcomo objetivo o desenvolvimento de páginas Web, plataformas ou qualqueroutraaplicaçãoquesejaexecutadaemumnavegador-comooGoogleChromee o Firefox - com conexão à internet.
DentrodoDesenvolvimentoWebexistem2áreasprincipais: oFrontende o Backend. ODiagrama abaixo exempliﬁca como os dois interageme emseguida explicamos cada um deles:
Diagrama Frontend x Backend


## Página 6

● O Frontend é constituído por tudo aquilo que o Usuário ﬁnal vê einterage e é composto, basicamente, das páginas webque esseUsuárioterá acesso. Algumas tecnologias geralmente utilizadas são: React,Angular, HTML, CSS e Javascript.● Já o Backend, também chamado de Servidor, tem as seguintesresponsabilidades: processa as requisições enviadas pelo Frontend,mantémas RegrasdeNegóciodosistemaegerenciaoacessoaoBancode Dados. É aqui que o Python está presente!
Existem bibliotecas que auxiliam (e muito) no desenvolvimento deaplicações web: os chamados frameworks! Umframeworkéumconjuntodeferramentas, técnicas e convenções para facilitar odesenvolvimentodealgumtipo especíﬁco de aplicação. Sendo assim, temosdiversostiposdeframeworksdiferentes, por exemplo:
● TemosFrameworksFrontend, quefacilitamacriaçãodeaplicaçõeswebque são executadas nos navegadores dos usuários de um sistema.Exemplos: React, Angular, Vue.js.● Temos Frameworks Mobile, que facilitam o desenvolvimento deaplicações mobile. Exemplo: Ionic e React Native.● TemosFrameworksWeb, quefacilitamodesenvolvimentodeaplicaçõesweb, abstraindodetalhesdebaixonível (comoprotocolosderede, acessoà banco de dados, tratamento de requisições HTTP). Exemplos: Ruby onRails (Ruby), Spring (Java), Express (Node.js).
E agora, voltando para o nosso querido Django… Desenvolvido porexperientes desenvolvedores, Django toma conta da parte pesada dodesenvolvimento web, como tratamento de requisições, mapeamentoobjeto-relacional, preparação de respostas HTTP, para que, dessa forma, vocêgaste seu esforço comaquilo que realmente interessa: as regras de negócioda sua aplicação!
Elefoidesenvolvidocomumapreocupaçãoextraemsegurança, evitandoos mais comuns tipos de ataques web, como Cross Site Scripting(XSS), CrossSite Request Forgery(CSRF), SQL injection, entreoutros.
É bastante escalável: Django foi desenvolvido para tirar vantagemdamaior quantidade de hardware possível (desde que você queira). Django usa

## Página 7

uma arquitetura “zero-compartilhamento”, o que signiﬁca que você podeadicionar mais recursos em qualquer nível: servidores de banco de dados,cache e/ou servidores de aplicação.
É utilizado por grandes empresas ao redor do mundo:
E, para que você possa dominar esse framework como um todo,utilizaremos uma abordagem bottom-up (de baixo paracima), isto é:
1. Primeiro, vamos começar do começo, instalando o Django!2. Depoisabordaremosa CamadadeModelos, queéondeﬁcacentralizadoo acesso ao Banco de Dados e a modelagemdas entidade da nossaaplicação - que chamamos deModelos.3. Emseguida veremos a Camada de Views, que é onde implementamosas regras de negócio da nossa aplicação.4. Por ﬁm, veremos a Camada de Templates, que é a parte do frameworkresponsável por renderizar páginas web, onde utilizaremos HTML, CSS,Javascript e a biblioteca de componentes Bootstrap.
Comodisseanteriormente, oDjangoéum framework paraconstruçãodeaplicações webemPython. Alémdisso, ele é estruturado emcamadas, sendochamado de um Framework MTV - isto é: Model-Template-View - que sãoexatamente as camadas que veremos a seguir.
Eparaentender comooDjangofunciona, vamosfazerumRaio-XdeumaRequisição, desde o navegador do usuário até o servidor que vai processá-la.
FLUXO DE UMA REQUISIÇÃO


## Página 8

Para ajudar melhor, vamos analisar o ﬂuxo de uma requisiçãosaindodonavegador do usuário, passando para o servidor onde o Django está sendoexecutado, retornando novamente ao navegador.
ODjangoédivididoemtrêscamadas: aCamadadeModelos, aCamadade Views e a Camada de Templates. Veremos cada uma nos Capítulosseguintes. MasagoravamosdarosprimeirospassoscomoDjango, começandopela suainstalação! Então ajeita sua cadeira, preparao café evamos nessa!


## Página 9

C A P Í T U L O   2
INSTALAÇÃO
Primeiro, precisamosnoscertiﬁcar queoPythoneoPIP(gerenciadordepacotes do Python) estão instalados corretamente.
Vá no seu terminal ou prompt de comando e digite o comando python--version. Deveser abertooterminalinterativodoPython(sealgocomo bash:command not found aparecer, é por que sua instalaçãonão está correta).
Agora, digite pip--version. A saída desse comando deve ser a versãoinstalada do pip. Se ele não estiver disponível, faça o downloaddo instaladornesse link e execute o código.
Vamos executar esse projeto em um ambiente virtual utilizando ovirtualenvparaqueasdependênciasnãoatrapalhemasquejáestãoinstaladasno seu computador (para saber mais sobre ovirtualenv, leiaesse post aquisobre desenvolvimento em ambientes virtuais).
Após criarmos nosso ambiente virtual, instalamos o Django com:
pip install django
Para saber se a instalação está correta, podemos abrir o terminalinterativo do Python (digitando python no seu terminal ou prompt decomandos) e executar:
importdjango
print(django.get_version())
A saída deve ser a versão do Django que acabou de ser instalada.

## Página 10

HELLO WORLD, DJANGO!
Comtudo instalado corretamente, vamos agora fazer umprojeto paraque você veja o Django em ação!
Nosso projetoéfazer umsistemadegerenciamentodeFuncionários. Ouseja, vamosfazer umaaplicaçãoondeserápossível adicionar, listar, atualizaredeletarFuncionários.
Vamos começar criando a estrutura de diretórios e arquivos principaispara o funcionamento do Django. Para isso, o pessoal do Django fez umcomando muito bacana para nós: o django-admin.py.
Se sua instalação estiver correta, esse comando já foi adicionado ao seuPATH!
Tente digitar django-admin--version no seu terminal (se não estiverdisponível, tentedjango-admin.py --version).
Digitando apenas django-admin, é esperado que aparece a lista decomandos disponíveis, similar a:
Available subcommands:
[django]checkcompilemessagescreatecachetabledbshelldiffsettingsdumpdataflushinspectdbloaddatamakemessagesmakemigrationsmigraterunserversendtestemailshellshowmigrationssqlflushsqlmigratesqlsequenceresetsquashmigrationsstartappstartprojecttesttestserver

## Página 11

Por ora, estamos interessados no comando startproject que cria umnovo projeto com a estrutura de diretórios certinha para começarmos adesenvolver!
Executamos esse comando da seguinte forma:
django-admin.pystartproject helloworld
Criando a seguinte estrutura de diretórios:
/helloworld- __init__.py- asgi.py- settings.py- urls.py- wsgi.py- manage.py
Explicando cada arquivo:
● helloworld/asgi.py: Aqui conﬁguramos a interface entre o servidor deaplicaçãoenossaaplicaçãoDjango, comcapacidadesassíncronas(nãosepreocupem com isso por enquanto), através do padrão ASGI.● helloworld/settings.py: Arquivo muito importante comasconﬁguraçõesdo nosso projeto, como conﬁgurações do banco de dados, aplicativosinstalados, conﬁguração de arquivos estáticos e muito mais.● helloworld/urls.py: Arquivodeconﬁguraçãoderotas(ouURLConf). Éneleque conﬁguramosquem responde a qual URL.● helloworld/wsgi.py: Aqui conﬁguramos a interface entre o servidor deaplicação e nossa aplicação Django, através do padrão WSGI● manage.py: Arquivo gerado automaticamente pelo Django que expõecomandos importantes para manutenção da nossa aplicação.
Para testar, vá para a pasta raíz do projeto e execute o comando pythonmanage.py runserver.
Depois, acesse seu browser no endereço http://localhost:8000.
A seguinte tela deve ser mostrada:

## Página 12

Se ela aparecer, nossa conﬁguração está correta e estamosprontosparacomeçarmos a desenvolver nossa aplicação!
Agora, vamoscriarum app chamado website parasepararmososarquivosde conﬁguração da nossa aplicação, que vão ﬁcar na pasta /helloworld, dosarquivos relacionados ao website.
De acordo com a documentação, um app no Django é:
UmaaplicaçãoWebquefaz algumacoisa, porexemplo-umblog,umbancodedadosderegistrospúblicosouumaplicativodepesquisa.Jáumprojetoéumacoleção de configurações e apps para um website em particular.
Um projeto pode ter vários apps e um app pode estar presente emdiversos projetos.
A ﬁm de criar um novo app, o Django provê outro comando,chamado django-admin.py startapp.
Ele nos ajuda a criar os arquivos e diretórios necessários para tal objetivo.


## Página 13

Na raíz do projeto, execute:
django-admin.py startapp website
Agora, vamos criar algumas pastas para organizar a estrutura da nossaaplicação. Primeiro, crie a pastatemplatesdentro dewebsite. Dentrodela, crieuma pastawebsitee dentro dela, uma pasta chamada_layouts.
Crie tambéma pastastaticdentrodewebsite, paraguardar osarquivosestáticos (arquivos CSS, Javascript, imagens, fontes, etc). Dentro dela crieumapastawebsite(isto é feito por questões de convenção do próprio framework).Também dentro destatic, crie: uma pastacss, umapastaimge uma pasta js.
Assim, sua estrutura de diretórios deve estar similar a:
Observação: Nós criamos umapastacomo nome do app(website, nocaso) dentro das pastas static e templates para que o Django crie onamespace do app. Dessaforma, oDjangoentendeondebuscar osrecursosquando você precisar!
Para que o Django enxergue esse app que acabamos de criar, énecessário adicioná-lo à lista de appsinstalados do Django. Fazemos issoatualizando a conﬁguração INSTALLED_APPSno arquivo de conﬁguraçãohelloworld/settings.py


## Página 14

Ela é uma lista e diz ao Django o conjunto de apps que devem sergerenciados no nosso projeto.
Énecessário adicionar osappsda nossa aplicaçãoàessalistaparaqueoDjango as enxergue. Para isso, procure por:
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',]
E adicione website e helloworld, ﬁcando assim:
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','helloworld','website']
Agora, vamos fazer algumas alterações na estrutura do projeto paraorganizarecentralizaralgumasconﬁgurações. Essaéumaconﬁguraçãopessoalque eusempre faço nos projetos que desenvolvo e que facilita a vidaquandodesenvolvemos utilizando Django.
1. Primeiro, vamos passar o arquivo de modelos models.py de /websitepara /helloworld, pois os arquivos comuns ao projeto vão ﬁcarcentralizados no app helloworld (geralmente para projetos menores emedianos temos apenas umarquivomodels.py para o projeto todo. Aseparação do arquivo de modelos geralmente só ocorre em projetosgrandes).2. Comonãotemosmaisoarquivodemodelosnapasta/website, podemos,então, excluir a pasta /migrations e o migrations.py, pois estes serãogerados e gerenciados pelo app helloworld.3. Crie um arquivo de rotas urls.py em /website. Vamos alterá-loposteriormente.
Por ﬁm, você deve estar com a estrutura de diretórios da seguinte forma:

## Página 15

CONCLUSÃO DO CAPÍTULO
Neste capítulo, vimos um pouco sobre o Django, suas principaiscaracterísticas, sua estrutura de diretórios e como começar a desenvolverutilizando-o!
Vimos as facilidades que o comando django-admintrazem e comoutilizá-lo para criar nosso projeto.
Tambémo utilizamos para criarapps, que são estruturas modulares donosso projeto, usados para organizar e separar funções especíﬁcas da nossaaplicação.
Nopróximocapítulo, vamosfalar sobreaCamada Model doDjango, queé onde residemas entidades do nosso sistema e toda a lógica de acesso adados!


## Página 16

C A P Í T U L O   3
CAMADAMODEL
A Camada de Modelos temuma função essencial na arquitetura dasaplicações desenvolvidas com o Django.
É nela que descrevemos os campos e comportamentos das entidadesque irão compor nosso sistema e que serão traduzidas emTabelas do nossoBanco de Dados.
Também é nela que reside a lógica de acesso aos dados da nossaaplicação. Neste capítulo, você verá como o Django facilita nossa vida aomanipular os dados do nosso sistema através da poderosa API de Acesso aDados.
Mas primeiro, vamos nos situar!
ONDE ESTAMOS…
No primeiro capítulo, tratamos de conceitosintrodutóriosdoframework,uma visão geral da sua arquitetura
Já no segundo capítulo, ﬁzemos a instalação do Django e a criação dofamoso Hello World emDjango.
Agora, vamos tratar da primeira camada do Dango, aCamada Model!

## Página 17

Vamos mergulhar um pouco mais e conhecer a camada Model daarquitetura MTV do Django (Model-Template-View).
Nela, vamos descrever, em forma de classes, as entidades do nossosistema, para que o resto (Template e View) façamsentido.
CAMADA MODEL
Vamos começar pelo básico: pela deﬁnição de modelo!
Um modelo- tambémchamadodeentidadedosistema- éadescriçãodo dado que será gerenciado pela sua aplicação.


## Página 18

Ele contémos campos e comportamentos desses dados. No ﬁm, cadamodelovai ser transformadoemumatabelanobancodedados: processoqueé feito pelo próprio Django, portanto não se preocupe!
No Django, um modelo tem basicamente duas características:
● É uma classe que herda de django.db.models.Model● Cada atributo representa um campo da tabela
Com isso, o Django gera automaticamente uma API (ApplicationProgramming Interface) de Acesso a Dados. Essa API foi desenhada parafacilitar e muito nossa vida quando formos gerenciar (adicionar, excluir eatualizar) os dados da nossa aplicação.
Para entendermos melhor, vamos modelar a principal entidade dosistema que vamos desenvolver: a entidadeFuncionário!
Vamos supor que sua empresa está desenvolvendo um sistema degerenciamento dos funcionários e lhe foi dada a tarefa de modelar edesenvolver o acesso aos dados da entidade Funcionário.
Pensando calmamente emsua estação de trabalho enquanto seuchefelhecobradiversasmetasedizendoqueodeadlinedoprojetofoiadiantadoemduas semanas você pensa nos seguintes atributos para tal classe:
●
Nome
●
Sobrenome
●
CPF
●
Tempo de serviço
●
Remuneração
Agora, é necessário traduzir isso para código Pythonpara que o Djangopossa entender.
No Django, os modelos são descritos no arquivo models.py.
Ele já foi criado no Capítulo anterior e está presente na pastahelloworld/models.py.
Nele, nós iremos descrever cada atributo (nome, sobrenome, CPF e etc)como um campo (ouField) da nossa classe de Modelo.
Vamos chamar essa classe deFuncionário.

## Página 19

Seguindo as duas características que apresentamos anteriormente(herdar da classeModelemapear osatributosdaentidadeatravésdecampos),podemos descrever nosso modelo da seguinte forma:
fromdjango.dbimportmodels
classFuncionario(models.Model):nome=models.CharField(max_length=255,null=False,blank=False)
sobrenome=models.CharField(max_length=255,null=False,blank=False)
cpf=models.CharField(max_length=14,null=False,blank=False)
tempo_de_servico=models.IntegerField(default=0,null=False,blank=False)
remuneracao=models.DecimalField(max_digits=8,decimal_places=2,null=False,blank=False)
objetos=models.Manager()
E agora vamos à explicação deste modelo:
●
Cada campo tem umtipo.
●
O tipo CharField representa uma string.
●
O tipo PositiveIntegerField representa um número inteiropositivo.
●
O tipo DecimalField representa umnúmero decimal comprecisão ﬁxa(geralmente utilizamos para representarvalores monetários).
●
Cada tipo tem um conjunto de propriedades, como: max_lengthparadelimitar ocomprimentomáximodastring;decimal_placesparadeﬁnironúmerodecasasdecimais; entreoutras(adocumentaçãodecadacampoe propriedade pode ser acessada aqui).

## Página 20

●
Ocampo objetos= models.Manager() éutilizadoparafazeroperaçõesdebusca e será explicado em seguida!
●
Observação: não precisamos conﬁgurar o identiﬁcador id - ele éherdado automaticamente ao herdade dedjango.db.models.Model!
Toda vez que alteramos os modelos da nossa aplicação Django énecessário gerar umaMigraçãoquevai atualizar astabelasdonossobancodedados.
Nós fazemos isso através de dois comandos muito importantes que oDjango traz para nós através do script manage.py: o comandomakemigrations e o comando migrate.
O COMANDOmakemigrations
O comando makemigrationsanalisa se foram feitas mudanças nosmodelos e, emcaso positivo, cria novas migrações (Migrations) para alterar aestrutura do seu banco de dados, reﬂetindo as alterações feitas.
Vamos entender o que eu acabei de dizer: toda vez que você fazuma alteração emseu modelo, é necessário que ela seja aplicada a estruturade tabelas do banco de dados.
A esse processo é dado o nome de Migração! De acordo com adocumentação do Django:
Migraçãoé a formadoDjangode propagarasalteraçõesfeitasemseumodelo(adiçãode umnovocampo,deleçãode ummodelo,etc … ) ao seuesquemadobancodedados.Elasforamdesenvolvidasparaserem(namaioriadasvezes)automáticas, mascabeavocêsaberahoradefazê-las,executá-lase resolver os problemas comuns que possam vir a acontecer.
Portanto, toda vez que você alterar um arquivo de modelo, não seesqueça de executar python manage.py makemigrations!
Ao executar esse comando, devemos ter a seguinte saída:
python manage.py makemigrations
Migrations for 'helloworld':helloworld\migrations\0001_initial.py- Create model Funcionario

## Página 21

Observação: Ao executar pela primeira vez, talvez seja necessárioexecutar o comando referenciando o app onde os modelos estão deﬁnidos,dessa forma: pythonmanage.pymakemigrationshelloworld. Depois disso,apenas python manage.py makemigrations deve bastar!
Agora, perceba que foi criado umdiretório chamadomigrationsdentroda pastahelloworld.
Nele, você podever umarquivochamado0001_initial.py: elecontémaMigrationque possibilita a criação do modelFuncionario nobanco de dados!
O COMANDOmigrate
Quandoexecutamoso makemigrations, oDjangocriaobancodedadoseas migrations, masnãoasexecuta, istoé: nãoaplicarealmenteasalteraçõesnobanco de dados.
Para que o Django aplique essa Migrações, são necessárias três coisas,basicamente:
1. Queaconﬁguraçãodainterfacecomobancodedadosestejadescritanoarquivosettings.py2. Que os Modelos e Migrações estejam deﬁnidos para esse projeto.3. Execução do comandomigrate
Se você criouoprojetocomdjango-admin.pycreateprojecthelloworld,a conﬁguração padrão foi aplicada. Procure pela conﬁguraçãoDATABASESnosettings.py.
Ela deve ser a seguinte:
DATABASES={'default': {'ENGINE':'django.db.backends.sqlite3','NAME': BASE_DIR /'db.sqlite3',}}
Por padrão, oDjangoutilizaumbancodedadoslevechamado SQLite. Jájá vamos falar mais sobre ele.

## Página 22

Sobre os modelos e migrations, eles já foram feitos com a deﬁniçãodo Funcionário no arquivo models.py e com a execução do comandomakemigrations.
Agora só falta executar o comando migrate, para realmente alterar aestrutura do Banco de Dados!
Para isso, vamos para a raíz do projeto (onde está o script manage.py) eexecutamos: python manage.py migrate. A saída deveser:
$ python manage.py migrate
Operations to perform:Apply all migrations: admin, auth, contenttypes, helloworld, sessionsRunning migrations:Applying contenttypes.0001_initial... OKApplying auth.0001_initial... OKApplying admin.0001_initial... OKApplying admin.0002_logentry_remove_auto_add...Applying contenttypes.0002_remove_content_ty...Applying auth.0002_alter_permission_name_max...Applying auth.0003_alter_user_email_max_leng...Applying auth.0004_alter_user_username_opts...Applying auth.0005_alter_user_last_login_nul...Applying auth.0006_require_contenttypes_0002...Applying auth.0007_alter_validators_add_erro...Applying auth.0008_alter_user_username_max_l...Applying auth.0009_alter_user_last_name_max_...Applying helloworld.0001_initial... OKApplying sessions.0001_initial... OK
Calmalá... Havíamosdeﬁnidoapenas uma Migrationeforamaplicadas15!!! Por quê???
Selembraqueaconﬁguração INSTALLED_APPS continhaváriosapps (enãoapenas os nossos helloworld e website)?
Poisentão, cada appdessescontémseusprópriosmodelosemigrations.Por issoqueaoexecutar ocomandomigrateoDjangoaplicoutudoqueestavaaguardando ser aplicado. Sacou?!

## Página 23

Coma execução do comando migrate, o Django irá executar diversoscomandos SQL para criar a estrutura necessária para execução da nossaaplicação. UmadelaséatabelareferenteaonossomodeloFuncionário, similarà:
CREATETABLEhelloworld_funcionario ("id"serialNOTNULLPRIMARYKEY,"nome"varchar(255)NOTNULL,"sobrenome"varchar(255)NOTNULL,...);
EagoraveremoscomopodemosanalisarobancodedadosqueoDjangocriou de forma visual, através da aplicaçãoDB Browserfor SQLite!
DB BROWSER FOR SQLITE
Apresento-lhes uma ferramenta MUITO prática que nosauxiliaveriﬁcar aestrutura do nosso Banco de Dados: o DB Browser forSQLite!
Comele, podemos ver a estrutura do banco de dados, alterar dadosemtempo real, fazer queries (consultas), veriﬁcar se os dados foramefetivados nobanco emuito mais!
Cliqueaqui parafazero download einstalaçãodosoftware. Aoterminarainstalação, abra o DB Browser for SQLite. Você deveter a seguinte tela:


## Página 24

Aqui, podemos clicar em“Abrir banco de dados” eprocurar pelobancode dados do nosso projeto db.sqlite3(ele está naraíz do projeto).
Ao importar o banco de dados, teremos uma visão geral, mostrandoTabelas, Índices, ViewseTriggers.
Paraver osdadosdecadatabela, váparaaaba“Navegardados”, escolhanossa tabela helloworld_funcionario e…
Voilá! O que temos? NADA 
Calma jovem… Ainda não adicionamos nada! Já já vamos criar
as Views e Templates e popular esse BD! 
API DE ACESSO A DADOS
Com nossa classe Funcionário modelada e já instalada no Banco deDados, vamos agora ver a API de acesso à dados provida peloDjangoquevaifacilitarmuitoa nossa vida!
Vamos testar a adição de um novo funcionário utilizando o shell doDjango. Para isso, digite o comando:
python manage.py shell


## Página 25

Oshell do Django é muito útil para testar trechos de código semterque executar o servidor inteiro!
Para adicionar um novo funcionário, basta criar uma instância do seumodelo e chamar o método save() (não desenvolvemos esse método, maslembra que nosso modelo herdou de Models? Pois é, é de lá que ele veio).
Podemos fazer isso com o código abaixo (no shell doDjango):
fromhelloworld.modelsimportFuncionario
funcionario=Funcionario(nome='Marcos',sobrenome='da Silva',cpf='015.458.895-50',tempo_de_servico=5,remuneracao=10500.00)
funcionario.save()
E…. Pronto!
O Funcionário Marcos da Silva será salvo no seu banco!
NADA de código SQL e queries enormes!!! Tudo simples! Tudo limpo!
É importante ressaltar que antes da conclusão comsucesso do método.save(), oregistronãopossuiumidentiﬁcadorúnico(tambémchamadodeIDouPK- PrimaryKey). Apósachamadaaométodo .save()podemosvisualizaro ID do registro da seguinte forma:
print(funcionario.id)
# Saída deve ser: 1
A API de busca de dados é ainda mais completa! Nela, você constróisua query à nível de objeto!
Mas como assim?!
Por exemplo, parabuscar todososFuncionários, abraoshelldoDjangoedigite:
funcionarios=Funcionario.objetos.all()

## Página 26

Selembradotal Manager quefalamosláemcima?Então, um Manager éainterface na qual as operações de busca são deﬁnidas para o seu modelo.
Ouseja, através do campo objetos podemosfazer queriesincríveissemuma linha de SQL!
Exemplo de um query um pouco mais complexa:
Busquetodososfuncionáriosquetenham maisde3 anosdeserviço, queganhem menosdeR$5.000,00deremuneração eque nãotenham“Marcos”no nome.
Podemos atingir esse objetivo com:
funcionarios=Funcionario.objetos.exclude(nome="Marcos").filter(tempo_de_servico__gt=3).filter(remuneracao__lt=5000.00).all()
Ométodo exclude() retira linhas da pesquisa (no nosso caso, vai excluiros registros que contenham“Marcos” no nome) e filter() ﬁltra a busca, deacordo com os ﬁltros que passamos!
No exemplo, para ﬁltrar por maior que, adicionamos a string__gt(gt doinglês greater than. Emportuguês “maior que”) e __lt (lt do inglês less than.Em português, “menor que”) aos campos.
Ométodo .all() aoﬁnal da query servepararetornar todas aslinhasdobanco que cumpramosﬁltrosdanossabusca(tambémtemoso first() queretorna apenas o primeiro registro, o last(), que retorna o último, entreoutros).
Agora, vamos ver como é simples excluir um Funcionário:
# Primeiro, encontramos o Funcionário que desejamos deletarfuncionario=Funcionario.objetos.get(id=1)
# Agora, o deletamos!funcionario.delete()
Aqui temos um método novo, o.get()! Com ele, podemos passar oidentiﬁcador único do registro que queremos encontrar. Em seguida,podemos chamar o método .delete()para deletar umregistro dobancodedados!

## Página 27

Simples, né?!
A atualização de campos tambémé extremamente simples, bastandobuscar a instância desejada, alterar o campo e salvá-lo novamente!
Por exemplo: o funcionário de id = 13 se casou e alterou seu nome deMarcos da SilvaparaMarcos da Silva Albuquerque.
Podemos fazer essa alteração no banco de dados da seguinte forma:
# Primeiro, buscamos o funcionário desejadofuncionario=Funcionario.objetos.get(id=13)
# Alteramos seu sobrenomefuncionario.sobrenome=f"{funcionario.sobrenome}Albuquerque"
# Salvamos as alteraçõesfuncionario.save()
CONCLUSÃO DO CAPÍTULO
Com isso, concluímos a construção do modelo da nossa aplicação!
Criamos o banco de dados, vimos como visualizar os dados como DBBrowser for SQLite e como a API de acesso a dados do Django é simples epoderosa!
No próximo capítulo, vamos aprender sobre a Camada View e comoadicionamos lógica de negócio à nossa aplicação Django!

## Página 28

C A P Í T U L O   3
CAMADAVIEW
Neste capítulo vamos abordar a Camada Viewdo Django, que é ondedescrevemos as lógicas de negócio da nossa aplicação!
É nesta camada que vamos desenvolver os métodos que irão:
● Processaras Requisições HTTP que chegarem à nossaaplicação;● FormularRespostas HTTP; e● Enviá-lasde volta ao usuário.
Vamos aprender o conceito das poderosas Views doDjango, aprender adiferença entre Function Based Views (FBV) e Class Based Views (CBV),como utilizar os Forms do Django, aprender o que são Middlewares, comodesenvolvê-los e muito mais.
Então vamos nessa, que esse capítulo está repleto de código e muitoconteúdo!
Mas antes, você já sabe: vamos nos situar para saber onde estamos,dentro do ciclo de vida de uma Requisição HTTP dentro do Framework Django.
ONDE ESTAMOS…
Primeiramente, vamos nos situar:

## Página 29

CAMADA VIEW
A principal responsabilidade desta camada é a de processar asrequisições vindas dos usuários, formar uma resposta e enviá-la de volta aousuário. E é nesta camada que residem as lógicas de negócio da nossaaplicação.
Essa camada deve: recepcionar, processar e responder!


## Página 30

Na etapa de recepção das Requisições, um dos primeiros passos édeterminar qual trecho de código a processará, através do que chamamosderoteamento de URLs!
A partir da URL que o usuário quiser acessar (/funcionarios, porexemplo), oDjangoirárotear aRequisiçãoparaquemirátratá-la. Masprimeiro,oDjangoprecisaserinformadosobrequalcódigoprocessaqualrota. Fazemosisso no chamado URLconf e damos o nome a esse arquivo, por convenção,de urls.py.
Geralmente, temos um arquivo de rotas por app do Django. Por issocriamos o arquivourls.py dentro da pasta /website, lá nos capítulos iniciaisdeste Ebook. Como o apphelloworldé o núcleo da nossa aplicação, ele faz opapel de centralizador de rotas, isto é:
● Primeiro, a Requisição cai no arquivo /helloworld/urls.py e é roteadapara o appcorrespondente.● Em seguida, o URLConf do app (/website/urls.py, no nosso caso) vairotear a Requisição para aViewque irá processá-la.
Traduzindo emcódigo, fazemos isso da seguinte, alterando o arquivo, oarquivo helloworld/urls.py:
fromdjango.urls.confimportincludefromdjango.contribimportadminfromdjango.urlsimportpath
urlpatterns=[# Inclui as URLs do app websitepath('', include('website.urls', namespace='website')),
# Interface administrativapath('admin/', admin.site.urls),]
Assim, o Django irá tentar fazer o match(casamento) de URLs primeirono arquivo de URLs do app Website (website/urls.py) depois noURLConf daplataforma administrativa. Se não houver o casamento de URLs entre o queestá conﬁgurado nas rotas do Django e oqueousuárioquer acessar, umerroHTTP404NOTFOUNDserá retornado ao usuário, signiﬁcando que a página- ourota - não foi encontrada.
Podeparecer complicado, masaliembaixo, quandotratarmosmaissobreViews, vai fazer maissentido. AconﬁguraçãodoURLConf ébemsimples, basta

## Página 31

deﬁnirmos qual função ou Viewirá processar requisições de tal URL. Porexemplo, queremos que:
Quandoumusuáriotentaracessara URLraizdanossaaplicação /, oDjangochame a função index() para processar tal requisição.
Vejamoscomopoderíamosconﬁgurar esseroteamentononossoarquivode rotas urls.py:
# Importamos a função index() definida no arquivo views.pyfrom.importviews
app_name='website'
# urlpatterns contém a lista de roteamentos de URLsurlpatterns=[# GET /path('', views.index, name='index'),]
O atributoapp_name= 'website'deﬁne o namespace do app website(lembre-se do décimo nono Zen do Python: namespaces são uma boa ideia!- clique aqui para saber mais sobre o Zen do Python).
A função auxiliarpath()tem a seguinte assinatura:
path(rota, view, kwargs=None, name='')
Destrinchando cada parâmetro:
● rota: string contendo a rota (URL).● view: a função (ou classe) que irá tratar essa rota.● kwargs: utilizadoparapassar dadosadicionaisàfunçãooumétodoqueirátratar a requisição.● name: nomedarota. ODjangoutilizaoapp_namemaisonomedarotaparanomear a URL. Por exemplo, nonossocaso, podemoschamar arotaraiz'/'com'website:index'(app_site= website e a rota raiz =index). Vejamais sobrepadrões de formato de URL.
FUNÇÕES vs CLASS BASED VIEWS
ComasURLscorretamenteconﬁguradas, oDjangoirárotearRequisiçõespara onde você deﬁniu. No caso acima, sua requisição irá ser processada pelafunçãoviews.index().

## Página 32

Podemos tratar as requisições de duas formas: através de Viewsdesenvolvidas através de funções (Function Based Views) ou Viewsdesenvolvidas através declasses(Class Based Views, ou apenasCBVs).
Utilizando funções, você basicamente vai deﬁniruma função que:
● Recebecomo parâmetro uma requisição (request).● Realizaalgum processamento.● Retornaalguma informação, geralmente umaRespostaHTTP.
Já as Class Based Views são classes que herdamda classe View dopróprio Django (django.view.generic.base.View) e que agrupam diversasfuncionalidades para facilitar a vida do desenvolvedor.
CLASS BASED VIEWS
Nós podemos herdar e estender as funcionalidades das Class BasedViewspara atender a lógica da nossa aplicação.
Paraentender asdiferençasdasFunçõesedasClassBasedViews, vamosfazer umexemplo. Suponha você quer criar uma página coma listagemdetodososfuncionários. Utilizando funções, vocêpoderiachegar aesseobjetivoda seguinte forma:
fromdjango.shortcutsimportrenderfromhelloworld.modelsimportFuncionario
deflista_funcionarios(request):# Primeiro, buscamos os funcionariosfuncionarios=Funcionario.objetos.all()
# Incluímos no contextocontexto={'funcionarios': funcionarios}
# Retornamos o template para listar os funcionáriosreturnrender(request,"templates/funcionarios.html",contexto)
Aqui, algumas colocações:
● Toda função que vai processar requisições no Django recebe comoparâmetro um objeto request contendo os dados da requisição.● Contexto é o conjunto de dados que estarão disponíveis na página webque será retornada ao usuário.

## Página 33

● A função django.shortcuts.render() é umatalho (shortcut) do próprioDjango que facilita a renderização de templates: ela recebe a própriarequisição, o diretório do template, o contexto da requisição e retorna otemplaterenderizado.
Já utilizando Class Based Views, podemos utilizar a ListViewpresenteemdjango.views.generic para listar todos os funcionários, da seguinte forma:
fromdjango.views.genericimportListViewfromhelloworld.modelsimportFuncionario
classListaFuncionarios(ListView):template_name="templates/funcionarios.html"model=Funcionariocontext_object_name="funcionarios"
Percebaquevocênãoprecisoudescrever alógicaparabuscaralistadefuncionários?
É exatamenteisso queas Views doDjangoproporcionam: elasfacilitamo desenvolvimento de Views para os casos mais comuns (como listagem,exclusão, busca simples, atualização).
Ocaso comumpara uma listagemde objetos ébuscar todooconjuntode dados daquela entidade e mostrar no template, certo?! Éexatamenteissoque a ListView faz!
Com isso, um objeto funcionarios estará disponível no seu templatepara acesso. Dessa forma, podemos - por exemplo- criar umatabelanonossotemplatecom os dados de todos os funcionários, assim:
<table><tbody>{% for funcionario in funcionarios %}<tr><td>{{ funcionario.nome }}</td><td>{{ funcionario.sobrenome }}</td><td>{{ funcionario.remuneracao }}</td><td>{{ funcionario.tempo_de_servico }}</td></tr>{% endfor %}</tbody></table>
Não se preocupe com a sintaxe do código acima! Vamos falar maissobre templates no próximo capítulo!

## Página 34

O Django tem uma diversidade enorme de Views, uma para cadaﬁnalidade, por exemplo:
● CreateView: Para criar de objetos (É o Create do CRUD)● DetailView: Traz os detalhes de um objeto (É o Retrievedo CRUD)● UpdateView: Para atualização de um objeto (É o Updatedo CRUD)● DeleteView: Para deletar objetos (É o Delete do CRUD)
E várias outras muito úteis!
Agora vamos tratar detalhes do tratamento de requisições através deFunções. Em seguida, trataremos mais sobre as ClassBased Views.
FUNÇÕES (FUNCTION BASED VIEWS)
Utilizar funções é a maneira mais explícita para tratar requisições noDjango (veremos que as Class Based Views podem ser um pouco maiscomplexas pois muita coisa acontece implicitamente, por baixo dos panos).
Geralmenteaoutilizar funçõesparatratar Requisições, oprimeiropassoéveriﬁcar qual foi o método HTTP utilizado: foi umGET? Foi um POST? UmOPTION?
A partir dessa informação, processamos a Requisição da maneiradesejada. Vamos seguir o exemplo abaixo:
defcria_funcionario(request, pk):# Verificamos se o método POSTifrequest.method=='POST':form= FormularioDeCriacao(request.POST)
ifform.is_valid():form.save()returnHttpResponseRedirect(reverse('lista_funcionarios'))
# Qualquer outro método: GET, OPTION, DELETE, etc...else:returnrender(request,"templates/form.html",{'form': form})
O ﬂuxo é o seguinte:
● Primeiro, conformemencionei, veriﬁcamosométodoHTTPdarequisiçãono atributomethod do objeto request.● Depoisinstanciamosumformcomosdadosdarequisição(nocasoPOST)comFormularioDeCriacao(request.POST) na linha 4 (vamos falar maissobreFormmais para frente).

## Página 35

● Veriﬁcamos os campos do formulário comform.is_valid()nalinha 6.● Se tudo estiver OK, utilizamos o helper reverse()para traduzir a rota'lista_funcionarios'para funcionários/. Utilizamos isso pararedirecionar o usuário para aviewde listagem daaplicação.● Sefor qualquer outrométodo, apenasrenderizamosapáginanovamentecom o método render() na linha 12.
Deu para perceber que o objeto requesté essencial nas nossas Views,né?
Separei aqui alguns atributos desse objeto que provavelmente serão osmais utilizados por você:
● request.scheme: String representando o esquema (se veio por umaconexãoHTTP ou HTTPS).● request.path: String com o caminho da página requisitada -exemplo: /cursos/curso-de-python/detalhes.● request.method: Conformecitamos, contémométodoHTTPdarequisição(GET, POST, UPDATE, OPTION, etc).● request.content_type: Representa o tipo MIME da requisição- text/plain para texto plano, image/png para arquivos.PNG, por exemplo- saiba mais clicando aqui.● request.GET: Um dict contendo os parâmetros GET darequisição.● request.POST: Um dict contendo os parâmetros do corpo de umarequisição POST.● request.FILES: Caso seja uma páginade upload, contémosarquivosqueforam enviados.● request.COOKIES: Dict contendo todos os COOKIES noformato de string.
Observação: Parasaber maissobreoscamposdoobjeto request, dêumaolhada na classe django.http.request.HttpRequest!
DEBUGANDO UMA REQUISIÇÃO NO PYCHARM
Algumas vezes, é interessante você ver o conjunto de dados que estáchegando do usuário para o Django. Outrasvezes, precisamosveriﬁcar seestátudo correto, se tudo está vindo como esperado ou se existem erros narequisição.

## Página 36

Uma forma de vermos isso é debugando o código, isto é: pausando aexecução do código no momento emque a requisição chega no servidor eanalisando seus atributos, veriﬁcando se está tudo OK (ou não).
Se você utiliza o PyCharm, ou alguma outra IDE comdebugger, podefazer os passosqueeuvoudescrever aqui (creioqueemoutraIDE, oprocessoseja similar).
Por exemplo, vamos adicionar umbreakpoint no método de uma View.Para isso, clique duas vezes ao lado esquerdo da linha onde quer adicionar obreakpoint. O resultado deve ser esse (linha 33, veja o círculo vermelho nabarra à esquerda, próximo ao contador das linhas):
Comisso, quandoumarequisiçãofor enviadadonavegador dousuárioeque venha a passar nessa linha de código, o debugger entrará em ação,mostrando as variáveis naquela linha de código.
Nesse exemplo, quando o debugger chegou nessa linha, é possívelinspecionar todos os valores atuais na Requisição, contexto, ambiente e mais:
A partir dessa visão, podemos veriﬁcar todos os atributos do objetorequestque chegou no servidor!
Conﬁe em mim, isso ajuda MUITO a detectar erros!


## Página 37

Dito isso, agora vamos ver os detalhes do tratamento de requisiçõesatravés deClass Based Views.
AS PRINCIPAIS CLASS BASED VIEWS
Conforme expliquei anteriormente, as Class Based Views servemparafacilitar nossa vida, encapsulando funcionalidades comuns que tododesenvolvedor sempre acaba implementando. Por exemplo, geralmente:
●
Queremos que quando umusuário pedir a página inicial, sejamostradoapenas uma páginasimples, com as opções possíveis.
●
Queremos queanossapáginadelistagemcontenhaalistadetodososfuncionários cadastrados no banco de dados.
●
Queremos uma página comumformuláriocontendo todos oscampospré-preenchidos paraatualizaçãode dados de um funcionário.
●
Queremos umapágina de exclusãode funcionários.
●
Queremos um formulário em branco para inclusão de um novofuncionário.
Certo?!
Pois é, as CBVs - Class Based Views - facilitam issopara nós!
Temos basicamenteduas formaspara utilizar umaCBV:
● Primeiro, podemos utilizá-las diretamente no nosso URLConf (urls.py),através do método estáticoas_view, dessa forma:
fromdjango.urlsimportpathfromdjango.views.genericimportTemplateView
urlpatterns=[path('', TemplateView.as_view(template_name="index.html")),]
● E a segunda maneira, a mais utilizada e mais poderosa, é criar umaClasse herdando da View desejada e sobrescrevendo os atributos emétodos nessa subclasse criada, alterando sua lógica para atingir seusobjetivos.
Abaixo, veremos as Views mais utilizadas, e como podemos usá-las emnosso projeto.

## Página 38

TemplateView
Por exemplo, para o primeiro caso (mostrar uma página simples),podemosutilizar aTemplateView(acesseadocumentação)pararenderizarumapágina, da seguinte forma:
classIndexTemplateView(TemplateView):template_name="index.html"
Conﬁgurando as rotas da seguinte maneira:
fromdjango.urlsimportpathfromhelloworld.viewsimportIndexTemplateView
urlpatterns=[path('', IndexTemplateView.as_view(), name='index'),]
ListView
Jáparaosegundocaso, de listagemdefuncionários, podemosutilizar aListView(acesse a documentação).
Nela, nós conﬁguramos o Model que deve ser buscado (Funcionariononossocaso), eautomaticamentefazabuscaportodososregistrospresentesnobanco de dados da entidade informada.
Por exemplo, podemos descrever a Viewda seguinteforma:
fromdjango.views.generic.listimportListViewfromhelloworld.modelsimportFuncionario
classFuncionarioListView(ListView):template_name="website/lista.html"model=Funcionariocontext_object_name="funcionarios"
Utilizamos o atributocontexto_object_namepara nomear a variável queestará disponível no contexto dotemplateHTML (caso não utilizado, o nomepadrão dado pelo Django seráobject).
E conﬁguramos sua rota da seguinte maneira:
fromdjango.urlsimportpathfromhelloworld.viewsimportFuncionarioListView

## Página 39

urlpatterns=[path('funcionarios/', FuncionarioListView.as_view(),name='lista_funcionarios')]
Isso resultará emuma página lista.html contendo umobjeto chamadofuncionarioscom todos os Funcionários cadastrados, disponível para iteração.
Dica: É uma boa prática colocar o nome daViewno formato: Model +CBVbase. Por exemplo: umaViewquelistatodososCursos, receberiaonomede CursoListView (Model =Cursoe CBV =ListView).
UpdateView
Para a atualização de registros podemos utilizar aUpdateView(veja adocumentação). Com ela, conﬁguramos qual o Model (atributomodel), quaiscampos (atributofield) equal onomedotemplate(atributotemplate_name), ecom isso temos um formulário para atualização de registros do modelodeﬁnido.
No nosso caso:
fromdjango.views.generic.editimportUpdateViewfromhelloworld.modelsimportFuncionario
classFuncionarioUpdateView(UpdateView):template_name='atualiza.html'model=Funcionariofields=['nome','sobrenome','cpf','tempo_de_servico','remuneracao']
Dica: Aoinvésdelistar todososcamposemfieldsemformatodelistade strings, podemos utilizar fields= '__all__'. Dessa forma, o Django irábuscar todos os campos para você!
Mas de onde o Django vai pegar o id do objeto a serbuscado?
O Django precisa ser informado do idou slugpara poder buscar oobjeto correto a ser atualizado. Podemos fazer isso de duas formas.
Primeiro, na conﬁguração de rotas (urls.py):

## Página 40

fromdjango.urlsimportpathfromhelloworld.viewsimportFuncionarioUpdateView
urlpatterns=[# Utilizando o {id} para buscar o objetopath('funcionario/<id>',FuncionarioUpdateView.as_view(),name='atualiza_funcionario'),
# Utilizando o {slug} para buscar o objetopath('funcionario/<slug>',FuncionarioUpdateView.as_view(),name='atualiza_funcionario'),]
Mas o que é slug?
Slug é uma forma de gerar URLs mais legíveis a partir de dados jáexistentes, transformando todas as letras para minúsculas e todos os espaçospara hífens.
Exemplo: podemos criar um campo slug utilizando o camponomedofuncionário. Dessa forma, as URLs ﬁcariam assim:
● /funcionario/vinicius
E não assim (utilizando o id na URL):
● /funcionario/175
A segunda forma de buscar oobjetoéutilizando(ou sobrescrevendo) ométodoget_object() da classe paiUpdateView.
A documentação deste método traz (traduzido):
Retornao objetoquea Viewirá mostrar. Requerself.querysete umargumento pk ou slug no URLConf.Subclassespodemsobrescreveressemétodo e retornar qualquer objeto.
Ou seja, o Django nos dá total liberdade de utilizarmos a convenção(quando passamos os parâmetros na conﬁguração da rota - URLConf) ou aconﬁguração(quando sobrescrevemos o método get_object()).
Basicamente, ométodoget_object()devepegar o id ouslugdaURLebuscar no banco de dados o registro com aqueleid.

## Página 41

Uma forma de sobrescrevermos esse método na Viewde listagemdefuncionários (FuncionarioListView) pode ser implementada da seguintemaneira:
fromdjango.views.generic.editimportUpdateViewfromhelloworld.modelsimportFuncionario
classFuncionarioUpdateView(UpdateView):template_name="atualiza.html"model=Funcionariofields='__all__'context_object_name='funcionario'
defget_object(self, queryset=None):funcionario=None
# Os campos {pk} e {slug} estão presentes em self.kwargsid=self.kwargs.get(self.pk_url_kwarg)slug=self.kwargs.get(self.slug_url_kwarg)
ifidisnotNone:# Busca o funcionario apartir do idfuncionario=Funcionario.objects.filter(id=id).first()
elifslugisnotNone:# Pega o campo slug do Modelcampo_slug=self.get_slug_field()
# Busca o funcionario apartir do slugfuncionario=Funcionario.objects.filter(**{campo_slug:slug}).first()
# Retorna o objeto encontradoreturnfuncionário
Dessa forma, os dados do funcionário estarão disponíveis na variávelfuncionariono templateatualiza.html!
DeleteView
Para deletar funcionários, utilizamos a DeleteView (documentação).
Sua conﬁguração é similar à UpdateView: nós devemos informar aoDjango qual objeto queremos excluir via URLConf ou através do métodoget_object(). Precisamos conﬁgurar:
●
O template que será renderizado.
●
O model associado à essa view.
●
O nome do objeto que estará disponível no template.
●
A URL de retorno, caso haja sucesso na deleção do Funcionário.

## Página 42

Com isso, a view pode ser codiﬁcada da seguinte forma:
classFuncionarioDeleteView(DeleteView):template_name="website/exclui.html"model=Funcionariocontext_object_name='funcionario'success_url=reverse_lazy("website:lista_funcionarios")
Ométodoreverse_lazy()serve para fazer a conversão de rotas (similarao reverse()) mas em um momento em que o URLConf ainda não foicarregado pelo Django(que é o caso aqui).
AssimcomonaUpdateView, fazemosaconﬁguraçãodo id aserbuscadonoURLConf, da seguinte forma:
urlpatterns=[path('funcionario/excluir/<pk>',FuncionarioDeleteView.as_view(),name='deleta_funcionario')]
Assim, precisamosapenasfazerum template deconﬁrmaçãodaexclusãodo funcionário. Podemos fazer estetemplateda seguinteforma:
<formmethod="post">{% csrf_token %}
Você tem certeza que quer excluir o funcionário<b>{{funcionario.nome }}</b>?
<br><br>
<buttontype="button"><ahref="{% url 'lista_funcionarios' %}">Cancelar</a></button><button>Excluir</button></form>
Algumas colocações:
● A tag do Django {% csrf_token %}éobrigatóriaemtodosos forms poisestá relacionado à proteção que o Django provê ao CSRF - Cross SiteRequest Forgery (tipo de ataque malicioso - saibamais aqui).● Nãosepreocupecomasintaxedestetemplate, poisveremosmaissobreele nopróximo capítulo!

## Página 43

CreateView
Nessa View, precisamos apenas dizer para o Django o model, o nomedo template, aclassedoformulário(vamostratarmaissobre Forms aliembaixo)e a URL de retorno, caso haja sucesso na inclusão do Funcionário.
Podemos fazer isso assim:
fromdjango.views.genericimportCreateView
classFuncionarioCreateView(CreateView):template_name="website/cria.html"model=Funcionarioform_class=InsereFuncionarioFormsuccess_url=reverse_lazy("website:lista_funcionarios")
O método reverse_lazy()traduz a View em URL. No nosso caso,queremosquequandohajaainclusãodoFuncionário, sejamosredirecionadospara a página de listagem, para podermos conferir que o Funcionário foirealmente adicionado.
A conﬁguração da rota no arquivo urls.py pode ser feita da seguinteforma:
fromdjango.urlsimportpathfromhelloworld.viewsimportFuncionarioCreateView
urlpatterns=[path('funcionario/cadastrar/',FuncionarioCreateView.as_view()name='cadastra_funcionario'),]
Comisso, estará disponível no template conﬁgurado (website/cria.html,no nosso caso), um objeto form contendo os campos do formulário paracriação do novo funcionário.
E agora trataremos da forma que o framework traz para construção deFormulários em código HTML, osFormsdo Django!
FORMS NO DJANGO
Podemos utilizar o formulário do Django nas páginas HTML de duasformas. A primeira, mostra o formulário inteiro ”cru”, isto é, semformataçãoesem estilo, conforme o Django nos entrega.

## Página 44

Podemos utilizá-lo no nossotemplateda seguinte forma:
<formmethod="post">{% csrf_token %}
{{ form }}
<buttontype="submit">Cadastrar</button></form>
Observação: apesar de ser umForm, sua renderização não contémas tags <form></form>- cabendo a nós incluí-los no template.
Já a segunda, é mais trabalhosa, pois temos que renderizar campo acampono template. Porém, nosdáumnível maior decustomização. Podemosrenderizar cada campo do form dessa forma:
<formmethod="post">{% csrf_token %}
<labelfor="{{ form.nome.id_for_label }}">Nome</label>{{ form.nome }}
<labelfor="{{ form.sobrenome.id_for_label }}">Sobrenome</label>{{ form.sobrenome }}
<labelfor="{{ form.cpf.id_for_label }}">CPF</label>{{ form.cpf }}
<labelfor="{{ form.tempo_de_servico.id_for_label}}">Tempo de Serviço</label>{{ form.tempo_de_servico }}
<labelfor="{{ form.remuneracao.id_for_label }}">Remuneração</label>{{ form.remuneracao }}
<buttontype="submit">Cadastrar</button></form>
Nessetemplate:
● {{ form.campo.id_for_label }} traz o id da tag <input> para adicionarà tag<label></label>.● Utilizamos o {{ form.campo }}para renderizar apenas um campo doformulário, e não ele inteiro.
Esse template será renderizado emuma página HTML nonavegador dousuáriodonossosistema. Apósserapresentado, oformulárioserápreenchidoeentão submetido de volta ao nosso servidor. E agora vem a parte maiscomplexa quando desenvolvemos Formulários utilizando o Django: otratamento de dados!

## Página 45

O tratamento dos dados enviados no formulários é umatarefaquepode ser bem complexa.
Considere um formulário com diversos campos e diversas regras devalidação: seu tratamento não é mais um processo simples.
Os Forms do Django são formas de descrever, emcódigo Python, osformulários das páginas HTML, simpliﬁcando eautomatizandoseuprocessode criação e validação.
O Django tratatrêspartes distintas dos formulários:
●
Preparaçãodos dados tornando-os prontos para renderização
●
Criaçãode formulários HTML para os dados
●
Recepçãoe processamento dos formulários enviadosao servidor
Basicamente, queremos uma forma de renderizar emnosso template oseguinte código HTML:
<formaction="/insere-funcionario/"method="post"><labelfor="nome">Nome:</label><inputid="nome"type="text"name="nome"value=""><inputtype="submit"value="Enviar"></form>
Que, ao ser submetido ao servidor, tenha seus campos de entradavalidadose, emcasodevalidaçãopositiva–semerros, sejainseridonobancodedados e  no caso de falha na validação, que possamos mostrar isso ao usuário.
Nocentro desse sistema de formuláriosdo Djangoestá a classe Form.
Nela, nós descrevemos os campos queestarãodisponíveisnoformulárioHTML. Por exemplo, podemos descrever o formulário acima da seguinte forma:
fromdjangoimportforms
classInsereFuncionarioForm(forms.Form):nome=forms.CharField(label='Nome do Funcionário',max_length=100)
Neste formulário:
● Utilizamos a classeforms.CharFieldpara descreverum campo de texto.● O parâmetro label descreve um rótulo para esse campo.

## Página 46

● max_length descreve o tamanho máximo que esse input pode receber(100 caracteres, no caso).
Veja os diversos tipos de campos disponíveis acessandoaqui.
A classe forms.Formpossui um método muito importante, chamadois_valid(). Quando umformulário é submetido ao servidor, esse é umdosmétodos que irá realizar avalidação dos campos doformulário.
Se tudo estiver OK, ele colocará os dados do formulário no atributocleaned_data(que pode ser acessado por você posteriormente para pegaralguma informação - como o nome que foi inserido pelo usuário no campo<input name='nome'>).
Como o processo de validação do Django é bemcomplexo, optei pordescrever aqui o essencial para começarmos a utilizá-lo. Para saber maissobre o funcionamento dos Forms, acesse a documentaçãoaqui.
Vamos ver agora umexemplo mais complexo comumformulário deinserção de umFuncionário comtodos os campos. Para isso, crie o arquivoforms.pynoapp website.
Emseguida, e consultando a documentação dos possíveis campos doformulário, podemos descrever um Form de inserção assim:
fromdjangoimportforms
classInsereFuncionarioForm(forms.Form)
nome=forms.CharField(required=True,max_length=255)
sobrenome=forms.CharField(required=True,max_length=255)
cpf=forms.CharField(required=True,max_length=14)
tempo_de_servico=forms.IntegerField(required=True)
remuneracao=forms.DecimalField()

## Página 47

Affff, mas o Model e o Formsão quase iguais…Terei que reescrever os
campos toda vez? 
Claro que não, jovem! Por isso o Django nospresenteoucomoincrívelModelForm!
ComoModelFormnós conﬁguramos o Model que servirá como base doFormulário; oscamposquequeremosapartir doatributo fields, e, atravésdocampoexclude, os campos que não queremos.
Para fazer essa conﬁguração, utilizamos uma classe interna, chamadaMeta. Através dela, é possível conﬁgurar uma série de comportamentos doModelForm, como o modelo que será utilizado (atributo model), os campos(através do atributo fields), a forma de ordenação (através doatributo ordering) e mais (veja mais sobre Metaoptions).
Assim, nosso ModelForm, pode ser descrito da seguinteforma:
fromdjangoimportforms
classInsereFuncionarioForm(forms.ModelForm):classMeta:# Modelo basemodel=Funcionario
# Campos que estarão no formfields=['nome','sobrenome','cpf','remuneracao']
# Campos que não estarão no formexclude=['tempo_de_servico']
Podemos utilizar apenas o campo fields, apenas o exclude ou os doisjuntos e mesmo ao utilizá-los, ainda podemos adicionar outros campos,independentedos campos do Model.
O resultado será um formulário com todos os campos presentesno fields, menos os campos do exclude mais os outros campos queadicionarmos avulsamente.
Ficou confuso?


## Página 48

Então vamos ver um exemplo que utiliza todos os atributos e aindaadiciona novos campos ao formulário:
fromdjangoimportforms
classInsereFuncionarioForm(forms.ModelForm)chefe=forms.BooleanField(label='Este Funcionário exerce função de Chefia?',required=True,)
biografia=forms.CharField(label='Biografia',required=False,widget=forms.TextArea)
classMeta:# Modelo basemodel=Funcionario
# Campos que estarão no formfields=['nome','sobrenome','cpf','remuneracao']
# Campos que não estarão no formexclude=['tempo_de_servico']
Isso vai gerar um formulário com:
● Todos os campos contidos em fields ● Sem os campos contidos em exclude● O campo forms.BooleanFieldcomo um checkbox (<inputtype='checkbox' name='chefe' ...>)● Biograﬁa como uma área de texto (<textareaname='biografia'...></textarea>)
Assim como é possível deﬁnir atributos nos modelos, os campos doformuláriotambém são customizáveis.
Veja que o campo biografia é do tipo CharField, portanto deveria serrenderizado como um campo <input type='text' ...>'.

## Página 49

Contudo, nós modiﬁcamos o campo, através da conﬁguração widgetcomforms.TextArea. Assim, ele não mais será um simples input, mas serárenderizado como um <textarea></textarea> no nosso template!
Nós veremos mais sobre formulários no próximo capítulo, quandoformos renderizá-los em nossostemplates.
Agora vamos tratar de um componente muito importante noprocessamento de Requisições e formulaçãodeRespostasdanossaaplicação:osMiddlewares.
MIDDLEWARES
Middlewares sãotrechosdecódigosquepodemser executadosantesoudepois do processamento de Requisições/Respostas pelas Views da nossaaplicação. É uma forma que nós temos para alterar como o Django processaalgum dado de entrada ou de saída.
Se você olhar no arquivo settings.py, nós já temos a listaMIDDLEWARE com diversos middlewares pré-conﬁgurados:
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware',]
Por exemplo, temos o middlewareAuthenticationMiddleware. 
Ele é responsável por adicionar a variável usera todas as requisições.Assim, você pode, por exemplo, mostrar o usuário logado no seu template:
<li><ahref="{% url 'profile' id=user.id %}">Olá, {{ user.email }}</a></li>
Vocêpodepesquisar eperceber queemlugar nenhumemnossocódigonós adicionamos a variáveluserao Contexto das Requisições.

## Página 50

Nãoémuitocomum, maspodeser quevocêtenhaqueadicionaralgumcomportamentoantesdecomeçar atratar aRequisiçãooudepoisdeformaraResposta.
Portanto, veremos agora como podemos criar ummiddleware.
Um middleware éummétodo callable (quetemumaimplementaçãodométodo __call__) que recebe uma Requisição e retorna uma Resposta e,assim como umaView, pode ser escrito comofunçãoou comoClasse.
Um exemplo de middleware escrito como função é:
defmiddleware_simples(get_response):
# Código de inicialização do Middlewaredefmiddleware(request):# Código a ser executado antes da View e# antes de outros middlewares serem executados
response=get_response(request)
# Código a ser executado após a execução# da View que irá processar a requisição
returnresponse
returnmiddleware
E como Classe:
classMiddlewareSimples:def__init__(self, get_response):self.get_response=get_response
# Código de inicialização do Middlewaredef__call__(self, request):# Código a ser executado antes da View e# antes de outros middlewares serem executados
response=self.get_response(request)
# Código a ser executado após a execução# da View que irá processar a requisição
returnresponse
Cada Middleware é executado de maneira encadeada, do topo dalista MIDDLEWAREpara o ﬁm. Sendo assim, a saída de um é a entrada dopróximo.

## Página 51

Já utilizando a construção do middleware via Classe, nós temos trêsmétodos importantes:
O MÉTODOprocess_view
Assinatura do método: process_view(request, func,args, kwargs)
EssemétodoéchamadologoantesdoDjangoexecutara View quevaiprocessar a Requisição e possui os seguintes parâmetros:
● request é um objeto da Classe HttpRequest, do próprioDjango.● funcé a própria Viewque o Django está prestes a chamar, ao ﬁnal dacadeia de middlewares.● argsé a lista de parâmetros posicionais que serãopassados àView.● kwargséo dictcontendoosargumentosnomeados(keywordarguments)que serão passados àView.
Esse método deve retornar None ou um objeto HttpResponse:
● Caso retorne None, o Django entenderá que deve continuar a cadeiade Middlewares.● Caso retorne HttpResponse, o Django entenderá que a resposta estápronta para ser enviada de volta e não vai se preocupar emchamar oresto da cadeia de Middlewares, nem a View que iria processar arequisição.
O MÉTODOprocess_exception
Assinatura do método: process_exception(request, exception)
Esse método é chamado quando uma View lança uma exceção e deveretornar ouNoneouHttpResponse.
Caso retorne um objeto HttpResponse, o Django irá aplicar oMiddleware de resposta e o Middleware de template, retornando a requisiçãoao navegador do usuário.
● request é o objeto HttpRequest● exception é a exceção que foi lançada pela view.

## Página 52

O MÉTODOprocess_template_response
Assinatura do método: process_template_response(request,response)
Esse método é chamado logo após a View ter terminado sua execuçãocaso a resposta tenha uma chamada ao método render()indicando que areposta possui um template.
Possui os seguintes parâmetros:
● request é um objeto HttpRequest.● response é o objetoTemplateResponseretornado pela viewou por outromiddleware.
Agora vamos criar um middleware um pouco mais complexo paraexempliﬁcar o que foi dito aqui!
Vamos supor que queremos um middleware que ﬁltre requisições e sóprocesse aquelas que venham de uma determinada lista de IP’s.
Esse middleware é muito útil quando temos, por exemplo, umconjuntode servidores com IP ﬁxo que vão se conectar entre si. Você poderia, porexemplo, ter uma conﬁguração no seusettings.pychamadaALLOWED_SERVERScontendo a lista de IPs autorizados a se conectar ao seu serviço.
Para isso, precisamos abrir o cabeçalho das requisições que chegamnonosso servidor e veriﬁcar se o IPde origemestáautorizado. Comoprecisamosdessa lógica antes da requisição chegar na View, vamos adicioná-la aométodo process_view, da seguinte forma:
classFiltraIPMiddleware:
def__init__(self, get_response=None):self.get_response=get_response
def__call__(self, request):response=self.get_response(request)returnresponse
defprocess_view(request, func, args, kwargs):# Lista de IPs autorizadosips_autorizados=['127.0.0.1']
# IP do usuárioip=request.META.get('REMOTE_ADDR')

## Página 53

# Verifica se o IP do está na lista de IPs autorizadosifipnotinips_autorizados:# Se usuário não autorizado > HTTP 403 (NãoAutorizado)returnHttpResponseForbidden("IP não autorizado")
# Se for autorizado, não fazemos nadareturnNone
Depois disso, precisamos registrar nosso middleware no arquivo deconﬁgurações settings.py (na conﬁguração MIDDLEWARE):
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware',
# Nosso Middleware'helloworld.middlewares.FiltraIPMiddleware',]
Agora, podemos testar seu funcionamento alterando a listaips_autorizados:
● Coloqueips_autorizados= ['127.0.0.1'] e tente acessar alguma URLda aplicação: devemos conseguir acessar normalmente nossa aplicação,pois como estamos executando o servidor localmente, nosso IP seráexatamente igual à 127.0.0.1 e, portanto, passaremosnotestecondicionalque desenvolvemos no Middleware.● Agora coloque ips_autorizados= [] e tente acessar alguma URL danossa aplicação: deve aparecer a mensagem “IPnão autorizado”, poisnosso IP (127.0.0.1) não está mais autorizado a acessar o servidor,mostrando que nossa lógica funcionou corretamente!
CONCLUSÃO DO CAPÍTULO
Neste capítulo vimos vários conceitos importantes: vimos os tipos deViews(funçõeseclasses), osprincipaistiposdeCBV(ClassBasedViews), comomapear URLs para as views da aplicação através doURLConf, comoutilizar ospoderososFormsdo Django, Middlewarese muito mais!
Nopróximocapítulo, veremosacamadadanossaaplicação, queéquemfaz a Interface com o Usuário, aCamadaTemplate.

## Página 54

C A P Í T U L O   4
CAMADATEMPLATE
OfocodestecapítuloseráaCamadaTemplatedaarquiteturadoDjango.Neste capítulo vamos aprender aconﬁgurar, customizar eestender templates.Também veremos como utilizar os ﬁltros e tags que o próprio Django nosdisponibiliza, assimcomo criar tagseﬁltroscustomizadoseMiddlewares, quesãopeçasmuitoimportantesnodesenvolvimentodeaplicaçõesqueutilizamoDjango!
Alémdisso, veremos como customizar o visual de páginas web comofamoso Bootstrap, que dará uma identidade visual proﬁssional às páginas danossa aplicação!
ACamadaTemplatetemumaimportânciamuitograndenasaplicaçõesDjango, poiséelaquemdácaraaonossosistema, istoé, fazainterfacecomousuário. Énela que se encontra o código Python- responsável por renderizarnossaspáginas- eosarquivosHTML, CSSeJavascript - quedarãovidaànossaaplicação!
Contudo, vale ressaltar que as aplicações web vem sofrendo umamudançaemsuaarquitetura. Antigamente, eramuitocomumquetodocódigoda aplicação web vivesse apenas noBackend, como uma aplicação apenas -como servidor renderizando as páginas da aplicação. Hoje emdia, é muitocomumhaver essaseparaçãoentreBackendeFrontend, comduasaplicaçõesdistintas: oBackendservindo oFrontend, através de - geralmente - umaAPI,enquanto o Frontend é desenvolvido como uma aplicação à parte, utilizandoframeworksconsagradoscomoReact, AngularouVue.js, queconsumirãodadosdoBackend.

## Página 55

Isso não quer dizer que a camada Template do Django não temmaisutilização! Muitosprojetosaindaautilizam, poiselaémuitopoderosa, masseuuso vem diminuindo.
ONDE ESTAMOS…
Primeiro, vamos relembrar onde estamos no ﬂuxo deRequisição/Resposta da nossa aplicação Django:


## Página 56

Agora, estamos na camada que faz a interface do nosso códigoPython/Django como usuário, interagindo, trocando informações e captandodados de input.
Antes de mergulhar nessa Camada, vamos começar pelo começo,respondendo à seguinte pergunta: o que é um Template?
DEFINIÇÃO DE TEMPLATE
Basicamente, um template é um arquivo base que pode sertransformado em outro arquivo (um arquivo HTML, um CSS, umCSV, etc),através do processo deinterpolação de código.
Um template no Django contém:
● Variáveis que podem ser substituídas por valores, a partir do seuprocessamento por uma Engine de Templates (núcleo ou “motor” detemplates). Para se usar variáveis em templates, usamos marcadoresiniciados com chaves, dessa forma:{{ variável }}.● Tags que controlama lógica de renderização do template. Usamos aschaves e o símbolo de porcentagem, dessa forma: {%tag %}.● Filtros que adicionam funcionalidades ao template. Usamos com ocaracter chamado “pipe”, dessa forma: {{ variável|filtro}}.
Entenda interpolação como o processo de se misturar códigos emlinguagens diferentes (por exemplo HTML comcódigo Python) adicionandofuncionalidade, e tendo como saída apenas código em uma das duaslinguagens.
Não entendeu ainda?
Pense o seguinte: você talvez já saiba que HTML não temestruturas derepetição como oforouwhiledo Python, correto?
Ese fosse possível criar umcódigo que misturasse HTML como fordoPythonpara criar uma estrutura derepetiçãodentrodocódigoHTML, comoocódigo abaixo?!
<h1>Teste de interpolação</h1>
for dado in [1, 2, 3, 4]:<p>{{ dado }}</p>

## Página 57

Éexatamente isso que a interpolaçãofaz (comuma pequenadiferençade sintaxe): adiciona funcionalidades de um código a outro!
AgoravamosàumexemplocomarealsintaxedeinterpolaçãoutilizandoaEnginede templates do Django!
{# base.html contém o template que usaremos como esqueleto #}{% extends "base.html" %}
{% block conteudo %}<h1>{{ section.title }}</h1>
{% for f in funcionarios %}<h2><ahref="{% url 'website:funcionario_detalhe' pk=f.id%}">{{ funcionario.nome|upper }}</a></h2>{% endfor %}{% endblock %}
Agora vamos à explicação:
● Linha 1: Escrevemos comentário coma tag {# comentário #}. Eles serãoprocessados peloEnginee não estarão presentes napágina resultante.● Linha 2: Utilizamos {% extends "base.html" %}para estender de umtemplate, ou seja, utilizá-lo como base, passandoo caminho para ele.● Linha 4: Podemos facilitar a organização do template, criando blocoscom{% block nome_do_bloco %}{% endblock %}.● Linha 5: Podemos interpolar variáveis vindas do servidor em nossotemplate utilizando {{ secao.titulo }}- dessa forma, estamosacessandooatributotitulodoobjetosecao(quedeveestarnoContextoda resposta).● Linha 7: É possível iterar sobre objetos de uma lista através da tag{% for objeto in lista %}{% endfor %}.● Linha 10: Podemos utilizar ﬁltros para aplicar alguma função à algumavariável. Nesseexemplo, estamosaplicandooﬁltroupper-quetransformatodos os caracteres de uma string em maiúsculos - ao conteúdo defuncionario.nome. Também é possível encadear ﬁltros, por exemplo:{{ funcionario.nome|upper|cut:" " }}
Parafacilitar amanipulaçãodetemplates, osdesenvolvedoresdoDjangocriaramuma linguagemquecontémtodosesseselementoseachamaramdeDTL-Django Template Language! Veremos mais delaneste capítulo!

## Página 58

Para começarmos a utilizar os templates do Django, é necessárioprimeiroconﬁgurar sua utilização. E é isso que veremosagora!
CONFIGURAÇÃO
O nosso arquivo de conﬁguração settings.pycontém a seguinteconﬁguração, que deﬁne qual Engine (tambémchamada de Backend) fará oprocessamento dos templates da nossa aplicação:
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS': [],'APP_DIRS':True,'OPTIONS': {},},]
Mas você já se perguntou o que essa conﬁguraçãoquer dizer? Nela:
● BACKENDé o caminho para uma classe que implementa a API detemplatesdo Django.● DIRSdeﬁne uma lista de diretórios onde o Django deve procurar pelostemplates. A ordem da lista deﬁne a ordem de busca.● APP_DIRSdeﬁne se o Django deve procurar por templates dentro dosdiretórios dosappsinstalados emINSTALLED_APPS.● OPTIONScontémconﬁgurações especíﬁcas doBACKENDescolhido, ouseja,dependendo do backend de templates utilizado, você poderáconﬁgurá-lo utilizando parâmetros emOPTIONS.
Por ora, vamos utilizar as conﬁgurações padrão “de fábrica” pois elas jános atendem. Agora, vamos ver sobre a tal Django TemplateLanguage!
DJANGO TEMPLATE LANGUAGE (DTL)
A DTL é a linguagempadrão de templates do Django. Ela é simples,porémpoderosa. Dando uma olhada na sua documentação, podemos ver aﬁlosoﬁadaDTL (traduzido):
Se você temalgumaexperiênciaemprogramação, ousevocêestáacostumadocomlinguagens que misturamcódigo de programação diretamentenoHTML,você deve ter em mente que o sistema de templates do Django não é

## Página 59

simplesmentecódigoPythonembutidonoHTML.Istoé:osistemadetemplatesfoi desenhado para ser aapresentação, e não paraconterlógica!
Se você vemde outra linguagemde programação deve ter tidocontatocom o seguinte tipo de construção: código de programação adicionadodiretamente no código HTML (como PHP).
Isto é o terror dos designers(e não só deles)!
Ponha-se no lugar de um designer que não sabe nada sobreprogramação. Agora imagina você tendo que dar manutenção nos estilos deuma página LOTADA de código de programação?!
Complicado, hein?!
Por esse motivo que o template não deve conter lógica de negócio,apenas lógica que altere aapresentação dos dados!
Agora, nadamelhor paraaprender sobrea DTL doquebotandoamãonamassa e melhorando as páginas da nossa aplicação. Epara deixar as páginasvisualmente agradáveis, vamos utilizar o famosoBootstrap!
CONSTRUINDO A BASE DO TEMPLATE
Nosso template queservirádeesqueletodeveconter ocódigoHTMLqueirá se repetir em todas as páginas.
Devemos colocar nele os trechos de código mais comuns de páginasHTML. Por exemplo, toda página HTML:
● Deve ter as tags: <html></html>,<head></head>e<body></body>.● Deve ter os links para arquivos estáticos: <link></link>e<script></script>.
Você pode fazer o download dos arquivos necessários para o nossoprojetoaqui (Bootstrap) e aqui (jQuery)- que é umadependência doBootstrap.
Faça isso para todos asbibliotecasexternasquequeirautilizar (ouutilizeum CDN - Content Delivery Network).
Ok! Agora, comos arquivos devidamente colocados na pasta/static/,podemos começar com nossotemplate:

## Página 60

<!DOCTYPE html><html>{% load static %}<head><title>{% block title %}Gerenciador de Funcionários{% endblock %}</title>
<!-- Estilos --><linkrel="shortcut icon"type="image/png"href="{%static 'website/img/favicon.png' %}"><linkrel="stylesheet"href="{% static 'website/css/bootstrap.min.css'%}"><linkrel="stylesheet"href="{% static 'website/css/master.css'%}">
{% block styles %}{% endblock %}</head>
<body><navclass="navbar navbar-expand-lg navbar-lightbg-white"><aclass="navbar-brand"href="{% url 'website:index'%}"><imgsrc="{% static 'website/img/favicon.png' %}"height='45px'></a><buttonclass="navbar-toggler"type="button"data-toggle="collapse"data-target="#conteudo-navbar"aria-controls="conteudo-navbar"aria-expanded="false"aria-label="Ativar navegação"><spanclass="navbar-toggler-icon"></span></button>
<divclass="collapse navbar-collapse"id="conteudo-navbar"><ulclass="navbar-nav mr-auto"><liclass="nav-item active"><aclass="nav-link"href="{% url 'website:index'%}">Página Inicial</a></li><liclass="nav-item"><aclass="nav-link"href="{% url 'website:lista_funcionario'%}">Funcionários</a></li></ul></div></nav>
{% block conteudo %}{% endblock %}
<scriptsrc="{% static 'website/js/jquery.min.js'%}"></script><scriptsrc="{% static 'website/js/bootstrap.min.js'%}"></script>
{% block scripts %}{% endblock %}
<scriptsrc="{% static 'website/js/scripts.js' %}"></script></body></html>
E vamos as explicações:
● <!DOCTYPEhtml> serve para informar ao browser do usuário que se tratade uma página HTML5.● Para que o Django possa carregar dinamicamente os arquivos estáticosdosite, utilizamosa tagstatic. Elavai fazer abuscadoarquivoquevocêquer e fazer a conversão dos links corretamente. Para utilizá-la, énecessário primeiro carregá-la e fazemos isso através do código

## Página 61

{% load <modulo> %}. Após carregá-la, utilizamos a tag da seguintemaneira: {%static 'caminho/para/arquivo' %}, passando comoparâmetro a localização relativa à pasta /static/.● Podemos deﬁnir quaisquer blocos no nosso template com a tag{% blocknome_do_bloco %}{% endblock %}. Fazemos isso para organizarmelhor aspáginasqueirãoestender essetemplate. Podemospassar umvalor padrão dentro do bloco (igual está sendo utilizado na linha 6) -dessa forma caso não seja deﬁnido nenhumvalor no template ﬁlho - ovalor padrão é aplicado.● Colocamos os arquivos necessários para o funcionamento do Bootstrapnesse template, isto é: o jQuery, o CSS e o Javascript doBootstrap.● O link para outras páginas da nossa aplicação é feito utilizando-se a tag{% url'nome_da_view' parm1parm2... %}. Dessaforma, deixamosqueoDjango cuide da conversão para URLs válidas!● Oconjunto de tags<nav></nav>deﬁnema barra superior de navegaçãocomos linksparaaspáginasdaaplicação. Essetambéméumtrechodecódigo presente em todas as páginas, por isso, adicionamos aotemplate. (Documentação da Navbar - Bootstrap)
E pronto! Temos umtemplatebase!
Agora, vamos customizar a tela principal da nossa aplicação:a index.html!
PÁGINA INICIAL
Template: website/index.html
Nossatelainicial temoobjetivodeapenasmostrar asopçõesdisponíveisao usuário, que são:
●
Link para a página de cadastro de novos Funcionários.
●
Link para a página de listagem de Funcionários.
Primeiramente, precisamos dizer ao Django que queremos utilizar otemplateque deﬁnimos acima como base.
Para isso, utilizamos a seguinte tag do Django, que serve para queum template estenda de outro:

## Página 62

{% extends “caminho/para/template” %}
Com isso, podemos fazer:
<!-- Estendemos do template base -->{% extends "website/_layouts/base.html" %}
<!-- Bloco que define o <title></title> da nossa página -->{% block title %}Página Inicial{% endblock %}
<!-- Bloco de conteúdo da nossa página -->{% block conteudo %}<divclass="container"><divclass="row"><divclass="col-lg-6 col-md-6 col-sm-6 col-xs-12"><divclass="card"><divclass="card-body"><h5class="card-title">Cadastrar Funcionário</h5><pclass="card-text">Cadastre aqui um novo<code>Funcionário</code>.</p><ahref="{% url 'website:cadastra_funcionario'%}"class="btn btn-primary">Novo Funcionário</a></div></div></div><divclass="col-lg-6 col-md-6 col-sm-6 col-xs-12"><divclass="card"><divclass="card-body"><h5class="card-title">Lista de Funcionários</h5><pclass="card-text">Veja aqui a lista de<code>Funcionários</code>cadastrados.</p><ahref="{% url 'website:lista_funcionarios'%}"class="btn btn-primary">Vá para Lista</a></div></div></div></div></div>{% endblock %}
Nesse template:
● Aclassecontainerdo Bootstrap (linha 9) serveparadeﬁnir aáreaútil danossa página (para que nossa página ﬁque centralizada e não ﬁqueocupando todo o comprimento da tela).● As classesrowecol-*fazemparte do sistema Griddo Bootstrap e nosajudaatornar nossapáginaresponsiva (queseadaptaaosdiversostiposetamanhosdetela: celular, tablet, desktop, etc). Émuitoimportantevocê

## Página 63

seatentaraessedetalheparanãocomprometeraexperiênciadousuário,caso ele acesse em aparelhos diferentes!● As classes card*fazem parte docomponente Card doBootstrap.● Asclasses btne btn-primary(documentação)sãousadasparadarvisualde botão à algum elemento.
Com isso, nossa Página Inicial - ou nossa Homepage -ﬁca assim:
Top, hein?!
Agora vamos para a página de cadastro de Funcionários!
TEMPLATE DE CADASTRO DE FUNCIONÁRIOS
Template: website/cadastra-funcionario.html
Nesse template, mostraremos o formulário para cadastro de novosfuncionários ao usuário do sistema.
Lembra que deﬁnimos o Form do Django InsereFuncionarioFormnocapítulo passado?
Vamos utilizá-lo no template que criaremos emseguida, adicionando-ona ViewFuncionarioCreateView. Dessa forma, esta View irá expor umobjetoformno nosso template para que possamos utilizá-lo.
Mas antes deseguir, vamosinstalar umabibliotecaquevai nosauxiliar emuito a renderizar os campos de input do nosso formulário: a WidgetTweaks!


## Página 64

Comela, nóstemosmaior liberdadeparacustomizar oscamposdeinputdo nosso formulário (adicionando classes CSS e/ou atributos, por exemplo).
Para isso, primeiro nós a instalamos com:
pip install django-widget-tweaks
Depois disso, adicione-a à lista de apps instalados, no já conhecidoarquivohelloworld/settings.py:
INSTALLED_APPS=[...'widget_tweaks']
E, notemplateondeformosutilizá-lo, carregamoselacomatagload, daseguinte forma: {% load widget_tweaks %}!
E pronto, agora podemos utilizar a tagque irá renderizar os campos doformulário, arender_field:
{% render_field nome_do_campo parametros %}
Para alterar como o input será renderizado, utilizamos osparâmetrosdatag. Dessa forma, podemos alterar o código HTML resultante.
Assim, podemosescrever nossotemplatedecadastrodeFuncionáriosdaseguinte forma:
{% extends "website/_layouts/base.html" %}
{% load widget_tweaks %}
{% block title %}Cadastro de Funcionários{% endblock %}
{% block conteudo %}<divclass="container"><divclass="row"><divclass="col-lg-12 col-md-12 col-sm-12 col-xs-12"><divclass="card"><divclass="card-body"><h5class="card-title">Cadastro de Funcionário</h5><pclass="card-text">Complete o formulário abaixo para cadastrarum novo<code>Funcionário</code>.</p><formmethod="post"><!-- Não se esqueça dessa tag -->

## Página 65

{% csrf_token %}
<!-- Nome --><divclass="input-group mb-3"><divclass="input-group-prepend"><spanclass="input-group-text">Nome</span></div>{% render_field form.nome class+="form-control" %}</div>
<!-- Sobrenome --><divclass="input-group mb-3"><divclass="input-group-prepend"><spanclass="input-group-text">Sobrenome</span></div>{% render_field form.sobrenome class+="form-control" %}</div>
<!-- CPF --><divclass="input-group mb-3"><divclass="input-group-prepend"><spanclass="input-group-text">CPF</span></div>{% render_field form.cpf class+="form-control" %}</div>
<!-- Tempo de Serviço --><divclass="input-group mb-3"><divclass="input-group-prepend"><spanclass="input-group-text">Tempo de Serviço</span></div>{% render_field form.tempo_de_servico class+="form-control" %}</div>
<!-- Remuneração --><divclass="input-group mb-3"><divclass="input-group-prepend"><spanclass="input-group-text">Remuneração</span></div>{% render_field form.remuneracao class+="form-control" %}</div>
<buttonclass="btn btn-primary">Enviar</button></form></div></div></div></div></div>{% endblock %}
Alguns pontos importante sobre o formulário acima:
● Utilizamos novamente as classes container, row, col-*e card* doBootstrap.

## Página 66

● Conforme mencionei no capítulo passado, devemos adicionar a tag{% csrf_token %}para evitar ataques de Cross SiteRequest Forgery.● As classes Input Group do Bootstrapinput-group, input-group-prependeinput-group-textservempara customizar o estilo dos elementos <input/>.● Para aplicar uma classe ao campo, utilizamos osímbolodeadição+=noatributoclass: {% render_field form.campo class+='classe' %} 
Observação: É possível adicionar a classe CSS form-controldiretamente no nosso FormInsereFuncionarioForm, daseguinte forma:
classInsereFuncionarioForm(forms.ModelForm):nome=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':"form-control"}))...
Mas essaé umapéssimaideiaporque bagunçacódigo CSS dentrodecódigo Python. Não faça isso!
Nosso formulário deve ﬁcar assim:
Agora, vamos desenvolver o template de listagem deFuncionários.


## Página 67

TEMPLATE DE LISTAGEM DE FUNCIONÁRIOS
Template: website/lista.html
Nesta página, nós queremos mostrar o conjunto de Funcionárioscadastrados no banco de dados e as ações que o usuário da aplicação podetomar, que são: atualizar os dados de um Funcionário ou excluí-lo.
Você se lembra da view FuncionarioListView? Ela é responsável porbuscar a lista de Funcionários e expor umobjeto chamadofuncionariosparaiteração no template.
Podemos construir nosso template da seguinte forma:
{% extends "website/_layouts/base.html" %}
{% block title %}Lista de Funcionários{% endblock %}
{% block conteudo %}<divclass="container"><divclass="row"><divclass="col-lg-12 col-md-12 col-sm-12 col-xs-12"><divclass="card"><divclass="card-body"><h5class="card-title">Lista de Funcionário</h5>
{% if funcionarios|length > 0 %}<pclass="card-text">Aqui está a lista de<code>Funcionários</code>cadastrados.</p>
<tableclass="table"><theadclass="thead-dark"><tr><th>ID</th><th>Nome</th><th>Sobrenome</th><th>Tempo de Serviço</th><th>Remuneração</th><th>Ações</th></tr></thead>
<tbody>{% for f in funcionarios %}<tr><td>{{ f.id }}</td><td>{{ f.nome }}</td><td>{{ f.sobrenome }}</td><td>{{ f.tempo_de_servico }}</td><td>{{ f.remuneracao }}</td><td><ahref="{% url 'website:atualiza_funcionario'pk=f.id %}"

## Página 68

class="btn btn-info">Atualizar</a><ahref="{% url 'website:deleta_funcionario'pk=f.id %}"class="btn btn-outline-danger">Excluir</a></td></tr>{% endfor %}</tbody></table>{% else %}<divclass="text-center mt-5 mb-5 jumbotron"><h5>Nenhum<code>Funcionário</code>cadastradoainda.</h5></div>{% endif %}<hr/><divclass="text-right"><aclass="btn btn-primary"href="{% url 'website:cadastra_funcionario'%}">Cadastrar Funcionário</a></div></div></div></div></div></div>{% endblock %}
Nesse template:
● Utilizamos as seguintes classes do Bootstrap para estilizar as tabelas:tablepara estilizar a tabela ethead-darkpara escurecero cabeçalho.● Na linha 13, utilizamos o ﬁltro lengthpara veriﬁcar se a lista defuncionários estávazia. Seelacontiver dados, atabelaémostrada. Seelaestiver vazia, uma caixa como texto “NenhumFuncionário cadastradoainda”será mostrada.● Utilizamos a tag {% for funcionario in funcionarios %}na linha 30para iterar sobre a listafuncionarios.● Nas linhas 39 e 46 fazemos o link para as páginas de atualização eexclusão do usuário.
O resultado, sem Funcionários cadastrados, deve ser esse:

## Página 69

E com um Funcionário cadastrado:
Quando o usuário clicar em “Excluir”, ele será levado para a páginaexclui.htmle quando clicar em “Atualizar”, ele será levado para a páginaatualiza.html.


## Página 70

Vamos agora construir a página de Atualização de Funcionários!
TEMPLATE DE ATUALIZAÇÃO DE FUNCIONÁRIOS
Template: website/atualiza.html
Nessa página, queremos que o usuário possa ver os dados atuais doFuncionário e possa atualizá-los, conforme sua vontade. Para isso utilizamos aViewFuncionarioUpdateViewque implementamos no capítulopassado.
Elaexpõeumformuláriocomoscamposdomodelopreenchidoscomosdados atuais para que o usuário possa alterar.
Vamos utilizar novamente a biblioteca Widget Tweaks para facilitar arenderização dos campos deinput.
Veja no código abaixo como podemos fazer nosso template:
{% extends "website/_layouts/base.html" %}
{% load widget_tweaks %}
{% block title %}Atualização de Funcionário{% endblock %}
{% block conteudo %}<divclass="container"><divclass="row"><divclass="col-lg-12 col-md-12 col-sm-12 col-xs-12"><divclass="card"><divclass="card-body"><h5class="card-title">Atualização de Dados do Funcionário</h5><formmethod="post"><!-- Não se esqueça dessa tag -->{% csrf_token %}
<!-- Nome --><divclass="input-group mb-3"><divclass="input-group-prepend"><spanclass="input-group-text">Nome</span></div>{% render_field form.nome class+="form-control" %}</div>
<!-- Sobrenome --><divclass="input-group mb-3"><divclass="input-group-prepend"><spanclass="input-group-text">Sobrenome</span></div>{% render_field form.sobrenome class+="form-control" %}</div>

## Página 71

<!-- CPF --><divclass="input-group mb-3"><divclass="input-group-prepend"><spanclass="input-group-text">CPF</span></div>{% render_field form.cpf class+="form-control" %}</div>
<!-- Tempo de Serviço --><divclass="input-group mb-3"><divclass="input-group-prepend"><spanclass="input-group-text">Tempo de Serviço</span></div>{% render_field form.tempo_de_servico class+="form-control" %}</div>
<!-- Remuneração --><divclass="input-group mb-3"><divclass="input-group-prepend"><spanclass="input-group-text">Remuneração</span></div>{% render_field form.remuneracao class+="form-control" %}</div><buttonclass="btn btn-primary">Enviar</button></form></div></div></div></div></div>{% endblock %}
Nesse template, não temos nada de novo.
Perceba que o código é similar ao template de adição de Funcionários,com os campos sendo renderizados com atagrender_field.
Como nossa Viewherda deUpdateView, o objetoformjá vempopuladocomos dados do modelo emquestão (aquele cujoidfoi enviado aoclicar nobotão de edição).
Sua interface deve ﬁcar similar à:

## Página 72

E por último, temos o template de exclusão de Funcionários.
TEMPLATE DE EXCLUSÃO DE FUNCIONÁRIOS
Template: website/exclui.html
A função dessa página é mostrar uma página de conﬁrmação para ousuárioantesdaexclusãodeumFuncionário. Essapáginavai concretizarasuaexclusão.
A view queﬁzemos, a FuncionarioDeleteView, facilitabastantenossavida.Comela, bastadispararmosumarequisição POST paraaURLconﬁgurada, queoFuncionário será deletado!
Dessa forma, nosso objetivo se resume à:
<!-- Estendemos do template base -->{% extends "website/_layouts/base.html" %}
<!-- Bloco que define o <title></title> da nossa página -->{% block title %}Página Inicial{% endblock %}
<!-- Bloco de conteúdo da nossa página -->{% block conteudo %}<divclass="container mt-5"><divclass="card">


## Página 73

<divclass="card-body"><h5class="card-title">Exclusão de Funcionário</h5><pclass="card-text">Você tem certeza que quer excluir o funcionário<b>{{ funcionario.nome }}</b>?</p><formmethod="post">{% csrf_token %}<hr/><divclass="text-right"><ahref="{% url 'website:lista_funcionarios'%}"class="btn btn-outline-danger">Cancelar</a><buttonclass="btn btn-danger">Excluir</button></div></form></div></div></div>{% endblock %}
Aqui, novamente nada de novo.
Apenas mostramos o formulário onde o usuário pode decidir excluir ounão o Funcionário, que deve ﬁcar assim:
Pronto!Com isso, temos todas as páginas do nossoprojeto! 
Você comcerteza aprendeubastante nessa caminhada! Mas calma queainda não terminou, ainda temos mais conteúdo para que você ﬁque craqueem Django! Agora vamos ver como construir tags e ﬁltroscustomizados!
TAGS E FILTROS CUSTOMIZADOS
Sabemos, atéagora, queoDjangopossuiumagrandevariedadedeﬁltrosetagspré-conﬁgurados.


## Página 74

Contudo, épossível que, emalgumasituaçãoespecíﬁca, oDjangonãoteofereça o ﬁltro outagnecessários.
Por isso, elepreviuapossibilidadedevocê construirseusprópriosﬁltrose tags! E já que ele dispõe dessa capacidade, vamos explorá-la construindoumatagqueiránosdizerotempoatualformatadoeumﬁltroqueiráretornara primeira letra da string passada.
Mas primeiro, vamos começar com a conﬁguração necessária!
CONFIGURAÇÃO
Osﬁltrosetagscustomizadosresidememumapastaespecíﬁcadanossaestrutura: a/templatetags.
Sendo assim, crie na raiz do app website essa pasta(website/templatetags) e adicione:
● Umarquivo__init__.pyembranco (para que o Django enxergue comoum pacote Python).● O arquivotempo_atual.pyem branco referente à nossatag.● O arquivoprimeira_letra.pyem branco referente aonosso ﬁltro.
Nossa estrutura, portanto, deve ﬁcar:
-website/...-templatetags/- __init__.py- tempo_atual.py- primeira_letra.py...
ParaqueoDjangoenxerguenossastagseﬁltrosénecessárioqueoapponde eles estão instalados esteja conﬁgurada na lista INSTALLED_APPSdosettings.py(no nosso caso, websitejá está lá, portanto, nada a fazer aqui).
Também é necessário carregá-los com o {% load filtro/tag %}.
E já que temos que escolher um para começar: vamos começardesenvolvendo oﬁltro.
Vamos chamá-lo de primeira_letrae, quando estiver pronto, iremosutilizá-lo da seguinte maneira:

## Página 75

<p>{{ valor|primeira_letra}}</p>
FILTROprimeira_letra
Filtros customizados são basicamente funções que recebemumoudoisargumentos. São eles:
●
O valor doinput.
●
Ovalor do argumento - que pode ter umvalor padrão ounão recebernenhum valor.
Para ser umﬁltro válido, é necessário que o código dele contenha umavariável chamadaregisterque seja uma instância detemplate.Library(ondetodos os tags e ﬁltros são registrados).
Isso deﬁne um ﬁltro!
OutraquestãoimportantesãoasExceções. Comoaenginedetemplatesdo Django não provê tratamento de exceção: ao executar o código do ﬁltroqualquer exceção será exposta como uma exceção do próprio servidor.
Por isso, nosso ﬁltro deveevitar lançar exceções e, ao invés disso, deveretornar um valor padrão.
Para entender melhor, vamosver umexemplodeﬁltronativodopróprioDjango.
Abraoarquivodjango/template/defaultfilter.py. Látemosadeﬁniçãodediversos ﬁltros quepodemosutilizar emnossostemplates(euseparei algunsevou explicar ali embaixo).
Lá temos o exemplo do ﬁltro lower:
@register.filter(is_safe=True)@stringfilterdeflower(value):"""Convert a string into all lowercase."""returnvalue.lower()
Nele:
● @register.filter(is_safe=True)é umdecorator utilizado para registrarsua função como um ﬁltro para o Django. Só assimo framework vai

## Página 76

enxergar seu código (saiba mais sobre decorators no post do Blog daPython Academy: Domine Decorators em Python).● @stringfilter é umdecorator utilizado para dizer ao Django que seuﬁltro espera uma string como argumento.
Agoraqueviuumﬁltroreal doDjango, vamoscodiﬁcareregistrarnossopróprio ﬁltro!
Uma forma de pegarmos a primeira letra de uma string é através daindexação, acessando o índice[0], da seguinte forma:
fromdjangoimporttemplatefromdjango.template.defaultfiltersimportstringfilter
register=template.Library()
@register.filter@stringfilterdefprimeira_letra(value):returnvalue[0]
Nesse código:
● O códigoregister= template.Library()é necessário para pegarmosuma instância da biblioteca de ﬁltros do Django. Com ela, podemosregistrar nosso ﬁltro com@register.filter.● @register.filter e @stringfilter são os decorators que citei aqui emcima.
E agora vamos testar, fazendo o carregamento e utilização emalgumtemplate. Para isso, vamos alterar a tabela do templatewebsite/lista.html para incluir nosso ﬁltro da seguinteforma:
<!—- Primeiro, carregamos nosso filtro, logo após o extends -->{% load primeira_letra %}...<tableclass="table"><theadclass="thead-dark"><tr><th><!-- Retiramos o "ID" aqui --></th><th>Nome</th><th>Sobrenome</th><th>Tempo de Serviço</th><th>Remuneração</th><thclass="text-center">Ações</th></tr></thead><tbody>{% for f in funcionarios %}

## Página 77

<tr><!-- Aplicamos nosso filtro no atributo funcionario.nome--><td>{{ f.nome|primeira_letra }}</td><td>{{ f.nome }}</td><td>{{ f.sobrenome }}</td><td>{{ f.tempo_de_servico }}</td><td>{{ f.remuneracao }}</td><tdclass="text-center"><aclass="btn btn-primary"href="{% url 'website:atualiza_funcionario' pk=f.id%}">Atualizar</a><aclass="btn btn-danger"href="{% url 'website:deleta_funcionario' pk=f.id%}">Excluir</a></td></tr>{% endfor %}</tbody></table>
O que resulta em:
E com isso, terminamos nosso primeiro ﬁltro!
Agora vamos fazer nossa tag customizada: atempo_atual!


## Página 78

TAGtempo_atual
De acordo coma documentação do Django, “tags são mais complexasque ﬁltros pois podem fazer qualquer coisa“.
Desenvolver uma tag podeser algobemtrabalhoso, dependendodoquevocê deseja fazer. Mas tambémpode ser simples. Como nossa tagvai apenasmostrar o tempo atual, sua implementação não deve ser complexa. Para isso,utilizaremos um “atalho” do Django: asimple_tag!
Asimple_tag- como a própria tradução já diz: “simples tag” - é umaferramenta para construção de tags simples. Comela, a criação de tags ﬁcasimilar à criação de ﬁltros, que vimos na seção passada.
Primeiro, precisamos incluir uma instância detemplate.Library(para teracesso à biblioteca de ﬁltros e tags do Django). Em seguida, utilizaro decorator @register(pararegistrar nossa tag) edeﬁnir aimplementaçãodanossa função.
Para pegar o tempo atual, podemos utilizar o método now()dabiblioteca datetime. Como queremos formatar a data, tambémutilizamos ométodostrftime(), passandocomoparâmetroastringformatada(%Héahora,%Msão os minutos e%S são os segundos).
Podemos, então, deﬁnir nossatagda seguinte forma:
importdatetimefromdjangoimporttemplate
register=template.Library()
@register.simple_tagdeftempo_atual():returndatetime.datetime.now().strftime('%H:%M:%S')
Eparautilizá-la, acarregamoscom{%loadtempo_atual%}eemseguidaa utilizamos em nosso template com{% tempo_atual%}.
Nonossocaso, vamosutilizar nossatagnotemplate-basequecriamos: owebsite/_layouts/base.html.
Vamosadicionar umnovoitemàbarradenavegação(doladodireito), daseguinte forma:

## Página 79

<body><!-- Navbar --><navclass="navbar navbar-expand-lg navbar-lightbg-light">...<divclass="collapse navbar-collapse"id="navbarSupportedContent"><ulclass="navbar-nav mr-auto"><liclass="nav-item active"><aclass="nav-link"href="{% url 'website:index'%}">Página Inicial</a></li><liclass="nav-item"><aclass="nav-link"href="{% url 'website:lista_funcionarios'%}">Funcionários</a></li></ul><!-- Adicione a lista abaixo --><ulclass="navbar-nav float-right"><liclass="nav-item"><!-- Aqui está nosso filtro --><aclass="nav-link"href="#"><b>Hora:</b>{%tempo_atual %}</a></li></ul></div></nav>...
O resultado deve ser:
Veja a hora do lado direito superior, na barra de navegação (Hora: 16:12:42)!
As possibilidades são inﬁnitas!


## Página 80

Com isso, temos nosso ﬁltro e tag customizados!
Agora vamos dar uma olhada nos ﬁltros que estão presentes nopróprioDjango: os Built-in Filters!
FILTROS DO DJANGO
É possível fazer muita coisa com os ﬁltros que já vêm instalados nopróprio Django. Muitas vezes, é melhor você fazer algumas operações notemplate do que fazê-las no backend (desde que sejam operações deapresentação, apenas). Sempre veriﬁque aviabilidadedeumoudeoutroparafacilitar sua vida!
Como a lista de built-inﬁltersdoDjangoébeeeeemextensa(vejaalistacompleta aqui), vou listar aqui os que eu consideromais úteis!
Sem mais delongas, aí vai o primeiro: o capfirst!!!
FILTROcapfirst
O que faz: Torna o primeiro caracter do valor paramaiúsculo.Exemplo:Entrada: valor = 'esse é um texto'.Utilização:
{{ valor|capfirst }}
Saída:
Esse é um texto
FILTROcut
O que faz: Remove todas as ocorrências do parâmetrono valor passado.Exemplo:Entrada: valor = 'Esse É Um Texto De Testes'Utilização:
{{ valor|cut:" "}}
Saída:

## Página 81

EsseÉUmTextoDeTestes
FILTROdate
O que faz: Utilizado para formatar datas. Possui uma grande variedade deconﬁgurações (veja aqui).
Exemplo:Entrada: Objeto datetime.Utilização:
{{ data|date:'d/m/Y'}}
Saída:
01/07/2018
FILTROfilesizeformat
O que faz: Transforma tamanhos de arquivos em valoreslegíveis.
Exemplo:Entrada: valor = 123456789Utilização:
{{ valor|filesizeformat }}
Saída:
117.7 MB
FILTROfloatformat
Oque faz: Arredonda números componto ﬂutuante como número de casasdecimais passado por argumento.
Exemplo:Entrada: valor = 14.25145Utilização:
{{ valor|floatformat:"2"}}

## Página 82

Saída:
14.25
FILTROjoin
Oque faz: Juntaumalistautilizandoastringpassadacomoargumentocomoseparador.
Exemplo:Entrada: valor = ["Marcos", "João", "Luiz"]Utilização:
{{ valor|join:" - "}}
Saída:
Marcos – João – Luiz
FILTROlength
O que faz: Retorna o comprimento de uma lista ou string. Émuito utilizadopara saber se existem valores na lista (selength> 0, lista não está vazia).
Exemplo:Entrada: valor = ['Marcos', 'João']Utilização:
{% if valor|length > 0 %}<p>Lista contém valores</p>{% else %}<p>Lista vazia</p>{% endif %}
Saída:
<p>Lista contém valores</p>
FILTROlower
O que faz: Transforma todos os caracteres de uma stringem minúsculas.
Exemplo:

## Página 83

Entrada: valor = PaRaLeLePíPeDoUtilização:
{{ valor|lower }}
Saída:
paralelepípedo
FILTROpluralize
O que faz: Retorna um suﬁxo plural caso o númeroseja maior que 1.Exemplo:Entrada: valor = 12Utilização:
Sua empresa tem {{ valor }} Funcionário{{ valor|pluralize:"s" }}
Saída:
Sua empresa tem 12 Funcionários
FILTROupper
O que faz: Transforma em maísculo todos caracteresda string.Exemplo:Entrada: valor = texto de testesUtilização:
{{ valor|upper }}
Saída:
TEXTO DE TESTES
FILTROwordcount
O que faz: Retorna o número de palavras da string.Exemplo:Entrada: valor = Django é o melhor framework webUtilização:

## Página 84

{{ valor|wordcount }}
Saída:
6
Código
Ocódigocompletodesenvolvidonesseprojetoestá disponívelnoGithubda Python Academy. Clique aqui para acessá-lo e baixá-lo!
Para rodar o projeto, execute em seu terminal:
● pip install -r requirements.txtpara instalar as dependências.● python manage.py makemigrationspara criar as Migrações.● python manage.py migratepara efetivar asMigraçõesno banco de dados.● pythonmanage.pyrunserverpara executar o servidor de testes doDjango.● Acessar o seu navegador na páginahttp://localhost:8000(por padrão).
E pronto… Servidor rodando! 
Conclusão do Capítulo
Neste capítulo vimos como conﬁgurar, customizar eestender templates,como utilizar osﬁltrose tags doDjango, comocriar tags eﬁltroscustomizadose um pouquinho de Bootstrap, para deixar as páginas bonitonas!
E AGORA?


## Página 85

F I N A L I Z A Ç Ã O
UM ATÉ BREVE…
Finalmente chegamos ao ﬁmdo nosso ebook! Mas, como você sabe, oDjangoestáemconstanteevolução. Por isso, ébomvocêsemanteratualizadonas novidades lendo, pesquisando e acompanhando o mundo do Django.
Edeixoaqui novamenteoconviteparavocêconheceraJornadaPython:lá você vai aprender do básico ao avançado, comprojetos completo e comusabilidade real, dicas de carreira, certiﬁcado, suporte à dúvidas, alémde darcontinuidade aos seus estudos de Django, comconteúdos emvídeo, Quizzes,projetos mais complexos e muito mais!
Clique na imagem abaixoagoramesmo para conhecera Jornada Python!
Te espero lá😉
