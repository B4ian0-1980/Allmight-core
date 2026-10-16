---json
{
  "id": "mongodb_construa_novas_aplica__es_com_novas_tecnologias",
  "title": "MongoDB Construa novas aplicações com novas tecnologias",
  "categoria": "03-linguagens",
  "subcategoria": "go",
  "resumo": "**Arquivo Original:** `MongoDB Construa novas aplicações com novas tecnologias.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "com",
    "construa",
    "linguagens",
    "mongodb",
    "novas",
    "tecnologias"
  ],
  "perguntas_tipo": [
    "Como utilizar MongoDB Construa novas aplicações com novas tecnologias?",
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

# MongoDB Construa novas aplicações com novas tecnologias

> **Arquivo Original:** `MongoDB Construa novas aplicações com novas tecnologias.pdf`
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
Agradeçoavocêporpensarforadacaixaeescolherumaexcelentealternativa
àtecnologiade1970:osbancosrelacionais!
Agradeçotambématodasaspessoasquesededicamaosoftwarelivre,
poissemelasnãoteríamosexcelentessistemasoperacionais,bancodedados,
servidoresdeaplica ção,browsers,ferramentasetudomaisdeótimaquali-
dade.
Agradeçoàminhaesposaporsempreestaraomeulado,aosmeuspaise
aDeusportudo.
Esegueojogo!
i

## Página 4

CasadoCódigo
Prefácio
Porqueconstruiraplicaçõesnovascomtecnologiaantiga?
Éimpressionantecomoaprendemosoquebancosdedadosrelacionais
sãoeoquenãosão,enãohánadaquepossaserfeitosobreisso.Suaaplicaç ão
podeusaramaisnovatecnologiaexistente,masquandoforpersistirosdados,
necessitarádobancodedadosrelacionalusandoamesmatecnologiadosanos
setenta.Existeespaçoparatodose,comcerteza,emvárioscasososbancosde
dadosNoSQLcomooMongoDBsesobressaememrelaç ãoaostradicionais
bancosrelacionais.
Públicoalvo
Esselivrofoifeitoparadesenvolvedoresdesistemasqueusambancosde
dadosrelacionaiseprocuramalternativasmelhores.Tambémfoiescritopara
osinteressadosemaprendersobreoMongoDB,queéomaisfamosoemais
usadobancodedadosNoSQL,paraexplicarporqueasgrandesempresas
estãoinvestindoterabytesnessatecnologia.
NositedoMongoDB,temosumaexcelentedocumentaç ão,que,noen-
tanto,apenasexplicacomoocomandofuncionaenãofaznenhumacom-
paraçãocomoSQLquetododesenvolvedorconhece.Aqui,caroleitor,você
sempreencontraráumcomparativocomoSQLrelacionalquevaifacilitar
muitoofuncionamentoeasvantagensdoMongoDB.
Quickstart–aprimeirapartedolivro
Pararapidamenteconfiguraroseuambiente,disponibilizaroseubanco
dedadosMongoDBmodeladocorretamenteparaasuaaplicaç ãonãoserá
v

## Página 5

CasadoCódigo
precisolertodososcapítulos,apenasoscincoprimeiros.
Melhorandoseubancodedados–asegundapartedolivro
Oscapítulosrestantescomplementamcomapartedemigraç ãodeoutro
bancodedadosparaoMongoDb,performance,administraç ão,comandos
avançadosdebuscaeutilizaçãodeparticionamentoecluster.
Apêndices-instalaçãoeFAQ
Foramcriadosdoisapêndicesfocadoseminstalação:oapêndiceA,que
éparainstalaçãodobancodedadosdoMongoDB,eoapêndiceB,paraa
ferramentaclienteRoboMongo. Existetambémumterceiroapêndice,com
asperguntaserespostasmaisfrequentessobreoMongoDB,porexemplo,se
elesuportatransaçõesouquaisasgrandesempresasqueousam.
Código-fonte
Ocódigo-fontedestelivroestádisponívelnoendere çohttps://github.
com/boaglio/mongodb-casadocodigo,ondeforamcriadastagsparacadaum
doscapítulos,parafacilitaracompreensãodaevoluç ãodonossosistemade
filmes.
vi

## Página 6

CasadoCódigo Sumário
Sumário
1 Porquecriaraplicaç õesnovascomconceitosantigos? 1
1.1 Osistemanamaneiratradicional . . . . . . . . . . . . . . . . 2
1.2 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2 JSONveioparaficar 7
2.1 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3 MongoDBbásico 11
3.1 Conceitos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.2 AcessandooMongoDB . . . . . . . . . . . . . . . . . . . . . . 13
3.3 ExemplodaMega-Sena . . . . . . . . . . . . . . . . . . . . . . 14
3.4 Buscarregistros . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.5 Adicionarregistros . . . . . . . . . . . . . . . . . . . . . . . . 21
3.6 Atualizarregistros . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.7 Removerregistros . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.8 Criareremovercollections . . . . . . . . . . . . . . . . . . . . 33
3.9 Alterandoumacolunadeumacollection . . . . . . . . . . . . 34
3.10 Melhorandoasbuscas . . . . . . . . . . . . . . . . . . . . . . . 35
3.11 CappedCollection. . . . . . . . . . . . . . . . . . . . . . . . . 39
3.12 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4 Schemadesign 41
4.1 Relacionandoumacollectionparamuitas . . . . . . . . . . . 43
4.2 Relacionandomuitascollectionparamuitas . . . . . . . . . . 45
vii

## Página 7

Sumário CasadoCódigo
4.3 Tudoemumacollection . . . . . . . . . . . . . . . . . . . . . 45
4.4 Schemadesignnaprática . . . . . . . . . . . . . . . . . . . . . 45
4.5 Protótipo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.6 SistemaMeusfilmesrelacional . . . . . . . . . . . . . . . . . . 48
4.7 SistemaMeusfilmesnoMongoDB . . . . . . . . . . . . . . . 50
4.8 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 51
5 ConversandocomMongoDB 53
5.1 Osistemadeseriados . . . . . . . . . . . . . . . . . . . . . . . 53
5.2 SeriadosemPHP . . . . . . . . . . . . . . . . . . . . . . . . . 54
5.3 Java . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
5.4 PlayFramework . . . . . . . . . . . . . . . . . . . . . . . . . . 69
5.5 RubyonRails . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
5.6 Node.js . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
5.7 Qt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
5.8 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 77
6 Migrandooseubancodedados 79
6.1 IMDBsimplificado . . . . . . . . . . . . . . . . . . . . . . . . 79
6.2 Migrandodeumbancodedadosrelacional . . . . . . . . . . 84
6.3 Migrandoparanuvem . . . . . . . . . . . . . . . . . . . . . . 86
6.4 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 95
7 Buscasavançadas 97
7.1 Operadoresdecomparação. . . . . . . . . . . . . . . . . . . . 98
7.2 Operadordistinct . . . . . . . . . . . . . . . . . . . . . . . . . 99
7.3 Expressõesregulares . . . . . . . . . . . . . . . . . . . . . . . . 100
7.4 Operadoreslógicos . . . . . . . . . . . . . . . . . . . . . . . . 100
7.5 Operadoresunários . . . . . . . . . . . . . . . . . . . . . . . . 101
7.6 OperadorestiloLIKE . . . . . . . . . . . . . . . . . . . . . . . 102
7.7 Incrementandovalores . . . . . . . . . . . . . . . . . . . . . . 106
7.8 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 107
viii

## Página 8

CasadoCódigo Sumário
8 Buscageoespacial 109
8.1 Obancodedados . . . . . . . . . . . . . . . . . . . . . . . . . 109
8.2 Usandoosistemaweb . . . . . . . . . . . . . . . . . . . . . . . 112
8.3 Entendoosistemaweb . . . . . . . . . . . . . . . . . . . . . . 113
8.4 Indoalém . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
8.5 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 115
9 AggregationFramework 117
9.1 PorquenãousarMapReduce . . . . . . . . . . . . . . . . . . 117
9.2 ExplorandooAggregationFramework . . . . . . . . . . . . . 119
9.3 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 126
10 Aumentandoaperformance 127
10.1 Criarumíndice . . . . . . . . . . . . . . . . . . . . . . . . . . 129
10.2 Listarosíndicescriados . . . . . . . . . . . . . . . . . . . . . . 130
10.3 Removerumíndicecriado . . . . . . . . . . . . . . . . . . . . 130
10.4 Índicetextual. . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
10.5 Criaríndiceembackground . . . . . . . . . . . . . . . . . . . 133
10.6 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 134
11 MongoDBparaadministradores 135
11.1 Ajustedeperformance . . . . . . . . . . . . . . . . . . . . . . 135
11.2 Gerenciandoespaçoemdisco. . . . . . . . . . . . . . . . . . 136
11.3 Autenticação . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
11.4 Programasexternos . . . . . . . . . . . . . . . . . . . . . . . . 140
11.5 Backup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
11.6 Restore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
11.7 Exibiroperaçõesrodando. . . . . . . . . . . . . . . . . . . . . 146
11.8 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 146
12 MongoDBemcluster 149
12.1 Altadisponibilidade. . . . . . . . . . . . . . . . . . . . . . . . 149
12.2 Testandodoisreplicasets . . . . . . . . . . . . . . . . . . . . . 150
12.3 Particionamento. . . . . . . . . . . . . . . . . . . . . . . . . . 152
12.4 Próximospassos . . . . . . . . . . . . . . . . . . . . . . . . . . 159
ix

## Página 9

Sumário CasadoCódigo
13 Continueseusestudos 161
14 ApêndiceA.InstalandoMongoDB 163
15 ApêndiceB.Robomongo 177
16 ApêndiceC.Perguntaserespostas 193
x

## Página 10

Capítulo1
Porquecriaraplicaçõesnovas
comconceitosantigos?
Nasúltimasdécadas,acriaçãodeumsistemaevoluiuapenasdeumlado,
odainterfacecomousuário,come çandocomsistemasnaarquiteturade
cliente/servidor,comoosfeitosemVisualBasicouDelphi,atésistemasem
trêscamadas,comoamaioriadossitesnaInternet,feitosemPHP,Javaou
ASP,eterminandonossistemacomcelular.
Deumlado,ateladesktopevoluiuparaatelawebe,finalmente,paraa
teladocelular,masportrásdetodaselasquasesempreestavaalgumbanco
dedadosrelacional.
Sesemprefoiassim,énaturalque,aoprojetarmosumsistema,sempreas-
sumimosqueoladodosdados,dainformação,dapersistência,nãovaimudar
suasregrastãocedo,portanto,desenhamosoproblemaemcimadasregras

## Página 11

1.1. Osistemanamaneiratradicional CasadoCódigo
(oulimitações)relacionaiseapartirdelescriamosumacamadademanipu-
laçãodessesdadospelanossaaplicaç ão,sejaeladesktop,weboumobile.
1.1 Osistema na maneira tradicional
O nosso sistema é a lista de ganhadores do prêmio IgNobel (http://
pt.wikipedia.org/wiki/Anexo: Lista_de_ganhadores_do_Prêmio_IgNobel),
comoo“sucessonotreinodepombosparadistinguirementrepinturasde
PicassoeMonet”,ou“depenagemdegalinhascomomeiodemediraveloci-
dadedoventodeumtornado”.
PelalistadaWikipedia,conseguimossepararquatroinformações: ano,
tipo,autoredescriçãodoprêmio.
Partindoparamodelagemrelacional,temosomodelodafigura 1.1.
Basicamente,pegamosasquatroinformaçõesecriamosumatabelapara
cadaum,ecomoumprêmioIgNobelpodeterváriosautores,criamosuma
tabelaauxiliar premio_autor.
Fig.1.1:Modelorelacionaldosganhadores
2

## Página 12

CasadoCódigo Capítulo1. Porquecriaraplicaçõesnovascomconceitosantigos?
Vamoslistaralgumasreflexõessobreessemodelo:
1) aomontarmosomodelo,pensamosemdesnormalizartodainformaç ão,
isolandoemquatrotabelasdistintas;
2) comoummesmoprêmiopodeterváriosautores,precisamoscriaruma
tabelaauxiliar premio_autor;
3) montamos toda estrutura baseada nas limitações de um banco de
dados (no mundo real não existe representação da tabela auxiliar
premio_autor);
4) nãopensamosnoqueaaplicaçãovaifazer,pensamosapenasemarrumar
osdados;
5) emcasodelentidão,revemososSQLsecriamosíndices.
ParaexibirumapáginacomodaWikipedia,éprecisofazerumaconsulta
envolvendotodasastabelascriadas:
select
p.de_premio, t.de_tipo, a.de_ano ,au.nm_autor
from premio p, tipo t, ano a, premio_autor pa, autor au
where p.id_premio = pa.id_premio
and p.id_tipo = t.id_tipo
and p.id_ano = a.id_ano
and pa.id_autor = au.id_autor
ComoapáginadaWikipediatemmuitosacessos,seelestivessemfeito
damaneiraconvencional,ositecomcertezanãoseriatãorápido.
Portanto,pensandonaaplicaçãoenãonosdados,oidealseriaquetudo
estivesseorganizadodeacordocomanecessidadedonegócioenãocom for-
mas normaisdomundorelacional.
SeapáginadaWikipediaexibetudodeumavez,ocorretoseriaainfor-
maçãoestarconcentradaemapenasumlugar(umatabela).Essapráticajáé
conhecidanomundodoDataWarehouse,chamadadedesnormalizaç ão.
NoMongoDB,organizamososdadosemfun çãodaaplicação.
3

## Página 13

1.1. Osistemanamaneiratradicional CasadoCódigo
Nãotemostabelas,temosconjuntosdedadoschamados collections,
que,aocontráriodetabelas,nãotêm constraints(chaveprimária,chavees-
trangeira)enemtransações,alémdenãoteraslimitaçõesdeumatabelarela-
cional.Dentrodeumacoluna,vocêpodeterumarray,umalistadevalores,
algoimpossívelemumatabelaconvencional.
Resumindo:damaneiraconvencional,asuaaplicaç ãoobedeceàsregras
doseubancodedados;noMongoDBéocontrário: éasuaaplicaç ãoque
mandaeosdadossãoorganizadosconformeanecessidadedosistema.
NesseexemplodaWikipedia,precisamosterumacollectioncomtodas
asinformações.
Asinformaçõessãoorganizadasdessamaneira:
{
"ano" : 1992,
"tipo" : "Medicina",
"autores" : [
"F. Kanda",
"E. Yagi",
"M. Fukuda",
"K. Nakajima",
"T. Ohta",
"O. Nakata"],
"premio" : "Elucidação dos Componentes Químicos Responsáveis
pelo Chulé do Pé (Elucidation of Chemical
Compounds Responsible for Foot Malodour),
especialmente pela conclusão de que as pessoas
que pensam que têm chulé, têm, e as que pensam
que não têm, não têm."
}
Assim,emumúnicoregistrotemostodasasinformaçõesdequepre-
cisamos.
Resumindo:
• Dequantastabelasprecisamosparaexibirumprêmio?Cinco.
• Dequantascollectionsprecisamosparaexibirumprêmio?Uma.
4

## Página 14

CasadoCódigo Capítulo1. Porquecriaraplicaçõesnovascomconceitosantigos?
1.2 Próximos passos
Certifique-sedequeaprendeu:
• aenumerarasprincipaispráticasdamodelagemrelacionaltradicional;
• diferençasdamodelagemrelacionaltradicionaledoMongoDB.
Talvezexistamalgumasdúvidassobrealgunsconceitosouaplicaçõesdo
MongoDB,nãoéprecisolerolivrointeiroparaesclarecê-las, consulteo
apêndice16.
Nopróximocapítulo,vamosaprenderalinguagemusadapeloMongoDB:
oJSONetodopotencialqueelaoferece.
5

## Página 16

Capítulo2
JSONveioparaficar
Comocrescimentodeserviçosnocome çodoséculo,otráfegodeinfor-
maçõestambémaumentou,efoiprecisocriarumaformasimplesdeenviar
informaçãodeumservidorparaumwebbrowser,semanecessidadedenen-
humpluginparafuncionar(comoFlash).
Poressemotivo,DouglasCrockfordidentificouumapráticausadadesde
1996pelaNetscapecomoasoluç ãodesseproblema. Elecriouumaespeci-
ficaçãoparaelaebatizou-acomoNotaç ãodeObjetosJavaScript(JavaScript
Object Notation),ousimplesmenteJSON.
Aideiaémanterasimplicidadeparatransferirasinformações,supor-
tandotiposdedadosbemsimples:
1) null—valorvazio;
2) Boolean—trueoufalse;

## Página 18

CasadoCódigo Capítulo2. JSONveioparaficar
1) MinKey,MaxKey,Timestamp—tiposutilizadosinternamentenoMon-
goDB;
2) BinData—arraydebytesparadadosbinários;
3) ObjectId—identificadorúnicodeumregistrodoMongoDB;
4) Date—representaçãodedata;
5) Expressõesregulares.
Éimportanteentenderasintaxeeostipos,poistodaacomunicaç ãofeita
entrevocêeoMongoDB,ouentresuaaplicaç ãoeoMongoDB,seránesse
formato.
SeaexpressãoemJSONformuitoextensa,vocêpodeusarferramentas
onlineparaformatação,comoosite http://jsonprettyprint.com/.
2.1 Próximos passos
Certifique-sedequeaprendeu:
• oqueéJSON;
• ostiposexistentesnoJSON;
• asintaxedoJSON.
NopróximocapítulofaremosasoperaçõesbásicasdoMongoDBparama-
nipulaçãodedados.
9

## Página 20

Capítulo3
MongoDBbásico
Parainiciarestecapítulo,éprecisoantesinstalarosoftwaredoMongoDB.
Consulte14.
3.1 Conceitos
OMongoDBéum document database(bancodedadosdedocumentos),mas
nãosãoosdocumentosdafamíliaMicrosoft,masdocumentoscominfor-
maçõesnoformatoJSON.Aideiaéodocumentorepresentartodaainfor-
maçãonecessária,semarestriçãodosbancosrelacionais.
Emumdocumentopodemexistirumvalorsimples,comoumnúmero,
umapalavraouumadata,etambémumalistadevalores.
Osdocumentossãoagrupadosem collections.
Umconjuntodecollectionsformaum database(bancodedados).

## Página 21

