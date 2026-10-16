---json
{
  "id": "introdu__o___programa__o_em_c_os_primeiros_passos_de_um_desenvolvedor",
  "title": "Introdução à programação em C Os primeiros passos de um desenvolvedor",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `Introdução à programação em C Os primeiros passos de um desenvolvedor.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "desenvolvedor",
    "introdu",
    "linguagens",
    "passos",
    "php",
    "primeiros",
    "programa"
  ],
  "perguntas_tipo": [
    "Como utilizar Introdução à programação em C Os primeiros passos de um desenvolvedor?",
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

# Introdução à programação em C Os primeiros passos de um desenvolvedor

> **Arquivo Original:** `Introdução à programação em C Os primeiros passos de um desenvolvedor.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

CasadoCódigo
Quemsoueu?
MeunomeéMaurícioAniche,etrabalhocomdesenvolvimentodesoftware
pelosúltimos10anos.Emboapartedessetempo,atueicomoconsultorpara
diferentesempresasdomercadobrasileiroeinternacional. Comcerteza,as
linguagensmaisutilizadaspormimaolongodaminhacarreiraforamJava,
C#eC.
Comosemprepuleideprojetoemprojeto(e,porconsequência,detec-
nologiaemtecnologia),nuncafuiafundoemnenhumadelas.Pelocontrário,
semprefoqueiementenderprincípiosquepudessemserlevadosdeumapara
outra,paraque,nofim,ocódigosaíssecomqualidade,independentedatec-
nologia.
Naacademia,formei-meemCiênciadaComputaç ãopelaUniversidade
PresbiterianaMackenzie,em2007.Emseguida,fizmestradoemCiênciada
ComputaçãopelaUniversidadedeSãoPaulo,ondedefendiminhadissertaç ão
em2012.Atualmente,soualunodedoutoradopelomesmoinstituto.
Prefirodizerquesouumapessoaquetemumpénaacademiaeoutro
naindústria. Gostodosdoismundos. Atualmente,trabalhopelaCaelum,
comoconsultoreinstrutor.TambémsouresponsávelpeloscursosdoAlura,
oportaldeensinoàdistânciadaCaelum.
Ensinar,semdúvida,éoquemaisgostodefazer.
i

## Página 4

CasadoCódigo
Agradecimentos
Agradecerésempreapartemaisdifícil.Emprimeirolugar,agrade çoameus
paisporsempreapoiaremtodaequalqueriniciativaquetenho.Veroquanto
elesficamorgulhososacadapequenaconquistaemminhacarreiramefaz
querersempremaisemais.
Agradeçotambémaomeuamigoecolegadetrabalho,GuilhermeSil-
veira,pelasincontáveisdiscussõesquetivemosaolongodaescritadestelivro.
AversãoRubyfoiescritaporele,esegueasmesmasideiasdeste. Criamos
juntostodaalinhadeensinodesseslivros.
Porfim,atodosmeusamigos,quemeaguentamfalandootempotodo
sobreoquantoédifíciletrabalhosoescreverumlivro.
Forteabraçoatodos!
iii

## Página 6

CasadoCódigo Sumário
Sumário
1 Introdução 1
1.1 Aquemsedestinaestelivro? . . . . . . . . . . . . . . . . . . . 3
1.2 Comodevolê-lo? . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 Jogodeadivinhaç ão 5
2.1 Comoeleficará? . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Éhoradecome çar! . . . . . . . . . . . . . . . . . . . . . . . . 8
3 Variáveis 9
3.1 Nossoprimeiroprograma . . . . . . . . . . . . . . . . . . . . 10
3.2 Declarandovariáveis . . . . . . . . . . . . . . . . . . . . . . . 14
3.3 Lendodoteclado . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4 Entendendoocompilador . . . . . . . . . . . . . . . . . . . . 17
3.5 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4 Controledefluxocomifsefors 21
4.1 Escopodevariáveis . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2 Loopsefor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.3 Parandoloops . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.4 Defines,constantesenúmerosmágicos . . . . . . . . . . . . . 33
4.5 Oelseif . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.6 Breakecontinue . . . . . . . . . . . . . . . . . . . . . . . . . . 36
4.7 Oloopwhile . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
4.8 Loopsinfinitos . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
4.9 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
v

## Página 7

Sumário CasadoCódigo
5 Tiposdedadoseoperaç õesmatemáticas 45
5.1 Operaçõesmatemáticas . . . . . . . . . . . . . . . . . . . . . . 46
5.2 Outrostiposnuméricos . . . . . . . . . . . . . . . . . . . . . . 48
5.3 Conversõesecasting . . . . . . . . . . . . . . . . . . . . . . . 51
5.4 Fun çõesmatemáticas . . . . . . . . . . . . . . . . . . . . . . . 53
5.5 Númerosrandômicos . . . . . . . . . . . . . . . . . . . . . . . 54
5.6 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
6 Finalizandoojogo 59
6.1 Switchecase . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
6.2 Novamenteusandovariáveiseescopos . . . . . . . . . . . . . 62
6.3 Embelezandoojogo . . . . . . . . . . . . . . . . . . . . . . . . 65
6.4 Acabamosoprimeirojogo! . . . . . . . . . . . . . . . . . . . . 67
6.5 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
7 Exercícios 69
7.1 Melhorandoojogodeadivinhaç ão . . . . . . . . . . . . . . . 69
7.2 Outrosdesafios . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
8 Jogodeforca 71
8.1 Comoeleficará? . . . . . . . . . . . . . . . . . . . . . . . . . . 72
8.2 Éhoradecome çar! . . . . . . . . . . . . . . . . . . . . . . . . 75
9 Arrays 77
9.1 Stringsearraydechars . . . . . . . . . . . . . . . . . . . . . . 79
9.2 Varrendooarray . . . . . . . . . . . . . . . . . . . . . . . . . . 81
9.3 Laçosencadeados . . . . . . . . . . . . . . . . . . . . . . . . . 84
9.4 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
10 Númerosbinários 89
10.1 Binárioeletras. . . . . . . . . . . . . . . . . . . . . . . . . . . 91
10.2 Bits:8,16,32,64 . . . . . . . . . . . . . . . . . . . . . . . . . . 91
10.3 Bitsenúmeroscompontoflutuante . . . . . . . . . . . . . . . 92
10.4 Hexadecimal. . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
10.5 Bitseimagens . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
10.6 Resumindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
vi

## Página 8

CasadoCódigo Sumário
11 Funçõeseponteiros 97
11.1 Escrevendofunções . . . . . . . . . . . . . . . . . . . . . . . . 98
11.2 Maisfunções . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
11.3 Passandoparâmetrosparafun ções . . . . . . . . . . . . . . . 102
11.4 Ponteiros. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
11.5 Passagemporreferência . . . . . . . . . . . . . . . . . . . . . 108
11.6 Arrayseponteiros . . . . . . . . . . . . . . . . . . . . . . . . . 112
11.7 Funçõescomretorno . . . . . . . . . . . . . . . . . . . . . . . 115
11.8 Extraindomaisfun ções . . . . . . . . . . . . . . . . . . . . . . 118
11.9 Variáveisglobais. . . . . . . . . . . . . . . . . . . . . . . . . . 120
11.10 Resumindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
12 Entradaesaída(I/O) 127
12.1 Headerfiles. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
12.2 Lendoarquivos. . . . . . . . . . . . . . . . . . . . . . . . . . . 134
12.3 Escrevendonoarquivo . . . . . . . . . . . . . . . . . . . . . . 138
12.4 MaissobreI/O . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
12.5 Resumindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
13 Finalizandoojogo 147
13.1 Evitandorepetiçãodecódigo . . . . . . . . . . . . . . . . . . . 147
13.2 Extraindofunções . . . . . . . . . . . . . . . . . . . . . . . . . 148
13.3 Ifsternários. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
13.4 Últimosdetalhes . . . . . . . . . . . . . . . . . . . . . . . . . . 154
13.5 Resumindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
14 Exercícios 157
14.1 Jogodeadivinhação . . . . . . . . . . . . . . . . . . . . . . . . 157
14.2 Jogodeforca . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
14.3 Outrosdesafios. . . . . . . . . . . . . . . . . . . . . . . . . . . 158
15 JogoFoge-foge 161
15.1 Comonossojogovaificar? . . . . . . . . . . . . . . . . . . . . 162
15.2 Éhoradecome çar! . . . . . . . . . . . . . . . . . . . . . . . . 163
vii

## Página 9

Sumário CasadoCódigo
16 Matrizes 165
16.1 Ponteirosdeponteiros . . . . . . . . . . . . . . . . . . . . . . 169
16.2 Alocaçãodinâmicadememória . . . . . . . . . . . . . . . . . 171
16.3 Resumindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
17 Structs 179
17.1 Definindoumastruct . . . . . . . . . . . . . . . . . . . . . . . 182
17.2 Ponteirosparastructs . . . . . . . . . . . . . . . . . . . . . . . 185
17.3 Introduçãoàanálisedealgoritmos . . . . . . . . . . . . . . . 192
17.4 Resumindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
18 Programandocomoumprofissional 199
18.1 Novamente,responsabilidades. . . . . . . . . . . . . . . . . . 203
18.2 Novamente,constantes . . . . . . . . . . . . . . . . . . . . . . 207
18.3 Usandoestruturasauxiliares . . . . . . . . . . . . . . . . . . . 208
18.4 Umpoucodeinteligênciaartificial . . . . . . . . . . . . . . . 213
18.5 Acoplamento,encapsulamentoeassinaturasdefun ções . . . 216
18.6 Resumindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
19 Recursividade 223
19.1 Entendendorecursão . . . . . . . . . . . . . . . . . . . . . . . 227
19.2 Complicandooalgoritmorecursivo . . . . . . . . . . . . . . . 232
19.3 Resumindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
20 Outrasdiretivasdecompilação 235
20.1 IfdefseIfndefs . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
20.2 Resumindo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
21 Exercícios 245
21.1 JogoFoge-foge . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
21.2 Outrosdesafios. . . . . . . . . . . . . . . . . . . . . . . . . . . 246
22 Oquefazeragora? 247
viii

## Página 10

CasadoCódigo Sumário
23 ApêndiceA:instalandoocompilador 249
24 ApêndiceB:códigos 251
24.1 Jogodaadivinhação . . . . . . . . . . . . . . . . . . . . . . . . 251
24.2 Jogodeforca . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
24.3 Foge-foge. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
ix

## Página 12

Capítulo1
Introdução
Vocêjáprogramoualgumaveznavida?Poisentão,prepare-se:suavidavai
mudar. Ensinaramáquinaafazeroquequerqueelafaç aéextremamente
divertido.E,porsorte,tambémútil.
Porém,ocaminhoélongo.Vocêprecisaráaprenderapensarcomouma
máquina,quenãosabeenãofaznadaquevocênãoamandarfazer,easaber
expressar-seemumalinguagemqueelaentende.
Aqui,optamospelalinguagemC.Céumalinguagembastantepopular,
porváriosmotivosdiferentes. Elaéusadahámuitotempo,porprograma-
doresdomundointeiro,nosmaisdiferentesprojetos. Éextremamentepo-
derosa: sistemasoperacionaissãofeitosemC,porexemplo;esimples: sua
sintaxeébemfácildeserassimilada.
Cétambémumaótimalinguagemparaaquelesquequeremaprender
programação,poiselanosdádiferentesníveisdeabstraç ão. Podemoses-

## Página 13

CasadoCódigo
quecerqueamemóriadocomputadorexiste,oumanipulá-ladiretamente,
sequisermos.
Vocêprovavelmentejápassouporoutroslivrosdeprogramação.Elesnão
meagradamporalgunsmotivos. Primeiro,porqueamaioriadelesensina
oalunoaprogramarusandoexemplosmatemáticos. Cáentrenós,amate-
máticaélegal,masnãoqueremosvê-laotempointeiro. Existemexemplos
melhores,comcerteza.Outrosfazemprojetosextremamentesimples,como
umapequenacalculadoraouumapequenaagenda.Masquemquer,aofinal
deumlivroenorme,terumasimplesagendafeita?
Minhapropostaparaestelivroéensinarvocêaprogramarpormeiode
jogos.Escreverumjogoéextremamentedesafiador.Elessãocheiosdelógicas
complicadasecasosexcepcionais. Umdosjogos,porexemplo,ésimilarao
Pac-Man,quevocêprovavelmentejogouquandocrian ça.Fazeroheróiandar
porummapa,fugindodosfantasmas,matandoousendomortosporeles,e
comendopílulasdeenergiaécomcertezamuitomaisdifícildeserfeitodo
queumasimplesagenda.
Mascalma,nãocome çaremoscomoPac-Man.Aolongodestelivro,de-
senvolveremos3grandesjogos:um jogodeadivinhaç ão,noqualocompu-
tadorpensaráemumnúmeroevocêchutaráatéacertar. Eledarádicasse
onúmeroémaioroumenordoqualvocêchutoue,claro,vocêterápoucas
chancesparaadivinhar. Percebaque,apesardesimples,temosmuitospro-
blemascomputacionaispararesolver:condicionais,loops,númerosrandô-
micos,eassimpordiante.
Depois,iremosparaum jogodeforca. Ocomputadorescolheráuma
palavradeumalista,edesenharáaforca. Ojogador,então,chutaletraseo
computadorvaimostrandoosacertos,oudesenhandoobonecoacadaerro.
Osdesafiosaquitambémsãograndes: arrays,leituraeescritadearquivos,
funçõesseparadasparaquehajareúsoentreelas,ponteirosdememória,e
maisloopsecondicionais.
Porfim,o Foge-foge,similaraoPac-Man. Comojáexplicado,oherói
fogedosfantasmas,quetentampegá-lo. Aqui,aprendemosmaissobrema-
trizes/arraysbidimensionais,criaçãodeestruturasetipospróprios,efun ções
recursivasediretivasdecompilaç ão.
Essesjogosnosdarãomuitasoportunidadesparadiscussõesemuitocó-
2

## Página 14

CasadoCódigo Capítulo1. Introdução
digo. Essescódigos,aliás,sãofeitospassoapasso. Programadoreserram,
mudamdeideiaeosmelhoramaospoucos,conformevãopassandopelos
desafiosdoprogramaquequeremfazer. Aquivocêveráqueissoacontece.
Nósmudaremosdeideiamuitasvezessobreocódigoquetemos.Descobri-
remosquealgoquefizemosnopassadonãoeranaverdadetãobomassim,e
melhoraremos.Éassimqueprogramadoresaprendemdeverdade:vendoum
códigocrescerdozero.
Enfim,aofinaldaleitura,vocêentenderátudooqueprecisaparacome çar
acriarprogramasdecomputador.
Ah,esquecidedoisdetalhesimportantes!
Primeiro:jogossãolegais!;-)
Segundo:Sevocêtiverqualquerdúvidadurantealeitura,venhaconversar
comigonalistadediscussãodolivro,disponívelem https://groups.google.
com/forum/#!forum/introducao-a-programacao-em-c. Vamoslábaterum
paposobreprogramação!
1.1 Aquem se destina este livro?
Estelivrodestina-seàquelesquequeremaprenderaprogramar.Nãohápré-
requisitos.Vocênãoprecisaconheceralgumalinguagemdeprogramaç ãoou
mesmoterumalógicadeprogramaç ãobemafiada.
Estedeveseroseuprimeirolivrodeprogramaç ão.Aquelequevocêguar-
darácomcarinho.
1.2 Como devo lê-lo?
Idealmente,vocêdeveleroscapítulosnasequência.Aolongodeles,vamos
evoluindocadaumdosjogosemisturandoteoriacomaprática. Pularum
capítulopodeserproblemático,eoseucódigopodenãofuncionar,sevocê
perderalgo.
Entretanto,aofinaldecadacapítulo,damosumlinkparaocódigocom-
pletoatéaquelemomento.Sevocêestiverperdidoouacharquepodepular
aqueladiscussão,nadaoimpededebaixarocódigoeiradiante.Masgaranto
avocêquehásurpresasediscussõesinteressantesemtodoseles.
3

## Página 16

Capítulo2
Jogodeadivinhação
Aolongodospróximoscapítulos,desenvolveremosumjogodeadivinhaç ão.
Ocomputadorpensaráemumnúmero,evocê,jogador,precisaráadivinhá-lo.

## Página 17

2.1. Comoeleficará? CasadoCódigo
Acadaerro,amáquinalhediráseonúmerochutadofoimaioroumenordo
queopensado.Vocêtambémpoderáescolheroníveldedificuldadedojogo,
eissolhedarámaisoumenosoportunidadesdechutarumnúmero.Aofinal,
sevocêganhar,ocomputadorlhediráquantospontosvocêfez,baseando-se
emquãobonseramseuschutes.
Ojogoparecesimples,maselelheajudaráaaprenderdiversosconceitos
importantessobreprogramação,como:
• Lerdotecladoeescrevernatela. Afinal,precisamosinteragircomo
usuário;
• Armazenarvaloresnamemóriaemanipulá-los;
• Executaroperaçõesmatemáticasemcimadessasvariáveis;
• Entenderosdiferentestiposdevariáveis,equalusarparaguardarnú-
merosinteirosenúmeroscompontoflutuante;
• Tomardecisõesnoprograma,baseando-senaentradadousuário;
• Usarloopsparaexecutaromesmotrechodecódigorepetidasvezes.
2.1 Como ele ficará?
Vejasócomonossojogoficaráaofinaldestescapítulos.Aocome çar,elepe-
diráparaqueousuárioescolhaumníveldedificuldade:
.
P /_\ P
/_\_|_|_/_\
n_n | ||. .|| | n_n Bem-vindo ao
|_|_|nnnn nnnn|_|_| Jogo de Adivinhação!
|" " | |_| |" " |
|_____| ' _ ' |_____|
\__|_|__/
6

## Página 18

CasadoCódigo Capítulo2. Jogodeadivinhação
Qual o nível de dificuldade?
(1) Fácil (2) Médio (3) Difícil
Escolha:
Depois,elecome çaráapedirpalpitesparaousuário.Enquantoousuário
errar,elecontinuarápedindo.
-> Tentativa 1 de 6
Chute um número: 5
Seu chute foi menor do que o número secreto!
-> Tentativa 2 de 6
Chute um número: 6
Seu chute foi menor do que o número secreto!
-> Tentativa 3 de 6
Chute um número: 7
Seu chute foi menor do que o número secreto!
-> Tentativa 4 de 6
Chute um número: 8
Seu chute foi menor do que o número secreto!
-> Tentativa 5 de 6
Chute um número: 9
Seu chute foi menor do que o número secreto!
-> Tentativa 6 de 6
Chute um número: 10
Seu chute foi menor do que o número secreto!
Sevocêesgotartodassuaschances,elelheavisaráquevocêperdeu:
7

## Página 19

2.2. Éhoradecome çar! CasadoCódigo
.
\|/ ____ \|/
@~/ ,. \~@
/_( \__/ )_\
\__U_/
Você perdeu! Tente novamente!
Sevocêacertar,vocêsaberáquantospontosfez:
.
OOOOOOOOOOO
OOOOOOOOOOOOOOOOOOO
OOOOOO OOOOOOOOO OOOOOO
OOOOOO OOOOO OOOOOO
OOOOOOOO # OOOOO # OOOOOOOO
OOOOOOOOOO OOOOOOO OOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOO OOOOOOOOOOOOOOOOOOOOOOOOO OOOO
OOOO OOOOOOOOOOOOOOOOOOOOOOO OOOO
OOOO OOOOOOOOOOOOOOOOOOOO OOOO
OOOOO OOOOOOOOOOOOOOO OOOO
OOOOOO OOOOOOOOO OOOOOO
OOOOOO OOOOOO
OOOOOOOOOOOO
Parabéns! Você acertou!
Você fez 985.00 pontos. Até a próxima!
2.2 É hora de começar!
Estáprontoparadesenvolveressejogo? Mãosàobra!
8

## Página 20

Capítulo3
Variáveis
Estamosprontosparacome çarnossojogodeadivinhaç ão.Masantesdeen-
trarmosdecabe çanele,precisamosescolherumalinguagemdeprogramaç ão.
Naverdade,vocêjásabequalé,poiselaestánacapadestelivro.Tudooque
escrevermosaquiseránalinguagemC.Éinteressantequeela,apesardeser
umalinguagemantiga,aindaébastanteutilizadaemmuitoslugaresimpor-
tantesnonossodiaadia. Sistemasoperacionais,porexemplo,sãoescritos
emC.
Porserumalinguagempopular,muitasdasmaismodernas,comoocaso
doJavaedoC#,forambaseadasnela. Ouseja,come çarporCéumaboa
escolha!Nestapartedolivro,nósestudaremosseusconceitosbásicose,com
eles,implementaremosnossoprimeirojogo:ojogodaadivinhaç ão.

## Página 21

3.1. Nossoprimeiroprograma CasadoCódigo
3.1 Nosso primeiro programa
TodoprogramaemCcome çaporumarquivoquecontémtodoocódigo-
fontedonossoprograma.Essearquivopodeserescritoemqualquereditor
detextossimples,comooBlocodeNotas. Éfácilsaberqueumarquivoé
umprogramaemC,simplesmenteporqueeleterminacomaextensão .c.O
primeiropassoécriarumarquivoesalvá-locomo adivinhacao.c(adivi-
nhacaoéonomedojogo). Geralmente,damosumnomesignificativopara
essearquivo,afinalquandoestivermosdesenvolvendoumsistemamaior,te-
remosmuitosdeles. Tambémevitequalquertipodeacentoouespaçosem
seunome.
Editores de código
Existemmuitoseditoresdecódigoparaprogramadores. Umadas
IDEs(nomequedamosaeditoresdetextofocadosemcódigo)maispo-
pulareséoEclipse. EleémuitousadoporprogramadoresJava. Entre-
tanto,nessemomentodoseuaprendizado,sugiroavocêusarumaIDE
maissimples,queoajudemenoseofaç apensarmaisnocódigoque
estáescrevendo.RecomendoeditorescomooSublimeText,Notepad++,
Ultraedit,ouqualqueroutroquesomentedeixeocódigocolorido,para
facilitaravisualizaç ão.
Nessearquivo,vamoscome çarjácomamensagemdeboas-vindasdo
nossojogo.Aorodar,eledeverádizer“Bem-vindoaoJogodeAdivinhaç ão”.
Todotextodeveserescritoentreaspas;assimalinguagemCsabequesetrata
deumtextoqualquerenãodealgum“comandoespecial”dalinguagem.No
arquivo,então:
"Bem-vindo ao Jogo de Adivinhação"
Porém,issonãoésuficiente.Precisamosdizeraoprogramaparaqueim-
primaotextonasaídapadrão,ouseja,nomonitor.Paraisso,usaremosnossa
primeirafunção.Maisadiante,veremoscommuitomaisdetalhes,masnesse
momento,umafun çãoéumconjuntodecódigoquefazumatarefabemdefi-
10

## Página 22

CasadoCódigo Capítulo3. Variáveis
nida.AlinguagemC,vemcomafun ção printfque,comoopróprionome
diz,imprime.Paraimprimirmosalgonatela,usandoo printf,fazemos:
printf("Bem-vindo ao Jogo de Adivinhação")
Vejaqueabrimosparêntesesepassamosonossotextoentreaspas. Po-
demoschamaressafun çãoquantasvezesquisermos,comotextoquequi-
sermos,eelesempreseráimpressonatela.Vejasónocódigoaseguir,onde
utilizamoso printfváriasvezesseguidas,paraimprimirumamensagem
maisamigávelebonitaparaousuáriofinal.
Reparetambémnopontoevírgula! TodalinhaemCterminacomponto
evírgula.Pareceestranho,masvocêlogoseacostumará!
printf("************************************");
printf("* Bem-vindo ao Jogo de Adivinhação *");
printf("************************************");
Estamosquaseprontosparaexecutarnossoprograma. Essemontede
printfs não pode ficar jogado dentro do nosso arquivo C. Precisamos
colocá-losdentroda“funçãoprincipal”doprograma. Todoprogramaem
Ctemumafun çãoprincipal.Éelaqueéexecutadaquandovocêrodaoseu
arquivo .exe, .out,ouqualquerquesejaaextensãoexecutáveldoseusis-
temaoperacional.Essafun çãochama-se main.
PrecisamostambémdizeraoCqueestamosusandoafun ção printf.
Afinal,elaprecisouserescritaemalgumlugar,certo? Paraisso,escrevere-
mosnocome çononossoarquivo, #include <stdio.h>.Éfácilentender
stdio:vemde standard I/O,ouseja,entradaesaídapadrão.Énessearquivo
queficamtodasasfun çõesdeentrada(lerdoteclado,porexemplo),esaída
(escrevernomonitor).Vocêveráquetodosnossosprogramasincluirãoesse
arquivo.
Nessemomento,nãosepreocupecomtodoocódigoqueaparecerá.Você
vaientendercadapartedelemaisàfrente. Porenquanto,entendaque,ao
rodaroprograma,tudoqueestarádentrodesse mainseráexecutado.Repare
tambémnaschaves{}.Elasdelimitamo“corpo”dessafunção.Ouseja,tudo
queestádentrodaschaves,estádentrodessafun ção.
11

## Página 23

3.1. Nossoprimeiroprograma CasadoCódigo
# include <stdio.h>
int main() {
printf("************************************");
printf("* Bem-vindo ao Jogo de Adivinhação *");
printf("************************************");
}
Programafeito. Precisamosagoraexecutá-lo. Entretanto,antesdisso,
queremostransformá-loemcódigodemáquina.Oprograma,escritoemC,
éótimoparaoutrossereshumanoslerememodificarem,maspéssimopara
amáquina.Precisamostransformá-loemcódigoqueamáquinaentende,ou
seja,emcódigodemáquina.Éparaissoqueserveum compilador.Elepega
oarquivoqueestáescritonasualinguagemdeprogramaç ãoeotransforma
emcódigodemáquina(quenósnãoconseguimosentender).
OcompiladormaisconhecidodalinguagemCéoGCC.Sevocêestá
usandoLinuxouMac,elejáveminstalado.SevocêestánoWindows,preci-
saráinstalá-lo.Vejaoapêndicedolivrosetiverdúvidasdecomofazerisso.
Comocompiladoremmãos,vamospedirparaelegerarumexecutável.Para
isso,vamosinvocá-lo,usandooterminal,passandoparaeleonomedoar-
quivo .Ceonomedoexecutávelquequeremosgerar(logoapóso -o).
Acostume-secomoterminal(ou Command Prompt),poisousaremos
bastanteaolongodolivro.Entrenodiretórioemquevocêsalvouocódigo-
fonte(sevocêaindanãosabecomousaroterminal,váaonossoapêndice),e
executeocomandoaseguir:
NoWindows:
gcc adivinhacao.c -o adivinhacao.exe
NoLinuxouMac(aúnicadiferen çaéquetiramoso .exedonomedo
arquivo):
gcc adivinhacao.c -o adivinhacao
Vamos agora executar o programa. No Linux ou Mac, basta fazer
./adivinhacao.NoWindows,bastadigitar adivinhacao.
12

## Página 24

CasadoCódigo Capítulo3. Variáveis
Comemore!Nossoprimeiroprogramaexecutouenosimprimiu“Bem-
vindoaoJogodeAdivinhaç ão”.
Aindanãoéoquequeremos,afinaleleimprimiutudonamesmalinha.
O printfnãoquebralinhasevocênãomandar. Vejaqueamáquinanão
faznadaquevocênãoqueiraexplicitamente! Paraquenossoprogramadê
enterentreumalinhaeoutra,bastaacrescentarmosum \naofinaldecada
printf.O \néocódigopara enteremnossosprogramasemC.Vejacomo
nossocódigofica:
# include <stdio.h>
int main() {
printf("************************************\n");
printf("* Bem-vindo ao Jogo de Adivinhação *\n");
printf("************************************\n");
}
Lembre-sedeque,acadamudan çafeitanocódigo-fonte,vocêdevecom-
pilarnovamenteoprograma. Serodarmos,elenosimprimirádamaneira
comoqueremos.Parabéns,temosnossoprimeiroprogramarodando.
************************************
* Bem-vindo ao Jogo de Adivinhação *
************************************
13

## Página 25

3.2. Declarandovariáveis CasadoCódigo
Comentários
Podemosinserircomentáriosemnossocódigo;ouseja,trechosde
textoemportuguês,queserãoignoradospelocompilador.Elesnosaju-
damadescrevermelhoroquequeremosfazer.Parafazerumcomentá-
rio,bastacome çaralinhacom //. Tudooqueviernasequênciaserá
completamenteignoradopelocompilador.Porexemplo:
// comentário, isso não faz nada
printf("Oi" );
// outro comentário, também não faz nada
Sevocênãoestiverentendendoalgumapartedocódigo,coloqueum
comentário.Mastambémnãoabusedeles:umcódigocommuitosfica
difícildeserlido.
3.2 Declarando v ariáveis
Nossopróximopassoagoraéterumnúmerosecreto,ecome çarapedirparao
usuáriochutarqualé.Começaremosguardandoessenúmeroemalgumlugar.
Algomuitocomumemnossosprogramasseráguardardados/informações,
paraquepossamosmanipulá-lasmaisparafrente.Essenúmerosecreto,por
exemplo,seráalgoqueusaremosaolongodetodonossoprogramae,porisso,
fazsentidoguardá-loemalgumlugarfácil.
Chamamosesseslugaresde variáveis.Paradeclararmosumavariávelem
C,precisamosdeduascoisas: deumnomequalquer,poiséassimquenos
referenciaremosaeladepois;esaberotipodedadoqueelaguardará.Nossos
programasdiferenciamtiposdedados.Ouseja,númerosinteirossãonúme-
rosinteiros,númeroscomvírgulasãonúmeroscomvírgula,etextos(que
apartirdeagorachamareide string)sãostrings. Apartirdomomentoem
quevocêdissequeumavariávelguardaumnúmerointeiro,vocêsópoderá
colocarnúmerosinteirosnela.
Vamoschamaressavariávelde numerosecreto,eelaserádotipo int
(quesignificainteiro).Emseguida,vamoscolocaronúmerosecreto,que,por
enquantoserá42,dentrodela. Vejaasduasnovaslinhasemnossocódigo,
14

## Página 26

CasadoCódigo Capítulo3. Variáveis
umadeclarandoavariável,eaoutradandoumvaloraela,usandoosinalde
igual:
int main() {
printf("************************************\n");
printf("* Bem-vindo ao Jogo de Adivinhação *\n");
printf("************************************\n");
int numerosecreto;
numerosecreto = 42;
}
Variável com nome repetido?
Variáveisdevemternomesúnicosdentrodoescopoqueestão. Ou
seja,nãopodemosdeclararduasvariáveis numerosecreto. Sefizer-
mosisso,poralgumengano,ocompiladorreclamaráenãonosgeraráo
executáveldoprograma.Amensagemseráalgocomo: error: redefinition
of ‘numerosecreto’.Ouseja,“redefinição”davariável.
Façaoteste.CrieumavariávelcomomesmonomeeinvoqueoGCC.
Comessavariávelemmãos,poderíamos,porexemplo,imprimi-la.Mas
aperguntaé:comoimprimimosoconteúdodeumavariável?Precisamos,de
algumaforma,avisarao printf()quequeremosimprimir,porexemplo,a
variávelnumerosecreto.
Umaprimeiratentativapoderiaseralgocomo:
printf("O número numerosecreto é secreto!");
Mas,obviamente,oprogramanãotrocaráotexto numerosecretopelo
conteúdodavariável.Elenãotemcomosaberdisso.Precisamosdeixaruma
“máscara”nastring;algoqueoprintf()saibaqueserásubstituídopor
umavariável:paraisso,usamoso %d. Quandocolocamoso %d nomeio
dastring,significaquequeremosquealisejacolocadaumavariáveldotipo
15

## Página 27

3.3. Lendodoteclado CasadoCódigo
inteiro.Existemváriasoutrasmáscaras,queveremosaolongodolivro.Pas-
samostambémparaafun ção printf()avariável numerosecretoque
queremosimprimir.
Paraisso,bastapassarmosumsegundoargumentoparaafun ção,sepa-
randoporvírgula.Vejaemcódigo:
int numerosecreto;
numerosecreto = 42 ;
// imprimindo somente o número
printf("%d" , 42 );
// no meio da frase
printf("O número %d é secreto!");
Porém,claro,vamosjogaressecódigofora,poisojogadornãopodesaber
onúmerosecreto.Issoacabariacomagraç adojogo.
3.3 Lendo do teclado
Agoraquejátemosondeguardaronúmerosecretoeaquantidadedejoga-
das,vamospedirparaousuáriodigitarumnúmero. Deformaanálogaao
printf,temosafun ção scanf,quelêdoteclado.Afun ção scanfprecisa
saberduascoisas:otipododadoqueelavailer,eemqualvariáveleladeverá
colocarovalorlido.Comoousuáriodigitaráumnúmero,declararemosuma
variáveldotipo intefalaremosparaafun çãoqueéumnúmeroqueserá
digitado:éissoqueo %d indica,idênticoaoqueusamosno printf:
int chute;
printf("Qual é o seu chute? ");
scanf("%d", &chute);
printf("Você chutou o número %d!", chute);
Leiacadaumadessaslinhascomaten ção,poiselastêmmuitasnovida-
des. Naprimeira,declaramosavariável chute. Depoisimprimimosuma
mensagemnatela. Atéaqui,vocêjáconhecetudo. Emseguida,usamoso
16

## Página 28

CasadoCódigo Capítulo3. Variáveis
scanfparaleravariável.Passamos %d,porquequeremoslerumnúmero,e
queremosguardá-lonavariávelchute.Repareno &:nãosepreocupecom
eleporenquanto,masguardequevocêsempredeveusá-lono scanf.
Logoapós,imprimimosumamensagem,etambémusamoso %d.Veja
queafun ção printfrecebeudepoisavariável chute.Oqueelafará?Ela
substituiráo %d pelovalorqueestánavariável chute.Elaéumafun ção
bastanteinteligente:
printf("Seu chute foi %d\n", chute);
Vejanossoprogramarodando:
************************************
* Bem-vindo ao Jogo de Adivinhação *
************************************
Qual eh o seu chute? 12
Seu chute foi 12
Acostume-secomvariáveis,afinalnósasusaremosotempointeiro. A
maneiradedeclará-lasserásempreamesma: otipodavariáveleonome
dela. Comonome,podemosleroumudaroseuvalor. Todososcapítulos
daquiparafrentedeclararãovariáveisdosmaisdiferentestipos.
3.4 Entendendo o compilador
SemprequequisermosrodarnossoprogramaemC,precisamosantespassá-
lopeloGCC.Masoqueaconteceali?OGCCéoquechamamosde compila-
dor.Compiladoréoprogramaquepegaocódigoescritoemumalinguagem
deprogramação comoC,Java,C#,ouqualqueroutralinguagemexistente
,eotransformaemuma“outralinguagem”. Essaoutralinguagem,nocaso
doscompiladoresC,éalinguagemdemáquina,queéentendidasomentepor
aquelesistemaoperacionalearquiteturausada(porexemplo,Windowsem
máquinasde32-bits,ouLinuxemmáquinasSunSparc).
17

## Página 29

3.4. Entendendoocompilador CasadoCódigo
Fig.3.1:Funcionamentodeumcompilador
Otrabalhodocompiladornãoénadafácil.Afinal,eleprecisaabriroseu
arquivo .c,eversetudooquevocêescreveuobedeceasregrasdalingua-
gemC(usamosatéotermo gramáticadalinguagemC).Sevocêesqueceuum
pontoevírgula,porexemplo,ocompiladorprecisapararoprocessoeavisar
odesenvolvedor.Depois,setudoestiverdeacordocomasregrasgramáticas
dalinguagem,eleprecisapegarcadainstruç ãodessaeconverterparacódigo
demáquina.
Hojeemdia,compiladoressãobastanteinteligentes.Elesconseguemper-
cebertrechosdecódigoquepodemserotimizados,emuitosdelesatémodi-
ficaminternamenteoseucódigoparaqueasaídasejaamelhorpossível.
OgrandeproblemadeprogramasescritosemCéqueelesnãosãoportá-
veis.Ouseja,oexecutávelgeradopeloseucompiladorGCCnoWindowsnão
funcionaránoLinux;ogeradonoLinuxnãofuncionaránoMac,eassimpor
diante. SeoseuprogramaemCsóusouinstruçõespadrõesdalinguagem,
vocêconseguirápegaromesmo.cecompilaremambasasplataformas,ge-
randodoisexecutáveisdiferentes;entretanto,muitosprogramasemCusam
funçõesespecíficasdesistemasoperacionaisespecíficos,perdendosuapor-
tabilidade.Esseéumproblemaquejáfoibemresolvidoporlinguagensmais
modernas,comoJavaeC#.Ofuncionamentodelesnãoserádiscutidonesse
18

## Página 30

CasadoCódigo Capítulo3. Variáveis
momento.
3.5 Resumindo
Nestecapítulo,aprendemos:
• AescrevernossoprimeiroprogramaemC,eaescreverafun ção main;
• Alereaescreverdaentradaesaídapadrãodosistema,pormeiode
printfe scanf;
• Aprendemostambémadeclararvariáveisdotipointeiro;
• Entendemosopapeldocompiladoremtodooprocesso.
19

## Página 32

Capítulo4
Controledefluxocomifsefors
Opróximopassodonossojogoédizerseochutedousuárioacertouounãoo
númerosecreto.Seeleacertou,daremosparabéns;seerrou,temosqueavisá-
lo.Ocódigopoderiaseralgocomo:
printf("Qual é o seu chute? ");
scanf("%d", &chute);
printf("Seu chute foi %d\n", chute);
printf("Parabens, você acertou!");
printf("Poxa vida, você errou!");
Porém,serodarmosnossocódigodojeitoqueestá,ocomportamentodo
programaseráestranho:eleimprimiráambasasmensagens. Paraqueisso
fiquecerto,precisamosdescobrirsepodemosimprimi-las. Imprimiremos
umaououtra.Portanto,nossoprogramaprecisatomarumadecisão.

## Página 33

CasadoCódigo
Éissoquenossosprogramasfazemotempotodo,eéjustamenteporisso
queelessãoúteis.Conseguimosensiná-losatomardecisõesbaseando-senas
informaçõesquetemosemmãos.Emnossojogo,adecisãoéfácil:seochute
dadopelousuárioforigualaonúmerosecreto,avisaremosqueeleacertou;
casocontrário,avisaremosqueerrou.
Empseudocódigo,éalgocomo:
SE chute FOR IGUAL A numero secreto, ENTAO
avisa que ele acertou
CASO CONTRARIO
avisa que ele errou
Emcódigo,ébemparecido,masusaremospalavraseminglês. Vamos
começarcomo“se”,queeminglês,éif,eo“casocontrário”,queéelse.
Agoraentraasintaxedo ifnalinguagemC.Vejaqueescrevemos ife,
dentrodosparênteses,colocamosacondiç ãoqueeledeveavaliar.Reparesó
naigualdade,queusamosdoisiguais. Issoéparadiferenciardoumúnico
igual(usadoparaatribuirvaloresparavariáveis).
Reparetambémnousodaschaves.Semprequetemosum if,abrimos
umachavepraindicarquealivemumnovoblocodecódigo.Esseblocode-
veráserexecutado,casoaquelacondiç ãosejaverdadeira.
printf("Qual é o seu chute? ");
scanf("%d", &chute);
printf("Seu chute foi %d\n", chute);
if(chute == numerosecreto) {
printf("Parabéns! Você acertou!");
} else {
printf("Você errou!")
}
Reparequeesseblocodecódigoéidênticoaoblocoqueabrimosquando
criamosafun ção main(). Podemosterquantocódigoquisermosdentro
dele.Vejaoexemploaseguir,ondecolocamosmaiscódigodentrodosblocos:
printf("Qual é o seu chute? ");
scanf("%d", &chute);
22

## Página 34

CasadoCódigo Capítulo4. Controledefluxocomifsefors
printf("Seu chute foi %d\n", chute);
if(chute == numerosecreto) {
printf("Parabéns! Você acertou!\n");
printf("Jogue de novo, você é um bom jogador!\n")
// poderíamos ter mais código aqui
// ...
} else {
printf("Você errou!\n");
printf("Mas não desanime, tente de novo!\n");
// poderíamos ter mais código aqui
// ...
}
Masousuárioprecisademaisdicasqueisso.Precisamosdizerseochute
queeledeufoimaior,menorouseacertouemcheio.Nossoprogramaprecisa
fazermaiscomparações.Ochuteémaiorqueonúmerosecreto?Ochuteé
menorqueonúmerosecreto?Ochuteéigualaonúmerosecreto?
Emquemomentodevemosfazerisso?Devemosverificarseeleémaiore
menordentrodo else.Afinal,éaqueletrechodecódigoqueseráexecutado
seochutefoidiferentedonúmerosecreto.Podemos,semqualquerproblema,
colocar ifsdentrode ifs.Nossacondiç ãoagoraseráumpoucodiferente.
Olharemosseochuteémaior( >)oumenor( <)queonúmerosecreto.Veja
ocódigo:
if(chute == numerosecreto) {
printf("Parabéns! Você acertou!\n");
} else {
if(chute > numerosecreto) {
printf("Seu chute foi maior do que o número secreto!\n");
}
if(chute < numerosecreto) {
printf("Seu chute foi menor do que o número secreto!\n");
}
}
23

## Página 35

CasadoCódigo
Teste seu programa!
Acostume-sedesdejáatestaroseuprogramadecomputador. Até
agora,nossoprogramatem3caminhosdiferentes:ocasodeojogador
acertaronúmero,ocasodeonúmerosermenoreocasodesermaior.
Rodeoprograma,nomínimo,3vezes,etestecadaumadaspossi-
bilidades. Énossaresponsabilidadegarantirquetudofuncionacomo
esperado.
Aprendadesdejáqueum bug,ouseja,umdefeitonoprograma,pode
custarmuitodinheiroaosnossosusuáriosfinais. Denovo, testeseus
programas.
Serodarmosnossoprogramaagora,eleimprimiráamensagemcerta,de
acordocomochutedousuário.Semprequetemosnossocódigofuncionando,
éhorademelhorarsualegibilidade.Condiçõesdentrode ifsgeralmentesão
difíceisdeseremlidaseentendidas.Porexemplo,apesardeesse chute ==
numerosecretosersimples,emumsistemamaior,essacondiç ãopoderia
sermaior.Umasugestãoparaissoécolocaressacondiç ãodentrodeumaou-
travariável,comumnomemelhor,queexpliqueaquelacondiç ão.Porexem-
plo,esse iftrataocasodeousuárioteracertadoonúmerosecreto.Vamos
colocá-loemumavariávelcujonomedeixeissoclaro:
int acertou = chute == numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
} else {
if(chute > numerosecreto) {
printf("Seu chute foi maior do que o número secreto!\n");
}
if(chute < numerosecreto) {
printf("Seu chute foi menor do que o número secreto!\n");
}
}
24

## Página 36

CasadoCódigo Capítulo4. Controledefluxocomifsefors
Vejasóqueavariável acertoutemumnomemuitomelhoredeixaclaro
oqueestáacontecendo.Reparequeelaédotipointeiro.AlinguagemCnão
temumtipoparaguardarverdadeirosoufalsos(outraslinguagenstêmotipo
boolean,querecebeapenas trueou false).
Masqualovalorqueestádentrodavariável? Aconven çãodalingua-
geméque 0significa“falso”,ouseja,quandoaexpressãoavaliadanãofor
verdadeira.E 1éocontrário:significaverdadeiro.Podemosatéimprimira
variável,rodarnossoprogramaalgumasvezeseverosvaloresqueestãonela:
int acertou = chute == numerosecreto;
// imprimirá 0 quando a condição for falsa,
// e 1 quando ela for verdadeira.
printf("Acertou: %d\n", acertou);
if(acertou) {
printf("Parabéns! Você acertou!\n");
} else {
if(chute > numerosecreto) {
printf("Seu chute foi maior do que o número secreto!\n");
}
if(chute < numerosecreto) {
printf("Seu chute foi menor do que o número secreto!\n");
}
}
Podemosfazeramesmacoisaparao ifdedentro,ecriarumavariável
queexpliqueoqueestáacontecendo.Dessavez,nãoprecisamosrepetiro if;
afinal,seosnúmerossãodiferentes(poisentrouno else)enãoémaior,logo
serámenor.Veja:
int acertou = chute == numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
} else {
int maior = chute > numerosecreto;
if(maior) {
25

## Página 37

4.1. Escopodevariáveis CasadoCódigo
printf("Seu chute foi maior do que o número secreto!\n");
} else {
printf("Seu chute foi menor do que o número secreto!\n");
}
}
Tudocontinuafuncionandoenossocódigoestámaislegível. Porém,
aindatemosumproblema:ousuáriosóconseguejogarumavez.
4.1 Escopo de v ariáveis
Vocêpercebeuquedeclaramosvariáveisemváriospontosdiferentesdonosso
código? Temosavariável chuteporexemplo,quefoideclaradalogono
começodafun ção main,bemcomoavariável maior,quefoideclaradalá
dentrodo else.
Seráqueconseguimosacessarqualquervariávelaqualquermomento?
Porexemplo,seráqueconseguimosimprimiravariável acertoudentrodo
segundo if?
int acertou = chute == numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
} else {
printf("Acertou: %d\n", acertou);
int maior = chute > numerosecreto;
if(maior) {
printf("Seu chute foi maior do que o número secreto!\n");
} else {
printf("Seu chute foi menor do que o número secreto!\n");
}
}
Sim.Issofunciona.Semprequedeclaramosumavariável,elaédisponível
noescopoemqueelaestáenosescoposmaisadentro.Masoqueé escopo?
26

## Página 38

CasadoCódigo Capítulo4. Controledefluxocomifsefors
Escopoéonomequedamosparaostrechosdoprograma,ondedeterminada
variáveléválida.
Declaramosavariável chutedentrodoescopodafun ção main. Por-
tanto,elaéválidadentrodetodaafun çãoetambémnosescoposquesão
declaradosdentrodela.Porexemplo,os ifse elsesquetemosemnosso
programa.
Noentanto,avariável maiordeclaradadentrodo elsesóévisívelden-
trodoescopodesse else(delimitadopelaschavesqueabrimosaoescrevê-
lo)enosescoposdedentro.Issoquerdizerque,setentarmosusaressavariá-
velemumescopo maiordoqueodo else,nãoconseguiremos.
int acertou = chute == numerosecreto;
printf("%d" , maior);
// lembre-se de que o maior está declarado mais abaixo
// do código, dentro do else
Vejaoerroqueocompiladornosdá,setentarmosusaressavariávelfora
do else:
error: use of undeclared identifier 'maior'
printf("%d", maior);
^
Logo,lembre-sedesempredeclararsuasvariáveisnoescopocorreto.Na
prática,vocêsempreadeclaranoescopo mais altoquevaiutilizá-la.
4.2 Loops e for
Ousuáriopodeter3chancesparaacertaronúmero.Ouseja,precisamosre-
petiromesmotrechodecódigováriasvezes.Imaginecomoseriaseuarquivo:
printf("Qual é o seu chute? ");
scanf("%d" , &chute);
printf("Seu chute foi %d\n", chute);
if (...)
27

## Página 39

4.2. Loopsefor CasadoCódigo
printf("Qual é o seu chute? ");
scanf("%d", &chute);
printf("Seu chute foi %d\n", chute);
if (...)
printf("Qual é o seu chute? ");
scanf("%d", &chute);
printf("Seu chute foi %d\n", chute);
if (...)
Aquioarquivoestáresumido.Agoraimaginealgopior,vocêdecidiumu-
dararegrapara10tentativas.Imaginecopiarecolar10vezesomesmotrecho
decódigo?Agoraimaginequedecidamosalterarafrase Qual é o seu chute?.
Precisaremosalterarem10lugaresdiferentes.Émuitotrabalho!
Desdejá,percebaquecódigorepetidoéerrado,enosdámaistrabalhodo
queoutracoisa.Muitossistemasdeverdadehojesofremcomisso.Imagine
trechosdecódigorepetidosemdiferentesarquivos,etodavezquearegrade
negóciosmuda,odesenvolvedorprecisaencontrartodasessasduplicações.
Quandoeleesquece,umbugacontece.Evocê,queprovavelmenteéusuário
demuitossoftwares,jáviuváriosdeles.
Podemosdizeraonossoprogramapararepetirtrechosdecódigo, de
formaautomática.Paraexecutaromesmocódigováriasvezes,fazemosoque
chamamosdeloops.Aprimeiramaneiradeseescreverumloopéusandoo
for.Vamosusá-lo,poissabemosexatamenteaquantidadedevezesqueque-
remosrepetirumcódigo;nessecaso,3.
Um forcontémtrêspartes: aprimeiraéavariávelqueseráusadade
contadoreoprimeirovalordela;asegundaéacondiç ãodeparadadoloop;
eoterceiroéoincremento.
Emportuguês,parececomplicado,masaideiaéquesefôssemosfazerum
loopde10a30,precisaríamos:inicializarnossavariávelcom10;dizerquea
condiçãoéqueonúmeroprecisasermenorde30paraoloopacontecer;e
que,acadavezqueolooprodar,incrementaríamosnossavariávelcontador
em1unidade.
28

## Página 40

CasadoCódigo Capítulo4. Controledefluxocomifsefors
Veja,emcódigo,nossoloop,de1a3. Inicializamosavariável icom
onúmero1,efizemosacondiç ãodeparadacomosendo i <=3. Comoo
incrementoéum i++,ouseja,soma1àvariável i,então iteráosvalores
0,1e2.Quandoforiguala3,acondiç ãoseráfalsa,eoloopparará:
for(int i = 1; i <= 3; i++) {
printf("Qual é o seu chute? ");
scanf("%d" , & chute);
printf("Seu chute foi %d\n", chute);
int acertou = chute == numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
} else {
int maior = chute > numerosecreto;
if(maior) {
printf("Seu chute foi maior do que o número
secreto!\n ");
} else {
printf("Seu chute foi menor do que o número
secreto!\n ");
}
}
}
printf("Fim de jogo!\n");
Vamosentenderpassoapassooqueacontececomessetrechodecódigo:
1) Oforcomeça.
2) Eleexecutaoprimeirobloco(blocodeinicializaç ão),declaraavariável i
eatribuiovalor1aela.
3) Emseguida,elevalidaacondiç ão,queestánobloco2.Como1émenor-
ou-iguala3,acomparaç ãoretornaverdadeira.
4) Comoacondiçãoéverdadeira,eleexecutaoblocodecódigo.
29

## Página 41

4.2. Loopsefor CasadoCódigo
5) Emseguida,eleexecutaoterceiroblocodo for,queéoincremento.Ali,
fazemos i++,eavariávelpassaavaler2.
6) Novamente,elevalidaacondiç ão.Como2émenor-ou-iguala3,acom-
paraçãoretornaverdadeira.
7) Comoacondiçãoéverdadeira,eleexecutaoblocodecódigo.
8) Novamente,eleexecutaoincremento.Avariável ipassaavaler3.
9) Elevalidaacondição.Como3émenor-ou-iguala3,acomparaç ãoretorna
verdadeira.
10) Comoacondiçãoéverdadeira,eleexecutaoblocodecódigo.
11) Eleexecutaoincremento.Avariável ipassaavaler4.
12) Elevalidaacondição. Como4nãoémenor-ou-iguala3,acomparaç ão
retornafalsa,eoloopacaba.
13) Oprogramacontinuaeamensagem“Fimdejogo”éimpressa.
Portanto,paraentenderofuncionamentodo for,bastaentenderosseus
3blocosequandocadaumdeleséexecutado.Oprimeirobloco,odeinici-
alização,éexecutadoumaúnicaveznocome ço. Emseguida,eleexecutao
segundobloco,acondiç ão. Seelaforverdadeira,eledisparaoblocodecó-
digo.Porfim,eleexecutaoterceirobloco,oincremento.Eaírepete,validaa
condição,executabloco,executaincremento,assimpordiante,atéacondiç ão
deixardeserverdadeira.
Podemosatéaproveitaressavariável ieexibironúmerodatentativa.
Assim,ojogadorficasabendoquantoschuteselejádeu. Eissoéfácil,pois
bastausarmosavariávelno printf. Vejasóosegundo printf. Repare
queessafun çãopoderecebermaisdeumparâmetro. Éassimquefazemos
quandotemosváriasvariáveisparaexibirnamesmalinha:
for(int i = 1; i <= 3; i++) {
printf("Qual é o seu %do. chute? ", i);
scanf("%d" , &chute);
printf("Seu %do. chute foi %d\n", i, chute);
30

## Página 42

CasadoCódigo Capítulo4. Controledefluxocomifsefors
// ...
}
Umdetalheinteressanteépensarnoescopodavariável i. Comoela
foideclaradadiretono for(vejaqueatéusamosasintaxededeclaraç ãode
variáveis:int i = 1),elasóexistedentrodo for.Ouseja,setentarmos
imprimiressavariávelalijuntocomamensagemdefimdejogo,porexemplo,
tomaremosoerrodocompilador,quediráqueavariávelnãoexiste.
4.3 Parando loops
Nossojogoestáindomuitobem.Jápedimosparaousuáriochutarumnú-
mero,efazemosisso3vezes,demaneiraautomática.Eeletambémnosavisa
seesteémaioroumenordoqueonúmerosecreto. Oproblemaéque,se
acertarmosonúmero,elecontinuanospedindomaisnúmerosparachutar.
Enãodeveria:ojogodeveriaterminarali.Veja:
************************************
* Bem-vindo ao Jogo de Adivinhação *
************************************
Qual é o seu chute? 42
Seu 1o. chute foi 42
Parabéns! Você acertou!
Qual é o seu chute? <-- essa linha não deveria estar aqui
Apesardetermosfeitonossoloopsópararquando iformenorque3,
temosumcasoespecial,emqueprecisamospararoloop. Éparaissoque
usamosapalavra break.Elasimplesmenteparaaexecuç ãodoloop,epassa
paraapróximalinha,logoapósofimdolaço.Precisamosquebrá-lonomo-
mentoemqueojogadoracertaonúmero;ouseja,dentrodo ifqueverifica
isso.Vamostambémcolocarumalinhalogoapósoloop,paraentendermos
melhoroqueacontecerá.
Vejaocódigo:
for(int i = 1; i <= 3; i++) {
printf("Qual é o seu %do. chute? ", i);
31

## Página 43

4.3. Parandoloops CasadoCódigo
scanf("%d", &chute);
printf("Seu %do. chute foi %d\n", i, chute);
int acertou = chute == numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
break;
} else {
int maior = chute > numerosecreto;
if(maior) {
printf("Seu chute foi maior do que o número
secreto!\n");
} else {
printf("Seu chute foi menor do que o número
secreto!\n");
}
}
}
printf("Obrigado por jogar!");
Agora,aojogarmos,elecontinuarápedindochutes,enquantoojogador
nãoacertar. Mas,seeleacertar,oprogramaparanahora,independenteda
jogadaemqueeleestá:
************************************
* Bem-vindo ao Jogo de Adivinhação *
************************************
Qual é o seu 1o. chute? 10
Seu 1o. chute foi 10
Seu chute foi menor do que o número secreto!
Qual é o seu 2o. chute? 42
Seu 2o. chute foi 42
Parabéns! Você acertou!
Obrigado por jogar!
Nossojogoestácadavezmelhor.
32

## Página 44

CasadoCódigo Capítulo4. Controledefluxocomifsefors
4.4 Defines,constantes e números mágicos
Definimosqueojogadorterá3chancesparaadivinharonúmerosecreto;e
esse3estáexplícitoemnossocódigo,alidentrodo for. Sequisermosdar
5chances,porexemplo,bastariatrocaressenúmero. Reparequeelenãoé
“simplesmenteumnúmero”. Eletemumsignificadoimportanteparanosso
código.Éonúmeromáximodetentativasqueumjogadorpodeter.
Umacoisaimportantesemprequepensamosemescreverprogramasde
computadoréescrevercódigosquesejamfáceisdeserlidosporoutrosseres
humanos.Afinal,raramenteumprograma termina.Elegeralmenteémantido
pormuitosemuitosanose,senãoforfácilentenderoqueestáescritoali,o
custodemanuten çãosobe.Umadasmaneirasparagarantirqueocódigoseja
fácildesermantidoédarbonsnomesparatudoeevitar“númerosmágicos”.
Númerosmágicossãoaquelesquetêmumsignificadoimportanteparao
código,eestãolájogados.Éocasodonosso 3.Sevocêmostraressecódigo
paraoutrapessoa,eleprecisarálê-lointeiroparaentenderoquesignifica;ao
passoque,setrocarmosonúmero3pelapalavra NUMERO_DE_TENTATIVAS,
tudoficamaisclaro.
Quandotemosnúmerosfixos(constantes,quenãovariam)eimportantes
emnossosistema,geralmentedamosumnomeaele,igualfizemosanterior-
mente.EmC,podemosusaradiretiva #define.Elanosajudaadefiniruma
constante;ouseja,umvalorquenuncamudaráaolongodocódigo.Portanto,
emvezdeusaronúmeromágico,usamosonomedefinido.Vejasuadefini-
çãologoabaixodo #include.Reparequenãousamososímbolodeigual,
apenasdemosumespaçoentreonomedefinidoeoseuvalor:
# include <stdio.h>
# define NUMERO_DE_TENTATIVAS 3
int main() {
// ...
for(int i = 1; i <= NUMERO_DE_TENTATIVAS; i++) {
printf("Qual é o seu %do. chute? ", i);
scanf("%d", &chute);
33

## Página 45

4.5. Oelseif CasadoCódigo
printf("Seu %do. chute foi %d\n", i, chute);
// ...
}
// ...
}
Repareque,diferentedoqueestávamosacostumadoscomnomesdeva-
riáveis,usamosletrasemmaiúsculoeosímbolode underscoreparanomear
constantes.Nãoéobrigatório,massimumaconven ção.Vocêveráquecon-
vençõescomoessasãobastantecomunsnomundodedesenvolvimentode
software. Semprequecairemumanovalinguagem,descubraassuascon-
venções:comonomearvariáveis,ondecolocaroabreefechachavesetc.
4.5 O else if
Atéagora,usamos ifse elsesparadizerseonúmeroeramaior,menorou
igualdoqueonúmerosecreto. Vejaocódigoatual. Reparequetemosum
if,um elsee,dentrodesse else,umoutroconjuntode if-else:
if(acertou) {
printf("Parabéns! Você acertou!\n");
break;
} else {
int maior = chute > numerosecreto;
if(maior) {
printf("Seu chute foi maior do que o número secreto!\n");
} else {
printf("Seu chute foi menor do que o número secreto!\n");
}
}
Poderíamosterescritotudoissoemumaúnicacombinaç ãode if-else
if-else.Ouseja,ainstruç ão elsepodesercombinadacomainstruç ão
if,justamenteparatratarcasoscomoesses,noqualtemosváriascondições
quedevemseravaliadas,atéquealgumasejaverdadeira.
34

## Página 46

CasadoCódigo Capítulo4. Controledefluxocomifsefors
Éesseocaso.Precisamosverificarseosnúmerossãoiguais( if).Sesim,
ousuárioacertou. Senão,precisamosavaliarseonúmeroémaior( else
if).Sesim,ousuáriochutouumnúmeromaior.Casocontrário( else),ele
chutouumnúmeromenor.Emcódigo,veja:
int acertou = chute == numerosecreto;
int maior = chute > numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
break;
} else if(maior) {
printf("Seu chute foi maior do que o número secreto!\n");
} else {
printf("Seu chute foi menor do que o número secreto!\n");
}
Agora,observeocódigoaseguir,muitosimilaraoanterior.Ambostêm
omesmoresultadofinal,masseucomportamentoédiferente.
int acertou = chute == numerosecreto;
int maior = chute > numerosecreto;
int menor = chute < numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
break;
}
if(maior) {
printf("Seu chute foi maior do que o número secreto!\n");
}
if(menor) {
printf("Seu chute foi menor do que o número secreto!\n");
}
Quandotemos if-else ifs-else,assimqueaprimeiracondiç ãofor
verdadeira,asoutrasnãoserãoavaliadas.Elevaide ifa if,epodeeventual-
mentenemolharparaosqueestãomaisabaixo.Jánocasodosvários ifsem
35

## Página 47

4.6. Breakecontinue CasadoCódigo
sequência,mesmoqueaprimeiradêverdadeiro(suponhaqueojogadoracer-
tou),os ifsdebaixotambémserãoavaliados;ouseja,ocomputadorolhará
seonúmeroémaior,edepoisseémenor.
Apesardeocomportamentofinalseromesmo(afinal,porlógica,seuma
dessascondiçõesforemverdadeira,asoutrasserãosemprefalsas),éimpor-
tantevocêentenderadiferençaentreambasasabordagens.Comcerteza,você
passarápormomentosnosquais if-elseifs-elseseráamelhoraborda-
gem,eporoutrosemque ifssequenciaisserãoamelhorsoluç ão.
4.6 Break e continue
Ousuáriopodedigitaronúmeroquequiser.Issoquerdizerquenadaoim-
pedededigitarumnúmeronegativo,porexemplo.Usuáriosquedigitamva-
loresinválidossãobemcomunsemtodosistemadesoftware,evocê,progra-
mador,deveimpedirqueelesinsiramdadosinválidosnaaplicaç ão.
Nossojogodevemostrarumamensagemdeerroparaele,dizendoque
nãopodedigitarnúmerosnegativos.Eletambémnãoperderáumarodadase
fizerisso.Fazerissonãoédifícilcomtudooquejáaprendemos.Umsimples
ifverificandoseochuteémenorque0,logoapóscapturarmosonúmerodo
usuário,ésuficiente.Reparetambémquefazemosum i--,opostodo i++,
parasubtrairumaunidadedavariável,jáqueessarodadanãovale:
for(int i = 1; i <= 3; i++) {
printf("Qual é o seu %do. chute? ", i);
scanf("%d" , &chute);
if(chute < 0) {
printf("Você não pode chutar números negativos\n");
i--;
}
// ...
}
Sótemumproblema:seojogadorchutarumnúmeronegativo,opro-
gramaoavisarádequeissoéinválidoetambémdiráqueonúmeroémenor
36

## Página 48

CasadoCódigo Capítulo4. Controledefluxocomifsefors
doqueosecreto.Nãoqueremosisso.Queremospararaexecuç ãodoloopali,
casoonúmerosejainválido.Maspercebaqueessaéumasituaç ãodiferente
daquelaemqueusamoso break.Aliqueríamosmataroloopinteiro.Aqui,
queremosapenaspassarparaapróximaiteraç ãodoloop.Paraisso,usaremos
ainstrução continue.
O continuedizaolaçoqueeledeveirdiretoparaapróximaiteraç ão,
semexecutarorestantedecódigoqueaindapossaexistirdentrodoseubloco
decódigo.Veja:
if(chute < 0) {
printf("Você não pode chutar números negativos\n");
i--;
continue;
}
Pronto.Agora,seousuárioinserirdadosinválidos,aaplicaç ãovairejeitá-
los.
Portanto,podemosmanipularoloop,usando breake continue.Eles
sãoinstruçõesespecialmenteúteisparaescrevermoscódigosmaissucintos.
Muitasvezestemoscondiçõesatratar,eelasacabampodedecidirsedevemos
continuarexecutandonossocódigo.Reparequeomesmocódigopoderiater
sidoescritosemousode continue.Bastariafazerum if-else.Observe:
if(chute < 0) {
printf("Você não pode chutar números negativos\n");
i--;
} else {
printf("Seu %do. chute foi %d\n", i, chute);
int acertou = chute == numerosecreto;
int maior = chute > numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
break;
} else if(maior) {
printf("Seu chute foi maior do que o número secreto!\n");
} else {
37

## Página 49

4.7. Oloopwhile CasadoCódigo
printf("Seu chute foi menor do que o número secreto!\n");
}
}
Mas,semprequecolocamosum if,precisamoscriarumnovoblocode
código,umaindentaç ãoàfrentedoresto. Issopodedeixarocódigomais
difícildeserlido. Vocêveráquefugirácadavezmaisdemuitasinstruções
aninhadas(ifs,dentrodeifs,dentrodefors,dentrodeifsetc.).Nossocódigo
como continueémaissucinto:eledecideseorestodoblocodeveounão
serexecutado.
Existemmuitasmaneirasdeescreveromesmoprograma.Issonãoélegal?
4.7 O loop while
Vamosmudararegradonossojogo. Ojogadornãoterámaisumaquan-
tidademáximadejogadasafazer;elasserãoinfinitas. Precisamosapenas
contá-las,paraexibiraeleonúmeroderodadasqueprecisouparaadivinhar
onúmero. Aindaprecisamosdeumloop,masoproblemaéqueagoranão
sabemosquandoeleparará.Emcódigo,nãosabemosqualcondiç ãocolocar
dentrodo for.
O foréumótimoloopquandosabemosaquantidadedevezesqueque-
remosexecutaralgumacoisa. Masquandonãosabemosbem,outrosloops
caemmelhor.Paraessecódigo,o whileémaisadequado.O whiletam-
béméumloop,comadiferen çadequenãoprecisamossaberexatamentea
quantidadedevezesqueoexecutaremos.
Queremosfazeralgocomo:
while(JOGADOR NAO ACERTOU) {
// continua jogando
}
Nossa estratégia será a seguinte. Teremos uma variável chamada
acertou,doladodeforado while,quediráseojogadoracertouounão.
Obviamente,elaseráinicializadacom 0,indicandoqueelenãoacertou.Tam-
bémteremosumavariávelchamada tentativas,queguardaráonúmero
dechutesfeitospelousuário(antes,issoestavanavariável ido for,quenão
existemais):
38

## Página 50

CasadoCódigo Capítulo4. Controledefluxocomifsefors
int numerosecreto = 42;
int chute;
int ganhou = 0;
int tentativas = 1;
Emseguida,escrevemosnossoloop. Eledeveacontecerenquantoojo-
gadornãoacertou.Jáfizemosum ifsemelhante,ondevíamosseojogador
acertou,o if(ganhou).Sequiséssemosfazerexatamenteocontrário,pode-
ríamos“negar”oif,usandoosinaldeexclamaç ão,ouseja, if(!ganhou).
Nessecaso,elesóentraseojogadornãoacertou. Podemosfazeramesma
coisano while. Vejaqueaexclamaçãoinverteacondiç ãoeéfácildeler:
semprequevirumaexclamaç ão,leiaapalavra“não”. Noloopaseguir,leia
“whilenãoganhou”,ou“enquantonãoganhou":
int ganhou = 0;
int tentativas = 1;
while(!ganhou) {
}
Vamosagoracapturaraentradadousuárioeverificarseonúmeroénega-
tivoounão.Aquiaindausaremoso continue;afinal,eletambémfunciona
comolaço while.Reparequetrocamos ipor tentativas:
int ganhou = 0;
int tentativas = 1;
while(!ganhou) {
printf("Qual é o seu %do. chute? ", tentativas);
scanf("%d" , & chute);
if(chute < 0) {
printf("Você não pode chutar números negativos\n");
continue;
}
printf("Seu %do. chute foi %d\n", tentativas, chute);
39

## Página 51

4.7. Oloopwhile CasadoCódigo
}
Oblocode ifse elseifscontinuaigual.Masreparequeretiramoso
break,etrocamosporum ganhou = 1.Afinal,éelequefaráolaçoparar:
int ganhou = 0;
int tentativas = 1;
while(!ganhou) {
printf("Qual é o seu %do. chute? ", tentativas);
scanf("%d" , &chute);
if(chute < 0) {
printf("Você não pode chutar números negativos\n");
continue;
}
printf("Seu %do. chute foi %d\n", tentativas, chute);
acertou = chute == numerosecreto;
int maior = chute > numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
ganhou = 1;
} else if(maior) {
printf("Seu chute foi maior do que o número secreto!\n");
} else {
printf("Seu chute foi menor do que o número secreto!\n");
}
}
Porfim,bastaapenasincrementarmosavariável tentativas. Antes,
avariável ieraincrementadanoterceiroblocodo for,executadoauto-
maticamente.No while,sevocêprecisarcontaraquantidadedeiterações,
precisaráfazerissoporcontaprópria:
40

## Página 52

CasadoCódigo Capítulo4. Controledefluxocomifsefors
while(!ganhou) {
// ...
if(acertou) {
printf("Parabéns! Você acertou!\n");
ganhou = 1;
} else if(maior) {
printf("Seu chute foi maior do que o número secreto!\n");
} else {
printf("Seu chute foi menor do que o número secreto!\n");
}
tentativas++;
}
Nossojogoagoratemtentativasilimitadas.
Portanto,temosdiferentesmaneirasdeexecutaromesmotrechodecó-
digo.Chamamosissodeloops.O fore whilesãobastantecomuns.Usa-
mos forquandosabemosaquantidadedevezesquevamosexecutarotrecho
decódigo,e whilequandonãosabemosbem.Vocêconsegueescreverqual-
querloopusandoqualquerumadessasduasabordagens,mascomotempo,
aexperiêncialhemostraráqualéomelhordeles,emtermosdemanuten ção.
Nessemomento,sigaaregraditaanteriormente. Sabeaquantidade? for.
Nãosabe? while.
4.8 Loops infinitos
Se você olhar o código com carinho, verá que poderíamos escrever esse
mesmocódigosemprecisardavariável ganhou. Afinal,poderíamosfazer
usodo breakepararoloopnomomentoemqueeleganhou:
while(!ganhou) {
// ...
if(acertou) {
printf("Parabéns! Você acertou!\n");
break;
} else if(maior) {
41

## Página 53

4.8. Loopsinfinitos CasadoCódigo
printf("Seu chute foi maior do que o número secreto!\n");
} else {
printf("Seu chute foi menor do que o número secreto!\n");
}
tentativas++;
}
Percebaque,comessecódigo,nossoloopvirou infinito.Afinal,suacon-
diçãonuncaseráfalsa. Nossoprogramasóparaporqueexisteum break
ali.
Nessecaso,avariável ganhoudeixadeserútil,jáqueelaserá 0para
sempre. Podemosdescartá-laefazeroloop whileserinfinito,massem
precisardela. Sabemosqueacondiç ão,quandoavaliada,nosdevolve 0ou
1.Oloopiterasemprequeacondiç ãoéavaliadaem 1.Vamoscolocaresse
valordiretonoloop:
while(1) {
// ...
}
Pronto.Agorareescrevemosnossoalgoritmo,demaneiraanãoprecisar
maisdavariávelganhou.Vejasócomoprogramarélegal:vocêpodeescrever
omesmoprograma,deváriasmaneirasdiferentes.
42

## Página 54

CasadoCódigo Capítulo4. Controledefluxocomifsefors
Cuidado com o loop infinito
Umdosgrandesperigosquandousamosloopséjustamentequando
escrevemosloopsquenãoparamnunca. Porexemplo,vejaocódigoa
seguir,ondeusamosumsimples while:
int i = 1;
while(i > 10) {
printf("i vale %d\n", i);
}
Repareque,nessecaso, inuncaserámaiorque10,poiselevalerá
1parasempre.Comoacondiç ãoserásemprefalsa,nessescasos,nosso
programaficaráinfinitamentedentrodesseloop.
Issoraramenteéproposital.Geralmente,quebramosoloopemalgum
momento.Portanto,presteaten çãonasuacondiç ãoegarantaqueumdia
elepararádeexecutar.
Está perdido?
O código até o momento está em
http://pastebin.com/Zhp0XzSc
4.9 R esumindo
Nestecapítulo,aprendemos:
• Atomardecisõesemnossosprogramas,usando ifs;
• Atomarmuitasdecisões,usandoifs, else ifse elses;
• Afazerloopscontadoscomofor;
• Afazerloopscomwhile;
• Acriarconstantesusando#define.
43

## Página 56

Capítulo5
Tiposdedadoseoperações
matemáticas
Comovimos,todadeclaraç ãodevariávelprecisaviracompanhadadeum
tipo.Nãoexistemvariáveissemtipo.AlinguagemCpossuiváriostiposdi-
ferentes,deacordocomodadoquevocêquerguardar. Vocêjáviuquese
quisermosguardarnúmerosinteiros,usamosotipo int.
Veja,porexemplo,queemnossojogo,jádeclaramosalgumasvariáveis
dotipointeiro:
int numerosecreto = 42;
int chute;
int acertou = 0;
int tentativas = 1;
Reparequeinicializamosnamesmalinhadadeclaraç ãoemváriasdelas.

## Página 57

5.1. Operaçõesmatemáticas CasadoCódigo
Jánavariávelchute,não.Lembre-sesempredeinicializaravariávelantes
deusá-la;sejanamesmalinha,oualgumaslinhasdepois,usandoosinalde
atribuição( =).
5.1 Operações matemáticas
Vamoscolocarumanovaregraemnossojogo:pontos.Aofinaldapartida,
diremosaojogadorquantospontoselefez.Aregraseráaseguinte:todojo-
gadorcome çacom1000pontos.Acadarodada,subtraímosdessenúmeroa
diferençaentreonúmerosecretoeochute,divididopor2.
Porexemplo,seonúmerosecretoé20eelechutar30,subtrairemos5,que
éoresultadode (30-20)/2.Seelechutar50,subtrairemos15,eassimpor
diante.Ouseja,quantomaispertoforochutedele,menospontoseleperderá,
tendomaispontosnofinal.
Paraisso,vamosdeclararavariável pontos,einicializá-lacomovalor
1000:
int pontos = 1000;
Agorabastamanipularessavariável. Comoelaguardaumnúmeroin-
teiro,podemosfazeroperaçõesmatemáticas.Podemossomar(+),multiplicar
(*),dividir(/)esubtrair(-)oconteúdodessasvariáveis.Observe:
pontos = pontos + 2;
pontos = pontos * 4 / 3;
pontos = pontos - 1;
int outravariavel = pontos * 7;
printf("Você fez %d pontos", pontos);
Vejaque,nessecódigo,fizemosdiversasoperaçõesmatemáticasquais-
quereaguardamosnaprópriavariável,ouemumanova.Estamosprogra-
mando,logotemosaliberdadedefazeroquequisermos.Vocêtambémpode
usarparêntesesparadefinirprecedênciadeoperações. Obviamente,assim
comonamatemática,elessãoopcionais,evocêpodeusarquantosquiser:
46

## Página 58

CasadoCódigo Capítulo5. Tiposdedadoseoperaçõesmatemáticas
int pontos = ((4 * 2) + (1/2)) * 3 - 1;
Agora,bastafazermosasubtraç ãologoantesdeonossoloopacabar.Des-
cobriremosquantospontosprecisamossubtraireofaremos:
for {
// ...
int pontosperdidos = (chute - numerosecreto) / 2;
pontos = pontos - pontosperdidos;
}
Vamostambémexibiraquantidadedepontosaofinaldojogo:
for {
// ...
}
printf("Você fez %d pontos\n", pontos);
printf("Obrigado por jogar!\n");
Tudofunciona.Nossojogoestábemmaisdivertido!
47

## Página 59

5.2. Outrostiposnuméricos CasadoCódigo
O que acontece se eu usar uma v ariável não iniciali-
zada?
Dependemuitodalinguagemedocompilador.EmC,quandovocê
declaraumavariável,oprogramaseparaumespaçodememóriaquees-
tavalivreparaela.Sevocêusá-lasemdarumvalorinicial,provavelmente
seuconteúdoseráumlixoqualquer;oqueestavanaquelaregiãodeme-
móriaantesdeseuprogramapegarparaele,queerausadoporalgum
outronoseucomputador.
LinguagenscomoJava,porexemplo,nãopermitemquevocêfaç aisso.
Sevocêtentarusarumavariávelseminicializá-la,ocompiladordaráum
errodecompilação.
EmC,tudoémaismanual.Portanto,lembre-sedesempreinicializar
suasvariáveis.
5.2 Outros tipos numéricos
Masoqueacontecesejogarmososnúmeros45e42?Oresultadodeveriaser
998.5.Afinal, (45-3)/2éiguala1.5.Porém,serodarmos,nossojogonos
dará999pontos.
Oqueaconteceu?Simples.Númerosinteirosnãofazemoperaçõescom
casasdecimais,portantotruncamoresultado. Precisamosmudarotipoda
variávelpontos.
Alémde int,temosoutrostiposparatrataroutrosproblemas. Otipo
double,porexemplo,noséútilquandoqueremosguardarnúmeroscom
casasdecimais.Paradeclararumavariáveldessetipo,reproduziremosoque
jáfizemos.Vejaocódigoaseguir,queusatantodoublesquantointeiros:
double pi = 3.1415;
int raio = 3;
double areadocirculo = pi * raio * raio;
printf("A área do círculo é %d", areadocirculo);
Outrodetalheimportanteéotamanhodavariável.Afinal,cadatipotem
48

## Página 60

CasadoCódigo Capítulo5. Tiposdedadoseoperaçõesmatemáticas
umtamanhodefinido,eissoimplicaemguardarnúmerosentrecertosin-
tervalos.Porexemplo,uminteiroemumamáquinade32bitségeralmente
armazenadoem4bytes(ouseja,32bits).Issosignificaquepodemosguardar
númerosde 2^-32até2`.Sãonúmerosgrandes,masàsvezesnãosuficien-
tesparaoseutipodeaplicaç ão.
UmbomexemploéopróprioYoutube,queusavainteirosparaguardaro
númerodevezesqueumvídeofoivisto.Em2014,oclipdamúsica Gangnam
Style,docoreano Psy,ultrapassouolimitedosinteiros;assim,elesprecisaram
mudarseustipospara long.
O longésimilaraointeiro,masaguentanúmerosmaioresainda;afi-
nal,eleéarmazenadoem8bytes(64bits). Portanto,elesuportanúmeros
de 2^-64até2`,sendoestesrealmentegrandes. Analogamente,temoso
short,queéuminteiromenorainda;eo float,queéum doublemenor
(floattemmenosprecisãodoque double,ouseja,suportamenoscasas
decimais).
Todoselessãousadosdamesmamaneira:
int n1;
double n2;
long n3;
short n4;
float n5;
Dependendodaplataformanaqualvocêestádesenvolvendo,escolhero
tipomaiseconômicopodefazersentido. Muitosdessesdispositivosdepe-
quenoportetêmmemóriasextremamentelimitadas.
E para guardar uma palavra?
Cnãotemumtiponativoparaseguardarumapalavrainteira.Mais
àfrente,estudaremosarraysde chars,usadospararesolvertalproblema.
Nessemomento,nãosepreocupecomisso.
Emnossojogo,comoaquantidadedepontospodetercasasdecimais,
precisamosusar double. Assim,poderemosternúmerosquebrados. Pre-
49

## Página 61

5.2. Outrostiposnuméricos CasadoCódigo
cisaremosacertartambémo printf,poisagoraprecisamosimprimirum
double.Bastatrocarmoso dpor fnamáscara:
double pontos = 1000;
printf("Você fez %f pontos", pontos);
Porém,oestranhoéque,serodarmosnovamentenossojogo,aindatere-
mosomesmoproblema:999pontos.Masoqueaconteceu,seagoradefini-
mosavariávelcomo double?Observealinhaemquefazemosaoperaç ão:
double pontosperdidos = (chute - numerosecreto) / 2;
Nestemomento,vocêprecisapensarcomoumcompilador.Acrediteou
não,elecome çaafazerasoperaçõesdadireitaparaesquerda.Ouseja,elevai
primeirofazeraconta (chute - numerosecreto) / 2,parasódepois
verqueprecisaguardaresseresultadonavariável pontosperdidos.
Olhesóapartedadireita.Vejaque chute, numerosecretoe 2são
inteiros. Oquenossoprogramafará? Umacontacomnúmerosinteiros! A
divisãoserátruncadadomesmojeito.Vejaqueesseproblemanãoaconteceria
setodasasvariáveisalijáfossem doubles.Porexemplo,acontaaseguirdá
1.5,poistodasasvariáveissãodotipocerto:
double a = 3;
double b = 2;
double c = a / b;
printf("%f", c); // imprime 1.5
Precisamosfalarparaonossoprogramaqueaquelacontadeveserfeita
com double.Umapossívelmaneiraéconvertermosapenasonúmero 2para
double.Setemosumaoperaç ãoqueenvolveinteirosenúmeroscompontos
flutuantes,elefaráacontacomnúmeroflutuante. Logo,bastacolocarmos
2.0emvezde 2:
double pontosperdidos = (chute - numerosecreto) / 2.0;
Agorasim,temosnúmerosquebradosemnossojogo.
50

## Página 62

CasadoCódigo Capítulo5. Tiposdedadoseoperaçõesmatemáticas
E se eu não quiser imprimir tantas casas decimais?
OCautomaticamenteimprimeváriascasasdecimaisquandousamos
amáscara %fno printf().Maspodemosmudarisso.Seusarmosa
máscara%.2f,estamosdizendoquequeremosimprimiraquelenúmero
comapenas2casasdecimais:
printf("Você fez %.2f pontos\n", pontos);
Vocêpodetrocaronúmero2pelaquantidadedecasasdecimaisque
vocêquiser.
5.3 Conversões e casting
Nase çãoanterior,for çamosonúmero2aserum double,aoescrevermos
2.0.Masseráqueessaéaúnicamaneiradefazermosisso?Eseanossaexpres-
sãofossecompostaapenasdevariáveisdotipointeiro?Comofor çaríamosa
contaparaqueelafossefeitacomcasasdecimais?
Vejaocódigoadiante.Nele,teremosomesmoproblemaquetivemoscom
ospontosemnossojogo.Aoperaç ãoaconteceráprimeirodoladodireitoe,
comotodoeleécompostopornúmerosinteiros,nãohaverácasasdecimais,
mesmoqueotipodavariávelàesquerdaseja double:
int a = 3;
int b = 2;
// mesmo problema do nosso jogo
double resultado = a / b;
printf("%f" , resultado);
Nessecaso,precisamos“converter”asvariáveisinteirasparaalgumtipo
compontoflutuante. Aessaconversão,damosonomede casting. Fazê-la
ébemfácil: bastacolocarmosotipoparaoqualqueremosconverterentre
parênteses,antesdeusaravariável.Veja:
int a = 3;
int b = 2;
51

## Página 63

5.3. Conversõesecasting CasadoCódigo
// o casting acontecendo abaixo nas
// duas variáveis: a, b.
double resultado = (double)a / (double)b;
printf("%f" , resultado);
Agorasim.Aocolocar (double),estamosdizendoaocompiladorpara
trataraquelavariável,queéum int,como doublenaquelemomento. A
operaçãoacontecerádaformaquequeremos.
Aoperaçãodecastingprecisaserusadacomcuidado. Algunscompi-
ladoresdeixarãovocêconverterdequalquertipoparaqualqueroutrotipo.
Entretanto,algunscastingspodemnãoterosresultadosesperados.
Porexemplo,sefizermosocastingdeum doubleparaum int,pro-
vavelmenteperderemosinformações.Afinal,um doubleconsegueguardar
númerosmuitomaioresecomcasasdecimaisdoqueum int.Sefor çarmos
aconversão,amáquinafará,porémocorreráumaperda.Vejaocódigoase-
guir,noqualconvertemosum doublepara int.Asaídadesteprogramaé
3,poisascasasdecimaisforamperdidas:
// aqui a casa decimal está guardada
double pi = 3.1415;
// agora o casting forçado, de um tipo
// que aguenta mais dados para um que aguenta
// menos dados, perde informação
int coitadodopi = (int )pi;
printf("%d" , coitadodopi);
Portanto,castingssãocapazesdeconverterumtipoemoutro.Mas,de-
pendendodosentidoemqueissoéfeito,informaçõespodemdesaparecer.
Bastavocêpensar:seestouconvertendoparaumtipoemquecabemaisin-
formaçãodoqueotipoatual,eleacontecerásemproblemas;casocontrário,
haveráperdadeconteúdo.
Devoltaaojogo,poderíamossimplesmentealteraralinhadacontados
pontosparaalgumadasqueseguem,eoefeitoaindaseriaomesmo:
52

## Página 64

CasadoCódigo Capítulo5. Tiposdedadoseoperaçõesmatemáticas
// casting só no 2
double pontosperdidos = (chute - numerosecreto) / (double)2;
// casting nas duas operações
double pontosperdidos =
(double)(chute - numerosecreto) / (double)2;
5.4 Funções matemáticas
Aindatemosumpequenoproblema.Oqueacontececomnossospontosse
chutarmosonúmero30? Acontaqueelefaráé: (30 - 42) / 2.0,que
dá-6.Depois,quandoeleforsubtrairdavariável pontos,elefará -(-6);
ouseja,somará6.Ojogadorganharápontosemvezdeperder!Precisamos
corrigirisso.Aprimeirasoluç ãoéfazerum if.Seonúmerofornegativo,
multiplicamospor -1(aíeleficarápositivo).Veja:
double pontosperdidos = (chute - numerosecreto) / 2.0;
if(pontosperdidos <0) {
pontosperdidos = pontosperdidos * -1;
}
Essecódigofunciona,mastemosumasoluç ãomaiseleganteparaisso,em
C.Podemosusarafun ção abs(),querecebeuminteirocomoparâmetro,e
otransformaempositivo.Ouseja,nofim,elafazamesmacoisaquenosso
if.Adiferen çaéquegastaremosmenoslinhasdecódigoparaisso.
Vejaexemplos:
int a = abs(-10); // retorna 10
int b = abs(10); // retorna 10
int x = -10;
int y = abs(x); // retorna 10
Comessafun çãoemmãos,bastaagoraaplicarmosàoperaç ãodesub-
tração,garantindoqueelasemprenosretornaráumnúmeropositivo. Em
código:
double pontosperdidos = abs(chute - numerosecreto) / 2.0;
53

## Página 65

5.5. Númerosrandômicos CasadoCódigo
Afun ção abs(),assimcomoa printf,precisaserimportadadeoutro
arquivo.Fazemosissopormeiode include,igualfizemoscomoarquivo
stdio.h.Parausarmosa abs(),precisamosimportar stdlib.h,quesig-
nifica standard library.Bastaadicionarmosoutralinhadeinclusãonocome ço
doarquivo:
#include <stdio.h>
#include <stdlib.h>
Tantoa stdlibquantoa stdiosãobastantecomunsemprogramasC,já
queelascontêmasdefiniçõesdasfun çõesmaiscomuns.Vocêveráqueseus
programasmuitoprovavelmentesemprecome çarãoimportandoessesdois
arquivos.
5.5 Números randômicos
Porenquanto,onúmerosecretoestáfixo,eissotiratodaagraç adojogo.
Precisamosfazercomque,acadavezqueoexecutarmos,ocomputadorpense
emumnúmerodiferente. Sorteanossaquea stdlibcontémumafun çãosó
paraisso:umaquenosdevolveumnúmerorandômico.
Afun çãochama-se rand()eelanosdevolveumnúmeroaleatórioa
cadavezqueéexecutada.Veja:
int n1 = rand();
printf("%d" , n1);
int n2 = rand();
printf("%d" , n2);
Aoexecutaroprogramaaseguir,elenosimprime:
16807
282475249
Doisnúmerosdiferentes,exatamentecomoqueríamos.Masoproblema
aconteceserodarmosdenovo:elenosdaráosmesmosnúmeros!Ouseja,eles
nãosãotãorandômicosassim.Computadoresnãosãocapazesdegerarnú-
meros100%randômicos.Porisso,dizemosqueelessão pseudorrandômicos.
54

## Página 66

CasadoCódigo Capítulo5. Tiposdedadoseoperaçõesmatemáticas
Normalmente,asimplementaçõesdefun çõesquedevolvemessesnúmeros
usamalgumafun çãomatemáticabastantecomplicadaparagerarumnúmero
quesejadifícildeprever.
Paragarantirmosqueessafun çãomatemáticausadapela rand()seja
diferenteacadarodada,precisamosdefiniruma“semente”diferenteacada
execuçãodonossoprograma. Asementeécomosefosseumavariávelque
entranessafórmulamatemáticaedeixaosnúmerossemprediferentes.Mas
precisamosdeumasementediferentetodavez,poissepassarmossemprea
mesma,afórmulatambémserásempreamesma,assimcomooresultado.
Paraisso,utilizamosadatacompletaatualcomosemente. Vejaque,se
rodarmosoprogramaduasvezes,adataatualsempreserádiferente,poisa
dataexataterámudado(algunsmilissegundos,segundosouminutosamais,
porexemplo).Issoésuficienteparatermossementesdiferentes.
Dataéalgobeminteressanteemsistemasdecomputaç ão.Umamaneira
muitocomumdeseolharparaelaépensarnossegundosquesepassaram
desdeumadataespecífica.Afinal,tendoonúmerodesegundospassados,é
possívelsaberadataexata.Emcomputaç ão,adataescolhidaparatalé“1de
janeirode1970";elaé,inclusive,chamadade Epoch. EmC,temosafun ção
time(),quenosdevolveexatamenteessaquantidadedesegundos.Paraisso,
bastadeclararmosuminteiroeinvocarmosafun ção time(),passandoo
valor“zero”paraela.Emseguida,elaépassadaparaafunção srand(),que
équemdefineasemente.
Afun ção time()estádefinidaemoutroarquivo,o time.h,etambém
precisamosimportá-lonocome çodoarquivo.Ocódigocompletoficaassim:
# include <time.h>
int segundos = time(0 );
srand(segundos);
int n1 = rand();
printf("%d", n1);
Agora,cadavezqueexecutarmosesseprograma,teremosumnúmero
diferente. Sabendodisso,vamosusarnúmerosrandômicosemnossojogo,
paraqueelefiquemaisdivertido.Porém,aindatemosumdetalheaacertar:
55

## Página 67

5.5. Númerosrandômicos CasadoCódigo
vocêreparouqueessenúmerorandômicoémuitogrande?Issonãoajudará
nossojogador.
Precisamosdefinirumintervaloparaele.Ouseja,amáquinasópoderá
chutarnúmerosde0a99. Nãoconseguimosmudarocomportamentoda
função rand(),maspodemosfazeroperaçõescomoresultado.Secalcular-
mosorestodadivisãodessenúmeropor100,porexemplo,teremossempre
umintervaloentre0e99. Logo,seráissooquefaremos. Vamosutilizaro
restodadivisãoparatermosumnúmeronointervaloquequeremos. Para
calcularorestodadivisãoentredoisinteiros,bastausarmosooperador%
(porcento):
int segundos = time(0);
srand(segundos);
int numerogrande = rand();
int numerosecreto = numerogrande % 100;
Ótimo.Nossojogoestácadavezmelhor.
Precisamos de tantas v ariáveis assim?
Não.Poderíamosterfeitoemmenoslinhas.Porexemplo:
srand(time(0));
int numerosecreto = rand() % 100;
Issoéquestãodegosto.Àsvezes,poucaslinhassãomaisfáceisdese-
remlidas.Mas,emoutras,teressasvariáveisnomeio,comnomesbem
definidos,ajudamoprogramadoraentendermelhoroqueestáaconte-
cendo.
Comeceapensarnisso.Mostreseucódigoparaseuamigoevejase
eleentendeu.Casonãotenhaentendido,outenhalevadomuitotempo
paraentender,ésinaldequedáparamelhorar.
56

## Página 68

CasadoCódigo Capítulo5. Tiposdedadoseoperaçõesmatemáticas
Está perdido?
Vocêpodeverocódigofeitoatéessemomentoem
http://pastebin.com/P1mREDbg
5.6 Resumindo
Nestecapítulo,aprendemos:
• Queexistemtiposdedadosdiferentes;
• Inteiros armazenam apenas números inteiros, enquantodoubles
guardamnúmeroscompontoflutuante;
• Quepodemosfazerasmaisdiversasoperaçõesmatemáticascomessas
variáveis;
• Usarfunçõesda stdlib,comoa abs();
• Gerarnúmerosrandômicos,usandosrand()e rand();
• Quepodemosfazerconversõesentretipos,usandocasting;
• Usarrestodadivisãoparagerarnúmerosdentrodeumintervalolimi-
tado.
57

## Página 70

Capítulo6
Finalizandoojogo
Faltapoucoparaterminarmosnossojogo. Vamosmudaragoraaregrado
númerodetentativas.Ousuáriopoderáescolherentre3níveisdedificuldade:
fácil,médioedifícil.Deacordocomonível,decidiremosaquantidade.Por
exemplo,nonívelfácil,eleterá20chances;nomédio,terá15chances;eno
difícil,apenas6chances.
Comoquevimosatéaqui,bastaperguntarmosparaousuárioonívelde
dificuldade,aíusamosalguns ifsparadecidiraquantidade:
int nivel;
int totaldetentativas;
printf("Qual o nível de dificuldade?\n");
printf("(1) Fácil (2) Médio (3) Difícil\n\n");
printf("Escolha: ");

## Página 71

CasadoCódigo
scanf("%d", &nivel);
if(nivel == 1) {
totaldetentativas = 20;
} else if (nivel == 2) {
totaldetentativas = 15;
} else {
totaldetentativas = 6;
}
Comosabemosaquantidadedevezesqueolooptemdeacontecer,basta
trocarmoso whileatualporum for.Precisamostambémlembrardejogar
foraavariável tentativasetrocartodasasvezesqueausamospor i.
Afinal, ivoltouasernossocontadordajogada.Precisamostambémvoltar
como breakparacasoousuárioacerteonúmero,poisnosso foragorasó
pararáquandoonúmerodetentativasesgotar.Porfim,precisamosvoltaro
i--casoelechuteumnúmeronegativo:
// deletamos a declaração do acertou aqui de cima
for(int i = 1; i <= totaldetentativas; i++) {
printf("Tentativa %d de %d\n", i, totaldetentativas);
// ...
if(chute < 0) {
printf("Você não pode chutar números negativos\n");
i--;
continue;
}
// ...
acertou = chute == numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
break;
}
60

## Página 72

CasadoCódigo Capítulo6. Finalizandoojogo
// ...
}
Está perdido?
Fizemosbastantemudan çasnessecódigo.Variáveissumiram,outras
apareceram.Éumbomdesafioparavocêfazerojogocompilarefunci-
onaratéaqui.
Seestásesentindoperdido,vejaocódigofeitoatéessemomentoem
http://pastebin.com/yzaRVAhX
6.1 Switch e case
Umaalternativaaos ifséusaro switch.O switchéum if mais simples.
Quandotemoscondiçõesrepetidas,nasquaiscomparamosumavariávelin-
teiracomváriosnúmeros(igualemnossocaso,emquecomparamos nivel
com1,2e3),podemosusaro switch.
Suasintaxeémaisclaraparaessetipodedecisão.Primeiro,vocêdefine
emqualvariávelo switchacontecerá.Emseguida,vocêtemumasequência
de case,umparapossívelop ção.Apósosdois-pontos,vocêescreveobloco
decódigoqueseráexecutado,casoo casesejaverdadeiro.Umdetalheim-
portanteéque,aofinaldecadabloco,vocênãopodeseesquecerdo break
(sim,omesmoqueusamosnoloop),poisprecisamosquebraraexecuç ãodo
switch.Veja:
int nivel;
scanf("%d", &nivel);
switch(nivel) {
case 1:
totaldetentativas = 20;
break;
case 2:
totaldetentativas = 15;
break;
61

## Página 73

6.2. Novamenteusandovariáveiseescopos CasadoCódigo
case 3:
totaldetentativas = 6;
break;
}
Esse switchtrataoscasosdenúmeros1,2e3.Seousuáriodigitar,por
exemplo,4,o switchnãofaránada. Podemosdefinirocomportamento
padrão;ouseja,oqueeledevefazer,casonenhum casebata.Vamosdefinir
oseguintecomportamento:seousuáriodigitarqualqueroutronúmeroque
não1,2,3,onívelseráavan çado.Issoquerdizerqueprecisamostransformar
o case 3emum else.O elsedo switchéo default.Observe:
int nivel;
scanf("%d", &nivel);
switch(nivel) {
case 1:
totaldetentativas = 20;
break;
case 2:
totaldetentativas = 15;
break;
default:
totaldetentativas = 6;
break;
}
6.2 Nov amente usando v ariáveis e escopos
Nossojogoaindatemum bug.Vocêconheceotermo bug,certo?Éonome
dodiaadiaquedamosparaproblemasemnossaaplicaç ão. Seousuário
acertaonúmero,sempremostramosumamensagemamigávelaele.Masfalta
mostrarmosumamensagemavisandoqueeleperdeu,casosuastentativasse
esgotem.
Nessemomento,seelasseesgotarem,aindaexibimos“Obrigadoporjo-
gar";porémprecisamosexibiralgomaisclaroparaele. Algocomo“Você
perdeu,tentenovamente!”.Aquestãoé:ondecolocaressalógica?
62

## Página 74

CasadoCódigo Capítulo6. Finalizandoojogo
Exibiramensagemdevitóriaerafácil,poistínhamosum ifespecialpra
essecaso.Mas,nocasodaderrota,não.Precisamosesperaro foracabare,
aísim,mostraramensagem.Oprimeiropassoécolocá-lalogoapósofimdo
loop:
} // fim do for
printf("Você perdeu! Tente novamente!");
printf("Você fez %.2f pontos\n", pontos);
printf("Obrigado por jogar!\n");
Entretanto,dessejeito,essamensagemaparecerátantonocasodavitória
quantodaderrota.Precisamosdeum ifali,quefaç acomqueissosejaim-
pressoapenasnaderrota.Podemosusaravariável acertou.Vejaque,como
elaestádeclaradaforado for,logonocome çodonossoprograma,podemos
usá-lamesmoapósoloop.Agorapense,seoloopforatéaúltimaiteraç ão,o
conteúdodavariávelacertouseráoresultadocalculadonaúltimaiteraç ão.
Seelevenceuojogo, acertouvalerá1;casocontrário,0.Podemosfazero
loop:
int acertou = 0;
for(...) {
// código aqui
acertou = chute == numerosecreto;
int maior = chute > numerosecreto;
if(acertou) {
printf("Parabéns! Você acertou!\n");
break;
} else if(maior) {
printf("\nSeu chute foi maior do que o número
secreto!\n\n");
} else {
printf("\nSeu chute foi menor do que o número
secreto!\n\n");
63

## Página 75

6.2. Novamenteusandovariáveiseescopos CasadoCódigo
}
// código aqui
}
if(!acertou) {
printf("Você perdeu! Tente novamente!\n");
}
Ótimo. Agoramostramosumamensagemamigávelnaderrota. Jáque
tudoestáfuncionando,podemosmelhorarumpouconossocódigo.Vejaque
amensagemdederrotaestáembaixodo for,masadesucessoestádentro.
Podemoscolocartudoemumsólugarparafacilitaramanuten ção.Ouseja,
saberemosque,logoapóso for,entraainteligênciadamensagemdeganhou
ouperdeu.
Vamosremovero printf()queexistedentrodo if(acertou),que
estádentrodo for, ecolocá-loemum else, logoapóso for. Re-
pareque,comoagoratemos if-else,acondiç ãofoiinvertida(fizemos
if(acertou)emvezde if(!acertou).Vocêpoderiaprogramardeam-
bososjeitos,afinaloresultadoseriaomesmo. Porém,comcertezaémais
fácilentenderumacondiçãosemanegaç ãodoquecomela:
for(...) {
if(acertou) {
break;
}
// ...
}
if(acertou) {
printf("Parabéns! Você acertou!\n");
} else {
printf("Você perdeu! Tente novamente!\n");
}
64

## Página 76

CasadoCódigo Capítulo6. Finalizandoojogo
6.3 Embelezando o jogo
Nossojogoestáinteirofuncional.Masaindanãoestábonito.Asfrasesestão
coladasumasàsoutras,ostextosestãorepetidosetc.Interfaceéfundamental
paranossosusuários. Afinal,elesnãoqueremsaberoqueestápordentro;
elessóquereminteragircomapartedefora.
Mesmoqueestejamosfazendoaplicaçõesnoterminal,aindaassimpode-
moscapricharefazernossosprogramasteremsaídaselegantes.Ocabe çalho
podeseralgomaischamativo.Podemosfazerdesenhosusandosóletras!Por
exemplo,umcabe çalhomaisdivertidoseria:
printf("\n\n");
printf(" P /_\ P \n");
printf(" /_\_|_|_/_\ \n");
printf(" n_n | ||. .|| | n_n Bem-vindo ao \n");
printf(" |_|_|nnnn nnnn|_|_| Jogo de Adivinhação!\n");
printf(" |" " | |_| |" " | \n");
printf(" |_____| ' _ ' |_____| \n");
printf(" \__|_|__/ \n");
printf("\n\n");
ASCIIA rt
Você consegue facilmente achar desenhos como esse no Google.
Bastaprocurarpor“asciiart”.
Ocabe çalhoémuitomaisbonito;entretanto,seocompilarmos,teremos
problemas.Ocompiladornosdaráumerroparecidocomesse:
adivinhacao.c:9:25: warning: unknown escape sequence '\ '
printf(" P /_\ P \n");
^~
Elereclamoudo \. Estecaracteredentrodo printféespecial. Afi-
nal,quandoqueremospularumalinha,usamos \n. Masesequisermos
realmenteimprimi-lo?Precisaremosdobrá-lo,ouseja,escrever \\.Vamos
65

## Página 77

6.3. Embelezandoojogo CasadoCódigo
corrigirodesenhodonossocastelo,dobrandotodasasbarrasnecessárias.A
mesmacoisacomasaspas,poisprecisamosfazer \"sequisermosimprimi-
lasnatela(casocontrário,ocompiladorpodeconfundireacharqueaquela
aspasestáfechandoaaspasabertaanteriormente).
Apesardeodesenhoterficadotortonocódigo,quandooexecutarmos,
eleficarácerto:
printf("\n\n");
printf(" P /_\\ P \n");
printf(" /_\\_|_|_/_\\ \n");
printf(" n_n | ||. .|| | n_n Bem-vindo ao \n");
printf(" |_|_|nnnn nnnn|_|_| Jogo de Adivinhação! \n");
printf(" |\" \" | |_| |\" \" | \n");
printf(" |_____| ' _ ' |_____| \n");
printf(" \\__|_|__/ \n");
printf("\n\n");
Eagora,jáquemostramosatentativaemqueeleestá,nãoprecisamos
maisficarmostrando“QualoseuXo. chute?”. Aperguntapodesermais
simples. Tambémnãoémaisnecessárioexibironúmerochutado,afinalo
usuárioqueodigitou,eelejáficanatela:
// antes
printf("Tentativa %d de %d\n", i, totaldetentativas);
printf("Qual é o seu %do. chute? ", i);
// depois
printf("-> Tentativa %d de %d\n", i, totaldetentativas);
printf("Chute um número: ");
Vamostambémexibirumamensagemdevitóriaouderrotamaisbonita,
usandoASCIIArtnovamente. Umarápidagooglada,etemosdesenhosde
umacaradefelicidadeedeumacareta,ideaisparaamensagemquequeremos
passar. Tambémexibiremosaquantidadedepontossomenteseojogador
ganhouojogo:
printf("\n" );
if(acertou) {
66

## Página 78

CasadoCódigo Capítulo6. Finalizandoojogo
printf(" OOOOOOOOOOO \n");
printf(" OOOOOOOOOOOOOOOOOOO \n");
printf(" OOOOOO OOOOOOOOO OOOOOO \n");
printf(" OOOOOO OOOOO OOOOOO \n");
printf(" OOOOOOOO # OOOOO # OOOOOOOO \n");
printf(" OOOOOOOOOO OOOOOOO OOOOOOOOOO \n");
printf("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO \n");
printf("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO \n");
printf("OOOO OOOOOOOOOOOOOOOOOOOOOOOOO OOOO \n");
printf(" OOOO OOOOOOOOOOOOOOOOOOOOOOO OOOO \n");
printf(" OOOO OOOOOOOOOOOOOOOOOOOO OOOO \n");
printf(" OOOOO OOOOOOOOOOOOOOO OOOO \n");
printf(" OOOOOO OOOOOOOOO OOOOOO \n");
printf(" OOOOOO OOOOOO \n");
printf(" OOOOOOOOOOOO \n");
printf("\nParabéns! Você acertou!\n");
printf("Você fez %.2f pontos. Até a próxima!\n\n", pontos);
} else {
printf(" \\|/ ____ \\|/ \n" );
printf(" @~/ ,. \\~@ \n");
printf(" /_( \\__/ )_\\ \n" );
printf(" \\__U_/ \n");
printf("\nVocê perdeu! Tente novamente!\n\n");
}
6.4 Acabamos o primeiro jogo!
Terminamosnossoprimeirojogo! Viusócomonãofoidifícil? Masainda
temosmuitacoisaparaaprendersobrealinguagemC.Nopróximocapítulo,
começaremosonossopróximojogo,ojogodeforca. Elenosfaráaprender
maiscoisasainda.
Atélá!
Código final
Ocódigofinaldojogopodeservistoaqui:
http://pastebin.com/SBe41fgB
67

## Página 79

6.5. Resumindo CasadoCódigo
6.5 Resumindo
Nestecapítulo,aprendemos:
•Switche casecomoalternativasparaalgunscasosdo if;
• Queprecisamosescaparbarraseaspassequisermosimprimi-lasno
printf;
• Queinterfaceéimportanteequeconseguimosfazerprogramasbonitos
mesmonoconsole.
68

## Página 80

Capítulo7
Exercícios
Agoraésuavezdepraticar! Vejaosexercíciosaseguiretenteresolvê-los.
Algunsdelessãomelhoriasnoprópriojogodeadivinhaç ão;outrossãonovos
programas,evocêdevefazê-losemumarquivoseparado.
7.1 Melhorando o jogo de adivinhação
1) Hojeojogoescolheumnúmeroentre0e99.Deixeousuárioescolheresse
limite.Vocêprecisacapturaressesdoisnúmerosdele,eusá-losnahorade
calcularonúmerorandômico.
2) Temosaindaalgunsnúmerosmágicosemnossocódigo.Use #defines
paraaquantidadedetentativasporníveisequantidadedepontosinicial.
3) Aoterminarumapartida,pergunteparaousuárioseelequerjogarnova-
mente.Seeledigitar“1”,significaquequer,entãovocêdeverácomeçaro

## Página 81

7.2. Outrosdesafios CasadoCódigo
jogodenovo.Paraisso,vocêprecisaráusarmaisumloop.
4) Nãodeixeousuáriojogaromesmonúmeronasequência.Seelejogouo
número“2”,errou,ejogounovamenteo“2”,avise-odequeelejájogouesse
número,enãocontecomoumatentativa.Paraisso,crieumavariávelque
guardaráo“últimonúmerochutado”.(Não tente guardar todos os números
chutados nesse momento. Aprenderemos como fazer isso mais para frente.)
7.2 Outros desafios
1) Escrevaumprogramaqueimprimatodososnúmerosparesentre2e50.
Parasaberseonúmeroépar,bastavocêverseorestodadivisãodonú-
meropor2éiguala0.
2) Escrevaumprogramaqueimprimaasomadetodososnúmerosde1até
100. Ouseja,elecalcularáoresultadode 1 + 2 + 3 + 4 + ... +
100.
3) Escrevaumprogramaquepe çauminteiroaousuário,ecomesseinteiro,
eleimprima,linhaalinha,atabuadadaquelenúmeroatéo10.Porexem-
plo,seeleescolheronúmero2,oprogramaimprimirá: 2x1=2, 2x2=4,
2x3=6, ..., 2x10=20.
4) Implementeumacalculadora.Oprogramadevepedir3númerosaousuá-
rio: a, be operacao.Se operacaoforiguala1,vocêdeveráimprimir
asomade a+ b.Seelafor2,asubtraç ão.Sefor3,amultiplicaç ão.Sefor
4,adivisão.
5) Escrevaumprogramaquepe çaumnúmerointeiroaousuárioeimprima
ofatorialdessenúmero. Paracalcularofatorial,bastairmultiplicando
pelosnúmerosanterioresaté1.Porexemplo,ofatorialde4é 4 * 3 * 2
* 1,queéiguala24.
6) Dadostrêsnúmeros,imprimi-losemordemcrescente.
70

## Página 82

Capítulo8
Jogodeforca
Nossopróximoobjetivoédesenvolverumjogodeforca.Ocomputadores-
colherá,demaneirarandômica,umapalavraqueestásalvaemumarquivo

## Página 83

8.1. Comoeleficará? CasadoCódigo
depalavras;eojogadordevechutar,letraporletra,atéadivinhá-la.Seojo-
gadorchutar5letraserradas,eleperde. Aofinal,ocomputadorofereceráa
possibilidadedeousuárioinserirumanovapalavranobancodedados.
Nestescapítulos,aideiaéensinarvocêa:
• Criar,varreremanipulararraysdediferentestipos.
• Usararraysdechars(strings)efun çõesparamanipulá-los.
• Entenderecriarfunçõesquerecebemparâmetrosedevolvemvalores.
• Lereescreverarquivoscomformatosespecíficos.
• Aprendermaisboaspráticasdecódigo,comoacriaçãoeextraç ãode
funçõesparaevitarrepetiç ãodecódigo.
• Criarheader files.
8.1 Como ele ficará?
Nossojogotambémteráumainterfaceamigável. Aoiniciar,elenosdará
boas-vindaseimprimiráaforca,porenquanto,semninguém:
/****************/
/ Jogo de Forca */
/****************/
_______
|/ |
|
|
|
|
|
_|___
_ _ _ _ _ _ _ _ _
Qual letra?
72

## Página 84

CasadoCódigo Capítulo8. Jogodeforca
Sevocêchutarumaletraerrada,eleoavisaráeohomenzinhocome çará
aaparecernaforca:
Você errou: a palavra NÃO tem a letra X
_______
|/ |
| (_)
|
|
|
|
_|___
_ _ _ _ _ _ _ _ _
Qual letra?
Sevocêchutarumaletracerta,aletraapareceentreovazado:
Qual letra? A
Você acertou: a palavra tem a letra A
_______
|/ |
|
|
|
|
|
_|___
_ _ _ _ _ A _ _ A
Qual letra?
Sevocêperder,eleteenforcaráporcompleto:
_______
|/ |
73

## Página 85

8.1. Comoeleficará? CasadoCódigo
| (_)
| \|/
| |
| / \
|
_|___
Umacaveiratambémaparecerá,avisandoqueojogoacabou:
Puxa, você foi enforcado!
_______________
/ \
/ \
// \/\
\| XXXX XXXX | /
| XXXX XXXX |/
| XXX XXX |
| |
\__ XXX __/
|\ XXX /|
| | | |
| I I I I I I I |
| I I I I I I |
\_ _/
\_ _/
\_______/
Esevocêganhar,umtroféuaparecerá:
Parabéns, você ganhou!
___________
'._==_==_=_.'
.-\: /-.
| (|:. |) |
'-|:. |-'
\::. /
'::. .'
) (
74

## Página 86

CasadoCódigo Capítulo8. Jogodeforca
_.' '._
'-------'
8.2 É hora de começar!
Estáprontoparadesenvolveressejogo? Mãosàobra!
75

## Página 88

Capítulo9
Arrays
Parasecome çarumjogodeforca,umamaneiraanálogaaonossojogode
adivinhaçãoéguardarapalavrasecreta. Atéagora,jáconhecemosdiversos
tiposdevariáveis,como int, double, float, long;porémaindanão
vimosotipousadoparaseguardarumtexto.
EmC,paraguardarmosumaúnicaletra,usamosotipo char. Eleé
declaradodamesmaformaqueosoutros. Mas,parasepassaraletraaser
armazenada,usamosaspassimples;eparaimprimir,usamosamáscara cno
printf.Vejaocódigoaseguir:
# include <stdio.h>
int main() {
char letra1 = 'M';
char letra2 = 'F';
char letra3 = 'A';

## Página 89

CasadoCódigo
printf("%c %c %c" , letra1, letra2, letra3);
}
Elenosimprimeasletras“M”,“F”e“A”.Maseparaguardarumapalavra?
Seráqueprecisamosarmazenarletraporletra? Arespostaé:sim. Precisa-
mosguardarumaauma;porém,paraisso,nãoteremosumavariáveldife-
renteparacadaletra.Aliás,setivéssemos,ficaríamosmalucos.Imaginepara
guardarumtextointeiro?Quantasvariáveisteríamos?
Eopior,nãoconseguiríamosfazercódigosdinâmicosparaimprimirpa-
lavrasdetamanhosdiferentes.Nãopodemosescreverum for,porexemplo,
paraimprimirasváriasletras:
// imagine uma palavra com 10 letras
for(int i = 1; i <= 10; i++) {
// não temos uma maneira de "gerar dinamicamente"
// o nome da variável a ser impressa.
// Ou seja, não conseguimos imprimir "letra1",
// depois "letra2", e assim por diante.
printf("%c", letra(i));
}
Oqueusaremosparaissoéoquechamamosde array.Arrayssãouma
maneiradeguardarmos“vários”deumsótipo.Esseselementosficamarma-
zenadasnamemória,umaoladodooutro.Porexemplo,umarraydeinteiros
guardaummontedenúmerosinteiros.Umarrayde charguardaummonte
decaracteres,eassimpordiante.Avantagemdoarrayéque,nomomentoda
declaração,dizemososeutamanhoeacessamoscadaumdesseselementos
pormeiodeumíndice.
Veja,porexemplo,umadeclaraç ãodeumarraydeinteiros,com5posi-
ções.Notequeadeclaraç ãoéidêntica,comexce çãodousodoscolchetes:
int notas[5];
Agora,parausaressearray,guardandoelendoseusinteiros,bastausar-
mososcolchetesparadefinirmosaposiç ãoquequeremosacessar. Afinal,
temos5. Oúnicodetalheimportanteéque,senossoarraytem5posições,
78

## Página 90

CasadoCódigo Capítulo9. Arrays
elasvãode0a4. Aprimeiraposiç ãodeumarrayéo0(enãoo1,como
muitosconfundem):
// guardando na primeira posição do array
notas[0] = 10;
// guardando na segunda posição
notas[1] = 5;
// imprimindo a primeira posição
printf("%d", notas[0]);
9.1 Strings e array de chars
Paraguardarmosnossapalavrasecreta,vamosdeclararumarraydechar.Va-
mosdefinirseutamanhocomo20:
char palavrasecreta[20];
Podemosguardarnossapalavradentrodele,damesmaformacomoes-
távamosfazendoantes.Adiferen çaéqueonúmeroquepassamosentrecol-
chetespodevirdeumavariável:
char palavrasecreta[20];
palavrasecreta[0] = 'M';
palavrasecreta[1] = 'E';
palavrasecreta[2] = 'L';
int numero = 3;
palavrasecreta[numero] = 'A';
palavrasecreta[4] = 'N';
palavrasecreta[5] = 'C';
palavrasecreta[6] = 'I';
palavrasecreta[7] = 'A';
Umtrabalhão.Paraimprimirapalavra,ficaumpoucomaisfácil.Afinal,
comopodemosusarvariáveisalinoíndice,conseguimosfazerumloopcom
otamanhodapalavra:
79

## Página 91

9.1. Stringsearraydechars CasadoCódigo
for(int i = 0; i < 8; i++) {
printf("%c", palavrasecreta[i]);
}
Entretanto,umarraydecharéumarrayespecial. Comonósousamos
paraguardartextos,temosfun çõesespecializadasparafacilitarnossavidana
horadecolocardadosdentrodele. Essasfun çõestambémvãonosajudara
escreverloopsmaisflexíveis(o8alinocódigoestáfixo,masqueremosque
eleseadapteaotamanhodapalavra).
Afun ção sprintf()émuitoparecidacoma printf().Enquantoo
printfimprimenatela,a sprintfimprimeemumarraydechars(o sé
justamentede string).Logo,sequisermosguardarapalavrasecretanoarray,
fazemos:
sprintf(palavrasecreta, "MELANCIA" );
Paraimprimirmosnatela,usamoso printfcomamáscara s.Elafaz
comquetodooarraysejaimpresso:
printf("%s" , palavrasecreta);
Entretanto,vejaqueinteressante.Nossoarraytem20posiçõeseapalavra
“melancia”temapenas8caracteres. Comoqueelesoubequedeveriaparar
noúltimo“a"? Porqueelenãoimprimiu20caracteres? StringsemCtêm
umpequenodetalhe:semprequeguardamosumapalavralácomomelancia,
queocupa8posições,guardamosumcaractereespecialna9ªposiç ão.Esse
caracterenosdizqueastringacabaali,equeorestoé“lixo”.Eleérepresentado
pelosímbolo `(barrazero).Apesardeseremdoiscaracteres,lembre-sede
queobarraéespecial.Esse `éarmazenadoemumaúnicaposiç ão.
Ouseja,quandofizemoso sprintf(),eleescreveunaverdadeotexto
MELANCIA`.Afun ção printf(),sabendodisso,foilendooarraydechars
atéencontraro `.Encontrou,parou.
Seestivéssemosdeclarandoasletrasdessapalavraumaauma,igualfize-
mosanteriormente,bastariaadicionaro `aofinal,queo printf("%s")
funcionarianormalmente:
80

## Página 92

CasadoCódigo Capítulo9. Arrays
char palavrasecreta[20];
palavrasecreta[0] = 'M';
palavrasecreta[1] = 'E';
palavrasecreta[2] = 'L';
palavrasecreta[3] = 'A';
palavrasecreta[4] = 'N';
palavrasecreta[5] = 'C';
palavrasecreta[6] = 'I';
palavrasecreta[7] = 'A';
// colocando o \0 para indicar que a string acabou
palavrasecreta[8] = '\0';
9.2 Varrendo o array
Vamoscome çarnossojogo.Assimcomooanterior,eleteráumloopprinci-
pal.Aideiaéque,enquantoelenãoacertarapalavra,ounãomorrerenfor-
cado,continuamosapedirumaletraaele.Vamoscriarduasvariáveis,uma
chamada acertou,eoutrachamada enforcou.Ambasserãobooleanos;
ouseja,guardarão0ou1,indicandoseojogadorganhououfoienforcado,
respectivamente.
Atéentão,aprendemosdoistiposdeloops:o foreo while.Ambos,
antesdeexecutaremocorpodecódigoquepossuem,elesvalidamacondiç ão.
Issoquerdizerque,seacondiç ãodo whileforfalsadesdeocome ço,o
códigonãoseráexecutadonenhumavez. Masnessenossocaso(enojogo
anteriortambém),aomenosumavezprecisamosrodaroblocodecódigo.
Podemosfazerusodo do-while,umoutrotipodeloop,idênticoao
while,comaexce çãodequeeleexecutaoblocodecódigoaomenosumavez.
Reparenacondiç ão while(!acertou && !enforcou). Conseguimos
lê-laemportuguês:enquanto não acertou E não enforcou.
int acertou = 0;
int enforcou = 0;
do {
81

## Página 93

9.2. Varrendooarray CasadoCódigo
// código aqui
} while(!acertou && !enforcou);
Invertendo booleanos
Percebaqueaexclamaç ãopodeserusadapara“negar”(ouinverter)
ovalordeumbooleano. Vejaocódigoaseguir,ondedeclaramosdois
inteiros, verdadeiroe falso,colocando1e0dentrodeles.Emse-
guida,imprimimosambosduasvezes;umaveznormal,eaoutrausando
aexclamaçãoparainverterovalor.
int verdadeiro = 1;
int falso = 0;
printf("%d %d" , verdadeiro, !verdadeiro);
printf("%d %d" , falso, !falso);
Reparequeoprogramaimprimirá 1 0naprimeiralinha,e 0 1na
segunda.Ouseja,eleinverteovalor.Usamosaexclamaç ãoparaconse-
guirmosescrevermaisclaraesucintamenteexpressõesbooleanas.
Omesmolooppoderiatersidofeitousandoacomparaç ãocom0
(falso).Porém,vejacomoescrevemosmaiscódigodessaforma:
while(acertou == 0 && enforcou == 0);
Vamosagoracapturarumaletradousuário,everseelaexistenapala-
vrasecreta. Paraisso,precisaremosfazerum fornapalavra(afinal,sabe-
mosotamanhodela),ecompararseo charqueestánaquelaposiçãobate
comoinformadopelousuário. Paracapturarotamanhodapalavradentro
deumarraydechars,usamosafun ção strlen(). Elaestádisponívelem
<string.h>.
A usaremos nofor, que irá de 0 (primeira posição do array) até
strlen(),queéaúltimaposiç ãopreenchida.Emseguida,compararemos
oconteúdodaquelaposiç ãocomochutedado,eavisaremosousuárioseele
acertouochute:
82

## Página 94

CasadoCódigo Capítulo9. Arrays
do {
char chute;
printf("Qual letra? ");
scanf("%c", & chute);
for(int i = 0; i < strlen(palavrasecreta); i++) {
if(palavrasecreta[i] == chute) {
printf("A posição %d tem essa letra\n", i+1);
}
}
} while (!acertou && !enforcou);
Asaídadoprograma,nessemomento,éaseguinte:
Qual letra? A
A posição 4 tem essa letra
A posição 8 tem essa letra
Qual letra? Qual letra? M
A posição 1 tem essa letra
Qual letra? Qual letra? E
A posição 2 tem essa letra
Qual letra? Qual letra? L
A posição 3 tem essa letra
Aindalongedoideal,masjáéumcome ço.Agora,reparecomaten ção,e
vejaqueeleescreveu“Qualaletra?”duasvezes,váriasvezes?Temosumbug
aí. Issoaconteceuporummotivobastantediferente. Vejaquesempreque
usávamoso scanf(),digitávamosumnúmero,porexemplo,edávamos
enter.O scanféinteligenteesabeque enternãofazpartedonúmero.
Mas,agoraqueestamoslendoumcaractereúnico,um enteréconsiderado
umcaractere.O scanf()seperdequandodigitamosumaletraeum enter.
O enterficade buffer,equandoexecutamoso scanf()pelasegundavez,
elenemnospedealetraepassao enterdireto.
Pararesolverisso,precisamosmudarumpoucoamáscara. Emvezde
passarmosapenaso "%c",passaremos " %c".Reparenoespaço.Eledizao
scanf()paraignoraro enter.Issoresolveoproblema:
scanf(" %c", &chute);
83

## Página 95

9.3. Laçosencadeados CasadoCódigo
Asaídaagora,comoesperado:
Qual letra? A
A posição 4 tem essa letra
A posição 8 tem essa letra
Qual letra? M
A posição 1 tem essa letra
Qual letra? E
A posição 2 tem essa letra
Qual letra? L
A posição 3 tem essa letra
Está perdido?
O código até este ponto está em
http://pastebin.com/jyLuQWd2
9.3 Laços encadeados
Precisamosagoramostrarparaousuárioapalavra,masdemaneiraescon-
dida.Ouseja,umasequênciade _ _ _ _,um underscoreporletra.Àme-
didaqueojogadoracertaumaletra,abrimosessacasa.Vamoscome çarde-
vagar,imprimindoapalavraescondida.
Ocódigoéparecidocomoloopanterior.Precisamospassarporcadaletra
dapalavrasecreta,eimprimirounderscore:
do {
for(int i = 0; i < strlen(palavrasecreta); i++) {
printf("_ ");
}
printf("\n");
}
Agora,precisamospensaremabriraletraqueelejáacertou. Paraisso,
precisamosguardartodososseuschutes.Paraguardarmuitoschars,vocêjá
84

## Página 96

CasadoCódigo Capítulo9. Arrays
sabe:array.Vamosdeclararumarrayresponsávelporguardarcadaumdos
chutesdousuário,eumavariávelquecontaonúmerodechutesjádados.
Essavariávelseráespecialmenteimportante,pois,alémdeindicaraquanti-
dade,elanosindicaráaposiç ãodessearrayqueoúltimochutedadodeveser
guardado.
Porexemplo,imagineoarray chuteseointeiro tentativas,inicia-
lizadocom0.Quando tentativasforiguala0,querdizerqueousuário
deu0chutes,eoprimeirochutedeveserguardadoem chutes[0].Quando
tentativasforiguala1,issoquerdizerqueousuáriodeu1chute,eopró-
ximochutedeveserguardadoem chutes[1].Quandoquisermosvertodos
oschutes,podemostambémfazerum forquevaide0a tentativas.
Vamoscome çardeclarandoessasvariáveis,antesdo do-while:
char chutes[26];
int tentativas = 0;
Agora,vamoscome çarasalvaroschutesdousuárionessearray. Logo
apóscapturarmosocharno scanf(),vamosguardá-lonoarray.Jásabemos
queaposiç ãolivredoarrayestánavariável tentativas:
char chute;
printf("Qual letra? ");
scanf(" %c", &chute);
chutes[tentativas] = chute;
tentativas ++;
Agoravamosvoltaraonossoloopanteriorqueexibeapalavraescondida.
Precisamosdealgumainteligênciaali: seousuáriojáchutouaquelaletra,
precisamosexibi-la;esenuncachutou,exibimosounderscore. Paraisso,
paracadaletradapalavrasecreta,precisamosfazerumloopdentrodoarray
dechutes,everseelaestálá.
Esseloopprecisaterumavariáveldefora,tomandocontadoresultado.
Afinal,seacharmosaletra,emqualquerposiç ãodoarray,devemospará-loe
imprimi-la.Caso,apóspassarmosemtodooarrayeoloopacabar,ealetra
nãoestiverlá,exibimosounderscore.
85

## Página 97

9.3. Laçosencadeados CasadoCódigo
Veja,emcódigo,avariável achou,quevalerá1,seacharmosaletrano
arraydechutes.Vamoscolocaraimpressãologonocome çodo do-while,
eremovero forquetínhamosmaisembaixo(afinal,precisamosmostrara
forcaantesdepedirapróximaletra).Reparetambémqueusamosaletra j
paraoloopdedentro,vistoqueavariável ijáestásendousadapeloloopde
fora:
do {
for(int i = 0; i < strlen(palavrasecreta); i++) {
int achou = 0;
for(int j = 0; j < tentativas; j++ ) {
if(chutes[j] == palavrasecreta[i]) {
achou = 1;
break;
}
}
if(achou) {
printf("%c ", palavrasecreta[i]);
} else {
printf("_ ");
}
}
printf("\n");
// ...
}
Vejaqueo foraninhado ouseja,o forqueestádentrodo for ini-
cializaumavariável jquevariade0atéaquantidadede tentativasjá
dadas. Emseguida,elecomparasealetraqueestáem chutes[j]éigual
aqueestáem palavrasecreta[i]. Repareque jvaivariarde0atéo
númerodechutes,enquanto ivaivaler0.Depois, jvariaránovamentede
0atéonúmerodechutes,enquanto ivalerá1,eassimpordiante.Ouseja,
compararemostodoscomtodos.
Vamosfazeroquechamamosde testedemesa,istoé,simularnossocó-
86

## Página 98

CasadoCódigo Capítulo9. Arrays
digonopapel. Imaginequeapalavrasecretaseja "MAO",equeoschutes
dadosforam“X”e“A”(aquantidadedetentativas,nessemomento,é2).
1) i=0,j=0,palavrasecreta[0]é‘M’echutes[0]=‘X’.MnãoéX,oloop
continua.
2) i=0,j=1,palavrasecreta[0]é‘M’echutes[1]=‘A’.MnãoéA,oloop
continua.
3) iéincrementado.
4) i=1,j=0,palavrasecreta[1]é‘A’echutes[0]=‘X’.AnãoéX,oloopcon-
tinua.
5) i=1,j=1,palavrasecreta[1]é‘A’echutes[1]=‘A’.AéA,oloopéquebrado,
achou=1,letraéimpressa.
6) iéincrementado.
7) i=2,j=0,palavrasecreta[1]é‘O’echutes[0]=‘X’.OnãoéX,oloop
continua.
8) i=2,j=1,palavrasecreta[1]é‘O’echutes[1]=‘A’.OnãoéA,oloopconti-
nua.
9) Loopmaiortermina.
Loopsdentrodeloopspodemparecercomplicadosnocome ço. Usee
abusedetestesdemesa. Coloqueasvariáveisqueestãodefinidasnaquele
momento,evátrocandoumaauma.Sequiser,coloque printfsnocódigo,
imprimindoasvariáveis i, j,equaisqueroutrasquequiserparaajudá-lono
entendimento.
Nestemomento,nossojogojáseparecemaiscomumjogodeforca. O
usuárioconseguechutarletras,evamosasmostrandoconformeeleacerta.
Estamoscaminhandobem.
87

## Página 99

9.4. Resumindo CasadoCódigo
Está perdido?
Vocêpodeverocódigoatéestemomentoem
http://pastebin.com/ctVzUyqy
9.4 R esumindo
Nestecapítulo,vocêaprendeu:
• Oquesãoarrays;
• Comodeclarararrays;
• Comoescreverdentrodearrays;
• Comopegaroconteúdodeumaposiçãodoarray;
• Queasposiçõesdoarraycomeçamno0,enãono1;
• Quearraysdecharsãoarrayscomoqualqueroutro;
• Queseguardamosumastringemumarraydechar,ocaractere `deve
sercolocadoaofimdapalavra;
• Quepodemoscolocarloopsdentrodeloops.
88

## Página 100

Capítulo10
Númerosbinários
Vimosatéentãoquetodasasvariáveisquedeclaramos,sejamelassimplesou
arrays,ficamarmazenadasnamemóriadocomputador.Aperguntaé:como
elefazisso?Comoeleguarda,porexemplo,umnúmero,dentrodaquelape ça
dehardwarequechamamosdememória?
Acrediteounão,umamemóriadecomputadorconsegueapenasdiferen-
ciarduascoisas:sealgoestáimantadoparaumladoouparaooutro.Aum
dosladosatribuímosovalor1,eaooutro,ovalor0.Ouseja,amemóriade
umcomputadornãoconsegueguardarumnúmerocomo“42”,poiselanão
consegueguardarnem“4”nem“2”.Elaconsegueguardarapenas“1"se“0"s.E
aívemodesafio:precisamosrepresentarqualquercoisausandoapenasesses
doisnúmeros.
Vamosvercomoissofuncionadevagar. Imagineonúmero0, como
representá-lo? Fácil: 0. Eonúmero1? Tambéméfácil,1. Pronto,temos
umbit.

## Página 101

CasadoCódigo
Odesafiocome çaquandoqueremosrepresentaronúmero2,usandoso-
menteosnúmeros0e1.Asoluç ãoéusaro10pararepresentaronúmero2.
Cuidado.Nãoleia 10comodez,leiacomo“umzero”,afinalelenãovale“dez”.
Eonúmerotrês?11.Istoé,“umum”.Edepoisonúmeroquatro?100.Depois
101,110,111.
Ficamoscomumatabela:
0 => 0
1 => 1
2 => 10
3 => 11
4 => 100
5 => 101
6 => 110
7 => 111
8 => 1000
...
Reparequeacontaaquiéparecidacomaquefazemoscombasedecimal
(queéabasequeusamos,ouseja,representandotodososnúmerospossíveis
usandoapenasde0a9).Vejaquenãotemosum“desenho”paraonúmero
dez.Oquefazemosquandochegamosnomaiornúmerodanossaescala(que
nocasoé9)?Empurramosumdígitoparaesquerda,ecome çamosacontagem
denovo:10,11,12,13,eassimpordiante.
Comnúmerosbinários,éamesmacoisa. Tínhamoso0,edepoiso1.
Como1éomaiordígitoquetemos,empurramosumdígitoparaaesquerda
ecome çamosacontagemdenovo:0,1,10,11,100,101,110,111,eassimpor
diante.
Assimcomonamatemáticatradicional,podemospreenchercomzeroà
esquerdaparapadronizaraquantidadededígitos.Porexemplo,seusarmos
8dígitos ouseja,8bits,temos:
0 => 00000000
1 => 00000001
2 => 00000010
3 => 00000011
4 => 00000100
90

## Página 102

CasadoCódigo Capítulo10. Númerosbinários
5 => 00000101
6 => 00000110
7 => 00000111
8 => 00001000
9 => 00001001
10 => 00001010
11 => 00001011
12 => 00001100
13 => 00001101
14 => 00001110
15 => 00001111
Oconjuntode8bitsjuntoséconhecidopor1byte. Podemosseguiro
mesmopadrãoatéqualquernúmerointeiro. UminteiroemCtem4bytes.
Issoquerdizerqueusamos 4 vezes 8=32bits.Com32dígitos,consegui-
mosrepresentarnúmerosbastantegrandes.
10.1 Binário e letras
Mascomorepresentarletras(chars)?Bastafazermosumatabela,dandoum
númeroparacadaletra.Porexemplo,‘A=65’.Então‘B=66’,‘C=67’:
A => 65 => 01000001
B => 66 => 01000010
C => 67 => 01000011
...
Z => 90 => 01011010
Pronto,ocomputadorécapazderepresentartodasasletrasexistentes
nonossoalfabetousandosomente8dígitos,0ou1. Essatabeladonosso
alfabeto,incluindodiversosoutroscaractereséa tabelaASCII,usadapor
muitotempocomooprincipalpadrãodetraduç ãodenúmerosecaracteres
porumcomputador.
10.2 Bits:8,16,32,64
Setivéssemosapenas8bitspararepresentarumnúmerointeiro,podería-
mosrepresentar 2 elevado a 8números,queéiguala256.Parecepouco,
91

## Página 103

10.3. Bitsenúmeroscompontoflutuante CasadoCódigo
masacrediteounão,nossosprimeirosvideogames,comooMasterSystem,
tinhamprocessadoresde8bitsesabiamsórepresentarnúmerosde0a255.
OMegaDrivetinhaumprocessadorumpoucomelhorde16bits,ecom
isso,representavanúmerosinteirosde0a65.535(ouseja, 2 elevado a 16
númerosdiferentes). NãoéàtoaqueosjogosdoMastertinham,emgeral,
nomáximo256cores,enquantoasdoMegatinhamaté65mil.
Masmesmoessenúmero,seráqueeleécapazderepresentartodosos
númerosinteirosquequeremos?Ouaindaumprocessadorcapazdeentender
earmazenar16bitstambémestáaptopararepresentartodasasletrasdetodos
osalfabetosdomundo?
Osprocessadoresmodernossãocapazesderepresentarnúmeroscomaté
64bits oquedábonsbilhões,alémdetodooconjuntodecaracteresdos
alfabetosexistentesnomundo. Mesmoassim,existemotimizaçõesparare-
presentaroalfabeto,comoumpadrãofamosoportersubstituídooASCII,
sendoomaisutilizadonainternetem2008,oUTF-8.
10.3 Bits e números com ponto flutuante
Agoratemosaquestãodosnúmeroscompontoflutuante.Comorepresentar
taisnúmeros,seocomputadorsóconhecezeroseuns?Domesmojeitoque
fizemoscomasletras,precisamosdealgumpadrão. Paraentendermelhor,
vamoscriaronossoprópriopadrão,maissimplesdoqueumusadohojeem
dia.
Imagineonúmerotrezeemeio(13,5).Quantosdígitoselepossuiantesda
casadecimal?Dois(embinário, 0010).Quaissãoessesdígitos? 1(0001)
e 3( 0011). Porfim,ovalordacasadecimalé 5( 0101). Portanto,para
representaronúmero 13,5,utilizaremosanotaç ãoqueindicaonúmerode
casasantesdavírgula( 2),oseuvalor dígitoadígito( 1e 3),eovalor
decimal( 5):
0010 0001 0011 0101
Pronto.Ocomputadorécapazdeentendernúmeroscomo 13,5.Com
isso,somoscapazesderepresentarqualquernúmerocomcasasdecimais,cuja
quantidadededígitoséfinita,mesmoqueessatécnicaestejalongedeser
ótimaouperfeita.
92

## Página 104

CasadoCódigo Capítulo10. Númerosbinários
Entretanto,aindatemosumalimitaç ão:nestetipodeabordagem,como
representarovalor 1 / 3,istoé,umter ço?Essenúmerotemumaquanti-
dadeinfinitadedígitos.
Umaprimeiraop çãoseriaarredondarmosonúmero 0,3,perdendopre-
cisão:
0001 0000 0011
Jáqueoarredondamentofoiruim,podemostentarmelhorá-lo 0,33:
0001 0000 0011 0011
Oumaisainda, 0,333:
0001 0000 0011 0011 0011
Comoocomputadorcostumaseguirpadrõesdetamanhofixo,écomum
queonúmerodepontoflutuante,assimcomoumnúmerointeiro,utilize64
bits.Issolimitaanossaaproximaç ão.Paranossoumter ço,usandoessaideia
apresentada(nãoideal),temosamelhoraproximaç ãode 0,333.3com 62
casasapósavírgula.
0001 0000 0011 0011 0011 ... 0011
Nossaabordagemébastantelimitada,masarepresentaç ãoescolhidapor
umprocessadorébemmaisinteligentequeessaepermiteaproximações
muitoboas.
10.4 Hexadecimal
Abasebinária,comovimos,temsomentedoisalgarismosdistintosparare-
presentar todososnúmeros.Aqueusamosnodiaadiatemdezalgarismos.
Entretanto,háumaoutrabasebastanteutilizada,abase hexadecimal,que
tem16algarismos.Pararepresentarnúmerosde0a15,precisamosapenasde
4bits.
Agoraprecisamosde16“desenhos”pararepresentaros16possíveisalga-
rismos.Paraissocompletamososnúmerosde0a9comasletrasA,B,C,D,
93

## Página 105

10.5. Bitseimagens CasadoCódigo
EeFpararepresentarosoutrosseisalgarismosfaltantes.Novamente,sema
necessidadededecorarafórmuladetransformaç ão,atabelaaseguirmostra
os 16primeirosnúmerosembasehexadecimal:
0 => 0
1 => 1
2 => 2
3 => 3
4 => 4
5 => 5
6 => 6
7 => 7
8 => 8
9 => 9
10 => A
11 => B
12 => C
13 => D
14 => E
15 => F
Poderíamoscontinuarcom:
16 => 10
17 => 11
18 => 12
...
32 => 21
...
177 => B1
...
255 => FF
Portanto,comdoisalgarismosdebasehexadecimal(16possibilidades
cada),conseguimosrepresentar 16 * 16,256,números.
10.5 Bits e imagens
Agora,umúltimodesafio:comorepresentarumaimagem?Éfácil.Mapea-
remosumaimagemparaumconjuntodenúmerosinteiros.Jásabemosque
94

## Página 106

CasadoCódigo Capítulo10. Númerosbinários
conseguimosrepresentarnúmerosinteirosdeformabinária.
Imagineumafoto.Elaécompostapordiversospontos,sendoquecada
umdelestemumacordiferente.Suponhaqueafototem1000por1000pon-
tos.Oquepodemosfazeréprimeiroenumerartodasascoresexistentes.Mas
vamoslimitá-lasa256diferentes:
cor0 = verde
cor1 = vermelho
cor2 = azul
cor3 = preto
cor4 = branco
...
cor255 = cinza
Nãopodemosusaronomedacor:precisamosdarumnúmeroaela.Por
exemplo:
cor0 = 00FF00 (verde)
cor1 = FF0000 (vermelho)
cor2 = 0000FF (azul)
cor3 = 000000 (preto)
cor4 = FFFFFF (branco)
...
cor255 = CCCCCC (cinza)
Comessatabelaemmãos,podemosescreverumalinhaparacadaponto
nafoto. Seoprimeiropontoévermelho(cor1),osegundoazul(cor2)eo
terceirocinza(cor255),emumaimagemcomdiversaslinhas,temos:
cor1 cor2 cor255 cor3 cor3 cor2 cor3 cor255
cor1 cor3 cor255 cor3 cor2 cor3 cor3 cor255
...
Mas como sabemos que temos, no máximo, 256 cores, podemos
representá-lasmaisfacilmentecomnúmerosemhexadecimal:
01 02 FF 03 03 02 03 FF
01 03 FF 03 02 03 03 FF
...
95

## Página 107

10.6. Resumindo CasadoCódigo
Isto é, a sequência 01 02 FF representa uma pequena ima-
gem de 3 pontos, cujas cores seriam vermelho, azul e cinza. Já
0102FF03030203FF\n0103FF03020303FF representa uma imagem
com2linhase8colunas.
Comisso,podemosrepresentarqualquerimagemcomtamanhofinito
(quecaibanamemória)ecujonúmerodecoresestejalimitadoa 256.Esseé
oraciocínioportrásdeummapadebitsdecores,um bitmapoformato BMP
,muitoutilizadoantigamentenomundodacomputaç ão.Suaado çãonãoé
maistãograndedevidoaotamanhoqueeleocupa:umaimagemcomgrande
qualidadeexigeumatabeladecoresenorme,eumnúmerodepontosmaior
ainda.Algoritmosdecompressãocomoo JPEGdominamessemercado.
Assimcomopensamosnaalternativaderepresentarumter çocomouma
fração(umdivididoportrês),poderíamosrepresentarumaimagemcomo
umasequênciadetraços,círculosetc.Essatambéméumaideiaboaparadi-
versostiposdeimagem,eéoraciocínioportrásdasimagensvetoriais,como
o SVG.
Omesmopodeseraplicadoaomundodamúsica,como WAVe MP3,aos
filmesetc.Nofim,representamosdesdeumnúmerointeiroatéumaimagem
detomografiacomapenaszerosouuns.Assustador.
10.6 Resumindo
Nestecapítulo,aprendemos:
• Quecomputadoresconseguemrepresentarapenas0se1snamemória;
• Queconseguimosescreverqualquernúmerocomnúmerosbinários;
• Quepodemoscriarpadrõeseregrasparaescrevernúmeroscomponto
flutuante,usandonúmerosbinários;
• Quenúmeroshexadecimaistambémsãobastanteimportanteseutili-
zados;
• Comofuncionaopadrãobitmap.
96

## Página 108

Capítulo11
Funçõeseponteiros
Vocêreparouquenossojogoaindanãotemumamensagemdeboas-vindas
aousuário?Vamoscolocá-la:
int main() {
// imprime cabeçalho
printf("/****************/\n");
printf("/ Jogo de Forca */\n");
printf("/****************/\n\n");
// código continua aqui
}
Nossojogo,emtermosdefuncionalidades,estáandandobem.Masva-
mosdarumapausanelas,paraatacaroutrodetalheimportantíssimonahora

## Página 109

11.1. Escrevendofunções CasadoCódigo
defazermosumsoftware. Vocêselembradocódigodojogodeadivinha-
ção?Eleficoumuitolegal,porém,aofinaldaimplementaç ão,tínhamosuma
função main()commaisde100linhasdecódigo.Sãomuitaslinhas,eisso
dificultamuitooentendimentodocódigoporoutraspessoas. Faç aoteste
vocêmesmo.Daquiaalgumassemanas,volteeolheomesmocódigo:você
lembrarámuitomenosdele.
Precisamosaprenderadividirnossoprogramaempartesmenores,que
sejammaisfáceisdeseremlidas.Énecessáriofazermosigualasbibliotecasdo
Cfazem.Porexemplo,quandovocêquerimprimiralgonatela,vocêchama
afun ção printf(). Vocênãosabecomoelafuncionapordentro,apenas
sabequeelaimprime.Amesmacoisacomo
11.1 Escrevendo funções
Imagineseconseguíssemostrocaras3linhasresponsáveispelaaberturado
jogoporumaúnica? Algoparecidocomocomentário,masemformatode
código,semespaços,usandoosparênteseseterminandoalinhacompontoe
vírgula:
abertura();
Oquequeremosaquiécriaroquechamamosde funções. Fun ções
sãoblocosdecódigoencapsuladosequepodemserreutilizadosaolongo
donossoprograma. Porexemplo,secriarmosumafun çãoquesechama
abertura() contendoaquelas3linhasdeimpressão,semprequeainvo-
carmos,nossoprogramafaráisso. Éigualao printf()ouao scanf():
ambossãofun çõesqueusamosaolongodonossoprograma.
Vamoscriaressafun çãoeusá-la.Escreveremosessecódigoforadafun-
ção main;afinal,elaprópriaéumafun ção,enãopodemosterfun çõesdentro
defun ções. Paradeclará-la,precisamosnomínimodeumnome. Podeser
qualquerpalavra.Faremos void abertura().Vocênãoprecisaentender
o voidporenquanto,enemoabre-e-fechaparênteses.Emseguida,abrire-
moschavesecolocaremosoconteúdodeladentrodesseblocodecódigo:
void abertura() {
printf("/****************/\n");
98

## Página 110

CasadoCódigo Capítulo11. Funçõeseponteiros
printf("/ Jogo de Forca */\n");
printf("/****************/\n\n");
}
Então, vamos fazer uso dessa função. Isso é feito dentro da função
main().Vamosremoveraquelas3linhas,queagoraestãojánafun çãocerta,
eapenasinvocá-la.Parainvocaréfácil,usamosseunomeeparênteses:
int main() {
abertura();
// código continua aqui
}
Serodarmosnossocódigo,ocomportamentoaindaéomesmo. Adi-
ferençaéqueagoranossafun ção mainéumpoucomaisfácildeserlida.
Quandooprogramadorlê abertura(),elesabequeéaliqueéfeitaaaber-
tura,masnãosabeosdetalhes.Sequisersaber,eledevelerocorpodafun ção
abertura().Diminuímosaquantidadedecódigoqueoprogramadorpre-
cisoulerparaentenderafun ção main().
Vamosentenderoqueacontececomamáquinaaoexecutaressecódigo.
Quandooprogramacome ça,eleautomaticamenteexecutaafun ção main()
e,depois,linhaalinhadocódigo.Atéaí,semnovidades.Porém,quandoele
encontraumachamadaparaoutrafun ção porexemplo, abertura(),ele
“suspende”aexecuçãode main()evaiparaaoutra.Lá,oprocedimentoé
omesmo.Eleexecutalinhaalinhae,quandoafun ção abertura()acaba,
elevoltapara main()econtinuaaexecuç ãoapartirdali.
Setivéssemosumaoutrachamadadefun çãodentrode abertura(),
ocomportamentoseriaomesmo.Amáquinasuspenderiaaexecuç ãodesta,
executariaaoutrae,quandoelaacabasse,voltariaparaaanterior,que,por
suavez,quandoacabasse,voltariaparaafun ção main().
99

## Página 111

11.2. Maisfunções CasadoCódigo
Está perdido?
O código até esse momento está em
http://pastebin.com/ES8eiBdf
11.2 Mais funções
Vejaagoraocódigoprincipaldonossojogoe,maisespecificamente,ocon-
teúdodentrodo do-while. Reparenostrêscomentáriosdecódigo. Será
quetambémnãoconseguimostransformá-losemfun ções?
do {
// imprime a palavra secreta
for(int i = 0; i < strlen(palavrasecreta); i++) {
int achou = 0;
// a letra já foi chutada?
for(int j = 0; j < tentativas; j++) {
if(chutes[j] == palavrasecreta[i]) {
achou = 1;
break;
}
}
if(achou) {
printf("%c ", palavrasecreta[i]);
} else {
printf("_ ");
}
}
printf("\n");
// captura um novo chute
char chute;
printf("Qual letra? ");
scanf(" %c", &chute);
100

## Página 112

CasadoCódigo Capítulo11. Funçõeseponteiros
chutes[tentativas] = chute;
tentativas ++;
} while (!acertou && !enforcou);
Reparenoprimeirocomentário: imprime a palavra secreta.Eleengloba
o for,queéresponsávelporimprimiraforca. Osegundocomentário, a
letra já foi chutada?,englobaosegundo for,queéresponsávelpordizerse
umadeterminadaletrajáfoichutadapelousuárioounão.Porfim,oúltimo
comentário,captura um novo chute,pegaumnovochutedousuário.
Vamospegaroúltimocomentárioetambémtransformá-loemumafun-
ção.Afinal,issodeixaránossocódigoaindamaislegível.Oprocedimentoé
omesmo.Logo,vamoscriarafun ção chuta():
void chuta() {
char chute;
printf("Qual letra? ");
scanf(" %c", &chute);
chutes[tentativas] = chute;
tentativas ++;
}
Vamosagoratambéminvocá-ladentrodo main(),nolugardocódigo
antigoqueremovemosemproldessanovafun ção:
int main() {
do {
// ...
chuta();
} while(!acertou && !enforcou);
}
Fizemosomesmoprocedimentodeanteriormente,mas,dessavez,ocó-
digonãocompila.Vejaoerro:elereclamaqueavariável chutesnãoexiste.
Eocompiladorestácerto;afinal,avariável chutesexisteapenasdentroda
função main():
101

## Página 113

11.3. Passandoparâmetrosparafunções CasadoCódigo
forca.c:15:2: error: use of undeclared identifier 'chutes';
did you mean 'chute'?
chutes[tentativas] = chute;
^~~~~~
chute
11.3 Passando parâmetros para funções
Variáveisvivem,esãovisíveis,apenasnoescopoemqueforamdeclaradas.
Porexemplo,sedeclaramosumavariáveldentrodafun ção main(),elaes-
tarávisívelsomentedentrodessafun çãoedosescoposdeclaradosdentrodela.
Porexemplo,sevocêtiverum fordentrodela,elaconseguiráveressavariá-
vel.
Nocódigoaseguir,avariável multiplicador,declaradadentroda
função main(),évisívelemtodolugardentrodessafun ção. Jáavariável
resultado,declaradadentrodo for,évisívelsomentedentrodesse for
(ouemoutrosescoposquefossemdeclaradosdentrodele). Entretanto,ne-
nhumadelasévisíveldentrodafun ção abertura():
void abertura() {
// aqui não enxergamos a variável multiplicador
printf("Tabuada do ");
printf("Quero imprimir o multiplicador aqui,
mas nao consigo... ");
}
int main() {
int multiplicador = 2 ;
abertura();
for(int i = 0; i < 10; i++) {
int resultado = multiplicador * i;
printf("%d x %d = %d", i, multiplicador,
resultado);
}
}
102

## Página 114

CasadoCódigo Capítulo11. Funçõeseponteiros
Pararesolveresseproblema,temosduassoluções.Aprimeiradelasépas-
sarasvariáveisquequeremosparaasoutrasfun ções.Issopodeserfeito;basta,
nomomentodadeclaraç ãodavariável,dizerquaisserãoosparâmetrosque
elareceberá. Nahoradeinvocarmos,passamososparâmetrosparaelanos
“parênteses”nomomentodadeclaração.Bastadizeronomedoparâmetroe
seutipo.
Veja,porexemplo,afun ção abertura()recebendocomoparâmetro
uminteiro multiplicador.Esseparâmetroécomosefosseumavariável
paraaquelafun ção.Elaexistenaqueleescopoepodesermanipuladacomo
qualqueroutra:
void abertura( int multiplicador) {
// aqui temos uma variável chamada multiplicador
// e seu valor será definido por quem chamar essa função
printf("Tabuada do %d", multiplicador);
}
Issosignificaquenãopodemosmaisinvocarafun ção abertura()sem
passarosseusparâmetros. Sempreprecisamospassarosparâmetrosqueas
funçõesrequerem.Nessecasoemparticular,precisamossemprepassarum
inteiroparaela.Observe:
// passando um inteiro diretamente
abertura(2 );
Jáqueelarecebeuminteiro,porquenãopassartambémuminteiroque
estáemumavariável?
int main() {
// passando uma variável
int numero = 10;
abertura(numero);
}
Reparequeestamospassandoavariável numerocomoparâmetroparaa
função abertura().Elacontémonúmero10.Issoquerdizerque,quando
afun ção abertura()forexecutada,oparâmetro multiplicadorvalerá
103

## Página 115

11.3. Passandoparâmetrosparafunções CasadoCódigo
10também. Écomoseamáquinacopiasseovalordavariável numeroe
colassenavariável multiplicador.
Paraqueessenossopequenocódigodetabuadafuncione,bastainvocar-
mosafun ção abertura(),passandoavariável multiplicador. Note
que,apesardeambososnomesseremiguais(odavariáveleodoparâmetro),
nãoéonomequefeztudoacontecer.Ouseja,oparâmetro multiplicador
édiferentedavariávelmultiplicadorqueestánamain();apenasoscon-
teúdoséquesãoiguais.Lembre-sedeque,quandovocêchamaumafun ção,
porexemplo, abertura(10),amáquinapegaonúmero10ecolocadentro
doparâmetroquefoideclaradonafun ção(quepodeterqualquernome).
void abertura( int multiplicador) {
printf("Tabuada do %d\n", multiplicador);
}
int main() {
int multiplicador = 2 ;
abertura(multiplicador);
for(int i = 0; i < 10; i++) {
int resultado = multiplicador * i;
printf("%d x %d = %d\n", i, multiplicador,
resultado);
}
}
Está perdido?
Ocódigodoexemplodatabuadaestáem
http://pastebin.com/zAWw0wbF
Voltandoaonossojogo,precisamosfazercomqueafun ção chuta()
recebaoarraydechuteseavariável tentativas.Vamoscolocaressepa-
râmetronaassinaturadafun ção.Reparecomodeclaramosqueoparâmetro
chutesédotipoarraydechar.
104

## Página 116

CasadoCódigo Capítulo11. Funçõeseponteiros
void chuta(char chutes[], int tentativas) {
char chute;
printf("Qual letra? ");
scanf(" %c", &chute);
chutes[tentativas] = chute;
tentativas ++;
}
Agora,passamosoarrayeointeiro,queforamdeclaradosnafun ção
main,paraafun ção chuta():
chuta(chutes, tentativas);
Novamente,notequeosparâmetros chutese tentativassão“variá-
veisdiferentes”dochutese tentativasqueestãonafun ção main().
Porém,issopodeserumproblema,dependendodocaso. Falaremosmais
sobreissoembreve.
Está perdido?
O código até esse momento está em
http://pastebin.com/N2QMxqfE
11.4 Ponteiros
Vejaoprogramaaseguir.Nelequeremosprovarque,quandousamosparâ-
metrosemfun çõesepassamosumavariávelcomoparâmetro,mesmoque
osnomesdelassejamiguais,elasaindasãodiferentes. Afun ção main()
contémumavariáveltentativas,fazoperaçõesdeincrementocomestae
imprime.Emseguida,elaapassaparaafun ção joga(),quefazumincre-
mento,eimprimedenovo.Aofinal,afun ção main()imprimenovamente
ovalordavariável.
# include <stdio.h>
void joga(int tentativas) {
105

## Página 117

11.4. Ponteiros CasadoCódigo
printf("joga %d\n", tentativas);
tentativas++;
printf("joga %d\n", tentativas);
}
int main() {
int tentativas = 0;
printf("main %d\n", tentativas);
tentativas++;
printf("main %d\n", tentativas);
tentativas++;
printf("main %d\n", tentativas);
joga(tentativas);
printf("main %d\n", tentativas);
}
Ointeressanteéasaídadesseprograma. Vejaqueavariávelnafun ção
main()vale2,quandochamamosafun ção joga().Emseguida,afun ção
joga()incrementa1,epodemosverqueelaimprimeonúmero3. Mas,
quandovoltamosparaafun ção main(),eleimprime2novamente:
main 0
main 1
main 2
joga 2
joga 3
main 2
Issonosprovaqueambasasvariáveis,apesardeteremomesmonome,
sãodiferentes. Quandoinvocamosafun ção joga(),passandoavariável
tentativasdeclaradanafun ção main(),amáquinacopiaseuconteúdoe
criaumanovavariávelchamada tentativas,queserávisívelsónafun ção
106

## Página 118

CasadoCódigo Capítulo11. Funçõeseponteiros
joga().Quandoafun ção joga()termina,eoprogramavoltaparaafun-
ção main(),avariável tentativascontinuavalendo2.Afinal,elanãofoi
modificadadepoisdisso.
Fig.11.1:Variáveiscommesmonomeemregiõesdiferentesdamemória
Esseisolamentoentreasfun çõeséumacoisaboa.Imaginesevocêpas-
sasseumavariávelcomoparâmetroparaumafun ção,eestativessealiber-
dadedemudá-la? Seuprogramaseriamaiscomplicadodeserentendido;
afinal,vocênãosaberiaquemmudouavariávelequandoissoaconteceu.É
poressemotivoquechamamosissode passagemporcópia.Ouseja,sempre
quepassamosumavariávelparaumafun ção,amáquinaacopiaecriauma
nova,paraqueaoriginalfiqueintacta.
Muitasvezesapassagemporcópiaésuficiente.Masàsvezes,não.Volteao
nossojogoevejaavariável tentativas.Elacontémaquantidadedechutes
jádadospelojogador. Afun ção chuta()aincrementa. Mas,naverdade,
deveríamosincrementaravariável tentativasqueestádentrodoescopo
dafun ção main().Nessemomento,oparâmetro tentativasdafun ção
chuta()éoqueéincrementado,enãoodafun ção
E para resolver isso? Gostaríamos, nesse caso, que a variável
tentativasdafun ção chuta()fosseamesmadafun ção main().
void chuta(char chutes[26], int tentativas) {
char chute;
scanf(" %c", &chute);
chutes[tentativas] = chute;
107

## Página 119

11.5. Passagemporreferência CasadoCódigo
// a soma precisa acontecer na variável
// 'tentativas', que existe no escopo
// da função 'main'
tentativas++;
}
int main() {
int tentativas = 0;
// ...
chuta(chutes, tentativas);
// ...
}
11.5 Passagem por referência
Podemosdizeraonossoprogramaquenãoqueremosqueelepasseoparâme-
troporcópia,massim,peloquechamamosde referência.Apassagempor
referênciaéalgobastanteavan çado. Comoqueamáquinafazparapassar
umavariávelporreferência?Simples,elapassaaposiç ãodamemóriaemque
essavariávelestá.Imagineamemóriadocomputadorcomoumafitaimensa
enumerada.Todasasvariáveisdenossosprogramasficamemalgumlugar
dessafita.
Pense novamente na passagem por cópia. Imagine que a variável
tentativasdafun ção main()estánaposição10damemória. Quando
passamosporcópia,amáquinaalocaumnovoespaçonamemóriaparaa
novavariáveltentativas.Suponhaqueelaficounaposiç ão200.Ouseja,
umavariávelapontaparaaposiç ão10,enquantoaoutraapontaparaaposi-
ção200. Vocêprecisapensaragoraemvariáveiscomoseelasfossemsetas,
oumelhor, ponteirosparaendere çosdememória,poiséexatamenteissoo
queelassão.Vejanafiguraaseguirasduasvariáveisquetêmomesmonome
tentativas,masseencontramemregiõesdiferentesdamemória:
Mas,senofundo,variáveissãoapenasponteirosparaendere çosdeme-
108

## Página 120

CasadoCódigo Capítulo11. Funçõeseponteiros
mória,porquenãoterduasvariáveisqueapontamparaomesmoendere ço?
Podemosfazerisso.Porexemplo,sequisermosveroendere çodememória
queumavariávelaponta,usamosocaractere &.Oprogramaaseguirimprime
oendere çodememóriadavariável c.Repareque,semprequeorodarmos,o
númeroserádiferente;afinal,cadahoraamáquinadecidepegarumendere ço
dememóriadiferentequeestálivrenaquelemomento,claro:
# include <stdio.h>
int main() {
int c = 10;
printf("%d\n", &c);
}
Issoquerdizerque,sepassarmoscomoparâmetroparaumafun ção um
&c,porexemplo,estaremospassandooendere çodememóriaemqueessa
variávelseencontra. Ouseja,casomudarmosoconteúdoqueestádentro
desseendere ço,eleserámodificadoparatodomundoquetenhaumavariável
apontadaparalá.
Sevocêdeclaraumavariáveldojeitoqueestáacostumado,amáquina
escondedevocêaideiadequeelaé,naverdade,umponteiro. Éporisso
quevocêconseguefazercoisascomoatribuições porexemplo, c = 10,ea
máquinafazoprocessodepegaroendere çodememóriaqueestáescondido
em cecolocarovalor10.
Vocêtambémtemaop çãodemanipulardiretamenteumendere çode
variável,ouseja,declararumponteiro. Umponteirosimplesmentecontém
umendere çodememória. Declará-loéparecidocomadeclaraç ãodeuma
variável:precisamosdeumnomeedeumtipo.Mascompletamosotipocom
estrelaouasterisco( *).
Vejaoexemploaseguir,noqualdeclaramosumponteiroparauminteiro.
Seeleéumponteiro,querdizerquepodemosguardaroendere çodavariável
cládentro.Parapegaroendere çodela,bastausarmoso &.
int c = 10;
109

## Página 121

11.5. Passagemporreferência CasadoCódigo
int* ponteiro;
ponteiro = &c;
Nessemomento,avariável ponteiroapontaparaomesmolugarao
qual caponta.Seimprimirmos &ce ponteiro,oresultadoéomesmo:
printf("%d %d", ponteiro, &c);
Agora,sequisermosacessaroqueestádentrodoendere çoparaqual
ponteiroaponta,usamoso *nafrentedavariável. Porexemplo,seim-
primirmosavariável ce *ponteiro,oresultadoéomesmo(10):
printf("%d %d", *ponteiro, c);
Ouseja,seavariáveléumponteiro,equeremosacessaroconteúdoque
estádentrodoendere çoaoqualelaaponta,usamosestrela.Vejanovamente
ocódigointeiroepercebacomomanipulamosumavariávelnormaleuma
variávelponteiro:
int c = 10;
int* ponteiro;
// ponteiro apontando para o mesmo endereço de c
ponteiro = &c;
// imprime o endereço da variável c
printf("%d %d\n", ponteiro, &c);
// imprime o conteúdo da variável c
printf("%d %d\n", *ponteiro, c);
Sabendodisso,vamospassaravariável tentativascomoreferência.
Ouseja,vamospassarseuendere çodememóriaparaafun ção chuta(),
usandoo &:
chuta(chutes, &tentativas);
Claroque,sepassamosumponteirodeinteiroparaafun ção,éporque
elarecebeumponteirodeinteiro.Precisamosmudaraassinaturadafun ção
chuta(),efazê-lareceberum int* tentativas.Alémdisso,devemos
usaro *paraacessaroconteúdoqueoponteiro tentativasaponta.Veja:
110

## Página 122

CasadoCódigo Capítulo11. Funçõeseponteiros
void chuta(char chutes[], int* tentativas) {
char chute;
printf("Qual letra? ");
scanf(" %c", &chute);
chutes[*tentativas] = chute;
(*tentativas)++;
}
Podemosagoracolocarum printf()emnossojogo,mostrandoonú-
merodetentativas. Vocêveráque,comoestamospassandooponteiroda
variável,onúmeroémodificadonavariávelquequeremos.
do {
printf("Você já deu %d chutes\n", tentativas);
// ...
}
Ponteiros,apesardepareceremcomplicadosemumprimeiroinstante,
sãopoderosíssimos. Nafiguraaseguir,vejaqueagoraambososponteiros
tentativasapontamparaomesmoendere çodememória,logopossuem
omesmoconteúdo:
Fig.11.2:Funcionamentodosponteiros
111

## Página 123

11.6. Arrayseponteiros CasadoCódigo
Está perdido?
O código feito até o momento está em
http://pastebin.com/ztjPwSvY
11.6 Arrays e ponteiros
Vocêdeveestarseperguntandoomotivopeloqualtivemosquepassaroin-
teirocomoponteiro,masnãooarray.Issonãomuda:sequisermosmodificar
umavariávelqueestádeclaradaemoutroescopo,precisamosmexerdireto
emseuendere çodememória,eusarponteiros;nãotemsoluç ão.
Acrediteounão,fizemosissonoarray.Umarrayé,porpadrão,umpon-
teiro. Avariávelchuteséumponteiroqueapontaparaointeiroqueestá
naprimeiraposiç ãodoarray. Sabemosqueaprimeiraposiç ãodoarrayé
chutes[0].Sefizermos &chutes[0],temosoendere çodememóriadesse
primeirointeiro.Essenúmeroéiguala chutes.
Vejaocódigo:
printf("%d %d", chutes, &chutes[0]);
Agoraquevocêestáentendendomaissobreamemória,vejaqueumar-
rayéuma“sequênciadevariáveis”declaradas.Emparticular,essasvariáveis
estãoexatamenteumadoladodaoutra.Quandodeclaramosumarrayde10
posições,amáquinaprocuraporumlugarondecaibam10inteiros,umao
ladodooutro.
Quandofazemos chutes[2],porexemplo,amáquinapegaaposiç ão
dememóriadaprimeiraposiç ãodessearray,evainavegandoatéaposiç ão
quequer.Noexemplo,onúmero2querdizeraterceiraposiç ãodoarray.Ele
pula3casasechegaaopróximointeiro.
Masvocêselembraquediscutimosotamanhodeuminteiro?Uminteiro
ocupa4bytes. Emoutraspalavras,sevocêdeclaraumavariávelinteira,a
máquinasepara4bytesdamemóriaparaele.Emumarray,aconteceamesma
coisa;setemosumarraydeinteirosde10posições,precisamosde40bytes.
Ouseja,se &chutes[0]nosretorna10, &chutes[1]nosretornará14,
112

## Página 124

CasadoCódigo Capítulo11. Funçõeseponteiros
poiséondeosegundointeirocome ça.Vejanafiguraaseguirumdiagrama
dofuncionamentodeumarrayecomolidamoscomele:
Fig.11.3:Funcionamentodeumarray
Vejaemcódigo. Oprogramaaseguirdeclaraumarraydeinteirosde
3posições. Emseguida,imprimimosaposiç ãodememóriaemqueestão
guardadoscadaumdessesnúmeros.Sabemosqueuminteirotem4byteseos
itensdeumarraysãoguardadosumaoladodooutro.Portanto,osnúmeros
devemcrescerde4em4.
# include <stdio.h>
int main() {
int numeros[3];
printf("%d %d %d\n", &numeros[0], &numeros[1 ], &numeros[2]);
}
Asaídacomosendere çosédiferenteacadavezqueexecutarmosotrecho
decódigo,poisoendere çodememóriamuda.Notequeelapulade4em4
bytes,comoesperado:
1458119804 1458119808 1458119812
Podemostrataresse int[]comoum int*.Afinal,arrayssãoponteiros.
Setemosumponteirodeinteiroesabemosqueeleapontaparaumarray,po-
demosacessaraprimeiraposiç ãofazendo *ponteiro.Sequisermosacessar
113

## Página 125

11.6. Arrayseponteiros CasadoCódigo
asegundaposiç ão,bastasomarmos1aesseponteiro, *(ponteiro + 1),e
assimpordiante.
Observeocódigoaseguir,noqualfazemosumloopeacessamososvalo-
resdoarray,usandootipoarrayconvencionaletambémdiretamenteopon-
teiro:
# include <stdio.h>
int main() {
int numeros[3];
// declarando um ponteiro que aponta para o
// mesmo lugar que o array/ponteiro numeros
int* ponteiro = numeros;
numeros[0] = 10;
numeros[1] = 20;
numeros[2] = 30;
for(int i = 0; i < 3; i++) {
printf("%d ", numeros[0]);
// repare na soma que fazemos com o ponteiro
printf("%d ", *(ponteiro + i));
printf("\n");
}
}
Apartirdeagora,suacabe çadeveestarmuitodiferente.Vocêconsegue
verponteirosemtudo? Lembre-sedequevariáveissãoponteirosparaen-
dereçosdememória.Alinguagemdeprogramaç ãogeralmentenosesconde
isso.Elaseviraemmanipularesseendere çoesalvarnossosdadoslá.Entre-
tanto,seprecisarmos,alinguagemCnosdeixalidardiretamentecomesses
endereçosdememória.
114

## Página 126

CasadoCódigo Capítulo11. Funçõeseponteiros
11.7 Funções com retorno
Apróximafun çãoquevamosextrairdenossocódigoseráresponsávelpornos
dizerseojogadorjáchutoudeterminadaletra.Vejaqueéissoqueo forde
dentrofaz.Elevarreapalavrasecretaealistadechutes,eguardanavariável
achouseousuáriojáchutouounãoaquelaletra.
Éfácilverqueesse forusaoarraydechutes;afinal,elenecessitapassar
portodoele,eprecisatambémdaletraqueseráprocurada.Vamosescrever
afun ção void jachutou(),quereceberáum char letra,um char*
chuteslembre-sequeumarrayéumponteiro,entãopodemosrecebercomo
umponteiro,eaquantidadedetentativas.
Vamostambémrelembraralógicadessafun ção.Elavarriaoarray,pro-
curandoporumchutequesejaigualàletracomqualelequercomparar.Se
eleacharaletranoarray,elemarcaavariável achoucomo1.O1,paranós,
significa“verdadeiro”.Casocontrário,achouéfalso.Essavariável,então,era
usadamaisparabaixo,paraexibirounãoaletra. Entretanto,issonãovem
aocaso,jáquenãofazpartedoprocessodedizerseumaletrajáfoiounão
chutada.
void jachutou(char letra, char* chutes, int tentativas) {
for(int j = 0; j < tentativas; j++ ) {
if(chutes[j] == letra) {
achou = 1;
break;
}
}
}
Comafun çãoescrita, vamosusá-laeinvocá-lanolugarondeocó-
digoantigoexistia. Ocódigoficousimples. Declaramosavariável achou,
inicializando-acom0,einvocamosnossafun ção jachutou.Emseguida,o
if,queimprimeounãoaletra,usaessavariável:
for(int i = 0; i < strlen(palavrasecreta); i++) {
int achou = 0;
jachutou(palavrasecreta[i], chutes, tentativas);
115

## Página 127

11.7. Funçõescomretorno CasadoCódigo
if(achou) {
printf("%c ", palavrasecreta[i]);
} else {
printf("_ ");
}
}
Porém,essecódigoaindanãofunciona.Afinal,jásabemosqueavariável
achou,declaradadentrodafun ção main(),nãoéamesmadadeclarada
dentroda jachutou().Sequisermos“compartilhar”avariável,precisare-
mospassaroseuponteiro.Sabemosqueissonãoédifícil,poisbastariapassar
oendere çode achou,usando &achou,ereceberoponteirodooutrolado,
comoparâmetro,um int* achou.
Apesardeaalternativaserválida,geralmentetemosumasoluç ãomais
eleganteparaisso.Vejaqueavariável achouéoresultadodanossafun ção
jaachou().Ouseja,elaprocessa,fazummontedecoisa,mas,aofinal,pre-
cisaapenas“contarparaquemachamou”oresultadodessavariável.Quando
umafun çãoprecisadevolverapenasumdadoumnúmero,ouchar,oudouble
etc. paraquemachamou,damosumtipoderetornoaela.
Atéagora,semprequedeclaramosumafun ção,usamosapalavra void
nocome ço.Usamos voidquandoafun çãonãoprecisaretornarnadaaquem
achamou. Mas,seelaprecisarretornar,podemostrocaressapalavrapelo
tipoderetorno.Porexemplo,queremosdevolveruminteiro,entãotrocamos
apalavra voidpor int:
int jachutou(char letra, char* chutes, int tentativas) {
// ...
}
Agora,precisamosindicarqualovalorquedeveserretornadoporessa
função. Parafazerisso,bastausarapalavra return. Quandoessetermo
aparecedentrodeumafun ção,geralmenteacompanhadoporumvalor por
exemplo, return 10;pararetornarovalor10,afun çãoparaali,equema
chamourecebeessevalor.
Aqui,queremosretornaroconteúdodavariável achouaofinaldafun-
ção. Colocaremoscomoúltimalinhaesseretorno. Alémdisso,precisamos
116

## Página 128

CasadoCódigo Capítulo11. Funçõeseponteiros
declararavariável achounocome çodessafun çãoeinicializá-lacom0,pois
elanãoexistiaaliatéentão:
int jachutou(char letra, char* chutes, int tentativas) {
int achou = 0;
for(int j = 0; j < tentativas; j++ ) {
if(chutes[j] == letra) {
achou = 1;
break;
}
}
return achou;
}
Nossafun ção jachutou()estápronta.Elanosdevolveuminteirosem-
prequeainvocarmos.Esseinteirovale1quandoeleacharaletra,e0quando
nãoachar.Vejaqueissopareceumafun çãodamatemática.Dadoumcon-
juntodevaloresdeentrada,elanosdevolveumresultadocomosaída.Épor
issoquechamamosdefun ção.
Comoamatemáticanosdábonsexemplosdefun ções,poderíamoster
umaquenosdevolvesseoquadradodeumnúmero.Elareceberiaumnúmero
comoparâmetroedevolveriaamultiplicaç ãodeleporelemesmo. Vejaem
código:
int quadrado(int n) {
return n * n;
}
Usaressafun çãoéigualusarfun çõesquedevolvem void.Adiferen ça,
claro,équeelasnosretornamalgo.Paracapturarmosovalorretornado,pre-
cisamosguardá-laemumavariável.Vejaalgunsexemplosdeusodafun ção
quadrado();umasguardandoemvariáveis,outrasusando-asdiretamente:
// guardando em uma variável
int resultado = quadrado(2);
printf("%d", resultado);
117

## Página 129

11.8. Extraindomaisfunções CasadoCódigo
// usando diretamente em um if
if(quadrado(3) < 10) {
printf("Já sabia, o quadrado de 3 é 9");
}
// usando direto em um printf
printf("%d", quadrado(5));
Voltandoaojogo,vamosagorafazerusodiretodafun ção jachutou().
Comovimosquepodemosutilizá-ladiretamentedentrodo if,semane-
cessidadedeumavariávelauxiliar,vamosusá-ladiretamentenocondicional
quedecidemostrarounãoaletra.Vejacomonossocódigoestácadavezmais
simples:
for(int i = 0; i < strlen(palavrasecreta); i++) {
if(jachutou(palavrasecreta[i], chutes, tentativas)) {
printf("%c ", palavrasecreta[i]);
} else {
printf("_ ");
}
}
Está perdido?
O código até o momento está em
http://pastebin.com/G1Lp35mS
11.8 Extraindo mais funções
Vamos continuar separando em funções. Agora, podemos extrair o
loop forde fora, aquele que varre a palavra secreta, para uma função
desenhaforca(). Extraí-laéfácil. Bastafazermosafunçãoreceberapa-
lavrasecreta,oschuteseaquantidadedetentativas. Comoelanãoprecisa
retornarnada,elaé void:
118

## Página 130

CasadoCódigo Capítulo11. Funçõeseponteiros
void desenhaforca(char* palavrasecreta, char* chutes,
int tentativas) {
printf("Você já deu %d chutes\n", tentativas);
for(int i = 0; i < strlen(palavrasecreta); i++) {
if(jachutou(palavrasecreta[i], chutes, tentativas)) {
printf("%c ", palavrasecreta[i]);
} else {
printf("_ ");
}
}
printf("\n");
}
Fazendousodessafun çãonolugarcerto,oloopprincipaldojogoficou
maissimplesdeserlidoeentendido.Agora,dáatéparaleremportuguêso
queacontece. Ele“desenhaforca”e“chuta”,enquanto“nãoacertou”e“não
enforcou”. Vejaquevocêconsegueentenderoalgoritmoemaltonívelem
poucossegundos.Odesenvolvedorsóprecisarálerosseusdetalhes ouseja,
aimplementaçãodecadaumadessasfun ções sequiseroutivernecessidade.
Nossocódigoestácadavezmaisbemescritoeisolado.Issoéfundamental
quandoprogramamos.
do {
desenhaforca(palavrasecreta, chutes, tentativas);
chuta(chutes, &tentativas);
} while (!acertou && !enforcou);
119

## Página 131

11.9. Variáveisglobais CasadoCódigo
Está perdido?
O código até o momento está em
http://pastebin.com/ERgqEeNb
Porfim,aindapodemosdeixarmaisfácildeserentendidaapartenaqual
selecionamosapalavrasecreta.Porenquanto,elaéfixa,porém,maisàfrente,
vamoslerdeumarquivodepalavras.Sejátivermosessecódigobemisolado
emumafun ção,ficaráfácildepoistrocar. Afun ção escolhepalavra()
receberáoarray palavrasecreta:
void escolhepalavra(char* palavrasecreta) {
sprintf(palavrasecreta, "MELANCIA" );
}
Vamosinvocá-latambémemumlugarmaisoportuno,demelhorlegi-
bilidade,umpoucomaisafastadodadeclaraç ãodasvariáveis. Logoabaixo
dainvocaçãodafun ção abertura(),porexemplo,parecebom.Afun ção
main()agoraestábastanteenxuta:
abertura();
escolhepalavra(palavrasecreta);
do {
// ...
} while (...);
Está perdido?
O código até o momento está em
http://pastebin.com/fJ3JJMXB
11.9 Variáveis globais
Reparequetodasnossasfun çõesagoraprecisampassarosmesmosparâme-
trosparaláeparacá.Fazsentido;afinal,oarraydechutes,apalavrasecretae
120

## Página 132

CasadoCódigo Capítulo11. Funçõeseponteiros
onúmerodetentativassãovariáveisimportantesparaojogo.Esseproblema,
inclusive,nosserviudemotivaç ãoparanossadiscussãodefun ções,parâme-
troseponteiros.
Eseconseguíssemosdeclararumavariávelquefossevisívelparamaisde
umafun ção,enãosóparaaquelanaqualelafoideclarada? Nossocódigo
ficariabemmenor,umavezquea assinaturadafunção assinaturaéonome
quedamosparaonome,parâmetrosetiposderetornodeumafun ção seria
bemmaissimples.
Naverdade,podemos.EmC,podemosdeclararumavariávelforadoar-
quivo.Essasvariáveissãochamadasde variáveisglobais,poiselasficamvisí-
veisepassíveisdeseremacessadasporqualquerfun çãodeclaradaemnosso
programa.Elassãobastanteúteisquandotemosvariáveisquesãoimportan-
tese,porconsequência,manipuladasportodasasnossasfun ções.
Vamos fazer isso com as variáveischutes, palavrasecreta e
tentativas.Vamosdeclará-laslogoapósalistade includes:
# include <stdio.h>
# include <string.h>
char palavrasecreta[20];
char chutes[26 ];
int tentativas = 0;
Jáqueagoraelassãovisíveisparatodasasfun ções,nãoprecisamosmais
passá-lasporparâmetroemtodasasfun ções.Vamosremoverosquenãosão
maisnecessários.
Nafun ção chuta(),nãoprecisamosmaisnemde chutesnemde
tentativascomoparâmetro.Jáque tentativasagoraéuminteirocon-
vencional(enãomaisumponteiro),vamostirarasoperaçõesdeponteiroe
fazeroperaçõescomunscomela:
void chuta() {
char chute;
printf("Qual letra? ");
scanf(" %c", &chute);
chutes[tentativas] = chute;
121

## Página 133

11.9. Variáveisglobais CasadoCódigo
tentativas++;
}
Afun ção jachutou()tambémnãoprecisamaisdoarrayde chutes,
nemdavariável tentativas.Aquiamudan çaésimples,ebastaremover-
mosdaassinaturadafun ção.Repareque,aindaassim,precisamosrecebera
letraqueprocuraremosnoarray.Vejacomoelaficoumaissimples:
int jachutou(char letra) {
int achou = 0;
for(int j = 0; j < tentativas; j++) {
if(chutes[j] == letra) {
achou = 1;
break;
}
}
return achou;
}
Afun ção desenhaforca()tambémnãoprecisarecebermaisnenhum
parâmetro,nempassartodoselesparaafun ção jachutou(),invocadaden-
trodela.
void desenhaforca() {
printf("Você já deu %d chutes\n", tentativas);
for(int i = 0; i < strlen(palavrasecreta); i++) {
if(jachutou(palavrasecreta[i])) {
printf("%c ", palavrasecreta[i]);
} else {
printf("_ ");
}
}
printf("\n");
}
122

## Página 134

CasadoCódigo Capítulo11. Funçõeseponteiros
Omesmoacontececomafun ção escolhepalavra():
void escolhepalavra() {
sprintf(palavrasecreta, "MELANCIA");
}
Porfim,a maintambémnãoprecisamaispassarosparâmetrosparaas
funções.Vejasócomoelaficoutotalmenteenxutaefácildeserlida.Repare
no tentativasnofimdoloop,jáquenãopodemosmaisfazeroincremento
dentrodafun ção chuta:
int main() {
int acertou = 0;
int enforcou = 0;
abertura();
escolhepalavra();
do {
desenhaforca();
chuta();
tentativas++;
} while (!acertou && !enforcou);
}
Vejaqueagoraescolhemosomelhorlugarparadeclararnossasvariáveis.
Variáveisquefazemsentidoexistirememumcontextomaisamploesão
diretamenterelacionadascomonossojogodeforca palavrasecreta,
chutese tentativas,sãoglobaisevisíveisportodasasfun ções.Jáva-
riáveisquesãomaislocaiseespecíficasdeumafun çãoemparticular,comoa
variávelachounafun ção jachutouea inafun ção desenhaforca,são
declaradaslocaiseexistemsónaquelecontexto.
Será,então,quevariáveisglobaissãosempreboas?Algoparavocêpensar
desdeocome çodesuacarreiraemdesenvolvimentodesoftwareéquetoda
123

## Página 135

11.9. Variáveisglobais CasadoCódigo
decisãodecódigotemsempreprósecontras.Semexce ção.Aindanãofomos
capazesdecriarbalasdepratas,ouseja,soluçõesperfeitaseexatasparatodos
osproblemas.Variáveisglobaisnosajudamadiminuiraquantidadedecó-
digoqueescrevemos,umavezqueprecisamospassarmenosparâmetrospara
láeparacá,easfun çõesjáasacessamdiretamente.
Adesvantageméqueagoraficamaisdifícilentenderquemmodificouo
quê.Antes,quandoasvariáveisestavamsempredeclaradasdentrodeescopos
controlados,sevocêquisessesaberquemmudouavariável tentativas,
bastavaolharafun çãoemqueelaestavadeclarada.Agora,vocêprecisaolhar
ocódigotodo.Ouseja,perdemosumpoucodocontrolesobreoacessoaelas,
jáquequalquerfun çãopodealterá-las.Éumatroca.
Variáveisglobaissãogeralmentemuitocriticadasporisso.Mas,sevocê
usá-lasbem,nãoteráproblemas.Lembre-sedecolocarcomoglobalapenas
aquelasquetenhamumsentidomaiorparaocódigo. Maisàfrente(eno
mundoreal),criaremosprogramascomváriosarquivos. Esseéorealpro-
blema:termuitosarquivosdiferentes,quefazemcoisasdiferentes,mexendo
nasmesmasvariáveis.Imagineocódigodoseujogodeadivinhaç ãomexendo
nasvariáveisdojogodeforca?Nãofazsentido.Mesmoqueinventássemos
algumaregraemqueosjogossecombinassem,oidealseriaquesóoarquivo
forca.cmexesseemvariáveisdojogodeforca,eo adivinhacao.cme-
xesseemvariáveisdojogodeadivinhaç ão.
Nestelivro,nãofalamossobreOrientaç ãoaObjetos,massemdúvida,é
opróximoassuntoarespeitodoqualvocêdeveler. OrientaçãoaObjetos
éumaoutramaneiradeescreverprogramasdecomputador. Suamaneira
depensarédiferenteda programaçãoprocedural,sendoestaqueusamos
aquicomalinguagemC,ondetemosumconjuntodefun çõesquetrabalham
juntas.
Existemmuitasmaneirasdiferentesdeseescreverumprogramadecom-
putadore,emtodaselas,vocêdevepensaremfacilitaramanuten çãodoseu
código.Comofazerisso?Deixandosemprepertoascoisasquemudamjun-
tas.Tudoqueérelacionadoaojogodaforcaficaemumarquivo,etudoque
érelacionadoaodeadivinhaç ãoficaemoutro.
Nossojogoagora,alémdebonitoporfora,estáficandotambémbonito
pordentro.
124

## Página 136

CasadoCódigo Capítulo11. Funçõeseponteiros
Está perdido?
O código até o momento está em
http://pastebin.com/HAC8XEkx
11.10 Resumindo
Nestecapítulo,aprendemos:
• Aescreverfunçõespróprias;
• Afazerusodasfunçõesdeclaradas;
• Oquesãoponteiros;
• ComousarponteirosemC;
• Quearrayssãoponteiros;
• Adeclararfunçõescomparâmetros;
• Acriarfunçõescomretorno;
• Ausarvariáveisglobais;
• Quandonãousarvariáveisglobais.
125

## Página 138

Capítulo12
Entradaesaída(I/O)
Faltapoucoparaterminarmosnossojogo.Nessemomento,precisamosfazer
todaalógicadevencerouperderojogo. Emumjogodeforca,perdemos
quandoesgotamostodasnossaschances,eganhamosquandoacertamosa
palavrasecreta.Mas,agoraquejáaprendemosacriarfun ções,tudoficamais
fácil.Antes,precisávamosolharaquelascentenasdelinhasdecódigoeacharo
pontoexato.Agora,podemosescreverocódigoemfun çõesisoladas,edepois
apenasinvocá-las.
Vamoscomeçarescrevendoafun çãoquenosdizqueojogadorperdeuo
jogo.Bastacontarmosonúmerodechutesincorretosqueeledeu.Casoeste
sejamaiorqueonúmerodetentativaspermitidas,eleperdeu.Nossafun ção
denominada enforcou()nosdevolverá1,seelefoienforcado;ou0,seainda
nãofoi.Onúmerodetentativasserá5(cabe ça,corpo,braços,pernasefim).
Alógicadessafun çãoseráaseguinte:declararemosinicialmenteumava-
riávelchamadaerros,quecontaráonúmerodeletrasqueousuáriochutou

## Página 139

CasadoCódigo
demaneiraincorreta.Essavariávelnosseráútilaofinal,pois,seelaformaior
ouiguala5,ojogadordeveráserenforcado.Faremosumloopnalistadechu-
tese,paracadachutedado,verificaremossealetraexistenapalavrasecreta.
Seexistir,quebramosoloopepassamosparaafrente. Aqui,utilizaremosa
mesmaestratégiaqueestamosusandoquandotemosloopsencadeados.Ava-
riávelexistenosajudaráasabersealetrafoiencontradanoloopdedentro.
Casocontrário,somaremos1àvariável erros,econtinuamos.
Veja,emcódigo:
int enforcou() {
int erros = 0;
// vamos fazer o loop em todos os chutes dados
for(int i = 0; i < tentativas; i++) {
int existe = 0;
// agora vamos olhar letra a letra da palavra secreta
// e ver se encontramos o chute aqui
for(int j = 0; j < strlen(palavrasecreta); j++) {
if(chutes[i] == palavrasecreta[j]) {
// encontramos, vamos quebrar o loop
existe = 1;
break;
}
}
// se não encontrou, soma um na quantidade de erros
if(!existe) erros++;
}
// se tivermos mais do que 5 erros, retornamos 1
// caso contrário, retornamos 0.
return erros >= 5;
}
Repareno returnemumalinha. Acostume-secomcódigosassim.
128

## Página 140

CasadoCódigo Capítulo12. Entradaesaída(I/O)
Lembre-sedequeamáquinavaiprimeiroavaliaroelementodadireita ou
seja,aexpressãocondicional,paradepoisfazeroretorno. Emoutraspala-
vras,se errosformaiorque5,elaavaliaráissopara1(verdadeiro);caso
contrário,0.Eafun çãoretornaráoresultadodisso.
Precisamosagorainvocaressafun ção.Comoelaestábemisolada,pode-
mosfacilmentetrocaravariável enforcou,quehavíamosdeclaradolána
nossa main(masquenuncausamos),pelainvocaç ãodafun ção.Precisamos,
claro,deletaravariável:
int main() {
int acertou = 0;
abertura();
escolhepalavra();
do {
desenhaforca();
chuta();
// aqui invocamos a função enforcou
} while (!acertou && !enforcou());
}
Sevocêrodaroprogramaagoraefizer5tentativaserradas,veráquenosso
programaparará.
Está perdido?
O código até o momento encontra-se em
http://pastebin.com/KndnEWkj
Conformevamosdesenvolvendonossosoftwareeaprendendocomele,
mudamosdeideia.Porexemplo,avariável tentativas,cujoobjetivoera
contaraquantidadedechutesdados,agoraficouambígua.Comessenome,
129

## Página 141

CasadoCódigo
tambémpoderiaseronúmerodechancesqueeletem.Seumnovatopegar
essecódigo,eleprecisarálermaisdocódigoparaentender.
Vamos,portanto, refatorarnossocódigo. Refatorarémudarocódigo,
geralmenteparamelhor,massemmudaroqueelefaz.Ouseja,deixá-lomais
bonitoefácildesermantido.Umarefatoraç ãocomumé,porexemplo,mudar
onomedascoisas,comovariáveis,métodosouatémesmoarquivos.
Trocaremosotermo tentativaspor chutesdados,quedeixabem
maisclarooqueelaguardalá.Precisamostrocarnadeclaraç ãoe,óbvio,em
todososlugaresqueausamos:
int chutesdados = 0;
Apróximaetapaédescobrirseganhamosounãoojogo. Aabordagem
seráamesma,porémao contrário.Passaremosprimeiropelapalavrasecreta.
Paracadaletra,descobriremosseousuáriojáachutou. Casoalgumaletra
nãotenhasidochutada,podemosmatarlogoafun çãoeretornarfalso. Ao
final,seelechutoutodasasletrasqueexistemnapalavra,eleganhouojogo.
Essafun çãoébemmaissimples,afinaljátemosafun ção jachutouque
nosdizseumaletrajáfoichutadaounão.Vamosapenaspassearpelapalavra
secretaeversealetrajáfoichutada.Seelanãofoi,entãonegaremoso ifefa-
remosum return 0.Notequepodemoster returnsaqualquermomento
donossocódigo;amáquinapararáafun çãonaquelemomentoeretornaráo
resultadodireto.Vamosdeclararessafun çãologoabaixoda jachutou():
int ganhou() {
for(int i = 0; i < strlen(palavrasecreta); i++) {
if(!jachutou(palavrasecreta[i])) {
return 0;
}
}
return 1;
}
Paravê-lafuncionar,bastatambémcolocarmossuainvocaç ãodentrodo
do-whileeremoverainútilvariável acertou. Pronto,nossojogoagora
paraseousuárioganhououperdeu:
130

## Página 142

CasadoCódigo Capítulo12. Entradaesaída(I/O)
int main() {
abertura();
escolhepalavra();
do {
desenhaforca();
chuta();
} while (!ganhou() && !enforcou());
}
Nossojogoagoratemcome ço,meioefim. Sónãoestábonito,maso
embelezamosmaistarde.
Erro de compilação?
Seucódigonãoestácompilando? Podeacontecer. Leiaapróxima
seção,naqualresolveremososeupossívelproblema.
Está perdido?
O código até o momento está em
http://pastebin.com/7eg47h7N
12.1 Header files
Éprovávelque,nessemomento,ocódigodealgunsleitoresdestelivrocom-
pile,edeoutrosnão.Reparequeemnenhummomentocomenteiondedeve-
moscolocarcadafun çãoquedeclaramos.Seráqueexisteumaordemespecí-
fica?Sim,existe.
OcompiladordalinguagemCnãoétãoesperto,eaordemdadeclaraç ão
dasfun çõeséimportante.Quandoocompiladorestápassandopeloarquivo,
131

## Página 143

12.1. Headerfiles CasadoCódigo
seeleencontraumainvocaç ãodefun çãoquenãoconhece,eleoptaporre-
clamar,emvezdecontinuareprocurarpeladeclaraç ãomaisàfrente(issoé
feitoporcompiladoresdelinguagensmaismodernas).Oerroquevocêdeve
tertomadoéparecidocomoseguinte:
forca.c:31:7: warning: implicit declaration of function
'jachutou' is invalid in C99 [-Wimplicit-function-declaration]
Entretanto,existeumamaneiraderesolverisso:declarandotodasasassi-
naturasdefun çõesqueaparecerãonaquelearquivo,antesdedarmosocódigo
delas.Aassinaturadeumafun çãoéaquelaprimeiralinhaqueusamospara
declará-la,quecontémotipoderetorno,onomeeosparâmetrosqueela
recebe.
Vamoscolocá-lastodas,umaauma,logoapósos includes.Aquioptamos
porcolocarantesdasvariáveisglobais,masnãohádiferen ça.
# include <stdio.h>
# include <string.h>
// lista de funções que aparecerão no arquivo
int enforcou();
void abertura();
void chuta();
int jachutou(char letra);
int ganhou();
void desenhaforca();
void escolhepalavra();
// variáveis globais
char palavrasecreta[20];
char chutes[26 ];
int chutesdados = 0;
// agora aqui começam as implementações das funções,
// do jeito que você está acostumado.
Notequeagoravocêpodeterassuasfun çõesemqualquerordem.Colo-
queafun ção ganhou()antesda jachutou(),porexemplo,evejaqueo
códigocompilanormalmente.
132

## Página 144

CasadoCódigo Capítulo12. Entradaesaída(I/O)
EsseéumproblemacomumdeprogramasescritosemC,eeleéainda
maisgravequandotemosnossocódigoespalhadoemarquivosdiferentese
queremosusarfun çõesdeumarquivoemoutro.Poressemotivo,apesarde
nossocódigofuncionarcomadeclaraç ãodessasfun ções,temosocostumede
colocarissoemumarquivoseparado.Essearquivoéconhecidocomo header
fileetemaextensão .h.
Reparequevocêjáviuessaextensãoantes. Éamesmaextensãodo
stdlib, stringetodososoutrosqueimportamos.Ouseja,emalgumlu-
gar,existeum stdlib.cquecontémaimplementaçãodasfun ções.Como
queremosusá-lasemnossoprograma,importamossuasdeclarações,quees-
tãotodasno .h.
Vamoscriaroarquivo forca.hecolocaressasdeclaraçõeslá:
// lista de funções que aparecerão no arquivo
int enforcou();
void abertura();
void chuta();
int jachutou(char letra);
int ganhou();
void desenhaforca();
void escolhepalavra();
Agora,emnosso forca.c,oimportaremos. Reparequeaquiusamos
aspasemvezdossinaisdemaioremenor.Afinal,esseéumheaderfilequeé
nossoeestánodiretóriocorrente:
# include <stdio.h>
# include <string.h>
# include "forca.h"
// variáveis globais
char palavrasecreta[20];
char chutes[26 ];
int chutesdados = 0;
// agora aqui começam as implementações das funções,
// do jeito que você está acostumado.
133

## Página 145

12.2. Lendoarquivos CasadoCódigo
Agora, semprequecriarmosumanovafun ção, precisamosdeclará-la
tambémnonossoheaderfile. Acostume-secomisso,pois,emnossopró-
ximojogo,dividiremosmelhorosarquivoseusaremosfun çõesparaláepara
cá,eelesserãoimportantes.
12.2 Lendo arquivos
Aúnicapartechatadojogoéqueapalavrasecretaestáfixa.Depoisqueele
adivinharaprimeiravez,acabou.Precisamosdarumjeitodefazercomque
apalavrasejarandômica.Criarnúmerosrandômicoséfácil,mascriarpala-
vrasquefaçamsentidoé,comcerteza,umproblemacomputacionalbastante
desafiador.
Oquefaremoséescolherumapalavraaleatóriadeumarquivodetexto,
queseránosso“bancodedadosdepalavras”.Essearquivopodeterqualquer
tamanho,ouseja,vocêpoderácolocarnovaspalavraslásemprequequiser,e
oprogramadeveentenderisso.
Vamoscome çarescrevendoumarquivodeexemplo.Semprequequiser-
moscriarumarquivoqueserálidopelocomputador,precisamosdefinirum
formato.Comosepararemosaspalavras?Porvírgula?Por enter?Oformato
éimportante,afinal,oprogramaprecisarásabercomointerpretá-lo.
Nossoarquivoteráoseguinteformato: aprimeiralinhanosindicará
quantaspalavrasexistemnaquelearquivo. Emseguida,teremosváriaspa-
lavras,umaemcadalinha. Issofacilitaráanossaleituraviacódigo. Vejao
arquivo,quechamaremosde palavras.txt:
3
MELANCIA
MORANGO
MELAO
Agoravamoscome çaralê-lo. Aprimeiracoisaqueprecisamosfazeré
abri-lo.Paraisso,precisamosdeclararumponteirodotipo FILE*,eusara
função fopen(),queabreumarquivododisco. Essafun çãonosdevolve,
então,umponteiroqueguardaremosnavariáveljádeclarada. Apartirdaí,
passamosessesponteirosparaasfun çõesquelerãooscaracteresdessear-
134

## Página 146

CasadoCódigo Capítulo12. Entradaesaída(I/O)
quivo.Repareno "r".Issoindicaqueestamosabrindo-osomenteparalei-
tura;entretanto,tambémpoderíamostê-loabertoparaescrita.
Todoocódigoestarádentrodafun ção escolhepalavra():
void escolhepalavra() {
FILE* f;
f = fopen("palavras.txt", "r");
}
EssaéaprimeiravezqueestamoslidandocomrecursosdeI/O,ouseja,
deentradaousaída.Naprática,elaspodemfalhar,poisoarquivopodenão
estardisponível,ounãotermospermissãodeleituraetc.Semprequelidamos
comisso,precisamostrataraspossíveisfalhas.
Afun ção fopen()devolveumponteirocomendere ço0,sealgumerro
ocorrer. Vamostrataressepossívelerro. Casoeletenhaocorrido,devolve-
remosumamensagemparaousuárioeacabaremoscomnossoprogramaali
mesmo,usandoafun ção exit()quefinalizaaaplicaç ão.Reparequeopa-
râmetro1,passadoao exit,indicaaosistemaoperacionalqueoprograma
terminoudemaneiraqueelenãogostaria;ouseja,umerroocorreu. Seti-
véssemosretornado0,osistemaoperacionalsaberiaqueoprogramarodou
deacordocomoesperado.Afun ção exit()estádeclaradaem stdlib.h.
Precisamoscolocaro include:
# include <stdlib.h>
void escolhepalavra() {
FILE* f;
f = fopen("palavras.txt", "r");
if(f == 0) {
printf("Banco de dados de palavras não disponível\n\n");
exit(1);
}
}
Agorasim,estamosprontosparacome çaralernossoarquivo,esabemos
quenaprimeiralinhatemosaquantidadedepalavrasqueleremosnasequên-
cia.Vamoscapturaressenúmero.Vocêjásabemaisoumenoscomolerdo
135

## Página 147

12.2. Lendoarquivos CasadoCódigo
arquivo. EmC,temosafun ção fscanf(),similaràquevocêjáconhece.
Suadiferen çaéqueoprimeiroparâmetroéoponteiroparaumarquivo.
Sequisermosleruminteirodeumarquivo,porexemplo,fazemosigual
aocódigoaseguir.Reparequeafun çãosabequeonúmero“acabou”quando
encontraum enternoarquivo.Ouseja,nessecaso,elalêatéacharumfimde
linha.
int qtddepalavras;
fscanf(f, "%d", &qtddepalavras);
Todavezquelemosdeumarquivo,aleituraésequencial.Emoutraspa-
lavras,sejácapturamosoprimeironúmero,apróximavezquechamarmos
afun ção fscanf(),elacontinuaráaleituradopontoqueparou. Écomo
seelativesseumapequenasetaqueapontaparaaposiç ãoqueestálendono
momento.
Vamosler,então,apróximacoisaqueaparecenoarquivo.Sabemosque
éumapalavra.Vamosdeclararumarrayeler,usandoamáscara %s.Dado
queemnossoexemplosabemosquetemos3palavras,vamosler3palavrasde
umasóvez,apenasparateste:
char palavra1[50];
fscanf(f, "%s", palavra1);
char palavra2[50];
fscanf(f, "%s", palavra2);
char palavra3[50];
fscanf(f, "%s", palavra3);
Nesse momento, se imprimirmos as 3 strings, teremosMELANCIA,
MORANGOe MELAO,igualesperávamos. Porém,nessenossojogoemparti-
cular,nãoprecisamossalvartodaselas,massimsomenteuma(aqueesco-
lhermosdemaneiraaleatória).Vamos,portanto,gerarumnúmeroaleatório,
de0atéaquantidadedeelementos,esalvarapenasapalavraqueestiverna-
quelaposição.
Nãotemoscomopulardiretoparaalinhaquequeremos,entãopreci-
saremosfazerumloopcomafun ção fscanf()e,nalinhacerta,salvaro
136

## Página 148

CasadoCódigo Capítulo12. Entradaesaída(I/O)
retorno. Parafacilitar,vamossalvarapalavrasecretajánavariávelcorreta
palavrasecreta.Reparequeaúltimainteraç ãodoloopserájustamentea
linharandômicaescolhida.Oloopacabaráeavariávelteráapalavrasecreta
quequeremos:
int qtddepalavras;
fscanf(f, "%d", &qtddepalavras);
// gera número aleatório
// não esqueça de incluir time.h
srand(time( 0));
int randomico = rand() % qtddepalavras;
// lê do arquivo até chegar na linha desejada
for(int i = 0; i <= randomico; i++) {
fscanf(f, "%s", palavrasecreta);
}
Nossocódigoestáquasepronto. Jáselecionamosumapalavraaleatória
dentrodonossobancodedadosdepalavras. Sóestamosnosesquecendo
deumacoisa:semprequelidamoscomI/O,precisamoslembrardeabriro
arquivo ouqualqueroutrafontedeentrada,usá-loe,aofinal,fechá-lo.
Fecharéimportante. Aofazerisso,aquelerecursoéliberadoparaque
outrosprogramasconsigamfazerusodeletambém.Quandoabrimosumar-
quivoparaleitura,osistemaoperacionalpodebloquearsualeituraemoutros
aplicativos,atéqueoprogramacorrentetermineseutrabalho.Ouseja,feche
omaisrápidopossível.Fazemosissocomafun ção fclose().
Ométodo escolhepalavra()completoficou:
void escolhepalavra() {
FILE* f;
f = fopen("palavras.txt", "r");
if(f == 0) {
printf("Banco de dados de palavras não disponível\n\n");
exit(1);
}
137

## Página 149

12.3. Escrevendonoarquivo CasadoCódigo
int qtddepalavras;
fscanf(f, "%d", & qtddepalavras);
srand(time(0));
int randomico = rand() % qtddepalavras;
for(int i = 0; i <= randomico; i++) {
fscanf(f, "%s", palavrasecreta);
}
fclose(f);
}
Repareque,aolongodestase ção,sóalteramosumpontodonossoar-
quivo,quefoiafun ção escolhepalavra().Etudofunciona.Vejasócomo
dividirnossoprogramaemfun çõesbemdefinidasérealmenteútil. Pode-
mosfazermudan çasempequenaspartesdoprogramasemnospreocupar-
moscomotodo.Éissoquefazumcódigoserfácildesermantido:quando
conseguimosmexerapenasempontosespecíficos,semanecessidadedeler
oualterartodoocódigo.
Está perdido?
O código até esse momento está em
http://pastebin.com/cAVVZFVw
12.3 Escrevendo no arquivo
Apróximafuncionalidadeemnossojogoéperguntaraousuárioseeledeseja
adicionarumanovapalavranobancodedados. Comoelafuncionará? Ao
finaldojogo,perguntaremosseeledesejafazerisso.Seeleresponder S(sim),
perguntaremosapalavraeaadicionaremosaoarquivo.
Vamoscomeçarpelapartefácil,queéperguntarseousuárioquerounão
adicionarumapalavra. Eisso,claro,emumanovafun ção,isoladadoresto
donossoprograma.Lembre-sedeque,comovamoscapturarumúnico char,
138

## Página 150

CasadoCódigo Capítulo12. Entradaesaída(I/O)
precisamoscolocarumespaçonamáscara,paraqueo scanf()ignoreo
enteraofinal:
void adicionapalavra() {
char quer;
printf("Você deseja adicionar uma nova palavra no
jogo (S/N)?");
scanf(" %c", &quer);
}
Seeleresponder S,perguntaremosaeleapalavra.Tambémnãoháno-
vidade:
void adicionapalavra() {
char quer;
printf("Você deseja adicionar uma nova palavra no
jogo (S/N)?");
scanf(" %c", &quer);
if(quer == 'S') {
char novapalavra[20];
printf("Digite a nova palavra, em letras maiúsculas: ");
scanf("%s", novapalavra);
// agora falta salvar no arquivo
}
}
Agoraprecisamossalvarnonossoarquivodebancodedados.Paraabrir
umarquivo,precisamosfazerusodafun ção fopen(),quejáconhecemos.
Oquemudarásãoosparâmetrosquepassaremosaela.O rindicavaleitura.
Usaremosaquio a,quesignifica append,ouseja,quevamosinserirnofim
doarquivo.
139

## Página 151

12.3. Escrevendonoarquivo CasadoCódigo
Comum FILEaberto, tudooqueprecisamosfazeréusarafun ção
fprintf(),análogaà printf(),quevocêjáconhece.Adiferen çaéque
oprimeiroparâmetroqueelarecebeéjustamenteoarquivoemqueelaes-
creverá.Vocêpercebeuqueo ftantoda fprintfquantoda fscanféde
file?.
Tambémnãoesqueceremosdetratarumpossívelerronaaberturadoar-
quivo.Elepodenãoteracontecidonocome çodojogo,maspodeacontecer
aofinal.Emcódigo:
if(quer == 'S') {
char novapalavra[20];
printf("Digite a nova palavra, em letras maiúsculas: ");
scanf("%s" , novapalavra);
FILE* f;
// abre arquivo
f = fopen("palavras.txt", "a");
if(f == 0) {
printf("Banco de dados de palavras não disponível\n\n");
exit(1);
}
// escreve a palavra nele
fprintf(f, "%s", novapalavra);
// fecha
fclose(f);
}
Atéomomento,aprendemosqueoponteiro FILE*apontaparaumar-
quivo,epassamosesseponteiroparatodasasoutrasfun çõesqueomanipu-
lam.O fscanf()conseguelerdadosdeumarquivoeo fprintfconse-
gueescrevernele.Mastudodependedaconfiguraç ãopassadaparaafun ção
fopen(). Sequisermosapenasler,usamos "r",esequisermos appendar
ouescreveraofinal,usamos "a".
140

## Página 152

CasadoCódigo Capítulo12. Entradaesaída(I/O)
Não esqueça de fechar o arquivo
Fecharoarquivocomo fclose()éespecialmenteimportanteem
momentosdeescrita.Issoporquemuitasvezesamáquinaoptapornão
escrevernodisconomomentoemquevocêinvocaum fprintf();
elaprefere“cachear”,ouseja,guardaramodificaçãoemmemóriaesó
salvarnodiscodepois.Elatomaessadecisãoporqueficarindoaodiscoe
escrevendofisicamentenele,depoucoempouco,podeserumaoperaç ão
demorada. Elaprefereesperarmaistextoeirdeumasóvezaodisco
rígido.
Aoperaçãodefechar,portanto,dizàmáquinaquevocêacaboutudo
oquetinhaqueescreverequeagora,independentedotamanhodesse
buffer,elaprecisaescrevernodisco. Seoprogramador,pordescuido,
esquecedefecharoarquivo,amáquinanãoescreveránele,eeleteráa
sensaçãodequeseucódigonãofuncionou. Assim,fechesempreoar-
quivoquevocêabriu.
Masvejaquesomenteescreveraofinalnãoésuficiente. Nossoarquivo
debancodedadostemumformatodiferente,poisaprimeiralinhaindica
aquantidadedepalavras. Ouseja,alémdeadicionarapalavra,precisamos
aindamodificaronúmeroqueestánocome ço.Paraisso,precisamosfazeruso
deumoutromododeaberturadearquivo.O "w",porexemplo,nosajuda
aescreveremarquivos,maselesóescreveemarquivosnovos. Emoutras
palavras,seoarquivoexistir,eleoapagaprimeiro.
Omodoqueprecisamosaquiéo r+.Elenospermitelerealterarumar-
quivo,sendoexatamenteoqueprecisamos.Oprimeiropassoéleronúmero
queestánocome çodoarquivo,incrementá-loesobrescrevê-lo.Emseguida,
adicionaranovapalavraaofinal.
Vamoscome çarabrindooarquivonessenovomodoelendoonúmero
queestánaprimeiralinha:
f = fopen("palavras.txt", "r+");
if(f == 0) {
printf("Banco de dados de palavras não disponível\n\n");
141

## Página 153

12.3. Escrevendonoarquivo CasadoCódigo
exit(1);
}
int qtd;
fscanf(f, "%d", &qtd);
Agora,precisamosincrementaressavariávelesobrescrevê-lanoarquivo.
Porém,comojálemosointeiro,o“ponteiro”queapontaparaolugardoar-
quivoquealeituracontinuaráestámaisàfrente.Precisamosvoltaressepon-
teiroeposicioná-lonolugarquedesejamoscome çaraescrever.Paramudaro
ponteirodeposição,usamosafun ção fseek().Elarecebetrêsparâmetros:
oarquivo,quantosbyteseladeveandar paraaesquerdaouparaadireita e
deondeeladevecome çaraandardocome çodoarquivo,daposiç ãocorrente
oudofinal.Vamosposicioná-la“0bytes”apartirdocomeçodoarquivo:
qtd++;
fseek(f, 0, SEEK_SET);
Repareque SEEK_SETéumaconstante. Poderíamosusartambéma
SEEK_CURparaandarapartirdopontoatual;oumesmo SEEK_END,para
andarapartirdofimdoarquivo.Comoponteiroposicionadonaposiç ãoque
queremos,bastaagoraescrevermosavariável qtd,usandoo fprintf().
Amáquinanãopensaráduasvezeseescreveráporcimadoqueestánaquela
posição:
fprintf(f, "%d" , qtd);
Agora,porfim,precisamosescreverapalavranofinaldoarquivo.Vamos
novamenteusar fseek()parairaofimdoarquivo,e fprintf()para
escreverapalavra. Repareno \nnocome çodastring. Precisamosdisso,
poisoponteironosposicionabemaofinaldoarquivoque,teoricamente,não
temum enternofim.Escrevemosum entere,aísim,apalavra:
fseek(f, 0, SEEK_END);
fprintf(f, "\n%s", novapalavra);
Pronto. Agoraojogadorpodeadicionarnovaspalavrasaofinaldapar-
tida:
142

## Página 154

CasadoCódigo Capítulo12. Entradaesaída(I/O)
void adicionapalavra() {
char quer;
printf("Você deseja adicionar uma nova palavra no
jogo (S/N)?");
scanf(" %c", &quer);
if(quer == 'S') {
char novapalavra[20];
printf("Digite a nova palavra, em letras maiúsculas: ");
scanf("%s", novapalavra);
FILE* f;
f = fopen("palavras.txt", "r+");
if(f == 0) {
printf("Banco de dados de palavras não
disponível\n\n");
exit(1);
}
int qtd;
fscanf(f, "%d" , &qtd);
qtd++;
fseek(f, 0, SEEK_SET);
fprintf(f, "%d", qtd);
fseek(f, 0, SEEK_END);
fprintf(f, "\n%s", novapalavra);
fclose(f);
}
}
143

## Página 155

12.4. MaissobreI/O CasadoCódigo
Está perdido?
O código até o momento está em
http://pastebin.com/FAM8pA1w
12.4 Mais sobreI/O
AbibliotecadeentradaesaídadalinguagemCébastanteextensa.Mesmoas
funçõesestudadasaquipodemfazermuitomaisdoqueomostrado. Todas
asfun ções,porexemplo,possuemretorno.Aprópria fscanf()retornao
númerodeitensdevolvidos.Porexemplo,seamáscarafor %d,elaretornará
1,casotudodêcerto.Seamáscarafor %d %d,ouseja,capturar2inteiros,ela
retornará2.
int n1, n2;
int sucesso = fscanf("%d %d", &n1, &n2);
if(sucesso == 2) {
printf("Os dois números: %d e %d", n1, n2);
}
else {
printf("Aconteceu um erro");
}
Podemosverificartambémseoponteiroatualdoarquivoestáapontando
paraofim.Paraisso,bastausarafun ção feof().Elepodeserbastanteútil
quandoqueremosleroarquivointeiroatéofim.Porexemplo,sequisermos
lercaractereporcaracteredoarquivoeimprimi-lo,precisamosrepetirisso
enquantonãochegarmosaofimdoarquivo.
Por enquanto, a única função de leitura que vimos até então é a
fscanf().ElaéimportantequandoqueremoslercaracteresASCIIestrings.
Mas,muitasvezes,precisamoslerumbyte,umchar,oumesmouma struct
(queaprenderemosnopróximojogo).Nessescasos,precisamoslereescrever
dadosdemaneira“maisbruta”.Afunção fgetc(),porexemplo,lêapenas
opróximo char.
144

## Página 156

CasadoCódigo Capítulo12. Entradaesaída(I/O)
FILE* f;
char c;
f = fopen("arquivo.txt", "r");
while(!feof(f)) {
c = fgetc(f);
printf("Char %c\n", c);
}
Nessescasos,tambémasfun ções fread()e fwrite()podemajudar.
Elasleemumaquantidadeespecíficadebyteseasguardamnaestruturaque
vocêpassar,sejaelaumarray,umavariávelouumastruct.Nopróximojogo,
faremosusodelas.
Percebaquedaquiparafrentevocêcome çaráaaprenderefazeruso
defun çõesquesãocomplexasefazemmuitacoisa. Amelhormaneirade
entendê-lasmelhoréleromanualoficial.Nisso,oGoogleoajudará.Sempre
quetiverdúvidadosparâmetrosqueumafun çãorecebe,oqueelaretornae
comointerpretaresseretorno,procurepelasuadefiniç ãonainternet.Buscar
étambémpartedodiaadiadoprogramador.
12.5 Resumindo
Nestecapítulo,aprendemos:
• Acriareusarheaderfilespróprios;
• Amanipularentradaesaída;
• Aabrirarquivoscomfopen;
• Ausarmodosdiferentesdeabrirarquivo,comosóleituraousóescrita;
• Alereescrevercomfscanfe fprintf;
• QueabibliotecadeI/Oégrande,eprecisamosbuscarsemprepeloma-
nualdasfun ções.
145

## Página 158

Capítulo13
Finalizandoojogo
Nossojogoestáinteirofuncional.Faltaagoraodeixarmosmaisapresentável
paraojogador.Afinal,interfaceéimportante.Vamosmelhorá-la,eaprovei-
tarparaaperfeiçoaralgunsdetalhestambémnocódigo,poisjásabemosque,
quantomaislegível,melhor.
13.1 Evitando repetição de código
Repetiçãodecódigoéalgosempreproblemático.Setemosomesmopedaço
decódigoemmuitospontosdaaplicaç ão,issoimplicaemalterartodosos
pontosquandonecessário.Infelizmente,naprática,muitasvezesnãopropa-
gamosaalteraç ãoparatodososlugaresnecessários,eissonostrazbugs.
Vocêjátemferramentasparaevitaressetipodeproblema.Seháumtre-
chodecódigoqueécomumparaváriaspartesdoseuprograma,bastaextraí-
loecolocá-loemumafun ção.Fun çõessãofacilmentereutilizáveis.Esevocê

## Página 159

13.2. Extraindofunções CasadoCódigo
alterá-las,todososlugaresqueasinvocamfarãousodanovafun ção.
Tambémjávimosquequandotemosalgum“númeromágico” ouseja,
umnúmerofixo,podemoscolocá-loemumaconstante. Aconstantepode
serfacilmentereaproveitadaepossuiumnomesemântico,muitomelhordo
quedeixaronúmerojogado.E,seaalterarmos,amudan çapropagarápara
todososlugaresqueausam.
Nossojogodeforcatemumnúmeromágico,quejáestáespalhadopelo
código.Vejaqueotamanhomáximodeumapalavraemnossojogoé20ca-
racteres. Issoestádefinidonadeclaraçãodoarray palavrasecreta. Se
quisermosmudarotamanhodapalavra,precisaremosmudaradeclaraç ão
doarray. Masnãoésóisso:énecessáriomudartambémdentrodafun ção
adicionapalavra(),poisládeclaramosumarraycomomesmotama-
nho.Nomomento,sãoapenas2pontos;porémamanhãserão3,edepoisde
amanhã,4.
Vamosjácorrigirisso,criandoumaconstanteparaisso.E,dessavez,va-
moscolocá-lanoheaderfile.Faremosum #defineporlá,eoreutilizaremos
emnossocódigo.Veja:
// forca.h
# define TAMANHO_PALAVRA 20
// forca.c
char palavrasecreta[TAMANHO_PALAVRA];
void adicionapalavra() {
// ...
char novapalavra[TAMANHO_PALAVRA];
}
13.2 Extraindo funções
Atéentão, sómostramosonúmerodechutesdadospelojogador, masa
partemaislegaldojogodeforcaéjustamenteexibirohomenzinhoenfor-
cado. Vamoslá,então,fazerumdesenhomaisamigáveldentrodafun ção
desenhaforca():
148

## Página 160

CasadoCódigo Capítulo13. Finalizandoojogo
void desenhaforca() {
printf(" _______ \n");
printf(" |/ | \n");
printf(" | (_) \n");
printf(" | \\|/ \n");
printf(" | | \n");
printf(" | / \\ \n");
printf(" | \n");
printf("_|___ \n");
printf("\n\n");
// ...
}
Entretanto,nãopodemosexibirobonecocheiootempointeiro.Issode-
pendedonúmerodeerros.Seonúmerodeerrosé0,exibimosapenasacorda.
Seeleerrou1vez,exibimosacabe ça;2vezes,acabe çaeocorpo;3vezes,a
cabeça,ocorpoeosbraços;4vezes,acabe ça,ocorpo,osbraçoseaspernas.
Precisamossaberonúmerodevezesqueojogadorjáerrou.Játemosalgo
parecidonafun ção enforcou().Elacalculaonúmerodeerrosedepoisnos
retornaseessaquantidadeémaiorque5.Maselanãonosserveexatamente,
porqueprecisamossaberaquantidadeexatadeerros.Ouseja,precisamossó
deumpedaçodessafun ção.
Obviamente, não temos como utilizar parte de uma função. Porém,
podemosquebrá-laemduasoutrasmenores. Vamosdividiressafun ção
enforcou()emduas:uma,nova, chuteserrados(),quecalculaonú-
merodechuteserrados;eaoutra,jáexistente,quefaráusodanovafun çãoe
nosretornaráverdadeiroseessenúmeroformaiorque5:
// extraímos para cá o pedaço daquela função
// que contava a quantidade de erros
int chuteserrados() {
int erros = 0;
for(int i = 0; i < chutesdados; i++) {
int existe = 0;
149

## Página 161

13.2. Extraindofunções CasadoCódigo
for(int j = 0; j < strlen(palavrasecreta); j++) {
if(chutes[i] == palavrasecreta[j]) {
existe = 1;
break;
}
}
if(!existe) erros++;
}
return erros;
}
int enforcou() {
// usamos a função que acabamos de criar
return chuteserrados() >= 5;
}
Quebrarfun çõesemfun çõesmenoresépartedonossodiaadia. Fa-
zemosissoparareutilizarpedaçosdefun çõesjáexistentes,oumesmopara
aumentaralegibilidade.Vejaqueafun ção enforcou()agoratemumali-
nhadecódigoeébemfácildeentenderoqueelafaz:seeleerroumaisde5
chutes,retornafalso.Qualquerdesenvolvedorgastamuitopoucotempopara
entendê-la.
Vamosaproveitareextrairmaisumafun ção.Repareque,dentrodafun-
ção chuteserrados(),temosumloopquenosdizseumaletraexisteou
nãonapalavrasecreta.Paraafun çãocomoumtodo,issoéusadoparacon-
tabilizaraquantidadedechuteserrados.Massóoalgoritmoquenosdizse
umaletraexistenapalavranosseráútilmaisparafrente.Extraindo,temos:
int letraexiste (char letra) {
for(int j = 0; j < strlen(palavrasecreta); j++) {
if(letra == palavrasecreta[j]) {
return 1;
}
}
150

## Página 162

CasadoCódigo Capítulo13. Finalizandoojogo
return 0;
}
int chuteserrados() {
int erros = 0;
for(int i = 0; i < chutesdados; i++) {
if(!letraexiste(chutes[i])) {
erros++;
}
}
return erros;
}
Lembre-sedeque,quantomenorafun ção,maisfácilelaserumaentidade
ereutilizada.
13.3 Ifs ternários
Comessafun çãoemmãos,bastaagorafazemosumasequênciade ifs,im-
primindoobonecodeacordocomonúmerodeerros.Porexemplo,os ifs
para0e1erros:
int erros = chuteserrados();
if(erros == 0) {
printf(" _______ \n");
printf(" |/ | \n");
printf(" | \n");
printf(" | \n");
printf(" | \n");
printf(" | \n");
printf(" | \n");
printf("_|___ \n");
}
if(erros == 1) {
151

## Página 163

13.3. Ifsternários CasadoCódigo
printf(" _______ \n");
printf(" |/ | \n");
printf(" | (_) \n");
printf(" | \n");
printf(" | \n");
printf(" | \n");
printf(" | \n");
printf("_|___ \n");
}
// e assim por diante...
Aideianãoéruim.Masnossocódigoficarábemextenso.Percebaque,
nofim,oquequeremosfazeréimprimirounãoumdeterminadocaractere,
dependendodovalordavariável erros. Vamosisolaressescaracteresno
próprio printf(),fazendousodamáscara %c:
printf(" _______ \n");
printf(" |/ | \n");
printf(" | %c%c%c \n", '(', '_', ')');
printf(" | %c%c%c \n", '\\', '|', '/');
printf(" | %c \n", '|');
printf(" | %c %c \n", '/', '\\');
printf(" | \n");
printf("_|___ \n");
printf("\n\n");
Agora,oscaracteresdoladodireitosãoosqueprecisamosimprimirde
acordocomavariável erros.Vejaoprimeiroqueaparece,o ‘(’,porexem-
plo.Elefazpartedacabe ça;portanto,precisamosimprimi-lose erros >=
1.Casocontrário,podemosimprimir“vazio”.
Notequetemosum ifbemcurto:se erros >=1,imprime ")";senão
" "(vazio).Essetipode ifquetemumacondiç ão,umvalorderetornono
casoverdadeiro,eoutronocasodefalso,épossíveldeserfeitoemumasó
linha.Chamamosissode ifternário.
A sintaxe de um if ternário é a seguinte:(condicao ? valor
verdadeiro : valor falso).Reparenopontodeinterrogaç ãoquese-
152

## Página 164

CasadoCódigo Capítulo13. Finalizandoojogo
paraacondiç ãodovalorverdadeiro,enodois-pontosquedivideovalor
usadonocasodacondiç ãofalsa. Essetipodeiféusado inline,ouseja,na
mesmalinhadeoutrainstruç ão. Vamosusarjuntocomo printf(),por
exemplo.Observeocódigoaseguir,quebradoemváriaslinhasparafacilitar
alegibilidade:
printf(" | %c%c%c \n",
(erros >=1 ? '(' : ' '), // Aqui o if ternário
'_',
')'
);
Amáquinafaráesse ifnahoradeexecutaro printfe,dependendo
daavaliaçãodacondiç ão,eleretornaráumvalorououtroparaserimpresso.
Podemosfazerissoparatodasaspartesdonossoboneco,cadaumdeacordo
comasuarespectivaquantidadedeerros. Olhe(edigite)essecódigocom
carinho,poiseleéextensoecheiodecaracteres:
int erros = chuteserrados();
printf(" _______ \n");
printf(" |/ | \n");
printf(" | %c%c%c \n", (erros>=1?'(':' '),
(erros>=1? '_':' '), (erros>=1?')':' '));
printf(" | %c%c%c \n", (erros>=3?'\\':' '),
(erros>=2? '|':' '), (erros>=3?'/': ' '));
printf(" | %c \n", (erros>=2?'|':' '));
printf(" | %c %c \n", (erros>=4?'/':' '),
(erros>=4? '\\':' '));
printf(" | \n");
printf("_|___ \n");
printf("\n\n");
Pronto. Vejacomoousodoifternárionosajudouaeconomizarboas
linhasdecódigo.Imaginerepetirmosessebonecoummontedevezes?Nosso
arquivoficariagigante.
153

## Página 165

13.4. Últimosdetalhes CasadoCódigo
Está perdido?
O código feito até o momento está em
http://pastebin.com/z9ZDU7Bf
13.4 Últimos detalhes
Vamosagoraexibirumamensagemcadavezqueelechutarumaletra,di-
zendoseeleacertouounão. Colocaremosessecódigodentrodafun ção
chute(),aqualpegaochutedojogador.Saberseumaletraexisteounãona
palavrasecretaéfácil:bastainvocarafun çãoqueextraímoshápoucotempo:
letraexiste().
void chuta() {
char chute;
printf("Qual letra? ");
scanf(" %c", &chute);
if(letraexiste(chute)) {
printf("Você acertou: a palavra tem a letra %c\n\n",
chute);
} else {
printf("\nVocê errou: a palavra NÃO tem a letra %c\n\n",
chute);
}
chutes[chutesdados] = chute;
chutesdados++;
}
Agoraprecisamosexibiramensagemdeganhououperdeuparaousuá-
rio;afinal,ojogoestáacabandosemdizeroqueaconteceu.Todaessalógica
deveexistirlogoapóso do-whileprincipal. Ali,bastainvocarmosnova-
menteafun ção ganhou()eimprimiramensagemdesucessoquequeremos.
Vamosaproveitareexibirumacaveiracasoeletenhaperdido:
154

## Página 166

CasadoCódigo Capítulo13. Finalizandoojogo
if(ganhou()) {
printf("\nParabéns, você ganhou!\n\n" );
printf(" ___________ \n");
printf(" '._==_==_=_.' \n");
printf(" .-\\: /-. \n");
printf(" | (|:. |) | \n");
printf(" '-|:. |-' \n");
printf(" \\::. / \n");
printf(" '::. .' \n");
printf(" ) ( \n");
printf(" _.' '._ \n");
printf(" '-------' \n\n");
} else {
printf("\nPuxa, você foi enforcado!\n");
printf("A palavra era **%s**\n\n", palavrasecreta);
printf(" _______________ \n");
printf(" / \\ \n");
printf(" / \\ \n");
printf("// \\/\\ \n");
printf("\\| XXXX XXXX | / \n");
printf(" | XXXX XXXX |/ \n");
printf(" | XXX XXX | \n");
printf(" | | \n");
printf(" \\__ XXX __/ \n");
printf(" |\\ XXX /| \n");
printf(" | | | | \n");
printf(" | I I I I I I I | \n");
printf(" | I I I I I I | \n");
printf(" \\_ _/ \n");
printf(" \\_ _/ \n");
printf(" \\_______/ \n");
}
Pronto.Nossojogoestáterminado.Evejaoquantovocêprecisouapren-
derparafazê-lo.
155

## Página 167

13.5. Resumindo CasadoCódigo
Código final
Ocódigofinaldojogopodeservistoaqui:
http://pastebin.com/Qu3dDdRZ
13.5 Resumindo
Nestecapítulo,aprendemos:
• Aquebrarfunçõesemfun çõesmenores;
• Ausarconstantesparaevitarnúmerosmágicosrepetidos;
• Ifsternários.
156

## Página 168

Capítulo14
Exercícios
Agoraésuavezdepraticar!
14.1 Jogo de adivinhação
1) Mudeoloopprincipaldojogoparaum do-while,igualfizemosnojogo
deforca.
14.2 Jogo de forca
1) Nãopermitirqueousuáriodigitenadaalémdeletrasmaiúsculas. Dica:
Imprima a letra ‘ A ’ e a letra ‘Z’ como inteiros (usando%d) e descubra seus
números. Em seguida, faça um if proibindo o caractere digitado de ser fora
desse intervalo.

## Página 169

14.3. Outrosdesafios CasadoCódigo
2) Nãopermitirqueousuárioinsiraumapalavraquejáexistanoarquivode
palavras.
3) Sópossibilitarainser çãodeumanovapalavracasoojogadorganheojogo.
4) Pergunteaousuáriooníveldedificuldadequeelequerjogar.Deacordo
comonível,vocêtemmaisoumenoschutes.
5) Afunção enforcou()temcódigorepetido.Vocêpodefazerusodafun-
ção jachutou()ediminuiraduplicaç ãodecódigo.
6) Vocêdeveterreparadoque,aoadicionarmosadécimapalavra,teremos
umproblema.Issoporquesempreescrevemosemcimadoquejáestáno
arquivo.Ecomo“10”émaiordoque“9”,temosumbyteamais,eoarquivo
ficadesposicionado(o entersome).Pararesolveresseproblema,combine
queonúmeroserásempreescritocom4algarismos(0001,0009,0021,
eassimpordiante). Assim,garantimosquenossoprogramafuncionará
bemparaaté9999palavras.Paraqueissofuncioneno printf,passamos
"%04d"comomáscara.Façaessaalteraç ãonojogo.
7) Aofinaldojogo,pergunteonomedousuárioesalve-oemumarquivo
ranking.txt,juntocomasuapontuaç ão.
14.3 Outros desafios
1) Escrevaumafunçãoquerecebadoisinteiros, ae b,ecalculeapotência
a^b ouseja, aelevadoa b.
2) Escrevaumprogramaquepe çaumnúmeroaousuárioe,comessenú-
mero,façaoprogramaescreverumarquivo tabuada.txtcomatabu-
adade1até20daquelenúmero.Supondoonúmero2deentrada,asaída
devesernoformato 2 x 1 = 2,eassimpordiante.
3) Dadosneumasequênciade nnúmerosinteiros,determinarasomados
númerospares.
4) Escrevaumafun çãoquenosdizseumnúmeroéprimoounão.
158

## Página 170

CasadoCódigo Capítulo14. Exercícios
5) Escrevaumprogramaquerecebe2númerosecalculaasomadosnúmeros
quesãoprimosnointervalo.
6) Escrevaumafun çãoquerecebaumarraydeinteirosesometodososele-
mentosdentrodessearray.
159

## Página 172

Capítulo15
JogoFoge-foge
Nossopróximojogoserábatizadode Foge-foge. Eleémuitosimilaraofa-
mosoPac-Man,queprovavelmentevocêjájogou. Nossoheróipasseiapelo

## Página 173

15.1. Comonossojogovaificar? CasadoCódigo
mapa,masprecisatercuidadocomosfantasmas.Afinal,sealgumencostar
nele,vocêperdeojogo.E,cuidado,osfantasmasandamdemaneiraaleatória!
Noentanto,onossoheróitambémtemseustruques.Seeletiverapílula
mágica,elepoderáexplodirmuitosfantasmasdeumasóvez.
Fazerumjogodessesnãoéfácil. Aquiaprendemosmuitacoisanova,
como:
• Criar,varreramanipularmatrizes(ouarraysbidimensionais);
• Alocarmemóriadinamicamente;
• Criarestruturas(tipos)próprias;
• Fazerfunçõesrecursivas;
• Usarfunçõesmaisavan çadasdemanipulaçãodestringsedememória;
• Usarponteirosdeponteiros;
• Usaroutrasdiretivasdecompilação.
15.1 Como nosso jogo v ai ficar?
Odesenhoaseguirmostracomoseráasaídafinaldonossojogo. OFoge-
fogeandapelomapa,usandoasteclas A, S, D, W.Eleprecisadesviardas
paredesetentardestruirosfantasmas.SevocêjájogouCounterStrike,vaise
sentiremcasa!
Semprequeoheróiandar,teremosumnovomapaimpresso.
Pílula: NÃO
............................................................
............................................................
............................................................
............................................................
...... .-. .-. .-. ...... ......
......| OO| | OO| | OO| ...... ......
......| | | | | | ...... ......
......'^^^' '^^^' '^^^' ...... ......
162

## Página 174

CasadoCódigo Capítulo15. JogoFoge-foge
...... ......
...... ......
...... ......
...... ......
...... .-. .-. .--. ...... ......
......| OO| | OO| / _.-'...... ......
......| | | | \ '-....... ......
......'^^^' '^^^' '--' ...... ......
...... .-. ...... ......
...... | OO| ...... ......
...... | | ...... ......
...... '^^^' ...... ......
............................................................
............................................................
............................................................
............................................................
15.2 É hora de começar!
Estáprontoparadesenvolveressejogo? Mãosàobra!
163

## Página 176

Capítulo16
Matrizes
Oprimeiropassoparaaimplementaç ãodoFoge-fogeépensarnomapaem
quenossoheróiandará.Nele,precisamosrepresentartudooquepodeexistir
porlá,como: paredes,monstros,opróprioherói,elugarespelosquaisele
podepassar.
Podemosrepresentarummapapormeiodeváriaslinhasecolunas.Em
cadaposição,teríamosumcaracterequerepresentariaoquetemali.Vejao
exemplodomapaaseguir,noqualoponto( .)significa“caminholivre”,o
arroba( @)representanossoheróieoscaracteres |e -seriamasparedes:
0123456789
0 |--------|
1 |...|..-.|
2 |..-|.@..|
3 |......-.|
4 |--------|

## Página 177

CasadoCódigo
Nossoheróiqueestánalinha2dacoluna6podeandarparaesquerda,
direita,cimaoubaixo. Masnãopodeandarduasvezesseguidasparaaes-
querda,porexemplo,poisháumaparedeali.
Podemosrepresentarcadalinhadessemapapormeiodeumarrayde
chars.Comocadalinhatem10posições,entãoumarrayde10posiçõesresol-
veria.Ecomotemos5linhas,precisamosde5dessesarrayspararepresentar
todoomapa:
char linha1[10];
char linha2[10];
char linha3[10];
char linha4[10];
char linha5[10];
Claramenteessanãoéumaboasoluç ão.Imaginesetivéssemosummapa
com50linhas?Precisaríamoster50variáveisdessas.Manipulá-lasnãoseria
fácil. Asoluçãoparaissoédeixardeusarvetoresepassarausar matrizes.
Matrizes,assimcomonamatemática,éumaestruturaretangulardedados,
ouseja,nosso“linhasecolunas”.
166

## Página 178

CasadoCódigo Capítulo16. Matrizes
Fig.16.1:Matrizes
Sequisermosumamatrizdecharsde5x10,declaramosumavariávelpara
tal.ParadeclararmosmatrizesemC,bastarepetirmosduasvezesoconjunto
de [];umparalinhaseoutroparacolunas,respectivamente:
char mapa[5][10];
Acessarealterarvaloresdasposiçõeséanálogoaousodevetores,coma
diferençaqueagorapassamosambasasposições:
// armazenando na posição 0x0
mapa[0][0] = '|';
// imprimindo a posição 2x3
printf("%c" , mapa[2][3]);
Paraquenossojogofiqueinteressante,vamoslê-lodeumarquivo.Nosso
programadevelerlinhaalinhaesalvá-lonamatriz mapa.Vamoscome çar
abrindooarquivo,dojeitoquejáconhecemos:
167

## Página 179

CasadoCódigo
FILE* f;
f = fopen("mapa.txt", "r");
if(f == 0) {
printf("Erro na leitura do mapa");
exit(1);
}
Agoraprecisamosmudaradeclaraç ãodonossomapa.Apesardeleter10
caracteresnalinha,precisamoslembrarque,quandousarmoso fscanf(),
passandoumastringcomomáscara,elecolocaráum \naofinal.Podemos
tambémusarasfun çõesdeleituraquevimosnofinaldocapítulo 12,como
a fread(),elerbyteabyte,masissonosdariaumtrabalhodesnecessário.
Vamosdeclararoarraycomumaposiç ãoamaisemcadalinha,apenaspara
guardaro enter:
char mapa[5][10+1];
Agora,bastalermoslinhaalinha. Comosabemosquetemos5linhas
exatas,bastafazermosum for.Nocapítulo9,discutimosqueumarray/vetor
ésimplesmenteumponteiroqueapontaparaumaposiç ãodamemóriaque
temespaçosvaziosparaguardaras nposiçõesdeclaradas.
Umamatrizéumaabstraç ãoaindamaior.Elaéumponteiroqueaponta
paraumalistadearrays.Comoarrayssãoponteiros,logo,umamatrizéum
ponteiroqueapontaparaumalistadeponteiros.
Ouseja, mapaéumponteiroqueapontaparaoutrosponteiros. Isso
significaque mapa[0]éumponteiroqueapontaparaumarray, mapa[1]é
umponteiroqueapontaparaoutroarray,eassimpordiante.Vejanaimagem
aseguirofuncionamentodeumamatriz:
168

## Página 180

CasadoCódigo Capítulo16. Matrizes
Fig.16.2:Matrizeseponteiros
16.1 Ponteiros de ponteiros
Emcódigo,nadanosimpedededeclararmosumamatrizedepoisdeclarar
ponteirosqueapontamparacadaumdosvetoresdentrodessamatriz.Veja
ocódigoaseguir. linha0[0]éiguala numeros[0][0],afinaltanto
linha0quanto numeros[0]apontamparaomesmoendere çodememória.
int numeros[5][10];
int* linha0 = numeros[0];
int* linha1 = numeros[1];
int* linha2 = numeros[2];
int* linha3 = numeros[3];
int* linha4 = numeros[4];
// os números serão iguais, afinal
// ambos ponteiros apontam para o mesmo
// endereço de memória
printf("%d %d" , linha0, numeros[0]);
Ouseja,nesseloopquefaremos,guardaremosaprimeiralinhanoarray
mapa[0],asegundalinhanoarray mapa[1],eassimpordiante.Vejaque
nessecódigo,declaramos int*pararepresentarcadaarrayqueestádentro
169

## Página 181

16.1. Ponteirosdeponteiros CasadoCódigo
damatriz.Masesequiséssemosumnovoponteiroparaapontarparaamatriz
comoumtodo?Comoelaéumponteiroqueapontaparaoutrosponteirosde
inteiro,adeclaraç ãoé int**,ouseja,duasestrelaspararepresentar“pon-
teirodeponteiro":
int numeros[5][10];
// o ponteiro copia é idêntico ao
// ponteiro numeros... ambos apontam
// para uma lista de ponteiros de inteiros
int** copia = numeros;
// as duas operações abaixo são idênticas
numeros[0][ 0] = 10 ;
copia[0][0] = 10;
Ouseja,enquantoumarrayéumponteiroparaumalistadeposições
dememóriaqueestãolivresparaguardarotipoescolhido,umamatrizéum
ponteiroqueapontaparaumalistadeponteiros,queapontamparaposições
dememórialivresparaguardaralgo.
Comissoemmãos,podemosagorafazeroloopparacapturaraslinhas
doarquivo. Apontamos mapa[i]comoolugarondeoscaracteresdevem
sercolocados:
for(int i = 0; i < 5; i++) {
fscanf(f, "%s" , mapa[i]);
}
Podemosimprimiromapademaneirasimples,porenquanto:
for(int i = 0; i < 5; i++) {
printf("%s\n", mapa[i]);
}
Porfim,precisamosfecharoarquivo:
fclose(f);
Pronto.Jáestamoslendoamatrizdemapadeumarquivo.Maspodemos
melhoraraindamais.
170

## Página 182

CasadoCódigo Capítulo16. Matrizes
Está perdido?
O código até o momento está em
http://pastebin.com/QxtGZR4B
Ponteiros de função
Acrediteounão,podemosterponteirosqueapontamparafun ções
também.Entretanto,esseéumassuntoquenãoéabordadonestelivro,
devidoàsuacomplexidade.
16.2 Alocação dinâmica de memória
Masesequisermosmapascomtamanhosdiferentes,para,porexemplo,di-
ferenciaroníveldojogo?Quantomaisdifícil,maioromapa.Ograndepro-
blemaé:comovariarotamanhodamatriz?
Umapossívelestratégiaseriaterumamatrizgigantequesuportasseo
maiormapapossível.Porexemplo,umamatriz mapa[100][100].Nosso
programaolhariaapenasparaaquantidadedelinhasecolunasdaquelemapa
emparticular,queserásempremenorque100x100.
Aqui,tomaremosoutradecisão: adegerarumarray(oumatrizes)de
tamanhosaleatórios. Leremosoartigo,descobriremosotamanhodomapa
e,então,declararemosumamatrizcomotamanhoideal.
Parafazerisso,precisamosmudaramaneiradedeclararmosnossoarray,
alocandoamemórianecessáriaemtempodeexecuç ão.Paraisso,usaremos
afun ção malloc().Elarecebecomoparâmetroaquantidadedebytesque
precisaseralocado,enosdevolveumponteiroparaoprimeirobytealocado.
Ocódigoaseguir,porexemplo,alocaumúnicobyte.Comoelenosde-
volveumponteiro,oseuretornopodeserarmazenadoemumponteirode
char:
char* letra = malloc( 1);
*letra = 'M';
171

## Página 183

16.2. Alocaçãodinâmicadememória CasadoCódigo
Sequiséssemosguardarum int,precisaríamosdemaisde1byte;afinal,
inteirossãorepresentadospor4bytes.Ocódigoseriaalgocomo:
int* numero = malloc(4 );
*numero = 20;
printf("%d" , *numero);
Mascomoaquantidadedebytesqueuminteiroocupapodevariarde
plataformaparaplataforma, émelhordizermosaocompiladorparausar
otamanhodointeirodaquelaplataforma. Paraisso, usamosainstruç ão
sizeof(int),quenosretornaotamanhocorreto:
int* numero = malloc(sizeof(int));
*numero = 20;
printf("%d" , *numero);
Comoo malloc()simplesmentealocaaquantidadedebytesdesejada
enosdevolveumponteiro,paradeclararmosumarraydemaneiradinâmica,
bastaapenaspassarmosaquantidadedebytescorretos.Porexemplo,sequi-
sermosumarraydeinteirosde10posições,precisamospassar40paraele(4
bytesporinteirovezes10inteiros).Comessenúmero,sabemosquepodemos
manipularumponteirocomosefosseumarray:
// calcula o tamanho de bytes
int colunas = 10;
int memoria = sizeof(int) * colunas;
// aloca memória suficiente para o array
int* numeros = malloc(memoria);
// usa o ponteiro como se fosse um array
numeros[0] = 10;
printf("%d" , numeros[2]);
Jáparaumamatriz,temosmaisdeumaabordagem.Imagineumamatriz
de5linhaspor10colunas.Precisamosprimeiroalocarumarrayparaguardar
5ponteirosdeinteiros.Depois,alocardezarraysde5arraysde10posições,e
guardarcadaumdessesarraysnosponteirosdeinteirosdeclaradosanterior-
mente.
172

## Página 184

CasadoCódigo Capítulo16. Matrizes
Vejaemcódigo:
int** matriz;
int linhas = 5;
int colunas = 10;
// alocando espaço para as linhas,
// que guardam ponteiro de inteiro.
matriz = malloc(sizeof(int*) * linhas);
// agora, para cada linha, alocamos
// espaço para um array com 10 ("colunas") posições.
for(int i = 0; i < linhas; i++) {
matriz[i] = malloc(sizeof(int) * colunas);
}
// agora podemos usar 'matriz' como uma matriz
matriz[2][3 ] = 10;
Éissooquefaremos.Vamosrecome çarnossocódigojáoseparandoem
funções(códigoorganizado,sempre).Vamosdeclararalgumasvariáveisglo-
baisqueserãoimportantesaolongodojogo:otamanhodomapaeomapa
emsi.
# include <stdio.h>
# include <stdlib.h>
char** mapa;
int linhas;
int colunas;
Nosso mapa.txttambémteráumformatodiferente.Aprimeiralinha
terádoisinteiros,indicandootamanhodomapaqueviráaseguir.Nomapa
atual,aprimeiralinhaseria 5 10:
5 10
|--------|
|...|..-.|
173

## Página 185

16.2. Alocaçãodinâmicadememória CasadoCódigo
|..-|.@..|
|......-.|
|--------|
Lerissoéfácil,dadoquesabemosusarbemafun ção fscanf().Usa-
remosessesnúmerosparaalocarotamanhodomapademaneiradinâmica,
queseráfeitonafun ção alocamapa():
void lemapa() {
FILE* f;
f = fopen("mapa.txt", "r");
if(f == 0) {
printf("Erro na leitura do mapa");
exit(1);
}
fscanf(f, "%d %d" , &linhas, &colunas);
alocamapa();
for(int i = 0; i < linhas; i++) {
fscanf(f, "%s", mapa[i]);
}
fclose(f);
}
Afun ção alocamapa()contémumcódigobastantesimilaraoqueusa-
mosparaentenderalocaç ãodinâmica. Adiferen çaéqueagoratemospon-
teirospara char.Apesardesabermosque charéarmazenadosempreem
1bytes,vamosusar sizeof()paranuncatermosproblema.Lembre-sede
queprecisamosadicionarmais1byte,paraguardaro enterqueésalvopelo
fscanf():
void alocamapa() {
mapa = malloc(sizeof(char*) * linhas);
for(int i = 0; i < linhas; i++) {
mapa[i] = malloc(sizeof(char) * colunas + 1);
}
}
174

## Página 186

CasadoCódigo Capítulo16. Matrizes
Nossa mainporenquantoapenasleráomapaeoimprimirá,paratermos
acertezadequetudoestáfuncionandocomogostaríamos:
int main() {
lemapa();
for(int i = 0; i < linhas; i++) {
printf("%s\n", mapa[i]);
}
}
Paratambémnãotermosproblemascomordemdadeclaraç ãodasfun-
ções,vamosdesdejácolocartodasasassinaturasdentrodo fogefoge.h,
queéimportadonocome çodonossocódigo-fonte:
// fogefoge.h
void alocamapa ();
void lemapa();
Pronto. Nossojogoagoraécapazdelermapasdequalquertamanho.
Porém,aindatemosumproblema. Vocêselembraque,nocapítulo 12,dis-
cutimosquetodorecursoabertodeveserfechado?Ouseja,seabrimosum
arquivo,precisamosfechá-lo.
Omesmoacontececommemóriaqueéalocadadinamicamente. Sem-
prequeusamos malloc(),osistemaoperacionalnosreservaumpedaçoda
memóriaenãopermitequenenhumoutroprogramaencostenele. Noen-
tanto,nossoprogramaéoresponsáveltambémporliberaressamemóriade
voltaaoSO.Fazemosissopormeiodafun ção free().Ouseja,paracada
malloc(),precisamosdeum free()aofinal.
Vejaafun ção liberamapa(),quenavegapelamatriz,liberandocada
umdosarraysalocadosdinamicamente. Aofinal,liberatambémamatriz
comoumtodo:
void liberamapa() {
for(int i = 0; i < linhas; i++) {
free(mapa[i]);
}
175

## Página 187

16.3. Resumindo CasadoCódigo
free(mapa);
}
Agora,bastaainvocarmosaofinaldonossoprograma,quandotemosa
certezadequeomapanãoserámaisutilizado:
int main() {
lemapa();
for(int i = 0; i < linhas; i++) {
printf("%s\n", mapa[i]);
}
liberamapa();
}
Nestemomento,aorodarmosoprograma,temosomapacomosaída:
|--------|
|...|..-.|
|..-|.@..|
|......-.|
|--------|
Está perdido?
O código até o momento está em
http://pastebin.com/HyxpNDPh
16.3 Resumindo
Nestecapítulo,aprendemos:
• Adeclararemanipularmatrizes;
• Oquesãoponteirosdeponteiros;
176

## Página 188

CasadoCódigo Capítulo16. Matrizes
• Quematrizessão,nofim,ponteirosdeponteiros;
• Adeclararmemóriadinamicamente,usandomalloc();
• Queainstrução sizeof()nosdevolveotamanhoembytesdeum
tipoespecíficonaquelaplataforma;
• Quedevemosliberaramemóriaalocadadinamicamenteaofim,com
free().
177

## Página 190

Capítulo17
Structs
Nossopróximopassoéfazeroheróiandar. Comotodojogo,usaremosa
combinaçãodeteclas A, S, D, W.Aideiaseráaseguinte: exibiremoso
mapa,leremosumaentradadoteclado,faremosasatualizaçõesnecessárias
nomapaerepetiremostudodenovo,atéqueojogadorganheouperca.
Vamoscome çarcomnossoloopprincipal,queseráparecidocomodo
nossojogodeforca. Usaremosafun ção scanf(),dojeitocomquevocê
jáestáacostumado. Lembre-sedoespaçoembrancoparaqueo enterseja
ignorado:
int main() {
lemapa();
do {

## Página 191

CasadoCódigo
imprimemapa();
char comando;
scanf(" %c", &comando);
move(comando);
} while (!acabou());
liberamapa();
}
Afun ção acabou(),comooseupróprionomediz,nosinformaráse
ojogoacabouounão. Porenquanto,vamosfazerumafun ção“falsa”,que
semprenosretorna 0.Ouseja,ojogonuncaacaba:
int acabou() {
return 0;
}
Afun ção imprimemapa()étambémbastantesimples.Elaapenasim-
primeomapa,dojeitoqueeleestánamatriz:
void imprimemapa() {
for(int i = 0; i < linhas; i++) {
printf("%s\n", mapa[i]);
}
}
Comocomandoemmãos,podemosmoveroheróiparaadire çãoque
ojogadorpediu. Oprimeiropassodoalgoritmodeveserlocalizaroherói.
Paraisso,nãotemoscomofugirdevarrertodaamatriz,usandodoisloops
encadeados:
void move(char direcao) {
int x;
int y;
for(int i = 0; i < linhas; i++) {
for(int j = 0; j < colunas; j++) {
180

## Página 192

CasadoCódigo Capítulo17. Structs
if(mapa[i][j] == '@') {
x = i;
y = j;
break;
}
}
}
}
Emseguida,modificaremosomapadeacordocomadire çãoescolhida:
Avaiparaaesquerda, Dparaadireita, Sparabaixoe Wparacima. Seo
jogadorandouparaesquerda,devemosdeslocaroheróiparalá,ouseja,para
a linha, coluna-1.Seeleandouparadireita,oheróivaipara linha,
coluna+1;separacima,vaipara linha-1, coluna;eseparabaixo,para
linha+1, coluna.Aofinal,devemoscolocarcomovazioaposiç ãoqueo
heróiestavaantes.Resolvemosissocomum switch:
void move(char direcao) {
// os fors aqui...
switch(direcao) {
case 'a':
mapa[x][y-1] = '@';
break;
case 'w':
mapa[x-1][y] = '@';
break;
case 's':
mapa[x+1][y] = '@';
break;
case 'd':
mapa[x][y+1] = '@';
break;
}
mapa[x][y] = '.';
}
181

## Página 193

17.1. Definindoumastruct CasadoCódigo
Sevocêrodarojogo,veráqueelejácome çaaseparecercomoqueque-
remos.Conseguimosmovimentarnossopersonagemparatodasasdire ções.
Masaindaestamoslongedeterminá-lo:sedigitarmosumaletrainválida,o
heróidesaparece.Eletambématravessaparedes.Temosmuitoacorrigir.
Está perdido?
O código até o momento está em
http://pastebin.com/LSAFA6BV
17.1 Definindo uma struct
Repareque,semprequeusamoso mapa,utilizamostambémasvariáveis
linhase colunas.Afinal,sempreprecisamosdelasparanavegarnamatriz.
Comoessasvariáveissãoglobais,nãotemosproblemasparausá-las. Mase
seprecisássemospassá-lascomoparâmetrosparaalgumafun ção?Seriatra-
balhoso;teríamosmuitosparâmetros.
Pelaprimeiraveztemosumconjuntodevariáveisque não fazem sentido
separadas.Amatrizsófazsentidosetiverumalinhaecolunajunto.Precisa-
mosagrupá-las,egarantirqueelassempreserão“transportadas”juntas.Para
tal,usaremosuma struct.
Estruturas(ou,emC, struct)sãoumamaneiraquetemosparaagrupar
variáveis.Ouseja,definiremosqueaestrutura mapacontémumamatriz(o
ponteirodeponteirode char),umavariávelparaguardaraquantidadede
linhas( int)eoutraparaguardaraquantidadedecolunas(também int).
Comessaestruturadefinida,podemosdeclararvariáveisqueaseguem.Dessa
forma,garantiremossemprequemapastêmumamatriz,eaquantidadede
linhasecolunas.
Vejaadeclaraç ãoda structaseguir,quecolocamosdentrodonosso
fogefoge.h.Dentrodele,declaramosamatrizeosdoisinteirosparaguar-
darassuasdimensões:
struct mapa {
char** matriz;
182

## Página 194

CasadoCódigo Capítulo17. Structs
int linhas;
int colunas;
};
Comodissemosanteriormente,comessastructemmãos,podemosfazer
usodelaedeclararvariáveisdessetipo.Mas,diferentedeuminteiroouum
charqueutilizamosatéentão,elatemvariáveisdentrodesi.Paraacessá-las,
usamosponto( .). Vejaotrechodecódigoaseguir,porexemplo,noqual
definimosummapaesetamososvalorespara linhase colunas.Repare
napalavra structnocome çodadeclaraç ão:
struct mapa facil;
char tabuleiro[10][20];
facil.matriz = &tabuleiro;
facil.linhas = 10;
facil.colunas = 20 ;
printf("O mapa tem tamanho %d x %d", facil.linhas,
facil.colunas);
Vamosfazerasdevidasalteraçõesnocódigo,usandoagoraa structque
definimos.Acome çarpelasvariáveisglobais,quesãosubstituídas:
struct mapa m;
Emtodolugarquefaziausode linhasou colunas,precisamostrocar
para m.linhase m.colunas.Emtodolugarquetínhamosamatriz mapa,
agoratorna-senecessáriousar m.matriz.
Umdetalheimportanteéperceberprecedênciadeoperadores.Porexem-
plo,dentrodafun ção lemapa(),temoso fscanf(),queagoraficoupare-
cidocomocódigoaseguir:
fscanf(f, "%d %d" , &m.linhas, &m.colunas);
Ainstrução &m.linhaséprocessadacorretamente.Passamosoende-
reçodavariável linhasqueestádentroda struct m.Umaoutrainterpre-
taçãodessainstruç ãoseriaqueo &éparaavariável m,ouseja,gostaríamos
183

## Página 195

17.1. Definindoumastruct CasadoCódigo
doendere çodememóriadaestrutura mcomoumtodo.Paraevitaressapos-
sívelambiguidade,écomumfazermosusodeparêntesesparadeixarclaraa
ordemdeprecedência:
fscanf(f, "%d %d", &(m.linhas), &(m.colunas));
Afun ção move(),comtodasasalterações,ficacomoaquesegue:
void move(char direcao) {
int x;
int y;
for(int i = 0; i < m.linhas; i++) {
for(int j = 0; j < m.colunas; j++) {
if(m.matriz[i][j] == '@') {
x = i;
y = j;
break;
}
}
}
switch(direcao) {
case 'a':
m.matriz[x][y-1] = '@';
break;
case 'w':
m.matriz[x -1][y] = '@';
break;
case 's':
m.matriz[x +1][y] = '@';
break;
case 'd':
m.matriz[x][y+1] = '@';
break;
}
m.matriz[x][y] = '.';
}
184

## Página 196

CasadoCódigo Capítulo17. Structs
Apesardasensaç ãodequeagoratemosmuitomaiscódigoescrito,usar
structsparaagrupardadosquedevemficarpertoéumaboaprática.Você
veráque,embreve,deixaremosdeusarvariáveisglobaisecome çaremosa
passaressas structsparaláeparacá.Comoelasagrupamtudooquepre-
cisamos,ficafácil:afun çãoreceberáapenasumponteiroparaaestrutura.
Repareque,semprequeprecisamosdeclararumavariáveldotipodaes-
trutura,énecessáriousarapalavra structantes comostruct mapa m.
Podemosmelhorarisso,fazendousodainstruç ão typedef.Elanospossi-
bilitadarumoutronomeaalgumtipojáexistente.
Porexemplo,vamosapelidar struct mapade MAPA,dentrodonosso
headerfile:
typedef struct mapa MAPA;
Graçasao typedef,agorapodemosdeclararvariáveisdotipo MAPAsem
apalavra struct.Veja:
MAPA m;
Está perdido?
O código feito até o momento está em
http://pastebin.com/YqyZdN6B
17.2 Ponteiros para structs
Vocêreparoutambémqueamaioriadasfun çõesqueescrevemosatéen-
tãotemapalavra“mapa”emalgumapartedonome? Aestrutura mapa,
bem como as funções alocamapa(), lemapa(), liberamapa() e
imprimemapa()fazemalgorelacionadoaomapa. Asfun çõesrestantes
acabou(), move()e main()apenasfazemusodaestruturae/oufun ções
domapa.
Podemospensaremisolartodasasfun çõesemumarquivoespecífico,
porexemplo, mapa.c.Masoqueganhamoscomisso?Reúsoemanutenibi-
lidade.Terumarquivodedicadosomentealidarcommapasnospossibilita
185

## Página 197

17.2. Ponteirosparastructs CasadoCódigo
utilizá-loemoutrasaplicações(mapaspodemserúteisemmuitosoutrosjo-
gos).Alémdisso,sabemosque,sealgodererradocommapas,muitoprova-
velmenteessecódigoestádentrodoarquivoespecífico.
Adiscussãoaquiésimilaràquefizemosquandochegamosàconclusãode
quefun çõeseramúteisparaisolarereutilizarcódigo.Aqui,amesmacoisa,
masemumnívelmaior.Teremosumarquivoqueagruparáumconjuntode
funçõesquetêmumarelaç ãoentresi.
Vamoscriaroarquivo mapa.h,comadefiniç ãoda structedasassi-
naturasdasfun çõesquelidamcommapas:
struct mapa {
char** matriz;
int linhas;
int colunas;
};
typedef struct mapa MAPA;
void alocamapa();
void lemapa();
void liberamapa();
void imprimemapa();
Jáoarquivo mapa.ccontémaimplementaçãodessasfun ções:
// mapa.c
# include <stdio.h>
# include <stdlib.h>
# include "mapa.h"
void lemapa() {
// código aqui
}
void alocamapa() {
// código aqui
}
186

## Página 198

CasadoCódigo Capítulo17. Structs
void liberamapa() {
// código aqui
}
void imprimemapa() {
// código aqui
}
Jáno fogefoge.c,incluímosoheaderdosmapas.Afinal,precisamos
dessasfun çõesdisponíveistambémnessearquivo.E,obviamente,retiramos
asfun çõesdemapa,queagoraestãoemseuarquivoparticular:
# include <stdio.h>
# include <stdlib.h>
# include "fogefoge.h"
# include "mapa.h"
Vamoscompilarnossoprograma. Alinhadecompilaç ãoagoraprecisa
contemplarambososarquivos. Paraisso,bastapassaralistadelesparao
gcc:
gcc fogefoge.c mapa.c -o fogefoge.out
Entretanto,ocompiladornessemomentonosdevolvemuitoserros. A
maioriadelesreclamandosobreanãoexistênciadavariável mnoarquivo
mapa.c.Efazsentido:avariável mestádeclaradaemoutroarquivo.
Variáveis, mesmoqueglobais, sãovisíveisapenasnoarquivoemque
foram declaradas. Ou seja, a variávelm é visível apenas dentro do
fogefoge.c.Efazsentidoelaserdeclaradalá,umavezqueelarepresenta
ummapadonossojogo. Nãoéalgogenéricoparacolocarmosdentrodo
mapa.c.
Aindaassim,queremossepararasfun çõesdemapadoresto. Portanto,
nãoteremosoutrasoluç ãoanãoserfazerasfun çõesquelidamcommapa
ereceberum mapacomoparâmetro. Vamospegar,porexemplo,afun ção
alocamapa()efazerisso:
void alocamapa (mapa m) {
m.matriz = malloc(sizeof(char*) * m.linhas);
187

## Página 199

17.2. Ponteirosparastructs CasadoCódigo
for(int i = 0; i < m.linhas; i++) {
m.matriz[i] = malloc(sizeof(char) * m.colunas + 1);
}
}
Ocódigoagoracompilará.Porém,daformacomoeleestáescrito,tere-
mosumproblema.Paraentendê-lo,criaremosumoutroprogramabastante
simples,queilustraráoqueprecisamos.
Ocódigoaseguirdeclaraumasimplesestrutura quadradocomdois
inteiros.Afun ção dobra()dobraosvaloresde xe y.Afun ção main()
imprimeosvaloresdosquadradosantesedepoisdeelesseremdobrados.
# include <stdio.h>
struct quadrado {
int x;
int y;
};
typedef struct quadrado QUADRADO;
void dobra(QUADRADO q) {
q.x = q.x * 2;
q.y = q.y * 2;
}
int main() {
QUADRADO q1;
q1.x = 20;
q1.y = 35;
printf("%d %d\n", q1.x, q1.y);
dobra(q1);
printf("%d %d\n", q1.x, q1.y);
}
Mas,aorodarmosoprograma,temosumasaídaquenãoesperamos:os
188

## Página 200

CasadoCódigo Capítulo17. Structs
resultadossãoiguais,antesedepoisdafun çãodedobra:
20 35
20 35
Arazãodoresultadoéfácildeserentendida.Evocê,naverdade,jásabe,
maspodeterseconfundidoporcausada struct. Vejaocódigoaseguir,
maissimplesainda,que,emvezdedobrarovalordentrodeuma struct,
dobraovalordeumavariável n:
void dobra(int n) {
n = n * 2;
}
int main() {
int n = 10;
printf("%d", n);
dobra(n);
printf("%d", n);
}
Asaídadoprogramaé 10 10.Vejaqueavariável ndométodo main
édiferentedavariável ndométodo dobra. Amáquina,nomomentoem
queinvocamosométodo dobra(),geraumacópiadavariável nqueestá
em maineapassaparaavariável ndafun ção dobra().Ouseja,passagem
porcópia.Oconteúdoé copiadoparaoparâmetro.Jávimosissoduranteo
capítulo11.Foiexatamenteporissoqueoptamosporusarponteiros,aliás.
Omesmoaconteceucoma struct.Aopassarmosavariável q1decla-
radana mainparaafun ção dobra,amáquinapassouapenasumacópiada
structoriginal.Asmudan ças,portanto,foramfeitasnacópia.Sequisermos
modificara structoriginal,damesmaformaquesequisermosmodificar
qualqueroutravariáveloriginal,precisamoslidarcomponteiros.
Afun ção alocamapa()devereceberumponteirodemapa,paraque
suasalteraçõessejamfeitassemprenaposiç ãodememóriadavariávelorigi-
nal.Ouseja,passagemporreferência:
void alocamapa (mapa* m) {
// ...
}
189

## Página 201

17.2. Ponteirosparastructs CasadoCódigo
Agora precisamos mudar o corpo da função. Afinal, antes fazíamos
m.linhasparaacessaroconteúdodavariável linhas,dentrode m.Mas
agora, méumponteiroparaummapa.Ouseja,precisamosprimeiroirpara
oconteúdodoponteiro,paradepoisusaravariável linhas. Emcódigo,
(*m).linhas.Vejaaprimeiralinhadessafun ção,modificada:
(*m).matriz = malloc(sizeof(char*) * (*m).linhas);
Dadoqueissoéumaoperaç ãobastantecomum(acessarprimeiroocon-
teúdodoponteiroedepoisumavariávelqualquerdentroda struct),a
linguagemCpossuiumaç úcarsintáticoquenosajudaaescreveramesma
coisademaneiramaissimples.Paraisso,usamosumaseta( ->).Asetafaza
mesmacoisaqueo“estrela-ponto”queusamosnocódigoanterior.Porexem-
plo, m->linhas.Vejaaprimeiralinha:
m->matriz = malloc(sizeof(char*) * m->linhas);
Vejaafun ção alocamapa()inteira:
void alocamapa(MAPA* m) {
m->matriz = malloc(sizeof(char*) * m->linhas);
for(int i = 0; i < m->linhas; i++) {
m->matriz[i] = malloc(sizeof(char) * m->colunas + 1);
}
}
Todasasoutrasfun çõesdoarquivo mapa.cdevemseguiramesmaabor-
dagem:receberumponteirodemapacomoparâmetroefazerusodasetapara
manipularessemapa.Asfun çõesagoratêmessaassinatura:
struct mapa {
char** matriz;
int linhas;
int colunas;
};
typedef struct mapa MAPA;
190

## Página 202

CasadoCódigo Capítulo17. Structs
void alocamapa(MAPA* m);
void lemapa(MAPA* m);
void liberamapa(MAPA* m);
void imprimemapa(MAPA* m);
A ordem importa?
Noheaderfile,vocêprecisacolocaro struct mapaantesdasdecla-
raçõesdasfun ções.Afinal,naassinaturadafun ção,usamosotipo MAPA,
eeleprecisaserdeclaradoantes.Vejaocódigoanteriorcomaten ção.
Nãopodemosesquecertambémdepassaroparâmetroparaafun ção
alocamapa(),invocadadentroda lemapa():
void lemapa(MAPA* m) {
// ...
fscanf(f, "%d %d" , & (m->linhas), &(m->colunas));
alocamapa(m);
// ...
}
Devoltaao fogefoge.c,precisamosagorapassaroendere çodememó-
riadavariável mparaasfun ções(usando &).Nessemomento,asalterações
concentram-senafun ção main:
int main() {
lemapa(&m);
do {
imprimemapa(&m);
char comando;
scanf(" %c", &comando);
191

## Página 203

17.3. Introduçãoàanálisedealgoritmos CasadoCódigo
move(comando);
} while (!acabou());
liberamapa(&m);
}
Nossojogoagoravoltouacompilareafuncionar.Reparequeocompor-
tamentoéomesmoquejátínhamosantesdecome çartodaessarefatoraç ão.
Adiferen çaéqueagoratemosnossocódigoaindamaisfácildeserlidoe
mantido.
Variáveis globais não são globais?
Variáveisdeclaradascomoglobaissãoglobaisparatodooprograma.
Mas,paraqueumarquivoenxergueumavariávelglobaldefinidaemou-
troarquivo,precisamosfazerusodapalavra extern.
Imagine,porexemplo,umavariável int n;definidanoarquivo
a.c. Paraausarmosnoarquivo b.c,precisaríamosredeclará-lacom
extern int n;. Agorasim,avariável n,global,évisívelporambos
arquivos.Reparequesóumarquivoarealmentedeclara,eosoutrosdei-
xamclaroqueelaé“externa”.
Está perdido?
O código até o momento está em
http://pastebin.com/PAz81Cda
17.3 Introdução à análise de algoritmos
Analiseagoraafun ção move().Analisarfun çõeséalgocomumemnosso
diaadiadetrabalho,umavezque,seumadelasnãofuncionarbemoulevar
muitotempoparaexecutar,podemosterproblemasemnossosoftware.
192

## Página 204

CasadoCódigo Capítulo17. Structs
Quandoanalisamosumafun ção,geralmentevemosotrabalhoqueela
tememrelaç ãoaosdadosdeentradaqueelarecebe.Nessecaso,considera-
moso mapacomoseudadodeentrada. Vejaque,semprequeinvocamos
afun ção,osdois forsgarantemquetodaamatrizépercorrida.Seoherói
estivernaúltimaposiçãoinferioràdireita,oalgoritmopassearápor todasas
posiçõesdela.
Ouseja,quantomaioromapa,maislerdaessafun çãoserá.Sefôssemos
definirissoemtermosmatemáticos,diríamosqueessafun çãotemacom-
plexidadede,nomáximo, linhas * colunas.Aquinãoentraremosem
detalhessobre análisedealgoritmos,queéumadisciplinafundamentalem
computação. Noentanto,percebadesdejáque,sevocêtemalgoritmosque
passeiamportodoumarrayoumatriz,quantomaioressearray,maistempo
essafun çãolevará.Seráqueconseguimos“economizar”nonúmerodevezes
quevarremosamatriz?
Reparequeessesloopsservemapenasparaencontraraposiç ãoatualdo
heróinomapa. Umasoluçãoparaissoétermosduasvariáveisglobais,que
guardariamoXeYdoherói. Dessaforma,nãoprecisaríamosbuscá-loo
tempotodo;játeríamosessainformaç ãosalva.
Vamosdeclararduasvariáveisglobaisparaisso:
int x;
int y;
Comessasduasvariáveis,podemoseliminaros forsencadeados,eafun-
ção move()ficaaindamenor.Nessemomento,repareque,alémdemenor,
elatambémémaisrápida:agoraelanãovarretodaamatrizparafazerseu
trabalho.Independentedotamanhodamatriz,elagastarásempreomesmo
tempoparaexecutar. Dizemosqueessafun çãolevatempoconstantepara
executar:
void move(char direcao) {
switch(direcao) {
case 'a':
m.matriz[x][y-1] = '@';
break;
193

## Página 205

17.3. Introduçãoàanálisedealgoritmos CasadoCódigo
case 'w':
m.matriz[x-1][y] = '@';
break;
case 's':
m.matriz[x+1][y] = '@';
break;
case 'd':
m.matriz[x][y+1] = '@';
break;
}
m.matriz[x][y] = '.';
}
Precisamosagoraencontrarolugaridealparaencontraraposiç ãodohe-
róipelaprimeira(eúnica)vez.Podemosfazerissologoapósainvocaç ãoda
função lemapa()nométodo main(). Masantes,vamosdeclararoutra
estrutura.PercebaquesemprequeháumX,hátambémumY.Porquenão
teraestrutura posicao?Comoumaposiç ãoérelacionadaaummapa,essa
estruturadeveserdeclaradanoheaderfiledemapa:
struct posicao {
int x;
int y;
};
typedef struct posicao POSICAO;
Vamosagoracriarafun çãoquelocalizaoheróieguardasuaposiç ãoem
umaestruturadessas. Reparequerecebemosoponteirodeambasasestru-
turas. Notetambémnassetas,usadasparaarmazenarosvaloresdentroda
posiçãodememóriaparaaqualosponteirosapontam:
void encontramapa(MAPA* m, POSICAO* p, char c) {
for(int i = 0; i < m->linhas; i++) {
for(int j = 0; j < m->colunas; j++) {
if(m->matriz[i][j] == c) {
p->x = i;
194

## Página 206

CasadoCódigo Capítulo17. Structs
p->y = j;
return;
}
}
}
}
Precisamosagoradeclararuma POSICAOqueguardaráaposiç ãodo
nossoherói,einvocarafun ção encontramapa()logoapóslermosomapa:
// variáveis globais
MAPA m;
POSICAO heroi;
// ...
int main() {
lemapa(&m);
encontramapa(&m, &heroi, '@');
// ...
}
Porfim,devemosfazercomqueafun ção move()façausoagorados X
e Yqueestãodentrodo heroi.Alémdisso,énecessáriotambématualizar
essavariávelsemprequeoheróiandar.Vamosfazê-lodentrodecadaop ção
do switch. Reparequefazemosasubstituiç ãodaposiç ãoatualdoherói
porvazionocome çodafun ção;afinal,jáquealteramososvaloresdavariável
heroi,apóso switchavariáveljáapontaparaanovaposiç ãodoherói.
void move(char direcao) {
m.matriz[heroi.x][heroi.y] = '.';
switch(direcao) {
case 'a':
195

## Página 207

17.3. Introduçãoàanálisedealgoritmos CasadoCódigo
m.matriz[heroi.x][heroi.y-1] = '@';
heroi.y--;
break;
case 'w':
m.matriz[heroi.x-1][heroi.y] = '@';
heroi.x--;
break;
case 's':
m.matriz[heroi.x+1][heroi.y] = '@';
heroi.x++;
break;
case 'd':
m.matriz[heroi.x][heroi.y+1] = '@';
heroi.y++;
break;
}
}
Nossojogocontinuafuncionando.Agoracomumalgoritmoaindamais
performático.Issoé,emaltonível,oquechamamosde análise de algoritmo.
Éolharparaeleeavaliarseudesempenho.Essedesempenhopodeseravali-
adodediferentesmaneiras:consumodememória,tempodeprocessamento,
espaçoemdiscoetc.
Geralmente,estamospreocupadoscomotempodeprocessamento.An-
tes,nossafun ção move()levavaumtempoproporcionalaotamanhoda
matriz.Ouseja,quantomaioramatriz,maistempoelelevava.Vimosainda
que,nopiorcaso,otempodoalgoritmopoderiaserproporcionalaonúmero
delinhasvezesonúmerodecolunas(linhasxcolunas),justamenteporque
eleeraobrigadoapassearportodaamatriz.Jánanovaversão,otempode
execuçãodafun çãonãovariadeacordocomotamanhodamatriz.Ouseja,
otempodelaésempreomesmo:éconstante.
Éissoquevocêaprenderánadisciplinadeanálisedealgoritmos.Obvia-
mente,porlávocêverátodooferramentalmatemáticoparaavaliareexpres-
sarotempodeexecuç ãodessesalgoritmos. Nãoéofocodestelivro,clara-
mente,maspercebadesdejáaimportânciadotema.
196

## Página 208

CasadoCódigo Capítulo17. Structs
Está perdido?
O código até o momento está em
http://pastebin.com/WDnyN8kV
17.4 Resumindo
Nestecapítulo,aprendemos:
• Porqueéimportantedeixarpertodadosqueserelacionam;
• Adefinirstructs;
• Adeclararvariáveisdotipodastruct;
• Ausarotypedefparadefinirumnomedetipoevinculá-loauma
struct;
• Asepararfunçõesemdiferentesarquivos;
• Acompilarmaisdeumarquivo.cjunto,paraformarumsóprograma;
• Apassarstructscomoreferência;
• Ausarooperador->paramanipularponteirosdestructs;
• Queanálisedealgoritmoséumaimportanteáreadacomputação.
197

## Página 210

Capítulo18
Programandocomoum
profissional
Estánahoradecontinuarmosnossojogo.Afinal,eleé,delonge,omaiscom-
plicadodostrês. Aprimeiracoisaafazeréacertaromovimentodonosso
herói. Nessemomento,seapertarmosalgumateclaquenãosejademovi-
mentação,oheróisomedomapa.Maisainda,elenãopodeandarporonde
quiser:eledevepararnasparedeseextremosdomapa.
Vamoscome çarignorandoqualquercomandoquenãosejadeandar.
Nessemomentodocódigo, podemosfazerissodentrodaprópriafun ção
move(). Umsimples ifresolve:sealetranãofor a, s, d, w,entãosai
dafun çãosemfazernada.
Apesardeatéentãotermosusadoapalavra returnparadevolvervalo-
resemumafun ção,podemosusá-laparaterminaraexecuç ãodeummétodo

## Página 211

CasadoCódigo
void.Nessescasos,apalavra returnnãovemacompanhadadenada.Re-
parequeesse ifécompridoeinvertido.Ouseja,sealetranãofornem a,
nem w,nem s,nem d,entãosaidafun ção:
void move(char direcao) {
if(
direcao != 'a' &&
direcao != 'w' &&
direcao != 's' &&
direcao != 'd'
) return;
// ...
}
Apróximavalidaçãoétratarocasodaparedeedosextremos.Nossoherói
sópodeandarseacasanaposiç ãoescolhidaéum .(ponto) ouseja,vazio.
Claro,seelejáestivernaúltimacasaàdireita,elenãopodeirmaisparaa
direita;omesmoparaesquerda,cimaebaixo.+
Parafazeresse if,precisaremosmudarumpouconossaimplementaç ão.
Ocálculodapróximaposiç ãoéfeitadentrodo switch,ondecalculamos
aposiçãoejámodificamosamatriz,colocandooherói. Agoraprecisamos
validarantesdecolocá-lolá. Paraisso,criaremosduasvariáveisauxiliares
quearmazenarãoaposiç ãoemqueoheróidevesercolocado,sendonelas
quefaremosasvalidações.
void move(char direcao) {
if(
direcao != 'a' &&
direcao != 'w' &&
direcao != 's' &&
direcao != 'd'
) return;
int proximox = heroi.x;
int proximoy = heroi.y;
200

## Página 212

CasadoCódigo Capítulo18. Programandocomoumprofissional
switch(direcao) {
case 'a':
proximoy--;
break;
case 'w':
proximox--;
break;
case 's':
proximox++;
break;
case 'd':
proximoy++;
break;
}
}
Avalidaçãoéfácil. Sabemosque proximoxdevesermenordoquea
quantidadedelinhasdamatriz,eque proximoydevesermenordoquea
quantidadedecolunas.Vamosescreveraquio ifaocontrário,poisusaremos
amesmaestratégiacomocaracteredadire ção:se proximoxformaiorou
igualàquantidadedelinhas,entãosaímosdafun ção.Amesmacoisaparao
proximoy:
if(proximox >= m.linhas)
return;
if(proximoy >= m.colunas)
return;
Reparequenãoabrimoschavesno if.Podemosfazerisso.Nessescasos,
a única coisa dentro do iféapróximainstruç ão. Ouseja,oquefizemos
anteriormenteéomesmoquefazeremosnocódigoaseguir:
if(proximox >= m.linhas) {
return;
}
if(proximoy >= m.colunas) {
return;
}
201

## Página 213

CasadoCódigo
Adiferen çaéqueessaocupamaislinhas. Issoéumpoucodegostode
cadadesenvolvedor.Namaioriadasvezes,optamosporabrirchaves,umavez
queissofacilitaalegibilidade.Masnessecasovamosdeixardeusá-las;afinal,
os ifssãomuitoparecidosesequenciais.Afaltadaschavesnãoatrapalhaa
legibilidade.
Apróximaetapaégarantirqueanovaposiç ãoévazia.Sóassimelepoderá
irparalá.Bastaadicionarmaisum if,tambéminvertido,queverificasea
posiçãocontémum .(ponto):
if(m.matriz[proximox][proximoy] != '.' )
return;
Issoquerdizerque,senossocódigosobreviveuportodosesses ifs,então
oheróiestáprontoparairparaessaposiç ão.Precisamosagorafazeratroca:
colocaroheróinanovaposiç ão,marcarasuaantigaposiç ãocomovazia,e
acertarnossavariável heroicomasnovascoordenadas:
m.matriz[proximox][proximoy] = '@';
m.matriz[heroi.x][heroi.y] = '.';
heroi.x = proximox;
heroi.y = proximoy;
202

## Página 214

CasadoCódigo Capítulo18. Programandocomoumprofissional
E se fizéssemos sem os ifs invertidos?
Teríamosumaquantidadegrandede ifsaninhados.Vejaqueafun-
çãosódeveexecutarseatecladigitadaéumadire ção,se proximox
formenorqueaquantidadedelinhas,se proximoyformenorquea
quantidadedecolunasouseapróximaposiç ãoévazia.
Ouseja,teríamosmuitos ifsaninhados,eocódigoficariamaisou
menoscomoomostradonasequência.Vejaqueocódigorealqueim-
portaficarialáparaafrente,commuitasindentações,oquedificultaria
sualegibilidade.Porisso,écomumfazermosocontrário:seumacondi-
çãofalha,saímosdafun ção.
if(primeira regra está certa) {
if(segunda regra está certa) {
if(terceira regra está certa) {
// ufa, agora sim vou fazer o que eu quero
printf("Tudo é valido!");
}
}
}
Pronto.Nossoheróiagorasóandaporondeérealmenteválido.
Está perdido?
O código até o momento está em
http://pastebin.com/p8yTC1ca
18.1 Nov amente, responsabilidades
Repareque,apesardeoandardoheróifuncionarbemdaformaquequería-
mos,nossocódigonãoestáperfeito.Afun ção move()émuitograndeetem
responsabilidadesdemais.Quandodizemosresponsabilidades,estamosnos
203

## Página 215

18.1. Novamente,responsabilidades CasadoCódigo
referindoàquantidadederegrasdenegóciodiferentesqueestádentrodela.
Vejaqueelaéresponsávelporsaberseocaractereéumadire çãoválida,por
calcularapróximaposiç ãodoherói,porsaberseanovaposiç ãoestádentro
domapaeéválida,eporfazerasmanipulaçõesnamatriz.
Ésimplesmentemuitacoisaparaumaúnicafun ção.Aliás,temcódigoaí
quesótemrelaç ãocommapas,ejásabemosquetudoquedizrespeitoamapas
deveriaestarno mapa.c.Essetipodesituaç ãoébastantecomumnodiaadia.
Afinal,estávamosmuitopreocupadosemfazeraregradenegóciofuncionar;
acabamosnãopensandonaqualidadedocódigo. Éporissoquedevemos
semprerefletirsobreoestadoatualdocódigo,emelhorá-lo,senecessário.
Vamoscome çaraquebraressafun ção. Aprimeiracoisaquepodemos
fazerélevaresse ifqueverificasealetradigitadaéumadire çãoqueégrande
,paraumafun çãoprópria.Afun çãosechamará ehdirecao(char)enos
retornaráuminteiro0ou1. Notequeprecisamosinvertertodoo if,pois
agoraafun çãonosretornaráverdadeiroseocaractereéumadire ção:
int ehdirecao(char direcao) {
return
direcao == 'a' ||
direcao == 'w' ||
direcao == 's' ||
direcao == 'd';
}
Afun ção move()jácomeçaaficarmenoremaisfácildeserentendida.
Repareque,antes,odesenvolvedorprecisavalero ifeentendê-lo. Agora
não:onomedafun çãodeixabemclarooqueelafaz.Odesenvolvedornão
precisanemleraimplementaç ãosenãoquiser:
void move(char direcao) {
if(!ehdirecao(direcao))
return;
// ...
}
204

## Página 216

CasadoCódigo Capítulo18. Programandocomoumprofissional
Podemosdeixaro switchdentrodafun ção.Afinal,calcularaposiç ãoé
partede“mover”.Masosdoispróximosifspodemirparadentrodasfun-
çõesdemapa;elesnosdizemseumadeterminadaposiç ãodomapaéválida
ounão.Aqui,nossaestratégiaseráretornar0,casoalgumadasposiçõesseja
inválida;ou,nofim,retornar1,dizendoque xe yestãodentrodoslimites
domapa.Emcódigo:
int ehvalida(MAPA* m, int x, int y) {
if(x >= m->linhas)
return 0;
if(y >= m->colunas)
return 0;
return 1;
}
Opróximo ifnosdizseapróximaposiç ãodomapaévazia.Issotam-
bémpodeirparadentrodomapa.Umasimplesfun çãoquenosdevolveum
booleanodeixaránossocódigomuitomaisclaro.Comoelamanipulamapa,
logo,estádentrodo mapa.c.Reparequeinvertemosacondiç ãodo ifpara
queelanosdigaseaquelaposiç ãoéounãovazia:
int ehvazia(MAPA* m, int x, int y) {
return m->matriz[x][y] == '.';
}
Os ifs,então,devemsersubstituídosporinvocaçõesaessasfun ções.
Vejaque,apesardetermosdiminuídopoucoaquantidadedecondicionais,
essecódigoémuitomaisfácildeserentendido.Afinal,apalavra ehvalida
deixamaisclarooqueacontecedoqueaquele ifgrande. Precisamosler
menos,oqueébom:
if(!ehvalida(&m, proximox, proximoy))
return;
if(!ehvazia(&m, proximox, proximoy))
return;
205

## Página 217

18.1. Novamente,responsabilidades CasadoCódigo
Vamosagoracolocaraspróximasduaslinhas,quesãoresponsáveispor
moveroqueestáemumaposiç ão,paraanovaposiç ão.Essatambéméuma
funçãoquedeveestarnomapaequeprovavelmenteseráutilizadamaisà
frente,poisteremosfantasmasnojogo,quetambémandarãoparaláepara
cá.
Afun ção andanomapa()receberá5argumentos:umponteirodemapa,
XeYdeorigem,eXeYdedestino.Elaébemsimples.Primeiro,elaarma-
zenaopersonagem(ouqualquercoisa)queestavanaposiç ãoantiga,paraem
seguida,fazeratroca:colocaopersonagemnaposiç ãodedestino,etrocapor
vazioaposiç ãoantiga:
void andanomapa(MAPA* m, int xorigem, int yorigem,
int xdestino, int ydestino) {
char personagem = m-> matriz[xorigem][yorigem];
m->matriz[xdestino][ydestino] = personagem;
m->matriz[xorigem][yorigem] = '.';
}
Ocódigotambémficamaissimplesno move(),jáque,agora,bastain-
vocaranossanovafun çãoquefazandarumpersonagemnomapa,etrocar
osvaloresdaposiç ãodonosso heroi:
andanomapa( &m, heroi.x, heroi.y, proximox, proximoy);
heroi.x = proximox;
heroi.y = proximoy;
Pronto. Afunção move()agoraémuitomaiscoesa. Ouseja,elafaz
muitomenostarefasedelegaparaoutrasfun ções.Temosagorafun çõesme-
noresemaisfáceisdeseremlidas,mantidasereutilizadas.Issoéprogramar.
Está perdido?
O código até o momento está em
http://pastebin.com/eCuugsgD
206

## Página 218

CasadoCódigo Capítulo18. Programandocomoumprofissional
18.2 Nov amente, constantes
Desdeoprimeirojogo,discutimososproblemasdetermosnúmerosmágicos
espalhadospelaaplicaç ão.Nomomento,nãotemosnúmerosmágicos,mas
sim“charsmágicos”. Vejaquetemosemnossocódigoasletras‘a’,‘d’,
‘s’,‘w’,quesignificamaspossíveisdireções,oumesmo ‘@’,‘.’e ‘|’,
queindicamospossíveispersonagensnomapa.
Vamoscriarconstantesparaisso. Vocêjáconheceasvantagens: maior
legibilidade,jáqueumaconstantetemumnome;efacilidadenamanuten ção,
umavezquebastaalterarovalordaconstanteparaaalteraç ãopropagar.
Asconstantesquedizemrespeitoaosmapasvãoparao mapa.h:
# define HEROI '@'
# define VAZIO '.'
# define PAREDE_VERTICAL '|'
# define PAREDE_HORIZONTAL '-'
Jáasconstantesquedizemrespeitoaojogovãoparao fogefoge.h:
# define CIMA 'w'
# define BAIXO 's'
# define DIREITA 'd'
# define ESQUERDA 'a'
Agora,bastafazermosusodelasemvezdetermosessescaracteresfixos.
Afun ção ehdirecao(),porexemplo,ficaaindamaislegível.Tambémusa-
remosessasconstantesdentrodo switch,nafun ção move().Repareque,
sedecidirmosmudarasteclasdojogo,bastaráalterarmosasconstantes.
int ehdirecao( char direcao) {
return
direcao == ESQUERDA ||
direcao == CIMA ||
direcao == BAIXO ||
direcao == DIREITA;
}
Generalizeoquefizemosnestase ção.Percebaque,nofundo,todavezque
falamosdeboaspráticasdecódigo,fazemosamesmacoisa:isolartrechosde
207

## Página 219

18.3. Usandoestruturasauxiliares CasadoCódigo
códigoparaquepossamosreutilizá-loemdiversospontosdaaplicaç ão,de
formaquefiquefácilsaberoqueelefazapenaslendooseunome.
Está perdido?
O código até o momento está em
http://pastebin.com/BjScydHn
18.3 Usando estruturas auxiliares
Opróximopassoéfazerosfantasmasandarempelomapa.Entretanto,ainda
nãodefinimoscomorepresentaremosumfantasmanomapa. Assimcomo
nosoutroscasos,escolheremosumacaractereparatal: F.
Vamoscolocaralgunsfantasmasnomapa,paracome çarmosnossostes-
tes:
5 10
|--------|
|.F.|....|
|..-|.@..|
|..F.....|
|--------|
Agoraprecisamosmovimentá-losnomapa.Oalgoritmopodeseroquão
complicadoquisermos: elespoderiamteralgumtipodeinteligênciaartifi-
cial,porexemplo. Mascome çaremoscomalgosimples,fazendotodoseles
andarem,porenquanto,somenteparaadireita.
Paratal,varreremosamatrizembuscadosfantasmas.Assimqueosen-
contrarmos,faremosandarumaposiç ãoàdireitacadaumdeles. Afun ção
fantasmas()seráresponsávelporisso.Aoencontrarmosumfantasma,ve-
rificaremosseapróximaposiç ãoàdireitaéválida.Sesim,entãoofantasma
andaráparaadireita:
void fantasmas() {
for(int i = 0; i < m.linhas; i++) {
for(int j = 0; j < m.colunas; j++) {
208

## Página 220

CasadoCódigo Capítulo18. Programandocomoumprofissional
if(m.matriz[i][j] == FANTASMA) {
if(ehvalida(&m, i, j+1)) {
andanomapa(&m, i, j, i, j+1);
}
}
}
}
}
Invocaremosafun ção fantasmas()logoapósafun ção move(),den-
trodonossoloopprincipaldojogo:
do {
imprimemapa(&m);
char comando;
scanf(" %c", &comando);
move(comando);
fantasmas();
} while (!acabou());
Serodarmosnossoprogramadojeitoqueestá,teremosumasurpresa:o
fantasmaandará,nãosóuma,mastodasascasasqueelepuderparaadireita.
Entenderporqueissoaconteceuéimportante,poisnosdaráumentendi-
mentoaindamaiorsobrealgoritmoselógicadeprogramaç ão.
Veja,porexemplo,ofantasmaqueestáem (3,3)domapa. Nossoal-
goritmooencontraráquando iforiguala3,e jfortambémiguala3. A
próximaposição, (3,4)évazia,eportantomovemosofantasma.Atéentão,
tudofuncionandodeacordo.
Entretanto,quandonossoloopiterar ouseja, iforiguala3,e jiguala
4,encontraremosomesmofantasmanovamente.Aposiç ãoàdireitaestará
vazia,eofantasmaserámovidoparalá. Oloopiteraránovamente, jserá
iguala5,eomesmofantasmaestarálánovamente.Percebaqueempurramos
omesmofantasmaváriasvezesparaadireita.
209

## Página 221

18.3. Usandoestruturasauxiliares CasadoCódigo
Precisamosencontrarumamaneiradesabersejáempurramosaquele
fantasmaounão. Podemospensaremdiversosalgoritmosparaisso,mas
nossasoluçãoserácriarumacópiadomapa. Comumacópia,poderemos
iteraremuma,emovernaoutra.Assim,nãoencontraremosomesmofan-
tasmaduasvezes.
Vamoscriar,portanto,umafun çãoquecopiaummapa.Elareceberádois
mapas: odestinoeaorigem. Copiarummapanãoéumatarefasimples.
Precisamoscopiarosdoisinteiros, linhase colunas,alocaramatriz,e
copiarlinhaalinhadamatrizorigem.
Paracopiarumalinha,usaremosafun ção strcpy(). Onomejádiz
oqueelafaz:copiaumastringemoutra.Afun çãorecebedoisparâmetros,
“destino”e“origem”.Essafunçãonadamaisfazdoquevarreroarrayecopiar
oconteúdonaposiç ãooriginalna“destino”,epararquandoencontrarum
null(`).
Vejaafun ção copiamapa(),dentrodo mapa.c:
void copiamapa(MAPA* destino, MAPA* origem) {
destino->linhas = origem->linhas;
destino->colunas = origem->colunas;
alocamapa(destino);
for(int i = 0; i < origem->linhas; i++) {
strcpy(destino->matriz[i], origem->matriz[i]);
}
}
Aocome çar,afun ção fantasmas()agorafaráumacópiadomapa m
e,depois,varrerácadacaracteredomapa copia. Semprequeacharum
fantasma,sabemosqueeletambémexisteem m.Seforpossívelmovê-lo ou
seja, ehvalida()e ehvazia()retornaverdadeiropara (i, j+1)no
mapa m,fazemossomentenomapa m.
Emseguida,comoofantasmanãoexistiránapróximaposiç ãoàdireitada
copia,umavezqueessemapaestáintocado,nãoteremosmaisoproblema
deofantasmaaparecernovamentenapróximaiteraç ãodoloop.
Aofinal,liberamosomapa copia,poisfizemosusodealocaç ãodinâ-
micaparacriá-lo,eelenãoémaisnecessário.
Emcódigo:
210

## Página 222

CasadoCódigo Capítulo18. Programandocomoumprofissional
void fantasmas() {
MAPA copia;
copiamapa(&copia, &m);
for(int i = 0; i < copia.linhas; i ++) {
for(int j = 0; j < copia.colunas; j ++) {
if(copia.matriz[i][j] == FANTASMA) {
if(ehvalida(&m, i, j+1) && ehvazia(&m, i, j+1)) {
andanomapa(&m, i, j, i, j+1);
}
}
}
}
liberamapa(&copia);
}
Écomumfazermosusodeestruturasauxiliaresparanossosalgoritmos.
Nessecasoemparticular,criamosumacópiadomapaparaconseguirmoster
osvaloresoriginaismesmoapósmodificá-los.
Umagrandepartedavidadoprogramadorécriar estruturasdedados
quefacilitemamanipulaç ãodosdadosquetemos. Esseé,aliás,umoutro
assuntoparavocêestudarfuturamente.
Outrasfunçõesdemanipulaç ão
Usamosafun ção strcpy()paracopiarumarrayparaooutro. Essa
função,comojáexplicamos,serveparacopiarstrings.Mas,àsvezes,quere-
moscopiaroutroselementosquenãostrings.Porexemplo,podemosquerer
uma structinteira.
Imagineoseguintecódigo:
struct contato {
char nome[20];
char email[50 ];
};
211

## Página 223

18.3. Usandoestruturasauxiliares CasadoCódigo
typedef struct contato CONTATO;
int main() {
CONTATO mauricio;
strcpy(mauricio.nome, "Mauricio Aniche");
strcpy(mauricio.email, "mauricio.aniche@caelum.com.br" );
}
Sequiséssemoscopiara structinteiraemvezdecopiaratributopor
atributo,poderíamosfazerusodainstruç ão memcpy(). Comoonomejá
diz,elacopiaoqueestánamemória.Aassinaturadelaébemparecidacoma
da strcpy(),comadiferen çadeque,alémdepassarodestinoeaorigem,
precisamospassartambémaquantidadedebytesquequeremoscopiar.
No código a seguir, copiamos o contatomauricio para o contato
aniche.Reparequeusamos sizeof()paracalcularaquantidadedebytes
da struct:
CONTATO aniche;
memcpy(&aniche, &mauricio, sizeof(CONTATO));
Outra função bastante comum quando manipulamos a memória é a
memset(). Geralmenteausamosparainicializarstructsouarrayscomal-
gumvalorpadrão(costumaser“nulo”).Issoéespecialmenteútil,poismuitos
compiladoresdeCnãolimpamasregiõesdememóriaantesdeliberá-lapara
oprogramador.Entãoécomumtermos“lixo”.
Paranãotermosnuncaoproblemadeterdadossujos,podemossempre
limparnossasstructs,porexemplo:
CONTATO marcelo;
// 0 significa NULO
memset(&marcelo, 0, sizeof(CONTATO));
Está perdido?
O código feito até o momento está em
http://pastebin.com/fwpRCbiD
212

## Página 224

CasadoCódigo Capítulo18. Programandocomoumprofissional
Épossíveldeixaressecódigoaindamaislegível, criandoumafun ção
paraencapsularotestedo if. Vejaqueocondicionalretornaverdadeiro
se ehvalida()e ehvazia()retornamverdadeiros. Reparequeambas
recebeminclusiveosmesmosparâmetros. Podemoscriarumafun çãoque
invocaessasduasfun çõesecomumnomequeexpliquemelhoroqueesse
condicionalsignifica.
int podeandar(MAPA* m, int x, int y) {
return
ehvalida(m, x, y) &&
ehvazia(m, x, y);
}
// ...
if(podeandar(&m, i, j+1)) {
andanomapa(&m, i, j, i, j+1);
}
Dessaforma,ocondicionalficarámaisclaro,enossocódigoaindamais
fácildeserreutilizado.
18.4 Um pouco de inteligência artificial
Nossofantasmaaindanãoémuitointeligente:elesósabeandarparaadireita.
Oproblemaéque,quandoeleandaatéabordadomapa,eleficaparadolá
parasempre. Vamosdarumpoucomaisdeinteligênciaaele. Ofantasma,
agora,senãoconseguirandarparaadireita,tentaráandarparaalgumaoutra
direção.Achancedeterumadire çãoválidaégrande.
Oquequeremosfazeraquiédarumpoucode inteligênciaartificial,ou
seja,ensinaramáquinaatentartomaradecisãoquemaximizaráseuganho.
Emoutraspalavras,ofantasmaagoranãoficaráparado,eleandarásempre
quepossívelemalgumadire ção. Claroqueesseéoexemplomaissimples
possíveldeinteligênciaartificial.Essaéumaáreagigantedeestudoerequer
dedicação.Porém,vamosdevagar.
Faremosissodemaneiraaleatória.Escolheremos,demaneirarandômica,
umadas4dire çõesválidas. Seelaforválida,éparaláqueofantasmavai;
213

## Página 225

18.4. Umpoucodeinteligênciaartificial CasadoCódigo
senãofor,tentaremosnovamente. Paraqueoprogramanãoentreemum
loopinfinito,faremosissonomáximo10vezes.Sedepoisdadécimatentativa
aindanãotivermosencontradoumapossíveldire ção,essefantasmaficará
paradonessarodada.
Vamoscome çardefinindoumaestruturaauxiliarqueguardaráas4pos-
síveisdire ções. Vejaqueissonosajudaráanãofazer4diferentes ifs: if
sorteado é direita, tente ir pra lá,if sorteado é esquerda, tente ir para lá.Ese
andássemosemtodasasdire çõespossíveis,contandodiagonais? Teríamos
muitocódigo. Pensesemprenisso. Muitocódigorepetido,mesmoqueseja
umpoucodiferentesumdooutro,ésempreproblemático.Procurecriares-
truturasqueflexibilizemefacilitemseucódigo.
Começaremos por declarar uma matriz dentro da nova função
praondevaifantasma(),ejádiretamenteinicializá-lacomas4dire ções
possíveis: x, y+1(direita), x+1, y(baixo), x, y-1(esquerda)e x-1,
y(cima).
int praondefantasmavai(int xatual, int yatual,
int* xdestino, int* ydestino) {
int opcoes[4][ 2] = {
{ xatual , yatual+1 },
{ xatual+1 , yatual },
{ xatual , yatual-1 },
{ xatual-1 , yatual }
};
}
Emseguida,criamosnossoloopde,nomáximo,10iterações,dentrodo
qualsorteamosumnúmerode0a3(aquantidadedelinhasdamatriz)etes-
tamosessadire ção.Seelaforválida,devolvemosadire ção reparequeaqui
precisamosreceberponteiros,poisqueremosqueafun çãodevolvadoisnú-
meros,efazemosafun çãoretornarverdadeiro.Casocontrário,seas10tenta-
tivasfalharem,retornamosfalso.Nãopodemosesquecerdeincluir time.h
noarquivo:
int praondefantasmavai(int xatual, int yatual,
int* xdestino, int* ydestino) {
214

## Página 226

CasadoCódigo Capítulo18. Programandocomoumprofissional
int opcoes[4][2] = {
{ xatual , yatual+1 },
{ xatual+1 , yatual },
{ xatual , yatual-1 },
{ xatual-1 , yatual }
};
srand(time(0));
for(int i = 0; i < 10; i++) {
int posicao = rand() % 4;
if(podeandar(&m, opcoes[posicao][0],
opcoes[posicao][1])) {
*xdestino = opcoes[posicao][0];
*ydestino = opcoes[posicao][1];
return 1;
}
}
return 0;
}
Agora, basta mudarmos o algoritmo da função fantasmas().
Ao encontrarmos um fantasma no mapa, invocaremos a função
praondefantasmavai() para descobrir o caminho dele. Se a fun-
çãonosretornarverdadeiro, sabemosquepodemosmovê-loparaaquela
direção:
void fantasmas () {
MAPA copia;
copiamapa( &copia, &m);
for(int i = 0; i < copia.linhas; i ++) {
for(int j = 0; j < copia.colunas; j ++) {
if(copia.matriz[i][j] == FANTASMA) {
int xdestino;
215

## Página 227

18.5. Acoplamento,encapsulamentoeassinaturasdefun ções CasadoCódigo
int ydestino;
int encontrou = praondefantasmavai(i, j,
&xdestino,
&ydestino);
if(encontrou) {
andanomapa( &m, i, j, xdestino, ydestino);
}
}
}
}
liberamapa(&copia);
}
Pronto.Nossosfantasmasagoraandamdemaneiraaleatóriapelomapa
etêmumpoucodeinteligêncianahoradeandar. Éclaroquepoderíamos
melhoraraindamais,porexemplo,fazendoosfantasmassempreandaremna
direçãodoherói,oumesmotrabalharemequipe,tentandocercá-lo. Esseé
umbomdesafioparavocê.
Está perdido?
O código até o momento está em
http://pastebin.com/knjL0xYH
18.5 Acoplamento, encapsulamento e assinatu-
ras de funções
Oquefaltaagoraéfazermosafinalizaç ãodojogo. OFoge-fogeéumjogo
noqualnãohávitória.Elesóacabaquandooheróimorre.Emnossojogo,o
heróimorreráquandoofantasma“passarporcimadele”.
Descobririssoéfácil. Comosabemosqueosfantasmasandamdepois
dopersonagem,sealgumfantasmapassarporcimadoherói,então,aofinal
doturno,nãohaveráheróinomapa. Játemosumafun çãoquenosajudaa
216

## Página 228

CasadoCódigo Capítulo18. Programandocomoumprofissional
encontraralgumpersonagemnomapa,a encontramapa(). Noentanto,
precisaremosadaptá-laparanosavisarcasoopersonagemnãosejaencon-
trado.
Mudaremos,então,aassinaturadafun ção,fazendo-adevolveragoraum
inteiro,quetrataremoscomobooleano. Elanosdevolveráverdadeiro,caso
encontremosopersonagem,efalso,casocontrário:
int encontramapa(MAPA* m, POSICAO* p, char c) {
for(int i = 0; i < m->linhas; i++) {
for(int j = 0; j < m->colunas; j++) {
if(m->matriz[i][j] == c) {
p->x = i;
p->y = j;
return 1;
}
}
}
// não encontramos!
return 0;
}
Reparequenossocódigocontinuacompilando,mesmoapóstermosmu-
dadoafun ção.Issoporquefizemosamudan çamaissimplesquepodíamos
naassinaturadela:trocamosde voidpara int.
Masoqueaconteceriasetrocássemos,porexemplo,onomeoumesmo
osparâmetrosqueelarecebe?Nossocódigoparariadecompilar.Todolugar
quefazusodeladeixariadefuncionar,umavezqueafun çãomudou.
Nãoéfácilmudaraassinaturadeumafun ção. Percebaoacoplamento
entreafun çãoeosdiversoslugaresquefazemusodela.Pensarmuitobemna
suaassinaturaéimportantíssimo. Nossosprogramas,atéentão,sãopeque-
nos,masmudarpodesercomplicadoemprojetosmaiores.
Partedotrabalhodobomdesenvolveréjustamentepensarnos“contra-
tos”queasfunçõestêm.Porcontrato,queremosdizeronomedafun çãopois
épormeiodelequevocêsabeoqueafun çãofaz,osparâmetrosqueelare-
217

## Página 229

18.5. Acoplamento,encapsulamentoeassinaturasdefun ções CasadoCódigo
cebeeoqueeladevolve.Seocontratoestiverbemdefinido,vocêraramente
precisarámudaraassinatura.
Avantagemdeterpensadobemnocontratoéqueaimplementaç ãode-
poispodevariar.Vocêreparouque,emváriosmomentosdolivro,mudamos
oconteúdodafun ção?Éocasodafun ção fantasma().Alteramosocom-
portamentodoandardosfantasmasaolongodestecapítulo. Ouseja,mu-
damosnossoalgoritmoparaalgomelhor,massem“quebrar”oresto. Tudo
continuoucompilando.
QuandovocêestudarOrientaçãoaObjetos,daremosaissoonomede en-
capsulamento.Encapsularsignificaesconderosdetalhesdoalgoritmoden-
trodafun ção.Issoéfeitoparaquepossamosmudá-losdepois,semnospre-
ocuparmosemfazerorestodosistemaparar,disponibilizandoparaaqueles
quequeremfazerusodela,umbomcontratoque,porserbom,tenhabaixa
chancedemudan ça.
Comolá,nocome çodonossojogo,pensamosbemqueprecisaríamosde
umafun ção acabou(),agorabastapreenchê-lacomumalgoritmodever-
dadeparadecidirseojogoacabouounão. Oquefaremosédeclararuma
estrutura POSICAO“inútil”einvocarafunção encontramapa(),quepro-
curarápeloherói.Seelaretornar0,entãoafun ção acabou()retornaráo
opostodisso.Ouseja,senãoencontrarmosoherói, acabou()retorna1:
int acabou() {
POSICAO pos;
return !encontramapa(&m, &pos, HEROI);
}
Sejogarmosagora,veremosqueestamosquaselá,masaindanãoestá
certo.Osfantasmasnãoconseguempassarporcimadoherói.Alémdisso,o
heróinãoconseguecomerfantasmas.Precisamosmelhorarnossoalgoritmo.
Oproblemaestánafun ção podeandar().Reparequeoalgoritmoláera
bemsimplista.Elepermitiaopersonagemandarseacasaàdireitaestivesse
vaziaoufossevazia:
int podeandar(MAPA* m, int x, int y) {
return
ehvalida(m, x, y) &&
218

## Página 230

CasadoCódigo Capítulo18. Programandocomoumprofissional
ehvazia(m, x, y);
}
Essafun çãoprecisasermaisinteligente.Podemosandarquando:
I) Apróximaposiçãoestiverdentrodoslimitesdomapa(éexatamenteo
queafun ção ehvalida()faz).
II) Apróximaposiçãonãoforumaparede(precisamoscriaressafun ção).
III) Apróximaposiçãonãoforumpersonagemidênticoaoqueestáan-
dando(esseéocasoparticularparaqueumfantasmanãopassepor
cimadeoutro).
Vamos, então, criar a função ehparede() e deletar a função
ehvazia(),poisnãoprecisaremosmaisdela. Acostume-setambémcom
isso: sevocênãousamaisafun ção,apague-a. Códigoquenãoéusadosó
serveparacomplicaravidadoprogramador.
int ehparede(MAPA* m, int x, int y) {
return
m->matriz[x][y] == PAREDE_VERTICAL ||
m->matriz[x][y] == PAREDE_HORIZONTAL;
}
Agoravamoscriarumafun çãoquecomparaopersonagemqueestána
posiçãocomoquefoipassadoporparâmetro.Apesardeessafun çãoterape-
nasumalinha,émuitomelhorterumafun çãodessadoqueterquelero if
eentenderoqueestáacontecendo. Lembre-sedequeonomedafun çãoé
importante,enosajudaalermenos.
int ehpersonagem(MAPA* m, char personagem, int x, int y) {
return
m->matriz[x][y] == personagem;
}
Porfim,vamosmudarafun ção podeandar().Dessavez,nãoteremos
jeito:precisaremosmudaraassinaturadelaparareceberopersonagemque
219

## Página 231

18.5. Acoplamento,encapsulamentoeassinaturasdefun ções CasadoCódigo
estáandando.Infelizmente,precisaremosprocurarportodososlugaresque
ainvocamepassaronovoparâmetro.Paciência,nãopensamosnissoantes.
Reparequeconseguimoslerseucódigodomesmojeitoquelemosalista-
gemanterior: pode andar se é válida E se não é parede E se não é personagem.
int podeandar(MAPA* m, char personagem, int x, int y) {
return
ehvalida(m, x, y) &&
!ehparede(m, x, y) &&
!ehpersonagem(m, personagem, x, y);
}
Comomudamosaassinaturadafun ção,vamosmudartambémnoslu-
garesqueainvocam.Porsorte,temosapenasdoislugares:dentrodafun ção
move()edentrodafun ção praondefantasmavai().Bastaapenaspas-
sarmosaconstantedorespectivopersonagem:
int praondefantasmavai(int xatual, int yatual,
int* xdestino, int* ydestino) {
// ...
if(podeandar(&m, FANTASMA,
opcoes[posicao][0], opcoes[posicao][1])) {
// ...
}
// ...
}
void move(char direcao) {
// ...
if(!podeandar(&m, HEROI, proximox, proximoy))
return;
// ...
}
220

## Página 232

CasadoCódigo Capítulo18. Programandocomoumprofissional
Agorasim. Fantasmaspodempassarporcimadoherói,eoheróipode
passarporcimadosfantasmas.Masoqueacontecesenossoheróipassarpor
cimadetodososfantasmas? Ojogoperdeagraç a. Vamosterminarojogo
tambémnessecaso.Issoéfácil,afun ção acabou()serveexatamentepara
isso,eaideiaéanálogaàquejátemos:senãohouvermaisfantasmasnomapa,
ojogotambémacabou.
Noteaquicomocriamosduasvariáveis, perdeue ganhou,apenaspara
aumentaralegibilidadedocódigo.Essaéoutraestratégiaquevocêpodeusar
parafacilitaraleitura:criarvariáveisqueexplicamoretornodeumafun ção
(ouumaconta,ouqualquerquesejaoconteúdoqueelaarmazena):
int acabou() {
POSICAO pos;
int perdeu = !encontramapa(&m, &pos, HEROI);
int ganhou = !encontramapa(&m, &pos, FANTASMA);
return ganhou || perdeu;
}
Pronto.Osfantasmasagoraandamdemaneiraaleatóriaepodemmatar
oherói.Ojogoestáficandoquente.
Está perdido?
O código até o momento está em
http://pastebin.com/gYFjK07E
18.6 Resumindo
Nestecapítulo,aprendemos:
• Novamente,aextrairpequenasfunçõesquesãoreutilizáveis;
• Quepodemos(edevemos)criarestruturasauxiliaresparafacilitara
criaçãodosnossosalgoritmos;
221

## Página 233

18.6. Resumindo CasadoCódigo
• Quepodemosnãoabrirchavesnoifeque,nessecaso,aexecuç ãodo
condicionalseráapenasapróximainstruç ãoqueaparecer;
• Quepodemoscopiarstringsusandostrcpy().
• Quepodemoscopiaroulimparstructs,arraysouqualquerponteiro,
usando memcpy()e memset();
• Que precisamos pensar bem no contrato das nossas funções, pois
mudá-losédifícil;
• Que podemos usar variáveis apenas para facilitar a legibilidade da
nossafun ção.
222

## Página 234

Capítulo19
Recursividade
Apróximafuncionalidadedonossojogoédarapossibilidadedenossoherói
comerapíluladosuperpoder.Seelecapturaressapílula,apertandoatecla
B,elesoltaráumabombaquedestruirátodososfantasmasqueestiverema
até3casasdedistância,àdireita.
Imagineomapaaseguir,porexemplo,esuponhaque Wtambémsejafan-
tasma.Todososfantasmasanotadoscomo Wmorrerão,casooheróioptepor
soltarabombanaquelemomento.Percebaquetodoselesestãonomáximoa
3casasdedistância.
|--------|
|.....F..|
|.....-..|
|.@W.W...|
|.. ..FF.|
|.....F..|

## Página 235

CasadoCódigo
|..F..F..|
|--------|
Vamoscome çarpelalógicadecapturarapílula. Elaserárepresentada
pelaletra Pnomapa.Casoojogadormovaoheróiemumacasaqueatenha,
devemosguardarissodealgumaforma:avariávelglobal tempilulanos
diráquantaspílulasojogadortemparagastar. Vamostambéminicializá-la
com0,umavezqueojogadorcome çasemnenhumapílula:
MAPA m;
POSICAO heroi;
// nova variável global
int tempilula = 0;
Precisamostambémcriaraconstante PILULA,adicioná-laaoheaderfile
domapa,emudaromapa:
// mapa.h
# define PILULA 'P'
// mapa.txt
5 10
|--------|
|FFF|....|
|FF-|.@P.|
|..F.....|
|--------|
Agora,bastaigualarmosessavariávela1semprequeoheróiandarpor
cimadeumadessaspílulas.Paraisso,nafun ção move(),bastaadicionarmos
averificação:acasadestinotemumapílula?Sesim,coloqueverdadeironela:
void move(char direcao) {
// ...
if(!podeandar(&m, HEROI, proximox, proximoy))
return;
224

## Página 236

CasadoCódigo Capítulo19. Recursividade
if(ehpersonagem(&m, PILULA, proximox, proximoy)) {
tempilula = 1;
}
// ...
}
Vamosatéexibirparaojogadoraquantidadedepílulasqueeletemna-
quelemomento.Vamoscolocaressecódigodentrodométodo main(),em-
boranãosejaolocalideal masdepoisdiscutimossobreisso.
int main() {
// ...
do {
printf("Pílula: %s\n", (tempilula ? "SIM" : "NÃO"));
imprimemapa(&m);
// ...
}
// ...
}
Apróximaetapaéfazernossoprogramaentenderoutrasentradasque
nãoumadire ção.Ouseja,seateclapressionadaforumadire ção,ométodo
move()deveserinvocado.Porém,seateclaforum B,eledevefazerabomba
explodir.
Precisamosfazerotestedatecladigitadaagoranoloopprincipaldopro-
grama,enãomaisdentrodafun ção move(). Dessaforma,eleconseguirá
dizerqualfun çãodeveráserinvocada.Aconstante BOMBAdeveserdefinida
noheaderfile:
// fogefoge.h
# define BOMBA 'b'
// fogefoge.c
225

## Página 237

CasadoCódigo
do {
printf("Pílula: %s\n", (tempilula ? "SIM" : "NÃO"));
imprimemapa(&m);
char comando;
scanf(" %c", &comando);
if(ehdirecao(comando)) move(comando);
if(comando == BOMBA) explodepilula();
fantasmas();
} while (!acabou());
Vamosdeclararafun ção explodepilula()apenasparanossocódigo
compilarnomomento,masaindasemumaimplementaç ãoconcreta,poisela
seráoalvodadiscussãodapróximase ção:
void explodepilula() {
}
Por que a main não é o melhor lugar?
Lembre-sedoencapsulamentoedequevocêdevefazeroprograma-
dorleramenorquantidadedecódigopossível.
Idealmente,afun ção main()apenasinvocaecoordenaoprograma
comoumtodo.Todaequalquerregradenegóciodeveestarencapsulada
emumafun çãocomumbomcontrato.Ouseja,esse printf()maiso
imprimemapa()deveriamestarencapsuladosemumafun ção.
Está perdido?
O código até o momento está em
http://pastebin.com/L27AnPjN
226

## Página 238

CasadoCódigo Capítulo19. Recursividade
19.1 Entendendo recursão
Implementaradestruiçãodosfantasmasàdireitaérazoavelmentefácil.Basta
fazermosumloopcontado3vezes,everificarseaposiç ão x, y+i(onde xe
yvemdaposição heroi)éválidaenãoéumaparede.Casoissosejaverdade,
bastatrocarmosaquelaposiç ãoporvazio:
void explodepilula() {
for(int i = 1; i <= 3; i++) {
if(ehvalida(&m, heroi.x, heroi.y+i) &&
!ehparede( &m, heroi.x, heroi.y+i)) {
m.matriz[heroi.x][heroi.y+i] = VAZIO;
}
}
}
Podemosaindatratarocasodaparede.Setiverumaparedenocaminho,
oefeitodabombaparadepropagarparaasoutrascasas. Ouseja,aparede
éimuneàbomba. Paraisso,mudaremosumpoucoamaneiracomonosso
algoritmofoidesenhado.Assimqueencontrarmosumaparede,quebramos
oloop.
void explodepilula() {
for(int i = 1; i <= 3; i++) {
if(ehvalida(&m, heroi.x, heroi.y+i)) {
if(ehparede(&m, heroi.x, heroi.y+1)) break;
m.matriz[heroi.x][heroi.y+i] = VAZIO;
}
}
}
227

## Página 239

19.1. Entendendorecursão CasadoCódigo
Está perdido?
O código feito até o momento está em
http://pastebin.com/Fqq7DWGB
Ótimo. Temosnossoalgoritmofuncionandoparaumadire ção. Mas,
comosabemos,temosváriasmaneirasdiferentesdeimplementaromesmo
algoritmo.Vamostentaralgodiferenteagora.Sabemosqueaprincipalparte
dessafun çãoéjustamentealinhaemquecolocamos VAZIOnaposição:
m.matriz[x][y] = VAZIO;
Vamoscolocarsomenteissonanossafun ção,quereceberá xe ycomo
parâmetros:
void explodepilula(int x, int y) {
m.matriz[x][y] = VAZIO;
}
Sabemostambémquedepoisdemarcaraposiç ãocomo VAZIO,omesmo
deveacontecerparaaposiç ão y+1.Éoquefaremos: chamaremosafunção
dentrodelamesma,passando y+1dessavez.Sim,issoépossível,echama-
mosissode funçãorecursiva.Ouseja,elainvocaasimesma:
void explodepilula(int x, int y) {
m.matriz[x][y+1] = VAZIO;
explodepilula(x, y+1);
}
Comomudamosasuaassinatura,precisamosmudarsuainvocaç ãotam-
bém:
if(comando == BOMBA) explodepilula(heroi.x, heroi.y);
228

## Página 240

CasadoCódigo Capítulo19. Recursividade
Pare e pense no que está acontecendo. Invocamos a função
explodepilula() pela primeira vez dentro do métodomain. Lá,
passamos heroi.x e heroi.y como parâmetros. Suponha que eles
valham 1,1nessemomento.Afun çãocome çaelimpaoqueestánaposiç ão
1,2(repareo+1dentrodamatriz).Emseguida,elainvocaasimesma,com
osparâmetros x, y+1,ouseja, 1, 2.Vamosparaasegundaexecuç ãoda
função. Aqui,elalimpaoqueestánaposiç ão,eseautoinvocanovamente,
dessavez,comosvalores 1, 3.Eassimpordiante.
Vocêtalveztenhavistoumproblemanisso. Senãoconseguiuperceber,
rodeaaplicaç ãoeexplodaabomba.Vocêveráumerro:
Segmentation fault: 11
Vocêpercebeuqueafun çãonuncaparoudeinvocarasimesma?Elase
chamapara 1,1,depoispara 1,2,entãopara 1,3,erepeteissoatéoinfinito.
Ouseja,temosumachamadarecursivainfinita.Afun çãoficaseinvocando
atéquenãohajamaisespaçonamáquinaparaguardarapilhadeexecuç ão.
Eaí,temosotaldo segmentationfault.
Quandocriamosfun çõesrecursivas,precisamosdeixarclaroemquemo-
mentoelapararádechamarasimesma.Issodependedoproblemaquees-
tamosresolvendo.Aqui,sabemosqueprecisamosexecutarafun ção3vezes.
Logo,colocaremosum“contador”. Ouseja,umavariávelqtd(dequanti-
dade),quequandofor0significaqueafun çãodeveparardechamarasi
própria.Ecomofazemosessenúmeroserzero?Nainvocaç ãorecursiva,pas-
samos qtd-1.Emcódigo:
void explodepilula(int x, int y, int qtd) {
// se acabou o número de vezes,
// então acaba a função
if(qtd == 0) return;
m.matriz[x][y+1] = VAZIO;
// dessa vez, passamos qtd-1, pois
// já rodamos uma vez a função
explodepilula(x, y+1, qtd-1);
}
229

## Página 241

19.1. Entendendorecursão CasadoCódigo
Mudamostambémainvocaçãonométodo main:
// 3 é a quantidade de casas que temos que explodir
if(comando == BOMBA) explodepilula(heroi.x, heroi.y, 3);
Vamos agora simular a execução dessa fun ção. A fun ção
explodepilula() é invocada namain(). Vamos supor que os pa-
râmetrospassadosparaelasejam 1, 1, 3.Naprimeiraexecuç ão,afun ção
limpaaposição 1, 2eautoinvoca-senovamentecomosparâmetros 1, 2,
2. Aprimeiraexecuçãoé,portanto,suspensaparaqueasegundaaconte ça.
Nela,aposiç ão 1, 3élimpa,eelaautoinvoca-secomosvalores 1, 3, 1.
Asegundainvocaç ão,então,ésuspensaparaaterceiraexecuç ão.Acasa 1,
4élimpa,eafun çãoénovamenteinvocadacomosvalores 1, 4, 0.
Como qtdéigualazero,aquartaexecuç ãomorre.Comisso,aterceira
execuçãovoltaàativaeacaba,jáquenãohámaisnadanela.Asegundainvo-
caçãovoltaetambémacaba.Omesmoacontececomaprimeira,finalizando
aexecuçãodafun çãocomoumtodo.
Acabamosdeescrevernossaprimeirafun çãorecursiva.Umafun çãore-
cursivaéaquelaqueinvocaasimesmaaolongodesuaexecuç ão.Paraque
issofuncionecorretamente,elaprecisaemalgummomentoparardeinvocar-
se(chamamosissode pontodefuga).
230

## Página 242

CasadoCódigo Capítulo19. Recursividade
Fibonacci
Podemosescrevermuitasoutrasfun çõesdemaneirarecursiva.Afun-
çãomatemáticadeFibonacciéumbomexemplo.Elaéexpressapormeio
daseguintefórmula:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
Pelanaturezadafun ção,percebaqueelainvocaaelamesma(ouseja,
recursiva). FibonaccideumnúmeroqualqueréigualàsomadoFibo-
naccidonúmeroanteriormaisoFibonnacidonúmeroanterioraoante-
rior.
Podemosescreveraseguintefun çãorecursivaparacalculá-lo.Repare
quesempreprecisamosdeumpontodefugae,nessecaso,atemos.Afi-
nal,sabemosqueFibonaccidezeroé0,eFibonaccide1é1.
Emcódigo,teríamosalgocomo:
int fib(int n) {
if(n == 0) return 0;
if(n == 1) return 1;
return fib(n-1) + fib(n-2);
}
Notequeafun çãoinvocaasimesmapassandosempre-1e-2. Em
algummomento,essesparâmetrosserãoiguaisa0ou1,eaíafun ção
entraemseupontodefugaeparadeinvocarasimesma.
Umbomexercícioédesenharaárvoredeinvocaçõeseentenderbem
oqueacontecequandofazemos fib(5),porexemplo.
231

## Página 243

19.2. Complicandooalgoritmorecursivo CasadoCódigo
Está perdido?
O código até o momento está em
http://pastebin.com/gsEqr1rD
19.2 Complicando o algoritmo recursivo
Precisamosmelhoraressafun ção.Afinal,elaaindaignorapossíveisexce ções,
comoocasodeumadas3casasàdireitanãoseremválidasouserempare-
des,porexemplo.Essessãosomenteoutrospontosdefugadafun ção.Caso
algumadessasafirmaçõessejaverdade,terminamosasuaexecuç ão.Emcó-
digo:
void explodepilula(int x, int y, int qtd) {
if(qtd == 0) return;
if(!ehvalida(&m, x, y+1)) return;
if(ehparede(&m, x, y+1)) return;
m.matriz[x][y+1] = VAZIO;
explodepilula(x, y+1, qtd-1);
}
Agora,precisamosexpandiraideiaparaasquatropossíveisdire ções,e
nãosóparaadireita. Reparequeaúnicacoisaquemudadeumadire ção
paraaoutrasãoascontasquefazemoscom xe y.Paraadireita,somamos
0,1,jáparaaesquerda,somaríamos 0,-1.Paracima, -1, 0,eparabaixo,
1, 0.
Vamosreceberessesnúmeroscomoparâmetrosdafun ção.Dessaforma,
afun çãoficagenéricaosuficienteparaserviratodososcasos.Dessavez,fare-
mosusodevariáveisauxiliares novoxe novoy.Vamos,inclusive,renomear
essafun çãopara explodepilula2:
void explodepilula2(int x, int y, int somax, int somay, int qtd){
if(qtd == 0) return;
232

## Página 244

CasadoCódigo Capítulo19. Recursividade
int novox = x+somax;
int novoy = y+somay;
if(!ehvalida(&m, novox, novoy)) return;
if(ehparede(&m, novox, novoy)) return;
m.matriz[novox][novoy] = VAZIO;
explodepilula2(novox, novoy, somax, somay, qtd-1);
}
Renomeamos a fun ção justamente para criar a fun ção
explodepilula(), que fará as 4 invocações necessárias para cada
direção.Éessaafun çãoqueseráinvocadadentroda main():
void explodepilula() {
explodepilula2(heroi.x, heroi.y, 0, 1, 3);
explodepilula2(heroi.x, heroi.y, 0, -1, 3);
explodepilula2(heroi.x, heroi.y, 1, 0, 3);
explodepilula2(heroi.x, heroi.y, -1, 0, 3);
}
Funçõesrecursivastêmvantagens.Elasgeralmentesãomaissimplesefá-
ceisdeseremlidaseimplementadas.Mas,dependendodocaso,elaspodem
nãosertãoperformáticas. Afinal,semprequeinvocamosumafun çãoden-
trodaoutra,oprogramaéobrigadoamantertodasasvariáveisqueexistem
naprimeirafun çãoemalgumcantodamemória,atéqueasegundafun ção
invocadaacabeeaprimeiravolteaserexecutada.
Setivermos,porexemplo,1000fun çõesinvocadasnasequência,amá-
quinaéobrigadaaguardarasvariáveisdas999chamadasanteriores,que
aindanãoacabaram. Omesmonãoaconteceriasetivéssemosusadoalgum
tipodeloop,porexemplo.
Podemosprolongaradiscussãoaqui. Muitoscompiladoresmodernos
conseguemreescreverarecursãonomomentodacompilaç ãoetransformá-
laemumloopconvencional,queocupamenosespaçodapilhadaexecuç ão.
Masessenãoéofoco.Oobjetivodestecapítuloéfazervocêentenderoque
sãofun çõesrecursivasecomoescrevê-las.
233

## Página 245

19.3. Resumindo CasadoCódigo
Paraterminar,faltafazerafun çãofuncionarsomentesetemosbombase
retirarabombacasoausemos.Podemosfazerissofacilmentedentrodafun-
ção explodepilula().Bastacolocar 0dentrodavariável tempilula:
void explodepilula() {
// se não tem pílula, não pode fazer nada
if(!tempilula) return;
explodepilula2(heroi.x, heroi.y, 0, 1, 3);
explodepilula2(heroi.x, heroi.y, 0, -1, 3);
explodepilula2(heroi.x, heroi.y, 1, 0, 3);
explodepilula2(heroi.x, heroi.y, -1, 0, 3);
// tira a pílula que acabou de usar
tempilula = 0;
}
Está perdido?
O código até o momento está em
http://pastebin.com/H9PcJcHa
19.3 Resumindo
Nestecapítulo,aprendemos:
• Oquesãofunçõesrecursivas;
• Quefunçõesrecursivasprecisamdepontosdefuga,ouseja,pontos
ondeelasnãoinvocammaisasipróprias.
234

## Página 246

Capítulo20
Outrasdiretivasdecompilaç ão
Oúltimopassoagoraédeixarnossojogobonito,jáqueelenãoestánada
apresentável.Comojásabemosqueprecisamossepararasresponsabilidades
aomáximo,vamosmoverafun ção imprimemapa()paraumnovoarquivo,
o ui.c(UIvemde User Interface,ouinterfacedousuário).
Oprimeiropassoédefinirmoscomoimprimiremoscadapersonagemdo
mapa.SeabusarmosumpouconovamentedeASCIIArt,podemosdesenhar
umfantasmademaneiramuitomaiselegante.Masprecisaremosdemaisde
umalinhaparaisso.Vamosdeclararumavariávelqueguardaodesenhodo
nossofantasma,emváriaslinhas.Odesenhoterá4linhaspor6caracteres.
Repare,noentanto,quedeclaramos7posiçõesnasegundadimensãodama-
triz,justamenteparaguardaro `final:
char desenhofantasma[4][7] = {
{" .-. " },

## Página 247

CasadoCódigo
{"| OO| " },
{"| | " },
{"'^^^' " }
};
Aideiaéque,quandoencontrarmosum Fnomapa,imprimiremosesse
desenho.Quandoencontrarmosum @,imprimiremosoherói,eassimpor
diante.Vamoscriar,portanto,odesenhodosoutrospossíveiscaracteresdo
nossomapa:
char desenhoparede[4][7] = {
{"......" },
{"......" },
{"......" },
{"......" }
};
char desenhoheroi[4][7] = {
{" .--. " },
{"/ _.-'" },
{"\\ '-." },
{" '--' " }
};
char desenhopilula[4][7] = {
{" "},
{" .-. "},
{" '-' "},
{" "}
};
char desenhovazio[4][7] = {
{" "},
{" "},
{" "},
{" "}
};
Comissoemmãos,precisamosagoraimprimirosdesenhosnahoracerta.
236

## Página 248

CasadoCódigo Capítulo20. Outrasdiretivasdecompilação
Mas,diferentementedooriginal,ondefazíamosdoisloopsaninhados(um
paracadadimensãodamatriz),aquiprecisaremosserumpoucomaisinteli-
gentes.
Notequecadadesenhotem4linhas.ComoestamosusandoaAPIsim-
plesdeescrevernatela,nãoconseguimosescrever4linhasparadesenharo
primeirocaracterequeaparecenomapa,edepoisvoltarparaaprimeiralinha
novamente,paracome çaradesenharosegundo.
Precisamosleraprimeiralinhadomapaeimprimirasprimeiraslinhas
detodosospersonagensqueestãoali.Depois,todasassegundaslinhas,todas
asterceirase,porfim,todasasquartaslinhas.Só,então,poderemoscome çar
aimpressãodasegundalinhadomapa.
Paraisso,precisamosdemaisumloopcontadode1até4(ou0a3),que
imprimiráalinhacertadetodososdesenhos.Vejaocódigoaseguir.Temos
alinhaem i,acolunaem jeapartedodesenhoaserimpressaem parte:
void imprimemapa(MAPA* m) {
for(int i = 0; i < m->linhas; i++) {
for(int parte = 0; parte < 4; parte ++) {
for(int j = 0; j < m->colunas; j++) {
// é aqui que imprimiremos
}
}
}
Vamos criar uma função que apenas imprimirá a parte especificada
dodesenho. Aassinaturadessafun çãodeveser imprimeparte(char
desenho[4][7], int parte),poisprecisamosreceberamatrizde 4x7
eointeiroquenosdizaparte:
void imprimeparte(char desenho[4][7], int parte) {
printf("%s", desenho[parte]);
}
237

## Página 249

CasadoCódigo
Agora, basta fazermos a função imprimemapa() invocar a fun-
ção imprimeparte() de acordo com o caractere que estiver em
m->matriz[i][j] e o número da parte a ser impressa. Um simples
switchresolveoproblema.
Repare na sintaxe que usamos em PAREDE_VERTICAL e
PAREDE_HORIZONTAL. Como em ambos os casos queremos imprimir
odesenho desenhoparede,podemoscolocarum caseembaixodooutro
e,dessaforma,ambosterãoomesmocomportamento:
void imprimemapa(MAPA* m) {
for(int i = 0; i < m->linhas; i++) {
for(int parte = 0; parte < 4; parte++) {
for(int j = 0; j < m->colunas; j++) {
switch(m-> matriz[i][j]) {
case FANTASMA:
imprimeparte(desenhofantasma, parte);
break;
case HEROI:
imprimeparte(desenhoheroi, parte);
break;
case PILULA:
imprimeparte(desenhopilula, parte);
break;
case PAREDE_VERTICAL:
case PAREDE_HORIZONTAL:
imprimeparte(desenhoparede, parte);
break;
case VAZIO:
imprimeparte(desenhovazio, parte);
break;
}
}
printf("\n");
}
238

## Página 250

CasadoCódigo Capítulo20. Outrasdiretivasdecompilação
}
}
No ui.c,nãopodemosesquecerdeimportarosheaderfilesnecessários:
# include <stdio.h>
# include "mapa.h"
Comoalgoritmopronto,precisamosapenasacertarasarestas. Preci-
samosgarantirqueafun ção imprimemapa()nãoexistamaisnemem
mapa.cenemem mapa.h.Elaagoraestáem ui.h.Observequeeleprecisa
incluir mapa.h,umavezqueelefazusode MAPAporlá:
# include "mapa.h"
void imprimeparte(char desenho[4][7], int parte);
void imprimemapa(MAPA* m);
Precisamosincluir ui.hdentrode fogefoge.c;afinal,éelequeinvoca
(jáinvocava,aliás)afunção imprimemapa().
# include <stdio.h>
# include <stdlib.h>
# include "time.h"
# include "fogefoge.h"
# include "mapa.h"
// novo include
# include "ui.h"
Ocódigoestátodocerto.Porém,aotentarmoscompilarnossos3arquivos
juntos(sim,agorasão3!),recebemosdiversoserrosparecidoscomosque
seguem:
> gcc fogefoge.c mapa.c ui.c -o fogefoge.out
In file included from fogefoge.c:6:
In file included from ./ui.h:4:
./mapa.h:12:8: error: redefinition of 'mapa'
struct mapa {
239

## Página 251

20.1. IfdefseIfndefs CasadoCódigo
^
./mapa.h:12:8: note: previous definition is here
struct mapa {
^
Oerronosdizqueestamos redefinindo mapa.Ouseja,poralgummotivo
eleencontrouumanovadeclaraç ãoda struct mapaemnossocódigo.Mas,
setemoscertezadequeissonãoacontece,porqueocompiladorseperdeu?
20.1 Ifdefs eIfndefs
Oproblemaaconteceporque,quandofazemosum include,ocompiladorlite-
ralmenteincluiocódigodaquelearquivoali.Écomosefosseum copia e cola
feitodeformaautomáticapelocompilador.Ecomoagoratemosumamistura
deinclusões,jáqueo fogefoge.cincluitanto mapa.hquanto ui.h,eo
ui.htambéminclui mapa.h,acabamosporrepetiramesmadeclaraç ão.
Aprimeirasoluçãoparaissoéacharacombinaç ãodeinclusõesasefazer.
Porexemplo,sesabemosqueo ui.hinclui mapa.h,sóprecisamosincluir
oprimeiro,poisosegundojáseráincluídoporele. Oproblemaéqueessa
soluçãopodeficarbastantecomplicadaàmedidaquenossoprogramacresce
etorna-semaiscomplicado.
Precisamosdeumamaneiradedizeraocompiladorparanãoincluirum
arquivoseelejáfoiincluído.Ouparaignorarumasegundadeclaraç ão.
Similaràsdiretivas includee define,ocompiladordalinguagemC
nosdáoutros2interessantes:o ifdefeo ifndef.Comoopróprionome
diz,oqueelesfazemsão ifs. Massão ifsdiferentes:elesacontecemem
tempodecompilaç ão.Orestantedonome,o def,éporqueocondicionalé
feitoemcimadeum define.
Entenderissoparececomplicado,porém,emcódigo,émuitomaissim-
ples.Vejaocódigoaseguir.Temos3 printfs.Noentanto,osegundoestá
entreum ifdef.Reparequeacondiç ãoéseo #define IMPRIMEexiste.
Comoelenãoexiste,asaídadesseprogramaésimplesmente: antes do
imprimiue depois do imprimiu.
# include <stdio.h>
240

## Página 252

CasadoCódigo Capítulo20. Outrasdiretivasdecompilação
int main() {
printf("antes do imprimiu\n");
// esse trecho de código não será compilado,
// pois o compilador viu que a constante
// IMPRIME nunca foi definida
# ifdef IMPRIME
printf("imprimiu\n");
# endif
printf("depois do imprimiu");
}
Noentanto,sedefinirmosumaconstante IMPRIMEcomqualquervalor
(ouatémesmovazio),nomomentodacompilaç ão,ocompiladorperceberá
queaquelaconstanteexisteecompilaráoqueestádentrodo ifdef:
// definimos a constante e,
// mesmo que vazia, ela existe!
# define IMPRIME
int main() {
printf("antes do imprimiu\n");
// o compilador percebe que ela existe,
// então compilará o que está dentro do ifdef.
# ifdef IMPRIME
printf("imprimiu\n");
# endif
printf("depois do imprimiu");
}
Agrandecharadaaquiéperceberqueessetesteéfeitoemtempodecom-
pilação.E,seotestefalhar,ocompiladornemolharáparaoqueestiverdentro
do ifdef:elerealmenteignoraráenãocompilaráoqueestiverlá. Clara-
mente,o ifndeféidêntico:adiferençaéqueeleverificaseaconstantenão
241

## Página 253

20.1. IfdefseIfndefs CasadoCódigo
foidefinida.
Sabendodisso, asoluçãoeleganteparaoproblemadasredefiniçõese
includesportodoladoéusaressasdiretivasdecompilaç ãodentrodenos-
sos .h.Aprimeiracoisaquefaremosemcadaumdeleséperguntarseuma
constantequalquer porexemplo, _UI_H_ existe.Seelanãoexistir,signifi-
caráparanósqueaqueleheadernãofoiincluídopornenhumoutroarquivo.
Logo,dentrodo ifndef,colocaremostodooconteúdoquequeremos,como
declaraçãodefun çõese structs,edefiniremosaconstante _UI_H_.Apar-
tirdeagora,elaexiste.Issosignificaque,napróximavezqueincluirmosesse
header,aconstanteexistirá,o ifndefseráfalso,eocompiladornãopas-
saránovamentepelasmesmasdefiniçõesdefun çõese struct,evitandoo
problemadaredeclaração.
Emcódigo,o ui.hficaria:
# ifndef _UI_H_
# define _UI_H_
# include "mapa.h"
void imprimeparte(char desenho[4][7], int parte);
void imprimemapa(MAPA* m);
# endif
Omesmoaconteceriacomo mapa.h.Obviamente,daremosumnome
diferenteàconstantequeéusada:
# ifndef _MAPA_H_
# define _MAPA_H_
// todo o conteúdo aqui dentro
# endif
E fogefoge.h:
# ifndef _FOGEFOGE_H_
# define _FOGEFOGE_H_
242

## Página 254

CasadoCódigo Capítulo20. Outrasdiretivasdecompilação
// todo conteúdo aqui dentro
# endif
Percebaqueocompiladorépoderoso.Podemosatédizeraeleoquedeve
ounãosercompilado.Naprática,usamosmuitoparaevitaroproblemadare-
declaraçãodecoisasqueestãodentrodenossosheaderfiles.Assim,podemos
incluiromesmoarquivováriasvezes,semnospreocuparmoscomdetalhes.
Outrocenárioondediretivasdecompilaç ãosãomuitoutilizadaséocaso
dedesenvolvimentodeaplicativosparaarquiteturas,plataformasousistemas
operacionaisdiferentes.Todoocódigoqueescrevemosnestelivroé ANSI C,
ouseja,épadrão.Elepodesercompiladoemqualquersistemaoperacional
comoWindows,LinuxeMac,eocomportamentoseráomesmo.
Noentanto,temosmuitasbibliotecasespecíficasdecadasistemaoperaci-
onal.Porexemplo,bibliotecasgráficasquesórodamnoWindows,ououtras
quesórodamnoLinux.Nessescasos,muitosdesenvolvedoresoptamporfa-
zergrandepartedocódigoem ANSI Ce,nospequenospedaçosespecíficos
decadasistemaoperacional,usardiretivasdecompilaç ão,paraquetrechosde
códigosósejamcompiladosnoWindows,eoutrostrechossónoLinux.Tam-
bémnãoentraremosemmuitosdetalhesdessadiferen ça. Masacostume-se
comeles:vocêpodeencontrarumdessesdevezemquando.
Pronto. Nossojogofunciona,etemosagoraumainterfacemuitomais
amigávelparanossojogodeFoge-foge.
Código final
O código final do jogo está em
http://pastebin.com/U1M7VjFM
20.2 Resumindo
Nestecapítulo,aprendemos:
• Aentenderoproblemadaredefiniçãodefun çõesestructsqueacontece
quandonossoprogramacresceemnúmerodearquivos;
243

## Página 255

20.2. Resumindo CasadoCódigo
• Ausarasdiretivasdecompilação #ifdefe #ifndefpararesolver
essesproblemas.
244

## Página 256

Capítulo21
Exercícios
Agoraésuavezdepraticar!
21.1 JogoFoge-foge
1) Suportecomandostantoemletrasmaiúsculasquantominúsculas.
2) Façaosfantasmasandaremnadire çãodoherói.Tenteotimizarocaminho
delesparaqueelescheguemomaisrápidopossívelaoherói.
3) Hojenossoheróicomefantasmas.Faç aeleteressepodersósecomeruma
outrapílula.Assimqueelecomê-la,eleteráessepoderdecomerfantasmas
por20turnos.
4) Façaosfantasmasnãocomeremaspílulas.Elasdevemsercomoumapa-
redeparaeles.

## Página 257

21.2. Outrosdesafios CasadoCódigo
5) Transformeafunção explodepilula()emumafun çãonãorecursiva.
Useloopsparaisso.E,claro,deixeocódigomaisbonitopossível.
6) Melhoreafunção move().Épossívelfazercomqueo switchnãofique
repetindo m.matriz[][]váriasvezes.
21.2 Outros desafios
1) Desenheaárvoredeinvocaçãopara fib(5).Vocêpercebeualgoproble-
mático?
2) Façaafun çãode fib(5)nãoprecisarrecalcularosmesmosvaloresmais
deumavez.Paraisso,useumarrayparaguardarosvaloresjácalculados.
Essatécnicaéconhecidacomo memorização.
3) Escrevaumafunçãoquenosdigaseumafraseépalíndroma.Frasespalín-
dromassãoaquelasquepodemserlidasdetrásparafrente.Porexemplo,
“Socorram-me, subi no ônibus em Marrocos!
épalíndroma.
246

## Página 258

Capítulo22
Oquefazeragora?
Sevocêchegouatéaqui,parabéns!Acaminhadafoilonga,masagoravocêjá
sabeoqueprecisasobreprogramaç ãoeestáprontoparacome çaraenfrentar
desafiosmaiores.
Vocêaindatemmuitoaestudar,como:
•OrientaçãoaObjetos(OO)elinguagensorientadasaobjetos: Javae
C#dominamomercado.AprenderoqueéOO,polimorfismo,heran ça
eencapsulamentosãofundamentaisparaquevocêconsigalidarbem
comessaslinguagens.
•Desenvolvimentoparaweb: nãoénecessárioconvenceralguémde
quewebéfundamental.EntendermaisdeHTML,CSSeJavascript do
ladodocliente,eosframeworksparadesenvolvimento doladodo
servidor sãoimportantessevocêquerseguirnessaárea.

## Página 259

CasadoCódigo
•Desenvolvimentomobile: todomundotemcelular. AndroideiOS
estãocadavezmaispopulares.AprenderJavaeObjective-C/Swiftsão
importantes,sevocêquerdesenvolveraplicativosmobile.
•Testesautomatizadosdecódigo: aquitestamosnossosprogramasde
maneiramanual.Ouseja,oexecutávamos,interagíamoscomeleevía-
mosseelefuncionava.Issonãoénadaprofissionaleimpossíveldese
fazeremumsistemagrande.Vocêprecisaaprenderaescreverprogra-
masquetestamprogramas.
•Boaspráticasdecódigo: estudarOrientaçãoaObjetos,padrõesde
projetosearquiteturadesoftwareoajudarãoaescreversoftwarepronto
paraomundoreal,eprontosparaseremmantidoseevoluídospara
sempre.
Avidadodesenvolvedordesoftwareéaprendersempre.Vocênãopode
parardebuscarporfontesdeinformaç ão.Nós,brasileiros,temosasortede
terumacomunidadededesenvolvimentobastanteativa.Participedefóruns
eeventos.Lá,vocêfaráumótimo networking,conhecerápessoas,desenvol-
vedoresmaisexperientesquevocê,etrocaráexperiências.
Nãotenhamedodepesquisar.OGoogleé,comcerteza,umaferramenta
primordialdetrabalho.Tambémnãoseassustecomoserrosdoseucompi-
lador.Leia-oscomaten çãoevádevagar,atéencontraroproblema.
Ocaminhoélongo,mascomcertezavocêjádeuoprimeiropasso.Não
pareagora!Eboasortecomasuacaminhada!
248

## Página 260

Capítulo23
ApêndiceA:instalandoo
compilador
SevocêusaLinuxouMac, provavelmentejátemoGCCinstalado. No
Windows, omelhorafazerébaixaro Mingw/GCC,disponívelem http:
//sourceforge.net/projects/mingw. Instaleospacotes basee c++. Não
esqueçatambémdecolocarodiretóriono PATH.NoWindows,vocêfaz
isso em Sistema -> Configurações Avançadas do Sistema ->
Variáveis de Ambiente.
Paratestarsuainstalaç ão, oidealseriacompilaralgumpequenopro-
grama.Crieoarquivoaseguiresalvecomonome teste.c:
# include <stdio.h>
int main() {

## Página 261

CasadoCódigo
printf("Meu compilador funciona!");
}
Agoraabraoterminaledigite gcc teste.c -o teste.out,noLi-
nux/Mac;ou gcc teste.c -o teste.exe,noWindows. Emseguida,
execute-o:noLinux/Mac, ./teste.out;enoWindows,clicandoduasve-
zesnoarquivo.Vocêdeveráverafrase“Meucompiladorfunciona!”.
Seaindaassimseucompiladornãofuncionar,omelhorafazerépesquisar
omotivonoGoogle.Procurarporfrasescomo“instalarGCCnoWindows”
ouoerroqueestáaparecendonatelapodeajudar.
250

## Página 262

Capítulo24
ApêndiceB:códigos
24.1 Jogo da adivinhação
// incluindo as bibliotecas
# include <stdio.h>
# include <stdlib.h>
# include <time.h>
// definindo as constantes
# define NUMERO_DE_TENTATIVAS 3
int main() {
// imprimindo um cabeçalho bonito do jogo
printf("\n\n");
printf(" P /_\\ P \n");

## Página 263

24.1. Jogodaadivinhação CasadoCódigo
printf(" /_\\_|_|_/_\\ \n");
printf(" n_n | ||. .|| | n_n Bem-vindo ao \n");
printf(" |_|_|nnnn nnnn|_|_| Jogo de Adivinhação! \n");
printf(" |\" \" | |_| |\" \" | \n");
printf(" |_____| ' _ ' |_____| \n");
printf(" \\__|_|__/ \n");
printf("\n\n");
// declarando variáveis que serão usadas mais à frente
int chute;
int acertou;
int nivel;
int totaldetentativas;
// definindo a quantidade de pontos inicial
double pontos = 1000;
// gerando um número secreto aleatório
srand(time( 0));
int numerosecreto = rand() % 100;
// escolhendo o nível de dificuldade
printf("Qual o nível de dificuldade?\n");
printf("(1) Fácil (2) Médio (3) Difícil\n\n");
printf("Escolha: ");
scanf("%d", &nivel);
switch(nivel) {
case 1:
totaldetentativas = 20;
break;
case 2:
totaldetentativas = 15;
break;
default:
totaldetentativas = 6;
break;
}
252

## Página 264

CasadoCódigo Capítulo24. ApêndiceB:códigos
// loop principal do jogo
for(int i = 1; i <= totaldetentativas; i++) {
printf("-> Tentativa %d de %d\n", i, totaldetentativas);
printf("Chute um número: ");
scanf("%d" , & chute);
// tratando chute de número negativo
if(chute < 0) {
printf("Você não pode chutar números negativos\n");
i--;
continue;
}
// verifica se acertou foi maior ou menor
acertou = chute == numerosecreto;
if(acertou) {
break;
} else if(chute > numerosecreto) {
printf("\nSeu chute foi maior do que o número secreto!\n
\n");
} else {
printf("\nSeu chute foi menor do que o número secreto!\n
\n");
}
// calcula a quantidade de pontos
double pontosperdidos = abs(chute - numerosecreto) / 2.0;
pontos = pontos - pontosperdidos;
}
// imprimindo mensagem de vitória ou derrota
printf("\n" );
if(acertou) {
printf(" OOOOOOOOOOO \n");
printf(" OOOOOOOOOOOOOOOOOOO \n");
253

## Página 265

24.2. Jogodeforca CasadoCódigo
printf(" OOOOOO OOOOOOOOO OOOOOO \n");
printf(" OOOOOO OOOOO OOOOOO \n");
printf(" OOOOOOOO # OOOOO # OOOOOOOO \n");
printf(" OOOOOOOOOO OOOOOOO OOOOOOOOOO \n");
printf("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO \n");
printf("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO \n");
printf("OOOO OOOOOOOOOOOOOOOOOOOOOOOOO OOOO \n");
printf(" OOOO OOOOOOOOOOOOOOOOOOOOOOO OOOO \n");
printf(" OOOO OOOOOOOOOOOOOOOOOOOO OOOO \n");
printf(" OOOOO OOOOOOOOOOOOOOO OOOO \n");
printf(" OOOOOO OOOOOOOOO OOOOOO \n");
printf(" OOOOOO OOOOOO \n");
printf(" OOOOOOOOOOOO \n");
printf("\nParabéns! Você acertou!\n");
printf("Você fez %.2f pontos. Até a próxima!\n\n", pontos);
} else {
printf(" \\|/ ____ \\|/ \n" );
printf(" @~/ ,. \\~@ \n");
printf(" /_( \\__/ )_\\ \n" );
printf(" \\__U_/ \n");
printf("\nVocê perdeu! Tente novamente!\n\n");
}
}
24.2 Jogo de forca
•forca.c
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <time.h>
# include "forca.h"
char palavrasecreta[TAMANHO_PALAVRA];
254

## Página 266

CasadoCódigo Capítulo24. ApêndiceB:códigos
char chutes[26];
int chutesdados = 0;
int letraexiste(char letra) {
for(int j = 0; j < strlen(palavrasecreta); j++) {
if(letra == palavrasecreta[j]) {
return 1;
}
}
return 0;
}
int chuteserrados() {
int erros = 0;
for(int i = 0; i < chutesdados; i++) {
if(!letraexiste(chutes[i])) {
erros++;
}
}
return erros;
}
int enforcou() {
return chuteserrados() >= 5;
}
int ganhou() {
for(int i = 0; i < strlen(palavrasecreta); i++) {
if(!jachutou(palavrasecreta[i])) {
return 0;
}
}
255

## Página 267

24.2. Jogodeforca CasadoCódigo
return 1;
}
void abertura() {
printf("/****************/\n");
printf("/ Jogo de Forca */\n");
printf("/****************/\n\n");
}
void chuta() {
char chute;
printf("Qual letra? ");
scanf(" %c", &chute);
if(letraexiste(chute)) {
printf("Você acertou: a palavra tem a letra %c\n\n",
chute);
} else {
printf("\nVocê errou: a palavra NÃO tem a letra %c\n\n",
chute);
}
chutes[chutesdados] = chute;
chutesdados++;
}
int jachutou(char letra) {
int achou = 0;
for(int j = 0; j < chutesdados; j++ ) {
if(chutes[j] == letra) {
achou = 1;
break;
}
}
return achou;
}
256

## Página 268

CasadoCódigo Capítulo24. ApêndiceB:códigos
void desenhaforca() {
int erros = chuteserrados();
printf(" _______ \n");
printf(" |/ | \n");
printf(" | %c%c%c \n", (erros>=1?'(':' '),
(erros>=1?'_':' '), (erros>=1?')':' '));
printf(" | %c%c%c \n", (erros>=3?'\\':' '),
(erros>=2?'|':' '), (erros>=3?'/': ' '));
printf(" | %c \n", (erros>=2? '|':' '));
printf(" | %c %c \n", (erros>=4?'/':' '),
(erros>=4?'\\':' '));
printf(" | \n");
printf("_|___ \n");
printf("\n\n");
for(int i = 0; i < strlen(palavrasecreta); i++) {
if(jachutou(palavrasecreta[i])) {
printf("%c ", palavrasecreta[i]);
} else {
printf("_ ");
}
}
printf("\n");
}
void escolhepalavra() {
FILE* f;
f = fopen("palavras.txt", "r");
if(f == 0) {
printf("Banco de dados de palavras não disponível\n\n");
exit(1);
}
257

## Página 269

24.2. Jogodeforca CasadoCódigo
int qtddepalavras;
fscanf(f, "%d", & qtddepalavras);
srand(time(0));
int randomico = rand() % qtddepalavras;
for(int i = 0; i <= randomico; i++) {
fscanf(f, "%s", palavrasecreta);
}
fclose(f);
}
void adicionapalavra() {
char quer;
printf("Você deseja adicionar uma nova palavra no
jogo (S/N)?");
scanf(" %c", &quer);
if(quer == 'S') {
char novapalavra[TAMANHO_PALAVRA];
printf("Digite a nova palavra, em letras maiúsculas: " );
scanf("%s" , novapalavra);
FILE* f;
f = fopen("palavras.txt", "r+");
if(f == 0) {
printf("Banco de dados de palavras não
disponível\n\n");
exit(1);
}
int qtd;
fscanf(f, "%d", & qtd);
qtd++;
258

## Página 270

CasadoCódigo Capítulo24. ApêndiceB:códigos
fseek(f, 0, SEEK_SET);
fprintf(f, "%d", qtd);
fseek(f, 0, SEEK_END);
fprintf(f, "\n%s", novapalavra);
fclose(f);
}
}
int main() {
abertura();
escolhepalavra();
do {
desenhaforca();
chuta();
} while (!ganhou() && !enforcou());
if(ganhou()) {
printf("\nParabéns, você ganhou!\n\n");
printf(" ___________ \n");
printf(" '._==_==_=_.' \n");
printf(" .-\\: /-. \n");
printf(" | (|:. |) | \n");
printf(" '-|:. |-' \n");
printf(" \\::. / \n");
printf(" '::. .' \n");
printf(" ) ( \n");
printf(" _.' '._ \n");
printf(" '-------' \n\n");
} else {
259

## Página 271

24.2. Jogodeforca CasadoCódigo
printf("\nPuxa, você foi enforcado!\n");
printf("A palavra era **%s**\n\n", palavrasecreta);
printf(" _______________ \n");
printf(" / \\ \n");
printf(" / \\ \n");
printf("// \\/\\ \n");
printf("\\| XXXX XXXX | / \n");
printf(" | XXXX XXXX |/ \n");
printf(" | XXX XXX | \n");
printf(" | | \n");
printf(" \\__ XXX __/ \n");
printf(" |\\ XXX /| \n");
printf(" | | | | \n");
printf(" | I I I I I I I | \n");
printf(" | I I I I I I | \n");
printf(" \\_ _/ \n");
printf(" \\_ _/ \n");
printf(" \\_______/ \n");
}
adicionapalavra();
}
•forca.h
# define TAMANHO_PALAVRA 20
int letraexiste (char letra);
int chuteserrados();
int enforcou();
void abertura();
void chuta();
int jachutou(char letra);
int ganhou();
void desenhaforca();
void escolhepalavra();
void adicionapalavra();
260

## Página 272

CasadoCódigo Capítulo24. ApêndiceB:códigos
24.3 Foge-foge
•fogefoge.c
# include <stdio.h>
# include <stdlib.h>
# include "time.h"
# include "fogefoge.h"
# include "mapa.h"
# include "ui.h"
MAPA m;
POSICAO heroi;
int tempilula = 0;
int acabou() {
POSICAO pos;
int perdeu = !encontramapa(&m, &pos, HEROI);
int ganhou = !encontramapa(&m, &pos, FANTASMA);
return ganhou || perdeu;
}
int ehdirecao( char direcao) {
return
direcao == ESQUERDA ||
direcao == CIMA ||
direcao == BAIXO ||
direcao == DIREITA;
}
void move(char direcao) {
int proximox = heroi.x;
int proximoy = heroi.y;
switch(direcao) {
case ESQUERDA:
261

## Página 273

24.3. Foge-foge CasadoCódigo
proximoy--;
break;
case CIMA:
proximox--;
break;
case BAIXO:
proximox++;
break;
case DIREITA:
proximoy++;
break;
}
if(!podeandar(&m, HEROI, proximox, proximoy))
return;
if(ehpersonagem(&m, PILULA, proximox, proximoy)) {
tempilula=1;
}
andanomapa(&m, heroi.x, heroi.y, proximox, proximoy);
heroi.x = proximox;
heroi.y = proximoy;
}
int praondefantasmavai(int xatual, int yatual,
int* xdestino, int* ydestino) {
int opcoes[4][ 2] = {
{ xatual , yatual+1 },
{ xatual+1 , yatual },
{ xatual , yatual-1 },
{ xatual-1 , yatual }
};
srand(time(0));
for(int i = 0; i < 10; i++) {
int posicao = rand() % 4;
262

## Página 274

CasadoCódigo Capítulo24. ApêndiceB:códigos
if(podeandar(&m, FANTASMA, opcoes[posicao][0],
opcoes[posicao][1])) {
*xdestino = opcoes[posicao][0];
*ydestino = opcoes[posicao][1];
return 1;
}
}
return 0;
}
void fantasmas() {
MAPA copia;
copiamapa(&copia, &m);
for(int i = 0; i < copia.linhas; i ++) {
for(int j = 0; j < copia.colunas; j ++) {
if(copia.matriz[i][j] == FANTASMA)
int xdestino;
int ydestino;
int encontrou = praondefantasmavai(i, j,
&xdestino,
&ydestino);
if(encontrou) {
andanomapa(&m, i, j, xdestino, ydestino);
}
}
}
}
liberamapa(&copia);
}
void explodepilula2(int x, int y, int somax, int somay, int qtd){
263

## Página 275

24.3. Foge-foge CasadoCódigo
if(qtd == 0) return;
int novox = x+somax;
int novoy = y+somay;
if(!ehvalida(&m, novox, novoy)) return;
if(ehparede(&m, novox, novoy)) return;
m.matriz[novox][novoy] = VAZIO;
explodepilula2(novox, novoy, somax, somay, qtd-1);
}
void explodepilula() {
explodepilula2(heroi.x, heroi.y, 0, 1, 3);
explodepilula2(heroi.x, heroi.y, 0, -1, 3);
explodepilula2(heroi.x, heroi.y, 1, 0, 3);
explodepilula2(heroi.x, heroi.y, -1, 0, 3);
}
int main() {
lemapa(&m);
encontramapa(&m, &heroi, HEROI);
do {
printf("Pílula: %s\n", (tempilula ? "SIM" : "NÃO"));
imprimemapa(&m);
char comando;
scanf(" %c", &comando);
if(ehdirecao(comando)) move(comando);
if(comando == BOMBA) explodepilula();
fantasmas();
} while (!acabou());
liberamapa(&m);
264

## Página 276

CasadoCódigo Capítulo24. ApêndiceB:códigos
}
•fogefoge.h
# ifndef _FOGEFOGE_H_
# define _FOGEFOGE_H_
# define CIMA 'w'
# define BAIXO 's'
# define DIREITA 'd'
# define ESQUERDA 'a'
# define BOMBA 'b'
int acabou();
void move(char direcao);
int ehdirecao(char direcao);
void fantasmas ();
void explodepilula();
void explodepilula2(int x, int y, int somax, int somay, int qtd);
# endif
•mapa.c
# include <stdio.h>
# include <stdlib.h>
# include "mapa.h"
# include <string.h>
void lemapa(MAPA* m) {
FILE* f;
f = fopen("mapa.txt", "r");
if(f == 0) {
printf("Erro na leitura do mapa");
exit(1);
}
265

## Página 277

24.3. Foge-foge CasadoCódigo
fscanf(f, "%d %d" , &(m->linhas), &(m->colunas));
alocamapa(m);
for(int i = 0; i < m->linhas; i++) {
fscanf(f, "%s", m ->matriz[i]);
}
fclose(f);
}
void alocamapa(MAPA* m) {
m->matriz = malloc(sizeof(char*) * m->linhas);
for(int i = 0; i < m->linhas; i++) {
m->matriz[i] = malloc(sizeof(char) * m->colunas + 1);
}
}
void copiamapa(MAPA* destino, MAPA* origem) {
destino->linhas = origem->linhas;
destino->colunas = origem->colunas;
alocamapa(destino);
for(int i = 0; i < origem->linhas; i++) {
strcpy(destino->matriz[i], origem->matriz[i]);
}
}
void liberamapa (MAPA* m) {
for(int i = 0; i < m->linhas; i++) {
free(m->matriz[i]);
}
free(m->matriz);
}
int encontramapa(MAPA* m, POSICAO* p, char c) {
266

## Página 278

CasadoCódigo Capítulo24. ApêndiceB:códigos
for(int i = 0; i < m->linhas; i++) {
for(int j = 0; j < m->colunas; j++) {
if(m->matriz[i][j] == c) {
p->x = i;
p->y = j;
return 1;
}
}
}
return 0;
}
int podeandar(MAPA* m, char personagem, int x, int y) {
return
ehvalida(m, x, y) &&
!ehparede(m, x, y) &&
!ehpersonagem(m, personagem, x, y);
}
int ehvalida(MAPA* m, int x, int y) {
if(x >= m->linhas)
return 0;
if(y >= m->colunas)
return 0;
return 1;
}
int ehpersonagem(MAPA* m, char personagem, int x, int y) {
return
m->matriz[x][y] == personagem;
}
int ehparede(MAPA* m, int x, int y) {
return
m->matriz[x][y] == PAREDE_VERTICAL ||
m->matriz[x][y] == PAREDE_HORIZONTAL;
}
267

## Página 279

24.3. Foge-foge CasadoCódigo
void andanomapa(MAPA* m, int xorigem, int yorigem,
int xdestino, int ydestino) {
char personagem = m-> matriz[xorigem][yorigem];
m->matriz[xdestino][ydestino] = personagem;
m->matriz[xorigem][yorigem] = VAZIO;
}
•mapa.h
# ifndef _MAPA_H_
# define _MAPA_H_
# define HEROI '@'
# define VAZIO '.'
# define PAREDE_VERTICAL '|'
# define PAREDE_HORIZONTAL '-'
# define FANTASMA 'F'
# define PILULA 'P'
struct mapa {
char** matriz;
int linhas;
int colunas;
};
typedef struct mapa MAPA;
void alocamapa(MAPA* m);
void lemapa(MAPA* m);
void liberamapa (MAPA* m);
struct posicao {
int x;
int y;
268

## Página 280

CasadoCódigo Capítulo24. ApêndiceB:códigos
};
typedef struct posicao POSICAO;
int encontramapa(MAPA* m, POSICAO* p, char c);
int ehvalida(MAPA* m, int x, int y);
int ehparede(MAPA* m, int x, int y);
int ehpersonagem(MAPA* m, char personagem, int x, int y);
void andanomapa(MAPA* m, int xorigem, int yorigem,
int xdestino, int ydestino);
void copiamapa (MAPA* destino, MAPA* origem);
int podeandar(MAPA* m, char personagem, int x, int y);
# endif
•ui.c
#include <stdio.h>
#include "mapa.h"
char desenhoparede[4][7] = {
{"......" },
{"......" },
{"......" },
{"......" }
};
char desenhofantasma[4][7] = {
{" .-. " },
{"| OO| " },
{"| | " },
{"'^^^' " }
};
char desenhoheroi[4][7] = {
269

## Página 281

24.3. Foge-foge CasadoCódigo
{" .--. " },
{"/ _.-'" },
{"\\ '-." },
{" '--' " }
};
char desenhopilula[4][7] = {
{" "},
{" .-. "},
{" '-' "},
{" "}
};
char desenhovazio[4][7] = {
{" "},
{" "},
{" "},
{" "}
};
void imprimeparte(char desenho[4][7], int parte) {
printf("%s", desenho[parte]);
}
void imprimemapa(MAPA* m) {
for(int i = 0; i < m->linhas; i++) {
for(int parte = 0; parte < 4; parte++) {
for(int j = 0; j < m->colunas; j++) {
switch(m->matriz[i][j]) {
case FANTASMA:
imprimeparte(desenhofantasma, parte);
break;
case HEROI:
imprimeparte(desenhoheroi, parte);
break;
case PILULA:
imprimeparte(desenhopilula, parte);
270

## Página 282

CasadoCódigo Capítulo24. ApêndiceB:códigos
break;
case PAREDE_VERTICAL:
case PAREDE_HORIZONTAL:
imprimeparte(desenhoparede, parte);
break;
case VAZIO:
imprimeparte(desenhovazio, parte);
break;
}
}
printf("\n");
}
}
}
•ui.h
# ifndef _UI_H_
# define _UI_H_
# include "mapa.h"
void imprimeparte(char desenho[4][7], int parte);
void imprimemapa(MAPA* m);
# endif
271