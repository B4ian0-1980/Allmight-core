---json
{
  "id": "vire_o_jogo_com_spring_framework",
  "title": "Vire o jogo com Spring Framework",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Vire o jogo com Spring Framework.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "com",
    "framework",
    "java",
    "jogo",
    "linguagens",
    "spring",
    "vire"
  ],
  "perguntas_tipo": [
    "Como utilizar Vire o jogo com Spring Framework?",
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

# Vire o jogo com Spring Framework

> **Arquivo Original:** `Vire o jogo com Spring Framework.pdf`
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
Prefácio
NestelivrotrataremosdoSpring,umframeworkusadonodesenvolvimentodeapli-
caçõescorporativasbaseadonosconceitosde inversão de controle, injeção de depen-
dênciase AOP.Sãopalavrasquemuitasvezessoamalienígenasemuitasvezesnão
adquiremsignificadonamentedodesenvolvedor. Estelivropossuidoisobjetivos:
clarificarosignificadoportrásdestesconceitoseexporcomosuaaplica çãoacabapor
gerarsistemasdequalidadesuperior,maisfáceisdemantereque,comisto,acabam
poraumentarovaloragregadodonossotrabalho.
Maisqueumframeworkparadesenvolvimentodeaplica çõescorporativas,vejo
oSpringcomoumaferramentadisciplinadora.Conformeodesenvolvedorvaiseha-
bituandoaoseumododetrabalhocome çaavalorizaraindamaisqualidadescomo
umamelhormodulariza çãodosistema,escritadecódigomaissimples,reaprovei-
tamentodecódigolegadoetecnologiasjáexistentes,alémdacria çãodeinterfaces
maissignificativas.NoSpringpodemosverdeformanítidaonúcleodaarquitetura
desistemasqueéjustamenteomodocomocomponentesdesoftwareinteragemen-
tresideumamaneiraexplícita.Paraosqueanseiamtrilharestecaminho,étambém
umauxílioemsuaforma ção.
Olivroédivididoemduaspartes.Naprimeiratratamosdosconceitosemque
sebaseiaoSpring.Veremosoquemotivousuacria ção,oqueoframeworktrouxe
deganhoparaodesenvolvimentodeaplica çõescorporativasecomosãoaplicados
nonúcleodoSpringqueéseucontainerdeinversãodecontrole/inje çãodedepen-
dências.Comistoéfornecidaaoleitorumabasesólidaquepodeseraplicadatanto
dentroquantoforadocontextodoSpring.
Nasegundapartetemosumaabordagemmais mão na massa.Veremosaplica-
çõesdoframeworkemsitua çõesreaisdodiaadia,comoporexemplonacamada
depersistência,controletransacional,segurançaetambémcriaremosumaaplica ção
webrealbaseadanoSpringMVC.Agrossomodo,pode-sedizerquequandoescrevi
aprimeirapartedolivroincluíoconteúdoquegostariamuitodeteraprendidona
i


## Página 6

CasadoCódigo
faculdade,enquantonasegundaestãoasinforma çõesqueteriammepoupadomuito
temponomeucotidianocomodesenvolvedor.
A quem se destina
Estelivrosedestinaatodosaquelesquejápossuemalgumconhecimentodapla-
taformaJava,quejáterãoumabagagemmaisricaparaentenderoquetentoexplicar
nestetexto.Casonãosejaoseucaso,tudobem:ostrêsprimeiroscapítuloscontém
oconceitualquevocêpoderáaplicarempráticamentequalquerplataforma.
Agradecimentos
Agradeçoàconfian çaeaoapoio(istosemmencionarapaciência!) dosmeus
editoresPauloSilveiraeAdrianoAlmeidasemosquaisestelivronãoseriapossí-
vel.Claroqueelesnãoagiramsozinhos,Nanna-minhaesposa-éfundamentalpor
terconseguidomeaguentarnesteprocessodetradu çãodo Springolêsparao Portu-
guês.Tambémprecisoagradeceraosmeuscolegas,emespecialaoMatheusEduardo
MoreiraeoFelipeZampa.
Osleitorestiveramparticipa çãoextremamenteimportante:apósolan çamento
daversãobetafiqueimaravilhadocomaquantidadedepessoasinteressadasneste
material,oquememotivouaconcluí-lomaisrápidoecomamelhorqualidadepos-
sível. Algunsentraramemcontatodiretocomigocomdicasesugestões,eaestes
ofereçomeuagradecimentoespecial:RenanReis,RodrigoMonteiro,AdrianoFaria
AlveseWillardyTyronedeOliveira.Eei,tambémnãopossodeixardeagradecerao
apoiodoRodrigoFernandesMoreiraeGabrielaCorrêadaEteg. Finalmente,para
evitarqueeusofraconsequênciasimprevisíveis,àminhamãe,SelmaWeissmann.
Infelizmenteoespa çodesteprefácioélimitadoparacontertodasaspessoasaquem
devoagradecer,assimcomominhamemória. Casoseunomemetenhaescapado,
porfavordesculpeestemalagradecido:comcertezaencontrareialgumaformade
retribuí-lonofuturook?
Muitoobrigadoatodosvocês.
ii


## Página 7

CasadoCódigo Sumário
Sumário
Os conceitos por trás do Spring 1
1 Lide com o alto acoplamento de forma elegante 3
1.1 Problemaessencial:acoplamento . . . . . . . . . . . . . . . . . . . . . 4
1.2 Afamigeradainversão . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2 Conhe ça o Spring Framework 15
2.1 PorquecriaramoSpring? . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.2 OMundodosobjetosem2004 . . . . . . . . . . . . . . . . . . . . . . 16
2.3 OsproblemasdoEJBem2004. . . . . . . . . . . . . . . . . . . . . . . 18
2.4 Alternativascome çamasurgir:IoC/DIeAOP . . . . . . . . . . . . . 19
2.5 Container:osujeitoquetornatudoistopossível . . . . . . . . . . . . 22
2.6 Doinícioaofimdeumobjeto,entendaociclodevida . . . . . . . . . 22
2.7 Springempartes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.8 OContainer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.9 TrabalhandocomAOPeAspects . . . . . . . . . . . . . . . . . . . . . 29
2.10 Instrumentaçãodecódigo . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.11 Acessoadadoseintegra ção . . . . . . . . . . . . . . . . . . . . . . . . 30
2.12 AplicaçõesnaWebcomoSpring . . . . . . . . . . . . . . . . . . . . . 30
2.13 Eaindamaiscomponentes!. . . . . . . . . . . . . . . . . . . . . . . . . 31
2.14 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3 Conhecendo o Container 33
3.1 Preparandoseuambientededesenvolvimento. . . . . . . . . . . . . . 34
3.2 Nossosistemadeexemplo . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.3 Declarandobeans . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
iii


## Página 8

Sumário CasadoCódigo
3.4 Instanciaçãoporfactorymethod . . . . . . . . . . . . . . . . . . . . . 43
3.5 Mapeandoatributoscomplexos . . . . . . . . . . . . . . . . . . . . . . 46
3.6 Usandoocontainer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
3.7 Ociclodevidadocontainer . . . . . . . . . . . . . . . . . . . . . . . . 52
3.8 Escopos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
3.9 Instanciaçãotardia. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
3.10 Aproveitandoociclodevidadosbeans. . . . . . . . . . . . . . . . . . 58
3.11 Quandoobeanconheceseucontainer . . . . . . . . . . . . . . . . . . 61
3.12 Modularizandoaconfiguração. . . . . . . . . . . . . . . . . . . . . . . 63
3.13 Aplicandoherançanadefini çãodosbeans . . . . . . . . . . . . . . . . 64
3.14 SpringExpressionLanguage(SpEL). . . . . . . . . . . . . . . . . . . . 65
3.15 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
4 Minimizando o XML com autowiring, anota ções e Java 71
4.1 Autowiring:automatizandoainje çãodedependências. . . . . . . . . 71
4.2 Vantagenselimita çõesdainje çãoautomática . . . . . . . . . . . . . . 76
4.3 FacilitandoaindamaiscomAnota ções . . . . . . . . . . . . . . . . . . 77
4.4 ConfiguraçãoprogramáticacomJava . . . . . . . . . . . . . . . . . . . 86
4.5 XML,anota çõesouconfigura çãoprogramática? . . . . . . . . . . . . 93
5 AOP: adicionando novos comportamentos aos beans 95
5.1 Comoidentificarosinteressestransversais. . . . . . . . . . . . . . . . 96
5.2 EntendendoAOP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
5.3 Preparandooambientededesenvolvimento . . . . . . . . . . . . . . .100
5.4 Aimplementa çãodoprimeiroaspecto . . . . . . . . . . . . . . . . . . 102
5.5 Entendaosadvices. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
5.6 Useosaroundadvices. . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
5.7 Useoadvicebefore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
5.8 EondeentraoProxynessahistória? . . . . . . . . . . . . . . . . . . . 108
5.9 Entendaaexecu ção . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
5.10 UmusointeressanteparaAOP:Logdeerros. . . . . . . . . . . . . . . 111
5.11 Declareaspectoscomanota çõesAspectJeesquemasXML . . . . . . 112
5.12 AsintaxeAspectJdedeclara çãodepointcuts . . . . . . . . . . . . . . 116
5.13 Concluindocomumresumãoconceitual. . . . . . . . . . . . . . . . . 121
iv


## Página 9

CasadoCódigo Sumário
Spring Framework na prática 123
6 Colocando a mão na massa 125
6.1 Obtendoocódigofonte. . . . . . . . . . . . . . . . . . . . . . . . . . . 126
6.2 Configureseuambientededesenvolvimento. . . . . . . . . . . . . . . 127
6.3 Oquevêmporai. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
7 Acesso a dados 131
7.1 DAO:nocentrodamentalidadeSpring. . . . . . . . . . . . . . . . . . 132
7.2 Conecte-seaobancodedados . . . . . . . . . . . . . . . . . . . . . . . 133
7.3 DevoltaaoDAO:oproblemacomasexce ções . . . . . . . . . . . . . 138
7.4 Templates:acabecomocódigorepetido . . . . . . . . . . . . . . . . . 140
7.5 OtrabalhocomJDBC. . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
7.6 OtrabalhocomoHibernate . . . . . . . . . . . . . . . . . . . . . . . . 152
7.7 IntegrecomaJPA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
7.8 Concluindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
8 Desenvolva aplica ções web com Spring MVC 165
8.1 Oqueiremosdesenvolver . . . . . . . . . . . . . . . . . . . . . . . . . 166
8.2 Abaseparatudo:MVC. . . . . . . . . . . . . . . . . . . . . . . . . . . 167
8.3 IniciandooProjeto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
8.4 DispatcherServlet:omaestroportrásdoSpringMVC. . . . . . . . . 171
8.5 OlámundocomSpringMVC . . . . . . . . . . . . . . . . . . . . . . . 174
8.6 OprimeirocontroladorútildoSpringFórum . . . . . . . . . . . . . . 177
8.7 Autenticandousuários:comoredirecionarelidarcomasessãoHTTP180
8.8 DefinindoqualmétodoHTTPusar . . . . . . . . . . . . . . . . . . . . 181
8.9 Recebendoparâmetrosdeentrada. . . . . . . . . . . . . . . . . . . . . 182
8.10 Oqueéaquele“redirect:/”retornadopelaactionlogin? . . . . . . . . 183
8.11 ComolidarcomasessãodousuárioeaclasseModelAndView . . . . 183
8.12 Cadastrandousuários:submissãodeformulários . . . . . . . . . . . . 185
8.13 Submetendooformuláriodecadastro . . . . . . . . . . . . . . . . . . 189
8.14 Melhorandoacamadadevisualiza çãocomoTiles . . . . . . . . . . . 190
8.15 Lidandocomconteúdoestático . . . . . . . . . . . . . . . . . . . . . . 197
8.16 AindahámaisdeSpringMVCporvir. . . . . . . . . . . . . . . . . . . 199
v


## Página 10

Sumário CasadoCódigo
9 A ções recorrentes com o SpringMVC 201
9.1 Façaavalida çãodeformulárioscomoHibernateValidator . . . . . .202
9.2 Envieseusavataresparaoservidorcomuploaddearquivos. . . . . .206
9.3 Definaocorpodaresposta . . . . . . . . . . . . . . . . . . . . . . . . . 210
9.4 FaçarequisiçõesassíncronascomAJAX . . . . . . . . . . . . . . . . . 211
9.5 Concluindocomumasurpresa . . . . . . . . . . . . . . . . . . . . . . 214
10 Gerenciando transa ções 217
10.1 Entendendoastransações . . . . . . . . . . . . . . . . . . . . . . . . . 217
10.2 Aspolíticastransacionais . . . . . . . . . . . . . . . . . . . . . . . . . . 219
10.3 Preparandooambientededesenvolvimento . . . . . . . . . . . . . . . 223
10.4 ComooSpringimplementaosuporteatransa ções . . . . . . . . . . . 223
10.5 Transaçõesprogramáticas . . . . . . . . . . . . . . . . . . . . . . . . . 225
10.6 Declarandotransações . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
10.7 Concluindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
11 Protegendo nossa aplica ção com Spring Security 231
11.1 Entendendoautenticaçãoeautoriza ção. . . . . . . . . . . . . . . . . . 232
11.2 OsmódulosdoSpringSecurity . . . . . . . . . . . . . . . . . . . . . . 233
11.3 Configurandoosfiltrosdeacesso . . . . . . . . . . . . . . . . . . . . . 235
11.4 ConfigurandoocontextodoSpring. . . . . . . . . . . . . . . . . . . . 237
11.5 Oformuláriodelogin . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
11.6 Escrevendoumprovedordeautentica ção . . . . . . . . . . . . . . . . 243
11.7 UsandoSpEL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .246
11.8 Protegendoinvocaçãodemétodosembeans. . . . . . . . . . . . . . .248
11.9 Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .248
11.10 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .249
12 E ai, gostou? 251
Bibliografia 256
Versão:16.2.5
vi


## Página 11

Parte I
Os conceitos por trás do Spring


## Página 13

Capítulo1
Lidecomoaltoacoplamentode
formaelegante
T odo objeto é carente: e aí o problema começa.
SpringFrameworkéumframeworkvoltadoparaodesenvolvimentodeapli-
caçõescorporativasparaaplataformaJava,baseadonosconceitosdeinversãode
controleeinje çãodedependências.Estaéadescri çãopadrãoqueencontramosna
grandemaioriadosmateriaissobreoassunto.
Vamosfazerdiferente?Quetalnãosimplesmentedescreverofuncionamentoda
ferramenta,massimapresentarosproblemasquemotivaramasuacria ção?Sãopro-
blemascomunsnodesenvolvimentodesistemasqueocorremindependentemente
daplataformaeoSpringnofinaldascontaséapenasumaferramentainteressante
paratratá-los.
Estasdificuldadespodemseragrupadasemduascategorias: essenciaise especí-
ficos da plataforma. Nestecapítulooobjetivoéapresentá-lasbrevementepara,no
transcorrerdestelivro,entendercomooSpringnosajudaaminimizá-las.


## Página 14

1.1. Problemaessencial:acoplamento CasadoCódigo
1.1 P roblema essencial: acoplamento
Problemasessenciaissãoaquelesqueindependemdaplataforma. FredBrooksno
seutextoclássico“NoSilverBullet”[2]apontaquatrodificuldades essenciaisine-
rentesaodesenvolvimentodequalquersoftware:
•Conformidade:todosoftwareprecisasercompatívelcomoambientenoqual
seráexecutado. Istoincluiconformidadecomsistemaoperacional,acessoa
interfacesdesistemaslegadoseasprópriasrestri çõesfísicasdoambiente.
•Invisibilidade:comopodemosvisualizarumsoftware? Apesardosavan ços
emnotaçõescomoaUMLaindanãochegamosaumasolu çãodefinitivapara
esteproblema.Boapartedonossoraciocíniosebaseiaemmetáforasvisuais
quedificilmenteseenquadramnodesenvolvimentodeprojetosdesoftware.
•Mutabilidade: osrequisitosmudamconstantementee,comisto,faz-sene-
cessárioqueaarquiteturadenossossistemassejaprojetadadetalformaque
possaseadequarcomomínimodeimpactopossívelaestastransforma ções.
•Complexidade:provavelmenteapiordasdificuldades,poisestádiretamente
relacionadaaoslimitesdonossointelecto.Conformeosoftwaresedesenvolve
acomplexidadedasregrasdenegócioedasintegra çõesqueesteprecisafazer
evoluematéchegaraumpontonoqualoscustosdemanuten çãosetornam
proibitivos(olivroclássicodeFredBrooks,“TheMythicalMan-Month”[1]
podeserresumidoaestaquestão).
Aorientaçãoaobjetosquandobemaplicadaconsegueminimizarestesproble-
masessenciaisatravésdametáforadoobjeto.Éumaideiasimples:sevivemosem
ummundorodeadodeobjetosinteragindoentresi,porquenãometaforizá-losem
umalinguagemdeprograma çãoquenospermita simularestasinteraçõesafimde
resolverproblemascomputacionais?Umplanoperfeitonoqualnadapodedarer-
rado,nãoé?Claroquenão.
Minimizamosoproblemadaconformidadeapartirdeinterfacesbemdefinidas,
comrelaçãoàinvisibilidade,temosaUML,eaprópriametáforadoobjetojáé quase
visual. Mutabilidade? Semprepodemosadicionarmaisumaclassepramodificar
algumcomportamento,ecomrela çãoàcomplexidade,bem,agoratemosclassese
ascoisasficarammaissimples,certo?Não.
Seignoramosofatodequeesterelacionamentoentreobjetosnãoésimples,ter-
minamosrefénsdeuma armadilha complexadaqualpossivelmenteaúnicasaída
4


## Página 15

CasadoCódigo Capítulo1. Lidecomoaltoacoplamentodeformaelegante
normalmenteéareescritatotaldonossocódigo. Sejáhácomplexidadenode-
senvolvimentoprocedural,comobjetosemcenaacabamosporadicionartambém
acomplexidadeinerentedogerenciamentodesuasintera ções.Nosso plano perfeito
falhou,eRobertC.Martin(aka“UncleBob”)emseutexto“TheDependencyInver-
sionPrinciple”[10]apontaalgunssintomasdequenossoprojetopodeestarapodre-
cendo.Estessão:
•Fragilidade:altereumtrecho,vejadiversosoutrossepartirem.
•Rigidez:consequênciadafragilidade,osoftwareédifícildesermodificado.
Nestecaso,tantodevidoàsuafragilidadequantoporrazõesnãotécnicas.A
própriagerênciadaempresacome çaabarrarmudan çasnosistemaporestar
traumatizadaporumpassadodolorosodebugsquesurgemdasolu çãode
outros.
•Imobilidade:hácomponentesmaravilhososnosoftware,quepoderiamser
aproveitadosemoutrosprojetos.Infelizmente,suaremo çãoétãocustosaque
ficamaisbaratosimplesmentereimplementarafuncionalidade(istosemmen-
cionarqueagoravocêtemdedarmanuten çãoemmaisdeumlugar)
Oquetornaumprojetofrágil,rígidoeimóveléamaneiracomoseencontra
definidaainterdependênciaentreseuscomponentes[10].Asolu çãoparaevitares-
tessintomasédesenharmosnossosoftwaredetalformaqueconsigamosgerenciar
demaneiraefetivaomodocomoseusobjetosserelacionam.Dizemosqueumsis-
temapossui alto acoplamentoquandosuasclassesdependemmuitoumasdasou-
tras.Quantomaisumaclassesabearespeitodeoutra,maioréoacoplamentoentre
asduase,consequentemente,altera çõesemumanormalmenteacarretamemmu-
dançasdecomportamentoemlocaisinesperadosdosistema.
Paraexporoproblema,vouiniciarcomumexemplobastantesimples:umain-
tegração.Nossointegradorécompostoporbasicamentetrêsclasses:um DAOque
buscainformaçõesapartirdedocumentosnoformatoXML,o Integradoremsi,
quepossuialgoritmosfantásticosdeotimiza ção(oqueotornaumcandidatopara
reutilização)eumbancodedadosrelacional,queéodestinodasinforma çõesque
extraímosdonosso DAO(nesteexemploiremosignorarclassesdedomínioafimde
manterasimplicidade).
5


## Página 16

1.1. Problemaessencial:acoplamento CasadoCódigo
O que é um DAO?
DAOsignifica Data Access Object.Éumaestratégiadeimplementa-
çãoquetemcomoobjetivosepararalógicadeacessoadadosdasregras
denegóciodesuaaplica ção.Eisaideia:escrevaocódigodeacessoada-
dosemumaclasseseparadaqueimplementeumainterface. Fa çacom
queorestodoseusistematenhaacessodiretoapenasaestainterface.
Precisoutrocarafontededados? Crieumanovaimplementa çãodesta
interfaceepronto:nãoprecisamaisalterarsuaclassecliente.
Comoseusistemasaberáqualimplementa çãousar?Éoassuntodeste
livro!
Figura1.1:Aprimeiraversãodenossointegrador
UmtermomuitocomumquandofalamossobreoSpringFrameworké depen-
dência. Nosso Integradorpossuiduas,quesãoasclasses DAO XML e Banco
de Dados,ouseja,paraquenossointegradorexista,estasduasclasses obrigatori-
amenteprecisamestarpresentes.
Emumprimeiromomentonossosistemapareceperfeito. Oquepoderiadar
errado?Nada,anãosertrêsdasquatrodificuldadesexpostasporFredBrooks:
•Conformidade:tantoaclassedeacessoabancodedadosquantonossoDAO
queacessadocumentosXMLprecisamestardeacordocomaslimita çõesim-
postasrespectivamentepelosistemagerenciadordebancodedadosepelas
6


## Página 17

CasadoCódigo Capítulo1. Lidecomoaltoacoplamentodeformaelegante
restriçõesdeesquemaXMLedosistemadearquivos.Istojáeraesperado,o
problemaéqueaclasse Integradorpossuiacessodiretoaosdetalhesdeimple-
mentaçãodesuasdependências.
•Mutabilidade:esenofuturohouveranecessidadedebuscarmosdadosnão
dearquivosXML,masdeoutrobancodedadosouseodestinonãoformais
umbancodedados,masumwebservice? Aindapior:eseoclientequiser
decidirqualfonteedestinousaremtempodeexecu ção?
•Complexidade:o Integradoralémdelidarcomasespecificidadesdoseu
maravilhosoalgoritmodeprocessamentodedadostambémprecisalidarcom
asidiossincrasiasdasfontesdeorigemedestinodosdados.
Aclasse Integradorpossuialtoníveldeacoplamentoemrela çãoaosdetalhes
deimplementaçãotantodaorigemquantododestinodosdados. Qualquermu-
dançaemumadasdependênciasde Integradoreseufuncionamentopodeser
comprometido. Aqualidadedeumsoftwareéinversamenteproporcionalaograu
deacoplamentodeseuscomponentes.
Aindahátempodesalvarestesistema.Oqueprecisamosfazeréincluir abstra-
ções.Oquevêmaserumaabstra ção?Éoresultadodoprocessonoqual,apartirda
análisedosdiversosusosdeumacategoriadeobjetos,come çamosaobservarcom-
portamentosquesempreestãopresentes.PodemospensareminterfacesJavaeclas-
sesabstratascomoabstra ções,poisestasentidadescontémcomportamentos(leia-se
métodos)queserãocomunsatodasasclassesqueasimplementem/realizem.
Vamosclarearoconceitodeabstra ção,observandoasegundaversãodonosso
sistemadeintegra çãofacilite:
7


## Página 18

1.1. Problemaessencial:acoplamento CasadoCódigo
Figura1.2:Asegundaversãodenossointegrador
Asinterfaces Origeme Destinosãoabstrações.Aclasse Integradornãoprecisa
conhecerdetalhessobreparseamentodearquivosXMLouarespeitodetransa ções
embancosdedados. Sóprecisasaberqueexisteumafun çãoquelheretornauma
listaderegistrosapartirdeumaorigemedeummétodoquepossaserusadopara
persistiroresultadodoseuprocessamento.Reparequefizemosumaabstra çãoaqui
aoidentificarmosapenasocomportamentoestritamentenecessárioparaqueuma
origemsejauma origemeumdestinoum destino.Comoresultado,reduzimossig-
nificativamenteoacoplamentoemnossosistema,vistoqueagorao Integrador
sótemacessoaoque de fatolheinteressa.
Vocêpodeseperguntarnestemomento: "como a complexidade do meu sis-
tema foi reduzida se na prática acabaram de ser introduzidos dois elementos a mais
no design original?”. Bem, primeirooencapsulamentoestámaior, poisaclasse
Integradornãopossuimaisconhecimentoarespeitodedetalhesdeimplementa-
çãotantodaorigemquantododestinodosdados.Segundo,comoo Integrador
nãosabecomqualfonte/destinodedadosestálidando, qualquerclassequeimple-
menteasinterfaces Origemou Destinopodeserusadaeporúltimo,amudan ça
decomportamentoemtempodeexecu ção,ondenaprimeiraversãodosistema,caso
fossenecessárioincluirumanovafontededados,eranecessáriorecompilarnosso
código.Agoranãomais,bastaquenosso Integradordecidaqualimplementa ção
8


## Página 19

CasadoCódigo Capítulo1. Lidecomoaltoacoplamentodeformaelegante
desejausar.
Narealidade,nossosistemaadquiriuumaflexibilidadeatéentãoinexistente.
Qualquerumpodeimplementartantoumafontequantoumaorigemdedadospara
osistema.Naimagemabaixopodemosterumano çãodestaflexibilidade.
Figura1.3:Possibilidadesinfinitasparanossosistema
Oquefizemosfoinarealidadeaplicaro“PrincípiodaInversãodeDependên-
cias”[10],ondeMódulos de alto nível não devem depender de módulos de baixo
nível, apenas devem depender de abstra ções e Abstrações não devem depender
de detalhes e sim detalhes devem depender de abstra ções.
Módulosdealtonívelsãoaquelesqueimplementamoquerealmenteinteressa
emnossoprojeto,ouseja,alógicadenegócio.Emnossoexemplo,estecorrespondeà
classe Integrador.Asclassesqueimplementamasinterfaces Origeme Destino
sãodenívelmaisbaixo,poisnãoestãodiretamenterelacionadasaoobjetivodanossa
aplicação,operandonapráticaafun çãodesuporteàclasseprincipal.
Aomesmotempo,vemosnasfiguras1.2e1.3queasduaspartesdaregraseapli-
cam:tantoo Integradorcomonossasfontesdedadosdependemapenasdenossas
abstrações.Enossasabstra ções,dependemdequem?Apenasdesimesmas.
Estáresolvidooproblemadoaltoacoplamentodopontodevistaestático. A
questãoquesobranestemomentoé:edopontodevistadinâmico,istoé,comoé
feitaainstancia çãodenossasclassesecomoestasserãorepassadasàclassecliente?
9


## Página 20

1.2. Afamigeradainversão CasadoCódigo
1.2 A famigerada inversão
“InversãodeControle”,“PrincípiodaInversãodeDependências”,queinversãoéesta?
Éaaplica çãodo princípio de Hollywood,cujonomeébaseadoemumclichêco-
mumnaquelacidade.Quandoatoresconcorremporumpapel,osprodutoresres-
ponsáveispelapeça/filmecostumamdizeraosparticipantesdoprocessoseletivo:
“nãonoschame,deixequenóschamamosvocê”. Assimosprodutoresevitamter
suaslinhastelefônicasinutilizadasporatoresansiososporumaresposta.
Todoframeworkénarealidadearealiza çãoda inversão de controle. Penseem
umservlet:vocênãoprecisasepreocuparemimplementarumloopquefiqueverifi-
candoatodomomentoachegadadeumsinaldeumaporta.Tudooquevocêprecisa
fazeréimplementarummétodode callbackqueseráexecutadosemprequeaporta
forativada. Omesmoprincípioéaplicadonacria çãodeumainterfacegráficaem
Swing:odesenvolvedornãoprecisaficarverificandoatodomomentoseousuário
clicouemumbotão:bastaquevocêimplementeasa çõesaseremexecutadasquando
alguémopressionar.
Quandoaplicamosoconceitodeinversãodecontrole, estamosnarealidade
transferindoaresponsabilidadedeverificaraocorrênciadeeventosnosistemapara
umsistemamaior,implementadoporalguémquemuitoprovavelmenteentendeeste
domínioestruturalmuitomelhorqueeuouvocê.Ecomistoescrevemosmenoscó-
digo,poisnoslivramosdestefardo,passandoa,emteoria,nospreocuparmosapenas
comoquerealmentenosinteressaqueéalógicadenegócio.
Porémotermo inversão de controle,quandoaplicadoaonossocasoqueéo
Springnãoéumaboaalternativapois,comofoiobservadonosexemplosacima,
qualquerframeworkimplementaestepadrão. Sendoassim,adescri çãoqueexpus
noprimeiroparágrafosemostracompletamentevazia:“(...)frameworkbaseadonos
conceitosdeinversãodecontrole/inje çãodedependências(...)”.Quemapontaeste
erroconceitualfoiMartinFowlernoseutexto Inversion of Control Containers and
the Dependency Injection Pattern[5].
Setodoframeworkéaaplica çãodainversãodecontrole,dizerqueoSpringse
baseianesteprincípioéumpleonasmo.Umadescri çãomelhorseriaportantoade
queéumframeworkbaseadonoconceitode injeção de dependências,queéuma
especializaçãodainversãodecontrole. Pronto: agoratemosumadescri çãomais
interessante.Nainje çãodedependências,nãoéaclasseclientearesponsávelporde-
finirquaisserãosuasdependências.Estaresponsabilidadeédelegadaaum container
de injeção de dependências.
10


## Página 21

CasadoCódigo Capítulo1. Lidecomoaltoacoplamentodeformaelegante
Paraentendermelhoroquevêmaserumcontainer,vamospartirparaaquarta
versãodonossosistema,quepodeservistanafigura1.4:
Figura1.4:Aquartaversãodenossointegrador
Nestanossanovaevolu ção,foiincluídoumnovoelementoemnossosistema:
o Service locator. Estaclasseimplementaumpadrãodeprojetodomesmo
nome,cujafun çãoélocalizarinstânciasdeclassesqueimplementemdeterminados
serviços(leiainterfacesouclassesabstratas).Nestanovaroupagemdonossosistema,
aclasse Integradordelegariaao Service Locator afunçãodeencontraraim-
plementaçãocorretadosservi çosdeEntradaeSaídadedados.Podemosimaginar
quenossoprojetopossuaumarquivodeconfigura çãoqueélidoemsuainicializa-
ção,eseriaoresponsávelporefetuarasbuscasnecessárias,talcomoexemplificado
abaixo:
public class Integrador {
11


## Página 22

1.2. Afamigeradainversão CasadoCódigo
public Integrador() throws Exception {
Properties configuracao = new Properties();
InputStream stream =
new FileInputStream("configuracao.properties");
configuracao.load(stream);
String nomeOrigem = configuracao.getProperty("nome_origem");
String nomeDestino = configuracao.getProperty("nome_destino");
ServiceLocator locator = new ServiceLocator()
setOrigem(locator.getOrigem(nomeOrigem);
setDestino(locator.getDestino(nomeDestino);
}
// demais métodos
}
Nãoprecisamosnospreocuparcomcomoo Service locator encontraes-
tasinstâncias. Elesimplesmenteasencontra. Háainversãodecontroleparcial
aqui. Nossaclasseclientedelegaatarefadeinstancia çãoparaoutrocomponente,
masaindaparticipaativamentenainje ção.Noentanto,aindatemosalgunsproble-
mas:nossaclasse Integradorestáacopladaaumanovaentidade:o Service
Locatorqueapesardenosfornecerasinstânciascorretasdenossasdependências,
ainjeção ainda éfeitapelaclassecliente.Temosportantoumainversãodecontrole
bemmeiaboca.
Oidealseriaquenossaclasse Integradornãopossuíssenenhumadependên-
ciaalémde Origeme Destino.Saio Service Locator,entraocontainerde
injeçãodedependências.
Todocontainerdeinje çãodedependênciasapresentabasicamenteomesmo
comportamento:apartirdeconfigura çõesquepodemestarnaformadedocumen-
tosXML,anota çõesJavaoumesmocódigoexecutável,esteseencarregadeinstanciar
corretamenteasclassesquedefinimosnestasconfigura çõeseapartirdestas,fazer
todoocontroledeciclodevidaeinje çãodedependências.
Simplificandoaomáximo,oSpringéumcompetentecontainerdeinje çãode
dependênciasemcimadoqualforamconstruídosdiversosmóduloscomoobjetivo
defacilitarodesenvolvimentodeaplica çõescorporativas.Notranscorrerdestelivro
vamosaprendercomdetalhesoseufuncionamento.
Enomeiodeste,quandoacharqueainje çãodedependênciasresolveutodosos
seusproblemas,ireilhemostrarqueistoéapenasparcialmenteverdade. Atalda
12


## Página 23

CasadoCódigo Capítulo1. Lidecomoaltoacoplamentodeformaelegante
programaçãoorientadaaaspectosresolveboapartedosproblemasrestantesdecor-
rentesdoaltoacoplamento.Esperoquegoste.
13


## Página 25

Capítulo2
ConheçaoSpringFramework
Aonde os objetos se encontram.
Agoraquesabemosquaisosnossosproblemasessenciais(acredite,osmaisdi-
fíceis)chegouohoradeconhecermosoferramentalqueiráminimizá-loseneste
processo,serapresentadosaumasériededificuldadesespecíficasdaplataformaJava
(SEeEE)queoSpringFrameworkajudaaresolver.
VamosfalarmaisagorasobreoSpring. Esteéumcapítulofundamentalpara
quemnuncatrabalhoucomoframework.Veremosumasériedeconceitosimpor-
tantesparaobomusodaferramentacomoporexemplobeans,containers,ciclode
vidaemuitosoutros.CasojápossuaoconhecimentobásicoarespeitodoSpringe
dosproblemasquetratareiaqui,sugiroquepuleparaopróximocapítulo.
2.1 P or que criaram o Spring?
OsgermesportrásdoSpringaparecempelaprimeiravezem2002comapublica ção
dolivro Expert One-T o-One J2EE Design and Development[7]deRodJohnson. É


## Página 26

2.2. OMundodosobjetosem2004 CasadoCódigo
ummarconahistóriadodesenvolvimentodeaplica çõescorporativasbaseadasna
plataformaJavaEEporapresentarumacríticabastanteconvincenteaopadrãode
desenvolvimentoempurradopelaSunMicrosystemsparaimplementa çãodelógica
denegócios:osEJBs( Enterprise JavaBeans).
TalcomoapresentadoporRodJohnson,EJBéumaexcelenteop çãoparadesen-
volvimentodeaplicaçõesdistribuídas,oquenãonecessariamenteimplicanamelhor
soluçãoaseradotadaparatodososcasos,principalmentequandoobjetosdistribuí-
dosnãosãoumanecessidade.Esteéoargumentobásicoportrásdolivro.
Em2003éiniciadoodesenvolvimentodoSpringFramework,porémelesófoi
apresentadooficialmentecomoversãofinalaopúblicoem2004comolivro Expert
One-T o-One J2EE Development Without EJB[8].Paramelhorentenderasrazõesque
motivaramacria çãodoSpringéinteressantevoltarmospara2004quandoestefoi
introduzido.
2.2 O M undo dos objetos em 2004
AplataformaJavaEEerabastantediferentedaqueencontramosem2012.Paraco-
meçar,estaeraconhecidacomoJ2EE(Java2EnterpriseEdition)eomodelodede-
senvolvimentoparaobjetosdenegócioincentivadopelaSuneraoEJB,cujaversão
atualeraa2.1,lan çadaemnovembrodoanoanterior.
OsegundolivrodeRodJohnsonélan çadoemjunhode2004. Dadoanovi-
dadedaespecifica ção2.1doEJB,aversãodominantedaplataformaaindaeraa2.0,
publicadaemagostode2001.
Aversão5dalinguagemJavasóserialan çadaoficialmenteemsetembrode2004.
Nãopodíamoscontarcomrecursostidoscomobásicoshojecomoporexemploano-
tações,generics,autoboxingemuitosoutros.Curiosamente,estasfuncionalidades
jáexistiamnalinguagemC #daplataforma.net,aqualRodJohnsonconheciaaal-
gumtempoequemencionacomoferramentaspoderosasparadesenvolvimentoem
seusegundolivro[8].
OEJBseencontrava(eaindaseencontra)nocentrodaespecifica çãoJavaEE.
Aideiaérealmentelinda: desenvolvercomponentesqueencapsulemasregrasde
negócioemumaplataformaquefaciliteaimplementa çãodeaplica çõesdistribuídas
dealtodesempenhoeescalabilidade.
BastariaaodesenvolvedorimplementaroquerealmenteinteressavanaqueleEJB
eesteseriagerenciadopeloservidordeaplica çõesqueofereceriatodaainfraes-
truturanecessáriaparaaexecu çãodestecomponente,comoporexemplocontrole
16


## Página 27

CasadoCódigo Capítulo2. ConheçaoSpringFramework
transacionaldeclarativo,umaplataformadepersistênciadedados,porexemplo,o
JDO,aprimeiraversãodos Entity Beans),poolingdethreads,sistemademensageria
emuitosoutrosrecursospoderosos.
OutrapromessadoEJBéquesurgiriaummercadosódecomponentesterceiriza-
dosvistoqueemteoria,umEJBquefosseimplementadoseguindoasespecifica ções
daSunpoderiaserexecutadosemproblemasemqualquerservidordeaplica ções.
Afinaldecontas,éumpadrão,certo?Ummundoteóricoperfeito:odesenvolvedor
sóprecisavasepreocuparemimplementarasualógicadenegócioeseconseguisse
criaralgoquefossereaproveitávelemoutrossistemas,poderiainclusiveficarrico
vendendoseusEJBs!Nadapoderiadarerrado!
Sóhaviaumpequenoproblema: o tempo gasto com requisitos não funcionais
muitas vezes era maior que com os funcionais.Comonãohaviamaindaanota ções,
odesenvolvedoraoimplementarseusEJBsprecisavasatisfazerumasériedeinterfa-
ceseaindagastavaumbomtempoescrevendoarquivosdeconfigura çãonoformato
XML,comoofamigerado ejb-jar.xml.Omaisinteressanteéquedasinterfaces
aseremimplementadas,namaiorpartedasvezespouquíssimosmétodoseramde
fatoúteis:amaiorparteseencontravaaliapenasocupandoespa ço.
Parapioraraindamaisasitua ção,aportabilidadeentreservidoreseranaprá-
ticaummitoeotalmercadomaravilhosoquesurgiriaporcausadaquelaplataforma
nuncaseconcretizou.Osurgimentodesolu çõescomooXDoclet,EJB-Genediver-
sasferramentasdesenvolvidasespecificamenteparaumououtroservidordeaplica-
ções(equenapráticaeramapenasgeradoresdecódigo)eramumsintomaclarode
quehaviaalgomuitoerradocomaplataformaJ2EE.
Sim, oEJBeramaravilhosoparaaconstru çãodeaplica çõescorporativas de
grande porte,quenecessitavamrealmentedeobjetosdistribuídos,clusteriza çãomas-
sivaetodaaparafernáliaquesóédefatoútilparaamenorpartedosprojetosdeTI.
Nestecontextoamaiorpartedosdesenvolvedoresseviademãosatadas,tendode
sacrificarsuaprodutividadeemproldeumasériedetecnologiasque,naprática,
raramenteusava.
Pior: amaioriadosdesenvolvedoressequersabiapraqueserviamosEJBs. O
maisinteressanteéquenohorizontevíamosaemergênciadaplataforma.netdaMi-
crosoft,quesemostravamuitomaispragmáticaapesardenãoapresentaraaltapor-
tabilidadedoJava.
OpróprioRodJohnsonemseusegundolivro[8]acreditavaqueosEJBsseriam
emumfuturopróximoconsideradostecnologialegada. Comobemsabemos,não
foiistooqueaconteceu.
17


## Página 28

2.3. OsproblemasdoEJBem2004 CasadoCódigo
2.3 O s problemas do EJB em 2004
UmdosprincipaisproblemascomosEJBsnestaépocaéofatodenãopoderemser
executados foradeumservidordeaplica ções. Comaemergênciadodesenvolvi-
mentoorientadoatesteseaconfirma çãodequeestapráticaampliavatantoapro-
dutividadequantoaqualidadedossistemas,aimplementa çãodetestesunitáriose
integradosemEJBssemprerequeriamalabarismosimensosporpartedosdesenvol-
vedores.
Piorqueisto: osservidoresdeaplica çãosempreforampesados(oquesóco-
meçouaserrevertidorecentementeem2011,tendocomomarcoolan çamentodo
JBossAS7),oquetornavaodesenvolvimentoedepura çãodestescomponentesuma
tarefabastanteárduamesmoparaasesta çõesdetrabalhomaispoderosasde2004.
Naprática,comoamaiorpartedosdesenvolvedoresnãoprecisavadeaplica çõesdis-
tribuídas,pouquíssimoseramosquerealmenteentendiamopropósitodeumEJB
real.
Oleitorpodeseperguntarnestemomentoarazãodetantosproblemascomo
EJBnestaépoca.Basicamentefoiomodocomoaespecifica çãofoicriada.Aoinvés
deseroresultadodeumaevolu çãobaseadanaobserva çãodosusosedesusosem
produçãooEJBfoiditadoporumcomitê.
Comitêssãoótimosquandooobjetivoégarantiralongevidadedeumpadrão,
vistoseremnormalmentecompostosporumgrandenúmerodeparticipantes. O
problemaéqueoprodutodesenvolvidonormalmenteécriadoantesquequalquer
umoponhaempráticanomercado,aocontráriodoqueocorreemprojetosde-
senvolvidosporumgrupomenordedesenvolvedoresoucomercial.Pior:comohá
umagamaimensadeinteressesenvolvidos,normalmenteesteprocessoélento,im-
pedindoqueadapta çõessejamfeitasemtempohábilparaqueumatecnologiase
mantenhacompetitiva.
Oquetodosdesejavameraclaro:asvantagensoferecidaspelaplataformaJavaEE
porémcomaprodutividadeeclarezaqueomercadoexigianaquelemomento.Uma
plataformaparaodesenvolvimentodeaplica çõescorporativasquefossepragmática.
AplataformaJ2EEtinhacomoobjetivosresolverdiversosrequisitosquenaprá-
ticaeramapenaspotenciais.Algunsexemplossãoanecessidadedeatenderàmaior
gamapossíveldetiposdeclientesexistentes:entãoodesenvolvedorimplementava
osEJBsparaseremexternalizadosviaRMI,IIOP,etc. Noentanto,nodiaadia,o
maiscomumerahaverapenasumtipodeclientedentrodacorpora ção,muitasve-
zesbaseadoempadrõesbemmaisinteroperantescomooSOAP.
18


## Página 29

CasadoCódigo Capítulo2. ConheçaoSpringFramework
Outroexemploeraomedoreinantenaépocadeque,dodiapranoite,sefizesse
necessáriaatrocadosistemagerenciadordebancodedados. Convenhamos:este
éotipodealtera çãoqueraríssimasvezesumdesenvolvedorsevêobrigadoatratar
dentrodeumacorpora çãooumesmodentrodeumasoftwarehouseresponsável
pelodesenvolvimentodealgumprodutoespecífico.Dadaestaconstantenecessidade
ematendertodasassitua çõespossíveis,odesenvolvedorsevianamaiorpartedas
vezesguiando-senãopelosrequisitosquedeveriamatenderseucliente,massimaos
impostospelatecnologia. Eranítidoquehaviaalgodemuitoerradonoreinoda
Javolândia.
2.4 A lternativ as começam a surgir : IoC/DI e AOP
NestamesmaépocacomeçamasepopularizarentreosdesenvolvedoresJavaoscon-
ceitosdeinversãodecontrole(IoC- Inversion of Control)/InjeçãodeDependências
(DI- Dependency Injection)ePrograma çãoOrientadaaAspectos(AOP- Aspect Ori-
ented Programming).
AsideiasportrásdaIoC/DIforamtratadasnocapítulo1. Comojásabemos,
estastécnicastemcomoobjetivoatacaroproblemadoaltoacoplamentoentreos
componentesdonossosistema.AAOPtemomesmoobjetivo,sóquevaiumpasso
além,aondeaorienta çãoaobjetosnãoconsegueentrarsemcriarmonstrinhos.
Comainje çãodedependênciasconseguimosidentificarosmódulosmaisfa-
cilmentevisíveisdenossosistema.Seguindooparadigmadeorienta çãoaobjetos,
separamososcomportamentosdenossaaplica çãoemclassesquesãoreferenciadas
emtodosospontosdenossosistemaqueprecisemusarafuncionalidadeencapsu-
lada.Estetipodecomportamentoéperfeitamenteaceitávelquandoasdependências
entreosobjetosestádiretamenterelacionadaàlógicadenegócioimplementada.Por
exemplo,onossointegradorexpostonaintrodu ção,queprecisavadeumDAOpara
receberosdadosaseremprocessadoseoutroparaenviaroresultadodoprocessa-
mento.
Noentantoháalgunscomportamentosqueaparecemportodaaaplica çãoque
nãoestãonecessariamenterelacionadosàlógicadenegócioqueestamosimplemen-
tando.Observamosqueestetipodecomportamentocostumagerarumainfinidade
decódigorepetitivoespalhadoportodoosistema.Chamamosestecomportamento
secundáriodeaspecto.
Umbomexemplodeaspectoseriaumcontroledeseguran ça.Vamosimaginar
quesejadenossointeressepermitiraexecu çãodealgunsmétodosemnossosistema
19


## Página 30

2.4. Alternativascomeçamasurgir:IoC/DIeAOP CasadoCódigo
apenasseousuáriocorrentetiverpermissãoparatal. Poderíamosimplementara
funcionalidadeemumaclassequeencapsulealógicadeacessoeemseguidainjetá-
laemdiversasoutrasclassesdonossosistema,talcomonoexemploabaixo:
public class ClasseMuitoImportante {
private ControleAcesso controleAcesso;
public ControleAcesso getControleAcesso() {
return controleAcesso;
}
public void setControleAcesso(ControleAcesso ca) {
controleAcesso = ca;
}
public void metodoImportante() {
if (getControleAcesso().possuiPermissaoParaTal()) {
// executa código incrivelmente importante
}
}
}
public class OutraClasseMuitoImportante {
private ControleAcesso controleAcesso;
public ControleAcesso getControleAcesso() {
return controleAcesso;
}
public void setControleAcesso(ControleAcesso ca) {
controleAcesso = ca;
}
public void apagarTudo() {
if (getControleAcesso().possuiPermissao()) {
// apaga TUDO
}
}
}
Reparecomonasduasclassesvemosomesmocódigosendorepetido:
private ControleAcesso controleAcesso;
public ControleAcesso getControleAcesso() {
return controleAcesso;
20


## Página 31

CasadoCódigo Capítulo2. ConheçaoSpringFramework
}
public void setControleAcesso(ControleAcesso ca) {
controleAcesso = ca;
}
public void algumMetodo() {
if (getControleAcesso().possuiPermissao()) {
// faça algo
}
}
Estediscoarranhadoespalhadoportodonossocódigoéoquechamamos as-
pecto,ouseja,umacaracterísticaqueécomumaváriospontos.
Enquantoainje çãodedependênciasmodularizanossosistemausandooquea
OrientaçãoaObjetostemanosoferecer,aAOPdiminuiaindamaisoacoplamento
isolandoos aspectosquenãosãofacilmenteidentificáveiseisoladospelaorienta ção
aobjetos.
Identificadoeisoladososaspectos,tudooqueaAOPprecisafazeréintercep-
taremtempodeexecu çãoaschamadasaosmétodosondedetectamosanecessidade
deaplicaçãodocomportamentoidentificadoe,combasenisto,alterarocomporta-
mentodenossasclassessemqueestassequersaibamdisto.
Nãosepreocupenestemomentosenãoconseguiucompreenderexatamente
comoaAOPfunciona: aexplica çãoquedeiéamaissuperficialpossível,apenas
paratrazeroassuntoatona.Teremosumcapítulointeirosóparatrataresteassunto.
OimportanteagoraésaberqueaplicandoIoC+DI+AOP,oSpringconsegue
evitarqueprecisemosdeumservidordeaplica çõesJavacompleto.Usandoumser-
vidordeServlets“simples”,comoJettyouTomcat,conseguiremospraticamenteos
mesmosresultadosquesópoderiamserobtidosanteriormentecomumservidorde
aplicaçõescomoJBoss,WebLogicouWebSphere.
Resumindo Inversão de Controle , I njeção de Depen-
dências eProgramação Orientada a Aspectos
Agrossomodo,vocêpodepensaroseguinte:aIoCcontrolaociclo
devidadenossasaplica ções,aDIdefinequaisclassesiremosinstanciare
emquaislugaresiremosinjetá-las.JáaAOPvaialémnamodulariza ção
queaDInosproporciona,adicionandonovoscomportamentosàsnossas
classes.
21


## Página 32

2.5. Container:osujeitoquetornatudoistopossível CasadoCódigo
2.5 C ontainer : o sujeito que torna tudo isto possí -
vel
Oservidordeaplica çõesJavatambéméchamadode Container EJB.Nofinaldascon-
tasoSpringiráapresentarumcontaineralternativonoqualpossasergerenciadoo
ciclodevidadenossosobjetosdenegócio. Chegouportantoomomentodeapre-
sentarumasériedeconceitosfundamentaisparaacompreensãodorestantedeste
livro.
Oátomodetodaanossahistóriaéo objeto de negócio.Esteéainstânciadeuma
classeaondeimplementamosnossosrequisitosfuncionais. OEJBéumobjetode
negóciose,nocasodoSpring,nósochamamosde bean.
Um beanéumobjetoquepossuiseu ciclo de vidagerenciadopelo containerde
IoC/DIdoSpring. Umaboamaneiradeentendercomoainversãodecontrolese
aplicaédescreveroquevêmaserotaldo ciclo de vida.
2.6 D o início ao fim de um objeto, entenda o ciclo de
vida
O Ciclo de vidadizrespeitoàsetapasdeexecu çãodeumobjeto.Asfasespelasquais
umobjetodenegóciopassaduranteaexecu çãodeumprograma,sãoilustradosna
figura5.1.
22


## Página 33

CasadoCódigo Capítulo2. ConheçaoSpringFramework
Figura2.1:Ciclodevidadeumobjeto
1) Oobjetoéinstanciado;
2) Sehouveremdependênciasasereminjetadasnoobjeto,estasdevemserinjetadas;
3) Seapósasdependênciastiveremsidoinjetadasfornecessárioexecutarummé-
tododeinicializa ção,estedeveráserinvocado;
4) Oobjetojáinicializadoecomtodasassuasdependênciasinjetadaséenviadoao
clientequedelenecessita;
5) Umaveznãomaisnecessário,existindoummétododestrutor,estedeveráser
invocadoeoobjetodescartadodo container.
Nãoédifícilimaginaraexecu çãodetodoesteprocedimentoprogramaticamente.
Comrelaçãoàultimaa ção,bastaríamosescreverummétododestrutor,algocomo
um finalize,emnossaclasseerezarparaqueestesejaexecutadonomomento
certopelaJVM.Masissonãoélámuitoelegante,certo?
Voltandoao bean,esteémaisqueummero JavaBean.Deveservistocomoum
componente.Oquediferenciaumcomponentedosdemaisobjetos,comoum Java-
Bean,porexemplo,sãoasseguintescaracterísticas:
23


## Página 34

2.6. Doinícioaofimdeumobjeto,entendaociclodevida CasadoCódigo
•Possui baixa granularidade,ouseja,seusclientesnãoprecisamsaberquais
assuasdependênciasinternas;
• Oquerealmenteimportaparaseusclienteséa interface disponibilizada pelo
objeto,quedefinequaisosservi çosoferecidospelomesmo(éoseucontrato);
• Sãofacilmente substituíveis por outras implementações quemantenhamo
mesmocontrato(plugabilidade).
O que é um Jav aBean?
FoiumpadrãoadotadopelaSunparaaescritadecomponentesreu-
tilizáveis.TodoJavaBeandevesatisfazertrêscondições:
1) Devepossuirumconstrutorpúblicoquenãorecebaparâmetros
2) Todososseusatributosvisíveisdevemserdeclaradoscomoprivados
(ouprotegidos)eacessadosapenaspormétodos gete set.
3) Deveimplementarainterfacejava.io.Serializable
ExemplodeJavaBean:
class Pessoa implements java.io.Serializable {
// construtor publico sem argumentos
public Pessoa() {}
private String nome;
// getter
public String getNome() {return this.nome;}
// setter
public void setNome(String valor) {this.nome = valor;}
}
Podemosdizerportantoqueo containeréoelementoarquiteturaldenossaapli-
cação,responsávelporgerenciarociclodevidados componentesdonossosistema.
24


## Página 35

CasadoCódigo Capítulo2. ConheçaoSpringFramework
Todo container(EJBounão)funcionabasicamentedamesmamaneira:sãoalimen-
tadosporalgumaformadeconfigura çãoecombasenelas,criaminternamenteas
regrasdegerenciamentodoscomponentesalidescritos.
Um containerpode ser intrusivoou não. É intrusivo quando requer que
seusobjetosgerenciadosdependamdesidealgumamaneira,comoporexemplo,
obrigando-osaimplementaralgumainterfaceoupossuíremalgumaanota çãoespe-
cífica.
O containerEJBéumexemplodeintrusivo. Nasversõesanterioresà3.0era
necessárioquetodoEJBimplementasseumasériedeinterfacesparaquepudessem
serreconhecidos(istoalémdoarquivodeconfigura ção).Mesmoapósaversão3.0,
aindapodemosdizerqueháumcertoníveldeintrusãopelofatodeseremnecessárias
anotaçõesJavaparaindicarpontosdeinje çãodedependênciasemétodosde callback
aseremchamadosduranteociclodevidadoobjeto.
NocasodoSpringtemosum containercomintrusividademínimapois,aocon-
tráriodoEJB,trabalhamoscomPOJOs(PlainOldJavaObject). UmPOJOéuma
classeJavanormalquenãoprecisaimplementarnenhumainterfaceoupossuirdeter-
minadaanotaçãoparaquepossasergerenciadaporum framework.Decertomodo
éaclassequeimplementaregrasdenegóciodeumaformaideal,ouseja,quese
preocupaúnicaeexclusivamentecomaexecu çãodenossosrequisitosfuncionais.
Comintrusividademínima,temoscomoganhoummaiorreaproveitamentode
código,vistoestenãomaisdependerdeumaplataformaespecíficaparaquesejaexe-
cutado.Outravantagemimportanteéfacilitaraescritadetestes,dadoaredu çãodas
dependênciasexternasaoobjetoqueatéentãoprecisaríamossimular,paraconseguir
realizartestes.
Outradiferençaimportanteentre containersdizrespeitoaoseupeso:podemser
leves(“lightweight”,comooSpring)oupesados(“heavyweight”,comoocontainer
EJB).DeacordocomRodJohnsonemseulivro Expert One-T o-One J2EE Develop-
ment Without EJB[8],todo containerlevepossuiasseguintescaracterísticas:
• Nãosãointrusivosousãominimamenteintrusivos;
• Possueminicializaçãorápidaeconsomempoucosrecursoscomputacionais;
• Sãoindependentesdoambientedeexecução. OSpringporexemplopode
serexecutadotantodentroquantoforadeumservidordeaplica çõesouaté
mesmoemapplets;
25


## Página 36

2.6. Doinícioaofimdeumobjeto,entendaociclodevida CasadoCódigo
• Definemrequisitosmínimos(praticamenteinexistentes)paraqueumcom-
ponentepossasergerenciado.
Independentedeserintrusivoounão,leveoupesado,todo containerdevesa-
tisfazertrêsrequisitos:serconfigurável,controlarociclodevidadosseusobjetose
provermétodosdeobtenção,tambémconhecidoscomo lookup,decomponentesde
negócio.
DadoqueaprincipalfalhadoEJBanteriorao3.0foioexcessivotempoque
gastávamoscomrequisitosnãofuncionais,devemosfazerumaperguntafinalso-
bre containers: realmente precisamos de um já que nosso objetivo é simplificar a
arquitetura?
Arespostaé sim.Um containernosoferecealgumasvantagensquejustificam
seuuso.Aprimeiradelasdizrespeitoàplugabilidade.Dadoqueasimplementa ções
denossoscomponentessãodefinidaspelaconfigura ção,ficamuitofácilsubstituir
umaimplementaçãoporoutrasemquebrarosistema.
O que é um lookup?
Usamosestaexpressãoparadesignaraobten çãodeobjetosapartir
deumcontainer.Todocontainerdeveproveralgumainterfacequenos
forneçamétodosquepossibilitemobterobjetosapartirdoseunomeou
tipo.
Veremosnocapítulo3comofazerumlookupnoSpring. Maspara
matar sua curiosidade, a especificação JNDI da plataforma Java EE,
muitousadopelosEJBsnarealidadeéumainterfacedelookup.Nocó-
digoabaixo,quandoexecutamosométodo lookupnoobjeto Context,
estamosexecutandoaobten çãodeumobjetojápreparadopelocontainer
paraexecução.
Context ctx = InitialContext();
// Lookup em ação
Object objeto = ctx.lookup("meuObjeto");
Uniformidadedeconfigura çãoéoutravantagemimportante: apartirdomo-
mentoemquepadronizamoscomoéociclodevidaedependênciasdenossoscom-
26


## Página 37

CasadoCódigo Capítulo2. ConheçaoSpringFramework
ponentesemumúnicoponto,aumenta-sesignificativamentea manutenibilidadede
nossosprojetos.
Costumomencionartambémcomovantagemoargumentodaautoridade.Em
grandepartedoscasos,quemimplementouogerenciamentodeciclodevida,inje ção
dedependênciasedemaisserviçosoferecidospelo frameworkpossuiumaexperiên-
cianomeiomuitomaiorqueaminhaousua.
Quandonãoestamostrabalhandocomumaversãodetestes,normalmentepo-
demostercertezadequeestamoslidandocomumsoftwaredevidamentetestado
nãosópelosdesenvolvedoresqueoimplementaramcomoquetambémpelacomu-
nidadequeousa.Quantomaioracomunidade,maior,emtese,éaquantidadede
testesemambientedeprodu çãopelosquaispassouaquelecódigo.
Finalmente,outravantageminteressanteoferecidapelos containerséofatode
nospropiciaremumpontoúnicodeacessoaosservi çosquecompõemnossaapli-
cação,garantindoassimumamaiorpadroniza çãodoprojetoeconsequentemente,
maiorfacilidadedeadapta çãodenovosmembrosdaequipeaeste.
2.7 S pring em partes
NãoseriaexagerodizerqueoSpringéaprovadequeosconceitosdeinversãode
controleeinje çãodedependênciasrealmentefuncionam,dadoquepraticamente
todasasfuncionalidadesdoframeworksãobaseadasemseu container.Observando
osmódulosbásicosdoframeworkédifícilnãosemaravilharcomopoderdestas
técnicas.
Éimportantetermosestavisãopanorâmicadosmódulosquecompõemofra-
meworkparaquefiqueclarooquãoabrangenteeleé:basicamenteoSpringabrange
todasasnecessidadesdeumaaplica çãocorporativa.
Emsuaversãobásica,oSpringéformadoporseiscomponentes: o container
deinversãodecontrole,suporteaAOP,instrumenta ção,acessoadados/integra ção,
suítedetesteseweb,comopodeservistonafigura2.2.
27


## Página 38

2.8. OContainer CasadoCódigo
Figura2.2:OscomponentesbásicosdoSpring
Éinteressanteobservarquecomorequisitobásicodefuncionamentonãotemos
umservidordeaplica çõesouServlets,masapenasaJVM.Estefoiumdosprincipais
diferenciaisdoSpringemseulan çamento:trazerparaodesenvolvedorrecursosde
computaçãocorporativaqueatéentãosóeramoferecidosporservidoresdeaplica ção
pesados.
Comoexemplodestesrecursospodemoscitarcontroletransacionaldeclarativo
egerenciamentodeciclodevidadecomponentes.
UmpontoimportantequedevesermencionadoéofatodoSpring,aocontrário
deumcontainerEJB,nãoserumasolu ção tudo ou nada.Vocêusaapenasoscompo-
nentesqueinteressamaoseuprojeto,podendoignorartranquilamenteaquiloque
nãoprecisa.Consequentemente,temoscomoresultadoumaarquiteturabemmais
enxutaefácildetrabalhar.
Masvoltemosaosnossosmódulos.
2.8 O C ontainer
SequisertrabalharcomoSpring,esteprovavelmenteéoúnicomóduloobrigatório.
Osmódulos coree beanssãoonúcleodoframeworkaondesãoimplementadoso
suporteàinversãodecontroleeinje çãodedependências.
28


## Página 39

CasadoCódigo Capítulo2. ConheçaoSpringFramework
Jánomódulo contextencontra-seaimplementa çãodo ApplicationContext.
NoSpringhádoistiposde containers: BeanFactorye ApplicationContext.
O BeanFactoryexistedesdeaprimeiraversãodo framework.Ébasicamente
umaimplementaçãosofisticadadopadrãoFactory,baseadaemconfigura ção.For-
neceapenasosuportebásicoaIoCeDIeencontra-seimplementadonomódulo
core. Asegundaversãoébaseadano BeanFactoryeoferecerecursoscorporativos
maisavançados,comoporexemplogerenciamentoderecursos,internacionaliza ção.
Naprática,raríssimasvezeso BeanFactoryéusado,eseuusoéinclusivedesen-
corajadopeloprópriopessoaldaSpringSource[14],queéaequiperesponsávelpelo
desenvolvimentodoframework.Napráticaseuusoatualmentesófariasentidoem
ambientescomputacionaisextremamenterestritos,comoporexemploappletsou
dispositivosmóveis.
Finalmente,temostambémomódulo Expression Language(SpEL).Comovere-
mosnopróximocapítulo,aformamaispopulardeconfigura çãodoSpringéatravés
dedocumentosXML.ASpELnosforneceumalinguagemmuitoparecidacomaEL
queestamosacostumadosausarcomJSPs,porémvoltadaparaaconfigura çãodo
container. Elatornanossosarquivosdeconfigura ção“vivos”,namedidaemquea
partirdoseuusopodemosdefinirvaloresdeconfigura çãoemtempodeexecu çãoe
nãoemtempodeconfigura ção.
2.9 T rabalhando com AOP e Aspects
OSpringvêmacompanhadodoseupróprioframeworkqueimplementaaprogra-
maçãoorientadaaaspectos. Estepodeviremdois“sabores”. Tradicional,queéa
primeiraimplementaçãodeAOPdoSpringou Aspects,queéousodoAspectJcomo
motordeAOPdoSpring,umaalternativabemmaispoderosaqueaoriginal.
Nãosepreocupe,comodisseanteriormente,teremosumcapítulosóparaenten-
dermoscomoaAOPrealmentefuncionanoSpring.
2.10 I nstrumentação de código
Oprojetonãoacabaquandofazemosodeploy.Éimportantelembrarqueamaior
partedocustodeumsoftwareéasuamanuten çãoeaequipedoSpringtinhaplena
consciênciadisto. Omódulodeinstrumenta çãofacilitaavidadopessoaldesu-
porteoferecendofacilidadesnaimplementa çãodeJMX.Estatecnologianosper-
miteacompanharemtempodeexecu çãotudooqueacontececomnossossistemas,
gerandodiversasestatísticasinteressantes.
29


## Página 40

2.11. Acessoadadoseintegração CasadoCódigo
2.11 A cesso a dados e integração
Todaaplicaçãocorporativaquesepreze,precisaacessareescreverdadosemalguma
fontededados. Decara,oSpringnosoferecesuporteàsprincipaistecnologiasde
persistênciaadotadaspordesenvolvedoresJava.HásuporteparaJDBC,ORMscomo
Hibernate,iBatis,JPA,JDOeOXM.Osuporteaestastecnologiassedaatravésde
templates,quereduzemsignificativamenteaquantidadedecódigo boilerplate,ou
seja,deinfraestrutura,queprecisamosescrevernestassitua ções,comoporexemplo
abrirefecharconexões,iniciarefinalizartransa çõesetc.
Alémdosuporteaestastecnologias,estemódulonosoferecetambémumanova
hierarquiadeexce çõesqueébemmaisinteressantedoqueasoferecidasoriginal-
mentepelastecnologiasquesãoabstraídas.
Umdospontosdevendado frameworkencontra-senestemódulo: ocontrole
transacional. Springnosofereceumaimplementa çãodetransa çõesdeclarativase
programáticasquevaialémdoqueéoferecidohojepelosservidoresdeaplica ção.
Maisqueisto:tornaanecessidadedestescoisadopassado.
Finalmenteenãomenosimportante,hátambémsuportenativoaJMS.Talcomo
ocorrecomasdiferentesfontesdedadosabrangidaspelo framework,temosaquia
aplicaçãode templatesquetornamavidadodesenvolvedormuitomaistranquilano
momentodelidarcomsuasfilasJMS.
2.12 A plicações na Web com o Spring
QuandovocêpensaqueoSpringjáfazcoisasdemais,nãoéraroosqueestãoco-
meçandocomessatecnologia,sesurpreenderemaodescobrirque,“debrinde”,há
um frameworkqueimplementaoMVCdeumaformaextremamenteprodutivapara
você.Trata-sedoSpringMVC.
Ointeressantedestemóduloéquenãofoiplanejado,massurgiuconformea
equipededesenvolvimentodo frameworkfoiaceitandoofatodequeoStruts, fra-
meworkquedominavaomercado,apresentavaumasériedelimita çõesquedificul-
tavambastanteasepara çãodeinteressesentreascamadasdecontrole,negócioe
visualização.
UmaoutracuriosidadesobreoSpringMVCéofatodeleserabasedeoutro
projetomuitoimportanteparaaSpringSource:o frameworkGrails,queébaseadoem
GroovyeapresentaomesmoníveldeprodutividadeoferecidopeloRubyonRails.
Alémdeste frameworkMVC,hátambémsuportebásicoparaqueo container
doSpringsejaaplicadoemumaaplica çãoJavawebconvencional,atravésdepeque-
30


## Página 41

CasadoCódigo Capítulo2. ConheçaoSpringFramework
nasalteraçõesnoarquivo web.xmlesuporteaalguns frameworkswebdemercado
comoJSF,Struts1.xe2.x,WebWorkeTapestry.
2.13 E ainda mais componentes!
O containerdoSpringétãoversátilque,poucotempoapósoseulan çamento,a
SpringSource,entidaderesponsávelpelodesenvolvimentodo framework,desenvol-
veuparaeleumasériedecomponentesopcionais.
DentreosmaisfamosospodemoscitaroSpringSecurity,quecuidadaseguran ça
daaplicaçãodeumamaneiraextremamenterobustaepodeseraplicadoemqualquer
projetoSpring,alémdeserumamaravilhosaaplica çãodoconceitodeAOP.
OutrocomponenteinteressanteéoSpringData,usadoparalidarmoscombases
dedadosrelacionaisounão,talcomoéfeitonomódulodeacessoadados/integra ção
doSpring,abstraiparaodesenvolvedoraquelesdetalhestediososerepetitivosde
implementação,atravésde templatesmuitofáceisdeseremusados.
Sequiserintegrarsuaaplica çãocomredessociaisépossívelusaromódulo
SpringSocial,quetornamuitofácilacomunica çãocomservi çosconsagradoscomo
Twitter,Facebook,LinkedIneoutros.
ParaaquelesquetrabalhamcomprocessamentoemlotemaispesadoháoSpring
Batch:umabibliotecaextremamenteleve,quetornaavidadequemprecisatrabalhar
comSpringeprocessamentopesadoemlotesumatarefabemmaisagradável.
Eestespormaisincrívelquepare çanãosãotodososmódulosadicionais.Vere-
mosesseseváriosoutrosnodecorrerdesselivro!
2.14 R esumindo
Nestecapítulopudemosconhecerosconceitosbásicosquenosguiarãonotranscor-
rerdestelivroapartirdosproblemasquejustificaramacria çãodoSpring. Feito
isto,tivemostambémumavisãopanorâmicadosmódulosbásicosquecompõemo
frameworkeinclusiveconhecemostambémalgunsmódulosopcionaisquepoderão
tornarnossavidamaisfácildaquiparafrente.
Nãoseassusteseestesconceitosaindanãoestiveremfazendosentidoparavocê.
Apartirdopróximocapítulo,quandocome çamosaporamãonamassamesmo
comoSpring,veremoscomotudoseencaixaemumquebracabe çasque,naprá-
tica,possuiapenasumtipoepe ça:o containerdeinversãodecontroleeinje çãode
dependências.
31


## Página 43

Capítulo3
ConhecendooContainer
ChegouomomentodelidarmosdiretamentecomoSpringFramework.Opontode
partidaseráocontainerdeinversãodecontrole/inje çãodedependências,chamado
nadocumentaçãooficialcomo“CoreContainer”[14]. Serãovistosquatrodeseus
componentesfundamentais:Core,Beans,ExpressionLanguage(SpEL)eContext.
Figura3.1:OquecompõeoCoreContainer


## Página 44

3.1. Preparandoseuambientededesenvolvimento CasadoCódigo
Nabasedo Core Containerseencontraomódulo Core.Muitosacreditamerro-
neamenteseresteolocalaondeseencontraimplementadoocontainerdoSpring,o
queé quaseverdade.Narealidadeaiseencontramasclassesbásicasquepermitirão
asuaimplementa çãonomódulo Beans.Em Coresãoencontradasfacilitadoresno
gerenciamentodeclassloaders,reflexão,tratamentoderecursos,strings,etc.Resu-
mindo,énestemóduloqueseencontratodaainfraestruturanecessáriaquepermite
aimplementaçãodocontainer.Naprática,entretanto,sempretrabalhamoscomes-
tesdoismódulosjuntoscomosefossemumsó.
Usandocomobaseo Coretemosomódulo Beans,ondeencontramosaprimeira
versãodocontainerqueéo BeanFactory.Esteéumaimplementa çãosofisticadado
padrãodeprojetos factoryquetornadesnecessáriaacodificaçãomanualde singletons
enospermiteodesacoplamentototaldogerenciamentodedependênciaseciclode
vidadenossosbeansdenossocódigofonteatravésdomecanismodeconfigura ção
implementadonestemódulo.
Comoveremosomecanismomaispopulardeconfigura çãodoSpringéoXML.
Comoobjetivodeadicionarmaiordinamismoàconfigura çãodoframeworka
equipededesenvolvimentodoSpringcriouaSpringExpressionLanguage(mais
conhecidacomoSpEL),queéumalinguagembaseadaemexpressõesquelembra
bastanteà Unified Expression Language(EL)presentenoJSP.Estalinguagemnos
permitedefinirvaloresecomportamentosaosnossosbeansdefinidosusandoXML
ouanotaçõesemtempodeexecu ção,oqueéimpossível(ouaomenosbastantedifí-
cil)semesterecurso.
Finalmente,temosomódulo Context,aondeseencontraaimplementa çãomais
avançadaecomumenteusadadocontainerqueéo ApplicationContext.Esta,base-
adanabasefornecidapelosmódulos Coree Beansoferecerecursospoderososcomo
porexemplointernacionaliza ção,propaga çãodeeventos,AOP,gerenciamentode
recursoseacessoafuncionalidadesbásicasdaplataformaJavaEE.
3.1 P reparando seu ambiente de desenvolvimento
Parainiciarnossotrabalhoéimportantequesejadescritocomodeveserfeitaacon-
figuraçãodoseuprojeto.Hábasicamenteduasmaneirasdeconfigurarseuprojeto:
usandoounãoumgerenciadordedependênciasbaseadonoMaven.
Configurando manualmente
ParaadicionarmanualmenteasdependênciasdoSpringbaixeoframeworkem
34


## Página 45

CasadoCódigo Capítulo3. ConhecendooContainer
http://www.springsource.org/download/community. Sempreháduasversõesdis-
poníveisparadownload: comousemadocumenta ção. Dadaaaltaqualidadeda
documentaçãodoprojetoeofatodeaindahojeem2012nemsempretermosaIn-
ternetdisponível,érecomendávelescolheraversãoquecontenhaadocumenta ção
básicadoframework.
Feito isto, basta adicionar ao seu classpath (ou usando sua IDE de sua
preferência) os seguintes arquivos jar: spring-core-3.1.1.RELEASE.jar, spring-
context-3.1.1.RELEASE.jar, spring-beans-3.1.1.RELEASE.jar, spring-expression-
3.1.1.RELEASE.jar.Tambéménecessárioadicionaraúnicadependênciaexternaque
oSpringusaránestecapítuloqueéoCommonsLoggingdaFunda çãoApacheque
deveestarnaversão1.1ouposterior.
Configurando com Maven
Suavidaserábemmaisfácilcasoestejatrabalhandocomalgumgerenciadorde
dependênciasbaseadoemMaven. Comoomódulo Contextébaseadonosoutros
trêsmódulosquetrataremosnestecapítulo,apenasestadependênciadeveserin-
cluídaemseuprojetoeconsequentementetodasasdemaisvirãoporconsequência.
Ocódigoabaixoexpõeumexemplodestaconfigura çãousandoMaven.
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-context</artifactId>
<version>3.1.1.RELEASE</version>
</dependency>
Escolha da IDE
AtualmenteasIDEsmaispopularescomoporexemploNetbeans,EclipseeJet-
BrainsIDEAoferecemsuporteaoSpringatravésdepluginsdadaapopularidadedo
framework.NoentantoomelhorsuporteatualmenteéoferecidopeloSpringSource
ToolSuite.
OSpringSourceToolSuite(STS)éadistribui çãocustomizadadoEclipsede-
senvolvidapelaequipedaSpringSourceequepodeserbaixadaemhttp://www.
springsource.org/downloads/sts. Éoambienteidealparaodesenvolvedorhabitu-
adoatrabalharcomoEclipsepoisjávêmcomtodosospluginsnecessáriosparaque
odesenvolvedorpossacome çaratrabalharimediatamentesemqueprecisesepreo-
cuparcomainstala çãodecomplementosemsuaIDE.Dentreospluginsdestaca-se
35


## Página 46

3.1. Preparandoseuambientededesenvolvimento CasadoCódigo
osuporteaosdemaisprojetosdaSpringSourcecomoporexemploSpringBatch,
IntegrationeMVC.OexcelentesuporteaoutrosprojetosdaempresacomoGrailse
Rootambémjustificamoseuuso.
Paraosiniciantesháalgunsrecursosqueauxiliambastanteoaprendizado,como
porexemplooautocompletarquandoestamosaeditararquivosdeconfigura çãoe
apossibilidadedevisualizargraficamenteosrelacionamentosentrenossosbeanstal
comopodeservistonaimagemabaixo.
Figura3.2:SpringSourceToolSuite
AinstalaçãodoSTSébastantesimples:bastabaixaroinstaladoradequadoao
seusistemaoperacionalemhttp://www.springsource.org/downloads/stseexecutá-
lo.CasojápossuaoEclipseinstalado,étambémpossívelinstalarmanualmenteos
pluginspresentesnoSTS.Paraisto,bastaseguirasinstru çõespresentesnomanual
deinstalaçãodaIDE[9].
ÉimportantelembrarqueaescolhadaIDEécompletamenteopcionaldadoque
praticamentetodasasmaisadotadaspelomercadooferecemsuporteaoframework.
Sendoassim,casonãosesintaàvontadecomoSTSéimportantequesaibaquea
36


## Página 47

CasadoCódigo Capítulo3. ConhecendooContainer
escolhadaIDEemnadainfluenciaráseuaprendizadodoSpringusandoestelivro.
3.2 N osso sistema de exemplo
A melhor maneira de aprendermos como funciona um framework é usando-o.
Nossopontodepartidaéumsistemabastantesimplestalcomofizemosnoprimeiro
capítulo.Esteexemploéidealparacome çarmospoisésimplesosuficienteparaque
possamosverobásicomasaomesmotemponosofereceespa çoparaquepossamos
transformá-loemummonstrocomplexoecomistoevidenciaropoderqueoSpring
nosfornece.
Trata-sedeumsistemadeBIinicialmentecompostoportrêselementos: uma
fontededados,umprocessadorresponsávelpelaexecu çãodoscálculose,finalmente,
umimpressorqueiráformatarosresultadosdetalformaquesetornemlegíveisaos
usuáriosfinaisdosistema.
Inicialmentenosso processadorseráaparteimutáveldonossosistemae,como
podeserobservadonodiagramadeclassesabaixopossuiduasdependências.Como
queremosmáximaflexibilidade,jáimplementamosnossocódigodeacordocomo
princípiode Inversão de Dependências,segundooqualnossocomponentedenível
maisalto(Processador)possuicomodependênciasdiretasapenasabstra çõesque,
nestecaso,sãoasinterfaces FonteDadose Impressor.
Figura3.3:Situa çãoInicialdonossosistema
3.3 D eclarando beans
Paraqueumbeanexistasãonecessáriostrêselementos:asconfigura ções,ocontai-
nereaclassequeoimplementa.NocasodoSpringasconfigura çõespodemvirde
trêsfontes:XML,anotaçõesoucódigoJava.Nossofocoinicialseráoprimeirofor-
mato,poisestetornaexplícitodeumamaneirabastantedidáticaofuncionamento
docontainer.Comoveremosnotranscorrerdestecapítulo,asfontesrestantestem
comoobjetivoprincipalaredu çãodoXMLoumesmosuaelimina ção,oqueaumenta
bastanteaprodutividadedodesenvolvedor.
37


## Página 48

3.3. Declarandobeans CasadoCódigo
Aconfiguraçõesdevemnosfornecerosdadosmínimosparaqueocontainer
consigainstanciaregerenciarociclodevidadenossosbeans. Aúnicainforma-
çãoqueobrigatoriamentedevemosforneceréqualaclassequeimplementaobean.
Usamosatag <bean>paradeclararumbeanenestaoúnicoatributoobrigatórioé
class.Sendoassim,paradeclaramosumaimplementa çãodenossainterface Fon-
teDadosqueobtenhanossosusuáriosusandoumarquivotextoconfiguramosobean
talcomonoexemploabaixo:
<bean id="fonteDados" class="br.com.casadocodigo.FonteDadosArquivo"/>
Oatributo id,comoopróprionomejádiz,identificaunicamenteumbeanno
container.Casooatributonãoestejapresente,obeanseriainstanciadoegerenciado
peloSpringdamesmamaneira.Adiferen çanocasoseriaquemnomeariaobean:o
própriocontainer.Éinteressanteobservarqueumbeanpodetermaisdeumnome,
masnãosepreocupecomistoporenquanto,estetemaseráabordadomaisàfrente
esóédefatoútilemprojetosmaioresqueenvolvamequipesmuitograndes.
Senossobeanjátemumnome,éfundamentaldefinirmostambémqualasua
origem,ouseja,qualclasseoimplementa.Paratalusamosoatributo class,oúnico
obrigatório,aondedevemosforneceronomecompletodaclasse.
Quandonossocontainerforinstanciadoealimentadocomestasconfigura ções,
obeanseráinstanciadoeemseguidaestarádisponívelparausopelorestantedo
sistema.
Noentantonossaconfigura çãoaindaestáincompleta.Definirquaisobjetosins-
tanciaréótimo,porémopadrãodeprojeto factoryjáresolverianossoproblema.
Nestemomentonossocontaineraindanãopassadeum factoryconfigurávelpor
XML,oqueaindanãojustificaaado çãodoSpring.Oleitoratentojádeveterobser-
vadoqueaclassequeestamosinstanciandosechama FonteDadosArquivo.Quetalse
tambémdefiníssemosqualoarquivoemqueseencontramosdadosquequeremos
instanciar?Entraema çãoatag <property>.Podemosdefinirqualobjetocarregar
modificandonossaconfigura çãoparaquefiquesimilaraoexemploabaixo:
<bean id="fonteDados" class="br.com.casadocodigo.FonteDadosArquivo">
<property name="arquivo" value="/arquivos/pessoas.csv"/>
</bean>
Hádoisatributosnatag <property>.Primeiroénecessáriodefinirqualatri-
butodenossoobjetodeverásermodificado,oqueéfeitocomoatributo name,que
fazreferênciaaopadrão JavaBeanquedeve,porconven ção,seradotadoportodosos
38


## Página 49

CasadoCódigo Capítulo3. ConhecendooContainer
nossosbeans.Deacordocomestapropriedade,devehaverimplementadonaclasse
FonteDadosArquivoummétodochamadosetArquivoquerecebacomoparâmetro
umobjetodotipo String. Ovaloraser injetadoencontra-sedefinidonoatributo
value. Éinteressanteobservarquenãoénecessáriosepreocuparcomotipoaser
recebidopelosetter,poisotipoédescobertoemtempodeexecu çãopelocontainer.
Combasenestaconfigura çãomaisrica,ocontaineriráexecutarasequênciade
operaçõesdescritaabaixo:
1) BeanfonteDadosdotipo br.com.casadocodigo.FonteDadosArquivoéinstanciado
2) O valor da propriedade arquivo é definido como sendo igual a “
/arquivos/pessoas.csv”
3) Beaninstanciadoeconfiguradodisponívelparaserusadopelorestodosistema
Éinteressanteobservarqueobeansóédisponibilizadoparausoapósseues-
tadotersidoinicializado.Como“brinde”acabamosdeganharasoluçãoparatoda
umagamadeproblemasdecorrentesdaobten çãoconcorrentedeobjetoscujaini-
cializaçãodoestadonãofoitotalmenteconcluída.Eestesequereranossoobjetivo
inicial!
Noentantoisoladamenteumbeannãoédegrandeutilidade.Opoderdocontai-
nercomeçaasurgirapartirdomomentoemqueainje çãodedependênciascomeça
aentrarema ção.Podemosvernocódigoabaixoaconfigura çãocompletadonosso
sistematalcomoseencontranoestadoatual.
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd">
<bean id="fonteDados" class="br.com.casadocodigo.FonteDadosArquivo">
<property name="arquivo" value="/arquivos/pessoas.csv"/>
</bean>
<bean id="impressor" class="br.com.casadocodigo.ImpressorImpl"/>
<bean id="processador" class="br.com.casadocodigo.Processador">
<property name="impressor" ref="impressor"/>
39


## Página 50

3.3. Declarandobeans CasadoCódigo
<property name="fonteDados" ref="fonteDados"/>
</bean>
</beans>
A primeira novidade que vemos no arquivo completo é a inclusão da tag
<beans>queéoelementoraizdodocumento.Nãoénecessárioseintimidarcomas
declaraçõesdenamespacespresentesnestedocumentovistoqueatualmenteamaior
partedasIDEs,comseusuporteaoSpringjáoferecemapossibilidadedegerarauto-
maticamenteestedocumentoparaosnovatosnoframework.Comoveremosmais
adiante,oSpringofereceumasériedenamespacesquetornamavidadodesenvol-
vedormuitomaisfácilampliandoasemânticadoXMLpadrão.
Naversãocompletadenossaconfigura ção,devemosfocarnossaaten çãosobre
obean processador.Umnovoatributoaparecenatag <property>: ref(abreviação
de reference),cujovaloréonomedeumdosbeansdefinidosnaconfigura ção.Esta
éatãofaladainje çãodedependênciasema ção.Novamente,éimportanteobservar
quenãoprecisamosnospreocuparcomotipodosobjetosqueestamosinjetando
poisoprópriocontainerseencarregadestatarefa.Casohajaalgumproblemacoma
tipagemdosobjetos,ocontainerirádispararumaexce çãonosinformandodoerro
paraquesejamfeitasasaltera çõesnecessáriasnasconfiguraçõeseosbeanssetornem
disponíveis.
Novamente,nocasodobean processador,estesóestarádisponívelapóstersido
instanciadoetodasassuasdependênciasteremsidoinstanciadas,preparadaseinje-
tadas.Éimportanteobservarquenossocontainerjápodeservistocomoumaclasse
factorymelhorevoluídaquenãosódecidequaisclassesinstanciarequaisproprie-
dadesdefiniremtempodeexecu ção,comotambémjáiniciaoprocessodeinje ção
dedependências. Notranscorrerdestecapítuloadistânciaentreopadrão factory
enossocontainertenderáacresceratéchegarmosaopontoqueserãovistoscomo
primosdistantes.
Tipos de injeção
OSpringtrabalhacomdoistiposdeinje çãodedependências.Aqueexpomos
acimaéchamada injeção por setter (setter injection).Comoopróprionomediz,as
dependênciassãoinjetadasemnossobeanapartirdemétodos setterqueimplemen-
tamosemnossasclasses.Nossaoutraop çãoéainje çãoporconstrutor constructor
injection.
Paraentendermelhorainje çãoporconstrutor,imaginequenossaclasse Proces-
sadorpossuaumconstrutortalcomooabaixo:
40


## Página 51

CasadoCódigo Capítulo3. ConhecendooContainer
public Processador(FonteDados fonteDados, Impressor impressor) {
setFonteDados(fonteDados);
setImpressor(impressor);
}
Para executar a inje ção por construtor, entra em a ção a tag
<constructor-arg>quepodemosverema çãonoexemploabaixo:
<bean id="processador" class="br.com.casadocodigo.Processador">
<constructor-arg ref="fonteDados"/>
<constructor-arg ref="impressor"/>
</bean>
Assimcomoatag <property>, <constructor-arg>poderecebercomo
atributotanto valuequanto ref. Noexemploacima,aordemdedigita çãodas
tagsimporta.Reparequecoincidecomaordememqueosparâmetrossãopassados
aoconstrutordaclasse.Éimportantemencionarquetambémépossíveldigitá-los
foradaordem,masnestecasofaz-seobrigatóriaapresen çadoatributo indexque
devereceberumvalornuméricoquerepresenteaordemdoparâmetroapartirdo
zeronoconstrutor,talcomopodeservistonoexemploabaixo:
<bean id="processador" class="br.com.casadocodigo.Processador">
<constructor-arg ref="impressor" index="1"/>
<constructor-arg ref="fonteDados" index="0"/>
</bean>
Umaperguntapertinentenestemomentoéarespeitodarazãopelaqualexistem
estasduasop çõesdeinje ção. Umasónãotornariaoaprendizadodoframework
maissimples?Talvez,mascomcertezatambémotornariabemmaislimitado.Deve
serlevadoemconsidera çãoqueumdosobjetivosprincipaisportrásdoSpringé
oreaproveitamentodecódigolegadodemodoquesuaintegra çãosejaamaisleve
possível. Pormaisleve,comojámencionado,deveserentendido com o mínimo
possível de dependências com relação ao código fonte do próprio Spring.
Existeumalongadiscussãoarespeitodequalseriaamelhorformadeinje ção.
Osmaispuristasdefendemainje çãoporconstrutorcomoamelhor.Oargumento
équeaodefinirmosemumconstrutortodasasdependênciasdeumaclassetorna-
mosevidentequaisatributosnãodevememhipótesealgumaseralteradosapósa
instanciaçãodaclasse.Oproblemadestaabordageméqueconformenossocódigo
41


## Página 52

3.3. Declarandobeans CasadoCódigo
sedesenvolveenovosatributossãoincluídosemnossasclasses,onúmerodeparâ-
metrosaserpassadoparanossosconstrutorestendeacrescere,consequentemente,
suamanutençãovaisetornandomaiscomplicada.
Emproldainje çãoporsetterestãodoisargumentos:adequepermiteamodi-
ficaçãodasdependênciasinjetadasapósainstancia çãodaclasseetambémofatode
evitarproblemasdecorrentesdeconstrutorescomnúmeroexcessivodeparâmetros.
Nofinaldascontas,nemumanemoutraalternativaéamaisrecomendada.Qual
opçãousardevesempreserumadecisãotomadacombasenobomsenso,enão
apenasnoqueumguruououtroafirmaarespeitodoassunto.
Nadaimpedetambémqueusemostambémumasolu çãomistaenvolvendoos
doistiposdeinje çãodedependênciasemummesmobean.Aconfigura çãoabaixo
éumexemplodisto:
<bean id="processador" class="br.com.casadocodigo.Processador">
<constructor-arg ref="fonteDados" index="0"/>
<constructor-arg index="1">
<null/>
</constructor-arg>
<property name="impressor" ref="impressor"/>
</bean>
Nesteexemploreaproveitamosomesmoconstrutorpassandoovalor nullpara
osegundoargumentoeinjetandoadependência impressorvia setter.
Dando nome aos beans
Assimcomopessoaspossuemapelidos,omesmopodemosfazercombeans.Há
doisatributosdatag <bean>quepodemosusarparanomearmosnossoscompo-
nentes. Oprimeirojáconhecemos:trata-sede id. Usamosesteatributoquando
precisamosdefinirumnomeúnicoparanossosbeans.
Onovoatributosechama name,queéusadoquandodefinimosmaisdeum
nomeparaomesmobean. Nesteatributopodemosinclusiveincluirumalistade
nomes,quedevemestarseparadospelocaracteredeespa ço,pontoevírgulaouvír-
gula.Ocódigoabaixoexpõeumexemplodeusodestesatributos:
<!-- Um bean com dois nomes: um definido por id, outro por name -->
<bean id="impressor" name="impressorArquivo"
class="br.com.casadocodigo.ImpressorImpl"/>
<!-- Um bean com dois nomes, todos definidos na tag name -->
42


## Página 53

CasadoCódigo Capítulo3. ConhecendooContainer
<bean name="impressor, impressorArquivo"
class="br.com.casadocodigo.ImpressorImpl"/>
Apossibilidadedecriarmaisdeumnomeparaomesmobeanéumrecurso
poucousadonamaiorpartedosprojetos.Normalmenteestapossibilidadeéexplo-
radaemprojetosmaioresnosquaistimesdistribuídosdesenvolvempartesdosis-
temaqueserãointegradosposteriormente.Éumamaneirainteressantedemanter
ospadrõesdenomenclaturaadotadosportimesdistribuídos.Seseuprojetonãofor
tãograndeassimsimplesmentenãofazmaissentido,alémdeserbemmaisprodu-
tivoadotarumpadrãodenomesunificado.
Casoseuprojetonãopossuaumpadrãodenomenclatura,umaboapráticaéusar
oadotadoesugeridopelaequipedaSpringSource. Estasugerequebeanssigamo
padrãocamelcased,noqualonomesempreéinicialmentedigitadoemletrasminús-
culas.Casoonomesejacomposto,cadapalavraéseparadadigitandoseuprimeiro
caractereemletramaiúscula,talcomonestesexemplos: importador, importadorAr-
quivo, importadorBancoDeDados.
3.4 I nstanciação por factory method
Nemsempreéinteressantequeumbeansejainstanciadoporumconstrutorcomofi-
zemosatéomomento.Muitasvezesénecessárioqueestessejaminstanciadosusando
ummétodopresenteemumaclasse factory.
Factoryéumpadrãodeprojetocujadescri çãomaisfamosaseencontranolivro
“PadrõesdeProjeto:Soluçõesreutilizáveisdesoftwareorientadoaobjetos”daGoF
[4].Estapráticadedesenvolvimentoconsistenaimplementa çãodeumaclasse,cha-
mada factory(fabrica),cujoobjetivoéainstancia çãodenovosobjetos.Todaclasse
factorypossuipelomenosummétodoinstanciador( factory method)responsável
pelainstanciação(etalvezpreparo)denovosobjetos.
Nosoftwaredeexemploqueestamosusandonestecapítulopoderíamosterim-
plementadoumaclassefactorytalcomoaexpostanodiagramaabaixo:
43


## Página 54

3.4. Instanciaçãoporfactorymethod CasadoCódigo
Figura3.4:Exemplodeaplica çãodopadrãoFactory
Nesteexemplo,aclasse FactoryFonteDadospossuium factory methodchamado
criarFonteDadosquerecebecomoparâmetroumaStringrepresentandootipode
FonteDadosqueoclientedeseja.Aclasseclienteobtémcomoresultadoumainstân-
ciade FonteDadoscombasenoparâmetrofornecidoe,comisto,ficacompletamente
desacopladodetodasasimplementa çõesdestainterface,alémdetambémnãopre-
cisarsepreocuparcomqualquerlógicaquepossasernecessárianaimplementa ção
destesobjetos.
NaAPIJDBCdoJavatambémpodemosverumaaplica çãodestepadrão,tal
comonoexemploabaixo:
import java.sql.*
// Ignorando início do código
Class.forName("com.mysql.jdbc.Driver");
Connection con =
DriverManager.getConnection("jdbc:mysql://localhost/database");
OmétodogetConnectiondaclasse DriverManageréumaimplementaçãodopa-
drão Factory.Éimportanteobservarque factory methodsnãoprecisamreceberpa-
râmetros.Interessanteobservaraaplica çãoaquidoconceitodeinversãodecontrole:
delegamosàclasse factoryaresponsabilidadedeescolherqualaimplementa çãocor-
retade FonteDadosaserobtida,oque,deoutramaneira,caberiaàclassecliente,cujo
44


## Página 55

CasadoCódigo Capítulo3. ConhecendooContainer
acoplamentoàsdemaispartesdosistemaseriabemmaior.
Ainstanciaçãodebeansapartirdeum factory methodpodesedardeduasma-
neiras: usandoummétodoestáticoounão. Tendocomobaseoexemploexposto
nobox Factorypodemosvernocódigoabaixocomodeclararainstancia çãodeum
beanapartirdeummétodoestático.
<bean id="fonteDadosEstatico"
class="br.com.casadocodigo.FactoryFonteDados"
factory-method="criarEstatico">
<constructor-arg index="0" value="arquivo"/>
</bean>
Emnossaclasse FactoryFonteDadosimplementamosométodoestático criarEs-
taticodetalmodoquerecebacomoparâmetroumnomequeidentifiquequaltipo
de FonteDadosdeveserinstanciada. Seovalorforiguala arquivo,seráretornada
umainstânciade FonteDadosArquivo,eseforrandômico, FonteDadosRandomico.
Éimportanteobservarque,apesardenossoobjetivoseraobten çãodeumains-
tânciade FactoryMethod,oatributo classdatag <bean>recebecomovalornão
onomedeumaclassequeimplementeestainterface,massimonomedanossa
classe factory.Dadoqueométodoestáticorecebeparâmetros,reaproveitamosatag
<constructor-arg>,passandocomovalorotipodebeanquedesejamoscomo
retorno.
Usarummétodonãoestáticoéigualmentesimples.Bastaqueo factory method
aserinvocadoestejaimplementadoemalgumoutrobeandeclaradoemnossoar-
quivodeconfigura ção.Noexemploabaixopodemosverumexemplodestetipode
configuração.
<!-- O bean que contém nosso factory method -->
<bean id="factory" class="br.com.casadocodigo.FactoryFonteDados"/>
<bean id="fonteDadosInstancia" factory-bean="factory"
factory-method="criar">
<constructor-arg index="0" value="randomico"/>
</bean>
Observequenestecasonãoénecessárioincluiroatributo classnatag <bean>
quandodeclaramosobean fonteDadosInstancia.Arazãoésimples:nestecasonão
fazsentido,dadoqueotiposerádecididoemtempodeexecu çãoeoSpringnãotem
como,deantemão,saberqualseriaeste.
45


## Página 56

3.5. Mapeandoatributoscomplexos CasadoCódigo
Finalmente, para declarar um bean a ser instanciado por umfactory
method que não receba parâmetros como valor, basta não incluir mais a tag
<constructor-arg>,comopodeservistonoexemploabaixo:
<bean id="fonteDadosArquivo" factory-bean="factory"
factory-method="criar">
<property name="arquivo" value="/caminho/para/arquivo"/>
</bean>
Éimportanteobservarqueainstancia çãopormétodosinstanciadoresnãonos
impededeinjetarvaloresnosatributosdenossosbeans,comopodeservistono
nossoúltimoexemplo.
3.5 M apeando atributos complexos
OformatoXMLnospermitedefinirintegralmenteoestadoinicialdenossosbeans.
Istoimplicaqueatag <property>ébemmaisqueoquemostramosatéestemo-
mento.Esta,alémdepossibilitardefinirmosovalordeatributosprimitivosestrings
tambémpossibilitaomapeamentodeatributoscomplexoscomolistas,mapas,ins-
tânciasdejava.util.Propertiesearrays.Eestassãoapenasalgumasdaspossibilidades
queiremosexpornestase ção.
Listas
Imagineumaimplementa çãodainterface FonteDadostalcomoaabaixo:
class FonteDadosArquivos implements FonteDados {
private List<String> arquivos;
public List<String> getArquivos() {return arquivos;}
public void setArquivos(List<String> lista) {arquivos = lista;}
// restante da classe ignorado para aumentar a clareza
}
Paramapearumalistadestrings,atag <property>aceitaemseuinterioratag
<list>,quepodemosserusadanocódigoabaixo:
<bean class="br.com.casadocodigo.FonteDadosArquivos">
<property name="arquivos">
<list>
<value>/caminho/para/arquivo1.csv</value>
46


## Página 57

CasadoCódigo Capítulo3. ConhecendooContainer
<value>/caminho/para/arquivo2.csv</value>
<value>/caminho/para/arquivo3.csv</value>
</list>
</property>
</bean>
Atag <value>éusadapararepresentarumvalorprimitivoou String.Podería-
mostambémterusadoatag <array>aoinvésde <list>eobteríamosomesmo
resultado.Ambasinjetariamumobjetodotipo java.util.ArrayListnoatributo arqui-
vosdobean.
Imagineagoraquetenhamosalteradonossaimplementa çãodaclasse FonteDa-
dosArquivosparaqueseuatributo arquivosnãorecebaumalistadestrings,massim
umalistadeinstânciasdotipo java.io.Filetalcomonosnippetabaixo:
class FonteDadosArquivos implements FonteDados {
private List<java.io.File> arquivos;
//restante da classe ocultado para facilitar a leitura
}
Atag <list>tambémaceitaemseuinterioratag <bean>. Sendoassim,é
possíveldeclararbeansanônimostalcomonoexemploabaixosemproblemaalgum.
<bean class="br.com.casadocodigo.FonteDadosArquivos">
<property name="arquivos">
<list>
<bean class="java.io.File">
<constructor-arg value="/caminho/para/arquivo1"/>
</bean>
<bean class="java.io.File">
<constructor-arg value="/caminho/para/arquivo2"/>
</bean>
<bean class="java.io.File">
<constructor-arg value="/caminho/para/arquivo3"/>
</bean>
</list>
</property>
</bean>
Casoosbeansnãofossemanônimos,outratagútiléatag <ref>,queaponta
paraareferênciadeumbeanexterno,talcomonoexemploabaixo:
47


## Página 58

3.5. Mapeandoatributoscomplexos CasadoCódigo
<list>
<ref bean="beanArquivo1"/>
<ref bean="beanArquivo2"/>
</list>
Mapas
Umaoutraimplementaçãodainterface FonteDadospoderiatersuasfontesdeda-
dosmapeadasportipoemumaestruturadotipo java.util.Maptalcomonoexemplo
abaixo:
public class FonteDadosMapaArquivos implements FonteDados{
private Map<String, Object> mapa;
public Map<String, Object> getMapa() {return mapa;}
public void setMapa(Map<String, Object> valor) {mapa = valor;}
// restante oculto para maximizar a clareza do exemplo
}
Entraema çãoatag <map>,queusaríamosparamapearoatributo mapada
classeacimadaseguintemaneira:
<bean name="fonteDadosMapa"
class="br.com.casadocodigo.FonteDadosMapaArquivos">
<property name="mapa">
<map>
<entry key="arquivo">
<ref bean="arquivo"/>
</entry>
<entry key="arquivoString"
value="/caminho/para/arquivo.csv"/>
</map>
</property>
</bean>
Nointeriordatag <map>incluímosumalistadeelementosdotipo <entry>
que,comoopróprionomeindica,representamumaentradanomapa. Oatributo
keyde <entry>identificasuachave. Emseuinteriorsãoaceitoselementosdos
tipos <ref>, <bean>, <value>, <list>, <array>e <map>.
48


## Página 59

CasadoCódigo Capítulo3. ConhecendooContainer
Properties
UmdosobjetosmaisusadosdaAPIJavapadrãoéaclasse java.util.Properties.
Comojáeradeseesperar,oformatoXMLdoSpringoferecesuporteespecialaesta
classe. Umexemplopráticoéaclasse SessionFactorydoHibernateparaaqualo
framework,comoveremosmaisadiantenolivro,integra-semuitobem.
OsnippetXMLabaixoéquaseautoexplicativo:
<bean id="sessionFactory"
class="org.springframework.orm.hibernate.LocalSessionFactoryBean">
<!--
Restante oculto para que possamos
focar apenas no mapeamento de propriedades
-->
<property name="hibernateProperties">
<props>
<prop key="hibernate.dialect">
org.hibernate.dialect.MySQL5InnoDBDialect
</prop>
<prop key="hibernate.hbm2ddl.auto">update</prop>
</props>
</property>
</bean>
Atag <props>representaumobjetodotipoProperties.Emseuinterioréaceita
atag <prop>que,comoopróprionomejádiz,éusadaparamapearasproprieda-
desaceitaspeloobjeto. Nointeriordatagéincluídoovalordapropriedadeque
queremosmapear.
3.6 U sando o container
Comadefini çãodenossosbeansprontachegouomomentodeusá-los,ouseja,fi-
nalmenteveremoscomoinstanciareusarnossocontainer.Mencioneianteriormente
queocontainerdoSpringpossuivêmemduasversões: BeanFactorye Application-
Context.Qualusar?
AequipedaSpringSourcejánosrespondeistonaprópriadocumenta çãodopro-
jeto[14]:ousodo BeanFactorysósejustificaemsitua çõesnasquaisasrestri ções
computacionaissejamextremascomo,porexemplonaimplementa çãodeapplets
Java.Naprática,entretanto,adiferen çanoconsumoderecursosentreasduasver-
sõesémínima,oquetornaseuusodesnecessário. Entraapergunta: sepossoter
49


## Página 60

3.6. Usandoocontainer CasadoCódigo
tudo,porquemerestringiraomínimo?Sendoassim,nodecorrerdestelivrousare-
mosapenaso ApplicationContext.
Atualmente BeanFactoryaindaexisteapenasparafinsderetrocompatibilidade.
Dadoqueainterface ApplicationContextaestendeeaprópriaSpringSourceade-
saconselha,usaremosapenas ApplicationContextcomonossocontainerdaquipara
frente.
Instanciando o container
Parausarmosocontainernossoprimeiropassoéinstanciá-lo.Dasdiversasva-
riaçõesde ApplicationContext,nossofocoinicialseráemapenasduasquesão Clas-
sPathXmlApplicationContexte FilePathXmlApplicationContext.Adiferen çaentreos
doisestáapenasnafontequeseráusadaparaobterosdocumentosXMLresponsáveis
pelaconfiguraçãodenossosbeansquesãorespectivamenteo classpathdaaplicação
eosistemadearquivoslocalaondenossoprojetoseráexecutado.
Figura3.5:HierarquiadosApplicationContexts
OconstrutormaisusadorecebecomoparâmetroumaStringrepresentandoa
localizaçãodoarquivodeconfigura ção.Oexemploabaixoinstanciaumcontainer
quebuscaoarquivospring.xmlapartirdoclasspathdaaplica ção.
import org.springframework.context.ApplicationContext;
import
org.springframework.context.support.ClassPathXmlApplicationContext;
(...)
50


## Página 61

CasadoCódigo Capítulo3. ConhecendooContainer
ApplicationContext context =
new ClassPathXmlApplicationContext("spring.xml");
Obtendo beans (lookup)
Ainterface ApplicationContextnãopoderiasermaissimples:dadanossaconfi-
guraçãoanterior,sedesejássemosobterobean processadorapartirdoseuidentifi-
cadorbastausarafun ção getBeancomonoexemploabaixo:
ApplicationContext context =
new ClassPathXmlApplicationContext("spring.xml");
Processador bean = (Processador) context.getBean("processador");
bean.processe();
Existembasicamenteduasversõesdométodo getBeanquepodemserusadas
quandonossoobjetivoéobterumbeanapartirdoseunome.
// a versão mais primitiva que nos obriga a fazer um type casting manual
Processador bean = (Processador) context.getBean("processador");
// Usando generics
Processador bean = context.getBean("processador", Processador.class);
Comomencionadoacima,nemsempredamosnomesaosnossosbeans.Nestes
casos,obtemosobeansobreoqualiremostrabalharpassandocomoparâmetroa
classeouinterfacedoobjetodesejado.
// buscando pela classe
Processador bean = context.getBean(Processador.class);
Hátambémsituaçõesemqueporrazõesdiversasprecisamosdemaisdeum
beanquerealizemumamesmaclasseouinterfaceeprecisamosprocessaralgumas
outodasestasinstâncias.Entraema çãoavariante getBeansOfType,queretornaum
mapanoqualachaverepresentaoidentificadorúnicodecadaumdosbeansobtidos.
Map<String, Processador> beans =
context.getBeansOfType(Processador.class);
Oleitoratentonestepontopodeseperguntar: oqueocorrequandopedimos
umbeanquenãoexista? Nestasitua çãoocontainerdisparaumaexce çãodotipo
org.springframework.beans.BeansExceptiondaqualpodemostiraralgumproveito
comonoseguintetrecho:
51


## Página 62

3.7. Ociclodevidadocontainer CasadoCódigo
Processador processador = null;
try {
processador = context.getBean("processador");
} catch (org.springframework.beans.BeansException ex) {
// instancie um processador de emergência
// caso nenhum esteja disponível no container
processador = new Processador();
// prepare-o a gosto :)
}
Éimportantemencionarque BeansExceptionéumaexceçãodetempodeexecu-
ção(nãochecada)e,portanto,vocênãoprecisaincluirtodaobten çãodeumbean
dentrodeumbloco try..catch.Casoocorraalgumerroduranteainstancia ção,inje-
çãodedependênciasougerênciadeciclodevidadosbeansnormalmenteéfatal.
Epormaisincrívelquepare ça,conhecendoapenasestasvariantesdosmétodos
de lookupodesenvolvedoriniciantejáconseguetrabalhar(ebem)comocontainer
doSpring.
3.7 O ciclo de vida do container
AcabamosdeverdeumamaneirabastanterústicacomotrabalharcomoSpring.Ba-
sicamentedeclaramosnossosbeansemnossoarquivodeconfigura ção,instanciamos
nossocontainercomestaeemseguidaexecutamoschamadasafun çõesdelookup
paraquepossamostrabalharcomnossosbeans.Obviamenteofuncionamentoreal
doSpringébemmaisricoeofereceumagamabemmaiordepossibilidadesaode-
senvolvedor.
Ofuncionamentorealdocontainerpodesermelhorcompreendidoobservando
odiagramaabaixo:
52


## Página 63

CasadoCódigo Capítulo3. ConhecendooContainer
Figura3.6:Ociclodevidadeumcontainer
Ocontainerassimcomoobeanpossuiseuprópriociclodevidaqueinicia-seno
momentoemqueesteéinstanciadoealimentadocomnossasconfigura ções.Cada
declaraçãodebeanqueescrevemosdaráorigemaumobjetodotipo BeanDefinition.
Estaclasseencontra-seimplementadanomódulo Beanseéaresponsávelporrepre-
sentarinternamenteomodocomodefinimosaconfigura çãodecadaumdenossos
beans.
Parafacilitarasuacompreensãoéinteressantepensarnaclasse BeanDefinition
comoa receitaseguidapeloSpringnogerenciamentodosbeansmanipuladospelo
container. BeanDefinitiondizaocontainerqualclasseinstanciar,quaisatributosde-
verãoserpreenchidos,asdependênciasasereminjetadasecomodevesertratadoo
ciclodevidadecadabean.
Comtodasestasinforma çõesemmemóriaseprontasparauso,inicia-seociclo
devidadosprópriosbeans,queserãoinstanciadosedestruídosconformesejane-
cessário. Oleitoratentopode-seperguntarnestemomento: quando um bean deve
ser criado ou destruído e como isto é definido?,oqueéoassuntodapróximase ção.
3.8 E scopos
Quandoumbeandeveserinstanciadooudestruídoequantasinstânciaspodemser
criadasédefinidopeloseuescopo( scope).Umdosobjetivosdocontainerétirardas
mãosdodesenvolvedoraresponsabilidadepelainstancia çãodosobjetos.
OescopopadrãodoSpringéo singletone,portanto,éaqueleadotadoemtodos
osbeansquandonãodefinimosnossosescoposexplicitamente.Umbeandeclarado
comesteescopoéinstanciadoumaúnicavezpelocontaineremantidoemmemória
atéqueocontainersejadestruído.Antesdeexporasop çõesoferecidaspeloSpring
53


## Página 64

3.8. Escopos CasadoCódigo
éinteressantepensarmosemalgumasquestõesquenosajudamaescolheraop ção
corretadeescopoparanossosbeans.
Quão cara é a construção de um bean? -Imagineumbeanquerepresenteum
objetocarodeserinstanciadoeconfiguradocomoporexemploumpooldeconexões
ouum EntityManagerJPA.Estessãoostiposdeobjetoquequeremosverconstruídos
umaúnicavezduranteaexecu çãodenossossistemasenãotodavezquesetornam
necessáriosporrazõesdeperformance.
O estado interno de um objeto pode ser compartilhado por mais de um usuário do
sistema?-Nodesenvolvimentodeaplica çõescorporativas acesso concorrenteéum
dosmaioresproblemasaserresolvido.Emsuaraizestáoestadocompartilhadoque
éaprincipalrazãoportrásdesolu çõescomomecanismosdesincroniza ção. Ima-
ginequenoexemplodenossocapítulocadainstânciade Processadorparaexecutar
seutrabalhoparaumusuárioprecisepossuirumestadoúnicoparaaqueleusuário.
Agoraimaginequeainstânciadeumusuáriosejacompartilhadaporoutro. Uma
sériedeconsequênciasinesperadaspoderiamocorrer.Aescolhadoescopocorreto
paranossosbeansevitaestetipodesitua çãodeumaformabastantesimples.
Quanto tempo uma instância realmente deve existir?-Oquenosvoltaàpri-
meiraquestão:objetoscujainstancia çãosejacaranormalmenteduramotempode
execuçãodosistema.Noentantonãoéinteressantequealgunsobjetosduremmuito
maisqueumarequisi ção.Porexemplo:umobjetoquecontenhaosdadosdigitados
emumformuláriowebnãoéfeitoparaqueduremaisdoqueumconjuntofinito(e
preferencialmentepequeno)derequisi ções.
Estestrêsquestionamentosabrangemamaiorpartedosproblemascomosquais
precisamosnospreocuparnomomentoemquedefinimosoescopodenossosbeans.
Mantendo-asemmente,éhoradeapresentarosescoposqueoSpringnosoferece
porpadrãoecomoinstruirnossocontaineraaplicá-losemnossosobjetos.
Singleton
Trata-sedoescopopadrãoaplicadopeloSpring.Garantequeapenasumains-
tânciadobeansejainstanciadapelocontainerecompartilhadaportodososoutros
beansqueausemcomodependência.Érecomendadanoscasosabaixo:
• Aconstruçãodoobjetoécara,comoporexemploumpooldeconexões,oob-
jeto SessionFactorydo Hibernateouo EntityManagerdoJPA.Nestescasos,é
interessantemanteramesmainstânciadoobjetocompartilhadaportodosos
54


## Página 65

CasadoCódigo Capítulo3. ConhecendooContainer
objetosclientesdosistema,garantindoassimquesuainstancia çãonãopreju-
diqueaperformancedosistemacomoumtodo.
• Oestadodoobjetopodesercompartilhadopormaisdeumobjetoclientesem
problemaouentãoéinteressantequeoestadosejacompartilhadopormaisde
umobjeto.
Nonossoexemploobean fonteDadoséumcasoemqueoescoposeaplicabem.
Comoéumafontededados,internamenteestaclassepoderiateralgummecanismo
decacheamentoquefavorecessechamadassubsequentesaosmétodosdepesquisa
implementados.Éinteressanteobservarqueoescoponoentantonãofoiaplicadoao
bean impressor,vistoquenãodesejamosqueseuestadointernosejacompartilhado
pormaisdeumobjetoclientedamesma.
Paradeclararumbeancomoumsingletonháduasop ções:vocêpodenãofazer
nadavistoseroescopopadrãousadopeloSpringouincluirnadefini çãodesteo
atributo scopecomovalor singletontalcomonoexemploabaixo:
<bean id="fonteDados" class="br.com.casadocodigo.FonteDadosArquivo"
scope="singleton">
<property name="arquivo" value="/arquivos/pessoas.csv"/>
</bean>
Ocódigoabaixoilustrabemocomportamentodoescopo singleton.
FonteDadosArquivo fonteDados1 =
context.getBean("fonteDados", FonteDadosArquivo.class);
FonteDadosArquivo fonteDados2 =
context.getBean(FonteDadosArquivo.class);
// O teste abaixo falharia caso fonteDados1
// e fonteDados2 fossem instâncias diferentes
assert fonteDados1 == fonteDados2;
Prototype
Oescopo prototypegarantequetodavezqueocontainerrecebaumarequisi ção
porumbeanumanovainstânciasejacriada.Énormalmenteadotadoemsitua ções
nasquaisobeantenhacurtadura ção.Seuuso,deacordocomasquestõesqueapre-
sentamosacimasefazrecomendadoquando:
• Aconstruçãodoobjetoébarata.
55


## Página 66

3.8. Escopos CasadoCódigo
• Oseuestadonãodevesercompartilhadopormaisdeumaclassecliente
• Oobjetosejaútilporumcurtoespaçodetempo
Definimosumbeancomo prototypepassandoovalordemesmonomedocon-
textoparaoatributo scopetalcomonoexemploabaixo:
<bean id="processador" class="br.com.casadocodigo.Processador"
scope="prototype">
<property name="impressor" ref="impressor"/>
<property name="fonteDados" ref="fonteDados"/>
</bean>
Assimcomonocasodoescopo singleton,podemosescreverumtestebastante
simplesparailustrarseufuncionamento:
Processador processador1 =
context.getBean("processador", Processador.class);
Processador processador2 =
context.getBean(Processador.class);
// O teste abaixo falharia caso estivéssemos lidando
// com a mesma instância
assert processador1 != processador2
Request e Session
ParaoambientewebSpringnosoferecemaisdoisescoposbastanteinteressantes
quesão requeste sessionquemantémumainstânciadobeanduranteaexistência
respectivamentedeumarequisi çãoedeumasessãodeusuário. Comotrataremos
dodesenvolvimentoparaesteambienteapenasposteriormentenestelivro,iremos
exporaquiapenasumexemplodecomodeclaramosbeansnesteescopo.
<!-- Usando o escopo de sessão -->
<bean id="processador" class="br.com.casadocodigo.Processador"
scope="session"/>
<!-- Usando o escopo de requisição -->
<bean id="processador" class="br.com.casadocodigo.Processador"
scope="request"/>
Éumexcelenteexemplodecomooescopoevitaproblemasdeacessoconcor-
renteemnossocódigo.Usandooescopodesessão,cadausuáriodosistemapossui
56


## Página 67

CasadoCódigo Capítulo3. ConhecendooContainer
suaprópriainstânciadobean,cujoestadodizrespeitoapenasaoqueaqueleusuário
estáfazendonaquelemomento.
Escopos customizados
Os quatro escopos acima são os mais comumente usados pelo Spring Fra-
mework e conseguem atender à maior parte dos casos. Uma das característi-
cas mais interessantes do Spring é sua flexibilidade. Sendo assim, caso ocorra
uma situação na qual os escopos oferecidos não lhe atendam, é possível criar
seupróprioescopo, bastandoparatalescreverumaimplementa çãodainterface
org.springframework.beans.factory.config.Scope.
Aescritadeescoposcustomizadosnormalmenteéfeitapordesenvolvedoresres-
ponsáveispelaimplementaçãodenovosframeworksoubibliotecasquedesejemadi-
cionarsuporteespecialaoSpringFramework.Émuitoútilemcontextosnosquais
énecessáriomanterosbeanssomenteenquantodeterminadotipodeconversa ção
estejaocorrendocomo,porexemplo,emsitua çõesnasquaissejanecessáriotratar
transaçõesdistribuídasouintegra çãocomsistemasremotos.
Trata-sedeumusobastanteespecíficoquefogedoobjetivodestelivroe,por-
tanto,ficaaquiapenasamen çãoaestapossibilidadeoferecidapeloframework.
3.9 I nstanciação tardia
Porpadrãoasimplementa çõesde ApplicationContextinicializamtodososbeansde
escopo singletonquandosuaconfigura çãoéparseada. Estaéumapráticabastante
sadia,vistoquecasoocorraalgumproblemanesteprocessoodesenvolvedoréime-
diatamenteavisadodoproblema,oquetornaestecomportamentoumaimportante
ferramentanaetapadedesenvolvimentodenossosprojetos. Noambientedepro-
duçãoahistóriaédiferente:hábeanscujainicializa çãono startupdosistemanãoé
necessáriaoumesmodesejável.Éocasodebeanscujousoocorresomenteumbom
tempoapósainicializa çãodosistema sedefatochegaremaserusados.
Nestassituaçõesfazsentidopostergarainicializa çãodocomponentesomente
paraquandoestadefatosefizernecessária.Comistodiminuímosotempode boot
dosistemaeaindaeconomizamosmemória.Beanscominicializa çãotardiasãocha-
madospelaequipedaSpringSourcede lazy-initialized beans.NoformatoXMLhá
duasmaneirasdedefinirestecomportamento.Aprimeiraéadicionandooatributo
lazy-initnatag <bean>comovalor truecomonocódigoabaixo:
<bean id="fonteDados" class="br.com.casadocodigo.FonteDadosArquivo"
57


## Página 68

3.10. Aproveitandoociclodevidadosbeans CasadoCódigo
lazy-init="true"/>
A segunda maneira consiste em definir o comportamento padrão para to-
dos os beans definidos no arquivo de configuração adicionando o atributo
default-lazy-initnatag <beans>talcomonocódigoabaixo:
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd"
default-lazy-init="true"
>
<!-- Conteúdo omitido para aumentar a clareza -->
</beans>
Destemodo,osbeanssóserãoinicializadosquandoforemusadospelaprimeira
vez.
3.10 A proveitando o ciclo de vida dos beans
Ofatodedelegarmosaresponsabilidadepelainstancia çãoedestrui çãodenossos
beansaocontainernãoimplicaquenãopossamosoudevamostirarproveitodociclo
devidadosmesmos. Todobeantem“direito”adoismétodosdecallbackquesão
executadospelocontainerlogoapóssuainicializa çãoeantesdesuadestrui çãotal
comopodeservistonociclodevidaampliadoquepodeservistonaimagemabaixo.
Figura3.7:Ociclodevidadobean
58


## Página 69

CasadoCódigo Capítulo3. ConhecendooContainer
Iremosverduasmaneirasdetirarproveitodestesmétodos:umaéapesadaatra-
vésdaimplementaçãodeinterfaces,enquantoaoutraéaleveusandoapenasosme-
canismosdeconfigura çãodocontainer.
Inicialização do bean
Talvezsejainteressanteque,umaveztenhamsidoinjetadastodasasdependên-
ciasemseuobjetoalgumcódigodeinicializa çãosejaexecutado.Porexemplo:para
garantirumtempoderespostamenor,nossobean fonteDadospoderia,logoapósser
iniciadojácarregartodososregistrospresentesemumarquivodenossoservidor.
Comomencionado,nestecasoháduasalternativas.
Aprimeiraalternativaéaquechamamosde pesada,vistoqueenvolveaim-
plementaçãodainterface org.springframework.beans.factory.InitializingBeane,por-
tanto,adicionaaonossoprojetoadependênciafísicaaumaclassedoSpringFra-
mework.Podemosmodificarnossaclasse FonteDadosRandomicoportantoparaque
fiquesimilaraocódigoabaixo:
import org.springframework.beans.factory.InitializingBean;
public class FonteDadosArquivo implements FonteDados, InitializingBean {
// O método da interface que precisa ser implementado
public void afterPropertiesSet() throws Exception {
// Código responsável pelo pré-carregamento dos dados
}
// Restante da classe ignorado para facilitar a leitura
}
Onomedoúnicométodoaserimplementadoporestainterfaceébastanteins-
trutivo: afterPropertiesSet.Umavezqueoprocessodepreparoeinje çãodedepen-
dênciasdobeanestejacompletoestemétodoseráinvocadopelocontainer. Como
mencionadoanteriormente,umadasvantagensobtidasapartirdestemétododecall-
backéqueevitamosumasériedeproblemasquepoderíamosenfrentaremsitua ções
nasquaisumobjetoéusadoantesdesercompletamenteinicializado.Nossobeansó
estarádisponívelparausoapartirdomomentoemqueestemétodoforexecutado.
Asegundaalternativa,eamaisrecomendávelpormanternossocódigocom-
pletamentedesacopladodoSpringenvolvealterarmosapenasosnossosarquivosde
configuração.Bastaadicionarmosoatributo init-methodàtag <bean>comoé
feitonoexemploabaixo:
<bean id="fonteDados" class="br.com.casadocodigo.FonteDadosArquivo"
init-method="init"/>
59


## Página 70

3.10. Aproveitandoociclodevidadosbeans CasadoCódigo
Háumaúnicaregranestecaso:ométododeveserdotipo voidenãoreceber
nenhumargumentocomovalor. Casoométodonãoexistaumaexce çãodotipo
org.springframework.beans.factory.BeanCreationExceptionserálançadainformando
aausênciadométododeclarado.
É possível minimizar a quantidade de configurações a ser digitada e ainda
padronizar o comportamento do seu projeto inteiro adicionando o atributo
default-init-methodàtag <beans>comonoexemploabaixo:
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd"
default-init-method="init">
<!-- Ocultado o conteúdo para facilitar a leitura -->
</beans>
Amesmacondi çãodoatributo init-methodémantida.Casoométodoexista
emqualquerumdosbeansdeclarados,esteseráexecutado. Casoométodonão
exista,nenhumaexce çãoserádisparada.Éimportantemencionarqueapresen çado
atributo init-methodemumatag <bean>sobrescreveocomportamentopadrão
quedefinimosnatag <beans>.
Finalizando um bean
Hámomentosemqueéinteressanteexecutaralgumcódigonomomentoemque
nossosbeanssãofinalizados.Estenormalmenteéopontoemquesãoexecutadasas
operaçõesdelimpezacomoporexemplolibera çãoderecursosoumesmooenvio
demensagensparasistemasremotosinformandoofatodedeterminadoobjetoestar
sendodeposto.Basicamenteomesmoprocedimentoqueaplicamosnocallbackde
inicializaçãoserárepetido.
A primeira opção e menos recomendada é a implementação da interface
org.springframework.beans.factory.DisposableBean.Umexemplodesuaimplemen-
taçãopodeservistonocódigoabaixo:
import org.springframework.beans.factory.DisposableBean;
public class FonteDadosArquivo implements FonteDados, InitializingBean {
// O método da interface que precisa ser implementado
public void destroy() throws Exception {
// recursos são liberados e operação de limpeza executada
60


## Página 71

CasadoCódigo Capítulo3. ConhecendooContainer
}
// Restante da classe ignorado para facilitar a leitura
}
Háumúnicométodoaserimplementadoqueéo destroy.Éinteressanteobservar
quenestecasotemosumavantagememcimadoprópriocomportamentopadrãoda
linguagemJava,naqualpodemosatéimplementarmétodosdestrutoresemnossas
classes,masnãotemoscertezadequandoemesmoseesteserádefatoexecutado.
Temosaquiumaprevisibilidadebemmaiorarespeitodaexecu çãodonossométodo
destrutor.
A opção mais recomendada para obter é quase idêntica à que adotamos
no caso do callback de inicialização. Na tag <bean>adicionamos o atributo
destroy-methode,sequisermospadronizaraexecu çãodométododefinaliza-
çãoemtodososbeans,éincluídooatributo default-destroy-methodàtag
<beans>.Asmesmasregrasmencionadasparaométododecallbackdeinicializa-
çãoseaplicamnestecaso.Ocódigoabaixoexpõeumexemplodestaconfigura ção:
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd"
default-destroy-method="destroy">
<bean id="fonteDados" class="br.com.casadocodigo.FonteDadosArquivo"
destroy-method="cleanup"/>
</beans>
Éimportantedeixaraquiumanotaarespeitodocomportamentodosmétodos
decallbackdedestrui çãoquandoobeanpossuiescopo prototype.Estesbeansnão
possuemasuafinaliza çãogerenciadapelocontainer:sãoapenasinicializadoseem
seguidaexcluídosdomesmo,nãosendocacheadoscomoocorrecomosdemaises-
coposqueforamapresentadosanteriormente.
3.11 Q uando o bean conhece seu container
Apesar de um dos objetivos principais do Spring é ser o mais desacoplado
possível de nossas classes de negócio, há momentos em que é interessante
a existência de algum acoplamento nesta direção. É muito fácil tornar um
61


## Página 72

3.11. Quandoobeanconheceseucontainer CasadoCódigo
bean consciente de sua condição. Basta que sua classe implemente a inter-
face org.springframework.context.ApplicationContextAwarecaso estejamos traba-
lhandocomumcontainerdotipo ApplicationContextouimplementeainterface
org.springframework.beans.factory.BeanFactoryAwarecasoestejamoslidandocom
umcontainerdotipo BeanFactory.
Ambasasinterfacespossuemapenasummétodoquedeveserimplementadotal
comoexpostonocódigoabaixo:
public interface ApplicationContextAware extends Aware {
void setApplicationContext(ApplicationContext applicationContext)
throws BeansException;
}
public interface BeanFactoryAware extends Aware {
void setBeanFactory(BeanFactory beanFactory) throws BeansException;
}
Umbomexemplodeusodestecomportamentoocorrequandoumbeandotipo
prototypeacidentalmentesetornaum singleton,talcomopodeserobservadonacon-
figuraçãoabaixo:
<bean id="impressor" class="br.com.casadocodigo.ImpressorImpl"
scope="prototype"/>
<bean id="processador" class="br.com.casadocodigo.Processador"
scope="singleton">
<property name="impressor" ref="impressor"/>
</bean>
Apesardobean impressorserdeclaradocomo prototype,umadesuasinstâncias,
aquelaaserinjetadanobean impressorseráum“singletonacidental”,dadoquetodo
beanpertencenteaoescopo singletonsóéinstanciadoumavez.Esenossobean pro-
cessadorsempreprecisardeumanovainstânciade impressor?Umasolu çãoparaeste
problemaétorná-loconscientedoseucontainerimplementandoainterface Appli-
cationContextAware.
Dadoquetodo ApplicationContextnarealidadeestendeainterface BeanFactory,
aoimplementarmosainterface BeanFactoryAwareestaremostornandonossaclasse
independentedotipodecontainer. Podemosalterarseucódigofonteparaquefi-
quesimilaraocódigoabaixooque,aomenosemteoria,resolveriaoproblemado
“singletonacidental”.
62


## Página 73

CasadoCódigo Capítulo3. ConhecendooContainer
public class Processador implements BeanFactoryAware {
private BeanFactory beanFactory;
public void setBeanFactory(BeanFactory bf) throws BeansException {
this.beanFactory = bf;
}
/* Resolvido o problema. Agora sempre será
retornada uma nova instância de Impressor,
e a declaração desta dependência em nosso arquivo de configuração
se torna desnecessária.*/
public Impressor getImpressor() {
return beanFactory.getBean(Impressor.class);
}
}
3.12 M odularizando a configuração
Conformenossosistemavaisedesenvolvendonovosbeansvãoaparecendoe,conse-
quentemente,otamanhodosnossosarquivosdeconfigura çãoaumentam.Éimpor-
tantelembrarqueacomplexidadenãoseencontraapenasemnossocódigofonte,
mastambémnosnossosartefatosdeconfigura ção.Senãohouverumasolu çãoade-
quadaparaquepossamosmelhororganizaromodocomodeclaramosnossosbeans
comcertezaamanuten çãodonossosoftwareseráaltamentecomprometida.
OSpringnospermitemodularizarnossosarquivosdeconfigura ção.Assimpo-
demosorganizarnossosbeansdemaneiralógicafacilitandoamanuten ção.Éuma
práticacomum,porexemplo,terumarquivoapenasparaadeclara çãodebeansde
acessoadados,outroparagera çãoderelatórioseporassimemdiante. Casosua
configuraçãosejamodular,todasasimplementa çõesde ApplicationContextofere-
cemumconstrutorquerecebecomoparâmetroumarraydestringsrepresentando
alocaliza çãodosseusarquivosdeconfigura ção. Noexemploabaixopodemosver
umexemplodesteconstrutornaclasse ClassPathXmlApplicationContext.
ApplicationContext context =
new ClassPathXmlApplicationContext({"spring-daos.xml",
"spring-relatorios.xml", "spring-processamento.xml"});
Umavezinstanciado,ocontainerirámesclarinternamenteostrêsarquivos,de
talformaque,naprática,todossetornamnarealidadeumsó.Étambémpossível
63


## Página 74

3.13. Aplicandoherançanadefini çãodosbeans CasadoCódigo
queumarquivodeconfigura çãoimporteoconteúdodeoutro.Paratal,usamosatag
<import>.Estapreferencialmentedeveserincluídanoiníciodoarquivoqueestáa
importarumnovorecurso,epossuiumúnicoatributo: resource,cujovalordeve
serocaminhorelativoaoarquivoaserimportado.Podemosverumexemplodoseu
usonocódigoabaixo:
<!-- A definição do bean fonteDadosInstancia fica no
arquivo spring-factory.xml -->
<import resource="spring-factory.xml"/>
<bean id="impressor" class="br.com.casadocodigo.ImpressorImpl" />
<bean id="processador" class="br.com.casadocodigo.Processador">
<property name="fonteDados" ref="fonteDadosInstancia"/>
<property name="impressor" ref="impressor"/>
</bean>
3.13 A plicando herança na definição dos beans
Parafinalizar,podemosreduziraquantidadedetextoaserdigitadoemnossosarqui-
vosdeconfigura çãoaplicandooconceitodeheran ça.Adefini çãodeumbeanpode
serbaseadaemoutra.Sendoassim,emsitua çõesemquedoisbeanssãobastantepa-
recidos,ogrossodaconfigura çãoédefinidaemumdesteseosegundoapenas herda
estas,sobrescrevendoasdiferen ças.Paraobteresteresultadousamosoatributo pa-
rentdatag <bean>,quedeveserpreenchidocomonomedobeanpai.Nocódigo
abaixopodemosverumexemplodaaplica çãodesterecurso.
<bean id="impressor" class="br.com.casadocodigo.Impressor"/>
<bean id="fonteDadosArquivo"
class="br.com.casadocodigo.FonteDadosArquivo">
<property name="arquivo" value="/caminho/para/Arquivo"/>
</bean>
<bean id="fonteDadosRandomico"
class="br.com.casadocodigo.FonteDadosRandomico"/>
<bean id="processador" class="br.com.casadocodigo.Processador">
<property name="fonteDados" ref="fonteDadosArquivo"/>
64


## Página 75

CasadoCódigo Capítulo3. ConhecendooContainer
<property name="impressor" ref="impressor"/>
</bean>
<!-- Aplicando herança -->
<bean id="processadorFilho" parent="processador">
<property name="fonteDados" ref="fonteDadosRandomico"/>
</bean>
Obean processadorFilhopossuiamesmaclasseeamesmadependênciaaobean
impressor.Aúnicadiferen çaestánaversãodafontededadosaserusada.Enquanto
processadorusaumabaseadaemarquivos, processadorFilhoadotaumabaseadaem
dadosrandômica.
3.14 S pring Expression Language (SpEL)
Atéestemomentonossaconfigura çãoéestática.Todososvaloresdenossosatribu-
tosedependênciassãoconhecidosapenasemtempodedesenvolvimento.Sabemos
queomundonãoétãosimplesassim,eemnãorarassitua çõesprecisamosade-
quarofuncionamentodonossosoftwareàscondi çõesdoambienteemqueesteé
executado.Estalimita çãofoiamotiva çãoportrásdacria çãodaSpringExpression
Language(SpEL)que,comoveremosnestase ção,adicionadinamismoàsnossas
configurações.
Introduzidanaversão3.0doframework,SpELnospermiteinjetarvalorestanto
porsetterquantoconstrutoresemnossosbeanscombaseexpressõesquesãoexe-
cutadasemtempodeexecu ção.Trata-sedeumalinguagembaseadaemexpressões
muitoparecidacomaExpressionLanguagequevemosnoJSP(foiinspiradanesta
aliás),detalmaneiraque,assimcomoesta,forneceaodesenvolvedorumacurvade
aprendizadomuitopoucoacentuada.
Sintaxe básica
Comojáeradeseesperar,asintaxedaSpELébastantesimilaràqueencontramos
naEL,sempreseguindoaformaabaixo:
<property name="atributo" value="#{expressão a ser calculada}"/>
Oconteúdoqueestiverentre #{e }sempredeveretornarumvalorquepodeser
nasuaformaumliteral.Noexemploabaixodefinimosoatributo maxNumArquivos
dobean fonteDadoscomumliteralinteirosimples.
65


## Página 76

3.14. SpringExpressionLanguage(SpEL) CasadoCódigo
<bean id="fonteDadosArquivos"
class="br.com.casadocodigo.FonteDadosListaArquivos">
<property name="maxNumArquivos" value="#{5}"/>
</bean>
Obteríamosomesmoresultadosemumaexpressão,simplesmentedigitando "5”
noatributo value.Esteexemplosurgiuapenasparaexporcomodeclararumliteral
simples.AbaixoháalgunsexemplosdecomodeclararoutrosliteraiscomaSpEL:
<!-- Incluindo um valor inteiro -->
#{34}
<!-- Incluindo um valor de ponto flutuante -->
#{3.14}
<!-- Usando uma string como literal -->
#{'texto'}
<!-- Incluindo uma string com aspas duplas
quando usamos aspas simples no xml -->
value='#{"texto"}'
<!-- Incluindo um valor booleano -->
#{true}
Operações básicas e comparação
UsarliteraisisoladosnãotrásvantagemalgumaaousodoSpringsemoSpEL.
Orecursocome çaaficarmaisinteressantequandocome çamosaaplicaropera ções
ecomparaçõesemnossasexpressões.
Todasasopera çõesmatemáticasqueusamosemJavaestãodisponíveisnaSpEL:
soma(+),subtra ção(-),multiplica ção(*),divisão(/),módulo(%)e,comobrinde,
umnovooperadorparapotencia ção(^).Abaixopodemosveralgunsexemplosde
aplicaçãodearitméticanonossobean fonteDadosArquivos.
<bean id="fonteDadosArquivos"
class="br.com.casadocodigo.FonteDadosListaArquivos">
<!-- Aplicando multiplicação -->
<property name="maxNumArquivos" value="#{5 * 3}"/>
</bean>
Hátambémoperadoresrelacionaisqueretornamvaloresbooleanos:menorque
(lt),maiorque(gt),igual(eq),diferente(ne),maiorouigual(ge)emenorouigual
(le).Abaixopodemosveralgunsexemplosdesuaaplica ção:
66


## Página 77

CasadoCódigo Capítulo3. ConhecendooContainer
<!-- Retorna true -->
#{5 gt 3}
<!-- Retorna false -->
#{5 eq 3}
Comotodalinguagemdeexpressão,operadoreslógicostambémexistem:and,
orenot,cujaaplica çãopodemosverabaixo:
<!-- Retorna true -->
#{(5 gt 3) and (5 lt 8)}
<!-- Retorna false -->
#{not true}
#{not ((5 gt 3) and (5 lt 8))}
Outrooperadorimportanteéoternáriocondicional,quefuncionaexatamente
comooqueestamosacostumadosausaremJava. Paraosnovatos,suasintaxeé
bastantesimples:
(expressão) ? (valor caso verdadeiro) : (valor caso falso)
Podemosverumexemplodaaplica çãodesteoperadornocódigoabaixo:
<bean id="fonteDadosArquivos"
class="br.com.casadocodigo.FonteDadosListaArquivos">
<!-- O valor de maxNumArquivos será igual a 5 -->
<property name="maxNumArquivos" value="#{5 > 4 ? 5 : 3}"/>
</bean>
Referenciando outros beans
OsexemplosdoSpELexpostosatéagorasãoinúteis. Opoderdalinguagem
surgeapartirdomomentoemquepassamosaacessaratributospresentesemoutros
beans.Imaginequetenhamosumsegundobeanchamado fonteDadosArquivosCopia
queuseaspropriedadesdefinidasnobean fonteDadosArquivotalcomonocódigo
abaixo:
<bean id="fonteDadosListaArquivos"
class="br.com.casadocodigo.FonteDadosListaArquivos">
<property name="arquivos">
<list>
<bean class="java.io.File">
<constructor-arg value="/opt/arquivos/arquivo1.csv"/>
</bean>
67


## Página 78

3.14. SpringExpressionLanguage(SpEL) CasadoCódigo
<bean class="java.io.File">
<constructor-arg value="/opt/arquivos/arquivo2.csv"/>
</bean>
<bean class="java.io.File">
<constructor-arg value="/opt/arquivos/arquivo3.csv"/>
</bean>
<bean class="java.io.File">
<constructor-arg value="/opt/arquivos/arquivo4.csv"/>
</bean>
</list>
</property>
</bean>
<bean id="fonteDadosArquivosCopia"
class="br.com.casadocodigo.FonteDadosListaArquivos">
<property name="arquivos"
value="#{fonteDadosListaArquivos.arquivos}"/>
</bean>
Alistadearquivosde fonteDadosArquivosCopiaseráamesmaquedefinimosno
bean fonteDadosArquivo.Asintaxeusadaparaacessaroutrosbeanseseusrespecti-
vosatributoséigualmentesimples:
(identificador do bean) .(nome do atributo/propriedade)
Narealidade,onomedoatributooupropriedadeéopcional. Podemosreferir
apenasobeansequisermos,substituindoassimoatributo refsequisermos,como
noseguinteexemplo:
<property name="impressor" value="#{impressor}"/>
Tambémépossívelusarcomovalororesultadodainvoca çãodeummétodo.Po-
deríamosdefiniroatributo numMaximoArquivosdobean fonteDadosArquivosCopia
daseguintemaneira:
<bean id="fonteDadosArquivosCopia"
class="br.com.casadocodigo.FonteDadosListaArquivos">
<property name="arquivos"
value="#{fonteDadosListaArquivos.arquivos}"/>
<property name="numMaximoArquivos"
value="#{fonteDadosListaArquivos.arquivos?.size()}"/>
</bean>
68


## Página 79

CasadoCódigo Capítulo3. ConhecendooContainer
Ovalordoatributoseráigualaonúmerodeitenspresentesnoatributo arquivos
dobean fonteDadosListaArquivos. Háumanovidadenesteponto: ooperadorde
proteçãodenulidade ?. Casooatributo arquivosde fonteDadosListaArquivosfosse
nulo,nãoteríamoscomoresultadoumaexce çãodotipo NullPointerException.
Pesquisando listas
Umrecursoavan çadodaSpELéoprocessamentodelistas.Épossívelcomesta
linguagemretornarlistasbaseando-seemconsultasfeitasemoutraslistas.Amelhor
maneiradeentenderestapossibilidadeécomexemplos,sendoassim,segueabaixo
umbomexemplodestetipodeaplica ção:
<bean id="fonteDadosArquivosGrandes"
class="br.com.casadocodigo.FonteDadosListaArquivos">
<property name="arquivos"
value=
"#{fonteDadosListaArquivos.arquivos.?[exists() and size() ge 1024]}"/>
</bean>
Obean fonteDadosArquivosGrandesreceberáumanovalista,cujoconteúdoserá
todososarquivosdefinidosnoatributo arquivosde fonteDadosListaArquivosque
existame,aomesmotempo,possuamtamanhomaiorouiguala1024bytes.
Propriedades do ambiente de execução
OutrousopoderosodaSpELéapossibilidadedeobtermosinforma çõesares-
peitodonossoambientedeexecu ção. Paratalusamosoobjeto systemProperties
quesempreestáimplicitamentedisponívelatodaexpressão,quecorrespondeauma
chamadaaométodo getProperties()daclasse java.lang.System.Sendoassim,sefosse
nossoobjetivodefinirumafontededadosquesemprebuscasseumarquivodentro
dodiretório homedousuáriocorrentepoderíamosdefinirnossobeantalcomono
exemploabaixo:
<bean id="fonteDadosArquivoUsuario"
class="br.com.casadocodigo.FonteDadosArquivo">
<property name="arquivo"
value="#{systemProperties['user.home']}/arquivo.csv"/>
</bean>
Comopodeserobservadonesteexemplo,aSpELnospermiteinclusivecon-
catenarstrings. Nestecaso,ovalordavariáveldeambiente user.homeserácon-
69


## Página 80

3.15. Resumindo CasadoCódigo
catenadoaorestantedotexto "/arquivo.csv”. O interessante é que a mesma sintaxe
que aplicamos ao objetosystemProperties pode ser aplicado a qualquer objeto do tipo
java.util.Properties::.
3.15 R esumindo
Estefoiumcapítulobastantedensoemquepudemosveramaiorpartedoqueestá
portrásdomecanismodeinversãodecontroleeinje çãodedependênciasdoSpring.
Paratalapresentamosoformatodeconfigura çãomaisusadodoSpringqueéoXML
e,comele,vimosobásicodesdecomodeclararumbean,osmodosquetemosde
instanciá-los,comoinjetardependênciasevaloresdeatributosatémaneirasdeti-
rarmosproveitotantodociclodevidadocontainercomodoprópriobean. Para
finalizar,demosdinamismoàsnossasconfigura çõesapresentandoaSpEL,umalin-
guagembaseadaemexpressõesincluídanoSpring3.0que,desdeentão,permeia
todoorestantedoframework,incluindoconfigura çõesbaseadasemanota ções.
Porfalaremanota ções,oleitordeveestarpreocupadocomaquantidadedeXML
quedigitamosnestecapítulo. Esperoterprovadooquãopoderosoéesteformato
(queaindanãofoicompletamenteexploradonestecapítulo),porémdevemosnos
atentaraofatodequetodoestedigitardeconfigura çõesnãoéamaneiramaispro-
dutivaquetemosdetrabalhar. Sendoassim,preparo-oparaopróximocapítulo,
aondeveremoscomominimizaraomáximoanecessidadededigitarmosconfigu-
raçõesaonossocontaineraumentandosignificativamenteaprodutividadeoferecida
peloframework.
70


## Página 81

Capítulo4
MinimizandooXMLcom
autowiring,anotaçõeseJava
Nestepontojáconhecemosbastantearespeitodomodocomoainversãodecon-
trole/injeçãodedependênciaséimplementadanoSpringFramework.Atéentãosó
usamosoformatomaispopulardeseconfigurarocontainer,queéoXML.Chegou
ahoradeaumentaranossaprodutividademinimizandootrabalhomanual.Vamos
veroutrasformasdeconfigura çãooferecidospeloframework,masvalelembrarque
vocêencontraráaconfiguraçãoviaXMLemdiversosprojetoseatémesmocomo
principalreferêncianadocumentação.
4.1 A utowiring : automatizando a injeção de depen -
dências
JánasprimeirasversõesdoSpringficouclaroqueoformatoXMLpodefacilmentese
tornarumgargalonaprodutividadedodesenvolvedor.Aprimeirasolu çãoencon-


## Página 82

4.1. Autowiring:automatizandoainjeçãodedependências CasadoCódigo
tradaparaoproblemafoiainclusãodainje çãoautomáticadedependências,maisco-
nhecidacomo autowiring.Esterecursopossibilitaaocontainerdescobriremtempo
deexecuçãoquaisasdependênciasquedevemserinjetadasemcadabeanSEMque
odesenvolvedorpreciseinstruí-loparatal.
Paramelhorentenderseufuncionamentovamosapresentarumexemplomais
elaboradoqueosanteriores.Trata-sedeumsistemadegestãocomercialcomposto
portrêsDAOs,todosderivadosdaclasse AbstractDAOque,porsuavez,possuicomo
dependênciaumobjetodotipo DataSourcequerepresentaumafontededadosqual-
quer.
Figura4.1:Visãogeraldonossosistema
Combasenoquejásabemos,aprimeiraversãodonossoarquivodeconfigura-
çãopoderiasersimilaràdescritaabaixo:
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.springframework.org/schema/beans
72


## Página 83

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
http://www.springframework.org/schema/beans/spring-beans.xsd">
<bean id="dataSource" class="br.com.casadocodigo.DataSource">
<property name="connectionString"
value="jdbc:mysql://localhost/db"/>
</bean>
<bean id="daoProduto" class="br.com.casadocodigo.DAOProduto">
<property name="dataSource" ref="dataSource"/>
</bean>
<bean id="daoUsuario" class="br.com.casadocodigo.DAOUsuario">
<property name="dataSource" ref="dataSource"/>
</bean>
<bean id="daoVenda" class="br.com.casadocodigo.DAOVenda">
<property name="dataSource" ref="dataSource"/>
</bean>
<bean id="processador" class="br.com.casadocodigo.Processador">
<property name="daoProduto" ref="daoProduto"/>
<property name="daoUsuario" ref="daoUsuario"/>
<property name="daoVenda" ref="daoVenda"/>
</bean>
</beans>
Observandoestaconfigura çãoficamaisclarocomooformatoXMLpodepre-
judicarnossaprodutividade.Aquantidadedecódigorepetidoéconsiderável.Note
queobean dataSource,compartilhadoportodosos DAOsdosistemafoiinjetada
manualmentetodasasvezesquefoinecessária. DadoqueaplataformaJavapos-
suiummecanismodereflexãobastantepoderosoeháapenasumbeandecadatipo
necessárioparaofuncionamentodosistema,nãoédifícilimaginarumalgoritmo
quedescubraautomaticamentequaisdependênciasprecisamsersatisfeitascombase
apenasnostiposdebeansdeclaradosnaconfigura ção.
Esterecursossechama autowiring. Aplicando-onaconfiguraçãoacima,obte-
mosumarquivodeconfigura çãosignificativamentemenor,comopodeserobser-
vadonocódigoabaixo:
<?xml version="1.0" encoding="UTF-8"?>
<beans default-autowire="byType"
73


## Página 84

4.1. Autowiring:automatizandoainjeçãodedependências CasadoCódigo
xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd">
<bean class="br.com.casadocodigo.DataSource">
<property name="connectionString"
value="jdbc:mysql://localhost/db"/>
</bean>
<bean class="br.com.casadocodigo.DAOProduto"/>
<bean class="br.com.casadocodigo.DAOUsuario"/>
<bean class="br.com.casadocodigo.DAOVenda"/>
<bean class="br.com.casadocodigo.Processador"/>
</beans>
Nanovaconfigura çãofoinecessáriodigitarapenas7linhasdescrevendonossos
beansaoinvésdas17escritasanteriormente. Outropontointeressante: dadoque
o containerdescobriráquaisdependênciasprecisamsersatisfeitas,nãoprecisamos
sequerdefinirnomesdenossosbeans.
Paraqueocontainerapliqueo autowiringpodemosadotardoiscaminhos.Opri-
meiroemenostrabalhosoéinstrui-loaaplicarestatécnicaatodososbeansquese
encontremdeclaradosnomesmoarquivo.Comofizemosnaúltimaversãodenossa
configuração,bastaadicionaroatributo default-autowireàtag <beans>. É
tambémpossívelaplicaroautowiringapenasaalgunsbeansdefinidosnomesmoar-
quivo.Comojáeradeseesperar,bastaacrescentaromesmoatributoàtag <bean>
querepresentaadefini çãodebeanemcimadaqualainje çãoautomáticadevaser
aplicada.Independentedolocalaondeoatributosejaincluído,estesemprepodere-
ceberumdosvaloresdescritosabaixo,quedescrevemqualaestratégiaaseradotada
pelocontainer:
•no:valordefaultadotadopelocontainer.Autowiringnãoseráadotado.
•byType: umadependênciaseráinjetadaautomaticamentecasosejaencon-
tradaapenasumadefini çãodobeanquepossuatipocompatível.
•byName:oSpringiráinjetaradependênciacombasenonome.Serãobusca-
dosbeansquepossuamomesmonomedapropriedadeaserpreenchida.
•constructor:similaraoalgoritmo byType,comadiferen çadequebuscará
porconstrutoresnãopadrãoparaexecutarainje çãoaoinvésdepropriedades.
74


## Página 85

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
•autodetect: o container irá inicialmente tentar a injeção do tipo
constructor. Casonãosejaencontradoumconstrutornobeanaserin-
jetado,procederáparaaestratégia byType.
Evitando ambiguidades
Paraqueainje çãoautomáticafuncioneéfundamentalqueocontainernãotenha
dúvidasarespeitodequaldependênciainjetar.Expondomelhoroproblema,vamos
complicarnossoexemplo. Suponhaqueobean DAOUsuarioprecisebuscarseus
dadosdeumbancodedadoslegado.Ingenuamentealteramosnossaconfigura ção
paraquefiquetalcomonoexemploabaixo:
<beans default-autowire="byType"
xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd">
<bean class="br.com.casadocodigo.DataSource">
<property name="connectionString"
value="jdbc:mysql://localhost/db"/>
</bean>
<bean id="dataSourceUsuarios"
class="br.com.casadocodigo.DataSource">
<property name="connectionString"
value="jdbc:mysql://localhost/users"/>
</bean>
<bean id="daoUsuario" class="br.com.casadocodigo.DAOUsuario">
<property name="dataSource" ref="dataSourceUsuarios"/>
</bean>
<bean class="br.com.casadocodigo.DAOProduto"/>
<bean class="br.com.casadocodigo.DAOVenda"/>
<bean class="br.com.casadocodigo.Processador"/>
</beans>
Observe que a dependência foi definida explicitamente para o bean
daoUsuariomas não para os demais DAOs. Como consequência, quando o
containerforiniciadonãosaberáqualfontededadosinjetarnosbeansdotipo
75


## Página 86

4.2. Vantagenselimitaçõesdainje çãoautomática CasadoCódigo
DAOVendae DAOProduto.Oresultadoseráolevantamentodeumaexce çãodotipo
org.springframework.beans.factory.UnsatisfiedDependencyException.
Háduassoluçõesparaoproblema:aprimeiraédefinirmanualmenteafontede
dadosdecadaDAOemnossosistema.Asolu çãomaisinteligenteéinstruirocontai-
nerarespeitodequaisbeans não sãocandidatosasereminjetadosautomaticamente.
Resolvemosesteproblemaadicionandooatributo autowire-candidatecomo
valor falsenobeanaserexcluído.Emnossoexemplo,bastariaalteraradefini ção
dobean dataSourceUsuariostalcomonoexemploabaixo:
<bean id="dataSourceUsuarios" class="br.com.casadocodigo.DataSource"
autowire-candidate="false">
<property name="connectionString"
value="jdbc:mysql://localhost/users"/>
</bean>
<bean id="daoUsuario" class="br.com.casadocodigo.DAOUsuario">
<property name="dataSource" ref="dataSourceUsuarios"/>
</bean>
Háumdetalheinteressanteaserobservadonaconfigura çãoacima: obean
daoUsuariodefineexplicitamentequalbeandeveserinjetadoemsuapropriedade
dataSource.Ainje çãodedependênciasautomáticaéanuladaemsitua çõescomo
esta,emqueaconfigura çãosejafeitaexplicitamente.
4.2 V antagens e limitações da injeção automática
Avantagemóbviaportrásdo autowiringéaredu çãodaconfigura ção. Oganho
ocultoéaevolu çãonaturaleautomáticadenossaconfigura çãoemtempodede-
senvolvimento,vistoqueoprogramadornãoprecisaatualizarconstantementeseus
arquivosXMLconformeprogridenoprocessodecria çãodoseucódigo.
Aprincipallimita çãodatécnicaéasubstitui çãodo explícitopelo implícito.Até
entãosempretínhamoscertezadecomoseriafeitaainje çãodedependênciasem
nossosbeanspoisofazíamosmanualmente.Apartirdomomentoemqueadotamos
o autowiringdelegamosestaresponsabilidadeaocontainer.Emprojetosnosquais
onúmerodebeanssejapequenoeonúmerodecandidatosasereminjetadossejao
aceitável(1)oganhodeprodutividadeégarantido,masconformeoprojetoevolui
eonúmerodecandidatosaumentaodesenvolvedorseveráconstantementepreci-
sandoexcluirumououtrocandidatoe,aindapior,acabarávoltandoparaomodo
manualdeconfigura ção.Naesmagadoramaioriadoscasososerrosserãodetecta-
76


## Página 87

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
dosemtempodedesenvolvimento,poisocontainerlan çaráumaexceçãodotipo
org.springframework.beans.factory.UnsatisfiedDependencyException.
Éimportantesalientarqueháapossibilidadedeerrossutis,emtempodeexecu ção,
decorrentesdainje çãoequivocadadeumbeanououtropelocontainer.
Outralimitaçãodo autowiringéofatodestenãoinjetarautomaticamentepro-
priedadesdotipoprimitivo,listasoustrings. Nestescasosodesenvolvedordeve
definirseusvaloresexplicitamentesempre,mesmoporquenãohácomoocontainer
adivinharseusvalores.
Aregradeouronaado çãodo autowiringéusá-loapenasemprojetospequenos
ou,nocasodeprojetosmaiores,naquelesemquesejamdefinidasconven çõesrígidas
bemdivulgadaseadotadasportodaaequipededesenvolvimento.
4.3 F acilitando ainda mais com Anotações
Aversão2.0doSpringtrouxeumrefor çoimportanteparaatarefaderedu çãodo
XMLsobaformadeconfigura çõesbaseadasemanota çõesJava.Comaadi çãodeste
recursoosdesenvolvedoresganharamoutroimpulsoemsuaprodutividaderedu-
zindoaquasenadaanecessidadedeprecisarmosescreverconfigura çãonoformato
XML.Trata-sedeumaferramentapoderosaqueserviuinclusivecomoumadasins-
piraçõesparaaJSR-330quedefineopadrãodeinje çãodedependênciasadotado
comopadrãopelaplataformaJavaEEapartirdesuaversão5.
AoinvésdesimplesmentecompetircomestaJSR,aSpringSourceoptoupor
abraçá-la,tornandoseucontainercompatívelcomamesmaaomesmotempoque
possibilitandoaodesenvolvedortirarproveitodascapacidadesúnicasdoSpring.
Comoveremos,hátambémsuporteàJSR-250( Common Annotations for the Java
Platform),queformaumadasbasesdoEJB3.0.
Agrossomodotemosaquiumaevolu çãodainje çãoautomáticaportipocoma
transferênciadenossaconfiguraçãodosarquivosXMLparaumcontextomaispró-
ximodeseuuso,queéaclasseondedevemserinjetadassuasdependências.
Definindo pontos de injeção
Ironicamente, o primeiro passo na redução do XML nesta seção será
incrementando-ocomonamespacecontext.Paratal,modificaremosaúltimaversão
donossoarquivodeconfigura çãoparaquefiquetalcomonoexemploabaixo:
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
77


## Página 88

4.3. FacilitandoaindamaiscomAnota ções CasadoCódigo
xmlns:context="http://www.springframework.org/schema/context"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context-3.0.xsd">
<context:annotation-config/>
<bean id="dataSource" class="br.com.casadocodigo.DataSource">
<property name="connectionString"
value="jdbc:mysql://localhost/db"/>
</bean>
<bean id="daoProduto" class="br.com.casadocodigo.DAOProduto"/>
<bean id="daoUsuario" class="br.com.casadocodigo.DAOUsuario" />
<bean id="daoVenda" class="br.com.casadocodigo.DAOVenda"/>
<bean id="processador" class="br.com.casadocodigo.Processador"/>
</beans>
Repare que o atributo default-autowire foi removido da tag
<beans>, criando a falsa impressão de que estamos desabilitando a inje-
ção automática. Na realidade estamos apenas modificando sua forma. A tag
<context:annotation-config/>informaocontainerdequenossaconfigura-
çãoserádefinidaporanota ções.
Nestemomentoanovidadeéaformacomodefiniremosospontosdeinje ção
dedependências.AoinvésdoXMLconvencional,usaremosagoraduasanota ções
fornecidaspeloSpring: @Requirede @Autowired.
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Required;
public abstract class AbstractDAO {
private DataSource dataSource;
public DataSource getDataSource() {return dataSource;}
@Required @Autowired
public void setDataSource(DataSource ds) {dataSource = ds;}
}
A anotação @Required (opcional) só pode ser aplicada em métodos
78


## Página 89

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
e setters. Possui a função de instruir o container a respeito da obrigato-
riedade de uma dependência, forçando-o a disparar uma exceção do tipo
org.springframework.beans.factory.UnsatisfiedDependencyException
casonãosejaencontradoumcandidatoqueasatisfa ça.
Jáaanotação@Autowired,comoopróprionomediz,indicaumpontoaonde
ainjeçãoautomáticadeveseraplicada.Estapodeserusadaemmétodos,atributos
econstrutores(importantemencionarqueapenasumconstrutorporclassepode
recebê-la).Casoopteporusá-la,épossíveldescartarousodaanota ção @Required,
talcomonoexemploabaixo:
@Autowired(required=true)
public void setDataSource(DataSource ds) {dataSource = ds;}
Comomencionadonoiníciodestase ção,oSpringtambémoferecesuporteàs
anotaçõesdaJSR-330. Aprincipalvantagememseuusoéofatodocódigofonte
nãoterdependênciadiretaaoSpringesimclassesquesempreserãoprovidaspela
plataformaJavaEE.
Aanota çãomaispopularnestecasoé @Inject. Comoporpadrãoseucó-
digofontenãovêmcomoSpring,énecessárioacrescentarabibliotecanecessária
aoclasspathdoseuprojeto. CasoestesejabaseadoemMaven,bastaadicionara
dependênciaexpostaabaixoouentãofazerodownloadmanualdoarquivojarem
http://code.google.com/p/atinject/.
<dependency>
<groupId>javax.inject</groupId>
<artifactId>javax.inject</artifactId>
<version>1</version>
</dependency>
Assimcomo @Autowired, @Injectpodeserusadaemmétodos,atributosou
construtores(mantendoalimita çãodesópoderanotarumconstrutorporclasse).
Comparadaàanota ção @Autowired,possuiadesvantagemdenãopossuiroatri-
buto required.
@Inject
public void setDataSource(DataSource ds) {dataSource = ds;}
}
Outraopçãoéaanota ção @ResourceintroduzidanaJSR-250. Comoerade
seesperar,seuusoépraticamenteidênticoaoqueencontramosnasanota çõesex-
79


## Página 90

4.3. FacilitandoaindamaiscomAnota ções CasadoCódigo
postasanteriormente.Umoutropontoimportanteéapossibilidadedeusarastrês
anotaçõesdentrodeumamesmaclasse,comopodeservistonoexemploabaixo:
public class Processador {
@Resource
public void setDaoProduto(DAOProduto daoProduto) {
this.daoProduto = daoProduto; }
@Autowired
public void setDaoUsuario(DAOUsuario daoUsuario) {
this.daoUsuario = daoUsuario; }
@Inject
private DAOVenda daoVenda;
// Outros métodos do processador
}
Encontrando os beans
Atéestemomentoadeclara çãodosbeansaindaéfeitadiretamenteemnosso
documentoXML.Aúnicadiferen çaestánofatodetermosmovidoasdefini ções
deinjeçãoparanossocódigofonte.Arealredu çãodoXMLsóocorrequandoins-
truímosocontainerabuscarasdefini çõesdenossosbeansvarrendooclasspathdo
nossosistemaembuscadeclassesdevidamenteanotadas,quepossamserreconhe-
cidascomobeans.
Modificaremos mais uma vez nosso arquivo de configuração de tal modo
que este tenha no final apenas duas linhas significativas. Instruiremos o con-
tainerabuscarnossasdefini çõesdebeansvarrendooclasspathinserindoatag
<context:component-scan/>emnossoarquivoXMLcomopodeservistono
exemploabaixo:
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:context="http://www.springframework.org/schema/context"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context-3.0.xsd">
80


## Página 91

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
<context:annotation-config/>
<context:component-scan base-package="br.com.casadocodigo"/>
</beans>
Atag <component-scan>possuioparâmetro base-packageobrigatório
querecebecomovaloronomedopacotequecontémtodasasnossasclassesque
implementamosbeansdenossosistema.Entraemcenaoconceitodeestereótipo.
UmaclasseéreconhecidapeloSpringcomoumaconfigura çãodebeansepossui
umaanotaçãoquedefinaotipodebean(estereótipo)queestarepresenta.
O tipo mais básico de componente é identificado no Spring pela anotação
@Component. Paraidentificarumaclassecomoumcomponente,bastaadicionar
estaanotaçãocomopodeservistonocódigoabaixo:
@Component("processador")
public class Processador {
...
}
Comopôdeservisto, aindacomanota çõesépossívelnomearnossosbeans
passando como parâmetro sua identificação. Caso este valor esteja ausente, o
nomedobeanserádefinidopelocontainerautomaticamente.Alémdoestereótipo
@ComponentoSpringtambémofereceumasériedeoutrasop çõescomoporexem-
plo @Repositoryparaidentificar DAOs, @Controllerparacontroladoresdo
SpringMVC, @Serviceparacontroletransacionalmaisfinoemuitosoutros. A
existênciademúltiplosestereótipospermiteàequipededesenvolvimentoimple-
mentarcomportamentosdistintosparacadatipodebean,enriquecendoassimainda
maisopoderdaferramenta.
AlémdasanotaçõesdoSpringusadasparaidentifica çãodeestereótipos,também
podemosusaraanota ção @NameddefinidanaJSR-330,quepossuiráexatamenteo
mesmocomportamentodaanota ção @Component. Abaixopodemosveralguns
exemplosdesuautiliza ção.
import javax.inject.Named;
@Named // Anotando um componente sem nome explícito
public class Processador {}
@Named("processador") // Definindo explicitamente o nome do bean
public class Processador {}
81


## Página 92

4.3. FacilitandoaindamaiscomAnota ções CasadoCódigo
Filtrando componentes
Há situações nas quais não é interessante o carregamento de todas as de-
finições de beans presentes em um pacote. Em nosso documento XML
quando incluímos apenas a tag <context:component-scan/>, esta-
mos instruindo o container a carregar todas as definições de beans con-
tidas no pacote definido pelo atributo base-package. Caso seja ne-
cessário incluir apenas parte destas definições, entram em ação as tags
<context:include-filter> e <context:exclude-filter>, ambas
aninhadasdentrode <context:component-scan>e, comoopróprionome
jádiz,definemrespectivamentequaisdefini çõesdebeansdevemserincluídase
ignoradasemnossaconfigura ção.
Tanto <context:include-filter> quanto
<context:exclude-filter> possuem dois parâmetros obrigatórios que
são typee expression. Oprimeiroidentificaotipodeexpressãousadapara
encontraroscomponentesnoclasspathdosistemaenquantoosegundodefinea
expressãoqueaplicaremosnafiltragem.
PorpadrãooSpringofereceosseguintestiposdeexpressão:
•annotation: noparâmetro expressiondeveráestarpresenteonome
completodaanotaçãodeidentifica çãodebeans(estereótipo)queseráincluída
nofiltro.
•regex:passamosumaexpressãoregularqueidentifiqueotipodeclasseque
entraránafiltragem.
•assignable:definequalaclassebaseouinterfaceimplementadapelasclas-
sesanotadasquedeveráserincluídanofiltro.
•aspectj:umaexpressãonoformatoAspectJparaidentificaroscomponen-
tes.
•custom: é possível implementar filtros customizados na varredura do
classpath, que são basicamente classes que implementem a interface
org.springframework.core.type.TypeFilter.
Nocódigoabaixopodemosveraaplica çãodefiltrosnavarreduracustomizada
donossoclasspath:
82


## Página 93

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
<context:component-scan base-package="br.com.casadocodigo.dao">
<!--
Inclui todos os componentes cujo
nome da classe comece com DAO
-->
<context:include-filter type="regex" expression="DAO*"/>
<!-- Exclui todos os componentes do estereótipo Controller -->
<context:exclude-filter type="annotation"
expression="org.springframework.stereotype.Controller"/>
</context:component-scan>
<context:component-scan base-package="br.com.casadocodigo.dao">
<!-- Inclui apenas classes com classe mãe DAOBase -->
<context:include-filter type="assignable"
expression="br.com.casadocodigo.DAOBase"/>
</context:component-scan>
Definindo escopos
Definimosoescopodeumbeanusandoaanota ção @ScopeprovidapeloSpring.
Estarecebecomoparâmetroonomedoescopoquesãoosmesmosapresentadosno
capítuloanterior: singleton, prototype, requestouonomedoseuescopo
customizado.Nocódigoabaixopodemosveralgumasaplica çõesdestaanota ção.
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;
...
@Scope("prototype")
@Component
public class DAOUsuario {...}
@Scope("request")
@Component
public class DAOProduto {...}
Assimcomonaconfigura çãoXMLconvencional,casosejaomitidooescopode
umbeanseráadotadoopadrão singleton.
Ciclo de vida
Épossíveldefinirmétodosdecallbackaseremexecutadosapósainje çãoeantes
dadestruiçãodosbeans,talcomoaprendemosafazernocapítuloanterior.Paratal
83


## Página 94

4.3. FacilitandoaindamaiscomAnota ções CasadoCódigo
usamosasanota ções @PostConstructe @PreDestroydefinidasnaJSR-250.No
códigoabaixopodemosverumexemplodeaplica çãodasmesmas:
import javax.annotation.PostConstruct; //JSR-250
import javax.annotation.PreDestroy; //JSR-250
import javax.inject.Named; //JSR-330
@Named
public class DAOProduto extends AbstractDAO {
@PostConstruct
public void init() {
System.out.println("\n\n\nDAO Produto iniciado\n\n\n");
}
@PreDestroy
public void destroy() {
System.out.println("\n\n\nDAO Produto Finalizado\n\n\n");
}
}
Éimportantemencionarqueodesenvolvedorcontinuacomaop çãodeusar
asinterfaces org.springframework.beans.factory.InitializingBean
ou org.springframework.beans.factory.DisposableBeanpraobtero
mesmoresultado.
Limitando o número de candidatos
Dadoqueasanota çõessãoumaevolu çãodoconceitode autowiringapresentado
naseçãoanterior,oproblemadaambiguidadedeconfigura çãoprecisasertratado.
Asoluçãononossocasosedáatravésdaado çãodequalificadores,queservempara
fornecerumamelhoridentifica çãoaosnossosbeans.
Usamosaanota ção @Qualifierparaguiarocontainernasele çãodequalde-
pendênciadeveráserinjetadaemdeterminadoatributoouparâmetrodeconstrutor
oumétododefinidoemumbean,talcomopodeservistonocódigoabaixo:
import org.springframework.beans.factory.annotation.Qualifier;
@Named("daoUsuario")
public class DAOUsuario {
@Qualifier("dataSourceUsuario")
private DataSource dataSource;
}
84


## Página 95

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
Ovalorpassadoàanota çãoéoidentificadorqueajudanaescolhadequalde-
pendênciadeveráserinjetadanaqueleponto. Porconven ção, seuvalorcorres-
pondeaonomedobeanaserinjetado. Épossíveltambémmesclarqualificadores
comconfiguraçãoXMLusandoatag <qualifier>. Sendoassim,oqualifica-
dor dataSourceUsuarioexpostoacimapoderiaseridentificadonaconfigura ção
XMLdaseguinteforma:
<!-- Este bean será injetado em DAOUsuario -->
<bean id="dsUsuario" class="br.com.casadocodigo.DataSource">
<qualifier value="dataSourceUsuario"/>
</bean>
<!-- Este bean não será injetado em DAOUsuario -->
<bean id="dsGeral" class="br.com.casadocodigo.DataSource">
<property name="connectionString" value="jdbc:database//meuDB"/>
</bean>
Aanotação @Qualifieréamaisgenéricapossível.Sefordeinteressedode-
senvolvedor,épossívelevoluirseucódigosemanticamentecriandosuaprópriaano-
taçãoqualificadora.Paratal,bastacriarsuaprópriaanota çãoaplicando-lheaano-
tação @Qualifiertalcomoem:
@Target({ElementType.FIELD, ElementType.PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Qualifier
public @interface TipoDataSource {
String valor();
}
Emseguida,bastausarsuaanota çãocustomizadaaoinvésdapadrãoparalimitar
onúmerodecandidatosasereminjetadosemseusbeans.Aanota çãoqualificadora
tambémpodeseraplicadaaparâmetrosdeconstrutoresoumétodos,talcomono
exemploabaixo:
public void setDataSource(@TipoDataSource("usuarios") DataSource ds) {
this.dataSource = ds;
}
V antagens e limitações do uso de anota ções
Háumdebatesemfimnacomunidadearespeitodasuperioridadedasanota ções
emrelaçãoaoXML.Aprincipalvantagemdasanota çõesestánofatodestasserem
85


## Página 96

4.4. ConfiguraçãoprogramáticacomJava CasadoCódigo
incluídasdiretamentenasclasses,maispróximasportantodocontextododesenvol-
vedordoqueumarquivoseparado.Outrobenefício,comojádito,éofatodereduzir
significativamenteotamanhodonossoarquivodeconfigura çãoqueprecisaríamos
escreversemorecurso.
Entretanto,éimportantesalientaralgumaslimita ções.Aprincipalvantagemdo
formatoXMLéofatodestepossibilitaralterarofuncionamentodonossosistema
semanecessidadederecompilarmosocódigofonte.Emsitua çõesemqueacusto-
mizaçãosejaumaspectocrítico,comoporexemplonodesenvolvimentodeprodutos
deprateleira,aado çãodasanota çõespodemacarretarmaisperdasqueganhos.Ape-
sardisto,éimportantemencionarquequalquerconfigura çãofeitausandoanota ções
podesersobrescritaemumarquivoXML.Porexemplo,épossíveldeclararumbean
específicoemXMLeesteserálevadoemconsidera çãoaoinvésdomesmodefinido
usandoanotações.
Outropontoimportanteaserlevantado:aredu çãodaconfigura çãomuitasvezes
éilusóriaquandousamosanota ções,poisnapráticanamaiorpartedasvezesoque
realmenteestamosfazendoétransferirinforma çõesdoformatoXMLparadentro
denossasclasses.
4.4 C onfiguração programática com Jav a
Aversão3.0doSpringtrouxecomonovidadeapossibilidadedeconfigurarmos
nossocontainercomcódigoJava,oferecendopossibilidadesinteressantesaodesen-
volvedorcomoporexemploconfigura çãoprogramáticae,finalmente,aelimina ção
totaldaconfigura çãoXML.
Osmodosdeconfigura çãoatéentãoapresentadossãodeclarativos. Odesen-
volvedordescreveaocontaineroqueinstanciareesteseencarregadotrabalhode
injeçãodedependênciaseinicializa çãodosbeans.Comaconfigura çãobaseadaem
códigoJavaoprogramadorpassaaagirimperativamentesobreociclodevidados
beans.Combasenoqueaprendemosatéestemomento,passoparaoleitorumdesa-
fio:usandoXMLouanota ções,comodefinirqualtipodeclasseinstanciarbaseado
emalgumfatordeexecu çãodosistemacomoporexemploahoracorrente?Como
veremos,estetipodeproblemaétrivialmenteresolvidousandoconfigura çãobase-
adaemcódigo.
@Configuration e @Bean
Nos formatos de configuração apresentados anteriormente o ponto de par-
86


## Página 97

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
tidasempreeraumarquivonoformatoXML.Comaconfigura çãoprogramática
nossopontodepartidapassaaserumaoumaisclassesquepossuamaanota ção
@Configurationque,porbaixodospanos,consisteemmaisum estereótipo(ste-
reotype)oferecidopeloSpring.
Todaclasseanotadacom @Configurationéentendidapelocontainercomo
umbeanresponsávelporarmazenarumaoumaisdefini çõesdebeans. Dadoque
estamostrabalhandocomumestereótipo,seuusoéexatamenteigualaoquejávimos
naseçãoanteriorcomopodeservistonocódigoabaixo:
import org.springframework.context.annotation.Configuration;
// Sem definir um nome explicitamente
@Configuration
public class JavaConfig {...}
// Definindo um nome explicitamente
@Configuration("configuracaoJava")
public class JavaConfig {...}
Se @Configurationdefineum repositório de beans,emseuinteriordevemos
incluiraanota ção @Bean,quedeveserinseridaapenasemfun çõesequivaleàtag
<bean>queusamosnaconfigura çãonoformatoXML.Nocódigoabaixopodemos
veralgunsexemplosdeseuuso:
@Configuration
public class JavaConfig {
@Bean
public DAOUsuario daoUsuario() {
return new DAOUsuario();
}
// Definindo mais de um nome para o mesmo bean
@Bean(name={"daoProduto","produtoDAO"})
public DAOProduto criarDAOProduto() {
return new DAOProduto();
}
// Definindo o nome do bean explicitamente
@Bean(name="datasource")
public DataSource getDataSource() {
DataSource ds = null;
87


## Página 98

4.4. ConfiguraçãoprogramáticacomJava CasadoCódigo
GregorianCalendar data = new GregorianCalendar();
if (data.get(GregorianCalendar.HOUR_OF_DAY) < 13) {
ds = new DataSourceUsuarios();
} else {
ds = new DataSource();
}
return ds;
}
}
Vemosnoexemploanteriortrêsusosdaanota ção @Bean. Noprimeirocaso,
aplicamosaanota çãosobreummétodosemdefinirexplicitamenteonomedobean.
Nestasituaçãoonomedobeancorresponderáaonomedométodoquerecebeua
anotação.Assimcomonaconfigura çãoXML,tambémépossíveldefinirmúltiplos
nomesparaumbean( aliases),queéoquefazemosnosegundocasodaanota ção,
passandocomoparâmetroumarraydestringscontendoestesnomes.
Comopodeserobservado,tudooqueosdoisprimeirosmétodosdonossocó-
digoanteriorsimplesmentecriamumanovainstânciadobean. Ousorealmente
interessantepodeserobservadonoterceirocasoemqueusamosahoracorrentedo
sistemaparaescolherqualimplementa çãodeveserinstanciada.
Finalmente,dadoque @Configurationnarealidadeéumestereótipo,isto
é,umavaria çãode @Component,poderíamosinformarocontainerviaXMLa
usar configurações baseadas em anotações com um arquivo similar ao exposto
abaixo,sabendoquenopacote br.com.casadocodigo.javaháapenasaclasse
JavaConfig:
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:context="http://www.springframework.org/schema/context"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context.xsd">
<context:component-scan base-package="br.com.casadocodigo.java"/>
</beans>
88


## Página 99

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
Ciclo de vida e escopo
Aanotação @Beanpossuidoisatributosopcionaisquenospermitemtirarpro-
veitodociclodevidadobeanporelarepresentado.Estesatributossão initMethod
e destroyMethod,querecebemcomovaloronomedométodoaserexecutado
apósainstancia çãoeinje çãodedependênciasnobeaneantesdesuadestrui çãopelo
container.Nocódigoabaixopodemosverumexemplodeseuuso:
@Bean(initMethod="iniciar", destroyMethod="destruir")
public DAOUsuario getDaoUsuario() {
return new DAOUsuario();
}
Tambémpodemosdefiniroescopodeumbean.Nestecaso,adicionamosaano-
tação @ScopeprovidapeloSpring. Nocaso,seuusoéexatamenteomesmoque
vimosnaconfigura çãobaseadaporanota ções,adiferen çaéqueiremosanotaro
métodoresponsávelpelainstanciaçãodobean.
@Scope("prototype")
@Bean(initMethod="iniciar", destroyMethod="destruir")
public DAOUsuario getDaoUsuario() {
return new DAOUsuario();
}
@Scope("request")
@Bean
public DAOProduto daoProduto() {
return new DAOProduto();
}
Injetando dependências
Nosexemplosexpostosatéestemomentotodososmétodosconstrutoresdebe-
ansexpostossimplesmenteinstanciamobjetossemsepreocuparcomainje çãode
dependências.Istoporquenarealidadeestamosnovamenteaquiusandoaconfigu-
raçãobaseadaemanota çõesque,naprática,éo autowiringbaseadoemtipo.
NaconfiguraçãobaseadaemJava,noentanto,éimportanteobservarque,uma
vezqueométodo @Beanretorneseuvalor,ocontainerseencarregadeinjetartodas
asdependênciasdesteobjeto,oquepodegeraralgumassitua çõesparaosiniciantes,
comoporexemploasitua çãoexpostanocódigoabaixo:
89


## Página 100

4.4. ConfiguraçãoprogramáticacomJava CasadoCódigo
@Configuration
public class JavaBuilder {
@Bean
public DataSource dataSource() {
return new DataSource();
}
@Bean
public DAOProduto daoProduto() {
return new DAOProduto();
}
@Bean
public DAOProduto preConfigurado() {
DAOProduto dao = new DAOProduto();
dao.setDataSource(new DataSource());
return dao;
}
}
Aprimeiravistapodemosteraimpressãodequeobean preConfigurado
expostoacimarecebecomodependênciaumainstânciadiferentedadefinidapelo
bean dataSource,certo?Errado:umavezobtidaainstânciadobeanocontainer
iráinjetarcomodependênciaobeanretornadopelométodo dataSource(). A
únicamaneiradeseevitarestecomportamentoconsisteemnãoimplementarna
classeDAOProdutoummétodosetterparaoatributo dataSource,injetandoesta
dependênciaapenaspeloconstrutor.
Dadoqueumaclasseanotadacom @Configurationéemsiumbean,esta
tambémpodereceberdependências.Sendoassim,poderíamosinjetarumadepen-
dêncianestaeemseguidareaproveitá-lanasdefini çõesdebeansqueestacontenha,
talcomonoexemploabaixo:
@Configuration
public class JavaBuilderDependencia {
@Autowired
private DataSource dataSource;
@Bean
public DAOProduto daoProduto() {
DAOProduto daoProduto = new DAOProduto();
daoProduto.setDataSource(dataSource);
90


## Página 101

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
return daoProduto;
}
}
Excluindo a configuração XML
Finalmente,comomencionadonoiníciodestase ção,veremoscomotornaro
Spring100%livredaconfigura çãoXML.Parataliremosusarumaimplementa çãodo
ApplicationContextchamada AnnotationConfigApplicationContext,
presente no pacote org.springframework.context.annotation.
Ao contrário de ClassPathXmlApplicationContext e
FileSystemXmlApplicationContext, esta classe recebe como parâmetro
uma ou mais classes que contenham definições de beans, ou seja, aquelas que
possuem uma anotação que as identifiquem como implementadoras de algum
estereótiporeconhecidopeloSpring.
Háapenasduasnovidadesnestetipodecontainer,seusconstrutoreseométodo
register. Épossívelinstanciarestecontextodeaplica çãodequalquerumadas
formasexpostasnocódigoabaixo:
import org.springframework.context.annotation.
AnnotationConfigApplicationContext;
...
AnnotationConfigApplicationContext context;
// Pelo construtor padrão
context = new AnnotationConfigApplicationContext();
/*
Passando apenas uma classe contendo definições de beans @Configuration
ou alguma classe que possua um estereótipo anotado
*/
context = new AnnotationConfigApplicationContext(JavaBuilder.class);
// Passando uma lista de classes anotadas
context = new AnnotationConfigApplicationContext(
JavaBuilder.class, DataSource.class);
// Passando o nome de um pacote base aonde buscar definições
context = new AnnotationConfigApplicationContext("br.com.casadocodigo");
91


## Página 102

4.4. ConfiguraçãoprogramáticacomJava CasadoCódigo
// Passando o nome de mais de um pacote aonde buscar definições
context = new AnnotationConfigApplicationContext(
"br.com.casadocodigo.java", "br.com.casadocodigo.daos");
Éinteressanteobservarque,aocontráriodaconfigura çãobaseadaemanota ções
comXMLemquepodemosusarfiltrosparadefiniroqueincluireoquenãoincluir
emnossocontainer,nãopossuímosesterecursousandoapenasosconstrutoresfor-
necidosporestaclasse.Paraquepossamospossuirumcontrolemaisfinosobrequais
definiçõesincluirusamosométodo register,querecebecomoparâmetrouma
listadeclassesanotadasaseremparseadaspelocontainer. Éummétodobastante
útilquandoqueremosaplicaralgumalógicaemcimadequaisbeansqueremosem
nossocontainercombaseemcondi çõesexternasànossaaplica ção.
Umbomusodestemétodopodeservistonoseguinteexemplo:
AnnotationConfigApplicationContext context =
new AnnotationConfigApplicationContext();
if (condição) {
context.register(DataSource.class);
} else {
context.register(DataSourceCustomizado.class);
}
context.register(DAOProduto.class, DAOUsuario.class);
// Atualiza a configuração do container após este ter sido alimentado
// com as classes acima
context.refresh();
Apóstermosinvocadoquantasvezesforemnecessáriasométodo registeré
importantequesejaexecutadoométodo refreshdocontainer,queiráatualizar
suasdefiniçõesinternasdebeans.
Parafinalizar,outrométodointeressantedestecontextodeaplica çãoé scan
querecebecomoparâmetroumalistadepacotesbaseaondeserãobuscadasclasses
anotadasaseremincluídasemnossocontainer. Umexemplodoseuusopodeser
vistonocódigoabaixo:
AnnotationConfigApplicationContext context =
new AnnotationConfigApplicationContext();
if (condição) {
context.scan("br.com.casadocodigo");
} else {
92


## Página 103

CasadoCódigo Capítulo4. MinimizandooXMLcomautowiring,anota çõeseJava
context.scan("br.com.casadocodigo2", "br.com.dao");
}
// Atualizamos o estado interno do container
context.refresh();
V antagens e limitações da configura ção Java
Agrandevantagemdaconfigura çãobaseadaemcódigofonteéapossibilidade
dodesenvolvedorpossuirmaiorcontrolesobreomodocomoseusbeanssãoinstan-
ciadoseseusestadosinternosdefinidos.ParaosquenãogostamdoformatoXML,
pode-sedizerqueoutragrandevantageméapossibilidadedenoslivrarmoscom-
pletamentedesteformato.
Éimportanteobservarnoentantoqueasconfigura çõesbaseadasemJavanãofo-
ramfeitasparasubstituircompletamenteoformatoXML,massimparaenriquecê-
lo,e,comotodaferramenta,deveserusadosemexcessospoispossuiagrandedes-
vantagemdesempreexigirrecompila çãodecódigofontequandoalgumaconfigu-
raçãoprecisaseralterada,oquetornaestaop çãomaisdifícildeseradotadaem
ambientesnosquaiscustomiza çãosejaumaprioridadealta.
4.5 XML, anotações ou configuração programá -
tica?
UmadasmaiorescríticasaoSpringFrameworksemprefoiofatodesteusarlongos
arquivosdeconfigura çãonoformatoXMLque,comovimosnestecapítulo,nem
sempreéomaisprodutivoparasetrabalhar.Sendoassimnestecapítulovimosal-
gumasrespostasaestacrítica.Paracome çar,fomosapresentadosao autowiringque
foionossoprimeiropassonaredu çãodaconfigura ção.Emseguida,conhecemosa
configuraçãobaseadaemanota çõesquereduziuaindamaisotamanhodosnossos
arquivosdeconfigura çãotransferindoaconfigura çãoparaclassesaoinvésdearqui-
vosexternose,finalmente,paraexcluircompletamenteosarquivosdeconfigura ção,
vimosaconfigura çãobaseadaemcódigoJavaquepermiteaodesenvolvedoraplicar
lógicanacomposi çãodadefini çãodenossosbeans.
Qualdastrêsformasdeconfigura ção(XML,anota çõesecódigoJava)éame-
lhornãoéumaperguntafactíveldeserrespondidadadoquecadaumaapresenta
vantagensedesvantagensúnicas.Anota çõeseJavanosobrigamarecompilarnosso
códigocasoocorramaltera ções,aopassoquedocumentosXMLconformeevoluem
vãosetornandocadavezmaisdifíceisdeseremmantidos.Nofinaldascontas,oque
93


## Página 104

4.5. XML,anotaçõesouconfigura çãoprogramática? CasadoCódigo
deveserlevadoemconsidera çãonãoéousoindividualdecadaumdestesformatos,
massimousocombinadodosmesmos.
94


## Página 105

Capítulo5
AOP:adicionandonovos
comportamentosaosbeans
Agrossomodo,pode-sedizerquedoisfatoreslevamumdesenvolvedoraadotaro
SpringFramework:ainversãodecontrole/inje çãodedependênciasquevimosexaus-
tivamentenostrêscapítulosanterioreseosuporteàprograma çãoorientadaaaspec-
tos-atãofaladaAOP( Aspect Oriented Programming)-oferecidopeloframework.
ÉgraçasàAOPqueoSpringforneceaodesenvolvedoracessoarecursos- servi-
ços corporativos-atéentãodisponíveisapenasemservidoresdeaplica çõespesados
comoWebLogic,WebSphere,JBosseoutros.EnquantoaIoCminimizaoproblema
doaltoacoplamento,aindarestaumtipodefuncionalidadequenormalmentese
encontrapulverizadaemnossossistemas,detalmodoqueaorienta çãoaobjetos
nãonospermiteisolardeumaformatãolimpaquantogostaríamos. Estetipode
funcionalidadeéchamadanojargãodaAOPde interesse transversal(cross-cutting
concern).


## Página 106

5.1. Comoidentificarosinteressestransversais CasadoCódigo
5.1 C omo identificar os interesses transversais
AmaiordificuldadeenfrentadanoprimeirocontatocomaAOPéacompreensãodo
quevêmaserum interesse transversal. Vamosexporesteconceitoescrevendoum
profilador( profiler)rudimentar.Umprofiladoréaferramentaqueusamosparades-
cobrirgargalosdeperformanceoumemóriaemnossossistemasapartirdamedi ção
dotempodeexecu çãoerecursoscomputacionaisconsumidosemtrechosdonosso
software.
Nãoprecisamosdeumprofiladorcompletoparadescobrirosgargalosdenossos
sistemas.Ocódigoabaixoexpõeumaprimeiraversãoquenospossibilitaráobtera
mesmafuncionalidade.
class DAO {
void persistirObjeto(Object obj) {
// obtenho o momento em que se iniciou a execução do código
long tempoInicial = System.currentTimeMillis();
// Executo o que realmente interessa neste método
getSessionFactory().currentSession().save(obj);
// Volto a obter o tempo total de execução
long tempoFinal = System.currentTimeMillis() - tempoInicial;
log.info("Método persistirObjeto levou " + tempoFinal + "ms");
}
}
Amesmaestratégiapoderiaseradotadaemoutrospontosdosistema,comopor
exemploemumaclasseresponsávelpelaemissãoderelatórios:
class Relatório {
void gerarRelatorio() {
// obtenho o momento em que se inicia a execução do código
long tempoInicial = System.currentTimeMillis();
// executo o código que gera o relatório
// (...)
// obtenho o tempo final de execução
long tempoFinal = System.currentTimeMillis() - tempoInicial;
log.info("Método gerarRelatorio levou " + tempoFinal + "ms");
96


## Página 107

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
}
}
Observandoosdoistrechosacima,ficanítidoqueaúnicavaria çãoéoobjetivo
decadamétodo:poisocódigoqueosenvolveébasicamenteomesmo.Estecódigo
duplicadoéoquechamamosde interesse transversal. Umaprimeiratentativade
modularizá-lopoderiaserisolando-oemumaclasse. Estaimplementa çãoéoque
nojargãodaAOPchamamosde aspecto(aspect),queestáparaaAOPassimcomo
aclasseestáparaaprograma çãoorientadaaobjetos.
Nossaprimeiraimplementaçãodesteaspectorudimentarpodeservistanaclasse
aseguir:
class Profilador {
private long tempoInicial;
private long tempoFinal;
// Obtém o tempo inicial de execução
public void iniciarMedicao() {
tempoInicial = System.currentTimeMillis();
}
// Obtém o tempo final de execução
public void finalizarMedicao() {
tempoFinal = System.currentTimeMillis();
}
// Retorna o tempo total de execução
public long tempoExecucao() {
return tempoFinal - tempoInicial;
}
}
Temosaimpressãoinicialdefinalmenteterconseguidoisolarafuncionalidade
alvo. Agorabastainjetaraclasse Profiladornasclassesquepretendemosmediro
tempodeexecu ção,isolandoachamadaaométodoe voilà:,modularidadeobtida,
certo?Errado:tudooquefizemosfoiadicionarmaisumadependêncianestasclas-
seseassimaumentaroproblemadoaltoacoplamento.Alémdesteefeitocolateral,
analisandomelhoroproblemapercebe-sequeomesmocódigorepetidoirávoltar
aosistema,sóquedeoutraforma,ouseja,temosumasolu çãoilusóriaparanosso
problema.
Comoveremosnorestantedestecapítulo,aAOPnospermiteimplementaras-
pectossemquesetornenecessáriaainclusãodemaisdependênciasaocódigofonte.
97


## Página 108

5.2. EntendendoAOP CasadoCódigo
5.2 E ntendendo AOP
QuandoestivermosfalandoemAOPsempretenhaemmenteaideiadequecom
elaestamosnarealidade interceptandoaexecuçãodosmétodospresentesemnos-
sos beans.Agrossomodo,escreveremosinterceptadorescapazesdealterarofluxo
originaldeexecu çãodonossocódigo. Osobjetoscujaexecu çãoseráinterceptada
tambémpossuemumnomedentrodojargãodaAOP: objeto alvo(target objects).
Nosexemplosexpostosanteriormente,nossos objetos alvoseriamasinstânciasdas
classes Relatórioou DAO.
Omaisinteressanteéqueo objeto alvonãoprecisaimplementaralgumainter-
faceoupossuirocódigorepetidoapresentadoanteriormente,preocupando-sepor-
tantoapenascomarazãopelaqualfoiimplementado. Oleitoratentodeveestar
seperguntandocomoissoépossível?Entraemcenaoutroconceitoimportantena
implementaçãoAOPdoSpring:os objetos proxiados(proxy objects).
Quandofalamosemclasses proxy,estamosnosreferindoaopadrãodeprojeto
demesmonomequesetornoupopularcomolivro“PadrõesdeProjeto”[11]daGoF.
Éumpadrãoestruturalcomoobjetivodecontrolaroacessoaumobjeto.
Asoluçãopropõeaexistênciadepelomenostrêselementos:aclassecliente,o
proxyeaclassealvo.Aplicando-seaboapráticadaprograma çãoorientadaaobjetos
decodificarmosparainterfaces,teremosasclasses proxyealvoimplementandouma
interfaceemcomum:interfaceestaqueseráadependênciadaclasseclientecomo
podeservistonodiagramaabaixo:
98


## Página 109

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
Figura5.1:OpadrãoProxy
Quandooobjetoclienteinvocaummétododainterface,estenarealidadeestará
acessandooobjeto proxy,queseencarregarádeexecutarounão,deacordocomas
regrasdeacessoqueimplementarmosemnosso proxy,ométodooriginaldaclasse
alvo.Umbomexemplodeaplica çãode proxiessãoframeworksdeseguran çacomo
oSpringSecurity,queestudaremosmaisafundoaindanesselivro,masjápodemos
adiantarquelá,o proxyéimplementadodetalformaqueaidentifica çãodousuário
permitaounãoaexecu çãodosmétodosquedesejamosproteger.
NaplataformaJavanãoénecessárioqueasclassesalvoe proxyimplementema
mesmainterface:paradizeraverdade,o proxymuitasvezeségeradodinamicamente
usando-sebibliotecasdemanipula çãode bytecodecomoCGLIB,ASMoumesmoo
suportequeopróprioJavaSEofereceparaestefim.
99


## Página 110

5.3. Preparandooambientededesenvolvimento CasadoCódigo
Figura5.2:Proxies
Graçasaos proxies,nãoprecisamosmodificarnossosobjetosalvo. Nestemo-
mentooutradúvidasurge:comosedefinequaismétodosdevemserinterceptados?
OfazemosusandoalgumaregraoulinguagemdeexpressãoquenojargãodaAOP
chamamosde pontos de corte(point cuts).Apropósito,os métodos interceptadostam-
bémpossuemumnomeespecial,sãoos pontos de junção(join points).
Sendoassim,eiscomoaAOPfuncionanoSpring:o objeto alvoéencapsulado
porum proxy,quandoalgumaclasseclientefazumachamadaaalgumdeseus pontos
de junção,o proxyexecutaoaspectoantesouapósos join pointseestes,finalmente,
serãoounãoexecutadosdeacordocomoaspectoimplementado.
Esabeestaop çãoporexecutaroaspectoantesoudepoisdo join point?Também
temumnome:sechama advice.Nestasessãotemosportantoumadescri çãointuitiva
decomoaAOPfunciona.Nossopróximopassoserávê-lanaprática.
5.3 P reparando o ambiente de desenvolvimento
GraçasànaturezamodulardoSpring,éperfeitamentepossívelusaroframework
semseusuporteàAOP,queatualmentevêmemduasop ções:atradicionalbaseada
naAPIdopróprioSpringouabaseadaemesquemasXMLeasintaxededefini-
çãode point cutsdoAspectJ,queéumprojetoquetemcomoobjetivotrazerparaa
plataformaJavaumaimplementa çãocompletadesteparadigmadeprograma ção.
Quaiscomponentesdevemserinseridosemseuprojetoéportantoumaquestão
determinadapelocaminhoaseguir:APIdoSpringouAspectJ?
Emambososcasos,adependênciaobrigatóriaéo spring-aop.Lembre-sede
secertificardequeestepossuiamesmaversãodosdemaismódulosdoSpringque
100


## Página 111

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
seuprojetofazreferência.CasoestejausandooMaven,bastainseriraconfigura ção
abaixonoseuarquivo pom.xml.
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-aop</artifactId>
<version>3.1.1.RELEASE</version>
</dependency>
Emdiversassitua çõesosobjetosalvonãoimplementarãoumainterfaceespecí-
fica,tornando-senecessáriaportantoagera çãode proxiesdinamicamente.Torna-se
necessáriaainclusãodabibliotecaCGLIB2emseuprojeto,cujaconfigura çãodo
Mavensegueaseguir:
<dependency>
<groupId>cglib</groupId>
<artifactId>cglib</artifactId>
<version>2.2.2</version>
</dependency>
Finalmente,casosejafeitaaescolhapelosuporteaoAspectJ,algumasbibliotecas
deste frameworktambémdevemserincluídas:
<dependency>
<groupId>org.aspectj</groupId>
<artifactId>aspectjrt</artifactId>
<version>1.6.12</version>
</dependency>
<dependency>
<groupId>org.aspectj</groupId>
<artifactId>aspectjweaver</artifactId>
<version>1.6.12</version>
</dependency>
Evite dores de cabeça com incompatibilidade de versões
UmproblemacomumaosqueseiniciamnoSpringFrameworkdizrespeito
aconflitosdeversãodosmódulosdoSpring. Muitasvezestopamoscomexce-
çõesemtempodeexecu çãodotipo LinkageError, NoClassDefFoundError,
NoSuchMethodError, NoSuchFieldErrorou ClassNotFoundException.
Naesmagadoramaioriadasvezes,esteproblemaocorrepoistemosmódulosdo
Springcomversõesdiferentesno classpathdosistema.
101


## Página 112

5.4. Aimplementaçãodoprimeiroaspecto CasadoCódigo
CasoestejausandoMaven,umaboasolu çãoparaevitarestetipodeproblemaé
ainclusãodepropriedadesnoarquivodeconfigura ção,cujoconteúdocorresponda
àversãodoSpringemusonoprojeto.Umexemplodousodepropriedadespodeser
vistonoarquivo pom.xmldeexemploaseguir:
<project>
(...)
<properties>
<!--
Repare: o nome da tag corresponde ao nome da propriedade.
-->
<spring.versao>3.1.1.RELEASE</spring.versao>
</properties>
<dependencies>
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-core</artifactId>
<!-- Usamos uma sintaxe similar à EL do
JSP para inserir a propriedade no conteúdo do XML -->
<version>${spring.versao}</version>
</dependency>
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-aop</artifactId>
<version>${spring.versao}</version>
</dependency>
</dependencies>
(...)
</project>
5.4 A implementação do primeiro aspecto
Amelhormaneiraqueconhe çoparaentenderamecânicaportrásdaAOPéusando
aAPIdoSpring.Apesardeserumaop çãobemmenospopularatualmente,pornão
tirarproveitodasanota çõesedosesquemasXML,éumaop çãoqueaindasemostra
bastanteválida.
Iremoscontinuaroproblemadonossoprofiladorque,destavez,seráaplicado
àclasse DAOPessoas,quelêepersisteumalistadeobjetosdotipo Pessoaecuja
implementaçãopodeservistanocódigoaseguir:
102


## Página 113

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
public class DAOPessoas {
public void persistir(Pessoa[] pessoas, File arquivo)
throws IOException {
if (pessoas == null || pessoas.length == 0) {
throw new IllegalArgumentException(
"Lista de pessoas nula ou vazia");
}
if (arquivo == null) {
throw new IllegalArgumentException(
"Arquivo nulo passado como parâmetro");
}
ObjectOutputStream oos =
new ObjectOutputStream(new FileOutputStream(arquivo));
oos.writeObject(pessoas);
oos.close();
}
public Pessoa[] ler(File arquivo) throws IOException {
ObjectInputStream ois =
new ObjectInputStream(new FileInputStream(arquivo));
Pessoa[] resultado = null;
try {
resultado = (Pessoa[]) ois.readObject();
} catch (ClassNotFoundException ex) {
throw new IOException(
"Erro ao ler arquivo. ClassNotFoundException", ex);
}
return resultado;
}
}
5.5 E ntenda os advices
Comomencionadoacimanestecapítulo,o adviceéocomponentedaAOPresponsá-
velpordefiniromomentoemqueumaspectodeveserexecutado.OSpringoferece
algunstiposde advicesquepodemserimplementadospeloprogramador.Éimpor-
tantemencionarqueaimplementa çãoAOPdoSpringnãoétãocompletaquantoa
doAspectJ,poissóinterceptaexecu çãodemétodos.Nãoháintercepta çãodemodi-
ficaçãodeatributosouconstrutores,comonoAspectJ.
Noentanto,estalimita çãonãoéumproblemaparaaesmagadoramaioriados
103


## Página 114

5.6. Useosaroundadvices CasadoCódigo
projetos,poisrarasvezestopamoscomestescasos.Quandoháumadefini çãodeatri-
butos,poderíamosinterceptarummétodo:setter ao invés do atributo diretamente, e
no caso do construtor, poderíamos interceptar umfactorymethod::.
Abaixoseguemostiposde advicesuportadospeloSpring:
•before:éinvocadoantesdaexecu çãodométodoalvo( point cut);
•after throws:invocadocasosejadisparadaumaexce çãoapósaexecu ção
dométodoalvo;
•after returning:invocadoquandodeterminadotipoderetornoouvalor
éretornadoapósaexecu çãodométodoalvo;
•introduction:dizrespeitoàintrodu çãodemétodosemobjetos proxypelo
Spring(veremosmaissobreeste adviceemumcapítuloaparte).
5.6 U se os around advices
Como nosso objetivo é medir o tempo de execução dos métodos da classe
DAOPessoas,nossoprofiladordeveexecutartrêspassos:
• Obteromomentoemqueaexecuçãodométodoalvoéiniciada;
• Executarométodoalvo;
• Obteromomentoatualesubtraí-lodomomentoinicialparadescobrirquanto
tempolevouaexecu çãodométodoalvo.
Precisamosportantodeum advicedotipo around,queétambémomaisgené-
ricopossível,poiselenospermitiráexecutaralgoanteseapósométodoqueserá
interceptado.
ParaqueestesejaimplementadousandoaAPIdoSpringbastaescrevermos
umaclassequeimplementeainterface org.aopalliance.intercept.MethodInterceptor,
talcomofoifeitonocódigoaseguir:
import org.aopalliance.intercept.MethodInterceptor;
import org.aopalliance.intercept.MethodInvocation;
public class AdviceAroundProfilador implements MethodInterceptor {
private List<Long> tempos = new ArrayList<Long>();
104


## Página 115

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
public List<Long> getTempos() {return tempos;}
public Object invoke(MethodInvocation invocation) throws Throwable {
long momentoInicial = System.currentTimeMillis();
/*
O método proceed executa a invocação do método
que estamos interceptando nos fornecendo seu
valor de retorno.
Assim é possível, por exemplo, substituir o valor retornado
para a classe cliente do objeto proxiado ;)
*/
Object resultado = invocation.proceed();
long tempo = System.currentTimeMillis() - momentoInicial;
getTempos().add(tempo);
System.out.println("Tempo para executar " + tempo + "ms");
/*
Na linha abaixo retornamos o resultado da invocação do
método interceptado
*/
return resultado;
}
}
A interface MethodInterceptor requer a implementação de um
único método, invoke, que recebe como parâmetro um objeto do tipo
MethodInvocation, que representa, como o próprio nome já nos diz, a in-
vocaçãodeummétodo.Nesteobjeto,noentanto,ométodoquemaisnosinteressa
é proceed,queretornaumobjetodotipo java.lang.Object,querepresenta
oretornodométodoalvo.
Nossa implementação é portanto bastante simples: a única diferença é que
os tempos de execução são todos adicionados ao atributotempos, do tipo
java.util.Listparaconsultafutura.
Umpontoimportanteemnossoprofiladoréofatodestesercompletamentein-
dependentedequalquertipodeobjetoalvo.Tantofazseestouinterceptandoaexe-
cuçãodeumobjetodotipo DAOPessoasou GeradorRelatorios,tudooque
realmenteinteressaparanossoaspectoéqueométodosejaexecutadoeseutempode
105


## Página 116

5.7. Useoadvicebefore CasadoCódigo
respostamedido.Aindamaisimportante,comestanossaimplementa çãodoaspecto
garantimosque DAOPessoasnãoprecisesaberdaexistênciadeumprofilador.
5.7 U se o advice before
Finalizadaaimplementa çãodenossaclasse DAOPessoas,surgeumnovorequisito:
precisamosevitarqueestaclassesobrescrevaarquivosjáexistentes.Asolu çãoime-
diataparaesterequisitopoderiaserincluirmaisumtrechodeverifica çãonométodo
persistir,comonoexemploaseguir:
public void persistir(Pessoa[] pessoas, File arquivo)
throws IOException {
if (pessoas == null || pessoas.length == 0) {
throw new IllegalArgumentException(
"Lista de pessoas nula ou vazia");
}
if (arquivo == null) {
throw new IllegalArgumentException(
"Arquivo nulo passado como parâmetro");
}
// Nossa nova validação
if (arquivo.exists()) {
throw new IllegalArgumentException(
"O arquivo já existe e não pode ser sobrescrito!");
}
(...)
}
Emumprimeiromomento,estapareceserumaótimasolu ção. Masesequi-
sermosincluiraindamaisrestri çõescomo,porexemplo,limitarquaisosdiretó-
riosaondenosso DAOpossagerararquivosoumesmoonúmeromáximodepes-
soasquepossamserinseridas? Iremosaumentarindefinidamentenossométodo
persistir? AOPsalvanossapelecomo advicedotipo before,queéexecutado
antesqueométodoalvosejachamado.
Um objeto alvo pode ter quantosadvices de determinado tipo quanto se-
jamnecessáriosparaummesmométodo. Sendoassim,poderíamosimplemen-
tar um novoadvicepara cada nova restrição. Para mantermos a facilidade de
106


## Página 117

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
compreensãodestetexto, vamosimplementarapenasumqueverifiqueseoar-
quivo em cima do qual serão persistidos os objetos do tipoPessoa exista
ou não. Para tal, basta escrevermos uma classe que implemente a interface
org.springframework.aop.MethodBeforeAdvice,comonocódigoaseguir:
import java.io.File;
import java.lang.reflect.Method;
import org.springframework.aop.MethodBeforeAdvice;
public class AdviceBeforeProfilador implements MethodBeforeAdvice {
public void before(Method method, Object[] args, Object target)
throws Throwable {
if (method.getName().equals("persistir") && args[1] != null) {
File arquivoAlvo = (File) args[1];
if (arquivoAlvo.exists()) {
System.out.println("Before Advice: arquivo já existe");
args[1] = null;
}
}
}
}
Comopodeservisto,estainterfacerequerquesejaimplementadoumúnico
métodochamado before,querecebecomoparâmetrosumainstânciadoobjeto
Method,querepresentaométodointerceptado,eum arrayde Object,repre-
sentandoosvaloresqueserãopassadosaométodoalvoeporúltimooobjetoalvo
quefoiinterceptado.Paraquenossaregrasejaaplicável,tiramosproveitodocom-
portamentopadrãodométodo persistirde DAOPessoas,quesempredispara
umaexceçãodotipo IllegalArgumentException,casoumainstânciadotipo
java.io.Filenãosejapassadacomoparâmetro.
Paratal,verificamosseométodo existsdoatributo Filequeseriapassado
aométodoalvoretornaverdadeiro. Emcasopositivo,nóssubstituímosseuvalor
namatrizpor null. Sim,vocêleucerto: nóspodemosalterarquaisosparâme-
trospassadosaométodoalvodentrodo advicedotipo before,assimcomotambém
poderíamosfazerno advicedotipo around.
107


## Página 118

5.8. EondeentraoProxynessahistória? CasadoCódigo
Cuidado com os aspectos que escreve
Imagine um programador dando manuten ção na classe
DAOPessoas e se deparando com umbug do tipo: “O Sistema
nãopermitepersistirarquivosnodiretório”. Umadesuasprimeiras
atitudespoderiaseraescritadeumtesteunitárionoqualasitua ção
descrita fosse reproduzida e, para sua surpresa, o código naquele
momentofuncionariaperfeitamente.
Horasehorasdetrabalhodepois,nossoexaustoprogramadorseen-
contracomoutrocolegaque,orgulhoso,descreveoseutrabalhonaes-
critadeum advicequealteraovalordosparâmetrospassadosparaesta
classeusandoAOP.
Apossibilidadedemodificarmosovalordeparâmetrosaseremen-
viadosaobjetosalvoouaindalógicasmaiscomplexaseintrusivascomo
anãoexecu çãodemétodos,sãoferramentaspoderosasquedevemser
usadascomcautela.Antesdeexecutarestetipodeatividade,lembre-se
dequeoobjetoalvonormalmenteéimplementadotendocomobaseum
cenáriooriginal,diferentedoquedeuorigemaoaspectomodificador.
Comoboaprática,semprequeaestratégiademodifica çãodeparâ-
metrosfornecessária,certifique-sededocumentá-laeinformartodaa
equipeaseurespeito,poisistopodesalvarhorasdetrabalhodosdesavi-
sadosetalvezatémesmoalgumasamizades.Épossívelminimizarainda
maisoproblemacomapresen çadetestesintegrados,queverifiquemo
comportamentodenossos beans,aoinvésdenossasclassesisolada-
mente.
5.8 E onde entra o Proxy nessa história?
Isoladamente, os advices que implementamos não irão habili-
tar a AOP. Para que isto ocorra faz-se necessário que declaremos
nosso objeto proxy. Para tal, usaremos uma instância da classe
org.springframework.aop.framework.ProxyFactoryBean. A maneira
maisfácildeentenderseufuncionamentoéatravésdaconfigura çãoXML:
<beans>
108


## Página 119

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
<!-- O nosso objeto alvo -->
<bean id="daoPessoasTarget" class="casadocodigo.DAOPessoas"/>
<!-- Nosso advice do tipo around -->
<bean id="aroundProfilador"
class="casadocodigo.api.AdviceAroundProfilador"/>
<!-- Nosso advice do tipo before -->
<bean id="beforeProfilador"
class="casadocodigo.api.AdviceBeforeProfilador"/>
<bean id="daoPessoas"
class="org.springframework.aop.framework.ProxyFactoryBean">
<property name="target" ref="daoPessoasTarget"/>
<property name="interceptorNames">
<list>
<value>aroundProfilador</value>
<value>beforeProfilador</value>
</list>
</property>
</bean>
</beans>
Comopodeserobservado,declaramosnossos adviceseobjetoalvocomosefos-
sem beansconvencionaisaseremgerenciadospelo container. Logoemseguida,o
quefazemosédefinirduasimportantesdependênciasdo bean daoPessoas,que
seráoproxyacessadopelasclassesclientes: target,querecebecomovaloro bean
daoPessoasTargete interceptorNames,quepossuirácomovalorumalista
queapontaparaosdois advicesquedeclaramosemnossoarquivodeconfigura ção.
Parailustrarousodaclasse proxyporumcliente,escrevemosumpequenoteste
cujaimplementaçãopodeservistaadiante:
DAOPessoas dao = (DAOPessoas) applicationContext.getBean("daoPessoas");
// Deve ser retornado o proxy, e não o objeto alvo
assert dao.getClass().equals(DAOPessoas.class) == false;
/* Suponha a existência dos objetos pessoas (do tipo Pessoa[])
e arquivo (do tipo File) */
dao.persistir(pessoas, arquivo);
109


## Página 120

5.9. Entendaaexecução CasadoCódigo
// Obtenho a instancia do advice around
AdviceAroundProfilador around =
applicationContext.getBean(AdviceAroundProfilador.class);
/*
Se executei o método, o tempo de execução
obrigatoriamente precisa estar armazenado
na lista de tempos do advice around
*/
assert ! around.getTempos().isEmpty();
/*
Agora é testada a execução do advice before.
Tentaremos executar o método persistir no mesmo
arquivo usado anteriormente. Uma exceção do tipo
IllegalArgumentException deverá portanto ser disparada,
pois o parâmetro arquivo será substituído por null pelo
advice.
*/
try {
dao.persistir(pessoas, arquivo);
} catch (IllegalArgumentException ex) {
assert "Arquivo nulo foi passado".equals(ex.getMessage());
}
5.9 E ntenda a execução
Combasenocódigoproduzido,atéentãopossuímosaseguintesequênciadeexecu-
çãoquandoumaclasseclienteacessanosso proxy:
1) Clienteinvocamétodopersistirnoobjeto proxy;
2) Proxybuscaporalgumadvicedotipo beforee,existindo,executa-o;
3) Proxybuscaporalgumadvicedotipo arounde,existindo,executa-o;
4) Oproxydotipo aroundexecutaométododoobjetoalvoeoretornaparao proxy;
5) Proxyretornavalorretornadoaoobjetocliente.
]
110


## Página 121

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
5.10 U m uso interessante para AOP: Log de erros
Parafinalizarnossase çãosobreousotradicional,quetalmaisumexemploprático?
Precisamosregistraromomentoemquealgumparâmetroinválidoéfornecidoao
nossoDAO.Entraema çãoo advicedotipo after throws.Escreverum advicedeste
tipoébastantesimples:bastaqueduasregrassejamseguidas:
• Aclassedeveimplementarainterfaceorg.springframework.aop.ThrowsAdvice;
• Devemserimplementadosumoumaismétodosdotipo voidcujonome
é afterThrowingequerecebacomoparâmetroumaexce çãodequalquer
tipo.
Ainterface ThrowsAdviceénarealidadeumainterfacedemarca ção,ouseja,
estanãoobrigaodesenvolvedoraimplementarnenhummétodo.Entraema çãoa
convençãodefinidapeloSpring,cujaaplica çãopodemosvernoexemplo:
import org.springframework.aop.ThrowsAdvice;
public class AdviceAfterThrows implements ThrowsAdvice {
// Restante da classe oculto para facilitar a leitura
// Interceptando exceções do tipo IllegalArgumentException
public void afterThrowing(IllegalArgumentException ex) {
enviarEmail("Parâmetros inválidos: " + ex.getMessage());
}
// Interceptando exceções do tipo IOException
public void afterThrowing(IOException ex) {
enviarEmail("IOException: " + ex.getMessage());
}
}
Nocódigoanteriorvemosqueomesmo advicepodeinterceptarmaisdeum
tipodeexce ção.Nestecaso,astrataremostantodotipo java.io.IOException
quanto java.lang.IllegalArgumentException.Assim,semprequeumerro
dostipostratadosforemdisparadospornossosobjetosalvo,ume-mailseráenviado
paraoadministradordosistema.Novamente,nãohámuitooqueseralteradoem
nossaconfiguraçãoXML,cujoresultadofinalpodeservistoaseguir:
111


## Página 122

5.11. DeclareaspectoscomanotaçõesAspectJeesquemasXML CasadoCódigo
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd">
<!-- O nosso target object -->
<bean id="daoPessoasTarget" class="casadocodigo.DAOPessoas"/>
<!-- Nosso advice do tipo around -->
<bean id="aroundProfilador"
class="casadocodigo.api.AdviceAroundProfilador"/>
<!-- Nosso advice do tipo before -->
<bean id="beforeProfilador"
class="casadocodigo.api.AdviceBeforeProfilador"/>
<!-- Advice do tipo after throws -->
<bean id="afterThrows" class="casadocodigo.api.AdviceAfterThrows"/>
<bean id="daoPessoas"
class="org.springframework.aop.framework.ProxyFactoryBean">
<property name="target" ref="daoPessoasTarget"/>
<property name="interceptorNames">
<list>
<value>aroundProfilador</value>
<value>beforeProfilador</value>
<!-- Inclusão do after throws -->
<value>afterThrows</value>
</list>
</property>
</bean>
</beans>
5.11 D eclare aspectos com anotações AspectJ e es-
quemas XML
Finalmente,temosaformamaismodernaeatualmentemaispopulardedeclararmos
nossosaspectoscomSpringusandoesquemasXMLeAspectJ.
112


## Página 123

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
ÉimportanteesclarecerquequandonosreferimosaoAspectJ,narealidadeapon-
tamosparaummododedeclara çãodeaspectosbaseadoemanota ções. Curiosa-
mente,porpadrãooSpringnãovêmcomsuporteàtodososrecursosoferecidos
peloAspectJ:usaremosapenassuasintaxeparadefini çãode point cutseasanota-
çõesaqueeste frameworkoferecesuporte. Portrásdospanostemosnarealidade
amesmaAPIdoSpringparasuporteàAOPquevimosnase çãoanterior,coma
diferençadequeagoraestaseencontra“disfarçadadeAspectJ”.
Comoveremos,hátambémumnovoesquemaXMLaseraprendido,queadici-
onasemânticaespecíficaaosuporteaAOP.Comistoaleituradosnossosarquivos
deconfiguraçãoficamaisfácildesercompreendidaepoderemosidentificarmais
claramentenestaquemsãoos beansconvencionaisequaisosnossosaspectos.
Incluindo o novo esquema em nosso arquivo de configuração
EsquemasXMLnospossibilitamadicionarnovoselementosanossosarquivos
deconfiguraçãoXMLdoSpring.ParaoferecersuporteaoAspectJdevemosinserir
adefiniçãodonamespace aopnoelemento <beans>denossoarquivodeconfigu-
ração,talcomonoexemploabaixo:
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:aop="http://www.springframework.org/schema/aop"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
http://www.springframework.org/schema/aop
http://www.springframework.org/schema/aop/spring-aop-3.1.xsd">
(...)
</beans>
Casoestejatrabalhandocomo SpringSource T ool Suite,ainclusãodesteesquema
éaindamaisfácil.Bastaabrirseuarquivodeconfigura çãodoSpringeescolheraaba
Namespaces,talcomopodeservistonaimagemaseguir.
113


## Página 124

5.11. DeclareaspectoscomanotaçõesAspectJeesquemasXML CasadoCódigo
Figura5.3:UsandooSpringSourceToolSuiteparaadicionarumnovoesquema
Emseguida,bastaselecionaronamespace aopnopainelàesquerdaqueauto-
maticamenteaIDEmodificaráoarquivoparavocê.
Declarando aspectos com @Aspect
Comonamespace aopincluídoemnossoarquivodeconfigura ção,nossopró-
ximopassoéinstruí-loafazerduascoisas: amaisóbviaqueéinformá-lodeque
usaremosanotaçõesparadefinirnossos beansehabilitaroesquemade auto proxy
doAspectJ.Voltandoaoexemploquevêmnosacompanhadonestecapítulo,nosso
arquivodeconfigura ção,excluindoasdefini çõesde namespacesparafacilitaralei-
tura,deveficartalcomonocódigoadiante:
<beans>
<!-- Informamos o container que iremos usar anotações -->
<context:annotation-config/>
<!-- Habilitando o auto proxiamento do AspectJ -->
<aop:aspectj-autoproxy />
<!-- Em que pacote nossos aspectos se encontram -->
<context:component-scan
base-package="casadocodigo.aspectj.anotacoes"/>
114


## Página 125

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
<!-- O objeto alvo -->
<bean id="daoPessoas" class="casadocodigo.DAOPessoas"/>
</beans>
A única alteração incluída em nosso arquivo de configuração foi a tag
<aop:aspectj-autoproxy />.Podemosveraquiaplicadoopoderdesimplifi-
caçãoqueanota çõeseesquemasXMLnosfornecemdemaneiraimediata.Enquanto
usandoaAPIpadrãodoSpringprecisamosescrever14linhassignificativasdeconfi-
guração,agoraprecisamosescreverapenas4:nossaconfigura çãoficou“apenas”72%
menor.
Configuraçãopronta,agoraprecisamosapenasescrevernossosaspectos. Para
começar,vamosvercomoimplementaromaisgenéricodosadvicesqueéo around.
Nossanovaimplementa çãopodeservistaabaixo:
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;
@Aspect // Identifica o bean como um aspecto
@Component // Identifica o aspecto como um bean
public class AdviceAroundProfiladorAnotacoes {
private List<Long> tempos = new ArrayList<Long>();
public List<Long> getTempos() {return tempos;}
@Around("execution(* casadocodigo.DAOPessoas.* (..))")
public Object profilar(ProceedingJoinPoint joinPoint)
throws Throwable {
long momentoInicial = System.currentTimeMillis();
Object resultado = joinPoint.proceed();
long tempo = System.currentTimeMillis() - momentoInicial;
tempos.add(tempo);
System.out.println("Tempo para executar = " + tempo + "ms");
return resultado;
}
115


## Página 126

5.12. AsintaxeAspectJdedeclaraçãodepointcuts CasadoCódigo
}
Ficaclaroqueébasicamenteamesmaimplementa çãodonossoprofilador.Adi-
ferençaestánofatodeincluirmosduasnovasanota ções. @Aspect,comoopróprio
nomediz,identificaum beancomoumaspecto.Jáaanota ção @Aroundidentifica
queométodo profilar-queobrigatoriamentedevereceberumparâmetrodo
tipo ProceedingJoinPoint-éum advicedotipo around.
Omaisinteressantedousodasanota çõeséquepodemostermaisdeum ad-
vicedomesmotipo- around-implementadoemumamesmaclasse:bastaincluir
maisanotações @Aroundemseucorpo. Oleitordeveestarcuriosoarespeitodo
significadodoparâmetroquepasseiparaestaanota ção,certo?
5.12 A sintaxe AspectJ de declaração de point cuts
Comomencionado,umadasmaioresvantagensdoAspectJéasuasintaxeparade-
finiçãode point cuts. Comovistoemnossoúltimoaspecto,aanota ção @Around
recebecomoparâmetroumaexpressão.Oassuntodestase çãoserájustamenteen-
tenderoqueestasignifica.
CasovocêjátenhatrabalhadocomAspectJ,éimportantemencionarque,como
oSpringnãooferecesuportea100%deste framework,etambémpelofatodenossa
AOPsercompletamentebaseadaem proxies,nãohásuportenativoparatodasas
possibilidadesqueestalinguagemparadefini çãode point cutsnosoferece,oquenão
éemsiumagrandedesvantagem,vistoqueosuportadodarácontadaesmagadora
maioriadassitua çõesencontradasnodesenvolvimentodeaplica çõescorporativas.
Asintaxeaplicadaérazoavelmentesimpleseaimagemabaixonosajudaráa
entendê-lamelhor:
116


## Página 127

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
Figura5.4:Definindoumpointcut
Oprimeiroelementosempreéogatilhoresponsávelpordispararoaspecto.Na
esmagadoramaioriadasvezesesteserádotipo executionque,comoopróprio
nomejádiz,identificaaexecu çãodométodoalvo. Porestarazãonestecapítulo
daremosmuitomaisaten çãoaestetipo.
Tipos de gatilho mais comuns
•execution():identificaaexecu çãodométodoalvo.
•within():defineumjoinpointdentrodeumconjuntodetipos.
•this():oaspectoseráaplicadoaobjetosdotipodobeandecla-
rado.
•annotation(): identificajoinpointsdeacordocomasanota-
çõespassadascomoparâmetro.
•args:identificajoinpointsquerecebamdeterminadalistadepa-
râmetros.
Ogatilho executionrecebecomoparâmetroaespecifica çãodométodoalvo,
queécompostaporquatrocomponentes.Oprimeirodizrespeitoaotipoderetorno
esperado,seguidodocaminhocompletoatéaclasse,nomedométodoe,finalmente,
quaisosparâmetrosqueestereceberá.
117


## Página 128

5.12. AsintaxeAspectJdedeclaraçãodepointcuts CasadoCódigo
Éimportantemencionarquepodemosusarcaracterescoringanadeclara çãodo
nomedaclasseemétodoalvo,talcomopodemosvernosexemplos:
/*
O método pode retornar qualquer valor. A classe pode estar
em qualquer pacote, porém deve se chamar 'DAOPessoas'.
O método pode possuir qualquer nome, o que indica que pegaremos
todos os métodos, ignorando os parâmetros que estes possam receber.
*/
execution(* *.DAOPessoas.*(..))
/*
Todas as classes cujo nome comece com 'DAO', levando em consideração
apenas os métodos chamados 'ler' ignorando os parâmetros recebidos e
o tipo de retorno
*/
execution(* *.DAO*.ler(..))
/*
Todos os métodos do tipo void de qualquer classe do pacote casadocodigo
ignorando os parâmetros
*/
execution(void casadocodigo.*(..))
/*
Todos os métodos que recebam como parâmetro um objeto do tipo File
pertencentes ao pacote casadocodigo
*/
execution(* casadocodigo.*(java.io.File))
/*
Execução de qualquer método público de qualquer bean
*/
execution (public * *(..))
Outrogatilhointeressanteéo @annotation,quenospermitecriar join points
paratodasasclassesquepossuamdeterminadaanota ção.Oexemploabaixolevaem
118


## Página 129

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
consideraçãotodasasclassesquepossuamaanota ção @ComponentdoSpring.
@annotation(org.springframework.stereotype.Component)
OSpringtambémestendeoconjuntodegatilhoscomotipo bean,quenos
permitereferenciarum beanporumnomeespecíficoouusandocaracterescoringa
comonosexemplosabaixo:
/* Aponta para ao bean daoPessoas */
bean("daoPessoas")
/* Aponta para qualquer bean cujo nome comece com 'dao' */
bean("dao*")
Éinteressantemencionarquetambémpodemosaplicarexpressõeslógicasna
definiçãodenossos point cuts.
Escrevendo outros tipos de advices
Tirandoproveitodasanota ções,podemosvercomoimplementarmaisdeum
tipode adviceemumamesmaclasse,comonocódigoaseguir:
@Aspect
@Component
public class AdviceAroundProfiladorAnotacoes {
private List<Long> tempos = new ArrayList<Long>();
public List<Long> getTempos() {
return tempos;
}
// Nosso advice do tipo around
@Around("execution(* casadocodigo.DAOPessoas.*(..))")
public Object profilar(ProceedingJoinPoint joinPoint)
throws Throwable {
long momentoInicial = System.currentTimeMillis();
Object resultado = joinPoint.proceed();
long tempo = System.currentTimeMillis() - momentoInicial;
tempos.add(tempo);
System.out.println("Tempo para executar = " + tempo + "ms");
return resultado;
119


## Página 130

5.12. AsintaxeAspectJdedeclaraçãodepointcuts CasadoCódigo
}
// Mais de um advice pode ser declarado na mesma classe
// quando usamos anotações
}
Osparâmetrospassadosaos advicesdetipo beforeou after throwing são
opcionais. Paraadvicesdotipo before,comopodemosveraseguir,épossívelpas-
sarinformaçõesarespeitodo join pointdefinindoumparâmetrodeentradadotipo
org.aspectj.lang.JoinPoint,quenospermite,comopôdeservistoanterior-
mente,interceptarosparâmetrosqueserãopassadosaométodoalvo.
@Aspect
@Component
public class AdviceAroundProfiladorAnotacoes {
// acima está o nosso advice do tipo around
// Advice do tipo before
@Before("execution(* casadocodigo.DAOPessoas.persistir(..))")
public void coletarEstatisticas(JoinPoint joinPoint) {
File arquivo = (File) joinPoint.getArgs()[1];
obterEstatisticasArquivo(arquivo)
}
// restante da classe abaixo
}
Nocasodeum advicedotipo after throwing,éimportanteumanotaadicional:
casosejapassadoumparâmetroparaestequecorrespondaàexce çãodisparada,na
anotação @AfterThrowingquevemosaseguirdeveserincluídooatributoadici-
onal throwing,cujovalorcorrespondeaonomedoparâmetrodeclaradonométodo
queimplementao advice.
@Aspect
@Component
public class AdviceAroundProfiladorAnotacoes {
// os advices que vimos anteriormente estão acima
// para facilitar a leitura
// Advice do tipo after throwing
120


## Página 131

CasadoCódigo Capítulo5. AOP:adicionandonovoscomportamentosaosbeans
@AfterThrowing(
pointcut="execution(* casadocodigo.DAOPessoas.*(..))",
throwing="ex")
public void informar(IOException ex) {
enviarEmail(ex)
}
// restante da classe ignorado para facilitar leitura
}
5.13 C oncluindo com um resumão conceitual
VimoscomofuncionaomecanismodeAOPimplementadopeloSpring.Come ça-
moscomaformamaisprimitivaoferecidapelo frameworkqueéousodiretodesua
APIpara,logoemseguida,passarmosaousodosrecursosmaisprodutivosofereci-
dospelaferramenta.
Agrandedificuldadenaintrodu çãoàAOPconsisteemevitaroafogamentodo
leitornaquantidadesignificativadeconceitosqueacompanhaesteparadigmadede-
senvolvimento.Sendoassim,umbomresumodosprincipaisconceitosenvolvidos,
podemserelencadoscomo:
•Interesse transversal:éafuncionalidadequeencontramosemnosso
sistema,espalhadacomocódigorepetitivoequedificilmenteconseguiríamos
isolardemaneiraeleganteeconsistenteusandoaorienta çãoaobjetos;
•Aspecto: éaimplementaçãodointeressetransversal. Importantelembrar
queumaspectonãoexisteisolado,massemprenaformadeum advice;
•Advice: éaformaqueumaspectoéimplementado. Correspondeaomo-
mentoemqueesteserádisparado:énaexecu çãodométodo?Éantes,depois
ouapósdispararmosumaexce ção?
•Point cut:éaexpressãoqueidentificaquaismétodosdeverãoserintercep-
tados;
•Join point:éométodoquequeremosinterceptar.
Eagoravamosparaaparteprática,naqualveremoscomoaplicartodososcon-
ceitosquevimosnestaprimeirase çãodolivro!
121


## Página 133

Parte II
Spring Framework na prática
Atéocapítuloanterior,vimospraticamentetodaateorianecessáriaparaobom
entendimentodoSpringFramework.Apartirdeagoracolocaremosmaisnossa mão
na massa. Usaremoscomobaseumaaplica çãorealchamada Spring Forumescrita
especialmenteparaestelivro.Estaéumgerenciadordefórumbemparecidocomo
GUJ(http://www.guj.com.br),porémbemmaissimplificadoparaquenãoprejudi-
queadidáticadestelivro.


## Página 134

Figura5.5:PáginainicialdoSpringForum


## Página 135

Capítulo6
Colocandoamãonamassa
Nossomodelodedomínioserásimples,compostoinicialmenteporapenasquatro
classes: Usuario, Assunto, Topicoe Resposta.
Todoocódigofonteéaltamentecomentado,detalmodoquepossaserusado
comoreferênciapeloleitor. Noscapítulosposteriores,semprehaverãomen çõesa
estabaseparaqueoleitorpossafazerexperimenta çõesemseuambientededesen-
volvimentolocal.


## Página 136

6.1. Obtendoocódigofonte CasadoCódigo
Figura6.1:Modelodedomínioinicial
6.1 O btendo o código fonte
UsamosoGit(http://www.git-scm.com),queéumsistemadecontroledever-
sõesdistribuídobastantepopularatualmente. Comomuitosprojetos,nossocó-
digofonteencontra-sehospedadonoGitHub(http://www.github.com)noendere ço
http://www.github.com/loboweissmann/spring-forum.Háportantoduasmaneiras
deseobterocódigofonte. Aprimeiradelasconsisteembaixá-lonoformatozip
comopodeservistonaimagemabaixo:
126


## Página 137

CasadoCódigo Capítulo6. Colocandoamãonamassa
Figura6.2:OlinkparabaixarnossocódigofontenoGitHub
Asegundaop çãoaseradotadaporaquelesquepossuemogitinstaladoemseus
computadorespodemclonarorepositórioexecutandoocomandoabaixo:
git clone https://github.com/loboweissmann/spring-forum.git [diretório
aonde será clonado o repositório]
Casonãosejafornecidoonomedodiretórioaondeseráclonadoorepositório,
serágeradoumcomonomepadrão: spring-forum.
Como instalo o Git?
AinstalaçãodoGitpodeserdiferentedeacordocomosistemaope-
racionalquevocêutilizará. Recomendoquevocêassistaosscreencasts
gravadospelopessoaldaCaelum,disponíveisem: http://blog.caelum.
com.br/passo-a-passo-para-comecar-com-git-e-novo-curso-online/
6.2 C onfigure seu ambiente de desenvolvimento
OprojetoébaseadoemMaven(http://maven.apache.org),sendoassimoleitornão
precisasepreocuparembaixarmanualmentetodasasdependênciasusadas.Além
denãoprecisarmosnospreocuparcomestetrabalho,tambémganhamosapossibi-
lidadedeusarmosaIDEdenossapreferência,semcomplica çãonenhuma.
127


## Página 138

6.3. Oquevêmporai CasadoCódigo
Versão do Java
TodoocódigofontedesenvolvidofuncionaperfeitamentenoJava1.5ouposte-
rior.
Instalando o Maven
CasonãopossuaoMaveninstaladoemseucomputador,oprocedimentode
instalaçãodomesmoébastantesimpleseencontra-sesumarizadonopassoapasso
abaixo:
1) BaixeaúltimaversãodoMavenemhttp://maven.apache.org;
2) OMavenédistribuídoemarquivoscompactadosnoformato.zipou.tar.gz.
Descompacte-oemumdiretóriodesuapreferência;
3) Certifique-sedequeexistaumavariáveldeambientechamadaJAVA_HOMEem
seucomputadorqueaponteparaasuainstala çãodoJDK;
4) Adicioneodiretóriobin,presentenasuainstala çãodoMAVENaopathdoseu
sistema.
Qual IDE usar
AtualmentepraticamentetodasasIDEsJavaoferecemsuporteaoMaven.Sendo
assim,paraexecutarsuasexperimenta çõesemnossocódigofontebastaquevocê
abraoseuprojetoMavencasoestejausandoNetbeansouentãoimportá-loparao
seu workspaceseestivertrabalhandocomoEclipse.
Dadoofatodeexistiro SpringSource T ool SuitequeéumadistribuiçãodoEclipse
desenvolvidapelaSpringSource,especificamenteparaoSpringFrameworkeseus
subprojetos(incluindoGrails!),levaemconsidera çãoosrecursosnestapresentepara
lidarcomarquivosdeconfigura ção,anota ções,beanserefatora ções,portantoacre-
ditoquesejaatualmenteamelhorop çãoparaaquelesqueestãodandoosprimeiros
passosno framework.
6.3 O que vêm por ai
Nocapítulo8mostraremosoSpringMVC,quecomoopróprionomejádiz,éo
frameworkwebMVCqueacompanhaoSpring.Veremoscomofuncionaaorques-
128


## Página 139

CasadoCódigo Capítulo6. Colocandoamãonamassa
traçãoderequisi çõeserespostasecomointegrá-locomomotorde templatesApache
Tiles2.
ConhecendobemofuncionamentodoSpringMVC,podemoscome çaranos
aprofundarnacamadadenegóciosdonossoprojeto,conhecendoosrecursosque
oSpringnosoferecenocapítulo7,comoporexemploosuporteaHibernateeJPA,
configuraçãodefontesdedadosetudooqueprecisamosparaternossoORMfavo-
ritofuncionandoportrásdospanos.
Sabendocomopersistirnossasinforma ções,iremosaocapítulo10conhecerum
recursodoSpringqueatraidiversosdesenvolvedores: osuporteatransa çõesdo
Spring,assimdaremosocontroletransacionalparanossaaplica ção. Nocapítulo
11voltaremosaoSpringMVCexplicandooprojetoSpringSecurity,umframework
desegurançadesenvolvidopelaSpringSourcebastanteflexívelefácildeusar.
Preparado?Então,émãonamassaapartirdeagora!
129


## Página 141

Capítulo7
Acessoadados
Dificilmenteencontramosumaaplica çãoquenãopreciselidarcomalgumtipode
bancodedados.Apesardestetipodeintera çãofazerpartedocotidianododesenvol-
vedor,suaimplementaçãopossuiumasériededificuldadesinerentesdesuaprópria
natureza,queconsomemumaboapartedashorasdedesenvolvimentoemumpro-
jeto.OSpringofereceumricosuportenativoàstecnologiasdeacessoadadosmais
popularesatualmentecomoJDBC,HibernateeJPA.
Comoveremos,estesuporte,assimcomotudonoSpring,baseia-senaaplica ção
deboaspráticasepadrõesdeprojetodeeficáciacomprovada.Omaisinteressanteéo
fatodeque,apesardelidarmosnestecapítulodetecnologiasdistintascomoJDBCe
Hibernate,omododetrabalhoépraticamenteomesmo,facilitandoassimavidado
desenvolvedorcasopreciseexecutarumamigra çãotecnológicaemalgummomento.
Neste capítulo abordaremos as três tecnologias com suporte nativo do fra-
meworkmaispopularesnaescritadeaplica ções:JDBC,HibernateeJPAe,nodes-
creverdestas,serãoapresentadasassolu çõesoferecidaspeloSpringaosproblemas
quecostumamassombrarosdesenvolvedoresnaescritaemanuten çãodacamada


## Página 142

7.1. DAO:nocentrodamentalidadeSpring CasadoCódigo
depersistência.
7 .1 DAO: no centro da mentalidade Spring
AooptarmospeloSpringestamossempredeumaformaououtralidandocomo
problemadoaltoacoplamento.Noquedizrespeitoàescritadacamadadepersis-
tência,vemoscomoconceitocentraloDAO- Data Access Object -queabordamos
brevementenoprimeirocapítuloetrataremoscommaiorriquezadedetalhesagora.
Esteéumpadrãodeprojetocujoprincipalobjetivoéisolaromáximopossívelo
códigoresponsávelporinteragircomnossasbasesdedadosdorestantedosistema.
ODAOéumobjetoqueofereceàsclassesclientesumainterfaceabstrataaondesão
expostasasopera çõesbásicasquepossuemafinalidadedealteraroupesquisarabase
dedados.
Acamadadepersistênciadoprojeto Spring FórumadotaopadrãoDAOena
imagemaseguirpodemosverumexemplodecomoopadrãoseencontraimple-
mentado. DAOAssuntoéainterfaceabstratavisívelàsclassesclientesdosistema
responsávelporinteragircomtudoemnossosistemaquedigarespeitoaobjetosdo
tipo Assunto.Ànossaclassecliente HomeControllernãointeressasaberseusa-
mosJDBC,Hibernateoualgumabasededados NoSQL:tudooquelheinteressaé
quesejapossívellistartodososassuntospossíveisatravésdométodo list().
132


## Página 143

CasadoCódigo Capítulo7. Acessoadados
Figura7.1:PartedacamadadepersistênciadoSpringFórum
Oleitorjádeveterobservadoarepeti çãodeumpadrão:novamentevemosos
ganhosvindosdaaplica çãodainje çãodedependências/inversãodecontrole,que
permitemaodesenvolvedorprogramarvoltadoparainterfacesenãoparaimple-
mentações.
Guardebemestepadrão,poistodoosuporteoferecidopeloSpringàstecnolo-
giasdeacessoadadosbaseia-seneste.Masantesdemergulharmosnasfacilidades
oferecidaspeloSpringnaado çãodestaprática,vamosdescobrircomooSpringlida
comumproblemafundamentalatodoDAO.
7 .2 C onecte -se ao banco de dados
Todo DAO precisa de uma fonte de dados (data source). As três tecnologias
de acesso a dados abordadas neste capítulo têm como fonte de dados um ob-
jetoqueimplementeainterface javax.sql.DataSourcequeéresponsávelpela
obtençãodeobjetosdotipo java.sql.Connectionatravésdainvoca çãodo
getConnection. NocasodoSpring,tudooqueprecisamosfazerédeclararum
133


## Página 144

7.2. Conecte-seaobancodedados CasadoCódigo
bean.Aprincipaldecisãoasertomadapelodesenvolvedordizrespeitoaqualim-
plementaçãousar.
HátrêsformasdeobterumafontededadosnoSpring:usandoJNDI,criando
umafontededadosbaseadaemdriversouatravésdeumpooldeconexões.Napre-
paraçãodenossoambientefaz-senecessáriaainclusãodeumanovadependência.
Nocaso,estamosfalandodomódulodesuporteaJDBCdoSpring,cujadependência
noformatoMavenélistadaaseguir:
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-jdbc</artifactId>
<version>3.1.2.RELEASE</version>
</dependency>
JNDI
Talvezsejaaformamaisinteressantedeseobterumafontededados.Aosque
nãoconhecem,JNDI( Java Naming and Directory Interface)éumaAPIpresentena
plataformaJavaEEquepermiteaodesenvolvedorobterobjetosourecursosatravés
deumnome. Casosuaaplica çãosejaexecutadaemumservidordeaplica ções,é
grandeaprobabilidadedesteoferecersuporteàcria çãodefontesdedadosdisponi-
bilizadasàsaplica çõeshospedadasusandoestaAPI.
HáduasgrandesvantagensnoJNDI.Aprimeiravemdofatodesetratardeuma
configuraçãoexternaàaplica ção,oquepossibilitaaodesenvolvedoralterarseuspa-
râmetrossemanecessidadedequeestasejarecompiladaouinstaladanovamenteno
servidor.Dependendodosetupdoservidoredaaplica ção,muitasvezesodesenvol-
vedorsequerprecisareiniciarosistemaparaqueasaltera çõessurtamefeito.
Háduasformasdeseobterumdatasourcedestamaneira.Ocaminhomaisfácil
sedaatravésdonamespace jee,quepodeserdeclaradotalcomonotrechoaseguir:
<beans default-autowire="byType"
xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:jee="http://www.springframework.org/schema/jee"
xsi:schemaLocation="http://www.springframework.org/schema/jee
http://www.springframework.org/schema/jee/spring-jee-3.1.xsd">
<!-- Restante do arquivo oculto para facilitar a leitura -->
</beans>
134


## Página 145

CasadoCódigo Capítulo7. Acessoadados
Atagquenosinteressaé <jee:jndi-lookup/>,queobtémumrecursoqual-
querpeloJNDI.Seuusoémuitosimplescomopodeservistonocódigoaseguir:
<!-- Obtém uma fonte de dados identificada como 'dataSource -->
<jee:jndi-lookupid="dataSource"
id="dataSource"
jndi-name="/jdbc/SpringForumDS"/>
EstaéusadaparaobterqualquerrecursoJNDI.Seuúnicoatributoobrigatório
é jndi-name,queindicaonomedorecursoaserbuscado. Osegundoatributo,
resource-ref,quandonãofornecido,indicaqueonomedorecursoserábuscado
combaseapenasnovalordefinidoem jndi-name.
Outroatributointeressantenestatagé cache,cujovalordefaulté false.
Definindo-ocomo true,orecursoserácacheadoevitandoassimnovasconsultas
aodiretórioJNDI,oquepodepropiciarumganhodeperformanceàaplica ção.O
únicopontonegativodedefiniresteatributocomoverdadeiroéofatodequeassim
perdemosapossibilidadedealterarmosasconfigura çõesdenossasfontesdedados
semanecessidadedereiniciarmosaaplica ção.
ComoJNDInormalmenteéusadoemservidoresdeaplica ção,outroparâmetro
quedeveserlevadoemconsidera çãoé resource-refque,casoomitido,temseu
valorpadrãocomo true. Porconsequência,oidentificadorJNDIreceberásem-
preoprefixo java:comp/env/,valorpadrãousadoporservidoresdeaplica ção,
minimizandoassimaquantidadedeconfigura çãoaserdigitada.
Cadaservidordeaplica ções/servletpossuimodosdistintosdeconfigurarrecur-
sosJNDI,oquefugiriadoescopodestelivro. Ébomficaratentoàdocumenta ção
oficialdoambientequevocêestiverutilizando.
Fonte de dados baseada em driver
SeJNDIédiscutivelmenteamelhorop çãodefontededadosparaprodu ção,há
tambémapiorqueéabaseadaemdriver.PorpadrãooSpringvêmcomumaimple-
mentaçãochamada DriverManagerDataSource,queéamaissimplespossível,
quesemprecriaumanovaconexãocomobancodedadosquandonecessária.Não
érecomendávelparaserusadanoambientedeprodu çãoporserumfatoconhecido
queaobten çãodeconexõescomobancodedadoséumaatividadebastantecarado
pontodevistacomputacional.
Seéumaopçãotãoruimassim,porqueincluí-lanoSpring?Porqueéumasolu-
çãobastanteinteressanteparacasosmaissimples,comoaescritadetestesintegrados
135


## Página 146

7.2. Conecte-seaobancodedados CasadoCódigo
ouaplicaçõesmaissimplesnasquaisopre çoasepagarpelaobten çãodeumacone-
xãocomobancodedadoscompense.Adefini çãodestebeandentrodoarquivode
configuraçãoébastantesimples,comopodemosvernoexemplolistadoaseguir:
<bean id="dataSource"
class="org.springframework.jdbc.datasource.DriverManagerDataSource">
<property name="username" value="springbrasil"/>
<property name="password" value="springbrasil"/>
<property name="driverClassName" value="com.mysql.jdbc.Driver"/>
<property name="url"
value="jdbc:mysql://localhost:3306/springbrasil"/>
</bean>
O desenvolvedor precisa definir apenas quatro parâmetros:username e
passwordparaautenticar-seaoservidor, driverClassNamedefinindoodriver
responsávelpelaobtençãodeconexõescomobancodedadose,finalmente,aURL
deconexão,cujovalorirávariardeacordocomosistemagerenciadordebancode
dadosescolhido(nonossoexemplousamosoMySQL).
Háumaoutravariantedestaimplementa çãoqueobtémumaúnicaconexãocom
obancodedados.Éaindamenosrecomendadaque DriverManagerDataSource
pelofatodepodercausarproblemasemaplica çõesmulti-threaded.Suaconfigura ção
épraticamenteigualàdaversãoanterior,variando-seapenasonomedaclasseaser
instanciada:
<bean id="dataSource"
class=
"org.springframework.jdbc.datasource.SingleConnectionDataSource">
<property name="username" value="springbrasil"/>
<property name="password" value="springbrasil"/>
<property name="driverClassName" value="com.mysql.jdbc.Driver"/>
<property name="url"
value="jdbc:mysql://localhost:3306/springbrasil"/>
</bean>
Definindo um pool de conexões
Seaconfigura çãoviaJNDIestiverforademãoeoleitorouviumeuconselhode
nãousarumafontededadosbaseadaemdriver,umaop çãointermediáriaéadotar-
mosalgumaimplementa çãodepooldeconexões.Umpoolconsisteemumaestra-
tégiadeprogramaçãoquenospermiteobterganhossignificativosdeperformance,
minimizandonossanecessidadedeinstanciarobjetoscujaconstru çãosejacara.
136


## Página 147

CasadoCódigo Capítulo7. Acessoadados
Aestratégiaésimples:aoinvésdeacadarequisi çãocriarumnovoobjeto,criar
maisdeumainstânciadeumavez,liberando-asparaosobjetosclientesconforme
estassejamrequisitadas.Quandoainstâncianãoformaisnecessária,aclassecliente
adevolveparaopoolaondeseráreaproveitadaporoutraclassecliente,casoseja
requisitada.ParaaplataformaJava,hádiversasimplementa çõesdisponíveis,comoo
C3P0(http://www.mchange.com/projects/c3p0/),DBCP,usadopeloTomcat(http:
//commons.apache.org/dbcp/)emuitasoutras.
Estasimplementaçõespossuembasicamenteasmesmasconfigura ções.Apenas
parailustrar,seráexpostoaseguircomousaroC3P0.Oprimeiropassoéincluí-lo
noclasspathdoprojeto.Bastaadicionarsuadependêncianoarquivo pom.xmldo
projeto:
<dependency>
<groupId>c3p0</groupId>
<artifactId>c3p0</artifactId>
<version>0.9.1.2</version>
</dependency>
Finalmente,bastadeclararobeantalcomonocódigoaseguir.Suaconfigura ção
ébastantesimilaràqueprecisamosfornecerpara DriverManagerDataSource.
<bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource"
destroy-method="close">
<property name="driverClass" value="com.mysql.jdbc.Driver"/>
<property name="user" value="sf"/>
<property name="password" value="sf"/>
<property name="jdbcUrl"
value="jdbc:mysql://localhost:3306/spring_forum"/>
<property name="maxPoolSize" value="10"/>
<property name="acquireIncrement" value="1"/>
<property name="maxIdleTime" value="120"/>
<property name="acquireRetryAttempts" value="10"/>
<property name="initialPoolSize" value="10"/>
</bean>
Asprimeirasquatropropriedadesequivalemrespectivamenteàclassedodriver
donossobancodedados,dadosdeautentica çãosobaformadenomedousuárioe
senhae,finalmente,aURLdeconexão.Anovidadeestáporcontadascincopropri-
edadesseguintes,cujadescri çãodetalhadapodemosveraseguir:
137


## Página 148

7.3. DevoltaaoDAO:oproblemacomasexce ções CasadoCódigo
•maxPoolSize:defineonúmeromáximodeconexõesaserarmazenadono
pool.
•acquireIncrement:acadarequisi çãoporumaconexão,definequantasno-
vasconexõesdevemserincluídasnopoolcasoestenãopossuamaisconexões
disponíveisatéatingironúmeromáximodefinidoem maxPoolSize.
•maxIdleTime:defineotempomáximoemsegundosqueumaconexãonão
usadadeveserarmazenadanopool.
•acquireRetryAttempts:defineonúmeroderetentativasnaobten çãode
umanovaconexãoporpartedopool.
•initialPoolSize:defineonúmeroinicialdeconexõesquedevemexistir
quandoaprimeiraconexãoforsolicitadaporalgumaclassecliente.
Atençãoespecialdeveserdadaaoatributo destroy-method,incluídonadefi-
niçãodobean.Ométodo closefecharátodasasconexõesabertaspelopoolquando
seubeanforfinalizadopelocontainer.
7 .3 D e volta ao DAO: o problema com as exceções
Aexceção SQLExceptionemumprimeiromomentopareceumasolu çãobastante
eleganteadotadapelaequipededesenvolvimentodoJDBC.Infelizmentetodaesta
elegânciacaidosaltoapartirdomomentoemquepensamosnassitua çõesemque
estaexceçãoédisparada:
• Quandonãoconseguimosobterumaconexãocomobancodedados;
• ComandoSQLmalformado;
• Falhadeconexãocomoservidor;
• Violaçãodeintegridade;
• Problemasnaliberaçãoderecursos;
• Deadlocks;
• Equalqueroutroproblemadecorrentedoacessoadados.
138


## Página 149

CasadoCódigo Capítulo7. Acessoadados
Comopodeservisto,éumaexce çãoaplicávelaqualquersitua çãoquefujada
execuçãonormaldenossoprograma.Sequisermosdaralgumtratamentoespecial,
temosdelidarcomcódigosdeerroespecíficosdodesenvolvedordodriver/bancode
dados,talcomonoexemploaseguir:
try {
//faço algo que pode disparar uma SQLException
} catch (SQLException ex) {
switch (ex.getErrorCode()) {
case 1022:
// chave duplicada no MySQL
break;
case 1037:
// falta de memória no MySQL
break;
}
}
Derepente SQLExceptionsemostroumancatambém,poisalémdeserexces-
sivamentegenérica,aindanosobrigaaescrevercódigovoltadoparaumfornecedor
específico,jogandonolixotodaaquelahistóriadeportabilidadeusadaparavender
oJava.
Asitua çãomelhoraumpoucocomoHibernate,quepossuiumahierarquia
de exceções bem mais rica e nos possibilita tratar erros com maior granulari-
dade. Há exceções como QueryException, OptimisticLockException,
ObjectNotFoundExceptionemuitasoutras.
Emumprimeiromomentotemosaimpressãodequenossoproblemafoiresol-
vido,principalmenteporquenãosãoexce çõeschecadase,portanto,nãoprecisam
serincluídasnasdeclara çõesdemétodosdasnossasinterfaces.Masesenofuturo
precisarmosporalgumarazãovoltarmosparaoJDBCemumpontoououtroda
aplicação? Nossasclassesclientejáestarãoinfectadascomreferênciasaclasseses-
pecíficasdoHibernate.Piorainda:eseestivermosimplementandoumcomponente
reaproveitável?
Seriaótimosehouvesseumahierarquiadeexce çõesquefosseagnósticaemrela-
çãoaomecanismodepersistência,nãoémesmo?Algoqueváalémdadeselegância
denossaamiga SQLExceptionmasquetambémnãonosamarrasseaalgumORM
específicocomoHibernate.EstahierarquiaexisteeéfornecidapeloSpring.
Nodiagramaabaixopodemosverquãoabrangenteegenéricaestaé,abordando
osprincipaisproblemasenfrentadospelosdesenvolvedores.Esabeoquemais?To-
139


## Página 150

7.4. Templates:acabecomocódigorepetido CasadoCódigo
dastemcomobase DataAccessException,quenãoéchecadaeportantonão
precisaserincluídanadeclara ção throwsdenossainterface.
Figura7.2:Hierarquiadeexce çõesdeacessoadadosdoSpring
InternamenteoSpringpossuiummecanismodetradu çãodeexce ções:háum
paracadatecnologiasuportadapeloSpring.Sendoassim,encontramosclassescomo
SQLExceptionTranslator, HibernateExceptionTranslatoreumasérie
de [sua tecnologia de acesso favorita]ExceptionTranslatorsàdisposiçãododesenvol-
vedor.Omaisinteressanteéquenãoprecisamoslidarcomestasclassesdiretamente:
bastausarmosostemplatesfornecidospeloSpring.
7 .4 T emplates : acabe com o código repetido
Járeparouqueemdiversassitua çõesrepetimossempreomesmoscript?Tomeuma
atualizaçãodedadosouconsultaJDBCporexemplo.Temosumalgoritmoquesem-
presegueamesmasequenciadepassos:
1) Obtenhaumaconexão;
2) Inicieumatransação;
140


## Página 151

CasadoCódigo Capítulo7. Acessoadados
3) Executeumaconsultaouatualiza çãodedados;
4) Comiteatransaçãoouexecuteorollbackcasoalgodêerrado;
5) Libererecursosfechandoaconexão.
Sempreprecisamosexecutarnaordemacimaosdoisprimeiroseúltimospassos
doalgoritmo.Umtemplateéumpadrãodeprojetoquesepopularizoucomolivro
Padrões de Projeto[4].Seuobjetivoédelegarparaumasubclasseumcallbackaparte
doalgoritmocujaexecu çãosejacustomizada,mantendoassimintactosospassosdo
algoritmoquenormalmentenãosofremmodifica ções.
Figura7.3:Exemplodetemplate
Templatesdesempenhamumpapelfundamentaldentrodosuporteadadosofe-
recidopeloSpring.Cadatecnologiasuportadapeloframeworkpossuiseupróprio
template,responsávelporencapsularospassosimutáveisdoalgoritmo,executarem
atransformaçãodasexce çõesdisparadasereduziraquantidadedecódigoqueo
desenvolvedorprecisaescrever.
Nossacompreensãodestepadrãosetornarámaisclaranaprática,sendoassim
convémtratarmosdaAPIbásicadepersistênciaqueoSpringsuporta.
141


## Página 152

7.5. OtrabalhocomJDBC CasadoCódigo
7 .5 O trabalho com JDBC
TalvezoJDBCsejaomecanismodepersistênciaquemaisrecebamelhoriasapartir
doSpring. TalveznãosejaexagerodizerqueoframeworkrevitalizaestaAPIcom
seustemplateseclassesdesuportedetalformaqueodesenvolvedorpossasentirno
futuroumfortemalestaraousá-lasemoSpring.Comferramentasdemapeamento
tãoavan çadascomoHibernate,ToplinkouJPAmuitossequestionamserealmente
valeàpenausarmosJDBCdiretamenteparamanipularmosnossasbasesdedados
relacionais.Averdadeéquehádiversoscasosnosquaisestaéamelhorop ção:
• AequipenãoprecisaaprenderoutraAPIdeacesso,apenasJDBC.
• Vocêprecisateracessorápidoafuncionalidadesespecíficasdoseugerenciador
debancodedados.
• Énecessáriotunarasconsultasouinstruçõesdemanipula çãocomgranulari-
dademáximaemseuprojeto.
• Performance:apesardosORMsjáotimizaremasconsultasfeitasaobancode
dados,sempreháumcasoououtroqueaferramentanãoconseguealcan çar.
EnestescasosJDBCcaicomoumaluva.
• VocêsimplesmenteprefereJDBC.
QuandolidamoscomJDBCficaclaraaquantidadedecódigoduplicadoquepre-
cisamosescrever.Comoexemplo,vejaocódigoabaixoresponsávelporlistartodos
osassuntosdoprojeto Spring Fórumusandoaabordagemtradicional:
class JdbcAssunto implements DAOAssunto {
public List<Assunto> listJDBC(int offset, int max) {
List<Assunto> resultado = new ArrayList<Assunto>();
Connection conexao = null;
try {
conexao = getDataSource().getConnection();
PreparedStatement stmt =
conexao.prepareStatement
("select id, nome from assunto limit ? offset ?");
stmt.setInt(1, max);
stmt.setInt(2, offset);
ResultSet rs = stmt.executeQuery();
while (rs.next()) {
142


## Página 153

CasadoCódigo Capítulo7. Acessoadados
resultado.add(
new Assunto(rs.getLong(1), rs.getString(2)));
}
} catch (SQLException ex) {
// tratamento
} finally {
if (conexao != null) {
try {
conexao.close();
} catch (SQLException ex) {
// trate o erro
}
}
}
return resultado;
}
}
Eocódigousadoparapersistirumassuntonãoémuitodiferente,conforme
podemosveraseguir:
public void persistirJDBC(Assunto assunto) {
Connection conexao = null;
try {
conexao = getConnection();
conexao.setAutoCommit(false);
PreparedStatement stmt =
conexao.prepareStatement("insert into assunto (nome) values (?)");
stmt.setString(1, assunto.getNome());
stmt.executeUpdate();
conexao.commit();
} catch (SQLException ex) {
try {
conexao.rollback();
} catch (SQLException ex2) {
// não deu pra fazer rollback
}
} finally {
if (conexao != null) {
try {
conexao.close();
} catch (SQLException ex2) {
143


## Página 154

7.5. OtrabalhocomJDBC CasadoCódigo
// não consegui liberar o recurso
}
}
}
}
Vemosnitidamentequeháumcódigoreplicadoque“emoldura”oquerealmente
interessaemcadamétodoequeocupaamaiorpartedocódigoqueprecisamoses-
crever.EntramemcenaostemplatesoferecidospeloSpringquefacilitamnossavida.
T emplates JDBC
NodesenvolverdoSpring,trêstiposdetemplatesurgiramparadarsuporteao
JDBC.Nocentroencontra-se JdbcTemplate,queoferecetodasasfuncionalida-
desbásicasoferecidaspeloframework. NamedParameterJdbcTemplateque
nosoferecefacilidadesaolidarcomconsultasquepossuamparâmetrosnomeados
e SimpleJdbcTemplate,queporalgumtempofoivistocomoocaminhoaser
seguidopelosdesenvolvedores.
Ahistóriaportrásdo SimpleJdbcTemplateécuriosa.Estaclasseaparecena
versão2.0doSpringcomoumaconveniênciaquebasicamenteencapsulaumobjeto
dotipo JdbcTemplateeprovêumaAPImaissimplesdeserusadaporserbaseada
nanovasintaxeoferecidapeloJava5. Agrossomodo,chamadasaestaAPIeram
transformadasinternamenteerepassadasàinstância JdbcTemplateparaserem
processadas.
Atéaversão3.0doSpringeravistacomo aimplementaçãoquedeveriaserado-
tadapelosdesenvolvedores,vistoqueversõesanterioresaoJava5nãoseriammais
suportadaspeloSpringnofuturoetambémporpossuirsuporteaparâmetrosnome-
ados.Naterceiraedi çãodolivro Spring em Ação[16]oautorchegaadizerqueasduas
outrasopçõessequerprecisamserusadas,pelofatode SimpleJdbcTemplateofe-
recertodososseusrecursos.Todoesteprestígioacabacomaversão3.1doSpring,
quepassaaconsiderá-loumaclassedepreciada.Como?
Istomesmo: olhandocommaioraten çãoàclasse JdbcTemplate,osdesen-
volvedoresportrásdoSpringperceberamque,pelofatodestajápossuirsuporteao
Java5eestarnocentrodosuporteaoJDBC,nãohárazãoemsemantertrêstiposde
template.
144


## Página 155

CasadoCódigo Capítulo7. Acessoadados
O uso do JdbcT emplate
Com JdbcTemplate,oprogramadornãoprecisasepreocuparcomobten çãoe
liberaçãoderecursos,poisestesjásãoimplementadospelotemplate.Precisamosnos
preocuparsomentecomoquerealmenteimporta,queéimplementa çãodenossos
comandosSQLeextra çãodosresultados.Alémdisto,estaclassetambémpossuia
funçãodetransformarexce çõesespecíficasdoJDBCparaahierarquiaoferecidapelo
Springquevimosnoiníciodestecapítulo.
Umavantagemde JdbcTemplateéofatodestaclasseser thread safeapóscon-
figurada,oquenospossibilitaterumaúnicainstânciadestacompartilhadaportodos
osnossosbeansqueprecisemdeseusservi ços.Hácasosemqueumanovainstância
sóécriadacasosejanecessáriolidarcomfontesdedadosdistintas.
Porfalareminstancia ção,asuaébastantesimples: bastausarseuconstrutor
querecebacomoparâmetroumobjetodotipo javax.sql.DataSourceouentão
simplesmenteinjetarumafontededadosporsetter. Podemosvernoexemploa
seguircomodeclará-laemumarquivodeconfigura çãoXML:
<!-- por setter -->
<bean id="jdbcTemplatePorSetter"
class="org.springframework.jdbc.core.JdbcTemplate">
<property name="dataSource" ref="dataSource"/>
</bean>
<!-- por construtor -->
<bean id="jdbcPorConstrutor"
class="org.springframework.jdbc.core.JdbcTemplate">
<constructor-arg ref="dataSource"/>
</bean>
<!-- ou por auto wiring -->
<bean id="jdbcAutoWired"
class="org.springframework.jdbc.core.JdbcTemplate"
autowire="byType"/>
Normalmente, JdbcTemplateéinjetadoemnossos DAOsqueousamcomo
baseparatodasassuasopera ções. Surgiuinclusiveumpadrãoparaestetipode
classe.Nestepadrão,queaindanãopossuiumnome,umanovainstânciadotem-
plateégeradanomomentoemqueinjetamosumobjetodotipo DataSource.
Podemosverumexemplodeimplementa çãodestepadrãonocódigoaseguir:
public abstract class BaseJdbcDAO {
private JdbcTemplate jdbcTemplate;
145


## Página 156

7.5. OtrabalhocomJDBC CasadoCódigo
@Autowired
public void setDataSource(DataSource ds) {
/*
Não precisamos de uma instância real do DataSource
se todas as nossas operações serão feitas usando o
JDBCTemplate, certo?
*/
jdbcTemplate = new JdbcTemplate(ds);
}
}
Este padrão é tão comum que no Spring já vêm uma implementa-
ção bastante similar ao exemplo exposto anteriormente. Trata-se da classe
org.springframework.jdbc.core.support.JdbcDaoSupport. Nãoéne-
cessárioimplementarocódigodescritoacimaparaencapsularseu JdbcTemplate,
bastaquesuasclassesestendam JdbcDaoSupport.
Consultando com JdbcT emplate
Como mencionado, ao lidarmos com os templates do Spring, só precisa-
mosnospreocuparcomadefini çãodenossasconsultasenaextra çãodedados.
JdbcTemplatenosofereceumasériedemétodosincrivelmenteúteisquandopre-
cisamosbuscarapenasumcampodenossasconsultas. Abaixopodemosverum
exemploextraídodo Spring Fórumquepodechocaroleitoracostumadoaomodo
detrabalhotradicionalJDBC:
public class JdbcAssunto extends JdbcDaoSupport {
public int getTotalAssuntos() {
return getJdbcTemplate()
.queryForInt("select count(*) from assunto");
}
}
Umalinhadecódigo!Oganhodeprodutividadesemostramaisevidentequando
comparamosoexemploacimacomumaimplementa çãomaistradicionalcomoa
seguiremquefoinecessárioescrevernomínimo17:
public int getTotalAssuntosJDBC() {
Connection conexao = null;
ResultSet rs = null;
146


## Página 157

CasadoCódigo Capítulo7. Acessoadados
try {
conexao = .getConnection();
rs = conexao.createStatement()
.executeQuery("select count(*) from assunto");
rs.next();
return rs.getInt(1);
} catch (SQLException ex) {
// trato o erro de alguma forma
} finally {
try {
if (rs != null) rs.close();
if (conexao != null) conexao.close();
} catch (SQLException ex) {
// trata o erro
}
}
}
Paraconsultasnasquaispretendemosobterapenasumcampo JdbcTemplate,
odesenvolvedornãoprecisasepreocuparcomaextra çãodosdados,vistoqueo
própriotemplatejáexecutaestetrabalhoparanós. Háumasériedefun çõespara
estefimimplementadasem JdbcTemplate,cujasmaispopularespodemosver
nalistaaseguir,quesemprepossuemduasassinaturas:umaquecontémapenasa
consulta,eoutraquecontém,alémdaconsulta,umalistanoformato varargsdoJava
5.Dentreestasdestacam-se queryForInt, queryForLong, queryForString,
queryForObjecteoutras,cujotiporetornadojáseencontradescritonopróprio
nomedafun ção.
Buscarumúnicovalorpassandoparâmetrosétambémigualmentesimples,tal
comopodeservistonoexemploaseguir:
public long getIdUsuario(String login, String nome) {
getJdbcTemplate()
.queryForLong("select id from usuario where login = ? and nome = ?",
login, nome);
}
Napráticasabemosqueosdoisexemplosacimasãocasosraros.Émuitomais
comumprecisamosquenossasconsultasnosretornementidadestotalmentepreen-
chidas(daíapopularidadedasferramentasORM).Esteprocessodeobterosdadosa
147


## Página 158

7.5. OtrabalhocomJDBC CasadoCódigo
partirdaconsultaeemseguidatransformá-losemobjetoscomplexoséoquechama-
mosdeextra ção.Parailustraroprocessoiremosmaisumavezrecorreraoprojeto
Spring Fórum. Ocódigoaseguirretornaumalistacomosassuntospresentesno
bancodedadosusandopagina ção:
public List<Assunto> list(int offset, int max) {
Integer[] parametros = {max, offset};
return getJdbcTemplate().query(
"select id, nome from assunto limit ? offset ?",
parametros,
new RowMapper<Assunto>(){
public Assunto mapRow(ResultSet rs, int rowNum) throws SQLException {
Assunto assunto = new Assunto();
assunto.setId(rs.getLong(1));
assunto.setNome(rs.getString(2));
return assunto;
}});
}
Afunção queryde JdbcTemplaterecebetrêsvalores:nossaconsulta,alista
deparâmetrosquepassaremosànossaconsultasobaformadeumamatrizdeobje-
toseumaimplementa çãode org.springframework.jdbc.core.RowMapper,
queéainterfacedecallbackresponsávelporleroscamposdecadaregistroobtido
pornossaconsultaeretornarumobjetobaseadonestesvalores.
Observeque RowMapperusa generics.Comistoconseguimosescrevercódigo
bemlimpo,comooexposto.Precisamosimplementarumúnicométodo, mapRow,
quepossuiporobjetivomapearoscampospresentesnoregistrocorrentedenossa
consultaparaoobjetodenossaescolha. Estemétodorecebedoisparâmetros:um
objetodotipo java.sql.ResultSeteoutrodotipointeiro,usadopararepre-
sentaraposi çãodoregistrodentrodoresultadoobtido.
Importante: quemiterasobreosregistroséaclasse JdbcTemplate,enão
nossaimplementaçãode RowMapper,sendoassim,emhipótesealgumaodesen-
volvedordeveinvocarométodo next()doobjeto ResultSetdentrodestaclasse.
Esteéumerrocomumquepodeocasionarconsequênciasimprevisíveisdeacordo
comodriverdobancodedadosusadoemsuaaplica ção.
148


## Página 159

CasadoCódigo Capítulo7. Acessoadados
Atualizando a base de dados
Asmesmasfacilidadesquevimosparaaobten çãodedados,tambémseaplica
àsuaatualiza ção.Separaaobten çãoderegistroso JdbcTemplatenosoferecea
função query,afun çãobásicaqueusaremosagoraé update.Seufuncionamento
épraticamenteidênticoaoquejávimosanteriormente,oquepodeserconfirmado
nocódigoaseguirqueatualizaosdadosdaentidade Assuntopassadacomoparâ-
metro:
public void update(Assunto assunto) {
getJdbcTemplate().update("update assunto set nome = ? where id = ?",
assunto.getNome(), assunto.getId());
}
Vemosexatamenteamesmaassinaturadométodo query:umastringrepresen-
tandoocomandoaserexecutadocontraobancodedadoseosparâmetrospassados
emordemusandoasintaxe varargsdoJava5.Naversãoanteriordo JdbcTemplate
emqueosuporteànovasintaxedalinguagemJavanãoestavapresente,seriapassada
umamatrizdeobjetostalcomonoexemploaseguir:
public void update(Assunto assunto) {
Object[] parametros = {assunto.getNome(), assunto.getId()};
getJdbcTemplate()
.update("update assunto set nome = ? where id = ?", parametros);
}
ExecutarcomandosDDL( Data Definition Language)contraabasededadosse-
gueamesmalinha. Adiferen çaéqueusamosafun ção execute,quevemosem
práticanoexemploaseguir:
String ddl = "create table assunto(" +
"id long auto_increment not null, " +
"nome varchar(255) not null, " +
"primary key(id))";
getJdbcTemplate().execute(ddl);
Ointeressantedessemétodoéqueelepodeserusadoparaexecutarqualquer
tipodeinstru çãoSQL,porexemplo,paraexecutarregistrosdeatualiza çãodebanco
dedadosemseusprojetos,talcomonoexemploaseguir:
public void atualizarBD(File arquivo) {
/*
149


## Página 160

7.5. OtrabalhocomJDBC CasadoCódigo
Obtém um java.io.BufferedReader a partir do arquivo
Código omitido para facilitar a leitura do exemplo
*/
BufferedReader reader = obterBufferedReader(arquivo);
String comando = null;
while ((comando = reader.readLine()) != null) {
getJdbcTemplate().execute(comando);
}
// Restante omitido
}
Inserção facilitada: obtenha os valores gerados de forma automática
Naversão2.5doSpringumanovaclassefoiadicionadaaoarsenalJDBCdo
framework. Apesardepoucodivulgadaeusada,éumaferramentamuitointeres-
santequandoenfrentamosproblemasaolidarcomainser çãoderegistros. Estou
falandode SimpleJdbcInsert,umaclassequebasicamenteéuminvólucropara
o JdbcTemplate.
Apesardeparecersimplesainser çãoderegistroséumatarefaquecarregaalguns
desafios.Tomeporexemploaobten çãodovalordeumcampogeradoautomatica-
mentecomonocasodechavesprimárias,queseráoqueveremosnestase ção.Assim
como JdbcTemplate, SimpleJdbcInserttambéméthreadsafeumavezque
tenhasidoconfigurado,porémsuaconstru çãoémaisinteressante,poisbaseia-seno
padrão builder.Nocódigoaseguirpodemosverumexemplodeseuuso.
public void inserir(Assunto assunto) {
HashMap<String, Object> parametros = new HashMap<String, Object>();
parametros.put("nome", assunto.getNome());
long id = new SimpleJdbcInsert(getDataSource())
.withTableName("assunto")
.usingGeneratedKeyColumns("id")
.executeAndReturnKey(parametros).longValue();
assunto.setId(id);
}
Oexemploinsereumnovoregistronatabela assuntoe,logoemseguida,re-
tornaovalordachaveprimáriadatabela,nocaso,umcampoautoincremental.A
primeirapartedocódigocriaummapaaondeseencontrarãopresentesosvalores
detodososcamposquepretendemosinseriremnossatabela,levandocomochave
onomedocampoaserpreenchido.
150


## Página 161

CasadoCódigo Capítulo7. Acessoadados
Anovidadeestánomodocomoinstanciamosnosso SimpleJdbcInsert.
Seuconstrutorpoderecebercomovalortantoumobjetodotipo JdbcTemplate
quantoum DataSource.Casosejaosegundocaso,serácriadointernamenteum
novoobjeto JdbcTemplateencapsulado. Emseguidasãoinvocadasasfun ções
withTableName,usadaparadefinironomedatabelanaqualseráfeitaainclusãoe
usingGeneratedKeyColumns,queiráinstruir SimpleJdbcInsertarespeito
dequaiscamposautogeradosdevemsermonitorados.
Finalmente,afun ção executeAndReturnKey,querecebecomoparâmetroo
mapacriadoanteriormenteiráexecutarainser çãonatabelaeretornarácomoresul-
tadoumobjetodotipo java.lang.Numberrepresentandoovalorgeradoparao
campo iddefinidopelométodo usingGeneratedKeyColumns.
Processamento em lote
Comomencionado,umadaspossíveisrazõespelasquaisosdesenvolvedoresop-
tampeloJDBCéperformance.Umdosmaioresvilõesnestaáreaéotráfegonarede.
SeformosexecutarNinser çõesouedi çõesemnossabasededadosemsérieecada
umarequererumaconexãoremota,comcertezapagaremosumaltopre çonestere-
quisito. Paraminimizaresteproblemadiversosfornecedoresdebancosdedados
incluemseusdriversJDBCapossibilidadedeprocessamentoemlote.
Porprocessamentoemloteentendaapossibilidadedeenviargruposdeco-
mandosSQLemumaúnicatransmissãoaobancodedados. Comistootráfego
pela rede diminuirá significativamente e nossa performance sofrerá melhorias
expressivas.Novamenteaquio Springsalvanossapelecomainterfacedecallback
org.springframework.jdbc.core.BatchPreparedStatementSetter.
Parailustrarseuuso,vamosexporaimplementa çãodeumaclassequeimporta
definições de usuários armazenadas em arquivo para o nosso banco de dados
conformeveremosaseguir:
public void importarUsuarios(File arquivo) {
// Obtém uma lista de usuários a partir do arquivo de entrada
final List<Usuario> usuarios = obterUsuarios(arquivo);
// Nosso BatchPreparedStatementSetter
BatchPreparedStatementSetter batch =
new BatchPreparedStatementSetter() {
public void setValues(PreparedStatement ps, int i) {
Usuario usr = usuarios.get(i);
151


## Página 162

7.6. OtrabalhocomoHibernate CasadoCódigo
ps.setString(1, usr.getNome());
ps.setString(2, usr.getLogin());
ps.setString(3, usr.getSenha());
}
public int getBatchSize() {
return usuarios.size();
}
}
// Executa o processamento em lote
jdbcTemplate.
batchUpdate(
"insert into usuario (nome, login, senha) values (?,?,?)",
batch);
}
Afunção getBatchSizeretornaumvalorinteirorepresentandootamanho
dolote. Emnossocaso,estaretornacomovaloronúmerodeinstânciasdaclasse
Usuarioqueafun ção obterUsuariosrecebeu.Atençãoespecialdeveserdada
aométodo setValuesquerecebedoisparâmetrosdeentrada:umobjetodotipo
java.sql.PreparedStatementeuminteiroindicandoaposi çãodocomando
dentrodolote.
Oprogramadordeveráapenasdefinirosvaloresdosparâmetrosdentrodacon-
sultaemaisnada.Lembre-sequeoresponsávelporexecutarolotedeopera çõesnão
éo BatchPreparedStatementSetter-reparenonomedaclasse-massimo
nosso JdbcTemplate.
7 .6 O trabalho com o Hibernate
ComoJDBCéabasedetodaainfraestrutura,nadamaisnaturalquesejatambém
aopçãomaisprimitiva,oquejustificaofatodamaiorpartedestecapítulotersido
voltadaaestatecnologia.QuandolidamoscomumORM,estamosencarandouma
criaturabemmaisevoluída:nocasodoHibernate,porexemplo,praticamentetodas
asfacilidadesreferentesamanipula çãoepesquisadedadosseencontrampresentes
nainterface org.hibernate.Session.
CasooleitorjátenhatrabalhadocomoHibernate,jáestáfamiliarizadocomo
SessionFactory,queéoobjetoresponsávelporcriar,abrirefecharsessões. E
152


## Página 163

CasadoCódigo Capítulo7. Acessoadados
comas sessões contextuais,estaentidadeconsegueliberarodesenvolvedordaneces-
sidadedeimplementarcódigoresponsávelpelaobten çãoefechamentodesessões.
Nestepontoéimportantelembrarmosdastrêsprincipaisresponsabilidadesdos
templatesdeacessoadadosdoSpring:
• Facilitaraimplementaçãodeconsultaseatualiza çõesdabasededados;
• Gerenciarrecursosdeformatransparenteaoprogramador.Porrecurso,en-
tendaaunidadebásicaresponsávelpelapersistência.NocasodoJDBC,esta-
mosfalandodeconexões,paraoHibernate,sessões;
• Transformar exceções específicas de uma tecnologia para a hierarquia do
Spring.
Levandoemconsidera çãoquedastrêsresponsabilidadesdeumtemplatede
acessoadadosdoSpring,asduasprimeirasjáforamresolvidaspelopróprioHi-
bernateemsuaevolu ção,aexistênciadeumtemplateespecíficoparaestatecnologia
sóserviriaparaatenderaterceiranecessidade.
Coloque-senolugardeumdosresponsáveispelaevolu çãodoSpring:háumga-
nhorealemmanterumtemplateespecíficoparaoHibernatesóparalidarcomexce-
çõesespecíficasdeplataforma?Não.Seráquenãoestaríamospoluindoocódigodos
desenvolvedoresqueusamnossoframeworksóparasuprirestanecessidade?Sim.
Valeriaàpena?Não.Háalgumasolu çãoalternativaparaoproblemadasexce ções?
Sim!
153


## Página 164

7.6. OtrabalhocomoHibernate CasadoCódigo
Existe um HibernateTemplate!
Nem sempre o Hibernate ofereceu o recurso de sessões contex-
tuais. Nesta época a forma mais popular de lidar com o Spring
era através da classeHibernateTemplate, disponível no pacote
org.springframework.orm.hibernate3, que funcionava exata-
mentecomo JdbcTemplatequevimosnaprimeirapartedestecapí-
tulo.
Já no pacoteorg.springframework.orm.hibernate4 esta
classenãoexiste,etentarusar HibernateTemplatecomaversão4
doHibernateéaltamentenãorecomendado,poisestasimplesmentenão
funcionarácomoesperado.Sendoassim,omelhorcaminhoaseseguir
ésimplesmenteignorarestaclasse,queaindaédistribuídajuntocomo
Springapenasparafinsderetrocompatibilidade.
Preparando o ambiente
ParaativarosuporteaoHibernateprecisamosadicionarumanovadependência
aonossoprojeto.Trata-sedopacote spring-orm,quenosfornecerásuporteaos
principaisORMsdomercadosuportadospeloSpring:Hibernate(3,e4),iBatis,JDO
eJPA.Abaixoseguecomoestadependênciadeveserincluídanoarquivo pom.xml.
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-orm</artifactId>
<version>3.1.2.RELEASE</version>
</dependency>
Como lidar com exceções
Comomencionado,nãoprecisamosdetemplatesparalidarmoscomastrans-
formaçõesdeexce çõesespecíficasdeplataformaparaasdahierarquiauniforme
do Spring. A solução é bastante simples: basta anotarmos nosso DAO com
@Repositoryaoinvésde @Componentcomofizemosatéentão.Estaéumasolu-
çãointeressantequepodeseraplicadaaqualquerDAO,inclusiveJDBC.Estaano-
taçãoéumestereótipoquepermiteaocontainerdoSpringaplicarfuncionalidades
maisinteressantesaDAOs,poisosdiferenciadosdemaisbeansdefinidosemseu
154


## Página 165

CasadoCódigo Capítulo7. Acessoadados
contexto.
Aseguirpodemosverumexemplodeaplica çãodestaanota ção,nocaso,naver-
são Hibernatedonosso DAOAssunto.
import org.springframework.stereotype.Repository;
@Repository
public class HibernateAssunto {
// conteúdo omitido
}
Apenas a presen ça da anota ção não é suficiente: faz-se ne-
cessário também incluir a definição de um novo bean do tipo
PersistenceExceptionTranslationPostProcessor. O que este bean
fazécriarumaspectodotipo after throw paratodososbeansanotadoscom
@Repository. Aexceçãoseráinterceptadaeautomaticamenteconvertidapara
outrapresentenahierarquiadeexce çõesuniformizadadoSpring.Abaixopodemos
vercomoadeclara çãodestebean-quesequerprecisadeumnome-étrivialem
XML:
<bean class="org.springframework.dao.annotation.
PersistenceExceptionTranslationPostProcessor"/>
Ecomistoostemplatessetornamcompletamentedesnecessáriosnãosóparao
HibernatemastambémparaqualqueroutroORMquesejanativamentesuportado
peloSpring.
O trabalho com a SessionFactory
Assim como o primeiro passo ao lidarmos com JDBC é a configu-
ração da fonte de dados, nosso segundo passo ao configurarmos o Hi-
bernate é a definição da nossa implementação da SessionFactory.
Há dois pacotes que devem ser levados em considera ção no su-
porte ao Hibernate: org.springframework.orm.hibernate3 e
org.springframework.orm.hibernate4, que contém respectivamente
asclassesdesuporteàsversões3e4doORM.
Qualimplementaçãode SessionFactoryescolherdependededuascondi-
ções:aversãodoHibernateusadaemseuprojetoequalaop çãodemapeamento
adotada:XMLouanota ções.
155


## Página 166

7.6. OtrabalhocomoHibernate CasadoCódigo
NocasodeestarmoslidandocomHibernate3,temosduasimplementa çõesaes-
colher: LocalSessionFactoryBean,casotenhamosoptadoporconfigura ções
noformatoXMLou AnnotationSessionFactoryBean,implementadanopa-
cote org.springframework.orm.hibernate3.annotationparaanotações.
Começaremoscom LocalSessionFactoryBean,poissuaconfigura çãobá-
sicaserámuitosimilaràde AnnotationSessionFactoryBean. Podemosver
abaixoumexemplodesuadeclara ção:
<bean
class="org.springframework.orm.hibernate3.LocalSessionFactoryBean">
<property name="dataSource" ref="dataSource"/>
<property name="hibernateProperties">
<props>
<prop key="hibernate.dialect">
org.hibernate.dialect.MySQL5InnoDBDialect
</prop>
<prop key="hibernate.hbm2ddl.auto">update</prop>
</props>
</property>
</bean>
Otrechoexpostoécomumatodasasimplementa çõesde SessionFactory.
Duas são as propriedades que sempre devem ser preenchidas:dataSource,
apontandoparaafontededadosaserusadae hibernateProperties, con-
tendotodasaschavesdeconfigura çãoquenormalmenteincluiríamosnoarquivo
hibernate.cfg.
Orestantedaconfigura çãodirárespeitoaomodocomomapeamosnossasclas-
ses.Casonossaop çãotenhasidoporarquivosXML,podemosincluirosarquivosa
seremlevadosemconsidera çãoumaumcomonocódigoaseguir:
<bean
class="org.springframework.orm.hibernate3.LocalSessionFactoryBean">
<!-- restante oculto para facilitar leitura -->
<property name="mappingResources">
<list>
<value>springforum.entidades.Assunto.hbm.xml</value>
<value>springforum.entidades.Topico.hbm.xml</value>
<!-- os demais arquivos seguiriam a mesma regra -->
</list>
</property>
</bean>
156


## Página 167

CasadoCódigo Capítulo7. Acessoadados
Masodesenvolvedortambémpodesepreferirapontarquaisoscaminhosden-
trodoclasspathousistemadearquivosaondedevemserbuscadososarquivosde
configuraçãoaseremlidoscomonoexemploaseguir:
<bean class="org.springframework.orm.hibernate3.LocalSessionFactoryBean">
<!-- restante oculto para facilitar leitura -->
<property name="mappingLocations">
<list>
<value>classpath:br.com.itexto.springforum.entidades</value>
<value>file:///home/kicolobo/mapeamentos</value>
</list>
</property>
</bean>
Casonossoobjetivosejalidarcomanota çõescomHibernate3,conformemen-
cionado, LocalSessionFactoryBeannãomaisseencaixa. Apartirdestemo-
mentopassaremosausar AnnotationSessionFactoryBean.Adiferen çaentre
estaimplementaçãoeaquevimosanteriormenteéquenãotemosmaisasproprieda-
des mappingResourcese mappingLocations,massim annotatedClasses
aondedefinimosindividualmentecadaclasseanotadacomaqualtrabalharemose
annotatedPackages,usadaparadefinirquaisospacotesemnossoclasspathque
contémasentidadesanotadasemnossosistema.
Aseguirpodemosverdoisexemplosdedefini çãodestebean:
<bean class="org.springframework.orm.hibernate3.annotation
.AnnotationSessionFactoryBean">
<!-- Definindo classes anotadas individualmente -->
<property name="annotatedClasses">
<list>
<value>br.com.itexto.springforum.entidades.Assunto</value>
<value>br.com.itexto.springforum.entidades.Topico</value>
</list>
</property>
<!-- Ou definindo apenas os pacotes aonde se encontram nossas
classes anotadas -->
<property name="annotatedPackages">
<list>
<value>br.com.itexto.springforum</value>
</list>
</property>
</bean>
157


## Página 168

7.6. OtrabalhocomoHibernate CasadoCódigo
Esim,épossívelmisturarosdoistiposdecaminhonamesmadefini çãopara
obtermáximaflexibilidade.
Quando formos trabalhar com Hibernate 4 nossa vida se
torna mais simples, pois não temos mais duas implemen-
tações distintas de SessionFactory, mas apenas uma:
org.springframework.orm.hibernate4.LocalSessionFactoryBean,
quepodelidartantocomconfigura çõesnoformatoXMLquantoanota ções. E
aindamaisinteressante,aindanospossibilitamisturarosdoisformatoscasoassim
quiséssemos.Abaixopodemosverumexemplodedefini çãodestebean:
<bean class="org.springframework.hibernate4.LocalSessionFactoryBean">
<!-- DataSource -->
<property name="dataSource" ref="dataSource"/>
<!-- As configurações específicas do Hibernate -->
<property name="hibernateProperties">
<props>
<prop key="hibernate.dialect">
org.hibernate.dialect.MySQL5InnoDBDialect
</prop>
<prop key="hibernate.hbm2ddl.auto">update</prop>
</props>
</property>
<!--
As opções de mapeamento que são exatamente as
mesmas que vimos para o Hibernate 3
-->
<property name="annotatedClasses">
<list>
<value>br.com.itexto.springforum.entidades.Assunto</value>
<value>br.com.itexto.springforum.entidades.Topico</value>
</list>
</property>
<property name="annotatedPackages">
<list>
<value>br.com.itexto.springforum</value>
</list>
</property>
<property name="mappingResources">
<list>
<value>springforum.entidades.Assunto.hbm.xml</value>
158


## Página 169

CasadoCódigo Capítulo7. Acessoadados
<value>springforum.entidades.Topico.hbm.xml</value>
</list>
</property>
</bean>
DAOs com Hibernate
AoadotarmosumaferramentaORMcomoHibernateaescritadacamadade
persistênciasetornamuitomaissimplesporqueéordensdemagnitudemaisfácil
escreverDAOsgenéricos,ouseja,aoinvésdeescrevermosumaimplementa çãodo
DAOparacadaentidade,épossívelescreverumaúnicaquesejacapazdelidarcom
omaiornúmerodesitua çõespossívele,paralidarcomoscasosemquesitua ções
peculiaresocorram,bastariaescreverumasubclassedesta.
Comessaclassegenérica,poderíamoscriarummétodoqueencapsuleaobten-
çãoda Session,dessaforma,todososoutrosDAOsqueaherdaremterãoessa
funcionalidade.
public class GenericDAO<T> {
@Autowired
private SessionFactory sessionFactory;
protected Session getSession() {
return sessionFactory.getCurrentSession();
}
// restante oculto para facilitar a leitura
}
Porviaderegra,sempreobtenhaumasessãode SessionFactoryapartir
dafun ção getCurrentSession,poisassimtemosagarantiadequeestaremos
semprelidandodentrodocontextotransacionalcorreto-paratal,vocêdeveativar
osuporteatransa çõesdoSpringcomoveremosnopróximocapítulo,casocontrário
umaexceçãoserádisparadadizendoquenenhumatransa çãoestáativa.Porém,uma
vezconfiguradoodesenvolvedornãoprecisamaissepreocuparcomisto,talcomo
éexpostonoexemploaseguir:
public class GenericDAO<T> {
public void persistir(T objeto) {
getSession().saveOrUpdate(objeto);
159


## Página 170

7.7. IntegrecomaJPA CasadoCódigo
}
}
7 .7 I ntegre com a JP A
Finalmente,temosoJPA.OmodocomoSpringlidacomestatecnologiaéexata-
menteomesmoquevimoscomHibernate.Enquantonaversão3.0doframework
tínhamosaclasse JpaTemplate,esteperdesuafun çãonaversão3.1pelasmes-
masrazõesquelevaramàobsolênciade HibernateTemplate. Sendoassim,as
mesmaspráticasseaplicam:
• AnoteseusDAOscom@RepositoryparaqueoSpringpossafazeratran-
siçãodasexce çõesespecíficasdoJPAparaaspadrãodoSpring;
• Templatesnãosãomaisnecessáriosporque EntityManagerFactoryjá
cuidadacria çãoedestrui çãodasinstânciasde EntityManager;
• Asfacilidadesparapesquisaepersistênciaesperadasemumtemplatejáestão
presentesem EntityManager.
Sendoassim,tudooqueprecisamossaberparatrabalharcomJPAécomoins-
tanciaro EntityManagerFactorycorreto.Amesmaconfigura çãodeambiente
aplicadanocasodoHibernate,ainclusãodadependência spring-ormaplica-se
nocasodoJPA.
Existe um JpaTemplate!
NarealidadeexisteumJpaTemplate, porémdesdeaversão3.1do
Springseuusoénãorecomendadoeaplica-seapenasàprimeiraver-
sãodoJPA,semplanosdeserdesenvolvidonofuturo. Asrazõespelas
quaisestaclassefoimarcadacomodepreciadapelaequipededesenvolvi-
mentodoframeworksãoexatamenteasmesmasquetornaramobsoleto
o HibernateTemplate.
160


## Página 171

CasadoCódigo Capítulo7. Acessoadados
Obtendo o EntityManagerFactory
SemprequeiniciamosumprojetobaseadoemJPAaprimeiraescolhaquepreci-
samosfazerdizrespeitoaotipode EntityManagerFactorycomoqualtrabalha-
remos.Hádoistiposdeacordocomquemogerencia:aaplica çãoouoservidorde
aplicações.Quandogerenciadopelaaplica ção,estaéaresponsávelporcontrolaro
contextotransacionalecomoserãocriadasnovasinstânciasdo EntityManager,já
nocasoemqueocontainerogerencia,aaplica çãodeformaalgumadeveriainteragir
diretamentecomestaentidade.
Para você que trabalha com Spring, não importará qual
EntityManagerFactory será usado, pois o Spring será sempre o responsá-
vel por gerenciar o contexto transacional e o modo como novas instâncias do
EntityManager serão instanciados. O único momento em que esta questão
se apresentará será quando definirmos qual bean declararemos como nossa
implementaçãode EntityManagerFactory.
AssimcomonocasodosuporteaoHibernate3,oSpringnosofereceduasim-
plementaçõesaescolhadodesenvolvedor:
•LocalEntityManagerFactoryBean:paraoscasosemqueaprópriaapli-
caçãogerenciao EntityManagerFactory;
•LocalContainerManagerFactoryBean: no caso de estarmos lidando
comumservidordeaplica ções.
Paracomeçar,veremoscomoconfiguraroJPAquandoesteégerenciadopela
aplicação.AocontráriodoqueocorrenocasodoHibernateemquetodaaconfigura-
çãoémovidaparaocontainerdoSpring,quandolidamoscomJPAénecessárioque
asconvençõesdestemecanismodepersistênciasejamrespeitadas. Istoquerdizer
queaindasefaznecessáriaapresen çadoarquivo persistence.xmldentrododi-
retório META-INFdoseuprojeto,oquenostrazcomovantagemofatodenãopreci-
sarmosdigitarestasconfigura çõesdentrodocontainerdoSpring.Aseguirpodemos
verumexemplodecomodefinirobean LocalEntityManagerFactoryBean.
<bean class="org.springframework.orm.jpa.LocalEntityManagerFactoryBean">
<property name="persistenceUnitName" value="springForumPU" />
</bean>
Repare que só precisamos definir uma propriedade neste caso, que é
persistenceUnitName.Seuvalordevecorresponderàmesmaunidadedepersis-
tênciaquedefinimosnoarquivo persistence.xml.Estaétambémaversãomais
161


## Página 172

7.7. IntegrecomaJPA CasadoCódigo
primitivaoferecidapeloSpring,poisnãonospermitedefinirumafontededados
customizadacomofizemoscomHibernateeJDBC,alémdetambémnãopossuir
suporteatransa çõesglobais.Deveserusadoapenasemambientesdetesteouapli-
caçõesquesejamexecutadasstandalone,ouseja,foradeumservidordeaplica ções.
Casoestejamostrabalhandocomumservidordeaplica ções,tambémpodemos
obterum EntityManagerFactoryBeanviaJNDI.Paratal,bastaprocedermos
exatamentecomofizemosparaobterumafontededadosapartirdestaAPIusando
onamespace jeequevimosnoiníciodestecapítulo.
<jee:jndi-lookup id="emf"
jndi-name="persistence/unidadePersistenciaSpringForum"/>
Nestecasoopré-requisitoédequetodaaconfigura çãoJPAsejagerenciadauni-
camentepeloservidordeaplica çõesresponsávelpeladetec çãodasunidadesdeper-
sistência. NocasoéimportantelembrarqueonomeJNDIdevecorresponderao
nomedaunidadedepersistênciaespecíficodesuaaplica ção.
Efinalmentetemoso LocalContainerEntityManagerFactoryBean::
como opção, que é a mais poderosa oferecida pelo Spring e
nos permite configurar com um nível de granularidade bem
maior o modo como nosso EntityManagerFactory deve se comportar.
Este possui como principais vantagens a possibilidade de
trabalhar com fontes de dados customizadas pelo Spring e o
fato de estar habilitado para lidar com transações locais e
globais, ao contrário de LocalEntityManagerFactoryBean
Umaadiçãobastanteútiléapresen çadapropriedade packagesToScan,que
indicaquaispacotesdevemseresscaneadosparaaprocuradeentidades.
<bean id="emf"
class="org.springframework.orm.jpa.
LocalContainerEntityManagerFactoryBean">
<property name="dataSource" ref="dsSpringForum"/>
<property name="packagesToScan">
<list>
<value>br.com.itexto.springforum.dao.jpa</value>
</list>
</property>
</bean>
162


## Página 173

CasadoCódigo Capítulo7. Acessoadados
Escrevendo DAOs
BasicamenteamesmaestratégiaqueaplicamosaoHibernateérepetidaparao
JPA.BastaqueimplementemosnossosDAOsdetalformaquenestespossaserinje-
tadonossainstânciade EntityManagerFactory.Nestecaso,podemosinclusivetirar
proveitodaanota ção @PersistenceUnitdoJPA,talcomopodeservistonalis-
tagemaseguir:
@Repository
public class GenericDAO<T> {
private EntityManagerFactory emf;
@PersistenceUnit
public void setEntityManagerFactory(EntityManagerFactory emf) {
this.emf = emf;
}
protected EntityManager getEntityManager() {
return emf.createEntityManager();
}
// restante do código omitido
}
EassimcomofizemosnocasodoHibernate,omesmoseaplicaaoJPA.Traba-
lhamoscomestemotordepersistênciaexatamentecomofaríamosnormalmente,tal
comoilustradonocódigoaseguir:
publci class GenericDAO<T> {
public void persistir(T objeto) {
getEntityManager().persist(objeto);
}
}
7 .8 C oncluindo
NestecapítulovimososuportequeoSpringofereceatrêsdasmaispopularesop ções
depersistênciaadotadaspordesenvolvedoresJava:JDBC,HibernateeJPA.Napri-
meirapartedestecapítulovimoscomoaAPIJDBC,apesardetãosólidaélimitada,
fornecendoassimpossibilidadesdemelhoriasquesãomuitobemimplementadasa
partirdostemplatesdoSpring.
Éimportanteobservarasmudan çasqueoframeworksofreudoseureleasean-
terior(3.0)paraoatual(3.1)noquedizrespeitoaoseusuporteaORMs,deixandode
163


## Página 174

7.8. Concluindo CasadoCódigo
ladoostemplateseadotandocomosolu çãoumamenordependênciaentrenossas
classeseasdoframework.
Ficaclaraatendênciaderedu çãodoescopodoSpringnestaáreaconformees-
tasferramentasevoluem.Estatendênciaexibeumacaracterísticamuitopositivada
equiperesponsávelpelodesenvolvimentodoSpring,queéoseupragmatismo.Não
hárazõesparareinventararodaquandoatecnologiasubjacentejápossuiboasal-
ternativasparaosproblemasapresentados.
Nopróximocapítulovamoscriarumaaplica çãowebqueusaráessesDAOsque
criamos.
164


## Página 175

Capítulo8
Desenvolvaaplicaçõeswebcom
SpringMVC
OobjetivoinicialdaprimeiraversãodoSpringerafornecer“apenas”ocontainer
deIoC/DIeumaimplementa çãodaAOPparaaplataformaJava,masconformeo
frameworkiatomandoformaaequipededesenvolvimentopercebeuque,estando
comafacaeoqueijonamãopoderiamsemmuitoesfor çocriarumaalternativaao
frameworkwebmaispopulardaépocaequemuitoosincomodava:Struts.Eassim,
meioqueporacidentefoiincluídonoprojetoumcomponentequecomotempose
mostrouvitalparaapopulariza çãodoframework:o Spring MVC.
Comoveremosnestecapítulo,o Spring MVCémaisqueumframeworkweb:
étambémaaplicaçãodetodasasboaspráticasdeprojetoquevimosnoscapítulos
anterioresdestelivro,oqueotornaumaalternativabastanteviávelnacria çãode
novasaplicaçõeswebparaaplataformaJavaEE.


## Página 176

8.1. Oqueiremosdesenvolver CasadoCódigo
8.1 O que iremos desenvolver
Nestecapítuloiremosdesenvolverumaaplica çãochamada“SpringFórum”.Trata-se
deummotordecomunidadesparadesenvolvedores:écomooGUJ(http://www.guj.
com.br),porémvoltadoparaprogramadoresSpring.Naimagemaseguirpodemos
verapáginainicialdestesistemaemquepodemosveralistagemdeboasvindase
dosúltimosmembrosquesecadastraramnosite.
Figura8.1:PáginainicialdoSpringFórum
Todo o código fonte do projeto encontra-se disponível no GitHub, e você
pode baixá-lo livremente neste link: http://www.github.com/loboweissmann/
spring-forum.Trata-sedeumaferramentainteressantequando,finalizadaaleitura
destelivro,vocêquiserselembrardecomoumououtrorecursodoSpringmencio-
nadonestetextopodeseraplicado.Nesteenopróximocapítulo,entretanto,veremos
apenasasfuncionalidadesdo Spring Fórumrelacionadasaocadastrodemembrose
autenticaçãonosistema,oqueémaisdoquesuficienteparaquepossamosdescrever
bemofuncionamentodoSpringMVC.
166


## Página 177

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
8.2 A base para tudo : MVC
(Antesdecome çarmoséimportanteumpoucodeteoria.Casooleitorjáestejafa-
miliarizadocomopadrãoMVCejáestejacansadodeleraseurespeito,sinta-sea
vontadeparapularestase ção.)
Atualmenteopadrãodeprojetomaispopularadotadopelosframeworksde
desenvolvimentodeaplica çõesweb, trata-sedeumaestratégiaquenospermite
isolarcompletamente-aomenosemteoria-ascamadasdenegócio( Modelo)e
Visualizaçãoatravésdainclusãodeumaintermediária:o Controlador.Acompre-
ensãodestepadrãosetornarámaisclaraconformedescrevemosestascamadas.
O modelodizrespeitoàtodaapartedosistemaresponsávelpelalógicadenegó-
cioeseuscomponentesauxiliares,comopersistência,cacheamento,integra çãocom
outrossistemasetc.
A visualização,comoopróprionomejánosdiz,éapartevisívelaousuário
final.QuandonosdeparamoscomumajanelaoupáginaHTML,estamoslidando
diretamentecomoresultadodestacamada.
Finalmente,temosacamadamenosóbviaqueéo controlador,queorquestra
ainteraçãoentreasduascamadasacimacitadas. Quandoousuárioclicaemum
link,ocontroladoréacionado.Estetransformaosparâmetrosdeentradaparaum
formatoquesejacompatívelcomainterfacedisponibilizadapelacamadadenegócio,
cujoresultadodoprocessamentoérecebidopelocontrolador,queomodificacaso
necessárioeemseguidaoenviaàcamadadevisualiza çãoparaquesejacontemplado
pelousuáriofinal.
Figura8.2:OpadrãoMVC
167


## Página 178

8.3. IniciandooProjeto CasadoCódigo
Nofinaldascontas,oqueobservamosnopadrãoMVCémaisumasolu çãoao
problemadoaltoacoplamento.Comoacamadadevisualiza çãonãopossuiacesso
diretoàcamadadenegócioevice-versa,asubstitui çãodeumaououtrasetornamais
fácil. Alémdisto,vemostambémganhosimensosnamanutenibilidadedenosso
modelo. Dadoqueeste não sabe daexistênciadeumacamadadevisualiza ção,o
desenvolvedorprecisalidarcommenosdependênciase,consequentementeacabará
produzindocódigodemaiorqualidade,maisfacilmentetestávelecomoobjetivamos
desdeoprimeirocapítulo,comacoplamentosignificativamentemaisbaixo.
8.3 I niciando o Projeto
NossoprimeiropassoserácriarumprojetowebnopadrãoJavaEE(5ouposterior).
UmadasmaneirasmaispadronizadaseprodutivasatualmenteéusandooMaven,
quecriaráaestruturadediretóriosbásicaetodaaestruturaqueusaremosnade-
claraçãodenossasdependências.Alémdisto,projetosbaseadosemMaventambém
possuemagrandevantagemdeseremagnósticosemrela çãoàIDE,oquepermitirá
aoleitortrabalharcomasuaop çãofavorita.
Crie o projeto com Maven
NãoéumexagerodizerquetodasasIDEsatualmenteoferecemsuporteàcria ção
deprojetoswebcomMaven,masomodocomocadaumaimplementaestafuncio-
nalidadevaialémdoobjetivodestelivro,razãopelaqualseráexpostoapenascomo
criarumnovoprojetoapartirdeumarquétipopadrãopelalinhadecomando.No
caso,ocomandousadoparacriaroprojeto Spring FórumcomMavenéoseguinte:
mvn archetype:generate -DgroupId=br.com.itexto -DartifactId=spring-Forum
-Dversion=1.0.0-SNAPSHOT -DarchetypeArtifactId=maven-archetype-webapp
Duranteaexecu çãodoMaven,seráperguntadoqualonomedopacotepadrão
usadopeloprojeto.Nonossocasoescolhemos br.com.itexto.springForum.
Ecomistocriamosumprojetoidentificadopelogrupo br.com.itextoeidenti-
ficador spring-Forumcomaversão 1.0.0-SNAPSHOT.
Incluindo as dependências fundamentais
Comoprojetocriado,nossopróximopassoseráincluirasdependênciasfun-
damentais:nesteprimeiromomentosóprecisamosnospreocuparcomumaqueé
168


## Página 179

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
opacote spring-webmvcquedeveráserdeclaradanatag <dependencies>do
arquivo pom.xml,comoaseguir:
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-webmvc</artifactId>
<version>3.1.2.RELEASE</version>
</dependency>
ObservequenãoprecisamosdeclararoutroscomponentesdoSpringcomopor
exemplo spring-core, spring-contexteoutros,poistodossãodependências
transitivasdo spring-webmvc. ParafacilitarousodaIDE,outradependência
importanteaserincluídaéoJSTL1.2,cujadependênciaéexpostaaseguir:
<dependency>
<groupId>jstl</groupId>
<artifactId>jstl</artifactId>
<version>1.2</version>
<scope>provided</scope>
</dependency>
Comestadependênciaorecursodepreenchimentoautomáticodecódigopela
IDEsetornarámaisfácilquandoestivermostrabalhandocomtagsJSTLemnossos
arquivosJSP.
Comotemplate,oleitorpodeusaroarquivo pom.xmlpresentenaraizdopro-
jeto Spring Fórum.
A configuração do Dispatcher Servlet
OnúcleodoSpringMVCéo Dispatcher Servlet,queéoresponsávelporgerenciar
todasasrequisi çõesrecebidaspelanossaaplica ção.Sendoassim,nadamaisnatural
quenossopróximopassosejasuaconfigura ção. Precisamosdeclará-lonoarquivo
web.xml,presentenodiretório src/main/webapp/WEB-INFdonossoprojeto.
OprimeirotrechodecódigoqueprecisamosdeclararéodoServletemsi:
<servlet>
<servlet-name>DispatcherServlet</servlet-name>
<servlet-class>
org.springframework.web.servlet.DispatcherServlet
</servlet-class>
<load-on-startup>1</load-on-startup>
</servlet>
169


## Página 180

8.3. IniciandooProjeto CasadoCódigo
Atag <servlet>éusadaparadeclararumservletdisponibilizadopornossa
aplicação.Aten çãoespecialdeveserdadaaonomequeusaremosparaidentificaro
servlet( <servlet-name>).Umaveziniciado,oServletirácarregarumcontainer
doSpringconfiguradoviaXMLporumarquivochamado WEB-INF/[nome do
servlet]-servlet.xml.Sendoassim,deacordocomocódigoanterioroServlet
buscarápeloarquivo DispatcherServlet-servlet.xml.
Épossívelcustomizaronomedoarquivodeconfigura ção,paraistobastaadi-
cionaroparâmetrodeinicializa ção contextConfigLocationàdeclaraçãodo
Servlet:
<servlet>
<servlet-name>DispatcherServlet</servlet-name>
<servlet-class>
org.springframework.web.servlet.DispatcherServlet
</servlet-class>
<init-param>
<param-name>contextConfigLocation</param-name>
<param-value>/WEB-INF/spring/spring-servlet.xml</param-value>
</init-param>
<load-on-startup>1</load-on-startup>
</servlet>
DeclaradooServlet,opróximopassoseráomapeamentodasURLsaestedire-
cionadas.Paratalusamosatag <servlet-mapping>:
<servlet-mapping>
<servlet-name>DispatcherServlet</servlet-name>
<url-pattern>/</url-pattern>
</servlet-mapping>
Atençãoespecialdeveserdadaàtag <url-pattern>.Nocasodo Spring Fó-
rum,optamospelomapeamento /.AssiminstruímosoServletContaineratratar
nosso Servlet Dispatchercomoopadrãoaserinvocadoparatodasasrequisi çõesre-
cebidaspelaaplica ção.Estenãoéoúnicomapeamentopossível:narealidadequal
opçãoaseradotadairávariardeacordocomasitua çãoeogostododesenvolvedor.
Podemosteralgumasoutrasop çõesinteressantesdemapeamentoquepoderiam
seradotadassemqualquerproblema:
•/**:indicaque qualquerrequisiçãoindependentedaURLserádirecionada
aonossoservlet.
170


## Página 181

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
•*.jsp: todaURLterminadacom .jsp. Exemplo: http://www. springFó-
rum.com.br/entrada.jsp
•/spring/**:todaURLiniciadacom spring.Exemplo: http://www. spring-
Fórum.com.br/spring/entrada
8.4 D ispatcher Servlet : o maestro por trás do
Spring MVC
Émuitoimportanteconhecerocomponenteresponsávelpororquestrarofunciona-
mentodo Dispatcher Servlet.Esteénarealidadeaimplementa çãodopadrão
Front Controller,muitousadonaescritadeframeworksvoltadosparaacria çãode
aplicaçõesweb.Oobjetivodestepadrãodeprojetoéfornecerumpontodeentrada
centralparatodasasrequisi çõesdirecionadasànossaaplica ção.Éseutrabalhoin-
terpretarestesrequisitosedecidirqualocomponenteresponsávelporseuprocessa-
mentoeeventualretornoparaousuário.
Afiguraaseguir,inspiradanadocumenta çãooficialdoprojeto,nosajudaater
umavisãoglobaldomodocomoestepadrãoseencaixadentrodocontextodoSpring
MVC.
Figura8.3:OpadrãoFrontControllernocontextodoSpringMVC
Apesarderaríssimasvezesprecisarmosinteragirdiretamentecomestecompo-
nente-quenãofoiprojetadoparaisto-conhecê-loéfundamentalparatrabalharmos
comoframeworkpoisinteragediretamentecomosprincipaiscomponentesportrás
dofuncionamentodo Spring MVC.
Todachamadaaoservidorinicia-sesobaformadeumarequisi çãoetermina
comoumarespostaenviadaaocliente.Duranteessecaminhoocorremcincoeventos
esquematizadosnafiguraaseguir,queexpõemoscomponentesfundamentaispor
171


## Página 182

8.4. DispatcherServlet:omaestroportrásdoSpringMVC CasadoCódigo
trásdoSpringMVC.Emumprimeiromomentooleitorpodesesentirassustado
comestenúmero,noentantoéimportantemencionarquedosquatroelementosque
serãodescritossóprecisaremoslidarcomdoisdestesapósfinalizadaaconfigura ção
daaplicação.
Figura8.4:Ociclodevidadeumarequisi ção
Comomencionado,tudocome çanomomentoemqueumarequisi çãochegaao
Dispatcher Servlet.Estaterásuaassinaturaanalisadaeenviadaao Mapeador
de requisições (Handler Mapping),queéocomponenteresponsávelpordesco-
brirqualcontroladordeveseracionado.
Umavezobtidoocontroladoralvo,esteéexecutadoeumnomelógicodotem-
platedevisualiza çãoaserrenderizadocomorespostaaousuário( view)éretornado
ao Dispatcher Servlet eoconjuntodevariáveis( model)queserãoexpostas
nestarenderização.
Com o nome lógico da visualização e o modelo obtidos, entra em cena o
Gerenciador de visualização (View Resolver),quepossuiafun çãode,com
basenonomedaview,retornarao Servlet Dispatcher qualelementodevi-
sualização-maiscomumenteumapáginaJSP-deveráserrenderizadadevoltaao
usuárioquefezarequisi ção.
Prepare o container do Spring
Comtodaaestruturafundamentalpronta,nossoúltimopassonaprepara çãodo
ambienteseráaconfiguraçãodocontainerIoC.Nocasodo Spring Fórum,oprincipal
172


## Página 183

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
arquivodeconfigura çãoéoarquivo spring-servlet.xml,presentenodiretório
src/main/webapp/WEB-INF/spring.
Entraemcenaumnovo namespace,chamado mvc,queseráusadoparaalimen-
tarmoso Dispatcher Servletcomconfiguraçõesadicionais.Énestepontodaaplica ção
quesãoincluídasasdefini çõesdecomponentescomoo Handler mappingeo View
resolverporexemplo.Aseguirpodemosveradeclara çãodestenamespace:
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:context="http://www.springframework.org/schema/context"
xmlns:mvc="http://www.springframework.org/schema/mvc"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context-3.1.xsd
http://www.springframework.org/schema/mvc
http://www.springframework.org/schema/mvc/spring-mvc-3.1.xsd">
<!-- Conteúdo ignorado para facilitar leitura -->
</beans>
Apenasacria çãodoarquivodeconfigura çãonãoésuficienteparaqueoSpring
MVCsejaativado:énecessárioincluirmosalgumasinstru çõesbásicasneste:
<beans ...>
<mvc:annotation-driven />
<context:annotation-config />
<context:component-scan
base-package="br.com.itexto.springForum.controladores"/>
</beans>
Aúnicanovidadeéatag <mvc:annotation-driven/>,queinstruio Servlet
Dispatcherabuscarseuscontroladoresapartirdeanota ções:aformamaispopular(e
produtiva)desetrabalharcomoSpringMVC.Sozinha,noentanto,estanãopossui
muitaserventia,énecessárioinstruirocontainerdequeestebuscaráadefini çãode
nossosbeansapartirdeanota ções-ocontroladoréumbeandiferenciadopeloeste-
reótipo @Controller-equaisospacotesquedevemservarridosparatal:voltam
astags <context:annotation-config/>e <context:component-scan>
quevimosnocapítulo4.
173


## Página 184

8.5. OlámundocomSpringMVC CasadoCódigo
8.5 O lá mundo com Spring MVC
Comquasetodasasnossasconfigura çõesnolugar,jápodemossentirumgostinho
decomoéaescritadeumcontroladornoSpringMVC.Paratal,iremosescreveralgo
extremamentesimples:umapáginaqueexponhaahoraatualdoservidoracompa-
nhadadeumasauda ção,talcomopodemosvernaimagemaseguir:
Figura8.5:Nosso‘Olámundo!’
Nosso primeiro passo será a escrita do controlador. Para
tal, crie uma classe chamada OlaMundoController no pacote
br.com.itexto.springforum.controladores, cuja listagem pode ser
vistaaseguir:
package br.com.itexto.springforum.controladores;
import java.util.Date;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
@Controller
public class OlaMundoController {
@RequestMapping("/ola")
174


## Página 185

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
public ModelAndView olaMundo() {
ModelAndView resultado = new ModelAndView("mundo");
resultado.addObject("data", new Date());
return resultado;
}
}
Hámuitanovidadenestecódigo,sendoassim,antesdeexperimentá-lo,vamos
veroqueelefaz.Vamoscome çarpelaanota ção @Controller.Estanarealidade
extendeaanota ção @Componentquevimosnocapítulo4.Quandoaplicamosesta
anotaçãoemumaclasse,estamosinformandoaocontainerdoSpringquetrata-se
deumtipoespecialdebean:umcontrolador,queseráusadopeloSpringMVCpara
tratarasrequisi çõesHTTPrecebidaspornossaaplica ção.
É gra ças às tags <mvc:annotation-driven/>,
<context:annotation-config/> e <context:component-scan/>
queocontainersaberáemquaispacotesbuscarnossasclassesdecontrole.
Outranovidadeinteressanteéaanota ção @RequestMappingquedeveser
aplicadasobreosmétodosdonossocontroladorquedesejamossereminvocados
deacordocomopadrãodeURLquedefinirmosemseuinterior. Nocasodafun-
ção olaMundo,semprequeaURLhttp://spring-forum/olaforrequisitada,oSpring
MVC,sabendodaexistênciadonossocontrolador,executaráafun ção olaMundo,
queretornaumobjetodotipo ModelAndView,queatéestemomentoapenastra-
tamosdeformateórica.
TodocontroladordoSpringMVCretornaimplícitaouexplicitamente(como
éocasodonosso OlaMundoController)umobjetodotipo ModelAndView.
Suafunçãoéfornecerao Dispatcher Servletosdadosqueestarãodisponíveispara
acamadadevisualiza çãoe,aindamaisimportante,qualpáginadanossaaplica ção
deveráserrenderizada.
Oconstrutorquerecebecomoparâmetrouma Stringnosinformaqualo
nomedapágina( view)aserrenderizada: nojargãodoSpringistosechama view
name.Jáométodo addObjectrecebedoisparâmetros:oprimeirodizcomoova-
lorseráidentificadopelapáginadurantesuarenderiza çãoeosegundoéopróprio
valor.
Nomomentodarenderiza ção,o modelétransparenteparaapágina.Estaapenas
temacessodiretoaosseusvalores,talcomopodemosvernapágina mundo.jsp,
presentenodiretório src/main/webapp/viewsdonossoprojeto,cujalistagem
175


## Página 186

8.5. OlámundocomSpringMVC CasadoCódigo
vemosaseguir:
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Ola mundo com Spring Framework</title>
</head>
<body>
<h1>Oi mundo!</h1>
<%-- O mesmo atributo 'data' que definimos no model --%>
<p>Hora é: ${data}</p>
</body>
</html>
Neste nosso ‘olá mundo’, ainda há uma pergunta a ser respondida: como
o Spring sabe que é o arquivomundo.jsp que será renderizado? Gra-
ças ao view resolver. É necessário informar ao Spring qual implementação
usar. Neste nosso primeiro exemplo usamos a mais simples das implementa-
çõesqueéo InternalResourceViewResolver,quedeclaramosnoarquivo
spring-servlet.xml,talcomonalistagemaseguir:
<bean id="viewResolver"
class="org.springframework.web.servlet.view.InternalResourceViewResolver" >
<property name="prefix">/views/</property>
<property name="suffix">.jsp</property>
</bean>
Ofuncionamentodestecomponentenãopoderiasermaissimples.Precisamos
definirduasdesuaspropriedades: prefixe sufix.Oprefixoinformaqualoiníciodo
caminhoquelevaaoarquivoJSPaserrenderizado:inícioestequecorresponderáà
pastaemnossoprojetoqueacontém.Jáosufixodizrespeitoàextensãodoarquivo.
Comonossocontroladordefinecomo view nameovalor mundo,serárenderizadoo
arquivo /views/ mundo.jsp.
Pronto,agoravocêpodeacessarasuaaplica çãoemseuservidor,atravésdaurl
/olaeveráapáginacomahoraatual.
176


## Página 187

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
Figura8.6:Nosso‘Olámundo!’
8.6 O primeiro controlador útil do Spring Fórum
Destepontoemdiante,iremosnospreocuparcomapenascincobeans,ilustrados
comsuasrespectivasdependênciasnaimagemaseguir:
Figura8.7:Osbeansquetomarãonossaaten ção
Trêsdestesbeanssãocontroladores: HomeController,responsávelpelapá-
ginainicialeoformuláriodecadastrodosistema, AutenticacaoController
177


## Página 188

8.6. OprimeirocontroladorútildoSpringFórum CasadoCódigo
que usaremos temporariamente como nosso mecanismo de autenticação e
UsuarioController,paralistarocadastrodeusuáriosdosistema. Estesusam
comodependênciasdoisDAOs: DAOUsuarioe DAOAssunto,usadosrespectiva-
menteparaobterepersistirinstânciasdeobjetosdotipo Usuarioe Assunto.
Oprimeirocontroladorqueveremosétambémomaissimples: trata-sede
HomeController,cujocódigofonteresponsávelporprocessaravisualiza çãoda
páginainicialdositeélistadoaseguir:
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
@Controller
public class HomeController {
@Autowired
private DAOUsuario daoUsuario;
@Autowired
private DAOAssunto daoAssunto;
@RequestMapping("/")
public String index(Map<String, Object> model) {
model.put("assuntos", getDaoAssunto().list());
model.put("usuarios", getDaoUsuario().list());
return "index";
}
// getters e setters
}
Aslinhasacimanosdizembastantearespeitodomodocomocontroladoressão
escritosparaoSpringMVC.Nossoprimeiropontodeaten çãodizrespeitoaanota-
ção @Controllerquenosfoiapresentadaemnosso‘Olámundo’.Observequehá
algumasdependênciascujaimplementaçãonãonosinteressanestemomento(foram
tratadasnocapítulo7),mascujasinterfacesencontram-selistadasaseguir:
public interface DAOUsuario extends DAOBase<Usuario> {
/* Busca usuario por login e senha */
public Usuario getUsuario(String login, String senha);
178


## Página 189

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
/* Busca usuario pelo login */
public Usuario getUsuario(String login);
/* Retorna a lista de usuários com paginação */
public List<Usuario> list(int offset, int max);
}
public interface DAOAssunto {
/* Retorna a lista de assuntos com paginação */
public List<Assunto> list(int offset, int max);
/* Persiste o assunto */
public void persistir(Assunto objeto);
/* Exclui o assunto */
public void excluir(Assunto objeto);
/* Retorna um assunto por seu identificador */
public Assunto get(Long id);
}
Aanotação @RequestMapping,umavezaplicadaaumafun çãodenossocon-
troladorotransformaemuma action,istoé,emummétodoresponsávelpelopro-
cessamentodaURLmapeada.Observequenossaactionrecebecomoparâmetroum
mapa.EstepossuiumnomeespecialdentrodoSpringMVC:sechamamodelo( mo-
del),erepresentaoconjuntodedadosquesãotransportadosdocontroladorparaa
camadadevisualiza ção.
Comopodeserobservado,incluímosdoisatributosnomapa: assuntose usu-
arios,representandorespectivamentealistagemdeassuntoseúltimosusuáriosca-
dastradosnosistema,talcomopodeservistoemdestaquenaimagemaseguir:
179


## Página 190

8.7. Autenticandousuários:comoredirecionarelidarcomasessãoHTTP CasadoCódigo
Figura8.8:Aondeseráexpostooconteúdodosatributos assuntose usuariosincluí-
dosnomodelo
PararecuperarosobjetosdisponíveisparaoJSP,napágina,bastariausara Ex-
pression Language ${assuntos}e ${usuarios}.
Oúltimopontoaserobservadoéovalorderetornodonossométodo:a String
indexapontaparaonomelógicodo templatedevisualizaçãoqueserárenderizado
comorespostaaousuárioqueoriginouarequisi ção.Entenderemoscomdetalheso
mecanismoderenderiza çãonotranscorrerdocapítulo.Nestemomentooleitordeve
estarseperguntando:“nãodeveríamosretornarumobjetodotipo ModelAndView
aoinvésdeumastring?”.
UmdosobjetivosportrásdoSpringMVCéfornecerliberdadeaodesenvolve-
dor.Quandouma actionretornaumastring,opróprioframeworkseencarregaráde
construirinternamenteumobjetodotipo ModelAndViewcujo view namecorres-
ponderáaovalordastringretornada.Sea actionrecebercomoparâmetroum Map,
esteseráinterpretadocomoo modeldoobjeto ModelAndView.
8.7 A utenticando usuários : como redirecionar e li-
dar com a sessão HTTP
Faremosagoraumcontroladorumpoucomaiselaborado:aqueleresponsávelpela
autenticaçãodeusuáriosno Spring Fórum.Amarca çãoHTMLusadaemnossofor-
mulárioéexpostaaseguir.Oúnicoaspectoquetalvezsejanovidadeéousodatag
JSTL <c:url/>paragarantirqueaURLdatag actiondoformuláriosempreaponte
180


## Página 191

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
paraoendere çocorreto,nocaso,oendere çorelativodanossaURLdeautentica ção.
<form action="<c:url value="/login"/>" method="post">
<input type="text" name="login"/>
<input type="password" name="senha"/>
<input type="submit" value="Entrar"/>
</form>
Umavezfeitaasubmissão,nosso Handler Mappingiráidentificarocontrolador
deautenticaçãopelofatodestepossuiraanota ção @RequestMappingapontando
paraomesmoendere çoeemseguidaexecutaráotruque:
@Controller
public class AutenticacaoController {
@RequestMapping(value="/login", method=RequestMethod.POST)
public String login(@RequestParam("login") String login,
@RequestParam("senha") String senha,
HttpSession sessao) {
Usuario usuario = daoUsuario.getUsuario(login, senha);
if (usuario == null) {
return "loginFalho";
} else {
usuario.setUltimoLogin(new Date());
daoUsuario.persistir(usuario);
sessao.setAttribute("usuario", usuario);
return "redirect:/";
}
}
}
8.8 D efinindo qual método HTTP usar
Aprimeiranovidadequeoleitorencontraráemnossocontroladoréainclusãodo
parâmetro methodnaanotação @RequestMapping. Estedeterminaquenossa
açãosomentereconheceráoacessoaURLdeautentica çãoseométodoHTTPforum
POST.Aotentaracessaromesmoendere çopelonavegador, pulando a submissão do
formulário,seremossaudadospeloerroHTTP405,nosinformandoqueométodo
nãoésuportadopelo Spring Forum,jáqueonavegadorenviaumarequisi ção GET,
comopodeservistonaimagemaseguir.
181


## Página 192

8.9. Recebendoparâmetrosdeentrada CasadoCódigo
Figura8.9:TentarseautenticarnosistemapelaURLnãoiráfuncionar.
Épossíveltambémpassarmaisdeummétododeacessoaoparâmetro method.
Bastaincluí-losem Array,comonoexemploaseguir,quepossibilitaagoraauten-
ticaçãotambémpelométodo PUT.
@RequestMapping(value="/login",
method={RequestMethod.POST, RequestMethod.PUT})
Dessaforma,paraseusmétodosdea ção,bastaindicarquaissãoosmétodos
aceitosatravésdoatributo methodnaanotação RequestMapping.
8.9 R ecebendo parâmetros de entrada
UmpontointeressantenoSpringMVCéatotalliberdadeoferecidaaodesenvolvedor
noquedizrespeitoàassinaturadenossasa çõestalcomopodeserobservadona
assinaturadanossafun ção login:
@RequestMapping(value="/login", method=RequestMethod.POST)
public String login(@RequestParam("login") String login,
@RequestParam("senha") String senha,
HttpSession sessao) {
...
}
182


## Página 193

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
Surgeumanovaanota ção: @RequestParam,quemapeiaosparâmetrosdofor-
mulário(ouURL)paraosdenossaa ção.Ovalorfornecidoparaaanota çãocorres-
pondeaonomedoparâmetrodeentradadefinidopeloformulárioouURL.Seuuso
éopcionalporémrecomendado.Casoomitida,o Spring MVCfaráomapeamento
deparâmetroscombasenonomedosmesmosdefinidosnométodo.
Anotações em parâmetros
Éimportanteobservarqueno bytecode,onomedosparâmetrossó
seencontrapresentequandoocódigoécompiladocominforma çõesde
depuração. Dadoquenemsemprepodemosterestagarantia,adota-se
apráticadeanotarosparâmetrosdosmétodoscomoumaboapráticaa
serseguida.
8.10 O que é aquele“redirect :/” retornado pela ac -
tion login?
Háumúltimopontointeressanteemnossaclasse AutenticacaoController.
Quandoéencontradoumusuáriocomo logine senhafornecidos,ovalorre-
tornadopela actioné redirect:/.Estainstru çãodizao Spring MVCquedeveser
feitoumredirecionamentoparaavisualiza çãocujonomelógicoé /,ouseja,araiz
doprojeto,quenocasoéaa ção indexdo HomeController.
Quandofazemosoredirect,indicamosparaonavegador,queéoclientede
nossaaplicação,queumanovarequisi çãodeveserenviadaparaoendere çoindi-
cado. Dessaforma,ocaminho /serárequisitado,ecomoconsequência,aa ção
indexdo HomeControllerseráinvocada,disparandoassimasconsultaspelos
assuntoseusuáriosnobancodedados.
8.11 C omo lidar com a sessão do usuário e a classe
ModelAnd View
Vimoscomoacessardiretamenteasessãodousuárionaaction login,implemen-
tadanaclasse AutenticacaoController.Bastaincluircomoparâmetroumatri-
butodotipo javax.servlet.http.HttpSession.Tambémépossívelacessar
atributosdesessãodeformatransparente,istoé,semanecessidadedemanipula ção
diretadeobjetos HttpSession,atravésdousodeanota ções.
183


## Página 194

8.11. ComolidarcomasessãodousuárioeaclasseModelAndView CasadoCódigo
Para exemplificar este recurso, nosso foco agora será o controlador
UsuarioController, onde implementaremos uma ação responsável por re-
tornarosdetalhesdousuárioatualmenteautenticadonosistema.Relembrando,na
action login,quandoaautentica çãoébemsucedidacriamosumnovoatributo
de sessão chamadousuario. Este comportamento é o gancho para a action
infoAutenticado,cujocódigofontepodemosveraseguir:
@Controller("usuario")
@SessionAttributes("usuario")
public class UsuarioController {
@RequestMapping("/usuario/autenticado")
public ModelAndView infoAutenticado(
@ModelAttribute("usuario") Usuario usuario) {
ModelAndView mav = new ModelAndView("usuario/show");
mav.getModel().put("usuario", usuario);
return mav;
}
}
A técnica contém dois passos: o primeiro consiste na inclusão da anota-
ção @SessionAttributesnaclassequeimplementanossocontrolador. Esta
pode receber dois tipos de valores, umaString, tal como fizemos na classe
UsuarioControllerounocasodeprecisarmosdemaisdeumatributodeses-
são,umarrayde String.Ovalordestas Stringdevecorresponderaonomedo
atributocomoqualqueremosreceberdiretamentedasessão.
Usaremososatributosdesessãonosegundopasso:anotamososparâmetrosde
nossasactionscom @ModelAttribute,querecebecomovaloronomedachave
correspondenteaoobjetopresentenasessãodousuário,talcomofoifeitonaaction
infoAutenticadoexpostaacima.
Portrásdospanos,ofuncionamentodoSpringMVCéoseguinte:apósarequi-
siçãoserrecebidapelo Dispatcher Servlet,esteirábuscarocontroladorresponsável
porseuprocessamento.Seestiveranotadocom @SessionAttributes,estepas-
saráàactionosatributosdesessãodefinidospelasanota ções @ModelAttribute
eemseguidacontinuarásuaexecu çãonormal.
Éinteressanteobservarque,aocontráriodoquevimosatéomomento,ovalorde
retornodaaction infoAutenticadonãoéuma String,massimumobjetodo
184


## Página 195

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
tipo org.springframework.web.servlet.ModelAndView,queéumaclasse
utilitáriadoframework,usadaparaencapsularduasentidadesquevimossendotra-
balhadasindividualmentenodecorrerdestecapítulo:onomelógicodavisualiza ção
queserárenderizadadevoltaaousuário( view)eosdadosembutidosnestapresentes
nomodelo( model).
Nasprimeirasversõesdo Spring MVC,esteeraovalorderetornoobrigatório
detodasasactions,poistornavaaimplementa çãodo Springmaisfácildeserfeita.
Passadoalgumtempo,comaintrodu çãodasanota çõesnoJava5,ficoumaisfácila
obtençãodasduasentidadesencapsuladasporesteobjeto,oquefezcomqueesta
convençãocaísseporterra.
Apesardenãosermaisumtipoderetornoobrigatório,aindaéumobjetobas-
tanteútilepossuialgunsmétodos,comooslistadosabaixo,quefacilitambastantea
vidadodesenvolvedor:
•String getViewName():retornaonomedaview;
•void setViewName(String valor) :defineonomedaviewaserrende-
rizada;
•ModelAndView addObject(String nome, Object valor) : adici-
onaumnovoatributoaomodelo;
•ModelMap getModelMap():retornaumobjetodotipo ModelMaprepre-
sentandoomodelo.Estaclasseporbaixodospanoséumaimplementa çãoda
interface Map<String, Object> doJava;
•void clear():limpaomodelo.
Nãoháumaregrasobrequandousarumaop çãoououtra,nessecaso,ficaacargo
dodesenvolvedorusarasop çõesdisponíveisdeacordocomsuapreferência.
8.12 C adastrando usuários : submissão de formulá -
rios
Dificilmenteencontramosumaaplica çãowebcominterfacegráficaquenãoprecise
lidarcomalgumtipodeformulário.Vimoscomotratarformuláriosbastantesimples
nocontrolador AutenticacaoController,masaquelenãorefletearealidade,
185


## Página 196

8.12. Cadastrandousuários:submissãodeformulários CasadoCódigo
poisconvenhamos,sãomuitorarosformulárioscomtãopoucoscampos.Nestases-
são,conheceremososuporteoferecidopelo Springnamanipulaçãoevalida çãode
formulários.
Processando formulários
Faremosoformuláriodecadastrodeusuáriosdo Spring Fórum,queusacomo
controladoraclasse HomeController.
Figura8.10:Oformuláriodecadastro
Oscampospresentesnoformuláriocorrespondemaosatributosdefinidosna
classededomínio Usuarioquetempartedesuaimplementa çãolistadaaaseguir:
public class Usuario {
private String nome;
private String email;
private String login;
private String senha;
186


## Página 197

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
// getters e setters
}
Partedonossoobjetivonopreenchimentodoformulárioétambémopreenchi-
mentodosatributosdaclasse Usuario. Paraobteresteresultado,entraemcena
abibliotecadetagsdo Springparaoprocessamentodeformulários,cujaaplica ção
vemosnamarca çãodonossoformulárioderegistroaseguir:
<%@taglib prefix="sf" uri="http://www.springframework.org/tags/form"%>
<sf:form modelAttribute="usuario" action="executarRegistro">
<label for="nome">Nome:</label>
<sf:input path="nome"/>
<label for="email">Email:</label>
<sf:input path="email"/>
<label for="login">Nome do usuário (login):</label>
<sf:input path="login"/>
<label for="senha">Senha:</label>
<sf:password path="senha"/>
<input type="submit" value="Faça parte!"/>
</sf:form>
O Spring MVCvemcomumabibliotecadetagsespecificamentedesenvolvida
paraprocessamentodeformulários. Estaédefácilaprendizadoparaosdesenvol-
vedores,poispossuisemânticamuitopróximaaosubconjuntodetagspresentesno
HTMLparaomesmofim.
Comoveremos,parapraticamentetodasasop çõespresentesnoHTML,háuma
tagfeitapelaequipededesenvolvimentodo Spring,usadaparafazeraliga çãoentreos
objetospresentesnomodeloqueseráfornecidoàvisualiza çãoeoscamposdefinidos
noformulário.
Comopodeservistonalistagemacima,parainiciarmosaimplementa çãode
nossosformuláriosnamarca ção,come çamoscomatag <sf:form>(vocêpossui
liberdadetotalparaescolheroprefixoquequiser).Estacorrespondeàtagdemesmo
nomenoHTMLepossuicomoprincipaldiferencialoatributo modelAttribute,
ondeovalorapontaparaoobjetonomodeloecujaspropriedadesserãoexpostasou
ligadasaoscamposdoformulário.
187


## Página 198

8.12. Cadastrandousuários:submissãodeformulários CasadoCódigo
Nocasodoformulárioanterior,oobjeto usuarionãosurgecomomágica.
Estefoiincluídonomodelopelaaction registro,implementadanocontrolador
HomeController,queéaactionqueseráinvocadaparaacessarmosateladeca-
dastrodousuário:
@RequestMapping("/registro")
public String registro(Map<String, Object> model) {
if (model.get("usuario") == null) {
model.put("usuario", new Usuario());
}
return "registro";
}
Noformulário,podemosverduastagsdeliga çãofornecidaspeloframework:
<sf:input>e <sf:password>,usadasrespectivamenteparacampostextuaise
senha.Oatributomaisimportantepresentenestastagsé path,cujovaloraponta
paraonomedapropriedadedoobjetorepresentadoaondeseráfeitaaliga ção.
Éimportantemencionarqueovalordoatributo pathnãoprecisaserumapro-
priedadediretadoobjeto. Sehipoteticamentequiséssemosdefinirumatributodo
tipo Assuntonaclasse Usuario,poderíamosligá-loaoformuláriosemproblema
algumtal:
<label for="Assunto favorito">Assunto favorito:</label>
<!-- Referenciando uma propriedade indireta -->
<sf:input name="assunto" path="assunto.nome"/>
Alémdastagslistadasacima,tambémpodemoscontarcomumasériedeoutras,
cujasprincipaisencontram-selistadasaseguir:
•checkbox:usadapararenderizarcamposdotipocaixadesele ção;
•checkboxes:usadapararenderizarumalistadecaixasdesele ção;
•radiobutton:para radiobuttons;
•select:paracaixasdesele ção. Esim,hátambémuma optionparaque
possamosdefinircommaiorcontroleasop çõespresentesnesta;
•textarea:paracaixasdetextodemúltiplaslinhas;
•hidden:usadaparacamposocultos.
188


## Página 199

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
8.13 S ubmetendo o formulário de cadastro
Conhecidasastagsbásicasdeliga çãoeescritonossoformulário,opróximopasso
éasubmissão. Amelhormaneiradeentendê-loénaprática,sendoassim,vejaa
implementaçãodaaction executarRegistronaclasse HomeController:
@RequestMapping(value="/executarRegistro", method=RequestMethod.POST)
public String executarRegistro(Usuario usuario, HttpSession sessao) {
getDaoUsuario().persistir(usuario);
sessao.setAttribute("usuario", usuario);
return "redirect:/";
}
Odesenvolvedorprecisaapenasincluirumparâmetronaassinaturadométodo
alvo,cujotipocorrespondaaoobjetoinicialmentepresentenomodeloetodoopro-
cessodeliga çãoéfeitodeformatransparentepeloframework.
Nocasodapáginaderegistro,aentidade Usuariopossuitodasassuaspropri-
edadesidentificadosnosatributos pathdoselementosdoformulário.Nemsempre
esteseráocaso.Paraestasoutrassitua ções,apráticamaiscomuméacria çãodeuma
classeespecialcujosatributospossamserdiretamentemapeadosparaoformulário
emquestão.
E se eu não quiser usar a Tag do Spring MVC?
Apesardetrazerumacertafacilidadenodesenvolvimentodocódigo
daview,ousodaTaglibdoSpringMVCpodetrazumproblema,queé
oacoplamentodacamadadevisualiza çãoaoframework.Nessecaso,a
soluçãoseriausarnãousaraTaglib.
Mascomoindicamosqualatributodeveserligadoao Model?Nesse
caso,usaríamosoatributo namedoinput:
<input type="text" name="email" />
Naprática,issoéexatamenteoqueaTaglibdoSpringMVCfaz.Ela
apenasgeraoHTMLcorrespondente.
189


## Página 200

8.14. Melhorandoacamadadevisualiza çãocomoTiles CasadoCódigo
8.14 M elhorando a camada de visualização com o
Tiles
Atéestemomentoo Spring Fórumaindaestáusandoo InternalViewResolver.Eleé
interessanteparacasosmuitobásicos,porémcomoestamoscriandoumaaplica ção
profissional,éimportantequemelhoremosestapartedosistematambém. Nesta
seçãocome çaremosporentendercomodefatofuncionaacamadadevisualiza ção
doSpringMVC.
Assimqueumarequisi çãoétratadaeprocessada,umarespostadeveserdevol-
vidaparaousuário.Oresponsávelporessatarefaéacamadade Visualização,onde
temosdiversasferramentasquepodemnosauxiliar,quesãogerenciadaspelo View
Resolver.Algunsdos Resolversmaispopularessão:
•InternalResourceViewResolver: encontraoarquivodevisualiza ção
(normalmenteJSP)no classpathdaaplicaçãoeorenderizacomoresposta;
•FreeMarkerViewResolver: visualizaçãobaseadanoprojetoFreeMarker
(http://freemarker.sourceforge.net),queéummotordetemplatesquesemos-
troubastantepopularnopassado;
•JasperReportsViewResolver:visualiza çãobaseadanogeradorderela-
tóriosJasperReports(http://jasperforge.org);
•TilesViewResolver: umadasopçõesmaispopularesadotadaemproje-
tosSpringMVC.Permiteacria çãodeinterfacesmaiselaboradasatravésde
templates.Veremosmaisarespeitodoseuusonestecapítulo;
•VelocityLayoutViewResolver: usaoApacheVelocity(http://velocity.
apache.org)comotecnologiadevisualiza ção;
•XsltViewResolver: umaopçãobastanteinteressanteparaprojetosque
usemtransformaçõesXSLTnasuacamadadevisualiza ção.
Estas são apenas algumas das opções que acompanham o Spring MVC e
há muitas outras escritas por desenvolvedores independentes disponibilizadas
para a comunidade. Caso seja de interesse do leitor, para implementar o seu
próprio View Resolver basta escrever uma classe que implemente a interface
org.springframework.web.servlet.ViewResolver.
190


## Página 201

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
O problema do código repetido nas telas
Umdosrequisitosdo Spring Fórumésuauniformidadevisual. Todasaspági-
nasdosistemadevempossuiralgunselementos,comoporexemploformuláriode
autenticação,logotipoerodapé. Aindamaisimportantequeisto,esteselementos
devemserimplementadosdetalmodoquenossaprodutividadesejagarantida,ou
seja,devemserreaproveitáveisparaqueevitemosassimosriscosdocopiarecolar.
Naimagemaseguirpodemosverumexemplodecomoestesblocosserepetemnas
páginasdosite:
Figura8.11:UniformidadevisualdoSpringFórum
TodapáginadoSpring Fórumpossuiamesmaestruturaorganizadaemtrêsgran-
desblocos: cabeçalho,aondeseencontraoformuláriodelogineologotipodosite,
conteúdoaondeéexpostootemadecadapáginavisitadae,finalmente, rodapé,para
informaçõesnãomenosimportantes,comocréditos,linksparacontatoetc. Nafi-
guraaseguirpodemosveraestruturaseguidapelaspáginas:
191


## Página 202

8.14. Melhorandoacamadadevisualiza çãocomoTiles CasadoCódigo
Figura8.12:Esquemavisualdenossaspáginas
Paraobteresteresultado,implementamosasse çõesreaproveitáveiscomotrechos
JSP,muitasvezeschamadosde templates(ou view helpers)queserãoinseridosno
corpoprincipaldapáginaconformeaordemexpostanaimagemacima. Usando
JSPconvencionalobtemosesteresultadocomJSTLadotandoumaestratégiasimilar
àexpostaaseguir:
<!DOCTYPE html>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<!-- Incluo o cabeçalho -->
<c:import url="templates/cabecalho.jsp"/>
<body>
<!-- O conteúdo entraria aqui -->
<c:import url="templates/rodape.jsp"/>
</body>
</html>
Osarquivos cabecalho.jspe rodape.jspsãooscomponentesaseremin-
seridosemnossapágina.Oproblemaéqueprecisaríamosrepetiroesquemaexposto
noexemploacimaemcadapáginaJSPdosistemaqueseguisseestelayout,oquealém
192


## Página 203

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
denãoserumatécnicaprodutiva,aindavêmcomoriscodoesquecimento.Pior:se
nofuturofornecessáriomodificarolayoutbásicodaaplica ção,teríamosdealterar
todososarquivosaondeaplicamosaformata çãooriginal.Nessecaso,precisamosde
umaferramentaquenosforne çaumasolu çãocompletaparafazero templatingda
aplicação.
Entraemcenao Apache Tiles (http://tiles.apache.org), queéummotorde
templatesbaseadoemcomposi ção( composite view)[3].Inicialmentedesenvolvido
comoumcomponentedo Jakarta Struts(http://struts.apache.org)porCédricDu-
moulin,comotemposetornoutãopopularqueacabousetransformandoemum
projetoindependenteadotadopordiversosframeworksdentreosquaisseencontra
o Spring MVC.
Ativando o Tiles em nosso projeto
PrecisamosadicionarcomodependênciaemnossoprojetooApacheTiles.Até
aversãocorrentedestelivro,oSpringaindanãooferecesuportenativoparaaver-
são3doframework. Sendoassim,teremosdenoscontentarporenquantocoma
últimoreleasedafamília2.x. Podemosmodificaro pom.xmlparaadicionaressa
novadependência:
<dependency>
<groupId>org.apache.tiles</groupId>
<artifactId>tiles-core</artifactId>
<version>2.2.2</version>
</dependency>
<dependency>
<groupId>org.apache.tiles</groupId>
<artifactId>tiles-jsp</artifactId>
<version>2.2.2</version>
</dependency>
EstasdependênciascorrespondemaocoredoTileseseusuporteaJSP.Claro,
istonãoéosuficiente,precisamostambémincluiro View Resolverespecíficoparao
Tilesemnossoarquivodeconfigura ção,talcomoexpostoaseguir:
<bean id="tilesViewResolver"
class="org.springframework.web.servlet.view.UrlBasedViewResolver">
<property name="viewClass"
value="org.springframework.web.servlet.view.tiles2.TilesView"/>
</bean>
193


## Página 204

8.14. Melhorandoacamadadevisualiza çãocomoTiles CasadoCódigo
Como pode ser visto, estamos usando um view resolver do tipo
UrlBasedViewResolver. Oatributo viewClassdefinequalaclasserespon-
sávelporrenderizarnossasrespostasdevoltaaousuáriofinal. Estaconfigura ção
não está completa: precisamos adicionar mais um bean em nosso sistema que
instruaoTilesarespeitodequaisarquivosdeconfigura çãodeverãoserlevadosem
consideraçãodurantesuaexecu ção.Entraemcenamaisumbean: TilesConfigurer,
cujadeclaraçãoéexpostaaseguir:
<bean class=
"org.springframework.web.servlet.view.tiles2.TilesConfigurer">
<property name="definitions">
<list>
<value>/tiles/tiles-config.xml</value>
</list>
</property>
</bean>
Observequenãoénecessáriodefinironomedobean:nosso ViewResolver
configuradoviaTilessemprebuscaráoutrobeandotipo TilesConfigurerpara
quefuncionecorretamente. Háumúnicoatributoqueprecisamosindicarneste
bean: definitions,querecebecomovalorumalistadestringsrepresentando
ocaminhoemnossoprojetoaondeasconfigura çõesdeverãoserencontradas.
Entendendo e configurando o Tiles
Aopensaremum“motordetemplatesbaseadoemcomposi ção”,lembre-seda-
quelesjogosdeencaixeinfantis.Assimcomoseuanálogofísico,eleécompostopor
umamolduraeaspe çasquenestaencaixamos. NojargãodoTiles,amoldurase
chama definição(definition),easpe çasserãoosatributosoutemplates.
194


## Página 205

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
Figura8.13:OTileséumjogodeencaixe,sóquepraweb
InfelizmenteoTilesprecisadeumarquivodeconfigura çãoparafuncionarque
éaondesãoincluídastodasasnossasdefini çõesdecomposi ção.Sendoassim,nosso
próximopassoécriá-lo.Ochamaremosde tiles-config.xmleestedeveráser
armazenadonodiretório /src/webapp/tilesdonossoprojeto. Seuconteúdo
devesersimilaraoexpostoaseguir:
<!DOCTYPE tiles-definitions PUBLIC
"-//Apache Software Foundation//DTD Tiles Configuration 2.0//EN"
"http://tiles.apache.org/dtds/tiles-config_2_0.dtd">
<tiles-definitions>
<!-- Definição básica -->
<definition name="main" template="/views/templates/main.jsp">
<put-attribute name="titulo" value="Spring Fórum"/>
<put-attribute name="cabecalho"
value="/views/templates/cabecalho.jsp"/>
<put-attribute name="rodape"
value="/views/templates/rodape.jsp"/>
</definition>
<definition name="index" extends="main" >
<put-attribute name="conteudo" value="/views/index.jsp"/>
</definition>
<definition name="signup" extends="main">
<put-attribute name="conteudo" value="/views/signup.jsp"/>
<put-attribute name="titulo" value="Bem vindo(a)!"/>
</definition>
195


## Página 206

8.14. Melhorandoacamadadevisualiza çãocomoTiles CasadoCódigo
<!-- restante omitido -->
</tiles-definitions>
Atag <definition>defineotemplateepossuiumúnicoparâmetroobriga-
tório: name,queoidentifica.A“moldura”usadaparaagruparoscomponentesdo
templateédefinidanoparâmetro template,cujovalordeveapontarparaoarquivo
JSPrelacionado.
Comopodeservistonaconfigura ção, oscomponentesnãonecessariamente
apontamparaarquivosJSP.Tambémpodemapontarpara String,comoporexem-
plooatributo titulo,usadoparadefinirotítulodapágina.
Nossaprimeiradefini ção, main,éabaseparatodasasoutrasdosistema. Ti-
lesnospermiteusaraheran çaqueestamosacostumadosaaplicaremnossasclasses.
Paratal,usamosoatributo extendsdatag <definition>tendocomovaloronome
dadefiniçãopai.Apartirdeentãobastaoprogramadordefinirquaisatributosde-
sejasobrescreveremcadadescendente(oqueéopcional)oumesmoadicionarnovos
casoachenecessário. OinteressantedoTileséque,conformepodeserobservado
emnossoexemplo,apartirdomomentoemqueescrevemosotemplatepai,ode-
senvolvedorsóprecisaráescreverotrechoJSPreferenteaoconteúdodecadapágina.
NossotemplateiniciallembrabastanteoqueescrevemoscomJSTLanterior-
mente,adiferen çaestánousodabibliotecadetagsoferecidapeloTiles:
<%@taglib prefix="tiles" uri="http://tiles.apache.org/tags-tiles" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
<link rel="stylesheet"
href="<c:url value="/recursos/stylesheets/estilo.css"/>" />
<!-- Inclusão do título pelo Tiles -->
<title>
<tiles:getAsString name="titulo" />
</title>
</head>
<body>
<!-- Inclusão do cabeçalho -->
<tiles:insertAttribute name="cabecalho"/>
196


## Página 207

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
<!-- Inclusão do conteúdo -->
<tiles:insertAttribute name="conteudo"/>
<!-- Inclusão do rodapé -->
<tiles:insertAttribute name="rodape"/>
</body>
</html>
AstagsdoTilessãomuitosimples. Sequisermosincluiratributosquenãose-
jamarquivos,bastaincluirumatagcomoporexemplo <tiles:getAsString/>
eparaincluirconteúdodinâmico,use <tiles:insertAttribute/>.Eistoter-
minanossocursobásicodeTiles,nossopróximopassoagoraseráconfigurá-loem
nossaaplicaçãoeentendercomoseu View Resolverfunciona.
Todonomelógicodeviewretornadopornossoscontroladorescorresponderáa
umadefiniçãopresentenosarquivosdeconfigura çãodoTiles.Éimportantemen-
cionarqueonomelógicodeumavisualiza çãopodecontercaminhos,comopor
exemplo usuario/show,oqueéinclusiveboaprática,poispossibilitaaequipede
desenvolvimentonofuturooptarporalgumoutrotipodecamadadevisualiza ção,
comoo InternalResourceViewResolver,quebuscaostemplatesapartirdo
caminhodefinidoporseusprefixoesufixo.
8.15 L idando com conteúdo estático
ComoTilesconfigurado,restaumimportantedetalhedanossacamadadevisuali-
zaçãoatratar:oconteúdoestático.Todaaplica çãowebprecisaenviaraseusclientes
imagens,JavaScript,CSSetc.Nocasodo Spring Fórum,vamosoptarporsalvartodos
estesrecursosnodiretório webapp/recursos.
EmumprimeiromomentopoderíamospensaremconfigurarumServletapenas
paraenviarestesrecursos,talvezatémesmoimplementandoalgummecanismode
cacheamentoHTTP.Istoédesnecessário,poisdesdeaversão3.0.4doSpringuma
novafuncionalidadefoiincluídanoframeworkjustamentepararesolveressasitua-
ção.
Bastaincluiratag <mvc:resources /> noarquivo spring-servlet.xmltalcomo
listadoaseguir:
<beans>
<mvc:resources mapping="/recursos/**"
location="/recursos/"
cache-period="120"/>
</beans>
197


## Página 208

8.15. Lidandocomconteúdoestático CasadoCódigo
O parâmetro mapping identifica o padrão de URL usado quando deseja-
mos obter um recurso estático. Em nosso caso optamos por um mapeamento
noqualtodaURLpossuaoprefixo recursos. Sendoassim,quandoobrow-
ser acessa um endereço como por exemplo http://localhost:8080/spring-forum/
recursos/css/main.css,seráenviadoparaeleoarquivo main.css,presentenodire-
tório webapp/recursos/css.Osdoisasteriscosincluídosnofinaldovalorindica
qualquersubcaminhoapósoprefixo.
Paradefinirqualolocaldearmazenamentodosrecursosestáticosusa-seoatri-
buto location. Porpadrão,esteapontarásempreparaalgumdiretóriopresente
naraizdaaplica ção.Éinteressanteobservarquetambémépossíveldefinircomoca-
minhoalgumalocaliza çãono classpathoumesmoumdiretóriopresentenosistema
dearquivos:
<!-- A partir de um diretório -->
<mvc:resources mapping="/recursos/**"
location="file:/arquivos"/>
<!-- A partir do classpath -->
<mvc:resources mapping="/recursos/**"
location:"classpath:springForum.imagens"/>
Finalmente,temosoúnicoparâmetroopcionaldestatag-enemporistomenos
importante-queéo cache-period.Esterecebecomovalorotempoemsegun-
dosdecacheamentodorecursoestáticoenviado. SeráincluídonarespostaHTTP
enviadaaobrowserumcabe çalhodotipo Expirescujovalorseráahoracorrente
acrescidadonúmerodesegundosquedefinimosnoatributo.
198


## Página 209

CasadoCódigo Capítulo8. DesenvolvaaplicaçõeswebcomSpringMVC
Cache HTTP com o cabeçalho Expires
Umdosrequisitosnãofuncionaismaisimportantesdequalquerapli-
caçãoéperformance. Nocasodeaplica çõesweb,umgargalobastante
conhecidoéatransmissãodeconteúdoestático. Osnavegadoresten-
tamminimizaresteproblemacacheandooresultadodassolicita ções,
evitandoassimaocorrênciadesolicita çõesrepetidasaummesmore-
curso. Éumaestratégiainteressanteequepodeficaraindamelhorse
fornecermosumadicaaobrowsersobrequandoaquelerecursoestará
desatualizado.
OprotocoloHTTPnospermitefazeristocomocabe çalho Expires.
Nocaso,esteforneceumadatadeexpira çãoparaorecursobaixado,pos-
sibilitandoaonavegadorsórepetiraconsultacasoestajáseencontreno
passado.Atítulodecuriosidade,estecabe çalhosegueaseguintesintaxe:
"Expires" ":" HTTP-date
Umvalorválidoparaaexpira çãodestelivroseria,porexemplo:
Expires: Thu, 01 Dec 2024 16:00:00 GMT
Comisso,onavegadorpediriaessainforma çãonovamenteparaoser-
vidorapenasem1deDezembrode2024. Antesdisso,usariaoquejá
estavacacheadoefoibuscadonaprimeirarequisi ção.
OusodestatagtambémfacilitamuitoaescritadenossosarquivosJSP.Aseguir
podemosverumpequenotrechodeumarquivoJSP,noqualdeclaramosoacessoa
algunsarquivosCSSdonossoprojeto.
<head>
<link rel="stylesheet"
href="recursos/stylesheets/foundation.min.css"/>
<link rel="stylesheet" href="recursos/stylesheets/main.css"/>
</head>
8.16 A inda há mais de Spring MVC por vir
VimosmuitodofuncionamentodoSpringMVCecomoconhecimentoquetemos,já
conseguimoscriarqualqueraplica çãoweb.Noentanto,nomundoreal,gostaríamos
199


## Página 210

8.16. AindahámaisdeSpringMVCporvir CasadoCódigo
defacilitarmuitasdastarefasquetemosaocriarumaaplica ção,porexemplofacilitar
avalida çãodosdados,poderfazeruploaddearquivosdeformadescomplicadae
outrosrecursosinteressantes. Nopróximocapítulo,vamosvercomopoderusar
outrasbibliotecasparaaumentaropoderdoSpringMVCevercomoelepodenos
ajudarnessaintegra ção.
200


## Página 211

Capítulo9
Açõesrecorrentescomo
SpringMVC
Hámuitotrabalhorepetitivoaserfeitoquandodesenvolvemosaplica çõesweb.Va-
lidaçãoéumcasobemclássico. Qualdesenvolvedornuncasepegouescrevendo
diversos ifaninhadoserepetidos?Uploaddearquivostambémpodeserconside-
radoumadessastarefaschatasquetemosquelidarquandodesenvolvemosaplica ção.
Ficarmanipulandobytesearquivoséalgobastantetrabalhoso.Seráquenãoháuma
maneiradedeixartudoissomaisfácil?
Nessecapítulovamosestudaraintegra çãodoSpringMVCcomdiferentesbiblio-
tecasevercomoelaspodematuaremconjuntoparanosajudaracriarumaaplica ção
webricaedefácildesenvolvimentoemanuten ção.


## Página 212

9.1. Façaavalida çãodeformulárioscomoHibernateValidator CasadoCódigo
9.1 F aça a v alidação de formulários com o Hiber-
nate Validator
Umaspectofundamentaldodesenvolvimentodequalqueraplica çãodizrespeitoà
validaçãodosdadosdeentrada.Semalplanejada,avalida çãodeformuláriospode
semostrarumadastarefasmaistediosasetrabalhosasduranteoprocessodedesen-
volvimento.
GraçasàequipededesenvolvimentodoSpring,nãoprecisamosnospreocupar
comisto,poisdevidoàpróprianaturezadoframeworkdeseintegraraoutrastecno-
logias,esteoferecesuporteàJSR-303( Bean Validation),quenospermiteadicionar
regrasdevalida çãoaosnossosformuláriosouclassesdedomínioatravésdeanota-
çõesdeumaformabastanteprodutiva.
Configure as dependências necessárias
AimplementaçãodereferênciaparaaJSR-303éoprojeto Hibernate Validator.
Aocontráriodoquepossapareceraalguns,trata-sedeumprojetoindependente
doORM( Object Relational Mapping)demesmonome,podendoserusadosema
necessidadedeincluí-loentreasdependênciasdoprojeto.Bastaincluiro Hibernate
Validatornalistadedependênciasnoseu pom.xml:
<dependency>
<groupId>org.hibernate</groupId>
<artifactId>hibernate-validator</artifactId>
<version>4.2.0.Final</version>
</dependency>
Definindo as validações
UsaroHibernateValidatornocontextodo Spring MVCérazoavelmentesimples.
Bastaanotarosatributosdaclassenaqualqueremosaplicarvalida çõestalcomo
fizemoscomaclasse Usuariolistadaaseguir:
public class Usuario {
@Size(max=128) @NotNull @NotEmpty
private String nome;
@Email(message="Isto não é um e-mail válido") @NotNull @NotEmpty
private String email;
202


## Página 213

CasadoCódigo Capítulo9. AçõesrecorrentescomoSpringMVC
@NotNull
private Date dataCadastro = new Date();
@NotNull @NotEmpty
@Size(min=8, max=32, message="Login muito curto ou muito longo")
private String login;
// getters e setters
}
Onomedasanota çõesjánosdizbastantearespeitodotipodevalida çãoaser
aplicadoemnossaclasse.Dasvalida çõeslistadasacima,aúnicaquenãofazpartedo
conjuntopadrãodaJSR-303é @Email,pertencenteao Hibernate Validator,usada
paraverificarseovalorcorrespondeaumendere çodee-mailválido.
Épossíveldefinirqualamensagemdeerroaserexibidaaousuárionocasode
umavalidaçãofalha,atravésdoparâmetro value,presenteemtodasasanota ções
compatíveiscomaJSR-303.Aseguircomoreferênciarápidasegueumalistagemdas
anotaçõesdevalida çãomaiscomumenteusadaspelosdesenvolvedores:
•@NotNull:garantequeoatributoanotadonãopossuavalornulo.
•@NotEmpty:aplicávelacole çõesoustrings,verificaseotextodigitadoestá
embrancoousealistaestávazia.
•@Size:usadaparagarantirqueotamanhodeumtextoestejadentrodospa-
râmetroslimitadores minou max.Importantesalientarquenãoénecessária
apresençadosdoisparâmetros,massimaomenosum.
•@Email:específicado Hibernate MVC,éusadaparagarantirqueovalordo
atributosejaumendere çodee-mailválido formalmente.
•@Pattern: recebecomoparâmetroobrigatório regexprepresentandouma
expressãoregularcontraaqualserávalidadooatributoanotado.Talvezseja
aanotaçãomaispoderosadaJSR-303devidoàgrandeflexibilidadeoferecida
pelasexpressõesregulares.
V alidação do lado servidor
Paraentendercomoavalida çãodoladoservidoréfeita,vamosmodificaraa ção
executarRegistro.Sualógicadefuncionamentoésimples:primeiroéverificado
203


## Página 214

9.1. Façaavalida çãodeformulárioscomoHibernateValidator CasadoCódigo
seháalgumerrodevalida ção.Casoexistam,seráfeitooredirecionamentoparao
formuláriodecadastro,aondeosmesmosserãoexpostosparaousuário:
@RequestMapping(value="/executarRegistro", method=RequestMethod.POST)
public String executarRegistro(@Valid Usuario usuario,
BindingResult bindingResult,
HttpSession sessao) {
if (bindingResult.hasErrors()) {
Map<String, Object> model = new HashMap<String, Object>();
model.put("usuario", usuario);
return registro(model);
}
getDaoUsuario().persistir(usuario);
sessao.setAttribute("usuario", usuario);
return "redirect:/";
}
Hádetalhesimportantesnocorpodestaa ção,acome çarpelapresen çadaano-
tação @Validaplicadasobreoparâmetro usuario,queinstruio Spring MVC
aexecutarostestesdevalida çãosobreoobjetoanotadonomomentodeexecu ção
daligaçãodosparâmetros.Encontrandoproblemas,estessãoarmazenadosemum
objetodotipo org.springframework.validation.BindingResult,queéa
interfaceinternadoframeworkresponsávelporrepresentaroresultadodaexecu ção
doprocessodeliga ção( binding).
Éimportantemencionarquenemsempreavalida çãoterminacomaexecu ção
dafun ção hasErrors()de BindingResult. Estainterfacetambémnosper-
miteiterarsobreoserrosencontrados,detalformaquepossamosaplicaralguma
regradenegócioemcimadavalida ção.Porexemplo:imaginequetenhamoscon-
vencionadoque,casoo hostdoe-mailnãotenhasidofornecidoovalorpadrãoseja
@gmail.com.Poderíamostirarproveitode BindingResult:
List<FieldError> erros_email = bindingResult.getFieldErrors("email");
for (FieldError erro : erros_email) {
if (erro.getCode().equals("Email") &&
contemEmail(usuario.getEmail())) {
// aplico a convenção do sistema
usuario.setEmail(usuario.getEmail() + "@gmail.com");
204


## Página 215

CasadoCódigo Capítulo9. AçõesrecorrentescomoSpringMVC
}
}
Aclasse FieldErrorrepresentaumerroencontradoduranteavalida çãoem
algumcampodaclasseavaliada.Estapossuiumatributochamado code,cujova-
lornormalmentecorrespondeaonomedaanota çãodevalida ção.Nocódigoante-
rior,tudooquefizemosfoiiteraremcimadacole çãodeerrosassociadosaocampo
emailembuscadavalida ção Email. Encontrando-a,verificamosseousuário
haviadigitadoalgumvaloreemcasopositivo,simplesmenteadicionamososufixo
@gmail.comaovaloratéentãoincorreto.
Exiba os erros de validação
Encontrarerrosdevalida çãodoladoservidordenadavalesenãofornecermos
aonossousuárioapossibilidadedecorrigi-los. Parafazeressaexibi ção,podemos
usaramesmabibliotecadetagsutilizadaparageraroformulário,equejávimos
anteriormente.
Para expor as mensagens de erro de volta ao usuário usamos a tag
<sf:errors/>,obtendoresultadosimilaraoexpostonaimagemaseguir:
Figura9.1:Expondomensagensdevalida ção
Oatributo pathfiltraoserrosporcampo. Jáoatributo cssClassdefineo
nomedoseletorCSSquedefineaformata çãoaservisualizadapelousuário.Podemos
verumexemplodeseuusonocódigoaseguir,extraídodoformuláriodecadastro
apresentadoacima:
205


## Página 216

9.2. Envieseusavataresparaoservidorcomuploaddearquivos CasadoCódigo
<%@taglib prefix="sf" uri="http://www.springframework.org/tags/form"%>
...
<sf:form modelAttribute="usuario" action="executarRegistro">
<label for="nome">Nome:<sf:errors path="nome" cssClass="erro"/>
</label>
<sf:input path="nome"/>
<!-- Restante omitido, pois é basicamente o
mesmo código aplicado a outros campos -->
</sf:form>
Oúnicoatributoobrigatórioé path,quequandoomitido,simplesmentenão
renderizarásaídaalgumaparaousuário.Abaixosegueumalistacomosoutrosatri-
butosqueodesenvolvedorpodetirarproveitoemseusprojetos:
•element:definequalelementoHTMLqueiráenvolvercadamensagemde
erro;
•cssStyle: permiteaodesenvolvedorincluirestiloCSScustomizadopara
umalocalizaçãoespecífica;
•delimiter:quetextoseráusadoparasepararasmensagensdeerroexpostas.
Seuvalorpadrãoé<BR/>.
9.2 E nvie seus av atares para o servidor com upload
de arquivos
Faremosagoraaevolu çãofinaldonossoformulárioderegistroincluindoapossi-
bilidadedefazerouploaddeavatares,oquepossibilitaráaosmembrosdo Spring
Fórumseexpressaremvisualmenteatravésdestasimagens.Atéomomentofizemos
o bindingapenasdeclassessimplescomo Usuario,porémaolidarcomuploadde
arquivosestamostrabalhandocomumacriaturabastantediferente.
Configurando o projeto
Infelizmenteo Spring MVCnãovemprontoparalidarcomuploaddearquivos,
porémaconfiguraçãodoprojetoparatalébastantesimples,compostaporapenas
doispassos:inclusãodenovasdependênciaseadefini çãodobeanresponsávelpor
lidarcomestetipodeopera ção,o MultipartResolver.
206


## Página 217

CasadoCódigo Capítulo9. AçõesrecorrentescomoSpringMVC
Duas dependências precisam ser incluídas em nosso projeto:Commons IO
e Commons File Upload, ambaspertencentesaoprojeto Apache Commons (http:
//commons.apache.org).Comisso,podemosadicionarasduasno pom.xml:
<dependency>
<groupId>commons-fileupload</groupId>
<artifactId>commons-fileupload</artifactId>
<version>1.2.2</version>
</dependency>
<dependency>
<groupId>commons-io</groupId>
<artifactId>commons-io</artifactId>
<version>2.1</version>
</dependency>
O passo final para habilitarmos o upload de arqui-
vos em nosso projeto é a declara ção de um bean do tipo
org.springframework.web.multipart.commons.CommonsMultipartResolver,
responsável por interceptar requisições de formulário com enctype do tipo
multipart/form-data. Atençãoespecialdeveserdadaaonomedobean:este
obrigatoriamentedeveteronome multipartResolver,poiso Dispatcher Servlet
buscaráumbeancomestenomeparalidarcomuploaddearquivos.
<bean id="multipartResolver" class=
"org.springframework.web.multipart.commons.CommonsMultipartResolver">
<property name="maxUploadSize" value="1048576"/>
</bean>
Aúnicapropriedadedefinidanobeané maxUploadSize,querecebeumnú-
merointeirocomovalorrepresentandootamanhomáximoembytesqueoprojeto
permitiráoupload.Adefini çãodestapropriedadedopontodevistadeseguran çaé
altamenterecomendada,poispordefaultseuvaloré -1,indicandoapossibilidade
derecebermosarquivosdequalquertamanho.
A atualização do formulário
Asmodificaçõesqueprecisamosfazeraoformuláriosãoexatamenteasmesmas
quefaríamosaumformulárioHTMLconvencional: apenasinclusãodoatributo
enctypeedeumcampodotipo file.Importanteobservarque,aocontráriodos
demaistiposdecampodeentradaqueforamexpostosnestecapítulo,nãoépossível
207


## Página 218

9.2. Envieseusavataresparaoservidorcomuploaddearquivos CasadoCódigo
fazero bindingcomcamposdotipo file.Aseguirpodemosverosúnicostrechos
alteradosemsuamarca çãoeoresultadofinalapósestasmodifica ções:
<sf:form modelAttribute="usuario"
action="executarRegistro" enctype="multipart/form-data">
<!-- Restante oculto -->
<label for="avatar">Avatar:</label>
<input type="file" name="avatar"/>
<!-- Restante oculto -->
</sf:form>
Figura9.2:Aversãofinaldonossoformuláriodecadastro
Configure o controlador
Denadaadiantaalterarasconfigura çõesdoprojetoeevoluiroformuláriodeca-
dastroseaaction executarRegistro,responsávelpeloprocessamentodosparâ-
metrossubmetidospeloformulárionãoformelhoradatambém.Aseguirpodemos
vercomoficouaversãofinaldestemétodo:
208


## Página 219

CasadoCódigo Capítulo9. AçõesrecorrentescomoSpringMVC
@RequestMapping(value="/executarRegistro", method=RequestMethod.POST)
public String executarRegistro(@Valid Usuario usuario,
BindingResult bindingResult, HttpSession sessao,
@RequestParam(value="avatar", required=false) MultipartFile avatar){
if (bindingResult.hasErrors()) {
Map<String, Object> model = new HashMap<String, Object>();
model.put("usuario", usuario);
return registro(model);
}
getDaoUsuario().persistir(usuario);
if (! avatar.isEmpty()) {
processarAvatar(usuario, avatar);
}
sessao.setAttribute("usuario", usuario);
return "redirect:/";
}
A modificação mais importante é a inclusão do parâmetroavatar, do tipo
org.springframework.web.multipart.MultipartFile, responsável por
representaroarquivorecebidopelocontroladornarequisi ção.Comopodemosver
naimplementa çãodestaaction,oúnicométododestaclassequenosinteressaé
isEmpty(),queretorna truecasonãotenhasidotransmitidojuntocomare-
quisiçãoumarquivoanexado.
Outrométodofoiincluídoemnossocontroladorapenasparalidarcomoar-
quivorecebido. Trata-sede processarAvatar,cujaimplementa çãoresumida
podeservistaaseguir:
private void processarAvatar(Usuario usuario, MultipartFile avatar) {
byte[] conteudo = avatar.getBytes();
persistirConteudo(usuario, conteudo);
}
Paraobteroconteúdodoarquivorecebido,executa-seométodo getBytesdo
objeto MultipartFile,queretornaum byte[],queéoconteúdorecebidoa
partirdasubmissãodoformuláriodecadastro.
209


## Página 220

9.3. Definaocorpodaresposta CasadoCódigo
9.3 D efina o corpo da resposta
Atéestemomento,nossasa çõesretornaramouonomedavisualiza çãoaserren-
derizadaouumobjetodotipo ModelAndView. Comoumaactionretornariao
conteúdodosarquivosqueo Spring Fórumagoraestáhabilitadoareceber?
Antesderesponderaestapergunta,nossoprimeiropassoseráevoluirapágina
devisualizaçãodedetalhesdousuário,paraquefiquesimilaràimagemaseguir:
Figura9.3:Expondooavatardosusuários
Tudooqueprecisamosfazerédefiniroatributo srcdatag <img/>apontando
paraaa çãoresponsávelporretornarum array de bytesrepresentandooconteúdodo
avatar,talcomofizemosnotrechoaseguir:
<img class="avatar"
src='<c:url value="/usuario/avatar/${usuario.login}"/> '/>
Usamosatag <c:url>doJSTLparagarantirqueaURLalvoestejasemprede
acordocomocontextodaaplica ção.Cabeentãooúltimopontodestasessãoqueéa
nossaaction,queencontra-seimplementadanaclasse UsuarioController,cujo
códigofontepodemosverlistadoaseguir:
210


## Página 221

CasadoCódigo Capítulo9. AçõesrecorrentescomoSpringMVC
@RequestMapping("/usuario/avatar/{login}")
@ResponseBody
public byte[] avatar(@PathVariable("login") String login) {
/*
Obtém um array de bytes representando o
avatar relacionado ao login
*/
return obterConteudo(login);
}
Aprimeiranovidadequepodemosvernaimplementa çãodaaction,dizrespeito
aovalorpassadoàanota ção @RequestMapping. Trata-sedavariável loginna
URL,oquenospermiterecebermapearURLscomoasabaixoparaestaaction:
http://localhost:8080/spring-forum/usuario/avatar/kicolobo
http://localhost:8080/spring-forum/usuario/avatar/mccarty
Outropontodedestaqueéainclusãodaanota ção @ResponseBody. Repare
quenossaactionretornaum array de bytes enãouma Stringouumobjeto
ModelAndViewcomofizemosanteriormente. Apresen çadestaanota çãoinstrui
o Spring MVCaenviarovalorderetornodiretamenteaonavegadordousuário.
9.4 F aça requisições assíncronas com AJAX
Atualmentepresentenacaixadeferramentasdetododesenvolvedorweb,éimpor-
tantecompreendermoscomousarAjaxno Spring MVC.
Infelizmente,naversãoatualdoframeworkaindanãoháumabibliotecadetags
quefaciliteavidadodesenvolvedornaescritadacamadadevisualiza ção,porémesta
ausêncianãodeveservistacomoumagravelimita çãodoframeworkdadoadifusão
debibliotecasJavaScriptcomojQueryouDojo,quesupremaesmagadoramaioria
dasnecessidadedosprogramadoresnestequesito.
Paraosnãoiniciados,AJAXéumacrônimopara Asynchronous Javascript and
XML.AtécnicafoidocumentadapelaprimeiravezporJesseJamesGarrett,noano
de2005emseublog[6]eseconsagrouaoseraplicadanaimplementa çãodoGoogle
Maps.Nãoéexagerodizerqueatécnicasetornou língua francaentreosdesenvol-
vedoresweb.
Osfundamentosportrásdatécnicavãoalémdoobjetivodestelivro,porémo
leitoraindanãofamiliarizadocomoconceitopodeteracessoamaterialdemelhor
211


## Página 222

9.4. FaçarequisiçõesassíncronascomAJAX CasadoCódigo
qualidadesobreoassuntonopostdeGarrett[6]acimacitadoouemlivrosintei-
ramentededicadosaoassuntocomoporexemplo Use a Cabeça - AJAX,deBrett
McLaughlin[12].
Resumidamente,AJAXéusadonodesenvolvimentodeaplica çõesparadoisob-
jetivos:renderizartrechosespecíficosdenossaspáginasounaobten çãodeinforma-
çõesqueserãoprocessadasdoladocliente,oumesmonamisturadestesdoisusos.
Renderização local
Atécnicaderenderizaçãolocal(ou in loco)consistenaexecu çãodeumaconsulta
assíncronaaoservidor,cujarespostaserárenderizadaemalgumlocalpré-definido
dapágina,porexemplodentrodeumatag <div>comidentificadorespecífico.
No Spring Fórumestatécnicafoiaplicadanapáginaqueexibeosdetalhesdo
usuário.Quandoolink Expor postséclicado,umarequisi çãoassíncrona,disparada
atravésdo jQuery,éfeitaaoservidor. Esteexecutaaactionrelacionadacomose
fosseumarequisi çãoconvencionaleretornaaonavegadorumtrechoemHTML
quesimplesmenteéexpostonadivqueanteriormenteestavavazia,conformepode
servistonaimagemaseguirqueesquematizaseufuncionamento.
Figura9.4:Renderiza çãoinloco
Doladoservidor,aactionéexatamentecomotodasasoutrasquevimosanteri-
ormente.Estaapenasbuscatodosostópicoscriadospelousuário,cujologinépas-
sadocomoparâmetro.Encontra-seimplementadanaclasse UsuarioController
conformepodeservistonocódigoaseguir:
@RequestMapping("/usuario/posts/{login}")
public String topicosUsuario(@PathVariable("login") String login,
Map<String, Object> model) {
212


## Página 223

CasadoCódigo Capítulo9. AçõesrecorrentescomoSpringMVC
model.put("topicos",
getDaoTopico().
getTopicosPorAutor(getDaoUsuario().getUsuario(login)));
return "usuario/posts";
}
Seoleitorbemselembra,no Spring FóruméusadooTilescomocamadade
visualização.ComonossoobjetivoéapenasrenderizarumtrechoHTML,adefini ção
detemplateincluídanoarquivo tiles-config.xmlpodeservistaaseguir.Não
hácomponentesaseremincluídosemnossotemplate,apenasestejáénecessário
paraoqueprecisamos.
<definition name="usuario/posts"
template="/views/usuario/postsUsuario.jsp"/>
EotrechoHTMLinseridoemnossapáginatambémnãopoeriasermaissimples,
conformeconferimosnotrechoabaixo:
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<table>
<thead>
<th>Assunto</th>
<th>T&iacute;tulo</th>
</thead>
<tbody>
<c:forEach items="${topicos}" var="post">
<tr>
<td>${post.assunto.nome}</td>
<td>${post.titulo}</td>
</tr>
</c:forEach>
</tbody>
</table>
Retorne o JSON
AoutraformadeaplicarmosAjaxconsisteemenviarconteúdonoformatoJSON
paraousuário,oqueéassustadoramentesimplescom Spring MVC.Nativamente,o
frameworknãooferecesuporteaesteformato,sendoassimnossoprimeiropasso
consistiráemincluirabiblioteca Codehaus Jacksonaoclasspathdenossoprojeto.
Bastaincluiraconfigura çãoabaixonalistadedependênciasdoarquivo pom.xml
doprojeto.
213


## Página 224

9.5. Concluindocomumasurpresa CasadoCódigo
<dependency>
<groupId>org.codehaus.jackson</groupId>
<artifactId>jackson-mapper-asl</artifactId>
<version>1.7.1</version>
</dependency>
ParaexemplificarcomoretornarJSONaousuário,amesmaactionexpostano
exemploanteriorfoireescrita,conformepodeservistonocódigoaseguir:
@RequestMapping("/usuario/postsJSON/{login}")
@ResponseBody
public List<Topico>
topicosUsuarioJson(@PathVariable("login") String login) {
Usuario usuario = getDaoUsuario().getUsuario(login);
return getDaoTopico().getTopicosPorAutor(usuario);
}
Nãohánovidadesnocódigoacima. Incluindoaanota ção @ResponseBody,
umavezquenossaactionsejaexecutada,oresultadoseráautomaticamenteconver-
tidoparaJSONpelo Jackson.Aoacessaraurlhttp://localhost:8080/spring-forum/
usuario/postsJSON/kicoloboaseguintesaídaobtidaéexpostaabaixo:
[{"titulo":"Spring MVC", "assunto":{"nome":"Web"}},
{"titulo":"Como eu configuro o Spring?", "assunto":{"nome":"IoC"}}]
9.5 C oncluindo com uma surpresa
Aolongodestecapítulo,conhecemosasolu çãooferecidapela SpringSourceparao
desenvolvimentodeaplica çõesweb.Comopodeservisto,trata-sedeumasolu ção
incrivelmenteflexível,quepossibilitaaoprogramadorcustomizarcadaaspectodo
seufuncionamento.Finalizadoestecapítulooleitortalvezsesintaassustadocoma
quantidadedeconfigura çõesqueprecisamosalterarduranteestecapítuloconforme
novosrecursoseramapresentados.
Acontecequeosusuáriosdo SpringSource T ool Suitenãoprecisamdefinirestas
configuraçõesmanualmente.Narealidade,aIDEforneceapossibilidadedecriarum
projetobaseadoem Spring MVCjápré-configurado.Paratal,bastaacessaromenu
File > New > Spring T emplate Project. Seráexpostaajanelaaseguir,aondetudoo
queousuáriodevefazeréselecionaraop ção Spring MVC Projectevoilà,oprojeto
estápré-configuradoeprontoparauso.
214


## Página 225

CasadoCódigo Capítulo9. AçõesrecorrentescomoSpringMVC
Figura9.5:SpringSourceToolSuite
Umpontoimportanteasermencionadoarespeitodoaparenteexcessodecon-
figuraçõeséofatodestasatividades,mesmocomoauxíliodaIDE,sãoexecutadas
normalmenteapenasnomomentodecria çãodoprojeto.Apartirdestemomento,o
fluxobásicoconsistirábasicamenteapenasemimplementaroscontroladoresetem-
platesdevisualiza çãorelacionados,associadosàstécnicasapresentadasnocapítulo
4destelivrofornecemàequipededesenvolvimentoumframeworkdealtíssimapro-
dutividade,comeficáciacomprovadaeminúmerosprojetospelomundo[15].
Ahistóriado Spring MVCnãoterminaporagora.Lacunas,comoporexemploa
ausênciadebibliotecasdetagquefacilitemavidadodesenvolvedorquepreciselidar
comAJAXestãoemdesenvolvimento.Alémdisto,deformabastantediscretao MVC
viveumavidaduplasobaformado Grails,umframeworkparadesenvolvimentode
aplicaçõeswebbaseadonalinguagemGroovytendocomobaseo MVC,quetem
215


## Página 226

9.5. Concluindocomumasurpresa CasadoCódigo
semostradoumadasformasmaisprodutivasdesecriaraplica çõeswebdentroda
plataformaJavaEE.
Masjáfalamosdemaissobreo MVC.Nospróximoscapítulosnossofocoserá
nosganhosqueoframeworkoferecenacamadadenegócios.
216


## Página 227

Capítulo10
Gerenciandotransações
Umdosrequisitosfundamentaisportrásdetodaaplica çãoégarantiraconsistência
dasnossasbasesdedados.NocapítuloanterioraprendemoscomooSpringfacilitaa
escritadacamadadepersistência.Comistoresolvemosboapartedosnossosproble-
mas,porémaindanãogarantimosaintegridadedosnossosdados.Muitossistemas
atuaispossuemumaltoníveldeconcorrênciaeprocessamentoparalelo,enãohá
comogarantirestanecessidadesemoauxíliodocontextotransacionalqueoSpring
praticamentetrivializa.
10.1 E ntendendo as transações
Agrossomodo,umatransa çãorepresentaumconjuntodeopera çõesnoqualou
todassãoexecutadascomsucessoounenhumaé.Comoexemplovamosimaginar
quenoprojeto Spring Fórumsejaimplementadaumaloja. Semprequeumcliente
comprarumproduto,oseguinteconjuntodeopera çõeséexecutado:
1) Oestoqueédecrementado;


## Página 228

10.1. Entendendoastransações CasadoCódigo
2) Éfeitoodébitonocartãodocliente;
3) Ume-maildeconfirmaçãodecompraéenviado;
4) Éenviadaumasolicita çãodeenvioparaatransportadora.
Agoraimaginequeosegundopassoapresentealgumproblemaenãosejafeito
odébitonocartãodocliente:teremosdecrementadonossoestoque,enviadoume-
maildeconfirma çãodecompraeoprodutotalvezjáestejainclusiveacaminho.Este
conjuntodeatividadespossuiumnomedentrodojargãotransacional: unidade de
trabalho(unit of work).
Agrossomodo,oqueumatransa çãorealmentefazétransformarumconjunto
detarefasemumaunidadedetrabalho,unificando-aseassimgarantindoqueou
todasdãocertoouque,emcasodeerronossabasededadosvolteaumestadocon-
sistente.Voltandoaoexemploanterior,casoumerroocorressenomomentoemque
odébitonocartãodoclientefosseacontecer,oestoquevoltariaparaoseuestadoan-
terioreospassosseguintessimplesmentenãoseriamexecutados,garantindoassim
aintegridadedonossosistema.
Transações são ACIDas
Todatransaçãodevesatisfazerquatrocondi çõesqueformamoacrônimo ACID:
•Atomicidade:oconjuntodeopera çõesqueformamaunidadedetrabalhode-
vemservistascomoumaúnicaopera çãoartificialmenteindivisível.Outodos
ospassossãoexecutadoscomsucessoounadaéfeito;
•Consistência: seatransa çãoforexecutadacomêxito,oestadofinalda
nossabasededadosdevesempreestaremumestadoconsistente.Aliás,esta
éarazãopelaqualtransa çõesexistem,certo?
•Isolamento:dificilmenteencontramossistemasmonousuárioatualmente.
Éincrementalmentecomum-narealidade,anorma-aocorrênciademaisde
umatransaçãosimultâneasendoexecutada.Énecessárioqueaexecu çãode
umatransaçãosejaindependentedasdemais,garantindoassimaexecu çãode
códigoconcorrenteeaintegridadedosdadosaofinaldoseuprocessamento.
•Durabilidade: finalizadaatransação,osdadosdevemestarpermanente-
mentepersistidosnabasededados.Paramelhorentenderesteconceito,éin-
teressanteobservarquediversosmecanismostransacionaismantémoestado
218


## Página 229

CasadoCódigo Capítulo10. Gerenciandotransações
dabasededadosduranteaexecu çãodeumatransa çãoemmemória.Apósa
suaexecução,estesobrigatoriamentedevemestarsalvosemummecanismo
dearmazenagemdurável,comoporexemploodiscorígido,fitaetc.
Éimportanteobservarquequandofalamosdestesquatroatributosestamosnos
referindonamaiorpartedasvezesabasesdedadosrelacionais.Comosurgimento
debancosdedadosNoSQL,asitua çãotemsemostradoumpoucodiferente,pois
estescostumamoferecersuporteincompletoaoACID.Éfundamentalqueoleitor
leveesteaspectoemconsidera çãocasoestejaatrabalharcomestetipodetecnologia.
10.2 A s políticas transacionais
OSpringoferecesuporteadoistiposdetransa ções:programáticasoudeclarativas.
Nocasodastransa çõesprogramáticas,estánasmãosdodesenvolvedoraresponsa-
bilidadededefiniraondecome çaeterminaumaunidadedetrabalho.Jánocasodas
transaçõesdeclarativas,tenhaemmentequeestamosnarealidadedefinindoregras
queditarãoaocontainerquaisoslimitesquedevemseraplicadosacadaunidadede
trabalho.
Osuporteatransa çõesdeclarativasdoSpringtemcomoinspira çãoo CMT(Con-
tainerManagementTransactions)daplataformaJavaEE.Éinteressanteobservarque
atéoaparecimentodoSpringnãohaviacomotirarproveitodesterecursosemapre-
sençadeumservidorpesadodeaplica ções.Comoveremos,oSpringsuperaoCMT
aopermitirumapersonaliza çãodemaiorgranularidadeatravésdapossibilidadede
podermosdefiniratravésdaspolíticastransacionaisqualocomportamentodasuni-
dadesdetrabalho.
NaimplementaçãodoSpringdastransa çõesdeclarativashácincopolíticasque
podemsermanipuladaspeloprogramador.
Propagação
Apolíticadepropaga çãodefineoslimitesdeumatransa ção.Pensecomoares-
postaàseguintepergunta:“dadoqueummétodoiniciaumatransa çãoeesteevoca
ouéchamadoporoutros,qualapropaga çãodatransa çãoporelecriada?”.OSpring
nosoferecealgumasrespostasaestaperguntasobaformadeconstantesdefinidasna
interface org.springframework.transaction.TransactionDefinition
quepodemosverlistadasaseguir:
•PROPAGATION_MANDATORY:ométodosópodeserexecutadodentrodeuma
219


## Página 230

10.2. Aspolíticastransacionais CasadoCódigo
transação.Seumatransa çãonãoestiveremexecu ção,quandoométodofor
invocadoumaexce çãoserádisparada;
•PROPAGATION_NESTED:casoométodosejaexecutadoapartirdeumatran-
sação,umanovaserácriadaparaestemétodoeseucommitourollbacknão
afetaráaqueoencapsulou.Casosejainvocadosemqueumatransa çãoexista,
umanovaserácriadasomenteparasi;
•PROPAGATION_NEVER:ométodojamaisdeveserexecutadodentrodeuma
transação.Casoistoocorra,umaexce çãoserádisparada;
•PROPAGATION_NOT_SUPPORTED:ométodonãodeveserexecutadodentro
deumatransa ção. Casosejachamadoapartirdeumatransa ção,estaserá
paralisadaatéquesuaexecu çãotermineparaemseguidavoltaràsuaexecu ção
normal;
•PROPAGATION_REQUIRED:ométodosópodeserexecutadoemumatransa-
ção.Casosejainvocadoapartirdeuma,entãofarápartedesta,ouseja,será
partedasuaunidadedetrabalho.Senãoexistirumatransa çãoemexecu ção,
umanovaserácriada;
•PROPAGATION_REQUIRES_NEW:ométodosópodeserexecutadodentroda
suaprópriatransa ção.Seforinvocadoapartirdeumatransa ção,entãouma
novaserácriadaexclusivamenteparaseuprocessamentoeaqueoencapsulou
seráparalisadaatéqueestefinalize;
•PROPAGATION_SUPPORTS:tantofazparaométodoseéounãoexecutado
dentrodeumatransa ção. Casosejaexecutadodentrodeuma,faráparteda
suaunidadedetrabalhocomoummétodoqualquer.
Isolamento
Estapolíticadefinequaloníveldeisolamentodenossatransa çãodeclarativa.A
perguntaportrásdestapolíticaé como minha transação é influenciada pela existência
de outras sendo executadas paralelamente?Hátrêsproblemasclássicosenvolvendo
estaquestão. Casoestejaenfrentandoumasitua çãofamiliaremseuprojetotalvez
estasejaasolu çãoparaasuadificuldade.
Oprimeiroproblemaéchamadode leitura suja(dirty reads). Ocorrequando
umatransaçãotemacessoadadosdeoutraqueaindanãotenhafinalizadosuaexe-
220


## Página 231

CasadoCódigo Capítulo10. Gerenciandotransações
cução.Voltandoaoexemploinicialdestecapítulo,umatransa çãoconcorrentepode-
rialeronossoestoquecomaquantidadedeumitemigualazeroporqueatransa ção
responsávelpelaatualizaçãodaqueleregistroaindanãoterminousuaexecu ção.
Outroproblemasãoas leituras diferentes(non repeatable reads),queéquando
umamesmaconsulta,executadacomosmesmosparâmetrossempreretornaresul-
tadosdiferentesquandoistonãodeveriaocorrer.Normalmenteacausadoproblema
éalgumaoutratransa çãoquenaquelemesmoinstanteestejaalterandoosmesmos
registrosdabasededados.
Similaraoproblemadas leituras diferenteséodas leituras fantasmas(phantom
reads),emquenossatransa çãoesperalerumnúmeroderegistroseacabalendoum
númeromaiorporqueoutratransa çãoseencontraincluindonovosregistrosnabase
dedados.
Osproblemasdecorrentesdeumamápolíticadeisolamentosãodifíceisdese-
remresolvidos,masfacilmenteevitáveisquandodefinimosocomportamentoade-
quado. NocasodoSpring,háquatrocomportamentosdistintosàdisposi çãodo
programadorquetambémseencontramrepresentadoscomoconstantesnainter-
face org.springframework.transaction.TransactionDefinition:
•ISOLATION_DEFAULT:atransa çãoadotaráocomportamentopadrãodabase
dedados.Éoquefornecemaiorportabilidadedecódigo,porémrequerquea
equipeconheçabemobancodedadoscomoqualestátrabalhando,vistoque
ocomportamentopadrãovariabastantedefornecedorparafornecedor;
•ISOLATION_READ_UNCOMMITED:trata-sedaop çãomaisperigosa,poisper-
miteàtransaçãolerregistrosqueaindanãotenhamsidocomitadosporoutras
transações.Facilitabastanteaocorrênciadeerrosdotipo leitura suja;
•ISOLATION_READ_COMMITED:definequeatransa çãosóteráacessoaregis-
trosquejátenhamsidocomitadosporoutrastransa ções.Evitaaocorrência
deerrosdotipo leitura suja,mastambémacarretamummaiorpesodeperfor-
mance,vistoquepodemgerarlocksnastabelasouregistrosdosistemadurante
asuaexecu ção;
•ISOLATION_REPEATABLE_READ:usadoparaevitarerrosdotipo leituras di-
ferentese fantasmas.Nocaso,atransa çãosóobteráresultadosdiferentescaso
sejamregistrosalteradosduranteasuaexecu ção;
221


## Página 232

10.2. Aspolíticastransacionais CasadoCódigo
•ISOLATION_SERIALIZABLE:éoníveldeisolamentomaiscarodoponto
devistacomputacional,vistoquegaranteanãoocorrênciadetodososerros
acimamencionados.
Muitaatençãodeveserdadaaqualpolíticaseradotada,poisquantomaisbranda,
maiorapossibilidadedeerros,equantomaisrígidamaiorseráapenalidadesobrea
performancedosistemacomoumtododevidoàcria çãodenovoslockssobreregis-
trosoutabelasnobancodedados.
Somente leitura
Estapolíticaéusadaparadefinirseatransa çãonãoefetuaránenhumaescritana
basededadossubjacente,permitindoqueestaexecutealgumasotimiza çõesparaa
suaexecução. Oprincipalganhodestapolíticaéoganhodeperformance,poisse
nenhumdadoseráalteradoduranteaexecu çãodeumatransa çãoqueimplemente
estapolítica,entãooacessoaosdadoséotimizado.
Éimportantemencionarquecasoocorraalgumatentativadealtera çãodedados
durantesuaexecu çãoumaexce çãoserádisparadapelosistema.
T empo de espera (timeout)
Muitasvezes,devidoaoestadodeumsistema,umatransa çãopodedemorar
muitoparaquesejaexecutadaouvoltedoestadodeparalisa ção,comoporexemplo
noscasosemqueiniciaacidentalmenteumanovatransa çãoouestáaguardando
afinaliza çãodeoutra. Nestescasos,paraseevitarumaparalisa çãodosistemaé
interessantedefinirmosumapolíticadetempodeespera. Casootempoexcedao
quefoidefinido,ainstru çãoderollbackéexecutada,mantendoabasededadosem
seuestadoconsistente.
Política de rollback
Porpadrãoumatransa çãodeclarativaexecutaaopera çãoderollbackapenasse
umaexceçãodetempodeexecu çãofordisparada.Arazãoportrásdestaconven ção
éofatodequeestetipodeexce çãoaoserdisparadanãopossibilitaaimplementa ção
deestratégiasderesgate. OSpringnospermitedefinirquaisostiposdeerroque
deverãoserusadosparadispararoprocedimentoderollback.
222


## Página 233

CasadoCódigo Capítulo10. Gerenciandotransações
10.3 P reparando o ambiente de desenvolvimento
Parahabilitarosuporteatransa çõesdoSpringénecessáriaainclusãodeumanova
dependênciaemnossoprojetoqueéomódulo spring-tx.Bastaadicionarade-
pendêncianoarquivo pom.xmldoseuprojeto:
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-tx</artifactId>
<version>3.1.2.RELEASE</version>
</dependency>
Casoseuprojetojátenhaincluídoomódulo spring-ormou spring-jdbc,
estanovadependêncianãoprecisaserincluída,poisambosjáatemcomodepen-
dênciatransitiva.
10.4 C omo o Spring implementa o suporte a transa -
ções
Agoraquetodaateoriafoiexposta,podemoscome çaracolocaresteconhecimento
emprática,entendendocomooSpringoferecesuporteaogerenciamentotransaci-
onal.Nocentrodestesuportetemoso Gerenciador de Transações (Transaction Ma-
nager).Comoopróprionomejádiz,esteéocomponenteresponsávelporgerenciar
astransaçõesenãoénecessariamentebaseadonaAPIpadrãodoJavaparatal,que
éaJTA( Java Transaction API),massimatecnologiaportrásdoarmazenamento,
comoporexemploJDBC,Hibernate,JPA,JDOeoutras.
PorpadrãooSpringvêmcomumalistabemgrandedegerenciadoresdetran-
sação,enósfocaremosnosqueabordamosnocapítulo7,ouseja,JDBC,Hibernate
eJPA.Adefini çãodequalimplementa çãousaréfundamental,poistrata-sedopri-
meiropassoasertomadopeloprogramadornaconfigura çãodosuportetransacional
doframework.
Transações com JDBC
CasoseuprojetouseJDBCcomomecanismodepersistência,oSpringofereceo
DataSourceTransactionManager,queatuadiretamentesobreafontededados
doseusistema.Portrásdospanos,esteéobeanresponsávelporchamarosmétodos
setAutoCommit, commite rollbackdasconexõesobtidasatravésdafontede
dadosemcasodesucessoouerrodesuastransa ções.
223


## Página 234

10.4. ComooSpringimplementaosuporteatransa ções CasadoCódigo
Aseguirpodemosverumexemplodedeclara çãodestebean. Paraquepossa
atuar,aúnicapropriedadeaserdefinidaé dataSource,quedeveapontarparao
beanquerepresentaafontededadosdoseusistema.
<bean id="transactionManager" class=
"org.springframework.jdbc.datasource.DataSourceTransactionManager">
<property name="dataSource" ref="dataSource"/>
</bean>
Transações com Hibernate
Quando lidamos com Hibernate, a escolha por trás de qual geren-
ciador de transações varia de acordo com a versão do ORM, ou seja,
caso esteja lidando com a versão 3, a classe do bean a ser declarado será
org.springframework.orm.hibernate3.HibernateTransactionManager,
esefor4, org.springframework.orm.hibernate4.HibernateTransactionManager.
Aconfigura çãodosdoisbeanséidêntica: ambosdevemdefiniradependência
sessionFactoryapontandoparao SessionFactorydoseuprojeto,conforme
podeservistonoexemploaseguirqueexpõeaconfigura çãodogerenciadorde
transaçõesparaoHibernate4:
<bean id="transactionManager" class=
"org.springframework.orm.hibernate4.HibernateTransactionManager">
<property name="sessionFactory" ref="sessionFactory" />
</bean>
JP A
O mesmo comportamento adotado nos dois gerenciadores de tran-
sação se aplica também ao caso do JPA. No caso, usamos a classe
org.springframework.orm.jpa.JpaTransactionManager, a qual devemos injetar a
propriedade entityManagerFactory apontando para oEntity Manager Factory
defaultdonossoprojeto,conformepodeservistonoexemploaseguir:
<bean id="transactionManager"
class="org.springframework.orm.jpa.JpaTransactionManager">
<property name="entityManagerFactory" ref="emf"/>
</bean>
224


## Página 235

CasadoCódigo Capítulo10. Gerenciandotransações
10.5 T ransações programáticas
O controle transacional de maior granularidade é o programático,
no qual o próprio desenvolvedor define manualmente a sua unidade
de trabalho. Para que isto ocorra entra em cena mais um template:
org.springframework.transaction.support.TransactionT emplate, que deve ser in-
jetadonosbeansaondesejadenossointeresseaplicaratécnica. Lembrandodo
exemploinicialdestecapítulo, poderíamosinjetá-lodentrodonossobean Loja,
talcomoexpostonaconfigura çãoaseguir,queusacomobaseogerenciadorde
transaçõesdoHibernate4:
<bean id="transactionManager" class=
"org.springframework.orm.hibernate4.HibernateTransactionManager">
<property name="sessionFactory" ref="sessionFactory"/>
</bean>
<bean id="loja" class="br.com.itexto.springforum.Loja">
<property name="transactionTemplate">
<bean class=
"org.springframework.transaction.support.TransactionTemplate">
<property name="transactionManager"
ref="transactionManager"/>
</bean>
</property>
</bean>
Dado que sempre que lidamos com transações o isolamento é funda-
mental, não é interessante ou seguro ter uma instância compartilhada por
mais de um bean, razão pela qual declaramos nosso template como um
bean embutido. Com a injeção pronta, tudo o que precisamos fazer é ali-
mentar nosso template com alguma implementação da interface de callback
org.springframework.transaction.support.TransactionCallback
talcomopodemosvernoexemploaseguir:
public class Loja {
private TransactionTemplate txTemplate;
public void setTransactionTemplate(TransactionTemplate tx) {
this.txTemplate = tx;
225


## Página 236

10.5. Transaçõesprogramáticas CasadoCódigo
}
public void executarVenda(Cliente cliente, Produto produto)
throws ErroSpringForum {
txTemplate.execute(new TransactionCallback<Void>(){
public void doInTransaction(TransactionStatus st) {
try {
decrementarEstoque(produto);
efetuarDebito(cliente, produto.getValor());
enviarEmailCompra(cliente, produto);
enviarTransportadora(cliente, produto);
} catch (ErroSpringForum erro) {
st.setRollbackOnly();
throw erro;
}
return null;
}
});
}
// restante da classe omitido
}
O que realmente nos interessa é o método executarVenda,
aonde definimos nossa unidade de trabalho, composta pela execu ção
em sequência dos métodos decrementarEstoque, efetuarDebito,
enviarEmailCompra e enviarTransportadora, executados dentro do
corpo do métododoInTransaction, da nossa implementação da interface
TransactionCallBack.
Oprimeiropassodogerenciamentoprogramáticodetransa çõeséaexecu çãodo
método executede TransactionTemplate.Esterecebecomoparâmetrouma
implementaçãodainterface TransactionCallback,queobrigaodesenvolvedor
aimplementarumúnicométodo: doInTransaction,quedefinecomoparâmetro
deentradaumobjetodotipo TransactionStatus.
TransactionStatus possui um único método que nos interessa:
setRollbackOnly. Caso uma exceção do tipo ErroSpringForum seja
disparadanocorpodométodo doInTransaction, esteseráinvocado, infor-
mando à transação corrente que todas as operações anteriormente executadas
deverãoserdesfeitas.
226


## Página 237

CasadoCódigo Capítulo10. Gerenciandotransações
10.6 D eclarando transações
Oproblemadastransa çõesprogramáticaséquesequisermosreplicaromesmocom-
portamentoemmaisdeumpontonosistema,oprogramadorprecisarásuarbastante
acamisa. Umaalternativamaisinteressanteparasitua çõesgenéricaséapossibili-
dadeoferecidapeloSpringdedefinirmosdeclarativamenteocontroletransacional.
Trata-sedeumusobastanteinteressantedoconceitodeAOP,poisoquereal-
menteiráocorrerportrásdospanoséaaplica çãodeum advicedotipo aroundem
todososbeanssobreosquaisdesejemosadicionarestecontroletransacional.
Hádoiscaminhosaseremseguidosnadefini çãodeclarativadetransa ções. O
primeiroémenosintrusivoeconsistenadefini çãodospontostransacionaisapenas
viaconfiguração,enquantoosegundoéamaneiramaisprodutivaexistenteatual-
menteatravésdeanotações.
Declarando transações via configura ção XML
Comomencionado,aop çãomenosintrusivaparaadicionarmosocontroletran-
sacionaldeclarativoéviaconfigura çãoXML.Dadoqueosuporteatransa çõesde-
clarativasdoSpringébaseadoemAOP,faz-senecessáriaainclusãodonamespace
aopemnossoarquivodeconfigura çãoemconjunto,comumanovidadequeéo
namespace tx,conformepodeservistonoexemploaseguir:
<beans default-autowire="byType"
xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:context="http://www.springframework.org/schema/context"
xmlns:jee="http://www.springframework.org/schema/jee"
xmlns:tx="http://www.springframework.org/schema/tx"
xsi:schemaLocation="http://www.springframework.org/schema/jee
http://www.springframework.org/schema/jee/spring-jee-3.1.xsd
http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
http://www.springframework.org/schema/tx
http://www.springframework.org/schema/tx/spring-tx-3.1.xsd
http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context-3.1.xsd">
</beans>
Dentrodonamespace txháumatagchamada <tx:advice>,usadaparade-
227


## Página 238

10.6. Declarandotransações CasadoCódigo
finirquaisosmétodosemquenossocontroletransacionalseaplica.Nossoprimeiro
passoseráasuadeclara çãoemnossoarquivodeconfigura çãotalcomopodeser
vistonotrechoaseguir:
<tx:advice id="txAdvice" transaction-manager="transactionManager">
<tx:attributes>
<tx:method name="executar*" propagation="REQUIRED"
isolation="SERIALIZABLE"/>
<tx:method name="*" propagation="SUPPORTS"/>
</tx:attributes>
</tx:advice>
Atag <tx:attributes>éusadaparadefinirtodososmétodosqueirãorece-
beronossocontroletransacional.Nocaso,estamosdefinindoquetodométodoque
comececom executarreceberáapolíticadepropaga ção REQUIREDcomomais
altoníveldeisolamentoetodososdemaismétodoscomapolíticadepropaga ção
SUPPORT,ouseja,casosejamexecutadosdentrodeumatransa ção,farãoparteda
suaunidadedetrabalho.
Oatributo transaction-managerdefinequalogerenciadordetransa çõesa
serusadoporeste advice. Casoomitido,seriausadocomopadrãoobeancujo
identificadorfosseiguala transactionManager.
Opróximopassoagoraédefinirquaisospointcutsaondeoadviceseráaplicado.
Voltaàcenaatag <aop:config>quevimosanteriormenteequefecharáonosso
círculo,talcomopodeservistonotrechoaseguir:
<aop:config>
<aop:advisor pointcut="execution(* *..Loja.*(..))"
advice-ref="txAdvice"/>
</aop:config>
Comistooaspectoéaplicadoemtodososmétodosdobean lojaenossocon-
troletransacionalestaconcluídousandoXML.
Declarando transações com anota ções
Oproblemacomaconfigura çãonoformatoXMLéqueestatendeacrescerbas-
tanteconformeoprojetoevolui.Asegundaalternativaque,comomencionei,étam-
bémamaisprodutivasedaatravésdeanota ções. Parahabilitá-lasóénecessário
adicionarumalinhadeconfigura çãotalcomonotrechoaseguir:
228


## Página 239

CasadoCódigo Capítulo10. Gerenciandotransações
<tx:annotation-driven transaction-manager="transactionManager" />
Atag <tx:annotation-driven>instruiocontaineraaplicarasregrasde
transacionalidadeatodososbeansquepossuamaanota ção @Transactionalin-
seridanadefini çãodaclasse(aplicandoaregraatodososmétodosdamesma)oua
métodosespecíficos.
Oatributo transaction-manager,comonocasodatag <tx:advice>,
éopcional: casoomitidoseráusadooprimeirobeanencontradocujonomeseja
transactionManager.
Aseguirpodemosverumexemplodeclasseanotadacom @Transactional:
@Component
public class Loja {
@Transactional(propagation=Propagation.REQUIRES_NEW,
isolation=Isolation.SERIALIZABLE,
timeout=120)
public void executarVenda(Produto produto, Cliente cliente) {
//conteúdo oculto, agora sem o TransactionTemplate
}
}
10.7 C oncluindo
NestecapítulovimoscomooSpringimplementaseusuporteatransa ções.Elaéuma
soluçãodealtíssimaprodutividadedevidoàsuafacilidadedeuso,oquetornoueste
suporteumadasprincipaisrazõespelasquaisdesenvolvedoresdomundointeiro
começaramaseinteressarpeloframework.Justamente,opontomaisimportanteé
vocêentenderadiferençaentreasdiferentesestratégiasdetransa çãoequaloimpacto
queelaspodemteremseuprojeto.
Casoqueiraseaprofundaremmecanismosdetransa çãoemgeral,recomendoa
leituradolivro Java Transaction Design Strategies,deMarkRichards[13]quepode
inclusiveserobtidogratuitamentenositedaInfoQ-http://www.infoq.com.
229


## Página 241

Capítulo11
Protegendonossaaplica çãocom
SpringSecurity
OSpringSecurityéumframeworkdecontroledeacesso,quenospermitedefinir
deformadeclarativa quemacessaráo quêemnossossistemas.Muitosodescrevem
comoum framework de segurança,masestaéumadefini çãomuitoimprecisaeque
podelevardesenvolvedoresàfalsaimpressãodequecomeleconseguiríamoscons-
truirprojetosinvulneráveisaataques,oquenãoéverdade.
Ocontroledeacessoépartefundamentalnaseguran çadequalquerprojeto,po-
rémsegurançanãoselimitaa“apenas”esteaspecto.Háoutrosproblemasquetam-
bémdevemsertratadospelodesenvolvedorquenãosãoresolvidospeloSpringSe-
curity,comoporexemplo,ataquesde negação de servi ço(DOS: Denial of Service),
entradasmaliciosas,inje çãodecódigoemuitasoutrasamea çasqueassolamsiste-
maspelomundo.
OcontroledeacessodoSpringSecuritypodeseraplicadoemdoisníveis:nasre-
quisiçõesquechegamànossaaplica ção,casoestejamoslidandocomumprojetoweb


## Página 242

11.1. Entendendoautenticaçãoeautoriza ção CasadoCódigo
enainvoca çãodemétodosdosbeansgerenciadospelocontextodoSpring.Como
veremos,nãoéacidentalmentequeuseiapalavra aspectonoparágrafoanterior:con-
trolaroacessoéuminteressetransversalqueéresolvidopeloframeworkatravésdo
suporteaAOP.Masantesdapráticaénecessárioconhecermososdoisconceitos
principaisportrásdoseufuncionamento.
11.1 E ntendendo autenticação e autorização
Todocontroledeacessopossuidoisprocedimentos: autenticaçãoe autorização.O
primeirotemporobjetivogarantirqueumusuáriorealmenteéquemdizser,en-
quantoosegundoverificaseeste,umavezautenticado,possuipermissãoparaexe-
cutardeterminadatarefanosistema.
Todoprocessodeautentica çãoseiniciacomousuárioapresentando-seaosis-
tema,entregandosuas credenciais,quesãoseusdadosdeidentifica ção,comoologin
esenhaoudadosbiométricos. Osistemaautenticadorentãogeraumaassinatura
únicacomestascredenciaise,combasenesta,verificaaexistênciaounãodousuá-
rioemsuasbasesdedados.
Existindoousuário,nãoraroascredenciaisestãoassociadasadadoscadastrais
relativosaeste,comoporexemplonomecompleto,datadaúltimaautentica ção,en-
dereçoetc.Aestasinforma çõesosframeworksdecontroledeacessocostumamdar
onomede principal(sujeito).Lembre-se:umusuárionãonecessariamenteéumser
humano,podeseroutrosistematambém.
Outroconjuntodeinforma çõesassociadasàscredenciaissãosuaspermissões
deacesso,normalmentechamadasde papéis(roles)ou autoridades(authorities),que
informamaosistemaquaisoslimitesdeatua çãodoindivíduo.Oprocessodeverifi-
caçãodaspermissõesdousuárioéaautoriza ção,queocorresempreapósaautenti-
caçãonosistema.
232


## Página 243

CasadoCódigo Capítulo11. ProtegendonossaaplicaçãocomSpringSecurity
Acegi eSpring Security são a mesma coisa?
Em2003,umgrupodeusuáriosentusiastasdoSpringiniciaramum
projetochamado Acegi Security System for Spring baseadonosuportea
AOPoferecidopeloframework.Comopassardotempo,estefoisetor-
nandocadavezmaispopularatéquesuaprimeiraversãooficialfoilan-
çadaem2006. Noanoseguinteoprojetofoiadotadocomopartedo
portfóliodoSpringeemsuasegundaversãofoirebatizadocomo Spring
Security.
ArespostaàperguntaéqueoSpringSecurityquetemoshojeéna
realidadeaevolu çãodoantigoprojetoAcegi.
11.2 O s módulos do Spring Security
AssimcomooSpring,oframeworkécompostoporumasériedecomponentessemi
independentesquepossibilitamaoprogramadorusarapenasaquelesqueserãoúteis
aoseuprojeto.Aversão3.1écompostapelosmódulosaseguir:
•spring-security-core:oúnicomóduloobrigatórioporsetratardaes-
sênciadoframework.Encontram-seaquiimplementadososmecanismosde
autorizaçãoeautentica ção,alémdetodasasinterfacesbásicasquesãoreapro-
veitadasportodososdemaismódulosecomponentesterceirizadosdesenvol-
vidosparaoframework;
•spring-security-config:apartirdaversão2.0,oframeworkpassoua
oferecerumnamespacepróprioquereduziudramaticamenteaquantidadede
configuraçãoqueodesenvolvedorprecisavadigitar.Dadooganhodeprodu-
tividadedeveserconsideradoobrigatórioportodososnãomasoquistas;
•spring-security-web:todaainfraestruturanecessáriaparaodesenvol-
vimentodeprojetosweb.Nestemóduloéqueseencontrapresenteocódigo
responsávelporlidarcomaintercepta çãoderequisi çõesaprojetoswebepor-
tantodeusoobrigatórioemprojetosdestetipo;
•spring-security-taglibs:contémumabibliotecadetagsquenosper-
mitedefinirquaisáreasdenossaspáginasserãoacessíveisaosusuáriosdosis-
temacombaseemsuaspermissões. Assimcomoomódulo spring-security-
233


## Página 244

11.2. OsmódulosdoSpringSecurity CasadoCódigo
config,apesardeseropcionalacabasendousadosempreportodosaqueles
queprojetemsuaspáginascomalgumatecnologiabaseadaemJSP;
•spring-security-remoting:provêintegraçãocomoSpringRemoting;
•spring-security-ldap: suporte a autenticação a partir de servidores
LDAP;
•spring-security-cas:suporteaautentica ção/autorizaçãoporservidores
desinglesignonCAS;
•spring-security-openid:suporteaOpenID.
Assimcomofizemosemtodaasegundapartedestelivro,usaremosoprojeto
Spring Fórumcomonossoguia.Nossaprimeiraatividadeseráainclusãodequatro
dependênciasnoarquivo pom.xmltalcomolistadasaseguir:
<!-- Spring Security Core -->
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-core</artifactId>
<version>3.1.3.RELEASE</version>
</dependency>
<!-- Spring Security Config -->
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-config</artifactId>
<version>3.1.3.RELEASE</version>
</dependency>
<!-- Spring Security Web -->
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-web</artifactId>
<version>3.1.3.RELEASE</version>
</dependency>
<!-- Spring Security Taglibs -->
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-taglibs</artifactId>
<version>3.1.3.RELEASE</version>
</dependency>
234


## Página 245

CasadoCódigo Capítulo11. ProtegendonossaaplicaçãocomSpringSecurity
11.3 C onfigurando os filtros de acesso
PrimeiroiremostratardomodocomooSpringSecurityatuasobreorecebimentode
requisiçõesHTTP.Paraativarestesuporte,teremosdedeclararumfiltronoarquivo
web.xmldonossoprojetoqueseráoresponsávelporlidarcomtodasaschamadas
externasquenossaaplica çãoreceberáecujaconfigura çãopodemosveraseguir:
<filter>
<filter-name>springSecurityFilterChain</filter-name>
<filter-class>
org.springframework.web.filter.DelegatingFilterProxy
</filter-class>
</filter>
<filter-mapping>
<filter-name>springSecurityFilterChain</filter-name>
<url-pattern>/*</url-pattern>
</filter-mapping>
Estefiltroéo DelegatingFilterProxyeseufuncionamentoconsisteemen-
caminhartodasasrequisi çõesparaumcomponentefundamentaldoSpringSecurity
queéo Filter Chain (filtro encadeador),orealresponsávelpelaconfigura çãode
acessoàsURLsdosistema,eéexecutadocomoumbeangerenciadopelocontexto
deaplicaçãodoSpring.
UmaaplicaçãoprotegidapeloSpringSecuritypodetermaisdeumfiltroenca-
deador,sendoassiménecessárioconfiguraro DelegatingFilterProxydetal
formaqueestesaibaqualobeancomoqualdeveinteragir.Fazemosistoatravésda
definiçãodoseunomepelatag <filter-name>,quedevecorresponderaoiden-
tificadordestebean.
Como veremos mais à frente neste capítulo, esta configuração é feita de
forma automática peloSpring Security minimizando o trabalho do pro-
gramador. Por conven ção do framework, o nome padrão deste bean é
springSecurityFilterChain,oquetornaumaboapráticasempreoadotar-
mosnestepontodaconfigura çãodonossoprojeto.
Apartirdestepontodolivrofaz-senecessáriaoutraaltera çãoemnossoprojeto.
Nocapítulo8definimosoarquivobásicodeconfigura çãodocontainerSpringatravés
dadeclaraçãodoservlet DispatcherServlettalcomonotrechoaseguir:
<servlet>
<servlet-name>DispatcherServlet</servlet-name>
235


## Página 246

11.3. Configurandoosfiltrosdeacesso CasadoCódigo
<servlet-class>
org.springframework.web.servlet.DispatcherServlet
</servlet-class>
<init-param>
<param-name>contextConfigLocation</param-name>
<param-value>/WEB-INF/spring/spring-servlet.xml</param-value>
</init-param>
<load-on-startup>1</load-on-startup>
</servlet>
O Spring Fórumeraapenasocontextodesteservlet. Asitua çãomudouagora
poisprecisamosconfigurarocontextodoSpringparaquesejacompartilhadopelo
DispatcherServletenossofiltro.Asolu çãoparaoproblemaéadeclara çãode
umlistenerdotipo ContextLoaderListenernoarquivo web.xmltalcomo
expostonotrechoaseguir:
<listener>
<listener-class>
org.springframework.web.context.ContextLoaderListener
</listener-class>
</listener>
<context-param>
<param-name>contextConfigLocation</param-name>
<param-value>
/WEB-INF/spring/spring-servlet.xml
/WEB-INF/spring/spring-data.xml
/WEB-INF/spring/spring-security.xml
</param-value>
</context-param>
EstelisteneréresponsávelporcarregarumcontextodoSpringparaanossaapli-
caçãousandocomoarquivosdeconfigura çãoovalorquedefinimosparaoparâme-
trodecontexto contextConfigLocation.Nãoénecessárioalteraraconfigura-
çãodo DispatcherServletquevimosantes.
236


## Página 247

CasadoCódigo Capítulo11. ProtegendonossaaplicaçãocomSpringSecurity
11.4 C onfigurando o contexto do Spring
Daquiparafrentesóprecisamosnospreocuparcomasconfigura çõespadrãodo
Spring. UmadasgrandesnovidadesqueoSpringSecuritytrouxeemrela çãoao
AcegifoioseuesquemaXMLquereduziubastanteaquantidadedeconfigura çãoque
oprogramadorprecisavaescrever.NaépocadoAcegi,nãoeramrarososcasosem
quenosvíamosdandomanuten çãoemcentenasdelinhasdeconfigura ção.Gra ças
àequipedaSpringSourceestaéhojeapenasumatristerecorda ção.
Paragarantiramodularidadedenossosistemavamoscriarumnovoarquivode
configuraçãoondedeclararemosonamespace securityusadopeloSpringSecu-
rity.Ocorpodonossoarquivoserásimilaraolistadoaseguir:
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:security="http://www.springframework.org/schema/security"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
http://www.springframework.org/schema/security
http://www.springframework.org/schema/security/spring-security-3.1.xsd">
<!-- Conteúdo oculto no momento -->
</beans>
Nossaprimeiraconfigura çãoéainclusãodatag <security:html>queseráa
responsávelpordefinir50%doqueoSpringSecurityprecisaparafuncionar.Pode-
mosversuadeclara çãoiniciallistadaaseguir:
<security:http auto-config="true">
<security:intercept-url
pattern="/post/publicar/**" access="ROLE_MEMBRO"/>
<security:intercept-url
pattern="/usuario/editar/**" access="ROLE_ADMIN,ROLE_MEMBRO"/>
<security:intercept-url pattern="/**" access="ROLE_ANONYMOUS"/>
</security:http>
É incrível a quantidade de tarefas executadas com tão pouco código:
<security:http>comoatributo auto-configdefinidocomo truefazbas-
tantecoisa:
• Criaráumformuláriodeautenticaçãodeformaautomática.
237


## Página 248

11.4. ConfigurandoocontextodoSpring CasadoCódigo
• DefineasURLsdelogouteautenticaçãoapartirdeconven çõesqueveremos
maisafrente.
• Configuraofiltroencadeador(SpringSecurityFilterChain).
Istosemmencionarqueaindaaproveitamosparadefinirasregrasdeacessopara
trêspadrõesdeURL!
Usamos <security:intercept-url>paradefinirasregrasdeacessoàs
URLsdosistema. Aordememquesãodeclaradaséimportante,poissempreque
umarequisiçãochegaao Filter Chainestaévalidadacontratodasasregrasdecima
parabaixo.Oatributo patterndefineopadrãodaURLusandoasintaxedoAnt,
enquanto accesscontémasregrasdeautoriza ção.Nesteprimeiromomentousa-
mosanota çãomaissimplespossívelqueconsistenameralistagemdetodasasper-
missões( roles)separadasporvírgula.
Atenção especial deve ser dada à terceira declara ção de
<security:intercept-url>. Observe o valor que definimos para o atri-
buto access: ROLE_ANONYMOUS.EsteéumvalorespecialparaoSpringSecurity
queindicaasitua çãonaqualousuáriotentandoacessarnossaaplica çãonãose
encontraautenticado. Sendoassim,imaginequeinvertêssemosaordememque
declaramosastags <security:intercept-url>. Nestecaso,teríamosacesso
liberadoaqualquerum,poisotestedeautoriza çãopassariaparaaurlrepresentada:
/* *,queapontaparaqualquerendere çoquecomeceapartirdaraizdoprojeto.
Com <security:intercept-url/>tambémpodemoshabilitarsuportea
HTTPS,quenormalmenteéaplicadoemse çõessensíveisdosite,comoporexemplo
nocheckoutdecomprasemumalojavirtual,aondedadosconfidenciaisdousuário
sãoenviados.Paratal,bastaadicionaroatributo requires-channel,queatual-
menterecebetrêspossibilidadesdevalor: https, httpe any(tantofazseaURL
foracessadaporHTTPouHTTPS).Podemosveralgunsexemplosdesuaaplica ção
nalistagemaseguir:
<!-- HTTPS aplicado -->
<intercept-url pattern="/checkout/**"
access="ROLE_MEMBRO" requires-channel="https"/>
<!-- HTTP padrão -->
<intercept-url pattern="/**"
access="ROLE_MEMBRO" requires-channel="http"/>
<!-- Tanto faz -->
<intercept-url pattern="/posts/**"
access="ROLE_MEMBRO" requires-channel="any"/>
238


## Página 249

CasadoCódigo Capítulo11. ProtegendonossaaplicaçãocomSpringSecurity
CasoousuárioacesseumaURLcomocanalpré-definidocomoprotocoloer-
rado-httpaoinvésdehttpsporexemplo-oSpringSecurityfaráoredirecionamento
deformaautomática.
Comoditonoiníciodestase ção,atag <security>resolve50%donossopro-
blemaaodefinirasregrasde autorizaçãodasrequisiçõesrecebidaspelaaplica çãoe
configuraobásicoportrásdocontroledeacessonestenível.Sabemoso quêestáa
seracessado,restasaber por quem.Entramemcenadoiscomponentesimportantes
doframework:oprovedoreogerenciadordeautentica ção( authentication provider
e authenciation manager).
O Gerenciador e o provedor de autenticação
Ogerenciadordeautentica çãoéoresponsávelporreceberascredenciaisdeum
usuárioeverificarsuaautenticidade,oqueéfeitotestando-ascontraumoumais
provedoresdeautentica çãoaquetemacesso. Estaverifica çãoéfeitasequencial-
mente,ouseja,oprimeiroprovedordeautentica çãoqueconfirmaraexistênciade
umusuáriocomestascredenciaisvalida-ocomoautêntico.
Pensenoprovedordeautentica çãocomoumafontededadosfeitaespecifica-
menteparaarmazenarinforma çõesdeusuárioscapazdeexecutarumaúnicacon-
sultaquerecebecomoparâmetroascredenciaisretornandoinforma çõesdousuário
casoexistam(incluindosuaspermissõesdeacesso).
NocontextodocontroledeacessoaURLso Chain Filteracessaapenasoge-
renciadordeautentica ção,nãoprecisandoportantosepreocuparcomaorigemdos
dadosdeautentica çãodousuáriotalcomopodeservistonoesquemaaseguir:
Figura11.1:ChainFilter,AuthenticationManagereseusAuthenticationProviders
239


## Página 250

11.4. ConfigurandoocontextodoSpring CasadoCódigo
Há inúmeros provedores de autenticação disponíveis para o Spring Se-
curity atualmente. Como exemplos podemos citar o suporte a LDAP, ban-
cos de dados, registros em memória, além do suporte a redes sociais como
Twitter, Facebook, Linkedin, Google+ e outras. Por trás da cortina, um
provedor de autenticação é apenas uma classe que implementa a interface
org.springframework.security.authentication.AuthenticationProvider,
sendoassimcasonãoexistaumqueatendasuasnecessidades,facilmentepodemos
criarum,talcomofaremosmaisafrentenestecapítulo.
Indo para a parte prática, é necessário que declaremos em nosso ar-
quivo de configuração nosso gerenciador de autenticação. Para tal usamos
<security:authentication-manager>,quereceberácomofilhosumoumais
elementosdotipo <security:authentication-provider>,representandoos
provedoresdeautentica çãousadosemnossoprojetotalcomonalistagemaseguir:
<security:authentication-manager>
<security:authentication-provider>
<security:user-service>
<security:user name="bruce"
password="lee" authorities="ROLE_MEMBRO"/>
<security:user name="admin"
password="admin" authorities="ROLE_MEMBRO,ROLE_ADMIN"/>
</security:user-service>
</security:authentication-provider>
</security:authentication-manager>
Atag <security:user-service>representaoprovedordeautentica ção
maissimplesdisponibilizadopeloSpringSecurity:estearmazenaosdadosdosusuá-
rioemmemóriacombasenadeclara çãodeumaoumaistags <security:user>,
quedefinemonome,senhaepermissõesdosusuáriosgerenciados.
. Como podemos ver, este é declarado dentro da tag
<security:authentication-provider> no interior de
<security:authentication-manager>. Posteriormente iremos adicio-
nar nossa própria implementação neste gerenciador de autenticação e assim
finalmenteveremoscomoestesatoresinteragementresiportrásdospanos.
Ainteraçãoentrenossofiltroeogerenciadordeautentica çãosedaemdoismo-
mentos:
•Usuário tenta se autenticar no sistema : há um mapeamento
ocultonatag <security:html>queligaaURLdoformuláriodeloginpor
240


## Página 251

CasadoCódigo Capítulo11. ProtegendonossaaplicaçãocomSpringSecurity
estaconfiguradoeonossogerenciadordeautentica ção.Quandoesterecebe
ascredenciaisdousuário,verificaseexisteumregistrodeusuárioquecorres-
pondaaestaseoautenticanosistema,emseguidaoretornandoaofiltro.
•Usuário já está autenticado no sistema :ogerenciadordeauten-
ticaçãoretornaráaspermissõesdousuário,queserãoverificadascontraasre-
grasdefinidaspelomapeamentodaURLquecorrespondaaopadrãodesejado
pelousuário.
Esteéonossoprimeirocontatocomestasentidades,paraclarearumpoucoas
coisas,agoraqueestamoscomnossoprojetointeiramenteconfigurado,vamostentar
acessaraurldepadrão /post/publicar/* * semestarmosautenticadosevero
queacontece.
11.5 O formulário de login
IniciandooprojetoeacessandoaURLhttp://localhost:8080/spring-forum/post/
publicarsomossaudadospeloformuláriodelogingeradoautomaticamentepelo
SpringSecurity:
Figura11.2:FormuláriodelogingeradopeloSpringSecurity
Ofiltroaoverificarquenãoexistiaumusuárioautenticadoeumaregrase
aplicava à URL em questão faz um redirecionamento para o endereço padrão
/spring_security_login,queapontaparaopáginaquecontémoformulário
deautenticaçãogeradoautomaticamentepeloSpringSecurity.Casoousuáriofor-
neçaologinesenhacorretoseousuárioencontradopossuaaspermissõesnecessá-
riasparaacessarorecurso,estesetornarádisponívelaestesemproblema.
241


## Página 252

11.5. Oformuláriodelogin CasadoCódigo
Éinteressantedarumaolhadanocódigofontedesteformuláriolistadonotrecho
aseguirpoisneleveremosalgumasconven çõesadotadaspeloframework:
<form name= 'f' action='/spring-forum/j_spring_security_check'
method='POST'>
<table>
<tr>
<td>User:</td>
<td><input type= 'text' name='j_username' value=''></td>
</tr>
<tr>
<td>Password:</td>
<td><input type= 'password' name='j_password'/></td>
</tr>
<tr>
<td colspan= '2'>
<input name="submit" type="submit" value="Login"/>
</td>
</tr>
</table>
</form>
A primeira destas convenções diz respeito à URL de autenticação:
j_spring_security_check. Em seguida, observamos também o nome
dosparâmetrosincluídosnoformulário: j_usernamee j_password,usados
pararepresentarologinesenhadousuário. Tudooqueoprogramadorprecisa
fazerécopiarestamarca ção,alterá-laparaquefiquedeacordocomolayoutdo
seusiteealteraralgumasconfigura çõesbásicasdoformuláriodeautentica çãono
contextodoSpringtalcomofizemosnocasodo Spring Fórumlistadoaseguir:
<security:http auto-config="true" use-expressions="true">
<security:form-login
login-page="/"
default-target-url="/"
authentication-failure-url="/"/>
<!-- Restante omitido -->
</security:http>
Adicionamos a nossa própria configuração do formulário de login usando
<security:form-login/>,queanteserageradadeformaautomáticapelofra-
mework.Aprimeiraaltera çãofeitadizrespeitoàURLaondeseráexpostooformulá-
242


## Página 253

CasadoCódigo Capítulo11. ProtegendonossaaplicaçãocomSpringSecurity
riodelogin.Emnossoprojetoesteéexpostoemtodasaspáginas,maspadronizamos
oredirecionamentoparaapáginainicialcasoalgumusuárionãoautenticadotente
acessarumaárearestrita. Abaixopodemosvercomoficouonossoformuláriode
autenticaçãoemdestaque:
Figura11.3:Nossoformuláriodelogin
Outro atributo importante que alteramos foidefault-target-url, que
define qual a URL a ser acessada caso a autenticação seja bem sucedida, e
authentication-failure-url,quedefinequalaURLaserexpostaemcaso
deumloginmalsucedido.Nocasodo Spring Fórum,ambasapontamparaapágina
inicial.Eistoétudooqueprecisamossabernestemomentoarespeitodoformulário
deautenticação.
11.6 E screvendo um provedor de autenticação
Devoltaaosprovedoresdeautentica ção,acria çãodeumcustomizadonosajudará
aentendermelhoromecanismoportrásdoSpringSecurity. Precisamosconhe-
cerapenastrêsinterfaces: AuthenticationProvider, Authenticatione
GrantedAuthority. Omodocomoestasserelacionamcomoprovedordeau-
tenticaçãoéilustradonodiagramadeclassesaseguir:
243


## Página 254

11.6. Escrevendoumprovedordeautenticação CasadoCódigo
Figura11.4:Nossoprovedordeautentica ção
Aprincipalinterfaceé AuthenticationProvider,quecomoopróprionome
jánosdiz,representaumprovedordeautentica çãoparaoSpringSecurity. Como
podeservistonodiagrama,estaébastantesimples,for çandooprogramadoraim-
plementarapenasdoismétodos. Comecemospelomaissimplesqueéafun ção
supports,querecebecomoparâmetroumvalordotipo java.lang.Object
querepresentaumobjetodeautentica çãosuportadopelonossoprovedor.
Umobjetodeautentica çãoéoresponsávelporarmazenarascredenciaisdo
usuário. O Spring Security já vêm com alguns, sendo o mais popular a classe
UsernamePasswordAuthenticationToken,querepresentaumobjetodeau-
tenticaçãodotipologinesenha:exatamenteousadoporformuláriosdeautentica-
ção.
A seguir podemos ver como implementamos esta função na classe
SFAuthenticationProvider:
public boolean supports(Class<?> authentication) {
return (UsernamePasswordAuthenticationToken.
class.isAssignableFrom(authentication));
}
Aoutrafun çãoaserimplementadaé authenticate,queretornaumobjeto
dotipo Authentication,queéoresponsávelporarmazenarosdadosdeauten-
ticaçãodousuário,oqueincluisualistadepermissões.Éinteressanteobservarque
244


## Página 255

CasadoCódigo Capítulo11. ProtegendonossaaplicaçãocomSpringSecurity
esteobjetoéusadoemdoismomentos:noprimeirocontémapenasascredenciais
dousuárioqueverificaremoscontranossabasededados,enosegundo,casooteste
dêpositivo,éusadointernamentepeloframeworknoprocessodeautoriza ção.
Aseguirpodemosveralistagemdanossaimplementa çãodestafun ção:
public Authentication authenticate(Authentication auth)
throws AuthenticationException {
UsernamePasswordAuthenticationToken token =
(UsernamePasswordAuthenticationToken) auth;
String username = token.getName();
String senha = token.getCredentials().toString();
Usuario usuario = getDaoUsuario().getUsuario(username, senha);
/*
Não encontrei um usuário, retornar null indica
uma autenticação falha.
*/
if (usuario == null) return null;
List<PermissaoUsuario> permissoes = getDaoPermissao().
getPermissoesUsuario(usuario);
SFAuthentication resultado =
new SFAuthentication(usuario, permissoes);
resultado.setAuthenticated(usuario != null);
return resultado;
}
Em nosso caso, criamos nossa própria implementação da interface
Authentication: SFAuthentication. Com ela apenas encapsulamos
duasinforma ções: anossainstânciadaclasse Usuarioealistadepermissões
relativasaeste,quesãoobtidasatravésdoDAO DAOPermissao,quenosretorna
umalistadeobjetosdotipo PermissaoUsuario.
Aclasse PermissaoUsuarioimplementaainterface GranthedAuthority,
quepossuiapenasumafun ção,chamada getAuthority,queretornaumvalordo
tipo String,queéonomedapermissãodentrodosistema.
Parafinalizaronossoprovedordeautentica ção,tudooqueprecisamosfazeré
declará-lonoarquivodeconfigura çõestalcomoéfeitonalistagemaseguir:
<!-- O bean que representa nosso provedor -->
<bean id="sfAuthenticationProvider"
autowire="byType"
245


## Página 256

11.7. UsandoSpEL CasadoCódigo
class="br.com.itexto.springforum.security.SFAuthenticationProvider"/>
<security:authentication-manager>
<!-- Nosso provedor -->
<security:authentication-provider ref="sfAuthenticationProvider"/>
<!-- Provedor baseado em memória -->
<security:authentication-provider>
<security:user-service>
<security:user name="jimmy" password="hendrix"
authorities="ROLE_MEMBRO"/>
</security:user-service>
</security:authentication-provider>
</security:authentication-manager>
Usandooatributo refdatag <security:authentication-provider>
bastareferenciarobeancorrespondenteaonossoprovedordeautentica çãoepronto,
esteseencontranalistadeprovedoresusadaspelogerenciadordeautentica çãodo
sistema.
11.7 U sando SpEL
Atéestepontodocapítulovimosapenascomodefinirestaticamenteaspermissões
aosrecursosdaaplica ção,oqueéumasolu çãobastantelimitada. Háoutromodo
caminho:assimcomoSpELtrouxedinamismoparaosnossosarquivosdeconfigu-
ração,estetambémseaplicaaoSpringSecurityeoqueémelhor:foiestendidopara
quenosofere çamáximaflexibilidade.
Podemosaplicarasexpressõesemtodosospontosdoframework:nosarquivos
deconfiguração,assimcomonasanota çõesetaglibsqueveremosmaisadianteneste
capítulo.Parahabilitarseuusonoarquivodeconfigura ção,tudooqueprecisamos
fazeréadicionaroatributo use-expressionscomovalor truecomofoifeito
notrechoaseguir:
<security:http auto-config="true" use-expressions="true">
<!-- Restante omitido -->
<security:intercept-url pattern="/post/publicar/**"
access="hasRole('ROLE_MEMBRO')"/>
<security:intercept-url pattern="/**"
access="isAnonymous()"/>
</security:http>
246


## Página 257

CasadoCódigo Capítulo11. ProtegendonossaaplicaçãocomSpringSecurity
AfunçãomaiscomuméhasRole,querecebeumastringrepresentandoonome
dapermissão,eéexcelenteparaquandoqueremoslidarcomapenasumapermissão,
masacoisaficameiocomplicadaquandoprecisamoscombinarmaisdeumacomo
noexemploabaixo:
<security:intercept-url pattern="/membro/gerenciar"
access="hasRole('ROLE_MEMBRO') or hasRole( 'ROLE_ADMIN')"/>
Nestecaso,usamos hasAnyRole,querecebeumalistadepapéisseparadaspor
vírgulacomoem:
<security:intercept-url pattern="/membro/gerenciar"
access="hasAnyRole('ROLE_MEMBRO','ROLE_ADMIN')"/>
Eclaro,podemoscombinarestasduasexpressõestambémsequisermos,como
noexemploaseguir:
<spring:security-url pattern="/membro/gerenciar"
access="hasAnyRole('ROLE_ADMIN','ROLE_MODERADOR')
and ! hasRole( 'ROLE_MEMBRO')"/>
Alémdestasfunçõesembutidas,háalistagemabaixoqueodesenvolvedorpode
usardeacordocomasuanecessidade:
•principal:apontaparao principaldousuárioautenticado.
•authentication:nosforneceacessoaoobjetoAuthenticationcorrente.
•permitAll:sempreretornatrue,permitindoquequalquerumacesseore-
curso.
•denyAll:sempreretornaráfalso,negandosempreoacesso.
•isAnonymous():verificaseestamoslidandocomumusuárionãoautenti-
cado.
•isAuthenticated():verificaseestamoslidandocomumusuárioautenti-
cado.
247


## Página 258

11.8. Protegendoinvocaçãodemétodosembeans CasadoCódigo
11.8 P rotegendo invocação de métodos em beans
Como dito no início deste capítulo, o Spring Security se aplica a dois níveis:
requisições e invocação de métodos. A maneira mais produtiva de tirar pro-
veito deste recurso se da através da anotação @Secured, definida no pacote
org.springframework.security.access.annotation. Podemosverum
exemplodasuaaplica çãonocódigoaseguir:
public class UsuarioService {
// Usando SpEL
@Secured("hasRole('ROLE_ADMIN')")
public void banir(Usuario usuario) {
...
}
// Passando uma lista de permissões
@Secured({"ROLE_ADMIN", "ROLE_MODERADOR"})
public void advertir(Usuario usuario, String mensagem) {
...
}
}
Comojáeradeseimaginar,oSpringSecurityexerceocontroledeacessoatravés
dosuporteaAOP.Sendoassim,faz-senecessárioqueadicionemosumaúnicalinha
emnossoarquivodeconfigura ção,talcomoexpostonocódigoaseguir:
<security:global-method-security secured-annotations="enabled"/>
Difícilpensaremumasolu çãomaissimples:agoratodobeangerenciadopelo
containerdoSpringquepossuaaanota ção @Securedemseusmétodosounasua
declaraçãodeclasse(oqueiráaplicararegraatodososmétodosdobean)teráseu
acessogerenciadopeloSpringSecurity.
Ointeressantedosuporteainvoca çãodemétodoséqueohorizontedeaplica ção
doSpringSecurityseamplia:aplica çõesdesktoppoderãotirarproveitodosmesmos
recursos.
11.9 T ags
OSpringSecuritytambématuanacamadadevisualiza çãoatravésdasuabiblioteca
detagsquepodemseraplicadasapáginasJSPoutecnologiasderivadas.Estasirão
248


## Página 259

CasadoCódigo Capítulo11. ProtegendonossaaplicaçãocomSpringSecurity
executarbasicamenteduasfun ções:liberar/negaracessoeexporinforma çõessobre
ousuáriocorrente.
Paratirarproveitodestastags,oprimeiropassoaserdadopeloprogramadoré
declará-lanotopodoarquivoJSPexatamentecomonotrechoaseguir:
<%@taglib prefix="sec"
uri="http://www.springframework.org/security/tags" %>
Delongeatagmaisusadaé <sec:authorize>,queliberaarenderiza çãodo
trechoJSPqueenvolvedeacordocomaspermissõesdefinidasnoatributo access
talcomolistadoaseguir:
<sec:authorize access="isAnonymous()">
<%-- Exibe o formulário de login --%>
</sec:authorize>
<sec:authorize access="isAuthenticated()">
<%-- Exibe conteúdo para o usuário autenticado --%>
</sec:authorize>
Outrataganossadisposi çãoé <sec:authentication/>,queexibiránapá-
ginaovalordapropriedadedoobjeto Authenticationdousuárioautenticado.
Napáginainicialdo Spring Fórum usamosistoparaexporamensagemdeboas
vindaseolinkdelogout,talcomonoexemploaseguir:
<sec:authorize access="isAuthenticated()">
Bem vindo(a) <sec:authentication property="principal"/> -
<a href="<c:url value="/j_spring_security_logout"/>">Sair</a>
</sec:authorize>
11.10 C onclusão
OSpringSecurityéumdosmelhoresexemplospráticosdeaplica çãodaAOP.Como
oleitorpodecomprovarnotranscorrerdestecapítulo,emmomentoalgumprecisa-
mosmodificarnossocódigofonte-comexce çãodainclusãodeumaanota ção-para
controlarseuacesso.Éinteressanteobservartambémquesuaconfigura çãofoifeita
deumaformabastantesimples:aofinalescrevemosalgoemtornode10linhasem
nossoarquivodeconfigura çãoepronto:nossocontroledeacessoestavapronto.
Émuitoimportantequeoleitorprocureporcomponentesdesenvolvidosporter-
ceirosvoltadosaoSpringSecurity.Nãoseriaexageroafirmarquehá90%dechance
249


## Página 260

11.10. Conclusão CasadoCódigo
dealguémjáterescritoumprovedordeautentica çãoqueatendaàssuasnecessida-
desecasoestenãoexista,bom:jávimosqueescreveropróprionãoéumatarefa
difícil.
250


## Página 261

Capítulo12
Eai,gostou?
NotranscorrerdestelivrofoiexpostoobásicoportrásdofuncionamentodoSpring
Framework.Meuprojetoinicialparasuaescritafoidividi-loemduaspartes:napri-
meirameuobjetivofoidescreverosconceitosportrásdaferramenta-inversãode
controle,injeçãodedependências,AOPeoutros-comoeugostariadetê-losconhe-
cidoemumprimeiromomento: expondoasrazõesquejustificamsuaexistência.
Coisasquegostariamuitodeteraprendidonafaculdade.
Nasegundaparteincluíosassuntosquegostariaquetivessemmesidoapresen-
tadosnoambientedetrabalho. OsuporteadadosdoSpringéumbomexemplo:
assimcomodiversosusuáriosdoframework,fiqueianossemtirarproveitodeste
suporteporque,apesardeterouvidofalardesuaexistênciaemlivros,raríssimasve-
zesencontreimaterialquemeapresentasseaquelasfuncionalidadesdeformaclara.
Setiveratingidoosobjetivosacima,dou-meporsatisfeito,porémoseucaminho
noaprendizadodoSpringnãoterminanestasúltimaspáginas,mesmoporqueas
limitaçõesdestelivromeimpediramdeincluirtodasaspossibilidadesexistentes.
Basicamenteoquepossodizeraoleitoré: todaclassepodesertratadacomoum


## Página 262

CasadoCódigo
beannoSpring,oquetornaotrabalhoportrásdaintegra çãodequalquertecnologia
comoframeworkconsisteapenasemsuadeclara çãocomotal.
A meta-prática: o código fonte do livro
Parafacilitaroaprendizadodoleitor, conformeiaescrevendoestelivrode-
senvolviumprojetoparalelochamado Spring Fórum,queaindaébastanterudi-
mentarnomomentoemqueentregueiaversãofinaldestelivroaoseditores-a
quemagrade çopelaincrívelpaciência-masquecontémasaplica çõesreferentes
àtodaasegundapartedolivro. SeucódigofonteestádisponívelnoGitHubem
https://github.com/loboweissmann/spring-forum
Jácomrelaçãoaocódigofontedaprimeirapartedolivro,vocêencontraocódigo
fontedolivronogithub:https://github.com/loboweissmann/spring-forum.
Futuro do Spring
ComopassardotempoéinegávelofatodequeaplataformaJavaEEacabouse
tornandoapadroniza çãodaclássicadobradinha Spring + Hibernate.Muitosleitores
seperguntamportantoseaindavaleàpenadedicar-seaoaprendizadodoSpring.
Seiquesoususpeitoparafalararespeito,masminhaopiniãoéadequesim,éum
aprendizadoválidoecontinuaráasê-lopormuitosanos.
Énosframeworksquesurgemasinova ções. Observandoaevolu çãodaplata-
formaJavaEEpodemosverqueaesmagadoramaioriadas“novidades”quenesta
vãosendoincorporadassãonarealidadeofrutodainfluênciadestesframeworks.E
agrandediferen çaentreseruminovadoreserumpadrãoéqueosegundonormal-
mentesebaseianomenordenominadorcomum,deixandoosrecursosmaisespecí-
ficos-enormalmentemaispoderosos-presentesnafonteoriginal.
Outrarazão,etalvezamaisimportante,sejaofatodoSpringserumaferramenta
disciplinadora. Comelepodemosvernitidamenteopoderdeumaboaabstra ção
atravésdaimplementaçãodeinterfaces,divisãoderesponsabilidades,tudobaseado
noconceitodeinversãodecontrole/inje çãodedependências.Porsisó,mesmoque
oleitorjamaisuseoSpringnaprática,estejájustificariaseuaprendizado.
Obrigado
Prafinalizar,agrade çoaoleitorquetenhachegadoaestaúltimapáginadolivro.
EsperoquecomestetrabalhotenhatornadomaisclarooqueestáportrásdoSpring
(etalvezqualquerframework)ecomotirarproveitodestaferramentaparatornar
252


## Página 263

CasadoCódigo Capítulo12. Eai,gostou?
seutrabalhomaisfácil. Agrade çotambémaoPauloSilveiraeAdrianoAlmeida,
editoresdestetrabalhopelasuapaciência,confian çaededica çãonafinaliza çãodeste
trabalho,poissemestesnadaseriapossível.
Eatéapróxima,poisnãopareiporaqui!:)
253


## Página 265

CasadoCódigo ReferênciasBibliográficas
Referências Bibliográficas
[1] FredBrooks.The Mythical Man-Month.Addison-Wesley.
[2] FredBrooks. Nosilverbullet-essenceandaccidentsofsoftwareengineering.
http://www.cs.nott.ac.uk/~cah/G51ISS/Documents/NoSilverBullet.html.
[3] TimededsenvolvimentodoApacheTiles. Thecompositeviewpattern. http:
//tiles.apache.org/2.2/framework/tutorial/pattern.html,?
[4] RalphJohnsonErichGamma,RichardHelmandJohnVlissides. Design Pat-
terns: Elements of Reusable Object-Oriented Software.Addison-WesleyProfes-
sionalComputingSeries,1994.
[5] MartinFowler. Inversionofcontrolcontainersandthedependencyinjection
pattern.http://martinfowler.com/articles/injection.html,2004.
[6] JesseJamesGarrett. Ajax:Anewapproachtowebapplications. http://www.
adaptivepath.com/ideas/ajax-new-approach-web-applications.
[7] RodJohnson. Expert One-T o-One J2EE Design and Development.WroxPress,
2002.
[8] RodJohnson.Expert One-T o-One J2EE Development Without EJB.WroxPress,
2004.
[9] Martin Lippert. Springsource tool suite 2.9.1 installation instructi-
ons. http://download.springsource.com/release/STS/doc/STS-installation_
instructions.pdf,2012.
[10] Robert C. Martin. The dependency inversion principle. http://www.
objectmentor.com/publications/dip.pdf,1996.
255


## Página 266

ReferênciasBibliográficas CasadoCódigo
[11] Robert C. Martin. Design principles and design patterns. http://www.
objectmentor.com/resources/articles/Principles_and_Patterns.pdf,2009.
[12] BrettMclaughlin.Use a Cabeça - Ajax.AltaBooks.
[13] MarkRichards.Java Transaction Design Strategies.InfoQ,2006.
[14] Spring Source. Spring reference documentation 3.1. http://static.
springsource.org/spring/docs/3.1.x/spring-framework-reference/pdf/
spring-framework-reference.pdf,2012.
[15] SpringSource. Springsource case studies. http://www.springsource.org/
case-studies.
[16] CraigWalls.Spring in Action.Manning,2011.
256