3.1. Conceitos CasadoCódigo
Sefornecessário,essedatabasepodeserduplicadoemoutrosservidores,
ecadacópiaéchamadade replica set(conjuntoderéplica).
Afigura3.1mostrauma replica set rs1quecontémdoisdatabases,ecada
umdelespossuiduascollections.
Fig.3.1:Conceitosbásicos
Outroconceitomaisavan çadoéode sharding(particionamento seráex-
emplificadonocapítulo12),queéusadoquandosuacollectionpassoudos
bilhõesderegistrosehávantagememdividirosdadosporservidor.
Afigura12.2 mostraumexemplocomumacollectionúnicadetrêster-
abytesquepodeserparticionadaemtrêspartiçõesdeumterabytecada,es-
palhadaemtrêsmáquinasdistintas.
Nesteexemplo,acollectiondevisitasdeumsitefoiseparadapeladata,
dividindodadosportrimestre. Namáquina1ficaramosdadosdejaneiro
atéabril;namáquina2,demaioatéagosto;enamáquina3,desetembroaté
dezembro.
12

## Página 22

CasadoCódigo Capítulo3. MongoDBbásico
Fig.3.2:Sharding
3.2 Acessando oMongoDB
OacessoaoMongoDBpodeserfeitoviaconsole(executável mongo)ouvia
Robomongo(parainstalar,consulte 15).
Qualquer comando funcionará nos dois, mas o Robomongo é mais
amigável,alémdepossuirautocomplete,queébemútilquandonãolem-
bramosdocomando.
Podemosresumiragrandemaioriadoscomandosnaseguintesintaxe:
db.<nome-da-collection>.<operacao-desejada>;
Exemplo:
db.colecao1.count();
13

## Página 23

3.3. ExemplodaMega-Sena CasadoCódigo
3.3 Exemplo daMega-Sena
NositedaCaixa,estãodisponíveisparadownloadtodososresultadosda
Mega-SenaemformatoHTML(http://www1.caixa.gov.br/loterias/loterias/
megasena/download.asp).
CopiandooHTML,colandoemumaplanilhaegravandonoformato
CSV,podemosfacilmenteimportarosvaloresparaoMongoDB.
Baixe o arquivo megasena.csv (https://github.com/boaglio/
mongodb-casadocodigo/blob/master/capitulo-03/megasena.csv) , copie
paraumdiretóriodetesteseexecuteocomando:
mongoimport
-c <nome-da-collection>
-type csv
--headerline <nome-do-arquivo-CSV>
NesteexemplodosdadosdaMega-Sena,osparâmetrossão:
mongoimport -c megasena -type csv --headerline megasena.csv
OresultadoésemelhanteemWindowséodafigura 3.3.
Fig.3.3:ImportardadosdaMega-Sena
EmLinux,oresultadoéparecidocomesse. Notequeapareceototal
dedocumentos(objetos)importados: 1607registrosdentrodacollection
megasena.
fb@cascao > mongoimport
-c megasena
14

## Página 30

CasadoCódigo Capítulo3. MongoDBbásico
Porpadrão,acolunado ObjectIdésempreexibida.Éprecisoexplici-
tamenteinativarasuaexibição,conformeosdoisexemplos:
> db.megasena.find({"Ganhadores_Sena":5}, {"Concurso":true,
"_id":false});
{ "Concurso" : 233 }
{ "Concurso" : 1350 }
> db.megasena.find({"Ganhadores_Sena":5},{"Concurso":1,
"_id":0});
{ "Concurso" : 233 }
{ "Concurso" : 1350 }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.megasena.find({"Ganhadores_Sena":5},{"Concurso":1,"_id":0});
• MySQL:
select "Concurso" from megasena where "Ganhadores_Sena"=5
3.5 Adicionar registros
Paraadicionarnovosregistros,usamosocomando insert:
db.<nome-da-collection>.insert(
{ <campo1>:<valor1>,
<campo2>:<valor2>,
...
});
Vamosinserirumnovosorteio,fazendoumaanalogiacomoMySQL:
• MongoDB:
db.megasena.insert(
{
21

## Página 31

3.5. Adicionarregistros CasadoCódigo
"Concurso" : 99999,
"Data Sorteio" : "19/06/2014",
"1ª Dezena" : 1,
"2ª Dezena" : 2,
"3ª Dezena" : 3,
"4ª Dezena" : 4,
"5ª Dezena" : 5,
"6ª Dezena" : 6,
"Arrecadacao_Total" : 0,
"Ganhadores_Sena" : 0,
"Rateio_Sena" : 0,
"Ganhadores_Quina" : 1,
"Rateio_Quina" : "88000",
"Ganhadores_Quadra" : 55,
"Rateio_Quadra" : "76200",
"Acumulado" : "NAO",
"Valor_Acumulado" : 0,
"Estimativa_Prêmio" : 0,
"Acumulado_Mega_da_Virada" : 0
});
• MySQL:
INSERT INTO MEGASENA
("Concurso",
"Data Sorteio",
"1ª Dezena",
"2ª Dezena",
"3ª Dezena",
"4ª Dezena",
"5ª Dezena",
"6ª Dezena",
"Arrecadacao_Total",
"Ganhadores_Sena",
"Rateio_Sena",
"Ganhadores_Quina",
"Rateio_Quina",
"Ganhadores_Quadra",
"Rateio_Quadra",
22

## Página 32

CasadoCódigo Capítulo3. MongoDBbásico
"Acumulado",
"Valor_Acumulado",
"Estimativa_Prêmio",
"Acumulado_Mega_da_Virada" )
VALUES
(99999,
"19/06/2014",
1,
2,
3,
4,
5,
6,
0,
0,
0,
1,
"88000",
55,
"76200",
"NAO",
0,
0,
0);
Atéomomento,semnenhumanovidade,apenasumadiferen çanasin-
taxeentreoMongoDBeoSQLrelacional,certo?
Poisbem,vamosmostraralgumasvantagensagora.
Alémdossorteios,vamosanotaroCPFdeganhador,noformatonúmero
doconcursoeCPF.
• MongoDB:
db.ganhadores.insert({"Concurso":99999,
"CPF":12345678900});
• MySQL:
23

## Página 41

3.7. Removerregistros CasadoCódigo
From ganhadores A
where NEW.nome = A.nome
) THEN
INSERT INTO ganhadores(nome)
VALUES (NEW.nome);
END IF;
END;
update ganhadores
set cpf = 33333333333
where nome='Mula sem cabeça';
3.7 Remover registros
Pararemoverregistros,usamosocomando removecomaseguintesintaxe:
db.<nome-da-collection>.remove(
{ <criterioDeBusca1>:<valor1>,...}
);
PararemovertodososregistroscomCPF33333333333:
> db.ganhadores.count();
3
> db.ganhadores.find({"CPF" : 33333333333}).count();
1
> db.ganhadores.remove({"CPF" : 33333333333});
WriteResult({ "nRemoved" : 1 })
> db.ganhadores.count();
2
Apenasumregistrofoiremovido,ototal countdiminuiude3para2.
ComparandocomSQLrelacional,temos:
• MongoDB:
db.ganhadores.remove({"CPF" : 33333333333});
• MySQL:
32

## Página 43

3.9. Alterandoumacolunadeumacollection CasadoCódigo
> exit
bye
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.megasena.drop();
• MySQL:
drop table megasena;
3.9 Alterando uma coluna de uma collection
Sefornecessárioremoverumacoluna,asintaxedocomandoé:
db.<collection>.update( {},
{ $unset : { <campo>: 1 }},
false,true);
Oparâmetro falseavisaquenãoéum upserteoparâmetro true
éaconfirmaçãopararemoveremtodososdocumentos,enãoapenasno
primeiro.
Porexemplo:
> db.messages.update( {},
{ $unset : { titulo: 1 }},
false,true);
WriteResult({ "nMatched" : 120477,
"nUpserted" : 0,
"nModified" : 120476 })
Sefornecessárioapenasalteraronome,asintaxeésemelhante:
db.<collection>.update( {},
{ $rename :
{ "<nome-da-coluna-atual>" : "<nome-da-coluna-novo>" }},
false,true);
34

## Página 44

CasadoCódigo Capítulo3. MongoDBbásico
Porexemplo:
db.messages.update( {},
{ $rename :
{ "mailboxx" : "mailbox" }},
false,true);
WriteResult({ "nMatched" : 120477,
"nUpserted" : 0,
"nModified" : 120477 })
3.10 Melhorando as buscas
Sedesejarmoscontartodosossorteiosde2009,precisamosfiltrarocampo
Data Sorteio demaneiraquesóconsidereasdatasqueterminemcom
“2009”,issoemSQLseriaocorrespondenteaocomandoLIKE.
NoMongoDB,parafazermosessetipodefiltro,usamosexpressõesregu-
lares.Essetipodeconsultapodeserfeitodeduasmaneiras:
db.<nome-da-collection>.find({ <campo>:/<texto-para-buscar>/})
ou:
db.<nome-da-collection>.find(
{<campo>:{$regex:<texto-para-buscar>}})
Exemplo:
fb@cascao ~ > mongo
MongoDB shell version: 2.6.1
connecting to: test
> db.megasena.find({"Data Sorteio":/2009/}).count()
105
> db.megasena.find({"Data Sorteio":{$regex:'2009'}}).count()
105
> exit
bye
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
35

## Página 45

3.10. Melhorandoasbuscas CasadoCódigo
db.megasena.find({"Data Sorteio":/2009/}).count();
• MySQL:
SELECT COUNT(*)
FROM megasena
WHERE "Data Sorteio" like '%2009%';
Entretanto,sefizermosumabuscaparacontarquantosganhadorestêm
joeemseunome,temosoresultado:
> db.ganhadores.find({"Nome":/joe/}).count();
0
> db.ganhadores.find({"Nome":/Joe/}).count();
1
Parafazerumabuscaignorandoletrasmaiúsculaseminúsculas,asintaxe
éumpoucodiferente:
db.<nome-da-collection>.find({ <campo>:/<texto-para-buscar>/i})
ou:
db.<nome-da-collection>.find(
{<campo>:{$regex:<texto-para-buscar>,$options:'i'}})
fb@cascao ~ > mongo
MongoDB shell version: 2.6.1
connecting to: test
> db.ganhadores.find({"Nome":/joe/i}).count();
1
> db.ganhadores.find({
"Nome":{$regex:'joe',$options:'i'}}).count();
1
> exit
bye
Alistacontémoutrosoperadoresdebusca,consultenafigura 3.5enosite
oficialdoMongoDB.
36

## Página 46

CasadoCódigo Capítulo3. MongoDBbásico
•$gt maiorque(greater-than)
•$gte igualoumaiorque(greater-than or equal to)
•$lt menorque(less-than)
•$lte igualoumenorque(less-than or equal to)
•$ne nãoigual(not equal )
•$in existeemumalista
•$nin nãoexisteemumalista
•$all existeemtodoselementos
•$not trazoopostodacondição
•$mod calculaomódulo
•$exists verificaseocampoexiste
•$elemMatch comparaelementosdearray
•$size comparatamanhodearray
37

## Página 47

3.10. Melhorandoasbuscas CasadoCódigo
Fig.3.5:Operadoresdebusca
38

## Página 48

CasadoCódigo Capítulo3. MongoDBbásico
Mais exemplos
NadocumentaçãooficialdoMongoDBhámaisexemplosdecoman-
dosMongoDBcomparandocomSQLrelacional: http://info.mongodb.
com/rs/mongodb/images/sql_to_mongo.pdf.
3.11 CappedCollection
OMongoDBpossuiumrecursobeminteressante,as capped collections(col-
lections“tampadas”),quesãocollectionscomtamanhospredefinidosecomo
seuconteúdorotativo.Normalmente,emumbancodedadosrelacional,esse
tipodecomportamentoéfeitomanualmenteouatravésdeumaaplicaç ão.
Asintaxeparacriarumacollectiondessetipoé:
db.createCollection("<collection>",
{capped: true, size: <tamanho-em-bytes>,
max: <número-de-documentos>})
Otamanhodevesernomínimo4096eopcionalmentepodemoslimitar
onúmerodedocumentoscom max.
Vamoscriarumacollectioncomolimitededoisdocumentos:
> db.createCollection("cacheDeDoisdocumentos",
{ capped: true, size: 4096,
max: 2 })
{ "ok" : 1 }
Emseguida,inserimosquatrodocumentos:
> db.cacheDeDoisdocumentos.insert({"nome":"teste 1"});
WriteResult({ "nInserted" : 1 })
> db.cacheDeDoisdocumentos.insert({"nome":"teste 2"});
WriteResult({ "nInserted" : 1 })
> db.cacheDeDoisdocumentos.insert({"nome":"teste 3"});
WriteResult({ "nInserted" : 1 })
> db.cacheDeDoisdocumentos.insert({"nome":"teste 4"});
WriteResult({ "nInserted" : 1 })
39

## Página 50

Capítulo4
Schemadesign
Quandosepensaemmodelarumsistemaemumbancodedados,sempresão
consideradasasregrasdenormalizaçãodedadosindependentedosistema
utilizado.
Anormalizaçãoevitaaredundânciadedadosarmazenados,maselapode
serumproblemaquandofornecessárioconsultaressasinformaçõesnormal-
izadaseseparadasemváriastabelas,emostrá-lasemumsiteemumaúnica
página.
Seasinformaçõesestãoseparadasemváriastabelas,issopossivelmente
estarámaisespalhadonodiscorígidoe,provavelmente,exigirámaisproces-
samentodaCPUparajuntartudoaoretornarparaumaconsulta.
QuandosetrabalhacomMongoDB,aprimeiracoisaparaseconsideraré
comoaaplicaçãoprecisadosdadosagrupadosesomentedepoisascollections
sãoorganizadas.

## Página 51

CasadoCódigo
Emummodelorelacional,écomumseparartudoemtabelas,jánoMon-
goDBsepara-sepor“entidades”,ondeostodosdadosnecessários(ouquase)
estãojuntos.
Lembre-sequenoMongoDBnãotemostabelascompostasporcolunas
quearmazenamapenasumtipodeinformaç ão,trabalhamoscomdocumen-
tos,quenãotêmessetipodelimitaçãoemsuaestrutura.
ÉimportantetambémsaberqueoMongoDBnãosuportanenhumtipo
deconstraint,poiseleesperaqueessavalidaç ãoexistadoladodaaplicaç ão.
Alémdisso,oMongoDBtambémnãosuportatransação,jáqueaideiaé
que,emvezdetermosumatransaç ãoqueenvolvaváriastabelas,asuaapli-
caçãotenhaumdocumentoquesejaarmazenadoemumacollection.
• MongoDB:
db.seriados.insert({
"_id":4,
"nome":"Chaves",
"personagens":[
"Seu Barriga",
"Quico",
"Chaves",
"Chiquinha",
"Nhonho",
"Dona Florinda"]})
• SQLRelacional:
INSERT INTO SERIADO(ID,NOME)
VALUES (4,'Chaves');
INSERT INTO PERSONAGEM(ID,NOME,SERIADO_ID)
VALUES (55,'Seu Barriga',4);
INSERT INTO PERSONAGEM(ID,NOME,SERIADO_ID)
VALUES (56,'Quico',4);
INSERT INTO PERSONAGEM(ID,NOME,SERIADO_ID)
VALUES (57,'Chaves',4);
INSERT INTO PERSONAGEM(ID,NOME,SERIADO_ID)
VALUES (58,'Chiquinha',4);
INSERT INTO PERSONAGEM(ID,NOME,SERIADO_ID)
42

## Página 52

