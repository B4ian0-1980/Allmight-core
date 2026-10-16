---json
{
  "id": "aplica__es_java_para_a_web_com_jsf_e_jpa",
  "title": "Aplicações Java para a web com JSF e JPA",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Aplicações Java para a web com JSF e JPA.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "com",
    "java",
    "jpa",
    "jsf",
    "linguagens",
    "para",
    "web"
  ],
  "perguntas_tipo": [
    "Como utilizar Aplicações Java para a web com JSF e JPA?",
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

# Aplicações Java para a web com JSF e JPA

> **Arquivo Original:** `Aplicações Java para a web com JSF e JPA.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

45326


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
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 3

E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 4

E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 5

CasadoCódigo
Porqueeudevoleresselivroe
comoeleestáorganizado?
Durantemuitotempo,umagrandepartedasaplica çõesqueeramdesenvolvi-
daspossuíamumamesmacaracterística: seremaplica çõesDesktop. Com
isso,plataformascomooVisualBasic,daMicrosoft®eoDelphi,daBorland®,
tornaram-semuitofamosasebatalhavampelograndemercadodedesen-
volvimentodesoftwarequejáhavianaquelaépoca.Comopassardotempo,
algumasdascaracterísticasquetornaramaqueletipodeaplica çãotãointeres-
sante,comoaperformance,come çaramaperderpesofrenteaalgunspontos
negativos,porexemplo,emrela çãoàmanutenibilidadedamesma.Ouseja,
comopossogarantirquetodomundoqueexecuteumaaplica çãoquedesen-
volviestejasemprecomaversãomaisnovadamesma?Claroqueépossível,
masassolu çõespodemnãosernecessariamentesimplesediretas.
Atualmente,asaplica çõesDesktopperderamgrandefatiadomercadode
software.Agora,quemodominasãoasaplica çõesweb,quetentamresolver
algunsdosproblemasexistentescomasaplica çõesDesktop.
NastecnologiasquegravitamaoredordaplataformaJava, épossível
destacarosframeworksMVC,queauxiliamosdesenvolvedoresacriarem
aplicaçõesweb.FrameworkscomooJSF( Java Server Faces),facilitamatarefa
dedesenvolveraplica çãoparaaweb.
Poroutrolado,agrandemaioriadasaplica çõesexistentesprecisa,deal-
gumamaneira,guardarasinforma çõescoletadasdentrodelaemumbanco
dedados.PoderíamosusarJDBCpuroparaessatarefaemnossasaplica ções,
porémtemosdisponíveisferramentasquenosauxiliamacriaraplica çõesque
secomuniquemcomobancodedados.Assim,épossívelabstrairváriasdas
i
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 6

CasadoCódigo
complexidadesexistentesnessaintegra ção,comoéocasodaespecifica ção
JPA.
Nestelivroveremoscomocriarumaaplica çãoutilizandoJSFeJPA.Fare-
mosissocomumaabordagemquemostraanecessidadedecadaitemque
seráintroduzidoaoleitor,eportanto,motivando-o.Acadacapítulo,iremos
aprenderconceitosquepodemfazerevoluiraaplica çãocriada,olhandomais
depertoparaquestõescríticas,comoboaspráticas,performanceecompo-
nentização.Vamossabernãoapenascomofazerouoquefazer,mastambém
omotivodascoisasseremdedeterminadaforma.Oobjetivodesselivronãoé
serumareceitadeboloparaoleitoresim,serummaterialquedesmistifique
asquestõesedúvidasqueexistemnagrandemaioriadasaplica çõesquesão
desenvolvidasparaaweb.
DesenvolvedoressemexperiênciasemdesenvolvimentoparaaWebem
Javaaproveitarãoesselivrodeformaque,paralelamenteàleitura,jáconsigam
irimplementandoseupróprioprojetoecolocandoempráticaosnovoscon-
ceitoseideiasaprendidas. Oobjetivoéque,aofinaldolivro,oleitorsaiba
comocriarumaaplica çãonova,desdeaparteweb,atéo back-endcomasre-
grasdenegócioeacamadadepersistência.Equeconhe çaquaisasarmadilhas
emqueelepodecairecomoselivrardelas,alémdeconseguirutilizarasboas
práticastantodoJSFquantodaJPA.
Paraodesenvolvedorexperiente,olivrocontémdiversosdetalheseboas
práticasquepodemfazeradiferen çanousodasferramentasindicadas.Por
exemplo,comoconfigurarocachedesegundonívelparaaaplica ção,oucomo
otimizaroconsumodasessãodoJSF,entreoutrassitua çõesqueserãoabor-
dadasnodecorrerdaleitura.
Olivroestáestruturadoemtrêspartes,cadaumacomseuobjetivoes-
pecífico:
Naprimeiraparte, teremosoprimeirocontatocomcadaferramenta,
aindasemnospreocuparmosmuitocomcomocadaumafuncionainterna-
mente.OprincipalobjetivoétornarfamiliarofuncionamentogeraldaJPAe
doJSF,mostrandocomointegrá-loseconstruindoumateladecadastrojunto
comacamadadepersistência.
Nasegundaparte,oobjetivoéapresentarasferramentasdeformamais
aprofundada,mostrandocomofuncionamecomousá-lasdaformacorreta.
ii
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 7

CasadoCódigo
Éumconteúdoútiltantoparaquemteveoprimeirocontatonaprimeiraparte
dolivro,quandoparaquemjádesenvolvehámuitotempo,masnuncatevea
oportunidadedeexplorarasferramentasapontodesabercomoelassecom-
portamemsitua çõesespecíficas.
Naterceiraeúltimaparte,veremoscomomelhorarnossaaplica çãoem
cimadoconhecimentoadquiridonasegundaparte.Ofocoéprincipalmente
usabilidadeeperformance.Exploraremostemasqueforamvistosnasegunda
parte,comoAJAXnoJSFe Lazy LoadnaJPA,mascomenfoquemuitomais
específicoemtiraromáximoproveitodasferramentas.
iii
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 8

E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 9

CasadoCódigo
Agradecimentos
Podemconsiderarclichê,masnãohácomoiniciarqualquertipodeagradec-
imentosemprimeiroagradeceraDeus,poissemelenãoestariaaquiagrade-
cendoaoutraspessoasmuitoimportantes,tantonaminhavida,quantona
escritadestelivro.
Gostariadeagradeceraosmeuspais,JoséCordeirodeSouzaeCleunice
dosSantosCordeiro,pelacria ção,pelosvaloresepeloincentivoemtodos
osmomentosdaminhavida. Desdeastarefasdaescola,cafésfeitosaltas
horasdanoiteparaaguentaramadrugadadetrabalhosdafaculdadeeagora
osperíodosde“entocamento”paraescreverestelivro.
Aindanase çãofamília,nãopoderiadeixardeagradecerminhairmã,
GisellySantosCordeiro,porserumexemplodeestudosededica çãoemuma
épocaemqueeuandavameiopregui çoso.
Um agradecimento muito especial à minha namorada, quase esposa,
DantieledeFreitasQueirózquetemsidoumaverdadeiraparceiranessesoito
anosqueestamosjuntos.Issomesmo,oitoanosdenamoro:).Agrade çopela
companhianosmomentosdescontraídos,masprincipalmentepelaparceria
nosmomentosdemuitotrabalhoeestudo.Sãomesessempodercurtirum
finaldesemanatranquilo,semsairparapescar,ouficarhorasfazendoqual-
queroutracoisa.Emvezdereclamar,eraeuescrevendoemumaescrivaninha
eelaestudandoemoutra.
Agradeçotambémaosmeussogros,WanderleyeIraci,poisquandoes-
tavanacasadeles,alémdeficarnomeucantoescrevendo,aindacarregavaa
filhadelescomigo.Eapesardetodabrincadeiraquesefazcomsogroesogra,
elessempreforampaizõescomigo.
Enãopoderiaterminaressalistasemagradeceradoiscarasemespecial:
v
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 10

CasadoCódigo
PauloSilveiraeAdrianoAlmeida.PrimeiramenteaoPaulopelaconfian çae
peloconvitedeescreverumlivro,algoqueeununcatinhafeito.Admiroessa
capacidadedeleemtransformarconhecimentoemalgopalpável,primeiro
comoGUJ,depoisaCaelumeagoraaCasadoCódigo.Etambémummuito
obrigadoaoAdriano,queteveodurotrabalhodetransformarquilosdetre-
chosdecódigoeexplica çãotécnicaemalgoleveeprazerosodeler.Semele
comoeditor,emvezdeumlivro,teriaescritoumpostgigantedeblog.
vi
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 11

CasadoCódigo Sumário
Sumário
Contatoinicial 1
1 Introdução 3
1.1 Aevolu çãodaintegra çãoentreJavaeBancosdedados. . . . 4
1.2 ComoeraavidacomoJDBC?. . . . . . . . . . . . . . . . . . 6
1.3 Diminui çãodaimpedânciaatravésdomapeamento . . . . . 9
1.4 BibliotecasORMeoHibernate . . . . . . . . . . . . . . . . . 10
1.5 MuitosframeworksORM,comoevitarovendorlock-in? . . 12
1.6 OdesenvolvimentowebcomServletseopadrãoMVC . . . 14
1.7 TirandoHTMLdocódigoJavacomasJavaServerPages . . . 17
1.8 Organizeseucódigocomasepara çãoderesponsabilidades . 18
1.9 OMVCeosframeworks . . . . . . . . . . . . . . . . . . . . . 18
1.10 PorqueusarJSF?. . . . . . . . . . . . . . . . . . . . . . . . . . 23
1.11 OprimeirocontatocomoJSF . . . . . . . . . . . . . . . . . . 23
1.12 Nospróximoscapítulos . . . . . . . . . . . . . . . . . . . . . . 26
2 PrimeirospassoscomaJPA 27
2.1 Defini çãodomodelo . . . . . . . . . . . . . . . . . . . . . . . 27
2.2 Configura çãobásicadopersistence.xml . . . . . . . . . . . . 29
2.3 Escolhaodialetodobancodedados . . . . . . . . . . . . . . 32
2.4 Automatiza çãodacria çãoeevolu çãodastabelas . . . . . . . 33
2.5 Grava çãodoprimeirodadonobancodedados . . . . . . . . 34
2.6 ConsultassimplesnobancodedadoscomaJPA . . . . . . . 39
2.7 ExclusãodedadoscomaJPA . . . . . . . . . . . . . . . . . . 40
2.8 Oquemaisvempelafrente? . . . . . . . . . . . . . . . . . . . 42
vii
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 12

Sumário CasadoCódigo
3 PrimeirospassoscomoJSF 43
3.1 OndeecomodefinotelascomoJSF? . . . . . . . . . . . . . . 43
3.2 Cria çãodatelaedosinputsbásicosdedados . . . . . . . . . 45
3.3 commandButton,ManagedBeanseasubmissãodeformulários 48
3.4 PassedadosdatelaparaoManagedBean . . . . . . . . . . . 50
3.5 Comoreceberosparâmetrosdiretonométodo . . . . . . . . 55
3.6 Grava çãodoautomóvelnobancodedados . . . . . . . . . . 56
3.7 ListeosdadoscomodataTable. . . . . . . . . . . . . . . . . . 57
3.8 Mas minha listagem está executando várias consultas no
banco... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.9 ExclusãodedadoseocommandLink. . . . . . . . . . . . . . 64
3.10 OprimeiroCRUDintegrado. . . . . . . . . . . . . . . . . . . 66
Domineasferramentas 67
4 EntendendoaJPA 69
4.1 OpadrãodeprojetosDataAccessObject,ouDAO . . . . . . 70
4.2 JPAnãoéumDAOgenérico,écontextual . . . . . . . . . . . 71
4.3 CiclodevidadeumobjetonaJPA. . . . . . . . . . . . . . . . 73
4.4 AJPAvaimaisalémdoqueumsimplesexecutardeSQLs. . 77
5 Comomapeartudo...ounada! 79
5.1 Defini çõesdeentidade . . . . . . . . . . . . . . . . . . . . . . 81
5.2 Fa çaatributosnãoserempersistidoscomo@Transient . . . 83
5.3 Mapeiechavesprimáriassimples . . . . . . . . . . . . . . . . 84
5.4 Mapeiechavescompostas. . . . . . . . . . . . . . . . . . . . . 88
5.5 Aanota ção@Basic. . . . . . . . . . . . . . . . . . . . . . . . . 93
5.6 @Table,@Columne@Temporal. . . . . . . . . . . . . . . . . 94
5.7 @Versionelockotimista . . . . . . . . . . . . . . . . . . . . . 96
5.8 Relacionamentosmuitosparaumcom@ManyToOne . . . . 98
5.9 @OneToOne . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
5.10 Relacionamentosbidirecionais. . . . . . . . . . . . . . . . . . 101
viii
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 13

CasadoCódigo Sumário
5.11 Oquetemaverodonodorelacionamentocomaopera ção
emcascata? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
5.12 Organizemelhorsuasentidadesepromovareaproveitamento
com@Embeddablee@Embedded . . . . . . . . . . . . . . . 108
5.13 Relacionamentos um para muitos com o @OneToMany e
@ManyToOne . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
5.14 AimportânciadoLazyLoading,ocarregamentopregui çoso 115
5.15 @Lob . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
5.16 @ElementCollection. . . . . . . . . . . . . . . . . . . . . . . . 118
5.17 Relacionamentosmuitosparamuitoscomo@ManyToMany 119
5.18 Customizeascolunasderelacionamentoscom@JoinColumn
e@JoinColumns . . . . . . . . . . . . . . . . . . . . . . . . . . 121
5.19 Configureastabelasauxiliarescom@JoinTable . . . . . . . . 123
5.20 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
6 ConsultascomaJPQLeosproblemascomunsnaintegra çãocom
oJSF 125
6.1 FiltredadoscomaJavaPersistenceQueryLanguage-JPQL. 126
6.2 Comoaplicarfun çõesnasconsultas. . . . . . . . . . . . . . . 127
6.3 Ondeestãomeusjoins? . . . . . . . . . . . . . . . . . . . . . . 129
6.4 Executesuasconsultaseuseparâmetros . . . . . . . . . . . . 131
6.5 Utilizefun çõesdeagrega ção . . . . . . . . . . . . . . . . . . . 132
6.6 Fa çasub-consultascomaJPQL . . . . . . . . . . . . . . . . . 133
6.7 AgrupamentoseHAVING . . . . . . . . . . . . . . . . . . . . 133
6.8 Consultascomplexas...resultadoscomplexos?. . . . . . . . . 134
6.9 UseoSelectNeweesque çaosarraysdeObject . . . . . . . . 135
6.10 OrganizesuasconsultascomNamedQueries . . . . . . . . . 136
6.11 ExecuteasNamedQueries . . . . . . . . . . . . . . . . . . . . 139
6.12 RelacionamentosLazy,N+1QueryeJoinFetch . . . . . . . . 140
6.13 EviteaLazyInitializationExceptioncomoOpenEntityMan-
agerInView . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
6.14 OproblemadasN+1consultasecomoresolvê-lo . . . . . . . 145
6.15 Foibastante,masnãoacabou... . . . . . . . . . . . . . . . . . 147
ix
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 14

Sumário CasadoCódigo
7 EntendaoJSFecrieaplica çõesweb 149
7.1 Seprepareparaummundodiferente,baseadoemcomponentes150
7.2 Awebstatelesscontraawebstateful . . . . . . . . . . . . . . 150
7.3 Ociclodevidadasrequisi çõesnoJSF. . . . . . . . . . . . . . 153
7.4 Fase1-Criarourestauraraárvoredecomponentesdatela
(RestoreView) . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
7.5 Fase2-Aplicarvaloresdarequisi çãonaárvoredecompo-
nentes(ApplyRequestValues) . . . . . . . . . . . . . . . . . . 154
7.6 Fase3-ConvertereValidar(Validate) . . . . . . . . . . . . . 155
7.7 Fase4-Atualizaromodelo(UpdateModel). . . . . . . . . . 156
7.8 Fase5-Invocara çãodaaplica ção(InvokeApplication) . . . 156
7.9 Fase6-Renderizararesposta(RenderResponse). . . . . . . 157
7.10 AjasobreasfasesdoJSFcomosPhaseListeners. . . . . . . . 159
7.11 ConheçaoscomponentesdoJSF . . . . . . . . . . . . . . . . 161
7.12 h:form. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
7.13 h:inputTexteh:inputTextarea . . . . . . . . . . . . . . . . . . 163
7.14 h:inputSecret . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
7.15 h:inputHidden . . . . . . . . . . . . . . . . . . . . . . . . . . . 164
7.16 h:selectOneMenu,f:selectItemef:selectItems . . . . . . . . . 164
7.17 h:selectOneRadio . . . . . . . . . . . . . . . . . . . . . . . . . 165
7.18 h:selectOneListbox . . . . . . . . . . . . . . . . . . . . . . . . 166
7.19 h:selectManyMenueh:selectManyListbox . . . . . . . . . . . 167
7.20 h:selectManyCheckbox . . . . . . . . . . . . . . . . . . . . . . 168
7.21 h:selectBooleanCheckbox. . . . . . . . . . . . . . . . . . . . . 169
7.22 NovidadedoJSF2.2:h:inputFile. . . . . . . . . . . . . . . . . 170
7.23 h:panelGrid. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
7.24 h:panelGroup. . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
7.25 h:outputText . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
7.26 h:outputLabel. . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
7.27 h:outputFormat . . . . . . . . . . . . . . . . . . . . . . . . . . 174
7.28 h:outputScripteh:outputStylesheet . . . . . . . . . . . . . . . 174
7.29 h:graphicImage. . . . . . . . . . . . . . . . . . . . . . . . . . . 175
x
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 15

CasadoCódigo Sumário
7.30 h:dataTable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
7.31 ui:repeat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
7.32 h:commandButtoneh:commandLink . . . . . . . . . . . . . 178
7.33 AdiferençaentreActioneActionListener . . . . . . . . . . . 179
7.34 Padronizaçãonocarregamentoderecursos . . . . . . . . . . 181
7.35 Entenda os conversores nativos, o f:convertDateTime e o
f:convertNumber. . . . . . . . . . . . . . . . . . . . . . . . . . 184
7.36 Conversorescustomizados . . . . . . . . . . . . . . . . . . . . 186
7.37 Conheçaosvalidadoresnativos . . . . . . . . . . . . . . . . . 189
7.38 Equandoosvalidadoresnativosnãofazemoqueeuquero?
Crieseusvalidadores . . . . . . . . . . . . . . . . . . . . . . . 194
7.39 Novidade:JSFcomGETebookmarkableURLs. . . . . . . . 198
7.40 h:buttoneh:link . . . . . . . . . . . . . . . . . . . . . . . . . . 198
7.41 Regrasdenavega ção. . . . . . . . . . . . . . . . . . . . . . . . 201
7.42 Entendaosescoposesaibacomoequandotrabalharcom
cadaum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
7.43 AcurvadeaprendizadodoJSF . . . . . . . . . . . . . . . . . 211
8 ValidaçõessimplificadasnaJPAenoJSFcomaBeanValidation 213
8.1 Trabalhecomosvalidadoresecriesuaprópriavalida ção . . 214
8.2 Organizegruposdevalida ção . . . . . . . . . . . . . . . . . . 216
8.3 Aintegra çãoentreBeanValidationeJPA. . . . . . . . . . . . 217
8.4 Aintegra çãoentreBeanValidationeJSF . . . . . . . . . . . . 219
Desenvolvendoafluência 221
9 Enriquecendonossaaplica çãoJSF 223
9.1 CombosemcascataecommandsemdataTable . . . . . . . . 224
9.2 Mostremensagenscomh:messageeh:messages. . . . . . . . 229
9.3 Internacionalizandonossaaplica ção . . . . . . . . . . . . . . 235
9.4 JSFeAjax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
9.5 Organizeocódigodastelascomtemplates. . . . . . . . . . . 246
xi
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 16

Sumário CasadoCódigo
9.6 CompositeComponents: criandonossospróprioscompo-
nentesapartirdeoutros . . . . . . . . . . . . . . . . . . . . . 252
9.7 Criarumjarcomcomponentescustomizados. . . . . . . . . 261
10 Truquesquepodemaumentaraescalabilidadeeaperformanceda
suaaplica ção 263
10.1 UtilizeocachedesegundoníveldaJPA . . . . . . . . . . . . 264
10.2 Façacachedeconsultas . . . . . . . . . . . . . . . . . . . . . . 270
10.3 Colhendoestatísticasdanossacamadadepersistência . . . . 274
10.4 Relacionamentosextra-lazy . . . . . . . . . . . . . . . . . . . 277
10.5 Paginaçãovirtualerealdedados . . . . . . . . . . . . . . . . 280
10.6 UtilizandoPooldeconexões . . . . . . . . . . . . . . . . . . . 285
10.7 TornandooJSFmaislevecomusointeligentedeAJAX . . . 288
10.8 Quandopossível,manipulecomponentesJSFnoladodocliente291
10.9 Consideraçõesfinaissobreotimiza ções. . . . . . . . . . . . . 293
11 Conclusão 295
12 Apêndice:iniciandoprojetocomeclipse 299
12.1 Adicionandootomcatnoeclipse . . . . . . . . . . . . . . . . 299
12.2 Criandooprojetoweb . . . . . . . . . . . . . . . . . . . . . . 301
12.3 BaixandoosjarsdoJSF . . . . . . . . . . . . . . . . . . . . . . 304
12.4 ConfigurandoaJPA . . . . . . . . . . . . . . . . . . . . . . . . 305
ÍndiceRemissivo 309
Bibliografia 309
Versão:17.9.26
xii
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 17

ParteI
Contatoinicial
Nessaprimeirapartedolivroteremosoprimeirocontatocomcadafer-
ramenta,aindasemnospreocuparmosmuitocomofuncionamentointerno
decadauma.
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 18

E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 19

Capítulo1
Introdução
Nestecapítuloinicial,veremosumpoucodahistóriaportrásdessasduasbib-
liotecas,JPAeJSF.Qualocaminhopercorridoatéchegarmosnoquetemos
hoje?Quaisproblemasessasferramentasvieramsolucionar?Emtodososca-
sos,consideraremosodesenvolvimentoorientadoaobjetos.Adiscussãodos
benefíciosdaorienta çãoaobjetosétemadediversoslivrosenãoentraremos
nessemérito.TantoJPAquantoJSFsãoferramentasparaprojetosparaesse
paradigma. Veremosagoracomocadaumadelascolaboraparaumdesen-
volvimentomaisprodutivo.
Paraquefiquemaissimplesacompanharosexemplosdolivro,olheo
capítulo12,queéumapêndicemostrandotodaamontagemdoambienteuti-
lizandoaIDEeclipse.Alémdisso,ocódigodolivroestádisponívelnogithub:
https://github.com/gscordeiro/faces-motors.
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 20

1.1. Aevoluçãodaintegra çãoentreJavaeBancosdedados CasadoCódigo
1.1 Aevolução da integração entre Jav a eBan-
cos de dados
Agrandemaioriadasaplica çõesconstruídasatualmente,dealgumamaneira,
necessitaseintegrarcomumbancodedadosrelacionaldisponibilizadoem
umservidor.Essebancodedados,costumeiramente,eracriadobaseadoem
umamodelagem,comoporexemplo,odiagramaentidade-relacionamento.
Dessaforma,facilitava-seavisualiza çãodetodasasentidadesquehaveriana
aplicação,bemcomoaanálisedetodoocontextoqueaenglobaria.
Comisso,podemosmodelarumaaplica çãodecompraevendadeau-
tomóveis. Noentanto,paranãonosperdermosnosrequisitosdaaplica ção
emantermosofoconasferramentas,vamosnosconcentrarbasicamenteno
cadastroenarecupera çãodosdadosde Marca, Modeloe Automovel.
Fig.1.1:Diagramaentidade-relacionamentodeMarca,ModeloeAutomovel
Enquantoisso,nomundoorientadoaobjetos,estamosacostumadosa
representarasentidadesenvolvidasnaaplica çãopormeiodeumoutrodia-
grama. Nessecaso,pelodiagramadeclasses,quepossuiomesmoobjetivo
damodelagementidade-relacional:permitirumavisualiza çãodaaplica ção
numcontextoglobaledecomotodasasclassesinteragementresi.
Umapossívelabordagemparamodelaraaplica çãoilustradanaimagem
1.1podeservistanafigura1.2.
4
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 21

CasadoCódigo Capítulo1. Introdução
Fig.1.2:DiagramadasclassesMarca,ModeloeAutomovel
Apesardeseremvoltadosaparadigmasdiferentes,épossívelnotaralgu-
massimilaridadesentreambososdiagramas.Sendoassim,qualadificuldade
demapearmosnossomodeloorientadoaobjetosparaobancodedadosrela-
cional?
Umapossíveldiferen çaéquenomodeloorientadoaobjetostemosas
classes Automovel, Modeloe Marca. Essasclassespossuem-alémdas
propriedadessimples,comonome,descri çãoepre ço-relacionamentoumas
comasoutras.Umexemplodissoéoautomóvelqueestáligadoaummodelo,
queestáligadoaumamarca. Jáomodeloentidade-relacionamentomostra
umautomóvelquetemumiddeummodeloqueporsuaveztemoidde
umamarca.Adiferen çaparecesutilaoanalisarmos,masnapráticatorna-se
grandeepodesetornarbastantetrai çoeira.
NomundoOO,objetosnãocarregam idsdeoutrosobjetos,elespossuem
umvínculocomooutroobjetointeiro. Dessamaneira,umobjetopodeter
listasdeoutrosobjetoseatéestruturasdedadosmaiscomplexas,formadas
poroutrasclasses.
Quandovamospersisti-losemumbancodedadosrelacional,precisamos
ajustarasdiferen çasexistentesentreambososmodelos. Some-seaissoo
fatodequenaorienta çãoaobjetospossuímosheran ça,polimorfismo,com-
posiçãoediversasoutrascaracterísticasquenãoestãopresentesnomod-
elorelacional. Aessasdiferen çasfundamentaisdaformadosobjetosno
mundoorientadoaobjetosenomundorelacional,chamamosde Impedân-
ciaObjeto-Relacional(Impedance Mismatch).
5
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 22

1.2. ComoeraavidacomoJDBC? CasadoCódigo
1.2 Como era a vida com o JDBC?
Durantealgumtempo,aprincipalferramentaquepermitiaaosdesenvolve-
doresintegraremseuscódigosJavacomobancodedados,possibilitandoa
manipulaçãodasinforma çõesneles,eraa API JDBC(Java Database Connec-
tivity).Elaconsistedeumconjuntodeclasseseinterfacesqueprovêemuma
formadeacessoaosbancosdedados,introduzidasatravésdosconhecidos
drivers,necessáriosparaaintegra çãocomobancodedados.
Esses driversfazemacomunica çãoentreanossaaplica çãoeobancode
dados,comunicando-seemumprotocoloqueoprópriobancoentenda.
Considerandoumaentidadechamada Automovel,quecontémalgumas
informaçõescomoonome,anodefabrica çãoecor,podemosterumaclasse
Javaquearepresenta:
public class Automovel {
private Long id;
private Integer anoFabricacao;
private String modelo;
private Integer anoModelo;
private String marca;
private String observacoes;
// getters e setters se necessário
}
Nessa mesma aplicação, podemos ter uma interface que determina
quaisopera çõespodemserrealizadasnobancodedados,apartirdeum
Automovel. Essainterfaceseráimplementadaporclassescujoúnicoob-
jetivoécuidardapersistênciadasinforma çõesesãoconhecidascomoDAO
(Data Access Object).
public interface AutomovelDAO {
void salva(Automovel a);
List<Automovel> lista();
}
6
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 23

CasadoCódigo Capítulo1. Introdução
Então, podemostercomoimplementa çãodessainterface, umaclasse
chamada JDBCAutomovelDAO, que implemente os métodossalva e
lista.
public class JDBCAutomovelDAO implements AutomovelDAO {
public void salva(Automovel a) {
// código para salvar vem aqui
}
public List<Automovel> lista() {
// código para listar vem aqui
}
}
Paraimplementarométodosalvar,atravésdoJDBC,éprecisoabrira
conexãocomobancodedados,escreveroSQLqueiráexecutar,passaros
dadosdoobjetoparaaqueryqueseráfeitaeassimpordiante.Umapossível
implementaçãoparaométodo salvaéaseguinte:
@Override
public void salva(Automovel automovel) {
String sql = "insert into automoveis " +
"(anoFabricacao, anoModelo, marca, modelo, observacoes)" +
" values (?, ?, ?, ?, ?)";
Connection cn = abreConexao();
try {
PreparedStatement pst = null;
pst = cn.prepareStatement(sql);
pst.setInt(1, automovel.getAnoFabricacao());
pst.setInt(2, automovel.getAnoModelo());
pst.setString(3, automovel.getMarca());
pst.setString(4, automovel.getModelo());
pst.setString(5, automovel.getObservacoes());
pst.execute();
7
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 24

1.2. ComoeraavidacomoJDBC? CasadoCódigo
} catch (SQLException e) {
throw new RuntimeException(e);
} finally {
try {
cn.close();
} catch (SQLException e) {
throw new RuntimeException(e)
}
}
}
Nessecódigoépossívelobservardiversascomplexidades,comootrata-
mentoobrigatóriodaSQLExceptionemdoismomentosearepetitivainvo-
caçãodosmétodos setInte setStringparamontarocomando.
Podemosiralémeveraimplementa çãodométodo lista,cujoobje-
tivoéfazerumaconsultanobancodedadosparadevolveruma Listde
Automovel.
public List<Automovel> lista() {
List<Automovel> automoveis = new ArrayList<Automovel>();
String sql = "select * from Automovel";
Connection cn = abreConexao();
try {
PreparedStatement pst = cn.prepareStatement(sql);
ResultSet rs = pst.executeQuery();
while( rs.next() ) {
Automovel automovel = new Automovel();
automovel.setId(rs.getLong("id"));
automovel.setAnoFabricacao(rs.getInt("anoFabricacao"));
automovel.setAnoModelo(rs.getInt("anoModelo"));
automovel.setMarca(rs.getString("marca"));
automovel.setModelo(rs.getString("modelo"));
automovel.setObservacoes(rs.getString("observacoes"));
automoveis.add(automovel);
}
} catch (SQLException e) {
throw new RuntimeException(e);
} finally {
8
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 25

CasadoCódigo Capítulo1. Introdução
try {
cn.close();
} catch (SQLException e) {
throw new RuntimeException(e)
}
}
return automoveis;
}
Esse código é ainda mais complexo que o da gravação de um novo
Automovel. Issosedeveaofatodequeaquiprecisamosretirarosdados
dobancodedados,quefoidevolvidono ResultSet,eatribuí-losaoobjeto
automovelcriadodentrodo while.
Notequeescrevemosocódigoquetrabalhatantocomaorienta çãoaob-
jetoseorelacional,transformandoodadoqueéadequadoemumdelespara
ooutro,fazendoosajustesnecessários.
Claro,oexemplomostradoétrivial,poiséumasimplesopera çãodecon-
sultaeinser ção. Porém,comoexercício,imagineseaconsultadevolvesse
informaçõesde3tabelasdiferentes,pormeiodarealiza çãodeopera çõesde
joins-aimpedâncianessecasoficariamaisevidenteainda.
FazeressaconversãodomundoOOparaorelacionalcadavezquepre-
cisamossalvarourecuperarqualquerobjetodobancodedadosexigetantoes-
forçodedesenvolvimento,queacabamosgastandoalgumaenergiacomalgo
quenãoéoobjetivofinaldosistema. Nãoseriamuitomelhorseessainte-
graçãoentreosdoisparadigmasjáestivesseprontaenãoprecisássemosnos
preocuparcomela?
1.3 Diminuição da impedância através do ma -
peamento
Vimosque,quandotrabalhamoscomoJDBC,misturamosdoisparadigmas
diferentesnaaplica çãoJava:oorientadoaobjetoseorelacional.Masnãoseria
maisinteressanteseutilizássemos umsóparadigma e,magicamente,oque
fizéssemosnelefosserefletidonooutro?Foijustamentecomesseintuitoque
começaramasurgirbibliotecasparapermitirque,emvezdemisturarmoso
9
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 26

1.4. BibliotecasORMeoHibernate CasadoCódigo
paradigmarelacionalnonossocódigoJava,possamosapenasnospreocupar
comobjetos.Algocomo:
public void salva(Automovel automovel) {
conexao.save(automovel);
}
Nocódigoanterior,reparequeapenastrabalhamoscomobjetoseque,
quando invocado, o métodosave se encarrega de fazer todo o SQL
necessário,comosrelacionamentosnecessáriosparanós.Muitomelhor,não?
Mascomoométodo savesabeemqualtabelao insertteráqueser
feito? QuaiscolunasterãoqueseradicionadasaoSQL?Qualéo datatype
decadaumadascolunas? Essassãoalgumasdasquestõesquepodemvirà
mentenesseinstante.
Dealgumamaneira,eleprecisaráteressainforma ção. Ouseja,deverá
haverumaformadeindicarqueobjetosdaclasse Automovelterãoregistros
inseridosnatabela automoveis.Essadefini çãochamamosdemapeamento,
quenocaso,éumaliga çãofeitaentreosdoismodelosdiferentes,orelacionale
oorientadoaobjetos.Temos,então,o Mapeamento Objeto Relacional(Object
Relational Mapping - ORM).
1.4 BibliotecasORM e oHibernate
Bibliotecasquefazemotrabalhodescritoacimachamamosdeframeworks
ORM. Temos diversas implementações desses frameworks a disposição,
comooEclipseLink,Hibernate,OpenJPAentreoutros.Dentreesses,muito
provavelmente,omaisfamosoemaisusadoéoHibernate.
Com ele, é possível indicar que umAutomovel vai poder ser
persistido no banco de dados, somente pela introdução da anotação
@javax.persistence.Entitynaclasse:
@Entity
public class Automovel {
private Long id;
10
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 27

CasadoCódigo Capítulo1. Introdução
private Integer anoFabricacao;
private String modelo;
private Integer anoModelo;
private String marca;
private String observacoes;
// getters e setters se necessário
}
Além disso, podemos indicar qual dos atributos representa a chave
primáriadatabela. Nocaso,éoatributo id,bastandoanotá-locom @Id
e GeneratedValuecasoqueiramosumvalorauto-incrementoparaele.
Duranteolivroaprenderemosocompletosignificadodessasanota çõesede
váriasoutras:
@Id @GeneratedValue
private Long id;
Pronto,issofeito,bastapersistiroobjetoatravésdopróprioHibernate.
Paraisso,podemosimplementarnovamenteainterface AutomovelDAO,
porémagora,paraoHibernate.
public class HibernateAutomovelDAO implements AutomovelDAO {
public void salva(Automovel a) {
Session s = abreConexao();
Transaction tx = s.beginTransaction();
s.save(a);
tx.commit();
s.close();
}
public List<Automovel> lista() {
Session s = abreConexao();
List<Automovel> automoveis =
s.createQuery("from Automovel").list();
11
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 28

1.5. MuitosframeworksORM,comoevitarovendorlock-in? CasadoCódigo
s.close();
return automoveis;
}
}
Notecomoocódigoanterior,utilizandoHibernate,éextremamentemais
simplesqueoescritopreviamentecomJDBC.Empoucaslinhasdecódigo
atingimosomesmoresultado.Claroquealgumascoisasaindaparecemmeio
mágicaseoutrasaindapodemsermelhoradasnessecódigo,comootrata-
mentodastransa ções,ummelhorlugarparaofechamentoda Session,que
éumaespéciedeconexãodoHibernate,eassimpordiante.Maisparaafrente
aprenderemosessasmelhorespráticas,técnicasedetalhesdousodoframe-
work.
Aoexecutarométodoquerealizaabuscadeautomóveisdobancode
dados,oseguintecódigoSQLédisparado:
select automovel0_.id as id0_, automovel0_.anoFabricacao as
anoFabri2_0_, automovel0_.anoModelo as anoModelo0_,
automovel0_.marca as marca0_, automovel0_.modelo as modelo0_,
automovel0_.observacoes as observac6_0_
from Automovel automovel0_
Apesar de parecer um pouco estranho, esse comando é apenas um
selectquediscriminaascolunasquedeverãoserbuscadasnobanco,uma
auma.
1.5 Muitos frameworks ORM, como evitar o
vendor lock-in?
Apartirdomomentoemqueosdesenvolvedoresperceberamqueosframe-
worksORMpoderiamaumentaraprodutividadeefacilitarodesenvolvi-
mentodeaplica ções, muitasbibliotecascomooHibernatesurgiram, en-
quantooutrasquejáexistiamserviramdeinspira çãoparaopróprioHiber-
nate.
12
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 29

CasadoCódigo Capítulo1. Introdução
Dessaforma,chegou-seaumcenárioemqueexistiammuitasbibliote-
caspararesolveromesmoproblema,mascadaumafazendootrabalhoàsua
maneira.Portabilidadepassouaserumproblema,jáquesevocêusassequal-
querumabiblioteca,elanãoseriacompatívelcomoutrasquejáexistiamno
mercado.Issocriavaofamoso vendor lock-in,ouseja,umavezusandodeter-
minadadistribui ção,ficava-sepresoàmesma.
Justamentecomointuitoderesolveressasitua ção,em2006,foicriada
umaespecifica çãoparaasbibliotecasORM,nocaso,a Java Persistence API -
JPA.Essanovaespecifica çãonãorepresentougrandesaltera çõesnaformade
usarumORM,paraquemjáestavaacostumadocomoHibernate.Entrealgu-
maspoucasdiferen ças,destacam-seosnomesdosmétodosedasclassesque
devemserusadas.AdaptandooDAOanteriormentecriadoparaoHibernate,
paraaJPA,teremososeguintecódigo:
public class JPAAutomovelDAO implements AutomovelDAO {
public void salva(Automovel a) {
EntityManager em = abreConexao();
em.getTransaction().begin();
em.persist(a);
em.getTransaction().commit();
em.close();
}
public List<Automovel> lista() {
EntityManager em = abreConexao();
List<Automovel> automoveis =
em.createQuery("select a from Automovel a")
.getResultList();
em.close();
return automoveis;
}
}
13
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 30

1.6. OdesenvolvimentowebcomServletseopadrãoMVC CasadoCódigo
Reparenocódigoquehouveapenasalgumasmudan çasdenomescomre-
laçãoaousodoHibernate.Porexemplo, Sessionvirou EntityManager,
ométodo save,naJPAé persisteoutrospequenosdetalhes.
NospróximoscapítulosvamosaprenderausaraJPA,atravésdoHiber-
natecomoimplementa ção,alémdeverquaisasmelhorespráticasparainte-
grarambasastecnologiascomumaaplica çãoweb.
1.6 O desenvolvimento web com Servlets e o
padrão MVC
Comapopulariza çãodasaplica çõesweb,muitasplataformasganharampop-
ularidade,comofoiocasodoPHPedoASP,enãodemorouparaqueoJava
tambémsuportassedealgumamaneiraodesenvolvimentoweb.
A infraestrutura para desenvolvimento Web em Java é baseada em
Servlets.Hojechamamosdeinfraestrutura,mas,nosprimórdios,elaseram
usadasdiretamenteparadesenvolveraplica ções.
UmaServletéumaclasseJavaqueficanoservidoreéinvocadacom
baseemalgumpadrãodeURL.Porexemplo,vamosconsiderarquetemos
umaaplica çãodecadastrodeveículosexecutandolocalmentenoendere ço
http://localhost:8080/automoveis.Nessaaplica ção,entreváriasServlets,vamos
destacaruma:
•/visualizar?id=<id do automóvel> -mostraparaousuárioos
dadosdeumdeterminadoautomóvel;
OcódigodessaServetpodesersimilarao:
@WebServlet(urlPatterns="/visualizar")
public class VisualizaAutomovelServlet extends HttpServlet {
protected void doGet(HttpServletRequest req,
HttpServletResponse res)
throws IOException, ServletException {
AutomovelDAO dao = new AutomovelDAO();
Automovel auto =
14
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 31

CasadoCódigo Capítulo1. Introdução
dao.busca(request.getParameter("id"));
PrintWriter out = res.getWriter();
out.println("<html>");
out.println("<body>");
out.println("Modelo: " + auto.getModelo()
+ "<br />");
out.println("Ano do Modelo: "
+ auto.getAnoModelo()
+ "<br />");
out.println("</html>");
out.println("</body>");
}
}
15
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 32

1.6. OdesenvolvimentowebcomServletseopadrãoMVC CasadoCódigo
Fig.1.3:Fluxodeexecu çãoondetudoficanaServlet
NotecomoescrevemosocódigoHTMLdentrodanossaclasseJava.Bem
estranho,não?Eopioréacomplexidadenamanuten çãodisso.Imagineque
precisássemosdevolverumarespostamaiselaboradaparaocliente,comCSS
eJavascriptmisturadosnessaresposta.Ficariaquaseimpossívelmanteresse
código.
Evidentementequeessaformadedesenvolveraplica çõesapresentavários
problemasetalvezomaisclarosejaapresen çadeHTMLdentrodeumcódigo
Java.Umaalternativaparasolucionaresseproblemafoijustamenteos JSPs.
16
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 33

CasadoCódigo Capítulo1. Introdução
1.7 Tirando HTML do código Jav a com as
Jav aServerPages
AsJSPs,sãopáginasHTMLquepodemterdentrodesitrechosdecódigoJava.
Comoemumprojetoreal,aquantidadedeHTMLdentrodeumaServletseria
muitomaiordoqueovistonosexemplosanteriores,enapráticaocódigoJava
deverdade(enãooqueescreviaHTML)eraexce ção.ComasJSPsemvezde
teralgoparecidocomoservletquerespondiapor /visualizar,poderíamoster
umapáginacomovistoaseguir.
<html>
<body>
Modelo: <%= req.getAttribute("modelo") %>
Ano do Modelo: <%= req.getAttribute("anoModelo") %>
</body>
</html>
Vejacomonossocódigoagorapareceumelhor.Agoraapropor çãoparece
estarmaiscorreta,sendooHTMLaregraeoJavaaexce ção.NasJSPstemos
apossibilidadedaescritadiretadoHTML,quealémdedeixarocódigomais
legível,deixa-omaismanutenível.
Apesardanotóriamelhoria,namisturaentreHTMLeJavapermanece-
ram,atravésdosScriptlets,aquelesestranhossinaisde <% %>.Issoprovocou
osurgimentodetécnicasparaeliminaressecódigoJavadavisualiza çãodore-
sultado.FoijustamenteopapeldaJSTL( Java Standard T ag Library)edaEL
(Expression Language).
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<body>
Modelo: <c:out value="${modelo}" />
Ano do Modelo: <c:out value="${anoModelo}" />
</body>
</html>
Mascomoosdadoschegamnatela?Deondeestãovindoo modeloeo
anoModeloparaseremusadospelaTag c:out?
17
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 34

1.8. Organizeseucódigocomasepara çãoderesponsabilidades CasadoCódigo
1.8 Organize seu código com a separação de re -
sponsabilidades
PrecisamosagorafazercomqueaServlet VisualizaAutomovelServlet
disponibilizeasinforma çõesparaoJSPqueseráexibidoemseguida. É
umasimplesaltera ção,bastandoadicionarasinforma çõesno requeste
despacharosmesmosparaoJSPqueseráexibido:
protected void doGet(HttpServletRequest req,
HttpServletResponse res) throws IOException, ServletException{
AutomovelDAO dao = new AutomovelDAO();
Automovel auto = dao.busca(request.getParameter("id"));
// coloca as informações no request para seguirem adiante
req.setAttribute("modelo", auto.getModelo());
req.setAttribute("anoModelo", auto.getAnoModelo());
RequestDispatcher rd =
req.getRequestDispatcher("/visualiza.jsp");
// encaminha para o JSP, levando o request com os dados
rd.forward(req, res);
}
Notequeagoratemosresponsabilidadesmelhoresdefinidaseseparadas
nessecódigo,sendoqueadaclasseérealizaralógicanecessáriaparabuscar
oautomóvelnobancodedado,eoJSPéresponsávelporexibirosdadosque
forampassadospelaServlet.
Essefoiumprimeiropassoparaatingirmosumbomníveldeorganiza ção
emnossocódigo.Porém,percebaquenãoestáperfeitoainda,jáqueestamos
tendotodootrabalhodepegarasinforma çõesdo requesterepassá-lasao
JSP.Comoseráquepodemosmelhorarisso?
1.9 OMVC e os frameworks
Noproblemaanterior,acabamospordeixarnossaServletaindacombas-
tanteresponsabilidade,vistoqueelaprecisarecolherosdadosdo request,
18
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 35

CasadoCódigo Capítulo1. Introdução
senecessárioconvertê-los, alémdedisponibilizarosobjetosparaoJSPe
despachararequisi çãoparaapáginaqueseráexibidaparaousuário.
Fig.1.4:Fluxodeexecu çãoondeapenasagera çãodoHTMLsaidaServlet
Seriamuitomelhorquearegradenegócio,nocasoabuscanobanco
dedados,ficasseisoladadainfraestrutura. Poderíamosfazercomquetoda
requisiçãorecebidapelaaplica çãocaísseemumlugarúnico,cujarespons-
abilidadefossefazerastarefaschataserepetitivasdeinfraestruturaquenão
queremoscolocarnomeiodocódigodenossaaplica ção. Tarefascomope-
garparâmetrosdorequesteconvertê-los,porexemplo,seriamfeitasporesse
componente.
Dessamaneira,teríamosofluxo:
19
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 36

1.9. OMVCeosframeworks CasadoCódigo
Fig.1.5:Fluxodeexecu çãoondeastarefasficambemdistribuídas
Apartirdessasepara çãoentreasdiversastarefasquenossaaplica ção
geralmentefaz, chegamosaomodelo MVC(Model- View-Controller). Ve-
jamosaresponsabilidadedecadaumadessaspartes.
Visão-View
A Visão (View)representaapartequeinteragecomousuário,astelas,
quepodemserformadasporarquivosJSP,HTML,imagens,JavaScripteCSS.
Na viewcolocamosapenascoisasrelacionadascomaapresenta çãoouvisão
dosdados,enãoalógicadanossaaplica ção(quevaino Model).Issonãoquer
dizerquenãopodemosterprograma ção,comotomadasdedecisãocomoum
ifouiterardadoscomum while.Significaquequalquer scriptdaapresen-
taçãotemaresponsabilidadedetratarcoisasdeapresenta ção:formataruma
data,esconderumcampo,listaritensdeumalista.
20
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 37

CasadoCódigo Capítulo1. Introdução
Modelo-Model
O Modelo (Model)faztodaaparteinteligentedosistema:cálculos,val-
idaçõesdenegócio,processamento,integra çõesetc. Comessaslógicasiso-
ladasdainfraestruturadaaplica ção,podemosfacilmentereaproveitá-laem
outroslugares.
Porexemplo,podemosreaproveitartodoomódulodecálculosdetaxas
dosistemadeumaconcessionáriaqueéwebemummóduloDesktop,porque
omesmodeveriaseencontrartotalmentedesacopladodetecnologiasusadas
nacamadadevisão,comowebouDesktop.
Controlador-Controller
O Controlador (Controller)éresponsávelporreceberasrequisi çõesdo
usuário,montarosobjetoscorrespondentesepassá-losao Modelparaque
façaoquetemqueserfeito. Depoisdereceberoretornodaopera çãoex-
ecutada,ocontroladorapresentaoresultadoparaousuário,geralmenteo
redirecionandoparaa View.
21
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 38

1.9. OMVCeosframeworks CasadoCódigo
Fig.1.6:Fluxodeexecu çãoondeastarefasficambemdistribuídas
Mascomofa çoparaseparartodasessasresponsabilidadesemminhaapli-
cação?Justamenteparaauxiliarnesseprocesso,acomunidadededesenvolve-
doresseorganizouecome çouadesenvolverdiversasferramentasqueaux-
iliamnessetrabalho. EssasferramentassãoconhecidascomoFrameworks
MVCouControladoresMVC.
Existemváriosdessesframeworksdisponíveisparaseusar,comooStruts,
SpringMVC,JSF(JavaServerFaces),VRaptorentreoutros.Nestelivrovamos
nosateraoJSF,explicandocomoelepodefacilitarodesenvolvimentodeapli-
caçõesWebemJava.
22
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 39

CasadoCódigo Capítulo1. Introdução
1.10 Por que usar JSF?
Aexemplodoqueaconteceucomosframeworksdemapeamentoobjeto-
relacional,surgiramdiversosframeworksMVC,porémestesaindaemmaior
número.DaísurgiuanecessidadedesepadronizarumframeworkMVC,as-
simcomoaJPAveiopadronizaroORM.
EnquantoaJPAestabeleceuumaAPImuitofamiliarparaquemeraacos-
tumadocomoframeworkdominante,oHibernate,oJSFveiomuitodifer-
entedoquehavianaépoca.Issosedevetambémàgrandesegmenta çãoentre
osframeworksMVC.EnquantomuitosdesenvolvedoresutilizavamoHiber-
natecomoframeworkORM,oframeworkMVCmaisutilizadonaépocado
surgimentodoJSFeraoStruts,quepossuíafamadesercomplexoepouco
produtivo.
Porterumaformatãodiferentedo“statusquo”daépoca,aaceitaçãodo
JSFnãofoitãoimediataquantoàdaJPA.Enquantoaado çãodestafoiquase
imediata,oJSFenfrentoumuitaresistência,principalmenteemsuaversão
1.X.Nestelivroabordaremosaversão2.X,queacaboucommuitaslimita ções
daversãoanterior,oferecendoumaferramentaprodutivaparaodesenvolvi-
mentodeaplica çõesWeb.
OutrofatorquecausouestranhezanoprimeirocontatocomoJSFfoio
fatodeeleserumframeworkbaseadoemcomponentesenãoema ções,como
eramosprincipaisframeworksdaépoca,ecomoaindaéatéhoje.Veremos
maissobrecomoessesparadigmassediferemembreve.
1.11 Oprimeiro contato com o JSF
AtravésdousodeumframeworkMVC,temoscomponentesespecíficospara
realizarastarefasdanossaaplica ção. NocasodoJSF2,nossastelasserão
escritasemumarquivoXHTMLutilizandoTagsdopróprioJSF.Dessaforma,
podemosfazerumsimplesformuláriodecadastrodeautomóveldaseguinte
forma:
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:f="http://java.sun.com/jsf/core"
xmlns:h="http://java.sun.com/jsf/html">
23
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 40

1.11. OprimeirocontatocomoJSF CasadoCódigo
<h:head>
<title>Cadastro de automóvel</title>
</h:head>
<h:body>
<h:form>
Modelo: <h:inputText
value="#{automovelBean.automovel.modelo}"/>
<br/>
<h:commandButton value="Grava"
action="#{automovelBean.grava}" />
</h:form>
</h:body>
</html>
ReparenousodeTagsparacriaroselementoscomoosinputseosbotões.
IssoénecessáriodevidoaofuncionamentointernodoFramework,quevamos
vercomdetalhesnodecorrerdolivro. Abrindoessapáginanonavegador,
vocêvêumatelasimilaràfigura1.7
Fig.1.7:FormulárioapenascomocampodomodelodoAutomóvel
Notetambémqueéindicadonocódigoque,aoclicarnobotãogravar,
suaa çãoé #{automovelBean.grava}. Issoindicaqueseráchamadoo
método gravadeumaclassechamada AutomovelBean. Essaclasseéo
quechamamosde Managed Beaneéresponsávelporintegraroquetemosna
telacomaregradenegócioqueseráexecutada:
@ManagedBean
public class AutomovelBean {
private Automovel automovel = new Automovel();
public void grava() {
new AutomovelDAO().grava(automovel);
24
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 41

CasadoCódigo Capítulo1. Introdução
}
// getter e setter
}
Eisoutropontointeressante: comonatelanãocriamososinputscom
TagsHTMLesimcomoJSF,comoelessãoexibidos?Onavegadorentende
asTagsdoJSF?
Na verdade, os componentes do JSF apenas geram o código HTML
necessário. Sepedirmosparavisualizarocódigofontedapágina,teremos
algosimilara:
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Cadastro de Automóvel</title>
</head>
<body>
<form id="j_idt6" name="j_idt6" method="post"
action="/faces-motors/faces/automovel/cadastro.xhtml"
enctype="application/x-www-form-urlencoded">
<input type="hidden" name="j_idt6" value="j_idt6" />
Modelo: <input type="text" name="j_idt6:j_idt9" />
<input type="submit" name="j_idt6:j_idt18"
value="Grava" />
<input type="hidden" name="javax.faces.ViewState"
id="javax.faces.ViewState"
value="2892395016760917637:4875835637171130451"
autocomplete="off" />
</form>
</body>
</html>
Nãoseassustecomesseestranhocódigogerado. Nospróximoscapítu-
losvamosaprendermaissobrecomoeleégerado,ecomopodemosterum
25
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 42

1.12. Nospróximoscapítulos CasadoCódigo
controlemaiorsobreele,bemcomoosignificadodetudoisso.
1.12 Nos próximos capítulos
Vimosrapidamenteastecnologiasquevamosesmiu çarduranteolivro,por
enquantosemmuitosdetalhes,apenasparaquevocêsintaumpoucodoque
estápelafrente.Nospróximoscapítulos,vamoscriarumaaplica çãodozero,
comdiversasfuncionalidadesquesãonecessáriasemaplica çõescomerci-
ais,mostrandoeexplicandosemprenovosrecursosdaJPA,doJSFecomo
integrá-losentresi.
Recomendamostambémqueoleitorquequeiraacompanharocódigo
emseucomputador,testarosexemplosecustomizá-losofa ça. Olivroestá
escritodemaneiraapossibilitaressadinâmica.
Poroutrolado,tambémconsideramosqueoleitorqueirausá-locomo
materialdereferênciaemassuntosespecíficos,comoociclodevidadoJSF.
Paraisso,bastaencontrarapáginaadequadanosumárioeestudaroassunto
quelheinteressa.
26
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 43

Capítulo2
PrimeirospassoscomaJPA
NestecapítuloveremososconceitosmaisbásicosdeJPAeJSF.Oobjetivoé
conseguirmosdesenvolverumaprimeiraversãodanossaaplica ção,jácom
umainterfacegráficaeapersistênciadedadosfuncionandoplenamente.
2.1 Definição do modelo
Comopontodepartidavamosanalisarnossaclasse Automovelcujocódigo
podeservistoaseguir:
@Entity
public class Automovel {
@Id @GeneratedValue
private Long id;
private String marca;
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 44

2.1. Definiçãodomodelo CasadoCódigo
private String modelo;
private Integer anoFabricacao;
private Integer anoModelo;
private String observacoes;
// getters e setters se necessário
}
Aúnicacoisaqueadiferedeumaclassecomuméapresen çadasano-
tações: @Entity, @Ide @GeneratedValue.
NocontextodaJPA,chamamosdeentidadesasclassesqueestãovincu-
ladascomumaunidadedepersistência. ComoaJPAtratademapeamento
objeto-relacional,aunidadedepersistênciaéumbancodedados,edemodo
geral,umaentidadeestaráassociadaaumatabelanessebanco.
Porcontadarela çãoentreaentidadeeatabelanobancodedados,
quandoquisermospersistirumobjeto Automovel,seránecessáriofazerum
insertemumatabela.Porém,qualéonomedessatabelaequaiscolunas
terãoqueserutilizadasnainser ção?
Nonossoexemplo, nãodefinimosnenhumnomedecolunaetabela.
Dessaforma,estamosseguindoumaconven çãodaprópriaJPA.Nessasitu-
ação,atabelateráexatamenteomesmonomedaentidadeeparacadaatributo
daclasse,teremosumacolunacomomesmonome.Aopersistirmosumob-
jetodotipo Automovelemumbancodedadosrelacional,agrava çãoéfeita
numatabelacomumaestruturasimilaràfigura2.1:
28
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 45

CasadoCódigo Capítulo2. PrimeirospassoscomaJPA
Fig.2.1:TabelaAutomovel
Percebemosque,paraumaentidadesimples,precisamosapenasdizerque
elaéumaentidade,pormeiodaanota ção @Entity,eespecificaroatributo
querepresentaasuachaveprimáriacomaanota ção @Id.Pronto.
Se,nonossoexemplo,desejássemosqueachaveprimáriafossealgorela-
cionadoàaplica ção,enãoumidentificadorcomvalorgeradoautomatica-
mente-porexemplo,oCPFdeumapessoa-,nãoprecisaríamoscolocarnada
alémdasanota ções @Entitye @Id,comonaclasseaseguir:
@Entity
public class Cliente {
@Id
private String cpf;
// outros atributos
}
2.2 Configuração básica do persistence .xml
OpróximopassoéindicarmosparaaJPAasinforma çõesdeconexãocom
obancodedados,comoousuário,senhaeendere çodeacesso. Paraisso,
temosquecriarumarquivochamado persistence.xmlecolocá-lona
pasta META-INF.Essediretóriodeveestarnoclasspathdoprojeto,portanto,
juntodasclasses.
29
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 46

2.2. Configuraçãobásicadopersistence.xml CasadoCódigo
Essearquivopossuiumcabe çalho,declaradocomatag persistence:
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.0"
xmlns="http://java.sun.com/xml/ns/persistence"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://java.sun.com/xml/ns/persistence
http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">
</persistence>
Dentro de persistence, é preciso indicar para a JPA qual con-
juntodeconfigura çõesteremos,paraquesejapossívelindicarqualbanco
de dados será utilizado. Esse conjunto de configurações é chamado de
persistence-unit,aoqualdevemosdarumnome:
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.0" ... >
<persistence-unit name="default">
</persistence-unit>
</persistence>
Chamamosde default,mas poderiaserdadoqualqueroutronome .
Guarde-o com atenção, pois futuramente ele deverá ser referenciado no
códigoJava.
Agora,bastaindicarosdadosdeconexãocomobancodedados,como
ousuário,senhaestringdeconexãocomobanco. Essasconfigura çõessão
feitasatravésdepropriedadesdaunidadedepersistência,descritapelatag
properties.
Dentrode propertiessãocolocadastags propertycontendoum
atributo name indicando qual é a configuração que será feita, além de
umatributo valuecomoconteúdodaconfigura ção. Comisso,parao
username, passworde urldeconexão,oXMLficasimilara:
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.0" ... >
30
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 47

CasadoCódigo Capítulo2. PrimeirospassoscomaJPA
<persistence-unit name="default">
<properties>
<property name="javax.persistence.jdbc.url"
value="jdbc:mysql://localhost/automoveis" />
<property name="javax.persistence.jdbc.user"
value="root" />
<property name="javax.persistence.jdbc.password"
value="password" />
</properties>
</persistence-unit>
</persistence>
TambéménecessárioindicarqualdriverJDBCseráutilizadoe,como
consequência,seu jardeveráestarnaaplica ção. Essadeclaraçãoéfeitaa
partirdapropriedade javax.persistence.jdbc.driver:
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.0" ... >
<persistence-unit name="default">
<properties>
<!-- outras propriedades -->
<property name="javax.persistence.jdbc.driver"
value="com.mysql.jdbc.Driver" />
</properties>
</persistence-unit>
</persistence>
Note que todas as propriedades até o momento começam com
javax.persistence.jdbc.Issoaconteceporqueelasfazempartedaes-
pecificaçãodaJPA.Noentanto,nãoprecisamosficarpresosaelas.Podemos
utilizarpropriedadesquesejamespecíficasdaimplementa çãoqueseráuti-
lizada,comoporexemplo,oHibernate.
31
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 48

2.3. Escolhaodialetodobancodedados CasadoCódigo
2.3 Escolha o dialeto do banco de dados
Quandotrabalhamosdiretamentecombancosdedadosrelacionais,escreve-
mososcódigosemSQLepodemosutilizarcomandosquesejamespecíficos
deumdeterminadobancodedados. Aprópriaimplementa çãodaJPAque
usaremosseencarregadeesconderessesdetalhesdecadabanco.
UmadasfuncionalidadesdoHibernateéaabstra çãodebancodedados.
Dessaforma,nãoénecessáriomodificarocódigodaaplica çãoquandotro-
camosumbancodedadosporoutro.Umadasbasesparaissoéjustamentea
existênciadediversosdialetos,querepresentamasdiferen çasdosSQLspara
cadabancodedados.
O dialeto que será usado na aplicação pode ser indicado no
persistence.xml por meio da propriedade hibernate.dialect,
emquedizemosqualclasseexistentedentrodopróprioHibernatepossuia
implementaçãodessedialeto.NocasodoMySQL,temos:
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.0" ... >
<persistence-unit name="default">
<properties>
<!-- outras propriedades -->
<property name="hibernate.dialect"
value="org.hibernate.dialect.MySQLInnoDBDialect"/>
</properties>
</persistence-unit>
</persistence>
32
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 49

CasadoCódigo Capítulo2. PrimeirospassoscomaJPA
Outros dialetos comuns
AlémdodialetoparaoMySQL,oHibernatepossuidialetosparadi-
versosoutrosbancosdedados:
•Oracle10g- org.hibernate.dialect.Oracle10gDialect
•Oracle(genérico)- org.hibernate.dialect.OracleDialect
•SQLServer2008 - org.hibernate.dialect.SQLServer2008Dialect
•PostgreSQL- org.hibernate.dialect.PostgreSQLDialect
Uma lista completa dos dialetos pode ser encontrada no
Javadoc do Hibernate, disponível em http://docs.jboss.org/
hibernate/orm/4.1/javadocs/ ou verificando as classes no pacote
org.hibernate.dialect.
Alémdepermitirquesejaindicadoqualodialetoaserusado,épossível
realizarmaisconfigura çõesquesãoespecíficasdoHibernateetambémbas-
tanteúteis.
2.4 Automatização da criação e evolução das
tabelas
Semprequesetrabalhacombancodedados,énecessáriotertodasastabelas
criadaseatualizadas.Noentanto,seoprojetoestivernoinício,nãoteremos
nenhumatabela.Justamenteparafacilitarisso,opróprioHibernateconsegue
realizaressacria ção,bastandoindicarqualestratégiadeveráserutilizada,
atravésdapropriedade hibernate.hbm2ddl.auto.
Umvalorpossívelparaessapropriedadeé create,comoqualoHiber-
natecuidaparaqueastabelassejamexcluídaserecriadas.Dessaforma,irá
trabalharsempreapartirdeumbancodedadosvazio.
Alémdaop ção create,existemmais3possibilidades:
33
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 50

2.5. Gravaçãodoprimeirodadonobancodedados CasadoCódigo
•create-drop-astabelassãocriadaspelopróprioHibernateeex-
cluídassomentenofinaldaexecu çãodoprogramacasosolicitadopelo
desenvolvedor;
•update-nadaéexcluído,apenascriado,ouseja,todososdadossão
mantidos.Útilparaaplica çõesqueestãoemprodu ção,dasquaisnada
podeserapagado;
•validate-nãocriaenemexcluinada,apenasverificaseasenti-
dadesestãodeacordocomastabelase,casonãoesteja,umaexce çãoé
lançada.
Umpossívelusodessapropriedadeno persistence.xmlé:
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.0" ... >
<persistence-unit name="default">
<properties>
<!-- outras propriedades -->
<property name="hibernate.hbm2ddl.auto"
value="update" />
</properties>
</persistence-unit>
</persistence>
2.5 Grav ação do primeiro dado no banco de da -
dos
Comaconfigura çãofeita,épossívelgravarasprimeirasinforma çõesepara
issoseránecessáriaumaconexãocomobancodedadosqueacabamosque
configurarno persistence.xml.Ouseja,precisaremosdeumaconexão
comaunidadedepersistência( persistence-unit).
Para verificarmos se nossa configuração estava correta, vamos criar
umaclassecujoobjetivoépersistirum Automovel. Vamoschamá-lade
PersistidorDeAutomovel. Essaclasseteráummétodo mainquefará
taltrabalho.
34
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 51

CasadoCódigo Capítulo2. PrimeirospassoscomaJPA
Dentrodo main,éprecisoconseguirumaconexãocomobancodedados
definidona persistence-unit.Oprimeiropassoparaconseguirmosisso
édescobrirquemsabecriarasconexões.Esseéjustamenteumdospapéisda
classe EntityManagerFactory.
Para conseguirmos uma instância dela, basta utilizar o método
createEntityManagerFactory da classe Persistence da própria
JPA, indicando qual é a persistence-unit que definimos no
persistence.xml,quenocasochamamosde default:
public class PersistidorDeAutomovel {
public static void main(String[] args) {
EntityManagerFactory emf = Persistence.
createEntityManagerFactory("default");
}
}
Umavezcomainstânciade EntityManagerFactory,bastainvocar-
mosométodo createEntityManager. Eledevolveumobjetodotipo
EntityManager,querepresenta,entreoutrascoisas,umaconexãocoma
unidadedepersistência.
public class PersistidorDeAutomovel {
public static void main(String[] args) {
EntityManagerFactory emf = Persistence.
createEntityManagerFactory("default");
EntityManager em = emf.createEntityManager();
}
}
Pronto,agorabastainstanciarepopularumobjetodotipo Automovel,
epassarmosesseobjetoparaa EntityManagerrealizarapersistência.
public class PersistidorDeAutomovel {
public static void main(String[] args) {
EntityManagerFactory emf = Persistence.
createEntityManagerFactory("default");
35
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 52

2.5. Gravaçãodoprimeirodadonobancodedados CasadoCódigo
EntityManager em = emf.createEntityManager();
Automovel auto = new Automovel();
auto.setAnoFabricacao(2014);
auto.setMarca("Ferrari");
auto.setModelo("La Ferrari");
auto.setObservacoes("Nunca foi batido");
em.persist(auto);
em.close();
emf.close();
}
}
Aoexecutaressecódigonadaserágravado. Issosedeveaofatodeque
emmomentonenhumdelimitamosatransa çãoedissemosqueo persist
estavaenvolvido. Mascorrigiresseproblemaébemsimples. Bastapedira
transaçãoparaa EntityManagereinvocarométodo begin, commite
rollbackconformenecessário:
public static void main(String[] args) {
EntityManagerFactory emf = Persistence.
createEntityManagerFactory("default");
EntityManager em = emf.createEntityManager();
Automovel auto = new Automovel();
auto.setAnoFabricacao(2014);
auto.setMarca("Ferrari");
auto.setModelo("La Ferrari");
auto.setObservacoes("Nunca foi batido");
EntityTransaction tx = em.getTransaction();
tx.begin();
em.persist(auto);
tx.commit();
em.close();
36
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 53

CasadoCódigo Capítulo2. PrimeirospassoscomaJPA
emf.close();
}
Executandoessecódigo,onovocarroserápersistidonobancodedados,
porémserápossívelperceberumacertademoraemsuaexecu ção,dandoa
sensaçãodequeumsimples insertlevatempodemaisparaseexecutar.
Isso acontece devido à invoca ção do método
createEntityManagerFactory. Esse método realiza diversas tare-
fas, entreelas, lerasanota çõesdasentidadesanotadasecriaropoolde
conexões com o banco de dados - o que vamos estudar e aprender a
configurarfuturamente.
Comisso,precisamosqueessecódigoexecuteapenasumavezemtodaa
aplicação,paraqueoúnicomomentoemqueocorreessalentidãosejaoda
criaçãoda EntityManagerFactory.Dessaforma,aspersistênciassubse-
quentesserãofeitasemtemponormal.
Podemosgarantirquea EntityManagerFactorysejacriadaumavez
sófazendoumaclassequetenhaumatributoestáticoparaarmazenaressa
instância,equeelasejaumaconstante,paraquenãosejacriadaoutrasvezes.
Podemoschamá-lade JPAUtil:
public class JPAUtil {
private static final EntityManagerFactory emf =
Persistence.createEntityManagerFactory("default");
}
Podemostambémfazeressaclasseterummétodo getEntityManager
quedevolvauma EntityManager,assimconseguimosteracessoaelasem-
prequeprecisarmosfazeraspersistências:
public class JPAUtil {
private static final EntityManagerFactory emf =
Persistence.createEntityManagerFactory("default");
public static EntityManager getEntityManager() {
return emf.createEntityManager();
}
}
37
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 54

2.5. Gravaçãodoprimeirodadonobancodedados CasadoCódigo
Com essa alteração, podemos modificar o métodomain na classe
PersistidorDeAutomovel,parausaressanovaclasse JPAUtil:
public static void main(String[] args) {
EntityManager em = JPAUtil.getEntityManager();
// código para persistir o automóvel
}
Por fim, ao executarmos o método main do
PersistidorDeAutomovel,nadaéexibido,masasinforma çõesvãosendo
persistidasnobancodedados.Atente-separaofatodeaestratégiadecria ção
dastabelaspoderrealizaro dropnassuastabelas.Casonãodesejequeisso
aconteça,utilize updatenapropriedade hibernate.hbm2ddl.autono
seu persistence.xml.
Outro ponto interessante é que você pode fazer com que o Hiber-
nateimprimanoconsolequaiscomandosSQLsestãosendorealizadosno
banco de dados. Para isso, basta adicionar uma nova propriedade no
persistence.xml,chamada show_sql,comovalor true. Opcional-
mente,vocêtambémpodeusarapropriedade format_sqlparaqueessa
exibiçãosaiaformatada:
<property name="hibernate.show_sql" value="true" />
<property name="hibernate.format_sql" value="true" />
Com essas duas propriedades habilitadas, o Hibernate vai exibir a
seguintesaída:
Hibernate:
insert
into
Automovel
(anoFabricacao, anoModelo, marca, modelo, observacoes)
values
(?, ?, ?, ?, ?)
38
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 55

CasadoCódigo Capítulo2. PrimeirospassoscomaJPA
2.6 Consultas simples no banco de dados com a
JPA
Comdadosgravadosnobancodedados,podemosrealizarpesquisas. A
primeiraconsultaquevamosrealizaratravésdaJPAseráumsimples select
* from Automovel,ouseja,vamosbuscartodososautomóveisgravados.
AotrabalharmoscomaJPA,temosaop çãoderealizarconsultasSQL,
porémmuitosdesenvolvedoresoevitam,principalmentepelofatodepoder
prenderaaplica çãoarecursosespecíficosdeumbancodedados.Paraisso,
foicriadaumalinguagemdeconsultas,parecidacomSQL,daqual umadas
vantagenséaabstra çãodobancodedadosqueestásendousado.Essalin-
guageméaJPQL( Java Persistence Query Language).
AJPQLpossuisintaxeeestruturamuitoparecidascomoSQL.Tantoque,
pararealizarmosumapesquisadetodososautomóveis,poucacoisamuda,
repare:
select a from Automovel a
EssaconsultaJPQLrealizaabuscadetodososautomóveis.Naclausula
fromindicamosqualéaentidade quedeveráserbuscadaedamosum alias,
umapelido,paraessaentidade,quenocasofoi a.Eindicamosnacláusula
selectàqualosautomóveisserãodevolvidos.
Paraexecutarmosessaconsulta,precisaremos,damesmamaneiraque
paraagrava ção,conseguira EntityManager.Comelaemmãos,podere-
mosinvocarométodo createQuery,querecebea Stringcomaconsulta
quedesejamosdispararetambémotipodoobjetoqueaconsultadevede-
volver-quenonossocasoé Automovel.Issodevolveráumobjetodotipo
javax.persistence.Query:
EntityManager em = JPAUtil.getEntityManager();
Query q =
em.createQuery("select a from Automovel a",Automovel.class);
Por fim, podemos executar essa consulta invocando o método
getResultList no objeto Query, que devolverá uma lista com ob-
jetosdotipoindicadonomomentodachamadaao createQuery:
39
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 56

2.7. ExclusãodedadoscomaJPA CasadoCódigo
EntityManager em = JPAUtil.getEntityManager();
Query q =
em.createQuery("select a from Automovel a",Automovel.class);
List<Automovel> autos = q.getResultList();
Pronto, agoraqueconseguimosalista, podemositerarsobreelapara
mostrar,porexemplo,amarcadetodososautomóveis:
EntityManager em = JPAUtil.getEntityManager();
Query q =
em.createQuery("select a from Automovel a",Automovel.class);
List<Automovel> autos = q.getResultList();
for(Automovel a : autos) {
System.out.println(a.getMarca());
}
Consultas complexas com a JPQL
Nocapítulo6,aprenderemosafazerconsultascomplexasenvolvendo
agrupamentos, ordenação, joins e vários outros recursos que costu-
mamosusarnodiadiaaoescrever queriesquesãoexecutadasnobanco
dedados.
2.7 Exclusão de dados com a JPA
Muitasvezes,acabamosporinserirdadosporenganonobancodedados,
ouelespodemnãosermaisnecessáriosepassamaserpassíveisdeserem
descartados.Porisso,precisamospoderexcluirasinforma ções,ounonosso
caso,precisamosexcluirautomóveisdobancodedados.
EssatarefacomaJPAsetornaextremamentesimples,jáque,damesma
maneira que no cadastro, ela faz todo o trabalho para nós. Basta que
chamemos o método adequado, no casoremove, passando um objeto
Automovelcomo idpopulado:
40
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 57

CasadoCódigo Capítulo2. PrimeirospassoscomaJPA
EntityManager em = JPAUtil.getEntityManager();
EntityTransaction tx = em.getTransaction();
Automovel auto = em.getReference(Automovel.class, 1L);
tx.begin();
em.remove(auto);
tx.commit();
O uso do método get Reference
Mais a frente veremos mais do métodogetReference. Por
enquanto nos importa saber que os trechos de código a seguir são
equivalente, com o diferencial que usando o método da interface
EntityManagertemoscomoretornoumobjetogerenciado,mesmo
semacessarobancodedados. Masoqueissosignificaaocertovere-
mosemdetalhesnocapítulo4.
//objeto gerenciado apenas com o id populado (não vai no
//banco de dados)
Automovel auto = em.getReference(Automovel.class, 1L);
//objeto não gerenciado com o id populado
Automovel auto = new Automovel();
auto.setId(1L);
Aoexecutarmosocódigoacima,porexemplo,dentrodeummétodo
main,o deleteéexecutado,excluindooautomóvelcujo idera1. Note
queéimprescindívelqueoobjetoaserexcluídotenhaseu idpopulado,caso
contrárioaexclusãonãoéfeita,jáquenãosetemcomosaberqualéainfor-
maçãoquedeveserremovidadobancodedados.
41
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 58

2.8. Oquemaisvempelafrente? CasadoCódigo
2.8 O que mais vem pela frente?
Empoucosminutosjáconseguimosvercomoconfigurarerealizar3oper-
açõescomunscomobancodedados:o select,o inserteo delete.
Aindafaltao update,masesseéumcasoàpartesobreoqualvamosfalar
nocapítulo4.
Duranteolivroaprenderemoscomorealizarqueriescomplexas, vali-
daçõesdedadosdeumaformaextremamentesimples,otimiza çãodeper-
formanceeboaspráticasparaorganizarseucódigoenvolvendoaJPA.
42
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 59

Capítulo3
PrimeirospassoscomoJSF
Nocapítulo2,definimosaentidade Automovelcomseusatributosecon-
seguimospersistiressainforma çãonobancodedadosatravésdaexecu çãode
umaclassecontendoummétodo main.
Apartirdeagora,vamoslevaressamesmaintegra çãoparaawebepara
issovamosusaroJSF,quenosajudaránotrabalhodecriaraaplica çãoweb.
Onossoprimeirotrabalhovaiserpermitirocadastrodosautomóveispor
meiodeumainterfaceweb,enãomaisviaaqueleestranhométodo main.
3.1 Onde e como defino telas com o JSF?
Precisamosconstruiratelaondeserãocadastradosnovosautomóveis.Atela
quequeremoscomoresultadofinaléparecidacomafigura3.1.
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 60

3.1. OndeecomodefinotelascomoJSF? CasadoCódigo
Fig.3.1:Formulárioquevamosconstruir
Para criarmos essa tela, o primeiro passo é termos um arquivo
XHTML, no qual escreveremos o código necessário para mostrar o for-
mulário de cadastro de automóveis. Podemos chamar esse arquivo de
cadastraAutomoveis.xhtml.
QuandodesenvolvemosumprojetousandooJSF,aconstru çãodatela
setornaumpoucodiferentedeoutrosframeworks,comooStruts,VRap-
toreSpringMVC,nosquaiscostumamosusarapenaselementosHTMLpara
criarosformulários,tabelasedemaiscaracterísticasdavisualiza çãodasinfor-
mações.NoJSF,praticamentetodaatelaécriadaapartirdeTaglibspróprias
dele,quepossuemopapelderenderizaroHTMLadequadoparaofunciona-
mentodoframework. Poressemotivo, nocome çodonossodocumento
XHTML,precisamosimportaressasTaglibscomoseguintecódigo:
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://java.sun.com/jsf/html">
</html>
NotequenaaberturadaTag htmlindicamosalguns namespaces. O
primeiroéo namespacepadrãoparaXHTMLs,enquantoooutroéespecí-
ficoparaconseguirmosusarasTagsdoJSFemnossoXHTML.
O xmlns:h="http://java.sun.com/jsf/html\T1\textquotedbl{}indicaquees-
tamoshabilitandoatravésdoprefixo hasTagsdoJSFquerenderizamHTML.
44
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 61

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
3.2 Criação da tela e dos inputs básicos de da -
dos
ComasTagshabilitadaspelo namespace h,podemosagoraconstruirocon-
teúdodapágina,contendooformulárioeoscamposparaqueosusuários
possamcolocarosdadosdoautomóvelasercadastrado.DentrodaTag html,
podemosdefinirocorpodapáginaeumcampodetextoparaamarcadoau-
tomóvel.VamosfazerissoutilizandoasTagsdoJSF.Paraisso,vamosescrever
noarquivo cadastraAutomoveis.xhtml:
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://java.sun.com/jsf/html">
<h:body>
<h:form>
Marca: <h:inputText />
</h:form>
</h:body>
</html>
EsseXHTMLmínimogeraateladafigura3.2.
Fig.3.2:FormulárioJSFcomumúnicocampo
ReparequeusamosaTag h:bodyemvezda bodydoHTML,a h:form
nolugarde forme h:inputTextemvezde input type="text".Es-
tamosusandooscomponentesdoJSFparageraroHTMLparanós.Seaces-
sarmosesse cadastraAutomoveis.xhtmlnonavegadorepedirmospara
verocódigofontegerado,eleserásimilaraocódigoaseguir:
<html xmlns="http://www.w3.org/1999/xhtml">
<body>
<form id="j_idt4" name="j_idt4" method="post"
action="/faces-motors/automovel/editar.jsf"
45
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 62

3.2. Criaçãodatelaedosinputsbásicosdedados CasadoCódigo
enctype="application/x-www-form-urlencoded">
<input type="hidden" name="j_idt4" value="j_idt4" />
Marca: <input type="text" name="j_idt4:j_idt25" />
<input type="hidden" name="javax.faces.ViewState"
id="javax.faces.ViewState"
value="-2173774569225484208:-2914758950899476002"
autocomplete="off" />
</form>
</body>
</html>
OcódigofonteégeradopelopróprioJSF.Repareno namedo input:é
umcódigotambémgeradopeloJSF.Essescódigosqueaprincípioparecem
malucossãoprimordiaisparaobomfuncionamentodoJSF.Comopassardo
temponosacostumaremoscomelesevamosentenderporcompletoomotivo
deelesseremtãoimportantesparaoJSF.
Esseformuláriopodeserexpandidoparaabrangertodososcamposque
precisaremosparaoautomóvel,comoomodelo,anodefabrica ção,anodo
modeloeobserva ções.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://java.sun.com/jsf/html">
<h:body>
<h:form>
Marca: <h:inputText /><br/>
Modelo: <h:inputText /><br/>
Ano de Fabricação: <h:inputText /><br/>
Ano do Modelo: <h:inputText /><br/>
Observações: <h:inputTextarea /><br/>
</h:form>
</h:body>
</html>
Aoabrirmosessapáginanonavegador,teremosumatelaparecidacoma
dafigura3.3.
46
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 63

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
Fig.3.3:Formuláriocomlayoutdesorganizado
Notecomooconteúdoficoutododesalinhado. Asdescri çõesdoscam-
posempurramos inputsparaadireitaeissofazcomqueatelapare ça
tortaeestranha.PensandoemHTML,podemoscontornaresseproblemade
pelomenosduasmaneiras:aprimeira,criandoumatabelaparaoformulário
edividindoadescri çãoeocampoemcolunasdiferentes,easegundaseria
fazendoessetrabalhodealinhamentocomCSS.
ComoJSF,podemosfazeressealinhamentodeumamaneirabemsim-
ples.BastaenvolveroconteúdodoformulárionaTag h:panelGrid,quedi-
videoconteúdoqueestiverdentrodelaemcolunas.Podemosindicarquantas
colunasqueremospeloatributo columns.
<h:body>
<h:form>
<h:panelGrid columns="2">
Marca: <h:inputText />
Modelo: <h:inputText />
Ano de Fabricação: <h:inputText />
Ano do Modelo: <h:inputText />
Observações: <h:inputTextarea />
</h:panelGrid>
</h:form>
</h:body>
O h:panelGridquebraaslinhasecolunasapartirdoselementosex-
istentesdentrodele. Dessaforma,otexto Marca:ficaemumacolunaeo
h:inputTextdeleficaemoutracoluna.Comojásecompletaramduascol-
47
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 64

3.3. commandButton,ManagedBeanseasubmissãodeformulários CasadoCódigo
unas,ospróximosconteúdosvirãonalinhaseguinte.Eassimsucessivamente,
atéfazeraorganiza çãodetodooformulário.
3.3 command Button ,M anagedBeans e a submis-
são de formulários
Umavezcomoformulárioprontoeorganizadonatela,precisamossubmeter
osdadospreenchidospelousuárioparaque,dealgumamaneira,sejafeitaa
gravaçãonobancodedados.
Para isso, o primeiro passo é termos na tela um botão que permita
asubmissãodasinforma ções, quepodeseradicionadopormeiodaTag
h:commandButton:
<h:body>
<h:form>
<h:panelGrid columns="2">
Marca: <h:inputText />
Modelo: <h:inputText />
Ano de Fabricação: <h:inputText />
Ano do Modelo: <h:inputText />
Observações: <h:inputTextarea />
<h:commandButton value="Salvar" />
</h:panelGrid>
</h:form>
</h:body>
Em h:commandButton,indicamosqualéotextoqueaparecenobotão
atravésdoatributo value,porém,nãodefinimosquala çãodeveráserfeita.
Ouseja,precisamosindicarondeestaráocódigoquevaifazerocadastrono
bancodedados.
Pararealizarmosocadastro,vamosprecisardeumaclassequecontenha
algummétodoquefa çaagrava ção.Essemétodo,porsuavez,deveserinvo-
cadoquandoobotãoforclicado. Essaclasse,quepossuiumarela çãocoma
tela,échamada Managed BeanenãopassadeumsimplesPOJO- Plain Old
Java Object.Aúnicaobrigatoriedadequetemosaocriarum Managed Beané
ousodaanota ção @ManagedBean:
48
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 65

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
@ManagedBean
public class AutomovelBean { }
POJO
OtermoPOJO- Plain Old Java ObjectfoicunhadoporMartinFowler,
RebeccaParsonseJoshMacKenzieparaindicarclassessimplesJava,que
nãoprecisamimplementarinterfaceenemrealizarqualquerheran çade
umframeworkespecífico.
Otrabalhoquetemosagoraédeindicarqueaoclicarnobotão“Salvar”
ummétododesse Managed Beandeveserchamado. Paraisso,vamoscriar
ummétodochamado salva:
@ManagedBean
public class AutomovelBean {
public void salva() {
// aqui vai o código para salvar
}
}
Já estamos na metade do caminho para conseguir invocar o método
ao clicar no botão, porém, ainda falta indicar para o botão que quando
eleforclicado, ométodo salvadeveráserchamado. Paraisso, aTag
h:commandButtonpossuiumatributochamado action,ondepodemos
indicaroquedeveserchamadoquandoclicado.
Parapassarmosessainforma çãoparao action,precisamosusarum
recursochamado Expression Language,quenospermitequenocódigodatela,
nocasoo xhtml,fa çamosumareferênciaparaalgodeum Managed Bean.
Nessecaso,queremosfazerumareferênciaaométodo salvado Managed
Bean AutomovelBean,processotambémconhecidocomo binding,então
usamos:
<h:commandButton value="Salvar"
action="#{automovelBean.salva}"/>
49
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 66

3.4. PassedadosdatelaparaoManagedBean CasadoCódigo
Nessecódigo,notequea Expression Languagepossuiumasintaxeum
poucodiferente,um #{}. Oconteúdodaschaveséoquequeremosrefer-
enciarcomrela çãoao Managed Bean,nessecaso,ométodo salva.Repare
tambémqueaconvençãoparaonomedo Managed BeanéCamel Case,porém
comaprimeiraletraemminúsculo.Parausaroutronome,épossívelusaro
atributo namenaanota ção @ManagedBean:
@ManagedBean(name="OutroNomeParaOAutomovelBean")
public class AutomovelBean { }
E com isso, usaríamos as Expression Languages
OutroNomeParaOAutomovelBeanemvezde automovelBean.
O que acontece quando clico no botão?
Énaturalimaginarquequandoobotãoéclicadoométododo Man-
aged Beanédiretamenteinvocado.Essasensa çãoacontecedevidoaofato
dequeométodoefetivamenteoexecuta. Porém,estamostrabalhando
comumaaplica çãowebenofundo,oqueestáacontecendoéumareq-
uisiçãoparaaaplica ção.
Aoreceberessarequisi ção,oJSF“percebe”quevocêclicounobotão
equeométodoindicadono actiondeveserinvocadoeportanto,ele
fazessachamadaparavocê.
3.4 Passe dados da tela para oManaged Bean
Apartirdomomentoemqueépossíveldispararummétododo Managed
Beancomocliquedeumbotão,queremosquesuaa çãosejafazeragrava ção
deumautomóvelnobancodedados.Esseautomóvelteráasinforma çõesque
ousuáriopreenchernatela.Entãooprimeiropassoéfazercomqueosdados
cheguemdealgumamaneiraao Managed Bean.
Agoraquesabemosquepararelacionaratelacomo Managed Beanbasta
ligá-losatravésdaExpression Language,ficafácilinferirquetemosquefazer
omesmoparaos inputs.
50
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 67

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
Vamos adicionar o atributovalue aos inputs, indicando qual pro-
priedadedo Managed Beanirárecebercadaumdosvalores. Comessaal-
teração,oformulárioficarácomoseguintecódigo:
Marca:
<h:inputText value="#{automovelBean.marca}"/>
Modelo:
<h:inputText value="#{automovelBean.modelo}"/>
Ano de Fabricação:
<h:inputText value="#{automovelBean.anoFabricacao}"/>
Ano do Modelo:
<h:inputText value="#{automovelBean.anoModelo}"/>
Observações:
<h:inputTextarea value="#{automovelBean.observacoes}"/>
<h:commandButton value="Salvar"
action="#{automovelBean.salva}"/>
Comisso,énecessárioapenastermososatributosno ManagedBeancom
seusrespectivos getterse setters:
@ManagedBean
public class AutomovelBean {
private String marca;
private String modelo;
private Integer anoFabricacao;
private Integer anoModelo;
private String observacoes;
public String getMarca() {
return this.marca;
}
public void setMarca(String marca) {
this.marca = marca;
51
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 68

3.4. PassedadosdatelaparaoManagedBean CasadoCódigo
}
// outros getters e setters
// método salva
}
Apenasissojáéosuficienteparaconseguirmosreceberosdadosno
nosso AutomovelBean,porém,aindaháalgoquepodesermelhoradonesse
código. Nocapítulo1,criamosaclasse Automovel,quejápossuíatodos
essesatributos. Comisso,podemosdeixardeteressasváriasinforma ções
naclasse AutomovelBeanedeixarapenasumatributo,nocaso,oatributo
Automovel:
@ManagedBean
public class AutomovelBean {
private Automovel automovel = new Automovel();
public Automovel getAutomovel() {
return this.automovel;
}
public void setAutomovel(Automovel automovel) {
this.automovel = automovel;
}
// método salva
}
Parafinalizar,bastaajustarmososcamposdoformuláriono xhtmlpara
usaronovoatributo automovelemvezdosdiversosatributosquetínhamos
antes.Assim,cadacampodoformuláriodeveráserrelacionadocomseure-
spectivoatributodentrode automovel:
Marca:
<h:inputText value="#{automovelBean.automovel.marca}"/>
Modelo:
<h:inputText value="#{automovelBean.automovel.modelo}"/>
52
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 69

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
Ano de Fabricação:
<h:inputText value="#{automovelBean.automovel.anoFabricacao}"/>
Ano do Modelo:
<h:inputText value="#{automovelBean.automovel.anoModelo}"/>
Observações:
<h:inputTextarea
value="#{automovelBean.automovel.observacoes}"/>
<h:commandButton
value="Salvar" action="#{automovelBean.salva}"/>
OqueacontecequandooformulárioésubmetidoéqueoJSFavaliaas
Expression Languagese“percebe”queprimeiroprecisaconseguiroManaged-
Bean automovelBean.
Umavezqueconseguiuumainstânciado Managed Bean,elecontinua
avaliandoaquelaexpressãoepercebequeprecisaconseguirum automovel
a partir daqueleautomovelBean. É aí que entra em ação o método
getAutomovelno Managed Bean,poisoJSFvaichamá-lo.
Agoraquechegouaoúltimoníveldaexpressãoeelejáconseguiuoob-
jeto automovel,oJSFiráchamaro setadequadoparacadapropriedade.
Então,paraamarca,oJSFchamaráo setMarcaenviandocomoparâmetro
ainforma çãodigitadanoformulário.Eassimfaráparaosoutroscampos.
Cuidado com aNullPointerException
Émuitocomumesquecermosdeinstanciaroobjetologonoatrib-
utoounoconstrutordo Managed Bean. Nessecaso, quandoofor-
muláriofossesubmetido,oJSFrecuperariaareferênciaparaaqueleob-
jeto, atravésdogetter, porém, eleestarianulo. Emseguida, tentaria
chamaro setteradequadoparaaquelapropriedade.Pronto,temosuma
NullPointerExceptionemnossaaplica ção.
Paraevitarcairnisso,lembre-sesempredeteroobjetopreviamente
instanciado.
53
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 70

3.4. PassedadosdatelaparaoManagedBean CasadoCódigo
Podemosinclusive,nométodo salva,pedirparamostraralgumasin-
formaçõesdoautomóvel. Assim,quandoseclicaremsalvar,veremosessa
informaçãonasaídadoservidor:
@ManagedBean
public class AutomovelBean {
private Automovel automovel = new Automovel();
// getter e setter
public void salva() {
System.out.println("Marca: " + automovel.getMarca());
}
}
Aodigitarmos“Ferrari”nocampoMarcaesubmetermosoformulário,o
logdoservidordeveráexibiramensagem:
Marca: Ferrari
Notetambémqueaosubmeteroformuláriooscamposvoltampreenchi-
doscomasinforma çõesqueforamsubmetidas. Issoaconteceporque,ao
começaragerararesposta,quenocasoseráamesmapágina,arenderiza ção
passapelos inputsdefinidosnoformulário.Comoelesestãoligadoscomas
propriedadesdo Managed Beanqueforampopuladasnasubmissãodofor-
muláriopeloatributo value,nahoraderenderizaroscampos,oJSFvai
buscarovalor,tambémdefinidonomesmoatributo valuedos inputs.
Nessemomento,oJSFnovamenteavaliaa Expression Language,primeiro
recuperandoo automovelBean,emseguidapegandoo automovelatravés
do getAutomovelno automovelBean,edepoiselerecuperaasinfor-
maçõesdesseautomóvel,chamandoo getterparacada inputligadoao
Managed Bean.
54
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 71

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
Fig.3.4:Formuláriocomvalorespreenchidos
3.5 Como receber os parâmetros direto no
método
No Managed Bean AutomovelBean, quando precisamos receber os
parâmetrosdarequisi ção,criamosumatributoedefinimosseu gettere setter.
Apartirda Expression Language2.2,utilizadopeloJBoss7eoTomcat7,por
exemplo,nãoprecisamosmaisdo setter.Comisso,épossívelfazercomque
ométododefinidona actiondobotãorecebaoparâmetro.
Dessa maneira, teremos no método salva um novo
parâmetro do tipo Automovel, e no xhtml vamos
referenciá-lo através do automovel do Managed Bean :
#{automovelBean.salva(automovelBean.automovel)}. Dessa
forma,teremosno Managed Bean:
@ManagedBean
public class AutomovelBean {
private Automovel automovel = new Automovel();
// getter
public void salva(Automovel automovel) {
// agora o método passou a receber automovel
}
}
Eo xhtmlindicandooparâmetroparaométododo Managed Bean:
55
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 72

3.6. Gravaçãodoautomóvelnobancodedados CasadoCódigo
<h:commandButton value="Salvar"
action="#{automovelBean.salva(automovelBean.automovel)}"/>
3.6 Grav ação do automóvel no banco de dados
Nessemomento,temoso Managed Beancomummétodo salvapreparado
para receber parâmetros, que, no nosso caso, será um objeto do tipo
Automovel. Nocapítulo2,configuramosoHibernateeaJPAefizemoso
cadastrodeumprimeiroautomóvelnobancodedados.Vamosusaraclasse
JPAUtilcriadanaquelecapítuloparanosforneceruma EntityManager
ecomisso,podemosfazerapersistênciadosdadosinformados.
O primeiro passo é, no método salva, conseguirmos uma
EntityManagerpormeioda JPAUtil:
@ManagedBean
public class AutomovelBean {
private Automovel automovel = new Automovel();
// getter e setter
public void salva() {
// conseguimos a EntityManager
EntityManager em = JPAUtil.getEntityManager();
}
}
Umavezcoma EntityManageremmãos, bastapersistiroobjeto
automovel,envolvendoapersistênciaemumatransa ção:
@ManagedBean
public class AutomovelBean {
private Automovel automovel = new Automovel();
// getter e setter
public void salva() {
// conseguimos a EntityManager
EntityManager em = JPAUtil.getEntityManager();
em.getTransaction().begin();
56
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 73

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
em.persist(automovel);
em.getTransaction().commit();
}
}
Um último passo, extremamente importante, é fecharmos a
EntityManager que foi aberta, dessa forma, não mantemos recursos
emusodesnecessariamente:
public void salva() {
// conseguimos a EntityManager
EntityManager em = JPAUtil.getEntityManager();
em.getTransaction().begin();
em.persist(automovel);
em.getTransaction().commit();
em.close();
}
Pronto,comissoconseguimospersistiroprimeiroautomóvelapartirda
nossaaplica çãoJSF.Éimportantenotarqueocódigoescritopoucodiferedo
desenvolvidonocapítulo2. Nodecorrerdolivro,aprenderemosmelhores
formasdesetrabalharcomessecódigodepersistênciaetambémcomofazer
umcontroledetransa çõesmaistransparenteesimplificado.
3.7 Liste os dados com o dataTable
Uma vez que temos os dados gravados no banco de dados, precisamos
mostrá-losparaosusuários. Portanto,vamosexibi-lasemumatabela,que
listarátodososautomóveisqueestãogravadosnobancodedados.Aofinal
dodesenvolvimento,teremosumatelaparecidacomafigura3.5.
57
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 74

3.7. ListeosdadoscomodataTable CasadoCódigo
Fig.3.5:ListagemdeAutomóveis
Oprimeiropassoparaaconstru çãodessatabelaécriarmosumnovo
xhtml,quepodemoschamarde listaAutomoveis.xhtml.Essearquivo
possuiomesmocabe çalhoimportandoaTagdoJSFqueoformuláriode
cadastro:
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://java.sun.com/jsf/html">
<h:body>
</h:body>
</html>
AgorapodemosconstruiratabelacomoJSFatravésdeumnovocom-
ponente, o dataTable. Como o próprio nome diz, o objetivo desse
componenteéexibirdadostabulares,tambémconhecidoscomo grids. O
dataTableprecisaquesejafornecidoumobjetoparaele,atravésdoatrib-
uto value,quenonossocasoseráumalistacomoselementosquedevem
serusadosnalistagem.
A listacom os elementosdeve ser recuperadade umManaged Bean
e,comocontinuamostrabalhandocomautomóveis,utilizaremosomesmo
AutomovelBeande antes. Dessa forma, precisamos ligar ovaluedo
dataTablecomumalistadeautomóveisno AutomovelBean.Oprimeiro
passo,écriarmosalistano Managed Beaneseurespectivo getter,quefaráa
consultanobancodedados:
@ManagedBean
public class AutomovelBean {
58
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 75

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
private Automovel automovel = new Automovel();
private List<Automovel> automoveis;
public List<Automovel> getAutomoveis() {
EntityManager em = JPAUtil.getEntityManager();
Query q = em.createQuery("select a from Automovel a",
Automovel.class);
this.automoveis = q.getResultList();
em.close();
return automoveis;
}
// método salva(), getter e setter do automovel
}
Códigos de persistência dentro do Managed Bean
Muitosdesenvolvedoressãocontracolocarcódigosqueenvolvam
JDBC,JPAe queriesdobancodedadosdentrodeclassesqueauxiliam
notrabalhocomoframework,comoo Managed Bean.Justamentepara
essescasos,diversosdesenvolvedorestendemausarclassesparaencap-
sularessastarefas,fazendoopapeldeumDAO( Data Access Object)ou
umrepositório.
Nase ção4.2vamosvercomofazeressaorganiza ção.
Agoraquetemosométodo getAutomoveisquedevolvealistarecém
buscadadobancodedados,podemosapontaro dataTableparaele:
<h:dataTable value="#{automovelBean.automoveis}" />
Paramontarmosessatabela,vamosprecisardizerquaiscolunasquere-
mosequaisinforma çõesdeverãosermostradasnelas.Então,vamosdefinir
umavariávelquevaiidentificarcadaumdosautomóveisbuscadosparaserem
exibidos.Vamoschamaressavariávelde automovelpeloatributo vardo
dataTable:
59
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 76

3.7. ListeosdadoscomodataTable CasadoCódigo
<h:dataTable
value="#{automovelBean.automoveis}" var="automovel"/>
Agora,dentrodessatabela,podemoscriaraprimeiracoluna,atravésda
Tag h:columnecolocaroconteúdoquedeverásermostradodentrodela:
<h:dataTable
value="#{automovelBean.automoveis}" var="automovel">
<h:column>
#{automovel.marca}
</h:column>
</h:dataTable>
Pronto,játemosumatabelaque,quandoatelaéacessada,mostrauma
listacomamarcadecadaumdosautomóveiscadastrados.Paracriarnovas
colunas,bastariarepetirblocosdaTag h:column:
<h:dataTable
value="#{automovelBean.automoveis}" var="automovel">
<h:column>
#{automovel.marca}
</h:column>
<h:column>
#{automovel.modelo}
</h:column>
<!-- outros colunas -->
</h:dataTable>
Nesseinstante,temosumatabelacomoamostradapelafigura3.6:
60
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 77

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
Fig.3.6:ListagemdeAutomóveissembordaecabe çalho
Notequeficouconfusodistinguiroquecadaumadascolunasrepresenta.
Nãotemosumaidentifica çãodoqueacadaumadelasserefere.Pararesolver
esseproblema,podemosadicionarumabordaparasepararcadacélulaeum
cabeçalhoacadacolunaparaidentificarseuconteúdo.
Adicionarabordaémaissimples,entãofaremosissoprimeiro. Como
nossapreocupa ção,porenquanto,nãoé layout,bastaadicionar border="1"
nanossa h:dataTable.
<h:dataTable value="#{automovelBean.automoveis}" var="automovel"
border="1">
<!-- colunas aqui dentro -->
</h:dataTable>
Comessaaltera çãooresultadoserácomonafigura3.7.
Fig.3.7:ListagemdeAutomóveiscombordaesemcabe çalho
Agorasimvamosadicionarocabe çalhodecadacoluna. Paraisso,pre-
cisamosmodificarumacaracterísticado h:column,queéoseucabe çalho.
Essascaracterísticasqueoscomponentespossuem,quenãonecessariamente
sãovisuais, sãooquechamamosdefacetas, asquaispodemosmodificar
atravésdeumnovocomponentechamado facet.
61
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 78

3.7. ListeosdadoscomodataTable CasadoCódigo
Oobjetivodo facetéapenasmudaracaracterísticadeumoutrocom-
ponente,nocasoo h:column,enãonecessariamentegerarcódigoHTML.
Justamente por isso, essa Tag não fica sob onamespace h. Precisamos
importá-ladeoutrolugar.Apartirdessemomento,temosqueusaraTaglib
coredoJSF,queéquempossuiasTagsquenãogeramconteúdoHTML:
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<h:body>
<h:dataTable value="#{automovelBean.automoveis}"
var="automovel" border="1">
<!-- colunas aqui dentro -->
</h:dataTable>
</h:body>
</html>
Pronto,agoraqueimportamosanovaTaglibpormeiodoprefixo f,pode-
mosusaraTag facetindicandoqualacaracterísticaqueseráalterada,que
nessecasoéocabe çalhodacoluna:
<h:column>
<f:facet name="header">
Marca
</f:facet>
#{automovel.marca}
</h:column>
Quandofazemososcabe çalhosparatodasascolunas,temosumatela
comoadafigura3.8.
62
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 79

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
Fig.3.8:ListagemdeAutomóveiscombordaecabe çalho
Sequiséssemos,poderíamosmudarmaiscaracterísticas,comoumro-
dapé,atravésda facetchamada footer.Cadacomponentepodepossuir
facetasdiferentes,portantoéimportanteficaratentonomomentodeusá-lo.
3.8 Mas minha listagem está executando v árias
consultas no banco ...
Agoraquetemosalistaprontaefuncionando,nãotemosmaisnadaparamel-
horarnessatela,certo?Errado!Existeumafalhagravíssimanessafuncional-
idadequepodefazercomqueoprojeto,aosercolocadoemumambientede
produção,tenhabaixaperformanceeatémesmoquasenenhumaescalabili-
dade,dependendodocaso.
SeanalisarmosoregistrodasconsultasqueaJPAestádisparandono
bancodedados,podemosrepararque,quandotemosmaisdeumainfor-
maçãono dataTable,ele fazumaconsultaparacadalinhadessatabela .
Ouseja,setivermosumatabelacom100linhas,serãodisparadas100consul-
tasnobancodedados,oqueéinaceitávelparaqualqueraplica ção.
IssoacontecedevidoaofuncionamentointernodoJSF,queinvocao
método getAutomoveisparacadalinhado dataTable.Comosolu ção,
podemosprotegeranossaconsultaesófazê-lanaprimeiravezquechamado
o getAutomoveis.Assim,nasvezesseguintes,apenasalistabuscadaante-
riormenteédevolvida.
Essa é uma alteração simples de ser feita: basta que no método
getAutomoveis,antesdefazeraconsulta,um ifverifiquesealistajáestá
populadaounão. Casoestejavazia,oquevaiacontecernaprimeirainvo-
63
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 80

3.9. ExclusãodedadoseocommandLink CasadoCódigo
cação,aconsultadeveserfeita-casocontrário,apenasdevolvealistasem
realizaraconsulta:
@ManagedBean
public class AutomovelBean {
private List<Automovel> automoveis;
public List<Automovel> getAutomoveis() {
if(this.automoveis == null) {
EntityManager em = JPAUtil.getEntityManager();
Query q =
em.createQuery("select a from Automoveis a",
Automovel.class);
this.automoveis = q.getResultList();
em.close();
}
return automoveis;
}
// atributos, método salva(), getter e setter do automovel
}
Reparequeagora,dentrodométodo getAutomoveis,antesdefazera
consulta,verificamosseoatributo automoveisjáfoipopulado.Casotenha
sido,significaqueaconsultafoifeitaeapenasdevemosdevolveroquefoi
consultadoanteriormente.
3.9 Exclusão de dados e o command Link
Parafinalizar,vamospermitiraexclusãodositens. Paraissoprecisaremos
adicionarumacolunaqueiráconterolink“excluir”.Chamaremosessacoluna
de“Ações”,jáquefuturamentepoderemosadicionaroutrasoperaçõesparaa
mesmalinha,comoeditaroudesabilitar.
Olinkéconstruídopormeiodocomponente commandLink,quefun-
cionaquasecomoo commandButton,mudandoapenasaformadevisual-
ização,quepassaaserum linkemvezdeumbotão.Vamosdefinirtambéma
64
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 81

CasadoCódigo Capítulo3. PrimeirospassoscomoJSF
actiondesse linkparaenviaro automovelqueforclicadonatabelacomo
parâmetroparaummétododeexclusãodentrodo Managed Bean:
Comisso,ocódigoparaanovacolunaficarácomo:
<h:column>
<f:facet name="header">Ações</f:facet>
<h:commandLink action="#{automovelBean.exclui(automovel)}">
excluir
</h:commandLink>
</h:column>
Uma regra com relação aos componentes commandLink e
commandButtonéqueelesdevemsempreaparecerdentrodeum form,
casocontrárioelesnãofuncionam.Porisso,vamosenvolvero dataTable
dentrodeumformulário:
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<h:body>
<h:form>
<h:dataTable value="#{automovelBean.automoveis}"
var="automovel">
<!-- colunas -->
</h:dataTable>
</h:form>
</h:body>
</html>
Por fim, falta a implementação do método exclui dentro do
AutomovelBean:
public void excluir(Automovel automovel){
EntityManager em = JPAUtil.getEntityManager();
EntityTransaction tx = em.getTransaction();
65
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 82

3.10. OprimeiroCRUDintegrado CasadoCódigo
tx.begin();
automovel = em.merge(automovel);
em.remove(automovel);
tx.commit();
em.close();
}
Nesseexemplo,ométodo mergeéprecisoparadevolveroobjetoaoes-
tadogerenciado.Masnãosepreocupe,nocapítulo4veremosoqueissosig-
nifica.
3.10 O primeiroCRUD integrado
Apesardesimples,essecapítuloserviuparafazermosumCRUDquasecom-
pleto.Aindafaltaaaltera çãoqueintegraoJSFeaJPA.
Compoucotrabalhodecodifica çãojátemosalgumasfuncionalidades.
Nospróximoscapítulosnosaprofundaremosmaisnosprincípiosdecada
framework,entenderemoscomoasferramentas“pensam”efuncionam,além
deevoluirmosmaisaindananossaaplica ção.
66
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 83

ParteII
Domineasferramentas
ApósumprimeirocontatocomJSFeJPAéhoradeentenderedominar
essasferramentas.
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 84

E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 85

Capítulo4
EntendendoaJPA
Nocapítulo2,nósiniciamosumprojetousandoJSFeJPA.Tivemoscon-
tatocomele,vendoapenasomínimonecessárioparaconseguirmosfazer
ummapeamentoextremamentesimplescomJPA,bemcomotelasigualmente
simplescomJSF.Nãovimosconceitos,nãoentendemoscomoascoisasfun-
cionam,apenasfomosláeusamos.
Apartirdeagora,aprenderemosmuitomaissobreaJPA.Veremosociclo
devidadosobjetosgerenciadospelaJPA,comorealizarconsultascomplexase
váriositensaosquaisprecisamosficaratentosparanãousarmosaferramenta
deformaincorreta.
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 86

4.1. OpadrãodeprojetosDataAccessObject,ouDAO CasadoCódigo
4.1 O padrão de projetos DataAccessObject, ou
DAO
QuandonãoutilizamosJPAououtraferramentademapeamentoobjeto-
relacional,temosquelidarcommuitocódigodeinfraestrutura-abrirefechar
conexões,tratamentodeexce ções,SQL, PreparedStatementsetc. Esse
tipodecódigonosobrigaadarumavoltarelativamentelongaparachegar-
mosaocódigoquenosinteressa,queéonossocódigododomínio.
Paraquepossamossepararasresponsabilidadesetambémmelhorara
legibilidadedonossocódigo,pegamostodaalógicadeacessoadadosecolo-
camosemumaclassequetenhaissocomosuarazãodeexistir,oDAO.
Essaclassetemaresponsabilidadedeproverparaaaplica çãoopera ções
deacessoadados,comoleitura,inclusão,altera çãoeexclusão.
Utilizandoboaspráticasde design,comoprogramarorientadoainter-
facesenãoaimplementa ções,usamosumainterfaceparaasopera çõesde
dadosqueprecisamosedeixamosaimplementa çãodesacopladadonosso
código.Issonospossibilitatrocardeimplementa çãosemalterá-lo.
Aflexibilidadeétantaquenocasomaissimplespodemosterimplemen-
taçõesdomesmoDAOparabancodedadosdiferentesouparamecanismos
diferentesdebancosrelacionais,comoosbancos NoSQLoumesmoarquivos
texto.
Atrocadobancodedadosduranteavidadeumprojetoérara,maspode
acontecer-játiveessaexperiência. Noentanto,essafacilidadedetrocade
bancoacabanãosendoumapeloforteparaousodopadrãoDAOpordois
motivosprincipais.Oprimeiroéque,comojádito,issoémuitorarodeacon-
tecer.EosegundoéquecomaJPAtemosapossibilidadedemudardebanco
comoumacaracterísticadaferramenta.
Uma vez que nossos objetos estão mapeados (mapeamento objeto-
relacional),devemostrabalharapenasorientadosaobjetos,eissonosdeixa
livresparamudardebanco.Nocasoemquepassei,porexemplo,nãofoipre-
cisomudarnenhumalinhadecódigonemmesmodoDAO,porqueaJPAfez
bemoseupapel. Então,emquecasooDAOaindasefazútil ?
UmcasoemqueoDAOsefazútil,hoje,équandoprecisamosmudar
deumbancorelacionalparaumnãorelacional,jáqueaJPAnãotemcomo
70
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 87

CasadoCódigo Capítulo4. EntendendoaJPA
focotrabalharcomessetipodebancodedados.Porém,assimcomoháuma
décadaatrásmudardebancodedadoseraofatormotivadordousodoDAO
ehojenãoémais,emalgumtempomudardemecanismodepersistência,
comomudardebancorelacionalparabanconãorelacional,podetambém
deixardesê-lo.Jáexistemprojetosquetêmcomoobjetivoutilizarasmesmas
anotaçõesdaJPAparaprovermapeamentodeobjetosparaumbanconão
relacional.
Apesar de o assunto de uso ou não de DAO hoje em dia ser muito
polêmico,éfatoqueaoutilizá-loseparamosmelhorasresponsabilidades,
principalmentequandotemosopera çõesderecupera çãodedadosquesão
maiscomplexasqueexecutarumaconsulta.
4.2 JPA não é um DAO genérico, é contextual
Muitaspessoasestãofamiliarizadascomodesenvolvimentodesistemasque
acessambancodedadosatravésdeDAOs. Aevolu çãonaturaldosprojetos
foitrocaraJDBCporJPAnaimplementa çãodessesDAOs,masmuitasvezes
aspessoasacostumadasautilizaressesobjetosnãocompreendiamqueaJPA
nãoerasóumaAPIquenosajudaaterDAOsgenéricoseagerarSQLsde
maneiramaisfácil.
Háumagrandediferen çaentreessasAPIs.Talveznessecaso,opapeldas
interfacesdedeixarqueousuáriodoDAOnãoprecisesabernadadasua
implementaçãotenhacontribuídoparasistemascomcomportamentoines-
perado.Obviamentequeasepara çãoderesponsabilidadeseaabstra çãoque
asinterfacesnosproporcionamsãobenéficas,nãohádúvidasemrela çãoa
isso.
OcasoéquemudarachavedeJDBCparaJPAnãoétãotrivial.Épreciso
queentendamosasdiferen çasenvolvidas,eéparaissoestecapítuloserve.
Paraquetenhamosalgomaispalpávelparaanalisar,observeocódigoa
seguir,queéomesmo Managed Bean,dessavezutilizandooDAO.
@ManagedBean
public class AutomovelBean{
private AutomovelDao dao;
private Automovel automovel = new Automovel();
71
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 88

4.2. JPAnãoéumDAOgenérico,écontextual CasadoCódigo
public AutomovelBean(){
// caso 1
dao = new JdbcAutomovelDao();
// caso 2
dao = new JpaAutomovelDao();
}
public void salvar(Automovel automovel){
dao.salvar(automovel);
}
}
Comoépossívelver,noconstrutortemosduasop çõesdeinstancia çãode
DAO.Aprimeiraop çãoseriaaimplementa çãoviaJDBCeasegundaviaJPA.
ComotudoestáencapsuladodentrodoDAO,hápouquíssimoimpactoem
nosso Managed Bean.
Paratirar,porenquanto,asespecificidadesdaWebetratarmosapenas
deJPA,vamosimaginarumcenárioquepoderiaperfeitamenteserexecutado
atravésdo Managed Beanapresentadoanteriormente. Paravermosmelhor,
separeiotrechodeformalinear.
Fluxodeexecu çãoquerepresentaousuáriosalvandooautomóvel.
// inicia a transação
AutomovelDao dao =
new // JdbcAutomovelDao() ou JpaAutomovelDao();
Automovel automovel = dao.buscarPorId(100);
automovel.setAnoFabricacao(1996);
dao.salvar(automovel);
// finaliza a transação
Nosdoiscasosestamosrepresentandoocenárioondeousuárioseleciona
algumautomóvelparaatualizar,depoismudaseuanodefabrica çãoeem
seguidaapertaobotãosalvar.
72
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 89

CasadoCódigo Capítulo4. EntendendoaJPA
TantooDAOimplementadocomJDBCquantoocomaJPAterãocom-
portamentosparecidos,masnosegundocasoéquevemaprincipaldiferen ça,
equepormuitasvezesassustaqueminiciaemJPA.
Naimplementa çãocomJDBC,oautomóveldevolvidoéumobjetocomo
qualqueroutro,ouseja,nãohánadaqueovinculecomobancodedados.
Então,quandorealizarmosalgumamodifica çãonesseobjetoeoabandonar-
mos,eleprovavelmenteseráremovidopelocoletorde Garbage Collectoreo
bancodedadosnuncasaberádessaaltera ção.
Já quando buscamos um objeto através da JPA, ele fica vinculado à
EntityManagerqueobuscounobanco.
Essa EntityManagerpassaateraresponsabilidadedemanteresseob-
jetoatualizadocomobancodedados. Sealteramosqualqueratributodele,
pormeiodovínculoqueeletemcoma EntityManager,eleacabarásendo
salvonobanco.
Paraissoacontecernãoprecisamospedirnovamentequeoobjetoseja
salvoousincronizadocomobanco. Inclusiveseolharmososmétodosda
interface EntityManager,veremosqueexisteummétodoparasalvarou,
deacordocomostermosusadospelaespecifica ção,parapersistiroobjeto,o
persist,masnãotemosummétodochamado update,porexemplo.
Issoaconteceporquerealizaraatualiza çãofazpartedasresponsabilidades
da EntityManager,bastandoqueexistaumatransa çãoparaisso,jáqueé
elaquem“dispara”aescritanobancodedados.Estaé,inclusive,outradifer-
ençaemrela çãoaJDBC:aJPAsóescrevenobancosehouvertransa ção;já
utilizandoJDBC,apesardeserpossível,ousodetransa çõeséopcional.
AlgunsdesenvolvedoresquejáseaventuraramcomaJPAantestalvezjá
tenhamouvidofalardométodo mergeedevemseperguntarseelenãoseria
oequivalenteao update,quedissemosquenãoexiste.Arespostaparaessa
perguntaénão,masvamosvermelhoroporquêestudandoociclodevidade
umobjetoquandoeleégerenciadopelaJPA.
4.3 Ciclo de vida de um objeto naJPA
NaJPA,todoobjetopassaporumciclodevidaquecontempladesdeomo-
mentoemqueeleéinstanciadopelaprimeiravezcom new,passandopelo
73
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 90

4.3. CiclodevidadeumobjetonaJPA CasadoCódigo
momentoemqueeleésalvonobancoepodechegaratéquandoeleére-
movidodobancodedados.
Afigura4.1serveparamostrarospossíveisestadosdeumobjeto,equal
métododainterface EntityManagerutilizamosparafazeressastransi ções.
Fig.4.1:CiclodevidadeumobjetonaJPA
Quandocriamosumobjetopelaprimeiravezeeleaindanãopassoupela
JPA,dizemosqueeleestánoestado New(novo).
Paraquenossoobjetosetorneumobjetopersistente,precisamospassá-lo
paraoestado Managed(gerenciado)eparaissodevemoschamarométodo
persist.
Umaoutramaneiradeconseguirmosumobjetogerenciadoécomo
métodomerge,porémtemosquenosatentarparaumadiferen çaimportante
entre persisteo merge:
EntityManager em = JPAUtil.getEntityManager();
// cria o porsche no estado new
Marca porsche = new Marca("Porsche");
// passa o porsche para estado gerenciado
74
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 91

CasadoCódigo Capítulo4. EntendendoaJPA
em.persist(porsche);
// cria a ferrari no estado novo
Marca ferrari = new Marca("Ferrari");
//devolve a instância gerenciada
Marca outraFerrari = em.merge(ferrari);
// vai imprimir false
System.out.println(ferrari == outraFerrari);
Ométodo persistfazcomqueoobjetopassadosejagerenciado,en-
quantoométodo mergeretornaoobjetoqueégerenciadoenãofaznada
comoobjetopassado.
Agoraquenossoobjetoestágerenciado,eleestánoestadoemqueaJPA
mantémumsincronismoentreoobjetoeobancodedados. Porém,como
acabamosdepassaresseobjetoqueeranovoparagerenciado,elesóvaide
fatoparaobancoquandofizermos commitnatransa ção.
Outraformadetermosobjetos Managedépormeiodasbuscasnobanco.
Todaentidaderetornadaéentregueemestadogerenciado.
Tendonossoobjetoemestadogerenciado,podemosremovê-lodobanco
atravésdométodoremove.Feitoisso,oobjetopassaparaoestado Removed,
mas,novamente,o deletenobancodedadossóérealizadoapóso commit.
Umdosestadoscomquemaislidaremosnocotidianoéo Detached.Ob-
jetosdetachedsãoobjetosquejáforamgerenciados,ouseja,queexistemno
bancodedados,masa EntityManagerqueostrouxedobancodedados
jáfoifechada,ouexplicitamentedesanexouoobjetodoseucontextoviao
método detach.
Mudançasfeitasemobjetos detachednãosãoatualizadasnobanco.Para
queissoocorraénecessárioretornaroobjetoparaoestadogerenciadoatravés
dométodo merge.Notrechodecódigoaseguirveremosmaisdetalhesdo
funcionamentodo detached.
EntityManager em = JPAUtil.getEntityManager();
em.getTransaction().begin();
75
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 92

4.3. CiclodevidadeumobjetonaJPA CasadoCódigo
// Busca o porsche
Modelo porscheDetached = em.find(Modelo.class, 1);
// Desanexa o porsche
em.detach(porscheDetached);
// Modificamos o objeto que está detached
porscheDetached.setDescricao("Porsche 911 Turbo");
porscheDetached.setPotencia(500);
// Buscamos uma instância gerenciada da mesma informação
Modelo porscheGerenciado = em.find(Modelo.class, 1);
// Modificamos o que acabamos de buscar
porscheGerenciado.setDescricao("Porsche 911 T.");
// Reanexa o porsche que havíamos modificado lá no começo
Modelo porscheModificado = em.merge(porscheDetached);
// O porsche detached não é o mesmo objeto que o porsche
//modificado
System.out.println(porscheDetached != porscheModificado);
// O porsche gerenciado é o mesmo objeto que o porsche
//modificado
System.out.println(porscheGerenciado == porscheModificado);
em.getTransaction().commit();
Ocódigoacimaserveparanosmostrarporqueométodo mergede-
volveumainstânciaemvezdemodificarainstânciapassadaporparâmetro.
Seemvezderetornar,o mergetransformasseaprópriainstânciapassada
porparâmetro,aconteceriaumconflitonocontextoda EntityManager
quandoadicionássemoso porscheDetached,vistoqueessemesmocon-
textojápossuíaainstância porscheGerenciado.
Se a EntityManager permitisse duas instâncias gerenciadas de
Modelocom id=1, qualseriao updatenomomentodo commitda
transação?Qualobjetoconsiderar?
76
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 93

CasadoCódigo Capítulo4. EntendendoaJPA
Paraquenãohajadúvidas,a EntityManagertemsempreumúnico
objetogerenciadodomesmotipoecomomesmo id.Poressemotivo,em
vezdepassarainstância porscheDetachedparagerenciado,comoelajá
tinhaumainstânciagerenciada, porscheGerenciado,a EntityManager
usouesseobjetocomobaseejogouasaltera çõesfeitasnoobjeto detachedem
cimadogerenciado.
Écomoseasaltera çõesfeitasnosPorschesfossemrealizadasnoobjeto
porscheGerenciado.Naverdadeissofoifeitodentrodométodo merge.
Comoainstânciaestágerenciadaefoialterada,nomomentodo commitela
serásincronizadacomobanco,ouseja,ocomando updatedoSQLseráfeito.
4.4 AJPA v ai mais além do que um simples execu-
tar de SQLs
AcabamosdeperceberqueaJPAfazmaiscoisasalémdeexecutarSQLs.Ela
mantémumaorganiza çãoentreosnossosobjetosatravésdessecontroledo
ciclodevidadeles.Éimportantíssimoentendertodoessecicloparaqueseja
possívelaprenderoutrospontosprimordiaisdaJPA.
77
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 94

E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 95

Capítulo5
Comomapeartudo...ounada!
ApartirdeagoraveremoscomomapearnossomodeloOrientadoaObjetos
paraorelacional.Normalmente,existeumfatorprincipalqueinfluenciabas-
tantenonossomapeamento,queéousodeumbancodedadosnovooude
umexistente.
Quandovamoscriarumaaplica çãonova, quenãoiráreutilizarnen-
humbancoexistente,costumamostermaiorliberdadeparaapenasrefletir
nobancoasdecisõesde designdasnossasclasses. Comisso,geralmenteo
mapeamentoémínimo,eutilizamosmuitooscomportamentospadrõesda
JPA.
Outrasitua çãoéquandoprecisamosmapearumbancodedadosex-
istente,especialmentequandoseguepadrõesdenomenclaturaedeestru-
turaprovenientesdemodeloEntidade-Relacionamentotradicional. Com
issopodemosentenderqueasentidadesgeralmenteterãosuachaveprimária
definidaporumconjuntodeatributosque,combinados,tornaaentidade
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 96

CasadoCódigo
única.Porexemplo,vamosconsideraraclasseabaixorepresentandoavenda
deumautomóvel.
Fig.5.1:Classevenda
Arespectivatabelaresponsávelporarmazenarnobancodedadososda-
dosdessaclassepodeseralgocomo:
Fig.5.2:DERcomnomesabreviadosechavecomposta
Podemosnotarquefoidefinidaumachavecompostaqueidentificauma
vendacomoúnica. Noexemplo,identificamosqueumavendaérepresen-
tadapelocódigodoautomóvelvendido,pelocódigodequemvendeuepelo
códigodequemcomprou,sendoqueessescódigossãochavesestrangeiras
que,combinadas,formamachaveprimária. Reparetambémnonomeda
tabelaenosnomesdascolunas,quegeralmenteseguemumpadrãoparecido
comoapresentado,emquemuitasvezesaspalavrassãoabreviadas.
Agoravamoscompararcomatabelaqueteríamosseutilizássemosapenas
asconven çõesdaJPA.
80
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 97

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
Fig.5.3:DERcomnomenclaturapadrãoJPA
Sãonotóriasasmudan çasnanomenclatura,queagorarefleteosmesmos
nomesutilizadosnaclasse.Mastalvezaprincipaldiferen çaseriautilizaruma
chaveprimáriaartificialemvezdachavequeutilizaosatributosjáexistentes
natabela.
Claroquenemsempreessaabordagemvaigerarchavescompostas.Por
exemplo,nocadastrodeumapessoa,achaveprimáriapoderiaseroCPFou
oe-mail.Masofatoéqueaabordagemdachaveartificialautoincrementada
temganhadomuitoespa ço.
Nessecapítulovamosvercomotrabalharcomomapeamento,paraque
eleseadequedamelhormaneirapossívelànossanecessidadedebancode
dados,sejaelamaispróximadasconven çõesdaJPA,sejaelatotalmentecus-
tomizada.
5.1 Definições de entidade
Comojávimosnocapítulo2,geralmentetemosaanota ção @Entitysobre
aclassecujasinforma çõesdosobjetosgostaríamosdepersistiremumbanco
dedados.Elassãooquechamamosde entidades.
Alémdaanotação @Entity,precisamosregistrarnossaclassenoarquivo
persistence.xml,comoaseguir.
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.0"
xmlns="http://java.sun.com/xml/ns/persistence"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
81
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 98

5.1. Definiçõesdeentidade CasadoCódigo
xsi:schemaLocation="http://java.sun.com/xml/ns/persistence
http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">
<persistence-unit name="default"
transaction-type="RESOURCE_LOCAL">
<class>facesmotors.entities.Automovel</class>
<properties>
...
</properties>
</persistence-unit>
</persistence>
Essepassohabilitaaentidadena persistence-unitdefault.
Pelaespecifica çãodaJPA,aoutilizarmosumservidordeaplica çõesJava
EE,nãoprecisaríamosespecificarasentidadesno persistence.xmldesde
quetivéssemosapenasuma persistence-unit. Naprática,asimple-
mentaçõesacabamestendendoissoparaoambienteJavaSE,comooque
estamos utilizando. Sendo assim, a declaração das entidades através do
persistence.xmléopcionalnanossaaplica ção.
Caso tenhamos mais de umapersistence-unit, declaramos to-
dasasentidadesemsuarespectiva persistence-unit. Noentanto,ele
continuarátentandocarregarasclassesautomaticamente,ecomisso,uma
persistence-unitpodeterclassescarregadasdeoutra. Umaconfusão
só!
Para evitarmos que se tente carregar automaticamente entidades que
não deveriam, já que não foram listadas nopersistence.xml, uti-
lizamos a configuração <exclude-unlisted-classes> com o valor
true, assim a JPA não tentará atribuir automaticamente entidades na
persistence-uniterrada.
Paraexemplificaraexistênciademaisdeuma persistence-unit,
considereasentidades Funcionarioe PrestadorServico.Oprimeiro
serefereaosfuncionáriosdaempresaetemseusdadosemumbancodeda-
dos. Osegundoserefereaumprestadordeservi çooufuncionáriotercei-
rizadoepossuiseusdadosarmazenadosemoutrobancodedados. Nesse
caso,aconfigura çãodo persistence.xmlficariacomoaseguir:
82
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 99

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
<persistence...>
...
<persistence-unit name="funcionarios"
transaction-type="RESOURCE_LOCAL">
<class>sistemarh.entities.Funcionario</class>
<exclude-unlisted-classes>true</exclude-unlisted-classes>
<properties>
...
</properties>
</persistence-unit>
<persistence-unit name="terceirizados"
transaction-type="RESOURCE_LOCAL">
<class>sistemarh.entities.PrestadorServico</class>
<exclude-unlisted-classes>true</exclude-unlisted-classes>
<properties>
...
</properties>
</persistence-unit>
</persistence>
Ecomissonenhumaclasseécarregadasemqueindiquemosqueelareal-
mentedevesercarregada.
5.2 Faça atributos não serem persistidos com o
@Transient
Por padrão, toda propriedade de uma entidade é persistente, a menos
queespecifiquemosocontrárioutilizandoaanota ção @Transientoua
palavrareservada transientnoatributo. Essaconfigura çãoéextrema-
menteútilquandotemosumcampoqueécalculado. Considereaentidade
Funcionario:
@Entity
public class Funcionario {
@Id @GeneratedValue
private Long id;
83
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 100

5.3. Mapeiechavesprimáriassimples CasadoCódigo
private Calendar dataNascimento;
private int idade;
}
Nessecaso,seutilizássemosessemapeamento,aJPAesperariaquehou-
vesseumatabelacom3campos: id, dataNascimentoe idade.Noen-
tanto,reparequeháumaredundânciaentreessescampos.Aidadepodefacil-
mentesercalculadaapartirdadatadenascimento.Imagineotrabalhoque
seriaterquemanterosdadosdaidadeatualizados.
Nessescasos,podemosindicarquea idadenãoserápersistidanobanco
dedados,atravésdaanota ção @Transient:
@Transient
private int idade;
Opcionalmente,podemosusarapalavrachave transient:
private transient int idade;
Pronto,agoraatabelapossuiapenasascolunas ide dataNascimento.
5.3 Mapeie chaves primárias simples
Tambémjávimossuperficialmentecomolidarcomchavesprimárias,mas
agoravamosnosaprofundar.Aconfigura çãomínimaéaanota ção@Id.
@Entity
public class Automovel {
@Id
private String placa;
//outros atributos e métodos
}
Nessecasoteremosumachaveprimárianaqualaprópriaaplica çãodeve
informarovalorantesdepersistirnobanco.Nonossoexemplo,utilizamosa
84
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 101

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
placadeumautomóvel,maspoderíamosutilizaroCPFcomochavedeuma
entidadechamada Pessoaeassimpordiante.
Chavescomvaloresautogerados
Noexemplodoautomóvel,porexemplo,poderíamostê-locadastrado
comainforma çãodaplacaerrada. Mascomosetratadachaveprimária,
mudar essa informação pode não ser tão simples, já que ela pode estar
sendo referenciada como chave estrangeira em outra tabela. Por isso, e
paraevitaracomplexidadedechavescompostas, équecadavezmaisse
temutilizadoaschavesautoincrementadas. Bastariaadicionaraanota ção
@GeneratedValue.
@Entity
public class Automovel {
@Id @GeneratedValue
private Integer id;
private String placa;
//outros atributos e métodos
}
Agoraaplacaéumatributocomoqualqueroutro,eadicionamosuma
chaveartificialque,devidoàpresen çadaanota ção @GeneratedValue,não
precisa-enãodeve-serinformadaquandoformospersistirum Automovel.
ApenascomissoaJPAjáirácomaestratégiadegera çãodevaloresde
cadabancodedados.EmalgunscasoscomoMySQLeSQLServeraJPAcriará
chavesdotipo auto-incremente identity,respectivamente.Emban-
coscomoPostgreSQLeOracleserãogeradas sequencesparaincrementar
achave.
Embancosquenãopossuemsuportea sequenceenemavaloresauto-
gerados,épossívelaindatermosumatabelanobancoquegerencieocontador
dachavedetodasasoutrastabelas.
Aessasdiferentesformasdeimplementarumachavecujoconteúdoé
gerenciadopelaJPAédadoonomede estratégia.
AJPApossuibasicamente4tiposdeestratégias: AUTO, IDENTITY,
SEQUENCEe TABLE.Noentanto, éimportantelembrarque SEQUENCE
85
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 102

5.3. Mapeiechavesprimáriassimples CasadoCódigo
e IDENTITYpodemnãosercompatíveiscomobancodedadosquevocê
estiverusando. Todasessasestratégiassãorepresentadasatravésda enum
GenerationType:
•DeixeaJPAescolher :
@Id @GeneratedValue(strategy=GenerationType.AUTO)
private Integer id;
Otipo AUTOnãochegaaserumaestratégiareal,elaserveparadeixara
JPAdecidiramelhorestratégiadependendodobancoutilizado,tendo
assimumamaiorportabilidade.Alémdisso,quandonãodefinimosa
estratégia,esseéovalorutilizado.
•Usevaloresautoincremento
@Id @GeneratedValue(strategy=GenerationType.IDENTITY)
private Integer id;
Especificandoaestratégiacomo IDENTITYforçamosaJPAautilizar
colunascomvaloresautoincrementáveis. Atente-seaofatodequeal-
gunsbancosdedadospodemnãosuportaressaop ção.
•Gerevaloresautoincrementoatravésdesequences
@Id @GeneratedValue(strategy=GenerationType.SEQUENCE)
private Integer id;
Nessecaso,estaremosconfigurandonossachaveparatrabalharcom
uma SEQUENCEdobancodedados.Ocomportamentopadrãoéuma
SEQUENCEglobalparaaaplica ção,emquetodasastabelascompartil-
hariamumamesmasequência.Porexemplo,aosalvarum Automovel
elereceberiaoid1;depoissalvandoum Acessorioelereceberiaid2;
eaosalvaroutro Automovelelereceberiaid3.
Emdiversoscasos,essaabordagemnãochegaaserumproblema,mas
podemosquererdeterminarumgeradordechaveespecíficoparacada
tabela;ouaindadeixartabelassimplescomogeradorglobalealgumas
86
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 103

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
específicascomumgeradorindividual. Parafazeressaconfigura ção,
bastadarmosumnomediferenteparacadageradorde idsquedese-
jarmos,peloatributo generatornaanota ção @GeneratedValue.
@Entity
public class Automovel {
@SequenceGenerator(name="automovelGenerator",
sequenceName="AUTOMOVEL_SEQ",
allocationSize=10)
@Id @GeneratedValue(strategy=GenerationType.SEQUENCE,
generator="automovelGenerator")
private Integer id;
//outros atributos e métodos
}
@Entity
public class Acessorio {
@SequenceGenerator(name="acessorioGenerator",
sequenceName="ACESSORIO_SEQ",
allocationSize=10)
@Id @GeneratedValue(strategy=GenerationType.SEQUENCE,
generator="acessorioGenerator")
private Integer id;
//outros atributos e métodos
}
Dessaforma,teremoscadaentidadeseguindoumasequênciade id
própria. Vimosaindaaanota ção @SequenceGenerator,queus-
amosparaespecificaralgunsdetalhesdasequência,comoonomeesua
allocationSize,ondedefinimos10.Issosignificaquea SEQUENCE
seráchamadapelaprimeiravezedevolverá1,masjáserãobuscados10
números.Paraospróximos9 id,elesserãobuscadosdamemória,e
apenasapósisso,a SEQUENCEseriachamadanovamente. Issoevita
diversasidasaobancoparagerarachave.Senãoespecificarmosnada,
otamanhopadrãoé50.
Uma outra opção interessante para o @SequenceGenerator
é a definição do valor inicial da sequência, através do atributo
87
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 104

5.4. Mapeiechavescompostas CasadoCódigo
initialValue.
•Useumatabelaauxiliar
public class Automovel {
@TableGenerator(
name="AUTOMOVEL_GENERATOR",
table="GENERATOR_TABLE",
pkColumnValue="AUTOMOVEL"
)
@Id @GeneratedValue(strategy=GenerationType.TABLE,
generator="AUTOMOVEL_GENERATOR")
private Integer id;
//outros atributos e métodos
}
Quandoutilizamosaestratégia Tabletemosumatabelaqueirágeren-
ciaraschavesdanossaentidade.Podemosterumamesmatabelapara
todoosistema,queirádiferenciarodonodachavepeloconteúdodo
atributo pkColumnValueda @TableGenerator.
Podemostambémtermaisdeumatabeladecontrole.Oúnicoatrib-
utoobrigatórioéonomedogerador,eparatodoorestopodemosnão
especificarnadaedeixaraconven çãofazerseutrabalho.
5.4 Mapeie chaves compostas
Emalgunscasospodemosterchavescompostasemnossasentidades.Issoé
comumquandomapeamosumbancopré-existente,mastambémpodeacon-
tecerquando,porexemplo,desejamosmapearumatabeladerelacionamento
muitosparamuitos.Esseúltimocasocostumaaparecerquandoprecisamos
terumatributonorelacionamento,eachavedessaentidadeserácomposta
dasduaschavesdorelacionamento.
Obviamente podemos ter chaves compostas em outros casos, mas
como exemplo tomaremos um relacionamento muitos para muitos de
Consumidoresquetem Produtosemsualistadedesejos.Esserelaciona-
88
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 105

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
mentotemumatributoqueespecificaseo Consumidordesejarecebere-
mailacadaaltera çãofeitano Produtoqueeleobserva.
Comotemosumatributonorelacionamento, iremosmapeá-locomo
umaentidade ConsumidorProduto,eemvezdemapearmosummuitos
paramuitoscomoveremosnase ção5.17,mapearemosumparamuitosde
Consumidorpara ConsumidorProdutoeoutrarela çãoumparamuitos
de Produtopara ConsumidorProduto.Omapeamentoumparamuitos
serávistonase ção5.13.
Fig.5.4:ConsumidoreProdutocomtabeladerelacionamento
Lidandocomchavescompostastemosduasformasdefazeromapea-
mento,via @EmbeddedIdouvia @IdClass. Emambososcasosprecis-
aremosdeumaclassequeimplementeainterface Serializablepararep-
resentarachave. IssoporquenaJPAachaveprimáriaérepresentadapor
umainstânciade Serializable.Podemosverissodeformamaisclarana
declaraçãodosmétodos finde getReference,quepossuemcomoobje-
tivorecuperarumainstânciadeumaentidadenobancodedadosatravésdo
seu id:
public interface EntityManager {
...
<T> find(Class<T> clazz, Serializable id);
<T> getReference(Class<T> clazz, Serializable id);
...
}
Então,pormaisquenossachavecontenhadoisoumaisatributos,pre-
cisamosdeumaúnicaclassequeosrepresente.Veremosagoraaspequenas
89
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 106

5.4. Mapeiechavescompostas CasadoCódigo
diferençasenvolvendocadaumasdessasformasdemapearaschavescom-
postas.
Mapeamentodechavecompostacomo@EmbeddedIde@Embed-
dable
Mapeandodessaforma,emvezdetermosumachavedotipo Integer
ou Long,teremosumachavedotipodaclassequecriamos.Aoanalisaros
exemplosficasimplesdesecompreender.
@Embeddable
public class ConsumidorProdutoPK implements Serializable {
...
private Integer consumidorId;
private Integer produtoId;
// equals e hashCode
}
Note que não anotamos a chave com@Entity, afinal ela não rep-
resenta uma entidade, apenas sua chave. Para esse caso, anotamos com
@Embeddable,indicandoqueessaclassecomplementaráoutra,quenocaso,
seráaclasse ConsumidorProduto.
@Entity
public class ConsumidorProduto {
@EmbeddedId
private ConsumidorProdutoPk id;
/ /outras propriedades e métodos
}
Parabuscarusandoachaveprimária,bastapassarmosumainstânciada
chavecomonoexemploaseguir.
ConsumidorProdutoPK pk = new ConsumidorProdutoPK();
pk.setConsumidorId(consumidorId);
pk.setProdutoId(produtoId);
ConsumidorProduto cp =
entityManager.find(ConsumidorProduto.class, pk);
90
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 107

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
Agorapararealizarmosumabuscade ConsumidorProdutobaseado
nachavedealgumconsumidor,teríamosaseguinteconsulta.
String jpql = "select cp from ConsumidorProduto as cp " +
"where cp.id.consumidorId = :consumidor";
Como podemos perceber, para acessar o id do consumidor, pre-
cisamosacessarapropriedadedotipo ConsumidorProdutoPKatravésde
"cp.id". Nãoseassustecomessasintaxediferenteno wherecasoainda
nãoaconhe ça,aindavamosfalarbastantesobreela.
Mapeamentodechavecompostacomo@IdClass
A principal diferença no uso de @IdClass com relação ao
@EmbeddedIdéquenesteúltimoprecisávamosacessarumapropriedade
intermediáriaparachegaràspropriedadesquecompõemachave.
Noexemploapresentado,porsetratardeumatabeladerelacionamento,
issopodenãoparecertãomal.Masquandotemosumatabeladechavecom-
postanaqualascolunasquecompõemachavesãoatributosdaentidade,isso
passaaserumproblema.
Considereumsistemadeumaescolaquetemumatabelaquearmazenaos
dadosdecadaaluno.Noentanto,essesalunospodemsermuitojovensenão
possuirdocumentos,entãoumapossívelsolu çãoseriacriarachavebaseada
nonomedoaluno,onomedamãeeadatadenascimentodoaluno. Além
dessasinforma çõesteríamosoutrascomopodemosveraseguir.
Fig.5.5:TabelaAlunocomchavetripla
91
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 108

5.4. Mapeiechavescompostas CasadoCódigo
Agora, se usássemos a abordagem que vimos com@EmbeddedIde
quiséssemosconsultarcrian çasemumadeterminadafaixadeidade,com
rendafamiliarentreoutradeterminadafaixa,precisaríamosdeumaconsulta
parecidacomaseguinte:
String jpql = "select a from Aluno a " +
"where a.id.nascimento between :dataInicial and :dataFinal " +
"and a.rendaFamiliar between :rendaMinima and :rendaMaxima";
Vemos que o tratamento dado às propriedadesnascimento e
rendaFamiliarfoidiferentepelofatodeumafazerpartedachaveprimária.
Emcasoscomoesse,ousodaabordagemquevamosveragoraresultaem
tratamentoigualaqualquerpropriedade.Vejamoscomoficaomapeamento
dessaforma.
public class AlunoPK implements Serializable {
...
private String nome;
private String nomeMae;
private Date nascimento;
// equals e hashCode
}
@Entity
@IdClass(AlunoPK.class)
public class Aluno {
@Id
private String nome;
@Id
private String nomeMae;
@Id
private Date nascimento;
private String nomePai;
private String raca;
}
Dessaformanóscontinuamostendoumaclassequerepresentaachave
paraquepossamosutilizarosmétodosqueesperamachaveprimáriacomo
92
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 109

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
o findeo getReferencedainterface EntityManager. Mascomo
podemosobservar,osmesmosatributosqueestãonaclasse AlunoPKes-
tãotambémnaclasse Aluno,oquenospermiterefazerapesquisaanterior
daseguinteforma:
String jpql = "select a from Aluno a " +
"where a.nascimento between :dataInicial and :dataFinal " +
"and a.rendaFamiliar between :rendaMinima and :rendaMaxima";
Agorasim,podemospesquisaratributossimplesoupartedachaveda
mesmaforma.
5.5 A anotação @Basic
Utilizamosessaanota çãoparainformarqueumapropriedadedaentidadeé
umacolunanobanco.Noentanto,comoessejáéocomportamentopadrão,
ousodessaanota çãoéopcionaleacabaficandorestritoaquandodesejamos
quemesmoumapropriedadecomum,quenãoéumrelacionamento,seja
carregadasobdemanda-outambémconhecidocomo Lazy Load,quevamos
estudarmaisnase ção5.14.
@Entity
public class Automovel {
private Integer id;
private String descricao;
...
@Id @GeneratedValue
public Integer getId(){
return id;
}
@Basic(fetch=LAZY)
public String getDescricao(){
return descricao;
}
}
93
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 110

5.6. @Table,@Columne@Temporal CasadoCódigo
Comisso,adescri çãosóserábuscadanobancodedadosquandoinvocar-
mososeu getterpelaprimeiravez.Porémpercebemosumadiferen çanesse
código,queéaanota çãoestarno getterenãonapropriedade. Precisamos
dissoporqueocarregamentosobdemandadepropriedadesdaprópriaenti-
dadesófuncionaseanotarmoso getter.Anotandoapropriedade,ocarrega-
mentoseráfeitonormalmentejuntocomaentidade.
5.6 @Table,@C olumn e @Temporal
Aconven çãodaJPAindicaqueascolunasdobancoterãoomesmonome
dosatributosdasentidades,eémuitocomumencontrardesenvolvedoresque
paradeixarasclassesmaislimpas,semanota ções,adotamessecomporta-
mentopadrão.Noentanto,quandomapeamostabelasligadas,muitasvezes
opadrãodenomenclaturaédiferente.Porexemplo,podemosternossaclasse
enossatabeladaseguinteforma:
Fig.5.6:ExemplodeclasseetabeladeAutomovelladoalado
Portanto,precisamosdealgumamaneirafazercomquenossaentidade
sejapersistidanessatabela.Claroquenãovamosmudarosnomesdosatrib-
utosdaentidadeeacabarabrindomãodaclarezanocódigoJava.Asolu ção
ésimples,bastamalgunsmapeamentos.
@Entity
@Table(name="T_AUTOMOVEIS")
public class Automovel {
94
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 111

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
@Id @GeneratedValue
@Column(name="COD")
private Integer id;
@Column(name="DESC", nullable=false, length=100)
private String descricao;
@Temporal(TemporalType.TIMESTAMP)
@Column(name="DT_CADASTRO", nullable=false, updatable=false)
private Date dataCadastro;
...
}
Paramapearonomedatabela,usamosaanota ção @Table,quenosper-
mitetambéminformaro schemadobanco,casonecessário.Jáparamapear
acoluna,usamosaanota ção @Column,quenospermitecolocarváriosde-
talhesdecomoessapropriedadeJavavaivirarumacolunanobanco.
Aomapearacolunapodemosespecificar,alémdonome,seacoluna
aceita valores nulos ou não, por meio do atributonullable, e o seu
tamanho,como length. Essasalteraçõesrefletemnaestruturadatabela,
ouseja,adescri çãoemqueindicamosotamanho100equenãoéanulável
seráNOT NULL epossivelmenteum VARCHAR(255)dependendodobanco
dedadosemuso.
Outraconfigura çãointeressantequefizemoséindicarseacolunapode
terseuvaloratualizadoounão. Essaúltimaconfigura çãonãoserárefletida
nobancodedadosemsi,massimnagera çãodoscomandosde updateno
banco.Mesmoqueousuárioouaaplica çãoalteremovalordapropriedade
dataCadastro,quandoo Automovelforatualizadonobanco,ocomando
updateiráignoraressapropriedade.
ÉpossívelatéespecificarumtrechodeSQLnativodobancoparagerar
acoluna,paraissopodemosusarapropriedade columnDefinition,mas
tomecuidado,porquevocêpoderáperderaportabilidadeentreosbancosde
dados:
@Column(name="DESC", columnDefinition="CLOB NOT NULL")
private String descricao;
95
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 112

5.7. @Versionelockotimista CasadoCódigo
Eporfim,nonossomapeamentotemosaconfigura çãodaprecisãode
dataqueiremosutilizar.Fazemosissousandoaanota ção @Temporal.Esse
mapeamentopodeserusadoematributosdotipo Dateou Calendare
comelepodemosespecificarseaoconversarcomobancodedadosqueremos
considerar:
•DATE:somenteadata,seminforma çãodehora;
•TIME:somenteinforma çãodehora,semdata;
•TIMESTAMP:valorpadrão,queconsideratantodataquantohora.
O datatypeaserutilizadopodevariardeacordocomobancodedados
emuso.
5.7 @Version e lock otimista
Existemtrêsformasdetratarmosconcorrênciadealtera çãoderegistrosno
bancodedados.Aprimeira,emaisusada,énãofazernada.Nessecaso,se
doisusuáriosleemamesmaversãodeumregistro,fazemalgumaaltera çãoe
depoissalvam,aaltera çãofeitaprimeiroiráseperder,jáqueserásobrescrita
peloquesalvarporúltimo.
Aoutraop çãoéoquechamamosde lockpessimista.Eletemessenome
porquepartedoprincípioqueprovavelmenteiráocorrerumaconcorrência
naedi çãodoregistro. Quandoalguémolê,elejáficabloqueadosomente
paraessapessoa.Dessaforma,evita-sequeoutrosusuáriostambémeditem
omesmoregistro.
Muitas vezes quando carregamos as informações para o usuário, ele
temnamesmatelaaop çãodevisualizaroueditar. Asimplesvisualiza ção
nãocausaproblemadeconcorrência,mascomoestamossendopessimistas,
acabamosconsiderandoquequandoesseregistroforlidoprovavelmenteele
seráalterado,entãoessebloqueioéfeitoparaescrita. Oproblemaéque
quandooutrousuárioforvisualizaromesmoregistro,porestarusandoa
mesmatelaqueoprimeiro,vamosquererumbloqueiodeescritaparaele
também.Mascomooregistrojáestábloqueado,osegundousuárionãocon-
seguenemler.
96
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 113

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
Issoficapioraindaseobancodedadosutilizadonãosuportarbloqueio
delinha.Nessecaso,pormaisquesolicitemosobloqueiodeumaúnicalinha,
atabelainteiraficabloqueada,causandoumproblemaenormenaaplica ção.
Emumsistemarazoavelmenteutilizado,empoucosminutosteríamos“en-
garrafamentosquilométricos”nonossobancodedados.
Aterceiraop çãoéusarmoso lockotimista.Apesardonome,nãoexiste
umbloqueioderegistronessaabordagem: emvezdissocriamosumapro-
priedade,dotiponuméricooudata,eanotamoscom @Version.Assim,a
cadaaltera çãodoregistroessapropriedadeseráatualizada,edessaforma,o
bancoficaparecidocomumsistemadecontroledeversão.
Casodoisusuáriosleiamomesmoobjetonaversão1,quandooprimeiro
salvaraaltera çãoesseobjetopassaparaaversão2nobanco.Então,quandoo
segundousuárioforpersistirsuasaltera ções,aJPAvaiperceberqueeleestá
tentandosalvarumaaltera çãobaseadanaversão1,masquejáexisteuma
versãomaisnovanobanco.Elalan çaráuma OptimisticLockException
eatransa çãoserámarcadapara rollback.Apesardetodooconceitoenvolvido,
omapeamentoébemsimples.
@Entity
public class Automovel {
@Id @GeneratedValue
private Integer id;
private String descricao;
@Column(nullable=false, updatable=false)
private Date dataCadastro;
@Version
private Date ultimaAlteracao;
...
}
Comaconfigura çãorealizada,éresponsabilidadedaaplica çãofazero
tratamentodospossíveisconflitos.Umaboaop çãoéapresentaraousuário,
97
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 114

5.8. Relacionamentosmuitosparaumcom@ManyToOne CasadoCódigo
emumatelacomparativa,asuaversãoeaversãomaisnovaparaqueelees-
colhacomoquerdeixarasinforma ções.
5.8 Relacionamentos muitos para um com
@ManyToOne
Utilizamosaanota ção @ManyToOnesemprequequisermosrelacionarenti-
dades.Paraanalisarmoscomousamosessetipoderelacionamento,considere
aclasse Modelodeautomóvel,queporsuaveztemumarela çãocom Marca.
Assimpodemosdizerqueo Modelo458Spideréda MarcaFerrari.
@Entity
public class Modelo {
@Id @GeneratedValue
private Long id;
@ManyToOne
private Marca marca;
}
@Entity
public class Marca {
@Id @GeneratedValue
private Long id;
}
Oresultadodessemapeamentonobancodedadoséoseguinte:
Fig.5.7:TabelaModelocomchaveestrangeiradeMarca
98
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 115

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
Natabela Modelotemosumachaveestrangeirachamada marca_idque
fazreferênciaparaatabela Marca. Essesnomesestãoseguindoanomen-
clatura defaultdefinidapelaJPA.
Comojávimos,atabelacriadasegueomesmonomedaentidadeeo
mesmovaleparaascolunassimples,quetêmomesmonomedosatributos.
Anovidadeaquiéachaveestrangeira,masseunomepadrãotambémébem
simples.Onome marca_idéformadoapartirdaconcatena çãodonomeda
propriedadequeestamosmapeando,quenocasoé marca,seguidode“_”,
eemseguidaonomedacolunaquerepresentaachaveprimáriadaentidade
Marca,quenocasoé id.
Noexemplo,apropriedade marcatemomesmonomedasuaclasse:
Marca,excetoporiniciaremminúsculo.
Outropontoimportanteaseobservaréqueéonomedapropriedadeque
éconsideradoparaaespecifica çãodonomedacolunadachaveestrangeira
nobanco,enãodaclasse. Assimcomoaoutrapartedonomedachavees-
trangeiraéformadapelonomedacolunadachaveprimárianatabela Marca,
enãoonomedapropriedadenaclasse Marca.
Vejamosoexemplo:
@Entity
@Table(name="T_MODELO")
public class Modelo {
@Id @GeneratedValue
private Integer id;
@ManyToOne
private Marca montadora;
}
@Entity
@Table(name="T_MARCA")
public class Marca {
@Id @GeneratedValue @Column(name="pk")
private Integer id;
}
99
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 116

5.9. @OneToOne CasadoCódigo
Comessenovoexemplo,onovonomedacolunaqueéchaveestrangeira
de T_MARCAé“montadora_pk”. Devemosobservarqueessamesmaregra
paracria çãodechaveestrangeiracomnome defaultseaplicaatodososoutros
tiposdemapeamento.
Oexemplodaclasse Marcaapresentadoaquiéapenasparavermosum
nomediferentedecolunadechaveprimária. Nase ção5.13veremoscomo
mapeá-la.
5.9 @OneToOne
Omapeamento @OneToOneébemparecidocomo @ManyToOnequevimos
anteriormente.Aprincipaldiferen çaéquenachaveestrangeirateremosare-
strição unique.Aindaconsiderandoa Marcadoautomóvel,podemosdizer
queelateráseusdetalhesecriaremosumanovaentidadeparaisso,chamada
DetalheMarca,queguardaráasinforma çõesextrassobreela.Comoquere-
mosquea Marcasóestejarelacionadaaum DetalheMarca,vamosindicar
queessarela çãoé @OneToOne:
@Entity
public class DetalheMarca {
@Id @GeneratedValue
private Integer id;
private Integer anoFundacao;
private String paisOrigem;
private String fundador;
@OneToOne
private Marca marca;
}
ElogoapósoDERquerepresentaessarela ção.
100
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 117

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
Fig.5.8:TabelaDetalheMarcacomachaveestrangeiradaMarca
Nesse mapeamento temos uma classeDetalheMarca cujas pro-
priedadespoderiamestardentrodaprópriaclasse Marca,masoptamospor
separaremtabelaseclassesdiferentesparaumamelhororganiza ção.
Avantagemdessetipodeabordageméqueevitamosclassesetabelascom
muitosatributosecolunas. Noentanto,podemosacabargerando joins
demaisquandonossasconsultasenvolveremasduasentidades.
Indoalémnesseexemplo,oqueacontecesetivermosumobjeto Marca
equisermosacessarseufundador?
Nasitua çãoapresentada,temoso DetalheMarcamapeandoa Marca,
masnãoocontrário.Temosummapeamentounidirecionalegostaríamosde
terumrelacionamentobidirecional.
@OneToOneunidirecional
Comoacabamosdever,ummapeamentounidirecionalconsisteemma-
pearmosapenasumdosladosdorelacionamento.Esseladoteráemsuatabela
umchaveestrangeirareferenciandoatabeladooutroladodorelacionamento.
Anteriormente,aclasse DetalheMarcamapeavaa Marcaeporissoa
tabela DetalheMarcatinhaumachaveestrangeiraparaatabela Marca.
5.10 Relacionamentos bidirecionais
Jásabemosqueapenas DetalheMarcatemumacessodiretoà Marca,mas
gostaríamosqueambososladosseenxergassem.
101
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 118

5.10. Relacionamentosbidirecionais CasadoCódigo
@Entity
public class DetalheMarca {
@Id @GeneratedValue
private Integer id;
private Integer anoFundacao;
private String paisOrigem;
private String fundador;
@OneToOne
private Marca marca;
}
@Entity
public class Marca {
@Id @GeneratedValue
private Integer id;
@OneToOne
private DetalheMarca detalhe;
}
Aseguirpodemosverqueesseóbviomapeamentoresultaemalgoines-
perado.
Fig.5.9:Mapeamentoerradocriachaveestrangeiranasduastabelas
Oqueaconteceuaquiéquecadatabelapossuisuaprópriachavees-
trangeiraapontandoparaaoutra,emvezdeumaúnicaemumdoslados.
Quandoháumrelacionamentobidirecional,devemosescolherumdoslados
102
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 119

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
paraserodonoenessecasosomenteatabeladodonoéqueteráachave
estrangeira.
Pormaisqueambososladostenhamumainstânciadooutrolado,odese-
jáveléquenobancodedadostenhamosapenasumachaveestrangeira.Como
éummapeamento @OneToOne,podemosescolherqualquerumdoslados.
Paranossomodelo,vamosdeixara Marcacomoadona.Comesseajuste,o
mapeamentoeastabelasficamdaseguinteforma.
@Entity
public class DetalheMarca {
@Id @GeneratedValue
private Integer id;
...
@OneToOne(mappedBy="detalhe")
private Marca marca;
...
}
@Entity
public class Marca {
@Id @GeneratedValue
...
@OneToOne
private DetalheMarca detalhe;
...
}
Analisandoocódigo,oladoquenãoéodonoindicaquemtemessepapel
atravésdoatributo mappedBy. Vemosquenaclasse DetalheMarcanós
dizemosqueodonodorelacionamentoéooutrolado,equeainforma ção
queseriapersistidaemumachaveestrangeira“própria”agoravaisermapeada
pelachaveestrangeiracriadapelapropriedade detalhedaclasse Marca.
103
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 120

5.11. Oquetemaverodonodorelacionamentocomaopera çãoemcascata? CasadoCódigo
Fig.5.10:AgoraquemtemachaveestrangeiraésóatabelaMarca
5.11 Oque tem a ver o dono do relacionamento
com a operação em cascata?
Vimosqueéimportantetermosumdonoparaorelacionamentobidirecional
paraquenãotenhamosduaschavesestrangeirasnobancodedados,oque
causariaproblemagravesnaaplica ção.Agoraveremosque,apesardetermos
apossibilidadedeusaropera çõesemcascata,issodeformaalgumadiminui
aimportânciadopapeldodonodorelacionamento.
Podemosconfiguraromapeamentoderelacionamentocomaop çãode
cascatacomopodemosveraseguir.
@Entity
public class DetalheMarca {
@Id @GeneratedValue
private Integer id;
@OneToOne(mappedBy="detalhe", cascade=CascadeType.ALL)
private Marca marca;
}
@Entity
public class Marca {
@Id @GeneratedValue
private Integer id;
@OneToOne(cascade=CascadeType.ALL)
104
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 121

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
private DetalheMarca detalhe;
}
Repare no atributo cascade com o valor CascadeType.ALL
nos relacionamentos. Com isso, qualquer operação, como por exemplo
persist, remove, mergequefizermosna Marcaseráfeitotambémno
DetalheMarca;porissonãoprecisamoschamaro persistnosdoislados.
Podemosespecificarsomentealgumasopera ções,possibilitandopropa-
garaopera çãodesalvarmasnãoadeexcluir.Mascomoestamostrabalhando
com @OneToOne,omaiscomumseráaop ção ALL,jáqueambososlados
representamumamesmainforma ção,quesófoidivididaparamelhorara
manutenibilidadedosistema.
Apesardafacilidadequeessafuncionalidadenosoferece,éimportante
lembrarmosquecontinuaexistindoumcomportamentodiferenteemcada
umdosladosdarela ção.Comotemosa Marcacomoadonadorelaciona-
mento, precisamosobrigatoriamentealimentá-lacomo DetalheMarca.
Semisso,ainforma çãodachaveestrangeiranãoserápersistida.
Aseguirveremosmaisalgunscenáriosparanãorestardúvidassobreesse
assuntotãoimportante.
Primeirocenário:Fechandoosdoisrelacionamentosepersistindo
oladofraco
Marca marca = new Marca("Ferrari");
DetalheMarca detalhe = new DetalheMarca("Enzo Ferrari");
marca.setDetalhe(detalhe);
detalhe.setMarca(marca);
entityManager.persist(detalhe);
Nesse código, nós relacionamos ambos os lados: Marca e
DetalheMarca, mas acabamos salvando o lado que não é o dono do
relacionamento. Énecessárioentendermosqueoimportantenãoéolado
queépassadoparaométodo persistesimqueodonoconhe çaooutro
lado.
Aquimandamossalvaro detalhe,mascomoconfiguramosocom-
portamentoemcascataparaasuapropriedade marca,écomosetambém
105
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 122

5.11. Oquetemaverodonodorelacionamentocomaopera çãoemcascata? CasadoCódigo
tivéssemosmandadopersistirdooutrolado. EomelhoréqueaJPAinfere
aordemcorretaemqueessasopera çõesprecisamserexecutadasnobanco.
Então,pormaisquetenhamoschamadoométodo persistdolado“fraco”
ooutroladotemainforma çãonecessáriaparapersistirachaveestrangeira.
Segundocenário:Persistindoladoforte
Marca marca = new Marca("Ferrari");
DetalheMarca detalhe = new DetalheMarca("Enzo Ferrari");
marca.setDetalhe(detalhe);
entityManager.persist(marca);
Nessecenáriosalvamosa marca,ecomoindicamosquegostaríamosdas
operaçõesemcascata,quandolermoso DetalheMarcadobancodedados,
veremosqueainforma çãodamarcaestarálá,jáqueachaveestrangeiraserá
alimentadacorretamente.
Terceirocenário:Nãofechandoorelacionamentoepersistindoo
ladofraco
Marca marca = new Marca("Ferrari");
DetalheMarca detalhe = new DetalheMarca("Enzo Ferrari");
marca.setDetalhe(detalhe);
entityManager.persist(detalhe);
Agoratemosumcódigomuitoparecidocomoquevimosnoprimeiro
cenário,sendoqueadiferen çaéqueagoraassociamosapenasoladoforteda
relação.
Comoo detalhenesseexemplonãoserelacionacoma marca,esta
nãoserápersistida,econsequentementearela çãoentremarcaedetalhenão
existirá.Asoluçãopoderiaserexigirmosapresen çadeuma Marcaparatodo
DetalheMarca;edefatoéomaiscorretoasefazernessecaso.
106
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 123

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
Quartocenário:Novamentenãofechandoorelacionamentoeper-
sistindooladofraco
Marca marca = new Marca("Ferrari");
DetalheMarca detalhe = new DetalheMarca("Enzo Ferrari");
detalhe.setMarca(marca);
entityManager.persist(detalhe);
Nesseexemplo,ambososladosserãopersistidosmasainforma çãoda
chaveestrangeiranãoseráalimentada. Comisso,quandolermostantoa
Marcaquantoo DetalheMarcadobancodedados,ambosvirãocomo
outroladonulo. Alimentaro detalhecomsua marcanessecasoserve
apenasparaaopera çãoemcascataserdisparada,masquandoa marcafor
persistida,comoelanãocontémainforma çãodoseu detalhe,achavees-
trangeiranãoseráalimentada.
Resumindoasopera çõesemcascata
Umapráticamuitocomumparaevitaressesproblemaséfazercomqueos
settersdosrelacionamentosdefinamosdoisladosdorelacionamento,assim
nãocorreríamosriscosdeesquecerdepreencheralgumlado.Essamudan ça
éextremamentesimples.
@Entity
public class DetalheMarca {
@Id @GeneratedValue
private Integer id;
@OneToOne(mappedBy="detalhe", cascade=CascadeType.ALL)
private Marca marca;
public void setMarca(Marca marca) {
this.marca = marca;
marca.recebeDetalhe(this);
}
public void recebeMarca(Marca marca) {
this.marca = marca;
107
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 124

5.12. Organizemelhorsuasentidadesepromovareaproveitamentocom@Embeddablee@EmbeddedCasadoCódigo
}
}
@Entity
public class Marca {
@Id @GeneratedValue
private Integer id;
@OneToOne(cascade=CascadeType.ALL)
private DetalheMarca detalhe;
public void setDetalhe(DetalheMarca detalhe) {
this.detalhe = detalhe;
detalhe.recebeMarca(this);
}
public void recebeDetalhe(DetalheMarca detalhe) {
this.detalhe = detalhe;
}
}
Pronto,agoratodavezquealguéminvocaralgumdos setters,automati-
camenteosdoisladosdosrelacionamentoestarãodefinidos.
5.12 Organize melhor suas entidades e pro -
mov a reaproveitamento com @Embeddable
e@Embedded
Jávimosqueaassocia ção @OneToOnegeralmenteéusadaparaorganizarmos
melhornossasclassesenormalizaraindamaisastabelas.Assim,emvezde
termosumatabelaenorme,dividimosasinforma çõescombaseemalgum
critérioeasrelacionamoscomainforma çãoprincipalatravésdachavees-
trangeira.Porémmuitasvezestemosumatabelajáexistentequecontémto-
dasasinforma ções.
PodemosquerersepararissoemobjetosdiferentesnonossomodeloOO,
oquenãoéraro.Assim,mantemosnossasclassesorganizadase,dependendo,
108
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 125

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
atémesmoreaproveitamososdados.
Outrosexemplosemquecostumamosencontrartabelasgrandesqueque-
bramosemobjetosmenoressãoquandomapeamosumapessoaoufun-
cionárioquepodepossuirendere ço,documentos,filia ção,emuitosoutros
detalhesquepoderíamosquerersepararemobjetosespecíficos.
Fig.5.11:Tabelagrandecomcamposdeassuntosdiversos
Agoraimaginequepoderíamosteraindacolunasreferentesàdatadead-
missãoedemissão,eváriasinforma çõesadicionaisemumaúnicatabela.Ela
poderiaserrepresentadaemumaentidadecomoseguintecódigo:
@Entity
public class Funcionario {
@Id @GeneratedValue
109
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 126

5.12. Organizemelhorsuasentidadesepromovareaproveitamentocom@Embeddablee@EmbeddedCasadoCódigo
private Integer id;
private String nome;
private Date nascimento;
private String rg;
private String orgaoExpedidor;
private String cpf;
private String tituloEleitor;
private Integer secao;
private Integer zona;
private String naturalidade;
private String nacionalidade;
private String nomeMae;
private String nomePai;
private String logradouro;
private String cep;
private String cidade;
private String uf;
@ManyToOne
private Cargo cargo;
}
@Entity
public class Cargo {
@Id @GeneratedValue
private Integer id;
private String descricao;
}
Aclasse Funcionariojáestágrande, masdependendodosistema,
poderiaseraindamaior. Umaformaderesolveresseproblemasemalterar
astabelasnobancoéusando @Embeddeddaseguintemaneira:
public class Funcionario {
@Id @GeneratedValue
private Integer id;
private String nome;
110
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 127

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
private Date nascimento;
@Embedded
private Documentacao documentacao;
@Embedded
private Endereco endereco;
@ManyToOne
private Cargo cargo;
}
@Entity
public class Cargo {
@Id @GeneratedValue
private Integer id;
private String descricao;
}
Comisso,precisaríamosterasclasses Documentacaoe Endereco,
comseusrespectivosatributoseindicarmosqueelasnãosãoentidades,mas
sim,classesqueprecisamterseusdadosreaproveitadosemoutrosentidades.
Fazemosissopormeiodaanota ção @Embeddable.
@Embeddable
public class Documentacao {
private String rg;
private String orgaoExpedidor;
private String cpf;
private String tituloEleitor;
private Integer secao;
private Integer zona;
private String naturalidade;
private String nacionalidade;
private String nomeMae;
private String nomePai;
111
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 128

5.12. Organizemelhorsuasentidadesepromovareaproveitamentocom@Embeddablee@EmbeddedCasadoCódigo
// getters e setters se necessário
}
@Embeddable
public class Endereco {
private String logradouro;
private String cep;
private String cidade;
private String uf;
// getters e setters se necessário
}
Comopudemosver,bastaanotaraclassecom @Embeddableparain-
dicarqueelanãoénaverdadeumaentidade,ouseja,queelanãorepresenta
umatabelanobanco,esimqueelaestarádentrodeumaentidade,represen-
tandoapenasumapartedeumatabela.
Comisso,aclasse Funcionarioficoumuitomaislimpa,ecadavez
queseadicionarumatributodeumtipoqueé @Embeddable, comoa
Documentacaoeo Endereco,bastaanotá-locom @Embedded.
Agoratemosquenosatentarparaumdetalhe:pormaisquesaibamosque
natabelaestátudojunto,quandovamosconsultarusandoJPQLtemosque
respeitaraestruturadasnossasclasses.Ésórecordarmosque,umavezfeito
omapeamento,esquecemosdobancoepensamosapenascomorienta çãoa
objetos.ParaconsultartodososfuncionáriosdeMatoGrossodoSul,fazemos
aseguinteconsulta:
select f from Funcionario as f where f.endereco.uf = 'MS'
Setentarmosconsultarpensandonatabela,teremosumexce çãodizendo
quenãoexisteapropriedade ufnaclasse Funcionario.
select f from Funcionario as f where f.uf = 'MS'
Ouseja, nãoestamosfalandodatabela Funcionario,esimdaenti-
dade Funcionario.
112
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 129

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
5.13 Relacionamentos um para muitos com o
@OneToMany e@ManyToOne
Nomodelodaaplica çãoqueestamosdesenvolvendo,a Marcapodeterdi-
versos Modelosassociadosaela. Dessaforma,temosumrelacionamento
umparamuitosentreambasasentidades.
public class Marca {
@Id @GeneratedValue
private Integer id;
@OneToMany
private List<Modelo> modelos;
}
Pararepresentarmosumrelacionamento OneToMany,utilizamosain-
terface java.util.List, porém, seria possível utilizar qualquer outra
Collection.
Jávimosoquantoéimportantedefinirmosseummapeamentoéunidi-
recionaloubidirecional.Veremosagoracomoissoéespecificadonarela ção
@OneToMany.
@OneToManyunidirecional
Pensandonamodelagemrelacional,obviamentearela çãoembanconão
podeficarnatabela Marca,umavezquenãotemoslistasembancosrela-
cionais. Asolu ção,nessecaso,éumatabeladerelacionamentochamada
Modelo_Marca,quetemaschavesestrangeirasdasduastabelasemquestão.
Noentanto,talvezfossemaisnaturaltermosnatabela Modeloumachave
estrangeiraqueapontasseparaatabela Marca,indicandoquemestáassoci-
adoaela.
@ManyToOneunidirecional
Vamospensarnesserelacionamentodeumaoutramaneira. Queremos
dizerquetodo Modeloestádealgumamaneiraassociadoauma Marca.No
113
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 130

5.13. Relacionamentosumparamuitoscomo@OneToManye@ManyToOne CasadoCódigo
entanto,umamesmamarcapodepossuirváriosoutrosmodelos,comovimos.
Podemosdizerqueo Modelopossuiuma Marcadaseguintemaneira:
public class Modelo {
@Id @GeneratedValue
private Integer id;
@ManyToOne
private Marca montadora;
}
Reparequeagoraaassocia çãoseinverteu,secomparamoscomoexem-
ploquevimoshápouco,emqueorelacionamentoeracomumalista.Agora
temosorelacionamentoparaumsóobjeto,a marca,porissousamoso
@ManyToOne.
Levandoessamaneiradepensarparaoladorelacional,seriaequivalentea
dizermosquenatabela Modelotemosalgoqueindiquequemésua Marca,o
queseriaachaveestrangeira.Dessaforma,teríamosnatabela Modelouma
coluna marca_id,queseriaumachaveestrangeirareferenciandoatabela
Marca.
@OneToManye@ManyToOnebidirecionais
Muitasdasvezes,precisamosacessarpelosobjetososdadosatravésdas
duaspontasdorelacionamento. Ouseja,podemosterumobjetodotipo
Marcaequerermosrecuperarosmodelosassociadosaeles;etambémpode-
mosterumobjetodotipo Modeloequerermosrecuperara Marcaassoci-
adaaela.Novamente,temosumcenárioondeorelacionamentobidirecional
poderianosajudar.
public class Marca {
@Id @GeneratedValue
private Integer id;
...
@OneToMany(mappedBy="montadora")
114
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 131

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
private List<Modelo> modelos;
...
}
public class Modelo {
@Id @GeneratedValue
private Integer id;
...
@ManyToOne
private Marca montadora;
...
}
Comojásabemos,oladoquenãotemo mappedByéodonodarela ção,e
portantoelegeralmentetemachaveestrangeiraemsuatabela.Pronto,agora
temosastabelasestruturadasdeumamaneirainteressanteetambémcon-
seguimosacessarasinforma çõesatravésdasduaspontasdorelacionamento.
Fig.5.12:Modelotemchaveestrangeiraparamontadora,dotipoMarca
5.14 Aimportância do LazyLoading, o carrega-
mento preguiçoso
Assimquetemosobjetosrelacionados,énecessárioteraten çãoredobradaem
comousá-los.Agoraqueindicamosquea Marcatemumalistacontendoos
modelos,podemos,apartirdequalquerobjeto Marca,descobrirquemeles
são.
Oprimeiropassoparaissoéconseguirumainstânciada Marca,que
podeserconseguidaatravésdométodo findda EntityManager:
115
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 132

5.14. AimportânciadoLazyLoading,ocarregamentopregui çoso CasadoCódigo
EntityManager em = JPAUtil.getEntityManager();
Marca m = em.find(Marca.class, 1);
Nesseinstante,umSQLéexecutadoparabuscaramarcapormeiodeseu
id.Reparequeorelacionamentocomos modelosfoiignorado.
Algumas pessoas podem achar estranho, porque como buscamos a
Marca,elajádeveriaestarcomos modeloscarregados.Maseseessa Marca
tivesseummilhãode modelos?Carregaríamostodoselesnamemória?E
maisimportanteainda,atéomomentonãoprecisamosdeles.Justamentepor
essemotivo,aJPAnãobuscaalistarelacionadaenquantonãoapedirmos.
Esse comportamento é conhecido comoLazy Loading, ou carregamento
preguiçoso.
Agoravamosinvocarométodo getModelosna Marca:
EntityManager em = JPAUtil.getEntityManager();
Marca m = em.find(Marca.class, 1);
List<Modelo> modelos = m.getModelos();
//só busca a lista quando ela é usada
Modelo modelo = modelos.get(0);
Apartirdomomentoemqueusamosos modelosretornadospelo
método getModelos(),elessãobuscadosnobancodedadosatravésde
umnovo select. Nesseexemplo,usamosalistaacessandoseuprimeiro
elemento.Apenasrecuperaralistasemutilizá-lanãofazbuscarnobanco.
NaJPA,todososrelacionamentosparauma Collection,ouseja,os
relacionamentos ToManysão lazyporpadrão. Noentanto,essacaracterís-
ticapodesermodificadaporumatributo fetchdaanota ção @OneToMany,
trocandoocomportamentode lazyparaseuinverso, eager:
@Entity
public class Marca {
@Id @GeneratedValue
private Integer id;
116
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 133

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
@OneToMany(fetch=FetchType.EAGER)
private List<Modelo> modelos;
}
Apartirdomomentoemquedizemosqueorelacionamentoé EAGER,
quandobuscarmosumamarca,elajávirácomtodosos modeloscarregados,
atravésdeum selectquepossuium joinparatrazertodasasinforma ções
deumasóvez.
O EAGERdeveserusadocommuitocuidado,porqueelepodefazercom
quemuitosobjetossejamcarregadosindevidamente,ecomquesuaaplica ção
tenhamenorperformanceeescalabilidade.
5.15 @Lob
Usamos @Lobparaindicarqueumapropriedadeéum large object,geral-
menteusadopara Stringmuitograndesouentãoparaguardarmostipos
binários,comoumarquivoanexodentrodonossoobjeto.
Comoosdadosqueserãoguardadosnesseatributopodemsermuito
grandes,comoporexemploumaimagememaltadefini çãoouumvídeo,é
muitocomumdefiniresseatributocomo lazy,assimelesóserácarregado
quandoefetivamenteserutilizado.Porém,comovimosnase ção5.5,sócon-
seguimosespecificarocarregamentosobdemandacomaanota ção @Basic
seasanota çõesestiveremnos getters,enãonapropriedade.
public class Automovel {
private Long id;
private byte[] fotografia;
...
@Id @GeneratedValue
public Long getId(){
return id;
}
@Lob @Basic(fetch=FetchType.LAZY)
117
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 134

5.16. @ElementCollection CasadoCódigo
public byte[] getFotografia(){
return fotografia;
}
...
}
5.16 @Element Collection
Osautomóveispodempossuir tagsquefacilitemapesquisaporeles.Assim,
poderíamosmarcá-loscomcaracterísticasespeciaisdeles.Comoas tagssão
simplestextos,como“automático”,“4portas”eassimpordiante,poderíamos
mapeá-lascomouma String,e,jáquepodemostervárias tags,umalista
de String.
@Entity
public class Automovel {
@Id @GeneratedValue
private Integer id;
private List<String> tags;
}
Nessecaso,teríamosumerro,poisaJPAnãosabecomotrataressalista
de String.Semprequetínhamosumalista,precisávamosindicarqueera
umrelacionamento. Porém,aquinãopodemossimplesmentedizerqueera
ummapeamento @OneToManyunidirecional-umavezque Stringnãoé
uma @Entity.
A partir da versão 2 da JPA, entrou o mapeamento
@ElementCollection, que permite associar uma entidade com uma
listadealgumtipobásico,comoa String.
@Entity
public class Automovel {
@Id @GeneratedValue
118
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 135

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
private Integer id;
private Integer anoFabricacao;
private Integer anoModelo;
@ElementCollection @Column(length=20)
private List<String> tags;
}
Dessa forma, o mapeamento gerará uma tabela de relacionamento
chamada Automovel_Tagscomaseguinteestrutura:
Fig.5.13:Tabeladerivadado‘relacionamento’deAutomovelcomString
5.17 Relacionamentos muitos para muitos com o
@ManyToMany
Osautomóveisvendidosnalojapodemteritensopcionais,comoarcondi-
cionado,limpadortraseiroeassimpordiante.Muitosdessesopcionaisestão
presentesemdiferentescarros,demodoqueprecisamosrelacionaressasin-
formações,oquecaracterizaumrelacionamentomuitosparamuitos.
Justamente para esse tipo de situação, a JPA possui a anotação
@ManyToMany,quevamosusarpararelacionar Automovele Opcional:
@Entity
public class Automovel {
@Id @GeneratedValue
private Integer id;
119
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 136

5.17. Relacionamentosmuitosparamuitoscomo@ManyToMany CasadoCódigo
@ManyToMany
private List<Opcional> opcionais;
}
@Entity
public class Opcional {
@Id @GeneratedValue
private Integer id;
private String descricao;
@ManyToMany(mappedBy="opcionais")
private List<Automovel> automoveis;
}
Fig.5.14:Relacionamentomuitosparamuitos
Comoesseéummapeamentobidirecional,temosquedefiniroladoque
éodonodorelacionamento.Nessecaso,fizemosodonosero Automovel,
dessaforma,elenãotemo mappedBy.
Vimosoqueocorrequandotemosumarela çãobidirecionalenãoespeci-
ficamoso mappedBy:aJPAentendequesãodoisrelacionamentosindepen-
dentes. Nocasodo @OneToOneissopodiaserobservado,jáqueeramcri-
adasduaschavesestrangeiras,umaemcadatabela.Aquino @ManyToMany,
oresultadocasoomitíssemoso mappedByseriaparecido,masemvezde
120
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 137

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
duaschavesestrangeiras-oquenãoépossívelporseremlistas-teríamos
duastabelasderelacionamento,umachamada Automovel_Opcionale
outrachamada Opcional_Automovel. PelopadrãodenomesdaJPA,
nonomedatabeladerelacionamentoapareceprimeiroonomedodono
darela ção. Porisso, nafigura5.14, atabeladerelacionamentosechama
Automovel_Opcional.
Omesmovaleparao @ManyToManyemrela çãoàatualiza çãodorela-
cionamentoviaseudono. Comojávimosemoutrosmapeamentos, so-
menteodonodorelacionamentoatualizaachaveestrangeira,enessecaso,
atabeladerelacionamento.Sendoassim,denadaadiantaadicionarumnovo
Automovelnalistade automoveisdoobjetodotipo Opcionalesal-
varesseobjeto. Precisamos, naverdade, adicionaro Opcionalnalista
opcionaisdo Automoveleentãosalvá-lo.Aísimteremosarela çãoper-
sistidanobanco.
5.18 Customize as colunas de relacionamentos
com @JoinColumn e @JoinColumns
Vimosdiversasformasderelacionamentoentreasentidades,esempreque
falamosnissonomundorelacional,falamosdechavesestrangeiras.Atéagora
nospreocupamosapenascomofuncionamentodosrelacionamentos,usando
osnomespadrõesqueaJPAdáessaschaves.
Vimosquepodesernecessárioousodaanota ção @Columnparaes-
pecificarumnomedecolunadiferentequandoqueremosfugirdopadrão
de nomenclatura. No entanto, não conseguimos usá-la para mudar o
nomedascolunasdaschavesestrangeiras. Paraissousamosasanota ções
@JoinColumne @JoinColumns.
@JoinColumnnomapeamentoderelacionamentos
Precisamosfazercomqueachaveestrangeirada Marcaassociadaao
Modelotenhaumnomediferentedopadrão. Queremosqueacolunase
chame montadora_fk.
@Entity
public class Modelo {
121
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 138

5.18. Customizeascolunasderelacionamentoscom@JoinColumne@JoinColumns CasadoCódigo
@Id @GeneratedValue
private Integer id;
@ManyToOne
@JoinColum(name="montadora_fk")
private Marca montadora;
}
No@JoinColumn,apropriedade nameserefereàcolunadatabelada
entidadequecontémaanota ção.Ouseja,comoaanota çãoestánaentidade
Modelo,acoluna montadora_fkestádentrodatabela Modeloeéchave
estrangeiradacoluna iddentrodatabeladaentidade Marca.
Use@JoinColumnsquandotiverchaveestrangeiracomposta
Usamosaanota ção @JoinColumnsapenasparaagruparmaisdeuma
@JoinColumn.Issoénecessárioquandotemosumachaveestrangeiracom-
posta.
Porexemplo,vamosconsiderarque Alunotemcomochaveseunomeeo
nomedesuamãe,equecada Provapertenceaum Aluno.Omapeamento
dessemodeloficariadaseguinteforma:
@Entity
public class Prova {
@Id @GeneratedValue
private Integer id;
@ManyToOne
@JoinColumns({
@JoinColumn(name="aluno_nome",
referencedColumnName="nome"),
@JoinColumn(name="aluno_nome_mae",
referencedColumnName="nomeMae")
})
private Aluno aluno;
}
122
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 139

CasadoCódigo Capítulo5. Comomapeartudo...ounada!
Nessecaso,comoachaveécomposta,precisamosindicar,pormeiodo
atributo referencedColumnName,qualéachavequeestamosrenomeando
eaqualcolunadaoutratabelaelaserefere.
5.19 Configure as tabelas auxiliares com
@JoinTable
Como vimos quando falamos sobre os vários tipos de relacionamentos,
alguns deles podem requerer uma tabela auxiliar, como foi o caso do
@ManyToMany entre os automóveis que continham os itens opcionais.
Naquelecaso,atabelaauxiliarsechamava Automovel_Opcional.
Semprequequisermosmudarascaracterísticasdeumatabelaauxiliar,
podemosusaraanota ção @JoinTable.
@Entity
public class Automovel {
@Id @GeneratedValue
private Integer id;
@ManyToMany(
@JoinTable(
name="T_AUTOMOVEIS_OPCIONAIS",
joinColumns=
@JoinColumn(name="AUTO_ID"),
inverseJoinColumns=
@JoinColumn(name="OPCIONAL_ID")
)
private List<Opcional> opcionais;
}
@Entity
public class Opcional {
@Id @GeneratedValue
private Integer id;
123
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 140

5.20. Conclusão CasadoCódigo
private String descricao;
@ManyToMany(mappedBy="opcionais")
private List<Automovel> automoveis;
}
Aanota ção @JoinTableécolocadanaentidadedonadorelaciona-
mentoenospermiteespecificaronomedatabeladerelacionamentoeascol-
unasqueaformam.Atravésdapropriedade joinColumnsinformamosas
colunasquesãochavedatabeladonadorelacionamento.Jánapropriedade
inverseJoinColumnsespecificamosascolunasquesãochavedaoutra
tabela,quenãoéadonadorelacionamento.
5.20 Conclusão
Vimos várias maneiras de customizar os mapeamentos do Hibernate, de
modoquejáépossívelterumaflexibilidademaioreseadequaradiferentes
modelosdedados.
124
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 141

Capítulo6
ConsultascomaJPQLeos
problemascomunsnaintegra ção
comoJSF
Nocapítulo3fizemosocadastro,exclusãoelistagemdosautomóveis,mas
aindanãosabemoscomorecuperardadosdeumamaneiramaiscomplexa
queum "select a from Automovel a" .
Nestecapítulo,vocêvaiaprendercomofuncionaabuscadedadosatravés
daJPAsemabandonaromodeloorientadoaobjetos.Veremostambémcomo
lidarcomafamosaetãotemida LazyInitializationException,além
dequestõesfundamentaisdeinfraestruturaparaevitá-la.
Analisaremos como um tratamento inadequado da
LazyInitializationException pode afetar nossos mapeamentos
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 142

6.1. FiltredadoscomaJavaPersistenceQueryLanguage-JPQL CasadoCódigo
econsequentementetodaaperformancedaaplica ção. Porfim,vamosver
casosemquenossomodelopodenãoseromaisadequadoparaacria çãode
umrelatórioemostrarcomopodemosfazê-losemmaioresdificuldades.
6.1 Filtre dados com a Jav aPersistenceQuery
Language -JPQL
A Java Persistence Query Language - JPQLéumalinguagemdeconsulta,assim
comoaSQL,porémorientadaaobjetos.Issosignificaquequandoestivermos
pesquisandodados,nãoconsideramosnomesdetabelasoucolunas,esim,
entidadeseseusatributos.Atravésdessalinguagemtemosacessoarecursos
queaSQLnãonosoferece,comopolimorfismoeatémesmomaneirasmais
simplesdebuscarmosinforma çõespormeioderelacionamentos.
Vamoscome çarcomumexemplobemsimplesemSQLeemJPQL,e
depoisanalisaremosasdiferen ças. Considereaentidade Automovel,ma-
peadadeumamaneiraquetenhamosumatabelachamada T_Automoveis
nobancodedados.Entresuascolunas,existea ano_modelo.
@Entity
@Table(name="T_Automoveis")
public class Automovel {
// id e outros atributos
@Column(name="ano_modelo")
private Integer anoModelo;
}
EmSQL,podemosfazerumaconsultaquebusqueautomóveiscujoano
sejamaiorouiguala2010:
select * from T_Automoveis where ano_modelo >= 2010
NoSQL,utilizamosonomedatabelaeonomedacoluna.Contudo,para
essamesmapesquisanaJPQL,precisaremosusarapenasasinforma çõesda
entidade:
126
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 143

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
select a from Automovel a where a.anoModelo >= 2010
Podemosnotarumacertasemelhan çaentreocódigoemSQLeoqueusaa
JPQL.Naverdade,issoédesejável,jáqueSQLéumalinguagembastantecon-
hecida.Emcontrapartida,podemosanotaralgumasdiferen ças,sendoquea
primeiraestánaidentifica çãodainforma çãoquevamospesquisar:enquanto
naSQLreferenciamosonomedatabela,naJPQLreferenciamosonomeda
entidade.Omesmopode-seperceberemrela çãoàpropriedade anoModelo.
Emvezdeusarmosonomedacoluna,usamosonomedapropriedadedaen-
tidade.
Da mesma forma como fizemos uma consulta usando o operador
>=, com JPQL podemos usar todos os operadores básicos que se usa
na SQL: =, >, >=, <, <=, <>, NOT, BETWEEN, LIKE, IN, IS
NULL, IS EMPTY, MEMBER [OF], EXISTS .
Alémdosoperadores,aJPQLnospermiteusaralgumasfun ções:
6.2 Como aplicar funções nas consultas
Écomumtermosquerealizaralgumasopera çõesquemanipulemalgunstex-
tosemnossasconsultas,comoporexemplo,considerarapenasumpeda ço
deuma String,realizarconcatena çãodetextos,converterparamaiúsculo
ouminúsculoeassimpordiante. Paraessescasos,aJPQLpossuidiversas
funçõesquepodemosutilizarnasconsultas.Asprincipaissão:
•CONCAT(String, String...):Recebeumalistacomduasoumais
Stringsedevolveumasó,concatenando-as;
•SUBSTRING(String, int start [, int length]) : Recebe
umtexto, suaposi çãoiniciale, opcionalmente, ocomprimentodo
textoqueserádevolvido,eretornasóapartesolicitada;
•TRIM([[LEADING|TRAILING|BOTH] [char] FROM] String) :
Apesar de geralmente usarmos apenasTRIM(’ um texto ‘) ,
temosváriascombinações:
TRIM(' UM TEXTO ') retorna 'UM TEXTO'
TRIM(LEADING FROM ' UM TEXTO ') retorna 'UM TEXTO '
127
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 144

6.2. Comoaplicarfunçõesnasconsultas CasadoCódigo
TRIM(TRAILING FROM ' UM TEXTO ') retorna ' UM TEXTO'
TRIM(BOTH FROM ' UM TEXTO ') retorna 'UM TEXTO'
TRIM(LEADING 'A' FROM 'ARARA') retorna 'RARA'
TRIM(TRAILING 'A' FROM 'ARARA') retorna 'ARAR'
TRIM('A' FROM 'ARARA') retorna 'RAR'
Casonãoinformemosumdostrêsvalores(LEADINGouTRAILING
ouBOTH)opadrãoseráBOTH.Ecasonãoinformemosque char
queremoslimpar,seráseguidoopadrão,queélimparoespa ço;
•LOWER(String):Devolveotextoemminúsculo;
•UPPER(String):Devolveotextoemmaiúsculo;
•LENGTH(String):Devolveocomprimentodotexto;
•LOCATE(String original, String substring [, int
start]):Devolveaposi çãoemquea substringéencontradana
original,eopcionalmenteháumterceiroparâmetroindicandoem
qualposi çãoabuscadevecome çar;
Emoutrosmomentos,podemosutilizarfun çõesquetrabalhamcomval-
oresnuméricos:
•ABS(int):Devolveovalorabsoluto(semosinal)deumdeterminado
número;
•SQRT(int):Devolvearaizquadradadeumnúmero;
•MOD(int, int):Retornaorestodadivisãodoprimeironúmeropelo
segundo.Porexemplo, MOD(5, 2) é1;
•SIZE(collection): Retorna o tamanho de uma cole ção:
SIZE(marca.modelos);
•INDEX(obj):Retornaaposi çãodeumdeterminadoelementoquando
eleestiveremumalistaordenada:
128
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 145

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
select candidato from Concurso concurso
join concurso.candidatosAprovados candidato
where INDEX(candidato) < 5
Essaconsultadevolveoscincoprimeiroscandidatosaprovadosnocon-
curso.
Eporfim,podemostambémmanipulardataspormeiodefun ções:
•CURRENT_DATE:Devolveadataatualdobancodedados;
•CURRENT_TIME:Devolveahoraatualdobancodedados;
•CURRENT_TIMESTAMP:Devolveadataehoraatualdobancodedados.
6.3 Onde estão meus joins?
Fig.6.1:DERentreastabelasAutomovel,ModeloeMarca
Estamoscomnossosmodelosdemaneiraquereflitamaestruturadetabelas
mostradanafigura6.1.Quandoéprecisobuscarautomóveisefiltrá-lospelo
nomedamarca,porexemplo“Ferrari”,temosqueescreverumSQLparecido
com:
select * from Automovel auto
left outer join Modelo modelo on auto.modelo_id = modelo.id
left outer join Marca marca on modelo.marca_id = marca.id
where marca.nome = 'Ferrari'
129
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 146

6.3. Ondeestãomeusjoins? CasadoCódigo
Agoralevandoopensamentoparaomundoorientadoaobjetos,temosa
seguinteestruturadeclassesrepresentandooautomóvel,marcasemodelos:
Fig.6.2:DiagramacomasclassesAutomovel,ModeloeMarca
Comisso,podemosrealizaraconsultaparabuscarautomóveiscujamarca
seja“Ferrari”,porématravésdaJPQL.
select a from Automovel a where a.modelo.marca.nome = 'Ferrari'
Quandotemosumcaminho“navegável”deobjetossimplesnonosso
modelonãoprecisamosdequalquer join.AJPAabstraiessanecessidade,
eaprópriaimplementa çãoqueestivermosusandofaráaconversãoparaos
joinsadequados.Porisso,dizemosqueaJPQLéumalinguagemdeconsulta
orientadaaobjetos:senós,atravésdenossosobjetos,conseguimosacessar
outrosobjetos,entãoaJPQLtambémconsegue.
Issosignificaqueos joinsestãoabolidosdonossodicionário?Aresposta
énão.Paratrabalharmoscomcole çõesdeobjetosprecisamosescrevê-lo.
Aindausandoosmesmosmodelos,vamosconsiderarqueprecisamos
buscarmarcasquetenhamalgummodelocom“911”emsuadescrição.
EmSQLteríamosaseguinteconsulta:
select * from Marca marca
left outer join Modelo modelo on marca.id = modelo.marca_id
where modelo.descricao like '%911%'
Agora,comoestamospesquisandodentrodalista,precisamosdo join
tambémnaJPQL:
select marca from Marca marca
join marca.modelos modelo
where modelo.descricao like '%911%'
130
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 147

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
6.4 E xecute suas consultas e use parâmetros
Nosexemplosquevimosatéaqui,sempredeixamososparâmetrosnaprópria
consultaporquestõesdidáticas,masemumcódigorealraramentetemos
parâmetrosfixos.Veremosagoracomopassá-losparanossa query.
Para efetivamente enviar a consulta escrita na linguagem
JPQL para JPA executar, nós precisamos de um objeto do tipo
javax.persistence.Query que conseguimos através do método
createQueryda EntityManager. Apartirdele,podemosalimentaros
parâmetros que são definidos por:nome_do_parametro(dois pontos
maisonomedoparâmetro).
String jpql =
"select a from Automovel a where a.modelo.marca.nome =
:nomeMarca";
Query query = entityManager.createQuery(jpql, Automovel.class);
query.setParameter("nomeMarca", "Ferrari");
List<Automovel> automoveis = query.getResultList();
Podemosperceberquechamamosoparâmetrode nomeMarca,masao
utilizá-lonaconsulta,devemoscolocaro :antes,paraidentificá-locomoum
parâmetro.Alémdisso,indicamosparaométodo createQuery,qualéo
tipoderesultadoquequeremosnanossaconsulta,quenocasoéumobjeto
dotipo Automovel. Comisso,a querysabequeprecisarádevolveruma
listadeobjetosdessetipo.
Podemostambémpassarumobjetodeumaentidadecomoparâmetro,e
nãoapenastextos,númerosoudatas. Umexemplodissoéoquepodemos
veraseguir.
String jpql =
"select a from Automovel a where a.modelo.marca = :marca";
Marca marca = ...
Query query = entityManager.createQuery(jpql, Automovel.class);
query.setParameter("marca", marca);
131
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 148

6.5. Utilizefunçõesdeagrega ção CasadoCódigo
List<Automovel> automoveis = query.getResultList();
Quandopassamosumobjetodeumaentidadeparaaconsulta,achaveé
utilizadaparafazerabusca,ouseja,a marcaseráfiltradapeloseu id.
6.5 Utilize funções de agregação
Podemoscalcularamédiadosanosdemodelodosautomóveisquetemos
cadastrados.Pararealizaressecálculo,écomumutilizarmosumafun çãoque
façatodootrabalhoparanós,umavezdadaumapropriedade.Essasfun ções
sãoconhecidascomofun çõesdeagrega ção,eaJPQLasdisponibilizapara
usarmos:
•AVG(property):Devolveamédiadevaloresnuméricos;
•MAX(property):Devolveovalormáximoentrevalorescomparáveis
(números,datas,strings);
•MIN(property):Devolveovalormínimoentrevalorescomparáveis
(números,datas,strings);
•SUM(property):Devolveasomadevaloresnuméricos;
•COUNT(property):Devolveaquantidadedeelementos.
Então,paracalcularmosamédiados anoModelo,teríamosaconsulta:
select AVG(a.anoModelo) from Automovel a
Precisaríamos apenas executar essa consulta, através da
javax.persistence.Query:
String jpql = "select AVG(a.anoModelo) from Automovel a";
Query query = entityManager.createQuery(jpql, Double.class);
Double media = query.getSingleResult();
132
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 149

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
Repareque,paraaagrega çãoquedevolveapenasumvalor,indicamosno
momentodechamaro createQueryqueoretornoé Double-queéotipo
resultantedamédia,enãomaisum Automovel,comofizemosantes.Além
disso,nahoraderecuperaroresultado,nãoteremosváriositens,esimum
só,queéoprópriovalor.Porisso,chamamosométodo getSingleResult
enãoo getResultList.
6.6 Faça sub -consultas com a JPQL
ComaJPQL,podemoscriar subselectsnasnossasconsultas. Aseguir,um
exemploquepesquisaautomóveisacimadamédiadeidade:
select a from Automovel a
where a.anoModelo >
(select AVG(auto.anoModelo) from Automovel auto)
Nesse subselectdefinimosumoutro aliaspara Automovel,jáqueasvar-
iáveisdo selectdeforaestãodisponíveisno subselect.
Podemosrealizaraindaconsultasmaiselaboradas. Agoraprecisamos
buscartodasas Marcasquetenhampelomenosum Automovelquecuste
pelomenosR $1.000.000(ummilhãodereais).
select marca from Marca marca where EXISTS (
select a from Automovel a where
a.modelo.marca = marca and a.preco >= 1000000
)
Reparenousodo EXISTSparaverificarqueasub-consultadevolveal-
gumresultadoparaaquela marca.
6.7 Agrupamentos e HAVING
Paraterminarnossapassagempelasop çõesdepesquisa,vamosanalisarum
casodeagrupamentocomarestri çãodegrupo.
select a.marca, COUNT(a) from Automovel a
GROUP BY a.marca
HAVING COUNT(a) > 10
133
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 150

6.8. Consultascomplexas...resultadoscomplexos? CasadoCódigo
Nesseexemplo,agrupamososautomóveispor marcaefizemosacon-
sultadevolveramarcaesuaquantidadedeautomóveis.Porfim,restringimos
apesquisaamarcascompelomenos10automóveis.
Mas...comofazemospararecuperara marcaeoresultadodo count,
sequandochamamosométodo createQuery,temosquedizerotipoda
informaçãoqueaconsultadevolve? Nãotemosumtipoquerepresentea
marcaeaquantidade .
6.8 C onsultas complexas ... resultados com -
plexos?
Namaioriadosexemplosquevimosatéagora,quasesemprelidamoscomo
objetocompleto:
select a from Automovel a
Masemalgunsexemplosquevimos,eprovavelmenteemmuitosmomen-
tosdonossodiaadiavamosvermais,hánecessidadedelistarmosapenas
partedoobjeto:
select a.descricao, a.preco from Automovel a
Nessescasosaconstru çãodapesquisaésimples.Mascomoficaoretorno
dessa Querynocódigojava?Éissoqueveremosapartirdeagora.
String jpql =
"select a.modelo.marca.nome, a.descricao, a.preco from
Automovel a";
Query query = entityManager.createQuery(jpql);
List<Object[]> result = query.getResultList();
for(Object[] row : result){
String nomeMarca = (String) row[0];
String descricao = (String) row[1];
Float preco = (Float) row[2];
}
134
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 151

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
Como é possível vermos no exemplo, quando invocamos o método
getResultListda Query,oretornoquetemosédotipo List. Mas
comonãoestamosdevolvendoum Automovelcompleto,nãoteremosum
List<Automovel>.Emvezdisso,estamosdevolvendováriaspropriedades
diferentes,detiposdiferentesedeobjetosdiferentes. Comtantaspossibili-
dades,nãohácomoespecificaresseresultadomaisdoquecomum array
de Object,emquecadapropriedadedaproje çãoaparecenamesmaordem
dentrodo array.
Existe,porém,umafuncionalidadequenospermitelidarcomproje ções
deformamais“agradável”doquemanipulandoumObject[].Éa select
new.
6.9 Use oSelectNew e esqueça os arrays de Ob-
ject
Apesardeemboapartedosistemalidarmoscomconsultasquedevolvemob-
jetoscompletos,emalgumassitua ções,nãotemoscomofugirdasproje ções.
Jávimoscomotratá-las,masnãoqueremosmanipular Object[]dentrodo
nossocódigo,jáqueseriaextremamentetrabalhoso.
Analisandooproblemaquetemos,verificamosqueprecisamosdeumob-
jeto,quenãofazpartedonossomodelo,masqueprecisaexistirparatransferir
oresultadodaconsultadeumaformamaisestruturada.Paraisso,vamoscriar
umaclassequerepresenteessasinforma ções.
public class ResumoAutomovel {
private String marca;
private String modelo;
private String descricao;
private Float preco;
public ResumoAutomovel(String marca, String descricao,
Float preco) {
//copia os parâmetros para as propriedades do objeto
}
135
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 152

6.10. OrganizesuasconsultascomNamedQueries CasadoCódigo
//getters e setters se necessário
}
Agoraquetemosesseobjeto,podemospedirparaaJPAusá-lopararep-
resentarnossaconsulta. Parafazermosisso, bastainstanciaroobjetono
select.
String jpql = "select new facesmotors.ResumoAutomovel" +
"(a.modelo.marca.nome, a.descricao, a.preco) from Automovel a";
Query query = entityManager.createQuery(jpql);
List<ResumoAutomovel> result = query.getResultList();
Aconsultacom select new iráchamar,paracadalinharetornada,o
construtordaclasseinformadaexatamentecomosmesmosparâmetrosque
constamnaconsulta.
6.10 Organize suas consultas com Named
Queries
Agoraquejávimoscomocriarnossasconsultasecomolidamoscomelasno
códigoJava,vamosverumrecursoquenosforneceumamaneiradiferente
deorganizá-las.Esserecursosechama named query.
@NamedQuery(name="Automovel.listarTodos",
query="select a from Automovel a")
@Entity
public class Automovel {
// atributos e métodos
}
As named queriestêmessenomeporquesãoconsultascomumnome
único. Noexemplo, demosonome Automovel.listarTodosàcon-
sulta select a from Automovel a ,quesimplesmentelistatodososau-
tomóveis. Nóscostumamoscolocaraconsultaemcimadaentidadequeé
retornadaporela. Nessecaso,comonossaconsultaretornaumalistade
Automovel,colocamo-lanessaentidade.
136
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 153

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
Um ponto importante é que o nome daquery deve ser único, por
isso geralmente costumamos usar o nome da entidade no nome da
queryparaevitarconflitos. Semisso, teríamosquecolocarnomescomo
listarTodosAutomoveis. Obviamenteissoéapenasumasugestãode
convenção.
Em um primeiro momento, anamed query pode parecer não ajudar
muito,atéporqueaconsultaqueestamosanalisandoémuitosimples,mas
vamosevoluirmaisesseexemplo.
@NamedQuery(name="Automovel.listarTodos",
query="select a from Automovel a where a.ativo = true")
@Entity
public class Automovel {
// outros atributos e métodos
private boolean ativo;
}
Agorafizemosumapequenamodifica çãonanossaclasseenaconsulta.
Vamosconsiderarqueosautomóveispararamdeserexcluídosfisicamente
dobanco,eagorapossuemumapropriedadequemarcaselogicamenteoob-
jetofoiexcluídoounão. Seemvezdeconcentraraconsultadeautomóveis
emumúnicolugarnósativéssemosespalhadopelaaplica ção,teríamosque
buscartodososlocaisondeelaerafeitaemudar.Senão,automóveis“fantas-
mas”começariamaaparecerparaosusuários.Eolhaqueaquela queryinicial
pareciatãoinofensivaqueachamosquenemvaleriaapenafazerisso.
Atéaívocêpodeseperguntar:“Masseeuencapsulassetodasasconsultas
emmétodosde DAO,eunãoteriaomesmoresultado?”.Arespostaé:“Sim,
teria!”.Ficaacargododesenvolverescolherondesepreferecolocarocódigo
daconsulta.
Umavantagemmaisvisíveléqueas named queriessãochecadasenquanto
ocontextodaJPAseinicia.Entãosefizermosmaisumamudan çanonosso
modelo,para,porexemplo,guardaradatadaexclusãoemvezdesomente
umatributo,masesquecermosdealterara query,teremosumerro:
137
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 154

6.10. OrganizesuasconsultascomNamedQueries CasadoCódigo
//esquecemos de mudar a consulta
@NamedQuery(name="Automovel.listarTodos",
query="select a from Automovel a where a.ativo = true")
@Entity
public class Automovel {
@Temporal
private Date dataExclusao;
}
Erro!
ERROR: HHH000177: Error in named query: Automovel.listarTodos
org.hibernate.QueryException: could not resolve property: ativo
of: facesmotors.entities.Automovel
[select a from facesmotors.entities.Automovel a where
a.ativo = true]
Entãoagoravamosarrumarnossa named query.
@NamedQuery(name="Automovel.listarTodos",
query="select a from Automovel a " +
"where a.dataExclusao is null")
@Entity
public class Automovel {
@Temporal
private Date dataExclusao;
}
Umaquestãoqueacabasurgindoésenãoexisteumaforma type safede
fazermosnossasconsultas. Ouseja,emvezdedependerdetextosquenão
sãovalidadospelocompilador,porquenãoescreverconsultasquedeemerro
decompila çãoemcasoscomoodoexemploqueacabamosdever?
Arespostaéqueessesuporteexiste.Foiadicionadonaversão2.0daJPA
echama-se CriteriaBuilder.Atravésdessaclasse,podemoscriar queries
programaticamenteeocompiladorgeraumaespéciedeclasseauxiliarpara
cadaentidade.Entãofazemosnossasconsultasusandoessasclasses.Noen-
tanto,essaAPIéextremamentecomplexaetornamuitocustosaaescritade
138
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 155

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
consultasrelativamentesimples.Poressemotivo,suaado çãonomercadoé
aindaquasenenhuma.
6.11 Execute asNamed Queries
Jávimoscomoexecutaruma querysimplesdentrodeumaclasseJava.Agora
veremoscomopraticamentenãomudanadacomousodas named queries.
Query query = em.createNamedQuery("Automovel.listarTodos",
Automovel.class);
List<Automovel> automoveis = query.getResultList();
Aúnicadiferen çaéque,emvezdeusarmosométodo createQuery,
usamoso createNamedQuery.Este,emvezdereceberaJPQL,recebeso-
menteseunome,jáqueelajáestádefinidanaanota çãoemcimadaentidade.
Foraissonadamuda,oretornodométodocontinuasendouma Query.Para
passarparâmetrosouexecutá-ladevemosfazerexatamentecomofazíamos
coma querynormal.
Nesseexemplopodemosnotaroutrodetalhe:comoonomeda queryé
uma Stringéumapráticacomumdefinirumaconstanteparaquenãoer-
remosnadigita çãoetambémparapodermosusarrecursosdecompleta ção
decódigoaodigitaronomeda query.
@NamedQuery(name=Automovel.BUSCAR_TODOS,
query="select a from Automovel a " +
" where a.dataExclusao is null")
@Entity
public class Automovel {
// outros atributos e métodos
public static final String BUSCAR_TODOS =
"Automovel.listarTodos";
private Date dataExclusao;
}
Eocódigoquerealizaaquery:
139
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 156

6.12. RelacionamentosLazy,N+1QueryeJoinFetch CasadoCódigo
Query query = em.createNamedQuery(Automovel.BUSCAR_TODOS,
Automovel.class);
List<Automovel> automoveis = query.getResultList();
Agoradefinimosumaconstanteepodemosusarocompletadordecódigo
daIDEparaverasconsultasdisponíveisnaclasse Automovel.
6.12 Relacionamentos Lazy, N+1 Query e Join
Fetch
Nocapítulo5forammostradosostiposderelacionamentosentreasenti-
dades. Umadasmaisimportantesfuncionalidadesquefoimostradaéo
relacionamento lazy,queporpadrãoocorreemtodososrelacionamentos
ToMany.Ouseja,todavezquenossaentidadetemumrelacionamentoque
éumalista,esserelacionamentoserá lazy. Agoraseorelacionamentofor
comumúnicoobjeto,ouseja,umrelacionamento ToOne,eleserá eagerpor
padrão.Masvimosquenessescasosépossívelalteraropadrãoparaquetam-
bémseja lazy.
Umrelacionamento lazypodeevitarocarregamentodesnecessáriode
milharesderegistros,comovimosnase ção5.14. Assim,sefôssemoslistar
vinte Marcasquepossuem,cadauma,dez Modelos,evitamosdecarregar
duzentosobjetosquandonãousamosos Modelosaolistaras Marcas.Mas
ese,poracaso,emumatelamaiscomplexafornecessáriolistarcadaitemde
umalistaqueé lazy?Aíoqueeraumavantagempassaadarmaistrabalho
paraotimizar.
Vamosconsideraroseguintemodelo:
@Entity
public class Marca {
@Id @GeneratedValue
private Integer id;
private String nome;
@OneToMany(mappedBy="montadora") //LAZY por padrão
140
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 157

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
private List<Modelo> modelos;
}
@Entity
public class Modelo {
@Id @GeneratedValue
private Integer id;
private String descricao;
@ManyToOne
private Marca montadora;
}
Comonãoalteramosopadrão,orelacionamentode Marcacom Modelo
élazy. Então,casotenhamosaseguintelistagemde Marcas,nãoteremos
nenhumcarregamentoindesejadodeobjetos.
<h:dataTable value="#{marcaBean.marcas}" var="marca">
<h:column>
<h:facet name="header">Nome da Marca</h:facet>
#{marca.nome}
</h:column>
</h:dataTable>
Consideraremosaquique #{marcaBean.marcas}simplesmentere-
tornaumalistade Marca,similarcomoquevimosnocapítulo3.
@ManagedBean
public class MarcaBean {
private List<Marca> marcas;
@PostConstruct
public void carregaMarcas(){
EntityManager em = JpaUtil.getEntityManager();
141
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 158

6.12. RelacionamentosLazy,N+1QueryeJoinFetch CasadoCódigo
marcas =
em.createQuery("select m from Marca m", Marca.class)
.getResultList();
em.close();
}
public List<Marca> getMarcas(){
return marcas;
}
}
Agora,estamosusandoumrecursonovo,queéo @PostConstruct.
Ele indica um método que será invocado quando o JSF precisar desse
ManagedBean. Dessaforma,tambémgarantimosqueaconsultaseráreal-
izadasomenteumavezparacadarequisi ção.
Masagoraprecisaremosdeumamodifica çãoquemudatodoocenário:
vamoslistaros Modelosdecada Marca:
<h:dataTable value="#{marcaBean.marcas}" var="marca">
<h:column>
<h:facet name="header">Nome da Marca</h:facet>
#{marca.nome}
</h:column>
<h:column>
<h:facet name="header">Modelos Cadastrados</h:facet>
<ul>
<ui:repeat value="#{marca.modelos}" var="modelo">
<li>#{modelo.descricao}</li>
</ui:repeat>
</ul>
</h:column>
</h:dataTable>
ATag <ui:repeat>,vemdoFaceletsetemcomopapeliterarsobreuma
Collection,fazendoopapeldeum foreach.
Executando novamente nossa tela teremos uma
LazyInitializationException. Essa, na verdade, é uma exceção
doHibernate,queéaimplementa çãodeJPAqueestamosutilizando. Mas
independentementedaimplementa çãoescolhida,teremosumaexce ção.
142
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 159

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
Omotivodoproblemaéofechamentodo EntityManagerdentro
dométodo carregaMarcasdo MarcaBean. Ouseja,nomomentoem
queaconsultaprecisaserrealizadaparabuscarosmodelosnobancode
dados, aconexãonãoestámaisaberta. Noentanto, senãofecharmosa
EntityManager,teríamosumaconexãoabertaenãoliberadaacadareq-
uisiçãoparaessapágina,ouseja,impraticável.
Nesse ponto, se não soubéssemos das vantagens do uso dolazy,
poderíamossimplesmentemudarorelacionamentopara eagereresolvero
problema. Masnãopodemosesquecerquemexernomapeamentoéalgo
muitosério,jáquevaleparaosistematodo,emtodasassitua ções.Ésóimag-
inarmosqueumalistagemde Marcaspodeserusadaemumcombo.Enesse
casocertamenteestaríamoscarregandodiversos Modelossemnecessidade.
Para resolver essa questão de ter que liberar recursos, no caso a
EntityManager,masaomesmotemponãomudaromapeamentoeainda
deixaraaplica çãofuncionando,foicriadoumpadrãochamado“OpenEntity
ManagerinView”.
6.13 Evite aLazyInitializationException com o
OpenEntityManagerInView
A LazyInitializationException ocorre quando tentamos acessar
propriedades lazyqueaindanãoforaminicializadas,masa EntityManager
quetrouxeoobjetodobancojáfoifechada.
Asolu çãoparaoproblemaéfechara EntityManagernomomento
correto.Seanalisarmos,percebemosqueoerroaconteciaporque,durantea
renderizaçãodatela,enquantoa h:dataTableiteravasobreoselementos,
foiqueocorreuaexce ção. Issoquerdizerquepodemos(edevemos)sim
fechara EntityManager,sótemosquetomarocuidadodefazerissodepois
queaprocessamentodetodaatelaterminar.
Existemdiversassolu çõesparaesseproblema,sendoqueumadasmais
comunsépormeiodaimplementa çãodeum javax.servlet.Filter.
Comojávimostambém,pararealizarqualquerescritanobancoviaJPA
precisamosdetransa ções.Sevocêestiverdesenvolvendosuaaplica çãopara
poderserexecutadaemum Servlet Container,comoporexemploJettyou
143
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 160

6.13. EviteaLazyInitializationExceptioncomoOpenEntityManagerInView CasadoCódigo
Tomcat,énecessáriotratarastransa çõesdiretamente,masnãoprecisamos
deixaressetratamentodentrodecadamétodoquesesalvanobanco.Emvez
disso,deixamosessecódigono Filter.Seestivéssemosutilizandoum Ap-
plication ServercomoJBossouGlassfish,poderíamosdeixarotratamentode
transações,eacria çãoefechamentoda EntityManageracargodoservi-
dor.
Dessa forma, bastaria que implementássemos um filtro que abrisse a
EntityManagereatransa ção,eemseguidadelegasseotratamentoparao
framework;enofinal,quandotudojáestivesseprocessado,fizesseo commit
ouo rollbackdatransa çãoefechassea EntityManager.
@WebFilter(urlPatterns="/*")
public class OpenSessionAndTransactionInView implements Filter {
@Override
public void doFilter(ServletRequest request,
ServletResponse response,
FilterChain chain)
throws IOException, ServletException {
// inicia a transação antes de processar o request
EntityManager em = JpaUtil.getEntityManager();
EntityTransaction tx = em.getTransaction();
try {
tx.begin();
// processa a requisição
chain.doFilter(request, response);
// faz commit
tx.commit();
// ou em caso de erro faz o rollback
} catch (Exception e) {
if(tx != null && tx.isActive()){
tx.rollback();
}
}
finally {
144
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 161

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
em.close();
}
}
@Override
public void init(FilterConfig filterConfig)
throws ServletException {
}
@Override
public void destroy() {
JpaUtil.closeEntityManagerFactory();
}
}
Agoracomofiltroimplementado,seapáginaforacessada,nãohaverá
mais LazyInitializationException. Noentanto,quandotivermos
muitasmarcasemodelosassociados,perceberemosquemuitasconsultases-
tãosendofeitasnobancodedados. Umaparacada Marcaqueexisteno
banco.Ondeestáoproblemaagora?
6.14 O problema das N+1 consultas e como
resolvê-lo
Vamosentendermelhoroqueestáacontecendo.Asváriasconsultasocorrem
porquefazemosumabuscaporumalistade Marca,que-atéomomentoem
queéexecutada-dentrodométodo carregaMarcas(),nãosabequeos
modelosserãousados.
Considerequetemos10marcascadastradasnobancodedadosequepara
cadaumadelastemos20 modelosassociados. Acadaitera çãodanossa
h:dataTable,umainstânciadiferentede Marcaéusadaecadaumapossui
umalistade Modeloqueaindanãofoicarregadadobanco. Porém,nessa
mesmaitera ção,nasegundacolunado dataTable,nósusamosessalista.
EntãoaJPAprecisacarregá-ladobanco,usandoumanovaconsulta. Esse
145
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 162

6.14. OproblemadasN+1consultasecomoresolvê-lo CasadoCódigo
procedimentoérepetidoparacadaumadasdezinstânciasde Marca,ou
seja,serãodezconsultasadicionais.
Tivemosnoinícioumaprimeiraconsultaquebuscouas Marcasno
bancoeretornou10objetos.Paracadaumadas10marcas,tivemosumacon-
sultaextraparabuscarseusmodelos,eporissodizemosquetivemosN+1
consultas.Néonúmerodeobjetosretornadospor1consultaoriginal.Nesse
caso,tivemos11consultas. Aprimeiraparabuscarasmarcas,eumapara
buscarosmodelosassociadosacadaumadas10marcas.
Pararesolveresseproblema,aop çãomais“certeira”étratarorelaciona-
mentocomosefosse eagersomentenessecaso.Comonãopodemosmexer
nomapeamentoporqueafetariaoutrasáreasdaaplica ção,mudamosnanossa
consulta.Sabemosque,comaJPA,parabuscaras Marcasprecisamosfazer
apenasoseguinte:
select m from Marca m
Como Marcapossuiumrelacionamentocom modelosessecarrega-
mentoéautomático. Sóprecisaríamosfazerum joincom Modelose
quiséssemosfazeralgumabuscacomoessa:
select marca from Marca marca
join marca.modelos modelo
where modelo.cilindradas > 500
Mas agora, precisamos de umjoin somente para carregar a lista
marca.modelos. Paraessefimtemoso join fetch. Usandoessain-
struçãofazemosumaconsultacomosefosse fetch=EAGERnorelaciona-
mento.Nossaconsultaentãoficariaassim:
select marca from Marca marca join fetch marca.modelos
Agoraconseguimosfazercomquequeumrelacionamentoqueé lazyse
comportecomosefosse eagersomentenessaconsulta.Masaten ção,ocon-
trárionãoépossível. Nãotemcomodefinirmosumrelacionamentocomo
eagerefazerumaconsulta lazyparacarregarumsimplescombo,porexem-
plo. Porisso,geralmentedeixamosomapeamento lazye,casoprecisemos,
forçamosocarregamentosomenteemumaconsulta.
146
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 163

CasadoCódigo Capítulo6. ConsultascomaJPQLeosproblemascomunsnaintegra ção...
6.15 Foi bastante, mas não acabou ...
AgoraquevocêjásabecomorealizarconsultascomaJPAetambémjácon-
seguerealizarasopera çõesbásicasdecadastro,altera çãoeexclusão,vocêjá
deveestarprontoparaencararagrandemaioriadossistemasqueenvolvam
essatecnologia.Claro,atecnologianãoacabaporaí,aindavamosvermuito
mais.Damesmaforma,aindatemosbastanteaversobreoJSF.Eéjustamente
daíquevamoscontinuar.
147
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 164

E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 165

Capítulo7
EntendaoJSFecrieaplica ções
web
Vimosnocapítulo3comoconstruirtelasutilizandoJSFefizemosformulários
elistagens.Nestecapítulo,teremoscomoobjetivooentendimentodecomoo
JSFfuncionapordentro.Nase ção7.11veremoscomoconstruirtelasusando
componentesricosecomponentescustomizados.
PelofatodoJSFserconstruídousandoumparadigmadiferentedamaio-
riadosframeworksWeb,duranteoprocessodeaprendizagemécomumque
tenhamosalgumasdificuldadescomessanovamaneiradecriaraplica ções
web.Então,primeirovamosentendercomoessemundonovofunciona,eaí
simestaremosprontosparapraticar.
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 166

7.1. Seprepareparaummundodiferente,baseadoemcomponentes CasadoCódigo
7.1 Se prepare para um mundo diferente ,
baseado em componentes
Quandovocêcomeçouaprogramar,seuprimeiroparadigmafoiaorienta ção
aobjetosouelalhefoiapresentadadepoisquevocêjátinhafeitodiversos
sistemas?Vocêinicioudesenvolvendoaplica çõesDesktopedepoisprecisou
irparaaweb?Quempassouporumadessasmudan ças:doproceduralpara
oOOoudoDesktopparaaWebvaientenderoquãodifícilépassarporuma
mudançadeparadigma.
Introduzi esses exemplos porque assim como existe mudança de
paradigmaentreaprograma çãoDesktopeaWeb,existemudan çatambém
aodesenvolverWebcomumaferramentabaseadaema çãoeumabaseadaem
componentes.Frameworkscomo VRaptor,SpringMVCeRubyonRails são
baseadosema ção,jáJSF,TapestryeWicketsãobaseadosemcomponentes.
Apesardetermosdiferen çasnofuncionamentodoladoservidor,ouseja,
desdeasubmissãodasinforma çõesdousuárionatelaatéprocessarmosalóg-
icadaaplica ção,aprincipaldiferen çadoJSFestánacamadadevisualiza ção.
Pelofatodeeletercomponentespróprioseutilizá-los,assimcomofizemos
nocapítulo3comastags h:form, h:inputTexteoutras,oresultadofinal
éumHTMLgeradoenãoumescritopornós.
QuandooJSFsurgiu,aideiaerafazercomonoWebFormsdo.Net,onde
teríamosferramentasdeclicarearrastarquemontariamatelaparanós.Ape-
sarde,noinício,teremsurgidoalgumasassim,averdadeéqueodesenvolve-
dorJavanãopossuiessacultura.Aconsequênciaéquehojeemdiaessaideia
praticamenteinexiste.Escrevemosnósmesmosocódigodaspáginas,emar-
quivos .xhtml.
7.2 A web stateless contra a web stateful
Quandodesenvolvemoscomumframeworkbaseadoema ção,comooclás-
sico Struts,écomumtermostagsquenosauxiliamnodesenvolvimentoda
view.Issopassaafalsaimpressãodequeeletambémestáligadoàtelaassim
comooJSF,noentanto,sevocêquiserignoraressastags,fazendotudona
mão,vocêpode.
150
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 167

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
Quandovamossubmeterumateladanossaaplica çãobaseadaema ção,
poucoimportaoestadoda view,comoelafoiescrita,tampoucoseemvezde
serumJSPelaforumHTMLestático. Oqueimportaéqueserámontada
umarequisi çãoqueterácomoparâmetrososcamposcontidosnoformulário
quevocêescreveu.Frameworksbaseadoema çõesnãoconhecematela,con-
hecemo requesteasinforma çõesqueestãosendopassadasnele.
Emcontrapartida,quandotrabalhamoscomJSF,eleéquemcriaatela.O
processonãoénadacomplicado,éatésimplesdeentender,sóquegeralmente
jásaímosfazendonosso Hello Worldenãoparamosparavercomoascoisas
funcionam.ComJSF,quandochamamosnossa pagina.xhtml,emvezde
executarmosumaServlet,oJSFvaileressearquivoemontaremmemória
umaárvoredecomponentes,conformepodemosvernafigura7.1. Depois
queessaárvoreémontada,elaépassadaparaumrenderizador.
Dessaforma,aárvoredecomponentesrepresentaapenasaestruturada
página,eoJSFautilizaráparaescreveroHTMLacadanóquepassar.
Fig.7.1:Árvoredecomponentesemmemória
151
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 168

7.2. Awebstatelesscontraawebstateful CasadoCódigo
Paracriaraestruturadaimagemanterior,bastariaumsimplescódigo
paramontarumformulário:
<h:form>
<h:panelGrid columns="2">
Marca: <h:inputText value="#{marcaBean.marca.nome}"
required="true"/>
</h:panelGrid>
<br/>
<h:selectBooleanCheckbox
value="#{marcaBean.continuarInserindo}"/>
Continuar Inserindo?
<br/>
<h:commandButton value="Salvar"
action="#{marcaBean.salvar}"/>
</h:form>
Masoqueissotemavercomstatefulmesmo? Adiferen çamaissigni-
ficativadoJSFemrela çãoàServlet(geradaautomaticamentebaseadaemum
JSP)nãoénagera çãodoHTML,istoé,naidadoservidorparaocliente,esim
quandooclientesubmeteoformulárioapresentado. Enquantonosframe-
worksbaseadosema çõestantofazcomoatelafoicriada,oJSFguardana
memóriaqualfoiaárvoreusadaparageraraquelatela.
UmavezqueoJSFconseguiuaárvoredecomponentes,elevaicomparar
cadaatributodarequisi çãocomoscamposqueestavamdisponíveisparao
usuário.Afinal,comofoioJSFquemgerouatela,elesabeexatamentequais
camposestavamdisponíveise,emcasodesele çõescomocombos,radiose
selects,sabetambémquaisop çõesestavamlá.
Tendotodasasinforma çõesnamão,oJSFvalidaseosdadosenviadossão
compatíveiscomosdisponíveis,ecasonãosejam,eleindicaquearequisi çãoé
inválida.ÉexatamentepelofatodeoJSFconhecertodooestadodanossatela,
eguardarissoatravésdasrequisi ções,queoconsideramosumframework
stateful.
152
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 169

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
7.3 Ociclo de vida das requisições noJSF
EntenderociclodevidadoJSFébasicamenteentendercomoelefunciona,e
éumatarefaobrigatóriaparaqualquerpessoaquevaiutilizá-lo.
TodoociclodevidadoJSFécompostopor6fases,nasquaisdiversas
tarefassãorealizadas.Masnãoseassuste,veremosqueémaissimplesdoque
pensávamos.
7.4 Fase1-C riar ou restaurar a árvore de com -
ponentes da tela (RestoreView)
Quando uma requisição chega ao JSF, a primeira tarefa realizada por
ele é construir ou restaurar a árvore de componentes correspondente
ao arquivo XHTML lido. Por exemplo, quando acessamos a página
cadastraAutomoveis.xhtmldanossaaplica ção,oJSFbuscaporpadrão
oarquivodemesmonomeparaconstruiratela.
Apesardonome Restore View,quandoatelaéacessadapelaprimeiravez
aárvoredecomponentesserácriada. Comojáfoiexplicadonase ção7.2,o
JSFlêo xhtmlecriaemmemóriaaárvoredecomponentes.
Paraconseguirmosenxergaroqueacontece,considereocódigoaseguir:
<h:form>
<h:inputText value="#{pessoa.nome}"/>
<h:inputText value="#{pessoa.idade}">
<f:validateRequired/>
</h:inputText>
</h:form>
Eaclasse Pessoa:
public class Pessoa {
private String nome;
private Integer idade;
//getters e setters
}
OJSFirácriarumainstânciade javax.faces.component.html.HtmlForm,
uma classe dele mesmo, que representa através de código
153
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 170

7.5. Fase2-Aplicarvaloresdarequisi çãonaárvoredecomponentes(ApplyRequestValues)CasadoCódigo
Java um h:form, e colocará abaixo dela duas instâncias de
javax.faces.component.html.HtmlInputText, que represen-
tam o h:inputText. No segundo HtmlInputTextserá chamado o
método addValidator passando como parâmetro uma instância de
javax.faces.validator.RequiredValidator.
Considerandoqueusuárioestejarequisitandoapáginapelaprimeiravez,
apósacria çãodaárvoredecomponentes,o requestvaidiretoparaafase6,
naqualserárenderizadaarespostaparaousuário.
Casoousuáriojáestejautilizandoaaplica ção,aárvore,emvezdeser
criada,serárecuperadadasessãodousuário. OJSFfazumcachedeár-
vores,guardandonasessãodousuáriooestadodastelasacessadasporúl-
timo. OutraalternativaésolicitarqueoJSFarmazeneoestadonocliente.
Nessecaso,aárvoreseráserializadaeenviadaemumcampoocultodentro
doHTMLgerado,equandoousuáriosubmeternovamenteelaserárecon-
struídaapartirdovalordessecampooculto.
Essaconfigura çãoéfeitano web.xmlcomopodemosveraseguir.
<context-param>
<param-name>javax.faces.STATE_SAVING_METHOD</param-name>
<!-- valor padrão é server -->
<param-value>client</param-value>
</context-param>
Depoisqueaárvoreérestaurada,sejabuscandonasessãoouviadeseri-
alização,arequisi çãodousuáriosegueparaafase2.
7.5 Fase2-A plicar v alores da requisição na ár -
vore de componentes (ApplyRequestValues)
AquioJSFirábuscarosvaloresinformadospelousuárioecolocá-losnosseus
respectivoscomponentes.Considerandoqueousuáriotenhaentradocomo
nome“João”eaidade“28”,opseudocódigoaseguirseriaexecutadonessa
fase.
HtmlInputText nome = ... // JSF já conhece o componente
nome.setSubmittedValue("Fulano");
154
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 171

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
HtmlInputText idade = ... // JSF já conhece o componente
idade.setSubmittedValue("28");
O importante aqui é entendermos que o JSF chama o método
setSubmittedValuepassandoovalorqueousuáriodigitou,semsepre-
ocuparseeleéválidoounão.Pormaisqueousuáriotivesseinformado“ABC”
naidade,essevalorseriapassadoparaessemétodoeocomponenteteriaesse
valornasuapropriedade submittedValue.
7.6 Fase3-C onverter e Validar(Validate)
Essasemdúvidaéafasemaisconhecida,jáque,sevocênãoentendercomo
funcionaoJSF,certamentemaiscedooumaistardeteráalgumerrodecon-
versãooudevalida ção.Essafaseédivididaempartes,comooprópriotítulo
dase çãoinforma:converteevalida.
Emnossoexemplo,aconversãoserátransformara String idade =
"28"em Integer idade = 28 . Casoousuárioinformassealgocomo
"28a",teríamosumerrodeconversão.
OJSFjápossuiconversoresprontosparaostiposbásicoscomo Integer,
Long, java.util.Date,entreoutros. Masequandoprecisarmoscon-
verterumcódigodefuncionárioparaumobjetodanossaaplica çãodotipo
Funcionario? PrecisaremosregistrarnoJSFumconversorcustomizado,
comoveremosnase ção7.36,masoprocessodeconversãodoJSFéomesmo.
OJSFdescobrequalaclassedoobjetoqueestávinculadacomo value
docomponente,quenocasodaidadeédotipo Integer,eentãobuscano
seucontextoumconversorparaessetipo.
Depoisdeconvertido,ovalorinformadopelousuárioserávalidado.No
casodocomponentequereferenciaidadetemoso RequiredValidator
agindoemcimadeum Integer,enãoemcimadeuma String.Damesma
forma,sefosseumvalidadordeintervalo, LongRangeValidator,omesmo
validariaumnúmero,enãoumaString.Sóconsideramoserrodevalida ção
seaconversãoaconteceucomsucesso,senãoteremoserrodeconversão.
155
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 172

7.7. Fase4-Atualizaromodelo(UpdateModel) CasadoCódigo
7.7 Fase4-A tualizar o modelo (UpdateModel)
Agoraquejátemosinforma çõesválidas,éhoradecolocaressesvaloresdentro
donossomodelo.Nonossoexemplo,omodeloéoobjetodotipo Pessoa,
eaexecu çãodafase4podeserentendidapelopseudocódigoaseguir.
HtmlInputText inputNome = ... // já convertido e validado
HtmlInputText inputIdade = ... // já convertido e validado
Pessoa pessoa = jsfAvaliaExpressionLanguage("#{pessoa}");
pessoa.setNome(inputNome.getValue());
pessoa.setIdade(inputIdade.getValue());
Como as ELs ligadas aos componentes eram#{pessoa.nome} e
#{pessoa.idade}, podemos perceber um padrão. Como nessa fase o
JSF está inserindo valores no modelo, e não recuperando, ele recupera
o objeto correspondente ao penúltimo nível da EL e chama o método
setdoúltimonível. Setivéssemosoobjeto FuncionarioligadoàEL
#{cadastroBean.cadastro.funcionario},oJSFrecuperariaoobjeto
cadastroqueépropriedadedo #{cadastroBean}echamariaométodo
setFuncionariodoobjeto cadastro.
Depoisdeterminadaessafase,temosnossomodelocomosvalorescor-
retos.Éoquepoderíamoschamarde“mundoperfeito”,ondeousuárioentra
com StringeoJSFnosentregaobjetosJavacomseustiposcorretoseval-
oresvalidados.
7.8 Fase5-I nvocar ação da aplicação (Invoke
Application)
Nessafaseacontecealógicadaaplica ção.Aquidentronãoprecisamosenão
devemosficarbuscandoobjetosbaseadosemalgum id,umavezqueissoé
responsabilidadedosconversores.Igualmente,nãodevemosficarvalidando
seumasenharespeitaotamanhomínimodecaracteresepossuiletrase
números,jáqueissodeveserfeitopelovalidador. Sevocêjáviuumpro-
jetoemJSFnoqualaa çãoiniciacom ifs,aprobabilidadedosrecursosdo
JSFestaremsendosubutilizadosémuitogrande.
156
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 173

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
Apesardapossibilidadedeconstruirmosvalidadorescustomizados,cos-
tumamosdeixarasvalida çõesdenegócio dentrodafase5,massomenteessas
deviamestaraqui.Vamosconsiderar,porexemplo,umsistemadeuniversi-
dade,emqueparaefetuarumamatrículaprecisamosverificarprimeirosenão
existemensalidadeemaberto,ousejánãoexisteumacordosendocumprido
emrela çãoàspossíveismensalidadesemaberto.Nessecasopoderíamoster
umtrechodecódigocomooseguinte.
public void efetuaMatricula(PropostaMatricula proposta){
try{
servicoFinanceiro.validaSituacaoAluno(proposta.getAluno());
// efetuaMatricula
} catch(MensalidadesEmAbertoException e){
// exibe mensagem para o usuário e aborta o a matrícula
}
}
Eagoraquerealizouaa ção,terminou,certo? Errado! Aindatemum
últimodetalheimportantíssimoporacontecer.
7.9 Fase6-R enderizar a resposta (Render Re-
sponse)
ChegamosàúltimafasedociclodevidadoJSF.Podemoschegaratéelade-
poisquetudoocorreubemnasoutrasfases,comoporexemplodepoisque
salvamosumregistrocomsucesso,oudepoisdeumerroemalgumafasein-
termediária.
Seocorrerumerrodeconversãoouvalida ção,asfases4e5sãopuladas
evamosdiretoparaafase6paramostrarnovamenteoformulárioparao
usuárioparaqueelepossacorrigir,jácomasdevidasmensagensdeerro.Ou
aindapodemoschegaraquilogodepoisdafase1,quandoousuáriopedea
páginapelaprimeiravez.NessecasooJSFmontaaárvoreejámandaafase
6,jáque,naprimeirarequisi çãoàaplica ção,nãohaveráformuláriosendo
submetidoenema çãoparaserinvocada.
157
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 174

7.9. Fase6-Renderizararesposta(RenderResponse) CasadoCódigo
Nessafaseaconteceagera çãodoHTMLapartirdaárvoredecompo-
nentesdoJSF.Vamosconsiderararenderiza çãodomesmotrechodecódigo
quevimosnafase1:
<h:form>
<h:inputText value="#{pessoa.nome}"/>
<h:inputText value="#{pessoa.idade}">
<f:validateRequired/>
</h:inputText>
</h:form>
Eaclasse Pessoa:
public class Pessoa {
private String nome;
private Integer idade;
//getters e setters
}
AcadatagqueoJSFpassa,elechamaorenderizadorcorrespondente.
ExistemrenderizadoresparacadacomponenteHTMLbásico,masbibliote-
casdecomponentescomoRichfacesePrimefacespodemsubstituí-los.Uma
utilidadedasubstitui çãodosrenderizadoreséqueessasbibliotecaspodemin-
cluir,porexemplo,regrasdeCSSprópriasdelas,semfor çarodesenvolvedor
acolocá-lasemtodososatributos.Assimcomoasbibliotecas,nóspodemos
tambémgerarnossaprópriaHTML.Sejaatravésdacria çãodenovoscompo-
nentesouimplementandonovosrenderizadores.
Paracadanódaárvore,oJSFmandarenderizaroiníciodatagedepois
seuscomponentesfilhos. Terminadososfilhos,ounãoexistindo,éfeitoo
fechamentodatag.Nocasodoscomponentesquepossuem Expression Lan-
guageligadaaeles,estaéavaliadaparaobteroobjetoJavacorrespondente.
Como está sendo gerada uma saída, ao avaliar a expressão
#{pessoa.nome}, uma instância depessoa será obtida e é nela que
ométodo getNomeseráchamado.
AssimqueoJSFtemoobjetoJava,elerecuperanovamenteoconversor
paraotipoadequadodainforma ção,paraquegerea Stringcorrespondente
158
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 175

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
aoobjeto,queseráexibidanatela.Casonãoexistaumconversor,oJSFapenas
chamaométodo toStringdoobjeto.
UmavisãogeraldociclodevidadoJSFpodeservistanafigura7.2.
Fig.7.2:CiclodevidadoJSF
7.10 Aja sobre as fases do JSF com os PhaseLis-
teners
VimosasseisfasesdoJSFearesponsabilidadedecadauma.Agoraveremos
comosolicitaraoJSFquenosnotifiqueacadamudan çadefase,atravésde
um PhaseListener.
Utilizamosum PhaseListenerpraticamentenasmesmassitua çõesem
queusaríamosum javax.servlet.Filter. Masemvezdeenvolvera
requisiçãointeira,seremosnotificadosantesedepoisdecadafase,oquefaz
comquetenhamosumacessomaisgranular. Comisso,podemosiraum
pontoespecíficodarequisi ção,casonosinteresse.
Umexemplodautiliza çãodo PhaseListeneréparaautenticação:
public class AutenticacaoPhaseListener implements PhaseListener{
private static final String RESTRICTION_PATTERN =
159
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 176

7.10. AjasobreasfasesdoJSFcomosPhaseListeners CasadoCódigo
"^/restrito/.*";
public PhaseId getPhaseId() {
return PhaseId.RESTORE_VIEW;
}
public void beforePhase(PhaseEvent event) {
}
public void afterPhase(PhaseEvent event) {
FacesContext context = event.getFacesContext();
String viewId = context.getViewRoot().getViewId();
boolean urlProtegida =
Pattern.matches(RESTRICTION_PATTERN, viewId);
Object usuario = context.getExternalContext()
.getSessionMap().get("usuarioLogado");
if(urlProtegida && usuario == null){
NavigationHandler navigator = context
.getApplication()
.getNavigationHandler();
navigator.handleNavigation(context, null, "login");
}
}
}
Esseéapenasumexemplodecódigodeautentica ção,masomaisim-
portanteéanalisarmosofuncionamentodo PhaseListener.Oprimeiro
método, getPhaseId()devolvequalfasedoJSFnosso listeneriráescutar.
Oupodemosdevolver PhaseId.ANY_PHASEparaindicarquequeremosser
notificadosantesedepoisdetodasasfases.
Diferente de um javax.servlet.Filter, não temos um único
métodoqueenvolvetodaafase. Emvezdisso, temosummétodoqueé
chamadoantesdoprocessamentodafase, beforePhase, eoutroqueé
chamadodepois, afterPhase. Nonossoexemplo,utilizamossomenteo
segundométodo,porqueantesdafase Restore Viewaindanãoépossívelre-
160
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 177

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
cuperarqualtelaestásendorequisitada.
Paraqueocódigodo PhaseListenerfuncione,precisamosdeuma
regradenavega çãoglobalquesaibairparaateladelogin,apartirdo outcome
login.Tambémdevemosregistrá-lono faces-config.xml,queacabaria
ficandocomumconteúdoparecidocomoseguinte:
<navigation-rule>
<navigation-case>
<from-outcome>login</from-outcome>
<to-view-id>/login.xhtml</to-view-id>
</navigation-case>
</navigation-rule>
<lifecycle>
<phase-listener>
facesmotors.AutenticacaoPhaseListener
</phase-listener>
</lifecycle>
Émuitoimportantequeateladeloginnãoestejacontidanaexpressão
regularquerestringeaspáginasdaaplica ção,senãoteremosum loopderedi-
recionamentos.
7.11 Conheça os componentes do JSF
Umaquestãointeressanteemrela çãoatodososcomponentesdoJSFéque,
apesardegeraremHTML,temosduaspropriedadespresentesempratica-
mentetodososcomponentes,oquenospermitecustomizarovisualdatela
apartirdefolhadeestilos.Essaspropriedadessão stylee styleClass.
AprimeiraaceitaconteúdoCSS,queserácolocadodentrodapropriedade
styledoHTMLgerado. Asegundarenderizaapropriedade classno
HTMLgeradoeacabasendomuitasvezesmaisusada,porqueéumaboa
práticacolocarclassesdeCSSnoHTML,enãooestilopropriamentedito.
<h:inputText style="padding: 10px;"
styleClass="valor_numerico" />
SãodiversoscomponentesdisponíveisnoJSF,algunsmaissimples,outros
maiscomplexos.Vamosaprendê-los.
161
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 178

7.12. h:form CasadoCódigo
7.12 h:form
<h:form>
</h:form>
Atag h:formgeralmenteéusadasemnenhumapropriedade,jáqueno
JSFnãoprecisamosespecificarnenhuma action,comoénormalfazerem
frameworksbaseadoema ções.Afinal,ainforma çãodoqueseráfeitoquando
apáginaforsubmetidaestánoprópriocomponentequefaráasubmissãodas
informações,comoo h:commandButton.
Quandoespecificamosalgumapropriedade,essageralmenteéo id.Pre-
cisamosdissoquandovamosmanipulardiretamenteoselementos,comopor
exemploparatrabalharmoscomAJAX.
Outracaracterísticaimportantecomrela çãoa iddecomponentesé
quandotemosoutroscomponentesdentrodoformulário.
<h:form id="formulario">
Idade: <h:inputText id="campo_idade"/>
</h:form>
Com esse código, o HTML gerado terá o formulário comid
formulario,porémo inputTextteráid formulario:campo_idade.
Reparequeo iddoformuláriofoiadicionadoaoiníciodocomponentefilho,
o inputText.Essecomportamentoéoquechamamosde naming container
epodemosdesabilitá-lopormeiodoatributo prependId,deixando-ocomo
false.
<h:form id="formulario" prependId="false">
Idade: <h:inputText id="campo_idade"/>
</h:form>
Pronto,dessavez,noHTMLgerado,o inputTextteráum idsomente
comovalor campo_idade. Oresultadodocódigononavegadorseráo
seguinte:
162
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 179

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
Fig.7.3:Resultadodatagh:inputText
7.13 h:inputText e h:inputTextarea
<h:inputText value="#{managedBean.objeto.descricao}"/>
Descrição:
<h:inputTextarea value="#{managedBean.objeto.descricao}"/>
Essesdoiscomponentespossuemumaapresenta çãovisualdiferentemas
sãopraticamenteiguais.Adiferen çaentreeleséqueo h:inputTextarea
possuiaspropriedades rows,queespecificaaquantidadedelinhas,e cols,
queespecificaaquantidadedecolunasqueocampoiráapresentar. Jáo
h:inputText tem as propriedadessize, que serve para especificar o
tamanhodocampobaseadonaquantidadedecaracteres,algoparecidocomo
colsdo h:inputTextarea;eapropriedade maxlength,queespecifica
aquantidademáximadecaracteresqueocampoaceita.
Depoisquevimosasdiferen ças,vamostratarambosapenascomo“in-
put”.NoJSF,pormaisquetenhamosdiversasformadeapresentaroselemen-
tosnatela,quasetodososcomponentessãoinputs. Umcombo,umselect,
umcheckboxouradiobuttonsãoformasdiferentesdeapresentarinputsao
usuário.
Aprincipalpropriedadedequalquerinputéa value.Aela,nósligamos
uma Expression Languageque,depoisdeconversãoevalida ção,permitiráao
JSFcolocarovalorqueousuáriodigitounocampo,diretamentedentroda
propriedadeespecificada.
Fig.7.4:Resultadodotagh:inputTextarea
163
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 180

7.14. h:inputSecret CasadoCódigo
7.14 h:inputSecret
Senha: <h:inputSecret value="#{managedBean.usuario.senha}"/>
O h:inputSecret gera o HTML equivalente a um input
type="password",mostrandooconteúdodigitadodeumamaneiraque
nãoseconsigavisualizaroconteúdo,normalmentemostrando*(asteriscos)
nolugardotexto.
Fig.7.5:Resultadodatagh:inputSecret
7.15 h:inputHidden
<h:inputHidden value="#{managedBean.objeto.id}"/>
Esse componente se comporta quase que exatamente como um
h:inputText,comadiferen çadeficarocultodousuário.Dessaforma,não
existeumresultadovisualparailustrarmos.
7.16 h:selectOneMenu, f:selectItem e
f:selectItems
Marca:
<h:selectOneMenu value="#{modeloBean.modelo.marca}">
<f:selectItem itemLabel="-- Selecione --"
noSelectionOption="true"/>
<f:selectItems value="#{marcaBean.marcas}" var="marca"
itemValue="#{marca}" itemLabel="#{marca.nome}"/>
</h:selectOneMenu>
Apesardeparecermaiscomplexo,um h:selectOneMenunadamaisé
doqueuminputquejátrazparaousuárioop çõespré-definidas.Porexemplo,
ousuárioprecisaescolherqualéa marcadocarroqueelequerpesquisar.Em
vezdedeixarmosqueeledigiteessainforma çãoepossivelmentecometaerro
164
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 181

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
dedigita ção,podemoslistarasop çõesdisponíveisparaele,assimépossível
escolher.
Essasop çõespodemserumacombina çãodeitensestáticos,comoodo
f:selectItem,comdinâmicos,comoodo f:selectItems.Geralmente
oprimeiroéusadoapenasparaumamensageminstruindoousuárioasele-
cionarumvalor.Semisso,aprimeiraop çãodocomboviriaselecionada,enão
teríamoscomosaberseousuárioescolheuaquelaop çãoousimplesmentese
esqueceudeselecionar.
Alistagemdinâmicageralmentevemdealgum Managed Beanquepos-
suaessalistagem.Noexemplo, marcaBeanjásepossuinaturalmenteessa
listagem,entãobuscamosdelá. Oimportanteanotarmoséaestruturado
f:selectItems,queumavezentendidaficarásimplesebempráticousar
qualquertipodeselect.
O f:selectItemspossuiumapropriedade valuequeligaocom-
ponentecomalistadevaloresqueelevailistar. Comisso,definimosuma
variávelparapodermosacessardedentrodaspropriedades itemValuee
itemLabel.
O itemValuedo f:selectItemsespecificaqualvalorseráatribuído
ao valuedo h:selectOneMenu.Reparequeno valuedocombotemos
a Marcado Modeloqueestásendoeditado,eo itemValueespecificaque
aoselecionarumitemdocomboovaloratribuídoseráuma Marca. Jáa
propriedade itemLabelserveparaespecificarmosoqueapareceráparao
usuário.
Fig.7.6:Resultadodatagh:selectOneMenu
7.17 h:selectOneRadio
Marca:
<h:selectOneRadio value="#{modeloBean.modelo.marca}">
165
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 182

7.18. h:selectOneListbox CasadoCódigo
<f:selectItems value="#{marcaBean.marcas}" var="marca"
itemValue="#{marca}" itemLabel="#{marca.nome}" />
</h:selectOneRadio>
Um h:selectOneRadio é praticamente igual a um
h:selectOneMenu. Primeiro como podemos perceber, os dois ini-
ciamseunomecom selectOne,ouseja,nosdoiscasosousuáriopoderá
selecionarapenasumelemento,porémaexibi çãoserápor radio button.
Outradiferen çaestáemcomocadacomponenteéapresentadoparao
usuário.Nocasodo h:selectOneRadio,podemosespecificarumpouco
maiscomoseráessaapresenta çãoatravésdapropriedade layout,quepor
padrãotemovalor lineDirection.Comessevalorasop çõesserãoapre-
sentadasumanafrentedaoutra.Oupodemosespecificar pageDirection,
enessecasoasop çõesserãoapresentadasumaabaixodaoutra.
Fig.7.7:Resultadodatagh:selectOneRadiocomlayoutlineDirection
Fig.7.8:Resultadodatagh:selectOneRadiocomlayoutpageDirection
7.18 h:selectOneListbox
Marca:
<h:selectOneListbox value="#{modeloBean.modelo.marca}" size="5">
<f:selectItems value="#{marcaBean.marcas}" var="marca"
itemValue="#{marca}" itemLabel="#{marca.nome}" />
</h:selectOneListbox>
166
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 183

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
Outro componente da família dosselectOne: a diferença desse
componente para um combo (h:selectOneMenu) é que o combo
mostraapenasumalinha, eprecisamosclicarparaabrirasop ções. Jáo
h:selectOneListboxjátrazasop çõesvisíveis,bastandoousuáriosele-
cionaroquedesejar. Casoqueiramoslimitarotamanhodalista,quepor
padrãomostratodososelementos,podemosutilizarapropriedade size.
Então,casotenhamosmaiselementosdoqueoquepodeserapresentado,
seráexibidaumabarraderolagemnocomponente.
Fig.7.9:Resultadodatagh:selectOneListbox
7.19 h:selectManyMenu e h:selectManyListbox
<h:selectManyMenu value="#{automovelBean.automovel.acessorios}">
<f:selectItems value="#{acessorioBean.acessorios}"
var="acessorio" itemValue="#{acessorio}"
itemLabel="#{acessorio.descricao}" />
</h:selectManyMenu>
Marca:
<h:selectManyListbox
value="#{automovelBean.automovel.acessorios}" size="5">
<f:selectItems value="#{acessorioBean.acessorios}"
var="acessorio" itemValue="#{acessorio}"
itemLabel="#{acessorio.descricao}" />
</h:selectManyListbox>
Apesardeestarmosentrandonafamíliados selectMany,adinâmica
doscomponentescontinuaamesma.Agorao valuedocomponenteguarda
umalistaenãomaisumúnicoobjeto.Ousodo f:selectItemsnoentanto,
167
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 184

7.20. h:selectManyCheckbox CasadoCódigo
continuainalterado.Assim,o itemValuecontinuarepresentandoumob-
jetoselecionadodetipocompatívelcomo valuedo selectemqueeleestá
inserido,eagoraeleédeumtipocompatívelcomoselementosdo value.
Emnossoexemplo,o valuedo selectéumalistadeacessóriosecada
elementodo f:selectItemséumacessórioquepodeserinseridonessa
lista.
Com rela ção aos componentes h:selectManyMenu e
h:selectManyListbox, a diferença entre eles é apenas a presença
dapropriedade sizenocomponente h:selectManyListbox,enquanto
ocomponente h:selectManyMenutemtamanhofixadoemumaúnica
linha.
Fig.7.10:Resultadodatagh:selectManyListbox
7.20 h:selectManyCheckbox
Acessórios:
<h:selectManyCheckbox
value="#{automovelBean.automovel.acessorios}">
<f:selectItems value="#{acessorioBean.acessorios}"
var="acessorio" itemValue="#{acessorio}"
itemLabel="#{acessorio.descricao}" />
</h:selectManyCheckbox>
Éaversão“many”docomponenteh:selectOneRadio,mostrando
checkboxesparaasele çãodousuário. Eletambémpossuiumapropriedade
chamada layoutqueporpadrãotemvalor lineDirectionemostraos
itensselecionáveisumaoladodooutro. Podemostambémmudarovalor
dapropriedadepara pageDirectionemostrá-losumabaixodooutro.
Excetuando-seisso,ocomportamentodocomponenteéomesmodoscom-
ponentes selectManyvistosanteriormente.
168
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 185

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
Fig.7.11:Resultadodatagh:selectManyCheckboxcomlayoutlineDirection
Fig.7.12:Resultadodatagh:selectManyCheckboxcomlayoutpageDirection
7.21 h:selectBooleanCheckbox
Usuário inativo:
<h:selectBooleanCheckbox
value="#{usuarioBean.usuario.inativo}"/>
Não podemos confundir esse componente com o
h:selectManyCheckbox. Apesar de ambos serem checkboxes, são
completamente diferentes. Como seu próprio nome sugere, usamos o
h:selectBooleanCheckboxligadocompropriedadesbooleanas. Como
podemosvernoexemplo,usamosessecomponenteparaalterarpropriedades
dosnossosobjetosdemodelo,comomudarostatusdeumusuárioenquanto
oeditamos.
Fig.7.13:Resultadodatagh:selectBooleanCheckbox
Podemostambémusarocomponentepara,alémdealterarapropriedade
deumobjeto,ativarounãoaexibi çãodeoutroscomponentes.
169
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 186

7.22. NovidadedoJSF2.2:h:inputFile CasadoCódigo
<h:selectBooleanCheckbox
value="#{compraBean.compra.temDesconto}">
<f:ajax render="desconto"/>
</h:selectBooleanCheckbox> Compra com desconto
<h:panelGroup id="desconto">
<h:panelGroup rendered="#{compraBean.compra.temDesconto}">
% desconto <h:inputText
value="#{compraBean.compra.desconto}"/>
</h:panelGroup>
</h:panelGroup>
7.22 Novidade doJSF2.2: h:inputFile
<h:form enctype="multipart/form-data">
Imagem: <h:inputFile value="#{automovelBean.uploadedFile}"/>
<h:commandButton value="Salvar"
action="#{automovelBean.salvar}"/>
</h:form>
EocódigoJavapararecebero uploaddoarquivo.
public void class AutomovelBean {
private javax.servlet.http.Part uploadedFile;
private Automovel automovel;
// getters e setters
public void salvar(){
try {
InputStream is = uploadedFile.getInputStream();
byte[] bytes = IOUtils.toByteArray(is);
automovel.setImagem(bytes);
em.persist(automovel);
} catch (IOException e) {
// tratar exceção
}
}
}
170
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 187

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
EsseéumcomponentenovodoJSF2.2.Atéaversãoanterior,pararealizar
uploaddearquivoeranecessárioutilizarcomponentedebibliotecascomoo
Primefaces.
Como podemos ver no exemplo, ligamos o value do
componente h:inputFile diretamente no objeto do tipo
javax.servlet.http.Part, novo na API de Servlet 3.0. A partir
desseobjetoconseguimosacessaro InputStreamdoarquivoenviadopelo
usuário.
Recuperamosentãoo byte[]apartirdo InputStreameoguardamos
napropriedade imagemdo Automovel,queéarmazenadanobancode
dadoscomoum @LobdaJPA.
Fig.7.14:Resultadodatagh:inputFile
7.23 h:panelGrid
<h:panelGrid columns="2">
Marca: <h:outputText value="#{automovel.modelo.marca}"/>
Modelo: <h:outputText value="#{automovel.modelo}"/>
Ano Fabr.: <h:outputText value="#{automovel.anoFabricacao}"/>
Ano Modelo: <h:outputText value="#{automovel.anoModelo}"/>
Km: <h:outputText value="#{automovel.kilometragem}"/>
</h:panelGrid>
Um h:panelGrid renderiza uma tabela cujo número de colunas
é definido pela propriedadecolumns. No exemplo, informamos que
queríamosduascolunas,entãoacadadoiscomponenteso h:panelGrid
criaumanovalinha. Avantagememusarocomponenteemvezdefazer
umatabelaéquepodemosparametrizaronúmerodecolunas,podendopor
exemploemvezdeduas,mostrarquatrocolunassemmudan çasnocódigo.
Assimcomoqualquercomponente container,ouseja,queenvolve
outroscomponentes,o h:panelGridnospermitemanipulartodososcom-
171
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 188

7.24. h:panelGroup CasadoCódigo
ponentesqueestãodentrodelecomoumsó.Sequisermosporexemploren-
derizarviaAJAXtodooconteúdodo container,nãoprecisamospassaro
iddecadacomponente,bastapassaro iddo container.Vamosvertudo
issocommaiscalmanase ção9.4,ondefalaremossobrecomofazerrequi-
siçõesassíncronascomoJSF.
7.24 h:panelGroup
<h:selectBooleanCheckbox
value="#{compraBean.compra.temDesconto}">
<f:ajax render="desconto"/>
</h:selectBooleanCheckbox> Compra com desconto
<h:panelGroup id="desconto">
<h:panelGroup rendered="#{compraBean.compra.temDesconto}">
% desconto<h:inputText
value="#{compraBean.compra.desconto}"/>
</h:panelGroup>
</h:panelGroup>
O h:panelGroupéumcontainerqueservesomenteparaagruparoutros
componentes.Assim,podemosrenderizarounãoeatualizartodooconteúdo
apartirdeumsócomponente.
Oexemploapresentadoéomesmo quevimosquandofalávamosdo
componente h:selectBooleanCheckbox. Nelepodemosvercomoo
h:panelGroupéusadoparaseratualizadoviaAJAXatravésdoseu idcom
valor "desconto".Vemostambémcomopodemoscondicionararender-
izaçãodetodooconteúdodeoutro h:panelGroupatravésdapropriedade
rendered.
7.25 h:output Text
Marca: <h:outputText value="#{automovel.modelo.marca}"/>
Modelo: <h:outputText value="#{automovel.modelo}"/>
Nemsempreutilizamosocomponente h:outputTextparaescreveral-
gumasaídananossaaplica ção,jáquepodemosescreverdiretamenteotexto
172
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 189

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
quedesejamos,mesmoquenelehajaconteúdodinâmico. Paraisso,basta
colocaraexpressãoquequisermos. Porexemplo,poderíamosreescrevero
exemploacimadaseguinteforma:
Marca: #{automovel.modelo.marca}
Modelo: #{automovel.modelo}
Ofuncionamentoéomesmo.ColocarotextodiretamentenãofazoJSF
trabalharerradoouseperder.Masenquantonoprimeiroexemplotínhamos
quatrocomponentes(asduas labelssãocomponentesimplícitos),nesseúl-
timotemosapenasum.Comojávimosofuncionamentodo h:panelGrid,
sabemosqueemalgunsmomentosonúmerodecomponentesinfluenciano
resultadofinal,eesseéummotivoparaousodo h:outputText.
Outromotivoparausarmoso h:outputTextéapossibilidadedeusá-lo
emconjuntocomconversores.Comoostextoscomuns(outputsimplícitos)
nãosãotags,nãotemoscomocolocarumconversornele. Epodemosusar
conversoresqueapresentemcorretamentevaloresmonetáriosoupercentuais,
porexemplo.
Fig.7.15:Resultadodatagh:outputText
Preço:
<h:outputText value="#{automovel.preco}">
<f:convertNumber type="currency" />
</h:outputText>
Usandoesseconversor,baseadonaconfigura çãodoseubrowser,oJSF
iráapresentaronúmeroarmazenadonapropriedade precoemReaisou,
dependendodalocaliza ção,poderiaapresentaremDólares.Porexemplo,o
Float 1000000.0 seriaapresentadoassim:“R$1.000.000,00”.
Outrousoparaocomponenteéapossibilidadedeespecificarmosclasses
deCSSassimcomopodemosfazeremqualqueroutrocomponenteJSF.Sem
ocomponente,precisaríamos,porexemplo,envolvermanualmenteotexto
emumHTML span.
173
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 190

7.26. h:outputLabel CasadoCódigo
7.26 h:output Label
<h:outputLabel value="Ano de Fabricação:" for="anoFabricacao"/>
<h:inputText value="#{automovel.anoFabricacao}"
id="anoFabricacao"/>
<h:outputLabel value="Ano do Modelo:" for="anoModelo"/>
<h:inputText value="#{automovel.anoModelo}" id="anoModelo"/>
Noentanto,aousarmoso h:outputLabeltemosumasemânticacor-
retacomrela çãoaos labelsdoscampos,jáque,emvezdeumsimplestexto,a
tag h:outputLabeldoJSFrenderizaatag labeldoHTML.Seuatributo
forreferenciao iddo inputaoqualeleserefere.
7.27 h:output Format
<h:outputFormat value="Eu moro em {0}, {1}" >
<f:param value="Campo Grande" />
<f:param value="MS" />
</h:outputFormat>
Usamosocomponente h:outputFormatquandoqueremosmontar
textosparametrizados.
Seusvalorespodemvirdeuma Expression Language.Vamosanalisarum
exemploumpoucomaiscomplexo.
<h:outputFormat value="#{preferenciasBean.bemVindo}" >
<f:param value="#{session.usuarioLogado.nome}" />
<f:param value="#{session.usuarioLogado.tratamento}" />
<f:param value="#{session.usuarioLogado.cargo}" />
<f:param value="#{session.localidadeSelecionada}" />
</h:outputFormat>
7.28 h:output Script e h:output Stylesheet
<h:outputStylesheet library="css" name="facesmotors.css"/>
<h:outputScript library="scripts" name="facesmotors-commons.js"
target="head"/>
174
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 191

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
EssesdoiscomponentesutilizamomecanismopadrãodoJSFdelidar
comrecursoscomojavascripts,folhasdeestiloCSS,imagenseatémesmo
paraacria çãodecomponentescustomizados.Varemosmaisdetalhessobre
essesuportenase ção7.34.
Aadi çãodessescomponentepermitequetambémadicionemosnossos
recursos,sejaCSSoujavascript,emqualquerlugardapágina,enoHTML
renderizadoelesestarãoondequisermos.Porexemplo,osarquivosCSSrela-
cionadoscomocomponente h:outputStylesheetestarãosempreno
headdoHTML.
Jáo h:outputScriptpossuiapropriedade targetquenospermite
indicarondequeremosqueoscriptsejacarregado. Senãoespecificarmos
nada,eleserácarregadonomesmolocalondeo h:outputScriptfoicolo-
cadonapágina,noentanto,podemosdeterminarosvalores: head, bodye
formparaindicarondequeremosqueelefique.
7.29 h:graphicImage
<h:graphicImage url="www.servidor.com/imagem.jpg"/>
<h:graphicImage library="images" name="imagem.jpg"/>
Usamos h:graphicImageparaexibirimagensnanossaaplica ção.Ba-
sicamentetemosdoismodos, comopudemosvernocódigoanterior. O
primeiroéusadoparaexibirumaimagembaseadaemsua url,easegunda
usamosparaexibirimagensdedentrodanossaaplica ção.
Oprimeiromodoapenasrenderizaatag imgdoHTMLcomapro-
priedade srccomomesmovalorpassadona urldo h:graphicImage.
Osegundomodoémaisinteressanteeusaomesmosuportearecursos
queastags h:outputScripte h:outputStylesheet. Apropriedade
libraryespecificaodiretórioea nameéonomedoarquivodentroda
pasta.Avantagemdesserecursoéquenãoprecisamosficarnospreocupando
emmontaro linkrelativodaimagemepodemosinclusivereferenciarimagens
queestãodentrodearquivos jar.Veremosmaissobreosuportearecursos
nase ção7.34.
175
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 192

7.30. h:dataTable CasadoCódigo
7.30 h:dataTable
<h:dataTable value="#{automovelBean.automoveis}" var="auto"
rowClasses="table-linha-par,table-linha-impar" border="1">
<h:column>
<f:facet name="header">Marca</f:facet>
#{auto.modelo.marca}
</h:column>
<h:column>
<f:facet name="header">Modelo</f:facet>
#{auto.modelo}
</h:column>
<h:column>
<f:facet name="header">Ano Fabricação</f:facet>
#{auto.anoFabricacao}
</h:column>
<h:column>
<f:facet name="header">Ano Modelo</f:facet>
#{auto.anoModelo}
</h:column>
</h:dataTable>
Utilizamos h:dataTablequandodesejamosmostrardadostabulares.
Temosduaspropriedadesprincipais, valuee var,bemparecidocomo
componente f:selectItems.Napropriedade valueligamosalistaque
queremositerar,ena vardefinimosumnomedevariávelqueusaremospara
referenciarcadaobjetodalista.
Dentro da h:dataTable nós definimos as colunas usando a tag
h:column,edentrodestapodemosdefinirumcabe çalhopelo f:facet
“header”,eumrodapécomof:facet“footer”.
Temostambémpropriedadescomo headerClasse footerClass
para especificarmos as classes CSS do cabeçalho e do rodapé, respecti-
vamente. Além dessas, como podemos ver no exemplo, temos ainda a
propriedade rowClassesquepermitefazer zebramentodaslinhas, uti-
lizando um estilo CSS para cada linha da tabela; e temos a propriedade
columnClassesquefazomesmoparaascolunas.
176
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 193

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
Fig.7.16:Resultadodatagh:dataTable
7.31 ui:repeat
<ui:repeat value="#{automovelBean.automoveis}" var="auto"
varStatus="status">
<motors:automovel automovel="#{auto}"/>
</ui:repeat>
Atag ui:repeattambéméusadaparaiterarelementos,masemvezde
renderizarumatabela,elasimplesmentepercorrealista,deixando-noslivres
paraescolherotipodesaídaquedesejamos.
Alémdastradicionaispropriedades valuee varquefuncionamigual
as da h:dataTable, a ui:repeat nos permite, com a propriedade
varStatus,definirumavariávelrelacionadaaostatusdaitera ção.Nonosso
exemplo,definimosavariável status,eatravésdelapodemosfazer,dentre
outrascoisas,asseguinteschecagens:
•#{status.first}:ébooleanoeindicaseéoprimeiroelementoda
lista;
•#{status.last}:ébooleanoeindicaseéoúltimoelementodalista;
•#{status.index}: dotipointeiroquerepresentaoíndicedaiter-
ação.Sefosseum fortradicional,seriao int i;
•#{status.even}:ébooleanoeindicaseo indexépar;
•#{status.odd}:ébooleanoeindicaseo indexéimpar.
177
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 194

7.32. h:commandButtoneh:commandLink CasadoCódigo
Parautilizaressatag,énecessárioimportaroscomponentesdisponíveis
doFacelets.Paraisso,ésóadicionarnocome çodoseu xhtmloseguinte:
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core"
xmlns:ui="http://java.sun.com/jsf/facelets">
</html>
7.32 h:command Button e h :command Link
<h:dataTable value="#{automovelBean.automoveis}"
var="automovel">
<h:commandLink value="Editar" action="editar">
<f:setPropertyActionListener value="#{automovel}"
target="#{automovelBean.automovel}"/>
</h:commandLink>
</h:dataTable>
<h:commandButton value="Salvar"
action="#{automovelBean.salvar(automovel)}"/>
Fig.7.17:Resultadodatagh:commandLink
Fig.7.18:Resultadodatagh:commandButton
Adiferen çabásicaentre h:commandButtonse h:commandLinksé
basicamente a forma como são renderizados. Fora isso, o que se aplica
178
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 195

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
aumseaplicatambémaooutro. Noexemploacima,poderíamostrocar
os componentes de lugar sem influenciar no funcionamento. Apesar do
h:commandLinkrenderizarumlink,elefaráo submitdoformulárioemque
estiverem.
Ambososcomponentes commandpossuemumapropriedade action
queemúltimainstânciaéuma String.Essa Stringpodeserliteralcomo
noexemplodolink,oupodeseroretornodométodoinvocadodo Managed
Bean. A Stringresultanteéusadaparaefetuaranavega ção,queveremos
nase ção7.41.
No h:commandLink, simplesmentecolocamosoobjetodecontexto
da h:dataTable na propriedade automovel do automovelBean.
Na prática, ele pegará oAutomovel que estava sendo apresentado
na linha do link que foi acionado e colocará onde otarget do
f:setPropertyActionListeneraponta.Então,efetuaráaregradenave-
gaçãobaseadana String“editar”.
Jánoexemplodobotão,ligamosoatributo actioncomaexecu çãode
ummétodo.Apósefetuararegradenegócio,essa actionvaidevolveralgo
queseráusadoparaatomadadedecisãodanavega ção,damesmaformacomo
nocasodolink.Adiferen çaéqueoretornopodeseruma String, null,um
método voidouaindaretornarum Objectqualquer,queteráseumétodo
toStringchamadoparaaobten çãodoresultadoparaanavega ção.
7.33 Adiferença entre Action eActionListener
<h:commandButton id="botaoSalvar" value="Salvar"
actionListener="#{automovelBean.listener}"
action="#{automovelBean.salvar(automovel)}"/>
Apesardeaparentementeparecidos, actione actionListenersão
conceitualmentebemdiferentes.Enquantooprimeiroéusadoparaexecutar
alógicadaaplica ção,osegundoserveparaobservarmoseventosdetela.Seria
comoficarescutandoasa çõesdousuário,massemobjetivodenegócio.
Como está apresentado no código, umactionListener deve ser
um método público evoid do objeto #{automovelBean}, mas
temos a opção de não termos nenhum parâmetro ou de receber um
179
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 196

7.33. AdiferençaentreActioneActionListener CasadoCódigo
javax.faces.event.ActionEvent.Esseúltimocasogeralmenteémais
interessante,porqueapartirdesseobjetotemosacessoaocomponenteque
originouaa ção,quenoexemploéobotãorotulado“Salvar”.
public void listener(ActionEvent event){
UIComponent source = event.getComponent();
System.out.println("Ação executada no componente "
+ source.getId());
}
Aoexecutaraa çãodesalvar,a actionListenerescreverianoconsole
o iddocomponente,quenocasoé botaoSalvar. Existetambémuma
outraformadeassociaruma ActionListenercomaa ção,atravésdatag
f:actionListener.
<h:commandButton id="botaoSalvar" value="Salvar"
action="#{automovelBean.salvar(automovel)}">
<f:actionListener type="facesmotors.LoggerActionListener"/>
<f:actionListener type="..."/>
</h:commandButton>
Nessecaso,estamosvinculandonossaa çãocomclassesqueimplementam
ainterface ActionListener. Umamesmaa çãopodetervários listeners,
massóconseguimosfazerissocomatag f:actionListener,jáqueapro-
priedade actionListenerdo h:commandButtone h:commandLink
sópermitevincularummétodo.Seespecificarmosmaisdeum listener,eles
serãoexecutadosnaordemqueinformarmos.
Aseguirtemosumexemplode ActionListener.
public class LoggerActionListener implements ActionListener{
@Override
public void processAction(ActionEvent event)
throws AbortProcessingException {
UIComponent source = event.getComponent();
System.out.println("Ação executada no componente "
+ source.getId());
180
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 197

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
}
}
Note a possibilidade de abortarmos a execução da ação principal,
quenocasoésalvaro Automovel, bastandoparaissolan çarmosuma
AbortProcessingException.Issotornapossível,porexemplo,verificar
seousuáriotemounãopermissãoparaexecutarumadeterminadaopera ção.
Agoradepoisdevermosas ActionListeners,podemoscompreender
melhorofuncionamentodatag f:setPropertyActionListener. Ela
adicionananossaa çãouma ActionListenerquecopiaumobjetodeum
local( value)paraoutro( target).
7.34 Padronização no carregamento de recur -
sos
Nodesenvolvimentowebemgeralprecisamoslidarcomcarregamentode
recursos como imagens, arquivos javascript, CSS e outros. Geralmente
guardamostodoselesemalgumapastaeos linkamosquandonecessário.
Masoqueacontecequandoprecisamoscomponentizaralgo? Porexemplo,
quandovamosdeixarprontodentrodeum jar,umateladeloginpadrão,
quealémdoscamposdeusuárioesenhapossuiumaimagem,comoacarreg-
amos?
Atépoucotempoatrás,paralidarmoscomrecursosdentrodearquivos
jar,eranecessárioousodeuma Servletquefizesseotrabalhopornós.Como
suportearecursosdoJSF,podemosusaramesmamaneiradecarregarrecur-
sosdedentrodaaplica çãooudedentrodeumjar.Podemosaindaversionar
umdeterminadorecurso,comoabibliotecadojQuery,porexemplo.
181
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 198

7.34. Padronizaçãonocarregamentoderecursos CasadoCódigo
Fig.7.19:Aestruturadosrecursosdentrodoprojetoounojaréigual
Abasedetudoéapasta resources,quepodetantoestarnaraizdo
contextowebquantonapasta META-INFdentrodeumjarouno classpath
daaplica ção.
Temos basicamente três componentes básicos do JSF que lidam
com recursos que são h:outputScript, h:outputStylesheet e
h:graphicImage.
Em comum nesses três componentes temos basicamente duas pro-
priedades: librarye name.
<h:outputScript library="scripts" name="facesmotors.js"/>
ParaoJSF, libraryéapastaabaixodapasta resources.Conforme
aimagemqueacabamosdever,temosbasicamentetrêsbibliotecasnanossa
aplicação: images, scriptse css. Jáapropriedade nameservepara
especificaronomedorecursoqueestádentroda library.
Essaéamaneiramaissimplesenaturaldesetrabalharcomosrecursos,
noentanto,podemosiralémetrabalharmosdeumamaneiramaiscomplexa.
Paraentendermosoquepodemosfazer,vamosdarumaolhadanonomeque
podemosterparaosrecursos:
[localePrefix/][libraryName/][libraryVersion/]resourceName[/resourceVersion]
182
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 199

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
Podemos ter desde a versão internacionalizada de um recurso (
localePrefix),atéespecificarmosversões,tantodabibliotecacomodore-
curso.
Então,seestivéssemosdesenvolvendoumabibliotecadecomponentes
chamada“facesmotors”,poderíamosfazeralgoparecidocomisso:
Fig.7.20:Jarscomversõesdiferentesdomesmoscript
Agora,temosduasversõesdeumamesmabiblioteca,masbastaespecifi-
carmosqueversãoqueremoscarregaraousarqualquerumdoscomponentes
comsuportearecursos.
<h:outputScript library="facesmotors/1_0"
name="facesmotors-scripts.js"/>
<h:outputScript library="facesmotors/1_1"
name="facesmotors-scripts.js"/>
Asversõessãoespecificadasusando _comoseparadordosnúmeros.
Alémdisso,podemosusaruma Expression Languageparacarregarrecursos
mesmoondenãoestivermosusandoalgumcomponentecomessetipodesu-
porte:
<script type="text/javascript"
src="#{resource['facesmotors/1_1:facesmotors-scripts.js']}">
</script>
183
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 200

7.35. Entendaosconversoresnativos,of:convertDateTimeeof:convertNumber CasadoCódigo
7.35 Entenda os conversores nativos , o
f:convert DateTime e o f:convert Number
OJSFpossuiconversoresnativosparatransformaras Stringsrecebidasna
requisiçãodaaplica çãoparaostiposbásicoscomo Integer, Floatealguns
outros.Comoseufuncionamentoétrivial,ouseja,ébasicamenteumasim-
plesconversãopara String,essase çãotemcomoobjetivotratarosconver-
soresquejáexistem,masque,diferentementedosconversorespara Integer
ou Float,precisamdealgumtipodeconfigura çãoextra.
Basicamente temos dois conversores nessa situa ção:
f:convertDateTime e f:convertNumber. Datas e números po-
dem ser informados ou apresentados de diversas formas, e por isso os
usamos,parapoderindicaroformatoquequeremosusaremcadasitua ção.
f:convertDateTime
<h:inputText value="#{managedBean.objeto.data}">
<f:convertDateTime pattern="dd/MM/yyyy"/>
</h:inputText>
<h:outputText value="#{managedBean.objeto.data}">
<f:convertDateTime dateStyle="full" type="both"/>
</h:outputText>
O uso mais comum desse conversor é a partir da sua propriedade
pattern,naqualinserimosopadrãodadataquequeremosinformarou
exibir. Mascasonãoqueiramosdeixaropadrãofixo,podemosutilizaras
propriedadesaseguir:
dateStyle
Podeassumirosseguintesvalorescomosrespectivosresultados:
•default(valorpadrão):21/12/2012
•short:21/12/12
•medium:21/12/2012
184
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 201

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
•long:21deDezembrode2012
•full:Sexta-feira,21deDezembrode2012
type
Apropriedade typepermiteconfigurarsequeremostrabalharsomente
comdata,hora,ouambos:
•date(valorpadrão):21/12/2012
•time:23:59:59
•both:21/12/201223:59:59
locale
Podemos informar a localidade. Deve ser uma instância de
java.util.Localeouentãouma String,como“en”ou“pt”.
Caso não informemos o locale, o JSF usará o devolvido por
FacesContext.getViewRoot().getLocale(),que,senãoforalterado
dealgumaforma,seráalocalidadepadrãodosistema(browser)dousuário.
timeZone
Uma característica do JSF que não agrada muito com relação ao
f:convertDateTime é que ele usa otime zone GMT por padrão, e
não o horário do sistema. Para mudar isso teríamos que informar
timeZone="GMT-3",nocasodohoráriooficialdoBrasil,masaíteríamos
algofixo.Pararesolveresseproblemapodemoscolocaroseguinteparâmetro
no web.xml.
<context-param>
<param-name>
javax.faces
.DATETIMECONVERTER_DEFAULT_TIMEZONE_IS_SYSTEM_TIMEZONE
</param-name>
<param-value>true</param-value>
</context-param>
Comisso,emvezdoconverterusarporpadrãoo time zoneGMT,será
usadoodosistema.
185
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 202

7.36. Conversorescustomizados CasadoCódigo
f:convertNumber
<h:outputText value="#{automovel.preco}">
<f:convertNumber type="currency"/>
</h:outputText>
<h:outputText value="#{automovel.kilometragem}">
<f:convertNumber type="number"/>
</h:outputText>
ApesardoJSFconverterautomaticamentenúmerosmaissimples,quando
trabalhamoscomnúmerosmais“complexos”, porexemplo, representação
de dinheiro ou número com separador de milhar, acabamos usando o
f:convertNumber.
Esse conversor possui muitas propriedades que auxiliam na for-
matação correta dos números. Podemos dizer o mínimo e o máx-
imo de casas decimais que devem ser usadas (maxFractionDigits
e minFractionDigits), qual o símbolo de dinheiro será utilizado (
currencyCodeou currencySymbol)paraexibirR $ouUS $,porexemplo,
ouaindaum patternqualquer.Podemostambémdesabilitarasepara ção
demilharcolocando groupingUsed="false".
Tambémécomumespecificarmosovalordapropriedade type,naqual
indicamosseovaloré“number”(valorpadrão),“currency”(indicandodin-
heiro)ou“percent”.
Outrapropriedadeimportanteéa locale,queporpadrãopegaalocal-
idadedobrowserdousuário.Assim,oscaracteresdesepara çãodemilhare
decimal(pontoouvírgula)sãousadosdeacordocomovalordadoparaessa
propriedade.
7.36 Conversores customizados
Comovistonase ção7.3,oJSFéquemgeraoHTMLqueseráapresentadopara
ousuário,maisespecificamentenasextafasedoseuciclodevida.Casoatela
jávenhacomalgumvalorpreenchido,porexemploaoeditaruma Pessoa,
esseobjetoprecisasertransformadopara Stringparaquesuainforma ção
possaserguardadanoHTML.Esseprocessonosparecesimples,jáquetodo
objetoJavapossuiummétodo toString.
186
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 203

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
Ointeressanteacontecedepoisqueousuárioeditaoformulárioeoen-
vianovamenteparaoservidor. Entãoaquela Stringquerepresentaum
objetodonossodomínioprecisavoltaraserumobjeto,porexemplo,do
tipo Pessoa. NessepontolembramosqueoJavanãotemummétodo
fromStringquefa çaoinversodo toString.Justamenteporisso,temos
osconversores.
Conversores são implementa ções da interface
javax.faces.convert.Converterepossuemdoismétodosqueseriam
oscorrespondentesao toStringeumhipotético fromStringdoJava.
Sendoassim,ainterface Converterpossuiosmétodos getAsString,
querecebeum Objectedevolvea String,eummétodo getAsObject
querecebea Stringedevolveo Object.Simplesassim.
Implementeconversorescustomizados
Agoraquecompreendemosamotiva çãoparaosconversores,vamosim-
plementarumusandoaJPA.Considereum h:inputText, definidoda
seguinteforma:
<h:inputText value="#{automovelBean.automovel}" />
automovelBean.automovelmapeiadiretamenteparaumobjetodo
tipo Automovel,então,vamoscriarumconversorque,quandoocampo
forsubmetido,aomostrarainforma çãodoautomóvel,emvezdemostraro
toStringdoobjeto,mostrealgomelhor.
Vamosfazeronosso Converterpara Automovel.
@FacesConverter(forClass=Automovel.class)
public class AutomovelConverter implements Converter {
}
Oprimeirodetalhequepodemosobservaréquealémdeimplementara
interface Converter,umconversorprecisaserregistradonocontextodo
JSF.IssopodeserfeitoviaXMLouviaaanota ção @FacesConverter,que
éoqueestamosusando.
187
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 204

7.36. Conversorescustomizados CasadoCódigo
Apartirdapropriedade forClassregistramosnossoconversorpara
atuar toda vez que o JSF precisar converter umaStringpara a classe
Automovel. Oprimeirométododessainterfacequeseráimplementadoé
o getAsString.
public String getAsString(FacesContext context,
UIComponent component, Object object) {
Automovel automovel = (Automovel) object;
if(automovel == null ||
automovel.getId() == null) return null;
return String.valueOf(automovel.getId());
}
Na implementação, simplesmente devolvemos a propriedadeid do
Automovel. Ou seja, sempre que quisermos mostrar na tela um
Automovel,oqueseráexibidoéoseu id.
public Object getAsObject(FacesContext context,
UIComponent component, String string){
if(string == null || string.isEmpty()) return null;
Integer id = Integer.valueOf(string);
Automovel automovel =
entityManager.find(Automovel.class, id);
return automovel;
}
Aquinóstemosométodoquecompletaaa çãodoconverter.Apartirda
Stringdevolvidapelométodo getAsString,recuperamosoobjetoque
originalmenteestavaligadoaonossomodelo.Casoa Stringpassadaseja
nulaouembranco,devolveremosumareferêncianula.
Umavezqueobtemosovalorsubmetido,convertemosomesmopara
o tipo da chave da nossa classe, no casoInteger, e em seguida bus-
camosesseobjetonobancodedadosatravésdométodo findoumesmo
getReferencedainterface EntityManager.
Criarconversoreséalgobastanteútilquandoseestátrabalhandocom
componentesdelista,comoo selectOneMenu,porexemplo.Assim,épos-
188
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 205

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
sívelindicarosvaloresdos selectItemsdessecomponentecomosendo
objetos,enãopelos ids.
7.37 Conheça os v alidadores nativos
SeguindoociclodevidadoJSF,logoapósaconversão,vemavalida ção.Por
isso,agoravamosverquaisasformasdevalida çãooJSFtrazprontasparaus-
armos.Comoexemplo,vamosconsiderarumtrechodetelacomooseguinte:
<h:panelGrid columns="2">
Ano de Fabricação:
<h:inputText value="#{auto.anoFabricacao}">
<f:validateLongRange minimum="1950" maximum="2012"/>
</h:inputText>
Ano do Modelo:
<h:inputText value="#{auto.anoModelo}">
<f:validateLongRange minimum="1950" maximum="2013"/>
</h:inputText>
Preço: <h:inputText value="#{auto.preco}" />
Kilometragem: <h:inputText value="#{auto.kilometragem}" />
Observações: <h:inputTextarea value="#{auto.observacoes}" />
</h:panelGrid>
Tantoapropriedade minimumquantoa maximumaceitam Expression
Language,casonecessário.Apesardeestarmoscolocandoessesvalidadores
noXHTML,comojáaprendemossobreociclodevida,sabemosqueissovai
virarumainforma çãoparaoJSFvalidarnossosdadosdoladoservidor.
Temosváriasopçõesdevalidadoresdisponíveis,etodoselestêmalgumas
propriedadesemcomum:
•disabled: queaceitaumaexpressãoepodemosusarparadesligar
condicionalmenteumvalidador.Porexemplo,podemosterumaregra
denegócioquenosfa çadeixarligadoumvalidadorapenasseostatus
189
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 206

7.37. Conheçaosvalidadoresnativos CasadoCódigo
doobjetosendosalvofordiferentede“rascunho";ouaindadeixarque
ousuárioadministradorpossaenviardadossemnenhumarestri ção.
<h:inputText value="#{auto.anoFabricacao}">
<f:validateLongRange
minimum="1950"
maximum="2012"
disabled="#{currentUser.role == 'admin'}"/>
</h:inputText>
•for: essapropriedadeéusadaquandotrabalhamoscom composite
components.Veremoscomocriaressescomponenteseentãousaremos
essapropriedadenase ção9.6.
•binding:assimcomoqualqueroutrocomponenteJSF,podemosusar
apropriedade bindingparaligaroobjetodaárvoredoJSFcomuma
propriedadedo Managed Beaneassimtemoscomomanipulá-lode
formaprogramática.
f:validateLongRangeef:validateDoubleRange
Sãousadosparavalidarnúmerosinteirosereais.Podemosnotarquenão
temosvalidadorespara Integere Float,jáqueessessãoapenasversões
commenorcapacidadedearmazenamentoque Longe Double.
Propriedades:
•minimum:aceita Expression Language,eindicaomínimovalorqueo
númeroemquestãopodeter.
•maximum:aceita Expression Language,eindicaomáximovalorqueo
númeroemquestãopodeter.
f:validateLength
É bem parecido com os validadores f:validateLongRange e
f:validateDoubleRange, a diferença é que enquanto estes trabalham
comvaloresnuméricoseseusintervalos,o f:validateLengthtrabalha
190
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 207

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
comcomprimentomáximoemínimodeuma String.Podemos,porexem-
plo,usá-loparavalidarocomprimentomínimodeumasenha.
Propriedades:
•minimum:aceita Expression Language,eindicaocomprimentomín-
imoquea Stringemquestãopodeter.
•maximum:aceita Expression Language,eindicaocomprimentomáx-
imoquea Stringemquestãopodeter.
f:validateRequired
Validaaobrigatoriedadeounãodopreenchimentodovalordeumcom-
ponentedeentradadedados.Naprática,geraomesmoresultadoqueapro-
priedade requireddocomponente.
<h:inputText value="#{auto.preco}">
<f:validateRequired
disabled="#{currentUser.role == 'admin'}"/>
</h:inputText>
Oucomomesmoresultado:
<h:inputText value="#{auto.preco}"
required="#{currentUser.role != 'admin'}"/>
f:validateRegex
Esse nos permite criar uma validação baseada em expressão regular.
ApesardetermosvalidadoresprontosemprojetoscomooCaelumStella,
disponívelemhttp://stella.caelum.com.br/,podemosutilizarexpressõespara
validarCEP,e-mail,eoutrosformatos.Éimportantesalientarqueessevali-
dadornãogeranenhumamáscaraparaocampo.Eleapenasvalidaumdeter-
minadopadrãodoladoservidor.
Essevalidadorpossuiapenasumapropriedade:
•pattern:podemoscolocarqualquerexpressãoquedesejarmos.Porex-
emplo,umaexpressãoparavalidarumloginquepossuaentre6e18
caracteres,aceitandosomenteletrasminúsculas.
191
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 208

7.37. Conheçaosvalidadoresnativos CasadoCódigo
<h:inputText value="#{user.login}">
<f:validateRegex pattern="[a-z]{6,18}"/>
</h:inputText>
Nessecaso,fizemosumaexpressãoregularqueindicaqueasenhasópode
terletrasde aaté zedeveestarentre6e18caracteres.
f:validateBean
Nase ção8.4veremosmaisdetalhesdaintegra çãoentreJSFe Bean Vali-
dation.Masemresumo,essatagéusadaparaespecificarosgruposquede-
sejamosvalidar.Issoporque,apesardeanossaclasseconterasanota çõesda
Bean Validation,emumatelacomoumwizardporexemplo,vamosquerer
validarapenaspartedaspropriedadesemcadamomento.
Propriedade:
•validationGroups: informamosogrupodepropriedadesquedese-
jamosvalidar. Casoqueiramosinformarmaisdeumgrupo, infor-
mamostodoselesseparadosporvírgula.
Podemosdesabilitaravalida çãovia bean validation emdeterminadas
propriedadescomoaseguir.
<h:panelGrid columns="2">
Ano de Fabricação:
<h:inputText value="#{auto.anoFabricacao}">
<f:validateBean disabled="true"/>
</h:inputText>
Ano do Modelo:
<h:inputText value="#{auto.anoModelo}">
<f:validateBean
disabled="${auto.status == 'rascunho'}"/>
</h:inputText>
Preço:
<h:inputText value="#{auto.preco}" />
192
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 209

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
Kilometragem:
<h:inputText value="#{auto.kilometragem}" />
Observações:
<h:inputTextarea value="#{auto.observacoes}" />
</h:panelGrid>
Masgeralmentefaríamosissoemsitua çõescomoamencionadaacima,
naqualtemosumwizardoualgumateladecadastronãotãotrivialemque
aquelesvalores,apesardeobrigatórios,nãoprecisamservalidadosnaquele
momento,provavelmenteporqueserãoprovidosdepois.Nessescasos,uma
possibilidadeétrabalharmoscomgruposeusaralgoparecidocomoseguinte:
<f:validateBean validationGroups="cadastroBasico">
<h:panelGrid columns="2">
Ano de Fabricação:
<h:inputText value="#{auto.anoFabricacao}"/>
Ano do Modelo:
<h:inputText value="#{auto.anoModelo}"/>
Preço:
<h:inputText value="#{auto.preco}" />
Kilometragem:
<h:inputText value="#{auto.kilometragem}" />
Observações:
<h:inputTextarea value="#{auto.observacoes}" />
</h:panelGrid>
</f:validateBean>
Agorasim,considerandoqueessatelacorrespondeaumcadastrobásico,
camposquesãoobrigatóriosmasquenãosãopartedessegruponãoseriam
validadosagora.
Outro ponto interessante nos exemplos apresentados é que podemos
tantocolocaratagdentrodeumdeterminadocomponente,comoemvolta
detodososcomponentesquegostaríamosquetivessemomesmotratamento.
Muitomenosrepetitivo.
193
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 210

7.38. Equandoosvalidadoresnativosnãofazemoqueeuquero?Crieseusvalidadores CasadoCódigo
7.38 Equando os v alidadores nativos não fazem
o que eu quero?Crie seus v alidadores
Jávimosváriasformasdevalidarosvaloresqueousuáriosubmete. Mas
muitasvezes,temosvalida çõesquesãoespecíficasdonossodomínio,como
verificarseumCPFdigitadoéefetivamenteválido.
Considerequeousuáriopodefazero Pedidodeum Produtopelo
codigodesse Produto. Vamossuporque,nessecenário,ousuáriopossa
fazer“pedidospopulares”,nosquaisédadoumdescontode20%(vintepor-
cento)nopre çodoproduto,desdequeovalorunitárionãoultrapasseR $
200,00.Paraconseguirmosfazerisso,vamosteroseguintecódigo:
@Entity
public class Produto {
@Id @GeneratedValue
private Integer id;
@Column(unique=true)
private String codigo;
private Float valor;
}
@Entity
public class Pedido {
@Id @GeneratedValue
private Integer id;
@ManyToOne
private Produto produto;
private Integer quantidade;
private boolean pedidoPopular;
}
Eo xhtmlmostrandooformulário:
<h:form>
<h:panelGrid columns="2">
194
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 211

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
Pedido popular?
<h:selectBooleanCheckbox
value="#{pedidoBean.pedido.pedidoPopular}">
<f:ajax/>
</h:selectBooleanCheckbox>
Produto:
<h:inputText id="produto"
value="#{pedidoBean.pedido.produto}"
converter="produtoConverter">
<f:validator
validatorId="produtoPedidoPopularValidator"
disabled="#{!pedidoBean.pedido.pedidoPopular}"/>
</h:inputText>
Quantidade:
<h:inputText value="#{pedidobean.pedido.quantidade}"/>
<h:panelGrid/>
</h:form>
O que percebemos de novidade nesse código é a presença da tag
f:validatornocomponente h:inputTextde id="produto".Nesse
validador,cujocódigoveremosaseguir,checamossearestri çãodenegó-
ciodevalormáximodeR $200,00estáounãosendorespeitada.Utilizamos
tambémapropriedade disabledparasomenteaplicarovalidadorcasoa
opçãode“pedidopopular”nãoestejaselecionada. Alémdisso,indicamos
queo validatorIdé produtoPedidoPopularValidator,queéuma
referênciaparaum Validatorquevamoscriar.
Comoestamostrabalhandocomvalidadores,sabemosqueelesseex-
ecutamnaterceirafasedociclodevidadoJSF,jáaatualiza çãodonosso
modelo acontece só na quarta fase. Sendo assim, o valor da expressão
#{!pedidoBean.pedido.pedidoPopular}sóseráatualizadanaquarta
fase,ouseja,depoisdomomentoemqueoconversorseexecutaria.
Geralmenteemcasosassim,oresultadoacabasendooinversodoesper-
195
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 212

7.38. Equandoosvalidadoresnativosnãofazemoqueeuquero?Crieseusvalidadores CasadoCódigo
ado,jáque,comoovalorde pedidoPopularoriginalmenteéfalso,entãoo
conversornãoserádesativadonaprimeirarequisi ção.Seousuárioselecionar
“pedidopopular”,ovalidadorsóserádesativadonapróximarequisição.Logo,
teríamossempreoresultadoesperado-validadorhabilitadooudesabilitado
corretamente-comumarequisi çãodeatraso.
Poressemotivo,no xhtmlcolocamosatag f:ajaxsemnenhuma
propriedadeespecificada. Issosomenteexecutaumpequeno request,atu-
alizandoovalordoprópriocomponentenomodeloenãotrazendonada
como resposta. Dessa forma, antecipamos a atualização da propriedade
pedidoPopularparaqueovalidadorsejadesabilitadoounãonomomento
correto.
Veremosnase ção9.4maisdetalhessobreousodatag f:ajaxenase ção
10.7comoutilizarAJAXdemodoeficienteparanãocomprometeraperfor-
mancedaaplica ção.
Aseguirtemosadefini çãodonossovalidador:
@FacesValidator("produtoPedidoPopularValidator")
public class ProdutoPedidoPopularValidator implements Validator{
}
Podemos notar que o validador funciona de forma bem pare-
cida com um conversor customizado. Ele implementa a interface
javax.faces.validator.Validatoreéregistradocomumidatravés
daanota ção @javax.faces.validator.FacesValidator.
Ao criar um validador customizado, temos a implementar um único
método,quedevelan çaruma ValidatorException,casoovalorsejain-
válido.
public void validate(FacesContext context,
UIComponent component, Object value) throws ValidatorException{
// objeto já vem convertido
Produto produto = (Produto) value;
if(produto.getValor() > 200.0){
FacesMessage message =
new FacesMessage("Pedido popular: máximo R$ 200");
message.setSeverity(FacesMessage.SEVERITY_ERROR);
196
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 213

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
throw new ValidatorException(message);
}
}
A implementação é simples: precisamos apenas lan çar uma
ValidatorException que recebe uma ou maisFacesMessage, e
que pode opcionalmente também receber umaThrowable. Caso o
validadorexecutesemlan çarexce ção,significaqueovaloréválido.
Nocasoderegrasmuitoespecíficas,épossíveldeixá-lasdiretono Man-
aged Bean. Paraisso,bastariaimplementarummétodoquerecebeostrês
parâmetrosqueosvalidadoresrecebem, FacesContext, UIComponente
Object,dandoumnomearbitrárioaele.
@ManagedBean
public class PedidoBean {
private Pedido pedido;
...
public void validaProdutoPedidoPopular(FacesContext context,
UIComponent component, Object value)
throws ValidatorException {
//objeto vem convertido
Produto produto = (Produto) value;
if(pedido.isPedidoPopular() &&
produto.getValor() > 200.0){
FacesMessage message =
new FacesMessage("Pedido popular: máximo R$ 200");
message.setSeverity(FacesMessage.SEVERITY_ERROR);
throw new ValidatorException(message);
}
}
}
E por fim, referenciar esse validador em um componente, como o
inputText:
<h:inputText id="produto"
value="#{pedidoBean.pedido.produto}"
197
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 214

7.39. Novidade:JSFcomGETebookmarkableURLs CasadoCódigo
converter="produtoConverter"
validator="#{pedidoBean.validaProdutoPedidoPopular}"/>
7.39 Novidade: JSF com GET e bookmarkable
URLs
Nessase çãoveremosalgunscomponentesquenospossibilitamusar book-
markable URLs,ouseja,URLsquepodemoscolocaremnosso bookmark,ou
favoritos.
AgoraquejávimoscomofuncionamoscomponentesbásicosdoJSFe
tambémjáentendemoscomofuncionamosconversoresevalidadores,poder-
emostirarmelhorproveitodessesuportequefoiadicionadonoJSFversão2.0
eaprimoradonaversão2.2.
7.40 h:button e h :link
<h:dataTable value="#{automovelBean.automoveis}"
var="automovel">
<h:button value="Editar" outcome="editar">
<f:param name="automovel" value="#{automovel.id}"/>
</h:button>
<h:link value="Editar" outcome="editar"
includeViewParams="true">
<f:param name="automovel" value="#{automovel.id}"/>
</h:link>
</h:dataTable>
Novamente,oscomponentesquerenderizambotãoelinktêmomesmo
comportamento,masnocasodo h:buttone h:link,elessãoelementos
quenãosubmetemoformulárioondeestão.Porissomesmonemprecisam
estardentrodeumformulário.Essescomponentesgeramrequisi çõesdotipo
GET,enão POSTcomooscomponentes command.
Algomuitoimportanteanotarmoséapropriedade outcome. Como
nãotemosumamaneiradeexecutarumaa çãoeassimdescobriroresultado
198
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 215

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
paraanavega ção,chamado outcome,temosquedeixarexplícitoqualéesse
resultado. Baseadonesse outcome,oJSFexecutaráaregradenavega ção
paradescobrirquallinkdeverámontar.
DepoisqueoJSFsabequalpáginaseráalvodolinkpelaregradenave-
gação,casoapropriedade includeViewParamsestejacomvaloriguala
true,eleidentificaseapáginaalvopossui f:viewParam;casopossua,ele
tentagerarlinkoubotãocomosparâmetrosnecessáriosnatelaseguinte.
Atelaqueseráexibida, porexemploa editarAutomovel.xhtml,
poderáterumcódigocomooseguinte:
<f:metadata>
<f:viewParam name="automovel"
value="#{automovelBean.automovel}"/>
<f:viewParam name="usuario" value="#{session.currentUser}"/>
</f:metadata>
Sendoassim,considerandoquetenhamosumconversorparausuárioque
otransformepara Stringdevolvendoseu username,equeo username
dousuáriologadoé“admin”,olinkgeradopeloh:linkseriaalgopare-
cidocomoseguinte:http://servidor.com.br/faces-motors/editarAutomovel.
xhtml?automovel=90&usuario=admin
A tag f:metadata, apenas delimita uma área para a definição de
metadados sobre a página, como os parâmetros. Ainda veremos sobre
f:viewParam, mas sua principal finalidade é explicitar as informações
queatelaprecisaparafuncionar. Usando includeViewParams=true,
mesmoqueessaspropriedadesnãoestejaminformadasviaum f:param
no h:link,oJSFrenderizaolinkusandoessasinforma çõesparaqueopos-
samossalvarnos bookmarks.
f:viewParam
<f:metadata>
<f:viewParam name="automovel"
value="#{automovelBean.automovel}"/>
<f:viewParam name="usuario" value="#{session.currentUser}"/>
</f:metadata>
199
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 216

7.40. h:buttoneh:link CasadoCódigo
Osparâmetrosda viewservemparaquepossamostrabalharcorretamente
comrequisi çõesGETnoJSF.Porexemplo,podemosmontarumlinkemoutra
aplicação,feitacomoutratecnologia,eenviarparanossaaplica çãoemJSF,
oupodemossimplesmenteacessarumlinksalvonosnossos bookmarks.Esse
linkiráconterasinforma çõesqueserãocarregadasnonossomodeloatravés
decadacomponente f:viewParam.
Podemospensarno f:viewParamcomosefosseum h:inputText,
mas,emvezdeentrarmoscomosdadosemumformulário,fazemosisso
viaURL.Podemoscolocarconversores,validadoresetudomaisquetemos
disponívelcomos inputsnormais.
Paraentendermosmelhor,considerequeaURLemquestãoéamesma
apresentadanoexemploanterior.
http://servidor.com.br/faces-motors/editarAutomovel.xhtml?automovel=
90&usuario=admin
Assumindoquetanto Automovelquanto Usuariopossuemconver-
soresadequadamenteimplementados,osobjetosserãoatribuídosaoqueé
apontadopelo valuedo f:viewParameatelaexecutaránormalmente.
f:viewAction
<f:metadata>
<f:viewParam name="modelo"
value="#{automovelBuscaBean.modelo}"/>
<f:viewParam name="anoMinimo"
value="#{automovelBuscaBean.anoMinimo}"/>
<f:viewParam name="anoMaximo"
value="#{automovelBuscaBean.anoMaximo}"/>
<f:viewAction
action="#{automovelBuscaBean.buscarAutomoveis}"/>
</f:metadata>
Essecomponenteénovonaversão2.2doJSFeserveparaauxiliarno
processodeconstru çãodeumatelaapartirdeumaURLquepodevirdeoutra
aplicaçãooudosnossos bookmarks. Porpadrão,essa actionvaiexecutar
comosefosseopressionardeum h:commandButtonou h:commandLink.
200
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 217

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
EleexecutanaquintafasedociclodevidadoJSFesónaprimeiravezque
abrimosatela,nãoexecutandonassubmissõesparaamesmapágina,que
chamamosde“postback”.Casoessaaçãopreciseserchamadatodasasvezes,
precisaríamoshabilitarissopormeiodapropriedade onPostback=true.
Quandoessaa çãoseexecutar,osvaloresassociadosao f:viewParamjá
estarãocarregadosefaremosapenasocarregamentodeoutrasinforma ções
necessáriasparaapágina.Comoefetuarabuscasegundoosparâmetrosin-
formados,porexemplo.
7.41 Regras de navegação
Aogravarmosuma Marcaoidealéquesejamosenviadosparaatelade
listagem.Omecanismotradicionalparafazeroredirecionamento,presente
noJSFdesdesuaprimeiraversão,éousoderesultadoslógicosacadaa ção,
edepoisvincularcadaumdessescomapróximapáginaaserexibida.Como
estamosfalandodenavega çãoentrepáginas,ocaminhocompletodaspáginas
deorigemedestinoprecisaserconhecido.
Nesse exemplo temos duas páginas: editar.xhtml e
listar.xhtml, ambas dentro da pastamarca, como pode ser visto
nafiguraaseguir.Vamosanalisarousoderesultadoslógicos,chamadosde
outcome,paranavegarentreessaspáginas.
Fig.7.21:Estruturadapasta‘marca’
@ManagedBean @ViewScoped
public class MarcaBean {
private Marca marca = new Marca();
public String salvar(){
try {
201
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 218

7.41. Regrasdenavegação CasadoCódigo
EntityManager em = JpaUtil.getEntityManager();
em.persist(marca);
return "sucesso";
}
catch(Exception e){
return "falha";
}
}
// getters e setters...
}
Apenas retornamos um resultado lógico, umaString“sucesso” ou
“falha”.EmqualquerprojetoJSF,épossívelterumarquivodeconfiguração,
o faces-config.xml,emquenósconfiguramosparaqualpáginacada
resultadodessedeveenviarousuário.
<faces-config ...>
<navigation-rule>
<from-view-id>/marca/editar.xhtml</from-view-id>
<navigation-case>
<from-outcome>sucesso</from-outcome>
<to-view-id>/marca/listar.xhtml</to-view-id>
<redirect/>
</navigation-case>
<navigation-case>
<from-action>#{marcaBean.excluir}</from-action>
<from-outcome>sucesso</from-outcome>
<to-view-id>/home.xhtml</to-view-id>
<redirect/>
</navigation-case>
<navigation-case>
<from-outcome>falha</from-outcome>
<to-view-id>/marca/editar.xhtml</to-view-id>
</navigation-case>
</navigation-rule>
</faces-config>
Aestruturabásicaéassim:uma <navigation-rule>possuiopcional-
menteuma <from-view-id>,naqualespecificamosqueessaregraseaplica
202
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 219

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
àsnavega çõesquepartiremdessapágina. Podemosusar‘*’(asterisco)para
indicarumapartedocaminhodapágina,ouentãodeixarsomenteoaster-
iscoparaindicarqueéumaregraglobal,queseaplicaaqualquerpáginado
sistema.
Após especificarmos a página de origem da regra, definimos
navigation-cases,quefuncionamcomum switch case,noquala
variávelanalisadaéooutcomeeopcionalmenteaprópriaa çãoquefoiexecu-
tada.Comopodemosver,no faces-config.xmlpodemosusaromesmo
outcomeemmaisdeuma action. Considerandoqueaactionexecutadafoi
salvar(),apróximapáginaaserexibidaserá /marca/listar.xhtml.
Pormaisqueexistaoutrocasodenavega çãoqueaceitaomesmo outcome,
essaoutrasóéválidacasoaa çãoprocessadaseja #{marcaBean.excluir}.
Emambososcasos,vemosapresen çadatag <redirect/>,queserve
paraindicarque,emvezdeum forward,oJSFdeveráfazerum redirect
paraapróximapágina.
Nofinal,temosocasoqueconsideraoresultado falha.Nessaregra,nós
colocamosapróximapáginaigualàoriginal,ouseja,emcasodeerro,não
mudaremosdepágina.Noentanto,podemosremoveresseúltimocasosem
prejuízo,jáque,mesmoqueoJSFnãoencontrenenhumcasodenavega ção
configuradoparao outcome falha,nãoocorreránenhumerro.Issoporque
ocomportamentopadrãoéficarnamesmapáginaquandonãoexistenenhum
casodenavega çãocompatível.
Navegaçõesimplícitas
Apesardanavega çãoatravésdeumresultadológicoserbemflexívelno
casodequerermosmudarapáginaqueseráexibidadepois,nocotidiano
dodesenvolvimentodeaplica çõesnãoémuitocomumissoacontecer. Na
prática,muitasvezestínhamosquefazerumaconfigura çãoquedificilmente
mudaria,alémdetermosumarquivoXMLcomimensasregrasdenavega ção,
apesardeexistiremdiversasferramentasvisuaisparaconstruí-las.
Na versão 2.0, foi acrescentado ao JSF o suporte de navegação im-
plícita. Retornado o outcome, é buscada uma regra de navegação no
faces-config.xmlecasonenhumasejaencontrada,ébuscadonomesmo
diretórioda viewatual,umapáginacomonomeigualao outcomeretornado.
203
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 220

7.42. Entendaosescoposesaibacomoequandotrabalharcomcadaum CasadoCódigo
Vamostomarcomoexemploamesmaestruturadafigura7.21.
Comodificilmenteteremosumapáginachamada sucesso.xhtml,va-
mosalterarocódigodométodo salvardaclasse MarcaBean.
public String salvar(){
EntityManager em = JpaUtil.getEntityManager();
em.persist(marca);
return "listar";
}
Usando a navega ção implícita, podemos deixar de usar as
navigation-rules no faces-config.xml, então vamos consid-
erarqueapagamosasregrasvistasanteriormente.
Agoraquandoométodo salvarexecutarcomsucesso,comonenhuma
regraparao outcome“listar”estádefinida,automaticamenteoJSFexibiráa
view listar.xhtmlqueestivernamesmapastada viewatual.
Porfim,éimportanteficaratentoaofatodeque,nanavega çãoimplícita,
assimcomoatravésdo faces-config.xml,porpadrãooJSFrealizaape-
nasum forwardparaa viewqueseráexibida. Vimosquepodemosmudar
issono faces-config.xmlpormeiodatag <redirect />. Nocaso
danavega çãoimplícita,bastaindicaranecessidadedo redirectna String
queestásendoretornada,com ?faces-redirect=true.Assim,ométodo
salvarqueredirecionaparao listar.xhtmlficaria:
public String salvar(){
EntityManager em = JpaUtil.getEntityManager();
em.persist(marca);
return "listar?faces-redirect=true";
}
Alémdisso,quandoométodoé voidenãotemosnenhumanavega ção
definida,significaqueatelaaserrenderizadaéamesmateladeorigem.
7.42 Entenda os escopos e saiba como e quando
trabalhar com cada um
DesdeaépocaemqueprogramávamosasnossasServlets,temoscontatocom
trêsescopos: request, sessione application.Essesmesmosescopos
204
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 221

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
eramosúnicosdisponíveisatéaúltimaversãodasérie1.XdoJSF.
Oresultadodissoerasimples:funcionalidadessimpleseramconstruídas
utilizandoescopo request,masqualqueroutraumpoucomaiscomplexa
nosobrigavaausarumescopomaior,comoo session.
Oobjetivodessase çãoéentendermosquandousarcadaescopo,semuti-
lizaralgomaiordoqueprecisamossóparaevitaralgumproblema.
RequestScope
Fig.7.22:Escoporequest
@ManagedBean
@RequestScoped
public class MeuBean {
}
Objetosarmazenadosnoescopo requestsobrevivemporumapassada
nociclodevidadoJSF,ouseja,desdequearequisi çãodousuáriochegaao
205
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 222

7.42. Entendaosescoposesaibacomoequandotrabalharcomcadaum CasadoCódigo
servidor(fase1)atéquearespostasejaenviadaaesseusuário(fase6). Por
serumescopoquetemumavidacurta,seriaopreferívelparautilizarmos,
afinal,quantomenostemponossosobjetosviverem,maiscedoamemória
doservidorseráliberadaecomissonossaaplica çãotendeaescalarmelhor.
Comoquasesemprenaprograma çãonãoháreceitadeboloaseguir,ape-
sardeserumaboapráticausarmossempreomenorescopopossível,issonão
significaqueusaremossempreoescopo request.Esseescopoéapropriado
quandonãoprecisamosmemorizardadosentreasrequisi çõesdosusuários.
Seguardamosemmemóriaváriasa çõesdousuário,comobuscarváriosfun-
cionáriosparavinculá-losaumdepartamento,esomentenofinalsalvamosas
informações,ébemprovávelque requestnãosejaamelhorop ção.Agora,
seaoeditarmososdadosdeumaúnicapessoativermosapenascamposque
nãoprecisamsercalculadoscombaseemoutroscampos,entãoprovavel-
mentepoderemosutilizaresseescopo.
Oescopo requestéopadrãodos Managed Beans,dessaforma,aonão
anotarsuaclasse,esseescoposeráutilizado.
206
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 223

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
SessionScope
Fig.7.23:Escoposession
207
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 224

7.42. Entendaosescoposesaibacomoequandotrabalharcomcadaum CasadoCódigo
@ManagedBean
@SessionScoped
public class MeuBean {
}
Nesse escopo, tudo que armazenarmos ficará disponível enquanto a
sessãodousuárioestiverativa. Asessãodousuárioéaliga çãodonaveg-
adorcomoservidorJava,entãoseomesmousuárioabrirdoisnavegadores
diferentesapontandoparaamesmaaplica ção,eleteráduassessõesdiferentes.
Geralmenteesseescopoéusadoparaguardarinforma çõesqueprecisam
permanecerpormuitotempo,masquesãoreferentesaumúnicousuário.
Umexemplo,alémdasinforma çõesdoprópriousuáriologado,éarmazenar
informaçãosobreaúltimaopera çãorealizadaporele,paraproporcionaruma
formafácildevoltaraela. Considerequeumusuárioacaboudeeditarum
Automovelefoiparaoutrapartedaaplica ção. Depoiselevoltaàtelade
ediçãodeautomóveisetemaop çãodereabriroúltimo Automoveleditado
porele.
208
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 225

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
ApplicationScope
Fig.7.24:Escopoapplication
@ManagedBean
@ApplicationScoped
public class MeuBean {
}
Tudoqueéarmazenadonoescopodeaplica çãopermaneceenquanto
aaplica çãoestiverexecutando,eécompartilhadaentretodososusuários.
Nesseescopoépossívelguardarinforma çõescomoosusuáriosqueestãoon-
linenaaplica çãoedisponibilizaralgumafuncionalidadedecomunica çãoen-
treeles. Écomumtambémarealiza çãodecachemanualdealgunsvalores
209
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 226

7.42. Entendaosescoposesaibacomoequandotrabalharcomcadaum CasadoCódigo
nesseescopo,comoporexemploumalistagemdeestadosemunicípios.
ViewScope
Fig.7.25:Escopoview
@ManagedBean
@ViewScoped
public class MeuBean {
}
Aversão2doJSFacrescentouumescopoquedessesuporteaomodelo
statefuldoframework,quenãoonerassetantoaescalabilidadedaaplica ção,
comoocasodoescopodesessão.Comisso,surgiuo @ViewScoped.
Esseescopoconsisteemmanterosdadoscontidosneleporquantasreq-
210
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 227

CasadoCódigo Capítulo7. EntendaoJSFecrieaplica çõesweb
uisiçõesforemfeitas,masdesdequesejamtodasparaamesma view. No
momentoemquetrocamosdepáginaoescopoézerado.Issoémuitobom,
porqueevitaqueacumulemosobjetosqueficamvivospormuitotempo,como
noescopodesessão,masaomesmotempopermitea çõesfeitasemsequência,
comocombosemcascata,quenesseescopofuncionamperfeitamente.
Apesardemuitoútil,énecessárioatentarparaalgunsdetalhesimpor-
tantesdesseescopo. Oprincipaldeleséqueoobjetonoescopo viewsóé
removidodamemóriaseamudan çadepáginaforfeitaviaum POST.Sesim-
plesmenteacessarmosumlinkqueapontaparaoutrapágina,osdadosdatela
anteriorcontinuarãonamemória. Essecomportamentopermiteabrirmos
umlinkemoutraabasemperderosdadosdapáginaoriginal. Massenão
lembrarmosdequesomentecomnavega çãoviaPOSToescopoédestruído,
podemosterobjetosdesnecessáriosnamemória.
7.43 Acurv a de aprendizado doJSF
SãomuitosconceitosnovoscasovocênuncatenhausadooJSFantes,ecom
isso,acurvadeaprendizadonocome çotendeaserumpoucomaiscompli-
cada. Issoécomum. Nessecapítulovocêaprendeudiversascaracterísticas
quefazemdoJSFumframeworkúnicoentreosdisponíveisemJavaeespero
quevocêestejaprontoparaaplicartodosessesconceitosemseusprojetos.
Masaindanãoétudo,temosmaisporver. agoraquejáaprendemosas
características,vamospodernoselevaraumnívelemqueusaremosastécni-
casavan çadaseváriasoutrasboaspráticas.
211
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 228

E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 229

Capítulo8
ValidaçõessimplificadasnaJPAe
noJSFcomaBeanValidation
Nestecapítuloseráapresentadaumabrevevisãosobrea Bean Validatione
comousá-laintegradaaoutrasespecifica çõesquesãoalvodestelivro.
Nocapítulo7vimosofuncionamentodoJSF,ecomoeletrataquestões
devalida ção.Vimoscomoésimplesadicionarumavalida çãodecampoobri-
gatórioouumintervalopermitidoparaumvalornumérico.
Comovalida çõessãorequisitosdequalqueraplica ção,passou-seaadotá-
lasnomodeloenãonaapresenta çãooucontroledoMVC.Foientãoquese
popularizou,impulsionadopelosucessodoHibernate,oHibernateValida-
tor,queacabouinspirandoumaespecifica çãochamada Bean Validation(JSR-
303).Comela,nóscolocamosasrestri çõesviaanota çãonasnossasentidades,
entãotantooJSFquantoaJPAusamessasinforma çõesparavalidarosdados.
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 230

8.1. Trabalhecomosvalidadoresecriesuaprópriavalida ção CasadoCódigo
8.1 Trabalhe com os v alidadores e crie sua
própria v alidação
AssimcomoaJPA,aBeanValidationéumaespecifica çãoquedefineuma
sériedeanota çõesparausarmosemnossasclasses. Porém,emvezdema-
peamentoobjetorelacional,definimosnonossomodeloasregrasdevali-
daçãodedados.Porexemplo,naentidade Automovelpodemosespecificar
asseguintesrestri ções.
@Entity
public class Automovel {
@Min(1900)
@MaxAnoAtualMais(message="O máximo do ano de fabricação é
{0}")
private Integer anoFabricacao;
@Min(1900)
@MaxAnoAtualMais(value=1, message="O máximo do ano do modelo
é {0}")
private Integer anoModelo;
@NotNull
private Float preco;
}
@Mine @NotNullsãovalidadoresnativosdaBeanValidation.Maspara
considerardinamicamenteoanoatual,criamosumvalidadorcustomizado
@MaxAnoAtualMais,noqualpassamosainforma çãodeatéquantosanosà
frentedoatualéconsideradoumvaloraceito.
Paraimplementaressavalida ção,precisamosdadefini çãodaanota ção
MaxAnoAtualMais:
@Documented
@Constraint(validatedBy = MaxAnoAtualMaisValidator.class)
@Target( { METHOD, FIELD, ANNOTATION_TYPE, CONSTRUCTOR,
PARAMETER })
214
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 231

CasadoCódigo Capítulo8. ValidaçõessimplificadasnaJPAenoJSFcomaBean...
@Retention(RetentionPolicy.RUNTIME)
public @interface MaxAnoAtualMais {
String message() default "O valor máximo para esse
campo é {0}";
int value() default 0;
Class<?>[] groups() default {};
Class<? extends Payload>[] payload() default {};
}
E também a classe onde estará toda a regra de validação:
public class MaxAnoAtualMaisValidator implements
ConstraintValidator<MaxAnoAtualMais, Integer> {
private int maxValue;
@Override
public void initialize(MaxAnoAtualMais annotation) {
int anosAdicionais = annotation.value();
int anoAtual =
Calendar.getInstance().get(Calendar.YEAR);
maxValue = anoAtual + anosAdicionais;
}
@Override
public boolean isValid(Integer value,
ConstraintValidatorContext context) {
if(value > maxValue){
String template =
context.getDefaultConstraintMessageTemplate();
String message =
MessageFormat.format(template, maxValue);
context
.buildConstraintViolationWithTemplate(message)
.addConstraintViolation()
215
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 232

8.2. Organizegruposdevalida ção CasadoCódigo
.disableDefaultConstraintViolation();
return false;
}
return true;
}
}
Nométodo initializedovalidador,nósrecebemosaanota çãoque
defineavalida ção. Nonossoexemplo,temosduasocorrênciasdaanota ção
@MaxAnoAtualMais,umacomzeroeoutracomumanoadicional.Recu-
peramosessevaloresomamoscomoanoatual,assimsabemosqualéomáx-
imoqueovalidadorirápermitir.
Nométodo isValid,recebemosovalorinformadopelousuárioere-
tornamos trueseovalorforválidoou falsecasocontrário. Orestante
docorpodométodofoiusadoapenasparamontarmosumamensagemmais
completaparaousuário.
Recuperamos a mensagem de erro configurada na anotação via
context.getDefaultConstraintMessageTemplate(). Nocasoda
validaçãodoanodefabrica ção,ovalorde templateé"O Valor máximo
do ano de fabricação é {0}” . Comissoemmãos,geramosamen-
sagem usando a classeMessageFormat que troca {0} pelo valo de
maxValue. Comamensagempronta,nósreconfiguramosamensagemde
errocomorestantedocódigo.
8.2 Organize grupos de v alidação
Alémdeespecificarmososvalidadoresparacadapropriedadedanossaen-
tidade,podemostambémagrupá-los.Paraumcadastromuitolongo,épos-
sívelterumgrupoquerepresenteavalida çãomínimaparasesalvaroregistro
comorascunho,eumgrupomaiscompletoquerepresenteavalida çãocomo
umtodo.Umexemplodissoéoe-mail,podemossalvarume-mailcomoras-
cunhosemterumdestinatário,masparaenviá-loodestinatárioéobrigatório.
Senãoespecificarmosnada,porpadrão,todasasvalida çõesficamemum
grupochamado Default.Etambém,sempreantesdepersistir,aJPAval-
216
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 233

CasadoCódigo Capítulo8. ValidaçõessimplificadasnaJPAenoJSFcomaBean...
idatudoqueestiverassociadoaessegrupo.Comisso,todososvalidadores
danossaentidade,mesmoquenãoobrigatóriosparasalvaraentidadecomo
rascunho,serãodisparadosnomomentoemquetentarmospersistiresseob-
jeto.
Paraespecificarumgrupo,usamosumaclassequalquer,geralmentecri-
adaapenaspararepresentá-lo.
package facesmotors.validation.groups;
public interface ValidacaoMinima { }
Eagoraespecificaremosogrupo ValidacaoMinimanavalida çãoda
propriedade preco.Issosignificaquemesmoquandosalvarmosumobjeto
emmodo“rascunho”,ouseja,emumaversãoincompleta,pelomenosaspro-
priedadesqueestiveremnessegrupodeverãoservalidadas.
@Entity
public class Automovel {
@Min(1900)
@MaxAnoAtualMais(message="O máximo do ano de fabricação
é {0}")
private Integer anoFabricacao;
@Min(1900)
@MaxAnoAtualMais(value=1, message="O máximo do ano do modelo
é {0}")
private Integer anoModelo;
@NotNull(groups={ValidacaoMinima.class, Default.class})
private Float preco;
}
8.3 A integração entre BeanValidation eJPA
IntegrarJPAeBeanValidationrequeresfor çoquasezero.Bastaquehajaum
Validation Provider,queéumaimplementa çãodeBeanValidationnoambi-
ente,queaJPAautomaticamentepassaráausá-la.
217
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 234

8.3. AintegraçãoentreBeanValidationeJPA CasadoCódigo
Noentantopodemosespecificarumaconfigura çãoparadesabilitarain-
tegraçãoentreJPAeBeanValidation:
<persistence-unit name="default"
transaction-type="RESOURCE_LOCAL">
<validation-mode>NONE</validation-mode>
<properties>
...
</properties>
</persistence-unit>
Natag validation-mode,osvalorespossíveissão:
•NONE:desabilitaaintegra çãoentreasespecifica ções;
•CALLBACK:explicitamenteligaaintegra ção, lançandoumaexce ção
casoumprovedornãoestejadisponível.Podeserinteressanteparaas-
segurarqueaaplica çãonãoiráexecutarsemasvalida çõesprevistas;
•AUTO:habilitaavalida çãoseo providerforencontrado.
Comovimosnase çãoanterior,aJPAporpadrãovalidaogrupo Default
aoinserireaorealizaraatualiza çãodosregistros. Podemos,porém,alterar
essecomportamentoparavalidarapenasogrupo ValidacaoMinima.Va-
mosadicionaraoarquivo persistence.xmlasseguintespropriedades:
<persistence-unit name="default"
transaction-type="RESOURCE_LOCAL">
<validation-mode>AUTO</validation-mode>
<properties>
...
<property
name="javax.persistence.validation.group.pre-persist"
value="facesmotors.validation.groups.ValidacaoMinima"/>
<property
name="javax.persistence.validation.group.pre-update"
value="facesmotors.validation.groups.ValidacaoMinima"/>
</properties>
</persistence-unit>
218
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 235

CasadoCódigo Capítulo8. ValidaçõessimplificadasnaJPAenoJSFcomaBean...
Além das duas propriedades, ainda temos a
javax.persistence.validation.group.pre-removequepodemos
usar para especificar o grupo padrão a ser considerado na exclusão das
informações. Em cada propriedade dessa, podemos passar mais de um
grupo,usandoavírgulacomoseparadordonomedasclasses.
8.4 A integração entre BeanValidation eJSF
Aintegra ção Bean ValidationeJSFtambéméautomáticadesdequeumaim-
plementaçãoestejadisponívelnoambientedaaplica ção. Temosapenasa
opçãodedesabilitaressaintegra çãopormeiodeumasimplesconfigura ção
no web.xml
<context-param>
<param-name>
javax.faces.validator.DISABLE_BEAN_VALIDATOR
</param-name>
<param-value>true</param-value>
</context-param>
Desdequenãodesabilitemosaintegra ção,nãoprecisamosfazernada
parausarasanota çõescomovalidadoresdoJSF.Detodaforma,temosatag
f:validateBeanque,apesardeparecer,nãoserveparahabilitaravali-
daçãodoJSFviaBeanValidation.Usamosessatagparadesabilitaravalida ção
ouentãoespecificarumgrupodiferentedevalida ção.
<f:validateBean
validationGroups=
"facesmotors.validation.groups.ValidacaoMinima">
<h:panelGrid columns="2">
Ano de Fabricação: <h:inputText
value="#{auto.anoFabricacao}" />
Ano do Modelo: <h:inputText value="#{auto.anoModelo}" />
Preço: <h:inputText value="#{auto.preco}" />
Kilometragem: <h:inputText
value="#{auto.kilometragem}" />
Observações: <h:inputTextarea
219
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 236

8.4. AintegraçãoentreBeanValidationeJSF CasadoCódigo
value="#{auto.observacoes}" />
</h:panelGrid>
</f:validateBean>
Nesseexemplo,especificamosquetodososcomponentesdentrodatag
f:validateBeanterãovalidadosapenasogrupo ValidacaoMinima.
Emrela çãoaoJSFtemosmaisumdetalhequeenvolveavalida çãode
camposcujosvaloressãodotipo String,comoporexemploapropriedade
observacoes. Porpadrão,quandodesenvolvemosparaawebcomJava,
todo inputcujovalorsejauma Stringnãoretornavalor null,esimuma
Stringembranco. Porém,aespecificação Bean Validationnãopossuium
validadorqueverificaseovalorédiferentede“embranco”.
@Entity
public class Automovel {
...
@NotNull
private String observacoes;
...
}
Emvezdecriarmosumnovovalidadorcustomizadoouusaralgumes-
pecíficodaimplementa çãode Bean Validation,queexistenoHibernateVal-
idator-aanota ção NotEmpty-,vamossomentefazerumaconfigura çãono
web.xmlparaque Stringembrancosejamsubmetidascomvalor null.
<context-param>
<param-name>
javax.faces.INTERPRET_EMPTY_STRING_SUBMITTED_VALUES_AS_NULL
</param-name>
<param-value>true</param-value>
</context-param>
Agora o validador @NotNull irá barrar Strings que não foram
preenchidaspelousuárioequeanteseramaceitasporconteremuma String
vazia.
220
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 237

ParteIII
Desenvolvendoafluência
Apósconhecerofuncionamentodasferramentascomquetemostrabal-
hado,éhoradedesenvolvernossafluência.Nessapartefinal,vamosrefinar
nossaaplica çãoeexplorarconceitosetécnicasimportantesdecomponenti-
zaçãoeperformance.
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 238

E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 239

Capítulo9
Enriquecendonossaaplica ção
JSF
Naprimeirapartedesselivronósvimoscomoconstruirumasimplesapli-
caçãointegrandoJSFeJPA.Jánasegundapartevimosmaissobrecomocada
frameworkfunciona.Agorairemosenriqueceraaplica çãocriadanaprimeira
parteusandooqueaprendemosnasegundaeacrescentandonovoselementos
aela.
Continuaremosusandoomodeloapresentadonocapítulo6,evocêpode
relembrá-lonafigura9.1.
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 240

9.1. CombosemcascataecommandsemdataTable CasadoCódigo
Fig.9.1:Modelodeclassesusadonessecapítulo
Apartirdeagora,usaremosalgunscomponentesdabiblioteca Primefaces,
quevocêencontraemhttp://primefaces.org/,paraapresentarcenáriosreais,
ondepoderíamosficarlimitadosseutilizássemososcomponentesdoJSF.
9.1 Combos em cascata e commands em data T-
able
Vocêdeveternotadoquecitamoscombosemcascataemoutraspartesdeste
livro,masoquefazdesseexemplotãoimportante?Primeiramente,vamosver
comoficouseucódigo,eapartirdelediscutiremosasdiferen çasqueteríamos
nocomportamentodaaplica çãodependendodoescopoqueescolhêssemos.
Fig.9.2:TeladecadastrodeAutomovelcomcombosinterdependentes
224
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 241

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
Primeiramente vejamos como ficou a nova versão da entidade
Automovel.
@Entity
public class Automovel {
@Id @GeneratedValue
private Long id;
@ManyToOne
private Modelo modelo;
private Integer anoFabricacao;
private Integer anoModelo;
private Double preco;
private Double kilometragem;
private String observacoes;
}
Aclasse AutomovelBean,tevecomoaltera çãoapenasoescopo,eain-
clusãodeumapropriedadedotipo Marcaqueguardaaescolhadousuário
que servir de filtro para os modelos. Como podemos ver, na entidade
Automovelguardamosapenaso Modelo,enãoa Marca. Issoporquea
partirdo Modeloacessamosa Marca.
@ManagedBean
@ViewScoped
public class AutomovelBean {
private Automovel automovel = new Automovel();
private List<Automovel> automoveis;
private Marca marca; // utilitário para buscar os modelos
// getters, setters e método salvar
}
Pormaisquenossoobjeto Automovelestejamaisrico,oprocessode
manipulá-lonãomuda:pontoparaaOrienta çãoaObjetos.Aseguirveremos
ocódigodatela.
225
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 242

9.1. CombosemcascataecommandsemdataTable CasadoCódigo
<h:form>
<h:messages />
<h:panelGrid columns="2">
Marca:
<h:selectOneMenu label="marca"
value="#{automovelBean.marca}"
required="true" converter="entityConverter">
<f:selectItem itemLabel="-- Selecione --"
noSelectionOption="true" />
<f:selectItems value="#{marcaBean.marcas}"
var="marca"
itemValue="#{marca}"
itemLabel="#{marca.nome}" />
<f:ajax render="selectModelo" />
</h:selectOneMenu>
Modelo:
<h:selectOneMenu id="selectModelo" label="modelo"
value="#{automovelBean.automovel.modelo}"
required="true"
converter="entityConverter">
<f:selectItem itemLabel="-- Selecione --"
noSelectionOption="true" />
<f:selectItems
value="#{automovelBean.marca.modelos}"
var="modelo" itemValue="#{modelo}"
itemLabel="#{modelo.descricao}" />
</h:selectOneMenu>
Ano de Fabricação:
<h:inputText
value="#{automovelBean.automovel.anoFabricacao}" />
Ano do Modelo:
<h:inputText
226
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 243

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
value="#{automovelBean.automovel.anoModelo}" />
Preço:
<h:inputText
value="#{automovelBean.automovel.preco}" />
Kilometragem:
<h:inputText
value="#{automovelBean.automovel.kilometragem}" />
Observações:
<h:inputTextarea
value="#{automovelBean.automovel.observacoes}" />
</h:panelGrid>
<h:commandButton value="Salvar"
action="#{automovelBean.salvar(auto)}" />
</h:form>
Nessecódigo,declaramosdois combos,umparaasmarcaseooutropara
osmodelos. Emambososcasos,temosum selectItemcoma label“
-- Selecione -- ”apenasparaessamensagemvirnaprimeiralinhado
combo. Noteapresen çadapropriedade noSelectionOption="true"
indicandoqueessaop çãonãoéselecionável.Ouseja,casoousuáriosubmeta
oformuláriocomessaop ção,seráconsideradoumvalor null.
Nocombodemarcas,usamosumoutro Managed Beandeapoiopara
nosdevolveralistade Marcas. Ométodo getMarcasdo MarcaBean,
queéchamadopormeiodaexpressão #{marcaBean.marcas},simples-
mentedevolveumalistade Marcasqueestiveremcadastradas.Norestante
oformatodessecombosegueomesmopadrãoquefoiapresentadonocapí-
tulo7,tantonoseufuncionamentoquantonousodoconversorgenéricode
entidades. Adiferençarecaisobreocomponente f:ajax. Porhorabasta
sabermosqueelemudaráovalordocombodemarcaseirárecarregarocom-
ponentecomid selectModelo,quenocasoéocombode Modelos.Na
seção9.4entenderemoscomotrabalharcomrequisi çõesAJAXnoJSF.
Analisando o combo de modelos, percebemos que precisamos de
um escopo que mantenha o automovelBean entre as requisições.
227
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 244

9.1. CombosemcascataecommandsemdataTable CasadoCódigo
Isso se deve ao fato de os elementos do combo de modelos depen-
derem diretamente do valor do combo de marcas. Veja como o
value do combo de marcas, #{automovelBean.marca}, serve de
entrada para o value do f:selectItems do combo de modelos:
#{automovelBean.marca.modelos}.
Considerandoqueo AutomovelBeanestivessecomescopo request,a
cadarequisi çãooJSFseesqueceriadesse bean,entãoacadaumaoJSFacharia
queéaprimeirarequisi çãoqueestariasendoenviada,oqueéerrado.
Fig.9.3:Sequênciadecomboemcascataqueterminaemerro
1) OusuáriosolicitaatelaeoJSFcriaaárvoredecomponentesquepos-
sui o combo de marcas preenchido e devolve para o usuário. Mas
o combo de modelos não tem nenhuma opção, afinal, a propriedade
#{automovelBean.marca}é null;
2) OusuárioselecionaamarcaeviaAJAXéfeitaumasolicita çãoparaocar-
regamentodosmodelos. OJSFrecriaaárvoredecomponentese,como
ousuárioenviouumamarcaválida,ouseja,queestavanasop çõesdo
combo,entãooJSFaceitaasolicita çãoedevolveocombodemodelos
preenchido;
3) O usuário seleciona o modelo e preenche os demais campos. Con-
siderandoquetodososoutroscampospreenchidossejamválidos,oprob-
lemarecaisobreovalorinformadonocombodemodelos.Comonosso
228
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 245

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
beanestánoescopo request,oJSFvaisecomportardamesmaformaque
nasegundarequisi ção.
Como o #{automovelBean}que guardava a marca selecionada foi
removido da memória devido a seu escopo ter acabado, um novo
AutomovelBeansemumamarcaselecionadaécriado.OJSFconsidera
quecomoamarcanãofoiselecionada,nãoteriacomoocombodemode-
lospossuirqualquerop çãoalémda“-- Selecione -- ”,assimsendo,
ovalorémarcadocomoinválido.
Apesar desse cenário ser facilmente resolvido no JSF com o uso
@ViewScoped,muitosprojetosaindautilizamJSF1.X,emqueelenãoex-
iste. Emesmoquemcome çarhojecomJSFenuncavenhaatrabalharcom
comumaversãomaisantigadoframeworkvaiprecisardecidirqualescopo
utilizaremcada Managed Bean.Aindica çãoésempreusaromenorescopo
possível,que,dentreasop çõesquetemos,éa request.Entãomesmoemum
projetonovoteremosquesaberquandousaroescopo viewemvezde request.
9.2 Mostre mensagens com h :message e
h:messages
Nase ção7.38criamosvalidadorescustomizados,enosexemplosapresenta-
dosnósgeramosumainstânciade FacesMessageelan çamosumaexce ção
comessamensagemdentro. Emoutrospontosdaaplica çãopodemoscriar
mensagens,porexemplo,parainformarqueaopera çãofoiefetuadacom
sucesso. Emtodosessescasos,oJSFprecisadeumcomponentequeasex-
ibaparaousuário.Casonãoexistanenhumcomponentecapazdeexibiressa
mensagem,oJSFacolocanoconsolejuntamentecomoavisoqueatelanão
aestáexibindo,paraqueodesenvolvedorpossaperceberecorrigiroerro.
Percebemos,noentanto,queemvezdeum,oJSFoferecedoiscompo-
nentesparaomesmofim. Ocódigoaseguirservirádebaseparaosdois
componentesdemensagem.
<h:form id="formAutomovel">
Todas as mensagens: <br/>
<h:messages/>
229
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 246

9.2. Mostremensagenscomh:messageeh:messages CasadoCódigo
<hr/>
Apenas mensagens globais: <br/>
<h:messages globalOnly="true"/>
<hr/>
Ano de Fabricação:
<h:inputText
value="#{automovelBean.automovel.anoFabricacao}">
<f:validateLongRange minimum="1950" maximum="2012"/>
</h:inputText>
Ano do Modelo:
<h:inputText id="anoModelo"
value="#{automovelBean.automovel.anoModelo}">
<f:validateLongRange minimum="1950" maximum="2013"/>
</h:inputText>
<h:message for="anoModelo"/>
Preço:
<h:inputText value="#{automovelBean.automovel.preco}" />
Kilometragem:
<h:inputText
value="#{automovelBean.automovel.kilometragem}" />
Observações:
<h:inputTextarea
value="#{automovelBean.automovel.observacoes}" />
</h:form>
O h:messagepossui a propriedadeforque o liga aoidde al-
gumcomponentequepossagerarumamensagem-noexemploéocom-
ponente anoModelo.Dessamaneira,qualquermensagem,sejadeconver-
são,valida ção,oumesmogeradapelaaplica ção,quesejaespecíficaparaesse
h:inputText,seráexibidano h:message.
Jáocomponente h:messagesnãotemvínculocomnenhumcompo-
230
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 247

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
nenteespecífico. Eleexibetodasasmensagensgeradasparaqualquercom-
ponente,oumesmomensagensglobais,quenãosãoendere çadasparaum
componenteespecífico.
Utilizamoslogonocome çoum h:messagesexibindoqualquermen-
sagemgeradanaúltimarequisi çãodousuário,mesmoqueelatambémseja
exibidaporumcomponente h:messageespecífico. Issopodecausarum
inconveniente,porqueamesmamensagemapareceduasvezes.Pararesolver
esseproblemaexisteapropriedade globalOnlydo h:messages,indi-
candoqueapenasasmensagensglobaisserãoexibidas.
Diferenciandomensagensglobaisdemensagensespecíficas
Umamensagemglobaléaquelaquenãoégeradaparaumcomponente
específico.Porexemplo,umerrodeconversãoouvalida çãoestárelacionado
comumcomponente,entãonãoéumamensagemglobal.Agoraumamen-
sagemdesucessooufalhaaosalvarum Automovelnobancodedadosnão
costumaserrelacionadacomobotãoquefoiacionadoparaefetuaraoper-
ação.Geralmenteessamensagemnãoficavinculadaanenhumcomponente,
sendo,portanto,umamensagemglobal.
FacesMessage msg =
new FacesMessage("Automovel salvo com sucesso!");
FacesContext.getCurrentInstance().addMessage(null, msg);
Nesse código temos a criação de uma mensagem global, já
que, ao adicionar a mensagem ao contexto to JSF através de
FacesContext.getCurrentInstance,passamos nullparaoprimeiro
parâmetro, noqualiriao iddocomponenteaquemessamensagemse
destina.
Masvamossuporquevamoscriarumamensagemparaocomponente
comid“anoModelo”.
FacesMessage msg =
new FacesMessage("Ano modelo informado é inválido");
FacesContext.getCurrentInstance()
.addMessage("formAutomovel:anoModelo", msg);
231
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 248

9.2. Mostremensagenscomh:messageeh:messages CasadoCódigo
Umdetalheincômodoquenotamosaquiéque,quandoreferenciamos
umobjetodentrodoXHTML,namaioriadasvezesbastacolocarmoso id
dele.Porém,quandoreferenciamosumobjetodentrodonossocódigoJava,
geralmentetemosquereferenciaro clientId.O clientIdéo idquevai
paraoHTMLgerado,queéoqueo client,ousejaonavegador,recebe.Por
issoonome clientId.
Jásabemoscomocriarumamensagemglobaleumamensagemespecí-
ficaparaumcomponente,mascomoapresentarissodamelhorformapara
ousuário?Umbompontodepartidaédefinirmosseteremoscomponentes
h:messagededicadosparacadacomponente,oupelomenosparaaqueles
quesabemosquedevemgerarmensagens,ouaindaseteremosumlocalna
páginaquemostrarátodasasmensagensdatela.
Parailustrarmelhoroproblema,vamosexecutaratelaapresentadano
iníciodase ção.
Fig.9.4:Errosdevalida ção
Analisandooresultado,percebemosquetantoocampo“anodefabri-
cação”quantoo“anomodelo”apresentaramerrodevalidação.Comoo“ano
modelo”temumcomponenteespecíficoparaele,amensagemsaiunosdois
componentes.Jáocomponente h:messagesquemostraapenasmensagens
globaisnãomostroumensagemalguma,porquenossométododenegócio
nemchegouaexecutar.
232
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 249

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
Colocandolabelsemensagenscustomizadasparaerrosdeconver-
sãoevalida ção
Certamenteum“detalhe”nãopassoudespercebido,queéonomees-
tranhodadoaocomponente“anodefabricação”.Issoaconteceporque,difer-
entedo“anomodelo”,nãodemosumidparaocomponente.Atribuir ids
émuitoimportantequandoformostrabalharcomAJAX,masaindanãoéo
maisamigávelparamensagensdousuário,apesardesermelhormostrarum
idatribuídopornósdoqueumgeradopeloJSF.
Pararesolveresseproblema,temosalgumasalternativas.Amaissimples
ediretaéutilizarapropriedade labeldisponívelemqualquercomponente
deentradadoJSF.Comisso,emvezdeusaro id,oJSFusaráa labelpara
identificarocomponentequandoacontecerumerro.
<h:form id="formAutomovel" prependId="false">
...
Ano de Fabricação:
<h:inputText label="Ano de fabricação"
value="#{automovelBean.automovel.anoFabricacao}">
<f:validateLongRange minimum="1950" maximum="2012"/>
</h:inputText>
Ano do Modelo:
<h:inputText id="anoModelo" label="Ano do modelo"
value="#{automovelBean.automovel.anoModelo}">
<f:validateLongRange minimum="1950" maximum="2013"/>
</h:inputText>
<h:message for="anoModelo"/>
Preço:
<h:inputText label="Preço"
value="#{automovelBean.automovel.preco}" />
Kilometragem:
<h:inputText label="Kilometragem"
value="#{automovelBean.automovel.kilometragem}" />
Observações:
233
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 250

9.2. Mostremensagenscomh:messageeh:messages CasadoCódigo
<h:inputTextarea label="Observações"
value="#{automovelBean.automovel.observacoes}" />
</h:form>
Agora,executandonovamenteatelaefor çandoomesmoerroteríamoso
resultadoaseguir.
Fig.9.5:Errosdevalida çãousandolabels
Avantagemdeusarmos labeléqueelafuncionatantoparaerrosdeval-
idaçãoquantodeconversão.Dentrodeerrosdevalida ção,podemosterum
valorforadointervaloválidoounãoinformarumcamporequerido,porex-
emplo.Masseoquedesejarmosforcolocarumamensagemespecíficanossa,
temosalgumasformasdeofazer.Podemostrocaramensagempadrãoqueo
JSFusaparaasmensagens,quejátemsuporteaportuguêsdoBrasil,ouentão
especificarumamensagemdiferentesomenteparaumcomponente.
Abordaremosagoraasegundaop ção,queéespecificarumamensagem
exataparaoquepodeacontecercomaquelecomponente. Paraisso,pre-
cisamosbasicamentede3atributos:
•converterMessage:noqualpodemosespecificarparaumdetermi-
nadocomponentequemensagemqueremosqueapare çacasoocorra
umerrodeconversão.
•requiredMessage:noqualpodemosespecificarparaumdetermi-
nadocomponentequemensagemqueremosqueapare çaquandoo
campoéobrigatóriomasnãofoiinformado.
234
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 251

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
•validatorMessage:noqualpodemosespecificarparaumdetermi-
nadocomponentequemensagemqueremosqueapare çacasoocorra
umerrodevalida ção.
FazendoumapanhadogeralsobrecomooJSFmontaamensagempara
ousuário,temosaseguintesequência:
1) OJSFverificaseexisteumamensagemespecíficaparaoerroqueestá
sendogerado:conversão,camporequeridoouvalida ção;
2) Nãohavendoumamensagemespecífica,oJSFgeraamensagempadrão
identificandoocomponenteatravésdasuapropriedade label;
3) Casonãotenhaum labelespecificadoparaocomponente,oJSFusaseu
id,quepodetersidoespecificadopelodesenvolvedor,ouaindagerado
automaticamentepeloJSF.Nesseúltimocaso,amensagemdificilmente
ajudaráousuáriodosistema.
MasesequisermosmudarasmensagenspadrõesdoJSF?
9.3 Internacionalizando nossa aplicação
Ainternacionaliza çãodeumaaplica çãoconsisteemdeixarseustextosde
acordocomoidiomadousuário. OJSFemsijáédessaforma,tendoin-
clusivesuporteaportuguêsdoBrasil.Issosignificaquetodasasmensagens
doJSFestãoemarquivodepropriedades,oquenosdáumaop çãoamaisde
customizá-las.
Porexemplo,paramudaramensagemdecamporequeridodoJSFprecis-
aríamoscriarumarquivochamado Messages_pt_BR.propertiesden-
trodeumpacotechamado javax.facesenessearquivocolocarumvalor
paraachave javax.faces.component.UIInput.REQUIRED.
javax.faces.component.UIInput.REQUIRED =
Campo obrigatório. Informe-o!
Comisso,todasasmensagensdecamporequeridopassariamausaro
textoquenósinformamos,enãootextopadrãodoJSF.
235
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 252

9.3. Internacionalizandonossaaplicação CasadoCódigo
Podemostambéminternacionalizarasmensagensqueusamostantoden-
trodonossocódigoJava,comodo xhtml.Primeiro,nósosdeclaramosum
novoarquivodemensagensno faces-config.xmleousamosemtodaa
aplicação.
<application>
...
<resource-bundle>
<base-name>facesmotors.messages.Mensagens</base-name>
<var>msgs</var>
</resource-bundle>
</application>
Eagora,considereateladecadastrodoautomóvel,quepossuidiversas
mensagensespalhadasporela:
Ano de Fabricação:
<h:inputText label="Ano de fabricação"
value="#{automovelBean.automovel.anoFabricacao}"/>
Ano do Modelo:
<h:inputText label="Ano do modelo"
value="#{automovelBean.automovel.anoModelo}"/>
Preço:
<h:inputText label="Preço"
value="#{automovelBean.automovel.preco}" />
Umadaspossibilidadesdeinternacionalizaressetrechodecódigoseria
conformeocódigoaseguir.
#{msgs.label_ano_fabricacao}:
<h:inputText label="#{msgs.label_ano_fabricacao}"
value="#{automovelBean.automovel.anoFabricacao}"/>
#{msgs.label_ano_modelo}:
<h:inputText label="#{msgs.label_ano_modelo}"
value="#{automovelBean.automovel.anoModelo}"/>
236
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 253

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
#{msgs.label_preco}:
<h:inputText label="#{msgs.label_preco}"
value="#{automovelBean.automovel..preco}" />
Todosostextosqueantesestavamliteraisdentrodo xhtmlforamextraí-
dosparaumarquivochamado Mensagens_pt_BR.properties,queestá
dentrodopacote facesmotors.messages.Oconteúdodessearquivoéo
seguinte:
label_ano_fabricacao = Ano de Fabricação
label_ano_modelo = Ano do Modelo
label_preco = Preço
label_km = Kilometragem
label_obs = Observações
Depoisqueregistramosavariável msgsno faces-config.xml,pode-
mosusá-laemqualquerlugardaaplica ção. Alémdisso,podemosdeclarar
váriasocorrênciasde resource-bundledentrodatag application,
permitindoqueexistamaisdeumarquivodemensagens.
Éimportantenotarmostambémque,apesardonomecompletodoar-
quivoser facesmotors.messages.Mensagens_pt_BR.properties,
dentro do Java esse arquivo é tratado apenas como
facesmotors.messages.Mensagens. Aextensãoédesconsiderada,eo
sufixo pt_BRserveparaindicaroidiomadoarquivo.
Senossaaplica çãodevesuportarmaisdeumidioma,versõesalterna-
tivasdoarquivodemensagemdevemsercriadas. Porexemplo,paracri-
armosumaversãodessemesmoarquivoeminglês,deveríamosdar-lheo
nomede facesmotors.messages.Mensagens_en.properties;ese
fossealgoespecíficoparaoinglêsamericano,oarquivodeveriasechamar
facesmotors.messages.Mensagens_en_US.properties.
Internacionalizaçãoalémdoslabels
Nase ção9.2,vimoscomomelhorarasmensagensapresentadasparao
usuário. Vimosqueumaformademelhoraraindica çãodequalocampo
queapresentoualgumerroécomousodapropriedade labelpresentenos
237
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 254

9.3. Internacionalizandonossaaplicação CasadoCódigo
componentesdeinputemgeral. Inclusivenoexemploquevimosdeinter-
nacionalizaçãoessapropriedadeestavasendousada. Masalémda label,
vimosquetemospropriedadesmaisespecíficas,nasquaispodemoscolocar
mensagensparaseremusadasemcasosdeerrodevalida ção,conversãooude
camporequerido.
#{msgs.label_preco}:
<h:inputText label="#{msgs.label_preco}"
value="#{auto.preco}"
converterMessage="O preço deve ser numérico" />
Observandoesseexemplo, nemprecisavaserditoquepodemostam-
bém passar esse tipo de mensagem para um arquivo de propriedades.
OJSFaceita Expression Language empraticamentequalquerpropriedade
deseuscomponentes, eo converterMessage, requiredMessagee
validatorMessagenãosãodiferentes. Comoomecanismodecarrega-
mentode bundlesnosdisponibilizaumavariávelacessívelvia Expression Lan-
guage,entãopodemosusá-laedeixarnossoexemplodaseguinteforma:
#{msgs.label_preco}:
<h:inputText label="#{msgs.label_preco}"
value="#{auto.preco}"
converterMessage="#{msgs.converter_preco}" />
Eagora,temosaatualiza çãodoarquivo .properties.
#======= labels do formulário de automovel =========
label_ano_fabricacao = Ano de Fabricação
label_ano_modelo = Ano do Modelo
label_preco = Preço
label_km = Kilometragem
label_obs = Observações
#===== messages customizadas do formulário de automovel =======
converter_preco =
O preço do automóvel deve ser numérico (ex: 50000)
238
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 255

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
9.4 JSF eAjax
OsuporteaAJAXdoJSFéalgobeminteressante.Noexemploaseguirvere-
moscomotrabalharcomcombosemcascata,masoprincípioéomesmodo
queseestivéssemosatualizandoqualqueroutrotipodecomponente.
Marca:
<h:selectOneMenu label="marca" value="#{automovelBean.marca}"
required="true" converter="entityConverter">
<f:selectItem itemLabel="-- Selecione --"
noSelectionOption="true" />
<f:selectItems value="#{marcaBean.marcas}" var="marca"
itemValue="#{marca}" itemLabel="#{marca.nome}" />
<f:ajax render="selectModelo" />
</h:selectOneMenu>
Modelo:
<h:selectOneMenu id="selectModelo" label="modelo"
value="#{automovelBean.automovel.modelo}"
required="true" converter="entityConverter">
<f:selectItem itemLabel="-- Selecione --"
noSelectionOption="true" />
<f:selectItems value="#{automovelBean.marca.modelos}"
var="modelo" itemValue="#{modelo}"
itemLabel="#{modelo.descricao}" />
</h:selectOneMenu>
...
Vamosanalisaroquedesejamosqueaconte çanesseexemplo.Temosum
comboquelistatodasas Marcasdeautomóveise,abaixo,outroquelista
todosos Modelosda Marcaselecionadanocombodecima.Mudandoode
cima,odebaixoérecarregado.Apenaspararecordarmos,nossomodeloestá
comonaseguintelistagem:
public class Marca {
...
private List<Modelo> modelos;
...
239
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 256

9.4. JSFeAjax CasadoCódigo
}
public class Modelo {
...
private Marca montadora;
...
}
DesconsideramosnessalistagemosmapeamentosdaJPAeoutraspro-
priedades das classes. O ponto importante é que aMarcapossui uma
listagemde Modelos.Comoomapeamentoobjetorelacionaljáfoifeito,não
precisamosnospreocuparcomcomoalistagemde Modeloserácarregada;
oqueimportaéque,umavezquetemosa Marcaemmãos,bastaacessarmos
apropriedade modeloseosobjetosestarãolá.
Observandoo xhtml,vemosqueocombode Modelosimplesmente
acessaapropriedade modelosda Marcaselecionada. NoManaged Bean
automovelBean,nãoexistenenhumcódigoextraparabuscar,apenasuma
propriedadedotipo Marcaqueestásendoalimentadapeloprimeirocombo.
Umavezqueessadependênciaestátodaconfigurada,bastaatualizarmoso
comboinferiorquandoodecimamudar,quenaturalmentealistagemde
Modelosseráatualizadaquandomudarmosa Marca.
Porém,paraumamelhorexperiênciadousuário,emvezdesubmetermos
atelainteiratodavezqueocombode Marcamudar,nóssimplesmenteman-
damosoJSFrenderizarnovamenteocombodebaixo.Parafazerissobastou
incluirocomando:
<f:ajax render="selectModelo" />
Dessaforma,indicamoso iddocomponentequequeremosatualizar.
Jávimosquenãoprecisamosfazerbuscaalgumapelosobjetosdocombo
de Modelo,eagoravemosquetambémnãoprecisamosfazernadaparaatu-
alizarositensdocombo.IssoacontecedessamaneiraporqueoJSFconhece
atela,elesabeondeo f:selectItemsestábuscandooselementos,então
saberenderizarnovamenteapenasotrechodaárvoredecomponentesque
solicitamos-queéasubárvoreabaixodo selectModeloqueinformamos
napropriedade renderdo f:ajax.
240
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 257

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
Alémdatag f:ajax,osuporteaAJAXdoJSFtemumapequenabib-
lioteca javascriptquerecebeoHTMLresultantedessanovarenderiza çãoe,
apartirdo iddoelemento,viaDOM( Document Object Model),substituio
conteúdoantigopelonovo.
Podemosimaginarumfuncionamentoparecido,setivéssemosnumatela
umbotãoqueincluísseumelementoaumalistausadaparaalimentarum
h:dataTable.Paraexemplificar,vamosconsiderarumainclusãoemmassa
de Marca,quenonossomodelotemapenasumadescri ção.
...
<h:commandButton value="Adicionar Marca"
action="#{marcaBean.addMarca}">
<f:ajax render="tabelaMarcas"/>
</h:commandButton>
<h:dataTable id="tabelaMarcas"
value="#{marcaBean.marcasParaIncluir}"
var="marca">
<h:column><h:inputText value="#{marca.nome}"/></h:column>
</h:dataTable>
...
@ManagedBean
@ViewScoped
public class MarcaBean {
...
private List<Marca> marcasParaIncluir = new ArrayList<>();
public void addMarca(){
marcasParaIncluir.add(new Marca());
}
// getter para a propriedade marcasParaIncluir
...
}
241
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 258

9.4. JSFeAjax CasadoCódigo
Fig.9.6:Cria çãodemarcaemlote
Novamente,precisamosapenasexecutarnossaa ção,queaquiéaadi ção
deumelementoemumalista,emandaroJSFrenderizarnovamenteaparte
datelaquequeremosatualizarviaAJAX.OrestooJSFfaz.
Propriedadessuportadas
Atéagoravimossomenteapropriedade render,masatag f:ajax
possuioutraspropriedadesimportantes:
•event: ÉoeventoDOMquequeremosusarparadispararaa ção
AJAX.Ovalorpadrãodessapropriedadeé clickparalinksebotões,
e changeparacomponentesdeentradadedados. Existetambémo
evento blur,quandoumcomponenteperdeofoco.
Sequisermosmudaroeventopadrãodediversoscomponentes, ao
mesmotempoemquedeixamostodoselescomsuporteaAJAX,pode-
mosfazeroseguinte:
...
<f:ajax event="keyup">
Ano de Fabricação:
<h:inputText value="#{auto.anoFabricacao}"/>
Ano do Modelo:
<h:inputText value="#{auto.anoModelo}"/>
</f:ajax>
...
242
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 259

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
Nessecaso,acadateclaqueousuáriodigitaremqualquerumdos
h:inputText será feita uma requisição e o componente terá seu
valoratualizadoservidor,masnenhumresultadoserápercebidonatela
porquenãomandamosatualizarnadacomapropriedade render.
AlémdoseventosDOM,temosdoiseventos“artificiais”adicionados
peloJSF:o action,quepodeserusadoemcomponentesdea çãocomo
h:commandButtone h:commandLinkeo valueChangequepode
serusadoemqualquercomponentedeentradadedados.
•render: Essaéapropriedademaiscomumdeseusarquandotra-
balhamoscomAJAXnoJSF.Atravésdela,informamosasubárvore,
ousubárvoresquedevemserrenderizadasnovamenteparaatualizar
atela. Cada idouconstanteinformadanapropriedade render
dáorigemaumasubárvorenova,contendoocomponenteinformado
etodososcomponentesabaixodeste. Sendoassim,setivermosum
h:panelGridou h:panelGroupnalistaaserrenderizada,nãopre-
cisamosinformaro iddenenhumcomponentequeestiverdentro
desses containers,porquetodosjáserãoautomaticamenteatualizados.
•execute:Atravésdessapropriedade,informamosqualsubárvoredeve
sersubmetidaaoservidorparaqueoJSFprocesse.Essaárvorenãoéa
mesmaqueiráserrenderizadanovamentepelapropriedade render.
•listener: Assim como umaaction do JSF pode teraction lis-
teners associada, uma requisição AJAX também pode ter um
listener. Para isso basta ligarmos a propriedadelistener com
ummétodocomaseguinteassinatura: public void <nome do
método>(javax.faces.event.AjaxBehaviorEvent event)
throws javax.faces.event.AbortProcessingException.
Noexemplodeedi çãoemlotede Marcas,pegamosumobjetoembranco,
ouseja,logoapósdarum newnele,eoadicionamosnatabela,queeraed-
itável. Assim,ousuáriopodiamodificarosvaloresdiretamentededentro
damesma.Agoravamosmudarumpoucooexemploparafazercomqueo
preenchimentodoobjetosejafeitoantesdeadicionarmosnatabela.Oresul-
tadoseriacomooquepodemosveraseguir.
243
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 260

9.4. JSFeAjax CasadoCódigo
...
Nova Marca:
<h:inputText id="novaMarca"
value="#{marcaBean.novaMarca.descricao}"/>
<h:commandButton value="Adicionar Marca"
action="#{marcaBean.addMarca}">
<f:ajax execute="novaMarca"
render="tabelaMarcas novaMarca"/>
</h:commandButton>
<h:dataTable id="tabelaMarcas"
value="#{marcaBean.marcasParaIncluir}" var="marca">
<h:column>#{marca.nome}</h:column>
</h:dataTable>
...
@ManagedBean
@ViewScoped
public class MarcaBean {
...
private Marca novaMarca = new Marca();
private List<Marca> marcasParaIncluir = new ArrayList<>();
public void addMarca(){
marcasParaIncluir.add(novaMarca);
novaMarca = new Marca();
}
//getter e setters
...
}
244
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 261

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
Fig.9.7:Cria çãodemarcaemlote
A mudança no código não foi tão significativa. Agora temos um
inputantesdobotão“AdicionarMarca”,enquantonatabelatemossomente
output.Amudan çamaisimportanteparanósnessemomentoéainclusão
dapropriedade execute.
Paraquepossamosatualizaratabelacomonovovalorpreenchido,pre-
cisamosqueoJSFrecebanoservidoroconteúdodo h:inputTextcom
id="novaMarca". Porpadrão,ocomponentequefazarequisi çãoAJAX,
quenonossocasoéobotão,sóenviaelemesmoparaoservidor. Dessa
forma,semespecificarmoso iddo h:inputTextquetinhaainforma ção
necessária,oJSFatéiriaprocessararequisi ção,masnãoatualizariaovalor
do inputporqueelenãoteriasidosubmetido.
Alémdo iddo input,no executeestáimplícitooenviode @this.
Essevaloréumaconstantequerepresentaoprópriocomponentequeestá
originandoarequisi çãoAJAX.
Percebemosquenapropriedade render,informamoso iddo input
noqualéinformadoonomeda Marca.Issoénecessárioparaqueomesmo
sejalimpadoautomaticamente,refletindooefeitodo Managed Bean,onde
criamosuma Marcanova.
Tantoapropriedade executequantoa renderaceitamasconstantes:
•@this: usadaparareferenciaroprópriocomponentequeestáorigi-
nandoarequisi çãoAJAX;
•@form:usadaparareferenciartodooformulárioqueestáemvoltado
componentequeestáoriginandoarequisi çãoAJAX;
•@all:usadaparareferenciartodaaviewdoJSF;
245
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 262

9.5. Organizeocódigodastelascomtemplates CasadoCódigo
•@none:usadaparainformarquenenhumaárvoredeveserprocessada.
9.5 Organize o código das telas com templates
UmadasprincipaisnovidadesdoJSF2foiaincorpora çãodoFaceletsnaes-
pecificação. Essajáeraumaferramentaindispensávelmesmoquandoera
umframeworkseparado,sendousadotantoparaaplicarmos templatesna
aplicação,quantoparaconstruirmoscomponentescompondooutroscom-
ponentes.
Autiliza çãode templatesfacilitaapadroniza çãodaaplica ção,jáquecon-
seguimosdeixarfixotudoaquiloqueraramentemuda,comotopo,rodapée
menulateraldaspáginas,bemcomoinformarsomenteapartequemuda,que
geralmenteéomeiodapágina.Esse layoutqueacabamosdedescreverpode
serilustradopelafigura9.8.
Fig.9.8:Exemplodeorganiza çãodeumtemplate
Definaotemplate
Adefini çãodotemplateéumtrabalhobemparecidocomodaconstru ção
deumapáginacomum.Adiferen çaéqueinserimosnessapáginasalgumas
246
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 263

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
marcações,indicandoondeoconteúdodinâmicoseráinserido.Nocódigoa
seguir,temosumexemplodessasdefini ções.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core"
xmlns:ui="http://java.sun.com/jsf/facelets">
<h:head>
<title>
<ui:insert name="pageTitle">Faces Motors</ui:insert>
</title>
<h:outputStylesheet library="css" name="template.css" />
</h:head>
<h:body>
<div id="topo">
<ui:insert name="topo">
<ui:include src="/WEB-INF/comuns/topo.xhtml"/>
</ui:insert>
</div>
<div id="menu">
<ui:include src="/WEB-INF/comuns/menu.xhtml"/>
</div>
<div id="body">
<ui:insert name="body"/>
</div>
<div id="rodape">
<ui:include src="/WEB-INF/comuns/rodape.xhtml"/>
</div>
</h:body>
</html>
Notemplateapresentado,definimosquatrose ções: topo, menu, bodye
rodape.Aorganiza çãonatelaseráfeitaviaCSS,masparanósoqueimporta
écomocadaáreadessaserápreenchida. Nadefini çãodotemplateusamos
basicamenteduastags: ui:inserte ui:include.
Abraespa çocomoui:insert
Usamos ui:insertquandoqueremosdefiniropontodotemplateonde
247
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 264

9.5. Organizeocódigodastelascomtemplates CasadoCódigo
seráinseridoumconteúdoprovenientedapáginacliente,ouseja,dapágina
queusaotemplate.Temosapenasapropriedade nameparapodermosrefer-
enciaressaáreaeditáveldentrodapáginacliente.
Comopodemosobservar,definimosasáreas pageTitlee topojácom
umconteúdopadrãoassociado.Issoquerdizerquecasoapáginaclientenão
informeumvalorparaessasáreas,elasapresentarãoosvaloresespecificados
nopróprio template. Depoisfizemosadefini çãodo body,queéondevai
ocorpodapáginapropriamentedito. Nessecasonãotemosumconteúdo
padrão.
Incluaconteúdocomoui:include
Atag ui:includeéusadaquandoqueremosincluiroconteúdodeuma
páginadentrodeoutra. Nonossoexemplo,usamosessatagparadefiniro
conteúdopadrãodasse çõesdo templatequecriamos.
A página em execução não é o template , e sim a página
cliente
Algoimportantequetemosqueaprendersobreousodetemplates
équeelesnãoexistemporsisó. Nuncateremosum templateexecu-
tando,afinaleleéumapáginaincompleta. Atémesmoporisso,éuma
boapráticacolocarmosos templateseaspáginasqueeleincluidentroda
pasta WEB-INF,paraqueousuárionãoconsigaacessá-lasdiretamente.
Setentarmosescreveronomedapáginasendoprocessada,nãosairá
onomedo template,esimonomedapáginacliente.Sendoassim,temos
quetomarcuidadoaousarmoscaminhosrelativosdentrodo template,
porqueessescaminhosserãorelativosnãoaele,esimàpáginacliente.
Porisso,notemplateapresentadousamoscaminhosabsolutos.
Componhaostemplates
Umavezquetemoso templatedefinido,sobraparacadapáginadanossa
aplicaçãousá-lo.
248
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 265

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://java.sun.com/jsf/facelets"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
Posso colocar qualquer coisa antes...
<ui:composition template="/WEB-INF/comuns/template.xhtml">
<ui:define name="body">
Conteúdo da página
</ui:define>
</ui:composition>
Ou depois da ui:composition, mas tudo será ignorado
</html>
Aformamaiscomumdedefinirumapáginaqueusaumtemplateé
criá-lanormalmente, usandoatag htmleemseguidadeterminaratag
ui:compositionqueindicaotemplatequeestásendousado.Apesardeser
umaop çãoválida,comoestáescritonocódigoanterior,tudoquefordefinido
foradatag ui:compositionseráignorado. Naprática,apáginacomeça
eterminajuntocomatag ui:compositionenãocomatag htmlcomo
geralmenteacontecequandonãousamos templatealgum.
Poressemotivo,umaformadiferentededefiniramesmapáginapodeser
vistaaseguir.
<ui:composition xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://java.sun.com/jsf/facelets"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core"
template="/WEB-INF/comuns/template.xhtml">
<ui:define name="body">
Conteúdo da página
</ui:define>
</ui:composition>
Agorajáiniciamosnossapáginacomatag ui:composition,elimi-
nandoassimapossibilidadedealguémdefinirporenganoalgumconteúdo
queseráignorado,vistoqueaprópriatagagoradelimitaonossoarquivo
XHTML.Emambososcasos,oresultadodapáginaclienteseráomesmo.
249
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 266

9.5. Organizeocódigodastelascomtemplates CasadoCódigo
Definaoconteúdocomoui:define
Napáginacliente,usamos ui:defineparadefiniroconteúdodeuma
áreacriadacom ui:insert.
Quandoousuáriosolicitaapágina home.xhtml,seráprocessadooar-
quivodemesmonome,queusaotemplate.Essapágina,porsuavez,define,
viatag ui:define,conteúdosidentificadospornomes.
Cuidadoscompáginasincluídas
Vimosnonossotemplatequeboapartedoseuconteúdofoidefinidaus-
andoinclusões.Noentanto,oqueacontecesesimplesmenteincluirmosuma
páginacomoaseguinte?
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://java.sun.com/jsf/facelets"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<h:graphicImage library="images" name="logo.png"/>
Desenvolvido pela Casa do Código
</html>
Oresultadodissoéqueteremosoconteúdototaldessapágina,queno
casoéa rodape.xhtml,dentrodapáginaqueaincluiu.Porém,comopode-
mosperceber,dentroda rodape.xhtmltemosatag html,oqueresultaem
umatag htmldentrodaoutra.
Paraevitarisso,costumamoscolocaraspáginasqueserãoincluídasden-
trodeumatag ui:composition,porque,comojávimosantes,tudoque
ficaforadessatagéignorado,incluindoatag html.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://java.sun.com/jsf/facelets"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<ui:composition>
250
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 267

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
<h:graphicImage library="images" name="logo.png"/>
Desenvolvido pela Casa do Código
</ui:composition>
</html>
Podemos utilizar a mesma abordagem de declarar um
ui:composition nas páginas que serão incluídas, assim, apenas a
partedentrodessatagseráconsideradoparaainclusão.
Aalternativaui:component
Podemos usar essa tag nos mesmos casos em que usamos
ui:composition sem um template associado. A diferença é que,
emvezdesimplesmenteoconteúdodatagsercopiado,comoaconteceriano
usoda ui:composition,utilizando ui:componentoJSFirácriarna
árvoredecomponentesumcomponentecomtodooconteúdodatag.
ui:insertanônima
Apáginaquechamamosde painel.xhtmlnãodeixadeserumtem-
plate,assimcomovimosanteriormenteaodefiniro layoutpadrãodaapli-
cação. Então,emambososcasos,podemosusartantoáreasnomeadasou
anônimasatravésdousodatag ui:insert.
Quandonãoespecificamosum namenessatag,dizemosqueelaéanôn-
ima,eparadefinirseuconteúdonãoprecisamosdatag ui:define.Basta
inserir o conteúdo que quisermos dentro da tagui:composition ou
ui:decoratequeeleseráinseridonolocaldotemplateondeestiveratag
ui:insertanônima.
Podemosterdiversasocorrênciasde ui:insertemummesmo tem-
plate,massomenteumapodeseranônima.
Passeparâmetroscomui:param
Podemos passar parâmetros para outra página, tanto usando
ui:composition, ui:decorate ou ui:include. Em todos os
casos,podemospassarobjetosparaapáginaqueestásendochamada,seja
elaum templateouumapáginaqueseráincluída.
251
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 268

9.6. CompositeComponents:criandonossospróprioscomponentesapartirdeoutros CasadoCódigo
Napáginaquerecebeoparâmetronãoprecisamosfazernada,bastausá-
loapartirdeseunome.
9.6 C omposite Components : criando nossos
próprios componentes a partir de outros
UmadaspossibilidadesmaisinteressantesquetemoscomoFaceletséade
criarcomponentes,compondojáexistentes. Vamosanalisarumexemplo
bemsimples,masfuncional:umcomponentequecombineum label,um
h:inputTexteum h:messageparaesseinput.Depoisdeanalisaroex-
emploeentenderaideiageral,veremoscomdetalhescomotudofunciona.
Códigotradicional:
Ano de Fabricação:
<h:inputText id="anoFabricacao" label="Ano de fabricação"
value="#{automovelBean.automovel.anoFabricacao}"/>
<h:message for="anoFabricacao"/>
Ano do Modelo:
<h:inputText id="anoModelo" label="Ano do modelo"
value="#{automovelBean.automovel.anoModelo}"/>
<h:message for="anoModelo"/>
Preço:
<h:inputText id="preco" label="Preço"
value="#{automovelBean.automovel.preco}" />
<h:message for="anoModelo"/>
Kilometragem:
<h:inputText id="kilometragem" label="Kilometragem"
value="#{automovelBean.automovel.kilometragem}" />
<h:message for="kilometragem"/>
...
Nãoédifícilperceberquantarepeti çãodecódigostemosnesseexemplo.
Sempretemoso labelaparecendoduasvezes,assimcomotemossempre
tambémo h:messages.Mesmosemsaberaindacomo,nãoédifícilimagi-
narquesejapossívelalgomenosrepetitivocomoocódigoaseguir.
252
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 269

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://java.sun.com/jsf/facelets"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core"
xmlns:fm="http://java.sun.com/jsf/composite/componentes">
<fm:input label="Ano de Fabricação" id="anoFabricacao"
value="#{automovelBean.automovel.anoFabricacao}"/>
<fm:input label="Ano do Modelo" id="anoModelo"
value="#{automovelBean.automovel.anoModelo}"/>
<fm:input label="Preço" id="preco"
value="#{automovelBean.automovel.preco}"/>
<fm:input label="Kilometragem" id="kilometragem"
value="#{automovelBean.automovel.kilometragem}"/>
</html>
Nase ção7.34tivemosoprimeirocontatocomosuportearecursosdoJSF.
Omecanismode composite componentsutilizaessamesmaestrutura.Dentro
dapasta resourcescolocamosumaoumaispastas,comosnomesque
quisermos,paraarmazenarnossoscomponentes.Nanossaaplica çãohaverá
umapasta,chamada“componentes”comopodemosvernafiguraaseguir.
253
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 270

9.6. CompositeComponents:criandonossospróprioscomponentesapartirdeoutros CasadoCódigo
Fig.9.9:Estruturadediretóriosdocomponenteinput
Para utilizar os componentes customizados, temos a seguinteuri
http://java.sun.com/jsf/composite/< pasta com os componentes> .Como
nossapastasechama componentes,acabamostendoa uri http://java.sun.
com/jsf/composite/componentes.
Reparemqueutilizamoso namespace fm,abrevia çãodefaces-motors,
apontandoparaapasta“componentes”.Apartirdessenamespacetemosuma
tagparacadaarquivodentrodapasta.Nãoéprecisoregistrarnadaemlugar
nenhum,étudoporconven ção.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:cc="http://java.sun.com/jsf/composite"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<cc:interface>
<cc:attribute name="id" required="true"/>
<cc:attribute name="label" required="true"/>
<cc:attribute name="value" required="true"/>
</cc:interface>
</html>
Da mesma forma que temos o blococc:interface temos o
cc:implementation,queéondedefinimosoconteúdodonossocompo-
nente.
254
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 271

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
...
<cc:implementation>
#{cc.attrs.label}:
<h:inputText id="#{cc.attrs.id}" label="#{cc.attrs.label}"
value="#{cc.attrs.value}" />
<h:message for="#{cc.attrs.id}"/>
</cc:implementation>
...
Aimplementa çãoébasicamenteomesmocódigoquetínhamosantes
de começar a usar nosso próprio componente, com a diferença de que
parametrizamostudoqueeravariável. Naimplementa çãodocomponente,
devemosutilizaraexpressão #{cc.attrs}paraacessarosatributosdo
nossocomponente,eentão,apartirdosatributos,vamosacessandocadaum
delesconformeanecessidade.
Lidandocomchildren
Analiseoseguintecódigo:
Ano de Fabricação:
<h:inputText value="#{automovelBean.automovel.anoFabricacao}">
<f:validateLongRange minimum="1950" maximum="2012"/>
</h:inputText>
Dentrodo h:inputTexttemosum f:validateLongRange,ouseja,
a tagdevalida çãoéfilhado input.Então,sequisermosquenossocomponente
customizadoaceitecritériosdevalida ção,comooscomponentesnativos,pre-
cisamosfazercomqueeleaceitetagsfilhas.
A implementa ção disso é muito simples, basta usarmos
cc:insertChildren onde quisermos que fique o conteúdo colocado
comofilhodonossocomponente.
...
<cc:implementation>
#{cc.attrs.label}:
<h:inputText id="#{cc.attrs.id}" label="#{cc.attrs.label}"
value="#{cc.attrs.value}">
255
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 272

9.6. CompositeComponents:criandonossospróprioscomponentesapartirdeoutros CasadoCódigo
<cc:insertChildren/>
</h:inputText>
<h:message for="#{cc.attrs.id}"/>
</cc:implementation>
...
Aúnicadiferen çaemrela çãoàimplementa çãoanterioréondepuxamos
oconteúdoquecolocamosdentrodonossocomponentenatelaqueousar.
...
<fm:input label="Ano de Fabricação" id="anoFabricacao"
value="#{automovelBean.automovel.anoFabricacao}">
<f:validateLongRange minimum="1950" maximum="2012"/>
</fm:input>
<fm:input label="Ano do Modelo" id="anoModelo"
value="#{automovelBean.automovel.anoModelo}">
<f:validateLongRange minimum="1950" maximum="2013"/>
</fm:input>
<fm:input label="Preço" id="preco" value="#{auto.preco}"/>
...
Entãoagorapodemoscolocartagdevalida ção,ouconversão,oumesmo
f:ajaxdentrodonossocomponente.Enfim,agoraelesuportadentroqual-
queroutroelementoqueumcomponentepadrãoJSFaceitaria.
Issoémuitoimportantequandotrabalhamoscomcomponentescus-
tomizados.Afinal,aprincipaldesvantageméquandoeleslimitamaspossi-
bilidadesdeuso.Adicionandosuportea tagsfilhasnósdeixamosnossocom-
ponentemaisversátil,diminuindoanecessidadedeadapta çõesquandoele
forreutilizadoemnovoscenários.
Lidandocomfacets
Oqueacontecequandotemosmaisdeumconteúdopassíveldeserin-
seridodentrodatagqueacabamosdecriar?
Porexemplo,considereumcomponentequeéumpainelcustomizado,e
quepodemosinformartantoovalordocabe çalhoquantodorodapédesse
256
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 273

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
painel. Parecesimples,não? Seriaapenaspassarmososrespectivosvalores
viapropriedadesdocomponente. Agoraconsidereque,alémdeumtexto,
queiramospermitiracoloca çãodeumíconenocabe çalhoeumbotãode
açãonorodapécomonaimagemaseguir.
Fig.9.10:Panelusandofacetparamontarcabe çalhocomfiguraerodapécom
botão
Masparaenriquecermaisaindaaspossibilidades,podemosemoutromo-
mentocolocaruminputnocabe çalhoeumbotãoparafiltraroconteúdodo
painel.
257
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 274

9.6. CompositeComponents:criandonossospróprioscomponentesapartirdeoutros CasadoCódigo
Fig.9.11:Panelcomh:inputTexteh:commandButtonnocabe çalho
Comissopercebemosquenãodápraficarpassandodezenasdepro-
priedadesparaocomponentenointuitodedeixá-lomaisversátil. Nesse
momento,vemosoporquêdaexistênciada tag f:facet.Elanospermite
criarse çõesnomeadasdentrodonossocomponente.Nãoéapenasumapro-
priedade,éumaáreainteiraqueficadentrodonossocomponente,podendo
conterdiversoscomponentesdentrodesi. Então,baseadononomedessa
área,conseguimosrecuperarseuconteúdo.
<fm:painel colunas="2">
<f:facet name="header">
<h:graficImage library="images" name="icon.png"/><br/>
Adicionar Automóvel
</f:facet>
<f:facet name="footer">
<h:commandButton value="Salvar"
action="#{automovelBean.salvar(auto)}"/>
</f:facet>
...
258
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 275

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
Ano de Fabricação:
<h:inputText
value="#{automovelBean.automovel.anoFabricacao}" />
Ano do Modelo:
<h:inputText value="#{automovelBean.automovel.anoModelo}" />
Preço:
<h:inputText value="#{automovelBean.automovel.preco}" />
Kilometragem:
<h:inputText
value="#{automovelBean.automovel.kilometragem}" />
Observações:
<h:inputTextarea
value="#{automovelBean.automovel.observacoes}" />
</fm:painel>
Para lidar comfacetstemos duas opções, o cc:insertFacet e o
cc:renderFacet.
Insiraasfacetascomcc:insertFacet
Usamosessatagdentrodobloco implementationdonossocomponente
quandoqueremosinserirnaquelelocalo f:facetquefoidefinido. É
comosecopiássemosecolássemoso f:facetparaolocalondeusarmos
atag cc:insertFacet.Assim,dentrodonossocomponenteteremosum
f:facet.
Quandotemosaimplementa çãodonossocomponenteeháumoutroque
esperaapresen çadedeterminadas facets,precisamosinseri-lo:
...
<cc:implementation>
<p:panelGrid columns="#{cc.attrs.colunas}">
<cc:insertFacet name="header"/>
<cc:insertFacet name="footer"/>
<cc:insertChildren/>
</p:panelGrid>
259
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 276

9.6. CompositeComponents:criandonossospróprioscomponentesapartirdeoutros CasadoCódigo
</cc:implementation>
...
Nessa implementação, fizemos um invólucro do componente
p:panelGrid,eelejásuportadois facetschamados“header”e“footer”,que
servemparadefinirosconteúdosdocabe çalhoerodapé,respectivamente.
Mostreasfacetascomcc:renderFacet
Essa tagdeveserusadaquando,emvezdecopiara f:facetparadentro
donossocomponente,nóssimplesmentequisermosrenderizarseuconteúdo
nolocalondecolocamosa cc:renderFacet.
Enquanto cc:insertFacet copia a tag f:facet utilizada, a
cc:renderFacetcopiaerenderizaoconteúdodentrodafaceta.
Poderíamosusaressa tagpararenderizarumconteúdoalternativopara
nossocomponente. Considereuma tagdeseguran ça,quesómostraoque
estáenvolvidoporelaseousuáriotiveracesso,ecasonãotenha,umconteúdo
diferenteémostrado.
Esseconteúdoalternativopoderiaserfixoousomenteumtexto,maspara
enriquecernossoexemplo,vamosconsiderarqueousuáriodonossocompo-
nentepodeespecificarqualquerconteúdoalternativo.
...
<seguranca:proteger>
<h:commandButton value="Excluir"
action="#{automovelBean.excluir(objeto)}"/>
<f:facet name="semAcesso">
<h:commandButton value="Solicitar Exclusão"
action="#{controller.solicitaExcusao(objeto)}"/>
</f:facet>
</seguranca:proteger>
...
Criamosaquiuma tagqueverificaseousuáriotemounãoacessopara
excluirumdeterminadoobjeto.Casonãotenha,nossocomponentepermite
nãomostrarnada,mostrarumamensagem,oucomonoexemplo,exibirum
botãoalternativoparasolicitaraexclusão. Solicita çãoessa,quedeveráser
analisadaporumadministrador.
260
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 277

CasadoCódigo Capítulo9. Enriquecendonossaaplica çãoJSF
Aimplementa çãodonossocomponenteéaseguinte:
...
<cc:implementation>
<ui:fragment rendered="#{currentUser.role == 'admin'}">
<cc:insertChildren/>
</cc:fragment>
<ui:fragment rendered="#{currentUser.role != 'admin'}">
<cc:renderFacet name="semAcesso"/>
</cc:fragment>
</cc:implementation>
...
Novamente temos uma implementação bem simples. Como pode-
mos ver, temos umif-elseverificando se o usuário é administrador.
Nesse caso, mostramos o conteúdo interno do nosso componente via
cc:insertChilder;ecasonãotenhaacesso,renderizamosoqueestiver
dentroda f:facetchamada“semAcesso”.
9.7 Criar um jar com componentes customiza -
dos
Os composite componentsusamamesmaestruturaderecursosqueoJSFusa
paraimagens,folhasdeestilosejavascripts,vistanase ção7.34. Emtodos
essescasos,paradisponibilizaressesrecursosemumjarbastacolocarmosa
pasta“resources”dentrodoMETA-INFdojar.
Aseguirvemoscomoficamosrecursosdentrodoprojetoedentrodojar.
261
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 278

9.7. Criarumjarcomcomponentescustomizados CasadoCódigo
Fig.9.12:Aestruturadoscomponentesnoprojetoenojaréamesma
Adicionandoojaremoutraaplica ção,essesrecursosficamdisponíveis
comoseestivessemdentrodela. Podemosreferenciarqualquerrecursoe
qualquercomponentecustomizadodamesmaformaquefazemosquando
elesestãodentrodanossaaplica ção,enãoemumjar.
262
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 279

Capítulo10
Truquesquepodemaumentara
escalabilidadeeaperformance
dasuaaplica ção
Vimoscomousarcorretamentecarregamento lazy,evitandoproblemade
N+1consultas,vimoscomousaroescopocorretoeváriasoutrastécnicasque
envolviamJPAeoJSF.Noentanto,mesmocomtudoisso,podeserquepre-
cisemosdealgomaisemnossaaplica ção.
Nessecapítulo,veremoscomotrabalharcomosdiversoscachesqueas
implementaçõesdaJPAnosfornecem. UsandoJSF,aprenderemoscomo
podemosdiminuironúmeroderequisi çõesaoservidore,mesmoquando
astiverdefazer,comoelaspodemserexecutadasbemmaisrápido.
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 280

10.1. UtilizeocachedesegundoníveldaJPA CasadoCódigo
10.1 Utilize o cache de segundo nível daJPA
AJPApossuidoisníveisdecache.Oprimeirodeles,mesmosemsabermos,
jáestamosusandodesdeoiníciodesselivro,jáquenãorequernenhumacon-
figuraçãoadicional.Nase ção4.2foiditoqueJPAécontextual;sófaltoudizer
queessecontextoprovêoquechamamosdecachedeprimeironível.
Cadaobjetoqueécarregadopelo EntityManageracabaficandono
cachedesse EntityManager. Apartirdeentão,todavezqueomesmo
objetoforbuscadopelachave,eleserádevolvidoimediatamente,semneces-
sidadedeumnovoacessoaobancoparaisso.Aimagemaseguirilustraesse
funcionamento.
Fig.10.1:CachedeprimeironívelevitaqueamesmaMarcasejabuscadano-
vamentenobanco
Essemecanismotemumpotencialmuitograndedeeconomizarconsul-
tas. Bastaqueamesmainstânciade EntityManagersejausada,poiso
cachedeprimeironíveléfeitoapenasdentrodela.Oproblemaéque,geral-
mente,cadainstânciadessaviveapenasduranteumarequisi çãodousuário,
sendofechadalogoemseguidaparaliberarrecursosdoservidor.
Ativandoocachedesegundonível
Jávimosquenenhumaconfigura çãoénecessáriaparausarmosocache
264
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 281

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
deprimeironível, porémelevivesomenteenquantoviverainstânciade
EntityManager.Comoessetempoécurto,temosumcachebom,masque
podeserusadoporpoucotempo.Outralimita çãodocachedeprimeironível
équeelenãoécompartilhado,assim,umusuáriocarregaalistade Marcae
ooutrousuáriotemquecarregarnovamenteamesmalista.
Fig.10.2:Cachedeprimeironível
Pararesolvermosessasitua ção,temosocachedesegundonível,queé
compartilhadoentretodasasinstânciasde EntityManager. Naprática,
querdizerqueseumusuáriocarregoualistade Marcaelaestarádisponível,
sejapraelemesmousarnovamenteemrequisi çõesfuturasouparaoutros
usuários.
265
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 282

10.1. UtilizeocachedesegundoníveldaJPA CasadoCódigo
Fig.10.3:Cachedesegundonível
Comocachedesegundonívelativado,umavezquealgumainstância
de EntityManagerbuscouoobjeto,eleestádisponívelparaasoutras.Na
figuravemosqueoquefoibuscadopelousuárioAbeneficiouousuárioB.
Comoocachedesegundonívelécompartilhado,nãofazmuitadiferen ça
seos EntityManagersqueestãoacessandoforamcriadosparaomesmo
usuárioouparausuáriosdiferentes.
AJPA2.0temsuportenativoaocachedesegundoníveleeleéconfigu-
radoatravésdoelemento shared-cache-modedo persistence.xml.
Podemosespecificarcincomodosdiferentesdecache:
•ALL:automaticamentehabilitatodasasentidadesnocachedesegundo
nível;
•NONE::desabilitaocachedesegundonívelparatodasasentidades;
•ENABLE_SELECTIVE:habilitaocachedesegundonívelparatodasas
266
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 283

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
entidadesqueestiveremanotadascom @Cacheable;
•DISABLE_SELECTIVE:habilitaocachedesegundonívelparatodas
asentidades,desabilitandosomenteasqueestiveremanotadascom
@Cacheable(false);
•UNSPECIFIED:quandonãoespecificamosnada,esseéovalorassum-
idopelo shared-cache-mode,enessecaso,cadaimplementa çãode
JPAtemliberdadeparadefinirqualmodoseráhabilitado.
Umexemplodeconfigura çãopodeservistoaseguir:
<persistence ...>
<persistence-unit name="default"
transaction-type="RESOURCE_LOCAL">
<shared-cache-mode>ENABLE_SELECTIVE</shared-cache-mode>
<properties>
...
</properties>
</persistence-unit>
</persistence>
Umavezquenossaentidadeestáconfiguradanocachedesegundonível,
pelousodaanota ção @Cacheable,nãoprecisamosfazernadadiferenteao
utilizá-la. Automaticamenteateremosdisponívelporbastantetempo,evi-
tandomuitosacessosaobancodedados.
@Entity @Cacheable
public class Marca {
...
}
Masaindaprecisamosdeumaimplementa çãodecache,sendoque,pos-
sivelmente,asmaisutilizadassão EHCachee Infinispan.
Ambasasimplementa çõespossuemconfigura çõesespecíficas,nasquais
podemosindicarparacadaentidadeonúmeromáximodeobjetosqueficarão
emmemória,edepoisoqueseráarmazenadoemdisco,etc. Comoessas
configuraçõesvariammuitodeacordocomcadatipodeaplica ção,notrecho
267
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 284

10.1. UtilizeocachedesegundoníveldaJPA CasadoCódigo
decódigoaseguircolocaremosapenasumexemplo,emcujaconfigura ção
padrãousaremosomódulo hiberante-ehche.
...
<persistence-unit name="default"
transaction-type="RESOURCE_LOCAL">
<shared-cache-mode>ENABLE_SELECTIVE</shared-cache-mode>
<properties>
...
<property name="hibernate.cache.region.factory_class"
value="org.hibernate.cache.ehcache
.EhCacheRegionFactory"/>
</properties>
</persistence-unit>
...
Comofuncionaaaltera çãodeumobjetoqueestánocache
Agoraquetemosumcachedesegundonívelfuncionando,oqueocorre
quandojácarregamosumalistade Marcanessecacheeumusuárioedita
umadelas?
Comoaaltera çãoseráfeitapelaprópriaJPA,nomomentoemqueesse
objetoalteradoéenviadoparaobanco,eleétambématualizadonocachede
segundonível.Noentanto,casoaversãoantigadoobjetoestivessecarregada
nocachedeprimeironíveldealgumoutro EntityManager,esseobjeto
ficariadesatualizadodentrodessaoutra EnitityManager.
ComoaJPAcuidadaatualiza çãodocachedesegundonível,nossoúnico
pontodefalhapassaaserocachedeprimeironível. Agoraocurtotempo
devidada EntityManager,queanteseraumadesvantagem,passaaser
umavantagem.Comootempoqueduraumarequisi çãogeralmenteébem
curto,eesseseriatambémotempodevidada EntityManager,paraque
houvessealgumerrodeconcorrênciaprecisaríamos,nomesmo“segundo”,
quedoisusuárioseditassemumamesmainstânciadeumaclassedeentidade
-quegeralmentemudapouco,porqueseassimnãofosse,nãoestariamno
cachedesegundonível.
Temos,noentanto,queponderardoisimportantespontos. Oprimeiro
éadura çãodasnossasrequisi ções.Setivermosprocessamentosdemorando
268
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 285

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
muito,achancedeconcorrênciaserámaior.Eporissoapalavra“segundo”
doparágrafoanteriorestáentreaspas,senossoprocessamentodemorardez
segundos,estaremosaumentandoachancedeconcorrência.
Outropontoqueprecisamoslevaremconsidera çãoéaprobabilidadede
concorrênciaversusobenefíciodocache.Comocadaaplica çãopossuiuma
dinâmicadiferente,issoprecisaseravaliadocasoacaso.Nanossaaplica çãode
exemplo,certamenteteremosmuitomaisusuáriosconsultandoautomóveis
doqueosalterando. Issonoslevaacrerqueparaessaaplica çãoastrêsen-
tidades, Marca, Modeloe Automovel,valemapenaestarnocachede
segundonível.
Aestruturadocachedesegundonível
Nasfigurasqueilustravamofuncionamentodoscachesdeprimeiroe
segundoníveisusamossemprecomoexemploométodo find,passandoa
classeeo idquegostaríamosdebuscar. Aestruturadocachedesegundo
níveléparecidacomafigura10.4.
Fig.10.4:Estruturadocachedesegundonível
Comissoocachesaberecuperarobjetosdequalquerentidade,desdeque
baseadosnachaveprimária.Masequandonãobuscamospelachave?Oque
acontecesefizermosumapesquisacomdiversosfiltroseelasempreretornar
osmesmosresultados? Nessecaso,precisaremosdeumcachediferente,o
cachedeconsulta. Comocachedesegundonívelcomovimosatéagorasó
conseguimosencontrarobjetospelachave.
269
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 286

10.2. Façacachedeconsultas CasadoCódigo
10.2 Faça cache de consultas
Apáginainicialdanossaaplica çãoiráapresentarosúltimosautomóveis
cadastrados,eseriainteressantequepudéssemosnosbeneficiardocache,afi-
naldecontasalistamudamuitopoucosecomparadocomaquantidadede
visualizaçõesqueacontecenela.Imaginequantasvezesamesmaconsultase-
riafeita,semprecomomesmoresultado.
Pararesolveresseproblema,temosocachedeconsultas.Esserecurso,no
entanto,aindanãofazpartedaJPA,entãoprecisaremosusarrecursosespecí-
ficosdoHibernate.Detodaforma,aJPAjáprevêqueemdeterminadosmo-
mentosiremosprecisardefuncionalidadesespecíficasdaimplementa çãoque
estamosusando,possibilitando-nosdesenvolveraplica çõesque,mesmocom
recursosespecíficosdeumaimplementa ção,continuemportáveisatécerto
ponto.
Para ativar o cache de consultas na nossa aplicação, precisamos da
seguinteconfigura ção:
...
<persistence-unit name="default"
transaction-type="RESOURCE_LOCAL">
<shared-cache-mode>ENABLE_SELECTIVE</shared-cache-mode>
<properties>
...
<property name="hibernate.cache.use_query_cache"
value="true" />
</properties>
</persistence-unit>
...
Ocachedeconsultassófuncionaseocachedesegundonívelestiverati-
vado.Esomenteserápossívelguardarnocacheconsultasqueretornemob-
jetosqueestãocomocachehabilitadocomaanota ção @Cacheable.Além
disso,precisamoshabilitarocacheemcadaconsultaquerealizarmos. No
trechodecódigoaseguir,vemoscomopodemoshabilitarocacheemuma
@NamedQuery.
@NamedQuery(name=Automovel.LISTAR_DESTAQUES,
query="select a from Automovel a",
270
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 287

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
hints={
@QueryHint(name="org.hibernate.cacheable", value="true"),
@QueryHint(name="org.hibernate.cacheRegion",
value=Automovel.LISTAR_DESTAQUES)})
@Entity
@Cacheable
public class Automovel {
public static final String LISTAR_DESTAQUES =
"Automovel.buscarDestaques";
...
}
Comaanota ção @QueryHint,podemoscolocarinforma çõesespecíficas
daimplementa çãodeJPAqueestamosusandonas queriese named queries.
Apesardaimplementa çãoemquestãoseroHibernate,ofuncionamentoseria
omesmousandooutraimplementa ção.
Atravésdas query hints,pormaisqueespecifiquemosumainforma ção
proprietária,usamosapenas Stringsparaisso,evitandoumadependência
comclassesdoHibernate.Casoencontreuma query hintqueelanãoconhece,
elaseráignorada.
Noexemploacimaestamosusandouma @NamedQuery,maspodemos
usaras query hintsemobjetos Querytambém.
Query query = JpaUtil.getEntityManager()
.createQuery("select a from Automovel a", Automovel.class);
query.setHint("org.hibernate.cacheable", true);
query.setHint("org.hibernate.cacheRegion",
Automovel.LISTAR_DESTAQUES);
List<Automovel> automoveis = query.getResultList();
Emambososexemplosusamosonomedaregiãoigualaonomeda named
query.Podemosdarqualquernomeparaaregiãodecachequeusaremos.
Obviamentepodemosfacilitaresseusocommétodosauxiliarescomoo
seguinte:
Query query = JpaUtil.getEntityManager()
.createQuery("select a from Automovel a", Automovel.class);
271
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 288

10.2. Façacachedeconsultas CasadoCódigo
JpaUtil.enableCache(query, Automovel.LISTAR_DESTAQUES);
List<Automovel> automoveis = query.getResultList();
...
public class JpaUtil {
...
public static Query enableCache(Query query, String region){
query.setHint("org.hibernate.cacheable", true);
query.setHint("org.hibernate.cacheRegion", region);
return query;
}
}
Diferentementedocachedesegundoníveldeentidades,queguardao
objetopelotipoepelo id,aestruturadocachedeconsultafuncionacomoo
esquemaaseguir:
Fig.10.5:Estruturadocachedeconsultas
Como vemos, o cache de consulta toma como base tanto a consulta
quantoosparâmetrospassados,jáqueamesmaconsultapodeserexecutada
comparâmetrosdiferentes,tendooutroresultado.
Umavezqueaconsultaéexecutada,ocacheguardaostipose iddos
objetosretornadospelaconsultae,apartirdeentão,ofuncionamentoéo
mesmodocachedesegundoníveldeentidades.Écomoseocachedecon-
sultastransformasseanossapesquisaemumasériedebuscasbaseadasem
chaveprimária,ecomojávimos,nessecasotiramosproveitodocachede
segundonível.
272
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 289

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
Tratandocachedesatualizado
Enquantoocachedesegundonívelconseguelidarbemcomatualiza ção
deobjetos,ocachedeconsultanãoconseguefazerissoautomaticamente.Ao
alterarmosumapropriedadedeumobjeto,podeserqueelepasseaaparecer
ouentãodeixedeaparecercomoresultadodeumaconsultaquejáestáno
cache.Comosaberseocachedeveounãoserinvalidado?Arespostaéque
automaticamentenãosabemos.
Parasolucionaressaquestão,usamosasregiõesquedefinimosnosex-
emplosanteriores. Podemoscolocarváriasconsultasouentidadesemuma
região,eentão,aoinvalidarmosumaregião,todasasconsultaseentidades
queestavamarmazenadasnelasaemdocache.Ficaacargododesenvolvedor
invalidararegiãonecessáriaacadamomento.
Seexisteumaregiãochamada Automovel.buscarDestaques,que
armazenaosautomóveisrecentementecadastrados,aoinserirmosumnovo
Automoveliremosinvalidaressaregiãoparaquedapróximavezqueacon-
sultasejafeitaelatragaessenovoobjetodobanco.Apartirdasegundavez
queaconsultaforexecutada,ocachevoltaráaretornararespostasempre-
cisaracessarobancodedados.
Parainvalidarocachedeconsultasprecisamosexplicitamenteacessara
APIdoHibernate,masparamanteraportabilidadedonossocódigo,uti-
lizamosmétodosauxiliarescomopodemosveraseguir.
@ManagedBean @ViewScoped
public class AutomovelBean {
public String salvar(Automovel auto) {
EntityManager em = JpaUtil.getEntityManager();
em.persist(auto);
JpaUtil.evictCache(em, Automovel.LISTAR_DESTAQUES);
return "listar";
}
}
public class JpaUtil {
...
273
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 290

10.3. Colhendoestatísticasdanossacamadadepersistência CasadoCódigo
public static void
evictCache(EntityManager em, String region){
try {
Session session = (Session) em.getDelegate();
Cache cache =
session.getSessionFactory().getCache();
cache.evictQueryRegion(region);
}
catch(Exception e) {
// provavelmente a implementação não é o Hibernate
}
}
}
Esse tipo de código é uma forma de contornar a dependência que
acabamoscriandocomumadeterminadaimplementa çãodaJPA,deixando-a
encapsuladaemumpontodonossocódigo.
10.3 Colhendo estatísticas da nossa camada de
persistência
Quandofalamosdeotimiza çãonacamadadepersistência,pensamosemevi-
tarconsultasaobancoeemfazerconsultasqueretornemsomenteosdados
necessários.
Nase ção5.14,enquantofalávamosdaimportânciadosrelacionamentos
lazy,comentamosdosmilharesderegistrosquedeixamosdeler,porém,essa
contafoifeitaemcimadeumcenáriosimples,conhecidoecontrolado.Mas
comosaberquantosobjetossãotrazidosdobancoparamontarumapágina
quelistavinteautomóveis,porexemplo?
Paraobtermosdadosestatísticosdacamadadepersistência,utilizaremos
maisumrecursoespecíficodoHibernate,queprovêestatísticasdequantos
objetosforamtrazidosdobanco,quantasconsultasforamfeitasequantasnão
precisaramacessarobancoporquefoiresolvidapelocache,bemcomoquan-
tidadede inserts, updatese deletes.Enfim,temosumatelemetriadacamada
depersistência.Paraisso,oprimeiropassoéhabilitaressafuncionalidade:
274
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 291

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
...
<persistence-unit name="default"
transaction-type="RESOURCE_LOCAL">
<shared-cache-mode>ENABLE_SELECTIVE</shared-cache-mode>
<properties>
...
<property name="hibernate.generate_statistics"
value="true"/>
</properties>
</persistence-unit>
...
Apartirdessemomento,podemosgerarnologainforma çãoestatística
quenosinteressar,acadarequisi ção,pormeiodeum Filter,oupodemos
aindacolocaressasinforma çõesdentrodeum PhaseListeneregeraressas
informaçõesparacadafasedociclodevidadoJSF.Assim,isolamosocódigo
deobten çãodeestatísticas.
Asestatísticassãoobtidasapartirda SessionFactorydoHibernate,
quenospermiteacessaroobjetoquecontémasinforma ções,equeimple-
mentaainterface org.hibernate.stat.Statistics.
public class JpaUtil {
...
public static Statistics getStatistics(){
EntityManager em = JpaUtil.getEntityManager();
Session session = (Session) em.getDelegate();
SessionFactory sf = session.getSessionFactory();
Statistics stats = sf.getStatistics();
return stats;
}
}
Nessemétodo,temosquesairdaJPAeentrarnaAPIdoHibernate.Pode-
mosaindafazerummétodoquegereasinforma çõesestatísticaseasadicione
nolog,edepoischamá-lo,sejano Filterouno PhaseListener.
public class JpaUtil {
...
public static void printStatistics(){
275
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 292

10.3. Colhendoestatísticasdanossacamadadepersistência CasadoCódigo
Statistics stats = JpaUtil.getStatistics();
log.info("Qtde de entidades buscadas: " +
stats.getEntityFetchCount());
log.info("Qtde de entidades carregadas: " +
stats.getEntityLoadCount());
log.info("Qtde de listas buscadas: " +
stats.getCollectionFetchCount());
log.info("Qtde de listas carregadas: " +
stats.getCollectionLoadCount());
double queryCacheHitCount =
stats.getQueryCacheHitCount();
double queryCacheMissCount =
stats.getQueryCacheMissCount();
double totalQueries =
queryCacheHitCount + queryCacheMissCount;
double queryCacheHitRatio =
(totalQueries == 0) ? 0 : queryCacheHitCount /
totalQueries;
log.info("Qtde de consultas encontradas no cache: " +
queryCacheHitCount);
log.info("Qtde de consultas fora do cache: " +
queryCacheMissCount);
log.info("Proporção de acerto do cache: " +
queryCacheHitRatio);
log.info("Qtde de consultas executadas: " +
stats.getQueryExecutionCount());
String[] queries = stats.getQueries();
for (int i = 0; i < queries.length; i++) {
log.info("Consulta " + i + ": " + queries[i]);
}
log.info("Query + lenta: " +
stats.getQueryExecutionMaxTimeQueryString());
276
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 293

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
stats.clear();
}
}
Escrevemosinforma çõesdequantasentidadesforambuscadasequan-
tasefetivamenteforamtrazidasdobanco,edepoisfizemosomesmocomas
coleções. Essascoleçõessãocarregamentosderelacionamento“*-to-many”
queforamdisparados.
Fizemostambémumaanálisedaefetividadedocachedeconsultaseno
finalatéescrevemoscadaconsultaexecutada.Essasestatísticassãoexempli-
ficativas,emuitasoutrassãopossíveis,comoporexemploumaanálisedo
cachedesegundoníveldeentidades,estatísticasporregiãodecacheentre
outrasinforma ções.
Nofinaldométodo,limpamosasestatísticasparaqueosnúmerosap-
resentadossejamreferentessomenteacadarequisi çãooufasedoJSF,enão
cumulativos.
10.4 Relacionamentos extra -lazy
Ase ção5.14,ondevimosaimportânciado lazy load,émuitoimportante,
jáque,semessecarregamentosobdemanda,aperformancedasnossasapli-
caçõesseriasofrível. Lá,vimosoexemplodorelacionamentoentreasenti-
dades Marcae Modelo,noqual,mantendoo lazyde Marcacomsualista
de Modelo,alistagemabaixonãocarreganenhumainstânciade Modelodo
banco:
public class Marca {
@Id @GeneratedValue
private Integer id;
...
@OneToMany(mappedBy="montadora")
private List<Modelo> modelos;
...
}
277
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 294

10.4. Relacionamentosextra-lazy CasadoCódigo
public class MarcaBean {
private List<Marca> marcas;
...
public List<Marca> getMarcas() {
if (marcas == null) {
marcas = JpaUtil.getEntityManager()
.createQuery("select m from Marca m", Marca.class)
.getResultList();
}
return marcas;
}
}
<h:dataTable value="#{marcaBean.marcas}" var="marca">
<h:column>
<f:facet name="header">Nome da Marca</f:facet>
#{marca.nome}
</h:column>
</h:dataTable>
Nesse h:dataTable,estamosapenaslistandoas marcas.Comojávi-
mosque,porpadrão,orelacionamentoé lazy,alistade modelosda Marca
nãoserácarregada.Massealterarmosnossalistagemparaincluiraquanti-
dadedemodeloscomoaseguir,ocomportamentomuda.
<h:dataTable value="#{marcaBean.marcas}" var="marca">
<h:column>
<f:facet name="header">Nome da Marca</f:facet>
#{marca.nome}
</h:column>
<h:column>
<f:facet name="header">Qtde de Modelos</f:facet>
#{fn:length(marca.modelos)}
</h:column>
</h:dataTable>
Afun çãoJSTL fn:lengthmostraotamanhodeuma Stringouentão
o size()deuma Collection. Nesseexemplo,écomoseestivéssemos
chamando marca.getModelos().size().Comoinvocamosummétodo
278
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 295

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
daAPIdoJava,quenãofoidesenvolvidopensandoembancodedados,ele
usaosdadosemmemória,eparaqueissofuncione,ocomportamentopadrão
ébuscaralista.
Poderíamos aqui querer otimizar por nós mesmos e criar um novo
métodoqueexecuteum countvia SQL,imaginandoqueacamadadeper-
sistência,emcasossimplescomoesse,maiscomplicadoqueajuda.Porém,
estaríamosenganadosmaisumavez.ApesardenãoestarespecificadonaJPA,
temosumrecursoespecíficodoHibernatechamado extra lazy,quehabilita
umaanálisemaisaprofundadadousoquesepretendefazerdacole ção,para
somenteentãodecidirseoselementosserãoounãobuscados.
Com extra lazy, é analisado que método está sendo chamado nessa
coleção,ecasosejaalgoresolvívelviabanco,semprecisarcarregaroselemen-
tos,oHibernateefetuaessaopera çãoemvezdecarregá-los.Comoconfigurar
ealgunsexemplosdeusopodemservistosnostrechosdecódigoaseguir.
import org.hibernate.annotations.LazyCollection;
import org.hibernate.annotations.LazyCollectionOption;
...
public class Marca {
@Id @GeneratedValue
private Integer id;
...
@OneToMany(mappedBy="montadora")
@LazyCollection(LazyCollectionOption.EXTRA)
private List<Modelo> modelos;
...
}
Exemplosdeusodo extra lazy:
// a Marca é carregada do banco, mas a lista de modelos não
Marca marca = entityManager.find(Marca.class, 1);
// com extra lazy, é feito um count no banco:
// select count(id) from Modelo where marca_id =?
int qtdeModelos = marca.getModelos().size();
279
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 296

10.5. Paginaçãovirtualerealdedados CasadoCódigo
// isEmpty pode ser descoberto a partir do resultado do count
boolean listaVazia = marca.getModelos().isEmpty();
Modelo modelo = entityManager.find(Modelo.class, 1);
// contains não traz a lista inteira, e sim, faz um select
// invertido: select 1 from Modelo where marca_id =? and id =?
boolean modeloNaLista = marca.getModelos().contains(modelo);
10.5 Paginação virtual e real de dados
Oconceitodepagina çãoécomumatodosnós. Eleestápresentequando
acessamosnossoe-mailouquandofazemosumabuscanoGoogle,quando
entramosemumsitequepossuiprodutosàvendaouquandoacessamosredes
sociais.Pagina çãoéircarregandoainforma çãoparaousuárioconformeele
vaiavan çandonavisualiza çãodosdados.Aofazerumapesquisaqueretorne
milharesderesultados,porquedeveríamoscarregartodoselesseousuário
geralmenteolhaapenasosprimeirosdezouvinteelementosexibidos?
Oquecostumaocorreréqueémaissimplescarregartudodobancoe
deixaralgumcomponentevisualexibirosdadosempáginasdedezouvinte
elementoscada. Oproblemaéqueissogeralmentefuncionabememapli-
caçõesjovens,compoucosdados,masàmedidaemqueaquantidadededa-
dosaumenta,aperformancedaaplica çãodiminui.
Costumamoschamaressaexibi çãofracionadadedadosdepagina çãovir-
tual,quetrazsomentebenefícioscosméticosparanossaaplica ção.Jáapag-
inaçãoquerealmentebuscaosdadosempor çõespequenaséchamadade
paginaçãoreal.
Devemosprocurardesdeoiníciodaaplica çãotrabalharcompagina ção
real,porqueselogodocome çofizermosavirtualteremosdoistrabalhos:o
defazereoderefazer.Obviamente,comosempreexistemcasosecasos,em
situaçõesbempontuais,nasquaisanaturezadosdadosjáfazcomqueeles
sejamlimitados,ousodepagina çãovirtualnãopoderánãoserfatordeter-
minanteparaumapossívelperformanceruimdaaplica ção.Masaboaprática
éprocurarmossempretrabalharcompagina çãoreal.
Vamos mostrar como fazer as paginações tanto virtual, quanto real,
atravésdousodocomponente dataTabledoPrimefaces,jáqueesseoferece
280
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 297

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
suportesimplesàspagina ções.
<h:form>
<p:dataTable value="#{modeloBean.modelos}" var="modelo"
paginator="true" rows="10">
<p:column>
<f:facet name="header">ID</f:facet>
#{modelo.id}
</p:column>
<p:column>
<f:facet name="header">Marca</f:facet>
#{modelo.marca.nome}
</p:column>
<p:column>
<f:facet name="header">Descrição</f:facet>
#{modelo.descricao}
</p:column>
</p:dataTable>
</h:form>
@ManagedBean @ViewScoped
public class ModeloBean {
private List<Modelo> modelos;
...
public List<Modelo> getModelos() {
if (modelos == null) {
modelos = JpaUtil.getEntityManager()
.createQuery("select m from Modelo m", Modelo.class)
.getResultList();
}
return modelos;
}
...
}
Olhandooexemploacima,aúnicadiferen çaemambososcódigoséna
declaraçãodo p:dataTable,ondeespecificamosqueteremospagina çãoe
quecadapáginaterá10linhas.Comissojátemosoresultadoaseguir.
281
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 298

10.5. Paginaçãovirtualerealdedados CasadoCódigo
Fig.10.6:Listagemsimplesusandopagina ção
Nessecaso, tivemosapagina çãovirtual, jáquetodasasinforma ções
foram carregadas do banco de dados, mesmo as que não estão sendo
mostradas.
Usandopagina çãoreal
Oimportanteparaaperformancedaaplica çãoéapagina çãoreal,porém
estanãovemdegra çacomoavirtual.NoníveldaJPA,temosmétodospara
limitaraquantidadederegistrosretornadosemumaconsultaeparainformar
apartirdequalregistrovamoscome çaralistar.Alistagemaseguirmostra
umexemplodepagina çãoreal.
TypedQuery<Modelo> query = em.
createQuery("select m from Modelo m", Modelo.class);
int tamanhoPagina = 10;
query.setMaxResults(tamanhoPagina);
List<Modelo> pagina1 = query.setFirstResult(0 * tamanhoPagina).
getResultList();
282
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 299

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
List<Modelo> pagina2 = query.setFirstResult(1 * tamanhoPagina).
getResultList();
List<Modelo> pagina3 = query.setFirstResult(2 * tamanhoPagina).
getResultList();
Usandoosmétodos setMaxResultse setFirstResultpodemos
delimitarotamanhodecadapáginaequalseráoprimeiroelementodecada
uma.Porém,comointegrarissoaocomponente p:dataTablequeiráexibir
cadapágina?Ecomosaberqualototaldepáginas?
O primefaces, além dos componentes visuais, possui classes auxil-
iares para eles. No caso dop:dataTable existe uma classe chamada
LazyDataModel,queéum javax.faces.model.DataModelcomsu-
porteacarregamentodeobjetossobdemanda.
Toda dataTable,sejaelanativadoJSFouespecíficadoPrimefaces,
obtémseusdadosapartirdeum DataModelemesmoquandopassamos
diretamenteumalistaparaa dataTable,pordentro,elatransformaisso
emum DataModel.
Assim, criando um LazyDataModel, estaremos passando para a
p:dataTablealgocomqueelanaturalmentesabelidar,porque,alémdo
comportamentonormaldeuma dataTable,ocomponentedoPrimefaces
conheceoconceitodepagina ção.
Éperfeitamentepossívelfazerpagina çãorealcomocomponentepadrão
h:dataTable. Adiferençaéqueteríamosquecriarlinksoubotõespara
navegarnaspáginasparafrenteeparatrás.
Amaiordificuldadenaimplementa çãodanossa LazyDataModeléque
precisaremosdeumaconsultaparasaberquantoselementosexistemnototal.
Semisso,nãoépossívelcriarcorretamenteosbotõesparamostraratéque
páginatemos.
<h:form>
<p:dataTable value="#{modeloBean.modelosLazyDataModel}"
var="modelo" paginator="true" rows="10" lazy="true">
...
283
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 300

10.5. Paginaçãovirtualerealdedados CasadoCódigo
</p:dataTable>
</h:form>
@ManagedBean @ViewScoped
public class ModeloBean {
private LazyDataModel<Modelo> modelosLazyDataModel;
public LazyDataModel<Modelo> getModelosLazyDataModel() {
if (modelosLazyDataModel == null) {
String jpql = "select m from Modelo m";
String count = "select count(m.id) from Modelo m";
modelosLazyDataModel = new
QueryDataModel<Modelo>(jpql, count);
}
return modelosLazyDataModel;
}
...
}
Atéaquipodemosperceberamudan çana p:dataTable,queagora
alémdeapontarparao modelosLazyDataModel, tambémtemapro-
priedade lazy=true.
No código do Managed bean , saiu a listagem di-
reta no banco e, em vez disso, instanciamos a classe
facesmotors.persistence.QueryDataModel, passando no con-
strutor duas consultas: a primeira retorna os objetos a serem listados
e a segunda devolve a quantidade de registros. A implementação da
QueryDataModeléaseguinte:
public class QueryDataModel<T> extends LazyDataModel<T> {
private String jpql;
public QueryDataModel(String jpql, String jpqlCount) {
this.jpql = jpql;
Long count = (Long) JpaUtil.getEntityManager()
.createQuery(jpqlCount)
284
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 301

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
.getSingleResult();
setRowCount(count.intValue());
}
@Override
public List<T> load(int first, int pageSize,
String sortField, SortOrder sortOrder,
Map<String, String> filters) {
return JpaUtil.getEntityManager().createQuery(jpql)
.setFirstResult(first)
.setMaxResults(pageSize)
.getResultList();
}
}
Comoocomponente p:dataTablesuportaordena çãoefiltragem,es-
sasinforma çõessãotambémpassadasparaométodo loadqueprecisamos
implementar.Paraanossanecessidade,porém,bastausarosdoisprimeiros
parâmetros,querepresentamalinhaatualeotamanhodapágina.
Oinconvenientedessaimplementa çãoéqueprecisamosinformarduas
consultas,umaparabuscarosdadoseoutrapararealizaro count.
Agoraquetemosumaimplementa çãode LazyDataModel,podemos
fazerqualquerconsultadanossaaplica çãopassarausarpagina çãoreal!
Aapresenta çãoda dataTablecompagina çãorealnãosealtera,masa
performancedanossaaplica ção,quandotivermosexibindolistascommuitos
registros,comcertezamelhora.
10.6 UtilizandoPool de conexões
Paranosconectarcomobancodedados,estamosespecificandopropriedades
comocaminhodobanco,usuárioesenhanoarquivo persistence.xml.
Alémdisso,jávimosqueexistemconfigura çõesespecíficasdoHibernateque
podemosadicionar,afimdehabilitarcomportamentosquenosinteressam,
comoporexemplocachedeconsultas.
285
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 302

10.6. UtilizandoPooldeconexões CasadoCódigo
Veremos agora como configurar nesse mesmo aquivo umpool de
conexões.Esserecursoémuitoimportante,jáquecadavezqueprecisamos
criarumainstânciade EntityManager,ouseja,praticamenteacadareq-
uisiçãodecadausuário,essainstânciainternamenteprecisadeumaconexão
comobancodedados. Porém,conexãoéumrecursocarodemaisparase
ficarcriandoefechandootempotodo.
Todavezquetemosrecursosmuitocaros,costumamosfazerum pool,que
éumareservadeobjetosprontosparaseremusados,emvezdedemandara
criaçãodenovosobjetossemprequeprecisarmos.
OHibernatetemintegra çãonativacomopoolqueiremosutilizaraqui,
o c3p0.Aconfigura çãodeumpoolnãocostumamudarmuito.
Aquiveremosaconfigura çãodo c3p0,masoconceitoéparecidopara
outrasimplementa ções.Aconfigura çãonecessáriaéaseguinte:
<persistence...>
<persistence-unit name="default"
transaction-type="RESOURCE_LOCAL">
...
<properties>
<property name="javax.persistence.jdbc.url"
value="..." />
<property name="javax.persistence.jdbc.driver"
value="..." />
<property name="javax.persistence.jdbc.user"
value="..." />
<property name="javax.persistence.jdbc.password"
value="..." />
<property name="hibernate.c3p0.min_size"
value="5" />
<property name="hibernate.c3p0.max_size"
value="20" />
<property name="hibernate.c3p0.timeout"
value="300" />
<property name="hibernate.c3p0.max_statements"
value="50" />
...
</properties>
286
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 303

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
</persistence-unit>
</persistence>
Comoagrandemaioriadasnossasitera çõescomobancodedadosirá
duraralgoentrealgunsmilissegundosapoucossegundos,aquantidadesde
operaçõesemexecu çãosimultaneamentenobancodedadosnãocostuma
sergrande,porissoespecificamosummáximode20conexõescomobanco,
usandoapropriedade hibernate.c3p0.max_size.
Utilizamosapropriedade hibernate.c3p0.min_sizeparaespeci-
ficarquedesejamosquesemprehajapelomenos5conexõesprontasparauso.
Comodefinimosummáximode20,sabemosqueonúmerodeconexõescri-
adasvaiflutuardentrodesseintervalo.
O que vai regular o número de conexões é a propriedade
hibernate.c3p0.timeout, em que especificamos um tempo de 300
segundos. Se tivermos uma conexão sem uso por esse tempo, ela será
fechada,respeitandosomenteotamanhomínimodo pool.
Ointeressanteaoutilizarmosumpooldeconexõeséque,pormaisquea
aplicaçãosoliciteexplicitamentequeumaconexãosejafechada,napráticaela
somentevoltaparaopoolparaserreutilizadaemoutromomento.Somente
oprópriopoolfechaasconexõesquandoelasnãosãomaisnecessárias.
E por fim, mas também muito importante, temos a propriedade
hibernate.c3p0.max_statements que especifica um cache de
java.sql.PreparedStatement. Quando damos os primeiros
passos usando JDBC, aprendemos que é uma boa prática utilizar
PreparedStatement, uma vez que os comandos de banco criados
usandoesseobjetoficampreviamentepreparadosnobanco. Porém, não
conseguimos tirar proveito dessa preparação se sempre descartarmos o
objeto PreparedStatement.
Autiliza çãodessecacherefleteclaramentenobancodedados. Anal-
isandoseulog,percebemosapenasachamadadecomandospreviamente
compilados e otimizados, sejam eles comandos deselect, insert,
updateou delete.Noentanto,temosquelembrarquepormaisquedois
insertsnobancotenhamparâmetrosdiferentes,setiveremamesmaes-
trutura,estaremosfalandodeumúnico PreparedStatement. Logo,o
287
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 304

10.7. TornandooJSFmaislevecomusointeligentedeAJAX CasadoCódigo
númerodecomandosnocachenãolevaemconsidera çãoosparâmetrospas-
sados,somenteaestruturadocomando.
Todososnúmerosapresentadosaquisãoexemplificativos,masservem
comoumaboabaseparainiciaraconfigura çãodaaplica ção.
Porém,comoqualquerotimiza ção,éprecisoverificarocomportamento
daaplica çãoemcenáriosreais.Paraisso,épossíveltambémutilizarasestatís-
ticasdoHibernateparamediraefetividadedopool,assimcomomedimosa
efetividadesdosnossoscaches.
10.7 Tornando o JSF mais leve com uso in -
teligente deAJAX
TratamosdeAJAXeJSFnase ção9.4,masoenfoqueanteseramelhorara
usabilidadedanossaaplica ção. Veremosagoracomoamesmaferramenta
podeserusadaparamelhoraraperformance.
Quandofazemosumarequisi çãoAJAX,umasubárvoredecomponentes
écriada,eoqueprecisamosfazeréprocurarcriarumasubárvorequesejaa
menorpossível,jáqueissoinfluencianaperformance.
Vamosanalisarasduasop çõesaseguir:
...
<f:ajax event="blur" render="dadosAutomovel">
<h:panelGroup id="dadosAutomovel">
...
Ano de Fabricação:
<h:inputText id="anoFabricacao"
value="#{automovelBean.automovel.anoFabricacao}"/>
<h:message for="anoFabricacao"/>
Ano do Modelo:
<h:inputText id="anoModelo"
value="#{automovelBean.automovel.anoModelo}"/>
<h:message for="anoModelo"/>
<h:panelGroup>
</f:ajax>
...
288
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 305

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
Aclasse Automovelpoderiaterumcódigoparecidocomoseguinte:
@Entity
public class Automovel {
...
@NotNull
private Integer anoFabricacao;
@NotNull
private Integer anoModelo;
...
}
DeacordocomocódigodoXHTML,cadavezquetirarmosofocode
algumcomponentequeaceiteoeventoDOM onblur,oJSFiráfazerumareq-
uisiçãoparaoservidorenviandoocomponentequeoriginouoevento,por
padrão,o execute="@this".
Comoretorno,todoo h:panelGroupcom id="dadosAutomovel"
seriarenderizadonovamente.Renderizartodoesse containernovamentesó
paramostrarumapossívelmensagemdeerroseriaumdesperdíciomuito
grandedeprocessamento.Asitua çãosónãoépiorporque,porpadrão,apro-
priedade executesóenviaocomponentequedisparaoeventoemquestão,
nocasoo onblur.
Umapossívelsolu çãoparaoproblemaseria:
<h:messages id="todasMensagens"/>
<f:ajax event="blur" render="todasMensagens">
<h:panelGroup id="dadosAutomovel">
...
Ano de Fabricação:
<h:inputText id="anoFabricacao"
value="#{auto.anoFabricacao}"/>
Ano do Modelo:
<h:inputText id="anoModelo"
value="#{auto.anoModelo}"/>
<h:panelGroup>
</f:ajax>
Comissocontinuamosenviandosomenteovalordecada h:inputText
enavoltarenderizamossomenteumcomponente,o h:messages. Con-
289
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 306

10.7. TornandooJSFmaislevecomusointeligentedeAJAX CasadoCódigo
tudo,essasolu çãonãoétãovisualparaousuárioquantoasanteriores,jáque
agora,paraqualquererroocorrido,emvezdeamensagemaparecerdolado
docampoqueoriginouoerro,apareceránotopodapágina.
Umasolu çãotãoeficientequantoessaúltima,equeaindaassimmostra
cadamensagemdeerroaoladodocampo,éaseguinte:
...
<f:ajax event="blur">
<h:panelGroup id="dadosAutomovel">
...
Ano de Fabricação:
<h:inputText id="anoFabricacao"
value="#{automovelBean.automovel.anoFabricacao}">
<f:ajax render="anoFabricacaoMsg"/>
</h:inputText>
<h:message id="anoFabricacaoMsg" for="anoFabricacao"/>
Ano do Modelo:
<h:inputText id="anoModelo"
value="#{automovelBean.automovel.anoModelo}">
<f:ajax render="anoModeloMsg"/>
</h:inputText>
<h:message id="anoModeloMsg" for="anoModelo"/>
<h:panelGroup>
</f:ajax>
...
Agora,o f:ajaxserveapenasparaespecificaroevento onblurcomo
padrão para os componentes dentro dele. Poderíamos também tirar o
f:ajaxqueenvolveosdemaiserepetir event="blur"nos f:ajaxin-
ternos.
Nessasduasúltimasop çõestemosumúnicocomponenteindo, eum
únicocomponentevoltandodoJSF.Écriadaumasubárvorecomumúnico
componentedentro,ecomovimosnase ção7.3,oJSFfazumasériedepro-
cessamentosbaseadoemsuaárvore.Quantomais inputstivermos,maisserá
290
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 307

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
necessárioconverter,validar,aplicarvalor;edepoismaisseráprecisopercor-
reraárvoregerandoHTMLcomoresposta.
10.8 Quando possível, manipule componentes
JSF no lado do cliente
Nase çãoanterior,revimostécnicasparafazeroajustefinodoqueéenviado
erecuperadodoservidor,atravésdeAJAX,paratermossomenteoprocessa-
mentonecessárioemcadarequisi ção.Maspodemosfazeraindamais.
UmacaracterísticadoJSFéquesuatelarefleteoestadodaárvoredecom-
ponentequeficanoservidor. Sendoassim,nãotemoscomosimplesmente
criarum <input type="text"> natelaviajavascript,umavezque,se
essecamponãofoicriadotambémnaárvoredoJSF,eleseráignorado.
Masmuitasvezeséinteressantetermosaalternativaderealizaralguns
controlesapenasnatela,semterquegerarumarequisi çãopara,porexemplo,
ocultaroumostrarumoutrocampo,tabelaououtrocomponente.
QuandousamoscomponentesdoPrimefaces,temosumafacilidadeque
éapresen çadapropriedade widgetVar. Elaexpõeumobjetojavascript
quepodemosmanipulardoladocliente,comopodemosfazercomqualquer
objetousandobibliotecasjavascriptcomoo jQuery.
CombinandoaAPIjavascriptquetemosvia widgetVareo jQuery,
podemosmanipularnossateladeformamuitoflexível.Vamosexplorarum
casosimplesdeumaaplica çãodevendadeingressos. Aocomprarmosum
ingresso,podemosinformarquetemosacessoaalgumaformadedesconto.
Dentreosmecanismosdedescontotemos: Estudante,Cartãodecréditoe
Idoso. Umapossívelimplementa çãodateladecompradeingressoseriaa
seguinte.
@Entity
public class VendaIngresso {
...
public enum TipoDesconto {ESTUDANTE, CARTAO_CREDITO, IDOSO}
private String nomeComprador;
291
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 308

10.8. Quandopossível,manipulecomponentesJSFnoladodocliente CasadoCódigo
@ManyToOne
private Evento evento;
private boolean vendaComDesconto;
private TipoDesconto tipoDesconto;
....
}
...
<h:selectBooleanCheckbox
value="#{ingressoBean.venda.vendaComDesconto}">
<f:ajax render="tipoDescontoPanel"/>
</h:selectBooleanCheckbox>
Compra com desconto?
<h:panelGroup id="tipoDescontoPanel">
<h:selectOneMenu value="#{ingressoBean.venda.tipoDesconto}"
rendered="#{ingressoBean.venda.vendaComDesconto}">
<f:selectItems value="#{IngressoBean.tiposDesconto}"
var="desconto" itemValue="#{desconto}"
itemLabel="#{desconto}"/>
</h:selectOneMenu>
</h:panelGroup>
Nãoprecisamosnementrarmuitoemdetalhesnessecódigo,afinalele
ébemsimplesetemcomoobjetivonoslembrardeumapráticacomumno
desenvolvimentocomJSF:arenderiza çãocondicionaldeumapartedatela,
queécombinadacomalgumarequisi çãoAJAXqueatualizaocomponente
queapareceousome.Pelanaturezasimplesdatela,otrechoqueapareceou
someépequeno,masemumatelacomplexapodenãoser.
Umaalternativaparaissoétrazerocomponentededescontoapenas
ocultoeentão,via jQuery,mostrá-losemanecessidadedequalquerrequi-
siçãoparaoservidor.
...
<h:form prependId="false">
<h:outputScript library="primefaces"
name="jquery/jquery.js" target="head"/>
292
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 309

CasadoCódigo Capítulo10. Truquesquepodemaumentaraescalabilidadeea...
<h:outputScript>
function atualizaValorDesconto(){
if ($("#temDesconto").is(":checked")) {
$("#tipoDesconto").show();
}
else {
$("#tipoDesconto").hide();
}
}
</h:outputScript>
<h:selectBooleanCheckbox id="temDesconto"
value="#{ingressoBean.venda.vendaComDesconto}"/>
Compra com desconto?
<span id="tipoDesconto" style="display: none;">
<h:selectOneMenu
value="#{ingressoBean.venda.tipoDesconto}">
<f:selectItems value="#{ingressoBean.tiposDesconto}"
var="desconto" itemValue="#{desconto}"
itemLabel="${desconto}"/>
</h:selectOneMenu>
</h:panelGroup>
</h:form>
Comessaaltera ção,nãoénecessárianenhumarequisi çãoadicionalpara
exibirocombocomasop çõesdedesconto. Decidirqualamelhorsolu ção
nãoétrivial,jáqueaequa çãoenvolvevariáveisdeseguran ça,performancee
manutenibilidadedocódigo.
10.9 Considerações finais sobre otimizações
Nãoédehojequeotemaotimiza çãocausafascínioemgrandepartedosde-
senvolvedores.Aoportunidadedereduzirotempodeprocessamentodeho-
rasparasegundos,oudemuitosminutosparamilissegundos,dáumasen-
saçãodepoder.Porém,abuscaporessasensa çãopodesetornarumvício,e
aotimiza çãoemexcessopodesetornarumadroga.
Muitasvezes,antesmesmodeseconheceraquantidadedeusuários,o
293
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 310

10.9. Consideraçõesfinaissobreotimiza ções CasadoCódigo
ambienteondeaaplica çãovaiexecutar, esemterconhecimentodastec-
nologiasenvolvidasnodesenvolvimentodaaplica ção,lan çamosmãodevel-
hoshábitosdeotimiza çãoqueconsideramosboaspráticas. Muitasdessas
boaspráticasinclusivefizeramsentidoemalgummomentodopassado,mas
muitasvezesnãofaznoprojetoatual.Nãoétãosimplesperceberissoquando
estamostentadosarepetirasensa çãodaotimiza ção.
Obviamenteexistemcasosexcepcionais,nosquaisrequisitosdeperfor-
manceextremosguiamtodoo designdaaplica ção,masamenosquevocê
trabalheemumlugarespecializadonessestiposdeaplica ção,elasserãoex-
ceção,enãoaregra.
Precisamosponderarperformanceversusmanutenibilidadedecódigo.
Nãoadiantamuitoganharummilissegundoeperderumasemanadede-
senvolvimentoedepoismaisváriashorastodasasvezesquealguémprecisar
voltaràquelecódigo.
Muitasvezes,pormaisqueaimplementa çãodaotimiza çãonãosejadifí-
cil,émaiscódigoparamanter,efazerdeterminadasotimiza çõesnãocom-
pensam. Somenteanalisandodetalhadamenteaaplica çãoéquepoderemos
saberoqueprecisaserotimizado.
294
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 311

Capítulo11
Conclusão
Asespecifica çõesdasquaisestelivrotratatrazemconsigoumpesoextrada
mudançadeparadigma.Écomumaindahojepensarqueorienta çãoaobjetos
éboaemteoria,masquandooassuntoéperformanceomelhoréabandonar
tudoepartirparacoisasespecíficasdebanco.Emumcasoououtroissoserá
verdade,masapropor çãocomqueissoéaconteceébembaixa,secomparada
aonúmerodevezesqueessahipóteseélevantada.
Igualmentetemosamudan çadeparadigmaquandotrabalhamoscom
JSF,jáqueodesenvolvimentoWebépredominantemente Action Based.Mas
vimosque,alémprodutivo,éperfeitamentepossíveldesenvolverusandoesse
frameworkeo Component Based.
Apesardesuasvantagens,nãoestamosatrásdo“santograal”,esabemos
quecadaferramentatemcenáriosondeelaéútileondeelanãoéamelhor
opção.Porexemplo,imagineumaaplica çãoquevocêestádesenvolvendo,na
qualsurgeanecessidadedeescreversuasprópriasinstru çõesSQL.Apesardas
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 312

CasadoCódigo
facilidadesqueumaferramentaORMoferece,podeserquevocêtenhaque
escreversuasSQLsemalgummomento.
Aquiaideianãoéotimiza çãodeperformance,afinal,nagrandemaioria
dasvezesissoconseguimosfazersemabrirmãodeumaferramentaORM,
comovimosnocapítulo10.
VocêachaqueseriainteressanteutilizarumaferramentacomoaJPAque
vaigeraroscomandosSQLsendoqueéjustamenteissoquevocêprecisacon-
trolar?Apesardeserpossívelalteraragera çãodoSQLdasprincipaisferra-
mentasORM,provavelmentenãoéissoquequeremosfazerquandoinici-
amosumprojeto.
UseiaJPAparaintroduzirumexemploquevaiservirparaoJSF.Imagine
agoraquevocêtemumaaplica çãowebondevocêprecisa–oudeseja–con-
trolaroHTMLfinal.Nessecaso,aquantidadedepessoasqueprecisamdisso
émuitomaiorquenoexemplocomSQL.Issoporqueexistemdiversostipos
deaplica ções,eemcadaumanecessidadedecontroledoHTMLfinalvaria
muito,comoumsite,portaletc.AnecessidadedecontroledoHTMLvisando
diversasotimiza çõesde pagespeed,layout,acessibilidadeeoutrosrequisitos
nãofuncionaisémuitogrande.
Agora pensando em aplicações web, basicamente composta de for-
mulárioscomplexos–oumesmosimples–,emqueéprecisoumcontrole
deestadomaiselaborado,comcadastrostãocomplexosqueprecisamserdi-
vididosemdiversaspáginas(comopassosdeumwizard),apreocupa çãocom
essesrequisitosnãofuncionaiscontinuamexistindo,masomaisimportante
éafuncionalidade.
OfatoéqueoJSFvaigeraroHTMLparavocê,assimcomoaJPAgera
oSQL.OproblemaéqueàsvezesaspessoaslutammuitocontraoHTML
geradopeloJSF,enquantodificilmentelutamcontraasSQLsdaJPA.Masveja
bem,“nãolutarcontra”emmomentoalgumsignificaabrirmãodosrequisitos
nãofuncionaisjácitados.Obviamente,aousarJPA,nãopodemosignorarse
estãoacontecendojoinsdesnecessáriosouN+1 queries.
Oqueprecisamosavaliaréqueprovavelmenteseremosmaisfelizesse
nãoprecisarmosalteraraformata çãodocomandoSQLemsi. Damesma
forma,nomesmocapítulo10,vimoscomoevitarrequisi çõesdesnecessárias
aoservidore,quandoarequisi çãofornecessária,comoevitaroprocessa-
296
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 313

CasadoCódigo Capítulo11. Conclusão
mentodesnecessáriopormeiodousoeficientedeAJAX.
Masaindaassim,vocêserámaisfelizsenãoprecisarcustomizartodoo
HTMLgerado.
OobjetivodolivrofoimostrartantoJSFquantoJPAdesdeseuusobásico,
atéseufuncionamentoemsitua çõesqueantesnãoentendíamos,ouapeláva-
mosparasolu çõesdecontorno.Porém,mostrarcomoduasespecifica çõestão
usadasfuncionamemdiferentesitua çõessemdeixardeserpráticoeobjetivo
nãoétarefafácil.Buscamossempreapresentarassolu çõesmaisutilizadasem
vezdeescrevercadapossibilidadequeaespecifica çãoecadaimplementa ção
proporcionam.
297
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 314

E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 315

Capítulo12
Apêndice:iniciandoprojetocom
eclipse
Nestelivrotratamosasferramentasdeformaindependentedeferramenta,
entãovocêpodeaplicarfacilmenteoqueforaprendidonasuaIDEpreferida.
Noentanto,visandofacilitaroiníciodoprojeto,veremoscomofazerissouti-
lizandoaIDEeclipse. Casoaindanãoatenhaemseucomputador,baixea
versão“forJavaEEDevelopers”nositedoprojeto(http://www.eclipse.org/
downloads/).
12.1 Adicionando o tomcat no eclipse
Parainiciaraconfigura ção,baixeaúltimaversãodoservidortomcat(http:
//tomcat.apache.org/)edescompacte-onodiretóriodesuapreferência.Não
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 316

12.1. Adicionandootomcatnoeclipse CasadoCódigo
énecessáriorealizarnenhumainstala ção. Nestelivroestamosutilizandoo
tomcat7.0.X,masversõesmaisnovasdeverãofuncionartambém.
No eclipse, vá até aview Servers e clique no linknew server
wizardcomonaimagemaseguir.
Fig.12.1:Adicionandootomcatnoeclipse
Napróximatela,selecioneoservidor Tomcat v7.0 ouodaversãoad-
equadaaoseutomcat.
Emseguida,cliquenobotão Browse...eselecioneolocalondevocê
descompactouotomcat.
Aofinal,na view Serversotomcatestáaparecendo.
300
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 317

CasadoCódigo Capítulo12. Apêndice:iniciandoprojetocomeclipse
Fig.12.2:Servidortomcatconfiguradonoeclipse
12.2 Criando o projeto web
Agoraqueoeclipsejáapontaparaoservidor,vamoscriarnossoprojetoweb.
Paraisso,cliquecomobotãodireitona view“ProjectExplorer”eselecionea
opção“DynamicWebProject”.
Apósdaronomedoprojeto,vamosconfiguraroJSFnoprojeto.Paraisso
basta,mudaraop çãonocomboindicadonafigura.
301
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 318

12.2. Criandooprojetoweb CasadoCódigo
Fig.12.3:ConfigurandooJSFnoprojeto
302
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 319

CasadoCódigo Capítulo12. Apêndice:iniciandoprojetocomeclipse
Fig.12.4:ConfigurandooJSFnoprojeto
DepoisdeselecionarmosoJSF,clicamosnobotão Next,quenoslevará
paraumatelaondepodemosconfigurarapastaondeficarãoosfonteseonde
ficarãooscompiladospeloeclipse. Deixaremostudonovalorpadrãoecli-
caremosnovamenteem“Next”.
Atelaqueapareceemsequênciaserveparaconfigurarmosondeoeclipse
iráobterosjarsdoJSF.Existeapossibilidadedebaixarmosdainternetvia
eclipse,masemvezdissovamosdesabilitaragerenciadosjarspeloeclipse.
303
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 320

12.3. BaixandoosjarsdoJSF CasadoCódigo
Fig.12.5:ConfigurandooJSFnoprojeto
Nessemomento,temosumprojetowebcriadoecomafuncionalidade
deJSFhabilitada.Porém,comodesabilitamosagestãodosjarspeloeclipse,
precisamosfazerodownloadmanualmente.
12.3 Baixando os jars do JSF
Umaformafácildeprocurarqualquerjarébuscandonorepositóriocentral
domaven(http://search.maven.org).
304
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 321

CasadoCódigo Capítulo12. Apêndice:iniciandoprojetocomeclipse
Fig.12.6:BuscandojarsdoJSF
Napágina,bastabuscarmospor com.sun.faceseváriasbibliotecas
JSFserãoencontradas.Baixeosjars jsf-imple jsf-apidaversãomais
atual.
Depois de baixarmos os jars, devemos colocá-los dentro da pasta
WebContent/WEB-INF/libdo nosso projeto. Pronto, agora você está
preparadoparacriarseusprojetosJSF.
12.4 Configurando a JPA
AgoraquenossoprojetojátemoJSFfuncionando,vamosconfiguraraJPA.
Aimplementa çãoqueutilizaremoséoHibernate. Parabaixá-lopodemos
acessarapáginadedownloaddoHibernate(http://hibernate.org/downloads)
.Vamosdescompactar zipbaixadoecolocarosjarsnoprojeto.
Depoisdebaixar,descompactamosoarquivoecopiamososjarsobri-
gatórios( required)etambémodaJPA.
305
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 322

12.4. ConfigurandoaJPA CasadoCódigo
Fig.12.7:CopiandojarsdoHibernate
Depois de copiar os jars, basta colocá-los na pasta
WebContent/WEB-INF/libdoprojeto,ejáteremosohibernatepronto,
faltandoapenasaconfigura çãodobancodedados,queaprendemosnase ção
2.2
Ocódigofontedolivroestádisponívelnogithub: https://github.com/
gscordeiro/faces-motors.
306
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 323

CasadoCódigo ÍndiceRemissivo
ÍndiceRemissivo
ABS,128
begin,36
binding,49
body,45
commandLink,64
commit,36
CONCAT,127
CURRENT_DATE,129
CURRENT_TIME,129
CURRENT_TIMESTAMP,129
dataTable,58
dialect,32
Entity,28
EntityManager,35
EntityManagerFactory,35
expressionlanguage,49
f:facet,62
f:setPropertyActionListener,179
faces-redirect,204
FacesMessage,197
Filter,144
form,45
GeneratedValue,28
h:body,45
h:column,60
h:commandButton,48
h:form,45
h:inputText,46
h:inputTextarea,46
h:panelGrid,47
hibernate.hbm2ddl.auto,33
html,23
Id,28
ImpedânciaObjeto-Relacional,5
ImpedanceMismatch,5
INDEX,128
JavaPersistenceAPI,13
JBoss,55
JDBC,6
JPA,13
LENGTH,127
LOCATE,127
LOWER,127
MOD,128
namespace,44
namingcontainer,162
navigation-case,202
307
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 324

ÍndiceRemissivo CasadoCódigo
navigation-rule,202
Persistence,35
persistence-unit,30
persistence.xml,30
POJO,49
PreparedStatement,7
prependId,162
rendered,172
ResultSet,8
rollback,36
Session,12
SIZE,128
SQRT,128
SUBSTRING,127
Taglib,44
Tomcat,55
Transaction,36
TRIM,127
UPPER,127
Vendorlock-in,13
where,127
xhtml,23
308
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com

## Página 325

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
309
E-book gerado especialmente para Douglas Gusson - douglasgusson@gmail.com