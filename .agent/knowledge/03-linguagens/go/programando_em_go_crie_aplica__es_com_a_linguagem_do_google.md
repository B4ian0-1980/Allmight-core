---json
{
  "id": "programando_em_go_crie_aplica__es_com_a_linguagem_do_google",
  "title": "Programando em Go Crie aplicações com a linguagem do Google",
  "categoria": "03-linguagens",
  "subcategoria": "go",
  "resumo": "**Arquivo Original:** `Programando em Go Crie aplicações com a linguagem do Google.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "com",
    "crie",
    "google",
    "linguagem",
    "linguagens",
    "programando"
  ],
  "perguntas_tipo": [
    "Como utilizar Programando em Go Crie aplicações com a linguagem do Google?",
    "Quais as boas praticas de go?"
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
  "dono": "stack-go",
  "prioridade": 2
}
---

# Programando em Go Crie aplicações com a linguagem do Google

> **Arquivo Original:** `Programando em Go Crie aplicações com a linguagem do Google.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de
10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem
autorização prévia por escrito da editora, sejam quais forem os meios:
fotográficos, eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 5

CasadoCódigo
Créditos
OGopherutilizadonacapadestelivroécriação deReneeFrench(http://
reneefrench.blogspot.com/)elicenciadosobCreativeCommonsAttributions
3.0(https://creativecommons.org/licenses/by/3.0/).
i

## Página 7

CasadoCódigo
Prefácio
Gotemsidofundamentalnomeudiaadiaescrevendoprogramasconcor-
renteseplataformas(systems programming).Éumalinguagemquefavorece
acriaçãodeprogramasparalelos,leves,rápidos,simplesdeentender,dedis-
tribuir(umsimplesbináriocompiladoestaticamente)edemanter.
Honestamente,porém,minhasprimeirasimpressões geraissobrealin-
guagemnãoforamdasmelhores.Aausênciadefuncionalidadesencontradas
emoutraslinguagensmaissofisticadasmeincomodava. Algumasbempo-
lêmicasecontroversas,comoadetiposgenéricoseotratamentodeerros
simplessemexceções. Nãoéincomumterqueescreverumaououtralinha
decódigoamaisemGodoqueserianecessárioemoutralinguagem.Nãoé
umalinguagemotimizadaparaprogramascurtos,massimparaprogramas
escaláveis.
Noinício,omodocomqueGolidacomconcorrênciaeparalelismofoio
quedespertoumeuinteressenalinguagem. Channelse goroutinessãoprimiti-
vasextremamentepoderosasquecontinuaminfluenciandobastanteaforma
comqueescrevoprogramasconcorrentes,inclusiveemoutraslinguagens.E
eutenhocertezadequevãoinfluenciaraformacomquevocêescrevepro-
gramastambém.
Orestonãopareciaternadadeespecialquandocomparadocomoutras
linguagens.Mas,comotempo,fuiaprendendoaapreciarasimplicidadede
Go.Demorouumpoucoatémecairafichadequeaausênciadefuncionali-
dadesquetrariamcomplexidadefoi(econtinuasendo)umadecisãoexplícita
deseusprincipaismantenedores.IssofazcomqueGosejaumalinguagem
relativamentefácildeaprenderegeralmenteexisteapenasuma(oupoucas)
forma(s)clara(s)deseresolverosproblemaseescrevercódigoemGo,amai-
iii

## Página 8

CasadoCódigo
oriadelasusandoapenasoquejáestádisponívelnabibliotecapadrão.
QuandomedávontadedereclamardequeGonãotemessaouaquela
funcionalidade,lembro-meoquãosimplesélereentenderprogramasescri-
tosemGo.Lembro-metambémdequantadiscussãodesnecessáriaseevita
nodiaadiacomoutrosprogramadoressobrecomocódigodeveriaseres-
crito.U m avezqueseentendeeaceitaamentalidadeportrásdalinguagem,
timesconseguemfocaremescrevercódigoqueresolveproblemasdeverdade
deformasimplesdemanter,emvezdegastartempodiscutindopreferências
pessoaisedeestilodecódigo.
Go,naminhaopinião,representaumótimobalançoentrepragmatismo
efuncionalidades.Éumaescolhaperfeitaparaprogramasqueprecisamso-
breviverpormuitotempo,namãodemuitaspessoasetimesdiferentes.
JátiveoprazerdetrabalhardiretamentecomoCaio,queéumexcelente
programadorefazrealmenteumbomtrabalhoemapresentaralinguagem.
Bomproveitoefelizprogramação!
F a b i oKung
iv

## Página 9

CasadoCódigo
Agradecimentos
À minhaesposaGabriela,pelapaciênciaetodooapoio.
AoFranciscoCapuano,peloexemploeinspiração.
À minhaavôArlindaeaomeutioWashington,porpermitiremqueeu
pudesseestudaremeapaixonarpelaminhaprofissão.
Atodaaminhafamíliaporacreditareconfiaremmim,sempre.
Eatodosque,deformadiretaouindireta,contribuíramparaaescrita
destelivro;emespecial:GuilhermeConte,AndersonLeite,ReinaldoBraga,
BrunoGrasselli,LucaPette,AdrianoAlmeidaePauloSilveira.
v

## Página 11

CasadoCódigo Sumário
Sumário
1 Introdução 1
1.1 PorqueGo?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Instalação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 OprimeiroprogramaemGo. . . . . . . . . . . . . . . . . . . 7
2 Explorando a sintaxe bá s ica 9
2.1 Estruturadocapítulo . . . . . . . . . . . . . . . . . . . . . . . 9
2.2 Ifeexpressões lógicas . . . . . . . . . . . . . . . . . . . . . . . 10
2.3 Arrayseslices . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.4 Exemplo1:conversordemedidas . . . . . . . . . . . . . . . . 10
2.5 Criandofunções básicas. . . . . . . . . . . . . . . . . . . . . 17
2.6 Exemplo2:quicksortefunções . . . . . . . . . . . . . . . . . 18
3 I n d oalém:mais exemplos 27
3.1 Exemplo3:mapaseestatísticas . . . . . . . . . . . . . . . . . 27
3.2 Exemplo4:pilhasetiposcustomizados. . . . . . . . . . . . . 31
4 C o l eções: arrays, slices e maps 39
4.1 Arrays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
4.2 Slices. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
4.3 Maps. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
vii

## Página 12

Sumário CasadoCódigo
5 Criando novos tipos 6 3
5.1 Novosnomesparatiposexistentes . . . . . . . . . . . . . . . 63
5.2 Conversãoentretiposcompatíveis . . . . . . . . . . . . . . . 65
5.3 Criandoabstrações maispoderosas . . . . . . . . . . . . . . . 67
5.4 Structs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
5.5 Interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
5.6 Duck typingepolimorfismo . . . . . . . . . . . . . . . . . . . 76
5.7 U mexemplodabibliotecapadrão:io.Reader . . . . . . . . . 78
6 F u nçõ e s 8 3
6.1 Aformabásica. . . . . . . . . . . . . . . . . . . . . . . . . . . 83
6.2 Valoresderetornonomeados . . . . . . . . . . . . . . . . . . 85
6.3 Argumentosvariáveis. . . . . . . . . . . . . . . . . . . . . . . 87
6.4 Funções deprimeiraclasse . . . . . . . . . . . . . . . . . . . . 89
6.5 Funções anônimas . . . . . . . . . . . . . . . . . . . . . . . . . 90
6.6 Closures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
6.7 Higher-order fu nct io ns. . . . . . . . . . . . . . . . . . . . . . . 94
6.8 Tiposdefunção . . . . . . . . . . . . . . . . . . . . . . . . . . 96
6.9 ServindoHTTPatravésdefunções . . . . . . . . . . . . . . . 99
7 Concorrênciacom goroutines e channels 103
7 . 1Goroutines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
7 . 2Channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
7 . 3Buffers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
7 . 4Controlandoadireçãodofluxo . . . . . . . . . . . . . . . . . 111
7 . 5Select. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
7 . 6Temporizadorese timeout s. . . . . . . . . . . . . . . . . . . . 115
7 . 7Sincronizandomúltiplasgoroutines . . . . . . . . . . . . . . . 117
7 . 8Concorrência,paralelismoeGOMAXPROCS. . . . . . . . . 119
7 . 9Recapitulando . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
viii

## Página 13

CasadoCódigo Sumário
8 Mão na massa: encurtador de URLs 123
8.1 Estruturadoprojeto. . . . . . . . . . . . . . . . . . . . . . . . 124
8.2 Criandooservidor. . . . . . . . . . . . . . . . . . . . . . . . . 124
8.3 CriandoURLscurtas . . . . . . . . . . . . . . . . . . . . . . . 126
8.4 RedirecionandoparaasURLsoriginais. . . . . . . . . . . . . 131
8.5 Apresentandoopacoteurl . . . . . . . . . . . . . . . . . . . . 133
8.6 Especificandoaimplementaçãodorepositório . . . . . . . . 134
8.7 Criandoidentificadorescurtos. . . . . . . . . . . . . . . . . . 135
8.8 Implementandoorepositórioemmemória . . . . . . . . . . 138
9 Compilando e executando o projeto 1 4 1
9.1 Entendendooprocessodecompilação . . . . . . . . . . . . . 142
9.2 Instalandooexecutávelnosistema . . . . . . . . . . . . . . . 143
9.3 Aprendendomais . . . . . . . . . . . . . . . . . . . . . . . . . 144
10 Colhendo estatísticas 1 4 5
10.1 Realizandoacontagemnorepositório . . . . . . . . . . . . . 146
10.2 Registrandoosacessosnoservidor . . . . . . . . . . . . . . . 147
10.3 SerializandoJSON. . . . . . . . . . . . . . . . . . . . . . . . . 151
10.4 VisualizandoasestatísticascomoJSON . . . . . . . . . . . . 153
11 Refatorando o código 159
11.1 Substituindovariáveisglobais . . . . . . . . . . . . . . . . . . 160
11.2 Reduzindoaduplicaçãodecódigo . . . . . . . . . . . . . . . 163
11.3 Escrevendologs . . . . . . . . . . . . . . . . . . . . . . . . . . 165
11.4 Flexibilizandoainicializaçãodoservidor. . . . . . . . . . . . 167
12 Próximos passos 171
12.1 Aprendendomais . . . . . . . . . . . . . . . . . . . . . . . . . 172
Bibliografia 173
Versão: 17.3.30
ix

## Página 15

Capítulo1
Intro dução
Desenvolverum softwarenuncafoiumatarefafácil.Escreverumprograma,
pormenorqueeleseja,exigealtasdosesdeconcentração,paciênciaeatenção
aosdetalhes.Porvezesosproblemasparecemnãotersolução. Enadadisso
parecetermudadomuitocomopassardotempo:novaslinguagensdepro-
gramaçãoenovasferramentassãocriadastodososdiasporprogramadores
aoredordomundo,enquantoonúmerodedesafiosnãodiminui.
Aocontrário,numaépocaemqueprocessadorescommúltiplosnúcleos
(multi-core processors)estão presentesatémesmoemdispositivosmóveis,
programadoreseadministradoresdesistemassofremparatentarusaraomá-
ximoosrecursosdamáquinasemquehajaimpactoparaseususuários–ta-
refaquesetornamaisdifícilconformeonúmerodeusuárioscresce.
Nãoexistenenhumalinguagemdeprogramaçãocapazderesolvertodos
estesproblemasdeformafácil.Noentanto,alinguagemGosurgiunumam-
bienteondetaisproblemassãoaindamaisextremos:oGoogle.

## Página 16

1.1.PorqueGo? CasadoCódigo
A p e s a rdebastanteinspiradanalinguagemC,Gopossuicaracterísticas
demaisaltonível,comoabstrações paraalgumasestruturasdedados,coleta
delixo(garbage collection)e d u c ktyping,alémdetrazerumaabordagemmo-
dernaeeleganteparaacriaçãodeaplicações concorrentes.Gotambéminclui
umaextensabibliotecapadrãocomferramentasparacomunicaçãoemredes,
servidoresHTTP,expressões regulares,leituraeescritadearquivosemuito
mais.
OobjetivodestelivroéapresentaraoleitorosrecursosdalinguagemGoe
importantespartesdabibliotecapadrão,sempretrazendoexemplosrelevan-
tesquedemonstramousodecadarecurso.
Resolverosproblemascitadosanteriormenteéumdesafioenorme,mas
Goveioparatornarestatarefaumpoucomaisprazerosa.
1.1 Por que Go?
GonasceucomoumprojetointernonoGoogle,iniciadoem2007porRob
Pike,Ken ThompsoneRobertGriesemer,eposteriormentelançadocomo
umprojetodecódigoabertoemnovembrode2009. Pikee Thompsonjá
haviamtrabalhadojuntosnoBellLabs,oberçodoUnixedoPlan9–osistema
operacionalquedeuorigemàsferramentasdecompilaçãousadascomobase
dodesenvolvimentodalinguagemGo.
Noartigo(eminglês)“GoatGoogle:LanguageDesignintheServiceof
SoftwareEngineering”(http://talks.golang.org/2012/splash.article),RobPike
atribuioslongosperíodosdecompilaçãoeadificuldadeemescalarodesen-
volvimentodegrandesaplicaçõescomosendoosprincipaismotivadorespara
acriação danovalinguagem. Segundoele,amaiorpartedoproblemaéa
formacomqueaslinguagensCeC++tratamogerenciamentodedependên-
ciasentreosdiversosarquivos-fonte.
Dentrodestecenário,Gofoiconcebidacomoobjetivodetornarodesen-
volvimentodeservidoresnoGoogleumatarefamaisprodutivaeeficiente.
Paraevitarosproblemasdecompilação,Goimplementaumcontroleri-
gorosoeinteligentededependências,baseadonadefiniçãoeusode packages
(pacotes).
Comumasintaxebastantelimpa,secomparadacomoutraslinguagens
2

## Página 17

CasadoCódigo Capítulo1.Introdução
inspiradasemC–comoC++eJava–,Gopermiteaescritadeprogramas
concisoselegíveis,alémdefacilitarbastanteaescritadeferramentasquein-
teragemcomocódigo-fonte.Bonsexemplosdetaisferramentassão go fmt
(formataocódigodeacordocomoguiadeestilodalinguagem)e go fix
(reescrevepartesdocódigoqueusaAPIsdepreciadasparaqueusemasnovas
APIsintroduzidasemversões maisrecentes).
Gopossuitipagemforteeestática,porémintroduzumaformacurtade
declaraçãodevariáveisbaseadaeminferênciadetipos,evitandoredundân-
ciaeproduzindocódigomuitomaissucintodoquelinguagensestaticamente
tipadastradicionais.Alémdisso,Gotrazumaimplementaçãode d u c ktyping
(sefaz“ q u a c k ”comoumpatoeandacomoumpato,entãoprovavelmente é
umpato)baseadaeminterfaces,permitindoacriaçãodetiposbastanteflexí-
veis.
Algunstiposdecoleção dedadoscomo slices(listasdetamanhodinâ-
mico)e maps(dicionáriosdedadosassociativos)são nativosàlinguagem,
quetambémforneceumconjuntodefunções embutidasparaamanipulação
destestipos; a r r a y s(listasdetamanhofixo)tambémestão disponíveispara
casosemqueumnívelmaiordecontroleénecessário.
Gosuportaousodeponteiros(referênciasaendereçosdememória),o
quetornaaindamaisfácilacriaçãodepoderosostiposcustomizados.Entre-
tanto,aritméticasobreponteirosnãoésuportada.A p e s a rdetodaaflexibi-
lidade,atravésdousodeumcoletordelixo(ou garbage collector),Goreduz
drasticamenteacomplexidadenogerenciamentodememóriadasaplicações,
tornando-asmaisrobustaseevitandovazamentosdescuidados.
Gotambémfornecerecursosquepermitemaescritadeprogramastotal-
menteprocedurais,orientadosaobjetos(atravésdadefiniçãodenovostipose
defunçõesqueoperamsobretaistipos)oufuncionais–funçõessãomembros
deprimeiraclasseemGo,quetambémsuportaacriaçãode c l o s u r e s(funções
queherdamocontextodeondeelasforamdefinidas).
AabordagemdeGoparaconcorrênciaéumdosmaioresdiferenciaisda
linguagem.Inspiradanofamoso paperdeC.A.R.Hoare CommunicatingSe-
quential Processes[2],Goimplementa goroutines–processosextremamente
levesquesecomunicamatravésde channels,evitandoousodememóriacom-
partilhadaedispensandoousodetravas,semáforoseoutrastécnicasdesin-
3

## Página 18

1.2.Instalação CasadoCódigo
cronizaçãodeprocessos.
Comtodosestesrecursosdisponíveis,chegouahoradevercomoGofun-
cionanaprática.
1.2 Instalação
OprimeiropassoparacomeçaraescreverprogramasemGoéinstalaralin-
guagemesuasferramentas.Ospacotesdedistribuiçãoestãodisponíveisno
sitehttp://golang.org/dl/.Nomomentodaescritadestelivro,aversãoestá-
veldisponíveléa 1.3.Façaodownloaddopacotereferenteaoseusistema
operacional.Aseguirvocêencontraráasinstruções específicasparacadapla-
taforma.
Linux
Abraumterminal,váparaodiretórioondevocêsalvouoarquivoda
distribuição (no caso do Linux, o nome do arquivoseráparecido com
go1.3.linux-amd64.tar.gz)eexecuteocomandoaseguir:
sudo tar -C /usr/local -xzf go1.3.linux-amd64.tar.gz
AsferramentasdalinguagemGoagoraestarãodisponíveisnodiretório
/usr/local/go.Adicioneodiretório /usr/local/go/binàvariávelde
ambiente PATHparateracessoàsferramentas,independentedodiretório
ondevocêestivernosistema. V o c êpodefazerissoadicionandoaseguinte
linhaaoseuarquivo $HOME/.profile:
export PATH=$PATH:/usr/local/go/bin
Paraverificarseainstalaçãoestácorreta,executeoseguintecomandono
terminal:
$ go version
Estecomandodeveráproduzirumasaídasimilaràseguinte:
go version go1.3 linux/amd64
4

## Página 19

CasadoCódigo Capítulo1.Introdução
Ma cOS
NoMacOSháduasformasdeinstalação.Amaissimpleséidênticaàno
Linux,sendoaúnicadiferençaonomedoarquivodedistribuição:
sudo tar -C /usr/local -xzf go1.3.darwin-amd64-osx10.8.tar.gz
A outra opção é baixar o instalador automático
go1.3.darwin-amd64-osx10.8.pkg.Execute-oesigaasinstruções.
Asduasformasdisponibilizamasferramentasinstaladasnodiretório
/usr/local/go. A p ó sainstalação,assimcomonoLinux,adicioneodi-
retório /usr/local/go/binàvariáveldeambiente PATHnoseuarquivo
$HOME/.profile:
export PATH=$PATH:/usr/local/go/bin
Everifiqueseainstalaçãoestácorreta,executandooseguintecomando
noterminal:
$ go version
Estecomandodeveráproduzirumasaídasimilaraoquesegue:
go version go1.3 darwin/amd64
Windows
NoWindows,assimcomonoMacOS,háduasformasdeinstalação. A
formarecomendadaéautilizaçãodoinstaladorautomático.Façaodownload
doarquivo go1.3.windows-amd64.msi,execute-oesigaasinstruções
passoapasso.A p ó sainstalação,asvariáveisdeambienteserãoautomatica-
menteconfiguradasevocêpoderáseguirparaasinstruçõesdepós-instalação.
A forma alternativa é fazer o download do pacote
go1.3.windows-amd64.zip e descompactá-lono diretório C:\Go.
Emseguida,adicioneodiretório C:\Go\binàvariáveldeambiente PATH.
Paratercertezadequeainstalaçãofoibem-sucedida,executeoseguinte
comandonoprompt:
C:\>go version
5

## Página 20

1.2.Instalação CasadoCódigo
Estecomandodeveráproduzirumasaídasimilaràseguinte:
go version go1.3 windows/amd64
Instalando G oem um diretório não-padrão
T o d a sasinstruções apresentadasanteriormentepartemdoprincípiode
queainstalaçãofoifeitanodiretóriopadrão–/usr/local/gonoLinux
eMacOS,e C:\GonoWindows.Casovocênãotenhaestaopçãooupre-
firarealizarainstalação emumdiretóriodiferente,algumasconfigurações
adicionaissãonecessárias.
Paraquetudofuncionecomoesperado,éprecisoconfiguraravariável
deambiente GOROOTparareferenciarodiretórioescolhidoparaainstala-
ção.Porexemplo,seainstalaçãofoifeitanodiretório $HOME/gonoLinux,
adicioneaseguinteconfiguraçãoaoseu $HOME/.profile:
export GOROOT=$HOME/go
export PATH=$PATH:$GOROOT/bin
NoWindows,umaconfiguraçãosemelhantedeveserfeita.
Entretanto,paraevitarproblemas,érecomendávelqueodiretóriopadrão
sejautilizado.
Pós-instalação
Apartirdestemomento,todososexemplosdecomandosserãoescritos
utilizandoanotaçãoUnix,assumindoquevocêtemumainstalaçãofuncional
dalinguagemGoequeodiretório GOROOT/binfoiadicionadoàvariável
PATH(sendoque GOROOTdeveserodiretórionoqualGofoiinstalada).
Paraextrairomáximodasferramentasdisponíveisnainstalação,preci-
samoscriarumdiretóriodetrabalho(workspace)ondetodososprogramas
devemresidir.Aestruturadoworkspaceincluitrêssubdiretórios:
•srccontémocódigo-fontedetodososseusprogramasescritosem
Go(organizadosempacotes),etambémocódigo-fontedepacotesde
terceirosinstaladosemseusistema;
•pkgcontémobjetosreferentesaospacotes;
6

## Página 21

CasadoCódigo Capítulo1.Introdução
•bincontémarquivosexecutáveisgeradosnoseusistema.
Crieumworkspaceeadicione-oàvariáveldeambiente GOPATH:
$ mkdir $HOME/go
Para maior conveniência,configure a variável GOPATH no seu ar-
quivo $HOME/.profile (ounasconfigurações avançadasdoseuWi n-
dowsconformemencionadoanteriormente),eadicionetambémodiretório
GOPATH/binàvariáveldeambiente PATH:
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
1.3 O primeiro programa em Go
ProgramasemGopodemserescritosemqualquereditordetextosquetenha
suporteàcodificação UTF-8. Osarquivos-fontes devemnecessariamente
sersalvosnestacodificação,casocontrárioocompiladornãoserácapazde
processá-los.
AgorapodemosfinalmenteescrevernossoprimeiroprogramaemGo.
Crieumnovodiretóriochamado cap1-oladentrode $GOPATH/src.No
diretóriorecém-criado,utilizeseueditordetextosfavoritoecrieumnovo
arquivochamado ola.gocomoseguinteconteúdoesalveoarquivo:
package main
import "fmt"
func main() {
fmt.Println("Olá, Go!")
}
Paraexecutaroprograma,utilizaremosaferramenta go.V áparaodire-
tório $GOPATH/srceexecuteoseguintecomando:
$ go run cap1-ola/ola.go
7

## Página 22

1.3.OprimeiroprogramaemGo CasadoCódigo
A p ó saexecuçãodoprograma,otexto“Olá,Go!”deveráserimpressono
terminal.
Arquivos-fontecontendocódigoGodevemseguirsempreamesmaes-
trutura,divididaemtrêsseções: primeiro,adeclaração dopacote,seguida
dadeclaraçãodospacotesexternosdosquaisoarquivo-fontedepende,epor
fim,ocódigoreferenteaoprogramaoupacotesendoescrito.
T o d ocódigoGodeveobrigatoriamenteexistirdentrodeumpacote(pac-
kage),etodoprogramaemGodeveterumpacote maincontendoumafun-
ção main()queservecomopontodepartidadoprograma.
Noexemploanterior,importamosopacote fmt,quecontémfunções
paraaformataçãode strings,eutilizamosafunção Printlnparamostrar
otexto“Olá,Go!”paraousuário.
Reparequeafunção main()nãorecebenenhumargumentoenãore-
tornanenhumvalor.DiferentedelinguagenscomoJavaeC,argumentospas-
sadosparaumprogramaGoatravésdalinhadecomandonãosãoautomati-
camentedisponibilizadosaoprograma.Emvezdisso,precisamosutilizarum
pacotechamado os,queseráapresentadoposteriormente.
Agorajátemosumambientededesenvolvimentofuncional,eacabamos
deescreveroprimeiroprogramaemGo.
Noscapítulos2e3,veremosalgunsexemplosqueapresentarãoasintaxe
básicaealgunsdosrecursosdalinguagem.Noscapítulosposteriores,entra-
remosemdetalhessobreasfuncionalidadesmaisimportantes.
8

## Página 23

Capítulo2
Explorandoasintaxebásica
Agoraquevocêjátemumambientecapazdecompilareexecutarprogramas
emGo,vamosfazerumpequenopasseiosobreasprincipaiscaracterísticasda
linguagemcomalgunsexemplosguiados.Oobjetivodosexemplosaseguir
éfamiliarizaroleitorcomoselementosmaiscomunsdasintaxe,asprinci-
paispalavrasreservadaseestruturasdecontrole,alémdeapresentaralguns
idiomascomunsnodesenvolvimentodeaplicações emGo.
Todososexemplosdecódigodestelivroestãodisponíveisparaconsulta
noendereçohttps://github.com/caiofilipini/casadocodigo-go.
Osrecursosapresentadosnosexemplosserãoexplicadosemmaioresde-
talhesnospróximoscapítulos.
2.1 Estrutura d ocapítulo
Estecapítuloébaseadoemdoisexemplos.

## Página 24

2.2.Ifeexpressões lógicas CasadoCódigo
Oprimeiroéumsimplesconversordemedidasqueapresentaráousode
algunselementosbásicosdalinguagem,comoasestruturasdecontrole ife
for,oconceitode slicesetratamentobásicodeerros.Esteexemplopodeser
encontradonaseção2.4.
Osegundo,encontradonaseção2.6,éumaimplementaçãodoalgoritmo
deordenação q u i c k s o r t,eintroduzousodefunções, recursividadeeafunção
append().
Antesdeapresentarosexemplos,porém,veremosofuncionamentobá-
sicodasexpressões ifeoquesão a r r a y se slices.
2.2 If e expressões lógicas
EmGo,diferentedealgumaslinguagens,somenteexpressões devalorlógico
verdadeirooufalsopodemserutilizadasemconjuntocominstruções if.
Estasexpressões devemnecessariamenteserdotipo bool–cujosúni-
cosvalorespossíveissão truee false–epodemservariáveisoumesmo
funções oumétodos,desdequeretornemumvalordotipo bool.
2.3 Ar r a y se slices
Gopossuidoistipospadrões paralistasdedados: arrayse slices.
U marrayéumalistadetamanhofixo,similaraum arraynaslingua-
gensCouJava.
Jáum sliceéumacamadadeabstraçãocriadacombasenos arrays
epodecrescerindefinidamente,proporcionandoumaflexibilidademuito
maior.
Asdiferençasentreelesserãodiscutidasemdetalhesnocapítulo4.
2.4 Exemplo 1: conversor de medidas
Oprimeiroexemploéumsimplesconversordemedidas.Eleaceitacomoen-
tradaumalistadevalorescomsuaunidadedemedida,eproduzumalistade
valoresconvertidos.Porquestões didáticas,oconversortrabalhaapenascom
doistiposdeconversões: degrausCelsiusparaFahrenheit,edequilômetros
pramilhas.
10

## Página 25

CasadoCódigo Capítulo2. Explorandoasintaxebásica
package main
import (
"fmt"
"os"
"strconv"
)
Aprimeiraseçãodoprogramanãoémuitodiferentedoquejávimosan-
teriormente.Porém,comoesteexemploéumpoucomaiscomplexo,impor-
tamosopacote fmt,mastambémprecisamosdospacotes ose strconv.
Opacote ospossuiumasériedeoperações quelidamcomosistema
operacionalhospedeirodeformaindependente,facilitandoaescritadeapli-
cações multiplataformas.Noexemploaseguir,utilizaremosestepacotepara
teracessoaosargumentospassadosaonossoprogramavialinhadecomando,
etambémparainstruiroprogramaainterrompersuaexecuçãoeretornarum
códigodeerroadequadoemcasosexcepcionais.
Jáopacote strconvforneceumagrandevariedadedefunções paraa
conversãode stringsparaoutrosformatosevice-versa. Osargumentos
recebidosvialinhadecomandosão sempretratadoscomo strings,por-
tanto,paraqueonossoconversorsejacapazderealizaroperações matemá-
ticassobreosvalores,utilizaremosopacote strconvparaconvertê-losem
númerosdecimais.
Aseguirprecisamosdeclararafunção main()que,conformevistono
capítuloanterior,nãorecebeargumentosenãoretornanenhumvalor.Ocon-
teúdodestafunçãoserádiscutidopassoapasso.
func main() {
// ...
}
Comoemqualquerprogramaquedependedaentradadedadosdeusuá-
rios,aprimeiracoisaqueoconversorfazégarantirqueosargumentospassa-
dosvialinhadecomandoestãoemumformatominimamentesão.Paraisso,
verificamosaquantidadedeargumentosrecebidos–presentesem os.Args
–atravésdousodafunçãoembutida len().
11

## Página 26

2.4. Exemplo1:conversordemedidas CasadoCódigo
os.Argscontémumalista(tecnicamenteum slice)detodososargumen-
tospassadosparaoprograma,sendoqueporpadrãooprimeiroargumento
sempreseráopróprionomedoprogramaexecutado.Portanto,verificamos
se os.Argspossuipelomenostrêsargumentos–onomedoprograma;pelo
menosumvaloraserconvertido;eaunidadereferenteaosvalores–através
dainstruçãodecontrole if.
Casoaquantidadedeargumentosfornecidossejamenordoquetrês,uti-
lizamosajáconhecidafunção Printlndopacote fmtparaapresentarao
usuárioumamensagemdeajudacomoformatodeentradadoprograma,
elogodepoisutilizamosafunção os.Exit()paraabortaraexecuçãodo
programa.Notequeafunção os.Exit()foichamadacomovalor 1como
argumento;ovalorespecificadoéretornadocomocódigodeerroparaosis-
temaoperacional.Seguindoospadrões deprogramasUnix,qualquervalor
diferentede 0indicaumaexecuçãoanormal.
if len(os.Args) < 3 {
fmt.Println("Uso: conversor <valores> <unidade>")
os.Exit(1)
}
Seguindoaexecuçãoquandotrêsoumaisargumentosforamfornecidos,
encontramosadeclaraçãoeatribuiçãodeduasvariáveis: unidadeOrigem
e valoresOrigem.EmGo,quandoumavariávelédeclaradaeatribuídana
mesmaoperação,nãoéprecisoinformarseutipo–ocompiladoréinteligente
osuficienteparaadivinhá-lobaseadonaoperaçãodeatribuição;ouseja,caso
ovalor 10sejaatribuídoàvariávelx,ocompiladorsabequeotipode xé
umnúmerointeiro,ou intemGo.
Atribuímosà unidadeOrigemoúltimoargumentopassado,deacordo
comoformatoesperado. Paraisso,acessamosaúltimaposição do slice
os.Args. Slicessão listasindexadasedetamanhovariávelemGo,sendo
queoprimeiroelementopossuiíndice 0.Sendoassim,oíndicedoúltimo
elementoésempre n - 1,sendo nonúmerototaldeelementospresentes
noslice–nocaso, len(os.Args)-1.
unidadeOrigem := os.Args[len(os.Args)-1]
12

## Página 27

CasadoCódigo Capítulo2. Explorandoasintaxebásica
AvariávelvaloresOrigemrecebeumasublistadosargumentos,des-
cartandooprimeiro(onomedoprograma)eoúltimo(aunidadejáatribuída
à unidadeOrigem).EmGo,estetipodeoperaçãoétrivialeconhecidacomo
slicing(fatiar,separar)–daívemonomedadoaotipodelistasdinâmicas.
Assim,fatiamosalistacompletadeargumentos,obtendosomenteosvalores
quedevemosconverter: os.Args[1 : len(os.Args)-1]. Oíndice 1
refere-seaosegundoelemento,e len(os.Args)-1aoúltimoelemento,que
édesconsideradonosliceretornado.
valoresOrigem := os.Args[1 : len(os.Args)-1]
U m avezqueidentificamosaunidade-origemeosvaloresaseremconver-
tidos,precisamosdescobrirqualéaunidade-destinoe,consequentemente,
qualfórmuladeconversãodeveráserusada.Conformemencionadoanteri-
ormente,nossoprogramasósabeconvertergrausCelsiusparaFahrenheite
quilômetrosparamilhas.
DeclaramosavariávelunidadeDestinocomosendodotipo string.
Comoseuconteúdodependedeumaverificaçãoe,portanto,nãopodemos
atribuiraelaumvalornomomentodadeclaração, precisamosutilizara
palavra-chave varantesdonomedavariável,enestecasoprecisamostam-
béminformarseutipologoapósonome.Sevocêestáacostumadocomlin-
guagenscomoCeJava,podeacharaordemdadeclaraçãoumpoucoestra-
nha–nestaslinguagens,declara-seprimeirootipoedepoisonomedavariá-
vel.ReparecomoemGoaleituradadeclaraçãoficamaisfluida:declareuma
variávelcomnome unidadeDestinodotipo string.
var unidadeDestino string
Paraatribuirovalorcorretoà unidadeDestino,verificamosocon-
teúdode unidadeOrigem:casosejaa string "celsius",atribuímos
"fahrenheit";casoseja "quilometros",atribuímos "milhas";caso
sejaqualqueroutrovalordesconhecido,informamosestefatoaousuárioein-
terrompemosaexecuçãodoprograma.Noteque,destavez,utilizamosafun-
ção fmt.Printf,queimprimenasaídapadrãouma stringdeacordocom
oformatoespecificado,similaràfunção printfdalinguagemC.Nestecaso,
especificamosoformato %s não é uma unidade conhecida!,onde
%sserásubstituídopelovalordavariávelunidadeDestino.
13

## Página 28

2.4. Exemplo1:conversordemedidas CasadoCódigo
if unidadeOrigem == "celsius" {
unidadeDestino = "fahrenheit"
} else if unidadeOrigem == "quilometros" {
unidadeDestino = "milhas"
} else {
fmt.Printf("%s não é uma unidade conhecida!",
unidadeDestino)
os.Exit(1)
}
Agoraqueconhecemosaunidade-origem,osvaloresaseremconver-
tidosetambémaunidade-destino,vamosàconversão propriamentedita.
Paraconvertertodososvaloresinformados,precisamospercorreroslice
valoresOrigem,transformarcadavaloremumnúmerodecimal,aplicar
afórmulasobreestenúmeroeimprimiroresultado.
Gopossuiapenasumaestruturaderepetição, for,quepodeserusada
dediferentesformasdeacordocomocontexto;nonossocaso,utilizamos
foremconjuntocomooperador rangeparaobteracessoacadaelemento
doslice valoresOrigem.Ooperador range,quandoaplicadoaumslice,
retornadoisvaloresparacadaelemento:primeiro,oíndicedoelementono
slice,edepois,oelementopropriamentedito.Atribuímosoíndiceàvariável
ieoelementoà v.
for i, v := range valoresOrigem {
// ...
}
Emseguida,utilizamosafunção ParseFloat()dopacote strconv
paraconvertera stringemumnúmerodepontoflutuante.Estafunção
recebedoisargumentos–ovaloraserconvertidoeaprecisãodovalorretor-
nado(32ou64bits)–eretornadoisvalores:ovalorconvertidoeumerrode
conversão(queé nilquandoovaloréconvertidocomsucesso).Casoum
erroaconteça,informamosaousuário(novamenteutilizando fmt.Printf
paramostrarcorretamenteovalor–string,representadocomo %snofor-
mato–esuaposiçãonalistadeargumentos–int,representadocomo %d)
einterrompemosaexecuçãodoprograma.
14

## Página 29

CasadoCódigo Capítulo2. Explorandoasintaxebásica
valorOrigem, err := strconv.ParseFloat(v, 64)
if err != nil {
fmt.Printf(
"O valor %s na posição %d não é um número válido!\n",
v, i)
os.Exit(1)
}
Comovalorcorretoemmãos, declaramosavariável valorDestino
comosendodotipo float64,verificamosqualéaunidade-origeme,apli-
candoafórmulacorrespondenteàunidade,atribuímosaelaovalorconver-
tido.
var valorDestino float64
if unidadeOrigem == "celsius" {
valorDestino = valorOrigem*1.8 + 32
} else {
valorDestino = valorOrigem / 1.60934
}
Porfim,utilizamosnovamenteafunção fmt.Printfparaapresentar
ovalorconvertidoesuaunidadeaousuário.Reparequeutilizamos %.2f
parainformaràfunçãoqueovalorédotipo floatedeveserarredondado
eformatadocomduascasasdecimais.
fmt.Printf("%.2f %s = %.2f %s\n",
valorOrigem, unidadeOrigem, valorDestino, unidadeDestino)
Aseguir,vocêencontraocódigocompletodoconversor.Paraexecutá-lo,
crieumnovodiretóriochamado cap2-conversorem $GOPATH/srce,
dentrodele,crieumarquivochamado conversor.gocomoconteúdo:
package main
import (
"fmt"
"os"
"strconv"
15

## Página 30

2.4. Exemplo1:conversordemedidas CasadoCódigo
)
func main() {
if len(os.Args) < 3 {
fmt.Println("Uso: conversor <valores> <unidade>")
os.Exit(1)
}
unidadeOrigem := os.Args[len(os.Args)-1]
valoresOrigem := os.Args[1 : len(os.Args)-1]
var unidadeDestino string
if unidadeOrigem == "celsius" {
unidadeDestino = "fahrenheit"
} else if unidadeOrigem == "quilometros" {
unidadeDestino = "milhas"
} else {
fmt.Printf("%s não é uma unidade conhecida!",
unidadeDestino)
os.Exit(1)
}
for i, v := range valoresOrigem {
valorOrigem, err := strconv.ParseFloat(v, 64)
if err != nil {
fmt.Printf(
"O valor %s na posição %d " +
"não é um número válido!\n",
v, i)
os.Exit(1)
}
var valorDestino float64
if unidadeOrigem == "celsius" {
valorDestino = valorOrigem*1.8 + 32
} else {
valorDestino = valorOrigem / 1.60934
16

## Página 31

CasadoCódigo Capítulo2. Explorandoasintaxebásica
}
fmt.Printf("%.2f %s = %.2f %s\n",
valorOrigem, unidadeOrigem,
valorDestino, unidadeDestino)
}
}
U mexemplodaexecuçãodoprograma:
$ go run cap2-conversor/conversor.go 32 27.4 -3 0 celsius
32.00 celsius = 89.60 fahrenheit
27.40 celsius = 81.32 fahrenheit
-3.00 celsius = 26.60 fahrenheit
0.00 celsius = 32.00 fahrenheit
Algumasdastécnicasapresentadasnesteexemplotambémserãoutiliza-
dasnospróximose,portanto,nãoserãoexplicadasnovamente.
2.5 Criando funções básicas
Antesdeimplementaropróximoexemplo,vejamosalgumasformasbásicas
paraadefiniçãodefunções:
func imprimirDados(nome string, idade int) {
fmt.Printf("%s tem %d anos.", nome, idade)
}
func main() {
imprimirDados("Fernando", 29)
}
Afunção imprimirDados()recebedoisargumentos,uma string
representandoo nome,eum intrepresentandoaidade,eimprimeosdois
argumentosatravésdousodafunção fmt.Printf().Assimcomoafunção
especial main(), imprimirDados()nãoretornanenhumvalor.
func soma(n, m int) int {
return n + m
17

## Página 32

2.6. Exemplo2:quicksortefunções CasadoCódigo
}
func main() {
s := soma(3, 5)
fmt.Println("A soma é", s)
}
Estaoutrafunçãosimples,denominada soma(),recebedoisargumen-
tos–ne m–dotipo interetornaasomadosdois,tambémdotipo int.
Noteque,comoosdoisargumentossãodomesmotipo,podemossimplifi-
carsuadeclaraçãoseparandoosnomesdosargumentoscomumavírgulae
especificandoseutipoumaúnicavez.
Agoraqueconhecemosobásicosobrefunções, vamosàimplementação
dopróximoexemplo.
2.6 Exemplo 2: quicksort e funções
Osegundoexemploéumaimplementaçãosimplesdofamosoalgoritmode
ordenação q u i c k s o r t.Aideiabásicadestealgoritmoé:
1)elegerumelementodalistacomopivôeremovê-lodalista;
2) particionaralistaemduaslistasdistintas:umacontendoelementosme-
noresqueopivô,eoutracontendoelementosmaiores;
3)ordenarasduaslistasrecursivamente;
4) retornaracombinaçãodalistaordenadadeelementosmenores,opróprio
pivô,ealistaordenadadeelementosmaiores.
Comoarecursividadeénaturalmentepartedestealgoritmo,nossaim-
plementação serábaseadaemumafunção recursiva. Esteexemploémais
complexodoqueoanterior,porémmuitomaisexpressivo,edemonstracomo
algumasconstruções dalinguagemajudamaescreverprogramasbastantesu-
cintos.
18

## Página 33

CasadoCódigo Capítulo2. Explorandoasintaxebásica
Implementando o quicksort
Nossoprogramalimita-seaordenarnúmerosinteiros.Osnúmerossão
recebidoscomoargumentosvialinhadecomandodeformamuitosimilarao
exemplodoconversordeunidades;adiferençaéquedestavezutilizamosa
função strconv.Atoi()paraconvertê-losemnúmerosinteirosemvezde
decimais.
Reparetambémqueadeclaraçãodoslice numeros,quearmazenaráos
númerosinteiros,ébastantediferentedaformaquefoiutilizadanoconver-
sor:aquiutilizamosafunçãonativa make()paracriareinicializarumslice
dotipo []int–umslicedenúmerosinteiros–especificandotambémseu
tamanhoinicialcomosendoomesmodalistarecebidacomoargumento,o
queésempreumaboaideiaquandosabemosdeantemãoqualseráotamanho
finaldoslice.
Depoisdeconverteraentradadoprogramaparaumalistadenúmerosin-
teiros,chamamosumafunçãodenominada quicksort(),passandocomo
argumentoalistadenúmerosaserordenadaeimprimindoalistaresultante.
func main() {
entrada := os.Args[1:]
numeros := make([]int, len(entrada))
for i, n := range entrada {
numero, err := strconv.Atoi(n)
if err != nil {
fmt.Printf("%s não é um número válido!\n", n)
os.Exit(1)
}
numeros[i] = numero
}
fmt.Println(quicksort(numeros))
}
Afunção quicksort()éresponsávelpelaimplementação doalgo-
ritmo. Elarecebecomoargumentoumslicedenúmerosinteiroseretorna
umsliceordenado,comopodemosvernaassinaturaaseguir:
19

## Página 34

2.6. Exemplo2:quicksortefunções CasadoCódigo
func quicksort(numeros []int) []int {
// ...
}
Oprimeiropassoéverificarsealistadeentradaestávaziaoucontém
apenasumnúmeroe,emcasopositivo,retornarapróprialista.Estacondi-
çãoéextremamenteimportanteemfunções recursivas;éachamada condição
de parada,queprevinequeafunçãosejaexecutadaeternamenteouatéque
aconteçaumasobrecarganapilhadeexecução(stack overflow).
if len(numeros) <= 1 {
return numeros
}
Opróximopassoécriarumacópiadosliceoriginalparaevitarqueeleseja
modificado.Utilizamosafunçãoembutida copy()paracopiaroconteúdo
doslice numerosparao n,queécriadocomomesmotamanhodoslice
original:
n := make([]int, len(numeros))
copy(n, numeros)
Apartirdesteponto,manipularemossomenteonovoslice n.Veremosa
função copy()emmaioresdetalhesnocapítulo4.2.
Emseguida,fazemosaescolhadopivô. Nestecaso,utilizamosumadas
técnicasmaissimpleseescolhemosoelementoqueseencontramaisoume-
nosnomeiodalista.Armazenamosoíndice–queseráimportanteembreve
–eoprópriopivô:
indicePivo := len(n) / 2
pivo := n[indicePivo]
Comopivô emmãos, precisamosremovê-lodalistaoriginal. Faremos
issoatravésdousodafunçãonativa append().Elaadicionaumelemento
aofinaldeumslice,esuaformageralé:
novoSlice := append(slice, elemento)
20

## Página 35

CasadoCódigo Capítulo2. Explorandoasintaxebásica
Issopodeparecerumtantoestranhoquandoqueremosdefato remover
umelementodoslice.Entretanto,combinandoouso append()comopera-
ções de slice,temosumaconstruçãobastantepoderosaeidiomáticaemGo:
n = append(n[:indicePivo], n[indicePivo+1:]...)
Primeiro, fatiamos o slice n do primeiro elemento atéo pivô –
n[:indicePivo] –eutilizamosestenovoslicecomobaseparaaope-
ração de append(); depois, fatiamos novamente n, partindo do ele-
mentoimediatamenteposterioraopivô atéoúltimoelementodisponível–
n[indicePivo+1:]–eutilizamosesteslicecomovaloraseradicionado
aoslice-base.Émuitoimportantenotarousodasreticênciasaofinaldose-
gundoargumento:estamosinformandoquetodososelementosdosegundo
slicedevemseradicionadosaoslice-base.
Oresultadodestaoperação éumalistaquecontémtodososelementos
anterioresaopivô, etodososelementosposterioresaele, excetoopróprio
pivô.Missãocumprida!
Opróximopassodoalgoritmoéparticionaroslicedenúmerosemdois
novosslices–umcontendotodososelementosmenoresouiguaisaopivô,e
outrocontendosomenteoselementosmaiores.Estatarefaédelegadaauma
outrafunçãochamada particionar(),queseráexplicadaembreve.Note
quetiramosproveitodofatodequeafunção particionar()retornadois
valoresdistintos–doisslices:
menores, maiores := particionar(n, pivo)
Oúltimopassoéordenarestesdoisslicesrecursivamenteecombinar
osresultadoscomopivô, eéexatamenteoqueaúltimalinhadafunção
quicksort()faz–novamenteatravésdousodafunção append():
return append(
append(quicksort(menores), pivo),
quicksort(maiores)...)
Primeiro,chamamos quicksort()recursivamenteparaordenaroslice
menores;depoisadicionamoso pivoaoresultadodestaordenação; em
seguida,fazemosoutrachamadarecursivaa quicksort()paraordenar
21

## Página 36

2.6. Exemplo2:quicksortefunções CasadoCódigo
oslice maiores; eporfim,combinamosasduaslistasordenadascom
append()demaneirasimilaràapresentadaanteriormenteeretornamos.
Aseguiralistagemcompletadafunção quicksort():
func quicksort(numeros []int) []int {
if len(numeros) <= 1 {
return numeros
}
n := make([]int, len(numeros))
copy(n, numeros)
indicePivo := len(n) / 2
pivo := n[indicePivo]
n = append(n[:indicePivo], n[indicePivo+1:]...)
menores, maiores := particionar(n, pivo)
return append(
append(quicksort(menores), pivo),
quicksort(maiores)...)
}
Parafinalizar,vamosanalisaraassinaturadafunção particionar():
func particionar(
numeros []int,
pivo int) (menores []int, maiores []int) {
// ...
}
Estafunçãorecebedoisargumentos–umslice numeros []inteum
pivo int–eretornadoisvalores–umslice menores []intcontendo
todososnúmerosmenoresouiguaisao pivoeumslice maiores []int
contendoosnúmerosmaioresqueo pivo. Aimplementação completaé
bastantetrivialetambémfazusodafunção append()apresentadaanteri-
ormente.
22

## Página 37

CasadoCódigo Capítulo2. Explorandoasintaxebásica
func particionar(
numeros []int,
pivo int) (menores []int,maiores []int) {
for _, n := range numeros {
if n <= pivo {
menores = append(menores, n)
} else {
maiores = append(maiores, n)
}
}
return menores, maiores
}
U mdetalheimportanteenovoqueaparecenafunção particionar()é
apresençadosímbolo _,conhecidocomo identificador vazio(ou b l an kiden-
tifie r).Comojávimosanteriormente,ooperador range,quandoutilizado
paraiterarsobreumslice,retornasempredoisvalores:oíndicedoelementoe
opróprioelemento.Muitasvezesnãoprecisamosdosdoisvalores,porémem
Goumavariáveldeclaradaenãoutilizadacausaumerrodecompilação.Para
resolveresteproblema,utiliza-seoidentificadorvazioparaignorarumvalor
quenãoseráusado.Istoseaplicaaqualqueroperaçãoqueretornemúltiplos
valoresenãoserestringeapenasaooperador range.
Aseguirvocêencontraalistagemcompletadanossaimplementaçãode
quicksort. Crieumdiretóriochamado cap2-quicksortlogoabaixodo
diretório $GOPATH/src,edentrodelecrieoarquivo quicksort.gocom
oconteúdoaseguir:
package main
import (
"fmt"
"os"
"strconv"
)
func main() {
23

## Página 38

2.6. Exemplo2:quicksortefunções CasadoCódigo
entrada := os.Args[1:]
numeros := make([]int, len(entrada))
for i, n := range entrada {
numero, err := strconv.Atoi(n)
if err != nil {
fmt.Printf("%s não é um número válido!\n", n)
os.Exit(1)
}
numeros[i] = numero
}
fmt.Println(quicksort(numeros))
}
func quicksort(numeros []int) []int {
if len(numeros) <= 1 {
return numeros
}
n := make([]int, len(numeros))
copy(n, numeros)
indicePivo := len(n) / 2
pivo := n[indicePivo]
n = append(n[:indicePivo], n[indicePivo+1:]...)
menores, maiores := particionar(n, pivo)
return append(
append(quicksort(menores), pivo),
quicksort(maiores)...)
}
func particionar(
numeros []int,
pivo int) (menores []int, maiores []int) {
for _, n := range numeros {
24

## Página 39

CasadoCódigo Capítulo2. Explorandoasintaxebásica
if n <= pivo {
menores = append(menores, n)
} else {
maiores = append(maiores, n)
}
}
return menores, maiores
}
Paraveresteexemploemexecução,utilizeocomandoaseguir:
$ go run cap2-quicksort/quicksort.go 10 30 41 53 78 12 19 22
[10 12 19 22 30 41 53 78]
Nestecapítulo,aprendemosautilizarobásicodasestruturasdecontrole
ife for. T a m b é mvimosoquesão arrayse slices,eaprendemosa
criarnossasprópriasfunções.
OstiposdecoleçãodisponíveisemGo,incluindo arrayse slices,se-
rãodiscutidosemdetalhesnocapítulo4.Asfunções etodososseusrecursos
serãoapresentadosnocapítulo6.
25

## Página 41

Capítulo3
Indoalém:maisexemplos
Nocapítuloanterior,aprendemosalgunselementosbásicosdasintaxeealgu-
masdasconstruções maisfundamentaisemGo.Nestecapítuloavançaremos
umpoucomaisatravésdeexemplosqueutilizam maps(dicionáriosdeda-
dos)etiposcustomizados.
3.1 Exemplo 3: mapas e estatísticas
U mmap–tambémconhecidocomoarrayassociativooudicionário–éuma
coleçãodepares chave/valorsemordemdefinida,emquecadachaveéúnica
earmazenaumúnicovalor.
Oexemploaseguirutilizaum map paracontarafrequênciadepa-
lavrascomas mesmasiniciais. Recebemos a lista de palavras via linha
de comando,assimcomojáfizemosnosexemplosanteriores. Armaze-
namosalistaemumslicedenominado palavras,chamamosafunção

## Página 42

3.1.Exemplo3:mapaseestatísticas CasadoCódigo
colherEstatisticas()utilizandooslice palavrascomoargumento,
armazenamosasestatísticasnumavariávele,porfim,chamamosafunção
imprimir()paraimprimi-las.
package main
import (
"fmt"
"os"
"strings"
)
func main() {
palavras := os.Args[1:]
estatisticas := colherEstatisticas(palavras)
imprimir(estatisticas)
}
Nenhumanovidadeatéaqui,excetopelofatodequeimportamosopacote
strings. Estepacotecontémumagamadefunções paramanipulação de
strings.
Afunção colherEstatisticas()possuiaseguinteassinatura:
func colherEstatisticas(palavras []string) map[string]int
Reparequeotipoderetornoé map[string]int:um mapcomchaves
dotipo stringevaloresdotipo int,idealparaarmazenarasestatísticas
quedesejamos.Paracadaitemarmazenado,achaveéaletrainicialdapalavra
eovaloréaquantidadedepalavrascomestainicial.
Dentrodafunçãodeclaramoso mapqueiráarmazenarasestatísticase
damosaeleonome estatisticas.Parainicializarum maputilizamosa
função make(),similaràinicializaçãodeslices:
estatisticas := make(map[string]int)
Emseguida,paracadapalavra,extraímossualetrainicial–palavra[0]
–e,utilizandoafunção ToUpper()dopacote strings,convertemosa
28

## Página 43

CasadoCódigo Capítulo3.Indoalém:maisexemplos
inicialparamaiúsculaeaarmazenamosnavariávelinicial.Destaforma,
garantimosquenãohajadistinçãodepalavrasescritasemcaixaaltaoubaixa.
Comainicialemmãos,procuramosnomapa estatisticasumaen-
tradacujachavesejaestainicial:
contador, encontrado := estatisticas[inicial]
Paraacessarumvaloremum map,utilizamosumanotação similarao
acessodevaloresemumslice,porémutilizamosa c h a v edovalorentreos
colchetes–nonossocaso,a stringrepresentandoaletrainicial.Estaope-
raçãoretornadoisvalores:ovalorarmazenadosobaquelachaveeum bool
indicandoseachaveexisteounão no map. Atribuímosestesdoisvalores
àsvariáveiscontadore encontrado,respectivamente.Casojáexistaum
contadorparaa inicial( encontradopossuiovalor true),incrementa-
mosacontagem( contador + 1)eaatualizamosnomapa;casocontrário,
éaprimeiraocorrênciadeumapalavracomestainiciale,portanto,armaze-
namosacontageminicial 1.
A p ó siterarsobretodasaspalavras,nossomapa estatisticaspossuia
contagemcompleta,eentãoeleéusadocomovalorderetornoparaafunção
colherEstatisticas().
if encontrado {
estatisticas[inicial] = contador + 1
} else {
estatisticas[inicial] = 1
}
return estatisticas
Afunção imprimir()recebeomapacontendoasestatísticasesim-
plesmenteiterasobretodasasentradas,imprimindoasestatísticasparacada
inicial:
func imprimir(estatisticas map[string]int) {
fmt.Println("Contagem de palavras iniciadas em cada letra:")
for inicial, contador := range estatisticas {
fmt.Printf("%s = %d\n", inicial, contador)
29

## Página 44

3.1.Exemplo3:mapaseestatísticas CasadoCódigo
}
}
V e j acomoiterarsobretodasasentradasdeum mapéumatarefatrivial
quandoutilizamosooperador range:comocadaentradanomapaé,por
definição,umpar c h a v e ,valor,oretornode rangeseencaixaperfeitamente.
Éimportanteressaltarque,emGo,aordemdeiteraçãosobre mapséalea-
t ó r i ae,portanto,nãosedeveconfiarnela.Nocapítulo4estudaremos maps
maisafundoeveremoscomogarantiraordemdesejadanestescasos.
Aseguirvocêencontraalistagemcompletadoprograma.Crieoarquivo
cap3-maps/maps.gocomoseguinteconteúdo:
package main
import (
"fmt"
"os"
"strings"
)
func main() {
palavras := os.Args[1:]
estatisticas := colherEstatisticas(palavras)
imprimir(estatisticas)
}
func colherEstatisticas(palavras []string) map[string]int {
estatisticas := make(map[string]int)
for _, palavra := range palavras {
inicial := strings.ToUpper(string(palavra[0]))
contador, encontrado := estatisticas[inicial]
if encontrado {
estatisticas[inicial] = contador + 1
} else {
estatisticas[inicial] = 1
}
30

## Página 45

CasadoCódigo Capítulo3.Indoalém:maisexemplos
}
return estatisticas
}
func imprimir(estatisticas map[string]int) {
fmt.Println("Contagem de palavras iniciadas em cada letra:")
for inicial, contador := range estatisticas {
fmt.Printf("%s = %d\n", inicial, contador)
}
}
Eumexemplodaentradaesaída:
$ go run cap3-maps/maps.go \
Lorem ipsum dolor sit amet leo eu velit ante sagittis dolor \
turpis dis
Contagem de palavras iniciadas em cada letra:
L = 2
I = 1
D = 3
S = 2
A = 2
E = 1
V = 1
T = 1
3.2 Exemplo 4: pilhase tipos customizados
Definirtiposcustomizadostrazinúmerosbenefíciosàlegibilidadeerobus-
tezdeumprograma.Gopossuialgumasfuncionalidadesquefacilitamesta
tarefa,everemosmaissobreesteassuntonocapítulo5.
Oexemploaseguirapresentaumaimplementaçãosimplesdeumapilha
deobjetosatravésdeumtipocustomizado.
Destaveznãoreceberemosargumentosvialinhadecomando,simples-
menteempilhamosedesempilhamosalgunsvaloreseinteragimoscomapilha
chamandoalgunsoutrosmétodosutilitários.
31

## Página 46

3.2.Exemplo4:pilhasetiposcustomizados CasadoCódigo
Parafacilitaroentendimentodainterfacedapilha,veremoscadapasso
dafunção main()queinteragecomela,eposteriormente,veremosaimple-
mentaçãodecadamétodo.
Inicialmente,criamosumainstânciadapilhaeatribuímosoobjetoretor-
nadoàvariável pilha. Emseguida,imprimimosoresultadodachamada
demétodos: pilha.Tamanho()e pilha.Vazia(),queretornam 0e
true,respectivamente.
pilha := Pilha{}
fmt.Println("Pilha criada com tamanho ", pilha.Tamanho())
fmt.Println("Vazia? ", pilha.Vazia())
Sevocêjáprogramouemqualqueroutralinguagemcomsuporteaori-
entação aobjetos,não encontrounenhumagrandenovidadeatéaqui. En-
tretanto,reparequeosnomesdetodososmétodosquechamamosseini-
ciamcomumaletramaiúscula.Gopossuiumaformamuitosimplesdecon-
troledeacesso: todoidentificadoriniciadocomumaletramaiúsculaden-
trodeumpacoteéautomaticamenteexportadoevisívelforadopacote.Na
prática,jáutilizamosestafuncionalidadequandochamamosfunções como
fmt.Println(),porexemplo.
U m apilhavazianãoémuitoútil.V a m o sagoraempilharquatroobjetose
verificaro Tamanho()dapilhaeseelacontinua Vazia():
pilha.Empilhar("Go")
pilha.Empilhar(2009)
pilha.Empilhar(3.14)
pilha.Empilhar("Fim")
fmt.Println("Tamanho após empilhar 4 valores: ",
pilha.Tamanho())
fmt.Println("Vazia? ", pilha.Vazia())
V e j aquesomoscapazesdeempilharvaloresdetiposcompletamentedi-
ferentes:duas strings,um inteum float64.Semnenhumasurpresa,
asduasúltimaslinhasdotrechoanteriorimprimirão 4e false,respecti-
vamente.Eagoraquetemosumapilhacheia,quetaldesempilhartodosos
objetos?
32

## Página 47

CasadoCódigo Capítulo3.Indoalém:maisexemplos
Comovimosanteriormente, foréaúnicaestruturaderepetição dis-
ponívelemGo. Masistonão significaqueelasejalimitada. Aseguiruti-
lizamosumaformadiferentedaiteração com for,similaràconstrução
while emoutraslinguagens. Enquantoapilhanão estivervazia( for
!pilha.Vazia()),oblocoseráexecutado.Dentrodobloco,desempilha-
mosumvaloreoatribuímosàvariávelv,cujovalorémostradoaousuário,
juntocomosresultadosde pilha.Tamanho()e pilha.Vazia()após
cadaoperação deremoção. Notequeométodo pilha.Desempilhar()
retornadoisvalores.Osegundovalorindicaumerroque,nestemomento,
optamosporignorar,atribuindo-oaoidentificadorvazio _.
for !pilha.Vazia() {
v, _ := pilha.Desempilhar()
fmt.Println("Desempilhando ", v)
fmt.Println("Tamanho: ", pilha.Tamanho())
fmt.Println("Vazia? ", pilha.Vazia())
}
Aofinaldaiteração,apilhaestávazianovamente.Poderíamosnoscertifi-
cardestefatochamandoafunção pilha.Vazia().Porém,decidimoscha-
marométodo pilha.Desempilhar()maisumavez.Agora,noentanto,
ignoramosoprimeirovalorretornadoeatribuímososegundoàvariávelerr.
Porfim,seumerrofoiretornado,eleéapresentadoaousuário.
_, err := pilha.Desempilhar()
if err != nil {
fmt.Println(err)
}
Agoravamosàdefiniçãodotipo Pilhaeseusmétodos.
Diferentedeoutraslinguagenscomsuporteàprogramaçãoorientadaa
objetos,Gonãopossuioconceitodeclasses.Emvezdisso,definimosestru-
turasdedadosemformade structs,construções semelhantesàs structs
dalinguagemC,eumconjuntodefunções –métodos,nestecaso–quema-
nipulamestesdados.Aseguirtemosadefiniçãodonovotipo Pilha:
type Pilha struct {
valores []interface{}
}
33

## Página 48

3.2.Exemplo4:pilhasetiposcustomizados CasadoCódigo
Onovotipopossuiapenasummembro:umslicedenominado valores,
quearmazenaobjetosdotipo interface{}.Estetipoéconhecidocomo
interface vaziaedescreveumainterfacesemnenhummétodo.Qualquertipo
emGoimplementapelomenoszerométodos,portantosatisfazainterface
vazia.Naprática,istofazcomqueanossaimplementaçãodepilhasejacapaz
dearmazenarobjetosde qualquertipoGoválido,conformepudemosverna
implementaçãodafunção main().
Oslice valoresfoiintencionalmentedeclaradocomainicialminúscula,
garantindoqueelenãosejaacessívelemoutropacote.
Tendodefinidootipo Pilha,podemoscomeçaradefinirseusmétodos.
Começaremoscomosimplesmétodo Tamanho():
func (pilha Pilha) Tamanho() int {
return len(pilha.valores)
}
Adefiniçãodeummétodoémuitosemelhanteàdefiniçãodeumafunção,
comojávimosanteriormente.Adiferençamarcanteéquemétodosdefinem
umobjeto receptor,quenestecasofoichamadode pilhaeédotipo Pilha,
quedeveserespecificadoentreparêntesesantesdonomedométodo.Assim,
ométodo Tamanho()acessaoslice pilha.valoreseretornaseutama-
nhoutilizandoafunção len().
Éimportanteobservarque,comoGonão possuioconceitodeclasses,
seusmétodostambémnãopossuemumreceptorimplícito–conhecidocomo
selfou thisemoutraslinguagens. Istofacilitamuitoaimplementação
do runtimedalinguagemeaumentaaclarezadocódigo,jáquedentroda
definiçãodométodosóexisteumaformadeacessarseureceptor.
Ométodo pilha.Vazia()étrivialesimplesmenteverificaseotama-
nhoatualdapilhaéigualazero:
func (pilha Pilha) Vazia() bool {
return pilha.Tamanho() == 0
}
Osdoismétodosapresentadosatéaquisãoimutáveis–nãopossuemne-
nhumefeitocolateral–e,portanto,bastantesimples.
34

## Página 49

CasadoCódigo Capítulo3.Indoalém:maisexemplos
Nocasodosmétodos Empilhar()e Desempilhar(),desejamosal-
terarapilhanaqualtaismétodosforamchamados.EmGo,argumentosde
funções emétodossão semprepassadosporcópia(comaexceçãodeslices,
mapsechannels,quesão conhecidoscomo reference types,comoveremos
nospróximoscapítulos).Porisso,quandoprecisamosalterarqualquerargu-
mento–incluindoreceptoresdemétodos–devemosdeclará-loscomo pon-
t e i ro s.Vejamosadefiniçãodométodo Empilhar():
func (pilha *Pilha) Empilhar(valor interface{}) {
pilha.valores = append(pilha.valores, valor)
}
Reparequeotipodoreceptorfoidefinidocomo *Pilha,eindicaque
avariável pilhaéum ponteiroparaumobjetodotipo Pilha. Paraem-
pilharumnovoobjeto,adicionamo-loaoslice pilha.valoresatravésdo
usodafunção append()ealteramosovaloratualde pilha.valorespara
guardaronovoslicequecontémoobjetoadicionado.
Deformasimilar,ométodoDesempilhar()tambémdefineoreceptor
comosendoumponteiro.Comovimosnadefiniçãodafunção main(),este
métodopossuidoisvaloresderetorno:oobjetodesempilhadoeumvalordo
tipo errorqueéretornadoquandoapilhaestávazia.Paraisso,utilizamoso
método pilha.Vazia()e,emcasoderetornopositivo,criamosumnovo
erroatravésdafunção errors.New()eretornamos nilnolugardoobjeto
desempilhado,juntocomoerrorecém-criado.
Casoapilhanão estejavazia,atribuímosoúltimoobjetoempilhadoà
variávelvalor.Emseguida,atualizamososlice pilha.valorescomuma
fatiadosliceatual,incluindotodososobjetosempilhadoscomaexceçãodo
último–queacaboudeserdesempilhado.Finalmente,retornamosoobjeto
removidoe nilnolugardoerro,indicandoqueoobjetofoidesempilhado
comsucesso.
func (pilha *Pilha) Desempilhar() (interface{}, error) {
if pilha.Vazia() {
return nil, errors.New("Pilha vazia!")
}
valor := pilha.valores[pilha.Tamanho()-1]
35

## Página 50

3.2.Exemplo4:pilhasetiposcustomizados CasadoCódigo
pilha.valores = pilha.valores[:pilha.Tamanho()-1]
return valor, nil
}
Confiraalistagemcompletadaimplementaçãodapilha. Utilizeocon-
teúdoaseguirparacriaroarquivo cap3-pilha/pilha.go:
package main
import (
"errors"
"fmt"
)
func main() {
pilha := Pilha{}
fmt.Println("Pilha criada com tamanho ", pilha.Tamanho())
fmt.Println("Vazia? ", pilha.Vazia())
pilha.Empilhar("Go")
pilha.Empilhar(2009)
pilha.Empilhar(3.14)
pilha.Empilhar("Fim")
fmt.Println("Tamanho após empilhar 4 valores: ",
pilha.Tamanho())
fmt.Println("Vazia? ", pilha.Vazia())
for !pilha.Vazia() {
v, _ := pilha.Desempilhar()
fmt.Println("Desempilhando ", v)
fmt.Println("Tamanho: ", pilha.Tamanho())
fmt.Println("Vazia? ", pilha.Vazia())
}
_, err := pilha.Desempilhar()
if err != nil {
fmt.Println("Erro: ", err)
}
}
36

## Página 51

CasadoCódigo Capítulo3.Indoalém:maisexemplos
type Pilha struct {
valores []interface{}
}
func (pilha Pilha) Tamanho() int {
return len(pilha.valores)
}
func (pilha Pilha) Vazia() bool {
return pilha.Tamanho() == 0
}
func (pilha *Pilha) Empilhar(valor interface{}) {
pilha.valores = append(pilha.valores, valor)
}
func (pilha *Pilha) Desempilhar() (interface{}, error) {
if pilha.Vazia() {
return nil, errors.New("Pilha vazia!")
}
valor := pilha.valores[pilha.Tamanho()-1]
pilha.valores = pilha.valores[:pilha.Tamanho()-1]
return valor, nil
}
U mexemplodesteprogramaemexecução:
$ go run cap3-pilha/pilha.go
Pilha criada com tamanho 0
Vazia? true
Tamanho após empilhar 4 valores: 4
Vazia? false
Desempilhando Fim
Tamanho: 3
Vazia? false
Desempilhando 3.14
Tamanho: 2
Vazia? false
Desempilhando 2009
37

## Página 52

3.2.Exemplo4:pilhasetiposcustomizados CasadoCódigo
Tamanho: 1
Vazia? false
Desempilhando Go
Tamanho: 0
Vazia? true
Erro: Pilha vazia!
Nestecapítulo,melhoramosnossoconhecimentoarespeitodosrecursos
básicosdalinguagemGo.Vimosautilizaçãobásicademapasparaclassifi-
carvaloressobchaves,eaprendemosadefinirtiposcustomizadosparacriar
abstrações maiscomplexas.
Mapasserãodiscutidosemdetalhesnocapítulo4.3,eaprenderemosainda
maissobreoutrasformasdecriartiposcustomizadosnocapítulo5.
38

## Página 53

Capítulo4
Coleções: arrays,slicesemaps
Noscapítulosanteriores,vimoscomocoleções sãoessenciaisparaasolução
deváriosproblemas.Agoraveremosascoleções disponíveisemGoemmai-
oresdetalhes.
4.1 Ar r a y s
ArraysemGosãocoleções indexadasdevaloresdomesmotipoedetamanho
fixoeinvariável.Oprimeiroelementodoarraypossuiíndice 0,eoúltimo
elementoésempre len(array) - 1.
Paradeclararumarray,podemosutilizarumadasseguintesformas:
var a [3]int
numeros := [5]int{1, 2, 3, 4, 5}
primos := [...]int{2, 3, 5, 7, 11, 13}

## Página 54

4.1.Arrays CasadoCódigo
nomes := [2]string{}
fmt.Println(a, numeros, primos, nomes)
Oresultadodaúltimalinhaseriaoseguinte:
[0 0 0] [1 2 3 4 5] [2 3 5 7 11 13] [ ]
Oarray afoideclaradocomo [3]int,ouumalistade3númerosintei-
ros.Otamanhodeumarraydeve sempreserespecificadonadeclaraçãoefaz
partedotipodoarray–[3]inte [5]intsãoconsideradostiposdiferentes,
aindaqueamboscarreguemvaloresdomesmotipo.
A p e s a rdenão termosinseridonenhumvalorem a,obtivemos [0 0
0]quandoimprimimosseuconteúdo.Quandoumarrayédeclarado,seus
elementosganhamautomaticamenteumvalorinicialconhecidocomo zero
valueemGo.Estevalorinicialvariadeacordocomotipodedadosdefinido
paraoarray,daseguinteforma:
•falseparavaloresdotipo bool;
•0para ints;
•0.0para floats;
•""(ou stringvazia)para strings;
•nilparaponteiros,funções, interfaces,slices,mapsechannels.
Algumasvezessabemosdeantemãoquaisserãoosvalorescontidosnum
array,epodemosdeclará-losutilizandoaformaliteral,comoem numeros
:= [5]int{1, 2, 3, 4, 5}.Nestescasos,parafacilitaravidadopro-
gramador,pode-sesubstituirotamanhodoarraynadeclaraçãopelooperador
ellipsis(reticências),instruindoocompiladoracalcularotamanhodoarray
combasenaquantidadedeelementosdeclarados,comofizemosem primos
:= [...]int{2, 3, 5, 7, 11, 13}.
Porfim,declaramos nomes := [2]string{} –umarraydeduas
strings–utilizandoaformaliteral,porémsemnenhumvalordeclarado
entreaschaves,fazendocomqueoselementossejaminicializadoscom "".
40

## Página 55

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
Estadeclaraçãoéidênticaàprimeiraformautilizada(paradeclararoarray
a)epoderiaserescritatambémdaseguinteforma:
var nomes [2]string
Otamanhodeumarraypodeserobtidoatravésdousodafunção len().
Porexemplo,aexecuçãodocódigoaseguirnosdaria 3 5 6 2comoresul-
tado:
fmt.Println(len(a), len(numeros), len(primos), len(nomes))
Podemostambémcriararrayscujosvaloressãotambémarrays,ouarrays
multidimensionais,deformasimilaraarrayssimples:
var multiA [2][2]int
multiA[0][0], multiA[0][1] = 3, 5
multiA[1][0], multiA[1][1] = 7, -2
multiB := [2][2]int{{2, 13}, {-1, 6}}
fmt.Println("Multi A:", multiA)
fmt.Println("Multi B:", multiB)
Repareque,nadeclaraçãoliteraldoarray multiB,nãoprecisamosespe-
cificarotipodosarraysinternos.
Imprimindoosvaloresde multiAe multiBteríamososeguinteresul-
tado:
Multi A: [[3 5] [7 -2]]
Multi B: [[2 13] [-1 6]]
Osarraystêmsuaimportânciaeseupapel,masnãosãomuitoflexíveis,
especialmentenoscasosemqueprecisamosaumentarseutamanhodinami-
camente.Épossívelfazerissocomarrays,masexigeumgrandetrabalhoma-
nualdeverificaçãodelimites,alocaçãodenovosarraysecópiadeconteúdo.
Emquasetodososcasos,emGoémaiscomumutilizarslices.Aprópria
bibliotecapadrãodalinguagemutilizaslicesemvezdearrayscomoparâme-
trosetiposderetornoemsuaAPIpública.Aseguirveremososbenefíciose
facilidadesdesetrabalharcomeles.
41

## Página 56

4.2. Slices CasadoCódigo
4.2 Slices
U msliceéumapoderosaabstração criadaemcimadearraysqueintroduz
umasériedefacilidades.Diferentedeumarray,noentanto,umslicepossui
tamanhovariávelepodecrescerindefinidamente.
Naprática,autilização deslicesémuitosimilaraoqueacabamosde
aprendersobrearrays. Paradeclararumslice, podemosutilizarquasea
mesmasintaxedadeclaraçãodearrays,incluindoaformaliteral,comadife-
rençadequenãoespecificamosotamanhodoslice:
var a []int
primos := []int{2, 3, 5, 7, 11, 13}
nomes := []string{}
fmt.Println(a, primos, nomes)
Teríamosaseguintesaídaimpressa:
[] [2 3 5 7 11 13] []
Comonãoespecificamosotamanhodosslices ae nomesnemadicio-
namosnenhumvaloraelesduranteadeclaração,ambosestãovaziosapósa
inicialização.
ArrayseslicesemGopossuemduaspropriedadesimportantes:tamanho
ecapacidade–len()e cap(),respectivamente,sãoasfunções utilizadas
parainspecionarestaspropriedades.
U mslicepodesercriadotambématravésdafunção make(),quein-
ternamentealocaumarrayeretornaumareferênciaparaoslicecriado.Ela
possuiaseguinteassinatura:
func make([]T, len, cap) []T
Trepresentaotipodoselementosdoslice, lenotamanhoinicialdo
arrayalocadoe capotamanhototaldaáreadememóriareservadaparao
crescimentodoslice.Porconveniência,pode-seomitiroúltimoargumento,
enestecasoGoassumeporpadrão omesmovalordotamanho. Vejamos
algunsexemplos:
42

## Página 57

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
b := make([]int, 10)
fmt.Println(b, len(b), cap(b))
c := make([]int, 10, 20)
fmt.Println(c, len(c), cap(c))
Essecódigoimprimiria:
[0 0 0 0 0 0 0 0 0 0] 10 10
[0 0 0 0 0 0 0 0 0 0] 10 20
Notequeos10primeiroselementos–10foiotamanhoespecificado–
dosdoisslicesforaminicializadoscom 0,o zero valuepara ints,conforme
vimosanteriormente.
U m agrandevantagemdeutilizarslices–defato,qualquertipocriado
atravésdafunção make()–emvezdearrayséque,quandousadoscomo
argumentosounoretornodefunções, sãopassadosporreferênciaenãopor
cópia. Istotornaestaschamadasmuitomaiseficientes,poisotamanhoda
referênciaserásempreomesmo,independentedotamanhodoslice.
Iteradores
Jáiteramossobreslicesnosexemplosanteriores,eagoraveremostodas
asdiferentesformasdeiteraçãodisponíveisemGo.
Sabemosqueaúnicaestruturaderepetição emGoéo for. Emsua
formamaisbásica,podemosespecificarumacondiçãológicaeoblocoserá
executadoenquantoacondiçãoforverdadeira–similaràconstrução while
emoutraslinguagens.Porexemplo:
a, b := 0, 10
for a < b {
a += 1
}
fmt.Println(a)
Podemosleressecódigocomo enquanto a for menor q u eb, incremente
43

## Página 58

4.2. Slices CasadoCódigo
o valor de a.Seuresultadoseriaaimpressãodovalor 10,ovalorde aapós
aexecuçãodobloco for.
T a m b é mpodemosutilizaro forcomumacláusuladeinicialização,uma
condiçãológicaeumacláusuladeincremento–aconstruçãotradicionalda
linguagemC:
for i := 0; i < 10; i++ {
// ...
}
Éimportantenotarque,comoavariávelinãoexistiaantesdo for,seu
escopoélimitadoaobloco;setentarmosacessarseuvalorapósaexecuçãodo
bloco,teremosumerrodecompilaçãoinformandoque inãofoidefinida.
Pararesolveressescasos,precisamosdeclararavariávelantesdo for:
var i int
for i = 0; i < 10; i++ {
// ...
}
fmt.Println(i)
Destaforma, icontinuaexistindoapósaexecução dobloco for,eo
programaimprimiriaovalor 10.
Qualquerelementodacláusula forpodeseromitido,masopontoe
vírgulaéobrigatório–anãoserqueoúnicoelementopresentesejaacondição
lógica,comojávimosnoprimeiroexemplodeusodo for.Desconsiderando
oescopodavariáveldecontrole,todasasformasaseguirsãoequivalentes:
i := 0
for i < 10 {
i += 1
}
for j := 0; j < 10; j++ {
// ...
}
44

## Página 59

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
var k int
for k = 0; k < 10; {
k += 1
}
l := 0
for ; l < 10; l++ {
// ...
}
Aformamaiscomumdeiterarsobreslices,porém,éutilizandooopera-
dor range,comojávimosnoscapítulosanteriores.Asintaxegeralé:
for indice, valor := range slice {
// ...
}
Ooperador rangeretornaoíndicedecadaelemento,começandoem 0,
euma cópiadecadavalorpresentenoslice.Quandoprecisamosmodificaros
valoresemumslice,ouestamosinteressadossomentenosíndices,podemos
simplesmenteomitirosegundovalornaatribuiçãoeacessarcadaelemento
atravésdeseuíndice:
numeros := []int{1, 2, 3, 4, 5}
for i := range numeros {
numeros[i] *= 2
}
fmt.Println(numeros)
Ocódigoanterioriterasobreumslicechamado numeros,multiplicando
cadavalorpor2. A p ó saiteração, imprimimosoconteúdode numerose
obtemos [2 4 6 8 10]comoresultado.
Aocontrário,quandonãoprecisamosdosíndicesdosvalores,podemos
ignorá-losatribuindo-osaoidentificadorvazio:
45

## Página 60

4.2. Slices CasadoCódigo
for _, elemento := range slice {
// ...
}
Aúltimaformadeutilizaçãodo foréaformaconhecidacomo loop i n -
fi n i t o,queemGoésimplesmenteumacláusulaforsemnenhumacondição
–Goassume truecomovalorpadrãoparaacondição:
for {
// loop infinito
}
Parasairdaexecuçãodeumloopinfinito,podemosutilizarocomando
break.
Aseguir,temosumexemploqueiniciaumloopinfinito,geranúmeros
aleatóriosesaidoloopsomentequandoonúmerogeradofordivisívelpor
42,ouseja,orestodadivisãodovalorpor42é0–i%42 == 0. Crieum
novoarquivochamado cap4-loop-infinito/loop_infinito.gocom
oseguinteconteúdo:
package main
import (
"fmt"
"math/rand"
"time"
)
func main() {
rand.Seed(time.Now().UnixNano())
n := 0
for {
n++
i := rand.Intn(4200)
fmt.Println(i)
if i%42 == 0 {
46

## Página 61

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
break
}
}
fmt.Printf("Saída após %d iterações.\n", n)
}
Quandogeramosnúmerosaleatórios,ésempreimportanteconfiguraro
valorconhecidocomo seed(semente)dogerador.Noexemploanterior,uti-
lizamoso timestampatualnoformatopadrãodoUnix–onúmerodenano
segundosdesde1ºdejaneirode1970–paragarantirque,acadaexecuçãodo
programa,ogeradordenúmerosaleatóriosproduzanúmerosdiferentesda
vezanterior.
U mexemplodasaídadoprograma:
$ go run cap4-loop-infinito/loop_infinito.go
1458
3816
2413
1179
594
1562
93
2911
1131
3008
2235
3910
2928
1470
Saída após 14 iterações.
Porpadrão, breaksaidoloopmaispróximoaopontoemqueocomando
foiexecutado.Hácasosnosquaistemosloops foraninhadosedesejamos
quebraroloopexternoemvezdointerno.Pararesolveresteproblema,Go
tambémdásuporteablocos fornomeados.Vejamosumexemplo:
var i int
47

## Página 62

4.2. Slices CasadoCódigo
externo:
for {
for i = 0; i < 10; i++ {
if i == 5 {
break externo
}
}
}
fmt.Println(i)
Esterecurso tambéméimportantequandotemos, porexemplo,um
bloco switch dentrode um bloco for. Como o comando break
tambéméusado para sair do switch, precisamosespecificar o nome
dadoaobloco forsequisermossairdoloop. V a m o scriarumprograma
para demonstraro uso de laços nomeados. Crie um arquivochamado
cap4-loop-nomeado/loop_nomeado.go definindoumpacote main,
importandoopacote fmt,eadicioneoseguinteconteúdoàfunção main():
var i int
loop:
for i = 0; i < 10; i++ {
fmt.Printf("for i = %d\n", i)
switch i {
case 2, 3:
fmt.Printf("Quebrando switch, i == %d.\n", i)
break
case 5:
fmt.Println("Quebrando loop, i == 5.")
break loop
}
}
fmt.Println("Fim.")
Asaídadoprogramaseriaaseguinte:
48

## Página 63

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
$ go run cap4-loop-nomeado/loop_nomeado.go
for i = 0
for i = 1
for i = 2
Quebrando switch, i == 2.
for i = 3
Quebrando switch, i == 3.
for i = 4
for i = 5
Quebrando loop, i == 5.
Fim.
Fatiando slices
F a t i a r(doinglêst oslice)éonomedadoaoperações queextraempartes
deumsliceoudeumarray.
Parafatiarumsliceouarray,utilizamosaseguinteforma:
novoSlice := slice[inicio : fim]
Sendoque 0 <= inicio <= fim <= len(slice).Qualquercom-
binaçãodeíndicesinicialefinalquenãoatendaaestaregraresultaemum
errodecompilacão(slice bounds o u to fr a n g e,ou limites do slice fora de a l -
cance).
Porquestões práticas,podemosomitiroíndiceiniciale/oufinal. Seo
índiceinicialforomitido, 0éassumidocomopadrão; demaneirasimilar,
len(slice)-1éassumidocomovalorpadrãoparaoíndicefinal:
fib := []int{1, 1, 2, 3, 5, 8, 13}
fmt.Println(fib)
fmt.Println(fib[:3])
fmt.Println(fib[2:])
fmt.Println(fib[:])
Essecódigoimprimiria:
[1 1 2 3 5 8 13]
[1 1 2]
[2 3 5 8 13]
[1 1 2 3 5 8 13]
49

## Página 64

4.2. Slices CasadoCódigo
Comocitadoanteriormentenestecapítulo,umsliceéumaabstraçãocri-
adacombasenosarrays.Entenderarelaçãoentreeleséessencialparatraba-
lharefetivamentecomslices.
Sabemosque,quandoumsliceécriado,umarrayéalocadointernamente.
Quandofatiamosestesliceeoatribuímosaumanovavariável,temosum
novoslicequecompartilhao mesmo array internodooriginal. Istoquer
dizerque,quandoumelementocomumaosdoisslicesémodificado,esta
modificaçãoérefletidanooutro.Vejamosumexemplo:
original := []int{1, 2, 3, 4, 5}
fmt.Println("Original:", original)
novo := original[1:3]
fmt.Println("Novo:", novo)
original[2] = 13
fmt.Println("Original pós modificação:", original)
fmt.Println("Novo pós modificação:", novo)
Asaídadesteprogramaseriaaseguinte:
Original: [1 2 3 4 5]
Novo: [2 3]
Original pós modificação: [1 2 13 4 5]
Novo pós modificação: [2 13]
V e j aque,aoalterarmosovalorde original[2]para13,oconteúdodos
doisslicesfoimodificado.Istoéverdadepara qualquerslicecriadofatiando
umoutroslice,independentedaquantidadedeindireções criadas.V e j amais
umexemplo:
a := []string{"Paulo", "almoça", "em", "casa", "diariamente."}
b := a[:len(a)-1]
c := b[:len(b)-1]
d := c[:len(c)-1]
e := d[:len(d)-1]
e[0] = "Tiago"
fmt.Printf("%v\n%v\n%v\n%v\n%v\n", a, b, c, d, e)
50

## Página 65

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
Eoresultadoimpressoseria:
[Tiago almoça em casa diariamente.]
[Tiago almoça em casa]
[Tiago almoça em]
[Tiago almoça]
[Tiago]
T o d a sasoperações apresentadasanteriormentetambémsãoválidasem
umarray,eéimportantemencionarquefatiarumarray sempreresultaem
umslice,nuncaemoutroarray.
Inserindo valores
T o d a sas operações realizadas sobre slices são baseadas na função
append().Jávimosalgunsexemplosdecomousá-la.Suaassinaturaé:
func append(slice []Tipo, elementos ...Tipo) []Tipo
Parainserirumnovovalor ao fi n a ldeumslice,utilizamos append()
emsuaformamaisbásica:
s := make([]int, 0)
s = append(s, 23)
fmt.Println(s)
Executandoestecódigo,veríamosovalor [23]impresso.
Parainserirumnovovalor no começodeumslice,precisamosinicial-
mentecriarumnovoslicecontendoovalorquedesejamosinserir,edepois
adicionartodososelementosdosliceinicialaorecém-criado.Parececompli-
cado,masnapráticaébastantesimples:
s := []int{23, 24, 25}
n := []int{22}
s = append(n, s...)
fmt.Println(s)
51

## Página 66

4.2. Slices CasadoCódigo
U m aoutraopçãomaissucintaécriaronovosliceutilizandoaformali-
teralnaprópriachamadaàfunção append():
s := []int{23, 24, 25}
s = append([]int{22}, s...)
fmt.Println(s)
Asduasformassãosemanticamenteequivalenteseimprimiriam [22 23
24 25].Reparequeutilizamosnovamenteooperador ellipsis(reticências)
paraexpandiroconteúdodoslice,garantindoquetodososvaloressejam
passadosdeformaindividualàfunção append().
T a m b é mépossívelinserirumoumaisvaloresemqualquerposição no
meiodeumslice.Paraisso,precisamosfatiarosliceatéaposiçãoondedese-
jamosinserirosnovosvalores–s[:3]–eutilizarestafatiadosliceoriginal
comoprimeiroargumentonachamadaà append().Osegundoargumento
deveser,porsuavez,oresultadodeumasegundaoperaçãode append(),
ondeinserimososvaloresrestantesdosliceoriginal–s[3:]...–aoslice
quecontémosnovosvalores–append(v, s[3:]...)....Reparenova-
menteousodooperador ellipsis,aparecendoduasvezesnesteexemplo:
s := []int{11, 12, 13, 16, 17, 18}
v := []int{14, 15}
s = append(s[:3], append(v, s[3:]...)...)
fmt.Println(s)
Essecódigoimprimiria [11 12 13 14 15 16 17 18].
Removendo valores
Pararemovervaloresdocomeçodeumslicenãoprecisamosdafunção
append().Bastafatiarosliceignorandoosíndicesdoselementosquedese-
jamosremover,eatribuironovosliceàmesmavariável.Porexemplo,pode-
mosremoveroprimeirovalordeumslicedaseguinteforma:
s := []int{20, 30, 40, 50, 60}
s = s[1:]
52

## Página 67

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
fmt.Println(s)
Assim,essecódigoimprimiriaoslice [30 40 50 60].
Demaneiraanáloga,pararemovervaloresdofinaldeumslice,fatiamos
estesliceignorandoosíndicesdoselementosfinais:
s := []int{20, 30, 40, 50, 60}
s = s[:3]
fmt.Println(s)
Eagoraoslice steriaoconteúdo [20 30 40].
Porfim,pararemovervaloresdomeiodeumslice,precisamosrecorrer
novamenteàfunção append(),utilizandoduasfatiasdosliceoriginalcomo
argumentos–aprimeiraincluindoelementosdoinícioatéoíndicedesejado,
easegundacomeçandodopróximoelementoquenosinteressa.Porexem-
plo,dadoumslice s := []int{10, 20, 30, 40, 50, 60},podemos
removerosvalores30e40daformaaseguir:
s := []int{10, 20, 30, 40, 50, 60}
s = append(s[:2], s[4:]...)
fmt.Println(s)
Aoexecutaressecódigo, teríamososlice [10 20 50 60]impresso
conformeoesperado.
C o p i a n d oslices
A t éagora,todasasvezesemquemanipulamosslices,utilizamosafunção
append()para modificarosliceoriginal.Noentanto,muitasvezespreci-
samosmanteroestadodosliceoriginalintactoemanipularuma cópiadele.
Paraisso,Gotambémpossuiumafunçãoembutidachamada copy(),com
aseguinteassinatura:
func copy(destino, origem []Tipo) int
53

## Página 68

4.3.Maps CasadoCódigo
Paracriarumacópiadeumslice,chamamosafunção copy()dase-
guinteforma:
numeros := []int{1, 2, 3, 4, 5}
dobros := make([]int, len(numeros))
copy(dobros, numeros)
for i := range dobros {
dobros[i] *= 2
}
fmt.Println(numeros)
fmt.Println(dobros)
Imprimindooconteúdodosdoisslices,teríamos [1 2 3 4 5]e [2 4
6 8 10]comoresultado,provandoqueosliceoriginalnãosofreunenhuma
alteração.
4.3 Maps
U mmap,oumapa,éumacoleção depares chave-valorsemnenhumaor-
demdefinida.ÉaimplementaçãoemGodeumaestruturadedadostambém
conhecidacomo hashtable,dicionáriodedadosouarrayassociativo,entre
outrosnomes.
Qualquertipoquesuporteosoperadoresdeigualdade(i.e. ==e !=)pode
serusadocomochaveemummapa. Noentanto,aschavesemummesmo
mapadevemnecessariamenteserdomesmotipo.Éimportantemencionar
tambémqueaschavessão únicas–searmazenarmosdoisvaloresdistintos
sobumamesmachave,oprimeirovalorserásobrescritopelosegundo.
Osvaloresemummapatambémdevemsempreserdomesmotipo,em-
boraainterfacevazia interface{}sejaumtipoválidonestecaso.Istopos-
sibilitaarmazenarvirtualmente qualquervalorsobumachave,porémrequer
uma asserção de tipo(type assertion)quandoosvaloressãorecuperados.
Podemosdeclararmapasutilizandoaformaliteralouafunção make(),
demaneiramuitosemelhanteàdeclaraçãodeslices.Porexemplo,parade-
54

## Página 69

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
clararummapavaziocomchavesdotipo intevaloresdotipo string,as
duasopções aseguirsãoequivalentes:
vazio1 := map[int]string{}
vazio2 := make(map[int]string)
Aquantidadedevaloresarmazenadosemummapaéflexívelepodecres-
cerindefinidamenteduranteaexecuçãodeumprograma,sendoquepode-
mosespecificarsuacapacidadeinicialquandosabemosdeantemãoquantos
valoresprecisaremosarmazenar.Issopodeserimportantequandosabemos
queomapairáarmazenarmuitosvalores,tornandoousodememóriamais
eficienteeevitandoproblemasdeperformance.Érecomendávelespecificá-la
semprequepossível,epodemosfazê-losimplesmentepassandoumsegundo
argumentoàfunção make():
mapaGrande := make(map[int]string, 4096)
Aqualquermomentopodemosinspecionaraquantidadedeelementos
queummapapossuiatravésdafunção len().Porexemplo:
capitais := map[string]string{
"GO": "Goiânia",
"PB": "João Pessoa",
"PR": "Curitiba"}
fmt.Println(len(capitais))
Ocódigoimprimiriaovalor3.
Populando mapas
Podemospopularummapautilizandoliteraisnomomentodadeclaração
e/ouatribuindovaloresindividualmenteapósadeclaração:
capitais := map[string]string{
"GO": "Goiânia",
"PB": "João Pessoa",
"PR": "Curitiba"}
55

## Página 70

4.3.Maps CasadoCódigo
capitais["RN"] = "Natal"
capitais["AM"] = "Manaus"
capitais["SE"] = "Aracaju"
fmt.Println(capitais)
populacao := make(map[string]int, 6)
populacao["GO"] = 6434052
populacao["PB"] = 3914418
populacao["PR"] = 10997462
populacao["RN"] = 3373960
populacao["AM"] = 3807923
populacao["SE"] = 2228489
fmt.Println(populacao)
Oresultadodaexecuçãodessecódigoseriaoseguinte:
map[GO:Goiânia PB:João Pessoa PR:Curitiba RN:Natal
AM:Manaus SE:Aracaju]
map[GO:6434052 PB:3914418 PR:10997462 RN:3373960
AM:3807923 SE:2228489]
Paratornaroexemploanteriorumpoucomaisreal,vamosimplementá-
loutilizandoumnovotipo,chamado Estado. Crieumarquivochamado
cap4-estados/estados.goeadicioneadefiniçãodotipo Estadocom
aseguinteestrutura:
type Estado struct {
nome string
populacao int
capital string
}
Agora,nafunção main(),podemospopularummapadeestadosdesta
forma:
estados := make(map[string]Estado, 6)
estados["GO"] = Estado{"Goiás", 6434052, "Goiânia"}
56

## Página 71

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
estados["PB"] = Estado{"Paraíba", 3914418, "João Pessoa"}
estados["PR"] = Estado{"Paraná", 10997462, "Curitiba"}
estados["RN"] = Estado{"Rio Grande do Norte", 3373960, "Natal"}
estados["AM"] = Estado{"Amazonas", 3807923, "Manaus"}
estados["SE"] = Estado{"Sergipe", 2228489, "Aracaju"}
fmt.Println(estados)
Essecódigoimprimiriaoseguinteconteúdo(asquebrasdelinhaealguns
espaçosembrancoforamdeliberadamenteadicionadosparafacilitaravisu-
alização):
$ go run cap4-estados/estados.go
map[GO:{Goiás 6434052 Goiânia}
PB:{Paraíba 3914418 João Pessoa}
PR:{Paraná 10997462 Curitiba}
RN:{Rio Grande do Norte 3373960 Natal}
AM:{Amazonas 3807923 Manaus}
SE:{Sergipe 2228489 Aracaju}]
L o o k u p :recuperando valores
Aoperaçãoderecuperaçãodeumvaloremummapaéconhecidacomo
lookupeémuitosimilaràrecuperaçãodevaloresdeumíndiceespecíficoem
umslice–bastaespecificarachavedesejadaentrecolchetes:
sergipe := estados["SE"]
fmt.Println(sergipe)
Destaforma,avariávelsergipereceberiao Estadopresentenomapa
eovalor {Sergipe 2228489 Aracaju}seriaimpresso.
Eoqueaconteceriasetentássemosacessarovalordeumestadoquenão
estápresentenomapa?
fmt.Println(estados["SP"])
Ovalor { 0 }seriaimpresso. Notequeexisteumespaçoembranco
anteseoutrodepoisdovalor0.Quandotentamosrecuperarovalordeuma
57

## Página 72

4.3.Maps CasadoCódigo
chavequenãoestápresentenomapa,o zero valuedotipoarmazenadoére-
tornado.Muitasvezesissopodecausarcomportamentosinesperadosemum
programa.Paraevitartaisproblemas,podemostestarseumachaveexisteou
não:
saoPaulo, encontrado := estados["SP"]
if encontrado {
fmt.Println(saoPaulo)
}
Osegundovalorretornadopelaoperaçãodelookupéum boolquere-
ceberáovalor truecasoachaveestejapresentenomapa,ou falsecaso
contrário.Algumasvezesprecisamostestarseumadadachaveexiste,mas
nãonecessariamenteprecisamosdovalorcorrespondente.Nestecaso,pode-
mosignorarovaloratribuindo-oaoidentificadorvazio:
_, encontrado := estados["RJ"]
if encontrado {
// ...
}
Atualizando valores
Paraatualizarvaloresexistentesemummapa,utilizamosamesmasintaxe
dainserção deumnovovalor. Porém,comoaschavessão únicas,ovalor
armazenadoseráatualizado.Porexemplo:
idades := map[string]int{
"João": 37,
"Ricardo": 26,
"Joaquim": 41,
}
idades["Joaquim"] = 42
fmt.Println(idades["Joaquim"])
Ovalor42seriaimpresso.
58

## Página 73

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
Removendo valores
Podemosremovervalorespresentesemummapautilizandoafunçãoem-
butida delete(),quepossuiaseguinteassinatura:
func delete(m map[TipoChave]TipoValor, chave TipoChave)
Porexemplo,casodesejássemosremoverosdadosdoEstadodoAma-
zonasnomapadeestadosutilizadoanteriormente,poderíamosfazê-lodesta
forma:
delete(estados, "AM")
Iterando s o b r emapas
Podemosutilizarooperador rangeparaiterarsobretodasasentradas
deummapa:
for sigla, estado := range estados {
fmt.Printf("%s (%s) possui %d habitantes.\n",
estado.nome, sigla, estado.populacao)
}
Teríamosasaída:
Goiás (GO) possui 6434052 habitantes.
Paraíba (PB) possui 3914418 habitantes.
Paraná (PR) possui 10997462 habitantes.
Rio Grande do Norte (RN) possui 3373960 habitantes.
Amazonas (AM) possui 3807923 habitantes.
Sergipe (SE) possui 2228489 habitantes.
U mdetalheimportantequejáfoimencionadoéqueaordemdoselemen-
tosemummapanãoégarantida.Emmapaspequenoscomoosqueapresen-
tamosatéaqui,aordemdeinserçãoparecetersidomantida,massetivermos
ummapacomumaquantidademaiordeelementos,veremosqueistonãoé
sempreverdade.Porexemplo:
quadrados := make(map[int]int, 15)
59

## Página 74

4.3.Maps CasadoCódigo
for i := 1; i <= 15; i++ {
quadrados[i] = i * i
}
for n, quadrado := range quadrados {
fmt.Printf("%d^2 = %d\n", n, quadrado)
}
U mexemplodaexecuçãodessecódigoseria:
2^2 = 4
6^2 = 36
10^2 = 100
14^2 = 196
1^2 = 1
5^2 = 25
9^2 = 81
13^2 = 169
4^2 = 16
8^2 = 64
12^2 = 144
3^2 = 9
7^2 = 49
11^2 = 121
15^2 = 225
Muitasvezesprecisamosapresentarosdadosseguindoumaordemdefi-
nida.Nocasodoexemploanterior,aleituraficariamuitomaisfácilseapre-
sentássemososvaloresordenadamente.EmGo,aformarecomendadaéman-
terumaestruturadedadosseparadacontendoaschavesordenadas,iterando
sobreestaestruturaeobtendoosvalorescorrespondentesnomapa.V a m o s
adaptaroexemploanteriorparautilizarestatécnica,aproveitandoasfacilida-
desdopacote sortparaordenaralistadechaves.Crieumarquivochamado
cap4-mapa-ordenado/mapa_ordenado.gocomoseguinteconteúdo:
package main
import (
"fmt"
60

## Página 75

CasadoCódigo Capítulo4. Coleções: arrays,slicesemaps
"sort"
)
func main() {
quadrados := make(map[int]int, 15)
for n := 1; n <= 15; n++ {
quadrados[n] = n * n
}
numeros := make([]int, 0, len(quadrados))
for n := range quadrados {
numeros = append(numeros, n)
}
sort.Ints(numeros)
for _, numero := range numeros {
quadrado := quadrados[numero]
fmt.Printf("%d^2 = %d\n", numero, quadrado)
}
}
Agorasim,asaídadoprogramaapareceriaordenada:
$ go run cap4-mapa-ordenado/mapa_ordenado.go
1^2 = 1
2^2 = 4
3^2 = 9
4^2 = 16
5^2 = 25
6^2 = 36
7^2 = 49
8^2 = 64
9^2 = 81
10^2 = 100
11^2 = 121
12^2 = 144
13^2 = 169
61

## Página 76

4.3.Maps CasadoCódigo
14^2 = 196
15^2 = 225
Reparenousodafunção sort.Ints()paraordenaroslicecontendo
aschavesdomapa. Paramaioresdetalhessobreasfunções deordenação
disponíveisnestepacote,acesseadocumentaçãooficial(eminglês)emhttp:
//golang.org/pkg/sort/.
Nestecapítulo,vimosemdetalhesostiposnativosdecoleçãodedados,
abstraçõesextremamenteimportantesemuitoutilizadasnodesenvolvimento
depraticamentequalquerprograma.
Nocapítulo5,veremoscomocriarabstrações aindamaispoderosasatra-
vésdetiposcustomizados.
62

## Página 77

Capítulo5
Criandonovostipos
Criartiposcustomizadoséumaferramentadeabstraçãomuitopoderosaem
linguagensdeprogramação. Go,comparadaalinguagenspuramenteorien-
tadasaobjetos,temumsuportelimitadoàscaracterísticasdesteparadigma.
Porexemplo,não épossívelcriarumahierarquiadetiposbaseadaemhe-
rança.Composiçãodetipos,noentanto,ésuportadaeencorajadaemGo.
Doistipospodemtambémimplementarumaoumaisinterfacesemco-
mum,tornando-osaindamaisflexíveis.Veremostodasestascaracterísticas
naspróximasseções.
5.1 No v o snomes para tipos existentes
Algumaslinguagensdinâmicas–comoRuby–possibilitamqueoprograma-
doraltereocomportamentodequalquerclasseouobjetoduranteaexecução
deumprograma. EmGoistonão épossível,maspodemosestendertipos

## Página 78

5.1.Novosnomesparatiposexistentes CasadoCódigo
existentesatravésdacriação denovostipos,porconveniênciaousimples-
menteparamelhoraralegibilidadedeumprograma.
Para demonstrar esta técnica,vamos criar um novo tipo chamado
ListaDeComprasbaseadoemumslicede strings:
type ListaDeCompras []string
func main() {
lista := make(ListaDeCompras, 6)
lista[0] = "Alface"
lista[1] = "Pepino"
lista[2] = "Azeite"
lista[3] = "Atum"
lista[4] = "Frango"
lista[5] = "Chocolate"
fmt.Println(lista)
}
O código anterior imprimiria [Alface Pepino Azeite Atum
Frango Chocolate].
Inicialmente,otipo ListaDeComprasnão parecemuitoútil.Porém,
agrandevantagememcriartiposcustomizadoséquepodemosestendê-los,
algoimpossíveldesefazercomostipospadrões dalinguagem. V a m o ses-
tenderotipo ListaDeComprasparafacilitaranossavidaquandoformos
aosupermercado,definindoummétodoqueseparaoselementosdalistaem
categorias:
func (lista ListaDeCompras) Categorizar() (
[]string, []string, []string) {
var vegetais, carnes, outros []string
for _, e := range lista {
switch e {
case "Alface", "Pepino":
vegetais = append(vegetais, e)
case "Atum", "Frango":
64

## Página 79

CasadoCódigo Capítulo5.Criandonovostipos
carnes = append(carnes, e)
default:
outros = append(outros, e)
}
}
return vegetais, carnes, outros
}
Considerandoamesmalistadecomprasdoexemploanterior,podería-
moscategorizá-ladaseguinteforma:
vegetais, carnes, outros := lista.Categorizar()
fmt.Println("Vegetais:", vegetais)
fmt.Println("Carnes:", carnes)
fmt.Println("Outros:", outros)
Agoratemostrêsslicesdistintoscontendooselementosdalistadecom-
prascategorizados,eexecutandoestecódigoteríamososeguinteresultado:
Vegetais: [Alface Pepino]
Carnes: [Atum Frango]
Outros: [Azeite Chocolate]
Reparenaformacomqueocomando switchfoiutilizadonaimple-
mentaçãodométodo Categorizar(),verificandomúltiplosvalores–se-
paradosporvírgulas–emalgumasdascláusulascase.T a m b é mutilizamosa
cláusuladefaultparacriarumslicechamado outros,contendoqualquer
valorquenãofoireconhecidopelascláusulas caseespecificadasanterior-
mente.
5.2 Conversão entre tipos compatíveis
A p e s a rdo tipo ListaDeCompras ter sido criado com base no tipo
[]string,napráticaelessão diferentesenão são automaticamenteinter-
cambiáveis.Destaforma,nãoépossívelutilizarumvalor ListaDeCompras
emqueum []stringéesperadoevice-versa.
65

## Página 80

5.2.Conversãoentretiposcompatíveis CasadoCódigo
Paracontornaresteproblema,precisamosrealizarumaconversãodeti-
pos(operação conhecidaemGocomo type conversion)manualmente. Po-
demosconverterumvalorparaoutrotipoutilizandooformato T(x),onde
Téotipodestinoe xovaloraserconvertido.Vejamosumexemplocon-
vertendovaloresentre ListaDeComprase []string. Crieumarquivo
chamado cap5-conversao/conversao.gocomoconteúdo:
package main
import "fmt"
type ListaDeCompras []string
func imprimirSlice(slice []string) {
fmt.Println("Slice:", slice)
}
func imprimirLista(lista ListaDeCompras) {
fmt.Println("Lista de compras:", lista)
}
func main() {
lista := ListaDeCompras{"Alface", "Atum", "Azeite"}
slice := []string{"Alface", "Atum", "Azeite"}
imprimirSlice([]string(lista))
imprimirLista(ListaDeCompras(slice))
}
Podemosagoraexecutaresteprogramaeverificaroresultadodaconver-
sãoentreostipos:
$ go run cap5-conversao/conversao.go
Slice: [Alface Atum Azeite]
Lista de compras: [Alface Atum Azeite]
66

## Página 81

CasadoCódigo Capítulo5.Criandonovostipos
5.3 Criando abstrações mais poderosas
Jávimosnocapítulo4quepodemosfacilmentemanipularslicesutilizando
apenasoperações de slicingeafunção append().Podemostambémcriar
umacamadadeabstraçãosobreossliceseimplementarumalistagenéricaque
armazenavaloresdequalquertipoepossuioperações pararemovervalores
doinício,domeioedofimdalista. Primeirovejamosadefinição dotipo
propriamentedito:
type ListaGenerica []interface{}
Criamosumtipochamado ListaGenericabaseadoemumsliceque
armazenavaloresdotipo interface{},oquepermitequealistaarmazene
valoresdequalquertipo.
Agorapodemoscriarosmétodos,começandopelométodoqueremove
valoresdeumíndiceespecífico:
func (lista *ListaGenerica) RemoverIndice(
indice int) interface{} {
l := *lista
removido := l[indice]
*lista = append(l[0:indice], l[indice+1:]...)
return removido
}
Reparequedefinimosotipodoreceptorcomo *ListaGenerica–um
ponteiroparaumvalordotipo ListaGenerica–poisdesejamosalterar
oconteúdodalista.Inicialmentedefinimosumavariávellparafacilitaras
operações sobreoponteiro.Depoisatribuímosovalorpresentenoíndicees-
pecificadodalistaàvariávelremovido,queseráretornadaaofinaldomé-
todo.Tendoovalordesejadoemmãos,alteramosalistaparadesconsiderar
oelementoremovido,efinalmenteretornamosovalorremovido.
Paraimplementarométodoqueremovevaloresdoiníciodalista,pode-
mossimplesmentechamarométodoRemoverIndice()passando 0como
argumento:
67

## Página 82

5.3.Criandoabstrações maispoderosas CasadoCódigo
func (lista *ListaGenerica) RemoverInicio() interface{} {
return lista.RemoverIndice(0)
}
Istofuncionaporque,substituindoo indicenaoperaçãoquealteraa
listapor 0,obtemosaexpressão append(l[0:0], l[1:]...),ouseja,
adicionamososelementosdalistainiciandonoíndice 1àlistavaziaretor-
nadapelaoperação l[0:0].
Demaneiraanáloga,podemosimplementarométodoqueremovevalo-
resdofinaldalista,novamenterecorrendoaométodo RemoverIndice(),
agorapassandooúltimoíndicedalistacomoargumento:
func (lista *ListaGenerica) RemoverFim() interface{} {
return lista.RemoverIndice(len(*lista)-1)
}
O que ocorre neste caso éo inverso do que vimos com o método
RemoverInicio(). Assumindo que o últimoíndicepresente na lista
seja 5, podemos substituiro valor de indice para obtera expressão
append(l[0:5], l[6:]),ouseja,adicionamosalistavaziaretornadapor
l[6:]àlistadaqualovalordoíndice 5foiremovido.
Aseguirestáalistagemcompletadoprograma. Crieumnovoarquivo
chamado cap5-lista-generica/lista.gocomoconteúdo:
package main
import "fmt"
type ListaGenerica []interface{}
func (lista *ListaGenerica) RemoverIndice(
indice int) interface{} {
l := *lista
removido := l[indice]
*lista = append(l[0:indice], l[indice+1:]...)
return removido
}
68

## Página 83

CasadoCódigo Capítulo5.Criandonovostipos
func (lista *ListaGenerica) RemoverInicio() interface{} {
return lista.RemoverIndice(0)
}
func (lista *ListaGenerica) RemoverFim() interface{} {
return lista.RemoverIndice(len(*lista)-1)
}
func main() {
lista := ListaGenerica{
1, "Café", 42, true, 23, "Bola", 3.14, false,
}
fmt.Printf("Lista original:\n%v\n\n", lista)
fmt.Printf(
"Removendo do início: %v, após remoção:\n%v\n",
lista.RemoverInicio(), lista)
fmt.Printf(
"Removendo do fim: %v, após remoção:\n%v\n",
lista.RemoverFim(), lista)
fmt.Printf(
"Removendo do índice 3: %v, após remoção:\n%v\n",
lista.RemoverIndice(3), lista)
fmt.Printf(
"Removendo do índice 0: %v, após remoção:\n%v\n",
lista.RemoverIndice(0), lista)
fmt.Printf(
"Removendo do último índice: %v, após remoção:\n%v\n",
lista.RemoverIndice(len(lista)-1), lista)
}
Aoexecutaresteprograma,veremososeguinteresultado:
$ go run cap5-lista-generica/lista.go
Lista original:
[1 Café 42 true 23 Bola 3.14 false]
Removendo do início: 1, após remoção:
69

## Página 84

5.4.Structs CasadoCódigo
[Café 42 true 23 Bola 3.14 false]
Removendo do fim: false, após remoção:
[Café 42 true 23 Bola 3.14]
Removendo do índice 3: 23, após remoção:
[Café 42 true Bola 3.14]
Removendo do índice 0: Café, após remoção:
[42 true Bola 3.14]
Removendo do último índice: 3.14, após remoção:
[42 true Bola]
5.4 Structs
U m as t r u c t(estrutura)ésimplesmenteumacoleçãodevariáveisqueformam
umnovotipo.Structssãoimportantesparaagrupardadosrelacionados,cri-
andoanoçãoderegistros.Jávimosumexemplobásicodissonocapítulo3.2,
quandoimplementamosumapilhabaseadanumastructsimples.
Seestivéssemosdesenvolvendoumprogramaparaextrairestatísticasde
umarquivodetexto,poderíamosdefinirastruct Arquivodaseguinteforma:
type Arquivo struct {
nome string
tamanho float64
caracteres int
palavras int
linhas int
}
Comastructdefinida,podemoscriarumainstânciaespecificandoovalor
doscamposnaordememqueelesforamdefinidoseseparadosporvírgulas:
arquivo := Arquivo{"artigo.txt", 12.68, 12986, 1862, 220}
fmt.Println(arquivo)
70

## Página 85

CasadoCódigo Capítulo5.Criandonovostipos
Destaforma, teríamosovalor {artigo.txt 12.68 12986 1862
220}impresso.
Porquestõesdeclareza,podemosespecificarosnomesdoscamposaoini-
cializarumastruct.Istopodeserespecialmenteútilquandonãoprecisamos
atribuirvaloresatodososcamposnomomentodainicialização,etambém
eliminaanecessidadededeclararosvaloresnaordememqueforamdefini-
dos.Porexemplo:
codigoFonte := Arquivo{tamanho: 1.12, nome: "programa.go"}
fmt.Println(codigoFonte)
Estecódigoproduziria {programa.go 1.12 0 0 0}comoresultado.
Notequeosvaloresquenãoforamespecificados( caracteres, palavras
e linhas)foraminicializadoscom 0,o zero valueparaotipo int.
Paraacessarosvaloresemumastruct,utilizamosooperador .separando
onomedavariáveleonomedocampoacessado:
arquivo := Arquivo{"artigo.txt", 12.68, 12986, 1862, 220}
codigoFonte := Arquivo{tamanho: 1.12, nome: "programa.go"}
fmt.Printf("%s\t%.2fKB\n", arquivo.nome, arquivo.tamanho)
fmt.Printf("%s\t%.2fKB\n",
codigoFonte.nome,
codigoFonte.tamanho)
Esseprogramaimprimiriaoseguinteresultado:
artigo.txt 12.68KB
programa.go 1.12KB
Emprogramasmaiores,émuitocomuminicializarumastructearmaze-
narumponteiroparaelanumavariávelqueserámanipuladaposteriormente.
Paraisso,utilizamosooperador &,queretornaumponteiroparaastructcri-
ada.Porconveniência,aomanipularumponteiroparaumastructpodemos
omitirooperador *.Naprática,issonãoinfluenciaaformacomoutilizamos
avariável,comopodemosveraseguir:
71

## Página 86

5.4.Structs CasadoCódigo
ponteiroArquivo := &Arquivo{tamanho: 7.29, nome: "arquivo.txt"}
fmt.Printf("%s\t%.2fKB\n",
ponteiroArquivo.nome,
ponteiroArquivo.tamanho)
Qualquervalorarmazenadoemumastructpodeseralterado–structs
sãotiposmutáveis:
codigoFonte := Arquivo{tamanho: 1.12, nome: "programa.go"}
fmt.Printf("%s\t%.2fKB\n",
codigoFonte.nome,
codigoFonte.tamanho)
codigoFonte.tamanho = 23.42
fmt.Printf("%s\t%.2fKB\n",
codigoFonte.nome,
codigoFonte.tamanho)
Executandoessecódigoveríamososseguintesvaloresimpressos:
Antes: programa.go 1.12KB
Depois: programa.go 23.42KB
Emlingugensorientadasaobjetostradicionais,definimosnovostipos
usandoclasses,quereunemdados(estado)emétodos(comportamento)em
umamesmaunidade–aprópriaclasse.
EmGo,utilizamosstructsparadefinirnovostipos. Assimcomofize-
mosanteriormentequandodefinimostiposqueestendemostipospadrãoda
linguagem,podemostambémdefinirmétodoscujosreceptoressão structs,
atingindonapráticaumefeitomuitosemelhanteàdefiniçãodeumaclasse.
V a m o senriquecer nosso tipo Arquivo criando dois métodos–
TamanhoMedioDePalavra()e MediaDePalavrasPorLinha():
func (arq *Arquivo) TamanhoMedioDePalavra() float64 {
return float64(arq.caracteres) / float64(arq.palavras)
}
func (arq *Arquivo) MediaDePalavrasPorLinha() float64 {
72

## Página 87

CasadoCódigo Capítulo5.Criandonovostipos
return float64(arq.palavras) / float64(arq.linhas)
}
func main() {
arquivo := Arquivo{"artigo.txt", 12.68, 12986, 1862, 220}
fmt.Printf("Média de palavras por linha: %.2f\n",
arquivo.MediaDePalavrasPorLinha())
fmt.Printf("Tamanho médio de palavra: %.2f",
arquivo.TamanhoMedioDePalavra())
}
Aimplementaçãodessesmétodosébastantetrivial.Executandoafunção
main()teríamososeguinteresultado:
Média de palavras por linha: 8.46
Tamanho médio de palavra: 6.97
Éimportantenotaraconversãode intpara float64nomomentoda
divisão, poisqueremosqueoresultadosejaumnúmerodecimal. Quando
dividimosdois ints,oresultadoproduzidoéoutro inteapartedecimal
donúmeroétruncada. Porexemplo,adivisão 2 / 3produziria 0como
resultado.
5.5 Interfaces
U m ainterfaceéadefiniçãodeumconjuntodemétodoscomunsaumoumais
tipos.ÉoquepermiteacriaçãodetipospolimórficosemGo.
Javapossuiumconceitomuitoparecido,tambémchamadodeinterface.
Agrandediferençaéque,emGo,umtipoimplementaumainterface im-
plicitamente–bastaqueestetipodefina t o d o sosmétodosdestainterface,
nãohavendoanecessidadedepalavras-chavecomo implements, extendsetc.
Porexemplo,vamoscriarumainterfacechamada Operacao,quedefineum
únicométodo Calcular():
type Operacao interface {
Calcular() int
}
73

## Página 88

5.5.Interfaces CasadoCódigo
Podemosagoracriarumtipochamado Somacontendodoisoperandos,
eimplementarométodo Calcular(). Parafacilitaraleituradosresulta-
dos,vamostambémimplementarométodo String(),queretornauma
representaçãotextualdaoperaçãodesoma.Estemétodoéinvocadoautoma-
ticamentequandoqueremosapresentarumvalorutilizandoopacote fmt.
Paraimplementá-lo,vamosutilizarafunção Sprintf()doprópriopacote
fmt,queretornauma stringformatada:
type Soma struct {
operando1, operando2 int
}
func (s Soma) Calcular() int {
return s.operando1 + s.operando2
}
func (s Soma) String() string {
return fmt.Sprintf("%d + %d", s.operando1, s.operando2)
}
Parautilizarestetiponaprática,poderíamossimplesmentedeclarareins-
tanciarumavariáveldotipo Soma. Entretanto,prestandoumpoucomais
deatenção,podemosverqueaassinaturadométodo Calcular()dotipo
Somasatisfazadefiniçãodainterface Operacao,eistoésuficienteparadi-
zerquea Soma é u m aOperacao.Destaforma,podemosatribuirumvalor
Somaaumavariáveldefinidacomosendodotipo Operacao:
var soma Operacao
soma = Soma{10, 20}
fmt.Printf("%v = %d\n", soma, soma.Calcular())
Reparenaformacomoutilizamosomarcador %vparaobterarepresen-
tação stringdeuma Soma–nestecaso, 10 + 20.Assim,executandoeste
códigoteríamosoresultado 10 + 20 = 30.
U múnicotiponãoésuficienteparademonstraraflexibilidadedeumain-
terface.Então,vamosagoracriarumnovotipochamado Subtracao,tam-
bémimplementandoainterface Operacao.Emseguidacriaremosumalista
7 4

## Página 89

CasadoCódigo Capítulo5.Criandonovostipos
deoperações queserãocalculadasindependentedotipo.Primeiro,vamosao
códigodotipo Subtracao:
type Subtracao struct {
operando1, operando2 int
}
func (s Subtracao) Calcular() int {
return s.operando1 - s.operando2
}
func (s Subtracao) String() string {
return fmt.Sprintf("%d - %d", s.operando1, s.operando2)
}
V a m o sagora criar uma lista de operações e calcular o va-
lor acumulado de todas elas. Crie um novo arquivo chamado
cap5-operacoes/operacoes.go. Adicione a ele as definições dos
tipos Operacao, Somae Subtracaodaformacomoforamapresentados
anteriormentee,porfim,crieaseguintefunção main():
func main() {
operacoes := make([]Operacao, 4)
operacoes[0] = Soma{10, 20}
operacoes[1] = Subtracao{30, 15}
operacoes[2] = Subtracao{10, 50}
operacoes[3] = Soma{5, 2}
acumulador := 0
for _, op := range operacoes {
valor := op.Calcular()
fmt.Printf("%v = %d\n", op, valor)
acumulador += valor
}
fmt.Println("Valor acumulado =", acumulador)
}
V e j aumexemplodaexecuçãodesteprograma:
75

## Página 90

5.6. Duck typingepolimorfismo CasadoCódigo
$ go run cap5-operacoes/operacoes.go
10 + 20 = 30
30 - 15 = 15
10 - 50 = -40
5 + 2 = 7
Valor acumulado = 12
5.6 Duck typing e polimorfismo
Duck typing(ou tipagem pato,emportuguêsliteral)éacapacidadedeum
sistemadetiposdedeterminarasemânticadeumdadotipobaseadoemseus
métodosenãoemsuahierarquia.Onometemorigemnochamado d u c ktest
(ou teste do pato):sefaz“ q u a c k ”comoumpatoeandacomoumpato,então
provavelmente éumpato.
Émaiscomumencontrarestapropriedadeemlinguagensdinamicamente
tipadascomoRubyouPython. Porém,comoGonãopermiteherançamas
ostiposimplementaminterfacesimplicitamente,napráticaconsidera-seque
Goimplementaumaformade d u c ktyping,comagrandevantagemdeter,
emtempodecompilação,agarantiadequeotipoesperadocomoargumento
implementaainterfacedesejada.
Parafacilitaroentendimento,vamosalteraroexemploanterioreex-
trairocódigoquecalculaovaloracumuladodalistadeoperações dafunção
main()paraumanovafunção:
func acumular(operacoes []Operacao) int {
acumulador := 0
for _, op := range operacoes {
valor := op.Calcular()
fmt.Printf("%v = %d\n", op, valor)
acumulador += valor
}
return acumulador
}
Destaforma,poderíamosreutilizarafunção acumular()passando
76

## Página 91

CasadoCódigo Capítulo5.Criandonovostipos
comoargumentoumslicecontendoquaisquerobjetosqueimplementassem
ométodo Calcular(),retornandoum int.
Para demonstrar este fato, vamos adicionar ao arquivo
cap5-operacoes/operacoes.goadefinição deumnovotipo Idade
implementandoométodo Calcular(). V a m o salterartambémafunção
main()parachamarafunção acumular()utilizandoobjetosdestetipo
paraobteraidadeacumulada:
type Idade struct {
anoNascimento int
}
func (i Idade) Calcular() int {
return time.Now().Year() - i.anoNascimento
}
func (i Idade) String() string {
return fmt.Sprintf("Idade desde %d", i.anoNascimento)
}
func main() {
operacoes := make([]Operacao, 4)
operacoes[0] = Soma{10, 20}
operacoes[1] = Subtracao{30, 15}
operacoes[2] = Subtracao{10, 50}
operacoes[3] = Soma{5, 2}
fmt.Println("Valor acumulado =", acumular(operacoes))
idades := make([]Operacao, 3)
idades[0] = Idade{1969}
idades[1] = Idade{1977}
idades[2] = Idade{2001}
fmt.Println("Idades acumuladas =", acumular(idades))
}
Assumindo2014comooanoatual,umexemplodaexecuçãodestepro-
gramaseria:
77

## Página 92

5.7.Umexemplodabibliotecapadrão:io.Reader CasadoCódigo
$ go run cap5-operacoes/operacoes.go
10 + 20 = 30
30 - 15 = 15
10 - 50 = -40
5 + 2 = 7
Valor acumulado = 12
Idade desde 1969 = 45
Idade desde 1977 = 37
Idade desde 1999 = 15
Idades acumuladas = 97
5.7 Um exemplo d a biblioteca padrão :
io.Reader
Abibliotecapadrão ésempreumaboareferênciaparaboaspráticas.Por-
tanto, vamos recorrer a uma interface muito importante presente nela:
io.Reader.EstainterfacedefineumúnicométodoRead()comaseguinte
assinatura:
func Read(p []byte) (n int, err error)
Estafunçãolêaté len(p)bytes,armazenaestesbytesem peretornao
númerodebyteslidosemcasodesucesso,ouum erroremcasodeerrona
leitura.
Comopudemosveranteriormente,qualquerobjetoqueimplementeo
métodoRead()comamesmaassinaturapoderáserusadoemumcontexto
ondeum io.Readeréesperado.
V a m o scriarumexemplosimplesde io.Reader.Paraisso,vamoscriar
umnovoarquivochamado cap5-leitor/leitor.godeclarandoasse-
guintesdependências:
import (
"fmt"
"io"
)
Agora vamos definir um novo tipo simples chamado
LeitorDeStrings, que não possui nenhum atributo e implementa
78

## Página 93

CasadoCódigo Capítulo5.Criandonovostipos
somenteométodo Read(),retornandoumslicede bytes–[]byte
–contendo uma string ASCII simples, porémrespeitando a interface
io.Reader:
type LeitorDeStrings struct{}
func (l LeitorDeStrings) Read(p []byte) (int, error) {
p[0] = ’A’
p[1] = ’B’
p[2] = ’C’
p[3] = ’D’
return len(p), nil
}
Emseguidavamosimplementarumafunçãochamada lerString(),
querecebecomoargumentoum io.Reader,chamaseumétodo Read(),
converteoslicede bytesresultanteemuma stringpropriamenteditaea
retorna:
func lerString(r io.Reader) string {
p := make([]byte, 4)
r.Read(p)
return string(p)
}
Por fim, na função main(), vamos criar uma instância de
LeitorDeStrings e utilizá-lacomo um io.Reader ao chamar a
função lerString(),imprimindoseuresultado:
func main() {
leitor := LeitorDeStrings{}
fmt.Println(lerString(leitor))
}
A seguir você encontra a listagem completa do arquivo
cap5-leitor/leitor.go:
package main
79

## Página 94

5.7.Umexemplodabibliotecapadrão:io.Reader CasadoCódigo
import (
"fmt"
"io"
)
type LeitorDeStrings struct{}
func (l LeitorDeStrings) Read(p []byte) (int, error) {
p[0] = ’A’
p[1] = ’B’
p[2] = ’C’
p[3] = ’D’
return len(p), nil
}
func lerString(r io.Reader) string {
p := make([]byte, 4)
r.Read(p)
return string(p)
}
func main() {
leitor := LeitorDeStrings{}
fmt.Println(lerString(leitor))
}
U mexemplodasaídaproduzidaporesteprograma:
$ go run cap5-leitor/leitor.go
ABCD
Alémdousodainterface io.Reader,háumaoutranovidadenoexem-
ploanterior:ousodecaracteresliterais–queemGosãodotipo rune.Este
tipofoicriadopararepresentarumcódigoUnicodeem32bits–runeéum
a l i a sparaotipo int32.
Defato,acodificaçãoUnicodeétãoimportanteemGoquetoda string
eopróprio código-fonte são codificadoscomoUTF-8porpadrão. Ken
80

## Página 95

CasadoCódigo Capítulo5.Criandonovostipos
ThompsoneRobPike,doisdoscriadoresdalinguagem,foramtambémres-
ponsáveispelaimplementaçãooriginaldopadrãoUTF-8.Destaforma,qual-
quercaractereUTF-8podeserutilizadolivrementeemprogramasescritos
emGo.
Nestecapítulo,aprendemosacriarnovostiposeabstrações baseadosem
structse interfaces.T a m b é mconhecemosumpoucosobreaimpor-
tanteinterface io.Reader,presentenabibliotecapadrão.
Nocapítulo ??,veremosemdetalhesosrecursosparaacriaçãoemani-
pulaçãodefunções.
81

## Página 97

Capítulo6
F u nções
A t éagorajácriamosdiversasfunções emdiferentescontextos.Criamosin-
clusiveumafunçãorecursivaquandoimplementamosoalgoritmo q u i c k s o r t
nocapítulo2.6. T a m b é mjávimoscomocriarobjetoseadicionarmétodos
quedefinemseucomportamento.
NestecapítuloveremosemdetalhestodososrecursosdisponíveisemGo
paraescreverfunções.
6.1 A forma básica
Apenaspararelembrar,utilizamosapalavra-chave funcparadeclararuma
novafunção. Porexemplo,umafunçãoquenãorecebenenhumargumento
enãoretornanenhumvalorpodeserdeclaradadaseguinteforma:
func ImprimirVersao() {
fmt.Println("1.12")

## Página 98

6.1.Aformabásica CasadoCódigo
}
Argumentossãodeclaradosdemaneirasimilaravariáveis,portanto,es-
pecificamosprimeiroseunome,edepoisseutipo:
func ImprimirSaudacao(nome string) {
fmt.Printf("Olá, %s!\n", nome)
}
Múltiplosargumentossãoseparadosporvírgulas:
func ImprimirDados(nome string, idade int) {
fmt.Printf("%s, %d anos.\n", nome, idade)
}
E,casoosargumentossejamdomesmotipo,podemosespecificá-louma
únicavez:
func ImprimirSoma(a, b int) {
fmt.Println(a + b)
}
Istofuncionainclusivequandoafunçãorecebemaisargumentosdeou-
trostipos.Adeclaraçãopodeserfeitadaseguinteforma:
func ImprimirSoma(a, b int, texto string) {
fmt.Printf("%s: %d\n", texto, a + b)
}
Pararetornarumvalor,especificamosseutipoaofinaldadeclaração e
utilizamosapalavra-chave returnpararetorná-lo:
func Somar(a, b int) int {
return a + b
}
Podemostambémespecificarmúltiplosvaloresderetorno,deformabas-
tantesimilaràlistadeargumentos:
84

## Página 99

CasadoCódigo Capítulo6. Funções
func PrecoFinal(precoCusto float64) (float64, float64) {
fatorLucro := 1.33
taxaConversao := 2.34
precoFinalDolar := precoCustoDolar * fatorLucro
return precoFinalDolar, precoFinalDolar * taxaConversao
}
6.2 Valores de retorno nomeados
Osvaloresretornadosporumafunção podemsernomeadosnomomento
dadeclaração, fazendocomqueelesestejamautomaticamentedisponíveis
comovariáveisnocorpodafunção.Destaforma,podemosutilizarapalavra-
chave returnsemespecificarnenhumvalor;osvaloresatuaisdasvariáveis
declaradasnadefiniçãodafunçãoserão retornados.Vejamosumexemplo,
reescrevendoafunção PrecoFinal()apresentadaanteriormente:
func PrecoFinal(precoCusto float64) (
precoDolar float64,
precoReal float64) {
fatorLucro := 1.33
taxaConversao := 2.34
precoDolar = precoCusto * fatorLucro
precoReal = precoDolar * taxaConversao
return
}
func main() {
precoDolar, precoReal := PrecoFinal(34.99)
fmt.Printf("Preço final em dólar: %.2f\n" +
"Preço final em reais: %.2f\n",
precoDolar, precoReal)
}
85

## Página 100

6.2. Valoresderetornonomeados CasadoCódigo
Repare que no corpo da função atribuímosos valores às variáveis
precoDolare precoRealdiretamenteutilizandoooperador =,poiselas
jáforamdeclaradasnadefiniçãodafunção.
Nomearosvaloresderetornoéumaótimamaneiradedocumentaruma
função.Noexemplomodificado,definimosqueafunçãoretornadoisvalores
específicos–precoDolare precoReal–tornandosuaintenção muito
maisclara.Noentanto,utilizarapalavra-chave returnsemespecificaros
valoresretornadosdificultaoentendimentodocódigo.Porissoésemprere-
comendávelespecificarosvaloresretornadosexplicitamente,mesmoqueeles
játenhamsidonomeadosnaassinaturadafunção.
Aseguir,vamosmodificarnovamenteafunção PrecoFinal()paradei-
xarexplícitoquaissãoosvaloresretornados.Crieumnovoarquivochamado
cap6-retornos-nomeados/precos.gocomoconteúdo:
package main
import "fmt"
func PrecoFinal(precoCusto float64) (
precoDolar float64,
precoReal float64) {
fatorLucro := 1.33
taxaConversao := 2.34
precoDolar = precoCusto * fatorLucro
precoReal = precoDolar * taxaConversao
return precoDolar, precoReal
}
func main() {
precoDolar, precoReal := PrecoFinal(34.99)
fmt.Printf("Preço final em dólar: %.2f\n" +
"Preço final em reais: %.2f\n",
precoDolar, precoReal)
}
86

## Página 101

CasadoCódigo Capítulo6. Funções
Executandoesteprograma,teríamososeguinteresultado:
$ go run cap6-retornos-nomeados/precos.go
Preço final em dólar: 46.54
Preço final em reais: 108.90
6.3 Argumentos v ariáveis
U m afunçãopodereceberumnúmerovariáveldeargumentos.Funções deste
tiposão conhecidasemGocomo variadic fu nct io ns. Jáutilizamosalgumas
delas,comoporexemplo fmt.Printf()e append().
Paracriaruma variadic fu nct io n,devemosprecederotipodoúltimo(ou
único)argumentocomreticências.Naprática,asreticênciasindicamquea
funçãopodereceberzerooumaisargumentosdotipoespecificado.
V a m o sdefinirumafunçãoquerecebeumalistavariáveldenomesdear-
quivosecriacadaumdelesemumdiretóriotemporário.Paraisto,vamos
utilizaralgumasfunções presentesnopacote os:
func CriarArquivos(dirBase string, arquivos ...string) {
for _, nome := range arquivos {
caminhoArquivo := fmt.Sprintf(
"%s/%s.%s", dirBase, nome, "txt")
arq, err := os.Create(caminhoArquivo)
defer arq.Close()
if err != nil {
fmt.Printf("Erro ao criar arquivo %s: %v\n",
nome, err)
os.Exit(1)
}
fmt.Printf("Arquivo %s criado.\n", arq.Name())
}
}
Noteousodasreticênciasnadeclaração doargumento arquivos:
arquivos ...string.
87

## Página 102

6.3. Argumentosvariáveis CasadoCódigo
Aimplementação dafunção étrivial. Percorremosalistadenomesde
arquivosrecebidae,paracadanomedearquivo,compilamosseucaminho
completoapartirdodiretórioespecificadoem dirBaseeutilizamosafun-
ção os.Create()paracriá-loemdisco.Essafunçãorecebeumcaminho
completodearquivoecriaumarquivonovonocaminhoespecificado.Caso
oarquivoemquestãojáexista,seuconteúdoserátotalmenteapagado,resul-
tandoemumarquivovazio.
Alémdeefetivamentecriaroarquivo,afunção os.Create()retorna
umponteiroparaumobjetodotipo os.Filerepresentandoodescritordo
arquivocriado.Estedescritorpodeserusadopararealizaroutrasoperações
noarquivo. Nesteexemplo,porém,apenaschamamosométodo Name()
paraobterseucaminhocompleto.
Afunção os.Create()tambémpoderetornarumerrocasonãoseja
possívelcriaroarquivo.Seistoacontecer,aexecuçãoseráinterrompidaeo
programaseráencerradoatravésdachamadaàfunção os.Exit().
Porfim,éimportantenotarousodapalavra-chave defer.Elaéutilizada
parainstruiroambientedeexecuçãoGoarealizarumatarefaimediatamente
antesdeafunçãoatualretornar.Ébastantecomumutilizar deferparaga-
rantirqueosrecursosalocadospelafunção sejamliberadosaofinaldesua
execução.Nesteexemplo,chamamosométodoClose()nodescritordoar-
quivocriadoparatercertezadequeeleserádevidamentefechadoeliberado.
Como dito anteriormente, uma função com argumentos va-
riáveis pode receber zero ou mais argumentos do tipo especi-
ficado. Para entender melhor, crie um novo arquivo chamado
cap6-variadic-functions/arquivos.go. Adicione a ele a fun-
ção CriarArquivos() apresentada anteriormente e, então, adicione
a seguinte função main() para realizar algumas chamadas à função
CriarArquivos()comlistasdeargumentosdiferentes:
func main() {
tmp := os.TempDir()
CriarArquivos(tmp)
CriarArquivos(tmp, "teste1")
CriarArquivos(tmp, "teste2", "teste3", "teste4")
}
88

## Página 103

CasadoCódigo Capítulo6. Funções
Inicialmentecriamosavariáveltmpeatribuímosaelaovalorretornado
por os.TempDir().Essafunçãoretornaocaminhododiretóriotemporário
utilizadopeloambientedeexecução Go. Emseguida,chamamosafunção
CriarArquivos()emtrêscenáriosdiferentes:inicialmentesemnenhum
nomedearquivo;depoiscomumúniconomedearquivo;eporfim,comtrês
nomesdearquivosdistintos.Aofinaldaexecução,oresultadoesperadoéque
osarquivos teste1.txt, teste2.txt, teste3.txte teste4.txt
sejamcriadosemdisco.
Aseguirencontramosumexemplodasaídadaexecuçãodesteprograma
noLinux:
$ go run cap6-variadic-functions/arquivos.go
Arquivo /tmp/teste1.txt criado.
Arquivo /tmp/teste2.txt criado.
Arquivo /tmp/teste3.txt criado.
Arquivo /tmp/teste4.txt criado.
Paraverificarmosqueosarquivosforamrealmentecriados,podemoslis-
tarosarquivosdodiretóriotemporário:
$ ls -l /tmp/
-rw-r--r-- 1 user group 0B May 1 10:56 teste1.txt
-rw-r--r-- 1 user group 0B May 1 10:56 teste2.txt
-rw-r--r-- 1 user group 0B May 1 10:56 teste3.txt
-rw-r--r-- 1 user group 0B May 1 10:56 teste4.txt
6.4 Funções de primeira classe
Funções emGosão first-class citizens(cidadãosdeprimeiraclasse).Issosig-
nificaquefunções podemserpassadascomoparâmetroparaoutras,ouuti-
lizadascomovaloresderetorno,eatémesmocomomembrosdeuma s t r u c t
oucoleção.
Sevocêjátrabalhoucomfunções e callbacksemJavaScript, lambdasem
Ruby,PythonouJava(quefinalmenteintroduziuexpressões lambdanaversão
8),ouescreveuprogramasemqualquerlinguagempuramentefuncional–
Lisp,Haskell,Scala,ErlangouClojure,paracitaralgunsexemplos–,jádeve
estarfamiliarizadocomosconceitosqueserãoapresentadosaseguir.
89

## Página 104

6.5. Funções anônimas CasadoCódigo
6.5 Funções anônimas
Duranteodesenvolvimentodeumaaplicaçãoémuitocomumencontrarmos
problemasqueexigemalgumtipodemanipulaçãodetextos:substituiçãode
caracteresacentuados,processamentode templates(modelosdedocumentos)
etc.
U m adasformasmaispoderosasderesolverestetipodeproblemaéo
usodeexpressões regulares.Godisponibilizaumasériedefacilidadespara
trabalharcomelasnopacote regexp,bastaadicioná-loàlistadepacotes
especificadosnacláusulaimport.
V e j aoexemploaseguir:
func main() {
texto := "Anderson tem 21 anos"
expr := regexp.MustCompile("\\d")
fmt.Println(expr.ReplaceAllString(texto, "3"))
}
Inicialmente criamos a expressão regular expr atravésda função
regexp.MustCompile().Essafunçãorecebeaexpressãodesejadaemfor-
mato string,compila-aeretornaumponteiroparaumobjetodotipo
regexp.Regexp,utilizadoparainteragircomaexpressãocompilada.Neste
exemplo,criamosumaexpressãoregularqueirácapturarqualquercaractere
numérico( \d,queprecisaserutilizadocomoumasequênciadeescapeden-
troda string,porissoutilizamosaduplabarrainversa).
Comaexpressão regularcompiladaemmãos, chamamosseumétodo
ReplaceAllString(),especificandoa stringquedeveráserprocessada
( Anderson tem 21 anos)eumasegunda stringindicandootextoque
irásubstituirosnúmerosencontrados–nestecaso,desejamossubstituiros
números2e1pelonúmero3.Destaforma,executandoafunção main()
apresentada,teríamosotexto Anderson tem 33 anosimpresso.
Estaéaformamaiscomumdesubstituiçãodetextosutilizandoexpres-
sões regulares.Noentanto,emalgunscasosprecisamosconstruirprocessa-
doresmaiscomplexos.Porexemplo,desejamostransformaraprimeiraletra
decadapalavraemmaiúscula.Éimpossívelresolveresteproblemausando
umasubstituiçãosimplescomoadoexemploanterior.
90

## Página 105

CasadoCódigo Capítulo6. Funções
Para resolver esses casos, objetos do tipo regexp.Regexp pos-
suem um método similar ao ReplaceAllString(), chamado
ReplaceAllStringFunc() que, em vez de uma string, aceita
umafunçãocomosegundoargumento.Eladeve,porsuavez,receberuma
stringcomoargumentoeretornaroutra stringtransformada. Neste
caso,utilizamosafunção ToUpper()dopacote stringsparatransformar
a stringrecebidaemmaiúsculas:
func main() {
expr := regexp.MustCompile("\\b\\w")
texto := "antonio carlos jobim"
processado := expr.ReplaceAllStringFunc(
texto,
func(s string) string {
return strings.ToUpper(s)
})
fmt.Println(processado)
}
Reparequedefinimosafunção transformadoranaprópriachamadaà
função ReplaceAllStringFunc(). Reparetambémqueafunção defi-
nidanãopossuiumnome.Funções destetipo–definidasnomomentoem
quesãoutilizadas–sãoconhecidascomo funçõ e sanônimas.
T a m b é mpodemosarmazenarumafunçãoanônimaemumavariável,e
nosreferirmosaestavariávelposteriormente. V a m o smodificaroexemplo
anteriorparautilizarestatécnica.Adicioneoseguintecódigoaumnovoar-
quivochamado cap6-funcoes-anonimas/regexp.go:
package main
import (
"fmt"
"regexp"
"strings"
)
91

## Página 106

6.6. Closures CasadoCódigo
func main() {
expr := regexp.MustCompile("\\b\\w")
transformadora := func(s string) string {
return strings.ToUpper(s)
}
texto := "antonio carlos jobim"
fmt.Println(transformadora(texto))
fmt.Println(expr.ReplaceAllStringFunc(
texto, transformadora))
}
Extraímosa mesma função anônima utilizada no exemplo anterior,
agoraaatribuindoàvariável transformadora. Éimportantenotarque
transformadora não éo nomeda função, éapenasum identificador
paraumaposição dememóriaquearmazenaumafunção, queentão utili-
zamosemdoiscontextosdistintos:primeiro,fazemosumachamadaexplí-
citaparatransformarotexto antonio carlos jobimemmaiúsculas;por
fim,passamosafunção transformadoracomoargumentoparaafunção
regexp.ReplaceAllStringFunc(),queiráentão substituirapenasos
caracterescapturadospelaexpressãoregular expr.
Executandoesseexemplo,teríamososeguinteresultado:
$ go run cap6-funcoes-anonimas/regexp.go
ANTONIO CARLOS JOBIM
Antonio Carlos Jobim
Parasabermaissobreosrecursosdopacote regexp,visitehttp://golang.
org/pkg/regex/.
6.6 Closures
Funções definidasdeformaanônimadentrodeoutrafunçãoherdamocon-
textodeondeelasforamcriadas.Parademonstrarestefato,vamoscriaruma
implementaçãodasequênciadeFibonacciutilizandoumafunçãoanônima.
92

## Página 107

CasadoCódigo Capítulo6. Funções
Crieumnovoarquivo cap6-closures/fibonacci.gocomoseguinte
código:
package main
import "fmt"
func main() {
a, b := 0, 1
fib := func() int {
a, b = b, a+b
return a
}
for i := 0; i < 8; i++ {
fmt.Printf("%d ", fib())
}
}
Inicialmente,declaramoseinicializamosasvariáveisae bcomosvalores
0e1,respectivamente,dentrodaprópriafunção main().
Emseguida,definimosafunção anônima –atribuídaàvariável fib–
quecalculaasequênciadeFibonacci.Reparequeestafunçãomanipuladi-
retamenteasvariáveisae b,atualizandoseusvaloresacadachamada.Esta
propriedadedeumafunçãopodermanipularocontextoondeelafoiorigi-
nalmentedefinidaéconhecidacomo c l o s u r e(c l a u s u r aemportuguês,embora
estetermosejararamentetraduzido).
Executandooprogramacriadoanteriormente,teríamososeguinteresul-
tado:
$ go run cap6-closures/fibonacci.go
1 1 2 3 5 8 13 21
93

## Página 108

6.7. Higher-order functions CasadoCódigo
6.7 Higher -order functions
Comojáfoidito,funçõesemGopodemretornaroutrasfunçõesourecebê-las
comoargumentos.Asfunções quepossuemestascaracterísticassãoconhe-
cidascomo higher-order fu nct io ns(fu nções de o rd e msuperioremportuguês–
novamenteumtermoraramenteutilizado)esãopartefundamentaldequal-
querlinguagemdeprogramaçãofuncional. A p e s a rdealinguagemGonão
serumalinguagemfuncionalpura,eladisponibilizaalgumasdaspoderosas
abstrações introduzidasporesteparadigma.
V a m o sextrair a função que calcula a sequênciade Fibonacci –
apresentada no exemplo anterior –para uma função externa chamada
GerarFibonacci(), alterando-a para que receba a quantidade de nú-
meros que deverão ser gerados. T a m b é mprecisamos fazer com que
esta função retorne outra função capaz de gerar a sequênciade Fi-
bonacci. Adicione o seguinte código a um novo arquivo chamado
cap6-higher-order-functions/cronometro.go:
package main
import (
"fmt"
"time"
)
func GerarFibonacci(n int) func() {
return func() {
a, b := 0, 1
fib := func() int {
a, b = b, a+b
return a
}
for i := 0; i < n; i++ {
fmt.Printf("%d ", fib())
}
}
94

## Página 109

CasadoCódigo Capítulo6. Funções
}
É importante notar que, como queremos que a função
GerarFibonacci() retorne outra função, definimos seu tipo de re-
tornocomosendo func()–umafunçãosemargumentosequenãoretorna
nenhumvalor.
Emseguida,vamoscriarumanovafunçãochamada Cronometrar(),
quereceberácomoargumentoumafunção qualquerecalcularáseutempo
deexecução,utilizandorecursosdopacote time:
func Cronometrar(funcao func()) {
inicio := time.Now()
funcao()
fmt.Printf("\nTempo de execução: %s\n\n",
time.Since(inicio))
}
Assimcomodefinimosqueafunção GerarFibonacci()retornauma
função, agoraespecificamosquea Cronometrar()recebetambémuma
função semargumentosesemvalorderetornochamada funcaodotipo
func().
Primeiro,armazenamosotempoatual–time.Now()–navariável
inicio.
Em seguida, chamamos a função recebida como argumento. Aqui
ficaclaroomotivopeloqual GerarFibonacci()retornaoutrafunção:
para quepossamos calcular seu tempode execução, precisamoscontro-
lar q u a n d oelaseráchamada. Assim, passamosafunção retornadapor
GerarFibonacci()comoargumentopara Cronometrar(),queporsua
vezdecideomomentoapropriadopararealizarachamada.
Porfim,utilizamosafunção time.Since()paracalcularointervalo
detempoentreomomentoatualeomomentoarmazenadoem inicio.Ela
retornaumvalordotipo time.Duration,querepresentaumperíodode
tempo.Estetipopossuiváriosmétodosúteis.Nesteexemplo,porém,utiliza-
mosapenasarepresentação stringdesteobjetoparaimprimirotempode
execuçãoda funcao.
95

## Página 110

6.8. Tiposdefunção CasadoCódigo
V a m o sagoracriarumafunção main()paracronometrarageraçãoda
sequênciadeFibonacciemtrêssituações diferentes:
func main() {
Cronometrar(GerarFibonacci(8))
Cronometrar(GerarFibonacci(48))
Cronometrar(GerarFibonacci(88))
}
Aseguirencontramosumexemplodasaídadesteprograma. Partedas
sequênciasgeradasforamomitidasparafacilitaravisualização:
$ go run cap6-higher-order-functions/cronometro.go
1 1 2 3 5 8 13 21
Tempo de execução: 51.647us
1 1 2 3 5 8 13 21 34 55 ... 701408733 1134903170 1836311903
2971215073 4807526976
Tempo de execução: 66.315us
1 1 2 3 5 8 ... 420196140727489673 679891637638612258
1100087778366101931
Tempo de execução: 130.485us
Repare na representação do tempo de execução de cada função:
51.647us para gerar8números, 66.315us para gerar48númerose
130.485usparagerarumasequênciade88números.Afunção String()
dotipo time.Durationdecideautomaticamenteaunidadedetempouti-
lizadadeacordocomotamanhodoperíodorepresentado.Nestecaso,auni-
dadeutilizadafoiomicrossegundo(µs).
Paramaioresinformações sobreasfunções etiposdisponíveisnopacote
time,visitehttp://golang.org/pkg/time/.
6.8 Tiposde função
Noexemploanterior,criamosumafunção Cronometrar()querecebe
comoargumentoumaoutrafunção. Esta,porsuavez,nãorecebenenhum
96

## Página 111

CasadoCódigo Capítulo6. Funções
argumentoenãoretornanenhumvalor.Algumasvezes,noentanto,precisa-
mosrecebercomoargumentofunções maiscomplexaseflexíveis.
U m adasformasdeobtertalflexibilidadeéatravésdadefiniçãodetipos
parafunções (fu nct io ntypes).
Considereumafunçãodeagregaçãoquerecebeumalistadevalores,um
valorinicialeumafunçãoagregadora:
func Agregar(
valores []int,
inicial int,
fn func(n, m int) int,
) int {
agregado := inicial
for _, v := range valores {
agregado = fn(v, agregado)
}
return agregado
}
Utilizando-acomobase,podemosagoraescreverumafunçãoparacalcu-
larasomadeumasérienumérica:
func CalcularSoma(valores []int) int {
soma := func(n, m int) int {
return n + m
}
return Agregar(valores, 0, soma)
}
Etambémpodemosescreverumafunçãoparacalcularoprodutodeuma
sérienumérica:
func CalcularProduto(valores []int) int {
multiplicacao := func(n, m int) int {
return n * m
}
97

## Página 112

6.8. Tiposdefunção CasadoCódigo
return Agregar(valores, 1, multiplicacao)
}
Podemosagoracriarafunção main()eutilizarasduasnovasfunções:
func main() {
valores := []int{3, -2, 5, 7, 8, 22, 32, -1}
fmt.Println(CalcularSoma(valores))
fmt.Println(CalcularProduto(valores))
}
Paraestasérie,oprogramaimprimiráosvalores7 4e1182720paraasoma
eoproduto,respectivamente.
Repare,porém,comootrecho func(n, m int) intaparecetrêsve-
zesecausaconfusãoespecialmentequandoutilizadocomoargumentonade-
finiçãodafunção Agregar().
V a m o sextrairestadeclaraçãocomumparaumtipodefunçãochamado
Agregadora:
type Agregadora func(n, m int) int
V e j acomoadefinição deumtipodefunção não émuitodiferenteda
definiçãodeoutrostipos.
Naprática,um fu nct io ntypeémuitosemelhanteaumainterface:qual-
querfunção querecebadoisargumentosdotipo interetorneumvalor
intsatisfazaassinaturadefinidapelotipo Agregadorae,portanto,pode
serutilizadacomoumafunçãoagregadora.
Agoravamosmodificarafunção Agregar()parautilizaronovotipo
nadeclaraçãodalistadeargumentos:
func Agregar(
valores []int,
valorInicial int,
fn Agregadora,
) int {
agregado := valorInicial
98

## Página 113

CasadoCódigo Capítulo6. Funções
for _, v := range valores {
agregado = fn(v, agregado)
}
return agregado
}
Assimtornamosmuitomaislegíveladefinição dafunção Agregar()
e especialmente do argumento fn. Alémdisso, CalcularSoma() e
CalcularProduto()nãoprecisamsofrernenhumaalteração,poisasfun-
ções queambaspassamcomoargumentopara Agregar()satisfazemim-
plicitamenteaassinaturade Agregadora.
6.9 Servindo HTTP através de funções
Nocapítulo5.7vimosumexemplodousodeinterfacesnaprópriabiblioteca
padrão dalinguagemGo. Agoravamosrecorrernovamenteaelaparade-
monstrarousodefunções querecebemoutrascomoargumentoatravésde
um fu nct io ntype.Paraissovamosutilizarumdosrecursosmaisimportantes
dabibliotecapadrão:escreverumservidorHTTP.
AmaiorpartedosrecursosdisponíveisparaaescritadeservidoresHTTP
podeserencontradanopacote net/http(http://golang.org/pkg/net/http/)
.
Nossoservidorserábastantesimpleseapenasretornaráadataatualdo
sistema.
AformamaisfácildeescreveresteservidoremGoéatravésdafunção
http.HandleFunc(),querecebedoisargumentos:primeiro,uma string
definindoopadrãodaURLatendidaporesteserviço,eporúltimo,umafun-
çãodotipo http.HandlerFunc,quedefineaseguinteassinatura:
type http.HandlerFunc func(http.ResponseWriter, *http.Request)
Issosignificaquequalquerfunçãoquepossuaamesmaassinaturapode
serusadacomoumservidorHTTP!
99

## Página 114

6.9. ServindoHTTPatravésdefunções CasadoCódigo
A implementação do serviço ébastantesimples. Crie um novoar-
quivochamado cap6-servidor-tempo/servidor_tempo.gocomo
conteúdo:
package main
import (
"fmt"
"net/http"
"time"
)
func main() {
http.HandleFunc(
"/tempo",
func(w http.ResponseWriter, r *http.Request) {
fmt.Fprintf(w, "%s",
time.Now().Format("2006-01-02 15:04:05"))
})
http.ListenAndServe(":8080", nil)
}
Émuitoimportantenotarque,naprática,umservidorHTTPemGoéum
programacomooutroqualquer,portanto,precisadefinirumpacote main
ondeafunção main()éopontodepartida.Sendoassim, main()éolugar
idealparaconfigurarmosnossoserviço.
Inicialmente,utilizamosafunção http.HandleFunc()pararegistrá-
lo,especificandoqueeleatenderárequisições recebidasnaURL /tempo.
Em seguida, especificamos uma função anônima que satisfaz a
assinatura definida pelo tipo http.HandlerFunc, recebendo um
http.ResponseWritereumponteiroparaumobjeto http.Request.
Aimplementaçãodestafunçãoapresentaalgumasnovidades:utilizamos
afunção fmt.Fprintf()paraimprimiradataehoraatualcomorespostaà
requisiçãoHTTP.Estafunçãoémuitosimilarà fmt.Printf,quejáusamos
muitasvezesatéaqui.Adiferençaéque Printf()escrevenasaídapadrão,
enquanto Fprintf()recebecomoprimeiroargumentoumvalordotipo
100

## Página 115

CasadoCódigo Capítulo6. Funções
io.Writer,ondeasaídaseráescrita–nestecaso,utilizamosovalorrece-
bidoem w.Estevaloré,naverdade,dotipo http.ResponseWriter,mas
satisfazainterface io.Writere,portanto,podeserutilizadonestecontexto.
Paraformataradataehoraatual,utilizamosométodo Format()de-
finidopelotipo time.Time. Estemétodorecebecomoargumentouma
stringquedefineoformatodesejado.Adataescolhidaparadefinirofor-
matononossoexemplonãoéaleatória:ométodoFormat()utilizaestadata
preestabelecida(2dejaneirode2006,15:04:05)paraanalisarereconhecero
formatorecebido.
Porfim,utilizamosafunção http.ListenAndServe()paraespecifi-
carqueoservidordeveráaceitarconexões naporta8080. Estafunçãoini-
ciaumservidorHTTP,bloqueiaaexecução doprogramaedelegaasco-
nexões recebidasnoendereçodefinidoparaosserviçosregistrados. Ose-
gundoargumentoéumvalordotipo http.Handlere,nestecaso,foi
especificadocomo nilpoisjáregistramosumserviçoatravésdométodo
http.HandleFunc().
Podemosexecutaroservidordamesmaformaqueexecutamostodosos
outrosprogramas:
$ go run cap6-servidor-tempo/servidor_tempo.go
Casooservidortenhasidoiniciadocomsucesso,nenhumasaídaserá
impressa. Paratestaroserviço,abraseunavegadoredirecione-oàURL
http://localhost:8080/tempo.Oresultadoseráumapáginasimilaràdemons-
tradaaseguir,comadataeahoraatuais:
101

## Página 116

6.9. ServindoHTTPatravésdefunções CasadoCódigo
Figura6.1:exemplodedataehoraretornadospeloservidordetempo
Nestecapítulo,vimostodososrecursosdisponíveisparaacriaçãoema-
nipulaçãodefunções, incluindofunções anônimas, c l o s u r e sefunções depri-
meiraclasse.
T a m b é mvimoscomocriarumservidorHTTPsimplesutilizandouma
funçãoparaatenderàsrequisições.
Nocapítulo7,veremososrecursosparaaescritadeprogramasconcor-
rentesemGo.
102

## Página 117

Capítulo7
Concorrênciacom goroutinese
channels
“ D onot communicate b ysharing memory; instead, s h a r ememory b y
communicating. ”
–EffectiveGo
Programação concorrenteéumtemabastantedelicadoecomplexo.Se
vocêjáescreveuprogramasquedependiamdemúltiplasthread soumúltiplos
processossabequeéumatarefaqueexigemuitaatençãoepaciência,especi-
almentequandoénecessáriocompartilharestadoentreasdiferenteslinhas
deexecução.
Amaiorpartedaslinguagensdeprogramaçãoimplementa thread sdeal-
gumaforma,sejaatravésdeumescalonadorprópriooudelegandoocontrole
paraosistemaoperacionalhospedeiro.

## Página 118

7.1. Goroutines CasadoCódigo
Ocompartilhamentodeestadoemumprograma multi-threadedénor-
malmenteimplementadoatravésdevariáveisglobaise/oucompartilhadase
exigealgummecanismodetravaousemáforoparaevitarcondições decor-
rida(race conditions).
Paraevitarestetipodeproblema,Goimplementaummodelodeconcor-
rênciabaseadoem goroutinesquesecomunicamatravésde channels,sendo
queopróprioambientedeexecuçãogarantequeapenasuma goroutineacesse
um channelemumdeterminadomomento.
Existeumdocumento(eminglês)nositeoficialdalinguagemchamado
E ff e c t i v eGo(http://golang.org/doc/effective_go.html)quedescreveumasé-
riedeboaspráticasparagarantiraescritadeprogramascomcódigolimpo
eidiomáticoemGo.Estedocumentocontémadefiniçãodeumsloganque
resumeaideologiaportrásdomodelodeconcorrênciaescolhido: Do not
communicate b y sharing memory; instead, s h a r ememory b y communicating
(nãocomuniqueatravésdememóriacompartilhada;emvezdisso,comparti-
lhememóriaatravésdacomunicação).
Naspróximasseções veremoscomoatingiresteobjetivo.
7 . 1 Goroutines
U m agoroutineéumtipodeprocessoextremamenteleve. Naprática,uma
goroutineémuitosimilaraumathread.Noentanto,goroutinessãogeren-
ciadaspeloambientedeexecuçãodalinguagem,quedecidequandoecomo
associá-lasathreadsdosistemaoperacional.
Parainiciarumagoroutine,utilizamosapalavra-chave goseguidade
umachamadadefunção.Oambientedeexecuçãoiráexecutarafunçãocha-
madasembloquearalinhadeexecuçãoprincipal.
Considereaseguintefunção imprimir(),querecebeumnúmeroin-
teiroeoimprimetrêsvezescomumespaçode200milissegundosentrecada
impressão:
func imprimir(n int) {
for i := 0; i < 3; i++ {
fmt.Printf("%d ", n)
time.Sleep(200 * time.Millisecond)
104

## Página 119

CasadoCódigo Capítulo7 .Concorrênciacom goroutinese channels
}
}
Agora considere a seguinte função main() que chama a função
imprimir()duasvezescomnúmerosdiferentes:
func main() {
imprimir(2)
imprimir(3)
}
Executandoestafunção main()obteríamos 2 2 2 3 3 3comore-
sultado.
V a m o salteraraprimeirachamadaparaquesejaexecutadaemumago-
routine:
func main() {
go imprimir(2)
imprimir(3)
}
Atravésdasimplesadiçãodapalavra-chave go,estanovaversãoexecuta
asduaschamadasdeformaconcorrenteeproduzumresultadocompleta-
mentediferente: 3 2 3 2 3 2.
Éimportanteressaltarqueasgoroutinesdependemdafunção main()
paraquecontinuemsuaexecução.Emoutraspalavras,asgoroutines morrem
quandoafunção main()finalizasuaexecução.
Podemosprovarestefatocomosimplesprogramaaseguir,queiniciauma
goroutinequedormepor5segundos,enquantoafunção main()dormepor
apenas3segundos:
func dormir() {
fmt.Println("Goroutine dormindo por 5 segundos...")
time.Sleep(5 * time.Second)
fmt.Println("Goroutine finalizada.")
}
func main() {
105

## Página 120

7.2. Channels CasadoCódigo
go dormir()
fmt.Println("Main dormindo por 3 segundos...")
time.Sleep(3 * time.Second)
fmt.Println("Main finalizada.")
}
Oresultadodaexecuçãodesteprogramaseriaoseguinte:
Main dormindo por 3 segundos...
Goroutine dormindo por 5 segundos...
Main finalizada.
Agoroutineexecutandoafunção dormir()nuncatermina,poisafun-
ção main()terminasuaexecuçãoanteseoprogramaéfinalizado.
7 . 2 Channels
Acapacidadedeexecutardiferentesgoroutinesconcorrentementeémuito
importanteeabrediversaspossibilidadesparaasolução deproblemasque
exigemaltaperformanceemelhoreficiêncianousoderecursosdeprocessa-
mento.
Entretanto,émuitoraraasituaçãoemqueváriasgoroutinessãodispara-
dasindependentemente,semquehajacomunicaçãoentreelas.Os channels
foramcriadoscomoumaabstraçãoparaviabilizarestacomunicação.
U mchanneléumcanalqueconduzinformações deumdeterminadotipo
–qualquertipoválidoemGo.
Paracriarumnovocanal,utilizamosafunção make(). Porexemplo,
paracriarumcanalcapazdetrafegarvaloresdotipo int,podemosutilizar
oseguintecomando:
c := make(chan int)
Parainteragircomumcanal,utilizamosooperador <-(conhecidocomo
a r r o woperator,ouoperadorseta).Aposiçãodocanalemrelaçãoàsetaindica
adireção dofluxodacomunicação. Porexemplo,paraenviarvalores int
paraocanal c,utilizamosaseguintenotação:
106

## Página 121

CasadoCódigo Capítulo7 .Concorrênciacom goroutinese channels
c <- 33
Eparareceberumvalorenviadoparaocanal c:
valor := <-c
Aseguirtemosumexemplosimplesquecombinatodosospassosanteri-
oresparademonstrarofluxodecomunicaçãocompleto:
func main() {
c := make(chan int)
go produzir(c)
valor := <-c
fmt.Println(valor)
}
func produzir(c chan int) {
c <- 33
}
Inicialmentecriamosumcanalparatrafegarvaloresdotipo int.
Em seguida, disparamos uma goroutine executando a função
produzir(), que recebe um canal como argumento e simplesmente
enviaumnúmerointeiroparaocanalrecebido.
Porpadrão,operaçõesdeenvioerecebimentoemumcanalbloqueiamaté
queooutroladoestejapronto.Estefatopermitequeaprópriacomunicação
entreduasgoroutinesgarantaasincronização entreelas,semquenenhum
mecanismodetravassejanecessário.
Porestemotivo,apróximalinhadafunção main()–querecebeumva-
lordocanal–farácomquealinhadeexecuçãoprincipalfiquebloqueadaaté
quealgumvalorsejaenviadoparaocanal c.Assimqueovalor33forenviado
pelafunção produzir(),alinhadeexecuçãoprincipalseráentãodesblo-
queada,ovalor33seráconsumido,atribuídoàvariávelvaloreimpressono
console.
107

## Página 122

7.3.Buffers CasadoCódigo
7 . 3 Buffers
Canaispodemsercriadoscomumbuffer.Porexemplo:
c := make(chan int, 5)
Ocanal cfoicriadocomumbufferdetamanho5.Istoquerdizerqueope-
rações deenvionãoserãobloqueadasenquantoobuffernãoestivercheio,e
operaçõesderecebimentonãoserãobloqueadasenquantoobuffernãoestiver
vazio.Vejamosmaisumexemploparafacilitaroentendimento:
func main() {
c := make(chan int, 3)
go produzir(c)
fmt.Println(<-c, <-c, <-c, <-c)
}
func produzir(c chan int) {
c <- 1
c <- 2
c <- 3
}
Criamosumcanalcombufferdetamanho3eimediatamentedisparamos
umagoroutinequeenviatrêsvalorespelocanalcriado. Emseguida,rece-
bemosquatrovaloresdocanaleosimprimimosnoconsole. Qualseriao
resultadodesseprograma?
fatal error: all goroutines are asleep - deadlock!
Causamosum deadlock! Agoroutineprodutoraencerrousuaexecução
logoapósproduzirostrêsvalores;porcausadobuffer,nenhumadasopera-
ções deenviofezcomqueaexecuçãofossebloqueada.Noentanto,aoten-
tarmosreceberumquartovalor–quenuncafoiproduzido–pelocanal,a
linhaprincipalficoubloqueada.Oambientedeexecuçãodetectouo deadlock
eencerrouaexecuçãodoprogramacomumerro.
Oprodutorprecisaindicardealgumaformaquenão enviarámaisne-
nhumvalorpelocanal.Paraissoexisteafunçãoembutida close().V a m o s
108

## Página 123

CasadoCódigo Capítulo7 .Concorrênciacom goroutinese channels
alterarafunção produzir()parafecharocanalapósproduzirostrêsva-
lores:
func produzir(c chan int) {
c <- 1
c <- 2
c <- 3
close(c)
}
Émuitoimportantequeoladoprodutorfecheocanalsemprequepossível
quandonãohouvermaisvaloresaseremproduzidos.
Agora,precisamostambémdetectarqueocanalfoifechadodoladodo
consumidor.
Ooperador <-retornasempredoisvalores:ovalorlidoeumvalor bool
indicandoseovalorfoilidocomsucessoounão; estevalorserá false
quandoocanaltiversidofechado.
A t éomomento,ignoramososegundovalorretornado. V a m o salterar
tambémafunção main()parachecá-lo:
func main() {
c := make(chan int, 3)
go produzir(c)
for {
valor, ok := <-c
if ok {
fmt.Println(valor)
} else {
break
}
}
}
Qualseriaoresultadodoprogramaagora?
1
2
3
109

## Página 124

7.3.Buffers CasadoCódigo
Resolvemoso deadlock!Porém,oprocessodechecarsempreseocanal
continuaabertoounãoébastantetedioso.
Felizmente,háumaoutraformadefazê-lo:podemosutilizaroopera-
dor rangeparalervaloresdeumcanalconformeelesforemsendoproduzi-
dos.V a m o scriarumexemploparautilizá-lo.Emumnovoarquivochamado
cap7-buffers/buffers.go,adicioneafunção produzir()apresen-
tadanoexemploanterior:
package main
import "fmt"
func produzir(c chan int) {
c <- 1
c <- 2
c <- 3
close(c)
}
Emseguida,crieaseguitefunção main(),parecidacomadoexemplo
anterior,porémutilizandoooperador range:
func main() {
c := make(chan int, 3)
go produzir(c)
for valor := range c {
fmt.Println(valor)
}
}
Ocódigoresultanteémenoremuitomaisclaro.
Executeoprogramaevejaqueoresultadoéidêntico:
$ go run cap7-buffers/buffers.go
1
2
3
110

## Página 125

CasadoCódigo Capítulo7 .Concorrênciacom goroutinese channels
7 . 4 Controlando a direção d ofluxo
Porpadrão,acomunicaçãoemumcanalébidirecional.Algumasvezes,po-
rém,desejamoscontrolaradireçãodofluxoquandopassamosumcanalcomo
argumentoparaoutrafunção,ouquandotemosumafunçãoqueretorneum
canal.
Considerando ainda o exemplo anterior, vamos alterar a função
produzir()paradefiniradireçãodacomunicação:
func produzir(c chan<- int) {
// ...
}
Repareque,aoreceberocanalcomoargumento,definimosqueafunção
poderásomenteenviarvaloresparaocanal( chan<-).Destaforma,casoa
funçãotenterecebervalorespelomesmocanal,causaráoseguinteerro:
invalid operation: <-c (receive from send-only type chan<- int)
Demaneirasimilar,podemosdefinirumcanal read-only(somentelei-
tura):
func consumir(c <-chan int) {
// ...
}
V a l eressaltarque,comoGoéumalinguagemcomtiposforteseoscanais
sãotipados,esseerroécausadoemtempode compilação.
7 . 5 Select
Émuitocomumencontrarumcenárioemqueumagoroutineprecisainte-
ragircommúltiploscanaisdecomunicação.Porexemplo,umafunçãopode
disparargoroutinesqueescrevemvaloresemcanaisdiferentes,eafunçãoori-
ginaldependedosvaloresdetodosestescanaisparaproduzirseuresultado
final.
Paraevitarqueaexecuçãodeumagoroutinesejabloqueadaesperando
poroperações emalgumdoscanaisdosquaiseladepende,Goforneceum
111

## Página 126

7.5. Select CasadoCódigo
comandochamado select,queémuitosemelhanteao switch.Suaforma
geralé:
select {
case v1 := <-canal1:
// ...
case v2 := <-canal2:
// ...
default:
// ...
}
Casoexistaalgumvaloraserlidono canal1,eleseráatribuídoàvariável
v1eoblocoassociadoaoprimeirocomando caseseráexecutado.Casocon-
trário,o canal2seráchecadoporvaloresrecebidose,emcasopositivo,seu
valorseráatribuídoàvariávelv2eoblocoassociadoaosegundocomando
caseseráexecutado.Senenhumdoscanaisespecificadospossuíremvalores
prontosparaseremlidos,obloco defaultseráexecutado.
U m adasformaismaiscomunsdousodo selectédentrodeumlaço
quecontrolaacomunicaçãocomasgoroutines.V a m o sescreverumprograma
que,dadaumalistadenúmeros,separa-osemduaslistasdistintasdeparese
ímpares.Oalgoritmoébastantetrivial,porém,vamosimplementá-lousando
umagoroutineecanaisseparadosparaenviarnúmerospareseímpares.V a -
mosutilizartambémumterceirocanalparaindicarofinaldaexecução da
goroutine.
Primeiro,vamoscriarafunção separar(),querecebealistadenúme-
rosetrêscanais: i, ppe pronto,todosunidirecionais:
func separar(nums []int, i, p chan<- int, pronto chan<- bool) {
for _, n := range nums {
if n%2 == 0 {
p <- n
} else {
i <- n
}
}
pronto <- true
}
112

## Página 127

CasadoCódigo Capítulo7 .Concorrênciacom goroutinese channels
Paracadanúmeropresenteem nums,verificamosseépar(divisívelpor
2–n%2 == 0)e,emcasopositivo,enviamosonúmeroparaocanal p;
casosejaumnúmeroímpar,eleseráenviadoparaocanal i. Aofinalda
iteração,enviamosovalor trueparaocanal pronto,indicandoofimdo
processamento.
V a m o sagoraseguirafunção main()passoapasso.Inicialmente,cria-
mososcanaisealistadenúmeros:
i, p, pronto := make(chan int), make(chan int)
pronto := make(chan bool)
nums := []int{1, 23, 42, 5, 8, 6, 7, 4, 99, 100}
Emseguida,disparamosuma goroutineparasepararosnúmeros:
go separar(nums, i, p, pronto)
Comtudopreparadoeagoroutinejáseparandoosvalores,precisamos
coletarosresultadosenviadosparacadacanal. Primeiro,criamosasduas
listaseumavariávelparacontrolarolaço:
var impares, pares []int
fim := false
Agoraprecisamospopularaslistas imparese paresdeacordocoma
separaçãoqueestásendofeitanagoroutine.Paraisso,criamosumlaçoque
executaráatéqueovalordavariável fimsejaverdadeiro,eutilizamosum
comando selectparalerosvaloresdecadaumdoscanais:
for !fim {
select {
case n := <-i:
impares = append(impares, n)
case n := <-p:
pares = append(pares, n)
case fim = <-pronto:
}
}
113

## Página 128

7.5. Select CasadoCódigo
Reparenaúltimacláusulacase:elasóseráexecutadaquandoagorou-
tineenviarovalor trueparaocanal prontoe,então,avariávelfimas-
sumiráovalor trueeacondição desaídadolaçoseráatendida. Utilizar
umcanalparasincronizargoroutinesqueenvolvemmúltiploscanaiséuma
técnicamuitocomumemGo.
Porfim,imprimimososvaloresseparadospresentesnaslistas impares
e pares:
fmt.Printf("Ímpares: %v | Pares: %v\n", impares, pares)
Aseguirpodemosverocódigocompletodafunção main():
func main() {
i, p := make(chan int), make(chan int)
pronto := make(chan bool)
nums := []int{1, 23, 42, 5, 8, 6, 7, 4, 99, 100}
go separar(nums, i, p, pronto)
var impares, pares []int
fim := false
for !fim {
select {
case n := <-i:
impares = append(impares, n)
case n := <-p:
pares = append(pares, n)
case fim = <-pronto:
}
}
fmt.Printf("Ímpares: %v | Pares: %v\n", impares, pares)
}
Executandoesteprograma,obteríamososeguinteresultado:
$ go run select.go
Ímpares: [1 23 5 7 99] | Pares: [42 8 6 4 100]
114

## Página 129

CasadoCódigo Capítulo7 .Concorrênciacom goroutinese channels
7 . 6 Temporizadores e timeouts
Controlaraexecuçãodemúltiplasgoroutinesatravésdeum selectéumatéc-
nicabastantesimplesemuitoutilizadaemGo.Porém,existemcasosemque
aexecuçãodeumadeterminadatarefaprecisaaconteceremumperíodoli-
mitadodetempo.
Opacote timeforneceumafunção After()queajudaaresolverestes
casos.Suaassinaturaé:
func After(d Duration) <-chan Time
Reparequeestafunçãoconvenientementeretornaumcanal.Assim,po-
demosfacilmenteutilizá-ladentrodeum selectparacontrolarotempode
execuçãodeumagoroutine,etomaralgumaatitudecasoelanãoproduzare-
sultadosdentrodotempoesperado.
V a m o ssimular esta situação com uma goroutine que simples-
mente dorme por 5 segundos e sinaliza o final de sua execução en-
viando o valor true para um canal. Crie um arquivo chamado
cap7-timeout/timeout.go edefinaumanovafunção executar()
comocódigodasimulação:
package main
import (
"fmt"
"time"
)
func executar(c chan<- bool) {
time.Sleep(5 * time.Second)
c <- true
}
Crieentãooesqueletodafunção main(),cujoconteúdoseráapresen-
tadoemparteslogoemseguida:
func main() {
// ...
}
115

## Página 130

7.6.Temporizadorese timeouts CasadoCódigo
Primeiramente,devemoscriarumcanale,então,dispararumagoroutine
executandoatarefademorada:
c := make(chan bool, 1)
go executar(c)
fmt.Println("Esperando...")
Suponhaqueotempomáximoaceitávelparaaexecuçãodestatarefaseja
de2segundos. V a m o simplementarummecanismode timeoututilizando
time.After()dentrodeum selectenquantoesperamosqueatarefaseja
finalizada:
fim := false
for !fim {
select {
case fim = <-c:
fmt.Println("Fim!")
case <-time.After(2 * time.Second):
fmt.Println("Timeout!")
fim = true
}
}
Executandoesteprogramateremososeguinteresultado:
$ go run cap7-timeout/timeout.go
Esperando...
Timeout!
Simples,não?
Sealterarmosafunção executar()paradormirporapenas1segundo
emvezde5,teremoscomoresultado:
$ go run cap7-timeout/timeout.go
Esperando...
Fim!
116

## Página 131

CasadoCódigo Capítulo7 .Concorrênciacom goroutinese channels
7 . 7 Sincronizando múltiplas goroutines
Anteriormente,vimosumexemplodecomoesperarqueumagoroutinefi-
nalizesuaexecuçãoatravésdautilizaçãodeumcanal. Noentanto,quando
precisamosesperarpelaexecuçãodemúltiplasgoroutines,controlarmanual-
mentequantasdelasjáterminarampodesetornarumatarefasujeitaafalhas.
Goforneceumtipochamado WaitGroup,presentenopacote sync,que
tornaestatarefabemmaissimples.Paravê-loemação,crieumarquivocha-
mado cap7-sincronizador/sincronizador.go,declarandoopacote
syncentresuasdependências:
package main
import (
"fmt"
"math/rand"
"sync"
"time"
)
Crietambémafunção main()comoconteúdo:
func main() {
inicio := time.Now()
rand.Seed(inicio.UnixNano())
var controle sync.WaitGroup
for i := 0; i < 5; i++ {
controle.Add(1)
go executar(&controle)
}
controle.Wait()
fmt.Printf("Finalizado em %s.\n", time.Since(inicio))
}
Inicialmente,armazenamoso timestampatualeconfiguramosasemente
117

## Página 132

7.7.Sincronizandomúltiplasgoroutines CasadoCódigo
paraageraçãodenúmerosaleatórios,garantindoquenúmerosdiferentesse-
jamgeradosacadaexecução.
Em seguida, criamos uma variávelchamada controle do tipo
sync.WaitGroup queutilizaremosparasincronizaraexecução dasgo-
routines. Antes de disparar cada goroutine, chamamos o método
controle.Add(1),indicandoqueumanovagoroutinedeverásersincro-
nizada,eentãoiniciamossuaexecuçãochamandoafunção executar().
Repare que passamos como argumentoum ponteiropara a variável
controle. ComoosargumentosemGosão passadoscomocópias,éim-
portantequeutilizemosumponteironestecaso,poisomesmo WaitGroup
deveserutilizadoportodasasgoroutines.
Porfim,chamamosométodo controle.Wait(),quenestecasoirá
bloquearaexecuçãodafunção main()atéquetodasasgoroutinestenham
finalizado.Quandoistoacontecer,ométodo Wait()iráretornar,eentão
imprimiremosotempopercorridoentreoinícioeofimdaexecuçãodopro-
grama.
Agora,vamosadicionarocódigodafunção executar():
func executar(controle *sync.WaitGroup) {
defer controle.Done()
duracao := time.Duration(1+rand.Intn(5)) * time.Second
fmt.Printf("Dormindo por %s...\n", duracao)
time.Sleep(duracao)
}
Primeiro,garantimosqueométodo controle.Done()seráchamado
quandoafunção terminarsuaexecução, notificandoo WaitGroupdeste
fato. Emseguida, criamosumvalordotipo time.Duration baseado
emumnúmeroaleatórioentre1e5segundos. Então chamamosafunção
time.Sleep()paraqueagoroutineatualdurmapeloperíodoespecificado.
U mexemplodaexecuçãodesteprograma:
$ go run cap7-sincronizador/sincronizador.go
Dormindo por 5s...
Dormindo por 4s...
118

## Página 133

CasadoCódigo Capítulo7 .Concorrênciacom goroutinese channels
Dormindo por 1s...
Dormindo por 4s...
Dormindo por 3s...
Finalizado em 5.001185837s.
7 . 8 Concorrência , paralelismo eGOMAXPROCS
Todososrecursosapresentadosnestecapítulofazempartedosuportenativo
deGoparaprogramasconcorrentes.Porém,éimportanteressaltarquecon-
corrêncianãoéparalelismo,enenhumdestesrecursosfarácomqueumpro-
gramaexecuteemparaleloutilizandotodososCPUsdisponíveisnoambiente
deexecução.
Algunsprogramas,noentanto,realizamoperações queexigemumpoder
deprocessamentomaiorepodemsebeneficiardautilização dosmúltiplos
coresdisponíveis.
Porpadrão,o runtimedalinguagemGoexecutaumaúnicagoroutineem
umdadomomento,masdisponibilizaumaformademodificarestaconfigu-
ração.
Porexemplo,aoiniciaraexecuçãodeumprograma,pode-seespecificar
avariáveldeambiente GOMAXPROCS:
$ GOMAXPROCS=2 go run paralelo.go
Épossíveltambémconfigurarestevalorprogramaticamenteatravésdo
pacote runtime:
func main() {
runtime.GOMAXPROCS(runtime.NumCPU())
// ...
}
Ocódigoanteriorinstruio runtimeautilizartodosos coresdisponíveis.
Aseguirveremosumexemplodeprogramaquesebeneficiadousode
múltiploscores.
package main
119

## Página 134

7.8.Concorrência,paralelismoeGOMAXPROCS CasadoCódigo
import (
"fmt"
"math"
"sync"
"time"
)
func calcular(base float64, controle *sync.WaitGroup) {
defer controle.Done()
n := 0.0
for i := 0; i < 100000000; i++ {
n += base / math.Pi * math.Sin(2)
}
fmt.Println(n)
}
func main() {
inicio := time.Now()
var controle sync.WaitGroup
controle.Add(3)
go calcular(9.37, &controle)
go calcular(6.94, &controle)
go calcular(42.57, &controle)
controle.Wait()
fmt.Printf("Finalizado em %s.\n", time.Since(inicio))
}
Ocódigoébastantesimpleseapenasdispara3goroutinesquerealizam
algumtipodecálculoqueexigealtousodaCPU.
Osresultadosaseguirforamcolhidosemumcomputadorcom4cores.
Inicialmente,umexemplodeexecuçãoutilizandoaconfiguraçãopadrãodo
runtime:
$ go run paralelo.go
2.712037442294368e+08
120

## Página 135

CasadoCódigo Capítulo7 .Concorrênciacom goroutinese channels
2.0087022191177934e+08
1.2321391006719112e+09
Finalizado em 4.515132372s.
Emseguida,instruímoso runtimeautilizardois cores:
$ GOMAXPROCS=2 go run paralelo.go
2.0087022191177934e+08
2.712037442294368e+08
1.2321391006719112e+09
Finalizado em 2.419171346s.
V e j aqueotempodeexecuçãocaiuquasepelametade! Porfim,vamos
instruiro runtimeautilizar3 cores.Éesperadoqueestaconfiguraçãosejaa
ideal,jáquetemosexatamente3goroutinesexecutando.Oresultado:
$ GOMAXPROCS=3 go run paralelo.go
2.712037442294368e+08
2.0087022191177934e+08
1.2321391006719112e+09
Finalizado em 2.165083253s.
Agorativemosumganhomenor,masaindasignificativo.
Éimportanteressaltarqueesterecursodeveserutilizadocombastante
cautelaepodeproduzirresultadosmuitodiferentesdependendodanatureza
doprogramaemquestão. Érecomendávelquecadacasosejaestudadocom
cuidado.
7 . 9 Recapitulando
Estecapítuloapresentouosprincipaisconceitosdeconcorrênciadisponíveis
emGo,dandoumfocoespecialagoroutinesechannels.Noentanto,hámuito
aserexploradosobreesseassunto.
Programaçãoconcorrenteéumtemadealtacomplexidade.Omodelode
concorrênciadalinguagemfoicriadocomoobjetivodetornaraescritade
programasconcorrentesumatarefamaisfácil.
Crieseusprópriosprogramasutilizandoosrecursosaprendidos,modifi-
queosexemplosapresentadosepratiquebastante.Assim,vocêabsorveráos
conceitosmaisfacilmente.
121

## Página 137

Capítulo8
Mã onamassa:encurtadorde
URLs
NossopasseiopelosprincipaisrecursosdalinguagemGochegouaofim.Para
consolidartodooconhecimentoacumuladoatéaqui,chegouahoradecolo-
caramãonamassaedesenvolverumaaplicaçãoreal!
V a m o sdesenvolverumservidorHTTPqueprovêumaAPI(application
programminginterface)paracriarURLscurtaseredirecioná-lasparaasURLs
originais.Paraisso,utilizaremososrecursosdopacote net/httpeimple-
mentaremosumrepositórioemmemória.

## Página 138

8.1.Estruturadoprojeto CasadoCódigo
8.1 Estrutura d op r o j e t o
A t éagora,todososexemplosapresentadosdefiniamumúnicopacote main.
Projetosmaioresemaiscomplexos,porém,necessitamdepacotesadicionais
paraorganizarmelhorocódigo.
Nocapítulo1.2,aprendemoscomoconfigurarumaáreadetrabalhoatra-
vésdavariáveldeambiente $GOPATH.Estepassoéespecialmenteimportante
paraqueprojetosquedefinemmúltiplospacotespossamsercorretamente
compilados.
T o d oprojetoemGosegueumaconvenção semelhante: aestruturade
diretórios epacotesédefinidadeacordocomocaminhodorepositório
ondeocódigo reside. Porexemplo,projetoshospedadosnoGitHubin-
cluem github.com/usuario/projeto/nome-do-pacotenocaminho
completodospacotes.Veremosaimportânciadestaconvençãonocapítulo
9.
Considerandoqueonossoprojetoseráhospedadoemhttps://github.
com/caiofilipini/encurtador,aseguinteestruturadediretóriosdeverásercri-
adaem $GOPATH/src:
Figura8.1:Estruturadoprojeto
V a m o scomeçarpeladefiniçãodoservidorpropriamentedito.
8.2 Criando o servidor
Oservidorserádefinidonoarquivo servidor.goeseráopontodepartida
danossaaplicação. Nestearquivo,definiremosafunção main()queserá
responsávelporconfigurareiniciaroservidorHTTP.
Primeiro,vamosdefiniropacote maineespecificarasdependências:
124

## Página 139

CasadoCódigo Capítulo8. Mãonamassa:encurtadordeURLs
package main
import (
"fmt"
"log"
"net/http"
"strings"
"github.com/caiofilipini/encurtador/url"
)
Nenhumagrandenovidadeatéaqui,excetopelocaminhodopacotein-
terno url.
Precisamosdeumavariávelparaarmazenaraportaondeoserviçoirá
aceitarnovasconexões, etambémumavariávelpararepresentaraURLbase
doserviço.Comoelasserãoutilizadasemmaisdeumlugar,vamoscriá-las
noníveldopacoteparaquesejamacessíveisportodasasfunções definidas
nele:
var (
porta int
urlBase string
)
Agoraprecisamosinicializá-las.Godisponibilizaummecanismopadrão
parainicializaçãodevariáveiserecursosutilizadosemumpacote:afunção
init().U mpacotepodedefinirváriasfunções init()diferentes(prática
comum,casoocódigodopacotesejadivididoemmúltiplosarquivos,masa
ordemdechamadaéindefinida).Nonossocaso,precisamosdeumaúnica:
func init() {
porta = 8888
urlBase = fmt.Sprintf("http://localhost:%d", porta)
}
Echegamosfinalmenteàdefiniçãodafunção main(),ondeconfigura-
mosasrotasparaonossoservidorHTTP:
125

## Página 140

8.3.CriandoURLscurtas CasadoCódigo
func main() {
http.HandleFunc("/api/encurtar", Encurtador)
http.HandleFunc("/r/", Redirecionador)
log.Fatal(http.ListenAndServe(
fmt.Sprintf(":%d", porta), nil))
}
Definimosduasrotasparaonossoservidor:
•/api/encurtar:responsávelporreceberumaURL,criarumidenti-
ficadorcurtoeretornaraURLcurta;
•/r/<id-curto>: responsávelporreceberumidentificadorcurtoe
redirecionarparaaURLoriginal.
Configuramosasduasrotasutilizandoafunção http.HandleFunc().
Arota /api/encurtarserátratadapelafunção Encurtador,enquantoa
função Redirecionadorcuidarádasrequisições recebidasem /r/.
Aseguirveremosemdetalhescadaumadestasfunções. Aimplementa-
çãodopacoteinterno urlseráapresentadaposteriormente.Porenquanto,
veremossomenteadefinição dotipo Url,queseráusadonosexemplosa
seguir:
type Url struct {
Id string
Criacao time.Time
Destino string
}
Estetipoéuma structsimples,contendoumcampoparaarmazenaro
identificadorcurto( Id),adataehoradacriaçãodaURLcurta( Criacao),
eaURLoriginal( Destino).
8.3 Criando URLs curtas
A função Encurtador() irátratar as requisições recebidas em
/api/encurtar.
126

## Página 141

CasadoCódigo Capítulo8. Mãonamassa:encurtadordeURLs
Como esta função será registrada através do método
http.HandleFunc(), ela precisa ser do tipo http.HandlerFunc.
Portanto,suaassinaturaé:
func Encurtador(w http.ResponseWriter, r *http.Request)
ComoestamosimplementandoumaAPIsobreHTTP,tentaremosseguir
opadrão arquiteturalREST(Representational State Transfer[1]). Assim,o
primeiropassoéverificarseestamosrecebendoumarequisiçãodotipoPOST
e,casocontrário,retornaremosumerroHTTP405(Method N o tAllowed),
indicandonocabeçalho Allowqueesteserviçoaceitaapenasrequisições
comométodoPOST:
if r.Method != "POST" {
responderCom(w, http.StatusMethodNotAllowed, Headers{
"Allow": "POST",
})
return
}
Para formatar a resposta incluindo o cabeçalho Allow, chama-
mos uma função utilitária responderCom() que recebe o objeto
http.ResponseWriter,ocódigoderespostadesejadoeummapadeca-
beçalhosdotipo Headers. Estetipoéapenasum type a l i a sparaotipo
map[string]stringefoicriadoparatornarocódigomaisclaro.Suade-
finiçãoéaseguinte:
type Headers map[string]string
A função responderCom() itera sobre os cabeçalhos
recebidos, configurando cada um deles através do método
http.ResponseWriter.Header().Set()antesde,finalmente,ajustar
o código de resposta chamando o método WriteHeader(), também
disponívelparaobjetosdotipo http.ResponseWriter:
func responderCom(
w http.ResponseWriter,
status int,
127

## Página 142

8.3.CriandoURLscurtas CasadoCódigo
headers Headers,
) {
for k, v := range headers {
w.Header().Set(k, v)
}
w.WriteHeader(status)
}
Continuandoofluxodeexecução,casotenhamosrecebidoumarequisi-
çãoPOSTválida,chamamosafunção extrairUrl()paralereretornara
URLrecebidanocorpodarequisição.Estafunçãoébastantesimples:
func extrairUrl(r *http.Request) string {
url := make([]byte, r.ContentLength, r.ContentLength)
r.Body.Read(url)
return string(url)
}
Primeiro,criamosumslicede byteschamado url,especificandoseu
tamanhoinicialcomosendootamanhodocorpodarequisição–presenteno
campo ContentLengthdotipo http.Request.Emseguida,utilizamos
ométodo Body.Read(),tambémdotipo http.Request,paralerocon-
teúdodocorpodarequisiçãoecopiá-loparaoslice url.Porfim,retornamos
uma stringcriadaapartirdaconversãodosbytespresentesnoslice url.
Com a URL recebida em mãos, chamamos o método
BuscarOuCriarNovaUrl() do nosso próprio pacote url, passando
comoargumentoaURLextraídadarequisição.Estemétodoretornatrêsva-
lores:umobjetodotipo url.Url,representandoaURLcurtarecém-criada;
umvalor bool,sendo truecasoumanovaURLcurtatenhasidocriada,
ou falsecasoaURLrecebidajátenhasidoencurtadaanteriormente;eum
errorcasoaURLrecebidasejainválida:
url, nova, err := url.BuscarOuCriarNovaUrl(extrairUrl(r))
Casotenhamosrecebidoumerro,retornamosumerroHTTP400(Bad
Request):
if err != nil {
responderCom(w, http.StatusBadRequest, nil)
128

## Página 143

CasadoCódigo Capítulo8. Mãonamassa:encurtadordeURLs
return
}
Emcasodesucesso,verificamosovalordavariávelnovaparadecidiro
códigoderesposta.ResponderemoscomocódigoHTTP201(Created)caso
aURLtenhasidocriada,ouHTTP200(O K),casoaURLjátenhasidoen-
curtadaanteriormente:
var status int
if nova {
status = http.StatusCreated
} else {
status = http.StatusOK
}
Finalmente,formatamosaURLcurtautilizandoa urlBasedefinidana
inicializaçãodopacoteeapontandoparaarota /r/,eentãorespondemos
comocódigodecididoanteriormente(201ou200)eaURLcurtanocabeça-
lho Location:
urlCurta := fmt.Sprintf("%s/r/%s", urlBase, url.Id)
responderCom(w, status, Headers{"Location": urlCurta})
Parademonstraralgunsexemplosderequisições paraonossoservidor,a
partirdeagorautilizaremosumaferramentachamada cURL.Sevocêéusuá-
rioLinuxouMacOS,provavelmentejápossuiestaferramentainstaladapor
padrão. Casocontrário,verifiqueasinstruções deinstalaçãoparaoseusis-
temaoperacionalemhttp://curl.haxx.se/download.html.
Utilizaremosduasopções docomando curl: -vparavisualizarmos
todososcabeçalhoseoconteúdodarequisição edaresposta;e -d,queé
utilizadaparafazerumarequisiçãodotipoPOST,sendoqueastringespe-
cificadaseráenviadanocorpodestarequisição. Parafacilitaravisualização,
algumaslinhasproduzidaspelocomandoserãoomitidasemtodososexem-
plosderequisições.
Aseguir,veremosumexemploderequisição paraencurtarumaURL
nova:
129

## Página 144

8.3.CriandoURLscurtas CasadoCódigo
$ curl -v http://localhost:8888/api/encurtar \
-d "http://casadocodigo.com.br/products/livro-vraptor"
> POST /api/encurtar HTTP/1.1
> User-Agent: curl/7.30.0
> Host: localhost:8888
> Accept: */*
> Content-Length: 64
> Content-Type: application/x-www-form-urlencoded
>
< HTTP/1.1 201 Created
< Location: http://localhost:8888/r/oZYm9
< Date: Tue, 03 Jun 2014 21:45:41 GMT
< Content-Length: 0
< Content-Type: text/plain; charset=utf-8
<
ReparenaURLcurtaretornadanocabeçalho Location.
Agora,serepetirmosamesmarequisição,receberemosumarespostacom
código200emvezdo201,conformeesperado:
$ curl -v http://localhost:8888/api/encurtar \
-d "http://casadocodigo.com.br/products/livro-vraptor"
> POST /api/encurtar HTTP/1.1
> User-Agent: curl/7.30.0
> Host: localhost:8888
> Accept: */*
> Content-Length: 64
> Content-Type: application/x-www-form-urlencoded
>
< HTTP/1.1 200 OK
< Location: http://localhost:8888/r/oZYm9
< Date: Tue, 03 Jun 2014 21:48:24 GMT
< Content-Length: 0
< Content-Type: text/plain; charset=utf-8
<
130

## Página 145

CasadoCódigo Capítulo8. Mãonamassa:encurtadordeURLs
8.4 Redirecionando para a sURLs originais
Analisando a URL curta retornada pelo exemplo anterior, percebemos
queelaapontaparaarota /r/, quefoiregistradaparasertratadapela
função Redirecionador(). Esta função tambémdeve ser do tipo
http.HandlerFunce,portanto,deveseguiramesmaassinatura:
func Redirecionador(w http.ResponseWriter, r *http.Request)
A p e s a rdeomecanismoderedirecionamentoserocoraçãodeumserviço
encurtadordeURLs,nãoprecisamosdemuitocódigopararealizarestatarefa.
OpadrãodasURLscurtasgeradaspeloserviçoanterioré/r/<id-curto>.
Nocasodarequisiçãodeexemplo,geramosaURLcurta /r/oZYm9;oiden-
tificadorcurtoé oZYm9.
Com isso em mente, o primeiro passo para redirecionar para a
URL original éextrair seu identificador do caminho da URL curta
(obtido em http.Request.URL.Path). Podemos chamar a função
strings.Split(),queseparaumastringemváriaspartesbaseadoemum
caractereespecificadoeretornaaspartesseparadasemumslice.V a m o suti-
lizar "/"comocaractereseparador,armazenarosliceretornadonavariável
caminho,eentãoassumirqueoúltimoelementodoslicecontémoidentifi-
cadoresperado:
caminho := strings.Split(r.URL.Path, "/")
id := caminho[len(caminho)-1]
AgoraprecisamosverificarseesteidentificadorcorrespondeaumaURL
armazenada.Paraisso,vamosutilizarafunção Buscar()donossopacote
url,querecebeumidentificadoreretornaaURLencontradaou nil,casoa
mesmanãoexista.Destaforma,verificamosseoretornoédiferentede nil.
Emcasopositivo,retornamosumarespostaHTTP301(M o v e dPermanently)
queiráredirecionarparaaURLoriginal( url.Destino);casooidentifi-
cadornãocorrespondaaumaURLencurtadaanteriormente,simplesmente
retornamosumerroHTTP404(N o tF o u n d):
if url := url.Buscar(id); url != nil {
http.Redirect(w, r, url.Destino,
131

## Página 146

8.4. RedirecionandoparaasURLsoriginais CasadoCódigo
http.StatusMovedPermanently)
} else {
http.NotFound(w, r)
}
Repareque,comoemnenhumdoscasosprecisamosrespondercomca-
beçalhosespeciais,utilizamosasfunções predefinidas http.Redirect()
e http.NotFound()paraformatarasrespostas.Outrodetalheimportante
éacriaçãodavariável urlnobloco if;istofazcomqueseuescoposeja
limitadosomenteaopróprioblocoeéumapráticabastantecomumquando
avariávelnãoseráutilizadaemnenhumoutrolugar.
UtilizandoaURLencurtadaanteriormente,podemosfazerumarequisi-
çãoGETevisualizararesposta:
$ curl -v http://localhost:8888/r/oZYm9
> GET /r/oZYm9 HTTP/1.1
> User-Agent: curl/7.30.0
> Host: localhost:8888
> Accept: */*
>
< HTTP/1.1 301 Moved Permanently
< Location: http://casadocodigo.com.br/...programador-apaixonado
< Date: Tue, 03 Jun 2014 22:15:40 GMT
< Content-Length: 99
< Content-Type: text/html; charset=utf-8
<
CasoaURLdesejadanãoexista,receberemosumerroHTTP404,como
noexemploaseguir:
curl -v http://localhost:8888/r/naoexiste
> GET /r/naoexiste HTTP/1.1
> User-Agent: curl/7.30.0
> Host: localhost:8888
> Accept: */*
>
< HTTP/1.1 404 Not Found
< Content-Type: text/plain; charset=utf-8
< Date: Tue, 03 Jun 2014 22:17:02 GMT
132

## Página 147

CasadoCódigo Capítulo8. Mãonamassa:encurtadordeURLs
< Content-Length: 19
<
8.5 Apresentando o p a c o t eurl
A t éaqui,opacoteinterno urlfoiapresentadomaisoumenoscomouma
caixapreta.Interagimoscomotipo url.Urleasfunções url.Buscar(),
url.BuscarOuCriarNovaUrl(), url.ConfigurarRepositorio()e
url.NovoRepositorioMemoria().
Agoraveremosemdetalhescadaumdesteselementos.
Criarumpacoteéamelhorformadeseparar–físicaelogicamente–cer-
toselementosemumaaplicaçãoGo.Nopacote url,definimostodaalógica
decriaçãoearmazenamentodasURLscurtas,sendoqueapenasumaparte
destasfuncionalidadesprecisaserexposta.Oservidornãoprecisaconhecer
detalhesdecomotudofunciona;precisaapenasconhecerainterfacepública
comaqualeledeveinteragirparacriareredirecionarURLs.
Todososexemplosapresentadosatéaquidefiniamapenasopacote main.
Paracriarumpacotediferente,bastaatribuiraeleumoutronome.Porisso,
oarquivo url/url.gocomeçacomaseguintedeclaração:
package url
T o d oocódigodefinidodentrodestearquivoserácompiladoemumpa-
cotechamado github.com/caiofilipini/encurtador/url,eapenas
oselementoscujosnomesiniciaremcomumaletramaiúsculaserãovisíveis
poroutrospacotes.
Opacote url,porsuavez,dependedealgunsoutrospacotes:
import (
"math/rand"
"net/url"
"time"
)
Alémdasdependências,nossopacotetambémdefinealgumasconstantes
utilizadasinternamente(notequeseusnomesiniciamcomletrasminúscu-
las):
133

## Página 148

8.6. Especificandoaimplementaçãodorepositório CasadoCódigo
const (
tamanho = 5
simbolos = "abcdefghijklmnopqr...STUVWXYZ1234567890_-+"
)
Aconstante tamanhodefineotamanhodoidentificadorcurtoquede-
verásergerado.Jáaconstante simboloslistatodososcaracterespermitidos
emumidentificador;veremosembrevecomoelessãogerados.
Parainicializarsuasdependências,umpacotepodedefinirumafunção
init(),comoaquefoiapresentadanoarquivo servidor.go.Opacote
urltambémdefinesuaprópriafunçãodeinicialização;nestecaso,elaéuti-
lizadaapenasparaconfigurarasementeparageraçãodenúmerosaleatórios:
func init() {
rand.Seed(time.Now().UnixNano())
}
Opacote urldefinetambémalgunstipos,comoojáconhecidotipo
Url:
type Url struct {
Id string
Criacao time.Time
Destino string
}
8.6 Especificandoa implementação d o reposi-
tório
ParapadronizaraimplementaçãodorepositórioondeasURLsserãoarma-
zenadas,definimostambémumainterfacechamada Repositorio:
type Repositorio interface {
IdExiste(id string) bool
BuscarPorId(id string) *Url
BuscarPorUrl(url string) *Url
Salvar(url Url) error
}
134

## Página 149

CasadoCódigo Capítulo8. Mãonamassa:encurtadordeURLs
Oobjetivodestainterfaceéespecificartodasasoperações queumrepo-
sitóriodeURLsdeverásercapazdeimplementar. Nesteexercício,imple-
mentaremosumrepositórioemmemória.Porém,poderíamossubstituiresta
implementaçãoporumbancodedadosrelacional,porexemplo,desdequeo
contratodefinidopelainterface Repositoriofosseatendido.Destaforma,
precisaríamosalterarapenasalinhaqueconfiguraorepositórioaserutilizado
noarquivo servidor.go.
Como a implementação concreta do repositório éconfigurada ex-
ternamente, precisamos definir uma função que seja capaz de registrar
esta configuração. Paraisso, definimosprimeiramenteavariável repo
para armazenaro repositório propriamentedito, e fornecemosa função
ConfigurarRepositorio():
var repo Repositorio
func ConfigurarRepositorio(r Repositorio) {
repo = r
}
Reparequeotipodoargumento rédefinidocomo Repositorio,queé
ainterfacedefinidaanteriormente.Destaforma,nãoimportaqualéaimple-
mentaçãoconfigurada,destequeainterfacesejaobedecida;oprópriocompi-
ladorgaranteestarestrição.Reparetambémqueaúnicaformadeconfigurar
orepositórioéatravésdestafunção,jáqueavariávelreponãoévisívelfora
dopacote.
Aimplementaçãodorepositórioemmemóriaseráapresentadaposteri-
ormente.
8.7 Criando identificadorescurtos
U m adasfuncionalidadesprincipaisdeumserviçoencurtadordeURLséa
capacidadedegeraridentificadorescurtos.Paraexporestafuncionalidade,o
pacote urlimplementaafunção BuscarOuCriarNovaUrl().Suaassi-
naturaéaseguinte:
func BuscarOuCriarNovaUrl(destino string) (
u *string,
135

## Página 150

8.7.Criandoidentificadorescurtos CasadoCódigo
nova bool,
err error,
)
Recapitulando,estafunçãorecebeaURLoriginalcomoargumentoere-
tornatrêsvalores:umponteiroparaumobjetodotipo Url,representandoa
URLcurtarecém-criada;umvalor bool,sendo truecasoumanovaURL
curtatenhasidocriada,ou falsecasoaURLrecebidajátenhasidoencur-
tadaanteriormente;eum errorcasoaURLrecebidasejainválida.
OprimeiropassoéverificarseaURLjáfoiencurtadaanteriormente,evi-
tandoduplicações. Paraisso,chamamosométodorepo.BuscarPorUrl()
passandoaURL destinocomoargumento.CasoumaURLtenhasidoen-
contrada,elaseráimediatamenteretornada,acompanhadadovalor false,
indicandoqueaURLjáexistia,e nilcomoerro:
if u = repo.BuscarPorUrl(destino); u != nil {
return u, false, nil
}
CasoaURLespecificadaaindanãotenhasidoencurtada,precisamoster
certezadequerecebemosumaURLválidaparaevitarproblemasderedireci-
onamento.Abibliotecapadrãoforneceumpacotechamado net/url,res-
ponsávelporidentificaremanipularURLsdetodosostipos.Estepacotede-
fineumafunção ParseRequestURI(),quetrataespecificamentedeURLs
HTTP,eretornaumerrocasoaURLespecificadanão sejaválida–exata-
menteoqueprecisamosfazer.Casoumerrotenhasidoencontrado,eleserá
retornado:
if _, err = url.ParseRequestURI(destino); err != nil {
return nil, false, err
}
Sechegamosatéaqui,temosacertezadequeaURLrecebidaéválidaenão
foiencurtadaanteriormente.Portanto,criamosumnovoobjeto Urleopo-
pulamoscomumidentificadorcurto,umadatadecriação(adata/horaatual)
eaURLdestino.Emseguida,chamamosométodo repo.Salvar()para
persisti-lonorepositórioeretornamosoendereçodoobjetorecém-criadoe
ovalor true,indicandoacriaçãodeumanovaURL:
136

## Página 151

CasadoCódigo Capítulo8. Mãonamassa:encurtadordeURLs
url := Url{gerarId(), time.Now(), destino}
repo.Salvar(url)
return &url, true, nil
Agoravamosacompanharpassoapassooalgoritmoparagerarumnovo
identificadorcurto,implementadopelafunção gerarId().Aideiageralé
extraircincocaracteresaleatórios(comodefinidopelaconstante tamanho)
dalistadecaracterespermitidos(definidanaconstante simbolos)ejuntá-
losemuma string–oidentificador;casoelejáexistanorepositório,repe-
timosoprocessoatéqueumidentificadortotalmentenovosejagerado:
func gerarId() string {
novoId := func() string {
id := make([]byte, tamanho, tamanho)
for i := range id {
id[i] = simbolos[rand.Intn(len(simbolos))]
}
return string(id)
}
for {
if id := novoId(); !repo.IdExiste(id) {
return id
}
}
}
Comocada caractereda string simbolos éacessadoindividual-
mente,elessãorepresentadoscomo bytes,porissoavariávelidfoidefinida
comoumslicede bytes,queéconvertidoparaumastring( string(id))
antesdeserretornado.
Outrodetalheinteressanteéque,parafacilitararepetição doprocesso
casoumidentificadorjáexista,criamosumafunçãoanônimaeaarmazena-
mosnavariávelnovoId.Assim,podemoschamá-lamaisdeumavezemum
laçoinfinito,queéquebradoquandoapalavra-chave returnforçaoretorno
dafunçãoassimqueumidentificadortotalmentenovoégerado.
Parafinalizar,comoorepositório repoéumobjetovisívelapenasao
pacote url,precisamosexporafuncionalidadedebuscarumaURLpeloseu
137

## Página 152

8.8. Implementandoorepositórioemmemória CasadoCódigo
identificadorcurto,daqualoredirecionadordepende.Paraisso,definimosa
função Buscar(),queapenasdelegaabuscaaoprópriorepositório:
func Buscar(id string) *Url {
return repo.BuscarPorId(id)
}
8.8 Implementando o repositório em memória
Orepositórioemmemória,partedopacote url,serádefinidonoarquivo
url/repositorio_memoria.go,quetambémcomeçacomadefiniçãodo
pacote:
package url
Naprática,esterepositórionadamaisédoqueummapacujaschavessão
osidentificadorescurtos,eosvaloressão ponteirosparaosobjetosdotipo
Url.Emoutraspalavras,um map[string]*Url:
type repositorioMemoria struct {
urls map[string]*Url
}
Reparequeonomedotipodefinidoé repositorioMemoria,inici-
andocomumaletraminúscula.Istogarantequeaimplementaçãonãoserá
conhecidaforadoprópriopacote,assegurandooencapsulamento.
Noentanto,precisamosfornecerumamaneiradecriarobjetosdestetipo.
Esteéoobjetivodafunção NovoRepositorioMemoria(),utilizadapelo
servidorparacriareconfigurarumrepositórionoiníciodaexecuçãodopro-
grama:
func NovoRepositorioMemoria() *repositorioMemoria {
return &repositorioMemoria{make(map[string]*Url)}
}
Comoaimplementaçãoébaseadaemummapa,seusmétodostirampro-
veitodasfuncionalidadesbásicasdosmapasemGo.
Porexemplo,ométodo IdExiste()simplesmenteverificaseoidenti-
ficadorespecificadoéumachavequeexistenomapa:
138

## Página 153

CasadoCódigo Capítulo8. Mãonamassa:encurtadordeURLs
func (r *repositorioMemoria) IdExiste(id string) bool {
_, existe := r.urls[id]
return existe
}
Demaneirasemelhante,ométodo BuscarPorId()retornaovalorar-
mazenadosoboidentificadorrecebido,queseránilcasoachavenãoesteja
presentenomapa:
func (r *repositorioMemoria) BuscarPorId(id string) *Url {
return r.urls[id]
}
JáométodoBuscarPorUrl()precisaiterarpelosvaloresarmazenados
nomapaecompará-losàURLrecebidacomoargumento,retornandooobjeto
correspondentecasoencontreaURLdesejada,ou nilcasocontrário:
func (r *repositorioMemoria) BuscarPorUrl(url string) *Url {
for _, u := range r.urls {
if u.Destino == url {
return u
}
}
return nil
}
Porfim,ométodoSalvar()armazenaumanovaentradanomapauti-
lizandooidentificadorda Urlcomochave,eoendereçodopróprioobjeto
comovalor:
func (r *repositorioMemoria) Salvar(url Url) error {
r.urls[url.Id] = &url
return nil
}
Comoestaoperação emummapanãoproduznenhumerro(anãoser
quenãoexistamaismemóriadisponívelparaarmazenarestevalor),ométodo
Salvar()simplesmenteretorna nil.
Missãocumprida!Nopróximocapítulo,veremoscomoexecutar,compi-
lareinstalaroprojetolocalmente.
139

## Página 155

Capítulo9
Compilandoeexecutandoo
projeto
Goéumalinguagemcompilada,assimcomoCouC++.Istosignificaquenão
existeumalinguagemintermediárianemumamáquinavirtualenvolvidasno
momentodaexecuçãodeumprograma.CódigoGoécompiladodiretamente
paraalinguagemdamáquina;oartefatogeradopeloprocessodecompilação
éumarquivobinárioexecutável,compatívelapenascomosistemaoperacio-
nalalvodacompilação.
Todososexemplosapresentadosatéaquiforamexecutadosatravésdo
comando go run.
Porexemplo,agoraquetemosumcódigofuncionalparaoservidorde
URLscurtas,podemosexecutá-loutilizandoomesmocomando.Primeiro,
certifique-sedequevocêestánodiretório quecontémocódigo dopro-

## Página 156

9.1.Entendendooprocessodecompilação CasadoCódigo
jeto( $GOPATH/src/github.com/caiofilipini/encurtador),een-
tãoexecuteocomandoaseguir:
$ go run servidor.go
Seoprogramafoicompiladocomsucessoeoservidorfoicapazdeabrir
um socketnaporta8888,nenhumasaídaserágeradaeoprocessoficaráblo-
queado.Paratercertezadequeoservidorestánoar,podemos,emumaoutra
instânciadoterminal,utilizaroseguintecomando:
$ telnet localhost 8888
Trying 127.0.0.1...
Connected to localhost.
Escape character is ’^]’.
Sevocêobteveumasaídasimilaraoexecutarocomando telnet,signi-
ficaqueoservidorestánoarefomoscapazesdenosconectaraele.
9.1 Entendendo o processo de compilação
Ocomando go runexecutaoprocessocompletodecompilação semque
vocêprecisesepreocuparcomoqueestáacontecendo.Porisso,éumutilitá-
riomuitoimportanteduranteodesenvolvimentodeprogramasemGo.
Naprática,estecomandorealizatrêsoperações distintassequencial-
mente:compilaosarquivos-fonteemarquivos-objeto;realizaoprocessode
linkedição dosarquivos-objeto,gerando(emumdiretóriotemporário)um
executávelbinário;executaobináriogerado.Estefluxoébastantesimilarao
utilizadoparacompilarprogramasemCeC++.
AsferramentasdistribuídascomalinguagemGofornecemcomandos
distintosparacompilaçãoelinkedição. Estescomandospossuemnomesdi-
ferentesdeacordocomaarquiteturadoprocessadoralvodacompilação.Por
exemplo,casoaarquiteturaalvoseja amd64,precisamosutilizarocomando
6gparacompilarosarquivos-fonte,eemseguidaocomando 6lpararea-
lizaralinkedição;demaneiraanáloga,pararealizaromesmoprocedimento
paraprocessadorescomarquitetura x86,oscomandossão 8ge 8l,respec-
tivamente.Essanomenclaturaéherançadasferramentasdecompilaçãodo
142

## Página 157

CasadoCódigo Capítulo9. Compilandoeexecutandooprojeto
sistemaoperacionalPlan9,queforamabaseparaacriaçãodasferramentas
disponíveisemGo.
É importante conhecer estes detalhes para entender o que acontece
quandocompilamoseexecutamosumprogramaemGo.Noentanto,épos-
sívelrealizartodoesteprocessocomumúnicocomando: go build.
PodemosgerarumexecutáveldonossoserviçoencurtadordeURLs
executando este comando. Como o código estáhospedado em um di-
retório chamado encurtador, oarquivoexecutávelserágeradocomo
mesmonome. Assumindoqueaindatemosumterminalabertonodire-
tório $GOPATH/src/github.com/caiofilipini/encurtador,pode-
mosgerarumexecutávelparaonossoprojetoeexecutá-lodaseguinteforma:
$ go build
$ ls -l ./encurtador
-rwxr-xr-x 1 caio xxxxx 6.6M Jun 5 22:35 ./encurtador
$ ./encurtador
Estespassosreproduzemexatamenteoprocessorealizadoquandoutili-
zamosocomando go run,comadiferençadequeoexecutávelgeradonãoé
descartadoquandosuaexecuçãoéfinalizada.Ocomando lsfoiadicionado
apenasparafacilitaravisualização.
9.2 Instalando o executável no sistema
Gotambémforneceumcomandochamado go install,queexecutao
mesmoprocessodecompilaçãoapresentadoanteriormente,porémfazains-
talaçãodoprogramanoambienteGolocal,conformeconfiguradonavariável
deambiente $GOPATH.
Porexemplo,considerandoqueestamoscompilandooprojetoemum
Linux64bits,quandoexecutamos go installnodiretório encurtador,
doisartefatossãogeradoseinstalados:
•o pacote url é compilado e disponibilizado em
$GOPATH/pkg/linux_amd64/github.com/.../encurtador/url.a
paraquepossaserutilizadoporoutrosprogramas;
143

## Página 158

9.3.Aprendendomais CasadoCódigo
•oexecutável encurtador,compatívelapenascomLinux64bits,é
geradonodiretório $GOPATH/bin.
Assim,casoodiretório $GOPATH/bintenhasidoadicionadoàvariável
deambiente $PATH,épossívelexecutaroservidordeURLscurtasdequal-
querlugardoseusistema.
9.3 Aprendendo mais
Oprocessodecompilação deprogramasemGoébastanteprático,porém
apenasobásicofoiapresentadonestecapítulo.Épossível,porexemplo,gerar
executáveiscompatíveiscomWindowsemumcomputadorcomMacOSou
Linuxevice-versa.
Parafinalizar,vamosfazerumpequenoexercício.Ocomando go build
possuiumaopção -xquemostra,passoapasso,todooprocessodecompi-
lação.Executeestecomandonoseucomputador,analiseosresultadosetente
entenderoqueaconteceemcadaumdospassos.
$ go build -x
Adocumentaçãocompletadocomando gopodeserencontradanoen-
dereçohttp://golang.org/cmd/go/.
144

## Página 159

Capítulo10
Colhendoestatísticas
SistemasencurtadoresdeURLsforamcriadosparafacilitarocompartilha-
mentodeURLs. Istosetornouespecialmenteimportanteapósapopulari-
zação deserviçoscomooT w i t t e r ,ondeonúmerodecaracteresélimitado,
impossibilitandoocompartilhamentodeURLsmuitograndes.
Hojeemdia,osserviçosencurtadoresdeURLsmaispopularesprovêm
tambémumasériedefuncionalidadescomplementares,sendoacoletaevi-
sualizaçãodeestatísticasumadasmaisimportantes.
V a m o scriarummecanismoparacoletarestatísticasarespeitodasURLs
curtascriadaspelonossopróprioserviço: implementaremosumasimples
contagemdequantasvezescadaURLfoiacessada.

## Página 160

10.1.Realizandoacontagemnorepositório CasadoCódigo
10.1 Realizandoa contagem no repositório
Existemváriasformasdeimplementaracontagemdeacessos.Comojáim-
plementamosorepositórioemmemóriautilizandoummapa,podemosrea-
proveitaraideiaeutilizartambémummapaparaarmazenaracontagem.
Parafacilitaraimplementação,vamosadicionarummétodoàinterface
Repositoriojáexistente,definidanoarquivo url/url.go:
type Repositorio interface {
// ...
RegistrarClick(id string)
}
Precisamostambémalterarotipo repositorioMemoriaparaimple-
mentaronovométodo.Masantesdeadicionaraimplementação, preci-
samoscriarumnovomapaparaarmazenaracontagemdeacessos. Para
isso, vamos adicioná-loà struct repositorioMemoria no arquivo
url/repositorio_memoria.go:
type repositorioMemoria struct {
// ...
clicks map[string]int
}
Comoadicionamosumnovomapa,precisamosgarantirqueeleserá
inicializado na criação do objeto. Portanto, vamos alterar a função
NovoRepositorioMemoria()parainicializá-lo:
func NovoRepositorioMemoria() *repositorioMemoria {
return &repositorioMemoria{
make(map[string]*Url),
make(map[string]int),
}
}
Parafacilitaraleitura,quebramosainicializaçãoemváriaslinhas.
Finalmente, podemos adicionar a implementação do método
RegistrarClick() ao tipo repositorioMemoria da seguinte
forma:
146

## Página 161

CasadoCódigo Capítulo10.Colhendoestatísticas
func (r *repositorioMemoria) RegistrarClick(id string) {
r.clicks[id] += 1
}
Comoovalorarmazenadosobumachave stringéum int,quepossui
0comovalorpadrão,nãoprecisamosverificarsejáexistealgumvalorarma-
zenadoparaachave idrecebida;quandooprimeiroacessoforregistrado,
achamada r.clicks[id]retornará 0e,portanto,aexpressãocompleta
r.clicks[id] += 1resultaránovalor 1sendoarmazenadoparao id
recebido.
Paraquepossamoschamá-lodeforadopacote url,precisamosex-
porestemétodo.Assim,podemosregistrarasrequisições recebidaspela
função Redirecionador()definidanoarquivo servidor.go. Para
isso, vamos alterar o arquivo url/url.go e criar uma nova função
RegistrarClick(). Elairáapenasdelegarachamadaaorepositório,de
maneirasemelhanteàformacomoimplementamosafunção Buscar():
func RegistrarClick(id string) {
repo.RegistrarClick(id)
}
Agoraorepositórioestápreparadopararealizaracontagemdeacessos.
10.2 Registrando os acessos no servidor
Pararegistrarcadaacesso,precisamosalteraro servidor.goparachamar
afunção url.RegistrarClick()acadarequisiçãorecebida.
Comonomomentoregistraremosapenasaquantidadedeacessos,po-
deríamossimplesmentealterarafunção Redirecionador()eadicionara
chamadaimediatamenteapósachamadaà http.Redirect(),resultando
noseguintecódigo:
func Redirecionador(w http.ResponseWriter, r *http.Request) {
// ...
if url := url.Buscar(id); url != nil {
http.Redirect(w, r, url.Destino,
147

## Página 162

10.2.Registrandoosacessosnoservidor CasadoCódigo
http.StatusMovedPermanently)
url.RegistrarClick(id)
}
// ...
}
Noentanto,normalmenteestetipoderedirecionamentodevesertratado
damaneiramaisrápidapossível.Casodesejássemosregistraroutrasmétri-
casnofuturo,precisaríamosadicionardiversasoutraschamadasadiferentes
funções oumétodos,atrasandoaindamaisarespostaepiorandomuitoaex-
periênciadousuário.
EstetipodeproblemaémuitocomumemservidoresHTTP.U m atéc-
nicabastanteutilizadapararesolvê-loéprocessarapenasonecessárionomo-
mentodarequisição,eutilizaralgummecanismopararealizarorestantedo
trabalhoemummomentoposterior.
Implementarestetipodesolução emGoétrivial: vamosutilizaruma
goroutine!
Precisamosdeumcanalpararealizaracomunicação comagoroutine.
Comotudooqueprecisamospararegistraroacessoédoidentificadorda
URLcurta–uma string–,criaremosumcanalcapazdetrafegar strings.
Estecanaldeveseracessívelpelaprópriagoroutine,mastambémpelafun-
ção Redirecionador(). Podemosdeclará-locomoumavariávelglobal,
damesmaformaquefizemoscomasvariáveisportae urlBase:
var (
porta int
urlBase string
stats chan string
)
V a m o scriarumafunçãoque,utilizandoooperador range,bloqueiaa
execuçãoatéquealgumamensagemsejarecebidanocanal,eentãoregistra
oacessonorepositórioeimprimeumalinhanasaídapadrão indicandoo
sucessodaoperação:
148

## Página 163

CasadoCódigo Capítulo10.Colhendoestatísticas
func registrarEstatisticas(ids <-chan string) {
for id := range ids {
url.RegistrarClick(id)
fmt.Printf("Click registrado com sucesso para %s.\n", id)
}
}
Paraquepossamosregistrarasestatísticasparacadaredirecionamento,
precisamosdispararagoroutineassimqueoservidorforiniciado. V a m o s
alterarafunção main()paracriarocanaleimediatamenteiniciarumago-
routineexecutandoafunção registrarEstatisticas():
func main() {
stats = make(chan string)
defer close(stats)
go registrarEstatisticas(stats)
// ...
}
Repareque,assimqueocanalfoicriado,garantimosqueeleseráfe-
chadoaofinaldaexecuçãodafunção main()atravésdachamada defer
close(stats).
Parafinalizar,vamosalterarafunção Redirecionador()paraenviar
oidentificadordaURLacessadaparaocanal stats,desencadeandoopro-
cessoqueiráregistraresteacesso:
func Redirecionador(w http.ResponseWriter, r *http.Request) {
// ...
if url := url.Buscar(id); url != nil {
http.Redirect(w, r, url.Destino,
http.StatusMovedPermanently)
stats <- id
}
// ...
}
149

## Página 164

10.2.Registrandoosacessosnoservidor CasadoCódigo
Agorajátemostodoocódigonecessáriopararegistrarasestatísticasde
acesso!
V a m o siniciaroservidorexecutandoanovaversãodocódigo:
$ go run servidor.go
Emumaoutrajaneladoterminal,vamoscriarumanovaURLcurta:
$ curl -v "http://localhost:8888/api/encurtar" \
-d "http://casadocodigo.com.br/products/livro-jogos-android"
> POST /api/encurtar HTTP/1.1
> User-Agent: curl/7.30.0
> Host: localhost:8888
> Accept: */*
> Content-Length: 55
> Content-Type: application/x-www-form-urlencoded
>
< HTTP/1.1 201 Created
< Location: http://localhost:8888/r/9aOFf
< Date: Sat, 07 Jun 2014 19:09:12 GMT
< Content-Length: 0
< Content-Type: text/plain; charset=utf-8
<
Apartirdeagora,cadarequisiçãoàURLcurtadeveráincrementarocon-
tador.V a m o srealizaralgumasrequisições everificarseoregistroestásendo
feito:
$ curl http://localhost:8888/r/9aOFf
$ curl http://localhost:8888/r/9aOFf
$ curl http://localhost:8888/r/9aOFf
Parafacilitaravisualização,osdetalhesdestasrequisiçõesforamomitidos
porcompleto.
Paracadaumadestasrequisições, najanelaondeoservidorfoiiniciado,
podemosverumalinharelacionadaindicandooregistrodoacesso:
Click registrado com sucesso para 9aOFf.
Click registrado com sucesso para 9aOFf.
Click registrado com sucesso para 9aOFf.
150

## Página 165

CasadoCódigo Capítulo10.Colhendoestatísticas
Mascomosaberseestamosdefatoregistrandocadaacesso?
Precisamosforneceralgumamaneiradevisualizarasestatísticascolhi-
das.Idealmente,umaAPIdestetipodeveproverestesdadosdeumamaneira
flexível,permitindoqueoclientedecidaamelhorformadeapresentá-los.
ComoestamosdesenvolvendoumaAPIsobreHTTP,umaformasimples
deatingiresteresultadoéretornarosdadosnoformatoJSON(JavaScript
Object Notation).
10.3 SerializandoJSON
Para serializar objetos no formato JSON, Go fornece o pacote
encoding/json. Basicamente, quase qualquer tipo válidoem Go
podeserserializado,incluindo mapse structs,comaexceçãodecanais,
funções eotipo complex(querepresentanúmeroscomplexos).
Serializaruma structutilizandoopacote encoding/jsonéumata-
refatrivial;bastachamarafunção json.Marshal(),quepossuiaseguinte
assinatura:
func Marshal(v interface{}) ([]byte, error)
Repare que, para ser capaz de serializar qualquer tipo, a função
Marshal()recebeumargumentodotipo interface{},denominado v.
Estafunçãoconvertetodososcampos públicosda struct vemsuasrepre-
sentações JSONeretornaumslicede bytescontendooJSONserializado,
eum error,queseránilcasoaserializaçãotenhasidorealizadacomsu-
cesso.
Porexemplo,paraserializarumvalordotipo url.Url,podemosutilizar
oseguintetrechodecódigo:
url := Url{
"9aOFf",
time.Now(),
"http://casadocodigo.com.br/products/livro-jogos-android",
}
json, err := json.Marshal(url)
151

## Página 166

10.3.SerializandoJSON CasadoCódigo
if err == nil {
fmt.Println(string(json))
}
Assim,oobjeto urlseriaconvertidoparaaseguinterepresentaçãoJSON
(aformataçãofoiadicionadaparafacilitaravisualização):
{
"Id":"9aOFf",
"Criacao":"2009-11-10T23:00:00Z",
"Destino":
"http://casadocodigo.com.br/products/livro-jogos-android"
}
Simples,não?
Oúnicoproblemacomoexemploanterioréonomedoscampos–como
apenasoscampospúblicossãoserializados,seusnomessãorefletidosnore-
sultadogeradoecomeçamcomletrasmaiúsculas;dificilmenteencontrare-
mosumaAPIretornandovaloresJSONdestaforma.
Felizmente,Goprovêumasolução paraesteproblema:marcadoresde
structs(ou s t r u c tt ag s). Podemoscontrolaraformacomooscamposde
uma structserãoserializadosatravésdautilizaçãodestesmarcadores.
Porexemplo,parainstruirométodo json.Marshal()aserializaros
camposda struct Urlcomnomescomeçandoemletrasminúsculas,pre-
cisamosadicionaraelaosseguintesmarcadores:
type Url struct {
Id string `json:"id"`
Criacao time.Time `json:"criacao"`
Destino string `json:"destino"`
}
Destaforma,executandoomesmotrechodecódigoapresentadoanteri-
ormente,obteríamoscomoresultadooJSON:
{
"id":"9aOFf",
"criacao":"2009-11-10T23:00:00Z",
152

## Página 167

CasadoCódigo Capítulo10.Colhendoestatísticas
"destino":
"http://casadocodigo.com.br/products/livro-jogos-android"
}
Utilizaremosmarcadoresdestetipoparaserializarasestatísticasdeacesso
dasURLs.
10.4 Visualizandoa sestatísticas co mo JSON
AgoraquejásabemosobásicosobreserializaçãoJSONemGo,vamosadici-
onarumanovarotaaonossoservidorpararetornarasestatísticasdeacesso
deumaURLnesteformato.
Antesdemaisnada,precisamosdefinirumanova structpararepre-
sentarasestatísticas,jáincluindoosmarcadoresparaconverterosnomesdos
camposparaletrasminúsculas.V a m o sadicionaradefinição destetipoao
arquivo url/url.go:
type Stats struct {
Url *Url `json:"url"`
Clicks int `json:"clicks"`
}
A struct Statsdefinedoiscampos:umareferênciaà Urlcorrespon-
denteeumvalor intquecontémaquantidadedeacessosaesta Url.
Precisamostambémadicionarosmarcadoresà struct Url,conforme
oexemploanterior:
type Url struct {
Id string `json:"id"`
Criacao time.Time `json:"criacao"`
Destino string `json:"destino"`
}
Parapoderretornaronúmerodeacessosarmazenadoparaumadetermi-
nadaURL,precisamosadicionarummétodoàinterface Repositorio:
type Repositorio interface {
// ...
153

## Página 168

10.4.VisualizandoasestatísticascomoJSON CasadoCódigo
BuscarClicks(id string) int
}
T a m b é mprecisamosadicionaraimplementaçãodestemétodoaoarquivo
url/repositorio_memoria.go:
func (r *repositorioMemoria) BuscarClicks(id string) int {
return r.clicks[id]
}
EstemétodoretornaráaquantidadedeacessosregistradosparaaURL
identificadapor id. Casonenhumacessotenhasidoregistradoparaesta
URL,aexpressão r.clicks[id]retornará0–ovalorpadrãodotipo int.
Paracriarumainterfacemaisnatural,vamosagoraadicionarummétodo
à struct UrlpararetornarasestatísticasreferentesaumaURL.Primeiro,
obtemosonúmerodeacessosregistradosparaestaURLchamandoorecém-
criadométodo repo.BuscarClicks();depois,criamosumnovoobjeto
Stats,associandoa Urleinjetandoonúmerodeacessos:
func (u *Url) Stats() *Stats {
clicks := repo.BuscarClicks(u.Id)
return &Stats{u, clicks}
}
Agoraprecisamoscriarumanovarotaao servidor.gopararetornar
oJSONcontendoasestatísticasdeumadeterminadaURL.Primeiro,vamos
adicionaranovarotaàconfiguraçãodoservidornafunção main(),antes
dachamadaà http.ListenAndServe():
func main() {
// ...
http.HandleFunc("/api/stats/", Visualizador)
// ...
}
Afunção Visualizador()émuitosimilarà Redirecionador(),
portanto,vamosdiretoàimplementação:
154

## Página 169

CasadoCódigo Capítulo10.Colhendoestatísticas
func Visualizador(w http.ResponseWriter, r *http.Request) {
caminho := strings.Split(r.URL.Path, "/")
id := caminho[len(caminho)-1]
if url := url.Buscar(id); url != nil {
json, err := json.Marshal(url.Stats())
if err != nil {
w.WriteHeader(http.StatusInternalServerError)
return
}
responderComJSON(w, string(json))
} else {
http.NotFound(w, r)
}
}
ComeçamosextraindooidentificadordaURLdocaminhodarequisição,
damesmaformaquefizemosnafunção Redirecionador().Emseguida,
chamamosafunção url.Buscar()paraobterosdadosdaURL.SeaURL
forencontrada,utilizamosafunção json.Marshal()paraserializarore-
sultadodachamada url.Stats()(i.e.umvalordotipo url.Stats).
Casoumerroocorraduranteaserialização,interrompemosoprocessa-
mentoeretornamosumerroHTTP500.
Jáemcasodesucesso,convertemososlice jsonemuma stringe
chamamosafunção responderComJSON()paraformatararesposta.
Estafunçãosimplesmentechamaafunção responderCom(),configu-
randoovalor application/jsonparaocabeçalho Content-Typeees-
crevendooJSONrecebidonocorpodaresposta:
func responderComJSON(w http.ResponseWriter, resposta string) {
responderCom(w, http.StatusOK, Headers{
"Content-Type": "application/json",
})
fmt.Fprintf(w, resposta)
}
155

## Página 170

10.4.VisualizandoasestatísticascomoJSON CasadoCódigo
Porfim,seoidentificadorrecebidonãocorresponderaumaURLcurta
existente,retornamosumerroHTTP404.
Oúltimopassonecessárioparacompletarestafuncionalidadeécriaral-
gumaligaçãoentreaURLcriadaesuasestatísticas.EmumaAPI RESTful,
quandoumrecursoécriado,arespostaàrequisição queocrioudevein-
cluirdealgumaformaestetipodeligação.Porexemplo,atravésdocabeçalho
Link.
V a m o salterarafunção Encurtador()paraincluirestecabeçalhocom
oendereçodasestatísticasdaURLrecém-criada.Precisamosmodificaracha-
madaàfunção responderCom()daseguinteforma:
func Encurtador() {
// ...
responderCom(w, http.StatusCreated, Headers{
"Location": urlCurta,
"Link": fmt.Sprintf("<%s/api/stats/%s>; rel=\"stats\"",
urlBase, url.Id),
})
}
Agorapodemosreiniciaroservidorevisualizaralgumasestatísticas:
$ go run servidor.go
V a m o srepetiroprocessorealizadoanteriormenteparacriarumanova
URLcurta,fazeralgumasrequisições aestaURLe,então,visualizarsuases-
tatísticas:
$ curl -v "http://localhost:8888/api/encurtar" \
-d "http://casadocodigo.com.br/products/livro-devops"
> POST /api/encurtar HTTP/1.1
> User-Agent: curl/7.30.0
> Host: localhost:8888
> Accept: */*
> Content-Length: 48
> Content-Type: application/x-www-form-urlencoded
156

## Página 171

CasadoCódigo Capítulo10.Colhendoestatísticas
>
< HTTP/1.1 201 Created
< Link: <http://localhost:8888/api/stats/Cp+Hf>; rel="stats"
< Location: http://localhost:8888/r/Cp+Hf
< Date: Sun, 08 Jun 2014 22:08:24 GMT
< Content-Length: 0
< Content-Type: text/plain; charset=utf-8
<
Reparequeretornamosocabeçalho Linkcomoendereçoparaacessaras
estatísticasdaURLrecém-criada.RequisitandoestaURL,teremososeguinte
resultado(maisumavezformatadoparafacilitaravisualização):
$ curl http://localhost:8888/api/stats/Cp+Hf
{
"url":{
"id":"Cp+Hf",
"criacao":"2014-06-09T00:08:24.899606706+02:00",
"destino":
"http://casadocodigo.com.br/products/livro-devops"
},
"clicks":0
}
Nenhumacessofoiregistradoporenquanto.V a m o sfazeralgumasrequi-
sições paraaURLcurta:
$ curl http://localhost:8888/r/Cp+Hf
$ curl http://localhost:8888/r/Cp+Hf
$ curl http://localhost:8888/r/Cp+Hf
$ curl http://localhost:8888/r/Cp+Hf
Agora,seacessarmosnovamenteasestatísticasdestaURL,veremosase-
guinteresposta:
$ curl http://localhost:8888/api/stats/Cp+Hf
{
"url":{
"id":"Cp+Hf",
"criacao":"2014-06-09T00:08:24.899606706+02:00",
157

## Página 172

10.4.VisualizandoasestatísticascomoJSON CasadoCódigo
"destino":
"http://casadocodigo.com.br/products/livro-devops"
},
"clicks":4
}
Registramoscorretamenteos4acessos.NossaAPIestáfinalmentecom-
pleta!
U mdetalheimportanteéque,comorequisições deredirecionamentopo-
demser(enormalmentesão)armazenadasemcache,acessarasURLscurtas
emumnavegadorpodeproduzirresultadosdiferentesnacontagemdeaces-
sos.
Nopróximocapítulo,veremoscomomelhorarocódigoproduzidoaté
aqui.
158

## Página 173

Capítulo11
Refatorandoocódigo
DepoisdeimplementartodasasfuncionalidadesnonossoservidordeURLs
curtas,podemosanalisarumpoucoocódigoproduzidoeidentificaralguns
pontosdemelhoria,comoporexemplo:
•Substituirvariáveisglobaisondepossível;
•Reduzirduplicaçãodecódigo;
•Introduzirlogs;
•T o r n a rainicializaçãomaisflexível.
V a m o sabordarcadaumdositensdestalistadeformaseparada.

## Página 174

11.1.Substituindovariáveisglobais CasadoCódigo
11.1 Substituindo v ariáveis globais
Utilizarvariáveisglobaiséumaformamuitopráticadecompartilharrecursos
entrediferentesfunções, objetosemétodosemumprograma. Noentanto,
algunsdestesvalorespodemserbastantesensíveis,epermitiracessoglobala
elespodeintroduzirumasériedeproblemas.
Nossoservidordefinetrêsvariáveisglobais: porta, urlBaseeoca-
nal stats. Asvariáveis portae urlBasepoderiamsertratadascomo
constantes,poissãoatribuídasduranteainicializaçãodoprogramaenãoso-
fremalterações durantesuaexecução.Porém,emGo,nãoépossíveldeclarar
umaconstanteseminicializá-laimediatamente,eumdospontosdemelho-
riaétornarainicializaçãodoservidormaisflexível,recebendoaportacomo
argumento,porexemplo.Istoimpedequeavariávelportasejaumacons-
tantee,comoavariávelurlBasedependedovalordefinidopara porta,
elatambémnãopodeserumaconstante.
Poroutrolado,ocanal statsfoideclaradocomoglobalapenaspor
conveniência.Atualmente,elejáépassadocomoargumentoparaafun-
ção registrarEstatisticas(),oquenosdeixacomapenasumponto
demudança:precisamosinjetá-lodealgumaformanocontextodafunção
Redirecionador().
Comoestafunçãoéutilizadaparaatenderrequisições HTTPeregistrada
atravésdafunção http.HandleFunc(),eladeveobrigatoriamenteseguir
aassinaturadefinidapelotipo http.HandlerFunc.Issoimpedequeadi-
cionemosqualquernovoargumentoaestafunção.
Noentanto,opacote httpforneceumaoutraformapararegistrar han-
dlers:afunção http.Handle().Estafunçãopossuiaseguinteassinatura:
func Handle(pattern string, handler Handler)
V e j aqueosegundoargumentoédotipo http.Handler,enão mais
http.HandlerFunc.Estetipoéumainterfacequedefineapenasummé-
todo:
type Handler interface {
ServeHTTP(ResponseWriter, *Request)
}
160

## Página 175

CasadoCódigo Capítulo11.Refatorandoocódigo
Podemos então criar um novo tipo que implemente o mé-
todo ServeHTTP() e, desta forma, registrá-loatravésda função
http.Handle(). V a m o sintroduzir o tipo Redirecionador ao ar-
quivo servidor.gocomouma structvazia:
type Redirecionador struct{}
Agoravamosalterarafunção Redirecionadorparatorná-lacompa-
tívelcomotipo http.Handler.Paraisso,precisamosdefini-lacomoum
métodonotipo Redirecionador(i.e.definirotipo *Redirecionador
comoreceptordométodo),etambémarenomearpara ServeHTTP.Ocorpo
dafunçãodevepermanecerinalterado:
func (red *Redirecionador) ServeHTTP(
w http.ResponseWriter,
r *http.Request,
) {
// ...
}
Porfim, precisamos alterar a função main() para registrar o tipo
Redirecionador.V a m o salteraralinhaqueregistraarota /r/daseguinte
forma:
func main() {
// ...
http.Handle("/r/", &Redirecionador{})
// ...
}
Naprática,essasalterações não afetamofuncionamentodoservidor.
Reinicie-oefaçaalgumasrequisições paratercertezadequetudocontinua
funcionando.
Estanovaestrutura,porém,permitequenoslivremosfacilmentedocanal
comovariávelglobal. Primeiro,vamosintroduzirumcampona struct
Redirecionadorparaarmazenarocanal:
161

## Página 176

11.1.Substituindovariáveisglobais CasadoCódigo
type Redirecionador struct {
stats chan string
}
Agorapodemosremoveradeclaraçãodocanalglobal stats.
Comoestecanalécriadonafunção main(),exatamenteomesmolocal
onderegistramosotipo Redirecionadorparaatenderrequisições, pode-
mosinjetá-lonomomentodacriaçãodoobjetodotipo Redirecionador.
T a m b é mprecisamosalteraracriaçãodocanalparadeclará-locomoumava-
riávellocalàfunção main():
func main() {
stats := make(chan string)
// ...
http.Handle("/r/", &Redirecionador{stats})
// ...
}
Porfim,precisamosalterarométodoServeHTTP()paraacessarocanal
atravésdoobjetoreceptor:
func (red *Redirecionador) ServeHTTP(
w http.ResponseWriter,
r *http.Request,
) {
// ...
if url := url.Buscar(id); url != nil {
http.Redirect(w, r, url.Destino,
http.StatusMovedPermanently)
red.stats <- id
} else {
// ...
}
162

## Página 177

CasadoCódigo Capítulo11.Refatorandoocódigo
Repareque,aoenviaroidentificadordaURLparaocanal,agorautili-
zamosaforma red.stats <- id,acessandoocanalatravésdoreceptor
red.
Livramo-nosdavariávelglobal!
Nossopróximodesafioéreduziraduplicaçãodecódigo.
11.2 Reduzindo a duplicação de código
Quandointroduzimosafunção Visualizador()pararetornarasestatís-
ticasemformatoJSON,acabamoscomalgunstrechosdecódigoduplicados
entreestanovafunçãoeafunção ServeHTTPdotipo Redirecionador.
Analisandoasduascomcuidado,encontramosumpadrãocomum:am-
basextraemoidentificadorrecebidonocaminhodarequisiçãoebuscampor
umaURLcorrespondenteàqueleidentificador;casoaURLsejaencontrada,
algumaaçãoéexecutadabaseadanoobjeto urlretornado;casocontrário,
umerroHTTP404édevolvido.
Podemosextrairumafunçãoqueabstraitodaestalógicae,casoaURL
buscadasejaencontrada,executaumafunção passandooobjetoretornado
comoargumento.V a m o schamá-lade buscarUrlEExecutar():
func buscarUrlEExecutar(
w http.ResponseWriter,
r *http.Request,
executor func(*url.Url),
) {
caminho := strings.Split(r.URL.Path, "/")
id := caminho[len(caminho)-1]
if url := url.Buscar(id); url != nil {
executor(url)
} else {
http.NotFound(w, r)
}
}
Reparequeestafunçãoimplementaexatamenteamesmalógicadescrita
anteriormente. Oterceiroargumentorecebidoéumafunção denominada
163

## Página 178

11.2.Reduzindoaduplicaçãodecódigo CasadoCódigo
executor,querecebeumponteiroparaumvalordotipo url.Url(i.e.,
ovalorretornadopelafunção url.Buscar()).Estafunçãoseráchamada
casoaURLsejaencontrada.
V a m o sagora alterar o método ServeHTTP() do tipo
Redirecionadorparautilizarestanovafunção:
func (red *Redirecionador) ServeHTTP(
w http.ResponseWriter,
r *http.Request,
) {
buscarUrlEExecutar(w, r, func(url *url.Url) {
http.Redirect(w, r, url.Destino,
http.StatusMovedPermanently)
red.stats <- url.Id
})
}
Porfim,vamosalterartambémafunção Visualizador,demaneira
similar:
func Visualizador(w http.ResponseWriter, r *http.Request) {
buscarUrlEExecutar(w, r, func(url *url.Url) {
json, err := json.Marshal(url.Stats())
if err != nil {
w.WriteHeader(http.StatusInternalServerError)
return
}
responderComJSON(w, string(json))
})
}
Oresultadofinaléumcódigomaisfocadoemelhorfatorado,permitindo
quealterações namaneiracomorecebemosoidentificadordaURL,ouaté
mesmonaformacomoretornamoserrosHTTP404,sejamfeitasemum
únicolugar.
164

## Página 179

CasadoCódigo Capítulo11.Refatorandoocódigo
11.3 Escrevendo l o g s
Escreverlogsparacadaaçãorealizadaporumaaplicaçãoéumrecursoextre-
mamenteimportanteparaidentificarproblemasoumesmorastrearrequisi-
ções.
Gofornecealgunsrecursossimplesparamanipulaçãodelogsnopacote
log.
Antesdemaisnada,precisamosadicionaropacote logàlistadedepen-
dênciasdonossopacote main:
import (
// ...
"log"
// ...
)
Para facilitar, vamos criar uma função utilitária no arquivo
servidor.goparanosajudaralogaralgumasações:
func logar(formato string, valores ...interface{}) {
log.Printf(fmt.Sprintf("%s\n", formato), valores...)
}
T o d a sasmensagensimpressasatravésdasfunções dopacote logse-
rãoprecedidaspeladataehoranaqualforamescritas.V a m o sintroduziral-
gumaschamadasafunções dessepacoteaonossoservidor,começandopela
main():
func main() {
// ...
logar("Iniciando servidor na porta %d...", *porta)
log.Fatal(http.ListenAndServe(
fmt.Sprintf(":%d", *porta), nil))
}
Primeirochamamosafunção logar()paraescreverumamensagem
indicandoaportanaqualoservidoraguardaráporconexões.
165

## Página 180

11.3.Escrevendologs CasadoCódigo
Afunção http.ListenAndServe()bloqueiaaexecuçãoquandoéca-
pazdeiniciaroservidorcomsucesso.Emcasodeerro,noentanto,elaretorna
um errorqueestávamosignorandoatéagora. Envolvê-laemumacha-
madaà log.Fatal()éimportantepordoismotivos:primeiro,casoum
erroocorraaoiniciaroservidor,saberemosexatamentequalfoiacausado
erro;segundo,afunção log.Fatal()imprimeumaentradanologcon-
tendoadataehoraatuaiseamensagemdeerroespecificada(nestecaso,o
erroocorridoaoiniciaroservidor),eimediatamenteencerraaexecuçãodo
programaretornandoumcódigodeerroparaosistemaoperacional.
Porexemplo,casoumoutroprocessoservidorjátenhasidoiniciadona
porta8888,setentarmosiniciá-lonovamente,veremososeguinteerronolog:
$ go run servidor.go
2014/06/09 15:50:50 Iniciando servidor na porta 8888...
2014/06/09 15:50:50 listen tcp :8888: bind: address already in
use
exit status 1
V a m o sagoraadicionarumamensagemdelogquandoumanovaURL
curtaécriada.Paraisso,vamosincluiraseguintechamadaaofinaldafunção
Encurtador():
func Encurtador(w http.ResponseWriter, r *http.Request) {
// ...
logar("URL %s encurtada com sucesso para %s.",
url.Destino, urlCurta)
}
Apartirdeagora,quandoencurtarmosumaURL,veremosumanova
entradanolog,similaraesta:
2014/06/09 15:56:43 URL
http://casadocodigo.com.br/products/livro-ruby
encurtada com sucesso para http://localhost:8888/r/rsHj_.
Finalmente,quandoregistramosumacessoaumadeterminadaURL,
na função registrarEstatisticas() fazemos uma chamada à
166

## Página 181

CasadoCódigo Capítulo11.Refatorandoocódigo
fmt.Printf() que pode ser substituída por uma chamada à função
logar():
func registrarEstatisticas(ids <-chan string) {
for id := range ids {
url.RegistrarClick(id)
logar("Click registrado com sucesso para %s.", id)
}
}
Destaforma,quandoregistrarmosumacesso,amensagemlogadain-
cluirátambémadataehoradequandooacessoocorreu:
2014/06/09 16:08:43 Click registrado com sucesso para rsHj_.
Nossoservidoragoraimprimemensagensdelogparacadaaçãoimpor-
tanteexecutada.
11.4 Flexibilizandoa inicialização d oservidor
Paratornarnossoservidormaisflexível,éimportantequealgumasconfigura-
çõespossamsermodificadassemqueocódigopreciseseralterado.Porexem-
plo,onúmerodaportaondeoservidoraceitaráconexões. Alémdisso,agora
queintroduzimoslogs,podemostambémincluirumaconfiguraçãoparaligar
oudesligarageraçãodelogs.
Existemdiversasformasdeatingiresteobjetivo,comoousodevariáveis
deambiente,arquivosdeconfiguraçãoexternosouargumentosdelinhade
comando.
Jávimoscomoreceberetratarargumentosdelinhadecomandoanterior-
menteatravésdopacote os.Noentanto,existeumoutropacotequefornece
recursosquefacilitamotratamentodestesargumentos:opacote flag.
Parautilizá-lo,precisamosadicioná-loàlistadedependências:
import (
// ...
"flag"
// ...
)
167

## Página 182

11.4.Flexibilizandoainicializaçãodoservidor CasadoCódigo
Opacote flagprovêumasériedefunçõesutilitáriasparatratarasopções
delinhadecomando.Porexemplo,paradefinirumaopção -pquereceberá
onúmerodaporta,podemosutilizarocódigoaseguir:
porta := flag.Int("p,", 8888, "porta")
Destaforma,definimosumaopção -pquedeveserumnúmerointeiro.
Casonenhumvalorsejaespecificado,ovalor8888seráusado.Oúltimoar-
gumentodefineonomedaopção,eseráutilizadoparagerarumamensagem
deajuda.Veremosumexemploembreve.
U mdetalheimportanteéqueasfunções utilitáriasdopacote flagpara
definiropções retornam ponteiros.Portanto,paratransformarmosnossava-
riávelglobal portaemuma flag,precisamosalterarseutipopara *int.
V a m o saproveitarecriarumanovavariávelqueirádefinirseageraçãodelogs
deveráserligadaoudesligada:
var (
porta *int
logLigado *bool
urlBase string
)
Emseguida,vamosalterarafunção init()paraconfigurarasopções:
func init() {
porta = flag.Int("p", 8888, "porta")
logLigado = flag.Bool("l", true, "log ligado/desligado")
flag.Parse()
urlBase = fmt.Sprintf("http://localhost:%d", *porta)
}
Reparequeincluímosumachamadaàfunção flag.Parse().Elaefeti-
vamentelêosargumentosrecebidosnainicializaçãodoprogramaeosvalida
deacordocomasopções definidas antesdachamadaà flag.Parse().É
importantenotartambémque,deagoraemdiante,quandoprecisarmosdos
valoresreaisarmazenadosnasvariáveis portae logLigado,precisamos
168

## Página 183

CasadoCódigo Capítulo11.Refatorandoocódigo
utilizarooperadordeindireção,poiselassãoponteiros.Porestemotivo,ao
configurara urlBase,usamos *portacomoonúmerodaporta.
Seiniciarmososervidorespecificandoaopção -h,veremosamensagem
deajudageradapelopacote flag:
$ go build
$ ./encurtador -h
Usage of ./encurtador:
-l=true: log ligado/desligado
-p=8888: porta
Agora,setentarmosespecificarumaportainválida,veremososeguinte
erro:
$ ./encurtador -p=abcd
invalid value "abcd" for flag -p: strconv.ParseInt:
parsing "abcd": invalid syntax
Usage of ./encurtador:
-l=true: log ligado/desligado
-p=8888: porta
Antesdecontinuarmos,precisamosgarantirqueaplicamosooperadorde
indireçãoemtodososlugaresondeavariávelportaéutilizada.Precisamos
alterarasduasúltimaslinhasdafunção main()daseguinteforma:
func main() {
// ...
logar("Iniciando servidor na porta %d...", *porta)
log.Fatal(http.ListenAndServe(
fmt.Sprintf(":%d", *porta), nil))
}
Porfim,vamosalterarafunção logar()paraescreverasmensagens
apenasseaopção -lfoiconfiguradacomvalor true:
func logar(formato string, valores ...interface{}) {
if *logLigado {
log.Printf(fmt.Sprintf("%s\n", formato), valores...)
}
}
169

## Página 184

11.4.Flexibilizandoainicializaçãodoservidor CasadoCódigo
Inicieoservidorcomaopção -l=falseereparequenenhumamen-
sagemdelogserágerada.Demaneirasimilar,especifiquediferentesportas
atravésdaopção -pevejasetudocontinuafuncionando.
NossoservidordeURLscurtasestáfinalmentecompleto!
170

## Página 185

Capítulo12
Próximospassos
Goéumalinguagemmoderna,criadacomoobjetivoprincipaldemelhorar
aprodutividadenodesenvolvimentoemlargaescaladeservidores,baseado
nasexperiênciasdealgunstimesdentrodoGoogle.
Hoje,maisdequatroanosapóstersidoanunciadapublicamente,cada
vezmaisempresastêmadotadoalinguagemparaescreverdiversostiposdi-
ferentesdeaplicações, muitoalémdosservidores.
Enquantooconteúdoapresentadonestelivrocobrealgumasdesuas
funcionalidadesbásicas,incluindopartesimportantesdabibliotecapadrão,
aindahámuitoaseraprendido.
Para discutir sobre o conteúdoe os exemplos deste livro, participe
da lista de discussão disponível em https://groups.google.com/d/forum/
casadocodigo-go.
Alémdisso,todososexemplospodemserencontradosnoGitHub,basta
acessarhttps://github.com/caiofilipini/casadocodigo-go.

## Página 186

12.1.Aprendendomais CasadoCódigo
OprojetodoencurtadordeURLsdesenvolvidonoscapítulosfinaistam-
bémestádisponívelemhttps://github.com/caiofilipini/encurtador.
12.1 Aprendendo mais
ParacontinuaraprendendosobrealinguagemGo,vocêencontraráaseguir
algunslinksselecionados(todoseminglês):
•Siteoficial:http://golang.org/
•Índicedepacotesdabibliotecapadrão:http://golang.org/pkg/
•Especificaçãodalinguagem:http://golang.org/ref/spec
•E ff e c t i v eGo:http://golang.org/doc/effective_go.html
•Blog oficial, contendo diversos artigos interessantes: http://blog.
golang.org/
•Índicegeraldadocumentaçãooficial:http://golang.org/doc/
172

## Página 187

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1]Roy ThomasFielding. Architecturalstylesandthedesignofnetwork-
basedsoftwarearchitectures.2000.
[2] C.A.R.Hoare. CommunicatingSequential Processes.PrenticeHall,1985.
173