CasadoCódigo Capítulo4. Schemadesign
VALUES (59,'Nhonho',4);
INSERT INTO PERSONAGEM(ID,NOME,SERIADO_ID)
VALUES (60,'Dona Florinda',4);
COMMIT;
Analisandooexemplodastabelas SERIADOe PERSONAGEMdessecom-
parativo,percebemosqueseparamosessasinformaçõesapenaspelalimitação
dobancodedadosrelacional.
Entretanto,existemalgumasmaneirasderelacionarascollections,tendo
umfuncionamentocomparadoàchaveestrangeiradobancodedadosrela-
cional.
ApesardeoMongoDBpossuirop çõesdeíndicesparamelhorarasua
busca,nadasuperaumbom schema design,comcollectionsquerefletemex-
atamenteoqueaaplicaç ãoespera,agrupandoasinformaçõesdamaneira
maisadequada.
4.1 Relacionando uma collection para muitas
Existemduasmaneirasderepresentaressetipoderelacionamento. Vamos
imaginarumexemplodeumsistemadevendadelivros,comvárioscomen-
táriosparacadalivro.
Certamente,pensandomaisdojeitorelacional,épossíveldividirasinfor-
maçõesemduascollections,inicialmentecadastrandoumlivro:
db.livros.insert({
_id:"A menina do Vale",
autor: "Bel Pesce",
tags: ["empreendedorismo","inspiração","virar a mesa" ]});
Ecadastrandodoiscomentáriosparaestelivro:
db.comentarios.insert({
livro_id: "A menina do Vale",
autor: "Amit Garg",
texto: "A Menina do Vale tem o poder de energizar qualquer
pessoa. É um livro sobre ação e mostra que qualquer
pessoa nesse mundo pode realizar os seus sonhos."});
43

## Página 53

4.1. Relacionandoumacollectionparamuitas CasadoCódigo
db.comentarios.insert({
livro_id: "A menina do Vale",
autor: "Eduardo Lyra",
texto: "Pare tudo e leia A Menina do Vale agora mesmo. Te
garanto que você vai aprender demais com essa
leitura e vai se surpreender com o quanto é capaz
de fazer."});
Essaabordagem,entretanto,nãotemnenhumavantagemparaoMon-
goDB,poisseparaasinformaçõesemlocaisdistintos,exigindomaisCPUe
operaçõesemdiscoquandoaaplicaçãonecessitarexibirtudodeumavez.
Nessecaso,oidealeraembutirasinformaçõesdecomentáriosdentrode
cadalivro,dessamaneira:
db.livros.insert({
_id:"A menina do Vale",
autor: "Bel Pesce",
tags: ["empreendedorismo","inspiração","virar a mesa" ],
comentarios: [
{
autor: "Amit Garg",
texto: "A Menina do Vale tem o poder de energizar qualquer
pessoa. É um livro sobre ação e mostra que qualquer
pessoa nesse mundo pode realizar os seus sonhos."
},
{
autor: "Eduardo Lyra",
texto: "Pare tudo e leia A Menina do Vale agora mesmo. Te
garanto que você vai aprender demais com essa
leitura e vai se surpreender com o quanto é capaz
de fazer."
}
]
})
Percebaquesempreaformacomoaaplicaç ãonecessitadasinformações
éessencialparaorganizarassuascollections,elaéachavedeumaboaper-
formancedeseusistema.
44

## Página 54

CasadoCódigo Capítulo4. Schemadesign
4.2 Relacionando muitas collection para
muitas
NoMongoDBtambémépossívelrepresentarorelacionamentodemuitos
paramuitos.Vamosexemplificarumcenárioemquetemosumalojadelivros
comváriascategorias,eumacategoriatenhavárioslivros.
Inicialmente,cadastramosumlivroreferenciandotrêscategorias:
db.livros.insert({
_id:"A menina do Vale",
autor: "Bel Pesce",
categorias: ["empreendedorismo","inspiração","virar a mesa"]});
Emseguida,cadastramosumacategoriareferenciandodoislivros:
db.categorias.insert({nome: "empreendedorismo",
lista_de_livros:
["A menina do Vale",
"28 Mentes Que Mudaram o Mundo"]
});
Noteque,pararepresentaramesmainformaç ãoemumbancodeda-
dosrelacional, serianecessáriaumatabelaintermediária. Provavelmente
teríamosaofinalastabelas: LIVRO, CATEGORIAe LIVRO_CATEGORIA.
4.3 Tudo em uma collection
Setudoficaremumacollection,háavantagemdetermosasinformaçõesde
maneiramaisintuitivaemelhorperformance.
Entretanto,podemosteralgumasdesvantagens,comocomplicardemais
aofazerumabusca,principalmenteparaobterresultadosparciais.
Alémdisso,cadaregistro/documentopossuiumlimitede16Mb.
SaibamaissobreoslimitesdoMongoDBnoapêndice 16.
4.4 S chema design na prática
Vamosanalisarumcasoreal: obancodedadosutilizadoéumasimplifi-
caçãododositeInternetMovieDatabase(IMDB).AtravésdosoftwareJMDB
45

## Página 55

4.5. Protótipo CasadoCódigo
(http://www.jmdb.de/)épossívelbaixarabasededadoslocalmentenoseu
computadoremMySQL,comquasemeiomilhãodefilmescadastrados.
4.5 Protótipo
Nossoprotótipodosistema“Meusfilmes”temcomoobjetivoexibirfilmese
atores.
Natelainicial 4.1épossívelfazerumabuscaporsomentefilmes,somente
atoresouambos.
Fig.4.1:ProtótipodoMeusfilmes páginainicial
Saindodatelainicial,podemosdetalharumator,comoéexibidona 4.2.
Alémdonomedoator,éexibidaalistadefilmesdequeeleparticipa.
46

## Página 56

CasadoCódigo Capítulo4. Schemadesign
Fig.4.2:ProtótipodoMeusfilmes detalhedeator
Podemosdetalharumfilme,comoéexibidona 4.3. Alémdonomedo
filme,sãoexibidasaquantidadedevotos,anotamédiaealistadecategorias
defilme,diretoreseatores.
47

## Página 57

4.6. SistemaMeusfilmesrelacional CasadoCódigo
Fig.4.3:ProtótipodoMeusfilmes detalhedefilme
4.6 S istema Meus filmes relacional
Osistemarelacionalqueexibeessasinformaçõesestádivididoem7tabelas:
•actors atores
•movies filmes
•directors diretores
•genres generosdosfilmes
•movies2actors tabelaassociativadefilmeseatores
•ratings notasdosfilmes
•movies2directors tabelaassociativadefilmesediretores
48

## Página 58

CasadoCódigo Capítulo4. Schemadesign
Fig.4.4:Modelorelacionaldemeusfilmes
Comotodosistemarelacional,essemodelofoicriadolevandoemconta
apenasasformasnormais,semlevaremconsidera çãocomoaaplicaçãofoi
montada.
49

## Página 60

CasadoCódigo Capítulo4. Schemadesign
{"name":"Lawrence, Harry (I)",sex:"M"},
{"name":"Ledger, Bernard",sex:"M"},
{"name":"O'Connor, David (I)",sex:"M"},
{"name":"Pantoliano, Joe",sex:"M"},
{"name":"Parker, Anthony Ray",sex:"M"},
{"name":"Pattinson, Chris",sex:"M"},
{"name":"Quinton, Luke",sex:"M"},
{"name":"Reeves, Keanu",sex:"M"},
{"name":"Simper, Robert",sex:"M"},
{"name":"Taylor, Robert (VII)",sex:"M"},
{"name":"Weaving, Hugo",sex:"M"},
{"name":"White, Adryn",sex:"M"},
{"name":"Witt, Rowan",sex:"M"},
{"name":"Woodward, Lawrence",sex:"M"},
{"name":"Young, Bill (I)",sex:"M"},
{"name":"Brown, Tamara (I)",sex:"F"},
{"name":"Foster, Gloria (I)",sex:"F"},
{"name":"Gordon, Deni",sex:"F"},
{"name":"Johnson, Fiona (I)",sex:"F"},
{"name":"McClory, Belinda",sex:"F"},
{"name":"Morrison, Rana",sex:"F"},
{"name":"Moss, Carrie-Anne",sex:"F"},
{"name":"Nicodemou, Ada",sex:"F"},
{"name":"Pender, Janaya",sex:"F"},
{"name":"Tjen, Natalie",sex:"F"},
{"name":"Witt, Eleanor",sex:"F"}
]})
4.8 Próximos passos
Certifique-sedequeaprendeu:
• aavaliaraaplicaçãoantesdemontaro schema;
• arepresentarcollectionsemrelacionamentoumparamuitos;
• arepresentarcollectionsemrelacionamentomuitosparamuitos.
Nopróximocapítulo,veremoscomoossistemasinteragemcomoMon-
goDB,comexemplospráticosemváriaslinguagens.
51

## Página 62

Capítulo5
ConversandocomMongoDB
Oqueéumrepositóriodedadossemumaaplicaç ãoparaconversarcomele?
Nestecapítuloveremoscomodiversaslinguagensdeprogramaç ãoseco-
municamcomoMongoDB.
Estáforadoescopodestelivroseaprofundarnaslinguagensounascon-
figuraçõesdeambiente,aquiapenascitaremosasfontesparainstalaç ãoefo-
caremosmaisnoexemplodalinguagemutilizada.
Osexemplostambémsedestinamaoaprendizadodaintegra çãodalin-
guagemcomoMongoDB,enãonamelhorpráticadalinguagememsiem
umsistema.
5.1 Osistema de seriados
Osistemausadocomoexemploécompostodeumcadastrodeseriados,us-
andoapenasumacollection.Atravésdaaplicaçãoépossívelfazeraoperação

## Página 64

CasadoCódigo Capítulo5. ConversandocomMongoDB
Fig.5.1:phpInfocomMongoDBdriver
Sobre oPHP
Em1994foicriadaalinguagemdeprogramaçãoPHP(Personal Home
Page)focadanacriaçãodeconteúdodinâmiconainternet.Hojeelaéus-
adaemmuitasaplicações,entreelasaWikipedia,FacebookeWordpress.
Alistadeseriados
Alistadeseriadosestánoarquivo index.phpeinicia-secriandouma
variávelconexaoquerecebeodriverdeacessoaoMongoDB:
<?php
$conexao = new MongoClient();
55

## Página 65

5.2. SeriadosemPHP CasadoCódigo
Emseguida,escolhemosacollectiondesejadautilizandoasintaxe:
[variavel]->[nome-do-banco-de-dados]->[nome-da-collection]
$collection = $conexao->test->seriados;
Finalmenteusamosumavariável cursorquearmazenaráoresultadoda
buscadetodososdocumentosdacollectioncomométodo find:
$cursor = $collection->find();
?>
Depois,osdocumentossãoexibidosnatelaatravésdeumloopdavariável
cursor,quedevolveumalistadedocumentos,tratadosumporum:
<?php
foreach ($cursor as $documento) {
Osvaloresdodocumentocompõemumarraynavariável documento.
Sãoexibidosapenasosvalores _idparachamarapáginadealterarosvalores
eo nomeparaexibirnatela.
echo "<a class=\"alert alert-success\" href=\"detalhe.php?id=".
$documento["_id"]."\">".
$documento["nome"]."</a>";
}
?>
Oresultadoobtidoéexibidonafigura 5.2.
56

## Página 66

CasadoCódigo Capítulo5. ConversandocomMongoDB
Fig.5.2:ListadeseriadosemPHP
Umnovoseriado
OsvaloresdeumnovoseriadosãoenviadosemumformulárioHTML
via POSTecapturadosnoPHPatravésdavariável $_POST.
Ocadastrodeseriadosestánoarquivo novo.phpeinicialmenteabrimos
aconexãonoMongoDBescolhendoacollectiondesejada:
$conexao = new MongoClient();
$collection = $conexao->test->seriados;
Emseguida,montamosodocumentoparacadastrar.Primeiromontamos
alistadepersonagensdentrodavariável personagens:
$personagens =array($_POST['personagem1'],$_POST['personagem2'],
$_POST['personagem3'],$_POST['personagem4'],
57

## Página 67

5.2. SeriadosemPHP CasadoCódigo
$_POST['personagem5'],$_POST['personagem6']);
Depoisodocumentofinalémontado,compostopeloscampos nomeea
listadepersonagens:
$documento = array("nome" => $_POST['nome'],
"personagens" => $personagens);
Finalmenteodocumentoéinseridoatravésdométodo insert:
$collection->insert($documento);
Oresultadoobtidoéexibidonafigura 5.3.
58

## Página 68

CasadoCódigo Capítulo5. ConversandocomMongoDB
Fig.5.3:CadastrodenovoseriadoemPHP
Alterarumseriado
Oidentificadorúnicodacollectiondeseriados( _id)éenviadocomo
parâmetrovia GETaoarquivo detalhe.php,ecapturadonoPHPatravés
davariável $_GET.
ApáginadedetalhedoseriadoiniciaabrindoumaconexãonoMongoDB
59

## Página 69

5.2. SeriadosemPHP CasadoCódigo
damesmamaneiraqueaspáginasanteriores:
$conexao = new MongoClient();
$collection = $conexao->test->seriados;
Emseguida,faremosabuscadodocumentousandoomesmométodo
find,porémcomoparâmetro _id.
Nessecaso,comoabuscaéfeitapeloidentificadorúnico,éprecisocriar
umobjetodotipo MongoId:
$id = $_GET['id'];
$cursor = $collection->find( array('_id' => new MongoId($id)));
Finalmente,oregistroéatribuídoàvariável documento:
$documento= $cursor->getNext();
Aopçãodealteraçãodedocumentoésemelhanteàdecadastro.Inicial-
menteodocumentoémontadonavariável documento:
$personagens =array($_POST['personagem1'],
$_POST['personagem2'],$_POST['personagem3'],
$_POST['personagem4'],$_POST['personagem5'],
$_POST['personagem6']);
$documento = array( "nome" => $_POST['nome'],
"personagens" => $personagens);
Usamosométodo updateparaalterarodocumento,enviandocomo
parâmetros:oidentificadorúnico,avariável documento,eaop ção upsert
ativa,quefaráumcadastrosenãoencontraroregistroqueestásendoalter-
ado:
$collection->update(array('_id' =>
new MongoId($id)),$documento, array('upsert'=>true));
A opção de remover o documento é semelhante também, usando o
método removeeenviandocomoparâmetrooidentificadorúnico:
$collection->remove(array('_id' => new MongoId($id)));
60

## Página 70

CasadoCódigo Capítulo5. ConversandocomMongoDB
Oresultadoobtidodateladealteraç ãoéexibidonafigura 5.4.
Fig.5.4:AlterarumseriadoemPHP
61

## Página 71

5.3. Java CasadoCódigo
5.3 Jav a
Sobre oJav a
Em1995,foicriadaalinguagemdeprogramaçãofocadanacriaçãode
aplicaçõesparadiversasplataformas:desktop,servidoremobile. Hoje
elaéusadaemdiversassoluções,deERPs,sitesdebancos,celulareseaté
eletrodomésticos.
ExistemváriasopçõesparatrabalharcomJavaeMongoDB,masvamos
nosfocarnasduasprincipais.
Driveroficial
Oscódigos-fontesdesteprojetoestãodisponíveisem https://github.com/
boaglio/mongodb-javapuro-casadocodigo.
Pré-requisitos:
• ServidorApacheTomcathttp://tomcat.apache.org/
• Javahttp://java.sun.com/
• JavaMongoDBdatabasedriverhttp://www.mongodb.org
Emnossosistemadeseriados,aclasse SeriadosDAOconcentraasroti-
nasqueacessamobancodedados.
AconexãocomoMongoDBécontroladapelaclasse MongoClient,
comonoexemplo:
public Mongo mongo() throws Exception {
MongoClient mongoClient = new MongoClient(
new ServerAddress("localhost",27017)
);
return mongoClient;
}
62

## Página 72

CasadoCódigo Capítulo5. ConversandocomMongoDB
Abuscadedadoséfeitaatravésdeumloopemumcursor DBCursor,
que retorna uma linha/ documento (DBObject) através de um objeto
DBObject.
public List<Seriado> findAll() {
List<Seriado> seriados = new ArrayList<Seriado>();
DBCursor cursor = seriadosCollection.find();
while (cursor.hasNext()) {
DBObject resultElement = cursor.next();
Esseobjetodotipo DBObjectéconvertidoemum Mapdeobjetos,e
depoisconvertidoparaumobjetodotipo Seriado:
Map<?,?> resultElementMap = resultElement.toMap();
Seriado seriado = new Seriado();
seriado.setId((ObjectId) resultElementMap.get("_id"));
seriado.setNome((String) resultElementMap.get("nome"));
seriados.add(seriado);
System.out.println("Seriado lido = " + seriado);
}
return seriados;
}
Nofinaltemosumalistadeobjetosdotipo Seriadoretornados.
PelosistemaemJava,apágina index.jspcriaumainstânciadaclasse
SeriadosDAOatravésdachamada:
<jsp:useBean
id="dao"
class="com.boaglio.casadocodigo.mongodb.SeriadosDAO" />
Depois,émontadaalistacomosnomesdeseriados:
<c:forEach var="seriado" items="<%= dao.findAll() %>">
<a class="alert alert-success"
href="detalhe.jsp?id=<c:out value="${seriado.id}"/>">
<c:out value="${seriado.nome}" />
63

## Página 73

5.3. Java CasadoCódigo
</a>
</c:forEach>
Umnovoseriado
OsvaloresdeumnovoseriadosãoenviadosemumformulárioHTML
via POSTecapturadosnoJSPatravésdavariável request.
Ocadastrodeseriadosestánoarquivo novo.jsp. Criamosumain-
stânciadaclasse SeriadoDAOedepoisverificamosseoconteúdode nome
existe,parainiciarumainclusão:
String nome = request.getParameter("nome");
SeriadosDAO dao = new SeriadosDAO();
if (nome!=null && nome.length()>0 ) {
Emseguida,recuperamososvaloresrestantesenviadospeloformulárioe
atribuímosaumobjetodotipo Seriado:
Seriado seriadoNovo = new Seriado();
seriadoNovo.setNome(nome);
List<String> personagens = new ArrayList<String>();
personagens.add(request.getParameter("personagem1"));
personagens.add(request.getParameter("personagem2"));
personagens.add(request.getParameter("personagem3"));
personagens.add(request.getParameter("personagem4"));
personagens.add(request.getParameter("personagem5"));
personagens.add(request.getParameter("personagem6"));
seriadoNovo.setPersonagens(personagens);
FinalmenteinserimosonovoseriadonoMongoDBchamandoométodo
insertcriadoem SeriadoDAO:
dao.insert(seriadoNovo);
64

## Página 74

CasadoCódigo Capítulo5. ConversandocomMongoDB
Alterarumseriado
OsvaloresdeumnovoseriadosãoenviadosemumformulárioHTML
via POSTecapturadosnoJSPatravésdavariável request.
Naalteraçãorecebemosoparâmetro id,parabuscarosdadosdoseriado
paraexibirnapágina,usandoométodo findById:
String id = request.getParameter("id");
SeriadosDAO dao = new SeriadosDAO();
Seriado seriado = dao.findById(id);
Ajustamos o identificador único do seriado (ObjectID) para o
parâmetro idrecebidonavariável seriadoParaAlterar:
Seriado seriadoParaAlterar = new Seriado();
seriadoParaAlterar.setId(new ObjectId(id));
Depoisatribuímososvaloresrecebidosdoformulárioparaavariável
seriadoParaAlterar:
seriadoParaAlterar.setNome( request.getParameter("nome") );
List<String> personagens = new ArrayList<String>();
personagens.add(request.getParameter("personagem1"));
personagens.add(request.getParameter("personagem2"));
personagens.add(request.getParameter("personagem3"));
personagens.add(request.getParameter("personagem4"));
personagens.add(request.getParameter("personagem5"));
personagens.add(request.getParameter("personagem6"));
seriadoParaAlterar.setPersonagens(personagens);
Finalmente,chamamosométodo updatecriadoem SeriadoDAO:
dao.update(seriadoParaAlterar);
Seforescolhidaaop çãoderemoveroseriado,usamosométodo remove:
if(opt.equals("remover"))
{
dao.remove(id);
}
65

## Página 75

5.3. Java CasadoCódigo
SpringData
Sobre oSpring Framework
Em2002foicriadoumframeworktotalmentebaseadoeminje çãode
dependênciascomoalternativaaossistemasemEJB.Hojeoframework
evoluiubastanteepossuidiversosmódulos,desdeseguran ça,webser-
vicesatédemobile. ParaaprofundarnousoSpring,procurepelolivro
“VireojogocomSpringFramework”(http://www.casadocodigo.com.br/
products/livro-spring-framework).
Sabercomousarodriveroficialéamelhorformadeaprendertodoo
poderdeacessoqueumaaplicaçãoJavapodeteremutilizaroMongoDB,en-
tretanto,quandoprecisamosdeprodutividade,partimosparaumframework.
Umaexcelenteop çãodeabstraçãododriverdoMongoDBéoSpring
Data,quefacilitaalgunspassosnousodoMongoDB.
No exemplo disponível em https://github.com/boaglio/
mongodb-java-springdata-casadocodigotemosumaversãodaaplicaç ãode
seriadoscomoMongoDBeSpringData.
EssaaplicaçãousatambémoutrosmódulosdoSpring,comooSpring
MVC,maselesnãoestãoconfiguradosdaformamaisadequadaparausoem
produção.OfocodessaaplicaçãoémostraraintegraçãodosistemaaoMon-
goDBatravésdoSpringData.
Apartedetela(JSP)éigualaoexemploanterior,adiferen çaéafacilidade
emmanipularosdados.
Inicialmente, temosamesmaclasse POJO Seriadousadoanterior-
mente,mascomumaanotaçãoqueindicaonomedacollectiondoMongoDB
aqueessaclassepertence:
@Document(collection = "seriados")
public class Seriado implements Serializable {
Em seguida, temos uma classe que contém as configurações
de conexão ao banco de dados, que deve ser uma classe filha de
AbstractMongoConfiguration:
66

## Página 76

CasadoCódigo Capítulo5. ConversandocomMongoDB
@Configuration
public class SpringMongoConfig extends
AbstractMongoConfiguration {
Assimcomonoexemploanterior,aconexãoaobancodedadosretorna
umobjetodotipo MongoClient,edevemossobrescreverométodo mongo
ecolocarosvaloresadequados:
private static final String SERVIDOR_MONGODB = "127.0.0.1";
@Override
@Bean
public Mongo mongo() throws Exception {
return new MongoClient(SERVIDOR_MONGODB);
}
Para manipular os dados, semelhante ao comportamento da classe
SeriadoDAOdoexemploanterior,temosagoraa SeriadoRepository,
quepossuiosmesmosmétodos,porémcomalgumasdiferen ças.
AclasserecebeumaanotaçãodeserumrepositóriodedadosdoSpring(
Repository)etemumatributodotipo MongoTemplate:
@Repository
public class SeriadosRepository {
@Autowired
private MongoTemplate mongoTemplate;
Comesseatributo,fazemosasoperaçõesdeacessoaoMongoDBcom
bemmenoscódigoquenoexemploanterior.
Para retornar a lista de todos os seriados, usamos apenas o
método findAll e informamos o tipo de dado que será retornando (
Seriado.class):
List<Seriado> seriados = new ArrayList<Seriado>();
seriados = mongoTemplate.findAll(Seriado.class);
return seriados;
67

## Página 77

5.3. Java CasadoCódigo
Dessamaneira,oSpringDataseconectaaobancodedados,acessaacol-
lection seriadosespecificadanaclasse Seriado(em @Document)ede-
poisretornaalistaderegistros,fazendoautomaticamenteaconversãododoc-
umentoJSONdoMongoDBparaumalistadeinstânciasdaclasse Seriado.
Sim,comcertezaessaéumamaneirabemprodutivadesetrabalhar!
Asoutrasoperaçõestambémsãobemmaissimples,comoabuscapela
chave, onde criamos um critério de busca peloide usamos o método
findOne,queretornaapenasumdocumento,nessecasodotipo Seriado.
Damesmamaneiracomono findAll,aconversãoautomáticadodocu-
mentoJSONparaainstânciadaclasse Seriadotambémacontece.
Seriado seriado = new Seriado();
Query queryDeBuscaPorID =
new Query(Criteria.where("id").is(id));
seriado =
mongoTemplate.findOne(queryDeBuscaPorID,Seriado.class);
return seriado;
Asoperaçõesdecadastrar/atualizartambémsãobemsimples.Passamos
oobjetoparagravareeleéautomaticamenteconvertido:
// cadastrar
mongoTemplate.insert(seriado);
// alterar
mongoTemplate.save(seriado);
Para remover um seriado peloid, criamos uma instância do tipo
Seriadoecolocamosnoatributo idovalorde new Object(id):
Seriado seriadoParaRemover = new Seriado();
seriadoParaRemover.setId(new ObjectId(id));
mongoTemplate.remove(seriadoParaRemover);
Outrasop ções
Umaopçãointeressanteéo Jongo(http://jongo.org/),quemtemcomo
objetivooferecercomandosnoJavasemelhantesaosdoMongoshell.
SeumabuscanoMongoshellfor:
68

## Página 78

CasadoCódigo Capítulo5. ConversandocomMongoDB
db.seriados.find({nome: "Chaves"})
UsandooJongoseria:
seriados.find("{nome:'Chaves'}").as(Seriado.class)
Aalternativasemelhanteao Spring Data éo Morphia(daMongoDB
https://github.com/mongodb/morphia):
Morphia morphia = new Morphia();
Datastore ds = morphia.createDatastore("test");
List<Seriado> seriados = ds.find(Seriado.class).asList();
Porúltimo,enãomenosimportante,éa Hibernate OGM (Hibernate
Object/GridMapper http://ogm.hibernate.org),quenomomentopossui
umaversãobemlimitadadoMongoDB,mastotalmentefuncional.
5.4 PlayFramework
Sobre oPlayFramework
Em2007,foicriadoumframeworkparaaplicaçõeswebnopadrão
MVC,visandoàprodutividadecomconven çãosobreconfiguração. A
sua versão 2 foi reescrita inteiramente em Scala e oferece recursos
interessantes dessa linguagem para os sistemas: é totalmente REST-
ful,integradacomJUniteSelenium,possuiI/Oassíncronoearquite-
tura modular. Para aprofundar no uso do Play Framework, pro-
cure pelo livro “Play Framework” (http://www.casadocodigo.com.br/
products/livro-play-framework-java).
Oscódigos-fontesdosistemaestãodisponíveisem https://github.com/
boaglio/play2-casadocodigo.
AaplicaçãoemPlaytemquasetudodoqueéprecisoparafazerumsis-
temacompleto. Precisamosapenasadicionarumadependênciadomódulo
paraconectaraoMongoDBnoarquivo build.sbt:
69

## Página 79

5.4. PlayFramework CasadoCódigo
libraryDependencies +=
"net.vz.mongodb.jackson" %
"play-mongo-jackson-mapper_2.10" %
"1.1.0"
Noarquivodeconfigurações application.confadicionamosduas
linhas:
mongodb.servers="127.0.0.1:27017"
mongodb.database="test"
Omapeamentoda collectionéfeitonaclasse Seriado:
private static
JacksonDBCollection<Seriado,String> collection =
MongoDB.getCollection("seriados",Seriado.class,String.class);
Parabuscartodososseriados,chamamosométodo finddavariável
collectiondeclarada:
public static List<Seriado> all() {
return Seriado.collection.find().toArray();
}
Abuscapelo idtambéméfeitapelamesmavariável collection:
public static Seriado findById(String id) {
Seriado seriado = Seriado.collection.findOneById(id);
return seriado;
}
Asoperaçõesdecadastro,alteraçãoeremo çãotambémsãosemelhantes:
// cadastro
Seriado.collection.insert(seriado);
// alteração
Seriado.collection.save(seriado);
// remoção
Seriado.collection.removeById(id);
70

## Página 80

CasadoCódigo Capítulo5. ConversandocomMongoDB
AstelassãobaseadasnotemplatedoPlay,apáginainicialqueexibeos
seriadosrecebealistacomoparâmetro:
@(seriados: List[Seriado])
@import helper._
@main("Seriados") {
@for(seriado <- seriados) {
<a class="alert alert-success" href="/@seriado.id">
@seriado.nome
</a>
}
5.5 Ruby onRails
Sobre oRuby onRails
Em 2004 foi criado um framework em Ruby para acelerar o de-
senvolvimento de aplicações Web MVC. Para aprofundar no uso do
Ruby on Rails, procure pelo livro “Ruby on Rails: coloque sua
aplicaçãowebnostrilhos”(http://www.casadocodigo.com.br/products/
livro-ruby-on-rails).
Oscódigos-fontesdosistemaestãodisponíveisem https://github.com/
boaglio/mongodb-rails-casadocodigo.
O nosso exemplo usará Mongoid, o driver escrito em Ruby (http://
mongoid.org/).
Inicialmentecriamososistemaassim:
rails new mongodb-rails-casadocodigo --skip-active-record
Emseguida,alteramosoarquivo Gemfileadicionandoduaslinhas:
71

## Página 81

5.5. RubyonRails CasadoCódigo
gem 'mongoid', '~> 4', github: 'mongoid/mongoid'
gem 'bson_ext'
CriamosoarquivodeconfiguraçãodeacessoaoMongoDB:
rails g mongoid:config
Comisso,serácriadooarquivo mongoid.ymlcomasconfiguraçõesde
acesso:
development:
sessions:
default:
database: mongodb_rails_casadocodigo_development
hosts:
- localhost:27017
test:
sessions:
default:
database: mongodb_rails_casadocodigo_test
hosts:
- localhost:27017
options:
read: primary
max_retries: 1
retry_interval: 0
Finalmente,geramosateladecadastrodeseriados:
rails generate scaffold seriados nome personagens
Depoisparasubiroservidor:
raisl server
Oresultadoesperadodatelainicialéofigura 5.5.
72

## Página 82

CasadoCódigo Capítulo5. ConversandocomMongoDB
Fig.5.5:TelainicialdoMongoDBcomRubyonRails
5.6 Node.js
Sobre oNode.js
Em2009,foicriadouminterpretadorJavaScriptbaseadonaengine
doGoogleChrome(chamadaV8).Aideiaéusaresseinterpretadorno
servidor,sendocapazdedisponibilizaraplicaçõeswebcommilharesde
conexõessimultâneas.ParaaprofundarnousodoNode.js,procurepelo
livro“Aplicaçõeswebreal-timecomNode.js”(http://www.casadocodigo.
com.br/products/livro-nodejs).
Oscódigos-fontesdosistemaestãodisponíveisem https://github.com/
boaglio/mongodb-nodejs-casadocodigo.
73

## Página 83

5.6. Node.js CasadoCódigo
ParamostrarmosumexemplomaissimplescomoNode.js,usamoso
framework expressparagerenciarasoperaçõesmaiscomuns.
Dentrodapasta seriados,existeoarquivo package.jsoncomas
dependênciasnecessárias:
{
"name": "seriados",
"version": "1.0.0",
"private": true,
"scripts": {
"start": "node ./bin/www"
},
"dependencies": {
"express": "~4.9.0",
"body-parser": "~1.8.1",
"cookie-parser": "~1.3.3",
"morgan": "~1.3.0",
"serve-favicon": "~2.1.3",
"debug": "~2.0.0",
"jade": "~1.6.0",
"mongodb": "*",
"monk": "*"
}
}
Oarquivoprincipaldonode.js(o app.js)possuialgumasvariáveispara
conectaraobancodedados:
var mongo = require('mongodb');
var monk = require('monk');
var db = monk('localhost:27017/test');
Apáginainicialchamaoscript index.js,quefazabuscadacollection
seriadosejoganavariável seriados:
var collection = db.get('seriados');
collection.find({},{},function(e,docs){
res.render('seriados', {
"seriados" : docs
74

## Página 84

CasadoCódigo Capítulo5. ConversandocomMongoDB
});
});
Finalmente,noarquivodetemplate seriados.jadetemosaexibição
dosseriados:
extends layout
block content
each seriado, i in seriados
.btn.btn-primary.btn-lg
<b>#{seriado.nome}</b> com: #{seriado.personagens}
Oresultadoéafigura 5.6.
Fig.5.6:MongoDBcomNode.js
5.7 Qt
Sobre oQt
Em1995,foicriadaalinguagemdeprogramaç ãobaseadaemC++
focadanacriaçãodeinterfacesgráficas.Hojeelaéusadaemmuitasapli-
cações,entreelasoKDE,Skype,Opera,GoogleEarth,VLCeVirtual
Box.
75

## Página 85

5.7. Qt CasadoCódigo
AaplicaçãoemQtpossuiimplementaçãoatravésdeC++eoutraatravés
descriptsnalinguagemQML.
Usandoessalinguagem,vamosconectaraoMongoDBusandoumcom-
ponentenãooficial(http://qt5.jp/mongodb-plugin-for-qml.html):
import me.qtquick.MongoDB 0.1
import QtQuick 2.0
import QtQuick.Controls 1.0
Emseguida,configuramosoacessoaobancodedadoseàcollectionde
seriados:
Database {
id: db
host: '127.0.0.1'
port: 27017
name: 'test'
property Collection
seriados: Collection { name: 'seriados' }
}
OQt,assimcomováriosframeworksweb,utilizaoconceitodeMVC,
portantoalistadosseriados(model)édelegadaaocomponentevisual Text,
queporsuavezutilizaométodo stringify(https://developer.mozilla.
org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
paraconverterodocumentoemtexto.
ListView {
id: lista
anchors.fill: parent
clip: true
model: db.seriados.find({"nome" : "Breaking Bad"})
delegate: Text {
text: JSON.stringify(model.modelData, null, 4)
76

## Página 86

CasadoCódigo Capítulo5. ConversandocomMongoDB
}
}
Fig.5.7:MongoDBcomQt
Oresultadoéafigura 5.7.
5.8 Próximos passos
Certifique-sedequeaprendeu:
• integraçãodoMongoDBcomPHP;
77


## Página 87

5.8. Próximospassos CasadoCódigo
• integraçãodoMongoDBcomJavacomdriveroficial;
• integraçãodoMongoDBcomJavacomSpringData;
• integraçãodoMongoDBcomNode.js;
• integraçãodoMongoDBcomQt.
Nopróximocapítulo,analisaremosumamigraçãodeMySQLparaMon-
goDB,quandoapenasscriptsnãosãosuficienteseémaisinteressantedesen-
volverumaferramentapararealizaramigraç ão.
78

## Página 88

Capítulo6
Migrandooseubancodedados
AmigraçãodebasesrelacionaisparaoMongoDBpodesersimples,naqual
algunsSQLsgeremcomandosparainserireoseusistemaestámigrado.
Entretanto,normalmenteemum schema designadequado,énormalter-
mosváriastabelasconvergindoparaumacollection.
Nessecaso,éinteressantecriarumprogramaauxiliarparaexecutaressa
migração,noqualéfeitaumaleituranabaserelacionaleumcadastrono
MongoDB.
6.1 IMDB simplificado
Os códigos-fontes do sistema estão disponíveis emhttps://github.com/
boaglio/mongodb-migra-imdb-casadocodigo.
OIMDB(InternetMovieDataBase http://imdb.com)éamaiorreferên-
ciadainternetdocinemamundial,quepossuiumgigantescobancodedados

## Página 89

6.1. IMDBsimplificado CasadoCódigo
comtodososfilmeseseusatoresediretores.
Ointeressanteéqueelesdisponibilizamosdadosgratuitamentepara
baixar (ftp://ftp.fu-berlin.de/pub/misc/movies/database/) , e o programa
JMDB(http://www.jmdb.de)éumsoftwarequebaixaessesdadoseinstala
emumabasededadosMySQLlocal.
Abasededadoséenorme,pois,alémdefilmes,incluiseriados(cadaum
dosepisódiosexistentes)evideogamesrelacionadosafilmes.
Paraonossoexemplo,abasededadosfoisimplificadatantonosdados
(temosapenasfilmes),comoemsuaestrutura.
Nessemodelosimplificadoexistemsetetabelas:
mysql> show tables;
+------------------+
| Tables_in_jmdb |
+------------------+
| actors |
| directors |
| genres |
| movies |
| movies2actors |
| movies2directors |
| ratings |
+------------------+
7 rows in set (0,00 sec)
Atabelaquepossuiocadastrodeatores:
mysql> desc actors;
+---------+---------------+------+-----+---------+
| Field | Type | Null | Key | Default |
+---------+---------------+------+-----+---------+
| actorid | mediumint(8) | NO | PRI | NULL |
| name | varchar(250) | NO | | NULL |
| sex | enum('M','F') | YES | | NULL |
+---------+---------------+------+-----+---------+
+----------------+
| Extra |
80

## Página 90

CasadoCódigo Capítulo6. Migrandooseubancodedados
+----------------+
| auto_increment |
| |
| |
+----------------+
3 rows in set (0,00 sec)
Atabelaquepossuiocadastrodediretores:
mysql> desc directors;
+------------+--------------+------+-----+---------+
| Field | Type | Null | Key | Default |
+------------+--------------+------+-----+---------+
| directorid | mediumint(8) | NO | PRI | NULL |
| name | varchar(250) | NO | | NULL |
+------------+--------------+------+-----+---------+
+----------------+
| Extra |
+----------------+
| auto_increment |
| |
+----------------+
2 rows in set (0,00 sec)
Atabeladetiposougênerosdefilmes:
mysql> desc genres;
+---------+--------------+------+-----+---------+-------+
| Field | Type | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| movieid | mediumint(8) | NO | MUL | NULL | |
| genre | varchar(50) | NO | | NULL | |
+---------+--------------+------+-----+---------+-------+
2 rows in set (0,00 sec)
Atabeladetiposougênerosdefilmes:
mysql> desc movies;
+---------+-----------------------+------+-----+---------+
81

## Página 91

6.1. IMDBsimplificado CasadoCódigo
| Field | Type | Null | Key | Default |
+---------+-----------------------+------+-----+---------+
| movieid | mediumint(8) | NO | PRI | NULL |
| title | varchar(400) | NO | | NULL |
| year | varchar(100) | YES | | NULL |
+---------+-----------------------+------+-----+---------+
+----------------+
| Extra |
+----------------+
| auto_increment |
| |
| |
+----------------+
3 rows in set (0,01 sec)
Atabelaauxiliarquerelacionafilmeseatores:
mysql> desc movies2actors;
+---------+---------------+------+-----+---------+-------+
| Field | Type | Null | Key | Default | Extra |
+---------+---------------+------+-----+---------+-------+
| movieid | mediumint(8) | NO | MUL | NULL | |
| actorid | mediumint(8) | NO | MUL | NULL | |
+---------+---------------+------+-----+---------+-------+
2 rows in set (0,00 sec)
Atabelaauxiliarquerelacionafilmesediretores:
mysql> desc movies2directors;
+------------+---------------+------+-----+---------+-------+
| Field | Type | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| movieid | mediumint(8) | NO | MUL | NULL | |
| directorid | mediumint(8) | NO | MUL | NULL | |
| addition | varchar(1000) | YES | | NULL | |
+------------+---------------+------+-----+---------+-------+
3 rows in set (0,00 sec)
Atabeladenotas(de0a10)edequantidadedevotosdosfilmes:
82

## Página 93

6.2. Migrandodeumbancodedadosrelacional CasadoCódigo
6.2 Migrando de um banco de dados relacional
Arotinademigraçãoébemsimples,basicamenteelaconsultaoMySQLpara
montarosdadosedepoisinsereodocumentonacollectiondoMongoDB.
AparteinicialestabeleceaconexãocomoMongoDBedepoisremovea
collectiondefilmes(seelajáexistir):
try {
mongoClient = new MongoClient(
new MongoClientURI("mongodb://localhost")
);
} catch (UnknownHostException e) {
e.printStackTrace();
}
blogDatabase = mongoClient.getDB("test");
filmesCollection = blogDatabase.getCollection("filmes");
filmesCollection.drop();
Em seguida, usamos a classe auxiliarMySQLDAO para consultas ao
MySQL,inicialmentecomalistadefilmes:
List<Filme> filmes = mysqlDAO.getFilmes();
Depoisfazemosumloopdefilmeporfilme,chamandoarotinaauxiliar
adicionarFilme:
for (Filme filme : filmes) {
adicionarFilme(filme.getId(),
filme.getTitulo(),
filme.getAno(),
filme.getNota(),
filme.getVotos());
contador++;
}
Arotina adicionarFilmemontaumdocumentoadicionandovalores
aum BasicDBObject. Aslistasdecategoriasediretoressãopreenchi-
daschamandoasrotinasauxiliares getCategoriase getDiretoresda
classe MySQLDAO:
84

## Página 94

CasadoCódigo Capítulo6. Migrandooseubancodedados
BasicDBObject document = new BasicDBObject();
document.put("_id",movieid);
document.put("titulo",title);
document.put("ano",year);
document.put("nota",rank);
document.put("votos",votes);
document.put("categorias",
mysqlDAO.getCategorias(Long.valueOf(movieid)));
document.put("diretores",
mysqlDAO.getDiretores(Long.valueOf(movieid)));
Porúltimo,temosalistadeatores,ondeinicialmentelemoscomarotina
auxiliar getAtoresdaclasse MySQLDAO:
List<BasicDBObject> atoresMongoDB =
new ArrayList<BasicDBObject>();
List<Ator> atoresMySQL =
mysqlDAO.getAtores(Long.valueOf(movieid));
TemosumloopdeatorporatorretornadodoMySQL,queéadicionado
àlista atoresMongoDB:
for (Ator ator : atoresMySQL) {
BasicDBObject atorMongoDB = new BasicDBObject();
atorMongoDB.put("nome",ator.getNome());
atorMongoDB.put("sexo",ator.getSexo());
atoresMongoDB.add(atorMongoDB);
}
Alistadedocumentosdeatoreséinseridaaodocumento:
document.put("atores",atoresMongoDB);
Finalmente,todoodocumentoéinseridonacollectiondefilmes:
filmesCollection.insert(document);
Oprocessopodedemoraralgumashoras,masacomcertezaabaseserá
migradacomsucesso.
85

## Página 95

6.3. Migrandoparanuvem CasadoCódigo
6.3 Migrando para nuvem
ExistemváriasopçõesdedisponibilizaroMongoDBnanuvem(http://www.
mongodb.com/partners/cloud),masvamosnosfocaraquinoOpenShiftda
RedHat.
Vamoscriarumacontagratuitapelosite https://www.openshift.com/.
Aoentrarmosnosistema,vemosalistadeaplicaçõesinstaladas,eop ção
deadicionarumanova,comoilustradonafigura 6.1.
Fig.6.1:OpenShift listadeaplicações
Diversas opções serão oferecidas, mas escolheremos o JBoss
Application Server 7 Cartridge,conformeafigura 6.2.
86

## Página 96

CasadoCódigo Capítulo6. Migrandooseubancodedados
Fig.6.2:OpenShift listadecomponentes
Depoisdeescolheroservidor,éoferecidaaop çãodeescolheraURL
pública,ondeinformamosovalorde seriados.Vejaafigura 6.3.
Fig.6.3:OpenShift registrandoaplicação
Umavezcriadaaaplicaçãodeseriados,adicionaremosocomponentedo
MongoDB(figura6.4).
87

## Página 97

6.3. Migrandoparanuvem CasadoCódigo
Fig.6.4:OpenShift adicionandoMongoDB
Agoraéinformadaasenhadeacesso(figura 6.5).
Fig.6.5:OpenShift MongoDBadicionado
ParaadministraroMongoDBremotamente,adicionamosocomponente
RockMongo(figura6.6).
88

## Página 98

CasadoCódigo Capítulo6. Migrandooseubancodedados
Fig.6.6:OpenShift adicionandoRockMongo
Depoisdeadicionado,éinformadaasenhadeacesso(figura 6.7).
Fig.6.7:OpenShift RockMongoadicionado
ConseguimosacessaroRockMongocomasenhafornecida(figura 6.8).
89

## Página 99

6.3. Migrandoparanuvem CasadoCódigo
Fig.6.8:OpenShift entrarnoRockMongo
AoentrarnoRockMongo,visualizamostodosascollections(figura6.9).
90

## Página 100

CasadoCódigo Capítulo6. Migrandooseubancodedados
Fig.6.9:OpenShift visãogeral
Atravésdele,podemosimportarumabaselocalcomaop ção import
(figura6.10).
Fig.6.10:OpenShift importarbancodedados
Podemostambémcriarcollectionsnovascomumtamanhoespecíficoe,
senecessário,comaop ção capped,quedeixaacollectioncomumtamanho
fixoeconteúdorotativo,semelhanteaumlogdeservidor(figura6.11).
91

## Página 102

CasadoCódigo Capítulo6. Migrandooseubancodedados
Anossaaplicaçãodeseriadossofreuumapequenaalteraç ãoparafun-
cionarnoOpenShift.
Oscódigos-fontespodemserbaixadosde https://github.com/boaglio/
mongodb-java-springdata-openshift-casadocodigoedepoissubidosparaa
suacontado OpenShift.
Aúnicaalteraçãoocorrenaclassedo SpringMongoConfig,quetrata
daautenticaçãodoMongoDB.
Felizmente, todas as informações de acesso ao
banco de dados estão em variáveis de ambiente
OPENSHIFT_MONGODB_DB_HOST, OPENSHIFT_MONGODB_DB_PORT,
OPENSHIFT_APP_NAME, OPENSHIFT_MONGODB_DB_USERNAME,
OPENSHIFT_MONGODB_DB_PASSWORD, facilmente acessíveis pelo sis-
tema:
host = System.getenv("OPENSHIFT_MONGODB_DB_HOST");
if (host == null) {
host = "127.0.0.1";
}
String sport = System.getenv("OPENSHIFT_MONGODB_DB_PORT");
db = System.getenv("OPENSHIFT_APP_NAME");
if (db == null) {
db = "test";
}
user = System.getenv("OPENSHIFT_MONGODB_DB_USERNAME");
password = System.getenv("OPENSHIFT_MONGODB_DB_PASSWORD");
if (sport != null) {
port = Integer.decode(sport);
} else {
port = 27017;
}
Notequeosvaloresvãofuncionartantoparaumaconexãolocal,quanto
noOpenShift.
Naautenticação,verificamossefoiinformadoousuárioe,emcasoposi-
tivo,usamosaautenticaçãocomusuárioesenha:
if (user != null) {
credential =
93

## Página 105

6.4. Próximospassos CasadoCódigo
Nopróximocapítulo,analisaremosasbuscasmaisavan çadasdoMon-
goDB,sendoalgumasimpossíveisdeserealizaremumbancodedadosrela-
cional.
96

## Página 106

Capítulo7
Buscasavançadas
Comonemtodosistemafazbuscasapenaspelachave,éessencialentender-
mososdiversostiposdebuscaexistentes.
Nocapítulo3aprendemosaseguintesintaxedebusca:
db.<nome-da-collection>.find(
{<campo1>:<valor1>,
<campo2>:<valor2>,
...},
{<campoParaExibir>:<exibeOuNaoExibe>,
<campoParaExibir>:<exibeOuNaoExibe>,
...});
Entretanto,parafazerumabuscamaisabrangente,commaisop ções,o
critériodebuscaédiferentedamaneirarelacional.

## Página 107

7.1. Operadoresdecomparação CasadoCódigo
Vamosparaumexemplodecomobuscarquantossorteiostiverammais
doquecincoganhadores. Nosexemplosaseguir,vamosusarooperador
countapenasparasimplificarosresultados.
db.<nome-da-collection>.find(
{<campo>:
{ <operador> : <valor1>}
).count();
7.1 Operadores de comparação
Nonossoexemplo,temosooperador greater than (oumaiorque)abre-
viadocomo gt.ParaoMongoDBentenderqueeleéumoperadorenãoum
campo,eleéprefixadocomdólar( $):
• MongoDB:
db.megasena.find({ "Ganhadores_Sena" :
{ $gt:4} }).count();
• MySQL:
select count(*)
from megasena
where "Ganhadores_Sena">4
Temosoutrosoperadoressemelhantes:
•$gt:maiorque
•$gte:maiorouigualque
•$lt:menorque
•$lte:menorouigualque
Alémdisso,temosoutrosoperadoresparausartambém,comoooperador
in,quenabuscaaseguircontaototaldesorteioscom5,6ou7ganhadores:
98

## Página 108

CasadoCódigo Capítulo7. Buscasavançadas
> db.megasena.find({"Ganhadores_Sena":{$in:[5,6,7]}}).count()
3
Outrooperadorinteressanteéo ne(not equal/nãoigual),quetrazo
resultadoopostoaocritérioespecificado. Noexemploaseguir,trazemosa
quantidadedesorteiosquenãotêm7ganhadores.
Notequeutilizandoooperador inobtemosovalorcomplementardo
totaldedocumentos:
> db.megasena.find({"Ganhadores_Sena":{$ne:7}}).count();
1607
> db.megasena.find({"Ganhadores_Sena":{$in:[7]}}).count();
1
> db.megasena.find().count()
1608
Senooperador neprecisarmosusarumalistadevalores,utilizamoso
operador nin(not in):
> db.megasena.find().count()
1608
> db.megasena.find({"Ganhadores_Sena":{$nin:[5,6,7]}}).count();
1605
> db.megasena.find({"Ganhadores_Sena":{$in:[5,6,7]}}).count();
3
7.2 Operador distinct
Umoperadorcomumnosbancosrelacionaiséo DISTINCT,queeliminaas
repetiçõesdoresultadodeumaconsulta.
db.<collection>.distinct(<campo>)
ExemplodaquantidadedeganhadoresdaMega-Sena:
> db.megasena.distinct("Ganhadores_Sena")
[ 0, 1, 2, 3, 4, 5, 15, 7 ]
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
99

## Página 110

CasadoCódigo Capítulo7. Buscasavançadas
db.<nome-da-collection>.find({
<operador lógico>:
[ <condição 1>, <condição 2>, ... ]
})
.count();
Nesteexemploosoperadoresretornamexatamenteomesmovalor:
> db.megasena.find({ $or:
[ {"Ganhadores_Sena":{ $eq:5 } },
{"Ganhadores_Sena":{ $eq:7 } }]
}).count();
3
> db.megasena.find({ $or:
[ {"Ganhadores_Sena":5},
{"Ganhadores_Sena":7}]
}).count();
3
> db.megasena.find({"Ganhadores_Sena":{$in:[5,7]} }).count();
3
7.5 Operadores unários
Outrooperadorinteressanteéo exists,queverificaaexistênciadeum
campo.
ComonoMongoDBoschemaéflexível,podendosercriadoumnovo
campoaqualquermomento,éinteressantesabercomoprocurarosdocu-
mentoscomessescamposnovos.
Noexemploaseguir,inicialmenteinserimosumdocumentonovocomo
camponovo obs:
> db.megasena.insert({"obs": "sem sorteio"});
WriteResult({ "nInserted" : 1 })
Agora,alterandoosvaloresdo existspara truee false,podemos
diferenciarosregistroscomonovocampo:
> db.megasena.find().count();
1609
101

## Página 111

7.6. OperadorestiloLIKE CasadoCódigo
> db.megasena.find({"obs":{$exists:true}}).count();
1
> db.megasena.find({"obs":{$exists:false}}).count();
1608
7.6 Operador estiloLIKE
Ooperador likeémuitocomumnasbasesrelacionaisepermitefazerbuscas
portrechosdetextonastabelas. NoMongoDBexisteumcorrespondente,
massemomesmonome.
Inicialmente,listandoosnomesquecontêmapalavra“ad":
> db.seriados.find({ "nome": /ad/},{"nome":1,"_id":0});
{ "nome" : "Carga Pesada" }
{ "nome" : "Breaking Bad" }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.seriados.find({ "nome": /ad/},
{"nome":1,"_id":0});
• MySQL:
select nome
from megasena
where "nome" like '%ad%';
Paraabuscasemconsiderarmaiúsculasouminúsculas,éprecisocolocar
i(de case Insensitive):
> db.seriados.find({ "nome": /bad/},{"nome":1,"_id":0});
> db.seriados.find({ "nome": /bad/i},{"nome":1,"_id":0});
{ "nome" : "Breaking Bad" }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
102

## Página 112

CasadoCódigo Capítulo7. Buscasavançadas
db.seriados.find({ "nome": /bad/i},
{"nome":1,"_id":0});
• MySQL:
select nome
from megasena
where upper("nome") like upper('%ad%')
Parabuscarporpalavrasqueterminamcomumtrechodecaracteres,é
precisocolocar $:
> db.seriados.find({ "nome": /ad/},{"nome":1,"_id":0});
{ "nome" : "Carga Pesada" }
{ "nome" : "Breaking Bad" }
> db.seriados.find({ "nome": /ad$/},{"nome":1,"_id":0});
{ "nome" : "Breaking Bad" }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.seriados.find({ "nome": /ad$/},
{"nome":1,"_id":0});
• MySQL:
select nome
from megasena
where "nome" like '%ad'
Parabuscarporpalavrasqueseiniciamcomumtrechodecaracteres,é
precisocolocar ^:
> db.seriados.find({ "nome": /^Ba/},{"nome":1,"_id":0});
> db.seriados.find({ "nome": /^Br/},{"nome":1,"_id":0});
{ "nome" : "Breaking Bad" }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
103

## Página 113

7.6. OperadorestiloLIKE CasadoCódigo
• MongoDB:
db.seriados.find({ "nome": /^Br/},
{"nome":1,"_id":0});
• MySQL:
select nome
from megasena
where upper("nome") like upper('Br%')
Paraordenaroresultadodaconsulta,usamososufixo sort,especifi-
candoascolunasquedesejamosordenaremordemcrescente(comovalor
1):
> db.seriados.find({},{_id:0,nome:1}).sort({nome:1});
{ "nome" : "Breaking Bad" }
{ "nome" : "Carga Pesada" }
{ "nome" : "Chaves" }
oudecrescente(comovalor-1):
> db.seriados.find({},{_id:0,nome:1}).sort({nome:-1});
{ "nome" : "Chaves" }
{ "nome" : "Carga Pesada" }
{ "nome" : "Breaking Bad" }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.seriados.find({},{_id:0,nome:1})
.sort({nome:-1});
• MySQL:
select nome
from megasena
order by nome desc
104

## Página 114

CasadoCódigo Capítulo7. Buscasavançadas
Paralimitarosresultados,podemosusar limitinformandoaquanti-
dadededocumentosparaexibir:
> db.seriados.find({},{_id:0,nome:1});
{ "nome" : "Chaves" }
{ "nome" : "Carga Pesada" }
{ "nome" : "Breaking Bad" }
> db.seriados.find({},{_id:0,nome:1}).limit(1);
{ "nome" : "Chaves" }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.seriados.find({},{_id:0,nome:1})
.limit(1);
• MySQL:
select nome
from megasena
limit 1
Alémdelimitarcom limit,podemosinformaraquantidadededocu-
mentosparapularantesdeexibircom skip:
> db.seriados.find({},{_id:0,nome:1});
{ "nome" : "Chaves" }
{ "nome" : "Carga Pesada" }
{ "nome" : "Breaking Bad" }
> db.seriados.find({},{_id:0,nome:1}).limit(1).skip(2);
{ "nome" : "Breaking Bad" }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.seriados.find({},{_id:0,nome:1})
.limit(1).skip(2);
105

## Página 116

CasadoCódigo Capítulo7. Buscasavançadas
7.8 Próximos passos
Certifique-sedequeaprendeu:
• operaçõesdebuscacomoperadoresdecomparação;
• operaçõesdebuscacomoperadoreslógicos;
• operaçõesdebuscacomoperadoresunários;
• operaçõesdebuscaestiloLIKE;
• operaçõesdeordenação.
Nopróximocapítulo,usaremososuportegeoespacialdoMongoDBpara
trabalharfacilmentecomcoordenadasedistâncias.
107

## Página 118

Capítulo8
Buscageoespacial
Quandofalamossobregeoespacial,significamanipularinformaçõesemduas
outrêsdimensões.
Trabalharcomcoordenadasemumbancodedadosnãoéalgomuitoin-
comum,entretantousarrotinasnativasquecalculamautomaticamenteadis-
tânciaentrecoordenadassimplificammuitoodesenvolvimentodesistemas.
Vamosmostrarumexemplodecalcularadistânciadeduascidadesamer-
icanas.
Ocódigo-fontedaaplicaçãoeo dumpdobancodedadosestãoem https:
//github.com/boaglio/mongodb-java-geospatial-springdata-casadocodigo.
8.1 O banco de dados
Pararestaurarobancodedados,faç aospassosaseguir(entendacommais
detalhesnocapítulo 11):

## Página 120

CasadoCódigo Capítulo8. Buscageoespacial
"y" : 25.661502
}
}
AtéentãoéumbancodedadoscomumdoMongoDB.Oqueativaouso
dasinformaçõesgeoespaciaiséacriaçãodeumíndicedessetipo.
Veremosmaisdetalhesdecriaçãodeíndicesnocapítulo 10,masnesse
casobastainformarocampoparaindexarascoordenadascomessasintaxe:
db.<collection>.ensureIndex( { <campo-com-coordenadas> : "2d" } )
Nonossobancodedados:
db.zipcodes.ensureIndex( { loc : "2d" } )
Comesseíndice,conseguimosbuscarascidadespróximasemradianos
comocomando nearutilizandoasintaxe:
db.<collection>.find( { <campo-com-coordenadas>:
{ $near : [ <coordenada>,<coordenada>],
$maxDistance: <distancia> }
} )
Exemplodascidadesa0.1radianosdeMiami:
db.zipcodes.find( { 'loc':
{ $near : [ 80.441031,25.661502],
$maxDistance: .1 } },
{ _id:0, "city":1,"state":1 } )
{
"city" : "MIAMI",
"state" : "FL"
}
{
"city" : "OLYMPIA HEIGHTS",
"state" : "FL"
}
Seaumentarmosadistância,consequentementeaparecemmaiscidades
vizinhas:
111

## Página 121

8.2. Usandoosistemaweb CasadoCódigo
db.zipcodes.find( { 'loc':
{$near : [ 80.441031,25.661502],
$maxDistance: .1 } }).count()
2
db.zipcodes.find( { 'loc':
{$near : [ 80.441031,25.661502],
$maxDistance: .5 } }).count()
31
db.zipcodes.find( { 'loc':
{$near : [ 80.441031,25.661502],
$maxDistance: 1 } }).count()
54
8.2 Usando o sistema web
Inicialmente, o sistema busca duas listas de cidadespara escolher, como
mostraafigura 8.1.
Fig.8.1:CalculandoadistânciaentreMiamieOrlando
112

## Página 122

CasadoCódigo Capítulo8. Buscageoespacial
Emseguida,exibeomapadasduascidadeseadistânciaentreelasesuas
cidadesvizinhas,comomostraafigura 8.2.
Fig.8.2:ExibindooresultadodadistânciaentreMiamieOrlando
8.3 Entendo o sistema web
SeguindoopadrãodoSpringData,osistemamapeiaascidadescomaclasse:
@Document(collection = "zipcodes")
public class Zip {
@Id
private ObjectId id;
private String city;
private String state;
private Loc loc;
113

## Página 123

8.3. Entendoosistemaweb CasadoCódigo
Napáginainicial,exibeduaslistasordenadasdecidades,queelebuscada
classe ZipsRepository:
List<Zip> zips = new ArrayList<Zip>();
Query query = new Query();
query.with(new Sort(Sort.Direction.ASC,"city"));
zips = mongoTemplate.find(query,Zip.class);
Ousuárioescolheacidadeorigemeadestino, easinformaçõessão
enviadas à classe ZipcodesController, e usamos a rotina auxiliar
CalculaDistanciapararetornarosdadosemquilômetros:
Zip zip1 = repository.findById(idCidadeOrigem);
Zip zip2 = repository.findById(idCidadeDestino);
double distancia = CalculaDistancia.distance(
zip1.getLoc().getX(),zip1.getLoc().getY(),
zip2.getLoc().getX(),zip2.getLoc().getY());
Atéaquinãotemosnadademaisdoquejáfoiusadoequalquercadastro
decoordenadaspoderiafazer.
Entretanto,odiferencialéessaconsultadecidadesvizinhas,ondeinfor-
mamosapenasascoordenadasdacidadeeotamanhodoraiodadistância.O
bancodedadosautomaticamentecalculaalistadascidadespróximas.
Criamosumaclassedotipo Criteriaparadefinirabuscageoespacial
comocomando near:
public List<Zip> findCidadesProximas(Double x,Double y) {
List<Zip> zips = new ArrayList<Zip>();
Criteria criteria = new Criteria("loc")
.near(new Point(x,y))
.maxDistance(
CalculaDistancia.getInKilometer(RAIO_DE_DISTANCIA_EM_KM)
);
Executamosabuscaelimitamosoresultadodascidadesvizinhascom
limit:
114

## Página 124

CasadoCódigo Capítulo8. Buscageoespacial
Query buscaCidades = new Query(criteria);
zips = mongoTemplate.find(
buscaCidades.limit(11),Zip.class);
8.4 Indo além
Comcerteza,osistemapodesermelhorado.Alémdisso,oMongoDBoferece
váriosrecursosparatrabalharcomcoordenadas,enãosó,maspolígonose
estruturasmaiscomplexas.ParatalexisteoGeoJSON(http://geojson.org/)e
seusoperadores.
8.5 Próximos passos
Certifique-sedequeaprendeu:
• acriaríndicegeospacialemcampocomcoordenadas;
• autilizarooperadornear.
Nopróximocapítulousaremoso aggregationframeworkparafacilmente
extrairimportantesinformaçõesdobancodedados.
115

## Página 126

Capítulo9
AggregationFramework
Dequeadiantacontermuitosdadossenãoforpossívelextrairinformaç ão
deles?
Époressemotivoqueagrupamososdadosconformeanecessidadepara
conseguirodetalhamentonecessário,oquenosbancosrelacionaisnormal-
menteéfeitocomocomando GROUP BY.
Entretanto,noMongoDBnãoexisteapenasumcomandosemelhante,ex-
istenaverdadealgobemmaisrobustoecompletochamado aggregation
framework(frameworkdeagrupamento),oqueveremosadiantecomousar.
9.1 Por que não usar MapReduce
Oaggregationframeworksurgiunaversão2.2doMongoDB,edesdeentãose
tornouumaversãomaissimplesecommaisperformancedoqueotradicional
map reduce.

## Página 127

9.1. PorquenãousarMapReduce CasadoCódigo
O map reduceéummodelodeprogramaçãocriadopelaGoogleparatra-
balharcommuitosdadosesercapazdeexecutartarefasemparalelocomo
objetivodeatingiroresultadodemaneiramaisrápidaeeficiente.
Fig.9.1:Fazendohotdogcomesemmapreduce
Nafigura9.1,vemosduasmaneirasdefazerumhotdog:atradicional(e
sequencial),emqueumatarefaéfeitaapósaoutra:primeiroassamosopão,
depoiscozinhamosasalsicha.
Com map reduce,conseguimosparalelizaralgumastarefas: umcozin-
heiroassaopãoenquantoooutrocozinhaasalsicha.
Seaideiaforfazercincohotdogs,nãotemmuitadiferen çaemusarqual-
querumadasmaneiras,masseoobjetivoforcincomilunidades,comcerteza
asegundaop çãoéamaiseficiente.
Vamosparaumexemplonanossacollectiondossorteios.
Inicialmentedefinimosafun çãodemapeamentodaquantidadedegan-
hadoresagrupadopelospela flagdeacumulado(SouN):
118

## Página 128

CasadoCódigo Capítulo9. AggregationFramework
map = function() {
emit(this.Acumulado , this.Ganhadores_Sena );
}
Emseguida,definimosafun ção reducequeseráchamadaparacada
agrupamento,sendoqueelasomaaquantidadedeganhadoresdeMega-Sena.
reduce = function(Acumulado, Ganhadores_Sena) {
return Array.sum(Ganhadores_Sena);
}
Finalmente,criaremosacollection ganhadores,emqueaplicaremoso
map reduce:
result = db.runCommand({
"mapreduce" : "megasena",
"map" : map,
"reduce" : reduce,
"out" : "ganhadores"})
Fazendoumaconsultanacollectioncriada,percebemosqueemtodosos
sorteiosemqueacumulou(SIM),ninguémganhou.
Jánossorteiosemquenãoacumulou(NÃO),533pessoasganharama
Mega-Sena.
> db.ganhadores.find();
{ "_id" : "NÃO", "value" : 533 }
{ "_id" : "SIM", "value" : 0 }
9.2 Explorando o Aggregation Framework
Asintaxedoaggregationframeworkébemdiferentedotradicional GROUP
BY.
Emnossoexemplomaissimples,vamosaplicarumafun çãodegrupoem
umcampo,comaseguintesintaxe:
db.collection.aggregate( { $group :
{ _id : null,
<nome-do-campo>:{
119

## Página 129

9.2. ExplorandooAggregationFramework CasadoCódigo
<função-de-grupo>:"$<nome-do-campo-para-agrupar>"
}
}
});
Vamos,porexemplo,somarosganhadoresdaMega-Sena:
> db.megasena.aggregate( { $group :
{_id:null,
soma:{$sum:"$Ganhadores_Sena"}
}});
{ "_id" : null, "soma" : 533 }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.megasena.aggregate( { $group :
{_id:null,
soma:{$sum:"$Ganhadores_Sena"}
}});
• MySQL:
select sum(Ganhadores_Sena)
from megasena
Vamosadicionartambémaopçãoparaexibirototaldesorteioseamédia
deganhadores:
> db.megasena.aggregate({ $group: {
_id: null,
total: { $sum: 1 } ,
soma: { $sum: "$Ganhadores_Sena" } ,
avg: { $avg: "$Ganhadores_Sena" }
} });
{ "_id" : null, "total" : 1607,
"soma" : 533, "avg" : 0.3316739265712508 }
120

## Página 130

CasadoCódigo Capítulo9. AggregationFramework
Peloresultado,percebemosquealémdos533ganhadorestemosaotodo
1607sorteiose,emmédia,0.33deganhadoresporsorteio,ouseja,aproxi-
madamenteumganhadorparacada3sorteios.
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.megasena.aggregate( { $group :
{_id:null,
total: { $sum: 1 } ,
soma: { $sum: "$Ganhadores_Sena" } ,
avg: { $avg: "$Ganhadores_Sena" }
}});
• MySQL:
select count(Ganhadores_Sena),
sum(Ganhadores_Sena),
avg(Ganhadores_Sena),
from megasena
Vamosagoraagruparporumcampo.Asintaxemudaumpouco:
db.collection.aggregate( { $group :
{ _id : <nome-do-campo>,
<nome-do-campo>:{
<função-de-grupo>:"$<nome-do-campo-para-agrupar>"
}
}
});
Oexemploaseguirretornaexatamenteomesmoresultadoqueoexemplo
de map reducedocomeçodocapítulo.
> db.megasena.aggregate({ $group: {
_id: "$Acumulado",
soma: { $sum: "$Ganhadores_Sena" }
} });
{ "_id" : "NÃO", "soma" : 533 }
{ "_id" : "SIM", "soma" : 0 }
121

## Página 131

9.2. ExplorandooAggregationFramework CasadoCódigo
Bemmaissimplesqueusaro map reduce,não?
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.megasena.aggregate({ $group: {
_id: "$Acumulado",
soma: { $sum: "$Ganhadores_Sena" }
} });
• MySQL:
select Ganhadores_Sena,
sum(Ganhadores_Sena)
from megasena
group by Acumulado;
Sedepoisdeagrupadososresultadosprecisarmosfazerumfiltro,deve-
mosusaro match:
db.collection.aggregate( { $group :
{ _id : <nome-do-campo>,
<nome-do-campo>:{
<função-de-grupo>:"$<nome-do-campo-para-agrupar>"
}
}
},
{ $match : {<filtro>} }
);
Noexemplo,vamoslistarapenasosresultadoscomsomamaiorquezero:
db.megasena.aggregate({ $group: {
_id: "$Acumulado",
soma: { $sum: "$Ganhadores_Sena" }
}} ,
{ $match : { soma : { $gt : 0 }}}
);
{ "_id" : "NÃO", "soma" : 533 }
122

## Página 132

CasadoCódigo Capítulo9. AggregationFramework
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.megasena.aggregate({ $group: {
_id: "$Acumulado",
soma: { $sum: "$Ganhadores_Sena" }
} },
{ $match : { soma : { $gt : 0 }}}
);
• MySQL:
select Acumulado,
sum(Ganhadores_Sena)
from megasena
group by Acumulado
having sum(Ganhadores_Sena)>0;
Vamosagoraagruparpormaisdeumcampoeordenaroresultado:
db.collection.aggregate( { $group :
{ _id : { <apelido1> : $<nome-do-campo1>,
<apelido2> : $<nome-do-campo2>,
... }
<nome-do-campo>:{
<função-de-grupo>:"$<nome-do-campo-para-agrupar>"
}
},
{ $sort : { _id: -1 } }
} );
ListaremosaquantidadedeganhadoresdaMega-Senaagrupadostam-
bémpelaflagdeseoprêmioestáacumulado;tudoordenadopelaquantidade
deganhadoresemordemdecrescente:
> db.megasena.aggregate({ $group: {
_id: { ganhadores_sena:"$Ganhadores_Sena",
acumulado: "$Acumulado" },
123

## Página 133

9.2. ExplorandooAggregationFramework CasadoCódigo
soma: { $sum: "$Ganhadores_Sena" }
} },
{ $sort : { _id: -1 } } );
{"_id":{ "ganhadores_sena":15, "acumulado":"NÃO" }, "soma" : 15 }
{"_id":{ "ganhadores_sena":7, "acumulado":"NÃO" }, "soma" : 7 }
{"_id":{ "ganhadores_sena":5, "acumulado":"NÃO" }, "soma" : 10 }
{"_id":{ "ganhadores_sena":4, "acumulado":"NÃO" }, "soma" : 32 }
{"_id":{ "ganhadores_sena":3, "acumulado":"NÃO" }, "soma" : 54 }
{"_id":{ "ganhadores_sena":2, "acumulado":"NÃO" }, "soma" : 136 }
{"_id":{ "ganhadores_sena":1, "acumulado":"NÃO" }, "soma" : 279 }
{"_id":{ "ganhadores_sena":0, "acumulado":"SIM" }, "soma" : 0 }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.megasena.aggregate({ $group: {
_id: { ganhadores_sena:"$Ganhadores_Sena",
acumulado: "$Acumulado" },
soma: { $sum: "$Ganhadores_Sena" }
} },
{ $sort : { _id: -1 } } );
• MySQL:
select Ganhadores_Sena,
Acumulado,
sum(Ganhadores_Sena)
from megasena
group by Ganhadores_Sena, Acumulado
order by Ganhadores_Sena desc;
Paraefetuarmosagrupamentosdeagrupamentos,bastaadicionarmais
umachave groupaofinal.
Noexemploanterior,vamosagruparnovamenteparasomartodososgan-
hadoresdaMega-Sena:
> db.megasena.aggregate({ $group: {
_id: { ganhadores_sena:"$Ganhadores_Sena",
124

## Página 134

CasadoCódigo Capítulo9. AggregationFramework
acumulado: "$Acumulado" },
soma: { $sum: "$Ganhadores_Sena" }
} },
{
$group: {
_id: null,
soma_total: { $sum: "$soma" }
}
} );
{ "_id" : null, "soma_total" : 533 }
Fazendoumaanalogiaaosbancosdedadosrelacionais,temos:
• MongoDB:
db.megasena.aggregate({ $group: {
_id: { ganhadores_sena:"$Ganhadores_Sena",
acumulado: "$Acumulado" },
soma: { $sum: "$Ganhadores_Sena" }
} },
{
$group: {
_id: null,
soma_total: { $sum: "$soma" }
}
} );
• MySQL:
select sum(soma) soma_total
from ( select Ganhadores_Sena,
Acumulado,
sum(Ganhadores_Sena) soma
from megasena
group by Ganhadores_Sena, Acumulado)
Para mais exemplos, acesse a documentação oficial em http://docs.
mongodb.org/manual/reference/sql-aggregation-comparison/.
125

## Página 135

9.3. Próximospassos CasadoCódigo
9.3 Próximos passos
Certifique-sedequeaprendeu:
• oconceitogeraldomap reduce;
• ofuncionamentoeusodoaggregationframework.
Nopróximocapítulo,veremoscomomelhoraraperformancedoMon-
goDB,analisandoosistemacomoumtodoemelhorandootempodeconsul-
tas.
126

## Página 137

CasadoCódigo
...
}
Nessalistatemos:
•count:totalderegistrosdacollection;
•nindexes:quantidadedeíndicescriados;
•indexSizes: nomeetamanhodosíndices,porpadrãotemosum
índiceparaocampo _id.
Usandoocomando explain,podemosextrairinformaçõesimportantes
deumaconsulta.
Novamentevamosdestacarapenasoqueinteressa:
> db.filmes.find({"ano" :"1999"}).explain();
{
...
"cursor" : "BasicCursor",
"n" : 8097,
"nscanned" : 511010,
"millis" : 198,
...
}
Issosignificaque,pelainformaçãodocampo cursor,nenhumíndice
foiusadonabusca.Ocampo nrepresentaaquantidadededocumentosre-
tornadosdabusca,ouseja,acollectionpossui8097filmesdoanode1999.
Ocampo nscannedéaquantidadededocumentosqueoMongoDBleu
antesderetornaroresultado.Comparandocomaconsultaanterior,percebe-
mosqueaquantidadederegistrosqueeleleuéexatamenteotamanhoda
collection,ouseja,elevarreuacollectioninteirapararetornaroresultado,o
quenosbancosrelacionaischamamosde Full Table Scan.
Otempodaexecuçãoémedidopelocampo millis.Nestecaso,foi198
milissegundos.
128

## Página 138

CasadoCódigo Capítulo10. Aumentandoaperformance
10.1 Criar um índice
Pararesolveresseproblema,vamoscriarumíndicecomaseguintesintaxe:
db.collection.ensureIndex(
{ <campo1> : <ordem>,
<campo2> : <ordem>,
...} );
Aordempodeserdefinidacom1paracrescenteou-1paradecrescente,
maselaéimportanteapenasparaíndicecomposto;emcampocomíndice
simplesnãoimportaaordem.
Vamoscriarumíndiceparaocampoqueusamosnabusca:
db.filmes.ensureIndex( { "ano" : 1 } )
Emseguida,rodamosnovamenteo explainparaverificarasdiferen ças:
> db.filmes.find({"ano" :"1999"}).explain();
{
...
"cursor" : "BtreeCursor ano_1",
"n" : 8097,
"nscanned" : 8097,
"millis" : 18,
...
}
Vejaumexemplodecriaçãodeumíndicecompostopeloscampos ano
comordemcrescentee notacomordemdecrescente:
db.filmes.ensureIndex( { "ano" : 1 , "nota" : -1 } )
Inicialmenteverificamospelocursorquefoiusadoonossoíndicedo
campoano,eaquantidadederegistrosretornadoscontinua8097.
Entretanto,ocampo nscannedretornou8097emvezde511010,epelo
campo millisvemosqueotempocaiude198para18milissegundos.
129

## Página 139

10.2. Listarosíndicescriados CasadoCódigo
10.2 Listar os índices criados
Paralistarosíndicescriados,usamosasintaxe:
db.collection.getIndexes();
Porexemplo:
> db.filmes.getIndexes();
[
{
"v" : 1,
"key" : { "_id" : 1 },
"name" : "_id_",
"ns" : "test.filmes"
},
{
"v" : 1,
"key" : { "ano" : 1 },
"name" : "ano_1",
"ns" : "test.filmes"
},
]
10.3 Remover um índice criado
Pararemoverumíndiceexistente,usamosasintaxe:
db.collection.dropIndex(<nome-do-indice>);
Vamosresolvernossoíndicecriado:
> db.filmes.dropIndex("ano_1");
{ "nIndexesWas" : 2, "ok" : 1 }
> db.filmes.getIndexes();
[
{
"v" : 1,
"key" : { "_id" : 1 },
"name" : "_id_",
130

## Página 140

CasadoCódigo Capítulo10. Aumentandoaperformance
"ns" : "test.filmes"
}
]
Oíndicedocampo _idnãopodeserremovido.Aotentarremovê-lo,o
MongoDBexibiráumamensagemdeerro.
> db.filmes.dropIndex("_id_");
{"nIndexesWas" : 1, "ok" : 0,"errmsg" : "cannot drop _id index"}
10.4 Índice textual
Abuscatextual(text search ou full text search)existenoMongoDBdesdea
versão2.4eéativaporpadrãodesdeaversão2.6.
Comela,épossívelfazerumabuscanãoapenasporumtrechodetexto,
mastambémporaproximaçõesdomesmotexto.
Asintaxeparacriarumíndicetextualou text indexé:
db.collection.ensureIndex({<campo>: "text"},
{default_language: <idioma>} );
Oparâmetro default_languageéopcional;seomitido,oíndiceé
criadonoidiomainglês.
Vamoscriarumíndicetextualemportuguêsparaacollectiondetextos:
> db.textos.ensureIndex( {texto: "text"},
{default_language: "portuguese"} );
{
"createdCollectionAutomatically" : false,
"numIndexesBefore" : 1,
"numIndexesAfter" : 2,
"ok" : 1
}
Vamoscadastrarumafrasesimples:
> db.textos.insert({texto: "Eu gosto de São Paulo"});
WriteResult({ "nInserted" : 1 })
131

## Página 142

CasadoCódigo Capítulo10. Aumentandoaperformance
"createdCollectionAutomatically" : false,
"numIndexesBefore" : 1,
"numIndexesAfter" : 2,
"ok" : 1
}
10.5 Criar índice em background
Nomomentoemqueoíndiceécriado,asoperaçõesdeleituraeescritasão
bloqueadasatéqueoíndicesejacriadocompletamente.
Paraevitaressebloqueio,épossívelcriaroíndiceembackground,con-
formeoexemplodeíndicesimples:
> db.textos.ensureIndex( { "texto": 1},
{background: true} );
{
"createdCollectionAutomatically" : false,
"numIndexesBefore" : 2,
"numIndexesAfter" : 3,
"ok" : 1
}
Eíndicetextual:
> db.textos.ensureIndex( { "$**": "text"},
{default_language: "portuguese"} ,
{background: true} );
{
"createdCollectionAutomatically" : false,
"numIndexesBefore" : 1,
"numIndexesAfter" : 2,
"ok" : 1
}
Acriaçãodeumíndiceembackgrounddemoraumpoucomaisdoqueo
padrão.
133

## Página 143

10.6. Próximospassos CasadoCódigo
10.6 Próximos passos
Certifique-sedequeaprendeu:
• afazeroexplaindeumaconsulta;
• aanalisaroresultadodeumexplain;
• acriareremoveríndicessimplesecompostos;
• acriaríndicesdebuscatextual;
• acriaríndicesembackground.
Nopróximocapítulo,veremosalgumastarefasadministrativas,comoati-
varautenticação,gerenciar backupse restoresdobancodedados.
134

## Página 144

Capítulo11
MongoDBparaadministradores
Sevocêéadministradordebancodedados,certamenteachouumabsurdoo
MongoDBsertãoabertoenãoexigirnenhumaautenticaç ãoparatrabalhar.
Elefoifeitodessamaneiraporpadrãoparafacilitarodesenvolvimento,
masevidentementeépossívelativaraautenticação,assimcomodefinirperfis
(roles)diferentesparaexecutartarefasespecíficas.
Veremosadianteodiaadiadealgumastarefasdeadminscomousode
storage,gerenciamentodeusuáriosebackup/restore.
11.1 Ajuste de performance
Amaioriadosbancosdedadosdelegaduastarefasaosadministradores:ajus-
tarosistemaoperacionaldamáquinaalémdobancodedados.
Écomumverservidoressubutilizadoscombancosdedados,porexem-
plo,oMySQL5tememseuparâmetro innodb_buffer_pool_sizeo

## Página 145

11.2. Gerenciandoespaçoemdisco CasadoCódigo
valorpadrãode128Mb. Seinstaladoemumservidorparrudode64Gbde
memóriaRAM,eleutilizarámenosde1%dacapacidadedamáquina.
Nessecaso,cabeaoDBAajustarosparâmetrosdobancodedadospara
seadequaraoservidor.ComMongoDBédiferente.
Depoisdeconfigurarosistemaoperacional, oMongoDBassumeque
“possousaramáquinaàvontade”eassimelevaiconsumirbemapartede
memóriadedisco,oqueforidealparagarantirumaboaperformancede
acessoaosdadosdascollectionsdobancodedados.
Seforpossívelalocaracollectioninteiranamemóriaparagarantiruma
boaperformance,oMongoDBfaráissosemdódeseuservidoreoqueestiver
rodandojuntocomele,desdequeelepercebaqueorecurso(memória)esteja
livreparauso.
ComooMongoDBtemessecomportamento,éumaboapráticaterum
servidor(ouumamáquinavirtual)dedicadoaisso.
11.2 Gerenciando espaço em disco
Paraobtermelhorperformanceeevitarproblemascomfragmentaç ãodear-
quivos,oMongoDBpré-alocaseusarquivosdedados.
Conformeobancodedadoscresce,elevaialocandomaisemaisespaço,
mesmoquenãonecessitenaquelemomento.
ComooMongoDBpossuiessecomportamento,éinteressantedetempos
emtemposexecutarocomando repairDatabaseparareescrevertodoo
bancodedadoseotimizaroespaçoutilizado.
> db.repairDatabase();
{ "ok" : 1 }
Seocorreuum crashnoservidor,ouaquelaeventualfaltadeenergia,
mesmoqueobancodedadossubanormalmente,éumaboapráticaexecutar
ocomando repairDatabaseparacorrigiralgumproblema,seexistir.
Éimportantesaberque,paraessecomandoserexecutadocomsucesso,é
necessárioexistiroespaçolivredepelomenosotamanhodobancodedados
atualemais2Gb.Issoaconteceporqueocomandoreescrevetodoobanco
dedadosemnovosarquivos,edepoisefetuaatrocadosantigospelosnovos.
Algunsexemplos:
136

## Página 146

CasadoCódigo Capítulo11. MongoDBparaadministradores
• tamanhodobancodedados:10Gb=espaçolivremínimonecessário:
22Gb
• tamanhodobancodedados:30Gb=espaçolivremínimonecessário:
62Gb.
Existetambémocomando compactcomamesmafinalidadequeo
repairDatabase,maséexecutadoparacadacollectionenãoparaobanco
dedadosinteiro.Entretanto,depoisdeexecutado,elenãoliberaespaçoem
disco.
> db.runCommand ( { compact: '<nome-da-collection>' } )
Exemplo:
> db.runCommand ( { compact: 'filmes' } )
{ "ok" : 1 }
11.3 Autenticação
Porpadrão,obancodedadosnãooferecenenhumaautenticaç ão,poisofoco
éfacilidadenouso,contudo,emumaempresaémuitoarriscadodeixaro
bancodedadosdessamaneira.
OMongoDBofereceautenticaçãoemváriosníveis,porbancodedados
ouporcollections,alémdesuporteaperfis(roles).
Existemdiferentesestratégiasparamontarumaautenticaç ãocomoum
todo. Vamoslistaraquiastarefasmaiscomunsqueenvolvempraticamente
todasasnecessidadesdeumDBA.
Adicionarautenticação
Paraadicionarautenticação,usamosobancodedados admineadi-
cionamos rolesexistentes. Emseguida,alteramosoarquivodeconfigu-
raçãodoMongoDBereiniciamososerviço.
Asintaxeparaadicionaraautenticaçãoé:
use admin
db.createUser({user: "<nome-do-usuario>",
137

## Página 147

11.3. Autenticação CasadoCódigo
pwd: "<senha-do-usuario>",
roles:[ "userAdminAnyDatabase",
"dbAdminAnyDatabase",
"readWriteAnyDatabase"]})
Exemplo:
use admin
db.createUser({user: "admin",
pwd: "minhasenha",
roles:[ "userAdminAnyDatabase",
"dbAdminAnyDatabase",
"readWriteAnyDatabase"]})
db.createUser({user: "outroAdmin",
pwd: "minhasenha",
roles:[ "userAdminAnyDatabase",
"dbAdminAnyDatabase",
"readWriteAnyDatabase"]})
Depois,énecessárioalteraroarquivodeconfiguraçãodoMongoDB(nor-
malmenteem /etc/mongodb.conf)eadicionaroparâmetrodeautenti-
cação,quepodeser security.authorizationou auth,amboscomo
valor true.
Alistacompletadeop çõesdeconfiguraçãoestádisponívelemhttp://docs.
mongodb.org/manual/reference/configuration-options/.
Autenticaçãoporbancodedados
Comoécomumexistirumaaplicaçãoqueutilizediversascollections,é
umaboaabordagemcriarumbancodedadosporaplicaç ãoecriarumaaut-
enticaçãodentrodele,permitindolereescrever.
Paracadastrarumusuárioadministradornobancodedados:
use <meu-banco-de-dados>
db.createUser(
{
user: "<nome-do-usuario-admin>",
pwd: "<senha-do-usuario-admin>",
roles: [
138

## Página 148

CasadoCódigo Capítulo11. MongoDBparaadministradores
{ role: "readWrite", db: "<meu-banco-de-dados>" }
]
}
)
Exemplo:
use meubanco
db.createUser(
{
user: "usuarioAdmin",
pwd: "minhasenha",
roles: [
{ role: "readWrite", db: "meubanco" }
]
}
)
Outranecessidadecomumécriarumusuáriosódeleitura.Nessecaso,a
sintaxeéparecida,apenasa rolemuda:
use <meu-banco-de-dados>
db.createUser(
{
user: "<nome-do-usuario-de-leitura>",
pwd: "<senha-do-usuario-de-leitura>",
roles: [
{ role: "read", db: "<meu-banco-de-dados>" }
]
}
)
Exemplo:
use meubanco
db.createUser(
{
user: "usuarioSomenteLeitura",
pwd: "minhasenha",
roles: [
139

## Página 149

11.4. Programasexternos CasadoCódigo
{ role: "read", db: "meubanco" }
]
}
)
11.4 Programas externos
OMongoDBoferecealgunsprogramasqueauxiliamnaanálisedeperfor-
mance,vamosdestacardoisdelesaseguir.
mongostat
Oprograma mongostatfuncionademaneirasemelhanteao vmstat
existenteemalgunssistemasoperacionaisUNIX,quetemoobjetivodein-
formardemaneirageralasoperaçõesdeconsulta,atualizaç ão,alocaçãode
memóriavirtual,operaçõesderedeeconexõesexistentes.
Parachamaroprograma,digite:
mongostat
Consulte a documentação oficial para mais detalhes:http://docs.
mongodb.org/manual/reference/program/mongostat/.
Nafigura11.1temosoexemploda base test emuso.
Fig.11.1:mongostatexibindooperaçõesnobancotest
140

## Página 150

CasadoCódigo Capítulo11. MongoDBparaadministradores
mongotop
Oprograma mongotopfuncionademaneirasemelhanteao topexis-
tenteemalgunssistemasoperacionaisUNIX,quetemoobjetivodeinformar
osprocessosmaispesados,queestãoconsumindomaisrecursodobancode
dados.
Parachamaroprograma,digite:
mongotop
Consulte a documentação oficial para mais detalhes:http://docs.
mongodb.org/manual/reference/program/mongotop/.
Nafigura 11.2temosoexemplodacollectionfilmesda base test em
uso.
Fig.11.2:mongotopexibindooperaçõesnacollectionfilmesdobancotest
Programasexternos
Seaautenticaçãoforativada,éprecisoconcederaousuáriooprivilégio
darole rootparaexecutaressesprogramasexternos,atravésdaseguinte
sintaxe:
db.grantRolesToUser("<usuario>",[{role:"root",db: "admin"}]);
Exemplo:
db.grantRolesToUser("admin",[{role:"root",db: "admin"}]);
Emseguida,parainiciaroprogramaexterno,énecessárioinformaros
parâmetrosparaautenticação:
141

## Página 151

11.5. Backup CasadoCódigo
mongotop --authenticationDatabase <banco-de-dados-admin>
-u <usuário-administrador>
-p <senha-do-administrador>
Exemplo:
mongotop --authenticationDatabase admin -u admin -p admin
Osoutrosprogramas,comoo mongoconsoleouo mongostatrecebem
osmesmosparâmetrosparaefetuarautenticação.
11.5 Backup
Operaçõesdebackupdosdadossãoessenciaisparagarantirobomfunciona-
mentoeumarestauraçãorápidasenecessário.
Backupfrio
Obackupdetudocombancoforadoar(conhecidocomo backup frio)é
efetuadocomocomando mongodump,comessasintaxe:
<derruba-serviço-do-MongoDB>
mkdir <diretorio-de-backup>
cd <diretorio-de-backup>
mongodump --dbpath <diretorio-de-dados-do-mongodb>
<sobe-serviço-do-MongoDB>
ExemploemLinux:
service mongod stop
mkdir /bkp/dados/
cd /bkp/dados/
mongodump --dbpath /var/lib/mongodb/
service mongod start
Osarquivosdobancodedadosserãogeradosdentrododiretório dump
emquefoiexecutadoo mongodump.Dentrodele,serãocriadossubdiretórios
decadabancodedados,edentrodecadaumdelesteremosdoisarquivospara
cadacollection:umarquivopequenocomosmetadadosdacollection,nome
142

## Página 152

CasadoCódigo Capítulo11. MongoDBparaadministradores
einformaçãodosíndices( <nome-da-collection>.metadata.json)e
outromaior,quecontémosdadosdacollectionemformato Binary JSON
(BSON).
Uma alternativa mais lenta, mas também interessante, é o comando
mongoexport,quepermiteexportarosdadosemformato CSVou JSON.
Asuasintaxesimplificadaé:
mongoexport -d <banco-de-dados>
-c <collection>
--out <arquivo-de-saida>
Exemplodeexportarparaoarquivo seriados.json:
fb@cascao > mongoexport -d test -c seriados --out seriados.json
connected to: 127.0.0.1
exported 3 records
Backupquente
Obackupdetudocombanconoar(conhecidocomo backup quente)tam-
béméefetuadocomocomando mongodump,comessasintaxe:
service mongod start
mkdir <diretorio-de-backup>
cd <diretorio-de-backup>
mongodump
ExemploemLinux:
service mongod start
mkdir /bkp/dados/
cd /bkp/dados/
mongodump
Backupdeapenasumbancodedados
Informandooparâmetro db,podemosfazerobackupdeapenasum
bancodedados:
143

## Página 153

11.6. Restore CasadoCódigo
mkdir <diretorio-de-backup>
cd <diretorio-de-backup>
mongodump --db <nome-do-banco>
Exemplo:
mkdir /bkp/dados/
cd /bkp/dados/
mongodump --db test
Backupdeapenasumacollection
Informandooparâmetro dbe collection,podemosfazerobackup
deapenasumacollection:
mkdir <diretorio-de-backup>
cd <diretorio-de-backup>
mongodump --db <nome-do-banco>
--collection <nome-da-collection>
Exemplo:
mkdir /bkp/dados/
cd /bkp/dados/
mongodump --db test
--collection filmes
11.6 Restore
Para restaurar os backups feitos com mongodump, utilizamos o
mongorestore, que deve ser sempre executado com o banco de da-
dosforadoar.
restorefull
O restore fulloucompletoéarestauraçãodetodososbancosdedadosdo
MongoDBeéfeitacomaseguintesintaxe:
<derruba-serviço-no-MongoDB>
cd <diretorio-de-backup>
mongorestore --dbpath <diretorio-de-dados-do-mongodb> dump
144

## Página 154

CasadoCódigo Capítulo11. MongoDBparaadministradores
ExemplonoLinux:
service mongod stop
cd /bkp/dados/
mongorestore --dbpath /var/lib/mongo dump
restoreparcial
Pararestaurarapenasumbancodedadosespecífico,asintaxeésemel-
hante:
<derruba-serviço-no-MongoDB>
cd <diretorio-de-backup>
mongorestore --dbpath <diretorio-de-dados-do-mongodb>
--db <nome-do-banco>
dump/<nome-do-banco>
ExemplonoLinuxde restoredobancodedados test:
service mongod stop
cd /bkp/dados/
mongorestore --dbpath /var/lib/mongo
--db test
dump/test
Seobancojáexistir,oMongoDBfaráum mergedoatualcomo dump
existente.
Pararestaurarremovendoobancoexistente,usamosoparâmetro drop:
<derruba-serviço-no-MongoDB>
cd <diretorio-de-backup>
mongorestore --drop
--dbpath <diretorio-de-dados-do-mongodb>
--db <nome-do-banco>
dump/<nome-do-banco>
Exemplo:
service mongod stop
cd /bkp/dados/
145

## Página 155

11.7. Exibiroperaçõesrodando CasadoCódigo
mongorestore --drop
--dbpath /var/lib/mongo
--db test
dump/test
11.7 Exibir operações rodando
OMongoDBoferecedoiscomandosbeminteressantesqueajudambastante
naadministraçãodobancodedados.
Ocomando db.currentOpexibeasoperaçõesemexecu çãonomo-
mento:
mongo> db.currentOp();
{"inprog :
[{
"opid : 123,
"op : "query
...
}]
}
Senecessário,épossívelderrubarumprocessodessescomocomando
db.killOp:
mongo> db.killOp(123)
{ "info" : "attempting to kill op" }
11.8 Próximos passos
Certifique-sedequeaprendeu:
• aativarautenticação;
• acriarusuárioseseusacessosaosbancodedados;
• afazerbackupdobancodedadoscompletoeparcial;
• arestaurarobackupdobancodedadoscompletoeparcial;
146

## Página 156

CasadoCódigo Capítulo11. MongoDBparaadministradores
• aexibiroperaçõesrodando.
No próximo capítulo analisaremos a questão dereplica set e
sharding,quandousarecomousar.
147

## Página 158

Capítulo12
MongoDBemcluster
Seoseubancoficougrandedemaisparaumaúnicamáquinaounecessita
dealtadisponibilidade,chegouahoradeentenderumpoucomaissobreos
conceitosde replica set e sharding.
12.1 Alta disponibilidade
Terosseusdadosreplicadosemdiferenteslugares(chamados nós)eseum
algumnócair,outroassumirnolugar,issoéoquechamamosdealtadisponi-
bilidade;asuaaplicaçãonãodeixadefuncionar.
Essaarquiteturaéchamadade replica set(ouconjuntodeservidoresrepli-
cados),ondepodemosterentre2e12servidores(masomínimosugeridoé
3).
Nafigura 12.1,temosoexemplodeumaarquiteturade3nós:oprimeiro
éonóprimário(emqueosdadossãolidoseescritos),eosoutrosdoissãoos

## Página 159

12.2. Testandodoisreplicasets CasadoCódigo
nóssecundários(osdadossãoapenascopiadosdonóprimárioesãousados
apenasparaconsulta).
Fig.12.1:MongoDB replica setcomtrêsnós
Acadadoissegundos,osnósseconversameverificamseestãoativos.
Issoéchamadode heartbeat.
Seonóprimáriocair,umdosnóssecundárioséeleitoparaseronovonó
primário.Novosnóssecundáriospodemseradicionadosaqualquerinstante,
seminterrompero clusterinteiro.
Umnópodeestarnamesmamáquinaqueoutronó,desdequeemportas
distintas. Entretanto,emtermosdealtadisponibilidadeissonãoéinteres-
sante,jáqueumafalhadehardwarepoderiacomprometermaisdeumnóao
mesmotempo.
Para informar ao MongoDB que se está usandoreplicaset, é
necessário adicionar ao arquivo de configuração ( mongodb.conf) o
parâmetro replSetou replication.replSetName:informando o
nomedoclustercriado.
12.2 Testando dois replica sets
Parateste,vamosiniciardoisserviçosdoMongoDBnamesmamáquinaem
diferentesportasparasimularum replica setdeduasmáquinas.
Emumterminal,iniciamosoprimeironónaporta27017docluster rs0:
150

## Página 160

CasadoCódigo Capítulo12. MongoDBemcluster
mongod --port 27017
--dbpath /tmp/mongodb/rs0-0
--replSet rs0
Emoutroinicial,iniciamososegundonónaporta27018domesmoclus-
ter rs0:
mongod --port 27018
--dbpath /tmp/mongodb/rs0-1
--replSet rs0
Agoraprecisamosdefinirqueméonóprimárioequeméosecundário.
Paraisso, vamosnosconectaraonóprimárioeexecutarocomando
rs.initiateparaativarocluster:
fb@cascao ~ > mongo --port 27017
MongoDB shell version: 2.6.1
connecting to: 127.0.0.1:27017/test
> rs.initiate()
{
"info2" : "no configuration explicitly specified
-- making one",
"me" : "cascao:27017",
"info" : "Config now saved locally.
Should come online in about a minute.",
"ok" : 1
}
Podemos consultar quantos nós temos em nosso cluster no array
members:
> rs.conf()
{
"_id" : "rs0",
"version" : 1,
"members" : [
{
"_id" : 0,
"host" : "cascao:27017"
151

## Página 161

12.3. Particionamento CasadoCódigo
}
]
}
Vamos adicionar o nó secundário da porta 27018 com o comando
rs.add:
rs0:PRIMARY> rs.add("cascao:27018")
{ "ok" : 1 }
Comisso,verificandonovamenteaconfiguração,percebemosqueoarray
de memberscontémumnovoelemento:
rs0:PRIMARY> rs.conf()
{
"_id" : "rs0",
"version" : 2,
"members" : [
{
"_id" : 0,
"host" : "cascao:27017"
},
{
"_id" : 1,
"host" : "cascao:27018"
}
]
}
Paraadicionarnovosnós,utilizeomesmocomando rs.add.
12.3 Particionamento
Suacollectionchegouàcasadosbilhõesderegistrosefisicamentenãocabe
maisemumúnicoservidor.
Nessecaso,chegouahoradequebrarasuacollectionporumachave,o
queéchamadode shardingouparticionamento.
152

## Página 162

CasadoCódigo Capítulo12. MongoDBemcluster
Umexemploéseexiste30Tbdedadosquenãocabememumservidor,
entãoépossívelparticionaracollectionedividiremtrêsmáquinasde10Tb
cada.
Paratal,éprecisoescolheramelhormaneiradedistribuiruniformemente
ainformaçãoentreosservidores. Essecritérioéfeitonacriaç ãodoparti-
cionamentodefinindoumachave(umfiltro)paradividirasinformações.
Afigura 12.2mostraumexemplocomumacollectionúnicadetrêster-
abytesquepodeserparticionadaemtrêspartiçõesdeumterabytecadaes-
palhadaemtrêsmáquinasdistintas.
Fig.12.2:Sharding
Arquiteturadesharding
OMongoDBcomparticionamentoexigetrêsdiferentesserviços:
153

## Página 163

12.3. Particionamento CasadoCódigo
•Shards:sãoasinstânciasdoMongoDBquecontêmosseusdadospar-
ticionados.Cada shardpodeserum replica set;
•Config Servers:sãoosservidoresquetêmmapeadososmetadados
detodaaarquitetura;
•Query Routing Instances:essainstânciacomquesuaaplicaç ão
irá secomunicar; é ela quedireciona as leiturase escritas para os
shards(nenhumaaplicaçãoacessaos shardsdiretamente).
Essaarquiteturaéilustradanafigura 12.3.Reparequeaaplicaçãoacessa
apenasasinstânciasde query router,eelafazadistribuiç ãodosacessos
aosdadosnos shards.Noteque,emvezdoexecutável mongod,éutilizado
parashardingo mongos.
Fig.12.3:MongoDBcomparticionamento(sharding)
154

## Página 164

CasadoCódigo Capítulo12. MongoDBemcluster
Emambientedeprodução,érecomendado:
•Shards instances:nomínimodoisserviços,ecada shardrepli-
cadocom replica set;
•Config instances:nomínimotrêsserviços;
•Query routing instances:nomínimodoisserviços.
Shardingdeexemplo
Vamosfazerumaconfiguraçãomínimadeshardingparaexemplificaro
funcionamento:
•Config instances:umserviço
•Query routing instances:umserviço
•Shards instances:doisserviços
Tudorodaránamesmamáquina,comosserviçosemportasdistintas.
Exemplodeconfiginstance
Oprimeiropassoécriarum config server naporta27020,comessas
configurações:
root@cascao /etc > cat config_db.conf
fork=true
dbpath=/var/lib/mongodb/dbs/config_db
logpath=/var/log/mongodb/config_db.log
logappend=true
port=27020
Emseguida,criamosodiretóriodobancodedadosesubimososerviço
apontandoparaoarquivodeconfiguração config_db.conf:
root@cascao > mkdir /var/lib/mongodb/dbs/config_db
root@cascao > mongod --configsvr --config /etc/config_db.conf
155

## Página 169

12.4. Próximospassos CasadoCódigo
• aparticionardadoscomsharding;
• aadicionarumacollectionaumsharding.
160

## Página 170

Capítulo13
Continueseusestudos
Agoraemdiante,paraaprimorarosconhecimentosnoMongoDB:
• Façaosexcelentestreinamentosgratuitosna MongoDB University
https://university.mongodb.com/
• ParticipedogrupointernacionaldeusuáriosdoMongoDB https://
groups.google.com/forum/#!forum/mongodb-user
• ParticipedogrupobrasileirodeusuáriosdoMongoDBhttps://groups.
google.com/forum/#!forum/br-mongodb
Eacompanheosprincipaisblogs:
• blogoficialhttp://blog.mongodb.org/

## Página 171

CasadoCódigo
• blogquecentralizanotíciasrelacionadasaoMongoDB http://planet.
mongodb.org/
• blogsobreMongoDBeoutrasbasesNoSQLhttps://blog.compose.io
162

## Página 172

Capítulo14
ApêndiceA.Instalando
MongoDB
OMongoDBéumexcelentebancodedadosNoSQL,masestáemsuafase
NERD,emquetudosefazcomlinhadecomandoe,apesardaexcelenteper-
formanceeestabilidade,porenquantonãoapresentapreocupaç ãocomain-
terfacegráfica.
Asuainstalaçãoébemsimples,mas,aocontráriodamaioriadosfabri-
cantes,naplataformaWindowsneminstalacomoserviço,seráprecisofazer
esteajustemanualmente.
AinstalaçãoemLinuxatualmenteéamaiscompleta,poisinstalaecon-
figuracomoserviço.
A documentação completa está no site:http://docs.mongodb.org/
manual/installation/.Vamosresumiralgunspassosemseguida.

## Página 174

CasadoCódigo Capítulo14. ApêndiceA.InstalandoMongoDB
Release [49,6 kB]
...
Efinalmenteinstalamos:
root@perola:~# apt-get install mongodb-org
Lendo listas de pacotes... Pronto
Construindo árvore de dependências
Lendo informação de estado... Pronto
Os pacotes extra a seguir serão instalados:
mongodb-org-mongos mongodb-org-server mongodb-org-shell
mongodb-org-tools
InstalaçãoemWindows
VamosbaixaraversãoparaWindowspelosite http://www.mongodb.org/
downloadseexecutar:
Fig.14.1:InstalaçãodeMongoDBparaWindows32bits
Iniciamosainstalaçãoclicandoem Next:
165

## Página 175

CasadoCódigo
Fig.14.2:Iníciodainstalação
Aceitamosostermosdeusotambém:
166

## Página 176

CasadoCódigo Capítulo14. ApêndiceA.InstalandoMongoDB
Fig.14.3:Termosdeuso
Selecionamosaop çãodeinstalaçãocompleta:
167

## Página 177

CasadoCódigo
Fig.14.4:Escolhendootipodeinstalaç ão
Finalmente,clicamosem Installparainstalar:
168

## Página 178

CasadoCódigo Capítulo14. ApêndiceA.InstalandoMongoDB
Fig.14.5:Copiandoosarquivoscomoinstalador
Ainstalaçãoseráconcluídaempoucosinstantes:
169

## Página 179

CasadoCódigo
Fig.14.6:Finalizandoainstalação
VamosadicionarosexecutáveisdoMongoDBao PATHdoWindows.
Paraisso,acessamosopaineldecontroleemodificamosalgumasvariáveis
deambiente:
170

## Página 180

CasadoCódigo Capítulo14. ApêndiceA.InstalandoMongoDB
Fig.14.7:Alterandovariáveisdeambiente
Clicandonaop ção New,criamosumanovavariável MONGODB_HOMEque
contémovalorde C:\Program Files\MongoDB 2.6 Standard\.
171

## Página 181

CasadoCódigo
Fig.14.8:Alterandovariáveisdeambiente
Emseguida,editamosavariáveldeambiente PATHeadicionamosaofinal
%MONGODB_HOME\BIN:
172

## Página 182

CasadoCódigo Capítulo14. ApêndiceA.InstalandoMongoDB
Fig.14.9:Alterandovariáveisdeambiente
Chamamosopromptdecomandoparainstalaroserviço. Iniciamos
criandoosdiretóriosdosdadoscom:
mkdir c:\data\db
mkdir c:\data\log
173

## Página 183

CasadoCódigo
Criamosoarquivodeconfiguração:
echo logpath=c:\data\log\mongod.log>
"C:\Program Files\MongoDB 2.6
Standard\mongod.cfg"
echo dbpath=c:\data\db>> "C:\Program Files\MongoDB 2.6
Standard\mongod.cfg"
Efinalmentecriamososerviço:
sc.exe create MongoDB binPath= "\"C:\Program Files\MongoDB 2.6
Standard\bin\mongod.exe\" --service
--config=\"C:\Program Files\MongoDB
2.6 Standard\mongod.cfg\"" DisplayName= "MongoDB 2.6 Standard"
start= "auto"
Oresultadoserásemelhanteaesse:
Fig.14.10:InstalandooMongoDBcomoserviçodoWindows
InstalaçãoemMacOSX
AinstalaçãoéfeitaatravésdoHomebrew:
174

## Página 184

CasadoCódigo Capítulo14. ApêndiceA.InstalandoMongoDB
Fig.14.11:InstalandooMongoDBpeloHomebrewnoMacOSX
Criamosum aliasparaoMongoDBinstalarcomoumserviço:
Fig.14.12:InstalandooMongoDBcomoserviço
Emseguida,usamos mongodb_start/ mongodb_stop:
Fig.14.13:ManipulandoserviçosdoMongoDBnoMacOSX
175

## Página 185

CasadoCódigo
Testandoainstalação
ComoMongoDBnoar,conectamosedigitamosocomandoparainfor-
maraversãoinstalada:
db.version()
OresultadoserásemelhanteaesseemLinuxeMacOSX:
fb@cascao ~ > mongo
MongoDB shell version: 2.6.1
connecting to: test
> db.version()
2.6.1
> exit
bye
fb@cascao ~ >
EaesseemWindows:
Fig.14.14:ExibindoaversãodoMongoDBnoWindows7
176

## Página 186

Capítulo15
ApêndiceB.Robomongo
ExistemdiversosclientesdesenvolvidosparaMongoDB,dentreosquaisse
sobressaioRoboMongo,umaexcelenteferramentaopensourcequepossui
amesmaengineemJavaScriptqueocliente shelloficial. Issosignificaque
todososcomandosexistentesfuncionamtambémnoRobomongo,mascom
umainterfacemuitomaisamigável.
Instalação
ORobomongopodeserbaixadoemseusite http://robomongo.org/para
Windows,LinuxeMacOSX.
AinstalaçãodoRobomongoébemsimplesenãoprecisadenenhuma
opçãoespecial,poressemotivosóilustraremosainstalaç ãoemWindows.

## Página 187

CasadoCódigo
Fig.15.1:Iníciodainstalação
Sãoexibidosostermosdeusodalicen çaopensource(GPL)paraconcor-
dar:
178

## Página 188

CasadoCódigo Capítulo15. ApêndiceB.Robomongo
Fig.15.2:TermosdeusodoRobomongo
Emseguida,éexibidoodiretóriodeinstalaç ão:
179

## Página 189

CasadoCódigo
Fig.15.3:Escolhendoodiretóriodeinstalação
Depoiséinformadoaop çãodepastademenudeinicializa çãoqueserá
criado:
180

## Página 190

CasadoCódigo Capítulo15. ApêndiceB.Robomongo
Fig.15.4:Opçãodepastademenudeinicializaç ão
Finalizadaainstalação,édadaaop çãodeiniciaroRobomongo:
181

## Página 191

CasadoCódigo
Fig.15.5:Finaldainstalação
Configuração
AoiniciaroRobomongo,éprecisoconfigurarpelomenosumaconexão
aoservidor.Issoéfeitoclicandonaop ção Create:
182

## Página 192

CasadoCódigo Capítulo15. ApêndiceB.Robomongo
Fig.15.6:Configurandoumaconexãoaoservidor
Emseguida,informamosonomedaconexão.ComoinstalamosoMon-
goDBnamesmamáquina,chamamosaconexãode localhost,quepor
padrãoescutarequisiçõesnaporta27017:
183

## Página 193

CasadoCódigo
Fig.15.7:Cadastrandoumaconexãolocal
Depoisdecriadaaconexão,podemosconectarclicandoem Connect:
Fig.15.8:ConectandolocalmenteaoMongoDB
184

## Página 194

CasadoCódigo Capítulo15. ApêndiceB.Robomongo
TemosalgumasopçõesnativasdoRobomongo,comoporexemploexibir
informaçõesdoservidornaop ção Server Status:
Fig.15.9:Exibindoinformaçõesdoservidor
Oresultadodasituaçãodoservidoréexibidodemaneiraamigável:
185

## Página 195

CasadoCódigo
Fig.15.10:Resultadodasituaçãodoservidor
Podemostambémvisualizaroslogsdoservidorcom Control + L ,
queaparecemnajanelainferior:
186

## Página 196

CasadoCódigo Capítulo15. ApêndiceB.Robomongo
Fig.15.11:Visualizandooslogsdoservidor
Alémdisso,conseguimosnavegarpelascollectionsexistentes,evisual-
izamososeuconteúdocomaop ção View Documents:
187

## Página 197

CasadoCódigo
Fig.15.12:Ativandoaop çãodeexibiroconteúdodeumacollection
Temostambémocomandoexecutadoexibidoemumanovaaba:
188

## Página 198

CasadoCódigo Capítulo15. ApêndiceB.Robomongo
Fig.15.13:Conteúdodeumacollectionexibidoemumanovaaba
Econseguimosabrirumnovoterminalcomaop ção Open Shell:
189

## Página 199

CasadoCódigo
Usandooterminalparaexibirascollections:
190

## Página 200

CasadoCódigo Capítulo15. ApêndiceB.Robomongo
Fig.15.15:Usandooterminalparaexibirascollections
Umrecursomuitoboméoautocompletedoterminal,queautomatica-
menteexibeaousuárioasop çõesqueelepodeusar:
191

## Página 201

CasadoCódigo
Fig.15.16:ExemplodeautocompletenoterminaldoRobomongo
192

## Página 202

Capítulo16
ApêndiceC.Perguntase
respostas
Nãoéprecisolerolivrointeiroparaesclareceralgumasdúvidassimples.
Vamostentaraquienumerarasquestõesmaiscomunseesclarecê-lasde
umavezportodas!
OqueéNoSQL?
ONoSQLéumtermotécnicoparadenominarumbancodedadosque
nãoérelacional.Normalmente,eleédotipobancodedadosdedocumento,
orientadoaobjetos,chave-valoroudegrafos.OMongoDBocupaaprimeira
posiçãodebancodedadosNoSQLdeacordocomapesquisadosite http:
//db-engines.com/.

## Página 203

CasadoCódigo
DeondeveioonomeMongoDB?
Onomeveiodapalavra humongous,quesignificaenorme,gigantesco,
paradaraideiadegrandegerenciamentodedados.
QuemusaoMongoDB?
Alistacompletacommaisde50clientesestáemhttps://www.mongodb.
com/customers. Seguem alguns dos mais famosos no Brasil: IBM,
Foursquare,Bosch,Cisco,eBay,McAfee,Microsoft,MTVNetworks,Tele-
fonicae TheNewYorkTimes.
OMongoDBéumsubstitutoparaosbancosrelacionais?
Não,elenãosubstituiumbancorelacional,poisnãopossuitransaç ãoou
constraints,quequasetodosistemapossui,maselepodeserumcomplemento
deumabaserelacional,servindocomocache,porexemplo. Entretanto,se
suaaplicaçãofordesenhadaadequadamente,elapodeusarinteiramenteo
MongoDBenãousarnenhumabaserelacional.
OMongoDBpossuiconstraints?
Não,oMongoDBcriaumíndiceparacadacollection,masvalidaçõesnos
campossãoesperadasqueaconte çamnaaplicação.
OMongoDBpossuiíndices?
Sim, com MongoDB conseguimos criar índices simples e compostos
(maisdeumcampo),inclusiveparaarrays.
OMongoDBsuportatransaç ões?
Não.
OMongoDBsuportacluster?
Sim,osbancosNoSQLemgeralsuportamoambientede cluster,eoMon-
goDBnãoéexce ção.Eletrabalhademaneiraeficientenessaarquiteturauti-
lizando replica set.Paramaisdetalhesconsulteo 12.
194

## Página 204

CasadoCódigo Capítulo16. ApêndiceC.Perguntaserespostas
Qualolimitemáximodeumregistro/documentoemumacollec-
tiondoMongoDB?Equaissãoosoutroslimites?
Olimiteéde16Mbdetamanhomáximo,permitindoteraté100níveisde
documentosaninhados.Paraterumcomparativo,existemalgumasversões
nainternetdaBíbliaemformatotextoqueocupamaproximandamente4mb,
portanto,paraultrapassarolimiteatualdoMongoDB,umsimplesregistro/
documentoprecisatermaistextodoquequatrobíbliascompletasjuntas.
Osnomesdecampos,collectionsedatabasespodemteraté123bytes.
Umcollectionpodeteraté64índices,cadaumdelespodeconterentre1
até31campos.
Otamanhomáximodobancodedadospodevariarconformeotipode
file systemeosistemaoperacional,masagrossomodoé4terabytesparaWin-
dowse54terabytesparaLinux.
Consulte os limites restantes na documentação oficial http://docs.
mongodb.org/manual/reference/limits/.
Comolistartodososbancosdedadosexistentes?
Utilizeocomando show databases ou show dbs.
Comolistartodosascollectionsdeumbancodedados?
Utilizeocomando show collections.
Comolistaroscomandosexistentes?
Utilizeocomando helpe db.listCommands().
195