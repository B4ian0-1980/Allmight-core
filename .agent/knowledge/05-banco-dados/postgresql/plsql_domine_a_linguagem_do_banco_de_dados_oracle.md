---json
{
  "id": "plsql_domine_a_linguagem_do_banco_de_dados_oracle",
  "title": "PLSQL Domine a linguagem do banco de dados Oracle",
  "categoria": "05-banco-dados",
  "subcategoria": "postgresql",
  "resumo": "**Arquivo Original:** `PLSQL Domine a linguagem do banco de dados Oracle.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "banco",
    "dados",
    "domine",
    "linguagem",
    "oracle",
    "plsql",
    "postgresql"
  ],
  "perguntas_tipo": [
    "Como utilizar PLSQL Domine a linguagem do banco de dados Oracle?",
    "Quais as boas praticas de postgresql?"
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
  "dono": "stack-postgresql",
  "prioridade": 2
}
---

# PLSQL Domine a linguagem do banco de dados Oracle

> **Arquivo Original:** `PLSQL Domine a linguagem do banco de dados Oracle.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

CasadoCódigo
Prefácio
Sempregosteidelivrosque“conversam”comoleitor,principalmenteostéc-
nicos.Comosefosseumatrocadeideiasentreoautoreapessoaqueoestá
lendo.Procureiescreverdestaforma,poiscreioquecomissoaleiturasetorna
maisclaraeamigável,umbatepapoentreamigos,conversandosobrequal-
querassunto.Ainten çãofoicolocaraquitudooquevocêvaiprecisarsaber
sobrealinguagemPL/SQL.Olivroabordaconceitosquesãoutilizadosno
diaadiadodesenvolvimentoeanálisedesistemasparabancodedadosOra-
cle.Demonstreidiversosexemplos,quetambémvãoajudá-locomofontede
referênciaparaconsultadecomandosecomoutilizá-los.Tenhaumaotima
leitura!
Público alvo
EstelivrosedestinaainicianteseexperientesnalinguagemPL/SQL.Para
osiniciantes,sãoabordadosconceitossobreaestruturadalinguagemPL/SQL
esuascaracterísticas. Eleensinacomocriarprogramas,dosmaissimples
atéosmaiscomplexos,paraatenderàsmaisdiversasnecessidades.Vocêvai
aprendercomoestalinguagempodetrazerumaltograudeprodutividadee
performanceparaassuasaplicações.Paraosjáexperientes,eleajudarácomo
fontedereferênciaepararelembrarconceitosetécnicasdalinguagem.
Como o livro está dividido?
Primeiramente,sãoabordadosconceitosbásicosdalinguagem,comosua
definição,comoéestruturadaeseusprincipaiscomponentes.Logoapós,en-
tramosafundonasuaestrutura,conhecendocadacomandoecadacompo-
i

## Página 3

CasadoCódigo
nentequeelautiliza,explorandosuasfuncionalidadesepropriedades.Oli-
vrotambémmostracomoincorporaralinguagemSQLdentrodosprogramas
escritosemPL/SQL,paraarecuperaç ãoemanipulaç ãodedados. Tiposde
dados,estruturascondicionaisederepetiç ão,armazenamentodeprogramas
atravésdeprocedures(procedimentos)e functions(funções),emodularizaç ão
atravésdepackages(pacotes)sãoalgunsdositensmostrados.
Todaessaabordagemérealizadanoâmbitoprático,ondesãodetalhadas
suasestruturas,seuscomandosecaracterísticas,sempreatravésdeexemplos
práticosedefácilcompreensão.
Os scripts de base (tabelas e dados) e fontes para a execução
dos exemplos do livro estão disponíveis no enderecohttps://github.com/
eduardogoncalvesbr/livroplsql-casadocodigo.
Confira outras obras do autor
SQL: Uma abordagem para bancos de dados Oracle http://www.
casadocodigo.com.br/products/livro-sql-oracle
Contatos
Para falar com o autor, envie e-mail para eduardogoncal-
ves.br@gmail.com Página no facebook: https://www.facebook.com/
eduardogoncalvesescritor
ii

## Página 4

CasadoCódigo
Sobre o autor
FormadoemTecnologiadaInformaç ão,possuimaisde10anosdeexperiên-
ciaemanáliseedesenvolvimentodesistemavoltadosatecnologiasOracle,
trabalhandoporgrandesempresascomoLojasRenner,MundialS.A,Tigre
S.A,Pernambucanas,TractebelEnergia,PortobelloCeramica,Bematech,en-
treoutros.EduardoGon çalvezéinstrutordecursosoficiaisdaOracle–nas
linguagensSQLePL/SQL.Tambématuanodesenvolvimentodeaplicações
mobileparaaplataformaiOS.Atualmente,atuacomoCoordenadordeOpe-
raçõesnaSuperoTecnologia.
iii

## Página 6

CasadoCódigo
Agradecimentos
Dedicoestelivroatodasosmeusamigosecolegasdaáreadetecnologia,bem
comomeusprofessoresementores,quetiveoprazerdeconhecer,ecomos
quaisaprendieatémesmotrabalhei.Duranteestaminhatrajetóriaaprendi
muitascoisascomestaspessoasextraordinárias. Trocamosexperiênciase
aprendemosmuito,unscomosoutros,programandoequebrandoacabe ça
paraescreveralinhadecódigoqueajudasseasolucionarumproblema(re-
gadoamuitocafé,namaioriadasvezes...risos),ouatémesmo,apenaspela
paixãodeprogramar.Saibamquecadaumdevocêscontribuiuimensamente
paraestetrabalho!Semvocêsistonãoseriapossível!Ficamaquimeussince-
rosagradecimentos!
v

## Página 8

CasadoCódigo Sumário
Sumário
1 PL/SQL 1
1.1 OqueéPL/SQL? . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 PorqueaprenderPL/SQL? . . . . . . . . . . . . . . . . . . . . 2
1.3 SQL,SQL*Plus,PL/SQL:Qualédiferen ça? . . . . . . . . . . 3
2 Programaç ão em bloco 7
3 Primeiros passos 13
3.1 ComoiniciarnoPL/SQL . . . . . . . . . . . . . . . . . . . . . 13
4 Pacote dbms_output 19
4.1 Exce çõesparaopacotedbms_output . . . . . . . . . . . . . . 26
5 V ariáveis bind e de substituição 27
5.1 Variáveisbind . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
5.2 Variáveisdesubstituição . . . . . . . . . . . . . . . . . . . . . 31
5.3 Utilizandovariáveisemarquivos . . . . . . . . . . . . . . . . 35
6 Aspectos iniciais da programaç ão PL/SQL 43
6.1 Caractereseoperadores . . . . . . . . . . . . . . . . . . . . . . 44
6.2 Identificadores . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
6.3 Transações . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.4 TransaçõesemPL/SQL . . . . . . . . . . . . . . . . . . . . . . 51
6.5 Trabalhandocomvariáveiseconstantes . . . . . . . . . . . . 52
6.6 TiposdedadosemPL/SQL . . . . . . . . . . . . . . . . . . . . 53
vii

## Página 9

Sumário CasadoCódigo
7 Exce ções 59
7.1 Exce çõespredefinidas . . . . . . . . . . . . . . . . . . . . . . . 60
7.2 Exce çõesdefinidaspelousuário . . . . . . . . . . . . . . . . . 79
8 Estruturas de condi ção: if 85
8.1 Estruturasdocomandoif-endif . . . . . . . . . . . . . . . . . 86
8.2 Estruturasdocomandoif-else-endif . . . . . . . . . . . . . . 87
8.3 Estruturasdocomandoif-elsif(-else)-endif . . . . . . . . . . 89
8.4 Formatandoasdeclaraçõesif . . . . . . . . . . . . . . . . . . . 93
8.5 Evitandoerroscomunsnousodeif . . . . . . . . . . . . . . . 94
9 Comandos de repeti ção 95
9.1 forloop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
9.2 whileloop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
9.3 loop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
9.4 Qualloopdeve-seusar? . . . . . . . . . . . . . . . . . . . . . . 105
10 Cursores 107
10.1 Cursoresexplícitos. . . . . . . . . . . . . . . . . . . . . . . . . 108
10.3 Cursorforloopcomdefiniç ãointerna . . . . . . . . . . . . . 118
10.4 Cursoresimplícitos . . . . . . . . . . . . . . . . . . . . . . . . 119
10.5 Atributosdecursorexplícitoeimplícito . . . . . . . . . . . . 121
10.6 Cursoresencadeados . . . . . . . . . . . . . . . . . . . . . . . 128
10.7 Cursorcomforupdate . . . . . . . . . . . . . . . . . . . . . . 130
11 Funç ões de caracteres e operadores aritméticos 143
11.1 Funçõesdecaracteres . . . . . . . . . . . . . . . . . . . . . . . 144
11.2 Funçõesdecálculos . . . . . . . . . . . . . . . . . . . . . . . . 149
11.3 Operadoresaritméticos. . . . . . . . . . . . . . . . . . . . . . 154
12 Funç ões de agregaç ão (grupo) 159
13 Funç ões de data 177
viii

## Página 10

CasadoCódigo Sumário
14 Funç ões de conversão 183
14.1 to_date . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
14.2 to_number . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
14.3 to_char . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
15 Funç ões condicionais 211
15.1 decodevs.case . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
16 Programas armazenados 225
16.1 proceduresefunctions . . . . . . . . . . . . . . . . . . . . . . 226
16.2 Usodocomandoreplace . . . . . . . . . . . . . . . . . . . . . 236
16.3 Recompilandoprogramasarmazenados . . . . . . . . . . . . 238
16.4 Recuperandoinformações . . . . . . . . . . . . . . . . . . . . 238
16.5 Recuperandocódigos . . . . . . . . . . . . . . . . . . . . . . . 239
16.6 Visualizandoerrosdecompilação . . . . . . . . . . . . . . . . 240
16.7 Passandoparâmetros . . . . . . . . . . . . . . . . . . . . . . . 243
16.8 Dependênciadeobjetos. . . . . . . . . . . . . . . . . . . . . . 249
17 packages 265
17.1 Estruturadeumpackage . . . . . . . . . . . . . . . . . . . . . 266
17.2 Acessoapackages . . . . . . . . . . . . . . . . . . . . . . . . . 270
17.3 Recompilandopackages. . . . . . . . . . . . . . . . . . . . . . 278
17.4 Recuperandoinformações . . . . . . . . . . . . . . . . . . . . 278
17.5 Recuperandocódigos . . . . . . . . . . . . . . . . . . . . . . . 279
17.6 Visualizandoerrosdecompilação . . . . . . . . . . . . . . . . 280
18 Transaç ões autônomas 283
19 Triggers 293
19.1 Triggerdebancodedados . . . . . . . . . . . . . . . . . . . . 294
19.2 Triggerdetabela . . . . . . . . . . . . . . . . . . . . . . . . . . 294
19.3 Triggerdelinha . . . . . . . . . . . . . . . . . . . . . . . . . . 301
19.4 Mutantetable. . . . . . . . . . . . . . . . . . . . . . . . . . . . 316
19.5 Triggerdesistema . . . . . . . . . . . . . . . . . . . . . . . . . 324
19.6 Triggerdeview . . . . . . . . . . . . . . . . . . . . . . . . . . . 330
ix

## Página 11

Sumário CasadoCódigo
20 PL/SQL Tables (estruturas homogêneas) 349
21 PL/SQL Records (estruturas heterogêneas) 359
22 Pacote utl_file 365
23 SQL dinâmico 385
23.1 Refcursor. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 397
24 Apêndice: SQL – Primeiros passos 405
24.1 ComoiniciarnoSQL . . . . . . . . . . . . . . . . . . . . . . . 405
25 Referências bibliográficas 413
26 Anexos 415
x

## Página 12

Capítulo1
PL/SQL
1.1 O que é PL/SQL?
AsiglaPL/SQLsignifica Procedural Language/ Structured Query Language,
ouseja,trata-sedeumalinguagemproceduraltendocomobaseaSQL(Lin-
guagemdeConsultaEstruturada).APL/SQLédirecionadaparaobancode
dadosOracleeéescritaatravésdeblocosdecódigoquesãoexecutadosdi-
retamentenobancodedados.Elapermiteodesenvolvimentodeprogramas
complexos,nosquaisgrandesvolumesdeinformaç ãosãoprocessados.
Comoqualqueroutralinguagemdeprogramaç ão, aPL/SQLéescrita
atravésdecódigos,sendoqueosprincípiosdelógicadeprogramaeprogra-
maçãoestruturadapodemserimplementados.
OsblocosPL/SQLpodemserescritoseguardadosnoprópriobancode
dados,atravésdefun ções( functions),procedimentos( procedures),

## Página 13

1.2. PorqueaprenderPL/SQL? CasadoCódigo
gatilhos( triggers)oupacotes( packages)paraseremexecutadoserea-
proveitadosquandonecessário.
Os códigos podem ser feitos utilizando-se uma interface, como o
SQL*Plus,queétotalmenteintegradaaobancodedados.Outrasferramen-
tascomoOracleForms,OracleReportseWorkflowBuildertambémpos-
suemmotoresPL/SQLquepermitemvalidarecompilaroscódigosescritos
emPL/SQL.
Atravésdetodosessesatributos,aPL/SQLsemantémcomoumalingua-
gemrobustaemuitoutilizadapelosdesenvolvedoreseanalistasdomundo
todo.Muitoprovavelmente,issosedáaofatodesuacrescentehistória,que
vemdesdeasprimeirasversõesdobancodedadosesuaevoluç ãopermanente
desdeentão.
Nomais,aPL/SQLdásuporteaosmaisvariadosrecursosdeprograma-
çãodesistemascomoautilizaç ãodevariáveis,constantes,cursores,estruturas
derepetiçãoecondicional,ousodepacotes,fun ções,procedimentosarma-
zenados,tratamentodeerros,chamadasàAPI,gatilhos,vetores,registros,
execuçãodiretadecomandosSQLetc.Alémdomais,elacondicionaemsua
estruturaospadrõesANSIparalinguagemSQLesuporteàcodificaç ãoJava.
1.2 P or que aprender PL/SQL?
ÉimportanteconheceralinguagemPL/SQL,independentedautilizaç ãoou
nãodasferramentasdedesenvolvimento.Mesmoutilizandoapenasobanco
dedados,éfundamentalconhecê-latendoemvistaquemuitosprocessos
dentrodoservidordobancosãoescritosouexecutadosporblocosnestalin-
guagem.
Noquedizrespeitoaodesenvolvimento,aPL/SQLproporcionarapidez,
eficiênciaesegurançaparaseusprogramas,poisseuscódigos,oumelhor,pro-
gramas,podemserarmazenadosnobancodedados. Assimsendo,napró-
ximavezqueprecisarexecutá-lonovamente,ésóchamá-lo,elejáestápronto.
Outropontointeressanteéqueosprogramasnãoprecisamestarnocliente,
jáqueaPL/SQLutilizaoservidordobancodedadosparaaexecuç ãoear-
mazenamentosdosseusprocessos.
OutravantagemdeseaprenderPL/SQLéquenobancodedadosOracle,
2

## Página 14

CasadoCódigo Capítulo1. PL/SQL
emborasejaimplementadoemdiversasplataformasdehardwareesoftware,a
PL/SQLéigualparatodaselas.Comisto,aportabilidadesemantémpresente.
1.3 SQL, SQL*P lus, PL/SQL: Qual é diferença?
Étanto“SQL”nostítulosdosprodutosOraclequeacabamosnosconfun-
dindo.Vamosentenderoqueécadaumadestassiglas.
•SQL:asiglaSQLsignifica Structured Query Language.Éumalingua-
gemestruturadadeacessoaosbancosdedados,declarativa,queusa
comandoscomo SELECT, INSERT, UPDATEe DELETE.Elasempre
éexecutadanoservidoratravésdeumainterfaceconectadaaobanco
dedados.ApesardenãoserpropriedadedaOracle,elaaincorporaem
suaestruturabaseeemsuaslinguagens.
•PL/SQL:éumalinguagemdeprocedimentos,propriedadedaOracle.
Caracteriza-seporumalinguagemnãodeclarativa,ouseja,nãobastam
apenascomandosSQL.Énecessárioousodecodificaç ãoemblocos,
chamadosblocosPL/SQL.Oscódigospodemserexecutadostantono
cliente(OracleForms,Reportsetc.) quantodiretamentenoservidor
dobancodedados.
•SQL*Plus:pode-sedizerqueeleéainterfaceentreousuárioeobanco
dedados.QuandoexecutamosumcomandoSQLouumblocoPL/SQL
peloSQL*Plus,eleosenviaaummotorPL/SQLqueexecutaoscoman-
dosPL/SQLeverificaaexistênciadecomandosSQL.Casoexistam,são
enviadosparaumexecutorSQL,queospassaparaobancodedados.
OSQL*Plusexibeoresultadonateladoseucomputador.
Paravisualizardeformamaisclaraosconceitosempregados,observea
imagemaseguirondeémostradoopapeldecadaumdentrodocontextode
suasaplicações.
3

## Página 15

1.3. SQL,SQL*Plus,PL/SQL:Qualédiferen ça? CasadoCódigo
Fig.1.1:Esquemacomasfun çõesdoSQL*Plus,PLSQLeSQL
Conformefoidito,atravésdoSQL*Plusnóspodemosentrarcomcoman-
dosSQLoublocosPL/SQL.Elessãoencaminhadosaoservidordobancode
dados,quepodedirecionarparaomotorPL/SQL,ouseja,oprocessadorque
vaivalidareexecutaroblocoPL/SQL,e/ouparaoexecutordedeclaraçõesde
comandosSQL.Atravésdestavisualizaç ãoépossívelentenderafinalidadee
importânciadecadaumdessesprodutos.
Umpontoimportanteaentenderécomosãoprocessadasasinstruções
SQLeblocosPL/SQLdentrodeaplicaçõesdesenvolvidascomOracleForms
ouReports. Paraentendimento,oOracleFormseReportssãoferramentas
RADparaodesenvolvimentodeformulárioserelatórios.Essasferramentas
seconectamnativamenteaobancodedadosOracle.Otermo“nativamente”
fazreferênciaacomoérealizadaaconexãocomobancodedados.Namai-
oriadasvezes,umaaplicaç ãoseconectaatravésdedriversdisponíveispela
ferramentaouporalgumgerenciadordeconexão,porexemplo,viaODBC
(encontradonoWindows).Poisbem,dentrodasferramentasOracleépossí-
velinserirtantocomandosSQL,quantoblocosPL/SQL.Essescomandosou
blocosserãoexecutadosparaalgumfimequandoissoaconteceasolicitaç ão
deexecuçãopodeserfeitadeformasdiferentes
4

## Página 16

CasadoCódigo Capítulo1. PL/SQL
Quandotemosdentrodaaplicaç ãocomandosSQLdistintos,elessãoen-
viadosumaumparaoservidordobandodedados.Dessaforma,aaplicaç ão
enviaumcomandoparaoservidor,esperaarespostaedepoisenviaoutro.
QuandotemosblocosPL/SQL,elessãoenviadosporcompletoaoservi-
dordobancodedados,nãoimportandooseuteor.Dentrodesteblocopode-
mostervárioscomandosSQLedemaisestruturasemPL/SQL.Dessemodo
economizamostempo,poisaaplicaç ãoenviadeumasóveztodasassolicita-
ções,eonúmeroderespostasesperadastambémreduzmuito.Reduzindoo
númeroderespostasetráfegodeinformaçõesentreaplicaç ãoeoservidordo
bancodedadosaumentamosachancedeganhodedesempenho,principal-
menteseestacomunicaç ãodependerdeumaredecliente xservidor.Vejaa
seguirailustraç ãodesteconceito.
Fig.1.2:Diferen çaentrecomandosSQLeBlocosPLSQL
5

## Página 18

Capítulo2
Programaçãoembloco
AlinguagemPL/SQLtrabalhaemblocosdecomando.Dentrodeblocopode-
mosteroutrosblocos,quenestecasosãochamadosdesub-blocos.Quando
queremosescreverumprogramaparaumdeterminadofim,utilizamosblo-
cosparaestruturaroscomandoseaformadecomoesteprogramavaisecom-
portar.
UmblocoPL/SQLéiniciadopelaexpressão begineéfinalizadapor
end.Estasduasexpressõesdeterminamaáreadonossobloco.Vejaumexem-
plodeblocoPL/SQL.
SQL> begin
2
3 end;
4
SQL>

## Página 19

CasadoCódigo
Comomencionadoanteriormente,podemosterblocosdentrodeoutros
blocos,osquaissãochamadosdesub-blocos.
SQL> begin
2
3 begin
4
5 end;
6
7 end;
8
SQL>
Alémdasexpressõesdedelimitaç ãodobloco,tambémpodemostero
declare,queéutilizadoparadelimitarumaáreaparadeclaraç ãodevariá-
veisqueserãoutilizadaspelaaplicaç ãoetambémaexpressão exception,
quedelimitaumaáreaparatratamentodeerros. Basicamente,umbloco
PL/SQLécompostopor:
• Áreadedeclaraçãodevariáveis( declare);
• Área de escopo para inserção de comandos e demais sub-blocos (
begin-end);
• Áreadetratamentodeerros.
AseguirumblocoPL/SQLcontemplandoestaspremissasbásicas.
SQL> declare
2
3 begin
4
5 begin
6
7 end;
8
9 exception
10 when others then
8

## Página 20

CasadoCódigo Capítulo2. Programaçãoembloco
11
12 end;
13
14
SQL>
Estetipodeblocoéchamadodeblocoanônimo,poisnãopossuemum
cabeçalhoetambémnãopodemsergravadosdiretamentenobancodedados.
Casovocêqueiraexecutá-losnovamente,énecessáriosalvaremumarquivo,
poisaofecharaferramentaelenãoéguardado.
Aprogramaçãoemblocotornaosprogramasmaisestruturadoselim-
pos.Principalmente,quandoutilizamosváriossub-blocosparaarealizaç ão
dedeterminadastarefasdistintas,comoasele çãodedados,umaatualizaç ão
ouexclusão.Fazendodestaforma,épossíveltratarcadablocobuscandouma
programaçãomaislógicaequepossafornecerinformaçõessobreoscoman-
doscontidosneleouatémesmoidentificarpossíveiserrosquepossamsurgir.
Vejaumexemplodeprograma.
SQL> declare
2 soma number;
3 begin
4 soma := 45+55;
5 dbms_output.put_line('Soma :'||soma);
6 exception
7 when others then
8 raise_application_error(-20001,'Erro ao somar valores!');
9 end;
10
SQL>
Nesteprograma,épossívelverificaraexistênciadeumaáreadedeclara-
çãodevariáveisondetemosavariável somadeclaradacomo number(vere-
mosestesconceitosmaisadiante);umaáreaondesãoinseridososcomandos
propriamenteditos, somarecebendoasomade45+45.Tambémtemosopa-
cote dbms_output,utilizadoquandoqueremosescreveralgonatela.Neste
caso,estamossolicitandoaescritadoresultadodasoma.Porúltimo,temos
9

## Página 21

CasadoCódigo
umaáreadedeclaraçãodeerrosondepodemostomaralgumaaç ãocasoum
erroaconte ça.Nesteexemplo,casosurjaqualquertipodeerro,chamamoso
procedimento raise_application_error,quefazcomqueaaplicaç ão
pareeimprimaumamensagemnatela.
Valelembrarqueasáreasdedeclaraçãoetratamentodeerrospodemexis-
tirtambémdentrodossub-blocos.
Ok. Nossoprogramajáestácriado. Agoravamosvercomoexecutá-
lo.Paraisso,podemosutilizaraferramentaSQL*Plus.Atravésdocomando
barra /podemosexecutarumblocoPL/SQL.
SQL> declare
2 soma number;
3 begin
4 soma := 45+55;
5 dbms_output.put_line('Soma :'||soma);
6 exception
7 when others then
8 raise_application_error(-20001,'Erro ao somar valores!');
9 end;
10 /
Soma :100
Procedimento PL /SQL concluído com sucesso.
SQL>
Ocomando /executaoblocoPL/SQL,mostrandoasaídageradapelo
dbms_output.BlocosPL/SQLnãonecessariamentepossuemumasaídaim-
pressanatela.Umamensagemindicandoqueoblocofoiexecutadocomsu-
cessotambémémostrada.Casoocorraalgumerrodesintaxenaconstruç ão
docomando,ouseja,algumcomandoescritoincorretamenteouumafun ção
utilizadaindevidamente,eletambémémostrado.Aseguirvamossimularum
errodesintaxeparavercomoaferramentasecomporta.
SQL> declare
2 soma number;
3 begin
4 soma 45+55;
10

## Página 22

CasadoCódigo Capítulo2. Programaçãoembloco
5 dbms_output.put_line('Soma :'||soma);
6 exception
7 when others then
8 raise_application_error(-20001,'Erro ao somar valores!');
9 end;
10 /
soma 45+55;
*
ERRO na linha 4:
ORA-06550: linha 4 , coluna 8:
PLS-00103: Encontrado o símbolo "45" quando um dos seguintes
símbolos era esperado:
:= . ( @ % ;
O símbolo ":=" foi substituído por "45" para continuar.
SQL>
Quandoocomandoéexecutado,aferramentaSQL*Plusfazváriasve-
rificações,inclusiveadesintaxedecomandos. Nalinha4estáfaltandoo
comandodeatribuiç ão :=queatribuiasomade45+55àvariável soma.
Comisso,umerroégeradoemostradonatela.Elegeralmentevemacompa-
nhadodealgumasinformaçõescomoalinhaeacolunaondeoerroestáocor-
rendo. Alémdisso,aferramentacostumaclarearomotivopeloqualoerro
estáocorrendo. Nestenossoexemplo,eledizquefoiencontradoosímbolo
“45”quandonaverdadeeraesperadoalgumoutro,porexemplo,osímbolo
deatribuição.
NotequeesteerrofoidetectadoantesmesmodeoOracleexecutaro
bloco. Agoravamosgerarumerro,masnãodesintaxe,massim,umerro
referenteadadosincorretos. Vamostentarsomarnúmeroscomcaracteres
alfanuméricos.
SQL> declare
2 soma number;
3 begin
4 soma := 45+'A';
5 dbms_output.put_line('Soma :'||soma);
6 exception
11

## Página 23

CasadoCódigo
7 when others then
8 raise_application_error(-20001,'Erro ao somar valores!');
9 end;
10 /
declare
*
ERRO na linha 1:
ORA-20001: Erro ao somar valores!
ORA-06512: em line 8
SQL>
Agoratemosoutroerro,entretanto,eleocorreuquandooblocofoiexe-
cutado.Nestecaso,oprogramatransferiuaaç ãoparaaáreadetratamentode
erros,gerandoumasaídaqueinformaacircunstânciaemqueerroaconteceu.
JávimosqueparaconstruirumprogramaemPL/SQLtemosquetraba-
lharemníveldebloco.Assimsendo,alinguagemPL/SQLpermiteadicionar,
dentrodasestruturasdestesblocos,todoequalquerrecursoparaqueeste
programapossaexecutaraçõesouprocedimentosservindo.
Dentrodosblocosépossíveldeclararvariáveiseconstantes,executarco-
mandosDML( select, delete, updatee insert),executarprocedi-
mentosarmazenados,fun ções,utilizarestruturasderepetiç ão,estruturasde
condição,alémdousodeoperadoresrelacionaisenuméricos.
12

## Página 24

Capítulo3
Primeirospassos
3.1 C omo iniciar no PL/SQL
Umadasdificuldadesqueencontramosquandoestamosaprendendouma
linguagemdeprogramaç ãoésaberporondecome çar.Nocasodoaprendi-
zadodaPL/SQL,nãoseriadiferente.Éumasituaç ãonormal.Atésentirmos
segurançaetermosconhecimentosuficiente,éinteressantetermosumroteiro
contendoosprimeirospassosparainiciarumprogramaPL/SQL.
Demonstroaquiumatécnicaqueutilizobastante,mesmotendoumbom
conhecimentonalinguagem.Naverdade,jáestáimplícitonaminhaformade
pensar,tantoqueacaboexecutando-amentalmente,enquantoescrevonesta
linguagem.Estemétodonãofoiretiradodenenhumlivro,foialgoque,en-
tendendoalógica,fuiseguindoedeucerto.Esperoqueajudevocês.
Vamostomarcomoexemplo,oenunciadoaseguir:

## Página 25

3.1. ComoiniciarnoPL/SQL CasadoCódigo
EscrevaumprogramaPL/SQLqueimprimanatelaosnomesosempre-
gadosdeumdeterminadogerenteedeumadeterminadalocalizaç ão.
Primeiro passo
Identifico no enunciado as fontes de dados, ou seja, as tabelas que farão
parte do programa, caso seja necessário.
Casotenhadúvidaemidentificarafontededados,vejaodocumento: 24.
Apósidentificarastabelas,montoos selectseexecutooscomandospara
trazerosdadosqueoprogramasolicita.Tudoissosemescreverumaúnica
linhaemPL/SQL.Somentemontoos selectseosexecutoparaverseos
dadosestãosendoretornados.Exemplo:
SQL> select ename, job, dname
2 from emp, dept
3 where emp.deptno = dept.deptno
4 and dept.loc = 'CHICAGO' -- será o parâmetro referente
a localização
5 and emp.mgr = '7698' -- será o parâmetro referente
ao gerente
6 /
ENAME JOB DNAME
---------- --------- --------------
ALLEN SALESMAN SALES
WARD SALESMAN SALES
MARTIN SALESMAN SALES
TURNER SALESMAN SALES
JAMES CLERK SALES
Tendomontadotodosos selectsdequeoprogramanecessita,vamos
paraopróximopasso.
Segundo passo
Inicio a montagem da estrutura do programa PL/SQL.
Nestecaso,analisoquetipodeobjetooprogramapede. Geralmente,o
enunciadotrazestainformaç ão,porexemplo,“façaumblocoPL/SQLanô-
nimo”,umaprocedure,uma function,uma packageetc. Nonosso
14

## Página 26

CasadoCódigo Capítulo3. Primeirospassos
exemplo,elenãomenciona.Comoelenãopedepararetornarinformações,
apenasimprimirnatela,nãocriareiuma function,porexemplo. Como
tambémnãomencionanadasobreprogramasarmazenados,tambémnãocri-
areiuma procedure,muitomenosuma package. Comotambémnão
mencionadisparosde triggers,nãoseráprecisocriarum.Voucriarum
blocoPL/SQLanônimo,mesmoporque,seforocaso,maisadianteeuposso
criarumcabe çalhoparatornaresteobjetoumprogramaarmazenado.Ésim-
ples.
ComeçodesenhandooblocoPL/SQL,seguindoaseguinteestrutura:
SQL> declare
2
3 begin
4
5
6 exception
7 when others then
8
9 end;
10 /
EstanãoéaestruturamínimadeumPL/SQL,poissabemosqueaárea
dedeclaraçãodevariáveis( declare)eaáreadetratamentodeerros(
exception)nãosãoobrigatórias,emboraestaúltimasejaimprescindível,
poisotratamentodeerroséfundamentalparaobomfuncionamentodosis-
tema. Contudo,nagrandemaioriadosprogramasteremosestaestrutura:
aáreadedeclaraçãodevariáveis,aáreaondeficarãoamaioriadoscoman-
dos,propriamenteditos,( begin- end),eaáreadetratamentodeerros(
exception).
Pronto.AestruturainicialdoseuprogramaPL/SQLestáprontaparaser
utilizada. Dentrodaáreadedeclaraçãodevariáveis,vocêvaicolocartodas
asquevocêvaiutilizardentrodoseuprograma. Aquitambémestarãode-
claradosostiposdedadosdefinidosporvocê,oscursores, exceptionsde
usuário,funçõeseprocedimentosetc.Casoseuprogramanãováutilizaresta
área,elapodeserexcluída.
Jádentrodocorpodoprograma, begin-end,éondevocêvaiescrevera
parteprincipaldele.Éneleondeselocalizameserãoexecutadososcomandos
15

## Página 27

3.1. ComoiniciarnoPL/SQL CasadoCódigo
daSQL,condições ifs,laçosderepetiç ão,aberturasdecursor,chamadasa
funçõeseoutrosprocedimentosarmazenados,eassimpordiante.
Aáreadetratamentodeerroséondevocêvaitratarospossíveisproble-
masquepoderãosurgirduranteaexecuç ãodoseuprograma.Quandoestiver
escrevendoumprogramaPL/SQLsempretrateospossíveiserros.Pelome-
nosa exception othersdevesertratada,paraqueaosinaldeumproblema,
oprogramanãoaborte. Tambémérecomendadaautilizaç ãodasfun ções
sqlerrme sqlcode,paraqueomotivodoerrosejamencionadonamen-
sagem.
UmprogramaPL/SQLsempreseguiráestaestrutura.Valeressaltartam-
bémquepodemosverestaestrutura declare-BEGIN-exception-END,deforma
encadeada,ouseja,umblocodentrodeoutro,comoformadeisolardetermi-
nadasinformaçõesourealizarverifica çõesdentrodoprograma.Contudo,a
estruturalógicaéamesma.
Segueoprogramacompleto:
SQL> declare
2 --
3 cursor c1( pdname varchar2
4 ,pmgr number) is
5 select ename, job, dname from emp, dept
6 where emp.deptno = dept.deptno
7 and dept.loc = pdname
8 and emp.mgr = pmgr;
9 --
10 r1 c1%rowtype;
11 begin
12 open c1( pmgr => 7698, pdname => 'CHICAGO');
13 loop
14 fetch c1 into r1;
15 --
16 if c1%found then
17 dbms_output.put_line('Nome: '||r1.ename||'
Cargo: '||r1.job);
18 else
19 --
20 exit;
16

## Página 28

CasadoCódigo Capítulo3. Primeirospassos
21 end if;
22 end loop;
23 --
24 close c1;
25 exception
26 when others then
27 dbms_output.put_line('Erro: '||sqlerrm);
28 end;
29 /
Nome: ALLEN Cargo: SALESMAN
Nome: WARD Cargo: SALESMAN
Nome: MARTIN Cargo: SALESMAN
Nome: TURNER Cargo: SALESMAN
Nome: JAMES Cargo: CLERK
Procedimento PL/SQL concluído com sucesso.
SQL>
Observ ação
Paragarantiraimpressãonatela,atravésdopacote dbms_output,
executeoseguintecomandonoSQL*Plus: set serveroutput on.
17

## Página 30

Capítulo4
Pacotedbms_output
Estepacotepossuifun çõeseprocedimentosquepermitemageraç ãodemen-
sagensapartirdeblocosanônimosdePL/SQL, procedures, packages
ou triggers. Eleutiliza-sedeumbufferemmemóriaparatransferência
destasmensagensnasessãoondeoprogramaestásendoexecutado.Quando
umprogramaenviamensagensatravésdopacote dbms_output,elassão
armazenadasnaáreadebufferesãoapresentadasapenasaotérminodopro-
grama.
SeestivermosutilizandoaferramentaSQL*Plus,pode-sehabilitareste
recursodigitandooseguintecomando: set serveroutput on.Fazendo
isso,todasasmensagenspassarãoaservisualizadasno promptdaferramenta.
Natabelaaseguir,serãovistososcomponentesmaisusadosdestepacote,
todosdotipo procedure.
•enable:habilitaachamadadasdemaisrotinasdopacote.

## Página 31

CasadoCódigo
•disable:desabilitaachamadadasdemaisrotinasdopacote.
•put:incluiumainformaç ãonaáreadebuffer.
•put_line:incluiumainformaç ãonaáreadebuffereadiciona,simul-
taneamente,umcaractereparaquebradelinha(linhanova).
•get_line:recuperaumalinhadobuffer.
•get_lines:recuperaváriaslinhasdobuffer.
Agora,seráabordadoemdetalhes,comscriptsexemplos,comosãoutili-
zadosestescomponentes.
enable
Estaprocedurehabilitachamadaspara put, put_line, new_line,
get_linee get_lines.Deveserespecificadoumtamanhoparaaáreado
bufferaserusada,definidoembytesepodendovariarde2.000até1.000.000.
Seissoforultrapassado,umamensagemdeerroserámostrada.
SQL> begin
2 dbms_output.enable(2000);
3 dbms_output.put_line ('TESTE');
4 end;
5 /
TESTE
Procedimento PL /SQL concluído com sucesso.
SQL>
disable
Esta procedure desabilita as chamadas para put, put_line,
new_line, get_linee get_lineselimpaobuffer.Émuitoútilnade-
puraçãodeprogramas,quandoforindesejadoosurgimentodemensagens
informativas.
20

## Página 32

CasadoCódigo Capítulo4. Pacotedbms_output
SQL> begin
2 dbms_output.disable;
3 dbms_output.put_line ('TESTE');
4 end;
5 /
Procedimento PL/SQL concluído com sucesso.
SQL>
Notequeamensagem“TESTE”nãoapareceunatela.
put
Estaprocedurerecebeumparâmetrocujovalorseráarmazenadonaárea
dobufferimediatamenteapósaúltimainformaç ão.Nãoéincluídoqualquer
caractereindicativodefimdelinha( enter). Ébomlembrarqueestesva-
loresdesaídasãotransformadosemstrings(caractere),portanto,sedesejar
queelestenhamumaformataç ãodiferenteseráprecisofazê-loatravésdoco-
mando to_charou to_number,porexemplo. Estaprocedureporsisó
nãoimprimenatela. Porisso,podemosutilizá-lajuntamentecomaproce-
dure new_line.Nesteexemplo,comoformadearmazenamentonobuffer,
utilizamosváriosprocedimentos put,umparacadaletra.Vejaoexemploa
seguir.
SQL> begin
2 dbms_output.put('T' );
3 dbms_output.put('E' );
4 dbms_output.put('S' );
5 dbms_output.put('T' );
6 dbms_output.put('E' );
7 dbms_output.new_line;
8 end;
9 /
TESTE
Procedimento PL/SQL concluído com sucesso.
SQL>
21

## Página 33

CasadoCódigo
put_line
Esteprocedimentoenviaoparâmetroinformadoparaaáreadebuffer,
acrescentando, automaticamente, umcaractereindicativodefimdelinha
apósotextoenviado. Comisso,oresultadoéimpressonatela,semane-
cessidadedaexecuç ãodequalqueroutroprocedimento. Notequeemcada
execuçãodo put_lineobufferélimpo.
SQL> begin
2 dbms_output.put_line('T');
3 dbms_output.put_line('E');
4 dbms_output.put_line('S');
5 dbms_output.put_line('T');
6 dbms_output.put_line('E');
7 end;
8 /
T
E
S
T
E
Procedimento PL /SQL concluído com sucesso.
SQL>
get_line
Esteprocedimentopermitelerdobufferumaúnicalinhadecadavez.
Elepossuidoisparâmetrosdesaídaondeoprimeiroretornaráoconteúdoda
linha( line)eosegundoretornaráseustatus( status).Ostatusindicase
alinhafoirecuperadaseguindooscritérios: 1indicaquefoirecuperadauma
linhadobuffer;
SQL> set serveroutput off
SQL> begin
2 dbms_output.enable(2000);
3 --
4 dbms_output.put('Como');
22

## Página 34

CasadoCódigo Capítulo4. Pacotedbms_output
5 dbms_output.new_line;
6 dbms_output.put('aprender');
7 dbms_output.new_line;
8 dbms_output.put('PLSQL?');
9 dbms_output.new_line;
10 end;
11 /
Procedimento PL/SQL concluído com sucesso.
SQL> set serveroutput on
SQL> declare
2 var1 varchar2(100) default null;
3 var2 varchar2(100) default null;
4 var3 varchar2(100) default null;
5 status number default null;
6 begin
7 --
8 dbms_output.get_line(var1,status);
9 dbms_output.get_line(var2,status);
10 dbms_output.get_line(var3,status);
11 --
12 dbms_output.put_line('Pergunta: '||var1||' '||var2||'
'||var3);
13 end;
14 /
Pergunta: Como aprender PLSQL?
Procedimento PL/SQL concluído com sucesso.
SQL>
Primeiramente,configuramosasessãoparanãomostrarassaídasdosco-
mandos pute put_line,atravésdocomando set serveroutput off.
Logoapós,noprimeirobloco,habilitamosumbufferde2000bytes(linha2).
Naslinhas4a9,temoscomandos putinserindocaracteresnobufferque
acabamosdehabilitar. Estamosutilizandotambémocomando new_line
paraqueoscaracteressejamguardadosemlinhasdiferentes.
23

## Página 35

CasadoCódigo
Nosegundobloco,temosdeclaradasasvariáveis var1, var2e var3
(linha2a4),queutilizaremosparaatribuirosvaloresdobuffer. Também
declaramosavariável status(linha5),queseráutilizadaparacompletar
achamadadaprocedure get_line.Naslinhas8a10,temosaschamadas
àprocedure get_line,querecuperamaslinhasdobuffereatribuemos
valoresàsvariáveisdeclaradas,anteriormente.Nalinha12,utilizamosoco-
mando put_lineparaimprimirnatelaoconteúdodasvariáveis,ouseja,os
mesmosrecuperadosdobuffer.Noteque,paraqueaimpressãoemtelafun-
cione,executamosocomando set serveroutput on,antesdaexecuç ão
dosegundobloco.
get_lines
Esteprocedimentopermitelerváriaslinhasdobufferutilizandoum ar-
raydecaracteres.Elepossuidoisparâmetros,umdesaída( lines)eoutro
deentradaesaída( numlines). Oprimeiroparâmetro, lines,setrata
deumatabeladotipo varchar2(255),podendoserdeclaradacomtipo
dbms_output.chararr. Jáoparâmetro numlinesservetantoparain-
formaraquantidadedelinhasquesedesejarecuperar,quantopararetornar
aquantidadedelinhasquerealmenteforamretornadasapósaexecuç ãoda
procedure.Vejaoexemploaseguir.
SQL> set serveroutput off
SQL> begin
2 dbms_output.enable(2000);
3 --
4 dbms_output.put('Como');
5 dbms_output.new_line;
6 dbms_output.put('aprender');
7 dbms_output.new_line;
8 dbms_output.put('PLSQL?');
9 dbms_output.new_line;
10 end;
11 /
Procedimento PL /SQL concluído com sucesso.
24

## Página 36

CasadoCódigo Capítulo4. Pacotedbms_output
SQL> set serveroutput on
SQL> declare
2 tab dbms_output.chararr;
3 qtlines number default 3;
4 res varchar2(100) default null;
5 begin
6 --
7 dbms_output.get_lines(tab,qtlines);
8 --
9 dbms_output.put_line(
'Retornou: '||qtlines||' registros.');
10 --
11 for i in 1..qtlines loop
12 res := res||' '||tab(i);
13 end loop;
14 --
15 dbms_output.put_line('Pergunta: '||res);
16 --
17 end;
18 /
Retornou: 3 registros.
Pergunta: Como aprender PLSQL?
Procedimento PL/SQL concluído com sucesso.
SQL>
Muitoparecidocomoexemploanterior,nesteexemplo,aalteraç ãofoi
substituirastrêsvariáveis var1, var2e var3,pelavariável tab,dotipo
array(linha2).Tambémdeclaramosasvariáveis qtlinese res(linhas
3e4),sendoqueaprimeiraéusadaparapassaraquantidadederegistrosa
seremretornados(econsequentementefazeroretorno)easegundaapenas
paramontarastringaserimpressanatela. Nalinha7,temosachamadaà
procedure get_lines,queretornaosdadosdobufferparadentrodenossa
variáveltab.Jánaslinhas11a13,utilizamosumaestrutura loop,paraler
osdadosdavariável arrayeconcatená-losnavariável res.Observeque
utilizamosavariável qtlines(contendoaquantidadedelinhasretorna-
das)paradeterminarovalorfinaldafaixapara loop.Nalinha15,temosa
25

## Página 37

4.1. Exceçõesparaopacotedbms_output CasadoCódigo
impressãodoconteúdode res.
4.1 E xceções para o pacote dbms_output
Existem duas exceções que podem ocorrer quando utilizamos o pacote
dbms_output.Segueminformaçõessobreelasecomotratá-las.
•ORU-10027(Overflowdebuffer). Solução: aumentarotamanhodo
buffersepossível.Casocontrário,encontrarummododegravarmenos
dados.
•ORU-10028(Overflowdecomprimentodelinha,limitede255caracte-
resporlinha).Soluç ão:verificarsetodasaschamadasfeitasacaracteres
porlinha pute put_linetêmmenosde255caracteresporlinha.
Nestecapítulofalamossobreo dbms_outputeseusrecursos.Duranteo
todoolivrodePL/SQLvamosutilizarestepacoteparagerarassaídasdasin-
formaçõesparanossosexemplos.Destaforma,émuitoimportanteconhecê-
loesaberutilizá-lo.
26

## Página 38

Capítulo5
Variáveisbindedesubstituição
AferramentaSQL*Pluspermiteousodevariáveiscomreferênciasdotipo
bindede substituição.
5.1 V ariáveis bind
AsvariáveisbindsãodeclaradasdentrodoSQL*Plusepodemserutilizadas
emtodoseuambiente,sendoemcomandosSQLoudentrodeprogramas
PL/SQL.Adeclaraçãodestetipodevariávelémuitosemelhanteàdeclaraç ão
utilizadanoPL/SQL,ondeanomeamosedefinimosumtipoparaela.Con-
tudo,nãoénecessáriaumaáreaespecíficaparadeclaraç ão,bastandoapenas
declará-lanopromptdoSQL*Plus.Vejaoexemplo:
SQL> variable mensagem varchar2(200)
SQL>

## Página 39

5.1. Variáveisbind CasadoCódigo
Estamos declarando uma variável chamada mensagem do tipo
varchar2com200posições. Depoisdedeclarada,ésóutilizá-lanospro-
gramas.
SQL> begin
2 :mensagem := 'Curso PLSQL';
3 end;
4 /
Procedimento PL /SQL concluído com sucesso.
SQL>
Notequeestamosutilizando-adentrodeumblocoPL/SQL,ondeatribuí-
mosumvalorparaela.Pararecuperarouatribuirumvalorparaumavariável
bind,emumprogramaPL/SQLoucomandoSQL,énecessárioreferenciá-la
atravésdautilizaçãodocaracteredoispontos( :),colocando-oantesdoseu
nome.Noentanto,quandoadefinimosouquandofor çamosaimpressãodo
seuvaloremtela,nãoháanecessidadedestecaractereespecial.
Paravisualizaroconteúdodeumavariável bindnateladoSQL*Plus,você
devehabilitaraimpressãoatravésdocomandoaseguir.
SQL> set autoprint on
SQL>
Apóshabilitaraimpressão,oconteúdodavariáveléimpressologoapós
aexecuçãodocomandoouprogramaondeelaestásendoutilizada. Vejaa
execuçãodoexemploanterior,agoracomo autoprintligado.
SQL> begin
2 :mensagem := 'Curso PLSQL';
3 end;
4 /
Procedimento PL /SQL concluído com sucesso.
MENSAGEM
28

## Página 40

CasadoCódigo Capítulo5. Variáveisbindedesubstituição
--------------------------------------------
Curso PLSQL
SQL>
Vejamaisumexemplo,agorautilizandoavariávelnocomando select.
SQL> select :mensagem from dual;
:MENSAGEM
----------------------------------------
Curso PLSQL
SQL>
Noteque,comoavariáveljáhaviarecebidoumvalor,quandoexecutamos
oblocoPL/SQL,estevaloraindapersisteemexecuçõesposteriores.
Paraalterarumvalordeumavariável binddiretamentepeloSQL*Plus,
podemosutilizarocomando exec.Vejaoexemploaseguir,ondedefinimos
umavariávelchamada gdepno,elogoapósatribuímosovalor10aela.
SQL> variable gdepno number
SQL>
SQL> exec :gdepno := 10
Procedimento PL/SQL concluído com sucesso.
gdepno
----------
10
SQL>
Agora, selecionamososempregadoscombasenocódigododeparta-
mento,vindodavariável bind gdepno.
SQL> select ename from emp where deptno = :gdepno;
29

## Página 41

5.1. Variáveisbind CasadoCódigo
ENAME
----------
CLARK
KING
MILLER
SQL>
Sequisermosvisualizaroconteúdodeumavariável bind,utilizamoso
comando print.Vejaoexemploaseguir:
SQL> print gdepno;
gdepno
----------
10
SQL>
Umavariável bindtemsuavidaútilcombasenasessãodoSQL*Plus.
Portanto,outrassessõesnãoasenxergam,somenteaqueascriou.Quandoo
SQL*Pluséfechado,automaticamente,elassãoexcluídasdamemória.
Autilizaçãodevariáveis bindtemalgumasrestrições,porexemploseu
usonacláusula from,quenãoépermitido,enasubstituiç ãodepalavras
reservadas.
Paravertodasasvariáveis bindsdeclaradasemumasessãodoSQL*Plus
utilizeocomando var.
SQL> var
variável wdname
Tipo de dados NUMBER
variável gnome
Tipo de dados varCHAR2(100)
SQL>
30

## Página 42

CasadoCódigo Capítulo5. Variáveisbindedesubstituição
5.2 V ariáveis de substituição
Outrotipodevariáveldeusuárioéavariáveldesubstituiç ão.Estetipotam-
bémpodeserutilizadoemcomandosDMLouPL/SQL.Seuobjetivoésubs-
tituirtalvariável,dentrodecomandosSQLouPL/SQL,porumconjuntode
caracterespredefinidosoudefinidosemtempodeexecuç ão.Aocontráriodas
variáveisbinds,asdesubstituiç ãopodemserutilizadastambémcomoforma
decompletarcomandosSQL,poiselapermiteautilizaç ãodepalavrasreser-
vadasemseuteor.Vejaaseguircomodefinirumavariáveldesubstituiç ão.
SQL> define wempno = 7369
SQL>
Paradefinirumavariáveldesubstituiç ãoutilizamosocomando define
seguidodeumnomeparaavariável. Nesteexemplo,alémdedefinirum
nome,atribuímosumvalorparaavariávelatravésdooperadordeigualdade(
=).Notequeparaasvariáveisdesubstituiç ãonãodefinimosumtipo,poissão
sempredotipoalfanumérico.Vejaumexemplo,utilizandoavariável wempno
queacabamosdedefinir.
SQL> select ename from emp where empno = &wempno;
antigo 1: select ename from emp where empno = & wempno
novo 1: select ename from emp where empno = 7369
ENAME
----------
SMITH
SQL>
Noteque,parautilizarmosavariáveldesubstituiç ão,colocamosnafrente
deseunomeo &.Estaéaindicaç ãodequeestamosutilizandoumavariável
desubstituição.Vejaumexemploutilizando-aemPL/SQL.
SQL> begin
2 for i in (select ename from emp where empno = &wempno) loop
3 dbms_output.put_line(i.ename);
4 end loop;
5 end;
31

## Página 43

5.2. Variáveisdesubstituição CasadoCódigo
6 /
antigo 2: for i in (
select ename from emp where empno = &wempno) loop
novo 2: for i in (
select ename from emp where empno = 7369) loop
SMITH
Procedimento PL /SQL concluído com sucesso.
SQL>
Paraalterarumvalordeumavariáveldesubstituiç ãotambémutilizamos
ocomando define.Vejaaseguir:
SQL> define wempno = 10
SQL>
SQL> begin
2 for i in (
select ename from emp where empno = &wempno) loop
3 dbms_output.put_line(i.ename);
4 end loop;
5 end;
6 /
antigo 2: for i in (
select ename from emp where empno = &wempno) loop
novo 2: for i in (
select ename from emp where empno = 10) loop
Procedimento PL /SQL concluído com sucesso.
SQL>
Jáparasabermosqualovalorcorrentedeumavariáveldesubstituiç ão,
utilizamosocomando defineseguidodonomedavariável.
SQL> define wempno
define wempno = "10" (CHAR)
SQL>
32

## Página 44

CasadoCódigo Capítulo5. Variáveisbindedesubstituição
Comomencionadoanteriormente,asvariáveisdesubstituiç ãopodem
tambémserutilizadasparasubstituiçãodepalavrasreservadas,ouseja,pode-
mosnãosósubstituirtalvariávelporumvaloralfanumérico,comotambém
porumasenten çaSQL,comoumaclausula whereou order by. Vejao
exemplo:
SQL> define gfrom = 'from emp'
SQL> define gwhere = 'where empno = 7369'
SQL> define gorderby = 'order by 1'
SQL>
SQL> select ename &gfrom &gwhere &gorderby;
antigo 1: select ename &gfrom &gwhere &gorderby
novo 1: select ename from emp where empno = 7369 order by 1
ENAME
----------
SMITH
SQL>
IssotambémfuncionaparaPL/SQL.
SQL> begin
2 for i in ( select ename &gfrom &gwhere &gorderby) loop
3 dbms_output.put_line(i.ename);
4 end loop;
5 end;
6 /
antigo 2: for i in (
select ename &gfrom &gwhere &gorderby) loop
novo 2: for i in (
select ename from emp where
empno = 7369 order by 1) loop
SMITH
Procedimento PL/SQL concluído com sucesso.
SQL>
33

## Página 45

5.2. Variáveisdesubstituição CasadoCódigo
Avidaútildeumavariáveldesubstituiç ãotambémserálimitadapela
sessãodoSQL*Plus.Enquantoasessãoestiverativa,elaexistirá.Outrasses-
sõesnãopodemvê-la,comotambémacontececomasvariáveisdotipo bind.
Umavariáveldesubstituiçãopodetersuadefiniç ãoexcluída. Paratalação,
podemosutilizarocomando undefine.Vejaoexemplo.
SQL> undefine gfrom
SQL>
Aocontráriodeumavariável bind,umavariáveldesubstituiç ãonãone-
cessitaserobrigatoriamentedefinidaoudeclarada. Podemossimplesmente
informá-laemnossocomandoSQLouPL/SQL,edeixarqueomotordo
SQL*Plussoliciteovalorparaela,semquesejanecessáriaumadefiniç ãopré-
via.Observeoexemploaseguir:
SQL> select job from emp where empno = &codigo;
Informe o valor para codigo: 7902
antigo 1: select job from emp where empno = &codigo
novo 1: select job from emp where empno = 7902
JOB
---------
ANALYST
SQL> define
define _CONNECT_IDENTIFIER = "xe" (CHAR)
define _SQLPLUS_RELEASE = "902000100" (CHAR)
define _EDITOR = "Notepad" (CHAR)
define _O_VERSION = "Oracle Database 10g Express Edition
Release 10.2.0.1.0 - Production" (CHAR)
define _O_RELEASE = "1002000100" (CHAR )
define 1 = "1" (CHAR)
define _RC = "1" (CHAR)
define wempno = "1111" (CHAR )
define Gwhere = "where empno = 7369" (CHAR)
define GORDERBY = "order by 1" (CHAR)
SQL>
34

## Página 46

CasadoCódigo Capítulo5. Variáveisbindedesubstituição
Vejaqueutilizamosumavariávelcomosubstituiç ão,chamada codigo.
Valeressaltarquenãoadefinimosemnenhummomento. Mesmoassim,o
SQL*Plusareconheceucomoumavariável,poisutilizamoso &nafrente
doseunome,esolicitouumvalorparaela. Destaforma,senãotivermosa
variáveldesubstituiçãojádefinida,oSQL*Plusvaisolicitarumvalor. Note
tambémqueapósasuautilizaç ãooSQL*Plusnãoadeixadefinida,ouseja,
issoocorreapenasemtempodeexecuç ão. EmPL/SQLtambémpodemos
utilizá-ladestaforma.
SQL> declare
2 wjob emp.job%type;
3 begin
4 select job into wjob from emp where empno = &cod_emp;
5 --
6 dbms_output.put_line(wjob);
7 end;
8 /
Informe o valor para cod_emp: 7902
antigo 4: select job into wjob from emp where empno = &cod_emp;
novo 4: select job into wjob from emp where empno = 7902;
ANALYST
Procedimento PL/SQL concluído com sucesso.
SQL>
5.3 U tilizando v ariáveis em arquivos
Tambémpodemosutilizarvariáveisbindsoudesubstituiçãodentrodearqui-
vosedepoisexecutá-losviaSQL*Plus. Nessescasos,seforemencontradas
variáveisdotipo bindoudesubstituiç ão,oSQL*Plusvaifazeropreenchi-
mentodosvalorescorrespondentes.
Noscasosdevariáveis bind,oSQL*Plusnãosolicitaráosvalores,poiseles
jádevemestardefinidos.Nocasodevariáveisdesubstituiç ão,vaidepender
sejáseencontramounãodefinidasnasessão.Vejaosexemplos:
Aseguirestamoscriandoumarquivodescriptchamado S_EMP.sql
contendoocomandopararetornarosempregadoscombaseemumdepar-
35

## Página 47

5.3. Utilizandovariáveisemarquivos CasadoCódigo
tamentoinformadoviaumavariável bind.
SQL> select ename, job from emp where deptno = :bdeptno
2
SQL> save B_EMP.sql
Criado arquivo B_EMP.sql
SQL>
SQL> get B_EMP.sql
1* select ename, job from emp where deptno = :bdeptno
SQL>
Definindoavariável binddentrodasessãodoSQL*Plus:
SQL> var bdeptno number
SQL>
Definindoumvalorparaavariável bind bdeptno:
SQL> exec :bdeptno := 10
Procedimento PL /SQL concluído com sucesso.
SQL> print bdeptno
BDEPTNO
----------
10
SQL>
Executandooarquivo S_EMP.sql:
SQL> @B_EMP.sql
ENAME JOB
---------- ---------
CLARK MANAGER
KING PRESIDENT
MILLER CLERK
SQL>
36

## Página 48

CasadoCódigo Capítulo5. Variáveisbindedesubstituição
Agoravamosveroutroexemploutilizandovariáveisdesubstituiç ão:
SQL> select ename from emp where deptno = &sdeptno
2
SQL> save S_EMP.sql
Criado arquivo S_EMP.sql
SQL>
SQL>
Nocasodasvariáveisdesubstituiç ão,conformejámencionado,mesmo
nãoasdefinindo,oSQL*Plusfazasolicitaç ãodevalores.Vamostestar.
SQL> @S_EMP.sql
Informe o valor para sdeptno: 20
antigo 1: select ename from emp where deptno = &sdeptno
novo 1: select ename from emp where deptno = 20
ENAME
----------
SMITH
JONES
SCOTT
ADAMS
FORD
SQL>
NotequeoSQL*Plussolicitouovaloratravésdalinha“Informeovalor
para sdeptno:”. Nestecaso,foiinformadoovalor20. Contudo,comoa
variávelnãoestádefinida,semprequeexecutamosestescriptoprogramavai
solicitarumvalor.
Paraqueelenãofiquesolicitandoumvalorsempreoquescriptforexe-
cutado, definimosavariávelatravésdocomando define. Comisso, o
SQL*Plusnãopedirámaisovalor.Vejaoexemplo:
SQL> define sdeptno = 10
SQL> @S_EMP.sql
antigo 1: select ename from emp where deptno = &sdeptno
novo 1: select ename from emp where deptno = 10
37

## Página 49

5.3. Utilizandovariáveisemarquivos CasadoCódigo
ENAME
----------
CLARK
KING
MILLER
SQL>
Reparequeagoraelenãopedemaisovalor,apenasfazasubstituiç ãoda
variávelcombasenovalorguardadonasessãodoSQL*Plus.Seexcluirmosa
definiçãodavariável,elevoltaasolicitarovalor.
SQL> undefine sdeptno
SQL> @S_EMP.sql
Informe o valor para sdeptno: 20
antigo 1: select ename from emp where deptno = & sdeptno
novo 1: select ename from emp where deptno = 20
ENAME
----------
SMITH
JONES
SCOTT
ADAMS
FORD
SQL>
Outraformadedefinirumavariáveldesubstituiç ãoéutilizando &&(du-
plo)emvezdeumsó &. IssofazcomqueoSQL*Pluscrieadefiniç ãoda
variável:
SQL> edit S_EMP.sql
SQL> get S_EMP.sql
1* select ename from emp where deptno = &&sdeptno
SQL>
SQL> @S_EMP.sql
38

## Página 50

CasadoCódigo Capítulo5. Variáveisbindedesubstituição
Informe o valor para sdeptno: 10
antigo 1: select ename from emp where deptno = &&sdeptno
novo 1: select ename from emp where deptno = 10
ENAME
----------
CLARK
KING
MILLER
SQL> @S_EMP.sql
antigo 1: select ename from emp where deptno = &&sdeptno
novo 1: select ename from emp where deptno = 10
ENAME
----------
CLARK
KING
MILLER
SQL>
Vejaqueeditamosoarquivo S_EMPeacrescentamosmaisum &aojá
existente.Depois,salvamosoarquivo.Aoexecutá-lo,oSQL*Plusdetectouos
&&,contudo,comoavariávelnãocontinhanenhumvalorinicialdefinido,ele
solicitouumvalor.Jánasegundavezqueexecutamosoarquivo,oSQL*Plus
jánãoosolicitou.Seexecutarmosocomando defineparaverasvariáveis
desubstituiçãodefinidasnasessão,veremosqueoSQL*Plusdefiniuautoma-
ticamenteanossavariável SDEPTNO.
SQL> define
define _CONNECT_IDENTIFIER = "xe" (CHAR)
define _SQLPLUS_RELEASE = "902000100" (CHAR)
define _EDITOR = "Notepad" (CHAR)
define _O_VERSION = "Oracle Database 10g Express Edition
Release 10.2.0.1.0 - Production" (CHAR)
define _O_RELEASE = "1002000100" (CHAR)
define _RC = "1" (CHAR)
define 1 = "30" (CHAR)
39

## Página 51

5.3. Utilizandovariáveisemarquivos CasadoCódigo
define SDEPTNO = "10" (CHAR)
SQL>
Outrorecursoquepodeserutilizadoéapassagemdevaloresparaasva-
riáveisdesubstituiçãoquandoexecutamosumarquivo.Esterecursoestáha-
bilitadosomenteparaasvariáveisdestetipo. Nestecaso,devemosutilizar
indexadoresnuméricosjuntamentecomo &,comoporexemplo, &1, &2etc.
noscomandosdentrodoarquivo.Casocontrário,oSQL*Plusvaiignorareste
valores,solicitandoaentradadelesassimqueforexecutadooarquivo.Vejao
exemploaseguir:
SQL> edit S_EMP.sql
SQL> get S_EMP.sql
1* select ename from emp where deptno = &1
SQL>
Editamosoarquivo S_EMP.sqlmodificandoonomedavariávelde
substituiçãode sdeptnopara1.Agoravamosexecutaroarquivopassando
umvalorcomoparâmetronachamadadaexecuç ão.
SQL> @S_EMP.sql 10
antigo 1: select ename from emp where deptno = &1
novo 1: select ename from emp where deptno = 10
ENAME
----------
CLARK
KING
MILLER
SQL>
Vejaqueovalor10informadonachamadadaexecuç ãodoarquivofoi
passadoparadentrodele,substituindoavariável &1.Comousodeindexa-
dores,oSQL*Plusdefineautomaticamenteavariávelnasessão,ecomisso,
naspróximasexecuções,nãonecessitamosinformarovalorcasoelenãoseja
diferentedaexecuçãoanterior.Paratrocarovalordavariável,bastainformar
umnovovalornachamada.
40

## Página 52

CasadoCódigo Capítulo5. Variáveisbindedesubstituição
SQL> @S_EMP.sql
antigo 1: select ename from emp where deptno = &1
novo 1: select ename from emp where deptno = 10
ENAME
----------
CLARK
KING
MILLER
SQL> @S_EMP.sql 20
antigo 1: select ename from emp where deptno = &1
novo 1: select ename from emp where deptno = 20
ENAME
----------
SMITH
JONES
SCOTT
ADAMS
FORD
SQL>
Noteque,naprimeiraexecuç ão,apenaschamamosoarquivosemapas-
sagemdeumvalor. Comoanteriormentejáhavíamosexecutadooarquivo
passandoovalor10,eleassumiuestevalorparaasdemaisexecuções.Nase-
gundaexecução,informamosumvalordiferente,20,fazendocomqueeleseja
passadocomoparâmetroapartirdeentão.
Outrocomandoqueéutilizadoparadefinirumavariáveldesubstituiç ão
éo accept. Adiferençadelepara defineéquepodemosformataruma
mensagemparasermostradaaousuárionomomentodesolicitaraentrada
deumvalor.Suautilizaç ãoémuitointeressantequandoestamosexecutando
scriptsviaarquivo.Vejaoexemplo.
SQL> edit S_EMP.sql
SQL> get S_EMP.sql
41

## Página 53

5.3. Utilizandovariáveisemarquivos CasadoCódigo
1 accept SDEPTNO number for 999 default 20 prompt "Informe o
deptno: "
2* select ename from emp where deptno = &SDEPTNO
SQL>
SQL> @S_EMP.sql
Informe o deptno: 20
antigo 1: select ename from emp where deptno = & SDEPTNO
novo 1: select ename from emp where deptno = 20
ENAME
----------
SMITH
JONES
SCOTT
ADAMS
FORD
SQL>
Emprimeirolugar,alteramosoarquivo S_EMPacrescentandoalinha
referenteao accept,quedevevirantesdocomandoSQLaoqualsequer
associaramensagemeavariável.Nestenossoexemplo,ocomandoestáantes
do select.Logoapósocomando accept,informamosonomeparava-
riável,seguidopelotipododado.Escolhemosumavariáveldotipo number
quevaisechamar SDEPTNO.Logoapósotipodavariável,podemosinformar
tambémamáscarautilizandoocomando forseguidodoformato.Noexem-
plo,colocamosoformatocomo999(máximode3casas).Tambémdefinimos
ovalor20comopadrão,atravésdaexpressão default,ouseja,avariáveljá
seráinicializadacomestevalor.Eagoravemosuprassumodorecurso.Atra-
vésdocomando prompt,definimosumamensagemparasermostradapara
ousuárionomomentodasolicitaç ãodosvalores. Estamensagemdeveser
informadasemprelogoapósocomando.Porfim,executamosoarquivo.
42

## Página 54

Capítulo6
Aspectosiniciaisdaprogramaç ão
PL/SQL
Comoemqualquerlinguagemdeprogramaç ão,emPL/SQLtambémháre-
grasquedevemserseguidasnahoradecodificarprogramas.Cadalinguagem
deprogramaçãotrabalhadeumaforma,contudocertosconceitosprevalecem
entretodas.
Aspectosrelacionadosaodesenvolvimento,comoáreaspredefinidaspara
declaraçõesdevariáveis,tratamentosdeerrosoucomentáriosemprogramas,
porexemplo,sãocomunsemtodasaslinguagens.Oquedifereentreelaséa
formacomocadaumatrataestesaspectos.
ParaprogramaremPL/SQL,vocêdeveconhecersuasintaxeeoselemen-
tosquepodemserutilizadosnacodificaç ãodosprogramas.Vejaagoraalguns
pontosimportantesparavocêiniciarnaescritadecódigosnestalinguagem.

## Página 55

6.1. Caractereseoperadores CasadoCódigo
6.1 C aracteres e operadores
Dentrodalinguagemvocêpodeutilizarcaractereseoperadoresparaauxiliar
nacodificação.Sãoeles:
•Caracteres: AaZ(maiúsculoseminúsculos),númerosde0a9eos
caracteresespeciais:()+-*/<>=!;:.’@%,"$ &_\{}[]| #
•Operadores Relacionais: <,>,=,!=,>=,<=,ISNULL,ISNOTNULL
•Operadores Lógicos: AND,OReNOT
6.2 I dentificadores
ParanomearidentificadoresemPL/SQL,porexemplo,variáveis,constantes
ouqualquerobjeto,nósdevemosseguiralgumasregras.Sãoelas:
• Aquantidadedecaracteresparanomearumidentificadorédenomá-
ximo30.
• Nãopodemosutilizarpalavrasreservadascomobegin, if, loop, endetc.
• Paranomearosidentificadores,podemosutilizarletras,númeroseal-
gunscaracteresespeciais,masnemtodos.
• Obrigatoriamente,oprimeirocaractereemumnomedeidentificador
deveserumaletra.
Escopo de identificadores
Oescopodeumidentificadorestálimitadoaoblocoondefoideclarado.
Podemosterváriosblocosencadeados. Logo,cadablocopodetersuapró-
priaáreadedeclaraçãodeidentificadores.Nestecaso,umidentificador,por
exemplo,umavariável,declaradaemumblocomaisinterno,nãopoderáser
acessadaemumblocomaisexterno.Vejaoexemploaseguir.
SQL>
create or replace procedure folha_pagamento(pqt_dias number) is
44

## Página 56

CasadoCódigo Capítulo6. AspectosiniciaisdaprogramaçãoPL/SQL
2 --
3 wqt_dias number;
4 wvl_bruto number;
5 wvl_ir number;
6 wvl_liquido number;
7 --
8 begin
9 wvl_bruto := (pqt_dias * 25);
10 --
11 declare
12 wtx_ir number;
13 begin
14 if wvl_bruto > 5400 then
15 --
16 wtx_ir := 27;
17 dbms_output.put_line('Taxa IR: '||wtx_ir);
18 --
19 else
20 --
21 wtx_ir := 8;
22 dbms_output.put_line('Taxa IR: '||wtx_ir);
23 --
24 end if;
25 --
26 wvl_ir := (wvl_bruto * wtx_ir) / 100;
27 --
28 wvl_liquido := (wvl_bruto - wvl_ir);
29 --
30 end;
31 --
32 dbms_output.put_line(
'Valor do salario bruto: '||wvl_bruto);
33 dbms_output.put_line(
'Desconto do valor do IR: '||wvl_ir);
34 dbms_output.put_line(
'Valor do salario liquido: '||wvl_liquido);
35 --
36 exception
37 when others then
45

## Página 57

6.2. Identificadores CasadoCódigo
38 dbms_output.put_line(
'Erro ao calcular pagamento. Erro: '||sqlerrm);
39 end folha_pagamento;
40 /
Procedimento criado.
SQL>
Nesseexemplo,temosumprogramaquecalculaovaloraserpagoaum
empregado,medianteaquantidadedehoraspassadaporparâmetroaum
procedimento. Umadaspremissasparacalcularovalorlíquidoaserpago
éocálculodoimpostoderenda(IR).Seanalisarmosoprograma,épossível
identificardoisblocos.Umprincipaleoutromaisinterno.Oblocointerno
éutilizadoparaocálculodoIR.Notequenelecriamosumasegundaáreade
declaraçãodevariáveisqueéespecíficadestebloco.Alideclaramosavariável
wtx_irquereceberáataxaparaocálculodoimpostomedianteumacondi-
ção.Apartirdaobten çãodataxa,écalculadoovalordoimpostoetambém
ovalorlíquidoaserpago.
Observações importantes:oescopodavariável wtx_irestálimitadoao
blocoemqueelafoideclarada.Casoausássemosforadesteescopo,oOra-
clegerariaumerroindicandoqueelanãofoideclarada. Emcontrapartida,
podemosobservarqueasvariáveis wvl_ire wvl_liquidoestãosendo
utilizadasdentrodoblocomaisinterno,semquenenhumerroaconte ça.Isso
épossíveldevidoaofatodeelasteremsidodeclaradasemumblocomais
externo.Logo,seusescoposabrangemtodooblocoondeforamdeclaradas,
inclusive,blocosinternoscontidosneste.Segueoresultado.
SQL> begin folha_pagamento(pqt_dias => 300); end;
2 /
Taxa IR: 27
Valor do salario bruto: 7500
Desconto do valor do IR: 2025
Valor do salario liquido: 5475
Procedimento PL /SQL concluído com sucesso.
46

## Página 58

CasadoCódigo Capítulo6. AspectosiniciaisdaprogramaçãoPL/SQL
SQL>
6.3 T ransações
Primeiramente,antesdecome çarmosatrabalharcomPL/SQL,éprecisoco-
nheceroconceitodetransaç ão.Umadascaracterísticasmaisbem-vindasdos
bancosdedadosCliente/Servidor,emrelaç ãoaosbancosdedadosdesktop,
éoconceitodetransações. Umatransaç ãoéumaunidadelógicadetraba-
lhocompostaporumaoumaisdeclaraçõesda Data Manipulation Language
(DML)ou Data Definition Language(DDL).Oscomandosparaocontroleda
transaçãosãoaquelesnecessáriosparaquesepossacontrolaraefetivaç ãoou
nãodasmodificaçõesfeitasnobancodedados.
Paraexplicaroqueéumatransaç ão,pode-setomarcomoexemplouma
transferência bancária onde um determinado valor é transferido de uma
contaparaoutra.Oprocessodetransferênciadestevalorconsisteemvários
passos,quesãoagrupadosdemodoque,senãoforemconcluídosemsuatota-
lidade,ouseja,seatransaç ãonãochegaratéofinal,todasasoutrasalterações
járealizadasserãodescartadaseacontavoltaráaoseuestadoanterior,como
senenhumatransferênciativessesidorealizada.Atravésdestecontrole,pode-
segarantirqueosdadospermanecerãoconsistentes.Oscomandos commit
e rollbackdaDCLauxiliamnestetrabalho.
Commit
Tornampermanentestodasasalteraçõesfeitasnobancodedadosdurante
asessão.Todasasalteraçõesrealizadasemumadeterminadatransaç ãoserão
confirmadascasoestecomandosejaaplicado.
47

## Página 59

6.3. Transações CasadoCódigo
Fig.6.1:Confirmandoasalteraçõesnobancodedados
Rollback
Usadoparadesfazertodasasalteraçõesfeitasdesdeoúltimo commitdu-
ranteasessão.Essecomandovairestaurarosdadosaolugarondeelesestavam
noúltimocommit.Alteraçõesserãodesfeitascasoatransaç ãosejaencerrada
pelocomando rollback.
48

## Página 60

CasadoCódigo Capítulo6. AspectosiniciaisdaprogramaçãoPL/SQL
Fig.6.2:Desfazendoasalteraçõesnobancodedados
NoOracle,umatransaç ãoseiniciacomaexecuç ãodaprimeirainstruç ão
SQLeterminaquandoasalteraçõessãosalvasoudescartadas. Ocomando
set transaction tambéminiciaumatransaç ão–transaçãoexplícita. O
usodocomando set transaction determinaalgumasregras,asquaissão
listadasaseguir.
49

## Página 61

6.3. Transações CasadoCódigo
• Deveseroprimeirocomandodatransação(casocontrário,ocorrerá
umerro);
• Somenteconsultassãopermitidasnatransação;
• Umcommit, rollback ou qualquer outro comando de DDL
(possuemcommitsimplícitos)encerramoefeitodocomando set
transaction.
Fig.6.3:Abrindoumanovatransaç ãodentrodoSQL*Plus
Nota:AfiguramostraumcomandoDMLsendoexecutadoe,logoapós,
umatransaçãosendoaberta.Comoumadasregrasparaseabrirumatran-
saçãoéqueelasejaumdosprimeiroscomandosdatransaç ão,oerroacon-
tecequandoexecutamosocomando.Notequeapósencerrarmosatransaç ão
(atravésdo rollback)abertapelocomandoDML,nósconseguimosexecu-
tarocomandoeabrirumanovatransaç ão.
50

## Página 62

CasadoCódigo Capítulo6. AspectosiniciaisdaprogramaçãoPL/SQL
6.4 T ransações em PL/SQL
AstransaçõesemPL/SQLseguemosmesmopreceitosexpostosanterior-
mente. Umpontoaacrescentaréousodos savepoints. Quandotra-
balhamoscomPL/SQLtemosesterecursoquenospermitedefinirpontos
desalvamentodentrodoprograma.Todavia,nãoéumapráticamuitoutili-
zada,principalmentepelofatodegeralmentetrabalharmoscomgrandesvo-
lumesdecódigo,poispodedificultaroentendimentodoprogramaeinclusive
desestruturá-lologicamente.Ésemprebomtermuitocuidadoquantoàefe-
tivaçãodedadosnomomentodeconstruirmosnossosprogramas.Devemos
visarsempreàconsistênciaeintegridadedasinformaçõesmanipuladasafim
deatingirmosoobjetivoesperado.Alémdepermitirquesejamsalvaspartes
deaçõesemdeterminadospontosdoprograma,tambémépossíveldesfazer
taisaçõesusandoestesmesmospontosdesalvamento.
Vejaumexemplosimplesdousodesterecurso.
SQL> begin
2 insert into dept values (41, 'GENERAL LEDGER', '');
3 savepoint ponto_um;
4 --
5 insert into dept values (42, 'PURCHASING', '');
6 savepoint ponto_dois;
7 --
8 insert into dept values (43, 'RECEIVABLES', '');
9 savepoint ponto_tres;
10 --
11 insert into dept values (44, 'PAYABLES', '');
12 rollback to savepoint ponto_dois;
13 --
14 commit;
15 end;
16 /
Procedimento PL/SQL concluído com sucesso.
SQL>
Neste exemplo temos vários pontos de salvamento identificados por
51

## Página 63

6.5. Trabalhandocomvariáveiseconstantes CasadoCódigo
ponto_um, ponto_doise ponto_tres. Cadapontoestáreferenciando
umcomando insert.Logoapós,temosum rollback to savepoint
desfazendotodasasoperaçõesapartirdo ponto_dois.Issoindicaqueos
comandosreferentesàslinhas2e5permanecemintactos. Jáoscomandos
referentesàslinhas8e11serãodescartados.
6.5 T rabalhando com v ariáveis e constantes
Identificadoresdevariáveiseconstantessãomuitocomunsemprogramas
PL/SQL,poistodaainformaç ãogeralmenteémanipuladadentrodelesena
maioriadasvezesprecisamosarmazená-laemmemóriaantesde,porexem-
plo,inseri-laemumatabela,enviarparaumaimpressoraouparaexportá-la
paraalgumoutrosistema.
Dessaforma,variáveiseconstantesnadamaissãoqueáreasemmemória
definidaseusadasdentrodeprogramaqueservemparaguardarinformações
emtempodeexecuç ão. Comoonomesugere,umavariávelpodeterseus
valoresatualizadosváriasvezesaolongodaexecuç ãodeumprograma.Con-
tudo,umaconstantenascecomumvalordefinidoeomantématéotérmino
dasuautilizaç ão.
Umavariávelouconstantedeveterumtipodefinido,quenãosealtera
aolongodaexecuç ãodeumprograma. Aodeclará-las,recebemumnome
queserásuaidentificação.Porregra,dentrodoOracle,estenomenãopode
ultrapassar30caracteres.Nomais,eladeveobedeceràsregrasdedefiniç ão
mencionadasanteriormentequandofalamosdeidentificadores.Estadefini-
çãodeveserfeitadentrodeumaáreaespecíficadedeclaraçõesdevariáveis
quecadablocoPL/SQLpodeter,identificadacomo declare.
Oescopodeumavariávelouconstanteselimitaaoblocoemqueforam
declaradas,podendosempreseracessadasnoseublocoeemblocosmaisin-
ternos,nuncaemblocosexternosàsuadeclaraç ão.Entretanto,casoumava-
riáveltenhasidodeclaradaduasvezes(mesmonome),umaemumblocoex-
ternoeoutraemumblocomaisinterno,avariáveldoblocoexternonãopo-
deráseracessadadentrodointerno,poishaveriaumconflito.Todavia,pelas
boaspráticasdeprogramaçãonãodevemosteridentificadorescomomesmo
nome.Logo,casoscomoestenãosãocomuns.
52

## Página 64

CasadoCódigo Capítulo6. AspectosiniciaisdaprogramaçãoPL/SQL
Alémdostipospredefinidos,comonumérico,data,string,entreoutros,
asvariáveiseconstantespodemreferenciartiposdedadosdedeterminadas
colunasdeumatabelacriadaemumbancodedados( %TYPE),ouseutipo
podereferenciarumatabelainteira( %ROWTYPE).Quandodeclaramosuma
variávelpodemosdefinirumvalorpadrão,chamadode DEFAULT,paraque
elajáinicializeassim.Paraasconstantes,issoéobrigatório.
Nomais,osvaloresdevariáveiseconstantespodemsermanipuladose
convertidosparaoutrostiposafimdeseremutilizadosdentrodosprogra-
masparasatisfazerobjetivosespecíficos.Seguemexemplosdedeclaraçõesde
variáveis.
DECLARE
DT_ENTRADA DATE DEFAULT SYSDATE;
DT_SAIDA DATE;
FORNECEDOR TIPO_PESSOA; -- Tipo de dado definido pelo
desenvolvedor
QT_MAX NUMBER(5) DEFAULT 1000;
QT_MIN CONSTANT NUMBER(50) DEFAULT 100;
NM_PESSOA CHAR(60);
VL_SALARIO NUMBER(11,2);
CD_DEPTO NUMBER(5);
IN_NAO CONSTANT BOOLEAN DEFAULT FALSE ;
QTD NUMBER(10) := 0;
VL_PERC CONSTANT NUMBER(4,2 ) := 55.00 ;
CD_CARGO EMPLOYEE.JOB%TYPE;
REG_DEPT DEPARTMENT%ROWTYPE;
6.6 T ipos de dados em PL/SQL
V ARCHAR2
Tamanhomáximoparacamposdetabela: 4.000bytes. Tamanhomáximo
paraPL/SQL:32.767bytes.O VARCHAR2évariávelesomenteusaoespaço
queestáocupado.Diferentementedo CHAR.
VARCHARéumsubtipo(assimcomo STRING)queexisteporquestões
decompatibilidadecomoutrasmarcasdebancodedadosetambémcom
opadrãoSQL.Entretanto,aOraclenomomentonãorecomendaousodo
53

## Página 65

6.6. TiposdedadosemPL/SQL CasadoCódigo
tipo VARCHARporquesuadefiniçãodevemudaràmedidaqueopadrãoSQL
evoluir.Deve-seusar VARCHAR2.
CHAR
Tamanhomáximo:2.000bytes
Otipo CHARéusadoparaconterdadosdestringdecomprimentofixo.
Aocontráriodasstringsde VARCHAR2,umastring CHARsemprecontémo
númeromáximodecaracteres.
Outrostipos:
•NCHARTamanhomáximo:2.000bytes;
•NCHAR VARYING Tamanhomáximo:4.000bytes;
•CHAR VARYING Tamanhomáximo:4.000bytes.
NUMBER(p,s)
Numéricocomsinalepontodecimal,sendoque péaprecisãode1a38
dígitose séaescala,de-84a127.
Estetipotambémpossuisubtiposcomo:
•DECIMAL:igualaNUMBER
•DEC:igualaDECIMAL
•DOUBLE PRECISION:igualaNUMBER
•NUMERIC:igualaNUMBER
•REAL:igualaNUMBER
•INTEGER:equivalenteaNUMBER(38)
•INT:igualaINTEGER
•SMALLINT:igualaNUMBER(38)
•FLOAT:igualaNUMBER
54

## Página 66

CasadoCódigo Capítulo6. AspectosiniciaisdaprogramaçãoPL/SQL
•FLOAT(prec):igualaNUMBER(prec),masaprecisãoéexpressaem
termosdebitsbinários,nãodedígitosdecimais. Aprecisãobinária
podevariarde1até126.
•BINARY_INTEGER:semelhanteaINTEGER.Éusadaparaindexarta-
belaPL/SQL.
DATE
1 JAN 4712 BC até31 DEC 4712 AD (DATAcomhora,minutoese-
gundo)Otipo DATEéusadoparaarmazenarosvaloresdedataehora.Um
nomemelhorseria DATETIMEporqueocomponentedehoraestásemprelá,
independentedevocêusá-loounão.Senãoforespecificadaahoraaoatri-
buirumvalorparaumavariáveldestetipo,opadrãodemeia-noite(12:00:00
a.m.)seráusado.
BOOLEAN
Truee False.
LONG
Tamanhomáximoparatabela: 2GB.TamanhomáximoparaPLSQL:
32.760.Somentepodeexistirumacolunaportabela.
RAW
Tamanhomáximoparacamposdetabela:2.000bytes.Tamanhomáximo
paraPL/SQL:32.767. LONG RAW éoutrotipoparecidocom RAW,adiferen ça
équeelepossui7bytesamenosquandoutilizadoemPL/SQL.
CLOB
Tamanhomáximo: (4 GB - 1) * DB_BLOCK_SIZE.Parâmetrode
inicialização:8TBa128TB.Onúmerodecolunas CLOBportabelaélimitado
somentepelonúmeromáximodecolunasportabela.
Armazenatextos,quesãovalidadosconformeosetdecaracteres,ouseja,
armazenaacentuaçãoetc.
55

## Página 67

6.6. TiposdedadosemPL/SQL CasadoCódigo
Tipos LOB,surgiramemsubstituiç ãoaostipos LONGe LONG RAW,pois
elessópermitiamumacolunaportabela.Jáostipos LOBpermitemmaisde
umacoluna.
NCLOB
Tamanhomáximo: (4 GB - 1) * DB_BLOCK_SIZE.Parâmetrode
inicialização:8TBa128TB.Onúmerodecolunas NCLOBportabelaélimi-
tadosomentepelonúmeromáximodecolunasportabela.
Objetodegrandecapacidadedecaracteresnacionais–contématé4GBde
caracteresdebytessimplesoucaracteresmultibytequeatendemoconjunto
decaracteresnacionaldefinidopelobancodedadosOracle.
BLOB
Tamanhomáximo: (4 GB - 1) * DB_BLOCK_SIZE.Parâmetrode
inicialização:8TBa128TB.Onúmerodecolunas BLOBportabelaélimitado
somentepelonúmeromáximodecolunasportabela.
Armazenamdadosnãoestruturadoscomo: som,imagem,dadosbiná-
rios.
BFILE
Tamanhomáximo:4GB.Tamanhomáximoparaonomedoarquivo:255
caracteres. Tamanhomáximoparaonomedodiretório: 30caracteres. O
valormáximode BFILEsélimitadopelovalordoparâmetrodeinicializa-
ção SESSION_MAX_OPEN_FILES,oqualélimitadopelonúmeromáximo
dearquivosabertosqueosistemaoperacionalsuporta.
ROWID
Éumtipoespecialusadoparaarmazenaros ROWIDs(endere çosfísicos)
daslinhasarmazenadasemumatabela.
Campos LONG
Emresumo, ostiposcomumenteutilizadossão: CHAR, VARCHAR2,
NUMBER, DATE, BOOLEANeosdafamília LOB.
56

## Página 68

CasadoCódigo Capítulo6. AspectosiniciaisdaprogramaçãoPL/SQL
Noentanto,existemalgumasrestriçõesparacampos LONGe LONG RAW.
• NãosepodecriarumOBJECT TYPE comoatributode LONG.
• UmacolunaLONGnãopodeestardentrodacláusula WHEREoucom
referênciaintegraldosdados,exceto NULLou NOT NULL.
• Umafunçãonãopoderetornarumcampo LONG.
• UmatabelapoderátersomenteumcampoLONG.
•LONGnãopodeserindexada.
•LONG não pode usar cláusulasWHERE, conforme já mencionado,
GROUP BY, ORDER BY e CONNECT BY.
Umadicaparavocêusarumcampo LONGnacláusulaWHEREécriaruma
tabelatemporáriacomoscamposdatabelaoriginal,masalterandoumtipo
LONGpara CLOB.Tambémépossívelalterardiretamentenatabelaocampo
LONGpara CLOB,casonãotenhaproblemadealteraraestruturadatabela
original.
57

## Página 70

Capítulo7
Exceções
Exceções são utilizadas dentro do Oracle quando algum erro acontece.
QuandoconstruímosprogramasemPL/SQLéfundamentaltratarmosasex-
ceçõesquepodemocorrermedianteaexecuç ãodosistemaeseusdiversos
processos.Basicamente,existemdoistiposdeexce çõesdentrodoOracle:as
predefinidaseasdefinidaspelousuário.
•Exceções predefinidas:sãoexce çõesexistentesimplicitamentedentro
doOracleequesãodisparadasautomaticamenteporelequandoocorre
umerronoprograma.
•Exceções definidas pelo usuário:sãoexce çõesqueprecisamserdecla-
radasedisparadaspelousuário.OOracledesconhecesuaexistência.

## Página 71

7.1. Exceçõespredefinidas CasadoCódigo
7 .1 E xceções predefinidas
Comofoidito,umaexce çãoéacionadaquandoumerroacontecedentrodo
programa. Mesmoquenãoastratemos,oOracleinterceptaoproblemae
mostraoerro.Todavia,sedeixarmosqueoOraclefaç aistonóspodemoster
sériosproblemas,poiserrosquenãosãotratadoscausamaparadadosistema,
ouseja,oprogramaéabortado.
DentrodaPL/SQLtratamosesteserrosatravésdas exceptions. Os
maisvariadostiposdeerrospodemsertratadosatravésdesterecurso. Por
exemplo,setemosdentrodonossoprogramaPL/SQLumcálculoondepossa
acontecerumadivisãoporzero,casoocorra,umerroédisparado,poissabe-
mosquematematicamentenãoépossívelresolvê-lo.APL/SQLsabedissoe
vaigerarumaexce çãocasoistoocorra.Medianteisto,podemosnosantecipar
etratarestepossívelerro.
Umpontobomdetratarmososerroséapossibilidadedemostrarmos
mensagens mais amigáveis aos usuários e lhes propor ações que possam
ajudá-losaresolversemainterven çãodaáreadesuporte,porexemplo.Além
domais,evitamosqueoprogramaoutodoosistemasejaabortado,oque
gerariaumgrandeincômodo.Atravésdotratamentodeexce çõestambémé
possíveldeterminarseoprogramapodecontinuarounãocomaaç ãoapóso
erroterocorrido.
Como este acionamento é feito?
QuandoaconteceumdesseserrospredefinidospeloOracle,automatica-
menteaPL/SQLpercebesuaocorrênciaeotransfereparaumaáreadetrata-
mentodeerro.Noentanto,àsvezesesseserrosdemonstramcertafaltadecla-
rezaemsuasdescrições,envolvendotermosmuitotécnicos,geralmenteem
inglês,oquepodeconfundirousuário.Comissoemmente,elespodemser
tratadospelodesenvolvedordesistemasafimdetorná-losmaiscompreensí-
veis.Contudo,omesmonãoacontececomoserroscausadospelosusuários.
EstetipodeerroaPL/SQLnãoconseguedetectarpelofatodenãoestarem
incluídosimplicitamentenoOracle. Ousodasexce çõesébemflexível,po-
dendoserusadasdentrodeblocosanônimos, procedures, functions,
packagese triggers.
60

## Página 72

CasadoCódigo Capítulo7. Exceções
Primeiramente,vamosfalarsobreas exceptionspredefinidas.Segue
umalistade exceptionsquepodemserutilizadasemPL/SQL.
•no_data_found:disparaquandoum select into éexecutadoe
nãoretornanenhumregistro.Nãoocorreseusarmosfun çõesdegrupo,
poisestasretornamvaloresnulosquandonãoháregistros. Também
nãoocorreem fetch(usadoemcursores).Nestecasousamosatribu-
tosdecursor.Exemplo: C1%NO* TFOUNDretornaverdadeirosenão
encontrarmaislinhas.
•invalid_cursor:tentamosusarumcursorquenãoestáaberto.
•invalid_number:quandoaconversãodeumtipoparaoutronãoé
possível,ouquandoumvalorultrapassaonúmerodecasasdefinidas
paraotipodedado.Exemplo:umavariável number(2)recebeovalor
100.
•login_denied:tentativadeconectaraobancodedadoscomusuário
inválido.
•cursor_already_open:tentamosabrirumcursorquejáseencon-
traaberto.
•dup_val_on_index:tentativadeinserirvalorduplicadoemumín-
diceúnico.Usadonaverificaç ãodechaveprimáriaouúnica.
•not_logged_on:tentamosusaralgumrecursodobancosemestar-
mosconectados.
•program_error: erro interno ao sistema Oracle, chamado de
internal.
•rowtype_mismatch:quandoum fetchretornaumadeterminada
linhadobancodedadosparaumavariáveldotiporegistroondeosda-
dosdestalinhanãosãocompatíveiscomostiposdefinidosnavariável.
•timeout_on_resource: tempoexpirouquandoobancoesperava
pelorecurso.
61

## Página 73

7.1. Exceçõespredefinidas CasadoCódigo
•too_many_rows:um select into retornoumaisdeumalinha.
•value_error: em algumas circunstâncias é disparado
invalid_numberou value_error.
•zero_divide:tentamosdividirporzero.
•others:quandonãosabemosqualerropodeocorrer.
Estaéumalistadas exceptionsmaiscomuns.Paramaioresdetalhese
demaisexce ções,consulteadocumentaç ãodobancodedadosdaversãoque
estiverutilizando.
Vamosabrirumparênteseparafalarumpoucosobreaexce ção others
esobreasexce ções invalid_numbere value_error.
A exception others émuitoutilizada,poismesmoquetratemoser-
rosespecíficossempreautilizamosparagarantirquedemaiserrosnãocau-
semaparadadosistema. Qualquer exceptionquandonãotratadaem
específicoacabasendoamparadapelaexce ção others. Portanto,quando
tratamosdiversasexce çõesdevemossemprecolocá-laporúltimonase çãode
tratamento.Outropontoaltamenterecomendadoéquepelomenosaexce ção
otherssejasempretratada,independentesejáestamostratadodeoutrasem
específico.
Jácomrelaçãoàsexce ções invalid_numbere value_error,embora,
possamparecerredundantes,existemlugaresespecíficosondeelaspodemser
usadas. invalid_numberéacionadaporerrosemcomandosSQLdentro
dosblocosPL/SQL.Jáaexce ção value_errorédisparadaporerrosem
comandosPL/SQL.
Vejaondeecomotratarasexce ções.Analiseocasoaseguir.
SQL> declare
2 wempno number;
3 begin
4 --
5 select empno
6 into wempno
7 from emp
8 where deptno = 9999;
62

## Página 74

CasadoCódigo Capítulo7. Exceções
9 --
10 end;
11 /
declare
*
ERRO na linha 1:
ORA-01403: dados não encontrados
ORA-06512: em line 5
SQL>
Nesteexemploestamostentandoselecionaroempregadocomocódigo
9999.Entretanto,esteempregadonãoexiste.Comoestamosutilizandoum
select into,sabemosquequandoum selectdestetiponãoretorna
linhasoOracledisparaumaexce ção. Nestecaso,foioqueaconteceu. Ao
tentarmosselecionaralinha,ocomandonãoalocalizoufazendocomque
oOraclegerasseumaexce ção. Oresultadofoiumamensagemdeerroin-
formandoqueosdadosnãoforamencontrados. Contudo,estamosfalando
deumexemplosimples.Setivéssemosumprogramacommuitoscomandos
select,ficariadifícilsaberondeestariaoerro.Semfalarqueamensagem
nãoajudariamuitoousuárioaresolveroproblemaporsisó.Agoravamos
tratarestaexce çãoeveroqueacontece.
SQL> declare
2 wempno number;
3 begin
4 --
5 select empno
6 into wempno
7 from emp
8 where deptno = 9999;
9 --
10 exception
11 when no_data_found then
12 dbms_output.put_line('Empregado não encontrado.');
13 when others then
14 dbms_output.put_line('Erro ao selecionar empregado.');
63

## Página 75

7.1. Exceçõespredefinidas CasadoCódigo
15 end;
16 /
Empregado não encontrado.
Procedimento PL /SQL concluído com sucesso.
SQL>
Primeiramente,vamosanalisaroprograma. Comopodeservisto,en-
treo begineo end,temosaexpressão exception. Énestaáreaque
definimosquaisexce çõesvamostratar. Percebaquelogoapósaexpressão
exceptiontemosváriascláusulaswhenindicandoquaisexce çõesestamos
tratando. Nesteexemplo,estamostratandoasexce ções no_data_found
e others. Otratamentodeexce çõesdevesempreacompanharumbloco
PL/SQLeseuescopoéválidosomentedentrodele.Vejaasintaxe.
declare
-- variáveis
begin
--
-- comandos
begin
-- comandos
exception
when <exception 1> then
-- comandos ou mensagens.
when <exception n > then
-- comandos ou mensagens.
end;
-- mais comandos
--
exception
when <exception 1> then
-- comandos ou mensagens.
when <exception n> then
-- comandos ou mensagens.
end;
Vejanesteexemploquetemosumblocodentrodeoutro,ecadaumpossui
64

## Página 76

CasadoCódigo Capítulo7. Exceções
suaáreadetratamentodeexce ções.Notetambémqueestaédefinidasempre
nofimdobloco.Muitobem,continuandonossoexemplo,podemosperceber
queneletemosdoistratamentos. Umparaverificarseoempregadoexiste
eoutroparaocasodeacontecerqualqueroutroerrodequenãosetenha
conhecimento.
Depropósito,tentamosselecionarosempregadosquesãodeumdeparta-
mentoquenãoexistenatabelaEMPparaqueaexce çãofosseacionada.Com
oacionamentodaexce ção,amensagem“Empregadonãoencontrado”foiim-
pressanatela,atingindonossoobjetivo.Comisso,foipossívelmostraruma
mensagemmuitomaisinteligíveledequebranãopermitimosqueoOracle
abortasseoprograma.Utilizamosopacote dbms_outputparaimprimirna
telaanossamensagemdeerro.
Nesteexemplo,vamoscolocarumcódigodedepartamentoqueexistena
tabelaEMP.
SQL> declare
2 wempno number;
3 begin
4 --
5 select empno
6 into wempno
7 from emp
8 where deptno = 30;
9 --
10 exception
11 when no_data_found then
12 dbms_output.put_line('Empregado não encontrado.');
13 when others then
14 dbms_output.put_line('Erro ao selecionar empregado.');
15 end;
16 /
Erro ao selecionar empregado.
Procedimento PL/SQL concluído com sucesso.
SQL>
Analisando este segundo exemplo podemos observar que a exceção
65

## Página 77

7.1. Exceçõespredefinidas CasadoCódigo
no_data_foundnãofoiacionada.Entretantoaexce ção othersfoi.Tam-
bémpudera,quandocolocamosumcódigodedepartamentoexistentenata-
belaEMP,o selectretornouváriaslinhas.Váriaslinhasemum select
intogeramumaexce çãochamada too_many_rows.Destaformavamos
incluí-laemnossoprograma.
SQL> declare
2 wempno number;
3 begin
4 --
5 select empno
6 into wempno
7 from emp
8 where deptno = 30;
9 --
10 exception
11 when no_data_found then
12 dbms_output.put_line('Empregado não encontrado.');
13 when too_many_rows then
14 dbms_output.put_line(
'Erro: O código de departamento informado'||
15 ' retornou mais de um registro.');
16 when others then
17 dbms_output.put_line('Erro ao selecionar empregado.');
18 end;
19 /
Erro: O código de departamento informado retornou mais de um
registro.
Procedimento PL /SQL concluído com sucesso.
SQL>
Incluindoaexce ção too_many_rows,foipossíveltrataroerroemes-
pecíficoemelhoraramensagemdeerro.Valesalientarquea exceptionfoi
incluídaantesdaexce ção others.Issosempredeveserfeitodestaforma.
Voltandoumpouconoexemploanterioraeste,foipossívelobservarque
semotratamentodaexce ção too_many_rows,ficoudifícilidentificarqual
66

## Página 78

CasadoCódigo Capítulo7. Exceções
oproblemaocorreu,poiscomoaexce ção otherséparatodasasexce ções
quepodemocorrerdentrodoprograma,nãoconseguimosespecificaruma
mensagemdeerroclaraosuficiente. Éóbvioquenesseexemplo,sabíamos
qualeraoproblemaealteramosoprogramaparatratá-lo.Contudo,mesmo
assim,outrostiposdeproblemaspodemocorrerforaostratadosespecifi-
camente.Casoissoaconte ça,énecessáriopelomenosumamensagemmais
detalhadasobreoerro,paraqueoproblemapossaseridentificadoeresolvido.
Paraidentificarerrosnãoconhecidos,aquelesqueacabamcaindonaex-
ceção others,podemoscontarcomduasvariáveisquesãoalimentadascada
vezqueuma exceptionédisparada.Asvariáveissão sqlcodee sqlerrm.
Aprimeiramostrasomenteocódigoeasegundamostraocódigoeadescri-
çãodoerro,vindosdoOracle. CadaerrodentroOraclepossuiumcódigo
associadoaele. Destaforma,quandouma exceptionégerada,ocódigo
doerrocorrenteégravadonavariável sqlcode. Amesmacoisaacontece
comavariável sqlerrm. Cadaerropossuiumadescriç ãoexplicandoseu
motivo.Aosergeradaumaexce ção,estavariávelrecebeadescriç ãodoerro
corrente.Comisto,épossívelobterocódigoedescriç ãodoerro,oquepossi-
bilitaidentificarsuacausa.Estasvariáveispodemedevemserusadasquando
tratamosaexce ção others.
Valesalientar,entretanto,quenamaioriadasvezesadescriç ãodoserros
vindosdoOraclenãosãodescriçõesmuitoamigáveis.Osusuáriospodemter
dificuldadesemidentificaroqueexatamenteocorreu.Porissoaimportância
detratarmospelomenosasexce çõesconhecidasdentrodeumprograma,
afimdeclarearaomáximooserrosquepodemocorrer. Vamosvoltarao
exemploanterioreusarasvariáveisparaidentificaroproblemaocorrido.
SQL> declare
2 wempno number;
3 begin
4 --
5 select empno
6 into wempno
7 from emp
8 where deptno = 30;
9 --
10 exception
67

## Página 79

7.1. Exceçõespredefinidas CasadoCódigo
11 when no_data_found then
12 dbms_output.put_line('Empregado não encontrado.');
13 when others then
14 dbms_output.put_line(
'Erro ao selecionar empregado. Erro: '||sqlerrm
15 ||' - Código: ('||sqlcode||').');
16 end;
17 /
Erro ao selecionar empregado. Erro: ORA-01422: a extração exata
retorna mais do
que o número solicitado de linhas - Código: (-1422).
Procedimento PL /SQL concluído com sucesso.
SQL>
Noexemploaseguirconcatenamosasvariáveis sqlcodee sqlerrm
comnossamensagemdeerro. Umaobservaç ão, avariável sqlerrmjá
trazocódigodoerro,nãotendonecessidadedeutilizaro sqlcode,ame-
nos,éclaro,quevocêqueirausarestecódigoparaalgodiferentedeape-
nasmostrarainformaç ão. Paramostrarapenasadescriç ãodoerrouse
sqlerrm(sqlcode). Notetambémqueainforma çãovindadobancode
dadosnãoémuitoclara.Dependendodalinguageminstaladaparabancode
dados,oOracleprocuratraduziramensagemdeerroeàsvezestornamais
difícilsuacompreensão.
Umadicaimportante: casovocênãocompreendaamensagemdeerro
ouelanãoexista,épossível,atravésdocódigodoerro,pesquisarmaiores
detalhesnadocumentaçãodobancoOracleounainternet.Estescódigossão
padronizadoseemqualquerversãooulinguagemelessemantêmosmesmos.
Umavezgeradaaexce ção,issonãogarantequeoprogramavápararo
processo.Comofoivisto,podemosterváriosblocosdentrodomesmopro-
gramaPL/SQLecadaumdestesblocospodemtertratamentosdeerros.Estes
blocos,porsuavez,podemconterdependênciasunscomosoutroseparaisto
podesernecessáriopararoprocessoquandoumerroacontece,nãopermi-
tindoqueoprogramacontinue.
68

## Página 80

CasadoCódigo Capítulo7. Exceções
Nota:ofatodenóstratarmosas exceptionsnosremeteaoutro
pontoaquedevemosestaratentos. Quandonãoatratamos,oOracle
realizaestetratamentoeabortaoprograma.Jáquandootratamentofica
pornossaconta,oumelhor,porcontadonossoprograma,somosnós
quemdefinesehaveráounãoumaparadanosistemaounoprocesso
queestásendoexecutado,ouseja,quandotratamosumerro,oOracle
passaanãotratá-lomaiseasaçõesficampornossaconta.
Vejaoexemploaseguir.
SQL> declare
2 wsal number;
3 wdeptno number;
4 begin
5 --
6 begin
7 select avg(sal), deptno
8 into wsal, wdeptno
9 from emp
10 where deptno = 99
11 group by deptno;
12 exception
13 when no_data_found then
14 dbms_output.put_line(
'Valores não encontrados para o departamento 99.');
15 when others then
16 dbms_output.put_line('Erro ao selecionar valores
referentes ao depto. 99. '||
17 'Erro: '||sqlerrm||'.' );
18 end;
19 --
20 begin
21 insert into emp (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
22 values (8002, 'ANGELINA', 'MANAGER', 7839,
TO_DATE('20/10/2011','DD/MM/RRRR'),
wsal, null, 20);
69

## Página 81

7.1. Exceçõespredefinidas CasadoCódigo
23 --
24 commit;
25 --
26 exception
27 when others then
28 dbms_output.put_line(
'Erro ao inserir novo empregado. '||
29 'Erro: '||sqlerrm||'.');
30 end;
31 --
32 dbms_output.put_line(
'Empregado ANGELINA inserido com sucesso.');
33 --
34 exception
35 when no_data_found then
36 dbms_output.put_line('Empregado não encontrado.');
37 when too_many_rows then
38 dbms_output.put_line(
'Erro: O código de departamento informado'||
39 ' retornou mais de um registro.');
40 when others then
41 dbms_output.put_line(
'Erro ao inserir empregado. Erro: '||sqlerrm
42 ||' - Código: ('||sqlcode||').');
43 end;
44 /
Valores não encontrados para o departamento 99.
Empregado ANGELINA inserido com sucesso.
Procedimento PL /SQL concluído com sucesso.
SQL>
NesteexemplocriamosumblocoPL/SQLqueinsereumnovoempre-
gado.Dentrodonossoprogramatemosum selectquebuscaamédiados
saláriosdosempregadosdeumdeterminadodepartamento.Neste select
estamostratandoasexce ções no_data_founde others.Logoapós,rea-
lizamosainclusãodoempregadoatravésdocomando insertinformando
comosaláriodesteempregadoovalorvindodo selectanterior. Depois
70

## Página 82

CasadoCódigo Capítulo7. Exceções
informamosaousuárioqueoempregadofoiinseridocomsucesso.Vejaque
paraocomando inserttambémestamostratandoaexce ção otherspara
ocasodealgumerro.
Entretanto,executandooprogramapodemosobservarquealgumasmen-
sagensforamgeradas,inclusiveadequeosvaloresdossaláriosnãoforamen-
contradosparaodepartamentoemquestão.Oresultadodissofoiainclusão
doempregadocomosalárioigualazero.
SQL> select * from emp order by empno;
EMPNO ENAME JOB MGR HIREDATE SAL
---------- ---------- --------- ---------- -------- ----------
7499 ALLEN SALESMAN 7698 20/02/81 1600
7521 WARD SALESMAN 7698 22/02/81 1250
7654 MARTIN SALESMAN 7698 28/09/81 1250
7698 BLAKE MANAGER 7839 01/05/81 2850
7782 CLARK MANAGER 7839 09/06/81 2450
7839 KING PRESIDENT 17/11/81 5000
7844 TURNER SALESMAN 7698 08/09/81 1500
7900 JAMES CLERK 7698 03/12/81 950
7934 MILLER CLERK 7782 23/01/82 1300
7935 PAUL SALESMAN 7698 15/03/80 1000
8001 SILVESTER MANAGER 7839 1000
8002 ANGELINA MANAGER 7839 20/10/11
COMM DEPTNO
---------- ----------
306 30
510 30
1428 30
285 30
245 10
500 10
150 30
95 30
130 10
100 30
80
20
71

## Página 83

7.1. Exceçõespredefinidas CasadoCódigo
12 linhas selecionadas.
SQL>
Podemosagravarasituaç ãocolocandoacoluna SALcomo not null,
paraquesurjaumerronomomentodainser çãodoregistro.
SQL> alter table emp modify sal number(7,2) not null;
Tabela alterada.
SQL> desc emp
Nome Nulo? Tipo
------------------------------------- -------- -----------------
EMPNO NOT NULL NUMBER(4 )
ENAME VARCHAR2(10)
JOB VARCHAR2(9)
MGR NUMBER(4)
HIREDATE DATE
SAL NOT NULL NUMBER(7,2)
COMM NUMBER(7,2)
DEPTNO NUMBER(2)
PC_COM_SAL NUMBER
SQL>
Vamosexcluiroregistroexistenteeexecutaroprogramanovamente.
SQL> delete from emp where empno = 8002;
1 linha deletada.
SQL> commit;
Validação completa.
SQL>
SQL> declare
2 wsal number ;
72

## Página 84

CasadoCódigo Capítulo7. Exceções
3 wdeptno number;
4 begin
5 --
6 begin
7 select avg(sal), deptno
8 into wsal, wdeptno
9 from emp
10 where deptno = 99
11 group by deptno;
12 exception
13 when no_data_found then
14 dbms_output.put_line(
'Valores não encontrados para o departamento 99.');
15 when others then
16 dbms_output.put_line('Erro ao selecionar valores
referentes ao depto. 99. '||
17 'Erro: '||sqlerrm||'.' );
18 end;
19 --
20 begin
21 insert into emp (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
22 values (8002, 'ANGELINA', 'MANAGER', 7839,
TO_DATE('20/10/2011','DD/MM/RRRR'),
wsal, null, 20);
23 --
24 commit;
25 --
26 exception
27 when others then
28 dbms_output.put_line(
'Erro ao inserir um novo empregado. '||
29 'Erro: '||sqlerrm||'.' );
30 end;
31 --
32 dbms_output.put_line(
'Empregado ANGELINA inserido com sucesso.');
33 --
34 exception
73

## Página 85

7.1. Exceçõespredefinidas CasadoCódigo
35 when no_data_found then
36 dbms_output.put_line('Empregado não encontrado.');
37 when too_many_rows then
38 dbms_output.put_line(
'Erro: O código de departamento informado'||
39 ' retornou mais de um registro.');
40 when others then
41 dbms_output.put_line(
'Erro ao inserir empregado. Erro: '||sqlerrm
42 ||' - Código: ('||sqlcode||').');
43 end;
44 /
Valores não encontrados para o departamento 99.
Erro ao inserir um novo empregado. Erro: ORA-01400: não é
possível inserir NULL em ("TSQL"."EMP"."SAL").
Empregado ANGELINA inserido com sucesso.
Procedimento PL/SQL concluído com sucesso.
SQL>
Vejaqueoprogramanosdeuváriasmensagens.Aprimeirainformaque
nãoconseguiurecuperarosalárioreferenteaodepartamentoencontrado.A
segundanosalertaqueoempregadonãopodeserinseridopelofatodeum
erroterocorrido. Notequeusamosaexce ção otherscomasvariáveisde
erro,quenosapontouquenãoépossívelinserirvaloresnulosparaocampo
SALdatabelaEMP.Issoaconteceudevidoàalteraç ãoquerealizamos. En-
tretanto,vejaqueamensagemnosinformandoqueoempregadofoiinserido
comsucessotambémémostrada.Issoéumerro,poisnaverdadeelenãofoi
inserido.Nestecaso,temosquetratarestassituaçõesnoprogramaparaqueas
açõesemensagensestejamcondizentescomquerealmenteestáacontecendo.
Senóspartimosdopressupostodequenenhumdosempregadospudesse
serincluídosemumvalordesaláriodefinido,teríamosquealteraropro-
gramaparaqueelenãoincluísseoempregadocasonãoconseguisserecuperar
osalário.Poisbem,semalteraraestruturadonossoprogramavamosutilizar
umrecursodaPL/SQLquepermitepararaexecuç ãodoprogramaquando
fornecessário.
74

## Página 86

CasadoCódigo Capítulo7. Exceções
Quandodesejarmosqueumprogramaouprocessosejainterrompido
apósumaexce ção,utilizamosachamada raise_applications_error.
Estachamadafazcomqueoprogramaparesuaexecuç ãoapartirdeumde-
terminadoponto.Emcontrapartida,eladesviaoprogramaparaoprimeiro
tratamentodeerroexistente,queseencaixecomoerroocorrido,seguindoa
hierarquiadosblocos.Nogeral,estedesviosempreéinterceptadopelaexce-
ção others.
Estachamadarequerdoisparâmetros,umcódigodeerroeumadescri-
ção. Comojáfoidito,aOraclemantémumapadronizaç ãodecódigosde
errosparaqueomesmoerrosejaidentificadoemqualquerbancodedados,
emqualquerversãoouidioma,sejaaquioudooutroladodomundo.Logo,
estescódigosnãopodemserusadospelosdesenvolvedoresparacustomizar
erros.Emcontrapartidaeladisponibilizaumafaixadecódigoquevaiapartir
donúmero-20000até-20999,paraqueutilizemosnestescasos. Seriauma
faixadecódigosdeerroscustomizável. Adescriç ãodoerroficapornossa
conta.Vamostestaraalteraç ãodoprograma.
SQL> declare
2 wsal number;
3 wdeptno number;
4 begin
5 --
6 begin
7 select avg(sal), deptno
8 into wsal, wdeptno
9 from emp
10 where deptno = 99
11 group by deptno;
12 exception
13 when no_data_found then
14 raise_application_error(-20000,
'Valores não encontrados para o departamento 99.');
15 when others then
16 dbms_output.put_line('Erro ao selecionar valores
referentes ao depto. 99. '||
17 'Erro: '||sqlerrm||'.' );
18 end;
75

## Página 87

7.1. Exceçõespredefinidas CasadoCódigo
19 --
20 begin
21 insert into emp (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
22 values (8002, 'ANGELINA', 'MANAGER', 7839,
TO_DATE('20/10/2011','DD/MM/RRRR'),
wsal, null, 20);
23 --
24 commit;
25 --
26 exception
27 when others then
28 raise_application_error(-20000,'Erro ao inserir um
novo empregado. '||
29 'Erro: '||sqlerrm||'.');
30 end;
31 --
32 dbms_output.put_line(
'Empregado ANGELINA inserido com sucesso.');
33 --
34 exception
35 when no_data_found then
36 dbms_output.put_line('Empregado não encontrado.');
37 when too_many_rows then
38 dbms_output.put_line(
'Erro: O código de departamento informado'||
39 ' retornou mais de um registro.');
40 when others then
41 dbms_output.put_line(
'Erro ao inserir empregado. Erro: '||sqlerrm
42 ||' - Código: ('||sqlcode||').');
43 end;
44 /
Erro ao inserir empregado. Erro: ORA-20000: Valores não
encontrados para o departamento 99.
-
Código: (-20000 ).
Procedimento PL /SQL concluído com sucesso.
76

## Página 88

CasadoCódigo Capítulo7. Exceções
SQL>
Analisandooresultadodaexecuç ão,podemosperceberqueocorreuum
erronabuscapelovalordosalário,ondenãofoiencontrado.Issogerouaex-
ceção no_data_found.Atravésdotratamentodestaexce çãofoichamado
o raise_application_error,quegerouumaexce çãofazendocomo
programafossedesviadoparaotratamentodeexce çãomaisexternoaoseu
bloco,nocaso,otratamento others,localizadonalinha40nonossopro-
grama.Isso,porque,embora,existaoutrotratamento otherslogoaseguir,
noblocoreferenteao insert,elesestãoemummesmonível.Porisso,aaç ão
doprogramafoidesviadaparaotratamentomaisexterno.Comodesvio,o
programanãocontinuacomasaçõessubsequentesatingindoassimnossoob-
jetivodetratamento.
Nota:seestivermosutilizandoumaestrutura loopeumaexce çãofor
geradadentrodela,enãohavendoumaáreadetratamentodeexce ções
nestaestrutura,o loopéinterrompidoeoprogramaédesviadoparao
primeirotratamentoencontradoemumnívelmaisexterno. Casohaja
umaáreadetratamentodeexce çõesdentro loop,eelanãorequerer
aparadadosistema,o loopcontinuaránormalmenteatéalcan çaro
términoprogramado.
Agoravamosalterarocódigododepartamentoparaumexistente,para
realizarumnovoteste.
SQL> declare
2 wsal number;
3 wdeptno number;
4 begin
5 --
6 begin
7 select avg(sal), deptno
8 into wsal, wdeptno
9 from emp
10 where deptno = 10
77

## Página 89

7.1. Exceçõespredefinidas CasadoCódigo
11 group by deptno;
12 exception
13 when no_data_found then
14 raise_application_error(-20000,
'Valores não encontrados para o departamento 99.');
15 when others then
16 dbms_output.put_line('Erro ao selecionar valores
referentes ao depto. 10. '||
17 'Erro: '||sqlerrm||'.');
18 end;
19 --
20 begin
21 insert into emp (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
22 values (8002, 'ANGELINA', 'MANAGER', 7839,
TO_DATE('20/10/2011','DD/MM/RRRR'),
wsal, null, 20);
23 --
24 commit;
25 --
26 exception
27 when others then
28 raise_application_error(-20000,
'Erro ao inserir um novo empregado. '||
29 'Erro: '||sqlerrm||'.');
30 end;
31 --
32 dbms_output.put_line(
'Empregado ANGELINA inserido com sucesso.');
33 --
34 exception
35 when no_data_found then
36 dbms_output.put_line('Empregado não encontrado.');
37 when too_many_rows then
38 dbms_output.put_line(
'Erro: O código de departamento informado'||
39 ' retornou mais de um registro.');
40 when others then
41 dbms_output.put_line(
78

## Página 90

CasadoCódigo Capítulo7. Exceções
'Erro ao inserir empregado. Erro: '||sqlerrm
42 ||' - Código: ('||sqlcode||').');
43 end;
44 /
Empregado ANGELINA inserido com sucesso.
Procedimento PL/SQL concluído com sucesso.
SQL>
Comoeraoesperado, oprogramafuncionounormalmente. Pode-se
aindasimularoerroreferenteaocomando insert,atribuindo nullàva-
riávelwsalantesdainclusão.
7 .2 E xceções definidas pelo usuário
Comofoiditoanteriormente,alémdasexce çõespredefinidasexistentesno
Oracle,podemoscriarnovasexce çõesparaatenderanecessidadesmaises-
pecíficasdonossoprograma.Adiferen çaentreestestiposestánadefiniç ão
econtroledestasexce ções.Estetipo,quandoutilizadopelousuário,deveser
declaradoemanipuladopelopróprioprograma.ParaoOracle,estasexce ções
nãoexistem,porisso,todoocontroledeveserfeitopelaaplicaç ão.Vamosver
oexemploaseguir.
SQL> declare
2 wsal number;
3 werro_salario exception ;
4 begin
5 --
6 begin
7 select nvl(avg(sal),0)
8 into wsal
9 from emp
10 where deptno = 99 ;
11 --
12 if wsal = 0 then
13 --
14 raise werro_salario;
79

## Página 91

7.2. Exceçõesdefinidaspelousuário CasadoCódigo
15 --
16 end if;
17 --
18 exception
19 when others then
20 raise_application_error(-20000,
'Erro ao selecionar valores referentes ao depto.
99. '||
21 'Erro: '||sqlerrm||'.');
22 end;
23 --
24 begin
25 insert into emp (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
26 values (8002, 'ANGELINA', 'MANAGER', 7839,
TO_DATE('20/10/2011','DD/MM/RRRR'),
wsal, null, 20);
27 --
28 commit;
29 --
30 exception
31 when others then
32 raise_application_error(-20000,
'Erro ao inserir um novo empregado. '||
33 'Erro: '||sqlerrm||'.');
34 end;
35 --
36 dbms_output.put_line(
'Empregado ANGELINA inserido com sucesso.');
37 --
38 exception
39 when no_data_found then
40 dbms_output.put_line('Empregado não encontrado.');
41 when too_many_rows then
42 dbms_output.put_line(
'Erro: O código de departamento informado'||
43 ' retornou mais de um registro.');
44 when others then
45 dbms_output.put_line(
80

## Página 92

CasadoCódigo Capítulo7. Exceções
'Erro ao inserir empregado. Erro: '||sqlerrm
46 ||' - Código: ('||sqlcode||').');
47 end;
48 /
Erro ao inserir empregado. Erro: ORA-20000: Erro ao selecionar
valores referentes ao depto.
99.
Erro: User-Defined exception. - Código: (-20000).
Procedimento PL/SQL concluído com sucesso.
SQL>
Vamosentenderoexemplo.Primeiramente,precisamosdefinirumnome
paraaexce çãoedeclará-lanaáreadedeclaraç ãodevariáveis. Noexemplo,
chamamosnossaexce çãode werro_salario. Quandodeclaramosuma
variáveldotipoexce çãoutilizamosotipo exception.Feitoisto,jápode-
mosutilizá-laemnossoprograma. Modificamosoprogramautilizadonos
exemplosanteriores,justamenteparamostrarformasdiferentesdetrataros
mesmosproblemas.Modificamoso selectquebuscaosalárioparaqueele
nãogereaexce çãonativadoOracle.
Sabemosqueousodefun çõesdeagrupamento,como sum, min, max,
avgetc.,nãogeramexce çõesmesmonãoatendendoàcláusula where.Com
isso,aexce ção no_data_foundnãoégerada.Contudo,pararealizarocon-
troleenãopermitirquevaloresnulosouzeradossejamcadastradosnocampo
salário,nósutilizamosumaestrutura ifparatestaroresultadovindodo
select,edependendocomofor,acionarounãoaexce çãoquedefinimos.
Nossotesteébemsimples,verificamosseovaloréigualoudiferentede
zero. Casosejaigualazerochamamosnossaexce çãoatravésdocomando
raise. Estecomandoacionanossaexce çãoefazcomqueaaç ãodopro-
gramasejadesviadaparaaáreadetratamentodeerrosdentrodahierarquia
deníveis,ouseja,apartirdaíasregrasesequênciassãoasmesmasutilizadas
nasexce çõespredefinidas.
Uma observação importante. Se houver comandos após a chamada
raise,elesnuncaserãoexecutados. Portanto,fiqueatentoquantoaisto.
Notetambémqueduasmensagensdeerroforamgeradas,inclusive,umaque
81

## Página 93

7.2. Exceçõesdefinidaspelousuário CasadoCódigo
dizqueaexce çãogeradafoiumaexce çãodefinidapelousuário: User-Defined
exception.Aindapodemosmelhorarestamensageminibindooscódigosde
erroefazendocomqueapare çaapenasumamensagem.Vejaaseguir.
SQL> declare
2 wsal number;
3 werro_salario exception ;
4 begin
5 --
6 begin
7 select nvl(avg(sal),0)
8 into wsal
9 from emp
10 where deptno = 99;
11 --
12 if wsal = 0 then
13 --
14 raise werro_salario;
15 --
16 end if;
17 --
18 exception
19 when werro_salario then
20 raise werro_salario;
21 when others then
22 raise_application_error(-20000,'Erro ao selecionar
valores referentes ao depto. 99. '||
23 'Erro: '||sqlerrm||'.');
24 end;
25 --
26 begin
27 insert into emp (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
28 values (8002, 'ANGELINA', 'MANAGER', 7839,
TO_DATE('20/10/2011','DD/MM/RRRR'),
wsal, null, 20);
29 --
30 commit;
31 --
82

## Página 94

CasadoCódigo Capítulo7. Exceções
32 exception
33 when others then
34 raise_application_error(-20000,
'Erro ao inserir um novo empregado. '||
35 'Erro: '||sqlerrm||'.');
36 end;
37 --
38 dbms_output.put_line(
'Empregado ANGELINA inserido com sucesso.');
39 --
40 exception
41 when werro_salario then
42 dbms_output.put_line(
'O salário necessita ser maior que zero.');
43 when no_data_found then
44 dbms_output.put_line('Empregado não encontrado.');
45 when too_many_rows then
46 dbms_output.put_line(
'Erro: O código de departamento informado'||
47 ' retornou mais de um registro.');
48 when others then
49 dbms_output.put_line(
'Erro ao inserir empregado. Erro: '||sqlerrm
50 ||' - Código: ('||sqlcode||').');
51 end;
52 /
O salário necessita ser maior que zero.
Procedimento PL/SQL concluído com sucesso.
SQL>
Comisso,finalizamosapartesobreexce ções. Vimosqueatravésdelas
épossívelrealizartodosostratamentosdeerrosdeumaformaorganizada
esemprejudicarofuncionamentodosistema.Outrofatorquedeveserco-
mentadoéqueasexce çõesnãoservemapenasparageraç ãodemensagensde
erro.Dentrodasáreasdetratamentopodemosusarchamadasa functions,
proceduresou packagesparasolucionarproblemassemainterven çãoou
83

## Página 95

7.2. Exceçõesdefinidaspelousuário CasadoCódigo
atémesmosemconhecimentodousuário.
84

## Página 96

Capítulo8
Estruturasdecondiç ão:if
Asestruturasdecondiç ãosãoutilizadasquandoprecisamosalterarofluxode
caminhodeumprograma.Atravésdestetipodeestruturaconseguimoscriar
condiçõesquepodemlevaroprogramaaexecutartarefasdiferentesdepen-
dendodecadasituaç ão. Portanto,utilizamosadeclaraç ão ifparaavaliar
umaoumaiscondições,executandoounãodeterminadaslinhasdeinstru-
ções.
NoPL/SQLutilizamosocomando if(se)paramontarestascondições.
Podemostercondiçõessimples,comumacondiç ãoapenas,atéousodecon-
diçõesaninhadasondepodemostercomandos ifdentrodeoutroscoman-
dos if,emumamesmaestrutura.
Juntamentecomocomando iftemosocomando else(senão),que
éutilizadoparadirecionaroprogramaparaoutroscaminhoscasoo ifnão
satisfaçaacondiç ãodesejada.Dentrodaestruturadeumcomando ifpo-
demosterdesdeum elseatévárioselses( elsif),seguindosuasintaxe.

## Página 97

8.1. Estruturasdocomandoif-endif CasadoCódigo
Oquedeveficarclaroéqueestaestruturageraumresultadomedianteuma
condiçãoquesatisfaç aocritérioimposto.
Nomais,podemosdizerqueserácomumacharestetipodeestruturaden-
trodosprogramas.Portanto,vocêvaiutilizá-lacomfrequência,poiscomona
grandemaioriadasvezesescrevemoscódigosquerefletemeabstraemsitua-
çõesdodiaadia,precisamostestar nvariáveisparafazercomqueoprograma
chegueaoobjetivopropostoemcadasituaç ão.
8.1 E struturas do comando if-end if
SQL> begin
2 --
3 if <condicao> then
4 <instruções>
5 end if;
6 end;
7
SQL>
Nesta estrutura, temos apenas uma condição. Caso o resultado de
<condicao>(linha3)sejaverdadeiro,eleestarásatisfazendoacondiç ãoe
executaráoscomandosqueestiveremdentrodoescopodo if.Casocontrá-
rio,não.O end if indicaofimdocomando if.Vejaasexecuçõesaseguir,
ondeoprogramaéexecutadoduasvezes,mascomdiferentesvalores:
SQL> declare
2 x number := 10;
3 res number;
4 begin
5 res := mod(x,2);
6 if res = 0 then
7 dbms_output.put_line('O resto da divisão é zero!');
8 end if;
9 --
10 dbms_output.put_line('Resultado do cálculo: '||res);
11 end;
12 /
86

## Página 98

CasadoCódigo Capítulo8. Estruturasdecondição:if
O resto da divisão é zero!
Resultado do cálculo: 0
Procedimento PL/SQL concluído com sucesso.
SQL>
SQL> declare
2 x number := 7;
3 res number;
4 begin
5 res := mod(x,2);
6 if res = 0 then
7 dbms_output.put_line('O resto da divisão é zero!');
8 end if;
9 --
10 dbms_output.put_line('Resultado do cálculo: '||res);
11 end;
12 /
Resultado do cálculo: 1
Procedimento PL/SQL concluído com sucesso.
SQL>
8.2 E struturas do comando if-else-end if
SQL> begin
2 --
3 if <condicao> then
4 <instruções>
5 else
6 <instruções>
7 end if;
8 end;
9
SQL>
Estaestruturaéformadaporum ifeum else.Casoacondiç ãodo if
87

## Página 99

8.2. Estruturasdocomandoif-else-endif CasadoCódigo
nãosejaatendidaofluxoserádesviadoparao else.Notequeo elsenão
fazrestriçãoouchecagemdecondiç ão.Emviasgeraisocomandoquerdizer:
seacondiç ãoforverdadeirafaç aisso,senãofaç aaquilo.
Vamosveromesmoexemplo,agoracomduascondições, ife else,
ondedependendodoresultadopode-sedeterminarqualfluxooprograma
devepercorrer.
SQL> declare
2 x number := 10;
3 res number;
4 begin
5 res := mod(x,2);
6 if res = 0 then
7 dbms_output.put_line('O resto da divisão é zero!');
8 else
9 dbms_output.put_line('O resto da divisão não é zero!');
10 end if;
11 --
12 dbms_output.put_line('Resultado do cálculo: '||res);
13 end;
14 /
O resto da divisão é zero!
Resultado do cálculo: 0
Procedimento PL /SQL concluído com sucesso.
SQL> declare
2 x number := 7;
3 res number;
4 begin
5 res := mod(x,2);
6 if res = 0 then
7 dbms_output.put_line('O resto da divisão é zero!');
8 else
9 dbms_output.put_line('O resto da divisão não é zero!');
10 end if;
11 --
12 dbms_output.put_line('Resultado do cálculo: '||res);
13 end;
88

## Página 100

CasadoCódigo Capítulo8. Estruturasdecondição:if
14 /
O resto da divisão não é zero!
Resultado do cálculo: 1
Procedimento PL/SQL concluído com sucesso.
SQL>
8.3 E struturas do comando if-elsif(-else)-end
if
SQL> begin
2 --
3 if <condicao> then
4 <instruções>
5 elsif <condicao> then
6 <instruções>
7 end if;
8 end;
9
SQL>
SQL> begin
2 --
3 if <condicao> then
4 <instruções>
5 elsif <condicao> then
6 <instruções>
7 else
8 <instruções>
9 end if;
10 end;
11
SQL>
Estaestruturapermitetestarmaisdeumacondiç ãodentrodeumaes-
trutura if.Alémdo ife elsepodemostero elsif.Podemosteruma
89

## Página 101

8.3. Estruturasdocomandoif-elsif(-else)-endif CasadoCódigo
estrutura ifcomvários elsif,dependendodanecessidadeequantidade
decondiçõesqueprecisarmostestar.Aseguir,umexemplo:
Entrandonaprimeiracondiç ão:
SQL> declare
2 x number := 10;
3 res number;
4 begin
5 res := mod(x,5);
6 if res = 0 then
7 dbms_output.put_line('O resto da divisão é zero!');
8 elsif res > 0 then
9 dbms_output.put_line('O resto da divisão não é zero!');
10 else
11 dbms_output.put_line( 'O resto da divisão é menor zero!');
12 end if;
13 --
14 dbms_output.put_line('Resultado do cálculo: '||res);
15 end;
16 /
O resto da divisão é zero!
Resultado do cálculo: 0
Procedimento PL /SQL concluído com sucesso.
SQL>
Entrandonasegundacondiç ão:
SQL> declare
2 x number := 11;
3 res number;
4 begin
5 res := mod(x,5);
6 if res = 0 then
7 dbms_output.put_line('O resto da divisão é zero!');
8 elsif res > 0 then
9 dbms_output.put_line('O resto da divisão não é zero!');
10 else
90

## Página 102

CasadoCódigo Capítulo8. Estruturasdecondição:if
11 dbms_output.put_line('O resto da divisão é menor zero!');
12 end if;
13 --
14 dbms_output.put_line('Resultado do cálculo: '||res);
15 end;
16 /
O resto da divisão não é zero!
Resultado do cálculo: 1
Procedimento PL/SQL concluído com sucesso.
SQL>
Entrandonaterceiracondiç ão:
SQL> declare
2 x number := -6;
3 res number;
4 begin
5 res := mod(x,5);
6 if res = 0 then
7 dbms_output.put_line('O resto da divisão é zero!');
8 elsif res > 0 then
9 dbms_output.put_line('O resto da divisão não é zero!');
10 else
11 dbms_output.put_line( 'O resto da divisão é menor zero!');
12 end if;
13 --
14 dbms_output.put_line('Resultado do cálculo: '||res);
15 end;
16 /
O resto da divisão é menor zero!
Resultado do cálculo: -1
Procedimento PL/SQL concluído com sucesso.
SQL>
Vimosqueaestruturadecondiç ãonosdáváriaspossibilidadesparafazer
comqueosprogramastomemrumosdiferentesparacadasituaç ão.Também
91

## Página 103

8.3. Estruturasdocomandoif-elsif(-else)-endif CasadoCódigo
foimencionadoanteriormentequeépossívelmontarestruturas ifaninha-
das,ouseja,umaestrutura ifdentrodeoutraestrutura if,porexemplo.
Portanto,pode-seusarumaninhamentodedeclarações if,quandosetema
necessidadedefiltrarumasériededados.Mastomecuidado,poismuitosní-
veisdedeclarações ifpodemcausarproblemasnomomentodadepuraç ão
doprograma.Onúmeromáximodeníveisdedeclarações ifrecomendado
sãoquatro.Vejaaseguiroexemplodasintaxededeclaraçõesaninhadas if:
SQL> begin
2 if <condição> then
3 if <condição> then
4 <instruções>
5 else
6 <instruções>
7 if <condição> then
8 <instruções>
9 else
10 <instruções>
11 end if;
12 end if;
13 end if;
14 end;
15
SQL>
Vamosveroexemplo:
SQL> declare
2 x1 number := 10;
3 x2 number := 5;
4 op varchar2(1) := '+';
5 res number;
6 begin
7 if (x1 + x2) = 0 then
8 dbms_output.put_line('Resultado: 0');
9 elsif op = '*' then
10 res := x1 * x2;
11 elsif op = '/' then
92

## Página 104

CasadoCódigo Capítulo8. Estruturasdecondição:if
12 if x2 = 0 then
13 dbms_output.put_line('Erro de divisão por zero!');
14 else
15 res := x1 / x2;
16 end if;
17 elsif op = '-' then
18 res := x1 - x2;
19 if res = 0 then
20 dbms_output.put_line('Resultado igual a zero!');
21 elsif res < 0 then
22 dbms_output.put_line('Resultado menor que zero!');
23 elsif res > 0 then
24 dbms_output.put_line('Resultado maiorl a zero!');
25 end if;
26 elsif op = '+' then
27 res := x1 + x2;
28 else
29 dbms_output.put_line('Operador inválido!');
30 end if;
31 dbms_output.put_line('Resultado do cálculo: '||res);
32 end;
33 /
Resultado do cálculo: 15
Procedimento PL/SQL concluído com sucesso.
SQL>
8.4 F ormatando as declarações if
Paraqueocódigoquecontenhaadeclaraç ão iffiquemaislegívelemais
fácildeentender,énecessáriooempregodealgumasregrasdealinhamento
taiscomo:
• Usando-seváriasdeclaraçõesif,recua-seapróximadeclaraç ão if
algunsespaçosparadentro;
• Oscomentáriosdevemficarapósadeclaração end if;
• Osblocosdedeclaraçõesdevemficarrecuadosalgunsespaçospara
dentro,contandoapartirdadeclaraç ão if;
93

## Página 105

8.5. Evitandoerroscomunsnousodeif CasadoCódigo
• Seumacondiçãoformuitograndeemudardelinha,recua-seestalinha
algunsespaçosparadentro;
• Deve-secolocaroelsesempreabaixodadeclaraç ão ifaoqualeleé
correspondente,assimcomoo end if domesmo;
8.5 E vitando erros comuns no uso de if
Érecomendadoquesetomemalgumasprecauçõesparaquenãoocorram
errosnasdeclarações if.Atabelaaseguirdemonstraalgunscuidadosne-
cessários:
• Verifiquesetodadeclaração iftemumadeclaraç ão end if corres-
pondente,esevocêdigitou elsifsemo eextra(como“elseif”).
• Nãofaçaloopsaninhadosmuitocomplexos.Acomplexidadedificulta
oacompanhamentoeadepuraç ãoquandoocorreremproblemasou
alterações. Avaliesualógicaparaverseumafun çãorealizaamesma
tarefa.
• Verifiquesevocêcolocouumespaçonadeclaração end if emvezde
nãousarespaçoouusarumtraço.
• Nãoseesqueçadasuapontuaç ão.Vocêprecisadepontosevírgulasde-
poisde end if edepoisdecadaumadasdeclarações,masnãodepois
dapalavra-chave then.
Nota: afun ção modtemoobjetivoderetornarorestodadivisão
entredoisnúmerospassadosporparâmetro.
Nota: caso não esteja visualizando as saída do comando
dbms_output, no SQL*Plus, execute o seguinte comando:set
serveroutput on.
94

## Página 106

Capítulo9
Comandosderepetiç ão
Oscomandosderepetiç ãosãoutilizadosparaquepossamosrepetirumade-
terminadaaçãoouaçõesdentrodeumprogramaquantasvezessejamne-
cessárias.Asrepetiçõespodemseriniciadasapartirdeumacondiç ãoesua
finalizaçãotambémdeveaconteceratravésdestecritério.EmPL/SQLtemos
basicamentetrêstiposdeestruturasderepetiç ão. Sãoelas: loop, while
loope for loop.Cadaestruturapossuicaracterísticasqueseadequamàs
maisvariadassituações,conformeasnecessidadesdecadadesenvolvimento.
Vamosconheceroscomandosquefazempartedestasestruturas:
9.1 for loop
Usa-seo for loop pararepetirdiversasvezesomesmoblocodecódigo,
atéqueacondiçãopredefinidasejaatendidaeimpe çaaexecuçãodolooping.
Vejaaseguirumexemplode looping for:

## Página 107

9.1. forloop CasadoCódigo
SQL> begin
2 for i in 1 ..10 loop
3 --
4 dbms_output.put_line('5 X '||i||' = '|| (5*i));
5 --
6 end loop;
7 end;
8 /
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
Procedimento PL /SQL concluído com sucesso.
SQL>
Nota:casonãoestejaconseguindovisualizarresultadonatelaexecuteo
comando:
SQL>
SQL> set serveroutput on
SQL>
Esteprogramaimprimenatelaatabuadadecinco.Criamosumaestru-
tura for loop querepetiráoblocoPL/SQLdezvezes,come çandopor1.
Cadavezqueumavoltaacontece,avariável i,quenestecasonãonecessitou
serdeclarada,poiso for loop adeclaradentrodoseuescopo,éincremen-
tada.Quandoestavariávelchegara10,oblocoPL/SQLseráexecutadouma
últimavezeentãoocomandoéfinalizado.Notequeutilizamosavariável i
comobaseparanossocálculo,eassimmontamosasaídaproposta.
Juntamentecomocomando forpodemosutilizarocomando REVERSE.
Estecomandofazcomqueacontagemaconte çadeformacontrária. Neste
96

## Página 108

CasadoCódigo Capítulo9. Comandosderepetição
exemplo, ireceberá 10 inicialmente, e será decrementado a cada volta.
Quando ichegara1,oblocoPL/SQLseráexecutadoumaúltimavezeo
comandoéfinalizado.Vejaoexemplo:
SQL> begin
2 for i in REVERSE 1..10 loop
3 --
4 dbms_output.put_line('5 X '||i||' = '||(5*i));
5 --
6 end loop;
7 end;
8 /
5 X 10 = 50
5 X 9 = 45
5 X 8 = 40
5 X 7 = 35
5 X 6 = 30
5 X 5 = 25
5 X 4 = 20
5 X 3 = 15
5 X 2 = 10
5 X 1 = 5
Procedimento PL/SQL concluído com sucesso.
SQL>
O loop for tambémpodeserexecutadoaninhadamente. Quandose
aninhaos loops for,o loopexternoéexecutadoprimeiroeposterior-
menteosinternos.
SQL> begin
2 for x in 5 ..6 loop
3 --
4 dbms_output.put_line('Tabuada de '||x);
5 dbms_output.put_line(' ');
6 --
7 for y in 1..10 loop
8 --
97

## Página 109

9.1. forloop CasadoCódigo
9 dbms_output.put_line(x||' X '||y||' = '||(x*y));
10 --
11 end loop;
12 --
13 dbms_output.put_line(' ');
14 --
15 end loop;
16 end;
17 /
Tabuada de 5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
Tabuada de 6
6 X 1 = 6
6 X 2 = 12
6 X 3 = 18
6 X 4 = 24
6 X 5 = 30
6 X 6 = 36
6 X 7 = 42
6 X 8 = 48
6 X 9 = 54
6 X 10 = 60
Procedimento PL /SQL concluído com sucesso.
SQL>
Nesteexemplo,utilizamosos for loops aninhadosparamostrarna
telaoscálculosdastabuadasde5e6. Pode-seutilizaroincrementodeum
loopcomopartedalógicadeumprograma,fazendocomquedeterminadas
98

## Página 110

CasadoCódigo Capítulo9. Comandosderepetição
açõessósejamexecutadastendocomobaseestainformaç ão.Vejaoexemplo
aseguir.
SQL> begin
2 for x in 1 ..15 loop
3 --
4 if mod(x,2) = 0 then
5 dbms_output.put_line('Número divisível por 2: '||x);
6 end if;
7 --
8 end loop;
9 end;
10 /
Número divisível por 2: 2
Número divisível por 2: 4
Número divisível por 2: 6
Número divisível por 2: 8
Número divisível por 2: 10
Número divisível por 2: 12
Número divisível por 2: 14
Procedimento PL/SQL concluído com sucesso.
SQL>
Aquiutilizamosumarepetiç ãoondeoblocoPL/SQLseráexecutado15
vezes.Contudo,aimpressãoemtelaserárealizadaapenasseoscritériosdo
comando ifforemverdadeiros.Nesteexemplo,estamossolicitandoqueo
programaimprimaemtelasomenteosnúmerosdivisíveispor2. Noteque
estamosutilizandoavariáveldeincremento(nestecaso,X)comoparteda
nossalógica.
Outraop çãointeressantenousodo for loop éapossibilidadedesubs-
tituirosnúmerosfixosdointervaloporvariáveis. Vejaomesmoexemplo
utilizandovariáveisparadefinirointervalo.
SQL> declare
2 inter1 number default 1;
3 inter2 number default 15;
99

## Página 111

9.1. forloop CasadoCódigo
4 begin
5 for x in inter1..inter2 loop
6 --
7 if mod(x, 2) = 0 then
8 dbms_output.put_line('Número divisível por 2: '||x);
9 end if;
10 --
11 end loop;
12 end;
13 /
Número divisível por 2 : 2
Número divisível por 2 : 4
Número divisível por 2 : 6
Número divisível por 2 : 8
Número divisível por 2 : 10
Número divisível por 2 : 12
Número divisível por 2 : 14
Procedimento PL /SQL concluído com sucesso.
SQL>
Cuidados ao utilizar o comando for loop
• Nãoseesquecerdecolocarumespaçoem end loop;
• Nãoseesquecerdopontoevírguladepoisde end loop;
• Nãoinserirocontadordomaisaltoparaomaisbaixoaousar reserve
oudefinirointervalodomaisaltoparaomaisbaixoeseesquecerde
usar reserve;
• Nãodefinirasvariáveisdeum loopdemodoqueolimiteinferior
tenhaumvalormaiordoqueolimitesuperior;
• Nãopermitirqueasvariáveisdoslimitesacabememvalores null;
• Aoaninharosloops,verifiqueseasdeclaraçõesseguemalógicapre-
tendida.
100

## Página 112

CasadoCódigo Capítulo9. Comandosderepetição
9.2 while loop
while loop éusadoparaavaliarumacondiç ãoantesdeumasequênciade
códigossejaexecutado.Adiferen çaentreo loop while eo loop for,é
queo loop while permiteaexecuç ãodecódigoapenasseacondiç ãofor
verdadeira,eo loop for fazcomqueocódigosejaexecutadopelomenos
umavez,independentedacondiç ão. Vejaaseguirumexemplodo loop
while:
SQL> declare
2 x number default 0;
3 label_vert varchar2(240 ) default '&label';
4 tam_label number default 0;
5 begin
6 --
7 tam_label := length(label_vert);
8 --
9 while (x < tam_label) loop
10 --
11 x := x + 1;
12 --
13 dbms_output.put_line(substr(label_vert,x,1));
14 --
15 end loop;
16 end;
17 /
Informe o valor para label: CURSO PLSQL
antigo 3: label_vert varchar2(240) default '&label';
novo 3: label_vert varchar2(240) default 'CURSO PLSQL';
C
U
R
S
O
P
L
S
Q
L
101

## Página 113

9.3. loop CasadoCódigo
Procedimento PL /SQL concluído com sucesso.
SQL>
Notequenesteexemplonãotemosumnúmerodeterminadoderepe-
tições. Onúmerovaidependerdotamanhodastringinformadaatravésda
variávellabel.Esteprogramaimprimenatelaemverticalumastringinfor-
madaviaparâmetro.Alógicafoiescritadeformaqueasrepetiçõesocorram
conformeaquantidadedecaracteresexistentedentrodavariável.Ocontrole
érealizadopelaexistênciadacondiçãocontidanocomando while.
9.3 loop
O loopéocomandoderepetiç ãomaissimplesefácildeentender.Seuob-
jetivoéigualaosdosdemaiscomandosderepetiç ão.Entretanto,possuica-
racterísticasdiferentesdefuncionamento. Nestecomandonãoépermitido
definirumintervaloderepetiç ão,muitomenosumacondiç ãoqueofaç aini-
ciarepararsuaexecuç ão. Emtese,seufuncionamentoéinfinito,poisao
entraremumaestruturacomoestanãohácomosair. Porisso,juntamente
comeleutilizamosocomando exit.Estecomandoéquemvaideterminar
afinalizaçãodasrepetições,impedindoqueoprogramaentreemumloop
eterno.
Declarações exit e exit when
Quandoumadeclaraç ão exitéencontrada,o loopéimediatamente
encerradoeocontroleépassadoparaadeclaraç ãoseguinte. Adeclaração
exit when permitequevocêespecifiqueacondiç ãorequeridaparasairda
execuçãodo loop. Seoresultadodacondiç ãoforverdadeiro,o loopé
encerrado,eseoresultadoforfalso,oloopingcontinua.
Aousar exitou exit when coloquesempreessescomandosnoiní-
cioounofinaldobloco loop. Dessaformavocêpodeevitarmuitoserros
lógicos.
Seguemexemplosdelooputilizando exite exit when:
102

## Página 114

CasadoCódigo Capítulo9. Comandosderepetição
Noexemploaseguirutilizamosaestrutura ifparacriarumacondiç ão
quepossadeterminarafinalizaç ãodocomando.Casoacondiç ãocontidano
ifsejaverdadeira,chamamosocomando exitparafinalizarasequência
derepetições.Casocontrário,ocomandocontinuasuaexecuç ão.
SQL> declare
2 x number default 0;
3 label_vert varchar2(240 ) default '&label';
4 tam_label number default 0;
5 begin
6 --
7 tam_label := length(label_vert);
8 --
9 loop
10 --
11 x := x + 1;
12 --
13 dbms_output.put_line(substr(label_vert,x,1));
14 --
15 if x = tam_label then
16 exit;
17 end if;
18 --
19 end loop;
20 end;
21 /
Informe o valor para label: ORACLE PLSQL
antigo 3: label_vert varchar2(240) default '&label';
novo 3: label_vert varchar2(240) default 'ORACLE PLSQL';
O
R
A
C
L
E
P
L
S
Q
103

## Página 115

9.3. loop CasadoCódigo
L
Procedimento PL /SQL concluído com sucesso.
SQL>
Jánoexemploaseguirutilizamos exit when,quenospermiteincluir
umacondiçãoquepossafinalizarocomando.Notequecomissonãoprecisa-
mosutilizarestruturasauxiliares,comoo if,comofoiutilizadonoexemplo
anterior.
SQL> declare
2 x number default 0;
3 label_vert varchar2(240 ) default '&label';
4 tam_label number default 0;
5 begin
6 --
7 tam_label := length(label_vert);
8 --
9 loop
10 --
11 x := x + 1;
12 --
13 dbms_output.put_line(substr(label_vert,x,1));
14 --
15 exit when x = tam_label;
16 --
17 end loop;
18 end;
19 /
Informe o valor para label: CURSO PLSQL
antigo 3: label_vert varchar2(240) default '&label';
novo 3: label_vert varchar2(240) default 'CURSO PLSQL';
C
U
R
S
O
P
104

## Página 116

CasadoCódigo Capítulo9. Comandosderepetição
L
S
Q
L
Procedimento PL/SQL concluído com sucesso.
SQL>
Emoutraslinguagensdeprogramaç ãoécomumencontrarocomando
repeat until (repitaaté).NaPL/SQLnãoexisteestecomando.Contudo,
utilizamososcomandos loope exit when parasanarestanecessidade.
9.4 Q ual loop deve-se usar?
Conformevistoatéaqui,temosdisponíveistrêsop çõesdeloops.Mascomo
saberseestamosfazendousodotipocorretodeloopparadeterminadasitu-
ação?Atabelaaseguirajudaaesclarecerestadúvida.
•for:usesempreoloopforsevocêsouberespecificamentequantasvezes
oloopdeveserexecutado.Setiverdecodificarumadeclaraç ão exit
ou exit when emum loop for,vocêpodereconsiderarseucódigo
eusarumloopouumaabordagemdiferente.
•while:useesteloopquandonãohácertezaseeleseráexecutado.Em-
borasejapossívelconseguiresseresultadoemum loop for usando
exitou exit when,essasituaç ãoémaisadequadaparao loop
while.O loop while éoloopmaisusadoporqueelefornecemais
flexibilidade.
•loop: vocêpodeusaroloopsimplessequisercriarumloopdotipo
repeat until.Oloopsimpleséperfeitoparaexecutaressatarefa.
Orientações sobre os loopS
Alistaaseguirapresentaráalgumasorientaçõessobreosloops.
105

## Página 117

9.4. Qualloopdeve-seusar? CasadoCódigo
• Verifiqueaousarumloopcomumadeclaração exitou exit when
seacondiç ãoseráatendidapelomenosumavez;casocontrário,você
teráumloopinfinito.
• Nuncacrieumloopinfinito.
• Usesempreosnomesderótulosnosloops.Issotornaocódigomuito
maisfácildeacompanhar,alémdelhedarflexibilidade.
• Nãouseumadeclaração returndentrodeumloopaousarosloops
emumafun ção. Emboraissofuncione,essaéumapráticaruimde
programaçãoquetemalgunsresultadosindesejados,eéomodoerrado
deencerrarumloop.
• Useexit when emvezde exit. exit when émuitomaisfácilde
acompanharerequermenoscódigo.
• Verifiqueseapontuaçãodosseusloopsestáadequada. Selecioneo
tipodeloopquevaiusarcomosincrementos. Vocêpodelidarcom
qualquertipodeincrementoemqualquerloop.
• Crievariáveisdelimitesuperioreinferiornosloopsforseumdosli-
mitespuderseralteradonofuturo. Vocêpodeatribuiresseslimites
imediatamenteaoseucódigo.Naverdade,muitoprovavelmentevocê
nemteráumlimitefixo,demodoquevocêdeveseguiresteconselho
automaticamente.
106

## Página 118

Capítulo10
Cursores
OcursoréumcomandodoPL/SQLquepermiteaconstruç ãodeumaestru-
turaderepetiç ão,ouseja,pode-sevarrerumatabela,linhaporlinha,coluna
porcolunaatravésdautilizaçãodestecomando,eassim,podemosmanipular
todososdadosdeumadeterminadatabela.
Ocursordeveserdeclaradonoiníciodobloco,ondeseráutilizado.De-
poisdedeclará-lo,eledevesercriadodentrodamesmaestrutura.Asinfor-
maçõescontidasnocursorsãobaseadasnosdadospelosquaissuaestrutura
foidefinida.Porexemplo,sedefinirmosumcursorcombasenatabeladeem-
pregados,serácomosdadosreferentesaosempregadosdestatabelaemque
vamostrabalharquandoestivermosmanipulandotalcursor.Portanto,osre-
tornosdosdadosapresentadospelocursorprovemdecomandos selects
feitosemdeterminadastabelasequetrazemdadosdelinhasecolunasespe-
cíficas.
ExistemdoistiposdecursoresnoPL/SQL,osexplícitoseosimplícitos.O

## Página 119

10.1. Cursoresexplícitos CasadoCódigo
cursorexplícitoéoquedefinimosnosprogramas,eoimplícito,comoonome
jádizédeclaradoimplicitamentepeloOracle,ouseja,quandousadoocursor
explícito,odesenvolvedor,nocasoquemestáescrevendoaaplicaç ão,alémde
declará-lodeveinserircomandosqueespecifiquemasuainicializaç ãoefina-
lização,bemcomoamanipulaç ãodosdados.Quandonãoexistirumcursor
explícitoassociadoparaocomandoSQL,oOracleocriaimplicitamente.Um
exemplodistoéquandotemosumcomando updateou delete,dentro
deumaaplicaç ão.Embora,nãosejavisívelexplicitamente,oOraclecriaum
cursorparaexecutartalcomando.Oscursoresimplícitoseexplícitospodem
existirnamesmaaplicaç ãoemummesmobloco.
Nestelivrodaremosênfasenoscursoresexplícitos. Atravésdelespode-
mosatenderasituaçõesbemespecíficasnodesenvolvimentodenossospro-
gramas.Contudo,serãomostradasascaracterísticaseofuncionamentodes-
tesdoistipos.
10.1 C ursores explícitos
Parautilizarmosumcursorexplícito,algumasregrasdevemserobedecidas.
Primeiramente,temosquedeclará-lo.Fazemosistodamesmaformaquecom
asvariáveiseconstantes.Vejaaseguiralgumasformasdedeclaraç ão:
cursor c1 is
select ename
,job
from emp
where deptno = 30;
Énadeclaraç ãoquedefinimosaestruturadocursor.Estaestruturainicia
comaexpressão cursor <nome cursor> is.O <nome cursor> segue
asmesmasregrasdadefiniç ãodevariáveis.Comistoestamosdefinindooca-
beçalhodocursor,rotulando-o.Logoapósaexpressão isvemocomando
selectqueseráabasedonossocursor.Este selectpodeserescritonor-
malmentecomosefôssemosexecutá-lopeloSQL*Plus,porexemplo.Osco-
mandos selectpodemconterváriastabelasecolunas.Tambémpodeser
usadaaexpressãoasterisco *parasereferiratodasascolunasdeumaoumais
tabelas. Valeressaltarque,quandoutilizamoscursor,nãoénecessáriousar
108

## Página 120

CasadoCódigo Capítulo10. Cursores
ocomando intono select. Tambémpodemospassarparâmetrospara
o selectatravésdoscursores.Issotornanossaestruturamaisorganizada
epossibilitautilizá-laparaexecuç ãodediferentescritérios.Olheopróximo
exemplo.
cursor c1( pdeptno number
,pjob varchar2) is
select empno
,ename
from emp
where deptno = pdeptno
and job > pjob;
Oquediferenestadeclaraç ãoéadefiniçãodeparâmetros.Noteque,após
serinformadoonomedonossocursor,sãodefinidosparâmetrososquaisse-
rãoutilizadosdentrocomando select.Adefiniçãodeparâmetroséidêntica
adefiniçãodevariáveis.Aúnicadiferen çaéquenãoénecessárioinformara
quantidadedecaracteresparaotipodoparâmetro.Porexemplo,oparâmetro
pjobfoidefinidoapenascomo varchar2,nãoimportandoaquantidade
decaracteres.Nestescasos,oOracleconsideraomáximodecaracteresque
otiposuporta.Nesteexemploforamdefinidosdoisparâmetroseosmesmos
foramutilizadosnacláusula wheredocomandoselect.
Depoisquedefinimosocursor,precisamosdeclararumavariávelquere-
ceberáestadefinição.Estavariávelfuncionarácomoum array,ouseja,ao
abrirmosocursorosregistrosserãojogadosparaeste arrayparatrabalhar-
moscomeles.Vejamosadeclaraç ãoaseguir.
declare
--
cursor c1 is -- lista todos os empregados do departamento 30.
select ename
,job
from emp
where deptno = 30;
--
r1 c1%rowtype;
--
begin
109

## Página 121

10.1. Cursoresexplícitos CasadoCódigo
Nesteexemplo,édeclaradoocursor C1queselecionatodososemprega-
dosdodepartamento30.Depoisdedefinidonossocursor,foideclaradauma
variávelchamada R1queédotipo c1%rowtype. C1vemdonossocursor.
Jáo %rowtype,indicaquenossavariávelseráumarraydelinhasvindasdo
cursor. Comisto,nossadeclaraç ãoestácompletaejápodemosusarnosso
cursor.
Quandoutilizamosno selectdocursorapenasumatabela,podemos
optarporusaraprópriaestruturadatabelacomosendooarrayparanossa
variável.ComoaPL/SQLmantémumaconexãodireta(chamamosdenativa)
comobancodedadoseseusobjetos,elaconseguereconheceracompatibi-
lidadeentreasduasestruturas,adoarrayeado cursor.Vejaoexemploa
seguir.
declare
--
cursor c1 is -- lista todos os empregados do departamento 30.
select *
from emp
where deptno = 30;
--
r1 emp%rowtype;
--
begin
Vejaquenesteexemplo,declaramosanossavariável R1dotipoEMPem
vezdotipo C1referenteaonossocursor.Quandoinformamosque R1édo
tipo emp%rowtype,estamosdizendoquenossavariávelarrayédomesmo
tipo,oumelhor,teráamesmadefiniç ãobaseadanaestruturadatabelaEMP.
Logo,emnossocursor,trazemostodasascolunasdestatabela.Assimsendo,o
OraclecomparaaestruturadocursorcomaestruturadatabelaEMPevalida
estadefinição.
Noteque,nestecaso,nãopoderíamossuprimircolunasno selectdo
cursor,poisnacomparaç ãoentreasestruturasoOracleacusariaumadife-
rença.Portanto,resumindo,osnomes,asquantidadeseostiposdascolunas
devemseriguaisentreasestruturas.
110

## Página 122

CasadoCódigo Capítulo10. Cursores
Usando o cursor explícito
Ousodecursoresbasicamenteenvolvetrêspassos.Abertura,recupera-
çãoemanipulaç ãodosregistrosefechamentodocursor. Segueoexemplo
mostrandoousodocursorquedeclaramosanteriormente.
SQL> declare
2 --
3 cursor c1 is -- lista todos os empregados do
departamento 30.
4 select ename
5 ,job
6 from emp
7 where deptno = 30;
8 --
9 r1 c1%rowtype;
10 --
11 begin
12 --
13 open c1;
14 loop
15 fetch c1 into r1;
16 exit when c1%notfound;
17 --
18 dbms_output.put_line('Nome: '||r1.ename||'
Cargo: '||r1.job);
19 --
20 end loop;
21 --
22 close c1;
23 --
24 end;
25 /
Procedimento PL/SQL concluído com sucesso.
SQL>
Aslinhas3a7mostramadeclaraç ãodocursorvistoanteriormente.Na
linha9estádeclaradaavariávelarray R1dotipo C1,queénossocursor.Na
111

## Página 123

10.1. Cursoresexplícitos CasadoCódigo
linha13estápresenteocomando open c1;. Estecomandoabreocursor.
Jánalinha15,temosoretornodaslinhasreferentesao selectatravésda
linhadecomando fetch c1 into r1;. Emlinhasgeraisestecomando
significa:retorneaprimeiralinhaderegistrodo select.Nalinha18temos
ocomando put_linedopacote dbms_outputqueimprimenatelaonome
ecargodoempregado.
Notequeoprogramarecuperaestasinformaçõesatravésdoarray R1.
Notetambémqueasmesmascolunasdefinidasno selectdocursoragora
podemserusadasatravésde R1. Paraencerrar,nalinha22temosofecha-
mentodocursor.Valelembrarqueestasdelimitaçõesnãoservemapenaspara
tornarmaisfácilavisualizaçãodocódigo,masprincipalmenteparademarcar
ousodosdadosvindosdocursoratravésdoarray.Porexemplo,nãopode-
mosutilizar r1.enameantesdaaberturae fetchdocursor,nemapóso
fechamento.
Vamosaumaobservaç ãointeressante. Vocêdeveestarseperguntando
sobreoporquêdo looppresentedentrodaestrutura,certo?Poisbem,ante-
riormente,pararecuperarumregistroutilizamosocomando fetch.Esteco-
mandodentrodonossoprogramaretornaráapenasumregistro,entretanto,
nossocomando selectpoderetornarmaisdeumregistro. Porisso,em
conjuntocomcursorprecisamossempresolicitaroretornodosdemaisregis-
tros.Ocursorporsisónãoretornatodososregistrosresultantedocomando
select.Porissoutilizamosumaestruturaderepetiç ãoparanosauxiliar.
Sóparavocêsentenderem,cadavezqueabrimosumcursoroOracle
aponta-oparaoprimeiroregistrodo select.Todavia,elesóérecuperado
quandochamamoso fetch.Esteporsuaveztrazapenasoprimeiroregis-
tro. Paraqueospróximosregistrossejamrecuperados,temosqueexecutar
o fetchnovamente. Éaíqueentraaestruturaderepetiç ão. Repetimoso
comando fetchatéquenãohajamaisregistrosretornados.Paraqueopro-
gramasaibaquandonãohámaisregistrospararetornar,podemosutilizara
linhadecomando exit when c1%notfound. Estalinhaindicaquando
sedevesairdaestruturaloop,ouseja,quandoocursor C1nãotivermais
registrospararetornar.
%notfoundéumatributodecursorqueindicaanãoexistênciademais
registrosaseremlidosdentrodeumcursor.Maisadianteveremosmaissobre
112

## Página 124

CasadoCódigo Capítulo10. Cursores
esteassunto.Notequeaestruturaderepetiç ãodeveobedeceràsdelimitações
deaberturaefechamentodocursor.Aausênciadeumaestruturaderepetiç ão
nãocaracterizaumerro.Contudo,apenasumregistroseriaretornado.
Nousodecursorémaiscomumvermosaestruturadotipoloopsimples,
maspodemosutilizartambémasestruturas whilee for loop,sendoque
esteúltimotornaamanipulaç ãodocursorbemmaisfácil,poiselejáfazal-
gunscontrolesautomaticamente. Maisàfrentenósveremosumexemplo.
Vamosveroutroexemploutilizandopassagemdevaloresporparâmetro.
SQL> declare
2 --
3 cursor c1( pdname varchar2
4 ,pmgr number) is
5 select ename, job, dname
6 from emp, dept
7 where emp.deptno = dept.deptno
8 and dept.loc = pdname
9 and emp.mgr = pmgr;
10 --
11 r1 c1%rowtype;
12 --
13 begin
14 --
15 open c1('CHICAGO',7698 );
16 loop
17 fetch c1 into r1;
18 exit when c1%notfound;
19 --
20 dbms_output.put_line('Nome: '||r1.ename||'
Cargo: '||r1.job);
21 --
22 end loop;
23 --
24 close c1;
25 --
26 end;
27 /
113

## Página 125

10.1. Cursoresexplícitos CasadoCódigo
Procedimento PL /SQL concluído com sucesso.
SQL>
Adeclaraçãodecursorescompassagemdeparâmetro,nósjáhavíamos
vistoanteriormente. Oquedevemosprestaraten çãoécomoequandode-
vemospassarosvaloresparaocursor. Observandoalinha15doprograma
anteriorépossívelverificaraaberturadocursor. Énestaaberturaquede-
vemospassarosvaloresparaosparâmetros. Aoabrirocursor,oOraclejá
levaosvaloresdeentradaparaseremutilizadosdentrodo select.Osva-
loresinformadosdevemseguiramesmaordemdefinidaparaosparâmetros.
Umaalternativaaissoéachamadapassagemdeparâmetronomeada,onde
aoinformarosvalorestambéméinformadoqualparâmetrodeverecebê-los.
Nestescasos,aordemnãoprecisaserrespeitada. Vejaomesmoprograma,
agorautilizandopassagemdeparâmetrosnomeada.
SQL> declare
2 --
3 cursor c1( pdname varchar2
4 ,pmgr number) is
5 select ename, job, dname
6 from emp, dept
7 where emp.deptno = dept.deptno
8 and dept.loc = pdname
9 and emp.mgr = pmgr;
10 --
11 r1 c1%rowtype;
12 --
13 begin
14 --
15 open c1( pmgr => 7698
16 ,pdname => 'CHICAGO');
17 loop
18 fetch c1 into r1;
19 exit when c1%notfound;
20 --
21 dbms_output.put_line('Nome: '||r1.ename||'
Cargo: '||r1.job);
114

## Página 126

CasadoCódigo Capítulo10. Cursores
22 --
23 end loop;
24 --
25 close c1;
26 --
27 end;
28 /
Procedimento PL/SQL concluído com sucesso.
SQL>
Noteaslinhas15e16.Apassagemnomeadaconsisteeminformaronome
doparâmetroeovalorqueeledevereceber. Deveserinformadoonome
doparâmetroseguidodossinais =>,seguidodovaloraserpassadocomo
parâmetro. Vejatambémqueaordemfoiinvertidacomrelaç ãoaoquefoi
definidonadeclaraçãodocursor.
Contudo,comoestamosinformandoqualparâmetrorecebetalvalor,não
teremosproblemaseosparâmetrosestiverememumaordemcontrária. O
usodesteartifícioébeminteressantequandotemosumagrandequantidade
deparâmetros. Seaquantidadeforgrandecorre-seoriscodecolocaral-
gumparâmetroforadaordemcorreta,quecertamenteocasionaráumerro
naaberturadocursorounalógicadoprograma.
10.2 C ursor F O R L O O P
Anteriormente,mencioneialgosobreocursorcomusodo for loop.Pois
bem.Conformeeujáhaviafalado,ousodecursorescom for loop tornao
trabalhomaiscômodo,poisnãoprecisamosnospreocuparemabrirefechar
ocursor,nemrealizaro fetch.Elefaztudosozinho.Paramelhorentendi-
mentovamosveroprogramaaseguir.
SQL> declare
2 --
3 cursor c1( pdname varchar2
4 ,pmgr number) is
5 select ename, job, dname
115

## Página 127

CasadoCódigo
6 from emp, dept
7 where emp.deptno = dept.deptno
8 and dept.loc = pdname
9 and emp.mgr = pmgr;
10 --
11 begin
12 --
13 for r1 in c1( pmgr => 7698
14 ,pdname => 'CHICAGO') loop
15 --
16 dbms_output.put_line('Nome: '||r1.ename||'
Cargo: '||r1.job);
17 --
18 end loop;
19 --
20 end;
21 /
Procedimento PL /SQL concluído com sucesso.
SQL>
Énítidaadiferen çaentreummétodoeoutro.Vejaqueeliminamosalgu-
maslinhasdecódigo.Opróprio forseencarregadeabrirocursor,realizar
abuscadosregistros,verificarquandonãohámaisregistrosefecharocur-
sor. Maisumdetalhe:utilizandoo for loop,nãoénecessáriodeclarara
variáveldotipo rowtypecombasenocursor,opróprio for loop fazisto
medianteumnomeinformado.Vejaquenoexemplo,sófoiprecisoinformar
umnome,nocaso R1,apósocomandofor,queorestoeleseencarregoude
fazer.Assimcomonousodo loop,o fortambémdelimitaumaáreaque
deverespeitada.
Agoravocêdeveestarsequestionando:porqueusar loopse for loop
trazmaisfacilidadesemfalarquenãoénecessárioquesecontroleumasérie
decoisas?Naverdadevocêtemrazão,nadaimpededevocêutilizarsempre
ocursorcom for loop.Contudo,àmedidaquevocêfortrabalhandocom
cursores,vaisentiranecessidadedeusarumououtro.Porexemplo,quando
temosumcursorondenãonecessariamentetemosquelertodasaslinhas
116

## Página 128

CasadoCódigo Capítulo10. Cursores
vindasdo select,podemosutilizaro loop,poisnestemétodosomosnós
quecontrolamosabuscadaslinhas.
Nestecaso,ébemmaispráticoutilizarum loop.Valeressaltarquecom
ousode for loop,devemosinformarquandoeledevepararsuaexecuç ão,
casonãofordenossavontadequeeleleiatodososregistrosresultantesdo
select. Jácomousodo loopéocontrário,sequisermosqueeleleiaos
registros,devemoscomandá-loatravésdo fetch.Quandoquiserpararuma
execução for loop,utilizamosocomando exitou exit when.Vejaum
exemplo.
SQL> declare
2 --
3 cursor c1( pdname varchar2
4 ,pmgr number) is
5 select ename, job, dname
6 from emp, dept
7 where emp.deptno = dept.deptno
8 and dept.loc = pdname
9 and emp.mgr = pmgr;
10 --
11 --
12 --
13 begin
14 --
15 for r1 in c1( pmgr => 7698
16 ,pdname => 'CHICAGO') loop
17 --
18 dbms_output.put_line( 'Nome: '||r1.ename||'
Cargo: '||r1.job);
19 --
20 /*
21 if r1.ename = 'MARTIN' then
22 exit;
23 end if;
24 */
25 --
26 exit when r1.ename = 'MARTIN';
27 --
117

## Página 129

CasadoCódigo
28 end loop;
29 --
30 end;
31 /
Procedimento PL /SQL concluído com sucesso.
SQL>
Maisàfrentenóstambémveremosqueàsvezespodesermaisperfor-
máticoutilizarumcursorpararetornarumúnicoregistroemvezdeutilizar
into.Nestecasonãoutilizamosestruturasderepetiç ão.
10.3 C ursor for loop com definição interna
10.3. CURSORFORLOOPCOMDEFINIÇÃOINTERNA
Comousodecursorescom for loop temosdisponívelmaisumrecurso
queéapossibilidadededeclararmosocomando selectdocursordentro
doprópriocomando for loop. Destaforma,nãoprecisamosdeclararo
cursornoescopodedeclarações,conformevistonosexemplosanteriores,e
sim,naprópriadefiniç ãodo for loop.Oúnicoinconvenienteéquesenós
tivermosquechamarestecursor for loop váriasvezesdentrodoprograma,
teremosocomando selectescritorepetidamenteemtodasasaberturas.
Nocasodeumaalteraç ãonele,teremosquemodificaremtodasaschamadas,
enquantonadeclaraçãoforado for loop (nobloco declare)aalteração
seráemumúnicolugar.
SQL> declare
2 --
3 begin
4 --
5 for r1 in (select empno, ename
6 from emp
7 where job = 'MANAGER' ) loop
8 --
9 dbms_output.put_line(
'Gerente: '||r1.empno||' - '||r1.ename);
118

## Página 130

CasadoCódigo Capítulo10. Cursores
10 --
11 for r2 in (select empno, ename, dname
12 from emp, dept
13 where emp.deptno = dept.deptno
14 and mgr = r1.empno) loop
15 --
16 dbms_output.put_line(
' Subordinado: '||r2.empno||' - '||r2.ename);
17 --
18 end loop;
19 --
20 dbms_output.put_line('');
21 --
22 end loop;
23 --
24 end;
25 /
SQL>
10.4 C ursores implícitos
10.4. CURSORESIMPLÍCITOS
EmviasgeraisquandonãocriamosumcursorexplicitooOraclecriaum
cursorautomaticamente. Aestecursorsedáonomede cursor implícito.
Implícitoporqueécriado,aberto,manipuladoefechadopelopróprioOracle.
Mascomosabemos,oumelhor,comovemosousodetalcursor?Naverdade
nãovemos,pelomenosnãonasuatotalidade.
OcursorimplícitoécriadoquandodentrodonossoprogramaPL/SQL
utilizamosalgumdoscomandos: delete, update, insertou select
into.
Quandoexecutamososcomandos delete, insertou update,oOra-
clecriaumcursorimplícito,abreestecursor,executaocomandoedepoiso
fecha.Quandoexecutamosum select into dentrodonossoprograma,
porexemplo,oOraclevaialémeabreumcursorimplicitamenteeexecuta
váriospassoseverificaçõesadicionais.Vejaospassosaseguir.
119

## Página 131

CasadoCódigo
Cursor implícito: passos realizados pelo Oracle
1) Criaumcursorimplícito.
2) Realizaumprimeiro fetchpararetornarumalinha.
3) Realizaumsegundo fetchparaverificarseocomandonãoretornamais
deumalinha.
4) Fechaocursor.
Notequenocasodo select into oOracleprecisatratardeterminadas
situações,poisousodocomando selectdentrodosprogramasPL/SQL
podemgerar exceptions. Quandonãoéretornadanenhumalinhauma
exceptionde no_data_foundédisparada. Jáquandováriaslinhassão
retornadasoutraexceptionchamada too_many_rowsprecisaseracionada
também.
Destaforma,quandosehácertezadequeo selectemquestãovaire-
tornarapenasumalinha,podeserusadoumcursorexplícito. Nestecaso,
menospassosserãoutilizados,poisquemtrataráestassituaçõessomosnós
dentrodoprograma.Entretanto,estaformaparecesermaistrabalhosa,ecom
certezaé!Contudo,quandoestamosfalandodeperformance,osganhospo-
demserbemconsideráveis.Éóbvioqueestamosfalandoaquiparaoscasos
ondeoscomandos selectssãocomplexoscommuitastabelasegrandes
quantidadesdedados.Paraumcursorexplícitoospassosficariamassim:
Cursor explícito: passos realizados pelo programa
1) Criaumcursorimplícito.
2) Realizaumprimeiro fetchpararetornaralinha.
3) Fechaocursor.
Comisto,fazemoscomquepelomenosumpassonãosejaexecutado.
Paraum selectquetrabalhecommilhõesderegistrosissopodenosdar
umótimoganhodetempodeexecuç ão.
120

## Página 132

CasadoCódigo Capítulo10. Cursores
10.5 A tributos de cursor explícito e implícito
10.5. ATRIBUTOSDECURSOREXPLÍCITOEIMPLÍCITO
Nosexemplosanterioresvimosalgunsatributosqueauxiliamnahoradese
utilizarcursores.Estesatributostrazeminformaçõesquepodemajudarode-
senvolvedoratomardecisõeseafazercomqueoprogramatomecertosca-
minhos.Estesatributosestãodisponíveistantoparacursoresexplícitoscomo
paraosimplícitos,comexce çãodoatributo %isopenquesópodeserutili-
zadoemcursoresexplícitos.Estesatributossãoutilizadosdaseguinteforma:
Quandoestamostrabalhandocomoscursoresexplícitosusamosonome
docursorseguidodoatributo,porexemplo, c1%found. Paraoscursores
implícitos,oOracledisponibilizaocursor“SQL”queapontasempreparao
comandoqueestásendoexecutadonomomento.Destaforma,usa-seonome
destecursorseguidodoatributo,exemplo, sql%found.ObservequeoOra-
cleutilizasempreomesmocursorparaumaoumaisexecuções.Portanto,ele
deveserutilizadosempreapósaexecuç ãodocomando,poisasinformações
deumcursorrecém-executadosobrescreverãoasinformaçõesdaexecuç ão
anterior.Aseguirosatributosquepodemosutilizar.
%found
Esteatributoéutilizadoparaindicarseaúltimaoperaç ãorealizadapelo
fetchfoiconcluídacomêxitoouseumadeterminadalinhafoialteradaatra-
vésdealgumcomando insert, updateou delete,ouse,nocasodeum
select into ouvealgumretornodeumaoumaislinhas. Paracursores
explícitos:
SQL> declare
2 --
3 cursor c1( pdname varchar2
4 ,pmgr number) is
5 select ename, job, dname
6 from emp, dept
7 where emp.deptno = dept.deptno
8 and dept.loc = pdname
9 and emp.mgr = pmgr;
10 --
121

## Página 133

CasadoCódigo
11 r1 c1%rowtype;
12 --
13 begin
14 --
15 open c1( pmgr => 7698, pdname => 'CHICAGO');
16 loop
17 fetch c1 into r1;
18 --
19 if c1%found then
20 --
21 dbms_output.put_line('Nome: '||r1.ename||'
Cargo: '||r1.job);
22 --
23 else
24 --
25 exit;
26 --
27 end if;
28 end loop;
29 --
30 close c1;
31 --
32 end;
33 /
Procedimento PL /SQL concluído com sucesso.
SQL>
Paracursoresimplícitos:
SQL> declare
2 --
3 wename emp.ename%type;
4 wjob emp.job%type;
5 wdname dept.dname%type;
6 --
7 begin
8 --
9 select ename, job, dname
122

## Página 134

CasadoCódigo Capítulo10. Cursores
10 into wename, wjob, wdname
11 from emp, dept
12 where emp.deptno = dept.deptno
13 and dept.loc = 'CHICAGO'
14 and emp.mgr = 7698
15 and job = 'CLERK';
16 --
17 if SQL%found then
18 --
19 dbms_output.put_line(
'O select retornou o seguinte registro: Nome: '||
20 wename||' Cargo: ' ||wjob);
21 --
22 end if;
23 --
24 end;
25 /
Procedimento PL/SQL concluído com sucesso.
SQL>
%notfound
Esteoutroatributomostraexatamenteocontrárioaoatributo %found,
poisocomando %notfoundretornasempre falseseoúltimocomando
fetchnãoretornarumalinhanocasodeumcursorexplícito,ouseoúl-
timocomandode update, insert, deletenãoalterarnenhumalinha.O
mesmonãoserveparaonãoretornodeumalinhaemumcomando select
into,poisnestecasoaexception no_data_foundédisparada.Paracur-
soresexplícitos:
SQL> declare
2 --
3 cursor c1( pdname varchar2
4 ,pmgr number) is
5 select ename, job, dname
6 from emp, dept
7 where emp.deptno = dept.deptno
123

## Página 135

CasadoCódigo
8 and dept.loc = pdname
9 and emp.mgr = pmgr;
10 --
11 r1 c1%rowtype;
12 --
13 begin
14 --
15 open c1( pmgr => 7698, pdname => 'CHICAGO');
16 loop
17 fetch c1 into r1;
18 --
19 exit when c1%notfound;
20 --
21 dbms_output.put_line(
'Nome: '||r1.ename||' Cargo: '||r1.job);
22 --
23 end loop;
24 --
25 close c1;
26 --
27 end;
28 /
Procedimento PL /SQL concluído com sucesso.
SQL>
Paracursoresimplícitos:
SQL> declare
2 --
3 wename emp.ename%type;
4 wjob emp.job%type;
5 wdname dept.dname%type;
6 --
7 begin
8 --
9 update emp
10 set deptno = 100
11 where job = 'ANALISTA_1';
124

## Página 136

CasadoCódigo Capítulo10. Cursores
12 --
13 if SQL%notfound then
14 --
15 dbms_output.put_line('Nenhum registro foi atualizado.');
16 --
17 end if;
18 --
19 end;
20 /
Procedimento PL/SQL concluído com sucesso.
SQL>
%rowcount
Esteatributoéutilizadoparafazeracontagemdonúmerodelinhaslidas,
ouparalinhasqueforamafetadasporalgumcomando insert, update
ou delete,ou,poralgumretornoocasionadoporumcomando select
into. Valesalientarqueautilizaç ãodelessegueasmesmasregrasparaos
tiposdecursoresmencionadosnosoutrosatributosanteriores.Paracursores
explícitos:
SQL> declare
2 --
3 cursor c1( pdname varchar2
4 ,pmgr number) is
5 select ename, job, dname
6 from emp, dept
7 where emp.deptno = dept.deptno
8 and dept.loc = pdname
9 and emp.mgr = pmgr;
10 --
11 r1 c1%rowtype;
12 --
13 begin
14 --
15 open c1( pmgr => 7698, pdname => 'CHICAGO');
16 --
125

## Página 137

CasadoCódigo
17 loop
18 fetch c1 into r1;
19 --
20 exit when c1%notfound;
21 --
22 dbms_output.put_line(
'Nome: '||r1.ename||' Cargo: '||r1.job);
23 --
24 end loop;
25 --
26 dbms_output.put_line('');
27 dbms_output.put_line(
'Registros recuperados: '||c1%rowcount||'.');
28 --
29 close c1;
30 --
31 end;
32 /
Procedimento PL /SQL concluído com sucesso.
SQL>
Paracursoresimplícitos:
SQL> declare
2 --
3 wename emp.ename%type;
4 wjob emp.job%type;
5 wdname dept.dname%type;
6 --
7 begin
8 --
9 delete emp
10 where deptno = (select deptno
11 from dept
12 where dname = 'SALES');
13 --
14 dbms_output.put_line(
SQL%rowcount||' registro(s) foram excluídos.');
126

## Página 138

CasadoCódigo Capítulo10. Cursores
15 --
16 commit;
17 --
18 end;
19 /
Procedimento PL/SQL concluído com sucesso.
SQL>
%isopen
Esteatributoéutilizadoparaverificarseumcursorestáounãoaberto.
Eleestarácomoverdadeiroseocursorestiveraberto,efalsoseestiverfe-
chado.Esteatributosópodeserusadoemcursoresexplícitos.Paracursores
explícitos:
SQL> declare
2 --
3 cursor c1( pdname varchar2
4 ,pmgr number) is
5 select ename, job, dname
6 from emp, dept
7 where emp.deptno = dept.deptno
8 and dept.loc = pdname
9 and emp.mgr = pmgr;
10 --
11 r1 c1%rowtype;
12 --
13 begin
14 --
15 loop
16 if c1%isopen then
17 --
18 fetch c1 into r1;
19 --
20 if c1%notfound then
21 --
22 close c1;
127

## Página 139

CasadoCódigo
23 exit;
24 --
25 else
26 --
27 dbms_output.put_line(
'Nome: '||r1.ename||' Cargo: '||r1.job);
28 --
29 end if;
30 --
31 else
32 --
33 dbms_output.put_line('O Cursor não foi aberto!');
34 dbms_output.put_line('Abrindo cursor...');
35 open c1( pmgr => 7698, pdname => 'CHICAGO');
36 --
37 end if;
38 --
39 end loop;
40 --
41 end;
42 /
Procedimento PL /SQL concluído com sucesso.
SQL>
10.6 C ursores encadeados
10.6. CURSORESENCADEADOS
Outrorecursodoscursoreséapossibilidadedeseremusadosdeformaen-
cadeada,ouseja,podemostercursoressendomanipuladosdentrodeoutros
cursores.Vejaumexemplo.
SQL> declare
2 --
3 cursor c1 is
4 select empno, ename
5 from emp
128

## Página 140

CasadoCódigo Capítulo10. Cursores
6 where job = 'MANAGER';
7 --
8 cursor c2(pmgr number) is
9 select empno, ename, dname
10 from emp, dept
11 where emp.deptno = dept.deptno
12 and mgr = pmgr;
13 --
14 begin
15 --
16 for r1 in c1 loop
17 --
18 dbms_output.put_line(
'Gerente: '||r1.empno||' - '||r1.ename);
19 --
20 for r2 in c2(r1.empno) loop
21 --
22 dbms_output.put_line(
' Subordinado: '||r2.empno||' - '||r2.ename);
23 --
24 end loop;
25 --
26 dbms_output.put_line('');
27 --
28 end loop;
29 --
30 end;
31 /
Procedimento PL/SQL concluído com sucesso.
SQL>
Nesteexemploestamosselecionandotodososempregadosgerentescom
seusrespectivossubordinados. Oprimeirocursor C1localizaosgerentes.
Paracadagerenteencontradoélistadotodososseussubordinadospelocursor
C2.Notequeocursor C2recebecomoparâmetroocódigodogerentevindo
de C1.Paracadalinharetornadade C1sãorecuperadastodasaslinhasde
C2.O for loop seencarregadeabrirefecharoscursoresquantasvezesfor
129

## Página 141

CasadoCódigo
necessárioatéquealeituradetodososregistrosemambososcursoreschegue
aofim.
10.7 C ursor com for update
10.7. CURSORCOMFORUPDATE
Quandoqueremosatualizarouexcluirlinhasdeumatabela,podemosfazer
istocomoauxíliodeumcursor for update.Podemoscriarumcursorba-
seadonatabelaemquestãoeutilizarainstruç ão for update paragarantir
queenquantoeleestivervarrendoaslinhasdatabela,nenhumaoutrasessão
possaestarmanipulandoosmesmosdados. Issotambémacontecemesmo
quevocênãovenhaaatualizá-los. Osimplesfatodeestarabrindoumcur-
sor for update jáfazcomqueoacessosejaexclusivo. Vejaaseguirum
exemplodecursor for update.
SQL> declare
2 --
3 cursor c1( pdname varchar2) is
4 select ename, job, dname
5 from emp, dept
6 where emp.deptno = dept.deptno
7 and dept.loc = pdname
8 for update;
9 --
10 r1 c1%rowtype;
11 --
12 begin
13 open c1( pdname => 'DALLAS');
14 loop
15 if c1%isopen then
16 fetch c1 into r1;
17 if c1%notfound then
18 close c1;
19 exit;
20 else
21 dbms_output.put_line(
'Nome: '||r1.ename||' Cargo: '||r1.job);
22 end if;
130

## Página 142

CasadoCódigo Capítulo10. Cursores
23 else
24 dbms_output.put_line('O Cursor não foi aberto!');
25 exit;
26 end if;
27 end loop;
28 end;
29 /
Procedimento PL/SQL concluído com sucesso.
SQL>
Utilizando for update,oOraclerealizaum locknaslinhasdata-
belagarantindoexclusividadeparamanipulá-las. Apósum rollbackou
commit,aslinhasvoltamaserliberadas. Estecomandopodeserutilizado
deduasformas,sendoacompanhadoounãopornomesdecolunasespecí-
ficas.Quandotemosum selectcomváriastabelasnacláusula fromnós
podemosdeterminarquais,ouqual,tabelasdevemserlocadasinformando
suascolunas. Casoqueiraquetodasastabelassejamlocadasusesomente
for update.Agoravejaomesmoexemplo,informandoascolunasparaa
locaçãodatabela.
SQL> declare
2 --
3 cursor c1( pdname varchar2) is
4 select ename, job, dname
5 from emp, dept
6 where emp.deptno = dept.deptno
7 and dept.loc = pdname
8 for update of ename, dname;
9 --
10 r1 c1%rowtype;
11 --
12 begin
13 open c1( pdname => 'DALLAS');
14 loop
15 if c1%isopen then
16 fetch c1 into r1;
131

## Página 143

CasadoCódigo
17 if c1%notfound then
18 close c1;
19 exit;
20 else
21 dbms_output.put_line(
'Nome: '||r1.ename||' Cargo: '||r1.job);
22 end if;
23 else
24 dbms_output.put_line('O Cursor não foi aberto!');
25 exit;
26 end if;
27 end loop;
28 end;
29 /
Procedimento PL /SQL concluído com sucesso.
SQL>
Nesteexemploestamoslocandoastabelas EMPe DEPT,poisestamos
informandocolunasdeambasàstabelas.Contudo,podemoslocarumaúnica
tabelainformandoumaoumaiscolunasquefazempartedela. Segueum
exemplo.
SQL> declare
2 --
3 cursor c1( pdname varchar2) is
4 select ename, job, dname
5 from emp, dept
6 where emp.deptno = dept.deptno
7 and dept.loc = pdname
8 for update of ename;
9 --
10 r1 c1%rowtype;
11 --
12 begin
13 open c1( pdname => 'DALLAS');
14 loop
15 if c1%isopen then
132

## Página 144

CasadoCódigo Capítulo10. Cursores
16 fetch c1 into r1;
17 if c1%notfound then
18 close c1;
19 exit;
20 else
21 dbms_output.put_line(
'Nome: '||r1.ename||' Cargo: '||r1.job);
22 end if;
23 else
24 dbms_output.put_line('O Cursor não foi aberto!');
25 exit;
26 end if;
27 end loop;
28 end;
29 /
Procedimento PL/SQL concluído com sucesso.
SQL>
Enquantoatabelaestiverem lockqualquersessãoquetentarmanipular
seusdados,exceto select,nãoteráêxito.Asessãoficaráesperandoalibe-
raçãoatéqueoprogramaquelockouaslinhasaslibere.Feitoisso,qualquer
outrasessãopoderáefetuaralterações.
Emboraoprogramaquecontémumcursor for update tenhaexclu-
sividadedeacesso,elesóconseguirárealizarum lockcasoastabelasque
fazempartedeste locknãoestejamlockadasporoutrassessões.Seissoesti-
verocorrendo,oprogramatambémsofreráumaesperaatéqueoutrasessão
liberetaistabelas.
Quandoexecutamosalgumaoperaç ãoemumadeterminadatabela,ea
mesmaestálockada,aconteceuma“espera”pelorecurso.Issoquerdizerque
suasessãoficarátentandoexecutaroscomandosatéqueorecursoestejadis-
poníveloucasovocêcanceleaoperaç ão.
Quandovocêestiverutilizandoumcursorcom for update enãoqui-
serque,aoexecutá-lo,elefiqueesperandoporumrecurso,porexemplo,uma
tabelaqueestejasendolocadaporoutrasessão,useadiretriz nowait.Feito
isto,oprogramanãoficaráemesperaeserádisparadouma exceptionin-
133

## Página 145

CasadoCódigo
formandoqueorecursoemquestãoestáocupado.
SQL> declare
2 --
3 cursor c1( pdname varchar2) is
4 select ename, job, dname
5 from emp, dept
6 where emp.deptno = dept.deptno
7 and dept.loc = pdname
8 for update of ename nowait;
9 --
10 r1 c1%rowtype;
11 --
12 begin
13 open c1( pdname => 'DALLAS');
14 loop
15 if c1%isopen then
16 fetch c1 into r1;
17 if c1%notfound then
18 close c1;
19 exit;
20 else
21 dbms_output.put_line(
'Nome: '||r1.ename||' Cargo: '||r1.job);
22 end if;
23 else
24 dbms_output.put_line('O Cursor não foi aberto!');
25 exit;
26 end if;
27 end loop;
28 end;
29 /
declare
*
ERRO na linha 1:
ORA-00054: o recurso está ocupado e é obtido com o NOWAIT
especificado
ORA-06512: em line 4
ORA-06512: em line 13
134

## Página 146

CasadoCódigo Capítulo10. Cursores
SQL>
Como for update paraauxiliarnaexclusãoeatualizaç ãodaslinhasde
umatabela,épossívelutilizarumrecursomuitopoderosoquetrazsimplici-
dadeeótimosganhosdeperformance.Quandovocêestiverexecutandoum
comando updateou deleteparaatualizarlinhasdeumatabelaexistente
noprópriocursor,use current of.EstacláusulafazcomqueoOracleuti-
lizeo rowiddalinha,queéoacessomaisdiretoerápidoaoregistro.Observe
oexemplo.
SQL> declare
2 --
3 cursor c1( pdeptno number) is
4 select *
5 from emp
6 where deptno = pdeptno
7 for update of sal nowait;
8 --
9 r1 c1%rowtype;
10 --
11 wreg_excluidos number default 0;
12 --
13 begin
14 open c1( pdeptno => 10);
15 loop
16 fetch c1 into r1;
17 exit when c1%notfound;
18 --
19 update emp set sal = sal + 100.00
20 where current of c1;
21 --
22 wreg_excluidos := wreg_excluidos + sql%rowcount;
23 --
24 end loop;
25 --
26 dbms_output.put_line(wreg_excluidos||'
registros excluídos!');
135

## Página 147

CasadoCódigo
27 --
28 end;
29 /
Procedimento PL /SQL concluído com sucesso.
SQL>
Notenocódigoque,aoutilizarocomando update,nãofoiprecisoin-
formarumacláusula wherebaseadaemalgumachavedatabela,comopor
exemplo, empno.Comoosregistrosestãoreservadosparaoprograma,atra-
vésdo for update,podemosatualizaraslinhasusandocomocritérioa
referenciadalinhadocursor. Dessaforma,oOraclegaranteaintegridade
dosdados.Omesmopodeserusadoparaocomando delete.
Esterecursotambémfuncionaparaquandoestivermosusandomaisde
umatabelanacláusula from. Oúnicopontodeobservaç ãoéquenãopo-
demosdeixardedefinirascolunasparao for update,tãopoucodefinir
colunasdediferentestabelassequisermosutilizaro current of.Issopor-
que,nestescasos,oOraclesópodetrabalharcom rowidsdeumaúnica
tabela.Vejaalgunsexemplos:
SQL> declare
2 --
3 cursor c1( pdloc varchar2) is
4 select ename, dname
5 from emp, dept
6 where emp.deptno = dept.deptno
7 and dept.loc = pdloc
8 for update of emp.ename, dept.loc;
9 --
10 r1 c1%rowtype;
11 --
12 wreg_atua_dep number default 0;
13 wreg_excl_emp number default 0;
14 --
15 begin
16 open c1( pdloc => 'NEW YORK' );
17 loop
136

## Página 148

CasadoCódigo Capítulo10. Cursores
18 fetch c1 into r1;
19 exit when c1%notfound;
20 --
21 update dept set loc = 'FLORIDA' where current of c1;
22 --
23 wreg_atua_dep := wreg_atua_dep + sql%rowcount;
24 --
25 delete emp where current of c1;
26 --
27 wreg_excl_emp := wreg_excl_emp + sql%rowcount;
28 --
29 end loop;
30 --
31 dbms_output.put_line(wreg_atua_dep||' registros de
departamentos atualizados!');
32 dbms_output.put_line(wreg_excl_emp||' registros de
empregados excluídos!');
33 --
34 end;
35 /
0 registros de departamentos atualizados!
0 registros de empregados excluídos!
Procedimento PL/SQL concluído com sucesso.
SQL>
Nesteexemploestamostentandoatualizaratabela DEPTetambémex-
cluirregistrosdatabela EMP.Entretanto,mesmoinformandoumacoluna
decadatabelano for update,eoOraclenãoapresentandoqualquerpro-
blemanaexecuç ão,osregistrosnãosofreramqualquermodificaç ão.Vamos
tentaralgodiferentenoexemploaseguir.
SQL> declare
2 --
3 cursor c1( pdloc varchar2) is
4 select ename, dname
5 from emp, dept
6 where emp.deptno = dept.deptno
137

## Página 149

CasadoCódigo
7 and dept.loc = pdloc
8 for update of emp.ename, dept.loc;
9 --
10 r1 c1%rowtype;
11 --
12 wreg_atua_dep number default 0 ;
13 wreg_excl_emp number default 0 ;
14 --
15 begin
16 open c1( pdloc => 'NEW YORK' );
17 loop
18 fetch c1 into r1;
19 exit when c1%notfound;
20 --
21 delete emp where current of c1;
22 --
23 wreg_excl_emp := wreg_excl_emp + sql%rowcount;
24 --
25 end loop;
26 --
27 dbms_output.put_line(wreg_excl_emp||' registros de
empregados excluídos!');
28 --
29 end;
30 /
0 registros de empregados excluídos!
Procedimento PL /SQL concluído com sucesso.
SQL>
Mesmoretirandoumdoscomandos,oOraclenãoconsegueconcretizar
asalterações. Portanto,oproblemanãoestánaquantidadeoudistin çãode
comandosdentrodoblocodocursore,sim,nasuadefiniç ão.Vamosdeixar
nacláusula for update somenteacolunareferenteàtabela EMP.
SQL> declare
2 --
3 cursor c1( pdloc varchar2) is
138

## Página 150

CasadoCódigo Capítulo10. Cursores
4 select ename, dname
5 from emp, dept
6 where emp.deptno = dept.deptno
7 and dept.loc = pdloc
8 for update of emp.ename;
9 --
10 r1 c1%rowtype;
11 --
12 wreg_atua_dep number default 0;
13 wreg_excl_emp number default 0;
14 --
15 begin
16 open c1( pdloc => 'NEW YORK' );
17 loop
18 fetch c1 into r1;
19 exit when c1%notfound;
20 --
21 delete emp where current of c1;
22 --
23 wreg_excl_emp := wreg_excl_emp + sql%rowcount;
24 --
25 end loop;
26 --
27 dbms_output.put_line(wreg_excl_emp||' registros de
empregados excluídos!');
28 --
29 end;
30 /
3 registros de empregados excluídos!
Procedimento PL/SQL concluído com sucesso.
SQL>
Agoranossocomandofuncionoucomêxito. Foiutilizadamaisdeuma
tabelanacláusula from,todavia,nacláusula for update definimosapenas
acolunarelacionadaàtabela EMP.Lembre-sequenoscasosondeo select
possuamaisdeumatabelanacláusula from,senãorelacionarmosacoluna
nacláusula for update,lockandoatabela,nãopoderemosutilizaracláu-
139

## Página 151

CasadoCódigo
sula current of. Seissoacontecer,oOracledisparauma exception
gerandoumerro.Noscasosondetemosapenasumatabelanacláusula from
podemosutilizarsomente for update.Vejaosexemplos.
SQL> declare
2 --
3 cursor c1( pdloc varchar2) is
4 select ename, dname
5 from emp, dept
6 where emp.deptno = dept.deptno
7 and dept.loc = pdloc
8 for update of dept.loc;
9 --
10 r1 c1%rowtype;
11 --
12 wreg_atua_dep number default 0;
13 wreg_excl_emp number default 0;
14 --
15 begin
16 open c1( pdloc => 'NEW YORK' );
17 loop
18 fetch c1 into r1;
19 exit when c1%notfound;
20 --
21 delete emp where current of c1;
22 --
23 wreg_excl_emp := wreg_excl_emp + sql%rowcount;
24 --
25 end loop;
26 --
27 dbms_output.put_line(wreg_excl_emp||' registros de
empregados excluídos!');
28 --
29 end;
30 /
declare
*
ERRO na linha 1:
ORA-01410: ROWID inválido
140

## Página 152

CasadoCódigo Capítulo10. Cursores
ORA-06512: em line 21
SQL>
Aquitentamosutilizar current of emum deletenatabela EMP,
sendoqueemnosso for update definimosumacolunadatabela DEPT.
SQL> declare
2 --
3 cursor c1( pdloc varchar2) is
4 select dname
5 from dept
6 where dept.loc = pdloc
7 for update;
8 --
9 r1 c1%rowtype;
10 --
11 wreg_atua_dep number default 0;
12 --
13 begin
14 open c1( pdloc => 'NEW YORK' );
15 loop
16 fetch c1 into r1;
17 exit when c1%notfound;
18 --
19 update dept set loc = 'FLORIDA' where current of c1;
20 --
21 wreg_atua_dep := wreg_atua_dep + sql% rowcount;
22 --
23 end loop;
24 --
25 dbms_output.put_line(wreg_atua_dep||' registros de
departamentos atualizados!');
26 --
27 end;
28 /
1 registros de departamentos atualizados!
141

## Página 153

CasadoCódigo
Procedimento PL /SQL concluído com sucesso.
SQL>
Aquiocomandofoiexecutadodeformacorretaecomsucesso.Comoo
selectdonossocursoréformadoapenasporumatabela,nãofoipreciso
especificarcolunasnacláusula for update.
142

## Página 154

Capítulo11
Funçõesdecaracterese
operadoresaritméticos
Funçõesdecaracteresedecálculostambémpodemserusadasnasexpressões
SQL.Atravésdelaspodem-semodificarosdados,tantonoquedizrespeito
aosvaloresselecionados,comotambémnaformaquesãoapresentados,por
exemplo,separarinformaçõesdentrodeumadeterminadaString,concatenar
caracteres,definiracaixadasletras(maiúsculas,minúsculaseintercaladas)
etc.
Jáosoperadoresaritméticospodemserutilizadosparaainser çãodecál-
culosdentrodoscomandosSQL.Cálculosestesreferentesàsoma,subtraç ão,
divisãoemultiplicaç ão.Valesalientarqueestasfun çõeseoperadorespodem
serutilizadosemqualquercláusulaSQLexcetonacláusula from.

## Página 155

11.1. Funçõesdecaracteres CasadoCódigo
11.1 F unções de caracteres
•INITCAP:retornaoprimeirocaracteredecadapalavraemmaiúscula.
•LOWER:for çacaracteresmaiúsculosaparecerememminúsculos.
•UPPER:for çacaracteresminúsculosaparecerememmaiúsculos.
•SUBSTR:extraiumtrechodeumastring,come çandoporumaposiç ão
inicialeapartirdestaposiç ãocontacombasenaquantidadesolicitada.
•to_char:converteumvalornuméricoparaumastringdecaracteres.
Tambéméutilizadaparainserirmáscaraemcamposnuméricosede
data.
•INSTR:retornaaposiç ãodoprimeirocaractereencontrado,passado
comoparâmetro.
•LENGTH:trazotamanhodoscaracteresembytes.
•RPAD:fazalinhamentoàesquerdaepreenchecomcaracteresàdireita,
atéumadeterminadaposiç ão. Ambososvaloressãopassadoscomo
parâmetro.
•LPAD:fazalinhamentoàdireitaepreenchecomcaracteresàesquerda,
atéumadeterminadaposiç ão. Ambososvaloressãopassadoscomo
parâmetro.
Seguemexemplosdousodestasfun ções:
SQL> declare
2 --
3 wnome1 varchar2(100) default 'analista de sistemas';
4 wnome2 varchar2(100) default 'PEDREIRO';
5 wnome3 varchar2(100) default 'padeiro';
6 --
7 begin
8 --
9 wnome1 := initcap(wnome1);
10 wnome2 := lower(wnome2);
144

## Página 156

CasadoCódigo Capítulo11. Funçõesdecaractereseoperadoresaritméticos
11 wnome3 := upper(wnome3);
12 --
13 dbms_output.put_line(wnome1);
14 dbms_output.put_line(wnome2);
15 dbms_output.put_line(wnome3);
16 --
17 end;
18 /
Analista De Sistemas
pedreiro
PADEIRO
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodasfun ções initcap, lowere upper.
Notequeosvaloresiniciaisdasvariáveis wnome1, wnome2e wnome3são
alteradosconformeaaç ãodecadafun ção.
SQL> select * from regions;
REGION_ID REGION_NAME
--------- -------------------------
1 Europe
2 Americas
3 Asia
4 Middle East and Africa
SQL> declare
2 wregion_name_short varchar2(500);
3 begin
4 --
5 for r1 in (select region_name from regions) loop
6 --
7 wregion_name_short := upper(substr(r1.region_name,1,2));
8 --
9 dbms_output.put_line(wregion_name_short);
10 --
145

## Página 157

11.1. Funçõesdecaracteres CasadoCódigo
11 end loop;
12 --
13 end;
14 /
EU
AM
AS
MI
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodasfun ções substre upper. Oexemplo
retornaosnomesdasregiõesmostrandoapenaspartedastringreferentea
estesnomes.
SQL> declare
2 wsalario varchar2(200);
3 begin
4 --
5 for r1 in (select ename, sal from emp where comm is
null) loop
6 --
7 wsalario := 'R$ '||to_char(r1.sal,'fm999G990D00');
8 --
9 dbms_output.put_line('Nome: '||r1.ename||'
Salário: '||wsalario);
10 --
11 end loop;
12 --
13 end;
14 /
Nome: SMITH Salário: R$ 800.00
Nome: JONES Salário: R$ 2 ,975.00
Nome: BLAKE Salário: R$ 2 ,850.00
Nome: CLARK Salário: R$ 2 ,450.00
Nome: SCOTT Salário: R$ 3 ,000.00
Nome: KING Salário: R$ 5, 000.00
Nome: ADAMS Salário: R$ 1 ,100.00
146

## Página 158

CasadoCódigo Capítulo11. Funçõesdecaractereseoperadoresaritméticos
Nome: JAMES Salário: R$ 950.00
Nome: FORD Salário: R$ 3, 000.00
Nome: MILLER Salário: R$ 1,300.00
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodafun ção to_char.Afun çãofoiutilizada
paraformatarosvaloresdacoluna SAL(salários).
SQL> declare
2 valor number;
3 begin
4 --
5 valor := instr(37462.12,'62');
6 --
7 dbms_output.put_line('Posição: '||valor);
8 --
9 end;
10 /
Posição: 4
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodafun ção instr.
SQL> begin
2 --
3 for r1 in (select first_name from employees where
length(first_name) > 10) loop
4 --
5 dbms_output.put_line('Nome: '||r1.first_name);
6 --
7 end loop;
8 --
9 end;
10 /
147

## Página 159

11.1. Funçõesdecaracteres CasadoCódigo
Nome: Christopher
Nome: Jose Manuel
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodafun ção length.
SQL> declare
2 wlast_name varchar2(200 );
3 wsalary varchar2(50);
4 begin
5 --
6 for r1 in (select last_name, salary
7 from employees where department_id = 30) loop
8 --
9 wlast_name := rpad(r1.last_name, 12,'++++');
10 wsalary := lpad(r1.salary,7,'0');
11 --
12 dbms_output.put_line('Último Nome: '||wlast_name||'
Salário: '||wsalary);
13 --
14 end loop;
15 --
16 end;
17 /
Último Nome: Raphaely++++ Salário: 0011000
Último Nome: Khoo++++++++ Salário: 0003100
Último Nome: Baida +++++++ Salário: 0002900
Último Nome: Tobias++++++ Salário: 0002800
Último Nome: Himuro++++++ Salário: 0002600
Último Nome: Colmenares++ Salário: 0002500
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodasfun ções rpade lpad.
148

## Página 160

CasadoCódigo Capítulo11. Funçõesdecaractereseoperadoresaritméticos
11.2 F unções de cálculos
•ROUND:arredondavalorescomcasasdecimais.
•TRUNC:truncavalorescomcasasdecimais.
•MOD:mostraorestodadivisãodedoisvalores.
•SQRT:retornaaraizquadradadeumvalor.
•POWER:retornaumvalorelevadoaoutrovalor.
•ABS:retornaovalorabsoluto.
•CEIL:retornaomenorinteiro,maiorouigualavalor.
•FLOOR:retornaomaiorinteiro,menorouigualavalor.
•SIGN:sevalormaiorque0retornar+1.Sevalormenorque0retornar
-1.Sevaloriguala0retorna0.
SQL> declare
2 wsal_calc number;
3 wcomm number;
4 begin
5 --
6 for r1 in (select sal, ename from emp where
deptno = 20) loop
7 --
8 wsal_calc := (r1.sal / 2.7);
9 --
10 dbms_output.put_line('Nome: '||r1.ename||'
Salário: '||wsal_calc);
11 --
12 end loop;
13 --
14 dbms_output.put_line('-');
15 --
16 for r1 in (select comm, ename from emp where comm is
not null) loop
17 --
149

## Página 161

11.2. Funçõesdecálculos CasadoCódigo
18 wcomm := round((r1.comm / 2.7));
19 --
20 dbms_output.put_line('Nome: '||r1.ename||'
Comissão: '||wcomm);
21 --
22 end loop;
23 --
24 dbms_output.put_line('-');
25 --
26 for r1 in (select sal, ename
27 from emp where empno between 7500 and 7700) loop
28 --
29 wsal_calc := round((r1.sal / 2.7),2);
30 --
31 dbms_output.put_line('Nome: '||r1.ename||' Salário: '||
32 r1.sal||' Salário Calc: '||wsal_calc);
33 --
34 end loop;
35 --
36 end;
37 /
Nome: SMITH Salário: 296.296296296296296296296296296296296296
Nome: JONES Salário: 1101.851851851851851851851851851851851852
Nome: SCOTT Salário: 1111.111111111111111111111111111111111111
Nome: ADAMS Salário: 407.407407407407407407407407407407407407
Nome: FORD Salário: 1111.111111111111111111111111111111111111
-
Nome: ALLEN Comissão: 111
Nome: WARD Comissão: 185
Nome: MARTIN Comissão: 519
Nome: TURNER Comissão: 0
-
Nome: WARD Salário: 1250 Salário Calc: 462.96
Nome: JONES Salário: 2975 Salário Calc: 1101.85
Nome: MARTIN Salário: 1250 Salário Calc: 462.96
Nome: BLAKE Salário: 2850 Salário Calc: 1055.56
PL/SQL procedure successfully completed.
150

## Página 162

CasadoCódigo Capítulo11. Funçõesdecaractereseoperadoresaritméticos
SQL>
Esseexemplomostraousodafun ção round.Noexemplo,sãomostradas
diferentesformasdechamadaaestafun ção.
SQL> declare
2 wsal_calc number;
3 begin
4 --
5 for r1 in (select first_name, salary, job_id
6 from employees where job_id = 'MK_MAN') loop
7 --
8 wsal_calc := (r1.salary / 2.7);
9 --
10 dbms_output.put_line('Nome: '||r1.first_name||'
Salário Calc.: '||
11 wsal_calc||' Salário: '||r1.salary
||' Job: '||r1.job_id);
12 --
13 end loop;
14 --
15 dbms_output.put_line('-');
16 --
17 for r1 in (select last_name, salary, email
18 from employees where email = 'NSARCHAN') loop
19 --
20 wsal_calc := trunc((r1.salary / 2.7));
21 --
22 dbms_output.put_line('Nome: '||r1.last_name||'
Sal. Calc: '||wsal_calc||
23 ' Sal. : '||r1.salary||'
Email. : '||r1.email);
24 --
25 end loop;
26 --
27 dbms_output.put_line('-');
28 --
29 for r1 in (select last_name, salary
30 from employees where employee_id between 100
151

## Página 163

11.2. Funçõesdecálculos CasadoCódigo
and 105) loop
31 --
32 wsal_calc := trunc((r1.salary / 2.7),2 );
33 --
34 dbms_output.put_line('Nome: '||r1.last_name||'
Sal. Calc: '||wsal_calc||
35 ' Sal. : '||r1.salary);
36 --
37 end loop;
38 --
39 end;
40 /
Nome: Michael Salário Calc.:
4814.814814814814814814814814814814814815 Salário:
13000 Job: MK_MAN
-
Nome: Sarchand Sal. Calc: 1555 Sal. : 4200 Email. : NSARCHAN
-
Nome: King Sal. Calc: 8888.88 Sal. : 24000
Nome: Kochhar Sal. Calc: 6296.29 Sal. : 17000
Nome: De Haan Sal. Calc: 6296 .29 Sal. : 17000
Nome: Hunold Sal. Calc: 3333.33 Sal. : 9000
Nome: Ernst Sal. Calc: 2222.22 Sal. : 6000
Nome: Austin Sal. Calc: 1777.77 Sal. : 4800
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodafun ção trunc.Noexemplo,sãomostradas
diferentesformasdechamadaaestafun ção.
SQL> declare
2 wres number;
3 begin
4 --
5 wres := mod(10,2);
6 dbms_output.put_line('Resultado: '||wres);
7 --
152

## Página 164

CasadoCódigo Capítulo11. Funçõesdecaractereseoperadoresaritméticos
8 wres := sqrt(64);
9 dbms_output.put_line('Resultado: '||wres);
10 --
11 wres := power(8,2);
12 dbms_output.put_line('Resultado: '||wres);
13 --
14 end;
15 /
Resultado: 0
Resultado: 8
Resultado: 64
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodasfun ções mod, sqrte power.
SQL> declare
2 wres number;
3 begin
4 --
5 wres := abs(-20);
6 dbms_output.put_line('Resultado: '||wres);
7 --
8 wres := ceil(10.2);
9 dbms_output.put_line('Resultado: '||wres);
10 --
11 wres := floor(10.2);
12 dbms_output.put_line('Resultado: '||wres);
13 --
14 end;
15 /
Resultado: 20
Resultado: 11
Resultado: 10
PL/SQL procedure successfully completed.
SQL>
153

## Página 165

11.3. Operadoresaritméticos CasadoCódigo
Nesseexemploémostradoousodasfun ções abs, ceile floor.
SQL> declare
2 wres number;
3 begin
4 --
5 wres := sign(-2000);
6 dbms_output.put_line('Resultado: '||wres);
7 --
8 wres := sign(2000);
9 dbms_output.put_line('Resultado: '||wres);
10 --
11 wres := sign(0);
12 dbms_output.put_line('Resultado: '||wres);
13 --
14 end;
15 /
Resultado: -1
Resultado: 1
Resultado: 0
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodafun ção sign.Noexemplo,sãomostrados
diferentesparâmetrosnachamadadestafun ção.
11.3 O peradores aritméticos
•*Multiplicação
•/Divisão
•+Adição
•-Subtração
SQL> declare
2 wsal_calc number;
154

## Página 166

CasadoCódigo Capítulo11. Funçõesdecaractereseoperadoresaritméticos
3 begin
4 --
5 for r1 in (select sal from emp where comm is not null) loop
6 --
7 wsal_calc := (r1.sal*2/3);
8 --
9 dbms_output.put_line('Salário Calc.: '||wsal_calc||'
Salário: '||r1.sal);
10 --
11 end loop;
12 --
13 end;
14 /
Salário Calc.: 1066.666666666666666666666666666666666667
Salário: 1600
Salário Calc.: 833 .333333333333333333333333333333333333
Salário: 1250
Salário Calc.: 833 .333333333333333333333333333333333333
Salário: 1250
Salário Calc.: 1000 Salário: 1500
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodasfun çõesaritméticasdemultiplicaç ãoe
divisão.
SQL> declare
2 --
3 wsal_calc number;
4 --
5 begin
6 --
7 for r1 in (select ename, sal
8 from emp where deptno = 30) loop
9 --
10 wsal_calc := round((r1.sal*2)/3+100.00,2);
11 --
155

## Página 167

11.3. Operadoresaritméticos CasadoCódigo
12 dbms_output.put_line('Nome: '||r1.ename||'
Salário Calc.: '||
13 wsal_calc||' Salário: '||r1.sal);
14 --
15 end loop;
16 --
17 end;
18 /
Nome: ALLEN Salário Calc.: 1166.67 Salário: 1600
Nome: WARD Salário Calc.: 933.33 Salário: 1250
Nome: MARTIN Salário Calc.: 933.33 Salário: 1250
Nome: BLAKE Salário Calc.: 2000 Salário: 2850
Nome: TURNER Salário Calc.: 1100 Salário: 1500
Nome: JAMES Salário Calc.: 733.33 Salário: 950
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodasfun çõesaritméticasdemultiplicaç ão,di-
visãoesoma.
SQL> declare
2 --
3 wdt_emissao number;
4 wpremiacao number;
5 --
6 cursor c1 is
7 select ename
8 ,dname
9 ,hiredate
10 ,sal
11 from emp e
12 ,dept d
13 where e.deptno = d.deptno
14 and trunc((sysdate - hiredate) / 365) = 30;
15 --
16 begin
17 --
156

## Página 168

CasadoCódigo Capítulo11. Funçõesdecaractereseoperadoresaritméticos
18 for r1 in c1 loop
19 --
20 wdt_emissao := trunc((sysdate - r1.hiredate) / 365);
21 wpremiacao :=
(r1.sal/10*trunc((sysdate - r1.hiredate) / 365));
22 --
23 dbms_output.put_line('Nome: '||r1.ename||'
Dt. Emissão: '||
24 wdt_emissao||' Premiação:
'||wpremiacao);
25 --
26 end loop;
27 --
28 end;
29 /
Nome: KING Dt. Emissão: 30 Premiação: 15000
Nome: CLARK Dt. Emissão: 30 Premiação: 7350
Nome: FORD Dt. Emissão: 30 Premiação: 9000
Nome: JONES Dt. Emissão: 30 Premiação: 8925
Nome: SMITH Dt. Emissão: 30 Premiação: 2400
Nome: JAMES Dt. Emissão: 30 Premiação: 2850
Nome: TURNER Dt. Emissão: 30 Premiação: 4500
Nome: BLAKE Dt. Emissão: 30 Premiação: 8550
Nome: MARTIN Dt. Emissão: 30 Premiação: 3750
Nome: WARD Dt. Emissão: 30 Premiação: 3750
Nome: ALLEN Dt. Emissão: 30 Premiação: 4800
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodasfun çõesaritméticasdemultiplicaç ão,di-
visãoesubtraç ão.
157

## Página 170

Capítulo12
Funçõesdeagregaç ão(grupo)
Asfun çõesdeagregaç ãosãoresponsáveisporagruparváriosvaloresere-
tornarsomenteumúnicovalorparaumdeterminadogrupo.Asfun çõesde
agregação,tambémchamadasdefun çõesdegrupo,sãoespecificadasnoco-
mando selectdeumacolunaesãoseguidaspelacolunaàqualseapli-
cam.Autilizaç ãodasfun çõesdeagregaç ãopodeimplicarnousodacláusula
group by.Issoaconteceporque,aoinformarmoscolunascomfun çõeseco-
lunassemfun çõesemummesmo select,precisamosagruparascolunas
quenãoestãosendoafetadaspeloagrupamentocausadopelasfun ções.Veja
ailustração:

## Página 171

CasadoCódigo
Fig.12.1:Dadosdeempregados
Nestailustração,temosalgunsempregados,departamentosevaloresde
salário.Nossoobjetivoaquiétentardealgumaformasomartodosossalários
pordepartamento,ouseja,verquantodesaláriotemosparaosempregados
referentesaosdepartamentos RESEARCH, SALESe ACCOUNTING.Daforma
comoosdadosestãodispostos,nãoconseguimosvisualizaristo,poisseten-
tarmosagrupardepartamento,nãoconseguiremos,vistoqueoagrupamento
consisteemselecionardadosquepossuemomesmovaloretorná-loúnico
paracadaconjuntodedados.
Por exemplo, temos os departamentos RESEARCH, SALES e
ACCOUNTING aparecendo diversas vezes. Se agruparmos, teremos um
único registro para o departamentoRESEARCH, outro para SALES, e
outro para ACCOUNTING. Entretanto, também estamos selecionando os
nomesdosempregadose,namaioriadoscasos,cadaumpossuiumnome
deferente,impossibilitandoqueosagrupemos.Senãoconseguimosagrupar
osempregados,logonãoconseguimosagruparosdepartamentos.Écomose
fosseumasequência.Quandousamosfun çõesdegruponascolunasdeum
select,temosqueagrupartodasasoutras,sendoatravésdeumafun çãode
agregaçãoousendopelousodo group by.
Jávimosquesenósquisermosasomatóriadetodosossaláriospordepar-
tamentonãopodemosselecionarosempregados,oumelhor,osnomesdeles.
160

## Página 172

CasadoCódigo Capítulo12. Funçõesdeagregaç ão(grupo)
Logo,acoluna Empregadonãopoderáaparecernonosso select. Caso
contrário,estaríamosincluindotambémporempregados,oquenosdariaum
agrupamentoinútil,tendoemvistaquecadanomedeempregadoédiferente.
Semprequandotrabalhamoscomagrupamentos,temosqueteremmente
aseguintesituaç ão:vaihavercolunasqueestarãosobreoefeitodasfun ções
deagregação,porexemplo,fun çõesdesomatóriaoudemédia,ecolunasque
nãoestarãosobreoefeitodestasfun ções,masqueprecisarãoseragrupadas
paraquejuntaspossamformarumconjuntodedados.
Vejaapróximailustraç ão:
Fig.12.2:Dadosagrupadosparcialmente
Nessaoutrailustraç ão,temosdoisgrupos.Umgrupoformadopelasco-
lunas Empregadoe Departamento,quesofrerãoaaç ãodo group by,
eoutrogrupoformadoapenaspelacoluna Salário,quesofreráaaç ãoda
nossafun çãodeagregaç ão.Valeressaltarquenossoobjetivoaquiéagrupar
ossaláriospordepartamento.
Poisbem,comopodeservistonailustraç ão,nestecaso,nãoconsegui-
mosmontaroagrupamento.Notequenacolunadedepartamentoépossível
161

## Página 173

CasadoCódigo
agruparosvalores,masnacolunadeempregadosissonãoépossível.Comoa
colunadeempregadosfazpartedo select,elaacabacomprometendotodo
nossoagrupamento.Aten çãoaumdetalhe–ofatodeacoluna Empregado
estarsendovisualizadaprimeironãoquerdizerquesejaacausadenãocon-
seguirmosagruparpordepartamento.Aordemdascolunasnãoalteraore-
sultado.Vamosretirá-ladonosso select.
Fig.12.3:Processodeagrupamentodesaláriospordepartamento
Agorasim. Tiramosacolunadeempregadoseficamosapenascomas
colunas Departamentoe Salário.
Vejacomoficounossoagrupamento:
162

## Página 174

CasadoCódigo Capítulo12. Funçõesdeagregaç ão(grupo)
Fig.12.4:Dadosagrupados-SaláriosxDepartamento
Fazendo desta forma conseguiremos alcançar nosso objetivo. Resu-
mindo:
• Devemossaberqueparaobtersucessoemnossosagrupamentos,as
colunasquenãoestãosendoagrupadaspelasfun çõesdeagrupamento
devemseragrupadaspelo group by;
• Tambémpodemosagrupardeterminadascolunas,mesmoqueelasnão
estejampresentesnacláusula select;
• Somente vamos precisar agrupar colunas através dogroup by
quandodesejarmosmostrarumresultadocombaseemoutro.Exem-
plo:valoresdesaláriopordepartamento,quantidadesdeempregados
pordepartamentoeassimpordiante.Sequisermosapenassaberaso-
matóriadetodososvaloresdesalárioindependentedodepartamento
oudequalqueroutrainformaç ão,nãoprecisaremosutilizaro group
by;
• Funçõesdeagregaç ão,nogeral,ignoramvaloresnulos;
• PararealizaroagrupamentodeinformaçõesoOraclepoderáordenar
ounãoascolunas.Casoacolunaqueestásobreaaç ãodafun çãofor
umacolunacomíndice,obancopoderáutilizaresteíndice.Comoos
163

## Página 175

CasadoCódigo
índicessãoordenados,nãoseránecessárioordenarosdadosparao
agrupamento.Casocontrário,elevairealizaraordenaç ão,primeiro,e
depoisagrupa.Nemtodasasfun çõespermitemusaríndices.
Agoravamosverestesconceitosnaprática.
Primeiramente,visualizamosonomedetodososempregados,osnomes
dosseusdepartamentoseseusrespectivossalários.
SQL> select ename, dname, sal
2 from emp e, dept d
3 where e.deptno = d.deptno
4 order by ename;
ENAME DNAME SAL
---------- -------------- ---------
ADAMS RESEARCH 1100
ALLEN SALES 1600
BLAKE SALES 2850
CLARK ACCOUNTING 2450
FORD RESEARCH 3000
JAMES SALES 950
JOHN RESEARCH 1000
JONES RESEARCH 2975
KING ACCOUNTING 5000
MARTIN SALES 1250
MILLER ACCOUNTING 1300
SCOTT RESEARCH 3000
SMITH RESEARCH 800
TURNER SALES 1500
WARD SALES 1250
15 rows selected.
SQL>
AtravésdeumprogramaPL/SQLselecionamososmesmosdadosdo
selectanterior,masagorasumarizandoossalários.Notequecontinuamos
selecionandoascolunasnomedoempregadoedepartamentodoempregado.
Oobjetivodoprogramaémostrarasomadossaláriospordepartamento.
164

## Página 176

CasadoCódigo Capítulo12. Funçõesdeagregaç ão(grupo)
SQL> declare
2 --
3 cursor c1 is
4 select ename, dname, sum(sal) soma_sal
5 from emp e, dept d
6 where e.deptno = d.deptno
7 order by ename;
8 --
9 begin
10 --
11 for r1 in c1 loop
12 --
13 dbms_output.put_line('Nome: '||r1.ename||'
Departamento: '||
14 r1.dname||'
Soma Sal.: '||r1.soma_sal);
15 --
16 end loop;
17 --
18 end;
19 /
declare
*
ERROR at line 1:
ORA-00937: not a single-group group function
ORA-06512: at line 4
ORA-06512: at line 11
SQL>
Aoexecutaroprograma,surgiuumerroque,emlinhasgerais,querdizer
queocomando select,contidonocursor,estátentandoutilizarumafun-
çãodegrupo,juntamentecomoutrascolunasnãoagrupadas,semutilizara
cláusuladeagrupamento. Comovistonosconceitosapresentadosanterior-
mente,issonãoépermitido.Dessaforma,devemosagruparascolunasque
nãoestãoassociadasafun çõesdeagrupamento.Vejaaseguircomoficou.
SQL> declare
2 --
165

## Página 177

CasadoCódigo
3 cursor c1 is
4 select ename, dname, sum(sal) soma_sal
5 from emp e, dept d
6 where e.deptno = d.deptno
7 group by ename, dname
8 order by ename;
9 --
10 begin
11 --
12 for r1 in c1 loop
13 --
14 dbms_output.put_line('Nome: '||r1.ename||'
Departamento: '||
15 r1.dname||'
Soma Sal.: '||r1.soma_sal);
16 --
17 end loop;
18 --
19 end;
20 /
Nome: ADAMS Departamento: RESEARCH Soma Sal.: 1100
Nome: ALLEN Departamento: SALES Soma Sal.: 1600
Nome: BLAKE Departamento: SALES Soma Sal.: 2850
Nome: CLARK Departamento: ACCOUNTING Soma Sal.: 2450
Nome: FORD Departamento: RESEARCH Soma Sal.: 3000
Nome: JAMES Departamento: SALES Soma Sal.: 950
Nome: JONES Departamento: RESEARCH Soma Sal.: 2975
Nome: KING Departamento: ACCOUNTING Soma Sal.: 5000
Nome: MARTIN Departamento: SALES Soma Sal.: 1250
Nome: MILLER Departamento: ACCOUNTING Soma Sal.: 1300
Nome: SCOTT Departamento: RESEARCH Soma Sal.: 3000
Nome: SMITH Departamento: RESEARCH Soma Sal.: 800
Nome: TURNER Departamento: SALES Soma Sal.: 1500
Nome: WARD Departamento: SALES Soma Sal.: 1250
PL/SQL procedure successfully completed.
SQL>
166

## Página 178

CasadoCódigo Capítulo12. Funçõesdeagregaç ão(grupo)
Feitososagrupamentosnecessários,voltamosaexecutaroprograma.O
resultadofoiapresentadologoemseguida.Noentanto,vejaquealgonãosaiu
comodeveria.Ossaláriosnãoforamsumarizadospordepartamentoe,sim,
porempregado. Seriaamesmacoisaquenãosumarizar. Vamosalteraro
comandoretirandoacolunanomedoempregadodocomandoSQL.
SQL> declare
2 --
3 cursor c1 is
4 select dname, sum(sal) soma_sal
5 from emp e, dept d
6 where e.deptno = d.deptno
7 group by ename, dname
8 order by ename;
9 --
10 begin
11 --
12 for r1 in c1 loop
13 --
14 dbms_output.put_line('Departamento: '||
15 r1.dname||' Soma Sal.: '||r1.soma_sal);
16 --
17 end loop;
18 --
19 end;
20 /
Departamento: RESEARCH Soma Sal.: 1100
Departamento: SALES Soma Sal.: 1600
Departamento: SALES Soma Sal.: 2850
Departamento: ACCOUNTING Soma Sal.: 2450
Departamento: RESEARCH Soma Sal.: 3000
Departamento: SALES Soma Sal.: 950
Departamento: RESEARCH Soma Sal.: 2975
Departamento: ACCOUNTING Soma Sal.: 5000
Departamento: SALES Soma Sal.: 1250
Departamento: ACCOUNTING Soma Sal.: 1300
Departamento: RESEARCH Soma Sal.: 3000
Departamento: RESEARCH Soma Sal.: 800
Departamento: SALES Soma Sal.: 1500
167

## Página 179

CasadoCódigo
Departamento: SALES Soma Sal.: 1250
PL/SQL procedure successfully completed.
SQL>
Aoretiraracoluna,oerropersiste.Issoacontecepoisnãoadiantaretirar
apenasdasele ção,mastambéménecessárioretirardoagrupamento. Veja
quenalinha7aindaconstaacoluna ename.Vejaaseguir,comodeveficaro
select,paraqueoprogramaconsigaatingiroobjetivoproposto.
SQL> declare
2 --
3 cursor c1 is
4 select dname, sum(sal) soma_sal
5 from emp e, dept d
6 where e.deptno = d.deptno
7 group by dname;
8 --
9 begin
10 --
11 for r1 in c1 loop
12 --
13 dbms_output.put_line('Departamento: '||
14 r1.dname||' Soma Sal.: '||r1.soma_sal);
15 --
16 end loop;
17 --
18 end;
19 /
Departamento: ACCOUNTING Soma Sal.: 8750
Departamento: RESEARCH Soma Sal.: 10875
Departamento: SALES Soma Sal.: 9400
PL/SQL procedure successfully completed.
SQL>
Selecionandoapenasacolunareferenteaonomedodepartamentoesu-
168

## Página 180

CasadoCódigo Capítulo12. Funçõesdeagregaç ão(grupo)
marizandoossalários,atravésdafun çãodeagregaç ão sum,temoscomore-
sultadoasomadossaláriospordepartamento.
Segueasfun çõesdeagregaç ãomaisutilizadas:
•count:retornaaquantidadedeincidênciasderegistros.
•sum:exibeasomadosvaloresdosregistros.
•avg:exibeamédiadosvaloresdeumadeterminadacoluna.
•min:exibeomenorvalordeumacoluna.
•max:retornaomaiorvalordeumacoluna.
SQL> declare
2 --
3 cursor c1 is
4 select count(employee_id) cont_emp, country_name
5 from employees e
6 ,departments d
7 ,locations l
8 ,countries c
9 where e.department_id = d.department_id
10 and d.location_id = l.location_id
11 and l.country_id = c.country_id
12 group by country_name
13 order by country_name;
14 --
15 begin
16 --
17 for r1 in c1 loop
18 --
19 dbms_output.put_line('Qtde. Empregados: '||
20 r1.cont_emp||' Cidade: '||r1.country_name);
21 --
22 end loop;
23 --
24 end;
25 /
Qtde. Empregados: 2 Cidade: Canada
169

## Página 181

CasadoCódigo
Qtde. Empregados: 1 Cidade: Germany
Qtde. Empregados: 35 Cidade: United Kingdom
Qtde. Empregados: 68 Cidade: United States of America
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodafun ção: count.Noexemplo,oobjetivoé
selecionaraquantidadedeempregadosporpaís.
SQL> declare
2 --
3 cursor c1 is
4 select count(*) cont_emp, country_name
5 from employees e
6 ,departments d
7 ,locations l
8 ,countries c
9 where e.department_id = d.department_id
10 and d.location_id = l.location_id
11 and l.country_id = c.country_id
12 group by country_name
13 order by country_name;
14 --
15 begin
16 --
17 for r1 in c1 loop
18 --
19 dbms_output.put_line('Qtde. Empregados: '||
20 r1.cont_emp||' Cidade: ' ||r1.country_name);
21 --
22 end loop;
23 --
24 end;
25 /
Qtde. Empregados: 2 Cidade: Canada
Qtde. Empregados: 1 Cidade: Germany
Qtde. Empregados: 35 Cidade: United Kingdom
170

## Página 182

CasadoCódigo Capítulo12. Funçõesdeagregaç ão(grupo)
Qtde. Empregados: 68 Cidade: United States of America
PL/SQL procedure successfully completed.
SQL>
Esseexemploéquaseigualaoanterior,apenasporumdetalhe.Noteque
comoconhecemosatabela employeesesabemosqueexisteapenasumre-
gistroparacadaempregado,podemosusarafun ção countdeoutraforma,
utilizandoasterisco( *)nolugardacoluna employee_id.
SQL> declare
2 --
3 cursor c1 is
4 select dname, max(hiredate) dt_admissao
5 from emp e, dept d
6 where e.deptno = d.deptno
7 group by dname
8 order by 2 desc ;
9 --
10 begin
11 --
12 for r1 in c1 loop
13 --
14 dbms_output.put_line('Departamento: '||
15 r1.dname||' Dt. Admissão: '||r1.dt_admissao);
16 --
17 end loop;
18 --
19 end;
20 /
Departamento: RESEARCH Dt. Admissão: 12-JAN-83
Departamento: ACCOUNTING Dt. Admissão: 23-JAN-82
Departamento: SALES Dt. Admissão: 03-DEC-81
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodafun ção: max. Noexemplo,oobjetivoé
171

## Página 183

CasadoCódigo
selecionaramaiordatadeadmissãodecadadepartamento.
SQL> declare
2 wres date;
3 begin
4 select min(hire_date) hire_date_min into wres
from employees;
5 --
6 dbms_output.put_line('Menor Dt. Emissão: '||wres);
7 --
8 end;
9 /
Menor Dt. Emissão: 17- JUN-87
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostraousodafun ção: min. Oobjetivoéselecionara
menordatadeadmissãoentretodososempregados.
Alémdasfun çõesdeagregaç ãoedousodo group by,tambémpode-
moscontarcomo having,paranosajudararestringirregistroscombase
nosvaloresretornadospelasfun çõesdeagregaç ão.O havingexistepoisnão
podemosutilizarfun çõesdeagregaç ãonacláusula where.
SQL> declare
2 --
3 cursor c1 is
4 select count(employee_id) cont_emp, sum(salary)
soma_salario, department_name
5 from employees e
6 ,departments d
7 where e.department_id = d.department_id
8 having count(employee_id) > 5
9 group by department_name
10 order by department_name;
11 --
12 begin
13 --
172

## Página 184

CasadoCódigo Capítulo12. Funçõesdeagregaç ão(grupo)
14 for r1 in c1 loop
15 --
16 dbms_output.put_line('Qtde. Empregado: '||
17 r1.cont_emp||' Soma Sal.: '||r1.soma_salario||
18 ' Depto.: '||r1.department_name);
19 --
20 end loop;
21 --
22 end;
23 /
Qtde. Empregado: 6 Soma Sal.: 51600 Depto.: Finance
Qtde. Empregado: 6 Soma Sal.: 24900 Depto.: Purchasing
Qtde. Empregado: 34 Soma Sal.: 304500 Depto.: Sales
Qtde. Empregado: 45 Soma Sal.: 156400 Depto.: Shipping
PL/SQL procedure successfully completed.
SQL>
Nesseexemplo,émostradoousodacláusula having.Oobjetivoése-
lecionaraquantidadedeempregadoseasomadossalários,agrupadospor
departamento,ondeaquantidadedeempregadosémaiorque5.Observeque
acláusula havingatuasomenteapósoagrupamentodaslinhas. Porisso,
nãoseriapossívelutilizaracláusula where,poiselaatuanomomentoem
queaslinhasestãosendoselecionadas,ouseja,antesdoagrupamento.
SQL> declare
2 --
3 cursor c1 is
4 select department_name, sum(salary) soma_sal,
country_name
5 from employees e
6 ,departments d
7 ,locations l
8 ,countries c
9 where e.department_id = d.department_id
10 and d.location_id = l.location_id
11 and l.country_id = c.country_id
12 having sum(salary) > (select avg(em.salary)
173

## Página 185

CasadoCódigo
13 from employees em
14 ,departments dm
15 ,locations lm
16 ,countries cm
17 where em.department_id = dm.department_id
18 and dm.location_id = lm.location_id
19 and lm.country_id = cm.country_id
20 and cm.country_id = c.country_id)
21 group by c.country_id
22 ,department_name
23 ,country_name
24 order by country_name
25 ,department_name;
26 --
27 begin
28 --
29 for r1 in c1 loop
30 --
31 dbms_output.put_line('Departamento: '||
32 r1.department_name||'
Soma Sal.: '||r1.soma_sal||
33 ' Cidade: '||r1.country_name);
34 --
35 end loop;
36 --
37 end;
38 /
Departamento: Marketing Soma Sal.: 19000 Cidade: Canada
Departamento: Sales Soma Sal.: 304500 Cidade: United Kingdom
Departamento: Accounting Soma Sal.: 20300 Cidade: United States
of America
Departamento: Executive Soma Sal.: 58000 Cidade: United States
of America
Departamento: Finance Soma Sal.: 51600 Cidade: United States
of America
Departamento: IT Soma Sal.: 28800 Cidade: United States
of America
Departamento: Purchasing Soma Sal.: 24900 Cidade: United States
of America
174

## Página 186

CasadoCódigo Capítulo12. Funçõesdeagregaç ão(grupo)
Departamento: Shipping Soma Sal.: 156400 Cidade: United States
of America
PL/SQL procedure successfully completed.
SQL>
Jánesseoutroexemplo,oobjetivoéselecionarasomadossalários,agru-
padospordepartamentoepaís,cujasejamaiorqueamédiadossaláriospor
país.
175

## Página 188

Capítulo13
Funçõesdedata
Funçõesdedatasãoutilizadasparamanipularmosvaloresdotipo date,
comoaplicarformataçõesparaumavisualizaç ãomaisrefinada,ouextrair
partesdeumadata,comoashoras,diadomêsousomenteoano. Seguem
algumasdelas:
•add_months:adicionamesesemumadeterminadadata.
•months_between:retornaaquantidadedemesesentreduasdatas.
•next_day:procuraopróximodiaapósumadatainformada.
•last_day:retornaoúltimodiadomêscombaseemumadatainfor-
mada.
•trunc:truncaumadatapassadaporparâmetro. O truncpodeser
feitopordiaemês,utilizandooparâmetro FMT(formato).

## Página 189

CasadoCódigo
•sysdate:retornaadatacorrentecombasenoservidordobancode
dados.
•sessiontimezone:mostraofusohoráriocombasenasessãoaberta
nobancodedados,mediantesualocalizaç ão.Valelembrarqueosfusos
horáriossãocalculadoscombasenomeridianodeGreenwich.
•current_date:mostraadatacorrentecombasenazonadetempo
dasessãodousuário.Azonadetempoéafetadaemrelaç ãoaoMeridi-
ano.Casonãohajamudan çasdezona,estafun çãoteráomesmovalor
que sysdate. sysdatebuscaahoradoservidordobancodeda-
dos;mesmoqueasessãotenhasidoabertaemumazonadiferenteda
qualoservidorencontra-se,elerefletiráohoráriodazonaondeestáo
servidor.Jáo current_daterefletiráazonaondefoiabertaasessão.
SQL> declare
2 --
3 wdt_admissao date;
4 wsexta date;
5 --
6 cursor c1 is
7 select first_name
8 ,hire_date
9 from employees
10 where to_char(hire_date,'mm') = to_char(sysdate,'mm')
11 order by 2;
12 --
13 begin
14 --
15 for r1 in c1 loop
16 --
17 wdt_admissao := to_date(to_char(
r1.hire_date,'dd/mm')||'/'||
18 to_char(sysdate,'rrrr'),'dd/mm/rrrr');
19 wsexta := next_day(to_date(
to_char(r1.hire_date,'dd/mm')||'/'
20 ||to_char(sysdate,'rrrr'),'dd/mm/rrrr')
,'FRIDAY');
178

## Página 190

CasadoCódigo Capítulo13. Funçõesdedata
21 --
22 dbms_output.put_line('Nome: '||
23 r1.first_name||'
Dt. Admissão: '|| wdt_admissao||
24 ' Sexta de Folga: '||wsexta);
25 --
26 end loop;
27 --
28 end;
29 /
Nome: Clara Dt. Admissão: 11-NOV-11 Sexta de Folga: 18-NOV-11
Nome: Sarath Dt. Admissão: 03-NOV-11 Sexta de Folga: 04-NOV -11
Nome: Guy Dt. Admissão: 15-NOV-11 Sexta de Folga: 18-NOV-11
Nome: Kevin Dt. Admissão: 16-NOV-11 Sexta de Folga: 18-NOV-11
Nome: Oliver Dt. Admissão: 23-NOV-11 Sexta de Folga: 25-NOV -11
PL/SQL procedure successfully completed.
SQL>
Nesseexemplofoimostradoousodafun ção next_day,ondeseleciona-
mososempregadosquetêmcomomêsdeadmissãoomêscorrente.Através
dessafun çãoécalculadaqualaprimeirasexta-feiralogoemseguidaaodia
daadmissãodecadaempregado.Estediaseráodiadafolgadele.
SQL> declare
2 --
3 wdt_termino_exp date;
4 wqt_meses_trabalho number;
5 --
6 cursor c1 is
7 select ename, dname
8 ,hiredate
9 from emp e, dept d
10 where e.deptno = d.deptno
11 and add_months(hiredate,350 ) >= sysdate;
12
13 --
14 begin
179

## Página 191

CasadoCódigo
15 --
16 for r1 in c1 loop
17 --
18 wdt_termino_exp := add_months(r1.hiredate,3);
19 wqt_meses_trabalho := to_char(months_between(
sysdate,r1.hiredate),'990D00');
20 --
21 dbms_output.put_line('Nome: '||r1.ename||' '||
22 'Depto: '||r1.dname||' '||
23 'Dt. Admissão: '||r1.hiredate||' '||
24 'Término Exp.: '||wdt_termino_exp||' '||
25 'Qtde. Meses Trab.: '||wqt_meses_trabalho
26 );
27 --
28 end loop;
29 --
30 end;
31 /
Nome: ADAMS Depto: RESEARCH Dt. Admissão: 12-JAN-83 Término
Exp.: 12-APR-83
Qtde. Meses Trab.: 346 .61
Nome: SCOTT Depto: RESEARCH Dt. Admissão: 09-DEC-82 Término
Exp.: 09-MAR-83
Qtde. Meses Trab.: 347 .71
PL/SQL procedure successfully completed.
SQL>
Nesse exemplo foi mostrado o uso das funções add_months e
months_between. Oexemploselecionaosempregadosesuasrespectivas
datasdetérminodeexperiênciadocargo.Notequelimitamosonúmerode
empregadosno select,atravésdafun ção add_months,paraevitarore-
tornodetodasaslinhasdatabela.
SQL> declare
2 wsessiontimezone varchar(10);
3 wcurrent_date date;
4 wsysdate date;
180

## Página 192

CasadoCódigo Capítulo13. Funçõesdedata
5 begin
6 wsessiontimezone := sessiontimezone;
7 wcurrent_date := current_date;
8 wsysdate := sysdate;
9 --
10 dbms_output.put_line(
'Fuso Horário: '||wsessiontimezone||' '||
11 'Data Corrente: '||wcurrent_date||' '||
12 'Data Atual: '||wsysdate);
13 --
14 end;
15 /
Fuso Horário: -03: 00 Data Corrente: 30-NOV-11 Data Atual:
30-NOV-11
PL/SQL procedure successfully completed.
SQL>
Nesseexemplofoimostradoousodasfun ções sessiontimezone,
current_datee sysdate.Exibimosofusohorário,adatacorrentelocale
dataatualdoservidor.
SQL> declare
2 --
3 wlast date;
4 wround date;
5 wtrunc date;
6 --
7 cursor c1 is
8 select ename
9 ,hiredate
10 from emp
11 where deptno = 20 ;
12 --
13 begin
14 --
15 for r1 in c1 loop
16 --
181

## Página 193

CasadoCódigo
17 wlast := last_day(r1.hiredate);
18 wround : = round(r1.hiredate, 'YEAR' );
19 wtrunc : = trunc(r1.hiredate, 'YEAR' );
20 --
21 dbms_output.put_line('Nome: '||r1.ename||' '||
22 'Dt. Admissão: '||r1.hiredate||' '||
23 'Último dia Mês Admissão: '||wlast||' '||
24 'Arredonda Ano Admissão.: '||wround||' '||
25 'trunc Ano Admissão: '||wtrunc
26 );
27 --
28 end loop;
29 --
30 end;
31 /
Nome: SMITH Dt. Admissão: 17-DEC-80 Último dia Mês Admissão:
31-DEC-80 Arredonda
Ano Admissão.: 01- JAN-81 trunc Ano Admissão: 01-JAN-80
Nome: JONES Dt. Admissão: 02-APR-81 Último dia Mês Admissão:
30-APR-81 Arredonda
Ano Admissão.: 01- JAN-81 trunc Ano Admissão: 01-JAN-81
Nome: SCOTT Dt. Admissão: 09-DEC-82 Último dia Mês Admissão:
31-DEC-82 Arredonda
Ano Admissão.: 01- JAN-83 trunc Ano Admissão: 01-JAN-82
Nome: ADAMS Dt. Admissão: 12-JAN-83 Último dia Mês Admissão:
31-JAN-83 Arredonda
Ano Admissão.: 01- JAN-83 trunc Ano Admissão: 01-JAN-83
Nome: FORD Dt. Admissão: 03-DEC-81 Último dia Mês Admissão:
31-DEC-81 Arredonda
Ano Admissão.: 01- JAN-82 trunc Ano Admissão: 01-JAN-81
PL/SQL procedure successfully completed.
SQL>
Nesseexemplofoimostradoousodasfun ções last_day, rounde
trunc.Percebaváriasformasdeusarasfun çõesparaextrairoumanipular
determinadasinformações,porexemploarredondaretruncardatas.
182

## Página 194

Capítulo14
Funçõesdeconversão
Emmuitoscasos,precisamosconverterumdeterminadodadodeumtipo
paraoutro.AOracledisponibilizafun çõesdeconversãoparaestetrabalho.
Essasfun ções,emborasejamsimplesdeseremusadas,ajudamemmuitono
momentodeconverterouformatardadosprovenientesdosseuscomandos
SQLouprogramasPL/SQL.
•to_date: converteumastring( charou varchar2)decaractere
paraumadata;
•to_number:converteumastring( charou varchar2)decaractere
paraumnúmero;
•to_char:converteumnúmeroouumadataparaumastringdecarac-
tere.

## Página 195

14.1. to_date CasadoCódigo
Cadafun çãopossuisuascaracterísticaseéutilizadaparacumprirumob-
jetivodiferente.Oqueelaspossuememcomuméonúmerodeparâmetros.
Oprimeiroparâmetroestárelacionadoaovalorquedeveserconvertido,o
segundocorrespondeaoformatoquevocêdesejaaplicare,porúltimoeop-
cional,oparâmetrodelinguagem.Trata-sedefun çõesmuitoutilizadasnodia
adia,eédefundamentalimportânciaconhecê-laseentendercomosecom-
portam.Alémdasmencionadasnalista,aOracledisponibilizaváriasoutras
funçõesparaasmaisdiversassituações.Contudo,essastrêssãoasquemais
comumenteutilizamosnaescritadenossosprogramas.Parasabermaissobre
outrasfun çõesdeconversão,consulteadocumentaç ãodisponívelnositeda
Oracle.
14.1 to_date
Estafun çãoébeminteressante.Comumpoucodetreinoecriatividade,po-
demosrealizarváriasconversõesquepodemajudarmuitonomomentode
formatar,selecionaroucriticarosdadosretornadosdeumcomandoSQL.
Elafuncionabasicamentedaseguinteforma: vocêvaipassarumvalorca-
ractereparafun ção,juntamentecomumformato,quedevesercompatível
comoconjuntodecaracteresquevocêpassou.Qualquerincompatibilidade,
oOraclegeraumerrodeconversão.
Exemplo: to_date(‘21/05/2009’,’dd/mm’). Estaconversãovai
gerarumerro,poisvocêestáinformandodia,mêseano,comocaractere,mas
namáscarasómencionoudiaemês.QuandooOraclevaifazeraconversão,
eleanalisaoformatoquevocêestápassandocomoparâmetroeverificaoque
éelementodefun çãoeoqueécaractere.Nestecaso,elesabeque dde mmsão
elementosconhecidosdediaemês,eque /éumcaracterequeservecomo
umaespéciedeseparador.Depoisdestaidentificaç ão,elepegacadacaractere
informadoevaiconvertendoconformeoformato.2=d,1=d,/=/,0=m,5=metc.
Masquandoelechegaàsegunda /vêquenãoháformatoparaocaractere,
poisterminounoelemento m.Logo,égeradoumerrodeconversão.Vejaa
execução:
SQL> declare
2 wdata date;
184

## Página 196

CasadoCódigo Capítulo14. Funçõesdeconversão
3 begin
4 wdata := to_date('21/05/2009','dd/mm');
5 end;
6 /
declare
*
ERROR at line 1:
ORA-01830: date format picture ends before converting entire
input string
ORA-06512: at line 4
SQL>
Ocontráriotambémgeraoutroerro:
SQL> declare
2 wdata date;
3 begin
4 wdata := to_date('21/05','dd/mm/yyyy');
5 end;
6 /
declare
*
ERROR at line 1:
ORA-01840: input value not long enough for date format
ORA-06512: at line 4
SQL>
Seguemexemplosdousodo to_date:
SQL> begin
2 for r1 in (select ename
3 ,hiredate
4 from emp
5 where hiredate > to_date('010182','ddmmrr')) loop
6 --
7 dbms_output.put_line('Empregado: '||r1.ename||
185

## Página 197

14.1. to_date CasadoCódigo
8 ' - Data de Admissão: '||r1.hiredate);
9 --
10 end loop;
11 end;
12 /
Empregado: SCOTT - Data de Admissão: 09-DEC-82
Empregado: ADAMS - Data de Admissão: 12-JAN-83
Empregado: MILLER - Data de Admissão: 23-JAN-82
PL/SQL procedure successfully completed.
SQL>
Esseexemplomostroucomoépossívelconverterstringsemdatasválidas.
Vejaquenalinha5doprogramatemosafun çãoconvertendoastring 010182
paraumadatautilizandooformato DDMMRR.
SQL> declare
2 wdate date;
3 begin
4 wdate := to_date('21.05.2009','dd.mm.yyyy');
5 --
6 dbms_output.put_line('Data: '||wdate);
7 end;
8 /
Data: 21-MAY-09
PL/SQL procedure successfully completed.
SQL>
Jánesseoutroexemplo,tambémutilizando to_date,notequenalinha
4doprograma,temosafun çãoconvertendooutrastringemumadata,utili-
zandoumformatodiferente.
SQL> declare
2 wdate date;
3 begin
4 wdate := to_date('April 21','month dd',
186

## Página 198

CasadoCódigo Capítulo14. Funçõesdeconversão
'nls_date_language=american');
5 --
6 dbms_output.put_line('Data: '||wdate);
7 end;
8 /
Data: 21-APR-11
PL/SQL procedure successfully completed.
SQL>
Podemostambémadicionaràchamadadafun çãoaspectosreferentesà
linguagem.Nesseúltimoexemplo,estamosconvertendoumastringporex-
tensoemdata,utilizandooformatoamericano.
SQL> declare
2 wdate date;
3 begin
4 wdate := to_date('Abril 21','month dd',
5 'nls_date_language=''BRAZILIAN PORTUGUESE''');
6 --
7 dbms_output.put_line('Data: '||wdate);
8 end;
9 /
Data: 21-APR-11
PL/SQL procedure successfully completed.
SQL>
Contudo,comopôdeservistonoexemploanterior,avisualizaç ãocon-
tinuasendonoformatoamericano,emboraestejamosconvertendoastring
paradatautilizandooformatobrasileiro.Lembre-se,conversãonãonecessa-
riamente,temavercomaformacomqueodadoseráimpressonatela.
SQL> declare
2 wdate date;
3 begin
4 wdate := to_date('Abril 21','month XX',
187

## Página 199

14.1. to_date CasadoCódigo
5 'nls_date_language=''BRAZILIAN PORTUGUESE''');
6 --
7 dbms_output.put_line('Data: '||wdate);
8 end;
9 /
declare
*
ERROR at line 1:
ORA-01821: date format not recognized
ORA-06512: at line 4
SQL>
Esseexemplo,mostraquedevemosinformarformatosválidos,oume-
lhor,formatosconhecidosdalinguagem.Casocontrário,aconversãonãoé
realizadaeerrosocorrerão.
Aseguir,algumaslimitaçõescomrelaç ãoafun ção to_date:
• AStringaserpassadaparaaconversãonãopodecontermaisde220
caracteres;
• Existem vários formatos de máscara disponíveis para a utilização.
QualquermáscaradiferentedaspermitidaspelaOraclegeraráumerro
deconversão;
• Nãopodehaverconfrontodemáscaras. Exemplo: casovocêqueira
utilizaramáscara HH24etambémsolicitarquesejamostradoAM
(indicadordeantemeridianoparamanhã)ouPM(indicadordepós-
meridianoparanoite).
• Nãoépermitidoespecificarelementosdeconversãoduplicados.Exem-
plo:‘DD-MM-MM’.Nestecaso,oformatoparamêsapareceduasvezes.
Vejaalgunselementosdeformataç ãoquepodemserusados:
•CC:adiciona1aosdoisprimeirosdígitosdoano(YYYY).
•SCC:igual CC,prefixandodatas BCcomumsinalnegativo.
188

## Página 200

CasadoCódigo Capítulo14. Funçõesdeconversão
•YY:representaoanocomduascasas.
•YYYY:representaoanocomquatrocasas.
•RR:representaosdoisúltimosdígitosdoano,masobedecendoàse-
guinteregra:soma1aosdoisprimeirosdígitosde CCseanofor < 50
eosúltimos2dígitosdoanocorrenteforem >= 50.Subtrai1de CC
seano >= 50 eosúltimosdoisdígitosdoanocorrenteforem < 50.
•RRRR:representaoano.Aceita2ou4dígitos.Seanoinformadocom2
dígitos,segueasmesmasregrasdeRR.
•YEAR:escreveoanoporextenso.
•MM:númerodomêsde01a12.01=Janeiro,02=Fevereiroetc.
•MONTH:nomedomês.
•MON:representaonomedomêsabreviadocomtrêscaracteres.
•DD:diadomêsde1a31.
•DDD:representaodiadoanode1a366.
•DAY:representaonomedodiaporextenso.
•HH, HH12, HH24:HHeHH12,horasde1a12.HH24,horasde0a23.
•MI:equivaleaosminutosde0a59.
•SS:equivaleaossegundosde0a59.
•SP:converteonúmeroparaseuformatoescrito. Disponívelapenas
paraaescritanoidiomainglês.
•SPTH:mostraosnúmerosdemaneiraordinal.1=First,2=Secondetc.
•FM:retiraespaçosembrancoprovenientedaausênciadecaracteresem
umformato.
189

## Página 201

14.1. to_date CasadoCódigo
Nota:esteselementostambémsãoutilizadosnaconversãodotipo
datepara String.
SQL> declare
2 wdate date;
3 begin
4 wdate := to_date('2008','yyyy');
5 --
6 dbms_output.put_line('Data: '||wdate);
7 end;
8 /
Data: 01-NOV-08
PL/SQL procedure successfully completed.
SQL>
Afun ção to_date,podeconverternãosóstringsrepresentandodatas
completas,comotambémstringsrepresentandopartesdeumadata. Esse
exemplomostraafun çãorealizandoaconversãodastring 2008emdata.
Noteque,aoserimpressoovalordavariável,aqualrecebeuodadocon-
vertido,elerecebeuaatribuiç ãodadataatual,modificadoapenaspeloano
convertido.
SQL> declare
2 wdate date;
3 begin
4 wdate := to_date(200,'ddd');
5 --
6 dbms_output.put_line('Data: '||wdate);
7 end;
8 /
Data: 19-JUL-11
PL/SQL procedure successfully completed.
SQL>
190

## Página 202

CasadoCódigo Capítulo14. Funçõesdeconversão
Esseexemploésimilaraoanterior.Aquiestásendorealizadaaconversão
combasenarepresentaç ãonuméricadodiareferenteaototaldediasdoano.
Uso de YYYY e RRRR
SabemosqueamáscaraYYYYrepresentaosquatrodígitosdoano.Opci-
onalmente,pode-seutilizarYYparamostrarapenasosdoisúltimosdígitos.
Contudo,paracorrigirproblemasdecompatibilidadecomaviradadoséculo,
aOraclecriouasmáscarasRReRRRR.Vejaaaplicaç ãoaseguir:
SQL> declare
2 wdate varchar2(50);
3 begin
4 wdate := to_char(sysdate,'dd/mm/yyyy');
5 dbms_output.put_line('Data: '||wdate);
6 --
7 wdate := to_char(
to_date('01/01/49','dd/mm/yy'),'dd/mm/yyyy');
8 dbms_output.put_line('Data: '||wdate);
9 --
10 wdate := to_char(to_date(
'01/01/50', 'dd/mm/yy'),'dd/mm/yyyy');
11 dbms_output.put_line('Data: '||wdate);
12 --
13 wdate := to_char(
to_date('01/01/49','dd/mm/rr'),'dd/mm/rrrr');
14 dbms_output.put_line('Data: '||wdate);
15 --
16 wdate := to_char(
to_date('01/01/50','dd/mm/rr'),'dd/mm/rrrr');
17 dbms_output.put_line('Data: '||wdate);
18 --
19 end;
20 /
Data: 30/11/2011
Data: 01/01/2049
Data: 01/01/2050
Data: 01/01/2049
Data: 01/01/1950
191

## Página 203

14.2. to_number CasadoCódigo
PL/SQL procedure successfully completed.
SQL>
Nesse exemplo, vemos formatações de datas utilizando a função
to_char,juntamentecomoselementosdeformataç ãoYYeRR.Noteque
podemosterdatasdiferentesaoconverterutilizandoRReYY,dependendo
doanodadatainformada.Paramaisdetalhesecompreensãodesseexemplo,
consulteasregrasdousodoformatoRRnalistadeelementosdeformataç ão
vistaanteriormente.
14.2 to_number
Muitosemelhanteàfun ção to_date,estafun çãotambémtemopapelde
converterdeterminadosvalores.Seuobjetivo,noentanto,éfazeraconversão
decaracteresparanuméricos.
Quandofalamosnafun ção to_date,foimencionadoqueovalordoca-
racterequeestásendoinformadocomoparâmetrodevesercompatívelcomo
formato.Poisbem,quandotrabalhamoscom to_number,omesmotambém
acontece.Aoinformarmosumvalorcaractereparaafun ção to_number,ele
devesercompatívelcomoformatoqueestamospassandoparaafun ção.To-
davia,existeumaparticularidadequantoaoformatoparacasasdecimaisede
grupo(milhar,porexemplo).
ParacálculosinternosdoOracle,sempreseráusadoponto( .)comose-
paradordecimalevírgula( ,)paraseparadordegrupo,comopadrãoame-
ricano. Paraatribuiçõesdevariáveisdotipocaractereouparavisualiza-
ção,oOraclepegaráaformataç ãoconformeestiverconfiguradonavariável
nls_numeric_characters.
UmadasrazõesdeoOracleutilizarestapremissatalvezsejapelofatodea
vírgulaserutilizadaparaaseparaç ãodevaloresoucolunasemumcomando
SQL.Vejaoexemplo:
Fazendoum selectdonúmero111,1utilizandovírgulacomoseparador
decimal.
192

## Página 204

CasadoCódigo Capítulo14. Funçõesdeconversão
SQL> select 111,1 from dual;
111 1
---------- ----------
111 1
SQL>
Agora,executandoomesmo select,masutilizandoopontocomose-
paradordecimal.
SQL> select 111.1 from dual;
111.1
----------
111.1
SQL>
Noprimeiroexemplo,ocomandoSQLacabouentendendoque111eraum
dadoe1eraoutro.Omesmonãoaconteceuquando,emvezdesepararmos
porvírgula,separamosporponto.
Vejamosoexemploaseguir.Neleestamostentandoconverterumvalor
ondetemoscomoseparadordedecimaisavírgula( ,),eparamilhar,oponto
( .).Poisbem,jásabemosqueparacálculosdeconversõesinternasoOracle
utilizaopontocomodecimal.Logo,ocomandoSQLaseguirgeraumerro.
SQL> declare
2 wvalor number;
3 begin
4 wvalor := to_number('4.569.900,87');
5 dbms_output.put_line('Valor: '||wvalor);
6 --
7 end;
8 /
declare
*
ERROR at line 1:
ORA-06502: PL/ SQL: numeric or value error: character to number
193

## Página 205

14.2. to_number CasadoCódigo
conversion error
ORA-06512: at line 4
SQL>
Ok!Oerroaconteceporqueondehávírguladeveriaserpontoeondehá
pontodeveriaservírgula.Poisbem,vejamoso selectaseguir:
SQL> declare
2 wvalor number;
3 begin
4 wvalor := to_number('4,569,900.87') ;
5 dbms_output.put_line('Valor: '||wvalor);
6 --
7 end;
8 /
declare
*
ERROR at line 1:
ORA-06502: PL/SQL: numeric or value error: character to number
conversion error
ORA-06512: at line 4
SQL>
Agoravocêdeveestarseperguntando:“Masporqueoerro,sendoque
tudoindicaqueagoraoformatofoiinformadocorretamente,pontoparade-
cimaisevírgulaparamilhares?”.Poisbem,vejao selectaseguir:
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17-DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
194

## Página 206

CasadoCódigo Capítulo14. Funçõesdeconversão
7654 MARTIN SALESMAN 7698 28- SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09-DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08- SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03-DEC-81 950
7902 FORD ANALYST 7566 03-DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
8000 JOHN CLERK 7902 30-MAR-11 1000
COMM DEPTNO
--------- ---------
20
300 30
500 30
20
1400 30
30
10
20
10
0 30
20
30
20
10
200 20
15 rows selected.
SQL>
Observeacoluna SAL,maisprecisamenteoregistro EMPNO=7566.Veja
queovalordosalárioestáaparecendocomo3272.5.Estenúmeropossuicomo
separadordedecimaisocaractereponto,masnãopossuiseparadordegrupo
demilhar.
Issonoslevaàconclusãodeque,alémdesabermosasregrasparapontos
195

## Página 207

14.2. to_number CasadoCódigo
evírgulas,tambémdevemosestarcientesdecomoestádefinidaasessãodo
Oracle. NoOracle,aformataç ãodemilharnãoaparece,amenosqueseja
aplicadaparatal.Vamosvoltaraoexemploanterior,agoracomaformataç ão:
SQL> declare
2 wvalor number;
3 begin
4 wvalor := to_number('4.569.900,87','9G999G999D00');
5 dbms_output.put_line('Valor: '||wvalor);
6 --
7 end;
8 /
declare
*
ERROR at line 1:
ORA-06502: PL/SQL: numeric or value error
ORA-06512: at line 4
SQL>
Ainda sim o erro persiste. Também pudera, vimos no registro
EMPNO=7566que,nasessãodoOracle,estádefinidocomocasadecimalo
ponto,enãoavírgula.Vamostrocar:
SQL> declare
2 wvalor number;
3 begin
4 wvalor := to_number('4,569,900.87','9G999G999D00');
5 dbms_output.put_line('Valor: '||wvalor);
6 --
7 end;
8 /
Valor: 4569900. 87
PL/SQL procedure successfully completed.
SQL>
196

## Página 208

CasadoCódigo Capítulo14. Funçõesdeconversão
Bingo! Estecomando selectfuncionouporduasrazões. Primeira:o
valorpassadonoformatocaracterepossuiumnúmeroválidoquecontém
comoseparadordecasasdecimaisomesmodefinidonasessãodoOracle.
Segundo:foidefinidoumformatoondeestipulamosquenesteconjuntode
caracteresháseparadoresdegrupooqualrepresentamoscomoelementode
função G.Utilizandodestaforma,oOracleentendequeopontoéoseparador
dedecimaleavírgulaéodemilhar.Paraprovarnossatese,vamosmudaros
separadoresnasessãoevamosexecutaromesmo selectanterior:
SQL> alter session set nls_numeric_characters ='.,';
Session altered.
SQL> declare
2 wvalor number;
3 begin
4 wvalor := to_number('4.569.900,87','9G999G999D00');
5 dbms_output.put_line('Valor: '||wvalor);
6 --
7 end;
8 /
declare
*
ERROR at line 1:
ORA-06502: PL/ SQL: numeric or value error
ORA-06512: at line 4
SQL>
197

## Página 209

14.2. to_number CasadoCódigo
Nota:alémdasalteraçõesreferentesaosseparadoresnuméricos,tam-
bémpodemosalterarassessõesparadefinirumnovoformatodedatae
tambémparaadefiniçãodelinguagens.Exemplos:
alter session set nls_language = 'BRAZILIAN PORTUGUESE';
alter session set nls_date_language = 'PORTUGUESE';
alter session set nls_date_format = 'DD/MM/RRRR';
Agoravamostrocaroscaracteresdelugar:
SQL> declare
2 wvalor number;
3 begin
4 wvalor := to_number('4,569,900.87','9G999G999D00');
5 dbms_output.put_line('Valor: '||wvalor);
6 --
7 end;
8 /
Valor: 4569900. 87
PL/SQL procedure successfully completed.
SQL>
Funcionou.Masespereummomento.Alémdeconverter,precisosaber
comoestádefinidonasessãodoOracle?Não.Nãoénecessáriosevocêespeci-
ficar,alémdoformato,quaiscaracteresdevemserutilizadosparaaseparaç ão
dedecimaisegrupos.Vejamosnovamenteopenúltimoexemplo.Nele,defi-
nimosqueopontoseriaadecimal,evírgulaogrupo.Contudo,issogerouum
erroaoexecutarnosso selectondeestavajustamentedefinidoaocontrário
daparametrizaçãofeita.
SQL> alter session set nls_numeric_characters ='.,';
Session altered.
198

## Página 210

CasadoCódigo Capítulo14. Funçõesdeconversão
SQL> declare
2 wvalor number;
3 begin
4 wvalor := to_number('4.569.900,87','9G999G999D00');
5 dbms_output.put_line('Valor: '||wvalor);
6 --
7 end;
8 /
declare
*
ERROR at line 1:
ORA-06502: PL/ SQL: numeric or value error
ORA-06512: at line 4
SQL>
Utilizandooparâmetro nls,aqueleterceiroparâmetrodafun çãoqueé
opcional,nósconseguimos,emvezdealterarasessãodoOracle,validarestes
caracteresapenasnonossocomando.Vamosexecutarnovamenteo select
anterior,masagoraincorporandooterceiroparâmetro:
SQL> declare
2 wvalor number;
3 begin
4 wvalor := to_number('4.569.900,87','9G999G999D00',
'nls_numeric_characters=,.');
5 dbms_output.put_line('Valor: '||wvalor);
6 --
7 end;
8 /
Valor: 4569900 .87
PL/SQL procedure successfully completed.
SQL>
Funcionouperfeitamente.Emborapare çacomplicadonoinício,vocêvai
seacostumandocomascaracterísticaselogopegaalógica.Valesalientarque
199

## Página 211

14.2. to_number CasadoCódigo
estaquestãodasessãotambéméválidaparao to_date. Vejao select,
agoraobservandoacoluna HIREDATE.
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17-DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28- SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09-DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08- SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03-DEC-81 950
7902 FORD ANALYST 7566 03-DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
8000 JOHN CLERK 7902 30-MAR-11 1000
COMM DEPTNO
--------- ---------
20
300 30
500 30
20
1400 30
30
10
20
10
0 30
20
30
20
10
200

## Página 212

CasadoCódigo Capítulo14. Funçõesdeconversão
200 20
15 rows selected.
SQL>
Paraoregistro EMPNO=7566,ovalordacoluna HIREDATEé02-APR-81.
Logo,esteéoformatodefinidonasessão.Vamosolharopróximo select.
SQL> declare
2 wdate date;
3 begin
4 wdate := to_date('02-APR-81');
5 dbms_output.put_line('Data: '||wdate);
6 --
7 end;
8 /
Data: 02-APR-81
PL/SQL procedure successfully completed.
SQL>
Nota-sequeno selectanteriornãofoigeradoerro,mesmonãosendo
informadooformato.Issoaconteceuporqueovalordecaractereinformado
comostringestánomesmoformatodasessãodoOracle.Vejaoqueacontece
quandocolocamosastringemoutroformato:
SQL> declare
2 wdate date;
3 begin
4 wdate := to_date('05/21/2009');
5 dbms_output.put_line('Data: '||wdate);
6 --
7 end;
8 /
declare
*
ERROR at line 1:
201

## Página 213

14.2. to_number CasadoCódigo
ORA-01843: not a valid month
ORA-06512: at line 4
SQL>
Paraconsertarissodevemosinformarumformatocompatívelcomocon-
juntodecaracterespassadooutrocaroformatodasessãodoOracle.Infor-
mandoumformatocompatível:
SQL> declare
2 wdate date;
3 begin
4 wdate := to_date('05/21/2009','mm/dd/yyyy');
5 dbms_output.put_line('Data: '||wdate);
6 --
7 end;
8 /
Data: 21-MAY-09
PL/SQL procedure successfully completed.
SQL>
AlterandoasessãodoOracle:
SQL> declare
2 wdate date;
3 begin
4 wdate := to_date('05/21/2009');
5 dbms_output.put_line('Data: '||wdate);
6 --
7 end;
8 /
Data: 05/21/2009
PL/SQL procedure successfully completed.
SQL>
202

## Página 214

CasadoCódigo Capítulo14. Funçõesdeconversão
Vejaalgunselementosdeformataç ãoquepodemserusados:
•9:cadanoverepresentaumcaracterequeserásubstituídopelocarac-
terereferenteaovalornuméricopassadocomoparâmetro.Oszerosna
frentesãotratadoscomoespaçosembranco.
•0:adicionando0comoumprefixoousufixoaonúmero,todososze-
rosiniciaisoufinaissãotratadoseexibidoscomozerosemvezdeum
espaçoembranco.
•$:prefixodosímbolodemoedaimpressonaprimeiraposiç ão.
•S:exibeumsinalde +inicialoufinalquandoovalorforpositivoeum
sinalde -inicialoufinalquandoovalorfornegativo.
•D:localizaçãodopontodecimal.Osnovesdeambososladosrefletem
onúmeromáximodedígitospermitidos.
•G:especificaumseparadordegrupo(milhar,porexemplo)comouma
vírgula.
•L:especificaalocalizaç ãodosímbolodemoedalocal(talcomo $).
•,:colocaumavírgulanaposiç ãoespecificada,independentementedo
separadordegrupo.
•.: especificaalocalizaçãodopontodecimal,independentementedo
separadordecimal.
•FM:removeosespaçosembrancoinicialefinal.
Há uma confusão muito comum com o uso doto_date e do
to_numbernoquedizrespeitoaoresultadomostradopelo selectquando
sãoutilizadasestasduasfun ções.Emboraestejamosinformandoumformato,
oOraclenãoapresentaoresultadodoSQLbaseadonele.Issoaconteceporque
oformatonousodestasfun çõeséapenasparaaconversãoenãoparaavisu-
alização.Parvisualizarmosoresultadocombasenoformatoquequeremos,
utilizamoso to_char.
203

## Página 215

14.3. to_char CasadoCódigo
14.3 to_char
Funçãoutilizadaparaconvertertiposdedadosnuméricosedatasparaca-
racteres.Alémdaconversão,eleémuitoutilizadoparaformataç ãovisualde
dados.Seguemexemplos:
SQL> declare
2 wsal varchar2(50);
3 begin
4 for r1 in (select ename
5 ,sal
6 from emp) loop
7 --
8 wsal := to_char(r1.sal,'9G999G999D00',
'nls_numeric_characters=''.,''');
9 --
10 dbms_output.put_line('Nome: '||r1.ename||'
Salário: '||wsal);
11 --
12 end loop;
13 end;
14 /
Nome: SMITH Salário: 800.00
Nome: ALLEN Salário: 1 ,600.00
Nome: WARD Salário: 1, 250.00
Nome: JONES Salário: 2 ,975.00
Nome: MARTIN Salário: 1,250.00
Nome: BLAKE Salário: 2 ,850.00
Nome: CLARK Salário: 2 ,450.00
Nome: SCOTT Salário: 3 ,000.00
Nome: KING Salário: 5, 000.00
Nome: TURNER Salário: 1,500.00
Nome: ADAMS Salário: 1 ,100.00
Nome: JAMES Salário: 950.00
Nome: FORD Salário: 3, 000.00
Nome: MILLER Salário: 1,300.00
PL/SQL procedure successfully completed.
204

## Página 216

CasadoCódigo Capítulo14. Funçõesdeconversão
SQL>
Nesteexemplosãoselecionadostodososnomesdosempregadoseseus
respectivossalários.Foiutilizadaafun ção to_charparaformatarosvalo-
resdosalário,comoelementodeformataç ãoparacasasdecimaisemilhar.
Notequeaquiusamosoparâmetro nls_numeric_characters,parade-
finirquaiscaracteresdevemserutilizadosparacadaseparadordoelemento.
SQL> begin
2 for r1 in (select count(*) qt_admitidos
3 ,to_char(hiredate,'mm' ) MES
4 from emp
5 group by to_char(hiredate,'mm')) loop
6 --
7 dbms_output.put_line('Admitidos: '||r1.qt_admitidos||'
Mês: '||r1.mes);
8 --
9 end loop;
10 end;
11 /
Admitidos: 1 Mês: 04
Admitidos: 2 Mês: 09
Admitidos: 4 Mês: 12
Admitidos: 1 Mês: 11
Admitidos: 2 Mês: 01
Admitidos: 2 Mês: 02
Admitidos: 1 Mês: 05
Admitidos: 1 Mês: 06
PL/SQL procedure successfully completed.
SQL>
Aquiafun ção to_charfoiutilizadaparaformataradatadeadmissãodo
empregado,mostrandoapenasomêsreferenteestadata.O selectagrupa
eapresentaquantosempregadosforamadmitidosemcadamês.
SQL> declare
2 wdata_extenso varchar2( 100);
205

## Página 217

14.3. to_char CasadoCódigo
3 begin
4 wdata_extenso := '22 de agosto de 2009 será o dia '||
5 to_char(to_date('22/08/2009','dd/mm/yyyy'),'ddd')||
6 ' do ano';
7 --
8 dbms_output.put_line(wdata_extenso);
9 --
10 end;
11 /
22 de agosto de 2009 será o dia 234 do ano
PL/SQL procedure successfully completed.
SQL>
Outroexemplocom to_char,usadonaformataç ãodedatas.Nessepro-
grama,sãoimpressosumadataeonúmerododiaqueelarepresentanoano.
SQL> declare
2 wdia_semana varchar2(50 );
3 begin
4 for r1 in (select ename, hiredate from emp) loop
5 --
6 wdia_semana := to_char(r1.hiredate,'day');
7 --
8 dbms_output.put_line('Nome: '||r1.ename||' Admissão: '||
9 r1.hiredate||' Dia da Semana: '||wdia_semana);
10 --
11 end loop;
12 end;
13 /
Nome: SMITH Admissão: 12/17/1980 Dia da Semana: wednesday
Nome: ALLEN Admissão: 02/20/1981 Dia da Semana: friday
Nome: WARD Admissão: 02/22/1981 Dia da Semana: sunday
Nome: JONES Admissão: 04/02/1981 Dia da Semana: thursday
Nome: MARTIN Admissão: 09/28/1981 Dia da Semana: monday
Nome: BLAKE Admissão: 05/01/1981 Dia da Semana: friday
Nome: CLARK Admissão: 06/09/1981 Dia da Semana: tuesday
Nome: SCOTT Admissão: 12/09/1982 Dia da Semana: thursday
206

## Página 218

CasadoCódigo Capítulo14. Funçõesdeconversão
Nome: KING Admissão: 11/17/1981 Dia da Semana: tuesday
Nome: TURNER Admissão: 09/08/1981 Dia da Semana: tuesday
Nome: ADAMS Admissão: 01/12/1983 Dia da Semana: wednesday
Nome: JAMES Admissão: 12/03/1981 Dia da Semana: thursday
Nome: FORD Admissão: 12/03/1981 Dia da Semana: thursday
Nome: MILLER Admissão: 01/23/1982 Dia da Semana: saturday
PL/SQL procedure successfully completed.
SQL>
Nesseexemplo,sãomostradosdadosreferentesàadmissãodoempre-
gado:nomedoempregado,datadeadmissãoediadasemana.Esteúltimo,
formatadoatravésdafun ção to_char.
SQL> declare
2 wdata_extenso varchar2( 100);
3 begin
4 wdata_extenso :=
'Joinville, '||to_char(sysdate,'dd')||' de '||
5 initcap(to_char(sysdate, 'fmmonth'))||' de '
6 ||to_char(sysdate,'yyyy')||'.';
7 --
8 dbms_output.put_line(wdata_extenso);
9 --
10 end;
11 /
Joinville, 30 de November de 2011.
PL/SQL procedure successfully completed.
SQL>
Nesseexemplo,usamos to_charparaimprimiremtelaadataporex-
tenso.
SQL> begin
2 for r1 in (select ename
3 ,hiredate
207

## Página 219

14.3. to_char CasadoCódigo
4 from emp
5 where to_char(hiredate,'yyyy') = '1982') loop
6 --
7 dbms_output.put_line(
'Nome: '||r1.ename||' Admissão: '||r1.hiredate);
8 --
9 end loop;
10 end;
11 /
Nome: SCOTT Admissão: 12/09/1982
Nome: MILLER Admissão: 01/23/1982
PL/SQL procedure successfully completed.
SQL>
Aqui utilizamos a função to_char para restringir dados em um
select.
SQL> declare
2 wsal_formatado varchar2(50);
3 begin
4 for r1 in (select sal from emp) loop
5 --
6 wsal_formatado :=
'R$ '||to_char(r1.sal,'fm9G999G990D00');
7 --
8 dbms_output.put_line('Salário: '||r1.sal||'
Salário Formatado: '||wsal_formatado);
9 --
10 end loop;
11 end;
12 /
Salário: 800 Salário Formatado: R$ 800.00
Salário: 1600 Salário Formatado: R$ 1,600.00
Salário: 1250 Salário Formatado: R$ 1,250.00
Salário: 2975 Salário Formatado: R$ 2,975.00
Salário: 1250 Salário Formatado: R$ 1,250.00
Salário: 2850 Salário Formatado: R$ 2,850.00
208

## Página 220

CasadoCódigo Capítulo14. Funçõesdeconversão
Salário: 2450 Salário Formatado: R$ 2,450.00
Salário: 3000 Salário Formatado: R$ 3,000.00
Salário: 5000 Salário Formatado: R$ 5,000.00
Salário: 1500 Salário Formatado: R$ 1,500.00
Salário: 1100 Salário Formatado: R$ 1,100.00
Salário: 950 Salário Formatado: R$ 950.00
Salário: 3000 Salário Formatado: R$ 3,000.00
Salário: 1300 Salário Formatado: R$ 1,300.00
PL/SQL procedure successfully completed.
SQL>
SQL> declare
2 wsal_formatado varchar2(50);
3 begin
4 for r1 in (select sal from emp) loop
5 --
6 wsal_formatado := to_char(r1.sal,'fmL9G999G990D00');
7 --
8 dbms_output.put_line('Salário: '||r1.sal||'
Salário Formatado: '||wsal_formatado);
9 --
10 end loop;
11 end;
12 /
Salário: 800 Salário Formatado: $800.00
Salário: 1600 Salário Formatado: $1,600.00
Salário: 1250 Salário Formatado: $1,250.00
Salário: 2975 Salário Formatado: $2,975.00
Salário: 1250 Salário Formatado: $1,250.00
Salário: 2850 Salário Formatado: $2,850.00
Salário: 2450 Salário Formatado: $2,450.00
Salário: 3000 Salário Formatado: $3,000.00
Salário: 5000 Salário Formatado: $5,000.00
Salário: 1500 Salário Formatado: $1,500.00
Salário: 1100 Salário Formatado: $1,100.00
Salário: 950 Salário Formatado: $950.00
Salário: 3000 Salário Formatado: $3,000.00
209

## Página 221

14.3. to_char CasadoCódigo
Salário: 1300 Salário Formatado: $1,300.00
PL/SQL procedure successfully completed.
SQL>
Esseexemploseparececomoanterior.Contudo,aquiestamosutilizando
oselementosdeformataç ão FMe L.Oprimeiroretiraosespaçosembranco,
ondealgumelementodeformataç ãonãotenhasidopreenchido,porausência
devalores. Osegundomostraamoedaconfiguradanasessãodousuário,
ondeoprogramaestásendoexecutado.
SQL> declare
2 wpositivo varchar2(100);
3 wnegativo varchar2(100);
4 begin
5 wpositivo := to_char(174984283.75,'fm999,999,999.00S');
6 wnegativo := to_char(100-1000,'fm999,999,999.00S');
7 --
8 dbms_output.put_line('Positivo: '||wpositivo||' -
Negativo: '||wnegativo);
9 --
10 end;
11 /
Positivo: 174,984,283.75+ - Negativo: 900.00-
PL/SQL procedure successfully completed.
SQL>
Jánesseexemplo,utilizamosoelementodeformataç ão S,queindicao
sinalreferenteaovalorformatado.Notequenovalorpositivofoiimpresso,
atrásdonúmero,osinaldepositivo( +),quantoparaovalornegativoéim-
pressoosinaldenegativo( -).
210

## Página 222

Capítulo15
Funçõescondicionais
OOracledisponibilizaoutrostiposdefun ções,dentreasquaisasfun ções
condicionais. Elassãoutilizadastantonasele çãodedadospelacláusula
selectcomotambémnousodecláusulas where. Seuusoébastantedi-
fundidoebemflexível.
•decode:estaestruturafuncionacomoumaestrutura if-elseden-
trodeumacláusula select. Émuitoutilizadaprincipalmentepara
visualizaçãodedadosondeéprecisorealizaralgumtesteparasaberse
estesdadospodemounãoaparecer.
•nullif:sãopassadosdoisparâmetrosparaestafun ção.Elacompara
osdois,seforemiguaiséretornado Null.Casocontrário,elaretorna
oprimeiroparâmetro.

## Página 223

CasadoCódigo
•nvl:paraestafun çãosãopassadosdoisparâmetros.Seoprimeirofor
nulo,eleretornaosegundo,casocontrário,retornaoprimeiro.
•case:muitoparecidocomo decode.Seuobjetivotambémépermi-
tirautilizaç ãodeumaestruturatipo if-elsedentrodocomando
SQL.Aocontráriodo decodesuaaplicaçãoevisualizaç ãosãomais
inteligíveis(padrãoANSI).
•greatest:retornaamaiorexpressãodeumalistadevalorespassada
comoparâmetro.Todasasexpressõesapósaprimeirasãoconvertidas
paraotipodedadodaprimeiraantesdacomparaç ãoserrealizada.
•least:funcionaoinversoda greatest.Estatrazamenorexpressão.
Vejaalgunsexemplos:
SQL> declare
2 cursor c1 is
3 select job,
4 sum (case
5 when deptno = 10 then sal
6 else
7 0
8 end) depart_10,
9 sum (case
10 when deptno = 20 then sal
11 else
12 0
13 end) depart_20,
14 sum(case
15 when deptno = 30 then sal
16 else
17 0
18 end) depart_30,
19 sum(sal) total_job
20 from emp
21 group by job;
22 --
23 begin
212

## Página 224

CasadoCódigo Capítulo15. Funçõescondicionais
24 for r1 in c1 loop
25 --
26 dbms_output.put_line(r1.job||' - Depart. 10: '
||r1.depart_10||' - Depart. 20: '||
27 r1.depart_20||' - Depart. 30: '||
r1.depart_30||' - Total: '||
28 r1.total_job);
29 --
30 end loop;
31 end;
32 /
CLERK - Depart. 10: 1300 - Depart. 20: 1900 - Depart. 30: 950 -
Total: 4150
SALESMAN - Depart. 10 : 0 - Depart. 20: 0 - Depart. 30: 5600 -
Total: 5600
PRESIDENT - Depart. 10: 5000 - Depart. 20: 0 - Depart. 30: 0 -
Total: 5000
MANAGER - Depart. 10: 2450 - Depart. 20: 2975 - Depart. 30:
2850 - Total: 8275
ANALYST - Depart. 10: 0 - Depart. 20: 6000 - Depart. 30: 0 -
Total: 6000
PL/SQL procedure successfully completed.
SQL>
Nesseexemplo,utilizamosafun ção case,parasomartodosossalários
pordepartamento,agrupandoporcargo.
SQL> declare
2 cursor c1 is
3 select job
4 ,sum(decode(deptno, 10, sal, 0 )) depart_10
5 ,sum(decode(deptno, 20, sal, 0 )) depart_20
6 ,sum(decode(deptno, 30, sal, 0 )) depart_30
7 ,sum(sal) total_job
8 from emp
9 group by job;
10 --
213

## Página 225

CasadoCódigo
11 begin
12 for r1 in c1 loop
13 --
14 dbms_output.put_line(r1.job||' - Depart. 10: '||
r1.depart_10||' - Depart. 20: '||
15 r1.depart_20||' - Depart. 30: '||
r1.depart_30||' - Total: '||
16 r1.total_job);
17 --
18 end loop;
19 end;
20 /
CLERK - Depart. 10: 1300 - Depart. 20: 1900 - Depart. 30: 950 -
Total: 4150
SALESMAN - Depart. 10: 0 - Depart. 20: 0 - Depart. 30: 5600 -
Total: 5600
PRESIDENT - Depart. 10 : 5000 - Depart. 20: 0 - Depart. 30: 0 -
Total: 5000
MANAGER - Depart. 10: 2450 - Depart. 20: 2975 - Depart. 30: 2850
- Total: 8275
ANALYST - Depart. 10: 0 - Depart. 20 : 6000 - Depart. 30: 0 -
Total: 6000
PL/SQL procedure successfully completed.
SQL>
Esseexemploéidênticoaoanterior.Apenastrocamosafun ção casepela
função decode.Valelembrarque caseédopadrãoSQLANSIe decode
édopadrãoOracle.
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
---------- ---------- --------- ---------- ---------- ----------
7369 SMITH CLERK 7902 12/17/1980 800
7499 ALLEN SALESMAN 7698 02/20/1981 1600
7521 WARD SALESMAN 7698 02/22/1981 1250
7566 JONES MANAGER 7839 04/02/1981 2975
214

## Página 226

CasadoCódigo Capítulo15. Funçõescondicionais
7654 MARTIN SALESMAN 7698 09/28/1981 1250
7698 BLAKE MANAGER 7839 05/01/1981 2850
7782 CLARK MANAGER 7839 06/09/1981 2450
7788 SCOTT ANALYST 7566 12/09/1982 3000
7839 KING PRESIDENT 11/17/1981 5000
7844 TURNER SALESMAN 7698 09/08/1981 1500
7876 ADAMS CLERK 7788 01/12/1983 1100
7900 JAMES CLERK 7698 12/03/1981 950
7902 FORD ANALYST 7566 12/03/1981 3000
7934 MILLER CLERK 7782 01/23/1982 1300
COMM DEPTNO
---------- ----------
20
300 30
500 30
20
1400 30
30
10
20
10
0 30
20
30
20
10
14 rows selected.
SQL> declare
2 wsal_comm1 number;
3 wsal_comm2 number;
4 begin
5 --
6 select sum(sal+comm) into wsal_comm1 from emp;
7 --
8 select sum(sal+nvl(comm,0)) into wsal_comm2 from emp;
9 --
215

## Página 227

CasadoCódigo
10 dbms_output.put_line('Sal. Comm1: '||wsal_comm1||' -
Sal. Comm2: '||wsal_comm2);
11 --
12 end;
13 /
Sal. Comm1: 7800 - Sal. Comm2: 31225
PL/SQL procedure successfully completed.
SQL>
Nesseexemploestamosutilizandoafun ção nvl.Notequequandoreali-
zamoscálculoscomvaloresnulos(linha6)oOraclenãoexecutataloperaç ão.
OOraclesempreconsideracomofalsoquandoexistemvalores NULL(nulo)
emcálculosaritméticosounousoderestriç ãodedados,como,porexemplo,
emcláusulas where. Quandoissoocorre,eleignoraaaç ão,masnãogera
erros.
SQL> declare
2 wmaior_letra varchar2(1 );
3 wmenor_letra varchar2(1 );
4 begin
5 --
6 select greatest('b','x' ,'t','u','a') into wmaior_letra
from dual;
7 --
8 select least('b','x','t','u','a') into wmenor_letra
from dual;
9 --
10 dbms_output.put_line('Maior Letra: '||wmaior_letra||' -
Menor Letra: '||wmenor_letra);
11 --
12 end;
13 /
Maior Letra: x - Menor Letra: a
PL/SQL procedure successfully completed.
SQL>
216

## Página 228

CasadoCódigo Capítulo15. Funçõescondicionais
Nesseexemplo,temosousodasfun ções greateste least.
SQL> declare
2 comparacao1 varchar2(100);
3 comparacao2 varchar2(100);
4 begin
5 --
6 select decode(nullif('abacaxi','abacaxi'),null,
'são iguais','são diferentes')
7 into comparacao1 from dual;
8 --
9 select decode(nullif('abacaxi','morango'),null,
'são iguais','são diferentes')
10 into comparacao2 from dual;
11 --
12 dbms_output.put_line('Comparação 1: '||comparacao1||' -
Comparação 2: '||comparacao2);
13 --
14 end;
15 /
Comparação 1: são iguais - Comparação 2: são diferentes
PL/SQL procedure successfully completed.
SQL>
Nesseexemplo,temosousodafun ção nullif.
15.1 decode vs. case
Doscomandoscondicionaisvistosanteriormente,o decodeéomaisutili-
zado.Elefuncionacomoumaespéciedecondiç ãoSE( if)paraalinguagem
SQL.EstecomandoéexclusivodoOracle,entretanto,nopadrãoANSIdalin-
guagemSQLexisteumcomandosimilar,o case.Vocêpodeusarqualquer
umdeles.Porém,ousodo casesóépermitidonasversõesmaisnovasdo
bancodedadosOracle.AOracle,nasversõesmaisrecentes,veminserindo
comandospadrõesANSIenquantoseuscomandosespecíficosmantêmsuas
217

## Página 229

15.1. decodevs.case CasadoCódigo
característicasparaquestõesdecompatibilidade.Vejacomparaçõesentrees-
tesdoiscomandos.
Exemplo 1
PadrãoANSI(tambémsuportadopeloOraclenasversõesmaisnovasdo
bancodedados):
SQL> declare
2 cursor c1 is
3 select job,
4 sum (case
5 when deptno = 10 then sal
6 else
7 0
8 end) depart_10,
9 sum (case
10 when deptno = 20 then sal
11 else
12 0
13 end) depart_20,
14 sum(case
15 when deptno = 30 then sal
16 else
17 0
18 end) depart_30,
19 sum(sal) total_job
20 from emp
21 group by job;
22 --
23 begin
24 for r1 in c1 loop
25 --
26 dbms_output.put_line(r1.job||' - Depart. 10: '||
r1.depart_10||' - Depart. 20: '||
27 r1.depart_20||' - Depart. 30: '||
r1.depart_30||' - Total: '||
28 r1.total_job);
29 --
218

## Página 230

CasadoCódigo Capítulo15. Funçõescondicionais
30 end loop;
31 end;
32 /
CLERK - Depart. 10: 1300 - Depart. 20: 1900 - Depart. 30: 950 -
Total: 4150
SALESMAN - Depart. 10 : 0 - Depart. 20: 0 - Depart. 30: 5600 -
Total: 5600
PRESIDENT - Depart. 10: 5000 - Depart. 20: 0 - Depart. 30: 0 -
Total: 5000
MANAGER - Depart. 10: 2450 - Depart. 20: 2975 - Depart. 30: 2850
- Total: 8275
ANALYST - Depart. 10: 0 - Depart. 20: 6000 - Depart. 30: 0 -
Total: 6000
PL/SQL procedure successfully completed.
SQL>
PadrãoOracle:
SQL> declare
2 cursor c1 is
3 select job,
4 sum(decode(deptno, 10, sal, 0)) depart_10,
5 sum(decode(deptno, 20, sal, 0)) depart_20,
6 sum(decode(deptno, 30, sal, 0)) depart_30,
7 sum(sal) total_job
8 from emp
9 group by job;
10 --
11 begin
12 for r1 in c1 loop
13 --
14 dbms_output.put_line(r1.job||' - Depart. 10: '||
r1.depart_10||' - Depart. 20: '||
15 r1.depart_20||' - Depart. 30: '||
r1.depart_30||' - Total: '||
16 r1.total_job);
17 --
18 end loop;
219

## Página 231

15.1. decodevs.case CasadoCódigo
19 end;
20 /
CLERK - Depart. 10: 1300 - Depart. 20: 1900 - Depart. 30: 950 -
Total: 4150
SALESMAN - Depart. 10: 0 - Depart. 20: 0 - Depart. 30: 5600 -
Total: 5600
PRESIDENT - Depart. 10 : 5000 - Depart. 20: 0 - Depart. 30: 0 -
Total: 5000
MANAGER - Depart. 10: 2450 - Depart. 20: 2975 - Depart. 30: 2850
- Total: 8275
ANALYST - Depart. 10: 0 - Depart. 20 : 6000 - Depart. 30: 0 -
Total: 6000
PL/SQL procedure successfully completed.
SQL>
Exemplo 2
PadrãoANSI(tambémsuportadopeloOraclenasversõesmaisnovasdo
bancodedados):
SQL> declare
2 cursor c1 is
3 select ename
4 , job
5 , mgr
6 ,
7 case
8 when mgr = 7902 then 'MENSALISTA'
9 when mgr = 7902 then 'MENSALISTA'
10 when mgr = 7839 then 'COMISSIONADO'
11 when mgr = 7566 then 'MENSAL/HORISTA'
12 else
13 'OUTROS'
14 end tipo
15 from emp;
16
17 --
220

## Página 232

CasadoCódigo Capítulo15. Funçõescondicionais
18 begin
19 for r1 in c1 loop
20 --
21 dbms_output.put_line('Nome: '||r1.ename||' - Cargo:
'||r1.job||' - Gerente: '||
22 r1.mgr||' - Tipo: '||r1.tipo);
23 --
24 end loop;
25 end;
26 /
Nome: SMITH - Cargo: CLERK - Gerente: 7902 - Tipo: MENSALISTA
Nome: ALLEN - Cargo: SALESMAN - Gerente: 7698 - Tipo: OUTROS
Nome: WARD - Cargo: SALESMAN - Gerente: 7698 - Tipo: OUTROS
Nome: JONES - Cargo: MANAGER - Gerente: 7839 - Tipo: COMISSIONADO
Nome: MARTIN - Cargo: SALESMAN - Gerente: 7698 - Tipo: OUTROS
Nome: BLAKE - Cargo: MANAGER - Gerente: 7839 - Tipo: COMISSIONADO
Nome: CLARK - Cargo: MANAGER - Gerente: 7839 - Tipo: COMISSIONADO
Nome: SCOTT - Cargo: ANALYST - Gerente: 7566 - Tipo:
MENSAL/HORISTA
Nome: KING - Cargo: PRESIDENT - Gerente: - Tipo: OUTROS
Nome: TURNER - Cargo: SALESMAN - Gerente: 7698 - Tipo: OUTROS
Nome: ADAMS - Cargo: CLERK - Gerente: 7788 - Tipo: OUTROS
Nome: JAMES - Cargo: CLERK - Gerente: 7698 - Tipo: OUTROS
Nome: FORD - Cargo: ANALYST - Gerente: 7566 - Tipo:
MENSAL/HORISTA
Nome: MILLER - Cargo: CLERK - Gerente: 7782 - Tipo: OUTROS
PL/SQL procedure successfully completed.
SQL>
PadrãoOracle:
SQL> declare
2 cursor c1 is
3 select ename
4 ,job
5 ,mgr
6 ,decode(mgr,7902,'MENSALISTA'
7 ,7839,'COMISSIONADO'
221

## Página 233

15.1. decodevs.case CasadoCódigo
8 ,7566,'MENSAL/HORISTA'
9 ,'OUTROS') tipo
10 from emp;
11 --
12 begin
13 for r1 in c1 loop
14 --
15 dbms_output.put_line('Nome: '||r1.ename||' -
Cargo: '||r1.job||' -
Gerente: '||
16 r1.mgr||' - Tipo: '||r1.tipo);
17 --
18 end loop;
19 end;
20 /
Nome: SMITH - Cargo: CLERK - Gerente: 7902 - Tipo: MENSALISTA
Nome: ALLEN - Cargo: SALESMAN - Gerente: 7698 - Tipo: OUTROS
Nome: WARD - Cargo: SALESMAN - Gerente: 7698 - Tipo: OUTROS
Nome: JONES - Cargo: MANAGER - Gerente: 7839 - Tipo: COMISSIONADO
Nome: MARTIN - Cargo: SALESMAN - Gerente: 7698 - Tipo: OUTROS
Nome: BLAKE - Cargo: MANAGER - Gerente: 7839 - Tipo: COMISSIONADO
Nome: CLARK - Cargo: MANAGER - Gerente: 7839 - Tipo: COMISSIONADO
Nome: SCOTT - Cargo: ANALYST - Gerente: 7566 - Tipo:
MENSAL/HORISTA
Nome: KING - Cargo: PRESIDENT - Gerente: - Tipo: OUTROS
Nome: TURNER - Cargo: SALESMAN - Gerente: 7698 - Tipo: OUTROS
Nome: ADAMS - Cargo: CLERK - Gerente: 7788 - Tipo: OUTROS
Nome: JAMES - Cargo: CLERK - Gerente: 7698 - Tipo: OUTROS
Nome: FORD - Cargo: ANALYST - Gerente: 7566 - Tipo:
MENSAL/HORISTA
Nome: MILLER - Cargo: CLERK - Gerente: 7782 - Tipo: OUTROS
PL/SQL procedure successfully completed.
SQL>
Aop çãoentreusarumououtrovaidependerdaabrangênciadosseus
programas.SeelesforemespecíficosparaousoemOracle,o decodepode
222

## Página 234

CasadoCódigo Capítulo15. Funçõescondicionais
serusadosemproblemas. Inclusive,comopôdeservistonosexemplos,ele
podesetornarvisualmentemaisclaroparaoentendimentodocódigo. Já,
sesuasaplicaçõesforemabrangentesnoquedizrespeitoaoperaremvários
bancosdedados,vocêteráqueusaropadrãoANSI,ouseja,usaro casepara
queelesfuncionememqualquerbancodedados,oupelomenosnaquelesque
seguemestepadrão.
223

## Página 236

Capítulo16
Programasarmazenados
Atéaqui, construímosprogramasemblocoschamadosblocosanônimos.
Casoquiséssemosguardá-los,teríamosquesalvá-losemumoumaisarquivos
emalgumdiretórionocomputadorparanãoperdê-los.Quandoquiséssemos
executá-losnovamente,teríamosqueresgatá-losdocomputadorparaentão
executá-losemumaferramenta,porexemplo,noSQL*Plus.Poisbem,agora
vamosaprendercomogravarestesprogramasnobancodedados. issonos
trazmuitosbenefícioseabremuitaspossibilidades.Aseguirvemosalgumas
delas:
•Reaproveitamento de códigos: podemosescreverprocedimentose
funçõesquepodemservircomobaseparaasdemaispartesdeumsis-
tema.Porexemplo,podemoscriarumafun çãoparavalidaç ãodenú-
merosdeCPFquepossaserutilizadaemváriosmódulosdosistema,

## Página 237

16.1. proceduresefunctions CasadoCódigo
comonomódulodeRHoudecompras,ouseja,podemosterumpro-
gramagravadonobancodedadosaoqualtodospodemteracesso.
•Rapidez:tendooprogramaarmazenadonobancodedados,podemos
acessá-lorapidamente,semterqueutilizarchamadasexternasaarqui-
vos.outropontointeressanteéqueasferramentasdedesenvolvimento
eanálisedoOracleenxergamdeformanativaestesobjetosarmazena-
dos.
•Controle de alterações:umprogramaarmazenadonobancodedados
émuitomaisfácildeseralterado.Épossívelabri-loealterá-lodeforma
maisrápida,compilandoeemseguidaefetivandoasalterações.Como
oprogramaestáemumúnicolugar,osdemaissistemasqueoutilizam
enxergarãotodasasalteraçõesrealizadas.
•Controle de acesso:atravésdeconcessõesépossívellimitarosacessos
aestesprogramas,permitindo-osaapenasalgunsusuários.
•Modularização:veremosmaisadianteque,pelofatodeestaremarma-
zenadosemumbancodedados,osprogramaspodemseragrupados
dentrodepacotes,oquepermitequenósosorganizemoseestrutu-
remosdeacordocomseusescopos,viabilizandoamodularizaç ãodo
sistema.
Osprogramasarmazenadospodemserdetrêstipos: procedimentos(
procedures),fun ções( functions)epacotes( packages). Aescolha
deumoudeoutrovaidependerdanecessidadeoudacaracterísticadopro-
grama.Trataremosnestecapítulode procedurese functions.Falaremos
sobre packagesnocapítuloaseguir.
16.1 procedures e functions
Paraqueumprogramasejaarmazenadoemumbancodedados,eleprecisa
receberumnomeúnico,chamadodeidentificador,queserásuaidentificaç ão
dentrodobancodedados.Éporelequevamosmanipulá-lo,localizá-lono
bancodedados,ouexecutá-lo. Anomenclaturautilizadaparanomeareste
226

## Página 238

CasadoCódigo Capítulo16. Programasarmazenados
identificadorsegueasmesmasregrasdosidentificadoresdevariáveisecons-
tantesvistosemcapítulosanteriores:elepodeterumtamanhomáximode
30caracteres,queserestringemaalgunscaracteresespeciais,nasuamaioria,
caracteresalfanuméricos;edeveiniciarporumaletra.
Depoisdecriados, osprogramasarmazenadospodemserexecutados
atravésdeferramentastaiscomoSQL*Plus,OracleForms,OracleReports
etc.,bemcomopodemserchamadosporoutrosprogramasarmazenadosou
porblocosPL/SQLanônimos.
Tambémtemosaop çãodecriar procedurese functionsdentrode
blocosPL/SQLanônimosoudentrodeoutras procedures, functions,
triggersou packages.Contudo,suasdefiniçõesnãoficamarmazenadas
dentrododicionáriodeobjetosdoOracle,apenasdentrodoobjetoondeestão
sendocriadas.
Conformeditoanteriormente,aescolhadotiponomomentodecriarum
programaarmazenadodependedanecessidade,oumelhor,doescopoem
queseencaixa. Porexemplo,quandoqueremosqueumprogramaretorne
umainformação,podemoscriá-locomo function.Estetipodeprograma
armazenado,alémdeexecutaralgumaaç ão,podeaindaretornarumtipode
informaçãoparaoprogramachamadorouparaaferramentaqueoexecutou.
Umexemploseriaumafun çãoqueretornasseseonúmerodeCPFéválido
ounão.
Casonãosejanecessárioretornarumainformaç ão,podemoscriaropro-
gramacomosendouma procedure. Nestecaso,elaexecutasuasa ções
comoumprogramaqualquer,masnãoretornanada(veremosmaisadiante
queépossível,sim,terretornoatravésdeprocedures).Oquedeveficarclaroé
quefun çõessempredevemretornarumvalor,jáprocedimentosnãopossuem
estaobrigatoriedade.Vejaaseguirumexemplode procedure.
SQL> create procedure calc is
2 --
3 x1 number := 10;
4 x2 number := 5;
5 op varchar2(1) := '+';
6 res number;
7 --
8 begin
227

## Página 239

16.1. proceduresefunctions CasadoCódigo
9 if (x1 + x2) = 0 then
10 dbms_output.put_line('Resultado: 0');
11 elsif op = '*' then
12 res := x1 * x2;
13 elsif op = '/' then
14 if x2 = 0 then
15 dbms_output.put_line('Erro de divisão por zero!');
16 else
17 res := x1 / x2;
18 end if;
19 elsif op = '-' then
20 res := x1 - x2;
21 if res = 0 then
22 dbms_output.put_line('Resultado igual a zero!');
23 elsif res < 0 then
24 dbms_output.put_line('Resultado menor que zero!');
25 elsif res > 0 then
26 dbms_output.put_line('Resultado maiorl a zero!');
27 end if;
28 elsif op = '+' then
29 res := x1 + x2;
30 else
31 dbms_output.put_line('Operador inválido!');
32 end if;
33 dbms_output.put_line('Resultado do cálculo: '||res);
34 end;
35 /
Procedimento criado.
SQL>
Oprocedimentoanteriortemoobjetivoderealizarcálculosnuméricos.
Notequebasicamente,oquemudadeuma procedureparaumblocoanô-
nimoéquenelatemosumcabe çalhoondeinformamosumidentificador,
nestecaso, calc,queprecedeocomando create procedure eantecede
ocomando isqueindicaoiníciodoprocedimento.Apósisso,temosbasica-
menteumblocoPL/SQLcomumaoquejávimosatéaqui.Omesmoacontece
228

## Página 240

CasadoCódigo Capítulo16. Programasarmazenados
comacriaç ãodefun ções.
Agoravejamosumexemplode function.
SQL> create function valida_cpf return varchar2 is
2 --
3 m_total number default 0;
4 m_digito number default 0;
5 cpf varchar2(50) default '02411848430';
6 --
7 begin
8 for i in 1 ..9 loop
9 m_total := m_total + substr (cpf, i, 1) * (11 - i);
10 end loop;
11 --
12 m_digito := 11 - mod (m_total, 11);
13 --
14 if m_digito > 9 then
15 m_digito := 0;
16 end if;
17 --
18 if m_digito != substr (cpf, 10, 1) then
19 return 'I';
20 end if;
21 --
22 m_digito := 0;
23 m_total := 0;
24 --
25 for i in 1..10 loop
26 m_total := m_total + substr (cpf, i, 1) * (12 - i);
27 end loop;
28 --
29 m_digito := 11 - mod (m_total, 11);
30 --
31 if m_digito > 9 then
32 m_digito := 0;
33 end if;
34 --
35 if m_digito != substr (cpf, 11, 1) then
36 return 'I';
229

## Página 241

16.1. proceduresefunctions CasadoCódigo
37 end if;
38 --
39 return 'V';
40 --
41 end valida_cpf;
42 /
Função criada.
SQL>
Essafun çãotemoobjetivodevalidarumnúmerodeCPFeretornarfalso
ouverdadeiro,dependendodavalidaç ão.Igualmenteàsprocedures,têm-se
umcabe çalhoondedefinimosumidentificadorparaafun ção,nesteexem-
plo, valida_cpf,queprecedeocomando create function eantecede
oscomandos return,seguidopelotipodedadoaserretornado,e isin-
dicandooiníciodafun ção.Logoapós,temosacodificaç ãodafun çãodentro
deumblocoPL/SQL.
Comocomentamosanteriormente, procedurese functionstam-
bémpodemsercriadasdentrodeblocosPL/SQLanônimosoudentrodeob-
jetos. Aseguir,utilizamososmesmosobjetosdosexemplosanteriorespara
mostrarcomoissoéfeito.
Procedurecriadanobloco:
SQL> declare
2 --
3 procedure calc is
4 --
5 x1 number := 10;
6 x2 number := 5;
7 op varchar2(1 ) := '+';
8 res number;
9 --
10 begin
11 if (x1 + x2) = 0 then
12 dbms_output.put_line('Resultado: 0');
13 elsif op = '*' then
14 res := x1 * x2;
230

## Página 242

CasadoCódigo Capítulo16. Programasarmazenados
15 elsif op = '/' then
16 if x2 = 0 then
17 dbms_output.put_line('Erro de divisão por zero!');
18 else
19 res := x1 / x2;
20 end if;
21 elsif op = '-' then
22 res := x1 - x2;
23 if res = 0 then
24 dbms_output.put_line('Resultado igual a zero!');
25 elsif res < 0 then
26 dbms_output.put_line('Resultado menor que zero!');
27 elsif res > 0 then
28 dbms_output.put_line('Resultado maiorl a zero!');
29 end if;
30 elsif op = '+' then
31 res := x1 + x2;
32 else
33 dbms_output.put_line('Operador inválido!');
34 end if;
35 dbms_output.put_line('Resultado do cálculo: '||res);
36 end;
37 --
38 begin
39 calc;
40 end;
41 /
Resultado do cálculo: 15
Procedimento PL/SQL concluído com sucesso.
SQL>
Nesseexemplo,épossívelverificarquea procedurefoicriadanonível
dobloco,ouseja,eleexisteapenasdentrodoblocoenãoestáarmazenada
nobancodedados. Logo,casosejadenossavontadeutilizá-lanovamente,
teremosquesalvartodoocódigodoblocoemumarquivoexterno. Desta
forma,tambémnãoépossívelqueoutrosprogramasusem-na.Notetambém
quenestescasosnãousamosocomando create.Come çamosdiretopelo
231

## Página 243

16.1. proceduresefunctions CasadoCódigo
tipodoprograma,a procedure.
Functioncriadaemuma procedure.
SQL> declare
2 --
3 res varchar2(1) default null;
4 --
5 function valida_cpf return varchar2 is
6 --
7 m_total number default 0;
8 m_digito number default 0;
9 cpf varchar2(50) default '02411848430';
10 --
11 begin
12 for i in 1..9 loop
13 m_total := m_total + substr (cpf, i, 1) * (11 - i);
14 end loop;
15 --
16 m_digito := 11 - mod (m_total, 11);
17 --
18 if m_digito > 9 then
19 m_digito := 0;
20 end if;
21 --
22 if m_digito != substr (cpf, 10, 1) then
23 return 'I';
24 end if;
25 --
26 m_digito := 0;
27 m_total := 0;
28 --
29 for i in 1..10 loop
30 m_total := m_total + substr (cpf, i, 1) * (12 - i);
31 end loop;
32 --
33 m_digito := 11 - mod (m_total, 11);
34 --
35 if m_digito > 9 then
36 m_digito := 0;
232

## Página 244

CasadoCódigo Capítulo16. Programasarmazenados
37 end if;
38 --
39 if m_digito != substr (cpf, 11, 1) then
40 return 'I';
41 end if;
42 --
43 return 'V';
44 --
45 end valida_cpf;
46 --
47 begin
48 res := valida_cpf;
49 --
50 if res = 'V' then
51 dbms_output.put_line('CPF válido');
52 else
53 dbms_output.put_line('CPF inválido');
54 end if;
55 --
56 end;
57 /
CPF inválido
Procedimento PL/SQL concluído com sucesso.
SQL>
Omesmoaconteceaquicomoexemplodestafun ção.Comoelaestácri-
adanoníveldobloco,elanãoseencontraarmazenadanobancodedados.
Notetambémquenestescasosnãousamosocomando create. Começa-
mosdiretopelotipodoprograma,a function.
Uma procedurepodeserchamadadedentrodeumblocoPL/SQL,de
dentrodeprogramasemOracleForms,OracleReportsetc.Entretanto,elas
nãopodemserchamadasatravésdeumcomandoSQL.Jáas functions
podemserchamadastambémdedentrodecomandosSQL,pelofatodeelas
retornaremumvalor.Contudo,háalgumasrestrições,porexemplo,elanão
podeteremsuacomposiç ãocomandosDML,DDLeDCL,apenas selects.
outracaracterísticadas functionséarecursividade,comaqualpodemos
233

## Página 245

16.1. proceduresefunctions CasadoCódigo
criarumafun çãoquechamaelamesma.
Os procedimentos podem ser chamados de duas formas. Se estiver-
mos trabalhando com SQL*Plus podemos chamá-la através do comando
execute,eatravésdeumblocoPL/SQLanônimoouprogramaarmazenado.
Vejaosdoisexemplosdechamadaaseguir.
SQL> execute calc;
Resultado do cálculo: 15
Procedimento PL /SQL concluído com sucesso.
SQL>
SQL> begin
2 calc;
3 end;
4 /
Resultado do cálculo: 15
Procedimento PL /SQL concluído com sucesso.
SQL>
Assimcomonosprocedimentos,asfun çõestambémpodemserchama-
dasdeduasformas.UmaatravésdeblocosPL/SQLanônimosouprogramas
armazenados,eatravésdecomandosSQL( select, insert, deleteou
update).ValeressaltarqueparachamadasviacomandoSQLexistemalgu-
masrestrições.Vejaosdoisexemplosdechamadaaseguir.
SQL> declare
2 --
3 res varchar2(1) default null;
4 --
5 begin
6 res := valida_cpf;
7 --
8 if res = 'V' then
9 dbms_output.put_line('CPF válido');
10 else
234

## Página 246

CasadoCódigo Capítulo16. Programasarmazenados
11 dbms_output.put_line('CPF inválido');
12 end if;
13 --
14 end;
15 /
CPF inválido
Procedimento PL/SQL concluído com sucesso.
SQL>
SQL> select decode(valida_cpf,'V','Válido','inválido') CPF
from dual;
CPF
---------
inválido
SQL>
Concedendo acesso a procedures e functions
Umavantagemnousode procedurese functionsestárelacionadaà
restriçãodeacesso.Objetoscriadosnobancodedadosprecisamdepermissão
paraacesso,casoquemosqueiraacessarnãosejaodonoouDBAdosistema.
Paradaracessoa procedurese functionsutilizamosocomando grant
execute.
SQL> grant execute on calc to public;
Concessão bem- sucedida.
SQL> grant execute on valida_cpf to TSQL2;
Concessão bem- sucedida.
SQL>
Tambémépossívelcriarmossinônimosparafacilitaroacesso.Ossinô-
nimospodemserespecíficosaumusuáriooupúblico.Valeressaltarqueeles
235

## Página 247

16.2. Usodocomandoreplace CasadoCódigo
nãodãoacesso,apenaspermitemcriarum aliasparaoobjeto.
SQL> create public synonym calc_valores for tsql.calc;
Sinônimo criado.
SQL> create synonym tsql2.valida_cpf for tsql.valida_cpf;
Sinônimo criado.
SQL>
Note que podemos dargrants e criar sinônimos para o usuário
public. Quandofazemosdestaforma,todososusuáriosdobancodeda-
dosterãoacessoaoreferidoobjeto.
16.2 U so do comando replace
Quandoprecisamosdarmanuten çãoem procedurese functions,po-
demosutilizaracláusula replaceparagarantirquealgumasdefiniçõesse-
jampreservadas. Comoessesobjetospossuemumidentificadorúnico,não
épossívelcriaroutrocomomesmonome.Logo,pararecriarmosumobjeto
comoestenóspodemosutilizaracláusula replace. Casocontrário,seria
necessárioexcluiroobjetoexistenteecriá-lonovamente.Comisto,informa-
çõesreferentesapermissõesdeacessoseriamexcluídastambém. Jácomo
comando replace,estetipodeinformaç ãopermanece,assimcomoamar-
caçãodeobjetosdependentespararecompilaç ão.
Comrelaçãoàdependênciadeobjetos,daqualfalaremosmaisàfrente,
sóparaumentendimentoprévio,écomumtermosprogramasquechamam
outrosprogramas,acabandoporcriardependênciasentreeles,oquepode
invalidartodoumconjuntodeobjetoscasoumsejaexcluídoouinvalidado.
Emalgunscasos,oOraclepoderárecompilarobjetos,automaticamente(de-
pendendodoníveldedependência),quandosãorecriados,enãoexcluídose
criadoslogoemseguida.
outravantagemdocomando replaceéapossibilidadedecriarobje-
tosmesmocomerrosdesintaxeemseuscódigos. Nessecaso,elesperma-
236

## Página 248

CasadoCódigo Capítulo16. Programasarmazenados
neceminválidosenquantotaiserrosexistirem. Aseguirousodocomando
replace.
SQL> create or replace procedure calc is
2 --
3 x1 number := 10;
4 x2 number := 5;
5 op varchar2(1) := '+';
6 res number;
7 --
8 begin
9 if (x1 + x2) = 0 then
10 dbms_output.put_line('Resultado: 0');
11 elsif op = '*' then
12 res := x1 * x2;
13 elsif op = '/' then
14 if x2 = 0 then
15 dbms_output.put_line('Erro de divisão por zero!');
16 else
17 res := x1 / x2;
18 end if;
19 elsif op = '-' then
20 res := x1 - x2;
21 if res = 0 then
22 dbms_output.put_line('Resultado igual a zero!');
23 elsif res < 0 then
24 dbms_output.put_line('Resultado menor que zero!');
25 elsif res > 0 then
26 dbms_output.put_line('Resultado maiorl a zero!');
27 end if;
28 elsif op = '+' then
29 res := x1 + x2;
30 else
31 dbms_output.put_line('Operador inválido!');
32 end if;
33 dbms_output.put_line('Resultado do cálculo: '||res);
34 end;
35 /
237

## Página 249

16.3. Recompilandoprogramasarmazenados CasadoCódigo
Procedimento criado.
SQL>
16.3 R ecompilando programas armazenados
Quandoalteramosuma procedureou functionnobancodedados,pode
acontecerdetermosquecompilá-lanovamente. Paraisso,utilizamosoco-
mando alter.Vejaosexemplos:
SQL> alter procedure calc compile;
Procedimento alterado.
SQL> alter function valida_cpf compile;
Função alterada.
SQL>
16.4 R ecuperando informações
Paravisualizarinformaçõesreferentesa procedurese functionsutilize
as views user_objects, all_objectsou dba_objects. Nestaview
constaminformaçõescomo STATUSedatadecriaç ãodoobjeto.
SQL> select owner, object_type, status, created, last_ddl_time
2 from all_objects where object_name = 'CALC';
OWNER OBJECT_TYPE STATUS
------------------------------ ------------------- -------
TSQL procedure VALID
createD LAST_DDL
-------- --------
25/11/11 25/11/11
SQL>
238

## Página 250

CasadoCódigo Capítulo16. Programasarmazenados
Outraformaderecuperardadosreferentesa procedurese functions
éutilizandoocomando describe.Estecomandomostrainformaçõesre-
ferentesaestesobjetos,comodadosdocabe çalhoeparâmetrosexistentes.
SQL> desc calc
procedure calc
Nome do Argumento Tipo
------------------------------ -----------------------
X1 NUMBER
X2 NUMBER
OP VARCHAR2
RES VARCHAR2
in/out Default?
------ --------
in
in
in
out
SQL>
16.5 R ecuperando códigos
Jáparavisualizarocódigodosobjetosarmazenadosnobancodedados,uti-
lizeasviews user_source, all_sourceou dba_source.
SQL> column text format a100
SQL> set pages 1000
SQL> select line, text
2 from all_source where name = 'CALC';
LinE TEXT
-------- --------------------------------------------------------
1 procedure calc is
2 --
3 x1 number := 10;
4 x2 number := 5;
239

## Página 251

16.6. Visualizandoerrosdecompilação CasadoCódigo
5 op varchar2(1) := '+';
6 res number;
7 --
8 begin
9 if (x1 + x2) = 0 then
10 dbms_output.put_line( 'Resultado: 0');
11 elsif op = '*' then
12 res := x1 * x2;
13 elsif op = '/' then
14 if x2 = 0 then
15 dbms_output.put_line('Erro de divisão por zero!');
16 else
17 res := x1 / x2;
18 end if;
19 elsif op = '-' then
20 res := x1 - x2;
21 if res = 0 then
22 dbms_output.put_line('Resultado igual a zero!');
23 elsif res < 0 then
24 dbms_output.put_line('Resultado menor que zero!');
25 elsif res > 0 then
26 dbms_output.put_line('Resultado maiorl a zero!');
27 end if;
28 elsif op = '+' then
29 res := x1 + x2;
30 else
31 dbms_output.put_line( 'Operador inválido!');
32 end if;
33 dbms_output.put_line('Resultado do cálculo: '||res);
34 end;
34 linhas selecionadas.
SQL>
16.6 V isualizando erros de compilação
Paravisualizarerrosdecompilaç ão,useocomando show error.
240

## Página 252

CasadoCódigo Capítulo16. Programasarmazenados
SQL> create or replace procedure calc is
2 --
3 x1 number := 10;
4 x2 number := 5;
5 op varchar2(1) := '+';
6 res number;
7 --
8 begin
9 if (x1 + x2) = 0 then
10 dbms_output.put_line('Resultado: 0');
11 elsif op = '*' then
12 res := x1 * x2;
13 elsif op = '/' then
14 if x2 = 0 then
15 dbms_output.put_line('Erro de divisão por zero!');
16 else
17 res := x1 / x2;
18 end if;
19 elsif op = '-' then
20 res := x1 - x2;
21 if res = 0 then
22 dbms_output.put_line('Resultado igual a zero!');
23 elsif res < 0 then
24 dbms_output.put_line('Resultado menor que zero!');
25 elsif res > 0 then
26 dbms_output.put_line('Resultado maiorl a zero!');
27 end if;
28 elsif op = '+' then
29 res := x1 + x2;
30 else
31 dbms_output.put_line('Operador inválido!');
32 end if;
33 dbms_output.put_line('Resultado do cálculo: '||res);
34 ; -- provocando um erro de sintaxe.
35 end;
36 /
Advertência: Procedimento criado com erros de compilação.
241

## Página 253

16.6. Visualizandoerrosdecompilação CasadoCódigo
SQL> show error
Erros para procedure CALC:
LinE/COL ERROR
-------- --------------------------------------------------------
34/3 PLS-00103: Encontrado o símbolo ";" quando um dos
seguintes símbolos era esperado:
begin case declare end exception exit for goto if loop
mod null pragma raise return select update while with
<um identificador>
<um identificador delimitado por aspas duplas>
<uma variável de ligação> << close current delete fetch
lock insert open rollback savepoint set sql execute
commit forall merge pipe
O símbolo "exit" foi substituído por ";" para continuar.
SQL>
Ocomandobasicamentemostraduascolunas. Aprimeiracomali-
nhaeacolunaondeocorreuoerro,easegunda,acolunacomadescriç ão.
Esteerrotambémpodeserencontradoatravésdasviews user_errors,
all_errorse dba_errors.
SQL> select line
2 ,position
3 ,text
4 from user_errors
5 where name = 'CALC';
LinE POSITION TEXT
----- --------- -------------------------------------------------
34 3 PLS-00103: Encontrado o símbolo ";" quando um
dos seguintes símbolos era esperado:
begin case declare end exception exit
for goto if loop mod null pragma raise
return select update while with
<um identificador> <um identificador
delimitado por aspas duplas>
242

## Página 254

CasadoCódigo Capítulo16. Programasarmazenados
<uma variável de ligação> << close
current delete fetch
lock insert open rollback savepoint
setsql execute commit
forall merge pipe
O símbolo "exit" foi substituído por ";"
para continuar.
SQL>
16.7 P assando parâmetros
Programasarmazenados,como procedurese functions,permitemtra-
balharcompassagemdeparâmetros.Quandocriamosumprocedimentoou
umafun ção,podemosespecificarparâmetrosdeentradaesaídaparaqueva-
lorespossamserlevadosparadentrodestesprogramasourecuperadosdeles.
Osparâmetrospodemserdotipo in, outou in out. indefineque
setratadeumparâmetrodeentrada. Jáumparâmetrodotipo outindica
queeleédesaída.Logo, in out indicaumparâmetrodeentradaesaída.
Quandoestamosfalandodeparâmetrosdeentrada( in),issoquerdi-
zerqueosvalorescontidosnelespodemseratribuídosaoutrasvariáveisou
parâmetrosexistentesdentroda procedureou function.Contudo,não
podemosatribuirvaloresaeles.Jáquandoestamosfalandodosparâmetros
desaída( out),estamosdizendoqueosvaloresdestesparâmetrospodem
seralterados,masnãoatribuídosaoutrasvariáveisouparâmetrosexistentes
dentrodestesobjetos.
Logo,quandotemosparâmetrosdotipo in out sendousados,issoin-
dicaquetantopodemosatribuirvaloresaelecomotambématribuirseusva-
loresaoutrasvariáveisouparâmetrosexistentesdentrodosobjetos.Vejaisso
naprática.
procedure exemplo( param1 in number
,param2 out number
,param3 in out number ) is
--
243

## Página 255

16.7. Passandoparâmetros CasadoCódigo
x number;
y number;
z number;
--
begin
--
x := param1; -- uso correto
param1 := x; -- uso incorreto
--
y := param2; -- uso incorreto
param2 := y; -- uso correto
--
z := param3; -- uso correto
param3 := z; -- uso correto
--
end;
/
Nota:quandonãoinformamosotipodoparâmetro,porpadrão,ele
serádotipo in.
Ousodeparâmetrosemprogramasarmazenadospodetornarnossos
programasmuitomaisflexíveis,possibilitandooreaproveitamentodecódigo.
Aseguir,sãomostradososmesmosexemplosde procedurese functions
anteriores,masagorarecriadosutilizandopassagemdeparâmetros.
SQL> create or replace procedure calc ( x1 in number
2 ,x2 in number
3 ,op in varchar2
4 ,res out varchar2) is
5 --
6 begin
7 --
8 if (x1 + x2) = 0 then
9 res := 0;
10 elsif op = '*' then
11 res := x1 * x2;
244

## Página 256

CasadoCódigo Capítulo16. Programasarmazenados
12 elsif op = '/' then
13 if x2 = 0 then
14 res := 'Erro de divisão por zero!';
15 else
16 res := x1 / x2;
17 end if;
18 elsif op = '-' then
19 res := x1 - x2;
20 if res = 0 then
21 res := 'Resultado igual a zero: '||res;
22 elsif res < 0 then
23 res := 'Resultado menor que zero: '||res;
24 elsif res > 0 then
25 res := 'Resultado maior que zero: '||res;
26 end if;
27 elsif op = '+' then
28 res := x1 + x2;
29 else
30 res := 'Operador inválido!';
31 end if;
32 --
33 end;
34 /
Procedimento criado.
SQL>
Executando calc:
SQL> declare
2 wres varchar2(100);
3 begin
4 calc ( x1 => 10
5 ,x2 => 5
6 ,op => '*'
7 ,res => wres);
8 --
9 dbms_output.put_line('Resultado Calc 1: '||wres);
10 --
245

## Página 257

16.7. Passandoparâmetros CasadoCódigo
11 calc ( 10
12 ,5
13 ,'/'
14 ,wres);
15 --
16 dbms_output.put_line('Resultado Calc 2: '||wres);
17 --
18 end;
19 /
Resultado Calc 1: 50
Resultado Calc 2: 2
Procedimento PL /SQL concluído com sucesso.
SQL>
Percebaquenestaexecuç ãochamamosduasvezesa procedure.Apri-
meirausandoapassagemdeparâmetrosnomeada,easegundasemnomea-
ção.Quandoinformamososparâmetrosnocabe çalhodoprograma,oOracle
tomacomoordenaçãoaordememqueosdispomos.Todavia,quandoexecu-
tamostalprogramaprecisamosrespeitarestaordem.Portanto,quandono-
meamosapassagemdeparâmetros,nomomentodaexecuç ãodoprograma,
nãoprecisamosnecessariamenteinformá-losnaordemcomaqualforamde-
finidos,bastaapenasinformarseusnomeseosrespectivosvaloresaserem
atribuídos.
SQL> create or replace function valida_cpf (cpf in char) return
varchar2 is
2 --
3 m_total number default 0;
4 m_digito number default 0;
5 --
6 begin
7 for i in 1 ..9 loop
8 m_total := m_total + substr (cpf, i, 1) * (11 - i);
9 end loop;
10 --
11 m_digito := 11 - mod (m_total, 11);
246

## Página 258

CasadoCódigo Capítulo16. Programasarmazenados
12 --
13 if m_digito > 9 then
14 m_digito := 0;
15 end if;
16 --
17 if m_digito != substr (cpf, 10, 1) then
18 return 'I';
19 end if;
20 --
21 m_digito := 0;
22 m_total := 0;
23 --
24 for i in 1..10 loop
25 m_total := m_total + substr (cpf, i, 1) * (12 - i);
26 end loop;
27 --
28 m_digito := 11 - mod (m_total, 11);
29 --
30 if m_digito > 9 then
31 m_digito := 0;
32 end if;
33 --
34 if m_digito != substr (cpf, 11, 1) then
35 return 'I';
36 end if;
37 --
38 return 'V';
39 --
40 end valida_cpf;
41 /
Função criada.
SQL>
Executando valida_cpf:
SQL> declare
2 --
3 res varchar2(1) default null;
247

## Página 259

16.7. Passandoparâmetros CasadoCódigo
4 --
5 begin
6 res := valida_cpf(cpf => '02091678520');
7 --
8 if res = 'V' then
9 dbms_output.put_line('CPF válido: 02091678520');
10 else
11 dbms_output.put_line('CPF inválido: 02091678520');
12 end if;
13 --
14 res := valida_cpf('02011648920');
15 --
16 if res = 'V' then
17 dbms_output.put_line('CPF válido: 02011648920');
18 else
19 dbms_output.put_line('CPF inválido: 02011648920');
20 end if;
21 --
22 end;
23 /
CPF inválido: 02091678520
CPF válido: 02011648920
Procedimento PL /SQL concluído com sucesso.
SQL>
Anteriormente, mencionamos que emboraprocedures não retor-
nemvalores,vimosqueatravésdeparâmetrosdotipo outistoépossível.
Contudo,as proceduresnãoretornamvaloresimplicitamentecomoas
functions.Valelembrarque,emboraas functionsretornemvalor,nós
podemosutilizarparâmetrosdotipo outemsuadefiniç ão,mesmoporque
uma functionsópoderetornarumúnicovalorporchamada,enquanto
atravésdosparâmetrosdotipo outépossívelterváriosretornos.
248

## Página 260

CasadoCódigo Capítulo16. Programasarmazenados
16.8 D ependência de objetos
Édefundamentalimportânciaqueodesenvolvedorconhe çacomooOracle
trataaquestãodadependênciaentreosobjetosarmazenadosnobancode
dados.Existemcasosemqueoprópriodesenvolvedoréquemvailiberaros
objetosnabasededados,sendoelaumabasetesteouatéemumabasede
produção. Diantedisto,ésemprebomsaberoquepodeacontecerquando
liberamosobjetosquepossuemdependênciasentresi.
OOracletrabalhaemcimadedoisconceitoscomrelaç ãoaestetipode
dependência.Osconceitosde dependência diretae dependência indireta.
ConformeestánadocumentaçãodaOracle,quandosetratadeumadepen-
dênciadiretaoOracleconseguerestabeleceroprogramaqueestáinválido.
Jáquandonãosetratadeumadependênciadireta,oOraclenãogaranteque
esterestabelecimentosejafeitodeformaautomática.Vamosverificarasca-
racterísticasreferentesàsdependênciasdiretaseindiretasentreobjetos.
Paraevidenciarasdiferen çasentreostiposdedependências,criaremos
exemplospráticos.Paracome çar,vamospartirdopontoondetemosquatro
procedureschamadas: proc1, proc2, proc3e proc4.
SQL> create or replace procedure proc4 is
2 begin
3 dbms_output.put_line('proc. 4!!!');
4 end;
5 /
Procedimento criado.
SQL> create or replace procedure proc3 is
2 begin
3 dbms_output.put_line('proc. 3!!!');
4 proc4;
5 end;
6 /
Procedimento criado.
SQL> create or replace procedure proc2 is
249

## Página 261

16.8. Dependênciadeobjetos CasadoCódigo
2 begin
3 dbms_output.put_line('proc. 2!!!');
4 proc3;
5 end;
6 /
Procedimento criado.
SQL> create or replace procedure proc1 is
2 begin
3 dbms_output.put_line('proc. 1!!!');
4 proc2;
5 end;
6 /
Procedimento criado.
SQL>
Observandoosscriptsanteriores, vemosquea procedure proc1
chamaa proc2ea proc2chamaa proc3atéchegarmosà procedure
proc4.Nestecaso,podemosidentificarosdoiscasosdedependênciaosquais
estamosabordando.
Adependênciadiretaestárepresentadanasseguintessituações: proc1
com proc2, proc2com proc3e proc3com proc4.Ouseja,aprocedure
proc2mantémumadependênciacoma procedure proc1,poisparaa
proc2serexecutadaéprecisoquea proc1sejaexecutadatambém.Logo,a
proc2precisaestarválidaparaquea proc1estejavalidada.Assimacontece
coma procedure proc2 quemantémumadependênciacoma proc3ea
procedure proc3 coma proc4.
Adependênciaindiretaestárepresentadanassituaçõesseguintes: proc1
com proc3, proc2com proc4, proc1com proc4. Damesmaforma
quenadependênciadireta,aprocedure proc1precisaserexecutadapara
quea proc3tambémseja(indiretamente).Logo,avalidaç ãoda procedure
proc3precisaexistirparaquea proc1tambémestejaválida.Vejaodesenho.
250

## Página 262

CasadoCódigo Capítulo16. Programasarmazenados
Fig.16.1:Esquemamostrandodependênciasdiretaseindiretas
Para verificar as dependências entre os objetos, podemos fazer um
selectnaview all_dependencies,ondeconstamtodasasdependên-
ciasexistentesentresosobjetoscriadosnabasededados.Paralimitarmosa
pesquisa,vamosselecionarasdependênciasreferentesaosobjetosquecria-
mos,informandoosnomesdosmesmosnacláusula wheredo select.
251

## Página 263

16.8. Dependênciadeobjetos CasadoCódigo
SQL> select name || ' => ' ||referenced_name "Referências"
2 from all_dependencies
3 where owner = 'TSQL'
4 and name in ( 'PROC1'
5 ,'PROC2'
6 ,'PROC3'
7 ,'PROC4'
8 )
9 and referenced_type = 'procedure'
10 order by name
11 /
Referências
-----------------------------------------------------------
PROC1 => PROC2
PROC2 => PROC3
PROC3 => PROC4
SQL>
Jáparaverificarosstatusdosobjetos,devemosfazerum selectnaview
all_objects,selecionandoocampo STATUS.
SQL> select object_name
2 ,status
3 from all_objects
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure'
11 /
OBJECT_NAME STATUS
------------------------------ -------
PROC1 VALID
PROC2 VALID
252

## Página 264

CasadoCódigo Capítulo16. Programasarmazenados
PROC3 VALID
PROC4 VALID
SQL>
Paratornarmaisclaraaexplanaç ãosobreasdependênciasentreobjetos,
nasequênciaestãoalgunsexemplosrelacionadosaosconceitosexpostosan-
teriormente:
Criandoobjetosforadaordemdedependência.Comojáhavíamoscriado
osobjetosanteriormente,vamosprimeiramenteexcluí-los.
SQL> drop procedure proc1;
Procedimento eliminado.
SQL> drop procedure proc2;
Procedimento eliminado.
SQL> drop procedure proc3;
Procedimento eliminado.
SQL> drop procedure proc4;
Procedimento eliminado.
SQL>
Apósexcluircada procedure,vamoscriá-lasnovamente.
SQL> create or replace procedure proc1 is
2 begin
3 dbms_output.put_line('proc. 1!!!');
4 proc2;
5 end;
6 /
Advertência: Procedimento criado com erros de compilação.
253

## Página 265

16.8. Dependênciadeobjetos CasadoCódigo
SQL>
SQL> create or replace procedure proc2 is
2 begin
3 dbms_output.put_line('proc. 2!!!');
4 proc3;
5 end;
6 /
Advertência: Procedimento criado com erros de compilação.
SQL>
SQL> create or replace procedure proc3 is
2 begin
3 dbms_output.put_line('proc. 3!!!');
4 proc4;
5 end;
6 /
Advertência: Procedimento criado com erros de compilação.
SQL>
SQL> create or replace procedure proc4 is
2 begin
3 dbms_output.put_line('proc. 4!!!');
4 end;
5 /
Procedimento criado.
SQL>
Vejaque proc1, proc2e proc3foramcriadascomadvertência.Con-
tudo,a proc4foicriadacomsucesso. Agoravamosverificarosstatusdos
objetos.
SQL> select object_name
2 ,status
254

## Página 266

CasadoCódigo Capítulo16. Programasarmazenados
3 from all_objects
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure';
OBJECT_NAME STATUS
------------------------------ -------
PROC1 INVALID
PROC2 INVALID
PROC3 INVALID
PROC4 VALID
SQL>
Comoeraprevisto,as procedures PROC1, PROC2e PROC3estão
inválidas,enquantoa PROC4estáválida. Istoocorreupelofatodequena
ordememqueosobjetosforamcriadossemprefaltavaacriaç ãodoobjeto
dependente,comexce ção,éclaro,doobjeto PROC4.
Criandoosobjetosnaordemdedependência:
SQL> create or replace procedure proc4 is
2 begin
3 dbms_output.put_line('proc. 4!!!');
4 end;
5 /
Procedimento criado.
SQL> create or replace procedure proc3 is
2 begin
3 dbms_output.put_line('proc. 3!!!');
4 proc4;
5 end;
6 /
Procedimento criado.
SQL> create or replace procedure proc2 is
255

## Página 267

16.8. Dependênciadeobjetos CasadoCódigo
2 begin
3 dbms_output.put_line('proc. 2!!!');
4 proc3;
5 end;
6 /
Procedimento criado.
SQL> create or replace procedure proc1 is
2 begin
3 dbms_output.put_line('proc. 1!!!');
4 proc2;
5 end;
6 /
Procedimento criado.
SQL>
VerificandoObjetos.
SQL> select object_name
2 ,status
3 from all_objects
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure'
11 /
OBJECT_NAME STATUS
------------------------------ -------
PROC1 VALID
PROC2 VALID
PROC3 VALID
PROC4 VALID
SQL>
Invalidandooobjeto PROC1:
256

## Página 268

CasadoCódigo Capítulo16. Programasarmazenados
SQL> create or replace procedure proc1 is
2 begin
3 dbms_output.put_line('proc. 1!!!');
4 ; -- provocando um erro de sintaxe
5 proc2;
6 end;
7 /
Advertência: Procedimento criado com erros de compilação.
SQL> select object_name
2 ,status
3 from all_objects
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure';
OBJECT_NAME STATUS
------------------------------ -------
PROC1 INVALID
PROC2 VALID
PROC3 VALID
PROC4 VALID
SQL>
Invalidandooobjeto PROC2:
SQL> create or replace procedure proc2 is
2 begin
3 dbms_output.put_line('proc. 2!!!');
4 ; -- provocando um erro de sintaxe
5 proc3;
6 end;
7 /
Advertência: Procedimento criado com erros de compilação.
SQL> select object_name
257

## Página 269

16.8. Dependênciadeobjetos CasadoCódigo
2 ,status
3 from all_objects
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure'
11 /
OBJECT_NAME STATUS
------------------------------ -------
PROC1 INVALID
PROC2 INVALID
PROC3 VALID
PROC4 VALID
SQL>
Invalidandooobjeto PROC3:
SQL> create or replace procedure proc3 is
2 begin
3 dbms_output.put_line('proc. 3!!!');
4 ; -- provocando um erro de sintaxe
5 proc4;
6 end;
7 /
Advertência: Procedimento criado com erros de compilação.
SQL> select object_name
2 ,status
3 from all_objects
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure'
258

## Página 270

CasadoCódigo Capítulo16. Programasarmazenados
11 /
OBJECT_NAME STATUS
------------------------------ -------
PROC1 INVALID
PROC2 INVALID
PROC3 INVALID
PROC4 VALID
SQL>
Invalidandooobjeto PROC4:
SQL> create or replace procedure proc4 is
2 begin
3 dbms_output.put_line('proc. 4!!!');
4 ; -- provocando um erro de sintaxe
5 end;
6 /
Advertência: Procedimento criado com erros de compilação.
SQL> select object_name
2 ,status
3 from all_objects
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure'
11 /
OBJECT_NAME STATUS
------------------------------ -------
PROC1 INVALID
PROC2 INVALID
PROC3 INVALID
PROC4 INVALID
SQL>
259

## Página 271

16.8. Dependênciadeobjetos CasadoCódigo
Corrigindoerecriandooobjeto PROC1:
SQL> create or replace procedure proc1 is
2 begin
3 dbms_output.put_line('proc. 1!!!');
4 proc2;
5 end;
6 /
Advertência: Procedimento criado com erros de compilação.
SQL> show error
Erros para procedure PROC1:
LinE/COL ERROR
-------- --------------------------------------------------------
4/3 PL/ SQL: Statement ignored
4/3 PLS -00905: o objeto TSQL.PROC2 é inválido
SQL>
Corrigindoerecriandooobjeto PROC2:
SQL> create or replace procedure proc2 is
2 begin
3 dbms_output.put_line('proc. 2!!!');
4 proc3;
5 end;
6 /
Advertência: Procedimento criado com erros de compilação.
SQL> show error
Erros para procedure PROC2:
LinE/COL ERROR
-------- --------------------------------------------------------
4/3 PL/ SQL: Statement ignored
4/3 PLS -00905: o objeto TSQL.PROC3 é inválido
SQL>
Corrigindoerecriandooobjeto PROC3:
260

## Página 272

CasadoCódigo Capítulo16. Programasarmazenados
SQL> create or replace procedure proc3 is
2 begin
3 dbms_output.put_line('proc. 3!!!');
4 proc4;
5 end;
6 /
Advertência: Procedimento criado com erros de compilação.
SQL> show error
Erros para procedure PROC3:
LinE/COL ERROR
-------- ---------------------------------------------------
4/3 PL/ SQL: Statement ignored
4/3 PLS -00905: o objeto TSQL.PROC4 é inválido
SQL>
Verificandoobjetos:
SQL> select object_name
2 ,status
3 from all_objects
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure'
11 /
OBJECT_NAME STATUS
------------------------------ -------
PROC1 INVALID
PROC2 INVALID
PROC3 INVALID
PROC4 INVALID
SQL>
261

## Página 273

16.8. Dependênciadeobjetos CasadoCódigo
Corrigindoevalidandooobjeto PROC4:
SQL> create or replace procedure proc4 is
2 begin
3 dbms_output.put_line('proc. 4!!!');
4 end;
5 /
Procedimento criado.
SQL> select object_name
2 ,status
3 from all_objects
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure'
11 /
OBJECT_NAME STATUS
------------------------------ -------
PROC1 INVALID
PROC2 INVALID
PROC3 INVALID
PROC4 VALID
SQL>
Recompilando PROC2:
SQL> alter procedure proc2 compile;
Procedimento alterado.
SQL> select object_name
2 ,status
3 from all_objects
262

## Página 274

CasadoCódigo Capítulo16. Programasarmazenados
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure'
11 /
OBJECT_NAME STATUS
------------------------------ -------
PROC1 INVALID
PROC2 VALID
PROC3 VALID
PROC4 VALID
SQL>
Executandoa PROC1:
SQL> execute proc1;
proc. 1!!!
proc. 2!!!
proc. 3!!!
proc. 4!!!
Procedimento PL/SQL concluído com sucesso.
SQL> select object_name
2 ,status
3 from all_objects
4 where owner = 'TSQL'
5 and object_name in ( 'PROC1'
6 ,'PROC2'
7 ,'PROC3'
8 ,'PROC4'
9 )
10 and object_type = 'procedure'
11 /
263

## Página 275

16.8. Dependênciadeobjetos CasadoCódigo
OBJECT_NAME STATUS
------------------------------ -------
PROC1 VALID
PROC2 VALID
PROC3 VALID
PROC4 VALID
SQL>
Vimosque,emboraexistamdependênciasindiretasentreosobjetos,o
Oracleconseguiuidentificaraschamadasevalidarosobjetossubsequentes.
Emboraisdotenhaocorrido,aOraclenãogarantequeemalgunscasosisto
venhaaacontecer.Diantedisto,podemosdizerqueoOracleestápreparado
pararestabelecerasvalidaçõesemcasodedependênciadiretaeindireta,con-
tudo,nãoégarantidoqueeleconseguirádetectarcertasligações.
Todavia,ésempreadequadoverificarosstatusdosobjetosapósalibera-
çãodeobjetosnovosounovasversõesnobancodedados.Dependendoda
quantidadedeobjetoscomdependência,invalidá-lospoderánoscustaral-
gumtempoatédeixarosistemaestávelnovamente.Valelembrarque,mesmo
existindoobjetosinválidosnobancodedados,podemosnãoterproblemas
nofuncionamento,casooOracle,aoexecutaralgumaoperaç ãocomumdes-
tesobjetos,detecteaexistênciadedependênciasdiretaseasrestabele ça.
264

## Página 276

Capítulo17
packages
Nocapítuloanterior,falamossobre procedurese functionsecomo
elas são armazenadas e executadas através de um banco de dados. Pois
bem, packages,tambémchamadosdepacotes,sãoprogramasarmazena-
dos,tendocomodiferencialapossibilidadedefuncionarcomorepositório
paraagruparváriosobjetosdotipo proceduree function,bemcomo
contercódigoPL/SQLouservirdeáreaparadefiniçõesdevariáveis,curso-
res,exce ções,procedimentosefun ções.
Contudo,talvezsuamaiorutilizaç ãoestejanoagrupamentodeprogra-
masquepossuemumamesmafinalidade, comoaquelesquefaç amparte
de uma área específica como RH, Financeira ou Comercial. Através de
packagesconseguimosorganizarestesprogramasdentrodeumúnicoob-
jetoedefinircomooacessoaestesobjetosserárealizado.

## Página 277

17.1. Estruturadeumpackage CasadoCódigo
17 .1 E strutura de um package
Um package pode ser constituído por até duas partes, uma chamada
especificationeoutrachamada body. Podemosterum package
especificationsem package body,contudo,nãopodemosterocon-
trário. Obrigatoriamente,paracriamosum package body énecessário
criartambémum package especification.Jávamosentenderporquê.
Dentrodo especification,podemosdeclararvariáveis, types,ca-
beçalhosde procedurese functions, exceptions,cursoresetc.,que
podemfazerounãoreferênciaaum package body. Quandoestiverfa-
zendoreferênciaaum body,podemosdizerqueo especification,como
nomesugere,funcionacomoumaespecificaç ãodo body.
Porexemplo,setemosum bodydentrodoqualháumcódigodeuma
procedure, podemos ter declarado noespecificationo cabeçalho
desteprograma,mesmoporque,pordefiniç ãodestetipodeobjeto,sócon-
seguiremosacessarumprogramaqueestáarmazenadodentrodeum body
casosuaespecificaç ãoestejadeclaradaemum especification.Poristo,
um bodynãopodeexistirsemum especification.
Casoo especificationnãofaçareferênciaaum body,elepodeestar
sendoutilizadoparadeclaraç ãodevariáveisououtrostiposdeobjetosque
nãonecessitariamdeum body.Valesalientarque,casotenhamoscabe çalhos
de procedurese functionsemum especification,sefaznecessário
queexistaum bodyrelacionado.
Jádentrodo bodyéondecolocamostodaacodificaç ãodosnossospro-
gramas,comocodificaçõesde procedurese functions. Alémdestes
objetos,tambémpodemosdeclararvariáveis,cursores,exce ções,typesetc.,
quepodemserutilizadospelorestantedosobjetoscriadosno body. No
entanto,podemosterobjetosdentrodo bodyquenãoestãodeclaradosno
especification,osquaisnãopoderãoseracessadosdiretamente,somente
atravésdeoutrosobjetoscontidosnopróprio body.Osobjetosdeclaradosno
especification,porexemplo,variáveisecursores,podemseracessados
dedentrodo body. Alémdisso,dentrodo bodypodemostercodificaç ão
PL/SQLcorrespondenteaopróprio package,poiso bodypodecontersua
própriaárea begine end.
266

## Página 278

CasadoCódigo Capítulo17. packages
Podemos ter no especification
• Especificaçãode procedurese functions;
• Declaraçãodevariáveiseconstantes;
• Declaraçãodecursores;
• Declaraçãode exceptions;
• Declaraçãode types.
Podemos ter no body
• CódigosPL/SQL;
• Códigosdeprocedurese functions;
• Declaraçãodevariáveiseconstantes;
• Declaraçãodecursores;
• Declaraçãode exceptions;
• Declaraçãode types.
Exemplode especification:
SQL> create package listagem is
2 --
3 cursor c1 is
4 select d.department_id
5 ,department_name
6 ,first_name
7 ,hire_date
8 ,salary
9 from departments d
10 ,employees e
11 where d.manager_id = e.employee_id
12 order by department_name;
267

## Página 279

17.1. Estruturadeumpackage CasadoCódigo
13 --
14 type tab is table of c1%rowtype index by binary_integer;
15 --
16 tbgerente tab;
17 n number ;
18 --
19 procedure lista_gerente_por_depto;
20 --
21 end listagem;
22 /
Pacote criado.
SQL>
Paracriarmosum package especification,utilizamosocomando
create. Seguindonossoexemplo, naprimeiralinhatemosocomando
createelogoemseguidaotipodeobjetoqueestamoscriando,nocaso,
package.Quandonãoinformamosotipo body,automaticamenteoOracle
criao packagecomosendodotipo especification.
Logodepoisdotipodeobjeto,informamosonome( listagem)seguido
daexpressão is(linha01). ispodesersubstituídopor as.Semprequefor
criarumobjeto package especification,vocêdeveutilizarestasin-
taxe.
Depois da expressão is, são declarados os objetos que poderão ou
não ser usados em umpackage body. Neste exemplo, temos um
especificationcomadeclaraç ãodealgunsobjetoscomoocursor c1,
o type tab,asvariáveis ne tbgerente,eaespecificaç ãodaproce-
dure lista_gerente_por_depto.Notequesóinformamosocabe çalho
da procedure.Logoteráqueexistirum bodyondeseucódigoestarácri-
ado.Oscabe çalhosdosobjetosinformadosdevemseridênticosaosdescritos
nocorpodo package.
Note que, nestes casos, todos os objetos, por estarem no
especification, têm seu escopo público, ou seja, qualquer usuá-
rio que tenha acesso a este objeto poderá referenciá-los em sua sessão,
utilizando-os. Todaadeclaraçãoéfinalizadaporpontoevírgula. Porfim,
268

## Página 280

CasadoCódigo Capítulo17. packages
temosocomando end(linha21),quefinalizao package.Colocarounão
onomedo packagelogoapósocomando endéopcional.Contudo,não
podemosternomesdiferentesnocabe çalhoerodapédoobjeto.
Exemplode body:
SQL> create package body listagem is
2 --
3 procedure lista_gerente_por_depto is
4 --
5 begin
6 for r1 in c1 loop
7 tbgerente(r1.department_id) := r1;
8 end loop;
9 --
10 n := tbgerente.first;
11 --
12 while n <= tbgerente.last loop
13 dbms_output.put_line(
'Depto: '||tbgerente(n).department_name||' '||
14 'Gerente: '||tbgerente(n).first_name||' '||
15 'Dt. Admi.: '||tbgerente(n).hire_date||' '||
16 'Sal.: '||to_char(tbgerente(n).salary,
'fm$999g999g990d00'));
17 n := tbgerente.next(n);
18 end loop;
19 --
20 end lista_gerente_por_depto;
21 --
22 end listagem;
23 /
Corpo de Pacote criado.
SQL>
Igualmenteaoutilizadonacriaç ãodo package especification,
para criarmos umpackage body, nós utilizamos também o comando
create. Naprimeiralinhadesteexemplo,temosocomando createe,
emseguida,otipodeobjetoqueestamoscriando,nocaso, package body.
269

## Página 281

17.2. Acessoapackages CasadoCódigo
Logodepoisdotipodeobjeto,informamosumnomeparaele( listagem),
seguidodaexpressão is(linha01),quepodesersubstituídopor as.Sempre
queforcriarumobjeto package body,vocêdeveutilizarestasintaxe.
Esteobjeto bodyfazreferênciaaoespecificationcriadonoexemplo
anterior.Neleestáocódigoda procedure lista_gerente_por_depto
(linhas3a20),declaradano especification. Noteque,nesteexemplo,
nãoutilizamosaárea begin end do bodyetambémnãodeclaramosqual-
querobjetodentrodocorpodo package.Contudo,dentroda procedure,
estamosutilizandoosobjetosqueforamdeclaradosno especification,
porexemplo,ocursor(linha6a8),otype(linha7,13a17)easvariáveis(linhas
10,12e17).
Assimcomoesta,outras procedures,casoexistissemmaisdentrodo
body,poderiamtambémacessarestesobjetos.Todavia,seelesestivessemde-
claradosno body,emvezdeno especification,oefeitoseriaomesmo.
Entretanto,oescopodestesobjetosseriainternoao body,nãopodendoser
acessadosexternamente.
Porfim,temosocomando end(linha22),quefinalizao package.Como
no especification,colocarounãoonomedo packagelogoapóso
comando endéopcional. Contudo,nãopodemosternomesdiferentesno
cabeçalhoerodapédoobjeto. Valeressaltarquetodaadeclaraç ãodeveser
finalizadaporpontoevírgula.
17 .2 A cesso a packages
Comomencionadoanteriormente,sópodemosacessarumobjetoqueseen-
contraemum bodyseeleestiverdeclaradono especification.Logo,o
especificationtemacaracterísticadeserumaáreapúblicaondetodos
osusuáriosquepossuamconcessãodeacessoaesteobjetopodemreferen-
ciarouexecutarosobjetosdo bodyporintermédiodoqueestáespecificado
nestaárea.
Tudooqueestiverdeclaradono especificationeno bodytemseu
escopononíveldeusuário,oumelhor,nasessãodousuárioqueexecutoutal
package.Osobjetos packagesócome çamaocuparrecursosnamemória
quandoalgumobjetoéreferenciado.Aáreade begin end do bodyéexe-
270

## Página 282

CasadoCódigo Capítulo17. packages
cutadaumaúnicaveznasessãodousuário,naprimeiravezqueo package
éreferenciado.
Porisso,quandoutilizada,écomumvê-laservircomolocalparainiciali-
zaçãodevariáveisouparaexecuç ãodeprocedimentosqueinicializemalgum
objetoqueseráutilizadoporoutrosobjetosaolongodavidaútildasessão.
Quantoaosobjetosdefinidosdentrodas procedurese functionsin-
ternasao body,estestêmseuescopoemnívellocaleosrecursossósão
ocupadosmedianteaexecuç ãodetais procedurese functions.
Àsvezes, packages especifications sãoutilizadascomoáreapara
declaraçãoeinicializaç ãodevariáveisoucursoresdentrodeumasessão,não
existindoum body. Comoo especificationtemseuescopoemnível
desessão,eleémuitoútilparaserusadopelosprogramasparaguardarin-
formaçõesqueserãoutilizadasemalgumprocessamentoouparadeterminar
padrõesemumsistema.Comoestasinformaçõesficamnasessãoenquanto
elaestiveraberta,todososprogramasqueestiveremsendoexecutadospo-
derãocompartilhardestaáreae,consequentemente,dosdadoseobjetosque
estãodeclaradosnela.
Resumindo,quandotrabalhamoscom packagesprecisamossaberde
algunsdetalhes:
•Packagespodemserconstituídasdeduaspartes: especification
e body.
• Umespecificationpodeexistirsemum body,masnãoocontrá-
rio.
• Quandoexistiremumespecificationeum body,osdoisobjetos
devemterexatamenteomesmonome.
• Paraacessarobjetosdedentrodeumbody,éprecisoqueelesestejam
declaradosemum especification(acessodireto),ouque,pelo
menos,possamseracessadosatravésdealgumobjetoqueestejano
especification(acessoindireto).
• Osobjetospertencentesaopackagetêmseuescopoemníveldeses-
sãodousuáriooqualexecutoutal package.
271

## Página 283

17.2. Acessoapackages CasadoCódigo
• Osobjetosdeumpackageocuparãorecursossomentequandoforem
referenciados.
• Áreascomoespecificatione begin end do bodyserãoexecu-
tadasumaúnicaveznasessãodousuário,naprimeiravezemquesão
referenciadas.
• Igualmenteaprocedurese functions,énecessárioterconcessão
deacessoparaexecutar packages.
• Comousodeespecificatione body,épossíveldisponibilizar
informaçõesemnívelglobaleemníveldeprograma,mantendoainte-
gridadeeconsistênciaatravésdeencapsulamento.
Vejanasequênciaumexemplodemaisuma packageesuaaplicaç ão.
O packageaseguiréresponsávelporefetuarcálculoscomosomatória,sub-
tração,divisãoemultiplicaç ão. Paracadaoperação,existeuma function
ondesãopassadosdoisparâmetrosreferentesaosnúmerosquesequercal-
cular.Apósocálculo,afun çãoretornaoresultado.
SQL> create package calculo as
2 --
3 function soma (x1 number, x2 number) return number;
4 function subtrai (x1 number, x2 number) return number;
5 function multiplica (x1 number , x2 number) return number;
6 function divide (x1 number, x2 number ) return number;
7 --
8 end calculo;
9 /
Pacote criado.
SQL>
Na primeira linha deste exemplo, temos o comandocreate e em
seguida o tipo de objeto que estamos criando, no caso,package (
especification). Logo depois do tipo de objeto, informamos o seu
nome (calculo) seguido da expressãoas (linha 01). No corpo do
272

## Página 284

CasadoCódigo Capítulo17. packages
especification,declaramosasfun ções soma, subtrai, multiplica
e divide(linhas3a6).Notequeaquisósãoinformadososcabe çalhosdas
funções.Porfim,temosocomando end(linha8)quefinalizao package.
Detalhessobreo package especification calculo:
• Foicriadoopackage especification chamado calculo;
• Nopackage especification foramdeclaradasquatrofun ções,
cadaumaresponsávelporumaoperaçãomatemática(soma,subtração,
multiplicaçãoedivisão).
SQL> create package body calculo as
2 --
3 res number;
4 --
5 procedure imprime_msg(msg varchar2) is
6 begin
7 dbms_output.put_line(msg);
8 end;
9 --
10 function soma (x1 number, x2 number) return number is
11 begin
12 res := x1 + x2;
13 return res;
14 end;
15 --
16 function subtrai (x1 number, x2 number) return number is
17 begin
18 res := x1 - x2;
19 --
20 if res = 0 then
21 imprime_msg('Resultado igual a zero: '||res);
22 elsif res < 0 then
23 imprime_msg('Resultado menor que zero: '||res);
24 elsif res > 0 then
25 imprime_msg('Resultado maior que zero: '||res);
26 end if;
27 --
28 return res;
273

## Página 285

17.2. Acessoapackages CasadoCódigo
29 --
30 end;
31 --
32 function multiplica (x1 number , x2 number) return
number is
33 begin
34 res := x1 * x2;
35 return res;
36 end;
37 --
38 function divide (x1 number, x2 number ) return number is
39 begin
40 if x2 = 0 then
41 res := null;
42 imprime_msg('Erro de divisão por zero!');
43 else
44 res := x1 / x2;
45 end if;
46 --
47 return res;
48 end;
49 --
50 end calculo;
51 /
Corpo de Pacote criado.
SQL>
Agoravamoscriarosegundoobjeto,queéasegundapartedonossopro-
grama.Naprimeiralinhatemosocomando createeemseguidaotipodo
objeto, package body,comseunome, calculo,eaexpressão as(linha
1).Declaramosumavariávelchamada resnocorpodo package(linha3).
Estavariávelestásendoutilizadaemtodooprograma. Entreaslinhas10a
46,estãooscódigosdasfun çõesdeclaradasnoobjeto especification.
Alémdestes,tambémtemosumobjeto procedure(linhas5a8)utilizado
paraimprimirmensagensnatela.Seobservarmosesteobjeto,veremosque
elenãofoideclaradono especification,logo,nãopoderáseracessado
274

## Página 286

CasadoCódigo Capítulo17. packages
deforado body.
Emnossoprograma,a procedure imprime_msg estásendoutilizada
naslinhas21,23,25e42,pelasfun ções subtraie divide.Valelembrarmais
umavezquetodaadeclaraç ãooucodificaç ãodeobjetodeveserfinalizadapor
pontoevírgula.Comono especification,o body também éfinalizado
comocomando end(linha48),seguindoasmesmasregras. Éimportante
frisarqueosnomesdosobjetos especificatione bodydevemseriguais.
Detalhessobreo package body calculo:
• Foicriadoopackage body chamado calculo;
• Nopackage body foideclaradaumavariávelchamada resqueserá
usadainternamentepelosprogramasexistentes(escopoprivado);
• Foramcodificadososobjetosreferentesàsfunctionssoma, subtrai,
multiplicae divide,declaradasno especification;estas,de
escopopúblico;
• Também foi codificado um objeto procedure chamado
imprime_msg, de escopo privado, e que imprime mensagens na
tela,vindasdas functions.
Executandoo package calculo:
SQL> declare
2 res number;
3 begin
4 res := calculo.soma(450, 550);
5 --
6 dbms_output.put_line('450 + 550 = '||res);
7 end;
8 /
450 + 550 = 1000
Procedimento PL/SQL concluído com sucesso.
SQL> declare
2 res number;
275

## Página 287

17.2. Acessoapackages CasadoCódigo
3 begin
4 res := calculo.subtrai(350, 650);
5 --
6 dbms_output.put_line('350 - 650 = '||res);
7 end;
8 /
Resultado menor que zero: -300
350 - 650 = -300
Procedimento PL /SQL concluído com sucesso.
SQL> declare
2 res number;
3 begin
4 res := calculo.multiplica(20, 10);
5 --
6 dbms_output.put_line('20 * 10 = '||res);
7 end;
8 /
20 * 10 = 200
Procedimento PL /SQL concluído com sucesso.
SQL> declare
2 res number;
3 begin
4 res := calculo.divide(50, 5);
5 --
6 dbms_output.put_line('50 / 5 = '||res);
7 end;
8 /
50 / 5 = 10
Procedimento PL /SQL concluído com sucesso.
SQL>
Observeoqueacontecequandotentamosacessaralgumobjetoquenão
temescopononívelpúblico, ouseja, quenãoseencontradeclaradono
especification:
SQL> declare
276

## Página 288

CasadoCódigo Capítulo17. packages
2 res number;
3 begin
4 res := calculo.divide(50, 5);
5 --
6 calculo.imprime_msg('50 / 5 = '||res);
7 end;
8 /
calculo.imprime_msg('50 / 5 = '||res);
*
ERRO na linha 6:
ORA-06550: linha 6 , coluna 11:
PLS-00302: o componente 'imprime_msg' deve ser declarado
ORA-06550: linha 6 , coluna 3:
PL/SQL: Statement ignored
SQL> begin
2 calculo.res := calculo.divide(50, 5);
3 --
4 dbms_output.put_line('50 / 5 = '||calculo.res);
5 end;
6 /
calculo.res := calculo.divide(50, 5);
*
ERRO na linha 2:
ORA-06550: linha 2 , coluna 11:
PLS-00302: o componente 'RES' deve ser declarado
ORA-06550: linha 2 , coluna 3:
PL/SQL: Statement ignored
ORA-06550: linha 4 , coluna 45:
PLS-00302: o componente 'RES' deve ser declarado
ORA-06550: linha 4 , coluna 3:
PL/SQL: Statement ignored
SQL>
Noscasosemquetentarmosacessarobjetosnãopúblicos,oOraclein-
formaqueeledeveserdeclarado.
277

## Página 289

17.3. Recompilandopackages CasadoCódigo
17 .3 R ecompilando packages
Quandoalteramosum packagenobancodedados,podeacontecerdeter-
mosquecompilá-la,novamente. Paraisso,utilizamosocomando alter.
Vejaosexemplosnasequência:
SQL> alter package listagem compile;
Pacote alterado.
SQL>
17 .4 R ecuperando informações
Para visualizar informações referentes àspackages, utilize as views
user_objects, all_objectsou dba_objects. Nestaviewconstam
informaçõescomo STATUSedatadecriaç ãodoobjeto.
SQL> select owner, object_type, status, created, last_ddl_time
2 from all_objects where object_name = 'listagem';
OWNER OBJECT_TYPE STATUS
------------------------------ ------------------- -------
TSQL package VALID
TSQL package body VALID
createD LAST_DDL
-------- --------
02/12/11 02/12/11
02/12/11 02/12/11
SQL>
Outraformaderecuperardadosreferentesa packageséutilizandoo
comando describe. Elemostraadefiniç ãodetodasas procedurese
functionscontidasno package.
SQL> desc listagem
procedure LISTA_GERENTE_POR_DEPTO
278

## Página 290

CasadoCódigo Capítulo17. packages
SQL>
17 .5 R ecuperando códigos
Jáparavisualizarocódigodosobjetos packagenobancodedadosutilize
asviews user_source, all_sourceou dba_source.
SQL> column text format a300
SQL> set lines 1000
SQL> set pages 1000
SQL> select line, text
2 from all_source where name = 'listagem';
LINE TEXT
---------- ------------------------------------------------------
1 package listagem is
2 --
3 cursor c1 is
4 select d.department_id
5 ,department_name
6 ,first_name
7 ,hire_date
8 ,salary
9 from departments d
10 ,employees e
11 where d.manager_id = e.employee_id
12 order by department_name;
13 --
14 type tab is table of c1%rowtype index by
binary_integer;
15 --
16 tbgerente tab;
17 n number;
18 --
19 procedure lista_gerente_por_depto;
20 --
21 end listagem;
1 package body listagem is
279

## Página 291

17.6. Visualizandoerrosdecompilação CasadoCódigo
2 --
3 procedure lista_gerente_por_depto is
4 --
5 begin
6 for r1 in c1 loop
7 tbgerente(r1.department_id) := r1;
8 end loop;
9 --
10 n := tbgerente.first;
11 --
12 while n <= tbgerente.last loop
13 dbms_output.put_line(
'Depto: '||tbgerente(n).department_name||' '||
14 'Gerente: '||tbgerente(n).first_name||' '||
15 'Dt. Admi.: '||tbgerente(n).hire_date||' '||
16 'Sal.: '||to_char(tbgerente(n).salary,
'fm$999g999g990d00'));
17 n := tbgerente.next(n);
18 end loop;
19 --
20 end lista_gerente_por_depto;
21 --
22 end listagem;
43 linhas selecionadas.
SQL>
17 .6 V isualizando erros de compilação
Paravisualizarerrosdecompilaç ão,useocomando show error.
SQL> create or replace package listagem is
2 --
3 cursor c1 is
4 select d.department_id
5 ,department_name
6 ,first_name
7 ,hire_date
280

## Página 292

CasadoCódigo Capítulo17. packages
8 ,salary
9 from departments d
10 ,employees e
11 where d.manager_id = e.employee_id
12 order by department_name;
13 --
14 type tab is table of c1%rowtype index by binary_integer;
15 --
16 tbgerente tab;
17 n number;
18 --
19 procedure lista_gerente_por_depto;
20 ; -- provocando um erro de sintaxe.
21 --
22 end listagem;
23 /
Advertência: Pacote criado com erros de compilação.
SQL> show error
Erros para package listagem:
LINE/COL ERROR
-------- --------------------------------------------------------
20/4 PLS-00103: Encontrado o símbolo ";" quando um dos
seguintes
símbolos era esperado:
end function package pragma private procedure subtype
type
use <um identificador>
<um identificador delimitado por aspas duplas> form
current
cursor
SQL>
Ocomandobasicamentemostraduascolunas. Aprimeiracomalinha
eacolunaondeocorreuoerro,easegundacolunacomadescriç ão. Es-
teserrostambémpodemservisualizadosatravésdasviews user_errors,
281

## Página 293

17.6. Visualizandoerrosdecompilação CasadoCódigo
all_errorse dba_errors.
SQL> select line
2 ,position
3 ,text
4 from user_errors
5 where name = 'listagem';
LINE POSITION TEXT
----- --------- -------------------------------------------------
20 4 PLS-00103: Encontrado o símbolo ";" quando um dos
seguintes símbolos era esperado:
end function package pragma private
procedure subtype type use
<um identificador> <um identificador
delimitado por aspas duplas> form
current cursor
SQL>
282

## Página 294

Capítulo18
Transaçõesautônomas
Quandobuscamosinformaçõesemumbancodedados,esperamosqueelas
estejamíntegras.Paragarantiraintegridadeeconsistênciasdosdados,oOra-
clemantémcontrolesdetransações. Quandoumaoperaç ãoDMLédispa-
rada,issoindicaqueosdadosdeumatabela,porexemplo,podemestarsendo
alterados.Nessemomento,podemosconcluirqueenquantoasalteraçõesnão
foremconfirmadasosdadosqueestãosendomanipuladosnatransaç ãoem
questãonãoestãoconsistentes. Apenasquandoforemconfirmados,através
deum rollbackoudeum commit,osdadosestarãoíntegros.
Hásituaçõesemquepodemosterváriaschamadasaoutrosobjetosque
estejamexecutandocomandosDMLeefetivando-oslogoemseguida.Entre-
tanto,aofazerisso,corremosoriscodeefetivaraçõesdeoutroscomandos
DML,executadosanteriormente,quenãodeveriamserefetivados,oupelo
menosnãonaquelemomento. Issoacontecepoissabemosque,aoexecutar
umcomandodeefetivaç ão,comoum commitouum rollback,oOracle

## Página 295

CasadoCódigo
efetivatudooqueestiverpendentenasessão.
Paraessescasos,podemosutilizartransaçõesautônomasparaisolarações
dedeterminadosprogramas.Utilizamosesterecursoinformando-onadecla-
raçãodosobjetos,comoem procedurese functions(dentroouforade
packages),blocosanônimos(menosemsub-blocos)ou triggers. Sua
funçãoéfazercomqueoOracleabraumanovasessãosomenteparaexecutar
talobjeto,ouseja,nestemomentoexistirãopelomenosduastransaçõesem
aberto:atransaç ãooriginaleoutratransaç ãoautônoma. Vejaoexemploa
seguir.
SQL> declare
2 --
3 procedure lista_dept is
4 --
5 pragma autonomous_transaction;
6 begin
7 --
8 dbms_output.new_line;
9 dbms_output.put_line(
'----------- Lista Departamentos -----------');
10 dbms_output.new_line;
11 --
12 for i in (select * from dept order by deptno) loop
13 dbms_output.put_line(i.deptno||' - ' ||i.dname);
14 end loop;
15 --
16 commit;
17 --
18 end;
19 --
20 begin
21 insert into dept (deptno, dname, loc)
values (43, 'ORDER MANAGER','BRASIL');
22 --
23 lista_dept;
24 --
25 commit;
26 --
284

## Página 296

CasadoCódigo Capítulo18. Transaçõesautônomas
27 lista_dept;
28 --
29 end;
30 /
Nesse exemplo, criamos um bloco PL/SQL anônimo e dentro dele
declaramos uma procedure chamadalista_dept. Esta procedure
lista todos os departamentos existentes. Ela foi declarada como
autonomous_transaction, ou seja, quando ela for executada será
abertaumatransaç ãoautônoma.
No corpo do bloco PL/SQL, temos uminsert que inclui um de-
partamento novo. Logo depois deste comando, chamamos a procedure
lista_deptparalistartodososdepartamentosquejáseencontramcadas-
trados.Depoisdisso,efetivamosaalteraç ãorealizadapelo insertemanda-
moslistarosdepartamentos,novamente.Agoravamosanalisaroresultado.
----------- Lista Departamentos -----------
10 - ACCOUNTING
30 - SALES
40 - OPERATIONS
41 - GENERAL LEDGER
42 - PURCHASING
----------- Lista Departamentos -----------
10 - ACCOUNTING
30 - SALES
40 - OPERATIONS
41 - GENERAL LEDGER
42 - PURCHASING
43 - ORDER MANAGER
Procedimento PL/SQL concluído com sucesso.
SQL>
No resultado, temos duas listagens. Uma impressa após o comando
insert,eoutraapósaefetivaç ãodo insertatravésdocomando commit.
Notequeaimpressãorealizadaantesdo commitnãomostraodepartamento
285

## Página 297

CasadoCódigo
43,embora,elejátenhasidoinseridonesteponto.Jáaimpressãoapósoco-
mando commitmostraonovodepartamento.
Destaforma,temosquenosatentarparaoseguintecenário.Sabemosque,
quandoéabertaumatransaç ãonoOracle,elamontaumaimagem,digamos
assim,dosobjetosedadosdisponíveisparaousuárionestasessão.Comre-
laçãoaosdados,avisãopermiteenxergarsomenteaquiloqueestáefetivado
nobancodedados,ouseja,dadosconsistenteseíntegros.Issoquerdizerque
dadospendentesdeefetivaç ãonãopoderãoservisualizados,issoé,dadosex-
cluídos,inseridosouatualizadosqueaindanãotenhamsidocommitados.
Logo,quandoistoacontece,nãoconseguimosvisualizarasalteraçõesque
estãosendorealizadas.Quandotemosumobjetoutilizandotransaç ãoautô-
noma,conseguimosmanipularsomenteosdadosefetivados.Dessaforma,se
nósrealizarmosumcomando selectafimdeobterosdadosalteradosna
sessãooriginal,masnãoefetivados,nãoconseguiremosenxergá-los.Apenas
pararessaltar,issosedáaofatodequedentrodesteobjetoestamosemoutro
escopo,emumanovatransaç ão.
Outropontomuitoimportanteéque,quandoutilizamosobjetoscom
transaçãoautônoma,precisamosefetivaratransaç ãoatravésdeum commit
oudeum rollback.Comoestetipodeaç ãofazcomqueumanovatran-
saçãosejaaberta,temosquefinalizá-la.Casocontrário,elaficariapendente
eissopoderiagerarumerro.
Conformevistonoexemploanterior,utilizamosaseguintelinhadeco-
mando pragma autonomous_transaction,naáreadedeclaraç ão,para
abrirumanovatransaç ão.Vejaoutroexemploaseguir.
Paraesteexemplo,criamosváriosobjetos.Primeiramente,criamosuma
procedurechamada lista_pais,quelistaránatelatodosospaísesjá
cadastradosnatabela countries.Cadalistaimpressateráumnúmeroin-
dicandoonúmerodaimpressão.
SQL> create procedure lista_pais(num_lista number) is
2 --
3 begin
4 --
5 dbms_output.put_line('Executando procedure: LISTA_PAIS');
6 --
286

## Página 298

CasadoCódigo Capítulo18. Transaçõesautônomas
7 dbms_output.new_line;
8 dbms_output.put_line(
'----------- Lista País - '||num_lista||'-----------');
9 dbms_output.new_line;
10 --
11 for i in (select * from countries where region_id = 1
order by country_name) loop
12 dbms_output.put_line(i.country_id||' -
'||i.country_name);
13 end loop;
14 --
15 end;
16 /
Procedimento criado.
SQL>
Aprocedureaseguirtemoobjetivodeinserirumregistronatabela
countriesreferenteaopaísPortugal.Notequenestaproceduretemosde-
claradaumatransaç ãoautônoma. Nocorpo,alémdocomando insert,
temosachamadaàprocedure lista_pais,quevailistarospaísescadas-
trados. Estalistagemseráasegundalistaaserimpressa. Logoapós,temos
um commitqueefetivaráaaçãodocomando inserteencerraráatransa-
çãoautônoma.
SQL> create procedure insere_pais_portugal is
2 --
3 pragma autonomous_transaction;
4 --
5 begin
6 --
7 dbms_output.put_line('Executando procedure:
INSERE_PAIS_PORTUGAL');
8 --
9 insert into countries (country_id, country_name,
region_id) 10 values ('PT',
'Portugal' ,1);
11 --
287

## Página 299

CasadoCódigo
12 lista_pais(2);
13 --
14 commit;
15 --
16 end;
17 /
Procedimento criado.
SQL>
Apróximaproceduretemafinalidadedeapenaschamaraprocedure
insere_pais_portugal. Elaserveapenaspara,digamosassim,estabe-
lecerumaligaç ãoindiretaentreasprocedures insere_pais_espanhae
insere_pais_portugal.
SQL> create procedure chama_insere_pais_portugal is
2 --
3 begin
4 --
5 dbms_output.put_line('Executando procedure:
CHAMA_INSERE_PAIS_PORTUGAL');
6 --
7 insere_pais_portugal;
8 --
9 end;
10 /
Procedimento criado.
SQL>
Jáaprocedure insere_pais_espanhatemoobjetivodeinserirum
registronatabela countriesreferenteaopaísEspanha. Nocorpoda
procedure, além do comandoinsert, temos a chamada à procedure
lista_pais,queirálistarospaísescadastrados. Estalistagemseráapri-
meiralistaaserimpressa. Logoapós,temosum rollbackquedesfaráa
açãodocomando insert. Depoisdo rollback,temosumanovacha-
288

## Página 300

CasadoCódigo Capítulo18. Transaçõesautônomas
madaàprocedure lista_pais,asegundanesteobjeto,queimprimeater-
ceiralistagem.
SQL> create procedure insere_pais_espanha is
2 --
3 begin
4 --
5 dbms_output.put_line('Executando procedure:
INSERE_PAIS_ESPANHA');
6 --
7 insert into countries (country_id, country_name,
region_id)
8 values ('ES','Espanha',1);
9 --
10 lista_pais(1);
11 --
12 chama_insere_pais_portugal;
13 --
14 rollback;
15 --
16 lista_pais(3);
17 --
18 end;
19 /
Procedimento criado.
SQL>
Note que em todos os objetos temos chamadas à procedure
dbms_output, indicando a execução do objeto corrente. Usaremos
estaidentificaçãoparasaberaordemcronológicadaexecuç ãodosprogra-
mas.Agoravamosexecutaraprocedure insere_pais_espanha,queéa
quedesencadearáaexecuçãodosdemaisobjetoscriados.
SQL> begin
2 insere_pais_espanha;
3 end;
4 /
289

## Página 301

CasadoCódigo
EssecódigoPL/SQLexecutaaprocedure insere_pais_espanha,que
chamaasdemaisproceduresondeobtivemososresultadosaseguir.
Nestenossoexemplo,aoexecutarmosessaprocedure,primeiramente,o
paísEspanhafoiinseridonatabela countries.Logoapósainser ção,man-
damoslistarospaíses.Oresultadodalistagem1émostradoaseguir.
Executando procedure: INSERE_PAIS_ESPANHA
Executando procedure: LISTA_PAIS
----------- Lista País - 1-----------
BE - Belgium
DK - Denmark
ES - Espanha
FR - France
DE - Germany
IT - Italy
NL - Netherlands
CH - Switzerland
UK - United Kingdom
Note que, na terceira linha da listagem, temos o país Espanha inse-
rido. Logoapósaexecuç ãodoprocedimentodelistagem,continuandoa
execução da procedureinsere_pais_espanha, foi chamada a proce-
dure chama_insere_pais_portugal,queporsuavez,chamaaproce-
dure insere_pais_portugal.Aprocedure insere_pais_portugal
será executada em outra transação, pois nela declaramos umpragma
autonomous_transaction.Elaexecutao insertreferenteaopaísPor-
tugalelogoemseguidaexecutaaimpressãodalistagem2.Paraencerrar,um
commitéexecutado,efetivandoasoperações.Vejaoresultado.
Executando procedure: CHAMA_INSERE_PAIS_PORTUGAL
Executando procedure: INSERE_PAIS_PORTUGAL
Executando procedure: LISTA_PAIS
----------- Lista País - 2-----------
BE - Belgium
DK - Denmark
FR - France
DE - Germany
IT - Italy
290

## Página 302

CasadoCódigo Capítulo18. Transaçõesautônomas
NL - Netherlands
PT - Portugal
CH - Switzerland
UK - United Kingdom
VejaqueaquinãoapareceuopaísEspanha. Issoporqueaprocedure
insere_pais_portugal foi executada dentro de uma transação autô-
noma,logo,quandoelachamaalistagem,apenasosdadosefetivadoseos
dasessãocorrentesãovisualizados.
Apósotérminodaexecuç ãodaprocedure insere_pais_portugal,
voltamosparaaprocedure insere_pais_espanha,onde,nasequência
doprograma,temosum rollback,desfazendotudoqueficoupendentena
sessão.Apósdesfazerasações,executamosalistagemdenúmero3.Aseguir,
oresultado.
Executando procedure: LISTA_PAIS
----------- Lista País - 3-----------
BE - Belgium
DK - Denmark
FR - France
DE - Germany
IT - Italy
NL - Netherlands
PT - Portugal
CH - Switzerland
UK - United Kingdom
Procedimento PL/SQL concluído com sucesso.
SQL>
Notequenasaídadalistagemfinal(listagem3)temoscadastradoopaís
Portugal,masnãoopaísEspanha.O rollbackacaboudesfazendoainser-
çãoreferenteaopaísEspanha,masnãoainser çãoreferenteaopaísPortugal,
poisestainser çãofoirealizadaeefetivadaviaoutratransaç ão,atransaç ão
autônoma.
Nãoécomumvertransaçõesautônomassendoutilizadasemprogramas
PL/SQL,contudo,emalgunscasoselassetornamimprescindíveis.Quando
291

## Página 303

CasadoCódigo
estivermostrabalhandocom triggers(capítulomaisaseguir),serávisto
que,paraodisparodedeterminadostiposde triggersemsituaçõesespe-
cíficas,somosobrigadosausartransaçõesautônomasparapoderatendero
objetivo.
292

## Página 304

Capítulo19
Triggers
Oobjeto triggernadamaisédoqueumblocodecódigoPL/SQLarmaze-
nadonobancodedadosequeédisparadoautomaticamentemedianteuma
ação.Estedisparopodeocorrerdeduasformas,porintermédiodealterações
feitasemregistrosdeumadeterminadatabela,nestecasosetratandododis-
parodeum triggerdebancodedadosouporaçõesemníveldesistema
porum triggerdesistema.
Vamosaprendersobreestesdoistipos,mostrandoascaracterísticasdos
triggersdebancodedadosquesãomuitoutilizadosnodesenvolvimento
deprogramasedos triggers de sistemaquesãomaisutilizadospelosadminis-
tradoresdebancodedados.

## Página 305

19.1. Triggerdebancodedados CasadoCódigo
19.1 T rigger de banco de dados
Um triggerdebancodedadossempreestáassociadoaumatabela.Não
existindotabela,nãoexiste triggerdebandodedados.Quandoqueremos
queumaaçãoaconte çaautomaticamentemedianteumaalteraç ãoemalguma
tabela,oumelhor,nosregistrosqueelapossui,podemosutilizá-losparaisto.
Um triggerpodedispararquandoalgumaaç ãoocorreemumatabela
etambémemumdeterminadomomento. Porexemplo,podemoscriarum
triggerquedisparequandofizermosum updateemdeterminadatabela,
equeocorraapóso updatedosregistros.Alémdisso,podemosdefinirque
este triggerdispararáparacadalinhaafetadapelocomando dml,cha-
madode trigger de linha,ouseexecutaráumaúnicavezindependentede
quantaslinhassofreremalterações.Esteúltimo,nóschamamosde trigger de
tabelaoudecomando. Tambémpodemosdefinircláusulas whereparao
triggerparaqueodisparosóaconte çasealgunscritériosforemobedeci-
dos.
19.2 T rigger de tabela
Vamosanalisaradefiniç ãodo trigger.
create trigger tipo_tabela
before delete or insert or update of sal on emp
begin
end;
Paracriarum trigger,primeiramentedamosumnome.Utilizamoso
comando create trigger paracriaroobjeto. Temosobrigatoriamente
quedefinirquandoseráodisparo.Nesteexemplo,informamosqueseudis-
paroocorreráantesdaação,nestecaso before.Casotenhamosnecessidade
queodisparoocorradepois,informamos after.
Vamosabrirumparêntesesaquiparaexplicarmelhorestaquestãode
aftere beforenaespecificaçãodo trigger.Aexpressão beforede-
finidano triggerpodeserumpoucoconfusa,poisdáaimpressãoqueo
triggervaidetectarquevamosexecutarum insert,porexemplo,eantes
deacontecertalaç ãoeledisparao trigger.
294

## Página 306

CasadoCódigo Capítulo19. Triggers
Masnãoébemassim. Naverdade,o beforequerdizerantesqueas
alteraçõessejamfeitasnosregistrosdatabelaemquestão,ouseja,podemos
dizerqueoOraclefazasalteraçõesprimeiramenteemmemória,paradepois
efetivá-lasnobancodedados.Comisso,dependendodomomentotratado,
beforeou after,podemosounãoalterarestesdados.
Quandoo triggerédisparadonomomento before,osdadosainda
nãoforamefetivados,nestecasopodemosalterarosvaloresantesqueeles
sejamgravadosnobancodedados.Quandoédisparadono afternãohá
maiscomoalterá-los,poisjáforamefetivadosnobancodedados.
Depoisdedefinirquandoocorrerá,precisamosinformaremquaissitu-
ações,oumelhor,ações,o triggerdevedisparar.Notequeparaestadefi-
niçãofoideterminadoqueodisparosempreocorreráquandoatabela emp
sofrerum delete, insertou updateespecíficonacoluna sal. Nos
casosde update,podemosounãoinformarcolunasespecíficasparadeter-
minarodisparo.Nesteexemplo,qualqueratualizaç ãoquenãosejanacoluna
saldatabela empo triggernãovaidisparar. Casonãoqueiradefinir
colunasespecíficasapenasnãouseaexpressão of.
Este triggerpodesercaracterizadocomoum trigger de tabela,pois
nãoinformamosqueelevaidispararparacadalinhaafetada.Portanto,não
importaquantaslinhasserãoexcluídas,inseridasouatualizadas,elesempre
dispararáumaúnicavez.
Nasequência,segueumexemplode trigger de tabelaesuaaplicação.Va-
moscriarum triggerquefaráaauditoriadatabela emp. Cadavezque
umoumaisregistrosforeminseridosouatualizados,esteprogramavaical-
cularaquantidadederegistroscontidosnatabela emp,asomadetodosos
saláriosecomissões. Essesdadosserãoinseridosemumatabelachamada
tab_audit_emp.Vamoscriaratabela:
SQL> create table tab_audit_emp
2 (
3 nr_registros number
4 ,vl_total_salario number
5 ,vl_total_comissao number
6 )
7 /
295

## Página 307

19.2. Triggerdetabela CasadoCódigo
Tabela criada.
SQL>
Segueocódigoda trigger:
SQL> create trigger tig_audit_emp
2 after insert or delete or update of sal, comm on emp
3 declare
4 wnr_registros number default 0;
5 wvl_total_salario number default 0;
6 wvl_total_comissao number default 0 ;
7 wnr_registros_audit number default 0;
8 begin
9 select count(*)
10 into wnr_registros
11 from emp;
12 --
13 select sum(sal)
14 into wvl_total_salario
15 from emp;
16 --
17 select sum(comm)
18 into wvl_total_comissao
19 from emp;
20 --
21 select count(*)
22 into wnr_registros_audit
23 from tab_audit_emp;
24 --
25 if wnr_registros_audit = 0 then
26 --
27 insert into tab_audit_emp (
nr_registros, vl_total_salario, vl_total_comissao)
28 values (wnr_registros, wvl_total_salario,
wvl_total_comissao);
29 --
30 else
31 --
32 update tab_audit_emp
296

## Página 308

CasadoCódigo Capítulo19. Triggers
33 set nr_registros = wnr_registros
34 ,vl_total_salario = wvl_total_salario
35 ,vl_total_comissao = wvl_total_comissao;
36 --
37 end if;
38 end;
39 /
Gatilho criado.
SQL>
Vamosentenderoqueeste triggerfaz.Primeiramente,chamamoseste
de tig_audit_emp.Elevaidispararapósatabela empsofrerumcomando
insert, deleteou update,sendoqueparaesteúltimo,somentequando
ascolunas salou commforemalteradas.Notequealinha for each row
nãoaparece.Issoindicaquenosso triggeréumdetabela.Portanto,não
importaaquantidadedelinhasafetadaspelocomando,elesóvaidisparar
umaúnicavez.O triggertambémsóvaiserdisparadoapós( after)os
comandos insert, deleteou updateforemefetivados.
Dentrodestascondiçõeso triggerdisparaeexecutacomandosSQL
parabuscarasinformaçõesqueserãoutilizadasparagerarnossaauditoria,
comoaquantidadederegistrosnatabela,asomadetodosossalárioseco-
missões.Issojustificaofatodeo triggerserdisparadoumaúnicavez,pois
nestedisparoelevarretodososregistrosdatabela,nãonecessitandotrabalhar
registroporregistroafetado.
Depoisdebuscarasinformações,oprogramafazum selectparaveri-
ficarsejáexisteumregistronatabeladeauditoria.Casoexista,elesomente
atualizaasinformaçõesexistentes.Casocontrário,insereumregistro.Vamos
testá-lo.Primeiramente,verificamosatabela tab_audit_emp.
SQL> select * from tab_audit_emp;
não há linhas selecionadas
SQL>
297

## Página 309

19.2. Triggerdetabela CasadoCódigo
Agoravamospegarumamassadetestepararealizarumaatualizaç ãonos
dadosdatabela emp.
SQL> select * from emp where deptno = 20
2 /
EMPNO ENAME JOB MGR HIREDATE SAL
---------- ---------- --------- ---------- -------- ----------
7369 SMITH CLERK 7902 17/12/80 880
7566 JONES MANAGER 7839 02/04/81 3272,5
7788 SCOTT ANALYST 7566 09/12/82 3300
7876 ADAMS CLERK 7788 12/01/83 1210
7902 FORD ANALYST 7566 03/12/81 3300
COMM DEPTNO
---------- ----------
20
20
20
20
20
SQL>
Vamosatualizarossaláriosdetodososempregadosqueestãoalocados
nodepartamento20.
SQL> update emp
2 set sal = sal + (sal * 10 / 100)
3 where deptno = 20
4 /
5 linhas atualizadas.
SQL> commit;
Validação completa.
298

## Página 310

CasadoCódigo Capítulo19. Triggers
SQL>
Vamosverificarasatualizaçõesnatabela emp.
SQL> select * from emp where deptno = 20;
EMPNO ENAME JOB MGR HIREDATE SAL
---------- ---------- --------- ---------- -------- ----------
7369 SMITH CLERK 7902 17/12/80 968
7566 JONES MANAGER 7839 02/04/81 3599,75
7788 SCOTT ANALYST 7566 09/12/82 3630
7876 ADAMS CLERK 7788 12/01/83 1331
7902 FORD ANALYST 7566 03/12/81 3630
COMM DEPTNO
---------- ----------
20
20
20
20
20
SQL>
Ok.Osdadosforamatualizados.Agoravamosverificarnossatabelade
auditoria.
SQL> select * from tab_audit_emp;
NR_REGISTROS VL_TOTAL_SALARIO VL_TOTAL_COMISSAO
------------ ---------------- -----------------
14 31308,75 2244
SQL>
Notequeo triggerrealizouocálculoconsiderandonãosóaslinhas
afetadas,massimtodasaslinhasdatabela,comoeraoesperado,ouseja,foi
criadoumregistronestatabelacontendoinformaçõesreferentesatodosos
299

## Página 311

19.2. Triggerdetabela CasadoCódigo
registrosdefuncionárioscadastrados.Agoravamosexcluiralgunsregistros
databela emp.
SQL> delete from emp
2 where deptno = 10
3 /
3 linhas deletadas.
SQL> commit;
Validação completa.
SQL>
Ok.Excluímososdadoscomsucesso.Agoravamosverificarnossatabela
deauditoria.
SQL> select * from tab_audit_emp;
NR_REGISTROS VL_TOTAL_SALARIO VL_TOTAL_COMISSAO
------------ ---------------- -----------------
11 22558,75 2244
SQL>
Porúltimo,vamostestarainser çãodedados.
SQL> insert into emp (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
2 values (7935, 'PAULO', 'CLERK' , 7902,
to_date('17/09/2011','dd/mm/yyyy'),
1000, null, 20);
1 linha criada.
SQL>
Novoresultado.
300

## Página 312

CasadoCódigo Capítulo19. Triggers
SQL> select * from tab_audit_emp;
NR_REGISTROS VL_TOTAL_SALARIO VL_TOTAL_COMISSAO
------------ ---------------- -----------------
12 23558,75 2244
SQL>
Apresentamosaquiapenasumaformadecomoutilizaros triggersde
tabela.Contudo,aspossibilidadesdeutilizaç ãosãomuitas.Tudovaidepen-
derdanecessidade.
19.3 T rigger de linha
Muitoparecidocomo trigger de tabela,odelinhatempraticamenteasmes-
mascaracterísticas,sendoporumdetalhe:o trigger de linhadisparaparacada
linhaafetadapelocomando dml.Vejaoexemplonasequência.
create or replace trigger tipo_linha
after update on func
referencing old as V
new as N
for each row
begin
end;
Nesteexemplotemosalgomaisdoqueadefiniç ãodequandoecomo
o triggerserádisparado. Estamosdefinindoqueeleserádotipolinha,
ouseja,elevaidispararparacadalinhaafetadapelo update. Paraissofoi
colocadoemsuadefiniç ãoaseguintelinhadecomando: for each row.
Quandotrabalhamoscom trigger de linha,podemosmanipularosvalo-
resdaslinhasafetadas. Emalgunscasos,podemosatéalterarosvaloresde
certascolunasantesdeasmesmasseremsalvas.Quandodefinimosqueum
triggerédelinha,oOraclecriaduasreferênciaschamadas olde new.Es-
tasreferênciasapontamsempreparaosdadosanterioresàsalteraçõesepara
osdadosposterioresàsalterações,respectivamente.
301

## Página 313

19.3. Triggerdelinha CasadoCódigo
Por exemplo, se alteramos o valor da colunasalde 100 para 500,
old.salconteráovalor100e new.salconteráovalor500.Eassimserá
paratodososvaloresdascolunasdatabelaqueestãosendoafetadasounão
pelocomando.
Quandotemosum triggersendodisparadono before,ouseja,antes
docomando dml,nóspodemosalterarovalorde new. Ovalorde old
nuncapodeseralterado. Casoaalteraç ãosejano after,nem oldnem
newpodemseralterados. Nemsempreteremososvaloresde olde new.
Quandoestamosatualizandoosregistrosemumatabelateremoso neweo
old,poisnestecasoestamosatualizandoumregistroquejáexiste.
Quandoestamosinserindoumregistro,nãotemososvaloresde old,
poissetratadeumregistronovo,nãohavendoassimvaloresantigos.Quando
estamosexcluindoumregistrotemoso oldenãotemoso new,poisestamos
excluindoumregistro,nãoinformandodadosnovos.
Asreferênciasolde newpodemreceberapelidos.Nestecasoutilizamos
adiretriz referencingparadefinirestainformaç ão.Nesteexemplo,esta-
moscriandoosseguintes alias: Vpara olde Npara new. Logo,quando
formostrabalharcomascolunasdevemosusar,porexemplo, v.salpara
pegarovalorantigoe n.salparaonovo.
Veremosaseguirumaaplicaç ãode trigger de linha ondecriaremosum
históricoparaatrocadecargosdosempregados. Cadavezqueumempre-
gadotrocardecargo,umhistóricocontendoalgumasinformaçõesseráguar-
dado. Nestehistóricoteremosocódigodoempregado,ocargoanterior,o
novocargo,adatadaalteraç ãoeumadescriç ão.Paraisso,vamoscriaruma
tabelaqueseráorepositóriodestasinformaçõeshistóricas.
SQL> create table tab_hist_cargo_emp
2 (
3 empno number
4 ,job_anterior varchar2(9)
5 ,job_atual varchar2(9)
6 ,dt_alteracao_cargo date
7 ,ds_historico varchar2(2000)
8 )
9 /
302

## Página 314

CasadoCódigo Capítulo19. Triggers
Tabela criada.
SQL>
Criamosa tab_hist_cargo_empqueabrigaráasinformaçõesque
compõemonossohistórico. Agoravamosparao triggerquefaráeste
controle.
SQL> create trigger tig_hist_cargo_emp
2 after update of job on emp
3 referencing old as v
4 new as n
5 for each row
6 begin
7 insert into tab_hist_cargo_emp ( empno
8 ,job_anterior
9 ,job_atual
10 ,dt_alteracao_cargo
11 ,ds_historico)
12 values ( :n.empno
13 ,:v.job
14 ,:n.job
15 ,sysdate
16 ,'O empregado '||:n.ename||
17 ' passou para o cargo '||:n.job||
18 ' em carater de promoção.');
19
20 end;
21 /
Gatilho criado.
SQL>
Cadavezqueo trigger tig_hist_cargo_emp disparar,depoisda
atualizaçãodeumcargo,serágravadoumhistórico,ouseja,umalinha,na
tabela tab_hist_cargo_empcontendoasinformaçõespertinentesàalte-
raçãodocargo. O triggervaidispararparacadalinhaalterada. Vamos
testá-lo.
303

## Página 315

19.3. Triggerdelinha CasadoCódigo
SQL> update emp
2 set job = 'MANAGER'
3 where empno = 7499
4 /
1 linha atualizada.
SQL>
Verificandoohistórico:
SQL> select * from tab_hist_cargo_emp
2 /
EMPNO JOB_ANTER JOB_ATUAL DT_ALTER
---------- --------- --------- --------
7499 SALESMAN MANAGER 05/09/11
DS_HISTORICO
-----------------------------------------------------------------
O empregado ALLEN passou para o cargo MANAGER em carater de
promoção.
SQL>
Muitobem.Ohistóricofoicriadoinformandoqueoempregado allen
mudoudecargo. Agoravamosaoutroexemplo. Criaremosum trigger
queirácalculareguardarnatabela empopercentualreferenteàcomissão
emrelaçãoaosaláriodoempregado. Paraisso,vamosincluirumacoluna
natabela empchamada pc_com_sal. Neste trigger,faremosusona
cláusulawhenparadeterminarquaisosregistrospoderãosofreestecálculo.
Valesalientarqueacláusula whenpodeserusadatantoparaostriggersde
linhascomoparaosdetabela.
Alterandoatabela emp:
SQL> alter table emp add pc_com_sal number;
Tabela alterada.
304

## Página 316

CasadoCódigo Capítulo19. Triggers
SQL>
Criandoo trigger:
SQL> create trigger tig_pc_com_sal_emp
2 before insert or update of sal, comm on emp
3 referencing old as v
4 new as n
5 for each row
6 when (n.job = 'SALESMAN')
7 begin
8 :n.pc_com_sal := nvl(:n.comm,0) * 100 / :n.sal;
9 end;
10 /
Gatilho criado.
SQL>
Notequeagoracriamosum triggerquevaidispararno before,ou
seja,antesdasinformaçõesseremefetivadasnobancodedados. Usamoso
before,poisoprogramaestaráalterandoumdado,oumelhor,ovalorde
umacoluna,referenteàmesmalinhaquevaidispararo trigger.Portanto,
issodeveacontecerantesqueasinformaçõessejamefetivadas.Seusássemos
after,nãoconseguiríamosfazertalalteraç ão.Utilizamosacláusula when
paradeterminarqueo triggersóvádispararquandoalinhaemquestão
fordealgumempregadoquetenhacomocargo( job)iguala salesman.
Vamostestá-lo.
SQL> select empno, ename, job, sal, comm, pc_com_sal from emp;
EMPNO ENAME JOB SAL COMM PC_COM_SAL
---------- ---------- --------- ---------- ---------- ----------
7369 SMITH CLERK 968
7499 ALLEN SALESMAN 1600 306
7521 WARD SALESMAN 1250 510
7566 JONES MANAGER 3599,75
7654 MARTIN SALESMAN 1250 1428
305

## Página 317

19.3. Triggerdelinha CasadoCódigo
7698 BLAKE MANAGER 2850
7782 CLARK MANAGER 2450
7788 SCOTT ANALYST 3630
7839 KING PRESIDENT 5000
7844 TURNER SALESMAN 1500 0
7876 ADAMS CLERK 1331
7900 JAMES CLERK 950
7902 FORD ANALYST 3630
7934 MILLER CLERK 1300
14 linhas selecionadas.
SQL> update emp set sal = sal;
14 linhas atualizadas.
SQL>
Primeiramente,verificamososdadosdatabela emp.Logoapós,execu-
tamosum updateapenasparaquenosso triggerdispare. Notequeo
updateatualizatodosossaláriosdosempregadoscomomesmosalário.Fi-
zemosissoapenasparaquetodasaslinhassejamvarridasequeocálculodo
percentualsejarealizadoparaosregistrosjácadastrados.Vamosveroresul-
tado.
SQL> select empno, ename, job, sal, comm, pc_com_sal from emp;
EMPNO ENAME JOB SAL COMM PC_COM_SAL
---------- ---------- --------- ---------- ---------- ----------
7369 SMITH CLERK 968
7499 ALLEN SALESMAN 1600 306 19,125
7521 WARD SALESMAN 1250 510 40,8
7566 JONES MANAGER 3599,75
7654 MARTIN SALESMAN 1250 1428 114,24
7698 BLAKE MANAGER 2850
7782 CLARK MANAGER 2450
7788 SCOTT ANALYST 3630
7839 KING PRESIDENT 5000
7844 TURNER SALESMAN 1500 0 0
306

## Página 318

CasadoCódigo Capítulo19. Triggers
7876 ADAMS CLERK 1331
7900 JAMES CLERK 950
7902 FORD ANALYST 3630
7934 MILLER CLERK 1300
14 linhas selecionadas.
SQL>
Vejaqueacoluna pc_com_salrecebeuocálculodopercentual,con-
formeaaç ãodisparadavia trigger. Tambémpodemosobservarqueso-
menteosregistroscujosempregadostenhamcomocargo salesmansofre-
ramestaaç ão.Agoravamosinserirumnovoempregado,comocargoigual
a salesmaneoutrocomocargo clerk,evamosveroqueacontece.
SQL> insert into emp (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
2 values (7940,'PEDRO' ,'CLERK',7788,
to_date('05/09/2011','dd/mm/rrrr'),750,100,30);
1 linha criada.
SQL> insert into emp (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
2 values (7941,'JOAO', 'SALESMAN',7698,
to_date('05/09/2011','dd/mm/rrrr'),1200,350,30)
3 /
1 linha criada.
SQL>
Verificandoatabela emp.
SQL> select empno, ename, job, sal, comm, pc_com_sal from emp;
EMPNO ENAME JOB SAL COMM PC_COM_SAL
---------- ---------- --------- ---------- ---------- ----------
7369 SMITH CLERK 968
307

## Página 319

19.3. Triggerdelinha CasadoCódigo
7499 ALLEN SALESMAN 1600 306 19,125
7521 WARD SALESMAN 1250 510 40,8
7566 JONES MANAGER 3599,75
7654 MARTIN SALESMAN 1250 1428 114,24
7698 BLAKE MANAGER 2850
7782 CLARK MANAGER 2450
7788 SCOTT ANALYST 3630
7839 KING PRESIDENT 5000
7844 TURNER SALESMAN 1500 0 0
7876 ADAMS CLERK 1331
7900 JAMES CLERK 950
7902 FORD ANALYST 3630
7934 MILLER CLERK 1300
7940 PEDRO CLERK 750 100
7941 JOAO SALESMAN 1200 350 29,1666667
16 linhas selecionadas.
SQL>
Analisandoasinformaçõespodemosconstatarqueoempregado pedro,
emboratenharecebidovaloresdesalárioecomissão,nãosofreuocálculo
dopercentual.Issoocorreupelofatodeelenãotercomocargo, salesman.
Nestecaso,o triggernãodisparou.Jáparaoempregado joao,o trigger
disparouecalculouopercentual.
Aquiapresentamosalgunsexemplossimples,apenasparamostrarofun-
cionamentodos triggers.Contudo,dependendodanecessidadepodemos
escrevercódigoscomplexosparaatenderàsmaisvariadassituaçõesquepo-
demsurgir.Mesmoporque,comopodeservisto,um triggernadamaisé
queumblocoPL/SQL,ouseja,umprograma,queéprogramadoparadispa-
rardeformaautomática.
Predicados condicionais para triggers de banco de dados
Vimosqueummesmo triggerpodedispararporumoumaistiposde
ações,comono insert, deletee update.Contudo,dependendodaaç ão
ocorridanatabela,podemsurgirnecessidadesdiferentesparacadauma.Para
isso,usamosospredicadoscondicionaisquenosdizemqualaç ãoresultou
308

## Página 320

CasadoCódigo Capítulo19. Triggers
nodisparodo trigger. Estespredicadossão: inserting, updating
e deleting.Seuspossíveisvaloressão truee false.Vejaoexemploa
seguir,ondecriaremosumhistóricoparagravarasaçõesdemanipulaç ãodos
departamentoscadastradosnatabela dept.Criandoatabela:
SQL> create table tab_hist_dept
2 ( deptno number
3 ,dt_historico date
4 ,ds_historico varchar2(2000)
5 )
6 /
Tabela criada.
SQL>
Nestatabelaserágravadoocódigododepartamento,adatadaaç ãoetam-
bémumdescritivodohistórico.Vamoscriaro triggerquefaráocontrole
dehistórico.
SQL> create or replace trigger tig_hist_dept
2 after insert or delete or update on dept
3 for each row
4 declare
5 wacao varchar2(200) default null;
6 begin
7 --
8 if inserting then
9 wacao := 'inserido';
10 elsif updating then
11 wacao : = 'atualizado';
12 elsif deleting then
13 wacao : = 'excluído';
14 end if;
15 --
16 insert into tab_hist_dept (deptno, dt_historico,
ds_historico)
17 values ( nvl(:new.deptno,:old.deptno)
18 ,sysdate
19 ,'O departamento ' ||
nvl(:new.dname,:old.dname)||'
309

## Página 321

19.3. Triggerdelinha CasadoCódigo
foi '||wacao||'.');
20 --
21 end;
22 /
Gatilho criado.
SQL>
O triggeremquestãotemoobjetivodeverificarqualaaç ãofoiexe-
cutadanatabelaeapartirdestainformaç ãomontarohistórico.Testandoa
geraçãodohistórico:
SQL> update dept
2 set dname = dname;
4 linhas atualizadas.
SQL> insert into dept values (50,'TI','BRASIL');
1 linha criada.
SQL> delete dept where deptno = 50;
1 linha deletada.
SQL>
Agoraexecutamosumasériedeaçõesemcimadatabela dept,parater-
mosdiferentestiposdehistórico.Vamosverificar:
SQL> select * from tab_hist_dept;
DEPTNO DT_HISTO DS_HISTORICO
---------- -------- -----------------------------------------
10 09/09/11 O departamento ACCOUNTING foi atualizado.
20 09/09/11 O departamento RESEARCH foi atualizado.
30 09/09/11 O departamento SALES foi atualizado.
40 09/09/11 O departamento OPERATIONS foi atualizado.
50 09/09/11 O departamento TI foi inserido.
50 09/09/11 O departamento TI foi excluído.
310

## Página 322

CasadoCódigo Capítulo19. Triggers
6 linhas selecionadas.
SQL>
Através dos predicados é possível determinar qual ação disparou o
triggere,comisso,fazercomqueoprogramatomedecisõesecaminhosdi-
ferentes.Devemosobservaralgumasrestriçõesecaracterísticascomrelaç ão
àcriaçãoemanipulaç ãodos triggersquediferemdeumblocoPL/SQL,
sendoesteanônimoounão.Dentrodeum triggernãopodemosutilizar
commitou rollback,amenosqueestejamosutilizando pragma.Seuuso
serádiscutidomaisadiante. Foraestaexce ção,nãoépermitidaautilizaç ão
destescomandosdentrodocódigodos triggers.Dessaforma,paravalidar
asalteraçõesrealizadaspelo triggerénecessáriaumaefetivaçãoexterna,
geralmentevindodoprogramacausadordodisparodoseudisparo. Temos
asseguintespremissas:
• Nãosãopermitidoscomandosdeddldentrode triggers;
• Não são permitidos comandos de controle da transação, como
rollback, commit, savepointetc.(excetocomousode pragma).
Outropontoquedeveserobservadoécomrelaç ãoàcriaç ãodeum
trigger.Quandoocriamos,oOraclefazvalidaçõesigualmenteaquando
criamos procedures, functionsou packages.Seeste triggerapre-
sentaralgumerrodesintaxe,objetosnãoexistentes,errosdereferênciaou
qualqueroutroproblemaqueimpossibiliteseuuso,oOraclepermiteacria-
ção,masodeixainválidonobancodedados.
Destaforma,o triggernãoficaaptoparaousoenãoserádisparado
mesmoqueasaçõessatisfaç amsuasdefinições.Nestecaso,eledeveserana-
lisado,corrigidoerecriado,novamente.Quandoissoacontecer,nãoéneces-
sárioexcluí-lo,bastarecriá-lo.Bastausarocomando replacenomomento
emqueestiverrecriando.Nasequência,mostroumexemplo:
SQL> create or replace trigger tig_hist_cargo_emp
2 after update of job on emp
3 referencing old as v
311

## Página 323

19.3. Triggerdelinha CasadoCódigo
4 new as n
5 for each row
6 begin
7 insert into tab_hist_cargo_emp ( empno
8 ,job_anterior
9 ,job_atual
10 ,dt_alteracao_cargo
11 ,ds_historico)
12 values ( :n.empno
13 ,:v.job
14 ,:n.job
15 ,sysdate
16 ,'O empregado '||:n.ename||
17 ' passou para o cargo '||:n.job||
18 ' em carater de promoção.');
19
20 end;
21 /
Gatilho criado.
SQL>
Casosejanecessáriocompilarum triggerpelofatodeeleestarinválido,
useocomando alter trigger.Todavia,nãoécomum,poisaocriá-loou
recriá-looOraclejáfazestavalidação,amenosqueeletenhasidoinvalidado
viadependênciadealgumoutroobjeto.
SQL> alter trigger tig_hist_cargo_emp compile;
Gatilho alterado.
SQL>
Tambémpodemosativaroudesativarum trigger.Quandoodesativa-
mos,elepermanececriadonobancodedados,masficainativo.Destaforma,
elenãodisparacasoatabeladereferênciasejamanipulada. Paraativarou
desativarum trigger,tambémutilizamosocomando alter table.
312

## Página 324

CasadoCódigo Capítulo19. Triggers
SQL> alter trigger tig_hist_cargo_emp disable -- desabilita o
trigger
2 /
Gatilho alterado.
SQL> alter trigger tig_hist_cargo_emp enable -- habilita o
trigger
2 /
Gatilho alterado.
SQL>
Tambémépossívelhabilitaroudesabilitartodosos triggersassocia-
dosaumatabelacomumcomandoapenas.
SQL> alter table emp disable all triggers;
Tabela alterada.
SQL> alter table emp enable all triggers;
Tabela alterada.
SQL>
Paraeliminarum trigger,utilizamosocomando frop trigger.
Essecomandofazcomqueelesejaeliminadodefinitivamente.
SQL> drop trigger tig_hist_cargo_emp;
Gatilho eliminado.
SQL>
Parasecriarum trigger,ousuáriodevepossuirosprivilégiosdecri-
ação: create trigger (ou create any trigger)e alter table.
Esteúltimoestárelacionadoàtabelabaseparao trigger.Quandoousuá-
riotemprivilégiosparacriaç ãodetabelas,implicitamente,játeráopoder
313

## Página 325

19.3. Triggerdelinha CasadoCódigo
paraalterá-lasouexcluí-las. Vejaumexemplodeconcessãodeprivilégios
para triggers.
Nota: create any trigger permite que o usuário crie
triggersemqualqueresquema,exceto sys.Issonãoérecomendado
paraacriaç ãodelesemtabelasdedicionáriodedados.
SQL> grant create trigger to tsql;
Concessão bem-sucedida.
SQL> grant create any trigger to tsql;
Concessão bem-sucedida.
SQL>
Pararecuperaradefiniç ãoeocódigodeum trigger,useas views
user_triggers, all_triggerou dba_triggers.
SQL> select trigger_body
2 from user_triggers where trigger_name = 'TIG_PC_COM_SAL_EMP';
TRIGGER_BODY
-----------------------------------------------------------------
begin
:n.pc_com_sal := nvl(:n.comm,0) * 100 / :n.sal;
end;
SQL>
Nogeral,os triggersdebancodedadospodemservir,porexemplo,
paracontrole,seguran çaeauditoriadeinformaçõesdetabelasemumbanco
dedados,paraarealizaç ãodebackupsoureplicaç ãodedados,objetivando
sempreaautomaçãodealgumprocesso.
314

## Página 326

CasadoCódigo Capítulo19. Triggers
Sequência de disparo de um trigger
Umatabelanãoestálimitadaaapenasum trigger. Podemostervá-
riosassociadosaumaúnicatabela. Quandoissoacontece,temosquenos
preocuparcomalgunsaspectos,porexemplo,seaordemdeexecuç ãodeum
determinado triggerinfluenciaemumaexecuç ãodeumoutro.Paraisso,
éprecisoentenderaordemdeexecuç ãodos triggers,quedependedotipo
edomomentoemqueserádisparado.Olhandoodesenhoaseguir,ficamais
claraaordemdeexecuç ão,dependendodotipoedomomentoemquesão
disparados.
Imagineoseguintecenário:temosdois triggers,umdetabela(cha-
madode tgrtab)eoutrodelinha(chamadode tgrlin). O trigger
detabeladisparatantonomomento beforequantonomomento after.
O triggerdelinhasegueamesmalógica.Ambossãodisparadosnaaç ão
update. Vamosvercomoficaaordemdedisparoquandoexecutamosum
updatenosregistros.
Fig.19.1:Esquemamostrandoasequênciadedisparodastriggersdelinhade
tabela
Notequeo trigger tgrtab executaumaúnicavezantesnaatualiza-
çãodetodososregistroseumaúnicaveznofinalquandotodososregistrosjá
foramatualizados.Jáo trigger tgrlin executaapósaprimeiraexecuç ão
do trigger tgrtab eantesedepoisdaatualizaç ãodecadaregistro.
315

## Página 327

19.4. Mutantetable CasadoCódigo
Outropontoaserobservadoéquenãoháimpedimentoalgumemtermos
dois triggersexatamenteiguais,quesejamdomesmotipoequedisparem
nomesmomomento.Entretanto,paraestescasos,nãoépossíveldeterminar
qualaordememquecadaumseráexecutado. AOraclenãogaranteaor-
demdaexecuç ãoquandohá triggerscontendocaracterísticasdedisparo
iguais. Casosejamdependentesumdooutro,oaconselháveléjuntá-los,e
quetaisdependênciassejamtratadasnocódigo.
19.4 M utante table
Existeumalimitaç ãonousodos triggers de linha,quandoselecionamosda-
dosdeumatabela,noevento after,quesejaabasedo trigger,ouseja,
estamostentandoselecionarosdadosdeumatabelaqueestásendoalterada
eaomesmotempoéacausadoradodisparo. Contudo,quandotempseste
cenário,masoeventoéo before,esteproblemanãoacontece.
Quandoum triggerédisparado,issoindicaqueosdadosdeumata-
belaestãosendoalterados.Nestemomentopodemosconcluirque,enquanto
asalteraçõesnãoforemconfirmadas,osdadosqueestãosendomanipulados
natransaçãoemquestãonãoestãoconsistentes.Apenasquandoforemcon-
firmados,atravésdeum rollbackoudeum commit,osdadosestarão
íntegros.
Seguindoestalógica,nomomentoantesdaefetivaç ãodosdadosaltera-
dos,nãoépossívelexecutaramanipulaç ãodeles,porexemplo,atravésdeum
comando select,mesmosenossainten çãosejabuscarapenasosregistros
quenãoestãosofrendotaisalterações.Issoconfirmaalimitaç ãononívelde
tabelaenãononíveldedados.Quandotentamosrealizarestaoperaç ão,um
errochamado mutante table égerado.Vejaoresumodasregrasaseguir:
• Oerrodemutante table nãoacontecequandoa triggeréde
linhaeomomentodedisparofor before,issotantoparaoscomandos
delete, update, insertou select.Jánoevento after,oerrode
mutante table aconteceparatodosestescomandos(comexce ção
dousodetransaçõesautônomas);
• Paraastriggersdetabela,nãoprecisamosnospreocuparcomo
errode mutante table,poisindependentedeoeventoser before
316

## Página 328

CasadoCódigo Capítulo19. Triggers
ou after,edequalsejaocomando, select, delete, updateou
insert,essetipodeproblemanãoocorre.
Agoraveremosoexemplonasequência:
SQL> create or replace trigger tig_emp_pragma
2 after update on emp
3 for each row
4 declare
5 wcont_registro number default 0;
6 begin
7 --
8 select count(*) into wcont_registro from emp;
9 --
10 dbms_output.put_line('Quantidade de registros na tabela
EMP: '||wcont_registro);
11 --
12 end;
13 /
Gatilho criado.
SQL>
Criamosum triggerdotipolinha,comoqualacadaatualizaç ãore-
alizadanosregistrosdatabela empéexecutadoum select count para
verificaremostraraquantidadederegistrosdestamesmatabela.Agorava-
mosexecutarocomandoaseguir:
SQL> update emp
2 set sal = sal
3 /
update emp
*
ERRO na linha 1:
ORA-04091: a tabela TSQL.EMP é mutante; talvez o gatilho/função
não possa localizá -la
ORA-06512: em "TSQL.TIG_EMP_PRAGMA", line 5
ORA-04088: erro durante a execução do gatilho
317

## Página 329

19.4. Mutantetable CasadoCódigo
'TSQL.TIG_EMP_PRAGMA'
SQL>
Comoeraprevisto,oerroocorreuapóstentarmosrealizaraalteraç ão.
Agoravamosrecriaro triggercomosendoumdetabelaeexecutaraatu-
alizaçãonovamente.
SQL> create or replace trigger tig_emp_pragma
2 after update on emp
3 declare
4 wcont_registro number default 0;
5 begin
6 --
7 select count(*) into wcont_registro from emp;
8 --
9 dbms_output.put_line('Quantidade de registros na tabela
EMP: '||wcont_registro);
10 --
11 end;
12 /
Gatilho criado.
SQL>
SQL> update emp
2 set sal = sal;
Quantidade de registros na tabela EMP: 14
Notequequandoutilizamosum triggerdotipotabelanãotemoseste
problema. Masaívemapergunta:esetivermosestanecessidadeenosde-
pararmoscomesteproblema?Oquefazer?Nestescasos,podemosutilizaro
recursodetransaçõesautônomas,informando-onadeclaraç ãodo trigger.
Suafun çãoéfazercomqueoOracleabraumanovasessãosomenteparaaten-
dero trigger,ouseja,nestemomentoexistirãopelomenosduastransações
emaberto.Umaéreferenteàtransaç ãoqueestárealizandoasalteraçõesna
318

## Página 330

CasadoCódigo Capítulo19. Triggers
tabelaemquestão,eoutrareferenteaodisparodo trigger.Vejaodesenho
aseguirondetentamosilustramoscomooOracletrataestasituaç ão.
Fig.19.2:Abrindotransaçõesatravésdepragmaautonomous_transaction
Contudo,conformejáexplicadonocapítuloanteriorsobretransações
autônomas,temosquenosatentarparaaseguintesituaç ão. Sabemosque,
quandoéabertaumatransaç ãonoOracle,elamontaumaimagemdosobje-
tosedadosdisponíveisparaousuárioemquestão.Comrelaç ãoaosdados,
issopermitevisualizarsomenteaquiloqueestáefetivadonobancodedados,
ouseja,dadosconsistenteseíntegros. Issoquerdizerquedadospendentes
deefetivaçãonãopoderãoservisualizados,issoé,dadosexcluídos,inseridos
ouatualizadosqueaindanãotenhamsido commitados.
Logo,quandoissoacontece,nocasodeum trigger,nãoconseguimos
visualizarasalteraçõesqueestãosendorealizadas,pelomenosnãoasque
fogemdoescopo olde new. Portanto,quandotemosum triggercom
transaçãoautônoma,conseguimosmanipularosdadosde olde new,mas
319

## Página 331

19.4. Mutantetable CasadoCódigo
serealizarmosumcomando selectafimdeobterestesdados,nãoconse-
guiremosenxergá-los.Apenaspararessaltar,istosedáaofatodequedentro
do triggerestamosemoutroescopo,emumanovatransaç ão.
Outropontomuitoimportanteéquequandoutilizamos triggercom
transaçãoautônomaprecisamosfinalizá-laatravésdeum commitoudeum
rollback. Comoa autonomous_transactionfazcomqueumanova
transaçãosejaaberta,temosquefinalizá-la. Casocontrário,elaficariapen-
denteeissopoderiagerarumerro.Vamosverificarnaprática:
SQL> create or replace trigger tig_emp_pragma
2 before update on emp
3 for each row
4 declare
5 --
6 pragma autonomous_transaction;
7 --
8 wcont_registro number default 0;
9 begin
10 --
11 select count(*) into wcont_registro from emp;
12 --
13 if nvl(:old.comm,0) < 300 then
14 :new .comm := :new.sal * 10 / 100;
15 end if;
16 --
17 dbms_output.put_line('Quantidade de registros na tabela
EMP: '||wcont_registro);
18 --
19 commit;
20 --
21 end;
22 /
Gatilho criado.
SQL>
Uma observação: para este exemplo alteramos o trigger de
after para before para que pudéssemos alterar o valor denew.
320

## Página 332

CasadoCódigo Capítulo19. Triggers
Note que na área de declaração colocamos a seguinte linha:pragma
autonomous_transaction;. Issofazcomqueumanovatransaç ãoseja
abertaparaaexecuç ãodo trigger. Agoravamosexecutarumaalteraç ão
natabela empeveremoscomoelesecomporta.
SQL> update emp
2 set sal = sal
3 /
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
Quantidade de registros na tabela EMP: 14
14 linhas atualizadas.
SQL>
Aexecuçãonãonosgerouerro.Vamosverificaratabela emp.Antesda
execuçãodaatualizaç ãoedisparodo triggerosdadosestavamassim:
SQL> select empno, ename, sal, comm from emp;
EMPNO ENAME SAL COMM
---------- ---------- ---------- ----------
7369 SMITH 968
7499 ALLEN 1600 306
7521 WARD 1250 510
7566 JONES 3599,75
7654 MARTIN 1250 1428
321

## Página 333

19.4. Mutantetable CasadoCódigo
7698 BLAKE 2850
7782 CLARK 2450
7788 SCOTT 3630
7839 KING 5000
7844 TURNER 1500 0
7876 ADAMS 1331
7900 JAMES 950
7902 FORD 3630
7934 MILLER 1300
14 linhas selecionadas.
SQL>
Apósaexecuç ãodaatualizaç ãoedisparodo triggerosdadosficaram
assim:
SQL> select empno, ename, sal, comm from emp;
EMPNO ENAME SAL COMM
---------- ---------- ---------- ----------
7369 SMITH 968 96,8
7499 ALLEN 1600 306
7521 WARD 1250 510
7566 JONES 3599,75 359,98
7654 MARTIN 1250 1428
7698 BLAKE 2850 285
7782 CLARK 2450 245
7788 SCOTT 3630 363
7839 KING 5000 500
7844 TURNER 1500 150
7876 ADAMS 1331 133,1
7900 JAMES 950 95
7902 FORD 3630 363
7934 MILLER 1300 130
14 linhas selecionadas.
SQL>
322

## Página 334

CasadoCódigo Capítulo19. Triggers
Agoravamoscadastrarumnovoempregadoatravésdeum insertpara
vermosbemocontroledetransaç ãosendoconsistido. Paraisso,alteramos
novamentenosso trigger,incluindonascondiçõesdedisparoocomando
insert.
SQL> create or replace trigger tig_emp_pragma
2 before update or insert on emp
3 for each row
4 declare
5 --
6 pragma autonomous_transaction;
7 --
8 wcont_registro number default 0;
9 begin
10 --
11 select count(*) into wcont_registro from emp;
12 --
13 if nvl(:old.comm,0) < 300 then
14 :new .comm := :new.sal * 10 / 100;
15 end if;
16 --
17 dbms_output.put_line('Quantidade de registros na tabela
EMP: '||wcont_registro);
18 --
19 commit;
20 --
21 end;
22 /
Gatilho criado.
SQL>
Executandoo insert.
SQL> insert into emp
2 (empno, ename, job, mgr, hiredate, sal, comm, deptno,
pc_com_sal)
3 values
323

## Página 335

19.5. Triggerdesistema CasadoCódigo
4 (7935, 'PAUL', 'SALESMAN', 7698, to_date('15-MAR-1980',
'dd-mon-rrrr'),
1000, 100, 30, null);
Quantidade de registros na tabela EMP: 14
1 linha criada.
SQL>
Notequeamensagemvindado triggernosinformouquetemos14
registros,ouseja,elenãoestácontandocomestequeacabamosdeinserir,
queseriaoregistro15. Mesmoquealteremoso triigerparaquedispare
nomomento after,elenãovaienxergaronovoregistro,poiso insertestá
acontecendonumatransaçãoeacontagemdoregistro,feitapelo trigger,
aconteceemoutra.
Semesmocomousodetransaçõesautônomasnãoforpossívelresolver
problemasde mutante table,talvezmesclarousode triggersdelinha
comosdetabelapossaserumasaída.
Considerações sobre triggers
• Umtriggertantodelinhaquantodetabelapodeagirdeformare-
cursiva.OOraclegaranteaté50níveisderecursividadeparaestesdois
tiposdeobjeto;
• Umtriggernãopodecontemplareventosdiferentesdeexecuç ão(
beforeou after)emummesmoobjeto. Devemsercriadosdois
triggersdistintos;
• Aoexcluirumatabela,triggersassociadasaelatambémsãoexcluí-
dosautomaticamente.
19.5 T rigger de sistema
Trigger de sistemasãoobjetoscriadosemníveldesistemaenãodetabelas.
Quandofalamosemsistemasnosreferimosaobancodedados,maispreci-
324

## Página 336

CasadoCódigo Capítulo19. Triggers
samenteaaçõesqueocorremnele.SeuusoémaiscomumpelosDBAs(ad-
ministradoresdebancodedados)eéumaferramentapoderosaquandouti-
lizadacomcriatividade.
Ostriggersdesistemadisparamconformeumeventoqueaconteceno
bancodedados.Vejaaseguiralistadealgunseventos:
•startup:quandoobancodedadoséaberto;
•shutdown: antes de o banco de dados iniciar o
shutdown(fechamento). Se for shutdown abort este evento
nãoédisparado;
•servererror:quandoumerroocorre.Comexce çãodoserros:ORA-
1034,ORA-1403,ORA-1422,ORA-1423eORA-4030;
•after logon:depoisdeumaconexãosercompletadanobancode
dados;
•before logoff:quandoousuáriodesconectadobancodedados;
•before create / after create:quandoumobjetoécriadono
banco de dados (comandocreate), exceto o comandocreate
database;
•before alter / after alter: quandoumobjetoéalteradono
bancodedados(comando alter),comexce çãodocomando alter
database;
•before drop / after drop: quandoumobjetoéeliminadodo
bancodedados(comando drop);
•before analyze / after analyze:quandoocomando analyze
éexecutado.Estecomandoéutilizadoparagerarestatísticasrelaciona-
dasaodesempenhodecomandosSQLeprocessosdobancodedados;
•before commit / after commit: quandoum commitéexecu-
tado;
325

## Página 337

19.5. Triggerdesistema CasadoCódigo
•before ddl / after ddl: quando um comando ddl é exe-
cutado, com exceção dos comandosalter database, create
controlfile, create database e ddlexecutadosapartirdein-
terfacePL/SQL;
•before grant / after grant:quandoocomando grantéexe-
cutado;
•before rename / after rename:quandoo renameéexecutado;
•before revoke / after revoke:quandoocomando revokeé
executado;
•before truncate / after truncate: quandoo truncateé
executado.
Alémdecontarcomoseventosparadeterminarquandoo trigger de sis-
temadevedisparar,tambémtemosadisposiç ãoosatributosdeeventoque
nosdãoinformaçõessobreobancodedados,transaçõesesobreasoperações
quedisparamo trigger.Vejaalistaaseguir.
•ora_client_ip_address(tipo: varchar2):retornaoIPdamá-
quinaclientenoeventodeLOGON,seoprotocoloforTCP/IP;
•ora_database_name(tipo: varchar2(50)): nomedobancode
dados;
•ora_dict_obj_name(tipo: varchar(30)): nomedoobjetoque
sofreuoevento ddl;
•ora_dict_obj_name_list(name_list out
ora_name_list_t) (tipo: binary_integer): retorna lista
deobjetosafetadosnoevento;
•ora_dict_obj_ownerR(tipo: varchar(30)):proprietário(usuá-
rio/schema)doobjetoquesofreuoevento ddl;
•ora_dict_obj_owner_list(OWNER_LIST OUT
ora_name_list_t) (tipo: binary_integer): retorna lista
deproprietários(usuário/schemas)dosobjetosafetadosnoevento;
326

## Página 338

CasadoCódigo Capítulo19. Triggers
•ora_dict_obj_type(tipo: varchar(20)):tipodeobjetoqueso-
freuoevento ddl;
•ora_grantee(user_list out ora_name_list_t) (tipo:
binary_integer):retornalistadeusuáriosourolesquereceberam
grant;
•ora_is_alter_column(column_name in varchar2) (tipo:
boolean):retorna trueseacolunaespecificadafoialterada;
•ora_is_drop_column(column_name in varchar2) (tipo:
boolean):retorna trueseacolunaespecificadafoieliminada;
•ora_login_user(tipo: varchar2(30)):nomedousuárioqueaca-
boudeconectaremumasessãodobancodedados;
•ora_privileges(privilege_list out ora_name_list_t)
(tipo: binary_integer): retorna lista de privilégios dados ou
revogados;
•ora_revokee(user_list out ora_name_list_t) (tipo:
binary_integer):retornalistadosqueperderamprivilégios;
•ora_sysevent(tipo: varchar2(20)):retornaonomedoevento
quefoidisparado.Onomeéomesmousadonadefiniç ãodo trigger;
•ora_with_grant_option(tipo: boolean): retorna trueseo
granttem with grant option.
Nasequência,algunsexemplos:
SQL> create table hist_usuario
2 (
3 nm_usuario varchar2(50)
4 ,dt_historico date
5 ,ds_historico varchar2( 4000)
6 )
7 /
327

## Página 339

19.5. Triggerdesistema CasadoCódigo
Tabela criada.
SQL>
Criamosumatabelaparaguardaroshistóricosgeradospelos triggers.
Noexemploaseguir,temosumqueregistraquandoousuárioconectano
bancodedados.
SQL> create or replace trigger tgr_hist_conexao_usuario
2 after logon on database
3 begin
4 insert into hist_usuario values
5 (ORA_LOGIN_USER,sysdate,'Conexão com o banco de dados
'||ORA_DATABASE_NAME);
6 end;
7 /
Gatilho criado.
SQL>
Conectandoaobancodedados:
SQL> disconnect
Desconectado de Oracle Database 10g Express Edition Release
10.2.0.1.0 - Production
SQL>
SQL> conn tsql/tsql@xe;
Conectado.
SQL>
SQL>
Nota:Comojáestávamosconectadosaobancodedados,primeira-
mente,desconectamoserefizemosaconexãologoapós.
Verificandohistórico:
328

## Página 340

CasadoCódigo Capítulo19. Triggers
SQL> select * from hist_usuario;
NM_USUARIO DT_HISTO DS_HISTORICO
-------------------- -------- -----------------------------------
TSQL 04/10/11 Conexão com o banco de dados XE
SQL>
Comopodeservisto,o triggergravouohistóricocomasinformações
pertinentesaousuárioqueconectounobancodedados.
Opróximoregistraalteraçõesde dmlrealizadospelousuário,maispre-
cisamenteacriaç ãodeobjetosnosistema.
SQL> create or replace trigger tgr_hist_criatab_usuario
2 after create on database
3 begin
4 insert into hist_usuario values
5 (ORA_LOGIN_USER,sysdate,
'O Objeto '||ORA_DICT_OBJ_NAME||' foi criado
no banco de dados.');
6 end;
7 /
Gatilho criado.
SQL>
Criandooobjetotabela teste_trigger:
SQL> create table teste_trigger
2 (
3 id_campo varchar2(50)
4 ,nm_campo date
5 ,ds_campo varchar2(4000)
6 )
7 /
Tabela criada.
SQL>
329

## Página 341

19.6. Triggerdeview CasadoCódigo
Verificandotabeladehistórico:
SQL> select * from hist_usuario;
NM_USUARIO DT_HISTO DS_HISTORICO
--------------- -------- ----------------------------------------
TSQL 04/10/11 O objeto TESTE_TRIGGER foi criado no
banco de dados.
SQL>
19.6 T rigger de view
Aprendemosanteriormentequeum triggerpodeestarassociadoauma
tabelaouaoaventodesistema.Contudo,quandoestamosfalandodeviews,
quesãobemsemelhantesatabelas,pelomenosnaformadeapresentaç ão
dosdados,existeapossibilidadedecriarmosum triggereoassociarmos
tambémaestetipodeobjeto.
Emregrasgerais,sóconseguimoscriarum triggerparaumadeter-
minadaviewquesejacompostadeapenasumatabela. Noentanto,secri-
armosum triggerusandoacláusula instead of,podemostrabalhar
com triggersassociadasaviewscompostasdeumaoumaistabelas. O
triggerusadocom instead of temsuadefiniç ãoumpoucodiferente,
poisestacláusulasubstituioseventos beforee after. Outropontoque
deveserobservadoéqueousodestacláusulasópodeserempregadocom
triggers de linha.
Aquestãodepoderounãocriarum triggerparaumaviewestárelacio-
nadaàsoperaçõesquepodemosefetuaremcimadestaview.Esquecendoum
poucoos triggers,sabemosqueoperaçõesdeDML( insert, delete
ou update)sópodemocorrerquandoaviewfordeapenasumatabela.Por-
tanto,autilizaç ãode triggersemviewssegueosmesmosprincípios. A
únicadiferençaéquequandoutilizamos triggerspararealizarcomando
DMLemviewspodemosutilizá-loscomaop ção instead of,oquetorna
possíveltratardeformadiferenteasviewsquepossuammaisdeumatabela
nasuacomposiç ão.
330

## Página 342

CasadoCódigo Capítulo19. Triggers
Aseguir,umexemplodeumaviewcompostapelastabelas empe dept
ondenósvamosinserirdados.Criando viewdeempregadospordeparta-
mento:
SQL> create view emp_dept_v as
2 select e.empno, e.ename, e.job, e.sal, d.dname
3 from emp e
4 ,dept d
5 where e.deptno = d.deptno
6 ;
View criada.
SQL>
Selecionandodados:
SQL> select * from emp_dept_v;
EMPNO ENAME JOB SAL DNAME
---------- ---------- --------- ---------- --------------
7369 SMITH CLERK 968 RESEARCH
7499 ALLEN SALESMAN 1600 SALES
7521 WARD SALESMAN 1250 SALES
7566 JONES MANAGER 3599,75 RESEARCH
7654 MARTIN SALESMAN 1250 SALES
7698 BLAKE MANAGER 2850 SALES
7782 CLARK MANAGER 2450 ACCOUNTING
7788 SCOTT ANALYST 3630 RESEARCH
7839 KING PRESIDENT 5000 ACCOUNTING
7844 TURNER SALESMAN 1500 SALES
7876 ADAMS CLERK 1331 RESEARCH
7900 JAMES CLERK 950 SALES
7902 FORD ANALYST 3630 RESEARCH
7934 MILLER CLERK 1300 ACCOUNTING
7935 PAUL SALESMAN 1000 SALES
15 linhas selecionadas.
SQL>
331

## Página 343

19.6. Triggerdeview CasadoCódigo
Criando triggercom instead of paramanipulaçãodosdados:
SQL> create or replace trigger trg_emp_dept_v
2 instead of
3 insert or delete or update
4 on emp_dept_v
5 referencing new as new old as old
6 declare
7 cursor c1(pdeptno dept.deptno%type) is
8 select deptno, dname
9 from dept
10 where deptno = pdeptno;
11 --
12 cursor c2(pempno emp.empno %type) is
13 select empno, ename
14 from emp
15 where empno = pempno;
16 --
17 wdeptno dept.deptno%type;
18 wdname dept.dname%type;
19 wempno emp.empno%type;
20 wename emp.ename%type;
21 begin
22 --
23 if inserting then
24 --
25 -- verifica se existe departamento.
26 open c1 (:new.deptno);
27 fetch c1 into wdeptno, wdname;
28 --
29 if c1%notfound then
30 insert into dept (deptno, dname, loc)
values (:new.deptno, :new.dname, null);
31 --
32 dbms_output.put_line(
'Departamento cadastrado com sucesso.');
33 else
34 dbms_output.put_line(
'Departamento existente: '||wdeptno||' -
332

## Página 344

CasadoCódigo Capítulo19. Triggers
'||wdname||'.');
35 end if;
36 --
37 -- verifica se existe empregado.
38 open c2 (:new.empno);
39 fetch c2 into wempno, wename;
40 --
41 if c2%notfound then
42 insert into emp (empno, ename, job, sal, mgr, deptno)
43 values (:new.empno, :new.ename, :new.job, :new.sal,
:new.mgr, :new.deptno);
44 --
45 dbms_output.put_line(
'Funcionário cadastrado com sucesso.');
46 else
47 dbms_output.put_line(
'Funcionário existente: '||wempno||' -
'||wename||'.');
48 end if;
49 --
50 end if;
51 --
52 end;
53 /
Gatilho criado.
SQL>
Naprimeirapartedacriaç ãodo triggervamostrataraaç ãode insert
naview emp_dept_v.Aseguirtemosváriasexecuçõesondetestamos,pri-
meiramente,ocomando insert.
SQL> insert into emp_dept_v (empno, ename, job, sal, mgr,
deptno, dname)
2 values (8000, 'BRUCE', 'MANAGER', 1000,
7839, 20, 'RESEARCH');
Departamento existente: 20 - RESEARCH.
Funcionário cadastrado com sucesso.
333

## Página 345

19.6. Triggerdeview CasadoCódigo
1 linha criada.
SQL>
SQL> insert into emp_dept_v (empno, ename, job, sal, mgr, deptno,
dname)
2 values (8000, 'BRUCE', 'MANAGER', 1000,
7839, 20, 'RESEARCH');
Departamento existente: 20 - RESEARCH.
Funcionário existente: 8000 - BRUCE.
1 linha criada.
SQL>
SQL> insert into emp_dept_v (empno, ename, job, sal, mgr, deptno,
dname)
2 values (8001, 'SILVESTER', 'MANAGER', 1000,
7839, 80, 'S&E');
Departamento cadastrado com sucesso.
Funcionário cadastrado com sucesso.
1 linha criada.
SQL>
SQL> insert into emp_dept_v (empno, ename, job, sal, mgr, deptno,
dname)
2 values (8001, 'SILVESTER', 'MANAGER', 1000,
7839, 90, 'FINANCIAL');
Departamento cadastrado com sucesso.
Funcionário existente: 8001 - SILVESTER.
1 linha criada.
SQL>
SQL> insert into emp_dept_v (empno, ename, job, sal, mgr, deptno,
dname)
2 values (8002, 'WILL', 'MANAGER', 1000, 7839,
90, 'FINANCIAL');
334

## Página 346

CasadoCódigo Capítulo19. Triggers
Departamento existente: 90 - FINANCIAL.
Funcionário cadastrado com sucesso.
1 linha criada.
SQL>
Agoravamosparaasegundapartedo trigger,ondevamostratara
ação update.Criaçãodo trigger:
SQL> create or replace trigger trg_emp_dept_v
2 instead of
3 insert or delete or update
4 on emp_dept_v
5 referencing new as new old as old
6 declare
7 cursor c1(pdeptno dept.deptno%type) is
8 select deptno, dname
9 from dept
10 where deptno = pdeptno;
11 --
12 cursor c2(pempno emp.empno%type) is
13 select empno, ename
14 from emp
15 where empno = pempno;
16 --
17 wdeptno dept.deptno%type;
18 wdname dept.dname%type;
19 wempno emp.empno%type;
20 wename emp.ename%type;
21 begin
22 --
23 ----------------------------------------------------------
24 if inserting then
25 --
26 -- verifica se existe departamento.
27 open c1 (:new.deptno);
28 fetch c1 into wdeptno, wdname;
29 --
335

## Página 347

19.6. Triggerdeview CasadoCódigo
30 if c1%notfound then
31 insert into dept (deptno, dname, loc)
values (:new.deptno, :new.dname, null);
32 --
33 dbms_output.put_line('Departamento cadastrado com
sucesso.');
34 else
35 dbms_output.put_line('Departamento existente:
'||wdeptno ||' - ' ||wdname||'.');
36 end if;
37 --
38 -- verifica se existe empregado.
39 open c2 (:new.empno);
40 fetch c2 into wempno, wename;
41 --
42 if c2%notfound then
43 insert into emp (empno, ename, job, sal, mgr, deptno)
44 values (:new.empno, : new.ename, :new.job,
:new.sal,:new.mgr, :new.deptno);
45 --
46 dbms_output.put_line('Funcionário cadastrado com
sucesso.');
47 else
48 dbms_output.put_line('Funcionário existente:
'||wempno||' - '||wename||'.');
49 end if;
50 --
51 ----------------------------------------------------------
52 elsif updating then
53 --
54 -- verifica se existe departamento.
55 open c1 (:new.deptno);
56 fetch c1 into wdeptno, wdname;
57 --
58 if c1%notfound then
59 --
60 dbms_output.put_line('Departamento não existe.');
61 --
62 else
336

## Página 348

CasadoCódigo Capítulo19. Triggers
63 --
64 update dept
65 set dname = :new.dname
66 where deptno = :new.deptno;
67 --
68 dbms_output.put_line('Departamento atualizado com
sucesso: '||: new.dname||'.');
69 --
70 end if;
71 --
72 -- verifica se existe empregado.
73 open c2 (:new.empno);
74 fetch c2 into wempno, wename;
75 --
76 if c2%notfound then
77 --
78 dbms_output.put_line('Funcionário não cadastrado.');
79 --
80 else
81 update emp
82 set ename = :new.ename
83 ,job = :new.job
84 ,sal = :new.sal
85 ,mgr = :new.mgr
86 ,deptno = : new.deptno
87 where empno = :new.empno;
88 --
89 dbms_output.put_line('Funcionário atualizado com
sucesso: '||: new.ename||'.');
90 --
91 end if;
92 --
93 end if;
94 --
95 end;
96 /
Gatilho criado.
337

## Página 349

19.6. Triggerdeview CasadoCódigo
SQL>
Testandoo trigger:
SQL> select * from emp_dept_v where empno = 8000;
EMPNO ENAME JOB SAL MGR
---------- ---------- --------- ---------- ----------
8000 BRUCE MANAGER 1000 7839
DEPTNO DNAME
---------- ----------
20 RESEARCH
SQL>
SQL> update emp_dept_v
2 set ename = 'BRUCEW'
3 ,job = 'ANALYST'
4 ,sal = 1500
5 ,deptno = 20
6 ,dname = 'RESEARCH'
7 where empno = 8000;
Departamento atualizado com sucesso: RESEARCH.
Funcionário atualizado com sucesso: BRUCEW.
1 linha atualizada.
SQL> select * from emp_dept_v where empno = 8000;
EMPNO ENAME JOB SAL MGR
---------- ---------- --------- ---------- ----------
8000 BRUCEW ANALYST 1500 7839
DEPTNO DNAME
---------- ----------
20 RESEARCH
SQL>
SQL> select * from emp_dept_v where deptno = 20;
338

## Página 350

CasadoCódigo Capítulo19. Triggers
EMPNO ENAME JOB SAL MGR
---------- ---------- --------- ---------- ----------
7369 SMITH CLERK 968 7902
7566 JONES MANAGER 3599,75 7839
7788 SCOTT ANALYST 3630 7566
7876 ADAMS CLERK 1331 7788
7902 FORD ANALYST 3630 7566
8000 BRUCEW ANALYST 1500 7839
SQL> select * from emp_dept_v where deptno = 20;
DEPTNO DNAME
---------- -----------
20 RESEARCH
20 RESEARCH
20 RESEARCH
20 RESEARCH
20 RESEARCH
20 RESEARCH
6 linhas selecionadas.
SQL>
SQL> update emp_dept_v
2 set dname = 'PESQUISA'
3 where deptno = 20;
Departamento atualizado com sucesso: PESQUISA.
Funcionário atualizado com sucesso: SMITH.
Departamento atualizado com sucesso: PESQUISA.
Funcionário atualizado com sucesso: JONES.
Departamento atualizado com sucesso: PESQUISA.
Funcionário atualizado com sucesso: SCOTT.
Departamento atualizado com sucesso: PESQUISA.
Funcionário atualizado com sucesso: ADAMS.
Departamento atualizado com sucesso: PESQUISA.
Funcionário atualizado com sucesso: FORD.
Departamento atualizado com sucesso: PESQUISA.
Funcionário atualizado com sucesso: BRUCEW.
339

## Página 351

19.6. Triggerdeview CasadoCódigo
6 linhas atualizadas.
SQL> select * from emp_dept_v where deptno = 20;
EMPNO ENAME JOB SAL MGR
---------- ---------- --------- ---------- ----------
7369 SMITH CLERK 968 7902
7566 JONES MANAGER 3599,75 7839
7788 SCOTT ANALYST 3630 7566
7876 ADAMS CLERK 1331 7788
7902 FORD ANALYST 3630 7566
8000 BRUCEW ANALYST 1500 7839
DEPTNO DNAME
---------- -----------
20 PESQUISA
20 PESQUISA
20 PESQUISA
20 PESQUISA
20 PESQUISA
20 PESQUISA
6 linhas selecionadas.
SQL>
Aexclusãofinalizaaúltimapartedonosso triggerdeview.
SQL> ed
Gravou arquivo afiedt.buf
1 create or replace trigger trg_emp_dept_v
2 instead of
3 insert or delete or update
4 on emp_dept_v
5 referencing new as new old as old
6 declare
7 cursor c1(pdeptno dept.deptno%type) is
8 select deptno, dname
9 from dept
340

## Página 352

CasadoCódigo Capítulo19. Triggers
10 where deptno = pdeptno;
11 --
12 cursor c2(pempno emp.empno%type) is
13 select empno, ename
14 from emp
15 where empno = pempno;
16 --
17 cursor c3(pdeptno dept.deptno%type) is
18 select count(*)
19 from emp
20 where deptno = pdeptno;
21 --
22 wdeptno dept.deptno%type;
23 wdname dept.dname%type;
24 wempno emp.empno%type;
25 wename emp.ename%type;
26 qt_empno number default 0;
27 begin
28 --
29 ----------------------------------------------------------
30 if inserting then
31 --
32 -- verifica se existe departamento.
33 open c1 (:new.deptno);
34 fetch c1 into wdeptno, wdname;
35 --
36 if c1%notfound then
37 insert into dept (deptno, dname, loc)
values (:new.deptno, :new.dname, null);
38 --
39 dbms_output.put_line(
'Departamento cadastrado com sucesso.');
40 else
41 dbms_output.put_line(
'Departamento existente: '||wdeptno||' -
'||wdname|| '.');
42 end if;
43 --
44 -- verifica se existe empregado.
341

## Página 353

19.6. Triggerdeview CasadoCódigo
45 open c2 (:new.empno);
46 fetch c2 into wempno, wename;
47 --
48 if c2%notfound then
49 insert into emp (empno, ename, job, sal, mgr, deptno)
50 values (:new.empno, : new.ename, :new.job, :new.sal,
:new.mgr, :new .deptno);
51 --
52 dbms_output.put_line(
'Funcionário cadastrado com sucesso.');
53 else
54 dbms_output.put_line(
'Funcionário existente: '||wempno||' - '||wename||'.');
55 end if;
56 --
57 ----------------------------------------------------------
58 elsif updating then
59 --
60 -- verifica se existe departamento.
61 open c1 (:new.deptno);
62 fetch c1 into wdeptno, wdname;
63 --
64 if c1%notfound then
65 --
66 dbms_output.put_line('Departamento não existe.');
67 --
68 else
69 --
70 update dept
71 set dname = :new.dname
72 where deptno = :new.deptno;
73 --
74 dbms_output.put_line('Departamento atualizado com
sucesso: '||:new.dname||'.');
75 --
76 end if;
77 --
78 -- verifica se existe empregado.
79 open c2 (:new.empno);
342

## Página 354

CasadoCódigo Capítulo19. Triggers
80 fetch c2 into wempno, wename;
81 --
82 if c2%notfound then
83 --
84 dbms_output.put_line('Funcionário não cadastrado.');
85 --
86 else
87 update emp
88 set ename = :new.ename
89 ,job = :new.job
90 ,sal = :new.sal
91 ,mgr = :new.mgr
92 ,deptno = : new.deptno
93 where empno = :new.empno;
94 --
95 dbms_output.put_line('Funcionário atualizado com
sucesso: '||: new.ename||'.');
96 --
97 end if;
98 --
99 ----------------------------------------------------------
100 elsif deleting then
101 --
102 -- verifica se existe empregado.
103 open c2 (: old.empno);
104 fetch c2 into wempno, wename;
105 --
106 if c2% notfound then
107 --
108 dbms_output.put_line('Funcionário não cadastrado.');
109 --
110 else
111 delete from emp where empno = :old.empno;
112 --
113 dbms_output.put_line('Funcionário excluído com
sucesso: '||: old.ename||'.');
114 --
115 end if;
116 --
343

## Página 355

19.6. Triggerdeview CasadoCódigo
117 -- verifica se existe departamento.
118 open c1 (: old.deptno);
119 fetch c1 into wdeptno, wdname;
120 --
121 if c1%notfound then
122 --
123 dbms_output.put_line('Departamento não existe.');
124 --
125 else
126 --
127 -- verifica se existe departamento.
128 open c3 (:old.deptno);
129 fetch c3 into qt_empno;
130 --
131 if qt_empno = 0 then
132 --
133 delete from dept where deptno = :old.deptno;
134 --
135 dbms_output.put_line('Departamento excluído com
sucesso: '||: old.dname||'.');
136 --
137 else
138 --
139 dbms_output.put_line('O departamento
'||:old.dname||'
não pode ser excluído.
Ainda existem
140 --
141 end if;
142 --
143 end if;
144 --
145 end if;
146 --
147* end;
SQL> /
Gatilho criado.
344

## Página 356

CasadoCódigo Capítulo19. Triggers
SQL>
Vamostestaraaç ãodeexclusão:
SQL> select * from emp_dept_v;
EMPNO ENAME JOB SAL MGR
---------- ---------- --------- ---------- ----------
7369 SMITH CLERK 968 7902
7499 ALLEN SALESMAN 1600 7698
7521 WARD SALESMAN 1250 7698
7566 JONES MANAGER 3599,75 7839
7654 MARTIN SALESMAN 1250 7698
7698 BLAKE MANAGER 2850 7839
7782 CLARK MANAGER 2450 7839
7788 SCOTT ANALYST 3630 7566
7839 KING PRESIDENT 5000
7844 TURNER SALESMAN 1500 7698
7876 ADAMS CLERK 1331 7788
7900 JAMES CLERK 950 7698
7902 FORD ANALYST 3630 7566
7934 MILLER CLERK 1300 7782
7935 PAUL SALESMAN 1000 7698
8001 SILVESTER MANAGER 1000 7839
8000 BRUCEW ANALYST 1500 7839
DEPTNO DNAME
---------- --------------
20 PESQUISA
30 SALES
30 SALES
20 PESQUISA
30 SALES
30 SALES
10 ACCOUNTING
20 PESQUISA
10 ACCOUNTING
30 SALES
20 PESQUISA
30 SALES
345

## Página 357

19.6. Triggerdeview CasadoCódigo
20 PESQUISA
10 ACCOUNTING
30 SALES
80 S&E
20 PESQUISA
17 linhas selecionadas.
SQL>
SQL> delete from emp_dept_v where empno = 8000;
Funcionário excluído com sucesso: BRUCEW.
O departamento PESQUISA não pode ser excluído. Ainda existem
funcionários agregados a ele.
1 linha deletada.
SQL> select * from emp_dept_v;
EMPNO ENAME JOB SAL MGR
---------- ---------- --------- ---------- ----------
7369 SMITH CLERK 968 7902
7499 ALLEN SALESMAN 1600 7698
7521 WARD SALESMAN 1250 7698
7566 JONES MANAGER 3599,75 7839
7654 MARTIN SALESMAN 1250 7698
7698 BLAKE MANAGER 2850 7839
7782 CLARK MANAGER 2450 7839
7788 SCOTT ANALYST 3630 7566
7839 KING PRESIDENT 5000
7844 TURNER SALESMAN 1500 7698
7876 ADAMS CLERK 1331 7788
7900 JAMES CLERK 950 7698
7902 FORD ANALYST 3630 7566
7934 MILLER CLERK 1300 7782
7935 PAUL SALESMAN 1000 7698
8001 SILVESTER MANAGER 1000 7839
DEPTNO DNAME
346

## Página 358

CasadoCódigo Capítulo19. Triggers
---------- --------------
20 PESQUISA
30 SALES
30 SALES
20 PESQUISA
30 SALES
30 SALES
10 ACCOUNTING
20 PESQUISA
10 ACCOUNTING
30 SALES
20 PESQUISA
30 SALES
20 PESQUISA
10 ACCOUNTING
30 SALES
80 S&E
16 linhas selecionadas.
SQL>
SQL> delete from emp_dept_v where deptno = 20;
Funcionário excluído com sucesso: SMITH.
O departamento PESQUISA não pode ser excluído. Ainda existem
funcionários agregados a ele.
Funcionário excluído com sucesso: JONES.
O departamento PESQUISA não pode ser excluído. Ainda existem
funcionários agregados a ele.
Funcionário excluído com sucesso: SCOTT.
O departamento PESQUISA não pode ser excluído. Ainda existem
funcionários agregados a ele.
Funcionário excluído com sucesso: ADAMS.
O departamento PESQUISA não pode ser excluído. Ainda existem
uncionários agregados a ele.
Funcionário excluído com sucesso: FORD.
Departamento excluído com sucesso: PESQUISA.
5 linhas deletadas.
347

## Página 359

19.6. Triggerdeview CasadoCódigo
SQL> select * from emp_dept_v;
EMPNO ENAME JOB SAL MGR
---------- ---------- --------- ---------- ----------
7499 ALLEN SALESMAN 1600 7698
7521 WARD SALESMAN 1250 7698
7654 MARTIN SALESMAN 1250 7698
7698 BLAKE MANAGER 2850 7839
7782 CLARK MANAGER 2450 7839
7839 KING PRESIDENT 5000
7844 TURNER SALESMAN 1500 7698
7900 JAMES CLERK 950 7698
7934 MILLER CLERK 1300 7782
7935 PAUL SALESMAN 1000 7698
8001 SILVESTER MANAGER 1000 7839
DEPTNO DNAME
---------- --------------
30 SALES
30 SALES
30 SALES
30 SALES
10 ACCOUNTING
10 ACCOUNTING
30 SALES
30 SALES
10 ACCOUNTING
30 SALES
80 S&E
11 linhas selecionadas.
SQL>
Comisso,encerramosoassuntosobre triggers.Comopôdeservisto,
estetipodeobjetoémuitointeressanteeútilparaimplementardiversostipos
derotinasquepossamserexecutadassemainterven çãodiretadousuárioe
comseguran ça,oquefazdeleumartifíciomuitopoderoso.
348

## Página 360

Capítulo20
PL/SQLTables(estruturas
homogêneas)
Conformecomentamosanteriormente,aPL/SQLcontemplaemsuaestru-
tura,todososrecursosencontradosemoutraslinguagensdeprogramaç ão.
Umrecursomuitobacanaéousodedadosintrínsecos,atravésdasestruturas
homogenias,comumente,chamadasde vetor.EmPL/SQLchamamoseste
recursode PL/SQL T able.
Paraquemnãoconhecevetores,umvetoréumaestruturaarraydeum
tipodefinidodedado. Porexemplo,podemosterumvetordenuméricos,
caracteresoudatas.Podemosimaginarumarray,oumelhor,umvetor,como
sefosseacolunadeumadeterminadatabelaquepossuiumtipodefinido,que
pudesseserpreenchidaporváriosvalores.
Adiferen çaentreumeoutroéqueosvetoressãodefinidosapenasem

## Página 361

CasadoCódigo
memória,bemcomoosdadosquesãoatribuídosaeles.Contudo,comoestão
emmemória,proporcionamumavelocidademaiordeacessoaosdados,ao
contráriodousodetabelas,noqualénecessário,namaioriadasvezes,acessá-
losfisicamentenodisco.
ParautilizarmosumaPL/SQLTable,temosqueprimeirodefini-lacomo
sefosseumtipodedadosendocriado,chamadode type. Issodeveser
feitonaáreadedeclaraç ão( declare)doblocoPL/SQL,sendoumbloco
anônimoouatravésdeuma procedure, functionou package. Após
adefiniçãodo typePL/SQLTable,énecessáriodeclararumavariávelque
utilizaráestadefinição.Valesalientarqueinicialmenteadefiniç ãodo type
nãoocupaespaçonamemória,apenasquandodeclaramosumavariávelcom
baseneste typeéqueistoacontece.
Vejaoexemploaseguir.
SQL> declare
2 --
3 type deptnotab is table of number index by binary_integer;
4 type dnametab is table of dept.dname%type index by
binary_integer;
5 type loctab is table of varchar2(200) index by
binary_integer;
6 --
7 wdeptnotab deptnotab;
8 wdnametab dnametab;
9 wloctab loctab;
10 --
11 idx binary_integer default 0;
12 begin
13 --
14 for r1 in (select deptno, dname, loc from dept) loop
15 idx := idx + 1;
16 wdeptnotab(idx) := r1.deptno;
17 wdnametab(idx) := r1.dname;
18 wloctab(idx) := r1.loc;
19 end loop;
20 --
21 for i in 1..wdeptnotab.last loop
22 dbms_output.put_line('Departamento: '||wdeptnotab(i)||
350

## Página 362

CasadoCódigo Capítulo20. PL/SQLTables(estruturashomogêneas)
23 ' - '||wdnametab(i)||
24 ' - Local: '||wloctab(i));
25 end loop;
26 end;
27 /
Departamento: 10 - ACCOUNTING - Local: FLORIDA
Departamento: 30 - SALES - Local: CHICAGO
Departamento: 40 - OPERATIONS - Local: BOSTON
Departamento: 80 - S& E - Local:
Departamento: 90 - FINANCIAL - Local:
Departamento: 99 - RH - Local: ARGENTINA
Departamento: 88 - RH - Local: ARGENTINA
Departamento: 41 - GENERAL LEDGER - Local:
Departamento: 42 - PURCHASING - Local:
Procedimento PL/SQL concluído com sucesso.
SQL>
Poisbem,oexemploanteriorémuitosimples.Eleselecionadadosdata-
bela dept.Ainten çãoaquinãoémostrarexemploscomplexosquedificul-
temoentendimentodoassunto.Pelocontrário,utilizamosexemplossimples,
focandonospontosquedevemosaprender.Destaforma,analisandoopro-
grama,temosnaslinhas3a4,trêsdefiniçõesdetabelaPL/SQL.Adefiniç ão
deumatabelaPL/SQLdeveiniciarpelocomando typeseguidodonome
dotipoquequeremoscriar. Porexemplo,nalinha3,criamoscomonome
deptnotab.
Logoapósonome,colocamosaexpressão is table of,quevainos
indicardequetiposeránossaPL/SQLTable,quenestecasodefinimosqueé
dotipo number.Depoisdeinformarmosotipo,devemosutilizaracláusula
index by binary_integer,queéumacláusulapadrãoparaacriaç ãode
PL/SQLTables. Elatemaavercomotipodeindexaç ão(nocaso,binária)
usadaparaacriaç ãodatabelaeacessoaosdadosnamemória.
Aslinhas4e5seguemomesmoformatodedefiniç ão,sendoqueumafoi
definidacomomesmotipodacoluna deptnodatabela depteaoutracom
otipo varchar2(200).Vejaque,nesseexemplo,adefiniç ãodo typeda
351

## Página 363

CasadoCódigo
tabelaPL/SQLéparecidacomasdefiniçõesusadasemvariáveis.
Naslinhas7a8,estãodeclaradasvariáveisdostiposcriadosnaslinhas3a
5,ouseja,variáveisdefinidascomotipoPL/SQLTable.Sãoestas,asvariáveis
queserãomanipuladasemnossoprograma. Naslinhas14a19,temosum
cursor for loop quelêtodasasinformaçõesdatabela depteasarmazena
emnossastabelasPL/SQL.
Umaobservaçãoimportanteéque,emboranesteexemplotenhasidocri-
adoum typedetabelaPL/SQLparacadainformaç ão(códigododepar-
tamento,nomedodepartamentoelocalizaç ão)épossívelcriarumatabela
PL/SQLusando %rowtypereferenciandocursoresoutabelas.Nessescasos,
épossíveldefinirum typedetabelaPL/SQLconstituídoporváriosarrays,
oumelhor,campos,paraumaúnicaPL/SQLTable.
Noteque,dessaforma,atabelaPL/SQLficarálimitadaàdefiniç ãodata-
belaoucursorutilizadosnadeclaraç ão. Contudo,nestecapítulo,estamos
falandodevetores,ouseja,estruturashomogêneasdedados. Assimsendo,
comonesseexemploforamrecuperadosdadosreferentesatrêscolunasda
tabela dept,foiprecisodefinirtrêstabelasPL/SQLparaguardá-los,eassim
mantermososconceitosreferentesavetores.
Continuando,conformepodeservistonaslinhas16a18,aformadearma-
zenamentoprecisaserdotipoindexadaparaquepossamosnavegarentreas
posiçõesdatabelaPL/SQL.Paraisso,criamosumavariávelchamada idxque
seráalimentadadentrodo loopeservirácomoíndicedenavegaç ãodentro
dasnossasPL/SQLTables.Paraarmazenardeterminadovalor,informamos
onomedatabelaPL/SQLseguidodoindexadorentreparênteses,conforme
pôdeservistonoexemplo(linhas16a18).
Seguindooexemplo,utilizamosoutro for loop quelênossastabelas
PL/SQLeimprimeosvaloresnatela(linhas21a25).Algumasfun çõesestão
disponíveisparao typePL/SQLTable.Umadelaséafun ção lastquere-
tornaoúltimoregistropreenchidonoarray.Tambémtemosafun ção count
queretornaaquantidadederegistroscontidosnatabela.Noexemplo,foiuti-
lizadaafun ção lastparaindicaraposiç ãofinaldo for loop,ouseja,ele
devevarreratabelaPL/SQLdaposiç ão1atéaúltimaposiç ãodela.
Reparequeusamosopróprioindexadordo for loop (i) paranave-
garpelosvaloresdastabelas,gravadosanteriormente. Comonossastabelas
352

## Página 364

CasadoCódigo Capítulo20. PL/SQLTables(estruturashomogêneas)
forampreenchidasutilizandoomesmo for loop,ouseja,todaspossuindo
amesmaquantidadederegistros,nósutilizamosapenasumadelasparaser-
vircomobaseparasabermosaquantidadeexataquedeveserlidapelocursor
for loop.Noentanto,atravésdoindexador (i)docursor,todososregis-
trosdetodasastabelasforamlidoseutilizadosnageraç ãodasaídafeitapelo
dbms_output.
Vejaafiguraaseguirparamelhorentendimentodecomoérealizadaa
gravaçãoeleituradosdados,usandocomobaseoprogramadoexemplo.
Cursor:gravaçãodatabelaPL/SQL
Fig.20.1:Esquemadegravaç ãodeumaPL/SQLTable
Cursor:leituradatabelaPL/SQL
353

## Página 365

CasadoCódigo
Fig.20.2:EsquemadeleituradeumaPL/SQLTable
Paraconcluir,seguemdoisexemplosondeforamdefinidasPL/SQLTables
combaseemtabelasecursores.
Exemploutilizandocursor:
SQL> declare
2 --
3 cursor c1 is
4 select d.department_id
5 ,department_name
6 ,first_name
7 ,hire_date
8 ,salary
9 from departments d
10 ,employees e
11 where d.manager_id = e.employee_id
12 order by department_name;
354

## Página 366

CasadoCódigo Capítulo20. PL/SQLTables(estruturashomogêneas)
13 --
14 type tab is table of c1%rowtype index by binary_integer;
15 --
16 tbgerente tab;
17 n number;
18 --
19 begin
20 for r1 in c1 loop
21 tbgerente(r1.department_id) := r1;
22 end loop;
23 --
24 n := tbgerente.first;
25 --
26 while n <= tbgerente.last loop
27 dbms_output.put_line(
'Depto: '||tbgerente(n).department_name||' '||
28 'Gerente: '||tbgerente(n).first_name||' '||
29 'Dt. Admi.: '||tbgerente(n).hire_date||' '||
30 'Sal.: '||to_char(tbgerente(n).salary,
'fm$999g999g990d00'));
31 n := tbgerente.next(n);
32 end loop;
33 end;
34 /
Depto: Administration Gerente: Jennifer Dt. Admi.: 17/09/97
Sal.: $4.400,00
Depto: Marketing Gerente: Michael Dt. Admi.: 17/02/06
Sal.: $13.000, 00
Depto: Purchasing Gerente: Den Dt. Admi.: 07/12/04
Sal.: $11.000, 00
Depto: Human Resources Gerente: Susan Dt. Admi.: 07/06/04
Sal.: $6.500,00
Depto: Shipping Gerente: Adam Dt. Admi.: 10/04/07
Sal.: $8.200,00
Depto: IT Gerente: Alexander Dt. Admi.: 03/01/00 Sal.: $9.000,00
Depto: Public Relations Gerente: Hermann Dt. Admi.: 07/06/04
Sal.: $10.000, 00
Depto: Sales Gerente: John Dt. Admi.: 01/10/06 Sal.: $14.000,00
Depto: Executive Gerente: Steven Dt. Admi.: 17/06/97
355

## Página 367

CasadoCódigo
Sal.: $24.000,00
Depto: Finance Gerente: Nancy Dt. Admi.: 17/08/04
Sal.: $12.000,00
Depto: Accounting Gerente: Shelley Dt. Admi.: 07/06/04
Sal.: $12.000,00
Procedimento PL /SQL concluído com sucesso.
SQL>
Noexemploanterior,temosumprogramaquelêasinformaçõesdede-
partamentoeseusgerentes. Paratal,criamosumcursor(linhas3a12)que
buscacadadepartamentocadastradonatabela departmentsquepossua
gerenteassociadonatabela employees. Sãotrazidaspelocursorasinfor-
mações:códigododepartamento,nomedodepartamento,primeironomedo
gerentedodepartamento,datadeadmissãoesaláriodogerente.
Nalinha14,definimosum typePL/SQLTablechamado tabeatribuí-
mosaeleotipo c1%rowtype.Estetipoconsisteemmontaramesmaestru-
turadocursor c1paraotipo tab,ouseja,serãocriadosparaaPL/SQLTable
osseguintesarrays: department_id, department_name, first_name,
hire_datee salary.
Naslinhas20a22,encontra-seaaberturadocursoreatribuiç ãodosresul-
tadosdomesmoparaatabelaPL/SQL tbgerente,quefoideclaradacomo
sendodotipo tabnalinha16doprograma.Notequeusamoscomoindexa-
doroprópriovalordocampo department_id,sendoqueeleéúnicopara
cadalinha. Vejatambém,queatribuímosàPL/SQLTableoarray r1. r1
possuiosdadosdetodasascolunasdocursor. Logo,nossatabelaPL/SQL
recebetodosestesvalores,respeitandoaestruturadefinida.
Nalinha24,temosousodafun ção firstindicandoquequeremosque
oponteiro,queindicaaposiç ãoemqueofocoseencontranaPL/SQLTable,
volteparaaprimeiraposiç ão.Sóparaentendimento,cadavezqueumdado
écarregadoemumalinhadaPL/SQLTable,ofocopermanecenestalinha.
EsteretornoparaaprimeiralinhadatabelaPL/SQLtemavercomo loop
whilequetemosentreaslinhas26a32.Noexemplo,como for loop,nós
utilizamosaprópriaestruturaderepetiç ãoparacontrolarafaixadeinícioe
fimdaslinhas.
356

## Página 368

CasadoCódigo Capítulo20. PL/SQLTables(estruturashomogêneas)
Comoagoraestamosutilizandoo while,nósprecisamoscontrolarisso.
Paratanto,testamosavariável N,querecebeaprimeiraposiç ãodoarrayna
linha24.Logo,estamossolicitandoqueaestrutura whilefiqueemloopen-
quantonãochegaraúltimalinhadoarray.Ocomandoutilizaafun ção last
databelaPL/SQL.Vejatambémque,nalinha31,utilizamosafun ção next
parafazercomqueoponteirováparaapróximalinhadatabela,fazendo
sucessivamentecomquetodasaslinhassejamvarridas.
Exemploutilizandotabela( %rowtype):
SQL> declare
2 --
3 type deptab is table of dept%rowtype index by
binary_integer;
4 --
5 wdeptab deptab;
6 --
7 idx binary_integer default 0;
8 begin
9 --
10 for r1 in (select * from dept) loop
11 idx := idx + 1;
12 wdeptab(idx) := r1;
13 end loop;
14 --
15 for i in 1..wdeptab.last loop
16 dbms_output.put_line(
'Departamento: '||wdeptab(i).deptno||
17 ' - '||wdeptab(i).dname||
18 ' - Local: '||wdeptab(i).loc);
19 end loop;
20 end;
21 /
Departamento: 10 - ACCOUNTING - Local: FLORIDA
Departamento: 30 - SALES - Local: CHICAGO
Departamento: 40 - OPERATIONS - Local: BOSTON
Departamento: 80 - S& E - Local:
Departamento: 90 - FINANCIAL - Local:
Departamento: 99 - RH - Local: ARGENTINA
357

## Página 369

CasadoCódigo
Departamento: 88 - RH - Local : ARGENTINA
Departamento: 41 - GENERAL LEDGER - Local:
Departamento: 42 - PURCHASING - Local:
Procedimento PL /SQL concluído com sucesso.
SQL>
Esseexemploémuitosemelhanteaosdemais.Aúnicadiferen çaéaforma
comofoicriadoo typePL/SQLTable.Notequeatabelafoidefinidacomo
tendoamesmaestruturadatabela dept.Logo,estamoscriandoemmemória
amesmaestruturada deptqueexistefisicamentenobancodedados.
358

## Página 370

Capítulo21
PL/SQLRecords(estruturas
heterogêneas)
VimosqueemPL/SQLTabletrabalhamoscomdadosintrínsecosatravésdas
estruturashomogêneas.EmPL/SQLRecords,vamostrabalharcomestrutu-
rasheterogêneas.ComPL/SQLTable,estávamoslimitadosacriar typesTa-
bleconstituídasapenasdeumtipodedado(numérico,caractereoudata),ou
utilizandotabelasecursores,onde,embora,tivéssemosvárioscamposcom
tiposdedadosdiferentes,cadaqualpossuíaseustiposjádefinidos,sema
possibilidadedealterarmosconformeanecessidade.
ComorecursodePL/SQLRecords,podemosdefinirtiposeestruturasde
dadosdistintasdentrodeummesmo type,semprecisarcriarvários types
paracadaum,ousemnecessitarassociá-losatabelasoucursores.
Vejaoexemploaseguir:

## Página 371

CasadoCódigo
SQL> declare
2 --
3 type deprec is record ( deptno number(2,0 )
4 ,dname varchar2(14)
5 ,loc varchar2(13));
6 --
7 wdeprec deprec;
8 --
9 begin
10 --
11 select *
12 into wdeprec
13 from dept
14 where deptno = 10;
15 --
16 dbms_output.put_line('Departamento: '||wdeprec.deptno||
17 ' - '||wdeprec.dname||
18 ' - Local: '||wdeprec.loc);
19 end;
20 /
Departamento: 10 - ACCOUNTING - Local: FLORIDA
Procedimento PL /SQL concluído com sucesso.
SQL>
Nesseexemplo,come çamospelacria ção,linha3,ondeinformamosaex-
pressão typeseguidapelonome, deprec.Logoapós,informamosotipo
do type, is record,queodefinecomoPL/SQLRecord.Apósisto,entre
parênteses,informamosqualaestruturaqueeste typeterá.Aqui,definimos
queeleseráconstituídoportrêscampos, deptno, dnamee loc. Desta
forma,nosépermitido,atravésdeste type,definirquantoscamposquiser-
moseutilizartiposdiferentesparaeles,possibilitandocriarumaestrutura
heterogênea.
Valesalientarque,emboraosnomesdoscampossejamsemelhantesaos
databela deptexistentenobancodedados,elesnãoestãoreferenciando-
os.Aquipoderíamoscolocarqualquernome,respeitandoapenasasmesmas
regrasparadefiniçãodevariáveis.
360

## Página 372

CasadoCódigo Capítulo21. PL/SQLRecords(estruturasheterogêneas)
Depoisdacriaçãodo type,declaramosumavariávelchamada wdeprec
queserádefinidacomestetipo(linha7).Naslinhas11a14,estamosselecio-
nandoosdadosdatabela deptcujodepartamentosejaiguala10.Estamos
utilizandoacláusula into,ondeosdadosvindosdo selectestãosendo
atribuídosaonossoPL/SQLRecord. Naslinhas16a18,temosaimpressão
doresultadocontidoemnosso typeRecord.Vejaaimagemaseguir,onde
émostradadeformasimbólicaadefiniç ãoearmazenamentodosdadosem
memórianoPL/SQLRecord.
Fig.21.1:Esquemadegravaç ãodeumPL/SQLRecord
Vocêdeveternotadoquenãoutilizamosestruturasderepetiç ãoeque,
aocontráriodisto,nossoexemplotrouxeapenasumalinhaderegistro.Pois
bem,umacaracterísticado typeRecordéqueeleporsisópodeguardar
apenasumregistroporvez,aocontráriodo typeTable,noqualpodemos
inserirváriaslinhas.
Destaforma,namaioriadasvezesvemosos typesRecordsendoutili-
zadosemconjuntocomos typesTable,sendoqueesteúltimonospermite
gravarváriaslinhas.Vamosutilizaroexemploanterior,agora,trazendotodos
osdadosdatabela depteusandoorecursode typeTablejuntamentecom
o typeRecord.
361

## Página 373

CasadoCódigo
SQL> declare
2 --
3 type deprec is record ( deptno number(2,0 )
4 ,dname varchar2(14)
5 ,loc varchar2(13));
6 --
7 type deptab is table of deprec index by binary_integer;
8 --
9 wdeptab deptab;
10 idx binary_integer default 0;
11 --
12 begin
13 --
14 for r1 in (select * from dept) loop
15 --
16 idx := idx + 1;
17 wdeptab(idx) := r1;
18 --
19 end loop;
20 --
21 for i in 1 ..wdeptab.last loop
22 dbms_output.put_line(
'Departamento: '||wdeptab(i).deptno||
23 ' - '||wdeptab(i).dname||
24 ' - Local: '||wdeptab(i).loc);
25 end loop;
26 end;
27 /
Departamento: 10 - ACCOUNTING - Local: FLORIDA
Departamento: 30 - SALES - Local: CHICAGO
Departamento: 40 - OPERATIONS - Local: BOSTON
Departamento: 80 - S&E - Local:
Departamento: 90 - FINANCIAL - Local:
Departamento: 99 - RH - Local : ARGENTINA
Departamento: 88 - RH - Local : ARGENTINA
Departamento: 41 - GENERAL LEDGER - Local:
Departamento: 42 - PURCHASING - Local:
Procedimento PL /SQL concluído com sucesso.
362

## Página 374

CasadoCódigo Capítulo21. PL/SQLRecords(estruturasheterogêneas)
SQL>
Conformemencionado,nesteexemploempregamosousodedoisrecur-
sosemummesmoprograma,paraquepudéssemosdefinirumaestrutura
heterogêneaepoderarmazenarmaisdeumregistroemmemória.
Valesalientarqueos typeTableseRecordspodemguardarqualquertipo
dedados,nãonecessariamente,dadosvindosdetabelasdobancodedados.
Podemosgerareprocessardadosdentrodeumprogramaeiralimentando
dentrodestesobjetossemteranecessidadedevarrerdadosqueestãoarma-
zenadosemtabelas,porexemplo.
Mas,voltandoaoexemplo,vemosquenaslinhas3a5,estácriadoo type
Record deprec,igualmenteaoexemploanterior. Jánalinha7temosum
typeTablecriadocombaseno typeRecord deprec.Dessaforma,épos-
síveltermosregistrosemformadetabela,podendoarmazenarmaisdeuma
linhanaPL/SQLTable,conformeaestruturadoPL/SQLRecordcriado.Veja
aseguiraimagemrepresentativadousodestesrecursosjuntos.
363

## Página 375

CasadoCódigo
Fig.21.2:EsquemadousocombinadodePL/SQLTableePL/SQLRecord
Ficouvistoqueaformadedefiniç ãoemanipulaç ãodos typeTablese
Recordsébastantesemelhante. Oentendimentodosconceitosapresentado
nocapítuloreferenteaPL/SQLTablessefaznecessárioparacompreender
todoocontextoapresentadonestesdoiscapítulos.Nomais,salientamosque
ousodestesrecursospodeajudaremuitonamanipulaç ãodosdados,princi-
palmente,emgrandesvolumes,quandoodesempenhopodeserprejudicado,
devidoamuitosacessosaredeouaodisconabuscapelasinformações.
364

## Página 376

Capítulo22
Pacoteutl_file
UmrecursobeminteressanteemuitoutilizadoemPL/SQLéaleituraees-
critadearquivos.Emmuitasempresasaexportaç ãoeimportaç ãodearquivos
sãomuitoutilizadasparaalimentarsistemasparalelos(tambémchamadosde
sistemassatélites)ouparagerarinformaçõesgerenciais. Apossibilidadede
extrairinformaçõesdosistemaetrabalhá-lasusandoferramentasespecíficas
paraanáliseéumapráticamuitocomum.
Para este trabalho existe um pacote dentro do Oracle chamado
utl_file. Estepacotetrabalhacomrecursosquepossibilitaacomunica-
çãoentreobancodedadosOracleeosistemaoperacional,fazendocomque
consigamoslerougerararquivosexternamenteaobancodedados.
Estepacotepossuiumasériedefun çõeseprocedimentosquesãoutiliza-
dosdentrodosblocosPL/SQLparaageraç ãoouleituradedados.Deforma
bemestruturadaeclara,épossívelnãosólerasinformaçõescomotambém

## Página 377

CasadoCódigo
trabalharcomelas,alterando-aseformatando-asantesdeinseri-lasemtabe-
lasougravá-lasemarquivo.
Algumaspremissasdevemserobservadasantesdeutilizaresterecurso.A
primeiradelaséterprivilégioparaexecutaropacote utl_file.Asegunda
premissafazreferênciaacomoo utl_filefazacomunicaçãoentreobanco
dedadoseosistemaoperacional,paraobteracessoaosdiretóriosdoservidor
ondeserãogravadosoulidososarquivoscomosdados.
ObancodedadosOraclepossuiumasériedeparametrizaçõesquega-
ranteseufuncionamento. Estesparâmetrospodemservisualizadosatravés
daview v$parameter. Estaviewlistatodososparâmetrosdobancode
dadosOracle.Umdestesparâmetrosé utl_file_dir,responsávelporin-
formarao utl_fileaquaisdiretórioseletemacessonoservidor.Apartir
daí,opacote utl_filesóteráacessoemgravarelerarquivosnestesdi-
retórios.Essesdiretóriosnãonecessitamestarnomesmoservidordobanco
dedados,entretanto,atravésdealgumcompartilhamento,osdoisprecisam
enxergarumaooutro.
Asop çõesdeconfiguraç ãodesteparâmetrosão:
•utl_file_dir=C:\sistema\ERP:indica umdiretórioespecífico
paraagravaç ãoeleituradearquivos(compatívelcomsistemaWin-
dows).
•utl_file_dir=/ora/dat: indica um diretório específico para a
gravaçãoeleituradearquivos(compatívelcomsistemaUnix).
•utl_file_dir=C:\sistema\ERP, /ora/dat:indicaváriosdire-
tórios,separadosporvírgula,paraagravaç ãoeleituradearquivos.
•utl_file_dir=* :indicaqueagravaç ãoouleituradearquivospode
serrealizadaemtodososdiretóriosdisponíveisnoservidor.
Nota:mesmoqueosdiretóriosjáestejamdevidamenteconfigurados
paraoparâmetro utl_file_dir,aspermissõesdeacessoaosdiretó-
riosnoníveldeservidortambémprecisamserrealizadas.
366

## Página 378

CasadoCódigo Capítulo22. Pacoteutl_file
Contudo,estaconfiguraç ãoemníveldeparâmetrodebancodedados
émeioinconveniente, poisoDBAparaalterarestadefiniç ãoprecisapa-
rarobancodedadospararealizá-la. Nemtodososparâmetrosdobanco
dedadosOraclenecessitamumaparadadosistema,masparaoparâmetro
utl_file_diréobrigatórioqueistosejafeito.Cadavezqueo utl_file
necessitaacessarumdiretóriodiferenteénecessáriorealizartodoestetraba-
lho.
Paraevitaristo,apartirdeversõesmaisnovasdobancodedadosaOracle
disponibilizouumrecursochamado directorycomoqualépossívelcriar
umobjetonobancodedadoseapontá-loparaumdiretóriodoservidor,sem
anecessidadedealterarmosissoviaparâmetrodebanco.Comisto,otrabalho
ficoumuitomaissimples,inclusive,nãoexigeconhecimentosespecíficosde
DBA.
Destaforma, antesdetudo, vamosaprendercomosecriaumobjeto
directory,parautilizarmosemnossaaplicaç ão utl_file.
SQL> create directory dir_principal as 'C:\tmp\arquivos';
Diretório criado.
SQL>
Usamos o comandocreate directory para criar um objeto que
aponteparaodiretórioondequeremosgravaroulerdeterminadosarqui-
vos. Emseguida,informamosumnomeparaoobjeto. Esteéonomeque
seráutilizadodentrodosnossosprogramas.Seguindoaexpressão asvemo
caminhoreferenteaodiretório.Paranossosexemplosusaremosesterecurso.
Alémdecriamosoobjeto,precisamosdarprivilégiosdeacessoaosusuá-
riosdobancodedados.Casoqueriadisponibilizaracessoparatodososusuá-
riosdobanco,dêprivilégiosatravésdousuário public.
SQL> grant read, write on directory dir_principal to TSQL;
Concessão bem- sucedida.
SQL>
367

## Página 379

CasadoCódigo
Atenção: paradaracessoaoobjeto directory,énecessárioestar
conectadocomousuário system,queéousuárioadministradordo
bancodedadosOracle.
Paraverosobjetos directorycadastrados,useocomando select:
SQL> select *
2 from all_directories
3 where directory_name = 'DIR_PRINCIPAL';
OWNER DIRECTORY_NAME DIRECTORY_PATH
------- ----------------- -------------------------------
SYS DIR_PRINCIPAL C:\tmp\arquivos
SQL>
Paraalterarumobjeto directory,utilizamosocomando replace.
Atravésdelepodemosalterarocaminhododiretório.
SQL> create or replace directory dir_principal as 'C:\tmp\';
Diretório criado.
SQL>
Paradarprivilégiosdeexecuç ãodo utl_fileénecessárioestarconec-
tadocomousuário sys.
SQL> grant execute on UTL_FILE to TSQL;
Concessão bem-sucedida.
SQL>
Nota:paraconectarcomousuário sysutilizeocomando concc
sys/<senha>@<string_banco> as sysdba;.
368

## Página 380

CasadoCódigo Capítulo22. Pacoteutl_file
Muitobem. Agorajácriamosnosso directoryejáconcedemospri-
vilégioparaousuário. Vamoscolocaramãonamassa. Paratrabalharcom
arquivos,precisamosconhecerumpoucosobreasfun çõeseprocedimentos
quefazempartedestepacote.Alémdisso,precisamosconhecerasexce ções
quepodemsergeradasemcasodeerros.
Nasequência,vejafun çõeseprocedimentosnousodo utl_file.
fclose
Fechaoarquivo.Exemplo:
procedure fclose(file in out file_type);
Onde: fileéonomedoarquivolidoougerado.
fclose_all
Fechatodososarquivos.Exemplo:
procedure fclose_all;
Nestecasotodososarquivosabertoserãofechados.
fflush
Descarregatodososdadosembufferparaseremgravadosemdiscoime-
diatamente.Exemplo:
procedure fflush(file in file_type);
Onde: fileéonomedoarquivolidoougerado.
fopen
Abreoarquivo.Exemplo:
function fopen(location in varchar2,
filename in varchar2,
openmode in varchar2)
return file_type;%%
369

## Página 381

CasadoCódigo
Onde: locationéonomedodiretórioondeseencontraoarquivoou
ondeoarquivodevesergerado. filenameéonomedoarquivoaserlido
ougerado. openmodeindicaqualmododeveseraplicadonoarquivo. R=
Read(ler), W=Write(escrever)ou A=Append(adicionar).
function fopen(location in varchar2,
filename in varchar2,
openmode in varchar2,
max_linesize in binary_integer) return file_type;
Onde: locationéonomedodiretórioondeseencontraoarquivo
ouondeoarquivodevesergerado. filenamenomedoarquivoaserlido
ougerado. openmodeindicaqualmododeveseraplicadonoarquivo. R=
Read(ler), W=Write(escrever)ou A=Append(adicionar). max_linesize
permiteespecificarotamanhomáximodelinha.Ointervalopermitidoéde
1até32.767.Sevocêomitiresseparâmetro,opadrão1.023éusado.
get_line
Lêumalinhadeumarquivo.Exemplo:
procedure get_line(file in file_type,
buffer out varchar2);
Onde: fileéonomedoarquivoondealinhadeveserlida. bufferé
olugarondeoconteúdolidodalinhadeveserinserido.
is_open
Verificaseumarquivoestáaberto.Exemplo:
procedure is_open(file in file_type) return boolean;
Onde: fileéonomedoarquivoquedeveserverificado.
new_line
Gravaumcaractere newlineemumarquivo.Exemplo:
370

## Página 382

CasadoCódigo Capítulo22. Pacoteutl_file
procedure new_line(file in file_type,
lines in natural := 1);
Onde: fileéonomedoarquivoquedevereceberanovalinha. lines
éonúmerototaldecaracteres newlinequevocêquergravarnoarquivo. O
padrãoégravaruma newlinenova.Esteargumentoéopcional.
put
Gravaumastringdecaracteresemumarquivo,masnãocolocauma ne-
wlinedepoisdela.Exemplo:
procedure put(file in file_type,
buffer in varchar2);
Onde: fileéonomedoarquivoquedevereceberoconteúdo. buffer
éoconteúdoasergravadonoarquivo.
put_line
Gravaumalinhaemumarquivo.Exemplo:
procedure put_line(file in file_type,
buffer in varchar2);
Onde: fileéonomedoarquivoquedevereceberoconteúdo. buffer
contémotextoquevocêdesejagravarnoarquivo. Onúmeromáximode
caracteresquevocêpodegravarusandoumachamadaselimitaaotamanho
delinhaquevocêespecificounachamadade fopenetemcomopadrão1.023.
putf
Formataegravasaída. Essaéumaimitaç ãobrutadoprocedimento
PRINTF()doC.Exemplo:
procedure putf(file in file_type,
format in varchar2,
arg1 in varchar2 default null,
arg2 in varchar2 default null,
371

## Página 383

CasadoCódigo
arg3 in varchar2 default null,
arg4 in varchar2 default null,
arg5 in varchar2 default null);
Onde: fileéonomedoarquivoquereceberáoconteúdo. format
representaastringquevocêdesejagravarnoarquivo. arg1ao arg5são
argumentosopcionaiscontendoosvaloresquesãosubstituídosnastringde
formatoantesdelasergravadanoarquivo.
Exceções de fclose e fclose_all
•utl_file.invalid_filehandle: vocêpassouum handledear-
quivoquenãorepresentavaumarquivoaberto.
•utl_file.write_error:osistemaoperacionalnãopodegravarno
arquivo.
•utl_file.internal_error:umerrointernoocorreu.
Exceções de fopen
•utl_file.invalid_path:odiretórionãoéválido.Vocêdeveveri-
ficarem utl_file_dir.
•utl_file.invalid_mode: ummodoinválidofoiespecificado. O
modoopendeveser R, Wou A.
•utl_file.invalid_operation:oarquivonãopodeserabertopor
algumoutromotivo.VerifiqueseoproprietáriodosoftwaredoOracle
temacessoaodiretório(issopodeserumaquestãodepermissão)e
entreemcontatocomoadministradordoseubancodedadospara
obterajuda.
•utl_file.internal_error:umerrointernoocorreu.
372

## Página 384

CasadoCódigo Capítulo22. Pacoteutl_file
Exceções de get_line
•utl_file.invalid_filehandle: vocêpassouhandledearquivo
inválido.Possivelmentevocêesqueceudeabriroarquivoprimeiro.
•utl_file.invalid_operation:oarquivonãoestáabertoparalei-
tura(modo R),ouexistemproblemascomaspermissõesdearquivo.
•utl_file.value_error:obuffernãoésuficientementelongopara
conteralinhaqueestásendolidadoarquivo.Otamanhodobufferé
aumentado.
•utl_file.no_data_found:ofinaldoarquivofoiatingido.
•utl_file.internal_error: ocorreuumerrointernodosistema
utl_file.
•utl_file.read_error: ocorreuumerrodosistemaoperacional
durantealeituradoarquivo.
Exceções de put, put_line, putf e fflush
•utl_file.invalid_filehandle:vocêusouum handledearquivo
inválido. Essaexceçãopodeserlevantadaquandovocêesquecerde
abriroarquivo.
•utl_file.invalid_operation: você tentou gravar em um ar-
quivoquenãoestavaabertoparagravaç ão(modo Wou A).
•utl_file.write_error:ocorreuumerrodesistemaoperacional,
talcomoumerrodediscocheio,aotentargravaremumarquivo.
•utl_file.internal_error:ocorreuumerrointerno.
Agoravamosverumexemploondevamoslerosregistrosdatabela emp
e deptegerarumarquivoparasergravadonodiretóriodefinidoemnosso
directory.Vamosgravarasinformaçõesnoarquivodeformalinearese-
parandoasinformaçõesporpontoevírgula.
373

## Página 385

CasadoCódigo
SQL> declare
2 cursor c1 is
3 select a.deptno, dname, empno, ename
4 from dept a
5 ,emp b
6 where a.deptno = b.deptno
7 order by a.deptno;
8 r1 c1% rowtype;
9 --
10 meu_arquivo utl_file.file_type;
11 --
12 BEGIN
13 --
14 meu_arquivo := utl_file.fopen('DIR_PRINCIPAL',
'empregados.txt', 'w');
15 --
16 open c1;
17 --
18 loop
19 fetch c1 into r1;
20 exit when c1%notfound;
21 utl_file.put_line(meu_arquivo, r1.deptno||';'||
22 r1.dname||';'||
23 r1.empno||';'||
24 r1.ename);
25 end loop;
26 --
27 close c1;
28 --
29 utl_file.fclose(meu_arquivo);
30 --
31 exception
32 when utl_file.invalid_path then
33 utl_file.fclose(meu_arquivo);
34 dbms_output.put_line ('Caminho ou nome do arquivo
inválido');
35 when utl_file.invalid_mode then
36 utl_file.fclose(meu_arquivo);
37 dbms_output.put_line ('Modo de abertura inválido');
374

## Página 386

CasadoCódigo Capítulo22. Pacoteutl_file
38 end;
39 /
Procedimento PL/SQL concluído com sucesso.
SQL>
Analisandooprograma,vemosquenalinha10declaramosumavariável
dotipo utl_file.file_typequevaiseroponteiro(handle)paraonosso
arquivofísico.Quandoissoéfeito,oOraclemontaumaestruturadearquivo
emmemóriareferenteaoarquivofísicocomqueiremostrabalhar.Jánalinha
14,atribuímosàvariáveldeclaradaàaberturadoarquivopassandocomopa-
râmetroo directorycriadoanteriormente,quefazreferênciaaolocaldo
diretórioondeoarquivodevesergravado,onomedoarquivoe,porúltimo,
omodo,quenestecasoémododeescrita,representadopor W.Quandoexe-
cutamosum fopenutilizandoomodoescrita,casonãoexistaoarquivoele
ocria.
Nalinha21,utilizamosachamada put_lineparainserirlinhasaoar-
quivo. Nestecaso,estamosconcatenandoumasériedeinformaçõesvindas
dastabelas empe depteenviandoparaoarquivo.Apósoterminodalei-
turadastabelas,ouseja,nofinaldocursor,fechamosoarquivonalinha29.
Notequeentreaslinhas31a37estãotratadasaspossíveisexce çõesrelaciona-
dasaopacote utl_file.Segueoresultado:
375

## Página 387

CasadoCódigo
Fig.22.1:Arquivogeradoatravésdopacoteutl_file
Apóstermosvistooprogramaquegeraasinformaçõeseasjogaemum
arquivo,vamosveracontrapartidaondelemosoarquivogeradoemostramos
asinformaçõesnatela.
376

## Página 388

CasadoCódigo Capítulo22. Pacoteutl_file
SQL> declare
2 --
3 meu_arquivo utl_file.file_type;
4 linha varchar2(32000);
5 --
6 wdeptno emp.deptno%type;
7 wdname dept.dname%type;
8 wempno emp.empno%type;
9 wename emp.ename%type;
10 --
11 begin
12 --
13 meu_arquivo := utl_file.fopen('DIR_PRINCIPAL',
'empregados.txt', 'r');
14 --
15 loop
16 --
17 utl_file.get_line(meu_arquivo,linha);
18 --
19 exit when linha is null;
20 --
21 wdeptno :=
rtrim(substr(linha,1,(instr(linha,';',1,1) -1)));
22
23 wdname :=
rtrim(substr(linha,(instr(linha,';',1,1) + 1)
24 ,(instr(linha,';' ,1,2) -1) -
25 (instr(linha,';',1, 1) + (1 -1))));
26
27 wempno :=
rtrim(substr(linha,(instr(linha,';',1,2) + 1)
28 ,(instr(linha,';' ,1,3) -1) -
29 (instr(linha,';',1, 2) + (1 -1))));
30
31 wename := rtrim(rtrim(substr(linha,(
instr(linha,';',1,3) + 1)),chr(13)));
32 --
33 dbms_output.put_line('Cód. Departamento: '||wdeptno);
34 dbms_output.put_line('Nome Departamento: '||wdname);
377

## Página 389

CasadoCódigo
35 dbms_output.put_line('Cód. Empregado: '||wempno);
36 dbms_output.put_line('Nome Empregado: '||wename);
37 dbms_output.put_line('_');
38 --
39 end loop;
40 --
41 utl_file.fclose(meu_arquivo);
42 --
43 exception
44 when no_data_found then
45 utl_file.fclose(meu_arquivo);
46 dbms_output.put_line ('Final do Arquivo.');
47 when utl_file.invalid_path then
48 utl_file.fclose(meu_arquivo);
49 dbms_output.put_line ('Caminho ou nome do arquivo
inválido');
50 when utl_file.invalid_mode then
51 utl_file.fclose(meu_arquivo);
52 dbms_output.put_line ('Modo de abertura inválido');
53 end;
54 /
Vamosanalisarocódigodoprograma. Nalinha3,declaramosumava-
riáveldotipo utl_file.file_typequevaiseroponteiroparaonosso
arquivofísico.Nalinhacriamosumavariávelchamada linhaquereceberá
osdadosdecadalinhavindadoarquivo.Abrimosoarquivoatravésdafun ção
fopenutilizandoomodo R(leitura).Jánalinha17,utilizamosachamadade
procedimento get_linesquelêumalinha(aprimeira)doarquivoeguarda
seuvalordentrodavariável linha.Nestecaso,elebuscatodooconteúdoda
linhaejogadentrodavariável,ouseja,todososvaloresdalinhaconcatenados
porpontoevírgula.
Nalinha19,temososeguintecódigo exit when linha is null.
Conformevistonasexce ções,vimosqueaochegaraofinaldeumarquivo
aexce ção no_data_foundéacionada,ouseja,quandonãohouvermais
linhasparaler,égeradaumaexce çãoinformandoquenãohámaislinhas
paraseremlidasnoarquivo. Contudo,dependendoosistemaoperacional
e/oudacodificaç ãodoarquivogerado,podeacontecer,nocasodetermos
378

## Página 390

CasadoCódigo Capítulo22. Pacoteutl_file
umcaractere enternofinaldoarquivo,deo utl_filelerestecaractere
econsiderá-locomoumalinha. Casooprogramanãoestejatratandoesta
situação,errospodemocorrer.
Destaforma,alinha19serveparatratarestetipodesituaç ão. Casoa
exceção no_data_foundnãoforacionada,estacláusulagaranteasaídado
loop.Masaten ção:issoserveparaarquivosquenãoestejamconsiderando
linhasembrancoemsuaestrutura. Casolinhasembrancofaç amparteda
formataçãodosdados,estalinhanãodevesercolocada. Depois,naslinhas
21a31utilizamosasfun ções substre instrparasepararosdados,tendo
comobaseocaracterepontoevírgula. Finalizamosaleituradoarquivona
linha41.Notequenesteexemplotratamosaexce ção no_data_found,na
linha44.
Vejaoresultado.
Cód. Departamento: 10
Nome Departamento: ACCOUNTING
Cód. Empregado: 7782
Nome Empregado: CLARK
_
Cód. Departamento: 10
Nome Departamento: ACCOUNTING
Cód. Empregado: 7934
Nome Empregado: MILLER
_
Cód. Departamento: 10
Nome Departamento: ACCOUNTING
Cód. Empregado: 7839
Nome Empregado: KING
_
Cód. Departamento: 30
Nome Departamento: SALES
Cód. Empregado: 7698
Nome Empregado: BLAKE
_
Cód. Departamento: 30
Nome Departamento: SALES
Cód. Empregado: 7935
Nome Empregado: PAUL
379

## Página 391

CasadoCódigo
_
Cód. Departamento: 30
Nome Departamento: SALES
Cód. Empregado: 7900
Nome Empregado: JAMES
_
Cód. Departamento: 30
Nome Departamento: SALES
Cód. Empregado: 7844
Nome Empregado: TURNER
_
Cód. Departamento: 30
Nome Departamento: SALES
Cód. Empregado: 7654
Nome Empregado: MARTIN
_
Cód. Departamento: 30
Nome Departamento: SALES
Cód. Empregado: 7521
Nome Empregado: WARD
_
Cód. Departamento: 30
Nome Departamento: SALES
Cód. Empregado: 7499
Nome Empregado: ALLEN
_
Final do Arquivo.
Procedimento PL/SQL concluído com sucesso.
SQL>
Porcuriosidade,vamosapresentaromesmoexemplodegeraç ãoeleitura
dearquivoutilizandoaseparaç ãodeinformaç ãonãoporpontoevírgula,mas
sim,pornúmerodecaracteresfixos.Estemétodovisatermosnúmerofixos
paraotamanhodascolunas. Valelembrarquenãomudaemnadaaforma
deutilizaropacote utl_file.Éapenasparamostrarumaformadiferente,
porémmuitoutilizada,degerarlayoutsdiferentesparaarquivostextos
380

## Página 392

CasadoCódigo Capítulo22. Pacoteutl_file
Geraçãodoarquivo:
SQL> declare
2 cursor c1 is
3 select a.deptno, dname, empno, ename
4 from dept a
5 ,emp b
6 where a.deptno = b.deptno
7 order by a.deptno;
8 r1 c1 %rowtype;
9 --
10 meu_arquivo utl_file.file_type;
11 --
12 BEGIN
13 --
14 meu_arquivo := utl_file.fopen('DIR_PRINCIPAL',
'empregados.txt', 'w');
15 --
16 open c1;
17 --
18 loop
19 fetch c1 into r1;
20 exit when c1%notfound;
21 utl_file.put_line(meu_arquivo, rpad(r1.deptno,2,' ') ||
22 rpad(r1.dname,14,' ') ||
23 rpad(r1.empno,4,' ') ||
24 rpad(r1.ename,10,' ')
25 );
26 end loop;
27 --
28 close c1;
29 --
30 utl_file.fclose(meu_arquivo);
31 --
32 exception
33 when utl_file.invalid_path then
34 utl_file.fclose(meu_arquivo);
35 dbms_output.put_line ('Caminho ou nome do arquivo
inválido');
381

## Página 393

CasadoCódigo
36 when utl_file.invalid_mode then
37 utl_file.fclose(meu_arquivo);
38 dbms_output.put_line ('Modo de abertura inválido');
39 end;
40 /
Procedimento PL /SQL concluído com sucesso.
SQL>
Leituradoarquivo:
SQL> declare
2 --
3 meu_arquivo utl_file.file_type;
4 linha varchar2(32000);
5 --
6 wdeptno emp.deptno%type;
7 wdname dept.dname%type;
8 wempno emp.empno%type;
9 wename emp.ename%type;
10 --
11 begin
12 --
13 meu_arquivo := utl_file.fopen('DIR_PRINCIPAL',
'empregados.txt', 'r');
14 --
15 loop
16 --
17 utl_file.get_line(meu_arquivo,linha);
18 --
19 exit when linha is null;
20 --
21 wdeptno := rtrim(ltrim(substr(linha,1,2)));
22 wdname := rtrim(ltrim(substr(linha,3,14)));
23 wempno := rtrim(ltrim(substr(linha,17,4)));
24 wename := rtrim(ltrim(substr(linha,21,10)));
25 --
26 dbms_output.put_line('Cód. Departamento: '||wdeptno);
27 dbms_output.put_line('Nome Departamento: '||wdname);
382

## Página 394

CasadoCódigo Capítulo22. Pacoteutl_file
28 dbms_output.put_line('Cód. Empregado: '||wempno);
29 dbms_output.put_line('Nome Empregado: '||wename);
30 dbms_output.put_line('_');
31 --
32 end loop;
33 --
34 utl_file.fclose(meu_arquivo);
35 --
36 exception
37 when no_data_found then
38 utl_file.fclose(meu_arquivo);
39 dbms_output.put_line ('Final do Arquivo.');
40 when utl_file.invalid_path then
41 utl_file.fclose(meu_arquivo);
42 dbms_output.put_line (
'Caminho ou nome do arquivo inválido');
43 when utl_file.invalid_mode then
44 utl_file.fclose(meu_arquivo);
45 dbms_output.put_line ('Modo de abertura inválido');
46 end;
47 /
Cód. Departamento: 10
Nome Departamento: ACCOUNTING
Cód. Empregado: 7782
Nome Empregado: CLARK
....
_
Final do Arquivo.
Procedimento PL/SQL concluído com sucesso.
SQL>
Conformepôdeservistonesseexemplo,aleituratomacomobase,po-
siçõesfixasqueindicamalocalizaç ãoexatadecadainformaç ãonalinha,
extraindo-as.
383

## Página 396

Capítulo23
SQLdinâmico
Namaioriadasvezes,trabalharemoscomcomandosSQLpreviamentedefi-
nidosdentrodenossosprogramas.Geralmente,ocorpodoscomandosnão
sealtera,apenasosparâmetrosquepassamosaeles.Podemosteromesmo
comandoSQLdiversasvezesdentrodonossoprograma,masmedianteapas-
sagemdeparâmetroscomvaloresdistintospodemosterresultadosdiferentes.
Contudo,podeacontecerde,dependendodasituaç ão,nãotermosestes
comandosSQLdefinidos,ouseja,mediantedeterminadasaçõestalvezpreci-
semosmodificaraestruturadocomandoSQLparaatenderasnecessidades,
mascomumdetalhe:tudoissoemtempodeexecuç ão.
Paraisso,alinguagemPL/SQLdisponibilizaumrecursochamadode SQL
dinâmicoquenosdáapossibilidadedeexecutarumcomandoSQLapartirde
umastring,ouseja,ocomandopassaaserumastringdecaracteresarmaze-
nadosemumavariável.Atravésdeumcomando,avariávelélidaeoSQLque
estádentrodelaéexecutado.Issoéfeitoatravésdoprocedimento execute

## Página 397

CasadoCódigo
immediate.Pormeiodesteprocedimento,podemosexecutarcomandosde
insert, delete, update, select, create, alter, drop,bemcomo
executarprocedimentosefun ções.Épossíveltambémrealizarpassagemde
parâmetrosparaessescomandos.Vejaosexemplosaseguir.
Usocom insert:
SQL> declare
2 --
3 winsert_emp varchar2(4000) default null;
4 winsert_dept varchar2(4000) default null;
5 --
6 wempno emp.empno%type;
7 wename emp.ename%type;
8 wjob emp.job%type;
9 wmgr emp.mgr%type;
10 whiredate emp.hiredate%type;
11 wsal emp.sal%type;
12 wcomm emp.comm% type;
13 wdeptno emp.deptno%type;
14 --
15 begin
16 --
17 wempno := 9999;
18 wename := 'BONO' ;
19 wjob := 'SALESMAN';
20 wmgr := 7698;
21 whiredate := SYSDATE;
22 wsal := 1000;
23 wcomm := 0;
24 wdeptno := 30;
25 --
26 winsert_emp := 'insert into emp ( empno
27 ,ename
28 ,job
29 ,mgr
30 ,hiredate
31 ,sal
32 ,comm
33 ,deptno)
386

## Página 398

CasadoCódigo Capítulo23. SQLdinâmico
34 values ( :empno
35 ,:ename
36 ,:job
37 ,:mgr
38 ,:hiredate
39 ,:sal
40 ,:comm
41 ,:deptno)';
42 --
43 execute immediate winsert_emp using wempno
44 ,wename
45 ,wjob
46 ,wmgr
47 ,whiredate
48 ,wsal
49 ,wcomm
50 ,wdeptno;
51 --
52 winsert_dept :=
'insert into dept values (:deptno, :dname, :loc)';
53 --
54 execute immediate winsert_dept using 99, 'RH', 'BRASIL';
55 --
56 end;
57 /
Procedimento PL/SQL concluído com sucesso.
SQL>
Nesteexemplo,nalinha26,temosavariável winsert_empquerecebe
comostringocomando insert. Notequeosvaloresqueserãoinseridos
(linha34a41)estãorepresentadosporvariáveischamadas bind.Estetipo
devariávelécaracterizadoporiniciarcomdoispontosantesdoseunome.
Quandodeclaramosumavariáveldotipo bindaPL/SQLinterpretaqueal-
gumvalordeveserinformadoparaela,emumdadomomento. Casoeste
valornãosejapassadoporparâmetroéabertoum promptparaqueeleseja
digitado.
387

## Página 399

CasadoCódigo
Naslinhas43a50,temosocomando execute immediate.Eleaparece
precedidodastringouvariávelreferenteaocomandoquedeveserexecutado.
Casoparâmetrosdevamserpassados,utilizamosacláusula usingparaisto.
Vejanoexemplo,queestamosutilizando usingparapassarosparâmetros
paraocomando insert,substituindoasvariáveis bind.Estasubstitui ção
acontecedeformasequencial.
Além da inserção de empregados, também temos, no mesmo bloco
PL/SQL,ainser çãodedepartamentos. Emborabemparecidocomainser-
çãodeempregado,esteexemploserveparamostrarqueosvaloresreferen-
tesaosparâmetrospodemserpassadosdiretamentenocomando execute
immediate.Vejaoresultadonasequência:
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL COMM
---------- ------- --------- ------- -------- --------- --------
7499 ALLEN SALESMAN 7698 20/02/81 1600 306
7521 WARD SALESMAN 7698 22/02/81 1250 510
9999 BONO SALESMAN 7698 25/10/11 1000 0
7654 MARTIN SALESMAN 7698 28/09/81 1250 1428
7698 BLAKE MANAGER 7839 01/05/81 2850 285
7782 CLARK MANAGER 7839 09/06/81 2450 245
7839 KING PRESIDENT 17/11/81 5000 500
7844 TURNER SALESMAN 7698 08/09/81 1500 150
7900 JAMES CLERK 7698 03/12/81 950 95
7934 MILLER CLERK 7782 23/01/82 1300 130
7935 PAUL SALESMAN 7698 15/03/80 1000 100
DEPTNO PC_COM_SAL
---------- ----------
30 19 ,125
30 40,8
30
30 114,24
30
10
10
30 10
388

## Página 400

CasadoCódigo Capítulo23. SQLdinâmico
30
10
30 10
11 linhas selecionadas.
SQL> select * from dept;
DEPTNO DNAME LOC
---------- -------------- -------------
10 ACCOUNTING FLORIDA
30 SALES CHICAGO
40 OPERATIONS BOSTON
80 S&E
90 FINANCIAL
99 RH BRASIL
6 linhas selecionadas.
SQL> COMMIT;
Validação completa.
SQL>
Usocom deletee update:
SQL> declare
2 --
3 begin
4 --
5 execute immediate 'delete from emp
6 where empno = :empno ' using 9999;
7 --
8 execute immediate 'update dept set loc = :loc
9 where deptno = :depnto' using 'AUSTRALIA', 99;
10 --
11 end;
12 /
389

## Página 401

CasadoCódigo
Procedimento PL /SQL concluído com sucesso.
SQL>
Nesseexemplo,estamosmostrandoaexclusãoeatualizaç ãoderegistros
via execute immediate.Aseguirtemosoresultado:
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL COMM
---------- ------- --------- ------- -------- --------- --------
7499 ALLEN SALESMAN 7698 20/02/81 1600 306
7521 WARD SALESMAN 7698 22/02/81 1250 510
7654 MARTIN SALESMAN 7698 28/09/81 1250 1428
7698 BLAKE MANAGER 7839 01/05/81 2850 285
7782 CLARK MANAGER 7839 09/06/81 2450 245
7839 KING PRESIDENT 17/11/81 5000 500
7844 TURNER SALESMAN 7698 08/09/81 1500 150
7900 JAMES CLERK 7698 03/12/81 950 95
7934 MILLER CLERK 7782 23/01/82 1300 130
7935 PAUL SALESMAN 7698 15/03/80 1000 100
DEPTNO PC_COM_SAL
---------- ----------
30 19 ,125
30 40,8
30 114,24
30
10
10
30 10
30
10
30 10
10 linhas selecionadas.
SQL> select * from dept;
390

## Página 402

CasadoCódigo Capítulo23. SQLdinâmico
DEPTNO DNAME LOC
---------- -------------- -------------
10 ACCOUNTING FLORIDA
30 SALES CHICAGO
40 OPERATIONS BOSTON
80 S&E
90 FINANCIAL
99 RH AUSTRALIA
6 linhas selecionadas.
SQL> COMMIT;
Validação completa.
SQL>
Usocomoscomandos createe alter. execute immediate pode
serusadotambémparaacriaç ãoealteraç ãodinâmicadetabelas:
SQL> declare
2 --
3 begin
4 --
5 execute immediate 'create table func
6 (cd_func number, nm_func varchar2(50))';
7 --
8 execute immediate 'alter table func
9 modify cd_func number not null';
10 --
11 end;
12 /
Procedimento PL/SQL concluído com sucesso.
SQL> desc func
Nome Nulo? Tipo
-------------------------------------------------- -------------
CD_FUNC NOT NULL NUMBER
NM_FUNC VARCHAR2(50)
SQL>
391

## Página 403

CasadoCódigo
Pormeiodousodo execute immediate épossívelretornarinforma-
çõesprovenientesdecomandosSQL.Vejaesteexemplodaexecuç ãodeum
update:
SQL> declare
2 --
3 watualiza_dept varchar2(2000);
4 --
5 wdname dept.dname%type;
6 wloc_re dept.loc%type;
7 --
8 wloc dept.loc%type default 'CHILE';
9 wdeptno dept.deptno%type default 99;
10 begin
11 --
12 watualiza_dept := 'update dept set loc = :1
where deptno = :2
13 returning dname, loc into :3, :4';
14 --
15 execute immediate watualiza_dept using wloc, wdeptno
16 ,out wdname, out wloc_re;
17 --
18 dbms_output.put_line('Localização atualizada para o
departamento '||
19 wdname||' (Loc: '|| wloc||').');
20 --
21 end;
22 /
Localização atualizada para o departamento RH (Loc: CHILE).
Procedimento PL /SQL concluído com sucesso.
SQL> select * from dept;
DEPTNO DNAME LOC
---------- -------------- -------------
10 ACCOUNTING FLORIDA
30 SALES CHICAGO
40 OPERATIONS BOSTON
392

## Página 404

CasadoCódigo Capítulo23. SQLdinâmico
80 S&E
90 FINANCIAL
99 RH CHILE
6 linhas selecionadas.
SQL>
Analisandoesseexemplo,temosnalinha12avariável watualiza_dept
recebendoastringreferenteaocomando update.Tambémépossívelobser-
varque,nalinha13,estáincluídaacláusula returningseguidadedoiscam-
pos,osquaisserãoonossoretorno,seguidadacláusula intoinformando
duasvariáveis bind,asquaisreceberãoosvaloresretornados.
Umaobservaçãoimportante,équenalinha15e16,referentesaocomando
execute immediate,temosduaspassagensdeparâmetrosdotipo in(en-
trada)eduasdotipo out(saída),sendoqueestasduasúltimasguardam
nossoretorno.Valelembrarquequandonãoinformadootipodavariávelna
cláusulausing,porpadrão,seutiposerádeentrada( in).
Vejaoutroexemploutilizandoretornodeinformaç ão,masagoracomo
usodacláusula returningtambémno execute immediate.Noteque
atravésdestanotaçãonãonecessitamosinformarotipodasvariáveisdere-
torno.
SQL> declare
2 --
3 watualiza_dept varchar2(2000);
4 --
5 wdname dept.dname%type;
6 wloc_re dept.loc%type;
7 --
8 wloc dept.loc%type default 'ARGENTINA';
9 wdeptno dept.deptno%type default 99;
10 begin
11 --
12 watualiza_dept := 'update dept set loc = :1 where
deptno = :2
13 returning dname, loc into :3, :4';
14 --
393

## Página 405

CasadoCódigo
15 execute immediate watualiza_dept using wloc, wdeptno
16 returning into wdname, wloc_re;
17 --
18 dbms_output.put_line('Localização atualizada para o
departamento '||
19 wdname||' (Loc: '|| wloc||').');
20 --
21 end;
22 /
Localização atualizada para o departamento RH (Loc: ARGENTINA).
Procedimento PL /SQL concluído com sucesso.
SQL> select * from dept;
DEPTNO DNAME LOC
---------- -------------- -------------
10 ACCOUNTING FLORIDA
30 SALES CHICAGO
40 OPERATIONS BOSTON
80 S&E
90 FINANCIAL
99 RH ARGENTINA
6 linhas selecionadas.
SQL>
Oexemploaseguirmostraousodo execute immediate naexecução
dinâmicadeumcomando delete:
SQL> create function rows_deleted ( table_name in varchar2
2 ,condition in varchar2) return integer as
3 begin
4 execute immediate 'delete from ' || table_name || '
where ' || condition;
5 return sql%rowcount;
6 end;
7 /
394

## Página 406

CasadoCódigo Capítulo23. SQLdinâmico
Função criada.
SQL> declare
2 wnr_linhas number;
3 begin
4 wnr_linhas := rows_deleted('EMP',' empno = 7935');
5 --
6 dbms_output.put_line('Linhas excluídas: '||wnr_linhas);
7 --
8 end;
9 /
Linhas excluídas: 1
Procedimento PL/SQL concluído com sucesso.
SQL>
Notequeutilizamosocursorimplícito sql%rowcountpararetornar
aquantidadedelinhasexcluídas. Atravésdesterecursotambémépossível
executarprocedimentosPL/SQL.Paraisso,criamosuma procedurepara
realizarinser çõesnatabela dept.
SQL> create or replace procedure cria_dept (
pdeptno in number
2 ,pdname in varchar2
3 ,ploc in varchar2
4 ,pstatus in out varchar2) is
5 begin
6 --
7 insert into dept values (pdeptno, pdname, ploc);
8 --
9 pstatus := 'OK';
10 --
11 commit;
12 --
13 exception
14 when others then
15 pstatus := sqlerrm;
395

## Página 407

CasadoCódigo
16 end;
17 /
Procedimento criado.
SQL>
Agorachamamosa procedurecriadaatravésdeoutroblocoPL/SQL,
utilizandoumachamadadinâmica.
SQL> declare
2 --
3 winsere_dept varchar2(2000);
4 --
5 wdname dept.dname%type default 'RH';
6 wloc dept.loc%type default 'ARGENTINA';
7 wdeptno dept.deptno%type default 88;
8 --
9 wstatus varchar2(4000);
10 --
11 begin
12 --
13 winsere_dept := 'begin cria_dept(:a, :b, :c, :d); end;';
14 --
15 execute immediate winsere_dept
16 using in wdeptno, in wdname, in wloc, in out wstatus;
17 --
18 if wstatus = 'OK' then
19 --
20 dbms_output.put_line('Departamento inserido com
sucesso.');
21 --
22 else
23 --
24 dbms_output.put_line('Erro ao inserir departamento.
Erro: '||wstatus);
25 --
26 end if;
27 end;
396

## Página 408

CasadoCódigo Capítulo23. SQLdinâmico
28 /
Departamento inserido com sucesso.
Procedimento PL/SQL concluído com sucesso.
SQL>
Vejaoresultado:
SQL> select * from dept;
DEPTNO DNAME LOC
---------- -------------- -------------
10 ACCOUNTING FLORIDA
30 SALES CHICAGO
40 OPERATIONS BOSTON
80 S&E
90 FINANCIAL
99 RH ARGENTINA
88 RH ARGENTINA
7 linhas selecionadas.
SQL>
Aseguir, diferentesusosdeSQLdinâmicoparacomandos select,
comretornodeinformações. Nestesexemplos,nãoutilizaremos execute
immediate;emvezdisso,usaremoscursoresdotipo ref cursor.
23.1 R ef cursor
Umavariáveldotipo ref cursor,comoécomumentechamada,éutili-
zadaparareferenciaraestruturadeuma query,deformadinâmica,ouseja,
elanãoestáligadaexatamenteaumúnicocomandoSQL,diferentedouso
decursores,noqualaodeclararmos,necessitamosinformarumcomando
selectespecífico.
Variáveisdotipo ref cursor,pornãoteremumaestruturapredefi-
nida,podemserusadasváriasvezesdentrodeumprogramaparadiferen-
tescomandos selecteparaumnúmeroilimitadodelinhas. Variáveis
397

## Página 409

23.1. Refcursor CasadoCódigo
dotipo ref cursor podemaindaseremdefinidascomoparâmetrosem
procedures.Suadeclaraç ãoésemelhanteàdeclaraç ãodevariáveisdotipo
tabelaouregistro( Index-By Table, Record).
Aprincipalvantagemnousodevariáveisdotipo ref cursor sedápelo
fatodeelaapenasapontarparaaestruturaoulinharetornadapelocomando
select. Sendoassim,oresultadonãoéarmazenado,apenasreferenciado.
Issoémuitoútilnapassagemdeinformaçõesentreváriossistemas,poisnão
háumapassagemdeinformaçõespropriamentedita,apenasocompartilha-
mentoatravésdoquechamamosdeumponteiro.
SQL> declare
2 type empcurtyp is ref cursor;
3 emp_cv empcurtyp;
4 --
5 my_ename varchar2(15);
6 my_sal number default 1000;
7 begin
8 open emp_cv for
'select ename, sal from emp where sal > :s' using my_sal;
9 loop
10 fetch emp_cv into my_ename, my_sal;
11
12 exit when emp_cv%notfound;
13 --
14 dbms_output.put_line(
'Empregado: '||my_ename||' Salário: '||my_sal);
15 --
16 end loop;
17 end;
18 /
Empregado: ALLEN Salário: 1600
Empregado: WARD Salário: 1250
Empregado: MARTIN Salário: 1250
Empregado: BLAKE Salário: 2850
Empregado: CLARK Salário: 2450
Empregado: KING Salário: 5000
Empregado: TURNER Salário: 1500
Empregado: MILLER Salário: 1300
398

## Página 410

CasadoCódigo Capítulo23. SQLdinâmico
Procedimento PL/SQL concluído com sucesso.
SQL>
Nesteexemplo,estamosutilizandoum ref cursor querecebeuma
stringdeumcomandoSQL(linha8).Utilizamosascláusulas opene for
paraatribuirocomandoàvariável ref cursor emp_cv.Depois,utiliza-
mosum loopsimples(linha9)paramanipularasinformações,quesãoatri-
buídasaduasvariáveisatravésdacláusulainto(linha10).Notequetambém
utilizamosacláusula usingparapassagemdeparâmetro.
SQL> declare
2 type empcurtyp is ref cursor;
3 emp_cv empcurtyp;
4 emp_rec emp%rowtype;
5 --
6 sql_stmt varchar2(200);
7 my_job varchar2(15) := 'CLERK';
8 begin
9 sql_stmt := 'select * from emp where job = :j';
10 --
11 open emp_cv for sql_stmt using my_job;
12 loop
13 fetch emp_cv into emp_rec;
14 exit when emp_cv %notfound;
15 --
16 dbms_output.put_line('Empregado: '||emp_rec.ename||'
Salário: '||emp_rec.sal);
17 --
18 end loop;
19 close emp_cv;
20 end;
21 /
Empregado: JAMES Salário: 950
Empregado: MILLER Salário: 1300
Procedimento PL/SQL concluído com sucesso.
399

## Página 411

23.1. Refcursor CasadoCódigo
SQL>
Esseexemploébemsemelhanteaoanterior.Adiferen çaestánaslinhas4
e13.Declaramosumavariáveldotipotabela,utilizandoaestruturadatabela
emp(linha4),quereceberáoresultadodo selectatravésdacláusulainto
nalinha13.
OpróximoexemplomostraquepodemosmontarumcomandoSQLatra-
vésdestringspassadasporparâmetro.
SQL> create procedure print_table (tab_name varchar2) is
2 type refcurtyp is ref cursor;
3 cv refcurtyp;
4 wdname dept.dname%type;
5 wloc dept.loc%type;
6 begin
7 open cv for 'select dname, loc from ' || tab_name;
8 --
9 loop
10 fetch cv into wdname, wloc;
11 exit when cv%notfound;
12 --
13 dbms_output.put_line('Departamento: '||wdname||'
Localização: ' ||wloc);
14 --
15 end loop;
16 --
17 close cv;
18 --
19 end;
20 /
Procedimento criado.
SQL> begin print_table (tab_name => 'DEPT'); end;
2 /
Departamento: ACCOUNTING Localização: FLORIDA
Departamento: SALES Localização: CHICAGO
Departamento: OPERATIONS Localização: BOSTON
Departamento: S &E Localização:
400

## Página 412

CasadoCódigo Capítulo23. SQLdinâmico
Departamento: FINANCIAL Localização:
Departamento: RH Localização: ARGENTINA
Departamento: RH Localização: ARGENTINA
Procedimento PL/SQL concluído com sucesso.
SQL>
Jánoexemploaseguirtemosummixdevariável ref cursor evariá-
veis tablee record. Aquiutilizamosacláusula bulk collect,queé
responsávelporpreparartodaacole çãodesaídadedados.Estacláusulapode
serusadajuntocomacláusula intonoscomandos select into, fetch
into, returning into evariáveis table. Estacláusulanãopodeser
usadaparavariáveisdotipo record.Dessaforma,casotenhamosinforma-
çõesreferentesaváriascolunas,seránecessáriaacriaç ãodeumavariáveldo
tipo tableparacadauma.
SQL> declare
2 type empcurtyp is ref cursor;
3 type numlist is table of number;
4 type namelist is table of varchar2(15);
5 --
6 emp_cv empcurtyp;
7 empnos numlist;
8 enames namelist;
9 --
10 sals numlist;
11 begin
12 open emp_cv for 'select empno, ename from emp';
13 fetch emp_cv bulk collect into empnos, enames;
14 close emp_cv;
15 --
16 for r in 1..empnos.count loop
17 dbms_output.put_line('Cód.: '||empnos(r)||' -
Empregado: '||enames(r));
18 end loop;
19 --
20 execute immediate 'select sal from emp'
21 bulk collect into sals;
401

## Página 413

23.1. Refcursor CasadoCódigo
22 --
23 for r in 1 ..sals.count loop
24 dbms_output.put_line('Salário: '||sals(r));
25 end loop;
26 end;
27 /
Cód.: 7499 - Empregado: ALLEN
Cód.: 7521 - Empregado: WARD
Cód.: 7654 - Empregado: MARTIN
Cód.: 7698 - Empregado: BLAKE
Cód.: 7782 - Empregado: CLARK
Cód.: 7839 - Empregado: KING
Cód.: 7844 - Empregado: TURNER
Cód.: 7900 - Empregado: JAMES
Cód.: 7934 - Empregado: MILLER
Cód.: 7935 - Empregado: PAUL
Salário: 1600
Salário: 1250
Salário: 1250
Salário: 2850
Salário: 2450
Salário: 5000
Salário: 1500
Salário: 950
Salário: 1300
Salário: 1000
Procedimento PL /SQL concluído com sucesso.
SQL>
Nalinha2,temosadefiniç ãodeumavariáveldotipo ref cursor que
receberáumcomandoSQL.Jánaslinhas3e4,temosadeclaraç ãodeduas
variáveisdotipo table. Estadeclaraçãodefinedoistiposarray,umarray
numéricoeoutrodecaracteres.Naslinhas7e8,sãodeclaradasduasvariá-
veiscombasenestestipos.Naslinhas12e13,foiutilizadoumcursorquelê
asinformaçõesdeum selectdinâmicoque,atravésdo bulk collect,
carregaasinformaçõesparaasvariáveisdotipoarray.
402

## Página 414

CasadoCódigo Capítulo23. SQLdinâmico
Notequenãofoinecessárioutilizar loopparaatribuiraslinhasvindasdo
select.O bulk collect jáfazestaatribuição.Naslinhas16e18,utiliza-
mosum for loop paralerosdadosdasvariáveisarray.Observequeo for
looptomacomobaseaquantidadedelinhasqueoarraypossui.Nestecaso,
utilizamoso countdeumadasvariáveisparadeterminarvalorfinaldo for
loop,mesmoporquecarregamosasduasvariáveisemummesmomomento
eutilizandoomesmo select.Logo,aquantidadededadoscarregadosnas
duasvariáveiséamesma.
Dentronomesmoprogramatemosoutraexecuç ãodinâmica(linhas20a
21),ondeépossívelusaro bulk collect tambémparareceberoresultado
vindoatravésdaexecuçãovia execute immediate.
Por último, um exemplo defunction para retornar a quantidade
deregistrosemumadeterminadatabela, passadaporparâmetro, usando
execute immediate comretornoutilizando into.
SQL>
create function row_count(tab_name varchar2) return integer as
2 rows integer;
3 begin
4 execute immediate 'select count(*) from ' ||
tab_name into rows;
5 return rows;
6 end;
7 /
Função criada.
SQL> select row_count('EMP') from dual;
ROW_COUNT('EMP')
----------------
10
SQL>
403

## Página 416

Capítulo24
Apêndice:SQL–Primeiros
passos
24.1 C omo iniciar no SQL
Umadasdificuldadesqueencontramosquandoestamosaprendendouma
linguagemdeprogramaç ãoésaberporondecome çar. Nocasodoapren-
dizadodaSQL,nãoseriadiferente. Éumasituaç ãonormal. Atésentirmos
segurançaetermosconhecimentosuficientesobrealinguagem,éinteressante
termosumroteirocontendoosprimeirospassosparainiciarumprograma
oucomandoSQL.
Destaforma,demonstroaquiumatécnicaqueutilizobastante,mesmo
tendoumbomconhecimentonalinguagem. Naverdade,jáestáimplícito
naminhaformadepensar,tantoqueacaboexecutando-amentalmente,en-

## Página 417

24.1. ComoiniciarnoSQL CasadoCódigo
quantoescrevonestalinguagem. Estemétodonãofoiretiradodenenhum
livro,foialgoque,entendendoalógica,fuiseguindoedeucerto.Esperoque
ajudevocês.
Vamostomarcomoexemploaquestãoaseguir:
Escreva um select que apresente as colunas, nome da região
( REGION_NAME: tabela REGIONS), nome da cidade (CITY: tabela
LOCATIONS), nome do departamento ( DEPARTMENT_NAME: tabela
DEPARTMENTS)eonomedosempregados( FIRST_NAME),massomente
daquelesquepossuamosaláriomaiorque11.000. Ordeneosdadospelos
mesmoscamposdo select,seguindoamesmaordemdoenunciado.
Primeiro passo
Identifico no enunciado as fontes de dados, ou seja, as tabelas que farão
parte do comando SQL.
Nestenossoexemplo,astabelassão:REGIONS,COUNTRIES,LOCATI-
ONS,DEPARTMENTSeEMPLOYEES,poisoenunciadonosdizisto.Con-
tudo,seelenãodizosnomesdastabelas,pelomenosdevemencionardoque
setratamtaisinformações,porexemplo,empregados,departamentos,países
etc.
Sevocêtivero MER(ModeloEntidadeRelacionamento,vejaanexos 26)
ficamaisfácil,poisnelevocêconsegueverificaralocalizaç ãodetaisinfor-
maçõesreferentesaosnomesdastabelasouosnomesdoscampososquaiso
enunciadopede.Exemplo:REGION_NAME,CITYetc.
CasonãotenhaoMER,vocêpodelocalizartaistabelasnobancodeda-
dos,executandoum selectna user_tablesou all_tablesparatentar
localizá-lasatravésdosseusnomes.Tendoaslocalizado,vocêpodeexecutar
ocomando descemcimadecadaumadelasparavisualizarsuascolunase
identificarasinformaçõessolicitadas.Vejaoexemploaseguir:
SQL> select table_name
2 from user_tables;
TABLE_NAME
------------------------------
EMP
406

## Página 418

CasadoCódigo Capítulo24. Apêndice:SQL–Primeirospassos
DEPT
BONUS
SALGRADE
DUMMY
REGIONS
LOCATIONS
DEPARTMENTS
JOBS
EMPLOYEES
JOB_HISTORY
COUNTRIES
23 linhas selecionadas.
SQL>
Casovocêqueiraversehácomentáriossobretaistabelas, porexem-
plo, indicando sua finalidade, você pode executar umselect na
user_tab_commentsou all_tab_comments,pesquisandopelonome
databela. Lembrandoqueutilizandoatabelacomprefixo allvocêdeve
informaraqueusuário,oumelhor,aqualdono,atabelapertence. Vejao
exemplo:
SQL> select comments
2 from user_tab_comments
3 where table_name = 'EMPLOYEES';
COMMENTS
-----------------------------------------------------------------
employees table. Contains 107 rows. References with departments,
jobs, job_history tables. Contains a self reference.
SQL>
Segundo passo
Conectado ao banco de dados, através de uma ferramenta, exemplo
SQL*Plus, faço um breve reconhecimento das tabelas envolvidas no enun-
407

## Página 419

24.1. ComoiniciarnoSQL CasadoCódigo
ciado.
Seguindooexemplo,vamosanalisaratravésdocomando descastabe-
lasecolunasqueidentificamos,comoastabelasEMPLOYEESeDEPART-
MENTS.
SQL> desc employees
Nome Nulo? Tipo
----------------------------------------- -------- -------------
EMPLOYEE_ID NOT NULL NUMBER(6)
FIRST_NAME VARCHAR2(20)
LAST_NAME NOT NULL VARCHAR2(25)
EMAIL NOT NULL VARCHAR2(25)
PHONE_NUMBER VARCHAR2(20)
HIRE_DATE NOT NULL DATE
JOB_ID NOT NULL VARCHAR2(10)
SALARY NUMBER(8,2)
COMMISSION_PCT NUMBER(2,2 )
MANAGER_ID NUMBER(6)
DEPARTMENT_ID NUMBER(4)
BIRTH_DATE DATE
HIRE_DATE_BKP DATE
SQL> desc departments
Nome Nulo? Tipo
----------------------------------------- -------- -------------
DEPARTMENT_ID NOT NULL NUMBER(4)
DEPARTMENT_NAME NOT NULL VARCHAR2(30)
MANAGER_ID NUMBER(6)
LOCATION_ID NUMBER(4)
SQL>
T erceiro passo
Inicio a escrita do comando SQL, preenchendo a cláusulaselect com
as colunas que devo mostrar, e a cláusulafrom informando às tabelas que
vou precisar para recuperar todas as informações.
select r.region_name
408

## Página 420

CasadoCódigo Capítulo24. Apêndice:SQL–Primeirospassos
,l.city
,d.department_name
,e.first_name
from regions r
,countries c
,locations l
,departments d
,employees e
Notequenemsempresãomencionadasnoenunciadotodasastabelasde
queprecisaremospararetornartodasasinformações.Destaforma,precisa-
mosconsultarnovamenteoMER,paraentenderquaissãotodasasligações
edequaisobjetosvamosnecessitar. Valesalientarqueentreastabelas,na
maioriadoscasos,existeumaoumaiscolunasquesãoasresponsáveispe-
lasligaçõesentreelas.Necessitamosfazerestasligaçõesparaqueoresultado
retornadosejaoresultadocorreto,eaintegridadesejamantida.
Outrofatorimportante:sempreutilizoapelidos(aliasl )paraidentificar
astabelasecolunasemumcomandoSQL.Issoserveparaevitarerrosde
colunasambíguas(colunascomnomesiguaisentreastabelas,pois,nestecaso,
oOraclenãosabedizerqueméquem),eparatornaraleituradocomando
SQLmaisinteligível.
Quarto passo
Fazer as ligaç ões entre as tabelas que estamos utilizando na cláusula
from.
10 where r.region_id = c.region_id
11 and c.country_id = l.country_id
12 and l.location_id = d.location_id
13 and d.department_id = e.department_id
Caso não se tenha o MER, podemos fazer umselect nas views
user_constraintse user_cons_columns,paratentarlocalizarasli-
gaçõesentreastabelas.Exemplo:
SQL> select cons. table_name||'.'||cons_col.column_name||
2 ' faz ligação com '||
409

## Página 421

24.1. ComoiniciarnoSQL CasadoCódigo
3 cons_depend.table_name||'.
'||cons_col_depend.column_name||' '||
4 'através da chave '||cons.constraint_name "
Dependências"
5 from -- tabela pesquisa
6 user_constraints cons
7 ,user_cons_columns cons_col
8 -- tabela dependencia
9 ,user_constraints cons_depend
10 ,user_cons_columns cons_col_depend
11 where cons.constraint_name = cons_col.constraint_name
12 and cons.table_name = cons_col.table_name
13 and cons.table_name =
'EMPLOYEES' -- tabela para pesquisa
14 and cons.constraint_type =
'R' -- Foreign key (ligação entre as tabelas)
15 --
16 and cons_depend.constraint_name =
cons_col_depend.constraint_name
17 and cons_depend.table_name =
cons_col_depend.table_name
18 and cons_depend.constraint_name = cons.r_constraint_name
19 order by 1
20 /
Dependências
-----------------------------------------------------------------
EMPLOYEES.DEPARTMENT_ID faz ligação com
DEPARTMENTS.DEPARTMENT_ID através da chave
EMP_DEPT_FK
EMPLOYEES.JOB_ID faz ligação com JOBS.JOB_ID através da chave
EMP_JOB_FK
EMPLOYEES.MANAGER_ID faz ligação com EMPLOYEES.EMPLOYEE_ID
através da chave EMP_MANAGER_FK
SQL>
Observação: Vocêpodeutilizareste selectsemprequepossível.
410

## Página 422

CasadoCódigo Capítulo24. Apêndice:SQL–Primeirospassos
Guarde-o!
Quinto passo
Colocar as demais críticas (restrições) solicitadas pelo enunciado.
14 and e.salary> 11000
15 order by r.region_name
16 ,l.city
17 ,d.department_name
18 ,e.first_name;
SegueocomandoSQLcompleto:
SQL> select r.region_name
2 ,l.city
3 ,d.department_name
4 ,e.first_name
5 from regions r
6 ,countries c
7 ,locations l
8 ,departments d
9 ,employees e
10 where r.region_id = c.region_id
11 and c.country_id = l.country_id
12 and l.location_id = d.location_id
13 and d.department_id = e.department_id
14 and e.salary> 11000
15 order by r.region_name
16 ,l.city
17 ,d.department_name
18 ,e.first_name;
Observações: paraosdemaiscomandos,comoo insert,o deletee
o update,podemosseguiromesmoraciocínio.Primeiramente,identifica-
mosastabelas,ascolunasparaasligaçõeserestrições,seforocaso,edepois
escrevemosocomando.
411

## Página 424

Capítulo25
Referênciasbibliográficas
• DATE,C.J.Introdução a Sistemas de Bancos de Dados.RiodeJaneiro:
Campus,1991.
• FERNANDES,Lúcia.Oracle 9i Para Desenvolvedores - Curso Completo.
RiodeJaneiro:AxcelBooks,2002.
• GENNICK,Jonathan,LUERS,Tom.Aprenda em 21 dias PL/SQL.2.ed.
RiodeJaneiro:Campus,2000.
• HEUSER,CarlosAlberto.Projeto de Banco de Dados. 4. ed. Porto
Alegre:SagraLuzzatto,2001.
• LIMA,AdilsondaSilva.Erwin 4.0 Modelagem de Dados. 2. ed. São
Paulo:Érica,2002.

## Página 425

CasadoCódigo
• LONEY,Kevinetal.Oracle 9i: O Manual do DBA.RiodeJaneiro:Cam-
pus,2002.
• MOLINARI,Leonardo.BTO Otimização da T ecnologia de Negócio.São
Paulo:Érica,2003.
• ORACLEDatabaseOnlineDocumentation10gRelease1(10.1). Dis-
ponívelem:<http://www.oracle.com/pls/db10g/portal.portal_demo3?
selected=1>.Acessoem:16mar.2011.
• OracleDatabaseNewFeaturesGuide11g,Release2(11.2)
• OracleDatabaseAdvancedApplicationDeveloper’sGuide11gRelease
2(11.2)
• OracleDatabasePL/SQLLanguageReference11gRelease2(11.2)
• OracleDatabaseReference11gRelease2(11.2)
• OracleDatabaseSQLLanguageReference11gRelease2(11.2)
• OracleDatabaseConcepts11g,Release2(11.2)
• OracleDatabasePL/SQLPackagesandTypesReference11gRelease2
(11.2)
• OracleDatabaseSQLDeveloperUser’sGuideRelease3.1
414

## Página 426

Capítulo26

## Página 427

CasadoCódigo
Anexos
Fig.26.1:EsquemadabasededadosSCOTTutilizadanosexemplos
416

## Página 428

CasadoCódigo Capítulo26. Anexos
Fig.26.2:EsquemadabasededadosHRutilizadanosexemplos
417