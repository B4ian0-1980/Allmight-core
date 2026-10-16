---json
{
  "id": "ruby_aprenda_a_programar_na_linguagem_mais_divertida_1",
  "title": "Ruby Aprenda a programar na linguagem mais divertida",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `Ruby Aprenda a programar na linguagem mais divertida.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aprenda",
    "divertida",
    "linguagem",
    "linguagens",
    "mais",
    "php",
    "programar",
    "ruby"
  ],
  "perguntas_tipo": [
    "Como utilizar Ruby Aprenda a programar na linguagem mais divertida?",
    "Quais as boas praticas de php?"
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
  "dono": "stack-php",
  "prioridade": 2
}
---

# Ruby Aprenda a programar na linguagem mais divertida

> **Arquivo Original:** `Ruby Aprenda a programar na linguagem mais divertida.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográficos,
eletrônicos mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 5

CasadoCódigo
Agradecimentos
AprimeirapessoaemaisimportantequegostariadeagradeceréminhaesposaRa-
faelaFernandes,tambémaClarinha,pelacompreensãonasváriasnoitesquetive
deixardedaraten çãoaelasparamededicaraescritadolivro.Aosmeuspaisemi-
nhairmãqueapoiarameincentivarambastanteaescritadolivrodurantetodosestes
meses.
AgradecimentosespeciaisaoPauloSilveiraeGuilhermeSilveiraquemederam
aoportunidadeímpardetrabalharnaCaelum,umasdasmelhoresempresasdetec-
nologiaparatrabalharnopaís. UmagradecimentonovamenteaoPauloSilveirae
AdrianoAlmeira,quenaQCON2012,emumaconversadepoucosminutos,me
apoiaramnaidéiadeescreverumlivrosobreRuby.
Todososamigosquetrabalhamoutrabalharamcomigonaconstru çãodonovo
CMSdoportalR7.com,foiparticipandodestetimequeaprendieensineigrande
partedascoisasqueseisobreRuby.Emespecialaosamigos:BrunoGrasselli,Elber
Ribeiro,FernandoMeyer,CaioFilipinieRafaelFerreira.
Dosamigoscitadosacima,umagradecimentoespecialaoRafaelFerreira,um
dosmelhoresdesenvolvedoresquetiveaoportunidadedetrabalhar. Umapessoa
comquemaprendoalgonovotodososdias.
Porfim,obrigadoaDeusporcolocarestaoportunidadenaminhavida.
i

## Página 7

CasadoCódigo
Q u e ms o ue u ?
MeunomeéLucasSouza,formadoemengenhariadacomputa çãonaUniverside
deRibeirãoPreto,trabalhoprofissionalmentecomdesenvolvimentodesoftwarehá
7anos. Duranteboapartedestesanos,trabalheidentrodeempresassituadasem
RibeirãoPreto,há4anosestouemSãoPaulo.Nestesanos,trabalheiprincipalmente
comJavaeRuby.
Em2005,jáprogramavautilizandoPHP,masdecidiquegostariadeaprender
outraslinguagenseopteiporaprenderJava.Rapidamentecomeceiàtrabalharcom
Java,noanode2006,partipeideumprojetoondefoipossívelaprendernãosóJava,
mastambémboaspráticasdedesenvolvimentodesoftware:testes,integra çãocon-
tínua,refatoraçãodecódigo,etc.
Noanode2008,tiveaoportunidadedeconheceraCaelum. Foiquandore-
solvimemudarparaSãoPauloapósreceberoconviteparatrabalharcomoconsul-
tor.Apósalgunsmeses,tiveaoportunidademetornarinstrutordoscursosdeJava
existentesàepoca.FuieditorchefedoInfoQBrasilporquase2anos,ondeerares-
ponsávelpelamanutenção,publica çãoerevisãodetodooconteúdotécnicodosite.
TambémparticipeidacriaçãodosnovoscursosdeHibernateeJSFdaCaelum,onde
desenvolviogostopelaescrita.Paraleloaisso,tivecontatocomváriosoutrosdesen-
volvedoresdaCaelum,quemeincentivaramaaprenderumpoucosobreRuby,que
jáeraumavontademinhanaépoca.
Em2011,recebioconviteparaserumdosintegrantesdotimeresponsávelporde-
senvolveronovoCMSdoportalR7.com,queseriaescritoprincipalmenteemRuby.
Aceiteiodesafio,edesdeentãomededicodiariamentenoaprendizadodecoisas
novasemrela çãoalinguagemRuby.Masnãosóisso,eugostoparticularmente,de
resolverproblemasrelacionadosaarquiteturaquevisammelhoraraescalabilidade
ealtadisponibilidadedoportal.
Procurosempreasmelhorasformasdeescrevercódigoslegíveisetestáveisuti-
lizandoRuby. Apesardeserumapaixonadopelalinguagemeconsiderá-laumas
iii

## Página 8

CasadoCódigo
dasmelhorescomasquaisjátrabalhei,costumocriticarseuspontosfracos,inclu-
sivenoprópriolivro.Achoquecadaproblemapossuiumalinguagemmelhorpara
resolvê-lo.
Um breve prefácio
Rubyéumalinguagemdinâmica,orientadaàobjetosequepossuialgumascarac-
terísticasfuncionais.Seucriador,YukihiroMatsumotoqueriaumalinguagemque
juntasseprogramaçãofuncionaleimperativa,masacimadetudoquefosseumalin-
guagemlegível.Estaéumadasgrandesvantagensdalinguagem,serextremamente
legível.
EstelivroébasicamenteumtutorialeumareferênciaparaalinguagemRuby.
Elecobreamaioriadascaracterísticasdalinguagemetambémsuasprincipaisapi’s:
String, Enumerable, File,etc.Alémdequestõesmaisavan çadasquepermiti-
rãoummaioraproveitamentodalinguagem,comometaprograma ção,distribui ção
decódigoegerenciamentodedependências.
P o r q u ê R u b y ?
Alémdascaracterísticascitadasacima,Rubyéalinguagemqueeuutilizoparaa
maioriadosprogramasqueescrevo,principalmentequandovoucome çaraplicações
web.Trabalhohá2anoscomRuby,epossodizerquealinguageméextramamente
produtivaesimples,consigofazercoisassimples,compoucaslinhasdecódigo.
Nosúltimosanosalinguagemprogrediuassustadoramente.Acomunidadecres-
ceubastante,possuioRubygems,ondeseencontramumgrandenúmerodeprojetos
queauxiliamodiaadiadodesenvolvedorRuby. Nogithub,agrandemaioriados
repositóriossãoescritosemRuby,oquepermitequeacomunidadecontribuacada
vezmaisparaamelhoriadoambienteemvoltadalinguagem.
Alémdisso,oframeworkMVCRubyonRails,permiteacria çãodeaplica ções
webcomextremarapidez.Essaagilidadetemsidoconsideradaporvárias startupsno
momentodacria çãodeseusprodutos.Avantageméqueonúmerodevagasdispo-
níveisnomercadocrescemacadadia,principalmenteempolosdedesenvolvimento
comoaCalifórnia.
Atualmente,aprenderapenasRailsnãoéosuficiente.Énecessárioumbomco-
nhecimentodalinguagemparacriarcódigosquefacilitemamanuten çãoecria çãode
novasfuncionalidades.AprendendomaissobrealinguagemRuby,fazcomquevocê
consigaescrevercódigosmaislegíveisedeixedeladovíciosquepodemtervindode
iv

## Página 9

CasadoCódigo
outraslinguagensquevocêtrabalhava.
v

## Página 11

CasadoCódigo Sumário
Sumário
1 Uma introdu ção prática à linguagem Ruby 1
1.1 Quando?Onde?Porquê? .......................... 1
1.2 Instalação ................................... 2
1.3 Tudopronto...mãosàmassa:Inferênciadetipos ............ 9
1.4 Tipagemforteedinâmica .......................... 1 0
1.5 Umalinguageminterpretadaecomclassesabertas ........... 1 1
1.6 OndeeuusariaRuby? ............................ 1 3
2 Seu primeiro passo no Ruby: conven ções e as diferentes estruturas primi-
tivas 15
2.1 MaistiposnoRuby ............................. 1 6
2.2 Comenteseucódigo ............................. 1 6
2.3 Otrabalhocomnúmeros .......................... 1 7
2.4 RepresentaçãodetextoscomasStrings .................. 1 8
2.5 EstruturasdeControle ...........................2 0
2.6 Entendaovalornulo ............................ 2 1
2.7 Substituao“ifnot”por“unless”...................... 2 1
2.8 Iteraçõessimplescomfor,while,until .................. 2 2
2.9 AsoutrasformasdedeclararStrings ................... 2 3
2.10 Próximospassos ............................... 2 5
3 O come ço da nossa aplicação 27
3.1 Adefini çãodaclasseLivro ......................... 2 8
3.2 Crieaestruturadoprojeto ......................... 3 3
3.3 Definaosatributosdeinstância ...................... 3 5
vii

## Página 12

Sumário CasadoCódigo
37section.3.4
3.5 Alteraçãoeleituradeatributos ....................... 3 8
3.6 Atributosnemtãoprivadosassim ..................... 4 3
3.7 Grandespoderes,grandesresponsabilidades ............... 4 3
4 Estruturas de dados 47
4.1 TrabalhecomArrays ............................4 7
4.2 Guardandonossolivros ...........................4 9
4.3 Percorrendomeuarray ........................... 5 2
4.4 Comosepararoslivrosporcategoria:trabalhecomHash ....... 5 2
4.5 Indomaisafundo:HashesnoRuby1.9 .................. 5 8
4.6 Indomaisafundo:Ooperador||= .................... 5 9
4.7 Indomaisafundo:OtipoSet ....................... 5 9
4.8 Eagora? ....................................6 4
5 Ruby e a programa ção funcional 65
5.1 Oqueéprograma çãofuncional ...................... 6 5
5.2 Funçõespuras ................................6 6
5.3 Comandosqueretornamvalores ..................... 6 7
5.4 Funçõesdealtaordem Higher-order functions..............6 9
5.5 Crieseuprópriocódigoqueusaumblocodecódigo ..........7 0
5.6 ExplorandoaAPIEnumerable ....................... 7 4
5.7 Parasabermais:Outrasmaneirasdecriarblocos ............8 0
5.8 Parasabermais:Currying .........................8 6
5.9 Parasabermais:Closure ..........................8 8
5.10 Próximospassos ...............................8 9
6 Explorando API File 91
6.1 UmpoucodaclasseFile ........................... 9 1
6.2 Serializaçãodeobjetos ........................... 9 3
6.3 Salvandoobjetosemarquivos .......................9 4
6.4 Recuperandoobjetossalvos ........................ 9 7
6.5 Próximospassos ...............................1 0 0
viii

## Página 13

CasadoCódigo Sumário
7 Compartilhando Comportamentos: Heran ça, Módulos e Mixins 101
7.1 Herança:Compartilhandocomportamentoscomclasses .......1 0 2
7.2 Herançaevariáveisdeinstância ......................1 0 6
7.3 Oscustosnousodaheran ça ........................1 1 2
7.4 Módulos ....................................1 1 6
7.5 Indomaisafundo:ConstantLookupdedentroparafora .......1 2 3
7.6 DuckTyping:opolimorfismoaplicadonoRuby ............1 2 5
7.7 HerançaouMixing?Qualdevousar? ...................1 3 0
8 Metaprograma ção e seus segredos 133
8.1 Entendaoselfemethodcalling ......................1 3 4
8.2 Oimpactodoselfnadefini çãodeclasses .................1 3 6
8.3 SingletonClasseaordemdabuscademétodos .............1 3 8
8.4 Indomaisafundo:AcessandoaSingletonClass .............1 4 2
8.5 Metaprogramaçãoeasdefini çõesdeumaclasse .............1 4 4
8.6 Criandoumframeworkparapersistirobjetosemarquivos ......1 5 3
8.7 Gerenciandoexce çõeseerros .......................1 5 9
8.8 Aexclusãodedadosimplementadacommetaprograma ção ......1 6 4
8.9 method lookupe method missing......................1 7 7
8.10 Utilizandoexpressõesregularesnasbuscas ................1 8 8
8.11 Próximospassos ...............................1 9 4
9 As bibliotecas no universo Ruby 197
9.1 ComomanusearsuasgemscomoRubygems ..............1 9 7
9.2 Gerenciandováriasversõesdeumagem .................2 0 0
9.3 GerenciedependênciascomoBundler ..................2 0 1
9.4 Quemusa b u n d l e r? .............................2 0 4
9.5 Criandoedistribuindogems ........................2 0 4
9.6 Distribuiçãodabiblioteca ..........................2 0 5
9.7 Próximospassos ...............................2 0 8
10 Criando tasks usando Rake 209
10.1 Parâmetrosnaraketask ...........................2 1 2
10.2 Taskscompré-requisitos..........................2 1 5
10.3 Próximospassos ...............................2 1 7
ix

## Página 14

Sumário CasadoCódigo
11 RVM (Ruby Ve r si o nManager) 219
11.1 Instalação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
11.2 InstalandodiferentesRubies . . . . . . . . . . . . . . . . . . . . . . . . 221
11.3 Organizesuasgemsutilizandogemsets. . . . . . . . . . . . . . . . . . 222
11.4 Troqueautomaticamentedegemsetscom.rvmrc . . . . . . . . . . . .224
11.5 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225
12 Ruby 2.0 227
12.1 EvitandomonkeypatchescomRefinements. . . . . . . . . . . . . . .228
12.2 NamedParameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .230
12.3 Utilizeprependaoinvésdeinclude . . . . . . . . . . . . . . . . . . . . 233
12.4 UtilizandolazyloadnomóduloEnumerable . . . . . . . . . . . . . . 235
12.5 EncodingUTF-8. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
12.6 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
13 Apêndice:Concorrênciae paralelismo 239
13.1 Threads . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
13.2 Múltiplosprocessos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
13.3 Fibers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .242
13.4 Odesignpattern Reactor . . . . . . . . . . . . . . . . . . . . . . . . . .243
13.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .244
x

## Página 15

Capítulo1
U m a i n t r o d uçãopráticaàlinguagem
R u b y
Vamoscomeçarcomumpoucodahistóriaecaracterísticasimportantesdalingua-
gemRuby,paracompará-lacomcomoutrasquevocêjádevetertrabalhado.Tam-
bémmostraremosoporquêváriosprogramadorestêmfaladoeusadotantoestalin-
guagem,pelaqualesperoquevocêseapaixonará.
1.1 Q uando? Onde? Por quê?
AlinguagemRubyfoicriadaporYukihiroMatsumoto,maisconhecidocomoMatz,
noanode1995noJapão,comoobjetivodeserumalinguagemmaislegíveleagra-
dáveldeseprogramar.
Mas,alémdascaracterísticasorientadaaobjetos,Rubytambémfoicriadapara
possuirumfortequêdelinguagemfuncional,tendorecursospoderososeessenciais
desseparadigma,comolambdase c l o s u r e s.

## Página 16

1.2. Instalação CasadoCódigo
ElafoiinspiradaemoutraslinguagenscomoPerl,SmalltalkeLisp,ehojeestá
entreaslinguagensmaisusadas,muitoemfun çãodadissemina çãodoseuprincipal
fr a mewo r kMVC,oRubyonRails- http://rubyonrails.org.
AlgumascaracterísticasdoRubydevemserfixadasdesdeocome çodosestudos,
poisvãofacilitarbastantenossacurvadeaprendizadodalinguagem,comoatipagem
forteedinâmica,alémdofatodalinguagemserinterpretada.Fiquetranquilocaso
vocêaindanãotenhaescutadofalarsobreessesalgunsdessesconceitos.
1.2 I nstalação
Em2013,oRubysepreparaparareceberaversão2.0dalinguagem. Emfevereiro
jásaiuumaprimeiraversão,masaindapoucoutilizada. Háumapêndicenesseli-
vroparavocêfazerainstala çãodessaversãomaisrecente,quetrazrecursosnovos,
tambémdiscutidosnofimdolivro.
Nessa seçãovamosaprenderainstalaroRubyemcadasistemaoperacional:
Ma c O S
Adivinhe?NoMacOS,ointerpretadorRubyjáestáinstalado!Abraoterminal
eexecute:
ruby -v
NaversãoMountainLion,aversãopré-instaladaéa1.9.2patch290,conforme
vocêpodevernaimagemaseguir:
2

## Página 17

CasadoCódigo Capítulo1. UmaintroduçãopráticaàlinguagemRuby
ORubypossuiváriosinterpretadoresdisponíveis,sevocêdesejautilizarversões
maisnovasquenãoestãodisponíveisdiretamenteapartirdoseusistemaoperacio-
nal,existemgerenciadoresdeversõesdoRuby,porexemplo,oRVM(RubyVersion
Manager). Noapêndice“GerenciadoresdeversõesdoRuby”explicareicomoelas
funcionamecomoinstalá-las.
Linux
SevocêforumusuárioLinux,asdistribui çõesemsuamaioria,disponibilizam
algunsinterpretadoresRuby.Casovocêestejausandoaversão12.04doUbuntu,que
éamaisrecente,bastainstalaropacotedointerpretadorRubyutilizandoo apt-get
install.Abraumterminaleexecuteocomando:
sudo apt-get install ruby1.9.3
3

## Página 18

1.2. Instalação CasadoCódigo
Agoravocêpodeconferiraversãoinstaladaexecutandoemumterminal:
ruby -v
Evocêveránasaídadoterminal,algocomo:
4

## Página 19

CasadoCódigo Capítulo1. UmaintroduçãopráticaàlinguagemRuby
Windows
CasooseusistemaoperacionalsejaWindows,amaneiramaissimplesefácilé
utilizarumasdasversõesdoRubyInstaller,quepermitequevocêfa çaainstala ção
comapenasalgunscliques.
OprimeiropassoébaixaraúltimaversãodoRubyInstaller.Paraisso,acesseo
site:
http://rubyinstaller.org/downloads/
Baixeaversão Ruby-1.9.3-p194,umarquivoexecutávelqueinstalaráauto-
maticamenteointerpretadorRubyemsuamáquina.Quandoodownloadterminar,
executeoarquivo Ruby-1.9.3-p194.exe.
Cliqueemexecutarparaprosseguircomainstala ção.
5

## Página 20

1.2. Instalação CasadoCódigo
Emseguida,cliquenobotão I accept the Licenseeemseguidanobotão A v a nça r.
Agoramarqueasop ções Add Ruby executables to your PATHparapoderposteri-
ormenteexecutaroRubyapartirdeumterminal.Marquetambémaop ção Associate
.rb and .rbw file with this Ruby installationparaqueosarquivos .rbsejaminterpre-
tadoscomoarquivosquecontémcódigoRuby.Porfimcliquenaop ção install.
6

## Página 21

CasadoCódigo Capítulo1. UmaintroduçãopráticaàlinguagemRuby
Ainstalaçãoseráfeitanodiretórioselecionadonatelaanterior.
7

## Página 22

1.2. Instalação CasadoCódigo
Ainstalaçãoserácompletadacomsucesso. Parafinalizarbastaclicarnobotão
::Finish’.
Paratestarqueainstala çãofoifeitacomsucesso,abraumterminaleexecuteo
comando ruby -vevejaqueoRubyfoiinstalado:
8

## Página 23

CasadoCódigo Capítulo1. UmaintroduçãopráticaàlinguagemRuby
1.3 T udo pronto ... mãos à massa : Inferência de tipos
Umdosconceitosbásicosemlinguagensdeprograma çãoéadeclara çãodevariáveis,
queéapenasumaassocia çãoentreumnomeeumvalor.EmRuby,bastadefinirmos
onomedavariáveleatribuirumvalorusandoosinal =:
idade = 27
Ocódigoacima,deveserexecutadodentrodoIRB( Interactive Ruby Shell),um
pequeno s h e l lquepermitequecódigosRubysejamcriadosetestados. Comoos
códigosdosprimeiroscapítulossãosimples,vamostestá-losdentrodoIRB.Para
executá-lo,bastadigitarirbnoterminaldesuapreferênciaounoconsoledoWin-
dows.
OutraformadecriareexecutarcódigoRubyécriandoumarquivo .rbe
executá-loutilizandoocomando ruby. Seocódigoacimafossedigitadodentro
deumarquivo idade.rbparaexecutá-lofaríamos:
ruby teste.rb
Duranteosprimeiroscapítulosdolivro,utilizaremosoIRB,conformeoscódigos
ficaremcomplexos,épreferívelqueelessejamcriadosdentrodearquivos%.rb
Aoexecutarmosocódigo,estamosdefinindoumavariávelchamada idadee
atribuindoovalor 27.Masqualotipodestavariável?Nãoénecessáriodeclararmos
sealiseráguardadoumnúmero,umtextoouumvalorbooleano?
Avariávelquecriamosédotipo Fixnum,umtipoespecialdoRubyquerepre-
sentanúmerointeiros. Masnãodeclaramosessainforma çãonavariável idade.
Sendoassim,comoRubysabequeotipodavariávelénumérico?
Aocontráriodeoutraslinguagens,comoC,ondeénecessáriodeclararmosotipo
davariável,nalinguagemRubyissonãoénecessário,poisointerpretadorinfereo
tipodavariávelautomaticamenteduranteaexecu çãodocódigo.Estacaracterística
éconhecidacomoinferênciadetipos.
Teste seus códigos online
Sevocêestivercomumpoucomaisdepressaequisertestaroscódigos
deexemplologo,vocêpodeusarosite http://tryruby.org.Elefunciona
comoumIRB,porém,dentrodoseu browserfavorito. Extremamente
útilparaquandovocêquerfazerumtesterápido,masestáemumcom-
putadorquenãotenhaoRubyinstalado.
9

## Página 24

1.4. Tipagemforteedinâmica CasadoCódigo
Paraverificardequetipoéavariável idade,bastaexecutarocódigoabaixo:
idade = 27
puts idade.class
Quandoinvocamos .classemqualquervariável,ointerpretadorRubyretorna
otipodavariável,queseráimpressanoIRBpelométodo puts.Nestecaso,otipo
retornadoé Fixnum.
1.4 T ipagem forte e dinâmica
Seeunãodeclaroqualotipodaminhavariável,querdizerqueotipodelanãoim-
portaparameuinterpretador?
ParaalinguagemRuby,arespostaé não.Eestadefini çãoéumadasquecausa
maisconfusãonacabe çadaspessoasqueestãocome çandoaprogramaremRuby.
Porserumalinguagemcominferênciadetipos,muitospensamqueotiponãoim-
portaparaointerpretadorcomoacontececomoPHP.Confuso?Vamosverissona
prática.
SecriarmosduasvariávelemumcódigoPHPqualquer,sendoumacontendo
uma String,comovalor 27eoutrodetiponuméricocomvalor 2:
<?php
$idade = 27 ;
$multiplicador = "2";
$idade * $multiplicador;
?>
Aoexecutarmosocódigoacima,oresultadoserá 54.Paraointerpretadordo
PHP,quandoexecutamosumaopera çãomatemáticaenvolvendoumavariáveldo
tipo inteumadotipo String,osvaloresdasvariáveispodemserautomatica-
menteconvertidosparaoutrostipos,afimdepossibilitaraopera ção.
SeexecutarmosexatamenteomesmocódigoemRuby:
idade = 27
multiplicador = "2"
idade * multiplicador
10

## Página 25

CasadoCódigo Capítulo1. UmaintroduçãopráticaàlinguagemRuby
Opa!Nãofuncionou.Ointerpretadorretornou TypeError: String can't
be coerced into Fixnum.ORubynãopermitequeumavariável Fixnumseja
somadacomoutradotipo String,diferentementedoqueocorrenoPHP,que
permiteestetipodeopera ção. IssoaconteceporqueparaointerpretadorRubyé
impossívelmultiplicarumnúmerocomumtexto.
Essacaracterísticadalinguagemderealizaropera çõesemvariáveisdetiposdi-
ferenteséoquechamamosdetipagemfracaouforte.NocasodoRuby,ondeotipo
édeterminanteparaosucessodaopera ção,dizemosque a linguagem tem tipagem
f o r t e.
Tendoatipagemforteemmente,vamosirmaisalém.Executeoseguintecódigo:
idade = 27
idade = "27"
Funcionou?
Estecódigofuncionanormalmente,porquenãoestamosfazendonenhumaope-
raçãoquemistureostipos. Ocódigoacimaapenasatribuium Fixnumàvariável
idadeedepoisatribuiumoutrovalor,sóquedotipo String.Quandoalinguagem
permitequeotipodavariávelpossaseralteradoduranteaexecu çãodoprograma,
dizemosque ela tem tipagem dinâmica.
Emcontrapartida,outraslinguagenspossuemtipagemestática,ouseja,umavez
queavariávelécriadacomoum int,elasópoderáserum int.Esseéocasodo
Java,ondeocompiladorcuidadefazeressachecagem.
Estaéumadascaracterísticasmaiscriticadaspelosdesenvolvedoresqueprefe-
remlinguagenscomtipagemestática,umadasalega çõeséqueemlinguagemcom
tipagemestáticaspodemosdescobrirerrosduranteacompila ção.Porém,veremos
duranteolivroqueatipagemdinâmicaéumadascaracterísticasmaispoderosasda
linguagem,trazendotamb;emmuitosbenefícios.
Valelembrarqueosconceitosforte,fraca,dinâmicaeestáticanãosãotãosimples
assim.Émaisfácilfalarseumalinguagemémaisouentãomenosfortementetipada
queoutra,porexemplo.Nessecapítuloapenastocamosdelevenesseassunto.
1.5 U ma linguagem interpretada e com classes aber -
t a s
Rubyéumalinguageminterpretada,ouseja,nãoexisteumprocessodecompila ção
paraumbinárioexecutável,comoacontecenalinguagemC,porexemplo.EmRuby,
11

## Página 26

1.5. Umalinguageminterpretadaecomclassesabertas CasadoCódigo
existeumarquivocomaextensão .rbeumprogramacujopapeléinterpretaro
conteúdodestearquivo,transformando-oeminstru çõesdemáquinaeexecutando
ocomportamentoesperado.
Vamosparaumexemplopráticoqueprecisamosresolver:descobriropluralde
todasaspalavras,porexemplo.
Umcaminhonaturalparasolucionaresteproblema,écriarummétodoquere-
cebeuma Stringcomoentradaeadicioneum sapósasuaúltimaletra(sim,estou
pensandoapenasnoscasosmaissimples).
Vamosaocódigoquesolucionaesteproblema:
def plural(palavra)
"#{palavra}s"
end
puts plural("caneta") # canetas
puts plural("carro") # carros
Nãosepreocupeaindacomosignificadodo #dentroda Stringnométodo
plural,vamosfalarbastantedeladuranteolivro.O putséummétodosimples
quepegaoargumentopassadoejogaparaasaídapadrão.DentrodoIRB,bastaria
escrever plural("caneta")queautomaticamenteointerpretadorjogaoresul-
tadonoconsole.Fa çaoteste!
Olhandoestecódigocomcuidado,elenãonosparecerátãoorientadoaobjetos
assim. Reparequeosdadoseoscomportamentosestãoseparados,maspodemos
tentarmelhorarisso. Jáqueométodo pluralagesomentenaprópria String,
nadamaisnaturalqueeleestejanaclasse String,assimusaríamos:
puts "caneta".plural
puts "carro".plural
Porém,aoexecutarmosocódigoacimareceberemososeguinteerrocomore-
torno:
NoMethodError: undefined method `plural' for "caneta":String
Isso significa que objetos do tipoString não possuem o comportamento
plural. Masesperaaí... eseescrevêssemosométodo pluraldentrodaclasse
String?
12

## Página 27

CasadoCódigo Capítulo1. UmaintroduçãopráticaàlinguagemRuby
class String
def plural
"#{self}s"
end
end
AgoratenteexecutarocódigoquecolocaaString“caneta”noplural:
puts "caneta".plural # canetas
Agorafunciona!Oquefizemosfoi“abrir”aclasseString duranteaexecução
docódigoeadicionamosumnovométodoqueestarádisponívelparatodososob-
jetosdotipo Stringqueexistem.Esserecursoéconhecidocomo classes abertas
(OpenClasses),recursoqueveremosbastanteaindaduranteospróximoscapítulose
discutiremosbastantesuasvantagensedesvantagens.
Porenquanto,éimportantetermosemmentealgunsproblemasemrela çãoa
linguagensinterpretadas.Umdessesproblemasénãoconseguirmosdescobrirerros
doprogramadorduranteacodifica çãodoprograma,masapenasquandotentamos
executá-lo,jáquenãotemosumcompiladorqueconseguechecarporerrospara
nós.Paracontornaresseproblema,osdesenvolvedoresRuby,desdecedo,mantémo
hábitodedesenvolvertestesdeunidadeparasuasclasses,afimdetentardescobrir
possíveiserrosexistentesnoprogramaomaisrápidopossível.
1.6 O nde eu usaria Ruby?
ÉmuitocomumencontraralinguagemRubysendousadaparaacria çãodescripts
paralereprocessararquivos,automatizarbuildsedeploys,fazer crawlingdesites
etc.
MassemdúvidasosmaiorescasesdesucessodalinguagemRubyestãoliga-
dosaaplica çõesweb.Acria çãodoRailssemdúvidasfoioquemaisalavancouo
sucessodalinguagem.EleéumframeworkwebquesegueopadrãoMVC( Model-
View-Controller)eevangelizao Convention over configuration,ouseja,acabarcom
aquelaquantidadeenormedeXMLsqueexistemnamaioriadosframeworksweb
queexistemnomercadoequedificultammuitoamanuten ção.
Surgiudentrodaempresa37signalsefoicriadoporDavidHeinemeierHansson,
queresolveuextrairpartedalógicawebdeumprojetochamadoBasecamp. Exis-
temvárioscasesdesucessonawebcomoopróprioBasecamp,AListApart(revista
13

## Página 28

1.6. OndeeuusariaRuby? CasadoCódigo
comdicasdedesenvolvimentodeaplica çõesweb),Groupon(Maiorsitedevendas
coletivasdemundo),etc.
ExistemtambémváriosSaaS(SoftwaresasaService)disponíveisqueforamcri-
adosemRailsequepermitemacria çãodeaplica çõesemminutos.OShopifyéum
delesepermiteacria çãodesuapróprialojavirtual,comtemplatepersonalizado,
listadeprodutos,pagamentoemcartãodecrédito,issotudocomapenasalgunscli-
ques.Alémdevislumbrarousonacria çãodasuapróprialoja,vocêpodepensarem
criaroseupróprioSaaSusandoRailscombastanterapidez.
FoioqueopessoaldaMailChimpfez.Elescriaramumservi çoqueajudavocêa
criarodesigndoseue-mailde newsletters,compartilhá-loemredessociaiseintegrar
comoutrosservi çosquevocêjáutiliza.Tudoissocompoucoscliques.
OimportanteéqueomercadoemtornodalinguagemRubyémuitogrande
atualmente,eatendênciaéquecontinuecrescendonospróximosanos.Sãovárias
asvagasexistentesparatrabalharcomRubye/ouRailsatualmente.Váriosservi ços
estãosendocriadoseumagrandequantidadedeStartupsapostamnalinguageme
nassuasaplica ções.
TenhaemmentequeoquantomaisvocêdominaralinguagemRuby,maisfácil
seráparavocêconhecerprofundamenteosframeworkscomooRailseasdiversas
bibliotecasrelacionadas.
Vamoscomeçarnossajornada?
14

## Página 29

Capítulo2
SeuprimeiropassonoRuby:
convençõeseasdiferentesestruturas
primitivas
AcabamosdeaprenderumpoucosobreoRuby,escrevemosjáalgumcódigo,osufi-
cienteparaquepudéssemosfazerum“olámundo”eentenderalgunsdosconceitos
portrásdalinguagem.
Antesdecriarumaaplica ção,quecome çaráaserescritanopróximocapítulo,
precisamosnosacostumarcomalgumassutilezasdalinguagemetambémcomases-
truturasbásicas.Vamosaprendermaissobreostiposexistentesnalinguagem,como
representarausênciadevalores,asdiferentesmaneirasdeescreverasestruturascon-
dicionaisetambémosloops.
UmaboadicaécontinuartestandoosnossoscódigosnoIRB,etambémexperi-
mentandosuascuriosidadesparaobterdiferentesresultados.

## Página 30

2.1. MaistiposnoRuby CasadoCódigo
2.1 M ais tipos no Ruby
Comovimosnocapítuloanterior,adeclara çãodevariáveisemRubyéumprocesso
bastantesimples,bastandoescolheronomedasuavariáveleatribuirumvalorpara
ela.Estejaatento,poisdeveserrespeitadaaregradecome çá-lascomletras, $ou _.
1 = "Lucas" # não funciona
nome = "Lucas" # funciona
$nome = "Lucas" # funciona
_nome = "Lucas" # funciona
Masequandonossavariávelpossuinomescompostos? Emalgumaslingua-
genséconvencionadoquecadapalavraqueformaráoidentificadordavariávelco-
mececomletramaiúscula,excetoaprimeira,porexemplo, telefoneCelular,
ouentão numeroDeRegistro. Essaconvençãoéconhecidacomo Camel Case.
EmRuby,utilizamosoutraconven çãoparasepararaspalavras.Nela,usamossem-
preletrasminúsculasecomoseparadoro _,dessaformapoderíamosteravariável
telefone_celular.
telefone_celular = "(11) 91234-5678"
2.2 C omente seu código
Sevocêestavaatento,deveterreparadoquealgumasvezesutilizamosuma #no
códigoquemostravaosdiferentesexemplosdedeclara çãodevariávelemRuby.Es-
távamosnaverdadefazendoumcomentário. Esseéoconhecidocomentáriode1
linha.Assim,seexistiremNlinhasevocêdesejecomentartodaselas,teráqueadi-
cionar #linhaporlinha.
#idade = 27
#ano = 2013
Paraessescasosondeprecisamoscomentardiversaslinhas,podemosutilizaros
comentáriosembloco,quepodemserfeitosusandoenvolvendooconteúdoaser
comentadoentreasdemarca ções =begine =end.
=begin
idade = 27
ano = 2013
=end
16

## Página 31

CasadoCódigo Capítulo2. SeuprimeiropassonoRuby:conven çõeseasdiferentesestruturas...
Comisso, essescódigosserãodesconsideradosnainterpreta çãodoseupro-
grama.
2.3 O trabalho com números
Emqualqueraplica çãoqueédesenvolvida,emalgummomentodeve-setrabalhar
comnúmeros.Muitasdasinforma çõespodemserrepresentadascomumnúmero
inteiro,como idade, anoou quantidade_estoque,porexemplo.Nessecaso,
declaramosavariávelcomonúmero:
idade = 27
ano = 2013
Aotrabalharmoscomnúmerosinteiros,podemosdescobrirseutipopergun-
tandoparaavariávelqualéasuaclasse:
idade.class
=> Fixnum
Repareque => Fixnumnãoprecisaserdigitado,eleapenasindicaqualseráa
saídadoIRB.Aolongodolivro,utilizareiestaabordagemparaindicarqualoretorno
deumachamadadentrodoIRB,facilitandosualeitura.
Númerosinteirosgeralmentesãodotipo Fixnum,excetoemcasosextrema-
mentegrandesondeo Bignuméempregado.Noentanto,númerosmuitograndes
equeprecisamosrepresentardeformaliteralpodemficarcomplicadosdelerno
código. Porexemplo,aquantidadedehabitantesnomundoem2013,poderíamos
fazer:
habitantes = 7000000000
7bilhõesdehabitanteséumnúmeroconsideravelmentegrande.Masesefosse
70bilhões?
habitantes = 70000000000
Reparequenãoétãofácilperceberqueháumzeroamaisnessegrandenúmero.
Paraessescasos,Rubynospermitesepararosmilharesatravésdo%_
habitantes = 7_000_000_000
17

## Página 32

2.4. RepresentaçãodetextoscomasStrings CasadoCódigo
Comissoconseguimosdeixaronúmeroliteralmaislegível.
Emoutrassitua ções,podemosprecisardefinirnúmerosquetenhamcasasdeci-
mais.Porexemplo,pararepresentaropesodeumapessoa:
peso = 77.9
Reparequeasepara çãodascasasdecimaiséo .(ponto)enãoa ,(vírgula).
2.4 R epresentação de textos com as Strings
Muitasdasvezesprecisamosdevariáveisqueguardeminforma çõesquesãocompos-
tasportexto,comoonomedeumapessoaeseuidentificaremalgumaredesocial.
Essetipodeinforma çãoéoquechamamosde String.EmRuby,qualquercarac-
tereouconjuntodecaracterescercadodeaspassimplesouduplaséconsideradouma
String:
nome_completo = "Lucas Souza"
twitter = '@Lucasas'
puts nome_completo.class # => String
puts twitter.class # => String
Masporqualmotivoequandoeuuso Stringcomaspassimplesouduplas?
ImaginequevocêpossuiumaamigachamadaJoanad’Arceprecisamosarmaze-
naronomedelaemumavariável:
nome_com_aspas_simples = 'Joana d 'Arc' # não funciona
nome_com_aspas_duplas = "Joana d 'Arc" # funciona
Reparequequandodefinimos Stringcomaspassimples,nãoconseguimos
adicionaroutraaspassimplesdentrodotexto,poisdessaformaéointerpretador
nãosabeondeficaofinalda String.Nestecasooúnicojeitoéusaraspasduplas.
MasexistemoutroscasosondeStringscomaspasduplassãomaisinteressantes.
Precisamosagoraexibirumamensagemdeboas-vindascontendoonomedapessoa
queestádefinidodentrodavariável nome.Omaisnaturalseriarepetirocompor-
tamentodeoutraslinguagenseusarooperador +pararealizarumaconcatena ção.
nome = "Joana d 'Arc"
boas_vindas = "Seja bem-vinda(o) " + nome
puts boas_vindas # => Seja bem-vinda(o) Joana d 'Arc
18

## Página 33

CasadoCódigo Capítulo2. SeuprimeiropassonoRuby:conven çõeseasdiferentesestruturas...
PorémemRubyquandoprecisamosconcatenarduas String,preferimosfazer
ousodainterpola ção:
nome = "Joana d 'Arc"
boas_vindas = "Seja bem-vinda(o) #{ nome}"
puts boas_vindas # => Seja bem-vinda(o) Joana d 'Arc
Bastacolocardentroda Stringavariáveldentrode #{variavel}. Éuma
maneiramaiseleganteecomumdeserusadaemcódigosRuby.Odetalheéqueem
Stringdefinidascomaspassimplesnãoépossívelfazerusodainterpola ção.
Prefirasempreousode Stringcomaspasduplasepriorizesempreainterpo-
laçãoquandoforconcatenar.
Existe diferença de performance entre String com aspas simples e duplas?
Existemuitadiscussãosobrequaltipodedeclara çãode Stringdevemosuti-
lizar,comoargumentoqueadeclara çãocomaspassimplessãomaisrápidasqueas
declaraçõescomaspasduplas.
As Stringdeclaradascomaspassimplespodemsersutilmentemaisrápidas
queasdeclaradascomaspasduplasporqueoanalisadorléxicodalinguagemRuby
nãotemquechecarseexistemmarcadoresdeinterpola ção #{}.Estenúmeropode
variardeinterpretadorparainterpretadorevaleressaltarqueestetemposeriamenos
duranteoparserdocódigoenãoduranteaexecu çãodomesmo.
Adiferençaétãoinsignificantequenãovaleapenaperdermostempocomesse
tipodecompara ção.Euparticularmenteprefirodeclará-lassemprecomaspasdu-
plas,porqueseemdeterminadomomentoeuprecisarinterpolarovalordealguma
variáveldentrodesta String,elajáfoicriadadeumamaneiraquenãopreciso
alterá-la.
Aúnicapreocupaçãoquedevemosterécomoquevamosinterpolardentrode
uma String.Porexemplo:
puts 'mensagem' # => mensagem
puts "#{sleep 1}mensagem" # => mensagem
A Stringdeclaradacomaspasduplasinterpolaachamadadeummétododa
classe Kernelqueinterrompeaexecu çãodocódigopor1segundo,ouseja,otempo
paraimpressãodasegunda String mensagemserádepelomenos1segundo.
19

## Página 34

2.5. EstruturasdeControle CasadoCódigo
2.5 E struturas de Controle
Rubypossuiasprincipaisestruturasdecontrole( if, whileetc)assimcomoas
linguagensJava,CePerl. Porémaocontráriodestasqueusamchaves {e }para
definiroconteúdodaestrutura,emRubyusa-seaspalavrareservada endapenas
parafinalizarocorpodaestrutura.
Supondoquedesejamosimprimirconteúdodavariável nomeapenassea idade
formaiorque 18,usamosaestrutura if,queemRubypossuiaseguintesintaxe:
idade = 27
nome = "Lucas"
if(idade > 18 )
puts nome # => Lucas
end
UmamaneiradedeixarocódigoRubyaindamaissimpleséremovendoospa-
rêntesesdachamadado if.
idade = 27
nome = "Lucas"
if idade > 18
puts nome # => Lucas
end
UmadasvantagensdoRuby,équenamaioriadasvezespodemosomitirouso
dosparenteses. Issoéoquechamamosde S y n t a x S u g a rou “açúcarsintático”da
linguagem,quevisadeixarocódigomaislegível.
Falandoemdeixarocódigomaislegível,seocorpodoseu %ifpossuirapenas
umalinha,prefiraumasintaxemaisenxuta:
idade = 27
nome = "Lucas"
puts nome if idade > 18 # => Lucas
Reparequeparecequeestamoslendoumtextoeminglês: “Imprimanomese
aidadeformaiorque18”. Estaéumadasgrandesvantagensdalinguagem,maior
legibilidadesemprequepossível.
20

## Página 35

CasadoCódigo Capítulo2. SeuprimeiropassonoRuby:conven çõeseasdiferentesestruturas...
2.6 E ntenda o v alor nulo
QuandodesejamosrepresentaralgumvalorvazioemRuby,usamosapalavrareser-
vada nil. Onilnãorepresentauma Stringvaziaouonúmerozero,elere-
presentaumvalorvazio,umespa çovazio.Quandoatribuímos nilaumavariável,
queremosdizerqueelanãopossuinenhumvalor.
caixa = nil
Anossavariável caixa,nãopossuinadadentrodela,ouseja,évazia.
Nestecontexto,podemosimprimirumamensagemdeboasvindascasoocon-
teúdodavariávelnometenhaalgumvalornãonulousandoométodo nil?:
nome = "Lucas"
puts "Seja bem-vindo #{ nome}" if not nome.nil? # => Seja bem-vindo Lucas
Seexecutarmosocódigoacima,amensagem‘Sejabem-vindoLucas’seráexi-
bida.Masenocasodavariávelpossuirovalor nil:
nome = nil
puts "Seja bem-vindo #{ nome}" if not nome.nil?
Nestecasonenhumamensagemseráexibida,avariável nomeénulaeométodo
nil?retorna true.Comofazemosanega çãousandoo notovaloréinvertidoe
portanto false.
Umpoucocomplicado,nãoé?Vocêvaiseacostumarrapidamente.
2.7 S ubstitua o “if not ” p o r“unless ”
Podemossimplificarocódigoacimausandoacondicionalnegada,o unless(“a
menosque”,nobomportuguês).
nome = nil
puts "Seja bem-vindo #{ nome}" unless nome.nil?
Podemoslerocódigo:“Imprima‘Sejabemvindo...’amenosqueonomeseja
nulo”.Namaioriadasvezesqueimplementamosum if not,elepodeserconver-
tidoparaum unless.
Eseeudisserquepodemosmelhoraraindamaisonossocódigo.Interessante,
não?Poisé,existealgoquevocêaindanãosabesobreasvariáveiscomvalor nil.
Seusadasdentrodecondicionaiscomo ife unlessavariávelquando nil
assumeautomaticamenteovalor trueenocasocontrário,assumeovalor false.
21

## Página 36

2.8. Iteraçõessimplescomfor,while,until CasadoCódigo
nome = nil
puts "Seja bem vindo #{ nome}" if nome
Avariável nomepossuiovalor nileassumeovalor falsenacondicional
anterior,sendoassimnenhumamensageméimpressanoterminal. Seavariável
possuiralgumvalornão nil:
nome = "Lucas"
puts "Seja bem-vindo #{ nome}" if nome # => Seja bem-vindo Lucas
Amensagem Seja bem-vindo Lucaséimpressa,poisavariávelnãoé nilepor-
tantoassumeovalor true.
2.8 I terações simples com for , while, until
F o r
Existemdiversasformasdeiterarumdeterminadonúmerodevezesporumcódigo
Ruby.Comoemoutraslinguagens,existemosconhecidos while, untile for.
Semdúvida,amaneiramaisusadaemcódigosRubyquevocêirásedepararaolongo
dotempoéo for.
Desejamosimprimirosnúmerosde1até100.Apenasadicionandoumamensa-
gem‘Numero:X’paradeixarmosnossasmensagensmaiselegantes.
for numero in (1..100)
puts "Numero: #{ numero}"
end
Ocódigoacimaatribuiàvariável numeroosvaloresde1até100,executaa
conteúdodo forqueterminaquandousamosapalavrareservada end.Odetalhe
maisimportantedocódigoacima,é (1..100),quecriaumrangedenúmerode1
até100,queéexatamenteonúmerodevezesquedesejamosexecutaraimpressãode
umnúmero.
Wh i l e
Podemosutilizariterarde1até100imprimindocadaumdosnúmerosutilizando
aestruturaderepeti ção while,queassimcomoemlinguagenstradicionaiscomo
JavaeC,executandoumblocodecódigoatéqueumadeterminadacondi çãoseja
falsa(conteúdoquetambémédelimitadopelapalavrareservada end).
22

## Página 37

CasadoCódigo Capítulo2. SeuprimeiropassonoRuby:conven çõeseasdiferentesestruturas...
numero = 0
while numero <= 100
puts "Numero: #{ numero}"
numero += 1
end
Quandoforexecutadoocódigoacimaexecutaráaimpressãodamensagem‘Nu-
mero:x’imprimindode1até100,quandoacondiçãodo whileseráfalse.
U n t i l
Aocontráriodo whilequeterminasuaexecu çãoquandoumacondi çãofalsa
sejaalcançada,aestruturaderepeti ção untilexecutaumdeterminadoblocode
códigoatéqueumacondi çãoverdadeirasejaencontrada:
numero = 0
until numero == 100
puts "Numero: #{ numero}"
numero += 1
end
Adiferençaéqueocódigoacimaexecutaráaimpressãodamensagem‘Numero:
x’de1até100,atéqueovalordavariável numeroseja100eocorraotérminona
execuçãodo until.
2.9 A s outras formas de declarar Strings
Aprendemosediscutimosduasformasdedeclarar String:
aspas_simples = 'linguagem_ruby'
aspas_duplas = "linguagem_ruby"
Mascomoprocedercasoprecisemosdeclarar Stringcomaspasduplaseaspas
simplesdentro,porexemplo: "Isso é “normal” e ‘útil’ no mundo Ruby”.Nenhumadas
duasabordagensanteriorresolvemoproblemasemousodocaracteredeescape \.
string_especial_usando_aspas_simples =
'Isso é "normal" e \ 'util\' no mundo Ruby '
string_especial_usando_aspas_duplas =
"Isso é \"normal\" e 'util' no mundo Ruby"
23

## Página 38

2.9. AsoutrasformasdedeclararStrings CasadoCódigo
puts string_especial_usando_aspas_simples
# => 'Isso é "normal" e \ 'util\' em Ruby '
puts string_especial_usando_aspas_duplas
# => "Isso é \"normal\" e 'util' em Ruby"
Existeumanota çãonalinguagemRubyquefoiinspiradanoPerlquepermite
declararmosestetipode Stringespecial.Bastadeclará-ladaseguinteforma:
string_especial = %{Isso é "normal" e 'util' no mundo Ruby}
puts string_especial
# => "Isso é \"normal\" e 'util' em Ruby"
Naverdadequalquercaracterenãoalfanuméricopodeserusadoapóso % ,
porexemplo:
string_especial = %[Isso é "normal" e 'util' no mundo Ruby]
puts string_especial
# => "Isso é \"normal\" e 'util' em Ruby"
string_especial = %?Isso é "normal" e 'util' no mundo Ruby?
puts string_especial
# => "Isso é \"normal\" e 'util' em Ruby"
string_especial = %~Isso é "normal" e 'util' no mundo Ruby~
puts string_especial
# => "Isso é \"normal\" e 'util' em Ruby"
Obviamenteocaractereutilizadoparadelimitara Stringdeveserescapado
com“\”casoapareçadentrodotextoqueestásendodeclarado:
string_especial = %{Isso é "normal" e \{util no mundo Ruby}
puts string_especial
# => "Isso é \"normal\" e {util em Ruby"
Entretantosevocêutilizarcomodelimitadoroscaracteres (parenteses),
[colchetes], {chaves}ou <menor e maior>elespodemaparecerdentro
da Stringsemseremescapadoscasosejamusadosempares(diferentementedo
exemplodadoanteriormente):
string_especial = %{Isso é "normal" e {util} no mundo Ruby}
puts string_especial
# "Isso é \"normal\" e {util} em Ruby"
24

## Página 39

CasadoCódigo Capítulo2. SeuprimeiropassonoRuby:conven çõeseasdiferentesestruturas...
Estaformadedeclara çãode Stringpossuialgumasvaria ções,quepodem,por
exemplo,adicionaracapacidadedeinterpolarvariáveis.
•%q :Nãopermiteinterpola ção;
•%Q :Permiteinterpola ção.
Existemalgumasoutrasvaria çõesquevamosaprenderaolongodolivro. Esta
maneiradedeclarar Stringpermitequesejamelastambémcriadascommúltiplas
linhas:
string_especial = %{Isso é "normal" e {util} no mundo Ruby
e a partir de agora veremos a 'todo' momento}
puts string_especial
Reparequeumaquebradelinha(\n)éinseridaexatamentenolugarondeque-
bramosalinhaemnossocódigo.Essacaracterísticaémuitoútilquandoprecisamos
criar Stringgrandeseprecisamosdeixá-lasmaislegíveis.
2.10 P róximos passos
Nestecapítuloaprendemosboasconven çõesdecódigonasdeclara çõesdevariáveis,
algunsoutrostiposdedadosexistentesnalinguagemRuby,estruturasdecontrole
como ife unlesseasmelhoresformasdeutilizá-las,afimdediminuirruídosna
sintaxeeasconhecidaseúteisestruturasderepeti ção for, whilee until.
Aprendemostambémasdiferentesformasdedeclararmos String,comvaria-
çõesesuporteamúltiplaslinhas.Ointeressantevalor nilqueserámuitoutilizado
durantetodoorestantedolivro.
Oimportanteélembrarqueestesconceitossãoabasequeprecisamosparaseguir
emfrenteeaprendermosrecursosmaisavan çadosdalinguagem.
Portanto,nãodeixedúvidasparatrás,sepreciso,volteeleianovamentepartes
quevocêjulganecessárioantesdeprosseguirmos.
25

## Página 41

Capítulo3
Ocomeçodanossaaplica ção
Noscapítulosanteriores,aprendemosalgumasfuncionalidadesbásicasdalingua-
gemRuby.E,comojávimos,umadassuasprincipaiscaracterísticaséserorientada
aobjetos.Nestecapítulofocaremosnacria çãodeclasses,métodoseobjetosusando
todoopoderquealinguagemnosproporciona.
Começaremosconstruindoumaaplica çãoqueservirádebaseparaospróximos
capítulosdolivro. Portanto,éinteressantequevocêfa çaoscódigoseentendaos
conceitosexplicadosnestecapítulo.
Existemváriosassuntosquepoderíamosabordarenestelivroconstruiremos
umaaplicaçãoparacontrolarumalojadelivros.Controlaremososeuestoque,quais
sãoosclientesdaloja,faremosalgumasvendaseguardaremostodasestasinforma-
çõesemdisco,utilizandoaAPIdearquivosdoRuby.
Agrandeperguntaquesempreficaquandocriamosumaaplica çãoé:poronde
começar?Temosmuitasop ções.Podemosiniciarodesenvolvimentopelodomínio
(criandoclasses),pelainterfacedousuário,pelobancodedadoseassimpordiante.
No nosso caso, começaremosdesenvolvendoasclassesdedomíniodaaplica ção.

## Página 42

3.1. AdefiniçãodaclasseLivro CasadoCódigo
3.1 A definição da classe Livro
Sevamosconstruirumaaplica çãoquegerenciaumalojadelivros,precisamosman-
terosdadosdosnossoslivrosemalgumlugar.Pensandobrevementeneles,teremos:
nome = "Linguagem Ruby"
isbn = "123-45678901-2"
numero_paginas = 245
preco = 69.90
Todososlivrosdanossalojaestãocomumdescontopré-definido:
desconto = 0.1
Agoraprecisamossaberqualéopre çodonossolivrocomdesconto.Umaconta
bemsimplespodenosdevolverqualovalorcomodesconto:
nome = "Linguagem Ruby"
isbn = "342-65675756-1"
numero_paginas = 245
preco = 69.90
desconto = 0.1
preco_com_desconto = preco - (preco * desconto)
Oproblemadestecódigo,todoespalhado,éque,quandoprecisarmoscalcular
odescontodequalquerlivro,teremosquerepetiramesmaopera ção.Seemalgum
momentoestalógicativerqueseralterada,vamosterquemudaremNlugaresdo
nossocódigo.
Podemosvoltarumpouconotempoeimitarasantigaseclássicasfun çõesque
temosemlinguagenscomoC.
def preco_com_desconto(preco, desconto)
preco - (preco * desconto)
end
Agora,todavezqueprecisarmosefetuarocálculodopre çocomdesconto,cha-
mamosafun ção preco_com_descontopassandoo precoeo desconto:
nome = "Linguagem Ruby"
isbn = "342-65675756-1"
28

## Página 43

CasadoCódigo Capítulo3. Ocomeçodanossaaplica ção
numero_paginas = 245
preco = 69.90
desconto = 0.1
puts preco_com_desconto(preco, desconto) # => 62.90
Caso haja necessidade de alterar algum outro livro, devemos criar as va-
riáveis referentes as informações deste outro livro e então chamar o método
preco_com_descontoparasabermosqualonovovalor:
nome = "Test Driven Development: Teste e Design no Mundo Real"
isbn = "342-65675751-1"
numero_paginas = 212
preco = 89.90
desconto = 0.1
puts preco_com_desconto(preco, desconto) # => 80.90
Oquetemosaquiéumtípicocasoondeosdadoseasuamanipula çãoestão
separados,quandodeveriamestarjuntos.EsseéumdosprincípiosportrásdaOri-
entaçãoàObjetos,unirdadoseamanipula çãodosmesmos,encapsulandooacesso.
Amaneiradefazermosissoécolocandoestecódigodentrodeumaclasseerepre-
sentarcadaumdoslivrosdanossalojacomoumainstânciadestaclasse.
ParacriarclassesusandoRuby,bastausarapalavrareservada classedelimitar
ofinaldasuaclassecomapalavrareservada end.
class Livro
end
29

## Página 44

3.1. AdefiniçãodaclasseLivro CasadoCódigo
Constantes
Onomedeumaclassedeveobrigatoriamentecome çarcomumaletra
maiúsculaeasoutrasminúsculas.Porexemplo: Livro.Reparequeo
nome Livronãoéuma String,jáquenãoestáentreaspasouden-
trododelimitadorde String. Onome Livroéumaconstante,que
definimosquandocriamosanossaclasse.
TodosostiposexistentesnoRubycomo String, Integer, Time
etc,sãoconstantes.
Casoonomedasuaconstantesejacomposto,usamosanota çãocamel
case,porexemplo: UnidadeDeEstoque.
Oquecriamosfoiumaabstra çãodeum Livroouseja,um templatequedirádo
queumlivroécomposto.Apartirdaclasse,queéotemplate,precisamoscriarum
novolivro,ondepoderemosdizerquaissãosuascaracterísticas,comotítulo,isbn,
autoreassimpordiante.Paracriarmoscadaum,usaremosapalavra new:
teste_e_design = Livro.new
web_design_responsivo = Livro.new
Quandousamoso newemumaclasse,estamoscriandoumainstânciadela(di-
zemostambémqueestamoscriandoumobjetodaqueletipo).Nocódigoanterior,
criamosduasinstânciaseasreferenciamosatravésdasvariáveis teste_e_design
e web_design_responsivo.Nósnãoprovemosnenhumtipodeinforma çãoso-
breesteslivros,comoonomedoautor,isbn,quantidadedepáginasetc.Esseéum
dosprincípiosdaorienta çãoaobjetos,guardardadossobreumadeterminadaenti-
dadedonossosistema.
Amelhormaneiradeprovermosestasinforma çõesénomomentoquecriamos
nossosobjetosdotipo Livro.Paraissoexisteométodo initializequeécha-
madotodavezqueexecutamosométodo newafimdecriarumobjeto.
teste_e_design = Livro.new("Mauricio Aniche" , 247, "123454")
web_design_responsivo = Livro.new("Tárcio Zemel" , 189, "452565")
Podemosatémesmoremoverosparênteses:
teste_e_design = Livro.new "Mauricio Aniche" , 247, "123454"
web_design_responsivo = Livro.new "Tárcio Zemel" , 189, "452565"
30

## Página 45

CasadoCódigo Capítulo3. Ocomeçodanossaaplica ção
Quando criamos uma classe, ganhamos automaticamente um método
initialize default,paraqueoobjetopossatersuasinforma çõesinicializadas.
Como queremos passar dados para inicializar nosso objeto de uma maneira
diferente,nocasopassandoonomedoautor,númerodepáginaseISBN,devemos
implementarnossoprópriométodo initializeemnossaclasse Livro:
class Livro
def initialize(autor, numero_de_paginas, isbn)
end
end
Sobrescrevemos o métodoinitialize default, criando ummétodocujo
nomedeveser initialize. Ométodoinitializeéummétodoespecialdo
Ruby,invocadopelo Livro.newparacriarumnovoobjeto. Nessemomento,o
Ruby aloca espaçoemmemóriaedepoisinvocaométodo initializepassando
osparâmetrosnecessáriosparacriaroobjeto.
Agoravamosimaginarqueexistemalgunslivrosquenãopossuemoatributo
isbn,onaturalseriaomitirovalordoisbn:
teste_e_design = Livro.new "Mauricio Aniche" , 247
Issonãofunciona,poisparaalinguagemRuby,aaridadedométodoéimpor-
tante,ouseja,devemospassarexatamenteaquantidadedeargumentosdefinidono
métodoinitialize.
SepensarmosemlinguagenscomoJava,podemosdefinirumoutrométodo
initializequerecebeapenasonomedoautoreonúmerodepáginas,recurso
conhecidocomo sobrecarga:
class Livro
def initialize(autor, numero_de_paginas, isbn)
end
def initialize(autor, numero_de_paginas)
end
end
Masissotambémnãofuncionará,poisointerpretadordoRubyconsideraapenas
oúltimométododefinidonaclasse.Rubynãosuportasobrecarga.Paraessasitua ção,
alinguagemsuportaousodeargumentoscomvalorespadrão:
31

## Página 46

3.1. AdefiniçãodaclasseLivro CasadoCódigo
class Livro
def initialize(autor, numero_de_paginas, isbn = "1")
end
end
Quandodeclaramosoargumento isbn = "1",definimosquenomomentoda
inicializaçãodosobjetosdotipo Livro,podemosomitiroúltimoargumento:
Livro.new "Lucas Souza" , 198
Ovalordoargumento isbné“1”.
Agoravamosinverteraordemdosargumentosdométodo initialize,colo-
candooatributo isbnantesdoatributo numero_de_paginasevamostambém
imprimirosvaloresdecadaumdosargumentos:
class Livro
def initialize(autor, isbn = "1", numero_de_paginas)
puts "Autor: #{ autor}, ISBN: #{ isbn}, Pág: #{ numero_de_paginas}"
end
end
Livro.new "Lucas Souza" , 200
E o resultado é: Autor: Lucas Souza, ISBN: 1, Páginas: 200.
Veja que o Ruby é esperto e consegue atribuir o valor 200 ao atributo
numero_de_paginasenãoaoatributo isbn. Issoocorreporquealinguagem
Rubypossuitrêstiposdeargumentos:
• Obrigatórios;
• Comvalorespadrão;
• Opcionais.
Vimosdoisdelesatéomomento:Obrigatórioecomvalorespadrão. Veremos
sobreosatributosopcionaisnospróximoscapítulos. Masvamosaoqueinteressa,
comooRubyconseguedescobrirparaqualatributodeveatributoosvaloresdacha-
madaaométodo initialize?
Quandoummétodorecebeachamada,ointerpretadordivideaatribui çãodos
valoresemalgunspassos. Primeiroeleprocuratodosargumentosobrigatóriose
32

## Página 47

CasadoCódigo Capítulo3. Ocomeçodanossaaplica ção
associaosvaloresaestes,casonãoencontrevalorparaalgumdestesatributosum
errodotipo ArgumentExceptionacontece.Emseguida,seaindaexistiremvalo-
ressobrando,estessãoatribuídosaosargumentos defaultqueexistiremnométodo.
Casosobreapenas1valor,eexistiremdoisargumentoscomvaloresdefault,oRuby
atribuiráovalorrestanteparaoprimeiroargumentocomvalordefault.
3.2 C rie a estrutura do projeto
Ocódigofinaldoprojetoqueseráconstruídofoidisponibilizadonomeugithub:
https://github.com/lucasas/projeto-ruby
Agora,éimportantequesejacriadaaestruturabásicadoprojeto,quefacilitaráa
alteraçãodasclassesqueserãocriadasaolongodoscapítulos.Oidealéquesomente
ostestessejamfeitosutilizandooIRBetodasasoutrasclassesecódigosfiquem
dentrodoprojeto.
Crieumapastachamada loja_virtualemumdiretóriodesuapreferência
edentrodestediretório loja_virtualcrieumapastachamada lib.Dentrodo
diretório libserãocriadososarquivosquerepresentamasclassesdosistema,como
porexemplo,aclasse Livroquepodemostransferirparaláagoramesmo.
Crieumarquivochamado livro.rbdentrodapasta libcomoconteúdo
atualquedefinimosnoIRB:
class Livro
def initialize(autor, isbn = "1", numero_de_paginas)
puts "Autor: #{ autor}, ISBN: #{ isbn}, Pág: #{ numero_de_paginas}"
end
end
Agoraqueaclasse Livrofoicolocadaemumarquivoseparadoprecisamosal-
teraramaneiraqueostestesdestaclasseserãofeitos. QuandoumIRBéabertoo
arquivo lib/livro.rbnãoécarregadoautomaticamente,vocêpodevalidarten-
tandocriarumobjeto Livroabrindoumnovoterminal:
Livro.new "Lucas Souza" , 200
# => NameError: uninitialized constant Livro
Paracarregaroconteúdodoarquivo lib/livro.rbénecessárioutilizaro
métodorequiredaclasse Kernel.Ométodo requirerecebecomoparâmetro
uma Stringquepodeseronomedoarquivo .rbquevocêdesejacarregar.Seo
33

## Página 48

3.2. Crieaestruturadoprojeto CasadoCódigo
parâmetronãoforocaminhoabsolutodoarquivo .rbomesmoseráprocuradoem
diretóriosqueestãodefinidosnaconstante $LOAD_PATH.
Oarquivo lib/livro.rb nãoestáemnenhumdosdiretóriolistadosem
$LOAD_PATH,queemgeral,contémosdiretóriosondeestãoosarquivos .rb
dasclassescoredoRuby. Sendoassimtemosdoiscaminhosparafazercomqueo
Rubyconsigacarregaroarquivoquecontémaclasse Livro.Oprimeiroéadicionar
naconstante $LOAD_PATH,queéumobjeto Array,odiretório libdoprojeto
loja_virtual:
$LOAD_PATH << "caminho relativo do projeto loja_virtual/lib"
Aoexecutarestecódigo,o requirepodeserfeitoapenascomonomedoar-
quivodapasta libquedesejamoscarregar:
require 'livro'
Asegundaop ção,emelhornaminhaopinião,écarregaroarquivopassandoo
seucaminhoabsoluto. Porém,issopodeserumpoucocustosojáquevocêpode
simplesmenteresolveralteraronomedapastade loja_virtualpara loja.
Oidealéutilizarométodo expand_pathdaclasse Filequeretornaocami-
nhoabsolutodeumnomedearquivopassadocomoparâmetro,levandoemcon-
sideraçãoodiretórioondeachamadadométodoéexecutado. Supondoqueo
arquivo livro.rbestejadentrodapasta lib,queporsuavezestádentrodo
diretório '/home/lucas/loja_virtual'aoexecutarachamadaaométodo
expand_pathdentrodestediretóriopassandoa String‘lib/livro’oretornodo
métodoserá'/home/lucas/loja_virtual/lib/livro':
# executando a partir do diretório /home/lucas/loja_virtual
puts File.expand_path("lib/livro")
# => "/home/lucas/loja_virtual/lib/livro"
Exatamenteodiretórioondeseencontraoarquivo livro.rb.
Agoraparatestaraclasse Livrocomofizemosnase çãoanterior,bastaabrirum
novoIRBnodiretório loja_virtualeinvocarométodo requirepassandoo
caminhoabsolutodoarquivo livro.rb:
# executando a partir do diretório /home/lucas/loja_virtual
require File.expand_path("lib/livro")
# objeto Livro criado com sucesso
Livro.new "Lucas Souza" , 200
34

## Página 49

CasadoCódigo Capítulo3. Ocomeçodanossaaplica ção
Apartirdeagora,todosasnovasclassesserãocolocadasdentrodearquivos .rb
napasta lib.EostestesserãofeitosnoIRB,lembrandoquedevesersempreaberto
apartirdodiretório loja_virtual. Eclaro,énecessáriocarregar,utilizandoo
métodorequire,todasasclassesqueserãoutilizadasnoteste.
Outradicaimportante:quandofornecessáriocriarclassesnovas,haveráuma
indicaçãodosprocedimentosquedeverãoserfeitosparaqueamesmapossaser
testada.Quandohouveraltera çãoemclassesjáexistentes,bastaeditaroconteúdo
daclassedentrodeseurespectivoarquivo .rb. Elembre-seoprojetopodefinal
comaimplementa çãocompletapodeserencontradonogithub:
https://github.com/lucasas/projeto-ruby
Encoding arquivos .R B
Osarquivosquecontémasclassescriadasemnossosistema,ficarão
emarquivos .rbdentrodeumdiretóriodesuapreferência. Porémé
importanteressaltarquearquivos .rbpossuemumencodingUS-ASCII
porpadrão. Casoseucódigocontenhaqualquercaracterequenãofor
compatívelcomoASCII,ainterpretadorRubyseráfinalizadoeacusará
oerro: invalid multibyte char (US-ASCII).
Sevocêquiseralteraroencodingpadrãodoarquivo .rb,bastaadi-
cionaraseguintelinhadoarquivo:
# encoding: utf-8
Nesteexemplo,ajustamosoencodingdoarquivoparaUTF-8,que
permitiráquevocêuseacentoseoutroscaracteres.
3.3 D efina os atributos de instância
Osparâmetrospassadosparaométodo initializesãonaverdadevariáveislo-
cais,ouseja,assimqueterminaraexecu çãodométodo,asvariáveislocaissimples-
mentedesaparecem.
Vamosprecisarasinforma çõesdoautor,númerodepáginaseISBNparatraba-
lharcomelasmaisadiantenosnossosprogramas.Queremosqueainforma çãodos
livrosacompanhemoobjetoquevaiserinstanciado. Pararesolveresteproblema
precisamoscopiarovalordestesparâmetrosparavariáveisdeinstânciadecadaob-
jeto.Estecomportamentoémuitocomumquandocriamosmétodosconstrutores.
35

## Página 50

3.3. Definaosatributosdeinstância CasadoCódigo
Entãovamoscopiarosvaloresdosparâmetrosdométodo initializepara
variáveisdeinstância:
class Livro
def initialize(autor, isbn = "1", numero_de_paginas)
@autor = autor
@isbn = isbn
@numero_de_paginas = numero_de_paginas
end
end
Reparequeasvariáveisdeinstânciatemumcaractere @antesdonome.Oim-
portanteaquiépercebermosqueasvariáveispodemternomesiguais,porém,variá-
veiscom @sãodeinstânciaecompõemoestadointernodoobjetoqueestásendo
criado,enquantovariáveislocaispossuemumescopomaiscurto,elasduramapenas
atéotérminodaexecuçãodométodo.
Visibilidade das v ariáveis de instância
EmRuby,todasasvariáveisdeinstânciacriadassãoprivadas,ouseja,
nãopossuemacessoexterno,nemparaleitura,nemparaescrita.Sequi-
sermosacessá-las,vamosutilizarrecursosdapróprialinguagem,queve-
remosnaspróximasse ções.
Vamostestarométodo initializequeagoraguardaosparâmetrosemva-
riáveisdeinstância:
teste_e_design = Livro.new("Mauricio Aniche" , "123454", 247)
web_design_responsivo = Livro.new("Tárcio Zemel" , "452565", 321)
p teste_e_design
p web_design_responsivo
Ocódigoacimaproduzaseguintesaída:
#<Livro:0x007fa526012048 @autor="Mauricio Aniche", @isbn="123454",
@numero_de_paginas=247>
#<Livro:0x007fa526012049 @autor="Tárcio Zemel", @isbn="452565",
@numero_de_paginas=321>
36

## Página 51

CasadoCódigo Capítulo3. Ocomeçodanossaaplica ção
puts ou p?
Quandoprecisamosimprimirinforma çõesnoconsoleemRuby,po-
demosutilizarosmétodos putsou p. Aprimeiradelasjáhavíamos
visto,ométodo puts.Noexemplodecódigoondetestamosnossasva-
riáveisdeinstância,usamosométodo p.
Ométodo putsimprimeoretornodométodo to_sdoobjetoque
foipassadoparaserimpresso.Istoé,casovocêfa ça puts variavel,
écomoseelemostrasseovalorde variavel.to_s,métodoquevere-
moslogoemseguida.Jáométodo pémaisutilizadoquandoqueremos
realizaro debugdoconteúdodoobjetopassadocomoargumento.Nesse
caso,ométodo inspectdoobjetoéinvocadoeoretornoéimpresso
natela. Quandooconteúdodasvariáveisdeinstânciasãoimpressas,é
porqueométodo inspectdaclasse Livroretornaosvaloresdetodas
asvariáveisdoobjetocriado.
3.4 S obrescrevendo o método T O_S
Convenhamosqueoresultadoimpressonãoéoideal,podemosretornarumamen-
sagemmaisagradávelcasoalgumusuáriodonossocódigoinstancieequeiraver
informaçõesmaiscoerentessobreumainstânciade Livro.
Aliás,exibirumamensagemamigávelao‘imprimir’umobjetoéconsiderado
umaboaprática.Esseassuntoéinclusivecapítulodeumlivromuitoconhecidona
comunidadeJava,chamado Effective Java,escritoporJoshuaBloch,hojeengenheiro
doGoogle.
EmRubypodemosaplicaramesmapráticasobrescrevendoométodo to_s,
queéherdadonaturalmenteportodasasclasses,poisfazpartedaclasse Object,e
fazendocomqueeledevolvauma String:
# coding: utf-8
class Livro
def initialize(autor, isbn = "1", numero_de_paginas)
@autor = autor
@isbn = isbn
@numero_de_paginas = numero_de_paginas
end
37

## Página 52

CasadoCódigo
def to_s
"Autor: #{ @autor}, Isbn: #{ @isbn}, Páginas: #{ @numero_de_paginas}"
end
end
UmanovidadenessecódigoéqueemRuby,quandodesejamosretornarumde-
terminadovalornãoprecisamosexplicitamentecolocarapalavra returnantesdo
valorquedesejamosretornar,oretornodequalquermétodoescritoemRubysempre
seráaúltimainstruçãodecódigo(veremosestecomportamentocommaisdetalhes
nocapítulo‘RubyFuncional’).Seaúltimainstruçãodeummétodofor,porexem-
plo,a String "Um texto qualquer",aoinvocarmosestemétodoreceberemos
comoretornodométodoaprópria String Um texto qualquer. Porém,em
algumasocasiõesousodapalavra returnénecessário,dependendodalógicaque
estamosimplementando,maslembre-sequeele nuncaéobrigatório.
Lembre-sequeométodo to_séinvocadoquandoutilizamosométodo puts.
Portantovamosalterarocódigoquetestaacria çãodosobjetoscomsuasvariáveis
deinstância:
teste_e_design = Livro.new("Mauricio Aniche" , "123454", 247)
web_design_responsivo = Livro.new("Tárcio Zemel" , "452565", 321)
puts teste_e_design
puts web_design_responsivo
Agoraocódigoacimaproduzaseguintesaída:
Autor: Mauricio Aniche , Isbn: 123454, Páginas: 247
Autor: Tárcio Zemel, Isbn : 452565, Páginas: 321
Amensagemestámuitomaiseleganteeconcisa.Lembre-se,sobrescreveromé-
todo to_ssempreéumaboapráticaquandoqueremoscriarumamensagemmais
elegantequedescrevaoestadointernodosobjetos.
3.5 A lteração e leitura de atributos
3.5. ALTERAÇÃOELEITURADEATRIBUTOS
Paraquenossoslivrospossamservendidos,precisamosqueelestenhamumatributo
quecontémseupre ço. Paraissovamosadicionarumnovoargumentonométodo
initializedaclasse Livroeguardarseuvaloremumavariáveldeinstância
chamada @preco:
38

## Página 53

CasadoCódigo Capítulo3. Ocomeçodanossaaplica ção
# coding: utf-8
class Livro
def initialize(autor, isbn = "1", numero_de_paginas, preco)
@autor = autor
@isbn = isbn
@numero_de_paginas = numero_de_paginas
@preco = preco
end
def to_s
"Autor: #{ @autor}, Isbn: #{ @isbn}, Páginas: #{ @numero_de_paginas}"
end
end
Epodemosinstanciarnovoslivrosinformandoopre ço:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9
Agoraparatodososobjetosdotipo Livroqueforamcriados,desejamostam-
bémsaberseupre ço. Maslembre-sequeasvariáveisdeinstânciasãosempre pri-
vadas,ouseja,sóconseguimosacessá-lasdentrodaclasse Livro.Asolu çãoneste
casoécriarummétodo públicoqueretorneovalordavariável @preco:
# coding: utf-8
class Livro
# outros métodos
def preco
@preco
end
end
Agora, dadaqualquerinstânciadeum Livro, podemosinvocarométodo
precoqueretornaráovalordavariável @preco:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9
puts teste_e_design.preco # => 60.9
Reparequefizemosummétodocomomesmonomedavariável. Essaéuma
convençãoutilizadapelosdesenvolvedoresRuby,ondeométodoqueacessaavariá-
veleaprópriavariávelpossuemomesmonome.
39

## Página 54

CasadoCódigo
OBrasiléumpaísquepossuiinfla çãoquegiraemtornode6%a7%aoano.
Emnossaaplica ção,permitiremosqueosnossoslivrossoframaltera çõesdepre ços
também. Dessaforma,dadaumainstânciadotipo Livrodesejamosalterarseu
preço:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9
teste_e_design.preco = 79.9
# => NoMethodError: undefined method `preco=' for
Autor: Mauricio Aniche , Isbn: 123454, Páginas: 247:Livro
Lembre-senovamente,asvariáveisdeinstânciasãosempre privadas.Entãopor
enquantonãoconseguimosalteraropre çodeumobjeto Livro.Asolu çãoécriar-
mosummétodo públicoquerecebeonovopre çodolivrocomoargumentoeatribua
estepreçoavariávelqueguardaovalordonossolivro, @preco:
# coding: utf-8
class Livro
# outros métodos
def preco
@preco
end
def preco=(preco)
@preco = preco
end
end
Podemosveroutraconven çãoparacriarcódigoRubymaislegível.Osmétodos
quealteramovalordevariáveisdeinstânciacostumamteronomedavariávelsem
o @,comumsinalde =eadeclara çãodosargumentosdométodo.Maslembre-se
queissoéumaconven ção.
Paraalteraropre çodeumainstânciadotipo Livropodemosagorainvocaro
métodopreco=:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9
teste_e_design.preco=(79.9)
puts teste_e_design.preco
40

## Página 55

CasadoCódigo Capítulo3. Ocomeçodanossaaplica ção
Aoexecutarmosocódigoacima,veremosqueonovopre çodolivroé 79.9.
Maspodemosdeixarnossocódigomaissimples.Removerosparênteseséumbom
caminhoparamelhoraralegibilidade:
teste_e_design.preco=79.9
Quandodefinimosmétodosquepossuemsinalde =emsuanomenclatura,po-
demosadicionarumespa çonachamadadométodo:
teste_e_design.preco = 79.9
Diferençasutil,masquedeixaasensa çãodequeestamosalterandoovalorda
variáveldiretamente. Nossocódigoestálegível, maspodemosmelhorá-loutili-
zandoapróprialinguagemRuby. Comocriarmétodosqueacessamemodificam
osvaloresdeumavariáveldeinstânciaéumatarefabastantecomum,oscriado-
resdalinguagempensaramemfacilitaresteprocessoecriaram: attr_writere
attr_reader.
Essesmétodospodemreceberváriosargumentosdotipo Symbol.Cadasím-
bolorepresentaonomedavariávelquedesejamosexporparaleituraouescrita:
# coding: utf-8
class Livro
attr_writer :preco
attr_reader :preco
# outros métodos
end
Quandochamamosométodo attr_writerpassandoosímbolo :preco,
automaticamenteosobjetosdotipo Livropassamaterummétodo preco=.O
mesmoacontecequandochamamosométodo attr_reader,nestecasoosobjetos
passamaterummétodo preco:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9
teste_e_design.preco = 79.9
puts teste_e_design.preco
Sevocêdesejacriarumpardemétodos,umdeleituraeoutrodeescritapara
umadeterminadavariáveldeinstância,existeumamaneiramaissimplesdoque
utilizarosmétodos attr_readere attr_writer.Comesseintuito,ométodo
attr_accessorfoicriado:
41

## Página 56

CasadoCódigo
# coding: utf-8
class Livro
attr_accessor :preco
# outros métodos
end
O attr_accessoratuacomoumsubstitutoparaosmétodos attr_writer
e attr_reader.Quandoousamos,definimosummétododeleituraeumoutro
deescritaseguindoaconven çãodalinguagem.
Comissoosmétodos precoe preco=quehaviamsidodefinidosmanual-
mente,podemserremovidos.
Símbolos
Símbolossãopalavrasqueparecemcomvariáveis,elespodemconterletras,nú-
merose _.Símbolossão Stringmaislevesegeralmenteutilizadoscomoidentifi-
cadores.
Averdadeéquesímbolossãostrings,comoumadiferen çaimportante,elessão
imutáveis,ouseja,seuvalorinternonãopodeseralterado.Porissogeralmenteos
utilizamoscomoidentificadores.
:um_simbolo_qualquer.object_id == :um_simbolo_qualquer.object_id
# true
"um_simbolo_qualquer".object_id == "um_simbolo_qualquer".object_id
# false
Vejaqueindependentedaquantidadedevezesquereferenciamosumsímbolo,
elesempreseráomesmoobjeto(ométodo object_idretornaoumidentificador
doobjetonamemória).Jánocasodas String,mesmosendoexatamenteiguais,
sãoobjetosdiferentesnamemória.Como Stringsãoimutáveis,cadaobjetotem
seupróprioespa çoemmemória,quandoelasnãosãomaisreferenciadas,poderão
sercoletadaspelocoletordelixo( Garbage Collector-GC).
Jáossímbolos,porteremumúnicainstâncianamemória,nuncaserãocoleta-
dospeloGC.Alémdisso,símbolosnãosãoguardadossomentenamemória,eles
tambémficamemumdicionáriodesímbolosotimizadopelointerpretador.
3.6 A tributos nem tão priv ados assim
42

## Página 57

CasadoCódigo Capítulo3. Ocomeçodanossaaplica ção
3.6. ATRIBUTOSNEMTÃOPRIVADOSASSIM
Umasdascaracterísticasdevariáveisdeinstânciaéqueelassãoprivadas,ouseja,
seuvalornãopodeseralteradodeforadaclasse,apenascommétodospúblicosque
internamenteemsuaimplementa çãoalteramovalordavariável.Vimosissoquando
precisamosalterarovalordavariável preco.
Infelizmente,existemmaneirasdeburlarestasrestri ções,eumavezquetemos
emmãosainstânciadeumobjetoqualquer,podemoslere alterarovalordasvariá-
veisdeinstância.
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9
puts teste_e_design.instance_variable_get "@preco" # => 60.9
Ométodo instance_variable_getretornaovalordeumavariáveldeins-
tânciaqualquer. Bastapassarcomoargumentoonomedavariávelcomo @. No
códigoacima,oresultadoserá 60.9.Lerovalordavariávelnãoétãoproblemático
secompararmoscomofatodequepodemosalterarovalordequalquervariávelde
instânciatambém:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9
teste_e_design.instance_variable_set "@preco", 75.5
puts teste_e_design.preco # => 75.5
Ométodo instance_variable_setrecebedoisargumentos,oprimeiroé
onomedavariáveldeinstânciaquevocêdesejaalterar,osegundoovalorquevocê
desejaatribuiràvariável.
Osmétodos instance_variable_sete instance_variable_getsão
métodosherdadosportodososobjetosRuby. Elespertencemaclasse Object,
queéaclassepaidahierarquiadeclassesquetemosnalinguagem.Essesmétodos
nosapesentamocome çodeumassuntomuitodiscutidoepoderosodalinguagem
conhecidocomometa-programa ção.
3.7 G randes poderes , grandes responsabilidades
3.7. GRANDESPODERES,GRANDESRESPONSABILIDADES
Osmétodosquevimosnase çãoanterior,podemparecermuitopoderososemuma
primeiraimpressão. Porém,comotempoedependendodotamanhodoprojeto
43

## Página 58

CasadoCódigo
podemnostrazergrandesdoresdecabe ça. Vamostomarcomoexemploanossa
classe Livro:
# coding: utf-8
class Livro
attr_accessor :preco
def initialize(autor, isbn = "1", numero_de_paginas, preco)
@autor = autor
@isbn = isbn
@numero_de_paginas = numero_de_paginas
@preco = preco
end
def to_s
"Autor: #{ @autor}, Isbn: #{ @isbn}, Páginas: #{ @numero_de_paginas}"
end
end
Vocêsentindo-seoPeterParkerdavidareal,resolvealterarovalordealguma
variávelusandoo instance_variable_set:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9
teste_e_design.instance_variable_set "@preco", 75.5
puts teste_e_design.preco # 75.5
Depoisdealgunsanos,vocêdecidecasar-secomMaryJaneeabandonarsuavida
dehomemaranhaetambémodesenvolvimentodesoftware.Oprojetoéassumido
poroutrodesenvolvedorqueresolvealteraronomedavariável precopara valor:
# coding: utf-8
class Livro
attr_accessor :valor
def initialize(autor, isbn = "1", numero_de_paginas, valor)
@autor = autor
@isbn = isbn
@numero_de_paginas = numero_de_paginas
@valor = valor
end
def to_s
44

## Página 59

CasadoCódigo Capítulo3. Ocomeçodanossaaplica ção
"Autor: #{ @autor}, Isbn: #{ @isbn}, Páginas: #{ @numero_de_paginas}"
end
end
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9
puts teste_e_design.preco
# => NoMethodError: undefined method `preco'
for Autor: Mauricio Aniche , Isbn: 123454, Páginas: 247:Livro
Achamadaaométodo precoretornaráoerro: NoMethodError,obviamente
porqueométodoagorasechama valor:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9
puts teste_e_design.valor
Porémoantigodesenvolvedorhomemaranhadeixouemalgumlugardosistema
umachamadaao instance_variable_set:
teste_e_design.instance_variable_set "@preco", 75.5
puts teste_e_design.instance_variable_get "@preco"
Oproblemaéquealémdetentarmosalterarovalordaumavariávelquenão
existemais,ocódigoacimaésilencioso,nãoretornanenhumerroavisandoque
aquela variável não existe, pelo contrário, ele cria uma variável nova chamada
@precoque não tem relaçãoalgumacomnossodomínio,jáquequandoavariá-
velnãoexiste,aotentarmosacessá-laelaserácriada.
Ocódigotornou-seobsoleto,senãoexistiremtestesdeunidadequevalidemeste
comportamentos,provavelmenteeleseriaobservadosomenteemprodu çãoquando
algumclienteusasseosistema.
Adicaésimplesaqui,seavariáveldeinstânciaéprivada,mesmoquealingua-
gemlhepermitaburlaressacaracterística,nãofa ça,resolvaoproblemadeoutra
maneira.Certamenteexistiráalgummétodonainterfacepúblicadoseuobjetoque
façaporvocêaaltera çãodavariáveldeumaformaseguraecorreta.
45

## Página 61

Capítulo4
Estruturasdedados
Rubypossuitrêstiposdeestruturasdedadosqueveremoscomdetalhesnesteca-
pítulo. Cadaumadestasestruturaspossuisuasqualidadesedefeitos,quevamos
explorardaquiemdiante.
4.1 T rabalhe com Ar r a y s
ArraysemRubysãocole çõesindexadas,ouseja,guardamobjetosemumadetermi-
nadaordemedisponibilizammétodosquepermitemacessarobjetosdestascole ções
atravésdoseuíndice.DiferentedoqueacontececomalinguagemCouJava,onde
precisamosdefinirarrayscomumaquantidademáximadeobjetos,emRubyosar-
raysnãoprecisamterseutamanhoprédefinido,elescrescemconformeanecessi-
dade.
Existemváriasformasdedefinirum ArrayemRuby,sendoqueamaissimples
éutilizando []:
numeros = [1 , 2, 3]

## Página 62

4.1. TrabalhecomArrays CasadoCódigo
puts numeros.class # => Array
Criamosumobjetodotipo Arrayutilizandodoiscolcheteseseparandoosvá-
rioselementosdo Arraycomavírgula.Paraacessaroselementosdeum Array,
utilizamosométodo [indice]querecebecomoargumentoaposi çãodoelemento
quedesejamosacessar,lembrandoqueemRubyosíndicescome çamem0:
numeros = [1 , 2, 3]
puts numeros[0] # => 1
puts numeros[1] # => 2
puts numeros[2] # => 3
Quandoprecisamosacessaroprimeiroouoúltimoelementopodemosfazê-lo
atravésdemétodos(firste last)daclasse Array:
numeros = [1 , 2, 3]
puts numeros.first # => 1
puts numeros.last # => 3
ComoRubyéumalinguagemcomtipagemdinâmica,podemosadicionarob-
jetos(adicionarnovoselementosemumarraysedáatravésdométodo <<,bem
parecidocomumappend,queadicionaráonovoelementonofinaldo Array)de
qualquertipodentrodeummesmo Array:
numeros = [1 , 2, 3]
numeros << "ola"
puts numeros # [1, 2, 3, "ola"]
# => 1, 2, 3, "ola"
Oproblemadeadicionarqualquertipodeobjetodentrodeum Array,éque
muitasvezesnãosabemosqualoobjetoqueestamoslidando.Porexemplo,vamos
definirummétodoquerecebeum Arraycomoargumento,buscapeloprimeiro
elemento,omultiplicapor2eporfimimprimeoresultadonatela:
def multiplica_primeiro_elemento_por_dois(numeros)
puts 2 * numeros.first
end
multiplica_primeiro_elemento_por_dois [1, 2, 3] # 2
multiplica_primeiro_elemento_por_dois ["abc", 2, 3]
# => TypeError: String can 't be coerced into Fixnum
48

## Página 63

CasadoCódigo Capítulo4. Estruturasdedados
Veremosqueexistemvantagensnatipagemdinâmicadasestruturasdedados
emRubynospróximoscapítulos.
A criação de array de strings
Paracriarum Arraydestrings,asintaxeutilizadapodeseramesmaqueusamos
paracriarumarraycomoutrostiposdeelementos:
palavras = [ 'ola', 'mundo']
p palavras # => ["ola", "mundo"]
Existeumasintaxemaissimplesparacriarumarraydepalavras:
palavras = %w{ola mundo}
p palavras # => ["ola", "mundo"]
Avantagemdeusaro %w{}épodersepararaspalavrasquecompõesoArray
utilizandoespaçoenãovírgula,assimpoluindopoucoocódigo.Podemosutilizar
tambémo %W{},quepermiteainterpola çãodevaloresnaspalavrasquecompõeo
array:
nome = "Lucas"
palavras = %W{ola #{ nome}}
p palavras # ["ola", "Lucas"]
4.2 G uardando nosso livros
AproveitandoqueagoraconhecemosumpoucodeumaestruturadedadosRuby,
vamosguardarasinstânciasdosobjetos Livroquecriamosdentrodela.
biblioteca = []
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 70.5
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 67.9
biblioteca << teste_e_design
biblioteca << web_design_responsivo
puts biblioteca
# => Autor: Mauricio Aniche, Isbn: 123454, Páginas: 247
# => Autor: Tárcio Zemel, Isbn : 452565, Páginas: 321
49

## Página 64

4.2. Guardandonossolivros CasadoCódigo
Hoje,decidimosquevamosguardarosobjetosdentrodeum Array,masfutura-
mentepodemosdescobriroutraestruturaquefuncionemelhor,sejamaisrápidaou
forneçavantagensqueo Arraynãooferece.Seoptarmosporessamudan ça,teremos
queprocurartodososlugaresqueinstanciamobjetosdotipo Livro,guardando-os
dentrodeumarray,eadaptarocódigoparaamaneiradanovaestrutura.
Paranosprotegermosdesseproblema,podemosisolarocódigoquefazessaatri-
buiçãoemumúnicoponto,queseráinvocadoemoutraspartesdocódigo.Assim,
alteramosemumsólugareosistemainteiroestámodificado.Essaconceitochama-
se encapsulamento.
Vamosisolarestecomportamentodeguardarlivrosdentrodeumarray,em
umaclassequepodemoschamarde Biblioteca,equandohouveranecessidade
demudarmosde Arrayparaalgumaoutraestrutura,faremosemapenasumlu-
gar. Adicioneadefiniçãodaclasse Bibliotecadentrodeumarquivochamado
biblioteca.rbdentrododiretório lib:
class Biblioteca
def initialize
@livros = []
end
def adiciona(livro)
@livros << livro
end
end
Agoraparaguardaroslivrosquecriamos,nãovamoscriarum Arrayeapendar
osvaloresdiretamentenele.Criaremosumobjetodotipo Bibliotecaechama-
remosométodoresponsávelporadicionarnovoslivrosnabiblioteca.Porém,para
testaraclasse Bibliotecaénecessáriocarregaroarquivoquecontémsuadefini-
ção:
require File.expand_path('lib/livro')
require File.expand_path('lib/biblioteca')
Aopassardotempo,osarquivosnecessáriosparaefetuarostestesserãoum
maiornúmero.Paranãodificultarostestes,vamoscriarumúnicoarquivoquefaráo
requiredetodososoutros.Vamoschamá-lode loja_virtual.rbeadicioná-
lonodiretório libdapasta loja_virtual.Dentrodelefaremosocarregamento
dosarquivos biblioteca.rbe livro.rb:
50

## Página 65

CasadoCódigo Capítulo4. Estruturasdedados
require File.expand_path('lib/livro')
require File.expand_path('lib/biblioteca')
Agoraparaefetuarostestesbastaexecutarumúnico require,doarquivo
loja_virtual.rb:
require File.expand_path('lib/loja_virtual')
Eexecutarostestesdaclasse Biblioteca:
biblioteca = Biblioteca.new
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 70.5
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 67.9
biblioteca.adiciona teste_e_design
biblioteca.adiciona web_design_responsivo
Seprecisarmosacessarquaissãooslivrosqueexistemdentrodanossabiblioteca,
bastaexporavariável @livrosatravésdo attr_reader:
class Biblioteca
attr_reader :livros
def initialize
@livros = []
end
def adiciona(livro)
@livros << livro
end
end
E para acessar as variáveis, podemos chamar o métodolivros na
Biblioteca:
biblioteca = Biblioteca.new
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 70.5
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 67.9
biblioteca.adiciona teste_e_design
51

## Página 66

4.3. Percorrendomeuarray CasadoCódigo
biblioteca.adiciona web_design_responsivo
p biblioteca.livros
# => [Autor: Mauricio Aniche, Isbn: 1, Páginas: 247,
Autor: Tárcio Zemel, Isbn: 1, Páginas: 189]
4.3 P ercorrendo meu array
Nocapítulo2,aprendemosalgumasestruturasdecontrole,entreelaso for,que
serveparaiterarmossobreranges,etambémcole çõescomoo Array. Ométodo
livrosdoobjetobiblioteca,retornatodososlivrosemformatode Array. Para
acessarcadalivrodestearray,bastaiterarmosatravésdo for:
biblioteca = Biblioteca.new
# popula a biblioteca
for livro in biblioteca.livros do
p livro.valor
end
# => 70.5
# => 67.9
4.4 C omo separar os livros por categoria : traba -
lhe com Ha s h
Amedidaquenossabibliotecacresce,precisamossepararoslivrosdentrodabibli-
otecaporcategorias.Dessaforma,oprimeiropassoparafazermosessasepara çãoé
adicionarmosumatributochamado categoriaàclasse Livro:
# coding: utf-8
class Livro
attr_accessor :valor
attr_reader :categoria
def initialize(autor, isbn = "1", numero_de_paginas, valor,
categoria)
@autor = autor
@isbn = isbn
52

## Página 67

CasadoCódigo Capítulo4. Estruturasdedados
@numero_de_paginas = numero_de_paginas
@valor = valor
@categoria = categoria
end
def to_s
"Autor: #{ @autor}, Isbn: #{ @isbn},
Páginas: #{ @numero_de_paginas}, Categoria: #{ @categoria}"
end
end
Acategoriadolivroseráum Symbol,como: :ruby, :testes, :html,
:javascript, :iosetc. Oslivrosquecriamosanteriormenterecebemumar-
gumentoamais,contendoasuarespectivacategoria:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
puts teste_e_design.categoria # => :testes
Agora que cada livro possui sua categoria, vamos adaptar nossa classe
Bibliotecaparaguardá-los. Dessaforma,aclasse Bibliotecateráaorgani-
zaçãodecategorias.
Osarraysguardamoselementossequencialmenteenãoexistenenhumadivisão
desteselementos. Precisamosdeumaestruturaquesuporteestetipodivisão,um
númeroNdeobjetosemumdeterminadocontainer,sendopossíveltermosvários
containerstambém.
Vamosutilizarum Hash,estruturaqueguardasempreumachave(identificador
único,quegeralmenteéumsímbolo)eumvalor(quepodeserqualquertipode
objetoRuby).Suainicializa çãoéfeitautilizando {}:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
hash = {"123454" => web_design_responsivo,
"452565" => web_design_responsivo}
O hash acima possui dois containers, um cujo identificador é aString
"123454", que corresponde aoisbn do objeto teste_e_design, e outro
53

## Página 68

4.4. Comosepararoslivrosporcategoria:trabalhecomHash CasadoCódigo
cujoidentificadoréa String "452565", quecorrespondeao isbn doob-
jeto web_design_responsivo. Cadaumdestescontainerspossuiumdeter-
minadovalor,no Hashacimaocontainer“123454”possuicomovaloroobjeto
teste_e_design,jáocontainer,cujoidentificadoé“452565”,possuicomovaloro
objeto web_design_responsivo.
Quandodesejamosacessarovalorqueestáinclusodentroum Hash,bastain-
vocarmosométodo [:chave]passandoachaveidentificadoradocontainer:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
hash = { "123454" => web_design_responsivo,
"452565" => web_design_responsivo }
p hash ["123454"]
# => Autor: Tárcio Zemel, Isbn: 452565, Páginas: 189,
Categoria: web_design
Bemparecidocomamaneiraqueacessamosvaloresdentrodeum Array. A
diferençaéquepassamosumobjetoquerepresentaachaveidentificadora,enãoum
Integerquerepresentaoíndice,comoacontecequandoacessamosvaloresdeum
Array.
Agora vou provar que o encapsulamento que fizemos ao definir a classe
Bibliotecanosajudaráamigrarsemsofrimentosde Arraypara Hashaes-
truturaqueguardavaoslivros:
class Biblioteca
attr_reader :livros
def initialize
@livros = {} # Inicializa com um hash
end
def adiciona(livro)
@livros[livro.categoria] ||= []
@livros[livro.categoria] << livro
end
end
54

## Página 69

CasadoCódigo Capítulo4. Estruturasdedados
Ocódigoqueinstanciaoslivroseosguardadentrodabiblioteca,continuafun-
cionando.
biblioteca = Biblioteca.new
teste_e_design = Livro.new "Mauricio Aniche" , 247, "123454",
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , 189, "452565",
:web_design
biblioteca.adiciona teste_e_design
biblioteca.adiciona web_design_responsivo
Oproblemaagoraéométodoqueutilizamospararetornaroslivrosqueestão
dentrodanossabiblioteca,retornamum Hashenãomaisum Arrayeaformade
iterarsobreestasduasestruturasdedadossãodiferentes.Aprimeiraop çãoéfazer
comqueométodo livroscontinueretornandoum Array:
class Biblioteca
def adiciona(livro)
@livros[livro.categoria] ||= []
@livros[livro.categoria] << livro
end
def livros
@livros.values.flatten
end
end
Criandonossaprópriaimplementa çãodométodo livros,conseguimosman-
teromesmocomportamentoanterior,quandoretornávamosumarraydiretamente.
Asegundaop çãopararesolveroproblema,éretornarum Hashealteraraforma
queiteramossobreoretornonométodo livros:
biblioteca = Biblioteca.new
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
55

## Página 70

4.4. Comosepararoslivrosporcategoria:trabalhecomHash CasadoCódigo
:web_design
biblioteca.adiciona teste_e_design
biblioteca.adiciona web_design_responsivo
for categoria, livros in biblioteca.livros do
p categoria
for livro in livros do
p livro.valor
end
end
# => :testes
# => 60.9
# => :web_design
# => 70.9
Adiferençaéqueométodo forrecebedoisargumentos,achaveeovalordo
hash.Emnossoexemplo,achaveéa categoriadaestantedelivros( :testes,
porexemplo),evaloréumarraycomoslivrosdestacategoria.
Os métodos values e flatten
Quandoprecisamosobtertodososvaloresdeumdeterminadohash,indepen-
dentedocontainer,utilizamosométodo values(queretornatodososvaloresdo
hashdentrodeum Array):
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
hash = { testes: teste_e_design, web_design: web_design_responsivo }
p hash .values # [teste_e_design, web_design_responsivo]
Nocasodaclasse Biblioteca,nósguardamosconjuntosdelivrosdentrode
Array,sendoum Arrayparacadacategoria.Quandoosvaloresdeumhashsão
dotipo Array,ométodo valuesretornaráumnovo ArraycomváriosArray
dentro,oquepodenãoserumresultadomuitointeressanteparatrabalharmos,veja:
56

## Página 71

CasadoCódigo Capítulo4. Estruturasdedados
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
hash = { testes: [teste_e_design], web_design: [web_design_responsivo]}
p hash .values
# => [Autor: Mauricio Aniche, Isbn: 123454, Páginas: 247,
Categoria: testes ],
[Autor: Tárcio Zemel, Isbn: 452565, Páginas: 189,
Categoria: web_design ]
Precisamosqueoretornodométodo livrossejaumúnico Arraycomto-
dososlivrosexistentesdentroda Bibliotecaindependentedacategoriadeles.
Podemosalcançarnossoobjetivoutilizandoométodo flatten:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
hash = { testes: [teste_e_design], web_design: [web_design_responsivo]}
p hash .values.flatten
# => [Autor: Mauricio Aniche, Isbn: 123454, Páginas: 247,
Categoria: testes,
Autor: Tárcio Zemel, Isbn: 452565, Páginas: 189,
Categoria: web_design ]
Ométodo flattenprocuraporobjetosdotipo Arraydentrodo Array
ondeométodofoichamado(emnossoexemploo Arrayretornandopelométodo
values),extraiessesvaloreseretornaumnovo Arraycomtodososelementos
extraídos.Éimportanteressaltarqueométodo flattenérecursivo,seoinvocar-
mosemum Array,quepossuiváriosoutrosobjetosdotipo Array,queporsua
vezsejamformadosporalgunsoutrosobjetoquetambémsejam Array,elerecur-
sivamenteextrairáoselementosdetodoseleseretornaráoselementosemumnovo
objeto Array.
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
57

## Página 72

4.5. Indomaisafundo:HashesnoRuby1.9 CasadoCódigo
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
jsf_e_jpa = Livro.new "Gilliard Cordeiro" , "543465", 234, 64.9,
:frameworks_mvc
hash = {}
hash[:testes]=[[ teste_e_design ], [ jsf_e_jpa ] ]
hash[:web_design] = [ [ web_design_responsivo ] ]
p hash .values.flatten
# => [Autor: Mauricio Aniche, Isbn: 123454, Páginas: 247,
Categoria: testes,
Autor: Gilliard Cordeiro , Isbn: 543465, Páginas: 234,
Categoria: frameworks_mvc,
Autor: Tárcio Zemel, Isbn: 452565, Páginas: 189,
Categoria: web_design ]
4.5 I ndo mais a fundo : Hashes no Ruby 1.9
Achaveidentificadoradeumobjeto Hashpodeserumobjetodequalquertipo
(String, Integer, Livro,etc). Porémomaiscomumédefinirmosaschaves
como Symbol,quesãocomumenteutilizadosparaestafinalidade.Porexemplo:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
hash = { :testes => [ teste_e_design],
:web_design => [ web_design_responsivo] }
p hash [:testes] # => ["Autor: Mauricio Aniche, Isbn: 123454,
Páginas: 247,
Categoria: :testes"]
Naversão1.9dalinguagemRubyfoiintroduzidaumanovasintaxeparadeclarar
elementosemumhashquandoachaveidentificadoraéum Symbol,muitoparecida
comasintaxedalinguagemJavascript.Entretantoaformaqueacessamosovalorde
Hashcontinuasendoamesma:
58

## Página 73

CasadoCódigo Capítulo4. Estruturasdedados
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
hash = { testes: [teste_e_design], web_design: [web_design_responsivo] }
p hash [:testes] # => ["Autor: Mauricio Aniche, Isbn: 123454,
Páginas: 247,
Categoria: :testes"]
4.6 I ndo mais a fundo : O operador ||=
Imaginequequeremossetarovaloremumadeterminadavariávelsomenteseovalor
atualdamesmafor nil,casoelajáestejapreenchida,ovalordevesermantido:
idade = nil
idade = 27 unless idade
puts idade # 27
idade = 35 unless idade
puts idade # 27
Muitocódigoparaumatarefatrivial.Porisso,oscriadoresdoRuby,fizeramo
operador ||=,queexecutaomesmocomportamentoqueimplementamoscomo
unless:
idade = nil
idade ||= 27
puts idade # 27
idade ||= 35
puts idade # 27
4.7 I ndo mais a fundo : O tipo Se t
Quandotrabalhamoscomobjetodotipo Array,podemosrepetirosmesmosele-
mentosquantasvezesacharmosnecessário,porexemplo:
numeros = [1 , 2, 2, 3, 2, 1]
p numeros # [1, 2, 2, 3, 2, 1]
59

## Página 74

4.7. Indomaisafundo:OtipoSet CasadoCódigo
Nãoexistenenhumaregraqueproíbaaduplicidadedeelementos.Masemcertas
ocasiõesénecessáriogarantirmosquedentrodeumaestruturadedadosexistam
elementosúnicos,ouseja,semrepeti ção.Rubycontemplaessanecessidadeatravés
deumoutrotipodecole ção,chamada Set,queguardavaloresemumordemnão
definida(diferentedearrays)egaranteanãoduplicidade.
Asintaxeusadaparacriarmosumacole çãodotipo Setéumpoucodiferente
dasquevimosatéomomento:
require 'set'
numero_sem_repeticao = Set.new [1, 2, 2, 3, 2, 1]
Quandoprecisamosutilizarotipo Set,precisamoscarregaroarquivo set.rb
quefoiinstaladojuntocomointerpretadoreasoutrasclassesbásicasdaprópria
linguagem.Oarquivo set.rbcontémaclasse Set.
Aclasse Setpossuiummétodo initializequerecebeum Arraycomos
elementosqueformarãoacole ção,aoreceberestearray,sãoguardadosapenasos
elementosnãorepetidosedescartadososrestantes.Podemosverificarestecompor-
tamentoiterandono Setquefoicriado:
require 'set'
numero_sem_repeticao = Set.new [1, 2, 2, 3, 2, 1]
for numero in numero_sem_repeticao do
p numero
end
# => 1
# => 2
# => 3
Vimosqueaclasse Setconsegue“descobrir”quaissãooselementos“iguais”e
manterapenasumdesteselementos.Issofuncionamuitobemcomosnúmeros,mas
esetentarmosadicionarváriasinstânciadeummesmo Livrodentrodeum Set.
Vamosver?
require 'set'
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
60

## Página 75

CasadoCódigo Capítulo4. Estruturasdedados
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
livros = Set.new [teste_e_design, web_design_responsivo ]
for livro in livros do
p livro
end
p hash [:testes] # => ["Autor: Mauricio Aniche, Isbn: 123454,
Páginas: 247,
Categoria: :testes"]
Reparequeduasinstânciasdelivrocompõemo Set.Issoocorreporquepara
alinguagemRuby,estesdoisobjetossãodiferentes. Podemosverificarissoinvo-
candoecomparandooretornodométodo object_id(queretornaumidentifica-
dorúnicodecadaobjetonamemória)decadaumdosobjetos:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
p teste_e_design.object_id == web_design_responsivo.object_id
# => false
Paragarantirmosquedoisobjetossãoiguaisporseusvalores,devemoscompará-
losutilizandoométodo eql?:
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565", 189, 70.9,
:web_design
p teste_e_design.eql? web_design_responsivo
# => false
Oretornacontinuasendo false.Emnenhummomentodefinimosométodo
eql?,naverdadeelefoiummétodoherdadodaclasse Object,equeemsuaimple-
mentaçãooriginalcomparaosobjetosatravésdeseus object_id. Nomomento
emquedecidirmosqueocritérioquedefineseumobjetoéigualaooutrolevará
61

## Página 76

4.7. Indomaisafundo:OtipoSet CasadoCódigo
outrovaloremconsidera ção,devemossobrescreverométodo eql?efazermosa
comparaçãoquejulgamosseraadequada:
# coding: utf-8
class Livro
attr_reader :isbn
def eql?(outro_livro)
@isbn == outro_livro.isbn
end
end
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "123454", 189, 70.9,
:web_design
p teste_e_design.eql? web_design_responsivo # => true
Sobrescrevemosométodo eql?edefinimosqueseumoutrolivrotivero
mesmo isbnqueolivroqueestamoscomparando,elessãoiguais. Éimportante
salientarquenãoestamosdizendoqueelessãoosmesmosobjetosnamemória.
==, equal? ou eql?
Ométodo ==retorna trueapenasseosdoisobjetosenvolvidos
nacomparaçãoforemamesmainstância,esteéseucomportamentopa-
drão. Elepodesersobrescritoafimdeefetuaracompara çãodeoutras
maneiras.
Ométodo equal?ésimilarao ==,eleretorna trueapenasseos
doisobjetosenvolvidosnacompara çãoforemamesmainstância.Asbi-
bliotecasexistentesnalinguagem,quandotemanecessidadedecompa-
rarsedoisobjetossãoamesmainstânciausamométodo equal?,por
essemotivo,nãodevemossobrescreverestemétodo,poisoefeitopode
serbastanteprejudicial.
Porfimométodo eql?porpadrãocomparaasinstânciasdosobjetos
também. Porém,estemétododevesersobrescritoquandodesejamos
avaliarsedoisobjetossãoiguaisporseusvalores,comofizemoscoma
classe Livro.
62

## Página 77

CasadoCódigo Capítulo4. Estruturasdedados
Porémsobrescreverapenasométodo eql?nãoésuficienteparaevitarmosdu-
plicidadedeobjetosdotipo Livrodentrodeumacole çãodotipo Set.Aindanão
ésuficiente,porqueo Setinternamenteutilizaum Hashparaguardarosvalorese
umacoleçãodotipo Hashéumconjuntodebuckets(container)comumrótuloe
dentroumadeterminadaquantidadedeobjetos.
Orótulodestesbucketssãonaverdadeoretornodométodo hashdeumde-
terminadoobjeto.Nocasodosobjetosdotipo Livro,oretornodométodo hash
quasesempreserádiferente. Issoporquetodoobjetopossuiumaimplementa ção
def au l tdométodohashquefazumcálculocompropriedadesespecificasdoobjeto
emquestão.
Sequisermosevitarduplicidadedosobjetosdotipo Livrodentrodeum Set,
devemosfazercomqueinstânciasquepossuemomesmoisbn(queénossocritério
deigualdade)tenhamomesmoretornoquandoinvocarmosométodo hash:
# coding: utf-8
class Livro
def hash
@isbn.hash
end
end
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "123454", 189, 70.9,
:web_design
p teste_e_design.hash == web_design_responsivo.hash # => true
Oquefizemosfoiretornarovalordométodo hashdoatributo Stringisbn.É
sempreimportantetomarmoscuidadosquandoredefinimosométodo hashprin-
cipalmentequandoguardarmosváriosobjetosdestetipodentrode Hashe Set.Se
ovalordo hashforpoucovariável,podemosterváriascolisõesdehash,oquepode
ocasionarumbuscamuitomaislentaporesseselementos.
Agorapodemostestarquecasoinstanciasdiferentesdaclasse Livrotenhamo
mesmoisbn,elesnãoserãomaisduplicadasdentrodeum Set:
require 'set'
teste_e_design = Livro.new "Mauricio Aniche" , "123454", 247, 60.9,
63

## Página 78

4.8. Eagora? CasadoCódigo
:testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "123454", 189, 70.9,
:web_design
livros = Set.new [teste_e_design, web_design_responsivo ]
for livro in livros do
p livro
end
# => Autor: Mauricio Aniche, Isbn: 123454,
Páginas: 247, Categoria: :testes
4.8 E agora?
No próximo capítulo veremos maneiras mais elegantes de iterarmos coleções,
usandocaracterísticasfuncionaisdalinguagemRuby. Exploraremosdiversosmé-
todosúteisqueexistemnasAPIsdoRuby.
64

## Página 79

Capítulo5
Rubyeaprograma çãofuncional
RubyéconhecidaporserumalinguagemrelacionadaaoparadigmaOrientadoa
Objetos,porém,tambémpossuisuporteaoparadigmafuncional. Nestecapítulo
mostrareiosconceitosgeraisrelacionadosaprograma çãofuncional,eexplicarcomo
alinguagemRubysuportaestesconceitosenosajudaacriarcódigosmaislegíveis,
commanutençãomaisfácileprincipalmentemaiseficiente.
5.1 O que é programação funcional
Fundamentalmente,aprograma çãofuncionaléumparadigmadeprograma çãoque
trataacomputa çãocomoaavalia çãodasfun çõesmatemáticaseacapacidadedeevi-
taramutabilidadedeestado.Oparadigmafuncionalenfatizaousodasfun çõesque
nãoalteramestado,aocontráriodaprograma çãoimperativa.Oparadigmafoifun-
damentadonoanode1930comolambdacalculus,umsistemaformaldesenvolvido
parainvestigaradefini çãodefun ções,aplica çãodelasetambémarecursão.

## Página 80

5.2. Funçõespuras CasadoCódigo
5.2 F unções puras
Aprincipaldiferen çaentreasfun çõesmatemáticaseasfun çõescriadasnaslingua-
gensimperativas,équenasegunda,fun çõespodemcausarefeitoscolaterais,alte-
randoovalorjácalculadoanteriormente.Napráticaissoquedizerqueaocriarmos
umfunçãoeainvocarmos,oseuresultadovaidependerdoestadoatualnomomento
emqueelaforexecutada.Noparadigmafuncionalasfun çõesdependemapenasdos
argumentosqueforamrecebidosemsuachamada,sendoassim,invocarafun çãoN
vezesresultasemprenomesmovalor,porestemotivochamamosestasfun çõesde
puras.
Eliminarestesefeitoscolateraisfacilitaoentendimentodocomportamentodo
programaetambémevitapreocupa çõesquandotemoscódigosendoexecutadopa-
ralelamente,poisnossocódigonaturalmentesetornou Thre ad Safe.
AlinguagemRubycontemplaváriascaracterísticasdasfun çõespuras. Vamos
tomarcomoexemploa String,quepossuiváriosfun ções(métodos)puras:
nome = "Lucas"
puts nome.upcase # => LUCAS
puts nome # => Lucas
Nocódigoacimacriamosumavariável nomequepossuiovalor“Lucas”.Acha-
madadométodo upcaseaoinvésdealteraravariávelparaguardarovalor“LU-
CAS”,retornaumanova Stringcomovaloremcaixaalta.Vocêpodeconfirmar
estecomportamentonalinhacriadaapósachamadadométodo upcasequeim-
primeovalordavariável nome,queéexatamenteomesmovalorquedefinimosna
declaraçãodavariável.
Ométodo upcaseéumafunçãopura,porquenãoimportaquantasvezesseja
invocado,retornarásempreomesmovaloretambémnãocausaefeitoscolaterais.
O símbolo !
AomesmotempoqueRubycontemplaoparadigmafuncional,elatambémé
umalinguagemimperativa,ouseja,possuifun çõesquefocamemalteraroestado
dosdados.ExistemváriosmétodosnaAPIdalinguagemquepossuemocaractere !
apósseusnomes.Ocaractere !nofinaldonomedométodoéumaconven ção,que
significaqueométododeveserusadocommodera ção,porquepodecausarefeitos
colaterais.Porexemploométodo upcase!:
66

## Página 81

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
nome = "Lucas"
puts nome.upcase! # => LUCAS
puts nome # => LUCAS
Comovocêpodenotaraoexecutarestecódigo,ométodo upcase!nãoéum
métodofuncionalpuro,porquepossuiefeitoscolateraisquealterama Stringden-
trodavariável nome.Porisso,semprequeutilizaralgummétodocom !nofinal,
tenhacuidado. Oladoboméqueseprecisarmosdefinirummétodoqueiráalte-
raroestadodeumdeterminadoobjeto,podemosdefini-loscomocaractere !no
finalparaqueoutrosdesenvolvedoresestejamcientesdocuidadoaoutilizaraquele
método.
5.3 C omandos que retornam v alores
Literais,chamadademétodos,variáveis,estruturasdecontrole,todosestescoman-
dossãoavaliadoscomoexpressõespelointerpretadorRuby. Vamostomarcomo
exemploocasoondedesejamosatribuirumdeterminadovaloraumavariávelse
umacondiçãoforverdadeiraeoutrovalorcasoacondi çãosejafalsa.Podemoscriar
essecódigoemRubydaseguintemaneira:
valor = nil
numero = "dois"
if numero == "um" then valor = 1
elsif numero == "dois" then valor = 2
else valor = 3
end
p valor # => 2
Porémocódigoacimapodeficarmaislegívelseaproveitarmosopoderdalin-
guagemRubydeavaliartudocomoumaexpressão:
numero = "dois"
valor = if numero == "um" then 1
elsif numero == "dois" then 2
else 3
end
p valor # => 2
67

## Página 82

5.3. Comandosqueretornamvalores CasadoCódigo
Podemosnosaproveitardestahabilidadedalinguagemdeavaliartudocomo
umaexpressãonomomentoqueprecisamosdeclararváriasvariáveiscomomesmo
valor:
a = b = c = 0
p a, b, c #= >000
Atémesmoquandoutilizamosum for,oseuresultadoéumaexpressão. Se
percorrermosum Arraycomtrêselementosusandoum foremultiplicarmos
cadaitempor 2,porexemplo,podemosatribuirseuresultadoaumavariável:
numeros = [1 , 2, 3, 4]
novos_numeros = for n in numeros
n * 2
end
p novos_numeros # => [1, 2, 3, 4]
Ométodo forqueutilizamosretornaum Arraycomosmesmosvaloresin-
seridosno Arrayantigo.Esseéocomportamentodo foretambémdométodo
eachqueveremosembreve,retornarsempreo Arrayoriginal.Paracriarumnovo
Arraycomosvaloresretornadosporcadaitera çãoénecessárioutilizarométodo
mapquetambémserávistoembreve.
M é t o d o s s e mreturn
TodososmétodosRubyretornamsempreoresultadodaúltimaexpressãode-
clarada,poressemotivo,vocênãoprecisaexplicitamenteadicionaro returnno
finaldecadamétodo:
def boas_vindas(nome)
"Bem vindo: #{ nome}"
end
p boas_vindas("Lucas") # => "Bem vindo: Lucas"
Quandoinvocadoométodo boas_vindasretornaráa Stringinterpolada
comovalordoargumento nomequefoipassado.
68

## Página 83

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
5.4 F unções de alta ordem Higher -order functions
Funçõesoumétodossãohigh-orderquandotemacapacidadedereceberoutrasfun-
çõescomoargumentosouretornarfun çõescomoresultado. EmRubyistoéfeito
usandoblocos,lambdaseprocs.
Blocos,lambdaseprocssãoumdosaspectosmaispoderosodalinguagemRuby,
etambémumdosquecausammaisconfusõesparaserementendidos,issoporque
Rubypossuiquatromaneirasdelidarcomhigh-orderfunctions.
Bl o c o s
Esteéométodomaiscomumtrabalharcomfun çõeshigh-orderemRuby. Os
blocossãomuitoutilizadosecomunsquandopercorremoscole ções:
numeros = [1 , 2, 3, 4]
numeros.each { |numero| p numero }
# => 1
# => 2
# => 3
# => 4
Masoqueestáacontecendonessecódigoafinal?
Aprimeirae mais importantepartequedevemosentender,estánachamadaao
métodoeachquefizemosnavariável numeros.Aoinvocarmosométodo,estamos
passandoumafun çãooublocodecódigocomoargumento.Internamenteométodo
eachiterao Array,executaoblocodecódigorecebidocomoargumentopassando
ovalordaitera ção(nestecasoavariável numero).Oblocodecódigoquerecebea
variávelnumeroestáimprimindoamesmanoconsoleutilizandoométodo p.
Existemoutrosmétodosdaclasse Arrayquerecebemumblocodecódigocomo
argumentoeoexecutamacadaitera ção.Porexemplo,ométodo collect:
numeros = [1 , 2, 3, 4]
numeros_ao_quadrado = numeros.collect { |numero| numero ** 2 }
p numeros_ao_quadrado # => [1, 4, 9, 16]
Ocomportamentodométodo collectésimilaraométodo each,cadaitem
do Arrayondeométodofoiinvocadoépassadocomoargumentoparaobloco
recebidonachamada.
69

## Página 84

5.5. Crieseuprópriocódigoqueusaumblocodecódigo CasadoCódigo
Ao invocar o métodocollect obtemos um novo Array com todos
os números ao quadrado. Desta maneira, quando imprimimos a variável
numeros_ao_quadradooresultadoé [1, 4, 9, 16].
TantoométodoeachquantoométodocollectfazempartedaAPIpúblicada
classe Array.ExistemváriosoutrosmétodobastanteúteisnaAPIdosarrays,você
devesempreconsultá-laparanãoreimplementarcomportamentosquejáexistem.
Lembre-sequeumdosprincipaisatrativosdalinguagemRubyéasualegibilidade,
conhecerbemaAPIdalinguageméumdospassosmaisimportantesparaconseguir
talvantagem.
5.5 C rie seu próprio código que usa um bloco de có -
digo
Masesequisermoscriarnossoprópriométodoquerecebeumblocodecódigo?
Comopodemosimplementá-lo?
Vamoscriarummétodoquefiltraoslivrosporumadeterminadacategoria,itera
cadaumdesteslivroseexecutaumblocodecódigoqueserápassadoparaestemé-
todo.Nossoprimeiropassoserácriarométododentrodaclasse Biblioteca:
class Biblioteca
def initialize
@livros = {} # Inicializa com um hash
end
def adiciona(livro)
@livros[livro.categoria] ||= []
@livros[livro.categoria] << livro
end
def livros
@livros.values.flatten
end
def livros_por_categoria(categoria)
@livros[categoria]
end
end
Ofiltroporcategoriaébemsimples,oargumentoesperadoseráo Symbol
70

## Página 85

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
identificadordotipodoslivrosquedesejamos.Agoraprecisamositeraresteslivros
eexecutarumblocodecódigopassadocomoargumentonachamadadométodo
livros_por_categoria:
class Biblioteca
def initialize
@livros = {} # Inicializa com um hash
end
def adiciona(livro)
@livros[livro.categoria] ||= []
@livros[livro.categoria] << livro
end
def livros
@livros.values.flaten
end
def livros_por_categoria(categoria)
@livros[categoria].each do |livro|
yield livro
end
end
end
Quandofiltramososlivrosporcategoria: @livros[categoria],recebemos
comoretornoum Array,eagorapodemospercorrê-loutilizandoométodo each
querecebeumblocodecódigo,eoexecutaN(númerodelivrosquecontémdentro
do Array)vezes,sendoqueacadaitera çãooblocoéexecutadorecebendooitem
(nocasoumobjetodotipo Livro)navariável livroquedeclaramosentreos
caracteres ||.
Outranovidadeéquediferentementedosatributos,blocosnãoprecisamserde-
claradosnaassinaturademétodo,paraexecutá-losbastachamarométodo yield
passandoosargumentosqueserãorecebidospeloblocodeclaradonachamadado
métodolivros_por_categoria.Ométodo yieldexecutaráautomaticamente
oblocoqueforpassadonachamadadométodo.
Agorabastainvocarométodopassandoa categoriapelaqualdesejamosefe-
tuarofiltroetambémoblocodecódigoqueseráexecutadoparacadaumdosobjetos
dotipo Livroencontradosno Array(adicionetambémo attr_readerparao
atributo autornaclasse Livro):
71

## Página 86

5.5. Crieseuprópriocódigoqueusaumblocodecódigo CasadoCódigo
biblioteca = Biblioteca.new
teste_e_design = Livro.new "Mauricio Aniche" , "123454",
247, 69.9, :testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565",
189, 69.9, :web_design
biblioteca.adiciona teste_e_design
biblioteca.adiciona web_design_responsivo
biblioteca.livros_por_categoria :testes do |livro|
p livro.autor
end
=> "Mauricio Aniche"
Quando executamos o métodolivros_por_categoria passamos um
Symbol :testesquerepresentaacategoriadelivrosquedesejamosfiltraretam-
bémumblocodecódigoquerecebenavariável livrodeclaradadentrodoscarac-
teres ||cadaumdosobjetosexistentesparaacategoriafiltrada.
Agrandevantagemdestaabordageméquepossuímosumamaneiraflexívelde
interagircomométodo,ouseja,oblocopassadanachamadadométodopodede-
cidirqualcomportamentoexecutarcomcadaumdosobjetosrecebidos.
Vocêsempredevepensaremblocoscomoumamaneiradeflexibilizarosméto-
dosdasuaAPI.Nóspodemos,porexemplo,aoinvésdeimprimironomedoautor
noconsole,imprimi-loemumaimpressora:
biblioteca = Biblioteca.new
impressora = Impressora.new
teste_e_design = Livro.new "Mauricio Aniche" , "123454",
247, 69.9, :testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565",
189, 69.9, :web_design
biblioteca.adiciona teste_e_design
biblioteca.adiciona web_design_responsivo
biblioteca.livros_por_categoria :testes do |livro|
impressora.imprime livro .autor
end
72

## Página 87

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
Aclasse Impressorapoderiaserumaimplementa çãoqueenviadadospara
umaimpressoraconectadaviaUSBoumesmoviaredesemfio. Oquequerolhe
mostraréquetrocandoapenas uma linha,mudamosocomportamentoeamaneira
queinteragimoscomométodo livros_por_categoria.Eleéummétodofle-
xível,querecebeumblocodecódigoondepodemoscustomizarocomportamento
quedesejamos.
Evite erros quando um bloco não é passado
Ométodo livros_por_categoriaesperaqueumblocodecódigosejapas-
sadocomoargumento.Porém,seesteblocoforutilizadointernamente,masnãofor
passadocomoargumento,ocorreráumerroinformandoqueestemétododeveria
tersidoinformado:
biblioteca = Biblioteca.new
teste_e_design = Livro.new "Mauricio Aniche" , "123454",
247, 69.9, :testes
biblioteca.adiciona teste_e_design
biblioteca.livros_por_categoria :testes
# => LocalJumpError: no block given (yield)
Podemosresolveresteproblemadeformadefensiva,evitandoumerrocasone-
nhumblocodecódigosejainformadoutilizandoométodo block_given?que
estádisponívelemtodososobjetoscriadosemRuby:
class Biblioteca
def livros_por_categoria(categoria)
@livros[categoria].each do |livro|
yield livro if block_given?
end
end
end
biblioteca = Biblioteca.new
teste_e_design = Livro.new "Mauricio Aniche" , "123454",
247, 69.9, :testes
73

## Página 88

5.6. ExplorandoaAPIEnumerable CasadoCódigo
biblioteca.adiciona teste_e_design
biblioteca.livros_por_categoria :testes
Ométodoblock_given?verificasealgumblocofoipassadocomoargumento
nachamadadométodoeretornaumvalorbooleano. Emnossoexemplo,casoal-
gumblocosejapassado,oexecutamos,casocontrárioométodo yieldnãoserá
invocado.
Estátécnicadefensivaémuitoútilquandocriamosframeworksqueserãouti-
lizadosporváriasbasesdecódigoRubyeondenãotemosmuitocontrolesobreos
clientesdestasAPIsqueestamoscriando.
5.6 E xplorando a API Enumerable
As classesArraye Hashquevimosatéomomento,possuemmétodoscomuns
entreelas,quesãodisponibilizadosporummódulo(veremosmódulosembreve)
chamado Enumerable. Estesmétodospermitemexecutartarefascomcole ções,
comapenasumaouduaslinhasdecódigoRuby.
M é t o d oinject
Vamoscriarumaclassechamada Relatoriodentrodeumnovoarquivocha-
mado relatorio.rbqueficarádentrodapasta libdoprojeto.Estaclasseterá
umasériedemétodosparafornecerdadosimportantesreferentesaoslivrosquete-
moscadastrados. Paracomeçar,vamoscriarummétodoqueretornaasomatotal
dospreçosdetodososlivrosquetemoscadastradosnabiblioteca:
class Relatorio
def initialize(biblioteca)
@biblioteca = biblioteca
end
def total
soma = 0.0
@biblioteca.livros.each do |livro|
soma += livro.valor
end
soma
7 4

## Página 89

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
end
end
Antesdecriarostestesparaestanovaclasse,nãoseesque çadeadicionaro
requiredentrodoarquivo lob/loja_virtual:
require File.expand_path('lib/livro')
require File.expand_path('lib/biblioteca')
require File.expand_path('lib/relatorio')
Agorabastaadicionaralgunslivrosdentrodabibliotecaeapósissocriarum
objetodotipo Relatoriopassandocomodependênciaoobjeto Bibliotecae
invocarométodo totalqueacabamosdecriar:
biblioteca = Biblioteca.new
teste_e_design = Livro.new "Mauricio Aniche" , "123454",
247, 69.9, :testes
web_design_responsivo = Livro.new "Tárcio Zemel" , "452565",
189, 69.9, :web_design
biblioteca.adiciona teste_e_design
biblioteca.adiciona web_design_responsivo
relatorio = Relatorio.new biblioteca
p relatorio.total # => 139.8
Podemosmelhoraressecódigo,utilizandoeconhecendoumpoucomaisdaAPI
Enumerable,quepossuiummétodochamado inject,quesimplificamuitoocó-
digo:
class Relatorio
def initialize(biblioteca)
@biblioteca = biblioteca
end
def total
@biblioteca.livros.inject(0) { |tot, livro | tot += livro.valor }
end
end
75

## Página 90

5.6. ExplorandoaAPIEnumerable CasadoCódigo
Ométodo injectrecebecomoprimeiroargumentoumvalorqueseráatri-
butoavariávelacumuladora,geralmenteinicializadoem0,osegundoargumento
éumblocoquerecebeoutrosdoisargumentos,oprimeiroéavariávelacumula-
dora,quefoiinicializadaanteriormente,noexemplo,0. Jáosegundoargumento
serefereacadaumdoslivrosexistentesno Arraydelivrosretornadospeloobjeto
Biblioteca.Acadaitera çãosomamosovalordoobjeto Livroàvariávelacumu-
ladoraquechamamosde total,nofinalovalordestavariáveléretornadocomo
resultadodométodo.
M é t o d omap
Aclasse Relatorioprecisaagoradeummétodoqueretorneotítulodetodos
oslivrosquepossuímosnoobjeto Biblioteca.Porémaclasse Livronãopossui
umatributo titulo,sendoassim,nossoprimeiropassoseráadicionaresteatributo
elogicamenteummétodoacessorparavisualizarotítulodolivro,jáqueoatributo
seráprivado:
# coding: utf-8
class Livro
attr_accessor :valor
attr_reader :categoria, :autor, :titulo
def initialize(titulo, autor, isbn = "1", numero_de_paginas,
valor, categoria)
@titulo = titulo
@autor = autor
@isbn = isbn
@numero_de_paginas = numero_de_paginas
@categoria = categoria
@valor = valor
end
def to_s
"Autor: #{ @autor}, Isbn: #{ @isbn},
Páginas: #{ @numero_de_paginas},
Categoria: #{ @categoria}"
end
def eql?(outro_livro)
@isbn == outro_livro.isbn
76

## Página 91

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
end
def hash
@isbn.hash
end
end
Opróximopassoécriarométodo titulosnaclasse Relatorioqueserá
responsávelporretornarotítulodoslivrospresentesnabiblioteca:
class Relatorio
def initialize(biblioteca)
@biblioteca = biblioteca
end
def total
@biblioteca.livros.inject(0) { |tot, livro | tot += livro.valor }
end
def titulos
titulos = []
@biblioteca.livros.each do |livro|
titulos << livro.titulo
end
titulos
end
end
biblioteca = Biblioteca.new
biblioteca.adiciona Livro.new "TDD", "Mauricio Aniche" , "123454",
247, 69.9, :testes
biblioteca.adiciona Livro.new "Design Responsivo" , "Tárcio Zemel" ,
"45256", 189, 69.9, :web_design
relatorio = Relatorio.new biblioteca
p relatorio.titulos # => ["TDD", "Design Responsivo"]
Ométodo titulospossuiomesmoproblemadométodo totalemsuapri-
77

## Página 92

5.6. ExplorandoaAPIEnumerable CasadoCódigo
meiraversão:Muitocódigoparaumatarefaextremamentesimples.Novamentese
conhecermosaAPIEnumerable,podemossimplificarocódigoutilizandoummé-
todochamado map:
def titulos
@biblioteca.livros.map { |livro| livro.titulo }
end
Ométodo mapiterasobreum Array,eparacadaelemento(nestecasoum
objeto Livro)executaumblocodecódigopassadocomoargumento.Oresultado
daexecuçãodestebloco,éguardadodentrodeum Arrayacumulador,queére-
tornadonofinaldaitera çãodetodososlivros. Nocódigoacima,oresultadoda
execuçãodoblocoéo titulodo Livro,comopossuímosdoisobjetos Livro
dentrodabiblioteca,oretornodométodo mapseráum Arraycontendootítulos
dosdoislivros.
Ométodo mappossuiomesmocomportamentodométodo collectquefoi
vistoanteriormente.Essencialmenteométodo collectfoicriadoparasatisfazer
programadoresSmalltalkquepossuiummétodosimilar.Jáométodo mappossuio
mesmonomedemétodossimilaresdelinguagenscomoScala.
Método map com notação simplificada
Existeumamaneiramaissimplesdepassarumbloconachamadaaométodo
map:
class Relatorio
def initialize(biblioteca)
@biblioteca = biblioteca
end
def total
@biblioteca.livros.inject(0) { |tot, livro | tot += livro.valor}
end
def titulos
@biblioteca.livros.map &:titulo
end
end
A expressão &:titulo cria um bloco como este: { |livro|
78

## Página 93

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
livro.titulo }. Ocharacter & invocaummétodo to_proc no objeto, e
passaesteblocoparaométodo map.
Simplificando uso do método inject
Aprendemosqueépossívelsimplificarousodométodo maputilizandoanota-
ção &:method.Ométodo injectpossuiumasimplificaçãoquando,porexemplo,
desejamosqueosvaloresdetodososlivrossejamsomados.Ocódigoatualdomé-
todo totaléassim:
class Relatorio
def total
@biblioteca.livros.inject(0) { |tot, livro | tot += livro.valor}
end
end
Podemosutilizarométodo mapparaobterumnovo Arrayapenascomos
valoresdetodososlivrosexistentes:
class Relatorio
def total
@biblioteca.livros
.map(&:valor).inject(0) { |tot, valor | tot += valor}
end
end
Ométodo injectpossuiumavaria ção,ondeépossívelpassarum Symbol
enãoumblococomoargumentoemsuachamada. Estavaria çãoentendequeo
símbolopassadocomoargumentorefere-seaométodoqueseráchamadonavariável
acumuladora,nocódigoacima,seriaométodo +:
class Relatorio
def total
@biblioteca.livros.map(&:valor).inject(:+)
end
end
Ométodo+entãoseráinvocadoautomaticamentenavariávelacumuladorapara
cadaumadasitera çõesfeita,recebendocomoargumentoavariável valorquere-
presentaoitemiterado.Outrodetalheéquenãofoinecessárioinicializaravariável
acumuladora,automaticamenteelaécriadacomovalor0.
79

## Página 94

5.7. Parasabermais:Outrasmaneirasdecriarblocos CasadoCódigo
5.7 P ara saber mais : O utras maneiras de criar blo -
cos
P r o c s
Na seçãoanteriorexecutamosblocosdecódigoatravésdométodo yield.Umase-
gundamaneiraérecebermosoblocodecódigocomoumargumentodotipo Proc.
Vamosverocódigoedepoisdiscutiremosasdiferen ças:
class Biblioteca
def initialize
@livros = {} # Inicializa com um hash
end
def adiciona(livro)
@livros[livro.categoria] ||= []
@livros[livro.categoria] << livro
end
def livros
@livros.values.flaten
end
def livros_por_categoria(categoria, &bloco)
@livros[categoria].each do |livro|
bloco.call livro
end
end
end
biblioteca = Biblioteca.new
biblioteca.adiciona Livro.new "TDD", "Mauricio Aniche" , "123454",
247, 69.9, :testes
biblioteca.adiciona Livro.new "Design Responsivo" , "Tárcio Zemel" ,
"45256", 189, 69.9, :web_design
biblioteca.livros_por_categoria :testes do |livro|
p livro.autor
end
80

## Página 95

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
=> "Mauricio Aniche"
O código é bastante parecido, porém possui duas importantes diferenças.
A primeira é que passamos um argumento chamado&bloco para o método
livros_por_categoria.Ocaractere &indicaqueestamosrecebendoumains-
tânciade Procquenarealidadeéoblocodecódigoquevamosexecutar. Ase-
gundadiferençaéquenãoinvoca-seoblocodecódigochamandoométodo yield,
agorainvocamosométodo callnoargumentorecebidonadeclara çãodométodo
(bloco).
Oqueaindanãoficamuitoclaroéporqueusaríamosuma Procaoinvésdeum
simples yield?
Asvezesprecisamosexecutaromesmoblocodecódigováriasvezes,umobjeto
dotipo Procguardaumblocodecódigo,epodeserpassadocomoparâmetrovárias
vezesparaefetuarachamadadeummesmométodo,porexemplo:
class Biblioteca
def initialize
@livros = {} # Inicializa com um hash
end
def adiciona(livro)
@livros[livro.categoria] ||= []
@livros[livro.categoria] << livro
end
def livros
@livros.values.flatten
end
def livros_por_categoria(categoria)
@livros[categoria].each do |livro|
yield livro if block_given?
end
end
end
biblioteca = Biblioteca.new
biblioteca.adiciona Livro.new "TDD", "Mauricio Aniche" , "123454",
81

## Página 96

5.7. Parasabermais:Outrasmaneirasdecriarblocos CasadoCódigo
247, 69.9, :testes
imprime_livro_no_console = Proc.new do |livro|
p livro.autor
end
biblioteca.livros_por_categoria :testes, imprime_livro_no_console
# => ArgumentError: wrong number of arguments (2 for 1)
O que fizemos foi definir um objeto Proc na variável
imprime_livro_no_console que guarda o bloco de código que havíamos
criadoanteriormente,comissopodemospassá-loparaqualquermétodoquerecebe
umblococomoargumento.
Oúnicoproblemaéqueocódigoacimanãofunciona,eamensagemdeerropa-
recebemestranha.Elanosdizqueestamosinvocandoummétodoque devereceber
umargumentopassandodois.Issoquedizerqueobloconãocontacomoargumento
dométodo?
Exatamente. Ométodo livros_por_categoriarecebeapenasumargu-
mentoexplícitochamado categoriaooutroéumbloco,quecomonaantiga
implementação,nãoprecisanecessariamenteserpassado. Masissoaindanãoex-
plicaoerroretornado,afinal,tudobemqueoblocopodeserounãopassado,mas
nomeuexemploeudesejopassá-lo.
Oqueaconteceéqueavariável imprime_livro_no_consolequeestáaguar-
dandoa Procquefoicriadaéumobjeto,ouseja,quandoinvocamosométodo
livros_por_categoria passando o objetoimprime_livro_no_console
comoargumento,écomoseestivéssemospassandoqualqueroutroargumentona
chamada.Porém,sabemosqueométodorecebeapenasumargumento,obrigatori-
amente.
O que precisamos fazer é transformar o objeto do tipo Proc
imprime_livro_no_console em um bloco convencional e passar este bloco
comoargumentonachamadadométodo. Essatransforma çãoéfeitautilizandoo
caractere &:
biblioteca = Biblioteca.new
biblioteca.adiciona Livro.new "TDD", "Mauricio Aniche" , "123454",
247, 69.9, :testes
82

## Página 97

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
imprime_livro_no_console = Proc.new do |livro|
p livro.autor
end
# transforma objeto proc em um bloco convencional
biblioteca.livros_por_categoria :testes, &imprime_livro_no_console
Aoadicionarocaractere &antesdavariávelqueguardaoblocoquedesejamos
passarcomoargumentoparaométodo livros_por_categoria,eleseráauto-
maticamente‘convertido’paraumblococonvencionalnovamente.
Destamaneira,ométodo livros_por_categoriacontinuarecebendoeexe-
cutandoumblocoatravésdachamadaaométodo yield.Avantageméqueobloco
emumobjetodotipo Procpodeserreutilizadoemoutraspartesdocódigo.
Recebendo dois blocos como argumento
Casosejanecessárioemalgummomento,receberdoisblocoscomoargumento
deummétodo,autiliza çãodo yieldtorna-seobsoleta,jáquenãoseriapossível
descobrirqualdosdoisblocosdeveriaserexecutado.
Neste caso, a soluçãoéreceberexplicitamenteosdoisblocoscomoargumentos
dométodo.Porém,comoobjetosdotipo Procenãoblocosconvencionais:
class Biblioteca
def livros_por_categoria(categoria, bloco_com_p, bloco_com_puts)
@livros[categoria].each do |livro|
# Sem o &, transformamos o bloco em um objeto novamente
bloco_com_p.call livro
bloco_com_puts.call livro
end
end
end
biblioteca = Biblioteca.new
biblioteca.adiciona Livro.new "TDD", "Mauricio Aniche" , "123454",
247, 69.9, :testes
imprime_livro_no_console = Proc.new do |livro|
p livro.autor
end
83

## Página 98

5.7. Parasabermais:Outrasmaneirasdecriarblocos CasadoCódigo
imprime_livro_no_console_com_puts = Proc.new do |livro|
puts livro.autor
end
biblioteca.livros_por_categoria :testes,
imprime_livro_no_console,
imprime_livro_no_console_com_puts
Comorecebemosdoisobjetosdotipo Proc,nãoépossívelinvocá-losatravés
dométodo yield,comofoidito.Devemostratá-loscomo Procs,porisso,para
executá-losénecessárioinvocarométodocallemcadaumdeles.
Seoblocopassadocomoargumentorecebermaisdeumargumento,bastainvo-
carométodocallpassando-osseparadospor ,,assimcomoseriafeitonachamada
utilizando yield.
Lambdas
Existemoutramaneiradeguardarumblocodecódigoemumavariávelepassá-
locomoargumentonachamadadeummétodo,sãooslambdas,quesãoconhecidos
tambémcomofunçõesanônimas:
biblioteca = Biblioteca.new
biblioteca.adiciona Livro.new "TDD", "Mauricio Aniche" , "123454",
247, 69.9, :testes
imprime_livro_no_console = lambda do |livro|
p livro.autor
end
biblioteca.livros_por_categoria :testes, &imprime_livro_no_console
=> "Mauricio Aniche"
Oslambdasseparecemmuitocomprocs,entretanto,existemduasdiferen ças.
Aprimeiraéquequandoutilizamoslambdas,aocontráriodasprocs,existeuma
checagemdaquantidadedeparâmetrospassados:
biblioteca = Biblioteca.new
biblioteca.adiciona Livro.new "TDD", "Mauricio Aniche" , "123454",
84

## Página 99

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
247, :testes
imprime_livro_no_console = lambda do
p 'executou lambda '
end
imprime_livro_no_console_proc = Proc.new do
p 'executou proc '
end
biblioteca.livros_por_categoria :testes, &imprime_livro_no_console_proc
=> NameError: undefined local variable or method `livro'
biblioteca.livros_por_categoria :testes, &imprime_livro_no_console
=> ArgumentError: wrong number of arguments (0 for 1)
Quandoinvocamosométodo livros_por_categoriapassandoumobjeto
dotipo Proc,nainvoca çãodobloconenhumargumentoéesperado,masmesmo
assimo pcolocadoéexecutado.Quandooblocopassadoédotipo Lambda,acon-
teceumerro: ArgumentErrorinformandoqueoblocodeveriaesperarpelomenos
1argumento,entretantonenhumfoideclarado.
A segunda diferença acontece quando utilizamosreturn dentro de um
lambda.Quandodeclaramosum returndentrodeum lambda,ométodoque
invocouoblocoreceberáoretornodesteblocoecontinuarácomsuaexecu çãonor-
malmente.Seutilizarmosum returndentrodeuma procométodoqueinvocouo
blocoseráinterrompidoeseuretornoseráovalorretornadonaexecu çãodamesma.
Vamosverumpequenoexemploparadeixarascoisasmaisclaras:
def proc_com_return
Proc.new { return "retornando algo de uma proc" }.call
"Proc finalizada"
end
def lambda_com_return
lambda { return "retornando algo de um lambda" }.call
"Lambda finalizado"
end
puts proc_com_return
puts lambda_com_return
85

## Página 100

5.8. Parasabermais:Currying CasadoCódigo
# => retornando algo de uma proc
# => Lambda finalizado
Procssãocomoprocedures,apenaspartedecódigoqueserãoexecutadoscomo
partedocomportamentodeummétodo.Lambdasseparecemmaiscommétodos,
ondeexistechecagemdonúmeroparâmetrosenãosobrescrevemo returndefi-
nidonométodoqueosinvocaram.Existeapenasumcasoondeé necessárioobri-
gatoriamenteinvocarummétodopassandoumainstânciade lambdaenãoum
instânciade proc:
def metodo_que_recebe_um_bloco(bloco)
bloco.call
"retornando algo do método"
end
p metodo_que_recebe_um_bloco(Proc.new { return "Retorno da Proc" })
p metodo_que_recebe_um_bloco(lambda { return "Retorno do Lambda" })
# => LocalJumpError: unexpected return
# => retornando algo do método
OinterpretadorRubynãopermitequeumargumentopassadoparaummétodo
contenhaum return.Emnossoexemploa Procpossuiumreturnexplícito,por
estemotivo,aconteceoerro: LocalJumpError. Comolambdassecomportam
comométodos,elespodemconterum returnexplícito.
5.8 P ara saber mais : Currying
Curryingéumatécnicamuitoutilizadaemlinguagensfuncionais,queconsisteem
transformarumafun çãoquerecebemúltiplosargumentosemumasequênciade
funçõesquerecebemumúnicoargumento.Adefini çãopareceumpoucocompli-
cado,maspodesersimplificadacomumpoucodecódigo,vamosver:
executa_comando = lambda { |conexao, comando | conexao.executa comando }
executa_comando.call Conexao.new, Update.new
Ocódigoacimasimulaaexecu çãodeumcomandoqualquer(noexemploum
Update)emumbancodedadosatravésdachamadadeummétodo executaem
umobjetodotipo conexao.Criamosumlambdaquerecebedoisargumentos:a
86

## Página 101

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
conexãocomobancoeocomandoquedesejamosexecutar,apósissoexecutamos
estelambdapassandoosargumentosnecessários.
Emdeterminadomomentopodeserútilexecutarolambda executa_comando
passandoumcomando Insert,comodemonstradonocódigoabaixo:
executa_comando = lambda { |conexao, comando | conexao.executa comando }
executa_comando.call Conexao.new, Update.new
executa_comando.call Conexao.new, Insert.new
Reparequesemprequevamosexecutarolambda executa_comandoprecisa-
mospassaraconexao,oúnicoparâmetroquemudoufoio comando.Paramelhorar
estecódigo,podemosutilizaratécnicadecurrying:
executa_comando = lambda { |conexao, comando | conexao.executa comando }
.curry
executa_comando_com_conexao = executa_comando.call Conexao.new
executa_comando_com_conexao.call Update.new
executa_comando_com_conexao.call Insert.new
Quandoinvocamosométodo currynoobjeto Lambda,nósoparticionamos
emduasfun ções,poisolambdarecebedoisargumentos. Aprimeirafun çãoque
receberáoobjeto Conexao,quandoinvocamosestaprimeirafun ção,elaretorna
asegundafun ção,quenesteexemplo,receberáoargumentoreferenteaocomando
quedesejamosexecutar: Insertou Update.Aoinvocarestasegundafun ção,o
conteúdodefinidoinicialmentenoobjetolambdacriado,seráfinalmenteexecutae
aoperaçãoseráefetuadautilizandoaconexaoeocomandoqueforampassados.
Agrandevantagemdousodecurryingéquandovamosexecutaromesmobloco
decódigo,sejaeleumlambdaouumaproc,ealgunsparâmetrossãosempreosmes-
mos.Utilizandoestatécnicapodemosfixaralgunsargumentoscomomesmovalor,
independentedaquantidadedevezesqueoblocoforexecutado.Tambémémuito
útilquandoqueremosdeixarocódigomaisclaroeconciso,porexemplo:
multiplicador = lambda { |x, y | x * y }
p multiplicador.call 2, 13
# => 26
Ocódigoacimaébemsimples,elecriaumlambdaquemultiplicadoisargumen-
tospassados xe yeretornaoresultado.Noexemplo,foicalculadoodobrodovalor
13.Agoradesejamoscalcularodobrodonúmero 43,fazemosistocomumasimples
chamadaao multiplicador:
87

## Página 102

5.9. Parasabermais:Closure CasadoCódigo
multiplicador = lambda { |x, y | x * y }
p multiplicador.call 2, 13
p multiplicador.call 2, 43
# => 26
# => 86
Utilizandocurryingpodemosdeixarocódigoumpoucomaislegível:
multiplicador = lambda { |x, y | x * y } .curry
dobro = multiplicador.call 2
p dobro.call 13
p dobro.call 43
# => 26
# => 86
Particionamosolambdaemduasfun ções,aprimeirarecebeoargumento x,eao
invocarestaprimeirafun çãopassandocomoargumentoovalor 2,achamamosde
dobro,afinalnãoimportaqualsejaovalorpassadonachamadadasegundafun ção,
ovalorde xestáfixoem 2.
5.9 P ara saber mais : Closure
Quandocriamosumblocodecódigo(lambda,procoublococonvencional)elepos-
suiacessoàsvariáveisvisíveisdoescopoondeforamcriados,equalqueraltera ção
nestasvariáveisserãorefletidasnoescopooriginal,ouseja,osblocospossuemuma
espéciedelinkcomasvariáveisdefinidasnoescopodeorigem.Porexemplo:
soma = 0
[1, 3, 5, 6, 9].each do |numero|
soma += numero
end
p soma # => 24
Reparequeoblocodecódigoquedefinimosepassamosnachamadaaométodo
eachpossuiacessoavariável somaquefoidefinidanoescopoondeoblocofoi
88

## Página 103

CasadoCódigo Capítulo5. Rubyeaprogramaçãofuncional
criado.Estacapacidadedefazer bindcomasvariáveisqueforamdefinidasnoescopo
ondeoblocofoicriadoéconhecidocom closure.
Estecomportamentopodeserconfirmadoaoexecutarmososeguinteexemplo:
def imprime_numero
numero = 134
yield
end
def chama_metodo_imprime_numero
numero = 42
imprime_numero do
puts "O número aqui é: #{ numero}"
end
end
chama_metodo_imprime_numero # => 42
Onúmeroimpressoé 42porquenoescopoondeoblocofoicriadoavariável
numeropossuiovalor 42.Nocontextoondeoblocofoi invocadoexisteumoutra
variávelnumerocomovalor 134,porémestasegundavariávelfoidefinidano
contextodométodo imprime_numeroenãoévisívelaobloco.
5.10 P róximos passos
Nestecapítuloaprendemosconceitosimportantesdeumoutroparadigmadepro-
gramação:ofuncional.Existemváriosconceitosdesteparadigmaespalhadospelos
maisimportantescódigosescritosemRubymundoafora. Portanto,possoafirmar
quevocêveráeutilizaráesterecursos,principalmenteosblocos,quenaminhaopi-
niãosãoosmaisimportantesequepodemcontribuirparaquevocêcriecódigos
eleganteselegíveis.
TambémaprendemosautilizarumpoucodaAPIEnumerablequepossuivários
métodoúteisparatrabalharmoscomcole çõesemRuby. ConhecerestaAPIéum
excelentecaminhoparacriarcódigosmaislegíveisefuncionaisquandolidamoscom
coleções,estude-aetenhaolinkdaAPI: http://ruby-doc.org/core-1.9.3/Enumerable.
htmlsempreabertoquandoestivertrabalhandoouestudando.
NopróximocapítuloveremosumpoucodaAPIde FiledoRuby,elaserámuito
importanteparacriarmosumespéciedeframeworkquesalvaerecuperadadosos
livroscriadosutilizandoarquivosemdisco.
89

## Página 105

Capítulo6
ExplorandoAPIFile
Agoraqueconhecemoseaprendemosautilizarblocos,temostodooconhecimento
necessárioparapartirmospraAPIdoRubyquelidacomarquivosediretórios.Uti-
lizaremosessaAPIparasalvarmososobjetosquerepresentam Livroemnosso
sistema.Veremostambémcomotrabalharcomserializa çãoedeserializa çãodeob-
jetos,queseráamaneiraquesalvaremosnossosobjetosemdisco.
6.1 U m pouco da classe File
Aclasse FiledaAPIdoRubyéumaabstra çãodeobjetosquesãocriadospara
representarumarquivo.Podemos,porexemplo,descobrirqualotamanho,embytes,
deumarquivosalvoemdisco:
arquivo_temporario = File.new("/tmp/arquivo")
p arquivo_temporario.size # => 564
AAPIdearquivospossuiumagrandevariedadedemétodosqueutilizamblocos
comoformadeintera ção.Podemoscriarumarquivoeincluirdadosdentrodelecom

## Página 106

6.1. UmpoucodaclasseFile CasadoCódigo
apenasumalinhadecódigo:
File.open("/tmp/arquivo", "w") do |arquivo_temporario|
arquivo_temporario.puts "primeira linha do meu arquivo"
end
Escrevendo com o método WRITE
Podemosescreverdentrodeumarquivoutilizandoométodo write
aoinvésdométodo puts.Aprincipaldiferen çaéqueométodo puts
adicionaumaquebradelinha \nnofinalda Stringquefoiincluída
noarquivo,enquantoométodo writenãoofaz.
Dadoquetemosoarquivotexto /tmp/arquivosalvo,podemosabri-loeim-
primircadaumadesuaslinhas:
arquivo_temporario = File.open "/tmp/arquivo", "r"
arquivo_temporario.each do |linha|
p linha # => "primeira linha do meu arquivo\n"
end
Modos de abrir um FI L E
Osegundoparâmetropassadoquandoinvocamosométodo open,é
omodoquedesejamosabriroarquivo.Asmaneirasmaiscomunssão:
•r-abreoarquivosomenteparaleitura
•w-abreoarquivosomenteparaescrita(sobrescrevetodoocon-
teúdodoarquivoseomesmoexistir)
•w+-abreoarquivotantoparaleituraquantoparaescrita(sobres-
crevetodooconteúdodoarquivoseomesmoexistir)
•a-abreoarquivosomenteparaescrita(come çaaescritanofinal
daúltimalinhaexistenteseoarquivojáexistir)
92

## Página 107

CasadoCódigo Capítulo6. ExplorandoAPIFile
AAPI Fileémuitoricaemdetalheseporissopoderíamosgastaralgumas
páginasexplicandotodososmétodosesuasutilidades.Porémvamosfazeralgomais
útil,vamoscomeçarasalvarosobjetosdaclasse Livroqueestamoscriandoesalvá-
losemarquivosparaposteriormentepoderlerestesdadoserecuperarosobjetos.
Poréménecessárioantescriarmosaclassequefaráestetrabalho.
6.2 S erialização de objetos
Serializaçãonadamaisédoqueoprocessodesalvarumobjetoutilizandoumsis-
temadearmazenamentoqualquer,comoporexemplo,umarquivo,ouatémesmo
transmiti-lopelarede.Estesdadossãosalvosemformatobináriaouformatotexto,
comoXML,JSON,YML,etcepodemserutilizadosposteriormentepararecriarum
objetoemmemóriacomomesmoestadoemqueelefoiarmazenado.
Rubypossuidoismecanismosdeserializa çãodeobjetosnativosdapróprialin-
guagem.Umdelesserializaosobjetosemumformatoqueéfácildeserlidoporum
serhumano,enquantoooutroserializaemumformatobinário.
Vamosutilizareexploraroformatohumanodeserializa çãoqueérepresentando
peloformato YAML(http://ruby-doc.org/core/classes/YAML.html).Qualquerob-
jetopodeserserializadoparaoformato YAMLsemomínimoesfor ço,gastandoape-
nasalgumaslinhasdecódigo:
require 'yaml'
teste_e_design = Livro.new "TDD", "Mauricio Aniche" , "123454",
247, 69.9, :testes
objeto_serializado = YAML.dump teste_e_design
p objeto_serializado
Asaídadessecódigoseráalgocomo:
"--- !ruby/object:Livro \nautor: Mauricio Aniche\nisbn: 247\n
numero_de_paginas: \"123454\"\n
titulo: TDD\nvalor: :testes\n"
A Stringquefoiimpressa,equepareceumpoucaestranha,éarepresenta-
çãodoobjeto teste_e_designnoformatotexto YAML,quepodeserfacilmente
adicionadodentrodeumarquivo.
Podemosdeserializaro YAMLquefoicriado,ecriarumaoutrainstânciade
Livro,comasmesmasinforma çõeseestadodoobjeto teste_e_design:
93

## Página 108

6.3. Salvandoobjetosemarquivos CasadoCódigo
outro_teste_e_design = YAML.load objeto_serializado
p outro_teste_e_design # => Autor: Mauricio Aniche, Isbn: 123454,
Páginas: 247, Categoria: testes
6.3 S alv ando objetos em arquivos
Noscapítulosanterioresguardamososobjetosdotipo Livrodentrodeum Hash,
separando-ospor categoria.Porém,agoravamossalvá-lostambémemarquivos,
anossaestratégiaserácriarumarquivocomtodososobjetosdotipo Livroque
foremcriadoseadicionadosnabiblioteca.
OidealédeixaralógicaquelidacomaAPI Fileseparadadalógicaexis-
tente na classeBiblioteca, por isso vamos criar uma nova classe chamada
BancoDeArquivosdentrodoarquivo lib/banco_de_arquivos.rb,jádefi-
nindoométodo salva:
require 'yaml'
class BancoDeArquivos
def salva(livro)
File.open("livros.yml", "a") do |arquivo|
arquivo.puts YAML.dump(livro)
arquivo.puts ""
end
end
end
Para testar este código, precisamos fazer orequire deste novo arquivo,
adicionando-odentrodoarquivo lib/loja_virtual:
require File.expand_path('lib/livro')
require File.expand_path('lib/biblioteca')
require File.expand_path('lib/relatorio')
require File.expand_path('lib/banco_de_arquivos')
Eagorasimpodemostestarocomportamentoimplementadonométodosalva:
teste_e_design = Livro.new "TDD", "Mauricio Aniche" , "123454",
247, 69.9, :testes
BancoDeArquivos.new.salva teste_e_design
94

## Página 109

CasadoCódigo Capítulo6. ExplorandoAPIFile
Abrimosoarquivo livros.yamlemmododeescrita,respeitandooconteúdo
jáexistenteeinserindonovosconteúdonofinaldoarquivo.Éimportanteressaltar
queseparamososobjetosserializadosatravésdeduaslinhas.Oconteúdodoarquivo
ésimilaraoconteúdoabaixo:
--- ! ruby/object:Livro
titulo: TDD
autor: Mauricio Aniche
isbn: '123454'
numero_de_paginas: 247
categoria: :testes
valor: 69.9
Na classeBibliotecaguardamososdadosemum Hasheagoravamos
também invocar o métodosalva para guardar os dados dentro do arquivo
livros.yml:
class Biblioteca
def initialize
@livros = {} # Inicializa com um hash
# Inicializa banco de arquivos
@banco_de_arquivos = BancoDeArquivos.new
end
def adiciona(livro)
@livros[livro.categoria] ||= []
@livros[livro.categoria] << livro
@banco_de_arquivos.salva livro
end
def livros
@livros.values.flaten
end
def livros_por_categoria(categoria)
@livros[categoria].each do |livro|
yield livro if block_given?
end
end
end
95

## Página 110

6.3. Salvandoobjetosemarquivos CasadoCódigo
teste_e_design = Livro.new "TDD", "Mauricio Aniche" , "123454",
247, 69.9, :testes
biblioteca = Biblioteca.new
biblioteca.adiciona teste_e_design
Podemosdeixarocódigoaindamaiseleganteutilizandoblocos:
class Biblioteca
def initialize
@livros = {}
@banco_de_arquivos = BancoDeArquivos.new
end
def adiciona(livro)
salva livro do
@livros[livro.categoria] ||= []
@livros[livro.categoria] << livro
end
end
def livros
@livros.values.flaten
end
def livros_por_categoria(categoria)
@livros[categoria].each do |livro|
yield livro if block_given?
end
end
private
def salva(livro)
@banco_de_arquivos.salva livro
yield
end
end
96

## Página 111

CasadoCódigo Capítulo6. ExplorandoAPIFile
Métodos priv ados
Ométodoarquivapodeserprivado,poisnãoexistenecessidadede
invocá-lodeforadaclasse Biblioteca.Paracriarmétodosprivados
emRuby,bastainvocarométodo privateeabaixodele,declararos
métodosquedesejaquesejamprivados.Oidealédeixá-lossempreno
finaldoarquivoondeaclasseestádefinida.
6.4 R ecuperando objetos salvos
Vamos alterar um pouco a classeBiblioteca. O primeiro passo será guar-
dar os objetos em umArray e com isso será necessário alterar o método
livros_por_categoriaparaqueelecontinueretornandoum Arraydoslivros
dacategoriaqueépassadacomoargumento:
class Biblioteca
attr_reader :livros
def initialize
@livros = [] # Inicializando com Array
@banco_de_arquivos = BancoDeArquivos.new
end
def adiciona(livro)
salva livro do
@livros << livro
end
end
def livros_por_categoria(categoria)
@livros.select { |livro| livro.categoria == categoria }
end
private
def salva(livro)
@banco_de_arquivos.salva livro
yield
end
97

## Página 112

6.4. Recuperandoobjetossalvos CasadoCódigo
end
Agoraométodo livro_por_categoriautilizaométodo selectexistente
naclasse Array. Ométodo livrosqueconsolidavatodososlivrosexistentes
dentrodo Hashfoiremovidoeagoraexisteapenasummétodoleitor: livrosque
retornaavariável @livros.
Vamosagorainicializaro Array @livroscomosdadosexistentesdentrodo
arquivolivros.yml.Paraissoseráprecisodeserializarosobjetosexistentesdentro
doarquivoetransformá-losnovamenteeminstânciasde Livro,utilizandoaclasse
YAML:
class BancoDeArquivos
def salva(livro)
File.open("livros.yml", "a") do |arquivo|
arquivo.puts YAML.dump(livro)
arquivo.puts ""
end
end
def carrega
$/ = "\n\n"
File.open("livros.yml", "r").map do |livro_serializado|
YAML.load livro_serializado
end
end
end
Ométodo carregaemsuaprimeiralinha,configuraoseparadordelinhasdo
arquivoparatrabalharcomduasquebras( \n\n),depoisoarquivo livros.ymlé
abertoemmodoleitura.Acadaitera çãooconteúdoserializadoétransformadoem
umainstânciade Livroatravésdométodoloaddaclasse YAML.Comoutilizamos
ométodomap,oretornodométodo carregaéumArraycomotodososobjetos
queforamdeserializados.
Podemosentãocarregarosobjetosserializadospresentesnoarquivoeadicioná-
losno Arraydeobjetos Livrodaclasse Bibliotecarepresentadopelavariável
@livros:
class Biblioteca
def initialize
@banco_de_arquivos = BancoDeArquivos.new
98

## Página 113

CasadoCódigo Capítulo6. ExplorandoAPIFile
end
def adiciona(livro)
salva livro do
livros << livro
end
end
def livros_por_categoria(categoria)
livros.select { |livro| livro.categoria == categoria }
end
def livros
@livros ||= @banco_de_arquivos.carrega
end
def salva(livro)
@banco_de_arquivos.salva livro
yield
end
end
Utilizamosavariável @livroscomcarregamento lazy,ouseja,sóbuscamos
osobjetosno BancoDeArquivosquandoavariávelforutilizadapelaprimeira
vez,porissoremovemosainicializa çãodavariávelnoconstrutor. Assim,ascha-
madassequentesretornamoconteúdocarregadopelaprimeiravez. Osmétodos
adicionae livros_por_categoriasãoosresponsáveisporinvocarométodo
privado livros,porissonãoacessammaisdiretamenteavariável @livros.
M é t o d oselect
Ométodo selectdaAPI Enumerablepercorretodoselementosexistentes
nacoleçãoondeométodofoichamado,eretornaum Arraycontendooselemen-
tositeradoscujaaexecu çãodoblocopassadoseja true,funcionandocomouma
espéciedefiltrodoobjetosquecompõeo Array.
Noexemploacima,seexistiremtrêsobjetosdotipo Livro(doispertencentesa
categoria :webeooutrodacategoria :testes)einvocarmosométodo select
definindoqueoretornodoblocoéacompara çãodacategoriado Livrocomuma
categoria :testes,oretornoseráum Arraycontendoapenaslivroscujacategoria
for :testes:
99

## Página 114

6.5. Próximospassos CasadoCódigo
biblioteca = Biblioteca.new
biblioteca.adiciona Livro.new "TDD", "Mauricio Aniche" , "123454",
247, 69.9, :testes
biblioteca.adiciona Livro.new "Web Design Responsivo" , "Tárcio Zemel" ,
"45256", 240, 69.9, :web
biblioteca.adiciona Livro.new "Web com JSF e JPA" , "Gilliard Cordeiro" ,
"543232", 270, 69.9, :web
biblioteca.livros_por_categoria :testes
# => Autor: Mauricio Aniche, Isbn: 123454, Páginas: 247,
Categoria: testes
6.5 P róximos passos
NestecapítulovimosumpoucosobreaAPI FiledoRuby,aprendemosacriareler
arquivosdodisco. Tambémrevimosalgunsconceitosdeserializa çãoqueestavam
perdidosemnossamemóriaeaprendemosqueemRubyexistemduasmaneirasna-
tivasdeserializarobjetos: YAMLqueéumaserializa çãomaisfácildeserlidapor
sereshumanose Marshallqueserializaosdadosemumformatobinário.
Opróximoassuntoseráocompartilhamentodecódigoentreasclasseseobjetos
Ruby. VeremosmaneirasdeaplicaroprincípioDRY(DontRepeatYourself)em
nossoscódigosutilizandotécnicasexistentesnoprincipaisframeworksebiblioteca
domundoRuby.
100

## Página 115

Capítulo7
CompartilhandoComportamentos:
Herança,MóduloseMixins
Umadasprincipaiscaracterísticadeumbomdesigndecódigoéaelimina çãode
duplicidadesdesnecessárias. OprincípioDRY(Don’tRepeatYourself)criadopor
AndyHunteDave Thomas,noexcelentelivro“ThePragmaticProgrammer”,propõe
quecadapequenaquantidadedecódigodevepossuirsomenteumarepresenta ção
emtodoosistema.
Emsistemasorientadosaobjetos,asclassessãoabstra çõesquepermitemque
determinadoscomportamentossejamisoladosjuntoscomosdadosquerepresentam
umaentidadenosistema,nanossaaplica ção,aclasse Livrocumpreestepapel,de
maneiraquetodososmétodoscriadosestãodisponíveisentretodasasinstâncias
criadasapartirdaclasse Livro.
Nofuturopodemosdecidirvenderalémdelivros,outrasmídiascomoDVD’s,
CD’setc. Estesobjetoscertamentepossuemdadosbastanteparecidos,comopor
exemplo,opre ço,jáqueestamoslidandocomumaaplica çãodevendas.Podemos

## Página 116

7.1. Herança:Compartilhandocomportamentoscomclasses CasadoCódigo
atémesmocriarrelatóriodosprodutosquetemosdisponíveis,eprecisamoscriar
umaclassequesejagenéricaparaquandocriarmosalgumoutrotipodemídia,não
precisarmosalteraraclassederelatório,oumesmooutrospontosdosistemasque
lidamcom Produto.
NestecapítuloveremosformasdecompartilharcomportamentosemRuby,o
primeirodelesébemconhecidodosdesenvolvedoresdomundodaorienta çãoaob-
jetos: Herança. Tambémconheceremosumamaneiraqueébemmaisutilizadae
conhecidapelacomunidadeRuby,masquenãosubstituiousodeheran ça,os mi-
xins.
Discutiremosasvantagensdecadaumadestasabordagenseveremosquando
devemosutilizarumououtro.
7 . 1 H erança : C ompartilhando comportamentos
com classes
Noscapítulosanterioresutilizamosbastanteométodo pparaimprimirdadosna
saídapadrão. Aprendemosqueométodo psempreinvocaummétodochamado
inspectnoobjetoquepedimosparaserimpresso.Ofatoéquenósnuncaimple-
mentamosessemétodoemnenhumadasclassesquecriamosatéagora.
Quandoinvocamosqualquermétodoemumobjeto,naverdadeestamosen-
viandoumamensagemparaeleesolicitandoquesejaexecutadoalgumcompor-
tamento. AlinguagemRubyprocuraqualmétododeveserexecutadoequandoo
encontra,executaomesmo.Porexemplo,quandoinvocamosométodo inspect
emumainstânciade Livro,ointerpretadorRubyiráprocurarométodonains-
tânciaquerepresentaepossuitodososmétodosdefinidosnaclasse Livro,caso
nãoencontre,ointerpretadortentaencontrá-loemalguma super classedaclasse
Livro:
p Livro.superclass # => Object
Eencontraométodo inspectdefinidonaclasse Object,queéasuperclasse
defaultdetodososobjetosquenãoestendemexplicitamentedeoutraclasse.
102

## Página 117

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
Herança Simples
EmRubypodemosfazercomqueumaclasseherdeapenasdeuma
únicaoutraclasse,oquecaracterizaoquechamamosdeHeran çaSim-
ples.
p Livro.superclass.methods # => [..., :inspect, ...]
Listando os métodos de uma classe
Ométodo methodsretornatodososmétodosdisponíveisparaos
objetosquesãocriadosapartirdaclasseoude subclasses.Podemospor
exemplo,listarosmétodosdaclasse Objecteassimconcluirmosque
eladisponibilizaométodo inspectparaosobjetosdotipo Livro,já
que Livroherdade Object.
Vamoscomeçaralidarcomoutrosobjetosemnossalojavirtual.Agoravamos
criar DVD’s,ejáconseguimospensaremabstraçõesparaestasduasclasses,porexem-
plo,todo Livroe DVDpossuemum titulo, valoreuma categoria.Portanto
vamoscriarumaclasse Midia,queficarádentrodoarquivo lib/midia.rb,eque
tambémseráasuperclassedasclasses Livroe DVD,quetambémnãofoicriadae
deveseradicionadanoarquivo lib/dvd.rb:
class Midia
end
# coding: utf-8
class DVD < Midia
attr_accessor :valor
attr_reader :titulo
def initialize(titulo, valor, categoria)
@titulo = titulo
@valor = valor
@categoria = categoria
end
103

## Página 118

7.1. Herança:Compartilhandocomportamentoscomclasses CasadoCódigo
def to_s
%Q{ Título: #{ @titulo}, Valor: #{ @valor} }
end
end
# coding: utf-8
class Livro < Midia
attr_accessor :valor
attr_reader :categoria, :autor, :titulo
def initialize(titulo, autor, isbn = "1", numero_de_paginas,
valor, categoria)
@titulo = titulo
@autor = autor
@isbn = isbn
@numero_de_paginas = numero_de_paginas
@categoria = categoria
@valor = valor
end
def to_s
"Autor: #{ @autor}, Isbn: #{ @isbn},
Páginas: #{ @numero_de_paginas},
Categoria: #{ @categoria}"
end
end
Não se esqueça de fazer o ‘require’ destas duas novas classes no arquivo
lib/loja_virtual.rb:
require File.expand_path('lib/midia')
require File.expand_path('lib/dvd')
require File.expand_path('lib/livro')
require File.expand_path('lib/biblioteca')
require File.expand_path('lib/relatorio')
require File.expand_path('lib/banco_de_arquivos')
Quandocriamoscriamosumaclassequeherdacomportamentodeoutra,utili-
zamosocaractere <.Definimos,porexemplo,queaclasse Livro < Midiaherda
todososcomportamentosexistentesnaclasse Midiaeemtodasassuperclasses
também.
104

## Página 119

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
As classesLivroe DVDdefinemummétodoacessorparaoatributo valor
eummétododeleituraparaoatributo titulo. Quandoinvocamosométodo
attr_reader :tituloestamosdefinindoummétodo tituloparaosobjetos
daclasse Livroe DVD,nocasodométodo attr_acessor :valordefinimos
doismétodos: valore valor=(novo_valor). Jáqueestecódigoestásendo
repetido,vamosextraí-loparadentrodaclasse Midiaeassimasclasses Livroe
DVDasherdarão:
class Midia
attr_accessor :valor
attr_reader :titulo
end
# coding: utf-8
class DVD < Midia
def initialize(titulo, valor, categoria)
@titulo = titulo
@valor = valor
@categoria = categoria
end
def to_s
%Q{ Título: #{ @titulo}, Valor: #{ @valor} }
end
end
# coding: utf-8
class Livro < Midia
attr_reader :categoria, :autor
def initialize(titulo, autor, isbn = "1", numero_de_paginas,
valor, categoria)
@titulo = titulo
@autor = autor
@isbn = isbn
@numero_de_paginas = numero_de_paginas
@categoria = categoria
@valor = valor
end
def to_s
105

## Página 120

7.2. Herançaevariáveisdeinstância CasadoCódigo
"Autor: #{ @autor}, Isbn: #{ @isbn},
Páginas: #{ @numero_de_paginas},
Categoria: #{ @categoria}"
end
end
teste_e_design = Livro.new "TDD", "Mauricio Aniche" , "123454", 247,
69.9, :testes
p teste_e_design.valor # => 69.9
p teste_e_design.titulo # => "TDD"
windows = DVD.new "Windows 7 for Dummies" , 98.9, :sistemas_operacionais
p windows.valor # => 98.9
p windows.titulo # => Windows 7 for Dummies
7 . 2 H erança e v ariáveis de instância
Asmídiasdanossalojavirtualpossuemumdescontoparticulardecadaumade-
lasqueéaplicadoaoseu valor. Nométodoinitializedaclasse Livrova-
mosdefinirumavariáveldeinstânciaqueguardaráovalordodesconto,efaremos
omesmonométodo initializedaclasse DVD.Apósissodefiniremosummé-
todo valor_com_descontodiretamentenaclasse Midia,jáqueesteseráum
comportamentopadrãoasduasmídiasexistentes:
class Midia
attr_accessor :valor
attr_reader :titulo
def valor_com_desconto
@valor - (@valor * @desconto)
end
end
# coding: utf-8
class DVD < Midia
def initialize(titulo, valor, categoria)
@titulo = titulo
@valor = valor
@categoria = categoria
106

## Página 121

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
@desconto = 0.1
end
def to_s
%Q{ Título: #{ @titulo}, Valor: #{ @valor} }
end
end
# coding: utf-8
class Livro < Midia
attr_reader :categoria, :autor
def initialize(titulo, autor, isbn = "1", numero_de_paginas,
valor, categoria)
@titulo = titulo
@autor = autor
@isbn = isbn
@numero_de_paginas = numero_de_paginas
@categoria = categoria
@valor = valor
@desconto = 0.15
end
def to_s
"Autor: #{ @autor}, Isbn: #{ @isbn},
Páginas: #{ @numero_de_paginas},
Categoria: #{ @categoria}"
end
end
teste_e_design = Livro.new "TDD", "Mauricio Aniche" , "123454", 247,
69.9, :testes
p teste_e_design.valor_com_desconto # => 59.41
windows = DVD.new "Windows 7 for Dummies" , 98.9, :sistemas_operacionais
p windows.valor_com_desconto # => 89.01
Ométodo valor_com_descontoexistenasinstânciasde Livroe DVD
como esperado. Porém existe algo interessante no código acima: o método
valor_com_descontoacessaduasvariáveisdeinstância, @valore @desconto,
107

## Página 122

7.2. Herançaevariáveisdeinstância CasadoCódigo
queestãodefinidasnassubclasses.Emoutraslinguagensestecomportamentonão
funcionaria,excetoseasvariáveisestivessemtambémdefinidasnaclasse Midia.
EstecomportamentoébastanteparticulardalinguagemRuby,quandofalamos
devariáveisdeinstânciaeheran ça. Vocêvaientenderissomelhornaspróximas
linhas.
Asclasses Livroe DVDassimcomooutrasmídiasquesurgirão,terãoumvalor
dedescontopré-definidoem10%. Sendoassim,vamoscriarumavariáveldeins-
tânciachamada @descontodentrodaclasse Midiaeinicializá-locomovalor
0.1:
class Midia
attr_accessor :valor
attr_reader :titulo
def initialize
@desconto = 0.1
end
def valor_com_desconto
@valor - (@valor * @desconto)
end
end
Podemosassim,eliminaravariável @descontodaclasse DVD:
# coding: utf-8
class DVD < Midia
def initialize(titulo, valor, categoria)
@titulo = titulo
@valor = valor
@categoria = categoria
end
def to_s
%Q{ Título: #{ @titulo}, Valor: #{ @valor} }
end
end
Agorapodemostestarnovamenteométodo valor_com_descontoeocom-
portamentodeveserobviamenteomesmo:
108

## Página 123

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
windows = DVD.new "Windows 7 for Dummies" , 98.9, :sistemas_operacionais
p windows.valor_com_desconto
# => TypeError: nil can 't be coerced into Float
Aconteceu um erro que não esperávamos, e ele nos indica que a variá-
vel @desconto está nula. Isso aconteceu porque não invocamos o método
initializedasuperclassequeinicializaavariável @desconto.Resolvemosisso
invocandoométodo superdentrodo initializedaclasse DVDqueinvocará
porsuavezo initializedaclasse Midia:
class DVD < Midia
def initialize(titulo, valor, categoria)
super()
@titulo = titulo
@valor = valor
@categoria = categoria
end
def to_s
%Q{ Título: #{ @titulo}, Valor: #{ @valor} }
end
end
windows = DVD.new "Windows 7 for Dummies" , 98.9, :sistemas_operacionais
p windows.valor_com_desconto # => 89.01
Porémaindanãoficouclarocomoométodo valor_com_descontopossui
acessoavariável @valor.TodooobjetoRubypossuiumconjuntodevariáveisde
instância,eestasvariáveisnãosãodefinidasnaclasse,massimquandoinvocamos
algummétodoqueascria,quenamaioriadoscasosacabasendooprópriométodo
initialize,queéumsimplesmétodocomooutroqualquer.
Pelomotivodenãoseremdefinidasnaclasse,variáveisdeinstância não são her-
dadasporsubclasses. Quandoinvocamosométodo initializedasuperclasse
(atravésdométodo super)umavariáveldeinstânciaécriadanoescopoondefoi
chamado,noexemploavariávelécriadadentrodoobjeto DVD.
Porestemotivoométodo valor_com_descontofunciona. Aocriarmos
umobjetodotipo Livroou DVD,omesmopossuiumavariáveldeinstância
chamada @valoreoutrachamada @desconto,quandoinvocamosométodo
valor_com_descontoasvariáveisreferenciadaspelométodosãoasdoobjeto
ondeométodofoichamado: Livroou DVD:
109

## Página 124

7.2. Herançaevariáveisdeinstância CasadoCódigo
teste_e_design = Livro.new "TDD", "Mauricio Aniche" , "123454", 247,
69.9, :testes
p teste_e_design.valor_com_desconto # => 59.41
windows = DVD.new "Windows 7 for Dummies" , 98.9, :sistemas_operacionais
p windows.valor_com_desconto # => 89.01
Podemosprovaressacaracterísticadalinguagem,setentarmosinvocarométodo
valor_com_descontoemumainstânciade Midia:
midia = Midia.new
midia.valor_com_desconto # => undefined method `*' for nil:NilClass
Oerroindicaqueavariável @valorestánula.Efazbastantesentido,poisem
nenhummomentonóscriamosumavariável @valornoconjuntodevariáveisde
umobjetodotipo Midia.
Pararesolveresteproblemabastainicializarobjetosdotipo Midiacomum
valorpadrão,porexemplo:
class Midia
attr_accessor :valor
attr_reader :titulo
def initialize
@desconto = 0.1
@valor = 10.0
end
def valor_com_desconto
@valor - (@valor * @desconto)
end
end
midia = Midia.new
midia.valor_com_desconto # => 9.0
Agora que o métodoinitialize da classe Midia define uma variá-
vel @valor e o métodoinitialize daclasse DVD define a mesma variá-
velcomoutrovalor,qualseráoseuvalornomomentodachamadaaométodo
valor_com_descontoemumainstânciade DVD?Vamosconferir:
110

## Página 125

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
windows = DVD.new "Windows 7 for Dummies" , 98.9, :sistemas_operacionais
p windows.valor_com_desconto # => 89.01
Exatamenteomesmovalorqueantes. Issoaconteceporquenãoherdamosa
variável@valornomomentodachamadaaométodo super,apenasfoicriada
umavariável@valorvalendo 10.0noconjuntodevariáveisdeinstânciadoobjeto
windows.Comologoemseguidaredefinimosovalordavariável @valorpara89.01
(valordoatributorecebidonométodo initialize),esteseráovalornomomento
daexecuçãodométodo valor_com_desconto.
Estaéumacaracterísticaimportantedeheran çaemRuby,poisnãoherdarva-
riáveisdeinstânciaexcluiapossibilidadedequeumadelassejautilizadaemuma
subclasse,sombreandoumavariávelquefoidefinidanasuperclasse.
Como invocar o método initialize da superclasse
OprimeiropontoquedevemosressaltaréqueRubynãopossuiconstrutores.
Existeummétodo initializequeéexecutadoquandocriamosumobjetoao
invocarométodo newemumaconstantedefinida.
Como Ruby possui apenas métodos, quando desejamos invocar o método
initializedasuperclasse,devemosinvocá-loatravésdapalavrachave super.
Porémexisteumapequenaarmadilha.
Quandoinvocamoso initializedasuperclasseapenascom supersemos
parenteses,ointerpretadorRubytentaráinvocá-lopassandoosmesmosparâmetros
recebidospelométodo initializedasubclasse,porexemplo:
# coding: utf-8
class DVD < Midia
def initialize(titulo, valor, categoria)
super # invocando super sem os parâmetros
@titulo = titulo
@valor = valor
@categoria = categoria
end
def to_s
%Q{ Título: #{ @titulo}, Valor: #{ @valor} }
end
end
111

## Página 126

7.3. Oscustosnousodaheran ça CasadoCódigo
windows = DVD.new "Windows 7 for Dummies" , 98.9, :sistemas_operacionais
# => ArgumentError: wrong number of arguments (3 for 0)
Osparâmetros titulo, valore categoriasãorepassadosparaométodo
initializedaclasse Midiaquenãorecebenenhumargumento,porestemotivo
oerro.
Pararesolverbastaadicionarosparentesesnachamada super()queométodo
initializedasuperclasseseráchamadosemapassagemdenenhumargumento.
Seométodo initializedasuperclasserecebeargumentos,vocêdevepassá-lose
nestecasoousodosparenteseséopcional.
7 . 3 O s custos no uso da herança
AmaioriadosprogramadoresRubyjáprojetaramclassesqueutilizamheran çapara
modelarasclassesqueescrevemnodiaadia.Defatoestamaneiradeprojetarclasses
émuitocomumequasenuncapensamosnosproblemasqueessaabordagempode
nostrazer.
Não existe encapsulamento entre os objetos
Utilizamosherançageralmenteparamodelarclassesnasquaisdesejamoscom-
partilharcomportamentos,masoquemuitagentenãosabeéquemuitasvezesaca-
bamoscompartilhandoimplementa ção. Entreoutrascoisas,issosignificaquenão
importadequantasclassesvocêherde,todososmétodoseoestadodoseuobjeto
sãodefinidosemumúnico namespace.Esevocênãotomarodevidocuidado,essa
perdadeencapsulamentoentreosobjetospodemtrazergrandesdoresdecabe ça.
Para testar esse comportamento, vamos refatorar o método
valor_com_desconto:
class Midia
attr_accessor :valor
attr_reader :titulo
def initialize
@desconto = 0.1
@valor = 10.0
end
def valor_com_desconto
112

## Página 127

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
@valor - desconto
end
private
def desconto
@valor * @desconto
end
end
Apenas extraímos parte do código para um método privado chamado
desconto,ocomportamentocontinuaomesmo.Masédestarefatora çãoquevem
oproblema.Hoje,apenasasclasses Livroe DVDestendemaclasse Midia,porém,
nofuturooutrasmídiaspodemsercriados,eemalgumadestasmídias,odesenvolve-
dorresolvecriar,porexemplo,ummétododeleituraqueretornaovalordodesconto
definido,semsaberqueexisteumoutrométodocomomesmonome,definidona
classe Livro:
class CD < Midia
attr_reader :desconto
def initialize(titulo, valor, categoria)
super()
@titulo = titulo
@valor = valor
@categoria = categoria
@desconto = 0.3
end
end
windows = CD.new "Windows 95" , 239.9, :sistemas_operacionais
p windows.valor_com_desconto # => 239.6
Perceberamoproblema? Ométodo descontodefinidonaclasse Livrofoi
invocado.Masporquê?
Lembre-sequequandoinvocamosummétodoemRuby,estamosnaverdade
enviandoumamensagemparaumobjeto,nomomentoemqueinvocamosomé-
todo valor_com_desconto,elepercebequetemqueinvocarumoutrométodo
chamado descontoparacompletarsuaopera ção.Nestemomentoointerpretador
Ruby,procuraporestemétodonaclasse CD.Aoencontrá-lo,ométodoéexecu-
113

## Página 128

7.3. Oscustosnousodaheran ça CasadoCódigo
tadoeoseuretornoéenviadoparaométodo valor_com_descontoqueefetuaa
subtraçãocomavariável @valoreretornaesteresultadofinal.
Oprincipalproblemaaqui,équeemRubynãoexisteoconceitodeencapsula-
mentoentreosobjetosenvolvidosnousodaheran ça.Omesmoproblemaacontece
comvariáveisdeinstância(queporpadrãosãosempreprivadas),quepodemser
alteradasnassuperclasses,eafetaralgumoutrocomportamentodassubclassesque
utilizamasvariáveisalteradas.
Reuso e customização podem ser armadilhas
Algumasclassesancestraisousuperclassesfornecemmétodosquesãoprojeta-
dosparaseremsubstituídospelasclassesdescendentesousubclasses.Estecompor-
tamentoquandobemdefinidoeexplicadopodesermuitoútil,jáquenasuperclasse
podemosdefiniramaiorpartedoscomportamentosdeixandoapenasalgumaparte
docomportamentoparasercustomizadopelassubclasses. Estetipodecomporta-
mentoétãocomumquevirouumDesignPatternchamado T emplate Method.
Porém,estascustomizaçõespodemnostrazeralgunsproblemas.Ocódigoes-
critoatéomomentopossuiumafalhadevidoascustomiza çõesdisponíveisemal-
gumasAPIdoRuby.Vamosverumexemplodecódigoquedemonstraoproblema:
class CD < Midia
def initialize(titulo, valor, categoria)
super()
@titulo = titulo
@valor = valor
@categoria = categoria
end
end
windows = CD.new "Windows 95" , 239.9, :sistemas_operacionais
p windows
# => #<CD:0x007ff86b91ec20 @desconto=0.1, @valor=239.9,
@titulo="Windows 95" ,
@categoria=:sistemas_operacionais>
puts windows # => #<CD:0x007ff86b91ec20>
Internamente,sabemosqueométodo pchamaométodo inspectdoobjeto
windowseométodo putsporsuavezchamaométodo to_s.Oresultadoexi-
114

## Página 129

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
bidonoterminalaoexecutarocódigoacima,éoretornodaimplementa çãodestes
métodos.
Ométodo inspectherdadodaclasse Objectforneceumsaídaparadepu-
rarmosoconteúdodoobjeto,jáométodo to_stambémdaclasse Objectéum
métodoquenamaioriadasvezesdevesersobrescritoafimdetornar-semaisútil
quandooinvocamos.Foioquefizemoscomosobjetos Livroe DVD,agoravamos
fazeromesmocomosobjetosdotipo CD:
class CD < Midia
def initialize(titulo, valor, categoria)
super()
@titulo = titulo
@valor = valor
@categoria = categoria
end
def to_s
%Q{ Titulo: #{ @titulo}, Valor: #{ @valor} }
end
end
windows = CD.new "Windows 95" , 239.9, :sistemas_operacionais
p windows # => Titulo: Windows 95, Valor: 239.9
Aparentementenãoexistenenhumproblemacomestecódigo.Entretanto,omé-
todo inspectdaclasse Objectfuncionadeumamaneiraumpoucodeselegante
noRuby1.9,definindosuaprópriaimplementa çãodométodo to_sdeixandoal-
gunsefeitoscolateraisemnossocódigo:
windows = CD.new "Windows 95" , 239.9, :sistemas_operacionais
puts windows # => Titulo: Windows 95, Valor: 239.9
Exatamenteamesmasaídadométodo inspect.Aprópriadocumenta çãodo
inspectfalasobreestadecisãoemrela çãoaodesignnocódigo.Resumidamente,
quandodeterminadoobjetonãosobrescreveométodo to_s,ométodo inspect
possuiseuretornopadrãoquevimosanteriormente,casocontrário,eleapenasde-
legaachamadaao to_s.
Amaneiraderesolveresteproblemaésobrescreverométodo inspectedefinir
suaprópriaimplementa çãoquepodeserparecidacomaoriginal.
115

## Página 130

7.4. Módulos CasadoCódigo
Indiretamente,issopodeafetarahierarquiadeclassescriadas.Seporexemplo,
aclasse Midiasobrescreverométodo to_s,todasasclassesqueaestendem,her-
darãoométodo to_seporconsequênciasequisermosumaimplementa çãodo
métodoinspectparecidacomaoriginal,vamosterquecriá-lanassubclasses.
Comesseconhecimentosobreaheran çaemRuby,temosembasamentoosufi-
cienteparaconhecermosumnovorecurso,chamado módulos,quesãoabasepara
umaalternativaaheran ça,conhecidocomo mixings.
7 . 4 M ódulos
Namespace
Aclasse Bibliotecaquecriamosnoscapítulosanteriores,armazenaum Array
deobjetosdotipo Livro. Jáqueestáclasseapenasarmazenaobjetos,podemos
batizá-lacomumnomemaissugestivo,maschamá-laapenasde Set,ouseja,um
conjunto,nestecasodelivros:
class Set
def initialize
@banco_de_arquivos = BancoDeArquivos.new
end
def adiciona(livro)
salva livro do
livros << livro
end
end
def livros_por_categoria(categoria)
livros.select { |livro| livro.categoria == categoria }
end
def livros
@livros ||= @banco_de_arquivos.carrega
end
private
def salva(livro)
@banco_de_arquivos.salva livro
116

## Página 131

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
yield
end
end
conjunto_de_livros = Set.new
conjunto_de_livros.adiciona Livro.new "TDD", "Mauricio Aniche" ,
"123454", 247, :testes
Oquefizemosnocódigoacimaémuitoperigoso,porqueacorelibdoRubyjá
possuiumaclassechamada Set,sendoassim,ocódigoacimaabreaclasseealtera
completamenteoscomportamentosdefinidospelosengenheirosqueprojetarama
classe.Sequisermosmesmoqueaclassequeguardaosobjetos Livrotenhaonome
Set,oúnicojeitoéadicionarum namespaceparadiferenciaraclasse SetdoRuby
comaclasse Setdosistemadevendadelivros.
Éimportanteressaltarqueasbibliotecasquevocêutilizaráquandoprogramar
emRubypodempossuirclassescujosnomesconflitamcomasprópriasclassesjá
existentesnocódigofontequeescrevemos.Osmódulospermitemqueclasseseou-
trosmódulospossuamomesmonomeevitandocolisões.Podemospensarnos na-
mespacescomodiretóriosnoprojetoondeseparamososarquivosquerepresentam
cadaclasseoumódulo.
AlgomuitocomumaconteceemcódigoJava,queutilizamospacotesparadis-
tribuireorganizarcódigo.Alémdeevitarpossíveisconflitoscomnomesdeclasses
jáexistentesnabibliotecasexistentes.
Vamosentãocriarummódulocujafun çãoécriarumnamespace,quenestecaso
podeseralgoqueidentifiquequeaclassepertenceaosistemadevendas. Vamos
batizarosistemacomoVendaFacil:
module VendaFacil
end
MódulosemRubyseguemasmesmasregrasdedefini çãodenomesdeclasses,a
diferençaéousodapalavra module.
Agorabastacolocaraclasse Setno namespacedomódulo VendaFacil:
module VendaFacil
class Set
def initialize
@banco_de_arquivos = BancoDeArquivos.new
end
117

## Página 132

7.4. Módulos CasadoCódigo
# Outros métodos ...
end
end
Utilizamosooperador Constant lookup::paraacessarmosumaclasseoucons-
tantequefoidefinidadentrodenamespace:
# acessando classe Set do namespace VendaFacil
conjunto_de_livros = VendaFacil::Set.new
conjunto_de_livros.adiciona Livro.new "TDD", "Mauricio Aniche" , "123454",
247, :testes
Vocêpodeutilizaro Constant lookupparaencontrarclassesouatémesmoou-
trosmódulosnonívelquedesejar. Seaclasseoumóduloquevocêdesejaacessar
estiveremumnamespace VendaFacil, Util, Setpodemosacessá-loutilizando:
VendaFacilUtilSet.
Utilizarmóduloscomonamespaceséaformapadrãodeorganizarbibliotecas
eclassesemRuby. Estaéumaexcelentepráticaquerecomendoquesejaseguida
conformeseucódigoforcrescendoeaspossibilidadesdeconflitosaumentarem.
Mixins
Precisamosformataroatributo valordosobjetos Livro, CDe DVDrespei-
tandoasregrasdeformata çãodoReal. Podemosdefinirométodoformatadorna
classe Midiaqueéasuperclassedetodasasclassescitadasanteriormente:
class Midia
def valor_formatado
"R$ #{ @valor}"
end
end
Oproblemadecriarométodo valor_formatadodentrodaclasse Midiae
queseprecisarmosutilizarestecomportamentoemclassesquenãofazemparteda
hierarquia,serianecessárioduplicarocódigo,oqueseriaextremamenteruim,pela
necessidadedemanteromesmocódigoemváriaspartesdosistema.
Osmódulostemoutrautilidade,muitoimportanteebastanteutilizadanasprin-
cipaisbibliotecaseframeworksexistentes,comoporexemplo,oRails. Os mixings
118

## Página 133

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
eliminamanecessidadedeheran çaparacompartilharcódigo,alémdepermitiruma
espéciedeherançamúltiplajáquepodemosutilizarváriosmódulosemumamesma
classe.
Módulospodemdefinirmétodosdeclasseedeinstância.Entãoissoquerdizer
quepodemosinstanciarmódulos?Não.Módulosnãopodemserinstanciados,suas
únicasutilidadessãofornecer namespacesecompartilharcódigo.Oquefazemosé
um includedomódulocriadoemumaouváriasclasses,eassimasclassesquein-
cluíramaquelemódulopassamateremsuainterfacetodosos métodos de instância
definidosnomóduloincluído.Nósmisturamososmétodosnaclassequeincluiuo
módulo,daívemonome mixings.
Podemoscriarométodo valor_formatadodentrodeummóduloeutilizá-lo
emvárioslugaresdosistema:
# lib/formatador_moeda.rb
module FormatadorMoeda
def valor_formatado
"R$ #{ @valor}"
end
end
Reparequenométodo valor_formatadoquefoicriado,nosreferimosàuma
variáveldeinstânciachamada @valor.Lembre-sequeosmétodoscriadosdentro
demódulos,assimcomonaheran ça,assumemoescopoondeforaminvocados.Por
exemplo:
# coding: utf-8
class Livro < Midia
# todos os métodos de instância são
# incluídos nos objetos Livro
include FormatadorMoeda
def initialize(titulo, autor, isbn = "1", numero_de_paginas,
valor, categoria)
@titulo = titulo
@autor = autor
@isbn = isbn
@numero_de_paginas = numero_de_paginas
@categoria = categoria
119

## Página 134

7.4. Módulos CasadoCódigo
@valor = valor
@desconto = 0.15
end
def to_s
"Autor: #{ @autor}, Isbn: #{ @isbn},
Páginas: #{ @numero_de_paginas},
Categoria: #{ @categoria}"
end
end
tdd = Livro.new "TDD", "Mauricio Aniche" , "123454", 247, :testes
tdd.valor_formatado # => R$ 247
Oobjeto tddpossuiométodo valor_formatadodefinidonomóduloque
incluímosnaclasse Livroeaoinvocarmos,avariável @valorutilizadaéavariável
definidanoobjeto Livroqueinvocamosométodo.
Resolvendo ambiguidade de métodos
Umadasdúvidasmaiscomunsparaquemestácome çandoautilizar
mixingsécomoéfeitaaprocuradométodoquetemqueserexecutado,
ouseja,sedefinirmosummétodo valor_formatadonaclasse Livro
oudentrodealgumoutro mixingfeitonaclasse Livroqualmétodoserá
executado.
OinterpretadorRubyprimeiroprocuraométododentrodaclassedo
objeto,depoisnos mixingsincluídosnaclasse,esóentãonasuperclassee
seus mixings.Seaclassepossuirmúltiplosmódulosincluídos,noúltimo
móduloincluídoseráfeitaaprimeirabusca,depoisnopenúltimoeassim
pordiante.
É válido ressaltar que quando fazemos o include do módulo
FormatadorMoeda, fazemos apenas uma referência que a classeLivro tem
os comportamentos definidos no módulo. O interpretador Ruby não copia os
métodosdeinstânciaparadentrodaclasse,aoinvésdisso,daclasse Livroparao
módulo FormatadorMoeda. Issoimplicaqueseomóduloforinclusoemvárias
classes, aoalterarmosalgumcomportamentodefinidonele, todasasclassesque
incluemomóduloterãoseuscomportamentosalteradostambém.
120

## Página 135

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
V ariáveis de instância e mixings
Módulosnãopossuemvariáveisdeinstância,poisnãopodemserinstanciados.
PrecisamosnoslembrardecomoasvariáveisdeinstânciasãofuncionamemRuby:
aprimeiramen çãoparaumavariávelprecedidacom @,criaumvariáveldeinstância
noobjetoatual.
Paraos mixings,issosignificaqueomóduloquevocêincluiemumaclasse,pode
definirvariáveisdeinstâncianoobjetodaclassequeestásendoinstanciado.Entre-
tantoestecomportamentopodetrazererrosinesperadosjáqueasvariáveisdeins-
tânciadefinidasnomódulo,podemconflitarcomvariáveisdeinstânciadefinidas
naclassequeoincluiu,oupodeatémesmoconflitarvariáveisdefinidasemoutros
módulosqueforamincluídosnaclasse.
Adicaparaevitarestetipodeproblema,éutilizaralgumtipodeprefixonono-
mesdasvariáveisafimdecriarumnomeúnico. Masesteéumproblemamuitas
vezesinevitávelquandoutilizamos mixings,jáquepodemosincluirquantosmódulo
quisermos.Portanto,tenhacuidadoevejaserealmentefazsentidovocêincluirum
módulosóparanãorepetircódigo.
Incluindo módulos em objetos existentes
Sevocêprecisaincluircomportamentosexistentesemummóduloapenasem
algunsobjetos, podefazerissoutilizandoapalavrachave extendaoinvésde
include. Por exemplo, dado que temos dois objetos do tipoDVD criados, e
desejamosqueapenasumdelespossuaoscomportamentosdefinidosnomódulo
FormatadorMoeda:
windows = DVD.new "Windows 7 for Dummies" , 98.9, :sistemas_operacionais
linux = DVD.new "Linux for Dummies" , 13.9, :sistemas_operacionais
windows.extend FormatadorMoeda
windows.valor_formatado # => R$ 98.9
linux.valor_formatado
# => NoMethodError: undefined method `valor_formatado' for "linux":DVD
Ométodo extendincluiosmétodosdeinstânciadomóduloapenasparao
objeto windows,ooutroobjeto linux,apesardeserdamesmaclasse,nãopossui
ométodo.
121

## Página 136

7.4. Módulos CasadoCódigo
Utilizando módulos da biblioteca padrão do Ruby
ExisteumagrandevariedadedemódulosnabibliotecapadrãodoRuby.Alguns
deles,muitopoderososnospermitemescrevermenoscódigoeexecutartarefascom-
plexasutilizandoapenasum include.Oprincipalmotivoéqueelesinteragemcom
códigodaclassequeosinclui.Asapisdecole çãodoRuby,porexemplo, Array, Set,
Hashpossuemumavariedadedemétodocomo: sort, include?, select,etc.
Seolharmosocódigodaclasse Biblioteca,podemosvisualizaroquãolegalseria
termostodosestesmétodosepodemosinvocá-losdiretamenteemumainstância
de Bibliotecaaoinvésderetornarum Arrayatravésdométodolivrosedaí
entãofazerasopera çõesdesejadas.
Todosestesmétodospodemserincluídosnaclasse Bibliotecaincluindoo
módulo Enumerable,eaúnicacoisaquenecessária,serácriarummétodo each
queiteraeretornatodososelementosdo Arrayde Livro.
class Biblioteca
include Enumerable
def initialize
@banco_de_arquivos = BancoDeArquivos.new
end
def adiciona(livro)
salva livro do
livros << livro
end
end
def livros_por_categoria(categoria)
livros.select { |livro| livro.categoria == categoria }
end
def livros
@livros ||= @banco_de_arquivos.carrega
end
# método each que possibilita que os outros métodos
# do módulo Enumerable funcionem em uma instância de Biblioteca
def each
122

## Página 137

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
livros.each { |livro| yield livro }
end
private
def salva(livro)
@banco_de_arquivos.salva livro
yield
end
end
Agora,seprecisarmossaberasomatóriatotaldetodososlivrosexistentesdentro
da Biblioteca,bastautilizamosométodo injectqueiterasobreoselementos
deum Arrayeguardaasomatóriaemumavariável:
biblioteca = Biblioteca.new
biblioteca.adiciona Livro.new "TDD", "Mauricio Aniche" , "123454",
247, 69.9, :testes
biblioteca.adiciona Livro.new "Web Design Responsivo" , "Tárcio Zemel" ,
"45256", 240, 69.9, :web
p biblioteca.inject(0) { |tot, livro | tot += livro.valor } # => 139.8
Aclasse Bibliotecasecomportacomoum Enumerable,possuitodosos
métodosqueum Array,porexemplo.Masnestecaso,todososmétodosdomódulo
Enumerableutilizamométodo eachqueiterapelavariável @livros.
7 . 5 I ndo mais a fundo : C onstant Lookup de dentro
para fora
Émuitoimportanteentendermosqueasconstantes(classes,módulos,etc)sãopro-
curadasdonamespacemaisinterno,partindoparaomaisexternoatéchegaraona-
mespaceglobal.Issoémuitoconfusoàsvezes,eporsorte,apareceránomomento
daexecuçãodocódigo.
Porexemplo,vamosalteraraclasse VendaFacil::Setparainicializarava-
riável@livroscomum Arrayvazioutilizandooutrasintaxe:
module VendaFacil
class Set
123

## Página 138

7.5. Indomaisafundo:ConstantLookupdedentroparafora CasadoCódigo
def initialize
@livros = Array.new
@banco_de_arquivos = BancoDeArquivos.new
end
# Outros métodos ...
end
end
Se executarmos este código noirb e imprimir de qual tipo é a variável
@livros,veremosquecontinuasendodotipo Array:
conjunto_de_livros = VendaFacil::Set.new
p conjunto_de_livros.livros.class # => Array
Estecomportamentopareceóbvio,porém,seexisteumpequenopeda çodecó-
digocomooabaixoascoisaspodemseralteradasdeformainesperada:
module VendaFacil
module Array
# alguns métodos aqui
end
end
Odesenvolvedorqueescreveuocódigoacima,sepreocupoucomofatodejá
existirumaconstante Arraydefinidaeorganizouocódigoadicionandoonames-
pace VendaFacilnacriaçãodestanovaconstante.Porém,estamudan çanoscausa
pequenasdoresdecabe ça.Aotentarchamarométodo newnaclasse Arraydentro
daclasse VendaFacil::Setumerroserálançado:
VendaFacil::Set.new
# => NoMethodError: undefined method `new' for VendaFacil::Array:Module
Existemdiversasmaneirasdesolucionarmosesteproblema.Umadelasévoltar
ainicializaçãodoArrayparaocódigoanterior [].Aoutraéalteraronomedomó-
dulo VendaFacil::Arrayparaalgumnomequenãoconflitecomclassesda core
standard librarydoRuby,oquenamaioriadasvezeséamelhorsolu ção.Senenhuma
dasopçõesanterioresforpossível,podemosutilizarexplicitamenteo constant lookup
donamespaceglobal:
124

## Página 139

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
module VendaFacil
class Set
def initialize
@livros = :: Array.new
@banco_de_arquivos = BancoDeArquivos.new
end
# Outros métodos ...
end
end
Adicionado ::antesdachamadaao Array.newforcaráointerpretadorRuby
aignorarosnamespacesinternoseexternos,eprocurardiretamentenonamespace
global,ondeestãoasconstantesquenãopossuemnamespace.
Nogeral,quandoutilizamos lookup absolutedeconstanteséumsinalquedeve-
ríamosutilizaroutrosnomesparaasclassesqueconflitam.
7 . 6 D uck Typing : o polimorfismo aplicado no Ruby
Sistemasdetiposéumapartefundamentalemtodasaslinguagensdeprograma ção,
eamaneiraquecadalinguagemoimplementainfluenciaodesigndasclassesdo
sistema.
LinguagensestaticamentetipadascomoC++eJavafazemcomquepensemos
emobjetoscomoabstra çãodeestruturadedadosecomportamentos,enãoexistede
fatoumagrandediferen çaentreosobjetoscriadoseoseutipo,elessãointimamente
ligados.
Porém,nãosãotodasaslinguagensquesecomportamdestemaneira.Ruby,por
exemplo,éumalinguagemquepossuitipagemdinâmica,quepermitequeasclasses
sejammodeladaselidemcomumestilodetipoconhecidocomo Duck Typing.
Duck Typingconsideraoqueumobjetopodefazerenãodequaltipoeleé,que-
brandoaliga çãocomaclassedoobjetocriado.Agoraquandoescrevemosummé-
todo,ouiteramosum Array,temosquepensarnoqueoobjetopodefazer,igno-
randoseutipo.Vamostomarcomoexemploaclasse Biblioteca,queatualmente
guardaváriosobjetosdotipo Livro.Devemoslidarcomobjetosquesejammídias,
ouseja, Livro, DVDe CD.Masseráquenossocódigoatualmentenãosuportaesses
outros“tipos"?Vamosver:
biblioteca = Biblioteca.new
125

## Página 140

7.6. DuckTyping:opolimorfismoaplicadonoRuby CasadoCódigo
windows = DVD.new "Windows 7 for Dummies" , 98.9, :sistemas_operacionais
biblioteca.adiciona windows
biblioteca.each do |midia|
p midia.titulo # => Windows 7 for Dummies
end
Reparequenãohouvenecessidadedealterarmossequerumalinhadecódigono
métodoadicionaetambémnométodo each.Issoaconteceprimeiroporqueo
interpretadorRubynãoseimportacomotipodeobjetopassadocomoargumento,
segundoporqueosmétodosnãoesperamnenhumcomportamentoespecíficodos
objetosqueestãosendoincluídos.Issosignificaquepodemospassar qualquertipo
deobjetonachamadadométodo:
class Revista
attr_reader :titulo
def initialize(titulo)
@titulo = titulo
end
end
biblioteca = Biblioteca.new
mundo_j = Revista.new "MundoJ"
biblioteca.adiciona mundo_j
biblioteca.each do |qualquer_objeto|
p qualquer_objeto.titulo # => MundoJ
end
Porém,paraométodo livros_por_categoria,queestácomumnomede-
fasado,oqueimportanãoéotipo,masoqueosobjetosguardadosnavariável
@livrospodemfazer.
biblioteca = Biblioteca.new
mundo_j = Revista.new "MundoJ"
126

## Página 141

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
biblioteca.adiciona mundo_j
biblioteca.livros_por_categoria :testes
# => NoMethodError: undefined method `categoria` for "mundo_j":Revista
O método livros_por_categoria espera que os objetos doArray
@livrostenhamummétodo categoria,porém,orecémcriadoobjeto Revista
possuiapenasummétodo modelo,ouseja,éumobjetoquedefinitivamentenão
deveriaestardentrodavariável @livrospoisnãopossuioscomportamentosne-
cessários.
Verifique manualmente os tipos dos objetos
Casopreciseexecutarcomandosapenasparadeterminadostipos,épossívelve-
rificarotipodeumobjetodealgunsmaneiras.Aprimeiraformafogeumpoucoda
estilodetipagemimpostopelo duck typing,porquefazumverifica çãoexplícitapelo
classedoobjeto.Vamosaproveitarpararenomearasvariáveisemétodosligadasao
nome livro:
class Biblioteca
include Enumerable
def initialize
@banco_de_arquivos = BancoDeArquivos.new
end
def adiciona(midia)
salva midia do
midias << midia
end if midia.kind_of? Midia
end
def midias_por_categoria(categoria)
midias.select { |midia| midia.categoria == categoria }
end
def midias
@midias ||= @banco_de_arquivos.carrega
end
127

## Página 142

7.6. DuckTyping:opolimorfismoaplicadonoRuby CasadoCódigo
def each
midias.each { |midia| yield midia }
end
private
def salva(midia)
@banco_de_arquivos.salva midia
yield
end
end
Ométodokind_of?retorna trueseoobjetoforumtipoousubtipodacons-
tantepassadocomoargumento,emnossoexemplo,daconstante Midia.Comave-
rificaçãoincluídanométodo adiciona,sãoaceitosapenasobjetosdotipo Midia,
Livro, DVDe CD.
biblioteca = Biblioteca.new
windows = DVD.new "Windows 7 for Dummies" , 98.9, :sistemas_operacionais
biblioteca.adiciona windows
mundo_j = Revista.new "MundoJ"
biblioteca.adiciona mundo_j # não inclui o objeto mundo_j
biblioteca.each do |midia|
p midia.titulo # => Windows 7 for Dummies
end
Casodesejemosincluirobjetosdeoutrostipos(porexemplo, Revista)que
nãosãosubtiposde Midia,devemosalterarométodo adicionaefazeraverifi-
caçãoporestesoutrostipos,ouseja,perdemostodoopoderdo duck typingqueé
justamenteevitarestetipodeverifica çãoeimportar-seapenascomoqueoobjeto
podefazer.
Podemospermitirquesejamincluídosqualquertipodeobjetoefazeraverifica-
çãoapenaspelosmétodos:
class Biblioteca
128

## Página 143

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
include Enumerable
def initialize
@banco_de_arquivos = BancoDeArquivos.new
end
def adiciona(midia)
salva midia do
midias << midia
end
end
def midias_por_categoria(categoria)
midias.select do |midia|
midia.categoria == categoria if midia.respond_to? :categoria
end
end
def midias
@midias ||= @banco_de_arquivos.carrega
end
def each
midias.each { |midia| yield midia }
end
private
def salva(midia)
@banco_de_arquivos.salva midia
yield
end
end
Comestamudan ça, ao executarmos o métodoadiciona podemos pas-
sar qualquer objeto como parâmetro. Porém, se executarmos o método
midias_por_categoriaapenasosobjetosquepossuem( respond_to?)omé-
todo categoriasãoconsideradosnacompara ção,independentedoseutipo.
Avantagemdousodo duck typingpodeserconstatadaaocriartestesdeunidade
paraaclasse Biblioteca,porquepoderíamospassar mocks,quepossuemumaim-
plementação f a k edométodo categoria,quepermitiriaqueoscomportamentos
129

## Página 144

7.7. HerançaouMixing?Qualdevousar? CasadoCódigo
fossemtestadosisoladamente.
7 . 7 H erança ou Mixing? Qual devo usar?
Móduloseheran çanogeralservemparacompartilharmoscódigoeevitarmosassim
aduplicidadedepartesdosistema. Masaperguntaprincipalé: qualdelasdevo
escolher?
Estáéumadastípicasquestões,comomuitasoutras,quearesposta deveser:
depende.Comaexperiênciaqueganhamosaolongodoanoscomodesenvolvedor,
tendemosaescolherumadasalternativas.Masoimportanteésemprelembrarque
nãoexiste bala de prata,enãoseesquecerquaissãoospontosfracosefortesdecada
umadasabordagens.
ClassesemRubyestãorelacionadosaideiadetipos.Quandocriamosumobjeto
“texto”dizemosqueeleédotipoString,ouquandocriamosumobjeto [1, 3]
dizemosqueeleédotipo Array.Quandocriamosclasses,estamosdefinindono-
vostipos,equandoutilizamosheran ça,criamosumsubtipodealgumoutrotipojá
existente.Setemosumobjeto carro,podemosdizerqueele é umVeículo,ou
seja,tudoqueum Veículopodefazer,o carrofaz.
Portanto,quandocriamossubtipos,estamosdefinindorelacionamentos é um.
Porém,nosdomíniosdamaioriadasaplica çõesnãoexistemestetipoderelaciona-
mento.Omaiscomumédizerqueumobjeto t e m u mou usa umoutroobjetopara
executarseuscomportamentos,ouseja,namaioriadasvezesutilizamoscomposi ção
enãoheran ça.
Alémdoqueheran çanostrazgravesproblemasdeacoplamento.Qualqueral-
teraçãonasuperclasse,podequebrartodasassubclasses,quemuitasvezesnãoestão
sobnossocontrole. Comportamentosdefinidosnasuperclassepodemvazarpara
quemutilizaassubclasses,eespalharestasregrasportodososladosnaaplica ção,o
queinibeaindamaisasmudan çaseevolu çãodosistema.
Mixingspossuembasicamenteosmesmosproblemasqueheran ça,aoincluir-
mosummóduloemumaclasse,elapassaatertodososcomportamentosdefinidos
nomódulo,sequisermosalteraralgumdestesmétodos,vamosquebrartodosos
códigosqueinvocamestemétodoatravésdeinstânciasdeclassesquemixaramos
comportamentosdestemódulo.
Porémeuvejoalgumasvantagensdeutilizar mixingsenãoheran ça:
• Módulospodemsergerenciadosemtempodeexecu çãoatravésdométodo
include,enquantoheran çaédefinidonomomentodaescritadaclasse;
130

## Página 145

CasadoCódigo Capítulo7. CompartilhandoComportamentos:Herança,MóduloseMixins
• Módulossãomaisfáceisdetestarunitariamentedemaneiraisolada;
• Módulosnospermiteutilizarmetaprogramação(capítulo8)paradefinir Do-
main Specific Languages;
• Módulossãoclassesquenãopodemserinstanciadas,elesexistemapenaspara
adicionarfuncionalidadesparaclassesjáexistentes.
Hojeeuusariaheran çaapenasemcasosesporádicosondeorelacionamento é
u mrealmenteforcomprovado. Nocasodequererapenascompartilharcompor-
tamentosentreváriasclasses,euusaria mixings. Porém,lembrandoosproblemas
queambasprovocamnodesigndaaplica ção,trazendograndeacoplamentoentreos
componentes.
Amelhorsolu çãoéutilizarcomposi çãoparareutilizaracoplamento,masaco-
munidadeRubynãoutilizamuitoestaprática,excetoalgunscasosraros,amaioria
doscódigosutilizam mixings.
131

## Página 147

Capítulo8
Metaprogramaçãoeseussegredos
Ametaprogramaçãopermitequevocênãofiquelimitadoàsabstra çõesquealingua-
gemlheoferece,permitequevocêváalémecrienovasabstra çõessobrealinguagem
Ruby,permitebasicamentequevocêcrie Domain Specific Languages-DSL,afimde
facilitaraleituraeescritadocódigodasuaaplica ção.
AgrandemaioriadosbonsprogramadoresRubyutilizamtécnicasdemetapro-
gramaçãoparacriaressasimplicidadedecódigo.Porém,estaéumatécnicaqueleva
umbomtempoparaserentendida,poisénecessárioconhecimentodalinguagem
Rubycomoumtodo.Nestecapítulovoumostrarcomoutilizarmetaprograma çãoa
favordoseucódigo,utilizandoassuasprincipaistécnicas.
Metaprogramaçãoéumconteúdomuitoextensoqueexigiriaumúnicolivrosó
paracontartodososseusdetalhes.Comoconteúdoquevocêveráapartirdeagora,
serácapazdecriarsuasprópriasDSL’sepouparváriaslinhasdecódigo.

## Página 148

8.1. Entendaoselfemethodcalling CasadoCódigo
8.1 E ntenda o self e method calling
Rubypossuiumconceitode current objectrepresentandopelavariável self.Esta
variávelpossuidoispapéisimportantesemtodocódigoRuby,inclusivenametapro-
gramação.
V ariáveis de instância
O selféresponsávelporarmazenarasvariáveisdeinstânciadeumobjeto.
Quandotentamosacessarumavariáveldeinstância,oRubyiráprocurarporela
dentrodoobjeto self:
class Revista
def initialize(titulo)
@titulo = titulo
end
def titulo
@titulo
end
end
mundo_j = Revista.new "MundoJ"
p mundo_j.titulo # => MundoJ
Aobjetoreferenciadopor mundo_jpossuiumavariáveldeinstância @titulo,
queestáassociadoaoobjeto self.Quandoinvocamosométodo titulo,avariá-
velacessadaestádentrodo self.
Method Calling
Avariávelselfpossuiumpapelimportantenaschamadasdemétodoquefa-
zemosnosobjetos.Quandoinvocamosummétodoemalgumobjeto,dizemosque
estamosenviandoumamensagemparaqueaqueleobjetoexecutealgumaa ção,esse
objetochamamosde“receiver(receptor)dachamada”.Quandoexecutamosocódigo
mundo_j.titulo,oobjeto mundo_jéoreceivere tituloéaaçãoquequeremos
quesejaexecutada.
Quandoexecutamosachamadaaalgummétodosemexplicitarqualéo receiver,
ointerpretadorRubyassumequeo receiveréo current object(self).Porexemplo:
134

## Página 149

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
# coding: utf-8
class Revista
def initialize(titulo)
@titulo = titulo
end
def titulo
@titulo
end
def titulo_formatado
"Título: #{ titulo}"
end
end
mundo_j = Revista.new "MundoJ"
p mundo_j.titulo_formatado # => Título: MundoJ
Nocódigoacima,nachamadaaométodo titulo,o receiveréself.Masquem
éo selfnestemomento?
# coding: utf-8
class Revista
def initialize(titulo)
@titulo = titulo
end
def titulo
@titulo
end
def titulo_formatado
puts self # => #<Revista:0x007f93aa18cd70>
"Título: #{ titulo}"
end
end
mundo_j = Revista.new "MundoJ"
p mundo_j.titulo_formatado # => Título: MundoJ
Ocódigo puts selfimprimiuqueo selféopróprioobjeto mundo_j,ou
seja,ométodo titulofoiinvocadonopróprioobjeto mundo_j.
135

## Página 150

8.2. Oimpactodoselfnadefini çãodeclasses CasadoCódigo
Podemos invocar o método titulo, especificando qual o receiver:
self.titulo, mas isso só deixaria nosso código mais poluído, porque o
selfnestecasonãofariadiferen ça,jáqueimplicitamenteométodoseráinvocado
em self.
Quandoo receiveréexplícito,ocomportamentoébastanteparecido,sendoa
únicaeimportantemudan çaqueo selféalteradoduranteachamadadométodo
pararepresentaro receiverexplícito.QuandooRubyterminaaexecu çãodométodo,
o selfvoltaaterseuestadoanterior.Porexemplo:
# coding: utf-8
class Revista
def initialize(titulo)
@titulo = titulo
end
def titulo
titulo_upcase = @titulo.upcase
"Título: #{ titulo_upcase}"
end
end
mundo_j = Revista.new "MundoJ"
p mundo_j.titulo # => Título: MUNDOJ
Quandoinvocamosométodo upcaseemuma String,entãoo selfneste
momentoseráoobjeto String.Logoapósaexecu çãodo upcase,o selfvolta
aseroobjeto mundo_j.
8.2 O impacto do self na definição de classes
QuandodefinimosclassesemRuby, selftambéméalteradopararepresentaro
objetoqueguardaasinforma çõesdaclassequeestamosdefinindo. Issoacontece
porquedefinirclassesemRuby,écomoexecutarumoutrocódigoqualquer,onde
criamosobjetoseinvocamosmétodos. Paramostrarcomoissofunciona,vamos
colocarum putsnomeiodadeclara çãodaclasse Revista:
# coding: utf-8
class Revista
puts "O self aqui é: #{ self}"
puts "O self aqui é do tipo: #{ self.class}"
136

## Página 151

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
def initialize(titulo)
@titulo = titulo
end
def titulo
titulo_upcase = @titulo.upcase
"Título: #{titulo_upcase}"
end
end
Quandoexecutamosestecódigo,oresultadoé:
# => O self aqui é: Revista
# => O self aqui é do tipo: Class
Nadefiniçãodeclasses,o selféumobjetodotipo Classqueguardatodas
asinformações daclassequeestamoscriando.Elepodeinclusive,guardarvariáveis
deinstância:
# coding: utf-8
class Revista
@id = 0
def self.id
@id += 1
end
def initialize(titulo)
@titulo = titulo
end
def titulo
titulo_upcase = @titulo.upcase
"Título: #{titulo_upcase}"
end
end
Hámuitacoisadiferentenessecódigoqueaindanãovimos,então,vamospor
partesecombastantecalma.
137

## Página 152

8.3.SingletonClasseaordemdabuscademétodos CasadoCódigo
Definimosumavariável@idcomovalor 0dentrodoobjeto selfdadefini-
çãodaclasse Revista,ejásabemosque selfnestemomentoéoobjetodotipo
Classqueguardanãosóosmétodosdefinidosnaclasse,mastambémvariáveisde
instânciaquenãosãodosobjetos Revistamassimdoobjeto Classqueguarda
informações daclasse Revista.Lembre-sequeemRuby tudosãoobjetos.
Logoapós,definimosummétodo iddentrode self,ouseja,ummétodo
dentrodoobjeto Class.Estemétododeveserexecutadoapartirdaobjeto Class
querepresentaaclasse Revista:
p Revista.id # => 1
p Revista.id # => 2
p Revista.id # => 3
p Revista.new('MundoJ').id
# => NoMethodError: undefined method `id' for #<Revista:0x007fcb7c86dd60>
Reparequeométodonãoexisteparainstânciasdotipo Revista,masapenas
naclasse Revista. Complicadoessaparte,não? V a m o sentenderelacommais
detalhesnapróximaseção,estudandoos Singletons.
8.3 Singleton Cl a s se a ordem d abusca de métodos
EmRuby,quandoinvocamosumdeterminadométodoemumobjeto,ointerpreta-
dorprocurapelométodonoobjeto classquerepresentaaclassedoobjetoondeo
métodofoiinvocado,porexemplo:
mundo_j = Revista.new "MundoJ"
p mundo_j.titulo # => Título: MUNDOJ
Oobjetodotipo Classquerepresentaaclasse Revistaguardareferência
paraométodo tituloequandoinvocamosestemétodo,ointerpretadorRuby
procuraporelenoobjeto Class. Tudoissojásabíamos,masanovidadeagoraé
queointerpretadorRubyprocuraporestemétodoemoutrolugarprimeiro:
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
linux = DVD.new "Linux for Dummies", 13.9, :sistemas_operacionais
def windows.desconto_formatado
"Desconto: #{@desconto * 100}%"
end
138

## Página 153

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
p windows.desconto_formatado
# => Desconto: 10.0%
p linux.desconto_formatado
# => NoMethodError: undefined method `desconto_formatado' for "linux":DVD
Quandoinvocamosométodo desconto_formatadonoobjeto windows,
oRubydefine selfcomooobjeto windowseentão procurapelométodoeo
encontra.Masporquequandoinvocamosomesmométodonoobjeto linuxele
nãoéencontrado.Ométodonãofoidefinidoparatodososobjetos DVD?ORuby
fazalguma magia negraparadefinirométododesconto_formatadoapenaspara
oobjeto windows?Arespostaénão.Lembre-sequemetaprogramaçãonãoémagia
negra,consisteapenasemaprenderalinguagemafundoesaberusá-laaseufavor.
Quandodefinimosométododesconto_formatadonoobjeto windows,o
Rubycriaumanovaclasseedefineométododentrodela.Estaclasseéanônimaeé
conhecidacomo Singleton c l a s s, metaclassou eigenclass.V a m o sseguirchamando-a
de singleton c l a s satéofinaldolivro.
A singleton c l a s scriadaédefinidacomoa classdoobjeto windows,ea
superclassda singleton c l a s séaclasse DVD,conformepodeserobservadona
imagemabaixo:
139

## Página 154

8.3.SingletonClasseaordemdabuscademétodos CasadoCódigo
Aoinvocarmosalgumoutrométodoquenãoestádefinidona singleton c l a s sdo
objeto windows,ointerpretadorRuby,primeiroiráprocurarpelométodona s i n-
gleton c l a s s,casonãoencontre,iráprocurarna superclass Revistaeprovavel-
menteoencontrará.
Quandodefinimosométodoidnaclasse Revista,nóscriamosométodona
singleton c l a s sdoobjeto Classquerepresentaasdefinições daclasse Revista.
QuandoinvocamosométodoRevista.id,naverdadeestamosinvocandoomé-
todona singleton c l a s s.
A p ó sadefinição,foicriadauma singleton c l a s scuja superclasséRevista,
conformeaimagemabaixomostra:
140

## Página 155

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Podemosagorainvocarométodoidnomomentodacriaçãodeobjetosdotipo
Revista:
# coding: utf-8
class Revista
@id = 0
def self.id
@id += 1
end
def initialize(titulo)
@id = self.class.id
@titulo = titulo
end
def id
@id
end
def titulo
titulo_upcase = @titulo.upcase
"Título: #{titulo_upcase}"
end
end
141

## Página 156

8.4. Indomaisafundo:AcessandoaSingletonClass CasadoCódigo
mundo_j = Revista.new "MundoJ"
p mundo_j.id # => 1
mundo_ruby = Revista.new "MundoRuby"
p mundo_ruby.id # => 2
Primeiradefiniçãoquedevemosnoslembrar,avariáveldeinstância @iddefi-
nidanométodoinitializenãoéamesmaquefoidefinidanacriaçãodaclasse.
Elasestãoemcontextos(self)diferentes,aprimeirafoidefinidanocontextodo
objeto Classquerepresentaasdefiniçõesdaclasse Revista,jáasegundapertence
aoobjeto Revistaqueestásendocriado,portantoelasnãoconflitam.Exatamente
poressemotivo,éimpossívelacessaravariável@iddaclasse Revistaemmétodos
deinstânciasde Revista,porexemplo,dentrodométodoinitialize.
Amesmaregravaleparaosmétodosid.Oprimeirofoicriadona singleton c l a s s
doobjeto Classquerepresentaaclasse Revista,osegundofoidefinidoparaas
instânciasde Revistaqueforemcriadas.
Ovalordavariável@iddométodoinitializeéinicializadocomovalorde
retornodométodoiddefinidona singleton c l a s sdaclasse Revista.Comoo self
nométodoinitializerepresentaoobjetoqueestásendocriado,paraacessaro
métodoidda singleton c l a s sdaclasse Revista,invocamos self.classeem
seguidaométodoid,queincrementaeretornaavariável@id.
8.4 Indo mais a fundo : Acessando a Singleton Cl a s s
Nósaprendemosadefinirmétodosna singleton c l a s sdeobjetosdotipo DVD,mas
tambémaprendemosaadicioná-losna singleton c l a s sdoobjeto Classquerepre-
sentaaclasse Revista. Existeoutrasintaxeparafazermosasmesmastarefasfeitas
anteriormente:
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
class << windows
def desconto_formatado
"Desconto: #{@desconto * 100}%"
end
end
142

## Página 157

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
p windows.desconto_formatado
# => Desconto: 10.0%
Utilizandoestasintaxe,oobjeto selfpassaaseroobjeto windows,fazendo
comqueométododesconto_formatadosejaadicionaapenasnesteobjeto.
Podemosutilizaramesmasintaxeaodefinirmétodosnocontextodeumclasse,
porexemplo:
class Revista
@id = 0
class << self
def id
@id += 1
end
end
end
p Revista.id # => 1
p Revista.id # => 2
Nestecaso,o selfdentroda singleton c l a s séopróprioobjetodotipo Class
querepresentaaclasse Revista.Umasdasvantagensdeutilizarestasintaxeépoder
invocarmétodosprivados,jáqueelesnãopodemseracessadosatravésdeum receiver
explícito.Imaginequeprecisamosadicionarummétodopararetornarovaloratual
davariável@id.Podemosimplementarissoutilizandoométodoattr_reader:
class Revista
@id = 0
class << self
attr_reader :id
end
end
Seutilizássemosasintaxeantiga,faríamos: self.attr_reader :id.Porém,
ointerpretadoracusariaumerro,informandoquemétodoprivadosnãopodemser
invocadosapartirdeum selfexplícito.
Euparticularmente,prefiroasintaxe self.nome_do_metodo.Utilizoasin-
taxe class << objetoapenasemcasosesporádicoscomooexemploqueeucitei
acima.[/box]
143

## Página 158

8.5.Metaprogramaçãoeasdefinições deumaclasse CasadoCódigo
8.5 Metaprogramação ea sdefinições de u m a classe
Podemosutilizarométodoattr_readerparacriarparesdemétodosgete set
queacessamasvariáveisdeinstânciadosobjetoscriadosapartirdaclasse DVD,por
exemplo:
# coding: utf-8
class DVD < Midia
attr_reader :titulo
def initialize(titulo, valor, categoria)
super()
@titulo = titulo
@valor = valor
@categoria = categoria
end
def to_s
%Q{ Título: #{@titulo}, Valor: #{@valor} }
end
end
Aoutilizarmosbibliotecasexternas,nosdeparamoscomcódigosquefazemcha-
madasamétodosnomomentodadefinição daclasse. Porexemplo,abiblioteca
Mongoid,quecriaumacamadaORMparaacessarmosdadosemumMongoDB,
possuiummétodofieldqueserveparaespecificarmosquaiscamposserãomape-
adosentreoobjetoeumdocumentosalvonobanco:
class Document
include Mongoid::Document
field :name, type: String
end
Estesmétodossãosempreinvocadosnomomentodadefiniçãodaclasse,ena
maioriadasvezesgeramcódigoporbaixodospanos.Nóstambémpodemoscriar
métodosqueserãoutilizadosnadefiniçãodeclasses,equegeramcódigoautomati-
camente.Esteéumdospoderesdametaprogramação,escrevercódigoautomatica-
mentesemquesejanecessáriamuitarepetição.
Nocapítuloanterior,noscriamosum Modulequeserveparaformataruma
variável@valordaclasseondeomódulofoiincluído.Emnossosexemplos,utili-
zamosomódulonaclasse Livro,mastambémpodemosutilizá-lonaclasse DVD:
144

## Página 159

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
# coding: utf-8
class DVD < Midia
include FormatadorMoeda
attr_reader :titulo
def initialize(titulo, valor, categoria)
super()
@titulo = titulo
@valor = valor
@categoria = categoria
end
def to_s
%Q{ Título: #{@titulo}, Valor: #{@valor} }
end
end
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
p windows.valor_formatado # => R$ 98.9
Agoraprecisamosqueavariável@descontotambémsejaformatada.Podemos
alteraromódulo FormatadorMoedapararesolveroproblema:
module FormatadorMoeda
def valor_formatado
"R$ #{@valor}"
end
def valor_com_desconto_formatado
"R$ #{valor_com_desconto}"
end
end
Pronto! Temostambémummétodo valor_com_desconto_formatado
(queutilizouométodovalor_com_descontodefinidonaclasse Midia):
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
p windows.valor_formatado # => R$ 98.9
p windows.valor_com_desconto_formatado # => R$ 89.01
Mastemosumproblemaumpoucograveaoadotarasoluçãopropostaacima.
Acada“valor”deatributooumétododosmeusobjetosqueeuqueiraformataradi-
145

## Página 160

8.5.Metaprogramaçãoeasdefinições deumaclasse CasadoCódigo
cionadooprefixo“R$” ,teremosqueadicioná-lonomódulo FormatadorMoeda.
Soluçãonãomuitoelegante,concorda?Certo,vocêconcordou:).
O que podemos utilizar émetaprogramação. V a m o scriar um método
formata_moeda que servirápara definirmos quais variáveisde instância ou
métodosdevem ter um métodosimilar que retorne o valor formatado, por
exemplo: Se houver um método valor_com_desconto, existiráum simi-
lar valor_com_desconto_formatado, se houveruma variávelde instância
@valor,haveráummétodovalor_formatadoeassimpordiante.
V a m o scolocar a mão na massa. O primeiro passo édefinir o método
formata_moeda:
# coding: utf-8
class DVD < Midia
attr_reader :titulo
def self.formata_moeda
def valor_formatado
"R$ #{@valor}"
end
def valor_com_desconto_formatado
"R$ #{valor_com_desconto}"
end
end
formata_moeda
def initialize(titulo, valor, categoria)
super()
@titulo = titulo
@valor = valor
@categoria = categoria
end
end
Ométodoformata_moedafoiadicionadona singleton c l a s sdoobjetodaclasse
DVD.Issosignificaquepossoinvocá-lologoapóssuadefiniçãosemexplicitamente
definirqualo receiver,poiso selfnestecasoéoobjetoquerepresentaaclasse DVD.
Nomomentoqueinvocamosométodoformata_moeda,eledefineosmétodos
valor_formatadoe valor_com_desconto_formatadoparatodososobjetos
146

## Página 161

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
DVDqueforemcriados. Masissonão ajudoumuitacoisa,poisoquefizemosfoi
copiarecolarocódigodefinidonomódulo FormatadorMoeda.
Oqueprecisamosédefinirautomaticamenteestesmétodos.V a m o sutilizarum
métodochamado define_method,querecebeonomedométodoquedesejamos
criareumblocoquerepresentaocorpodométodo,ouseja,oconteúdoentreo def
eo end.Lembrandoquequalquerparâmetrodefinidonoblocotorna-separâmetro
dométodoqueestásendocriado.
A primeira informação que precisamos passar na chamada do método
formata_moedasão asvariáveisdeinstânciaquedesejamosformataretambém
quaisosmétodos.Naverdadeestasinformações serãopassadosnachamadadomé-
todo,porqueprecisamosdelasparasaberquaisserãoosmétodosqueserãogerados
automaticamentevia define_method.
# coding: utf-8
class DVD < Midia
attr_reader :titulo
def self.formata_moeda(*variaveis_e_metodos)
def valor_formatado
"R$ #{@valor}"
end
def valor_com_desconto_formatado
"R$ #{valor_com_desconto}"
end
end
formata_moeda :valor_com_desconto, :valor
def initialize(titulo, valor, categoria)
super()
@titulo = titulo
@valor = valor
@categoria = categoria
end
end
Agora vamos utilizar o método define_method para criar os método
valor_formatadoe valor_com_desconto_formatado:
147

## Página 162

8.5.Metaprogramaçãoeasdefinições deumaclasse CasadoCódigo
# coding: utf-8
class DVD < Midia
attr_reader :titulo
def self.formata_moeda(*variaveis_e_metodos)
variaveis_e_metodos.each do |name|
define_method("#{name}_formatado") do
valor =
respond_to?(name) ? send(name) : instance_variable_get("@#{name}")
"R$ #{valor}"
end
end
end
formata_moeda :valor_com_desconto, :valor
def initialize(titulo, valor, categoria)
super()
@titulo = titulo
@valor = valor
@categoria = categoria
end
end
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
p windows.valor_formatado # => R$ 98.9
p windows.valor_com_desconto_formatado # => R$ 89.01
Recebemososvaloresquedevemserformatadosemum Array contendo
[:valor, :valor_com_desconto],sendoassimprecisamoscriarosmétodo
valor_formatadoe valor_com_desconto_formatado.Porissoiteramoso
Array,paragerarummétodoparacadavalor.
Ométododefine_methodrecebenoprimeiroargumento,cadaumadosvalo-
resdo Arrayinterpoladocom _formatado,eosegundoargumentoéoblocoque
defineocorpodométodo,ondedefinimosseucomportamento.Reparequeobloco
nãorecebenenhumparâmetroporqueométodoqueestamosdefinindonãoprecisa.
Lembre-sequesefossenecessárioreceberalgumparâmetronométodo,deveríamos
explicitá-losnobloco.
Osegredomaiordonossocódigoestánabuscapelovalorquedeveserfor-
matado. U mdetalheimportante,invocamososmétodos respond_to, send
148

## Página 163

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
e instance_variable_getdentrodocorpodométodoqueestamoscriando.
Todosestesmétodossão invocadosno default receiver,quenestecaso,éoobjeto
windows.Ométododefine_methodestácriandoummétodonasinstânciade
DVDenãonoobjeto Classquerepresentaaclasse DVD.
O método respond_to que jáhavíamosvisto, verifica se o objeto pos-
suiumdeterminadométodo.Estemétodorecebeum Symbol,seoobjetoti-
ver o métodoo retornoé true, senão false. Em nosso exemplo, o pri-
meiroitemdo Arrayé:valor_com_desconto,quandoinvocamosométodo
respond_to?(:valor_com_desconto)oretornoétrue,logoemseguidain-
vocamosométodovalor_com_descontoutilizandoumoutrométododocore
Ruby,chamado send.
Ométodosendrecebeum Symbolqueéonomedométodoquedesejamos
invocar.Casoométodoquevamosinvocarexijaargumentosemsuachamada,po-
demospassá-loslogoapósonomedométodoseparando-oscom ,:
def qualquer_metodo(qualquer_argumento, outro_argumento)
p qualquer_argumento, outro_argumento
end
send(:qualquer_metodo, 123, 321) # => 123, 321
Osegundoitemdo Arrayéo Symbol valorqueéumavariávelpresente
nosobjetosdotipo DVD.Quandofazemosaverificação seoobjeto DVDpossui
ométodo valor,oresultadoé false,jáqueestemétodorealmentenão está
definido.Nestecaso,nósprecisamosacessarovalordavariável@valor,porém,
variáveisdeinstânciasãoprivadas.Podemostrapacearestaregrautilizandoomé-
todo instance_variable_getpassandoonomedavariávelcom @,seavariável
existir,seuvalorseráretornado.]Emambososcasos,guardamosovaloremuma
variávellocalchamada valor,quelogoemseguidaéinterpoladocoma String:
R$.Paracomprovarqueosmétodosrealmenteforamcriadosnosobjetos DVD,po-
demosutilizarométodomethodsqueretornaum Arraycomtodososmétodos
disponíveis:
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
p windows.methods # => [..., :valor_formatado,
:valor_com_desconto_formatado, ...]
EstatécnicademetaprogramaçãoémuitoutilizadaemframeworkscomoRails,
porexemplo.Ocomportamentoqueutilizamosébemparecidocomocomporta-
149

## Página 164

8.5.Metaprogramaçãoeasdefinições deumaclasse CasadoCódigo
mentoutilizadonométodoattr_accessorquecrianovosmétodosparaacessar-
mosvariáveisdeinstânciadeobjetosdeumadeterminadaclasse.
Compartilhando o método formata_moeda
Aimplementação dométodo formata_moedautilizadoparacriarmétodos
queformatamvaloresdeatributosoumétodoscriadosanteriormenteestãorestritos
parausodentroaclasse DVD.Sequisermosutilizá-lodentrodasclasses Livroe
CD,podemosmovê-loparadentrodaclasse Midiajáqueestaéasuperclassede
Livroe CD.
Porémsequisermosutilizá-lodentrodaclasse Revista,teríamosquefazer
comqueelatambémestendesse Midia,umaopçãoquenãofazmuitosentidoem
nossomodelodenegócio.Alémdenãofazersentidométodosqueformatamvalores
seremdefinidosdentrodaclasse Midia,poisissofogedesuasresponsabilidades.
Omelhorcaminhoéutilizarummódulo:
module FormatadorMoeda
def formata_moeda(*variaveis_e_metodos)
variaveis_e_metodos.each do |name|
define_method("#{name}_formatado") do
valor =
respond_to?(name) ? send(name) : instance_variable_get("@#{name}")
"R$ #{valor}"
end
end
end
end
Eutilizardentrodasclassesquedesejamosestecomportamento.Utilizandoo
extendnadefinição daclasse,osmétodosdefinidosnomóduloserão incluídos
como“métodosdeclasse”,ouseja,serãoincluídosnoobjeto Classquerepresenta
asdefinições daclasse DVD,podendoserutilizadosexatamentedamesmamaneira
queeramquandodefinimosométododiretamentenadefiniçãodaclasse:
# coding: utf-8
class DVD < Midia
attr_reader :titulo
extend FormatadorMoeda
150

## Página 165

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
formata_moeda :valor_com_desconto, :valor
def initialize(titulo, valor, categoria)
super()
@titulo = titulo
@valor = valor
@categoria = categoria
end
end
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
p windows.valor_formatado # => R$ 98.9
p windows.valor_com_desconto_formatado # => R$ 89.01
V aragsem R u b y
Ométodoformata_moedarecebeum Arraycontendosímbolosquerepre-
sentamosnomesdasvariáveisemétodosparaosquaisdesejamoscriarmétodos
formatadores. Existeumamaneiramaiselegantedecriarmosmétodosquepreci-
samreceberargumentoscomnúmerovariávelemRuby:
# coding: utf-8
class DVD < Midia
attr_reader :titulo
# adicionado o caractere * antes do nome do argumento
# define que este argumento recebe N valores
# separados por vírgula
def self.formata_moeda(*variaveis_e_metodos)
variaveis_e_metodos.each do |name|
define_method("#{name}_formatado") do
valor =
respond_to?(name) ? send(name) : instance_variable_get("@#{name}")
"R$ #{valor}"
end
end
end
formata_moeda :valor_com_desconto, :valor
151

## Página 166

8.5.Metaprogramaçãoeasdefinições deumaclasse CasadoCódigo
# outros metodos
end
Bastaadicionarocaractere *antesdonomedoargumentoquereceberávários
valores.Dentrodométodooargumentoéum Array,quecontémosváriosvalores
passados. Podemosadicionarapenasumargumentoquereceberáváriosvalores,
porqueseriaimpossívelparaointerpretadorRubyatribuirosvalorescorretamente
setivéssemosdoisargumentosdestetipo.
Definindo métodosde classe e de instância no módulo
Casosejanecessáriodefinirmétodosdeinstânciaedeclassedentrodomesmo
módulo,existeumtécnicamuitoutilizadaemframeworkscomoRails.Estatécnica
fazusodeum hook methoddoRubychamado included,queéchamadoautoma-
ticamentequandoincluímosummóduloemumaclasse.Nestemétodorecebemos
umobjeto Classquerepresentaaclassequeestáincluindoomódulo.
Mesmoassiménecessáriosepararosmétodosdeinstânciadosmétodosde
classe. Geralmentefazemosissoutilizandoum nested modulequecontémapenas
osmétodosdeclasse,deixandoosmétodosdeinstâncianadefinição dopróprio
módulo,porexemplo:
module FormatadorMoeda
def metodo_de_instancia
"um metodo de instancia qualquer"
end
# Módulo que guarda os métodos de classe
module ClassMethods
def formata_moeda(*variaveis_e_metodos)
variaveis_e_metodos.each do |name|
define_method("#{name}_formatado") do
valor = respond_to?(name) ?
send(name) :
instance_variable_get("@#{name}")
"R$ #{valor}"
end
end
end
end
152

## Página 167

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
# hook method que é executado quando incluímos o módulo
# dentro de alguma classe, recebendo no argumento
# classe_que_incluiu_modulo o objeto %%Class%% que
# representa a classe que incluiu o módulo
def self.included(classe_que_incluiu_modulo)
classe_que_incluiu_modulo.extend ClassMethods
end
end
# coding: utf-8
class DVD < Midia
attr_reader :titulo
include FormatadorMoeda
formata_moeda :valor_com_desconto, :valor
def initialize(titulo, valor, categoria)
super
@titulo = titulo
@valor = valor
@categoria = categoria
end
end
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
p windows.valor_formatado # => R$ 98.9
p windows.valor_com_desconto_formatado # => R$ 89.01
p windows.metodo_de_instancia # => "um metodo de instancia qualquer"
Utilizandoestatécnica,podemoscriarmódulosquepossuemmétodosqueserão
adicionadosnasinstânciasde DVDetambémmétodosquepodemserutilizadosna
definiçãodaclasse.
8.6 Criando u m framework para persistir objetos
em arquivos
AprincipalcamadadepersistênciadifundidanacomunidadeRubyéconhecida
como A c t i v e R e c o r d,aimplementação deum design patterndemesmonomeque
153

## Página 168

8.6. Criandoumframeworkparapersistirobjetosemarquivos CasadoCódigo
visapersistirdadosdeumobjetoatravésdeinterfacespúblicasdefinidasnopróprio
objeto. Essainterfacegeralmentepossuiosmétodoscreate, update, finde
delete.
Atualmenteocódigodaclasse BancoDeArquivosrecebeumobjetodotipo
Livroeosalvaemumarquivochamado livros.yml.Apartirdeagorafaremos
umarefatoração,ondeaclassedeixarádeexistireosmétodosparainserir,atualizar,
buscareremoverumobjeto Livrodobancodearquivosserãofeitosatravésdeuma
interfacenopróprioobjeto.
V a m o scomeçarfazendoocódigoapenasnaclasse Revista,quefoirefatorada
paraterapenasumatributo tituloeum valor:
class Revista
attr_reader :titulo, :id
def initialize(titulo, valor)
@titulo = titulo
@valor = valor
end
end
Opróximopassoserádefinirummétodosavequefaráumaimplementação
dupla,eleseráresponsávelporcriarumarquivocujonomeseráum idautomático
geradoparacadaobjeto Revistaegravaroconteúdodoobjetodentrodestear-
quivo.T a m b é mseráresponsávelporatualizaroconteúdodoarquivocasoomesmo
jáexista.
Dentreestespassos,oprimeiroécriarumcampo ideatribuirumvalorauto-
máticoaele:
class Revista
attr_reader :titulo, :id
def initialize(titulo, valor)
@titulo = titulo
@valor = valor
@id = self.class.next_id # Atribui um id ao objeto Revista
end
private
def self.next_id
154

## Página 169

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Dir.glob("db/revistas/*.yml").size + 1
end
end
Criamosummétododeclasse(next_id)quegeraopróximo idparaoobjeto
queestásendocriado.Suaimplementaçãoébemsimples,eleutilizaaclasse Dir
daAPI FiledoRuby,paracontarquantosarquivos .ymlexistemdentrodapasta
db/revistasondeestãolocalizadososarquivosreferentesaosobjetossalvosem
disco.Somandoovalor1aquantidadedearquivossabemosqualéo iddopróximo
arquivogerado. Definimostambémummétodoparaacessarmoso iddoobjeto
quefoicriado.
Agorabastacriarmosométodosavequeseráresponsávelporguardarocon-
teúdodoobjetoserializadodentrodeumarquivocujonomeseráo iddoobjeto:
class Revista
attr_reader :titulo, :id
def initialize(titulo, valor)
@titulo = titulo
@valor = valor
@id = self.class.next_id
end
def save
File.open("db/revistas/#{@id}.yml", "w") do |file|
file.puts serialize
end
end
private
def serialize
YAML.dump self
end
def self.next_id
Dir.glob("db/revistas/*.yml").size + 1
end
end
A implementação do método save abre um arquivo na pasta
155

## Página 170

8.6. Criandoumframeworkparapersistirobjetosemarquivos CasadoCódigo
db/revistas/#{id_do_objeto}.yml (cria a pasta db/revistas na
raizdoprojeto)emmododeescritaeimprimedentrodeleoconteúdodopróprio
objeto(self)serializadoemyaml.Podemoscomprovarqueocomportamentofoi
implementadocomsucessoexecutandoocódigoabaixo:
mundo_j = Revista.new "Mundo J", 10.9
mundo_j.save
Aoabrirmosoarquivo db/revistas/1.ymlveremososeguinteconteúdo:
--- !ruby/object:Revista
valor: 10.9
titulo: Mundo J
id: 1
Exatamenteoconteúdoqueexistianoobjeto mundo_j.
Ométodosavetambémseráresponsávelporsalvarasatualizações feitasno
objeto.Felizmentenãoseránecessárioalterarnenhumalinhadecódigonométodo
jáquequandoabrimosoarquivoutilizandoomodo w,qualquerimpressãofeita
dentrodomesmosubstituioconteúdoexistentepelonovo.Porém,paratestarque
aatualizaçãoestáfuncionando,precisamospermitirqueosdadosdoobjetopossam
seralterados. V a m o sfazercomqueo valorpossaseralteradoadicionandoum
métododeescrita:
class Revista
attr_reader :titulo, :id
attr_accessor :valor # permite escrita no atributo valor
def initialize(titulo, valor)
@titulo = titulo
@valor = valor
@id = self.class.next_id
end
def save
File.open("db/revistas/#{@id}.yml", "w") do |file|
file.puts serialize
end
end
private
156

## Página 171

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
def serialize
YAML.dump self
end
def self.next_id
Dir.glob("db/revistas/*.yml").size + 1
end
end
Agoravamosalteraro valordeumobjeto Revistaesalvá-loparaverificar
queasalterações serãorefletidasnoarquivocorrespondente:
mundo_j = Revista.new "Mundo J", 10.9
mundo_j.save
mundo_j.valor = 12.9
mundo_j.save
Aoabrirmosoarquivo db/revistas/1.yml,podemosverqueoconteúdo
realmentefoialteradocomoesperávamos:
--- !ruby/object:Revista
valor: 12.9
titulo: Mundo J
id: 1
Buscando objetos
Comissocompletamosduasoperações principaisdoCRUD(Create,Retrieve,
Update,Delete):CreateeUpdate.V a m o sagoraimplementarométodoquerecebe
um id,buscapeloarquivocorrespondente,eretornaoobjetodeserializado:
class Revista
attr_reader :titulo, :id
attr_accessor :valor
def initialize(titulo, valor)
@titulo = titulo
@valor = valor
@id = self.class.next_id
end
157

## Página 172

8.6. Criandoumframeworkparapersistirobjetosemarquivos CasadoCódigo
def save
File.open("db/revistas/#{@id}.yml", "w") do |file|
file.puts serialize
end
end
def self.find(id)
YAML.load File.open("db/revistas/#{id}.yml", "r")
end
private
def serialize
YAML.dump self
end
def self.next_id
Dir.glob("db/revistas/*.yml").size + 1
end
end
Ocódigonãoestámuitodiferentedoencontradonaclasse BancoDeArquivos
implementadanocapítulo6.Adiferençaprincipaléquecriamosométodofind
comométododoobjeto Classreferenteaclasse Revista.Issofazbastantesen-
tido,jáquenãotermosainstânciadoobjetoqueestamosprocurando,nósnaverdade
queremoscriá-laapartirdoconteúdodoarquivo.Emframeworkscomo A c t i v eRe-
cordessetipodecomportamentoécomum.
Outradiferençaéqueagoranósguardamosapenas1objetoserializadoporar-
quivo,porisso,nomomentodaleituraprecisamosapenasutilizarométodoopen
daclasse FileepassaroseuresultadoparaserdeserializadopelaAPIdeYAML.
Invocandoométodofindpassandocomargumentoum idcujoarquivoexista
emdisco,oobjetoexistenteserádeserializadoeretornado:
mundo_j = Revista.find 1
p mundo_j.valor # => 12.9
Comovimos,casoeleexistaeleumobjetodotipo Revistaéretornadoparao
clientedométodofind.Masaperguntaqueficaé:Quandooarquivoforremovido
ounãoexistiremdisco,oqueométodofindretornará?
158

## Página 173

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Adecisão decomoimplementarestecomportamentoébemextensaecausa
grandesdiscussões, unsvão preferirocomportamentoquejáexiste,queconsiste
emretornar nilcasooarquivoreferenteao idnãosejaencontrado.
Retornar nil,naminhaopinião,nãofuncionamuitobem,afinalnãoencon-
traroarquivoquecontémosdadosdoobjetoqueestásendoprocuradoéumerro.
Quandoretornamos nilnãoestamosexpressandooquerealmenteaconteceude
fatoecomissooclientedométodonãosabecomorealmentetratarapossívelfalha.
Algunsdesenvolvedorestemopéssimohábitodeinventarcódigosdeerro,que
emgeralsãonúmeroaleatóriosde1à1000,paraexpressarumerroqueaconteceuno
sistema.Todosnósaquijánosdeparamoscomcoisasdogêneroemalgummomento
denossasvidas,oqueconvenhamosnãoénadalegal,jáqueonúmero,excetosefor
decorado,nãorepresentamuitainformação. Portanto, nuncafaçaisso,nodiaque
fizerprovavelmentevocêselembrarademimeteráquecorrer30kmemumaesteira
nosoldomeiodia.
Outraspreferemretornarexceções, omeucaso,avisandoaoclientedométodo
findqueelenãodeveriainvocarométodopassandoum idquenãoexistemais.
EssecomportamentotambéméseguidopeloActiveRecord,queretornaumaexce-
çãodotipo DocumentNotFound.Exceçõesnaverdadesãoobjetosqueencapsulam
oerro.Oclientedométodotemaopçãodeserecuperardopossívelerroouelaserá
propagadaatéofinaldastackdeexecução,estourandoumerroparaousuário,pro-
vavelmente.
Ométodo find,comofoiditoanteriormente,precisaretornarumaexceção
casooarquivoreferenteao idpassadonãosejaencontrado.Porém,exceções são
classes,eprecisamserdefinidasemalgummomento.ORubypossuiumagrande
hierarquiadeexceções quepodemservistasnafigura8.1,evocêveráqueessahie-
rarquianosajudamuitonomomentodecriarmoscódigoparatratarasexceções.
8.7 Gerenciando exceções e erros
Geralmente quando precisamos disparar exceções, criamos classes que se-
jam filhas de StandardError, uma subclasse de Exception. A classe
StandardErroréasuperclassedamaioriadasexceções quenosdeparamosaté
agora: NoMethodError,porexemplo.Nocasodométodofindvamosretorna
umaexceçãoprópriaquechamaremosde DocumentNotFound,quedeveseradi-
cionadanoarquivo lib/document_not_found.rb:
159

## Página 174

8.7.Gerenciandoexceções eerros CasadoCódigo
class DocumentNotFound < StandardError
end
Agora,bastadispararmosestaexceçãocustomizadaquandooarquivonãoexis-
tir:
# coding: utf-8
class Revista
def self.find(id)
raise DocumentNotFound,
"Arquivo db/revistas/#{id} não encontrado.", caller
unless File.exists?("db/revistas/#{id}.yml")
YAML.load File.open("db/revistas/#{id}.yml", "r")
end
end
Nósdisparamosexceções utilizandoummétododo Kernelchamado raise,
quenestecasoéexecutadoapenasseométodoFile.exists?retornar false,
ouseja,casooarquivonãoexistaemdisco.Ométodoraiseinterrompeofluxo
deexecuçãodométodo,porisso,seométodoraiseforinvocado,existeagarantia
queocódigo YAML.load # ...nãoseráexecutado.
A forma que utilizamos o método raise dispara uma exceção do tipo
DocumentNotFound,comumamensagemdeerroquerepresentaumaexplicação
doerroretornadoeporúltimoutilizamosmaisummétododo Kernel: caller,
queretornaa S t a c kTracequeinformamaisorganizadamenteondeoerroaconteceu
eondepoderiatersidotratado.
R A I S E e suas v ariações
Podemosinvocarométodo raisepassandoapenasum String
querepresentaamensagemdeerroqueseráinseridanaexceçãoqueestá
sendolançada:
raise "Aconteceu um erro qualquer"
Nestecasootipodeexceçãodisparadaserá:RuntimeError.
160

## Página 175

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Exceções mais informativ as
Lembre-sequeasexceções são objetosnormais,epossuemumde-
finição formalescritaemumaclasse. V o c ê ,assimcomoemqualquer
outroobjeto, pode adicionarmétodos,inclusivedefinirseu próprio
initialize,quereceberáosargumentosdesejados:
class DocumentNotFound < StandardError
def initialize(mensagem)
@mensagem = mensagem
end
def mensagem_formatada
"-- #{@mensagem}"
end
end
C o m otratar os erros
Oqueaconteceráquandoinvocarmosométodo findpassandocomoargu-
mentoo iddeumarquivoquenãoexiste?U m aexceçãoserálançada,eoseguinte
erroseráimpresso:
Revista.find 42 # => DocumentNotFound: Arquivo db/revistas/42
não encontrado.
Etambémseráimpressaa stack tracecomaschamadaseonderealmenteoerro
estourou.Oquenãosabemosaindaécomolidarcomesteerroenãointerrompero
fluxodeexecuçãodonossosistema.V a m o sadicionarumtratadordeexceções, ou
melhor,um exception handler:
begin
Revista.find 42
rescue
p "O objeto que estava procurando não foi encontrado."
end
# => O objeto que estava procurando não foi encontrado.
161

## Página 176

8.7.Gerenciandoexceções eerros CasadoCódigo
T o d ooconteúdoexistentequeestádentrodo begin,estáprotegidopelo excep-
tion handler rescuequefoidefinido.Quandonãopassamosnenhumargumento
parao rescue,eletrataexceções tipooudesubtiposde StandardError,ouseja,
seocódigo Revista.find 42retornarqualquerexceçãodestestipos,o pqueco-
locamosseráexecutado.Casovocêqueirarestringiropoderdetratamentodeerro
do rescue,vocêpodeespecificaraexceçãoouexceções quedesejatratar:
begin
Revista.find 42
rescue DocumentNotFound
p "O objeto que estava procurando não foi encontrado."
end
begin
Revista.find 42
rescue DocumentNotFound, OutraExcecaoAqui
p "O objeto que estava procurando não foi encontrado."
end
V o c êpodetambémreceberemumavariávellocal,oobjetoquerepresentaoerro
queaconteceu:
begin
Revista.find 42
rescue DocumentNotFound => erro
p erro
end
V áriosrescue
V o c êpodedefinirváriosexception handlersapósum begin:
beginRevista.find42rescueDocumentNotFoundp“Documentonaoencon-
trado”rescueOutraExcecaoAquip“Outraexcecao”end
Bastanteparecidocomumswitch/case. Casoaexceção batacomoprimeiro
rescueamensagem“Documentonaoencontrado”seráimpresso,casonão,o match
seráfeitocomaexceção OutraExcecaoAqui,sebater,amensagem“Outraexce-
cao”seráimpressa.
162

## Página 177

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Operaçõ e sobrigatórias com o ensure
Algumasvezeséimportantequealgumprocessosejafeitocasoocódigoseja
executadocomsucessooucasoalgumaexceçãosejatratada.Oexemplomaisclássico
equandoestamoslendoumarquivoutilizandoaclasse File,eprecisamosgarantir
queoarquivoéfechadoapósaexecuçãodocódigo.
Paragarantirestecomportamentoutilizamosacláusulaensurelogoapósa
cláusularescue,ondedefinimosumpedaçodecódigoqueseráexecutadoseocó-
digodentrodo beginexecutarnormalmente,setratarmosumaexceçãoutilizando
o rescueouatémesmoseaconteceralgumaexceçãoquenãohaviasidoprevista:
file = File.open("/tmp/file")
begin
p file.read
rescue
p "tratando erro"
ensure
file.close
end
re tr y
Outrasvezesénecessárioretentaraexecuçãodeumatarefadefinidadentrode
umbloco begin end,porexemplo,tentarinserirumregistronobancodedados,
casoobancoestejaindisponível,podemostentarnovamente. Épossívelalcançar
esteobjetivoutilizandoométodoretrydentrodacláusularescue:
begin
db.collection("people").insert({nome: "Lucas Souza"})
rescue
p "Conexao está indisponível"
retry # executa o bloco begin/end novamente
end
Casoalgumaexceçãoaconteça,atentativadeinserçãonobancodedadosserá
executadanovamente. Émuitoimportantesalientarqueocódigoacimapodese
tornarum loopinfinito,casoobanconãoestejadisponívelemnenhummomento.
Oidealécriar flagsquegarantamumnúmeromínimodetentativasouterrealmente
certezadoqueestáfazendo.
163

## Página 178

8.8. Aexclusãodedadosimplementadacommetaprogramação CasadoCódigo
8.8 A exclusão de dados implementada co m meta -
programação
Aúltimaoperação quefaltaparacompletarmosoCRUDdaclasse Revistaéa
exclusãodeobjetosdestetipo.Aimplementaçãodométododestroyserábastante
simples,porém,causaráalgunsefeitoscolaterais.V a m o saocódigo:
# coding: utf-8
require "FileUtils"
class Revista
attr_reader :titulo, :id
attr_accessor :valor
# initialize
# save
# destroy
def destroy
FileUtils.rm "db/revistas/#{@id}.yml"
end
# métodos privados
end
Utilizamosaclasse FileUtils,quepossuiumasériedemétodosutilitários
paralidarcomarquivos.Lembre-sequeénecessáriofazerum requiredestaclasse
parapoderutilizá-la.Aimplementaçãodométododestroyébemsimples,quando
invocadoumatentativaparaexcluiroarquivocujonomeéavariáveldeinstância
@id.ymléfeitautilizandoométodormdaclasse FileUtils.
Ocomportamentopodesertestadoexecutandoocódigoabaixo:
mundo_j = Revista.find 1
mundo_j.destroy
Revista.find 1
# => DocumentNotFound: Arquivo db/revistas/1 não encontrado
164

## Página 179

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Reparequenasegundavezquetentamosbuscarumobjeto Revistaatravés
dométodofind,umaexceçãoédisparadagarantindoqueoobjetorealmentefoi
excluídoquandoinvocamosométododestroy.
Masoqueacontececasoométodo destroysejainvocadoduasvezesem
sequência?
mundo_j = Revista.find 1
mundo_j.destroy
mundo_j.destroy # => Errno::ENOENT: No such file or
directory - db/revistas/1.yml
Nasegundatentativaoarquivojánãoexistemaisemdisco,porestemotivoa
exceção No such file or directoryfoidisparada. Porém,não fazsentido
essaexceçãoserdisparadaquandoumusuárioestáinvocandoométododestroy,
quecomoopróprionomediz,destróioobjetoemquestãoenãodiznadasobrelidar
comarquivosemdisco,todaestálógicaestáencapsuladadentrodométodoeosseus
detalhesnãodevemserexpostosparaosclientesdaAPI.
Paracontornaresteproblema,vamosadicionaruma flagchamada destroyed
queseráinicializadacomovalor false,equeteráseuvaloralteradopara true
naprimeirachamadaaométododestroy:
# coding: utf-8
require "FileUtils"
class Revista
attr_reader :titulo, :id, :destroyed
attr_accessor :valor
def initialize(titulo, valor)
@titulo = titulo
@valor = valor
@id = self.class.next_id
@destroyed = false
end
def destroy
unless @destroyed
@destroyed = true
FileUtils.rm "db/revistas/#{@id}.yml"
end
165

## Página 180

8.8. Aexclusãodedadosimplementadacommetaprogramação CasadoCódigo
end
end
Aotentarmosinvocarométododestroyporduasvezes,asegundachamada
nãodisparanenhumaexceçãoeavariável@destroyedpossuiovalor true:
mundo_j = Revista.find 1
mundo_j.destroy
mundo_j.destroy # => nil
p mundo_j.destroyed # => true
Mascomonemtudoéperfeito,aindaexisteumproblemaemnossométodo
destroy. Casoalgumobjetosejacriadodiretamentepelométodo new,ova-
lordavariável@destroyedseráfalse,sendoassimpossívelinvocarométodo
destroy.Oproblemaéqueoobjetoacaboudesercriadoecomcertezaaindanão
existeumarquivoqueguardeseusvalores. Aoinvocarmosométodocaímosno
mesmoproblemaanterior:
mundo_j = Revista.new "Mundo Java", 10.9
mundo_j.destroy # => Errno::ENOENT: No such file or directory
Podemosresolveresteproblemaadicionandoumaoutra flagqueseráresponsá-
velporguardarainformaçãoseoobjetoéumnovoregistroounão,porisso,vamos
chamá-lade @new_record.Esta flagseráinicializadacom trueeprecisaterseu
valoralteradopara falsequandooobjetoforsalvoatravésdométodosave:
# coding: utf-8
require "FileUtils"
class Revista
attr_reader :titulo, :id, :destroyed, :new_record
attr_accessor :valor
def initialize(titulo, valor)
@titulo = titulo
@valor = valor
@id = self.class.next_id
@destroyed = false
@new_record = true
end
166

## Página 181

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
def save
@new_record = false # seta objeto como registro existente
File.open("db/revistas/#{@id}.yml", "w") do |file|
file.puts serialize
end
end
def destroy
# verificar se o objeto nao foi removido anteriormente
# e se o objeto nao é um novo registro
unless @destroyed or @new_record
@destroyed = true
FileUtils.rm "db/revistas/#{@id}.yml"
end
end
end
Agoranomomentoquecriarmosumobjetodiretamentepelométodonewe
tentarmosremovê-lo,nadaseráexecutado:
mundo_j = Revista.new "Mundo Java", 10.90
mundo_j.destroy # => nil
Casooobjetosejasalvoantesdeserremovido,ométododestroyéexecutado
normalmente:
# cria e salva objeto revista
mundo_j = Revista.new "Mundo Java"
mundo_j.save
mundo_j.destroy
# verifica que o objeto já nao existe mais
Revista.find 1 # => DocumentNotFound
Masvocêdeveestarseperguntandoseissonãocausariaproblemasnaexecu-
çãodométodofind,pois,aparentementeométodoYAML.loadaodeserializaro
conteúdodoarquivoexecutaométodoinitialize,certo?Errado.Oprocesso
dedeserializaçãonãoexecutaométodoinitialize,eleapenasrecuperaosva-
loressalvosemdisco,diretamenteparaasvariáveisdeinstância.Porestemotivo,
167

## Página 182

8.8. Aexclusãodedadosimplementadacommetaprogramação CasadoCódigo
quandoexecutamosométodofind,oobjetoretornadopossuiavariáveldeinstân-
cia @new_recordcomovalor false,jáqueantesdesalvaroobjeto,nósdefinimos
ovalordestavariávelpara false:
mundo_j = Revista.find 1
mundo_j.new_record # => false
Código com muitas responsabilidades
Ocódigodaclasse Revistapossuimuitasresponsabilidades,alémdeguardar
todososatributosdaclasse,osmétodosresponsáveisporrefletiroestadodoob-
jetonoseuarquivoemdiscoestãotodosdefinidosnaprópriaclasse.Alémdisso,se
quisermosaproveitarestesmétodosemoutrasclasses,teríamosqueduplicarocó-
digo,ferindooprincípiodoDRY(Don ’tRepeat Y o u r s e l f)etendomuitotrabalhono
momentoquealteraralgumdestescomportamentosfornecessário.
Podemosisolarocódigoresponsávelporlidarcomarquivosemumaclasse,e
utilizarherançaparareaproveitaroscomportamentosdefinidos.Porém,senofu-
turoexistiranecessidadedeutilizarherançaparaumpropósitomelhor,nãopode-
mosherdardeduasclasses,nestecasoserianecessárioumagranderefatoraçãopara
suportarestamudança.
Amelhorsoluçãonestecenárioéutilizaros mixingsparacompartilharcompor-
tamentos,incluindo-osnasclassesquedesejarmos.V a m o scomeçaranossarefato-
raçãoseguindo baby steps,definindoprimeiroummódulocomosmétodossave,
destroye finddemaneiraquetodososcódigosqueutilizamaclasse Revista
continuemfuncionando:
# coding: utf-8
require "FileUtils"
module ActiveFile
def save
@new_record = false
File.open("db/revistas/#{@id}.yml", "w") do |file|
file.puts serialize
end
end
def destroy
168

## Página 183

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
unless @destroyed or @new_record
@destroyed = true
FileUtils.rm "db/revistas/#{@id}.yml"
end
end
module ClassMethods
def find(id)
raise DocumentNotFound,
"Arquivo db/revistas/#{id} nao encontrado.", caller
unless File.exists?("db/revistas/#{id}.yml")
YAML.load File.open("db/revistas/#{id}.yml", "r")
end
def next_id
Dir.glob("db/revistas/*.yml").size + 1
end
end
def self.included(base)
base.extend ClassMethods
end
private
def serialize
YAML.dump self
end
end
Lembre-sedecriaromóduloacimadentrodoarquivo lib/active_file.rb
eexecutaro requiredomesmodentrodoarquivo lib/loja_virtual.rb.
Agora,podemosutilizaromódulo ActiveFileeremoverboapartedocódigo
queestavasendodefinidonaclasse Revista:
class Revista
attr_reader :titulo, :id, :destroyed, :new_record
attr_accessor :valor
include ActiveFile
169

## Página 184

8.8. Aexclusãodedadosimplementadacommetaprogramação CasadoCódigo
def initialize(titulo, valor)
@titulo = titulo
@valor = valor
@id = self.class.next_id
@destroyed = false
@new_record = true
end
end
Ocódigodaclasse Revistaficoubemmaisconcisoeenxuto.Masométodo
initializeaindapossuidetalhesemsuaimplementaçãoquesãonecessáriospara
queomódulo ActiveFilefuncionecorretamente,porexemplo,acriaçãoasvariá-
veis @id, @new_recorde @destroyed.Comestadependênciadecódigo,todas
asclassesqueutilizaremomódulo ActiveFileterãoquedefinirexatamenteas
mesmasvariáveis.Amelhormaneiraderesolveresteproblemaéimitarframeworks,
como ActiveRecorde Mongoid,definindoométodoinitializedentrodo
mixingecontrolandoacriaçãodevariáveisatravésdemétodosdeclasse.
V a m o stomarcomoexemploumcódigoutilizandoMongoid:
class Revista
include Mongoid::Document
field :titulo, type: String
end
mundo_j = Revista.new titulo: "MundoJ"
Achamadaaométodofielddefinequeosobjetosdotipo Revistaterão
umapropriedade titulo,cujovalorédotipo String.V a m o simplementarnossa
soluçãodemaneirabemparecida,excetopelotipo,quenomomentonãoétãoim-
portante.Nossoprimeiropassoserácriarométodofield:
module ActiveFile
# outros metodos
module ClassMethods
# metodo find
# metodo next_id
def field(name)
170

## Página 185

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
@fields ||= []
@fields << name
end
end
def self.included(base)
base.extend ClassMethods
end
end
Ométodoéresponsávelapenasporguardaremum Arraychamado @fields
quaisserãoosatributosdosobjetosqueincluíremomódulo ActiveFile.
Utilizando class_eval p a r aa j u d a rna definição da classe
Alémdeguardarquaisserãoosatributosqueformarãooobjetoasersalvoem
arquivo,ométodofieldcriaosmétodosacessores: gete setparacadaum
dos fieldsdefinidos. Avariávelselfdentrodométodofieldéainstância
de Classreferenteaclassequeestáincluindoomódulo,emnossocaso,aclasse
Revista.
Paradefinirmétodosacessoresparaumdeterminado field,podemosinvocar
ométodoattr_acessorpassandoavariávelname:
module ActiveFile
module ClassMethods
def field(name)
@fields ||= []
@fields << name
self.attr_acessor name
end
end
def self.included(base)
base.extend ClassMethods
end
end
Entretantoessecódigonãofunciona,porqueométodoattr_acessorépri-
vadoenãopodeserinvocadocomum receiverexplícito.Asoluçãopodeserauti-
lização dométodo send,quenão diferenciaseestamosinvocandoummétodo
171

## Página 186

8.8. Aexclusãodedadosimplementadacommetaprogramação CasadoCódigo
private, protectedou public. Masvamosaprenderumaoutramaneirade
definirmétodosdeinstância,destavezutilizandometaprogramação.
Ométodoclass_evaldaclasse Objectquandoutilizadopermitequeum
blocodecódigosejaexecutadocomoseomesmoestivesseescritonadefiniçãoda
classe.Oscódigosabaixopossuemomesmoefeito:
class String
def plural
"#{self}s"
end
end
p "cachorro".plural # cachorros
String.class_eval do
def plural
"#{self}s"
end
end
p "cachorro".plural # cachorros
Ambosdefinemométodopluralparainstânciasde String,ouseja,ambos
abremaclasse Stringedefinemummétodochamado plural.
172

## Página 187

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
I N S T A N C E_E V A L
O instance_evaltambémpertenceaclasse Objecteservepara
executarmosumblocodecódigo.Porém,adiferençaprincipalentreele
eométodoclass_evaléqueosmétododefinidosdentrodobloco
passadoao instance_evalsãoincluídosna singleton c l a s sde self.
Destaforma,aoinvocarmosométodoinstance_evalemumains-
tância Classreferenteaclasse String,osmétodosdefinidossetor-
narãométodosdeclasse:
String.instance_eval do
def metodo_de_classe
"Isso eh um metodo de classe"
end
end
# Isso eh um metodo de classe
p String.metodo_de_classe
Utilizandoométodoclass_evalépossíveldefinirmososmétodosnecessá-
riosparaacessarovalordeumdeterminado field:
module ActiveFile
module ClassMethods
def field(name)
@fields ||= []
@fields << name
get = %Q{
def #{name}
@#{name}
end
}
set = %Q{
def #{name}=(valor)
@#{name}=valor
end
173

## Página 188

8.8. Aexclusãodedadosimplementadacommetaprogramação CasadoCódigo
}
self.class_eval get
self.class_eval set
end
end
def self.included(base)
base.extend ClassMethods
end
end
Nasvariávellocais gete setdefinimosduas String,quepossuemoconteúdo
exatodosmétodoscriadosautomaticamentepelométodoattr_acessor.A p ó s
definirestasduasvariáveis,cadaumadelasépassadaaométodoclass_evalque
fazo evaluateeexecutaoresultadocomoumcódigoRubyqualquer.
Osegundopassodanossarefatoraçãoédefinirummétodoinitializege-
néricoparatodososobjetosqueincluíremomódulo ActiveFile.Nestemétodo
definiremososvaloresdasvariáveis@id, @new_recorde @destroyed:
module ActiveFile
def included(base)
base.extend ClassMethods
base.class_eval do
attr_reader :id, :destroyed, :new_record
def initialize
@id = self.class.next_id
@destroyed = false
@new_record = true
end
end
end
end
Ométodoinitializeserádefinidonaclassequeincluiomódulo,quandoo
hook method includedforexecutado.Aimplementaçãodométodoinitialize
estáparcialmentefeita,masjápermitequeométodoinitializesejaremovido
daclasse Revista.Alémdissopodemosdefiniros fieldsdaclasseutilizandoo
métodofieldquecriaasvariáveisdeinstânciaeosmétodosparaacessá-las:
174

## Página 189

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
class Revista
include ActiveFile
field :titulo
field :valor
end
revista = Revista.new
p revista.new_record # => true
p revista.id # => quantidade de revistas + 1
revista.titulo = "Veja"
revista.valor = 10.90
revista.save
T o d a sasoperações quefazíamosanteriormente,continuamfuncionandoda
mesmamaneira. Aúnicarestrição équeanteserapossívelinicializarosobjetos
passandoosvaloresdosatributosatravésdachamadaaométodonew. Entramos
naterceirapartedarefatoração,quepossibilitaráainicializaçãodasvariáveisdeins-
tância.
Simulando named parameters
N a m e dparameterséacapacidadedeinvocarfunções oumétodosquerecebem
osvaloresdosatributosnãoporsuaordem,masseguindoonomedecadaumdeles.
Emlinguagenssemestacaracterística,énecessárioseguiraordemdedefiniçãodos
parâmetrosdométodo,porexemplo:
def metodo(primeiro_parametro, segundo_parametro)
p primeiro_parametro, segundo_parametro
end
metodo 10, "segundo" # => 10, "segundo"
metodo "segundo", 10 # => "segundo", 10
Comopodemosver,aordemrealmenteéimportante.Outradesvantageméque
nãoficaclarooquerepresentacadavalorquepassamosnachamadadométodo,a
únicamaneiradedescobrirestasinformações éolhandoocódigofonte,oquenem
sempreépossível.Aoutilizar named parameterspodemosdefinirovalordecada
atributonachamadadométodo:
175

## Página 190

8.8. Aexclusãodedadosimplementadacommetaprogramação CasadoCódigo
def metodo(primeiro_parametro: 1, segundo_parametro: 2)
p primeiro_parametro, segundo_parametro
end
metodo primeiro_parametro: 10, segundo_parametro: "segundo"
# => 10, "segundo"
metodo segundo_parametro: "segundo", primeiro_parametro: 10
# => 10, "segundo"
OcódigoacimafoiescritoemRuby,porém,sóiráfuncionarnaversão2.0que
temprevisãodereleasefinalparafevereirode2013.Reparequenãofoinecessáriose-
guiraordemdedefiniçãodosparâmetrosdométodo,podemospassá-losnaordem
quedesejamos.NoRuby1.9eversõesanterioresépossívelsimularocomportamento
dos named parametersutilizando Hash:
def metodo(parametros)
p parametros[:primeiro_parametro], parametros[:segundo_parametro]
end
metodo primeiro_parametro: 10, segundo_parametro: "segundo"
# => 10, "segundo"
metodo segundo_parametro: "segundo", primeiro_parametro: 10
# => 10, "segundo"
Recebemosum Hasheaoinvocarmosométodo,aschavessão o“nome”dos
atributoseosvaloressão,obviamente,osvaloresdosatributosrelacionadosacada
chave.ÉmuitocomumencontrarmoscódigosescritosemRubyqueutilizam Hash
parasimularos named parameters,porisso,utilizaremosestatécnicaparapassaros
valoresdosatributosdosobjetosqueincluemomódulo ActiveFile:
module ActiveFile
def included(base)
base.extend ClassMethods
base.class_eval do
attr_reader :id, :destroyed, :new_record
def initialize(parameters = {})
@id = self.class.next_id
176

## Página 191

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
@destroyed = false
@new_record = true
parameters.each do |key, value|
instance_variable_set "@#{key}", value
end
end
end
end
end
Iteramosoargumento parameterseparacadaatributo(key)definimosseu
respectivovalor(value)utilizandoométodoinstance_variable_set.Existe
umaressalvaaserfeita,oargumento parameterséinicializadocomum Hash
vazioparaquandoométodonewforchamadosemnenhumargumento,ocódigo
funcionenormalmente.
Agoraaocriarumobjetodotipo Revista,podemospassarovalordosatribu-
tos @tituloe @valor:
revista = Revista.new titulo: "Veja", valor: 10.90
p revista.titulo # => Veja
p revista.valor # => 10.90
revista.save
Comissoeliminamostodoocódigoexistentenaclasse Revistareferentea
persistênciadosdadosemarquivos.
8.9 method lookup e method missing
V a m o srelembraralgunsconceitosvistosnestecapítulo.Aprimeiracoisaimportante
quetemosquelembrarésobre variáveisde instância,elas sempreestãodentrodo
contextodeumobjeto,sejaelaumainstânciade Classoudequalqueroutraclasse
definida,issoquedizerqueointerpretadorRubysempreiráprocurá-lasdentrodo
current o b j e c t.
Quandofalamosdemétodosahistóriaéumpoucodiferente.Existem contai-
nersondepodemosdefinirmétodos:Classes,Móduloseas Singleton Classes. Re-
lembrandobrevementecadaumdelestemos:
177

## Página 192

8.9. method lookupe method missing CasadoCódigo
•Classes:sãoinstânciasde Classquerepresentamasdefiniçõesdeummodelo
emnossosistema.Porexemplooobjeto Classqueguardaasinformações
referentesà Revista.
•Módulos:sãoparecidoscomclasses,porém,nãopodemserinstanciados.Ser-
vemcomo containersdemétodoqueserãocompartilhadoscomváriasclasses
dosistema.
•SingletonClass:instânciacriadaautomaticamenteparaarmazenarinforma-
ções referentesaumobjetoespecífico.Atravésdela,podemosdefinircompor-
tamentosespecíficosporobjeto.
Existeumconceitomuitoimportantequejáfoivistoemváriaspartesdocapítulo,
porém,não vimosconcretamentecomofuncionaesteprocesso. O method lookup
consistenamaneiraqueointerpretadorRubyprocurapelométodoqueprecisaser
executado.Quandoinvocamosummétodoemumobjetodotipo DVD,porexemplo,
oprimeirolugarondeointerpretadoriráprocurá-loseránaclassequearmazenaos
métodosespecíficosdosobjetos DVD,ouseja,oobjetodotipo Classreferentea
classe DVD:
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
windows.titulo
Casoométodoquefoiinvocadonãoexistadentrodaclasse DVD,ointerpretador
iráprocurá-lonosmódulosqueforamincluídosnaclasse DVD,seguindoaordem
178

## Página 193

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
inversadeinserção dosmesmos. Portanto,tomecuidadocomaordemquevocê
insereos mixings,casoelespossuammétodos‘iguais’,oúltimométodoincluídoserá
executado.
Seométodotambémnãoexistirdentrodosmódulosincluídosnaclass DVD,o
interpretadoriráprocurá-lana superclassdaclasse DVD,quenestecaso,éaclasse
Midia.
179

## Página 194

8.9. method lookupe method missing CasadoCódigo
U m avezqueométodotambémnãoexistirdentroda superclassde DVD,oin-
terpretadoriráprocurá-loentãona superclassdaclasse Midia,queparecenãoestar
definido,maséaclasse Object.Lembre-sequetodosasclassesquenãoestendem
explicitamenteumaoutra,temcomo superclass sempreaclasse Object.
180

## Página 195

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Aclasse Objectincluiummódulochamado Kernel,ondeencontra-se,por
exemplo,ométodoputs.OinterpretadorRubyiráprocurarpelométodoinvocado
dentrodestemódulotambém:
181

## Página 196

8.9. method lookupe method missing CasadoCódigo
ApartirdoRuby1.9,casoométodonãoexistatambémnaclasse Object,existe
umoutropassoaserpercorrido,aclasse BasicObject,queéa superclassdaclasse
Object. Aclasse BasicObjectéotopodahierarquiadeclassesdefinidaspela
linguagemRuby,éoúltimolugarondeointerpretadoriráprocurarporummétodo
afimdeexecutá-lo.Casoelenãosejaencontradoaexceção NoMethodErrorserá
lançada.
182

## Página 197

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Esteprocessoexecutadono method lookupdoRubyéconhecidocomo o n estep t o
ri g h t ,the nu p,ouseja,ométodoébuscadonaclassedoobjeto,casonãoencontrado,
ointerpretadorsobenahierarquiaefazabuscaatéencontrá-lo.
C o m osaber minha hierarquia de classes?
Paradescobrirtodaacadeiahierárquicaquecompõe umadeterminadaclasse,
bastautilizamosométodoancestors:
183

## Página 198

8.9. method lookupe method missing CasadoCódigo
p DVD.ancestors
# => [DVD, FormatadorMoeda, Midia, Object, Kernel, BasicObject]
Reparequeo Arrayretornadorepresentaexatamenteofluxoquefoiexplicado.
Trabalhando com method missing
VimosnaseçãoanteriorqueointerpretadorRubybuscapelométodoquepre-
cisaserexecutado,olhandoprimeirona singleton c l a s sdoobjeto,depoisnaclasse
doobjeto,nasuperclassedaclassedoobjeto,assimpordiante,atéchegarnaclasse
BasicObject.QuandoointerpretadorRubynãoencontraométodo,elenaver-
dadeexecutaachamadadeum hook methodchamado method_missing.
Quandoum hook methodéinvocadooprocessopelabuscadométodoquedeve
serexecutadoéexatamenteomesmodeumoutrométodo,ointerpretadorper-
corretodaahierarquiadeclasses.Entretanto,nestecaso,ointerpretadorencontraa
implementaçãodométodomethod_missingdefinidonaclasse BasicObject,
destamaneiraabuscapelométodoterminanesteponto.Ocomportamentopadrão
destemétodoélançarumaexceçãodotipo NoMethodError,ouseja,quandoin-
vocamosummétodoquenão existenahierarquiadeclassesdoobjeto,ométodo
method_missingéexecutadoeporessemotivorecebemosumaexceção.
O importante de entender todo esse processo, é que o método
method_missing éum métodocomo qualquer outro, de modo que pode-
mossobrescrevê-loecriarumcomportamentopróprioparatratarcasosondeum
métodonãoexiste.Omaiorexemplodissoéo A c t i v e R e c o r d,quefazomapeamento
entreoobjetoeobancodedados.Quandoutilizado,o A c t i v e R e c o r dmapeiatodas
ascolunasdeumatabelaparamétodosgete setemobjetocujotipoéonomeda
própriatabela,porém,nãoobrigatoriamente:
class Revista < ActiveRecord::Base
end
Seatabela Revistativerumacolunachamada nome,aocriarmosumobjetodo
tipo Revista,podemosobterealterarovalordocampo:
revista = Revista.new
revista.nome = "MundoJ"
p revista.nome # => MundoJ
Estãodisponíveismétododebuscanaclasse Revista.Sequisermos,porexem-
plo,buscarportodasasrevistascujonomefor“MundoJ”,podemosfazê-loutilizando
ummétodochamado find_by_nome:
184

## Página 199

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
mundo_j = Revista.find_by_nome "MundoJ"
Setivermosumacolunachamada valor,podemosfazerabuscapor valor,
utilizandoummétodochamado find_by_valor:
mundo_j = Revista.find_by_valor 90.8
Podemosfazercombinações debuscapordoiscamposaomesmotempo:
mundo_j = Revista.find_by_nome_and_valor "MundoJ", 90.8
Obviamente,todosestesmétodossão criadosemanipuladosviametaprogra-
mação.Masnestecasoespecífico,aimplementaçãodaclasse ActiveRecordBase
reimplementa o método method_missing. Com esta alteração,
todas as chamadas de métodos inexistentes feitas em um
objeto do tipo ActiveRecordBase acarretarão na execução deste novo
method_missing que possui uma implementação amarrada com as colunas
existentesdobancodedados.
Exemplificando,aoinvocarmosométodofind_by_nomenaclasse Revista,
ointerpretadorRubybuscaráporelenahierarquiadeclassesnormalmente,como
este métodonão existe, o hook method method_missing mais próximo da
classe Revista seráexecutado, ou seja, o métodoreimplementadona classe
ActiveRecord::Base.
Esta nova implementação utiliza convenções e verifica pri-
meiramente se o método que desejamos invocar segue o padrão
find_by_alguma_coluna_da_tabela. Emcasopositivo,osegundopassoé
verificarseacolunaexistenobancodedados,casoexistaumabuscaporestecampo
epelovalorpassadonainvocaçãodométodosãoefetuadosnobancodedados.Se
acolunanãoexistirouométodonaestivernopadrãodenomesdoActiveRecord,
aimplementaçãodefinidanaclasse BasicObjectéinvocadaatravésdométodo
super.
Implementando finders
V a m o scriarmétodosfindersparaefetuarbuscasnaclasse Revistaatravésde
seus fieldsutilizando method_missing.Ointuitoépermitirqueosseguintesmé-
todossejaminvocados:
mundo_j = Revista.find_by_titulo "MundoJ"
mundo_j = Revista.find_by_valor 90.8
185

## Página 200

8.9. method lookupe method missing CasadoCódigo
V a m o sutilizaro method_missingnomódulo ActiveFileparasuportar
estescomportamentos:
module ActiveFile
module ClassMethods
def method_missing(name, *args, &block)
load_all.select do |object|
field = name.to_s.split("_").last
object.send(field) == args.first
end
end
private
def load_all
Dir.glob('db/revistas/*.yml').map do |file|
deserialize file
end
end
def deserialize(file)
YAML.load File.open(file, "r")
end
end
end
Podemosinvocaragoraummétodochamado find_by_titulo:
# Retorna todas as revistas cujo titulo é 'MundoJ'
revistas = Revista.find_by_titulo "MundoJ"
Explicandoocódigocommaisdetalhes.Oprimeiropassofoiredefinirométodo
method_missing,querecebetrêsargumentos:
1) name-nomedométodoqueestásendoinvocadoenãofoidefinidoemnenhum
classedahierarquia
2) *args-argumentospassadosparaométodoquefoiinvocado
3) &block-blocodecódigopassadonachamadodométodoinexistentequepode
serexecutadocom yield.
186

## Página 201

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Aimplementaçãodométodomethod_missinginvocaummétodoprivate
chamado load_allquepercorretodososarquivos .ymldodiretórioondeestão
localizadososobjetosserializadosdotipo Revista,osdeserializaeadiciona-os
dentrodeum Arrayretornadonofinaldométodo.
Comtodososobjetos Revistaemmãosépossívelfiltrarosquedesejamosuti-
lizandoométodoselectdaAPI Enumerable.Nachamadaaométodoselect
nósfizemoso splitnonomedométodoqueestásendoexecutado(noexem-
plo:“find_by_titulo”)pelocaractere _,eobtemosaúltimaocorrência,nestecasoa
Stringcujovalorétitulo.
Comonomedocampopeloqualdesejamosefetuarofiltroemmãos,bastaaces-
sarovalordavariáveltituloutilizandoométodosendecomparandooseuresul-
tadocomoprimeiroargumentopassado,quecorrespondeaoprimeiroparâmetro
dachamadaaométodofind_by_titulo:“MundoJ”.
Entretantonossocódigoestáfrágil:
# NoMethodError: undefined method `blah' for #<Revista:0x007fd0328369e0>
Revista.blah
Oproblemaestánachamadaaométodosendquerecebeua String blah
comoargumento.Comoosobjetos Revistanãopossuemnenhummétodoacessor
chamado blah,aexceção NoMethodErrorélançada. Devemosnosprecavere
programardefensivamente semprequeredefinirmosométodomethod_missing.
Asoluçãonestecasoéverificarqueo fieldpeloqualdesejamosefetuarabusca,
existeounãonaqueleobjeto:
module ActiveFile
module ClassMethods
def method_missing(name, *args, &block)
field = name.to_s.split("_").last
super if @fields.include? field
load_all.select do |object|
object.send(field) == args.first
end
end
private
def load_all
187

## Página 202

8.10.Utilizandoexpressões regularesnasbuscas CasadoCódigo
Dir.glob('db/revistas/*.yml').map do |file|
deserialize file
end
end
def deserialize(file)
YAML.load File.open(file, "r")
end
end
end
Averificação feita,invocao method_missingoriginal(herdadodaclasse
BasicObject)casoo fieldqueestamosacessandonãoestejaregistradonavariá-
veldeinstância @fields.Ocomportamentofeitoparaefetuarbuscasporobjetos
somenteéválidocasoestejasendofeitaporumatributoválido,qualqueroutrocaso,
o method_missingoriginaléinvocado.Lembre-sequeéaltamenterecomendável
invocaro method_missingoriginalutilizandoométodosuper,quandoalguma
situaçãosairdocontroledareimplementaçãoquefoifeita.
8.10 Utilizando expressões regulares n a sbuscas
Amaioriadosatributosquetrabalhamosatéomomentosãodotipo String.Com
aclasse Stringépossívelfazerdiversasoperações etransformações comseusmais
de100métodos.Porém,algumasvezesénecessáriobuscardeterminadoconjunto
decaracteresesubstituí-losporoutros,ouatémesmocriarvalidações parauma
String,comoverificarseelaéumemailválido,porexemplo.Nestasocasiões uti-
lizamosasexpressões regulares.
O q u euma expressão regular pode fazer p o rmim
U mexpressãoregularconsisteemum patternquepodeseravaliadojuntoàuma
String.Nateoriaissosignificafazercomparações como:“ otextoqueestáescrito
aqui”contémasequênciadecaracteres“escrito”,porexemplo.Napráticaasexpres-
sões regularesservempara:
•T e s t a rseuma String‘ c a s a ’comumdeterminado pattern
•Extrairpartesdeuma Stringque‘ c a s a m ’comumdeterminado pattern
188

## Página 203

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
•Alteraruma String,substituindopartesque‘ c a s a m ’comumdeterminado
patternporoutra String
Criando métodosde bu s c autilizando expressões regulares
Existemváriasmaneiradecriarexpressões regularesemRuby,masvoumostrar
amaisbásicadelas,utilizandoocaractere‘/’.Portanto,emRubyaoescrevermos
/windows/,estamoscriandoumaexpressãoregularqueutilizaremosparacomparar
com Strings.Essasimplesexpressãoregular‘ c a s a ’ ,porexemplo,comasseguintes
Strings:“windowsxp”,“bluewindows”.Masnãocasacomas Strings:“window”,
“Windows”.
Escapando caracteres especiais
Existemalgunscaracteresespeciaisutilizadosparaconstruirexpres-
sões regulares,porexemploocaractere‘/’.Sequisermoscriarumaex-
pressãoregularquepossua‘/’devemosescapá-la:
/windows\/xp/ # casa com 'windows/xp'
Ométodo find_by_titulopoderiareceberumaexpressão regularenão
uma Stringcomoargumento. Destamaneira,abuscasetornariamaispode-
rosaenão existirianecessidadedesaberotítuloexatodeuma Revistapara
recuperá-la.Comoaimplementação dométodo find_by_tituloéfeitaden-
trodométodomethod_missing,precisamosfazê-logenéricoapontodereceber
comoargumentouma String,umaexpressãoregulareum Float(paraométodo
find_by_valor).
Utilizaremosentãoométodokind_of?paraverificarotipodeargumentopas-
sado,parasaberquetipodecomparaçãoénecessáriadentrodo selectexecutado
como Arraydeobjetos Revista:
module ActiveFile
module ClassMethods
def method_missing(name, *args, &block)
argument = args.first
field = name.to_s.split("_").last
189

## Página 204

8.10.Utilizandoexpressões regularesnasbuscas CasadoCódigo
super if @fields.include? field
load_all.select do |object|
should_select? object, field, argument
end
end
private
def should_select?(object, field, argument)
if argument.kind_of? Regexp
object.send(field) =~ argument
else
object.send(field) == argument
end
end
def load_all
Dir.glob('db/revistas/*.yml').map do |file|
deserialize file
end
end
def deserialize(file)
YAML.load File.open(file, "r")
end
end
end
Ooperador =~tentacasara Stringcomoa Regexppassadacomoargumento,
seoargumentopassadorealmenteforumainstânciadeumaexpressãoregular.Caso
aexpressãoregularnãocasecoma Stringovalor niléretornado,casocasea
posição inicial(ondeaexpressãoregularcomeçaacasarcoma String)éretor-
nada.Como nilequivalea falseequalqueroutrovalorequivalea true,caso
aexpressãoregularcasecomotítulodo DVDoobjetoéretornadonachamadado
métodofind_by_titulo:
# Retorna todas as revistas cujo titulo comecem com 'Mundo'
revistas = Revista.find_by_titulo /Mundo/
190

## Página 205

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Utilizando caracteres especiaisdentro de expressões
regulares
Quandoasexpressões regularessãocriadasutilizando /expressao
regular/'precisamosescaparoscaracteres‘/’:
/windows\// # casa com 'windows/xp'
Seaexpressãoregularforbastantecomplexa,ficaquaseimpossível
interpretá-lavisualmente. Nestescasos,utilizamosumaoutramaneira
deinstanciarexpressões regularesemqueépossíveladicionarcaracteres
‘/’semprecisarescapá-las:
%r(windows/) # gera a expressão regular /windows\//
Melhorando o method_missing
Averificaçãofeitanaimplementaçãodo method_missingparasaberporqual
fielddesejamosefetuarabusca,estámuitofrágil:
Revista.abc_titulo "MundoJ"
Podemosefetuarabuscautilizandoqualquernomedemétodoquepossuaum
‘_’seguidodonomedo field.Lembrandoqueessecomportamentoéexecutado
nalinhadecódigoabaixo:
field = name.to_s.split("_").last
Podemostornarestecódigomaisseguroutilizandoumaexpressãoregularque
verificaráseonomedométodocomeçacom find_by_:
module ActiveFile
module ClassMethods
def method_missing(name, *args, &block)
super unless name.to_s =~ /^find_by_/
argument = args.first
field = name.to_s.split("_").last
191

## Página 206

8.10.Utilizandoexpressões regularesnasbuscas CasadoCódigo
super if @fields.include? field
load_all.select do |object|
should_select? object, field, argument
end
end
end
Agora nossa implementação de method_missing invoca o
method_missing herdado atravésde super caso o nome do métodonão
casecomaexpressãoregular /^find_by_/. Agoraaoexecutarmosinvocarmos
ummétodoabc_titulo:
# NoMethodError
Revista.abc_titulo "MundoJ"
O method_missingoriginaléinvocado.
Extraindo a variávelfield a partir da expressão regular
Aimplementaçãodo method_missingestámaissegura,porém,existempon-
tosquepodemsermelhorados.Aindautilizamosométodosplitparaextrairo
nomedo fieldpeloqualdesejamosfazerabusca. Podemosextrairestevalora
partirdaexpressãoregularquefizemosanteriormente,utilizandogrupos:
"Windows XP" =~ /Windows (.*)/
"Windows 98" =~ /Windows (.*)/
"Windows Vista" =~ /Windows (.*)/
Osgrupossãodelimitadosporparenteses ()definidosdentrodaexpressãore-
gular. Noexemploacima,ogrupocriadoirácapturaras Strings: “98”,“XP”e
“Vista”,respectivamente.Mascomopodemosrecuperarestesvalores?Simples,basta
utilizarumavariávelchamada $numero_do_grupo:
"Windows XP" =~ /Windows (.*)/
p $1 # => "XP"
"Windows 98" =~ /Windows (.*)/
p $1 # => "98"
"Windows Vista" =~ /Windows (.*)/
p $1 # => "Vista"
192

## Página 207

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
Comonaexpressão regularacima,definimosapenas1grupo,acessamosele
utilizando $1. Se tivéssemosdefinido mais grupos, a regra seria a mesma,
$numero_do_grupo.
Agorapodemosalteraraimplementaçãodo method_missingparaextrairo
nomedo fielddeumgrupodaexpressãoregular:
module ActiveFile
module ClassMethods
def method_missing(name, *args, &block)
super unless name.to_s =~ /^find_by_(.*)/
argument = args.first
field = $1
super if @fields.include? field
load_all.select do |object|
should_select? object, field, argument
end
end
end
193

## Página 208

8.11.Próximospassos CasadoCódigo
Substituindo v alores utilizando expressões regula -
r e s
Expressõesregularessãotãopoderosasquenospermitesubstituirde-
terminadaocorrênciaemuma Stringporoutrovalor.Porexemplo:
mundo_java = Revista.new titulo: "Mundo Java"
p mundo_java.titulo.sub /Java/, "J" # => "Mundo J"
Ométodosubprocuraaprimeiraocorrênciaquecasecomaexpres-
sãoregularna Stringesubstituipelovalordosegundoargumento:
mundo_java = Revista.new titulo: "Mundo Java Java"
p mundo_java.titulo.sub /Java/, "J" # => "Mundo J Java"
Se quisermossubstituirtodas asocorrênciautilizamoso método
gsub:
mundo_java = Revista.new titulo: "Mundo Java Java"
p mundo_java.titulo.gsub /Java/, "J" # "Mundo J J"
Osmétodosube gsubretornamnovosobjetosdotipo String.
Casoqueiraalterara Stringoriginalbastainvocaosmétodoutilizando
ocaractere !:
mundo_java = Revista.new titulo: "Mundo Java"
mundo_java.titulo.gsub! /Java/, "J"
p mundo_java.titulo # => "Mundo J"
8.11 Próximos passos
Nestecapítulovimosconceitosbásicoseavançadossobremetaprogramação.Apren-
demosacriarmétododinamicamenteutilizando define_methodetambémofa-
mosoeperigoso method_missingqueservecomo f a l l b a c kparamétodosquenão
existemnoobjetoreceptor.Estessãoconceitosamplamenteutilizadosembibliote-
casqueosdesenvolvedoresRubyutilizamnodiaadia,porissoaimportânciade
aprendê-los.Sãopoucososcasosemqueutilizamosrecursostãoavançados.
Eporfalarembibliotecas,nopróximocapítuloaprenderemoscomofuncionam
194

## Página 209

CasadoCódigo Capítulo8. Metaprogramaçãoeseussegredos
adistribuiçãoeutilizaçãodelasemprojetos.Aprenderemosacriarumbiblioteca,
distribuí-laecomogerenciardependênciasemprojetosRuby.
195

## Página 211

Capítulo9
AsbibliotecasnouniversoR u b y
EmlinguagensmodernascomoRuby,écomumautilizaçãodebibliotecasqueacele-
remodesenvolvimento.EstasbibliotecassãodistribuídasnouniversoRubyatravés
de gems,quesãoarquivosqueterminamcomaextensão .gem,ondeficamlocali-
zadosocódigofontedabibliotecaetambéminformações emetadados,comoversão
enome.
Nestecapítulo,nósaprenderemosainstalaregerenciarestas gemsetambém
comocriaredistribuiruma.
9.1 Co m o manusear suas gems co m o Rubygems
Rubygemséoframeworkpadrãoqueutilizamosparaempacotar,instalar,atualizar
eremoverbibliotecasescritasemRubydentrodeumaplicativoououtrabiblioteca.
Atualmente,todasasbibliotecasmodernaseatualizadasestãodisponíveisparains-
talaçãoatravésdoRubygems.Comapenasumcomando,todooprocessodebaixar
agemnainterneteinstalá-laéfeitoautomaticamente.

## Página 212

9.1.ComomanusearsuasgemscomoRubygems CasadoCódigo
OpróprioRubygemsdisponibilizaumaferramentadelinhadecomandopara
gerenciarasgems.Tudopodeserfeitoutilizandoocomandogemqueestádisponível
automaticamentesevocêestiverutilizandoumaversãodoRubysuperiora1.9.Nas
versões maisantigaseranecessárioinstalaroRubygemsmanualmente.
Instalando uma gem
Osvaloresdoslivros,dvdsecdsdanossalojavirtualestãosendoimpressoscom
oprefixo "R$".Queremosagoraqueovalorsejaimpressoporextensoeaoinvés
deescreverumcódigoquefazisso,utilizaremosuma gemcriadaporbrasileiros
chamada brnumeros,cujoobjetivoémanipularnúmerosdeacordocompadrões
propostosapenasnoBrasil.Parainstalá-la,bastaexecutaroseguintecomandono
seuterminal:
gem install brnumeros
Asaídadoconsoledeveserparecidacomasaídaabaixoseainstalaçãofoifeita
comsucesso:
Fetching: brnumeros-3.3.0.gem (100%)
Successfully installed brnumeros-3.3.0
1 gem installed
Installing ri documentation for brnumeros-3.3.0...
Installing RDoc documentation for brnumeros-3.3.0...
Asduasúltimaslinhasindicamqueadocumentação(RDoc)da gemfoiinstalada
também.Casovocênãoqueiraqueadocumentaçãosejainstalada,bastapassara
opção --no-rdoc --no-ri.
A p ó sainstalação,vocêpodeverificaras gemsdisponíveisatravésdocomando
gem list,queretornatodasasgemsinstaladas:
*** LOCAL GEMS ***
brnumeros (3.3.0)
Utilizando a gem instalada
U m avezquea gemfoiinstalada,bastautilizarmosométodorequirepara
carregá-ladentrodocódigofontedanossaaplicação,assimcomofizemoscombi-
bliotecasnativasanteriormente.Énecessáriotambémexecutarum requirenas
rubygems:
198

## Página 213

CasadoCódigo Capítulo9. AsbibliotecasnouniversoRuby
require 'rubygems'
require 'brnumeros'
V a m o sentãoadicionarumnovométodonomódulo FormatadorMoedacha-
mada valor_por_extenso:
# carregando rubygems
require 'rubygems'
# carregando gem brnumeros
require 'brnumeros'
module FormatadorMoeda
module ClassMethods
def formata_moeda(*variaveis_e_metodos)
variaveis_e_metodos.each do |name|
define_method("#{name}_formatado") do
valor = respond_to?(name)
? send(name)
: instance_variable_get("@#{name}")
"R$ #{valor}"
end
# metodo que retorna valor por extenso em reais
define_method("#{name}_por_extenso") do
valor = respond_to?(name)
? send(name)
: instance_variable_get("@#{name}")
valor.por_extenso_em_reais
end
end
end
end
def self.included(base)
base.extend ClassMethods
end
end
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
windows.valor_por_extenso
# => noventa e oito reais e noventa centavos
199

## Página 214

9.2. Gerenciandováriasversões deumagem CasadoCódigo
Ocódigonãopossuimuitasnovidades,apenasautilizaçãoda gem brnumeros
atravésdachamadaaométodopor_extenso_em_reaisquepegaovalordeum
Integerou Floateretornauma Stringcomovalorporextenso.
Instalando versões específicas de uma gem
Emalgumasocasiões énecessárioinstalarumadeterminadaversão deuma
gem, por exemplo,em casos de incompatibilidadede outrasgemsque utiliza-
mosnonossosistema. Ocomando gempermitequesejapassadoumparâme-
tro --version versao_desejada. Podemosinstalarumaversão maisantiga
da gem brnumeros:
gem install brnumeros --version '3.2.0'
Fetching: brnumeros-3.2.0.gem (100%)
Successfully installed brnumeros-3.2.0
1 gem installed
Damaneiraqueoparâmetro --versionfoiespecificado,aversão3.2.0será
instalada.Maspodemossermaisflexíveise,porexemplo,instalarqualquerversão
quesejamaiorqueaversão3.2.0:
gem install brnumeros --version '> 3.2.0'
Fetching: brnumeros-3.3.0.gem (100%)
Successfully installed brnumeros-3.3.0
1 gem installed
Ouaindaespecificarqueaversãoinstaladadeveseraúltimaversãodeumde-
terminado m i n o r.Porexemplo,instaleaúltimaversão3.0.x:
gem install brnumeros --version '~> 3.0.0'
Fetching: brnumeros-3.0.8.gem (100%)
Successfully installed brnumeros-3.0.8
1 gem installed
9.2 Gerenciando v árias versões de u m a gem
Como acabamos de ver, podemos instalar uma versão mais antiga da gem
brnumeros:
200

## Página 215

CasadoCódigo Capítulo9. AsbibliotecasnouniversoRuby
gem install brnumeros --version '3.2.0'
Agoraaorodarmosocomando gem listveremosasduasversões:
*** LOCAL GEMS ***
brnumeros (3.3.0, 3.2.0)
Masqualdasduasversões serãoutilizadasnomódulo FormatadorMoeda?A
respostaé:aúltima.Sevocêprecisautilizaraversãomaisantigada gememum
determinadoprojeto,bastautilizarométodogemdentrodocódigo,especificando
qualversãoserácarregada:
# carregando rubygems
require 'rubygems'
# carregando gem brnumeros versao 3.2.0
gem 'brnumeros', '3.2.0'
require 'brnumeros'
module FormatadorMoeda
module ClassMethods
end
end
Ométodogem,dizquea gem brnumerosdevesercarregadanaversão3.2.0.
Porém,essametodologiadegerenciarasversões das gemsquedesejamosutilizar
podesetornarumproblemacomopassardotempo,principalmenteporqueno
universoRubyémuitocomumtermosváriasdependênciasemummesmoprojeto,
mesmoqueestesejapequeno.Controlarcadaversãoémuitotrabalhoso,porisso
atualmenteexistemgerenciadoresdedependênciasescritosemRubyquefacilitam
nossavidaecuidamdestaspreocupações paraagente.
9.3 Gerenciedependênciasco m o Bundler
AformamaiseficazdegerenciardependênciasemprojetosRubyéatravésdeuma
gemchamada B u n d l e r. Suafunçãoégarantirqueocódigodasuaaplicaçãousará
asversões exatasdasgemsdasquaiseladepende.Parautilizaro B u n d l e rdevemos
primeiroinstalá-lo:
gem install bundler
201

## Página 216

9.3.GerenciedependênciascomoBundler CasadoCódigo
Asdependênciasdasuaaplicaçãodevemserdeclaradasdentrodeumaarquivo
chamado Gemfile. Essearquivodeve,primeiramente,conterafontedeondeas
dependênciasserãobaixadas:
source "http://rubygems.org"
Adeclaração sourceindicaqueasgemsserãobaixadasdorepositóriooficialdo
Rubygems.Opróximopassoédeclararquaissãoasgemsquesãodependênciasdo
projeto:
source "http://rubygems.org"
gem "brnumeros", "3.3.0"
Nadeclaração gem,indicamosonomeeaversãoquedesejamos.Nadeclaração
daversãopodemosseguiromesmopadrãoqueseguimosaoinstalarumgemma-
nualmente.No Gemfiledonossoexemplo,aversãoinstaladaseráexatamentea
versão3.3.0,sequisermosinstalaraúltimaversãodo m i n o r3.2.x,adeclaraçãoseria
feitadaseguintemaneira:
source "http://rubygems.org"
gem "brnumeros", "~> 3.3.0"
Paraqueasgemssejaminstaladasrespeitandooquefoidefinidono Gemfile,
bastarodarmosocomando bundle installnoterminal,queirágerarumnovo
arquivochamado Gemfile.lock,queespecificatodasasgemsobtidasparao
Gemfileesuarespectivaversãobaixada.
O Gemfile.lockéumaboaalternativaparacongelarasversões dasgemsa
seremutilizadas,umavezqueaorodarmosocomando bundle installsobrea
presençadeum Gemfile.lock,asversõespresentesnessearquivoserãoutilizadas
paraespecificarasgemsaserembaixadas.
Paraqueasversões especificadasno Gemfilesejamrespeitadasduranteoload
daaplicação,precisamoscarregarumaclassedobundler:
require 'bundler/setup'
require 'brnumeros'
module FormatadorMoeda
module ClassMethods
end
end
202

## Página 217

CasadoCódigo Capítulo9. AsbibliotecasnouniversoRuby
Automaticamenteaversãoespecificadano Gemfileserácarregadaparaagem
brnumeros.Agoraaoinvésdeexecutarum irbnoterminalparatestarasclasses
queestamosconstruindo,executeocomando bundle consolequeabreo irb
como bundlepré-carregado:
bundle console
require File.expand_path('lib/loja_virtual')
windows = DVD.new "Windows 7 for Dummies", 98.9, :sistemas_operacionais
windows.valor_por_extenso
Resolvendo conflitos com bundle exec
Existem gemsquecriamcaminhosexecutáveisparautilizarmosnoconsole,o
próprio Bundlernosdisponibilizacomandosúteiscomoo bundle console.
Agem rake,queseráexploradanopróximocapítulo,criaumexecutávelquenos
permiterodar tasksapartirdoterminal:
rake -T
Ocomandoacimalistatodasas tasksdefinidaspelaaplicação. Porém,setiver-
mosmaisdeumaversãodagem rakeinstaladanosistemaeno Gemfiledaapli-
caçãoestiverespecificadaalgumadestasversões, ocomandoacimaacusaráumerro:
rake aborted!
You have already activated rake 10.0.3,
but your Gemfile requires rake 10.0.2
Basicamenteissosignificaqueno Gemfiledaaplicaçãoestáespecificadaaver-
são10.0.2dagem rake,enquantonosistemaexisteumaversãomaisnova10.0.3.Se
vocênãopuderatualizaraversãodo rakenoseu Gemfile,énecessárioexecutar
ocomando rake,utilizandoumoutrocomandochamado bundle exec:
bundle exec rake -T
Ocomando bundle execexecutarátodososcomandos(rake, rails,etc)
respeitandoaversãodescritano Gemfile,nesteexemplo,ocomando rake -T
seráexecutadocomaversão10.0.2,resolvendooconflito.Nocapítulosobre RVM
veremosqueexisteumaalternativaaousodocomando bundle exec.
203

## Página 218

9.4. Quemusa bundler? CasadoCódigo
9.4 Quem usa bundler?
O Rails,omaisfamosoframeworkdomundoRuby,utilizaporpadrão o B u n -
dlerparagerenciarassuasdependências.Qualqueraplicação Railsteráumar-
quivo Gemfilecomasdependências,portanto,éessencialentendercomoutilizá-
lo. V o c êpodevermaisdetalhesdaexcelentedocumentação disponívelnosite:
http://gembundler.com/
9.5 Criando e distribuindo gems
Comofoiditoanteriormente,umagemnadamaiséqueumarquivocompac-
tadocomocódigo fontedabibliotecaeumarquivoquecontémosmetadados,
comonome,versão eoutrasdependências.V a m o sdistribuirocódigodaclasse
ActiveFileemumagem.
Érecomendávelqueumagemtenhaumaestruturadefinidadediretórios.Opró-
prio b u n d l e rpossuium bootstrapquegeraestesdiretóriosdemaneiraquenãoéne-
cessáriocriá-losmanualmente.Rodandoocomando bundle gem active_file
queirágeraraseguintesaída:
create active_file/Gemfile
create active_file/Rakefile
create active_file/LICENSE
create active_file/README.md
create active_file/.gitignore
create active_file/active_file.gemspec
create active_file/lib/active_file.rb
create active_file/lib/active_file/version.rb
Comaseguinteestrutura:
204

## Página 219

CasadoCódigo Capítulo9. AsbibliotecasnouniversoRuby
Semdúvida,omaisimportantedestaestruturaéapasta lib.Énelaqueficam
localizadososarquivoscomcódigoRubyquecompõem abiblioteca. Estediretó-
rioéadicionadoao GEM_PATHdoRubyGemsparainformarquaisbibliotecasestão
disponíveisparauso.
ORubyGemssobrescreveométodorequiredomódulo Kernelcomuma
implementaçãoquefazumabuscapelagemquevocêprecisautilizandoosdiretórios
adicionadosao GEM_PATH.Porisso,semprequeutilizamosométodorequire
"alguma_biblioteca", o RubyGemsiráprocurarpor um arquivochamado
lib/alguma_biblioteca.rb.Poressemotivoaimportânciadetermosumdi-
retório lib.
Abrindooarquivo active_file/lib/active_file.rbtemososeguinte
conteúdo:
require "active_file/version"
module ActiveFile
# Your code goes here...
end
Somenteumarquivoécarregadoeelecontémaversãodagem,importanteno
momentodageraçãodoarquivo .gemqueveremosmaisafrente.T a m b é mfoide-
claradoummódulocomonomedagemusandoanotaçãocamelcase.Essadefinição
émuitoimportante,lembre-sequeosmódulosservemparacriarmos namespaces,e
comissoevitamosconflitoscomoutrasgemsutilizadascomodependências.
Dentrodestemóduloénecessárioincluirocódigodomódulo ActiveFileque
estádentrodaaplicação,omesmocódigoquefizemosnocapítuloanterior.T o d oo
códigodaimplementação dagem active_fileestádisponívelnomeugithub:
http://github.com/lucasas/active_filevocêpodecopiarocódigodiretamentedelá.
9.6 Distribuição d abiblioteca
Paragerarumarquivo .gemprecisamosdeumarquivo .gemspec,quepossuios
metadadosdanossabiblioteca.Comocriamosnossabibliotecautilizandoo B u n d l e r
umarquivo .gemspecfoicriadoautomaticamentecomoseguinteconteúdo:
require File.expand_path('../lib/active_file/version', __FILE__)
Gem::Specification.new do |gem|
205

## Página 220

9.6. Distribuiçãodabiblioteca CasadoCódigo
gem.authors = ["Lucas Souza"]
gem.email = ["lucasas@gmail.com"]
gem.description = %q{TODO: Write a gem description}
gem.summary = %q{TODO: Write a gem summary}
gem.homepage = ""
gem.files = `git ls-files`.split($\)
gem.executables = gem.files.grep(%r{^bin/})
.map{ |f| File.basename(f) }
gem.test_files = gem.files.grep(%r{^(test|spec|features)/})
gem.name = "active_file"
gem.require_paths = ["lib"]
gem.version = ActiveFile::VERSION
end
V a m o sapagaroconteúdoereescrevê-loapenascomasinformações maisrele-
vantes:
require File.expand_path('../lib/active_file/version', __FILE__)
Gem::Specification.new do |gem|
gem.name = "active_file"
gem.version = ActiveFile::VERSION
gem.description = "Just a file system database"
gem.summary = "Just a file system database"
gem.author = "Lucas Souza"
gem.files =
Dir["{lib/**/*.rb,README.md,Rakefile,active_file.gemspec}"]
end
Asinformações declaradassão autodescritivas,sendoamaisimportantedelas
s.filesqueindicaquaisarquivosformarãoocódigofontedagem.
Comessasinformações noarquivo .gemspecbastarodarmosocomando gem
build active_file.gemspeceumarquivo active_file-0.0.1.gemserá
gerado.Parainstalaragemrecémcriada,bastarodarocomando gem install
active_file-0.0.1.gem --local. A p ó sissobastarodarocomando gem
list active_file -dparaverificarqueagemfoiinstaladacomsucesso.
*** LOCAL GEMS ***
active_file (0.0.1)
206

## Página 221

CasadoCódigo Capítulo9. AsbibliotecasnouniversoRuby
Author: Lucas Souza
Installed at: /Users/lucas/.rvm/gems/ruby-1.9.2-p290
Just a file system database
Porfim,sequisermosdistribuiresta gemparadesenvolvedoresRubynomundo
inteiro,bastacriarumcontanositehttp://rubygems.orgesubmetê-la.Paraisso,
bastaexecutarocomando gem push active_file-0.0.1.gemeserão soli-
citadosemailesenharecémcriados. A p ó souploaddagem,bastaacessarhttp:
//rubygems.org/gems/active_file.
Precisamosagoraprepararnossoprojetoparaqueeledeixardeutilizaromó-
dulo ActiveFilequeestádentrodopróprioprojetoepasseautilizaragem
active_filequecriamos,queestáno rubygems. Comonossoprojetojáuti-
lizaagem brnumeroscomodependênciaeusaráagem active_filetambém
comodependência,podemosutilizaro b u n d l e rparagerenciá-las:
source 'http://rubygems.org'
gem 'brnumeros', '3.3.0'
gem 'active_file', '0.0.1'
Rodandoum bundle install, asdependênciassão instaladas. Precisa-
mostambémapagaroarquivo active_file.rbdoprojetoeadicionaralinha
require 'active_file'noarquivo revista.rb:
require 'bundler/setup'
require 'active_file'
class Revista
# implementação
end
Agoraestamosutilizandoomódulo ActiveFileapartirdagem.
Adicionando dependênciasem uma gem
Quandocriamosumagemécomumutilizarmosoutrasgemsparanosauxiliar.
Comissocriamosumdependênciaimplícita,ouseja,oprojetoquedependerdasua
gem,dependeráautomaticamentedagemquevocêutilizouemsuacriação.
207

## Página 222

9.7.Próximospassos CasadoCódigo
Nestecasoérecomendáveldeclararessasdependênciasnoarquivo .gemspec,
assimaoinstalaragememoutrosprojetos,asdependênciaimplícitastambémserão
instaladas:
Gem::Specification.new do |gem|
gem.name = "active_file"
gem.version = ActiveFile::VERSION
gem.description = "Just a file system database"
gem.summary = "Just a file system database"
gem.author = "Lucas Souza"
gem.files =
Dir["{lib/**/*.rb,README.md,Rakefile,active_file.gemspec}"]
# dependência do código com a gem brnumeros
gem.add_dependency "brnumeros", "~> 3.3.0"
end
Precisamos também carregar as dependênciasda gem no arquivo
active_file.rb:
# coding utf-8
# carregando dependências
require "brnumeros"
require "FileUtils"
require "active_file/version"
module ActiveFile
# implementação
end
9.7 Próximos passos
Nestecapítuloaprendemosacriar,gerenciaredistribuirdependênciasnoformato
gem.IssoéessencialparatrabalharcomqualquerprojetoRuby,afinalémuitoco-
mumutilizarmosbibliotecasprontasparafazerpartedotrabalhonecessário.Ge-
renciarestasdependênciastambémémuitomaissimplesutilizandoagem B u n d l e r
queatravésdosarquivos Gemfilee Gemfile.lockcontrolaquaisversões equais
gemsutilizamosemumprojeto.
Nopróximocapítuloveremoscomocriar tasks(pequenosscripts)emaplicações
Rubyutilizandoagem r a k e.
208

## Página 223

Capítulo10
Criando tasksusando Rake
SevocêjáleututoriaisouinvestigouocódigodealgumprojetoescritoemRuby,pro-
vavelmentevocêjáouviufalardeumagemchamada r a k e. Suasprimeirasversões
tinhamemmentecriarumferramentadebuildsimilaraofamoso M a k e.Porém,a
gem r a k epossuimuitasferramentasqueatornamumapoderosabibliotecadeauto-
mação.
Oprimeiropassoparautilizaro r a k eéinstalá-loexecutando gem install
rakenoseuterminalouentãoadicionado-ono Gemfiledoprojetoeexecutando
emseguidaocomando bundle install.A p ó sainstalaçãoteremosdisponívelo
comando rake,porondeexecutaremososscriptsdeautomaçãoqueserãocriados.
Sãomuitosospassosquepodemserautomatizadosdentrodeumprojeto,desde
rodartestesautomaticamente,atérealizaro b u i l ddeumpacotenoambientedepro-
dução.
Nossoaplicativoprecisadeumscriptque“limpe”abasededados,resumida-
mente,precisamosapagartodooconteúdodapasta db/revistas.Issopodeser
feitofacilmentecomoseguintecódigoRuby:

## Página 224

CasadoCódigo
require 'fileutils'
FileUtils.rm Dir['db/revistas/*.yml']
Ocódigoébastantesimples,massetodaavezqueprecisarmosapagarobanco
dedadosfornecessáriorepetirestescript,estamosbastantesujeitosaerros. Seria
bemmaissimplesexecutaralgocomo rake db:cleannoterminal,certo?
Issoépossívelisolandooscriptanterioremuma r a k et a s k.U mpequenoscript
queseráexecutadopelocomando r a k e,queiráprocurarporestesscriptsdentrode
umarquivochamado Rakefile.Agem active_filequecriamosnocapítulo
anteriorpossuiumarquivochamado Rakefilecomoseguinteconteúdo:
#!/usr/bin/env rake
require "bundler/gem_tasks"
Comocriamosagemutilizandoo b u n d l e r,automaticamentetodasassuas r a k e
tasksestãodisponíveisparauso.Podemosremoverestalinhaecriaranossaprópria
t a s kchamada db:clear:
#!/usr/bin/env rake
require 'fileutils'
namespace :db do
task :clear do
FileUtils.rm Dir['db/revistas/*.yml']
end
end
Podemosagorarodarocomando rake -Tqueretornaumalistacomtodas
as tasksencontradasdentrodoarquivo Rakefiledodiretórioonderodamoso
comando.Comoa rake tasknãopossuiumadescrição,elanãoseráretornada
nalistade tasksdisponíveis.Resolvemosesteproblemaadicionandoumadescrição:
#!/usr/bin/env rake
require 'fileutils'
desc "Limpa todas as revistas da pasta db/revistas"
namespace :db do
task :clear do
FileUtils.rm Dir['db/revistas/*.yml']
210

## Página 225

CasadoCódigo Capítulo10.Criando tasksusando Rake
end
end
Serodarmosnovamenteocomando rake -Tobteremososeguinteresultado:
rake db:clear # Limpa todas as revistas da pasta db/revistas
Paratestarmosa r a k et a s kqueacabamosdecriar,bastaexecutarnoterminal
ocomando rake db:clear. Porém,não fazsentidotentarmoslimparobanco
dedadosapartirdapastadagem active_file.Precisamosexporas r a k etasks
criadasparaqueelaspossamserutilizadasdentrodoprojetolojavirtualoudeoutros
projetosondeforemutilizadas.
Oprimeiropassoconsisteemextrairastasksparaarquivosseparados,queficam
emumapastachamada lib/tasks. Fazemosissoporqueastasksadicionadas
dentrodo Rakefilesãodisponibilizadasapenasseexecutarmosocomando rake
dentrodapastaondeomesmoseencontra. V a m o sentão extrairataskparaum
arquivochamado db.rake:
# lib/tasks/db.rake
require 'fileutils'
namespace :db do
desc "Limpa todas as revistas da pasta db/revistas"
task :clear do
FileUtils.rm Dir['db/revistas/*.yml']
end
end
Agoratorna-senecessárioqueastaskscriadasnapasta lib/taskssejamco-
piadasparaoarquivo .gem:
require File.expand_path('../lib/active_file/version', __FILE__)
Gem::Specification.new do |gem|
gem.name = "active_file"
gem.version = ActiveFile::VERSION
gem.description = "Just a file system database"
gem.summary = "Just a file system database"
gem.author = "Lucas Souza"
gem.files = Dir["{lib/**/*.rb,lib/tasks/*.rake,
README.md,Rakefile,active_file.gemspec}"]
end
211

## Página 226

10.1.Parâmetrosnaraketask CasadoCódigo
Porém,terosarquivosondeastasksforamdefinidasdentrodagemnãoésufici-
enteparautilizá-lasdentrodeprojetosexternos.Existeanecessidadedecarregara
classe active_fileeasraketasksexistentesnapasta lib/tasks.Estesarquivos
podemsercarregadosutilizandoométodoimportdorake,quecarregaarquivos
comaextensão .rake:
# coding utf-8
require "fileutils"
require "active_file/version"
require 'rake'
import File.expand_path("../tasks/db.rake", __FILE__)
module ActiveFile
# implementação
end
Alinha File.expand_path("../tasks/db.rake", FILE)retornaoca-
minhoabsolutoparaoarquivo db.rakequecontémasraketasksqueprecisamser
importadas.T a m b é mfoinecessáriocarregaro rake,poisométodoimportfaz
partedesuaAPI.
U mpontoimportantequedeveserressaltadoéqueoconteúdodeumarquivo
.rakeécódigoRuby,ocomando taskéummétodoRubyquetambémfazparte
daAPIpúblicadoRake,issopermitequevocêimplementeumaraketaskutilizando
todasasAPIsRubyquedesejar.
V o l t a n d oaocódigo,paraqueaimplementaçãopossasertestada,bastageraruma
novaversãodagem active_fileeatualizá-ladentrodoprojetodalojavirtual.Ao
executarocomando rake -Tdentrodoprojeto,oseguinteresultadoseráexibido:
rake db:clear # Limpa todas as revistas da pasta db/revistas
Issocomprovaqueastasksqueforamdefinidasdentrodagem active_file,
podemseraproveitadasdentrodeprojetosqueapossuemcomodependência.
10.1 Parâmetros n a rake t a s k
Éextremamenteimportantereceberparâmetrosnainvocaçãodemétodos,afimde
flexibilizá-los.Comas r a k etasksnãoédiferente,émuitocomumanecessidadede
212

## Página 227

CasadoCódigo Capítulo10.Criando tasksusando Rake
flexibilizá-lasparaevitarrepetiçãodecódigo.Porexemplo,sefornecessárioexcluir
obancodedadosreferenteaclasse DVD,nãofaríamosalgocomoocódigoabaixo:
# lib/tasks/db.rake
require 'fileutils'
namespace :db do
desc "Limpa todas as revistas da pasta db/revistas"
task :clear do
FileUtils.rm Dir['db/revistas/*.yml']
end
desc "Limpa todas os dvds da pasta db/dvds"
task :clear_dvds do
FileUtils.rm Dir['db/dvds/*.yml']
end
end
Existemuitarepetiçãonocódigoacima,qualqueralteraçãonaAPI FileUtils
acarretariaemmudançasemtodasas tasksqueexcluemdadosdaspastas. Além
disso,acadanovamídiaquetivermosnosistema,seránecessáriocriarumanova
t a s kpararemovê-las.Aoolharcomcuidadoocódigoépossívelperceberqueaúnica
diferençaentreas taskséapenasonomedapastaondeencontram-seosarquivosque
desejamosexcluir.
Omaisóbvionestecasoéreceberonomedapastaquedesejamosexcluiros
arquivos *.yml,assimflexibiliza-seumaúnicat a s kqueseráresponsávelporapagar
osarquivosdequalquermídiaexistenteounovadentrodosistema. V a m o sentão
receberoparâmetro folderna rake task db:clear:
# lib/tasks/db.rake
require 'fileutils'
namespace :db do
desc "Limpa todas os arquivos de uma midia"
task :clear, [:folder] do |task, args|
FileUtils.rm Dir["db/#{args.folder}/*.yml"]
end
end
Todososparâmetrosqueprecisamserrecebidosnachamadada r a k et a s k,de-
vemseradicionadoslogoapósseunomeemformadeum Array.Aoexecutaro
213

## Página 228

10.1.Parâmetrosnaraketask CasadoCódigo
comando rake -To r a k einformaquea t a s kdb:clearprecisaserinvocadacom
umparâmetrochamado folder:
rake db:clean[folder] # Limpa todas os arquivos de uma midia
Outraalteraçãofeitanocódigosãoosdoisargumentosrecebidosnobloco.O
primeiroparâmetro task,éumobjetodotipo Rake::Taskqueguardaasinfor-
maçõesdatask,osegundoargumentoargscontémosvalorespassadosnachamada
dataskemformade open-struct,ouseja,parautilizaroparâmetro folderdecla-
radosdeve-sefazê-loutilizando args.folder,comodefatofoifeito.
Parainvocara r a k et a s kbastapassaroargumentoentre []:
rake db:clear['revistas']
rake db:clear['dvds']
Múltiplosparâmetros
Se necessárioreceber váriosargumentosna r a k et a s k, basta declará-losno
Arraydeparâmetrosdefinidosapósonomedatask:
# lib/tasks/db.rake
require 'fileutils'
namespace :db do
desc "Limpa todas os arquivos de uma midia"
task :clear, [:folder, :file_extension] do |task, args|
FileUtils.rm Dir["db/#{args.folder}/*.#{args.file_extension}"]
end
end
Parainvocara r a k et a s kbastainformarosdoisparâmetrosseparadosporvírgula:
rake db:clear['revistas','yml']
Porém,existeumdetalheimportantenachamadada r a k et a s k.Reparequenão
colocamosocaracteredeespaçonachamadada t a s k,porqueachamadadeveser
feitaemumúnicocomando,juntandooseunomeeargumentos.Sefornecessário
invocara t a s kpassandonomeeargumentosutilizandoespaços,oargumentoparao
comando rakedevesercolocadoentreaspas.Algocomoocomandoabaixo:
rake "db:clear['revistas', 'yml']"
214

## Página 229

CasadoCódigo Capítulo10.Criando tasksusando Rake
10.2 Ta s k sco m p r é-requisitos
Podemoscriar tasksquesãoutilizadascompré-requisitosdeoutras.U m at a s kmuito
comumquandoutiliza-se A c t i v eRecordéa db:seedquepopulaobancodedados.
V a m o scriaruma t a s ksimilarao db:seed:
# lib/tasks/db.rake
require 'fileutils'
namespace :db do
desc "Limpa todas os arquivos de uma midia"
task :clear, [:folder] do |task, args|
FileUtils.rm Dir["db/#{args.folder}/*.yml"]
end
desc "Popula com os dados definidos no arquivo db/folder/seeds.rb"
task :seed, [:folder] do
seed_file = File.expand_path "db/#{args.folder}/seeds.rb"
load(seed_file) if File.exist?(seed_file)
end
end
A t a s kprocuraporumarquivo db/seeds.rbeocarregacasoeleexista. O
arquivo seeds.rbécontémocódigoRubyquepopulaobancocomdadosiniciais,
porexemplo:
require "active_file"
require "revista"
Revista.new(titulo: "Veja", valor: 10.90).save
Revista.new(titulo: "Época", valor: 12.90).save
Aoexecutara r a k et a s kpelocomando db:seeddoisobjetosdotipo Revista
serãocriados.
Outra r a k et a s kbastanteútilqueexisteno Active Recordéa db:reseedque
possuiomesmocomportamentoda db:seed,porém,removeosdadosexistentes
nobancoantesdepopulá-lonovamente.U m at a s kcomoessapodeserimplemen-
tadafacilmentenagem active_file:
# lib/tasks/db.rake
require 'fileutils'
215

## Página 230

10.2.T a s k scompré-requisitos CasadoCódigo
namespace :db do
desc "Limpa todas os arquivos de uma midia"
task :clear, [:folder] do |task, args|
FileUtils.rm Dir["db/#{args.folder}/*.yml"]
end
desc "Popula com os dados definidos no arquivo db/folder/seeds.rb"
task :seed, [:folder] do
seed_file = File.expand_path "db/#{args.folder}/seeds.rb"
load(seed_file) if File.exist?(seed_file)
end
desc "Popula com os dados definidos no arquivo db/folder/seeds.rb,
apagando os existentes"
task :reseed, [:folder] do
FileUtils.rm Dir["db/#{args.folder}/*.yml"]
seed_file = File.expand_path "db/#{args.folder}/seeds.rb"
load(seed_file) if File.exist?(seed_file)
end
end
Reparequeocódigoda t a s kreseedéumacópiadas tasks cleare seedna
ordem.Comoocomportamentoquedesejamosexecutarfoifeitoemoutras tasks,
podemosreutilizá-las:
# lib/tasks/db.rake
require 'fileutils'
namespace :db do
desc "Limpa todas os arquivos de uma midia"
task :clear, [:folder] do |task, args|
FileUtils.rm Dir["db/#{args.folder}/*.yml"]
end
desc "Popula com os dados definidos no arquivo db/folder/seeds.rb"
task :seed, [:folder] do
seed_file = File.expand_path "db/#{args.folder}/seeds.rb"
load(seed_file) if File.exist?(seed_file)
end
216

## Página 231

CasadoCódigo Capítulo10.Criando tasksusando Rake
desc "Popula com os dados definidos no arquivo db/folder/seeds.rb,
apagando os existentes"
task :reseed, [:folder] => ["db:clear", "db:seed"] do
end
end
Nadefiniçãoda t a s kdb:reseeddeclaramoscomopré-requisitoaexecuçãodas
tasks db:cleare db:seeddeclarando-ascomoum Arrayquerepresentaovalor
do Hashcujachavesãoosparâmetrosenomeda t a s k.
10.3 Próximos passos
O rakeéumaferramentaessencialquandoexisteanecessidadedeautomatizar
tarefasnalinguagemRuby.AgrandemaioriadosprojetosescritosemRubyeprin-
cipalmenteoRails,omaisfamosodeles,utilizam rake. Portanto,exploreainda
maisasuadocumentaçãoetenteautomatizarastarefasdoseuprojetoutilizando-
o.OutrosdesenvolvedoresquechegarãoaoprojetoeconheceremRubynãoterão
dificuldadesparalidarcomessesscripts.
Nopróximocapítulo,aprenderemosalidarcomváriasversões doRubyna
mesmamáquinaecomoseparargemsemlugaresdiferentes,organizandomelhor
seuambienteeevitandoconflitos,utilizandoRVM.
217

## Página 233

Capítulo11
R V M(Ruby Version Manager)
Ruby Version Manager,maisconhecidocomoRVM,permitedentreoutrascoisas,
queváriasversões doRubysejaminstaladasemumamáquina.Issoébastanteútil
principalmentenasmáquinasdosdesenvolvedores,quemuitasvezesprecisamdar
manutençãoemprojetosqueutilizamversões diferentesdoRuby.
NessecapítulovocêvaiaprendertambémqueoR V Mpossuimaisutilidadesdo
queapenastrocarentreversões doRuby.
11.1 Instalação
OprimeiropassoparautilizaroR V Méinstalá-loemsuamáquina.Sevocêutiliza
MacOSouLinuxbastatero curleo makeinstalados. Emseguidaexecuteo
seguintecomando:
bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)
Executandoocomandoacima,oR V Mseráinstaladonodiretóriohomedoseu
usuário.ComooR V Méutilizadovialinhadecomando,énecessárioqueeleseja

## Página 234

11.1.Instalação CasadoCódigo
carregadopeloarquivo .bash_profileou .bashrc.Abraoarquivoeadicione
aseguintelinha:
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"
Ouexecutealinhaabaixonoterminal:
echo '[[ -s "$HOME/.rvm/scripts/rvm" ]] &&
source "$HOME/.rvm/scripts/rvm"' >> .bash_profile
Bastaagorarecarregaro .bash_profileparaqueoR V Mestejadisponívelna
linhadecomando.
source ~/.bash_profile
Lembre-sequeumavezqueeleestiverconfiguradodentrodo .bashrc,sempre
quevocêselogar,eleserácarregadoautomaticamente.
VerifiquequeoR V Mfoiinstaladocorretamente,executandoocomando: rvm
notesquemostraráalgumasinformações sobreoR V Meseusistemaoperacional.
Instalação no Windows
SevocêutilizaWindows,tambémpodeinstalaroR V Memsuamá-
quina.Bastaseguiressepost:http://blog.developwithpassion.com/2012/
03/30/installing-rvm-with-cygwin-on-windows que explica em deta-
lhescomoinstalareconfiguraroR V Memsuamáquina.
Dependendodoseusistemaoperacional,énecessárioainstalaçãodealgumas
dependências.Paravisualizá-lasbastaexecutarocomando rvm requirements:
Notes for Mac OS X 10.8.2, Xcode 4.5.2.
For MacRuby: Install LLVM first.
For JRuby: Install the JDK.
See http://developer.apple.com/java/download/
For IronRuby: Install Mono >= 2.6
For Ruby 1.9.3: Install libksba # If using Homebrew,
'brew install libksba'
220

## Página 235

CasadoCódigo Capítulo11.RVM(Ruby Version Manager)
Emgeral,aoexecutarestecomandovocêvisualizaráoqueprecisaparainstalar
cadaumadasversõesdoRuby.Executarestecomandocomfrequênciagarantiráque
suainstalaçãocontinuesemprefuncionando.
11.2 Instalando diferentes Rubies
Aexpressão ru b i e sémuitocomumnomundoRVM,equenaverdadesignificater
váriasversões doRubyinstaladas.Mascomoinstala-seumaversãodoRubyutili-
zandoRVM?V a m o scomeçarinstalandoaversãodoRubyMRI1.9.3:
rvm install 1.9.3
Duranteainstalação,vocêverámensagenscomo:
Installing Ruby from source to:
/Users/lucas/.rvm/rubies/ruby-1.9.3-p194,
this may take a while depending on your cpu(s)...
ruby-1.9.3-p194 - #fetching
ruby-1.9.3-p194 - #extracted to /Users/lucas/.rvm/src/ruby-1.9.3-p194
(already extracted)
ruby-1.9.3-p194 - #configuring
ruby-1.9.3-p194 - #compiling
ruby-1.9.3-p194 - #installing
Removing old Rubygems files...
Installing rubygems-1.8.24 for ruby-1.9.3-p194 ...
Installation of rubygems completed successfully.
ruby-1.9.3-p194 - adjusting #shebangs for
(gem irb erb ri rdoc testrb rake).
ruby-1.9.3-p194 - #importing default gemsets
(/Users/lucas/.rvm/gemsets/)
Install of ruby-1.9.3-p194 - #complete
ParautilizaraversãoquefoiinstaladautilizandoRVM,bastaexecutar:
rvm use 1.9.3
Agora,aoexecutar ruby -vaversão1.9.3-pxxxseráexibida:
ruby 1.9.3p194 (2012-04-20 revision 35410) [x86_64-darwin12.2.0]
221

## Página 236

11.3.Organizesuasgemsutilizandogemsets CasadoCódigo
Éimportanteressaltarquepor defaultaversão doRubyemsuamáquinaéa
versão instaladadiretamentenosistemaoperacional. Sevocêquiserqueaversão
defaultdosistemasejaumaversãofornecidapeloRVM,bastaexecutar:
rvm --default 1.9.3
Aoexecutar ruby -vaversão 1.9.3seráexibidacomoversão defaultdasua
máquina.
Nopróximocapítuloveremosalgumasnovidadesqueestãopresentesnaversão
2.0doRuby.Então,jávamosnospreparareinstalaroRuby2.0:
rvm install ruby-2.0.0-p0
Parautilizaraversãorecém-instaladabastaexecutar:
rvm use ruby-2.0.0-p0
Pronto!Agoraestamosutilizandoaversão 2.0.0-p0.Semprequequiservoltar
autilizaralgumaversão específicadoprojetobastautilizarocomando rvm use
*ruby version aqui*.
ParainstalaroutrosinterpretadoresRuby,bastaseguirosmesmospassosdes-
critosanteriormente.Asversões suportadaspeloR V Mpodemservistasem:https:
//rvm.io/interpreters/
11.3 Organize suas gems utilizando gemsets
OR V McriacompartimentosindependentesparacadaversãodoRubyinstalada,ou
seja,ointerpretadorRuby,asgemseoIRBsão todosseparadosdosistemaeuns
dosoutros.Oquepodeaconteceréquedoisprojetosqueutilizamamesmaversão
doRubyprecisemdeversões diferentesdeumadeterminadagem.Comoasgems
sãoseparadosapenasporinstalações doRuby,oespaçodegemsteriaduasversões
damesmagem,oquepoderiacausarconflitosemsuautilização eaobrigação de
utilizarocomando b u n d l eexecparaexecutaroprojetocomasversões corretasde
cadagem.
OR V MpermitequedentrodoespaçodegemsdecadainstalaçãodoRuby,sejam
criadosespaçosseparadosparaasgemsdecadaprojeto,evitandoconflitosdever-
sões emantendoseusistemamaisorganizado.Estesespaçossãoconhecidoscomo
gemsets(conjuntodegems). Etambémpossuiintegraçãocomocomando b u n d l e
installqueinstalaráasgemsdiretamentenogemsetconfigurado.
222

## Página 237

CasadoCódigo Capítulo11.RVM(Ruby Version Manager)
Crie gemsets
Paracriarumnovo gemsetbastaexecutar:
rvm gemset create loja_virtual
# => 'loja_virtual' gemset created
(/home/lucas/.rvm/gems/ruby-1.9.3-p194@loja_virtual).
Parautilizaro gemsetcriadobastaexecutar:
rvm use 1.9.3@loja_virtual
# => Using /Users/lucas/.rvm/gems/ruby-1.9.3-p194
with gemset loja_virtual
Naraizdoprojeto,vamosrodarocomando bundle installeapósasua
execuçãopodemosverificarasgemsinstaladasno gemsetexecutandoocomando
quejávimosanteriormente gem list:
*** LOCAL GEMS ***
active_file (0.0.5)
brnumeros (3.3.0)
Paracomprovarqueasgemsestãoisoladasno gemset,vamoscriarumoutro
novoeinstalaro railsnela:
rvm gemset create novo_gemset
rvm use 1.9.3@novo_gemset
gem install rails
Executandoocomando gem listserão listadasapenaso railsesuasde-
pendências:
*** LOCAL GEMS ***
actionmailer (3.2.11)
actionpack (3.2.11)
activemodel (3.2.11)
activerecord (3.2.11)
activeresource (3.2.11)
activesupport (3.2.11)
...
223

## Página 238

11.4.T r o q u eautomaticamentedegemsetscom.rvmrc CasadoCódigo
Asgemsexistentesno gemset‘loja_virtual’nãosãolistadas,poisestãoisoladas.
Removendo gems d osistema
OR V Mpossuium gemsetchamado globalondeasgemsinstaladas
antesdautilizaçãodoR V Mestão:
rvm use 1.9.3@global
# => Using /Users/lucas/.rvm/gems/ruby-1.9.3-p194
with gemset global
gem list
*** LOCAL GEMS ***
bundler (1.2.3)
rake (10.0.3, 10.0.2)
rubygems-bundler (1.1.0)
rvm (1.11.3.5)
Jáqueestamosorganizandoasgemsem gemsets,devemosremover
asgemsglobais.Bastaexecutarocomando rvm gemset emptyque
limparáo gemsetquevocêestiverutilizando.
O gemset globalébastanteútilparaadicionarautomaticamentegems
queserãoutilizadasportodasasnovasinstalações ounovos gemsetscri-
ados. Asgems rakee bundlersãobonsexemplosdedependências
queestarãopresentesnagrandemaioria gemsetscriados.
11.4 Tr o q u e automaticamente de gemsets co m
.rvmrc
Aoutilizarmaisdeum gemset,énecessáriolembrardetrocá-lodeacordocomopro-
jetoqueestamostrabalhando.Comoprogramadores,éruimtermosquelembrarde
executarocomando rvm use 1.9.3@meu_gemsetatodomomento.Emgeral,
preferimosqueestascoisassejamfeitasdemaneiraautomática.
Oarquivo .rvmrcpermitequeestastrocassejamfeitasdemaneiraautomática.
Aoadicionarumarquivochamado .rvmrcdentrodoprojeto,todavezqueentrar-
mosnapastadoprojeto,oR V Miráprocurarporessearquivoeexecutarocomando
queseencontradentrodele.
224

## Página 239

CasadoCódigo Capítulo11.RVM(Ruby Version Manager)
Oarquivo .rvmrcterá,geralmente,alinhacorrespondeatrocaparao gemset
doprojeto.Porexemplo,oarquivo .rvmrcdoprojeto loja v i r t u a lteráoseguinte
conteúdo:
rvm use 1.9.3@loja_virtual
Porém,ocódigoacimaaoserexecutadopelaprimeiravez,nosalertaráquenão
podemosutilizarum gemsetquenãofoicriado:
Gemset 'loja_virtual' does not exist, 'rvm gemset create loja_virtual'
first, or append '--create'.
ComofoialertadopeloRVM,podemosapenasadicionaro --createdentro
do .rvmrc:
rvm use 1.9.3@loja_virtual --create
Criando gemset e rvmrc em u m a linha
Épossívelcriarumnovo gemseteseurespectivo .rvmrcexecu-
tandoaseguintelinha:
rvm --create --rvmrc 1.9.3@seu_gemset
11.5 Próximos passos
Oobjetivodestecapítulofoidescrevercomofuncionamasprincipaisfuncionalida-
desdoRVM.V o c êpodeconsultaradocumentaçãodoR V Mnosite:https://rvm.io
ondesãolistadastodasassuasfuncionalidades.
Nopróximocapítuloveremosasnovas f e at u re squeestarãodisponíveisnanova
versãodalinguagemRuby.Faremosalgunstesteseexploraremosseusnovoscon-
ceitos,quetornarãoavidadosdesenvolvedoresRubyumpoucomaisfácildoquejá
é.
225

## Página 241

Capítulo12
R u b y2.0
Aversãofinalfoilançadanodia24defevereiro,exatamentenovigésimoaniversário
desuaprimeiraversão. Aideiadestecapítuloéfalarsobreasprincipaismudanças
queocorrerãonalinguagemquevocêaprendeuduranteoscapítulosanteriores.
U m alistacompletacomasmudançasintroduzidasnaversão2.0podemservis-
tasaqui:https://github.com/ruby/ruby/blob/v2_0_0_rc1/NEWS,enquantoqueaqui
nosateremosàsprincipais:
•Refinements
•N a m e dParameters
•Module prepend
•E n u m e r a b l eLazy
•Encoding UTF-8

## Página 242

12.1.EvitandomonkeypatchescomRefinements CasadoCódigo
12.1 Evitando monkey patches co m Refinements
V o c êaprendeuanteriormentequeépossível abrirmosumaclasseRubyeadicionar
novosmétodosdinamicamente. Porexemplo,podemosabriraclasse Stringe
adicionarumnovométodochamado bang:
class String
def bang
"#{self}!"
end
end
Executandoocódigoacima,fazcomquetodososobjetosdotipo Stringte-
nhamummétodochamado bang:
"ruby".bang # => "ruby!"
"rails".bang # => "rails!"
Rubyéumalinguagemondetodasasclassessãomutáveis.Essahabilidadede
alterarclassesem runtimeéutilizadaemdiversasbibliotecas. U mexemplo,éo
ActiveSupport,umapedaçodoRailsqueabreváriasclassesdocoredoRuby,para
adicionarmétodosutilitáriosquevisamfacilitarodesenvolvimento.Essatécnicaé
conhecidanacomunidadeRuby,como M o n k e yP a t c h.
Porém,abrirumaclasseeadicionarmétodosarbitrárioséumatécnicaquesti-
onável.A p e s a rdeparecerlegal,podenostrazergrandestranstornos.Oproblema
principaldestaabordageméqueassimcomonósabrimosaclasse Stringeadici-
onamosummétodochamado bang,qualqueroutrabibliotecaRubyqueutilizamos
podefazerexatamenteamesmacoisa.Oqueacontecerianestecasodependemuito
daordemdecarregamento,oquecausariatambémcomportamentosinesperadosna
execuçãodaaplicação.
Amudançafeitanaclasse Stringéglobaletrabalharcomescoposglobaissem-
preéruim,porterdecontrolarcadalugarquepode,eventualmente,alteraraquele
escopo.
Pensandonestesproblemasrecorrentesoriundosdasversões atuaisdoRuby,foi
pensadoumafuncionalidadechamada refinements,quevisaalteraroescopode
umaclasseapenasemcontextolocal,ouseja,vocêescolheomomentoexatoque
desejaqueaclasse Stringtenhaométodobang.Issoevitaospossíveisproblemas
descritosanteriormente.
228

## Página 243

CasadoCódigo Capítulo12.Ruby2.0
V a m o svercomoessanova f e at u redalinguagemRubyfunciona.Existemdois
métodosimportantesquetemosqueconhecerquandodecidimosutilizaros r e fi n e-
ments,oprimeiroéométodorefinedomódulo Kernel,quepermitequeo mon-
key patchsejafeitoemumescopolocal,naverdade,elefuncionacomosefosseum
containerdemétodosadicionaisquepodemserutilizadosemumfuturopróximo
dentrodeumescopoquenãosejaglobal.
Osegundoéométodousing,quepermitequeos refinementssejamutilizados
emumaclasseoumétodo,ouseja,permitequeosmétodos“adicionais”daclasse
Stringsejaminjetadosnoescopoondevocêinvocá-lo,ouseja,osmétodosserão
adicionadosapenasnoescopoondevocêefetuouachamada,paratodososoutros,
ométodobangsimplesmentenãoexistirá.
Paraimplementar refinements,oprimeiropassoéabriraclasse Stringeadi-
cionarométodobangutilizandoométodoKernel#refine:
module StringBang
refine String do
def bang
"#{self}!"
end
end
end
Agora,setentarmosinvocarométodobangemumobjeto String,seráretor-
nadaumaexceçãodizendoqueométodonãoexiste:
"ruby".bang
# => NoMethodError: undefined method `bang' for "":String
Issoaconteceuporqueaclasse Stringfoialteradaemumescopolocal.Para
utilizaro refinementquefoifeito,devemosutilizarométodousing,noobjetomain:
using StringBang
"ruby".bang # => "ruby!"
class DVD
# outros metodos aqui
def titulo
@titulo.bang
end
end
229

## Página 244

12.2.NamedParameters CasadoCódigo
dvd = DVD.new "Chitãozinho e Xororo"
dvd.titulo # => "Chitãozinho e Xororo!"
Essaéumaimportante f e at u renaversão2.0queevitaráváriosproblemasqueos
monkey patchesglobaispodemcausar.Adicaparavocêqueutiliza monkey patchesé
evitá-losaomáximo.U m aboaalternativaécriarmódulosquedefinemosmétodos
quevocêdesejaincluireutilizaro extendparaincluí-losapenasnosobjetosque
vocêdeseja:
module Banger
def bang
"#{self}!"
end
end
"ruby".extend(Banger).bang # => "ruby!"
Nocódigoacima,nóstambémestamosadicionandoométododesejadoemum
escoponão global. Porém,adicionamosapenasnosobjetosdotipo Stringque
desejamos.A p e s a rdeserbastantechatoinvocar extend(Bang)emvárioslugares,
ébemmaisgarantidoquenãoteremosproblemasfuturos.
12.2 Named Parameters
Lançadocomonome Keywords Arguments,estanova f e at u redalinguagemRubyjá
existeemoutraslinguagenshábastantetempoefoifinalmenteintroduzidananova
versão.
Paravocêquenãoconhece named parametersvamosentenderoproblemaque
esteconceitoresolve. Supondoquevocêtenhaummétodochamado setupque
precisareceberalgumasinformações: timeoute name.Implementamosométodo
comocódigoabaixo:
def setup(timeout, name)
p timeout * 1000, name
end
Aoinvocarmosométodosetup,devemospassarosargumentosdeacordocom
aposiçãoqueelesforamdeclarados:
230

## Página 245

CasadoCódigo Capítulo12.Ruby2.0
setup 60, 'correios'
Seinvocarmosométodotrocandoaposiçãodosparâmetrospodemostersur-
presas:
setup 'correios', 60
# => correioscorreioscorreios...
A String‘correios’seráimpressa1000vezesnasaídadoconsole.Aoutilizar-
mos named parameters,invocamosométodopassandonãoapenasosvaloresdospa-
râmetros,mastambém,qualargumentoreceberáaquelevalor.Faremosalgocomo
ocódigoabaixo:
setup timeout: 60, name: 'correios'
# => 60000, 'correios'
Porém,paraestecódigofuncionar,devemosalteraraimplementaçãodométodo
parasuportar named parameters:
def setup(timeout: 0, name: '')
p timeout, name
end
Énecessáriodeclararumvalor defaultparaqueosargumentospossamserpre-
enchidoscorretamentenachamadadométodoutilizando named parameters.Essa
novaimplementaçãodométodosetupnospermiteinvocarométododasseguintes
maneiras:
# passando apenas o atributo timeout
setup timeout: 20
# => 20, ''
# passando apenas o atributo name
setup name: 'sedex'
# => 0, 'sedex'
# passando nenhum deles
setup
# => 0, ''
# passando os atributos em ordem inversa
setup name: 'sedex', timeout: 20
# => 20, 'sedex'
231

## Página 246

12.2.NamedParameters CasadoCódigo
Omaisinteressanteéquenãoprecisamospassarosargumentosnaordemcor-
reta,bastachamarométodopassandoovalordecadaargumentoatravésdeseu
nome.
V a m o salterarumpoucoométodosetupadicionandoumatributoquenão
teráacaracterísticadeum named parameter:
def setup(value, timeout: 0, name: '')
p value, timeout, name
end
Comessamudança,todasaschamadasqueforamfeitasnoexemploanterior,
nãofuncionarão,poisoatributo value,estádeclaradocomoatributoobrigatório
edeveser sempreoprimeiroatributoaserpassadonachamadadométodo.Sendo
assimaschamadasanterioresdevemsertransformadas:
# passando apenas o atributo timeout
setup 79.9, timeout: 20
# => 79.9, 20, ''
# passando apenas o atributo name
setup 79.9, name: 'sedex'
# => 79.9, 0, 'sedex'
# passando nenhum deles
setup 79.9
# => 79.9, 0, ''
# passando os atributos em ordem inversa
setup 79.9, name: 'sedex', timeout: 20
# => 79.9, 20, 'sedex'
# passando o parametro valor no final
setup name: 'sedex', timeout: 20, 79.9
# => SyntaxError: (irb):19: syntax error
Issodeixaumpoucoclaroqueos named parametersnaverdadesãoapenasatri-
butoscomvalores default.
V a m o sexplorarumpoucomaisos named parameterstentandodeclararumnovo
atributoapósoúltimonamed parameter:
232

## Página 247

CasadoCódigo Capítulo12.Ruby2.0
def setup(value, timeout: 0, name: '', url)
p value, timeout, name, url
end
# => SyntaxError: (irb):23: syntax error, unexpected tIDENTIFIER
OinterpretadorRubynão permitequetaldeclaração demétodosejafeita. É
permitidoapenasqueum Hashsejadeclaradocomoatributonãonomeadonofinal
dadeclaraçãodeummétodo:
def setup(value, timeout: 0, name: '', **options)
p value, timeout, name, options
end
Comesteúltimosargumento,podemosinvocarométodosetuppassandoum
Hashcomosvaloresquequisermos:
setup 79.9, name: 'sedex', timeout: 20,
url: 'http://correios.cep.com.br/consulta'
# => 79.9, 20, 'sedex', { :url => "http://correios.cep.com.br/consulta" }
Adicaentão ésempredeclararos named parametersnofinaldométodoeos
outrosatributosnocomeço.
12.3 Utilizeprepend a oinvés de include
V a m o srelembrarrapidamentecomofuncionamosmódulosemRuby. Módulos,
podemserutilizadosparaacriaçãode namespacesoucomo containerdemétodos
queserãoincluídosemclasses,técnicaconhecidacomo mixings.Porexemplo:
module FormatadorMoeda
def valor_formatado
@valor.por_extenso_em_reais
end
end
class DVD
include FormatadorMoeda
def initialize(valor)
233

## Página 248

12.3.Utilizeprependaoinvésdeinclude CasadoCódigo
@valor = valor
end
end
dvd = DVD.new 56.6
dvd.valor_formatado # => cinquenta e seis reais e sessenta centavos
Comovimosanteriormente,aodar includedeummódulodentrodeuma
classe,amesma‘ganha’todososmétodosqueforamdeclaradosnomódulo. Al-
gumdesenvolvedormaisdesatento,poderecriarummétodovalor_formatado
naclasse DVDcomumcomportamentocompletamentediferentedoqueforadefi-
nidonomódulo:
class DVD
include FormatadorMoeda
def initialize(valor)
@valor = valor
end
def valor_formatado
"R$ #{@valor}"
end
end
dvd = DVD.new 56.6
dvd.valor_formatado # => R$ 56.6
E o comportamentodo método valor_formatado definido no módulo
FormatadorMoedafoisobrescritopelaprópriaclassequeoincluiu.Oqueaconte-
ceunaverdadenãofoiumasobrescritademétodo,oqueaconteceuéqueointer-
pretadorRubysempreiráprocurarpelométodorespeitandoo object model,ou
seja,primeiroirábuscarométodonaprópriaclasse DVDecomoencontraráumaim-
plementaçãodométodovalor_formatadodisponível,iráexecutá-loenãoserá
necessárioprocurá-lodentrodomódulo FormatadorMoeda.
Podemos ordenar que o interpretador Ruby procure pelo método
valor_formatado primeiro nos módulos e depois na própria classe DVD,
bastautilizarmosométodoprependenãomaisométodoinclude:
class DVD
prepend FormatadorMoeda
234

## Página 249

CasadoCódigo Capítulo12.Ruby2.0
def initialize(valor)
@valor = valor
end
def valor_formatado
"R$ #{@valor}"
end
end
dvd = DVD.new 56.6
dvd.valor_formatado # => cinquenta e seis reais e sessenta centavos
Reparequeométodo valor_formatadofoiprocuradoprimeiramenteno
FormatadorMoedaecomoomesmofoiencontrado,nãofoinecessáriobuscá-lo
naclasse DVD.
12.4 Utilizando lazy l o a dno módulo Enumerable
Rubyéumalinguagemimperativa,porém,permitequesejamfeitoscódigoselegan-
tesquepossuemcaracterísticasfuncionais.Porexemplo:
[1, 2, 3, 4, 2, 5].map { |numero| numero * 10 }
# [10, 20, 30, 40, 20, 50]
Criamosumnovo Arrayapartirdoprimeiro Arraycomtodososnúmeros
multiplicadospor10. Agora,precisamosquedestenovo Arraysejamextraídos
apenasosnúmerosmaioresque30.Simples:
[1, 2, 3, 4, 2, 5].map { |numero| numero * 10 }
.select { |numero| numero > 30 }
# [40, 50]
Porém,ocódigoacimaapesardeserbastanteeleganteelegível,possuiumpro-
blemadeperformance. São criados Arraysintermediáriosacadamanipulação
queéfeita,nestecaso,dois Arraysdesnecessários.Naverdade,aomanipularum
Arraypequenocomoodoexemplo,issopodenãoparecerumproblema,masse
estivéssemosparseandoumarquivode1GBteríamossériosproblemas.
Aversão 2.0doRubycopiou,nobomsentido,umacaracterísticapresentena
maioriadaslinguagensfuncionaisexistentes,as lazy collections. Issosignificaque
235

## Página 250

12.5.EncodingUTF-8 CasadoCódigo
podemosevitaracriaçãodestes Arraysintermediárioseexecutaroprocessamento
dasfunções utilizadasparamanipularacoleçãoumaúnicavez.
Napráticabastainvocarmosométodo lazyantesdeencadearaschamadas
funcionaisnosdadosquedesejamosmanipular:
[1, 2, 3, 4, 2, 5].lazy.map { |numero| numero * 10 }
.select { |numero| numero > 30 }
# <Enumerator::Lazy:
# <Enumerator::Lazy:
#<Enumerator::Lazy: [1, 2, 3, 4, 2, 5]>:map>:select>
Reparequeoretornonãoforamosnúmeros40e50comoanteriormente.Ao
invésdisso,foiretornadoumobjeto Enumerator::Lazy,ouseja,nenhumpro-
cessamentofoifeitonocódigoanterior.Paraqueasfunções mape selectsejam
executadasno Arrayoriginal,bastainvocarométodoto_a:
lazy_array = [1, 2, 3, 4, 2, 5].lazy
.map { |numero| numero * 10 }
.select { |numero| numero > 30 }
p lazy_array.to_a
# [40, 50]
12.5 Encoding UTF-8
Naversão 1.9doRuby,o encoding defaulté US-ASCII.Napráticaissosignifica
quesevocêquiserutilizarcaracteresacentuados,seránecessárioautilizaçãodeum
comentárionocomeçodoarquivo: # coding: utf-8ouumaexceção invalid
multibyte char (US-ASCII)serálançada.
Noversão2.0o encoding defaultéUTF-8.Comissoaoescrevercaracterescom
acento,nãoémaisnecessárioautilizaçãodocomentárioquealterao encoding.V o c ê
podequerermanteracompatibilidadeentreasversões 1.9e2.0,nestecaso,manter
ocomentárioénecessário.
12.6 Próximos passos
Nestecapítulosvimosasprincipaisnovidadesqueestão disponíveisnaversão 2.0
dalinguagemRuby.Nopróximo,veremosumdosassuntosmaispolêmicossobrea
linguagem:concorrênciaeparalelismo.VeremosseissoexistedeverdadeemRuby
236

## Página 251

CasadoCódigo Capítulo12.Ruby2.0
equaisasvantagensedesvantagensdecadaumadasabordagensdisponíveisatual-
mente.
237

## Página 253

Capítulo13
Apêndice:Concorrênciae
paralelismo
Concorrênciaéacapacidadedecomporumcenárioondeastarefaspodemserexe-
cutadasindependentesumadasoutras.Paralelismoéacapacidadedeexecutarvárias
destastarefassimultaneamente.
Complicadonãoémesmo?V o utentaralgo‘ d omundoreal’paraexemplificara
diferençaentreestesdoisconceitoscomputacionais.
V a m o ssuporquevocêprecisafazerexercíciosdematemáticaehistóriaquefo-
ramatribuídoscomo homework.V o c êdecideresolverumexercíciodematemáticae
depoisumexercíciodehistória,depoisvocêfazoutroexercíciodematemáticaeapós
umoutroexercíciodehistória,atéquetodososproblemasestejamresolvidos.Ao
trazermosametáforaparaomundodacomputação,estamosfazendoosexercícios
deformaconcorrente.
Seconcorrênciasignificafazerváriastarefassimultaneamenteumadecadavez,
oqueéparalelismo?Paralelismoéahabilidadedeexecutarumpoucodecadatarefa,

## Página 254

CasadoCódigo
demaneirasimultânea.Porexemplo,dirigirseuveículoefazerumaudiocursode
inglêsaomesmotempo.V o c êpodeprogredirnasduastarefasdemaneirasimultâ-
nea.
Trazendodevoltaparaomundodacomputação,maisespecificamenteparao
mundoweb,suponhaquevocêtemumaaplicaçãoRailsquepossuiumgrandetrá-
fegodeusuários,algoemtornode1requestporsegundo.Aoexecutarumbench-
marknestaaplicaçãovocêpercebequeamesmatemumamédiadetempoderes-
postaemtornode100msporrequest,oquenoslevaacrerqueaaplicaçãosuporta
10requestsporsegundo,aproximadamente.
Seaaplicaçãoalcançarumnúmeromaiorque10requestsporsegundo,elesse-
rãoenfileiradose startadosapenasquandooservidorestiverlivre,causandoumau-
mentonotempofinaldorequest.Esseéumdosmotivospelosquaisdevemosnos
preocuparcomconcorrênciaeparalelismo.Independentedalinguagemqueesta-
mosfalando,existemdiversasmaneirasderesolveresteproblema. Cadaumadas
soluções causamuitadiscussão,pois,muitaspessoasdefendemseuspontosdevista,
tantoosbonsquantoosruins. Frasescomo:‘Rubynãoescala’sãomuitocomuns,
porém,éumsinaldequeodesenvolvedornão entendecorretamenteoqueéne-
cessárioparaescalarumprogramafeitoemdeterminadalinguagem,sejaelaqual
for.
Osmaissensatosdefenderãosuasabordagensparaescalarosistema,algunsde-
fendemautilizaçãodeThreads,mastalvezseesquecemdasdificuldadesdelidarcom
memóriacompartilhada,outrosdizemquevocêdevetrocaralinguagemeutilizar
Node.js,porexemplo. Existemosquedefendemaprogramação orientada(event
based)dentrodapróprialinguagemhospedeira.
Oimportanteéentenderosbenefíciosemalefíciosquecadaumadasaborda-
genspodemtrazerparasuaequipeeparaasuaempresa,eescolheraquemelhorse
encaixanoproblema.Entenderqueaescolhadalinguagemmudaadecisãoqueserá
tomadaparamelhoraraperformancedeumaaplicaçãotambéméimportante,pois
cadaumadelaspossuiabordagensmaisadequadaspararesolveromesmoproblema,
cadaumacomsuascaracterísticas.
Aideiadestecapítulonãoéensinarvocêaescalarumaaplicação,poisissoseria
demandadeapenasumlivro,massimmostraroscaminhos,vantagensedesvan-
tagensdassoluções existentesparavocêmelhoraraperformancedasuaaplicação
Ruby,namaioriadasvezesRailstambém.Proponhoum‘calaboca’aspessoasque
criticamalinguagemRubysemrealmentesaberoquepodemfazerparalidarcom
seusproblemas.
240

## Página 255

CasadoCódigo Capítulo13.Apêndice:Concorrênciaeparalelismo
13.1 Threads
Antesdaversão1.9doRuby,asThr e a d snãoeramnativasdoSistemaOperacional,
ouseja,elaseramgerenciadaspelas V i r t u a lMachine,oquecausavagrandesproble-
mas,jáqueelasnãoseaproveitavamdeváriasvantagensdisponibilizadasautoma-
ticamentepeloS.O(leiamaissobreasgreenthreads:http://en.wikipedia.org/wiki/
Green_threads). Apartirdaversão 1.9,as Thr e a d ssão nativasdoSistemaOpe-
racional,oquepodelevarvocêapensarqueosdesenvolvedoresRubypoderiam
implementarThr e a d sassimcomoosdesenvolvedoresJavafizerampormuitosanos.
Porém,issonão ébemaverdade. AlinguagemRubypossuiummecanismo
de lockchamado Global Interpreter LockcarinhosamenteconhecidocomoGIL.Este
mecanismoevitaqueváriasThr e a d spossamalterarumdadocompartilhadoentre
elas,comissoépraticamenteimpossívelalcançarconcorrênciaemaplicações Ruby.
OutroagravanteéquemuitasbibliotecasRubysãoescritasnalinguagemC,eestas
bibliotecasnãosão Thr e a dSafecomissoseriamuitoperigosoutilizarestasbiblioteca
emumambientemultithreadsemutilizaroGIL.
IssoquedizerquenuncapodereiutilizarThr e a d senquantoutilizarRuby?Não,
mentira.V o c êpodeutilizarThr e a d sdesdequeutilizealguminterpretadorquenão
possuaum Global Interpreter Lock,comooJRuby.Maslembre-se,principalmentese
vocêveiodomundoJava,vocêpodeutilizarThr e a d sutilizandoJRuby,masenfren-
taráosmesmosproblemasenfrentadosquandodesenvolviaemJava:garantirque
seucódigoéthreadsafe,checarquetodasasbibliotecasquevocêutilizasãothread
safetambém,nãofazer deadlockseváriosoutrasdificuldadesencontradasquando
manipulamosThr e a d smanualmente.
13.2 Múltiplosprocessos
EsteédelongeomecanismosmaisutilizadonomundoRubyparaescalarprinci-
palmenteaplicações feitasemRails.Pelosimplesmotivodeserdifíciltrabalharcom
Threads,osdesenvolvedoresRubynamaioriadasvezespreferemapenas startarmais
processos.Oproblemanestecasoéquevocêprecisasepreocuparemsincronizaros
dadosquetransitamentreosprocessos,seránecessárioalgumaferramenta,como
porexemplooDRb(http://segment7.net/projects/ruby/drb)quepermiteacomuni-
caçãoentrediferentesprocessosRuby.
Existeaindaumproblemaemrelaçãoamemóriafísicaqueseráutilizada.Por
exemplo,seumprocessoRubygastar200MBdememória,evocêforkarmais4pro-
cessosidênticosaeste,oespaçoemmemóriaparacadaumseráde200MB,oque
241

## Página 256

13.3.Fibers CasadoCódigo
geraumademandadepelomenos1GBdememóriafísica.Servidoreswebcomoo
Mongrel,funcionamdestamaneira,porissonãodevemserutilizadosemprodução.
ServiçosmaisrobustoscomoPassenger(móduloparaA p a c h eoNgix)eoU n i-
cornimplementaramumasoluçãoumpoucomaiseleganteeeficiente.Eles forkamo
processoatravésdoSistemaOperacionalUnixquecriaumacópiadoprocessoorigi-
nalefazcomqueelescompartilhemamesmamemóriafísica.Asacadaéquequando
umprocessoalteraalgumdadonamemóriaosoutrosprocessosnãosãoafetados.
Destamaneiraépossíveltermoscincoprocessosrodandogastandoapenas200MB
dememóriafísicaeatendendocincovezesmaisrequisições concorrentemente.
Aparteinteressanteéquepodemospararapenasumprocessoporvez,issoé
bomquandodesejamos,porexemplo,fazerdeploydeumaaplicaçãosemquehaja
downtimeparaosusuários.
13.3 Fibers
ApartirdoRuby1.9,épossívelcriarcódigoquesãoexecutadosdeformaconcor-
rente,utilizandoas Fibers,recursomuitoparecidocomasthreads,porém,maissim-
pleseleves.Adiferençaéqueuma Fibernãoégerenciadapelamáquinavirtualou
pelosistemaoperacional,massimpeloprópriodesenvolvedor.
Outradiferençaimportante,éque fiberssãomaisrápidasdeseremcriadasenão
ocupammuitoespaçoemmemória,poisrodamsempredentrodeumaúnicathread.
Justamenteporrodaremapenasumaúnicathreadéquenão sepodeconfiarque
dadoscompartilhadosserão alteradosentrediversas fibers,porissoaimportância
do Global Interpreter Lockparagarantiraintegridadedosdadosnestecenário.
Aperguntaquenosfazemosé:‘Sefibersrodamdentrodeumaúnicathread,
ondeestáograndebenefíciodaconcorrência?’
Arespostaéque fiberssãopartesdeumasoluçãomaisrobusta.Elaspermitem,
porexemplo,queosdesenvolvedoresgerenciemmanualmenteofluxodeconcor-
rênciaqueexecutaráastarefasnecessárias.Porexemplo,suponhaqueseuservidor
webrecebaum r e q u e s tequeexisteumtempo,mesmoquemínimo,paraqueares-
postasejageradaaousuário.Nestemeiotempo,outros r e q u e s t spodemchegarenão
éinteressantequeestesesperemqueoprimeiro r e q u e s tsejaconcluídaparaserem
atendidos.
Aoutilizaruma fi b e rpor r e q u e s t,garantimosqueaoreceberumarequisiçãoo
servidoradeixesoboscuidadosdesuaprópria fi b e r,enquantoissooutrasrequisi-
ções sãoatendidaserepassadasparasuaspróprias fibers. Conformecada fi b e rfor
242

## Página 257

CasadoCódigo Capítulo13.Apêndice:Concorrênciaeparalelismo
concluídaoseuresultadoseráretornandoparaousuário.
Oúnicoproblemadestaabordageméquandoexisteanecessidadedeutilizar
I/Oblocante,porexemplo,acessarumbancodedados,enviaremail,etc. Como
existeumaúnicathread,qualquer fi b e rquepreciseutilizarI/O,irábloqueá-laeassim
perderemososbenefíciosdautilizaçãode fibers.
13.4 O design pattern Reactor
Odesignpattern reactorébemsimples,eleconsisteemdelegarchamadasIOpara
serviçosexternos(reactors)quesuportamrequisições concorrentes.Estes reactors
proveemumamaneiraderegistramos callbacksqueserão disparadosassincrona-
mente,assimqueasrequisições foremcompletadas.
Suponhaquesuaaplicaçãowebprecisaconsultarum web serviceexternoparare-
tornarinformações aousuário.Essarequisiçãopodeserbastantelenta,dependendo
daperformancedeumaaplicativodeterceiros.Utilizando reactor,nósapenasrece-
bemosarequisiçãoedelegamosachamadaao web serviceexternoparaum handler,
edizemosparaesteoquedeveráserfeitoquandoarequisição externaterminar,
ouseja,registramos callbacksqueserãoexecutadosbaseadosnarespostadorecurso
externoemquestão.
Nocasodasuaaplicação rodaremumservidorweb single threadexisteuma
questãoimportante.Quandorecebemoso r e q u e s tedelegamosachamadaao web
serviceparaum handlercontinuamosbloqueandoa threadeevitandooprocessa-
mentodenovasrequisições. Paraevitarqueissoaconteça,oidealéencapsularo
r e q u e s tdentrodeuma fi b e r,efetuaro r e q u e s tao web serviceepausara fi b e rdemodo
queoutrasrequisições possamserprocessadasenquantoaguarda-seachamadaao
web service.Quandoestachamadaforefetuada,a fi b e rénovamenteativadaefinal-
mentearespostaéenviadaaocliente.
EstaéaabordagemutilizadapeloEventMachine(Ruby)epeloNode.js(Javas-
cript).OThi néumdosservidoreswebRubyescritosbaseando-senoEventMachine,
existemtambémváriasbibliotecasbaseadasnoEventMachinequepodemserutili-
zadasdemaneira standaloneparafazerrequisições assíncronas.
Oúnicoproblemadeutilizaropadrão reactoréquebradeparadigmanomo-
mentodeescreverocódigo. Sevocênão tomarocuidadonecessário,podeaca-
barcomumagrandequantidadede callbacksaninhados,problematambémen-
frentadoquandoutilizamosNode.js.RecomendoquevocêleiaoartigodoMartyn
Loughran,umdoscriadoresdoPusher:http://rubylearning.com/blog/2010/10/01/
243

## Página 258

13.5.Conclusão CasadoCódigo
an-introduction-to-eventmachine-and-how-to-avoid-callback-spaghetti.Nestear-
tigoeleexplicacomoevitar callbacksmacarrônicos quandoutilizamosEventMa-
chine.
13.5 Conclusão
AconclusãoqueparticularmentechegoéqueconcorrênciaemRubyéalgopossível
epodeserfeitodemuitasmaneiras.Utilizandoos fibersquesurgiramnoRuby1.9,
queemconjuntocomIOnãobloqueante,permitequesejaalcançadoaltosníveisde
concorrência.Existetambémaopçãodeforkarprocessosexistentes,comoéfeitono
passenger,quepodeserutilizadotantocom N g i n xquantocom Apache.
Lembrandoquequandodesenvolvemosaplicações web,questões comocachee
minimizardependênciasexternassempredevemserlevadasemconsideraçãopara
melhoriasnaperformance. Sevocêprecisaescalarumaaplicação webqueutiliza
Ruby,temaobrigação deestudarnão apenasastécnicasdescritasanteriormente,
mastambémestasquestões.
244