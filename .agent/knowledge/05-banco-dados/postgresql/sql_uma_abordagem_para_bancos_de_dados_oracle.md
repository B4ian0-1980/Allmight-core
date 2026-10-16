---json
{
  "id": "sql_uma_abordagem_para_bancos_de_dados_oracle",
  "title": "sql-uma-abordagem-para-bancos-de-dados-oracle04.pdf",
  "categoria": "05-banco-dados",
  "subcategoria": "postgresql",
  "resumo": "**Arquivo Original:** `SQL Uma abordagem para bancos de dados Oracle.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "abordagem",
    "banco",
    "bancos",
    "dados",
    "oracle",
    "para",
    "pdf",
    "postgresql"
  ],
  "perguntas_tipo": [
    "Como utilizar sql-uma-abordagem-para-bancos-de-dados-oracle04.pdf?",
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

# sql-uma-abordagem-para-bancos-de-dados-oracle04.pdf

> **Arquivo Original:** `SQL Uma abordagem para bancos de dados Oracle.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
T odos os direitos reservados e protegidos pela Lei nº9.610, de
10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem
autorização prévia por escrito da editora, sejam quais forem os meios:
fotográﬁcos, eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 3

CasadoCódigo
Agradecimentos
Em primeiro lugar, agradeço a Deus por este presente que é a minha vida e
por mais esta conquista. Dedico este livro a minha esposa Thaiseam i n h a
filha Lisyê. Vocês são meus tesouros. Obrigado por entender as ausências,
cujomotivo,foiàsincontáveishorasdespendidasparaqueesteprojetofosse
possível. E por último, não menos importante, agradeço aos meus pais por
tudoquesemprefizeramecontinuamfazendopormim. Amotodosvocês.
i

## Página 5

CasadoCódigo
Sobreoautor
FormadoemTecnologiadaInformação,possuimaisde10anosdeexperiên-
cia em análise e desenvolvimentos de sistema voltados á tecnologias Oracle,
trabalhando em grandes empresas como Lojas Renner, Mundial S.A, Tigre
S.A,Pernambucanas,TractebelEnergia,PortobelloCerâmica,Bematech,en-
tre outros. É instrutor de cursos oficiais da Oracle – nas linguagens SQL e
PL/SQL. Também atua no desenvolvimento de aplicações mobile para a pla-
taforma iOS. Atualmente, desempenhando o papel de Líder Operacional de
ProjetosnaSuperoTecnologia.
iii

## Página 7

CasadoCódigo
Prefácio
Sempregosteidelivrosdosquais“conversam”comoleitor,principalmenteos
técnicos. Comosefosseumatrocadeidéias,entreoautorequemestalendo.
Procureiescreverdestaforma,poiscreioquecomistoaleiturasetornamais
claraeamigável,comosefosseumbatepapoentreamigos,conversandosobre
qualquerassunto.
Procurei colocar neste livro tudo que você vai precisar saber sobre a lin-
guagemSQL.Olivroabordaconceitosquesãoutilizadosnodiaadiadode-
senvolvimento e análise de sistemas para banco de dados Oracle. Repleto de
exemplos,estelivrotambémvaiajudá-locomofontedereferênciaparacon-
sultadecomandosecomoutilizá-los. Tenhatodos,umaótimaleitura!
v

## Página 9

CasadoCódigo
Considerações
Públicoalvo
EstelivrosedestinaainicianteseexperientesnalinguagemSQL.Paraosini-
ciantes,sãoabordadosconceitossobreaestruturadalinguagemSQLeasca-
racterísticasvoltadasparabancodedadosOracle. Inclusivealgunsconceitos
do padrão ANSI, também são abordados. Para os já experientes, ele ajudará
comofontedereferênciaepararelembrarconceitosetécnicasdalinguagem.
Comoestádivididoolivro?
Primeiramente, são abordados conceitos sobre bancos de dados relacio-
nais, como por exemplo, os conceitos de Relações, Tabelas, Linhas, Colunas,
Registros,IntegridadedeDados,bemcomoaspectosrelacionadosàLingua-
gemSQL,comosuadefiniçãoesuastrêsestruturas–LinguagemdeDefinição
dos Dados (DDL), Linguagem de Manipulação dos Dados (DML) e Lingua-
gemdeControledosDados(DCL).
Depoisdestaintrodução,sãoabordadosedetalhadostodososaspectosda
linguagemSQLnoâmbitoprático,ondeémostradacadaumadesuasestru-
turas,seuscomandosecaracterísticas. Sempreapresentandoexplicaçõespara
cada conceito ou comando e, em seguida, demonstrando aplicações através
deexemplos.
Os scripts de base (tabelas e dados), fontes para a execução dos
exemplos do livro, estão disponíveis no endereço https://github.com/
eduardogoncalvesbr/livrosql-casadocodigo.
Contatos
Para falar com o autor, envie email para eduardogoncal-
ves.br@gmail.com.
vii

## Página 11

CasadoCódigo Sumário
Sumário
1 Noinício...Eraocaos! 1
1.1 Porquelerestelivro ........................ 1
2 Bancodedados 9
2.1 Introduçãoaobancodedadosrelacional ............ 1 0
2.2 Chaveprimária(índiceprimário) ................ 1 1
2.3 Chaveestrangeira ......................... 1 3
2.4 Chavealternativa .......................... 1 5
2.5 Integridadedeentidade ...................... 1 8
2.6 Integridadereferencial ...................... 1 8
3 IntroduçãoàlinguagemSQL 23
3.1 OracleCorporationeBancodedadosOracle ......... 2 5
3.2 ComunicandocomobancodedadosOracle ......... 2 8
3.3 Escopodousuário ......................... 3 0
3.4 Transações ............................. 3 2
3.5 DicionáriodedadosdoOracle .................. 3 6
3.6 ComooOracleexecutacomandosSQL ............. 3 8
4 ExecutandocomandosSQLcomSQL*Plus 41
4.1 OqueéSQL*Plus? ......................... 4 1
4.2 ComandosdeediçãodoSQL*Plus ............... 4 2
4.3 Variáveisdesistema ........................ 4 7
4.4 DefinindoVariáveisnoSQL*Plus ................ 6 0
ix

## Página 12

Sumário CasadoCódigo
4.5 ConfiguraçõesiniciaisdelogindoSQL*Plus .......... 6 1
4.6 VerificandoVariáveisdeSubstituiçãonoSQL*Plus ...... 6 3
4.7 AutomatizarlogindoSQL*Plus ................. 6 4
5 LimitesdoSGDBOracle 65
5.1 TiposdedadosdoSGDBOracle ................. 6 7
5.2 Resumo ............................... 7 2
6 Gerenciandousuários 73
6.1 Manipulandousuários ...................... 7 3
6.2 Concedendoacessoaousuário .................. 7 5
6.3 Privilégiosdesistema ....................... 7 8
6.4 AcessoatravésdeROLES ..................... 8 1
7 Manipulaçãodetabelas 99
7.1 ManipulandoTabelas ....................... 9 9
7.2 ALTERTABLE ........................... 1 1 0
7.3 DROPTABLE ........................... 1 1 3
7.4 TRUNCATETABLE ........................ 1 1 4
7.5 Ordenandodados ......................... 1 1 4
7.6 Trazendodadosdistintos ..................... 1 1 9
7.7 Relacionamentoentretabelas .................. 1 2 0
7.8 INNERJOIN ............................ 1 2 0
7.9 Cláusula USING .......................... 1 2 4
8 Selecionandodados 145
8.1 Selecionandodados ........................ 1 4 5
8.2 SELECTFORUPDATE ...................... 1 5 1
8.3 Selecionandoodestino ...................... 1 5 4
8.4 Restringindodados ........................ 1 5 5
8.5 Escolhendolinhasecolunas ................... 1 5 6
8.6 Utilizandooperadores ....................... 1 5 7
x

## Página 13

CasadoCódigo Sumário
9 Manipulaçãodedados 171
9.1 Inserçãodedados ......................... 1 7 1
9.2 Atualizaçãodedados ....................... 1 7 6
9.3 Exclusãodedados ......................... 1 8 0
10 Trabalhandocomfunções 185
10.1 Funçõesdecaracteres,decálculoseoperadoresaritméticos .1 8 5
10.2 Funçõesdeagregação(grupo) .................. 1 9 6
10.3 Funçõesdedata .......................... 2 0 9
10.4 Funçõesdeconversão ....................... 2 1 2
10.5 Funçõescondicionais ....................... 2 3 7
11 Integridadededadoseintegridadereferencial 249
11.1 Integridadededadoseintegridadereferencial ......... 2 4 9
12 Oracleavançado 291
12.1 Trabalhandocomviews ...................... 2 9 1
12.2 Trabalhandocomíndices ..................... 3 0 4
12.3 Sinônimos ............................. 3 1 4
12.4 SEQUENCES ............................ 3 2 9
13 ANEXOS 337
14 REFERÊNCIASBIBLIOGRÁFICAS 341
xi

## Página 15

Capítulo1
Noinício... Eraocaos!
1.1 Porquelerestelivro
AntesdeiniciarmoscomasabordagensdebancodedadoseSQLvamosen-
tenderquaisforamàsmotivaçõesquelevaramaodesenvolvimentodestastec-
nologias e como isso melhorou muito a forma de desenvolver sistemas, cri-
andosoftwaresmaisrobustoseconfiáveis.
Houve um tempo onde não existia o conceito de banco de dados, muito
menossistemasgerenciadoresparaestefim. Masentão,comoosdadoseram
armazenados? Poisbem,nestetempoosdadoseramarmazenadosemarqui-
vos,comoporexemplo,planilhasouarquivosdetexto,queficavamgravados
nos computadores dos usuários ou em fitas e disquetes. Na época isso já era
umaevoluçãoemtanto,contudo,mesmoasinformaçõesestandoarmazena-
dasemmeiosdigitais,haviafalhaseissoocasionavamuitosproblemas.
Muitosdosproblemasestavamrelacionadosaduplicidadededadosein-

## Página 16

1.1. Porquelerestelivro CasadoCódigo
consistências de informações. Sem falar nos problemas de falhas dos arqui-
vos, onde os mesmos, por alguma razão acabavam corrompidos e todas as
informaçõeseramperdidas. Muitasvezesestasinformaçõesficavamguarda-
dasemdisquetesoufitasqueseperdiamaolongodotempoousedegradavam
pelomauuso.
Outra dificuldade era que as informações não se relacionavam, ou seja,
não existia uma ligação entre elas, e com isto, pouco poderia ser feito para
utilizá-las como fonte estratégica de negócio numa empresa, por exemplo.
Era muito complicado cruzar informações de diversas áreas de negócio e
consolidá-lasafimdemediraprodutividadedeumaempresaouusá-lasem
tomadasdedecisão. Paraquevocêpossaentenderoqueestoufalando,vamos
2

## Página 17

CasadoCódigo Capítulo1. Noinício... Eraocaos!
observaroscasosaseguir.
Observando a figura anterior, vemos um problema clássico no uso desta
abordagem,aduplicidadededados. Nelevemosqueexistemduasplanilhas,
uma com a lista de empregados e outra com a lista de departamentos. Além
das informações estarem em planilhas independentes, não possuindo assim,
referenciaumacomaoutra,épossívelconstataraduplicidadededados,onde
onomedodepartamento,nestecaso,representadopelacolunaDNAME,apa-
recenasduaslistas. Istoeraumproblema,poisaduplicidadededados,além
deresultaremmaiorespaçoemdisco,abremargemparaoutroproblemaque
eraainconsistênciasdedados,conformepodeservistonopróximoexemplo.
3

## Página 18

1.1. Porquelerestelivro CasadoCódigo
Voltandoasmesmaslistasanteriores,adeempregadosedepartamentos,
podemos observar que a escrita referente ao departamento ACCOUNTING
(Contabilidade) na planilha de empregados foi escrito de forma incorreta,
sendodigitadocomoACCOUNT.Comisto,aumentam-seaschancesdosur-
gimentodedadosinconsistentesenãoconfiáveis,ondetemosduasdescrições
diferentes,masquequeremdizeramesmacoisa.
Outraformadearmazenamentodedadosemarquivoseraofamoso“ta-
belão”, onde as informações de diferentes tipos eram gravadas todas num
únicoarquivo. Vejaoexemploaseguir.
4

## Página 19

CasadoCódigo Capítulo1. Noinício... Eraocaos!
Notequetodososdadosreferentesaosempregados,como,nome,depar-
tamento, cargo, etc. estão todos em um mesmo arquivo. Com isto, vemos
muitas informações sendo duplicadas em um arquivo inchado, onde os ris-
cosdeinconsistênciasãoenormes,poisamesmainformaçãoqueapareceem
vários lugares, por exemplo, podem conter descrições diferentes por conta
de erros de digitação. Sem falar, quando uma informação muda, como, por
exemplo, um nome de departamento ou de um cargo, é necessário verificar
todas as linhas onde esta informação aparece para alterá-las de forma igual.
Além do retrabalho, pode ocorrer, por esquecimento de quem está atuali-
zando, que linhas que não sejam alteradas com a nova informação, gerem
dadosconflitantesesemnexo.
Creioquevocêpodeterumaidéiadecomoascoisaseramantesdeexisti-
remsistemasdegerenciamentodedados,cujoobjetivoerajustamentepossi-
bilitarumambienteconsistenteeorganizado,oquenãoacontecianopassado.
Foiassim,paraqueesteseoutrosproblemasfossemresolvidos,quesurgiram
os bancos de dados e seus gerenciadores. Com uma implementação baseada
emtécnicasdemodelagemdedadosecomumalinguagemrobustadeacesso,
foipossívelcriarumambienteseguro,confiáveledealtodesempenhoepro-
cessamentoparaamanipulaçãoearmazenagemdosdados.
Alémdemantertodososdadosnumúnicolugar,deformacentralizada,
através da modelagem de dados foi possível levar o conceito de administra-
5

## Página 20

1.1. Porquelerestelivro CasadoCódigo
çãodedadosparaumnívelmaisalto,diriaatéumexistencial,muitomelhore
muitomaisorganizado. Atravésdasregrasdenormalizaçãodedados,acha-
madas Formas Normais, é possível modelar toda estrutura de dados de um
sistema, visando a organização, o desempenho e principalmente a flexibili-
dadeeaclareza. Quandomodelamosumsistema,nãoapenascriamosabase
de dados a satisfazer apenas o intuito de armazenamento, mas sim, avalia-
mosqualamelhordefazeristo. Paraexemplificar,vejacomoficaroexemplo
anterior,utilizandoosdadosdeEmpregadoseDepartamentos.
Não vamos aqui, nos aprofundar nos conceitos de modelagem de da-
dos, entrando nos meandros de cada Forma Normal, por exemplo, nem nas
demais técnicas, mas seguindo este exemplo simples, é possível demonstrar
como podemos estruturar estas duas fontes de dados de forma clara e or-
ganizada. Note que nesta ultima figura tempos o que podemos chamar de
duas tabelas, uma de dados de empregados, onde temos informações sobre
6

## Página 21

CasadoCódigo Capítulo1. Noinício... Eraocaos!
nomes(ENAME),cargos(JOB),salários(SAL)eoutradedadosdedeparta-
mento,ondetemosinformaçõescomnomes(DNAME)elocalizações(LOC).
Vejaqueemborasejamduasfontesdedadosdistintasexisteumaligaçãoen-
tre elas. Esta ligação está sendo feita através de uma das colunas, a coluna
DEPTNO. Veja que esta coluna existe nas duas tabelas. Este que parece ser
um pequeno detalhe faz com que nossas fontes sejam consistentes e estejam
dentro das regras de modelagem. Observe como ligamos vários emprega-
dosadepartamento,semrepetirasinformações,utilizandoumcódigo. Com
isto, se necessitarmos alterar alguma informação relacionada a um determi-
nadodepartamento,como,porexemplo,onomeousualocalização,nãopre-
cisamos alterar para cada empregado, alteramos apenas o departamento em
questão, na tabela de departamentos. Desta forma, conseguimos manter as
informações de forma consistente, sem duplicidades, e desta forma também
dispostosdeformaestruturada.
Éobvioqueestefoiumexemplosimples,comojámencionado,contudo,
serve para mostrar que com o advento dos bancos de dados estas e outras
técnicas podem ser utilizadas na criação de sistemas capazes de atender as
demandas mais complexas ou que exigem maior processamento e alta per-
formance. Alémdomais,obancodedadospermiteapossibilidadedecriar-
mosumambienteúnicoondetodasasfontesdedadoscoexistamnele. Desta
forma, deixamos de ter arquivos distintos, em localizações diferentes e que
nãopossuemumaligaçãológica,nemmesmofísica.
Agoraquevocêjáentendeucomoeranoinício,estánahoradeentender
oagora,comofuncionandoosbancosdedadoseseusgerenciadores. Enten-
der seus conceitos e como trabalham. Além disso, aprender como é feita a
comunicaçãocomestesbancosecomosdadosarmazenadosneles.
7

## Página 23

Capítulo2
Bancodedados
Paraseobteroarmazenamentoadequadodainformação,éprecisoquesejam
escolhidosmétodosquesatisfaçamosrequisitosdesegurançaeconsistência.
O banco de dados, principalmente o baseado no modelo relacional, é muito
utilizadoparaestefim. Paratanto,deve-seentendersuascaracterísticas,seus
conceitosefundamentos. Autilizaçãodosmétodosdearmazenamentoatra-
vés do uso de tabelas (linhas e colunas) garante seu armazenamento, bem
comoasregrasdefinidasparaomodelorelacional. AIntegridadereferencial
precisaserestudadaeanalisada. Aálgebrarelacional,quesetratadeumadas
técnicaspararecuperaçãodedadospelosmotoresdosbancosdedados,deve
serentendidaeoperadadeformaeficazparaalcançaroobjetivoesperado. E
porúltimo,masnãomenosimportante,deve-seconheceralinguagempadrão
de acesso a dados, a SQL, para o modelo relacional, a qual reúne as aborda-
gensdaslinguagensdedefinição,manipulaçãoecontroledosdados.

## Página 24

2.1. Introduçãoaobancodedadosrelacional CasadoCódigo
2.1 Introduçãoaobancodedadosrelacional
Banco de dados relacional pode ser visto como uma coleção de dados. Esses
dadosestãodisponibilizadosdeformaorganizadaeintegrados,armazenados
em forma de tabelas interligadas por chaves primárias e estrangeiras, cons-
tituindo uma representação de dados natural, podendo ser modificada sem
restrições. Alémdisso,obancopodeserutilizadoportodasasaplicaçõesre-
levantessemduplicaçãodedadosesemanecessidadedeseremdefinidosem
programas,maspodendoser,comocompostodetabelasourelações.
A abordagem relacional dos dados é baseada na observação de que ar-
quivos podem ser considerados como relações matemáticas. Consequente-
mente, a teoria elementar de relações pode ser usada para lidar com vários
problemaspráticosquesurgemcomosdadosdessesarquivos. Combaseem
EdgarF.Codd,oprincipalexpositordomodelodedadosrelacional,pode-se
dizerqueumdosrecursospoderososdomodelorelacionaléacapacidadede
permitir a manipulação de relações orientadas a conjuntos. Esta caracterís-
ticapossibilitouodesenvolvimentodepoderosaslinguagensnãoprocedurais
com base na teoria dos conjuntos (álgebra relacional) ou em lógica (cálculo
relacional). Em consequência disto, tabelas são tratadas como relações e as
linhasdessastabelassãousualmenteconhecidascomotuplas,que conforme
amaiorpartedaliteratura podeserdefinidacomolinhaouregistro.
Um banco de dados relacional tem como objetivo a implementação do
modelo de dados relacional, incorporando todas as características básicas
comorepresentaçãodeentidades,atributoserelacionamentos. Asentidades,
tambémchamadasdetabelas,sãoconstituídasporumconjuntodelinhasnão
ordenadas,astuplas. Cadalinhaquefazpartedatabelaéconstituídaporum
ou vários campos que são chamados de atributos da entidade. Vamos pegar
comoexemploatabelachamadaEMP,dobancodedadosqueseráusadoem
nossotreinamento:
10

## Página 25

CasadoCódigo Capítulo2. Bancodedados
Paraquehajaorelacionamentoentreasentidades,maisprecisamenteen-
tre as linhas de uma tabela, é preciso estabelecer o conceito de chaves. Os
tipos de chaves geralmente encontradas num banco de dados relacional são
três: chave primária (PKPrimary Key), chave estrangeira (FKForeign Key)
echavealternativa.
2.2 Chaveprimária(índiceprimário)
Trata-sedeumidentificadorúnicoparatabela. Quandoumacolunaoucom-
binações de coluna é instituída como chave primária, nenhum par de linhas
databelapodeconteromesmovalornaquelacolunaoucombinaçãodecolu-
nas. Umachaveprimáriadeveseguiroconceitodaminimalidade,istoé,que
todas as suas colunas sejam efetivamente necessárias para garantir o requi-
11

## Página 26

2.2. Chaveprimária(índiceprimário) CasadoCódigo
sitodeunicidadedevaloresdestachave. Portanto,quandoseconsegue,com
umatributo,garantiraunicidadedeumregistro,umsegundoatributocom-
pondoachaveédesnecessário. Quandoseconseguecomdois,umterceiroé
desnecessárioeassimpordiante. VoltemosàtabelaEMP:
Fig. 2.2: No caso da tabela EMP, existe apenas uma coluna definida como
chaveprimária(PKSimples). Portanto,agarantiadaunicidadedosdadosfoi
conseguidacomapenasumacolunadatabela,acolunaEMPNO.
12

## Página 27

CasadoCódigo Capítulo2. Bancodedados
Fig. 2.3: Neste caso foram necessárias mais de uma coluna (PK Com-
posta) para garantir a unicidade dos dados, as colunas EMPLOYEE_ID e
START_DATE.
2.3 Chaveestrangeira
Estachaveédeterminadaporumacolunaouumconjuntodecolunaspossui-
dorasdeumconjuntodevaloresválidosqueestãopresentesemoutratabela.
Para enfatizar este conceito, pode-se dizer que uma chave estrangeira é uma
coluna ou uma combinação de colunas, cujos valores aparecem necessaria-
mente na chave primária de outra tabela. A chave estrangeira pode ser vista
comosendoomecanismodeimplementaçãodorelacionamentoentretabelas
deumbancodedadosrelacional.
13

## Página 28

2.3. Chaveestrangeira CasadoCódigo
Fig.2.4: AstabelasDEPTeEMPpossuemsuascolunasdefinidascomochave
primária(EMPNOtabelaEMPeDEPTNOtabelaDEPT)eestãointerligadas
atravésdacolunaDEPTNO,queexistetantonatabelaDEPTquantonatabela
EMP. Esta ligação garante que um empregado só poderá ser atribuído a um
departamentoexistentenatabeladedepartamentos(DEPT).
Relacionamentos
Astabelas“conversam”entresiatravésderelacionamentos. Paraqueisso
sejapossível,éprecisoquehajainformações(colunas)quesejamcomunsen-
treastabelas. UmexemplotípicoéaexistênciadacolunaDEPTNOnatabela
de empregados. A ligação ou relacionamento entre as duas tabelas é reali-
zadoatravésdestecampo. Nafiguraanterior,existeumrelacionamentoentre
astabelasEMPeDEPT.
14

## Página 29

CasadoCódigo Capítulo2. Bancodedados
2.4 Chavealternativa
Vimos que existem princípios para a criação de chaves primárias. O princí-
pio da unicidade e o da minimalidade mostram que, embora se tenha várias
colunasquepodemfazerpartedachaveprimária(tambémchamadasdecha-
vescandidatas),namaioriadasvezesnãosefaznecessário,nemadequado,o
usodelasparagarantiraintegridade. Nomomentodaescolhadequalcoluna
deve ser usada, pode-se tomar como critério a escolha da coluna que se de-
seja usar nas chaves estrangeiras que referenciam a tabela em questão. Essas
chavescandidataspodemserutilizadascomoíndicessecundários,úteispara
acelerar operações de busca, embora nem sempre sejam eficazes. As chaves
alternativas podem ser definidas como sendo um identificador único, inclu-
sivesendoimplementadocomotalemumabasededados.
Fig. 2.5: A tabela EMPLOYEES tem como chave primária a coluna EM-
PLOYEE_ID e como chave candidata a coluna EMAIL. A coluna EMAIL só
conterávaloresúnicos,podendoserutilizadacomoparâmetroempesquisas
realizadasnestatabela.
15

## Página 30

2.4. Chavealternativa CasadoCódigo
Comrelaçãoaousodechavesestrangeiras,algumasregrasdevemserob-
servadas. Aexistênciadeumachaveestrangeiraimpõerestriçõesquedevem
sergarantidasaoexecutardiversasoperaçõesdealteraçãodobancodedados.
Vejaalgumasaseguir:
• Quandodainclusãodeumalinhanatabelaquecontémachavees-
trangeira: devesergarantidoqueovalordachaveestrangeiraapareça
nacolunadachaveprimáriareferenciada.
• Quandoaalteraçãodovalordachaveestrangeira: devesergarantido
queonovovalordeumachaveestrangeiraapareçanacolunadachave
primáriareferenciada.
• Quandodaexclusãodeumalinhadatabelaquecontémachavepri-
mária referenciada pela chave estrangeira:deve ser garantido que
nacolunachaveestrangeiranãoapareçaovalordachaveprimáriaque
estásendoexcluída.
• Quandodaalteraçãodovalordachaveprimáriareferenciadapela
chaveestrangeira: devesergarantidoquenacolunachaveestrangeira
nãoapareçaoantigovalordachaveprimáriaqueestásendoalterada.
Outro aspecto que deve ser observado é a possibilidade de haver uma
chaveestrangeiraqueestejareferenciandoachaveprimáriadaprópriatabela.
Quandoissoacontece,asoluçãosedápormeiodoautorrelacionamento,isto
é,aassociaçãoacontecenamesmatabela. Atabela-mãeeatabela-filhasãoa
mesmatabela. Valeressaltarqueumachaveestrangeira,sendoelaautorrela-
cionadaounão,podecontervaloresnulos.
16

## Página 31

CasadoCódigo Capítulo2. Bancodedados
Fig. 2.6: Todos os empregados da tabela EMP possuem um identificador
(EMPNO). Entretanto, há outros que, além deste código, também possuem
outro identificador que define quem é seu gerente. Neste exemplo, pode-
mos perceber que o empregado ALLEN tem como gerente (MGR) o tam-
bém empregado BLAKE. Neste nosso modelo, o autorrelacionamento acon-
tece quando um empregado tem como gerente um empregado também ca-
dastrado na mesma tabela, recebendo assim um código que existe na coluna
EMPNO.
Quando se fala no uso de chaves, surge outro ponto importante, que é
sobre o conceito deregras de integridade. O modelo relacional de banco
dedadosprevêduasregrasgeraisdeintegridade. Sãoconhecidascomointe-
gridade de entidade e integridade referencial. De modo genérico, essas duas
regras são aplicáveis a qualquer banco de dados que venha a implementar o
modelorelacional.
17

## Página 32

2.5. Integridadedeentidade CasadoCódigo
Seosdadosdeumbancodedadosestãoíntegros,issosignificadizerque
eles refletem corretamente a realidade representada pelo banco de dados e
que são consistentes entre si. A integridade visa proteger os dados de um
banco provendo sua segurança e integridade para que as informações sejam
armazenadas de forma adequada. Com relação aos dois tipos de regras de
integridade,pode-sedizerque:
2.5 Integridadedeentidade
U ma t r i b u t o ,q u ef a zp a r t ed eu m ac h a v ep r i m á r i ae mu m ar e l a ç ã o ,n ã op o -
derá conter valores nulos, ou seja, ausência de informação. Outra caracte-
rística importante da integridade de entidade diz respeito aos dados que são
armazenados,poisosvalorescontidosnoscamposdechaveprimáriadevem
serúnicos,nãohavendoduplicidadededados.
2.6 Integridadereferencial
Esta integridade se trata de uma restrição que fixa que os valores que estão
contidos em um campo de chave estrangeira devem, por sua vez, aparecer
noscamposdechaveprimáriadatabelareferenciada. Suaprincipalfunçãoé
garantirqueasreferências(ligações)entreasrelações,relacionamentosentre
tabelas,estejamcompatíveis.
18

## Página 33

CasadoCódigo Capítulo2. Bancodedados
Fig. 2.7: A figura mostra com clareza as conexões existentes entre as tabelas
LOCATIONS,JOBS,JOB_HISTORY,entreoutras,atravésdaschavesestran-
geiras. Estas ligações garantem que os dados armazenados estejam consis-
tentes e confiáveis. Trata-se de um exemplo, onde são mostradas as chaves
primáriaseestrangeirasexistindoentreastabelas.
Paraqueasregrasdeintegridadesejamaplicadasdeformaeficaz,éneces-
sário que haja um sistema que as gerencie. Neste momento, entra em jogo o
SGBD(SistemadeGerenciamentodebancodedados). Umdosobjetivospri-
mordiaisdeumSGBDéaintegridadededados. Todasasregrasderestrição
existentes aplicáveis a um banco de dados são controladas por este sistema,
ouseja,elegarantequeaselassejamaplicadasdeformaamanterconsistentes
19

## Página 34

2.6. Integridadereferencial CasadoCódigo
osdados. Deformasucinta,pode-sedizerqueosistemadegerenciamentodo
bancodedados(tambémpodendoserchamadodeDBMS )éoso ftwa r eq ue
controla e manipula todos os acessos ao banco de dados. Alguns benefícios
dosSGDBssãoosseguintes:
• Simplicidadeeuniformidade(omodelorelacionalécompacto);
• Independênciatotaldosdados(benefíciomaisimportante);
• Interfacesdealtonívelparausuáriosfinais;
• Visõesmúltiplasdedados;
• M elho riadodiálogoen tr eoCPDeousuário;
• Melhorianasegurançadosdados;
• Reduçãosignificativadoatravancamentodeaplicaçõesedotempo;
• Gastosnamanutenção;
• AlíviodacargadetrabalhodoCPD;
• Possibilidade de crescimento futuro e inclusão de novos dados devido
àflexibilidadedosistemaeindependênciadedadosfísicos.
OsSGBDsseguemtambémprincípiosqueoscaracterizamcomoumsis-
temadegerenciamentodebancosdedadosrelacionais. Em1970,E.F.Codd,
matemático da IBM já mencionado anteriormente, publicou um artigo inti-
tuladocomo“Ummodelorelacionaldedadosparagrandesbancosdedados
compartilhados”,contendoosprincíp ios,ouregras,quedefinemumsistema
degerenciamentodebancosdedadoscomosendoumsistemarelacional. São
asqueseguem:
• Regra 1 :todas as informações em um banco de dados relacional
são representadas de forma explícita no nível lógico e exatamente em
apenasumaforma,ouseja,porvaloresemtabelas.
20

## Página 35

CasadoCódigo Capítulo2. Bancodedados
• Regra2: cadaumequalquervalorindividual(atômico)emumbanco
dedadosrelacionalpossuiagarantiadeserlogicamenteacessadopela
combinaçãodonomedatabela,novalordachaveprimáriaedonome
dacoluna.
• Regra3: valores nulos devem ser suportados de forma sistemática
e independente do tipo de dados usado para representar informações
inexistenteseinformaçõesinaplicáveis.
• Regra4: a descrição do banco de dados é representada no nível ló-
gico da mesma forma que os dados ordinários, permitindo aos usuá-
rios autorizados que utilizem a mesma linguagem relacional aplicada
aosdadosregulares.
• Regra5: umsistemarelacionalpodesuportarváriaslinguagensevá-
riasformasderecuperaçãodeinformações,entretanto,devehaverpelo
menosumalinguagem,comoumasintaxebemdefinidaeexpressapor
conjuntos de caracteres, que suporte de forma compreensiva todos os
seguintes itens: definição de dados, definição de “views”, manipulação
de dados (interativa e embutida em programas), restrições de integri-
dade,autorizaçõeselimitesdetransações(begin,commiterollback).
• Regra6: todas as “views”, que são teoricamente atualizáveis, devem
sertambématualizáveispelosistema.
• Regra 7 :a capacidade de manipular um conjunto de dados (rela-
ção)atravésdeumsimplescomandodeve-seentenderasoperaçõesde
inclusão,alteraçãoouexclusãodedados.
• Regra8: programas de aplicação permanecem logicamente inalte-
rados quando ocorrem mudanças no método de acesso ou forma de
armazenamentofísico.
• R e g r a9:mudanças nas relações e nas “views” devem provocar o
mínimoimpactopossívelnasaplicações.
• Regra 10 :as aplicações não podem ser afetadas quando ocorrem
mudançasnasregrasderestriçõesdeintegridade.
21

## Página 36

2.6. Integridadereferencial CasadoCódigo
• Regra11: as aplicações não podem ser logicamente afetadas quando
ocorremmudançasgeográficasnosdados.
• Regra12: se um sistema possui uma linguagem de baixo nível, essa
linguagem não pode ser usada para subverter as regras de integridade
erestriçõesdefinidasnonívelmaisalto.
Alémdestasregras,Coddtambémdescreveuumaálgebrarelacionalfun-
damentandoestesistemadegerenciamentodebancodedadosrelacional.
22

## Página 37

Capítulo3
IntroduçãoàlinguagemSQL
AS Q L(Structured Query Language) é uma linguagem para interface com
bancos de dados relacionais, isto é, todos os usuários e programas que de-
sejaremrealizaralgumatarefanobancodedadosdevemfornecercomandos
escritos nesta linguagem. Existem inúmeras versões de SQL, mas a versão
original foi desenvolvida no laboratório de pesquisa da IBM San Jose (atual-
mente Centro de Pesquisa Almaden). No início, por volta de 1970, foi cha-
madadeSEQUELedepoisonomefoimudadoparaSQL.AlinguagemSQL
foidesenvolvidaparaserusadasegundoomodelodeCoddepermaneceaté
hojecomoalinguagempadrãoparabancodedadosrelacionais. Em1986,foi
estabelecidoumpadrãopeloANSI(AmericanNationalStandardsInstitute )o
chamado SQL1. Com o tempo, foram aparecendo outras necessidades e fo-
ram atribuídas outras funcionalidades à linguagem, sendo criado o padrão
SQL2. Atualmente, a linguagem SQL está no padrão SQL3, cujas principais
inovações são a criação de funções, regras, procedimentos, armazenamento

## Página 38

CasadoCódigo
deimagensesonsemtabelas,disparadoresdeeventos(gatilhos),armazena-
mentodecódigosemJava,entreoutras.
A SQL inclui, em suas fundamentações, as operações da álgebra relacio-
nal. Por exemplo: em SQL, tem-se o comandoSELECT q u ef a zop a p e ld o
operadordeProjeçãoemálgebrarelacional. Jáoscomandos FROMe WHERE
da linguagem SQL funcionam como referência aos operadores de Produto
cartesiano e de Seleção, respectivamente. O nascimento da linguagem SQL
deveu-se à necessidade de executar as operações relacionais, incluindo Di-
ferença, Divisão, Intersecção, Junção, Produto cartesiano, Projeção e União.
Esta linguagem é flexível e economiza tempo. Praticamente todos os for-
necedores de SGBDR (Sistema Gerenciador de Banco de Dados Relacional)
oferecem ferramentas de 4ª Geração (4GL) que estão aptas a trabalhar com
estalinguagem,comaqualpodemrealizarrepetidostesteseposteriormente
incluí-losemcódigosdeaplicativos.
ComrelaçãoàabrangênciadalinguagemSQL,pode-sedizerqueelapos-
sui inúmeras funcionalidades, dentre as quais está a gama de comandos que
possui–Comandosdemanipulação,ComandosdedefiniçãoeControle.
Linguagem de Definição dos Dados (Data Definition Language
DDL)
Esta parte da SQL descreve como as tabelas e outros objetos podem ser
definidos. Oscomandosdalinguagemdedefiniçãodedados(DDL)sãores-
ponsáveis por definir tabelas e outros objetos pertencentes ao banco dados.
Dentre os principais comandos da DDL estão:
CREATE TABLE , CREATE
INDEX, ALTER TABLE , DROP TABLE , DROP VIEW E DROP INDEX .
LinguagemdeManipulaçãodosDados(DataManipulationLan-
guage–DML)
Esta parte da SQL possui comandos para que os usuários façam acesso e
armazenamento dos seus dados. Fazem parte da DML os seguintes coman-
dos:
INSERT, DELETE, UPDATE, SELECTE LOCK.
LinguagemdeControledosDados(DataControlLanguage DCL)
Para finalizar, temos a DCL, que é subdividida em três grupos de co-
24

## Página 39

CasadoCódigo Capítulo3. IntroduçãoàlinguagemSQL
mandos: comandos para controle de transação, sessão e sistema. Para os
comandos de controle, podem-se citar os mais usados, que são:COMMIT,
ROLLBACK, GRANTe REVOKE.
QuempodeutilizaraLinguagemSQLequaissuasvantagens?
A linguagem SQL pode ser usada por aqueles que necessitam se comu-
nicar com bancos de dados relacionais. Trata-se de uma linguagem flexível,
simples, mas ao mesmo tempo completa e de simples interpretação. Possui
grandes recursos para as mais variadas operações envolvendo manipulação
de dados. É de fácil escrita e leitura, pois permite a compreensão das instru-
ções mesmo para aqueles que possuem pouco conhecimento nesta lingua-
gem. Contudo, embora pareça simplória, seu poderio garante sua utilização
pelosmaioresbancosdedadosdomercado.
3.1 OracleCorporationeBancodedadosOra-
cle
Em 1977, a empresa Software Development Laboratories (SDL) foi formada
porLarryEllison,BobMiner,EdOateseBruceScott. LarryeBobvieramda
Ampex,ondeestavamtrabalhandoemumprojetodaCIAapelidadode“Ora-
cle”. ACIAfoiseuprimeirocliente,emboraoprodutoaindanãotivessesido
lançado comercialmente. A SDL mudou seu nome para Relational Software
Inc. (RSI)noanode1978e,em1979,colocouaprimeiraversãocomercialdo
software,quefoivendidaàbasedaForçaAéreaemW right-Patterson.Essefoi
oprimeiroRDBMScomercialnomercado. Depoisdisso,em1982,aRSImu-
dou seu nome para Oracle Systems Corporation (OSC), que posteriormente
foi simplificado para Oracle Corporation. Em poucos anos, a Oracle se tor-
noulíderembancosdedadosrelacionais.
Uma grande característica deste SGDBR é a integração no mercado da
tecnologia da informação, acompanhando as novidades que vêm surgindo,
comoainclusãodemultimídia,CAD/CAM,gráficos,textos,desenhos,foto-
grafias, som e imagem. Além disso, contempla desenvolvimentos voltados à
programação orientada a objetos e banco de dados semânticos. Implementa
a linguagem SQL, inclusive incorporando as modificações realizadas no pa-
25

## Página 40

3.1. OracleCorporationeBancodedadosOracle CasadoCódigo
drãoSQL3,anovaversãoaprovadapelaANSI,comotambémsualinguagem
própria, voltada a procedimentos, PL/SQL. Seu teor é constituído de vários
componentes, como gerador de aplicação, dicionários de dados, gerador de
relatório, planilhas eletrônicas, pré-compiladores para linguagens hospedei-
ras,utilitários,ferramentasdemodelagem,gráficos,cálculosestatísticosear-
mazenagemdedadosdeváriostipos(data,valoresnuméricoscomesemde-
cimais,caracteresvariáveisoufixos,binários,imagens,textos,sons).
O SGDBR da Oracle pode ser usado em vários tipos de equipamentos,
sendo eles computadores de pequeno e grande porte. Quanto à plataforma,
dásuporteaumagamadeambientesincluindo,UNIX,VMS,MVS,HP,Ma-
cintosh,RedeNovell,MS-Windowsentreoutros. Possuicompatibilidadecom
outrosSGDBRs,taiscomo,DB/2eSQL/DSdaIBM,Sybase,Ingres,Informix,
e outros não relacionais como SAS, lipper, Lotus etc. Outras características
relacionaissão:
• Controlesofisticadodeconcorrências;
• S u po rteto talparavisõesejunções;
• Consistênciagarantidanaleituradedados;
• Otimizaçãodeconsultasavançadasbaseadasemcusto;
• Transaçõesdemultietapasgarantidascontrafalhas;
• Recuperaçãoautomáticacontraquebrasoufalhasdecomputador;
• Indexaçãodinâmica;
• Pesquisasdistribuídas;
• Junçõesexternas( outer joinsinexistentesemoutrosSGBDRDs);
• Funçõeslógicasdetextos;
• UsuárioseSCHEMAS;
• Índices,clustersehash clusters;
• Sequências;
26

## Página 41

CasadoCódigo Capítulo3. IntroduçãoàlinguagemSQL
• Procedimentos,pacotesetriggers;
• Sinônimos,papéiseprivilégios;
• Segmentosde Rollback;
• Snapshotsevisõesmaterializadas.
No que diz respeito à segurança, o banco de dados Oracle não deixa a
desejar,poisoaltograudedesempenho,portabilidadeeinteroperabilidadeo
transformaemlídermundialemseusegmento. Aintegridadeeconsistência
permitemqueusuáriosconstruamsistemasseguros,confiáveisecomaltadis-
ponibilidade de recursos. Algumas características relacionadas à segurança
são:
• Suportemultinivelar;
• Integridadededados;
• Disponibilidadeetolerânciaafalhas;
• Administraçãodeprivilégios;
• Administraçãodasegurança;
• Altodesempenho;
• Suporteamigração;
• Controledeconcorrência;
• SuportedesegurançamultinivelaraBDdistribuído;
• Suporteapadrõesinternacionais.
Atualmente, aversãodobancodedadosencontra-sena11g, sendoa9ie
10g as mais difundidas no mercado. A Oracle também disponibiliza outros
produtos,quetêmcomoobjetivoauxiliarosusuáriosnasmaisdiversasáreas
denegócio.
27

## Página 42

3.2. ComunicandocomobancodedadosOracle CasadoCódigo
3.2 ComunicandocomobancodedadosOracle
A ferramentaSQL*Plus acompanha o banco de dados Oracle quando ele é
instalado. Elatemaresponsabilidadedefazeracomunicaçãoentreousuário
eobancodedados. Aoseracionada,éapresentadaumateladeidentificação
onde devem ser informados o nome do usuário, senha e astring de conexão
comobancodedadoscomoqualdesejaseconectar.
SuafinalidadegeraléaexecuçãodecomandosSQL,códigoPL/SQL,pro-
cedimentos(procedures),gatilhos( triggers)efunções( functions). Ainterface
destaferramentaésemelhanteaopromptdoMS-DOS,poisdisponibilizaum
promptqueficaesperandoaentradadeumainstrução. Elatambémapresenta
algumas informações, como, por exemplo, a versão programa e a versão do
bancodedadosOracleconectado.
28

## Página 43

CasadoCódigo Capítulo3. IntroduçãoàlinguagemSQL
Fig.3.2: ExemplodateladoSQL*Plus
Comonamaioriadasferramentas,existemdiversasconfiguraçõesdevi-
sualização de instruções e resultados, como formatação de linhas, colunas,
páginas, comandos para mostrar informações sobre a execução do código,
entreoutras. Alémdisso,háumasériedecomandosquesãoúteisparaama-
nipulaçãodestasinstruções:
• EditarocomandoSQLarmazenadono buffer;
• Formatarosresultadosretornadospelobancodedados;
• ArmazenaroscomandosdeSQLparadiscoerecuperá-losparaexecu-
ção;
• ModificaromododetrabalhardoSQL*Plus;
• Enviarmensagensereceberrespostasdeoutrosusuários;
• Listaradefiniçãodequalquertabela;
• Fazeracessoecopiardadosentrebancodedados.
Nasequência,vejaumexemplodeumainstruçãodigitadaeexecutadado
SQL*Plus:
29

## Página 44

3.3. Escopodousuário CasadoCódigo
Existemoutrasferramentascominterfacesmaisamigáveisdisponibiliza-
daspelaOracleparafazerestetrabalhocommaisrapidezutilizandooutrosre-
cursos,como,porexemplo,aferramentaSQLDeveloper. Outrasferramentas
de terceiros que também possuem muitos recursos são SQLTools (Free Soft-
ware),Toad(FreeSoftware),SQLNavigatorePL/SQLDeveloper(necessitam
delicença).
3.3 Escopodousuário
Para se ter acesso ao banco de dados Oracle são necessários um usuário e
uma senha. Se você não estiver acessando o banco através do usuário admi-
nistradordobancodedados,quefoiconfiguradonomomentodainstalação
dobanco,ocadastroteráobrigatoriamentequeserfeitoparaquevocêtenha
acesso.
GeralmenteéoDBA(DatabaseAdministrator )quemcriaosusuáriosque
30

## Página 45

CasadoCódigo Capítulo3. IntroduçãoàlinguagemSQL
poderãoteracessoaobancodedados,masnadaimpedequevocêoscrie ape-
sardenãoserrecomendadoquandoestamosfalandodebancosdeprodução.
Deixe esta tarefa para o DBA. Ele é o administrador do banco e não só cria
os usuários como também garante o acesso aos objetos e recursos dos quais
precisamosparaoperarobanco. Opapeldesteprofissionalémanterobanco
emperfeitaordemefuncionandoadequadamente.
Tendoousuárioesenhadevidamentehabilitadosecompermissõespara
acessoaobancodedados,bastaescolheraferramentaeefetuarologin.
Ao conectarmos a um banco de dados através de uma das ferramentas
mencionadas anteriormente, iniciamos uma sessão dentro dele. Quando so-
licitamosestaconexão,obancodedadosabreumasessãoondesomenteeste
usuário terá acesso a esta área. Agregado ao usuário também existe uma es-
trutura chamada de
SCHEMA, onde todas suas configurações e todos os ob-
jetos que foram criados para ele estão disponíveis para acesso, ou seja, esses
objetoseconfiguraçõestêmumdono,quedentrodobancodedadosOracleé
chamadode
OWNER.Éóbvioque,sevocêacaboudecriarumusuário,muito
provavelmenteelenãodeverápossuirnenhumobjetocriado.
Se um usuário cria um objeto no banco de dados, este objeto pertence a
ele. Destaforma,somenteeleteráacessoaesteobjeto,amenosqueelemesmo
dê acesso a outros usuários do banco de dados. Sim, isso pode ser feito, e é
muitocomumdeacontecer.
Quando falamos em objetos, referimo-nos a tabelas, packages, triggers,
procedures,functionsetc. Nocasodastabelasquecontêmosdados,osusuá-
rios com acesso a estes objetos também poderão acessar os dados contidos
nelas.
Emgrandessistemascorporativosvemosmuitoistoacontecer. Porexem-
plo, temos várias tabelas correspondentes a diversos módulos dentro do sis-
t em a.T em osom ód ulodeRH,om ód ulodeco n ta sapa ga r ,co n ta sar ece ber
e assim por diante. Podemos ter criado no banco de dados um usuário para
cada módulo e, através deste usuário, dar acessos a estes objetos aos outros
usuários (módulos) do sistema ou, ainda, para outro usuário principal, di-
gamos assim, o qual iniciará nosso sistema. Ou seja, podemos ter um único
usuárioresponsávelporacessarosobjetosqueestãocriadosemoutrosusuá-
rios.
31

## Página 46

3.4. Transações CasadoCódigo
OSGDBOracleémuitoflexíveleíntegroquandosetratadamanipulação
de dados e seus SCHEMAS de usuário. Outro ponto interessante é que os
dadosquedisponibilizarmospodemserrestringidosatalpontoque,seassim
quisermos, outros usuários só poderão ter acesso de leitura, não podendo
fazerqualqueralteração.
Para que esta manipulação de dados aconteça sem problemas, visando a
integridade das informações e garantindo o ótimo funcionamento do banco
dedadoseprogramasconectadosaele,obancoOracletrabalhacomtransa-
ções. Nopróximotópico,vamosveroquesignificaumatransação.
3.4 Transações
Primeiramente,antesdecomeçarmosatrabalharcombancosdadosOracle,é
precisoconheceroconceitodetransação. Umadascaracterísticasmaisbem-
vindasdosbancosdedadosCliente/Servidor,emrelaçãoaosbancosdedados
desktop,éoconceitodetransações. Umatransaçãoéumaunidadelógicade
trabalhocompostaporumaoumaisdeclaraçõesda Data ManipulationLan-
guage(DML)ou DataDefinitionLanguage (DDL).Oscomandosparaocon-
troledatransaçãosãooscomandosnecessáriosparaquesepossacontrolara
efetivaçãoounãodasmodificaçõesfeitasnobancodedados. Paraexplicaro
queéumatransação,pode-setomarcomoexemploumatransferênciabancá-
rianaqualumdeterminadovalorétransferidoparaoutraconta. Oprocesso
de transferência deste valor consiste em vários passos, que são agrupados de
modoque,senãoforemconcluídosemsuatotalidade,ouseja,seatransação
nãochegaratéofinal,todasasoutrasalteraçõesjárealizadasserãodescarta-
das e a conta voltará ao seu estado anterior, como se nenhuma transferência
tivesse sido realizada. Através deste controle, pode-se garantir que os dados
permanecerão consistentes. Os comandos
COMMIT e ROLLBACK da DCL
auxiliamnestetrabalho.
COMMIT
Torna permanentes todas as alterações feitas no banco de dados durante
asessão. Todasasalteraçõesrealizadasemumadeterminadatransaçãoserão
confirmadascasoestecomandosejaaplicado.
32

## Página 47

CasadoCódigo Capítulo3. IntroduçãoàlinguagemSQL
Neste exemplo, é mostrada atualização do cargo referente ao empre-
gado TURNER, e logo após, a efetivação da atualização através do comando
COMMIT.
ROLLBACK
Usado para remover todas as alterações feitas desde o últimoCOMMIT
durante a sessão. Esse comando vai restaurar os dados ao lugar onde eles
estavam no últimoCOMMIT. Alterações serão desfeitas caso a transação seja
encerradapelocomando ROLLBACK.
33

## Página 48

3.4. Transações CasadoCódigo
Jánesteexemplo, temosaexclusãodecincolinhasreferentesaosempre-
gadosquetrabalhamnodepartamento20. Contudo,logoapósaexclusão,foi
executadoum ROLLBACK,an ulandoaação .
NoOracle,umatransaçãoseiniciacomaexecuçãodaprimeirainstrução
SQL e termina quando as alterações são salvas ou descartadas. O comando
34

## Página 49

CasadoCódigo Capítulo3. IntroduçãoàlinguagemSQL
SET TRANSACTION também inicia uma transação – transação explícita. O
uso do comandoSET TRANSACTION determina algumas regras, listadas a
seguir.
• Deve ser o primeiro comando da transação (caso contrário, ocorrerá
umerro);
• Somenteconsultassãopermitidasnatransação;
•U m COMMIT, ROLLBACK ou qualquer outro comando de DDL (pos-
suem COMMITS implícitos) encerram o efeito do comando SET
TRANSACTION.
35

## Página 50

3.5. DicionáriodedadosdoOracle CasadoCódigo
3.5 DicionáriodedadosdoOracle
O banco de dados Oracle é muito robusto e sua gama de parametrizações,
estruturas e arquiteturas requer uma organização para que tudo possa ocor-
rer de forma harmônica, e para que tanto o banco de dados quanto nós que
trabalhamoscomelepossamosacharasinformaçõesquandonecessitamos.
Paraqueissoaconteça,todasasinformaçõessobreosobjetosestãograva-
dasemtabelasqueformamochamadodicionáriodedados . Estedicionário
é fundamental para que o banco de dados possa operar de forma adequada.
Aestruturadodicionárioébastantecomplexa,porissoexistemvisõesdodi-
cionário com nomes e estruturas mais legíveis para que possamos utilizá-las
para recuperar informações pertinentes ao banco de dados. Existem cente-
nasdessasvisões. Comtodacerteza,trata-sedeumSGBDmuitocompletoe
estruturadodeformaaseadequaraosmaisdiferentestiposdenegócio.
Cuidado!
As informações no dicionário de dados são mantidas por comandos
SQL. Porexemplo, CREATE TABLE EMPLOYEES atualiza astabelas do
dicionário, de modo que a visãoUSER_TABLES apresente as informa-
ções sobre a nova tabela. Nunca insira ou altere diretamente as tabelas
do dicionário: isto invalida o banco de dados, corrompendo totalmente
abasededados. Obviamentenãoéqualquerusuárioquepodealteraro
dicionáriomas,sevocêforumDBA,teráacessototal.
V ejaalgumasdasvisõesmaisusadaspelousuário:
• DICTIONARY:mostratodasasvisõesquecompõemodicionáriode
dados;
• USER_TABLES: mostraastabelasdasquaisousuárioédo no;
• ALL_TABLES: mostraastabelasàsquaisousuáriotemacesso;
• USER_TAB_COLUMNS: mostratodasascolunasdefinidasnastabe-
lasdasquaisousuárioédo no;
36

## Página 51

CasadoCódigo Capítulo3. IntroduçãoàlinguagemSQL
• ALL_TAB_COLUMNS: mostratodasascolunasdefinidasnastabelas
àsquaisousuáriotemacesso;
• ALL_OBJECTS/ALL_SOURCE: mostratodososobjetosaosquaiso
usuário tem acesso. Alguns deles são:TABLES, VIEWS, PACKAGES,
PROCEDURES, FUNCTIONS, CLUSTERSetc. Ostiposdeobjetopodem
m udarco nfo rmeaversãodobanco .
Além destas, ainda temos visões com informações sobre índices (tabelas
ecolunas), VIEWS, CONSTRAINTS, TABLESPACESetc.
Neste exemplo, temos a execução da viewUSER_TABLES, que mostra
todasastabelaspertencentesaousuáriologado.
37

## Página 52

3.6. ComooOracleexecutacomandosSQL CasadoCódigo
3.6 ComooOracleexecutacomandosSQL
ExistemváriasformasdeseexecutardeclaraçõesDML.OOracle,atravésdo
Optimizer, escolhe a forma mais eficaz para fazer isto. O Optimizer é o pro-
grama otimizador do banco de dados Oracle, que é responsável pela melhor
escolha possível para executar um comando SQL. Mas não vamos nos ater
aqui a explorar suas funcionalidades e capacidades (que são muitas, diga-se
depassagem). Oqueéinteressanteentendersãoospassosdaexecuçãodeum
comandoSQL.
QuandoseexecutaumcomandoSQLemumbancodedados,trêsetapas
são executadas, sendo elas:
PARSE, EXECUTE e FETCH.E mc a d ae t a p a ,o
Oracledefinetarefasquedevemserseguidasparaqueoresultadosejaobtido.
PARSE
Aprimeiratarefadestaetapaéverificarasintaxedocomandoevalidara
semântica.
D e p o i s ,éav e zd ep e s q u i s a rs ee s t ec o m a n d oj áf o ie x e c u t a d oa n t e r i o r -
mente,encontrando-senamemória. Seexistir,oplanodeexecuçãojáestará
traçado, tendo em vista que o comando já foi analisado e executado antes.
Seforconstatadaaexistência,serápassadodiretoparaafase
EXECUTE,não
r epetindoao u trasações.
Casonãosejaencontradonamemória,oOracleverificanodicionáriode
dados a existência das tabelas e colunas envolvidas no comando, bem como
aspermissõesdeacessoaestesobjetos.
Após a pesquisa, o otimizador poderá traçar o caminho de acesso para
cadatabelapresentenocomando,montandoumplanodeexecução(também
chamado de
PARSE TREE ) para obter e/ou atualizar os dados referentes à
requisiçãofeitaatravésdestecomando.
Tendo o plano montado, o Oracle o inclui em memória para que a exe-
cução seja realizada e para que este plano seja utilizado por outro comando
idênticoaoatual.
EXECUTE
Aprimeiratarefado EXECUTEéaplicaroplanodeexecução. Comisto,a
38

## Página 53

CasadoCódigo Capítulo3. IntroduçãoàlinguagemSQL
leituradosdadosseráfeitadeformafísicaoulógica,dependendodasualoca-
lizaçãoemdiscoouemmemória. Seestiveremmemória,nãoseránecessário
fazer qualquer acesso a disco. Caso contrário, a leitura é feita, e o retorno é
armazenadonaáreadememóriadobancodedados.
Já com os dados em memória, será realizada a análise das restrições que
consiste em verificar as regras de integridade (
CONSTRAINTS). Esta tarefa é
aplicadaaprocessosdeatualização.
Comoaanterior,estatarefatambémsóéaplicadaemprocessosdeatua-
lização, sendoqueéprecisobloquearaslinhasdedados( LOCKED),alocaro
segmentode ROLLBACK,paraqueaatualizaçãodaslinhassejarealizada.
FETCH
SeforocasoemqueocomandoSQLexecutadoforum SELECT,oOracle
retornaasinformações.
39

## Página 55

Capítulo4
ExecutandocomandosSQLcom
SQL*Plus
4.1 OqueéSQL*Plus?
ÉumaferramentadisponibilizadapelaOraclequefuncionacomoumprompt
decomandoparaexecuçãodecomandosSQLePL/SQL.Suasprincipaisfun-
cionalidadessão:
• ProcessamentoonlinedecomandosSQLque:
– Definemaestruturadebasededados;
– Realizamconsultas ad-hocàbasededados;
– Manipulamasinformaçõesarmazenadasnabasededados.

## Página 56

4.2. ComandosdeediçãodoSQL*Plus CasadoCódigo
• FormataçãodelinhasecolunasrecuperadasporumaconsultaSQL.
• EdiçãodecomandosSQLatravésdeumeditordelinhas built-inoude
seueditordetextosfavorito.
• Armazenamento,recuperaçãoeexecuçãodecomandosSQLem/dear-
quivos.
Nasequência,veremoscomandosdoSQL*Plusquesãoutilizadosparaa
manipulaçãodecomandosSQLnestaferramenta.
4.2 ComandosdeediçãodoSQL*Plus
Os comandos de edição têm o objetivo de modificar a informação armaze-
nada no SQL Buffer. Estes comandos afetam apenas uma linha de cada vez,
istoé,aediçãoéfeitalinhaalinha. Ficaguardadonobuffersempreoúltimo
comandoSQLexecutado. OscomandosdeediçãonãoficamnoBuffer.
Quando listamos o conteúdo do SQL Buffer, o SQL*Plus mostra do lado
esquerdo do texto (ao lado da numeração) um asterisco em uma das linhas,
indicando que se trata da linha corrente, ou seja, da linha apta para modifi-
cação. Destaforma,qualquercomandodeediçãoqueviermosafazerafetará
apenasalinhacorrente.
L-IST
EstecomandotemafinalidadedelistarumaoumaislinhasdoSQLBuffer.
Aúltimalinhalistadapelocomandosetornaráalinhacorrente.
SQL> list
select * from DEPT
SQL>l
select * from DEPT
SQL>
A-PPEND
Com este comando, podemos adicionar um trecho de texto ao fim da li-
nhacorrente.
42

## Página 57

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
SQL>a where rownum < 10
select * from DEPT where rownum < 10
C-HANGE
Este comando de edição tem o objetivo de substituir parte do texto (ou
todo)poroutro.
Observe que os separadores apresentados são iguais. Podemos utilizar
qualquer caractere especial não presente nos textos, porém, dentro de um
comando,sópodemosusarumdeles.
SQL>l
select * from DEPT where rownum < 10
SQL> c/10/20
select * from DEPT where rownum < 20
DEL
Exclui uma determinada linha da área do SQL Buffer. Caso não sejam
informadosparâmetrosqueindiquemalinhaaserremovida,seráexcluídaa
linhacorrente.
SQL>l
select *
from DEPT
where rownum < 20
SQL>del 3
SQL>l
select *
from DEPT
SQL>
I-NPUT
Estecomandoadicionaumaoumaislinhasapósalinhacorrente(noSQL
Buffer). Estecomandodiferedocomando Appendumavezquepodevoltar
aoestadodedigitação,abrindoumanovalinhaparadigitaçãoimediatamente
apósalinhacorrente.
43

## Página 58

4.2. ComandosdeediçãodoSQL*Plus CasadoCódigo
SQL>l
select *
SQL>i from DEPT
SQL>l
select *
from DEPT
SQL>
ED-IT
EstecomandoacionaumeditorregistradonoWindowsepassacomopa-
râmetroonomedeumarquivoouotextopresentenoSQLBuffer ,deacordo
comocomandoexecutado.
Quandoomitimosonomedoarquivoasereditado,oSQL*Plusacionao
edi to rdosistemapassandoco moparâmetr ootextodoSQLBuffer .
Quando desejamos editar um determinado arquivo, seu nome pode ser
informadocomousemaextensão. AextensãodefaultéSQL.
R-UN
Este comando envia o conteúdo do SQL Buffer para o banco de dados e,
aomesmotempo,apresentanovídeoaslinhasenviadas(listaoSQLBuffer).
SQL>r
select ENAME from EMP where rownum < 3
ENAME
----------
SMITH
ALLEN
/(BARRA)
Quandodigitamosumabarranalinhadeprompteemseguidateclamos
Enter, o SQL*Plus envia o conteúdo do SQL Buffer para o banco de dados,
porém não apresenta o texto enviado, isto é, não lista o SQL Buffer. Esta é a
diferençaentreocomando Runeabarra.
SQL>/
44

## Página 59

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
ENAME
----------
SMITH
ALLEN
EXIT/QUIT
Oscomandos EXITe QUITsãoequivalentesetêmafinalidadedeencer-
rarasessãodoSQL*Plus. Istosignificaqueaconexãocomobancodedados
e,simultaneamente,opróprioprogramaserãoencerrados.
Quando digitamos apenasQUIT (ou apenas EXIT) ,ot é r m i n od op r o -
grama é considerado normaleac o nexão se encerra também normalmente
com COMMIT.
DESC-RIBE
Este comando tem a finalidade de apresentar a definição de um objeto
criado na base de dados Oracle. O objeto pode ser umaTABLE, VIEW,
SYNONYM, FUNCTION, PROCEDUREou PACKAGE.
SQL> DESC BONUS
Name Null? Type
------------------------------- -------- ----
ENAME VARCHAR2(10)
JOB VARCHAR2(9)
SAL NUMBER
COMM NUMBER
SQL>
SAVE
EstecomandosalvaoconteúdodoSQLBufferemumarquivodosistema
operacional.
SQL>l
select ENAME from EMP where rownum < 3
SQL> save EMPREGADOS. sql
45

## Página 60

4.2. ComandosdeediçãodoSQL*Plus CasadoCódigo
Created file EMPREGADOS. sql
SQL>
GET
ArecuperaçãodeumtextoparaoSQLBufferéfeitapormeiodocomando
GET.TodooconteúdodoarquivoécopiadoparaoSQLBuffer,portanto,este
ar quivodeveco n tera penasumco mando .
SQL> get EMPREGADOS.sql
select ENAME from EMP where rownum < 3
SQL>
ST AR-T/@
Estecomandoexecutaoconteúdodeumarquivodecomandosexistente
no sistema operacional. Cada comando de SQL ou de SQL*Plus é lido e tra-
tado individualmente. Em um arquivo executado porStart, podemos in-
cluirdiversoscomandosdeSQL.
Oc o m a n d o@ é sinônimo deStart eo @@ é semelhante, com a dife-
rençadeque,seestecomandoforincluídoemumarquivodecomandos,ele
pesquisará o arquivo associado no diretório do arquivo executado e não no
diretóriolocal,comoseriaocasodo
@edo Start.
SQL> star EMPREGADOS. sql
ENAME
----------
SMITH
ALLEN
SQL>
HOST
Abre um prompt noDOS,o u SHELL no UNIX, sem fechar o SQL*Plus.
Pararetornar,bastadigitar EXIT.
46

## Página 61

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
SPOOL
SPOOL {NOME_ARQUIVO|OFF|OUT}
Quandoqueremosarmazenaroresultadodeumaconsultautilizamoseste
comando. Oresultadoéarmazenadoemumarquivodosistemaoperacional
quepode,opcionalmente,serenviadoparaaimpressorapadrão,configurada
neste sistema operacional.
NOME_ARQUIVO indica o nome do lugar onde
osresultadosserãogravados. Eleégravadocomaextensão LST, entretanto,
pode ser gravado com outra extensão, como por exemplo,TXT.E s t am u -
dança pode ocorrer de acordo com o sistema operacional.OFF Interrompe
a gravação (geração) do arquivo.OUT interrompe a geração do arquivo e o
enviaparaimpressora.
SQL> spool c:\temp\arquivo1.txt
SQL> select ename, job, sal from emp where comm is not null ;
ENAME JOB SAL
---------- --------- ---------
ALLEN SALESMAN 1600
WARD SALESMAN 1250
MARTIN SALESMAN 1250
TURNER VENDEDOR 1500
SQL> spool off;
SQL> edit c:\temp\arquivo1.txt
SQL>
4.3 Variáveisdesistema
As variáveis de sistema determinam o comportamento da ferramenta
S Q L * P l u seaa p r e s e n t a ç ã od o sr e s u l tados exibidos por ela. Através da pró-
pria ferramenta, é possível consultar estas variáveis e também configurá-las.
Usamosocomando
SETparaconfigurarasvariáveis,e SHOWparavisualizar
seusvalores.
• ARRAY[SIZE]{15|n}DefineonúmerodelinhasqueoSQL*Plusdeve
recuperar do banco de dados a cada leitura (Fetch). Vale ressaltar que
47

## Página 62

4.3. Variáveisdesistema CasadoCódigo
não se trata do aspecto visual em tela, mas sim, do acesso interno aos
dadosdobanco,pelaferramenta.
• DEF[INE] {‘&’|c|OFF|ON}Determina o caractere a ser usado para
prefixar variáveis de substituição.ON ou OFF controla se o SQL*Plus
iráounãopesquisarnotextoaprocuradevariáveisdesubstituiçãopara
substituí-lasporvalores. Aousarmos
ON,oprefixodesubstituição,por
padrão,será &.
Exemplo:
SQL> set define on
SQL> select ename, job, sal from emp where deptno = &deptno
/
Enter value for deptno: 20
old 1: select ename, job, sal from emp where deptno = &deptno
new 1: select ename, job, sal from emp where deptno = 20
ENAME JOB SAL
---------- --------- ---------
SMITH CLERK 800
JONES MANAGER 3272.5
SCOTT ANALYST 3000
ADAMS CLERK 1100
FORD ANALYST 3000
SQL> set define off
SQL> select ename, job, sal from emp where deptno = &deptno;
Bind variable "DEPTNO" not declared.
SQL>
Vocêtambémpodeinserirumadescriçãomaisinteligívelparasolicitar
os dados para as variáveis de substituição, utilizandoACCEPT.P a r a
isto, salve seuSELECT em um arquivo e, antes do comando, coloque
asseguinteslinhas,comonoexemploaseguir.
set echo off
accept qtd prompt "Informe a quantidade de empregados desejada:"
select ename
48

## Página 63

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
,sal
from emp
where sal is not null
and rownum < &qtd
order by 2 desc
/
Agora é só executar o arquivo pelo SQL*PLUS, utilizando o comando
@,porexemplo.
• VariáveldeSubstituição Você também pode utilizar uma variável de
substituição,porexemplo,oEcomercial,deformaduplaparareutilizar
o valor da variável sem ter que solicitá-lo sempre ao usuário. Veja o
exemploaseguir:
SQL> select employee_id, last_name, job_id, && column_name
2 from employees
3 where job_id = ’SA_MAN’
4 order by &column_name
5/
Enter value for column_name : salary
old 1: select employee_id, last_name, job_id, && column_name
new 1: select employee_id, last_name, job_id, salary
old 4: order by &column_name
new 4: order by salary
EMPLOYEE_ID LAST_NAME JOB_ID SALARY
----------- ------------------------- ---------- ----------
149 Zlotkey SA_MAN 15373.05
148 Cambrault SA_MAN 16105.1
147 Errazuriz SA_MAN 17569.2
146 Partners SA_MAN 19765.35
145 Russell SA_MAN 20497.4
SQL>
• ECHO{OFF|ON} QuandoexecutamoscomandosSQLapartirdeum
arquivo, podemos definir se eles devem ser exibidos na tela (ON)o u
não( OFF).
49

## Página 64

4.3. Variáveisdesistema CasadoCódigo
Exemplo:
SQL>edit c:\temp\arquivo3.txt
SQL> get c :\temp\arquivo3.txt
1* select ename, job, sal from emp where deptno = &deptno
SQL>
SQL>@ c:\temp\arquivo3.txt
Bind variable "DEPTNO" not declared.
SQL> set define on
SQL>@ c:\temp\arquivo3.txt
Enter value for deptno: 20
old 1: select ename, job, sal from emp where deptno = &deptno
new 1: select ename, job, sal from emp where deptno = 20
ENAME JOB SAL
---------- --------- ---------
SMITH CLERK 800
JONES MANAGER 3272.5
SCOTT ANALYST 3000
ADAMS CLERK 1100
FORD ANALYST 3000
SQL> set echo on
SQL>@ c:\temp\arquivo3.txt
SQL> select ename, job, sal from emp where deptno = &deptno
/
Enter value for deptno: 20
old 1: select ename, job, sal from emp where deptno = &deptno
new 1: select ename, job, sal from emp where deptno = 20
ENAME JOB SAL
---------- --------- ---------
SMITH CLERK 800
JONES MANAGER 3272.5
SCOTT ANALYST 3000
ADAMS CLERK 1100
FORD ANALYST 3000
50

## Página 65

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
SQL>
• HEA[DING]{ON|OFF} Determinaseoscabeçalhosdecolunadevem
serapresentados(default: ON).
Exemplo:
SQL> select ename, job, sal from emp where comm is not null ;
ENAME JOB SAL
---------- --------- ---------
ALLEN SALESMAN 1600
WARD SALESMAN 1250
MARTIN SALESMAN 1250
TURNER VENDEDOR 1500
SQL> set heading off
SQL>/
ALLEN SALESMAN 1600
WARD SALESMAN 1250
MARTIN SALESMAN 1250
TURNER VENDEDOR 1500
SQL> set heading on
SQL>/
ENAME JOB SAL
---------- --------- ---------
ALLEN SALESMAN 1600
WARD SALESMAN 1250
MARTIN SALESMAN 1250
TURNER VENDEDOR 1500
SQL>
• LIN[ESIZE]{80|n} Indicaonúmerodecaracteresporlinha(default:
80).
Exemplo:
51

## Página 66

4.3. Variáveisdesistema CasadoCódigo
SQL> set lines 10
SQL> select ename, job, sal from emp where comm is not null ;
ENAME
----------
JOB
---------
SAL
---------
ALLEN
SALESMAN
1600
WARD
SALESMAN
1250
MARTIN
SALESMAN
1250
TURNER
VENDEDOR
1500
SQL> set lines 80
SQL> select ename, job, sal from emp where comm is not null ;
ENAME JOB SAL
---------- --------- ---------
ALLEN SALESMAN 1600
WARD SALESMAN 1250
MARTIN SALESMAN 1250
TURNER VENDEDOR 1500
SQL>
• PAGES[IZE]{24|n} Indicaonúmerodelinhasparacadapáginado
52

## Página 67

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
relatório(default: 24).
Exemplo:
SQL> set pages 10
SQL> select empno, ename, job, mgr from emp;
EMPNO ENAME JOB MGR
--------- ---------- --------- ---------
7369 SMITH CLERK 7902
7499 ALLEN SALESMAN 7698
7521 WARD SALESMAN 7698
7566 JONES MANAGER 7839
7654 MARTIN SALESMAN 7698
7698 BLAKE MANAGER 7839
7782 CLARK MANAGER 7839
EMPNO ENAME JOB MGR
--------- ---------- --------- ---------
7788 SCOTT ANALYST 7566
7839 KING PRESIDENT
7844 TURNER VENDEDOR 7698
7876 ADAMS CLERK 7788
7900 JAMES CLERK 7698
7902 FORD ANALYST 7566
7934 MILLER CLERK 7782
14 rows selected.
SQL>
• TIMI[NG] {OFF|ON} Controla a apresentação de estatísticas de
tempo. ON mostra as estatísticas em cada comando SQL ou bloco de
PL/SQL.
Exemplo:
SQL> set timing on
SQL> select * from dept;
53

## Página 68

4.3. Variáveisdesistema CasadoCódigo
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
50 TI BRASIL
real:8 3
SQL>
• PAU[SE]<mensagem>Mostraamensagemapósopreenchimentoda
páginadetela.
Exemplo
SQL> set pause ’tecle enter para continuar...’
SQL>
• PAU[SE]{ON|OFF} Indica se o mecanismo de pausa após o preen-
chimentodeumapáginadeveseracionado(default: OFF).
Exemplo:
SQL> set pause on
SQL> select empno, ename, job, mgr from emp;
tecle enter para continuar...
EMPNO ENAME JOB MGR
--------- ---------- --------- ---------
7369 SMITH CLERK 7902
7499 ALLEN SALESMAN 7698
7521 WARD SALESMAN 7698
7566 JONES MANAGER 7839
7654 MARTIN SALESMAN 7698
7698 BLAKE MANAGER 7839
7782 CLARK MANAGER 7839
7788 SCOTT ANALYST 7566
7839 KING PRESIDENT
7844 TURNER VENDEDOR 7698
54

## Página 69

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
7876 ADAMS CLERK 7788
7900 JAMES CLERK 7698
7902 FORD ANALYST 7566
7934 MILLER CLERK 7782
14 rows selected.
SQL>
• SERVEROUT[PUT] {OFF|ON} [SIZE n] [FOR[MAT]
{WRA[PPED] | WOR[D_WRAPPED] | TRU[NCATED]} ]Con-
trola a apresentação das informações geradas através do pacote
DBMS_OUTPUT em stored procedures ou blocos de PL/SQL. O
parâmetro Size determinaonúmerodebytesquepodemserbuferi-
zados dentro do Oracle (o valor deve variar entre 2000 e 1.000.000).
O default é 2000. QuandoWRAPPED é habilitado, a quebra de linha
o c o r r eac a d aLINESIZE caracteres. Quando WORD_WRAPPED é
utilizado, a quebra de linhas ocorre a cada LINESIZE caracteres,
porém em final de palavra. QuandoTRUNCATED é habilitado, cada
linhaétruncadaem LINESIZEcaracteres.
Exemplo:
SQL> declare
2 x varchar2(100);
3 begin
4x : = ’Curso de SQL’ ;
5 dbms_output.put_line(x);
6 end;
7/
PL/SQL procedure successfully completed.
SQL> set serveroutput on
SQL>/
Curso de SQL
PL/SQL procedure successfully completed.
55

## Página 70

4.3. Variáveisdesistema CasadoCódigo
SQL>
• ESC[APE]{\|c|OFF|ON} Definequalocaractereaserusadocomoes-
cape. ON altera o valor<c> para o default\. Este caractere é utili-
zadoantesdocaractereparavariáveisdesubstituiçãoparaindicarque
otextoaseguirdeveserconsideradonormalenãoumasubstituição.
Exemplo:
SQL> show escape
escape OFF
SQL> set escape on
SQL> show escape
escape "\" (hex 5 c)
SQL> select ’SQL &Cia’ from dual;
Enter value for cia:
old 1: select ’SQL & Cia’ from dual
new 1: select ’SQL ’ from dual
’SQL
----
SQL
SQL> select ’ SQL \& Cia ’ from dual;
’SQL&CIA’
---------
SQL & Cia
SQL>
• SQLT[ERMINATOR] { ;|c|OFF|ON} Indica qual caractere o
SQL*PLUS reconhecerá como fim de linha de execução. OFF
indica que não existe caractere associado, o fim do comando é reco-
nhecido por uma linha inteira em branco. A opçãoON retorna ao
valordefaultde ;.
Exemplo:
56

## Página 71

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
SQL> show sqlterminator;
sqlterminator ";" (hex 3b)
SQL> set sqlterminator ’@’
SQL> select * from departamento@
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
30 SALES CHICAGO
40 OPERATIONS BOSTON
50 TI BRASIL
SQL> set sqlterminator ’;’
SQL> select * from departamento;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
30 SALES CHICAGO
40 OPERATIONS BOSTON
50 TI BRASIL
SQL>
• SQLP[ROMPT] {SQL>|text } Indica o texto de prompt para o
SQL*PLUS.
Exemplo:
SQL> show sqlprompt
sqlprompt "SQL> "
SQL>
SQL> set sqlprompt "CURSO SQL>"
CURSO SQL>
CURSO SQL> select * from dept;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
57

## Página 72

4.3. Variáveisdesistema CasadoCódigo
30 SALES CHICAGO
40 OPERATIONS BOSTON
50 TI BRASIL
CURSO SQL> set sqlprompt "SQL>"
SQL>
SQL>
SQL>
ModificaraformacomooSQL*Plusmostraseuprompt:
SQL> set sqlprompt "&&_USER@&&_CONNECT_IDENTIFIER SQL>"
Enter value for _user: tsql
Enter value for _connect_identifier: xe2
tsql@xe2 SQL>
tsql@xe2 SQL>
tsql@xe2 SQL> set sqlprompt "&_USER@&_CONNECT_IDENTIFIER SQL>"
tsql@xe2 SQL>
tsql@xe2 SQL>
• TERMOUT(ON|OFF) Exibe na tela os resultados de comandos exe-
cutadosapartirdearquivos,como,porexemplo, PROMPTs.
Exemplo:
SQL> set termout off
SQL>@ "C:\base_HR\hr_main.sql"
SQL>
SQL> set termout on
SQL>@ "C:\base_HR\hr_main.sql"
Preparando execução...espere
---------------------------------
Executando arquivo HR_DROP. SQL ....
=> Excluindo procedimento ADD_JOB_HISTORY ....
=> Excluindo procedimento SECURE_DML ....
=> Excluindo tabela COUNTRIES ....
58

## Página 73

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
...
--------------------------------
Executando arquivo HR_CRE. SQL ....
=> Criando tabela REGIONS ....
=> Criando tabela COUNTRIES ....
=> Criando tabela LOCATIONS ....
=> Criando visão EMP_DETAILS_VIEW ...
---------------------------------
...
Execução finalizada...
• FEEDBACK(n|ON|OFF) Exibe o retorno de um comando SQL. No
c a sod eu mc o m a n d oSELECT, exibe o número de registros que o co-
mandoretornou,porexemplo: “4linhasselecionadas”. Jáumcomando
CREATE,r eto rnaseoob jetoemquestãofo io unãocriado .
Ovalordefaultpara FEEDBACKé 6. Destaforma,somenteapartirde
6ocorrênciasnoresultadoéqueelemostraráoretorno. Nocasodeum
comando SELECT,seoresultadofororetornode6oumaisregistros,
apareceráaquantidaderetornada. Casocontrário,não. Nocasodeum
comandocriandoumatabela,porexemplo,seovalorconfiguradopara
o
FEEDBACK também for 6, ele não mostrará o resultado dizendo ou
nãosecriou,pois,paraestecomando,oretornoéapenasumalinha.
FEEDBACK 0 éomesmoque OFF. FEEDBACK ON a tivaocomandoe
assumeoúltimonúmerodefinidoparaele.
Exemplo:
SQL> set feedback 5
SQL> select ename from emp where comm is not null ;
ENAME
----------
ALLEN
59

## Página 74

4.4. DefinindoVariáveisnoSQL*Plus CasadoCódigo
WARD
MARTIN
TURNER
SQL>
SQL> set feedback 3
SQL> select ename from emp where comm is not null ;
ENAME
----------
ALLEN
WARD
MARTIN
TURNER
4 linhas selecionadas.
SQL>
SQL> set feedback 3
SQL> select ename from emp where comm is not null ;
ENAME
----------
ALLEN
WARD
MARTIN
TURNER
4.4 DefinindoVariáveisnoSQL*Plus
A variável de sistema DEFINE, que é configurada através do comando SET,
serve para ativar ou não as definições referentes ao uso das variáveis de sub-
tituição. Contudo, existe também um comando com este mesmo nome que
é utilizado para definir variáveis no SQL*Plus, as quais serão usadas como
variáveisdesubstituição. Vejaoexemploabaixo:
60

## Página 75

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
SQL> define employee_num = 200
SQL> select employee_id, last_name, salary, department_id
2 from employees
3 where employee_id = &employee_num;
EMPLOYEE_ID LAST_NAME SALARY DEPARTMENT_ID
----------- ------------------------- ---------- -------------
200 Whalen 6442,04 10
SQL> undefine employee_num
SQL>
Neste exemplo, está sendo definida uma variável chamada EM-
PLOYEE_NUM.Notequealémdeserdefinida,amesmaestárecebendoum
valor por padrão. Depois de definida, ou melhor, declarada, a variável é uti-
lizada como uma variável de substituição, sendo precedida por E comercial.
Paralimparadefinição,utilizeocomandoUNDEFINE.
4.5 Configurações iniciais de login do
SQL*Plus
OSQL*Pluspossuiumarquivodeconfiguraçãoqueéacionadocadavezqueo
programaéiniciado. Nestearquivo,épossívelinserirconfiguraçõesparaque,
aoiniciaroprograma,elassejamexecutadas. Configuraçõescomoonúmero
delinhasporpágina(
PAGESIZE)ecaracteresporlinha( LINESIZE)podem
serinseridasnestearquivo. Parainserirasconfigurações,bastaabriroarquivo
glogin.sqleinseri-lasdeformabemparecidacomoseestivessedigitando
nopróprioprograma. Vejaumexemploem:
C:\oraclexe\app\oracle\product`.2.0\server\sqlplus\admin
Nocorpodoarquivo,temos:
--
-- Copyright (c) 1988, 2004, Oracle Corporation.
-- All Rights Reserved.
--
-- NAME
-- glogin.sql
61

## Página 76

4.5. ConfiguraçõesiniciaisdelogindoSQL*Plus CasadoCódigo
--
-- DESCRIPTION
-- SQL*Plus global login "site profile" file
--
-- Add any SQL*Plus commands here that are to be executed when
-- a user starts SQL*Plus, or uses the SQL*Plus CONNECT
-- command
--
-- USAGE
-- This script is automatically run
--
-- Used by Trusted Oracle
COLUMN ROWLABEL FORMAT A15
-- Used for the SHOW ERRORS command
COLUMN LINE/COL FORMAT A8
COLUMN ERROR FORMAT A65 WORD_WRAPPED
-- Used for the SHOW SGA command
COLUMN name_col_plus_show_sga FORMAT a24
COLUMN units_col_plus_show_sga FORMAT a15
-- Defaults for SHOW PARAMETERS
COLUMN name_col_plus_show_param FORMAT a36 HEADING NAME
COLUMN value_col_plus_show_param FORMAT a30 HEADING VALUE
-- Defaults for SHOW RECYCLEBIN
COLUMN origname_plus_show_recyc FORMAT a16 HEADING
’ORIGINAL NAME’
COLUMN objectname_plus_show_recyc FORMAT a30 HEADING
’RECYCLEBIN NAME’
COLUMN objtype_plus_show_recyc FORMAT a12 HEADING
’OBJECT TYPE’
COLUMN droptime_plus_show_recyc FORMAT a19 HEADING ’DROP TIME’
-- Defaults for SET AUTOTRACE EXPLAIN report
-- These column definitions are only used when SQL*Plus
-- is connected to Oracle 9.2 or earlier.
COLUMN id_plus_exp FORMAT 990 HEADING i
62

## Página 77

CasadoCódigo Capítulo4. ExecutandocomandosSQLcomSQL*Plus
COLUMN parent_id_plus_exp FORMAT 990 HEADING p
COLUMN plan_plus_exp FORMAT a60
COLUMN object_node_plus_exp FORMAT a8
COLUMN other_tag_plus_exp FORMAT a29
COLUMN other_plus_exp FORMAT a44
-- Default for XQUERY
COLUMN result_plus_xquery HEADING ’Result Sequence’
-- Banco Curso SQL
SET PAGESIZE 24
SET LINES 80
4.6 Verificando Variáveis de Substituição no
SQL*Plus
Paraverificarseassubstituiçõesreferentesasvariáveisdesubstituiçãoforam
feitas corretamente na instrução SQL, use o comando VERIFY. O comando
O comando SET VERIFY ON faz com que o SQL*Plus exiba o texto de um
comandoapóselesubstituirasvariáveisdesubstituiçãopelosrespectivosva-
loresinformados. Vamosaumexemplo:
SQL> set verify on
SQL> select employee_id, last_name, salary
2 from employees
3 where employee_id = &employee_num
4/
Enter value for employee_num: 200
old 3: where employee_id = &employee_num
new 3: where employee_id = 200
EMPLOYEE_ID LAST_NAME SALARY
----------- ------------------------- ----------
200 Whalen 6442.04
SQL>
63

## Página 78

4.7. AutomatizarlogindoSQL*Plus CasadoCódigo
Note no exemplo, que é mostrado o texto OLD e NEW, com o antes e
depoisdasubstituiçãodasvariáveis.
4.7 AutomatizarlogindoSQL*Plus
Quando executamos o SQL*Plus, é solicitado um usuário, senha e string do
banco. Podemosfazercomque,aoiniciar,elejáconecteautomaticamenteao
bancodedados. CliquecomobotãodireitodomousenoatalhodoSQL*Plus
eváem
Propriedades.N oc a m p oDestinonaaba Atalho,logoapósa
chamadado .exe,coloque <usuário>/<senha>@<string_conexão>.
Porexemplo: tsql/tsql@xe2. Vejaoprintaseguir.
[imageimages/img_pg_50_do_pdf.png]
64

## Página 79

Capítulo5
LimitesdoSGDBOracle
A seguir, os limites definidos para os diversos componentes que constituem
ou que são utilizados dentro da plataforma do banco de dados ou nas suas
linguagens.
• Tabelas:onúmeromáximodetabelas clusterizadasé32. Eéilimitado
porbancodedados.
• Colunas: o número máximo por tabela é de 1000 colunas. Por índice
(ou índice clusterizado), é de 32 colunas. Por índice bitmap, é de 30
colunas.
• Linhas: onúmerodelinhasportabelaéilimitado.
• Índices: o número de índices por tabela é ilimitado. Por tamanho de
colunas indexadas, é de 75% do tamanho total do bloco do banco de
dados(minus some overhead).

## Página 80

CasadoCódigo
• Caracteres: aquantidadeparanomesdeobjetosélimitadaa30carac-
teres.
• CláusulaGROUPBY: aexpressão GROUPBY etodasasexpressõesde
agregação(porexemplo,SUM,AVG)devemestardentrodeumúnico
bloconabasededados.
• CONSTRAINTS:onúmerode constraintsporcolunaéilimitado.
• SUBQUERIES:on í v e ld esubqueries, em um comando SQL, é ilimi-
tado na cláusula FROM quando no primeiro nível de umaquery,eé
limitadoa255nacláusula WHERE.
• G r u p od ev a l o r e s :oc a m p odata pertence ao intervalo de 1-Jan-
4712BCa31-Dec-4712AD.
• TabelasouVIEWS“joined”emumaQUERY: ilimitado.
• PACKAGESarmazenadas: em PL/SQL e Developer/2000 pode ha-
verlimitesnotamanhode PROCEDURESarmazenadasqueelaspodem
chamar. Olimiteemgeralestáentre2000a3000linhasdecódigo.
• TRIGGERSemcascata: dependedosistemaoperacional;geralmente
32.
• Usuárioseregras: élimitadoa2,147,483,638.
• Partições: comprimento máximo de linha da chave particionada é de
4KB– overhead. Onúmeromáximodecolunasnachaveparticionadaé
de16. Onúmeromáximodepartiçõesdisponíveisportabelaouíndice
éde64KB–1partição .
• DefiniçãoparaCREATEMATERIALIZEDVIEW: temtamanhomá-
ximode64Kbytes.
66

## Página 81

CasadoCódigo Capítulo5. LimitesdoSGDBOracle
O limite de até quanto uma instrução SQL pode retornar (resposta)
depende de alguns fatores, incluindo configurações, espaço em disco e
memória.
Quandoumobjetoestáinstanciadonamemória,nãoexisteumlimite
fixo para o número de atributos neste objeto. Mas o total máximo do
tamanhodamemóriaparaumobjetoinstanciadoéde4GB.Quandoum
objetoinstanciadoéinseridodentrodatabela,osatributossãoalocados
emcolunasseparadas,eolimitede1000colunaséaplicado.
5.1 TiposdedadosdoSGDBOracle
Nasequência,vejaostiposdedadosutilizadospelaslinguagensSQLePLSQL
paraaconstruçãodeprogramasouparametrizaçõesdobancodedados.
VARCHAR2
O tamanho máximo para campos de tabela é de 4000 bytes. O tamanho
máximo para PL/SQL é de 32.767 bytes. OVARCHAR2 év a r i á v e les o m e n t e
usaoespaçoqueestáocupado. Diferentementedo CHAR.
Comentário: VARCHARéumsubtipo(assimcomo STRING)queexiste
porquestõesdecompatibilidadecomoutrasmarcasdebancodedadosetam-
bém com o padrão SQL. Entretanto, a Oracle, no momento, não recomenda
ou s od ot i p o
VARCHAR porque sua definição deve mudar à medida que o
padrãoSQLevoluir. Deve-seusar VARCHAR2.
CHAR
Otamanhomáximoéde2000bytes.
Comentário: Otipo CHARéusadoparaconterdadosdestringdecom-
primento fixo. Ao contrário das strings deVARCHAR2,u m as t r i n gCHAR
semprecontémonúmeromáximodecaracteres.
Outrostipos
• NCHAR:tamanhomáximode2000bytes
67

## Página 82

5.1. TiposdedadosdoSGDBOracle CasadoCódigo
• NCHARVARYING:tamanhomáximode4000bytes
• CHARVARYING:tamanhomáximode4000bytes
NUMBER(p,s)
É um numero com sinal e ponto decimal, sendo: (p)recisão de 1 a 38 dí-
gitos(e)scala-84a127.
Estetipotambémpossuisubtiposcomo:
• DECIMAL:igualaNUMBER;
• DEC:igualaDECIMAL;
• DOUBLEPRECISION: igualaNUMBER;
• NUMERIC:igualaNUMBER;
• INTEGER:equivalenteaNUMBER(38);
• INT:igualaINTEGER;
• SMALLINT:igualaNUMBER(38);
• FLOAT:igualaNUMBER;
• FLOAT(prec):igual a NUMBER(prec), mas a precisão é expressa em
termos de bits binários, não de dígitos decimais. A precisão binária
podevariarde1até126.
DATE
Otipo DATEéusadoparaarmazenarosvaloresdedataehora. Umnome
melhor seria DATETIME porque o componente de hora está sempre lá, in-
dependente de você usá-lo ou não. Se não for especificada a hora ao atribuir
umvalorparaumavariáveldotipo
DATE,opadrãodemeia-noite(12:00:00
a.m.) seráusado.
Eleédotipo:1JAN4712BCaté31DEC4712AD(DATAcomhora,minuto
esegundo).
68

## Página 83

CasadoCódigo Capítulo5. LimitesdoSGDBOracle
TIMESTAMP
Data com segundos fracionais. Permite o armazenamento de dados de
tempo,comooano,omês,ahora,minutoeos egundodotipodedados DATE,
alémdosvaloresdesegundosfracionais. Existemmuitasvariaçõesdessetipo
dedados,como WITH TIMEZONE , WITH LOCALTIMEZONE .
INTERVALYEARTOMONTH
Armazenados com um intervalo de anos e meses. Permite que os dados
de tempo sejam armazenados como um intervalo de anos e meses. Usado
pararepresentaradiferençaentredoisvaloresdedata/horaemqueapenaso
anoeomêssãosig nificativos.
INTERVALDAYTOSECOND
Armazenados como um intervalo de dias, horas, minutos e segundos.
Permite que os dados de tempo sejam armazenados como um intervalo de
dias, horas, minutos e segundos. Usado para representar a diferença precisa
entredoisvaloresdedata/hora.
BOOLEAN
Édoti po Truee False.
LONG
Somentepodeexistirumacolunaportabela. Seutamanhomáximopara
tabelaéde2GB.SeutamanhomáximoparaPL/SQLéde32.760.
RAW
Otamanhomáximoparacamposdetabelaéde2000bytes. Seutamanho
máximoparaPL/SQLéde32.767.
LONG RAW éoutrotipoparecidocom RAW,adiferençaéqueelepossui7
bytesamenosquandoutilizadoemPL/SQL.
69

## Página 84

5.1. TiposdedadosdoSGDBOracle CasadoCódigo
CamposLONG
Existemalgumasrestriçõesparacampos LONGe LONG RAW .
• Nãosepodecriarum OBJECT TYPE co moa trib u todeLONG.
• Uma colunaLONG n ã op o d ee s t a rd e n t r od ac l á u s u l aWHERE ou com
referênciaintegraldosdados,exceto NULLou NOT NULL .
• U mafunçãonãopoder eto rnarumcam poLONG.
• Umatabelapoderátersomenteumcampo LONG.
• LONGnãopodeserindexada.
• LONGnãopodeusarcláusulasalémdo WHERE,jámencionado, GROUP
BY, ORDER BY e CONNECT BY .
Umadicaparavocêusarumcampo LONGnacláusula WHEREécriaruma
t a b e l at e m p o r á r i ac o mo sc a m p o sd at a b e l ao r i g i n a l ,m a sa l t e r a n d ou mt i p o
LONG para CLOB. Também é possível alterar diretamente na tabela o campo
LONG para CLOB, caso não tenha problema de alterar a estrutura da tabela
original. Vejaoexemplo:
create global temporary table table_temp (campo_lob clob) on
commit preserve rows
/
insert into table_temp select to_lob(coluna_lob) from
table_original
/
Outraalternativa,casovocêtenhaconhecimentosemPLSQL,éacriação
deumprogramapararealizarapesquisa. ComrecursosdaPLSQLvocêcon-
segue utilizar funções que não são permitidas, pelo menos nestes casos, em
SQL.Ocódigopodeserparecidocomomostradoaseguir.
declare
cursor c1 is
select view_name, text
70

## Página 85

CasadoCódigo Capítulo5. LimitesdoSGDBOracle
from user_views;
begin
for r1 in c1 loop
if r1. text like ’%emp%’ then
dbms_output.put_line(r1.view_name);
end if;
end loop;
end;
Por existirem estas limitações, a Oracle criou a famíliaLOB ( CLOB,
BLOB, NLOB, BFILE),quevisaresolveralgunsdestesproblemasenfren-
tadoscomotipo LONG.
CLOB
Otamanhomáximoé (4 GB - 1) * DB_BLOCK_SIZE,parâmetrode
inicialização(8TBa128TB).Onúmerodecolunas CLOBportabelaélimitado
somente pelo número máximo de colunas por tabela. Ele armazena textos.
Estes textos são validados conforme ocaracter set , ou seja, armazena
acentuaçãoetc. Tipos LOBsurgiramemsubstituiçãoaostipos LONGe LONG
RAW,poisestessópermitiamumacolunaportabela. Ostipos LOBpermitem
maisdeumacoluna.
NCLOB
O tamanho máximo é de(4 GB - 1) * DB_BLOCK_SIZE, parâme-
tro de inicialização (8TB a 128TB). O número de colunasNCLOB por tabela
é limitado somente pelo número máximo de colunas por tabela. Objeto de
grandecapacidadedecaracteresnacionais–contématé4GBdecaracteresde
bytes simples ou caracteres multibyte que atendem o conjunto de caracteres
nacionaldefinidopelobancodedadosOracle.
BLOB
Otamanhomáximoéde (4 GB - 1) * DB_BLOCK_SIZE,parâmetro
deinicialização(8TBa128TB).
71

## Página 86

5.2. Resumo CasadoCódigo
O número de colunasBLOB por tabela é limitado somente pelo número
máximo de colunas por tabela. Armazenam dados não estruturados como:
som,imagem,dadosbinários.
BFILE
O tamanho máximo é de 4GB. O tamanho máximo para o nome do ar-
quivoéde255caracteres. Otamanhomáximoparaonomedodiretórioéde
30caracteres. Onúmeromáximode
BFILEsabertosélimitadopelovalordo
parâmetro de inicializaçãoSESSION_MAX_OPEN_FILES, o qual é limitado
pelonúmeromáximodearquivosabertosqueosistemaoperacionalsuporta.
ROWID
Éumtipoespecialusadoparaarmazenaros ROWIDs(endereçosfísicos)
daslinhasarmazenadasemumatabela.
5.2 Resumo
Emresumo,ostiposcomumenteutilizadossão: CHAR, VARCHAR2, NUMBER,
DATE, BOOLEANeosdafamília LOB.
72

## Página 87

Capítulo6
Gerenciandousuários
6.1 Manipulandousuários
Vimos anteriormente que para se conectar ao banco de dados é necessário
terumusuárioeumasenha. Oescopodecriaçãodeusuáriosgeralmentefaz
parte da função do Administrador do Sistema, também chamado de DBA.
Eleéquemcriaosusuáriosdentrodobanco,concedendoassim,oacessoao
ambiente.
Entretanto,éimportantesabercomocriarumusuárioeconcederprivilé-
giosparaquepossaoperarnosistemadobancodedados. Noteque,paracriar
um usuário, é necessário estar conectado ao banco. Para isto, temos que ter
umusuárioquejáestejacriadoequetenhapoderparacriaroutrosusuários.
Quando um banco de dados Oracle é instalado, existem dois usuários
que são criados automaticamente. Um deles é o
SYS eo u t r ooSYSTEM.A s
senhas para estes usuários podem ser modificadas também no momento da

## Página 88

6.1. Manipulandousuários CasadoCódigo
instalaçãodobancodedados. Casocontrário,assenhaspadrõessão: SYS e
MANAGER,respectivamente.
Além das definições de nome e senha, outras informações também
podem ser definidas, como em quais TABLESPACE e TABLESPACE
TEMPORARYousuáriovaiseralocado,quaisasquotas,ouseja,quantodees-
paço nestas TABLESPACES ele terá para a criação de objetos e manipulação
dedadosouseelevaiseragregadoaalgum PROFILE específico. Mas como
foi dito, estas informações cabem aos DBA definirem. Quando criamos um
usuário, não precisamos informar todas estas definições. O Oracle trabalha
com valores padrões e, caso não sejam informados, ele usará estes padrões
paraestabelecerestasconfigurações.
Como já foi mencionado anteriormente, ao criar um usuário, o Oracle
tambémcriaum
SCHEMA,ondeestarãoagregadostodososobjetosqueeleve-
nhaacriar. Destaforma,quandooutrosusuáriosquiseremseutilizardeobje-
tosdosquaiselesnãosejamosdonos,terãoqueusaronomedeste
SCHEMAna
frente do nome do objeto. Exemplo:TSQL.FILME. Mas lembre-se: mesmo
utilizandoonomedoesquemanafrentedoobjeto,outrousuáriosóteráeste
acessocasooproprietáriodoobjetotenhadadoconcessãodeacesso(
GRANT).
O DBA também pode estabelecer estas configurações e definir que, a cada
novousuáriocriado,omesmoassumaestasdiretrizes. Destaforma,osusuá-
riosqueirãocriarobjetosoumanipulá-losnãoprecisarãosepreocuparcom
essesdetalhes.
Vejamosacriaçãobásicadeumusuário:
SQL> create user TSQL identified by teste123;
User created.
SQL>
Asinformaçõesdefinidasnomomentodacriaçãodousuáriopodemser
alteradasposteriormente. Paraisso,éutilizadoocomando ALTER USER .No
exemploaseguir,vamosalterarasenhadousuárioqueacabamosdecriar.
SQL> alter user TSQL identified by TSQL;
74

## Página 89

CasadoCódigo Capítulo6. Gerenciandousuários
User altered.
SQL>
Paraexcluirumusuário,usamosocomando DROPou DROP CASCADE .
Esteúltimoéutilizadoquandoousuárioéproprietáriodealgumobjeto. Vale
ressaltarqueumusuárioconectadonãopodeserexcluído.
SQL> drop user TSQL;
drop user TSQL
*
ERROR at line 1:
ORA-01922: CASCADE must be specified to drop ’TSQL’
SQL>
Este erro ocorreu pelo fato de que o usuário possui objetos criados em
seu esquema. Nesses casos, para excluí-lo, devemos utilizar a expressão
CASCADE.Vejadenovoaexecução,agorautilizando CASCADE:
SQL> drop user TSQL cascade;
User dropped.
SQL>
Paraobterinformaçõessobreosusuários,useas VIEWS: USER_USERS,
ALL_USERS e DBA_USERS. Para saber sobreQUOTAS do usuário, acesse:
USER_TS_QUOTASe DBA_TS_QUOTAS.
6.2 Concedendoacessoaousuário
DentrodoOracle,nãobastaapenascriarumusuário,éprecisoconcederaces-
sos (privilégios) para que ele possa manipular os objetos ou até mesmo criá-
losnobancodedados. Destaforma,podemoster,basicamente,doistiposde
privilégios: osdeobjetoseosdesistemas.
75

## Página 90

6.2. Concedendoacessoaousuário CasadoCódigo
Privilégiosdeobjetos
Os privilégios de objetos são aqueles que permitem o usuário a executar
um SELECT, UPDATE, DELETE, INSERT, ALTER,entreoutros.
Jáosprivilégiosdesistemadãoaousuáriopermissãoparaadministraro
bancodedados. Nalistadeprivilégios,estãoacriaçãoeeliminaçãodeobjetos
emqualquer SCHEMAdeusuário.
Seguealistadealgunsprivilégiosdeobjetos:
• SELECT: permiteaousuárioselecionarosdadosdastabelasdobanco
dedados;
• DELETE: permiteaousuárioexcluirregistrosdastabelasdobancode
dados;
• INSERT: permiteaousuárioinserirregistrosdastabelasdobancode
dados;
• UPDATE: permiteaousuárioatualizarregistrosdastabelasdobanco
dedados;
• ALTER: permiteaousuárioalterarobjetosdobancodedados;
• EXECUTE: permiteaousuárioexecutarprocedimentosarmazenados
nabasededados;
• INDEX: permiteaousuáriocriaríndicesemtabelasosclusters;
• READ: permitealeituradearquivosemumdeterminadodiretório;
• REFERENCES: permite ao usuário referenciar uma determinada ta-
belaparaacriaçãodechavesestrangeiras( FK);
• WRITE: permiteaescritadearquivosemumdeterminadodiretório;
• ALL[PRIVILEGES]: contemplatodososprivilégiosanteriores.
Na sequência, veja exemplos de como dar privilégios de objetos a um
usuário. Paraisto,utilizamosocomando GRANT.
Concedendo as ações de SELECT, UPDATE e DELETE,n at a b e l a
LOCATIONS,paraousuário TSQL:
76

## Página 91

CasadoCódigo Capítulo6. Gerenciandousuários
SQL> grant select , update, delete on LOCATIONS to TSQL;
Grant succeeded.
SQL>
Concedendoaaçãode UPDATE,apenasparaoscampos POSTAL_CODE
E STREET_ADDRESS,natabela LOCATIONS,paraousuário TSQL:
SQL> grant update (POSTAL_CODE, STREET_ADDRESS) on
LOCATIONS to TSQL;
Grant succeeded.
SQL>
Concedendo a ação de EXECUTE,d a PROCEDURE
P_PESQUISA_EMPREGADOS,paraousuário TSQL:
SQL> grant execute on P_PESQUISA_EMPREGADOS to TSQL;
Grant succeeded.
SQL>
Pare retirar os privilégios dados a um usuário, utilizamos o comando
REVOKE.Vejaosexemplosaseguir.
Revogandoaação UPDATE,natabela LOCATIONS,paraousuário TSQL.
SQL> revoke update on LOCATIONS from TSQL;
Revoke succeeded.
SQL>
Revogandoaação EXECUTE,da PROCEDUREP_PESQUISA_EMPREGADOS,
paraousuário TSQL.
SQL> revoke execute on P_PESQUISA_EMPREGADOS from TSQL;
77

## Página 92

6.3. Privilégiosdesistema CasadoCódigo
Revoke succeeded.
SQL>
Ao contrário do GRANT,o REVOKE só pode ser usado com
UPDATE/REFERENCES a partir da tabela inteira, não sendo possível re-
vogarapenasdeumacoluna.
Outro recurso que pode ser usado no momento de executar o comando
de GRANTéo WITH GRANT OPTION .Elepermiteaousuárioqueestárece-
bendoaconcessãoopoderdetambémdaracessoparaoutrosusuários. Vejo
oexemplo:
SQL> grant select on JOB_HISTORY to TSQL with grant option ;
Grant succeeded.
SQL>
Nesteexemplo,alémdaconcessãodeacessodadaaousuário TSQL,tam-
bém está sendo dada a permissão para que ele possa dar o mesmo tipo de
acessoaoutrosusuáriosdobancodedados.
6.3 Privilégiosdesistema
Estetipodeprivilégiopermiteaousuáriomanipularqualquerobjetodabase
de dados, de qualquer
SCHEMA (indicando a expressãoANY), ou ainda exe-
cutarcomandosrelacionadosàadministraçãodobanco. Segueumalistacom
algunsprivilégiosdesistema:
• CREATETABLE: permiteacriaçãodetabelas;
• CREATESYNONYM: permiteacriaçãodesinônimos;
• CREATEPUBLICSYNONYM: permite a criação de sinônimos pú-
blicos;
78

## Página 93

CasadoCódigo Capítulo6. Gerenciandousuários
• CREATESEQUENCE: permiteacriaçãode SEQUENCES;
• CREATEVIEW: permiteacriaçãode VIEWS;
• CREATEPROCEDURE: permiteacriaçãode PROCEDURES;
• CREATETRIGGER: permiteacriaçãode TRIGGERS;
• SELECT ANY TABLE:permite a consulta em tabelas de qualquer
SCHEMA;
• CREATE ANY INDEX:permite a criação de índices em qualquer
SCHEMA;
• CREATE ANY TABLE:permite a criação de tabelas em qualquer
SCHEMA;
• CREATEANYTRIGGER: permiteacriaçãode TRIGGERSemqual-
quer SCHEMA;
• DROP ANY SEQUENCE:permite a exclusão de SEQUENCES em
qualquer SCHEMA;
• EXECUTE ANY PROCEDURE: permite a execução em
PROCEDURESdequalquer SCHEMA;
• DROPTABLESPACE:permiteaexclusãodequalquer TABLESPACE;
• INSERTANYTABLE: permiteainserçãoemqualquertabeladequal-
quer SCHEMA;
• CREATESESSION: permiteaconexãoaobancodedados;
• ALTERSESSION: permite a alteração na sessão aberta no banco de
dados;
• ALTERUSER: permiteaalteraçãodousuário;
• ALTERTABLESPACE: permiteaalteraçãode TABLESPACE;
• ALTERANYTRIGGER: permiteaalteraçãode TRIGGERSemqual-
quer SCHEMA;
79

## Página 94

6.3. Privilégiosdesistema CasadoCódigo
• CREATEANYDIRECTORY: permite a criação deDIRECTORIES
emqualquer SCHEMA;
• DROPANYDIRECTORY: permiteaexclusãode DIRECTORIESem
qualquer SCHEMA.
Exemplosdeconcessão:
Co ncedendoaaçãode ALTER USER paraousuário TSQL:
SQL> grant alter user to TSQL;
Grant succeeded.
SQL>
Co ncedendoaaçãode CREATE ANY TABLE paraousuário TSQL:
SQL> grant create any table to TSQL;
Grant succeeded.
SQL>
Exemplosderevogação:
Revogandoaaçãode
DROP ANY SEQUENCE paraousuário TSQL:
SQL> revoke drop any sequence from TSQL;
Revoke succeeded.
SQL>
Revogandoaaçãode CREATE ANY DIRECTORY paraousuário TSQL:
SQL> revoke create any directory from TSQL;
Revoke succeeded.
SQL>
80

## Página 95

CasadoCódigo Capítulo6. Gerenciandousuários
Assim como em privilégios de objetos, quando concedemos privilé-
giosdesistemasparaosusuáriostambémpodemospermitirqueelecon-
cedaestesprivilégiosaoutros. Fazemosistoutilizandoacláusula WITH
ADMIN OPTION .
UsuárioPUBLIC
Quandoestamostrabalhandocomumbancodedadosgrande,ondeexis-
tem muitos usuários, pode ser dispendioso gerar concessões para cada um.
Paraisso, existeumusuáriochamado
PUBLIC.Quandoconcedemosalgum
privilégioparaele, écomosetodososusuárioscadastradosnobancodeda-
dosrecebessemesteprivilégio. Contudo,aocontráriodosusuáriosnormais,
osquaisvimoscomomanipular,criar,alterareexcluir,esteusuárionãopode
serutilizadoparaseconectarnobancodedados. Logo,comele,nãoépossível
criar,excluir,alterarourealizarqualqueratividaderelacionadaaosobjetos.
Concedendo a ação de
SELECT,n at a b e l aSALGRADE,p a r aou s u á r i o
PUBLIC:
SQL> grant select on SALGRADE to public ;
Grant succeeded.
SQL>
6.4 AcessoatravésdeROLES
Imagineuma ROLEcomosendoumobjetoagrupadordeprivilégios. Quando
criamosuma ROLE,podemosincluiremseuteorumasériedeprivilégiose,
melhor, depois de ter feito isto, podemos atribuir estaROLE au mo um a i s
usuário. Entendeu a ideia? Pois bem, umaROLE n a d am a i séq u eu ma g r u -
pamentodeprivilégiosque,apartirdomomentoemqueécriadaedefinida,
pode ser passada para o usuário como se fosse um privilégio. O usuário,
quando recebe como privilégio uma
ROLE, obtém, automaticamente, todos
os privilégios que ela possui. Dentro de umaROLE podemos ter privilégios
81

## Página 96

6.4. AcessoatravésdeROLES CasadoCódigo
de objetos e sistema. UmaROLE não possui proprietário e pode ser conce-
didaaoutradesdequenãosejaparaelamesma. As ROLESpodemaindaser
desativadaseativadasporusuário. Vejaumexemplo:
Criandoa ROLE CONTROLA_EMPREGADO :
SQL> create role CONTROLA_EMPREGADO;
Role created.
SQL>
Nopassoanterior,apenascriamosa ROLE.Agoratemosquedefinirquais
os privilégios ela terá. Vamos permitir a realização deSELECTS na tabela
EMP.
SQL> grant select on EMP to CONTROLA_EMPREGADO;
Grant succeeded.
SQL>
Paraonossoteste,vamoscriarumnovousuáriochamado TSQL2.
SQL> create user TSQL2 identified by TSQL2;
User created.
SQL>
Agora, concederemos a ele o privilégioCONTROLA_EMPREGADO,q u e
nadamaiséquenossa ROLEcriadaanteriormente.
SQL> grant CONTROLA_EMPREGADO to TSQL2;
Grant succeeded.
SQL>
V amosco nectarco mousuáriono vo:
82

## Página 97

CasadoCódigo Capítulo6. Gerenciandousuários
SQL> conn TSQL2/TSQL2@xe2;
ERROR:
ORA-01045: user TSQL2 lacks CREATE SESSION privilege;
logon denied
Warning: You are no longer connected to ORACLE.
SQL>
Houveumerro. OOracleestáinformandoqueousuário TSQL2nãopos-
suiprivilégiosparacriarumasessãonobancodedados, ouseja, queelenão
pode conectar por falta de privilégios. Note que, realmente, apenas criamos
o usuário, mas não dissemos o que ele pode fazer. Para resolver isso, temos
quedefiniralgunsprivilégiosparaele.
Vamosconectarcomousuário
SYSTEM,queéumdosusuárioscommais
privilégios dentro do banco de dados Oracle. Através dele, vamos conceder
oprivilégiode
RESOURCEe CONNECT,quesãopredefinidosdentrodoOra-
cle. Na verdade, sãoROLES criadas, contendo uma série de privilégios que
permitem aos usuários realizar várias operações dentro do banco de dados,
incl usiveparaco nectar -seaele.
SQL> conn system/manager@xe2;
Connected.
SQL>
Concedendoalgunsprivilégios:
SQL> grant resource, connect to TSQL2;
Grant succeeded.
SQL>
Voltando ao usuário TSQL2, agora conectando no banco de dados com
sucesso:
SQL> conn TSQL2/TSQL2@xe2;
Connected.
SQL>
83

## Página 98

6.4. AcessoatravésdeROLES CasadoCódigo
V a m o st e s t a rs en o s s aROLE está realmente concedida para o usuário
TSQL2. Realizaremos um SELECT em cima da tabela EMP do SCHEMA
TSQL,noqualnossa ROLEsebaseia.
SQL> select * from TSQL.EMP where rownum < 10;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 2975
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
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
9 rows selected.
SQL>
Perfeito. NossaROLEestáatribuída. Agorapodemostestaromesmoco-
mando SELECT,masantesdissovamosrevogaroprivilégiodadoaousuário.
P a r ai s t o ,c o n e c t e m o sc o mou s u á r i oTSQL, que também possui privilégios
deadministrador,eexecutemosarevogaçãodoprivilégio.
84

## Página 99

CasadoCódigo Capítulo6. Gerenciandousuários
SQL> conn TSQL/TSQL@xe2;
Connected.
SQL>
Revogandooprivilégiodousuário TSQL2:
SQL> revoke CONTROLA_EMPREGADO from TSQL2;
Revoke succeeded.
SQL>
Estabelecendoconexãocomousuário:
SQL> conn TSQL2/TSQL2@xe2;
Connected.
SQL>
Conforme havíamos previsto, uma vez que retiramos o privilégio do
usuário,elenãoconsegueselecionarosdadosdatabela EMP.
SQL> select * from TSQL.EMP;
select * from TSQL.EMP
*
ERROR at line 1:
ORA-00942: table or view does not exist
SQL>
Vamosvoltaroprivilégio:
SQL> conn TSQL/TSQL@xe2;
Connected.
SQL>
SQL> grant CONTROLA_EMPREGADO to TSQL2;
Grant succeeded.
SQL>
85

## Página 100

6.4. AcessoatravésdeROLES CasadoCódigo
Ousuáriovoltaterprivilégiosdeacesso.
SQL> conn TSQL2/TSQL2@xe2;
Connected.
SQL>
SQL> select * from TSQL.EMP where rownum < 15;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 2975
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
86

## Página 101

CasadoCódigo Capítulo6. Gerenciandousuários
10
14 rows selected.
SQL>
Vamostentaralgodiferente,vamosinserirnatabela EMP:
SQL> insert into EMP (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
values (999,’FULANO’,’VENDEDOR’,NULL,’10-JAN-11’,3000,10,
20);
*
ERROR at line 1:
ORA-01031: insufficient privileges
SQL>
Vejaquenãoconseguimosrealizarestetipodeoperação,poisnãofoidado
o privilégio de inserção para o usuário e ele também não está contemplado
nanossa ROLE.Co n tudo ,istoaindapodeserfei to .
SQL> conn TSQL/TSQL@xe2;
Connected.
SQL>
SQL> grant insert on EMP to CONTROLA_EMPREGADO;
Grant succeeded.
SQL>
Apósoprivilégiode INSERTtersidoatribuídoa ROLE,nossousuáriojá
pode,agora,realizarinserçõesnatabela EMP.
SQL> conn TSQL2/TSQL2@xe2;
Connected.
SQL>
SQL> insert into EMP (empno, ename, job, mgr, hiredate, sal,
comm, deptno)
values (999,’FULANO’,’VENDEDOR’,NULL,’10-JAN-11’,3000,10,
87

## Página 102

6.4. AcessoatravésdeROLES CasadoCódigo
20);
1 row created.
SQL>
Através das ROLES,épossívelcriarvárioscenáriosparagarantirgrupos
deconcessões,como,porexemplo,concessõesparagerentesdeumaempresa,
empregados de uma fábrica ou setor, ou seja, modelar o acesso aos dados
atravésdeconjuntosdeprivilégios,deformaapermitirourestringirousoda
informação.
Uma
ROLE permite o acesso a objetos que estão em outrosSCHEMAS,
masnãopermitequesejamcriadosoutrosobjetoscombasenosobjetosque
ela deu permissão. Um exemplo disso é a criação de
VIEWS c o mb a s ee m
tabelas que não estão criadas noSCHEMA do usuário conectado, mesmo ele
tendooprivilégiode SELECTede CREATE VIEW .Vejaoexemploaseguir:
Comousuário TSQL2conectado,vamostentarcriaruma VIEWcombase
natabela EMPdo SCHEMA TSQL (tabelacriadanesteusuário)àqualfoicon-
cedidaapermissãode SELECTatravésda ROLE CONTROLA_EMPREGADO .
SQL> conn TSQL2/TSQL2@xe2;
Connected.
SQL>
SQL> create view EMP_V as select * from TSQL.EMP;
create view EMP_V as select * from TSQL.EMP
*
ERROR at line 1:
ORA-01031: insufficient privileges
SQL>
Noteque,nessaexecução,nãoconseguimosexecutaracriaçãoda VIEW.
Umerroinformandoqueosprivilégiosforaminsuficientesnosfoimostrado.
Vamos tentar agora conceder umGRANT de CREATE VIEW p a r aou s u á r i o
TSQL2. Noteque,paraisso,temosqueconectarcomoutrousuárioquetenha
permissão para conceder privilégios. Com esse intuito, utilizamos o usuário
TSQL.
88

## Página 103

CasadoCódigo Capítulo6. Gerenciandousuários
SQL> conn TSQL/TSQL@xe2;
Connected.
SQL>
SQL> grant create view to TSQL;
Grant succeeded.
SQL>
Depois do privilégio concedido, vamos tentar, novamente, criar a nossa
VIEWco mbasenatabeladeo u tr oSCHEMA.
SQL> conn TSQL2/TSQL2@xe2;
Connected.
SQL>
SQL> create view EMP_V as select * from TSQL.EMP;
create view EMP_V as select * from TSQL.EMP
*
ERROR at line 1:
ORA-01031: insufficient privileges
SQL>
Mesmo com oGRANT de CREATE VIEW , não foi possível criar a nova
VIEW. Para testar se o usuário recebeu mesmo o privilégio de criação de
VIEW,vamoscriarumatabelachamada EMP2apartirdatabela EMPdousuá-
rio TSQL.Nestecaso,épossívelrealizaracriaçãodoobjeto.
Agora você deve estar se perguntando o porquê de dar certo, sendo que
estamos criando um objeto também a partir de um objeto concedido. A di-
ferença é fácil de entender. UmaVIEW,e m b o r as e j ac r i a d an oSCHEMA do
usuárioqueestáconectado,trazdadosdeoutratabelaqueestáemoutrousuá-
rio/schema,ouseja,cadavezquevocêacessá-la,elaexecutao
SELECTquea
compõeparabuscarosdados. Osdadosreferentesabuscanãoseencontram
nousuá riodo noda
VIEW e,sim,emoutro. Nestecaso,a VIEW éobrigadaa
acessaroutro SCHEMA.
Como existe esta limitação emROLES, a execução de sua criação não é
permitida. Já a criação de uma tabela, a partir dos dados de outra que está
89

## Página 104

6.4. AcessoatravésdeROLES CasadoCódigo
em outro SCHEMA, faz com que esta tabela que está em outroSCHEMA seja
acessada uma única vez, somente no momento da criação da nova, ou seja,
quando executamos oCREATE TABLE é feita uma cópia da tabela que está
nooutro SCHEMAeestacó p iaécriadanousuárioqueexecu to uoco mando .
SQL> create table EMP2 as select * from TSQL.EMP;
Table created.
SQL>
Notequeoerronãoacontecequandotentamoscriaruma VIEWcombase
natabelaqueestácriadanomesmo SCHEMA.
SQL> create view EMP_V as select * from EMP2;
View created.
SQL>
ROLESnãopodemsercriadasdentrodeoutrosobjetos,porexemplo,
dentrode PROCEDURESou FUNCTIONS.
AtribuindoROLESpordefault
Um recurso existente quando estamos trabalhando com ROLES é o de
associar uma ROLE por padrão para um usuário. Isso funciona da seguinte
forma:seassociarmosumaROLEpadrãoparaumusuário,elesóteráacessoa
estaROLE.Seousuárionãorecebeunenhumaatribuiçãodefault,elepoderá
usufruirdetodasasROLESqueestiveremliberadasparaele. Oquedeveser
ressaltadoéque,primeiramente,umaROLEdeveseratribuídaaumusuário,
antes de ser atribuída como seu default. O que deve ser observado, também,
é que quando se atribui ROLES por padrão a um usuário, ele perde acesso a
outras ROLES que por ventura possa ter, inclusive a de conexão. Para isto, é
necessárioreatribuí-las,todascomo
DEFAULT.Vejaostiposdeatribuiçõesa
seguir:
90

## Página 105

CasadoCódigo Capítulo6. Gerenciandousuários
• ROLE{<NOME>[,<NOME>]}: atribui determinada(s) ROLE(S) ao
usuário;
• ROLE ALL [EXCEPT ROLE [,ROLE]]:atribui todas as ROLES já
concedidasaousuário,podendoabrirexceções;
• ROLENONE: retiraaatribuiçãodas ROLESjáconcedidasaousuário.
Veja:
SQL> conn TSQL/TSQL@xe2;
Connected.
SQL>
SQL>
SQL> alter user TSQL2 default role CONTROLA_EMPREGADO;
-- Atribuindo uma ROLE como default.
User altered.
SQL> create role EXCLUI_EMPREGADO; -- Criando a ROLE
EXCLUI_EMPREGADO.
Role created.
SQL> grant delete on EMP to EXCLUI_EMPREGADO; -- Concedendo
ações a ROLE criada.
Grant succeeded.
SQL> grant EXCLUI_EMPREGADO to TSQL2; -- Concedendo a ROLE ao
usuário.
Grant succeeded.
SQL> alter user TSQL2 default role CONTROLA_EMPREGADO,
EXCLUI_EMPREGADO; -- Atribuindo duas ROLES como default.
User altered.
SQL>
91

## Página 106

6.4. AcessoatravésdeROLES CasadoCódigo
SQL> alter user TSQL2 default role all ; -- atribuindo todas as
ROLES como default.
User altered.
SQL> alter user TSQL2 default role all except EXCLUI_EMPREGADO;
-- atribuindo todas as ROLES como default, com exceções.
User altered.
SQL>
SQL> alter user TSQL2 default role none ; -- retirando a
atribuição de todas as ROLES default.
User altered.
SQL>
Estesexemplosdemonstramacriaçãoeatribuiçãode ROLESparaousuá-
rio TSQL2.
Mesmoquedeterminadas ROLESjátenhamsidoconcedidasaousuário,
podemos fazer com que, por padrão, elas não estejam disponíveis quando o
usuárioabrirumasessãonobancodedados. Vejaoexemplo:
Vamosconcederdoisprivilégiosparaousuário TSQL2:
SQL> conn TSQL/TSQL@xe2;
Connected.
SQL>
SQL> grant CONTROLA_EMPREGADO to TSQL2;
Grant succeeded.
SQL> grant EXCLUI_EMPREGADO to TSQL2;
Grant succeeded.
SQL>
92

## Página 107

CasadoCódigo Capítulo6. Gerenciandousuários
Contudo, vamos configurar o usuário para não receber umaROLE por
defaultquandoeleconectaraobancodedados:
SQL> alter user TSQL2 default role none ;
User altered.
SQL>
Voltemosparaousuário TSQL2.Aotentarmosnosconectarcomousuá-
rio TSQL2,podeocorrerumproblemaportermosdefinidoqueelenãoteria
nenhuma ROLE como default. Como já foi dito anteriormente, quando cri-
amos um usuário temos que dar algumasconcessões, entre elas, a concessão
de conexão ao banco. Esta concessão se torna default pra o usuário, por isso
conseguimos conectá-lo ao banco. Quando definimos que não haveria mais
ROLESdefault,perdemosestatambém. Vejaatentativaaseguir:
SQL> conn TSQL2/TSQL2@xe2;
ERROR:
ORA-01045: user TSQL2 lacks CREATE SESSION privilege;
logon denied
Warning: You are no longer connected to ORACLE.
SQL>
SQL> conn TSQL2/TSQL2@xe2;
ERROR:
ORA-01045: user TSQL2 lacks CREATE SESSION privilege;
logon denied
SQL>
SQL> conn TSQL/TSQL@xe2;
Connected.
SQL>
SQL> grant resource, connect to TSQL2;
Grant succeeded.
93

## Página 108

6.4. AcessoatravésdeROLES CasadoCódigo
SQL> grant create session to TSQL2;
Grant succeeded.
SQL>
SQL> conn TSQL2/TSQL2@xe2;
Connected.
SQL>
SQL>
Testandoosprivilégiosconcedidos:
SQL> select * from TSQL.EMP;
select * from TSQL.EMP
*
ERROR at line 1:
ORA-00942: table or view does not exist
SQL> delete from TSQL.EMP where DEPTNO = 20;
delete from TSQL.EMP where DEPTNO = 20
*
ERROR at line 1:
ORA-00942: table or view does not exist
SQL>
Note que não foi possível selecionar e nem excluir os registros da tabela
EMP.Issosedeupelofatodeque,emboraousuáriotenhaosprivilégioscon-
cedidos,osmesmosnãoforamatribuídosaele. Agoradevemosativarospri-
vilégiosparaousuárioparaqueelepossa,enfim,acessarosdados.
Ativandoedesativando ROLES
Vimosatéaquiquepodemosatribuir ROLESporpadrãoaosusuáriosdo
bancodedados. Alémdeatribuirmosuma ROLEouumconjuntode ROLES
em específico para um usuário, também podemos atribuir todas asROLES
94

## Página 109

CasadoCódigo Capítulo6. Gerenciandousuários
ounenhuma. Noexemploanterior,emboratenhamosdoisprivilégiosconce-
didosparaousuário TSQL2,elesnãoestãodisponíveis. Issoocorreuporque
porpadrão foidefinido quenenhuma ROLE seriacolocadacomodefaultno
momentoemqueousuárioconectasse,ouseja,elasexistemeestãoconcedi-
das,masestãodesativadasparaesteusuário. Oquetemosquefazeréativá-las:
SQL> set role CONTROLA_EMPREGADO, EXCLUI_EMPREGADO;
Role set .
SQL>
Depoisderealizadaaativação,as ROLESestarãodisponíveis:
SQL> select EMPNO, ENAME, JOB, MGR, HIREDATE from TSQL.EMP
where rownum < 5;
EMPNO ENAME JOB MGR HIREDATE
--------- ---------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80
7499 ALLEN SALESMAN 7698 20-FEB-81
7521 WARD SALESMAN 7698 22-FEB-81
7566 JONES MANAGER 7839 02-APR-81
SQL>
Outrasformasdeativaçãoedesativaçãode ROLES:
• ROLE {<NOME> [IDENTIFIED BY PASSWORD] [,
<NOME>[IDENTIFIED BY PASSWORD]]}: atribui determi-
nada(s) ROLE(S) ao usuário, podendo especificar uma senha de
acesso;
• ROLE ALL [EXCEPT ROLE [,ROLE]]:atribui todas as ROLES já
concedidasaousuário,podendoabrirexceções;
• ROLENONE: retiraaatribuiçãodas ROLESjáconcedidasaousuário.
Veja. Exemplosdeativaçãode ROLESemespecífico:
95

## Página 110

6.4. AcessoatravésdeROLES CasadoCódigo
SQL> set role CONTROLA_EMPREGADO;
Role set .
SQL> set role EXCLUI_EMPREGADO identified by senha12345;
Role set .
SQL> set role CONTROLA_EMPREGADO, EXCLUI_EMPREGADO;
Role set .
SQL> set role EXCLUI_EMPREGADO identified by senha12345,
EXCLUI_EMPREGADO identified by senha67890;
Role set .
SQL>
Exemplosdeativaçãode ROLESemmassa:
SQL> set role all ;
Role set .
SQL> set role all except EXCLUI_EMPREGADO, CONTROLA_EMPREGADO;
Role set .
SQL>
Exemplosdedesativaçãode ROLESemmassa:
SQL> set role none ;
Role set .
SQL>
96

## Página 111

CasadoCódigo Capítulo6. Gerenciandousuários
RolespredefinidaseinformaçõessobreROLES
Quando o banco de dados é instalado, algumasROLES sãocriadas. Elas
já vêm com alguns privilégios concedidos. Elas podem ser atribuídas aos
usuários para que eles possam conectar ao banco de dados ou até mesmo
administrá-lo. Na sequência estão listadas as três mais utilizadas. Existem
muitasoutraseistovaidependerdaversãodobancodedados.
• CONNECT:
CREATE SESSION , ALTER SESSION , CREATE
DATABASE LINK , CREATE SYNONYM , CREATE VIEW ;
• RESOURCE: CREATE TABLE , CREATE CLUSTER , CREATE
SEQUENCE, CREATE PROCEDURE , CREATE TRIGGER ;
• DBA: todososprivilégiosdesistema( withadminoption ).
Informações sobre ROLES, privilégios de ROLES e de usuários podem
serencontradasacessandoasseguintes VIEWS:
• DBA_ROLES
• DBA_ROLE_PRIVS
• ROLE_TAB_PRIVS
• ROLE_SYS_PRIVS
• ROLE_ROLE_PRIVS
97

## Página 113

Capítulo7
Manipulaçãodetabelas
7.1 ManipulandoTabelas
CREATETABLE
Estecomandoéusadoparacriarumatabelaedefinirsuascolunas,bemcomo
outraspropriedadesemumbancodedados.
V ejaacriaçãoatabela EMP:
SQL> create table emp
( empno number(4,0) not null
,ename varchar2(10)
,job varchar2(9)
,mgr number(4,0)
,hiredate date
,sal number(7,2)

## Página 114

7.1. ManipulandoTabelas CasadoCódigo
,comm number(7,2)
,deptno number(2,0)
);
Table created.
SQL>
Criandoatabela DEPT:
SQL> create table dept
(
deptno number(2,0)
,dname varchar2(14)
,loc varchar2(13)
);
Table created.
SQL>
DEFAULTESPECIFICATIONS
Nadefiniçãodacriaçãodatabelapodemosespecificarparadeterminada
coluna um valor padrão (DEFAULT). Feito isso, quando fazemos uma inser-
ção de um registro, caso não informemos valor para esta coluna, o Oracle
assumeovalorquedeclaramoscomo DEFAULT.Issoécomumenteutilizado
em colunas que se referem a datas. Por exemplo, podemos ter um campo
natabelareferenteàdataderegistronosistemadetodososempregadosque
forem cadastrados. Para isso, definimos um valor default para o campo e,
quandoinserirmosumregistro,estecamporeceberáestevalorpadrão. Neste
exemplopodemosdizerqueovalor
DEFAULTé SYSDATE.
Colunas com valores DEFAULT só assumem estes valores caso não se-
jaminformadasnomomentodeumainserção,pois,aoinformá-las,vocêterá
que definir um valor. Mesmo que seja
NULL, o Oracle não acionará o valor
DEFAULT,eleassumiráo NULLinformado.
Vejaatabelaaseguirsendocriadacomestetipodeespecificação:
SQL> create table empregados
( empno number(4,0) not null
100

## Página 115

CasadoCódigo Capítulo7. Manipulaçãodetabelas
,ename varchar2( 10)
,job varchar2(9)
,mgr number(4,0)
,hiredate date default sysdate
,sal number(7,2)
,comm number(7,2) default 0
,deptno number(2,0)
)
/
Table created.
SQL> select * from empregados;
no rows selected
SQL>
Seminformaradatadeadmissão( HIREDATE),seuusoficaassim:
SQL>insert into empregados (empno,ename,job,mgr,sal,comm,deptno)
values(100,’CEREBRO’,’PEDREIRO’,null,3000,0,10)
/
1 row created.
SQL>
SQL> select * from empregados;
EMPNO ENAME JOB MGR HIREDATE SAL COMMDEPTNO
----- ------- -------- --- --------- ----- --------- ---------
100 CEREBRO PEDREIRO 09-APR-11 3000 0 10
SQL>
Notequeadatadeadmissãofoipreenchidacomadataatualdomomento
emqueocomandofoiexecutado.
Seinformarmosadatadeadmissãocomonula:
101

## Página 116

7.1. ManipulandoTabelas CasadoCódigo
SQL> insert into empregados (empno,ename,job,mgr,hiredate,sal,
comm,deptno)
values(101,’PINK’,’SERVENTE’,100,null,1000,0,10)
/
1 row created.
SQL>
SQL> select * from empregados;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
100 CEREBRO PEDREIRO 09-APR-11 3000
101 PINK SERVENTE 100 1000
COMMDEPTNO
--------- ---------
01 0
01 0
SQL>
Nesse caso, como a coluna foi informada, embora tenha sido passado o
valornulo,elefoiconsiderado. Comisto,ovalor DEFAULTnãofoiatribuído.
Aoinserirsemovalordecomissão( COMM):
SQL> insert into empregados (empno,ename,job,mgr,hiredate,sal,
deptno)
2 values(102,’JOCA’,’SERVENTE’,100,sysdate,1000,10)
3/
1rowcreated.
SQL>
SQL>select * from empregados;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
102

## Página 117

CasadoCódigo Capítulo7. Manipulaçãodetabelas
100 CEREBRO PEDREIRO 09-APR-11 3000
101 PINK SERVENTE 100 1000
102 JOCA SERVENTE 100 09-APR-11 1000
COMMDEPTNO
--------- ---------
01 0
01 0
01 0
SQL>
Note que a comissão ficou zerada, uma vez que não foi atribuída no co-
mando INSERT.
CriandotabelacombaseemSELECT
NoOracle,épossívelcriarumatabelaatravésdaseleçãodeoutratabela.
Vejaaseguiracriaçãodatabela SALES,combasenatabela EMP,naqual
somenteempregadosvendedoressãoarmazenados.
SQL> create table SALES as select * from emp where
job = ’SALESMAN’;
Table created.
SQL>
A g o r av e j aac r i a ç ã od at a b e l aANALYST,t a m b é mc o mb a s en at a b e l a
EMP,ondesomenteempregadosanalistassãoarmazenados.
SQL> create table ANALYST as select * from emp where
job = ’ANALYST’;
Table created.
SQL>
Este comando não apenas cria a tabela utilizando a estrutura de uma já
existente,comotambémlevaseusdadoscadastrados. Alémdisso,essesdados
103

## Página 118

7.1. ManipulandoTabelas CasadoCódigo
não precisam ser confirmados, pois o próprio comandoCREATE gera um
COMMITimplicitamente,assimcomotodocomando DDL.
Caso só deseje a estrutura, e não os dados contidos na tabela, use o co-
mandodestaforma:
SQL> create table CLERK as select * from emp where 1<>1;
Table created.
SQL> desc clerk
Name Null? Type
------------------------------- -------- ----
EMPNO NOT NULL NUMBER(4)
ENAME VARCHAR2(10)
JOB VARCHAR2(9)
MGR NUMBER(4)
HIREDATE DATE
SAL NUMBER(7,2)
COMM NUMBER(7,2)
DEPTNO NUMBER(2)
SQL> select * from clerk;
no rows selected
SQL>
N otequeacláusula WHERE 1<>1 ,fazcomquenenhumdadosejaretor-
nado.
Tabelastemporárias
OOraclepossuiumrecursonacriaçãodetabelasqueéatabelatemporá-
ria. Basicamente, ela funciona da seguinte forma. A princípio, ela age como
uma tabela normal: sua criação é feita como qualquer tabela Oracle. A dife-
rença está no armazenamento de dados. Em uma tabela normal, inserimos
informações e, se desejarmos que elas permaneçam salvas no banco, nós as
efetivamos através do
COMMIT. No caso das tabelas temporárias, seus dados
104

## Página 119

CasadoCódigo Capítulo7. Manipulaçãodetabelas
ficam armazenados somente enquanto a transação ou sessão no Oracle (por
exemplo, no SQL*Plus) estiver aberta. Quando a transação ou sessão é fe-
chada,todososdadossãoexcluídoseatabelavoltaaficarzerada. Daívemo
conceitodetabelatemporária,jáqueseusdadossãotemporáriosnumatran-
saçãoo usessão .
Temosdoistiposdetabelastemporárias: temporáriaportransaçãoetem-
poráriaporsessão. Astabelastemporáriasportransaçãoguardamseusdados
enquanto a transação não for encerrada por um
COMMIT ou ROLLBACK.J á
as temporárias por sessão guardam seus dados até que a sessão seja encer-
rada. Vale lembrar que quando conectamos ao banco de dados, através do
SQL*Plus,porexemplo,oOracleabreumasessão. Quandoefetuamosopri-
meirocomandodentrodestasessãoéqueoOracle,implicitamente,abreuma
transação. Além disso, estando dentro de uma transação, podemos abrir vá-
riasoutrastransações.
No exemplo a seguir, vamos criar uma tabela chamada
EMP_TMP com
baseno SCRIPTdatabela EMP,quejáconhecemos. Aúnicamudançaéque
vamoscriá-lanoformatodetabelatemporária.
Temporáriaporsessão
SQL> create global temporary table emp_tmp
( empno number(4,0) not null
,ename varchar2(10)
,job varchar2(9)
,mgr number(4,0)
,hiredate date
,sal number(7,2)
,comm number(7,2)
,deptno number(2,0)
)
on commit preserve rows ;
Table created.
SQL>
Vamosinserirdadosnatabelaapartirdatabela EMP.
105

## Página 120

7.1. ManipulandoTabelas CasadoCódigo
SQL> insert into emp_tmp select * from emp where deptno = 10;
4 rows created.
SQL> select * from emp_tmp;
EMPNO ENAME JOB MGR HIREDATE SAL COMM DEPTNO
----- ------ --------- ----- --------- ----- ------ --------
7782 CLARK MANAGER 7839 09-JUN-81 2450 10
7839 KING PRESIDENT 17-NOV-81 5000 10
7934 MILLER CLERK 7782 23-JAN-82 1300 10
3 JOCA MECANICO 21-APR-11 5000 0 10
SQL>
Vamosfecharatransação.
SQL> commit;
Commit complete.
SQL> select * from emp_tmp;
EMPNO ENAME JOB MGR HIREDATE SAL COMM DEPTNO
----- ------ --------- ----- --------- ----- ------ --------
7782 CLARK MANAGER 7839 09-JUN-81 2450 10
7839 KING PRESIDENT 17-NOV-81 5000 10
7934 MILLER CLERK 7782 23-JAN-82 1300 10
3 JOCA MECANICO 21-APR-11 5000 0 10
SQL>
Note que, na execução anterior, mesmo fechando a transação, os dados
permanecem. Vamosfecharasessãoeverificaroqueacontece.
SQL> select * from emp_tmp;
EMPNO ENAME JOB MGR HIREDATE SAL COMM DEPTNO
----- ------ --------- ----- --------- ----- ------ --------
7782 CLARK MANAGER 7839 09-JUN-81 2450 10
106

## Página 121

CasadoCódigo Capítulo7. Manipulaçãodetabelas
7839 KING PRESIDENT 17-NOV-81 5000 10
7934 MILLER CLERK 7782 23-JAN-82 1300 10
3 JOCA MECANICO 21-APR-11 5000 0 10
SQL> disconnect
SQL> conn tsql/tsql@xe2;
Connected.
SQL>
SQL> select * from emp_tmp;
no rows selected
SQL>
Temporáriaportransação
SQL> create global temporary table emp_tmp
( empno number(4,0) not null
,ename varchar2(10)
,job varchar2(9)
,mgr number(4,0)
,hiredate date
,sal number(7,2)
,comm number(7,2)
,deptno number(2,0)
);
Table created.
SQL>
Igualmenteaoquefizemosanteriormente,vamosinserirdadosnatabela
apartirdatabela EMP.
SQL> insert into emp_tmp select * from emp where deptno = 10;
4 rows created.
SQL> select * from emp_tmp;
107

## Página 122

7.1. ManipulandoTabelas CasadoCódigo
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7782 CLARK MANAGER 7839 09-JUN-81 2450
7839 KING PRESIDENT 17-NOV-81 5000
7934 MILLER CLERK 7782 23-JAN-82 1300
3 JOCA MECANICO 21-APR-11 5000
COMM DEPTNO
--------- ---------
10
10
10
01 0
SQL>
Vamosfecharatransação.
SQL> select * from emp_tmp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7782 CLARK MANAGER 7839 09-JUN-81 2450
7839 KING PRESIDENT 17-NOV-81 5000
7934 MILLER CLERK 7782 23-JAN-82 1300
3 JOCA MECANICO 21-APR-11 5000
COMM DEPTNO
--------- ---------
10
10
10
01 0
SQL> commit;
Commit complete.
108

## Página 123

CasadoCódigo Capítulo7. Manipulaçãodetabelas
SQL> select * from emp_tmp;
no rows selected
SQL>
Note que agora o resultado foi outro. Como finalizamos a transação, os
dadosforamexcluídos.
Algumascaracterísticasdastabelastemporárias:
• Dados de tabelas temporárias só podem ser vistos na sessão que os
criou;
• Podemos criar TRIGGERS e VIEWS para tabelas temporárias assim
comoparaastabelascomuns;
•O u s o d eTRUNCATE, ROLLBACKe SAVEPOINTépermitido;
• A definição de uma tabela temporária fica acessível para todas as ses-
sões;
• Transaçõesfilhaspodemacessardadosdetabelastemporáriasdatran-
sação pai. Entretanto, se a transação pai modificou algum dado da ta-
bela, a transação filha não poderá usar a tabela. O mesmo acontece se
a transação filha estiver utilizando a tabela. Neste caso, nenhuma ou-
tratransação,inclusiveatransaçãopai,poderáutilizá-laatéatransação
serfinalizada. Contudo,feitoisso,osdadosinseridosnatransaçãofilha
sãoexcluídos;
• Épermitidocriartabelastemporáriasemtempodeexecução;
• Podemoscriaríndicesparatabelastemporárias,maselesserãotempo-
rários;
• Épermitidaacriaçãodeconcessões(
GRANTS)pa raasta belastem po-
rárias,bemcomosinônimos;
• Podemos utilizar tabelas temporárias emPROCEDURES, FUNCTIONS
e PACKAGES.
109

## Página 124

7.2. ALTERTABLE CasadoCódigo
7.2 ALTERTABLE
Atravésdestecomando,vocêpodealteraraestruturadeumatabela,incluindo
novas colunas, alterando o tipo de dado, alterando a obrigatoriedade e cri-
andonovas
CONSTRAINTS,comochavesprimáriaseestrangeiras.
Adicionandoacoluna DT_NASCIMENTO,doti po DATE,natabela EMP:
SQL> alter table EMP add DT_NASCIMENTO date;
Table altered.
SQL> desc EMP
Name Null? Type
------------------------------- -------- ----
EMPNO NOT NULL NUMBER(4)
ENAME VARCHAR2(10)
JOB VARCHAR2(9)
MGR NUMBER(4)
HIREDATE DATE
SAL NUMBER(7,2)
COMM NUMBER(7,2)
DEPTNO NUMBER(2)
DT_NASCIMENTO DATE
SQL>
Excluindoacoluna DT_NASCIMENTOdatabela EMP:
SQL> alter table EMP drop column DT_NASCIMENTO;
Table altered.
SQL> desc EMP;
Name Null? Type
------------------------------- -------- ----
EMPNO NOT NULL NUMBER(4)
ENAME VARCHAR2(10)
JOB VARCHAR2(9)
MGR NUMBER(4)
110

## Página 125

CasadoCódigo Capítulo7. Manipulaçãodetabelas
HIREDATE DATE
SAL NUMBER(7,2)
COMM NUMBER(7,2)
DEPTNO NUMBER(2)
SQL>
Modificandoacoluna ENAMEpara VARCHAR2(240) NOT NULL ,antes
NULL:
SQL> alter table EMP modify ENAME varchar2(240) not null ;
Table altered.
SQL> DESC EMP;
Name Null? Type
------------------------------- -------- ----
EMPNO NOT NULL NUMBER(4)
ENAME NOT NULL VARCHAR2(240)
JOB VARCHAR2(9)
MGR NUMBER(4)
HIREDATE DATE
SAL NUMBER(7,2)
COMM NUMBER(7,2)
DEPTNO NUMBER(2)
SQL>
Adicionandoacoluna DS_OBSERVACAO,dotipo VARCHAR2(2000),na
tabela EMP.
SQL> alter table EMP add (ds_observacao varchar2(2000));
Table altered.
SQL> DESC EMP;
Name Null? Type
------------------------------- -------- ----
EMPNO NOT NULL NUMBER(4)
ENAME NOT NULL VARCHAR2(240)
111

## Página 126

7.2. ALTERTABLE CasadoCódigo
JOB VARCHAR2(9)
MGR NUMBER(4)
HIREDATE DATE
SAL NUMBER(7,2)
COMM NUMBER(7,2)
DEPTNO NUMBER(2)
DS_OBSERVACAO VARCHAR2(2000)
SQL>
Modificandoacoluna DS_OBSERVACAOpara VARCHAR2(4000),an tes
VARCHAR2(2000):
SQL> alter table EMP modify ds_observacao varchar2(4000);
Table altered.
SQL> DESC EMP;
Name Null? Type
------------------------------- -------- ----
EMPNO NOT NULL NUMBER(4)
ENAME NOT NULL VARCHAR2(240)
JOB VARCHAR2(9)
MGR NUMBER(4)
HIREDATE DATE
SAL NUMBER(7,2)
COMM NUMBER(7,2)
DEPTNO NUMBER(2)
DS_OBSERVACAO VARCHAR2(4000)
SQL>
Renomeandoumacolunadatabela:
SQL> alter table EMP rename column ename to nome;
Table altered.
SQL>
112

## Página 127

CasadoCódigo Capítulo7. Manipulaçãodetabelas
A travésdocomando ALTER TABLE ,tambémépossívelcolocaratabela
emmododeconsulta,impedindoquealteraçõesde DDL ou DML sejamrea-
lizadas. Consequentemente, asuavoltaaomododegravaçãotambémérea-
lizadaporestecomando.
SQL> alter table emp read only ; -- configura para somente
leitura.
Table altered.
SQL>
SQL> alter table emp read write ; -- configura para leitura e
gravação.
Table altered.
SQL>
7.3 DROPTABLE
Assimcomovocêpodecriarumatabela,vocêtambémpodeexcluí-la,desde
quevocêtenhapoderesparaisto.
Excluindoatabela EMP:
SQL> drop table EMP;
Table dropped.
SQL>
Excluindoatabela DEPT:
SQL> drop table DEPT;
Table dropped.
SQL>
113

## Página 128

7.4. TRUNCATETABLE CasadoCódigo
7.4 TRUNCATETABLE
Oc o m a n d oTRUNCATE elimina todas as linhas da tabela. Diferente do
DELETE,aaçãodestecomandonãopermite ROLLBACK,ouseja,umavezexe-
cutado, não há como voltar à situação anterior, pois ele faz umCOMMIT im-
plicitamente. Por isso, ele também pode ser considerado um comandoDDL.
Entretanto, ele não elimina a estrutura da tabela ou de índices, somente os
dados.
Seexistiremprivilégios, TRIGGERSou CONSTRAINTS,elescontinuarão
intactos. Nocasodas TRIGGERS,elasnãosãodisparadasquandoocomando
éexecutado. Umcuidadoquesedeveterédesabilitaraschavesestrangeiras(
FKs) antes de executar este comando, a menos que seja uma chave de autor-
relacionamento( SELF-JOIN).
Truncandoatable EMP:
SQL> truncate table EMP;
Table truncated.
SQL>
7.5 Ordenandodados
ORDERBY
Este comando especifica a ordem em que as linhas selecionadas serão exibi-
das. Estas colunas podem ou não estar dispostas no
SELECT. Para definir
a ordenação, deve-se colocar a cláusulaORDER BY e, logo após, o nome da
colunaousuaposiçãonacláusula SELECT,casoelaestejainformada. Além
disso,vocêpodedefinirqualtipodeordenação:
• ASC –ordenaçãoascendente(quandonãosedefinequaltipodeorde-
nação,estaseráapadrão)
• DESC–ordenaçãodescendente
Ordenandoporumnomedecoluna. Ordenaçãodotipo ASC,poisotipo
nãofoiinformado:
114

## Página 129

CasadoCódigo Capítulo7. Manipulaçãodetabelas
SQL> select ename
from emp
order by ename;
ENAME
----------
ADAMS
ALLEN
BLAKE
CLARK
FORD
JAMES
JONES
KING
MARTIN
MILLER
SCOTT
SMITH
TURNER
WARD
14 rows selected.
SQL>
A ordenação também pode ser feita informando a posição da coluna, na
sequência em que ela aparece noSELECT. Neste exemplo, a ordenação está
sendorealizadapelacoluna2( FIRST_NAME).
SQL> select employee_id
,first_name
,email
from employees
where rownum < 15
order by 2;
EMPLOYEE_ID FIRST_NAME EMAIL
----------- -------------------- -------------------------
103 Alexander AHUNOLD
115

## Página 130

7.5. Ordenandodados CasadoCódigo
104 Bruce BERNST
109 Daniel DFAVIET
105 David DAUSTIN
107 Diana DLORENTZ
111 Ismael ISCIARRA
110 John JCHEN
112 Jose Manuel JMURMAN
102 Lex LDEHAAN
113 Luis LPOPP
108 Nancy NGREENBE
101 Neena NKOCHHAR
100 Steven SKING
106 Valli VPATABAL
14 rows selected.
SQL>
Ordenaçãopelacoluna SALARY.
SQL> select first_name
,email
,salary
from employees
where salary between 4000 and 5000
order by salary;
FIRST_NAME EMAIL SALARY
-------------------- ------------------------- ---------
Sarah SBELL 4000
Alexis ABULL 4100
Diana DLORENTZ 4200
Nandita NSARCHAN 4200
Jennifer JWHALEN 4400
Valli VPATABAL 4800
David DAUSTIN 4800
7 rows selected.
SQL>
116

## Página 131

CasadoCódigo Capítulo7. Manipulaçãodetabelas
Ordenandopelacoluna FIRST_NAME,agorainformandootipodeorde-
nação ASC(ascendente):
SQL> select first_name
,email
,salary
from employees
where job_id = ’IT_PROG’
order by first_name asc;
FIRST_NAME EMAIL SALARY
-------------------- ------------------------- ---------
Alexander AHUNOLD 9000
Bruce BERNST 6000
David DAUSTIN 4800
Diana DLORENTZ 4200
Valli VPATABAL 4800
SQL>
Além das ordenações vistas anteriormente, podemos escolher o tipo de
ordenaçãoporcoluna:
SQL> select job
,sal
from emp
where deptno = 20
order by job asc, sal desc;
JOB SAL
--------- ---------
ANALYST 3000
ANALYST 3000
CLERK 1100
CLERK 800
MANAGER 2975
SQL>
117

## Página 132

7.5. Ordenandodados CasadoCódigo
Neste exemplo, estamos ordenando da seguinte forma. Primeiramente,
os registros são ordenados de forma ascendente pela colunaJOB. Logo em
seguida, é aplicada a segunda ordenação pelo maior salário (colunaSAL),
considerando a primeira ordenação já aplicada, ou seja, dentro de um con-
juntodelinhasdeummesmocargo,serárealizadaaordenaçãoporsalário.
Tambémpode-seutilizarocomando SELECTjuntamentecomo ORDER
BYparaordenarinformaçõescombaseemcolunasdeoutrastabelas.
SQL> select empno
,ename
,deptno
from emp e
where rownum < 11
order by (select dname
from dept d
where d.deptno = e.deptno);
EMPNO ENAME DEPTNO
--------- ---------- ---------
7839 KING 10
7782 CLARK 10
7788 SCOTT 20
7566 JONES 20
7369 SMITH 20
7698 BLAKE 30
7844 TURNER 30
7521 WARD 30
7499 ALLEN 30
7654 MARTIN 30
10 rows selected.
SQL>
Neste exemplo, a ordenação está sendo realizada por valores vindos de
uma subquery. No caso, estes valores são os nomes dos departamentos sele-
cionados.
118

## Página 133

CasadoCódigo Capítulo7. Manipulaçãodetabelas
7.6 Trazendodadosdistintos
DISTINCT
Este comando é usado no caso de uma consulta apresentar mais de um re-
gistro com valores idênticos. Usando-o, não será permitida reincidência de
registrosjáexibidos. Vejaoexemplo:
SQL> select deptno
from emp
order by deptno asc;
DEPTNO
---------
10
10
10
20
20
20
...
30
30
30
30
14 rows selected.
SQL>
SQL> select distinct deptno
from emp
order by deptno asc;
DEPTNO
---------
10
20
30
119

## Página 134

7.7. Relacionamentoentretabelas CasadoCódigo
SQL>
Neste exemplo, um DISTINCT pela coluna DEPTNO faz com que seja
mostradaapenasumaocorrênciadecadacódigodedepartamento.
Emvezdeusarocomando DISTINCTtambémpodemosusaro UNIQUE.
Ambossãosemelhantes.
Sabemos que oDISTINCT é utilizado para restringir linhas duplicadas.
Também sabemos que, em umSELECT que esteja gerando linhas duplica-
das,porpadrão,oOracletraztodas. Entretanto,tambémexisteoinversodo
DISTINCT, chamado ALL. Embora quase não o vemos, ele pode ser usado;
entretanto, não faz realmente diferença, pois seu resultado seria igual a não
informá-lo.
7.7 Relacionamentoentretabelas
É muito comum quando se está selecionando determinadas informações
surgir a necessidade de acessar outras tabelas com um mesmo comando
SELECT, para que seja possível reunir seus dados em um único resultado.
A travésdacláusula WHERE,conseguimosfazeraligaçãoentretabelase,con-
sequentemente,criarumvínculoentreasinformações. AestaligaçãooOra-
c l ei n t i t u l ad e“Join”, ou seja, relacionamento. Os tipos de relacionamento
existentessão:
INNER JOIN (tambémchamadodo SIMPLE JOIN ), OUTER
JOINe SELF JOIN .Vejaascaracterísticasdecadaumadiante.
7.8 INNERJOIN
Para que esta cláusula seja verdadeira, é necessário que as duas colunas que
estãosendocomparadaspossuamomesmovalor,ouseja,éprecisoquetenha
equivalêncianasduastabelas. Exemplo:
SQL> select ename, dname
2 from emp e, dept d
3 where e.deptno = d.deptno;
ENAME DNAME
120

## Página 135

CasadoCódigo Capítulo7. Manipulaçãodetabelas
---------- --------------
SMITH RESEARCH
ALLEN SALES
WARD SALES
JONES RESEARCH
MARTIN SALES
BLAKE SALES
CLARK ACCOUNTING
SCOTT RESEARCH
KING ACCOUNTING
TURNER SALES
ADAMS RESEARCH
JAMES SALES
FORD RESEARCH
MILLER ACCOUNTING
14 rows selected.
SQL>
Noteque,nesteexemplo,existeumrelacionamentoentreastabelas EMPe
DEPT,atravésdacoluna DEPTNO.Esterelacionamentoéquefazasduastabe-
las conversarem e retornarem as informações correspondentes. Se olharmos
separadamente cada tabela, podemos observar que nem todos os departa-
mentosapareceramnoresultadodo
SELECT.Observeatabela DEPT:
SQL> select * from dept order by deptno;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
SQL>
A go raolheatabelaEMP:
121

## Página 136

7.8. INNERJOIN CasadoCódigo
SQL> select ename, deptno
from emp
order by 2;
ENAME DEPTNO
---------- ---------
CLARK 10
KING 10
MILLER 10
JONES 20
FORD 20
ADAMS 20
SMITH 20
SCOTT 20
WARD 30
TURNER 30
ALLEN 30
JAMES 30
BLAKE 30
MARTIN 30
14 rows selected.
SQL>
Secompararmosacoluna DEPTNOdatabela EMPcomadatabela DEPT
vamos perceber que o departamento OPERATIONS (código 40) não apa-
rece para nenhum empregado. Logo, não há uma relação entre este depar-
tamentocomalgumempregadocadastrado. Sendoassim,elesnãoaparecem
no
SELECTondelistamosempregadoscomseusrespectivosdepartamentos.
EsteéotipomaiscomumderelacionamentoentretabelasusadosnoOracle:
duasoumaistabelasserelacionandoparaformarumúnicoresultadoemum
comandoSQL.
O Oracle, em versões anteriores à 9i, tinha uma forma peculiar de tra-
balhar com relacionamentos entre tabelas. Ele possuía uma sintaxe própria,
ou seja, não utilizava a sintaxe do padrão ANSI (SQL92) para estes relacio-
namentos. Contudo,opadrãoANSI( AmericanNationalStandardsInstitute )
fi c o uf o rt en a sv e r sõe sm a i sr ec e n t e sd oba n c oee s táset o rn a n d oon o v opa -
122

## Página 137

CasadoCódigo Capítulo7. Manipulaçãodetabelas
drão recomendado pela própria Oracle, por vários motivos, inclusive com a
propostadeganhosdedesempenhoatravésdoseuuso.
Destaforma, paracadatipo derelacionamento explicadoaqui, colocarei
tambémaformadeescrevê-lonopadrãoANSI.Assim,vocêteráaoportuni-
dadedeconheceropadrãoOracle,utilizadoemversõesanterioresdobanco
de dados, e também nas versões novas pois a Oracle mantém o seu padrão
porquestõeshistóricas(pelomenosporenquanto) evocêtambémverácomo
escreverrelacionamentosentretabelasutilizandoopadrãoANSI,onovopa-
drãosuportadopelaOracle.
PadrãoANSISQL92–INNERJOIN
Conforme a documentação da Oracle para as versões mais recentes do
banco, por exemplo, a versão 11G, existe ainda outra forma de classificar e
utilizar os relacionamentos
INNER JOIN entre as tabelas. São os chamados
JOINSNATURAL.Dentrodesteconceito,sãoutilizadasascláusulas NATURAL
JOIN, USING e ON para montar outras formas de relacionamento. Só pre-
cisamos ressaltar o que já conversamos sobre as versões anteriores à versão
Oracle9i: asintaxedos
JOINSeradiferentedospadrõesANSI.Destaforma,
este novo padrão, que está em conformidade com o SQL:1999, não funciona
emversõesanteriores. ConformedocumentaçãodaprópriaOracle,paraver-
sõesanterioresà9i,estenovopadrãonãoofereciabenefíciosdedesempenho
para a sintaxe de
JOIN.Talvez, esse seria o motivo pelo qual a Oracle não
tenhaadotadoestepadrãodesdeoinício.
Uma das coisas que você vai notar é que no padrão ANSI existe mais de
uma forma de escrever um relacionamento do tipoINNER JOIN . Mas não
sepreocupe,analisandoestasformasvocêtambémvaiperceberqueointuito
foisimplificaraescritaetornarmaisclaraaleituradocomandoSQL.Oscon-
ceitossãoosmesmos,inclusiveparaosoutrostiposderealcionamento,desde
o
OUTER JOIN ou até mesmo oSELF JOIN . A seguir, alguns exemplos e
regrasutilizandoestascláusulas.
CláusulaNATURALJOIN
Para caracterizarmos um relacionamento doNATURAL JOIN , precisa-
mos seguir a sua premissa básica: a possibilidade de unir duas tabelas com
123

## Página 138

7.9. CláusulaUSING CasadoCódigo
basenomesmonomedecoluna. Vejaalgumasregrascomrelaçãoaestetipo
derelacionamento:
•A c l á u s u l aNATURAL JOIN tem como base todas as colunas das duas
tabelasquetêmomesmono me;
• Ela seleciona as linhas a partir de duas tabelas que têm valores iguais
emtodasascolunascorrespondentes;
• Se as colunas que têm os mesmos nomes tiverem tipos de dados dife-
rentes,seráretornadoumerro.
Vejaumexemplo:
SQL> select dname, ename, sal
from dept
natural join emp
Como pode ser visto neste exemplo, estamos selecionando os nomes
dos funcionários, nomes dos empregados e seus respectivos salários. Note
que o relacionamento entre as duas tabelas foi realizadoatravés de um mé-
todo
INNER JOIN ,utilizandoacláusula NATURAL JOIN pararelacioná-las.
Neste caso, não é necessário relacionar as colunas de forma explícita, pois as
duas tabelas estão sendo relacionadas por este tipo de cláusula, a
NATURAL
JOIN.Portanto,todootrabalhoficaacargodomotordobancodedados. Ele
iráconsultaradefiniçãodastabelasutilizadasnocomandoSQLàprocuradas
colunasquecombinamconformeasregrasdefinidasparaestetipoderelaci-
o namen to ,col unasco momesmono me,mesmoti podedadoetamanho .
7.9 CláusulaUSING
Enquantonousodas NATURAL JOINS vocênãonecessitaespecificarasco-
lunas,poisnestecasoéprecisoapenasexistiremcolunascomosmesmosno-
mesetipodedadosentreastabelas,nosrelacionamentosutilizandoacláusula
USINGénecessárioespecificá-las. Naverdade,éparaexatamenteestefimque
estacláusulaserve. Elaéutilizadaparaquandovocênecessitarespecificar,de
formaexplícita,osnomesdascolunas. Vejaaseguir,emquaiscasos:
124

## Página 139

CasadoCódigo Capítulo7. Manipulaçãodetabelas
• Se várias colunas tiverem os mesmos nomes, mas tipos de dados que
não correspondem, usecláusula USING para especificar as colunas
para a EQUIJOIN ( EQUIJOINS tambémsão chamadasde %SIMPLE
JOINSou INNER JOINS );
• U seacláusula USINGparacorrespondersomenteumacolunaquando
houvermaisdeumacolunacorrespondente;
• Ascláusulas NATURAL JOIN e USINGsãomutuamenteexclusivas;
• Frequentemente,estetipodejoinenvolvecomplementosdechavepri-
máriaeestrangeira.
Vejaumexemploonémostradaauniãodatabeladeempregadosedepar-
tamentos, com intuito de recuperar a localização (LOCATION_ID) de cada
empregado.
SQL> select employee_id, last_name
location_id, department_id
from employees JOIN departments
USING (department_id);
EMPLOYEE_ID LOCATION_ID DEPARTMENT_ID
----------- ------------------------- -------------
100 King 90
101 Kochhar 90
102 De Haan 90
103 Hunold 60
104 Ernst 60
105 Austin 60
106 Pataballa 60
107 Lorentz 60
108 Greenberg 100
... 000
205 Higgins 110
206 Gietz 110
106 rows selected.
SQL>
125

## Página 140

7.9. CláusulaUSING CasadoCódigo
R e g r a sp a r aou s od ea p e l i d o sd et a b e l ac o mou s od ac l á u s u l a
USING
• Não qualifique (comnome de tabela ou apelido) uma coluna que é
usadanaclá usula
• SeamesmacolunaforusadaemqualqueroutrapartedainstruçãoSQL,
nãolhedêumapelido,casocontrário,aexecuçãoretornaráumerro.
• Colunas que são comuns nas duas tabelas, mas não são usadas na
cláusula USING devem ser prefixadas com um apelido de tabela, caso
contrário, você receberá a seguinte mensagem de erro “column ambi-
guouslydefined.”
Vejaumexemplo:
SQL> select l.city, d.department_name
from locations l JOIN departments d
USING (location_id)
where d.location_id = 1400;
where d.location_id = 1400
*
ERROR at line 4:
ORA-25154: column part of USING clause cannot have qualifier
SQL>
Note, neste exemplo, que ao colocarmos um apelida na coluna LOCA-
TION_ID,quesetratadeumacolunautilizadanacláusulaUSING,umerro
foigerado. Vejaagora,comodeveriaserestecomando:
SQL> select l.city, d.department_name
from locations l JOIN departments d
USING (location_id)
where location_id = 1400
/
CITY DEPARTMENT_NAME
126

## Página 141

CasadoCódigo Capítulo7. Manipulaçãodetabelas
------------------------------ ------------------------------
Southlake IT
SQL>
CláusulaON
AcláusulaONpossibilitavocêatornarexplícitatodasascondiçõesdere-
lacionamentosentretabelas. Nãosóaquelasexclusivas,aquelasquepossuem
ligaçõesdechavesprimáriascomchavesestrangeira. Destaforma,paracasos
que não for possível utilizar as cláusulas
NATURAL JOIN ou USING,utilize
aclá usula ON.Aseguir,algumascaracterísticas:
• Acondiçãode JOINparaa JOIN NATURAL ébasicamenteumaequi-
join de todas as colunas com o mesmo nome. Ou seja, o era implícito
antes,podeagoradecolocadodeformaexplícitaatravésdousodacláu-
sula
ON.
• U s eac l á u s u l aON para especificar condições arbitrárias, ou seja, con-
dições não lógicas, que fugiriam as regras de umNATURAL JOIN ,o u
especificar colunas a serem unidas. Por exemplo, colunas com nomes
diferentes.
• A condição de
JOIN é separada de outras condições de pesquisa ou
filtrosnacláusula WHERE.
•A c l á u s u l aON facilita a compreensão do código, pois torna tudo mais
explícitoedeformaorganizada.
• Useapelidosdetabelasparaqualificarascolunasutilizadasnacláusula
ON,quandoosno mesdascol unasfo r emiguais.
Vejaumexemplo:
SQL> select e.employee_id, e.last_name, e.department_id,
d.department_id, d.location_id
from employees e JOIN departments d
ON (e.department_id = d.department_id)
127

## Página 142

7.9. CláusulaUSING CasadoCódigo
/
EMPLOYEE_ID LAST_NAME DEPARTMENT_ID DEPARTMENT_ID LOCATION_ID
----------- ------------ ------------- ------------- -----------
100 King 90 90 1700
101 Kochhar 90 90 1700
102 De Haan 90 90 1700
103 Hunold 60 60 1400
104 Ernst 60 60 1400
105 Austin 60 60 1400
106 Pataballa 60 60 1400
...
201 Hartstein 20 20 1800
202 Fay 20 20 1800
203 Mavris 40 40 2400
204 Baer 70 70 2700
205 Higgins 110 110 1700
206 Gietz 110 110 1700
106 rows selected.
SQL>
Veja que neste exemplo, as tabelas foram unidas pela coluna DEPART-
MENT_ID na cláusula ON, sendo que as colunas foram rotuladas com os
respectivos apelidos, conforme definido nas tabelas. Vejamos agora, outros
dois exemplos, um mostrando como trabalhar com várias tabelas utilizando
ac lá u s ula
ON e, também, outro exemplo mostrando como inserir condições
adicionaisemumaJOIN.
TrabalhandocommaisdeduastabelasusandoacláusulaON:
SQL> select employee_id, city, department_name
from employees e
JOIN departments d
ON d.department_id = e.department_id
JOIN locations l
ON d.location_id = l.location_id;
EMPLOYEE_ID CITY DEPARTMENT_NAME
128

## Página 143

CasadoCódigo Capítulo7. Manipulaçãodetabelas
----------- ------------------------------ ---------------------
100 Seattle Executive
101 Seattle Executive
102 Seattle Executive
103 Southlake IT
104 Southlake IT
105 Southlake IT
...
205 Seattle Accounting
206 Seattle Accounting
106 rows selected.
SQL>
Inserindocondições adicionais em uma JOIN, utilizando as cláusulas
ANDe WHERE
SQL> select e.employee_id, e.last_name, e.department_id,
d.department_id, d.location_id
from employees e JOIN departments d
on (e.department_id = d.department_id)
and e.manager_id = 149;
EMPLOYEE_ID LAST_NAME DEPARTMENT_ID DEPARTMENT_ID LOCATION_ID
----------- ------------ ------------- ------------- -----------
179 Johnson 80 80 2500
177 Livingston 80 80 2500
176 Taylor 80 80 2500
175 Hutton 80 80 2500
174 Abel 80 80 2500
SQL>
SQL> select e.employee_id, e.last_name, e.department_id,
d.department_id, d.location_id
from employees e JOIN departments d
on (e.department_id = d.department_id)
where e.manager_id = 149;
129

## Página 144

7.9. CláusulaUSING CasadoCódigo
EMPLOYEE_ID LAST_NAME DEPARTMENT_ID DEPARTMENT_ID LOCATION_ID
----------- ------------ ------------- ------------- -----------
179 Johnson 80 80 2500
177 Livingston 80 80 2500
176 Taylor 80 80 2500
175 Hutton 80 80 2500
174 Abel 80 80 2500
SQL>
No-Equijoins
Relacionamentosentretabelasquenãosãoconstituídosporumoperador
de igualdade são chamados deNo-Equijoins. Geralmente, estes relacio-
namentos envolvem tabelas que possuem uma ligação, contudo, não uma li-
gaçãodiretaatravésdeumaequijoin,massim,umrelacionamentocombase
emumgrupoourangedevalores. Vejaoexemploaseguir:
SQL> select e.last_name, e.salary, j.grade_level
from employees e JOIN job_grades j
on e.salary
between j.lowest_sal and j.highest_sal;
LAST_NAME SALARY GRA
------------------------- ---------- ---
Olson 3074.61 B
Philtanker 3221.02 B
Markle 3221.02 B
Landry 3513.84 B
Gee 3513.84 B
Marlow 3660.25 B
Vargas 3660.25 B
...
Hartstein 19033.3 E
Partners 19765.35 E
Russell 20497.4 E
De Haan 24889.7 E
Kochhar 24889.7 E
King 35138.4 F
130

## Página 145

CasadoCódigo Capítulo7. Manipulaçãodetabelas
107 rows selected.
SQL>
OUTERJOIN
O uso desta cláusula se dá quando mesmo que não exista a equivalência
entreastabelas,osdadossejampreservadoseretornados. Exemplo:
SQL> select ename, dname
from emp e, dept d
where e.deptno(+) = d.deptno;
ENAME DNAME
---------- --------------
SMITH RESEARCH
ALLEN SALES
WARD SALES
JONES RESEARCH
MARTIN SALES
BLAKE SALES
CLARK ACCOUNTING
SCOTT RESEARCH
KING ACCOUNTING
TURNER SALES
ADAMS RESEARCH
JAMES SALES
FORD RESEARCH
MILLER ACCOUNTING
OPERATIONS
15 rows selected.
SQL>
Assim como foi visto no exemplo comINNER JOIN ,a q u it a m b é mv e -
mos um relacionamento entre as tabelas EMP e DEPT, através da coluna
DEPTNO. Contudo, também percebemos a expressão (+) que indica ao co-
131

## Página 146

7.9. CláusulaUSING CasadoCódigo
mandoSQLquemesmoquenãohajadeterminadoscódigosdedepartamento
na tabela EMP, os mesmos devem ser mostrados. Esta expressão sempre é
colocadajuntodacolunaondeosvalorespodemnãoexistir. Nestecaso, po-
demos ter departamentos que não possuem empregados cadastrados. Logo
a expressão é colocada ao lado da coluna DEPTNO da tabela EMP. Se for-
mos olhar separadamente cada tabela, podemos observar que nem todos os
departamentosexistemnatabelaEMP.Observe:
SQL> select * from dept;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
SQL>
A go raolheatabelaEMP:
SQL> select ename, deptno
from emp;
ENAME DEPTNO
---------- ---------
SMITH 20
ALLEN 30
WARD 30
JONES 20
MARTIN 30
BLAKE 30
CLARK 10
SCOTT 20
KING 10
TURNER 30
ADAMS 20
JAMES 30
FORD 20
132

## Página 147

CasadoCódigo Capítulo7. Manipulaçãodetabelas
MILLER 10
14 rows selected.
SQL>
SecompararmosnovamenteacolunaDEPTNOdatabelaEMPcomada
tabelaDEPTvamosperceberqueodepartamentoOPERATIONS(código40)
nãoapareceparanenhumempregado. Entretanto,estedepartamentoaparece
em nosso resultado, na primeira query pelo fato de o nosso relacionamento
serdotipoOUTERJOIN.
OrelacionamentodotipoOUTERJOINaindapodeserclassificadocomo
LEFT ou RIGHT. Contudo, no padrão Oracle, a diferenciação de um e de
outro,LEFTOUTERJOINouRIGHTOUTERJOIN,émaissimbólica,pois
oquemandaéondeosinal(+)estáposicionado. Nestecaso,oladodacoluna
ondeestiverosinal(+)éoladoondepodenãoexistiraequivalência. Aseguir,
veremos o padrão ANSI, onde o conceito de LEFT OUTER JOIN e RIGHT
OUTER JOIN se faz mais claro no momento da interpretação de comando
SQL.
PadrãoANSISQL92–OUTERJOIN
A implentação conceitual doOUTER JOIN para o padrão ANSI segue a
mesmalinhadopadrãoOracle. Oquemudaéaformacomoescrevemosoco-
mandoeindentificamosotipodorelacionamento. Sóressaltando,enquanto
umrelacionamentodotipo
INNER JOIN objetivaaexistênciadeumaequi-
valência total entre os lados comparados, o relacionamento do tipoOUTER
JOIN, prevê situações onde possa não existir esta equivalência em todos os
casos.
O cenário mais comum no uso deOUTER JOINS , eu diria que 99% dos
casos, são relacionamentos de Joins INNER sendo comparadas com Joins
OUTER.Destaforma,auniãoentreduastabelasqueretornaosresultadosde
uma junção
INNER JOIN e de linhas sem equivalencia da tabela esquerda
é chamada deLEFT OUTER JOIN . Logo, o retorno de uma junçãoINNER
JOINcomlinhassemcorrespondênciadatabeladiretaéchamadade RIGHT
OUTER JOIN . No entanto, ainda existe outro cenário, que é quando existe
133

## Página 148

7.9. CláusulaUSING CasadoCódigo
uma união entre duas tabelas que retornam os resultados de umaINNER
JOIN e os resultados de umaLEFT OUTER JOIN e RIGHT OUTER JOIN .
Estetipoderelacionamento OUTER JOIN AOraclechamade FULL OUTER
JOIN.Aseguir,veremosexemplosdostrêstiposde OUTER JOINS existente:
LEFT OUTER , RIGTH OUTER e FULL OUTER .
ExemplodeLEFTOUTERJOIN:
SQL> select ename, dept.deptno, loc
from dept left outer join emp
on emp.deptno = dept.deptno
/
ENAME DEPTNO LOC
---------- --------- -------------
SMITH 20 DALLAS
ALLEN 30 CHICAGO
WARD 30 CHICAGO
JONES 20 DALLAS
MARTIN 30 CHICAGO
BLAKE 30 CHICAGO
CLARK 10 NEW YORK
SCOTT 20 DALLAS
KING 10 NEW YORK
TURNER 30 CHICAGO
ADAMS 20 DALLAS
JAMES 30 CHICAGO
FORD 20 DALLAS
MILLER 10 NEW YORK
EDUARDO 20 DALLAS
50 BRASIL
40 BOSTON
60 BRASIL
18 rows selected.
SQL>
Neste exemplo, estamos recuperando todos os empregaos com seus res-
pectivosdepartamentoselocalizações. Notequeosdepartamentosondenão
134

## Página 149

CasadoCódigo Capítulo7. Manipulaçãodetabelas
háempregadosalocados,tambémsãoretornadospelocomandoSELECT.Se
analisarmos o comando, estamos selecionando os dados das tabelas DEPT e
EMP, relacionando-as através de um relacionamento do tipo
LEFT OUTER
JOIN, onde podemos observar que a tabela da esquerda (DEPT) é a tabela
ondepodenãoexistircorrespondência,ouseja,nossatabelaLEFT.
Em resumo o tipo de relacionamento LEFT OUTER JOIN nos diz:
mesmoquenãoexistacorrespondênciacomatabeladaesquerda,tragaseus
dados,mesmoassim.
Exemplode
RIGHT OUTER JOIN :
SQL> select ename, dname
from dept right outer join emp
on emp.deptno = dept.deptno;
ENAME DNAME
---------- --------------
FORD RESEARCH
ADAMS RESEARCH
SCOTT RESEARCH
JONES RESEARCH
SMITH RESEARCH
JAMES SALES
TURNER SALES
BLAKE SALES
MARTIN SALES
WARD SALES
ALLEN SALES
MILLER
KING
CLARK
14 rows selected.
SQL>
Utilizando o mesmo exemplo, vamos trocar o tipo de relacionamento.
Agoravamosrelacionarastabelasatravésdeum RIGHT OUTER JOIN .Note
quecontinuamosrecuperandotodososempregadoscomseusrespectivosde-
135

## Página 150

7.9. CláusulaUSING CasadoCódigo
partamentos e localizações. Contudo, veja que os empregados que não es-
tãoalocadosemdepartamentoalgum,tambémsãoretornadospelocomando
SELECT.Voltandoaanalisarocomando,estamosselecionandoosdadosdas
tabelas DEPT e EMP, mas, agora, relacionando-as através de um relaciona-
m e n t od oti po
RIGHT OUTER JOIN , onde a tabela da direita (EMP) é a ta-
belaondepodenãoexistircorrespondência,ouseja,nossatabelaRIGHT.
Em resumo o tipo de relacionamento RIGHT OUTER JOIN nos diz:
mesmoquenãoexistacorrespondênciacomatabeladadireita,tragaseusda-
dos,mesmoassim. Comojácomentado,dentrodopadrãoANSIaindatemos
uma formade relacionamentoque échamada de
FULL OUTER JOIN .P a ra
estaformaderelacionamentonãoháumasimilarnoOracle. Elaconsisteem
buscar as linhas que possuem ligações entre as tabelas (
INNER JOIN ), mas
também as que não existem entre as duas (LEFT OUTER JOIN e RIGHT
OUTER JOIN ),semr esul taremumPr od u toCartesiano .
Contudo,emversõesmaisrecentes,oOracleServeraceitaopadrãoANSI.
Vejaoexemploaseguir.
SQL> select ename, dept.deptno, loc
from emp full outer join dept
on emp.deptno = dept.deptno
/
ENAME DEPTNO LOC
---------- ---------- -------------
SMITH 20 DALLAS
ALLEN 30 CHICAGO
WARD 30 CHICAGO
JONES 20 DALLAS
MARTIN 30 CHICAGO
BLAKE 30 CHICAGO
CLARK
SCOTT 20 DALLAS
KING
TURNER 30 CHICAGO
ADAMS 20 DALLAS
JAMES 30 CHICAGO
FORD 20 DALLAS
136

## Página 151

CasadoCódigo Capítulo7. Manipulaçãodetabelas
MILLER
40 BOSTON
10 NEW YORK
16 rows selected.
SQL>
Conforme pode ser visto, oSELECT retornou todos os empregados e
departamentos,mesmoosquenãosãoequivalentes.
Em resumo o tipo de relacionamento FULL OUTER JOIN nos diz:
mesmo que não exista correspondência com a tabela da direita ou com a ta-
beladaesquerda,tragaseusrespectivosdados,mesmoassim.
SELFJOIN
Este tipo de relacionamento indica que uma tabela também pode se re-
lacionarcomelamesma. Emalgunscasospodemostertabelasquepossuem
maisdeumtipodeinformação .U mexem ploéatabelaEMP .N elatemosin-
formaçõesdeempregados,mastambémdegerentesassociados,onde,através
da coluna MGR, nós conseguimos ver os gerentes de cada empregado. Note
queoscódigosdosgerentesinseridosnestacolunasãoosquetambémapare-
cemnacolunaEMPNO,ouseja,sãoempregados,também. Vejaoexemplo:
SQL> select e.ename empregado, g.ename gerente
from emp e, emp g where e.mgr = g.empno order by 1;
EMPREGADO GERENTE
---------- ----------
ADAMS SCOTT
ALLEN BLAKE
BLAKE KING
CLARK KING
FORD JONES
JAMES BLAKE
JONES KING
MARTIN BLAKE
MILLER CLARK
137

## Página 152

7.9. CláusulaUSING CasadoCódigo
SCOTT JONES
SMITH FORD
TURNER BLAKE
WARD BLAKE
13 rows selected.
SQL>
Note que para usarmos a tabela EMP duas vezes na cláusulaFROM,s e m
ocorrer o erro de ambiguidade entre as colunas, nós utilizamos umALIAS
diferenteparacadaumadelas.
PadrãoANSISQL92–SELFJOIN
Para unir uma tabela com ela mesma, criando assim, uma SELF
JOIN,também existe uma forma dentro do padrão ANSI.Crie um relaciona-
mentoSELFJOINatravésdacláusulaON.
SQL> select worker.last_name emp, manager.last_name mgr
from employees worker JOIN employees manager
on (worker.manager_id = manager.employee_id);
EMP MGR
------------------------- -------------------------
Hartstein King
Zlotkey King
Cambrault King
Errazuriz King
Partners King
Russell King
Mourgos King
Vollman King
...
Hutton Zlotkey
Abel Zlotkey
Fay Hartstein
Gietz Higgins
138

## Página 153

CasadoCódigo Capítulo7. Manipulaçãodetabelas
106 rows selected.
SQL>
ProdutoCartesianoouProdutoCruzado
Sempre quando informamos mais de uma tabela na cláusula FROM, de-
vemos,obrigatoriamente,colocarosrelacionamentosreferentesaestastabe-
las. Caso isto não seja feito, o Oracle não gera uma mensagem de erro. Ao
invésdisso,elegeraumresultadooqualchamamosde“ProdutoCartesiano”
ou“ProdutoCruzado”. Imaginemosduastabelasemum comando
SELECT.
A tabela “A” com 10 registros e a tabela “B” com 20 registros. Caso não seja
informado um relacionamento na cláusula
WHERE, eseja executadoeste co-
mandoSQL,oresultadoseráoretornode200linhas,ouseja,paracadalinha
databela“A”,eleretornarátodasaslinhasdatabela“B”,ouvice-versa. Exem-
plo:
SQL> select ename, dname
from emp, dept
where emp.deptno = 20;
ENAME DNAME
---------- --------------
SMITH ACCOUNTING
SMITH RESEARCH
SMITH SALES
SMITH OPERATIONS
JONES ACCOUNTING
JONES RESEARCH
JONES SALES
JONES OPERATIONS
SCOTT ACCOUNTING
SCOTT RESEARCH
SCOTT SALES
SCOTT OPERATIONS
ADAMS ACCOUNTING
ADAMS RESEARCH
ADAMS SALES
139

## Página 154

7.9. CláusulaUSING CasadoCódigo
ADAMS OPERATIONS
FORD ACCOUNTING
FORD RESEARCH
FORD SALES
FORD OPERATIONS
20 rows selected.
SQL>
ParacadalinhaencontradanatabelaDEPTfoiretornadatodasaslinhas
databeladeEMP.
PadrãoANSISQL92–ProdutoCartesianoouProdutoCruzado
Paragerarprodutocartesianoouprodutocruzado,comotambémécha-
mado,utilizamosacláusulaCROSSJOIN.
SQL> select last_name, department_name
from employees
cross join departments;
LAST_NAME DEPARTMENT_NAME
------------------------- -----------------------
Abel Administration
Ande Administration
Atkinson Administration
Austin Administration
...
Vishney Payroll
Vollman Payroll
Walsh Payroll
Weiss Payroll
Whalen Payroll
Zlotkey Payroll
2889 rows selected.
SQL>
140

## Página 155

CasadoCódigo Capítulo7. Manipulaçãodetabelas
ALIASdeTabelaeColuna
ALIASéumapelidoquepodemosdarparaumatabelaoucolunanomo-
mento que estivermos escrevendo um comando SQL. OsALIAS de tabela
são comumente utilizados em SELECTS quando trabalhamos com mais de
umatabelanacláusula FROM.Quandoistoaconteceprecisamoscriarosrela-
cionamentosnacláusulaWHEREidentificandocadacolunadestesrelaciona-
mentos. Porconvenção,nagrandemaioriadasvezes,ascolunasderelaciona-
mentopossuemomesmonomeentreastabelasparafacilitaroentendimento
do modelo de dados. Com isto, ao montar o comando
SELECT precisamos
dizerdequaiscolunasestamosnosreferindo. Comoosnomesdetabelasge-
ralmente são nomes longos, para facilitar a identificação e a que se referem,
ao invés de colocarmos o nome da tabela na frente das colunas, nós usamos
um
ALIAS.U s u a l m e n t eoALIAS éu mn o m ep e q u e n of o r m a d op o rp o u -
coscaracteres,geralmenteformadopelasiniciaisdonomedaprópriatabela,
gerando assim um rótulo para a mesma. Sua utilidade é simplesmente criar
uma identificação para o objeto, auxiliando na construção de um comando
visualmentemaisenxuto.
SQL> select emp.first_name
,emp.email
,emp.job_id
,dep.department_name
from employees emp
,departments dep
where emp.department_id = dep.department_id
and dep.department_id = 50
and emp.manager_id = 100;
FIRST_NAME EMAIL JOB_ID DEPARTMENT_NAME
-------------------- ---------------- ---------- ---------------
Matthew MWEISS ST_MAN Shipping
Adam AFRIPP ST_MAN Shipping
Payam PKAUFLIN ST_MAN Shipping
Shanta SVOLLMAN ST_MAN Shipping
Kevin KMOURGOS ST_MAN Shipping
SQL>
141

## Página 156

7.9. CláusulaUSING CasadoCódigo
Não diferente do uso para tabelas, o ALIAS de coluna também é utili-
zado para criar uma identificação. Contudo, na grande maioria das vezes
não é usada para simplificar o nome e sim para clarificar seu significado.
O ALIAS de coluna pode ser gerado de duas formas, utilizando ou não as-
pas duplas (“”). Quando queremos mostrar uma identificação mais forma-
tada, podemos usar aspas duplas para isto. Por exemplo, temos a coluna
DEPTNOqueéocódigododepartamento.Sequisermosmostrarumaiden-
tificaçãoformatada,ouseja,maissignificativa,podemosdeclararoALIASda
colunacomo“CódigodoDepartamento”. AodeclararmosdestaformaoOra-
cle mostra esta descrição como sendo o nome da coluna ao mostrar o resul-
tadodoSELECT.Seoptarmospornãoutilizaraspasparaidentificaracoluna,
nãopodemos,porexemplo,terdescriçõesseparadasporespaçosembranco.
Isto causaria confusão, dando a impressão de estarmos informando vários
ALIASparaamesmacoluna. Nestecaso,poderíamosfazerdestaforma,CO-
DIGO_DO_DEPARTAMENTO.
Apelidosdecolunas
Para finalizar, você pode perceber que em alguns casos poderá ver a ex-
pressão
AS antecedendo o apelido da coluna. Contudo, a utilização ou não
destaexpressãonãofaránenhumadiferença. Nestecaso,vocêpodeoptarpor
utilizá-laounão,poisoresultadoseráomesmo. Vejaumexemplo:
SQL> select last_name AS "Último Nome"
,job_id AS cargo
,salary AS "Salário"
from employees
where (job_id = ’SA_REP’
or job_id = ’AD_PRES’)
and salary > 15000
/
Último Nome CARGO Salário
------------------------- ---------- ----------
King AD_PRES 35138,40
Vishney SA_REP 15373,05
Ozer SA_REP 16837,15
Abel SA_REP 16105,10
142

## Página 157

CasadoCódigo Capítulo7. Manipulaçãodetabelas
SQL>
Dessaformaocomandoficaatéumpoucomaislegível.
143

## Página 159

Capítulo8
Selecionandodados
8.1 Selecionandodados
SELECT
Co mesteco mando ,vocêselecio nalinhasecol unasdeumao umaistabelas.
Selecionandoascolunas EMPNOe ENAMEdatabela EMP:
SQL> select empno, ename from emp;
EMPNO ENAME
--------- ----------
7369 SMITH
7499 ALLEN
7521 WARD
7566 JONES

## Página 160

8.1. Selecionandodados CasadoCódigo
7654 MARTIN
7698 BLAKE
7782 CLARK
7788 SCOTT
7839 KING
7844 TURNER
7876 ADAMS
7900 JAMES
7902 FORD
7934 MILLER
14 rows selected.
SQL>
SELECT*
O * substituitodasascolunasdatabela.
SQL> select * from dept;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
SQL>
ROWNUM
ROWNUMéumapseudocolunaqueindicaumnúmerosequencialreferente
àslinhasretornadasqueatendamacláusula WHEREdeumcomando SELECT.
Você também poderá utilizá-la na própria cláusulaWHERE como forma de
restrição. Neste caso, se no comandoSELECT houver uma cláusulaORDER
BY, a restrição será aplicada antes da ordenação. Veja alguns exemplos a se-
guir.
SQL> select rownum, deptno, dname from dept;
146

## Página 161

CasadoCódigo Capítulo8. Selecionandodados
ROWNUM DEPTNO DNAME
--------- --------- --------------
1 10 ACCOUNTING
2 20 RESEARCH
3 30 SALES
4 40 OPERATIONS
55 0 T I
SQL>
Nesse exemplo, a colunaROWNUM traz um número sequencial para cada
registro retornado.
SQL> select ename, job, deptno from emp order by deptno;
ENAME JOB DEPTNO
---------- --------- ---------
CLARK MANAGER 10
KING PRESIDENT 10
MILLER CLERK 10
JONES MANAGER 20
FORD ANALYST 20
ADAMS CLERK 20
SMITH CLERK 20
SCOTT ANALYST 20
WARD SALESMAN 30
TURNER VENDEDOR 30
ALLEN SALESMAN 30
JAMES CLERK 30
BLAKE MANAGER 30
MARTIN SALESMAN 30
14 rows selected.
SQL>
SQL> select ename, job, deptno from emp where
rownum < 5 order by deptno;
147

## Página 162

8.1. Selecionandodados CasadoCódigo
ENAME JOB DEPTNO
---------- --------- ---------
SMITH CLERK 20
JONES MANAGER 20
WARD SALESMAN 30
ALLEN SALESMAN 30
SQL>
Note neste último exemplo que, primeiramente, foi aplicada a restrição
paratrazerosquatroprimeirosregistros,depoisfoiaplicadaaordenação. No
SELECT anterior a este, vimos que, se fosse aplicada somente a ordenação
dosdados,visualizandotodooresultado,poderíamosconstatarqueosquatro
primeirosregistrosseriamtodosdodepartamento10e20. Agoravejatodoo
resultadosemordenação.
SQL> select ename, job, deptno from emp;
ENAME JOB DEPTNO
---------- --------- ---------
SMITH CLERK 20
ALLEN SALESMAN 30
WARD SALESMAN 30
JONES MANAGER 20
MARTIN SALESMAN 30
BLAKE MANAGER 30
CLARK MANAGER 10
SCOTT ANALYST 20
KING PRESIDENT 10
TURNER VENDEDOR 30
ADAMS CLERK 20
JAMES CLERK 30
FORD ANALYST 20
MILLER CLERK 10
14 rows selected.
SQL>
148

## Página 163

CasadoCódigo Capítulo8. Selecionandodados
ROWID
Cada linha armazenada no banco de dados tem um endereço. O banco
de dados Oracle usa o tipoROWID para armazenar o endereço (ROWID)d e
cadalinhanobancodedados. O ROWIDpodesermuitoútilnoscasosemque
queremosidentificarumvalorúnicoemdeterminadatabela,quandoatravés
dascolunasnelaexistentesnãoconseguimosestasingularidade.
Estetiposeencaixaemtrêscategorias:
• ROWIDsfísicos (PhysicalROWIDs): armazenamendereçosdelinhas
de tabelas padrões do Oracle (heap-organized tables), tabelas clusteri-
zadas (clustered tables) e tabelas e índices particionados. Estes IDs re-
presentam os endereços físicos, ou seja, levam em consideração as in-
formaçõesdosblocosdedadosarmazenadosfisicamentenodisco.
• ROWIDslógicos (Logical ROWIDs): armazenam os endereços de li-
nhasdetabelasindexadas( index-organizedtables). Osíndicesb-TREE
sebaseiamnos
ROWIDslógicosparamontarsuaarvoreeassimacele-
rarabuscapelosdadosemumaconsulta.
• ROWIDsestrangeiros (Foreign ROWIDs): são identificadores em ta-
belas estrangeiras, tais como tabelas do DB2 acessadas através de um
gateway. Elesnãosão
ROWIDspadrãodoOracleDatabase.
Segueumexemplo:
SQL> select rowid, d.* from dept d;
ROWID DEPTNO DNAME LOC
------------------ --------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
50 TI BRASIL
AAAAAAAAAAA 
AAAAAAAAAAB 
AAAAAAAAAAC 
AAAAAAAAAAD 
AAAAAAAAAAE 
AAAAAAAAAAF 60 ABC% BRASIL
6 rows selected.
SQL>
149

## Página 164

8.1. Selecionandodados CasadoCódigo
Paracadalinharetornada,existeum ROWIDespecífico.
Tabela DUAL
DUALéumatabelaquepossuiumacolunachamada DUMMY,eumúnico
registrocomovalorX.Trata-sedeumatabelacriadano SCHEMA SYS (que
éseudono)equeexisteporpadrãonobancoOracle. Elaéutilizadaquando
precisamosretornarumúnicovalor,porexemplo,ovalordeumaconstante,
expressão, retornar o resultado de cálculos numéricos e de datas ou pseudo-
colunas ou seja, algo que não se origina de tabelas de dados comuns. Seu
usoémuitocomumemprogramasousimplescomandosSQL.Suaestrutura
atende os requisitos da linguagem, pois contempla as cláusulas
SELECT e
FROMquesãoobrigatórias. Portanto,éumatabelacomooutraqualquer,em-
borapossuaumacaracterísticabemdefinida: adeauxiliaremdeterminadas
operações,sendodesnecessárioselecionartabelascomunsdedados.
Selecionandoosdadosdatabela
DUAL:
SQL> select * from dual;
D
-
X
SQL> select sysdate from dual;
SYSDATE
---------
13-APR-11
SQL>
Utilizando a tabela DUAL para cálculos com dados constantes, ou seja,
nãoutilizandodadosvindosdetabelasdobancodedados:
SQL> select 10*100/2 from dual;
10*100/2
---------
500
SQL> select mod (10,2) from dual;
MOD(10,2)
---------
150

## Página 165

CasadoCódigo Capítulo8. Selecionandodados
0
SQL>
8.2 SELECTFORUPDATE
Ao executar umSELECT com a opçãoFOR UPDATE , estamos bloqueando
as linhas da tabela selecionada. Como padrão, para o comandoSELECT,o
Oraclenãofazestebloqueio, mascomousodesterecursoelemudaa forma
padrão de bloqueio. É muito útil quando queremos garantir que o que esta-
mosvisualizandoemumdadomomentonãoestásendoalterado.
Paraliberarobloqueio,precisamosexecutarum
COMMITou ROLLBACK.
Vejaoexemploaseguir.
SQL> select * from dept for update ;
DEPTNO DNAME LOC
---------- -------------- -------------
10 ACCOUNTING FLORIDA
30 SALES CHICAGO
40 OPERATIONS BOSTON
43 ORDER MANAGER BRASIL
41 GENERAL LEDGER
42 PURCHASING
6 linhas selecionadas.
SQL>
No exemplo, estamos bloqueando todas as linhas da tabelaDEPT.C o n -
tudo,senestecomandoSQLtivéssemosalgumacláusula WHERErestringindo
oresultado,apenasestaslinhasretornadaséqueseriambloqueadas. Vejoou-
troexemplonasequência:
SQL> select employee_id, salary, commission_pct, job_id
from employees
where job_id = ’SA_REP’
for update
order by employee_id
/
EMPLOYEE_ID SALARY COMMISSION_PCT JOB_ID
151

## Página 166

8.2. SELECTFORUPDATE CasadoCódigo
----------- ---------- -------------- ----------
150 14641 .3 SA_REP
151 13908.95 .25 SA_REP
152 13176.9 .25 SA_REP
155 10248.7 .15 SA_REP
156 14641 .35 SA_REP
...
176 12591.26 .2 SA_REP
177 12298.44 .2 SA_REP
178 10248.7 .15 SA_REP
179 9077.42 .1 SA_REP
30 rows selected.
SQL>
Aqui estamos selecionando todos os empregados que têm como cargo
SA_REP. Como estamos aplicando umFOR UPDATE , todas as linhas e, so-
mente elas, estarão bloqueadas para qualquer alteração. Vale lembrar que,
paraliberá-las,precisamosexecutarum COMMITou ROLLBACK.
Você também pode bloquear linhas de mais de uma tabela. Isso é sim-
ples. Casoestejaaplicandoum FOR UPDATE emumcomandoSQLemcuja
cláusula há várias tabelas, automaticamente os registros listados serão blo-
queados. Aseguir,umexemplo:
SQL> select e.employee_id, e.salary, e.commission_pct
2 from employees e JOIN departments d
3 USING (department_id)
4 where job_id = ’ST_CLERK’
5 and location_id = 1500
6 FOR UPDATE
7 order by e.employee_id
8/
EMPLOYEE_ID SALARY COMMISSION_PCT
----------- ---------- --------------
125 4685.12
126 3953.07
127 3513.84
152

## Página 167

CasadoCódigo Capítulo8. Selecionandodados
128 3221.02
...
141 5124.35
142 4538.71
143 3806.66
144 3660.25
20 rows selected.
SQL>
Note que aqui estamos selecionando dados de duas tabelas. Estamos se-
lecionandoempregadosquepossuemcomocargo ST_CLERKecujalocaliza-
ção seja 1500. Logo, se tentássemos excluir dados, ou melhor, empregados
cujo cargo fosse ST_CLERK, não conseguiríamos, pois estes registros estão
bloqueados. O mesmo aconteceria se tentássemos excluir dados de departa-
mentocujalocalizaçãofosse 1500.
Casovocêdesejebloquearapenasumadastabelas,porexemplo,poderia
aplicar o FOR UPDATE informando a coluna da tabela que você quer blo-
quear. Vejaomesmoexemploanterior,agorainformandoacolunadatabela
aserbloqueada.
SQL> select e.employee_id, e.salary, e.commission_pct
2 from employees e JOIN departments d
3 using (department_id)
4 where job_id = ’ST_CLERK’
5 and location_id = 1500
6 FOR UPDATE of e.salary
7 order by e.employee_id
8/
EMPLOYEE_ID SALARY COMMISSION_PCT
----------- ---------- --------------
125 4685.12
126 3953.07
...
140 3660.25
141 5124.35
153

## Página 168

8.3. Selecionandoodestino CasadoCódigo
142 4538.71
143 3806.66
144 3660.25
20 rows selected.
SQL>
DEADLOCKS
Comousodobloqueiodedados,sendopelautilizaçãodo FOR UPDATE ,
LOCKouqualqueroutromeio,podeacontecerdetransaçõesficarembloque-
adas de tal forma que uma acabe por ter que esperar pela outra. A isso se dá
on o m ed eDEADLOCK. Por exemplo, uma transação “A” bloqueia determi-
nados registros. Outra transação “B” tenta atualizá-los. Ela ficará esperando
a transação ”A” liberar os registros. Todavia, aconteceu que, antes de a tran-
sação “B” acessar tais registros, ela acabou atualizando outra fonte, que será
utilizada pela transação “A” mais adiante. Quando a transação “A” for tentar
acessar tal fonte, não conseguirá, pois “B” não efetivou as transações. Nisto,
atransação“A”ficaráesperandopela“B”evice-versa. Geralmente,nobanco
de dados, há regras definidas para resolver este conflito, como por exemplo,
tem podeesperapo rumr ecurso .
8.3 Selecionandoodestino
FROM
Especifica o nome (ou nomes) da tabela de onde devem ser selecionadas as
linhas.
Selecionandodadosdastabelas
EMPe DEPT:
SQL> select ename, dname
from emp e, dept d
where e.deptno = d.deptno
and d.deptno = 20;
ENAME DNAME
---------- --------------
154

## Página 169

CasadoCódigo Capítulo8. Selecionandodados
SMITH RESEARCH
JONES RESEARCH
SCOTT RESEARCH
ADAMS RESEARCH
FORD RESEARCH
SQL>
Dentrodacláusula FROM,épossívelescrevercomandos SELECT,fazendo
comqueelefaçaopapeldeumatabelaouvisão.
SQL> select ename, dname
from emp e
,(select dname, deptno from dept) d
where e.deptno = d.deptno
and e.deptno = 20;
ENAME DNAME
---------- --------------
SMITH RESEARCH
JONES RESEARCH
SCOTT RESEARCH
ADAMS RESEARCH
FORD RESEARCH
SQL>
Notequeestãosendoselecionadosdadosdatabela EMPedatabela DEPT.
Contudo,atabela DEPTnãoestásendoacessadadiretamente,mas,sim,atra-
vésdeum SELECT,comosefosseuma view. Nestescasos,épossívelrestringir
colunasedados,senecessário.
8.4 Restringindodados
WHERE
Especificaacondiçãooucondiçõesqueaslinhasdevemsatisfazer. Acláusula
WHEREéutilizadacomoumaespéciedefiltroparaseuscomandosSQL.Éela
quemvairestringirabuscadosseusdados.
155

## Página 170

8.5. Escolhendolinhasecolunas CasadoCódigo
SQL> select first_name, email, country_name
from employees e
,departments d
,locations l
,countries c
where e.department_id = d.department_id
and d.location_id = l.location_id
and l.country_id = c.country_id
and c.country_name = ’Canada’
/
FIRST_NAME EMAIL COUNTRY_NAME
-------------------- ------------------------- ------------
Michael MHARTSTE Canada
Pat PFAY Canada
SQL>
Nesteexemplo, estamosselecionandodadosdeváriastabelas, utilizando
ac l á u s u l aWHERE para fazer as ligações entre elas e também para restringir
registros.
8.5 Escolhendolinhasecolunas
Atravésdocomando SELECT,podemosselecionarapenasaslinhasoucolu-
nasquedesejarmos.
SQL> select first_name, phone_number
from employees
where rownum < 5;
FIRST_NAME PHONE_NUMBER
-------------------- --------------------
Steven 515.123.4567
Neena 515.123.4568
Lex 515.123.4569
Alexander
515.423.4567
SQL>
156

## Página 171

CasadoCódigo Capítulo8. Selecionandodados
8.6 Utilizandooperadores
Algumas vezes, é preciso refinar a consulta para se obter o resultado espe-
rado. Neste caso, o uso de filtros é imprescindível para que possam ser feitas
restrições nos dados que serão buscados no banco de dados. Os filtros são
definidos no SQL com a cláusula
WHERE. Para representar estas condições,
existemosoperadoresrelacionaiseosoperadoreslógicos.
Operadoresrelacionais:
• >:m a i o rq u e
• <: menorque
• =: iguala
• <=: menoreiguala
• >=: maioreiguala
• <>ou!=: diferentede
Operadoreslógicos:
• AND:operador E,utilizadoparavalidarmaisdeumacondição;
• OR:operador OU,utilizadoparavalidarpelomenosumacondição;
• NOT:r ep r esen tanegaçãodeumasen tença;
• [NOT] BETWEEN: utilizado na restrição de intervalos de valores e
datas;
• [NOT] LIKE: útil na pesquisa aproximada por sua característica de
permitir caracteres curingas. O
% vai substituir uma cadeia de ca-
racteres,nãoimportandoquantosnemquais,eo _ vaisubstituirum
caractereapenas,nãoimportaqual;
• [NOT]IN :definemcondiçõescomconjuntodevalores;
157

## Página 172

8.6. Utilizandooperadores CasadoCódigo
• IS[NOT]NULL : verifica se o campo é nulo ou não. Sempre utilize
esteoperadorparaverificarseocampoéounãonulo. Nuncautilizeo
operador =paraisto,como campo = “” ; campo=“” ; campo =
nullou qualquer outra forma;
• ANY : compara o valor com cada valor resultante de uma subquery.
Deveserprecedidopelosoperandos (,), >=, <=, !=;
• [NOT] EXISTS: retorna um resultado verdadeiro se uma subquery
apresentanomínimoumalinhadentrodascondiçõesdaquery.
Existe uma particularidade sobre o uso doLIKE. Às vezes, temos a ne-
cessidade de pesquisar por caracteres que fazem parte de alguma expressão
ousintaxedentrodalinguagem. Quandoissoacontece,nãoconseguimosre-
alizartalpesquisa,poisnamaioriadasvezeségeradoumerroouoresultado
não é apresentado como queríamos. Para suprir essa necessidade, podemos
definir
ESCAPES para dizer à linguagem que naquele momento estes carac-
teresnãorepresentamfunções,massimplescaracteres. Vejaoexemplo:
SQL> insert into dept values(60,’ABC%’,’BRASIL’);
1 row created.
SQL> select dname from dept where dname like ’%%%’;
DNAME
--------------
ACCOUNTING
RESEARCH
SALES
OPERATIONS
TI
ABC%
6 rows selected.
SQL> select * from dept where dname like ’%/%%’ escape ’/’;
158

## Página 173

CasadoCódigo Capítulo8. Selecionandodados
DEPTNO DNAME LOC
--------- -------------- -------------
60 ABC% BRASIL
SQL>
N e s t ee x e m p l o ,n ac l á u s u l ao n d ea p a r e c eaf u n ç ã oLIKE, podemos ver
trêssímbolosdeporcentagem. SabemosqueemSQLestesímboloéutilizado
como expressão para determinar que o caractere especificado pode estar no
início,fimouemqualquerparteda
string.Oprimeiroeoúltimosímbolo
deporcentagemreferem-seàsexpressõesutilizadascomo LIKE,jáosegundo
caracteredeporcentageménossoparâmetrodepesquisa. Noteque,paraque
alinguagemnãoconfundaestecaracterecomumaexpressão,elaéprecedida
pelocaracteredeescape(
/),queindicaqualtextodesejamospesquisar. Este
símboloédefinidoatravésdacláusula ESCAPEepodeserqualquercaractere
exceto % e _ (porcentagemeunderscore).
Operadordeconcatenação
Além dos operadores exibidos na tabela, também temos mais um que se
encaixa na categoria de operadores de concatenação. Ele é representado por
doispipelines,
||.
OperadordeCotação(q)alternativo
O operador de cotação (q) é utilizado para substituir o delimitador de
aspasutilizadonoscomandosSQL,geralmente,paracomparaçãodestrings.
Sabemosqueparadelimitarumastringutilizamosocaracterdeaspassimples.
Contudo, há casos onde a string utilizada contém uma ou mais aspas na sua
composição. Por exemplo, Car’s Paul, veja que esta string possui uma aspa
simples na sua escrita. Desta forma, se fossemos utilizar esta string em uma
comparaçãoemumcomandoselectousefosseutilizaremumaconcatenação,
faríamosdestaforma: ‘Car’sPaul’. Vejaoexemploabaixosendoexecutado.
O operador de cotação (q) é utilizado para substituir o delimitador de
aspasutilizadonoscomandosSQL,geralmente,paracomparaçãodestrings.
Sabemosqueparadelimitarumastringutilizamosocaracterdeaspassimples.
Contudo, há casos onde a string utilizada contém uma ou mais aspas na sua
composição. Por exemplo, Car’s Paul, veja que esta string possui uma aspa
simples na sua escrita. Desta forma, se fossemos utilizar esta string em uma
159

## Página 174

8.6. Utilizandooperadores CasadoCódigo
comparaçãoemumcomandoselectousefosseutilizaremumaconcatenação,
faríamosdestaforma: ‘Car’sPaul’. Vejaoexemploabaixosendoexecutado.
SQL> select ’Car’s Paul ’ from dual
2/
select ’ Car’s Paul’ from dual
ORA-01756: quoted string not properly terminated
SQL>
Note que ao executar o comando, um erro de sintaxe foi gerado, infor-
mandoqueastringdecotaçãonãofoifinalizadacorretamente. Sabemosque
a primeira e terceira aspas fazem parte da sintaxe para delimitar os caracte-
res. Contudo,aaspadomeio,quefazpartedocontextodastring,oumelhor,
da frase, está gerando o erro. Agora vamos substituir o caracter delimitador,
atravésdocomandodecotaçãoq,queporpadrãoéaspa,porcolchetes.
SQL> select q’[Car’s Paul] ’ from dual
2/
Q’[CAR’SPAUL]’
--------------
Car’s Paul
s
SQL>
Notequeagora,apósdefinirmosoutrodelimitador,ocomandoSQLfun-
cionoucorretamente. Outrosdelimitadorespodemserutilizadosconformea
conveniência. Os mesmos podem ser definidos com um ou vários bytes, ou
qualquerumdosseguintesparesdecaracteres: {},()ou<>.
RegrasdePrecedênciadeOperadores
Dentro da linguagem SQL existe uma prioridade que define qual opera-
dor é executado por primeiro, ou seja, qual a precedência de cada operador
den tr odeumainstruçãoSQL.
1) Operadoresaritiméticos
160

## Página 175

CasadoCódigo Capítulo8. Selecionandodados
2) Operadordeconcatenação
3) Condiçõesdecomparação
4) IS[NOT]NULL,LIKE,[NOT]IN
5) [NOT]BETWEEN
6) Diferentede
7) CondiçãológicaNOT
8) CondiçãológicaAND
9) CondiçãológicaOR
Conforme pode ser visto neste quadro, existe uma precedência de exe-
cução para os operadores no momento que uma instrução SQL é executada.
Portanto, quando um comando SQL é enviado para a execução, o motor do
banco de dados ao avaliar questões, como, por exemplo, sintaxes e existên-
ciadas tabelase colunasenvolvidas, ele tambémverifica estatal precedência
paradeterminarquaispassoseemqueordemestespassosdeverserexecuta-
dos. SabemosqueumcomandoSQLtemcomoobjetivolevaraumresultado,
contudo,temosqueteremmentequeobancodedadosnãoprocessatudode
umasóvez,eleanalisacadapartedainstuçãoevaigerandoosresultadospar-
ciaisatéchegaraumresultadofinal. Destaforma,quandoainstruçãoSQLfor
avaliada,obancodedadostomarácomopontodepartidaestaprecedência.
Você deve estar se perguntando qual a relevância disto na escrita de co-
mandosSQL.Poisbem,selevarmosemcontaquestõesdeperformancepara
comandosSQLcomplexos,teroconhecimentodecomoagemestasregrasde
precedência, pode ajudá-lo a escrever um comando mais performático, di-
gamos assim. Segundo as regras de otimização do banco de dados Oracle,
umainstruçãoSQLpodesermodificadapelopróprioOtimizadordobanco,
visando uma melhor execução. Como? Escrevendo cláusulas comparativas
levando em conta a ordem de precedência. Desta forma, o otimizador do
bancodedadosnãoprecisaráfazerestetrabalhodereordenarestascláusulas.
Contudo,istoserárevelevantequandoestivermosfalandodeajustesfinosde
161

## Página 176

8.6. Utilizandooperadores CasadoCódigo
performance,ouseja,seuSQLnãovaideixardeexecutarporfaltadaaplica-
çãodestasregras.
Noentanto,vocêprecisaconhecerestasregras,paraqueemdeterminados
casos, não acabe comentendo enganos no momento que estiver escrevendo
instruçõesSQL,como,porexemplo,quandoestiverutilizandoosoperadores
OReAND.Vejaoexemploaseguir.
SQL> select last_name, job_id, salary
2 from employees
3 where job_id = ’SA_REP’
4 or job_id = ’AD_PRES’
5 and salary > 15000
6
SQL>
Paraentenderestecomando,vamosavaliá-loutilizandoasregrasdepre-
cedência. Utilizando estas premisas podemos observar que neste comando
temos duas condições. A primeira nos diz que devem ser selecionados em-
pregados que possuem JOB_ID = ‘AD_PRES’ e que SALARY > 15000. A se-
gunda é que o JOB_ID = ‘SA_REP’. Note que estamos seguindo as regras de
precedência,earegraéclara,operadoresANDtemprecedênciasobreopera-
dores OR. Neste caso, serão selecionados os registros que satisfazerem a pri-
meiracondição,empregadoscomcargoigual‘AD_PRES’esaláriomaiorque
15.000,ouasegundacondição,empregadoscomocargoigala‘SA_REP’.Para
melhorentendermos,poderíamosvisualiarascondiçõesdaseguinteforma:
job_id = ’SA_REP’
ou
job_id = ’AD_PRES’ E salary > 15000
Agora,vamosveroresultado:
LAST_NAME JOB_ID SALARY
------------------------- ---------- ----------
King AD_PRES 35138,40
Tucker SA_REP 14641,00
162

## Página 177

CasadoCódigo Capítulo8. Selecionandodados
Bernstein SA_REP 13908,95
Hall SA_REP 13176,90
Olsen SA_REP 11712,80
Cambrault SA_REP 10980,75
Tuvault SA_REP 10248,70
King SA_REP 14641,00
Sully SA_REP 13908,95
McEwen SA_REP 13176,90
Smith SA_REP 11712,80
Doran SA_REP 10980,75
Sewall SA_REP 10248,70
Vishney SA_REP 15373,05
...
Taylor SA_REP 12591,26
Livingston SA_REP 12298,44
Grant SA_REP 10248,70
Johnson SA_REP 9077,42
31 rows selected
SQL>
Note que o resultado satisfez as condições da instrução SQL, trazendo
apenas um registro para a primeira condição e outros trinta referentes a se-
gundacondição.
Agora vamos analisar o comando SQL de outro ângulo. Vamos ima-
ginar que na verdade nossa intenção não seria trazer o resultado da forma
como foi mostrado, idéia seria trazer empregados que tivessem como cargo
’AD_PRES’ ou ‘SA_REP’ e que o salário fosse maior que 15.000. Neste caso,
da forma como foi escrito nosso comando, não vai satisfazer nossa condi-
ção,pois,comovimos,ocomandoSQLfoiavaliadoeexecutadoconformeas
regras de precendência de operadores. Com isto, para fazer com que nossa
condiçãosejasatisfeita,vamossobreporaprecedênciapadrãodalinguagem.
Mesmoexistindoestasregrasdeprecedênciaparaosoperadores,épossí-
vel,sim,sobrepo-lascomaajudadeparênteses. Vamos,novamente,observar
ocomandoSQL,agoraalteradoparasatisfazernossacondição:
SQL> select last_name, job_id, salary
163

## Página 178

8.6. Utilizandooperadores CasadoCódigo
2 from employees
3 where (job_id = ’SA_REP’
4 or job_id = ’AD_PRES’)
5 and salary > 15000
6/
SQL>
Analisando o comando SQL, note que apenas acrescentamos um par de
parênteses isolando duas de nossas comparações. Com isto, formamos duas
novas condições. A primeira condição irá recuperar os empregados onde
JOB_ID=‘SA_REP’ouJOB_ID=‘AD_PRES’.Jáasegundacondiçãoirátrazer
os empregados onde SALARY > 15000. Desta forma, estamos sobrepondo a
precedênciadosoperadores,forçandocomqueaprimeiracondição,mesmo
contendo um operador OR, seja resolvida primeiro, para então, a segunda
condição possa ser resolvida. Desta forma, poderíamos visualizá-las da se-
guinteforma:
(job_id = ’SA_REP’ OU job_id = ’AD_PRES’)
E
salary > 15000
Vamosveroresultadoabaixo:
LAST_NAME JOB_ID SALARY
------------------------- ---------- ----------
King AD_PRES 35138,40
Vishney SA_REP 15373,05
Ozer SA_REP 16837,15
Abel SA_REP 16105,10
SQL>
Comopodeservisto,oresultadoatendeuasexpectativas. Foramlistados
todososempregadosquepossuemocargoiguala‘AD_PRES’ou‘SA_REP’,e
quepossuemsaláriomaiorque15.000.
Anteriormente,vimososoperadoresquepodemserutilizadosdentroda
linguagemSQL.Vejamosalgunsexemplos.
Utilizandoooperadorrelacional MAIOR QUE :
164

## Página 179

CasadoCódigo Capítulo8. Selecionandodados
SQL> select ename, sal
from emp
where sal> 2000;
ENAME SAL
---------- ---------
JONES 2975
BLAKE 2850
CLARK 2450
SCOTT 3000
KING 5000
FORD 3000
6 rows selected.
SQL>
Utilizandoosoperadoresrelacionais MAIOR QUE ede IGUALDADE:
SQL> select ename, sal
from emp
,dept
where sal> 2000
and emp.deptno = dept.deptno
and dept.loc = ’NEW YORK’ ;
ENAME SAL
---------- ---------
CLARK 2450
KING 5000
SQL>
Utilizandoosoperadoresrelacionais DIFERENÇAede IGUALDADE:
SQL> select count (*)
from emp
where deptno = 30;
COUNT(*)
165

## Página 180

8.6. Utilizandooperadores CasadoCódigo
---------
6
SQL>
SQL> select count (distinct(empno))
from emp
where deptno<> 20;
COUNT(DISTINCT(EMPNO))
----------------------
9
SQL>
Utilizando BETWEENpararestringirdatas:
SQL> select count (*)
from emp
where hiredate between ’01-JAN-1980’ and ’01-DEC-1982’;
COUNT(*)
---------
12
SQL>
Ousodooperador INpararestringirpormaisdeumconjuntodestrings:
SQL> select dname
from dept
where loc in (’DALLAS’,’CHICAGO’);
DNAME
--------------
RESEARCH
SALES
SQL>
Nestesexemplos,estásendoutilizadoooperador LIKEparaarealização
derestrições,filtrandoporpartesdecaracteresemumacoluna:
166

## Página 181

CasadoCódigo Capítulo8. Selecionandodados
SQL> select job_id, job_title
from jobs
where lower (job_id) like ’mk%’;
JOB_ID JOB_TITLE
---------- -----------------------------------
MK_MAN Marketing Manager
MK_REP Marketing Representative
SQL>
SQL> select * from dept;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
50 TI BRASIL
SQL> select dname from dept where dname like ’%_S_%’;
DNAME
--------------
RESEARCH
SQL>
SQL> select ename, job, hiredate
from emp
where to_char(hiredate,’dd/mm/yyyy’) like ’03/__/%’;
ENAME JOB HIREDATE
---------- --------- ---------
JAMES CLERK 03- DEC-81
FORD ANALYST 03- DEC-81
SQL>
167

## Página 182

8.6. Utilizandooperadores CasadoCódigo
Agoraousodo EXISTSe NOT EXISTS ,comoformadeapenasverificar
aexistênciaounãodedeterminadosregistrosemoutrastabelas. Istoéusado
paraquandonãonecessitamosretornardadosdestastabelas,apenasverificar
correspondênciasentreelas:
SQL> select dname
from dept d
where exists (select 1
from emp e
where e.deptno = d.deptno
and e.hiredate between ’01-JUL-1980’
and ’31-DEC-1980’);
DNAME
--------------
RESEARCH
SQL>
SQL> select dname
from dept d
where not exists (select 1
from emp e
where e.deptno = d.deptno);
DNAME
--------------
OPERATIONS
SQL>
Porúltimo,nesteexemplo,temosousodosdois pipelinesparaaconcate-
naçãodedados:
SQL> select ename, ’R$ ’||sal from emp where deptno = 10;
ENAME ’R$’||SAL
---------- -------------------------------------------
CLARK R$ 2450
168

## Página 183

CasadoCódigo Capítulo8. Selecionandodados
KING R$ 5000
MILLER R$ 1300
SQL>
169

## Página 185

Capítulo9
Manipulaçãodedados
9.1 Inserçãodedados
INSERT
Estecomandoincluilinhasemumatabelaouvisão. Vejamosoexemplo:
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 2975
7654 MARTIN SALESMAN 7698 28-SEP-81 1250

## Página 186

9.1. Inserçãodedados CasadoCódigo
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
10
14 rows selected.
SQL>
Vamosinserirumregistronatabela EMP:
SQL> insert into emp(empno, ename, job, mgr, hiredate, sal,
comm, deptno) values(8000,’JOHN’,’CLERK’,7902,’30-MAR-2011’
,1000,200,20);
1 row created.
172

## Página 187

CasadoCódigo Capítulo9. Manipulaçãodedados
SQL> commit;
Commit complete.
SQL>
Vejaoresultadoaseguir:
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 2975
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
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
03 0
173

## Página 188

9.1. Inserçãodedados CasadoCódigo
20
30
20
10
200 20
15 rows selected.
SQL>
Agora,inserindoumnovodepartamento:
SQL> select * from dept;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
SQL> insert into dept(deptno
,dname
,loc)
values (5 0
,’TI’
,’BRASIL’)
/
1 row created.
SQL> commit;
Commit complete.
SQL>
Vejaoresultadoaseguir:
SQL> select deptno, dname, loc from dept;
174

## Página 189

CasadoCódigo Capítulo9. Manipulaçãodedados
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
50 TI BRASIL
SQL>
InserindodadosatravésdeSELECTS
Vimos anteriormente que é possível criar uma tabela com base em um
SELECT emoutratabela. Esterecursotambémpodeserutilizadoparaoco-
mando INSERT.Observe:
SQL> select * from clerk;
no rows selected
SQL> insert into clerk select * from emp where job = ’CLERK’;
4 rows created.
SQL> select * from clerk;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7934 MILLER CLERK 7782 23-JAN-82 1300
COMM DEPTNO
--------- ---------
20
20
30
10
175

## Página 190

9.2. Atualizaçãodedados CasadoCódigo
SQL>
Nesteexemplo,estamosalimentandoatabela CLERKcombasenosdados
vindosdatabela EMP.
9.2 Atualizaçãodedados
AtuallizandodadosatravésdeUPDATE
Oc o m a n d oUPDATE muda o valor de um ou mais campos de uma tabela.
Você pode alterar uma ou mais colunas por vez e também delimitar quais
r egistr osquerqueoco mandoafete.
Quando ele é executado, para que a integridade dos dados seja mantida,
o Oracledeixa locadasas linhasque foramafetadas pelocomando de atuali-
zação. Nesse caso, outros usuários não conseguirão atualizá-las, a menos, é
c l a r o ,q u ev o c êe x e c u t eu m
COMMIT ou um ROLLBACK, finalizando a tran-
sação.
Paradelimitarosregistros,usesempreocomandojuntamentecomacláu-
sula WHERE. Caso esta cláusula não esteja informada no comando, todos os
registrosdatabelaserãoafetadosporele.
SQL> select ename, job, hiredate, sal, comm, deptno
from emp
where deptno = 30;
ENAME JOB HIREDATE SAL COMM DEPTNO
---------- --------- --------- --------- --------- ---------
ALLEN SALESMAN 20-FEB-81 1600 300 30
WARD SALESMAN 22-FEB-81 1250 500 30
MARTIN SALESMAN 28-SEP-81 1250 1400 30
BLAKE MANAGER 01-MAY-81 2850 30
TURNER VENDEDOR 08-SEP-81 1500 0 30
JAMES CLERK 03- DEC-81 950 30
6 rows selected.
SQL>
176

## Página 191

CasadoCódigo Capítulo9. Manipulaçãodedados
SQL> update emp
set comm = comm + (sal/100*10)
where hiredate between to_date(’01/02/1981’,’dd/mm/yyyy’)
and to_date(’31/05/1981’,’dd/mm/yyyy’);
4 rows updated.
SQL> select ename, job, hiredate, sal, comm, deptno
from emp
where deptno = 30;
ENAME JOB HIREDATE SAL COMM DEPTNO
---------- --------- --------- --------- --------- ---------
ALLEN SALESMAN 20-FEB-81 1600 460 30
WARD SALESMAN 22-FEB-81 1250 625 30
MARTIN SALESMAN 28-SEP-81 1250 1400 30
BLAKE MANAGER 01-MAY-81 2850 30
TURNER VENDEDOR 08-SEP-81 1500 0 30
JAMES CLERK 03- DEC-81 950 30
6 rows selected.
SQL>
Aqui,estãosendoatualizadasascomissõesdosempregados,combaseem
umadeterminadafaixadedatasdeadmissão.
Note que o funcionárioBLAKE n ã os o f r e ua l t e r a ç ã on os a l á r i o ,e m b o r a
estejadentrodoscritériosdeseleção. IssosedeveaofatodequeoOraclenão
considera o cálculo envolvendo colunas com valores nulos. Para ele, valor
nuloindica
FALSO.Destaforma,qualquercálculoenvolvendovaloresnulos,
éignoradoparaalinguagem. Vamosvermaisàfrentequepodemoscontornar
essasituaçãoutilizandofunçõesespecíficas.
Já no próximo exemplo, atualizações estão sendo feitas na tabela
LOCATIONS. Note que estaremos utilizando uma subconsulta na cláusula
WHEREpararestringirosdadosaserematualizados.
SQL> select street_address, city, state_province, country_name
from locations l
177

## Página 192

9.2. Atualizaçãodedados CasadoCódigo
,countries c
where l.country_id = c.country_id
and country_name in (’Italy’,’Canada’, ’China’);
STREET_ADDRESS CITY STATE_PROVINCE
-------------------------------- --------------- ---------------
147 Spadina Ave Toronto Ontario
6092 Boxwood St Whitehorse Yukon
40-5-12 Laogianggen Beijing
1297 Via Cola di Rie Roma
93091 Calledel la Testa VeniceItaly
COUNTRY_NAME
---------------
Canada
Canada
China
Italy
SQL>
SQL> update locations
set state_province = ’S/P’ -- sem província
where country_id in (select l.country_id
from locations l
,countries c
where l.country_id = c.country_id
and country_name in (’Italy’,
’Canada’,
’China’))
and state_province is null ;
3 rows updated.
SQL> select street_address, city, state_province, country_name
from locations l
,countries c
where l.country_id = c.country_id
and country_name in (’Italy’,’Canada’, ’China’);
178

## Página 193

CasadoCódigo Capítulo9. Manipulaçãodedados
STREET_ADDRESS CITY STATE_PROVINCE
-------------------------------- --------------- ---------------
147 Spadina Ave Toronto Ontario
Whitehorse Yukon
Beijing S/P
Roma S/P
602 Boxwood St
412 Laogianggen            
127 Via Cola di Rie 
9091 Calledel la Testa Venice S/P
COUNTRY_NAME
---------------
Canada
Canada
China
Italy
Italy
SQL>
AtualizandodadosatravésdeSELECTS
Vocêtambémpodeatualizarosdadosatravésde SELECTS.
SQL> select * from clerk;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7934 MILLER CLERK 7782 23-JAN-82 1300
COMM DEPTNO
--------- ---------
20
20
30
10
SQL> update clerk
set comm = ( select comm from emp where empno = 7499);
179

## Página 194

9.3. Exclusãodedados CasadoCódigo
4 rows updated.
SQL> select * from clerk;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7934 MILLER CLERK 7782 23-JAN-82 1300
COMM DEPTNO
--------- ---------
300 20
300 20
300 30
300 10
SQL>
Reparequeacolunadecomissões,atabela CLERK,estásendoatualizada
com base no valor retornado da comissão, referente ao empregado cujo có-
digoé 7499.
9.3 Exclusãodedados
ExcluindodadosatravésdeDELETE
Estecomandoéresponsávelporexcluirlinhasdeumatabela. Assimcomoo
comando
UPDATE, ele mantém locadas as linhas enquanto a transação não
é concluída. Ele também pode ser usado juntamente com a cláusulaWHERE
pararestringirregistros. Ocuidadocomaexclusãoderegistrostambémvale
para este comando, pois, sem isso, você pode excluir todos os dados de uma
tabela.
SQL> select * from emp;
180

## Página 195

CasadoCódigo Capítulo9. Manipulaçãodedados
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 2975
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
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
03 0
20
30
20
10
200 20
15 rows selected.
SQL>
181

## Página 196

9.3. Exclusãodedados CasadoCódigo
SQL> delete from emp where deptno = 20;
6 rows deleted.
SQL>
Excluímos todos os empregados cujo departamento era o20. Veja o re-
sultadoaseguir:
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7900 JAMES CLERK 7698 03- DEC-81 950
7934 MILLER CLERK 7782 23-JAN-82 1300
COMM DEPTNO
--------- ---------
300 30
500 30
1400 30
30
10
10
03 0
30
10
9 rows selected.
SQL>
182

## Página 197

CasadoCódigo Capítulo9. Manipulaçãodedados
Agora vamos excluir dados da tabela de departamento, dos quais não
existe nenhuma referência na tabela de empregados. Note o uso do opera-
dor NOT EXISTS comoauxílionaexclusãodosdados.
SQL> select * from dept;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
50 TI BRASIL
SQL>
SQL> delete from dept d
where not exists (select 1
from emp e
where e.deptno = d.deptno);
2 rows deleted.
SQL>
Vejaoresultadoemseguida:
SQL> select * from dept;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
SQL>
ExcluindodadosatravésdeSELECTS
Podemos também utilizar cláusulasSELECTS para auxiliar na exclusão
dedados:
183

## Página 198

9.3. Exclusãodedados CasadoCódigo
SQL> delete from clerk
where deptno = ( select deptno from clerk where sal> 1200);
1 row deleted.
SQL>
184

## Página 199

Capítulo10
Trabalhandocomfunções
10.1 Funçõesdecaracteres, decálculoseope-
radoresaritméticos
Funçõesdecaracteresedecálculostambémpodemserusadasnasexpressões
SQL. Através delas, podem-se modificar os dados, tanto no que diz respeito
aosvaloresselecionados,comotambémnaformacomosãoapresentados. Por
exemplo, separar informações dentro de uma determinada
STRING,c o n c a -
tenar caracteres, definir a caixa das letras (maiúsculas, minúsculas e interca-
ladas), efetuar arredondamentos em valores, calcular a média, calcular raiz
quadradaetc.
Jáosoperadoresaritméticospodemserutilizadosparaainserçãodecál-
culosdentrodoscomandosSQL.Cálculos,estes,referentesàsoma,subtração,
divisãoemultiplicação.

## Página 200

10.1. Funçõesdecaracteres,decálculoseoperadoresaritméticos CasadoCódigo
Vale salientar que estas funções e operadores podem ser utilizados em
qualquercláusulaSQLexcetonacláusula FROM.
Funçõesdecaracteres
• INITCAP: retornaoprimeirocaracteredecadapalavraemmaiúscula;
• LOWER: forçacaracteresmaiúsculosaparecerememminúsculo;
• UPPER: forçacaracteresminúsculosaparecerememmaiúsculo;
• SUBSTR: extraiumtrechodeumastring,começandoporumaposi-
ção inicial ea partir desta posição conta combase na quantidade soli-
citada;
• TO_CHAR: converteumvalornuméricoparaumastringdecaracte-
res. Também é utilizada para inserir máscara em campos numéricos e
dedata;
• INSTR: retornaaposiçãodoprimeirocaractereencontrado,passado
comoparâmetro;
• LENGTH: trazotamanhodoscaracteresembytes;
• RPAD: faz alinhamento à esquerda e preenche com caracteres à di-
reita, até uma determinada posição. Ambos os valores são passados
comoparâmetro;
• LPAD:fazalinhamentoàdireitaepreenchecomcaracteresàesquerda,
até uma determinada posição. Ambos os valores são passados como
parâmetro.
• CONCAT: Utilizado para concatenar, ou seja, unir valores. Contudo
élimitadoadoisparâmetros.
Seguemexemplosdousodestasfunções.
Primeiro, veja o uso das funções
INITCAP, LOWER e UPPER.N o t eq u e
ovaloresdascolunassãoalteradosconformeaaçãodecadafunção.
186

## Página 201

CasadoCódigo Capítulo10. Trabalhandocomfunções
SQL> select ename from emp where job = ’MANAGER’;
ENAME
----------
JONES
BLAKE
CLARK
SQL>
SQL> select initcap(ename) from emp where job = ’MANAGER’;
INITCAP(EN
----------
Jones
Blake
Clark
SQL>
SQL> select dname, lower(dname) from dept;
DNAME LOWER(DNAME)
-------------- --------------
ACCOUNTING accounting
RESEARCH research
SALES sales
OPERATIONS operations
SQL>
SQL> select upper (’treinamento de sql’ ) from dual;
UPPER(’TREINAMENTO
------------------
TREINAMENTO DE SQL
SQL>
Opróximoexemplomostraousodasfunções SUBSTRe UPPER.Oexem-
ploretornaosnomesdasregiõesmostrandoapenaspartedastringreferente
187

## Página 202

10.1. Funçõesdecaracteres,decálculoseoperadoresaritméticos CasadoCódigo
aestesnomes:
SQL> select * from regions;
REGION_ID REGION_NAME
--------- -------------------------
1 Europe
2 Americas
3 Asia
4 Middle East and Africa
SQL> select region_name, upper(substr(region_name,1,2))
from regions;
REGION_NAME UPPER(SU
------------------------- --------
Europe EU
Americas AM
Asia AS
Middle East and Africa MI
SQL>
Opróximoexemplomostraousodafunção TO_CHAR.Nesteexemplo,a
funçãofoiutilizadaparaformatarosvaloresdacoluna SAL(salários):
SQL> select ename, sal,
’R$ ’||to_char(sal, ’fm999G990D00’) salario
from emp
where comm is null ;
ENAME SAL SALARIO
---------- ---------- --------------
SMITH 800 R$ 800,00
JONES 2975 R$ 2.975,00
BLAKE 2850 R$ 2.850,00
CLARK 2450 R$ 2.450,00
SCOTT 3000 R$ 3.000,00
KING 5000 R$ 5.000,00
ADAMS 1100 R$ 1.100,00
188

## Página 203

CasadoCódigo Capítulo10. Trabalhandocomfunções
JAMES 950 R$ 950,00
FORD 3000 R$ 3.000,00
MILLER 1300 R$ 1.300,00
10 linhas selecionadas.
SQL>
Esteexemplomostraousodafunção INSTR:
SQL> select instr(37462.12,’62’) from dual;
INSTR(37462.12,’62’)
--------------------
4
SQL>
Esteexemplomostraousodafunção LENGTH:
SQL> select first_name
from employees
where length (first_name) > 10;
FIRST_NAME
--------------------
Christopher
Jose Manuel
SQL>
Esteexemplomostraousodasfunções RPADe LPAD:
SQL> select rpad(last_name,12,’++++’)
,lpad(salary,7,’0’)
from employees
where department_id = 30;
RPAD(LAST_NA LPAD(SA
------------ -------
189

## Página 204

10.1. Funçõesdecaracteres,decálculoseoperadoresaritméticos CasadoCódigo
Raphaely++++ 0011000
Khoo++++++++ 0003100
Baida+++++++ 0002900
Tobias++++++ 0002800
Himuro++++++ 0002600
Colmenares++ 0002500
6rowsselected.
SQL>
P o rfim,ousodafunção CONCAT:
SQL> select concat(’Livro ’ ,’SQL’) concatenado from dual
2/
CONCATENADO
-----------
Livro SQL
SQL>
Funçõesdecálculos
• ROUND:arredondavalorescomcasasdecimais;
• TRUNC:truncavalorescomcasasdecimais;
• MOD:mostraor estodadivisãodedo isvalo r es;
• SQRT:retornaaraizquadradadeumvalor;
• POWER:r eto rnaumvalo relevadoao u tr ovalo r;
• ABS:retorna o valor absoluto;
• CEIL:retornaomenorinteiro,maiorouigualavalor;
• FLOOR:r eto rnaomaio rin teir o ,meno ro uigualavalo r;
190

## Página 205

CasadoCódigo Capítulo10. Trabalhandocomfunções
• SIGN:sevalormaiorque0,retorna+1. Sevalormenorque0,retorna
-1. Sevaloriguala0,retorna0.
Osexemplosaseguirmostramousodafunção ROUND.Observeasdife-
rentesformasdechamadaaestafunção.
SQL> select (sal / 2.7), round((sal / 2.7)), ename
from emp
where comm is not null ;
(SAL/2.7) ROUND((SAL/2.7)) ENAME
---------- ---------------- ----------
592,592593 593 ALLEN
462,962963 463 WARD
462,962963 463 MARTIN
555,555556 556 TURNER
SQL> select (sal / 2.7), round((sal / 2.7),2), sal,
ename from emp where empno between 7500 and 7700;
(SAL/2.7) ROUND((SAL/2.7),2) SAL ENAME
---------- ------------------ ---------- ----------
462,962963 462,96 1250 WARD
1101,85185 1101,85 2975 JONES
462,962963 462,96 1250 MARTIN
1055,55556 1055,56 2850 BLAKE
SQL>
Apróximafunçãoexemplificadaéa TRUNC.Noexemplo,sãomostradas
diferentesformasdechamadaaestafunção.
SQL> select (salary / 2.7), trunc((salary / 2.7))
from employees
where email = ’NSARCHAN’
/
(SALARY/2.7) TRUNC((SALARY/2.7))
------------ -------------------
191

## Página 206

10.1. Funçõesdecaracteres,decálculoseoperadoresaritméticos CasadoCódigo
1555,55556 1555
SQL>
SQL> select (salary / 2.7), trunc((salary / 2.7),2)
from employees
where employee_id between 100 and 105;
(SALARY/2.7) TRUNC((SALARY/2.7),2)
------------ ---------------------
8888,88889 8888,88
6296,2963 6296,29
6296,2963 6296,29
3333,33333 3333,33
2222,22222 2222,22
1777,77778 1777,77
6 linhas selecionadas.
SQL>
Estesexemplosmostramousodasfunções MOD, SQRTe POWER:
SQL> select mod (10,2) from dual;
MOD(10,2)
----------
0
SQL>
SQL> select sqrt(64) from dual;
SQRT(64)
----------
8
SQL>
SQL> select power(8,2) from dual;
POWER(8,2)
----------
192

## Página 207

CasadoCódigo Capítulo10. Trabalhandocomfunções
64
SQL>
Aseguirémostradoousodasfunções ABS, CEILe FLOOR.
SQL> select abs (-20) from dual;
ABS(-20)
----------
20
SQL>
SQL> select ceil(10.2) from dual;
CEIL(10.2)
----------
11
SQL>
SQL> select floor(10.2) from dual;
FLOOR(10.2)
-----------
10
SQL>
Porúltimo,vejamosousodafunção SIGN.Nosexemplos,sãomostrados
diferentesparâmetrosnachamadadestafunção.
SQL> select sign(-200) from dual;
SIGN(-200)
-----------
-1
SQL> select sign(200) from dual;
193

## Página 208

10.1. Funçõesdecaracteres,decálculoseoperadoresaritméticos CasadoCódigo
SIGN(200)
----------
1
SQL> select sign(0) from dual;
SIGN(0)
----------
0
SQL>
Operadoresaritméticos
Aseguir,vejaosoperadoresemsuasequênciadeprioridade.
• *: multiplicação
• /:d i v i s ã o
• +: adição
• -:s u b t r a ç ã o
Este exemplo mostra o uso das funções aritméticas de multiplicação e
divisão:
SQL> select sal, (sal*2/3) from emp
where comm is not null ;
SAL (SAL*2/3)
--------- ---------
1600 1066.6667
1250 833.33333
1250 833.33333
1500 1000
1000 666.66667
SQL>
194

## Página 209

CasadoCódigo Capítulo10. Trabalhandocomfunções
Este exemplo mostra o uso das funções aritméticas de multiplicação, di-
visãoeso ma:
SQL> select ename, sal, round((sal*2)/3+100.00,2)
from emp
where deptno = 30;
ENAME SAL ROUND((SAL*2)/3+100.00,2)
---------- --------- -------------------------
ALLEN 1600 1166.67
WARD 1250 933.33
MARTIN 1250 933.33
BLAKE 2850 2000
TURNER 1500 1100
JAMES 950 733.33
6 rows selected.
SQL>
Este exemplo mostra o uso das funções aritméticas de multiplicação, di-
visãoesub tração:
SQL> select ename
,dname
,trunc((sysdate - hiredate) / 365) anos
,hiredate
,(sal/10*trunc((sysdate - hiredate) / 365)) premiacao
,sal
from emp e
,dept d
where e.deptno = d.deptno
and trunc((sysdate - hiredate) / 365) = 30;
ENAME DNAME ANOS HIREDATEPREMIACAO
---------- -------------- ---------- -------- ----------
MILLER ACCOUNTING 30 23/01/82 3900
KING ACCOUNTING 30 17/11/81 15000
FORD RESEARCH 30 03/12/81 9000
195

## Página 210

10.2. Funçõesdeagregação(grupo) CasadoCódigo
JAMES SALES 30 03/12/81 2850
TURNER SALES 30 08/09/81 4500
MARTIN SALES 30 28/09/81 3750
SAL
----------
1300
5000
3000
950
1500
1250
6 linhas selecionadas.
SQL>
10.2 Funçõesdeagregação(grupo)
As funções de agregação são responsáveis por agrupar vários valores e re-
tornar somente um único valor para um determinado grupo. As funções de
agregação, também chamadas de funções de grupo, são especificadas no co-
mando
SELECT e são seguidas pela coluna à qual se aplicam. A utilização
das funções de agregação pode implicar no uso da cláusulaGROUP BY .I s so
acontece porque, ao informarmos colunas com funções e colunas sem fun-
ções em um
SELECT, precisamos agrupar as colunas que não estão sendo
afetadaspeloagrupamentocausadopelasfunções. Vejaailustração:
196

## Página 211

CasadoCódigo Capítulo10. Trabalhandocomfunções
Fig.10.1
Reparenaimagemquetemosalgunsempregados,departamentosevalo-
res de salário. Nosso objetivo aqui é tentar de alguma forma somar todos os
salários por departamento, ou seja, ver quanto de salário temos para os em-
pregadosreferentesaosdepartamentos
RESEARCH, SALESE ACCOUNTING.
Da forma como os dados estão dispostos, não conseguimos visualizar isso,
pois, se tentarmos agrupar por departamento, não conseguiremos, já que o
agrupamento consiste em selecionar dados que possuem o mesmo valor e
torná-loúnicoparacadaconjuntodedados.
Por exemplo, temos os departamentos
RESEARCH, SALES e
ACCOUNTING aparecendo diversas vezes. Se agruparmos, teremos um
único registro para o departamento RESEARCH,o u t r op a r aSALES,e
outro para ACCOUNTING. Entretanto, também estamos selecionando os
nomes dos empregados e, na maioria dos casos, cada um possui um nome
deferente, impossibilitando que os agrupemos. Se não conseguimos agrupar
os empregados, não conseguimos agrupar os departamentos. É como se
fosseumasequência.
Quandousamosfunçõesdegruponascolunasdeum
SELECT,temosque
agrupar todas as outras colunas, sendo através de uma função de agregação
ousendopelousodo
GROUP BY .Jávimosquesenósquisermosasomatória
de todos os salários por departamento não podemos estar selecionando os
197

## Página 212

10.2. Funçõesdeagregação(grupo) CasadoCódigo
empregados,oumelhor,seusnomes. Logo,acoluna Empregadonãopoderá
aparecer no nossoSELECT.C a s oc o n t r á r i o ,e s t a r í a m o sa g r u p a n d ot a m b é m
porempregados,oquenosdariaumagrupamentoinútil,tendoemvistaque
cadanomedeempregadoédiferente.
Semprequandotrabalhamoscomagrupamentostemosqueteremmente
a seguinte situação: vai haver colunas que estarão sob o efeito das funções
de agregação, como funções de somatória ou de média, e colunas que não
estarão sobre o efeito destas funções, mas que precisarão ser agrupadas para
que,juntas,possamformarumconjuntodedados.
Vejaapróximailustração:
Fig.10.2
Nesta outra ilustração temos dois grupos. Um, formado pelas colunas
Empregado e Departamento,quesofrerãoaaçãodo GROUP BY ,eo u tr o ,
formado apenas pela colunaSalário, que sofrerá a ação da nossa função
deagregação. Valeressaltarquenossoobjetivoaquiéagruparossaláriospor
departamento. Pois bem, como pode ser visto na ilustração, neste caso, não
conseguimosmontaroagrupamento. Notequenacolunadedepartamentoé
possívelagruparosvalores,masnacolunadeempregadosissonãoépossível.
198

## Página 213

CasadoCódigo Capítulo10. Trabalhandocomfunções
Como a coluna de empregados faz parte doSELECT, ela acaba comprome-
t e n d ot o d on o s s oa g r u p a m e n t o .A t e n ç ã oau md e t a l h e–of a t od eac o l u n a
Empregadoestarsendovisualizadaprimeironãoquerdizerquesejaacausa
de não conseguirmos agrupar por departamento. A ordem das colunas não
alteraoresultado. Vamosretirá-ladonosso SELECT.
Fig.10.3
Agora sim. Tiramos a coluna de empregados e ficamos apenas com as
colunas Departamentoe Salários.
Vejacomoficounossoagrupamento:
199

## Página 214

10.2. Funçõesdeagregação(grupo) CasadoCódigo
Fig.10.4
Fazendodessaformaconseguimosalcançarnossoobjetivo.
Resumindo
• Devemos saber que, para obter sucesso em nossos agrupamentos, as
colunasquenãoestãosendoagrupadaspelasfunçõesdeagrupamento
devemseragrupadaspelo GROUP BY ;
• Tambémpodemosagrupardeterminadascolunas,mesmoqueelasnão
estejampresentesnacláusula SELECT;
• Somente vamos precisar agrupar colunas através do GROUP BY
quando desejarmos mostrar um resultado com base em outro. Por
200

## Página 215

CasadoCódigo Capítulo10. Trabalhandocomfunções
exemplo, valores de salário por departamento, quantidades de empre-
gados por departamento e assim por diante. Se quisermos apenas sa-
berasomatóriadetodososvaloresdesalário,independentedodepar-
tamento ou de qualquer outra informação, não precisamos utilizar o
GROUPY BY ;
• Funçõesdeagregação,nogeral,ignoramvaloresnulos;
• Pararealizaroagrupamentodeinformações,oOraclepoderáordenar
o un ã oa sc o l u n a s .C a s oac o l u n aq u ee s t ás o baa ç ã od af u n ç ã of o r
umacolunacomíndice,obancopoderáutilizá-lo. Comoosíndicessão
ordenados,nãoseránecessárioordenarosdadosparaoagrupamento.
Casocontrário,elevairealizaraordenaçãoprimeiro,edepois,agrupar.
Nemtodasasfunçõespermitemusaríndices.
Agoravamosveressesconceitosnaprática.
Primeiramente,visualizamosonomedetodososempregados,osnomes
dosseusdepartamentoseseusrespectivossalários.
SQL> select ename, dname, sal
from emp e, dept d
where e.deptno = d.deptno
order by ename;
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
201

## Página 216

10.2. Funçõesdeagregação(grupo) CasadoCódigo
SMITH RESEARCH 800
TURNER SALES 1500
WARD SALES 1250
15 rows selected.
SQL>
AtravésdeumcomandoSQLselecionamososmesmosdadosdo SELECT
anterior, mas agora sumarizando os salários. Note que continuamos selecio-
nandoascolunasdonomedoempregadoedodepartamentodoempregado.
Oob jetivodop r ogramaémostraraso madossaláriospo rdepartamen to .
SQL> select ename, dname, sum(sal)
from emp e, dept d
where e.deptno = d.deptno
order by ename;
select ename, dname, sum(sal)
*
ERROR at line 1:
ORA-00937: not a single- group group function
SQL>
Ao executar o programa, surgiu um erro que, em linhas gerais, quer nos
dizer que o comandoSELECT está tentando utilizar uma função de grupo,
juntamente com outras colunas não agrupadas, sem a cláusula de agrupa-
mento. Comovistonosconceitosapresentadosanteriormente,issonãoéper-
mitido. Devemos agrupar as colunas que não estão associadas a funções de
agrupamento. Vejaaseguircomoficou.
SQL> select ename, dname, sum(sal)
from emp e, dept d
where e.deptno = d.deptno
group by ename, dname
order by ename;
ENAME DNAME SUM(SAL)
---------- -------------- ---------
202

## Página 217

CasadoCódigo Capítulo10. Trabalhandocomfunções
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
Feitos os agrupamentos necessários, voltamos a executar oSELECT.O
resultadofoiapresentadologoemseguida. Noentanto,vejaquealgonãosaiu
como deveria. Os salários não foram sumarizados por departamento e, sim,
porempregado. Destaforma,seriaamesmacoisaquenãosumarizar. Vamos
alterarocomandoretirandoacolunanomedoempregadodocomandoSQL.
SQL> select dname, sum(sal)
from emp e, dept d
where e.deptno = d.deptno
group by ename, dname
order by ename;
DNAME SUM(SAL)
-------------- ---------
RESEARCH 1100
SALES 1600
SALES 2850
ACCOUNTING 2450
RESEARCH 3000
SALES 950
RESEARCH 1000
203

## Página 218

10.2. Funçõesdeagregação(grupo) CasadoCódigo
RESEARCH 2975
ACCOUNTING 5000
SALES 1250
ACCOUNTING 1300
RESEARCH 3000
RESEARCH 800
SALES 1500
SALES 1250
15 rows selected.
SQL>
Aoretiraracoluna,oerropersiste. Issoacontecepoisnãoadiantaretirar
apenasdaseleção,mastambéménecessárioretirardoagrupamento. Repare
quenalinha4aindaconstaacoluna ENAME.Vejaaseguircomodeveficaro
SELECT,paraqueseconsigaatingiroobjetivoproposto.
SQL> select dname, sum(sal)
from emp e, dept d
where e.deptno = d.deptno
group by dname;
DNAME SUM(SAL)
-------------- ---------
ACCOUNTING 8750
RESEARCH 11875
SALES 9400
SQL>
Selecionando apenas a coluna referente ao nome do departamento e su-
marizando os salários, através da função de agregaçãoSUM, temos como re-
sultadoasomadossaláriospordepartamento.
Seguemasfunçõesdeagregaçãomaisutilizadas:
• COUNT: retornaaquantidadedeincidênciasderegistros;
• SUM: exibeasomadosvaloresdosregistros;
204

## Página 219

CasadoCódigo Capítulo10. Trabalhandocomfunções
• AVG: exibeamédiadosvaloresdeumadeterminadacoluna;
• MIN: exibeomenorvalordeumacoluna;
• MAX: r eto rnaomaio rvalo rdeumacol una.
Oprimeiroexemplomostraousodafunção COUNT.Oobjetivoéseleci-
onaraquantidadedeempregadosporpaís.
SQL> select count (employee_id) cont_emp, country_name
from employees e
,departments d
,locations l
,countries c
where e.department_id = d.department_id
and d.location_id = l.location_id
and l.country_id = c.country_id
group by country_name
order by country_name;
CONT_EMP COUNTRY_NAME
--------- ----------------------------------------
2 Canada
1 Germany
35 United Kingdom
68 United States of America
SQL>
O próximo exemplo é quase igual ao anterior, apenas por um detalhe.
Noteque,comoconhecemosatabela EMPLOYEESesabemosqueexisteape-
nas um registro para cada empregado, podemos usar a funçãoCOUNT de
outraforma,utilizandoasterisco( * )nol ugardacol una EMPLOYEE_ID.
SQL> select count (*) cont_emp, country_name
from employees e
,departments d
,locations l
,countries c
205

## Página 220

10.2. Funçõesdeagregação(grupo) CasadoCódigo
where e.department_id = d.department_id
and d.location_id = l.location_id
and l.country_id = c.country_id
group by country_name
order by country_name;
CONT_EMP COUNTRY_NAME
--------- ----------------------------------------
2 Canada
1 Germany
35 United Kingdom
68 United States of America
SQL>
Opróximoexemplomostraousodafunção MAX.Oobjetivoéselecionar
amaiordatadeAdmissãodecadadepartamento.
SQL> select dname, max(hiredate)
from emp e, dept d
where e.deptno = d.deptno
group by dname
order by 2 desc;
DNAME MAX(HIRED
-------------- ---------
RESEARCH 30-MAR-11
ACCOUNTING 23-JAN-82
SALES 03- DEC-81
SQL>
Esteexemplomostraousodafunção MIN.Oobjetivoéselecionarame-
nordatadeadmissãoentretodososempregados:
SQL> select min (hire_date) from employees;
MIN(HIRE_
---------
206

## Página 221

CasadoCódigo Capítulo10. Trabalhandocomfunções
17-JUN-87
SQL>
Além das funções de agregação e do uso doGROUP BY , também pode-
m o sc o n t a rc o moHAVING para nos ajudar a restringir registros com base
nosvaloresretornadospelasfunçõesdeagregação.O HAVINGexistepoisnão
podemosutilizarfunçõesdeagregaçãonacláusula WHERE.
Noexemploaseguir,émostradoousodacláusula HAVING.Oobjetivoé
selecionaraquantidadedeempregadoseasomadossalários,agrupadospor
departamentoscujaquantidadedeempregadosémaiorque5. Observequea
cláusula
HAVINGatuasomenteapósoagrupamentodaslinhas. Porisso,não
seriapossívelutilizaracláusula WHERE,jáqueelaatuanomomentoemque
aslinhasestãosendoselecionadas,ouseja,antesdoagrupamento.
SQL> select count (employee_id) cont_emp,
sum(salary) soma_salario, department_name
from employees e
,departments d
where e.department_id = d.department_id
having count (employee_id) > 5
group by department_name
order by department_name;
CONT_EMP SOMA_SALARIO DEPARTMENT_NAME
--------- ------------ ------------------------------
6 51600 Finance
6 24900 Purchasing
34 304500 Sales
45 156400 Shipping
SQL>
Jánesteoutroexemplo,oobjetivoéselecionarasomadossalários,agru-
pados por departamento e país, sendo que a soma é maior que a média dos
saláriosporpaís.
SQL> select department_name, sum(salary), country_name
from employees e
,departments d
207

## Página 222

10.2. Funçõesdeagregação(grupo) CasadoCódigo
,locations l
,countries c
where e.department_id = d.department_id
and d.location_id = l.location_id
and l.country_id = c.country_id
having sum (salary) > ( select avg (em.salary)
from employees em
,departments dm
,locations lm
,countries cm
where em.department_id =
dm.department_id
and dm.location_id =
lm.location_id
and lm.country_id = cm.country_id
and cm.country_id = c.country_id)
group by c .country_id
,department_name
,country_name
order by country_name
,department_name;
DEPARTMENT_NAME SUM(SALARY) COUNTRY_NAME
--------------------------- ----------- ------------------------
Marketing 19000 Canada
Sales 304500 United Kingdom
Accounting 20300 United States of America
Executive 58000 United States of America
Finance 51600 United States of America
IT 28800 United States of America
Purchasing 24900 United States of America
Shipping 156400 United States of America
8 rows selected.
SQL>
208

## Página 223

CasadoCódigo Capítulo10. Trabalhandocomfunções
10.3 Funçõesdedata
Funções de data são utilizadas para manipular valores do tipodate,c o m o
aplicarformataçõesparaumavisualizaçãomaisrefinada,ouextrairpartesde
uma data, as horas, dia do mês ou somente o ano. Seguem algumas destas
funções:
• ADD_MONTHS: adicionamesesemumadeterminadadata;
• MONTHS_BETWEEN: retorna a quantidade de meses entre duas
datas;
• NEXT_DAY:procuraopróximodiaapósumadatainformada;
• LAST_DAY: retorna o último dia do mês com base em uma data in-
formada;
• TRUNC: truncaumadatapassadaporparâmetro. Podeserfeitopor
diaemês,utilizandooparâmetro
FMT(formato);
• SYSDATE:retornaadatacorrentecombasenoservidordobancode
dados;
• SESSIONTIMEZONE: mostra o fuso horário com base na sessão
abertanobancodedados,mediantesualocalização. Valelembrarque
osfusoshoráriossãocalculadoscombasenomeridianodeGreenwich.
• CURRENT_DATE: mostra a data corrente com base na zona de
tempo da sessão do usuário. A Zona de tempo é afetada em relação
ao Meridiano. Caso não haja mudanças de zona, esta função terá o
mesmovalorque
SYSDATE,quebuscaahoradoservidordobancode
dados, mesmo que a sessão tenha sido aberta em uma zona diferente
daquela em que o servidor se encontra. Já o
CURRENT_DATE refletirá
azo nao ndefo iabertaasessão .
209

## Página 224

10.3. Funçõesdedata CasadoCódigo
Quando for calcular a quantidade de anos entre duas datas, utilize a
função MONTHS_BETWEEN, dividindo o retorno da função (quantidade
demesesentreasdatas)por12(quantidadedemesesemumano). Desta
forma, você chegará a um valor mais preciso do que subtraindo duas
datas e dividindo (retorno em dias) por 365 dias. O resultado final, em
ambasasformas,podesertruncado.
Seguem alguns exemplos. No primeiro, é mostrado o uso da função
NEXT_DAY. O exemplo seleciona os empregados que têm como mês de ani-
versário o mês corrente. Através dessa função, é calculado qual o primeiro
domingologoemseguidaaodiadeaniversáriodecadaempregado.
SQL> select first_name
,to_date(to_char(birth_date,’dd/mm’)||’/’||
to_char(sysdate,’rrrr’)
,’dd/mm/rrrr’) dt_aniversario
,next_day(to_date(to_char(birth_date,’dd/mm’)||’/’||
to_char(sysdate,’rrrr’),’dd/mm/rrrr’)
,’SUNDAY’) DOMINGO
from employees
where to_char(birth_date,’mm’) = to_char(sysdate, ’mm’)
order by 2;
FIRST_NAME DT_ANIVER DOMINGO
-------------------- --------- ---------
Joshua 06-APR-11 10-APR-11
Adam 10-APR-11 17-APR-11
TJ 10-APR-11 17-APR-11
Amit 21-APR-11 24-APR-11
Sundita 21-APR-11 24-APR-11
Jack 23-APR-11 24-APR-11
Alana 24-APR-11 01-MAY-11
7 rows selected.
SQL>
A seguir, é mostrado o uso das funções ADD_MONTHS e
MONTHS_BETWEEN. Selecionamos os empregados e suas respectivas da-
210

## Página 225

CasadoCódigo Capítulo10. Trabalhandocomfunções
tas de término de experiência do cargo. Note que limitamos o número de
empregados no SELECT através da função ADD_MONTHS,p a r ae v i t a ro
retornodetodasaslinhasdatabela.
SQL> select ename, dname
,hiredate
,add_months(hiredate,3) dt_termino_exp
,to_char(months_between(sysdate,hiredate),’90D00’)
qt_meses_trabalho
from emp e, dept d
where e.deptno = d.deptno
and add_months(hiredate,3) >= sysdate;
ENAME DNAME HIREDATE DT_TERMIN QT_MES
---------- -------------- --------- --------- ------
JOHN RESEARCH 30-MAR-11 30-JUN-11 0.14
SQL>
Noexemploseguinte,émostradoousodasfunções SESSIONTIMEZONE,
CURRENT_DATE e SYSDATE. São exibidos o fuso horário, a data corrente
localedataatualdoservidor.
SQL> select sessiontimezone
,current_date
,sysdate
from dual;
SESSIONTIMEZONE CURRENT_D SYSDATE
-------------------------------------------- --------- ---------
-03:00 03-APR-11 03-APR-11
SQL>
O próximo exemplo mostra o uso das funçõesLAST_DAY, ROUND e
TRUNC.Sãoapresentadasváriasformasdeusarasfunçõesparaextrairouma-
nipulardeterminadasinformações,como,porexemplo,arredondaretruncar
datas.
SQL> select ename
,hiredate
211

## Página 226

10.4. Funçõesdeconversão CasadoCódigo
,last_day(hiredate) last
,round(hiredate, ’YEAR’) round
,trunc(hiredate, ’YEAR’) trunc
from emp;
ENAME HIREDATE LAST ROUND TRUNC
---------- --------- --------- --------- ---------
SMITH 17- DEC-80 31- DEC-80 01-JAN-81 01-JAN-80
ALLEN 20-FEB-81 28-FEB-81 01-JAN-81 01-JAN-81
WARD 22-FEB-81 28-FEB-81 01-JAN-81 01-JAN-81
JONES 02-APR-81 30-APR-81 01-JAN-81 01-JAN-81
MARTIN 28-SEP-81 30-SEP-81 01-JAN-82 01-JAN-81
BLAKE 01-MAY-81 31-MAY-81 01-JAN-81 01-JAN-81
CLARK 09-JUN-81 30-JUN-81 01-JAN-81 01-JAN-81
SCOTT 09- DEC-82 31- DEC-82 01-JAN-83 01-JAN-82
KING 17-NOV-81 30-NOV-81 01-JAN-82 01-JAN-81
TURNER 08-SEP-81 30-SEP-81 01-JAN-82 01-JAN-81
ADAMS 12-JAN-83 31-JAN-83 01-JAN-83 01-JAN-83
JAMES 03- DEC-81 31- DEC-81 01-JAN-82 01-JAN-81
FORD 03- DEC-81 31- DEC-81 01-JAN-82 01-JAN-81
MILLER 23-JAN-82 31-JAN-82 01-JAN-82 01-JAN-82
JOHN 30-MAR-11 31-MAR-11 01-JAN-11 01-JAN-11
15 rows selected.
SQL>
10.4 Funçõesdeconversão
Em muitos casos, precisamos converter um determinado dado de um tipo
para outro. O Oracle disponibiliza funções de conversão para este trabalho.
Estasfunções,emborasejamsimplesdeseremusadas,ajudammuitonomo-
mentodeconverterouformatardadosprovenientesdosseuscomandosSQL.
• TO_DATE: converteumastring(
char ou varchar2)deca ract er e
paraumadata;
• TO_NUMBER: converteumastring( charou varchar2)decarac-
tereparaumnúmero;
212

## Página 227

CasadoCódigo Capítulo10. Trabalhandocomfunções
• TO_CHAR: converte um número ou uma data para uma string de
caractere.
Cadafunçãopossuisuascaracterísticasesãoutilizadasparacumprirum
o b j e t i v od i f e r e n t e .Oq u ee l a sp o s s u e me mc o m u méon ú m e r od ep a r â m e -
tros. O primeiro parâmetro está relacionado ao valor que deve ser conver-
tido;osegundocorrespondeaoformatoquevocêdesejaaplicar;eporúltimo
e opcional, o parâmetro de linguagem. Trata-se de funções muito utilizadas
nodiaadia,eédefundamentalimportância,conhecê-laseentendercomose
comportam. Alémdasmencionadas,aOracledisponibilizaváriasoutraspara
as mais diversas situações. Contudo, essas três são as que mais comumente
utilizamos nas construções de nossos comandos SQL. Para saber mais sobre
outras funções de conversão, consulte em livros de Oracle que falam sobre a
SQLounadocumentaçãodisponívelnositedaOracle.
TO_DATE
Esta função é bem interessante. Com um pouco de treino e criatividade,
podemosrealizarváriasconversõesquepodemajudarmuitonomomentode
formatar,selecionaroucriticarosdadosretornadosdeumcomandoSQL.
Ela funciona basicamente da seguinte forma: você vai passar um valor
caractere para a função, juntamente com um formato. Este formato deve ser
compatível com o conjunto de caracteres que você passou para a função. A
qualquerincompatibilidade,oOraclegeraumerrodeconversão.
Exemplo:
TO_DATE(‘21/05/2009’,’dd/mm’). Esta conversão vai
gerarumerro,poisvocêestáinformandodia,mêseano,comocaractere,mas
namáscarasómencionoudiaemês. QuandooOraclevaifazeraconversão,
eleanalisaoformatoquevocêestápassandocomoparâmetroeverificaoque
éelementodefunçãoeoqueécaractere. Nestecaso,elesabeque
dde mmsão
elementos conhecidos de dia e mês, e que/ é um caractere que serve como
uma espécie de separador. Então, depois desta identificação, ele pega cada
caractereinformadoevaiconvertendoconformeoformato
2=d, 1=d, /=/,
0=m, 5=m etc. Mas quando ele chega na segunda/,v êq u en ã oh áf o r m a t o
para o caractere, pois terminou no elementom. Logo, é gerado um erro de
conversão.
213

## Página 228

10.4. Funçõesdeconversão CasadoCódigo
V ejaaexecução:
SQL> select TO_DATE(’21/05/2009’,’dd/mm’) from dual;
select TO_DATE(’21/05/2009’,’dd/mm’) from dual
*
ERROR at line 1:
ORA-01830: date format picture ends before converting entire
input string
SQL>
Ocontráriotambémgeraoutroerro:
SQL> select TO_DATE(’21/05’,’dd/mm/yyyy’) from dual;
select TO_DATE(’21/05’,’dd/mm/yyyy’) from dual
*
ERROR at line 1:
ORA-01840: input value not long enough for date format
SQL>
Seguem exemplos do uso doTO_DATE.Op ri m e i r om o s tr ac o m oépo s -
sível converter strings em datas válidas. Veja que, na linha 4 do programa,
temos a função convertendo a string010182 para uma data utilizando o
formatoDDMMRR.
SQL> select ename
,hiredate
from emp
where hiredate > to_date( ’010182’,’ddmmrr’);
ENAME HIREDATE
---------- ---------
SCOTT 09- DEC-82
ADAMS 12-JAN-83
MILLER 23-JAN-82
JOHN 30-MAR-11
SQL>
214

## Página 229

CasadoCódigo Capítulo10. Trabalhandocomfunções
Já neste outro exemplo, também utilizandoTO_DATE e SELECT, temos
afunçãoconvertendooutrastringemumadata,utilizandoumformatodife-
rente.
SQL> select to_date(’21.05.2009’,’dd.mm.yyyy’) from dual;
TO_DATE(’
---------
21-MAY-09
SQL>
Podemos também adicionar à chamada da função aspectos referentes à
linguagem. Nesteexemplo,estamosconvertendoumastringporextensoem
data,utilizandooformatoamericano:
SQL> select to_date(’April 21’ ,’month dd’ ,
’nls_date_language=american’) from dual;
TO_DATE(’
---------
21-APR-11
SQL>
Contudo, como pode ser visto no exemplo anterior, a visualização con-
tinua sendo no formato americano, embora estejamos convertendo a string
paradatautilizandooformatobrasileiro. Lembre-se,conversãonãonecessa-
riamentetemavercomaformacomqueodadoseráimpressonatela.
SQL> select to_date(’Abril 21’ ,’month dd’ ,
’nls_date_language=’’BRAZILIAN PORTUGUESE’’’ ) from dual;
TO_DATE(’
---------
21-APR-11
SQL>
215

## Página 230

10.4. Funçõesdeconversão CasadoCódigo
Esteexemplomostraquedevemosinformarformatosválidos,oumelhor,
formatos conhecidos da linguagem. Caso contrário, a conversão não é reali-
zadaeerrosocorrerão:
SQL> select to_date(’Abril 21’ ,’month XX’ ,
’nls_date_language=’’BRAZILIAN PORTUGUESE’’’ ) from dual;
select to_date(’Abril 21’ ,’month XX’ ,
’nls_date_language=’’BRAZILIAN PORTUGUESE’’’ ) from dual
*
ERROR at line 1:
ORA-01821: date format not recognized
SQL>
Aseguir,algumaslimitaçõescomrelaçãoàfunção TO_DATE:
•As t r i n gas e rp a s s a d ap a r aac o n v e r s ã on ã op o d ec o n t e rm a i sd e2 2 0
caracteres;
• Existem vários formatos de máscara disponíveis para a utilização.
QualquermáscaradiferentedaspermitidaspelaOraclegeraráumerro
deconversão;
• Nãopodehaverconfrontodemáscaras. Porexemplo,vocêqueriautili-
zaramáscara
HH24etambémsolicitarquefossemostrado AM(indica-
dordeantemeridianoparamanhã)ou PM(indicadordepós-meridiano
paranoite);
• Nãoépermitidoespecificarelementosdeconversãoduplicados. Exem-
plo: DD-MM-MM.Nestecaso,oformatoparamêsapareceduasvezes.
Vejaalgunselementosdeformataçãoquepodemserusados:
• CC: adiciona1aosdoisprimeirosdígitosdoano(YYYY);
• SCC: igualCC,prefixandodatasBCcomumsinalnegativo;
• YY: r ep r esen taoanoco md uascasas;
216

## Página 231

CasadoCódigo Capítulo10. Trabalhandocomfunções
• YYYY: r ep r esen taoanoco mqua tr ocasas;
• RR: representa os dois últimos dígitos do ano, mas obedecendo a se-
guinte regra: soma 1 aos dois primeiros dígitos de CC se ano for < 50
eosúltimos2dígitosdoanocorrenteforem>=50. Subtrai1deCCse
ano>=50eosúl timosdo isdígi tosdoanoco rr en tefo r em<50;
• RRRR: representaoano. Aceita2ou4dígitos. Seanoinformadocom
2dígitos,segueasmesmasregrasde
RR;
• YEAR: escreveoanoporextenso;
• MM: númerodomêsde01a12. 01=Janeiro,02=Fevereiroetc.;
• MONTH: nomedomês;
• MON: representaonomedomêsabreviadocomtrêscaracteres;
• DD: diadomêsde1a31;
• DDD: r ep r esen taodiadoanode1a366;
• DAY:representaonomedodiaporextenso;
• HH,HH12,HH24:HH e HH12, horas de 1 a 12. HH24, horas de 0 a
23;
• MI: equivaleaosmin u tosde0a59;
• SS: equivaleaossegundosde0a59;
• SP: converte o número para seu formato escrito. Disponível apenas
paraaescritanoidiomainglês;
• SPTH: mostra os números de maneira ordinal. 1 = First, 2 = Second
etc.;
• FM: retira espaços em branco proveniente da ausência de caracteres
emumformato.
217

## Página 232

10.4. Funçõesdeconversão CasadoCódigo
Esses elementos também são utilizados na conversão do tipoDATE
parastring.
A função TO_DATE pode converter não só strings representando datas
completas, como também strings representando partes de uma data. Este
exemplo mostra a função realizando a conversão da string2008 em data.
Noteque,aoserconvertida,recebeuadataatual,modificadaapenaspeloano
convertido:
SQL> select to_date(’2008’,’yyyy’) from dual;
TO_DATE(’
---------
01-APR-08
SQL>
Esteexemploésimilaraoanterior. Neste,estásendorealizadaaconversão
combasenarepresentaçãonuméricadodiareferenteaototaldediasdoano:
SQL> select to_date(200,’ddd’) from dual;
TO_DATE(2
---------
19-JUL-11
SQL>
UsodeYYYYeRRRR
Sabemosqueamáscara YYYYrepresentaosquatrodígitosdoano. Opci-
onalmente, pode-se utilizarYY para mostrar apenas os dois últimos dígitos.
Contudo,paracorrigirproblemasdecompatibilidadecomaviradadoséculo,
aOraclecriouasmáscaras RRe RRRR.Vejaaaplicaçãoaseguir:
SQL> select to_char(sysdate,’dd/mm/yyyy’) from dual;
218

## Página 233

CasadoCódigo Capítulo10. Trabalhandocomfunções
TO_CHAR(SY
----------
14/04/2011
SQL> select to_char(to_date(’01/01/49’,’dd/mm/yy’),’dd/mm/yyyy’)
from dual;
TO_CHAR(TO
----------
01/01/2049
SQL> select to_char(to_date(’01/01/50’,’dd/mm/yy’),’dd/mm/yyyy’)
from dual;
TO_CHAR(TO
----------
01/01/2050
SQL> select to_char(to_date(’01/01/49’,’dd/mm/rr’),’dd/mm/rrrr’)
from dual;
TO_CHAR(TO
----------
01/01/2049
SQL> select to_char(to_date(’01/01/50’,’dd/mm/rr’),’dd/mm/rrrr’)
from dual;
TO_CHAR(TO
----------
01/01/1950
SQL>
Nesse exemplo, vemos formatações de datas utilizando a função
TO_CHAR, juntamente com os elementos de formataçãoYY e RR.N o t eq u e
podemos ter datas diferentes ao converter utilizandoRR e YY, dependendo
doanodadatainformada.
219

## Página 234

10.4. Funçõesdeconversão CasadoCódigo
Para mais detalhes e compreensão desse exemplo, consulte as regras do
usodofo rma toRRnalistadeelemen tosdefo rma taçãovistaan terio rmen te.
TO_NUMBER
Muitosemelhanteàfunção TO_DATE,estafunçãotambémtemopapelde
converterdeterminadosvalores. Seuobjetivo,noentanto,éfazeraconversão
decaracteresparanuméricos.
Quandofalamosnafunção TO_DATE,foimencionadoqueovalordoca-
racterequeestásendoinformadocomoparâmetrodevesercompatívelcomo
formato. Poisbem,quandotrabalhamoscom
TO_NUMBER,omesmotambém
acontece. Aoinformarmosumvalorcaractereparaafunção TO_NUMBER,ele
devesercompatívelcomoformatoqueestamospassandoparaafunção. To-
davia,existeumaparticularidadequantoaoformatoparacasasdecimaisede
grupo(milhar,porexemplo).
Para cálculos internos do Oracle, sempre será usado ponto (
.)c o m o
separador decimal, e vírgula (,) para separador de grupo, como padrão
americano. Para atribuições de variáveis do tipo caractere ou para visualiza-
ção, o Oracle pegará a formatação conforme estiver configurado na variável
NLS_NUMERIC_CHARACTERS(decimal,milhar).
Uma das razões pelas quais o Oracle utiliza essa premissa pode ser pelo
fato de a vírgula ser utilizada para a separação de valores ou colunas em um
comando SQL. Veja o exemplo, no qual fazemos um
SELECT do número
111,1utilizandovírgulacomoseparadordecimal:
SQL> select 111,1 from dual;
111 1
---------- ----------
111 1
SQL>
Agora, executando o mesmoSELECT, mas utilizando o ponto como se-
paradordecimal:
SQL> select 111.1 from dual;
220

## Página 235

CasadoCódigo Capítulo10. Trabalhandocomfunções
111.1
----------
111.1
SQL>
Noprimeiroexemplo,ocomandoSQLacabouentendendoque 111 era
umdadoe 1eraoutro. Omesmonãoaconteceuquando,emvezdeseparar-
mosporvírgula,separamosporponto.
Vejamosoexemploaseguir. Nele,estásetentandoconverterumvalorno
qualtemoscomoseparadordedecimaisavírgula,eparamilhar,oponto. Pois
bem, já sabemos que para cálculos de conversões internas o Oracle utiliza o
pontocomodecimal. Logo,ocomandoSQLaseguirgeraumerro:
SQL> select to_number(’4.569.900,87’) valor
from dual;
select to_number(’4.569.900,87’) valor
*
ERROR at line 1:
ORA-01722: invalid number
SQL>
Ok! O erro acontece porque, onde há vírgula, deveria ter ponto, e onde
háponto,deveriatervírgula. Poisbem,vejamoso SELECTaseguir:
SQL> select to_number(’4,569,900.87’) valor
from dual;
select to_number(’4,569,900.87’) valor
*
ERROR at line 1:
ORA-01722: invalid number
SQL>
Agora você deve estar se perguntando: mas por que o erro, sendo que
tudoindicaqueagoraoformatofoiinformadocorretamente,compontopara
decimaisevírgulaparamilhares? Vejao
SELECTaseguir:
221

## Página 236

10.4. Funçõesdeconversão CasadoCódigo
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
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
03 0
20
30
20
10
200 20
15 rows selected.
222

## Página 237

CasadoCódigo Capítulo10. Trabalhandocomfunções
SQL>
Observeacoluna SAL,maisprecisamenteoregistro EMPNO=7566. Veja
que o valor do salário está aparecendo como3272.5. Este número possui
comoseparadordedecimaisocaractereponto,masnãopossuiseparadorde
grupodemilhar.
Isso nos leva a conclusão de que, além de sabermos as regras para pon-
tos e vírgulas, também devemos estar cientes de como está definida a sessão
doOracle. NoOracle,aformataçãodemilharnãoaparece,amenosqueseja
aplicadaaformataçãoparatal. Vamosvoltaraoprimeiroexemplo,agoraapli-
candoumaformatação:
SQL> select to_number(’4.569.900,87’,’9G999G999D00’) valor
from dual;
select to_number(’4.569.900,87’,’9G999G999D00’) valor
*
ERROR at line 1:
ORA-01722: invalid number
SQL>
Ainda assim, o erro persiste. Também pudera, vimos no registro
EMPNO=7566 que na sessão do Oracle está definido como casa decimal o
ponto,enãoavírgula. Vamostrocar:
SQL> select to_number(’4,569,900.87’,’9G999G999D00’) valor
from dual;
VALOR
---------
4569900.9
SQL>
Bingo! Este comando SELECT funcionou por duas razões. Primeira: o
valor passado no formato caractere possui um número válido que contém
223

## Página 238

10.4. Funçõesdeconversão CasadoCódigo
comoseparadordecasasdecimaisomesmodefinidonasessãodoOracle. Se-
gundo: foidefinidoumformatoparaoqualestipulamosque,nesteconjunto
decaracteres,háseparadoresdegrupoquerepresentamoscomoelementode
função
G. Utilizando desta forma, o Oracle entende que o pontoéose p a r a -
dordedecimaleavírgula,odemilhar .P araprovarnossatese,vamosmudar
osseparadoresnasessãodoOracleeexecutaromesmo
SELECTanterior:
SQL> alter session set nls_numeric_characters=’.,’;
Session altered.
SQL> select to_number(’4.569.900,87’,’9G999G999D00’) valor
from dual;
select to_number(’4.569.900,87’,’9G999G999D00’) valor
*
ERROR at line 1:
ORA-01722: invalid number
SQL>
Agoravamostrocaroscaracteresdelugar:
SQL> select to_number(’4,569,900.87’,’9G999G999D00’) valor
from dual;
VALOR
---------
4569900.9
SQL>
Funcionou. Mas espere um momento! Além de converter, preciso saber
comoestádefinidonasessãodoOracle? Não. Nãoénecessáriosevocêespe-
cificar,alémdoformato,quaiscaracteresdevemserutilizadosparaasepara-
çãodedecimaisegrupos. Vejamosnovamenteoexemploanterioraoúltimo.
Nele, definimos que na sessão seria definido que o ponto seria a decimal, e
vírgula, o grupo. Contudo, isto gerou um erro ao executar nosso
SELECT
ondeestavajustamentedefinidoaocontráriodaparametrizaçãofeita.
224

## Página 239

CasadoCódigo Capítulo10. Trabalhandocomfunções
SQL> alter session set nls_numeric_characters=’.,’;
Session altered.
SQL> select to_number(’4.569.900,87’,’9G999G999D00’) valor
from dual;
select to_number(’4.569.900,87’,’9G999G999D00’) valor
*
ERROR at line 1:
ORA-01722: invalid number
SQL>
Utilizando o parâmetroNLS, aquele terceiro parâmetro da função que é
opcional,nósconseguimos,emvezdealterarasessãodoOracle,validaresses
caracteresapenasnonossocomando. Vamosexecutarnovamenteocomando
SELECTanterior,masagoraincorporandooterceiroparâmetro:
SQL> select to_number(’4.569.900,87’,’9G999G999D00’,
’nls_numeric_characters=,.’) valor
from dual;
VALOR
---------
4569900.9
SQL>
Funcionouperfeitamente. Emborapareçacomplicadonoinício,vocêvai
seacostumandocomascaracterísticaselogopegaalógica. Valesalientarque
estaquestãodasessãotambéméválidaparao TO_DATE.
Alémdautilizaçãodoselementosdeformatação G(grupo)e D(decimal),
vocêpodeoptarporutilizaremseuformatooponto . eavírgula ,.V e j ao
exemplo:
SQL> select to_number(’4,569,900.87’,’9,999,999.00’) valor
from dual;
VALOR
----------
4569900,87
225

## Página 240

10.4. Funçõesdeconversão CasadoCódigo
SQL>
Contudo,mesmoinformandoelementosfixos,porassimdizer,temosque
respeitar a definição padrão do Oracle para conversões internas (chamadas,
implícitas). Dessaforma,setentarmosimporumformatoparaoOracle,por
exemplo, utilizando vírgula para decimais, mesmo sendo de forma fixa, ele
nãopermitirá. Vejaaseguir:
SQL> select to_number(’4.569.900,87’,’9.999.999,00’) valor
from dual;
select to_number(’4.569.900,87’,’9.999.999,00’) valor
*
ERRO na linha 1:
ORA-01481: modelo inválido para formato de número
Observe que, mesmo informando a máscara de acordo com o número
informado,oOraclenãoaceitouaconversão. Eledesconheceoformatofixo,
comdecimaissendoseparadosporvírgula.
Massetentarmosmodificaropadrão,alterandoassimasessão? Vaifun-
cionar?
SQL> alter session set nls_numeric_characters=’,.’;
Sessão alterada.
SQL> select to_number(’4.569.900,87’,’9.999.999,00’) valor
from dual;
select to_number(’4.569.900,87’,’9.999.999,00’) valor
*
ERRO na linha 1:
ORA-01481: modelo inválido para formato de número
SQL>
Veja que o erro permanece, pois essa alteração reflete apenas para o uso
dos elementos G e D, e não para o uso fixo de elementos. Neste caso, para
conseguirmosconverterovalor,utilizandovírgulacomoseparadordecimal,
temosqueusaroselementosdeformato, mesmoquejátenhamosalteradoa
sessãoparatal. Agora,sim,aformacorreta:
226

## Página 241

CasadoCódigo Capítulo10. Trabalhandocomfunções
SQL> alter session set nls_numeric_characters=’,.’;
Sessão alterada.
SQL> select to_number(’4.569.900,87’,’9G999G999D00’) valor
from dual;
VALOR
----------
4569900,87
SQL>
Formatosdesessãoparadatas
Abrindo um parênteses dentro deste tópico, salientamos que, além das
alterações referente aos separadores numéricos, também podemos alterar as
sessões para definir um novo formato de data e também para a definição de
linguagens. Vejaexemplosdedefiniçãodeformatoparaasessão:
alter session set nls_language = ’BRAZILIAN PORTUGUESE’ ;
alter session set nls_date_language = ’PORTUGUESE’;
alter session set nls_date_format = ’DD/MM/RRRR’;
Agora,naprática,vejao SELECT,observandoacoluna HIREDATE:
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
227

## Página 242

10.4. Funçõesdeconversão CasadoCódigo
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
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
03 0
20
30
20
10
200 20
15 rows selected.
SQL>
Para o registro EMPNO=7566, o valor da coluna HIREDATE é
02-APR-81. Logo, este é o formato definido na sessão. Vamos olhar o pró-
ximo SELECT:
SQL> select to_date(’02-APR-81’) from dual;
TO_DATE(’
---------
02-APR-81
SQL>
228

## Página 243

CasadoCódigo Capítulo10. Trabalhandocomfunções
Nota-sequenãofoigeradoerro,mesmonãosendoinformadooformato.
Isso aconteceu porque o valor de caractere informado como string está no
mesmoformatodasessãodoOracle. Vejaoqueacontecequandocolocamos
astringemo u tr ofo rma to:
SQL> select to_date(’05/21/2009’) from dual;
select to_date(’05/21/2009’) from dual
*
ERROR at line 1:
ORA-01843: not a valid month
SQL>
Para consertar isso, devemos informar um formato compatível com o
conjuntodecaracteresinformadooutrocaroformatodasessãodoOracle.
Primeirovejaasoluçãoinformandoumformatocompatível:
SQL> select to_date(’05/21/2009’,’mm/dd/yyyy’) from dual;
TO_DATE(’
---------
21-MAY-09
SQL>
Agora,alterandoasessãodoOracle:
SQL> alter session set nls_date_format = ’mm/dd/yyyy’;
Session altered.
SQL> select to_date(’05/21/2009’) from dual;
TO_DATE(’0
----------
05/21/2009
SQL>
229

## Página 244

10.4. Funçõesdeconversão CasadoCódigo
Vejaalgunselementosdeformataçãoquepodemserusados:
• 9: cadanoverepresentaumcaracterequeserásubstituídopelocarac-
terereferenteaovalornuméricopassadocomoparâmetro. Oszerosna
frente são tratados como espaços em branco.Exemplo: 999999Resu-
tado:234
• 0: adicionando 0 como um prefixo ou sufixo ao número, todos os
zeros iniciais ou finais são tratados e exibidos como zeros em vez de
umespaçoembranco. Exemplo: 099999Resutado:001234
• $: prefixodosímbolodemoedaimpressonaprimeiraposição. Exem-
plo: $999999Resutado:$1234
• S: exibe um sinal de
+ inicial ou final quando o valor for positivo, e
umsinalde -inicialoufinalquandoovalorfornegativo;
• D: localização do ponto decimal. Os noves de ambos os lados refle-
temonúmeromáximodedígitospermitidos. Exemplo: 99D99Resu-
tado:99.99
• G: especificaumseparadordegrupo(milhar,porexemplo)comouma
vírgula.Exemplo: 9G999Resutado:9,999
• L: especifica a localização do símbolo de moeda local (tal como$).
Exemplo: L999999Resutado:FF1234
• ,:colocaumavírgulanaposiçãoespecificada,independentementedo
separadordegrupo. Exemplo: 999,999Resutado:999,9991,234
• .: especifica a localização do ponto decimal, independentemente do
separadordecimal. Exemplo: 999999.99Resutado:1234.00
• FM: remove os espaços em branco inicial e final.Exemplo: FM9999
Resutado:9999
• MI: Sinal de subtração à direita (valores negativos). Exemplo:
999999MIResultado: 1234-
230

## Página 245

CasadoCódigo Capítulo10. Trabalhandocomfunções
• PR: Números negativos entre colchetes.Exemplo: 999999PRResul-
tado: <1234>
• EEEE: Notação científica (o formato deve especificar quatro Es).
Exemplo: Notação científica (o formato deve especificar quatro Es).
Resultado: 1.234E+03
• U: Retorna o símbolo monetário dual “Euro” (ou outro) na posição
especificada.Exemplo:U9999Resultado: $1234
• V: M u l t i p l i c ap o r1 0nv e z e s( n=n ú m e r od e9 sa p ó sV ) .Exemplo:
9999V99Resultado: 123400
• S: Retorna o valor negativo ou positivo.Exemplo: S9999Resultado:
-1234or+1234
• B: Exibevaloreszeroembranco,enão0. Exemplo: B9999.99Resul-
tado: 1234.00
Há uma confusão muito comum entre o uso do TO_DATE ed o
TO_NUMBERnoquedizrespeitoaoresultadomostradopelo SELECTquando
sãoutilizadasessasduasfunções. Emboraestejamosinformandoumformato,
o Oracle não apresenta o resultado do SQL baseado nele. Isso acontece por-
q ueof o rma tonousodessasfunçõeséa penaspa raaco n v ersão ,enãopa raa
visualização. Paravisualizarmosoresultadocombasenoformatoquequere-
mos,utilizamoso
TO_CHAR.
TO_CHAR
Função utilizada para converter tipos de dados numéricos e datas para
caracteres. Além da conversão, ele é muito utilizado para formatação visual
dedados.
Seguem exemplos. Aqui, são selecionados todosos nomes dos emprega-
doseseusrespectivossalários. Foiutilizadaafunção
TO_CHAR paraforma-
tar os valores do salário, com o elemento de formatação para casas decimais
emilhar. Notequefoiutilizadooparâmetro
NLS_NUMERIC_CHARACTERS,
paradefinirquaiscaracteresdevemserutilizadosparacadaseparadordoele-
mento:
231

## Página 246

10.4. Funçõesdeconversão CasadoCódigo
SQL> select ename
,to_char(sal,’9G999G999D00’
,’nls_numeric_characters=’’.,’’’) sal
from emp;
ENAME SAL
---------- -------------
SMITH 800.00
ALLEN 1,600.00
WARD 1,250.00
JONES 3,272.50
MARTIN 1,250.00
BLAKE 2,850.00
CLARK 2,450.00
SCOTT 3,000.00
KING 5,000.00
TURNER 1,500.00
ADAMS 1,100.00
JAMES 950.00
FORD 3,000.00
MILLER 1,300.00
JOHN 1,000.00
15 rows selected.
SQL>
No próximo exemplo, a funçãoTO_CHAR foi utilizada para formatar a
data de admissão do empregado, mostrando apenas o mês referente a esta
data. O SELECT agrupa e apresenta quantos empregados foram admitidos
emcadamês:
SQL> select count (*) QT_ADMITIDOS
,to_char(hiredate,’mm’) MES
from emp
group by to_char(hiredate,’mm’);
QT_ADMITIDOS ME
------------ --
10 4
232

## Página 247

CasadoCódigo Capítulo10. Trabalhandocomfunções
20 9
41 2
11 1
20 1
20 2
10 5
10 3
10 6
9 rows selected.
SQL>
Vejaoutroexemplocom TO_CHAR,usadonaformataçãodedatas. Neste
programa, são impressos uma data e o número do dia que ela representa no
ano.
SQL>select ’22 de agosto de 2009 será o dia ’ ||
to_char(to_date(’22/08/2009’,’dd/mm/yyyy’),’ddd’)||
’ do ano’ from dual;
’22DEAGOSTODE2009SERÁODIA’||TO_CHAR(TO_DAT
------------------------------------------
22 de agosto de 2009 será o dia 234 do ano
SQL>
A seguir, são mostrados dados referentes à admissão do empregado:
nome do empregado, data de admissão e dia da semana. Este último foi for-
matadoatravésdafunção TO_CHAR:
SQL> select ename, hiredate, to_char(hiredate, ’day’) dia_semana
from emp;
ENAME HIREDATE DIA_SEMAN
---------- ---------- ---------
SMITH 12/17/1980 wednesday
ALLEN 02/20/1981 friday
WARD 02/22/1981 sunday
233

## Página 248

10.4. Funçõesdeconversão CasadoCódigo
JONES 04/02/1981 thursday
MARTIN 09/28/1981 monday
BLAKE 05/01/1981 friday
CLARK 06/09/1981 tuesday
SCOTT 12/09/1982 thursday
KING 11/17/1981 tuesday
TURNER 09/08/1981 tuesday
ADAMS 01/12/1983 wednesday
JAMES 12/03/1981 thursday
FORD 12/03/1981 thursday
MILLER 01/23/1982 saturday
JOHN 03/30/2011 wednesday
15 rows selected.
SQL>
Já neste exemplo, usamosTO_CHAR para imprimir em tela a data por
extenso:
SQL> select ’Joinville, ’ ||to_char(sysdate,’dd’)||’d e’ ||
initcap(to_char(sysdate, ’fmmonth’))||’d e
’||to_char(sysdate,’yyyy’)||’.’ from dual;
’JOINVILLE,’||TO_CHAR(SYSDATE,’DD’)
-----------------------------------
Joinville, 04 de April de 2011.
SQL>
Aqui utilizamos a função TO_CHAR para restringir dados em um
SELECT:
SQL> select *
from emp
where to_char(hiredate,’yyyy’)=’1982’ ;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- ---------- ---------
7788 SCOTT ANALYST 7566 12/09/1982 3000
234

## Página 249

CasadoCódigo Capítulo10. Trabalhandocomfunções
7934 MILLER CLERK 7782 01/23/1982 1300
COMM DEPTNO
--------- ---------
20
10
SQL>
Podemos concatenar strings juntamente com comandos de conversões.
Veja neste exemplo, na linha 6, a conversão dos salários de todos os empre-
gadossendoconcatenadacomastring R$representandoamoeda.
SQL> select ’R$ ’||to_char(sal, ’fm9G999G990D00’)
"SAL FORMATADO" , sal from emp;
SAL FORMATADO SAL
---------------- ---------
R$ 800.00 800
R$ 1,600.00 1600
R$ 1,250.00 1250
R$ 3,272.50 3272.5
R$ 1,250.00 1250
R$ 2,850.00 2850
R$ 2,450.00 2450
R$ 3,000.00 3000
R$ 5,000.00 5000
R$ 1,500.00 1500
R$ 1,100.00 1100
R$ 950.00 950
R$ 3,000.00 3000
R$ 1,300.00 1300
R$ 1,000.00 1000
15 rows selected.
SQL>
O próximo exemplo se parece com o anterior. Contudo, aqui estamos
utilizandooselementosdeformatação FM e L.Oprimeiroretiraosespaços
235

## Página 250

10.4. Funçõesdeconversão CasadoCódigo
em branco, onde algum elemento de formatação não tenha sido preenchido,
por ausência de valores. O segundo mostra a moeda configurada na sessão
dousuárionoqualoprogramaestásendoexecutado.
SQL> select to_char(sal,’fmL9G999G990D00’) "SAL FORMATADO" ,
sal from emp;
SAL FORMATADO SAL
----------------------- ---------
$800.00 800
$1,600.00 1600
$1,250.00 1250
$3,272.50 3272.5
$1,250.00 1250
$2,850.00 2850
$2,450.00 2450
$3,000.00 3000
$5,000.00 5000
$1,500.00 1500
$1,100.00 1100
$950.00 950
$3,000.00 3000
$1,300.00 1300
$1,000.00 1000
15 rows selected.
SQL>
Já a seguir, utilizamos o elemento de formataçãoS, que indica o sinal
referente ao valor formatado. Note que no valor positivo foi impresso, atrás
donúmero,osinaldepositivo( +),enquantoparaovalornegativoéimpresso
osinaldenegativo( -).
SQL> select to_char(174984283.75,’999,999,999.00S’) positivo
,to_char(100-1000,’999,999,999.00S’) negativo
from dual;
POSITIVO NEGATIVO
236

## Página 251

CasadoCódigo Capítulo10. Trabalhandocomfunções
--------------- ---------------
174,984,283.75+ 900.00-
SQL>
10.5 Funçõescondicionais
O Oracle disponibiliza outros tipos de funções, dentre as quais estão as fun-
çõescondicionais. Elassãoutilizadastantonaseleçãodedadospelacláusula
SELECTcomotambémnousodecláusulas WHERE.Seuusoébastantedifun-
didoebemflexível. Vejaaseguir:
• DECODE: esta estrutura funciona como uma estruturaIF-ELSE
dentro de uma cláusula SELECT. É muito utilizada principalmente
paravisualizaçãodedadosondeéprecisorealizaralgumtesteparasa-
berseestesdadospodemounãoaparecer;
• NULLIF: Afunção
NULLIF comparaduasexpressões. Seelasforem
iguais, a função retornará um valor nulo. Se elas não forem iguais, a
função retornará a primeira expressão. Entretanto, você não pode es-
pecificaroliteral
NULLparaaprimeiraexpressão;
• NVL: para esta função são passados dois parâmetros. Se o primeiro
fornulo,eleretornaosegundo,casocontrário,retornaoprimeiro;
• NVL2: A função NVL2 examina a primeira expressão. Se a primeira
expressãonãofornula,afunçãoNVL2retornaráasegundaexpressão.
Seaprimeiraexpressãofornula,aterceiraexpressãoseráretornada;
• CASE: muito parecido com o
DECODE. Seu objetivo também é per-
mitirautilizaçãodeumaestruturatipo IF-ELSEdentrodocomando
SQL. Mas ao contrário doDECODE sua aplicação e visualização são
maisinteligíveis(padrão ANSI).
• GREATEST:retornaamaiorexpressãodeumalistadevalorespassada
comoparâmetro. Todasasexpressõesapósaprimeirasãoconvertidas
paraotipodedadodaprimeiraantesdacomparaçãoserrealizada;
237

## Página 252

10.5. Funçõescondicionais CasadoCódigo
• LEAST: funcionaaoinversoda GREATEST:trazamenorexpressão.
• COALESCE: A vantagem desta função em relação aoNVL,éq u ee l a
podeaceitarváriosvaloresalternativos. Porexemplo,seaprimeiraex-
pressão passada para a COALESCE não for nula, a função retornará
aquela expressão. Caso contrário, ela fará umCOALESCE das expres-
sõesremanesceentes,ouseja,vaitestandoasdemaisatéencontraruma
queasatisfaçaacondiçãodenãonula.
Veja alguns exemplos. No primmeiro, utilizamos a função
CASE para
somartodosossaláriopordepartamento,agrupandoporcargo:
SQL> SELECT JOB,
sum(case
when deptno = 10 then sal
else
0
end) "DEPART 10" ,
sum(case
when deptno = 20 then sal
else
0
end) "DEPART 20" ,
sum(case
when deptno = 30 then sal
else
0
end) "DEPART 30" ,
sum(sal) "TOTAL JOB"
FROM EMP
GROUP BY JOB;
JOB DEPART 10 DEPART 20 DEPART 30 TOTAL JOB
--------- --------- --------- --------- ---------
CLERK 1300 2900 950 5150
SALESMAN 0 0 4100 4100
PRESIDENT 5000 0 0 5000
VENDEDOR 0 0 1500 1500
MANAGER 2450 3272.5 2850 8572.5
238

## Página 253

CasadoCódigo Capítulo10. Trabalhandocomfunções
ANALYST 0 6000 0 6000
6 rows selected.
SQL>
O segundo é idêntico ao anterior. Apenas trocamos a funçãoCASE pela
função DECODE. Vale lembrar queCASE é do padrão SQLANSI e DECODE
édopadrãoOracle:
SQL> select job
,sum(decode(deptno, 10, sal, 0)) "DEPART 10"
,sum(decode(deptno, 20, sal, 0)) "DEPART 20"
,sum(decode(deptno, 30, sal, 0)) "DEPART 30"
,sum(sal) "TOTAL JOB"
from emp
group by job;
JOB DEPART 10 DEPART 20 DEPART 30 TOTAL JOB
--------- --------- --------- --------- ---------
CLERK 1300 2900 950 5150
SALESMAN 0 0 4100 4100
PRESIDENT 5000 0 0 5000
VENDEDOR 0 0 1500 1500
MANAGER 2450 3272.5 2850 8572.5
ANALYST 0 6000 0 6000
6 rows selected.
SQL>
Nopróximoexemplo,estamosutilizandoafunção NVL.Notequequando
realizamos cálculos com valores nulos (segundo comandoSELECT) o Ora-
clenãoexecutataloperação. OOraclesempreconsideracomofalsoquando
existem valores NULL (nulo) em cálculos aritméticos ou no uso de restrição
dedados,porexemplo,emcláusulas WHERE.Quandoissooco rr e,eleigno ra
aação,masnãogeraerros.
SQL> select * from emp;
239

## Página 254

10.5. Funçõescondicionais CasadoCódigo
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- ---------- ---------
7369 SMITH CLERK 7902 12/17/1980 800
7499 ALLEN SALESMAN 7698 02/20/1981 1600
7521 WARD SALESMAN 7698 02/22/1981 1250
7566 JONES MANAGER 7839 04/02/1981 3272.5
7654 MARTIN SALESMAN 7698 09/28/1981 1250
7698 BLAKE MANAGER 7839 05/01/1981 2850
7782 CLARK MANAGER 7839 06/09/1981 2450
7788 SCOTT ANALYST 7566 12/09/1982 3000
7839 KING PRESIDENT 11/17/1981 5000
7844 TURNER VENDEDOR 7698 09/08/1981 1500
7876 ADAMS CLERK 7788 01/12/1983 1100
7900 JAMES CLERK 7698 12/03/1981 950
7902 FORD ANALYST 7566 12/03/1981 3000
7934 MILLER CLERK 7782 01/23/1982 1300
8000 JOHN CLERK 7902 03/30/2011 1000
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
03 0
20
30
20
10
200 20
15 rows selected.
SQL> select sum (sal+comm) from emp;
240

## Página 255

CasadoCódigo Capítulo10. Trabalhandocomfunções
SUM(SAL+COMM)
-------------
9000
SQL> select sum (sal+nvl(comm,0)) from emp;
SUM(SAL+NVL(COMM,0))
--------------------
32722.5
SQL>
Nestesexemplos,temosousodasfunções GREATESTe LEAST:
SQL> select greatest(’b’,’x’,’t’,’u’,’a’) maior_letra from dual;
M
-
x
SQL>
SQL> select least(’b’,’x’,’t’,’u’,’a’) menor_letra from dual;
M
-
a
SQL>
Nestesexemplos,temosousodafunção NULLIF:
SQL> select decode(nullif(’abacaxi’,’abacaxi’),null,’são iguais’
,’são diferentes’ )
comparação from dual;
COMPARAÇÃO
--------------
são iguais
241

## Página 256

10.5. Funçõescondicionais CasadoCódigo
SQL>
SQL> select decode(nullif(’abacaxi’,’morango’),null,’são iguais’
,’são diferentes’ )
comparação from dual;
COMPARAÇÃO
--------------
são diferentes
SQL>
SQL> select ’10=10: ’ || nvl2( nullif(10,10),’Diferentes’,
’Iguais’) resultado
from dual
union all
select ’11=10: ’ || nvl2( nullif(11,10),’Diferentes’,’Iguais’)
from dual
/
RESULTADO
-----------------
10=10: Iguais
11=10: Diferentes
SQL>
V ejaoU sodafunção NVL2.
SQL> select employee_id
,last_name
,job_id
,commission_pct
,nvl2(commission_pct,’Possui Comissão’ ,’Não Possui’ )
from employees
where employee_id between 175 and 183
/
EMPLOYEE_ID LAST_NAME JOB_ID COMMISSION_PCT
242

## Página 257

CasadoCódigo Capítulo10. Trabalhandocomfunções
----------- ---------------------- ---------- --------------
175 Hutton SA_REP 0,25
176 Taylor SA_REP 0,20
177 Livingston SA_REP 0,20
178 Grant SA_REP 0,15
179 Johnson SA_REP 0,10
180 Taylor SH_CLERK
181 Fleaur SH_CLERK
182 Sullivan SH_CLERK
183 Geoni SH_CLERK
NVL2(COMMISSION_PCT,’POSSUICOM
------------------------------
Possui Comissão
Possui Comissão
Possui Comissão
Possui Comissão
Possui Comissão
Não Possui
Não Possui
Não Possui
Não Possui
9 rows selected
SQL>
Veja um exemplo da funçãoCOALESCE onde usamos a função para re-
cuperarasinformaçõesdosempregados,seusgerentesesuascomissões,reu-
nindoestasinformaçõesemumamesmacoluna,dependendodacondição..
SQL> select last_name
,employee_id
,coalesce(to_char(commission_pct)
,to_char(manager_id)
,’No commision and no manager’ )
from employees
/
243

## Página 258

10.5. Funçõescondicionais CasadoCódigo
LAST_NAME EMPLOYEE_ID
------------------------- -----------
King 100
Kochhar 101
De Haan 102
Hunold 103
...
Partners 146
Errazuriz 147
Cambrault 148
Zlotkey 149
...
COALESCE(TO_CHAR(COMMISSION_PCT),TO_CHAR
----------------------------------------
No commision and no manager
100
100
102
.3
.3
.3
.2
107 rows selected.
SQL>
DECODEXCASE
Doscomandoscondicionaisvistosanteriormente,o DECODEéomaisuti-
lizado. Elefuncionacomoumaespéciedecondição“SE”( IF)paraalingua-
gemSQL.EstecomandoéexclusivodoOracle,entretanto,nopadrão ANSIda
linguagemSQLexisteumcomandosimilarchamado CASE.Vocêpodeusar
qualquer um deles. Entretanto, o uso doCASE só é permitido nas versões
mais novas do banco de dados Oracle. A Oracle, nas versões mais recentes,
vem inserindo comandos padrõesANSI, contudo, mantém seus comandos
244

## Página 259

CasadoCódigo Capítulo10. Trabalhandocomfunções
específicos com suas características para questões de compatibilidade. Veja
comparaçõesentreessesdoiscomandos.
Exemplo1
PadrãoANSI (tambémsuportadopeloOraclenasversõesmaisnovasdo
bancodedados):
SQL> select job,
sum(case
when deptno = 10 then sal
else
0
end) "DEPART 10" ,
sum(case
when deptno = 20 then sal
else
0
end) "DEPART 20" ,
sum(case
when deptno = 30 then sal
else
0
end) "DEPART 30" ,
sum(sal) "TOTAL JOB"
from emp
group by job;
JOB DEPART 10 DEPART 20 DEPART 30 TOTAL JOB
--------- ---------- ---------- ---------- ----------
CLERK 1300 1900 950 4150
SALESMAN 0 0 5600 5600
PRESIDENT 5000 0 0 5000
MANAGER 2450 2975 2850 8275
ANALYST 0 6000 0 6000
SQL>
PadrãoOracle:
SQL> select job,
sum(decode(deptno, 10, sal, 0)) "DEPART 10" ,
245

## Página 260

10.5. Funçõescondicionais CasadoCódigo
sum(decode(deptno, 20, sal, 0)) "DEPART 20" ,
sum(decode(deptno, 30, sal, 0)) "DEPART 30" ,
sum(sal) "TOTAL JOB"
from emp
group by job;
JOB DEPART 10 DEPART 20 DEPART 30 TOTAL JOB
--------- ---------- ---------- ---------- ----------
CLERK 1300 1900 950 4150
SALESMAN 0 0 5600 5600
PRESIDENT 5000 0 0 5000
MANAGER 2450 2975 2850 8275
ANALYST 0 6000 0 6000
SQL>
Exemplo2
PadrãoANSI (tambémsuportadopeloOraclenasversõesmaisnovasdo
bancodedados):
SQL> select ename
, job
, mgr
,
case
when mgr = 7902 then ’MENSALISTA’
when mgr = 7839 then ’COMISSIONADO’
when mgr = 7566 then ’MENSAL/HORISTA’
else
’OUTROS’
end tipo
from emp;
ENAME JOB MGR TIPO
---------- --------- ---------- --------------
SMITH CLERK 7902 MENSALISTA
ALLEN SALESMAN 7698 OUTROS
WARD SALESMAN 7698 OUTROS
JONES MANAGER 7839 COMISSIONADO
246

## Página 261

CasadoCódigo Capítulo10. Trabalhandocomfunções
MARTIN SALESMAN 7698 OUTROS
BLAKE MANAGER 7839 COMISSIONADO
CLARK MANAGER 7839 COMISSIONADO
SCOTT ANALYST 7566 MENSAL/HORISTA
KING PRESIDENT OUTROS
TURNER SALESMAN 7698 OUTROS
ADAMS CLERK 7788 OUTROS
JAMES CLERK 7698 OUTROS
FORD ANALYST 7566 MENSAL/HORISTA
MILLER CLERK 7782 OUTROS
14 linhas selecionadas.
SQL>
PadrãoOracle:
SQL> select ename
,job
,mgr
,decode(mgr,7902,’MENSALISTA’
,7839,’COMISSIONADO’
,7566,’MENSAL/HORISTA’
,’OUTROS’) tipo
from emp;
ENAME JOB MGR TIPO
---------- --------- ---------- --------------
SMITH CLERK 7902 MENSALISTA
ALLEN SALESMAN 7698 OUTROS
WARD SALESMAN 7698 OUTROS
JONES MANAGER 7839 COMISSIONADO
MARTIN SALESMAN 7698 OUTROS
BLAKE MANAGER 7839 COMISSIONADO
CLARK MANAGER 7839 COMISSIONADO
SCOTT ANALYST 7566 MENSAL/HORISTA
KING PRESIDENT OUTROS
TURNER SALESMAN 7698 OUTROS
ADAMS CLERK 7788 OUTROS
JAMES CLERK 7698 OUTROS
247

## Página 262

10.5. Funçõescondicionais CasadoCódigo
FORD ANALYST 7566 MENSAL/HORISTA
MILLER CLERK 7782 OUTROS
14 linhas selecionadas.
SQL>
A opção entre usar um ou outro vai depender da abrangência do seus
comandos SQL. Se eles forem específicos para o uso em Oracle, oDECODE
podeserusadosemproblemas. Inclusive,comopôdeservistonosexemplos,
elepodesetornarvisualmentemaisclaroparaoentendimentodocódigo. Já
se suas aplicações forem abrangentes no que diz respeito a operar em vários
bancosdedados,vocêteráqueusaropadrão ANSI,ouseja,usaro
CASEpara
queelesfuncionememqualquerbancodedados,oupelomenosnaquelesque
seguemestepadrão.
248

## Página 263

Capítulo11
Integridadededadose
integridadereferencial
11.1 Integridade de dados e integridade refe-
rencial
Paraqueasinformaçõesemumbancodedadospossampermaneceríntegras,
utilizamosumrecursomuitointeressantequeoprópriobancodedadosOra-
cle disponibiliza – estamos falando das
CONSTRAINTS.A s CONSTRAINTS
jáforamvistasnodecorrerdolivro,masnãoforamdetalhadastecnicamente.
Neste tópico iremos conhecê-las e identificá-las, tendo em vista que até este
pontojáutilizamosdiretaouindiretamenteseusrecursos.
Através das
CONSTRAINTS, conseguimos manter, por exemplo, a inte-
gridadeentreduastabelas. Tambémconseguimoscriticardeterminadovalor

## Página 264

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
que esteja sendo inserido em um campo da tabela ou até obrigar que este
campo seja preenchido. Desta forma, conseguimos manter a integridade,
tantodedadoscomoareferencial,mesmoqueissonãoestejasendofeitoatra-
vés de um programa (telas de cadastro, por exemplo), ou seja, podemos de-
finir regras quevão ser implementadas diretamenteno banco, independente
deexistiremounãocontrolesnasaplicações.
As
CONSTRAINTSqueiremosversãoasseguintes:
• NOTNULL
• UNIQUEKEY
• PRIMARYKEY
• FOREIGNKEY
• CHECK
NOTNULL
Esta CONSTRAINT garante que um campo da tabela tenha que ser obri-
gatoriamentepreenchidonomomentodainclusãodealgumregistro.
Noexemploaseguir,acriaçãodeuma CONSTRAINT jánomomento da
criaçãodatabela.
SQL> create table regions
( region_id number constraint region_id_nn not null
,region_name varchar2(25)
);
Table created.
SQL>
Vejamaisexemplosaseguirparaamanipulaçãode CONSTRAINTS NOT
NULL:
Vamos criar uma CONSTRAINT de NOT NULL p a r aoc a m p o
REGION_NAME da tabela REGIONS. Podemos criá-la de duas formas,
250

## Página 265

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
nomeando-a ou não. Utilizamos para manipularCONSTRAINTS em tabe-
las já existentes o comandoALTER TABLE , como vimos anteriormente. O
script a seguir mostra a criação de umaCONSTRAINT nomeada, que recebe
umnomenomomentodesuacriação.
SQL> desc regions
Name Null? Type
------------------------------- -------- ----
REGION_ID NOT NULL NUMBER
REGION_NAME VARCHAR2(25)
SQL> alter table regions modify region_name constraint
region_name_nn not null ;
Table altered.
SQL> desc regions;
Name Null? Type
------------------------------- -------- ----
REGION_ID NOT NULL NUMBER
REGION_NAME NOT NULL VARCHAR2(25)
SQL>
SQL> select constraint_name
from user_cons_columns
where table_name = ’REGIONS’
and column_name = ’REGION_NAME’;
CONSTRAINT_NAME
------------------------------
REGION_NAME_NN
SQL>
Noteque,paravisualizara CONSTRAINTcriada,montamosum SELECT
emcimadatabela USER_CONS_COLUMNS,selecionandopelonomedatabela
epelono medacol una.
251

## Página 266

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
Assimcomoparaas CONSTRAINTS,tambémpodemosvisualizarin-
formaçõesdeíndicesnoníveldecoluna,atravésdeumatabelachamada
USER_IND_COLUMNS.
Paraexcluiruma CONSTRAINTexistentetambémutilizamosocomando
ALTER TABLE .
SQL> alter table regions drop constraint region_name_nn;
Table altered.
SQL> desc regions;
Name Null? Type
------------------------------- -------- ----
REGION_ID NOT NULL NUMBER
REGION_NAME VARCHAR2(25)
SQL>
Já o exemplo a seguir mostra a criação de umaCONSTRAINT não no-
meada. Neste caso, não quer dizer que ela não terá uma identificação, o que
acontece é que o Oracle define um nome para ela. Note que a criação desta
CONSTRAINT é implícita pelo Oracle, pois, em nenhum momento estamos
adicionando uma CONSTRAINT. O que fazemos é modificar uma coluna
NULL para NOT NULL . Fazendo isto o Oracle criará umaCONSTRAINT au-
tomaticamente.
SQL> alter table regions modify region_name not null ;
Table altered.
SQL> desc regions;
Name Null? Type
------------------------------- -------- ----
REGION_ID NOT NULL NUMBER
REGION_NAME NOT NULL VARCHAR2(25)
SQL> select constraint_name
from user_cons_columns
252

## Página 267

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
where table_name = ’REGIONS’
and column_name = ’REGION_NAME’;
CONSTRAINT_NAME
------------------------------
SYS_C0011019
SQL>
O mesmo acontece quando modificamos uma coluna paraNULL.N e s t e
casooOracleeliminaa CONSTRAINTcriadaporele.
SQL> alter table regions modify region_name null;
Table altered.
SQL> desc regions;
Name Null? Type
------------------------------- -------- ----
REGION_ID NOT NULL NUMBER
REGION_NAME VARCHAR2(25)
SQL> select constraint_name
from user_cons_columns
where table_name = ’REGIONS’
and column_name = ’REGION_NAME’;
no rows selected
SQL>
UNIQUEKEY
Esta CONSTRAINT é utilizada quando não queremos que os valores de
uma coluna possam se repetir. Seu conceito é bem parecido com a chave
primária. Entretanto, veremos mais adiante que a chave primária, além de
não permitir valores repetidos, não aceita valores nulos nos campos que fa-
z e mp a r t ed ac h a v e .N oc a s od a
CONSTRAINT UNIQUE , valores nulos são
permitidos, ou seja, ela desconsidera estes valores em sua verificação. Veja o
exemplo:
SQL> desc regions;
Name Null? Type
253

## Página 268

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
------------------------------- -------- ----
REGION_ID NOT NULL NUMBER
REGION_NAME VARCHAR2(25)
SQL> alter table regions modify region_name constraint
region_name_un unique;
Table altered.
SQL> desc regions;
Name Null? Type
------------------------------- -------- ----
REGION_ID NOT NULL NUMBER
REGION_NAME VARCHAR2(25)
SQL> select constraint_name
from user_cons_columns
where table_name = ’REGIONS’
and column_name = ’REGION_NAME’;
CONSTRAINT_NAME
------------------------------
REGION_NAME_UN
SQL>
Agora vamos tentar inserir um registro, colocando no campo
REGION_NAMEalgumnomejáexistentenatabela:
SQL> select * from regions;
REGION_ID REGION_NAME
--------- -------------------------
1 Europe
2 Americas
3 Asia
4 Middle East and Africa
SQL> insert into regions values (5,’Europe’);
254

## Página 269

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
insert into regions values (5,’Europe’)
*
ERROR at line 1:
ORA-00001: unique constraint (TSQL2.REGION_NAME_UN) violated
SQL>
Como o nomeEurope já existe na tabela, é gerado um erro. Isso ocor-
reu devido ao fato de termos criado umaCONSTRAINT do tipo UNIQUE.O
mesmo não acontece quando tentamos inserir um valor nulo para a coluna
emquestão:
SQL> insert into regions values (5,null);
1 row created.
SQL> select * from regions;
REGION_ID REGION_NAME
--------- -------------------------
1 Europe
2 Americas
3 Asia
4 Middle East and Africa
5
SQL>
Para desabilitar ou excluir umaCONSTRAINT, utilizamos o comando
ALTER TABLE .
SQL> alter table regions disable constraint region_name_un;
Table altered.
SQL> alter table regions drop constraint region_name_un;
Table altered.
255

## Página 270

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
SQL>
Uma CONSTRAINT também pode ser criada através do seguinte co-
mando:
SQL> alter table regions add constraint region_name_un_2
unique (region_name);
Table altered.
SQL>
PRIMARYKEY
Como já foi explicado anteriormente, a chave primária possui um obje-
tivo bem definido. Ela garante que a informação contida na coluna que faz
parte desta chave seja única. Dentro de uma tabela, ela vai servir como um
identificador único para cada linha existente. Uma chave primária pode ser
composta, ou seja, pode ser constituída de várias colunas. Nesse caso, essas
colunasservirãodeidentificadoresúnicosparacadaregistro.
Exemplodechaveprimáriasimples:
SQL> alter table regions add constraint reg_id_pk primary key
(region_id);
Table altered.
SQL>
Exemplodechaveprimáriacomposta:
SQL> alter table regions add constraint reg_pk_01 primary key
(region_id, region_name);
alter table regions add constraint reg_pk_01 primary key
(region_id, region_name)
*
ERROR at line 1:
ORA-02260: table can have only one primary key
256

## Página 271

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
SQL>
Notequeaotentarmoscriara CONSTRAINT dechaveprimáriaoOracle
gerou um erro nos dizendo que já existe uma chave primária criada para a
tabela REGIONS. É isso mesmo, o Oracle está certo. Criamos uma chave
primária chamada REG_ID_PK, no exemplo anterior. Uma tabela só pode
conter uma chave primária. Desta forma, se quisermos mesmo criar uma
novachaveprimária,devemosprimeiramenteexcluiraexistente.
SQL> alter table regions drop constraint reg_id_pk
Table altered.
SQL>
Vamostentarnovamente:
SQL> alter table regions add constraint reg_pk_01 primary key
(region_id, region_name);
alter table regions add constraint reg_pk_01 primary key
(region_id, region_name)
*
ERROR at line 1:
ORA-01449: column contains NULL values ; cannot alter to NOT NULL
SQL>
Ops! Outroerroocorreu. OOracledizquenãopodemoscriarumachave
primária utilizando colunas que possuem valores nulos. Isso é verdade e faz
parte das premissas para a criação de uma chave primária. Lembra quando
criamos uma região sem nome nos exemplos anteriores? Agora temos que
excluiresteregistroouatualizá-lodandoumnomederegião.
Vamosexcluí-lo:
SQL> select * from regions
/
257

## Página 272

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
REGION_ID REGION_NAME
--------- -------------------------
1 Europe
2 Americas
3 Asia
4 Middle East and Africa
5
SQL> delete from regions where region_id = 5;
1 row deleted.
SQL> select * from regions;
REGION_ID REGION_NAME
--------- -------------------------
1 Europe
2 Americas
3 Asia
4 Middle East and Africa
SQL>
Agorasim!
SQL> alter table regions add constraint reg_pk_01 primary key
(region_id, region_name);
Table altered.
SQL>
Vamostestarsenossachavefunciona:
SQL> select * from regions;
REGION_ID REGION_NAME
--------- -------------------------
1 Europe
258

## Página 273

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
2 Americas
3 Asia
4 Middle East and Africa
SQL> insert into regions (region_id, region_name) values
(1,’Brazil/West’);
1 row created.
SQL>
SQL> insert into regions (region_id, region_name)
values (1,’Europe’);
insert into regions (region_id, region_name) values (1,’Europe’)
*
ERROR at line 1:
ORA-00001: unique constraint (TSQL2.REGION_NAME_UN_2) violated
SQL> insert into regions (region_id, region_name)
values (1,null);
insert into regions (region_id, region_name) values (1,null)
*
ERROR at line 1:
ORA-01400: cannot insert NULL into
("TSQL2"."REGIONS"."REGION_NAME")
SQL> select * from regions;
REGION_ID REGION_NAME
--------- -------------------------
1 Brazil/West
1 Europe
2 Americas
3 Asia
4 Middle East and Africa
SQL> insert into regions (region_id, region_name)
259

## Página 274

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
values (5,’Brazil/South’);
1 row created.
SQL>
Vejamosalgumascaracterísticas:
No Oracle, quando criamos uma chave primária, automaticamente, um
índiceúnicoécriado. Casojáexistaumíndice,paraacolunaoucolunasque
compõemestachave,oOracleutilizaráoexistente. Entretanto,paraqueisto
aconteça,todasascolunasdesteíndicedevemestarpresentesnacomposição
da chave primária, inclusive na mesma ordem em que são apresentadas na
chave.
Quandoexcluímosumachaveprimária,oíndiceaelaassociadotambém
é excluído. Se quisermos excluir um índice referente a uma chave primária,
devemosprimeiramentedesabilitá-la. Jáquandoativamosumachaveprimá-
ria,umíndiceúnicoécriado,casoelenãoexista.
V amosanalisaratabela
DEPARTMENTS:
select index_name name
,’INDEX ’ ||index_type type
,null referencia
,status
from user_indexes
where table_name = ’DEPARTMENTS’
union
select constraint_name
,’CONSTRAINT ’ ||upper(decode(constraint_type,’C’, ’Check’,
’O’, ’R/O View’ ,
’P’, ’Primary’,
’R’, ’Foreign’,
’U’, ’Unique’,
’V’,’Check view’ )) constraint_type
,’CONSTRAINT ’ ||r_constraint_name
,status
from user_constraints
where table_name = ’DEPARTMENTS’
order by 1
260

## Página 275

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
Este SELECTtrazinformaçõestantode CONSTRAINTScomodeíndices.
Vejaoresultadonasequência:
Fig.11.1
Nas linhas em destaque temos para a tabelaDEPARTMENTS um índice
eu m aCONSTRAINT de PRIMARY, ou seja, uma chave primária foi criada
para esta tabela. Automaticamente, quando ela foi criada, o Oracle também
criouumíndiceparaestachave. Vamosveroqueacontecequandotentamos
excluiroudesabilitarachave:
SQL> alter table departments disable constraint DEPT_ID_PK;
alter table departments disable constraint DEPT_ID_PK
*
ERROR at line 1:
ORA-02297: cannot disable constraint (TSQL.DEPT_ID_PK) -
dependencies exist
SQL>
Primeiramente, o Oracle nos informa que não podemos desabilitar a
CONSTRAINT de chave primária, pois existem pendências provindas dela. O
que o Oracle quer dizer com isto? Provavelmente, esta tabela possui alguns
dados e eles já estão sendo utilizados em uma ou mais tabelas. Mas como o
Oracle identificou isto? Não se preocupe, não tem mistério. Se formos pro-
cu r a rq ua i ssã oa sta be la sq u eu sa mc o m or e f e r e n c iaan o s sac h a v ep ri m á ria ,
vamosencontraroresultadoaseguir.
261

## Página 276

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
Naslinhasemdestaque,vemosqueexistemduaschavesestrangeiras(ve-
remosoconceitonopróximotópico)quereferenciam,ouseja,ligamatabela
DEPARTAMENTSàstabelas EMPLOYEESe JOB_HISTORY.
SQL> select table_name
,constraint_name
from user_constraints
where r_constraint_name = ’DEPT_ID_PK’;
TABLE_NAME CONSTRAINT_NAME
------------------------------ ------------------------------
EMPLOYEES EMP_DEPT_FK
JOB_HISTORY JHIST_DEPT_FK
SQL>
Comoscomandosqueaprendemosanteriormente,vamosdesabilitá-las:
SQL> alter table employees disable constraint EMP_DEPT_FK;
Table altered.
SQL> alter table job_history disable constraint JHIST_DEPT_FK;
Table altered.
SQL>
Em seguida tentamos novamente, desabilitar aCONSTRAINT de chave
primária:
SQL> alter table departments disable constraint DEPT_ID_PK;
Table altered.
SQL>
Pronto! CONSTRAINTS desabilitadas. Mastalvezvocêdeveestarseper-
guntando: Não há jeito mais fácil de desabilitar estas referências, sem ser
uma a uma? Há sim! Você pode fazer isso colocando logo após o nome da
262

## Página 277

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
CONSTRAINT a seguinte cláusula: CASCADE. Ao invés de desabilitarmos as
CONSTRAINTS uma a uma, vamos desabilitar todas asCONSTRAINTS (de
uma só vez) que fazem referência à chave primária em questão, utilizando
CASCADE.V ejaoexem plo:
SQL> alter table departments disable constraint DEPT_ID_PK
cascade;
Table altered.
SQL>
Isso faz com que o Oracle procure as dependências existentes para a
CONSTRAINT em questão (chave primária) e desabilite qualquer referência
ligadaaela.
Agoravamosexecutarnovamenteo SELECTeveroresultado:
Fig.11.2
Oíndiceaindapermaneceeestáválido. Entretanto,nossa CONSTRAINT
de chave primária foi desabilitada. Vamos a mais um caso, voltamos a ha-
bilitar a nossa chave primária. OCASCADE não funciona para habilitarmos
as CONSTRAINTS em cascata, neste caso vamos habilitar uma a uma. Mas
espere, vamos continuar trabalhando com a chave primária, então, vejamos
os comandos na sequência. Vamos executar somente o primeiro, os demais
ficamsomentecomoexemplo.
SQL>
SQL> alter table departments enable constraint DEPT_ID_PK
263

## Página 278

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
/
Table altered.
SQL> alter table job_history enable constraint JHIST_DEPT_FK
/
Table altered.
SQL> alter table employees enable constraint EMP_DEPT_FK
/
Table altered.
SQL>
Voltamosaterostatusanterioràsalterações.
Fig.11.3
Agoravamosexcluiroíndice DEPT_ID_PKparavercomovaisecompor-
tar nossa chave primária. Vale lembrar que, para excluir um índice referente
aumachaveprimária,temosquedesabilitá-laprimeiro.
SQL> alter table departments disable constraint DEPT_ID_PK;
Table altered.
SQL> drop index DEPT_ID_PK;
264

## Página 279

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
Index dropped.
SQL>
Segueonovoresultado:
Fig.11.4
Podemos ver que o índice foi excluído e que aCONSTRAINT de chave
primáriacontinuaexistindo,emboradesabilitada. Vamoshabilitá-laparaver
oqueacontece:
SQL> alter table departments enable constraint DEPT_ID_PK;
Table altered.
SQL>
Resultado:
Fig.11.5
265

## Página 280

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
Noteque,quandohabilitamosa CONSTRAINTdechaveprimária,oOra-
cle criou o índice. Preste atenção em um detalhe. Como já excluímos o
índice uma vez, o Oracle vai excluir o índice sempre que desabilitarmos a
CONSTRAINT.
SQL> alter table departments disable constraint DEPT_ID_PK;
Table altered.
SQL>
Resultado:
Fig.11.6
Comestesexemplos,ficoumaisfácilentendercomofuncionaoconceito
de comoo Oracle mantéma integridade daschaves primárias. Agora vamos
entendercomofuncionamaschavesestrangeiras.
FOREIGNKEY
Seu papel é estabelecer relacionamentos entre tabelas e umbanco de da-
dos. Quandoescrevermosummodelodedadosenvolvendotabelas,nóspen-
samosemrelacionamentos,quesãoresponsáveisporligarumaoumaistabe-
las. Um relacionamento pode ocorrer entre duas ou mais tabelas, mas tam-
bémpodeacontecerdentrodamesmatabela. Chamamosistodeautorrelaci-
onamento.
Mas um relacionamento não serve apenas para melhor visualizarmos o
modelodedadosouparamostrarcomodeterminadastabelasestãoserelaci-
onando. Seuobjetivoémuitomaisimportanteemerecetotalatenção.
266

## Página 281

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
Atravésdosrelacionamentos,podemosmanteralgoqueéchamadode in-
tegridadereferencial,ouseja,garantiasdequeosdadosentreastabelasque
estão se relacionando estejam íntegros. Isso é conseguido através da criação
das
FOREIGN KEYS ou Chaves Estrangeiras, como são comumente chama-
das.
Existem regras para definição e funcionamento dessas chaves, por isto,
quandoestivermosdefinindoummodelodedadosrelacional,devemospres-
tar bastante atenção no negócio como um todo. Precisamos que de ponta
a ponta os dados possam permanecer íntegros, de forma que possamos
recuperá-losdamaneiracomoquisermosequandonósprecisarmos.
Depois de bem definidas e criadas na base de dados, seu funcionamento
segue regras para que o banco de dados possa identificar e avisar caso al-
gum problema aconteça. Basicamente, seu funcionamento ocorre da se-
guinte forma: a coluna
chave estrangeira sempre referencia uma co-
luna chave primária , sendo de outra tabela ou da mesma. Quando re-
ferenciamos, não apenas indicamos uma ligação, mas também criamos uma
dependência entre os objetos, ou melhor, entre seus registros. Dessa forma,
para manter esse controle funcionando, as seguintes regras e restrições são
aplicadas:
• Nãoépermitidaainclusãodedadosemumacolunachaveestrangeira
que não existam em uma chave primária, tanto no que diz respeito a
relacionamentos entre duas ou mais tabelas quanto em um autorrela-
cionamento.
• Assimcomonainserção,emumaatualizaçãodedadosemumachave
estrangeira, também não são permitidos valores que não constam na
chaveprimáriareferenciada.
• No caso de exclusão de dados de uma chave primária, a integridade
referencialestabelecidapelachave estrangeiragarantequeosregistros
referenciados não possam ser excluídos, evitando que os registros fi-
quemórfãos.
• Omesmoacontecequandotentamosatualizardadosdeumachavepri-
máriaquepossuemreferênciascomoutraschavesestrangeiras. Aleida
267

## Página 282

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
integridadereferencialgarantequeissonãosejapossível.
Vamosverificaras CONSTRAINTScriadasparaatabela DEPARTMENTS:
select constraint_name
,’CONSTRAINT ’ ||upper(decode(constraint_type,
’C’, ’Check’,
’O’, ’R/O View’ ,
’P’, ’Primary’,
’R’, ’Foreign’,
’U’, ’Unique’,
’V’,’Check view’ ))
constraint_type
,’CONSTRAINT ’ ||r_constraint_name referencia
,status
from user_constraints
where table_name = ’DEPARTMENTS’
order by 1
Fig.11.7
O b s e rv eq u eat a b e l aDEPARTMENTS possui várias CONSTRAINTS.V a -
mosdestacara CONSTRAINT DEPT_ID_PK q ueéa CONSTRAINT dechave
primáriadatabela.
Vamosverificaras CONSTRAINTScriadasparaatabela EMPLOYEES.
select constraint_name
,’CONSTRAINT ’ ||upper(decode(constraint_type,
’C’, ’Check’,
’O’, ’R/O View’ ,
’P’, ’Primary’,
268

## Página 283

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
’R’, ’Foreign’,
’U’, ’Unique’,
’V’,’Check view’ ))
constraint_type
,’CONSTRAINT ’ ||r_constraint_name referencia
,status
from user_constraints
where table_name = ’EMPLOYEES’
order by 1
Fig.11.8
Atabela EMPLOYEEStambémpossuivárias CONSTRAINTS,atémaisque
a tabela anterior. Isso ocorre porque em nosso modelo de dados esta tabela
possui muitos relacionamentos com outras do sistema. Vamos nos atentar
para duas
CONSTRAINTS,a EMP_EMP_ID_PK ea EMP_DEPT_FK.Ap r i -
meiraéreferenteàchaveprimáriadatabelaeas egundafazreferênciaàtabela
DEPARTMENTS, ou seja, nosso relacionamento. Se analisarmos o contexto,
essa chave estrangeira garante que só conseguimos cadastrar um empregado
para um departamento existente na tabela de departamentos. Com isso, não
corremos o risco de cadastrar empregados com códigos de departamentos
inexistentes. Está aí nossa integridade referencial. Vamos ver se as regras e
restriçõesmencionadasanteriormentesãoverdadeiras?
Vamostentarinserirumnovoempregadoparaumdepartamentoquenão
269

## Página 284

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
existenatabeladedepartamentos.
SQL> insert into employees
values(207,’FERNANDO’,’SILVA’,’FSILVA’,’9998-9990’,SYSDATE,
’MK_MAN’,1000,0,206,
280,’01-JAN-79’,SYSDATE);
insert into employees
*
ERROR at line 1:
ORA-02291: integrity constraint (TSQL.EMP_DEPT_FK) violated -
parent key not found
SQL>
Atravésda CONSTRAINTdechaveestrangeira EMP_DEPT_FK,foigaran-
tida a integridade dos dados. O Oracle identificou a violação da integridade
referencialebloqueouainserção. Vamostentaratualizarodepartamentode
um determinado empregado utilizando um departamento inexistente, para
vercomooOraclevaisecomportaragora:
SQL> update employees
set department_id = 390
where employee_id = 100;
update employees
*
ERROR at line 1:
ORA-02291: integrity constraint (TSQL.EMP_DEPT_FK) violated -
parent key not found
SQL>
Mais uma vez, através da chave estrangeira a integridade foi mantida.
Agoravamosfazerocontrário. Jávimosqueatravésdachaveestrangeiracri-
ada para a tabela referenciada (EMPLOYEES) garantimos a integridade dos
dados, não permitindo, com aCONSTRAINT EMP_DEPT_FK , que fossem
utilizados códigos de departamentos não existentes. Contudo, precisamos
testar as duas pontas e, para isto, vamos tentar realizar algumas alterações
270

## Página 285

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
na tabela referência (DEPARTMENTS), onde está localizada a chave primária
DEPT_ID_PK.
Vimosqueosvalorescontidosemcolunasdechaveestrangeiradevemser
origináriosdeumadeterminadachaveprimáriapertencenteaoutratabelaou
atémesmoàprópriatabela. Emnossos exemplos, estamos trabalhandocom
o relacionamento entre as tabelas
EMPLOYEES e DEPARTMENTS que estão
ligadaspelacoluna DEPARTMENT_ID.Vamostentaralteraralgumcódigode
departamentoexistentequecontenhaempregadoscadastradosparaveroque
acontece.
SQL> update departments
set department_id = 999
where department_id = 10
/
update departments
*
ERROR at line 1:
ORA-02292: integrity constraint (TSQL.EMP_DEPT_FK) violated -
child record found
SQL>
Notequeaconsistênciafoifeitaeamensagemdequeoregistroqueestá
sendoalteradopossuidependênciaemoutrasfontesfoimostrada. Maisuma
vez,foigarantidaaintegridade. Naexclusãoocorreráamesmasituação,con-
tudo,vamosveroseguinteexemplo:
SQL> delete from departments
where department_id = 10;
delete from departments
*
ERROR at line 1:
ORA-02292: integrity constraint (TSQL.EMP_DEPT_FK) violated -
child record found
SQL>
271

## Página 286

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
Agora vejamos um exemplo de criação deCONSTRAINT de FOREIGN
KEY:
SQL> alter table emp add constraint dept_emp_fk
foreign key (deptno)
references dept (deptno);
Tabela alterada.
SQL>
Neste exemplo, é vista a criação daFOREIGN KEY em cima da tabela
EMP,aqualpossuiocampo DEPTNOquefazreferênciaàtabela DEPT,campo,
este, utilizado na chave. Note também que, ao criar esse tipo de chave, so-
mosobrigadosainformarestareferência,utilizandoacláusula REFERENCES
comoformadeconsistirorelacionamentoentreasduastabelas.
CHECK
Comoonomesugere,as CONSTRAINTSde CHECKsãoutilizadasparaa
realizaçãodechecagensemcolunasdeumatabela. Vocêasutilizaparadeter-
minarvaloresiniciaisefinaisparacamposdataenumérico,pararestringira
entrada de determinados valores etc. Por exemplo, vamos supor que para o
campovalordacomissãonãoépermitidaaentradadevalorescasooempre-
gado não seja um vendedor. Através de uma
CONSTRAINT CHECK pode-se
fazerestecontrole. Outroexemploseriatermosumcampoquesópoderece-
berosvalo r es‘ M ’e‘ F’ .
Vejaalgunsexemplos:
Criando
Permitircódigodedepartamentoentre10e900:
SQL> alter table departments add constraint dept_id_ck
check (department_id between 10 and 900);
Table altered.
SQL>
272

## Página 287

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
Permitir somente a entrada de valores em maiúsculo para o campo
EMAIL:
SQL> alter table em loyees add constraint email_ck
check (email = upper(email));
Table altered.
SQL>
Permitirsomenteainserçãodedeterminadasregiões:
SQL> alter table regions add constraint region_name_ck
check (region_name in (’Europe’,’Americas’,’Asia’,
’Middle East and Africa’ ));
Table altered.
SQL>
Permitirsomenteaentradaderegistrosapenasquandoasomadosalário
maisaco missãosejamaio rquedezmil.
SQL> alter table emp add constraint sal_comm_ck
check (sal + nvl(comm,0) < 10000);
Table altered.
SQL>
Nãopermitirqueempregadosnãovendedores( SALESMAN)tenhamco-
missãoinformadas.
SQL> alter table emp add constraint sal_comm_sales_ck
check ( (nvl(comm,0) = 0 and job <> ’SALESMAN’)
or (job = ’SALESMAN’));
Table altered.
SQL>
273

## Página 288

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
Excluindo
SQL> alter table emp drop constraint sal_comm_ck;
Table altered.
SQL>
Desabilitando/Habilitando
SQL> alter table emp disable constraint sal_comm_sales_ck;
Table altered.
SQL> alter table emp enable constraint sal_comm_sales_ck;
Table altered.
SQL>
Acriaçãoemanipulaçãodas CONSTRAINTS CHECK sãomuitoparecidas
comasjávistasnormalmente. Seufuncionamentotambémémuitointuitivo
e de fácil entendimento. Vamos ver agora algumas aplicações, em cima dos
exemplosvistos.
Entradaincorretadecódigodedepartamento:
SQL> insert into departments values(901,’TESTE CHECK’ ,200,1700);
insert into departments values(901,’TESTE CHECK’ ,200,1700)
*
ERROR at line 1:
ORA-02290: check constraint (TSQL.DEPT_ID_CK) violated
SQL>
Entradaincorretadoe-mail:
SQL> insert into employees
values( 900, ’Pato’,’Donald’,’pdonald’,’234.423.4567’,
’03-JAN-2001’,’IT_PROG’,9000,0,102,60,
274

## Página 289

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
’03-JAN-1975’,’03-NOV-1991’);
insert into employees
*
ERROR at line 1:
ORA-02290: check constraint (TSQL.EMAIL_CK) violated
SQL>
Entradaincorretadaregião:
SQL> insert into regions values(5,’TESTE’);
insert into regions values(5,’TESTE’)
*
ERROR at line 1:
ORA-02290: check constraint (TSQL.REGION_NAME_CK) violated
SQL>
Entradaincorretadosaláriomaiscomissão(valormaior):
SQL> insert into emp values(9875,’MARCOS’,’SALESMAN’,7698,
’09-JUL-1989’,7500,4000,20);
insert into emp values(9875,’MARCOS’,’SALESMAN’,7698,
’09-JUL-1989’,7500,4000,20)
*
ERROR at line 1:
ORA-02290: check constraint (TSQL.SAL_COMM_CK) violated
SQL>
Entradaincorretadacomissãoquantoaocargo:
SQL> insert into emp values(9875,’MARCOS’,’CLERK’,7902,
’09-JUN-1985’,8000,3000,20);
insert into emp values(9875,’MARCOS’,’CLERK’,7902,
’09-JUN-1985’,8000,3000,20)
*
ERROR at line 1:
275

## Página 290

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
ORA-02290: check constraint (TSQL.SAL_COMM_SALES_CK) violated
SQL>
Podemosverquetodasas CONSTRAINTScriadasobtiveramsucessonos
seusobjetivos,garantindoaintegridadedasinformações. Nãorestamdúvidas
de que sua utilidade pode ajudar e muito na concretização e bom funciona-
mentodomodelodedados.
FOREIGNKEYDELETECASCADE,SETNULLEDISABLE
O Oracle dispõe de algumas funcionalidades que podem ser usadas na
criaçãode CONSTRAINTS.Vamosdiscuti-lasnasequência,mas,antesdisso,
vamoscriarumacópiadatabela DEPT.Vamoschamá-lade DEPARTAMENTO.
Elaseráutilizadaemnossosexemplos.
SQL> create table departamento as select * from dept;
Table created.
SQL> select * from departamento;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
50 TI BRASIL
SQL>
SQL> alter table departamento add constraint pk_deptno
primarykey (deptno);
Table altered.
SQL>
DELETECASCADE
276

## Página 291

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
Quandodefinimosuma CONSTRAINTde FOREIGN KEY como DELETE
CASCADE, estamos informando ao Oracle que, quando um valor de chave
primária referente à chave estrangeira em questão for excluído, os registros
referenciadosporestachave(emoutrastabelasounamesma)podemserex-
cluídos. Emboraesterecursosejamuitointeressanteeprático,deve-setomar
muitocuidado,poisprecisamosestarcientedetodasasreferênciasexistentes
paranãoacabarmosporexcluirregistrosquenãopoderiamserexcluídos.
SQL> create table empregado
( empno number(4,0)
,ename varchar2(10)
,job varchar2(9)
,mgr number(4,0)
,hiredate date
,sal number(7,2)
,comm number(7,2)
,deptno number(2,0) constraint deptno_fk references
departamento(deptno) on delete cascade
)
/
Table created.
SQL>
A CONSTRAINT DEPTNO_FK dizaoOracleque,sealgumdepartamento
databela DEPARTAMENTOforexcluído,todososempregadosqueestãoloca-
dos neste departamento devem ser excluídos também. Vamos ver como isso
funcionaria:
Paracomeçar,inserimosnatabela EMPREGADOosdadosdatabela EMP:
SQL> insert into empregado select * from emp;
14 rows created.
SQL>
Mostrandoosdadosdatabelapopulada:
277

## Página 292

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
SQL> select * from empregado;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
9999 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
10
14 rows selected.
SQL>
278

## Página 293

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
Mostrandoosdadosdatabela DEPARTAMENTO:
SQL> select * from departamento;
DEPTNO DNAME LOC
--------- -------------- -------------
10 ACCOUNTING NEW YORK
20 RESEARCH DALLAS
30 SALES CHICAGO
40 OPERATIONS BOSTON
50 TI BRASIL
SQL>
Agoravamostentarexcluirodepartamento 20:
SQL> delete from departamento where deptno = 20;
1 row deleted.
SQL>
L e m b r e - s eq u e ,q u a n d oc r i a m o sat a b e l aEMPREGADOS, definimos uma
CONSTRAINT DELETE CASCADE . Logo, quando excluímos um registro na
tabela DEPARTAMENTO,t oda sa sr ef er ên cia sco mata be laEMPREGADOS são
afetados. Vejaoresultadoaseguir:
SQL> select * from empregado;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
9999 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7900 JAMES CLERK 7698 03- DEC-81 950
7934 MILLER CLERK 7782 23-JAN-82 1300
279

## Página 294

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
COMM DEPTNO
--------- ---------
300 30
500 30
1400 30
30
10
10
03 0
30
10
9 rows selected.
SQL>
Comopodeservisto,alémdaexclusãododepartamento,tambémforam
excluídososempregadosdestedepartamentonatabela EMPREGADOS.
SETNULL
Já quando definimos estaCONSTRAINT como SET NULL , estamos in-
dicando que, para as referências existente nos valores de chave estrangeira,
deve-se atualizar com valores nulos, caso os valores de chaves primárias fo-
rem excluídos. Ao contrário do
DELETE CASCADE , os registros referencia-
dosnãoserãoexcluídos,apenasterãoseusvaloresatualizadosparanulos.
SQL> create table empregado
( empno number(4,0) constraint empno_pk primary key
,ename varchar2(10)
,job varchar2(9)
,mgr number(4,0) constraint mgr_fk references
empregado on delete set null
,hiredate date
,sal number(7,2)
,comm number(7,2)
,deptno number(2,0)
);
280

## Página 295

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
Table created.
SQL>
Neste exemplo estamos definindo que caso um gerente seja excluído, os
empregados que estão subordinados a ele ficarão sem gerente, ou seja, fica-
rão com o campoMGR como nulo. Assim, são preservados os registros e a
integridadedosdadosémantida. Vejaaseguirumexemplo:
SQL> insert into empregado select * from emp;
14 rows created.
SQL>
Visualizandoosdadosdatabela EMPREGADOS:
SQL> select * from empregado;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
COMM DEPTNO
--------- ---------
20
281

## Página 296

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
300 30
500 30
20
1400 30
30
10
20
10
03 0
20
30
20
10
14 rows selected.
SQL>
Vamos excluir um empregado, que tenha pelo menos um subordinado.
Conseguimosvisualizarissoatravésdacoluna MGR:
SQL> delete from empregado where empno = 7839;
1 row deleted.
SQL> select * from empregado;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 01-MAY-81 2850
7782 CLARK MANAGER 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
282

## Página 297

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
10
13 rows selected.
SQL>
Excluímosoempregado KING.Logo,seusubordinado JONESteveain-
formaçãoreferenteàgerêncialimpa.
DISABLE
Utilizandoaexpressão DISABLE,estamosindicandoquea CONSTRAINT
devesercriada,masquedevepermanecerdesabilitada. Ocontrárionãoéne-
cessário,poisquandocriamosuma CONSTRAINTelaporpadrãojáéativada.
SQL> create table empregado
( empno number(4,0)
,ename varchar2(10)
,job varchar2(9)
,mgr number(4,0)
,hiredate date
,sal number(7,2) constraint ck_sal
check (sal< 10000) disable
283

## Página 298

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
,comm number(7,2)
,deptno number(2,0)
);
Table created.
SQL>
Criamosuma CONSTRAINTquecontrolaaentradadosvaloresnacoluna
salário. Contudo,adeixamosdesabilitada.
Vamosverificarseufuncionamento.
Alimentandoatabela EMPREGADO:
SQL> insert into empregado select * from emp;
14 rows created.
SQL> commit;
Commit complete.
SQL>
Visualizandoosdadosinseridos:
SQL> select * from empregado;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
284

## Página 299

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
10
14 rows selected.
SQL>
Atualizando o salário referente ao empregado7839 para 20000.N e -
nhumerroocorreu,ouseja,a CONSTRAINTnãofoiacionada.
SQL> update empregado set sal = 20000 where empno = 7839;
1 row updated.
SQL> rollback;
Rollback complete.
SQL>
Agora vamos habilitar aCONSTRAINTparaveroqueacontece.
285

## Página 300

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
SQL> alter table empregado enable constraint ck_sal;
Table altered.
SQL>
Executamosomesmo UPDATEeagoraa CONSTRAINTfoiacionada,ge-
randooerro:
SQL> update empregado set sal = 20000 where empno = 7839;
update empregado set sal = 20000 where empno = 7839
*
ERROR at line 1:
ORA-02290: check constraint (TSQL.CK_SAL) violated
SQL>
Veja agora como poderiam ficar todas as declarações em uma definição
detabela:
SQL> create table empregado
( empno number(4,0) constraint pk_empno primary key
,ename varchar2(10)
,job varchar2(9)
,mgr number(4,0) constraint fk_mgr references
empregado on delete set null
,hiredate date default sysdate
,sal number(7,2) constraint ck_sal
check (sal< 10000) disable
,comm number(7,2) default 0
,deptno number(2,0) constraint fk_deptno references
departamento (deptno) on delete cascade
);
Table created.
SQL>
286

## Página 301

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
V a m o sa b r i ru mp a r â m e t r op a r af a l a rs o b r ead e c l a r a ç ã od ec r i a ç ã o
das CONSTRAINTS. Nos exemplos de criação de CONSTRAINTS sem-
pre vimos como criá-las através do comandoALTER TABLE . Todavia, as
CONSTRAINTS também podem ser criadas e definidas no momento em que
estamosmontandoo SCRIPTdacriaçãodatabela. Tambémháduasformas
defazeristo. AOraclechamaessasdefiniçõesde CONSTRAINT IN-LINE e
CONSTRAINT OUT-OF-LINE .
CONSTRAINTINLINE
Estetipoconsisteemdeclararas CONSTRAINTSlogodepoisdonomeda
coluna. Você pode fazer isso de forma nomeada ou não. Como já foi visto
anteriormente, caso não nomeie, o Oracle criará um nome interno para a
CONSTRAINT.Vejaosdoisexemplos:
Nomeando-as:
create table employees
( employee_id number(6,0) constraint pk_emp primary key
,first_name varchar2(20)
,last_name varchar2(25) constraint nn_last_name check
("LAST_NAME" IS NOT NULL )
,email varchar2(25) constraint nn_email NOT NULL
,phone_number varchar2(20)
,hire_date date constraint nn_hire_date check
("HIRE_DATE" IS NOT NULL )
,job_id varchar2(10) constraint nn_emp_job check
("JOB_ID" IS NOT NULL )
,salary number(8,2)
,commission_pct number(2,2)
,manager_id number(6,0)
,department_id number(4,0) constraint fk_emp_dept references
departments (department_id)
)
Semnomeação:
create table employees
( employee_id number(6,0) primary key
287

## Página 302

11.1. Integridadededadoseintegridadereferencial CasadoCódigo
,first_name varchar2( 20)
,last_name varchar2(25) check
("LAST_NAME" IS NOT NULL )
,email varchar2(25) NOT NULL
,phone_number varchar2(20)
,hire_date date check ("HIRE_DATE" IS NOT NULL )
,job_id varchar2(10) check ("JOB_ID" IS NOT NULL )
,salary number(8,2)
,commission_pct number(2,2)
,manager_id number(6,0)
,department_id number(4,0) references departments
(department_id)
)
Aquestãodenomearounãovaidecadaum.Asduasformasestãocorre-
tas. Contudo, sevocêquiserusarpadrõesdenomesetornarmaisfácileágil
a identificação das CONSTRAINTS criadas no seu banco de dados, fica aí a
dica. Apenasvaleressaltarque,independentededarnomesounão,issonão
prejudicaemnadaseufuncionamento.
CONSTRAINTOUFOFLINE
Jáestetipoconsisteemdeclararas CONSTRAINTS logodepoisdadecla-
raçãodetodasascolunas. Nestecaso,aformanomeadaéobrigatória. Vejao
exemplo:
create table employees
( employee_id number(6,0)
,first_name varchar2(20)
,last_name varchar2(25)
,email varchar2(25) constraint nn_email not null
,phone_number varchar2(20)
,hire_date date
,job_id varchar2(10)
,salary number(8,2)
,commission_pct number(2,2)
,manager_id number(6,0)
,department_id number(4,0)
,constraint pk_emp primary key (employee_id)
288

## Página 303

CasadoCódigo Capítulo11. Integridadededadoseintegridadereferencial
,constraint nn_last_name check ("LAST_NAME" IS NOT NULL )
,constraint nn_hire_date check ("HIRE_DATE" IS NOT NULL )
,constraint nn_emp_job check ("JOB_ID" IS NOT NULL )
,constraint fk_emp_dept foreign key (department_id) references
departments (department_id)
)
Para as CONSTRAINTS de NOT NULL não é possível declarar neste for-
mato,mantendo,portanto,oformato INLINE.
289

## Página 305

Capítulo12
Oracleavançado
12.1 Trabalhandocomviews
Muitas vezes os usuários precisam acessar várias colunas que estão em mais
deumatabela. Issopodesetornarcomplexoquandonãoháodomíniodalin-
guagemSQLedispendiosoquandoseprecisadestainformaçãováriasvezes.
Comocomando
SELECTpodemoscriarumconjuntodedadosquesatisfaça
as necessidades do usuário, montando grupos de informações provenientes
deumaoumaisfontes(tabelas). Essapráticadenomina-se
VIEW.Utilizando
VIEWS,pode-secriarumamontagemdosdados,comsomenteaquelasinfor-
maçõesdequeousuárioprecisa. Portanto,uma VIEW nadamaiséqueuma
montagemdedados,criadaemtempodeexecução,comosefosseoresultado
deum
SELECT.Vejalgumasobservaçõessobreas VIEWS:

## Página 306

12.1. Trabalhandocomviews CasadoCódigo
• Geralmente, as visões não são armazenadas, precisando ser recalcula-
daspara cadaconsultaque asreferencie. No bancoéguardada apenas
suaespecificação.
• Adeclaração SELECTquedefineumavisãonãopodeconterumacláu-
sula ORDER BY .
• Podem-sefazer INSERTSem VIEWS,desdequeemsuaespecificação
nãohaja SUBQUERIES, UNIONS, MINUS,maisdeumatabelanacláu-
sula FROM,n ã oh a j aSELECTS em cláusulas FROM e WHERE,en ã o
tenhamfunçõesdeagregaçãoouexpressões.
•A s VIEWS também podem ser do tipo “materializada”. Neste caso, os
dadossãoarmazenadosnobancodedados.
•E s t e t i p o d eVIEWcomumenteéutilizadoquandograndesvolumesde
dadossãorecuperadosatravésdela.
• Épossívelexecutaroperações DMLnormalmentenas VIEWSsimples.
• Não é possível remover linhas se aVIEW contiver: funções de grupo,
cláusula GROUP BY , DISTINCTou ROWNUM.
• Nãoépossívelmodificarosdadosemuma VIEW seelacontiver: fun-
ções de grupo, cláusulaGROUP BY , DISTINCT, ROWNUM ou colunas
definidasporexpressões.
• Não será possível adicionar dados usando umaVIEW se ela incluir:
funçõesdegrupo,cláusula GROUP BY , DISTINCT, ROWNUM,colunas
definidas por expressões ou colunasNOT NULL em tabelas base que
nãosejamselecionadaspela VIEW.
Criandoumaviewdeempregadospordepartamentoquerecebem
comissão
SELECTbaseparaaco nstruçãoda VIEW:
SQL> select dname, ename, job, sal, comm
from emp e, dept d
where e.deptno = d.deptno
292

## Página 307

CasadoCódigo Capítulo12. Oracleavançado
and e.comm is not null ;
DNAME ENAME JOB SAL COMM
-------------- ---------- --------- --------- ---------
SALES ALLEN SALESMAN 1600 300
SALES WARD SALESMAN 1250 500
SALES MARTIN SALESMAN 1250 1400
SALES TURNER VENDEDOR 1500 0
RESEARCH JOHN CLERK 1000 200
SQL>
Criaçãoda VIEW EMP_DEPT_COMM :
SQL> create view emp_dept_comm as
select dname, ename, job, sal, comm
from emp e, dept d
where e.deptno = d.deptno
and e.comm is not null ;
View created.
SQL>
DESCRIPTIONe SELECTda VIEW.
SQL> desc emp_dept_comm;
Name Null? Type
------------------------------- -------- ----
DNAME VARCHAR2(14)
ENAME VARCHAR2(10)
JOB VARCHAR2(9)
SAL NUMBER(7,2)
COMM NUMBER(7,2)
SQL> select * from emp_dept_comm;
DNAME ENAME JOB SAL COMM
-------------- ---------- --------- --------- ---------
SALES ALLEN SALESMAN 1600 300
SALES WARD SALESMAN 1250 500
293

## Página 308

12.1. Trabalhandocomviews CasadoCódigo
SALES MARTIN SALESMAN 1250 1400
SALES TURNER VENDEDOR 1500 0
RESEARCH JOHN CLERK 1000 200
SQL>
CriandoumaviewdeempregadosquetrabalhamcomTecnologia
daInformação(IT)nosEstadosUnidos
SELECTbaseparaaco nstruçãoda VIEW:
SQL> select e.first_name, e.job_id
from employees e
,departments d
,locations l
where e.department_id = d.department_id
and d.location_id = l.location_id
and l.country_id = ’US’
and d.department_name = ’IT’;
FIRST_NAME JOB_ID
-------------------- ----------
Alexander IT_PROG
Bruce IT_PROG
David IT_PROG
Valli IT_PROG
Diana IT_PROG
SQL>
Criaçãoda VIEW EMP_IT_US :
SQL> create view emp_it_us as
select e.first_name, e.job_id
from employees e
,departments d
,locations l
where e.department_id = d.department_id
and d.location_id = l.location_id
and l.country_id = ’US’
294

## Página 309

CasadoCódigo Capítulo12. Oracleavançado
and d.department_name = ’IT’;
View created.
SQL>
DESCRIPTIONe SELECTda VIEW:
SQL> desc emp_it_us
Name Null? Type
------------------------------- -------- ----
FIRST_NAME VARCHAR2(20)
JOB_ID NOT NULL VARCHAR2(10)
SQL> select * from emp_it_us;
FIRST_NAME JOB_ID
-------------------- ----------
Alexander IT_PROG
Bruce IT_PROG
David IT_PROG
Valli IT_PROG
Diana IT_PROG
SQL>
Criando VIEWS complexas para mostrar dados resultantes de um com-
mandoSQLco n tendofunçõesdegru po ,jun tandod uaso umaistabelas:
SQL> create or replace view dept_sum_vu (name, minsal, maxsal,
avgsal) as select d.department_name, min(e.salary),
max(e.salary), avg(e.salary) from employees e JOIN
departments d on (e.department_id = d.department_id)
group by d.department_name
/
View created.
SQL> select * from dept_sum_vu;
295

## Página 310

12.1. Trabalhandocomviews CasadoCódigo
NAME MINSAL MAXSAL AVGSAL
------------------------------ ---------- ---------- ----------
Administration 6442.04 6442.04 6442.04
Accounting 12152.03 17569.2 14860.615
Executive 24889.7 35138.4 28305.9333
IT 6149.22 13176.9 8433.216
Purchasing 3660.25 16105.1 6076.015
Human Resources 9516.65 9516.65 9516.65
Public Relations 14641 14641 14641
Shipping 3074.61 12005.62 5088.56089
Finance 10102.29 17569.2 12591.26
Sales 8931.01 20497.4 13112.3074
Marketing 8784.6 19033.3 13908.95
11 rows selected.
SQL>
Alterandoumaview
Paraalteraruma VIEW,recrie-autilizandoaexpressão OR REPLACE .
SQL> create or replace view emp_it_us as
select e.first_name, e.job_id
from employees e
,departments d
,locations l
where e.department_id = d.department_id
and d.location_id = l.location_id
and l.country_id = ’US’
and e.manager_id = 103 --inclusão de um gerente específico.
and d.department_name = ’IT’;
View created.
SQL>
Excluindoumaview
296

## Página 311

CasadoCódigo Capítulo12. Oracleavançado
SQL> drop view emp_dept_comm;
View dropped.
SQL>
UsandoacláusulaWITHCHECKOPTION
Quando estamos trabalhando com VIEWS podemos nos assegurar
quanto às questões de integridade. Por exemplo, se quisermos criar restri-
ções para determinados dados, que não possam ser manipulados através de
comandos DML, podemos utilizar a cláusula
WITH CHECK OPTION para
garantirisso. Vejaoexemploaseguir:
SQL> create view emp_manager124 as
2 select first_name, manager_id
3 from employees
4 where manager_id = 124
5 with check option constraint emp_manager124
6/
View created.
SQL> update emp_manager124 set manager_id = 201 where
manager_id = 124;
update emp_manager124 set manager_id = 201 where
manager_id = 124
*
ERROR at line 1:
ORA-01402: view WITH CHECK OPTION where -clause violation
SQL>
Neste exemplo, criamos umaVIEW que seleciona todos os empregado
cujoogerentesejao 124. Notequenadefiniçãoda VIEWutilizamosacláu-
sula WITH CHECK OPTION . Veja, também, que utilizamos a palavra-chave
CONSTRAINT e definimos um nome para ela. Feito isto, quando tentamos
atualizardadoscujogerentenãosejaaquelecomocódigo 124,porexemplo,
297

## Página 312

12.1. Trabalhandocomviews CasadoCódigo
um erro de violação é gerado. Esse tipo de checagem também funcionará se
tentarmosinserirouexcluirempregadosquenãotenhamcomovalorparao
campo
MANAGER_IDocódigo 124. Dessaforma,dadosquenãosãoselecio-
nadospela VIEWnãopodemsofrerqualquertipodealteraçãoseutilizarmos
estacláusula.
VIEWSsomenteLeitura
Outra opção bastante interessante é a possibilidade de restringirmos a
VIEW para que nenhum comando DML possa ter ação sobre ela, ou seja,
mantê-la em modo somente leitura. Para isso, utilizamos a cláusulaWITH
READ ONLY .Vejaoexemploaseguir:
SQL> create view emp_manager124 as
2 select first_name, manager_id
3 from employees
4 where manager_id = 124
5 with read only ;
View created.
SQL> update emp_manager124 set manager_id = 201 where
manager_id = 124;
update emp_manager124 set manager_id = 201 where
manager_id = 124
*
ERROR at line 1:
ORA-42399: cannot perform a DML operation on a read-only view
SQL>
Note, neste exemplo, que ao tentarmos atualizar dados daVIEW,u m a
mensagemdeerroégeradainformandoquesetratadeuma VIEWemmodo
somenteleitura.
298

## Página 313

CasadoCódigo Capítulo12. Oracleavançado
VIEWSMaterializadas(MaterializedVIEWS)
AsViewsMaterialized,assimconhecidasdesdeaversão9i,sãonadamais
queobjetosdobancodedadosOraclequecontêmdadoslocaisdetabelasre-
motasousãousadaspracriarumaagregaçãodetabelasemumdeterminado
intervalo de tempo. Uma curiosidade é que nas versões precedentes à 9i as
ViewsMaterializadaseramconhecidascomo Snapshots.
Vimos que as
VIEWScomunsnãoguardamosdadospropriamenteditos,
guardam apenas a estrutura de como estes dados devem ser recuperados. Já
as Views Materialized funcionam de forma diferente. Elas são geralmente
utilizadas quando estamos trabalhando com grandes quantidades de dados
ouquandoestesdadosdemandamumprocessamentomuitodemorado,que,
sefosseexecutadoonline,poderiacomprometerousodetodoosistema.
AcriaçãodeumaViewMaterializedenvolvetodaumaconfiguraçãoque
deve ser feita na sua definição. É neste momento que você especifica, por
exemplo,quandoelavaiseratualizada,dequeformavaiseratualizadaeassim
por diante. Não vamos explorá-la a fundo devido à necessidade de conheci-
mentos mais apurados, inclusive, sobre a administração do banco Oracle. A
títulodecuriosidade,segueumexemplo:
SQL> create materialized view emp_dept_20
refresh complete next sysdate + 1
as select * from emp where deptno = 20;
Snapshot created.
SQL> select * from emp_dept_20;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7566 JONES MANAGER 7839 02-APR-81 3272.5
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7876 ADAMS CLERK 7788 12-JAN-83 1100
7902 FORD ANALYST 7566 03- DEC-81 3000
COMM DEPTNO
299

## Página 314

12.1. Trabalhandocomviews CasadoCódigo
--------- ---------
20
20
20
20
20
SQL> drop materialized view emp_dept_20;
Snapshot dropped.
SQL>
Esta VIEWteráseusresultadosatualizadosacada1dia. Vejaoexemploa
seguir:
SQL> select sysdate from dual;
SYSDATE
---------
16-APR-11
SQL>
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
300

## Página 315

CasadoCódigo Capítulo12. Oracleavançado
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
10
14 rows selected.
SQL>
Nestequadro,mostramosadatacorrentee,nasequência,todososregis-
trosdatabela EMP.
SQL> select * from emp_dept_20;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7566 JONES MANAGER 7839 02-APR-81 3272.5
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7876 ADAMS CLERK 7788 12-JAN-83 1100
7902 FORD ANALYST 7566 03- DEC-81 3000
COMM DEPTNO
--------- ---------
20
301

## Página 316

12.1. Trabalhandocomviews CasadoCódigo
20
20
20
20
SQL> insert into empvalues(555,’EDUARDO’,’ANALISTA’,NULL
,’01-JAN-2011’,5000,NULL,20);
1 row created.
SQL> commit;
Commit complete.
SQL>
Logo após, selecionamos os dados daVIEW. Na sequência, fazemos um
INSERTnatabela EMP.
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
...
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
555 EDUARDO ANALISTA 01-JAN-11 5000
COMM DEPTNO
--------- ---------
20
300 30
302

## Página 317

CasadoCódigo Capítulo12. Oracleavançado
500 30
20
1400 30
20
30
20
10
20
15 rows selected.
SQL> select * from emp_dept_20;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7566 JONES MANAGER 7839 02-APR-81 3272.5
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7876 ADAMS CLERK 7788 12-JAN-83 1100
7902 FORD ANALYST 7566 03- DEC-81 3000
COMM DEPTNO
--------- ---------
20
20
20
20
20
SQL>
Selecionamososdadosdatabela EMP eco n sta ta mosq ueor egistr oin se-
rido está lá. Contudo, note que, embora tenhamos inserido um empregado
novo, ele não aparece naVIEW.I s s oa c o n t e c ep o r q u en o s s aVIEW está pro-
gramadaparaatualizarumavezpordiaapenas.
Vamosvercomoelaficaumdiadepoisdaentradadoempregadonovo:
SQL> select sysdate from dual;
303

## Página 318

12.2. Trabalhandocomíndices CasadoCódigo
SYSDATE
---------
17-APR-11
SQL> select * from emp_dept_20;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7566 JONES MANAGER 7839 02-APR-81 3272.5
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7876 ADAMS CLERK 7788 12-JAN-83 1100
7902 FORD ANALYST 7566 03- DEC-81 3000
555 EDUARDO ANALISTA 01-JAN-11 5000
COMM DEPTNO
--------- ---------
20
20
20
20
20
20
6 rows selected.
SQL>
Após 24 horas, nossaVIEW foi atualizada e agora o registro está sendo
mostrado.
12.2 Trabalhandocomíndices
Pode-sedizerqueíndicessãoestruturasdedadosmantidasinternamentepelo
gerenciadordobancodedadosparaotimizaroacessoaosdadosnastabelas.
Seu principal propósito é aumentar a performance na busca pelos dados em
tabelasdobancodedados. Existemalgumasregrasparaqueelessejamutili-
zadosnessasbuscas:
304

## Página 319

CasadoCódigo Capítulo12. Oracleavançado
• Quando as colunas na cláusulaSELECT fazem parte de um índice, e
pelomenosumadestascolunasexistanacláusula WHERE.
• Quando as colunas na cláusulaWHERE aparecem sem o emprego de
funções, ou seja, não fazem parte de uma expressão, ou não são pas-
sadas por parâmetro em funções tais comoTO_CHAR, TRUNC etc., a
menosquesejamíndicesbaseadosemfunção.
• Nocasodeíndicescompostos,afaltadeumacolunanacláusula WHERE
podefazercomqueobanconãouseoíndice,ouseja,oOraclelevaem
consideração a posição das colunas obedecendo a ordem definida no
momentodacriaçãodoíndice.
• Casoaquantidadededadosaserretornadaemumcomando
SELECT
sejamuitogrande,oOraclepodeoptarpornãousaroíndice.
NoOracle,osíndicessãoclassificadosportipos. Abordaremosostipos b-
treeebitmap. Osíndicesb-treesãoosíndicesdeusogeralnoOracle. Elessão
ostiposdeíndicespadrãocriadosduranteacriaçãodeíndices. Osíndicesb-
treepodemseríndicesdeumaúnicacoluna(simples)ouíndicescompostos
(várias colunas). Índices b-tree podem ter até 32 colunas. Os índices deste
tipopodemserúnicosounãoúnicos.
Único
Este tipo de índice é utilizado em colunas que não possuem valores em
duplicidade. Casotenhamosumacolunacomvaloresduplicados,estacoluna
nãopoderáserumíndiceúnico,amenosquesejacriadoumíndicecomposto.
Neste caso, as colunas juntas, que formam o índice, não poderão ter valores
duplicados. Vejaatabela
EMP:
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
305

## Página 320

12.2. Trabalhandocomíndices CasadoCódigo
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
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
03 0
20
30
20
10
200 20
15 rows selected.
SQL>
Agora, vamos criar um índice único para a colunaEMPNO. Note que ela
não possui valores duplicados, logo, é uma forte candidata a este tipo de ín-
dice.
306

## Página 321

CasadoCódigo Capítulo12. Oracleavançado
SQL> create unique index empno_un1 on emp (empno);
Index created.
SQL>
Vejaoqueacontecequandotentamoscriarumíndiceúnicoparaacoluna
JOB:
SQL> create unique index job_un1 on emp (job);
create unique index job_un1 on emp (job)
*
ERROR at line 1:
ORA-01452: cannot CREATE UNIQUE INDEX ; duplicate keys found
SQL>
Nãoconseguimos,poisnacoluna JOBexistemvaloresduplicados. Con-
tudo, se adicionarmos mais uma coluna, sendo que os valores concatenados
destas colunas nunca sejam duplicados (índices compostos), veremos que
nossoíndiceécriadocomsucesso.
SQL> create unique index job_ename_u1 on emp (job, ename);
Index created.
SQL>
Os índices também garantem a integridade dos dados e, no caso dos ín-
dicesúnicos,elenãodeixaráquevaloresduplicadossejaminseridosouatua-
lizadosnoscamposcompostosporele. Vamosverificarseistoéverdade?
SQL> insert into emp (empno) values (7369);
insert into emp (empno) values (7369)
*
ERROR at line 1:
ORA-00001: unique constraint (TSQL.EMPNO_UN1) violated
307

## Página 322

12.2. Trabalhandocomíndices CasadoCódigo
SQL>
Naatualizaçãoocorreomesmoerro.
SQL> update emp set empno = 7369
where empno = 7839;
update emp set empno = 7369
*
ERROR at line 1:
ORA-00001: unique constraint (TSQL.EMPNO_UN1) violated
SQL>
Estecontroledeintegridadetambémocorrecomosíndicescompostos:
SQL> insert into emp (empno,job, ename)
values (999,’CLERK’,’SMITH’);
insert into emp (empno,job, ename) values (999,’CLERK’,’SMITH’)
*
ERROR at line 1:
ORA-00001: unique constraint (TSQL.JOB_ENAME_U1) violated
SQL>
Se tomarmos cuidado e inserirmos os dados corretamente, respeitando
osíndices,nossoscomandosexecutarãodentrodoesperado.
SQL> insert into emp (empno) values (8888);
1 row created.
SQL>
SQL> update emp set empno = 9999
where empno = 7839;
1 row updated.
SQL>
308

## Página 323

CasadoCódigo Capítulo12. Oracleavançado
SQL> insert into emp (empno, job, ename)
values (999,’CLERK’,’JOAOZINHO’);
1 row created.
SQL>
Note neste último comando que, embora o valorCLERK já exista na co-
luna JOB, ele não acusa erro de chave violada. Isto ocorre porque o índice
não é composto apenas pelo campoJOB, mas também pelo campoENAME.
Logo,osvalores CLERKe JOAOZINHOnãoexistemnatabela EMP,demodo
quenãoviolamosoíndiceúnico.
Nãoúnico
Ao contrário do índice único, este índice permite que sejam criados ín-
dices em colunas cujos valores sejam duplicados. Isso vale tanto para índice
simples (com uma coluna), como para índices compostos (uma ou mais co-
lunas).
SQL> create index job_un1 on emp (job);
Index created.
SQL>
SQL> create index job_deptno_in1 on emp (job, deptno);
Index created.
SQL>
Logo,ocontroledeintegridadenãoérealizado.
SQL> insert into emp (empno, ename, job)
values (1111,’PEDRINHO’,’SALESMAN’);
1 row created.
SQL>
309

## Página 324

12.2. Trabalhandocomíndices CasadoCódigo
SQL> insert into emp (empno, ename, job, deptno)
values (1112,’LUIZINHO’,’SALESMAN’,30);
1 row created.
SQL>
Vejaaestruturadeumíndice b-TREE,definidaporgruposde ROWIDS
deformabalanceada.
BITMAP
Emumíndicebitmap,oOraclecriaumbitmapparacadachavedistintae
depois armazena asROWIDS associadas ao valor de chave como um bitmap.
Nocasodeumíndicecomum,esteprocessoérealizadopormeiodoarmaze-
namentodeumalistade ROWIDSparacadachavedeíndicequecorresponde
às linhas da tabela com aquele valor de chave, pois, no Oracle, cada chave é
armazenadajuntamentecomo
ROWIDcorrespondente. Ofuncionamentodo
índicebitmapacontecedaseguinteforma:
• U mmapadebitsparacadavalordechaveéusadoemvezdeumalista
de ROWIDS.Cadabitcorrespondeaumapossível ROWIDe,seobites-
310

## Página 325

CasadoCódigo Capítulo12. Oracleavançado
tivermarcadoisso,significaquealinhacomo ROWIDcorrespondente
contémovalorchave.
• Uma função de mapeamento é usada para converter a posição do bit
para o valor correspondente doROWID, para que o índice forneça a
mesmafuncionalidadequeumíndicecomum,mesmousandoumare-
presentaçãodiferente.
Uma das razões para a utilização dos índices bitmaps é quando temos
tabelasquepossuemumacardinalidadebaixa,istoé,acoluna(oucolunas)na
qualoíndiceébaseadopossuiumnúmeropequenodevaloresdistintos(por
exemplo: sexo, estado civil, UF). No caso da tabela
EMP, temos um campo
queseencaixanessesaspectos,ocampo JOB.Vejaaseguir:
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
9999 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
COMM DEPTNO
--------- ---------
20
300 30
500 30
311

## Página 326

12.2. Trabalhandocomíndices CasadoCódigo
20
1400 30
30
10
20
10
03 0
20
30
20
10
14 rows selected.
SQL>
Notequenacoluna JOBdiversosvaloresserepetemecomistoosdados
não se tornam muito distintos. Vejamos a criação de um índice bitmap para
estacoluna:
SQL> create bitmap index job_ibm1 on emp (job);
Index created.
SQL>
Tambémpodemoscriaríndicescompostosdotipobitmap.
Vejaaestruturadeumíndicebitmap,ondesãodefinidosmapasconforme
acolunaoucolunasescolhidasparaaindexação.
Fig.12.2
312

## Página 327

CasadoCódigo Capítulo12. Oracleavançado
Outroexemplo:
Fig.12.3: QuandocriamosumaCONSTRAINTdechaveprimária(vistomais
adiante) o Oracle, automaticamente, cria um índice único para as colunas
destachave,casonãoexista.
Quando criamos uma CONSTRAINT de chave primária (veja mais
adiante)oOracle,automaticamente,criaumíndiceúnicoparaascolunas
destachave,casonãoexista.
Sevocêtentarcriarumíndice,sendoeleb-TREEoubitmap,parauma
combinação de colunas já existente, o Oracle não deixará realizar esta
criação. Elemostraráumamensageminformandoquealistadecolunas
jáestáindexada.
Diretrizesparacriaçãodeíndices
• Crieumíndicequando:
– Umacolunacontiverumaamplafaixadevalores;
– Umacolunacontiverumgrandenúmerodevaloresnulos;
– Umaoumaiscolunasforemusadasconjuntamenteemumacláu-
sula WHEREouemumacondiçãodejunção;
– A tabela for grande e houver a expectativa de que a maioria das
consultasrecuperarámenosde2%a4%daslinhasnatabela.
313

## Página 328

12.3. Sinônimos CasadoCódigo
• Nãocrieumíndicequando:
– Ascolunasnãoforemusadascomfrequênciacomoumacondição
naconsulta;
– Atabelaforpequenaehouveraexpectativadequeamaioriadas
consultasrecuperarámaisde2%a4%daslinhasnatabela;
– Atabelaforatualizadacomfrequência;
– Ascolunasindexadasforemreferenciadascomopartedeumaex-
pressão.
12.3 Sinônimos
Parasimplificaroacessoaosobjetosemumbancodedadosutilizamossinô-
nimos. Atravésdeles,épossívelabreviarnomesdeobjetoslongosereferir-se
facilmente a objetos de outro usuário. Um sinônimo funciona como sendo
umaliasparaoobjeto,podendosercriadodeformaprivadaembaixodopró-
prio
SCHEMAouemnívelpúblico. Esteúltimodáacessoatodososusuários,
entretanto, só pode ser criado ou excluído pelo administrador do banco de
dados.
Comojáfoidito,osinônimoprivadodevesercriadoembaixodo
SCHEMA
(usuário) o qual deseja acessar o objeto. Contudo, não podemos confundir
seu objetivo. Mesmo tendo um sinônimo criado para um determinado ob-
jeto,issonãogarantiráoacesso. Lembre-sedequeossinônimossão
ALIAS
(apelidos)enãofornecemconcessõesaobjetos.
Antesdecriarmosossinônimos,precisamosterconcessões( GRANTS)de
acessoaosobjetos,paranossossinônimosfuncionarem.
Os sinônimos públicos (PUBLIC) são criados também embaixo de um
SCHEMA, entretanto, ele não estará restrito a ele, como acontece com a cria-
ção privada. Ao contrário, ele estará disponível para todos os usuários que
possuemacessoaobanco.
Nos capítulos anteriores, vimos como dar
GRANTS aos objetos para que
outrosusuáriospossamacessarobjetosdosquaisnãosãodonos. Vimosque,
embora determinado usuário tivesse
GRANT para acessar um objeto, era ne-
cessáriocolocarnafrentedonomedesteobjetoonomedoseudono. Através
314

## Página 329

CasadoCódigo Capítulo12. Oracleavançado
dacriaçãodesinônimos,podemosisentarestainformação. Comisso,ousuá-
rio que for acessar o objeto não precisa saber embaixo de qualSCHEMA ele
estácriado.
Vamos acompanhar alguns exemplos. Para isso, utilizaremos o usuário
TSQL já visto em capítulos anteriores. Também vamos criar mais dois usuá-
riosparatestarmosasfuncionalidadesdossinônimos.
Criandousuários:
SQL> create user aluno1 identified by aluno1;
User created.
SQL> grant resource, connect to aluno1;
Grant succeeded.
SQL>
SQL> create user aluno2 identified by aluno2;
User created.
SQL> grant resource, connect to aluno2;
Grant succeeded.
SQL>
Testandousuários:
SQL> conn aluno1/aluno1@xe2;
Connected.
SQL>
SQL> conn aluno2/aluno2@xe2;
Connected.
SQL>
Selecionandoosdadosdatabeladeempregadosatravésdousuário TSQL,
queéseudono:
315

## Página 330

12.3. Sinônimos CasadoCódigo
SQL> conn tsql/tsql@xe2;
Connected.
SQL>
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
10
316

## Página 331

CasadoCódigo Capítulo12. Oracleavançado
14 rows selected.
SQL>
Vamosveroqueacontecequandotentamosacessaratabela EMPatravés
dousuário ALUNO1,quecriamosrecentemente.
SQL> conn aluno1/aluno1@xe2;
Connected.
SQL>
SQL> select * from emp;
select * from emp
*
ERROR at line 1:
ORA-00942: table or view does not exist
SQL> select * from tsql.emp;
select * from tsql.emp
*
ERROR at line 1:
ORA-00942: table or view does not exist
SQL>
Vimos que não conseguimos acessar a tabela, nem mesmo colocando o
nome do usuário dono na frente do nome. Vamos tentar criar um sinônimo
paraatabela,aindanousuário ALUNO1:
SQL> create synonym emp for tsql.emp;
create synonym emp for tsql.emp
*
ERROR at line 1:
ORA-01031: insufficient privileges
SQL>
Nãofoipossívelcriarosinônimo,pois ALUNO1nãotemprivilégiospara
isso. Vamosvoltaraousuário TSQLecriarestesinônimoporlá. Outraalter-
nativaseriadar GRANTdecriaçãodesinônimospara ALUNO1.
317

## Página 332

12.3. Sinônimos CasadoCódigo
SQL> conn tsql/tsql@xe2;
Connected.
SQL>
SQL> create synonym aluno1.emp for tsql.emp;
Synonym created.
SQL>
Agoravamosvoltaraousuário ALUNO1etentaracessarnovamente:
SQL> conn aluno1/aluno1@xe2;
Connected.
SQL>
SQL> select * from emp;
select * from emp
*
ERROR at line 1:
ORA-00942: table or view does not exist
SQL>
Ainda não estamos conseguindo acessar a tabela. Não é para tanto: ape-
nas criamos o sinônimo, ainda não foi dada a concessão de acesso à tabela.
Lembre-sedoquefalamosanteriormente–sinônimosnãoconcedemacesso.
Vamos criar uma concessão, através do comando
GRANT para a tabela em
questão. Para isso, temos que estar conectado no usuário dono da tabela ou
umusuárioquetenhaacessototalaobancodedados(
SYS, SYSTEMou um
usuárioquetenharecebidoo GRANTde DBA,porexemplo). Mas,parabrin-
carmosumpoucocomocenário,vamosexcluirosinônimocriadoanterior-
menteantesdecriaro
GRANT:
SQL> drop synonym emp;
Synonym dropped.
SQL>
318

## Página 333

CasadoCódigo Capítulo12. Oracleavançado
Perfeito. Agoravamoscriaro GRANT:
SQL> conn tsql/tsql@xe2;
Connected.
SQL>
SQL>
SQL>
SQL> grant select on emp to aluno1;
Grant succeeded.
SQL>
Criadaaconcessão,vamostentaracessaratabela:
SQL> conn aluno1/aluno1@xe2;
Connected.
SQL>
SQL> select * from emp;
select * from emp
*
ERROR at line 1:
ORA-00942: table or view does not exist
SQL> select * from tsql.emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
319

## Página 334

12.3. Sinônimos CasadoCódigo
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
10
14 rows selected.
SQL>
Percebemos que na primeira tentativa não foi possível acessá-la, entre-
tanto,aocolocarnonomedodononafrentedatabela,conseguimosvisuali-
zar seus dados. Agora, para que não seja preciso informar este dono, vamos
criarnossosinônimonovamente:
SQL> conn tsql/tsql@xe2;
Connected.
SQL>
SQL> create synonym aluno1.emp for tsql.emp;
Synonym created.
SQL> conn aluno1/aluno1@xe2;
Connected.
320

## Página 335

CasadoCódigo Capítulo12. Oracleavançado
SQL>
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
10
14 rows selected.
321

## Página 336

12.3. Sinônimos CasadoCódigo
SQL>
Pronto. Sinônimocriadoetestado. Quetalagoramodificarmosestesinô-
nimo,simplificandoseunome? Paranãoficarmosalternandoentreumusuá-
rioeo u tr o ,vamosdarGRANTpara ALUNO1criarsinônimos.
SQL> conn tsql/tsql@xe2;
Connected.
SQL>
SQL> grant create synonym to aluno1;
Grant succeeded.
SQL>
Agora,vamosexcluirecriarnovamenteosinônimomodificando-o:
SQL> conn aluno1/aluno1@xe2;
Connected.
SQL>
SQL> drop synonym aluno1.emp;
Synonym dropped.
SQL> create synonym aluno1.e for tsql.emp;
Synonym created.
SQL> select * from e;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
322

## Página 337

CasadoCódigo Capítulo12. Oracleavançado
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
10
14 rows selected.
SQL>
Para que ALUNO2 possa acessar esta mesma tabela, também são neces-
sários os mesmos passos realizados para oALUNO1, a menos, é claro, que
criemos um sinônimo público (PUBLIC). Entretanto, temos que ter ciência
quetodososusuárioscriadosnabasededadosterãoacessoaestesinônimo.
Contudo,apenasosquepossuemconcessãoterãoacessoaosdadosdatabela.
Vamoscriarumsinônimo PUBLIC:
SQL> conn tsql/tsql@xe2;
Connected.
SQL>
SQL> create public synonym funcionarios for tsql.emp;
323

## Página 338

12.3. Sinônimos CasadoCódigo
Synonym created.
SQL>
Vamosacessá-loatravésde ALUNO1e ALUNO2:
SQL> conn aluno1/aluno1@xe2;
Connected.
SQL>
SQL> select * from funcionarios;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
324

## Página 339

CasadoCódigo Capítulo12. Oracleavançado
10
03 0
20
30
20
10
14 rows selected.
SQL>
SQL> conn aluno2/aluno2@xe2;
Connected.
SQL>
SQL> select * from funcionarios;
select * from funcionarios
*
ERROR at line 1:
ORA-00942: table or view does not exist
SQL>
Acesso através do usuárioALUNO1: ok. Já o acesso através deALUNO2
não foi bem sucedido. Isso ocorreu porque apenas criamos o sinônimo para
atabelae,embora,sejaumsinônimo PUBLIC,elenãodáodireitodeacesso.
V amosvol taraousuárioTSQLedar GRANTpara ALUNO2.
SQL> conn tsql/tsql@xe2;
Connected.
SQL>
SQL> grant select on emp to aluno2;
Grant succeeded.
SQL>
Vamosaoteste,novamente:
SQL> conn aluno2/aluno2@xe2;
Connected.
325

## Página 340

12.3. Sinônimos CasadoCódigo
SQL>
SQL> select * from funcionarios;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
20
30
20
10
14 rows selected.
326

## Página 341

CasadoCódigo Capítulo12. Oracleavançado
SQL>
Notequenãofoinecessáriocriarumsinônimoespecíficoparaousuário
ALUNO2. Ele usou o sinônimo público criado. Lembre-se também que não
é o sinônimo que permite o acesso e, sim, oGRANT. Veja que este usuário
podeacessardiretamenteatabela,colocandoonomedodononafrente. Isso
graçasàconcessãocriada:
SQL> select * from tsql.emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
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
03 0
327

## Página 342

12.3. Sinônimos CasadoCódigo
20
30
20
10
14 rows selected.
SQL>
GRANTS são criados através do usuário dono do objeto, ou por meio
deumusuáriocomperfilde DBA,comoousuário SYSTEM.Jáossinôni-
mos podem ser criados diretamente no usuário que deseja ter o acesso.
InformaçõessobreSINÔNIMOS
• ALL_SYNONYMS
• USER_SYNONYMS
• DBA_SYNONYMS
Seumsinônimoforcriadoparaumusuárioquejápossuiumobjetocomo
mesmonome,égeradoumerroeosinônimonãoécriado. OOracleinforma
quejáexisteumobjetocriadocomestenomeparaousuárioemquestão.Isso
acontece tanto quando o usuário está criando o próprio sinônimo, quanto
paraoutrousuárioqueestejacriandoosinônimoparaele.
Seosinônimoestiversendocriadoemnívelpúblico(
PUBLIC),oOracle
permite a criação mesmo tendo usuários com objetos com o mesmo nome.
Nessecaso,ousuárioquepossuiumobjetocomomesmonomedosinônimo
criado,aotentaracessarutilizandoestenome,estaráacessandooseupróprio
objeto,enãoosinônimo. Seousuárionecessitaracessarosinônimo,teráque
indicarono medodo nodosinô nimonafr en tedomesmo .
328

## Página 343

CasadoCódigo Capítulo12. Oracleavançado
12.4 SEQUENCES
OobjetoT SEQUENCEéutilizadocomomeiodeincrementarvalores. AOra-
cle disponibiliza a criação deste objeto que você pode utilizar para diversos
fins,nãosomenteparaoincrementoemcolunasdetabelas(embora,sejasua
maiorutilidade),masparaqualquerfinalidadeemquesetenhaanecessidade
de gerar números sequenciais. Você pode utilizá-la para gerar numeração
para recibos de pagamento, notas fiscais, etiquetas ou códigos de produtos,
porexemplo. Éumrecursobastanteinteressante, poisvocênão precisacon-
trolarasequência,oOraclejáfazisto. Vocêcriaoobjetoeeleficaarmazenado
nobancodedadose,quandoquiserusá-lodentrodosprogramasoucoman-
dosSQL,sóéprecisochamá-lo.
Quandovocêconstróiuma
SEQUENCE,algunsparâmetrospodemserde-
finidos,comovalormínimoemáximoaqueesta SEQUENCEpodechegar,se
oincrementovaiserdeumoumaisnúmerosporvez,eseelapoderáreiniciar
aochegaraovalormáximo. Vejaalistadeparâmetros:
• INCREMENTBYn: especificaointervaloentrenúmerosdesequên-
c i a ,o n d enéu mi n t e i r o( s ee s s ac l á u s u l af o ro m i t i d a ,as e q u ê n c i aé
aumentadaemincrementosde1);
• START WITH n :especifica o primeiro número da sequência a ser
gerado(seessacláusulaforomitida,asequênciainiciarácom1);
• MAXVALUEn: especificaovalormáximoqueasequênciapodegerar;
• NOMAXVALUE: especifica o valor máximo 10`para uma sequência
crescentee-1paraumasequênciadecrescente(estaéaopçãopadrão);
• MINVALUEn: especificaovalordasequênciamínima;
• NOMINVALUE :especifica um valor mínimo iguala1p a r au m a
sequência crescente e -(10`) para uma sequência decrescente (esta é a
opçãopadrão);
• CYCLE / NOCYCLE :especifica se a sequência continuará gerando
valores depois de atingir o valor máximo ou mínimo (
NOCYCLE éa
opçãopadrão);
329

## Página 344

12.4. SEQUENCES CasadoCódigo
• CACHEn/NOCACHE: especifica quantos valores são pré-alocados
pelo Oracle Server e mantidos na memória (por padrão, o Oracle Ser-
verarmazena20valoresemcache).
Segueumexemplodecriaçãoeusode SEQUENCE:
SQL> create sequence emp_s
minvalue 1
maxvalue 1000
increment by 1
nocycle
noorder
nocache
/
Sequence created.
SQL>
Paraincrementarasequência:
SQL> select emp_s.nextval from dual;
NEXTVAL
---------
1
SQL>
Paramostrarovalorcorrente:
SQL> select emp_s.currval from dual;
CURRVAL
---------
1
SQL>
330

## Página 345

CasadoCódigo Capítulo12. Oracleavançado
CURRVALsóépermitidodepoisquepelomenosum NEXTVALtenha
sidoexecutado. Casocontrário,oOraclegeraumerro.
Uso no INSERT:
SQL> insert into emp values(emp_s.nextval,’JOCA’,’MECANICO’,
NULL,SYSDATE,5000,0,10);
1 row created.
SQL>
SQL> select * from emp;
EMPNO ENAME JOB MGR HIREDATE SAL
--------- ---------- --------- --------- --------- ---------
7369 SMITH CLERK 7902 17- DEC-80 800
7499 ALLEN SALESMAN 7698 20-FEB-81 1600
7521 WARD SALESMAN 7698 22-FEB-81 1250
7566 JONES MANAGER 7839 02-APR-81 3272.5
7654 MARTIN SALESMAN 7698 28-SEP-81 1250
7698 BLAKE MANAGER 7839 01-MAY-81 2850
7782 CLARK MANAGER 7839 09-JUN-81 2450
7788 SCOTT ANALYST 7566 09- DEC-82 3000
7839 KING PRESIDENT 17-NOV-81 5000
7844 TURNER VENDEDOR 7698 08-SEP-81 1500
7876 ADAMS CLERK 7788 12-JAN-83 1100
7900 JAMES CLERK 7698 03- DEC-81 950
7902 FORD ANALYST 7566 03- DEC-81 3000
7934 MILLER CLERK 7782 23-JAN-82 1300
555 EDUARDO ANALISTA 01-JAN-11 5000
2 JOCA MECANICO 21-APR-11 5000
COMM DEPTNO
--------- ---------
20
300 30
500 30
331

## Página 346

12.4. SEQUENCES CasadoCódigo
20
1400 30
30
10
20
10
03 0
20
30
20
10
01 0
16 rows selected.
SQL>
Depoisquea SEQUENCEgeraumnúmero,elanãopassamaispelomesmo
valor,amenosqueelareinicie. Tambémnãoháummeiodevoltarovalorge-
rado. Oquepodeserfeitoéadiantara SEQUENCE.ComaajudadoPL/SQL,
vocêpodecriarumscriptparaadiantá-la. Contudo,elaprecisaestarconfigu-
radaparareiniciaraochegaraofim. Nessecaso,suacontagemseráreiniciada
e,destaforma,conseguiremosdeixá-lanasequênciaanterioràquequeremos.
Vejaosexemplos:
Exemplo 1 (com base na SEQUENCE EMP_S criada anterior-
mente)
Execute este SELECT até o valor corrente ficar maior que o valor que
desejamos retornar. Para este caso, vamos deixar a sequência em 21. Nosso
ob jetivoévol tarparasequência5.
SQL> select emp_s.nextval from dual;
NEXTVAL
---------
21
SQL>
332

## Página 347

CasadoCódigo Capítulo12. Oracleavançado
Altere o INCREMENT BY da SEQUENCE com o seguinte valor:
-(NEXTVAL - 5) ,ouseja,-16.
SQL> alter sequence emp_s increment by -16;
Sequence altered.
SQL>
Executeum NEXTVALparaa SEQUENCE:
SQL> select emp_s.nextval from dual;
NEXTVAL
---------
5
SQL>
Agora,volteo INCREMENT BY paraovalororiginal:
SQL> alter sequence emp_s increment by 1;
Sequence altered.
SQL>
Verifiqueovalorcorrenteda SEQUENCE:
SQL> select emp_s.currval from dual;
CURRVAL
---------
5
SQL>
333

## Página 348

12.4. SEQUENCES CasadoCódigo
Exemplo 2 (com base na SEQUENCE EMP_S criada anterior-
mente)
Execute este SELECT até o valor corrente ficar maior que o valor que
desejamosretornar. Nossoobjetivoévoltarparasequência5.
SQL> select emp_s.nextval from dual;
NEXTVAL
---------
7
SQL>
V amosal teraraSEQUENCEpara CYCLE.
SQL> alter sequence emp_s cycle;
Sequence altered.
SQL>
Executamos o PL/SQL a seguir atribuindo para a variável
WPOS_DESEJADAovalorinicialquedesejamosparaa SEQUENCE:
SQL> declare
wnext_val number := 0;
wcurr_val number := 0;
wmax_value number := 0;
wlast_number number := 0;
wincrement_by number := 0;
--
wpos_desejada number := 5;
begin
--
select max_value + wpos_desejada
,last_number
,increment_by
into wmax_value
,wlast_number
,wincrement_by
334

## Página 349

CasadoCódigo Capítulo12. Oracleavançado
from all_sequences
where sequence_name = ’EMP_S’;
--
dbms_output.put_line(wmax_value);
dbms_output.put_line(wlast_number);
--
loop
wlast_number := wlast_number + wincrement_by;
--
select emp_s.nextval into wnext_val from dual;
--
exit when wlast_number = wmax_value + 1;
--
end loop;
--
select emp_s.currval into wcurr_val from dual;
--
dbms_output.put_line(wcurr_val);
--
end;
/
PL/SQL procedure successfully completed.
SQL>
Agora,vamosalterara SEQUENCEpara NOCYCLE,voltandoàconfigura-
çãooriginal:
SQL> alter sequence emp_snocycle;
Sequence altered.
SQL>
Vamosveroresultado:
SQL> select emp_s.currval from dual;
CURRVAL
335

## Página 350

12.4. SEQUENCES CasadoCódigo
---------
5
SQL>
Excluindouma SEQUENCE:
SQL> drop sequence emp_s;
Sequence dropped.
SQL>
InformaçõessobreSEQUENCES
• ALL_SEQUENCES
• USER_SEQUENCES
• DBA_SEQUENCES
CachedevaloresdaSEQUENCE
Ao habilitar o armazenamento em cache para os valores de uma
SEQUENCE, você está tornando mais ágil o acesso a estes valores. O que se
deveteremmentequandoseestátrabalhandocomarmazenamentoemcache
équepodemocorrerintervalosnosvaloresda SEQUENCEnocasodeocorrer
umrollback,algumafalhanosistemaouuma SEQUENCEestiversendousada
emoutratabela.
336

## Página 351

Capítulo13

## Página 352

CasadoCódigo
ANEXOS
338

## Página 353

CasadoCódigo Capítulo13. ANEXOS
Fig.13.2
339

## Página 355

Capítulo14
REFERÊNCIAS
BIBLIOGRÁFICAS
DATE,C.J.IntroduçãoaSistemasdeBancosdeDados. RiodeJaneiro: Cam-
pus,1991.
FERNANDES, Lúcia. Oracle 9i Para Desenvolvedores Curso Completo.
RiodeJaneiro: AxcelBooks,2002.
GENNICK, Jonathan, LUERS, Tom. Aprenda em 21 dias PL/SQL. 2. ed.
RiodeJaneiro: Campus,2000.
HEUSER, Carlos Alberto. Projeto de Banco de Dados. 4. ed. Porto Ale-
gre: SagraLuzzatto,2001.
LIMA, Adilson da Silva. Erwin 4.0 Modelagem de Dados. 2. ed. São
Paulo: Érica,2002.
LONEY,Kevinetal. Oracle9i: OManualdoDBA.RiodeJaneiro: Cam-

## Página 356

CasadoCódigo
pus,2002.
MOLINARI,Leonardo. BTOOtimizaçãodaTecnologiadeNegócio. São
Paulo: Érica,2003.
ORACLE Database Online Documentation 10g Release 1 (10.1). Dispo-
nívelem:<http://www.oracle.com/pls/db10g/portal.portal_demo3?selected=
1>. Acessoem: 16mar. 2011.
OracleDatabaseNewFeaturesGuide11g,Release1(11.1)
OracleDatabaseReference11g,Release1(11.1)
OracleDatabaseSQLLanguageReference11g,Release1(11.1)
OracleDatabaseConcepts11g,Release1(11.1)
OracleDatabaseSQLDeveloperUser’sGuide,Release1.2
342