---json
{
  "id": "java_ee_aproveite_toda_a_plataforma_para_construir_aplica__es",
  "title": "Java EE Aproveite toda a plataforma para construir aplicações",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Java EE Aproveite toda a plataforma para construir aplicações.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "aproveite",
    "construir",
    "java",
    "linguagens",
    "para",
    "plataforma",
    "toda"
  ],
  "perguntas_tipo": [
    "Como utilizar Java EE Aproveite toda a plataforma para construir aplicações?",
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

# Java EE Aproveite toda a plataforma para construir aplicações

> **Arquivo Original:** `Java EE Aproveite toda a plataforma para construir aplicações.pdf`
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

## Página 3

CasadoCódigo
Agradecimentos
EsteéosegundolivroqueescrevopelaCasadoCódigoeasatisfaç ãoéimensa.
Serumdosautoresdaeditoraquedesburocratizouacriaç ãodelivrosnopaís
éumaenormehonra.Porcontadisso,meuprimeiroagradecimentovaino-
vamenteparaPauloeAdriano,pormedaremespaçoparaescrever.
Vouaproveitarparatambémdeixarosagradecimentosaosmeuspais,
donaSebastianaeseuAlberto!Sempremeincentivaramaestudare,deixa-
rambemclaroparamim,queaúnicacoisaqueninguémpodetirardevocê
éoconhecimentoadquirido. Achoquenuncavouconseguirdemonstraro
quantoissofoirelevante.
Porúltimo,queroagradeceravocê,quetemsededeconhecimentoequer
estarsempreaprendendo.Sãodepessoasassimqueomundoprecisaeeues-
pero,sinceramente,quecadagotadesuordirecionadoparaseuaprendizado
setransformeemumpassoamaisdadonasuacarreira.
i

## Página 5

CasadoCódigo
Autor
AlbertoSouzaéBacharelemCiênciadaComputaçãopelaUniversidadeSal-
vadoredesenvolvedordesde2005,tendoparticipadodemuitosprojetosweb
eexperimentadodiversaslinguagens.Participadeprojetosopensourcecomo
oStellaeVRaptor.PossuiacertificaçãoSCJPetrabalhacomodesenvolvedor
einstrutorpelaCaelum.SeuTwitteré@alberto_souzaevocêtambémpode
encontrá-lonoGitHub,noendere çohttp://www.github.com/asouza. Tam-
béméumdosfundadoresdoprojetoSetupMyProject,umaaplicaçãowebque
vemajudandodiversosdesenvolvedoresacriaremprojetosJAVAdemaneira
bastantesimples.
Alémdejáterescritooutroslivros, Play Framework na prática: Gaste
tempo no que é preciosoeo Spring MVC: Domine o principal framework web
Java,eletambémpossuidoisblogssobretecnologia. Umespecíficosobre
oSpring(http://domineospring.wordpress.com)eoutroqueeledesvendaos
detalhesportrásdeváriastecnologiasquesãousadasnosprojetos(http://
setupmyproject.wordpress.com).
iii

## Página 7

CasadoCódigo
Público-alvo
Estelivroéparapessoasquejáconhe çamumpoucosobreaestruturade
umprojetowebutilizandoalinguagemJAVA.OmínimodeJSFvaiajudar
paraquevocêconsigaacompanharaconstruçãodaaplicaçãoWEBdeuma
maneiramaisfluida,masfiquetranquilo,poistudodoJSFseráexplicadopara
você.Quasetodocapítulovaicobrirdetalhesquevãoalémdousonormale
vaideixá-lomaiscríticoemrelaçãoaousodatecnologia.
ConsideretambémqueolivroésobreoJAVAEEcomoplataforma,então
existemváriasoutrasespecificaçõesqueserãocobertasequelhedeixarámais
embasadoparatomarsuasfuturasdecisõesemrelaç ãoàplataforma.
v

## Página 9

CasadoCódigo Sumário
Sumário
1 Introdu ção 1
1.1 PorqueoJavaEE? . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 SpringxJavaEE . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 Comeceaaventura . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Público-alvo . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.5 Curiosidade:porqueJSFcomoframework? . . . . . . . . . . 5
1.6 Vamoslá?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 Come çando o projeto 7
2.1 Configuraçãoecriaçãodoprojeto . . . . . . . . . . . . . . . . 7
2.2 Acessandooprimeiroendere ço. . . . . . . . . . . . . . . . . 25
2.3 Umpoucopordentrodoframework . . . . . . . . . . . . . . 29
2.4 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3 Cadastro de produtos 33
3.1 Formuláriodecadastro . . . . . . . . . . . . . . . . . . . . . . 33
3.2 Lógicadecadastro . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.3 Gravandoosdadosnobancodedados . . . . . . . . . . . . . 38
3.4 ConfigurandoaJPA . . . . . . . . . . . . . . . . . . . . . . . . 42
3.5 ConfiguraçãodoDataSourcenoWildlFly . . . . . . . . . . . 46
3.6 Anecessidadedeumatransação . . . . . . . . . . . . . . . . . 54
3.7 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
vii

## Página 10

Sumário CasadoCódigo
4 Melhorando o cadastro e um pouco mais de JSF 59
4.1 Associandováriosautores . . . . . . . . . . . . . . . . . . . . 60
4.2 Limpandooformulário . . . . . . . . . . . . . . . . . . . . . . 67
4.3 Listandooslivros . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.4 ForwardxRedirect . . . . . . . . . . . . . . . . . . . . . . . . 70
4.5 Exibindoamensagemdesucesso . . . . . . . . . . . . . . . . 73
4.6 Isolandoocódigodeinfraestrutura . . . . . . . . . . . . . . . 76
4.7 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
5 V alidação e conversão de dados 83
5.1 Validaçãobásica . . . . . . . . . . . . . . . . . . . . . . . . . . 83
5.2 Exibindoasmensagensdeerrodemaneiraamigável . . . . . 87
5.3 TrocandoasmensagensdefaultdoJSF . . . . . . . . . . . . . 90
5.4 IntegraçãocomaBeanValidation . . . . . . . . . . . . . . . . 92
5.5 Convertendoadata . . . . . . . . . . . . . . . . . . . . . . . . 96
5.6 Converterparaentidades . . . . . . . . . . . . . . . . . . . . . 101
5.7 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
6 Upload de arquivos 109
6.1 RecebendooarquivonoManagedBean . . . . . . . . . . . . 109
6.2 Salvandoocaminhodoarquivo . . . . . . . . . . . . . . . . . 114
6.3 Gravandoosarquivosforadoservidorweb . . . . . . . . . . 117
6.4 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
7 Carrinho de compras 127
7.1 Exibindooslivrosnapáginainicial . . . . . . . . . . . . . . . 127
7.2 Navegandoparaodetalhedoproduto . . . . . . . . . . . . . 131
7.3 LidandocomLazyInitializationException . . . . . . . . . . . 139
7.4 SeráqueomelhoréoDAOserumEJBstateful? . . . . . . . 143
7.5 Formatandoadatadepublicação . . . . . . . . . . . . . . . . 145
7.6 Carrinhodecompraseoescopodesessão . . . . . . . . . . . 146
7.7 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
viii

## Página 11

CasadoCódigo Sumário
8 Fechamento da compra e processamento assíncrono 157
8.1 Implementandoateladefinalização . . . . . . . . . . . . . . 157
8.2 Gravandoasinformaçõesdousuário . . . . . . . . . . . . . . 162
8.3 ValidaçãoseletivacomaBeanValidation . . . . . . . . . . . . 167
8.4 Salvandoasinformaçõesdocheckout . . . . . . . . . . . . . . 173
8.5 Integrandocomoutraaplicação . . . . . . . . . . . . . . . . . 178
8.6 Executandooperaçõesdemoradasassincronamente . . . . . 183
8.7 JAX-RSparatodasasoutrasrequisiçõesHTTP . . . . . . . . 187
8.8 ConfigurandooJAX-RS . . . . . . . . . . . . . . . . . . . . . 193
8.9 Curiosidade:usandoumExecutorServicegerenciado . . . . 194
8.10 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
9 Melhorando a performance com cache 197
9.1 CacheandooretornodasconsultasnaJPA . . . . . . . . . . . 197
9.2 Providerdecacheesuasconfigurações . . . . . . . . . . . . . 204
9.3 Invalidaçãodocacheporalteração . . . . . . . . . . . . . . . 205
9.4 Cacheandotrechosdapágina . . . . . . . . . . . . . . . . . . 206
9.5 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209
10 Respondendo mais de um formato 211
10.1 Expondoosdadosemoutrosformatos . . . . . . . . . . . . . 211
10.2 Contentnegotiation. . . . . . . . . . . . . . . . . . . . . . . . 219
10.3 Simulandoumclienteparaonossoserviço . . . . . . . . . . 220
10.4 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
11 Mais de processamento assíncrono com JMS 225
11.1 Enviandooe-maildefinalização . . . . . . . . . . . . . . . . 225
11.2 Umpoucomaissobreprocessamentoassíncrono . . . . . . . 232
11.3 UtilizandooJMSparamensageria . . . . . . . . . . . . . . . . 235
11.4 RegistrandotratadoresdemensagenscomMDBs . . . . . . . 239
11.5 ImplementaçãodoJMSutilizadapeloWildFly . . . . . . . . 245
11.6 Cautelanousodocódigoassíncrono . . . . . . . . . . . . . . 245
11.7 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
ix

## Página 12

Sumário CasadoCódigo
12 Protegendo a aplicação 247
12.1 DefinindoasregrasdeacessocomoJAAS . . . . . . . . . . . 248
12.2 Configurandooformuláriodelogin . . . . . . . . . . . . . . 250
12.3 ConfigurandooLoginModuledoJAAS . . . . . . . . . . . . 254
12.4 Exibindoousuáriologadoeescondendotrechosdapágina . 260
12.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
13 Organização do layout em templates 269
13.1 Templates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
13.2 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
14 Internacionalização 277
14.1 Isolandoostextosemarquivosdemensagens . . . . . . . . . 278
14.2 Accept-Languageheader . . . . . . . . . . . . . . . . . . . . . 281
14.3 Passandoparâmetrosnasmensagens . . . . . . . . . . . . . . 282
14.4 Deixequeousuáriodefinaalíngua . . . . . . . . . . . . . . . 283
14.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
15 Enviando e recebendo informações via WebSocket 289
15.1 Comonotificarosusuários? . . . . . . . . . . . . . . . . . . . 289
15.2 APIdeWebSocketseonavegador . . . . . . . . . . . . . . . . 290
15.3 Enviandomensagensapartirdoservidor . . . . . . . . . . . 293
15.4 OutrosdetalhesdaespecificaçãodeWebSockets . . . . . . . 302
15.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303
16 Últimas considerações técnicas 305
16.1 Deploy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 305
16.2 Profiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
16.3 Testes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
16.4 Projetosparalelosquepodemnosajudar . . . . . . . . . . . . 309
16.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 310
17 Hora de praticar 311
17.1 Estudamosmuitosassuntos! . . . . . . . . . . . . . . . . . . . 312
17.2 Mantenhacontato . . . . . . . . . . . . . . . . . . . . . . . . . 312
x

## Página 13

Capítulo1
Introdução
Pormuitotempo,aespecificaçãoJavaEE(Java Enterprise Edition)ficouco-
nhecidacomosendoalgoextremamentecomplexodeserentendido. Caso
vocêtenhatrabalhadocomasprimeirasversõesouconhecealguémquetra-
balhou,deveselembrardacomplicaçãoqueeraconfigurarcadaumadastec-
nologias,etambémoquãotrabalhosoerafazê-lasfuncionarememconjunto.
Poisbem,essaslembran çasficaramemumpassadodistante. Osurgi-
mentodeoutrosframeworksnomercado,notoriamenteoSpring,fizeram
comqueasempresasresponsáveisporevoluiraespecificaç ãosemovimen-
tassem.
Desdeaversão5,oJavaEEvemevoluindoapassoslargostantopelolado
daconfiguraçãodastecnologiasenvolvidasquantopeloprismadaintegraç ão
entreelas.ComaentradadoCDI(Context Dependency Injection)naversão
6,asintegraçõespararamdegiraremtornodosEJBs(Enterprise JavaBean)
etudoficoumaissimplesdesertrabalhado.Aversão7,queéaatual,deixou

## Página 14

1.1. PorqueoJavaEE? CasadoCódigo
tudoaindamaisfácil,etrouxenovasmelhoriasnoCDI,alémdetambém
deixarmuitomaissimplesaintegraçãocomsistemasdemensageria.Eesses
sãoapenasdoisdosexemplos.
Comtodaessadesburocratização,astecnologiasenvolvidasnaespecifica-
çãoe,porconsequência,osservidoresqueasimplementam–comooWildfly
(antigoJboss)–,alçaramnovosvoos.Hoje,aquelahistóriaqueJavaEEerasó
paraempresasgigantesnãoémaisválida.Qualquertipodeaplicaç ão,dentro
dequalquerempresa,podetirarproveitodaúltimaversãodaespecificaç ão.
Apartirdeagora,tudooqueeucomentarérelativoàversão7doJava
EE.Seemalgummomentoeuprecisarreferenciaroutraversão,vocêserá
devidamenteavisado.
1.1 P or que o Jav aEE?
Quasetodasasaplicaçõespossuemcertasfuncionalidadesqueexigemum
certoconjuntodetecnologias,quevivemserepetindoentreelas. Alguns
exemplosmaiscomunssão:
• Mandare-mail;
• Gravardadosnobancodedados;
• Fazerasegurançadaaplicação;
• Exporaaplicaçãonaweb.
Podemostambémpensaremtecnologiasnecessáriasparaoutrasfuncio-
nalidades,vistasmaiscomumenteemaplicaçõesmaiores:
• Integraçãoviamensageria;
• IntegraçãoviaREST;
• WebSocketsparaalertarusuáriossobrealgo;
• Realizaçãodetarefasassíncronas.
2

## Página 15

CasadoCódigo Capítulo1. Introdução
Vocêprovavelmentejácaiu(ouvaicair)emumaaplicaçãoquedemande
aintegraçãodemuitasdascoisasqueacabamosdelistar. Eénessetipode
cenárioquepossuirumservidorquejátraztodasessasimplementaçõesde-
cididaspodeajudarbastante.
DêumaolhadanoconjuntodeespecificaçõesquecompõemoJavaEE7.
Fig.1.1:EspecificaçõesdoJavaEE
Percebaquesãomuitascoisas,etudoissoéentregueprontoparavocê.
Nãovamossermentirososedizerquetudovaifuncionarlindamentesem
nenhumagotadesuor,mas,hojeemdia,otrabalhoparaconfiguraretirar
proveitodecadaumadelasestámuitomenor. Vocêficarásurpresocoma
facilidadecomquequasetodasnossasfuncionalidadesserãoimplementadas!
Baseadonessaevolução,escolherumservidorJavaEEparasuapróxima
aplicaçãoéumaconsideraçãoquesefaznecessária,mesmosabendoquea
competiçãocontinuaacirrada,jáqueoscompetidores,comooSpring,não
pararamdeevoluirtambém.
Umoutropontoaltamenterelevanteéoquantodeajudavocêpodeobter
atravésdainternet.Nesseponto,osprojetosrelacionadosaoJavaEE,comoo
JSF(JavaServer Faces),tambémsebeneficiambastante.
3

## Página 16

1.2. SpringxJavaEE CasadoCódigo
1.2 S pring x Jav aEE
Essaéumaoutradiscussãoquequasesempreacabaaparecendo. Hámuito
tempo,nasprimeirasversõesdoJavaEE,nãotinhacomparaç ão,oecossis-
temadoSpringerarealmenteumaalternativamelhor.Nemeramuitosim-
plesdeconfigurarcomoéhoje,mas,mesmoassim,eramuitomaisfácildo
quequalquercoisanecessáriaparaoJavaEE.
Nosdiasdehoje,asduasfrentesestãomuitofortes.Ambaspossuemim-
plementaçõesquesedestacamfrenteàconcorrentee,comisso,adecisãode
seguirporumladooupelooutrodevesertomadacombasenoqueoseu
projetoprecisa.
MinhafunçãocomestelivroéfornecerumavisãopragmáticasobreoJava
EE.Nãoescondereinadaevocêmesmoserácapazdeavaliarqualconjunto
detecnologiasémelhorparaasuaempresaouparaopróximoprojeto.Não
éàtoaqueeutambémjáescreviolivro Spring MVC: Domine o principal
framework web Java,pelaCasadoCódigo.Melhordoquenosapaixonarmos
pelatecnologiaésabermostirarproveitodelasemfun çãodocenárioquese
apresenta.
1.3 C omece a aventura
Duranteolivro,vamosconstruirumaaplicaçãomuitoparecidacomopróprio
sitedaCasadoCódigo.Desenvolveremosfuncionalidadesquenoslevarãoao
usodediversasdasespecificaçõesdoJavaEE,como:
•Bean validationparavalidarmososnossosdados;
• ProcessamentoassíncronoviaJMS;
• JSF2.2ealgumasdassuasnovidades,comoaintegraçãocomoHTML
5;
• WebSocketsparanotificarmosusuáriosdepromoçõesrelâmpagos;
• CDIparaisolarmosacriaçãodecomponenteseajudarmosnacompo-
siçãoderegrasdenegócios;
4

## Página 17

CasadoCódigo Capítulo1. Introdução
• JAX-RSparapossibilitarmosintegraçõesviaREST;
• JPAparaacessoabancodedados,alémdesuaAPIdecache;
• UmpoucosobreEJBseumcasodeusobeminteressante;
• JAASparaadicionarmosautenticaçãoeautorização;
• JavaMailparamandarmose-mailsdefinalizaçãodecompra.
• JTAparacontrolarmosastransações.
• UmpoucosobreaConcurrencyUtilitiesAPIparatermosThreadsge-
renciadaspelocontainer.
• OsuficientesobreaJNDIparaconseguirmosbuscarosobjetosneces-
sáriosdentrodoservidor.
1.4 P úblico-alvo
Opúblicoseriaaspessoasquejáconhecemumpoucosobreaestruturade
umprojetobaseadonoDesignPatternMVC,atravésdoJSF.Omínimode
JSFajudarávocêaconseguiracompanharaconstruçãodaaplicaçãoWEB.
Masfiquetranquilo,poistudoalémdobásicodoJSFseráexplicadopara
você.Quasetodocapítulovaicobrirdetalhesquevãoalémdousonormale
vaideixá-lomaiscríticoemrelaçãoaousodatecnologia.
1.5 C uriosidade:por que JSF como framework?
AnossaaplicaçãowebvaiserbaseadanaCasadoCódigoe,talvez,algunsde
vocêspensem:porqueseráusadooJSF?Elenãoémaiscomumenteusado
emsistemaswebque,naverdade,funcionamquasecomosistemasdesktop?
Sim,issoéverdade.Emcontrapartida,oJSF2.2evoluiuemrelaç ãoaocon-
troledoHTMLgerado,dando-nosapossibilidadedeconstruirpáginasmais
condizentescomasnecessidadesatuais.
Alémdisso,duranteolivro,seráusadaumaabordagemquedeixaráoJSF
maispróximodosframeworks Action Basedcomquesomosacostumados,
5

## Página 18

1.6. Vamoslá? CasadoCódigo
mesmoelesendoumframeworkmuitoconhecidoporserbaseadoemcom-
ponentes,ofamoso Component Basead.
Complementando, eleéumadasespecificaçõesoficiaisdoJavaEEe,
comonolivrovamosdiscutiraespecificaç ão,nadamaisjustoqueusarmosa
tecnologiaindicadaporela.
Não fique perdido!
Todoocódigo-fontedolivroestádisponívelnoGitHub,bastaacessar
oendereçohttps://github.com/asouza/casadocodigojavaee.
Fiqueàvontadeparanavegarpelosarquivosdoprojeto.Os commits
foramdivididosdeacordocomoscapítulosdolivro,justamenteparaque
vocêpossaacessarocódigocompatívelcomocapítuloqueestejalendo.
Alémdisso,foicriadoumgrupodediscussão,noqualvocêpodepos-
tartodasassuasdúvidasreferentesàleitura.Paraacessá-lo,bastaseguir
estelink: https://groups.google.com/forum/#!forum/livro-javaee.
1.6 V amos lá?
Fiquejuntocomigoeleiacadacapítulocomcalma;eusemprelhedireiseé
horadedarumapausaoudejápularparaopróximo.Esperoquevocêtenha
umagrandejornada!
6

## Página 19

Capítulo2
Começandooprojeto
2.1 C onfiguração e criação do projeto
Oobjetivodolivroéconstruirumaaplicaç ãosemelhanteàdaprópriaCasa
doCódigo.Porserumsitede e-commerce,aaplicaçãonosforneceachance
deimplementardiversasfuncionalidades.Alémdisso,éumdomínioquenão
vainoscausarmuitasdúvidas.
Nofinaldolivro,anossaaplicaç ãoteráaseguintecara:

## Página 20

2.1. Configuraçãoecriaçãodoprojeto CasadoCódigo
Fig.2.1:SitedaCasadoCódigo
Aprimeiracoisaqueprecisamosfazeréjustamentecriareconfiguraro
mínimonecessárioparaternossaaplicação,rodandocorretamentecomo
JSF.ComovamosusaroMavenparagerenciarasnossasdependências,so-
mosobrigadosacriaroprojetoseguindoumaestruturadeterminadaporessa
ferramenta.
Olayoutdaspastas,comodecostume,vaiseguiroseguinteformato:
8

## Página 21

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.2:Estruturadaspastas
Provavelmente,vocêjádeveterfeitoestaatividadealgumasvezes,então,
paramudarumpoucoasuarotina,vouutilizarummodoumpoucodiferente
decriaroprojeto.UsaremosumprojetodaRedHat,chamado Jboss Forge,
quepodeserbaixadoem http://forge.jboss.org/download.
OJbossForgefornecevárioscomandosprontosparaacriaçãodeprojetos.
Apósbaixado,extraiaoarquivoemumapastadesuapreferência. Acesseo
terminaldoseucomputadoredigiteoseguintecomando:
$caminhoParaSuaInstalacao/bin/forge
Issoabriráumaaplicaçãonopróprioconsole.
Fig.2.3:ConsoledoForge
9

## Página 22

2.1. Configuraçãoecriaçãodoprojeto CasadoCódigo
Agora,bastaquedigitemosocomandoresponsávelpelacriaç ãodopro-
jeto.
project-new --named casadocodigo
Pronto! IssoésuficienteparavocêcriaroseuprojetobaseadonoMa-
ven. Aestruturadepastasjáestápronta,sóprecisamosrealizarasdevidas
configurações.
Dependências necessárias
Precisamosadicionartodasasdependênciasnecessáriasparaqueseja
possívelcomeçarmosatrabalharnoprojeto. Essajáéumadaspartesbem
interessantesdetrabalharemumprojetofortementebaseadonasespecifica-
çõesdoJavaEE.
Comoquasetodasasdependênciasimportantesjávêmprontasdentrodo
servidorquevamosusar,nósquasenãoprecisamosalteraro pom.xml.Para
nãoficarmosperdendotemporealizandoessasconfigurações,vamosmais
umavezutilizaroconsoledo Forge.
EntrenapastacriadaparaoseuprojetoerodeoForgemaisumavez.De
dentrodoconsole,escrevaoseguintecomando:
faces-setup --facesVersion 2.2
Depoisdaexecução,deveaparecerumamensagemdesucesso,parecida
comessa:
**SUCCESS** JavaServer Faces has been installed.
Semesforçonenhum,acabamosdecriartudooqueénecessárioparater
nossoprojetocomJSFrodando.
Comonãoqueremosusarconfiguraçõesdasquaisnãotemosconheci-
mento,vamospassearpelasalteraçõesrealizadaspelocomando.Umprimeiro
arquivoquepodemosolharéo pom.xml,responsávelporgerenciarnossas
dependências.
<dependencyManagement>
<dependencies>
10

## Página 23

CasadoCódigo Capítulo2. Começandooprojeto
<dependency>
<groupId>org.jboss.spec</groupId>
<artifactId>jboss-javaee-6.0</artifactId>
<version>3.0.2.Final</version>
<type>pom</type>
<scope>import</scope>
</dependency>
<dependency>
<groupId>javax.faces</groupId>
<artifactId>javax.faces-api</artifactId>
<version>2.2</version>
<scope>provided</scope>
</dependency>
</dependencies>
</dependencyManagement>
<dependencies>
<dependency>
<groupId>javax.faces</groupId>
<artifactId>javax.faces-api</artifactId>
<scope>provided</scope>
</dependency>
</dependencies>
Aqui, as dependências foram geradas com a tag
dependencyManagement. Esta geralmente é usada quando estamos
nospreocupandoemcriarprojetosquepodemprecisardasmesmascon-
figurações de um certo projeto “pai”. Não é o nosso caso, mas também
nãointerfereemnadanonossotrabalho,inclusivevocêpodeatéapagaro
conteúdodela.Aúnicacoisaemquetemosdeprestaraten çãoéque,quando
fornecessárioadicionarnovas libsmanualmente,vamossempreusara
tag <dependency>dentroda <dependencies>.Sóoqueestádentrode
<dependencies>érealmenteimportadoparaoprojeto.
Aindaemrelaçãoàsdependências,percebaqueeleadicionouaespeci-
ficaçãodoJSFcomoescopo provided. Comovamosrodarnossocódigo
dentrodeumservidordeaplicação,nocasooWildfly,todasessasbibliotecas
jáestarãodisponíveis. Sóadeixamosno pom.xml,porquevamosprecisar
usarasclassesdentrodonossoprojeto.Também,paraqueaIDE(Integrated
11

## Página 24

2.1. Configuraçãoecriaçãodoprojeto CasadoCódigo
Development Environment)compile,elaprecisaráteracessoaos jars,pelo
menosemtempodecompilação.
Além desse arquivo, também foi gerado um outro, chamado
faces-config.xml, criado na pasta WEB-INF. Mais para a frente,
vamos usá-lo para realizar configurações relativas ao JSF; por enquanto,
segureaansiedade.
Habilitando o CDI
Comojácomentamos,oCDIéaespecificaçãoquefazacolaentreasdi-
versasespecificações.Comonãopoderiaserdiferente,vamosusá-laintensa-
menteduranteaconstruçãodenossoprojeto.Porcontadisso,éinteressante
jádeixaressepassoconfigurado.
Denovo,vamosusaroForgeparagerarasconfiguraçõesnecessárias.
Dentrodoconsole,executeoseguintecomando:
cdi-setup --cdiVersion 1.1
Maisumavez,o pom.xmlfoialterado,agoraparaadicionarasdepen-
dênciasnecessáriasparaoCDI,emaisumavezelasforamconfiguradascomo
provided,jáqueestarãodisponíveisdentrodonossoservidordeaplicações.
<dependencyManagement>
...
<dependency>
<groupId>org.jboss.spec</groupId>
<artifactId>jboss-javaee-6.0</artifactId>
<version>3.0.2.Final</version>
<type>pom</type>
<scope>import</scope>
</dependency>
<dependency>
<groupId>javax.enterprise</groupId>
<artifactId>cdi-api</artifactId>
<version>1.1</version>
<scope>provided</scope>
</dependency>
...
12

## Página 25

CasadoCódigo Capítulo2. Começandooprojeto
</dependencyManagement>
<dependencies>
<dependency>
<groupId>javax.enterprise</groupId>
<artifactId>cdi-api</artifactId>
<scope>provided</scope>
</dependency>
</dependencies>
Alémdisso,dentrodapasta WEB-INF,foicriadomaisumarquivo,dessa
vezo beans.xml.
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<beans xmlns="http://xmlns.jcp.org/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
bean-discovery-mode="all" version="1.1"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd" />
EsteéoarquivonecessárioparahabilitarofuncionamentodoCDIno
seuprojeto. Presteatençãonoatributo bean-discovery-mode,eleestá
configuradocomovalor all. Issoquerdizerquetodaclassecriadaden-
trodonossoprojetoserácarregadaecontroladapelaimplementaç ãodoCDI
queseráusada.Vocêserálembradodissoquandocome çarmosrealmentea
produzirocódigo.
PercebaqueousodoForgenospoupouumpoucodetrabalhodeterde
ficarcriandoosarquivosecolocando-osnosseusdevidoslugares. Éuma
ferramentamuitoboa,evocêpodeautomatizardiversos setupsdosseuspro-
jetos.
Importando o projeto para a IDE
ComoestamosusandooWildflyeescrevendoumprojetobaseadono
JavaEE,vousugerirquevocêtenhamaisumaexperiênciadiferenteeuseo
JBoss Developer Studio.EleéumaIDEbaseadanoEclipse,ecustomizada
pelaRedHatparaatenderquemdesejatrabalharmaisintensamentecomo
13

## Página 26

2.1. Configuraçãoecriaçãodoprojeto CasadoCódigo
JavaEE.Casoopteporela,odownloadpodeserrealizadoem http://www.
jboss.org/products/devstudio/download/.
DiferentedoEclipsetradicional,oDeveloperStudiotrazum wizardde
instalação.Bastaseguirospassossugeridosporele.
Vejaalgumastelasquesãoimportantes:
Fig.2.4:Primeiropassodainstalação
14

## Página 27

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.5:Escolhasuapastadeinstalaç ão
15

## Página 28

2.1. Configuraçãoecriaçãodoprojeto CasadoCódigo
Fig.2.6:OutrospluginsdaRedHatnãosãonecessários
Vamosimportaroprojetocomoum Maven Project;assim,paracada
novadependêncianecessária,bastaalterarmoso pom.xml,eaprópriaIDE
seencarregarádeatualizaronosso classpath.
Fig.2.7:Selecioneaop çãoimport
16

## Página 29

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.8:EscolhaoMavenProject
17

## Página 30

2.1. Configuraçãoecriaçãodoprojeto CasadoCódigo
Fig.2.9:Aponteparaoendere çoondeseuprojetofoicriado
Pronto,agoratemosnossoprojetoimportado.Oúltimopassoéadicioná-
loaumservidor,paraquepossamosrealizarnossostestesevercomoaapli-
caçãovaiandando.
Paraisso,vamosseguirocaminhopadrãodecriaç ãodeservidoresdentro
doEclipse. Apenasparanoslocalizarmos,ospróximospassosdeverãoser
realizadosnaaba ServersdoseuEclipse.
18

## Página 31

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.10:Cliquenolinkdecriaç ãodeservidores
Fig.2.11:SelecioneoWildFly,ecliquenomenuJbossComunity
19

## Página 32

2.1. Configuraçãoecriaçãodoprojeto CasadoCódigo
Fig.2.12:Deixetudonovalordefault
20

## Página 33

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.13:Aponteparaocaminhodeinstalaç ãoeuseostandalone-full.xml
Paraqueessepassosejapossível,vocêdeverealizarodownloaddoWild-
fly,quepodeserencontradoem http://wildfly.org/downloads/.Pegueaver-
são 8.2.0.Final.
21

## Página 34

2.1. Configuraçãoecriaçãodoprojeto CasadoCódigo
Versões do WildFly
Apartirdaversão8.x,oWildFlycome çouaimplementaraespecifi-
caçãodoJavaEE7.Duranteolivro,vamosusaraprópriaversão8,mas
fiqueavontadeparatestarnovasversõesquetambémimplementama
especificaçãodo7.Tudodevefuncionarnormalmente.
Alémdisso,owizardpedequenósutilizemosoarquivodeconfiguraç ão
chamado standalone.xml. Oproblemaéqueelenãocarregatodosos
módulosdaespecificaçãoqueserãonecessáriosparaodesenvolvimentoda
aplicação. Porexemplo,mesmonãosendoimportanteagora,maisàfrente
nolivroseráusadoumrecursochamadodemensageria,quenãoestáconfi-
guradonestearquivo.
Paraevitarterdecome çaralterandoumarquivoedepoisterdeutilizar
outro,játroqueessaopçãopelo standalone-full.xml.Porfim,adicione
oprojetonoservidor.
22

## Página 35

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.14:Adicioneoprojetonoservidor
Associe um servidor ao projeto
VamosprecisardasAPIsdoJavaEEqueestãodisponíveisdentrodoser-
vidor.Atéagora,temosusadooForgeparaconfigurareadicionarasdepen-
dênciasnecessáriasdentrodonosso pom.xml,paraquepossamoscompilar
nossocódigo.Issoéútilapenasquandooutrosarquivosprecisamsergerados.
Duranteváriosmomentos,vamosprecisarapenasteracessoàsinterfaces
daespecificação.ParagarantirmosquesóvamosusaroForgequandoreal-
mentefornecessário,vamosadicionaras libsdisponíveisnoWildflydentro
donossoprojeto.
23

## Página 36

2.1. Configuraçãoecriaçãodoprojeto CasadoCódigo
Fig.2.15:MenudealteraçãodoBuildPath
Fig.2.16:ServerRuntimelibraries
24

## Página 37

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.17:SelecioneoWildFly
2.2 A cessando o primeiro endereço
Comtudoconfigurado,chegouahoraderealmentecome çarmosaproduzir
algumacoisa!Onossoprimeirodesafioélevarousuárioparaateladecadas-
trodelivrosdaCasadoCódigo.Oendere çoquequeremosqueeledigiteéo
/produtos/form.xhtml.
Nestemomento,casoousuáriodigite http://localhost:8080/casadocodigo/
produtos/form.xhtml,elereceberáumerrodoservidorindicandoqueesseen-
dereçonãopodeseratendidoporninguém.
Então, por mais óbvio que isso pareça, precisamos criar uma página
que fique acessível pelo navegador. Podemos criar uma pasta chamada
produtosdentrode WebContente,ládentro,criamosoarquivochamado
25

## Página 38

2.2. Acessandooprimeiroendereço CasadoCódigo
form.xhtml.
<html xmlns:h="http://java.sun.com/jsf/html">
<h:body>
<h:form>
<div>
<h:outputLabel>Titulo</h:outputLabel>
<h:inputText/>
</div>
<div>
<h:outputLabel>Descrição</h:outputLabel>
<h:inputTextarea cols="20" rows="10"/>
</div>
<div>
<h:outputLabel>Número de páginas</h:outputLabel>
<h:inputText/>
</div>
<div>
<h:outputLabel>Preço</h:outputLabel>
<h:inputText/>
</div>
<h:commandButton value=" Gravar"/>
</h:form>
</h:body>
</html>
Aqui,jáusamosalgumastagsdoJSFqueforamimportadaspormeiodo
namespace http://java.sun.com/jsf/html. Agora,casoomesmoendere çoseja
acessado,recebemosumarespostaestranha.
26

## Página 39

CasadoCódigo Capítulo2. Começandooprojeto
Fig.2.18:NavegadorinterpretouumXMLcomum
PercebaqueastagsqueusamosdoJSFnemforaminterpretadas.Como
pedimosporumendere çoqueterminacom xhtml,oWildflyentendeuque
realmenteestásendosolicitadoumsimplesdocumentoXML,enãoumapá-
ginaqueprecisaserprocessadaparaageraç ãodeHTML.
Vamosfazerumasimplesalteração. Emvezdeterminarcom xhtml,
vamosfazercomqueoendere çoterminecom .jsf. Eagora,comoum
passedemágica,foiexibidaapáginacorretamente.Aperguntaintriganteé:
como isso aconteceu?
Já está tudo configurado!
OWildflyjápossuiaimplementaçãodoJSF;nocaso,estásendousada
aMojarrasemnósprecisarmosfazernada,nemadicionarum web.xml.O
servletdoJSFjáfoiconfigurado.
Umoutrobomquestionamentoé: só porque estou dentro de um servidor
de aplicação, quer dizer que vou usar o JSF como framework MVC? Perceba
queessaseriaumasuposiç ãoumtantoquantopresun çosadosservidores.
Naverdade,meioquesemsaber,informamosaoservidorquenossoprojeto
gostariadehabilitaroJSF.
27

## Página 40

2.2. Acessandooprimeiroendereço CasadoCódigo
Lembradoarquivo faces-config.xml?Quandoumservidordeapli-
caçãooencontranapasta WEB-INF,automaticamenteassumequeaaplica-
çãoquerusarJSF,eoseu servletéconfigurado.
Voltando à extensão .jsf, ela é apenas uma das opções de
url-patterncriadasporpadrão.
•/faces –http://localhost:8080/casadocodigo/faces/produtos/form.
xhtml
•*.jsf–http://localhost:8080/casadocodigo/produtos/form.jsf
•*.faces–http://localhost:8080/casadocodigo/produtos/form.faces
Percebaquesempretemosdepassarocaminhoparaoarquivo,oque
mudasãoasmaneirascomopassamos.
Oengraçadoéque,pormaisqueessassejamasconven ções,nenhumade-
laséusadapelamaioriadasempresasnomercado.Émuitocomumencontrar
o servletdoJSFconfiguradoparao url-pattern *.xhtml.Paraficarmos
próximosdoquevocêvaiencontrarnoseupróximoemprego,vamosrealizar
essaalteração.
Primeiro,énecessárioqueoarquivo web.xmlsejagerado. Paraisso,
vamosutilizaropróprioEclipse. Cliquecomobotãodireitoemcimado
nomedoprojeto,eescolhaaop ção Properties.
Fig.2.19:Geradordeweb.xml
Noarquivogerado,adicioneanovaconfiguraçãodo Servlet.
<?xml version="1.0" encoding="UTF-8"?>
<web-app ...>
<display-name>casadocodigo</display-name>
28

## Página 41

CasadoCódigo Capítulo2. Começandooprojeto
<servlet>
<servlet-name>jsf</servlet-name>
<servlet-class>
javax.faces.webapp.FacesServlet
</servlet-class>
</servlet>
<servlet-mapping>
<servlet-name>jsf</servlet-name>
<url-pattern>*.xhtml</url-pattern>
</servlet-mapping>
</web-app>
Pronto,agoravocêpodeacessaroendere çopreviamentecombinado,que
tudofuncionaránormalmente.
2.3 U m pouco por dentro do framework
Umpontoquemuitasvezesdiferencia“usuários”doframeworkde“entende-
dores”éjustamenteteroconhecimentodoqueacontecepordentrodaferra-
menta.Porexemplo,comooJSFregistrao Servletdeleautomaticamente?
Foiexplicadoqueeleanalisaaexistênciadoarquivo faces-config,mas
ondeissoéfeito?Ondeestáocódigodecarregamentoda FacesServlet?
Essassãoperguntasque,pormaisquenãotenhamavercomoseucódigo
denegócioemsi,podemserimportantesparaentenderofluxodoframework.
O web.xml é desnecessário!
Desdeaversão3daespecificaç ão,nãoémaisnecessárioteroarquivo
web.xmlpararealizaraconfiguraçãode servletsefiltros.Umadasop ções
édeclararumarquivochamado web-fragmentdentrodapasta META-INF
eempacotarcomoum jar.Oprojetoqueadicionaressa libjávaiganhar
debrindeasconfiguraçõescontidasdentrodo fragment.
Outra opção usada pelo JSF é a de registrar umlistener
que é chamado quando o servidor acaba de subir. Dentro do
jar da implementação do JSF, existe um arquivo com o nome
29

## Página 42

2.3. Umpoucopordentrodoframework CasadoCódigo
javax.servlet.ServletContainerInitializer, localizado na
pasta META-INF/services. Quando o servidor sobe, ele analisa esse
arquivoecarregaqualquerclassequeestejaconfiguradadentrodele.Nocaso
doJSF,aclasseéa FacesInitializer.
Agoravamosdarumaolhada,apenasporcuriosidade,naimplementaç ão
dessaclasse.
public void onStartup(Set<Class<?>> classes,
ServletContext servletContext)
throws ServletException {
if (shouldCheckMappings(classes, servletContext)) {
InitFacesContext initFacesContext = new
InitFacesContext(servletContext);
if (null == initFacesContext) {
throw new
ServletException("Unable to initialize Mojarra");
}
Map<String,? extends ServletRegistration> existing =
servletContext.getServletRegistrations();
for (ServletRegistration registration :
existing.values()) {
if (FACES_SERVLET_CLASS.
equals(registration.getClassName())) {
// FacesServlet has already been defined,
// so we're not going to add
// additional mappings;
return;
}
}
ServletRegistration reg =
servletContext.addServlet("FacesServlet",
"javax.faces.webapp.FacesServlet");
reg.addMapping("/faces/*", "*.jsf" , "*.faces");
servletContext.setAttribute(RIConstants.
FACES_INITIALIZER_MAPPINGS_ADDED,
Boolean.TRUE);
30

## Página 43

CasadoCódigo Capítulo2. Começandooprojeto
...
}
}
private boolean shouldCheckMappings
(Set<Class<?>> classes, ServletContext context) {
if (classes != null && !classes.isEmpty()) {
return true;
}
try {
return
(context.getResource("/WEB-INF/faces-config.xml")
!= null);
} catch (MalformedURLException mue) {
}
return false;
}
Percebaqueométodo shouldCheckMappingsverificaaexistênciado
arquivo faces-config.xml.
Otrechoquesegueéoresponsávelpordecidirseo servletdeveser
registradoautomaticamente.
for (ServletRegistration registration : existing.values()) {
if (FACES_SERVLET_CLASS.
equals(registration.getClassName())) {
// FacesServlet has already been defined, so we're
// not going to add additional mappings;
return;
}
}
ServletRegistration reg =
servletContext.addServlet("FacesServlet",
31

## Página 44

2.4. Conclusão CasadoCódigo
"javax.faces.webapp.FacesServlet");
reg.addMapping("/faces/*", "*.jsf", "*.faces");
Eleprocuraporummapeamentodo servlete,casonãotenha,fazo
registroprogramático.Porsinal,percebaqueos url-patternscriadossão
justamenteosquecomentamosanteriormente.
Possível problema com os cookies
OJSFfazusodoescopode sessionparaimplementardetalhesinter-
nos,comomanteraárvoredecomponentes(vamosvoltaraelamaisà
frente).Casovocêtenhaoutrasaplicaçõesnoseucomputadorquetam-
bémfazemusodasessão,ébemprovávelquevocêacabecomváriosco-
okiesassociadosàchave jsessionidnoseunavegador.
Nessecenário,muitasvezesoJSFseperde,nãoconseguindoassociar
corretamentearequisiçãocomaárvoredecomponentes.Paranãopas-
sarporproblemasdesnecessários,minhasugestãoéquevocêlimpeos
cookiesassociadosao localhostnoseunavegador.
2.4 C onclusão
Estecapítulofoiumpoucolongoe,paraserbemsincero,atésimples.Opro-
blemaéquefoinecessáriamuitaexplicaçãoparaumsimples hello world.A
parteboadessahistóriaéquevocêpassouporumadasetapasmaisdifíceis
noaprendizadodequalquerprojeto:o setupinicial.
Agora,tudotendeasermaisfluido!Porisso,euindicoquevocêcontinue
aleitura.Nospróximoscapítulos,jácome çaremosaacessarobancodedados
paracadastrarelistarosprodutosdaloja.
32

## Página 45

Capítulo3
Cadastrodeprodutos
Passadaafasedeconfiguração,chegouahoradecome çarmosaimplementar
algumasdasfuncionalidadesdaloja. Umadas featuresmaisbásicas,porém
importante,éocadastrodelivros,jáquesemlivrosnãoexistemcompras.O
legaléquejácomeçamosumpoucodissonocapítuloanterior,entãovamos
apenasdarcontinuação.
3.1 F ormulário de cadastro
Vamosreaproveitaroformulárioqueusamoscomo hello worlddonossopro-
jetoparacome çaracriarateladecadastro.
<html xmlns:h="http://java.sun.com/jsf/html"
xmlns:jsf="http://xmlns.jcp.org/jsf">
<h:body>

## Página 46

3.1. Formuláriodecadastro CasadoCódigo
<h:form>
<div>
<h:outputLabel>Titulo</h:outputLabel>
<h:inputText/>
</div>
<div>
<h:outputLabel>Descrição</h:outputLabel>
<h:inputTextarea cols="20" rows="10"/>
</div>
<div>
<h:outputLabel>Número de páginas</h:outputLabel>
<h:inputText/>
</div>
<div>
<h:outputLabel>Preço</h:outputLabel>
<h:inputText/>
</div>
<h:commandButton value=" Gravar"/>
</h:form>
</h:body>
</html>
Nãotemnadademais,apenasumHTMLnormalcomalgumastagsdo
JSF.Sóparaconstar,nossomodelodelivronãoprecisasermuitocomplexo.
Eleteráapenasumtítulo,descrição,númerototaldepáginasepre ço,pelo
menosporenquanto.
Umdetalheimportantequeficoufaltando: paraondevamosenviaras
informaçõescadastradas? Aindanãocriamosnadaquetrateessalógica.
ComooJSFtentatrazerparaomundowebumaprogramaç ãoparecidacom
omundodesktop,temosdeadicionarummétodoquedeveserchamadoapós
oformuláriosersubmetido.
Paracomeçarmosaimplementaçãodessalógica,vamosalteraronosso
commandButtonparaqueelereferencieométodoquedeveserinvocado.
.
.
.
<h:commandButton value="Gravar" action="#{adminBooksBean.save}"/>
34

## Página 47

CasadoCódigo Capítulo3. Cadastrodeprodutos
3.2 L ógica de cadastro
Agora, se você tentar cadastrar um novo livro, vai receber a seguinte
exception:
javax.servlet.ServletException:
javax.el.PropertyNotFoundException:
/produtos/form.xhtml @17,69 action="#{adminBooksBean.save}":
Target Unreachable, identifier 'adminBooksBean' resolved to null
Elaindicaquea expression languagenãoconseguiuresolverareferência
paraavariável adminBooksBean. Essaserájustamenteaprimeiraclasse
quevamoscriar,paraquepossamoscome çaraimplementarocadastrono
nossosistema.
package br.com.casadocodigo.loja.managedbeans;
...
@Model
public class AdminBooksBean {
public void save(){
System.out.println("Precisamos salvar o livro!!");
}
}
Agora,quandoapertamosobotão,amensagemjáéimpressanoconsole
donossoservidor.Umpontoimportanteaquiéousoda annotation @Model.
ElaéumaannotationdoCDIqueindicaqueosobjetosdaclasseporelaano-
tadasempreserãocriadosnoescopode request,eficarãodisponíveispara
seremacessadospela Expression Language.
Porpadrão,onomedavariávelcujoobjetoficaráacessíveléomesmo
nomedaclasse,comaprimeiraletraemminúsculo. Esseéumcasobem
comumparaumaaplicaçãoweb,naqual,emgeral,queremoscriarnovos
objetosapartirdecadarequisição.
Voltandoparanossafuncionalidade,precisamospelomenosimprimiras
informaçõesdecadastroqueforampreenchidaspelousuário.Parafazerisso,
énecessárioassociarcadaumdoscamposdonossoformulárioaumapro-
priedade.
35

## Página 48

3.2. Lógicadecadastro CasadoCódigo
<h:form>
<div>
<h:outputLabel>Titulo</h:outputLabel>
<h:inputText value="#{adminBooksBean.product.title}" />
</div>
<div>
<h:outputLabel>Descrição</h:outputLabel>
<h:inputTextarea cols="20" rows="10"
value="#{adminBooksBean.product.description}" />
</div>
<div>
<h:outputLabel>Número de páginas</h:outputLabel>
<h:inputText
value="#{adminBooksBean.product.numberOfPages}" />
</div>
<div>
<h:outputLabel>Preço</h:outputLabel>
<h:inputText value="#{adminBooksBean.product.price}" />
</div>
<h:commandButton value="Gravar"
action="#{adminBooksBean.save}" />
</h:form>
Analise,porexemplo,apropriedade valuedo inputreferenteaotítulo
dolivro.Estamosdizendoqueaclasse AdminBooksBeanpossuiummétodo
chamado getProduct,equeesteretornaumobjetoquepossuium getter
eum setterparaapropriedade title. Dessaforma,oJSFconseguenave-
garpelaspropriedadesdos beans,tambémconhecidosnomercadocomo
Managed Beans,epopularosreferidoscampos.
Agora,parafazeressecódigofuncionar,precisamosimplementaraspar-
tesquefaltamnonossocódigo.Inicialmente,vamoscriaraclassequerepre-
sentaonossolivro.
package br.com.casadocodigo.loja.models;
//imports
36

## Página 49

CasadoCódigo Capítulo3. Cadastrodeprodutos
public class Book {
private Integer id;
private String title;
private String description;
private int numberOfPages;
private BigDecimal price;
//getters e setters
//adicione um toString interessante.
}
Agora, precisamos realizar as alterações necessárias na classe
AdminBooksBean.
public class AdminBooksBean {
private Book product = new Book();
public void save(){
System.out.println(product);
}
public Book getProduct() {
return product ;
}
}
Casovocêrealizeumnovotestenaaplicação,deveráverasinformações
queforampassadaspelousuário.
Reflexão sobre como a requisição é feita
Esseéumbommomentoparapensarmosumpoucoemcomoascoisas
acontecemdentrodeumaaplicaçãoJSF.Nawebtradicional,somosacostu-
madosadarnomesparaos inputs,epegarosvaloresassociadosaestesnomes
37

## Página 50

3.3. Gravandoosdadosnobancodedados CasadoCódigo
doladodoservidor.Sóquepareeolheparaonossoformulário:ondeestão
osnomes?Todaaassociaçãoérealizadapormeiodoatributo value,dispo-
nívelnastagsdopróprioJSF.
QuandoutilizamosoJSF,paracadatelacarregada,éconstruídaumaár-
voredecomponentesrepresentandocadaumdoselementosqueescrevemos
napágina.Tantoéque,sevocêolharocódigo-fontequeaparecenoseuna-
vegador,encontraráalgoassim:
<input type="hidden" name="javax.faces.ViewState"
id="j_id1:javax.faces.ViewState:0"
value=
autocomplete="off" />
Esseéo idquefoidadoparaaárvorecriada.Agora,todasasvezesem
querealizarmosum postpormeiodonossoformulário,o idserámantido,
pelomenosenquantonãofizermosnenhum redirect.
Experimenteacessarnovamenteoendere çodoformulárioemvezdesub-
meterosdadosdo form.Vocêveráqueo idvaimudar.Parairmantendo
oestadodosvaloresdosinputsdoladodoservidor,oJSFguardaaárvorena
sessãodousuário.
Agora,vocêpodeseperguntar: para que serve esse id, já que ele mantém
o estado da árvore na sessão?Esseéumótimoquestionamento!Oproblema
éque,sevocêabrirváriasabasnoseunavegadore,comoasessãocontinu-
arásendoamesma,oframeworkvaiprecisardistinguirsobrequalárvoreo
requestestáfalando.
Éporcontadessemecanismoqueosvaloresquevocêpreencheunofor-
muláriopararealizarostestescontinuaramnosinputs,mesmodepoisdevocê
terfeitoarequisição.Emumaaplicaçãowebnormal,essesvaloresteriamde-
saparecido. Étambémporcontadissoquevocênãoprecisacolocarnomes
nosinputs,nemactionsnosformulários,tudoéassociadonomomentoem
queeleconstróiaárvoredecomponentes.
3.3 G rav ando os dados no banco de dados
Pormaisquenossoformuláriojáestejaumtantoquantofuncional,aindanão
estamosefetivamentegravandoasinformaçõespassadas.Paramelhoraressa
38

## Página 51

CasadoCódigo Capítulo3. Cadastrodeprodutos
parte,vamoscome çaraefetuarasalteraçõesnecessáriasapartirdonosso
controller.
Aprimeiracoisaécome çarausarumDAO(Data Access Object )respon-
sávelpeloacessoaosdadosreferenteàclasse Book.
Lembrete sobre o DAO
ODataAccessObjectéapenasumaclassecujoobjetivoéisolaro
acessoaosdadosdeumdeterminadapartedosistema.Nonossoexem-
plo,vamosprecisargravar,listarecarregarumlivro.Nãoqueremosmis-
turaressapartedeacessoàinfraestruturacomnossaslógicas.
Ocódigodométodo savedeveficarparecidocomoquesegue:
public void save(){
bookDAO.save(product);
}
Edeondevemessainstânciadaclasse BookDAO?Umadasop çõeséque
nósmesmoscriemosesseobjetonamão.
@Model
public class AdminBooksBean {
private Book product = new Book();
private BookDAO bookDAO = new BookDAO();
public void save(){
bookDAO.save(product);
}
}
Oproblemaéque,provavelmente,oconstrutordo BookDAOvaiprecisar
receberalgumobjetoquerepresenteaconexãocomobancodedadose,nesse
caso,vamosterdecome çaracontrolaressasdependênciasnamão. Essaé
umaótimaparteparausarmosmaisdoCDInonossoprojeto.
39

## Página 52

3.3. Gravandoosdadosnobancodedados CasadoCódigo
ComoanossaclassejáégerenciadapeloCDI,podemospedirparaqueele
instancieumnovoobjetodotipo BookDAOparanós.Onossoúnicotrabalho
éindicarqueprecisamosreceberessainstância injetada.
@Model
public class AdminBooksBean {
private Book product = new Book();
@Inject
private BookDAO bookDAO;
public void save(){
bookDAO.save(product);
}
public Book getProduct() {
return product;
}
}
Aannotation @Injectéjustamentearesponsávelporindicarospontos
deinje çãodentrodasuaclasse. Esseéumbommomentoparalembrá-lo
deque,emumprojetousandoCDI,aúnicaconfiguraç ãonecessáriapara
habilitaroscandeclasseséacriaçãodoarquivo beans.xml,dentrodapasta
WEB-INF.
Para que serve um arquivo em branco?
Éumótimoquestionamento,maslembre:oarquivoestáláparahabi-
litarseuprojetoparaserscaneadopeloWeld,queéaimplementaç ãodo
CDIusadadentrodoWildFly.Casonãofossenecessáriocriá-lo,oWeld
teriadeirolhandodentrodecadaclassedecada jardoseuprojeto
paradescobrirquaisclassesgostariamdesergerenciadasounão.Dessa
forma,eleprimeirobuscapelaexistênciadoarquivoe,apenasemcaso
positivo,dáprosseguimentopelabuscaporclasses.
40

## Página 53

CasadoCódigo Capítulo3. Cadastrodeprodutos
Nesseexatomomento,nossocódigonãocompila,jáquenãocriamos
aindaaclasse BookDAO,assimcomonãoexisteométodo save. Chegou
ahoraderesolvermosessapartedonossocódigo.
package br.com.casadocodigo.loja.daos;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import br.com.casadocodigo.loja.models.Book;
public class BookDAO {
@PersistenceContext
private EntityManager manager;
public void save( Book product) {
manager.persist(product);
}
}
AquiestamosusandoaJPApararealizarapartedeacessoefetivoaonosso
bancodedados.Napróximase ção,trataremossobrecomoconfigurá-la.
Voltandoaonosso BookDAO,percebaqueelaéumaclassebemnormal.
Nãofoinecessárianenhumaconfiguraçãoextra,eessaéumadasbelezasdo
CDI.
Até podemos usar annotations, como foi o caso na classe
AdminBooksBean, mas váriasvezes nãoprecisamos adicionarnenhuma
delas.Nestecasoespecífico,vocêpodeestarseperguntando: qual é o escopo
da criação desse objeto?
Quandonãocolocamosnenhumaanotaçãoemcimadaclasse,estamos
dizendoque,naverdade,quemdecideoescopodoobjetoéolocalondeele
vaiserinjetado.Observeoexemplo:
@Model
public class AdminBooksBean {
41

## Página 54

3.4. ConfigurandoaJPA CasadoCódigo
...
@Inject
private BookDAO bookDAO = new BookDAO();
...
}
Comojávimos,aannotation @Modelindicaqueosobjetosdaclasseano-
tadadevemviverpelotempodeumarequisiç ãowebe,alémdisso,também
devemficarexpostosna expression language. Comoaclasse BookDAOnão
definiuoescopoexplicitamente,otempodevidadoseuobjeto,nessecaso,
vaiserodaduraçãodeum request,jáqueaclassequesolicitousuainje ção
definiuesteescopo.
Casotivéssemospedidoessainje çãoemumaclassedeescopo session,o
objetodotipo BookDAOteriaassumidoomesmo.Essaestratégiadentrodo
CDIéchamadadeescopo @Dependent.Nãoadicionarnenhumaanotação
detempodevidaéomesmoquefazeroseguinte:
@Dependent
public class BookDAO {
...
}
Váriasvezes,emumaaplicaçãoweb,o @Dependentvaiseroperfeito
paravocê. Comoquasetudocomeçaapartirdoseu Managed Bean,queé
criadoumavezporrequisição,todososoutrosobjetosautomaticamentevão
seguiromesmotempodevida.
3.4 C onfigurando a JP A
Estamosquaseconseguindogravaroproduto,sófaltaagoraconfigurarmos
aJPA(Java Persistence API )paraquenossoacessoaobancodedadosfique
completo.Parafazerisso,precisamosseguiralgunspassos.
42

## Página 55

CasadoCódigo Capítulo3. Cadastrodeprodutos
Mapeando a entidade
Chegouahoradefazermosasconfiguraçõesnecessáriasparaqueosob-
jetosdaclasse Bookpossamsersalvos. Umpassoimportanteéensinara
implementaçãodaJPA–emnossocaso,oHibernate–queaclasse Bookvai
representarumatabelanobancodedados.
import javax.persistence.Entity;
...
@Entity
public class Book {
@Id @GeneratedValue(strategy=GenerationType.IDENTITY)
private Integer id;
private String title;
private String description;
private int numberOfPages;
private BigDecimal price;
...
}
AquiusamosalgumasannotationsespecíficasdaJPApararealizaresses
ensinamentos:
•@Entity–indicaqueaclassevaivirarumatabela;
•@Id–indicaqueoatributoemquestãoéachave-primária;
•@GeneratedValue–indicaamaneiracomovaisergeradaachave-
primária;
•@Lob–indicaqueoatributoemquestãovaisersalvocomo Clobou
Blobnobancodedados.
Nãoachoquevaleapenaentrarmosemtodososmapeamentospossíveis
daJPA.Onossofocoduranteolivroéconstruirumaaplicaç ãowebtirando
proveitodetodasasespecificaçõesquenossejamúteis.Nessecontexto,aJPA
éapenasmaisumadelas.
43

## Página 56

3.4. ConfigurandoaJPA CasadoCódigo
@PersistenceContext e o Persistence.xml
Uma annotation que passou batida no nosso debate anterior foi a
@PersistenceContext. Elaéutilizadaparaindicar,dentrodeum con-
tainerJavaEE,anecessidadedeinje çãodeum EntityManagerqueseja
controladoecriadopelopróprioservidor. Olegaldessaannotationéque
suasemânticaémuitoforte,então,váriasoutrastecnologias,comooSpring,
fazemseuusoparaindicarainje çãodeum EntityManager.
Um outro ponto importante são as informações de acesso ao banco
de dados. A especificação JPA indica que devemos utilizar um ar-
quivo chamado persistence.xml, e que nele devem estar contidas
nossas informações de acesso ao banco de dados. Este arquivo deve
ser criado na pastaMETA-INF, dentro dobuild path do seu projeto.
Em projetos que usam Maven, como é o nosso caso, o caminho será
src/main/resources/META-INF/persistence.xml.
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<persistence xmlns="http://xmlns.jcp.org/xml/ns/persistence"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
version="2.1"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/persistence
http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
<persistence-unit name="casadocodigo-dev"
transaction-type="JTA">
<description>Dev persistence unit</description>
<provider>
org.hibernate.ejb.HibernatePersistence
</provider>
<jta-data-source>
java:jboss/datasources/casadocodigoDS
</jta-data-source>
<properties>
<property name="hibernate.hbm2ddl.auto"
value="update"/>
<property name="hibernate.show_sql"
value="true" />
<property name="hibernate.format_sql"
44

## Página 57

CasadoCódigo Capítulo3. Cadastrodeprodutos
value="true" />
<property name="hibernate.dialect"
value="org.hibernate.dialect
.MySQL5InnoDBDialect"/>
</properties>
</persistence-unit>
</persistence>
Perceba que fizemos algumas configurações específicas do Hibernate,
comoapropriedade hibernate.hbm2ddl.auto. Elaéusadaparaque
nãoprecisemosficarcriandotabelasnovasnobancotodasasvezesemque
mapeamosumanovaentidade.
Umaoutrataginteressanteéa <provider>,necessáriaparainformar
qualimplementaçãodaJPAseráutilizadanoprojeto.Nonossocaso,como
estamosdentrodoWildFly,seráusadooHibernate.
Umpontoquevocêpodeestarseperguntandoéondeestãoasconfigu-
raçõesdeacessoaobancodedadosemsi.Semprequevamosnosconectar,
somosobrigadosainformarcoisascomo:
• URLdeacessoaobanco;
• Login;
• Senha;
• Drivernecessário.
Evocêestácobertoderazão,issotudoénecessário.Aúnicadiferen çaé
quevamostirarproveitodetodaainfraestruturaprovidapelonossoservidor
deaplicação.Emvezderealizarmosessasconfiguraçõesedeixarmosacargo
doHibernategerenciarasnossasconexões,vamospedirparaqueoWildFly
crieegerencie-as.Dessaforma,aúnicatarefadoHibernateseráadepedir
umanovaconexãosemprequenecessário.
Esseéjustamenteoobjetivodaseguintelinhadeconfiguraç ão:
<jta-data-source>
java:jboss/datasources/casadocodigoDS
</jta-data-source>
45

## Página 58

3.5. ConfiguraçãodoDataSourcenoWildlFly CasadoCódigo
Simplesmente passamos um nome que está associado a um
DataSource, que será configurado dentro do próprio servidor. Se-
gureumpoucoacuriosidadeagora,napróximase çãodiscutiremosmais
sobreessenome. Aindaprecisamospararepensarsobreasigla JTA(Java
Transaction API),queapareceunonomedessatagetambémnapropriedade
transaction-type.Tudoissoserádesvendadoaindanestecapítulo.
3.5 C onfiguração do DataS ource no WildlFly
Precisamos completar nossa configuração de acesso ao banco de dados,
e o ponto que ficou faltando foi justamente a configuração relativa do
DataSource. Aqui,valeapenaressaltarqueessaconfiguraç ãovaivariar
entreosservidoresdeaplicaçãoquevocêdecidirusar.
Arquivo de configuração do WildlFly
O arquivo responsável pelas configurações do nosso WildFly,
nesse momento, é o standalone-full.xml. Ele fica na pasta
caminhoInstalacaoWildfly/standalone/configuration/
standalone-full.xml.
Onome standalonevemdofatodeestarmosrodandoapenasumains-
tânciadoservidor.Eletambémsuportaumaoutramaneiradeexecuç ão,na
qualsubimosváriasinstânciasdoservidorefazemoscomqueelassecom-
portemcomosefossemapenasuma,modoconhecidocomo Cluster Mode.
Casovocêestejacuriosoetenhanavegadoatéapasta configuration,
veráqueládentroexistemoutrosarquivosdeconfigurações.Estaéumadas
grandesvantagensdoWildFly: suamodularização. Podemosdefinirquais
módulossãonecessáriosparaanossaaplicaç ão. Porexemplo,nocasodo
standalone-full.xml,recebemosprontotudodequenormalmentepo-
demosprecisar.
• JPA;
• E-mail;
• JSF;
46

## Página 59

CasadoCódigo Capítulo3. Cadastrodeprodutos
• Transações(JTA);
• Weld(CDI);
• Servlets;
• WebServices;
• EJB.
Percebaquejásãováriasop ções.Háalgunsitensdessalistaquejáestu-
damos,algunsquevocêjádevesaber–comoapartedeServlets–,eainda
outrosquevamostrabalharduranteolivro. Alémdestes,aindavamosusar
umaoutraespecificação,queéademensageria,masissoéassuntoparaser
vistomaisparaafrente.
Paraexemplificarmelhor,analiseotrechodoarquivoquecontémessas
configurações:
<extensions>
<extension module="org.jboss.as.clustering.infinispan"/>
<extension module="org.jboss.as.connector"/>
<extension module="org.jboss.as.deployment-scanner"/>
<extension module="org.jboss.as.ee"/>
<extension module="org.jboss.as.ejb3"/>
<extension module="org.jboss.as.jaxrs"/>
<extension module="org.jboss.as.jdr"/>
<extension module="org.jboss.as.jmx"/>
<extension module="org.jboss.as.jpa"/>
<extension module="org.jboss.as.jsf"/>
...
</extensions>
Voltandoaonossotrabalhodeconfiguraç ãodo DataSource,éjusta-
mentedoarquivo standalone-full.xmlquevamosprecisaralterarpara
realizarumapartedessetrabalho.
47

## Página 60

3.5. ConfiguraçãodoDataSourcenoWildlFly CasadoCódigo
Adicionando mais um DataSource
Casovocêcontinueolhandooarquivo,veráqueexisteumatagchamada
datasources,queéjustamenteolocalonderesidemasconfiguraçõeses-
pecíficasdeacessoaobancodedados.Apenasporcuriosidade,essatagestá
dentrodeumaoutrachamada subsystem. Cada subsystemcontémas
configuraçõesrelativasàsextensõesmapeadasnoiníciodoarquivo.
Percebaque,dentrodatag datasources,jáexisteaconfiguraçãode
um DataSource,justamenteoquejávemprontodentrodoWildFly.Infe-
lizmente,essaconfiguraçãousaoH2comobancodedados,oqueénãotão
comumnomercado.Eleémaisutilizadoparafinsdetestes.
Pensandonisso,vamosconfigurarumoutro DataSourceparaquepos-
samosusaroMySQL.
<datasources>
<datasource>
...
</datasource>
<datasource
jndi-name="java:jboss/datasources/casadocodigoDS"
pool-name="casadocodigoDS">
<connection-url>
jdbc:mysql://localhost:3306/casadocodigo
</connection-url>
<driver>mysql</driver>
<security>
<user-name>root</user-name>
<!-- Caso precise de senha-->
<password> sua-senha</password>
</security>
</datasource>
</datasources>
Percebaqueaconfiguraçãoéquaseautoexplicativa. Algumasinforma-
çõessãoexatamenteasmesmascomquejáestamosacostumados.Veja:
•<connection-url>–URLdeconexãoparasuabasededados;
48

## Página 61

CasadoCódigo Capítulo3. Cadastrodeprodutos
•<security>–contémasinformaçõesdeloginesenhaparaobanco;
Entretanto,existemalgumastagseatributosquemerecemumpoucomais
deatenção.Omaissimpleséoatributo pool-name.Elerepresentaonome
do pool de conexões queserácriadoparaarmazenartodasasconexõesque
foremcriadaspelonosso datasource. Casovocêqueiraespecificarmais
informaçõessobreesse pool,podeusaratag <pool>. Vejaumexemploa
seguir,aconfiguraçãonãoéobrigatória.
<datasource jndi-name="java:jboss/datasources/casadocodigoDS"
pool-name= "casadocodigoDS">
<connection-url>jdbc:mysql://localhost:3306/casadocodigo
</connection-url>
<driver>mysql</driver>
<security>
<user-name> root</user-name>
</security>
<pool>
<min-pool-size>10</min-pool-size>
<max-pool-size>20</max-pool-size>
</pool>
</datasource>
Outroatributo,aindanaprópriatag datasource,éo jndi-name.
Nele,passamosonomequedeveserreferenciadopelaaplicaç ão,paraqueela
possarecuperarareferênciaparaoobjetoquerepresentao datasource.
AJNDIéumaoutraespecificaçãodomundoJavaqueémuitoutilizada.
Quasetodososobjetosquesãocriadospeloprópriocontainerficamdispo-
níveisparaseremacessadosviaalgumnomequepodeserregistrado.Quem
faztodootrabalhoparabuscaroobjetoporessenomeéaimplementaç ãoda
especificaçãoJNDI(Java Naming and Directory Interface).
AindaemrelaçãoàJNDI,éimportanteprestaraten çãonoiníciodaString
dedefiniçãodovalor,come çandocom java:jboss/.Essecome çoéoque
informaoníveldedisponibilidadedosobjetoscriadosdentrodocontainer,e
éoquechamamosde namespacedaJNDI.
NocasodoWildFly,paraexporobjetosquedevemserrecuperadosre-
motamente,podemostrabalharcomosseguintesnamespaces:
49

## Página 62

3.5. ConfiguraçãodoDataSourcenoWildlFly CasadoCódigo
•java:jboss/
•java:/
Alémdosatributosquediscutimos–queestãopresentesnaprópriatag
datasource–,existemaisumdetalhebemrelevante:atag driver.Per-
cebaqueapenascolocamosonome mysql. Mascomoocontainervaisa-
berqualclassedeveserusadaparaconectarnestebanco? Domesmojeito
queusamosbancoMySQL,poderíamosterusadooPostgreSQL.Casovocê
prestebastanteaten ção,veráqueomesmoocorrenadefiniç ãododriverdo
datasourceanterior,comoH2.
<datasource jndi-name="java:jboss/datasources/ExampleDS"
pool-name="ExampleDS" enabled="true"
use-java-context="true">
<connection-url>...</connection-url>
<driver>h2</driver>
...
</datasource>
Eletambémdefineapenasumnomedodriver.
Agora,vemumoutromomentoimportante. Percebaque,logoabaixo
dastags datasource,existeadeclaraçãodeumatagchamada drivers.É
justamentenelaqueumapartedestemisteriosonomecome çaaserresolvida.
<drivers>
<driver name="h2" module="com.h2database.h2">
<xa-datasource-class>org.h2.jdbcx.JdbcDataSource
</xa-datasource-class>
</driver>
</drivers>
Onomeinformadonaconfiguraçãodo datasourceéapenasumachave
paraoWildFlypoderencontrarasconfiguraçõesdefinidasnatag driver.
Porexemplo,paraonossoexemplocom mysql,podemosadicionaroutra
tag.
<drivers>
<driver name="h2" module="com.h2database.h2">
50

## Página 63

CasadoCódigo Capítulo3. Cadastrodeprodutos
<xa-datasource-class>org.h2.jdbcx.JdbcDataSource
</xa-datasource-class>
</driver>
<driver name="mysql" module="com.mysql">
<datasource-class>
com.mysql.jdbc.Driver
</datasource-class>
</driver>
</drivers>
Agora,voupedirumfavor,nãofiquechateado.Aindaprecisamosrealizar
maisumpassoparafinalmenteconfigurarnosso datasource. Comtudo
issopronto,faltaapenasmaisumdetalhe:informarondeestáo jarcomas
classesdodriverdoMySQL.EaquioWildFlytomamaisumadecisão.
Váriasvezes,asempresasqueremdefinirumaversãopadrãodecertas
bibliotecas,porexemplo,osdriversdeacessoaobancodedados. Paraeste
tipodecaso,emalgunsservidores,vocêsimplesmenteadicionaesses jars
emumapastacompartilhada.Porexemplo,noTomCat,issoficarianapasta
libdoservidor.
Esealgumaaplicaçãoprecisardaversãoatualizadadodriver,comoela
faráagora?Umaatualizaçãopodeimpactaremváriasoutrasaplicações.
Parapermitirocompartilhamentode jarsentreaplicações,mastambém
comopensamentodepossibilitaraevoluç ãodasversões,oWildFlyusou
umesquemademodularização.Adicionamosos jarsnecessáriosdentroda
pasta modules,queficadentrodapastadeinstalaç ãodoservidor.
51

## Página 64

3.5. ConfiguraçãodoDataSourcenoWildlFly CasadoCódigo
Fig.3.1:EstruturademódulosdoWildFly
Percebaqueo com.h2database.h2coincidentementeéocaminhoaté
apasta main,ondeexistemo jareumarquivodeconfiguraçãoreferente
aobancoH2.Vamosdarumaolhadanessearquivo.
<module xmlns="urn:jboss:module:1.3" name="com.h2database.h2">
<resources>
<resource-root path="h2-1.3.173.jar"/>
</resources>
<dependencies>
<module name= "javax.api"/>
<module name= "javax.transaction.api"/>
<module name= "javax.servlet.api" optional="true"/>
</dependencies>
</module>
Nãoprecisamosficardebatendosobreseuconteúdo.Apartemaisimpor-
52

## Página 65

CasadoCódigo Capítulo3. Cadastrodeprodutos
tanteparanóséoatributo nameeatag resources.
•name–valoraserreferenciadoporalgumaconfiguraçãoexterna,como
odriver.
•resources–informaalocalizaçãodos jarsnecessáriosparaqueo
módulosejacarregado.
PrecisamoscriaralgoparecidoparaaconfiguraçãododriverdoMySQL.
Então,dentrodapasta modules/system/layers/base/com,criease-
guinteestruturadepastas: mysql/main. Dentrodapasta main,crieo
arquivochamado module.xmlcomoseguinteconteúdo:
<?xml version="1.0" encoding="UTF-8"?>
<module xmlns="urn:jboss:module:1.3" name="com.mysql">
<resources>
<resource-root path="mysql-connector-java-5.1.35.jar"/>
</resources>
<dependencies>
<module name="javax.api"/>
</dependencies>
</module>
Para fechar, só precisamos do driver. Você pode baixá-lo em
http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.35/
mysql-connector-java-5.1.35.jar.
Pronto! Agoracomtudoconfigurado,vocêjápodeiniciaroWildFlye
tentarcadastrarumnovolivro.
Alterando o arquivo de configuração pelo Eclipse
OarquivodeconfiguraçãodoseuWildFlypodeseralteradodiretamente
pormeiodanavegaçãonosistemadearquivos,comofoimostradoduranteo
capítulo,assimcomopordentrodoseuEclipse.
Parafazerdasegundaforma,queesteautorachamaissimples,bastaabrir
aaba Serversenavegardiretamenteatéoarquivo.
53

## Página 66

3.6. Anecessidadedeumatransação CasadoCódigo
Fig.3.2:Alterandoostandalone.xmlpeloEclipse
Vocêpodefazertodasasalteraçõesnecessáriasapartirdeagora,pormeio
daprópriaIDE.Duranteocapítulo,essaformanãofoimostradadiretamente
justamenteparatermossempreemmentequeéimportanteentendercomo
ascoisasfuncionam,paranãoficarmospresosàIDE.
3.6 A necessidade de uma transação
Quandotentamosgravarumnovolivro,nessemomento,recebemosase-
guinteexception:
javax.servlet.ServletException:
javax.persistence.TransactionRequiredException: JBAS011469:
Transaction is required to perform this operation
(either use a transaction or extended persistence context)
Aexceptionéatébemclara,falaqueprecisamosdeumatransaç ãopara
conseguirmossalvarumobjeto. Paraanossasorte,lidarcomtransaçõesjá
ésuportadopelaprópriaespecificaçãoJavaEE.Assim,nossoúnicotrabalho
seráfazerumasimplesconfiguração.
...
import javax.transaction.Transactional;
@Model
public class AdminBooksBean {
54

## Página 67

CasadoCódigo Capítulo3. Cadastrodeprodutos
private Book product = new Book();
@Inject
private BookDAO bookDAO;
@Transactional
public void save(){
bookDAO.save(product);
}
public Book getProduct() {
return product ;
}
}
Aannotation @TransactionalfoiintroduzidaapartirdoJavaEE7,
epermitemarcarquemétodosgerenciadospeloCDIrodemdentrodeum
contextotransacional. Alémdisso,noiníciodocapítulo,tambémfizemos
umaleveconfiguraçãonoarquivo persistence.xml.
<persistence-unit name="casadocodigo-persistence-unit"
transaction-type="JTA">
<jta-data-source>
java:jboss/datasources/casadocodigoDS
</jta-data-source>
</persistence>
IndicamosquequemvaicuidardasnossastransaçõeséaJTA,justamente
aespecificaçãoquecuidadapartedetransaçõesnoJavaEE.Tambémépor
contadessaespecificaçãoqueusamosatag <jta-data-source>,parain-
formarquenosso DataSourcedevesercriadodemodoqueastransações
sejamgerenciadaspelaJTA.
Apenasporcuriosidade,quandorodamosnossaaplicaç ãoemumser-
vidordeaplicação,ovalordoatributo transaction-typejáé JTApor
padrão.QuandorodamosumaaplicaçãoqueusaaJPAdentrodeoutroam-
biente,ovalordefaulté RESOURCE_LOCAL,queinformaqueoresponsável
porcuidardastransaçõeséopróprio EntityManager.
Agora,finalmente,somoscapazesdegravarosnossoslivros!
55

## Página 68

3.7. Conclusão CasadoCódigo
Opinião do autor sobre a JTA
AJavaTransactionAPIéumaespecificaçãoquevaibemalémdoquecui-
dardesimplestransaçõesdebancodedados.Suasimplementaçõessuportam
queváriasoperaçõessejamenvolvidasnamesmatransação,porexemplo:
• Comunicaçãocombancodedados;
• Comunicaçãocomservidoresdemensageria;
• Comunicaçãocommúltiplosbancosdedadosnamesmatransaç ão.
A possibilidade de termos todas essas operações envolvidas em uma
mesmatransação,pormaisqueexista,ébaixa.Geralmente,estetipodece-
náriopodeserencontradoemalgunsbancosoubolsasdevalores.Algumas
vezes,chegaaficaratémaiscomplexo,comsistemasrodandoemmáquinas
diferentestendodeparticipardamesmatransaç ão.
Quandoprecisamosenvolvermúltiplosserviçosnamesmatransação,tra-
balhamoscomoconceitodetransaç ãodistribuída,quejáésuportadopela
própriaJTA.Driversdebancodedados,porexemplo,suportamoconceito
pormeiodaimplementaçãodainterface XAConnection.
Ditoisso,esteautornãoachaválidogastarmosmuitotempodiscutindo
todasessaspossibilidadesdaJTA,jáquequasenãotemoscontextodeusopara
taiscenários.AindavamosvoltaràJTAquandofomosdiscutirmensageria,
controlemaisfinosobreatransaçãocorrenteetc.,quetendemasercasosmais
práticoserelevantesnamaiorpartedasuavidacomodesenvolvedor.
3.7 C onclusão
Nestecapítulo,passamospormuitacoisa.Foinecessáriamuitaconfiguraç ão
paraquenossoacessoaobancodedadosfossepossível.Sóqueosaldopo-
sitivodetodoessetrabalhoéqueaprendemosmaissobreoWildFlyesuas
configurações.
Porsinal,aconfiguraçãoespecíficadoservidoraindaéo“calcanharde
Aquiles”daespecificaçãoJavaEE.Játemosmuitosdetalhesquefuncionam
56

## Página 69

CasadoCódigo Capítulo3. Cadastrodeprodutos
noautomático,mascomomuitasespecificaçõestêmrelaçãocomdetalhesde
infraestrutura,somosobrigadosarealizaressesajustes.
Aparteboadissotudoéqueconseguimosgravarnossoslivrosnobanco
dedadose,olhandoapenasparaocódigo,atéquenãotivemosnadacom-
plexo. Apartepotencialmentemaiscomplicadadestemomento,queerao
controletransacional,funcionouapenascomousodeumaanotaç ão.Eessa
éapartequemaisevoluiunaespecificaç ão,escrevercódigoJavaemsitem
ficadomuitofácil.
Nopróximocapítulo,vamosevoluironossocadastro,associandoauto-
rescomoslivroscadastrados,elistandoeadicionandomensagensdeconfir-
mação. Minhasugestãoéquevocênãopareainda. Venhacomigoevamos
completaressafuncionalidade.
57

## Página 71

Capítulo4
Melhorandoocadastroeum
poucomaisdeJSF
Nossocadastrodelivrosjácome çouafuncionar,sóqueestáfaltandoumaca-
raterísticabemimportante:osautoresdoslivros.NositedaCasadoCódigo,
oslivrospodemserescritostantoporumapessoacomoporvárias.
Um caso bom para mostrar essa possibilidade é a página do li-
vro Coletânea Front-end (http://www.casadocodigo.com.br/products/
livro-coletanea-front-end).Elefoiescritopordiversaspessoas,eonomede
cadauméexibidodentrodosite.

## Página 72

4.1. Associandováriosautores CasadoCódigo
Fig.4.1:Imagemilustrandoosnomesdosautores
Vamoscomeçaratrabalharnanossaaplicaçãoparatermosamesmapos-
sibilidade.
4.1 A ssociando v ários autores
Nossaprimeiratarefavaiserprepararanossateladecadastroparaqueousuá-
rioqueadministraalojapossaassociarosautores.Paraisso,vamosalteraro
arquivo livros/form.xhtml.
...
<div>
<h:outputLabel>Autores</h:outputLabel>
<h:selectManyListbox
value="#{adminBooksBean.selectedAuthorsIds}">
<f:selectItems value="#{adminBooksBean.authors}"
var="author"
itemLabel="#{author.name}" itemValue="#{author.id}"/>
</h:selectManyListbox>
</div>
Aquifoinecessáriousarastags selectManyListboxe selectItems,
paraquepossamosconstruirumatag selectdoHTMLcomapossibilidade
deescolhadeváriositens.Mesmoqueestejamosusandoapenasalgumastags
doJSF,játemostrabalhoaserfeito.Porexemplo,deondevemalistagemde
60

## Página 73

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
autoresqueprecisamosexibirnatela? Quallistavaiserpreenchidacomas
informaçõesselecionadaspelousuário?
Vamos por partes. Perceba que no atributo value
da tag selectManyListbox referenciamos a propriedade
selectedAuthorsIds. É justamente a lista que vamos manter na
nossaclasse AdminBooksBeanparapodermosreceberosIDsselecionados.
@Model
public class AdminBooksBean {
...
private List<Integer> selectedAuthorsIds =
new ArrayList<>();
// get e set para esse atributo.
}
Semprequeumusuárioselecionarosautoresetentarcadastrarumnovo
livro,vamosusaros idsescolhidosparaassociarosautoresaolivro.
@Model
public class AdminBooksBean {
...
private List< Integer> selectedAuthorsIds =
new ArrayList<>();
@Transactional
public void save(){
populateBookAuthor();
bookDAO.save(product);
}
private void populateBookAuthor() {
selectedAuthorsIds.stream().map( (id) -> {
return new Author (id);
}).forEach( product :: add);
}
}
Ométodo populateBookAuthorusaumpoucodapartedoslambdas
doJava8. Lembretambémdecriarométodo addnaclasse Book,para
61

## Página 74

4.1. Associandováriosautores CasadoCódigo
quepossamosadicionarcadaumdoslivros.Paraquenossatelafuncionede
maneiraadequada,precisamosforneceralistadeautoresquedeveserexibida.
Percebaqueatag selectItemsfazreferênciaàpropriedade authors,
daclasse AdminBooksBean.
<f:selectItems value="#{adminBooksBean.authors}" var="author"
itemLabel= "#{author.name}" itemValue="#{author.id}" />
Paraqueissofuncione,énecessárioquepelomenossejacriadoum getter
nonossobean.
@Model
public class AdminBooksBean {
...
private List<Author> authors = new ArrayList<Author>();
...
public List<Author> getAuthors() {
return authors;
}
}
Nessemomento,onossocódigonemcompila,jáqueaindanãocriamos
aclassequerepresentaoautor.Aindabemqueesseéumproblemafácilde
seresolver.
package br.com.casadocodigo.loja.models;
...
@Entity
public class Author {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Integer id;
private String name;
62

## Página 75

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
/**
* @deprected Apenas para o uso dos frameworks.
*/
public Author(){
}
public Author(Integer id) {
this.id = id;
}
//métodos de acesso
}
Quandovocêreiniciaroservidor,dadaanossaconfiguraç ãodoHiber-
nate,obancodedadosjávaiseratualizadocomanovatabela.Parafacilitar,
jávamoscriaralgunsautores,bastaexecutarosseguintesinsertsnoseubanco
dedados:
insert into Author(name) values('Alberto Souza');
insert into Author(name) values('Mauricio Aniche');
insert into Author(name) values('Adriano Almeida');
insert into Author(name) values('Paulo Silveira');
insert into Author(name) values('Sergio Lopes');
insert into Author(name) values('Guilherme Silveira');
Agora,casovocêacesseateladecadastrodenovoslivros,vaiperceberque
elaatéfunciona,masnãoexibenenhumautornocampodesele ção.Naver-
dade,oleitormaisatentotalvezatétenhapercebidoisso,jáqueemnenhum
momentofoicarregadaumalistadeautoresemnossocódigo.
Nessemomento,semprequeusarmosaclasse AdminBooksBeanvamos
teranecessidadedecarregaralistadeautores.Pensandonisso,umaprimeira
soluçãoquepodepassarpelanossacabe çaéadecarregaressalistadiretono
construtor.
@Model
public class AdminBooksBean {
@Inject
63

## Página 76

4.1. Associandováriosautores CasadoCódigo
private AuthorDAO authorDAO;
private List<Author> authors = new ArrayList<Author>();
...
public AdminBooksBean(){
this.authors = authorDAO.list();
}
...
}
Ograndeproblemaaquiéqueoconstrutorvaiserexecutadoantesdain-
jeçãodedependênciastersidorealizadanonossoobjeto.Pararesolverisso,
pensandoemOrientaçãoaObjetos(OO),bastariaquerecebêssemosasde-
pendênciaspeloconstrutor.
@Inject
public AdminBooksBean(AuthorDAO authorDAO,BookDAO bookDAO) {
this.bookDAO = bookDAO;
this.authors = authorDAO.list();
}
Casovocêtentefazeressaalteração,nomomentodo restartdoservidor,
vocêreceberáaseguinteexception:
WELD-001435: Normal scoped bean class
br.com.casadocodigo.loja.managedbeans.AdminBooksBean is not
proxyable because it has no no-args constructor - Managed Bean
[class br.com.casadocodigo.loja.managedbeans.AdminBooksBean] with
qualifiers [@Any @Default].
Aquisomosobrigadosaaceitarodestino.Aespecificaç ãodoCDIdefine
quetodaclassecujoescopoforsuperiora dependentprecisaterumconstru-
torsemargumentos. Podemosatétrabalharcomumconstrutorsemargu-
mentoseoutrocom,comojáestamosacostumadosafazerparaatenderos
frameworks,masnessecasousaremosumasoluç ãoalternativa.
Comoprecisamosrodarumcódigoapósapartedeinje çãotersidofeita,
podemoscriarummétodononosso beaneanotá-locom @PostConstruct.
64

## Página 77

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
@PostConstruct
public void loadObjects(){
this.authors = authorDAO.list();
}
Essaannotationvemdeumaespecificaç ãochamada Commons Anno-
tations for the Java Plaftorm. Vocêpodesaberumpoucomaissobreela
acessandooendere çohttps://jcp.org/en/jsr/detail?id=250.
Seuobjetivoédefiniralgumasannotationsquepodemserúteisemtodo
tipodeaplicaçãoJava,desdeaplicaçõesdesktopatéaplicaçõeswebquero-
demdentrodeservidoresdeaplicações,igualànossasituaç ão.Lembre-sede
queessemétodoéchamadoautomaticamentepelanossaimplementaçãodo
CDI,idealmentevocênuncadeveriachamá-lomanualmente.Atépensando
nisso,aespecificaçãopermitequevocêdiminuaavisibilidadedométodopara
private.
Problemas com a conversão
Comosautoresdevidamentecarregados,chegouahoradetentarmosre-
alizarnovoscadastros. Oproblemaéque,nahoradeconcluirocadastro,
recebemosaseguinteexception:
javax.servlet.ServletException: java.lang.ClassCastException:
java.lang.String cannot be cast to java.lang.Integer
OJSFnãoconseguiuconverteros idsdosautoresparaotipointeiroes-
peradodentrodalista.Oproblemaé,atécertoponto,curioso,poisseadicio-
narmosum System.outdentrodométodoqueadicionaosautoresdentro
dolivro,serãoimpressostodosos idsqueforamselecionados.
private void populateBookAuthor() {
//Essa linha imprime => [3, 1, 2]=====
System.out.println(selectedAuthorsIds+"=====");
selectedAuthorsIds.stream().map( (id) -> {
return new Author( id);
}).forEach(product :: add);
}
65

## Página 78

4.1. Associandováriosautores CasadoCódigo
Agrandearmadilhaaquiéousodapartede Generics.Quandodefi-
nimosotipodeumalista,somosobrigadosarespeitá-lo,sóqueapenasem
tempodecompilação. Emtempodeexecução,atéexistemmeiosderecu-
perarotipoquefoidefinidoegarantirqueelesóentraránalistadevalores
querespeitemarestrição. Aseguir,vejaumexemplousandoumpoucode
reflection.
Field field = AdminBooksBean.class.getDeclaredField
("selectedAuthorsIds");
ParameterizedType type =
(ParameterizedType)field.getGenericType();
//imprime java.lang.Integer
System.out.println(type.getActualTypeArguments()[0]);
SóquenessepontooJSFcometeumpecado. Aimplementaç ãopa-
drão que usamos, aMojarra, não faz essa verificação de maneira auto-
mática e, por consequência, adiciona objetos do tipo String à lista que
deveria ser de inteiros. E é exatamente essa falha, ou podemos chamar
até de preguiça, que faz o nosso código receber uma exception do tipo
java.lang.ClassCastException.
Paracontornaresseproblema,pelomenosnestemomento,temosdere-
correraousodeumdetalhedeimplementaç ãodoJSF.Podemosconfigurar
paraserusadoumconversorespecíficoparaosvaloresdeumdeterminado
componente.
<h:selectManyListbox
value="#{adminBooksBean.selectedAuthorsIds}"
converter= "javax.faces.Integer">
<f:selectItems value="#{adminBooksBean.authors}"
var="author"
itemLabel="#{author.name}" itemValue="#{author.id}" />
</h:selectManyListbox>
Reparequepassamoso iddoconversorresponsávelportransformar
objetosdotipo Stringemobjetosdotipo Integer.Essainformaçãopode
serencontradadentrodaprópriaclassequedefineoconversor.
package javax.faces.convert;
66

## Página 79

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
public class IntegerConverter implements Converter {
/**
* <p>The standard converter id for this converter.</p>
*/
public static final String CONVERTER_ID =
"javax.faces.Integer";
...
}
Vocêtambémpodenavegaratéhttp://docs.oracle.com/javaee/7/tutorial/
jsf-page-core001.htmparaencontraros idsnecessários.
Independentedaforma,estamosquebrandooencapsulamentodocon-
versorparaconseguirrealizarumasimplestransformaç ão. Provavelmente,
nãoacontecerá,mas,casoo idsejatrocado,muitasaplicaçõespodemsofrer.
Pronto,agoraconseguimoscadastrarnovoslivroscomseusautores.No
próximocapítulo,vamosmelhoraraindamaisessapartedeconversão!
4.2 L impando o formulário
Depoisquevocêrealizoualgunscadastros,deveterpercebidoqueosdados
aindapermaneceramnoscamposdoformulário. Essaéumacaracterística
marcantedoJSF.Porpadrão,elesempremantémoestadodaárvoredecom-
ponentesusadas.Emnossocaso,estamosusandoinputsquesãopreenchidos
comvaloresvindosdosbeans,entãoosdadossãomantidosmesmoapósum
request.
Paraonossocadastro,essecomportamentonãofazmuitosentido.Depois
decadastrarumnovolivro,queremosqueesseformuláriofiquelimpo.Para
fazerisso,precisamoslimparosdadosmantidosdentrodetodososobjetos
queestãoligadosaonossoformulário.
@Transactional
public void save(){
populateBookAuthor();
bookDAO.save(product);
clearObjects();
67

## Página 80

4.3. Listandooslivros CasadoCódigo
}
private void clearObjects() {
this.product = new Book();
this.selectedAuthorsIds.clear();
}
Percebaquesimplesmenteinstanciamosdenovoosobjetos.Nocasoda
lista,retiramostodososobjetosqueestavamdentrodela,maspoderíamoster
atribuídoumanovainstânciado ArrayList.
4.3 L istando os livros
Outrafuncionalidadeimportantenapartedeadministraç ãodaCasadoCó-
digoéadelistaroslivroscadastrados.Ointeressantedessaimplementaç ão
équenãoprecisaremosusarnadadenovo,eservirácomorevisãodealguns
dosconceitosqueforamdiscutidosatéaqui.
Maisumavez,vamoscome çarpensandonapágina,queteráonomede
lista.xhtml,eficará,comojáeraesperado,napasta livros:
<html xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://xmlns.jcp.org/jsf/core"
xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets">
<h:body>
<h:dataTable value="#{adminListBooksBean.books}"
var="book">
<h:column>
<f:facet name="header">
Titulo
</f:facet>
#{book.title}
</h:column>
<h:column>
<f:facet name="header">
Número de páginas
</f:facet>
#{book.numberOfPages}
68

## Página 81

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
</h:column>
<h:column>
<f:facet name="header">Autores</f:facet>
<ui:repeat var="author"
value="#{book.authors}">
#{author.name}|
</ui:repeat>
</h:column>
</h:dataTable>
</h:body>
</html>
Éumapáginabemcomum,apenasusamosalgumastagsdoJSFparacri-
armosumatabelae,alémdisso,exibimosquaissãoosautoresassociadosao
livro. Paraessatelafuncionar,percebaqueprecisamosdeumanovaclasse
chamada AdminListBooksBean.
package br.com.casadocodigo.loja.managedbeans.admin;
@Model
public class AdminListBooksBean {
@Inject
private BookDAO bookDAO;
private List< Book> books = new ArrayList<Book>();
@PostConstruct
private void loadObjects(){
this.books = bookDAO.list();
}
public List<Book> getBooks() {
return books;
}
}
Perceba que não tem nada de muito diferente do que já fizemos
no beanresponsável pelo cadastro de novos livros. Também usamos o
69

## Página 82

4.4. ForwardxRedirect CasadoCódigo
@PostConstructparaacessaroDAOinjetado,einvocarmosométodoque
vairetornaralistadelivros.Porsinal,essemétodoéjustamenteaúnicacoisa
novanessetrechodecódigo.
public class BookDAO {
@PersistenceContext
private EntityManager manager;
public void save( Book product) {
manager.persist(product);
}
public List<Book> list() {
return manager.createQuery("select distinct(b) from
Book b join fetch b.authors",Book.class)
.getResultList();
}
}
Adecisãodecriarumanovaclasseparausarnessanovatelaéumadecisão
desteautorquevosescreve.Nãoexistenenhumaregradizendoquevocêdeve
terum beanparacadanovatela. Entretanto,aOrientaçãoaObjetos(OO)
dizquequantomaissepararmosasresponsabilidades,melhorseráquando
tivermosqueevoluirnossocódigo. Semcontarque,porqualmotivovocê
ficariacarregandoalistadelivros?Elasóéusadanessatela,enãonaoutra.
4.4 F orw ard x Redirect
Agoraquejáinserimoselistamos,chegouahorademelhorarumpoucoo
fluxoentreessasoperações.Nestemomento,quandoumlivroéinserido,o
usuáriovoltaparaamesmateladecadastro. Nessetipodecenário,ofluxo
maisindicadoévoltarcomousuárioparaalistagem,talvezmostrandouma
mensagemdesucesso.
@Transactional
public String save(){
populateBookAuthor();
70

## Página 83

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
.save(product);
clearObjects();
return "/livros/lista";
}
Essecódigoimplementajustamenteofluxosugerido.Quandoacabamos
desalvarumnovolivro,pedimosparaoJSFnosdirecionarparaoendere çode
listagem,responsávelporlistarosprodutos.Opontonegativodessasoluç ão
équeoendere çoqueficanabarradonavegadoraindaéoúltimoacessado
pelousuário,que,nessecaso,foium postpara /livros/form. Casoo
nossoclienteaperteum F5,onavegadorvaitentarrefazeraúltimaoperaç ão,
causandoumanovainser çãodeprodutonosistema.
Fig.4.2:Problemadoforwarddepoisdeumpost
Observequeopróprionavegadorpercebequetemalgodeestranhoe
perguntasevocêtemcertezadequequerreenviarosdados.Essatécnicade
redirecionamentoqueaconteceapenasdoladodoservidoréoquechama-
mos,nomundoJava,de forward.Obrowsernemsabeoqueaconteceu,tanto
que,seolharmosnoconsoledoChrome,elesóvaiidentificarum request.
71

## Página 84

4.4. ForwardxRedirect CasadoCódigo
Fig.4.3:Chrometoolsindicaapenasumrequest
Éconsideradoumamápráticarealizarumforwardapósousuárioter
feitoum post,justamenteporcontadoproblemadaatualizaç ão.Paraesse
cenário,amelhorsoluçãoéforçarousuárioafazerumanovarequisiçãopara
anossalistageme,dessaforma,permitirqueeleatualizeapáginasemque
umnovo postsejarealizado.
@Transactional
public String save(){
populateBookAuthor();
.save(product);
return "/livros/lista?faces-redirect=true";
}
Oparâmetro faces-redirect=trueindicaparaoJSFque,emvezde
simplesmentefazerumforward,énecessárioqueeleretorneostatus302para
onavegador,solicitandoqueestefaçaumnovo requestparaonovoendere ço.
Fig.4.4:Chrometoolsindicadoisrequests
72

## Página 85

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
Fig.4.5:Detalhesdarespostageradapeloservidor
Percebaque,entreoscabe çalhoscontidosnaresposta,existeumchamado
Location,queinformajustamentequaléoendere çoaoqualonavegador
devefazerapróximarequisição.Essatécnica,emquefazemosum redirectdo
ladodoclientelogoapósum postválido,éumpadrãoconhecidonaweb,
chamadode Always Redirect After Post,edevesersempreutilizado.
Este padrão não é muito comum no JSF
Pormaisqueessepadrãosejamuitoconhecidonaweb,oJSFnão
nosforçaautilizaressaboapráticaporcontadoseuestilodemanteres-
tadodoscomponentesnoservidor.Aqui,éapenasumaquestãodegosto.
Esteautornãoenxergaavantagememdeixardetrabalharcomomodelo
padrão.Prefirodeixarparausaressamanuten çãodoestadoquandoreal-
mentefornecessário,porexemplo,quandoestivermostrabalhandocom
validação.Alémdisso,acabamosdetirarumcódigoquenãotinhanada
avercomnossalógicadaaplicação,queeraalimpezadosobjetos,apenas
paranãomantermososdadosnonossoformulário.
4.5 E xibindo a mensagem de sucesso
Aindasobreonosso redirect,geralmenteénecessárioqueindiquemospara
ousuárioquetudoocorreubem. Issoéfeitoexibindoumamensagemde
73

## Página 86

4.5. Exibindoamensagemdesucesso CasadoCódigo
sucessoparaoclienteemquestão.
UmadasmaneirasderealizaressatarefaéutilizandoumaclassedoJSF,
dequevocêaindavaiouvirfalarbastante,chamada FacesContext.
@Transactional
public String save(){
populateBookAuthor();
bookDAO.save(product);
FacesContext facesContext =
FacesContext.getCurrentInstance();
facesContext.addMessage(null,
new FacesMessage("Livro gravado com sucesso"));
return "/livros/list?faces-redirect=true";
}
Aclasse FacesContextéusadainternamentepeloJSFecontémvárias
informaçõesassociadasaumrequestnaaplicaç ão. Aseguir,temosalguns
métodosdeexemplo:
•getExternalContext()–paraacessarmosobjetosdaespecificação
deServlets;
•getMessagesList()–paratermosacessoatodasasmensagensadi-
cionadas;
•addMessage(...)–paraadicionarmosumamensagemaserexibida
naview;
•isValidationFailed()–paraverificarsehouvefalhasnoprocesso
devalidação.
Aindaexistemváriosoutrosmétodos.Percebaque,inclusive,usamoso
addMessageparaadicionaramensagemdesucesso.Osegundoparâmetroé
atébemclaro,aclasse FacesMessageéaabstraçãodoJSFpararepresentar
umamensagemquevaiseradicionadaàtela. Jáoprimeiroparâmetro,que
nonossocasofoi null,descobriremosomotivoemalgunsminutos.
74

## Página 87

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
Adicionamosamensagem,masumaperguntaqueficaé: onde e como
vamos mostrar essa informação para o usuário?Nonossocaso,queremosque
elasejaexibidanateladelistagemdoslivros,massóquandorealmentetiver
mensagens. Vamosalteraroarquivo lista.xhtml,eincluiratagdoJSF
responsávelporisso.
...
<h:body>
<h:messages/>
<h:dataTable value="#{adminListBooksBean.books}" var="book">
...
</h:body>
Atag messagesrealizatodootrabalhodepegarasmensagensadicio-
nadaspormeiodo FacesContexteexibirnanossatela.
Sóparanãoesquecermos,vamoscomentarsobreo nullqueestásendo
passadocomoargumentonométodo addMessage. Esseprimeiroparâ-
metroserveparaindicarmoso iddoelementocomoqualamensagem
deveestarassociada.Comonãoqueremosligaramensagemanenhumele-
mento,passamoso nulleadeixamosglobal,podendoserexibidapelatag
messages.
Agora,oengraçadoéque,casovocêrealizeumnovocadastro,amen-
sagemaindanãovaiserexibida. Quandoadicionamosmensagenscomo
método addMessage,elasficamdisponíveisduranteaexecuç ãodo request
atual.Comoestamosfazendoum redirectdoladodocliente,elasseperdem,
jáque,paraexibiralistagem,éfeitaumanovarequisiç ão.Nãosepreocupe,
esseéumproblemaclássicoemaplicaçõesweb,etodososframeworksfamo-
sosjáresolvemissoparanós.
@Transactional
public String save(){
populateBookAuthor();
bookDAO.save(product);
FacesContext facesContext =
FacesContext.getCurrentInstance();
facesContext.getExternalContext().getFlash()
75

## Página 88

4.6. Isolandoocódigodeinfraestrutura CasadoCódigo
.setKeepMessages(true);
facesContext.addMessage(null,
new FacesMessage("Livro gravado com sucesso"));
return "/livros/list?faces-redirect=true";
}
Ométodo getFlashretornaumobjetodotipo Flash. Invocando
o setKeepMessagesnesseobjeto,estamosdizendoaoJSFqueeledeve
manterasmensagensatéopróximo request.Pronto,comessaalteração,nossa
mensagemdesucessovaicome çaraserexibidanateladalistagem.
Escopo flash é um ajuste fino
Ojeitomaiscomumdepassarinformaçõesemum requestépormeio
deparâmetros.Pensandodojeitomaisnormalpossível,jáquequeremos
passaramensagemdesucessoparao requestquevairetornaratelade
listagem,poderíamosteroseguinteretornonométodo save:
return "/livros/list?faces-redirect=true
&sucesso=Livro gravado com sucesso";
Poderíamos acessar o parâmetrosucesso a partir do nosso
bean responsável pela tela de listagem, e adicionar a mensagem no
FacesContext.
HttpServletRequest request = (HttpServletRequest)
FacesContext.getCurrentInstance().getExternalContext()
.getRequest();
facesContext.addMessage(null,
new FacesMessage(request.getParameter("sucesso")))
Comoissodariamuitomaistrabalho,oescopo flashcaicomouma
luva,mantendoamensagematéopróximo request!
4.6 I solando o código de infraestrutura
Vamosanalisarcomumpoucomaisdecuidadoocódigoqueacabousendo
escritonométodo save.
76

## Página 89

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
@Transactional
public String save(){
populateBookAuthor();
bookDAO.save(product);
FacesContext facesContext =
FacesContext.getCurrentInstance();
facesContext.getExternalContext().getFlash()
.setKeepMessages(true);
facesContext.addMessage(null,new
FacesMessage("Livro gravado com sucesso"));
return "/livros/list?faces-redirect=true";
}
Acabamoscommaislinhasdecódigodedicadasausardetalhesinternos
doJSFdoquepararesolveronossoproblemaemsi,queéodegravarnovos
livros. Percebaqueestamosescrevendoocódigonecessáriopararecuperar
um FacesContextquando,naverdade,sóestamosinteressadosemusá-lo.
Aqui,denovo,temosumamotivaçãoclaraparausaroconceitodeinje çãode
dependências:isolaracriaçãodoobjetodoseuuso.
@Model
public class AdminBooksBean {
@Inject
private FacesContext facesContext;
@Transactional
public String save(){
populateBookAuthor();
bookDAO.save(product);
facesContext.getExternalContext().getFlash()
.setKeepMessages(true);
facesContext.addMessage(null,
new FacesMessage("Livro gravado com sucesso"));
return "/livros/list?faces-redirect=true";
}
77

## Página 90

4.6. Isolandoocódigodeinfraestrutura CasadoCódigo
...
}
Perceba que pedimos para receber injetado o objeto do tipo
FacesContext em vez de ficar criando todas as vezes em que preci-
sarmos dele. Agora, quando tentamos subir a aplicação, recebemos a
seguinteexception:
WELD-001408: Unsatisfied dependencies for type FacesContext with
qualifiers @Default at injection point [BackedAnnotatedField]
@Inject private br.com.casadocodigo.loja.managedbeans.admin
.AdminBooksBean.facesContext at
br.com.casadocodigo.loja.managedbeans.admin.AdminBooksBean
.facesContext(AdminBooksBean.java:0)
Elaindicaqueo WELDnãofoicapazdeinjetaroobjetonoatributo
facesContextdaclasse AdminBooksBean. Aclasse FacesContexté
abstrata,portanto,nãopodeserinstanciada. Suaimplementaç ãopadrão,a
FacesContextImpl,temumconstrutorquerecebeobjetosespecíficosdo
JSFtambém.
public FacesContextImpl(ExternalContext ec,
Lifecycle lifecycle){
...
}
Atéaversão2.2,versãoatualdoJSF,nãotemumaintegraç ãocompleta
comoCDI.Algunscomponentes,comoo FacesContext,aindanãosão
gerenciadospelocontainerdeinje ção.Apartelegaléqueissonãoéumpro-
blemamuitograndeparanós,bastaqueensinemosaoCDIcomoeledeve
criarumobjetodotipo FacesContext.
package br.com.casadocodigo.loja.infra;
import javax.enterprise.context.ApplicationScoped;
import javax.enterprise.context.RequestScoped;
import javax.enterprise.inject.Produces;
import javax.faces.context.FacesContext;
78

## Página 91

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
@ApplicationScoped
public class FacesContextProducer {
@Produces
@RequestScoped
public FacesContext get(){
return FacesContext.getCurrentInstance();
}
}
Ométodoanotadocom @Producesdevesersempreusadoquandoo
processodecriaçãodeumobjetonãoéopadrão. Outrasituaç ãoéquando
queremosproduzirumobjetodeumaclassequenãoégerenciadapeloCDI.
O FacesContext,porcoincidência,seenquadranasduassituações.Ainda
usamosduasanotaçõesreferentesaoescopo:
•@ApplicationScoped–paradizerquesóénecessáriaumainstância
do FacesContextProducer;
•@RequestScoped–paradizerqueométodo getdeveserchamado
umavezacadanovo request.
Éimportantequeo FacesContextsejanovamenteproduzidoacada
request,casocontrário,vocêpodeacabarinjetandoumainstânciaquefoipo-
puladacominformaçõesdeoutrarequisição.
JSF 2.3 mais integrado com o CDI
AnovaversãodoJSFvirábemmaisintegradaaoCDI.Componentes
internosjávãoterprodutoresdefault,nospoupandodecriarestecódigo
dentrodonossoprojeto.
Caso queira saber mais sobre as novas integrações, acessehttp://
jdevelopment.nl/jsf-23/.
79

## Página 92

4.6. Isolandoocódigodeinfraestrutura CasadoCódigo
Isolando a adição de mensagens no Flash
Nossocódigomelhorouumpouco,masaindatemos2linhasquesãores-
ponsáveisporadicionarumamensagemnoflash.
facesContext.getExternalContext().getFlash()
.setKeepMessages(true);
facesContext.addMessage(null,
new FacesMessage("Livro gravado com sucesso"));
Esteéumdostrechosdecódigoquetambémgeramdordecabe ça.Para
onossocaso,o addMessagesófazsentidosevocêchamaralinhadecima.
Achancedeissoseresquecidoérelativamentealtae,provavelmente,vamos
acabarperdendoumtempopreciosoparaacharacausadobug.
Umoutrofatoquedevemosconsideraréqueestamosprogramandoori-
entandoaobjetos,epodemoscriarabstraçõesumpoucomelhoresparaque
ocódigofiquemaisfácildeserentendido.
@Model
public class AdminBooksBean {
@Inject
private MessagesHelper messagesHelper;
@Transactional
public String save(){
populateBookAuthor();
bookDAO.save(product);
messagesHelper.addFlash(
new FacesMessage("Livro gravado com sucesso"));
return "/livros/list?faces-redirect=true";
}
}
Percebaqueagoratemosummétodoquedizclaramenteoqueestásendo
feito.Usamosumanovaclassechamadade MessagesHelper,quefoicriada
justamenteparaisolaressecomportamento.
80

## Página 93

CasadoCódigo Capítulo4. MelhorandoocadastroeumpoucomaisdeJSF
package br.com.casadocodigo.loja.infra;
import javax.enterprise.context.ApplicationScoped;
import javax.faces.application.FacesMessage;
import javax.faces.context.FacesContext;
import javax.inject.Inject;
public class MessagesHelper {
@Inject
private FacesContext facesContext;
public void addFlash(FacesMessage facesMessage) {
facesContext.getExternalContext().getFlash()
.setKeepMessages(true);
facesContext.addMessage(null,facesMessage);
}
}
4.7 C onclusão
Nestecapítulo,evoluímosnossocadastro. Alémdisso,vimosumconceito
importanteemaplicaçõesweb,queéoescopo Flasheacapacidadedefa-
zermos redirectsnoladodocliente. Esteúltimo,apesardeserumconceito
naturalemumaaplicaçãoweb,nãoémuitousadonomundoJSF,porconta
domodelodeprogramaçãoimpostopeloframework.
Tambémcomeçamosumadiscussãosobreosmecanismosdeconversão
dosvaloresvindosdos requestsparaostiposdonossosistemae,infelizmente,
caímosemumasituaçãoruim,causadapelopróprioJSF.
Parafechar,discutimosumpoucodeboaspráticasdecódigo,evimos
comooCDInosajudouadeixaronossocódigoumpoucomaisdesacoplado
ecoeso.
Nopróximocapítulo,vamostentarmelhoraraconversãodanossalistade
autoresetambémtratarsobreavalidaçãodosvaloresvindosdoformulário.
Casoaindaestejacomfôlego,nãopareagoraecontinuealeitura.
81

## Página 95

Capítulo5
Validaçãoeconversãodedados
Onossocadastrojáestáfuncional,masestamosdeixandodefazerumacoisa
básica:validarosdadosdeentrada.Nestemomento,casoumusuárioqueira
cadastrarumnovolivro, eletemaop çãodedeixartodososcamposem
branco.
5.1 V alidação básica
Aprimeiraop çãodesoluçãoparaessasituaçãoéescreverocódigodevalida-
çãodentrodoprópriométodo save,daclasse AdminBooksBean.
@Transactional
public String save(){
populateBookAuthor();
if(product .getTitle()==null ||

## Página 96

5.1. Validaçãobásica CasadoCódigo
product.getTitle().trim().isEmpty()){
messagesHelper.addMessage
(new FacesMessage("titulo obrigatorio"));
}
if(product.getDescription()==null ||
product.getDescription().trim().isEmpty()){
messagesHelper.
addMessage
(new FacesMessage("descrição obrigatoria"));
}
if(messagesHelper.hasMessages()){
//volta para a mesma tela
return "/livros/form";
}
bookDAO.save(product);
messagesHelper.addFlash
(new FacesMessage("Livro gravado com sucesso"));
clearObjects();
return "/livros/list?faces-redirect=true";
}
Apesardeadicionarmosuns ifsesimularmosunsnovosmétodosna
classe MessageHelper,alógicanãotemnadadecomplicado,naverdade,
deveserbemparecidacomváriasdasquaisoleitorjápresenciou.Umponto
negativodessasoluçãoéqueoManagedBean,queidealmentedeveriaapenas
ficarchamandológicasdosistemaecontrolandoqualéopróximopassode
navegação,agoratambémestáresponsávelpelocódigodevalidação.
ComoumadasideiasoriginaisdoJSFésermuitoútilparaaplicaçõescom
muitosformulários,suastagsdeinputjávêmcomatributosquehabilitam
essetipodevalidaçãobásica.
<h:body>
<h:messages/>
<h:form>
<div>
84

## Página 97

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
<h:outputLabel>Titulo</h:outputLabel>
<h:inputText
value="#{adminBooksBean.product.title}"
required="true"/>
</div>
<div>
<h:outputLabel>Descrição</h:outputLabel>
<h:inputTextarea cols="20" rows="10"
value="#{adminBooksBean.product.description}"
required="true"/>
</div>
<div>
<h:outputLabel>Número de páginas</h:outputLabel>
<h:inputText
value="#{adminBooksBean.product.numberOfPages}"
required="true">
<f:validateLongRange minimum="80"/>
</h:inputText>
required="true"/>
</div>
<div>
<h:outputLabel>Preço</h:outputLabel>
<h:inputText value="#{adminBooksBean.product.price}"
required="true">
<f:validateDoubleRange
minimum="10" maximum="100"/>
</h:inputText>
</div>
<div>
<h:outputLabel>Autores</h:outputLabel>
<h:selectManyListbox
value="#{adminBooksBean.selectedAuthorsIds}"
required="true">
<f:selectItems
value="#{authorsList.get()}" var="author"
itemLabel= "#{author.name}"
itemValue= "#{author.id}" />
</h:selectManyListbox>
85

## Página 98

5.1. Validaçãobásica CasadoCódigo
</div>
<h:commandButton value="Gravar"
action="#{adminBooksBean.save}" />
</h:form>
</h:body>
</html>
Oatributo requiredéútilapenasparaverificarseocampofoipreen-
chidoounão.Alémdesseatributo,aindapodemosassociarvalidadoresmais
específicoscomosinputs.Porexemplo,usamoso validateDoubleRange
paracolocarumlimitenospossíveisvaloresdolivro.Éimportanteressaltar
queessavalidaçãoérealizadadoladodoservidor,poisastagsdevalidaç ão
doJSFnãogeramqualquercódigoJavaScript.
Paraexibirasmensagensdeerro,tambémnãoprecisamosalterarnada,
dadoqueusamosamesmatag messages.Paracadaproblemaencontrado,o
JSFadicionamensagensexatamentedojeitoquenósfizemosdurantealógica
decriaçãodeumlivro.
Comessasaltera ções,semnemprecisarmosalterarcódigoJava,jáconse-
guimosnosprecaverdeformuláriospreenchidosdemaneiraincorreta.
Oleitormaisatentodeveterpercebidoqueaconteceumafalhadevalida-
ção:ousuárioéautomaticamentelevadoparaamesmatelaemqueeleestava,
queéjustamenteocomportamentoquenósdesejamos.Alémdisso,também
nãofoinecessárionenhumcódigoextraparamanterosvaloresdosinputs,
situaçãomuitocomumemoutrosframeworksMVC.Esseéumpontoque
devemosagradeceraomodelomanuten çãodeestadodoscomponentesdo
JSF,tambémconhecidocomo stateful.
Um pouco sobre o ciclo de vida
Quandorealizamosarequisição,oJSFatualizaaárvoredecomponentes
relativaàtelaatual,aplicandoosvaloresqueforampreenchidosnoformulá-
rio.Vejaaseguirumtrechodecódigodaclasseresponsávelporisso.
/**
* ApplyRequestValuesPhase executes <code>processDecodes</code>
* on each component in the tree so that it may update it's
* current value from the information included in the current
86

## Página 99

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
* request (parameters, headers, cookies and so on.)
*/
public class ApplyRequestValuesPhase extends Phase {
public void execute(FacesContext facesContext)
throws FacesException {
if (LOGGER.isLoggable(Level.FINE)) {
LOGGER.fine("Entering ApplyRequestValuesPhase");
}
UIComponent component = facesContext.getViewRoot();
assert (null != component);
try {
component.processDecodes(facesContext);
}
}
...
}
Ocomentárioestáeminglês,maselebasicamentefalaamesmacoisado
parágrafoanterior. Depoisqueosvaloressãoassociadosaoscomponentes,
elevaiaplicarasregrasdevalidaçõese,aí,quandoelasfalham,bastaelerees-
creveroHTMLbaseadonoestadodecadaelementodatela.
Quandotrabalhamosnomodoconvencional,geralmentenóstemosde
tomarcontadeumapartedessefluxo.Porissoque,naopiniãodesteautor,o
modelohíbridogeralmenteéomelhor.Mantemosoestadoquandonecessá-
rio,erecriamostudodozeroquandoformaisinteressante,comonocapítulo
4(seção4.4)como redirect.
5.2 E xibindo as mensagens de erro de maneira
amigável
Pormaisqueoformulárioestejasendovalidado,asmensagensdeerroainda
nãodizemmuitacoisasobreoproblemaemquestão.
87

## Página 100

5.2. Exibindoasmensagensdeerrodemaneiraamigável CasadoCódigo
j_idt4:j_idt8: Validation Error: Value is required.
j_idt4:j_idt12: Validation Error: Value is required.
j_idt4:j_idt16: Validation Error: Value is less than allowable
minimum of '100'
j_idt4:preco: Validation Error: Value is required.
j_idt4:j_idt26: Validation Error: Value is required.
j_idt4:j_idt28: Validation Error: Value is required.
Pensando no cliente, essas mensagens e nada dizem praticamente a
mesmacoisa. Percebaque,antesdecadamensagemdevalidaç ão,aparece
umaespéciede id.Comonãoinformamosnenhum idespecíficoparanos-
soselementos,oJSFgeraosdeleparacontroleinterno.Então,umaprimeira
açãoparamelhoraramensageméadecolocar idsparanossoselementos.
<h:form>
<div>
<h:outputLabel>Titulo</h:outputLabel>
<h:inputText value="#{adminBooksBean.product.title}"
required="true" id="titulo"/>
</div>
...
Agora,setentarmoscadastrarumlivrosemtítulo,amensagemdevali-
daçãoseráparecidacomaseguinte:
j_idt4:titulo: Validation Error: Value is required.
PercebaqueaindasobrouumidentificadorgeradopeloJSF.Eleéo iddo
formulárioaoqualoinputpertence.Podemosusaroatributo prependId,
datag form,paradizerquenãoqueremosqueelefiquesendoadicionado
comopartedaidentificaçãodoelemento.
<h:form prependId="false">
<div>
<h:outputLabel>Titulo</h:outputLabel>
<h:inputText value="#{adminBooksBean.product.title}"
required="true" id="titulo"/>
</div>
88

## Página 101

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
...
</h:form>
Agora,quandoocorrerumafalhadevalidação,amensagemseráparecida
comessa:
titulo: Validation Error: Value is required.
...
Estaalteraçãojádeixaonossousuárioumpoucomaisfeliz,entretanto,
essamensagememinglêsaindanãotemmuitoavercomonossoprojeto.Para
tentarmelhorar,podemosrecorreraoutroatributodastagsdeformulário.
<h:inputText value="#{adminBooksBean.product.title}"
required="true"
id="titulo"
requiredMessage="Campo obrigatório"/>
...
Oatributo requiredMessagepermitequevocêespecifiqueumamen-
sagemdevalidaçãorelacionadaaoatributo required. Comessaúltima
alteração,quandotentamoscadastrarumlivrosemdizerqualotítulo,rece-
bemosaseguinteamensagemdevalidaç ão:
Campo obrigatório
Campo obrigatório
Campo obrigatório
...
Atéqueamensagemficoudojeitoquenósqueríamos,porém,perdemos
odetalhequeinformavaqualcampotinhadadoproblema.Pararesolvereste
problema,podemosrecorreràtag message.
<div>
<h:outputLabel>Titulo</h:outputLabel>
<h:inputText value="#{adminBooksBean.product.title}"
required="true" id="titulo"
requiredMessage="Campo obrigatorio"/>
<h:message for="titulo"/>
</div>
89

## Página 102

5.3. TrocandoasmensagensdefaultdoJSF CasadoCódigo
Elapermitequeassociemosamensagemcomalguminputdanossapá-
gina.Dessaforma,conseguimosexibiramensagemondeformaispertinente
paraaaplicação.
5.3 T rocando as mensagens default do JSF
Atéquechegamosaumasoluçãodevalidaçãojusta,sótemumdetalheque
aindapodenosincomodar,especificamenterelacionadocomamensagem
devalidação. Decidimosque,quandoocampoéobrigatório,vamosusaro
textodealerta“Campoobrigatório”. Casovocêsótenhaumformuláriona
aplicação,atéquenãofazdiferen ça,masemumcontextoumpoucomais
amplo,essamensagemficaráespalhadaemtodososlugares.
Todas as mensagens de conversão e validação que são exibidas pelo
JSFpodemsercustomizadas. Elas,pordefault,encontram-senoarquivo
Messages.properties,quevemdentrodo jardaespecificaçãodoJSF.
Todas as mensagens de conversão
Casofiquecuriosoparasabertodasaspossibilidades,acesse http://
bit.ly/messages-properties-jsf.
Paraalteraressasmensagens,precisamoscriaranossaversãodoarquivo
esubstituiraschavesquetêmrelaçãocomanossaaplicação.Paracome çar,
vamoscriarumarquivochamado jsf_messages.propertiesdentrode
src/main/resources,comoseguinteconteúdo:
javax.faces.component.UIInput.REQUIRED={0}: Campo obrigatório
UsamosamesmachavedefinidapeloJSF,sóalteramosovalor.Oparâme-
trodeíndice zeroéjustamenteo iddoelemento.Agora,precisamosensinar
aoJSFqueelesempredeveprocurarasmensagensprimeirononossoarquivo
e,depois,nodele.Paraisso,vamosalteraroarquivo faces-config.xml,
queestáem src/main/webapp/WEB-INF.
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<faces-config xmlns="http://xmlns.jcp.org/xml/ns/javaee"
90

## Página 103

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
version="2.2"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
http://xmlns.jcp.org/xml/ns/javaee/web-facesconfig_2_2.xsd">
<application>
<message-bundle>jsf_messages</message-bundle>
</application>
</faces-config>
Você poderia ter colocado o arquivo em qualquer lugar no seu
classpath,bastaqueinformenatag message-bundle. Comessaalte-
ração,podemosinclusiveapagarousodoatributo requiredMessagedos
nossosinputs. Agora,casovocêtenhamantidoatag messagesnoinício
doseuformulário,quandoacontecerumerrodevalidação,amensagemserá
exibidadojeitoquegostaríamos.
titulo: Campo obrigatório
Alterando a mensagem de conversão
Voltandoumpoucoparaosproblemasdevalidaç ão,umoutroerroque
podeexistirnoformuláriodecadastroéaentradadeumvalornãocondizente
comotipodocampo.Porexemplo,umusuáriopodedigitar“dez”emvezde
“10”nocampodenúmerodepáginas.
Essetipodesituaçãotambémacontece,emgeral,comcamposdevalores
depontoflutuante,comoéocasodopre çodonossolivro.Casoapessoadigite
“59,90”,ocorreráumproblemadeconversãoparanossotipoBigDecimal,
jáquearepresentaçãodeumvalordestetipodeveserfeitacom .(ponto),e
nãocom ,(vírgula).Seráexibidaaseguintemensagem,tambématravésda
tag messages:
preco: '59,90' must be a signed decimal number.
Comopodemosver,éumamensagemnadaamigávelparaousuárioco-
mum.
Paraexibirmensagensamigáveiserelativasaoserrosdeconversão,adi-
cionamosaschavesquecome çamcom avax.faces.converter.
91

## Página 104

5.4. IntegraçãocomaBeanValidation CasadoCódigo
javax.faces.converter.IntegerConverter.INTEGER=''{2}'' deve ser
um número javax.faces.converter.BigDecimalConverter.DECIMAL={2}
deve ser um valor separado apenas por "."
Ex: 450.50 ou 4100.50
javax.faces.component.UIInput.REQUIRED={0}: Campo obrigatório
Quandoalgumproblemadeconversãoacontece,oíndice {2}recebeo
iddoinputqueoriginouoerro.
5.4 I ntegração com a Bean Validation
Anossavalidaçãojáfuncionaintegralmente,masaindatemumpontoque,
pelomenosparaesteautor,éumpoucoruim.Asnossasregrasdevalidaç ão
estãonanossaview. Quemolhaparanossomodelonãofazideiadoqueé
obrigatórioparacriarumlivro.Semcontarque,casotenhamosumaforma
alternativadecadastrarumlivro–porexemplo,pormeiodeumaimportação
deumarquivodetexto–,nãovamosconseguirreaproveitarasregras.
Essetipodesituaçãoétãocomumquevirouatéespecificaç ão,a Bean
Validation.Ecomonãopodiaserdiferente,oJSFécompletamenteintegrado
comela. Essaéumadasvantagensdeseconstruirumprojetobaseadono
JavaEE,umavezquecadavezmaisasespecificaçõesseintegramdemaneira
transparente.
AimplementaçãoquevamosutilizaréaquejávemporpadrãonoWildfly,
feitapelotimedoHibernate,chamadade Hibernate Validator.
SóprecisamosensinaraBeanValidationoquedeveservalidadonanossa
classe Book.
@Entity
public class Book {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Integer id;
@NotBlank
92

## Página 105

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
@NotNull
private String title;
@NotBlank
@NotNull
@Length(min = 10)
private String description;
@Min(50)
private int numberOfPages;
@DecimalMin("20")
private BigDecimal price;
@ManyToMany
@Size(min = 1)
@NotNull
private List<Author> authors = new ArrayList<>();
Aseguir,vejaasexplicaçõesparaalgumasdasannotations:
•NotBlank–verificaseastringédiferentede nullesetambémnão
évazia;
•Length–verificaseotamanhodastringestáentreummínimoeum
máximo;
•Min–verificaseonúmeroestáentreomínimoeomáximo;
•DecimalMin–verificaseopontoflutuanteestáentreomínimoeo
máximo;
•Size–mesmocomportamentodo@Length,maspodeseraplicado
paralistas,arraysetc.
Éimportanteressaltarqueasvalidaçõessãobemcoesas. Porexemplo,
aannotation @NotEmptyapenasdisparaavalidaçãodestringvazia.Aan-
notation @NotNullsóverificaseovalorfordiferentede null.Porconta
93

## Página 106

5.4. IntegraçãocomaBeanValidation CasadoCódigo
disso,usamosa NotBlank,queéumaannotationespecíficadoHibernate
Validatorqueuneosdoiscomportamentos.
Nesseexatomomento,estamoscomdoismecanismosdevalidaç ão:opa-
drãodaJSFeodaBeanValidation. Pensandonaaplicaç ãoemsi,nãotem
nenhumproblema.Estamosprotegidosportodososlados.Entretanto,nãoé
esseojeitoquevocêencontranomercado.Hojeemdia,aBeanValidationé
ojeitopadrãodevalidarobjetosnomundoJava,entãovamoscontinuarcom
elaapartirdaqui.
Aprimeiracoisaquevocêdevefazeréapagaroatributo requireddas
tags,etambémretirarqualquertagdevalidaç ãoquevocêtenhaadicionado
nosinputsdoformulário. Comessasalterações,quandotentamosrealizar
umnovocadastrocomdadosinválidos,recebemosasseguintesmensagens
deerro:
may not be empty
length must be between 10 and 2147483647
may not be empty
must be greater than or equal to 50
may not be null
size must be between 1 and 2147483647
Aquitemosdoisproblemas:atag messagesvoltouaexibirasmensagens
deerro,semassociarcomodevidocampo;easmensagenssãoasdefault,
definidaspelopróprioHibernateValidator.
Pararesolveroprimeiro,vamosvoltaraoarquivodemensagensdefault
doJSF.
javax.faces.validator.BeanValidator.MESSAGE={0}
Nachavequedefineamensagemassociadaaoserrosdevalidaç ãodaBean
Validation,foiconfiguradoparasóexibiroerro,seminformarqualéocampo.
Essecasoéidealsevocêoptarpormensagensassociadasdiretamenteaoin-
put.
<div>
<h:outputLabel>Titulo</h:outputLabel>
<h:inputText value="#{adminBooksBean.product.title}"
94

## Página 107

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
id="titulo"/>
<h:message for="titulo"/>
</div>
Agora,casoqueiramosexibirtodasasmensagensjuntas,jáacabaficando
confuso. Adecisãovaidependerdoestilodosistema. Paraonosso,vamos
optarporexibirtodasjuntas.Paraissofuncionar,vamossobrescreverachave
doarquivodemensagensdoJSFeadicionaronomedocampoquefalhouna
validação.
...
javax.faces.validator.BeanValidator.MESSAGE={1}:{0}
Comessaalteração,todavezqueavalidaç ãodeumcampofalhar,será
exibidaamensagemcomoseguintepadrão:
idDoElemento:mensagem de validação
Alterando as mensagens da Bean V alidation
Parafechar, sófaltacustomizarmosasmensagensdevalidaç ão. Elas
ainda,pordefault,estãoaparecendoeminglês,mascomoaCasadoCódigoé
umaempresabrasileira,devemosexibi-lasemportuguês.Parafazermosisso,
assimcomojáfizemoscomasmensagenspadrõesdoJSF,teremosdealte-
rarovalordealgumaschavesjádefinidaspelaespecificaç ãoepeloHibernate
Validator.Oarquivocomessaschavesjávemdentrodo jardopróprioHi-
bernateValidator,eseunomeé ValiadtionMessages.properties.Na
sequência,vejaalgumaschavesquejávêmpordefault:
javax.validation.constraints.AssertFalse.message =
must be false
javax.validation.constraints.AssertTrue.message =
must be true
javax.validation.constraints.Past.message =
must be in the past
javax.validation.constraints.Pattern.message =
must match "{regexp}"
javax.validation.constraints.Size.message =
size must be between {min} and {max}
95

## Página 108

5.5. Convertendoadata CasadoCódigo
...
org.hibernate.validator.constraints.NotBlank.message =
may not be empty
org.hibernate.validator.constraints.NotEmpty.message =
may not be empty
Para forçarmos as nossas mensagens, devemos criar um ar-
quivo de mesmo nome na raiz do nossoclasspath, no caso, em
src/main/resources. Aqui, éimportantelembrarparaoleitorqueo
nomedessearquivoestánaespecificaçãodaBeanValidation,nãotemosa
opçãodequerertrocardenome. Comoarquivocriado,bastaredefiniras
mensagens.
org.hibernate.validator.constraints.NotEmpty.message =
não pode ser em branco
org.hibernate.validator.constraints.NotBlank.message =
não pode ser em branco
Pronto,combinandoumpoucodeespecializaçãodoJSFcomumpouco
deespecializaçãodaBeanValidation,conseguimoschegaraoresultadoque
queríamos.Eaindapodemosescolheramelhorformadeexibirnossasmen-
sagens.
Veja todas as mensagens que podem ser alteradas
Paraveraschavesquepodemsersobrescritassemanecessidadede
ficarabrindoo jar,acesse https://github.com/hibernate/
hibernate-validator/blob/master/engine/src/main/resources/org/
hibernate/validator/ValidationMessages.properties 
5.5 C onvertendo a data
NaCasadoCódigo,muitoslivrossãoescritosotempotodo.Paraterumfluxo
interessantedelançamentos,foidecididoqueoslivroscadastradosdevemter
umadatadelan çamento.
@Entity
public class Book {
96

## Página 109

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
...
@NotNull
@Future
private Calendar releaseDate;
...
}
Percebaquejáestamosusandoasannotationsdevalidaç ãodaBeanVa-
lidation. Usamosa @Futureparagarantirqueasdatasdelan çamentosão
sempredodiaatualparaafrente.Agora,precisamoscolocarumcamponovo
nonossoformulário.
...
<div>
<h:outputLabel>
Data de lançamento
</h:outputLabel>
<h:inputText
value="#{adminBooksBean.product.releaseDate}" />
</div>
Nossocódigousaumsimplesinputdetextoparareceberumadata. É
sempreeducadofacilitaravidadousuário,eoHTML5játrazuminputque
automaticamenteabreumcalendário.Paraousarmos,devemossetaroatri-
buto typecomovalor date.
<h:inputText value="#{adminBooksBean.product.releaseDate}"
type="date"/>
OproblemaéqueoJSFignoraestenossoatributo,jáqueelenãofazparte
dosatributosespecificadosparaessatag.Esse,naverdade,eraumproblema
citadoporváriosusuáriosdoframework;elenosimpediadeterumcontrole
maisfinosobreoHTMLgerado.Sóque,desdeaúltimaversão,oJSFvemten-
tandoatacarestetópicoaofornecermaiscontroleaoselementosdaview.Por
exemplo,paraestecaso,podemosusarumnovo namespace,quepermite
forçarmosousodaspropriedadesquebementendermos.
97

## Página 110

5.5. Convertendoadata CasadoCódigo
<html xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://xmlns.jcp.org/jsf/core"
xmlns="http://www.w3.org/1999/xhtml"
xmlns:pt="http://xmlns.jcp.org/jsf/passthrough">
...
<h:inputText
value="#{adminBooksBean.product.releaseDate}"
pt:type="date"/>
</html>
Esseéoobjetivodonamespace http://xmlns.jcp.org/jsf/passthrough. Per-
cebaque,paratrocarmoso typedoinput,usamos pt:type.Osatributos
associadosaessenamespacesãoignoradospelafasederenderizaç ãodoJSF
e,dessaforma,eleserámostradonapáginafinal.
Agora,quandotentamoscadastrarumnovolivroinformandoadatade
lançamento,recebemosaseguintemensagemdeconversão:
Conversion Error setting value '2015-06-10' for 'null Converter'.
CaímosemumpontoespecíficodoJSF.Comoqueremosqueeleconverta
ovalorinseridoparaumobjetoquerepresenteumadata,precisamosindicar
quequeremosusarumconversorespecífico.Percebaqueoformatodadata
foi yyyy-MM-dd.Esteéoformatousadopeloinputdotipo datedoHTML
5.
Essapadronizaçãoéinteressante,jáqueajudanotratamentodasdatas
doladodoservidor.Assim,sabemosquesemprevamosreceberadatanesse
formato.
<div>
<h:outputLabel>Data de lançamento</h:outputLabel>
<h:inputText
value="#{adminBooksBean.product.releaseDate}">
<f:convertDateTime pattern="yyyy-MM-dd"/>
</h:inputText>
</div>
98

## Página 111

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
Usamosatag convertDateTimeparaassociaroconversorcomoinput
emquestão.Agora,quandotentamoscadastrar,caímosemoutroproblema.
javax.servlet.ServletException:
java.lang.IllegalArgumentException: Cannot convert 6/10/15
9:00 PM of type class java.util.Date to class java.util.Calendar
Aexceptionnosdizquenãofoipossívelconverterotipo Datepara
Calendar,queéjustamenteotipodonossoatributo. Oconversorasso-
ciadopegaovalorpassadonorequest,egeraumobjetodotipo Date.Eesse
éjustamenteonossoproblema.
Aqui,denovovemosumpoucodepreguiç anaequipedaespecificação,
jáque CalendaréumtipobemantigonoJavaejámereciateraconversão
automática.
Criando um Converter específico
Pararesolveresteproblema,vamosserobrigadosacriaranossaimple-
mentaçãode Converter. Oquenãoénenhumproblema,jáqueoJSFjá
vempreparadoparaserestendidonessaparte.
package br.com.casadocodigo.loja.converters;
import java.util.Calendar;
import java.util.Date;
import javax.faces.component.UIComponent;
import javax.faces.context.FacesContext;
import javax.faces.convert.Converter;
import javax.faces.convert.DateTimeConverter;
import javax.faces.convert.FacesConverter;
@FacesConverter(forClass=Calendar.class)
public class CalendarHtml5Converter implements Converter{
private static DateTimeConverter originalConverter =
new DateTimeConverter();
static {
99

## Página 112

5.5. Convertendoadata CasadoCódigo
originalConverter.setPattern("yyyy-MM-dd");
}
@Override
public Object getAsObject(FacesContext context,
UIComponent component,
String value) {
Date date = (Date)
originalConverter.getAsObject(context,
component, value);
if(date == null) {
return null;
}
Calendar newCalendar = Calendar.getInstance();
newCalendar.setTime(date);
return newCalendar;
}
@Override
public String getAsString(FacesContext context,
UIComponent component,
Object value) {
if(value == null){
return null;
}
Calendar calendar = (Calendar) value;
return originalConverter.getAsString(context, component,
calendar.getTime());
}
}
Agrandejogadaaquiéaannotation FacesConverter. Elaéaúnica
configuraçãonecessáriaparatermosumnovoconversornosistema.Como
já sabemos para qual tipo queremos converter, ainda usamos o atributo
forClass.Dessaforma,oJSFjásabeque,semprequeassociarmosuminput
100

## Página 113

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
aumapropriedadedotipo Calendar,eledeveusarnossoconversor.
Paranãoimplementartodoocódigodaconversão,tiramosproveitoda
classequejáexistenoframework,a DateTimeConverter.
Asimplementaçõesdainterface Convertertêmumpapelmuitoim-
portantenoJSF.Elassãousadastantoparatransformarosvaloresvindosdo
requestparaobjetosdonossomodeloquantoparatransformarosnossosob-
jetosemStringsquedevemserassociadascomosinputsexibidosnaview.
Percebaquefoinecessárioimplementardoismétodos:
•getAsObject–invocadoparatransformarovalorpassadocomopa-
râmetronotipoesperadopelomodelo;
•getAsString–invocadoparatransformarovalordomodelona
Stringquedeveserassociadaaoinputdaview.
5.6 C onverter para entidades
Apesardejátermosadicionadonossasvalidaçõesetratadodaconversãoda
data,aindatemumpontoqueincomodaesteautor.
<div>
<h:selectManyListbox
value="#{adminBooksBean.selectedAuthorsIds}"
converter="javax.faces.Integer">
<f:selectItems value="#{adminBooksBean.authors}"
var="author"
itemLabel= "#{author.name}"
itemValue="#{author.id}" />
</h:selectManyListbox>
</div>
Associamososautoresaumalistadeinteirospara,sódepois,realmente
criarnossalistadeobjetosdotipo Authoreassociaraolivroemquestão.A
seguir,segueocódigoparalembrá-los:
private void populateBookAuthor() {
selectedAuthorsIds.stream().map( (id) -> {
101

## Página 114

5.6. Converterparaentidades CasadoCódigo
return new Author (id));
}).forEach(product :: add);
}
AdicionamosumacomplexidadenonossoManagedBeansóporqueoJSF
nãoquisfazerum Convertermaisinteligente.Agorachegouomomento
deresolvermosissoeficarmosmaisfelizes!
Paratermosumaideiadoquequeremos,vamoscome çaralterandoa
nossapágina.
<div>
<h:outputLabel>Autores</h:outputLabel>
<h:selectManyListbox
value="#{adminBooksBean.product.authors}">
<f:selectItems value="#{adminBooksBean.authors}"
var="author"
itemLabel="#{author.name}" itemValue="#{author}" />
</h:selectManyListbox>
</div>
Aideiaéquesejamoscapazesdeadicionarosautoresselecionadosdireta-
mentenoobjetodotipo Bookquemantemosnaclasse AdminBooksBean.
Pararefletiressaalteração,vamostambémalteraroManagedBean,demodo
quenãoémaisnecessárioficarcriandoosobjetosdotipo Authornamão.
@Model
public class AdminBooksBean {
....
@Transactional
public String save(){
productDAO.save(product);
messagesHelper.addFlash(
new FacesMessage("Livro gravado com sucesso"));
return "/livros/list?faces-redirect=true";
}
102

## Página 115

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
}
Bemmaisdireto! Agora,quandotentamosrodar,recebemosaseguinte
exception:
Caused by: java.lang.IllegalArgumentException:
Can not set java.lang.Integer field
br.com.casadocodigo.loja.models.Author.id to java.lang.Integer
Aexceptionénova,masomotivoéomesmoquenoslevouausaruma
listadeinteirosemvezdetrabalharcomalistadeautores.Porcontadede-
talhesdo generics,nossalistadeautoresdoobjetodotipo Bookacabou
preenchidacomummontedeinteiros.
Casovocêolhetodaa stack,veráqueaexception,naverdade,égerada
quandooHibernatevaipersistiralistaequenãotemnadaavercomoJSF,
pelomenosdiretamente. Paratentarcontornaressasituaç ão,vamoscriar
nosso ConvertergenéricoparaconverterentidadesdaJPA.
package br.com.casadocodigo.loja.converters;
...
import org.picketbox.util.StringUtil;
@FacesConverter
public class EntityConverter implements Converter {
@Override
public Object getAsObject(FacesContext context,
UIComponent component, String value) {
if (StringUtil .isNullOrEmpty(value )) {
return null;
}
UISelectItems uiComponent = (UISelectItems)
component.getChildren()
.get(0);
103

## Página 116

5.6. Converterparaentidades CasadoCódigo
Collection<?> objects = (Collection<?>)
uiComponent .getValue();
Object foundEntity = objects.stream()
.filter((entity) -> {
return getAsString(context, uiComponent,
entity).equals(value);
}).findFirst().get();
return foundEntity;
}
@Override
public String getAsString(FacesContext context,
UIComponent component, Object value) {
Field idField = findIdField(value);
return getIdValue(value, idField);
}
private String getIdValue(Object value, Field idField) {
try {
Field field = value.getClass()
.getDeclaredField(idField.getName());
field.setAccessible(true);
return field.get(value)
.toString();
} catch
(IllegalArgumentException | IllegalAccessException
| NoSuchFieldException | SecurityException e ) {
throw new RuntimeException(e);
}
}
private Field findIdField(Object value) {
Field idField =
Arrays.stream(value.getClass().getDeclaredFields())
.filter((field) -> field.getAnnotation(Id.class)
!= null)
104

## Página 117

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
.findFirst().get();
return idField;
}
}
Respirefundo,essenãoéumcódigotãosimples. Voupedirparanão
olharmuitoparaosmétodosprivados,elesusamumpoucode reflection
eestãoaíapenasparadarumapoio.Vamoscome çarpelomaissimples,que
érelembrandooobjetivo.
Escrevemosesse Converterparaquepossamosadicionardiretamente
osobjetosselecionadosno combodentrodarespectivapropriedade,que
nessecasoéa List<Author>daclasse Book. Comoqueremosfazerum
conversorquepossaseraplicadoparaqualquerentidade,jáimplementamos
umgenérico.
Agora,vamoscome çaraentenderumpoucomaisdocódigo.Come çare-
mospelométodomaisdireto,queéo getAsString.Comojáestudamos
(seção5.5),eleéresponsávelporpegarumobjetoegerarasuarepresentaç ão
emString,paraqueovalorpossaserassociadoauminputdaview.Nonosso
caso,queremospegarqualquerentidadegerenciadapelaJPA,acessaroatri-
butoanotadocom @Iderecuperarseuvalor.Porisso,tivemosdeusarum
poucodaAPIde reflection.
Ocódigofoiquebradoemdoismétodosprivadosjustamenteparaque
vocêpudesseolharumpoucomaise,quemsabe,matarumpoucodacuri-
osidade.A reflectionemsinãoétãoimportante,porissonãovamosgastar
tempoexplicandolinhaporlinha.
Ométodo getAsObjectjárequerumpoucomaisdecuidado,poisele
tiraproveitodoestilo statefuldoJSF.Vamosprestaraten çãonaslinhas
decódigoqueestãologoaseguir:
@Override
public Object getAsObject(FacesContext context,
UIComponent component, String value) {
...
UISelectItems uiComponent = (UISelectItems)
105

## Página 118

5.6. Converterparaentidades CasadoCódigo
component.getChildren().get(0);
Collection<?> objects = (Collection<?>)
uiComponent.getValue();
...
}
Oparâmetrodotipo UIComponentindicaqualfoioelementodaárvore
decomponentesutilizado.Napágina,usamosatag selectManyListBox,
que é representada pela classeHtmlSelectManyListbox. Com essa
informação em mente, também já sabemos que o filho direto desse ele-
mentoéatag selectItems,quepodeserreferenciadapormeiodaclasse
UISelectItems. Éporissoquefazemoso castdoprimeiroelementore-
tornadopelométodo getChildren.Umaimplementaçãomaisprecavida
buscarianalistaretornadaporumobjetodotipo UISelectItems.
O objeto do tipo UISelectItems possui o método chamado
getValue,queretornaparanósalistaassociadaaoelemento.Essecódigo
sóépossíveldeserexecutadoporque,acadanovo postparaosistema,o
JSFremontaaárvoredecomponentesnecessária,paraaplicarosvaloresdos
parâmetros,nospossibilitandoacessaroseuestado.
Agora,vemasegundapartedocódigo.Nela,oJSFvaiinvocarestemé-
todoparacada idselecionadono combo.Pensandonisso,énecessáriodes-
cobrirexatamentequaisobjetosdalistapossuemos idsqueforamescolhidos
nahoradocadastro.
Object foundEntity = objects.stream().filter((entity) -> {
return getAsString(context, uiComponent,
entity).equals(value);
}).findFirst().get();
Oparâmetro valuerepresentaovalorselecionadonatela.Anossaló-
gicasimplesmentevarretodososobjetosdalistaeprocuraporalgumque
possuaarepresentaçãoemStringigualaovalorquefoienviado,jáqueeste
foigeradojustamentepelométodo getAsString.Dessaforma,consegui-
mosretornarasinstânciasdoobjetoemquestão–nonossocaso,o Author
106

## Página 119

CasadoCódigo Capítulo5. Validaçãoeconversãodedados
–,epoupartodoaquelecódigodeconversãoqueestavanonossoManaged
Bean.
Associando o Converter com o componente
Por fim, para que o JSF use o nosso conversor mágico, é necessário
associá-locomocomponentenatela.
<h:selectManyListbox value="#{adminBooksBean.product.authors}"
converter="entityConverter">
...
<h:selectManyListbox
Sóqueaindanãodemosnenhumidentificadorparanosso Converter.
@FacesConverter("entityConverter")
public class EntityListConverter implements Converter {
...
}
Parafecharcomchavedeouro,precisamosapenasfazeraúltimaaltera-
ção.Duranteousodatag selectItems,fizemosreferênciaàpropriedade
iddoobjetodotipo Author.
<f:selectItems value="#{authorsList.get()}" var="author"
itemLabel= "#{author.name}" itemValue="#{author.id}" />
Sóqueagoraestamosusandoumconverterquesemprepegao iddas
entidadesdaJPA.Damaneiracomoestá,nosso Convertervaiprocurar
porumatributoanotadocom @Idnaclasse Integer,enãona Author.
Vamospromoveressaalteração.
<f:selectItems value="#{authorsList.get()}" var="author"
itemLabel= "#{author.name}" itemValue="#{author}" />
5.7 C onclusão
Estefoiumcapítuloumpoucomaisdenso.Lidamoscomosproblemasdeva-
lidaçãoeconversão,típicosdodiaadia.Aparteinteressanteéquepassamos
porváriosdetalhesdoJSFedaBeanValidation.
107

## Página 120

5.7. Conclusão CasadoCódigo
Umadicaquepossodaré:sempretentebuscaroquejávemprontodentro
doframework,massaibaosuficientedeleparaconseguiriralém,quando
necessário. Fizemosissoemalgumassituaçõesevaleubastanteapena. O
Converterpara Calendareodalistapodemserusadosemqualquerprojeto
quevocêvenhaaparticipar.
Achoqueesseéumbommomentoparavocêpararerefletirsobretudo
quefoiestudadoatéaqui.JátrabalhamoscomaJPA,CDI,JTAebastantecom
oJSF.AindatemmaisdeJSFedeoutrasespecificaçõesporvir. Descansee
voltecomtodafor çaparacontinuaraleitura.
108

## Página 121

Capítulo6
Uploaddearquivos
Umacaracterísticaimportantedaslivrariasonlineéadisponibilizaçãodosu-
máriodoslivrosqueestãoàvenda. ACasadoCódigo,comonãopoderia
deixardeser,tambémdeveofereceressapossibilidadeaseususuários.
6.1 R ecebendo o arquivo no Managed Bean
VamoscomeçaralterandoapáginadaCasadoCódigoresponsávelpelaen-
tradadedadosdecadaumdosnovoslivros.
<h:form>
...
<div>
<h:outputLabel value="Capa do livro"/>

## Página 122

6.1. RecebendooarquivonoManagedBean CasadoCódigo
<h:inputFile id="summary" label="Sumário do livro"/>
</div>
Aúnicamudan çafoiaadiçãodoinputquevaireceberoarquivoque,
nestecaso,deveserdotipo file.Agora,setentarmosenviarosdadosdesse
formulário,devemosreceberaseguinteexception:
javax.servlet.ServletException: UT010016:
Not a multi part request
Not a multi part request significa que tentamos enviar o ar-
quivo de uma forma que o JSF não consegue entender. Basicamente, o
que acontece é que todos os dados do formulário são enviados de al-
gumamaneira,eopadrãoéqueelessejamsubmetidosusandooformato
application/x-www-form- urlencoded. Dessaforma,osdadossão
enviadosseguindoquaseasmesmasregrasusadasquandoutilizamosomé-
todo GET.Umasequênciadechavesevalores.
Anossasituaçãoatualexigequefaç amosumaalteraçãonesseformato,
demodoqueoarquivopossaserintegralmentepassadodonavegadorparao
servidor.Éporissoquevamosutilizaroformato multipart/form-data.
<h:form enctype="multipart/form-data">
...
<div>
<h:outputLabel value="Capa do livro"/>
<h:inputFile id="summary" label="Sumário do livro"/>
</div>
Oatributo enctypeservejustamenteparaindicarmoscomoqueremos
mandarosdadosdonavegadorparaoservidor,eo multipart/form-data
éojeitoutilizadoquandoprecisamostransmitirarquivos. Porexemplo,já
existeumtrabalhosendofeitoparaqueoseu formpossaenviarosdados
peloformatoJSON.Casofiquecurioso,navegueaté http://www.w3.org/TR/
html-json-forms/.
110

## Página 123

CasadoCódigo Capítulo6. Uploaddearquivos
Alterando o método do Managed Bean
Agoraquenossoformuláriojáenviaoarquivo,precisamosrecebê-loeli-
darcomele.Faremosissonométodo savedaclasse AdminBooksBean.O
primeiropasso,naverdade,éfazero bindingentreo inputFileealguma
propriedadedonossobean. Oleitormaisatentodeviaatéestarsepergun-
tandoqualeraomotivodenãotermosfeitoissoantes.
<div>
<h:outputLabel value="Sumário do livro"/>
<h:inputFile id="summary" value="#{adminBooksBean.summary}"
label="Sumário do livro"/>
</div>
Aqui,assumimosqueobeanvaiterumapropriedadechamada summary.
Éjustamentenelaquevamosguardaroarquivoquetiversidoenviadopelo
formulário.
@Model
public class AdminBooksBean {
...
private Part summary;
public void setSummary(Part summary) {
this.cover = cover ;
}
public Part getSummary() {
return cover;
}
@Transactional
public String save(){
System.out.println(summary.getName() + ";"
+summary.getHeader("content-disposition"));
...
}
}
111

## Página 124

6.1. RecebendooarquivonoManagedBean CasadoCódigo
Aparteimportantedessecódigoéoatributodotipo Part. Elefoiin-
troduzidoapartirdaversão3daespecificaç ãodeServlets,eéainterfaceres-
ponsávelporrepresentaroarquivoquefoienviadopeloformulário.
Percebaqueonomedoargumentoéomesmonomedoinputquedecla-
ramosnoformulário.Aquiusamosdoismétodos:
•getName()–retornaonomedoinputusadonoformulário;
•getHeader()–usadopararecuperaralgumainformaçãosobreoque
foienviado.
Casonósquiséssemosrecuperaronomedoarquivo,comofaríamos?O
leitormaisexperientedeveestarpensandoquetemalgummétodoquejáre-
tornaissopronto,masesseéjustamenteoproblema.
Ainterface Partéamaneiramaisprimitivadetratarmososdadosenvi-
adospormeiodo enctype multipart/form-data.Paraficarumpouco
maisclaro,dêumaolhadanamaneiracomoessesdadossãoenviadosapartir
donavegador.
112

## Página 125

CasadoCódigo Capítulo6. Uploaddearquivos
Fig.6.1:Corpodorequestparaumarequisiç ãomultipart
Paraoscamposquenãorepresentamarquivos,oJSFjánosajudabastante
efazaligaçãodiretacomaspropriedadesdonossomodelo.Paraoarquivo
enviado,vamosterdefazeroparseerecuperaronomedele,infelizmente.O
nossocódigovaificarparecidocom:
@Transactional
public String save(){
System.out.println(extractFilename
(summary.getHeader("content-disposition"));
}
113

## Página 126

6.2. Salvandoocaminhodoarquivo CasadoCódigo
private String extractFilename(String contentDisposition) {
if (contentDisposition == null) {
return null;
}
String fileNameKey = "filename=";
int startIndex = contentDisposition.indexOf(fileNameKey);
if (startIndex == -1) {
return null;
}
String filename = contentDisposition.substring(startIndex
+ fileNameKey.length());
if (filename.startsWith("\"")) {
int endIndex = filename.indexOf("\"", 1);
if (endIndex != -1) {
return filename.substring(1, endIndex);
}
} else {
int endIndex = filename.indexOf(";");
if (endIndex != -1) {
return filename.substring(0, endIndex);
}
}
return filename;
}
EsteéjustamenteotipodecódigoquedevemosevitarternonossoMa-
nagedBean.Casoumapessoanovachegueaoseuprojeto,elavaiperdermais
tempotentandoentenderissodoqueprestandoaten çãonofluxodoprojeto
emsi,queéomaisimportante.Umpoucomaisàfrente,vamosusaroCDI
paranosajudaradeixaressecódigomaiscoeso.
6.2 S alv ando o caminho do arquivo
Agoraquejátemosoobjetoquerepresentaoarquivoenviadoemnossas
mãos,énecessáriogravá-loemalgumlugar.Vamosaproveitartambémejá
isolaressecódigoderecuperaronomedoarquivoesalvá-lo.
114

## Página 127

CasadoCódigo Capítulo6. Uploaddearquivos
@Model
public class AdminBooksBean {
...
private Part summary;
@Inject
private FileSaver fileSaver;
@Transactional
public String save(){
String summaryPath =
fileSaver.write("summaries", summary);
...
}
}
package br.com.casadocodigo.loja.infra;
@RequestScoped
public class FileSaver {
@Inject
private HttpServletRequest request;
private static final String CONTENT_DISPOSITION =
"content-disposition";
private static final String FILENAME_KEY = "filename=";
public String write(String baseFolder, Part multipartFile) {
String serverPath = request.getServletContext()
.getRealPath("/" + baseFolder);
String fileName = extractFilename(multipartFile
.getHeader( CONTENT_DISPOSITION));
String path = serverPath + "/" + fileName;
try {
multipartFile.write(path);
115

## Página 128

6.2. Salvandoocaminhodoarquivo CasadoCódigo
} catch (IOException e) {
throw new RuntimeException(e);
}
return baseFolder + "/" + fileName;
}
private String extractFilename(String contentDisposition) {
if (contentDisposition == null) {
return null;
}
int startIndex = contentDisposition
.indexOf(FILENAME_KEY);
if (startIndex == -1) {
return null;
}
String filename = contentDisposition
.substring( startIndex
+ FILENAME_KEY.length());
if (filename.startsWith("\"")) {
int endIndex = filename.indexOf("\"", 1);
if (endIndex != -1) {
return filename.substring(1, endIndex );
}
} else {
int endIndex = filename.indexOf(";");
if (endIndex != -1) {
return filename.substring(0, endIndex );
}
}
return filename;
}
}
Dêumarespiradaeolhecomcuidadoparaocódigo. Percebaquenão
fizemosnadademais,apenascriamosoutraclasseresponsávelporgravaro
arquivoemumapastadanossaaplicação.Aideiaénãodeixarqueessecódigo
atrapalheofluxodométodo savenonossoManagedBean.Alémdisso,é
necessáriocriaroatributo summaryPathnaclasse Book,juntamentecom
116

## Página 129

CasadoCódigo Capítulo6. Uploaddearquivos
oseugetteresetter.
Dessaforma,casosejanecessáriocriarumlinkparaosumário,bastaque
façamosalgoparecidocomoquesegue:
<a href="${book.summaryPath}">Sumário do livro</a>
Podemosinclusiveacrescentaresselinknalistagematualdoslivros.
...
<h:column>
<f:facet name="header">Sumário</f:facet>
<h:outputLink value="#{request.contextPath}
/#{book.summaryPath}">
#{book.summaryPath}
</h:outputLink>
</h:column>
6.3 G rav ando os arquivos fora do servidor
web
Nossalógicadeuploadgravaosnovosarquivosemumapastadentrodapró-
priaaplicaçãoweb. Oproblemadessaabordagem,mesmoquandoestamos
emambientededesenvolvimento,éque,acadanovaalteraç ãoquetemosno
projeto,anossaIDEfor çaum hot deploynoservidor.Emgeral,o hot deploy
destróiaaplicaçãoqueestavanoservidorecriaumanova,fazendocomque
percamososarquivosquejátinhamsidoenviados.
Alémdisso,umfatoqueincomodaodesenvolvedoréperceberqueos
arquivosenviadosnãoficamexatamentedentrodoprojetoqueeleestávisu-
alizando–porexemplo,noEclipse–,masnainstalaçãodoservidorquefoi
escolhida.Parasimplificartudoisso,facilitandoinclusiveoprocessodede-
ployquediscutiremosmaisparaofimdolivro(capítulo 16),équepodemos
usarumserviçocomoo Amazon S3.
Basicamente,aAmazonforneceumserviçoondepodemosenviarnos-
sosarquivos,eestesficamdisponíveisparaseremacessadospelaweb. Eles
possuemservidoresdedicadossóparaisso.
117

## Página 130

6.3. Gravandoosarquivosforadoservidorweb CasadoCódigo
Integração com o Amazon S3
Paraquemestiverinteressadonessaop ção,aprimeiracoisaquedevemos
fazeréalterarocódigoqueestánaclasse FileSaver,queéaresponsável
porgravaroarquivo.
public class FileSaver {
...
public String write(String baseFolder,
Part multipartFile) {
AmazonS3Client s3 = client();
String fileName = extractFilename(multipartFile
.getHeader( CONTENT_DISPOSITION ));
try {
s3.putObject("casadocodigo", fileName,
multipartFile.getInputStream(),
new ObjectMetadata());
return "https://s3.amazonaws.com/casadocodigo/"
+fileName;
} catch (AmazonClientException | IOException e) {
throw new RuntimeException(e);
}
}
private AmazonS3Client client() {
AWSCredentials credentials = new BasicAWSCredentials(
,
);
AmazonS3Client newClient =
new AmazonS3Client(credentials,
new ClientConfiguration());
newClient.setS3ClientOptions(new S3ClientOptions()
.withPathStyleAccess(true));
return newClient;
118

## Página 131

CasadoCódigo Capítulo6. Uploaddearquivos
}
...
}
Percebaquetemosmaiscódigosrelativosàintegraç ãocomaAmazondo
querelacionadoaoCDIouoJSFemsi. Detudooquefoiescritoanterior-
mente,aslinhasmaisimportantessãoasqueestãologoaseguir:
AmazonS3Client s3 = client();
...
s3.putObject("casadocodigo", fileName,
multipartFile.getInputStream(),
new ObjectMetadata());
Oobjetodotipo AmazonS3Clientencapsulatodoalógicaeoproto-
colodecomunicaçãocomaAmazon. Onossoúnicotrabalhoépassaros
parâmetros.
• Oprimeiroéapastaremotaondeoarquivovaisersalvo,tambémco-
nhecidacomo bucket;
• Osegundoéonomedoarquivo;
• Oterceiroéalgumaimplementaçãodaclasse InputStream,quere-
almenterepresentaoarquivo;
• Oquartosãoinformaçõesextrascomo:datadeexpiraçãodoarquivoe
qualqueroutrainformaçãoquesejaespecíficadaaplicação.
Aoutrapartedocódigoéamesmaparaqualquerintegraç ãoquevocêvá
fazercomaAmazon.Sempreprecisamoscriarumobjetoquecontémascre-
denciaisdeacesso,paragarantirquesóodonodacontapossafazeruploads
paraobucket.
119

## Página 132

6.3. Gravandoosarquivosforadoservidorweb CasadoCódigo
private AmazonS3Client client() {
AWSCredentials credentials = new BasicAWSCredentials(
,
);
AmazonS3Client newClient = new AmazonS3Client(credentials,
new ClientConfiguration());
newClient.setS3ClientOptions(new S3ClientOptions()
.withPathStyleAccess(true));
return newClient;
}
Basicamente,estasseriamasalteraçõesqueteríamosdefazernonosso
código. Comodeixamosencapsuladaalógicadegravaç ãodoarquivo,não
somosobrigadosaalterarnenhumalinhadonosso Controller.
Simulando o S3 localmente
Oempecilhocomasoluç ãoapresentadaéquevamosterderealmente
criarumcontanaAmazonparaconseguirrealizarnossostestes,oqueécom-
pletamenteinviável.Pararesolveresteproblema,existeumprojetochamado
S3 Ninja,quepodeserencontradoem http://s3ninja.net/.
ElefoicriadocomoobjetivodeservircomoumemuladorparaoS3real,
daAmazon.OS3NinjaéumaaplicaçãowebescritaemJavaquesobeumser-
vidorqueaceitarequisiçõesvindasdopróprioSDKdaAmazon.Justamente
oqueestávamosprocurando. Umapartemuitoboaéqueoseuusoébem
simples.
O primeiro passo é realizar o download do.zip, bastando aces-
saroendereçohttps://oss.sonatype.org/content/groups/public/com/scireum/
s3ninja/2.3/s3ninja-2.3-zip.zip.
Vocêtambémpodeencontrarolinkno readmedoGitHubdoprojeto,
emhttps://github.com/asouza/casadocodigojavaee.
Umavezquevocêbaixouoprojeto,descompacte-oemumapastadesua
preferência.Aindadentrodapastadescompactada,precisamoscriarumes-
truturasimplesdesubpastasquevãosimularos bucketsdaAmazon.Vamos
criarprimeiroapasta datae,dentrodela,criaremosoutrapasta,chamada
s3.Aestruturafinalvaificarparecidacomamostradanafiguraaseguir:
120

## Página 133

CasadoCódigo Capítulo6. Uploaddearquivos
Fig.6.2:EstruturadepastasdoS3Ninja
Agoraqueaestruturaestácriada,bastainiciarmososervidordoS3Ninja.
java IPL
Percebaque IPLéjustamenteumarquivoJavacompiladoquejávemna
raizdodiretóriodescompactado.Apósexecutarocomando,vocêdevevera
seguintesaída:
I N I T I A L P R O G R A M L O A D
---------------------------------------
IPL from: /Users/alberto/ambiente/servidores/s3ninja-2.3-zip
IPL completed - Loading Sirius as stage2...
Opening port 9191 as shutdown listener
Oservidorestárodandonoendere çohttp://localhost:9444/.Vocêpode
acessá-lopelonavegador.
Fig.6.3:Teladeboas-vindasdoS3Ninja
121

## Página 134

6.3. Gravandoosarquivosforadoservidorweb CasadoCódigo
Agoraqueonossoemuladorestárodando,precisamosalterarocódigo
deconfiguraçãodeacessoàAmazonefazê-loapontarparaoservidorlocal.
private AmazonS3Client client() {
AWSCredentials credentials = new BasicAWSCredentials(
,
);
AmazonS3Client newClient = new AmazonS3Client(credentials,
new ClientConfiguration());
newClient.setS3ClientOptions(new S3ClientOptions()
.withPathStyleAccess(true));
//nova linha
newClient.setEndpoint("http://localhost:9444/s3");
return newClient;
}
Pronto!Quandocadastrarmosumnovolivro,oarquivodosumáriovai
sergravadonapasta data/s3/casadocodigo/nomedoarquivo,nolocal
quevocêescolheuparaexecutaroS3Ninja.Percebaquetambémalteramos
oretornodométodo write,daclasse FileSaver.
public String write(String baseFolder, Part multipartFile) {
AmazonS3Client s3 = client();
String fileName = extractFilename(multipartFile
.getHeader(CONTENT_DISPOSITION));
try {
s3.putObject("casadocodigo", fileName,
multipartFile.getInputStream(),
new ObjectMetadata());
//url de acesso ao arquivo
return "https://s3.amazonaws.com/casadocodigo/"
+fileName+"?noAuth=true";
} catch (AmazonClientException | IOException e) {
throw new RuntimeException(e);
}
122

## Página 135

CasadoCódigo Capítulo6. Uploaddearquivos
}
Aideiaéquenossométodojáretorneoendere çodeacessoaoarquivo
enviado,paraquepossamosusá-lonoslinksdonossosistema.
Isolando a criação do AmazonS3Client
Anossaalteraçãonoslevouadeixarocódigodecriaç ãodoobjetode
acessoàAmazonmisturadocomocódigodaclasse FileSaver.Comojá
temsidoanossaprática,quando,porexemplo,recebemosinjetadoo DAO,o
nossoobjetivonessecódigoéusaroclientedaAmazon,enãoficarcriando.
Então,vamoscome çarrecebendoumobjetodotipo AmazonS3Clientem
vezdecriá-lo.
public class FileSaver {
@Autowired
private AmazonS3Client s3;
public String write(String baseFolder,
MultipartFile multipartFile) {
String fileName = extractFilename(multipartFile
.getHeader(CONTENT_DISPOSITION));
try {
s3.putObject("casadocodigo",fileName,
multipartFile.getInputStream(),
new ObjectMetadata());
return "http://localhost:9444/s3/casadocodigo/"
+fileName+ "?noAuth=true";
} catch (AmazonClientException | IOException e) {
throw new RuntimeException(e);
}
}
}
123

## Página 136

6.3. Gravandoosarquivosforadoservidorweb CasadoCódigo
Paraestecódigofuncionar,assimcomofizemosquandofoinecessário
injetaroobjetodotipo FacesContext,precisamoscriarummétodopara
criarumobjetodotipo AmazonS3Client.
package br.com.casadocodigo.loja.infra;
import javax.enterprise.inject.Produces;
import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.S3ClientOptions;
public class AmazonS3ClientProducer {
@Produces
public AmazonS3Client s3Ninja() {
AWSCredentials credentials = new BasicAWSCredentials(
,
);
AmazonS3Client newClient =
new AmazonS3Client(credentials,
new ClientConfiguration());
newClient.setS3ClientOptions(new S3ClientOptions()
.withPathStyleAccess(true));
newClient.setEndpoint("http://localhost:9444/s3");
return newClient;
}
}
Umdetalheinteressanteéqueessenossométodoprodutornãodeveter
nenhumaanotaçãodeescopo.Oproblemaéqueaclasse AmazonS3Client
possuimétodosmarcadoscomo final,eaespecificaçãodoCDIexigeque
todososcomportamentosdaclassee,inclusiveaclasse,nãoestejammarca-
doscomo final,parasuportarainje çãodeobjetosbaseadosemescopos
diferentesdo Dependent.
124

## Página 137

CasadoCódigo Capítulo6. Uploaddearquivos
Agoravocêtemduasop çõesparasalvarosarquivosenviadospelosseus
usuários. Esteautorsugerequevocêsempreguardeoarquivoemumlocal
foradoservidorweb.Acomplexidadeadicionadaaoprojetoécompensada
pelaflexibilidadedemanterosarquivosentre reloadsdaaplicação,emtempo
dedesenvolvimento.
Alémdisso,ainstalaçãonoambientedeproduçãovaiserfacilitada,jáque
vocênãovaiterdesepreocuparemmanterosarquivosquejátenhamsido
enviadospelosusuários.Tudovaiestaremumlugarseparado.
Umdetalhesimples,masmuitoimportante: lembre-se sempre de subir
o servidor do S3 Ninja antes de rodar sua aplicação!
6.4 C onclusão
Nestecapítulo,focamosunicamentenouploaddearquivos.Essaéumafun-
cionalidademuitocomumnasaplicações,masmuitasvezesesquecemosde
olharcomdetalhesparaentenderexatamentecomofunciona.Ointeressante
équetudofoimuitodireto,nãotivemosqueperdertempocomnenhuma
configuraçãoextra.Basicamente,usamostudooquejáestavaprontonasúl-
timasversõesdasespecificaçõesdoJSFedeServlets.
Nãopareagora,jáváparaopróximocapítulonoqualvamosrealizarofe-
chamentodeumacompra.VamosimplementarumCarrinho,verumpouco
maisdosescoposdoCDIedeixaroterrenopreparadopararealizarmosuma
integraçãocomoutrosistema.
125

## Página 139

Capítulo7
Carrinhodecompras
JátemosocadastrodelivroseasualistagemnalojadaCasadoCódigo,en-
tãochegouomomentodeimplementarmosoprocessodecompra.Paraco-
meçarmosessafase,precisamos,primeiramente,possibilitarqueosusuários
escolhamoslivrosquemaislhesinteressameoscoloquememumcarrinho
decompras.
7 .1 E xibindo os livros na página inicial
NaCasadoCódigo,osvisitantesconseguemnavegarparaaspáginasdede-
talhesdoslivrosapartirdalistagemexibidanapáginainicialdosite.

## Página 140

7.1. Exibindooslivrosnapáginainicial CasadoCódigo
Fig.7.1:Listagensdahome
Percebaquetemosduaslistagens: umacomosúltimoslan çamentose
outraqueexibeosúltimoslivroscompre çospromocionais.Nossoprimeiro
desafioéjustamentereproduziressapágina.
Aqui,paraficarclaroquerealmenteestamosreproduzindoositedaCasa
doCódigo,seráusadoomesmoHTMLconstruídoporeles.Comoocódigo
dapáginaérelativamentegrande,paraverapáginacompleta,oleitorpode
navegaratéolink https://github.com/asouza/casadocodigojavaee/blob/master/
src/main/webapp/site/index.xhtml.
Notre
choaseguir,vejaalgumaspartesimportantes.Apenasparafinsde
organização,estadevesercriadaemumanovapastachamada site,como
nomede index.xhtml.
<ui:repeat var= "book" value=
"#{homeBean.lastReleases()}">
<li class="col-left"
><a href="/products/livro-plsql"
class="block clearfix"
> <img width="170" height="240"
src="#{book.coverPath}"
alt=" #{book.title}" title="#{book.title}"/>
<h2 class="product-title">#{book.title}
</h2> <small
class="buy-button">Lan&#231;amento!</small></a>
</li>
</ui:repeat>
128

## Página 141

CasadoCódigo Capítulo7. Carrinhodecompras
...
<ui:repeat var="book" value="#{homeBean.olderBooks()}">
<li><a href="/products/livro-laravel-php"
class="block clearfix">
<h2 class="product-title">#{book.title}</h2>
<img width="143" height="202"
src="#{book.coverPath}"
alt="#{book.title}"
title="#{book.title}"/><small
class="buy-button">Compre</small>
</a></li>
</ui:repeat>
ApáginabasicamenteéumHTML,eusamosatag repeatparaim-
primiroslivrosretornadospelosmétodosemquestão. Paraconcentraras
lógicasrelativasànossahome,foicriadaaclasse HomeBean.
package br.com.casadocodigo.loja.managedbeans.site;
//imports
@Model
public class HomeBean {
@Inject
private BookDAO bookDao;
public List<Book> lastReleases(){
return bookDao .lastReleases();
}
public List<Book> olderBooks(){
return bookDao .olderBooks();
}
}
Umasimplesclasseanotadacom @Model,nadaquevocêjánãotenha
129

## Página 142

7.1. Exibindooslivrosnapáginainicial CasadoCódigo
visto. Paraonossocódigoficarcompletamentefuncional,precisamostam-
bémadicionarosnovosmétodosnaclasse BookDAO.
package br.com.casadocodigo.loja.daos;
//imports
public class BookDAO {
@PersistenceContext
private EntityManager manager;
...
public List<Book> lastReleases() {
return manager.createQuery("select b from Book b where
b.releaseDate <= now() order by
b.id desc",Book.class)
.setMaxResults(3).getResultList();
}
public List<Book> olderBooks() {
return manager.createQuery("select b from
Book b",Book.class)
.setMaxResults(20).getResultList();
}
}
Aqui,usamosumpoucomaisdaJPAparaconseguirfazernossasque-
ries.UmdetalhemuitoimportantequandoestamostrabalhandocomaJPA
é:pensenasuasconsultascomoseestivesserealmentetrabalhandocomos
objetos!
ClaroqueéimportanteconhecerSQL,masquandovocêaceitatrabalhar
comumaferramentadeMapeamentoObjeto-Relacional(ORM),éinteres-
santequeamaioriadassuasqueriesconsigamtirarproveitodasvantagens
oferecidaspelaJPQL.
130

## Página 143

CasadoCódigo Capítulo7. Carrinhodecompras
Pronto,comissojáconseguimosexibirtodososnossoslivroscadastra-
dos.Umdetalheimportanteparaessapáginafuncionarbeméquetodosos
produtoscadastradosestejamcomumaimagemassociada.Parafacilitar,sim-
plesmenterodeumcomandoSQLqueatualizetodasascapasparaalguma
imagempreviamentecadastrada.Vejaumexemplo:
update Book set coverPath =
'http://localhost:9444/s3/casadocodigo/
covers_games-android-featured_medium.png?noAuth=true';
Umoutropontoimportanteéque,casovocêtenhaoptadoporusaroS3
Ninja,seuservidordeveestarrodando. Então,lembre-sedeirnapastade
instalaçãoerodaroseguintecomando:
java IPL
Pronto,játemosumapáginainicialigualadaCasadoCódigo!Emelhor
ainda,nãofoinecessáriousarnadadenovo,trabalhamosapenascomoque
jáestudamoseconseguimosreproduzirumaaplicaçãobastanteconhecidano
mercado.
7 .2 N avegando para o detalhe do produto
Agoraquejátemosalistagemdoslivros,énecessárioqueosusuáriosdaapli-
caçãoconsigamnavegarparaapáginadedetalhesdolivro. Énessaoutra
páginaqueelevaiencontrarinformaçõescomo:pre ço,autoreseresumodo
conteúdodaobra.Percebaque,atualmente,olinkparaosdetalhesestáfixo
emnossalistagem.
<ui:repeat var="book" value="#{homeBean.lastReleases()}">
<li class="col-left"><a href="/products/livro-plsql"
...
</li>
</ui:repeat>
...
<ui:repeat var="book" value="#{homeBean.olderBooks()}">
131

## Página 144

7.2. Navegandoparaodetalhedoproduto CasadoCódigo
<li><a href="/products/livro-laravel-php" ...>
...
</a></li>
</ui:repeat>
O hrefestásempreapontandoparaumaURLfixa,eprecisamosdeixar
issodinâmico.Essaéumapartetranquiladeresolver.Vamosdarumaolhada:
<ui:repeat var= "book" value="#{homeBean.lastReleases()}">
<li class="col-left"><a
href="#{request.contextPath}/site/
detalhe.xhtml?id=#{book.id}"
...
</li>
</ui:repeat>
...
<ui:repeat var= "book" value="#{homeBean.olderBooks()}">
<li><a
href="#{request.contextPath}/site/
detalhe.xhtml?id=#{book.id}"
...>
...
</a></li>
</ui:repeat>
Simplesmenteapontamosagoraparaoendere çodetalhe.xhtml,res-
ponsávelporexibirosdetalhesdolivro.Temostambémdepassaroparâme-
troindicandoqualo iddolivroqueestamosbuscando. Assim,usamoso
request.contextPathparasempregarantirqueestamosreferenciandoa
raizdocontextodanossaaplicação.
Agoraénecessárioquetenhamosessapágina,paraqueessenossolink
funcione.Maisumavez,vamosusarolayoutoriginaldaCasadoCódigoe,
comooHTMLémuitogrande,vamosapenasdeixarostrechosimportan-
tesaquinolivro. Oconteúdointeiropodeserencontradoem https://github.com/
 asouza/casadocodigojavaee/blob/master/src/main/webapp/site/detalhe.xhtml.
Essap
áginadevesercriadacomonomede detalhe.xhtml,edeve
ficarna
pasta site.
132

## Página 145

CasadoCódigo Capítulo7. Carrinhodecompras
<html xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://xmlns.jcp.org/jsf/core"
xmlns="http://www.w3.org/1999/xhtml"
xmlns:pt="http://xmlns.jcp.org/jsf/passthrough">
<head>
...
<title>#{productDetailBean.book.title}</title>
...
</head>
...
<header>
<div id="product-overview" class="container">
<img width="280px" height="395px"
src="#{productDetailBean.book.coverPath}"
class="product-featured-image"
alt="#{productDetailtBean.book.description}"/>
<h1 class="product-title">
#{productDetailBean.book.title}
</h1>
<p class="product-author">
<span class="product-author-link">
<ui:repeat var="author"
value="#{productDetailBean.book.authors}">
#{author.name}|
</ui:repeat>
</span>
</p>
<p class="book-description">
#{productDetailBean.book.description}
</p>
133

## Página 146

7.2. Navegandoparaodetalhedoproduto CasadoCódigo
</div>
</header>
...
<section class="author product-detail">
<h2 class="section-title">
<ui:repeat var="author"
value="#{productDetailBean.book.authors}">
#{author.name}|
</ui:repeat>
</h2>
<span>
<p class="book-description"><img class="author-image"
src="" alt="" style="float: left; margin-right: 10px; "/>
<a>Descricao sobre os autores</a>.</p>
</span>
</section>
<section class= "data product-detail">
<h2 class="section-title">Dados do livro:</h2>
<p>Número de páginas:
<span>
#{productDetailBean.book.numberOfPages}
</span></p>
<p></p>
<p>
Data de publicação:
#{productDetailBean.book.releaseDate.time}
</p>
Denovo,pelomenosatéagora,éumapáginaapenascomcódigosquejá
estudamos.Paralidarcomaresponsabilidadedecarregaroproduto,criamos
134

## Página 147

CasadoCódigo Capítulo7. Carrinhodecompras
umnovobean,chamado ProductDetailBean.
package br.com.casadocodigo.loja.managedbeans.site;
//imports
@Model
public class ProductDetailBean {
@Inject
private BookDAO bookDAO;
private Book book ;
@PostConstruct
public void loadBook(){
this.book = bookDAO.findById(id);
}
public Book getBook() {
return book;
}
}
Recebendo parâmetros e executando ações em requisições via GET
Oleitormaisatentodeveestarseperguntandodeondeveioo idqueestá
sendousadoparacarregaroproduto,eesseéumótimoquestionamento!A
requisiçãoquecheganapáginadedetalhevemapartirdeum GET,sendo
que,atéomomento,qualquermétododosnossosbeanssófoiinvocadoa
partirderequisiçõesvia POST.
Hámuitotempoatrás,aindanaprimeiraversãodoJSF,issoseriaumpro-
blemaparanós.Seríamosobrigadosafazerum POSTapenasparasatisfazero
frameworke,comisso,anavegabilidadedonossositeestariacomprometida.
Porexemplo,todososlinksquesãoacessadosvia POSTnãosãoindexados
peloGoogle,oqueseriaextremamenteprejudicialparaaCasadoCódigo.
Percebendoqueissoeraumproblema,aversão2.0doJSFtrouxeosu-
porteparaorecebimentodeparâmetrosqueviessemapartirdeumnovo
request. Assim,foicriadaa taglib viewParam,queficanopacote core,
135

## Página 148

7.2. Navegandoparaodetalhedoproduto CasadoCódigo
bastandousá-ladentrodeumaoutra,chamada metadata.
Vamosalterarnossapáginadedetalhe:
<html xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://xmlns.jcp.org/jsf/core"
xmlns="http://www.w3.org/1999/xhtml"
xmlns:pt="http://xmlns.jcp.org/jsf/passthrough">
<f:metadata>
<f:viewParam id="id" name="id"
value="#{productDetailBean.id}"/>
</f:metadata>
...
Podemosrecebero ideassociá-locomnossobean,pormeiodosméto-
dosdeacesso.
package br.com.casadocodigo.loja.managedbeans.site;
//imports
@Model
public class ProductDetailBean {
@Inject
private BookDAO bookDAO;
private Book book ;
private Integer id;
public void setId(Integer id){
this.id = id;
}
public Integer getId() {
return id;
}
@PostConstruct
136

## Página 149

CasadoCódigo Capítulo7. Carrinhodecompras
public void loadBook(){
this.book = bookDAO.findById(id);
}
public Book getBook() {
return book;
}
}
Casotentemosrodarestecódigo,aindareceberemosumaexception. O
problemaéqueo bindingdoparâmetrocomseu beansóacontecenafase
UPDATE_MODEL_VALUESdociclodevidadoJSF.Esteéomomentoqueo
JSFvaisetarosvaloresnoseubean;enquantoqueainvocaç ãodométodo
anotadocom @PostConstruct,nessecaso,aconteceumafaseantes,na
PROCESS_VALIDATIONS.
Omomentoqueo beanéinstanciadovaidependerdoseuusodentro
dapágina.Porexemplo,nahome,elesóéinstanciadonomomentoqueoJSF
vaiescreveroHTMLparaonavegador,jáquesóousamosparaconsumir
informações.Jánapáginadedetalhes,precisamossetaro idpassadocomo
argumento,assim,eleseráinstanciadonafasedevalidaçãoparaquequalquer
verificaçãoouconversãonecessáriasejarealizada.
ÉimportantesemprelembrardasfasesdoJSF,conhecerumpoucode
cadaumadelaspodepouparbastanteumadordecabe çanahoradedesven-
darbugsnaaplicação.
Umamaneirasimplesderesolveresteproblemaseriatirarocódigodo
métodoanotadocom @PostConstruct, ecolocá-lodentrodométodo
setId. Só que, a partir do JSF 2.2, foi criada uma nova tag, chamada
viewAction. Oobjetivoéqueelasejausadaempáginasdeumsistema
escritoemJSFqueforamacessadasvia GET.
<f:metadata>
<f:viewParam id="id" name="id"
value="#{productDetailBean.id}"/>
<f:viewAction action="#{productDetailBean.loadBook()}"/>
</f:metadata>
137

## Página 150

7.2. Navegandoparaodetalhedoproduto CasadoCódigo
Porpadrão,a viewActionpermitequeinvoquemosalgummétododo
nosso beannafase INVOKE_APPLICATION,justamenteausadapeloJSF
parainvocarnossaslógicas. Comisso,garantimosqueocarregamentodo
livrosóseráfeitoquandoo idjátiversidosetado.
Vejacomoocódigofinaldaclasse ProductDetailBeandeveficar:
package br.com.casadocodigo.loja.managedbeans.site;
//import
@Model
public class ProductDetailBean {
@Inject
private BookDAO bookDAO;
private Book book = new Book ();
private Integer id;
public void setId(Integer id) {
this.id = id;
}
public Integer getId() {
return id;
}
public void loadBook() {
this.book = bookDAO.findById(id);
}
public Book getBook() {
return book;
}
}
Parafechar, precisamossóadicionarométodo findByIdnaclasse
BookDAO.
package br.com.casadocodigo.loja.daos;
138

## Página 151

CasadoCódigo Capítulo7. Carrinhodecompras
//import
public class BookDAO {
@PersistenceContext
private EntityManager manager;
...
public Book findById(Integer id) {
return manager.find(Book.class, id);
}
}
7 .3 L idando com LazyInitializationException
Casooleitortenhaacessadoapáginadedetalhedolivro,vaiperceberque
umaexceptionfoilan çada.
javax.servlet.ServletException: failed to lazily initialize a
collection of role: br.com.casadocodigo.loja.models.Book.authors,
could not initialize proxy - no Session
O problema acontece exatamente na linha a seguir, da página
detalhe.xhtml:
<ui:repeat var="author"
value="#{productDetailBean.book.authors}">
Denovotemosumproblemarelacionadoaociclodevida,sóqueagorado
EntityManager.Ométodo getAuthorsdaclasse Bookusaumatributo
mapeadocomaannotation @ManyToMany.Pordefault,aimplementaçãoda
JPAvaitentarcarregaressacole çãoapenasnomomentodoseuusoefetivo.
Paraqueissoaconte ça,énecessárioqueum SQLsejadisparadonobanco
e,consequentemente,o EntityManagerestejaabertoparapossibilitaressa
operação.
139

## Página 152

7.3. LidandocomLazyInitializationException CasadoCódigo
Éjustamentenessepontoqueociclodevidanospassaumarasteira.Por
padrão,o EntityManagergerenciadopeloservidordeaplicaçãoécriado
nomomentoemquealgummétododaclassequeorecebeuinjetadoforinvo-
cado.Sóquetodososobjetosquesãocarregadosdentrodoescopodométodo
deixamdesergerenciadoslogoapósofimdesuaexecuç ão,deixandooobjeto
emumestadochamado detached.Essecomportamentoéoquenosleva
aoproblemaqueestamosvivenciando.
Umamaneiradealteraressecomportamentoédefinindoumescopode
transação.Porexemplo,casotivéssemosanotadoométodo loadBookscom
@Transactional,o EntityManagerviveriaatéofimdométodo,oque,
infelizmente,tambémnãoéosuficienteparanós.Semcontarqueaannota-
tion @Transactionaldeveserutilizadaparademarcarmétodosquereal-
menteprecisemdeumatransação,comofizemosnomomentodesalvarum
livro.
EntityManager extended e o EJB Stateful
Jáexistemsoluçõesquepodemserusadaspararesolveresteproblema.As
opçõesmaiscomunssão:
• CriarumfiltrodaespecificaçãodeServletsquecomeceumatransaç ão
noiníciodorequest,equefechenofim;
• CriarumprodutordeEntityManagerdoCDIeassociá-locomo
escopoderequisição;
• Planejartodasasqueriesdosistemacomousode fetch joins. Dessa
forma,tudooqueé lazyjáécarregado.
Oplanejamentodequerieséasoluçãoquemaisagradaesteautor.Elajá
vemsendoutilizadaduranteolivro,sónãotinhasidodeixadoclaroqueera
porestemotivo.
public class BookDAO {
@PersistenceContext
private EntityManager manager;
140

## Página 153

CasadoCódigo Capítulo7. Carrinhodecompras
...
public List<Book> list() {
return manager.createQuery("select b from Book b join
fetch b.authors",
Book.class).getResultList();
}
Apartenegativadessasoluç ãoéqueelaaumentaconsideravelmentea
complexidadedasqueriesqueserãoescritasnosistema,jáqueotempotodo
teremosdedecidirexatamenteoqueprecisasercarregadoparacadaobjeto.
Parabalancearessaequação,podemosusarumoutrorecurso,jáprovido
pelaespecificação.Primeiro,temosdedeixarclaraanossanecessidade.Pre-
cisamosqueo EntityManagerfiqueabertoenquantoestivermosusandoo
objetocriadoapartirdaclasse ProductDetailBean,umavezqueelevive
durantetodorequest.
Aprimeiraatitudequepodemostomaréadealteraramaneiraqueo
EntityManageréassociadoaoobjetodotipo BookDAO.Atualmente,ape-
sardenãotermosconfigurado,eleésempreligadoaumatransaç ão.
public class BookDAO {
@PersistenceContext(type=PersistenceContextType.TRANSACTION)
private EntityManager manager;
...
}
Quase nunca especificamos o atributotype, já que o padrão é
PersistenceContextType.TRANSACTIONe,normalmente,éoquene-
cessitamosmesmo. Agoraénecessárioaumentaroseutempodevidapara
eleiralémdeumatransaçãoouapenasdaexecuçãodeummétodo.
public class BookDAO {
@PersistenceContext(type=PersistenceContextType.EXTENDED)
private EntityManager manager;
141

## Página 154

7.3. LidandocomLazyInitializationException CasadoCódigo
...
}
É justamente para isso que serve o
PersistenceContextType.EXTENDED.Essetipode EntityManager
deve ser injetado quando é necessário que os objetos carregados por ele
permaneçamgerenciadosenquantooobjetoquesolicitouainje çãoestiver
sendo controlado pelo container. Isso já deveria ser o suficiente, uma
vez que, como o nosso DAO não declarou nenhum escopo do CDI, é
assumido que ele éDependent. Como ele está sendo injetado dentro
do ProductDetailsBean,deveriaficarvivoenquantotalbeantambém
estivesse.
Sóque,apenasporumaquestãodaespecificaç ão,umaclassequedeclaraa
necessidadedeum EntityManagerestendidoprecisatambémseranotada
com @Stateful.
@Stateful
public class BookDAO {
@PersistenceContext(type=PersistenceContextType.EXTENDED)
private EntityManager manager;
...
}
Classesanotadascom @Statefulautomaticamentesãotratadaspelo
containercomo Enterprise Java Beans,eelasficamvivasdentrodocontainer
enquantooobjetoquepediusuainje çãotambémestiver.Como,emgeral,os
beansdoJSFvivemnoescopoderequisição,osseusEJBs statefultambém
viverão.
Pronto, agora podemos acessar a página de detalhes, pois
tudo deve funcionar normalmente. Resolver o problema do
LazyInitializationException dessa forma não é uma aborda-
gem normalmente encontrada, mas este autor acredita que ela é a mais
simplesepoderosaquetemos.
142

## Página 155

CasadoCódigo Capítulo7. Carrinhodecompras
EJB, o antigo centro da especificação
AntesdachegadadoCDI,osEJBseramocentrodaespecificaç ão.
Quandoeranecessáriousarosrecursosprovidospeloservidordeapli-
cação,eraobrigatóriotransformarnossoobjetoemumEJB.Hojeemdia,
aindavemosissoemalgunscasos,masatendênciaécadavezmaisque
simplesobjetospossamreceberqualquerrecursofornecidopeloservi-
dor.
7 .4 S erá que o melhor é o DAO ser um EJB state-
ful?
Anossasolução,apesardeenvolvermuitateoria,ficoubemsimples.Sótem
umpontoqueaindapodeincomodar.ODAOsabequevaiserusadoemum
cenárioqueexigeaextensãodociclodevidado EntityManager.Sóque
esserequisitotemmuitomaisrelaçãocomonossobeandoJSFdoquecom
DAOemsi.
Um objeto dessa mesma classe já é usado em outros cenários na
nossa aplicação, como por exemplo, para salvar um novo livro ou
fazer a listagem. Para essas situações, não foi necessário usar o
PersistenceContextType.EXTENDED.
Paratentarmosmelhoraressasituação,podemosoptarporumasoluç ão
nãoconvencional.Precisodeixarclaroparavocê,leitor,que:oquevoumos-
traragoranãoénormalmenteencontradomundoafora,masmesintona
obrigaçãodemostrarumaestratégiaqueconsideropossuirumdesignme-
lhor.
Comoéo beandoJSFqueestádefinindootempodevidanecessáriodo
EntityManager,podemostransformá-loemumEJB statefulemvezde
DAO.
@Model
@Stateful
public class ProductDetailBean {
143

## Página 156

7.4. SeráqueomelhoréoDAOserumEJBstateful? CasadoCódigo
@PersistenceContext(type=PersistenceContextType.EXTENDED)
private EntityManager manager;
private BookDAO bookDAO;
private Book book ;
@PostConstruct
private void loadManager(){
this.bookDAO = new BookDAO(manager);
}
...
}
Perceba que, além dessa mudança, também paramos de injetar o
ProductDAO.Agora,eleécriadomanualmentenométodoanotadocom
@PostConstruct.
AideiaéquenóspassamosparaoDAOo EntityManagerestendido.
Dessaforma,vocêpodereceberoDAOinjetadoautomaticamentepelocon-
taineremsituaçõescomuns,mastambémpodeusaromesmoDAOemsitu-
açõesquenecessitemdeum EntityManagerestendido.Omáximoquevai
acontecerévocêprecisarinstanciaralgunsDAOsmanualmente,masnada
quesejamuitocomplicado.
Duranteorestantedolivro,serásugeridoquevocêuseessaabordagem,
masfiqueàvontadepararefletireusaraqualseencaixamelhornosseus
projetos.
Sóprecisamosalteraraclasse BookDAOparaelatambémsuportarore-
cebimentodeum EntityManagerpeloconstrutor.
public class BookDAO {
@PersistenceContext
private EntityManager manager;
public BookDAO(){
}
144

## Página 157

CasadoCódigo Capítulo7. Carrinhodecompras
public BookDAO(EntityManager manager){
this.manager = manager;
}
Comoaannotation @PersistenceContextnãopodeserusadaem
parâmetros,somosobrigadosamanterainje çãoviaatributoprivado.Tam-
béménecessáriomanteroconstrutorsemargumentos,paraqueoobjetoseja
instanciadoe,posteriormente,ainje çãofeita.
Oladoruimdessasoluçãoestájustamentenofatodevocêterdeinstan-
ciarosDAOsnamão,alémdereceberum EntityManagerqueapenasé
repassadoparaafrente.Comofaleianteriormente,fiqueàvontadeparare-
fletiredecidiramaneiraquemelhorseencaixarnassuasnecessidades.
7 .5 F ormatando a data de publicação
Nofimdanossapáginadedetalhes,estamosexibindoadatadepublicaç ão
dolivro.
<p>Data de publicação: #{productDetailBean.book.releaseDate.time}
Pormaisquefuncione,asaídageradanãoéexatamenteaqueesperamos.
Paranosajudarnessetipodecenário,podemosusaratag outputTextjunto
comatagdeconversãodedatas.
<p>Data de publicação: <h:outputText
value="#{productDetailBean.book.releaseDate.time}">
<f:convertDateTime pattern="dd/MM/yyyy"/>
</h:outputText></p>
A outputTextsimplesmenteimprimeovalorpassadocomoargu-
mentoparaoatributo value.Ointeressanteéquepodemosassociaratag
convertDateTimee,comisso,oJSFjávaiformatarovalordojeitoque
precisamos.Essaéumaótimaprática,poisestamosusandooframeworkexa-
tamentenopontoondeénecessário.
145

## Página 158

7.6. Carrinhodecompraseoescopodesessão CasadoCódigo
7 .6 C arrinho de compras e o escopo de sessão
Agoraquejáconseguimosnavegarparaapáginadedetalhesdolivro,pode-
moscomeçaraimplementarafuncionalidadedeadicioná-losaocarrinhode
compras.Vamosapenasrelembrarotrechodo detalhe.xhtmlresponsável
porisso.
<form action="/cart/add" method="post" class="container">
<ul id="variants" class="clearfix">
<li class="buy-option">
<input type="radio" name="id"
class="variant-radio"
id="product-variant-#{productDetailBean.book.id}"
value="#{productDetailBean.book.id}"
checked="checked" />
<label class="variant-label"
for="product-variant-#{productDetailBean
.book.id}">
E-book + Impresso
</label>
<small class="compare-at-price">
R$ #{productDetailBean.book.price}
</small>
<p class="variant-price">
R$ #{productDetailBean.book.price}
</p>
</li>
</ul>
<button type="submit" class="submit-image icon-basket-alt"
title="#{productDetailBean.book.title}"></button>
</form>
Oproblemaéqueesseformulárionãoestáligadoanenhum beanda
nossaaplicação.Pararesolverisso,emvezdemodificaroformuláriointeiro
parausarastagsdoJSF,vamosutilizarumanovafuncionalidadequeveio
146

## Página 159

CasadoCódigo Capítulo7. Carrinhodecompras
comoJSF2.2.
<html xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://xmlns.jcp.org/jsf/core"
xmlns="http://www.w3.org/1999/xhtml"
xmlns:pt="http://xmlns.jcp.org/jsf/passthrough"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:jsf="http://xmlns.jcp.org/jsf">
...
<form jsf:id="form" method="post" class= "container">
<ul id="variants" class="clearfix">
<li class="buy-option">
<input type="radio" name="id"
class="variant-radio"
id="product-variant-#{productDetailBean
.book.id}"
value="#{productDetailBean.book.id}"
checked="checked"/>
<label class="variant-label"
for="product-variant-#{productDetailBean
.book.id}">
E-book + Impresso
</label>
<small class="compare-at-price">
R$ #{productDetailBean.book.price}</small>
<p class="variant-price">
R$ #{productDetailBean.book.price}</p>
</li>
</ul>
<button type="submit"
jsf:action="#{shoppingCartBean
.add(productDetailBean.id)}"
class="submit-image icon-basket-alt"
title="#{productDetailBean.book.title}"></button>
147

## Página 160

7.6. Carrinhodecompraseoescopodesessão CasadoCódigo
</form>
Percebaqueusamosumnovo namespace,o xmlns:jsf="http://xmlns.
jcp.org/jsf\T1\textquotedbl{},queimportaparaanossapáginaorecursodo Pass
Through Elements.Estamosusandooprefixo jsfparareferenciá-lo.Este
recursonospermitemarcaralgunselementosquenormalmenteseriamsim-
plescomponentesdoHTML,comocomponentesquedevemsergerenciados
peloJSF.
<form jsf:id="form" method="post" class="container">
Sódeusarumatributoprefixadocom jsfjáindicamosparaofra-
meworkqueeledeveinterpretaresseelementocomoumcomponentegeren-
ciado.ApartebeminteressanteéqueoJSFjásaberelacionarvárioselementos
doHTMLcomseuscomponentesdoservidor.Porexemplo,umformulário
jáéassociadocomaclasse HtmlForm. Usamosamesmatécnicaquando
usamosobotãodentrodoformulário.
<button type="submit"
jsf:action="#{shoppingCartBean.add(productDetailBean
.book.id)}"
class="submit-image icon-basket-alt"
title="#{productDetailBean.book.title}"></button>
Usamosoatributo actionemumelementodotipo button,eissosó
fazsentidoporqueestamosusandooprefixo jsf. Percebaquepassamos
comoargumentojustamenteareferênciaparaométodoquedevesercha-
madononossobeanresponsávelporadicionarprodutosnocarrinho.
Esterecursoveioparafecharumalacunaimportantequeexistiaemapli-
caçõesescritascomoJSF.Muitosprogramadoresreclamavamquenãotinham
controlesobreoHTMLgerado,oque,apartirdestaúltimaversão,deixoude
serverdade.VocêagorapodemontarumapáginainteiracomHTMLpuroe
sógerenciaroscomponentesquevocêrealmenteprecisa.
148

## Página 161

CasadoCódigo Capítulo7. Carrinhodecompras
Lógica para adicionar os produtos no carrinho
Oatributo actiondonossobotãoestáapontandoparaométodo add
do bean ShoppingCartBean. Vamosdarumaolhadaemcomoestáo
códigoreferenteaestapartedosistema.
package br.com.casadocodigo.loja.managedbeans.site;
//imports
@Model
public class ShoppingCartBean {
@Inject
private ShoppingCart shoppingCart;
@Inject
private BookDAO bookDAO;
public String add(Integer id){
Book book = bookDAO.findById(id);
ShoppingItem item = new ShoppingItem(book);
shoppingCart.add(item);
return "/site/carrinho?faces-redirect=true";
}
public String remove(Integer id){
Book book = bookDAO.findById(id);
ShoppingItem item = new ShoppingItem(book);
shoppingCart.remove(item);
return "/site/carrinho?faces-redirect=true";
}
}
Ocódigoemsinãotemnadadenovo.Apenasusamosoutraclassecom
oobjetivodemanterosprodutosadicionadosaonossocarrinho.Vamosdar
umaolhadanela:
package br.com.casadocodigo.loja.models;
149

## Página 162

7.6. Carrinhodecompraseoescopodesessão CasadoCódigo
public class ShoppingCart implements Serializable{
/**
*
*/
private static final long serialVersionUID =
private Map<ShoppingItem, Integer> items =
new LinkedHashMap<ShoppingItem, Integer>();
public void add(ShoppingItem item) {
items.put(item, getQuantity(item) + 1);
}
public Integer getQuantity(ShoppingItem item) {
if (!items.containsKey(item)) {
items.put( item, 0);
}
return items.get(item);
}
public Integer getQuantity() {
return items.values().stream()
.reduce(0, (next, accumulator) -> next
+ accumulator );
}
public Collection<ShoppingItem> getList() {
return new ArrayList<>(items.keySet());
}
public BigDecimal getTotal(ShoppingItem item) {
return item.getTotal(getQuantity(item));
}
public BigDecimal getTotal(){
BigDecimal total = BigDecimal.ZERO;
for(ShoppingItem item : items.keySet()){
150

## Página 163

CasadoCódigo Capítulo7. Carrinhodecompras
total = total.add( getTotal(item));
}
return total;
}
public void remove(ShoppingItem shoppingItem) {
items.remove(shoppingItem);
}
public boolean isEmpty() {
return items.isEmpty();
}
}
Alémdessaclasse,tambémprecisamosdaclasse ShoppingItem.
package br.com.casadocodigo.loja.models;
//imports
public class ShoppingItem {
private Book book ;
// apenas para ficar mais facil de gerar
// o hashcode e equals
private Integer bookId;
public ShoppingItem(Book book) {
this.book = book;
this.bookId = book .getId();
}
public Book getBook() {
return book;
}
public BigDecimal getPrice() {
return book.getPrice();
}
151

## Página 164

7.6. Carrinhodecompraseoescopodesessão CasadoCódigo
public Integer getBookId() {
return bookId;
}
public BigDecimal getTotal(Integer quantity) {
return getPrice().multiply(new BigDecimal(quantity));
}
@Override
public int hashCode() {
final int prime = 31;
int result = 1;
result = prime * result + ((bookId == null) ? 0 :
bookId.hashCode());
return result ;
}
@Override
public boolean equals(Object obj) {
if (this == obj)
return true;
if (obj == null)
return false;
if (getClass() != obj.getClass())
return false;
ShoppingItem other = (ShoppingItem) obj;
if (bookId == null) {
if (other.bookId != null)
return false;
} else if (!bookId.equals(other.bookId))
return false;
return true;
}
}
Oscódigoscompletosdessasclassespodemserencontradosem http://
bit.ly/carrinho-casadocodigo.
152

## Página 165

CasadoCódigo Capítulo7. Carrinhodecompras
Oleitormaisatentodeveterpercebidoque,apósadicionarumproduto
nocarrinho,fazemosum redirectparaumatelacujaresponsabilidadeéjus-
tamenteexibirtodosositensadicionados.
@Model
public class ShoppingCartBean {
@Inject
private ShoppingCart shoppingCart;
@Inject
private BookDAO bookDAO;
public String add(Integer id){
Book book = bookDAO.findById(id);
ShoppingItem item = new ShoppingItem(book);
shoppingCart.add(item);
return "/site/carrinho?faces-redirect=true";
}
...
Comoaindanãotemosessepáginapronta,chegouahoradeimplemen-
tarmos.Denovo,comoelaéumtantoquantogrande,vamosapenascolocar
ostrechosimportantesparaanossaleitura.Alocalizaç ãodoarquivodeveser
site/carrinho.xhtml.
<form jsf:id="cartForm" method="post" >
<table id="cart-table">
...
<tbody>
<ui:repeat var="item" value="#{shoppingCart.list}">
<tr>
<td class="cart-img-col">
<img src="#{item.book.coverPath}"
width="71px" height="100px"/>
</td>
153

## Página 166

7.6. Carrinhodecompraseoescopodesessão CasadoCódigo
<td class="item-title">#{item.book.title}</td>
<td class="numeric-cell">R$ #{item.price}</td>
<td class="quantity-input-cell">
<input type="number" min="0"
readonly="readonly"
id="update
name="upda
value="#{shoppingCart.getQuantity(item)}"/>
</td>
<td class="numeric-cell">
R$ #{shoppingCart.getTotal(item)}
</td>
<td class="remove-item">
<a jsf:action="#{shoppingCartBean
.remove(item.bookId)}">
<img src="..." alt="Excluir" title="Excluir"/>
</a></td>
</tr>
</ui:repeat>
</tbody>
<tfoot>
<tr>
<td colspan="3"><input type="submit" class="checkout"
name="checkout" value="Finalizar compra "
id="checkout"/>
</td>
<td class="quantity-input-cell"><input type="submit"
class="update-cart" name="update" value=""/>
</td>
<td class="numeric-cell">R$ #{shoppingCart.total}</td>
<td></td>
</tr>
</tfoot>
</table>
154

## Página 167

CasadoCódigo Capítulo7. Carrinhodecompras
</form>
MontamosnovamenteumHTMLlimpo,esóadicionamosalgunsatribu-
tosdoJSFparatransformaralgunselementosemcomponentesgerenciados
peloframework.Umdetalheinteressantefoiqueusamosavariáveldenome
shoppingCart,fazendoclarareferênciaànossaclasse ShoppingCart.
Vocêdeveestarseperguntando: quer dizer que, independente da classe que
eu crie, os objetos criados a partir dela estarão disponíveis via Expression
Language?
Casoissofosseverdade,nossosDAOsquesãoinstanciadosviaCDIes-
tariamdisponíveisnapáginaeteríamosumaquebradecamadasmuitoperi-
gosa.Paracontrolarquemdeveficardisponívelounão,podemosusaraan-
notation @Named.Alémdisso,aindaprecisamosmanteresseobjetovivodu-
ranteváriosrequestsdomesmousuário,contextotambémconhecidocomo
Session. Precisamosmanteroobjetona session,umavezquenossousuário
podeadicionarváriositensnocarrinho.
package br.com.casadocodigo.loja.models;
//outros imports
import javax.enterprise.context.SessionScoped;
import javax.inject.Named;
@Named
@SessionScoped
public class ShoppingCart implements Serializable{
...
}
Implementamos Serializableapenasparadeixarclaroqueoestado
deumobjetodestaclassepodeserpersistido. Agoranossousuáriojápode
adicionarositensnocarrinhoevisualizaralistadeprodutosquevãosercom-
prados.
155

## Página 168

7.7. Conclusão CasadoCódigo
7 .7 C onclusão
Nestecapítulo,implementamosváriasfuncionalidadesdaCasadoCódigo.
Passamosporalgumasdificuldadesqueforamimportantes,jáquenosre-
velaram novas técnicas. Por exemplo, usamos oPass Through Element
paramanternossoHTMLfielaositeesóadicionarnaárvoredoJSFal-
guns elementos. Além disso, também trabalhamos com a especificação
dosEJBs,poisusamosaannotation Statefulparaconseguirmanterum
EntityManagerestendido.
Minhadicaéquevocêrespireumpouco,tenteimplementaroudigerir
tudooquefoiexibidoatéaquieaí,depois,vocêcontinuaaleitura. Ainda
temmuitocoisaboaporvir.Jánopróximocapítulovamosnosintegrarcom
outrosistemaetrabalharcomexecuçõesdecódigosassíncronos.
156

## Página 169

Capítulo8
Fechamentodacomprae
processamentoassíncrono
Nocapítuloanterior,come çamosaimplementaroprocessodefechamento
decompradalojadaCasadoCódigo,ejáconseguimosconcluirapartede
adicionarositensemumcarrinhodecompras.Agora,precisamosrealmente
finalizarumnovopedidodentrodaloja.
8.1 I mplementando a tela de finalização
Aversãodeteladefinalizaç ãodecompraquevamosimplementardeveficar
próximadafiguraaseguir:

## Página 170

8.1. Implementandoateladefinalização CasadoCódigo
Fig.8.1:TeladecheckoutdaCasadoCódigo
Primeiro,precisamosalterarumpouconossocódigodateladocarrinho
paraadicionarumlinkquenosleveparaoendere çodefinalizaçãodecompra.
<tfoot>
<tr>
<td colspan="3">
<a href="${request.contextPath}/site/checkout.xhtml"
id="checkout" class="checkout">Finalizar compra
</a></td>
...
</tr>
</tfoot>
Simplesmenteadicionamosumlinkquelevaráousuárioparaatelade
checkout.Porsinal,essavaisermaisumapáginanaqualusaremosbastante
onovorecursodo PassThrough Elements.
Basicamente, vamosteroHTMLjádefinidopelaCasadoCódigo, e
apenas serão modificados os elementos que devem ser gerenciados pelo
JSF. O arquivo responsável por montar a tela de checkout deve ficar em
site/checkout.xhtml.
158

## Página 171

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
Comojávemsendofeito, vamosapenasanalisaraspartesimportan-
tesdocódigo. Oarquivocompletopodeserencontradoem http://bit.ly/
checkout-casadocodigo.
<form accept-charset="UTF-8" jsf:prependId="false"
class="section__form
js-shipping-address-with-selector"
jsf:id="checkoutUserForm" method= "post"
<div style="display:none"></div>
<div class="fieldset"
data-email-check='#checkout_email_suggestion'>
<div class="field field--required">
<label for="checkout_email">E-mail</label>
<input autocapitalize="off"
autocomplete="shipping email"
jsf:id="email" data-autofocus="true"
jsf:value= "#{checkoutBean.systemUser.email}"
placeholder="E-mail" size="30"
spellcheck="false"
type="email"/>
</div>
...
</div>
<h5>Endereço de entrega</h5>
<div class="fieldset" id="shipping-address"
data-shipping-address="">
<div class="field field--optional">
<label for=
"checkout_shipping_address_first_name">
</label>
Nome
<input autocomplete="shipping given-name"
159

## Página 172

8.1. Implementandoateladefinalização CasadoCódigo
jsf:id="name"
jsf:value="#{checkoutBean.systemUser
.firstName}"
placeholder="Nome" size="30"
type="text"/>
</div>
<div class="field field--required">
<label for=
"checkout_shipping_address_last_name">
Sobrenome</label>
<input autocomplete="shipping family-name"
jsf:id="lastName"
jsf:value="#{checkoutBean.systemUser
.lastName}"
placeholder="Sobrenome" size="30"
type="text"/>
</div>
<div class="field field--required">
<label for=
"checkout_shipping_address_company">
CPF/CNPJ
</label>
<input autocomplete="shipping organization"
jsf:id="socialId"
jsf:value="#{checkoutBean.systemUser
.socialId}"
placeholder="999.999.999-99" size="30"
type="text">
</div>
...
<div class="field field--required"
data-country-section="1">
<label for=
"checkout_shipping_address_country">
País
160

## Página 173

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
</label>
<select
jsf:value="#{checkoutBean.systemUser
.country}"
jsf:id="country" size="1">
<f:selectItem itemValue=""
itemLabel="Escolha o país"/>
<f:selectItem itemValue="Portugal"
itemLabel="Portugal"/>
<f:selectItem itemValue="Brasil"
itemLabel="Brasil"/>
<f:selectItem itemValue="Africa do Sul"
itemLabel="Africa do Sul"/>
<f:selectItem itemValue="Argentina"
itemLabel="Argentina"/>
<f:selectItem itemValue="Colombia"
itemLabel="Colombia"/>
</select>
</div>
Éumformuláriocommuitoscampos,eaquisóexibimosalguns.Aparte
interessanteéqueconseguimosmanteroHTMLoriginal,eapenasadiciona-
mosalgunsatributosespecíficosdoJSFparaqueoframeworkentendaqueos
inputseoformulárioemsidevamsertratadoscomocomponentes.Umque
nosdeuumpoucomaisdetrabalhofoio select.
<select jsf:value="#{checkoutBean.systemUser.country}"
jsf:id="country" size="1">
<f:selectItem itemValue="" itemLabel= "Escolha o país"/>
<f:selectItem itemValue="Portugal" itemLabel="Portugal"/>
<f:selectItem itemValue="Brasil" itemLabel="Brasil"/>
<f:selectItem itemValue="Africa do Sul"
itemLabel="Africa do Sul"/>
<f:selectItem itemValue="Argentina" itemLabel="Argentina"/>
<f:selectItem itemValue="Colombia" itemLabel="Colombia"/>
</select>
OJSFsabeapenasqueumatag select,marcadacomumatributoes-
pecial,devevirarumcomponentedotipo HtmlSelectOneListBox,mas
161

## Página 174

8.2. Gravandoasinformaçõesdousuário CasadoCódigo
nãotemideiadoquefazercomoselementos optionque,pensandoapenas
emHTML,deveriamvirdentrodeum select.Porcontadessalimitação,
somosobrigadosausaratag selectItem,oquerealmentenãoimpacta
muito.
Outro detalhe bem interessante é que a usamos como filha de um
select,justamenteparadeixarclaroqueofatodemarcarumelemento
HTMLcomumatributoJSFrealmenteofazsergerenciadoeentrarnaár-
voredecomponentes.
8.2 G rav ando as informações do usuário
Oleitormaisatentojádeveterpercebidoousodeumnovo beanparalidar
comafinalizaçãodopedido.O valuedetodososinputsestãoapontando
para #{checkoutBean...},queéjustamenteessenovobean.Aprimeira
tarefaquevamostrataréadegravarasinformaçõesdonovocomprador.
Apenaspararefrescarsuamemória,vamosolharumdosinputsdofor-
muláriomaisumavez:
<input autocapitalize="off" autocomplete="shipping email"
jsf:id="email" data-autofocus="true"
jsf:value= "#{checkoutBean.systemUser.email}"
placeholder="E-mail" size="30" spellcheck="false"
type="email"/>
...
<input class="btn" name="commit"
jsf:action="#{checkoutBean.checkout()}"
type="submit" value="Continuar" />
Percebaqueeleestáassociadoaosmétodosdeacessoqueretornamum
objetoquerepresentaumusuário. Alémdisso,obotãodefinalizaç ãodeve
fazerusodométodo checkoutnamesmaclasse. Vamosdarumaolhada
paraentenderumpoucomaisdocódigo.
package br.com.casadocodigo.loja.managedbeans.site;
162

## Página 175

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
//imports
@Model
public class CheckoutBean {
private SystemUser systemUser = new SystemUser();
@Inject
private SystemUserDAO systemUserDAO;
@Inject
private ShoppingCart cart;
public SystemUser getSystemUser() {
return systemUser;
}
public void setSystemUser(SystemUser systemUser) {
this.systemUser = systemUser;
}
@Transactional
public void checkout() throws IOException {
systemUserDAO.save(systemUser);
//vamos também gravar a compra
//aprovar com um sistema externo
}
}
Aclasseéum beannormal,nadaquenãotenhamostrabalhadoatéagora.
Paraquetudofuncione,precisamosapenasimplementaraparterelativaao
usuário.Começaremospelaclasse SystemUser.
package br.com.casadocodigo.loja.models;
//imports
@Entity
163

## Página 176

8.2. Gravandoasinformaçõesdousuário CasadoCódigo
public class SystemUser {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Integer id;
@Email
@NotBlank
@Column(unique=true)
private String email;
@NotBlank
private String firstName;
@NotBlank
private String lastName;
@NotBlank
@Column(unique=true)
private String socialId;
@NotBlank
private String address;
@NotBlank
private String city;
@NotBlank
private String state;
@NotBlank
private String postalCode;
@NotBlank
private String phone;
@NotBlank
private String country;
private String password;
//metodos de acesso
ÉsimplesmenteumaclassemapeadacomannotationsdaJPAedaBean
Validation. Parafechar,énecessárioquetenhamosoDAOresponsávelpor
gravarumnovousuárionobancodedados.
package br.com.casadocodigo.loja.daos;
//imports
164

## Página 177

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
public class SystemUserDAO {
@PersistenceContext
private EntityManager entityManager;
public void save( SystemUser systemUser) {
entityManager.persist(systemUser);
}
}
Issojáésuficienteparagravarmosousuárioqueestácomprandoumnovo
produto. Poderíamosterverificado,porexemplo,seoe-mailjáexistepara
nãocadastrardenovo. Ficacomodesafioparaoleitorincrementarainda
maisaaplicação.
Ajuda extra com o OmniFaces
PorcontadaintegraçãodoJSFcomaBeanValidation,nossoformulário
inclusivejáestásendovalidado.Bastaadicionarmosatag messageembaixo
decadainputparaexibirmosasmensagensdeerro.
<input autocapitalize="off" autocomplete="shipping email"
jsf:id="email" data-autofocus="true"
jsf:value= "#{checkoutBean.systemUser.email}"
placeholder="E-mail" size="30" spellcheck="false"
type="email"/>
<p class="field_error-message"><h:message for="email"/>
</p>
Essecódigoatéfuncionaenãoinfluenciadiretamentenolayoutdaapli-
cação,masdetodojeitoestamosexibindoo <p>sempreemvezdesóexibir
quandorealmenteexistirumproblema.Paracontornarmosisso,teríamosde
verificarsealgumamensagemfoiadicionadaounão.
Comainten çãodeajudarodesenvolvedorqueutilizaoJSFnodiaadia,
BaukeScholtzcriouumabibliotecachamada OmniFaces.Aideiadessepro-
165

## Página 178

8.2. Gravandoasinformaçõesdousuário CasadoCódigo
jetoéoferecerclassesetagsextrasquerealmentepossamajudarenquanto
estamosdesenvolvendoumaaplicaçãobaseadaemJSF.
SegueumapequenalistadeutilidadesfornecidaspeloOmniFaces:
• Novosvalidadores;
• MaisfacilidadescomAJAX;
• Formatadoresmaiselaborados;
• Novoscomponentes.
Paraonossocaso,vamosusarumaversãodiferentedatag messages,
umaextensãoprovidapeloOmniFacesqueseaplicamuitobemparaanossa
situação.
<html xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://xmlns.jcp.org/jsf/core"
xmlns="http://www.w3.org/1999/xhtml"
xmlns:pt="http://xmlns.jcp.org/jsf/passthrough"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:jsf= "http://xmlns.jcp.org/jsf"
xmlns:o="http://omnifaces.org/ui">
<input autocapitalize="off" autocomplete="shipping email"
jsf:id="email" data-autofocus="true"
jsf:value= "#{checkoutBean.systemUser.email}"
placeholder="E-mail" size="30" spellcheck="false"
type="email"/>
<o:messages for="email" var="message" >
<p class="field_error-message">
#{message.summary}</p>
</o:messages>
Tivemosdeimportaronamespace http://omnifaces.org/ui. Percebaque
agorausamosatag messagesassociadaaoprefixo o:.Essatagsóexibeo
166

## Página 179

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
conteúdoentreelacasoexistaalgumamensagemassociadaaocomponente
referenciadopeloatributo for.
Nãoprecisamoscolocartodoocódigodoformulárioaqui,useamesma
tagparaexibirasmensagensdeerrosdosoutroscampos.Fiqueapenasatento
ao idquevocêvaiutilizarnoatributo for.
PrecisamosadicionaroOmniFacesaonossoprojeto.Paraisso,bastaque
sejaadicionadaumanovadependêncianonossoarquivo pom.xml.
<project ....>
...
<dependencies>
...
<!-- omni -->
<dependency>
<groupId>org.omnifaces</groupId>
<artifactId>omnifaces</artifactId>
<version>2.1</version>
</dependency>
...
</dependencies>
...
</project>
TentenãoconfundiroOmniFacescomumabiblioteca,comooPrime-
Faces. Enquantooúltimotentatrazernovoscomponentesdelayoutparao
nossocódigo,oprimeirofocaemclassesetagsutilitárias.
8.3 V alidação seletiv a com a BeanValidation
Pararepresentarousuário,foiusadaaclasse SystemUser. Umpossível
problemaquepodemosteréque,maisàfrente,quandoadicionarmosaparte
desegurançanaaplicação,teremosdoistiposdeusuários:umcomtodasas
167

## Página 180

8.3. ValidaçãoseletivacomaBeanValidation CasadoCódigo
informaçõespreenchidas,representandotipicamenteumcompradordaCasa
doCódigo;eoutroquesóprecisarádoe-mailedasenha,jáqueseráum
usuáriocompapeldeadministrador.
Analisandoaclasse SystemUser,percebemosqueadicionamosasre-
grasdevalidaçõesemquasetodososatributos.
@Entity
public class SystemUser {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Integer id;
@Email
@NotBlank
@Column(unique=true)
private String email;
@NotBlank
private String firstName;
@NotBlank
private String lastName;
@NotBlank
@Column(unique=true)
private String socialId;
@NotBlank
private String address;
@NotBlank
private String city;
@NotBlank
private String state;
@NotBlank
private String postalCode;
@NotBlank
private String phone;
@NotBlank
private String country;
private String password;
Equandotivermosdecadastrarumnovousuárioqueéadministrador?
Comovamosfazerparaensinaraimplementaç ãodaJPAqueelanãodeve
168

## Página 181

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
validartodasessasinformações?
MantendoasannotationsegerandoastabelaspormeiodopróprioHiber-
nate,inclusiveascolunasdobancosãogeradasnãoaceitandovaloresnulos.
Pensandojustamentenestetipodesituação,aBeanValidationjápreviu
quevocêpodeter grupos de validação.
@Entity
public class SystemUser {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Integer id;
@Email
@NotBlank
@Column(unique=true)
private String email;
@NotBlank( groups=BuyerGroup.class)
private String firstName;
@NotBlank( groups=BuyerGroup.class)
private String lastName;
@NotBlank( groups=BuyerGroup.class)
private String socialId;
@NotBlank( groups=BuyerGroup.class)
private String address;
@NotBlank( groups=BuyerGroup.class)
private String city;
@NotBlank( groups=BuyerGroup.class)
private String state;
@NotBlank( groups=BuyerGroup.class)
private String postalCode;
@NotBlank( groups=BuyerGroup.class)
private String phone;
@NotBlank( groups=BuyerGroup.class)
private String country;
private String password;
O atributo groups permite que você passe a referência para uma
interfacequedefineogrupoquepertenceaalgumavalidaç ão. Perceba
quedeixamosapenasosatributos emaile passwordsemgrupoalgum.A
169

## Página 182

8.3. ValidaçãoseletivacomaBeanValidation CasadoCódigo
interfacequedefineogruponãoprecisatermétodoalgum,éatípica interface
de marcação.
package br.com.casadocodigo.loja.models.validation.groups;
public interface BuyerGroup {
}
ComooJSFjáéintegradocoma Bean Validation,podemosdizerquecada
inputdoformuláriodevetersuavalidaçãoassociadaaumgrupoespecífico.
Vamosanalisarnovamenteoarquivo checkout.xhtml:
<form accept-charset="UTF-8" jsf:prependId="false"
class="section__form js-shipping-address-with-selector"
jsf:id="checkoutUserForm" method="post">
<div style="display:none"></div>
<div class="fieldset"
data-email-check='#checkout_email_suggestion'>
<div class="field field--required">
<label for="checkout_email">E-mail</label>
<input autocapitalize="off"
autocomplete="shipping email"
jsf:id="email" data-autofocus="true"
jsf:value= "#{checkoutBean.systemUser.email}"
placeholder="E-mail" size="30"
spellcheck="false" type="email">
<f:validateBean
validationGroups="br.com.casadocodigo.loja
.models.validation.groups.BuyerGroup"/>
</input>
</div>
...
</div>
170

## Página 183

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
<h5>Endereço de entrega</h5>
<div class="fieldset" id="shipping-address"
data-shipping-address="">
<div class="field field--optional">
<label for=
"checkout_shipping_address_first_name">
Nome
</label>
<input autocomplete="shipping given-name"
jsf:id="name"
jsf:value= "#{checkoutBean.systemUser.firstName}"
placeholder="Nome" size="30" type="text">
<f:validateBean
validationGroups="br.com.casadocodigo.loja
.models.validation.groups.BuyerGroup"/>
</input>
</div>
<div class="field field--required">
<label for="checkout_shipping_address_last_name">
Sobrenome</label>
<input autocomplete="shipping family-name"
jsf:id="lastName"
jsf:value= "#{checkoutBean.systemUser.lastName}"
placeholder="Sobrenome" size="30" type="text">
<f:validateBean
validationGroups="br.com.casadocodigo.loja
.models.validation.groups.BuyerGroup"/>
</input>
</div>
<div class="field field--required">
<label for="checkout_shipping_address_company">
171

## Página 184

8.3. ValidaçãoseletivacomaBeanValidation CasadoCódigo
CPF/CNPJ
</label>
<input autocomplete="shipping organization"
jsf:id="socialId"
jsf:value="#{checkoutBean.systemUser
.socialId}"
placeholder="999.999.999-99" size="30"
type="text">
<f:validateBean
validationGroups="br.com.casadocodigo.loja
.models.validation.groups.BuyerGroup"/>
</input>
</div>
...
<div class="field field--required"
data-country-section="1">
<label for="checkout_shipping_address_country">
País
</label>
<select
jsf:value="#{checkoutBean.systemUser.country}"
jsf:id="country" size="1">
<f:validateBean
validationGroups="br.com.casadocodigo.loja
.models.validation.groups.BuyerGroup"/>
<f:selectItem itemValue=""
itemLabel="Escolha o país"/>
<f:selectItem itemValue="Portugal"
itemLabel="Portugal"/>
<f:selectItem itemValue="Brasil"
itemLabel="Brasil"/>
<f:selectItem itemValue="Africa do Sul"
itemLabel="Africa do Sul"/>
<f:selectItem itemValue="Argentina"
itemLabel="Argentina"/>
<f:selectItem itemValue="Colombia"
172

## Página 185

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
itemLabel="Colombia"/>
</select>
</div>
...
Devemosfazerissoparatodososinputsquedevamservalidadosquando
umacompranalojaestiveracontecendo. Denovo,estamosusandoopo-
derdo PassThrough Elements.Transformamosumsimplesinputemum
componentedoJSFe,comisso,ganhamosodireitodeassociaroutroscom-
ponentesdoframeworkaesseelemento.Osgruposdevalidaç ãosãoprevistos
naespecificação;nãotenhamedodeusá-los.
8.4 S alv ando as informações do checkout
Jáestamossalvandoasinformaçõesdousuárioquandoeleclicanobotãopara
fecharopedido.Opróximopassoéarmazenartodasasinformaçõesdacom-
praemsi.
@Model
@Path("payment")
public class CheckoutBean {
private SystemUser systemUser = new SystemUser();
@Inject
private SystemUserDAO systemUserDAO;
@Inject
private CheckoutDAO checkoutDAO;
@Inject
private ShoppingCart cart;
public SystemUser getSystemUser() {
return systemUser;
}
public void setSystemUser(SystemUser systemUser) {
this.systemUser = systemUser;
}
173

## Página 186

8.4. Salvandoasinformaçõesdocheckout CasadoCódigo
@Transactional
public void checkout() throws IOException {
systemUserDAO.save(systemUser);
Checkout checkout = new Checkout(systemUser ,cart);
checkoutDAO.save(checkout);
}
}
Paraqueocódigoanteriorcompile,énecessárioquesejacriadaaclasse
Checkout,alémdoDAO.OcódigodoDAOnãotemnadanovo,jáquesim-
plesmenteprecisamossalvaroobjeto.
package br.com.casadocodigo.loja.daos;
public class CheckoutDAO {
@PersistenceContext
private EntityManager entityManager;
public void save( Checkout checkout) {
entityManager.persist(checkout);
}
}
Jáocódigodaclasse Checkoutprecisadeumcertomomentoderefle-
xão.Precisamosgravarasseguintesinformações:
• Usuárioassociadoàcompra;
• Valortotaldocarrinho;
• Osprodutosassociadosàcompra.
Umaideiainicialseria,então,terclassesparecidascomasseguintes:
@Entity
public class Checkout {
174

## Página 187

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
@Id @GeneratedValue(strategy=GenerationType.IDENTITY)
private Integer id;
@ManyToOne
private SystemUser buyer;
private BigDecimal value;
private List<Item> items = new ArrayList<>();
...
}
@Entity
public class FinalShoppingItem {
@Id @GeneratedValue(strategy=GenerationType.IDENTITY)
private Integer id;
@ManyToOne
private Book book ;
private int quantity;
private BigDeciamal currentPrice;
...
}
Essemodeloatéfunciona,masparaonossocasoésuficienteguardaruma
representaçãomaissimplesdocarrinho,apenasparaconsultasfuturas.Então,
emvezdemodelardessejeito,podemosfazeroseguinte:
@Entity
public class Checkout {
@Id @GeneratedValue(strategy=GenerationType.IDENTITY)
private Integer id;
@ManyToOne
private SystemUser buyer;
private BigDecimal value;
private String jsonCart;
//construtor para ser usado pelos frameworks
175

## Página 188

8.4. Salvandoasinformaçõesdocheckout CasadoCódigo
protected Checkout() {
}
public Checkout(SystemUser user, ShoppingCart cart) {
this.buyer = user ;
this.value = cart .getTotal();
this.jsonCart = cart.toJson();
}
}
AideiaéguardarmosasinformaçõesdocarrinhocomoumJSON,um
formatomuitoconhecidoderepresentaçãodedados. Inclusive,osbancos
maisconhecidosjásuportamquedadossejamarmazenadosnesteformato.
Acesseolink http://bit.ly/json-mysqleleiaumpoucomais.
Adicionamosométodo toJsondentrodaclasse ShoppingCart.
public class ShoppingCart {
...
public String toJson() {
//como vamos gerar o JSON?
}
}
Usando a nova especificação de geração de JSON
AJSR353(https://www.jcp.org/en/jsr/detail?id=353)defineumadasno-
vasespecificaçõesdoJavaEE7,a Java API for JSON Processing.Issoquer
dizerquevocêjátemsuporteàgeraçãodeJSONdentrodequalquerservidor
queimplementeaúltimaversãoda spec.Issoseencaixaperfeitamentepara
asnossasnecessidades!
public String toJson() {
JsonArrayBuilder itens = Json.createArrayBuilder();
for (ShoppingItem item : getList()) {
itens.add(Json.createObjectBuilder()
.add("title", item.getBook().getTitle())
.add("price", item.getBook().getPrice())
176

## Página 189

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
.add("quantity",getQuantity(item).intValue())
.add("sum", getTotal(item)));
}
return itens.build().toString();
}
PercebaqueamontagemdoJSONéumpoucomanual,mas,emcom-
pensação,nospermitedeformaclaradecidirexatamenteoqueprecisamos
quesejagerado.Vamosdarumaolhadaemcadadasclassesenvolvidas.
Aclasse Jsonéseupontodepartida.Elapossuiosmétodosnecessários
paraoiníciodacriaçãodoseuJSON.Porexemplo,nonossocaso,foipreciso
pedirpelaconstruçãodeum Array,poisprecisamosguardartodosositens
docarrinho.Alémdisso,dedentrodo loop,énecessáriocriarumarepre-
sentaçãoparacadaitemdonossocarrinho.Quandoqueremoscriarapenas
umobjetoJSON,usamosométodo createObjectBuilderevamosadi-
cionandoasinformaçõesnecessárias. Oresultadogeradoéparecidocomo
seguinte:
[
{
"title": "javaee",
"price": 100,
"quantity": 1,
"sum": 100
},
{
"title": "spring mvc",
"price": 100,
"quantity": 1,
"sum": 100
}
]
Estamosquaselá. Onossopedidojáégeradoeassociadocomonovo
comprador.Agoravamos,porenquanto,paraapartefinaldonossoprocesso.
Precisamosvalidarovalordanossacompraemumsistemaexterno!
177

## Página 190

8.5. Integrandocomoutraaplicação CasadoCódigo
JSON-B
NoJavaEE8serádisponibilizadoaespecificaç ãoJSON-B(Java API
for JSON Binding),quevainospossibilitartransformarobjetosemJSON
esairdeJSONparaobjetos,deformaautomática.
8.5 I ntegrando com outra aplicação
Paraaaplicaçãoficaraindamaisparecidacomumadavidareal,vamosterde
nosintegrarcomumsistemaexternoparavalidarovalorfinaldacompra.
Alógicaésimples:sóaceitamospagamentosdeatéR$500,00reais.So-
mosobrigadosapassarosdadosusandoo JSON,evamosusaroHTTPcomo
protocolodeintegração.
Casoovalortenhaseguidoaregra,éretornadoostatus 201,queindica
queumnovorecursofoicriado,nestecaso,opagamento.Poroutrolado,se
tiversidopassadoumvalormaiorque500,éretornadoostatus 400,oque
indicaquearequisiçãopossuidadosinválidos.
CasovocêqueiraefetuarumtesteeestejausandoLinuxouMac,basta
executarum curl.
curl --header "Content-type: application/json" --request POST
--data '{"value": 600}'
http://book-payment.herokuapp.com/payment
UmoutrojeitodeverificaréusandoumplugindoChrome,o Postman.
JAX-RS client
Vamosprecisardeumabibliotecaquenosajudearealizararequisiç ão
HTTP,paraquenossaintegraçãofuncione.Paraanossasorte,naúltimaver-
sãodoJavaEE,foiadicionadoosuporteaestetipodecenárionaespecificaç ão
JAX-RS.Vamoslidarmaisdiretamentecomessaespecificaç ãoemumcapí-
tulomaisparaafrente,ondeteremosqueexporosdadosdonossosistema
emoutrosformatos.
Paranãoperdermuitotempo,vamosvercomoficariaocódigofinalda
finalizaçãodocheckout.
178

## Página 191

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
@Model
public class CheckoutBean {
...
@Transactional
public void checkout() throws IOException {
systemUserDAO.save(systemUser);
Checkout checkout = new Checkout(systemUser,cart);
checkoutDAO .save(checkout);
//código de integração
Client client = ClientBuilder.newClient();
PaymentData paymentData = new PaymentData(total);
String uriToPay =
"http://book-payment.herokuapp.com/payment";
Entity<PaymentData> json = Entity.json(paymentData);
WebTarget target = client.target(uriToPay );
Builder request = target.request();
request.post(json, String.class);
}
}
Respireumpoucoevamospensarsobreotrechodecódigoqueacabamos
deescrever.
1) Criamosoobjetodotipo Clientparafazerarequisição;
2) GeramosoJSONdeumobjetopormeiodaclasse Entity;
3) Definimosoendereçodarequisiçãopormeiodométodo target;
4) Construímosarequisiçãoemsi,comométodo request;
5) Disparamosum postcomoJSONeinformamosquesimplesmentees-
peramosumStringderesposta.
179

## Página 192

8.5. Integrandocomoutraaplicação CasadoCódigo
AAPIdefazerrequisiçõesficoucomumdesignbeminteressante. Os
passossãobemmarcadoseumdependedooutro. Otrechofinal,emque
montamosarequisiçãoemsi,poderiatersidoescritodeumaformamais
sucinta.
client.target(uriToPay).request().post(json, String.class);
Outro detalhe que pode chamar a atenção é a utilização da classe
PaymentData. Qualomotivodenecessitarmosdela? Osistemadepaga-
mentocomoqualestamosrealizandoaintegraç ãopedequeoformatodo
dadopassadosejaoseguinte:
{"value": 600}
Écomosefosseum Map,precisamosdeumachavechamada value
associadaaumvalorqualquer.Casopassemoso BigDecimaldireto,qual
seriaonomedessachave? Éjustamenteporissoqueprecisamoscriaruma
classe.
package br.com.casadocodigo.loja.models;
import java.math.BigDecimal;
public class PaymentData {
private BigDecimal value;
public PaymentData() {
}
public PaymentData(BigDecimal value) {
this.value = value ;
}
public BigDecimal getValue() {
return value;
}
}
180

## Página 193

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
Reparequetemosumatributoquesechamaexatamente value,justa-
menteparaqueo JSONsejageradocomaschavescorretas.
Outropontoemqueprecisamosteraten çãoéparaasemânticadocódigo.
Paraumapessoaquenãoconheceosistema,oqueesseconjuntodelinhas
querdizer?
@Transactional
public void checkout() throws IOException {
...
//código de integração
Client client = ClientBuilder.newClient();
PaymentData paymentData = new PaymentData(total);
String uriToPay =
"http://book-payment.herokuapp.com/payment";
Entity<PaymentData> json = Entity.json(paymentData);
WebTarget target = client.target(uriToPay);
Builder request = target.request();
request.post(json, String.class);
}
Oqueestamosfazendoéaprovandoumpagamentocomumsistemaex-
terno,masnossocódigocontémapenasummontedelinhasusandoumaAPI.
Paramelhorar,vamosdeixá-lodaseguinteforma.
@Model
public class CheckoutBean {
...
@Inject
private PaymentGateway paymentGateway;
@Transactional
public void checkout() throws IOException {
systemUserDAO.save(systemUser);
Checkout checkout = new Checkout(systemUser,cart);
checkoutDAO .save(checkout);
181

## Página 194

8.5. Integrandocomoutraaplicação CasadoCódigo
paymentGateway.pay(total);
}
}
Agora,bastaqueaclasse PaymentGatewaysejacriada.
package br.com.casadocodigo.loja.services;
import java.math.BigDecimal;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
public class PaymentGateway {
public PaymentGateway() {
}
public void pay(BigDecimal total) {
Client client = ClientBuilder.newClient();
PaymentData paymentData = new PaymentData(total);
String uriToPay =
"http://book-payment.herokuapp.com/payment";
Entity<PaymentData> json = Entity.json(paymentData);
client.target(uriToPay).request()
.post(json, String.class);
}
}
182

## Página 195

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
8.6 E xecutando operações demoradas assin-
cronamente
Agoraquenossocódigodeintegraç ãojáfunciona,vamostentarpensarum
poucoadiante. ACasadoCódigoéumaempresadesucesso,oBrasilin-
teirocompralivrosdetecnologianela. Emcertosmomentosdoano,como
na Black Friday,elaliberacertaspromo çõesquefazemcomqueositefique
muitomovimentadoe,comisso,temosmuitosusuáriosconcluindocompras
aomesmotempo.Algosimilaraconteceemtodasasoutrasempresas.
Nãoéraronessassituaçõesdeusointensoqueossistemasfiquemum
poucomaislentos,ouatéquecaiamefiquemforadoarporumtempo,oque
podegerarumprejuízogrande.Emgeral,todosossistemastêmseuspontos
degargaloe,comonãopoderiaserdiferente,nóstemosonossotambém.
Jáseperguntouquantotempopodelevarparaanossaaplicaçãofazeruma
requisiçãoparaosistemadepagamento?Casoesseoutrosistemademore,o
quepodeacontecercomonossosite?
Neste exato momento, o funcionamento é basicamente o seguinte:
quandoumanovarequisiçãochegaaonossoservidorweb,elefazumtra-
tamentoinicialedelegaaresponsabilidadeparaaServletconfigurada,nesse
caso,adoJSF.A FacesServletvaidescobrirquaisbeansdevemseraci-
onadosparatratararequisiç ão,efazerotrabalhoparaqueissorealmente
aconteça.
Todoessefluxoacontecedentrodeuma Threadcriadapeloservidorweb,
paraqueelepossatratarváriasrequisiçõessimultaneamente.Essa Threadsó
éliberadaquandoométododonossobeanacabadefazerotrabalhoeindica
paraqualendere çodevemosir.
Essemodelodetrabalho,emquealguémficaesperandoooutroacabar
paraaísimcontinuarseutrabalho,éconhecidocomomodelo síncrono. O
problemadessemodeloéqueoservidorwebtemumnúmerolimitadode
Threadsquepodemsercriadase,casoessenúmerochegueaolimite,asre-
quisiçõesdosnossosusuáriosvãocome çaraserenfileiradasepodemoster
umalentidãonasaplicações.
Comojácomentamos,emumpicodeacesso,podemossofrerdestepro-
blemajustamentenomomentoemqueprecisamosrealizaraintegraç ãocom
183

## Página 196

8.6. Executandooperaçõesdemoradasassincronamente CasadoCódigo
umsistemaexterno,noqualnãotemosnenhumcontrolesobreotempode
resposta.
Agrandesacadaparaessetipodesituaç ãoétentarliberaroservidorpara
atenderoutrasrequisiçõesenquantorealizamosaintegraç ãocomonosso
meiodepagamento. Éexatamenteparaissoque,desdeaversão3daespe-
cificaçãodeServlets,vocêpodecriarumaServletqueconseguetrabalharde
modoassíncrono!E,paraanossasorte,oJavaEE7nosforneceumaabstraç ão
sobreisso.
Antesdeentrarmosnaimplementaçãoprovidapelaespecificação,vamos
pensarnoexemplodecódigoquegostaríamosdeter.
@Transactional
public void checkout() throws IOException {
systemUserDAO.save(systemUser);
Checkout checkout = new Checkout(systemUser, cart);
checkoutDAO.save(checkout);
new Thread(() -> {
paymentGateway.pay(checkout.getValue());
}).start();
}
Esseseriaojeitomaissimples,mastemosumproblemaprincipal.Uma
vezquevocêdisparoua thread,oprocessamentodorequestvaiacontecer
normalmente,enãoébemissoquequeremos. Precisamosquearesposta
sósejageradaquandoalógicadeaprovarumanovacompraforprocessada.
Dedentrodanossa thread,necessitamosdealgumobjetoquenospermita
notificaraoservidoroexatomomentoqueeleestáliberadoparadevolvera
respostaparaocliente.
Infelizmente,aespecificaçãodoJSFnãofoiconcebidaparatratarmosre-
quisiçõesdessamaneira. Porcontadisso,vamosterdequebrarnossopro-
cessodecheckoutemduasetapas.
Dedentrodonosso beandoJSF,vamosapenasgravarosdadosnobanco
dedados.Quandoessaoperaçãoacabar,vamosredirecionararequisiçãopara
184

## Página 197

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
outroendereçoresponsávelapenasporaprovaracompra. Daquiapouco,
trataremosdessaoutrapartedosistema.AgoravamosresolverapartedoJSF.
@Model
public class CheckoutBean {
private SystemUser systemUser = new SystemUser();
@Inject
private SystemUserDAO systemUserDAO;
@Inject
private CheckoutDAO checkoutDAO;
@Inject
private ShoppingCart cart;
@Inject
private FacesContext facesContext;
@Transactional
public void checkout() throws IOException {
systemUserDAO.save(systemUser);
Checkout checkout = new Checkout(systemUser,cart);
checkoutDAO .save(checkout);
String contextName = facesContext.getExternalContext()
.getContextName();
HttpServletResponse response = (HttpServletResponse)
externalContext.getResponse();
response.setStatus(307);
response.setHeader("Location", "/" +contextName+"/
services/payment?uuid="+checkout.getUuid());
}
}
Usamoso HttpServletResponsepararealizarum redirectparaum
endereçoquenãotemnadaavercomJSF.Os redirectsqueusamoparâmetro
do faces- redirect=true,pormeiodo FacesContext,sópodemser
feitosparaURLstratadaspeloServletdopróprioJSF.
185

## Página 198

8.6. Executandooperaçõesdemoradasassincronamente CasadoCódigo
Umoutropontoaseobservarnessecódigoéousodostatus 307,cujo
significadoé T emporary Redirect. Oendereçoquevaifazerapartefinalda
integraçãodeveseracessadovia POST,jáquenãoqueremosqueonavegador
graveoendere çoepossibiliteumacessodescuidadodeumusuário.
Essestatusservejustamenteparainformarparaoclientequeopróximo
redirecionamentodeveserfeitocomomesmoverbousadoparaacessaro
endereçoatual,quenocasofoium POST.Oheader Locationindicaqual
endereçooclientedeveacessarparaefetuaroredirecionamento.
Outro detalhe interessante é que passamos um argumento chamado
uuid.Aideiaésempregerarumidentificadorumpoucomaiscomplicado
paracadapedido,paraquenenhumusuáriotentealteraraURLecoloqueum
IDdecompraválida. Paranãotermosquelembrardedefiniresse uuido
tempointeiro,vamosutilizarumrecursoprovidopelaJPA.
@Entity
public class Checkout {
...
private String uuid;
...
@PrePersist
public void prePersist(){
this.uuid = UUID.randomUUID().toString();
}
...
}
Você pode anotar um método da sua entidade com a annotation
@PrePersist, e ele vai ser invocado logo antes da invocação método
persist,do EntityManager.
Essesmétodossãoconhecidoscomo métodos de callback,epodemser
degrandeajudaquandotemoslógicasquesempredevemacontecersobde-
terminadascircunstâncias.
ExistemoutrasannotionsdecallbackdaJPA:
186

## Página 199

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
•PreUpdate–ométodoéexecutadologoantesdeum merge;
•PostUpdate–ométodoéexecutadologoapósum merge;
•PreRemove–ométodoéexecutadologoantesdeum remove;
•PostRemove–ométodoéexecutadologoapósum remove;
•PostLoad – o método executado logo após umfind ou um
getReference.
8.7 JAX-RS para todas as outras requisições
HTTP
AtéagoraestávamosusandooJSFparatratarasrequisiçõeswebreferentesà
nossaaplicação.Entretanto,comoelenãooferecesuporteparatratarasmes-
masrequisiçõesdeformaassíncrona,vamosterdeoptarporoutropeda çoda
específicação,oJAX-RS.
OJAX-RS,acrônimopara The Java API for RESTful Web Services,éaes-
pecificaçãoquenospossibilitaparticipardeintegraçõespuramentebaseadas
noprotocoloHTTP.Aindavamosexplorarmaisdessaspossibilidadesemum
capítuloespecialsóparaisso,masnessemomentojánecessitamosdaespe-
cificaçãoporcontadasuaintegraçãocomoscontextosassíncronosprovidos
pelaespecificaçãodeServlets.
Aideiaéquecriemosum beandoJAX-RS,tambémconhecidocomo
Resource,paracarregaracomprapelo uuidefazeraintegraçãocomo
sistemaexterno.
package br.com.casadocodigo.loja.resources;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriBuilder;
187

## Página 200

8.7. JAX-RSparatodasasoutrasrequisiçõesHTTP CasadoCódigo
@Path("payment")
public class PaymentResource {
@Inject
private CheckoutDAO checkoutDao;
@Inject
private PaymentGateway paymentGateway;
@POST
public Response pay(@QueryParam("uuid") String uuid) {
String contextPath = ctx.getContextPath();
Checkout checkout = checkoutDao.findByUuid(uuid);
BigDecimal total = checkout.getValue();
paymentGateway.pay(total);
URI redirectURI = UriBuilder
.fromPath("http://localhost:8080"
+contextPath + "/site/index.xhtml")
.queryParam("msg", "Compra realizada com sucesso")
.build();
Response response = Response.seeOther(redirectURI)
.build();
return response;
}
}
PorcontadoCDI,conseguimosrecebertodasasnossasdependênciasin-
jetadas. Ocódigoemsi,atéapartedaintegraç ão,éomesmoquetinhano
beandoJSF.Apartenovaéotipoderetornodonossométodo.Percebaque,
quandoacabamosaintegração,devolvemosumobjetodotipo Response,e
aquientraumpoucomaisdeteoriasobreoHTTP.
Ométodo seeOtherdaclasse Responsemontaumobjetocujares-
188

## Página 201

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
postageraráostatus303,tambémconhecidocomo See Other. Essestatus
deveserusadoquandoqueremosnotificaroclientedarequisiç ãodequeele
devepegararespostaeacessara URIretornadapormeiodeum GET.
EsteéumdospilaresdoJAX-RS:proverabstraçõesparatrabalharmos
demaneiradiretacomoHTTP,usandooprotocolocomoalicerceparaas
integraçõesquevamosimplementardentrodanossaaplicação.
Outrodetalheimportanteéousodaannotation @Pathparaindicar
qualoendere çobasedonossorecurso. Qualquermétodoqueváseraces-
sadodentrodessaclasseserásolicitadopormeiodeumendere çonoestilo
payment/*.Porexemplo,configuramosométodoquerealizaaintegraç ão
paraseracessadoapenasvia POST.
@POST
public Response pay(@QueryParam("uuid") String uuid) {
...
}
Poderíamos,inclusive,teradicionadomaisum @Pathemcimadomé-
todo.Dessaforma,teríamosumendere çoespecíficoparaele.Optamosape-
naspordiferenciaroacessoatravésdoverboHTTP.Percebaoendere çoque
aparecenonavegador,depoisdeclicarmosnobotãodefinalizaç ãodecompra.
http://localhost:8080/casadocodigo/services/payment
?uuid=1234567890123456789
Aindatemumapartedoendere ço,o/services,quenãodesvendamos.
Segureum
poucoaansiedade,temosdecaminharcomcalma.
Tratando a requisição de maneira assíncrona
Parafechar,sóprecisamosfazercomqueocódigodeintegraç ãocomo
sistemaexternorodeemumcontextoassíncrono. Issojáésuportadopelo
próprioJAX-RS,porcontadasuaintegraçãocomaespecificaçãodeServlets.
@Path("payment")
public class PaymentResource {
private
static ExecutorService executor =
189

## Página 202

8.7. JAX-RSparatodasasoutrasrequisiçõesHTTP CasadoCódigo
Executors.newFixedThreadPool(50);
@Context
private ServletContext ctx;
@Inject
private CheckoutDAO checkoutDao;
@Inject
private PaymentGateway paymentGateway;
@POST
public void pay(@Suspended final AsyncResponse ar,
@QueryParam("uuid") String uuid) {
String contextPath = ctx.getContextPath();
Checkout checkout = checkoutDao.findByUuid(uuid);
executor.submit(() -> {
BigDecimal total = checkout.getValue();
try {
paymentGateway.pay(total);
URI redirectURI = UriBuilder
.fromUri(contextPath +
"/site/index.xhtml")
.queryParam("msg",
"Compra realizada com sucesso")
.build();
Response response = Response
.seeOther(redirectURI).build();
ar.resume( response);
} catch (Exception exception) {
ar.resume( exception);
}
});
190

## Página 203

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
}
}
Respire fundo. Vamos olhar com carinho para o código que acaba-
mos de escrever. O primeiro detalhe é que usamos um objeto do tipo
ExecutorService.
private static ExecutorService executor =
Executors.newFixedThreadPool(50);
Existemváriasimplementaçõesdessainterfaceparacriarmosum pool de
threads,muitosimilaraoquejáfazemosquandocriamosum pool de conexões.
Aideiaénãoterdeficarcriandonovasthreadsotempointeiro.Oatributoé
estático,porquevocêquerusaromesmopoolparatratartodasasrequisições.
O ExecutorServicepossuiométodo submit,noqualprecisamos
passarumainstânciadealgumaimplementaç ãode Runnable. Paranão
termosdeficarusandoclassesanônimas,recorremosparaousodos lambdas
doJava8.
executor.submit(() -> {
BigDecimal total = checkout.getValue();
try {
paymentGateway.pay(total);
URI redirectURI = UriBuilder
.fromUri(contextPath + "/site/index.xhtml")
.queryParam("msg",
"Compra realizada com sucesso")
.build();
Response response = Response.seeOther(redirectURI)
.build();
ar.resume(response);
} catch (Exception exception) {
ar.resume(exception);
191

## Página 204

8.7. JAX-RSparatodasasoutrasrequisiçõesHTTP CasadoCódigo
}
});
Agoravemapartequefaltavaparaonossocódigofuncionar: oobjeto
dotipo AsyncResponse.EssaéaabstraçãodoJAX-RSparanotificarmoso
servidordequenossaexecuçãoassíncronafoifinalizada.
@POST
public void pay(@Suspended final AsyncResponse ar ,...){
executor.submit(() -> {
BigDecimal total = checkout.getValue();
try {
//codigo de integração
Response response = Response.seeOther(redirectURI)
.build();
ar.resume(response);
} catch (Exception exception) {
ar.resume(new WebApplicationException(exception));
}
});
}
Ométodo resumeéoresponsávelporfazeranotificaçãodequenossa
tarefaassíncronafoifinalizada.Paraquetudofuncione,precisamosanotaro
parâmetrodotipo AsyncResponsecomaannotation @Suspended.Elaé
usadaparaindicarparaocontainerqueométodoemquestãodeveserexe-
cutadoemumcontextoassíncrono.
Pronto,agorafazemosocódigodecomunicaç ãocomosistemaexterno
sembloquearonossoservidor!Essaéumaótimatécnica,tarefasdemoradas
nãoprecisamenão devemserexecutadasnathreadqueatendearequisiç ão
emsi.
192

## Página 205

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
8.8 C onfigurando o JAX-RS
Paraquetudofuncione,sófaltouresolveraconfiguraç ãoresponsávelporas-
sociaropadrãodeendere ço/services/*paraqualquer Resourcedo
JAX-RS.Essaconfiguraçãonãopoderiasermaissimples,bastaquecriemos
umaclasse-filhade Application.
package br.com.casadocodigo.loja.resources;
import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;
@ApplicationPath("/services")
public class JaxRsConfiguration extends Application {
}
Além de herdarmos de Application, anotamos a classe com
ApplicationPathedefinimosqualoendere çobase.Éjustamenteporisso
que,quandofomosacessaro Resourceresponsávelpelopagamento,será
usadooendere çoservices/payment.
Outramaneiraderealizaramesmaconfiguraç ãoéutilizaro web.xml.
Comonossaaplicaçãoéweb,bastaqueadicionemosum Servletespecífico.
<servlet>
<servlet-name>javax.ws.rs.core.Application</servlet-name>
</servlet>
<servlet-mapping>
<servlet-name>javax.ws.rs.core.Application</servlet-name>
<url-pattern>/services/*</url-pattern>
</servlet-mapping>
Odetalheimportanteaquiéovalordatag servlet-name. Éobriga-
tórioquesejausado javax.ws.rs.core.Application. Aespecifica-
çãoobrigaqueaimplementaç ãodoJAX-RSregistre,dinamicamente,uma
Servletexatamentecomessenome.Eaí,no url-pattern,colocamoso
nossopadrãodeURLbase.
EsteautorsempreprefereconfiguraçõesbaseadasemcódigoJava,então
écomaprimeiraop çãoquevamosseguirnolivro.
193

## Página 206

8.9. Curiosidade:usandoumExecutorServicegerenciado CasadoCódigo
8.9 C uriosidade: usando um ExecutorS ervice
gerenciado
Nonossocódigodeintegração,fomosnósqueficamosresponsáveispelacri-
açãodeum pool de threads.Pormaisqueissofuncione,temosdeficaratentos
pois,nomomentoquedecidimosusarumrecursonãoinjetadopeloservidor,
passamosaterquetalveznospreocuparcomalgunsdetalhesamaisdeinfra-
estrutura.Porexemplo,tivemosdedecidironúmerode threadsdisponíveis
nosnossos pools.
Sabendoquecertoscódigosprecisamserexecutadosemoutras threads,o
JavaEE,naversão7,trouxeumanovaespecificaç ão,a JA V A EE Concurrency
Utilities. Vamosvercomopoderiaficarnossocódigodeintegraç ãocomo
meiodepagamento.
@Path("payment")
public class PaymentResource {
@Context
private ServletContext ctx;
@Inject
private CheckoutDAO checkoutDao;
@Inject
private PaymentGateway paymentGateway;
@Resource( name =
"java:comp/DefaultManagedExecutorService")
private ManagedExecutorService managedExecutorService;
@POST
public void pay(@Suspended final AsyncResponse ar,
@QueryParam("uuid") String uuid) {
String contextPath = ctx.getContextPath();
Checkout checkout = checkoutDao.findByUuid(uuid);
managedExecutorService.submit(() -> {
194

## Página 207

CasadoCódigo Capítulo8. Fechamentodacompraeprocessamentoassíncrono
BigDecimal total = checkout.getValue();
try {
paymentGateway.pay(total);
URI redirectURI = UriBuilder
.fromUri(contextPath +
"/site/index.xhtml")
.queryParam("msg",
"Compra realizada com sucesso")
.build();
Response response =
Response.seeOther(redirectURI).build();
ar.resume(response);
} catch (Exception exception) {
ar.resume(exception);
}
});
}
}
Anovidadeéque,emvezdeusarainterface ExecutorService,pas-
samosausara ManagedExecutorService.Percebaqueainje çãofoifeita
pormeiodaannotation @Resource. Tambémtivemosdeusarachave
java:comp/DefaultManagedExecutorService,queéonomeimposto
pelaespecificaçãoquedeveestardisponívelnaJNDI.
Aalteraçãoemsifoisimples,masaindatemosoutrosganhosnãotão
explícitos. Porexemplo,nossocódigopodenecessitardetransações,EJBs,
segurançaemuitosoutrosdetalhesqueestamosanalisandoduranteacons-
truçãodoprojeto.Quandovocêiniciauma threadmanualmente,tudoissoé
perdido,jáqueoservidornãotemconhecimentodesserecurso.Quandousa-
mosum ExecutorServicegerenciadopeloservidordeaplicações,temos
agarantiadequeosdevidoscontextosserãopropagados,oquenospermite
focarnanossaregradenegóciodoqueemdetalhesdeinfraestrutura.
195

## Página 208

8.10. Conclusão CasadoCódigo
8.10 C onclusão
Estefoiumcapítulobemdenso.UsamosnovosstatusdoHTTP,adicionamos
oJAX-RSnanossaaplicaçãoparalidarcomrequisiçõesnãorelacionadascom
oJSF,eaindadiscutimoscomolidarcomrequisiçõespotencialmentedemo-
radas,delegandoaexecuçãoparaocontextoassíncronodoservidor.
Minhasugestão,assimcomofoinoúltimocapítulo,équevocêpareum
poucoparadigerirtudooquefizemos. Nopróximopassodanossaaven-
tura,vamosdebatersobrecacheecomoissopodeajudarnaperformanceda
aplicação,comcertezaumtópicomaissimplesedefácilcompreensão.
196

## Página 209

Capítulo9
Melhorandoaperformancecom
cache
SemprequeentramosnositedaCasadoCódigo,elenosmostraummontede
livrosquepodemoscomprar.Oleitormaisatentojádeveterpercebidoque
essalistagemnãomudamuitodentrodeumdeterminadointervalodetempo.
Eofatodenãomudarnoslevaaumquestionamento: será que realmente
precisamos ficar executando as duas consultas todas as vezes em que um usuário
acessar essa página?
9.1 C acheando o retorno das consultas na JP A
Apenaspararefrescarmosamemória,nahomedaCasadoCódigoexibimos
duaslistagensdelivros:aprimeiracomosprincipaislan çamentoseasegunda

## Página 210

9.1. CacheandooretornodasconsultasnaJPA CasadoCódigo
comoutroslivrosdaeditora.
Atualmente,todavezqueumnovousuárioacessaaaplicaç ão,essascon-
sultasdevemserrealizadasnobancodedados.Casoosdadosmudassemem
cadaumadasconsultas,atéfariasentidobuscarasinformaçõesotempotodo,
masnessasituaçãoemespecífico,oslivrosretornadossãosempreosmesmos.
Umadasprincipaisaçõesquepodemosrealizarparamelhoraraperfor-
mancedaaplicaçãoéjustamenteminimizaroacessoaobancodedados,guar-
dandoosretornosemum cache. Naverdade,issopodeseraplicadopara
qualquerpartedoseusistemaquebusqueinformaçõesdeumaaplicaç ãoex-
terna.
Paraanossaalegria,oHibernatejásuportaqueoresultadodecertasque-
riesdosistemadevamserguardadosnamemória.Esse cachecompartilhado
entreváriasinstânciasdo EntityManageréconhecidocomo Second Level
Cache.
public class BookDAO {
@PersistenceContext
private EntityManager manager;
...
public List<Book> lastReleases() {
TypedQuery<Book> query = manager
.createQuery(
"select b from Book b where b.releaseDate
<= now() order by b.id desc",
Book.class).setMaxResults(3);
query.setHint(QueryHints.HINT_CACHEABLE, true);
return query.getResultList();
}
public List<Book> last(int number) {
TypedQuery< Book> query = manager
.createQuery("select b from Book b
198

## Página 211

CasadoCódigo Capítulo9. Melhorandoaperformancecomcache
join fetch b.authors",
Book.class).setMaxResults(number);
query.setHint(QueryHints.HINT_CACHEABLE, true);
return query.getResultList();
}
}
Ométodo setHintesperacomoargumentouma Stringinformando
onomedaconfiguraçãoquequeremosdefinir,assimcomoseuvalor.Acons-
tante HINT_CACHEABLEguardaovalor org.hibernate.cacheable.
CasoestivéssemosusandodiretamenteaAPIdoHibernate,poderiater
sidousadométodo setCacheable.O setHintfoiamaneiraencontrada
pelaespecificaçãoparapodermosinvocaralgunsdetalhesdaimplementaç ão
semrecorreràssuasclasses.
Agora,setentarmosacessaroendere çosite/index.xhtmleobser-
varmosoconsoledoWildFly,vamosperceberqueaqueryaindaestásendo
executadatodasasvezes. O cachedequerynãoestáhabilitadoporpadrão.
Comoéumaconfiguraçãomuitosensível,oHibernateexigequevocê,por
vontadeprópria,habiliteousodocachedeconsultas. Precisamosalteraro
arquivo persistence.xml.
<persistence-unit name="casadocodigo-persistence-unit"
transaction-type="JTA">
...
<properties>
...
<property name="hibernate.cache.use_query_cache"
value="true"/>
</properties>
</persistence-unit>
Aconfiguraçãodecachedequeriesaindanãoésuportadapelaespecifica-
ção,entãousamoschavesespecíficasdoHibernate.Apósessaconfiguraç ão,
quandotentamosiniciaroservidor,recebemosumaexception.
199

## Página 212

9.1. CacheandooretornodasconsultasnaJPA CasadoCódigo
Caused by:
org.hibernate.cache.NoCacheRegionFactoryAvailableException:
Second- level cache is used in the application, but property
hibernate.cache.region.factory_class is not given; please either
disable second level cache or set correct region factory using
the hibernate.cache.region.factory_class setting and make sure
the second level cache provider (hibernate-infinispan, e.g.) is
available on the classpath.
Informamosquequeremoshabilitaro cachedequeries,masaindapreci-
samosconfiguraroHibernateparausaro cachedesegundoníveldemaneira
geral. Podemoscachearmuitomaisdoquequeries,evamosfazerissona
continuaçãodestecapítulo!
<persistence-unit name="casadocodigo-persistence-unit"
transaction-type="JTA">
...
<shared-cache-mode>ENABLE_SELECTIVE</shared-cache-mode>
<properties>
...
<property name="hibernate.cache.use_query_cache"
value="true"/>
</properties>
</persistence-unit>
Atag shared-cache-modedaJPAdeveserusadaparainformarmos
comovamosdecidirquaisobjetosdevemsercacheados. Vamospensarum
poucomaissobreisso.QuandofazemosumaconsultapormeiodaJPA,geral-
menteéretornadaumalistadeobjetos.Essaconfiguraç ãoserveparatermos
apossibilidadededizerquaistiposdeobjetosdevemsermantidosem cache.
Aopção ENABLE_SELECTIVEéamaisutilizada,poispermitequeoprogra-
madordefinaexatamentequaisentidadespodemsermantidasnamemória.
Vejaquaissãoasoutrasop ções:
•ALL–todasasentidadespodemficarnocache.Geralmentenãousa-
mosessaop ção,poisnemtodaentidademerecesercacheada.
200

## Página 213

CasadoCódigo Capítulo9. Melhorandoaperformancecomcache
•NONE–nenhumaentidadepodeirparaocache. Sóseriausadasea
aplicaçãorealmentequiserdeixarexplícitoquenadapodesercache-
ado.
•DISABLE_SELECTIVE–partedoprincípioquetodasasentidadespo-
demficarnocache.Dessaforma,oprogramadordeveirconfigurando
cadaentidadequenãopodesercacheada.
Comnossaconfiguraçãofeita, chegouahoradeacessarmosapágina
inicialdosite. Porém,quandoofazemos,percebemosumcomportamento
muitoestranho:diversasconsultasestãoaparecendonoconsoledoservidor.
Hibernate:
select
book0_.id as id1_1_0_,
book0_.coverPath as coverPat2_1_0_,
book0_.description as descript3_1_0_,
book0_.numberOfPages as numberOf4_1_0_,
book0_.price as price5_1_0_,
book0_.releaseDate as releaseD6_1_0_,
book0_.summaryPath as summaryP7_1_0_,
book0_.title as title8_1_0_
from
Book book0_
where
book0_.id=?
Hibernate:
select
book0_.id as id1_1_0_,
book0_.coverPath as coverPat2_1_0_,
book0_.description as descript3_1_0_,
book0_.numberOfPages as numberOf4_1_0_,
book0_.price as price5_1_0_,
book0_.releaseDate as releaseD6_1_0_,
book0_.summaryPath as summaryP7_1_0_,
book0_.title as title8_1_0_
from
Book book0_
where
201

## Página 214

9.1. CacheandooretornodasconsultasnaJPA CasadoCódigo
book0_.id=?
Hibernate:
select
book0_.id as id1_1_0_,
book0_.coverPath as coverPat2_1_0_,
book0_.description as descript3_1_0_,
book0_.numberOfPages as numberOf4_1_0_,
book0_.price as price5_1_0_,
book0_.releaseDate as releaseD6_1_0_,
book0_.summaryPath as summaryP7_1_0_,
book0_.title as title8_1_0_
from
Book book0_
where
book0_.id=?
Hibernate:
select
book0_.id as id1_1_0_,
book0_.coverPath as coverPat2_1_0_,
book0_.description as descript3_1_0_,
book0_.numberOfPages as numberOf4_1_0_,
book0_.price as price5_1_0_,
book0_.releaseDate as releaseD6_1_0_,
book0_.summaryPath as summaryP7_1_0_,
book0_.title as title8_1_0_
from
Book book0_
where
book0_.id=?
Entendendo exatamente como funciona o cache de segundo nível
Asimplementaçõesde cache,emgeral,sãoestruturasbaseadasemma-
pas.QuandopedimosparaoHibernatedeixaroresultadodasconsultasno
cache,oqueelefaz,porbaixodospanos,éjustamenteadicionarumaentrada
nessemapa,associandooretornodaconsulta. Éjustamenteaquiqueestá
nossoproblema.Paraocachedequery,sãoarmazenadosapenasos idsdas
entidadesretornadas,nãoosobjetoscompletos.
202

## Página 215

CasadoCódigo Capítulo9. Melhorandoaperformancecomcache
Internamente,asentradasdocachesãodivididasnaschamadas regiões.
Elasservemparaqueaaplicaçãopossa,porexemplo,limpartodaumaregião
decache.
//exemplo para limpar o cache pela API do Hibernate
entityManagerFactory.
unwrap(SessionFactory.class).getCache().
evictQueryRegion("algumaRegiao");
TambémpodemosacessarocachedesegundoníveldiretamentepelaAPI
daJPA,maselaaindanosoferecemenosop ções. Nãoconseguimoslimpar
umaregiãoespecificamente,porexemplo. Vejaumexemplodecomovocê
poderiaacessá-lo:
Cache cache = entityManagerFactory().getCache();
cache.evictAll();
Nofim,oqueaconteceéque,paracada idencontradonocachedaquery
específica,oHibernatevaibuscarporessemesmo idnaregiãodocacheda
entidadeespecífica.Comoelenãoencontra,fazum selectparabuscaros
dadosdedeterminadaentidade.
Habilitando a entidade para ser cacheada
Pararesolvermosonossoproblema,bastaquesejaadicionadaumaan-
notationnaentidadequeestáparticipandodaquery.
package br.com.casadocodigo.loja.models;
...
import javax.persistence.Cacheable;
@Entity
@Cacheable
public class Book {
...
}
Percebaqueessaannotationtambémédaespecificaç ão. Agorasim,se
tentarmosacessarapáginainicialdaaplicaç ãoduasvezes,vamosperceber
203

## Página 216

9.2. Providerdecacheesuasconfigurações CasadoCódigo
que,apartirdasegunda,asconsultasparamdeserfeitas.Semprequevocê
pensaremcachedesegundonível,comeceanotandoasentidadesparanão
cairnestetipodeproblema.
Comaentidadeanotada,aindaganhamosdebrindeocachedaentidade
quandousamosométodo finddo EntityManager.Quandovocêtentar
acessarapáginadedetalhesdeumlivro,perceberáquesóaconsultados
autoresdolivrovaiserdisparada,porcontado Lazy Load,masnãomaisada
entidade.
9.2 P rovider de cache e suas configurações
Quandooptamosporusarocachedesegundonível,somosobrigadosadeci-
dirqualseráaimplementaçãousadaparamanterosdadosemmemória.Em
umsistemasendoexecutadoforadeumservidordeaplicaç ão,aop çãomais
naturaltemsidousaro EhCache.
ComoestamosrodandodentrodoWildFly,jáestamosutilizandouma
implementaçãochamada Infinispan.Nãofoinecessáriofazernenhumaconfi-
guraçãorelativaaisso,poisaimplementaç ãodo EntityManagerFactory
usadapeloWildFlyjáusao Infinispanpordefault.
Configurando o timeout
Umpontomuitorelevantesobreocacheéotempoqueosobjetosdevem
vivernele.Porexemplo,osdetalhesdeumlivropoucomudamcomopassar
dotempo. Omáximoqueaconteceéatualizaçãodedetalhesinternosdos
capítulosporcontadeumaerrata,ouatualizaç ãodetecnologia.
Pensandonessecenário,podemoscolocarumtempodeexpiraç ãobem
alto,especificamenteparaaentidade Book.OInfinispanpermitequeessas
configuraçõessejamadicionadasnopróprio persistence.xml.
<persistence-unit name="casadocodigo-persistence-unit"
transaction-type="JTA">
...
<properties>
...
204

## Página 217

CasadoCódigo Capítulo9. Melhorandoaperformancecomcache
<!-- infinispan cache -->
<property
name="hibernate.cache.infinispan.br.com.casadocodigo
.loja.models.Book.expiration.lifespan"
value= "900000"/>
</properties>
</persistence-unit>
ÉimportantenotarqueessaéumaconfiguraçãoespecíficadoInfinispan.
Casooseuprojetoutilize,porexemplo,oEhCache,aconfiguraç ãojáserá
diferente.NocasoespecíficodoEhCache,elaseriafeitaemumarquivosepa-
rado,chamadode ehcache.xml.Ovalordeveserpassadoemmilissegun-
dos,porissoinformamos 900000,querepresenta15minutos.Naverdade,
podemospassarbemmais,pensandoqueoslivrosrealmentenãosãoatuali-
zadosfrequentemente.
Outropontoimportanteparasernotadoéonomedachavedeconfigu-
ração.Basicamente,eleobedeceaumtemplateimpostopeloInifinispan.
hibernate.cache.infinispan.NOME_COMPLETO_ENTIDADE
.expiration.lifespan
Caso você queira definir um tempo padrão
para qualquer entidade anotada, pode usar a op ção
hibernate.cache.infinispan.entity.expiration
.expiration.lifespan.
Existemdiversasoutrasconfiguraçõesquepodemserfeitas. Éaconse-
lhadoqueoleitoracesseolink http://bit.ly/conf-infinispan.
9.3 I nv alidação do cache por alteração
Umúltimodetalheimportantequedeveserlembradoésobreainvalidaç ão
dosdadosqueestãopresentesnocache. Porexemplo,todocachedequery
éautomaticamenteinvalidadoquandorealizamosqualqueroperaçãocomas
entidadespertencentesaocache.
Nonossocaso,quandoinserimosumnovolivro,oscachesdasqueries
relacionadasàclasse Booksãodesfeitos. Amotivaçãoésimples:amesma
205

## Página 218

9.4. Cacheandotrechosdapágina CasadoCódigo
query,apartirdeagora,podetrazerumresultadodiferentee,porcontadisso,
ocacheéinvalidado.
Umaoutrasituação,nãodeinvalidação,masdealteraçãodoestadodoca-
che,acontecequandoalteramosumobjetoqueestásendobuscadovia find.
Porexemplo,seumlivroforcolocadonocachee,posteriormente,seusdados
foremalteradosvia EntityManager,asnovasinformaçõesvãoseratualiza-
dasnocache.Comoestamosrodandodentrodeumservidordeaplicaç ão,a
alteraçãovaiserrealizadadentrodamesmatransaç ãoJTAqueoobjetotiver
sidomodificado.
9.4 C acheando trechos da página
Nesseexatomomento,onossocacheestárestritoaonossoacessoaobanco
dedados,sóquepodemosiraindaalém.Nahomedaloja,otempointeiro
processamosotrechode xhtmlresponsávelporexibiraslista,eapergunta
queficaé: por que estamos fazendo isso?
Comoessestrechosnãomudamporumbomtempo,nãotemosane-
cessidadedeficarprocessandoelessempre.OOmniFaces,bibliotecaquejá
usamosquandofoinecessáriopersonalizarasmensagensdeerrodoformu-
láriodecheckout,tambémprovêumatagutilitáriaparaguardartrechosde
páginanocache.
Vamosfazerumalevealteraçãonoarquivo site/index.xhtml.
<html xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://xmlns.jcp.org/jsf/core"
xmlns="http://www.w3.org/1999/xhtml"
xmlns:pt="http://xmlns.jcp.org/jsf/passthrough"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:o="http://omnifaces.org/ui">
....
<o:cache>
<ul id="home-highlight-collection">
<ui:repeat var="book"
value="#{homeBean.lastReleases()}">
206

## Página 219

CasadoCódigo Capítulo9. Melhorandoaperformancecomcache
<li class="col-left">
<a href="#{request.contextPath}/site
/detalhe.xhtml?id=#{book.id}"
class="block clearfix"> <img width="170"
height="240"
src="#{book.coverPath}"
alt=" #{book.title}"
title="#{book.title}"/>
<h2 class="product-title">
#{book.title}
</h2>
<small class="buy-button">
Lan&#231;amento!
</small></a>
</li>
</ui:repeat>
</ul>
</o:cache>
...
<o:cache>
<ul class="clearfix book-collection">
<ui:repeat var="book"
value="#{homeBean.olderBooks()}">
<li><a href=
"#{request.contextPath}/site/detalhe.xhtml?
id=#{book.id}" class="block clearfix" >
<h2 class="product-title">
#{book.title}
</h2>
<img width="143"
height="202"
src="#{book.coverPath}"
alt="#{book.title}"
title="#{book.title}"/><small
class="buy-button">Compre</small>
</a></li>
207

## Página 220

9.4. Cacheandotrechosdapágina CasadoCódigo
</ui:repeat>
</ul>
</o:cache>
</html>
Adicionamoso namespacedoOmniFacesnatagHTMLeusamosatag
cache.Ousoébemdireto,bastaenvolvermosotrechoquesóqueremosque
sejaexecutadoumavezcomatag cache,eamágicaestáfeita.OOmniFaces
vaiexecutarotrechonaprimeiravezqueousuárioentrarnapáginae,apartir
dasegunda,recuperaráovalordocacheeentregaráparaoJSF.
Oleitormaisatentovaiperceberque,apartirdosegundoacesso,nem
oslogsdoHibernatesãomaisgerados.Issojustamenteporqueaexpression
languageenvolvendoo #{homeBean.metodo}nãoémaisexecutada.Por
padrão,oOmniFacesvaimanterocacheatreladoàsessãodousuárioe,caso
otrechopossaserreaproveitadoparaqualquerusuário,podemosusaroatri-
buto scope.
<o:cache scope= "application">
...
</o:cache>
Aindaépossívelespecificardiversasoutraspropriedadesnatagdecache
doOmniFaces.
•reset–vocêpodepassarumaexpressionlanguagecujoretornoéum
booleano.OOmniFacesvaidescartarocachetodavezqueaexpressão
retornar false.
•time–tempoemsegundosparaoseucacheexpirar.Essaéumapro-
priedadebemimportante,todocódigocacheadodeveriaterumacon-
figuraçãoclaradequandoelevaiexpirar.
Porfim,casosuaaplicaçãoprecisedefinirumvalorpadrãodemaneira
global,omesmopodeserfeitonoarquivo web.xml.
<context-param>
<param-name>
208

## Página 221

CasadoCódigo Capítulo9. Melhorandoaperformancecomcache
org.omnifaces.CACHE_SETTING_APPLICATION_TTL
</param-name>
<param-value>900</param-value>
</context-param>
Aquidizemosqueostrechosdecacheassociadosàaplicaç ãointeirade-
vempermanecernamemóriapor,nomáximo,15minutos.
RelembrandoqueoOmniFaceséumabibliotecaquerealmentetemmui-
toscomponentesutilitários,considere-ocomoparteintegrantedoseudiaa
diadedesenvolvimentocomoJSF.
9.5 C onclusão
Estefoiumcapítulomaiscurto,masmuitoimportante. Habilitarocache
podefazergerarumbomimpactodeperformancenasuaaplicaç ão.Noen-
tanto,sejapragmáticoefaçatestesdeperformanceparaverseoimpactoes-
peradorealmenteéoatingido.
Outropontoimportanteéquecolocarobjetos,trechosdepáginaequal-
queroutracoisanocache,muitasvezes,temavercomumadecisãodenegó-
cio.Porexemplo,naCasadoCódigo,odonodoprodutopodeterinformado
queoslivrossãoatualizadossemanalmente.Semessainformaç ão,nãopode-
ríamosterdeixadoaslistagensportantotemponamemória.
Encerrandoaspreocupações,lembre-sedequetermuitosobjetosname-
móriaincrementaoconsumo,oquepodelevar,porcontadeumusoexa-
gerado,àfaltadememóriaemalgummomento. Lembresemprededefinir
políticasdeexpiraçãodecacheparaterumcontrolemaisfinorelativoaisso.
Minhadicaéquevocênãoparedeleragora,estecapítulofoimaistran-
quiloeopróximotambémserá! Nele,vamospossibilitarqueosdadosda
nossaaplicaçãosejamexibidosporoutrostiposdeaplicações,nãoapenasna-
vegadores.
209

## Página 223

Capítulo10
Respondendomaisdeum
formato
Nossaaplicação,atéopresentemomento,lidacomrequisiçõesvindasdeum
navegador,sóqueagoravamosumpoucoalémdoquejáexistenaCasado
Código.Sitesdevendasmuitograndes,comoaAmazoneoSubmarino,além
deexporemosseusprodutos,fazemparceriascomoutrossitesparaqueessas
outrasaplicaçõestambémpossamexibi-los.
10.1 E xpondo os dados em outros formatos
Quandofalamosdeintegraçãocomoutrasaplicações,oprimeiropontoem
quetemosquepensaré:qualéoformatoquevamosusarpararealizarain-
tegração?

## Página 224

10.1. Expondoosdadosemoutrosformatos CasadoCódigo
Atualmente,nossaaplicaçãosóécapazderetornarpáginasparaosclien-
tes,nocasoosnavegadores,em HTML.Umoutrotipodecliente,hojejámuito
comum,sãooscelularescomAndroidouiOS.Ecomovocêjádeveesperar,
exibirdadosatravésde HTMLpodenãoseroformatoidealparaserusado
nessesaparelhos.
Paraconseguirretornarformatosderespostasdiferentes,teremosdeusar
oJAX-RS,jáqueoJSFnãosuportaoutrotipoderespostaquenãosejaHTML.
ComojáfizemostodapartedeconfiguraçãodoJAX-RS,bastaquecriemos
um Resourcepararesponderaosformatosquedesejamos.
package br.com.casadocodigo.loja.resources;
//imports
@Path("books")
public class BooksResource {
@Inject
private BookDAO bookDAO;
@GET
@Produces({ MediaType.APPLICATION_JSON})
@Path("json")
public List<Book> lastBooksJson() {
return bookDAO.lastReleases();
}
}
Percebaqueocódigofoibemdireto.Criamosummétodo,retornamosa
listadelivroseusamosaannotation @Producesparadizerqueestemétodo
suportadevolverarespostanoformatoJSON.PorcontadoCDI,maisuma
vez,podemosrecebertudooqueprecisamosinjetado.
Parafechar,usamosaannotation @Pathparadefiniroendere çobase
do Resource,eaannotation @GETparadizerqueestemétodosópodeser
acessadopormeioderequisiçõesqueusemesteverbo.
Umaperguntaquepodeficarnacabe çaé: por que o verbo de acesso só
pode ser get?Oprincipalmotivoéasemânticadaoperaç ão.Um getre-
212

## Página 225

CasadoCódigo Capítulo10. Respondendomaisdeumformato
presentaqueainforma çãoestásendobuscada,eumaconsequênciadissoé
queoclientepodefazerdiversasrequisiçõesparaesteendere ço,queelesabe
que nuncavaialteraroestadodoservidor,porexemplo.Diferentedequando
usamosum POSTparavalidaropagamento,nocapítulo 8.O POSTsempre
indicaquealgovaisercriadonoservidor,então,seoclientefazduasrequi-
siçõescomosmesmosdadosusandoesteverbo,eletemdeestarconsciente
quealgopodedarerrado.
Paratestarmossenossocódigoestáretornandoarespostaquedeveria,
podemosusaro curl.
curl -X GET "http://localhost:8080/casadocodigo/services
/books/json"
Oleitormaiscuriosoqueestátentandoexecutararequisiç ãodeveter
percebidoqueoresultadonãofoicompleto. Sófoiretornandoumlivroe,
mesmoassim,faltandoarelaçãodeautores.Vejaumexemploderesultado:
[
{
"id": 60,
"title": "JAVAEE",
"description": "Uma aplicação completa usando o que...",
"numberOfPages": 200,
"price": 50,
"author": []
}
]
Omotivoficaclaroquandovamosolharnoconsoledoservidor.
Caused by: org.hibernate.LazyInitializationException: failed to
lazily initialize a collection of role:
br.com.casadocodigo.loja.models.Book.authors,
could not initialize proxy - no Session
Fomos, novamente, surpreendidospeloLazy Load. Vamosrelembrar
comoestáométodo lastReleasesnaclasse BookDAO:
213

## Página 226

10.1. Expondoosdadosemoutrosformatos CasadoCódigo
public List<Book> lastReleases() {
TypedQuery<Book> query = manager
.createQuery(
"select b from Book b where b.releaseDate
<= now() order by b.id desc",
Book.class).setMaxResults(3);
query.setHint(QueryHints.HINT_CACHEABLE, true);
return query.getResultList();
}
Os autores só vão ser carregados no momento em que o método
getAuthorsforinvocado. Comoestesóéchamadonahoradetransfor-
maroobjetodotipo List<Book>paraJSON,oobjetonãoestáligadoao
EntityManager.Éexatamenteomesmoproblemaquetivemosnatelade
detalhesdolivro,oobjetoentranoestado detached.Paraanossasorte,a
soluçãoéamesma.Transformamosnosso ResourceemEJB Statefule
trabalhamoscomo EntityManager extended.
@Path("books")
@Stateful
public class BooksResource {
@PersistenceContext(type=PersistenceContextType.EXTENDED)
private EntityManager entityManager;
private BookDAO bookDAO;
@PostConstruct
private void loadDAO(){
this.bookDAO = new BookDAO(entityManager);
}
@GET
@Produces({ MediaType.APPLICATION_JSON})
@Path("json")
public List<Book> lastBooksJson() {
return bookDAO.lastReleases();
}
}
214

## Página 227

CasadoCódigo Capítulo10. Respondendomaisdeumformato
Denovo,pormaisqueessasoluç ãonosfaçaescreverumpoucomaisde
código,deixamostudomuitoclaro.Porsinal,esseproblematambémpode-
riatersidoresolvidoplanejandomelhorasquerieseusandomais fetch joins.
Comojádiscutimos,oladoruimdo fetchéqueasnossasqueriesficarão
maiscomplicadas.
Esteautorprefereumusoconjunto,analisandocadaumadassituações.
Casovocêtenhaumobjetomuitocomplexo,podeplanejaraqueryetrazer
sóonecessário.Casocontrário,podeapostarumpoucomaisno Lazy Load.
Antesdeavan çarmos,valeumaúltimaobservação.Sófoipossívelouso
do @Stateful,poistodo ResourcedoJAX-RSécriadoedestruídopor
requeste,comisso,égarantidoquenosso EntityManagertambémsóverá
esseescopo.Casotivéssemosumobjetocomumescopomaior,porexemplo
desessão,o EntityManage extended viveriaporumtempomaislongo,
oque,namaioriadoscasos,nãoéoqueprecisamos.
Agora,serodarmosomesmocomandoparaexecutaro request,recebe-
mosarespostacompleta!Nessemomento,nossaaplicaçãoconsegueretornar
oslivrosemJSON,alémdaspáginasHTML.
Esenossoclienteprecisardeumretornoem XML?Teríamosdecriar
outrométodoeinformarqueoretornoédotipo XML.;(
@GET
@Produces({ MediaType.APPLICATION_XML})
@Path("xml")
public List<Book> lastBooks() {
return bookDAO.lastReleases(
}
Agora,setentarmosfazerarequisiçãoparaonovoendere ço,esperamos
obtero XMLesperado.Oproblemaéque,emvezdisso,recebemosumaex-
ception.
Could not find MessageBodyWriter for response object of type:
java.util.ArrayList of media type: application/xml
215

## Página 228

10.1. Expondoosdadosemoutrosformatos CasadoCódigo
JAX-B e um pouco de burocracia
Aespecificaçãoresponsávelpordefinirasregrasdeserializaçãodeobjetos
em XML(evice-versa)éJAX-B.Aocontráriodeváriasoutrasespecificações
queforamevoluindocomopassardotempo,elaaindaexigeumaconfigura-
çãomaiordoqueadesejada.Porexemplo,percebaque,parageraro JSON,
nãoprecisamosfazernadademuitoespecial.
Seguindoaexceptionaopédaletra,entendemosquenãoconseguimos
serializarumobjetodotipo ArrayList, poisoJAX-RSnãoencontrou
ninguémcapazderealizarestetrabalho. OproblemaéqueoJAX-Bexige
queaclassedoobjetosendoserializadoutilizeumaannotationchamada
@XmlRootElement. Sóque,parandoparapensar,comovamosadicionar
umaannotationnaclasse ArrayList,teríamosdecriarumanovaclasse,
queteriaaannotationeaídeclarariaumatributodotipo ArrayList.
@XmlRootElement
public class Books {
private List<Book> list = new ArrayList<>();
}
Paraanossasorte,o RestEasy,implementaçãodoJAX-RSusadapeloWi-
dlFly,suportaquemantenhamosoretornodotipo List.Porbaixodopano,
eleenvelopaalistaretornadaemumobjetoespecíficodele.
Detodojeito,agorasomosobrigadosaanotaraclassequerepresentao
tipodalista,nessecaso,a Book.
@Entity
@Cacheable
@XmlRootElement
public class Book {
...
}
Damaneiracomoestá,jáconseguimosgerarumretornodoservidor.
Casoexecutemoso curlmaisumavez,oresultadodeveserparecidocom:
<collection>
<book>
216

## Página 229

CasadoCódigo Capítulo10. Respondendomaisdeumformato
<authors>
<id>1</id>
<name>Alberto Souza</name>
</authors>
<authors>
<id>2</id>
<name>Mauricio Aniche</name>
</authors>
<description>
...
</description>
<id>59</id>
<numberOfPages>100</numberOfPages>
<price>100.00</price>
...
</book>
<book>
...
</book>
</collection>
TemalgunsdetalhesestranhosnesseXML.Oprimeiroéonomedatag
pai, collection.EsseéjustamenteonomeatributodaclassedoRestEasy,
queservede wrapperparaanossacole ção.Nãoqueissosejaumproblema
dotamanhodomundo,mas,paraonossocenário,omelhoréqueatagse
chamasse books.Paradeixarissoflexível,oRestEasyforneceumaannota-
tion.
@GET
@Produces({ MediaType.APPLICATION_XML})
@Path("xml")
@Wrapped(element="books")
public List<Book> lastBooks() {
return bookDAO.lastReleases();
}
Aannotation @Wrappedfazotrabalhoquequeremos.Agora,sepedir-
mospeloXML,elevirácomatag bookscomoaprincipal. Éimportante
ressaltarqueessaéumaannotationdoRestEasy,enãodaespecificaç ão.Caso
217

## Página 230

10.1. Expondoosdadosemoutrosformatos CasadoCódigo
vocênãoqueirasairdaespecificação,vaiterdepartirparaacriaç ãodaclasse
wrapper,sóquemanualmente.
Outropontoestranhoéquecadaautorestáespecificadoemumatagcha-
mada authors.
<authors>
<id>1</id>
<name>Alberto Souza</name>
</authors>
<authors>
<id>2</id>
<name>Mauricio Aniche</name>
</authors>
Omaiscomumseriaalgoparecidocom:
<authors>
<author>
<id>4</id>
<name>Paulo Silveira</name>
</author>
<author>
<id>5</id>
<name>Sergio Lopes</name>
</author>
</authors>
Paraatingirmosessaestrutura,vamosprecisarusarmaisalgumasanno-
tationsdoJAX-B.
...
@XmlRootElement
@XmlAccessorType(XmlAccessType.FIELD)
public class Book {
...
@XmlElement(name="author")
@XmlElementWrapper(name="authors")
private List<Author> authors = new ArrayList<>();
218

## Página 231

CasadoCódigo Capítulo10. Respondendomaisdeumformato
...
}
A @XmlAccessorTypeéusadaparainformarmosaimplementaç ão
doJAX-Bquenossasconfiguraçõesvãoserbaseadasnosatributos. Opa-
drão é que ele busque as configurações em cima dosgetters. Já a
@XmlElementWrapperservejustamenteparadizermosquetodososob-
jetosdalistaemquestãodevemvirdentrodeumatagchamada authors.
Porfim,usamosa @XmlElementparaconfigurarquecadaobjetodotipo
Authordevavirdentrodeumatagchamadade author.
PodemoscustomizarbastanteageraçãodoXML,tudovaidependerda
necessidadedaaplicaçãoqueestiverconsumindo.Claroqueomelhorénão
precisarmosmexeremnada,masnemsempreissoépossível.
Também é importante prestar atenção no uso da annotation
@XmlElement, que influencia na geração do JSON. Antes, o nome da
propriedadequereferenciavaosautoresera authors, mesmonomedo
atributo.Agoraé author,dadaanossaconfiguração.Esteéumproblema
queaespecificaçãodoJavaEEaindaprecisaatacar:normalizarageraç ãode
JSONeXML.
10.2 C ontent negotiation
Terummétodoparacadaformatoderespostadiferenteatéfunciona,oúnico
problemaéquevocêvaiacabarcomcódigosrepetidos.Lembre-sedequeo
únicopontoquevaimudaréarepresentaçãodoretorno;alógicapararecu-
perarodadovaiseramesma.Vamostentarresolveresteproblema.
Primeiro,precisamosdeixarapenasummétodo,respondendodoisfor-
matos:
@GET
@Produces({MediaType.APPLICATION_JSON,
MediaType.APPLICATION_XML})
public List<Book> lastBooksJson() {
return bookDAO.lastReleases();
}
219

## Página 232

10.3. Simulandoumclienteparaonossoserviço CasadoCódigo
O ponto agora é: quando um cliente fizer o request para a URL
/services/books,qualformatovamosretornar? Essaéaparteinteres-
sante,oprotocoloHTTPjáforneceumjeitodelidarcomesseproblema!Ele
permitequeoclienteindiquequaloformatoderespostaqueeleprefere.
Vejaumexemploderequisiçãousandoo curl:
curl -H "Accept:application/json" -X GET
"http://localhost:8080/casadocodigo/services/books"
curl -H "Accept:application/xml" -X GET
"http://localhost:8080/casadocodigo/services/books"
Noprimeiroexemplo,fizemosumarequisiçãoindicandoquedesejamos
oretornonoformato application/json.Issoéfeitopormeiodocabe-
çalho Accept.PercebaquenosegundojáindicamosquequeremosoXML
comoformato.Essatécnicaéconhecidacomo Content Negotiation,eémuito
utilizadaemintegraçõesbaseadasnoHTTP,tambémconhecidacomoREST.
Lembre-sedequeRESTéoconceitosobreoqualoJAX-RSéfundamen-
tado.Casosejanecessárioquetodososmétodosdo Resourcesuportemos
doisformatosderesposta,podemosadicionaraannotation @Producesem
cimadaclasse.
@Path("books")
@Stateful
@Produces({MediaType.APPLICATION_JSON,
MediaType.APPLICATION_XML})
public class BooksResource {
...
}
10.3 S imulando um cliente para o nosso serviço
Paraficarmaispróximoaindadarealidade,vamoscriarumaaplicaç ãocliente
paraconsumirnossoserviço. Nãoprecisamosdemuito,simplesmentecrie
umnovo Maven projectnoseuEclipse.Osdetalhesdacriaç ãoficamporsua
conta,leitor.
Vamosporumaclassequesimulaoconsumodalistagemdoslivros.
Lembre-sedemanteroservidorrodando.
220

## Página 233

CasadoCódigo Capítulo10. Respondendomaisdeumformato
package br.com.casadocodigo.loja.client;
//imports
public class BookList {
public static void main(String[] args) {
Client client = ClientBuilder.newClient();
Response response = client.target(
"http://localhost:8080/casadocodigo/services/books")
.request(MediaType.APPLICATION_JSON).get();
System.out.println(response.readEntity(String.class));
}
}
PercebaqueusamosaAPIdoJAX-RSparafazerasrequisições. Inclu-
sive,játínhamosutilizadoessaAPIquandointegramoscomovalidadorde
pagamentosexternos.EssaAPIfoiumagrandeadiç ãoquefoifeitanaespeci-
ficação,nãoprecisamosmaisficarbuscandoentreváriasop çõesqueexistiam.
Fazemosarequisiçãoespecificandootipoderetornoesperado,nessecasoo
application/json.Fiqueàvontadeparatrocarporoutros media types.
Umoutropontoimportanteéométodo readEntity. Eleesperaque
passemosotipoquedeveráserusadoparadesserializaroJSON.Nonosso
caso,sófoinecessárioimprimirnoconsole,masvocêpoderiatercriadoo
seutipopararepresentaralistadelivros.
Lembre-sedeque,nessemomento,vocênãoestádentrodoservidor,e
simaoladodocliente;portanto,nãotemosacessoanenhumaclassequejá
foicriada.
Vejaaseguirumesbo çodocódigoquevocêpoderiacriarnoladodo
cliente:
ClientBook[] books = response.readEntity( ClientBook[].class);
Lembre-sesempredequeaclasse ClientBookteriademapeartodas
asinformaçõesrecebidasdoservidor.Paraqueessecódigofuncione,preci-
samosadicionarasdependênciasdaimplementaçãodoJAX-RS,nocaso,o
RestEasy.
221

## Página 234

10.3. Simulandoumclienteparaonossoserviço CasadoCódigo
<dependencies>
<dependency>
<groupId>org.jboss.resteasy</groupId>
<artifactId>resteasy-client</artifactId>
<version>3.0.11.Final</version>
</dependency>
<dependency>
<groupId>org.jboss.resteasy</groupId>
<artifactId>resteasy-jackson-provider</artifactId>
<version>2.3.4.Final</version>
</dependency>
</dependencies>
Pronto,comissoconseguimosconsumiroserviçonoestiloRESTqueestá
expostonanossaaplicação.Fiqueàvontadeparairalémetentarexpornovos
serviços.
Especificando o tipo de retorno na URL
O RestEasy provê uma facilidade para que possamos especificar
o formato de retorno do servidor. Basta que você adicione um
context-paramamaisno web.xml.
<context-param>
<param-name>resteasy.media.type.mappings</param-name>
<param-value>
json : application/json, xml : application/xml
</param-value>
</context-param>
Agoravocêpodeirnonavegadoe,porexemplo,acessaroendere ço
http://localhost:8080/casadocodigo/services/books.json.
222

## Página 235

CasadoCódigo Capítulo10. Respondendomaisdeumformato
10.4 C onclusão
Nestecapítulo,foiabordadoumtemaqueestáemevidência:integraç ãode
sistemasviaREST.Suportaro Content Negotiationéfundamentalparavocê
darflexibilidadeàsaplicaçõesclientessobrequalformatoelaspreferem.Ou-
tropontoimportantefoiousodaannotation @@Produces,pois,pormeio
dela,vocêvaiinformarquaissãoostiposderetornosuportadosporseuser-
viço.
Nopróximocapítulo,trabalharemosparafecharunspequenosdetalhes
relativosaofechamentodeumacompra.Porexemplo,énecessárioqueum
e-mailsejaenviadoparanotificaronossocliente!Comoestecapítulofoiaté
curto,nãodurmanopontoecontinueasuajornada.
223

## Página 237

Capítulo11
Maisdeprocessamento
assíncronocomJMS
Nossoprocessodecomprajáestábemcompleto,atétratamosdeoutrostó-
picosnosúltimosdoiscapítulos.Sóque,paraofechamentodacompraficar
aindamaispróximocomodositedaCasadoCódigo,faltoumandarmosum
e-maildefinalizaçãodecompraesimularmosopedidodageraç ãodenota
fiscal.
11.1 E nviando o e-mail de finalização
Vamoscomeçarpeloenviodoe-mail.Alógicanãotemnadadecomplicado:
assimqueovalordanossacompraforautorizado,precisamosenviarume-
mailparaousuárioquesolicitouopedido.

## Página 238

11.1. Enviandooe-maildefinalização CasadoCódigo
@Path("payment")
public class PaymentResource {
private static ExecutorService executor =
Executors .newFixedThreadPool(50);
@Context
private ServletContext ctx;
@Inject
private CheckoutDAO checkoutDao;
@Inject
private PaymentGateway paymentGateway;
@Inject
private MailSender mailSender;
@POST
public void pay(@Suspended final AsyncResponse ar,
@QueryParam("uuid") String uuid) {
String contextPath = ctx.getContextPath();
Checkout checkout = checkoutDao.findByUuid(uuid);
executor.submit(() -> {
BigDecimal total = checkout.getValue();
try {
paymentGateway.pay(total);
String mailBody = "Nova compra. Seu código
de acompanhamento é "+checkout.getUuid();
mailSender .send("compras@casadocodigo.com.br",
checkout.getBuyer().gete-mail(),
"Nova compra",
mailBody);
....
}
226

## Página 239

CasadoCódigo Capítulo11. MaisdeprocessamentoassíncronocomJMS
...
}
}
Paramantermosaclarezadonossocódigo,jáisolamosocódigodeenvio
dee-mailemumaclassechamada MailSender.
package br.com.casadocodigo.loja.infra;
//infra
@ApplicationScoped
public class MailSender {
public void send( String from,String to,String subject,
String body){
//precisamos enviar o e-mail
}
}
Especificação JavaMail
Comojáestamosfazendonodecorrerdolivro,vamosusarmaisuma
especificaçãopararesolveronossoproblema.A JavaMaildefinetudooque
precisamosquandooassuntoéenviodee-mail,eéjustamenteelaqueserá
usadapelanossaclasse MailSender.
Comoestamosdentrodeumservidordeaplicaç ão,nossoúnicotrabalho
éconfigurarodisparodoe-mail. Porém,antesdeentrarnaconfiguraç ão
específicadoservidor,vamosanalisarcomoficariaonossocódigodeenvio
emsi.
package br.com.casadocodigo.loja.infra;
import javax.annotation.Resource;
import javax.enterprise.context.ApplicationScoped;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
227

## Página 240

11.1. Enviandooe-maildefinalização CasadoCódigo
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
@ApplicationScoped
public class MailSender {
@Resource(mappedName = "java:jboss/mail/gmail")
private Session session;
public void send( String from,String to,String subject,
String body){
Message mimeMessage = new MimeMessage(session);
try {
mimeMessage .setRecipients(javax.mail.Message
.RecipientType.TO, InternetAddress.parse(to));
mimeMessage .setFrom(new InternetAddress(from));
mimeMessage .setSubject("Sua compra foi registrada");
mimeMessage .setContent(body,"text/html");
Transport.send(mimeMessage);
} catch (MessagingException e) {
throw new RuntimeException(e);
}
}
}
Respireumpoucoevamosdissecarocódigoqueacabamosdeescre-
ver. Percebaqueamontagemdoe-mailgiraemtornodoobjetodotipo
MimeMessage.Apartirdele,invocamostodososmétodosnecessáriospara
construiroe-mail:
•setRecipients–usamosparadefinirquemvaireceberose-mails;
•setFrom–definequemestáenviandooe-mail;
•setSubject–defineoassuntodoe-mail;
•setContent–ocorpodoe-mailemsi.Nonossoexemplo,informa-
mosqueestamosenviandoume-mailemHTML.
228

## Página 241

CasadoCódigo Capítulo11. MaisdeprocessamentoassíncronocomJMS
Ométodo senddaclasse Transportéusadoparaefetivamentedis-
pararoe-mail. Paraconcluir,sófaltadecifraroobjetodotipo Session,
querecebemosinjetadoassociadoumnomedaJNDI.Esseobjetorepresenta
basicamentetodanossaconfiguraçãodeenviodee-mail.
Édentrodelequeestãoguardadasinformaçõescomo:
• Loginesenhadeacessoaoservidordee-mail;
• Endereçodoservidordee-mail,porexemplo, smtp.gmail.com;
• Estilodecomunicação,sevaisercriptografadoounão.
Para que a injeção deste objeto funcione, é preciso adicionar algu-
mas configurações no arquivostandalone-full.xml, que está em
caminhoInstalacaoWildFly/standalone/configuration. Para
quenãosejanecessárionavegarportodosistemadearquivos,podemosaces-
saroarquivopormeiodopróprioEclipse.
Fig.11.1:ArquivodeconfiguraçãopeloEclispe
Éimportanteressaltarqueessapartedaconfiguraç ãoéespecíficado
WildFly. Dentrodoarquivo,procurepelo subsytemassociadoaonames-
pace jboss:domain:mail:2.0.
<subsystem xmlns="urn:jboss:domain:mail:2.0">
<mail-session name="default"
jndi-name="java:jboss/mail/Default">
<smtp-server outbound-socket-binding-ref="mail-smtp"/>
</mail-session>
</subsystem>
229

## Página 242

11.1. Enviandooe-maildefinalização CasadoCódigo
PercebaqueopróprioWildFlyjápossuiumaconfiguraç ãopadrãopara
enviodee-mail.Logo,énecessárioadicionarmosanossa.
<subsystem xmlns="urn:jboss:domain:mail:2.0">
<mail-session name="default"
jndi-name="java:jboss/mail/Default">
<smtp-server outbound-socket-binding-ref="mail-smtp"/>
</mail-session>
<mail-session name="gmail"
jndi-name="java:jboss/mail/gmail">
<smtp-server
outbound-socket-binding-ref="mail-smtp-gmail"
ssl="true" username="seuUserName"
password="seuPassword"/>
</mail-session>
</subsystem>
EstamosfazendoaconfiguraçãobaseadanoGmail,portanto,alémde
passarnossousuárioesenha,somosobrigadosainformarquetodacomu-
nicaçãoseráfeitademaneiracriptografada.Éexatamenteporissoqueadici-
onamosoatributo ssl.
Lembre-sedequeessasconfiguraçõespodemmudaremfun çãodoser-
viçodee-mailqueestiverusando,masatendênciaéqueonossoexemploseja
suficienteparaamaioriadoscasos.
Outro ponto importante a se notar é o atributojndi-nameda tag
mail-session.Ovalorpassadofoijustamenteomesmoqueoreferenciado
pormeiodonossocódigo.
@ApplicationScoped
public class MailSender {
@Resource( name = "java:jboss/mail/gmail")
private Session session;
...
}
Aannotation @Resourceserve,geralmente,parademarcarumponto
deinjeção,assimcomoa @Inject.Atendênciaéque,cadavezmais,pas-
230

## Página 243

CasadoCódigo Capítulo11. MaisdeprocessamentoassíncronocomJMS
semosausara @Inject. Oproblemaéqueaindavamosteroscasosem
queainje çãovemderecursosmapeadosvia JNDI,eéjustamenteparaessas
situaçõesquevocêusaráa@Resource.
Parafecharaconfiguraçãodoe-mail,vamosvoltarrapidamenteparao
arquivo standalone-full.xml. Natag mail-server,faltouanalisar-
mosoatributo outbound-socket-binding-ref. Elefazreferênciaao
pedaçodaconfiguraçãoondeespecificamosdetalhescomoendere çoeporta.
Essaconfiguraçãoéfeitanase ção socket-binding-group.
<socket-binding-group ...>
<socket-binding .../>
...
<outbound-socket-binding name="mail-smtp">
<remote-destination host="localhost" port="25"/>
</outbound-socket-binding>
<outbound-socket-binding name="mail-smtp-gmail">
<remote-destination host="smtp.gmail.com" port="465"/>
</outbound-socket-binding>
</socket-binding-group>
Além das que já existem, adicionamos mais uma tag
outbound-socket-binding para especificar um endereço externo
queoWildFlydeveráusar.Ovalordoatributo nameéexatamenteomesmo
doatributo outbound-socket-binding-ref.
Agora,casovocêfecheumacompra,ume-mailjáserádisparadoparao
usuárioutilizadonoprocesso.Tomesócuidadoparanãousarume-mailde
mentira,enãoveroe-mailsendoentreguenasuacaixadeentrada.
231

## Página 244

11.2. Umpoucomaissobreprocessamentoassíncrono CasadoCódigo
Jav aEE 7 e configurações independentes do servidor
Visando,cadavezmais,deixarasconfiguraçõesindependentesno
servidor, a partir do Java EE 7 foi criada uma annotation chamada
MailSessionDefinition.Configurarumenviodee-mail,pelome-
nosemtese,deveriaserresumidoacriarumaclassenosistemaeutilizar
essaannotation.
@MailSessionDefinition(name = "java:jboss/mail/gmail",
host = "smtp.gmail.com",
user="user" ,
password="password",
transportProtocol = "smtps",
from="test@gmail.com",
properties = {
"mail.smtp.port=465"
})
public class MailConfiguration {
}
Percebaquefizemosquasetodooprocessobaseadoematributosjá
definidosnaannotation.Sóaportadoservidorqueprecisouserespeci-
ficadapormeiodeumapropriedadeextra.
Oproblemaéqueessaconfiguraç ão, pelomenosnoWildFly8.2,
aindanãofuncionacorretamentee,porisso,optamosporrealizaracon-
figuraçãobaseadaemarquivosespecíficosdoservidor.
11.2 U m pouco mais sobre processamento assín-
crono
Nocapítulo8,noqualcome çamosaconcluirofechamentodacompra,usa-
mosoobjetodotipo AsyncResponseparapermitirqueoservidornão
ficassecomathreadqueatendeo requesttravadaenquantoestávamosnos
comunicandocomaoutraaplicação.
232

## Página 245

CasadoCódigo Capítulo11. MaisdeprocessamentoassíncronocomJMS
Aquidevemosprestaraten çãoemumdetalhe.Dopontodevistadousuá-
riodaCasadoCódigo,oprocessamentocontinuousíncrono,jáqueeleteve
deficaresperandopelarespostaenquantonossoprocessoestavatrabalhando.
Agora,dopontodevistadoservidor,oprocessamentofoiassíncrono,jáque
athreadqueatendeo requestfoiliberadae,sóquandoaintegraç ãofoifinali-
zada,elafoinotificadaparageraradevidarespostaparaocliente.
Alémdejáesperarpelaintegraçãocomosistemadevalidaç ãodepaga-
mento,onossousuárioagoraaindaestáesperandopeloenviodoe-maile,
tambémvaiserobrigadoaesperarpelacomunicaç ãodosistemaquegeraa
notafiscal.Vamosvercomoficariaonossocódigoagora:
@Path("payment")
public class PaymentResource {
...
@Inject
private MailSender mailSender;
@Inject
private InvoiceGenerator invoiceGenerator;
@POST
public void pay(@Suspended final AsyncResponse ar,
@QueryParam ("uuid") String uuid) {
String contextPath = ctx.getContextPath();
Checkout checkout = checkoutDao.findByUuid(uuid);
executor.submit(() -> {
BigDecimal total = checkout.getValue();
try {
paymentGateway.pay(total);
String mailBody = "Nova compra.
Seu código de acompanhamento é "+
checkout.getUuid(); mailSender
.send("compras@casadocodigo.com.br",
233

## Página 246

11.2. Umpoucomaissobreprocessamentoassíncrono CasadoCódigo
checkout.getBuyer().gete-mail(),
"Nova compra", mailBody);
invoiceGenerator.invoiceFor(checkout);
....
}
...
}
}
Para não perdermos a linha de pensamento, vamos analisar a classe
InvoiceGeneratorsónofimdocapítulo. Oproblemadessefluxoéque
apenasavalidaçãodovaloréobrigatóriaparaliberaracompra;asoutras
duasoperaçõespodemserfeitassemqueonossousuáriofiqueesperando
peloretorno.
Pararesolveresteproblema,emvezderealizaralógicademaneirasín-
crona,podemos,maisumavez,partirparaumaabordagemassíncrona.Em
vezdetravarocódigoesperandopeloenviodoe-mailegeraç ãodanotafis-
cal,simplesmenteemitimosuma mensagemnosistemainformandoqueuma
novacompraacaboudeseraprovada,otratamentoficaparadepois.
Vamosdarumaolhadaemumesbo çodecódigo:
@POST
public void pay(@Suspended final AsyncResponse ar,
@QueryParam("uuid") String uuid) {
String contextPath = ctx.getContextPath();
Checkout checkout = checkoutDao.findByUuid(uuid);
executor.submit(() -> {
BigDecimal total = checkout.getValue();
try {
paymentGateway.pay(total);
234

## Página 247

CasadoCódigo Capítulo11. MaisdeprocessamentoassíncronocomJMS
//emitimos um comunicado de nova compra
....
}
...
}
}
Aideiaéquepossamosenviarumanovamensagem,equeasclassesres-
ponsáveistratemissodemaneiraassíncrona.
11.3 U tilizando o JMS para mensageria
AespecificaçãoJMS(Java Message Service)nospossibilitajustamenteimple-
mentaressaformadetrabalhar.Basicamente,precisamosenviarumamen-
sagemquechegueparaosobjetosresponsáveisportrataroseventosdeuma
novacompra.Nonossocaso,énecessárioenviaroe-mailesolicitarageraç ão
danotafiscal.
Vamoscomeçarpelocódigodeenviodemensagem:
@Path("payment")
public class PaymentResource {
...
@Inject
private JMSContext jmsContext;
@Resource(lookup = "java:/jms/topics/checkoutsTopic")
private Destination checkoutsTopic;
@POST
public void pay(@Suspended final AsyncResponse ar,
@QueryParam ("uuid") String uuid) {
String contextPath = ctx.getContextPath();
Checkout checkout = checkoutDao.findByUuid(uuid);
JMSProducer producer = jmsContext.createProducer();
235

## Página 248

11.3. UtilizandooJMSparamensageria CasadoCódigo
executor.submit(() -> {
BigDecimal total = checkout.getValue();
try {
paymentGateway.pay(total);
producer.send(checkoutsTopic,
checkout.getUuid());
...
} catch (Exception exception) {
...
}
});
}
}
Temos alguns pontos para analisar nesse código. O objeto do
tipo JMSProducer é o responsável por enviar uma mensagem. Para
efetivamente disparar a mensagem para o sistema, usamos o método
send(destino,conteudo).
ExistemdoistiposdedestinonoJMS:
• Quandoamensagemdevesertratadaapenasumavez,usamosumdes-
tinoconhecidocomo Fila;
• Quandoamensagempodesertratadaporváriosobjetos,usamosum
destinoconhecidocomo T ópico.
Porexemplo,nonossocaso,énecessárioqueamensagemdocheckout
sejatratadapeloobjetoqueenviae-mailepelogeradordanotafiscal,então,
nessecasousamosumtópico.
Agora,casotivéssemosoptadoporvalidaropagamentoenviandouma
mensagem,serianecessárioquetalmensagemfossetratadaapenasumavez
e,paraessecenário,usarumafilaseriaoideal.
236

## Página 249

CasadoCódigo Capítulo11. MaisdeprocessamentoassíncronocomJMS
O destino no JMS é representado por meio de um objeto do tipo
Destination.Assimcomojáfizemosquandofoinecessárioreceberocon-
textodeusodoe-mail,temosdeutilizaraannotation @Resource,poisva-
mosreferenciarotópicoexpostonaJNDI.
Alémdodestino,somosobrigadosapassaroconteúdodamensagem.No
nossocaso,optamosporpassaroidentificadordacompra.Dessaforma,cada
objetoresponsávelpelotratamentodefinalizaçãodacomprapodecarregá-la
erealizarsualógica.
@Path("payment")
public class PaymentResource {
@Resource(name = "java:/jms/topics/checkoutsTopic")
private Destination checkoutsTopic;
....
Agora, sófaltaresolverotrechodecódigoresponsávelporcriarum
JMSProducer.
...
@Inject
private JMSContext jmsContext;
@Resource(lookup = "java:/jms/topics/checkoutsTopic")
private Destination checkoutsTopic;
@POST
public void pay(@Suspended final AsyncResponse ar,
@QueryParam("uuid") String uuid) {
...
JMSProducer producer = jmsContext.createProducer();
executor.submit(() -> {
...
}
}
237

## Página 250

11.3. UtilizandooJMSparamensageria CasadoCódigo
Oobjetodotipo JMSContextrepresentaoelodeconexãoentreaaplica-
çãoeainfraestruturanecessáriaparaenviarasmensagens.Éatravésdeleque
criamosumobjetodotipo JMSProducer. Pararecebê-loinjetado,pode-
mosusardiretamenteaannotation @Inject.Todoservidordeaplicaçãoé
obrigadoadisponibilizarumaimplementaçãopadrãodainterfaceedeixá-la
disponível.
Configurando o tópico
Paraqueainje çãodo Destinationfuncione,énecessárioquesejain-
formadoaoservidorqueotópicosejacriadoeexpostocomdeterminado
nomenaJNDI.Aocontráriodaconfiguraçãodo DataSourceedoe-mail,
aconfiguraçãodosdestinosdoJMS,apartirdoJavaEE7,podeserfeitainte-
gralmenteviaannotations.
package br.com.casadocodigo.loja.conf;
import javax.jms.JMSDestinationDefinition;
@JMSDestinationDefinition(
name="java:/jms/topics/checkoutsTopic",
interfaceName = "javax.jms.Topic"
)
public class ConfigureJMSDestinations {
}
Essaéasimplicidadequeestamosbuscando!Configurarumpedaçocom-
plexodosistemadeumamaneiraextremamentesimples.Oatributo name
recebeonomequeseráexpostonaJNDI.Jáoatributo interfaceNamere-
cebeonomecompletodainterfacedoJMSligadaaumtipodedestino.No
nossocaso,passamos javax.jms.Topic,massefossenecessáriotrabalhar
comumafila,bastariapassar javax.jms.Queue.Aindaépossível,quando
vocêtemváriosdestinos,configurarmúltiplosdestinos.
@JMSDestinationDefinitions({
@JMSDestinationDefinition(
238

## Página 251

CasadoCódigo Capítulo11. MaisdeprocessamentoassíncronocomJMS
...
),
@JMSDestinationDefinition(
...
)
})
public class ConfigureJMSDestinations {
}
Talvezcauseumacertaestranhezacriarumaclassecompletamentevazia.
Aquiesbarramosemumalimitaçãodalinguagem,jáqueaannotationsempre
deveestarassociadaaumcódigoJava.
11.4 R egistrando tratadores de mensagens com
MDBs
Jáadicionamososuporteaotratamentoassíncronodepartesdoprocessa-
mentodeumanovacompra.Aúnicaperguntaqueficoué:cadavezquechega
umanovacompramandamosumamensagem,masquemestátratando?Pre-
cisamosassociarobjetoscomotópicoespecificado.
Parafazermosisso,vamosrecorrerdenovoaosEJBs,sóqueagoraaum
tipoespecialchamadode Message Driven Bean(MDB).ÉumEJBespecialque
podeserassociadoaumdestinoereceberasmensagensqueforemchegando.
VamosvercomoficariaparacriarumMDBresponsávelpormandaroe-mail
dacompra.
package br.com.casadocodigo.loja.listeners.checkout;
import javax.ejb.ActivationConfigProperty;
import javax.ejb.MessageDriven;
import javax.inject.Inject;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.TextMessage;
239

## Página 252

11.4. RegistrandotratadoresdemensagenscomMDBs CasadoCódigo
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
//outros imports
@MessageDriven(activationConfig = {
@ActivationConfigProperty(
propertyName = "destinationLookup",
propertyValue = "java:/jms/topics/checkoutsTopic")
})
public class SendCheckoute-mailListener
implements MessageListener{
private Logger logger = LoggerFactory
.getLogger(SendCheckoute-mailListener.class);
@Inject
private MailSender mailSender;
@Inject
private CheckoutDAO checkoutDao;
@Override
public void onMessage(Message message) {
TextMessage text = ( TextMessage) message;
try {
Checkout checkout = checkoutDao
.findByUuid(text.getText());
String e-mailBody = "<html><body>Compra realizada
com sucesso. O código de acompanhamento é "
+ checkout.getUuid() + "</body></html>";
mailSender.send("compras@casadocodigo.com.br",
checkout.getBuyer().gete-mail(),
"Sua compra foi registrada com sucesso",
e-mailBody);
} catch (Exception e ) {
logger.error("Problema no envio do e-mail",e);
}
}
240

## Página 253

CasadoCódigo Capítulo11. MaisdeprocessamentoassíncronocomJMS
}
Precisamosinvestirumtempoparaentenderpartesdestecódigo.Vamos
começarpelousodaannotation @MessageDriven.Elaéaresponsávelpor
informaraoservidordeaplicaçãoqueestamoscriandoumnovoMDB.Sua
configuração,porém,émeiocomplicadadeolhar.
@MessageDriven(activationConfig = {
@ActivationConfigProperty(
propertyName = "destinationLookup",
propertyValue = "java:/jms/topics/checkoutsTopic")
})
Para dizer que queremos escutar as mensagens que fo-
rem chegando no tópico que configuramos, precisamos usar
a annotation @ActivationConfigProperty. Na ver-
dade, o atributo activationConfig recebe um array de
@ActivationConfigProperty. Por meio dessa annotation, vamos
passandoasinformaçõesnecessárias.
Alistadepossíveispropriedadespodeserencontradaem http://docs.
oracle.com/cd/E19798-01/821-1841/bnbpo/index.html.
Paraonossocaso,precisamosda destinationLookupparaassociaro
nomedaJNDI,ondeserábuscadaareferênciaparaonossotópico.Éimpor-
tanteressaltarqueessapropriedadeéprevistanaespecificaç ão;nãoimpor-
tandooservidorquevocêrodeocódigo,talconfiguraçãodevesersuportada.
AlémdaannotationrelativaaoMDB,tambémsomosobrigadosaimple-
mentarainterface MessageListener,quedefineométodo onMessage.É
justamenteelequevaiserinvocadotodavezqueumanovamensagemchegar.
@Override
public void onMessage(Message message) {
TextMessage text = ( TextMessage) message;
try {
241

## Página 254

11.4. RegistrandotratadoresdemensagenscomMDBs CasadoCódigo
Checkout checkout = checkoutDao
.findByUuid(text.getText());
String e-mailBody = "<html><body>Compra realizada
com sucesso. O código de acompanhamento é "
+ checkout.getUuid() + "</body></html>";
mailSender .send("compras@casadocodigo.com.br",
checkout.getBuyer().gete-mail(),
"Sua compra foi registrada com sucesso",
e-mailBody );
} catch (Exception e) {
logger.error("Problema no envio do e-mail", e);
}
}
Recebemoscomoargumentoumobjetodotipo Message,queéainter-
facemãedetodasaspossíveismensagensdoJMS.Como,nahorademandar
a mensagem, foi usado o códigoproducer.send(checkoutsTopic,
checkout.getUuid()), passando como segundo argumento uma
String,émontadoumobjetodotipo TextMessage.Comoissoégaran-
tidopelaespecificação,podemossimplesmentefazero castdamensagem
quechegaerecuperaramensagemenviada.
TextMessage text = (TextMessage) message;
try {
Checkout checkout = checkoutDao.findByUuid(text.getText());
...
}
Paracompletaroprocesso,podemoscriaroMDBresponsávelporpedir
ageraçãodanotafiscaldacompra.
package br.com.casadocodigo.loja.listeners.checkout;
//imports
@MessageDriven(activationConfig = {
@ActivationConfigProperty(
242

## Página 255

CasadoCódigo Capítulo11. MaisdeprocessamentoassíncronocomJMS
propertyName = "destinationLookup",
propertyValue =
"java:/jms/topics/checkoutsTopic")
})
public class GenerateInvoiceListener
implements MessageListener{
private Logger logger = LoggerFactory.
getLogger(GenerateInvoiceListener.class);
@Inject
private InvoiceGenerator invoiceGenerator;
@Inject
private CheckoutDAO checkoutDao;
@Override
public void onMessage(Message message) {
TextMessage text = (TextMessage) message;
try {
Checkout checkout = checkoutDao
.findByUuid(text.getText());
invoiceGenerator.invoiceFor(checkout);
} catch (JMSException e) {
logger.error("Problema na geracao
da nota fiscal {}",e);
}
}
}
Ocódigoemsinãotemnadadenovo. Oleitormaiscríticodeveaté
estarpensando: por que o e-mail e a nota fiscal não foram processados pelo
mesmo MessageListener? Oproblema,nessecaso,dedeixartodaaló-
gicanomesmolugar,équeomalfuncionamentodeumapodeinfluenciar
naoutra.Dojeitoquefizemos,mesmoqueocorraumproblemanoenviodo
e-mail,anotafiscalcontinuasendogerada.
Umaoutraquestãoéquedeixarmuitocódigodeprocessamentolongo
dentrodomesmo listenerpodefazercomqueopróprio listener
vireumgargalo,ealgumasmensagenscomecemadar timeout.Sempretente
deixá-loscomomínimoderesponsabilidadepossível,ealtamentecoesos.
243

## Página 256

11.4. RegistrandotratadoresdemensagenscomMDBs CasadoCódigo
Paraqueaclasse InvoiceGeneratornãofiqueobscura,vamosdar
umaolhadanela:
package br.com.casadocodigo.loja.services;
//imports
public class InvoiceGenerator {
public void invoiceFor(Checkout checkout) {
Client client = ClientBuilder.newClient();
InvoiceData invoiceData = new InvoiceData(checkout);
String uriToGenerateInvoice =
"http://book-payment.herokuapp.com/invoice";
Entity<InvoiceData> json = Entity.json(invoiceData);
client.target(uriToGenerateInvoice).
request().post(json, String.class);
}
}
ElausaaAPIdeclientedoJAX-RSparafazerumarequisiç ãoaumsistema
externo,parasolicitarageraçãodeumanovanotafiscal.Alémdisso,usamos
oobjetodotipo InvoiceDataparapassarasinformaçõesnecessáriaspara
ageraçãodanotafiscal.
package br.com.casadocodigo.loja.models;
import java.math.BigDecimal;
import br.com.casadocodigo.loja.models.Checkout;
public class InvoiceData {
private BigDecimal value;
private String buyere-mail;
public InvoiceData(Checkout checkout) {
this.value = checkout.getValue();
this.buyere-mail = checkout.getBuyer().gete-mail();
}
244

## Página 257

CasadoCódigo Capítulo11. MaisdeprocessamentoassíncronocomJMS
public BigDecimal getValue() {
return value;
}
public String getBuyere-mail() {
return buyere- mail;
}
}
11.5 I mplementação do JMS utilizada peloWild-
Fly
Todoserviçodemensageriaéprovidoporumoutroservidor,quegeralmente
éintegradonoservidordeaplicaçãodemodoqueaaplicaçãopossatirarpro-
veito.NocasodoWildFly,éutilizadooHornetQ(http://hornetq.jboss.org/)
.
Aideia,comovimosnodecorrerdocapítulo,étentarminimizaroaco-
plamentocomaimplementaçãodaespecificação.Detodaforma,énecessário
entenderquaisimplementaçõessãousadas,jáquevocêpodeserobrigadoa
recorreraalgumaconfiguraçãoespecífica.
11.6 C autela no uso do código assíncrono
Aexecuçãodecódigodemaneiraassíncronatendeaelevaracapacidadede
umsistemadeescalar.Comopassamosmenostempoparadarumaresposta,
jáqueboapartedelavaiserprocessadaemoutromomento,conseguimos
atendermaisrequisiçõesemumdeterminadointervalodetempo.Entretanto,
adicionamosumacertacomplexidadenosistema,pontoquesempredeveser
pesadoemqualquerdecisãoarquitetural.
Umadicadesteautoréquevocê,namaioriadasvezes,comecesempre
pensandoemumcódigomaissimples,geralmentesíncronoe,quandoneces-
sário,evoluaparaocódigoassíncrono.
245

## Página 258

11.7. Conclusão CasadoCódigo
11.7 C onclusão
Estefoiumcapítuloumpoucomaisdenso!Enquantoaespecificaç ãorelativa
aoenviodee-mailsérelativamentesimples,aJMSébemmaiscomplicada.
Lidarcomcódigoassíncronosempreéumpoucomaiscomplexoeexigemais
danossaaten ção.
Éimportantelembrardequesemprequevocêestiverdentrodeumser-
vidordeaplicação,um Message Driven Bean devesercriadoparaconse-
guirsernotificadodenovasmensagens. Outropontoimportanteéainter-
face MessageListener,quedeveserimplementadaparaqueométodo
onMessagepossaserchamadodentrodo MDB.
Minhadicaéquevocêdescanseumpoucoasuamenteparapoderpro-
cessartudoqueestudamos.Nopróximocapítulo,vamosadicionarapartede
segurançae,maisumavez,usaremosumaespecificaç ãodoJavaEE.
246

## Página 259

Capítulo12
Protegendoaaplicação
Atéagora,todasasURLsdonossosistemaestãoacessíveisportodososusuá-
rios. Algumasatésãoliberadas,comoaquelevaparaapáginainicial,que
deveexibirtodososlivros. SóquetemosalgumasURLsquenecessitamde
umusuáriologado,comoasquecompõemapartedeadministraç ãodaloja.
Podemosatéimplementartodaessapartedeseguran çanamão,mas,
comojávemsendofeitonodecorrerdolivro,vamosusarumaespecifica-
çãodoJavaEEquedefinesoluçõesparaváriasdasnecessidadesqueteremos.
Ébomsemprelembrarqueimplementarumaestratégiadeseguran çanãoé
trivial.
AlémdeforçarologinparaalgumasURLs,énecessárioterpreocupaç ão
compelomenosmaisalgunsitens,como:
• QuaisperfispodemacessarasURLs,tambémconhecidocomoautori-
zação;

## Página 260

12.1. DefinindoasregrasdeacessocomoJAAS CasadoCódigo
• URLsacessadasporváriosperfis,mascomtrechosdepáginarestritos;
• Fontesdedadosdiferentespararealizaçãodelogin.
12.1 D efinindo as regras de acesso com o JAAS
Java Authentication and Authorization Service (também conhecido como
JAAS)éjustamenteaespecificaçãodoJavacriadaparatratardapartedese-
gurançaemnossasaplicações.Inclusive,aespecificaçãodeServletstambém
jáéintegradaaessaespecificação.
Basicamente,precisamosconfiguraralgunsdetalhesparaqueosendere-
çosdanossaaplicaçãocomecemaficarprotegidos.Boapartedessaconfigu-
raçãoéfeitadiretamentenoarquivo web.xml.
<web-app xmlns:xsi=
"http://www.w3.org/2001/XMLSchema-instance" ...
...
<security-constraint>
<display-name>Administracao</display-name>
<web-resource-collection>
<web-resource-name>
administracao
</web-resource-name>
<description>
Urls que levam para paginas de administracao
</description>
<url-pattern>/livros/*</url-pattern>
<http-method>GET</http-method>
<http-method>POST</http-method>
</web-resource-collection>
<auth-constraint>
<role-name> ADMIN</role-name>
</auth-constraint>
</security-constraint>
<security-role>
<role-name>ADMIN</role-name>
</security-role>
...
</web-app>
248

## Página 261

CasadoCódigo Capítulo12. Protegendoaaplicação
Semprevamostrabalharcomoseguintepar:URLse roles.Declarare-
mosendereçosquesópodemseracessadosporcertosusuáriosdedetermi-
nadosperfis,definidosnosistema.Paracadaassociaç ãoquefornecessária,
vamosdeclararumatag security-constraintedefinirasregras.
Vamosdarumzoomnoconteúdodatag,paradeixartudocompleta-
menteclaro:
<security-constraint>
<display-name>Administracao</display-name>
<web-resource-collection>
<web-resource-name>administracao</web-resource-name>
<description>
Urls que levam para paginas de administracao
</description>
<url-pattern>/livros/*</url-pattern>
<http-method>GET</http-method>
<http-method>POST</http-method>
</web-resource-collection>
<auth-constraint>
<role-name>ADMIN</role-name>
</auth-constraint>
</security-constraint>
Atag web-resource-collectiondefineospadrõesdeendere çoque
devemserprotegidos. Nonossocaso,informamosque,paraacessarqual-
querendereçoquecomececom /livros,ousuáriodeveestarlogado.Além
disso,informamososverbosHTTPassociadosaoacesso. Paracompletar,
usamosatag auth-constraintparaindicarquaisgrupos,tambémco-
nhecidoscomo roles, podemacessarosendere çosprotegidos. Dentro
datag web-resource-collection, vocêpodeadicionarquantastags
url-patternvocêdesejar,tudovaidependerdaaplicação.
CasovocêinicieoWildFlyetenteacessaroendere çohttp://localhost:
8080/casadocodigo/livros/form.xml,perceberáqueéretornadaumapágina
embranco,escrito Forbidden.Inclusive,sehabilitaro Firebugouo Chrome
tools,vaipercebernoconsolequeostatusretornadopeloservidoré403,que
indicajustamentequevocênãotemautorizaçãoparaacessardeterminados
recursos.
249

## Página 262

12.2. Configurandooformuláriodelogin CasadoCódigo
Fig.12.1:Acessonegado
12.2 C onfigurando o formulário de login
Jácomeçamosfalandosobreosperfisautorizadosparaacessardeterminados
recursos,mascomoissoiaserpossívelsenemdemosachancedeousuário
selogar?ParaexplicarparaoJAASquenecessitamosqueousuárioprimeiro
seautentique,paradepoistentaracessoaqualquerrecurso,vamosdeclarara
tag login-configno web.xml.
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
...
<login-config>
<auth-method>FORM</auth-method>
<form-login-config>
<form-login-page>
/users/login.xhtml
</form-login-page>
<form-error-page>
/users/login.xhtml
</form-error-page>
</form-login-config>
</login-config>
<security-constraint>
...
</security-constraint>
</web-app>
250

## Página 263

CasadoCódigo Capítulo12. Protegendoaaplicação
Atag auth-methodindicaquequeremostrabalharcomumformu-
láriodelogin,ondeousuáriovaipassaroseuloginesuasenha. Jáatag
form-login-configserveparaindicarmosqualdeveserapáginadelo-
ginequaldeveserapáginaquandoaconteceralgumafalhanele.
Para o nosso caso, apontamos as duas para a mesma página. Para
que essa configuração funcione, precisamos criar a página de login em
webapp/users/login.xhtml.
<html xmlns="http://www.w3.org/1999/xhtml">
<body>
<form method="POST"
action="${request.getContextPath()}/j_security_check">
<div>
<label for="e-mail">e-mail</label>
<input type="text"
name="j_username" value="${param.j_username}"
id="e-mail"/>
</div>
<div>
<label for="password">Senha</label>
<input type="password" name="j_password"
id="password"/>
</div>
<input type="submit" value="Login" />
</form>
</body>
</html>
Oleitormaisatentodeveterestranhadooendere çoutilizadonatag
action,assimcomoosnomesdos inputs. Opontoéqueaespecifica-
çãodeServletsjáforneceaintegraç ãodeautenticaçãobaseadonoJAAS,o
servidorsóprecisasaberqualéoendere çoque,quandoacessado,devedar
inícioaoprocessodeautenticação.
Alémdisso,eletambémprecisasaberquaisparâmetrosindicamologin
easenhapassadospelousuário.Todosessesvaloressãodefinidospelaespe-
cificaçãodeServlets,enãopodemseralterados.Nofundo,tambémnãofaz
251

## Página 264

12.2. Configurandooformuláriodelogin CasadoCódigo
sentidoquerermudar,jáqueissonãoinfluenciaemnadaofuncionamento
danossaaplicação.
Oproblemaagoraéquesemprequetentamosrealizarumloginnaapli-
cação,somosbarrados.Pensandoumpoucomelhor,fazatésentido,poisnão
adicionamosnenhumasenhaparaosnossoscompradoresdalojaetambém
nãocadastramosnenhumnovousuáriocomlogin,senhaeperfisassociados.
Incrementando o domínio para refletir o modelo de segurança
Odomíniodanossaaplicaç ãoaindanãofoiatualizadopararefletiro
nossonovoesquemadeseguran ça.Oprimeiropassoéjustamenteassociaro
usuáriocomosseusrespectivosperfis.
@Entity
public class SystemUser {
...
@ManyToMany(fetch = FetchType.EAGER)
private List<SystemRole> roles = new ArrayList<>();
//getters e setters
}
Agora,precisamosdaclasse SystemRole:
package br.com.casadocodigo.loja.models;
import javax.persistence.Entity;
import javax.persistence.Id;
@Entity
public class SystemRole {
@Id
private String name;
@Deprecated //apenas para os frameworks
public SystemRole() {
}
252

## Página 265

CasadoCódigo Capítulo12. Protegendoaaplicação
public SystemRole(String name) {
this.name = name;
}
//getters e setters
}
Quandovocêsubiraaplicação,porcontadaconfiguraçãodoHibernate,
asnossastabelasjáserãoatualizadas. Agorapodemoscadastrarumnovo
usuáriocomoperfildeadministração.Podemosinseriralgunsdadosdireta-
mentepeloconsoledoMySQL.
insert into SystemUser(e-mail,password)
values ('admin@casadocodigo.com.br',
);
insert into SystemRole values('ADMIN');
insert into SystemUser_SystemRole values
(id_gerado_para_o_admin,'ADMIN');
Asenhausadafoigeradaapartirdoseguintetrechodecódigo:
package br.com.casadocodigo.loja.security;
import org.jboss.security.Base64Encoder;
public class PassGenerator {
public static void main(String[] args) throws Exception {
Base64Encoder.main(new String[]{"123456","SHA-256"});
}
}
Aclasse Base64EnconderéfornecidapelopróprioWildFly,eéútil
pararepresentarasenhausandoa Base64.Alémdisso,apósotextotersido
encodado,éaplicadooalgoritmode hash SHA-256.
Mesmocomosdadoscadastrados,aindanãoconseguimosefetuarologin
dentrodanossaaplicação.Afinaldecontas,ondefoiqueexplicamosparao
253

## Página 266

12.3. ConfigurandooLoginModuledoJAAS CasadoCódigo
servidordaaplicaçãoamaneiracomoqueremosbuscarosdadosdelogine
senhapassadosnoformulário?
12.3 C onfigurando o LoginM odule do JAAS
Paraqueonossologinsejaefetuado,éprecisoterumaclassequeconsigare-
cuperarosdadospassadospelousuárioe,dessaforma,verifiqueserealmente
esseusuárioexistenobancodedados.OJAASdefineumainterfacechamada
LoginModule,quedeveserimplementadapelaaplicação,justamentecomo
propósitonecessitado.
Paraanossasorte,estamosdentrodeumservidordeaplicaç ão,etodos
elesjáfornecemimplementaçõesprontasdessainterface,demodoafacilitar
onossotrabalho.
Configurando um LoginModule no WildFly
ParaadicionarmosomódulodeloginnoWildFly,precisamos,maisuma
vez,alteraroarquivo standalone-full.xml.Lembre-sedeacessá-lopor
meiodopróprioEclipse,paranãoprecisarnavegarportodosistemadear-
quivos.
Noarquivodeconfiguração,temosummóduloassociadoaonamespace
urn:jboss:domain:security:1.2.Percebaque,dentrodele,jáexistem
algunsdomíniosdeseguran çacompostosporumoumais login modules.
<security-domains>
<security-domain name="other" cache-type="default">
<authentication>
<login-module code="Remoting" flag="optional">
<module-option name="password-stacking"
value="useFirstPass"/>
</login-module>
<login-module code="RealmDirect" flag="required">
<module-option name="password-stacking"
value="useFirstPass"/>
</login-module>
</authentication>
</security-domain>
254

## Página 267

CasadoCódigo Capítulo12. Protegendoaaplicação
<security-domain name="jboss-web-policy"
cache-type="default">
<authorization>
<policy-module code="Delegating" flag="required"/>
</authorization>
</security-domain>
...
</security-domains>
OsquejáestãodeclaradossãousadosinternamentepeloWildFly. Por
exemplo, o security-domain de nome other é utilizado interna-
menteparaverificarascredenciaisdeacessodasaplicaçõesparaEJBsre-
motos. Elesatépodemcombinarmaisdeumlogin module. Aindano
security-domainusadopelosEJBs,existemdoismódulosdelogin.Paraa
maioriadasaplicações,apenasummódulojáésuficiente,eesseéjustamente
onossocaso.
Vamosadicionarmaisum security-domainnalistajáexistenteno
WildFly.
<security-domains>
...
<security-domain name="database-login"
cache-type="default">
<authentication>
<login-module code="Database" flag="required">
<module-option name="dsJndiName"
value="java:jboss/datasources/
casadocodigoDS"/>
<module-option name="principalsQuery"
value="select password from SystemUser
where e-mail=?" />
<module-option name="rolesQuery"
value="select roles_name,'Roles'
from SystemUser_SystemRole as
255

## Página 268

12.3. ConfigurandooLoginModuledoJAAS CasadoCódigo
user_roles inner join SystemUser as
su on su.id = user_roles.SystemUser_id
where su.e-mail = ?"/>
<module-option name="hashAlgorithm"
value="SHA-256"/>
<module-option name="hashEncoding"
value="base64"/>
</login-module>
</authentication>
</security-domain>
</security-domains>
Vamosrespirarumpoucoeentendertodaessaconfiguraç ão.Oprimeiro
detalheéqueusamosovalor Databasenoatributo code. OWildFlyjá
ofereceváriasimplementaçõesdainterface LoginModulee,quandoquere-
mosusarumadelas,fazemosareferênciaatravésdeumachavejádefinida.
Seguemalgunsexemplos:
•Database–
org.jboss.security.auth.spi.DatabaseServerLoginModule
•Ldap–
org.jboss.security.auth.spi.LdapLoginModule
•Simple–
org.jboss.security.auth.spi.SimpleServerLoginModule
•PropertiesUsers–
org.jboss.security.auth.spi.PropertiesUsersLoginModule
Possibilidades do módulo de segurança
A lista completa pode ser encontrada emhttps://docs.jboss.org/
author/display/WFLY8/Security+subsystem+configuration.
256

## Página 269

CasadoCódigo Capítulo12. Protegendoaaplicação
Outro detalhe importante é o atributoflag. Atribuímos o valor
requiredparadizerquenossousuário,obrigatoriamente,temdepassarpor
essemóduloparateracessoàparteprotegidadaaplicaç ão.
Parafecharessaparte,énecessáriodiscutirasop çõesqueforampassadas
paraomódulodelogin.Amaneiramaissimplesdejustificá-lasédandouma
olhadanocódigo-fontedaclassequeseráusadapelonossomódulo.
public class DatabaseServerLoginModule extends
UsernamePasswordLoginModule
public void initialize(Subject subject, CallbackHandler
callbackHandler, Map<String,?> sharedState,
Map<String ,?> options)
{
addValidOptions(ALL_VALID_OPTIONS);
super.initialize(subject, callbackHandler,
sharedState , options);
dsJndiName = (String) options.get(DS_JNDI_NAME);
if( dsJndiName == null )
dsJndiName = "java:/DefaultDS";
Object tmp = options.get(PRINCIPALS_QUERY);
if( tmp != null )
principalsQuery = tmp.toString();
tmp = options.get( ROLES_QUERY);
...
}
}
Dessecódigotodo,vocêprecisaperceberapenasumdetalhe:ométodo
initializerecebe,emdosargumentos,umobjetodotipo Mappormeio
davariável options.Essemapaémontadojustamenteapartirdasop ções
quepassamosnaconfiguraçãoemXML.Ométodo initializeédefinido
pelaespecificação,esempreéchamadoparainicializarosvaloresnecessários
paracada LoginModule.
Agoraficamaisclaroomotivodasop çõesquepassamosnoarquivode
configuraçãoseremnoestilo chave -> valor.Tambémqueosnomesaliusados
257

## Página 270

12.3. ConfigurandooLoginModuledoJAAS CasadoCódigo
sãoespecíficosdocontainerquevocêestiverusando.
<login-module code="Database" flag="required">
<module-option name="dsJndiName"
value="java:jboss/datasources/casadocodigoDS"/>
<module-option name="principalsQuery"
value="select password from SystemUser
where e-mail=?"/>
<module-option name="rolesQuery"
value="select roles_name,'Roles'
from SystemUser_SystemRole as user_roles
inner join SystemUser as su
on su.id = user_roles.SystemUser_id
where su.e-mail = ?"/>
<module-option name="hashAlgorithm"
value="SHA-256"/>
<module-option name="hashEncoding"
value="base64"/>
</login-module>
Agora,vamosdissecarumpoucoasop çõesparaentenderexatamenteo
quesignificacadauma:
•dsJndiName–nomeJNDIdonossodatasource,quejáestáconfi-
gurado.
•principalsQuery–SQLnecessáriopararecuperarumusuárioba-
seadonologin.Nonossocaso,foiutilizadooe-mail.
•rolesQuery–SQLnecessáriopararecuperarosperfisdedetermi-
nadousuário,baseadonoseulogin.
•hashAlgorithm–algoritmodehashquevaiseraplicadonasenha
parafazerachecagemnobanco.
258

## Página 271

CasadoCódigo Capítulo12. Protegendoaaplicação
•hashEncoding–algoritmousadopararealizaro encodingdasenha.
Um detalhe que pode chamar atenção é o uso da coluna inexistente
Rolesnaqueryquerecuperaosperfis.Aquiéapenasumdetalhemaistéc-
nicoimpostopelopróprioJAAS.Dentrodaespecificaç ão,tantoousuário
logadoquantoosperfisassociadosaelesãorepresentadoscomoclassesque
implementamainterface Principal.
OJAASnospermitequeagrupemosessesobjetoemgruposdeacesso.
Vejaalgunsexemplos:
• Usuárioadministradorquepodefazertudonosistema;
• Usuárioadministradorquenãopodedeletarlivros.
Essesgrupossãorepresentadosporimplementaçõesdainterface Group.
OWildFlylheobrigaaretornarnaqueryquecarregaosperfis,aquaisgrupos
cadaumadelaspertence.Casoaaplicaç ãonãofaçausodosgrupos,devemos
especificarumaespéciedegrupopadrão,eéexatamenteporissoqueadicio-
namosacoluna Roles.Jáapalavratemdeser Roles,porserumaexigência
doWildFly.
Associando a aplicação com um security domain
Mesmoconfigurandoonovo security-domainnoWildFly,aindanão
conseguimosefetuarologindentrodaaplicaç ão. Oúltimopassoéjusta-
menteinformarquenossaaplicaçãoprecisafazerusododomínioconfigu-
rado.Paraqueissoaconte ça,énecessárioqueoprojetocrieumarquivocha-
mado jboss-web.xml,napasta WEB-INF.
<?xml version="1.0" encoding="UTF-8"?>
<jboss-web>
<security-domain>database-login</security-domain>
</jboss-web>
Lembre-sedequeesseéumarquivoespecíficodoWildFly!
Pronto,agorajáconseguimosefetuarologindanossaaplicaç ão. Tente
acessarosendere çosqueestãoprotegidosepercebaquetudovaifuncionar
comodeveria.
259

## Página 272

12.4. Exibindoousuáriologadoeescondendotrechosdapágina CasadoCódigo
Casovocêcadastreoutrosusuárioscomoutrosperfis,configureumapá-
ginadeerrocomostatus403,no web.xml. Dessaforma,quandoalguém
tentaracessarumendere çonãopermitido,serálevadoparaumapáginain-
formativa.
Outrafuncionalidadequevocêpodeimplementaréadecadastrodeno-
vosusuáriosadministradores.Lembre-seapenasdeprotegeroseuacesso!
12.4 E xibindo o usuário logado e escondendo
trechos da página
Umdetalhecomuméexibirologindousuárionaspáginasqueeleacessa
dentrodosistema.Porexemplo,queremosexibiroe-maildelenapáginade
listagemdelivros.
<html xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://xmlns.jcp.org/jsf/core"
xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets">
<h:body>
<div>
Seja bem vindo, e-mailDoUsuario
</div>
...
</h:body>
</html>
Oproblemaé: deondevemessainformação? Naverdadetemosmais
coisasapensar.Percebaquetodaconfiguraç ãoquefizemosrelativaaoJAAS
nãoenvolveu,emnenhummomento,asclassesdonossosistema. Tudofoi
realizadousandoosarquivosdeconfiguraçãodoservidordaaplicação.
Omáximodeinformaçãoqueconseguimosrecuperardousuáriologado
éologinpassadoporeleque,nessecaso,éjustamenteoe-mail.Pararecuperar
oobjetoquecontémessainformação,podemosusardiretamenteo request.
<div>
Seja bem vindo, #{request.getUserPrincipal().getName()}
</div>
260

## Página 273

CasadoCódigo Capítulo12. Protegendoaaplicação
Casosejaapenasessaainformaç ãoquevocêprecisadoseuusuáriolo-
gado,essecódigoémaisdoquesuficiente. Oproblemaéquequasenunca
vocêquerapenasisso. Muitasvezesvamosquerersabermaisinformações,
comoonomedousuário,datadeúltimologinetc.
Paraconseguirmosfazerisso, vamosprecisarcarregarasinformações
pertinentesanossaentidadedaaplicação,nessecasoa SystemUser.Ome-
lhorjeitodefazerissoécriandoumanovaclassenaaplicaç ãoeisolandoessa
lógicaládentro.
package br.com.casadocodigo.loja.security;
//imports
@Model
public class CurrentUser {
@Inject
private HttpServletRequest request;
@Inject
private SecurityDAO securityDAO;
private SystemUser systemUser;
public SystemUser get(){
return this.systemUser;
}
@PostConstruct
private void loadSystemUser() {
Principal principal = request.getUserPrincipal();
if (principal != null ) {
this.systemUser = securityDAO
.loadUserByUsername(principal.getName());
}
}
}
Lembre-sedequeaannotation @ModeljáinformaaoCDIqueosobjetos
criadosapartirdestaclassedevemvivernoescopodeumarequisiç ãoweb,e
261

## Página 274

12.4. Exibindoousuáriologadoeescondendotrechosdapágina CasadoCódigo
quetambémdevemficarexpostosna expression language.Oobjetodotipo
Principalrepresentaousuárioqueacaboudeselogarnosistemae,como
jávimos,recuperamo-lopormeiodo request.Ométodo getNameretorna
justamenteologindousuário.
Colocamosocódigodecarregamentodentrodeummétodoanotadocom
@PostConstruct. Percebaquesócarregamosdefatoousuário,casoele
estejalogado.Paranãoficarmoscomcódigosemexplicaç ão,vamosapensar
darumaolhadanaclasse SecurityDAO.
package br.com.casadocodigo.loja.security;
//imports
public class SecurityDAO {
@PersistenceContext
private EntityManager em;
public SystemUser loadUserByUsername( String username)
throws UsernameNotFoundException {
String jpql = "select u from SystemUser u
where u.e-mail = :login";
SystemUser user = em.createQuery(jpql, SystemUser.class)
.setParameter("login", username)
.getSingleResult();
return user;
}
}
Agora,nanossapágina,bastaqueusemosoobjetoexpostopeloCDIna
expression language.
<div>
Seja bem vindo, #{currentUser.get().e-mail}
</div>
Lembre-sedequeopadrãoéexporoobjetoassociadoaumachavecom
omesmonomedaclasse,mascomaprimeiraletraminúscula.
262

## Página 275

CasadoCódigo Capítulo12. Protegendoaaplicação
Umpontoquepodeterchamadoaaten çãodoleitormaiscuriosoéofato
deaclasse CurrentUsernãousaroescopodesessão,jáqueelaguarda
referênciaparaousuárioqueacaboudelogar.Omotivoésimples:jáqueas
informaçõesdousuárioatualsãomantidasno request,optamospordeixara
nossaclassenomesmoescopo.
Apartepotencialmenteruiméquevamosfazeraquerydebuscadeusuá-
riootempotodo.Entretanto,issosóseráumproblemaseasuaaplicaç ãoreal-
mentecomeçaraapresentarproblemasdeperformance.Casooleitorprefira
usaroescopodesessão,fiqueàvontadeparaalteraraconfiguraç ãodaclasse.
Ocódigoficariaparecidocom:
@Named
@SessionScoped
public class CurrentUser implements Serializable{
...
}
Oúnicodetalheemquevocêprecisaprestaraten çãoécomoobjetocar-
regadopelo EntityManager.Umavezqueeleforfechado,oobjetoentra
noestado detached,equalquertentativade lazy loadvaigerarumaexcep-
tion. Paraessasituaçãoemespecífico,omelhorcenárioéusarumaquery
planejada,játrazendotodasasinformaçõesnecessárias.
Ousodo EntityManager extended édesencorajado,porqueoob-
jetovaificarnoescopodesessão,eaconexãocomobancoseriamantidapor
umtempomaiordoquenósgostaríamos.
Paraesteautor,manteroobjetonoescopoderequestéomaissimplese
maisprecavido.Porexemplo,casoousuáriologadoatualizealgumainforma-
ção,estajáserárefletidanopróximorequest,umavezqueestamosfazendo
ocarregamentoporrequisição.
Apenaspararelembrar:quasenuncaprecisamoscome çarapensarnaso-
luçãojáconsiderandoumrequisitodeperformance.Tenteirpelocaminho
maissimpleseanaliseosresultados.
Menu de administração na home da Loja
Agoraquetemosumaáreadeadministraçãoprotegida,podemosfacilitar
oacessoaela.Nessemomento,todasasvezesemqueousuárioqueracessar
263

## Página 276

12.4. Exibindoousuáriologadoeescondendotrechosdapágina CasadoCódigo
ocadastrodelivros,eletemdedigitaroendere çononavegador.Parafacili-
tar,vamosadicionarmaisumaop çãonomenudapáginainicialdaCasado
Código.Lembre-sedequeoarquivoéo site/index.xhtml.
<nav id="main-nav">
<ul class="clearfix">
<li><a href="#{request.contextPath}/livros/list.xhtml"
rel="nofollow">Administração</a></li>
<li><a href="/cart" rel="nofollow">
Seu carrinho
</a></li>
<li><a href="/pages/sobre-a-casa-do-codigo"
rel="nofollow"> Sobre nós
</a></li>
<li><a href="/pages/perguntas-frequentes"
rel="nofollow"> Perguntas Frequentes
</a></li>
</ul>
</nav>
Oproblemaéqueagoraqualquerusuáriopodeveressemenu,masele
sódeveserexibidoparaosadministradores. Podemosmudarumpoucoo
códigoparafazeressaverificação.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:o="http://omnifaces.org/ui"
xmlns:c="http://java.sun.com/jsp/jstl/core">
...
<nav id="main-nav">
264

## Página 277

CasadoCódigo Capítulo12. Protegendoaaplicação
<ul class="clearfix">
<c:if test="#{currentUser.hasRole('ADMIN')}">
<li><a href="#{request.contextPath}/
livros/list.xhtml"
rel="nofollow">Administração</a></li>
</c:if>
<li><a href="/cart" rel="nofollow">
Seu carrinho
</a></li>
<li><a href="/pages/sobre-a-casa-do-codigo"
rel="nofollow"> Sobre nós
</a></li>
<li><a href="/pages/perguntas-frequentes"
rel="nofollow"> Perguntas Frequentes
</a></li>
</ul>
</nav>
...
</html>
Adicionamosmaisummétodonaclasse CurrentUser,o hasRole.
package br.com.casadocodigo.loja.security;
//imports
@Model
public class CurrentUser {
@Inject
private HttpServletRequest request;
@Inject
private SecurityDAO securityDAO;
private SystemUser systemUser;
265

## Página 278

12.4. Exibindoousuáriologadoeescondendotrechosdapágina CasadoCódigo
public SystemUser get(){
return this.systemUser;
}
public boolean hasRole(String name) {
return request.isUserInRole(name);
}
@PostConstruct
private void loadSystemUser() {
Principal principal = request.getUserPrincipal();
if (principal != null) {
this.systemUser = securityDAO
.loadUserByUsername(principal.getName());
}
}
}
Aimplementaçãoémaisfácildoqueagentepoderiapensar.ComoaAPI
deServletséintegradacomoJAAS,opróprio requestjáforneceométodo
isUserInRoleparaverificarseousuárioqueselogoupossuideterminado
perfil.Lembre-sedequequandodamosinícioaoprocessodelogin,omódulo
desegurançaconfiguradonoWildFlyseráusadoeosperfisdousuárioserão
carregados.Pronto,dessaforma,garantimosqueaop çãodomenusóaparece
paraosusuáriosqueestãologadoscomoadministradores.
Apenasparanãopassarembranco,foiutilizadaatag ifdaJSTLpara
verificarmosseousuáriopossuioperfilounão.Comosótrabalhamoscom
elementosHTMLpadrão,nãoexistenenhumarestriç ãoquantoaousodessa
tag.
Paranãoperdermosofocodocapítulo,existeumtextomuitobom,um
poucoantigo,quedetalhabemamisturadetagsdaJSTLcomcomponentes
doJSF.Acesseolink http://bit.ly/jstl-jsfeentendaaindamaissobrequestões
dociclodevida.
266

## Página 279

CasadoCódigo Capítulo12. Protegendoaaplicação
12.5 C onclusão
Nestecapítulo,estudamosbastantesobreoJAAS.Apesardeserumaespeci-
ficaçãoantigaepoucoatualizada,conseguiuatendernossasnecessidadesda
nossaaplicação.Fiqueapenasatentoatodasasconfiguraçõesquefizemosno
WildFlyforamespecíficasdele,enãopodemserreaproveitadasquandovocê
forutilizaroutroservidordeaplicação.
Esseéjustamenteumdospontosquevãoseratacadosnapróximaversão
doJavaEE.AAPIdeseguran çavaisermodernizadaparaquefiquemaisfácil
deserconfigurada.Vocêpodeacompanharoandamentoem https://jcp.org/
en/jsr/detail?id=375.
Umúltimopontoquepode,noprimeiromomento,causarumpoucode
desconfiançaéofatodeosendere çosprotegidosseremespecificadosdireta-
menteno web.xml.Esse,naverdade,éocenárioideal.Tentarmantersuas
regrassimples;éomelhorquevocêpodefazer.Porexemplo,seasURLses-
tivessemcadastradasnobanco,comovocêteriacertezadequeosendere ços
necessáriosrealmenteestãoprotegidos?
Pormaisquepare çatentadordeixartudodinâmico,tentecome çarpelo
simples.CasorealmenteprecisequeasassociaçõesentreperfiseURLssejam
dinâmicas,vocêvaiterdepartirparaumasoluçãomaismanual,jáqueoJAAS
nãopossuiessafuncionalidadeprontaparauso.
Nãopareagora,nopróximocapítulovamostentarmodularizarnosso
layout,diminuindoaspartesqueserepetem!
267

## Página 281

Capítulo13
Organizaçãodolayoutem
templates
Jáimplementamosalgumasdasfuncionalidadesqueexistemdentrodosis-
temarealdositedaCasadoCódigo.Entretanto,umapartecomquenãonos
preocupamosatéagoraéemrelaçãoàorganizaçãodolayoutdaaplicação.E
esseéumpontobemrelevante,jáqueolayouttambémsofrealteraçõesdu-
ranteotempodevidadaaplicação,levando-nos,váriasvezes,aproblemasde
manutençãojustamentepornãodaradevidaimportânciaaessaparte.
Porexemplo,atualmente,entreaspáginasquejáimplementamos,temos
adeexibiçãodosdetalhesdeumlivro,aqueexibeosprodutosdocarrinhoea
quelistaoslivrosdisponíveisnaloja.Olhandocomaten çãoparaelas,vamos
perceberqueambaspossuemomesmo headere footer.
<head>

## Página 282

CasadoCódigo
...
</head>
<header id="layout-header">
...
</header>
<nav class="categories-nav">
...
</nav>
<!-- resto da página-->
<footer id="layout-footer">
...
</footer>
Aquitemosoproblemaclássicoderepetição.Casoalgumamudan çaseja
necessárianessestrechos,vamosterdesaircaç andoemtodasaspáginas.
Umamaneiracomumderesolveressasituaç ãoéutilizandoosistemade in-
cludes,quejáésuportadoemaplicaçõesJSF,pormeiodo Facelets.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:o="http://omnifaces.org/ui"
xmlns:c="http://java.sun.com/jsp/jstl/core">
<head>
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge,
chrome=1"/>
<meta name="viewport" content="width=device-width,
initial-scale=1, maximum-scale=1"/>
...
</head>
<body class="index">
<ui:include src="header.xhtml"/>
...resto da pagina
270

## Página 283

CasadoCódigo Capítulo13. Organizaçãodolayoutemtemplates
<ui:include src="footer.xhtml"/>
</body>
</html>
Atéisolamoso headereo footer,sóquesobrouesseiníciodede-
claraçãodoHTML.Aívocêpodepensar: não tem problema, é só criar mais
uma include e isso também vai estar isolado.Sóqueaíéqueentraumoutro
problema:paraumapessoanovamontarumapágina,seguindoopadrãodo
sistema,elatemdesaberdetodasessas includeseaindatemdesaberaordem!
Atendênciaésópiorar.
13.1 T emplates
Paraamenizaresseproblema,aespecificaçãodoJSFjápensouemumasolu-
ção.Aideiaéquepossamoscriarummodelodepáginaquepossaserusado
portodasasoutrastelas.Esseémaisummecanismosuportadopelo Facelets.
Vamosdarumaolhadaemcomovaificarapágina site/index.xhtml,
utilizandoessaespéciedemolde.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:o="http://omnifaces.org/ui"
xmlns:c="http://java.sun.com/jsp/jstl/core">
<ui:composition template="/site/_template.xhtml">
<ui:define name="extraCss">
<link href=
"#{request.contextPath}/resources/css
/book-collection.css" rel="stylesheet"
type="text/css" media="all" />
</ui:define>
<ui:define name="body">
<section id="index-section"
class="container middle">
271

## Página 284

13.1. Templates CasadoCódigo
...
</section>
</ui:define>
</ui:composition>
</html>
Atag compositionéusadaparaindicarquequeremosusarummodelo
padrãodepágina,tambémconhecidocomo template.Percebaqueatéusamos
umatributotambémchamado template,epassamosocaminhodoarquivo
queservirádemodeloparaaspáginasdanossaloja.
Antesdeanalisaroarquivoquevaiservirdebase,vamoscontinuarana-
lisandoasoutrastagsqueusamos. Atag definedeveserutilizadapara
informarqueapáginaatualpassaráalgunstrechosdecódigoquedevemser
usadospela master page,demodoacompletaraestruturadapágina.
•extraCss–usamosparapassaroHTMLnecessáriocomosestilos
específicosdapágina;
•body–usamosparapassaroHTMLespecíficodapáginaatual.
Podemosterquantastags defineforemnecessárias,tudovaidepender
decomootemplatefoiorganizado.Vamosagoradarumaolhadanoarquivo
site/_template.xhtmlparavercomopodemosmontaraestruturada
página.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:o="http://omnifaces.org/ui"
xmlns:c="http://java.sun.com/jsp/jstl/core"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<head>
<ui:include src="head.xhtml"/>
<ui:insert name="extraCss"/>
272

## Página 285

CasadoCódigo Capítulo13. Organizaçãodolayoutemtemplates
</head>
<body class="index">
<ui:include src="header.xhtml"/>
<ui:insert name="body"/>
<ui:include src="footer.xhtml"/>
</body>
</html>
Percebaqueéumapáginanormal,aúnicatagnovaqueusamosfoia
insert. Elaservejustamenteparademarcamosospontosdapáginaque
serãopreenchidospelapáginaqueforusaressetemplate,comofoiocasoda
site/index.xhtml.
Ovalordoatributo namedatag inserttemdeserexatamenteomesmo
doatributo namedatag define,paraqueoFaceletsconsigafazeraassoci-
açãoemontarapáginafinal.
Umúltimodetalhe,nãomenosimportante: astagsnovasqueusamos
estãodisponíveisnonamespace http://xmlns.jcp.org/jsf/facelets,quefoirefe-
renciadopeloprefixo uinanossapágina.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
...>
...
</html>
Detalhe especial sobre a tag composition
Umpontoquepodeterficadonasuacabe çafoiousodatag htmlpara
importaras taglibsqueusamosdentrodaspáginas _template.xhtmle
site/index.xhtml. Analisando,ficaparecendoqueatag htmlvaiser
renderizadaduasvezes:umapelotemplateeoutrapelapáginaespecífica.
Éjustamenteaíqueentraousodatag composition.Tudooqueestá
foradelaéignoradonomomentodarenderizaç ãodapáginae,porconta
273

## Página 286

13.1. Templates CasadoCódigo
disso,nãocorremosoriscodeterastagsduplicadasnoresultadofinal.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:o="http://omnifaces.org/ui"
xmlns:c="http://java.sun.com/jsp/jstl/core">
<!-- Tudo que tem daqui pra cima é ignorado-->
<ui:composition template="/site/_template.xhtml">
...
</ui:composition>
<!-- Tudo que tem daqui pra baixo é ignorado-->
</html>
Passando parâmetros para o template
Umoutrodetalhequetalveztenhapassadodesapercebidofoiousodo
atributo class,natag bodydotemplateprincipal.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:o="http://omnifaces.org/ui"
xmlns:c="http://java.sun.com/jsp/jstl/core"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<head>
<ui:include src="head.xhtml"/>
<ui:insert name="extraCss"/>
</head>
<body class="index">
<ui:include src="header.xhtml"/>
<ui:insert name="body"/>
<ui:include src="footer.xhtml"/>
274

## Página 287

CasadoCódigo Capítulo13. Organizaçãodolayoutemtemplates
</body>
</html>
Elasempreestáassumindoqueapáginaqueutilizaráotemplateseráa
index.xhtml. Oproblemaéquecadapáginatemasuaclasseespecífica,
porexemplo,atelacomositensdocarrinhousaaclasse cart. Esseéum
casoemquenãopodemosusaratag insert,jáquenãoqueremosdefinir
umtrechodeHTML,massimapenasumparâmetro.
Paraestetipodesituaç ão,vamosusaratag param. Vamosdaruma
olhadacomoficariaateladocarrinhodecompras:
<html xmlns:h= "http://java.sun.com/jsf/html"
xmlns:f="http://xmlns.jcp.org/jsf/core"
xmlns="http://www.w3.org/1999/xhtml"
xmlns:pt="http://xmlns.jcp.org/jsf/passthrough"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:jsf= "http://xmlns.jcp.org/jsf">
<ui:composition template="/site/_template.xhtml">
<ui:param name="bodyClass" value="cart"/>
<ui:define name="body">
...
</ui:define>
</ui:composition>
</html>
Percebaqueusamosatag paramparadefinirumparâmetrodenome
bodyClass.Agora,notemplate,bastaqueacessemosavariávelquefoide-
finida,via expression language.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:o="http://omnifaces.org/ui"
xmlns:c="http://java.sun.com/jsp/jstl/core"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<head>
<ui:include src="head.xhtml"/>
275

## Página 288

13.2. Conclusão CasadoCódigo
<ui:insert name="extraCss"/>
</head>
<body class="#{bodyClass}">
<ui:include src="header.xhtml"/>
<ui:insert name="body"/>
<ui:include src="footer.xhtml"/>
</body>
</html>
Pronto!Agoratemosumlayoutbemorganizadoeprontoparaserevo-
luído.Podemosalteraraordemdasinformações,enãoseránecessárioalterar
nenhumarquivoqueuseotemplate.Alémdisso,ostrechosdefinidospelatag
insertnãosãodepassagemobrigatória,oqueforneceaindamaisflexibili-
dade.
13.2 C onclusão
Estecapítulofoibemrápido, apenasorganizamosumpoucomaisnosso
layout. Nãousamosnenhumaespecificaçãonovaemsi,masmesmoassim
foiimportante,jáqueastelascompõemumapartefundamentaldequalquer
aplicação.
Nãopareagora,jácomeceopróximocapítuloparaquepossamosfazer
comquenossaaplicaçãosuporteváriosidiomas.
Apenas como lembrete: todos os arquivos de layout podem ser
encontrados no repositório do livro, em https://github.com/asouza/
casadocodigojavaee.
Vocêtambémpodeacessarocommitespecíficodaorganizaçãodolayout.
Ésóacessarolink http://bit.ly/commit-facelets.
276

## Página 289

Capítulo14
Internacionalização
Atéestemomento,todosostextosdaaplicaç ãoestãoescritosdiretamente
naspáginas. Porexemplo,vamosanalisaromenudenavegaç ãoda include
quecontémo headerdoprojeto.
<div id="header-content">
<nav id="main-nav">
<ul class="clearfix">
<c:if test="#{currentUser.hasRole('ADMIN')}">
<li><a href="#{request.contextPath}/livros
/list.xhtml" rel="nofollow"> Administração
</a></li>
</c:if>
<li><a href="/cart" rel="nofollow">

## Página 290

14.1. Isolandoostextosemarquivosdemensagens CasadoCódigo
Seu carrinho
</a></li>
<li><a href="/pages/sobre-a-casa-do-codigo"
rel="nofollow">
Sobre nós
</a></li>
<li><a href="/pages/perguntas-frequentes"
rel="nofollow">
Perguntas Frequentes
</a></li>
</ul>
</nav>
</div>
Todosostextosdaaplicaçãoestãoescritosdiretamentenapáginae,em
geral,talvezissonãosejaumproblema.Entretanto,ositedaCasadoCódigo
játemasuaversãointernacional,a Code Crushing.Elestêmomesmolayout
esómudamemumacoisa:todosostextossãoescritoseminglês.
14.1 I solando os textos em arquivos de mensa-
gens
Casocontinuemoscomaestratégiadeescreverostextosdiretamentenaspá-
ginas,teríamosdeduplicarcadaumadelas.Paraconseguirmos internacio-
nalizarnossaaplicação,vamosterdeisolarostextosemumnovoarquivode
propriedades,dessavezo messages.properties.
menuPrincipal_admin = Administração
menuPrincipal_seuCarrinho = Carrinho
menuPrincipal_sobre = Sobre
menuPrincipal_perguntasFrequentes = Perguntas frequentes
Usamosumnovoarquivo,jáqueooutroquecriamos,o jsf_messages,
foiconfiguradoparaterasmensagensespecíficasdoJSF,enãodaaplicaç ão
emsi.Essenovoarquivotambémdeveficarno classpathdoprojeto,por
278

## Página 291

CasadoCódigo Capítulo14. Internacionalização
issoqueeledevesercriadoem src/main/resources. Anomenclatura
emumarquivo propertiessempreéfontedediscussão.
Aquiestamosseguindooseguinte:dividimososgruposcomo _eusa-
moso camelCaseparaosnomesdositensemsi. Agoraquejáisolamosos
textosnoarquivo messages,podemosusaraschavesnasnossaspáginas.
<div id="header-content">
<nav id="main-nav">
<ul class="clearfix">
<c:if test="#{currentUser.hasRole('ADMIN')}">
<li><a href="#{request.contextPath}/livros
/list.xhtml" rel="nofollow">
menuPrincipal_admin
</a></li>
</c:if>
<li><a href="/cart" rel="nofollow">
menuPrincipal_seuCarrinho
</a></li>
<li><a href="/pages/sobre-a-casa-do-codigo"
rel="nofollow">
menuPrincipal_sobre
</a></li>
<li><a href="/pages/perguntas-frequentes"
rel="nofollow">
menuPrincipal_perguntasFrequentes
</a></li>
</ul>
</nav>
</div>
Oproblemaéqueprecisamosacessarosvaloresassociadasaessascha-
ves. Paraisso, precisamosensinaroJSFacarregaroarquivoedeixaras
chavesdisponíveisparaseremusadasnaspáginas. Vamosalteraroarquivo
faces-config.xml,paraadicionaratag resource-bundle.
279

## Página 292

14.1. Isolandoostextosemarquivosdemensagens CasadoCódigo
<application>
<message-bundle>jsf_messages</message-bundle>
<resource-bundle>
<base-name>messages</base-name>
<var>msg</var>
</resource-bundle>
</application>
A tag base-name indica a localização do arquivo, dentro
do classpath do nosso projeto. Como deixamos o arquivo em
src/main/resources, que fica na raiz doclasspath, só precisa-
mospassaronome.Atag varéutilizadaparainformaronomedavariável
queficarádisponívelparaacessarmosnaspáginas.
<div id="header-content">
<nav id="main-nav">
<ul class="clearfix">
<c:if test="#{currentUser.hasRole('ADMIN')}">
<li><a href=
"#{request.contextPath}/livros/list.xhtml"
rel="nofollow">#{msg.menuPrincipal_admin}
</a></li>
</c:if>
<li><a href="/cart" rel="nofollow">
#{msg.menuPrincipal_seuCarrinho}
</a></li>
<li><a href="/pages/sobre-a-casa-do-codigo"
rel="nofollow">
#{msg.menuPrincipal_sobre} </a></li>
<li><a href="/pages/perguntas-frequentes"
rel="nofollow">
#{msg.menuPrincipal_perguntasFrequentes}
</a></li>
</ul>
</nav>
280

## Página 293

CasadoCódigo Capítulo14. Internacionalização
</div>
Avariávelmsgguardaareferênciaparaummapacarregadocomasinfor-
maçõesdoarquivodepropriedades.Oacessoàschavespormeiodasintaxe
#{msg.chave}éapenasum syntax sugarpara #{msg[chave]}.
14.2 A ccept-Language header
Atéagora,temosapenasoarquivo messages.propertiescomostex-
tosemportuguês. Sóqueprecisamossuportarasmensagenstambémem
inglês. Parafazerisso,precisamoscriaroarquivocomaextensãodalo-
calizaçãoquequeremossuportar. Porexemplo, podemoscriaroarquivo
messages_en.properties.
menuPrincipal_admin = Admin
menuPrincipal_seuCarrinho = Shopping Cart
menuPrincipal_sobre = About
menuPrincipal_perguntasFrequentes = Frequent questions
Podemostambémcriaroarquivocomaextensão _pt.properties,
parasuportaroportuguêspadrão. ParaqueoJSFsaibaquais locales
ele deve aceitar, precisamos adicionar mais uma configuração no
faces-config.
<application>
<message-bundle>jsf_messages</message-bundle>
<resource-bundle>
<base-name>messages</base-name>
<var>msg</var>
</resource-bundle>
<locale-config>
<default-locale>pt</default-locale>
<supported-locale>en</supported-locale>
</locale-config>
</application>
Definimosqualalínguapadrãoeaindaadicionamosasoutrasquesãosu-
portadas.Aperguntaqueficaé: como o JSF descobre qual idioma o navegador
prefere?
281

## Página 294

14.3. Passandoparâmetrosnasmensagens CasadoCódigo
Fig.14.1:Headercomaop çãodelíngua
Arespostaestánocabe çalhodarequisiçãoHTTP.Percebaqueháuma
chavechamada Accept-Language,eénelaquevêmaslínguasprediletasdo
seuusuário.Nocasodonavegadordoautordestelivro,estácomoportuguês.
Tantoqueaprimeiraop çãoéo pt.Porém,casonossosistemanãosuporte
esseidioma,elefalaqueprefereo en-US.
Carregaroarquivodemensagensemfun çãodalínguadonavegadoréa
maneirapadrãodeoJSFlidarcomainternacionalizaç ão.
14.3 P assando parâmetros nas mensagens
Outrasituaçãomuitocomumnomomentodeexibirasmensagensinterna-
cionalizadaséanecessidadedequeamensagemsejaconstruídadinamica-
mente. Porexemplo,napáginadelistagemdelivros,queremosdarboas-
vindasaousuárioqueacaboudelogarnosistema.
Seja bem vindo, #{currentUser.get().email}
Vamosdeixarinclusiveessamensageminternacionalizada.Paraisso,va-
mosacrescentaraentradanoarquivodemensagens.
usuarios.bemVindo = Olá {0}
Pararepresentarosparâmetros,usamososíndices. Estatécnicajávem
suportadaporpadrãonosuporteàinternacionalizaç ãopresentenopróprio
Java.Agora,parausarnapágina,podemosusaratagdoJSF.
<h:outputFormat value="#{msg.usuarios_bemVindo}">
<f:param value= "#{currentUser.get().email}" />
</h:outputFormat>
282

## Página 295

CasadoCódigo Capítulo14. Internacionalização
Atag outputFormatdeveserutilizadasemprequevocêquiserescrever
umtextoparametrizado.Passamosotextocomosparâmetrosparaoatributo
value,efazemosusodatag paramparairdefinindoosvaloresdecada
índice. Casovocêtenhamaisdeumíndice,passeonúmeroequivalentede
tags param.
14.4 D eixe que o usuário defina a língua
Respeitaroidiomasugeridopelonavegadoréumaótimaformadetentarmos
acertaralínguapreferidapelousuário.Oproblemadessaabordageméseo
idiomaconfiguradonãoforrealmenteoseupreferido.
Nessemomento,casovocêestejaachandoquetodomundopodetrocar
issofacilmente,penseemtodasaspessoasquevocêjáconheceuquenãoti-
nhammuitoconhecimentodecomputação. Muitosusuários,porexemplo,
apesardeusaremdiariamenteumnavegador,nãosabemcomofazeressa
troca.
Umaestratégiaadotadaporalgunssiteséadeoferecerlinksparaqueo
própriousuáriopossadefiniroidiomapredileto.
283

## Página 296

14.4. Deixequeousuáriodefinaalíngua CasadoCódigo
Fig.14.2:Bandeirasdospaíses
VamosadotaramesmaabordagemparaaCasadoCódigo.Inicialmente,
vamosadicionaroslinksparaqueousuáriopossaescolher.Faremosissono
arquivo header.xhtml:.
<nav id="main-nav">
<ul class="clearfix">
<li>
<h:form>
<h:commandLink action="#{i18nBean
.changeLocale('pt')}"
value="#{msg.lingua_pt}" />
</h:form>
284

## Página 297

CasadoCódigo Capítulo14. Internacionalização
</li>
<li>
<h:form>
<h:commandLink action="#{i18nBean
.changeLocale('en')}"
value="#{msg.lingua_en}" />
</h:form>
</li>
...
</nav>
Jáatédefinimososlinkscomasactionsparaum beannosso,quevaiser
oresponsávelportrocaroidiomadaaplicação.
package br.com.casadocodigo.loja.managedbeans.admin;
//imports
@Model
public class I18nBean implements Serializable {
@Inject
private FacesContext context;
public String changeLocale(String language){
context.getApplication()
.setDefaultLocale(new Locale(language));
return "/site/index.xhtml?faces-redirect=true";
}
}
O código anterior até funciona, mas o problema é que trocamos o
localeparaaaplicaçãotoda. Naverdade,oquequeremosétrocaroidi-
omaapenasparaousodeumusuário.
Amelhormaneiradefazerissoémantendoonossobeannoescopode
sessionemvezdoescopode request,paraqueoidiomasetadosejamantido
enquantoousuárioestivernavegandopelaaplicação.
285

## Página 298

14.4. Deixequeousuáriodefinaalíngua CasadoCódigo
@Named
@SessionScoped
public class I18nBean implements Serializable {
private Locale locale;
@Inject
private FacesContext context;
public String changeLocale(String language){
this.locale = new Locale(language);
return "/site/index.xhtml?faces-redirect=true";
}
public Locale getLocale() {
return locale ;
}
}
Odetalheestranhodessecódigoéqueemmomentoalguminvocamos
ummétododaAPIdoJSF.Esseéjustamentenossotrabalho,énecessário
fazercomoqueo localeescolhidopelousuáriosejapassadoparaoJSF
emtodarequisição!Éissomesmo,oJSFnãoprovêumamaneirapadrãode
manteroidiomaescolhidoentreváriasrequisições.
Parafazerisso,podemosusaratag view. Comotodasastelasdaloja
sãobaseadasnotemplatedefinidonoarquivo _template.xhtml,podemos
alterá-loparaqueo localesejaconfiguradoparacadapágina.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:o="http://omnifaces.org/ui"
xmlns:c="http://java.sun.com/jsp/jstl/core"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<f:view locale="#{i18nBean.locale}"/>
...
Astagsdonamespace http://java.sun.com/jsf/core,cujooprefixopadrãoé
286

## Página 299

CasadoCódigo Capítulo14. Internacionalização
f,sãogeralmenteusadasquandoqueremosfazerconfiguraçõesquenãotêm
averexatamentecomapágina,massimcomalgumaconfiguraç ãodoJSF.
Oatributo localerecebecomoargumentoumobjetodotipo Locale,
justamente oque éretornado pelométodogetLocaleda nossaclasse
I18nBean.
Dessaforma,conseguimossempredefiniro localeparacadapágina
acessada,eaindapermitimosqueousuáriodaaplicaç ãooalteresempreque
quiser.
Umaúltimaperguntaquepodeestarnasuacabe çaé: e quando o usuá-
rio acessar a loja pela primeira vez, qual o locale que será usado? Para
resolverisso,podemosrecuperaroidiomapadrão,quefoiconfiguradono
faces-config,eguardarnonossoatributo.
@Named
@SessionScoped
public class I18nBean implements Serializable {
private Locale locale;
@Inject
private FacesContext context;
@PostConstruct
private void loadLDefaultLocale(){
this.locale =
context.getApplication().getDefaultLocale();
}
public String changeLocale(String language){
this.locale = new Locale(language);
return "/site/index.xhtml?faces-redirect=true";
}
public Locale getLocale() {
return locale;
}
}
287

## Página 300

14.5. Conclusão CasadoCódigo
Agora,todavezqueousuárioacessaraaplicaç ãopelaprimeiravez,ele
veráapáginaemportuguês. Casoeleprefiraoutroidioma,bastaclicarno
link!
14.5 C onclusão
Estecapítulotambémfoitranquilo.Internacionalizaçãoéumtemamuitoco-
mumentretodasasaplicações,lembre-seapenasdenãoserradical.Casovocê
nãotenhaplanosdefazeroutrasversões,nãosepreocupecomessedetalhe.
Sóouseserealmentefornecessário,afinaldecontas,vocêestádeixandode
darmanutençãosóemumlugarparadaremdois!Anteseraapenasapágina,
agoraéapáginaeoarquivodemensagens.
Nopróximocapítulo,discutiremossobreumatécnicaqueestáemevi-
dência,autilizaçãode WebSockets.Atravésdela,vamosdispararnotificações
paraonossonavegadordeumamaneiramuitosimples!Porcontadisso,não
paredeleragora,ejádevoreopróximocapítulo.
288

## Página 301

Capítulo15
Enviandoerecebendo
informaçõesviaWebSocket
Umafuncionalidadedesejadapelalojaéadepoderavisarosclientessobre
promoçõesrelâmpago.Aideiaéqueoadministradorpossadecidirquealgum
livrofiqueempromo çãoemdeterminadoinstante,equetodososusuários
queestejamemalgumapáginanaquelemomentosejamnotificados.
15.1 C omo notificar os usuários?
Aperguntaqueficananossacabe çaé: como vamos enviar alguma coisa para
a página que está sendo acessada pelo usuário, naquele instante?Umadasso-
luçõesmaisantigaseraimplementarumJavaScriptquefica,detemposem
tempos,consultandoumaURLdoservidorparasabersealgonovoaconte-

## Página 302

15.2. APIdeWebSocketseonavegador CasadoCódigo
ceu.
//exemplo usando um pouco de jquery
setInterval(function(){
$.ajax({
url: "/sales",
success: function(data){
//Atualiza o valor de cada ação na tabela
}, dataType: "json"});
}, 30000);
Poderíamoscriarum resourcedoJAX-RSqueresponderiaparaessare-
quisição. Ograndeproblemadessaabordageméqueoclienteficaotempo
inteirodisparandorequisiçãocontraoservidor,masnamaioriadasvezesnão
temnadadenovoacontecendo!Basicamente,estamosmetralhandooservi-
dorcomváriasrequisiçõesinúteis.
15.2 API de WebSockets e o navegador
Naverdade,oqueprecisamoséquequandoalgumapromo çãosejacadas-
trada,oservidornotifiqueoclientecomanovidade.Paracontornaropro-
blemadeficarfazendorequisiçãootempointeiro,aindaantigamente,osser-
vidorescomeçaramasuportarquecertasconexõesabertaspeloclientenão
fossemfechadas,técnicaconhecidacomo Comet.
Essafoiumatécnicacriadajustamenteparaosservidorescome çarema
suportarochamado Long Pollinge,dessaforma,pudessemenviarinforma-
çõesparaoclientesemanecessidadedeumanovarequisiç ão.
Poisbem,naúltimaversãodoHTML5,essetipodetécnicavirouuma
especificaçãochamada WebSocket.Sóqueelesforamalémdesóespecificaro
quejátinhapronto,eadicionaramnovosdetalhes:
• Alémdeoservidorpodernotificarocliente,oclientetambémpode
enviarinformaçõesparaoservidor;
• Acomunicaçãoéfeitabaseadaemumnovoprotocolo,chamadojusta-
mentedeWebSocket;
290

## Página 303

CasadoCódigo Capítulo15. EnviandoerecebendoinformaçõesviaWebSocket
• APIpadrãoparaserusadadentrodonavegadoremvezdeficarsimu-
landorequisiçãoAJAX.
Usando a API de WebSockets no navegador
Vamoscomeçaraimplementarnossanovafuncionalidade. Aprimeira
coisaqueprecisamoséabriroWebSocketnapáginaparapodermosman-
darereceberinformaçõespelamesmaconexão.Comoqueremosque,inde-
pendentedapágina,ousuáriosejanotificado,vamosdeixaressecódigono
_template.xhtml.
<html xmlns="http://www.w3.org/1999/xhtml"
xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
xmlns:o="http://omnifaces.org/ui"
xmlns:c="http://java.sun.com/jsp/jstl/core"
xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://java.sun.com/jsf/core">
<f:view locale="#{i18nBean.locale}"/>
<head>
<ui:include src="head.xhtml"/>
<ui:insert name="extraCss"/>
</head>
<body class="#{bodyClass}">
<ui:include src="header.xhtml"/>
<ui:insert name="body"/>
<ui:include src="footer.xhtml"/>
<script>
var salesChannel = new WebSocket(
"ws://localhost:8080/#{request.contextPath}
/channel/sales");
</script>
</body>
</html>
291

## Página 304

15.2. APIdeWebSocketseonavegador CasadoCódigo
Criamosumnovoobjetodotipo WebSocket,passandojustamenteoen-
dereçoqueprecisamosmanterolinkabertocomocliente.Perceba,inclusive,
queoprotocolousadonãoéoHTTP,esimoWS,deWebSocket.
Agoraqueaconexãoestáaberta,precisamosreceberasnovasmensagens,
queserãoenviadasapartirdoservidor.
salesChannel.onmessage = function (message) {
var newSale = JSON.parse(message.data);
if(confirm("Quer participar da seguinte promocao: "
+newSale.title+"?")){
document.location.href =
"#{request.contextPath}/site/
detalhe.xhtml?id="+newSale.bookId;
}
};
Apropriedade onMessageaceitaumfun çãoquevaiserinvocadasem-
prequeoservidorenviarumanovamensagemparaocliente. Percebaque
anossafun çãosimplesmentelevaousuárioparaateladedetalhesdolivro
como idigualaoquefoirecebidocomoargumento.AAPIdeWebSockets
émuitodireta,aabstraçãocriadapelaespecificaçãorealmentedeixoutudo
muitosimples.
Umoutrodetalhequevaleanalisarcommaiscarinhoéoformatodamen-
sagem.ElasemprechegacomoumJSONe,pormeiodapropriedade data,
conseguimosacessarotextoquefoienviadopeloservidor.
Tambéméinteressantenotaroconsoledonavegador.Quandoacessamos
umapáginaqueabreumWebSocket,arequisiçãoficaabertacomostatus101,
querepresentaaconexãoemandamento.
292

## Página 305

CasadoCódigo Capítulo15. EnviandoerecebendoinformaçõesviaWebSocket
Fig.15.1:ConexãoabertaviaWebSocket
Casovocêuseoserviçodo WhatsApp Web,abraoconsoledapáginae
percebaqueeleusaumWebSocketparaficarenviandoerecebendonovas
mensagens.
15.3 E nviando mensagens a partir do servidor
Comofoicomentado,precisamosdeumanovatelanaaplicaç ãoparapermitir
queooadministradordalojaconsigalan çarnovaspromo çõesnosistema.
Podemoscriaresseformulárioem promocoes/form.xhtml.
<html xmlns:h="http://java.sun.com/jsf/html"
xmlns:f="http://xmlns.jcp.org/jsf/core"
xmlns="http://www.w3.org/1999/xhtml"
xmlns:pt="http://xmlns.jcp.org/jsf/passthrough">
<h:body>
<h:messages />
<h:form>
<div>
<h:outputLabel>Titulo</h:outputLabel>
<h:inputText
value="#{adminSalesBean.sale.title}"
label="titulo"/>
</div>
<div>
<h:outputLabel for="livro">
Livro
</h:outputLabel>
293

## Página 306

15.3. Enviandomensagensapartirdoservidor CasadoCódigo
<h:selectOneMenu
value="#{adminSalesBean.sale.book.id}"
id="livro">
<f:selectItems
value="#{adminListBooksBean.books}"
var="book"
itemLabel="#{book.title}"
itemValue="#{book.id}"/>
</h:selectOneMenu>
</div>
<h:commandButton value="Gravar"
action="#{adminSalesBean.save}"/>
</h:form>
</h:body>
</html>
EmrelaçãoaoJSF,nãotemosnadadenovo.Odetalheinteressanteestá
apenasnousodatag selectItems.Precisamosdalistadelivroscadastra-
dos.Emvezdefazerumanovalógicaparaisso,aproveitamoso beanquejá
existe.
Lembre-sesempredequenãoexistenenhumaregraqueimpõeaneces-
sidadedecriarum beanparacadatela.Dividasuasclassesdeformaareapro-
veitarasresponsabilidades,semperderacoesão.
Alémdereaproveitaralistagemdelivros,precisamosdeumnovo bean
queseráresponsávelportratarasolicitaçãodeumanovapromo ção.
package br.com.casadocodigo.loja.managedbeans.admin;
//imports
@Model
public class AdminSalesBean {
private Sale sale = new Sale ();
@PostConstruct
private void configure() {
294

## Página 307

CasadoCódigo Capítulo15. EnviandoerecebendoinformaçõesviaWebSocket
this.sale.setBook(new Book());
}
public String save() {
//precisamos notificar os usuários sobre a promoção
return "/admin/promocoes/form.xhtml?faces-redirect=true";
}
public Sale getSale() {
return sale;
}
public void setSale(Sale sale) {
this.sale = sale;
}
}
Denovo,apenascódigosquejáestudamos!Paraquenossocódigocom-
pile,tambéménecessárioquesejacriadaaclasse Sale,aabstraçãodeuma
novapromoçãonosistema.
package br.com.casadocodigo.loja.models;
//imports
public class Sale {
private String title;
private Book book ;
public String getTitle() {
return title;
}
public void setTitle(String title) {
this.title = title ;
}
295

## Página 308

15.3. Enviandomensagensapartirdoservidor CasadoCódigo
public Book getBook() {
return book;
}
public void setBook(Book book) {
this.book = book;
}
}
Agora,sófaltaresolvermosjustamenteapartedeenviaramensagemvia
WebSocket.Umúltimodetalhe:nãoseesque çadeadicionaronovoendere ço
naconfiguraçãodoJAASnoseu web.xml.Nãoqueremosqueosusuários
quenãosãoadministradoreslancempromo çõesnosistema.
WebSockets no Java EE
Entendendoanovatendênciadasaplicaçõesweb,aespecificaçãoJavaEE
nãoperdeutempoeadicionouosuporteàcomunicaç ãoviaWebSocket. O
maislegaldetudoissoéquerealmenteficoumuitosimplessuportaressemo-
delodentrodanossaaplicação.
AnossaprimeiratarefaéadeaceitarumanovaconexãoviaWebSocket.
package br.com.casadocodigo.loja.websockets;
import javax.websocket.server.ServerEndpoint;
@ServerEndpoint("/channel/sales")
public class SalesEndpoint {
}
Éumaconfiguraçãobemparecidacomaquefazemosquandoprecisa-
mosdeum Servlet.Sóque,emvezdeusarmosaannotation @WebServlet,
usamosanovaannotation @ServerEndpoint.Tambémsomosobrigadosa
passaroendere çoemqueaconexãoviaWebSocketseráaberta.Percebaque
aURLéamesmautilizadadentrodanossapágina.
Agoraqueaconexãoestáaberta,énecessárioqueonosso beandecadas-
trodepromo çõessejacapazdemandarumamensagemparacadaclienteque
296

## Página 309

CasadoCódigo Capítulo15. EnviandoerecebendoinformaçõesviaWebSocket
abriuumnovoWebSocketnesse endpoint.Parasaberqueumanovacone-
xãofoisolicitada,bastaqueummétodosejacriadoeanotadocom @OnOpen.
...
import javax.inject.Inject;
import javax.websocket.OnOpen;
import javax.websocket.Session;
@ServerEndpoint("/channel/sales")
public class SalesEndpoint {
@Inject
private ConnectedUsers connectedUser;
@OnOpen
public void onNewUser(Session session){
connectedUser.add(session);
}
}
Podemosdarqualquernomeparaométodo,oimportanteéqueeleesteja
anotadocom OnOpen.Alémdisso,podemosreceberumparâmetrodotipo
Session,querepresentaaconexãoestabelecidaentreoclienteeoservidor.
Quandoumanovapromo çãoforlan çada,vamosprecisardetodosobjetosdo
tipo Sessionparaquepossamosnotificarcadaumdelesdonovoevento.
Umaprimeirasoluçãopoderiaserguardaresseconjuntodentrodaprópria
classe SalesEndpoint.
@ServerEndpoint("/channel/sales")
public class SalesEndpoint {
private Set<Session> remoteUsers = new HashSet<>();
@OnOpen
public void onNewUser(Session session){
remoteUsers .add(session);
}
}
297

## Página 310

15.3. Enviandomensagensapartirdoservidor CasadoCódigo
Oproblemaéqueaespecificaçãodizque,paracadanovaconexão,um
novoobjetodaclasseanotadacom @ServerEndpointserácriadoe,por
contadisso,semprevamosperderosclientesquejáestavamadicionadosno
nosso Set.
Pararesolveressasituação,podemoscriarumaoutraclassequeseráres-
ponsávelpormanterasreferênciasaosusuáriosqueestãoconectadosnaquele
momento.
package br.com.casadocodigo.loja.websockets;
//outros imports
import javax.websocket.Session;
@ApplicationScoped
public class ConnectedUsers {
private Set<Session> remoteUsers = new HashSet<>();
private Logger logger =
LoggerFactory.getLogger(ConnectedUsers.class);
public void add(Session remoteUser) {
this.remoteUsers.add(remoteUser);
}
}
O código é basicamente o mesmo que tínhamos escrito, só
que agora mantemos a lógica dentro de uma classe anotada com
@ApplicationScoped. Graças ao CDI, podemos injetar um objeto
destetipodentrodanossaclasse SalesEndpoint.
package br.com.casadocodigo.loja.websockets;
import javax.inject.Inject;
import javax.websocket.OnOpen;
import javax.websocket.Session;
import javax.websocket.server.ServerEndpoint;
298

## Página 311

CasadoCódigo Capítulo15. EnviandoerecebendoinformaçõesviaWebSocket
@ServerEndpoint("/channel/sales")
public class SalesEndpoint {
@Inject
private ConnectedUsers connectedUsers;
@OnOpen
public void onNewUser(Session session){
connectedUsers.add(session);
}
}
Comooescopodaclasse ConnectedUsersédeaplicação,conseguimos
manterumalistaúnicacomtodosusuáriosconectadosnaquelemomento.
Agoraquejátemosquasetudopronto,podemosvoltarparaonosso bean,e
finalmentedispararamensagem!
package br.com.casadocodigo.loja.managedbeans.admin;
//imports
@Model
public class AdminSalesBean {
private Sale sale = new Sale();
@Inject
private ConnectedUsers connectedUsers;
@PostConstruct
private void configure() {
this.sale.setBook(new Book());
}
public String save() {
connectedUsers.send(sale.toJson());
return "/admin/promocoes
/form.xhtml?faces-redirect=true";
}
299

## Página 312

15.3. Enviandomensagensapartirdoservidor CasadoCódigo
public Sale getSale() {
return sale;
}
public void setSale(Sale sale) {
this.sale = sale;
}
}
Apenasrecebemosinjetadooobjetodotipo ConnectedUsers,ein-
vocamosométodo sendpassandoumJSONcomoargumento.Ométodo
sendvaiseroresponsávelporenviarasmensagensparaocliente,também
viaWebSocket.
package br.com.casadocodigo.loja.websockets;
import javax.inject.Inject;
import javax.websocket.OnOpen;
import javax.websocket.Session;
import javax.websocket.server.ServerEndpoint;
@ServerEndpoint("/channel/sales")
public class SalesEndpoint {
@Inject
private ConnectedUsers connectedUsers;
@OnOpen
public void onNewUser(Session session){
connectedUsers.add(session);
}
public void send( String message) {
for (Session user : remoteUsers) {
if (user.isOpen()) {
try {
user.getBasicRemote().sendText( message);
300

## Página 313

CasadoCódigo Capítulo15. EnviandoerecebendoinformaçõesviaWebSocket
} catch (IOException e ) {
logger.error("Não foi possivel enviar
mensagem para um cliente, {}",e);
}
}
}
}
}
Ométodo getBasicRemoteretornaoobjetocapazdemandarmensa-
gensparaoclienteconectado.Porfim,ométodo sendTextéoresponsável
porenviarumamensagemnoformatotexto.
Étudotãosimplesquepareceatéestranho,mascomojámostramosdu-
ranteolivro,oJavaEEcaminhouparaumaltoníveldesimplicidade.Amai-
oriadasespecificaçõesjáestábaseadaemAPIsdeusofácil,easmaisantigas,
comooJAAS,estãosendoatualizadasparaviremmaissimplesnoJavaEE8.
Paranãoficarmoscomumcódigosemexplicaç ão,vamosapenasolharo
método toJsonnaclasse Sale.
package br.com.casadocodigo.loja.models;
import javax.json.Json;
import javax.json.JsonObjectBuilder;
import br.com.casadocodigo.loja.models.Book;
public class Sale {
private String title;
private Book book ;
//outros métodos
public String toJson() {
JsonObjectBuilder sale = Json.createObjectBuilder();
sale.add("title", this.title)
.add("bookId", this.book.getId());
301

## Página 314

15.4. OutrosdetalhesdaespecificaçãodeWebSockets CasadoCódigo
return sale.build().toString();
}
}
Apenas usamos um pouco mais da nova especificação de geração de
JSON,presentenoJavaEE7.
15.4 O utros detalhes da especificação de Web-
Sockets
Nossa funcionalidade já está implementada, vamos apenas tentar deixar
nossocódigoumpoucomelhor.Porexemplo,casoumusuáriofecheonave-
gador,asuaconexãoWebSocketseráperdida,masmesmoassimaindaman-
temosareferênciaparaelenaclasse ConnectedUsers. Omelhoréque
retiremosessecliente,paranãotermosobjetosinválidos.
@ServerEndpoint("/channel/sales")
public class SalesEndpoint {
//outros métodos
@OnClose
public void onClose(Session session,CloseReason closeReason){
connectedUsers.remove(session);
System.out.println(closeReason.getCloseCode());
}
}
Continuandonalinhadasimplicidade,bastaqueanotemosonossomé-
todocom @OnClose.Recebemosumobjetodotipo Sessionque,comojá
vimos,representaaconexãocomocliente.Alémdisso,aindapodemosrece-
berumobjetodo CloseReasonque,comoopróprionomediz,retornao
motivodaquebradaconexão.
Parafechar,casosuaaplicaçãonecessiterecebermensagensdocliente,
bastaquesejacriadoummétodoanotadocom OnMessagee,assimcomo
fizemosparaenviar,podemosreceberuma Stringcomoargumento.
302

## Página 315

CasadoCódigo Capítulo15. EnviandoerecebendoinformaçõesviaWebSocket
15.5 C onclusão
OusodeWebSocketsjáéumarealidadenasaplicações.Muitasdasqueusa-
mos(comoWhatsAppWeb,Slacketc.) usamessaAPIparapoderenviare
recebermensagensdeumservidor.Oexemplomaiscomumencontradopelo
mundoéacriaçãodeumchat,masmostramosqueaaplicaç ãodoconceito
valeparaoutrassituaçõestambém.
Caso você tenha a necessidade de usar vários WebSockets na sua
aplicação, nada impede que seja criada várias classes anotadas com
@ServerEndpoint,equetodascompartilhemdomesmoobjetodotipo
ConnectedUsers. Aúnicapreocupaçãonecessáriaéadeevoluiraclasse
ConnectedUsers,paraqueelasuporteclientesvindosde endpointsdi-
ferentes.
Vocêjáestáquasenofimdolivro!Nopróximocapítulo,serácomentado
detalhesimportantesquevocêdevelevaremconsideraçãoquandoforreali-
zarodeploydasuaaplicaç ão,alémdealgumasopiniõesimportantessobre
algumaspartesquepoderiamsermelhoresdentrodaespecificaç ão.
Minhadicaéquevocêjáfinalizeolivro,nãodeixeparaamanhãoque
vocêpodefazer agora.
303

## Página 317

Capítulo16
Últimasconsideraçõestécnicas
16.1 D eploy
Umapartemuitoimportantenavidadequalqueraplicaç ãoéasuainstalação
noambientedeprodução,momentotambémconhecidocomo deploy.Para
queodeploysejaomaisfácilpossível,idealmentetodasasconfiguraçõesde-
veriamficardentrodaprópriaaplicação,comofizemosnomomentodacon-
figuraçãodotópicodoJMS.Entretanto,asnossasconfiguraçõesdeacessoa
bancodedadoseenviodee-maileseguran çaaindaficaramnoarquivodo
próprioWildFly.
Dadoessecenário,nãovamostermuitaescapatória.Seráprecisopegar
umamáquinalimpaeinstalartudooquefornecessárioparaanossaaplicação
rodar.

## Página 318

16.1. Deploy CasadoCódigo
Opções de servidores
Estamosvivendoaépocados clouds.Criaredestruirmáquinassãoope-
raçõesqueestãoaumcliquedeumbotãoemumainterfaceweb.Vamostirar
proveitodissoeconhecertrêsboasop çõesdomercado.
Vamoscomeçarpela Amazonepela DigitalOcean. Ambasoferecem
todaainfraestruturanecessáriaparavocêcriarseusservidoreseinstalartudo
oquefornecessárioparaquesuaaplicaçãoexecute.
Comoaresponsabilidadedeinstalarecuidardossoftwaresnecessários
paraaexecuçãodosistemaédoprogramador,essetipode cloudéconhecido
como IAAS,acrônimopara Infrastructure as a Service.Esteautorgostamuito
daDigitalOcean,porcontadamaiorsimplicidade.
Uma terceira opção, especificamente para o mundo Java EE, é o
OpenShift.Alémdefornecerainfraestrutura,elestambémpossuempainéis
deconfiguraçãoemqueépossíveladicionarservidoresdeaplicaç ão,bancos
dedadosemaisumaoutragrandevariedadedesoftwares.
Nessetipode cloud,odesenvolvedorficaresponsávelapenasporenviar
ocódigo,todoorestodeveriaserderesponsabilidadedoserviçodecloud.
Oproblema,comojácomentamos,équetemosalgumasconfiguraçõesque
ficamnosarquivosdeconfigurações.Porexemplo,oOpenShiftatéresolvea
configuraçãodobancodedados,masaindanosdeixaavernaviosemrelaç ão
aoe-maileapartedeseguran ça.
Porcontadessesproblemas,esteautorprefereaindanãousaroOpenShift
comoopçãodeservidor.Dequalquerforma,essedetipode cloud,queoferece
alémdaautomatizaçãodainfraestruturademáquinas,tambémaautomati-
zaçãodainfraestruturadesoftware,éconhecidocomo PAAS,acrônimopara
Platform as a Service.Outraop çãonessalinhaéo CloudBees.
Lembre-sedequerealizarodeploynãomudamuitoemrelaç ãoaoque
vocêjávemfazendolocalmente.Vocêprecisaráterumbancodedados,um
WildFlyinstaladonamáquinadedeployeo wardasuaaplicação,paraque
vocêpossaadicionarnapasta stadalone/deploymentsdopróprioWild-
fly. Lembre-seapenasdecriaro DataSourcedeproduçãocomomesmo
nomequevocêcriouodedesenvolvimento.
306

## Página 319

CasadoCódigo Capítulo16. Últimasconsideraçõestécnicas
Dependências necessárias
Parageraroarquivo wardedeployusandooMaven,énecessárioquero-
demosocomando caminhoParaMaven/bin/mvn package.Oproblema
éque,quandoexecutamosessalinha,recebemososseguinteserrosnocon-
sole:
Fig.16.1:Problemadecompilação
Acontecerammuitomaiserrosdoqueoexibido,masessetrechojános
passaumaideia.OMavennãoestáconseguindoencontrarasdependências
necessáriasparacompilarnossocódigo.
ComoadicionamosoWildFlynonossoprojeto,dentrodoEclipse,esse
problemaficoumascarado. Sóquequandovamoscompilardiretopeloter-
minal,énecessáriotertodosos jarsnecessáriosparaquetudofuncione.
Pararesolveressaquestão,bastaqueasdependênciasnecessáriassejamadi-
cionadasno pom.xml.
<!-- javaee7 api -->
<dependency>
<groupId>javax</groupId>
<artifactId>javaee-api</artifactId>
<version>7.0</version>
<scope>provided</scope>
</dependency>
<dependency>
<groupId>org.picketbox</groupId>
<artifactId>picketbox</artifactId>
307

## Página 320

16.1. Deploy CasadoCódigo
<version>4.9.2.Final</version>
<scope>provided</scope>
</dependency>
<dependency>
<groupId>org.hibernate</groupId>
<artifactId>hibernate-validator</artifactId>
<version>5.2.0.Final</version>
<scope>provided</scope>
</dependency>
<dependency>
<groupId>org.jboss.resteasy</groupId>
<artifactId>resteasy-jaxb-provider</artifactId>
<version>3.0.11.Final</version>
<scope>provided</scope>
</dependency>
<dependency>
<groupId>org.hibernate</groupId>
<artifactId>hibernate-core</artifactId>
<version>4.3.10.Final</version>
<scope>provided</scope>
</dependency>
<dependency>
<groupId>org.hibernate</groupId>
<artifactId>hibernate-entitymanager</artifactId>
<version>4.3.10.Final</version>
<scope>provided</scope>
</dependency>
Percebaquedeixamosoescopodetodasessasnovasdependênciascomo
provided,justamenteparaexplicaraoMavenqueelassãoúteisnacompi-
lação,masquenãodevemserempacotadasno warfinal.
308

## Página 321

CasadoCódigo Capítulo16. Últimasconsideraçõestécnicas
16.2 P rofiles
Nãoéanormaltermosinformaçõesquevariamentreosambientesqueexecu-
tamosonossocódigo:configuraçõesdebancodedados,classesqueprecisam
sercarregadasetc.OmundoJavaEEaindacarecedeumaespecificaç ãoque
adicioneapartede environmentànossaaplicação.
Os alternativesdoCDIaindasãoconfiguradosviaXML,oquenosdeixa
compoucaflexibilidadeparaindicarqualoambientequeestásendoexecu-
tadonomomento.AtéexisteumainiciativadaApachecomoprojetoTamaya
(http://tamaya.incubator.apache.org/),masaindaestamoslongedetertodas
asespecificaçõesligadasaumaespecificaçãodeambiente,comoelasjáestão
ligadasaoCDI.
16.3 T estes
Outropontoqueaindadeixaadesejardentrodaespecificaç ãoJavaEEéo
apoioparaociclodetestesdanossaaplicaç ão.Talvez,nãosejanemrespon-
sabilidadedaespecificação,mascomotodososcomponentesdonossocódigo
são,dealgumaforma,ligadosaoJavaEE,eramaisdoquejustoquetivéssemos
algumaajudanessaárea.
PrecisamosiniciarcontextosdoCDI,criaredestruirbasesdedados,tes-
tarinvocaçãodemétodosnosbeansdoJSFourecursosdoJAX-RS,enfim,
umaáreaqueaindapodeserbemexplorada.
16.4 P rojetos paralelos que podem nos ajudar
Natentativadefecharalgunsdosburacosquecitamosnestecapítulo,alguns
projetosforamcriadospelacomunidade:
•DeltaSpike:umconjuntodebibliotecasquepodemajudaremvárias
partesdoprojeto.Porexemplo,elestêmumaimplementaçãodeprofi-
les.
•Arquillian:aideiaéfacilitarostestesintegradoscomocontainer.Por
maisquetenhaseuvalor,aindaémuitocomplexoe,naopiniãodeste
autor,maisatrapalhadoqueajuda.
309

## Página 322

16.5. Conclusão CasadoCódigo
Essesdoisprojetosjáestãobemfamosos.ODeltaSpikerealmentepode
terseuvalor,jáqueeleseaventuraemáreasqueaindanãoestãotãofortesna
especificação.Comocomentado,eletrazumaimplementaç ãoparaapartede
profiles,assimcomotentaajudar,porexemplo,napartedetestes.
16.5 C onclusão
Ésempreimportanteterumolharcríticosobretodasassoluçõesqueusamos.
OconjuntodetecnologiasprovidaspeloJavaEEaindacarecedemelhorias
emalgunspontos. Mesmoassim,aversão7daespecificaç ãotrouxemuitas
facilidades,comovimosnodecorrerdolivro. Valemuitoapenautilizá-la,
desdeprojetossimplesatécomplexos,jáqueasAPIsestãomuitofáceisde
seremaproveitadas.
Estefoioúltimocapítulotécnicodolivro! Nopróximo,aproveitopara
agradeceravocêpelacompanhiaetambémdeixomeuscontatos,paraque
nãopercamosaamizade!
310

## Página 323

Capítulo17
Horadepraticar
Muitoobrigadoporterficadocomigodurantetodaajornadadolivro! É
muitoimportantequevocêtentepraticartudooquefoiestudado.
Hojeemdia,nomundoJava,asduasmelhoresplataformasdedesenvol-
vimentosãooJavaEEeoSpring.Sejapragmático,tenteconhecerbemdos
doismundosetenhaasinformaçõesnecessáriasparatomaramelhordecisão
noseuprojeto.
Apenasparadarumpanorama,adisputaestámuitoacirrada.Enquanto
oSpringtemcomponentesmaisbemconectadosetrazcoisascomoProfile
efacilidadesparatestes;oJavaEE7forneceAPIsparatrabalhoscomplexos,
masquesãoexpostasdemaneiramuitosimplesparaoprogramador.
Tudodependerádasnecessidadesdaaplicaçãoedasrestrições,quemui-
tasvezessãoimpostaspelosclientes.Nãosejaapaixonado,crieumatabelade
decisãoevejaquaissãoospontosnecessários,providospelosdoislados,que
podemlheauxiliarparaseguircomomelhorcaminhotécnico.

## Página 324

17.1. Estudamosmuitosassuntos! CasadoCódigo
Paraconcluir,émuitoimportantequevocêcontinueestudando! Faç a
maisprojetos,leiaasespecificações,ajudeaspessoasnosfórunsetudomais.
Todafontedeaprendizadovaiserimportantenomomentoemqueasituaç ão
complicadachegar.
17 .1 E studamos muitos assuntos!
Conseguimosumfeitoquaseraro,usamosdiversasespecificaçõessemfor çar
abarraemnenhumlugar.Tudoquefoiutilizadoteveummotivoepoderia
seraplicadocasovocêestivesseconstruindoqualqueroutraaplicação.
Porsinal,apenasrefor çando,esteautorrecomendafortementequevocê
refaçaaaplicaçãointeira,ouquepegueumaoutraaplicaç ãodequevocêgosta
etenteconstruirumasimilar.
Quetaltentarimplementarváriasfuncionalidadesdofacebook? Aque-
lasatualizaçõesdoscomentáriosdospostsparecemserumótimocasopara
autilizaçãodeWebSockets. Existemváriasaplicaçõesquepodemservirde
inspiração!
17 .2 M antenha contato
Estoucompletamentedisponívelparaajudá-loondeforpossível.Vocêpode
meachardasseguintesformas:
• Pore-mail,bastaenviarumamensagemparalivrojavaee@gmail.com;
• CasouseoTwitter,ésóacessarhttps://twitter.com/alberto_souza;
• AindaháapossibilidadedeacompanharmeusprojetospeloGitHub,
bastaacessar https://github.com/asouza.
• Casoqueirapostarumadúvidaeaindaajudaroutraspessoas,useo
fórumcriadoespecialmenteparaolivro,disponívelem https://groups.
google.com/forum/#!forum/livro-javaee.
Porúltimo,todoequalquerfeedbacksobreolivroébem-vindo. Useo
fórumoumandediretamenteparameue-mail. Escrevê-lofoiumgrande
desafio,esperoqueeletenhasidodealgumavaliaparavocê.
312