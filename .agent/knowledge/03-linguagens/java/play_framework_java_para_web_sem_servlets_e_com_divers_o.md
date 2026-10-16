---json
{
  "id": "play_framework_java_para_web_sem_servlets_e_com_divers_o",
  "title": "Play Framework Java para web sem servlets e com diversão",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Play Framework Java para web sem servlets e com diversão.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "com",
    "divers",
    "framework",
    "java",
    "linguagens",
    "para",
    "play",
    "sem"
  ],
  "perguntas_tipo": [
    "Como utilizar Play Framework Java para web sem servlets e com diversão?",
    "Quais as boas praticas de java?"
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
  "dono": "stack-java",
  "prioridade": 2
}
---

# Play Framework Java para web sem servlets e com diversão

> **Arquivo Original:** `Play Framework Java para web sem servlets e com diversão.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográficos,
eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 5

CasadoCódigo
Agradecimentos
Agradeçoavocêporquereraprendermais,àminhaesposaporsempreestaraomeu
lado,aosmeuspaiseaDeusportudo.
Esegueojogo!
i

## Página 7

CasadoCódigo
S o b r eo a u t o r
FormadopelaUNESPemBCC,foiinstrutoroficialdaSunMicrosystemsedaOra-
cleEducation.Atualmentecontribuiparaalgunsprojetosopensource,comoKDE,
Jenkinsentreoutros.
iii

## Página 9

CasadoCódigo
Prefácio
Omelhorpresentequesedáéaquelequevocêgostariadeganhar.
EsseéolivroqueeugostariadelerquandoestavacomeçandoausaroPlay
Framework,eleéomeupresenteparavocê,aproveite!
Públicoalvo
EsselivrofoifeitoparaprogramadoresJava(inicianteseveteranos)quebuscam
pelodesenvolvimentorápidoedivertidodeaplicações web.
Quickstart – a primeira p a r t edo livro
Pararapidamenteconfiguraroseuambientededesenvolvimento,disponibilizar
asuaaplicaçãobonita,acessandobancodedadosepublicandonanuvemnãoserá
precisolertodososcapítulos,apenasosquatroprimeiros.
Melhorando sua a p l i c ação – a segunda p a r t edo livro
Oscapítulosrestantescomplementamasuaaplicaçãocomacriaçãodeserviços,
autenticaçãoeousodealgunspluginsimperdíveisparaoseusistema.
Código f o n t e
O código fontedesse livro estádisponívelno endereço https://github.com/
boaglio/play2-casadocodigo,ondeforamcriadastagsparacadaumdoscapítulos,
parafacilitaracompreensãodaevoluçãodonossosistemadefilmescult.
v

## Página 11

CasadoCódigo Sumário
Sumário
1 H e l l oPlay J a v ae H e l l oPlay S c a l a 1
1.1 OqueéoPlay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 OquenãoéoPlay. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.3 InstalaçãodoPlay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 SuaprimeiraaplicaçãoJava. . . . . . . . . . . . . . . . . . . . . . . . . 6
1.5 AestruturadaaplicaçãoPlay. . . . . . . . . . . . . . . . . . . . . . . . 7
1.6 SubindosuaaplicaçãoPlay . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.7 OláScala . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.8 PrecisosaberScala? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.9 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2 N a v e g a n d ocom estilo 15
2.1 Bem-vindoaoEclipse . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.2 Navegação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.3 Adicionandoestilo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.4 Organizandoaspáginas. . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.5 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3 Persistindo se u sdados 29
3.1 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
4 Publicando em qualquer lugar 45
4.1 Redelocal. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.2 ServidorJavaEE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.3 Deploynanuvem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.4 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
vii

## Página 12

Sumário CasadoCódigo
5 Melhorando o input do usuário 55
5.1 Isolandomensagens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
5.2 Tratandoerros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
5.3 Páginascustomizadas . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
5.4 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
6 Criando se rviços 67
6.1 Acessandoserviçoviaweb . . . . . . . . . . . . . . . . . . . . . . . . . 67
6.2 DebugandopeloEclipse . . . . . . . . . . . . . . . . . . . . . . . . . . 69
6.3 Acessandoserviçoviamobile . . . . . . . . . . . . . . . . . . . . . . . 71
6.4 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
7 I n t e g r a n d onas re dessociais 7 5
7 . 1CriandoumaaplicaçãonoFacebook . . . . . . . . . . . . . . . . . . . 75
7 . 2IntegraçãoviaJavaScript . . . . . . . . . . . . . . . . . . . . . . . . . . 77
7 . 3IntegraçãoviaSecureSocial. . . . . . . . . . . . . . . . . . . . . . . . . 80
7 . 4Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
8 Melhorias na a p l i c ação 89
8.1 ConfigurandoHTTPS. . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
8.2 Lendoconstantesglobais . . . . . . . . . . . . . . . . . . . . . . . . . . 93
8.3 Uploaddeimagem. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
8.4 Testandosuaaplicação . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
8.5 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
9 Continue se u sestudos 115
9.1 Parasabermais. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
10 ApêndiceA - Play console em detalhes 117
11 ApêndiceB - Instalação e configuração do PostgreSQL 119
12 ApêndiceC - Instalação e configuração do Android 129
viii

## Página 13

Capítulo1
H e l l oPlayJ a v aeH e l l oPlayScala
1.1 O que é o Pl a y
OPlayéumframeworkqueredefineodesenvolvimentowebemJava.Oseufoco
éodivertidodesenvolvimentonoqualainterfaceHTTPéalgosimples,flexívele
poderoso,sendoumaalternativalimpaparaasopções EnterpriseJavainfladas.Ele
focanaprodutividadedodesenvolvedorparaasarquiteturasRESTful,esuavanta-
gememrelaçãoàslinguagenseframeworksnãoJava,comoRailsePHP,équeele
usufriudetodoopoderdaJavaV i r t u a lMachine(JVM).
1.2 O que n ã o é o Pl a y
OPlaynãoéumframeworkpadrãoJavaEE,comoSpring,StrutsouVRaptor–ele
usaumaarquiteturaextremamentesimples.
U m aaplicação JSFrodasobreaAPIdeServlet,queporsuavezrodaemum
containerJavaEE,queficadentrodeumHTTPServer.

## Página 14

1.2.OquenãoéoPlay CasadoCódigo
Percebaquetododesenvolvedoréobrigadoatrabalharcomessasquatrocama-
das. JácomoPlay,temosapenasduas:opróprioPlayframeworkeoseuHTTP
serverembutido(Netty).
Alémdisso,elenão éapenasumframeworkweb,eleéumasolução completa
queenvolvepersistênciaemuitomaisrecursos,como:
•ServidorHTTPintegrado;
•AcessocompletoàinterfaceHTTP;
•APIdeserviçosREST;
•Códigocujasmudançasépossíveltestarcomumsimplesreloaddepágina;
•Enginedetemplatedealtaperformance;
•Permitirquesuaaplicaçãofuncioneparaváriosidiomas;
•Compilaçãodosarquivosestáticosdesuaaplicação;
•SuporteaI/Oassíncrono;
•ValidaçãoHTMLdoinputdousuário;
•Cacheintegrado;
•Sistemadebuildpróprioeintegrado(sbt);
•Plataformaakkacriadaparaambientedistribuídoeàprovadefalhas;
•Persistênciadedados.
ConfiraavisãogeraldoPlaynafigura1.1
2

## Página 15

CasadoCódigo Capítulo1.HelloPlayJavaeHelloPlayScala
Figura1.1:Playframeworkstack
1.3 Instalação d oPl a y
AinstalaçãodoPlayébemsimplesefeitaemapenasdoispassos.Oprimeirodelesé
fazerodownloaddositehttp://www.playframework.org.Depoisdisso,façaoajuste
conformeoseusistemaoperacional.
Instalação no Windows
Descompacteopacotenaraizerenomeieodiretóriocompactadopara play.
Exemplo: oarquivo play-2.2.1.zip criaráodiretório C:\play-2.2.1\.
Renomeie-opara C:\play\.
3

## Página 16

1.3.InstalaçãodoPlay CasadoCódigo
Figura1.2:V a r i á v e ldeambientenoWindows
Editeavariável PATHconformeafigura1.2,adicionandonofinaldo PATHo
valorde ;C:\play\.
4

## Página 17

CasadoCódigo Capítulo1.HelloPlayJavaeHelloPlayScala
Atrás de u m p r o x y
Se sua internet estiver atrásde um proxy, altere o arquivo
C:\play\framework\build.batnalinhadecomandoJavaeadici-
oneosparâmetros:
-Dhttp.proxyUser=<meu-usuario>
-Dhttp.proxyPassword=<minha-senha>
-Dhttp.proxyHost=<servidor>
-Dhttp.proxyPort=<porta>
Casosejalançadaumaatualização doPlay,evocêqueiraatualizar,renomeie
odiretório C:\play\para C:\play-old\edescompacteanovaversão em
C:\play\.
Instalação em Linux
Descompacteopacotenaraiz,porexemplo: /home/fb/play-2.2.1/,ecrie
umlinksimbólicoparaessediretóriochamado play,como:
ln -s /home/fb/play-2.2.1/ /home/fb/play
Casohajaumaatualização,descompacteanovaversãoeatualizeolinksimbólico
paraonovodiretório.
Adicionenoarquivo $HOME/.bashrcouem $HOME/.bash_profileoco-
mando: export PATH=$PATH:$HOME/play/.
Instalação em Ma cOSX
Descompacteopacotenaraiz,porexemplo: /home/fb/play-2.2.1/,ecrie
umlinksimbólicoparaessediretóriochamado play,como:
ln -s /home/fb/play-2.2.1/ /home/fb/play
Adicionenoarquivo /etc/pathsodiretório $HOME/play/.
Emumaeventualatualização,descompacteanovaversãoeatualizeolinksim-
bólicoparaonovodiretório.
SepreferirusaroHomebrew,apenasrodeocomando brew install play.
5

## Página 18

1.4.SuaprimeiraaplicaçãoJava CasadoCódigo
T estandosua instalação
Depoisdeconfigurado,abraoconsoledoseusistemaoperacionaledigite play
help.Oresultadoesperadoestánafigura1.3.
Figura1.3:InstalaçãodoPlaycomsucessonoWindows
Pronto! AgoraqueoPlayestáinstalado,podemoscomeçaranossaprimeira
aplicação!
1.4 Su aprimeira aplicação Ja v a
Para criar a nossa primeira aplicação, é só digitar play new
<nome-da-aplicação>:
fb@cascao ~/workspace-play > play new play-java
_
_ __ | | __ _ _ _
| ’_ \| |/ _’ | || |
| __/|_|\____|\__ /
|_| |__/
play 2.2.1 built with Scala 2.10.2 (running Java 1.7.0_51),
6

## Página 19

CasadoCódigo Capítulo1.HelloPlayJavaeHelloPlayScala
http://www.playframework.com
The new application will be created in /home/fb/workspace-play/play-java
What is the application name? [play-java]
>
Depoisescolhaaopção2,quevaicriarumaaplicaçãoPlayJava:
Which template do you want to use for this new application?
1 - Create a simple Scala application
2 - Create a simple Java application
> 2
OK, application play-java is created.
Have fun!
fb@cascao ~/workspace-play >
Epronto,suaaplicaçãoestácriada!
1.5 A estrutura d aaplicação Pl a y
V a m o sapenasolharoquefoicriado,semmuitosdetalhes:
.
|-- app (arquivos Java da aplicação)
| |-- controllers
| | `-- Application.java
| `-- views
| |-- index.scala.html
| `-- main.scala.html
|-- build.sbt
|-- conf (arquivos de configuração)
| |-- application.conf
| `-- routes
|-- project
| |-- build.properties
| `-- plugins.sbt
7

## Página 20

1.6.SubindosuaaplicaçãoPlay CasadoCódigo
|-- public (arquivos estáticos)
| |-- images
| | `-- favicon.png
| |-- javascripts
| | `-- jquery-1.9.0.min.js
| `-- stylesheets
| `-- main.css
|-- README
`-- test (arquivos para testes)
|-- ApplicationTest.java
`-- IntegrationTest.java
1.6 Subindo sua aplicação Pl a y
Aadministraçãodesuaaplicaçãoéfeitapelo play console,quepossuidiversos
comandosdegerenciamento.
Parachamaroconsole,dentrododiretóriocriadonasuaaplicaçãodigite play,
edepoisocomando runparasubir.
fb@cascao ~/workspace-play/play-java > play
[info] Loading project definition from
/home/fb/workspace-play/play-java/project
[info] Set current project to play-java (in build
file:/home/fb/workspace-play/play-java/)
_
_ __ | | __ _ _ _
| ’_ \| |/ _’ | || |
| __/|_|\____|\__ /
|_| |__/
play 2.2.1 built with Scala 2.10.2 (running Java 1.7.0_51),
http://www.playframework.com
> Type "help play" or "license" for more information.
> Type "exit" or use Ctrl+D to leave this console.
[play-java] $ run
[info] Updating {file:/home/fb/workspace-play/play-java/}play-java...
[info] Resolving org.fusesource.jansi#jansi;1.4 ...
[info] Done updating.
8

## Página 21

CasadoCódigo Capítulo1.HelloPlayJavaeHelloPlayScala
--- (Running the application from SBT, auto-reloading is enabled) ---
[info] play - Listening for HTTP on /0.0.0.0:9000
(Server started, use Ctrl+D to stop and go back to the console...)
Emseguida,épossívelacessaraaplicaçãoatravésdobrowserpeloendereçohttp:
//localhost:9000/,obtendoumresultadosemelhanteàfigura1.4.
Figura1.4:RodandoPlay
Paraderrubaroservidor,tecle Control+De,parasairdo play console,
digite exit.
1.7 Ol á Scala
Duranteolivro,vamosfocarnoJava,mascriarerodarumaaplicação emScalaé
parecido:
9

## Página 22

1.7.OláScala CasadoCódigo
fb@cascao ~/workspace-play > play new play-scala
_
_ __ | | __ _ _ _
| ’_ \| |/ _’ | || |
| __/|_|\____|\__ /
|_| |__/
play 2.2.1 built with Scala 2.10.2 (running Java 1.7.0_51),
http://www.playframework.com
The new application will be created in /home/fb/workspace-play/play-scala
What is the application name? [play-scala]
>
Depoisselecioneaopção1,quevaicriarumaaplicaçãoPlayScala:
Which template do you want to use for this new application?
1 - Create a simple Scala application
2 - Create a simple Java application
> 1
OK, application play-scala is created.
Have fun!
fb@cascao ~/workspace-play > cd play-scala/
fb@cascao ~/workspace-play/play-scala > play
[info] Loading project definition from
/home/fb/workspace-play/play-scala/project
[info] Set current project to play-scala
(in build file:/home/fb/workspace-play/play-scala/)
_
_ __ | | __ _ _ _
| ’_ \| |/ _’ | || |
| __/|_|\____|\__ /
|_| |__/
play 2.2.1 built with Scala 2.10.2 (running Java 1.7.0_51),
http://www.playframework.com
10

## Página 23

CasadoCódigo Capítulo1.HelloPlayJavaeHelloPlayScala
> Type "help play" or "license" for more information.
> Type "exit" or use Ctrl+D to leave this console.
[play-scala] $ run
[info] Updating {file:/home/fb/workspace-play/play-scala/}play-scala...
[info] Resolving org.fusesource.jansi#jansi;1.4 ...
[info] Done updating.
--- (Running the application from SBT, auto-reloading is enabled) ---
[info] play - Listening for HTTP on /0.0.0.0:9000
(Server started, use Ctrl+D to stop and go back to the console...)
[info] Compiling 5 Scala sources and 1 Java source to
/home/fb/workspace-play/play-scala/target/scala-2.10/classes...
[info] play - Application started (Dev)
Oresultadotambémésemelhanteàfigura1.5.
11

## Página 24

1.8.PrecisosaberScala? CasadoCódigo
Figura1.5:RodandoPlay
1.8 Precisosaber Scala?
Felizmentenão. OcoredoPlay2éfeitoemScala,maseleéperfeitoparaJava,
poispodemostrabalharcomelesemaprenderumanovalinguagemeambosusam
anossaqueridaJVM.
1.9 Próximos passos
Certifique-sedequeaprendeu:
•visãogeraldoPlayFramework;
•comoinstalaroPlay;
•comocriarsuaprimeiraaplicaçãoemJavaeScala.
12

## Página 25

CasadoCódigo Capítulo1.HelloPlayJavaeHelloPlayScala
Agoraquejámolhamosospés,nospróximoscapítulosvamosaprenderanadar
criandooprimeiroCRUD.
13

## Página 27

Capítulo2
Navegandocomestilo
AaplicaçãodoPlaypossuiumaestruturasimplesquefacilitamuitoodesenvolvi-
mentodeaplicações. Nessecapítulo,veremoscomodeixarsuaaplicaçãocomuma
interfacemaisprofissionalecomocontrolaranavegação entreastelasusandoos
templates.
Masantesdisso,vamossairdoconsoleeaprenderaconfigurarsuaaplicaçãono
Eclipse?
2.1 Bem -vindo a oEclipse
V a m o scriarumaaplicação chamada“filmes”,damesmamaneiraquevocêviuno
capítuloanterior.
•playnewfilmes
•cdfilmes
•play

## Página 28

2.1.Bem-vindoaoEclipse CasadoCódigo
AcessandooconsoledoPlay,usamosocomando eclipseparaprepararoseu
projeto:
fb@cascao /home/fb/workspace-play/filmes > play
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
[info] Set current project to filmes
(in build file:/home/fb/workspace-play/filmes/)
_
_ __ | | __ _ _ _
| ’_ \| |/ _’ | || |
| __/|_|\____|\__ /
|_| |__/
play 2.2.1 built with Scala 2.10.2 (running Java 1.7.0_51),
http://www.playframework.com
> Type "help play" or "license" for more information.
> Type "exit" or use Ctrl+D to leave this console.
[filmes] $ eclipse
[info] About to create Eclipse project files for your project(s).
[info] Updating {file:/home/fb/workspace-play/filmes/}filmes...
[info] Resolving org.fusesource.jansi#jansi;1.4 ...
[info] Done updating.
[info] Compiling 4 Scala sources and 2 Java sources to
/home/fb/workspace-play/filmes/target/scala-2.10/classes...
[info] Successfully created Eclipse project files for project(s):
[info] filmes
[filmes] $
Osarquivosnecessáriosforamcriadosparaimportamosoprojeto.
AbraoseuEclipsenoworkspaceemquecriouoprojetoeselecioneaopção
Importconformeindicadonafigura:
16

## Página 29

CasadoCódigo Capítulo2. Navegandocomestilo
Figura2.1:ImportandooprojetocomEclipse
Emseguida,escolhaaopção Existing Projects into workspace.V e j a
aimagem:
17

## Página 30

2.1.Bem-vindoaoEclipse CasadoCódigo
Figura2.2:Escolhaaopçãodeprojetosexistentes
Depoisdeindicarodiretóriodoseuworkspace,escolhaoprojetofilmesesele-
cione Finishparaconcluiraimportação:
18

## Página 31

CasadoCódigo Capítulo2. Navegandocomestilo
Figura2.3:Finalizeaimportaçãodoprojeto
para os usuários d oIntellij IDEA
ParaprepararoseuprojetoparaessaIDE,useocomando ideaden-
trodoconsoledoPlay.
Pronto,tudoestádentrodoEclipse,ficoumaisfácildetrabalhar!
Agoraqueimportamosoprojeto,temosdiversosarquivosorganizadosnonosso
Eclipse.Precisamosentenderparaqueservecadaumdeles.
19

## Página 32

2.2.Navegação CasadoCódigo
Figura2.4:Arquivosdoprojetofilmes
2.2 Navegação
Quallinkchamaqualmétodo?Emaplicações JavaEEessemapeamentopodeser
feitodediversasmaneiraseemdiferenteslugares,oquetornacomplicadoocontrole
dealterações deumsistema. Felizmente,noPlaytudoissoéconcentradoemum
únicoarquivo,quearmazenaomapeamentodetodasasrotasqueumaaplicação
suporta.
Oarquivoderotas, conf/routes,édividoemtrêspartesdefinidasnessaor-
dem:
1)métodoHTTP–GETouPOST;
2) URIdaaplicação;
20

## Página 33

CasadoCódigo Capítulo2. Navegandocomestilo
3)classequeseráchamadaaoacessaraURIcomométodoHTTP.
Porpadrão,apáginaraizvemcomaconfiguraçãoconformeafigura:
Figura2.5:Arquivoderotas
V a m o sentendermelhorofuncionamentodessearquivocriandoumapáginade
informações sobreosistema.
Escrevemos um métodoque trataráas informações na classe existente
Application,quejácontémométodo indexresponsávelpelapáginainicial.
public static Result sobre() {
return ok("Sobre");
}
T o d ométododeumcontrollerdoPlaydeveseguirtrêsregrassimples:
1)deveserpublic;
2) deveserstatic;
3)deveretornarumobjetodotipoResult(oudeumasubclassedele).
FazendooacessoàURLhttp://localhost:9000/sobrerecebemosamensagemde
errodafigura2.6,poiscriamosocontrolador,masnãomapeamosarota.
21

## Página 34

2.3.Adicionandoestilo CasadoCódigo
Figura2.6:ErroaoacessarURLsemrotamapeada
V a m o smapeararotadanossanovapágina,adicionandoaoarquivo routesa
seguintelinha:
# método HTTP GET - URI - método que será chamado
GET /sobre controllers.Application.sobre()
Logoapósadicionarmosessalinha,apáginaéexibidacorretamente,apenascom
umtextosimples.
Figura2.7:Páginacriadaqueexibetextosimples
2.3 Adicionando estilo
V a m o sdeixarnossaaplicaçãomaiselegante?Paraisso,vamosaproveitaroexcelente
trabalhodeMarkOttoeJacobThorntoneusaroconjuntodetemplateschamado
Bootstrap.
22

## Página 35

CasadoCódigo Capítulo2. Navegandocomestilo
Começaremosfazendoodownloaddoarquivozipadoemhttps://github.com/
twbs/bootstrap/archive/v3.0.0.zipedescompactando-oemumdiretóriotemporário
(Exemplo: C:\TEMP\).
Em seguida, copiamos o conteúdo do diretório dist (
C:\TEMP\bootstrap-3.0.0\dist\) para o diretório public da nossa
aplicação filmes.
V a m o scriarumtemplateparaanossapáginaSobrecriandoumarquivodentro
de app.viewschamado sobre.scala.html,comoseguinteconteúdo:
@(sistema: String)(versaoDoPlay : String)
AquitemosumacaracterísticabeminteressantedoPlay:conseguimosdefinir
parâmetrosparaonossotemplate–nessecaso,doisdotipo String.
V a m o susaroprimeiroparâmetro, sistema,paradefinirotítulo(title)ea
descrição(h3)dapágina.
<!DOCTYPE html>
<html>
<head>
<title>@sistema</title>
PodemosusarosestilosescriptsdoBootstrapedoPlay.
<link href=
"@routes.Assets.at("bootstrap/css/bootstrap.min.css")"
rel="stylesheet" media="screen">
<link rel="stylesheet" media="screen"
href="@routes.Assets.at("stylesheets/main.css")">
<link rel="shortcut icon" type="image/png"
href="@routes.Assets.at("images/favicon.png")">
<script
src="@routes.Assets.at("javascripts/jquery-1.9.0.min.js")"
type="text/javascript">
</script>
</head>
Porfim,orestantedolayoutdapágina.
<body>
<div class="container">
<div class="header">
23

## Página 36

2.3.Adicionandoestilo CasadoCódigo
<ul class="nav nav-pills pull-right">
<li class="active"><a href="/">Home</a></li>
</ul>
<h3 class="text-muted">@sistema</h3>
</div>
<div class="jumbotron">
<p><a class="btn btn-lg btn-success" href="#">
powered by Play Framework @versaoDoPlay</a></p>
</div>
</div>
</body>
</html>
Logo após a criação desse template, o Play compilouuma classe chamada
views.html.sobre,queusaremosnonossocontroller Applicationdessama-
neira:
public static Result sobre() {
// ok("Sobre");
return ok(views.html.sobre.render(
"Top 100 filmes Cult",
play.core.PlayVersion.current())
);
}
Alémdecriaraclasse views.html.sobre, foicriadotambémométodo
rendercomosdoisparâmetros Stringqueescolhemos.
Logoapósgravarocontroller,semprecisarfazerrestartalgum,façaapenasum
reloadnapáginaeoresultadoseráoseguinte:
Figura2.8:Páginasimplescomestilos
24

## Página 37

CasadoCódigo Capítulo2. Navegandocomestilo
Agoraestámelhor,não?
2.4 Organizando a spáginas
V a m o scontinuarcolocandoummenuereorganizandoaspáginas.
Apáginainicialseráalterada,masvamosantesanalisaraquevemporpadrão.
@(message: String)
@main("Welcome to Play") {
@play20.welcome(message, style = "Java")
}
Alémdeessapáginaterumparâmetrodotipo String,elatambémchamaou-
trotemplate(o main)passandodoisparâmetros:oprimeirodelesdotipo String
eosegundo(entrechaves)dotipoHTML.
Anovapáginainicial inicio.scala.html tambémchamaráotemplate
main,porémpassandoparâmetrosdiferentes:
@main("Top 100 filmes Cult") {
<style>
body {
padding-top: 50px;
}
.starter-template {
padding: 40px 15px;
text-align: center;
}
</style>
<div class="navbar navbar-inverse navbar-fixed-top">
<div class="container">
<div class="navbar-header">
<button type="button" class="navbar-toggle"
data-toggle="collapse" data-target=".navbar-collapse">
</button>
<a class="navbar-brand" href="/">Top 100 filmes Cult</a>
25

## Página 38

2.4. Organizandoaspáginas CasadoCódigo
</div>
<div class="collapse navbar-collapse">
<ul class="nav navbar-nav">
<li><a href="/sobre">Sobre o sistema</a></li>
<li><a href="/play">Sobre o Play Framework</a></li>
<li>
<a href="http://getbootstrap.com/">Sobre o Bootstrap</a>
</li>
</ul>
</div>
</div>
</div>
<div class="container">
<div class="starter-template">
<h1>Top 100 filmes Cult</h1>
<p class="lead">O melhor do cinema est&aacute; aqui !</p>
</div>
</div>
}
Onossosegundopassoécriarumnovocontrollerparachamaronovotemplate:
package controllers;
import play.mvc.Controller;
import play.mvc.Result;
public class Inicio extends Controller {
public static Result index() {
return ok(views.html.inicio.render());
}
}
Eoúltimopassoé,noarquivoderotas,alterarapadrãoparaonovocontroller:
#GET / controllers.Application.index()
GET / controllers.Inicio.index()
Fazendoumreloadnapáginainicialtemoscomoresultadoafigura2.9,mascom
HTMLbemsimples.
26

## Página 39

CasadoCódigo Capítulo2. Navegandocomestilo
Figura2.9:Novapáginaprincipal
OquefaltaéusarosestilosdoBootstrapdentrodotemplate main,jáqueele
seráutilizadoemtodasaspáginas.V a m o sadicionarumalinhachamandoosestilos
logoapósatag title:
<title>@title</title>
<link href="@routes.Assets.at("bootstrap/css/bootstrap.min.css")"
rel="stylesheet"
media="screen">
Fazendoumnovoreloadnapáginainicialtemoscomoresultadocomosestilos
aplicadoscomonafigura:
27

## Página 40

2.5.Próximospassos CasadoCódigo
Figura2.10:Novapáginaprincipalcomestilos
Paracompletar,vamosadicionararotadaantigapáginainicialparaolink“Sobre
oPlay”.Oarquivofinalficouassim:
GET / controllers.Inicio.index()
GET /assets/*file controllers.Assets.at(path="/public", file)
GET /sobre controllers.Application.sobre()
GET /play controllers.Application.index()
2.5 Próximos passos
Certifique-sedequeaprendeu:
•aconfiguraroEclipsecomumaaplicaçãoPlay;
•aestruturadearquivosdeumaaplicação;
•comoalterararotadenavegaçãodepáginas;
•comoaplicarestilos.
Agoraquejátemosumaaplicaçãonavegável,nospróximoscapítulosvamoscriar
oprimeiroCRUDacessandobancodedados.
28

## Página 41

Capítulo3
Persistindoseusdados
Praticamentetodososprincipaissitesdomercadousambancodedadosparamani-
pularsuasinformações, enonossosistemanãoserádiferente.
Nessecapítuloveremoscomdetalhesafacilidadedepersistênciadedadoscom
Playatravésdocadastrodediretoresdeumfilme,descrevendodesdeaclassede
domínio(Model),passandopeloControllereterminandonapáginaJSP(View).
OgerenciadorobjetorelacionaldoPlayéchamadode ebean,queusaopadrão
JPA.SuaimplementaçãoéconhecidaebemdivulgadapelacomunidadeJava.
V a m o siniciarapartedepersistênciadenossosistemaadicionandoumaclasse
importanteparaonossonegócio: Diretor.
Ela precisa ficar dentro do pacote models e estender a classe
play.db.ebean.Model:
package models;
import javax.persistence.*;
import play.data.validation.Constraints;
import play.db.ebean.Model;

## Página 42

CasadoCódigo
ComaanotaçãoEntity,mapeamosaclasseparaumatabela:
@Entity
public class Diretor extends Model {
Emapeamostambémascolunasdessatabela,sendoqueacoluna nomeéobri-
gatória.
private static final long serialVersionUID = 1L;
@Id
public Long id;
@Constraints.Required
public String nome;
Alémdisso,usandoorecurso Model.FinderdoPlay,criaremosavariávelau-
xiliar find,queauxiliaránasconsultaspordiretor:
public static Model.Finder<Long,Diretor> find =
new Model.Finder<Long,Diretor>(Long.class,Diretor.class);
}
Porpadrão,oPlayimplementainternamenteumbancodedadosemH2para
facilitarodesenvolvimento.Precisamosapenasdescomentardoarquivodeconfigu-
ração application.confasseguinteslinhas:
db.default.driver=org.h2.Driver
db.default.url="jdbc:h2:mem:play"
db.default.user=sa
db.default.password=""
ebean.default="models.*"
Logoapóscriarmosaclasse Diretor,aoacessarmosaplicação,oPlaysinaliza
queprecisamosatualizar(oucomoelechama,evoluir)obancodedadosparaalgo
querepresenteasclassesqueforamcriadas.
30

## Página 43

CasadoCódigo Capítulo3.Persistindoseusdados
Figura3.1:Evolutiondoplay
Reparequeafigura3.1mostraumscriptquecriaumatabelaquerepresentafi-
elmenteaclasse Diretor.
Clicandoem apply,oseubancodedadosseráatualizadoemmemória.
Rascunho de CRUD
ComoestamosfazendooController,criaremosapenasosmétodosdonosso
CRUD(C r e a t eRetrieve Update Delete)dediretores.
Inicialmente,anossaclassetemapenasométodo lista,quetraráalistade
todososdiretoresdosfilmes.
package controllers;
import play.mvc.Controller;
import play.mvc.Result;
public class DiretorCRUD extends Controller {
public static Result lista() {
return TODO;
}
}
31

## Página 44

CasadoCódigo
Parachamarométodolista,vamosadicionaràpagina inicio.scala.html
otrechodecódigoaseguir:
<ul class="nav navbar-nav">
<li><a href="/diretor">Diretores</a></li>
<li><a href="/sobre">Sobre o sistema</a></li>
Figura3.2:todoplay
Acessandoapáginainicialdosistema,veremosolink Diretores. Aoclicar
nele,veremosafigura3.2,quemostraateladoplaydeTODO,algoqueémuitoútil
aomontarprojetos!Comcertezaessatelaébemmaiselegantedoquelevarumerro
de Página não encontradadoservidor.
Listando
U m acaracterísticainteressantedoPlayéqueostemplantes,assimcomoosmé-
todosJava,podemterparâmetros.
Precisamos enviar uma lista de diretores para o arquivo
diretor.scala.htmldentrode app.views,queficalogonoinício:
@(diretores: List[Diretor])
Emseguida,chamamosotemplate mainutilizadono2,passandocomoparâ-
metrootítulodapáginaeoseuconteúdoHTML.
32

## Página 45

CasadoCódigo Capítulo3.Persistindoseusdados
@main("Diretores") {
<div class="container">
<div class="header">
<ul class="nav nav-pills pull-right">
Aquicriamosarotaparaocadastrodenovodiretor:
<li class="active">
<a href="@routes.DiretorCRUD.novoDiretor()">
Novo diretor
</a>
</li>
<li class="active"><a href="/">Home</a></li>
</ul>
<h3 class="text-muted">Diretores</h3>
</div>
Nessetrechodefinimosoloopquevaiiterarentrecadadiretor,exibindooseu
nomeeumlinkparaalterarcadaumdeles:
<table class="table table-striped table-bordered" id="example"
cellpadding="0" cellspacing="0" border="0" width="100%">
<tfoot>
@for(diretor <- diretores) {
<tr>
<th>G
<a href="@routes.DiretorCRUD.detalhar(diretor.id)">
@diretor.nome
</a>
</th>
</tr>
}
</tfoot>
</table>
</div>
}
OúltimopassoéconfigurararotadolinkdapáginaparaoController,noarquivo
derotas conf/routes:
GET /diretor controllers.DiretorCRUD.lista()
33

## Página 46

CasadoCódigo
V a m o satualizarométododelistarosdiretoresnonossocontroller:
public static Result lista() {
List<Diretor> diretores = Diretor.find.findList();
return ok(views.html.diretor.render(diretores));
}
Aclasse Diretorestende play.db.ebean.Model,queporsuavez,herda
váriosmétodosquefazemotrabalhocomobancodedados,alémdeimplementar
avariávelauxiliar find.U s a n d oométodo findList,temosalistadetodosos
diretoresarmazenados.
Comisso,temosanossatelafuncionando,mascomoatabelafoirecém-criada,
estávaziaenãotemosnadaparaserexibido.
V a m o saprenderemseguidacomoconfigurarumbancodedados.
Conectando
ParacadarestartdoservidordoPlay,oseubancodedadosserálimponova-
mente.Noiníciododesenvolvimentodeumcadastro,issonãoéumproblema,mas
chegaummomentoemqueosistemanecessitadeumcadastromínimojánobanco
dedadosparafuncionardemaneiraadequada.Criarumcadastrodefilmesemque
éprecisocadastrarosdiretorestodavezéinviável.Poressemotivoprecisamoster
essasinformações pré-cadastradasemumrepositório.
V a m o sagoraconfiguraronossobancodedadosparaconectar-seaoPostgreSQL.
ParainstalaroPostgreSQLeastabelasdonossoexemplo,consulteoapêndice
11.
Novamentenoarquivo application.conf,comentamosaslinhasdoH2a
adicionamosduaslinhasdoPostgreSQL:
#db.default.driver=org.h2.Driver
#db.default.url="jdbc:h2:mem:play"
#db.default.user=sa
#db.default.password=""
db.default.driver=org.postgresql.Driver
db.default.url="postgres://postgres:postgres@localhost/filmes"
V a m o stambémdesativaroevolution,poissemprenoiníciodaaplicação,oPlay
verificaseparacadaclassemodelexisteumatabelaemnossobancodedados,eo
nossoPostgreSQLjáestácorretamenteconfigurado.
34

## Página 47

CasadoCódigo Capítulo3.Persistindoseusdados
# Evolutions
# ~~~~~
# You can disable evolutions if needed
evolutionplugin=disabled
Pl a yevolution
NotequeoPlaycriaautomaticamenteumscriptSQLparacadamu-
dançaqueforfeitanoseumodelo. Façaumrefreshdoseuprojetono
workspacedoEclipsecom F5eprocurepeloarquivo 1.sqldentrodo
diretório conf-evolutions-default.
Figura3.3:Playdatabasedriver
Acessandonovamenteaaplicação,deparamo-noscomoerrodafigura3.3,que
mostraqueexisteumadependênciadanossaaplicaçãocomodriverJDBCdoPost-
greSQL.
Pararesolveresseproblemadedependência,editeoarquivo build.sbtadici-
onandoalinhado postgresqlconformeoexemplo:
name := "filmes"
35

## Página 48

CasadoCódigo
version := "1.0-SNAPSHOT"
libraryDependencies ++= Seq(
javaJdbc,
javaEbean,
cache,
"postgresql" % "postgresql" % "9.1-901-1.jdbc4"
)
play.Project.playJavaSettings
Aofazerorestartdoservidor,notenologqueodownloaddodriverfoifeito(e
guardadodentrododiretóriodoPlay):
fb@cascao ~/workspace-play/filmes > play run
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
...
[info] downloading http://repo1.maven.org/maven2/postgresql/postgresql
/9.1-901-1.jdbc4/postgresql-9.1-901-1.jdbc4.jar ...
[info] [SUCCESSFUL]
postgresql#postgresql;9.1-901-1.jdbc4!postgresql.jar
(1683ms)
...
Figura3.4:Listadediretores
Eapáginadediretoresfinalmenteécarregadadobancodedadosconformea
figura3.4.
Cadastrando
V a m o sadicionarocadastrodediretor.Paraisso,vamosseguirospassospara
construirumatelanoPlay:
36

## Página 49

CasadoCódigo Capítulo3.Persistindoseusdados
1)CriarummétodonoController;
2) Criarumapáginatemplatedentrodopacoteviews;
3)ConfigurarnoarquivoderotasomapeamentodaURIparaocontroller.
Paratratarcomtelasdecadastroeseusformulários,oPlaytemumobjetocha-
mado Formqueencapsulapartedacomplexidadedetrabalharcomformuláriosem
HTML.
Napartedocontroller,vamosadicionarumobjetodotipo Formparadiretor:
private static final Form<Diretor> diretorForm =
Form.form(Diretor.class);
Emseguida,vamosadicionardoismétodos,oprimeiroqueapenaschamaatela
decadastro:
public static Result novoDiretor() {
return ok(views.html.novoDiretor.render(diretorForm));
}
Jáoosegundofazagravaçãonobancodedados.V a m o sverporpartes.Inicial-
menteavariávelformretornaráasinformações dodiretor:
public static Result gravar() {
Form<Diretor> form = diretorForm.bindFromRequest();
Emseguida,échamadoométodoqueverificaseo Formveiocomalgumerrode
validação,porexemplo,umcampoobrigatórionãopreenchido.Casoocorraalgum
errodepreenchimento,oPlayautomaticamenteavisacomumamensagemnatela.
Paraexatamenteessanecessidade,oPlaytemumescopochamado flash,noqual
asinformações nelecolocadasestão disponíveisapenasemumarequisição. Com
isso,adicionamosasmensagensde sucessoou erro,queserãoexibidasnatela
conformeanecessidade.
Paraasuaexibiçãocorreta,dentrodotemplate main.scala.htmltemosas
chamadas:
37

## Página 50

CasadoCódigo
@if(flash.containsKey("sucesso")) {
<div class="alert alert-success">
@flash.get("sucesso")
</div>
}
@if(flash.containsKey("erro")) {
<div class="alert alert-danger">
@flash.get("erro")
</div>
}
Emseguida,seoformuláriopossuirerros,enviamosamensagemadequada.
if (form.hasErrors()) {
flash("erro","Foram identificados problemas no cadastro");
return ok(views.html.novoDiretor.render(diretorForm));
}
Depoistemosarotinadegravarosdadosnobanco,lembrandoqueaclasse
Diretorherdouométodo save,quefaztodootrabalhodepersistência.
Diretor diretor = form.get();
diretor.save();
// equivalete a ===> form.get().save();
Efinalmentetemosumregistrodeumamensagemqueseráexibidanapágina,
juntocomoredirecionamentoparaarotaadequada.
flash("sucesso","Registro gravado com sucesso");
return redirect(routes.DiretorCRUD.lista());
}
Nocomeçodoarquivodetemplate,informamosqueeletemcomoparâme-
troumobjetodotipo Form. Lembrandoqueostemplatesestão nalinguagem
Scala, a sintaxeéum pouco diferente: Form[Diretor] em Scala éigual a
Form<Diretor>emJava.
@(diretorForm : Form[Diretor])
38

## Página 51

CasadoCódigo Capítulo3.Persistindoseusdados
@main("Novo diretor") {
<div class="container">
<div class="header">
<ul class="nav nav-pills pull-right">
<li class="active"><a href="/">Home</a></li>
</ul>
</div>
<div>
Aquiusamosohelperparafazerachamadadoformulárioaonossométodode
gravardentrodocontroller.
@helper.form(action=routes.DiretorCRUD.gravar()) {
<form class="form-horizontal">
<fieldset>
<legend>Novo diretor</legend>
Alémdisso,eleéusadoparainformarotipodeentradadedadosparaonome
dodiretor.
<div class="control-group">
<div class="controls">
@helper.inputText(diretorForm("nome"))
<p class="help-block">informe o nome do diretor</p>
</div>
</div>
}
<div class="control-group">
<label class="control-label" for="singlebutton"></label>
<div class="controls">
<button id="singlebutton" name="singlebutton"
class="btn btn-primary">
Gravar
</button>
</div>
</div>
</div>
}
39

## Página 52

CasadoCódigo
Finalmentevamosadicionararotadessecadastro.Notequeparagravarestamos
usando POST:
GET /diretor/novo controllers.DiretorCRUD.novoDiretor()
POST /diretor/ controllers.DiretorCRUD.gravar()
Figura3.5:Novocadastrodediretor
Aoclicarnolinkdenovodiretor,veremosumatelacomonafigura3.5.
40

## Página 53

CasadoCódigo Capítulo3.Persistindoseusdados
Figura3.6:Cadastrodediretorfeitocomsucesso
Depoisdocadastro,éexibidaamensagemdesucesso,comonafigura3.6.
Detalhando, alterando e removendo
Ométododocontrollerdedetalharémaissimples,éumabuscaseguidadeum
redirecionamento:
public static Result detalhar(Long id) {
Form<Diretor> dirForm =
form(Diretor.class).fill(Diretor.find.byId(id));
return ok(views.html.alterarDiretor.render(id,dirForm));
}
Ométododocontrollerdealterarésemelhanteaodecadastrar–adiferençaé
quechamamosométodo updateaoinvésde save:
public static Result alterar(Long id) {
form(Diretor.class).fill(Diretor.find.byId(id));
Form<Diretor> alterarForm = form(Diretor.class).bindFromRequest();
if (alterarForm.hasErrors()) {
return badRequest(
views.html.alterarDiretor.render(id,alterarForm));
}
alterarForm.get().update(id);
flash("sucesso","Diretor "
+ alterarForm.get().nome + " alterado com sucesso");
41

## Página 54

CasadoCódigo
return redirect(routes.DiretorCRUD.lista());
}
Eoderemoverapenaschamamosométodo delete:
public static Result remover(Long id) {
Diretor.find.ref(id).delete();
flash("sucesso","Diretor removido com sucesso");
return lista();
}
Ocontrollerdealteração receberáosparâmetrosde ide Form<Diretor>.
Notequeeleutilizaumaopçãodiferentedohelper,comimport(tambémaquitemos
umapequenadiferençanasintaxe;emScala import helper._éequivalentea
import helper.*emJava).
@(id: Long, diretorForm: Form[Diretor])
@import helper._
@main("Alterar diretor") {
<div class="container">
<div class="header">
<ul class="nav nav-pills pull-right">
<li class="active"><a href="/">Home</a></li>
</ul>
</div>
<h1>Alterar diretor</h1>
Aquidefinimosachamadaaométodoalterardocontroller,etambémvoltamos
paraalistagemseforescolhidaaopçãocancelar:
@form(routes.DiretorCRUD.alterar(id)) {
<fieldset>
@inputText(diretorForm("nome"), ’_label -> "Nome do diretor")
</fieldset>
42

## Página 55

CasadoCódigo Capítulo3.Persistindoseusdados
<div class="control-group">
<div class="actions">
<input type="submit" value="Gravar" class="btn btn-primary">
<a href="@routes.DiretorCRUD.lista()" class="btn btn-primary">
Cancelar
</a>
}
Aquidefinimosaopçãoderemoverodiretor,chamandoorespectivométodo
docontroller.
@form(routes.DiretorCRUD.remover(id)) {
<input type="submit" value="Remover esse diretor"
class="btn danger">
}
</div>
</div>
</div>
}
Aúltimaparteédefinirasrotasrestantes,portantotodasasrotasdediretorsão:
GET /diretor controllers.DiretorCRUD.lista()
GET /diretor/novo controllers.DiretorCRUD.novoDiretor()
GET /diretor/:id controllers.DiretorCRUD.detalhar(id: Long)
POST /diretor/:id controllers.DiretorCRUD.alterar(id:Long)
POST /diretor/ controllers.DiretorCRUD.gravar()
POST /diretor/:id/remover controllers.DiretorCRUD.remover(id:Long)
43

## Página 56

3.1.Próximospassos CasadoCódigo
Figura3.7:Cadastrodediretorfeitocomsucesso
Ateladealteraçãoficarácomonafigura3.7,eexibirámensagensapósalterarou
removeralgumregistrodediretor.
PercebaqueforamcriadosváriostemplatesdesseCRUDparaficarbemclaroo
papeldecadaoperação.Massenecessário,épossíveldiminuironúmerodelesunifi-
candoalgumasoperações, comoporexemploaoperaçãodenovodiretorealteração
dediretornomesmotemplate.
3.1 Próximos passos
Certifique-sedequeaprendeu:
•avisãogeraldoEbean(APIdepersistência)doPlayFramework;
•comousaroobjeto F o r mdoPlay;
•comotrabalharcomtemplateseformuláriosdoPlay;
•comoadicionarrotascomGETePOST.
Agoraquejátemosumprodutorazoavelmenteviávelcriado,vamospublicarnas
nuvensparaficaracessívelemqualquerlugardomundo!
44

## Página 57

Capítulo4
Publicandoemqualquerlugar
Parapublicarnossaaplicação(oufazerdeploy)noPlaytemosalgunscenáriosdis-
tintos.
OPlayutilizaumservidorbaseadonoNetty,queéleveerobusto,suportando
HTTPeHTTPS.
4.1 Redelocal
Damesmamaneiraquefoimostradonoscapítulosanteriores,umsimples play
runésuficienteparapublicarsuaaplicaçãorapidamentenaredelocal.
SedesejarrodaremoutraportaHTTP,éprecisousarumparâmetroespecífico
play -Dhttp.port=<número-da-porta> run:
fb@cascao ~/workspace-play/filmes > play -Dhttp.port=9999 run
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
[info] Set current project to filmes (in build

## Página 58

4.2. ServidorJavaEE CasadoCódigo
file:/home/fb/workspace-play/filmes/)
--- (Running the application from SBT, auto-reloading is enabled) ---
[info] play - Listening for HTTP on /0.0.0.0:9999
(Server started, use Ctrl+D to stop and go back to the console...)
Nocasodasaídaanterior,foiusadoo -Dhttp.port=9999.
4.2 Servidor Ja v aEE
A t éaversãodoPlay2.1.4erapossíveloficialmentegerarumpacoteW A Rquerodasse
emumservidorcomoA p a c h eT o m c a touJBoss,masnasversões posterioresissofoi
descontinuado.
Existeopluginnãooficial play2-war-pluginquefazaconversão,masnão
converte100%.Elenãosuporta,entreoutrascoisas,WebSockets.
U mWebSocketéumaimplementação demensagemassíncrona,bidirecional
(full-duplex)emcimadeumaconexãoTCP,quefoiespecificadanoJavapelaJSR
356.
SeusarWebSocketforessencial,entãooficialmenteaúnicamaneiraderodaré
atravésdoservidordoPlay.
4.3 Deployn a nuvem
Nãoseriaumabsurdosetodomêsfossecobradaumataxafixadetrezentosreais
deenergiaelétrica,independentedouso?Entretanto,quandosepagaporumser-
viçodehospedagem,éexatamenteoqueacontece,poisositeficanoar,indepen-
dentedousodosrecursosporumaquantiamensalfixa.Paramudaressecenário,
surgiuoconceitodecloudcomputing(computaçãoemnuvem),segundooqualos
serviçossão pagospelouso,proporcionandoinúmerasvantagens:todaapartede
infraestrutura(rede,armazenamentodearquivos,bancodedados,segurança)éde
responsabilidadedaprestadoradeserviços,eocrescimentodousodeserviçosé
pagoproporcionalmente,oque,emtermosdecusto,éumaexcelenteopção.
ParacolocaroPlaynanuvem,existemváriasopçõesoficialmentedocumentadas,
comoCloudbees,CloudFoundryeCleverCloud.
V a m o sfocaronossoexemplono H e r o k u.
46

## Página 59

CasadoCódigo Capítulo4. Publicandoemqualquerlugar
Primeiros passsos no Heroku
Acesseositehttps://www.heroku.com/ecrieumacontagratuita.
Depoisdisso,acessehttps://toolbelt.heroku.com/ebaixeoconjuntodeferra-
mentasparaoseusistemaoperacional.
TudonoHerokusefazcomesseconjuntodeferramentas,ealgumascoisastam-
bémépossívelfazerpelosite.
Figura4.1:CriandoumaaplicaçãonoHeroku
Pelositeépossívelcriarumaaplicaçãoweb.V a m o scriarumaaplicaçãochamada
“play-capitulo4”conformeafigura4.1. Nesseexemplofoicriadaaaplicação p l ay -
capitulo4. Crieumnomeparecido,comoporexemplo <seu-usuario-no-Heroku>-
p l ay.
47

## Página 60

4.3.Deploynanuvem CasadoCódigo
Banco de dados
Figura4.2:Adicionandofuncionalidadesàsuaaplicação
Emseguida,adicionaremosumamelhoriaaositeclicandonaopção Get add-ons
conformeafigura4.2.
Figura4.3:EscolhendoPostgreSQLparasuaaplicação
Nalistadeopções, escolhaobancodedadosPostgreSQLconformeafigura4.3.
48

## Página 61

CasadoCódigo Capítulo4. Publicandoemqualquerlugar
Figura4.4:Adicionandofuncionalidadesàsuaaplicação
Escolhendoaopção Hobby Deveassociadaàaplicaçãorecém-criada,teremos
umaaplicaçãogratuitacomobancodedadosPostgreSQLdisponívelcomsuporte
a20conexões simultâneasetabelascomnomáximo10.000linhas(figura4.4).O
HerokutrabalhapreferencialmentecomPostgreSQL,masoferecetambémoutras
opções comoMySQL,MongoDB,Neo4J;éprecisoconsultarnositeosplanosexis-
tentes,masamaioriadelesofereceumgratuitodeteste.
Épossívelescolherumplanocombancodedadosdemaiorcapacidade,mas
nessecasoserácobradaumataxapropocionalaotamanhoescolhido.Existemoutras
variações também:oMySQL,porexemplo,cobradezdólaresporumbancodeum
gigabyte;jáoPostgreSQL,cobranovedólaresporumbancocomdezmilhões de
linhas,independentedeseutamanho.
49

## Página 62

4.3.Deploynanuvem CasadoCódigo
Figura4.5:Adicionandofuncionalidadesàsuaaplicação
Depoisdecriado,obancodedadosapareceránalistade add-onsdasuaapli-
cação. Paraobterinformações deacessoaobancodedados,cliquenolink H e r o k u
P o s t g r e sHobby Dev paraexibirumatelasemelhanteàfigura4.5.
C a r g ade dados
Obancodedadosfoicriadocomsucesso,masestávazioeprecisadastabelasde
filmesediretoresparaocorretofuncionamentodaaplicação.
Depoisdebaixarmososcriptdehttp://bit.ly/JLFA9C,chamaremosoprograma
psqlparafazeracargadedados.
OpsqléumprogramaquefazpartedoPostgreSQLeéointerpretadordecoman-
dosSQLemmodotexto,ouseja,éelequeenviaoscomandosSQLparaobancode
dados.Noapêndice11mostramosoPgAdmin3,queéointerpretadordecomandos
SQLemmodográfico.
Asintaxesimplificadadopsqlé:
<diretório-de-instalação-postgresql>/psql
-h <servidor>
-U <usuário>
50

## Página 63

CasadoCódigo Capítulo4. Publicandoemqualquerlugar
-d <banco-de-dados>
-p <porta> < <arquivo-SQL>
Exemploacessandoumbancodedadoslocalchamado filmes:
C:\Program Files\PostgreSQL\9.3\bin>psql -U postgres -h
localhost -d filmes -p 5432
psql (9.3.1)
WARNING: Console code page (437) differs from Windows code page (1252)
8-bit characters might not work correctly. See psql reference
page "Notes for Windows users" for details.
Type "help" for help.
filmes=#
Exemploacessandoumbancodedadosnanuvemerodandoumscriptdeco-
mandosSQL:
C:\Program Files\PostgreSQL\9.3\bin\psql
-h ec2-23-23-81-171.compute-1.amazonaws.com
-U bcgtehhaqzonak
-d d98lmbl09e2843
-p 5432 < C:\SQL\banco-filmes-postgresql.sql
Senha para usuário bcgtehhaqzonak:
CREATE TABLE
CREATE TABLE
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
...
Depoisdeexecutadooscript,foramcriadasduastabelasemnossobancode
dadosepopuladascomalgunsregistros.
Acessandonovamenteateladafigura4.5,verificamosqueaquantidadedetabe-
lasaumentoudezeroparadois,oquecomprovaaexecuçãodoscriptcomsucesso.
51

## Página 64

4.3.Deploynanuvem CasadoCódigo
Deploy da a p l i c ação
Paraoprocessodedeploy(publicação) daaplicação, precisamoscriarumar-
quivodeconfiguraçãodoPlay,diferenciadoparaesseambiente,eoutroarquivoque
orientaoHerokucomosubiraaplicação.
No diretório de configurações (o mesmo que se encontra o
application.conf), criaremos o arquivo heroku.conf com as informa-
ções deacessoaobancodedados:
include "application.conf"
# db.default.url="postgres://usuario:senha@servidor/nomeDoBanco"
db.default.url=
"postgres://bcgtezonak:senha@comp.amazonaws.com/d98lmbl09e2843"
Depoisdisso,naraizdoprojetocriaremosoarquivo Procfilecontendoas
informações
web: target/universal/stage/bin/filmes
-Dhttp.port=$PORT
-Dconfig.resource=heroku.conf
ParausarosserviçosdoHeroku,éprecisoinstalaroseuconjuntodeferramentas,
disponívelparadownloademhttps://toolbelt.heroku.com/,quecontémosprogra-
mas herokue git.
NoHerokunãoexisteoconceitodestopestartdoservidor,issoéfeitoquando
vocêcommitaalgumaalgumaalteraçãonoseucódigo.
Portanto,basicamenteprecisamosnoslogarnoHerokuconformeoexemplo:
fb@cascao ~/workspace-play/filmes-cap04 > heroku auth:login
Enter your Heroku credentials.
Authentication successful.
fb@cascao ~/workspace-play/filmes-cap04 >
Emseguida,adicioneoseuprojetoaodoHerokupelogit:
git remote add heroku git@heroku.com:play-capitulo4.git
Eparaconferirsefoiadicionadocorretamente,oservidordeveaparecercon-
formeoexemplo:
52

## Página 65

CasadoCódigo Capítulo4. Publicandoemqualquerlugar
fb@cascao ~/workspace-play/filmes-cap04 > git remote -v
heroku git@heroku.com:play-capitulo4.git (fetch)
heroku git@heroku.com:play-capitulo4.git (push)
Suporte a oJa v a7
SedesejarquenoHerokuasuaaplicaçãorodecomoJava7 ,adicione
naraizdoprojetoumarquivochamado system.propertiescontendouma
únicalinha: java.runtime.version=1.7.
Depoisdisso,precisamosapenascommitarasalterações eenviarparaoHeroku
peloGit,orestanteseráfeitoautomaticamente.
fb@cascao ~/workspace-play/filmes-cap04 > git commit -a -m "capitulo-04"
fb@cascao ~/workspace-play/filmes-cap04 > git push heroku master
Enter passphrase for key ’/home/fb/.ssh/id_dsa’:
warning: no threads support, ignoring --threads
Counting objects: 5, done.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 287 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
-----> Play 2.x - Java app detected
-----> Installing OpenJDK 1.7...done
-----> Running: sbt clean compile stage
Getting org.scala-sbt sbt 0.13.0 ...
...
[info] Done packaging.
[success] Total time: 6 s, completed Nov 23, 2013 1:15:21 AM
-----> Dropping ivy cache from the slug
-----> Dropping project boot dir from the slug
-----> Dropping compilation artifacts from the slug
-----> Discovering process types
Procfile declares types -> web
-----> Compiled slug size: 98.3MB
-----> Launching... done, v9
53

## Página 66

4.4. Próximospassos CasadoCódigo
http://play-capitulo4.herokuapp.com deployed to Heroku
To git@heroku.com:play-capitulo4.git
e43afcf..aea7172 master -> master
Em seguida, acessando o link http://play-capitulo4.herokuapp.com/ (ou
http://<seu-usuario-no-Heroku>-play.herokuapp.com/)veremosanossaaplicação
funcionandoperfeitamenteconformeafigura4.6.
Figura4.6:Aplicaçãonanuvem
4.4 Próximos passos
Certifique-sedequeaprendeu:
•amudaraportaHTTPdoservidordoPlay;
•acriarumaaplicaçãonoHeroku;
•acriarepopularumabasededadosPostgreSQLnoHeroku;
•aconfigurarumaaplicaçãoPlaypararodarnoHeroku.
AgoraquefinalizamosoQuickstart,vamosaprenderamelhorarnossaaplicação
nospróximoscapítulos.
54

## Página 67

Capítulo5
Melhorandooinputdousuário
Onossosistemaaindatemalgunsproblemas:nãoexistecadastrodefilmeseseten-
tarmosremoveralgumdiretor,ocorreoerrodafigura5.1.
Figura5.1:Playcomerrodevalidação
V a m o scriarocadastrodefilmesusandomaiscomponentes,masdessavezcus-

## Página 68

CasadoCódigo
tomizandoospróprioshelpersexistentesdoPlayparaonossoproveito.
AclasseControllerdonossoCRUDserábemsemelhanteàdeDiretor,apenas
nalistainicialvamosordernarosfilmespeloano,porissochamaremosométodo
passandooparâmetroquedesejamosordenar:
public class FilmeCRUD extends Controller {
public static Result lista() {
List<Filme> filmes = Filme.find.where()
.orderBy("ano").findList();
return ok(views.html.filme.render(filmes));
}
Notetambémométodogravar,queébemsemelhanteaodeDiretor,apesarde
gravarmuitomaiscampos.Essafacilidadeacontecelogonaprimeiralinha,quando
ométodobindFromRequestrelacionaoscamposinformadosnatelacomoobjeto
form.
public static Result gravar() {
Form<Filme> form = filmeForm.bindFromRequest();
if (form.hasErrors()) {
flash("erro",
"Foram identificados problemas no cadastro de filme");
List<Diretor> diretores = Diretor.find.findList();
return ok(views.html.novoFilme.render(filmeForm,diretores));
}
form.get().save();
flash("sucesso","Registro gravado com sucesso");
return redirect(routes.FilmeCRUD.lista());
}
Depois bindFromRequest, temos a validação dos campos com o
form.getErrors. Se existir algum erro, éexibida a mensagem colocando
noescopoflash.
56

## Página 69

CasadoCódigo Capítulo5.Melhorandooinputdousuário
Emseguida,umapequenaotimização decódigo: chamamosométodo save
diretodo formparagravaroregistro.
Figura5.2:Cadastrodeumfilme
Paraexibirmosateladafigura5.2,usaremosomesmohelperexistente,porém
vamoscustomizarcriandoumarquivodetemplate campo.scala.htm.
Aquicolocamosos diveestilosconformeoestilodoBootstrap3:
@(elements: helper.FieldElements)
<div class="@if(elements.hasErrors) {error} else {form-group}">
<label for="@elements.id" class="col-sm-2 control-label">
@elements.label
</label>
<div class="col-sm-10">
@elements.input
</div>
</div>
Enoarquivo novoFilme.scala.htmlexistemdoisparâmetros,oformulário
defilmesealistadediretores,queseráutilizadaemumcombo.
57

## Página 70

CasadoCódigo
@(filmeForm : Form[Filme],diretores: List[Diretor])
@implicitField = @{ FieldConstructor(campo.f) }
@import helper._
Essetrechonãoapresentanovidades,apenasaschamadasdoformulárioeolink
paraapáginainicial.
@main("Novo filme") {
<div class="container">
<ul class="nav nav-pills pull-right">
<li class="active"><a href="@routes.FilmeCRUD.lista()">Home</a></li>
</ul>
<div class="row clearfix">
<div class="col-md-12 column">
@form(action=routes.FilmeCRUD.gravar(),’class->"form-horizontal") {
<fieldset>
<legend>Novo filme</legend>
Aquiusamosdoishelpersparamontaroscomponentesdatela:o @inputText
parageraroscampostextodonome,duraçãoegênerodofilme,e @selectpara
montaroscombosdediretoreano.
@select(
filmeForm("ano"),
options(Filme.anoOptions),
’_label -> Messages("filme.ano"),
’_default -> "-- Ano --"
)
@inputText(filmeForm("nome"),’_label -> "Filme")
@select(
filmeForm("diretor.id"),
options(Diretor.options),
58

## Página 71

CasadoCódigo Capítulo5.Melhorandooinputdousuário
’_label -> "Diretor", ’_default -> "-- Diretor --"
)
@inputText(filmeForm("duracao"),’_label -> "Duração")
@inputText(filmeForm("genero"),’_label -> "Gênero")
Aquifinalizamosoarquivosemnovidades,comosbotões degravarecancelar
semelhantesaodateladediretor.
</fieldset>
<div class="form-group">
<label class="col-md-3 col-md-3 control-label"
for="singlebutton"> </label>
<div class="col-lg-6">
<button id="singlebutton" name="singlebutton"
class="btn btn-primary">
Gravar
</button>
<a href="@routes.FilmeCRUD.lista()" class="btn btn-primary">
Cancelar
</a>
</div>
</div>
}
</div>
}
Namaioriadastelastemosalgunstextosemcomum,comoapalavra Homeou
Gravar. Paraalterarde“Gravar”para“Efetivar”nosistema,énecessárioalterar
manualmenteemtodasaspáginas.
Parafacilitaressetipodetrabalho,oPlaypermiteisolartodasasmensagensem
umúnicoarquivo,oquesimplificaamanutençãodosistema.
5.1 Isolando mensagens
Paraconfigurarmosonossosistemaparaisolarasmensagens,bastaeditarmoso
arquivo application.confparaadicionarmososidiomassuportados:
59

## Página 72

5.1.Isolandomensagens CasadoCódigo
#application.langs="en"
application.langs="en,pt"
Emseguida,nomesmodiretóriodoarquivodeconfiguraçãoanterior,criaremos
umarquivodemensagenscomaextensãodoidiomasuportado.
Paraanossaaplicação,usaremosoarquivo messages.pt:
#
# Mensagens
#
# globais
global.home=Home
global.erro=Erro interno do sistema
global.gravar=Gravar
global.cancel=Cancelar
# filme
filme.duracao=Duração
filme.novo=Novo filme
filme.ano=Ano
filme.nome=Filme
filme.diretor=Diretor
filme.nome.hint=informe o nome do filme
filme.genero=Gênero
filme.ano.combo=-- Ano --
filme.diretor.combo=-- Diretor --
Comessaalteração,oarquivo novoFilme.scala.htmlficariaassim:
@(filmeForm : Form[Filme],diretores: List[Diretor])
@implicitField = @{ FieldConstructor(campo.f) }
@import helper._
@main(Messages("filme.novo")) {
<div class="container">
<ul class="nav nav-pills pull-right">
<li class="active">
60

## Página 73

CasadoCódigo Capítulo5.Melhorandooinputdousuário
<a href="@routes.FilmeCRUD.lista()">
Home
</a>
</li>
</ul>
<div class="row clearfix">
<div class="col-md-12 column">
@form(action=routes.FilmeCRUD.gravar(),’class->"form-horizontal") {
<fieldset>
<legend>@Messages("filme.novo")</legend>
@select(
filmeForm("ano"),
options(Filme.anoOptions),
’_label -> Messages("filme.ano"),
’_default -> Messages("filme.ano.combo")
)
@inputText(filmeForm("nome"),
’_label -> Messages("filme.nome"))
@select(
filmeForm("diretor.id"),
options(Diretor.options),
’_label -> Messages("filme.diretor"), ’_default ->
Messages("filme.diretor.combo")
)
@inputText(filmeForm("duracao"),
’_label -> Messages("filme.duracao"))
@inputText(filmeForm("genero"),
’_label ->Messages("filme.genero"))
</fieldset>
<div class="form-group">
61

## Página 74

5.2.Tratandoerros CasadoCódigo
<label class="col-md-3 col-md-3 control-label"
for="singlebutton"> </label>
<div class="col-lg-6">
<button id="singlebutton" name="singlebutton"
class="btn btn-primary">
@Messages("global.gravar")
</button>
<a href="@routes.FilmeCRUD.lista()"
class="btn btn-primary">
@Messages("global.cancel")
</a>
</div>
</div>
}
</div>
}
Alémdeusarmoso @Messagesparatrocarostextosnatela,tambémtroca-
mososvalorestextopassadoscomoparâmetro,comofoifeitonoiníciosubstituindo
@main("Novo filme") por @main(Messages("filme.nome")).
5.2 Tratando erros
Setentarmosremoveralgumdiretor,ocorreoerrodafigura5.1.
Paracorrigirmosesseproblema,bastatratarmosqualquertipodeExceptione
devolvermosparaatelaumamensagempadrão.
Naclasse DiretorCRUD,alteramosarotinaderemoverdiretoradicionandoo
tratamentoadequado:
public static Result remover(Long id) {
try {
Diretor.find.ref(id).delete();
flash("sucesso","Diretor removido com sucesso");
} catch (Exception e) {
flash("erro",play.i18n.Messages.get("global.erro"));
}
return lista();
}
Comisso,obteremosoresultadoesperadocomumamensagemamigávelao
usuário,comomostraafigura5.3.
62

## Página 75

CasadoCódigo Capítulo5.Melhorandooinputdousuário
Figura5.3:Playcomerrodevalidaçãotratado
5.3 Páginas customizadas
Figura5.4:Páginanãoencontradapadrão
SetentarmosacessarumaURLquenãoexiste,oPlayautomaticamentelistatodasas
actionsexistentes,comonafigura5.4.
Entretanto,nãoéinteressantedeixarissocomopadrão,poismostra(demaneira
nadasegura)asdiferentesmaneirasdeacessoàaplicação,alémdeconfundirousuá-
rioenãoexibirumlinkpararetornar.
Felizmente,essecomportamentopodeserfacilmentealteradosobrescrevendo
comaclasse GlobalSettings,queéresponsávelpordefiniropções globaisao
sistematodo.
63

## Página 76

5.3.Páginascustomizadas CasadoCódigo
Paraalteraressasconfigurações, bastacriarmosumaclassechamada Globale
estender GlobalSettings.
Se,porexemplo,desejarmosexibirumavisoquandoaaplicaçãosubir,bastaso-
brescrevermosométodo:
import play.*;
public class Global extends GlobalSettings {
@Override
public void onStart(Application app) {
System.out.println("Top 100 filmes cult no ar!");
}
}
Entretanto,parasobrescreverosmétodos,devemosobedeceràAPIdoPlay,uti-
lizandoamesmaassinaturadosmétodosconformeadocumentaçãoemhttp://www.
playframework.com/documentation/2.2.1/api/java/play/GlobalSettings.html.
Parasobrescreverocomportamentodepáginanãoencontrada,precisamosusar
aassinaturacomretornodotipo Promise<SimpleResult>(Promiseeéuma
classeinternaemScaladoPlay,ePromise.pureusadodentrodométodotambém):
import static play.mvc.Results.notFound;
import play.GlobalSettings;
import play.libs.F.Promise;
import play.mvc.Http.RequestHeader;
import play.mvc.SimpleResult;
public class Global extends GlobalSettings {
@Override
public Promise<SimpleResult> onHandlerNotFound(
RequestHeader request) {
return Promise.<SimpleResult> pure(
notFound(views.html.paginaNaoEncontrada.render(request.uri()))
);
}
}
64

## Página 77

CasadoCódigo Capítulo5.Melhorandooinputdousuário
E essa classe utiliza a seguinte página customizada,
paginaNaoEncontrada.scala.html:
@(url: String)
<html>
<body>
<h1>Oops, essa p&aacute;gina n&atilde;o existe...</h1>
<p>@url</p>
<p> <a href="/">Top 100 filmes Cult</a></p>
</body>
</html>
Eobtemosoresultadodafigura5.5:
Figura5.5:Páginanãoencontradacustomizada
5.4 Próximos passos
Certifique-sedequeaprendeu:
•autilizaroshelpersdeinputdeformuláriosdoPlay;
•aisolarasmensagensdaaplicação;
65

## Página 78

5.4.Próximospassos CasadoCódigo
•acustomizarpáginapadrãodosistema.
Agoraquejátemosumavalidaçãodeentradamelhorada,vamosexporalguns
serviçosdenossosistemaeacessá-losexternamente.
66

## Página 79

Capítulo6
Criandoserviços
Quandoacessamosumsitecomumcelular,pormaismodernoqueeleseja,nãoéa
mesmacoisaquecomodesktop,principalmentepelotamanhodatela.
Comissosurgeanecessidadededisponibilizarmosasinformações dositede
umamaneiramaisamigávelparaqueumaaplicaçãodecelularuseessesdadoscomo
bementender.
Poressemotivo,vamosmostraraquicomopodemosfacilmentedisponibilizar
asinformações ecomoacessardeumaaplicaçãoAndroid.
6.1 Acessando serviço viaweb
Existemdiversasmaneirasdedisponibilizarasinformações donossosite,vamos
tratardosdoisformatosmaiscomuns:XMLeJSON(JavaScript Object Notation).
Começaremoscriandoumcontrollerchamado Servicesespecíficoparaesses
doisserviços,ambosusamamesmarotinadeobteralistadefilmesordenadospelo
ano:

## Página 80

6.1.Acessandoserviçoviaweb CasadoCódigo
public class Services extends Controller {
private static List<Filme> getFilmesOrderByAno() {
return Filme.find.where().orderBy("ano").findList();
}
}
ParaexibirmosalistadefilmesemXML,formatamosoretornomanualmente:
public static Result listaFilmesEmXML() {
List<Filme> filmes = getFilmesOrderByAno();
return ok("<message \"status\"=\"OK\"> "
+ filmes.toString() + "</message>");
}
ParaexibiroresultadoemJSON,usamosarotinaauxiliar Json.toJsonpara
formataralistadefilmes.
public static Result listaFilmesEmJSON() {
List<Filme> filmes = getFilmesOrderByAno();
return ok(Json.toJson(filmes));
}
AcessandoaURLhttp://<ip-da-sua-maquina>:9000/filmesJSONviabrowser,
vemosasinformações dofilmecomomostraafigura6.1.
68

## Página 81

CasadoCódigo Capítulo6. Criandoserviços
Figura6.1:ListadefilmesemformatoJSON
Entretanto,estamosaquidividindoosistemaemduaspartes,aquedisponibiliza
serviços(aweb)eaqueconsomeosserviços(amobile–Android),eprecisamos
verificarseonossoserviçoestáfuncionandocorretamente.
U m amaneiraeficazdefazeressaverificaçãoédepurar(oudebugar)aaplicação
econferirseosdadosenviadosestãocorretos.
Portanto,vamosrapidamenteconfiguraroEclipseparadepuraranossaaplica-
ção.
6.2 Debugando p e l oEclipse
Jásabemosqueparasubiraaplicaçãousamosnoconsoleocomando play run:
fb@cascao ~/workspace-play/filmes > play run
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
[info] Set current project to filmes
(in build file:/home/fb/workspace-play/filmes/)
--- (Running the application from SBT, auto-reloading is enabled) ---
[info] play - Listening for HTTP on /0.0.0.0:9000
(Server started, use Ctrl+D to stop and go back to the console...)
Parasubiremmododebug,usamosnoconsoleocomando play debug run:
69

## Página 82

6.2. DebugandopeloEclipse CasadoCódigo
fb@cascao ~/workspace-play/filmes > play debug run
Listening for transport dt_socket at address: 9999
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
[info] Set current project to filmes
(in build file:/home/fb/workspace-play/filmes/)
--- (Running the application from SBT, auto-reloading is enabled) ---
[info] play - Listening for HTTP on /0.0.0.0:9000
(Server started, use Ctrl+D to stop and go back to the console...)
Agora,alémdeaaplicaçãoestardisponívelnaporta9000,aportadedebug9999
estáliberadaparaacessar.
PeloEclipse,naopção Debug Configurations,vamosconfigurarumaconexão
remotaconformeafigura6.2.
Figura6.2:Configurandoaaplicaçãoemdebug
Colocandoumbreakpointnosserviços,visualizamosasinformações conforme
afigura6.3.
70

## Página 83

CasadoCódigo Capítulo6. Criandoserviços
Figura6.3:Aplicaçãoemdebug
6.3 Acessando serviço viamobile
V a m o sutilizarumasimplesaplicaçãodecelularparausarumserviçonosso.
ParamontaroseuambienteAndroidechamaroemuladordaaplicaçãomobile,
consulteoapêndice12.
Inicialmente,carregamososdadosdoserviçoeosatribuímosaumavariáveldo
tipo JSONArray.Issoéfeitochamandoométodo jParser.getJSONFromUrl
epassandocomoparâmetroaURLhttp://<ip-da-sua-maquina>:9000/filmesJSON
quedevolveráoconteúdodasinformações noformatoJSON.
public class Top100FilmesCult extends ListActivity
implements OnClickListener {
@Override
public void onClick(View arg0) {
try {
71

## Página 84

6.3. Acessandoserviçoviamobile CasadoCódigo
JSONParser jParser = new JSONParser();
JSONArray json = jParser.getJSONFromUrl(
"http://192.168.0.101:9000/filmesJSON");
Depois,cadafilmeélidodoformatoJSONeadicionadoàlistanateladinami-
camente:
for (int i = 0 ; i < json.length() ; i++) {
try {
JSONObject c = json.getJSONObject(i);
String nome = c.getString(NOME);
String ano = c.getString(ANO);
listItems.add(ano + " - " + nome);
} catch (JSONException e) {
e.printStackTrace();
}
}
} catch (Exception e) {
e.printStackTrace();
}
adapter.notifyDataSetChanged();
}
Etemoscomoresultadoafigura12.4exibindoalistadefilmes.
72

## Página 85

CasadoCódigo Capítulo6. Criandoserviços
Figura6.4:ListadefilmesnoAndroid
6.4 Próximos passos
Certifique-sedequeaprendeu:
•aexporumserviçoemformatoXMLeJSON;
•adebugarumaaplicaçãoPlaynoEclipse.
Agoraquejátemosserviçosexpostos,vamosintegrá-losàsredessociaispara
melhordifusãodenossosistema!
73

## Página 87

Capítulo7
Integrandonasredessociais
Asredessociaissãoessenciaisparaadivulgaçãodositeeseusserviços.V a m o sinte-
graronossositeaoFacebookdeduasmaneiras,primeiramenteutilizandoaAPIna-
tivadisponibilizadaparaosdesenvolvedores,edepoisutilizandoumplugindoPlay
paraconectaraváriasredessociais:T w i t t e r ,GitHub,Google,LinkedIn,Foursquare,
Instagram,VK(redesocialrussasemelhanteaoFacebook)eXING(redesocialse-
melhanteaoLinkedIn).
7 . 1 Criando u m a aplicação no Facebook
QualquerintegraçãoaoFacebookéfeitacadastrando-seumaaplicação,oquepode
serfacilmentefeitonolinkhttps://developers.facebook.com/apps/.
Devemospreencherasinformações daaplicação,comomostraafigura7 . 1.As
informações sãosimples:oprimeirocampoéonomedoaplicativo,osegundoéo
namespace(sedesejarterumaURLhttp://apps.facebook.com/namespace),efinal-
mente,oterceiroéparaclassificarsuacategoria. Noexemplousamosacategoria

## Página 88

7.1.CriandoumaaplicaçãonoFacebook CasadoCódigo
de Diversão,massefosseumaplicativodetênis,paraexemplificar,acategoria
adequadaseria Esporte.
Figura7.1:CadastrodeaplicaçãonoFacebook
No capítulo 4 publicamos uma aplicação básica(http://play-capitulo4.
herokuapp.com/),eusaremosagoraumaURLdiferentepararefletiraaplicação
completa(http://top100filmescult.herokuapp.com/) . Depois de cadastrados os
dadosiniciais,devemosinformarume-maildecontatoeodomínionoquala
aplicaçãofuncionará.Seránecessáriocadastrarumdomíniodiferente,porexemplo
<seu-usuario-no-Heroku>-top100filmescult.herokuapp.com,semelhante à figura
7 . 2.
76

## Página 89

CasadoCódigo Capítulo7 .Integrandonasredessociais
Figura7.2:CadastrodeaplicaçãonoFacebookcomdomínio
A p ó socadastrocomsucesso,nenhumamensagemaparecenatela,apenasatela
érecarregadaeoaplicativorecém-criadoaparecenalista.
7 . 2 Integração viaJa v aScript
AintegraçãoviaJavaScriptéalgoquepodeserfeitoindependentedelinguagemou
frameworkutilizado,ouseja,seanossaaplicaçãofosseemASP.NetouPHP,seria
indiferente.
V a m o scolocarnalistadefilmesdositeumapartedecomentáriosdoFacebook.
Ousuáriousaatelacomoumacoisasó,masnaverdadevamosinserirumtrechode
códigoJavaScript(queseencarregarádegravareexibiroscomentários),editandoo
arquivo filme.scala.html.Inicialmenteadicionamosachamadarotinainfor-
mandonocampo appIdovalordachavequeestánafigura7 . 1.
O código está disponível no Quickstart: Facebook SDK for
JavaScript nolinkhttps://developers.facebook.com/docs/javascript/quickstart.
V a m o sadaptá-loaonossoexemplo.
<script>
77

## Página 90

7.2.IntegraçãoviaJavaScript CasadoCódigo
window.fbAsyncInit = function() {
// init the FB JS SDK
FB.init({
appId : ’260229664128047’, // App ID from the app dashboard
status : true, // Check Facebook Login status
xfbml : true // Look for social plugins on ...
});
// Additional initialization code such as adding
// Event Listeners goes here
};
Emseguida,vamoschamarorestantedarotinadoFacebook:
// Load the SDK asynchronously
(function(){
// If we’ve already installed the SDK, we’re done
if (document.getElementById(’facebook-jssdk’)) {return;}
// Get the first script element, which we’ll use
// to find the parent node
var firstScriptElement =
document.getElementsByTagName(’script’)[0];
// Create a new script element and set its id
var facebookJS = document.createElement(’script’);
facebookJS.id = ’facebook-jssdk’;
// Set the new script’s source to the source of the Facebook JS SDK
facebookJS.src = ’//connect.facebook.net/en_US/all.js’;
// Insert the Facebook JS SDK into the DOM
firstScriptElement.parentNode.insertBefore(facebookJS,
firstScriptElement);
}());
</script>
<div id="fb-root"></div>
<script>(function(d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
78

## Página 91

CasadoCódigo Capítulo7 .Integrandonasredessociais
js.src =
"//connect.facebook.net/pt_BR/all.js#xfbml=1&appId=260229664128047";
fjs.parentNode.insertBefore(js, fjs);
}(document, ’script’, ’facebook-jssdk’));</script>
Enofinaldapáginaadicionaremosodiv fb-commentsqueexibiráocampo
decomentários.
<center>
<div
class="fb-comments"
data-href="http://top100filmescult.herokuapp.com/filme"
data-numposts="5"
data-colorscheme="light">
</div>
</center>
}
Etemoscomoresultadoaopçãodecomentários,conformeéilustradonafigura
7 . 3.
79

## Página 92

7.3.IntegraçãoviaSecureSocial CasadoCódigo
Figura7.3:comentáriosdefilme
7 . 3 Integração viaSecureSocial
U m adascoisasmaischatasqueexistemhojeéfazercadastrodeusuárioesenhade
site,eumadascoisasmaispráticasinventadasnosúltimostemposéapossibilidade
deautenticar-seemumsiteusandoologindoFacebook,Google,T w i t t e r ,LinkedIn,
easdemaisredessociais.
Felizmente,utilizandoopluginSecureSocial(http://securesocial.ws)consegui-
remoscompoucosajustesfazeressaintegração nonossositedefilmes. OSecure
Socialéummódulodeautenticação doPlayFrameworkquesuportaosprotoco-
losmaisusadosdomercado:OAuth,OAuth2,OpenID,usuário/senhaeproporci-
onaalgumasinformações dosusuáriosautenticados,comonome,sobrenome,nome
completoee-mail.
V a m o sintegrardaseguintemaneira:paracadastroealteração dediretores,é
necessáriologar-secomoFacebook,eparalistarosdiretoresapareceráamensagem
80

## Página 93

CasadoCódigo Capítulo7 .Integrandonasredessociais
“bem-vindo”juntocomonomecompletodousuáriodoFacebook.Nateladelistade
diretores,seousuárioestiverlogado,apareceráseunomecompleto;casocontrário,
apareceráguest,comonafigura7 . 4.
Figura7.4:Listadediretoressemautenticação
Inicialmente configuramos o uso do módulo Secure Social no arquivo
build.sbt:
libraryDependencies ++= Seq(
javaJdbc,
javaEbean,
cache,
"postgresql" % "postgresql" % "9.1-901-1.jdbc4",
"securesocial" %% "securesocial" % "2.1.2"
)
Emseguida,vamosadicionarasnovasrotasaoarquivo routes.confcomo
orientaositedoplugin(http://securesocial.ws/guide/installation.html).
# pagina de login
GET /login
securesocial.controllers.LoginPage.login
GET /logout
securesocial.controllers.LoginPage.logout
# registro de usuario e gerenciamento de senha
GET /signup
securesocial.controllers.Registration.startSignUp
81

## Página 94

7.3.IntegraçãoviaSecureSocial CasadoCódigo
POST /signup
securesocial.controllers.Registration.handleStartSignUp
GET /signup/:token
securesocial.controllers.Registration.signUp(token)
POST /signup/:token
securesocial.controllers.Registration.handleSignUp(token)
GET /reset
securesocial.controllers.Registration.startResetPassword
POST /reset
securesocial.controllers.Registration.handleStartResetPassword
GET /reset/:token
securesocial.controllers.Registration.resetPassword(token)
POST /reset/:token
securesocial.controllers.Registration.handleResetPassword(token)
GET /password
securesocial.controllers.PasswordChange.page
POST /password
securesocial.controllers.PasswordChange.handlePasswordChange
# pontos de entrada dos provedores de autenticacao
GET /authenticate/:provider
securesocial.controllers.ProviderController
.authenticate(provider)
POST /authenticate/:provider
securesocial.controllers.ProviderController
.authenticateByPost(provider)
GET /not-authorized
securesocial.controllers.ProviderController.notAuthorized
Depois,criamosumarquivodepluginschamado play.pluginsnodiretório
conf,queindicaospluginsutilizados:
1500:com.typesafe.plugin.CommonsMailerPlugin
9994:securesocial.core.DefaultAuthenticatorStore
9995:securesocial.core.DefaultIdGenerator
9996:securesocial.core.providers.utils.DefaultPasswordValidator
9997:securesocial.controllers.DefaultTemplatesPlugin
9998:service.InMemoryUserService
9999:securesocial.core.providers.utils.BCryptPasswordHasher
10000:securesocial.core.providers.TwitterProvider
10001:securesocial.core.providers.FacebookProvider
82

## Página 95

CasadoCódigo Capítulo7 .Integrandonasredessociais
10002:securesocial.core.providers.GoogleProvider
10003:securesocial.core.providers.LinkedInProvider
10004:securesocial.core.providers.UsernamePasswordProvider
10005:securesocial.core.providers.GitHubProvider
10006:securesocial.core.providers.FoursquareProvider
10007:securesocial.core.providers.XingProvider
10008:securesocial.core.providers.VkProvider
10009:securesocial.core.providers.InstagramProvider
Onúmeroaoladodonomedoplugindeterminaasuaprioridade,ouseja,a
ordememqueeleserácarregado(nonossoarquivo,o CommonsMailerPlugin
serácarregadoprimeiro).
Emseguida,adicionamosoarquivo securesocial.conf,quecontémascon-
figurações geraisdoplugin:informações dee-mailechavesdosprovedoresdeau-
tenticaçãodasredessociais.
U mexemplodessearquivoestádisponívelnositehttp://securesocial.ws/guide/
configuration.html,enelevamosapenasalterarasconfigurações existentesdoFace-
book,adicionandoa clientIde clientSecretdenossaaplicação:
facebook {
authorizationUrl="https://graph.facebook.com/oauth/authorize"
accessTokenUrl="https://graph.facebook.com/oauth/access_token"
clientId=260229664128047
clientSecret=1808b7b1d37ff5ca9bc95b21648a397e
scope=email
}
Na sequência,colocaremos uma chamada a esse arquivo no final do
application.conf:
# Logger provided to your application:
logger.application=DEBUG
include "securesocial.conf"
Encerradaaconfiguração,vamosaosajustesemnossocódigo.Inicialmente,va-
mosalterarocontroller DiretorCRUDparaobteronomedousuáriodoFacebook
comavariáveluserName:
@SecureSocial.UserAwareAction
public static Result lista() {
83

## Página 96

7.3.IntegraçãoviaSecureSocial CasadoCódigo
Comaanotação @SecureSocial.UserAwareAction,permite-seobtero
usuáriodoFacebooknessemétodo.
List<Diretor> diretores = Diretor.find.findList();
Aquibuscamosalistadediretores,comovimosnocapítulodepersistência3.
Identity user = (Identity) ctx().args.get(SecureSocial.USER_KEY);
EssaéachamadaemqueopluginSecureSocialbuscaasinformações eatribui
aoobjeto user.
final String userName = user != null ? user.fullName() : "guest";
return ok(views.html.diretor.render(diretores,userName));
}
Efinalmenteonomedousuário,seestiverlogado,recebeonomecompleto;caso
contrário,recebeovalor“guest”eéatribuídoàvariáveluserName.
Emseguidanasrotinasdecadastrareremoverdiretor,vamosadicionaraano-
taçãoapropriadaparaexigirautenticaçãonoFacebook:
@SecureSocial.SecuredAction
public static Result remover(Long id) {
...
}
@SecureSocial.SecuredAction
public static Result novoDiretor() {
...
}
@SecureSocial.SecuredAction
public static Result alterar(Long id) {
...
84

## Página 97

CasadoCódigo Capítulo7 .Integrandonasredessociais
}
@SecureSocial.SecuredAction
public static Result gravar() {
...
}
Efinalmente,notemplate diretor.scala.html,mudamososparâmetrosde
entrada,adicionandoo usuario:
@(diretores: List[Diretor])(usuario: String)
@main("Diretores") {
<div class="container">
Eemseguida,adicionamosumamensagemdebem-vindocomonomedousuá-
rio:
<div class="header">
<ul class="nav nav-pills pull-right">
<li class="active">
<a href="@routes.DiretorCRUD.novoDiretor()">Novo diretor</a>
</li>
<li class="active"><a href="/">Home</a></li>
</ul>
<h2 class="text-muted">Bem-vindo @usuario ! </h2>
<h3 class="text-muted">Diretores </h3>
</div>
Aotentarmosacessarateladecadastrodenovodiretor,opluginredireciona
paraateladeautenticação,comoexibidonafigura7 . 5.
85

## Página 98

7.3.IntegraçãoviaSecureSocial CasadoCódigo
Figura7.5:AutenticaçãocomSecureSocial
Nonossoprimeiroacesso,oFacebookperguntaseépermitidooacessodosda-
dosdousuáriopelonossosite(figura7 . 6).
86

## Página 99

CasadoCódigo Capítulo7 .Integrandonasredessociais
Figura7.6:Permissãodeacessoaosdadosdousuário
Finalmente,depoisdeautenticado,onomedousuárioéexibidocomsucesso,
comomostraafigura7 . 7.
Figura7.7:Listadediretorescomusuárioautenticado
AquiconcluimosqueopluginSecureSocialpermitefacilmenteobterinforma-
çãodousuáriologadoetambémrestringiroacessoemalgumastelas,possibilitando
acriaçãodeumaestruturamaiscomplexadecontroledepermissão,etambém,se
necessário,armazenaressainformaçãonobancodedados.
7 . 4 Próximos passos
Certifique-sedequeaprendeu:
87

## Página 100

7.4.Próximospassos CasadoCódigo
•acadastrarumaaplicaçãonoFacebook;
•aadicionarchamadaJavaScriptparaincluircomentáriosdoFacebook;
•aintegrarologindoFacebookutilizandooSecureSocial.
Agoraquejátemosositeintegradoàsredessociais,vamosadicionaralgumas
melhorias,comoserviçodeuploadealgunstestes.
88

## Página 101

Capítulo8
Melhoriasnaaplicação
Nossaaplicaçãojácumpreoseupapel,masexistempequenasmelhoriasquepodem
serfeitas. NessecapítuloaprenderemosaativaroHTTPSnosite,fazeruploadde
imagensecriartestesefetivosdenossosistema.
8.1 Configurando HTTPS
EmalgunsambientesousodeHTTPSéobrigatório,enosambientesdeservido-
resJavatradicionaisénecessáriofazerumasériedepassosparaterumambiente
HTTPS,comoporexemplo,criarumcertificadoassinadolocalmenteoumudaras
portas.
NoPlay,acriaçãodeumambienteassiméfeitaautomaticamentepassandoape-
nasumparâmetro,queseráaportaqueseráexecutadooHTTPS:
fb@cascao ~/workspace-play/filmes> play
[info] Loading project definition from
/home/fb/workspace-play/filmes/project

## Página 102

8.1.ConfigurandoHTTPS CasadoCódigo
[info] Set current project to filmes
(in build file:/home/fb/workspace-play/filmes/)
_
_ __ | | __ _ _ _
| ’_ \| |/ _’ | || |
| __/|_|\____|\__ /
|_| |__/
play 2.2.1 built with Scala 2.10.2 (running Java 1.7.0_51),
http://www.playframework.com
> Type "help play" or "license" for more information.
> Type "exit" or use Ctrl+D to leave this console.
[filmes] $ run -Dhttps.port=9443
--- (Running the application from SBT, auto-reloading is enabled) ---
[info] play - Listening for HTTP on /0.0.0.0:9000
[info] play - Listening for HTTPS on port /0.0.0.0:9443
(Server started, use Ctrl+D to stop and go back to the console...)
NotepelologqueoserviçoHTTPsubiunaporta9000 eoHTTPSna9443.
T o d ooprocessodecriarumcertificadoassinadolocalmenteéfeitopeloPlayinter-
namente.
Acessandoosistemacomumbrowser,obtemosumavisoexibidonafigura8.1.
90

## Página 103

CasadoCódigo Capítulo8. Melhoriasnaaplicação
Figura8.1:primeiroacessoemHTTPS
Esseavisosignificaqueositequeestamosvisitandonão égarantidoporuma
unidadecertificadora,comoporexemploaempresaVerisign. Paraadiquirirum
certificadodigital,éprecisopagarparaessasempresas,quefuncionamsemelhantes
acartóriosvirtuais,elasasseguramqueositequeestásendoacessadoérealmenteda
empresaqueelerepresenta.Quandoumcertificadoéassinadolocalmente(comono
nossocaso),ositefunciona,apenasexibindoumaviso.NocasodoGoogleChrome,
ohttpsapareceriscadoemvermelho,comomostraafigura8.2.
91

## Página 104

8.1.ConfigurandoHTTPS CasadoCódigo
Figura8.2:osistemaemHTTPS
SedesejarmosativarexclusivamenteaportaHTTPS,bastapassarmosumparâ-
metroparadesativaraportaHTTP:
fb@cascao ~/workspace-play/filmes > play
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
[info] Set current project to filmes
(in build file:/home/fb/workspace-play/filmes/)
_
_ __ | | __ _ _ _
| ’_ \| |/ _’ | || |
| __/|_|\____|\__ /
|_| |__/
play 2.2.1 built with Scala 2.10.2 (running Java 1.7.0_51),
http://www.playframework.com
> Type "help play" or "license" for more information.
> Type "exit" or use Ctrl+D to leave this console.
[filmes] $ run -Dhttps.port=9443 -Dhttp.port=disabled
--- (Running the application from SBT, auto-reloading is enabled) ---
[info] play - Listening for HTTPS on port /0.0.0.0:9443
92

## Página 105

CasadoCódigo Capítulo8. Melhoriasnaaplicação
(Server started, use Ctrl+D to stop and go back to the console...)
NotepelologqueoserviçoHTTPnãosubiuetemosapenasoHTTPSnaporta
9443.
Sefornecessárioconfigurarumcertificadodigitaloficial(pago)emumambi-
entedeprodução,seránecessárioseguiradocumentaçãodoservidordeaplicação
escolhido. NocasodoservidordoPlay2,asinstruções oficiasestão noendereço
http://www.playframework.com/documentation/2.2.x/ConfiguringHttps.
8.2 Lendo constantes globais
Com o Play conseguimos definir facilmente valores globais no arquivo
application.conf, apenas declarando como se fossem valores de arquivo
properties:
servidorDeDocumentos = "192.168.10.123"
Ededentrodocódigoconseguimoslerovalordaconstante:
String servidorDeDocumentos =
Play.application().configuration()
.getString("servidorDeDocumentos");
Alémdelerumaconstantedotipo String,podemosleroutrostipostambém,
comobooleano(comgetBoolean)ounumérico(comgetInt).
8.3 Up l o a dde imagem
Quandopensamosemumsistemaweb,pensamostambémemumcadastrodeusuá-
rios.Seessecadastropossuirumafotodeperfil(oqueébemprovável),seránecessá-
riaumaopçãodeuploaddeimagem,queéalgoqueoPlaypermitefazerfacilmente,
comoveremosadiante.
V a m o scriarumaopção deadicionarumaimagemparacadafilmeexistente.
Nofinaldateladelistadefilmes,teremosumaopçãodeuploaddeimagem,ondeo
usuárioescolheofilme,aimagem,mandaoarquivoeeleapareceráautomaticamente
nalista.
Ateladecadastroserácriadacomonafigura8.3.
93

## Página 106

8.3.Uploaddeimagem CasadoCódigo
Figura8.3:cadastrodeimagemdeumfilme
Inicialmentedefinimosodiretóriodeuploaddasimagensdosfilmesnoarquivo
deconfigurações application.conf:
diretorioDeImagens = "/tmp/imagens/"
Emseguidavamosalteraroarquivo filme.scala.htmlparaexibirainfor-
maçãodofilmeeocampoparauploaddaimagem,adicionandootrechoaseguirno
finaldoarquivo.
...
código da lista de filmes
...
</table>
<br/>
<br/>
@helper.form(action = routes.FilmeCRUD.upload(),
’enctype -> "multipart/form-data") {
Iniciamoscomachamadaàrotinadeuploadqueadicionao enctypedo
tipo multipart/form-data,queéobrigatórionoformulárioHTMLparafazer
upload.
94

## Página 107

CasadoCódigo Capítulo8. Melhoriasnaaplicação
<table class="table table-striped table-bordered"
cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<th>Escolha o filme</th>
<td>
<select name="filmeId" >
@for(filme <- filmes) {
<option value="@filme.id">@filme.id - @filme.nome</option>
}
</select>
</td>
</tr>
Depois adicionamos a lista de filmes e em seguida a opção de upload (
type="file")noparâmetro picture.
<tr>
<th>Escolha uma imagem para fazer upload:</th>
<td>
<input type="file" name="picture" class="form-control">
</td>
</tr>
<tr>
<td colspan="2">
<input type="submit" class="btn btn-primary"
value="Enviar imagem">
</td>
</tr>
</table>
}
</div>
}
Emseguidaprecisamoscriarnocontrollerométodoquereceberáaimageme
escreveránodiretórioespecificado.
Ométodo uploadéconfiguradoparareceberarquivo,eemseguidaconfigu-
ramosavariávelpictureparareceberoarquivo.
public static Result upload() {
MultipartFormData body = request().body().asMultipartFormData();
FilePart picture = body.getFile("picture");
95

## Página 108

8.3.Uploaddeimagem CasadoCódigo
Seousuárionão enviounenhumarquivo,eleviránulo,portanto,precisamos
fazeressaverificaçãoantesdemontaronomedoarquivo.
Seoarquivonãofornulo,buscamostambémoIDdocombodefilmeseadicio-
namosaonomedoarquivo: <ID-DO-FILME>-<ARQUIVO>.
if (picture != null) {
String filmeId = form().bindFromRequest().get("filmeId");
String imagem = filmeId + ".png";
Emseguidaescrevemosoarquivonodiretórioconfiguradonavariávelglobal
diretorioDeImagens:
File file = picture.getFile();
String diretorioDeImagens =
Play.application().configuration()
.getString("diretorioDeImagens");
file.renameTo(new File(diretorioDeImagens,imagem));
E finalmente temos o redirecionamento para uma página
upload.scala.html, em caso de sucesso, e para a páginainicial em caso
deerro.
return ok(views.html.upload.render("Arquivo \"" +
imagem + "\" foi carregado com sucesso !"));
} else {
flash("error","Erro ao fazer upload");
return redirect(routes.Application.index());
}
}
Apáginaupload.scala.htmlébemsimpleseapenasexibeumamensagem
eumlinkpararetornarparaalistadefilmes.
@(mensagem: String)
@main("Upload finalizado com sucesso") {
<div class="container">
96

## Página 109

CasadoCódigo Capítulo8. Melhoriasnaaplicação
<div class="header">
<h2>@mensagem</h2>
</div>
<div class="control-group">
<label class="control-label" for="singlebutton"></label>
<div class="controls">
<a href="/filme" class="btn btn-primary">
retornar para lista de filmes
</a>
</div>
</div>
</div>
}
Eparafinalizarapenasprecisamosadicionararotaparaouploaddeimagemno
arquivoderotas:
POST /filmesUpload controllers.FilmeCRUD.upload()
Comissofaremosouploaddaimagem A.Clockwork.Orange.png,con-
formeafigura8.4.
Figura8.4:cadastrodeumaimagem
Depoisdoupload,amensageméexibidacomsucessoeaimagemgravadano
diretórioespecificado,conformeoexemploadiante(figura8.5).
97

## Página 110

8.3.Uploaddeimagem CasadoCódigo
Figura8.5:uploaddaimagemcomsucesso
V a m o sfazerummétodoparalerasimagensdequefizemosupload,inicialmente
adicionamosarota,ométodo imagemteráumparâmetro idquerepresentaa
identificaçãodeumfilme.
GET /filmeImagem controllers.FilmeCRUD.imagem(id:Long)
Parafazermosumtesterápido,vamosadicionarumachamadadaimagemde
quefizemosouploadnoiníciodalistadefilmesnoarquivo filme.scala.html:
@(filmes: List[Filme])
@main("Filmes") {
<img src="http://localhost:9000/filmeImagem?id=32"/>
<div id="fb-root"></div>
Oresultadoesperadoéaimagemaparecernotopo,conformeafigura8.5.
98

## Página 111

CasadoCódigo Capítulo8. Melhoriasnaaplicação
Figura8.6:imagemdouploadcarregadanatela
Percebemosquearotinafunciona,masserámaisadequadoexibiraimagemao
ladodonomedofilme.Portanto,nomesmoarquivovamossubstituiressetrecho:
<td>
<a href="@routes.FilmeCRUD.detalhar(filme.id)">
@filme.nome
</a>
</td>
Poresse:
<td>
<a href="@routes.FilmeCRUD.detalhar(filme.id)">@filme.nome</a>
<img src="@routes.FilmeCRUD.imagem(filme.id)" alt="">
</td>
Ecomoresultadotemosaimagemaoladodofilmecorretamente(figura8.7).
99

## Página 112

8.3.Uploaddeimagem CasadoCódigo
Figura8.7:imagemdouploadcarregadacorretamente
Entretanto,anossaaplicaçãotemumproblema:elapermiteouploaddequal-
quertipodearquivoeexibeapenasimagensdotipoPNG.Seescolherumaimagem
rosemary-baby.jpg,elaseráenviadacomsucesso,masnão seráexibida. Para
solucionaresseproblema,vamoslimitaressetipodearquivonoupload,fazendoa
seguintealteração.
Inicialmente vamos adicionar novas variáveis globais no arquivo
application.conf:
contentTypePadraoDeImagens="image/png"
extensaoPadraoDeImagens=.png
Emseguida,onovocódigodométododeupload.
Primeiro,lemososvaloresdasconstantesglobais.
public static Result upload() {
MultipartFormData body = request().body().asMultipartFormData();
FilePart picture = body.getFile("picture");
String extensaoPadraoDeImagens =
Play.application().configuration()
.getString("extensaoPadraoDeImagens");
if (picture != null) {
100

## Página 113

CasadoCódigo Capítulo8. Melhoriasnaaplicação
String filmeId = form().bindFromRequest().get("filmeId");
String imagem = filmeId + extensaoPadraoDeImagens;
Aquiusamosométodo getContentTypeparaidentificarotipodeimagem
queestásendoenviada.NoexemplovamostentarenviarumaimagemdotipoJPEG
(figura8.8).
Figura8.8:imagemdouploaddearquivodotipoJPEG
String contentType = picture.getContentType();
File file = picture.getFile();
String diretorioDeImagens =
Play.application().configuration()
.getString("diretorioDeImagens");
String contentTypePadraoDeImagens =
Play.application().configuration()
.getString("contentTypePadraoDeImagens");
Aquiidentificamosseotipodearquivoenviadoéo image/PNG.Emcasoposi-
tivo,ocomportamentoéomesmodométodoanterior,eemcasonegativoéexibida
amensagemdeerroconformeafigura8.9.
if (contentType.equals(contentTypePadraoDeImagens)) {
file.renameTo(new File(diretorioDeImagens,imagem));
return ok(views.html.upload.render("Arquivo \"" +
imagem + "\" do tipo [" + contentType +
"] foi carregado com sucesso !"));
} else { // se for uma imagem nao aceita
return ok(views.html.upload.render(
"Imagens apenas no formato \"" +
contentTypePadraoDeImagens + "\" serão aceitas!"));
101

## Página 114

8.4. Testandosuaaplicação CasadoCódigo
}
}
else { // se o usuario nao enviou o arquivo
flash("error","Erro ao fazer upload");
return redirect(routes.Application.index());
}
}
Figura8.9:imagemdeerroaotentarouploaddearquivodotipoJPEG
Comisso,conseguimosfazerouploaddeimagensusandoosrecursospróprios
doplay.
8.4 Testando sua aplicação
Conformenossaaplicaçãovaicrescendo,achancedeumanovaalteraçãoafetaralgo
quejáfuncionaaumenta,eparaimpedirqueissoaconteça,éinteressanteteruma
boacoberturadetestes,principalmentenaspartescríticasdosistema.
OPlaynosajudanissotambém,proporcionandodiferentestiposdeteste.
Iniciaremoscomumtestechamandoumcontrolleretestandooseuresultado.
CriaremosumaclassecomummétodotestaHTMLdoIndexdentrodopacote
test.
import static org.fest.assertions.Assertions.assertThat;
import static play.mvc.Http.Status.OK;
import static play.test.Helpers.*;
import org.junit.Test;
102

## Página 115

CasadoCódigo Capítulo8. Melhoriasnaaplicação
import play.mvc.Result;
public class WebTest {
@Test
public void testaHTMLdoIndex() {
Aquibuscamosoresultadocomométodo callActionchamandoocon-
troller Inicio.index(). Emseguida,comparamosseoresultadoéostatusde
sucesso(equivalenteaostatusHTTP200 —http://pt.wikipedia.org/wiki/Anexo:
Lista_de_c%C3%B3digos_de_status_HTTP).
Result result = callAction(controllers.routes.ref.Inicio.index());
assertThat(status(result)).isEqualTo(OK);
ComistocomparamosseoresultadoretornouumarquivodotipotextoHTML:
assertThat(contentType(result)).isEqualTo("text/html");
DepoiscomparamosseoencodingretornadoéUTF-8:
assertThat(charset(result)).isEqualTo("utf-8");
Efinalmenteverificamossenoresultadoexisteotexto“melhordocinema”.
assertThat(contentAsString(result)).contains("melhor do cinema");
}
}
Parainiciarumaaplicaçãodoplayjáaprendemosqueocomandoéplay run.
Jápararodarostestesocomandoésemelhante: play test.
fb@cascao ~/workspace-play/filmes > play test
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
[info] Set current project to filmes
(in build file:/home/fb/workspace-play/filmes/)
[info] WebTest
[info] + testaHTMLdoIndex
[info]
[info]
[info] Total for test WebTest
103

## Página 116

8.4. Testandosuaaplicação CasadoCódigo
[info] Finished in 0.02 seconds
[info] 1 tests, 0 failures, 0 errors
[info] Passed: Total 1, Failed 0, Errors 0, Passed 1
[success] Total time: 2 s, completed 30/01/2014 22:56:08
fb@cascao ~/workspace-play/filmes >
Nofinaldologtemos success,quedemonstraqueotesteexecutoucomsu-
cesso.
Testes no Eclipse
A p e s a rdeexistirumainterfacegráficaparaexecutartestesnoEclipse,
nemtodotestedoPlayéexecutadocomsucesso,poressemotivoéim-
prescindívelquetodaexecuçãodetestessejafeitanoplayconsole.
V a m o svercomootestesecomportaemcasodefalha,paraissobastatrocarmos
otexto:
assertThat(contentAsString(result)).contains("melhor do cinema");
Por:
assertThat(contentAsString(result))
.contains("melhor do Fernando Boaglio");
Temosumlognoconsole,bemmaiorqueoanterior,executandoomesmoco-
mando play test:
fb@cascao ~/workspace-play/filmes > play test
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
[info] Set current project to filmes
(in build file:/home/fb/workspace-play/filmes/)
[info] Compiling 1 Java source to
/home/fb/workspace-play/filmes/target/scala-2.10/test-classes...
Aquiédetalhadooerroem WebTest.testaHTMLdoIndex:
[error] Test WebTest.testaHTMLdoIndex failed: <’
[error]
[error] <!DOCTYPE html>
104

## Página 117

CasadoCódigo Capítulo8. Melhoriasnaaplicação
[error]
[error] <html>
[error] <head>
[error] <title>Top 100 filmes Cult</title>
[error] <link href="/assets/bootstrap/css/bootstrap.min.css"
rel="stylesheet" media="screen">
[error] <link rel="stylesheet" media="screen"
href="/assets/stylesheets/main.css">
[error] <link rel="shortcut icon" type="image/png"
href="/assets/images/favicon.png">
[error] <script src="/assets/javascripts/jquery-1.9.0.min.js"
type="text/javascript"></script>
[error] </head>
[error] <body>
[error] <style>
[error] body {
[error] padding-top: 50px;
[error] }
[error] .starter-template {
[error] padding: 40px 15px;
[error] text-align: center;
[error] }
[error]
[error] </style>
[error] <div class="navbar navbar-inverse navbar-fixed-top">
[error] <div class="container">
[error] <div class="navbar-header">
[error] <button type="button" class="navbar-toggle"
data-toggle="collapse"
data-target=".navbar-collapse">
[error] </button>
[error] <a class="navbar-brand" href="/">
Top 100 filmes Cult
</a>
[error] </div>
[error] <div class="collapse navbar-collapse">
[error] <ul class="nav navbar-nav">
[error] <li><a href="/diretor">Diretores</a></li>
[error] <li><a href="/filme">Filmes</a></li>
[error] <li><a href="/sobre">Sobre o sistema</a></li>
[error] <li><a href="/play">Sobre o Play Framework</a></li>
105

## Página 118

8.4. Testandosuaaplicação CasadoCódigo
[error] <li><a href="http://getbootstrap.com/">
Sobre o Bootstrap</a></li>
[error] </ul>
[error] </div>
[error] </div>
[error] </div>
[error] <div class="container">
[error] <div class="starter-template">
[error] <h1>Top 100 filmes Cult</h1>
[error] <p class="lead">O melhor do cinema est&aacute; aqui!</p>
[error] </div>
[error] </div>
[error] </body>
[error] </html>
[error]
Depoisdeexibirtodooresultado,ologinformaqueoeledeveriaconterotexto
“melhordoFernandoBoaglio”,exibindoum Xaoladodotestecomerro.
[error] ’> should contain the String:<’melhor do Fernando Boaglio’>
[info] WebTest
[info] x testaHTMLdoIndex
[info]
[info]
[info] Total for test WebTest
[info] Finished in 0.014 seconds
[info] 1 tests, 1 failures, 0 errors
[error] Failed: Total 1, Failed 1, Errors 0, Passed 0
[error] Failed tests:
[error] WebTest
[error] (test:test) sbt.TestsFailedException: Tests unsuccessful
[error] Total time: 3 s, completed 30/01/2014 23:05:27
fb@cascao ~/workspace-play/filmes >
Podemostestarqualquercoisa,inclusivemanipularobancodedados. Entre-
tanto,provavelmentecadastrarinformações nobancodedadosvaiatrapalharode-
senvolvimento,principalmenteseeleforcompartilhadocomumaequipe.
Poressemotivo,éinteressanteterconfigurações específicasdeteste,comopor
exemplo,acessarumbancodedadosdiferente.
V a m o smostrarumexemploemquecadastramosumdiretorebuscamosum
filmeutilizandoconfigurações específicas.
106

## Página 119

CasadoCódigo Capítulo8. Melhoriasnaaplicação
Inicialmentecriaremosumarquivo testes.conf nomesmodiretório do
application.conf,comoseguinteconteúdo:
#
# ambiente de testes
#
application.langs="en,pt"
ebean.default="models.*"
evolutionplugin=disabled
db.default.driver=org.postgresql.Driver
db.default.url="postgres://postgres:postgres@localhost/filmes"
logger.root=ERROR
logger.play=INFO
logger.application=DEBUG
diretorioDeImagens = "/tmp/testes/imagens/"
contentTypePadraoDeImagens="image/png"
extensaoPadraoDeImagens=.png
Nessearquivoestamosusandoomesmobancodedados,maspodemosalterar
essearquivosemproblemasesemcomprometeraaplicação.
Emseguida,criaremosoteste DatabaseTestcomométodo startAppea
anotação @BeforeClass,quesignificaqueessemétodoseráexecutadoantesde
chamarmososmétodoscom @Test.
O método startApp éresponsávelpor carregar as configurações com
ConfigFactory.parseFile.
public class DatabaseTest {
private static Configuration additionalConfigurations;
public static play.test.FakeApplication app;
@BeforeClass
public static void startApp() {
Config additionalConfig =
ConfigFactory.parseFile(new File("conf/testes.conf"));
additionalConfigurations = new Configuration(additionalConfig);
System.out.println(additionalConfigurations.asMap());
app = Helpers.fakeApplication(additionalConfigurations.asMap());
107

## Página 120

8.4. Testandosuaaplicação CasadoCódigo
Helpers.start(app);
}
Aqui,adicionamosométodoquefinalizaasconfigurações adicionais,executado
depoisdechamarmososmétodoscom @Test.
@AfterClass
public static void stopApp() {
Helpers.stop(app);
}
Depois,otesteadicionaumdiretorchamado“FernandoMeireles”eemseguida
verificaseoidgeradonãoénulo.
@Test
public void testaDiretor() {
Diretor diretor = new Diretor();
diretor.nome = "Fernando Meireles";
diretor.save();
assertThat(diretor.id).isNotNull();
}
Então,otestebuscaumfilmepeloid32econfereseonomeé“ AClockwork
Orange”.
@Test
public void testaFilme() {
Filme filme = Filme.find.byId(32l);
assertThat("A Clockwork Orange").isEqualTo(filme.nome);
}
}
Agorarodamosostestesnovamenteeverificamosque,depoisdacompilação,
sãoexecutadoscomsucesso.
108

## Página 121

CasadoCódigo Capítulo8. Melhoriasnaaplicação
fb@cascao ~/workspace-play/filmes > play test
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
[info] Set current project to filmes
(in build file:/home/fb/workspace-play/filmes/)
[info] Compiling 2 Java sources to
/home/fb/workspace-play/filmes/target/scala-2.10/test-classes...
[info] WebTest
{extensaoPadraoDeImagens=.jpg,
db={default={driver=org.postgresql.Driver,
url=postgres://postgres:postgres@localhost/filmes}},
application={langs=en,pt},
evolutionplugin=disabled, logger={application=DEBUG,
root=ERROR, play=INFO},
ebean={default=models.Diretor,models.Filme},
diretorioDeImagens=/tmp/imagens/,
contentTypePadraoDeImagens=image/jpeg}
[info] + testaHTMLdoIndex
[info]
[info]
[info] Total for test WebTest
[info] Finished in 0.011 seconds
[info] 1 tests, 0 failures, 0 errors
Depoisdoprimeirotesteencerrado,inicia-seosegundo:
[info] application - [securesocial] loaded templates plugin:
securesocial.controllers.DefaultTemplatesPlugin
[info] play - Starting application default Akka system.
[debug] application - [securesocial] calling deleteExpiredTokens()
[info] application - [securesocial] loaded user service:
class service.InMemoryUserService
[info] application - [securesocial] loaded password hasher bcrypt
[info] application - [securesocial] loaded identity provider: twitter
[info] application - [securesocial] loaded identity provider: facebook
[info] application - [securesocial] loaded identity provider: google
[info] application - [securesocial] loaded identity provider: linkedin
[info] application - [securesocial] loaded identity provider: userpass
[info] application - [securesocial] loaded identity provider: github
[info] application - [securesocial] loaded identity provider: foursquare
[info] application - [securesocial] loaded identity provider: xing
[info] application - [securesocial] loaded identity provider: vk
109

## Página 122

8.4. Testandosuaaplicação CasadoCódigo
[info] application - [securesocial] loaded identity provider: instagram
[info] application - [securesocial] unloaded ... provider: instagram
[info] application - [securesocial] unloaded ... provider: vk
[info] application - [securesocial] unloaded ... provider: xing
[info] application - [securesocial] unloaded ... provider: foursquare
[info] application - [securesocial] unloaded ... provider: github
[info] application - [securesocial] unloaded ... provider: userpass
[info] application - [securesocial] unloaded ... provider: linkedin
[info] application - [securesocial] unloaded ... provider: google
[info] application - [securesocial] unloaded ... provider: facebook
[info] application - [securesocial] unloaded ... provider: twitter
[info] application - [securesocial] unloaded password hasher bcrypt
[info] play - Shutdown application default Akka system.
[info] DatabaseTest
[info] + testaDiretor
[info] + testaFilme
[info]
[info]
[info] Total for test DatabaseTest
[info] Finished in 0.001 seconds
[info] 2 tests, 0 failures, 0 errors
Aquitemososegundotesteencerrado,efinalmente,oresumofinal:
[info] Passed: Total 3, Failed 0, Errors 0, Passed 3
[success] Total time: 4 s, completed 30/01/2014 23:20:27
fb@cascao ~/workspace-play/filmes >
Teste em web com Selenium
OSeleniuméumaferramentadeautomaçãodetestesfuncionaispara
interfacesW e b .Suaprincipalvantageméautilizaçãodopróprionave-
gadorwebpararealização dostestes. Consulteositeoficialparamais
informações: http://www.seleniumhq.org/.
Sequisermosfazerumtestecomobrowser,podemosusaroSeleniumefeliz-
menteoPlayencapsulaasprincipaisfunções, facilitandomuitoaconstruçãodetes-
tes.
V a m o sfazerumtestecomresultadosemelhanteaoprimeiro,emqueverificamos
seapáginainicialcontémotexto“melhordocinema”.
110

## Página 123

CasadoCódigo Capítulo8. Melhoriasnaaplicação
Primeiro,configuramosdiretonocódigoumservidordoPlaynaporta3333,
queutilizaráumbancodedadosemmemória(ouseja,qualqueralteraçãoneleserá
desprezada).
Paramaisdetalhesnasconfigurações, consulteadocumentaçãoemhttp://www.
playframework.com/documentation/2.2.1/JavaFunctionalTest.
public class BrowserTest {
@Test
public void testarIndex() {
running(testServer(3333,fakeApplication(inMemoryDatabase())),
HTMLUNIT,
new Callback<TestBrowser>() {
Aquichamamosobrowsernoservidornaporta3333echamamosaURLhttp:
//localhost:3333/.Emseguida,éverificadosenocódigofontedapáginafoiretornado
otexto“melhordocinema”.
public void invoke(TestBrowser browser) {
browser.goTo("http://localhost:3333/");
assertThat(browser.pageSource())
.contains("melhor do cinema");
}
});
}
OinteressantedaAPIdoSeleniuméqueelapermitereproduziranavegaçãono
sistemacomosefosseowebbrowser.
Nesseexemplo,vamosacessarapáginadelistagemdefilmes:
@Test
public void testarLinkNovoFilme() {
running(testServer(3333,fakeApplication()),
HTMLUNIT,
new Callback<TestBrowser>() {
public void invoke(TestBrowser browser) {
browser.goTo("http://localhost:3333/filme");
Emseguidaverificamosseelacontémotexto“Filmes":
assertThat(browser.pageSource()).contains("Filmes");
111

## Página 124

8.4. Testandosuaaplicação CasadoCódigo
Depoisdisso,comométodo clicksimulamosoeventodeousuárioclicarno
primeirolinkdalistadefilmes,quenoslevaráparaapáginadofilmePsicose.
OtesteterminaverificandosenocódigofonteHTMLdapáginaexisteotexto
“Psicose”.
browser.$("table td a").first().click();
assertThat(browser.pageSource()).contains("Psicose");
}
});
}
}
Aqui,finalmente,temosaexecuçãocompleta:semprequeforexecutadooco-
mando play test,todosostestesquecriarmosserãoexecutados.
fb@cascao ~/workspace-play/filmes > play test
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
[info] WebTest
[info] + testaHTMLdoIndex
[info]
[info]
[info] Total for test WebTest
[info] Finished in 0.014 seconds
[info] 1 tests, 0 failures, 0 errors
[info] DatabaseTest
[info] + testaDiretor
[info] + testaFilme
[info]
[info]
[info] Total for test DatabaseTest
[info] Finished in 0.001 seconds
[info] 2 tests, 0 failures, 0 errors
[info] BrowserTest
[info] + testarLinkNovoFilme
[info] + testarIndex
[info]
[info]
[info] Total for test BrowserTest
[info] Finished in 0.0 seconds
[info] 2 tests, 0 failures, 0 errors
112

## Página 125

CasadoCódigo Capítulo8. Melhoriasnaaplicação
[info] Passed: Total 5, Failed 0, Errors 0, Passed 5
[success] Total time: 19 s, completed 31/01/2014 00:34:54
fb@cascao ~/workspace-play/filmes >
8.5 Próximos passos
Certifique-sedequeaprendeua:
•configurarHTTPSdeumaaplicaçãodoPlay;
•fazeruploaddearquivos;
•manipulararquivosparaexibirnowebbrowser;
•criartestesdocontroller;
•criartestesdobancodedadoscomconfigurações específicas;
•criartestescomSelenium.
113

## Página 127

Capítulo9
Continueseusestudos
Nossaaplicaçãoestácompleta,mascomcertezapodesermelhorada.
Aseguiralgumasideiasdoquepoderiaserimplementado:
•enviaremailsdosfilmespreferidos;
•integraremoutrasredessociaisalémdoFacebook;
•criarumaáreadeusuário,comperfil,informações efotos,filmespreferidos.
9.1 Para saber mais
Agoraemdiante,paraaprimorarosconhecimentosnoPlay:
•AcompanheacomunidadedoPlayFrameworknoGooglePlus:https://plus.
google.com/communities/116192785110716864793
•Leia a documentação do site: http://www.playframework.com/
documentation/2.2.x/Home

## Página 128

9.1.Parasabermais CasadoCódigo
•Participe do grupo de email https://groups.google.com/forum/#!forum/
play-framework,escrevendonotítulodoemail[play-2.2-java]
•SequiserseaprofundaremScalaparaentendermelhorofontedoPlay,façao
cursogratuitoonlinedoMartinOdersky,umdosdesenvolvedoresdalingua-
gem:https://www.coursera.org/course/progfun
Eacompanheosprincipaisblogs:
•blogoficial:http://typesafe.com/blog/PlayFramework
•blogdeJamesRoper,commiterdaequipedoPlay-http://jazzy.id.au/default/
tags/play
•blogdePascalVoitot,commiterdaequipedoPlay-http://mandubian.com/
•blogdeJamesW a r d ,commiterdaequipedoPlay-http://www.jamesward.
com/category/play-framework/
•blogcomváriosartigosdePlay-http://www.scoop.it/t/playframework
116

## Página 129

Capítulo10
ApêndiceA-Playconsoleem
detalhes
Aquisegueumbreveresumodoconsoledoplay,listandoalgunscomandosqueserão
úteiscomousonodiaadia.
Oscomandosaquilistadossãoexecutadosdentrodoconsole,conformeoexem-
plo:
fb@cascao ~/workspace-play/filmes> play
[info] Loading project definition from
/home/fb/workspace-play/filmes/project
[info] Set current project to filmes (in build file:
/home/fb/workspace-play/filmes/)
_
_ __ | | __ _ _ _
| ’_ \| |/ _’ | || |
| __/|_|\____|\__ /
|_| |__/

## Página 130

CasadoCódigo
play 2.2.1 built with Scala 2.10.2 (running Java 1.7.0_51),
http://www.playframework.com
> Type "help play" or "license" for more information.
> Type "exit" or use Ctrl+D to leave this console.
[filmes] $
•helpe tasks-exibeoscomandosexistentesdoconsole
•compile-recompilaosfontes
•clean-limpatemporáriosecache
•run-iniciaoservidor
•settings-listaasvariáveisdoservidor
•reload-recarregaosarquivosdoprojeto
•session list-listainformações dassessões existentes
118

## Página 131

Capítulo11
ApêndiceB-Instalaçãoe
configuraçãodoPostgreSQL
Paraconseguirmospersistirasinformações donossosite,precisamosdeumbanco
dedadosinstaladoparafuncionaroambientedocapítulo3.
Inicialmenteacessamoso siteoficialhttp://www.postgresql.org/download/e
baixamosversãomaisrecentedisponíveldasérie9.xdoPostgreSQL.
V a m o sutilizarcomoexemploaversão9.3.1paraWindows.
FaçaodownloaddopacoteparaWindowseexecute-ocomumusuáriocom
privilégiosdeadministradordamáquina.
A p ó sdescompactaremumaáreatemporária,seráexibidaatelainicialconforme
afigura11.1.

## Página 132

CasadoCódigo
Figura11.1:iniciodainstalação
Nafigura11.2informeodiretóriodeinstalação(podeserovalorpadrãomesmo).
120

## Página 133

CasadoCódigo Capítulo11.ApêndiceB-InstalaçãoeconfiguraçãodoPostgreSQL
Figura11.2:diretóriodeinstalação
Ainstalação éfeitasobreousuáriochamado postgres,forneçasuasenha
(também postgres)conformeafigura11.3.
121

## Página 134

CasadoCódigo
Figura11.3:senhadousuáriopostgres
Continueainstalação atéofinal. Obancodedadosseráinstaladoeiniciado
automaticamente.Alémdele,foiinstaladaaferramenta pgAdmin 3,conformea
figura11.4.
Figura11.4:acessoaopgAdmin3
OpgAdmin3éumaferramentacompletademanutenção emanipulação do
bancodedadosdoPostgreSQL.
Aoclicarnaopção PostgreSQL 9.3 (localhost:5432)apareceráuma
janelapedindoasenha. Informeovalor postgresemarqueaopção Store
passwordcomonafigura11.5.
122

## Página 135

CasadoCódigo Capítulo11.ApêndiceB-InstalaçãoeconfiguraçãodoPostgreSQL
Figura11.5:conectandoaobancodedados
Naopção Database,selecioneaopção New Database...conformeafigura
11.6.
123

## Página 136

CasadoCódigo
Figura11.6:criandoumnovobancodedados
Nocampo nameécolocadoonomedobancodedadoscomonafigura11.7.
124

## Página 137

CasadoCódigo Capítulo11.ApêndiceB-InstalaçãoeconfiguraçãodoPostgreSQL
Figura11.7:criandoobancodedadosfilmes
Depoisdecriarobancofilmes,selecione-oecliquenoíconecomalupaSQL
conformeindicadonafigura11.8.
125

## Página 138

CasadoCódigo
Figura11.8:bancofilmescriado
AcesseoSQLdastabelaspelolinkhttp://bit.ly/JLFA9Cecopieoseuconteúdo.
EmseguidacoledentrodajanelaSQLecliqueondeestáindicadonafigura11.9,
eemseguidapercebaamensagemdeexecuçãocomsucesso.
126

## Página 139

CasadoCódigo Capítulo11.ApêndiceB-InstalaçãoeconfiguraçãodoPostgreSQL
Figura11.9:populandoabasedados
Astabelasforamcriadascomsucesso.
Cliquenatabelaeemseguidanoíconeindicadonafigura11.10paravertodosos
registros.
127

## Página 140

CasadoCódigo
Figura11.10:listadefilmes
Oseuambientedebancodedadosestáprontoparauso,senecessáriopodecriar
novosbancosdedadosparatestessemproblemas.
128

## Página 141

Capítulo12
ApêndiceC-Instalaçãoe
configuraçãodoAndroid
Esseapêndiceéumabreveintrodução aoAndroidcomconceitossuficientespara
executar o exemplo play2-android-casadocodigo, disponívelem https://
github.com/boaglio/play2-android-casadocodigo.
Nocapítulodeserviços(6)aprendemosadisponibilizarinformaçõesemformato
JSON.AnossaaplicaçãoemAndroidcarregaráessasinformações nesseformatoe
exibiránateladocelular.
ParadesenvolvercomAndroid,alémdaJDKserãonecessáriasmaisduasferra-
mentas:AndroidSDKeoEclipsecomoADTPlugin(chamadodeADTBundle).
BaixeeinstaleoADTbundledasuaplataformahttp://developer.android.com/
sdk/index.html.

## Página 142

CasadoCódigo
Figura12.1:ADTbundle
DepoisdeimportaronossoprojetoAndroid,cliquenoA V D M(AndroidV i r t u a l
DeviceManager)comoindicadonafigura12.1,queéolocalquecriamosemuladores
decelularpararodaranossaaplicação.
130

## Página 143

CasadoCódigo Capítulo12.ApêndiceC-InstalaçãoeconfiguraçãodoAndroid
Figura12.2:emuladorAndroid
Clicandoem N e w,vamoscriarumemuladorconformeafigura12.2.
131

## Página 144

CasadoCódigo
Figura12.3:ExecutandoaplicaçãoAndroid
Agoracomumemuladorexistente,chamandoaopção Run Ase Android
Applicationcomonafigura12.3,oemuladorseráexecutadoautomaticamente,e
emseguidaaaplicaçãoseráchamada.
Aoclicarmosnobotão buscar filmes,alistadefilmesacessaarotinacriada
nocapítulodeserviços6.3.
132

## Página 145

CasadoCódigo Capítulo12.ApêndiceC-InstalaçãoeconfiguraçãodoAndroid
Figura12.4:listadefilmesnoAndroid
Etemoscomoresultadoafigura12.4exibindoalistadefilmes.
133