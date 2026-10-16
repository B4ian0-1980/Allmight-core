---json
{
  "id": "introdu__o___computa__o_da_l_gica_aos_jogos_com_ruby",
  "title": "Introdução à Computação Da lógica aos jogos com Ruby",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `Introdução à Computação Da lógica aos jogos com Ruby.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aos",
    "com",
    "computa",
    "gica",
    "introdu",
    "jogos",
    "linguagens",
    "php"
  ],
  "perguntas_tipo": [
    "Como utilizar Introdução à Computação Da lógica aos jogos com Ruby?",
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

# Introdução à Computação Da lógica aos jogos com Ruby

> **Arquivo Original:** `Introdução à Computação Da lógica aos jogos com Ruby.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

48000


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
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 3

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 4

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 5

CasadoCódigo Sumário
Sumário
1 Introdução 1
1.1 Programa ção . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Paraoprofessor . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 Quemsoueu . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 Agradecimentos . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 PrefácioporFábioAkita 5
3 Jogodaadivinha ção 9
3.1 Ojogo:entradaesaídabásica . . . . . . . . . . . . . . . . . . 9
3.2 Seráqueacertou?Ooperadordecompara ção==. . . . . . . 15
3.3 Operadordeatribui çãoevariáveis . . . . . . . . . . . . . . . 18
3.4 Operadoresdecompara ção. . . . . . . . . . . . . . . . . . . . 19
3.5 Entradaesaída. . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.6 Oquesãofun ções . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.7 Refatora ção:\n. . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.8 Interpretadoroucompilador. . . . . . . . . . . . . . . . . . . 22
3.9 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4 Controledefluxo 25
4.1 Masese...ifeelse . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.2 Codesmell:comentários . . . . . . . . . . . . . . . . . . . . . 28
4.3 Condi çõesaninhadas(nestedifs) . . . . . . . . . . . . . . . . 29
4.4 Codesmell:copyepaste . . . . . . . . . . . . . . . . . . . . . 31
i
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 6

Sumário CasadoCódigo
4.5 Ola çofor(loop) . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.6 Aplicandoola ço foraonossoprograma . . . . . . . . . . . . 36
4.7 Codesmell:Magicnumbers . . . . . . . . . . . . . . . . . . . 38
4.8 Refatora ção:extrairvariável . . . . . . . . . . . . . . . . . . . 39
4.9 Quebrandoola çocomobreak. . . . . . . . . . . . . . . . . . 39
4.10 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5 Funções 43
5.1 Fun ções . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.2 Boaprática:encapsulamentodecomportamento . . . . . . . 46
5.3 Escopodevariáveis . . . . . . . . . . . . . . . . . . . . . . . . 47
5.4 Codesmell:variáveissemcontroledeescopoevariáveisglobais 49
5.5 Retornodefun ção . . . . . . . . . . . . . . . . . . . . . . . . . 50
5.6 Variáveislocais . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
5.7 Extraindomaisumafun ção . . . . . . . . . . . . . . . . . . . 56
5.8 Boaprática:earlyreturn . . . . . . . . . . . . . . . . . . . . . 59
5.9 Pequenasrefatora çõesespecíficasdalinguagem. . . . . . . . 60
5.10 Resumindo:opoderdaextra çãodecódigo . . . . . . . . . . 61
5.11 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
6 Arrays 65
6.1 Criandoemanipulandoarrays. . . . . . . . . . . . . . . . . . 66
6.2 Aplicandooarrayaonossojogo . . . . . . . . . . . . . . . . . 69
6.3 Facilidadesdeumarray. . . . . . . . . . . . . . . . . . . . . . 71
6.4 Simplificandonossocódigodearray . . . . . . . . . . . . . . 73
6.5 ArrayseStrings . . . . . . . . . . . . . . . . . . . . . . . . . . 74
6.6 Interpola çãodeStrings . . . . . . . . . . . . . . . . . . . . . . 76
6.7 Fun çõesemétodos . . . . . . . . . . . . . . . . . . . . . . . . 77
6.8 TestandométodosnoIRB . . . . . . . . . . . . . . . . . . . . 77
6.9 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
ii
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 7

CasadoCódigo Sumário
7 Pontosematemática 81
7.1 Pontoflutuante. . . . . . . . . . . . . . . . . . . . . . . . . . . 83
7.2 Simula çãodocódigo . . . . . . . . . . . . . . . . . . . . . . . 86
7.3 Matemática . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
7.4 Unless...eaduplanega ção . . . . . . . . . . . . . . . . . . . . 89
7.5 Númeroaleatório . . . . . . . . . . . . . . . . . . . . . . . . . 90
7.6 Operadoresmatemáticos . . . . . . . . . . . . . . . . . . . . . 91
7.7 Sistemadetipos . . . . . . . . . . . . . . . . . . . . . . . . . . 92
7.8 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
8 Binário 95
8.1 Binário . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
8.2 Binárioeletras . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
8.3 Bits:8,16,32,64 . . . . . . . . . . . . . . . . . . . . . . . . . . 97
8.4 Bitsenúmeroscompontoflutuante. . . . . . . . . . . . . . . 98
8.5 Hexadecimal . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
8.6 Bitseimagens . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
8.7 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
9 Níveldedificuldadeeocase 103
9.1 Case...when...end . . . . . . . . . . . . . . . . . . . . . . . . . 106
9.2 Escopodevariávellocal. . . . . . . . . . . . . . . . . . . . . . 107
9.3 Trapaceando . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
9.4 Corrigindoonúmerosorteado . . . . . . . . . . . . . . . . . 109
9.5 While:jogandodiversasvezes . . . . . . . . . . . . . . . . . . 112
9.6 loopdo...end . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
9.7 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
10 ArteASCII:jogodaadivinha ção 121
10.1 Melhorandonossainterfacecomousuário . . . . . . . . . . 121
11 Exercíciosextras:jogodaadivinha ção 125
11.1 Melhorandoojogodeadivinha ção . . . . . . . . . . . . . . . 125
11.2 Outrosdesafios. . . . . . . . . . . . . . . . . . . . . . . . . . . 126
iii
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 8

Sumário CasadoCódigo
12 Jogodaforca 129
12.1 Chutedeumapalavracompletaeacompara çãocom== . . 132
12.2 Encontrandoumalgoritmo. . . . . . . . . . . . . . . . . . . . 134
12.3 Implementandooalgoritmo . . . . . . . . . . . . . . . . . . . 135
12.4 Boaprática:explorandoadocumenta ção. . . . . . . . . . . . 139
12.5 next...Evitandochutesrepetidos. . . . . . . . . . . . . . . . . 142
12.6 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
13 Responsabilidades 145
13.1 Mostrandopartedapalavrasecreta . . . . . . . . . . . . . . . 145
13.2 Separandoainterfacecomousuáriodalógicadenegócios . 146
13.3 Extraindoalógicadenegócios. . . . . . . . . . . . . . . . . . 152
13.4 Extraindoalógicadeumchuteválido . . . . . . . . . . . . . 153
13.5 Implementação:mostrandopartedapalavrasecreta . . . . . 156
13.6 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
14 Entradaesaídadearquivo:palavrasaleatóriaseotopplayer 161
14.1 Lendoumarquivodepalavras,nossodicionário . . . . . . . 161
14.2 Limpandoaentradadedados . . . . . . . . . . . . . . . . . . 163
14.3 Processamentoememóriadevemserotimizadas? . . . . . . 164
14.4 Escritaparaarquivo:omelhorjogador . . . . . . . . . . . . . 166
14.5 Lendoomelhorjogador . . . . . . . . . . . . . . . . . . . . . 168
14.6 Refatoração:extrairarquivo . . . . . . . . . . . . . . . . . . . 170
14.7 Apilhadeexecu ção . . . . . . . . . . . . . . . . . . . . . . . . 171
14.8 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
15 ArteASCII:jogodaforca 181
15.1 Melhorandonossainterfacecomousuário . . . . . . . . . . 181
16 Exercíciosextras:jogodaforca 187
16.1 Melhorandoojogodaforca . . . . . . . . . . . . . . . . . . . 187
16.2 Outrosdesafios. . . . . . . . . . . . . . . . . . . . . . . . . . . 189
iv
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 9

CasadoCódigo Sumário
17 Foge-foge,umjogobaseadonoPacman 191
17.1 Definindoabasedojogoeomapa . . . . . . . . . . . . . . . 191
17.2 Arraydearray:matriz. . . . . . . . . . . . . . . . . . . . . . . 194
17.3 Movimento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
17.4 Refatorando . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
17.5 Ovazio,onulo . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
17.6 Laçofuncionalbásico . . . . . . . . . . . . . . . . . . . . . . . 201
17.7 Extraindoaposi ção . . . . . . . . . . . . . . . . . . . . . . . . 202
17.8 Refatorando . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
17.9 Passagemporreferênciaouvalor?. . . . . . . . . . . . . . . . 206
17.10 Detecçãodecolisãocomomuroeofimdomapa. . . . . . . 208
17.11 Refatorandocom||e&& . . . . . . . . . . . . . . . . . . . . . 210
17.12 Ducktypingnaprática . . . . . . . . . . . . . . . . . . . . . . 214
17.13 forixforlinha . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
17.14 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
18 Botandoosfantasmasparacorrer:arraysassociativos,ducktyping
eoutros 219
18.1 Arrayassociativo:casee+1,-1 . . . . . . . . . . . . . . . . . . 219
18.2 Movimentodosfantasmas:odesafionoducktyping . . . . . 223
18.3 Movimentodosfantasmas:reutiliza çãodefun ção . . . . . . 228
18.4 Fantasmacontrafantasma?. . . . . . . . . . . . . . . . . . . . 230
18.5 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
19 Matrizesememória 233
19.1 Teletransportandofantasmas:cuidadosatomarcomamemória233
19.2 Corrigindooteletransporte . . . . . . . . . . . . . . . . . . . 237
19.3 Copiandonossomapa. . . . . . . . . . . . . . . . . . . . . . . 240
19.4 Movendoosfantasmasnamatrizcopiada . . . . . . . . . . . 242
19.5 Refatorandoomovimentodofantasma. . . . . . . . . . . . . 248
19.6 Ofantasmacavaleiro . . . . . . . . . . . . . . . . . . . . . . . 251
19.7 Movimentoaleatóriodosfantasmas. . . . . . . . . . . . . . . 252
19.8 Quandooheróiperde. . . . . . . . . . . . . . . . . . . . . . . 253
19.9 Retornonuloouopcional? . . . . . . . . . . . . . . . . . . . . 256
19.10Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256
v
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 10

Sumário CasadoCódigo
20 Estruturaseclasses:umaintrodu çãoaOrienta çãoaObjetos 259
20.1 Abagunçadosdefs . . . . . . . . . . . . . . . . . . . . . . . . 259
20.2 Extraindoumaprimeiraestrutura. . . . . . . . . . . . . . . . 260
20.3 Usandoumaestrutura. . . . . . . . . . . . . . . . . . . . . . . 262
20.4 Codesmell:featureenvy . . . . . . . . . . . . . . . . . . . . . 264
20.5 Boaprática:buscarqueminvocaantesderefatorar . . . . . . 267
20.6 Boaprática:Tell,don’task . . . . . . . . . . . . . . . . . . . . 270
20.7 Atributoseattr_accessor . . . . . . . . . . . . . . . . . . . . . 270
20.8 EstruturaouClasse?. . . . . . . . . . . . . . . . . . . . . . . . 271
20.9 Averdadeportrásdemétodos,fun çõeselambdas . . . . . . 272
20.10Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
21 Destruindoosfantasmas:omundodarecursão 275
21.1 Destruindoosfantasmas . . . . . . . . . . . . . . . . . . . . . 275
21.2 Andandoparaadireita . . . . . . . . . . . . . . . . . . . . . . 277
21.3 Recursãoinfinita. . . . . . . . . . . . . . . . . . . . . . . . . . 278
21.4 Abasedarecursão. . . . . . . . . . . . . . . . . . . . . . . . . 282
21.5 Basedarecursão:distânciaquatrooumuro . . . . . . . . . . 284
21.6 Recursãoparatodososlados:buscaemprofundidade . . . . 285
21.7 Resumindo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
22 Exercíciosextras:jogodofoge-foge 289
22.1 MelhorandooJogodofoge-foge. . . . . . . . . . . . . . . . . 289
22.2 Outrosdesafios. . . . . . . . . . . . . . . . . . . . . . . . . . . 290
23 InstalandooRuby 291
23.1 InstalaçãonoWindows . . . . . . . . . . . . . . . . . . . . . . 291
23.2 InstalaçãonoLinux . . . . . . . . . . . . . . . . . . . . . . . . 292
23.3 InstalaçãonoMacOSX. . . . . . . . . . . . . . . . . . . . . . 292
23.4 Oeditordetexto . . . . . . . . . . . . . . . . . . . . . . . . . . 292
vi
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 11

CasadoCódigo Sumário
24 Comocontinuar 295
24.1 Praticar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
24.2 Estruturadedadosealgoritmos . . . . . . . . . . . . . . . . . 296
24.3 OrientaçãoaObjetos?. . . . . . . . . . . . . . . . . . . . . . . 296
24.4 Competiçõesdeprograma çãodaACM. . . . . . . . . . . . . 296
24.5 Outralinguagem? . . . . . . . . . . . . . . . . . . . . . . . . . 297
24.6 Compartilheeboajornada . . . . . . . . . . . . . . . . . . . . 298
Versão:18.4.26
vii
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 12

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 13

Capítulo1
Introdução
1.1 Programação
Oprofissionalquecriaocódigoportrásdeumjogo,umsitenainternetouum
aplicativomobileéoprogramador.Eleéodonodoseu,domeu,detodosos
computadores.Nãoqueremosserapenasusuários,queligamocomputador
esãoobrigadosaseguirasregrasestabelecidasporoutros.Avontadedecriar
algonovo,dealteraralgoexistente,éoquenostornaprogramadores.
Todaintrodu çãoaprograma çãoenvolveentenderporcimacomofunci-
onamocomputadoreumprograma.Asimplica çõesnoslimitesdacompu-
taçãosãosentidosnodiaadiadoprogramador.
Aideiaportrásdestematerialédecobriroconteúdodeumamatériade
IntroduçãoàPrograma çãodoprimeiroousegundosemestredeumafacul-
dadedeAnálisedeSistemas,CiênciadaComputa ção,Engenhariaetc.Por-
tantonãopretendemosabordartópicosmuitoespecíficosdeumalinguagem
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 14

1.2. Paraoprofessor CasadoCódigo
ououtra,massimtratardequestõessobrecomoumprogramaécriado,qual
asuabase,comodetectarproblemasetransformarnossasideiasesolu ções
emcódigo.
Vamosnosfocaremconceitosextremamenteimportantescomoconstru-
çãodalógica,pilhadeexecu ção,simula çãodecódigoearecursão.
Porissonãoseguiremosaopédaletratodososidiomatismosdalingua-
gemRuby,masmostraremosdiversasvaria çõesdecomoseprogramaruma
mesmaestruturalógica,tentandoindicarvantagensedesvantagensdecada
abordagem.
Duranteessajornadacriaremostrêsjogosdistintos,umjogodeadivi-
nhaçãonumérica,umjogodaforcaeumbaseadonoclássicoPacman nosso
Foge-Foge.
Ojogodeadivinha çãopermiteaojogadorescolheroníveldedificuldade
eeletemqueacertaronúmerosecretoescolhidoemumintervaloquede-
pendedadificuldade. Sãodadasdicasemrela çãoaonúmeroacadanovo
chute.
Jánojogodaforca,ojogadordeveadivinharumapalavrasecretalida
aleatoriamentedeumarquivoquefuncionacomoumdicionário.Passaremos
aarmazenarqueméograndeganhadordojogoemumarquivolocal.
Porfim,noFoge-Fogeveremoscomoimplementarumjogobaseadoem
turnos( turn based)ondeoheróipodeandarporummapa,lidoentrediversos
arquivos,cominimigos(fantasmas)ebombasquepodemosusar.
Nofim,vocêestaráaptoparatomaropróximopassoemsuacarreira
comoprofissionaldesenvolvedor,sejapraticandomais,aprendendoOrien-
taçãoaObjetos,estruturadedados,algoritmos,tudodeacordocomoque
desejaparasi,umacarreiranomundodosjogos,internet,mobileetc.
Todoocódigopodeserencontradonolinkaseguir,eleestáseparadode
acordocomofinaldecadacapítulo.
http://bit.ly/1LGOznk
1.2 Para o professor
Aoutilizaressematerialemsuasaladeaula,oferecemosdiversosexercícios
quesãoextensõesligadasdiretamenteaosjogosimplementados.Oferecemos
2
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 15

CasadoCódigo Capítulo1. Introdução
tambémdesafiosnuméricosquepermitemaoalunocriarumnovoprograma
dozero.
Sinta-seàvontadeparaenviarsugestõesdenovosexercícios,sejameles
numéricos,lógicos,jogos,ouextensõesaojogocriado.
1.3 Quem sou eu
Agoraqueapartemaisimportante nossoaprendizado jáfoidiscutido,che-
gamosàminhaapresenta ção.
MeunomeéGuilhermeSilveira,trabalhocomdesenvolvimentodesoft-
waredesdemeuprimeiroestágioem1996. Aprendiaprogramarnaépoca
aos9anos,meuirmãoerameuprofessorparticular,quemeinstigouacriar
pequenosjogosemBasic. Jogossãomotivosinteressantespoistrazemum
prazertantonodesenvolvimentoquantoapossibilidadedecompartilhá-los
comqualquerumdenossosfamiliares.
ApesardetertrabalhadoporumbomtempocomVisualBasic,CeC++,
crescicomoprofissionalutilizandoalinguagemJava,queatéhojeéaminha
principalferramenta,masnuncamemantiverestritoaela apesardogosto
pessoal.AprendiRubyaprimeiravezem2009evejoalinguagemcomoum
contrapontointeressanteàabordagem type safeecompiladadoJava,oque
permiteentendermelhorospontosfortesefracosdecadalinguagem,ede
outrasquevimaaprendernosanosquesepassaram.
Porgostardeensinarcomputa çãodesdecrian ça,acabeiporfundarjunto
aoPauloSilveiraaCaelumem2004.Deláparacá,juntoaoMaurícioAniche
metorneicoordenadordoAlura,ondetenhoaoportunidadedecriarosmais
diversoscursos,efetuandoextensivapesquisacomexpertsemcadaárea. É
umprazerestarsempreaprendendocompessoastãointeressantesecheiasde
conhecimento,juntá-loerepassá-locomadidáticadaCaelumnostrêsmeios
queachomaisinteressanteshojeemdia: comolivro,comocursoonlinee
presencial.
1.4 Agradecimentos
Dedicoestelivroaomeupai,CarlosFelício,pelasuaalegria,nossafelicidade,
porteracreditadoemmeupotencialcomoeducadorematemático,porter
3
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 16

1.4. Agradecimentos CasadoCódigo
incentivadominhaindependênciaecrescimentoprofissional. Sãocentenas
ospontosdeminhavidapessoaleprofissionalondeocaminhofoicaminhado
pormim,masnãosemantesconsultá-lo.
UmagradecimentoespecialaoPauloSilveira,quemaisde20anosatrás
meensinouoconteúdoaquipresente,equemeincentivouaescrevereste
livro.
AgradeçoàJovianeJardim,quetantoatualizaomaterialdidáticodaCa-
elumsobreRuby,respectivamentedequemeondepudeaprender comose
porquêsdalinguagem. AgradeçoaoFábioAkita,cujoblogservecomoins-
piraçãoparaentendermelhoraevolu çãodalinguagemedeseuecossistema
durantetodosessesanos.AoFábioKung,quemuitosanosatrásmeintrodu-
ziuaomundoRuby,emelevouaperguntarpelaprimeiravezcomoalingua-
geminfluenciavadiversascaracterísticasdemeucódigo,abrindoaportapara
minhasprimeirascríticasdetodasaslinguagens.
ObrigadoaoMaurícioAniche,pelasinúmerasdiscussõessemanaisque
temostodavezquecome çamosumnovolivro,ondemaisaprendodoque
ensino.EobrigadoaoAdrianoAlmeidaquemaisumavezaturoumeusspams
sobreoconteúdo,títuloeviabilidadedesteprojeto.
Obrigadoavocê,alunoeprofessor,estudanteaoseaventurarcomigopelo
aprendizadodeprograma ção,professoraocompartilharcomseusamigos
essenovomundoqueseabreparaumanovagera çãodejovensbrasileiros,
omundoondesomososdonosdocomputador.
4
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 17

Capítulo2
PrefácioporFábioAkita
Ascoisasmudammuitorápidonomundodatecnologia.Eucomeceiadigitar
minhasprimeiraslinhasdecódigonumMSXHotbitnomeiodosanos80,na
antigalinguagemBasic.
Escrevercódigoémuitosimples,literalmentequalquerumconseguepes-
quisartrechosdecódigonoGoogleecolartudojunto,emumemaranhado
deinstru çõesque,comsorte,consegueprocessaralgumacoisaútil.
Todosquepensamemtecnologiaimaginamummundoondetudomuda
constantemente,ondeoqueaprendemosontemvaiserjogadoforaamanhã
eteremosqueaprendertudodenovo. Qualosentidoemestudardemais
quandosabemosquepodemossimplesmentepegaralgunspeda çosdecódigo
efazertudoaparentementefuncionar?
Recentementeobserveiumachef,querealmenteestudougastronomia,
cozinhando.Aspequenascoisasmechamaramaaten ção.Paraengrossarum
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 18

CasadoCódigo
caldo,atémesmosnós,programadoresenerdsquemalsabemfritarumovo,
sabemosquebastacolocaralgumascolheresdemaizenae voilà.Elaprimeiro
pegouumpoucodocaldoemumatigelaemisturouamaizenabem,depois
jogounapanela. Porquê? Porquesecolocaramaizenadiretamenteelavai
empelotar.
Emumpequenoerro,elaesqueceudecolocarsalnoarroz.Eagora?Se
fosseeu,tentariaconsertarjogandosaldiretamentenoarrozetentandomis-
turar. Iaficarumadroga,partescomsaldemais,partesaindasemsal. Ela
pegouumatigeladeágua,misturouosaledaíjorrouaáguasalgadanesse
arroz.Ficoucomosenãotivessefaltadosal.
Oqueéisso? Sãotécnicasfundamentais,coisasqueparaqualquerchef
éoóbvio,onosso“helloworld”. Masparamim,umcompletoamador,são
novidadesqueserãomuitoúteisnofuturo.
Programarémuitofácil,comofazerarroz.Eusempredigoquequalquer
umpodecolocaringredientesnumapanelaeligarofogo,masissonãootorna
umchef. Damesmaforma,qualquerumpodedigitar(oucopiarecolar)
códigos,masissonãootornaumprogramador.
Gastronomia,pintura,música,programa ção,sãotodasprofissõesdeprá-
tica.Apráticanosfazmelhoresemnossaarte.Nãoéalgoquepodemosmera-
mentedecorareaplicarsemconsciênciadoquesignificaouaondequeremos
chegar. Eemqualquerprofissãodepráticaexistemfundamentos,conheci-
mentosessenciais,técnicasbásicas,quequantoantesentendermosmaisvão
facilitarnossaevolu ção.
OGuilhermeSilveiraéumdosmelhoresprogramadoresquejáconheci,
elerealmentetemnãosóavoca ção,masotalentotantoparaassimilaresse
tipodeconhecimentocomoparaexplicá-lo.Émuitoraroencontraressacom-
binação.
Estelivroqueeleescreveunãovaitorná-loogrande“ninja”daprogra-
mação.Não,elevailhedaresseconhecimentoessencialeastécnicasbásicas
que,sedevidamenteestudados,devemforneceroalicerceparaquequaisquer
novastecnologiasdopresenteedofuturoquesurjamsejammuitomaisfáceis
deassimilar.
MelhoraindaporqueoGuilhermeescolheunossaamadalinguagemRuby
paraajudá-losaaprenderemumaplataformaquefoicriadacomconceitos
6
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 19

CasadoCódigo Capítulo2. PrefácioporFábioAkita
comoestéticaeprodutividadeemmente. AtravésdalinguagemRubyedo
contextodecriarpequenaslógicasdejogos,conceitosimportantescomoen-
tradaesaída,fun ções,recursão,sãoexplicadoscomclareza.Conceitosesses
quesãouniversaiseimportantes,nãoimportaquallinguagemvocêusahoje
oupossausarnofuturo.
Bomestudo!
7
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 20

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 21

Capítulo3
Jogodaadivinha ção
3.1 O jogo: entrada e saída básica
Nossoprimeirograndeprojetoseráacria çãodeumjogoqueescolheum
númeroaleatório,enosdesafiaaadivinhá-lo. Ojogopermiteaescolhado
níveldedificuldade,nosdáfeedbackconstantesobrenossoserroseacertos.
Portanto,nossoprimeiroprogramanosdizseonúmeroémaioroume-
nordoqueoescolhidopelocomputador.Seráumarquivoescritonalingua-
gemRuby,quenomeescolherparaele? Comoojogobrincacommaiorou
menor,vamoschamarde maior_ou_menor,masqualaextensãoparaele?
OpadrãodoRubyéutilizaraextensão rb,portantocriamosumarquivo
chamado maior_ou_menor.rb.Oconteúdo?Vazio.
Dadoesseprograma,vazio,queremosmandarocomputadorexecutá-lo.
Paraissodizemosparao rubyrodarnossoarquivo:
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 22

3.1. Ojogo:entradaesaídabásica CasadoCódigo
ruby maior_ou_menor.rb
Enadaacontece.Claro,nãohavianadaparaserfeito.
Umprogramaéumalistadecomandosqueocomputadorobedece.So-
mososdonosdocomputadornãosófisicamente,massomosodonodesuas
“mentes”.Somoscapazesdedizercomandosqueocomputadordeveobede-
cer. EssescomandosserãoescritosaquinalinguagemRuby,eumtradutor,
umintérprete,serácapazdetraduziressescomandosparaumcódigo“ma-
luco”quenossamáquinaentende.Afinal,quemhojeemdiaqueraprendera
falaralínguadasmáquinas?Muitocomplicado,principalmenteparacome çar
aprogramar.Entãoaprendemosumalinguagemmaispróximadenósdoque
doscomputadores( uma linguagem de alto nível).Qualoprimeirocomando
quequerodarparameucomputador?Porfavor,imprimaumamensagemde
boas-vindas.
Paraissodizemosparaocomputadorcolocarumamensagemnasaída:
coloque, puts,amensagem "Bem-vindo ao jogo da adivinhação" :
puts "Bem-vindo ao jogo da adivinhação"
Asaídaaorodarnovamente ruby maior_ou_menor.rb éagoraoque
esperamos:
Bem-vindo ao jogo da adivinhação
Jásomososdonos.Elenosobedece,eamágicaagoraestáemaprender
maiscomandoseformasdejuntarcomandosparacriarprogramascomple-
xosquefazemasmaisdiversastarefas,desdeumjogoatémesmoumpiloto
automáticodeavião.Todoselessãocódigosescritosporsereshumanos,eo
computadorobedece.
Nonossocaso,queremosperguntaraousuárioqualéoseunome,para
personalizarmossuaexperiência. Nãoéàtoaqueosjogosdehojeemdia
perguntamonome,nofimépossívellembrarquemfoiomelhorjogador,
criarumranketc. Nonossocasocome çaremospedindoonome,usando
novamenteo putsparacolocarumamensagemnasaídadocomputador:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
10
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 23

CasadoCódigo Capítulo3. Jogodaadivinha ção
Eoinverso?Queremosquenossoprogramaleiaumdado,pegue( get)
informaçãodousuário,aentradadedadosmaissimpleséfeitacomafun ção
gets,quedevolveumtexto,umvalorqueousuáriodigitou,juntocomo
enter(o return):
nome = gets
Imprimimosonomedamesmamaneiraqueimprimimosoutrasmensa-
gem:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "Começaremos o jogo para você, "
puts nome
Eapósexecutarmoscom ruby maior_ou_menor.rb temos:
Bem-vindo ao jogo da adivinhação
Qual é o seu nome?
Guilherme
Começaremos o jogo para você,
Guilherme
Quesaídahorrível.Vamossepararomomentoemqueonomefoilidodo
restodoprograma,quandonotificamosousuárioquecome çaremosojogo.
Primeirocolocamosalgumaslinhasembranco,istoé,nãoimprimimosnada,
somenteumaquebradelinha:
puts "Bem vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts
puts
puts
puts
puts
puts
puts "Começaremos o jogo para você, "
puts nome
11
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 24

3.1. Ojogo:entradaesaídabásica CasadoCódigo
Easaídaagoraficaumpoucomelhor:
Bem-vindo ao jogo da adivinhação
Qual é o seu nome?
Guilherme
Começaremos o jogo para você,
Guilherme
A saída ainda está feia, gostaríamos de jogar na tela a mensagem
Começaremos o jogo para você, Guilherme . Paraissoprecisamos
juntardoistextos,oprimeiroéo nome.Comofazerisso?Emlinguagensde
programaçãoemgeral,chamamosde Stringumvalorqueéumconjuntode
caracteres,comoumapalavra,umtexto,umaplacadecarroetc. Portanto,
queremosjuntarduas String,umadepoisdaoutra.Comofazerisso?Usare-
mosasomadeduas Strings,chamadade concatenação:
puts "Começaremos o jogo para você, " + nome
Ficandocomocódigofinal:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts
puts
puts
puts
puts
puts
puts "Começaremos o jogo para você, " + nome
Agorasimnossasaídaébonita:
12
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 25

CasadoCódigo Capítulo3. Jogodaadivinha ção
Bem-vindo ao jogo da adivinhação
Qual é o seu nome?
Guilherme
Começaremos o jogo para você, Guilherme
Desejamosescolherumnúmerosecreto.Nesteinstantedeixaremosum
númerofixoedepoisoalteraremosparaquecadavezonúmerotenhaum
valordiferente. Primeiro,imprimimosamensagemdeanúnciodosorteio,
algoquejáconhecemos:
puts "Escolhendo um número secreto entre 0 e 200..."
Depoisqueremosdefinirumnovovalor.Ovalor 175seránossonúmero
secreto,logofaloque numero_secretodevereceberovalor 175:
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
Ficamoscomoresultado:
Bem-vindo ao jogo da adivinhação
Qual é o seu nome?
Guilherme
Começaremos o jogo para você, Guilherme
Escolhendo um número secreto entre 0 e 200...
Escolhido... que tal adivinhar hoje nosso número secreto?
13
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 26

3.1. Ojogo:entradaesaídabásica CasadoCódigo
Precisamosagoraperguntarumnúmero,umchute,queousuáriodeseja
escolher.Jásabemosleressainforma ção,portantofazemos:
puts
puts
puts
puts
puts "Tentativa 1"
puts "Entre com o numero"
chute = gets
Masoquefazercomochute?Primeiroavisamosousuárioqueproces-
saremosseuchute,seráqueeleacertou? Novamente,éocódigocomque
estamoscome çandoanosacostumar: putspassando Stringseconcate-
nações:
puts
puts
puts
puts
puts "Tentativa 1"
puts "Entre com o numero"
chute = gets
puts "Será que acertou? Você chutou " + chute
Testamosnossoprograma,chutandoonúmero100:
Bem-vindo ao jogo da adivinhação
Qual é o seu nome?
Guilherme
Começaremos o jogo para você, Guilherme
Escolhendo um número secreto entre 0 e 200...
Escolhido... que tal adivinhar hoje nosso número secreto?
14
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 27

CasadoCódigo Capítulo3. Jogodaadivinha ção
Tentativa 1
Entre com o numero
100
Será que acertou? Você chutou 100
3.2 Será que acertou? O operador de compara -
ção ==
Estamosprontosparaverificarseousuárioacertououerrou.Como?Quere-
mosverificarseovalorchutadoéigualaonúmerosecreto.Qualosímbolo
matemáticoparaigualdade? Oigual, =. Masjáusamoso =antesparadi-
zerqueumvalorestavasendoutilizado.Comoentão::verificarseumvaloré
igualaoutro ? Usaremos o == . Será que o chute
Porexemplo,seráque175éiguala175?
puts 175 == 175
Levandoemconsidera çãoqueverdadeiroé trueeminglês,asaídaé:
true
Eseráqueeleéiguala174?
puts 175 == 175
puts 175 == 174
Levandoemconsidera çãoquefalsoé falseeminglês,asaídaé:
true
false
Istoé,ooperador ==realmentecomparaaigualdadeentredoisnúmeros.
Osvaloresverdadeiroefalsosãochamadosde booleanos.
Agorapodemosverificarseonúmerochutadoéiguala 175:
puts 175 == chute
15
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 28

3.2. Seráqueacertou?Ooperadordecompara ção== CasadoCódigo
Ficandocomoprograma:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts
puts
puts
puts
puts
puts
puts "Começaremos o jogo para você, " + nome
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
puts
puts
puts
puts
puts "Tentativa 1"
puts "Entre com o numero"
chute = gets
puts "Será que acertou? Você chutou " + chute
puts 175 == chute
Eeuerrei:
...
Tentativa 1
Entre com o numero
100
Será que acertou? Você chutou 100
false
Maseseeuchutar 175?
...
Tentativa 1
Entre com o numero
175
16
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 29

CasadoCódigo Capítulo3. Jogodaadivinha ção
Será que acertou? Você chutou 175
false
Oqueaconteceu? 175éiguala 175,comojásabíamos,maseleimprimiu
false.Acontecequeonúmero 175éigualaonúmero 175,verdade.Mas
lembraqueotextoqueousuárioentroucomoinforma ção,comoseuchute,é
umtexto?Otexto "175"nãoé“igualigual”aonúmero175.Sãoduascoisas
totalmentediferentes.Uméumtexto,outroéumnúmero.Antesmesmode
analisarseusvalores,elessãoduascoisasdetiposdiferentes,seustipossão
diferentes:uméuma String,ooutroéum Int(númerointeiro).
puts "175" == 175
puts "175" == "175"
puts 175 == 175
Comoresultado:
false
true
true
Queremosentãoconverternossochuteparaumnúmerointeiro( to an in-
teger),eadivinha?Existeummétodochamado to_iqueconvertea String
parauminteiro:
puts "175".to_i == 175
Resultandoem:
true
Masnaverdade175énosso numero_secreto,equeremoscompará-lo
como chuteportanto:
puts chute.to_i == numero_secreto
Terminandoaprimeirapartedenossojogocomocódigo:
17
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 30

3.3. Operadordeatribuiçãoevariáveis CasadoCódigo
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts
puts
puts
puts
puts
puts
puts "Começaremos o jogo para você, " + nome
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
puts
puts
puts
puts
puts "Tentativa 1"
puts "Entre com o numero"
chute = gets
puts "Será que acertou? Você chutou " + chute
puts 175 == chute.to_i
Agorasimnossojogodeumatentativafunciona,ouvocêacerta,ouvocê
erra. Antesdecontinuarmoscomasfuncionalidadesdojogoretomamoso
quejávimoseescrevemosparaentendermaisafundoosconceitosemelhorar
nossocódigo.
3.3 Operador de atribuição e v ariáveis
Vimosquepodemosutilizaro =paraatribuirumvaloraalgo.Porexemplo,
utilizamos nome = gets paralerdousuárioumtexto.Aessealgodamoso
nomedevariável.Nonossocaso,avariável nomerecebeovalorquefoilido
dojogador.
Nonossojogotemostrêsvariáveis:ochute,onúmerosecretoeonomedo
jogador.Cadavariávelpossuiumvalor.Onúmeroescolhidoestáfixocomo
175,enquantotantoonomedojogadorquantoochutesãovaloreslidosa
partirdaentradadousuário.
18
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 31

CasadoCódigo Capítulo3. Jogodaadivinha ção
3.4 Operadores de comparação
Comoosímbolo =foiutilizadopelalinguagemparaatribuirumvalorauma
variável,teremosqueadotaralgumoutrosímboloparaacompara çãodevalo-
res.O ==éopadrãomaiscomumadotadopelaslinguagensdeprograma ção
paratalsitua ção.Comovimosantes,ocódigoaseguirimprimeverdadeiroe
depoisfalso:
puts 175 == 175
puts 175 == 174
Masseráqueexistemoutroscomparadores? Outromuitocomuméo
diferente,istoé,não( !)igual( =),comonoexemploaseguir,queimprime
verdadeiroduasvezes:
puts 175 != 375
puts 175 != 174
Outrosoperadoresutilizadoscomumenteemopera çõesmatemáticassão
osdemaior( >),menor( <),maiorouigual( >=)oumenorouigual( <=).
Osexemplosaseguirtodosimprimemverdadeiro:
puts 175 > 174
puts 174 < 175
puts 170 >= 170
puts 175 >= 170
puts 170 <= 170
puts 170 <= 175
3.5 Entrada e saída
Aprendemosalerdoteclado(entrada, input)invocandoo gets,eaimprimir
resultadonasaídacomo puts.Entradaesaídasãovitaisparaumprograma
poissãoamaneirapadrãodeelesecomunicarcomomundoexterior.
Porenquanto,aleituraéfeitadoteclado(naverdade,daentradapadrão),
easaídaparaoconsole(naverdade,asaídapadrão).Nodecorrerdestema-
terialveremoscomolerdeeescreverparaumarquivo,porexemplo.
19
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 32

3.6. Oquesãofun ções CasadoCódigo
Nofuturoépossível,porexemplo,lerdaouenviarinforma çõesparaa
internet,lerdadosdeumjoystickousecomunicarcomumacaixadesomvia
bluetooth.Tudoissosãoentradaesaída:ojoystickéumaentradadedados,
umacaixadesoméumasaída.
3.6 O que são funções
Aolermoseescrevermosdadosutilizamosduaspalavrasimportantes: gets
e puts.Essasduaspalavrasnãosãomeraspalavras,sãoalgoquepodemos
chamar,invocar,pedirparaserexecutado.Sãofun ções.
Umafun çãopodereceberparâmetros,comonocasode puts:
puts "Bem-vindo ao jogo da adivinhação"
EmRuby,aoinvocarumafun ção,ousodosparênteseséopcionalem
muitassitua ções,ocasoaseguirmostraomesmocódigoagoracomparênte-
ses:
puts("Bem-vindo ao jogo da adivinhação")
DesenvolvedoresRubycostumaminvocarfun çõessemousodosparên-
teses,queéopadrãoqueseguiremossemprequeficarclarooqueestáacon-
tecendo.Assimcomonamatemática,oparênteseserveopcionalmentepara
deixarclarooqueestáacontecendoantesdoquê.
VimostambémqueemRubyépossívelterumafun çãocomparâmetro
opcional,queéoprópriocasode puts.Osexemplosaseguirtêmtodoso
mesmoresultado:aimpressãodeumalinhaembranco.
puts ""
puts
puts("")
puts()
Porfim,umafun çãoretornaalgumacoisa. Lembradafun çãodesoma
namatemática?Oqueelaretornava?Asomadedoisnúmeros.Eafun ção
demultiplica ção?Umvezesooutro.Oqueafun çãodepotênciaretornava?
Umnúmeromultiplicadodiversasvezesporelemesmo?Todafun çãoretorna
20
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 33

CasadoCódigo Capítulo3. Jogodaadivinha ção
algoemRubye,nocasode getseleretornaumalinhadeentradadousuá-
rio.Podemosfazeroquequisermoscomesseretorno,comoatribuí-loauma
variável:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "Começaremos o jogo para você, " + nome
Masoretornodeumafun çãojápodeserusadodiretoparainvocaroutra
função:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
puts "Começaremos o jogo para você, " + gets
Códigoestranho,né? Temosquetomarcuidadocomcódigoestranho.
Seestáestranhoparanós,paraquemlerestecódigodaquidoismeseses-
tarámaisestranhoainda.Porissomesmonãooescrevemos.Nossoobjetivo
comoprogramadoresnãoéescreverumcódigoindecifrável,éescreverum
códigoquefuncioneequepossaseralteradonofuturosemcriarbugs.Éisso
quebuscaremosnodecorrerdestematerial,aprenderjuntosaprogramare
escreverbonsprogramas.
3.7 Refatoração :\ n
Senossoobjetivoéescrevercódigomelhor,pareaqui,Guilherme.Vocêes-
creveuseis putssóparapularseislinhas,poxa.Verdade.Éhoradeparar,
olharparatrásemelhorarnossocódigo,oprocessoquechamamosdere-
fatorar. Queremosalterarnossasseislinhasde putsparaumcódigomais
simplesquealcanceomesmoresultado.
Oquequeremoséimprimirseislinhasembranco?Seriamuitolegalse
fossepossívelentãoescrever:
puts "proxima_linha,proxima_linha,proxima_linha,proxima_linha,
proxima_linha,proxima_linha"
21
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 34

3.8. Interpretadoroucompilador CasadoCódigo
Claro,Rubynãoentendeisso.Masexisteumasequênciamágica(não,não
émagia)quesignificauma novalinha, new line,asequência \n.Portanto,
podemossubstituirnossocódigopor:
puts "\n\n\n\n\n\n"
Oresultadoéomesmo.Seissofunciona,podemossubstituirtambémo
putsdequatrolinhasporquatro \ns. Maravilha,nossocódigoagorafica
maissimples:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
puts "\n\n\n\n"
puts "Tentativa 1"
puts "Entre com o numero"
chute = gets
puts "Será que acertou? Você chutou " + chute
puts 175 == chute.to_i
Refatoramosnossocódigo.
3.8 Interpretador ou compilador
Cadaarquiteturadecomputadoresistemaoperacionalpossuiumdetermi-
nadoconjuntodecomandos,umalinguagem,queeleentende. Algunsdos
sistemascompartilhamosmesmoscomandos,masmesmoassimsãocoman-
dosmuitobásicos,quepermitembasicamenteopera çõesmatemáticas(sim-
plesecomplexas),eteríamosqueimplementartodoumprogramaoujogo
comelessedesejássemosutilizarsualinguagem.Nãosóisso,énecessárioes-
creverparacadaumadasarquiteturasdemáquinaesistemaoperacional,um
trabalhoenorme.Escrevernessaslinguagensmaisbaixonível,maispróximas
dalinguagemdamáquina(códigodemáquina)é,portanto,raro.
22
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 35

CasadoCódigo Capítulo3. Jogodaadivinha ção
Napráticaexisteummercadomuitomaiorparadesenvolvedoresquees-
crevememumalinguagemdemaisaltonível,commenospreocupa çõestão
pequenas. Nessemundo,temosdoiscaminhosfamosos. Podemosescrever
nossoprogramaemformadetexto,comoviemosfazendoatéagora,erodar
outroprogramaquelêonossoetraduz,interpreta,emtemporealparaqueo
computadorexecuteoscomandosquedesejamos.
Nessesentido,temosqueinstalarprimeiroesseinterpretador,sendoque
existe uma versão dele para cada arquitetura e sistema operacional. Ao
mesmotemposomenteexistiráumaversãodonossocódigo. Esseéopro-
cessodeinterpreta ção,queaimplementa çãopadrãodalinguagemRubyuti-
liza.
Oupodemospedirparaumprogramatransformaronossotexto,escrito
umaúnicavez,nalinguagemdamáquina,oquegerariaumprogramaautos-
suficiente,executável.Elecompilaumprogramaparacadaconfigura çãode
máquinadesejada.Portantoessaoutraabordagem,deumcompilador,acaba
gerandodiversosarquivosexecutáveis.AlinguagemCéfamosaporsercom-
pilada.
Existemtambémlinguagenshíbridasediversasoutrasvaria ções.Alin-
guagemmaispróximaefamosadecódigodemáquina,masquenãoécódigo
demáquina,éo Assembly Language.
AlinguagemJavaéumexemplodevaria ção,éumalinguagemprimeiro
compilada(arquivos .class),depoisinterpretada( java virtual machine)e,
porfim,compiladaparacódigodemáquina( just in time developer).
OJRuby,uminterpretadordoRubybaseadoemJava,tambémsebaseia
namesmaabordagemhíbrida.
3.9 Resumindo
VimosatéagoracomocriarumprogramaemRuby,lidarcomentradaesaída
devariáveissimplescomonúmerosinteirose Strings,comparareconver-
ternúmerosinteiros,alémdeusarmosalgumasfun ções,invocarfun ções,en-
tendercomofuncionamoperadoresbásicosdecompara ção,edemosnosso
primeiropassoemdire çãoaumcódigomelhor,entendendooqueéare-
fatoração,oprocessodeconstantemelhoriaquepermeiaodiaadiadeum
23
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 36

3.9. Resumindo CasadoCódigo
desenvolvedor,sempredeumamaneiraanãoatrapalharsuaprodutividadee
qualidade.Vimostambémcomofuncionamosprocessosdeinterpreta çãoe
decompila çãodeumprograma.
24
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 37

Capítulo4
Controledefluxo
4.1 Mas e se... if e else
Escrevemosoiníciodenossojogo,ondeojogadorécapazdechutaruma
únicavezonúmeroentre0e200edizemosseeleacertouounão.Umjogo
basicamenteimpossíveldeseganhar.Maisaindaseaúnicainforma çãoque
damosé trueou false,quehorror.Primeirovamosmudaressamensagem
paradizeralgocomo Acertou!ou Errou!.
Istoé,trocamosalinhado puts 175 == chute.to_i porduaslinhas
queimprimemessasmensagens:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 38

4.1. Masese...ifeelse CasadoCódigo
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
puts "\n\n\n\n"
puts "Tentativa 1"
puts "Entre com o numero"
chute = gets
puts "Será que acertou? Você chutou " + chute
puts "Acertou!"
puts "Errou!"
Masagoraoprogramanãofazmaissentidonenhum:elesempreimprime
asduasmensagens!Queremosimprimiraprimeiramensagemsomentecaso
onosso numero_secretosejaigualaovalorchutado( chute.to_i).Esó
vamosimprimiramensagemdeerrodochutecasocontrário.Gostaríamos
defazeralgocomo:
se numero_secreto == chute.to_i
puts "Acertou!"
se não
puts "Errou!"
fim
Infelizmente,oRubynãotemaspalavras see se nãocomopalavra-chave
parafazeressecódigofuncionar. Maseletemalgomuitoparecido,o if,
else. Elesdois,juntocomo end,permitemdefinirdoisblocosdecódigo
queserãoexecutadossomenteseacondi çãoverificadaforverdadeira( if)
oufalsa( else),portantosealterarmosnossoprogramapara:
if numero_secreto == chute.to_i
puts "Acertou!"
else
puts "Errou!"
end
Rodamosnossojogoetemosoresultadoadequadoquandoerramos:
...
Tentativa 1
26
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 39

CasadoCódigo Capítulo4. Controledefluxo
Entre com o numero
160
Será que acertou? Você chutou 160
Errou!
If sem else: será?
Épossívelusaro ifsemo elsetambém. Asegundacondiçãoé
opcional,comoem:
if numero_secreto == chute.to_i
puts "Acertou!"
end
Semprequetemosum ifsem else,valeapenanosperguntarmos
oqueaconteceránocasocontrário. Queremosmesmoignoraraoutra
condição? Emnossoexemplo,não,eemmuitosexemplosdodiaadia
desejamosmostraralgumamensagemdeerro. Masexistemsitua ções
emqueénaturalusarmossomenteacondi ção if.Éimportantesempre
pensarepesarqualabordagemsedesejautilizar. Oexemploaseguir
mostraumasitua çãoemquenãoutilizaríamoso elsesemproblema
algum:
if numero_foi_muito_proximo
put "Quase lá! Está chegando bem perto!"
end
Sóquenossocódigoestámeiofeio,essalinhado ifestáfazendobastante
coisa,comparandoumnúmerocomovalordeumastringtransformadaem
inteiro. Quantacoisa! Paradeixarclarooqueestáacontecendo,vamosco-
mentarumalinhadenossocódigo:umcomentárioéumtextoqualquerque
seráignoradopelointerpretadordoRuby:
# Acertei ou não?
if numero_secreto == chute.to_i
puts "Acertou!"
27
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 40

4.2. Codesmell:comentários CasadoCódigo
else
puts "Errou!"
end
4.2 Code smell: comentários
Mascuidado: comentáriossãoindíciosdequenossocódigoestádifícilde
entender.Nesseinstantenossocódigoéatérazoável,masseexisteanecessi-
dadedecomentá-lopoisnãooentendemosdireito,éhoradefazermelhorias.
Éhoraderefatorá-lo.Jávimosumtipoderefatora çãoantes,agoraveremos
umnovo. Temosumacondi ção numero_secreto == chute.to_i . O
queelanosdiz? Seacerteiounão. Portanto,quetalextrairmosdaíoseu
valoremumanovavariável, extract variable:
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
else
puts "Errou!"
end
Olhacomonosso ifficoumuitomaisclaro.Olhandoagoraocódigore-
fatorado,ficamaisclaroqueonossocondicionaldeixavaascoisasumpouco
maiscomplexas.Nofim,temosotextoquedizexatamentequandoocódigo
seráexecutado...“ifacertou”,istoé,seacertou,imprimeAcertou!.
28
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 41

CasadoCódigo Capítulo4. Controledefluxo
Outros tipos de comentários
ExistemdiversostiposdecomentáriosemRuby.Omaisfamosoéo
deumalinha:
# meu nome
nome = "Guilherme"
Ouocomentáriodemúltiplaslinhas:
=begin
Meus dados pessoais, começando pelo nome,
passando até mesmo pela minha idade.
=end
nome = "Guilherme"
idade = 33
Masocomentáriodemúltiplaslinhasmaiscomuméousodopróprio
#emtodaselas:
# Meus dados pessoais, começando pelo nome,
# passando até mesmo pela minha idade.
nome = "Guilherme"
idade = 33
Existemaindaoutrasmaneirasdesecomentarcódigoemumarquivo,
masomaisimportanteélembrarque,seprecisacomentar,podeserque
preciserefatorar.Repenseseucódigo.
4.3 Condições aninhadas (nested ifs)
Masojogoaindaémuitodifícil.Queremosdeixá-lomaisfácildizendopara
ojogador,casoeleerre,seonúmeroémaioroumenordoqueonúmerochu-
tado.Jáconhecemosooperadordemenor( <)edemaior( >),eascondi ções
quepodemoscriarcom ifs,portantopodemosverificarseonúmeroémaior
edaramensagemdeacordo:
29
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 42

4.3. Condiçõesaninhadas(nestedifs) CasadoCódigo
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
Massóqueremosexecutaressecódigocasoojogadornãotenhaacertado:
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
Ojogofuncionaeaestruturaquecriamos,comum ifdentrodeoutro
iféchamadade nested if.Reparequeessetipodeestruturaéumsinal
delógicamaiscomplexa,afinalocódigoestáfazendodiversasverifica ções,
nãosóumacomofaziaantigamente.
A v ariável diferença
Quetalcriarumavariávelchamada diferenca?Algocomo:
diferenca = numero_secreto - chute.to_i
Poderíamosagoraverificarseadiferen çaézero(acertou),maior(o
númerosecretoémaior)oumenor(onúmerosecretoémenor)quezero.
Éumaabordagemválidamasaindamanteriaduasoutrêscondi çõesem
nossos ifs,portantonãoutilizaremosessaabordagemnesteinstante.
30
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 43

CasadoCódigo Capítulo4. Controledefluxo
4.4 Code smell: copy e paste
Mesmoassim,ojogocontinuamuitodifícil.Faltaumúltimopassoparaper-
mitirquenossojogadortenhaalgumachancedeganhar:temosquedaral-
gumaschances,algumasvidas,paraqueelepossatentar.Vamosdar3vidas,
3tentativas,portantofazemosum copy e pastedocódigodatentativa:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
puts "\n\n\n\n"
puts "Tentativa 1"
puts "Entre com o numero"
chute = gets
puts "Será que acertou? Você chutou " + chute
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
31
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 44

4.4. Codesmell:copyepaste CasadoCódigo
puts "\n\n\n\n"
puts "Tentativa 2"
puts "Entre com o numero"
chute = gets
puts "Será que acertou? Você chutou " + chute
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
puts "\n\n\n\n"
puts "Tentativa 3"
puts "Entre com o numero"
chute = gets
puts "Será que acertou? Você chutou " + chute
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
32
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 45

CasadoCódigo Capítulo4. Controledefluxo
Agorasim,jogoeacertonaterceiratentativa:
...
Tentativa 1
Entre com o numero
100
Será que acertou? Você chutou 100
O número secreto é maior!
...
Tentativa 2
Entre com o numero
180
Será que acertou? Você chutou 180
O número secreto é menor!
...
Tentativa 3
Entre com o numero
175
Será que acertou? Você chutou 175
Acertou!
Ojogofuncionaejátemumacertagra ça,poisédesafiadoracertarem
trêstentativas.Masagoraquerocorrigiramensagemdeentradadonúmero,
reparequeesquecidecolocaracentoem número.Quehorror!Tenhoquemu-
darocódigoemtrêslugaresdiferentespoiseufiz copy e paste.Sim,veremos
comomelhoraressecódigoparadarandamentoemnossojogo!
4.5 O laço for (loop)
Nossojogoatualpodedivertirporalgunsminutosmasémuitofácilperceber
queserádifícildemanterseucódigoàmedidaqueoevoluímos. Copy e pasteé
umadaspráticasmaisnocivasaumcódigoeabusamosdeleaquidepropósito.
Queremosexecutaromesmopeda çodecódigotrêsvezeseparaissonoslevei
aocaminhodomal,do copy e pastesempensar.Éhoraderefatorar.
Comoseriabompoderdizerparaointerpretadoralgocomo:
execute 3 vezes
puts "\n\n\n\n"
33
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 46

4.5. Olaçofor(loop) CasadoCódigo
puts "Tentativa 1"
puts "Entre com o numero"
chute = gets
puts "Será que acertou? Você chutou " + chute
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
end
Notequejáadicioneium endparadizerparaointerpretadorondenosso
códigoaserexecutadodiversasvezestermina.
Masalinguagemnãosabeoquesignifica 3 vezes.Oqueelaconhecesão
variáveis,númerosetc. Comorepresentar3vezesemnúmeros? Damesma
maneiraqueumacrian çarepresentaostrêsnúmeros:1,2e3!ImagineJulieta,
doisaninhos,paraquempedimos“porfavor,conteatétrês”.Eelaconta:1,
2e 3.Oqueelafez?
Elacriouumavariávelchamadadedos,ecolocouonúmeroumláden-
tro. Depoisonúmerodoisnavariáveldedos,depoisonúmerotrês. Pode-
mosmandarocomputadorfazeramesmacoisa,crieumavariávelchamada
dedoseexecuteocódigoaseguirparatodososnúmerosinteirosentre1e3:
rode para dedos em 1 ate 3
# código a ser executado
end
Estamosquaselá.Novamente,Rubynãofalaportuguêstãobemquanto
aJulieta,portantotraduzimosparaalinguagemdele, 1 até 3 vira 1..3,
enquanto rode para vira fore emvira in:
34
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 47

CasadoCódigo Capítulo4. Controledefluxo
for dedos in 1..3
# codigo a ser executado
end
Podemostestarcomumamensagemdeimpressãosimples:
puts "Vou contar de 1 até 3"
for dedos in 1..3
puts "Contando"
end
Resultandoem:
Vou contar de 1 até 3
Contando
Contando
Contando
Sófaltoucontardeverdade,istoé,faltouimprimirmosonúmeroque
estamoscontando. Dentrodocódigoaserexecutadodiversasvezestemos
acessoàvariávelchamada dedos,queéovalorqueestamospassandoagora:
puts "Vou contar de 1 até 3"
for dedos in 1..3
puts "Contando: " + dedos
end
Masaorodar,percebemosquetemosumerrodeexecu ção,algoligadoa
nãoserpossívelconverterumnúmeroemuma String:
TypeError: no implicit conversion of Fixnum into String
Claro,nãofazsentidosomarumtextocomumnúmero.Fazsentidocon-
catenarduas Strings,ousomardoisnúmeros. Masumnúmeroeuma
StringnãopodemserconcatenadosnemsomadosemRuby.Vamoscon-
verternossonúmerointeiroemuma Stringinvocandoseumétodoque
transformaem String,o to_s:
35
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 48

4.6. Aplicandoolaço foraonossoprograma CasadoCódigo
puts "Vou contar de 1 até 3"
for dedos in 1..3
puts "Contando: " + dedos.to_s
end
Resultandoem:
Vou contar de 1 até 3
Contando: 1
Contando: 2
Contando: 3
4.6 A plicando o laço for ao nosso programa
Pronto!Oquetemosaquiéumtrechodecódigoqueserárepetidodiversas
vezes.Um loop,um laçoqueexecutanossocódigotrêsvezes.O foréumdos
diversostiposde loopquepodemosfazereaindaveremosoutrasmaneiras
maisàfrente.
Agoraqueremostrazernossola çoparaocódigoemquefizemos copy e
paste.Queremosnoslivrardasujeira,executandoomesmotrechotrêsvezes.
Paraissocriamosumla çocujavariável tentativavaleentre 1e 3:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
for tentativa in 1..3
puts "\n\n\n\n"
puts "Tentativa 1"
puts "Entre com o numero"
chute = gets
36
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 49

CasadoCódigo Capítulo4. Controledefluxo
puts "Será que acertou? Você chutou " + chute
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
end
Agora nosso programa roda três vezes. Mas sempre imprime
Tentativa 1. Corrigimosparamostraratentativacertajuntocomoto-
taldetentativas:
# ...
for tentativa in 1..3
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de 3"
puts "Entre com o numero"
chute = gets
puts "Será que acertou? Você chutou " + chute
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
37
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 50

4.7. Codesmell:Magicnumbers CasadoCódigo
end
end
end
Nossojogocontinuafuncionandocomoantes,masjásabemosqueébem
maisfácilmantê-loagora. Podemoscorrigiramensagemdo numerosem
acentotrocandoumúnicopontodoprograma,poisnãotemosmaiso copy e
paste
puts "Entre com o número"
Mas3tentativasparecesermuitopoucoparaacertar.Queremosmudar
para5.Alteramosnonossola ço:
for tentativa in 1..5
Erodamos.Pormaisqueojogomedêcincotentativas,eleimprime:
...
Tentativa 1 de 3
...
Tentativa 2 de 3
...
Tentativa 3 de 3
...
Tentativa 4 de 3
...
Tentativa 5 de 3
...
Quehorror.Ondeerrei?
4.7 Code smell:M agic numbers
Reparequeonúmero 3apareceuduasvezesemnossocódigo.Tantonola ço
quantonaimpressãodamensagemdequaleraatentativaatual. Oquehá
deerradonisso? Primeiro,nossonúmeroestáduplicado. Antesvimosum
exemplode copy e pastedeumgrandetrechodecódigo,epercebemosque
mudarumpontoseriatrabalhosopoisteríamosquemudartodos.
38
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 51

CasadoCódigo Capítulo4. Controledefluxo
Masreparequemesmoquandotemosumsimplesnúmerorepetidoem
duaspartesdomeuprogramaémuitofácilesquecerqueeleexiste.Também
seriainviávelprocurartodasaspartesdetodososmeusarquivosondeonú-
mero 3aparece.Elequerdizermuitascoisas,ejustamenteporissoeleéum
númeromágicojogadonomeuprograma: ninguémsabeoqueeleé,eele
aparecejogadoemdiversoslugares.
4.8 Refatoração : extrair v ariável
Oquefaremosédarumnomeaessenúmero.Vamoscriarumavariávelque
sechama limite_de_tentativas:
limite_de_tentativas = 3
Efetuamosarefatora çãode extract variableeaextraímos. Agoranosso
númeronãoémaismágico,eleémuitobemdefinidoeestáclaroparatodos
oquesignifica.
Apósextrairavariável,refatoramosquemacessavaessevalor(nocaso,
mágico)esubstituímosporumareferênciaàvariávelquedescreveseuvalor:
for tentativa in 1..limite_de_tentativas
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de " +
limite_de_tentativas.to_s
Pronto!Agorabastamudarolimitepara 5:
# ...
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
# ...
end
4.9 Q uebrando o laço com o break
Ótimo!Paraterminarmosnossaprimeiraversãodojogo,temosquecorrigir
umúnicobug,nossoprimeirobugdetectadopelojogador.Seeleacertarde
39
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 52

4.9. Quebrandoolaçocomobreak CasadoCódigo
primeiraonúmero 175,ojogocontinuaperguntando,feitobobo.Aindanão
dá.Queremosalterarnossojogopara,casoousuárioacerte,elesaiaforado
laço,ele quebre(break)onossola ço( loop).
Algocomo:
if acertou
puts "Acertou!"
quebra
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
Adivinha,oRubypossuiumapalavra-chavechamada breakquequebra
ola çoatual,saindodelecompletamente!Fazendoaaltera çãoaseguir,ojogo
terminalindamentemesmoqueojogadoracertedeprimeira:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de " +
limite_de_tentativas.to_s
puts "Entre com o número"
chute = gets
puts "Será que acertou? Você chutou " + chute
40
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 53

CasadoCódigo Capítulo4. Controledefluxo
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
break
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
end
Comoresultado:
...
Tentativa 1 de 5
Entre com o número
175
Será que acertou? Você chutou 175
Acertou!
4.10 Resumindo
Vimos neste capítulo como funciona o operador+, que é válido en-
tre Strings, quando executa uma operação de concatenação, e entre
números, ao executar uma soma. Aprendemos a converter um número
inteiro em String, executar código condicionalmente com o uso do
if...else...end,autiliza çãoeopepinodeseusar ifsaninhados,como
funcionae(novamente)omalcheiroqueumcomentárioindica,arefatora-
çãodeextrairvariável,ocontroledefluxoatravésdeumla ço,permitindoa
execuçãorepetidadeumtrechodecódigo,alémdecomoquebraressela çoa
qualquerinstantecomousodo break.Nossojogojánosdesafiaaacertar
umnúmeroentre0e200(podetestar,édifícilalguémacertaremtãopoucas
41
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 54

4.10. Resumindo CasadoCódigo
tentativas).Nossopróximopassoémelhorarbastanteessenossocódigoantes
deadicionardiversasnovasfuncionalidades.
42
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 55

Capítulo5
Funções
5.1 Funções
Somoscapazesdejogarcomummínimodediversão,masantesdecontinu-
armoscomasfuncionalidadesavan çadas,queremostercertezadequeoutro
desenvolvedorserácapazdecontribuircomnossoprojeto.
Nomundomodernoémuitocomumqueprojetossejamdesenvolvidos
pormaisdeumprogramador,sejadentrodeumapequenaougrandeem-
presa,ouaindanoscasosdeprojetosdecódigoaberto,nosquais,atravésde
plataformascomooGithubetecnologiascomooGit,desenvolvedoresdo
mundointeirocontribuemcomosmaisvariadosprojetos,desdeocoredo
linuxatéointerpretadorpadrãodalinguagemRubyemsi.
Sendoassim,vamosdarumaolhadanovamenteemnossocódigo.Oque
maismechamaaaten çãoéquetemosumúnicoarquivocommaisdetrinta
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 56

5.1. Funções CasadoCódigo
linhasequefaztudolámesmo,semrédeas,nemlimites.Infelizmenteéco-
mumencontrarcódigocomoessenomundoselvagem,masparanós,bons
programadores,tudo(oumuitacoisa)emumúnicolugaréum code smellque
queremosaospoucoscombater.
Comecemospeloiníciodocódigo,ondepedimosonomedousuário:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
limite_de_tentativas = 5
# ...
Nessetrechodecódigopedimostalinforma çãoeimprimimosamensa-
gemdeboas-vindas,issoé,damosinícioaojogocomoumtodo:
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
Masumnovodesenvolvedortemqueolharessecódigolinhaalinhapara
entenderoqueeleestáfazendo.Dequemaneirapoderíamosdeixarissomais
claro?Comumcomentário,comoem:
# dá boas-vindas
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
puts "Escolhendo um número secreto entre 0 e 200..."
44
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 57

CasadoCódigo Capítulo5. Funções
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
limite_de_tentativas = 5
# ...
Masjávimosanteriormentequeumcomentárioéumcheirofétidonocó-
digo( code smell),oquefazer?Queremosextrairessecódigo.Diferentemente
doquefizemosantes,umpeda çodecódigonãoéummerovalor,comoum
númeroouuma String,eleéalgoaserexecutado,eessadiferen çaéimpor-
tante.Tantoumpeda çodecódigo,umcomportamento,podeterumnome
quantoumvalorpodeterumnome.Massomenteumpeda çodecódigopode
serexecutado,invocado.
Qualamaneirapadrãodeextrairumcódigoparapoderinvocá-lo?Pri-
meiro,substituímosnossocódigopeloquedesejamosescrever,chamar,in-
vocar:
da_boas_vindas
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
limite_de_tentativas = 5
# ...
Agora precisamos definir (define, abreviado def) o significado de
da_boas_vindas,portanto:
def da_boas_vindas
end
E dizemos o que será executado quando alguém chama, invoca, o
da_boas_vindas:
def da_boas_vindas
puts "Bem-vindo ao jogo da adivinhação"
45
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 58

5.2. Boaprática:encapsulamentodecomportamento CasadoCódigo
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
end
Oquecriamos?Umafun ção( function),queéumtrechodecódigoque
podeserexecutadoquantasvezesdesejarmos,bastandoparaissoinvocá-lo
(ouchamá-lo)atravésdeseunome.Umafun çãoépe çafundamentaldere-
aproveitamentodecódigoeserápartedoseudiaadiadeprogramador.Em
Ruby,amaneirapadrãoeusualdedefinirumafun çãoéatravésdaconstru ção
def ... end einvocá-laatravésdeseunome.Reparequeanomenclatura
segueopadrãocom underlineparasepararpalavras.
5.2 Boa prática : encapsulamento de comporta -
mento
Reparequeagoraumdesenvolvedornovoécapazdeentenderoquesignifica
da_boas_vindassemterqueolharocódigointeiro:opróprionomediz
tudo!Eledáboas-vindasaojogador.Aochamar da_boas_vindastambém
nãoénecessárioentendercomoéfeitooesquemadeboas-vindas,simples-
mentebastachamar,dizer,invocar da_boas_vindas,semsepreocuparem
comoocomportamentoéfeito,massomentecomainterface,ouseja,como
queelefaz,nãocomo.
def da_boas_vindas
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
end
da_boas_vindas
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número secreto?"
46
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 59

CasadoCódigo Capítulo5. Funções
# ...
Escondemoscomoocomportamentoéexecutado,somentemostramoso
queéfeitoatravésdonomedanossafun ção.Esseprocessodeescondercomo
ascoisassãofeitas,apenasdeixandodisponívelumainterfacequeindicao
queseráfeitoeoqueénecessárioparaqueelesejaexecutado,échamadode
encapsulamento,algomuitobemrecebidoporbonsprogramadores.Elefaci-
litaamanuten çãodonossocódigoemlongoprazoaopermitircompreender
maisfacilmentetrechosisolados,alémdeoutrasvantagensqueveremoscom
opassardotempoetiposdiferentesdeencapsulamento.
5.3 Escopo de v ariáveis
Assimcomoextraímosocódigoreferenteàsboas-vindas,desejamosfazero
mesmocomocódigoquesorteiaonúmerosecreto.Repetimosoprocessode
definirafun ção:
def sorteia_numero_secreto
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
end
Epassamosainvocá-la:
da_boas_vindas
sorteia_numero_secreto
limite_de_tentativas = 5
# ...
Oqueacontece?Ocódigoparadefuncionar!Onúmerosorteadonãoé
mais175?
...
Tentativa 1 de 5
47
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 60

5.3. Escopodevariáveis CasadoCódigo
Entre com o número
175
Será que acertou? Você chutou 175
maior_ou_menor.rb:26:in ` block in <main>':
undefined local variable or method ` numero_secreto'
for main:Object (NameError)
from maior_ou_menor.rb:19:in ` each'
from maior_ou_menor.rb:19:in ` <main>'
Notequeamensagemdeerroemtempodeexecu çãodointerpretadorem
Rubynosdizexatamentequalerroaconteceuemquallinhadecódigo.Lendo
debaixoparacima,alinha19denossoarquivo maior_ou_menor.rbexecutou
um each(nosso for),quandoderepente,nalinha26,ocódigotentouacessar
umavariávellocaloumétodoindefinido,o numero_secreto.Comoassim
indefinido?
Antigamentehavíamosutilizadoumavariávelquefoidefinidanopro-
gramacomoumtodo,nãoemumescopoespecífico.Elaeradefinidalogode
caranoprograma,etodooprogramapodiaacessá-la,elaeraabertaatodos.
Agoranãofazemosmaisassim.Nossavariávelédefinidadentrodeumbloco,
nocaso,dentrodenossafun ção:
def sorteia_numero_secreto
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
end
Umavariáveldefinidadentrodeumafun ção(porenquanto)sóévisível
dentrodesseespa ço,eesseespa çoéchamadodeescopo( scope)davariável.
Variáveisdessetiposãochamadasvariáveislocais,quesãomuitoboas,pois
nospermitemcontrolarquempodeequemnãopodeacessá-las.
48
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 61

CasadoCódigo Capítulo5. Funções
5.4 Code smell: v ariáveis sem controle de es -
copo e v ariáveis globais
Variáveisglobaissãoocúmulo,omáximo,dodescontrole. Opensamento
costumaserassim:hojeacreditamosquesóprecisamosdeumadela.Seama-
nhãprecisamosdeduas,nãodámais,temosquealterartodoonossocódigo.
Seescrevemosumabibliotecaqueoutrosdesenvolvedoresvãousar,minhas
variáveisglobaispodemteromesmonomequeasdeles,ou,piorainda,seeu
mudaronomedeminhavariável(oufun ção,ouqualquercoisa)global,que-
broacompatibilidadecomtodososmeusclientes.Comoregrageral,quanto
maiscoisaglobal,pior.
Sãofamososeinúmerososcasosdequebradecompatibilidadeentrever-
sõesoudeincompatibilidadeentrebibliotecasdevidoaoabusodeelementos
globais.
EmRuby,avariáveldefinida“voando”nãoéglobalaopédaletra.Elapode
seracessadaporqualqueroutrocódigo“voando”,quenãoestáexplicitamente
dentrodenenhumaoutrafun ção,masdequalquermaneiravariáveisdefini-
dasassimtêmseucontroledeescopo,digamos,descontrolado.Naprática,ao
utilizá-lasnãohácontroledeescopo.Evite-as.
Usando v ariáveis globais
Comoreferência,variáveisrealmenteglobais(eaítambémmorao
perigo)sãodefinidascom $nafrente,comonoexemploaseguir,onde
qualquerumpodeacessar,comencapsulamentoecontrolezero:
$nome = "Guilherme"
Noexemploaseguirtemosavariáveltradicionaldeclaradaforade
qualquerfun ção,“voando”.
nome = "Guilherme"
Quandoqualquerum“foradeumafunção”podeacessarumavariá-
vel,oencapsulamentoéquasezero,eocontrolesobreseucódigotam-
bém.
49
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 62

5.5. Retornodefunção CasadoCódigo
5.5 Retorno de função
Masentãocomofazercomquenossafun çãodevolvaonúmerosecretoesco-
lhido?Queremosqueelaretornedizendoalgo,queretorneumvalor.Seela
vairetornarumvalor, returnnela:
def sorteia_numero_secreto
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
return numero_secreto
end
Esevamosinvocá-la,podemosatribuirseuretornoaumanovavariável:
da_boas_vindas
numero_secreto = sorteia_numero_secreto
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de " +
limite_de_tentativas.to_s
puts "Entre com o número"
chute = gets
puts "Será que acertou? Você chutou " + chute
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
break
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
50
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 63

CasadoCódigo Capítulo5. Funções
end
end
Pronto!Nossocódigovoltaafuncionar.Masfiqueatento:avariávello-
calqueexistiaduranteachamadadafun ção sorteia_numero_secreto
édiferentedaquefoicriadadepois,apesardeteremomesmovalor,claro.
Podemosdeixarissoclaromudandoonomedavariáveldafun ção:
def sorteia_numero_secreto
puts "Escolhendo um número secreto entre 0 e 200..."
sorteado = 175
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
return sorteado
end
NotequeemRubyoretornodaexpressãodaúltimalinhadecódigosem-
preéretornadoporumafun ção.Porissoémuitocomumqueosprograma-
doresRubynãoescrevamapalavra returnnaúltimalinhadeumafun ção,
ficandosomente:
def sorteia_numero_secreto
puts "Escolhendo um número secreto entre 0 e 200..."
sorteado = 175
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
sorteado
end
5.6 Variáveis locais
Faltamagoramaisdoispassosparaterminarmosdeextrairtodasasfun ções
quequeremos.Desejamosextrairocódigodeperguntaronúmeroparanosso
jogador,eoqueverificaseeleganhou.Come çamoscomoquecolocaemprá-
ticaoconhecimentodefun çõesqueadquirimosatéagora:extrairapergunta,
queéonossocódigoaseguir:
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de " +
51
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 64

5.6. Variáveislocais CasadoCódigo
limite_de_tentativas.to_s
puts "Entre com o número"
chute = gets
puts "Será que acertou? Você chutou #{chute}"
Qualonomequedaremosaessecódigo? Comoele pede um número
paraousuário,vamoschamá-lode pede_um_numero. Jásabemosqueo
códigoprecisaráretornaronúmeroquefoipedido,afinaleleseráutilizado
embreveparaverificarseojogadoracertououerrou,portantoextraímoso
códigojuntocomoretornonafun ção pede_um_numero:
def pede_um_numero
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de " +
limite_de_tentativas.to_s
puts "Entre com o número"
chute = gets
puts "Será que acertou? Você chutou " + chute
chute
end
Agoranossocódigodoloopprincipaldojogofica:
da_boas_vindas
numero_secreto = sorteia_numero_secreto
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero
acertou = numero_secreto == chute.to_i
if acertou
puts "Acertou!"
break
else
maior = numero_secreto > chute.to_i
if maior
puts "O número secreto é maior!"
52
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 65

CasadoCódigo Capítulo5. Funções
else
puts "O número secreto é menor!"
end
end
end
Mesmoassimaindatemalgodeestranhocomochute.Elesempreéuti-
lizadocomo .to_i.Istoé,oloopprincipaléinvejoso,elequersemprefazer
algoquequemsabefazeréonúmero,transformaruma Stringemnúmero.
Nãoqueremosuma String,enemautilizamos,estamossempretransfor-
mandoemnúmero. Atéonomedafun çãodizisso: pede_um_numero,e
estranhamenteeladevolveuma String.Vamoscorrigiressapossívelfonte
debugsagoramesmo,retornandoonúmero:
def pede_um_numero
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de " +
limite_de_tentativas.to_s
puts "Entre com o número"
chute = gets
puts "Será que acertou? Você chutou " + chute
chute.to_i
end
Eagorautilizaronúmerojáeducadamente:
da_boas_vindas
numero_secreto = sorteia_numero_secreto
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero
acertou = numero_secreto == chute
if acertou
puts "Acertou!"
break
else
53
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 66

5.6. Variáveislocais CasadoCódigo
maior = numero_secreto > chute
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
end
Tentamosrodaraaplica çãoerecebemosumerronovo:
maior_ou_menor.rb:18:in ` pede_um_numero':
undefined local variable or method ` tentativa'
for main:Object (NameError)
from maior_ou_menor.rb:30:in ` block in <main>'
from maior_ou_menor.rb:29:in ` each'
from maior_ou_menor.rb:29:in ` <main>'
Jávimosalgoparecidocom variável local ou método não definidoanterior-
mente.Tentávamosusarumavariávelquesóeravisívelemoutroescopo.Será
queéissoqueocorreaquinovamente? undefined local variable cos-
tumaseroqueelemesmodiz:nãoexistealgocomessenomenesteescopo.
Acompanhemosalinhaondeocorreuoerro: linha29efetuouo for
(each)equandochegounalinha30,invocouafun ção pede_um_numeroque
chegouatéalinha18,ondenãoencontrouninguémchamado tentativa.
Minhalinha18éondetentamosacessara tentativaem:
def pede_um_numero
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de " +
limite_de_tentativas.to_s
puts "Entre com o número"
chute = gets
puts "Será que acertou? Você chutou #{chute}"
chute.to_i
end
Realmente,avariávelnãofoidefinidaaquidentro!Elafoidefinidaden-
trodonossola ço for.Todavezquecome çamosumnovoescopo,oescopo
54
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 67

CasadoCódigo Capítulo5. Funções
dasvariáveisémodificado,podendoounãoteracessoàsvariáveisqueesta-
vamdisponíveisantesdainvoca ção.Porexemplo,quandoefetuamosnosso
for,continuamospodendoacessarasvariáveisdeforado fornormalmente.
Masaoinvocarmosumafun çãodefinidacomofizemosatéaqui,nãotemos
acessoàsvariáveisqueforamdeclaradasantesdachamadadafun ção. Isso
querdizerquetemosumproblema.Comoacessarasvariáveis tentativa
e limite_de_tentativasdequeprecisamos?
Lembradoencapsulamento?Éelequenosdáopoderdeacessarsomente
oqueénecessário,evitandoumcódigomacarrônico,umamisturaquefaz
tudodetudoqueéjeito.Aoencapsularmosessecomportamentodepedirum
númerosurgiuanecessidadedeacessarmosdoisvalores,nadamaisnatural
ejustoquepassemosessesdoisvaloresparaafun ção pede_um_numero,
fazemosessapassagematravésdedoisargumentos,doisparâmetros:
def pede_um_numero(tentativa, limite_de_tentativas)
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de " +
limite_de_tentativas.to_s
puts "Entre com o número"
chute = gets
puts "Será que acertou? Você chutou #{chute}"
chute.to_i
end
Invocamosafun çãopassandoosdoisvalores:
da_boas_vindas
numero_secreto = sorteia_numero_secreto
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero(tentativa, limite_de_tentativas)
# ...
end
Agorasimnossoprogramavoltaafuncionar.Reparequeasfun çõessão
umprimeirorecursobásicodeencapsulamentoquenospermiteesconder
55
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 68

5.7. Extraindomaisumafunção CasadoCódigo
ocomportamento,recebendocomoparâmetrosoqueénecessárioedevol-
vendocomoretornooresultadodaexecu çãodocódigo.
Propositalmenteisolamosnossocódigodemaneiraqueasfun çõestives-
semumagranularidade,umtamanhoeumaquantidadedelógicapequenos.
Funçõesgrandesecomplexaspodemsersemprequebradasempeda çosme-
nores,possivelmentemaisfáceisdeseremcompreendidos.
5.7 Extraindo mais uma função
Agorafaltasómaisumpasso:extrairocódigo,alógicadenegóciosedesaída
paraousuário,queverificaseojogadoracertou:
acertou = numero_secreto == chute
if acertou
puts "Acertou!"
break
else
maior = numero_secreto > chute
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
Oqueessecódigofaz? Ele verifica se acertou,portantocriaremosuma
função verifica_se_acertou.Notequeelaprecisasaberqualonúmero
secretoequalochutedojogador,logoreceberemososdoiscomoparâmetro:
def verifica_se_acertou(numero_secreto, chute)
acertou = numero_secreto == chute
if acertou
puts "Acertou!"
break
else
maior = numero_secreto > chute
if maior
56
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 69

CasadoCódigo Capítulo5. Funções
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
end
end
Vamosinvocá-lanonossoloopprincipal:
da_boas_vindas
numero_secreto = sorteia_numero_secreto
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero(tentativa, limite_de_tentativas)
verifica_se_acertou(numero_secreto, chute)
end
Tentamosrodareocódigonemcome çaaserrodado.ORubyparou,mas
nãofoiumerrodeexecu ção.Ointerpretadornãoconseguiunemlernosso
arquivo rb.Issopoisnossaestruturaestáinválidaagora,temosumerrode
“compilação”,umerroemnossasintaxe:
maior_ou_menor.rb:29: Invalid break
maior_ou_menor.rb: compile error (SyntaxError)
Nalinha29tentamosexecutaro breakdentrodeumafun ção,oquenão
temproblema.Maslembre-sequeo breakquebraoloopmaispróximo,equal
oloopqueestáocorrendonaquelafun ção? Nenhum. Entendo,vocêcomo
serhumanosabequeumoutropontodoprograma(nossoloopprincipal)
invocaráaquelafun ção,queentãoteráum break. Masointerpretadornão
temcomosaberisso.Piorainda,podeserqueumprogramadordesavisado
invoquetalfun çãosemestardentrodeumloop. Éporissomesmoquea
sintaxedalinguagemnãopermiteum breaksolto,voltando.O breaksópode
existirseháumloopvisívelnoescopoatual,quenãoéocaso. Masentão
comofalarparaonossola çoterminar?
Seafun çãoverificaseacertou,parecenaturaleladizersesimousenão.
Fazemos:
57
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 70

5.7. Extraindomaisumafunção CasadoCódigo
def verifica_se_acertou(numero_secreto, chute)
acertou = numero_secreto == chute
if acertou
puts "Acertou!"
return true
else
maior = numero_secreto > chute
if maior
puts "O número secreto é maior!"
return false
else
puts "O número secreto é menor!"
return false
end
end
end
Agoraaoinvocarafun çãopodemosquebrarnosso loop:
da_boas_vindas
numero_secreto = sorteia_numero_secreto
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero(tentativa, limite_de_tentativas)
if verifica_se_acertou(numero_secreto, chute)
break
end
end
Pronto! Nossojogovoltouafuncionar. Umaúltimarefatora çãodeboa
práticadecódigoenvolvemudarnossos ifs:
def verifica_se_acertou(numero_secreto, chute)
acertou = numero_secreto == chute
if acertou
puts "Acertou!"
return true
else
maior = numero_secreto > chute
58
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 71

CasadoCódigo Capítulo5. Funções
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
return false
end
end
5.8 Boa prática : early return
Repareque,casoousuáriotenhaacertado,nóssaímosdafun çãologodecara.
Issosechamadesaída cedo(early return). Sesaímosdafun ção,podemos
jogartodoocódigodoerroparaforado if:
def verifica_se_acertou(numero_secreto, chute)
acertou = numero_secreto == chute
if acertou
puts "Acertou!"
return true
end
maior = numero_secreto > chute
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
return false
end
Comooretornodefalsoestánaúltimalinha,podemosomitirapalavra
return:
def verifica_se_acertou(numero_secreto, chute)
acertou = numero_secreto == chute
if acertou
puts "Acertou!"
return true
end
59
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 72

5.9. Pequenasrefatoraçõesespecíficasdalinguagem CasadoCódigo
maior = numero_secreto > chute
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
false
end
5.9 Pequenas refatorações específicas da lin -
guagem
Pronto,nãohámaisrefatora çõesquegostaríamosdefazernesseinstanteque
são,emgeral,universaiseindependentesdelinguagem. Masexisteumas-
pectodalinguagemqueosprogramadoresRubyemgeralpreferem. Opri-
meiroenvolveainvoca çãodefun ções. Lembraqueaoinvocaro putso
parênteseseraopcional?Nonossocasotambém,portantomudamosnosso
códigopara:
da_boas_vindas
numero_secreto = sorteia_numero_secreto
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero tentativa, limite_de_tentativas
if verifica_se_acertou numero_secreto, chute
break
end
end
Outracaracterísticadalinguagembastanteutilizadapordesenvolvedores
Rubyenvolveanossacondi çãodequebradola ço. Quandotemossomente
umainstru çãodecódigoaserexecutadoemum ifécomumqueosprogra-
madoresfa çam:
break if verifica_se_acertou numero_secreto, chute
Emvezde:
60
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 73

CasadoCódigo Capítulo5. Funções
if verifica_se_acertou numero_secreto, chute
break
end
ApesardeseropadrãodosprogramadoresRuby,nessecasoespecífico
deixareiaversãotradicional,com if ... end ,queacreditosermaiscom-
preensívelparanósprogramadoresnesseinstantedenossacarreira.
5.10 Resumindo: o poder da extração de código
Nossocódigofinalécompostoagoraporquatrofun çõesindependentes,que
podemserentendidasporqualquerdesenvolvedorisoladamente.Seusnomes
tambémdizembastantesobreoquefazem.Ocódigoaseguirdáboas-vindas:
def da_boas_vindas
puts "Bem vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, " + nome
end
Podemosaqualquerinstantesortearumnovonúmerosecreto:
def sorteia_numero_secreto
puts "Escolhendo um número secreto entre 0 e 200..."
sorteado = 175
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
sorteado
end
Oupedirumnúmeroparaojogador:
def pede_um_numero(tentativa, limite_de_tentativas)
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de " +
limite_de_tentativas.to_s
puts "Entre com o número"
61
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 74

5.11. Resumindo CasadoCódigo
chute = gets
puts "Será que acertou? Você chutou " + chute
chute.to_i
end
Podemostambémverificarseeleacertououerrouochute:
def verifica_se_acertou(numero_secreto, chute)
acertou = numero_secreto == chute
if acertou
puts "Acertou!"
return true
end
maior = numero_secreto > chute
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
false
end
Porfim,nossocódigodola çoprincipalécompostodetodosessescom-
portamentos:
da_boas_vindas
numero_secreto = sorteia_numero_secreto
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero tentativa, limite_de_tentativas
if verifica_se_acertou numero_secreto, chute
break
end
end
5.11 Resumindo
Aprendemoscomocriarnossasfun ções,encapsulandopartedocomporta-
mento,dalógicadeumatarefa. Entendemosmelhorcomofuncionaoes-
62
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 75

CasadoCódigo Capítulo5. Funções
copodevariáveis: aquelasdefinidasdentrodeumafun çãosãolocaisaela.
Vimostambémquevariáveissemcontroledeescoposãoasquedefinimos
abertamenteemnossocódigoequepodemostambémcriarvariáveisglobais,
fáceisdeseremacessadasmasperigosasparaumaaplica ção.Vimoscomore-
ceberargumentos,parâmetros,eretornarvaloresdenossasfun ções.Porfim,
aprendemoscomofuncionao early return,quepermitesairmaiscedo
dafun çãoe,porvezes,simplificarnossocódigo.]
63
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 76

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 77

Capítulo6
Arrays
Testeiojogoaquicomminhamãe,maselasemquererdigitouduasvezeso
mesmonúmero.Ebotouaculpanoprograma outramaneiradedizerqueo
programadorbobeou,claro.Ebobeeimesmo,eudeveriatomarocuidadoe
protegerojogadordenãotentarchutaromesmonúmeroduasvezes.Nesse
instanteeleprecisalembrardecabe çatodososnúmerosquechutou,oqueé
muitodifícil.
Comomemorizaroúltimonúmerochutado?Comumavariável,claro:
ultimo_chute = -1
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero tentativa, limite_de_tentativas
if verifica_se_acertou numero_secreto, chute
break
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 78

6.1. Criandoemanipulandoarrays CasadoCódigo
end
ultimo_chute = chute
end
Maseopenúltimochute?
ultimo_chute = -1
penultimo_chute = -1
limite_de_tentativas = 5
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero tentativa, limite_de_tentativas
if verifica_se_acertou numero_secreto, chute
break
end
penultimo_chute = ultimo_chute
ultimo_chute = chute
end
Eoantepenúltimochute? Eoanteantepenúltimochute? Eoqueveio
antesdesse?Dariaumnónaminhacabe çadetantavariável.Nãoquerotudo
issojogadoemumadezenadevariáveis.Piorainda,semudarmosonúmero
limitedetentativasde5paraoutronúmeroqualquer,teríamosquemudar
tambémonúmerodevariáveis,reescreverocódigoetc.Quetrabalho.
Comosempre,vamospararparapensarefazerumaúnicapergunta:o
quequeremos? Umamaneiradeguardardiversosnúmeros,depreferência
agrupadosparaqueeunãotenhacinquentanomesdevariáveistotalmente
diferentes.
Quetalumaúnicavariávelcapazdeguardarcinconúmeros?
6.1 Criando e manipulando arrays
Oquequeremosaquiéarmazenarumalistadenúmeros.Umasequênciade
númerosquepoderemosreferenciaratravésdeumavariávelsó.Essalistade
númeroséumarrayemRubyeveremosaquialgumasdascoisasqueum array
écapazdefazer.
66
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 79

CasadoCódigo Capítulo6. Arrays
Paracriarmosum arraycomcinconúmeros,usamos:
chutes = [176, 100, 130, 150, 175]
Sequeremosacessaraprimeiracasinha,oprimeironúmero,utilizamos
onúmerozerodentrodecolchetes:
chutes = [176, 100, 130, 150, 175]
puts chutes[0] # imprime 176
Portanto,tomecuidado!EmRuby,assimcomoemdiversasoutraslingua-
gens,opadrãoécome çarnonúmerozero. Sequisermosacessaronúmero
100,usaremos:
chutes = [176, 100, 130, 150, 175]
puts chutes[1] # imprime 100
Ouaindapodemosimprimiro 175:
chutes = [176, 100, 130, 150, 175]
puts chutes[4] # imprime 175
Paraalterarovalordentrodeumarrayusamosomesmocolcheteea
contagemdaposi çãocome çandocomzero:
chutes = [176, 100, 130, 150, 175]
chutes[3] = 300
puts chutes[2] # imprime 100
puts chutes[3] # imprime 300
puts chutes[4] # imprime 150
Podemostambémcriarumarrayvazioecolocarvaloresaospoucos:
chutes = []
chutes[0] = 50
chutes[1] = 150
chutes[2] = 300
puts chutes[0] # imprime 50
puts chutes[1] # imprime 150
puts chutes[2] # imprime 300
67
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 80

6.1. Criandoemanipulandoarrays CasadoCódigo
Mascomosabemosototaldeelementosquetemosdentrodenossoarray?
Podemosusarumcontador:
chutes = []
chutes[0] = 50
tentativa = 1
chutes[1] = 150
tentativa = 2
chutes[2] = 300
tentativa = 3
puts chutes[2] # imprime 300
puts chutes[tentativa - 1] # imprime 300
Ouaindafazerumla çoparaimprimirtodososvalores:
chutes = []
chutes[0] = 50
chutes[1] = 150
chutes[2] = 300
tentativa = 3
for contador in 1..tentativa
puts chutes[tentativa - 1]
end
Oresultadodessecódigoéaimpressão:
50
150
300
Massequisermosimprimirtodososvaloresdeumavezsó,podemospe-
dirparaimprimirdiretamenteoarray:
chutes = []
chutes[0] = 50
chutes[1] = 150
68
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 81

CasadoCódigo Capítulo6. Arrays
chutes[2] = 300
puts chutes
Resultandoem:
50
150
300
6.2 Aplicando o array ao nosso jogo
Vamosaplicaressenossoarrayaocódigodojogo.Primeirocriamosumarray
dechutesvazios,alémdototaldechutes:
limite_de_tentativas = 5
chutes = []
Assim que o usuário faz um chute, colocamos um valor dentro de
nosso arrayconversandocomele: “Senhorchutes,porfavor,coloqueaí
dentroo chuteatual”. Mascomo? Damesmamaneiraaumentamoso
total_de_chutes:
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero tentativa, limite_de_tentativas
chutes[total_de_chutes] = chute
total_de_chutes = total_de_chutes + 1
if verifica_se_acertou numero_secreto, chute
break
end
end
Comoétãocomumsomaremumavariável(alémdeoutrasopera ções
matemáticasqueveremosadiante),épossívelsomarereatribuirovalorde
umavezsó:
chutes[total_de_chutes] = chute
total_de_chutes += 1
69
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 82

6.2. Aplicandooarrayaonossojogo CasadoCódigo
Pronto,nosso arrayjáestácrescendo.Agoraéhoradeimprimi-loacada
novatentativa.Ondeimprimimostodasasinforma çõesdarodadaatual?No
pede_um_numero,portantopassamoscomoparâmetroparaeleoconteúdo
de chutes:
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero chutes, tentativa,
limite_de_tentativas
chutes[total_de_chutes] = chute
total_de_chutes += 1
if verifica_se_acertou numero_secreto, chute
break
end
end
Emsuadefini ção,recebemososchutescomoargumento,imprimindo-os:
def pede_um_numero(chutes, tentativa, limite_de_tentativas)
puts "\n\n\n\n"
puts "Tentativa " + tentativa.to_s + " de " +
limite_de_tentativas.to_s
puts "Chutes até agora: " + chutes
puts "Entre com o número"
chute = gets
puts "Será que acertou? Você chutou " + chute
chute.to_i
end
Aorodarocódigopercebemosque,comodecostume, Arraynãoécon-
vertidopara Stringautomaticamenteatravésdooperador +.Temosquein-
vocarométodo to_sparatransformá-loemuma String:
puts "Chutes até agora: " + chutes.to_s
Agorasim.Nossocódigorodaefunciona,imprimindoosnúmerosque
chutamosatéagora:
Tentativa 1 de 5
Chutes até agora: []
Entre com o número
70
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 83

CasadoCódigo Capítulo6. Arrays
200
...
Tentativa 2 de 5
Chutes até agora: [200]
Entre com o número
6.3 Facilidades de um array
Dadoumdosexemplosdeinser çãodeelementosemumarray:
total = 0
chutes = []
chutes[total] = 50
total += 1
chutes[total] = 150
total += 1
chutes[total] = 300
total += 1
puts chutes
Queresultaem:
50
150
300
Seráqueumarraynãoseriacapazdesaberquantoselementoshádentro
dele?Naprática,elesabe,eparaissoeledisponibilizaseutamanho,seu size:
total = 0
chutes = []
chutes[total] = 50
total += 1
chutes[total] = 150
total += 1
chutes[total] = 300
total += 1
puts chutes.size # imprime 3
71
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 84

6.3. Facilidadesdeumarray CasadoCódigo
Ouainda:
chutes = [100, 300, 500]
puts chutes.size # imprime 3
chutes[3] = 600
puts chutes.size # imprime 4
Seotempotodoelesabeotamanho,seriapossívelincluirdiretonapri-
meiraposi çãovazia.Notequeaprimeiraposi çãovaziaéaposi çãodototal
deelementos.Setemzeroelementos,éaposi çãozero.Setemumelemento,
éaposi çãoumdoarrayeporassimvai:
chutes = []
chutes[chutes.size] = 50
chutes[chutes.size] = 150
chutes[chutes.size] = 300
puts chutes.size # imprime 3
Masseoarraysabeseutotal,nãoseriapossíveleledisponibilizaralgoque
permitisseincluirumelementoaoseufinal,diretamente?Paraissotemoso
<<:
chutes = []
chutes << 50
chutes << 150
chutes << 300
puts chutes.size # imprime 3
Porfim,sequerofazerumla çoportodososelementosdeumarray,sou
mesmoobrigadoacriarumavariáveltemporária? Umcontador? Quando
contamosnosdedosusamosumcontador.Massetemosumasacolacomdez
canetas,equeremosdizeracordecadaumadelas,nãousamosumcontador,
simplesmenteabrimososaco,pegamosumacaneta,olhamosacor,pegamosa
próximacaneta,olhamosacor,apróxima,apróxima.Nãoprecisamoscontar
“1”,“2”etc.Quandoqueremospassarportodososelementos,semanecessi-
dadedecontar,podemosutilizarum forespecífico:
72
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 85

CasadoCódigo Capítulo6. Arrays
chutes = [100, 300, 500]
for chute in chutes
puts chute
end
6.4 S implificando nosso código de array
Essasacadademanterumavariáveldeajudacomotamanhorealutilizadode
umarrayémuitoimportanteeextremamenteutilizadoemdiversassitua ções.
Podemosremovernossavariável total_de_chuteseusaro size:
limite_de_tentativas = 5
chutes = []
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero chutes, tentativa,
limite_de_tentativas
chutes[chutes.size] = chute
if verifica_se_acertou numero_secreto, chute
break
end
end
MasseoRubytemalgoparanosauxiliarcomotamanhoatualdeum
array,seráqueelejánãotemalgoquenosajudaacolocarumvalornofinal
dele?Sim,jávimososímbolo <<:
chutes = [100, 300, 500]
chutes << 600
puts chutes.size # imprime 4
puts chutes[3] # imprime 600
Portanto,nossocódigofinalficaaindamaissimples:
da_boas_vindas
numero_secreto = sorteia_numero_secreto
73
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 86

6.5. ArrayseStrings CasadoCódigo
limite_de_tentativas = 5
chutes = []
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero chutes, tentativa,
limite_de_tentativas
chutes << chute
if verifica_se_acertou numero_secreto, chute
break
end
end
Apesardeserpossívelensinarsomenteo <<,éimportanteentendermos
queumarraypossuiumtamanhoinicialequevamosadicionandoaospoucos
novosvalores,mantendoumcontadorquedizquantoselementostemoslá
dentro.
6.5 Arrays e Strings
Atéagorausamosemdiversosmomentosalgoquesecomportamuitopa-
recidoaumarraysempararparapensarneles: eramnossas String,um
conjuntodecaracteres. Stringstambémpossuemumamaneiradesaber
seutamanho:
nome = gets
puts nome.size.to_s + " caracteres"
Rodamosocódigocomonome Guilhermeeeleimprime 10.Dez?Mas
meunometemnovecaracteres! Testamoscomdiversosoutrosvaloreseo
resultadoparecesersempreomesmo,umcaracteramais.Oqueestáacon-
tecendo?
Vamostentarimprimironomeeveroqueexisteládentro?
nome = gets
puts nome + " tem " + nome.size.to_s + " caracteres"
Eoresultado:
74
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 87

CasadoCódigo Capítulo6. Arrays
Guilherme
Guilherme
tem 10 caracteres
Queestranho!Esetentarmosimprimirocaracterequeestánestaposi ção,
utilizandoo []parapegaroelementonaposi ção 10:
nome = gets
puts "Resultado: "
puts nome[10]
Resulta:
Guilherme
Resultado:
Realmentetemalgodeestranhoaqui.Oqueacontece?Vamosverificaro
queeudigitei:
G, u, i, l, h, e, r, m, e, RETURN/ENTER
Acontecequequandolemosuma Stringcomo gets,recebemosuma
Stringincluindoo return(enter)queousuáriodeu,istoé,aquebradelinha,
ocaracterede new linejáestáaídentro.Porisso,toda Stringquelemose
quetentamosimprimirtemtamanhoumpoucomaiordoqueaparentemente
digitamos.Naverdadenóstambémfornecemoscomoentradao returneesse
códigotambémfoiinseridoemnossa String.
Comoarrancarforaessecaractere?Existeumafun çãonoRubyquepode-
mosusarcomtoda String.Essafun çãoespecialarrancaoscaracteresconsi-
derados“branco”,ouseja,quebrasdelinhaeespaço,tantodocome çoquanto
dofinaldasua String.Justamenteporarrancar,oseunomeé strip.O
códigoaseguir,queusao strip,imprime 9:
nome = gets.strip
puts nome + " tem " + nome.size.to_s + " caracteres"
Aplicamoso stripemnossocódigoaoleronome:
nome = gets.strip
Eaolerochute:
chute = gets.strip
75
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 88

6.6. InterpolaçãodeStrings CasadoCódigo
6.6 I nterpolação de Strings
Outracaracterísticainteressantedeuma Stringéacapacidadedecriaruma
Stringcomplexacompartesdeoutrasvariáveis. Tomecomoexemploa
impressãodonomequeusamosagora:
nome = gets.strip
puts nome + " tem " + nome.size.to_s + " caracteres"
Começaaficarbemchatoterquetransformartudocom to_seterque
ficarconcatenandocomabreefechaaspas,alémdediversos +.Queconfusão.
Emvezdisso,podemoscriarumanova Stringecolocarvaloresládentro:
nome = gets.strip
puts "#{nome} tem #{nome.size} caracteres"
Oresultadofinaléomesmo,masocódigoficabemmaissimples. Essa
característicadecomporuma Stringnovacomoresultadodeoutrasvariá-
veiséoquechamamosdeinterpolaruma String(string interpolation).
Podemosaplicaroconceitodeinterpola çãode Stringemduasfun-
cões de nosso jogo, simplificando nosso código ainda mais. A função
da_boas_vindaspodefazer:
puts "Começaremos o jogo para você, #{nome}"
Jáafunção pede_um_numerofica:
def pede_um_numero(chutes, tentativa, limite_de_tentativas)
puts "\n\n\n\n"
puts "Tentativa #{tentativa} de #{limite_de_tentativas}"
puts "Chutes até agora: #{chutes}"
puts "Entre com o número"
chute = gets.strip
puts "Será que acertou? Você chutou #{chute}"
chute.to_i
end
Pronto.Nossocódigodeconcatena çãopassaagoraaconverterautomati-
camente,invocandoafun ção to_sdecadaumdoselementosqueestásendo
interpolado.
76
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 89

CasadoCódigo Capítulo6. Arrays
6.7 Funções e métodos
Atéagoracriamosfun çõessoltas,fun çõesquesãodefinidas“voando”epor-
tantopodemserinvocadasdequalquerlugar. Opa,pareceadescri çãode
global,Guilherme? Issomesmo. Nossasfunçõesestãocomumescopoque
qualquerumpodeinvocardequalquerlugar,oquepodeparecermeioexa-
gerado.
Veremosemoutrosexemploscomomelhoraresseaspectodenossopro-
gramautilizandoconceitosbásicosdeorienta çãoaobjeto.Masantesdecri-
armosnossasfun çõescomescopocontrolado,játivemoscontatocomelas,
mesmosemperceber!
Noteque,quandolimpamosuma Stringdecaracteresbrancos,não
fizemosocódigoaseguir:
strip " Guilherme \n"
Massim:
" Guilherme \n".strip
Emvezdeinvocarmosumafun çãoglobal,passandouma Stringcomo
parâmetro,falamosparanossoobjeto Stringquegostaríamosdechamar
suafun ção strip.Fizemosissoatravésdooperador ..Essafun ção strip
nãoéglobal,masespecíficade Strings,portantoelatemumescopoli-
mitadoedeveser sempreaplicadaauma String. Écomoseafun ção,ao
invésdeserumacoisaglobal,flutuante,semdonoeaomesmotempocom
umgrandedono(todomundo,qualquerum),pertencesseauma String,
comoseelafosseumcomportamentodeuma String.Toda Stringtema
capacidadedeser stripada,temessecomportamentodisponível,essemétodo
(method)disponível.
6.8 Testando métodos no IRB
Masquempodeterummétodo?Qualquervalortemmétodos?
Vamosfazeralgunstesteseparaissogostariadeapresentarumaferra-
mentadoRubyquepermiteaexecu çãodepequenostestesdecódigorapida-
mente,o irb.Executando irb,temosumalinhadecomandoondepodemos
77
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 90

6.8. TestandométodosnoIRB CasadoCódigo
executarqualquercomandoRuby,eelemostraasaídaeoretornodaquele
código.
Umtestefáciléchamarométodomethods,quedevolvealistademétodos
queumvaloremRubypossui.Repareosmétodosqueminha Stringtem:
irb(main):001:0> "Guilherme".methods
=> [:<=>, :==, :===, :eql?, :hash, :casecmp, :+, :*, :%, :[],
:[]=, :insert, :length, :size, :bytesize, :empty?, :=~, :match,
:succ, :succ!, :next, :next!, :upto, :index, :rindex, :replace,
:clear, :chr, :getbyte, ...
:enum_for, :equal?, :!, :!=, :instance_eval, :instance_exec,
:__send__, :__id__]
Eosmétodosdeumnúmerointeiro:
irb(main):002:0> 175.method
=> [:to_s, :inspect, :-@, :+, :-, :*, :/, :div, :%, :modulo,
:divmod, :fdiv, :**, :abs, :magnitude, :==, :===, :<=>, :>, :>=,
:<, :<=, :~, :&, :|, :^, :[], :<<, :>>, :to_f, :size, :zero?,
:odd?, :even?, :succ, :integer?, :upto, ...
:enum_for, :equal?, :!, :!=, :instance_eval, :instance_exec,
:__send__, :__id__]
Muitacoisa?Nãotemproblema,aospoucosvamosconhecendoeutili-
zandocadavezmaisdeles.Porexemplo,jáusamosométodo stripe to_i
deuma String.Jáusamoso to_sdeuminteiro.Poderíamostambémusar
o upcasedeuma Stringparareceberumaoutra String,agoraemletra
maiúscula:
nome = "Guilherme"
puts nome.upcase # GUILHERME
Ouométodo odd?e even?parasaberseumnúmeroéímparoupar:
numero_secreto = 175
puts "O números secreto é ímpar?"
puts numero_secreto.odd? # true
CadavaloremRubyéumobjeto,etodoobjetopodetermétodos,por
issobasicamentetodovaloremRubypodetermétodos.Veremoscomocriar
78
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 91

CasadoCódigo Capítulo6. Arrays
nossosprópriostiposeobjetosmaisadiante,porenquantoésuficienteenten-
dermosquetodososnossosvaloressãodeumtipodeterminadoeporisso
possuemdiversosmétodosquepodemosinvocar.
Olhandoalistademétodosdeumnúmerointeiro,uma Stringeum
Array,surgemsímbolosquejáutilizamos,comoos []paraacessaruma
posiçãodeumarray,o +paraconcatenarousomar,ouaindao <<eo ==.
Seriamelesmétodos?Sim,napráticaelessãométodosepoderíamosinvocá-
loscomotal,sónãoparecenadanatural:
irb(main):001:0> "Guilherme".+(" Silveira")
=> "Guilherme Silveira"
irb(main):002:0> x = [50, 100, 150]
=> [50, 100, 150]
irb(main):003:0> x.[](2)
=> 150
irb(main):004:0> x.<< 200
=> [50, 100, 150, 200]
Lembraqueosímbolo +nãofuncionaentreuma Stringeuminteiro?
Éjustopoisométodo +deuma Stringéparaconcatenar Strings. Já
ométodo +denúmerosinteiroséparasomarinteiros.Sesóexistisseuma
funçãoglobalquesechamasse +,comofazerparaelasuportartodosostipos
de +queexistemnomundo?
Ométodoserveparacolocarcomportamentonovalor,juntarocompor-
tamentoespecíficoaovalorespecífico:uma Stringsabesetornarmaiús-
cula,eumnúmerosabedizerseéparouímpar.
6.9 R esumindo
Vimoscomoarmazenardiversosdadosemumaúnicavariávelatravésdouso
deumarray.Portrásdospanos,essearraypossuiumnúmerodeterminado
deespa çoseumcontador,eàmedidaqueeleéocupado,oespa çodobrade
tamanhopermitindocolocarmaiscoisasládentro. Vimosque Stringse
79
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 92

6.9. Resumindo CasadoCódigo
númerosinteirossãovaloresquepossuemmétodos,fun çõesquepossuem
umescopoespecífico,ejustamenteporissotemosfun çõesqueparecemser
iguais(comoafun ção +)masnaverdadesãodiferentes,sóquecomomesmo
nome.Conhecemosdiversasfun çõesemétodosjá,desdeo putse getsaté
o stripeo odd?.
Vimostambémcomolidarcomumarraynaprática,adicionandoebus-
candoelementos,alémdepesquisandoseutamanho.Aprendemosautilizara
interpolaçãode Stringparafacilitaracria çãodetextoscustomizados.Por
fim,revisamosporcimacomouminterpretadordeRubypodegerenciara
memóriadevariáveissimplesearrays.
80
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 93

Capítulo7
Pontosematemática
Chegouahorademostrarparaonossojogadorquantospontoseleganhou.
Ojogadorcome çacommilpontos.Acadachutequeelefazeleperdeuma
partedessespontos.Porexemplo,seonúmeroéo 175eelechuta 215,ele
erroupor 40,entãoojogadorperde 20pontos,istoé,eleperdeadiferen ça
entreosdoisnúmerosdivididapordois.
Sabemosdefinirumavariávelcomoumnúmero,portantoospontosaté
esseinstantesão 1000:
limite_de_tentativas = 5
chutes = []
pontos_ate_agora = 1000
Acadanovochute,calculamosadiferen çaqueerramos, chutemenoso
numero_secreto:
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 94

CasadoCódigo
pontos_a_perder = chute - numero_secreto
Agoraqueremosdividir( /)estevalorpor 2:
pontos_a_perder = chute - numero_secreto / 2
Porfim,tiramosdospontosatéagoraospontosaperder:
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
Nofinaldoprogramaimprimimosquantospontoseleganhou:
puts "Você ganhou #{pontos_ate_agora} pontos."
Ficandocomoseguintecódigo:
da_boas_vindas
numero_secreto = sorteia_numero_secreto
limite_de_tentativas = 5
chutes = []
pontos_ate_agora = 1000
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero chutes, tentativa,
limite_de_tentativas
chutes << chute
pontos_a_perder = chute - numero_secreto / 2
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
if verifica_se_acertou numero_secreto, chute
break
end
end
puts "Você ganhou #{pontos_ate_agora} pontos."
Sabendoqueonúmerosecretoé 175,testaremosprimeirochutaronú-
mero 215.Devemosperder 20pontos.Agoravamosacertar,oquenosdará
980pontos,repareasaída:
82
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 95

CasadoCódigo Capítulo7. Pontosematemática
...
Entre com o número
215
...
Entre com o número
175
...
Acertou!
Você ganhou 784 pontos.
Comoassim?Aconteceque,assimcomonamatemática,asopera çõesde
soma( +),subtra ção( -),multiplica ção( *),divisão( /)etc.obedecemuma
ordemrígida. Antesadivisãoemultiplica ção,depoisasomaesubtra ção.
Portantonossocódigoaseguirestádividindoonúmerosecretopor2:
pontos_a_perder = chute - numero_secreto / 2
Oquefazcomqueacontatenhaumresultadototalmentediferentedo
quequeríamos.Nósqueremosqueadivisãosejafeitadepois.Comoerafeito
naescolamesmo?Comousodeparêntesesparaindicarquemdeveserexe-
cutadoantes,paramudaraprecedênciapadrãodointerpretador:
pontos_a_perder = (chute - numero_secreto) / 2
Agorasim:
...
Entre com o número
215
...
Entre com o número
175
...
Acertou!
Você ganhou 980 pontos.
7.1 Ponto flutuante
Vamostestarcomoutrosnúmerosagora. Quetaltentarmos 176edepois
175?Devemosperdersomentemeioponto,resultandoem 999.5:
83
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 96

7.1. Pontoflutuante CasadoCódigo
...
Entre com o número
176
...
Entre com o número
175
...
Acertou!
Você ganhou 1000 pontos.
Como assim? Não perdi nada? Esse resultado só é possível se
pontos_a_perderforzero. Maseleéadivisãodeumpordois. Quanto
éumdivididopordois?Arespostaé:depende.
Naescolaaprendemosissoefacilmenteesquecemosquandocrescemos.
Primeiroaprendemosqueadivisãodeumpordoisézeroedárestoum.
Depoisaprendemosqueadivisãodeumpordoisémeio.Asduasrespostas
sãoválidas:umanouniversodosnúmerosinteiros,eaoutranouniversodos
númerosreais(nonossocaso,com ponto flutuante).
Porqueointerpretadornoslevouaoprimeirocaso?Poisatéagorausamos
númerosinteiros.Porexemplo:
irb(main):001:0> 215 - 175
=> 40
irb(main):002:0> 215 - 175 / 2
=> 128
irb(main):003:0> (215 - 175) / 2
=> 20
irb(main):004:0> exit
Masvamosparanossocasoatual,emqueusamos 176:
irb(main):001:0> 176 - 175
=> 1
irb(main):002:0> (176 - 175) / 2
=> 0
Acontaestásendofeitacomdoisnúmerosinteiros,portantooresultado
éinteiro. Mas,Guilherme,vocêconseguemeprovarqueessenúmeroestá
84
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 97

CasadoCódigo Capítulo7. Pontosematemática
sendotratadocomouminteiro?Sim,ométodo .classindicaqualotipo
daquelevalorqueestamosreferenciando. Reparequenúmerosinteirossão
Fixnumenúmeroscompontoflutuantesão Float:
irb(main):001:0> chute = 176
=> 176
irb(main):002:0> chute.class
=> Fixnum
irb(main):003:0> chute = 176.0
=> 176.0
irb(main):004:0> chute.class
=> Float
Setenhopelomenosumfloat,ocomputadorsabequeacontadeveser
feitacomnúmeroflutuante:
irb(main):001:0> 1.0 / 2
=> 0.5
irb(main):002:0> 1 / 2.0
=> 0.5
irb(main):003:0> 1.0 / 2.0
=> 0.5
Seambossãonúmerosinteiros,ocomputadorusanúmerosinteiros:
irb(main):001:0> 1 / 2
=> 0
Sabendodisso,comocorrigirnossocódigoparaacontaserfeitacomnú-
meroscompontoflutuante?Umasolu çãoédividirpor 2.0,aoutraémulti-
plicarpor 0.5,ambasteriamomesmoefeitoprático:
pontos_a_perder = (chute - numero_secreto) * 0.5
pontos_a_perder = (chute - numero_secreto) / 2.0
Mantemosaop çãodadivisãopor 2.0pordeixarmaisclarooque
estamosfazendocomadiferen çadochuteparaopróximodesenvolvedor,
lembra-sedaimportânciadepequenasescolhasnacompreensãodocódigo?
Agorasimoresultadoéonúmerocompontoflutuanteadequado:
85
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 98

7.2. Simulaçãodocódigo CasadoCódigo
...
Entre com o número
176
...
Entre com o número
175
...
Acertou!
Você ganhou 999.5 pontos.
7.2 Simulação do código
Vamostentaragoraoutrocenário,chutemos 171e 175:
...
Entre com o número
171
...
Entre com o número
175
...
Acertou!
Você ganhou 1002.0 pontos.
Comoépossíveleuterganhadopontos? Vamosrevisarafórmulaque
escrevemos:
# ...
pontos_ate_agora = 1000 # linha 1
for tentativa in 1..limite_de_tentativas # linha 2
chute = # ... linha 3
pontos_a_perder = (chute - numero_secreto) / 2.0 # linha 4
pontos_ate_agora = pontos_ate_agora -
pontos_a_perder # linha 5
# ... linha 6
end
# linha 7
86
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 99

CasadoCódigo Capítulo7. Pontosematemática
Querosaberexatamenteoqueaconteceparachegarnonúmero 1002.0,
istoé,querosimularmeuprogramanamão.Paraisso,pegamosumpeda ço
depapel(ouumpeda çodanossamemória,nanossacabe ça),ecome çamos
a“executar”ocódigonopapel,linhaalinha.
Oprogramachegaàlinhamarcada 1. Atéaqui,nãoimaginamosque
ocódigoexecutadovaiinterferircomnossoresultado.Agoraexecutamosa
linha 1,chegandoàlinha 2. Oquetemosnanossamemória? Aseguinte
situação,emqueexistemvariáveiscomvalores:
limite_de_tentativas = 5
pontos_ate_agora = 1000
Executamosalinha 2,entrandonalinha 3:
limite_de_tentativas = 5
pontos_ate_agora = 1000
tentativa = 1
Executamosalinha 3,entrandocomonúmero 171:
limite_de_tentativas = 5
pontos_ate_agora = 1000
tentativa = 1
chute = 171
Portanto,alinha 4seráequivalentea:
pontos_a_perder = (171 - 175) / 2
pontos_a_perder = -2
Opa.Númeronegativo?Vamosexecutá-la:
limite_de_tentativas = 5
pontos_ate_agora = 1000
tentativa = 1
chute = 171
pontos_a_perder = -2
Finalmente,executamosalinha 5:
87
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 100

7.3. Matemática CasadoCódigo
pontos_ate_agora = 1000 - -2
pontos_ate_agora = 1002
Encontramosnossobug.Onúmeronegativoocorreupoisonúmerochu-
tadofoimenorqueonúmeroreal.Esseprocessodesimularnopapelocódigo
sendoexecutado,juntocomosdadosdasvariáveisnamemória,évitalnoco-
meçodecarreiradeumdesenvolvedorparasercapazdemaisparaafrente
inferirocomportamentodocódigosemprecisardopapel,somentedeca-
beça.Oexemplodadoaquiépropositalmentemaissimplesdoqueosexem-
plosfuturosqueveremos,masmesmonodiaadiaerrosdecontanegativa,
divisãoporzero,somamaisoumenosum,sãoextremamentecomuns.Um
desenvolvedorcomfortetreinodesimula çãoécapazdedetectareresolver
taisproblemasmaisfacilmente.Nãotenhavergonha.
7.3 Matemática
Vamoscorrigirnossoprogramaverificandoseadiferen çaénegativa:
pontos_a_perder = (chute - numero_secreto) / 2.0
if pontos_a_perder < 0
pontos_a_perder = -pontos_a_perder
end
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
Jáconhecemosooutroestilode if,odeumaúnicalinha,quepoderia
serutilizadoaqui:
pontos_a_perder = (chute - numero_secreto) / 2.0
pontos_a_perder = -pontos_a_perder if pontos_a_perder < 0
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
Masevitaremosessecódigo,eleémuitoobscuropoisescondeo ifde
nossavista.Mesmonãousandoumavaria çãodo ifdeumalinha,podemos
fazerumavaria çãocomacontadevezesqueacreditopessoalmenteficarmais
clara.Seonúmeroénegativo,inverteosinalmultiplicandoopróprionúmero
por -1:
88
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 101

CasadoCódigo Capítulo7. Pontosematemática
pontos_a_perder = (chute - numero_secreto) / 2.0
if pontos_a_perder < 0
pontos_a_perder *= -1
end
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
Aindanãoestábom?Voltemosàauladematemática.Quandotemosum
númeroequeremossaberseuvalor,removidoosinal,queremosseuvalor
absoluto. Absoluto,entendeu?Dentreosmétodosdenúmerosinteiros,existe
umafun ção,ométodo abs:
pontos_a_perder = (chute - numero_secreto).abs / 2.0
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
if verifica_se_acertou numero_secreto, chute
break
end
Pronto.Adiferen ça,independentedenúmero,divididapor 2.
7.4 Unless... e a dupla negação
Outravaria çãoseriautilizaroinversodeum if,osomentesenão,o unless.
Somentesenãoformaiorquezero:
pontos_a_perder = (chute - numero_secreto) / 2.0
unless pontos_a_perder > 0
pontos_a_perder = -pontos_a_perder
end
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
Ouaindaemumalinha:
pontos_a_perder = (chute - numero_secreto) / 2.0
pontos_a_perder = -pontos_a_perder unless pontos_a_perder > 0
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
Nãoseincomodeseo unlessnãoparecernatural. Elenãoé. Nada
negativoénatural.Repareasduasfrasesaseguir:
89
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 102

7.5. Númeroaleatório CasadoCódigo
O natural é entendermos uma frase afirmativa.
O natural é entendermos uma frase não negativa.
Aprimeiraémaissimplesdoqueasegundaporummotivo:elanãoen-
volveumanega ção.Umadaspiorespráticaséaindaousodaduplanega ção,
maisconfusaainda:
O natural não é entendermos uma frase não afirmativa.
Pioraindaseanega çãoéimplícita.Oexemploaseguircontinuasendoo
mesmodesempre,masaduplanega çãopareceescondida:
O natural é não entendermos uma frase negativa.
Evitaremosousodo unlessporenvolverumanega çãoimplícita(como
nousodapalavra negativa)aoinvésdeexplícita(comonousodo não). E
mesmoquefosseexplícito,evitaremosousodaduplanega ção.Nofim,useo
unlesssomenteseeleformudarosentidodesuavidaespiritual:raramente.
Portantonãoalteramosemnadanossocódigo.
7.5 Número aleatório
Atéagoraonossojogoutilizouonúmero 175demaneirafixa,masjáestána
horadeescolhermosumnúmeroqualquer,umnúmeroaleatório,quetoda
vezmuda.Existeumafun çãoemRubychamada randquedevolveumnú-
meroentre 0(inclusive)e 1(exclusive).Portanto,poderíamoscalcular:
aleatorio = rand
Paraquenossonúmerotenhaovalormínimo 0(inclusive)emáximo
200(exclusive)podemosmultiplicaronúmeropor 200:
aleatorio = rand
numero_secreto = aleatorio * 200
Essaabordagemébastanteutilizadaemdiversaslinguagens,masemRuby
temosaop çãodepassarcomoargumentoparaafun ção randonúmero 200,
obtendoomesmotipoderesultadoqueantes:
90
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 103

CasadoCódigo Capítulo7. Pontosematemática
numero_secreto = rand(200)
Nossafun ção sorteia_numero_secretofica:
def sorteia_numero_secreto
puts "Escolhendo um número secreto entre 0 e 200..."
sorteado = rand(200)
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
sorteado
end
7.6 Operadores matemáticos
Vimosatéaquidiversosoperadoresmatemáticosquepodemseraplicados
tantoavaloresdotipo Fixnumquanto Floats.Asquatroopera çõesbásicas
sãoasoma( +),subtra ção( -),multiplica ção( *)edivisão( /).Umaquinta
operaçãoimportanteéaderesto(módulo, mod,
treze = 13
cinco = 5
dois = treze / cinco
tres = treze % cinco
dois_ponto_seis = 13.0 / 5
Essesoperadorescostumamserosmesmosemquasetodasaslinguagens
deprograma ção.Alémdeles,utilizamosoparêntesespararedefinirapriori-
dadedeexecu çãodasopera ções.
Existematalhosparaopera çõestradicionais,comoocasodesomar,sub-
trair,dividir,multiplicarouaplicarorestodeumadivisãoemsimesmo:
numero = 5
numero += 1 # 6
numero -= 2 # 4
numero *= 2 # 8
numero /= 4 # 2
numero *= 13 # 26
numero %= 10 # 6
91
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 104

7.7. Sistemadetipos CasadoCódigo
7.7 Sistema de tipos
Comovimosatéagora,cadavariávelquecriamosreferenciaumvalordeum
tipodeterminado. Cadalinguagemtrabalhacomumsistemadetiposdife-
rentes.EmRuby,umavariávelpodereferenciaremuminstanteumavariável
deumtipo Fixnumedepoisumadeumtipo String:
quinze = 15
quinze = "Quinze"
Porém,oqueimportaemtempodeexecu çãoéotipodovalorreferenci-
ado:
quinze = " Quinze "
quinze.strip # Quinze
quinze = 15
quinze.strip # undefined method ` strip'
Cadavaloréumainstânciadaqueletipo,éumobjetodaqueletipo,por-
tantopoderesponderadiversosmétodosqueforamdefinidosnele.Veremos
nofuturocomocriarnossosprópriostiposemétodos.
EmRuby,umtipoédinâmicoosuficienteparaqueelepossaseralterado,
eummétodoqueantesnãoexistiapodepassaraexistir. Esseconceito,de
queumacategoriadevaloreséabertaparamodifica ção,(chamadode classe
aberta),ouseja,essacapacidadequepermiteaaltera çãodeumtipoemtempo
deexecu çãoépoderosaeperigosa,poispodesurtirefeitosinesperados,como
quebradecompatibilidade,difíceisdeseremsimuladosecompreendidos.
Você pode consultar a documentação de cada tipo, como da classe
Stringnositedalinguagem:http://ruby-doc.org/core-2.1.2/String.html
7.8 Resumindo
Aprendemosafazeropera çõesmatemáticascomnúmerosinteirosecom
pontosflutuantes(casasdecimaisemgeral),alémdecolocarmosemprática
umdosprocessosquefarápartedoseudiaadiadeprograma ção:comosi-
mularumprograma primeironopapel,depois,comaprática,decabe ça.A
simulaçãoocorrecadavezmaisdemaneiraautomáticamasumcódigocom
92
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 105

CasadoCódigo Capítulo7. Pontosematemática
altacomplexidadetornataltarefadifícil,porissomesmoaimportânciade
semprerefatorarmosetentarmossimplificarocódigofinal.
Aprendemosautilizaro unlesseatomarcuidadoparaevitarmosuma
duplanega ção,alémdecomoutilizarnúmerosaleatórioseentenderque,se
eutenhotiposdiferentes,como String, Arrayetc.,euprecisodeumsis-
temadetipos,umaarquiteturadecomodevemfuncionaresecomportaresses
tipos,alémdesuasrela ções.
93
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 106

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 107

Capítulo8
Binário
8.1 Binário
Jávimosqueocomputadorusaamemóriaparaarmazenarosvaloresearrays
queutilizamosemnossoprograma. Massempreouvimosfalarqueeleusa
somentezeroeunsparafazertudo,comoassim?
Aideiadequezeroseunsemquantidadesuficientepodemrepresen-
tarqualquercoisaéinicialmenteassustadora. Imagineonúmero0,como
representá-lo?Fácil:0.Eonúmero1?Tambéméfácil,1.Pronto,temosum
bit.
O desafio começa, claro, quando queremos representar o número 2,
usandosomenteosalgarismos0e1. Asolu çãoéusaro10pararepresen-
taronúmero2.Cuidado.Nãoleia 10comodez,leiacomo“umzero”.Eo
númerotrês?11.Istoé,“umum”.Edepoisonúmeroquatro?100.Depois101,
110,111.Ficamoscomumatabela:
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 108

8.1. Binário CasadoCódigo
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
Claro,assimcomonamatemáticatradicional,podemospreenchercom
zeroàesquerdaparapadronizaraquantidadededígitos. Porexemplo,se
usarmos8dígitos,1 byte:
0 => 00000000
1 => 00000001
2 => 00000010
3 => 00000011
4 => 00000100
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
Pronto. Podemosseguiromesmopadrãoatéqualquernúmerointeiro,
claro,dadoquetenhamosmemóriasuficienteparaarmazenaressenúmero
comoumasequênciadezeroseuns.Nãoprecisamosdecoraragoraafórmula
deconversãodabase01,dabasededoisalgarismos( binária),paraabase
0123456789,abasededezalgarismos( decimal).Nemadeida,nemadevolta.
Masjásomoscapazesdeentendercomoocomputadorrepresentatodosos
númerosinteiros.
96
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 109

CasadoCódigo Capítulo8. Binário
8.2 Binário e letras
Mascomorepresentarletras? Enúmeroscompontoflutuante,casasdeci-
mais?
Dêumnúmeroparaumaletra.Porexemplo,‘A=65’.Então‘B=66’,‘C=
67’:
A => 65 => 01000001
B => 66 => 01000010
C => 67 => 01000011
...
Z => 90 => 01011010
Pronto,ocomputadorécapazderepresentartodasasletrasexistentesno
nossoalfabetousandosomente8dígitos0ou1. Essatabeladonossoalfa-
beto,incluindodiversosoutroscaracteres,éatabelaASCII,usadapormuito
tempocomooprincipalpadrãodetradu çãodenúmerosecaracteresporum
computador.
8.3 Bits:8,16,32,64
Cadaumdessesnúmeroséumbit,umaunidade0ou1. Seestamosuti-
lizandooitobitspararepresentarumnúmerointeiro,podemosrepresentar
2*2*2*2*2*2*2*2=256.Somenteosnúmeroszeroa256podemserrepresen-
tadoscomoitobits. Quehorror. MaseraassimquefuncionavaoMaster
System.JáoMegaDrivetinhaumprocessadorde16bits,representavanati-
vamentenúmerosaté65.536.NãoéàtoaqueosjogosdoMastertinhamem
geralnomáximo256cores,enquantoasdoMegatinhamaté65mil.
Masmesmoessenúmero,seráqueeleécapazderepresentartodosos
númerosinteirosquequeremos?Ouaindaumprocessadorcapazdeentender
earmazenar16bitsécapazderepresentartodasasletrasdetodososalfabetos
domundo?
Osprocessadoresmodernossãocapazesderepresentarnúmeroscomaté
64bits,oquedábonsbilhões,alémdetodooconjuntodecaracteresdos
alfabetosexistentesnomundo. Mesmoassimexistemotimiza çõesparare-
presentaroalfabeto,comoumpadrãofamosoportersubstituídooASCII
em2008comoomaisutilizadonainternet,oUTF-8.
97
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 110

8.4. Bitsenúmeroscompontoflutuante CasadoCódigo
8.4 Bits e números com ponto flutuante
Masaquestãodopontoflutuante,dacasadecimal,aindapersiste. Como
representartaisnúmerosseocomputadorsóconhecezeroseuns,números
inteiros?Énecessárioinventaralgumpadrão.Vamoscriaronossopróprio,
maissimplesdoqueumusadohojeemdia.Imagineonúmerotrezeemeio,
tambémconhecidocomo13,5.Quantosdígitoselepossuiantesdacasadeci-
mal?Dois?Então, 0010.Qualovalorquevemantesdacasadecimal?Um
depoistrês?Então, 0001 0011.Qualodígitoquevemdepoisdacasadeci-
mal? 5?Então, 0101.Portanto,pararepresentaronúmero 13,5utilizarei
anota çãoqueindicaonúmerodecasasantesdavírgula( 2),ovalordelas,
dígitoadígito( 1e 3)eovalordecimal( 5):
0010 0001 0011 0101
Pronto. Ocomputadorécapazdeentenderessenúmerocomo 13,5.
Comissosomoscapazesderepresentarqualquernúmerocomcasadecimal
cujaquantidadededígitossejafinita,mesmoqueessatécnicaestejalongede
serótimaouperfeita.Existeumalimita çãograndeemrela çãoàrepresenta ção
denúmeroscompontoflutuante. Seeuusoessetipodeabordagem,como
representarovalor 1 / 3 ,istoé,umter ço?
Essenúmerotemumaquantidadeinfinitadedígitos.Nãopodemosre-
presentarnanossaabordagem.Oquefazer?Arredondamospara 0,3,per-
demosprecisão:
0001 0000 0011
Oarredondamentofoimuitoruim?Tentamosentão 0,33:
0001 0000 0011 0011
Ouainda 0,333:
0001 0000 0011 0011 0011
Comoocomputadorcostumaseguirpadrõesdetamanhofixo,écomum
hojeemdiaqueumnúmerodepontoflutuante,assimcomoumnúmeroin-
teiro,utilize64bits. Issolimitaanossaaproxima ção. Paranossoumter ço,
usandoessaideiaapresentada(nãoideal),temosamelhoraproxima çãode
0,333.3com 62casasapósavírgula.
98
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 111

CasadoCódigo Capítulo8. Binário
0001 0000 0011 0011 0011 ... 0011
Emnossaabordagemderepresenta ção(emnossoalgoritmo)issonosli-
mitabastante,masarepresenta çãoescolhidaporumprocessadorébemmais
inteligentequeanossaepermiteaproxima çõesmuitoboas.
Umaideiaquesurgeéaderepresentarumadivisãocomoessacom 1
divididopor 3: 0001 0011,eaideiaéboa.Existemsistemaselinguagens,
principalmentematemáticas,quevãovalorizaraprecisãomaisdoqueame-
móriaouaperformance.Aslinguagensemgeralnãofazemissoporpadrão.
8.5 Hexadecimal
Assimcomovimosabasebinária,quetemsomentedoisalgarismosdistintos
pararepresentar todososnúmeros,conhecemosadecimal,quetemdezalga-
rismos.Existeoutrabasebastanteutilizada,abase hexadecimal,quetem
dezesseisalgarismos.Issopoiselaéoconjuntodequatrobits,querepresenta
dezesseispossibilidadesdiferentes,comovimosantes.
Massetemosdezesseisalgarismos,quealgarismossãoesses?Naescola
eusóvido0atéo9.Aqui,usaremosasletrasA,B,C,D,EeFpararepresen-
taressesoutrosseisalgarismos.Novamente,semanecessidadededecorara
fórmuladetransforma ção,atabelaaseguirmostraos 16primeirosnúmeros
embasehexadecimal:
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
99
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 112

8.6. Bitseimagens CasadoCódigo
14 => E
15 => F
Epoderíamoscontinuar,com:
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
cada),podemosrepresentar 16 * 16números, 256números.
8.6 Bits e imagens
Eoúltimodesafio:comorepresentarumaimagemdeumamaneirabemsim-
ples?Sesomoscapazesdemapearumacoisaanúmerosinteiros,somosca-
pazesdemapearaomundobinário,certo?
Nossodesafioécomorepresentarumaimagemcomnúmerosinteiros.
Primeirovamospensaremumafoto.Elatemdiversospontos.Cadaponto
temumacordiferente.Imaginequeafototem1000por1000pontos.Oque
podemosfazeréprimeiroenumerartodasascoresexistentes,limitando-asa
256:
cor0 = verde
cor1 = vermelho
cor2 = azul
cor3 = preto
cor4 = branco
...
cor255 = cinza
Mascalma,Guilherme,vocêdissequeocomputadorentendenúmeros,
nãocores.Sim,ecadacornocomputadortemumnúmero.Porexemplo:
100
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 113

CasadoCódigo Capítulo8. Binário
cor0 = 00FF00
cor1 = FF0000
cor2 = 0000FF
cor3 = 000000
cor4 = FFFFFF
...
cor255 = CCCCCC
Pronto. Dadaessatabela,agorapodemosescreverumalinhaparacada
pontonafoto.Seoprimeiropontodafotoévermelho(cor1)eosegundoazul
(cor2)eoterceirocinza(cor255)etc.,emumaimagemcomdiversaslinhas
temos:
cor1 cor2 cor255 cor3 cor3 cor2 cor3 cor255
cor1 cor3 cor255 cor3 cor2 cor3 cor3 cor255
...
Queemhexadecimalseria:
01 02 FF 03 03 02 03 FF
01 03 FF 03 02 03 03 FF
...
A sequência 0102FF representa uma pequena imagem
de 3 pontos, cujas cores seriam vermelho, azul e cinza. Já
0102FF03030203FF\n0103FF03020303FF representa uma imagem
comduaslinhase8colunas.
Comissopodemosrepresentarqualquerimagemcomtamanhofinito
(quecaibanamemória)ecujonúmerodecoresestejalimitadoa 256.Esse
éoraciocínioatrásdeummapadebitsdecores,um bitmap,oformato BMP,
tantoutilizadoantigamentenomundodacomputa ção. Suaado çãonãoé
maistãograndedevidoaotamanhoqueeleocupa:umaimagemcomgrande
qualidadeexigeumatabeladecoresenorme,eumnúmerodepontosmaior
ainda.Algoritmosdecompressãocomoo JPEGdominamessemercado.
Assimcomopensamosnaalternativaderepresentarumter çocomouma
fração(umdivididoportrês),poderíamosrepresentarumaimagemcomo
umasequênciadetra ços,círculosetc. Essatambéméumaideiaboapara
101
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 114

8.7. Resumindo CasadoCódigo
diversostiposdeimagem,eéoraciocínio,oalgoritmo,portrásdasimagens
vetoriais,comoo SVG.
Omesmopodeseraplicadoaomundodamúsica,como WAVe MP3,aos
filmesetc.
Nofim,representamosdesdeumnúmerointeiroatéumaimagemdeto-
mografiacomzerosouuns.Temosumafun ção,umalgoritmo,quemapeia
ummundoaooutro.
8.7 Resumindo
Vimoscomoumcomputadorécapazderepresentarnúmerosinteirosemum
formatobinário,comsomentedoisalgarismos,eescolhemos0e1paraserem
essesalgarismos.Aprendemosquenossabasedodiaadiaéadecimal,com
osalgarismosde0a9.Vimosqueeleutilizaabasehexadecimalcomosalga-
rismosextrasAatéF,equeconvertendodeumparaooutropassamosaser
capazesdeconverterqualquernúmeroemalgoparaocomputador,sempre
limitadoadeterminadotipodearredondamento,umavezquetemoslimite
dememória.
Aprendemoscomofuncionaatémesmoumafun çãogenéricaquetrans-
formacaracteresemnúmeroseaindaimagensemnúmeros,tudoissopara
entenderopoderdamatemáticanacomputa ção: eissoésóoiníciopara
aquelesquepretendemseaventurarnomundodapesquisanaciênciadacom-
putação.
102
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 115

Capítulo9
Níveldedificuldadeeocase
Nossojogoaindaébemdifícil. Umnúmeroentrezeroeduzentosprecisa
emmédiamaisde5tentativasparaacertar. Issopoisumatáticacomum(e
inteligente)écomeçarcomonúmerodomeio:100.
Seerrareonúmeroformaior,tenteonovonúmerodomeio,entre100e
200:150.Novamente,175.Novamente,187.Paraoúltimochute,teríamosas
opçõesentre188e200,umachancemuitopequenadeacertar.
Vamosfazercomotodososjogosfazem:permitiraojogadorqueescolha
oníveldedificuldade,cadaumdeterminandoointervalodenúmerosdentro
doqualserásorteadoonossonúmerosecreto. Porexemplo,nonívelfácil,
escolheremosumnúmeroentre0e30.Nomaisdifícil,umnúmeroentre0e
200.
Paradefinirnossafun ção pede_dificuldade:
def pede_dificuldade
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 116

CasadoCódigo
puts "Qual o nível de dificuldade que deseja?
(1 fácil, 5 difícil)"
dificuldade = gets.to_i
end
SabemosqueoRubysempreretornaoresultadodaúltimaexpressão,por-
tantonãoprecisamosdadefini çãodavariável dificuldade:
def pede_dificuldade
puts "Qual o nível de dificuldade que deseja?
(1 fácil, 5 difícil)"
gets.to_i
end
Porémessecódigoémaisdifícildecompreenderenossalvasomenteme-
nosde15caracteres.Nãomachucadeixá-lomaisclaro,porissofugireiaqui
dopadrãodenãodefiniravariável,deixandoóbviooretornodafun ção:
def pede_dificuldade
puts "Qual o nível de dificuldade que deseja?
(1 fácil, 5 difícil)"
dificuldade = gets.to_i
end
Agoraquandocome çamosojogo,logodepoisdedarboas-vindas,pedi-
remosoníveldedificuldade:
da_boas_vindas
dificuldade = pede_dificuldade
numero_secreto = sorteia_numero_secreto
Paraosorteiodonúmerosecretoseránecessáriosaberadificuldade,por-
tantoapassamoscomoparâmetro:
da_boas_vindas
dificuldade = pede_dificuldade
numero_secreto = sorteia_numero_secreto dificuldade
Nanossafun ção sorteia_numero_secretoorecebemos:
104
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 117

CasadoCódigo Capítulo9. Níveldedificuldadeeocase
def sorteia_numero_secreto(dificuldade)
puts "Escolhendo um número secreto entre 0 e 200..."
sorteado = rand(200)
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
sorteado
end
Definimosagoranossavariável maximoecorrigimosumbug. Nosso
númeromáximonãoera 200,eleera 199:
def sorteia_numero_secreto(dificuldade)
maximo = ???
puts "Escolhendo um número secreto entre 0 e
#{maximo - 1}..."
sorteado = rand(maximo)
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
sorteado
end
Precisamosagoraverificarovalordadificuldadeeconfiguraromáximo
deacordocomela:
if dificuldade == 1
maximo = 30
else
if dificuldade == 2
maximo = 60
else
if dificuldade == 3
maximo = 100
else
if dificuldade == 4
maximo = 150
else
maximo = 200
end
end
105
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 118

9.1. Case...when...end CasadoCódigo
end
end
Sim.Quenojo.Seriapossívelfazerumasériede ifs?Algoque,casoo
primeirofossefalso,tentasseosegundo,casoosegundofossefalso,tentasse
oterceiro?Sim,amaiorpartedaslinguagenssuportaaconstru çãoquejunta
o elsecomumnovo if. Nessecaso,asequência if...elsif...end
executarásomenteaprimeiracondi çãoverdadeira:
if dificuldade == 1
maximo = 30
elsif dificuldade == 2
maximo = 60
elsif dificuldade == 3
maximo = 100
elsif dificuldade == 4
maximo = 150
else
maximo = 200
end
9.1 Case...when ...end
Pormaisqueo if...elsif...endresolvanossoproblema,comorepeti-
mosarestri çãosempredeacordocomamesmavariável( dificuldade),
existeoutraconstru ção,aindamaissimples.Casoadificuldadeseja1,omá-
ximoé30.Casoseja2,60etc.
case dificuldade
when 1
maximo = 30
when 2
maximo = 60
when 3
maximo = 100
when 4
maximo = 150
else
106
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 119

CasadoCódigo Capítulo9. Níveldedificuldadeeocase
maximo = 200
end
Eutambémpoderiajuntardoisdeumavezsó,masnãovou,poisocódigo
ficaruimnovamente:
case dificuldade
when 1..2
maximo = 30 * dificuldade
when 3
maximo = 100
when 4
maximo = 150
else
maximo = 200
end
Rodamosnossojogoeverificamosqueelefunciona.Elemostraomáximo
deacordocomoníveldedificuldadeeescolheumnúmeronaqueleintervalo.
9.2 Escopo de v ariável local
Masreparealgodeestranho.Avariável maximofoidefinidadentrodo when,
efoiutilizadaforadele:
def sorteia_numero_secreto(dificuldade)
case dificuldade
when 1
maximo = 30
when 2
maximo = 60
when 3
maximo = 100
when 4
maximo = 150
else
maximo = 200
end
puts "Escolhendo um número secreto entre 1 e #{maximo}..."
107
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 120

9.3. Trapaceando CasadoCódigo
sorteado = rand(maximo) + 1
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
sorteado
end
EmRuby,umavariáveldefinidadentrodeumafun çãoévisíveldurante
todaafun ção.Nãoéum if, caseou forquelimitaoescopodavariável
maisainda.Porexemplo,ocódigoaseguirimprime15:
for i in 1..15
puts "calculando"
end
puts i
Essemesmocódigonamaioriadasoutraslinguagensdeprograma ção
retornariaalgumtipodeerro.Avariável iteriaoescoposomentedobloco
for. EmRubyissonãoacontece. Tomemuitocuidadoelembre-sequeo
padrãoéodasoutraslinguagens,emRubyessavariávellocalésemprelocal
aométodocomoumtodo.
9.3 Trapaceando
Masqueremosimpressionarnossosamigos. Queremostercertezadeque
quandojogamos,ganhamos,pormaisdifícilqueseja. Portanto,vamosve-
rificarsequemjogasoueumesmo:
if nome == seu nome
ganhei!
end
Ótimo,paraissoprecisamosarmazenaronome.Sabemosqueafun ção
quedáboas-vindasaindanãoretornaonome,masqueremos:
nome = da_boas_vindas
Portantonossafun çãopassaaretornaronome:
108
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 121

CasadoCódigo Capítulo9. Níveldedificuldadeeocase
def da_boas_vindas
puts "Bem vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets.strip
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, #{nome}"
nome
end
Aorodarastentativas,logoapóslerochutedojogador,verificamosseé
vocêmesmoe,casopositivo,ganhamos:
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero chutes, tentativa,
limite_de_tentativas
chutes << chute
if nome == "Guilherme"
puts "Acertou!"
break
end
# ...
end
Pronto! Jápodemosmostrarojogoparanossosamigoseoquãobom
somosemadivinha ção.
9.4 C orrigindo o número sorteado
Vimosqueoarraycome çacomaposi ção0,abasebináriaeahexadecimal
(assimcomoadecimal)também. Éjustoporissoqueonúmeroaleatório
tambémcomeçacomzeroe,consequentemente,nossonúmerosecretotam-
bém.Masissoéumtantoquantocontraintuitivoparaoserhumanonodiaa
dia.Jogadoresnãoestãoacostumadosaconsideraronúmerozeroemjogos
deadivinha ção,portantovamosalterarnossosorteiodenúmerosecretopara
considerarsomenteentre 1eomáximo,inclusive.
Arredondando:
109
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 122

9.4. Corrigindoonúmerosorteado CasadoCódigo
def sorteia_numero_secreto(dificuldade)
case dificuldade
when 1
maximo = 30
when 2
maximo = 60
when 3
maximo = 100
when 4
maximo = 150
else
maximo = 200
end
puts "Escolhendo um número secreto entre 1 e #{maximo}..."
sorteado = rand(maximo) + 1
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
sorteado
end
Nossocódigofinalfica:
def da_boas_vindas
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets.strip
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, #{nome}"
nome
end
def pede_dificuldade
puts "Qual o nível de dificuldade que deseja?
(1 fácil, 5 difícil)"
dificuldade = gets.to_i
end
def sorteia_numero_secreto(dificuldade)
case dificuldade
when 1
110
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 123

CasadoCódigo Capítulo9. Níveldedificuldadeeocase
maximo = 30
when 2
maximo = 60
when 3
maximo = 100
when 4
maximo = 150
else
maximo = 200
end
puts "Escolhendo um número secreto entre 1 e #{maximo}..."
sorteado = rand(maximo) + 1
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
sorteado
end
def pede_um_numero(chutes, tentativa, limite_de_tentativas)
puts "\n\n\n\n"
puts "Tentativa #{tentativa} de #{limite_de_tentativas}"
puts "Chutes até agora: #{chutes}"
puts "Entre com o número"
chute = gets.strip
puts "Será que acertou? Você chutou #{chute}"
chute.to_i
end
def verifica_se_acertou(numero_secreto, chute)
acertou = numero_secreto == chute
if acertou
puts "Acertou!"
return true
end
maior = numero_secreto > chute
if maior
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
111
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 124

9.5. While:jogandodiversasvezes CasadoCódigo
false
end
nome = da_boas_vindas
dificuldade = pede_dificuldade
numero_secreto = sorteia_numero_secreto dificuldade
limite_de_tentativas = 5
chutes = []
pontos_ate_agora = 1000
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero chutes, tentativa,
limite_de_tentativas
chutes << chute
if nome == "Guilherme"
puts "Acertou!"
break
end
pontos_a_perder = (chute - numero_secreto).abs / 2.0
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
if verifica_se_acertou numero_secreto, chute
break
end
end
puts "Você ganhou #{pontos_ate_agora} pontos."
9.5 While: jogando diversas vezes
Jogarojogoumavezédivertido,masjogardiversasvezesrequersuaexe-
cuçãodesdeocome ço,digitarnossonome,escolheradificuldadeepoderia
envolveraindaoutrospassos.Sedesejamosexecutarnossola çoprincipaldo
jogodiversasvezes,nadamaisnaturaldoqueextrairessecomportamento
paraumafun çãochamada joga.Poderepararqueelaprecisado nomeeda
dificuldade,quesãoasduasúnicasvariáveisindependentesdarodada:
112
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 125

CasadoCódigo Capítulo9. Níveldedificuldadeeocase
nome = da_boas_vindas
dificuldade = pede_dificuldade
joga nome, dificuldade
Nossafun çãoextraídarecebeosdoisvalores:
def joga(nome, dificuldade)
numero_secreto = sorteia_numero_secreto dificuldade
limite_de_tentativas = 5
chutes = []
pontos_ate_agora = 1000
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero chutes, tentativa,
limite_de_tentativas
chutes << chute
if nome == "Guilherme"
puts "Acertou!"
break
end
pontos_a_perder = (chute - numero_secreto).abs / 2.0
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
if verifica_se_acertou numero_secreto, chute
break
end
end
puts "Você ganhou #{pontos_ate_agora} pontos."
end
Agoracomofazerparajogardiversasvezes? Queremosexecutarocó-
digo joga nome, dificuldade eternamente. Olaçode forexecuta
umamesmacoisaumnúmerodeterminadodevezes,quenãoéoquede-
sejamos. Queremoseternamente,parasempre. Portanto,dizemosaocom-
putadorque para sempre:
113
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 126

9.6. loopdo...end CasadoCódigo
while true
joga nome, dificuldade
end
Claro,dizer trueéalgoestranho,ojogadorumdiavaiquererpararde
jogar.Secriarmosumafun ção quer_jogar:
while quer_jogar
joga nome, dificuldade
end
Edefinimosessafun ção,queperguntaseousuáriodesejajogar,retor-
nando truesearespostafor S:
def quer_jogar
puts "Deseja jogar novamente? (S/N)"
quero_jogar = gets.strip
quero_jogar == "S"
end
Masaotentarmosjogar,percebemosqueeleparamesmoqueeudigite s.
Oqueacontece?Lembradenossatabela ASCII?Letramaiúsculanãoéigual
àletraminúscula.Vamosinvocarométodo upcasedenossa String,que
serácapazdetransformá-laemmaiúscula:
def quer_jogar
puts "Deseja jogar novamente? (S/N)"
quero_jogar = gets.strip
quero_jogar.upcase == "S"
end
9.6 loop do...end
Pormaisqueojogofuncione,temosalgoestranho. Logoapósperguntar
nossonomeedificuldade,eleperguntasedesejamosjogarnovamente:
Bem-vindo ao jogo da adivinhação
Qual é o seu nome?
guilherme
114
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 127

CasadoCódigo Capítulo9. Níveldedificuldadeeocase
...
Começaremos o jogo para você, guilherme
Qual o nível de dificuldade que deseja? (1 fácil, 5 difícil)
1
...
Deseja jogar novamente? (S/N)
Nãoqueremosexecutaro quer_jogarlogodecara.Masaconstru ção
while...endprimeiroexecutaacondi ção,edepoisentranola ço.Quere-
mosumla ço,um loopqueprimeiroexecutatodoocódigo,esóquebrana
condiçãoespecíficadenãoquererjogar:
loop do
joga nome, dificuldade
if NAO quer_jogar
break
end
end
Mascomodizerquequeremosinverterumacondi ção?Seforfalsa,ver-
dadeira;seforverdadeira,falsa?Éooperador !:
loop do
joga nome, dificuldade
if !quer_jogar
break
end
end
Podemosescrevercomo ifemumalinha:
loop do
joga nome, dificuldade
break if !quer_jogar
end
Masaindaestáruim.Misturamosumoperadorcomportuguês.Quetal
renomearmosnossafun çãopara nao_quer_jogar,pareceficarmaislegí-
vel?
115
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 128

9.6. loopdo...end CasadoCódigo
loop do
joga nome, dificuldade
break if nao_quer_jogar
end
MaisaindaseseguirmosopadrãodoRubydeutilizar ?emfun çõese
métodosquedevolvemverdadeirooufalso( Booleans):
loop do
joga nome, dificuldade
break if nao_quer_jogar?
end
Nossafun çãonegativavira:
def nao_quer_jogar?
puts "Deseja jogar novamente? (S/N)"
quero_jogar = gets.strip
nao_quero_jogar = quero_jogar.upcase == "N"
end
Claro,assimcomoantes,seousuáriodigitaralgumaletraquenãoaes-
perada,ocomportamentonãoéoideal. Nossocódigofinaléumjogoque
podemospedirparaamigoseparentesjogarem,ondejáutilizamosdezenas
deconceitosdeprograma çãoecomputa ção:
def da_boas_vindas
puts "Bem-vindo ao jogo da adivinhação"
puts "Qual é o seu nome?"
nome = gets.strip
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, #{nome}"
nome
end
def pede_dificuldade
puts "Qual o nível de dificuldade que deseja?
(1 fácil, 5 difícil)"
dificuldade = gets.to_i
end
116
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 129

CasadoCódigo Capítulo9. Níveldedificuldadeeocase
def sorteia_numero_secreto(dificuldade)
case dificuldade
when 1
maximo = 30
when 2
maximo = 60
when 3
maximo = 100
when 4
maximo = 150
else
maximo = 200
end
puts "Escolhendo um número secreto entre 1 e #{maximo}..."
sorteado = rand(maximo) + 1
puts "Escolhido... que tal adivinhar hoje nosso número
secreto?"
sorteado
end
def pede_um_numero(chutes, tentativa, limite_de_tentativas)
puts "\n\n\n\n"
puts "Tentativa #{tentativa} de #{limite_de_tentativas}"
puts "Chutes até agora: #{chutes}"
puts "Entre com o número"
chute = gets.strip
puts "Será que acertou? Você chutou #{chute}"
chute.to_i
end
def verifica_se_acertou(numero_secreto, chute)
acertou = numero_secreto == chute
if acertou
puts "Acertou!"
return true
end
maior = numero_secreto > chute
if maior
117
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 130

9.6. loopdo...end CasadoCódigo
puts "O número secreto é maior!"
else
puts "O número secreto é menor!"
end
false
end
def joga(nome, dificuldade)
numero_secreto = sorteia_numero_secreto dificuldade
limite_de_tentativas = 5
chutes = []
pontos_ate_agora = 1000
for tentativa in 1..limite_de_tentativas
chute = pede_um_numero chutes, tentativa,
limite_de_tentativas
chutes << chute
if nome == "Guilherme"
puts "Acertou!"
break
end
pontos_a_perder = (chute - numero_secreto).abs / 2.0
pontos_ate_agora = pontos_ate_agora - pontos_a_perder
if verifica_se_acertou numero_secreto, chute
break
end
end
puts "Você ganhou #{pontos_ate_agora} pontos."
end
def nao_quer_jogar?
puts "Deseja jogar novamente? (S/N)"
quero_jogar = gets.strip
nao_quero_jogar = quero_jogar.upcase == "N"
end
118
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 131

CasadoCódigo Capítulo9. Níveldedificuldadeeocase
nome = da_boas_vindas
dificuldade = pede_dificuldade
loop
joga nome, dificuldade
break if nao_quer_jogar?
end
9.7 Resumindo
Vimos como refatorar uma sequência deifs aninhados para um
case...when...endquandoascondi çõessãoaplicadasaumaúnicava-
riável,lembrandoquetaisconstru çõespodemsersensíveisamudan ças:se
umnovovaloréaceito,temosquelembrardemudartodosospontosdaapli-
caçãoquefazemusodesses ifse cases,oqueéumcuidadoquedevemos
tomar.
Entendemosmelhoroescopodevariávellocal,criamosumrecursopara
umusuáriodeterminadoganharojogofacilmente,corrigimosumproblema
comonúmerosorteadoeaprendemosmaisdoistiposdela çobastanteutili-
zados:o while...endeo loop do...end.
119
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 132

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 133

Capítulo10
ArteASCII:jogodaadivinha ção
10.1 Melhorando nossa interface com o usuá -
rio
Podemosdeixaronossojogomaisatraentemudandoamaneiracomonos
comunicamoscomnossousuáriofinal. Umdosrecursosmaisantigosuti-
lizadospelosprogramadoresparaconstruirumainterfacedivertidaécriar
imagenscomcaracterescomuns,dodiaadia. Naépocaemqueestávamos
restritosàtabelaASCII,usávamossomenteosseuscaracteres,emesmoassim
éramoscapazesdefazerdivertidas.Vamosalterarumpouconossasfun ções
parautilizaressaarteASCII( ASCII art).
Primeiroalteremosnossafun ção da_boas_vindasparadesenharum
castelodeboas-vindas:
def da_boas_vindas
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 134

10.1. Melhorandonossainterfacecomousuário CasadoCódigo
puts
puts " P /_\ P "
puts " /_\_|_|_/_\ "
puts " n_n | ||. .|| | n_n Bem vindo ao "
puts " |_|_|nnnn nnnn|_|_| Jogo de Adivinhação!"
puts " |' ' | |_| |' ' | "
puts " |_____| ' _ ' |_____| "
puts " \__|_|__/ "
puts
puts "Qual é o seu nome?"
nome = gets.strip
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, #{nome}"
nome
end
Alteramostambémainterfacenahoradeperguntaradificuldade:
def pede_dificuldade
puts "Qual o nível de dificuldade?"
puts "(1) Muito fácil (2) Fácil (3) Normal (4) Difícil
(5) Impossível"
puts "Escolha: "
dificuldade = gets.to_i
end
Elecome çaráapedirpalpitesparaousuário. Enquantoousuárioerra,
elecontinuapedindo.Sevocêacertar,ficamosmuitofelizes.Extraímosuma
funçãochamada ganhou:
def ganhou
puts
puts " OOOOOOOOOOO "
puts " OOOOOOOOOOOOOOOOOOO "
puts " OOOOOO OOOOOOOOO OOOOOO "
puts " OOOOOO OOOOO OOOOOO "
puts " OOOOOOOO # OOOOO # OOOOOOOO "
puts " OOOOOOOOOO OOOOOOO OOOOOOOOOO "
puts "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO "
puts "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO "
122
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 135

CasadoCódigo Capítulo10. ArteASCII:jogodaadivinha ção
puts "OOOO OOOOOOOOOOOOOOOOOOOOOOOOO OOOO "
puts " OOOO OOOOOOOOOOOOOOOOOOOOOOO OOOO "
puts " OOOO OOOOOOOOOOOOOOOOOOOO OOOO "
puts " OOOOO OOOOOOOOOOOOOOO OOOO "
puts " OOOOOO OOOOOOOOO OOOOOO "
puts " OOOOOO OOOOOO "
puts " OOOOOOOOOOOO "
puts
puts " Acertou! "
puts
end
Nosmomentosemqueojogadorganhou,invoqueessafun ção.Testamos
nossojogo,agorasimtemosmuitomaisdiversão:
P /_ P
/__|_|_/_
n_n | ||. .|| | n_n Bem -vindo ao
|_|_|nnnn nnnn|_|_| Jogo de Adivinhação!
|' ' | |_| |' ' |
|_____| ' _ ' |_____|
__|_|__/
...
Qual o nível de dificuldade?
(1) Muito fácil (2) Fácil (3) Normal (4) Difícil (5) Impossível
...
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
123
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 136

10.1. Melhorandonossainterfacecomousuário CasadoCódigo
OOOO OOOOOOOOOOOOOOOOOOOO OOOO
OOOOO OOOOOOOOOOOOOOO OOOO
OOOOOO OOOOOOOOO OOOOOO
OOOOOO OOOOOO
OOOOOOOOOOOO
Acertou!
...
124
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 137

Capítulo11
Exercíciosextras:jogoda
adivinhação
Aquivocêencontraexercíciosextrasparasoltarsuaimagina çãoepraticar
lógicadeprograma çãonalinguagemRuby.
11.1 Melhorando o jogo de adivinhação
1) Senoúltimochuteousuárioerrarporum,avise-oqueissoaconteceue
dêaeleumaúltimachance.Paraissovocêprecisaráverificarseeleestáno
últimochuteeerrouporum,nessecasoaumenteonúmerodetentativas
emuma.
2) Temosaindaalgunsnúmerosmágicosemnossocódigo.Extraia-os.
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 138

11.2. Outrosdesafios CasadoCódigo
3) Nãodeixeousuáriojogaromesmonúmero. Seelejogouonúmero 2,
errou,ejogounovamenteo 2,avisequeelejájogouessenúmero,enão
contecomoumatentativa.
4) Mostrequantasvezesvocêganhou.
5) Mostrequantasvezesvocêperdeu.
6) Mostreaporcentagemdevezesquevocêganhou.Cuidadocomadivisão
por 0.
7) AoperderojogomostreumASCIIartcomo:
\|/ ____ \|/
@~/ ,. \~@
/_( \__/ )_\
\__U_/
Você perdeu! Tente novamente!
Paraissovocêdeveverificarseousuárioperdeuapósola çodetentativas
terminaresomentenessecasomostraramensagemde“perdeu”.Lembre-
sedeextrairocódigodo putsemumafun çãoseparada,seucódigoficará
maislegível.
11.2 Outros desafios
1) Escrevaumprogramaqueimprimatodososnúmerosparesentre2e50.
Parasaberseonúmeroépar,bastavocêverseorestodadivisãodonú-
meropor2éiguala0.
2) Escrevaumprogramaqueimprimaasomadetodososnúmerosde1até
100.Ouseja,elecalcularáoresultadode1+2+3+4+...+100.
3) Escrevaumprogramaquepe çauminteiroaousuário,ecomesseinteiro,
eleimprima,linhaalinha,atabuadadaquelenúmeroatéo10.Porexem-
plo,seeleescolheronúmero2,oprogramaimprimirá: 2x1=2, 2x2=4,
2x3=6, ..., 2x10=20 .
126
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 139

CasadoCódigo Capítulo11. Exercíciosextras:jogodaadivinha ção
4) Implementeumacalculadora.Oprogramadevepedir3númerosaousuá-
rio, a, be operacao.Se operacaoforigual1,vocêdeveráimprimira
somade a+ b.Seelafor2,asubtra ção.Sefor3,amultiplica ção.Sefor
4,adivisão.
5) Escrevaumprogramaquepe çaumnúmerointeiroaousuárioeimprima
ofatorialdessenúmero. Paracalcularofatorial,bastairmultiplicando
pelosnúmerosanterioresaté1.Porexemplo,ofatorialde4é 4 * 3 * 2
* 1,queéiguala24.
127
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 140

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 141

Capítulo12
Jogodaforca
Nossopróximograndejogoéodaforca,ondeojogadordeveadivinharuma
palavra,chutandocadavezumanovaletraouapalavrainteira.
Começamosnossoarquivo forca.rbcomamensagemdeboas-vindas
deacordocomonomedojogador:
def da_boas_vindas
puts "Bem-vindo ao jogo da forca"
puts "Qual é o seu nome?"
nome = gets.strip
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, #{nome}"
nome
end
Opróximopassoéaescolhadeumapalavrasecreta.Queremosmostrar
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 142

CasadoCódigo
onúmerodeletrascontidasnapalavrasecreta,paraissousamosométodo
size:
def sorteia_palavra_secreta
puts "Escolhendo uma palavra..."
palavra_secreta = "programador"
puts "Escolhida uma palavra com #{palavra_secreta.size}
letras... boa sorte!"
palavra_secreta
end
Definimostambémafun çãoqueperguntaseojogadordesejajogarno-
vamente:
def nao_quer_jogar?
puts "Deseja jogar novamente? (S/N)"
quero_jogar = gets.strip
nao_quero_jogar = quero_jogar.upcase == "N"
end
Onossola çoprincipaljogaráojogodiversasvezes:
nome = da_boas_vindas
loop do
joga nome
break if nao_quer_jogar?
end
Agoraaúnicagrandediferen çaestáemnosso joga. Nossafunçãode
jogardeveescolherapalavrasecreta,configurar0erroatéagoraecome çar
comzeroponto.
def joga(nome)
palavra_secreta = sorteia_palavra_secreta
erros = 0
chutes = []
pontos_ate_agora = 0
130
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 143

CasadoCódigo Capítulo12. Jogodaforca
# laco principal a escrever
puts "Você ganhou #{pontos_ate_agora} pontos."
end
Ola çoprincipaldeveserexecutadoatéonúmerodeerroschegara5,isto
é,enquanto errosformenorque 5:
def joga(nome)
palavra_secreta = sorteia_palavra_secreta
erros = 5
chutes = []
pontos_ate_agora = 0
while erros < 5
# o jogo
end
puts "Você ganhou #{pontos_ate_agora} pontos."
end
Agoradefinimosafun çãoquelêapalavrachutada.Mas,diferentemente
deantes,nãotemosumlimitedetentativasenãoarmazenamosatentativa
atual,somenteoschuteseonúmerodeerros:
def pede_um_chute(chutes, erros)
puts "\n\n\n\n"
puts "Erros até agora: #{erros}"
puts "Chutes até agora: #{chutes}"
puts "Entre com a letra ou palavra"
chute = gets.strip
puts "Será que acertou? Você chutou #{chute}"
chute
end
Podemos continuar com nosso laço principal, pedindo o chute e
guardando-onoarraydechutes:
131
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 144

12.1. Chutedeumapalavracompletaeacompara çãocom== CasadoCódigo
def joga(nome)
palavra_secreta = sorteia_palavra_secreta
erros = 0
chutes = []
pontos_ate_agora = 0
while erros < 5
chute = pede_um_chute chutes, erros
chutes << chute
# colocar as regras de acerto e erro aqui!
end
puts "Você ganhou #{pontos_ate_agora} pontos."
end
12.1 Chute de uma palavra completa e a compa -
ração com ==
Ojogadorganha100pontosacadapalavrachutadacertaeperde30pontos
acadapalavrainteirachutadaerrada. Elenãoperdenemganhapontosao
chutarumaletra,afinalcomcincochuteserradoseleperdeojogo.
Faltacolocarmosasregrasdeacertoeerro.Primeirodevemosconferirse
ousuáriochutouumaúnicaletra,istoé,sesuaentradatemtamanho1,ouse
ochutefoidapalavrainteira:
if chute.size == 1
# chutou uma única letra
else
# chutou a palavra inteira
end
Masjáfalamosqualoproblemadecomentários. Vamos=extrairuma
variável,algoquenosdigaseele chutou_uma_unica_letra:
chutou_uma_unica_letra = chute.size == 1
if chutou_uma_unica_letra
132
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 145

CasadoCódigo Capítulo12. Jogodaforca
else
end
Casoeletenhachutadoapalavrainteira,eacertado,mostramosamen-
sagemdeparabénseparamosajogadacomo breakquejáconhecemos:
chutou_uma_unica_letra = chute.size == 1
if chutou_uma_unica_letra
else
acertou = chute == palavra_secreta
if acertou
puts "Parabéns! Acertou!"
pontos_ate_agora += 100
break
else
end
end
Casoeleerre,tiramosos 30pontoseaumentamosumerro:
chutou_uma_unica_letra = chute.size == 1
if chutou_uma_unica_letra
else
acertou = chute == palavra_secreta
if acertou
puts "Parabéns! Acertou!"
pontos_ate_agora += 100
break
else
puts "Que pena... errou!"
pontos_ate_agora -= 30
erros += 1
end
end
Nossojogojáfuncionaparachutesinteirosdapalavra,porexemploseeu
133
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 146

12.2. Encontrandoumalgoritmo CasadoCódigo
tentarchutarapalavra programadores(-30pontos),edepoisapalavra progra-
mador(+100pontos),ojogoparacommeus70pontos:
Erros até agora: 0
Chutes até agora: []
Entre com a letra ou palavra
programadores
Será que acertou? Você chutou programadores
Que pena... errou!
...
Erros até agora: 1
Chutes até agora: ["programadores"]
Entre com a letra ou palavra
programador
Será que acertou? Você chutou programador
Parabéns! Acertou!
Você ganhou 70 pontos.
...
12.2 Encontrando um algoritmo
Mas precisamos agora suportar os chutes de letras. Cada vez que o
jogador tenta uma única letra devemos verificar se a nossaString
palavra_secretaincluiocaractereescolhido. Seriainteressantedizer
quantasvezesencontramostalletra.Sequisermoscontarquantasvezesen-
contramosumaletraemumapalavra,comopoderemosfazer?Vamospensar
comofazemosissocomocrian ças.Esseéosegredoparaescreveremcódigo
asolu çãodequalquerproblemalógico:lembre-secomovocêresolveopro-
blema,eimplemente-o. Mascuidado,lembre-secomoumacrian ça,poisa
criançausaasestruturasmaisbásicasdelógica(elanãousapotência,nem
log,nemcoisascomplexas,somente ifse fors).
Porexemplo,dadaapalavramágica, programadorparaumacrian ça,
comoelacontaquantasvezesaparecealetra o? Elaescrevezeroemum
cantinhodopapel(ounacabe ça,namemória!).Depoiselaolhaaprimeira
letradapalavra(apontaparaelacomodedo!).Essaletraéaletra oqueestou
procurando?Não.Vaiparaapróxima.É?Não.Próxima.É?Sim!Entãosoma
umnocantinhodopapel(namemória).Continuaatéofim.
134
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 147

CasadoCódigo Capítulo12. Jogodaforca
Nofim,seonúmeroézero,significaquealetranãoestáládentro,au-
mentaumerro.Seonúmeroédiferentedezero,elerepresentaquantasvezes
aletrafoiencontrada.Pronto.Temosnossaestruturalógicapararesolvero
problema,temosnossoalgoritmo.
Estouusandooexemplodeumacrian ça,masnãoseassuste,mesmoque
váresolverumproblemadegrafoscomplexosemquedesejaencontrarame-
noremaisbaratarotaentretrêscidadesviaaviãoaideiaéteremmenteque
descreveroproblemaemportuguês,ecomovocê(umadulto,umacrian ça
grande,nãoimporta)oresolveriacomestruturasbásicasdelógicaéachave
paraescreveroalgoritmonalinguagemdeprograma çãoquedeseja.Como
passardotempo,claro,vocêcome çaaeliminaressepasso.Nãotenhapressa
nenhuma.Doismeses,seismeses,seisanos.Osprogramadoresquevocêjá
viuescrevendocódigotêmanosdeexperiênciaeporissojáfizeramomesmo
quevocêestáfazendomilharesdevezes.CommilharesdepontosdeXPvocê
tambémserácapazdeescreveroalgoritmodecontarletrasdecabe ça.
12.3 Implementando o algoritmo
Tomemosaestrutura o algoritmo aopédaletra,comofoidescritaaqui:
dada a palavra mágica, %%programador%% para uma criança,
Ela escreve zero em um cantinho do papel (ou na cabeça, na
memória!).
Depois ela olha a primeira letra da palavra (aponta para ela com
o dedo!).
Essa letra é a letra %%o%% que estou procurando? Não.
Vai para a próxima.
É? Não.
Próxima.
É? Sim!
Então soma um no cantinho do papel (na memória).
Continua até o fim.
No fim,
se o número é zero,
significa que a letra não está lá dentro, aumenta um erro
se o número é diferente de zero,
135
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 148

12.3. Implementandooalgoritmo CasadoCódigo
ele representa quantas vezes a letra foi encontrada.
AgoratemosquetraduzirnossaestruturaparaRuby. Semproblemas.
Comecemoscomasvariáveis:
palavra_secreta = "programador"
chute = "o"
total_encontrado = 0
Depois ela olha a primeira letra da palavra (aponta para ela com
o dedo!).
Essa letra é a letra %%o%% que estou procurando? Não.
Vai para a próxima.
É? Não.
Próxima.
É? Sim!
Então soma um no cantinho do papel (na memória).
Continua até o fim.
No fim,
se o número é zero,
significa que a letra não está lá dentro, aumenta um erro
se o número é diferente de zero,
ele representa quantas vezes a letra foi encontrada.
Agoraprecisamostraduzirnossola ço,quandoacrian çapassaparacada
letra:
palavra_secreta = "programador"
chute = "o"
total_encontrado = 0
for i = 0..(palavra_secreta.size - 1)
letra = palavra_secreta[i]
Essa letra é a letra %%o%% que estou procurando? Não.
É? Não.
É? Sim!
Então soma um no cantinho do papel (na memória).
end
136
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 149

CasadoCódigo Capítulo12. Jogodaforca
No fim,
se o número é zero,
significa que a letra não está lá dentro, aumenta um erro
se o número é diferente de zero,
ele representa quantas vezes a letra foi encontrada.
Sealetraforaletracorreta,devemosatualizarnossocontador:
palavra_secreta = "programador"
chute = "o"
total_encontrado = 0
for i = 0..(palavra_secreta.size - 1)
letra = palavra_secreta[i]
if letra == chute
total_encontrado += 1
end
end
No fim,
se o número é zero,
significa que a letra não está lá dentro, aumenta um erro
se o número é diferente de zero,
ele representa quantas vezes a letra foi encontrada.
Enofimmostraroresultado:
palavra_secreta = "programador"
chute = "o"
total_encontrado = 0
for i = 0..(palavra_secreta.size - 1)
letra = palavra_secreta[i]
if letra == chute
total_encontrado += 1
end
end
if total_encontrado == 0
puts "Letra não encontrada!"
137
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 150

12.3. Implementandooalgoritmo CasadoCódigo
erros += 1
else
puts "Letra encontrada #{total_encontrado} vezes!"
end
Claro,nonossocódigojátemosavariável palavra_secretae chute.
Portanto,nossafun ção jogafica:
def joga(nome)
palavra_secreta = sorteia_palavra_secreta
erros = 0
chutes = []
pontos_ate_agora = 0
while erros < 5
chute = pede_um_chute chutes, erros
chutes << chute
chutou_uma_unica_letra = chute.size == 1
if chutou_uma_unica_letra
total_encontrado = 0
for i = 0..(palavra_secreta.size - 1)
letra = palavra_secreta[i]
if letra == chute
total_encontrado += 1
end
end
if total_encontrado == 0
puts "Letra não encontrada!"
erros += 1
else
puts "Letra encontrada #{total_encontrado}
vezes!"
end
else
acertou = chute == palavra_secreta
138
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 151

CasadoCódigo Capítulo12. Jogodaforca
if acertou
puts "Parabéns! Acertou!"
pontos_ate_agora += 100
break
else
puts "Que pena... errou!"
pontos_ate_agora -= 30
end
end
end
puts "Você ganhou #{pontos_ate_agora} pontos."
end
Essecódigoéuma“bela”deumafunção.Umcodigozão.Emtamanho,
nãoemqualidade.Pelocontrário,éassustadorotamanho,eoquefazemos
comcódigohorrívelqueoGuilhermeescreve?Refatoramos.
12.4 Boa prática : explorando a documentação
Novamentevamosaplicaroconceitodeextrairumtrechodecódigo,uma
funçãonova.Reparequeoatodecontarquantasvezesumcaractereaparece
emuma Stringpareceseralgorazoavelmenteisolável.Tireeledali:
def conta(texto, caracter)
total_encontrado = 0
for i = 0..texto.size
letra = texto[i]
if letra == caracter
total_encontrado += 1
end
end
total_encontrado
end
139
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 152

12.4. Boaprática:explorandoadocumentação CasadoCódigo
Masseolharmosnadocumenta ção, Stringspossuemummétodocha-
mado charsquedevolveumarraydecaracteres,quefacilitanossola ço:
def conta(texto, caracter)
total_encontrado = 0
for letra in texto.chars
if letra == caracter
total_encontrado += 1
end
end
total_encontrado
end
Ótimo,ocódigoficoumaissimples.Masjáqueestamosolhandoadocu-
mentação,éimportanteolharmoscomcalma,oqueéaquelemétodo count?
Elecontaonúmerodeapari çõesdeumcaractereemuma String(entre
outrasutiliza çõespossíveis).Logo,podemosremovercompletamentenossa
novafun ção!EssecódigojáexistenoRuby!
MasGuilherme,porquevocêmelevouacriartodaessafun ção,comum
laço,umcontador,paradepoisrefatorareporfimolharadocumenta çãoe
perceberqueocódigojáexistia?
Nãoestamosaquiaprendendoaser copy e pasters. Queremosentender
comoumprogramafuncionaeoquedeveserfeitoparaseresolverumpro-
blema.Semprequevocêusarumabibliotecaoufun çãoéimportanteentender
comoelaresolveseuproblema.Podemosnãosaberosmínimosdetalhes,mas
senãoentendermosoqueaconteceportrás,achancedealgumbugacontecer
émaior,afinalelapodefazeralgoquenãosabemosqueelafaz.
Nessecasoespecífico,évitalparaumprogramadorentendercomofunci-
onaumla çocomumcontador,essetipodeestruturalógicaéusadoemtodo
cantoquandoprogramamosdandocomandos,ordens(programa çãoimpe-
rativa)comofizemosatéagora.Desdeoalgoritmocomercialdocálculodo
totaldeumacompraatéumalgoritmomatemáticoencontrarosfatorespri-
mosdeumnúmeroqualquer,la çoscomacumuladores(númerosouarrays)
aparecemereaparecem.
140
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 153

CasadoCódigo Capítulo12. Jogodaforca
Comoregrageral,semprequequisermosfazeralgocomumvalordotipo
X(porexemplo Stringou Fixnum),vale muito, muito, muitoapenaolhar
adocumenta çãoeversejáexisteummétodoquefa çaisso.
Econformevocêjádeveterpercebido,sempreveremoscomoascoisas
funcionam,paraentãomelhorarnossocódigo.
Comoficaentãonossafun ção joga?
def joga(nome)
palavra_secreta = sorteia_palavra_secreta
erros = 0
chutes = []
pontos_ate_agora = 0
while erros < 5
chute = pede_um_chute chutes, tentativa,
limite_de_tentativas
chutes << chute
chutou_uma_unica_letra = chute.size == 1
if chutou_uma_unica_letra
total_encontrado = palavra_secreta.count(chute[0])
if total_encontrado == 0
puts "Letra não encontrada!"
erros += 1
else
puts "Letra encontrada #{total_encontrado}
vezes!"
end
else
acertou = chute == palavra_secreta
if acertou
puts "Parabéns! Acertou!"
pontos_ate_agora += 100
break
else
puts "Que pena... errou!"
pontos_ate_agora -= 30
erros += 1
141
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 154

12.5. next...Evitandochutesrepetidos CasadoCódigo
end
end
end
puts "Você ganhou #{pontos_ate_agora} pontos."
end
12.5 next...E vitando chutes repetidos
Pormaisquenossojogofuncione,temalgomuitoestranhoainda,ojogo
permitequeeutenteduasvezesamesmaletraoupalavra,algoquenãofaz
sentido.Elepoderiameavisar.Comofazerisso?
Pensandocomocrian ça,parasaberseeujáfaleiumaletraoupalavra,
devotodavezquefalarumaletraouumapalavraanotá-la. Depoisquando
faloumaletraoupalavranovabastaconferirseelajáfoianotadaantes.
Játemosaspalavrasanotadasemumarray,o chutes. Bastaverificar-
mos:
chute = pede_um_chute chutes, tentativa,
limite_de_tentativas
# verificar aqui se ja chutei
chutes << chute
Comoverificarseumvalorjáestápresenteemumarray?Comocrian ça,
tenhoqueirparatodososelementosdoarray,comparandoumaum,até
encontrar.Seencontrarumigual,verdadeiro,tem.Senenhumforigual,não
encontrei,nãotem.Issoé,umla çocomacumulador(ou early return),como
decostume.Emvezdeimplementarmosisso,parecerazoávelimaginarque
essatarefasejatãocomumquealinguagemnosforne çaisso.Sim,elaprovê
umafun çãochamada include?quenosdizseoarrayincluiovalorque
procuramos.
chute = pede_um_chute chutes, tentativa,
limite_de_tentativas
if chutes.include? chute
puts "Você já chutou #{chute}"
142
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 155

CasadoCódigo Capítulo12. Jogodaforca
end
chutes << chute
Tentamoseoqueacontece?
Entre com a letra ou palavra
p
...
Chutes até agora: ["p"]
Entre com a letra ou palavra
p
Será que acertou? Você chutou p
Você já chutou p
Letra encontrada 1 vezes!
...
Chutes até agora: ["p", "p"]
Entre com a letra ou palavra
Elenãoignorounossasegundaletra,adicionounoarrayumasegunda
vez,apesardemostraramensagemquejáahavíamospedido.Claro,nonosso
ifnóssomentemostramosamensagem,precisamosescreverocódigoque
continuanossola ço,ignorandotodoorestodocódigo.Mascomofazerisso?
Precisamosdealgumtipodecódigoquesejacapazdecontinuarola ço,
irparaapróximarodada,apróximaitera ção,semqueelepare. Apalavra
breakquebravaola ço,nãoéoquequeremos.Queremoscontinuarnapró-
ximarodada, next(emdiversaslinguagens, continue).
while erros < 5
chute = pede_um_chute chutes, tentativa,
limite_de_tentativas
if chutes.include? chute
puts "Você já chutou #{chute}"
next
end
chutes << chute
...
end
143
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 156

12.6. Resumindo CasadoCódigo
Agorasim,aorepetirmosumaletra,elanãoéadicionadaaoarraynova-
mente,nemverificada:
...
p
Será que acertou? Você chutou p
Letra encontrada 1 vezes!
...
Erros até agora: 0
Chutes até agora: ["p"]
Entre com a letra ou palavra
p
Será que acertou? Você chutou p
Você já chutou p
...
12.6 Resumindo
Vimoscomoutilizardiversascaracterísticasqueaprendemosanteriormente
deumalinguagemdeprograma ção,comola ços( while, for, loop),con-
dicionais( if),entradaesaída( putse gets),alémdeusaro strip,
arrays,somaesubtra ção.
Aprendemosautiliza çãodo breakedo nextparaquebraroucontinuar
umla ço,o countparacontarelementoseondeencontraradocumenta ção
dalinguagemparaevitarreinventararoda.
Entendemostambémcomofuncionaocora çãodeumprograma:acri-
açãoedescri çãodeumprocessoqueresolveumproblema,seualgoritmo.
Pensandocomocrian çassomoscapazesdequebraroalgoritmoempartes
tãopequenasquecondicionaisela çospodemdescrevê-lo,portantocriando
nossocódigoapartirdessadescri ção.
144
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 157

Capítulo13
Responsabilidades
13.1 Mostrando parte da palavra secreta
Nossojogoaindaédifícildeganhar:nãomostramosasposi çõesondeasletras
foramencontradas.Porexemplo,aochutaraletra odeveríamosteraresposta
doprograma:
__o______o_
Depoisde o,aochutar a:
__o__a_a_o_
Comopodemosfazerisso? Primeiropensamosondedesejamosimple-
mentaressecódigo. Vamosdaressainforma çãocomorespostaaojogador,
um feedbackacadanovarodada. Vamosimprimi-laduranteoprocessode
pedirumnovochute,dentrodo pede_um_chute:
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 158

13.2. Separandoainterfacecomousuáriodalógicadenegócios CasadoCódigo
def pede_um_chute(chutes, erros)
puts "\n\n\n\n"
puts "Erros até agora: #{erros}"
puts "Chutes até agora: #{chutes}"
puts "Entre com a letra ou palavra"
chute = gets.strip
puts "Será que acertou? Você chutou #{chute}"
chute
end
Reparequeafun çãode pedir_um_chuteéumafun çãodeinterface
comojogador,comousuário( user interfaceou UI).Diferentedeumcódigo
comoafun ção joga,queédelógicadonossojogo,lógicadonossonegócio
(business logic).
Tudoemumarquivo,80linhas,tudocomosefosseumescopoglobal,
qualquerumpodefazerqualquercoisa.Deondevenho,chamamosissode
“mistura”,temumpoucodetudo,juntatudonumúnicorecipiente. Naco-
midaficagostoso,masaquificaruimdeentender.
Chegouahoradecome çarmosasepararqueméquem,oqueéoquê.E
todotipodesepara çãoéfeitaemníveis. Jáfizemosumaprimeira,quando
extraímoseisolamosvariáveis;umasegunda,quandoextraímoseisolamos
funções;agoravamosextraireisolarpartesdenossojogodeacordocomsuas
responsabilidades.Queremosumaúnicaresponsabilidadeporarquivo,para
ficarmaisfácildeencontraroqueestáemquelugar.
13.2 Separando a interface com o usuário da ló -
gica de negócios
Asfun çõesquetemosemnossoprogramasão:
da_boas_vindas
sorteia_palavra_secreta
pede_um_chute
nao_quer_jogar?
joga
146
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 159

CasadoCódigo Capítulo13. Responsabilidades
Valelembrarquenossojogopossuiumainterfacedetextocomousuário,
tantoparaaentradaquantoparaasaída.Dessasfun ções, da_boas_vindas,
pede_um_chutee nao_quer_jogar?sãofun çõesclaramentedeinterface
comousuário,elasmostramepedeminforma ção,semexecutarnenhum
códigodelógica. Sãosomentesequênciasdeinvoca çõesafun çõesdotipo
getse puts,nomáximocomumaconversãodeumdadodeentradaqueé
Stringparaum booleano(verdadeirooufalso).
Já a função sorteia_palavra_secreta por enquanto só efetua
puts,nãopossuinenhumalógica,portantoacolocaremostambémnogrupo
deinterfacecomousuário.
Vamoscriarumarquivochamado ui.rbecolocamosnelenossasfun-
ções:
def da_boas_vindas
puts "Bem-vindo ao jogo da forca"
puts "Qual é o seu nome?"
nome = gets.strip
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, #{nome}"
nome
end
def pede_um_chute(chutes, erros)
puts "\n\n\n\n"
puts "Erros até agora: #{erros}"
puts "Chutes até agora: #{chutes}"
puts "Entre com a letra ou palavra"
chute = gets.strip
puts "Será que acertou? Você chutou #{chute}"
chute
end
def nao_quer_jogar?
puts "Deseja jogar novamente? (S/N)"
quero_jogar = gets.strip
nao_quero_jogar = quero_jogar.upcase == "N"
end
147
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 160

13.2. Separandoainterfacecomousuáriodalógicadenegócios CasadoCódigo
def sorteia_palavra_secreta
puts "Escolhendo uma palavra..."
palavra_secreta = "programador"
puts "Escolhida uma palavra com #{palavra_secreta.size}
letras... boa sorte!"
palavra_secreta
end
Éfácilnotarqueaúltimafun ção, joga,énaverdadeumamisturade
lógica( ifs, laçosetc.)einterfacecomousuário( puts).Oquefazercom
ela?Vamosanalisarcasoacasocadaumdos putsdenossafun ção,extraindo
apartede UIdadelógica,paradesembaralharospaguettiquetemos.
Primeiroencontramosocódigoqueverificasejáchutamosessemesmo
valoranteriormente:
chute = pede_um_chute chutes, erros
if chutes.include? chute
puts "Você já chutou #{chute}"
next
end
chutes << chute
Oquepodemosfazeraqui? Umasolu çãoécriarumafun çãochamada
avisa_chute_repetido,quesomenteinvocao puts,nonossoarquivo
ui.rb:
def avisa_chute_repetido(chute)
puts "Você já chutou #{chute}"
end
Ealterarnossocódigodelógicadevalorinválidoparachamaressafun-
ção:
chute = pede_um_chute chutes, erros
if chutes.include? chute
avisa_chute_repetido chute
next
end
chutes << chute
148
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 161

CasadoCódigo Capítulo13. Responsabilidades
Depoistemosasitua çãoemqueprocuramosaletra,comdoispossíveis
resultadosimpressos:
if total_encontrado == 0
puts "Letra não encontrada!"
erros += 1
else
puts "Letra encontrada #{total_encontrado}
vezes!"
end
Trocamospornovosmétodos,deresponsabilidadebemclaraemnosso
ui.rb:
def avisa_letra_nao_encontrada
puts "Letra não encontrada!"
end
def avisa_letra_encontrada(total_encontrado)
puts "Letra encontrada #{total_encontrado} vezes!"
end
Osdoiscasosdechutedepalavracompletatambémpodemserextraídos
emfun çõesparaonosso ui.rb:
def avisa_acertou_palavra
puts "Parabéns! Acertou!"
end
def avisa_errou_palavra
puts "Que pena... errou!"
end
Nossoúltimo putsdafun ção jogaéaquelequemostraospontos:
def avisa_pontos(pontos_ate_agora)
puts "Você ganhou #{pontos_ate_agora} pontos."
end
Ficamoscomafun ção jogalimpadequalquerinvoca çãodiretaa puts
ou gets.Tudooqueéfeitocomainterfacedousuárioestáfeitonoarquivo
ui.rb:
149
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 162

13.2. Separandoainterfacecomousuáriodalógicadenegócios CasadoCódigo
def joga(nome)
palavra_secreta = sorteia_palavra_secreta
erros = 0
chutes = []
pontos_ate_agora = 0
while erros < 5
chute = pede_um_chute chutes, erros
if chutes.include? chute
avisa_chute_repetido chute
next
end
chutes << chute
chutou_uma_unica_letra = chute.size == 1
if chutou_uma_unica_letra
total_encontrado = palavra_secreta.count(chute[0])
if total_encontrado == 0
avisa_letra_nao_encontrada
erros += 1
else
avisa_letra_encontrada total_encontrado
end
else
acertou = chute == palavra_secreta
if acertou
avisa_acertou_palavra
pontos_ate_agora += 100
break
else
avisa_errou_palavra
pontos_ate_agora -= 30
erros += 1
end
end
end
150
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 163

CasadoCódigo Capítulo13. Responsabilidades
avisa_pontos pontos_ate_agora
end
Portanto,nossoarquivo forca.rbpossuiadefini çãodafun ção joga
eainvoca çãodojogo:
nome = da_boas_vindas
loop do
joga nome
break if nao_quer_jogar?
end
Testamosrodarnosso ruby forca.rb etemosumerro:
forca.rb:43:in ` <main>': undefined local variable or method
` da_boas_vindas' for main:Object (NameError)
Elenãoencontraafun ção da_boas_vindasdonossooutroarquivo,
ui.rb.Claro,umarquivonãovêoutroarquivoporpadrão.Seriaumalou-
curaqueointerpretadorabrissetodososarquivosdenossocomputadorau-
tomaticamente,porpadrão,parabuscartudooquefossenecessário.Porisso
énecessárioindicarao forca.rbqueprecisamosdoarquivodeinterface
comousuário,requeremosocarregamentodoarquivo ui.rbrelativoao
diretórioatual,indicandologonocome çodenosso forca.rb:
require_relative 'ui'
def joga(nome)
# ...
end
# ...
Agorasim,rodamosnossojogoetudovoltaafuncionarnormalmente!
151
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 164

13.3. Extraindoalógicadenegócios CasadoCódigo
require
Assimcomoexisteainstru ção require_relative,hátambéma
require.Elabuscaemumalistadediretóriosespecíficospeloarquivo
mencionado. Porexemplo,podemosusá-laparacarregarabiblioteca
padrãodeacessoHTTP:
require "net/http"
require "uri"
uri = URI.parse("http://www.casadocodigo.com.br")
Net::HTTP.get_print(uri)
13.3 Extraindo a lógica de negócios
Nossafun ção jogaéanossalógicadenegóciosprincipal eclaramente
grandedemais. Elaémantidanoarquivochamado forca.rb. Mastam-
bém,pensandoassim,oiníciodenossojogoéumcódigodelógica:
nome = da_boas_vindas
loop do
joga nome
break if nao_quer_jogar?
end
Nadamaisnaturalnessavisãodoqueisolá-loemumafun çãoemnosso
forca.rbquesechame jogo_da_forca:
require_relative 'ui'
def joga(nome)
# ...
end
def jogo_da_forca
152
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 165

CasadoCódigo Capítulo13. Responsabilidades
nome = da_boas_vindas
loop do
joga nome
break if nao_quer_jogar?
end
end
Terminamosnossojogonesseinstantecomdoisarquivos.O forca.rb
comasduasfun çõesdelógica,o ui.rbcomnossafun çãodeinterfacecom
ousuário. Maseachamadaparao jogo_da_forca? Devemoscolocá-la
emalgumlugar.Vamoscriaroarquivo main.rbcomainvoca çãoaoinício
dojogo:
require_relative 'logic'
jogo_da_forca
Notequetodoprogramacostumaterumafun çãodeentrada.Nossocó-
digonãoestámaisvoando,comocódigoglobal. Issoétãocomumqueem
diversaslinguagenséobrigatóriaadefini çãodessafun çãoprincipal( main).
13.4 Extraindo a lógica de um chute v álido
Desejamosfazerumapequenaextra çãodefun çãoparavercomoficoumais
fácilentenderondeestánossocódigoeondeeledeveficar. Pensenalógica
denãopermitirchutesrepetidos.Encontrou?
chute = pede_um_chute chutes, erros
if chutes.include? chute
avisa_chute_repetido chute
next
end
Quecódigofeio,notequantainforma çãoemcincolinhas.Issonomeio
deumafun çãodecercade40linhas.Vamosisolá-loemumalógicaclara,que
pedeumchute válido:
chute = pede_um_chute_valido chutes, erros
153
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 166

13.4. Extraindoalógicadeumchuteválido CasadoCódigo
Agorabastadefinirafun çãode pede_um_chute_valido.Mascalma,
ondedeveficaressafun çãodelógica,quechamanossaUIdiversasvezes(até
umchuteválido)?Noarquivodelógica,claro.Nossafun çãofazumloope
pedeumchuteatéqueelesejaválido:
def pede_um_chute_valido(chutes, erros)
loop do
chute = pede_um_chute chutes, erros
if chutes.include? chute
avisa_chute_repetido chute
else
return chute
end
end
end
Repareque,aopedirnovamenteumchute,imprimimosnovasquatroli-
nhasetodoocabe çalho,meiorepetitivo.Vamosmudarnossasduasfun ções
quepedemumchuteparasimplificá-las. Aopedirochutemostramosso-
menteumavezaslinhasembranco,oserroseoschutes:
# no arquivo ui.rb
def cabecalho_de_tentativa(chutes, erros)
puts "\n\n\n\n"
puts "Erros até agora: #{erros}"
puts "Chutes até agora: #{chutes}"
end
# no arquivo forca.rb
def pede_um_chute_valido(chutes, erros)
cabecalho_de_tentativa chutes, erros
loop do
chute = pede_um_chute chutes, erros
if chutes.include? chute
avisa_chute_repetido chute
else
return chute
end
154
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 167

CasadoCódigo Capítulo13. Responsabilidades
end
end
Pedirumchuteficamaissimples:
def pede_um_chute(chutes, erros)
puts "Entre com a letra ou palavra"
chute = gets.strip
puts "Será que acertou? Você chutou #{chute}"
chute
end
Podemosinclusiveremoverosdoisparâmetrosaopedirumchute:
def pede_um_chute(chutes, erros)
puts "Entre com a letra ou palavra"
chute = gets.strip
puts "Será que acertou? Você chutou #{chute}"
chute
end
Claro,aoinvocarafun çãonãoprecisamosmaisdosparâmetros:
chute = pede_um_chute
Ficamoscomasduasfun çõesde ui:
def pede_um_chute
puts "Entre com a letra ou palavra"
chute = gets.strip
puts "Será que acertou? Você chutou #{chute}"
chute
end
def cabecalho_de_tentativa(chutes, erros)
puts "\n\n\n\n"
puts "Erros até agora: #{erros}"
puts "Chutes até agora: #{chutes}"
end
Eumadelógica:
155
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 168

13.5. Implementação:mostrandopartedapalavrasecreta CasadoCódigo
def pede_um_chute_valido(chutes, erros)
cabecalho_de_tentativa chutes, erros
loop do
chute = pede_um_chute
if chutes.include? chute
avisa_chute_repetido chute
else
return chute
end
end
end
13.5 Implementação : mostrando parte da pala -
vra secreta
Agoraqueisolamosduascamadas lógicadenegócioeinterfacecomousuá-
rioestamospreparadospararefatorareadicionarnovasfuncionalidadescom
maisfacilidadeeorganiza ção.
Nossopróximopassoéimplementaromostradordepalavraparcialcomo
citamosanteriormente.Porexemplo,aochutarasletras ae o,teríamos:
__o__a_a_o_
Qualoalgoritmoparafazerisso?Queremosimprimircadaletradenossa
palavrasecreta,logotemosqueversecadaumadelasjáfoichutada.Sesim,
usaaletra,senão,usao _(underline).
Temosnossoalgoritmo!Reparequeforamutilizadassomenteaspalavras
para cada(laço)e se/se não(if/else):
para cada letra in palavra_secreta
if letra ja foi chutada
usa letra
else
usa "_"
end
end
Claro,vamostraduzirparaRuby:
156
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 169

CasadoCódigo Capítulo13. Responsabilidades
for letra in palavra_secreta.chars
if chutes.include? letra
puts letra
else
puts "_"
end
end
Essecódigoéumafun çãodelógicamisturadacominterface,nãoparece
serbom.Alémdisso,cada putsvaiimprimirumaquebradelinha,teremos
umaletraporlinha,quenãoéoquequeremos.Emvezdisso,podemoscriar
umaúnicafun çãodelógica, palavra_mascarada,que,dadooschutesea
palavrasecreta,devolveapalavramascarada:
def palavra_mascarada(chutes, palavra_secreta)
mascara = ""
for letra in palavra_secreta.chars
if chutes.include? letra
mascara += letra
else
mascara += "_"
end
end
mascara
end
Essapalavrapodesercalculadalogoantesdepedirumchute,nocome ço
dola ço:
# ...
while erros < 5
mascara = palavra_mascarada chutes, palavra_secreta
chute = pede_um_chute_valido chutes, erros
chutes << chute
# ...
Aopedirochute,passaremosamáscaratambémcomoparâmetroparaa
interfacecomousuário:
157
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 170

13.5. Implementação:mostrandopartedapalavrasecreta CasadoCódigo
# ...
while erros < 5
mascara = palavra_mascarada chutes, palavra_secreta
chute = pede_um_chute_valido chutes, erros, mascara
chutes << chute
# ...
Vamosagoraàinterfacecomousuárioparafazercomque,aopedirum
chuteválido,mostremosamensagemcomamáscara:
# ui.rb
def cabecalho_de_tentativa(chutes, erros, mascara)
puts "\n\n\n\n"
puts "Palavra secreta: #{mascara}"
puts "Erros até agora: #{erros}"
puts "Chutes até agora: #{chutes}"
end
# forca.rb
def pede_um_chute_valido(chutes, erros, mascara)
cabecalho_de_tentativa chutes, erros, mascara
loop do
chute = pede_um_chute
if chutes.include? chute
avisa_chute_repetido chute
else
return chute
end
end
end
Agorasim,jogamosumarodada,escolhendoaletra a:
Palavra secreta: ___________
...
Será que acertou? Você chutou a
Letra encontrada 2 vezes!
...
Palavra secreta: _____a_a___
Erros até agora: 0
158
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 171

CasadoCódigo Capítulo13. Responsabilidades
Chutes até agora: ["a"]
...
Notequeaoadicionarumanovafuncionalidadealteramosoarquivode
lógica,nosso forca.rb. Aoalteraramaneiracomooprogramainterage
comousuário,mudamoso ui.rb. Seadicionamosumanovafuncionali-
dadequetambémmudaaitera çãocomousuário,alteramosambososarqui-
vos.
13.6 Resumindo
Aprendemosasepararocódigodelógicadenegóciosdocódigodeinterface
comousuário( UI)eparadeixartalsepara çãoaindamaisóbviacriamosar-
quivosdistintos,gerandoadependência(orequerimento)entreelesatravés
do require_relative.
Aofinalmenteadicionaralógicademostrarapalavrasecretacomoschu-
tesnasposi çõesadequadasfomoscapazesdeperceberqueaestruturacriada
nosajudaadefinirondevaicadamodifica ção:umanovalógicadenegócios
eumanovaitera çãoatravésdainterfacecomousuáriovãoemarquivosdis-
tintos.
Emsistemasmaioresouutilizandopráticasdecontroledeescopo( names-
pace),deorienta çãoaobjetos( OO)oulinguagensfuncionais,somoscapazes
deorganizaraindamaisnossocódigo.Àmedidaqueevoluirnoaprendizado
delinguagensvocêteráaoportunidadedeaprendercadaumdessesconcei-
tos,tudonomomentoadequadoedependendodocaminhoqueescolherpara
seupróximopasso.
159
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 172

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 173

Capítulo14
Entradaesaídadearquivo:
palavrasaleatóriaseotopplayer
14.1 Lendo um arquivo de palavras , nosso dici-
onário
Chegamosaosnossosúltimosdesafiosdojogodaforca.Primeiroqueremos
fazercomquealistadepalavrassejalidadeumarquivo,paraqueojogador
nãotenhaideiadequalpalavraestamosutilizando.
Paraissoteremosumarquivobemsimples,chamado dicionario.txt,
cujoformatoéumapalavraporlinha:
alura
casa do codigo
caelum
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 174

14.1. Lendoumarquivodepalavras,nossodicionário CasadoCódigo
desenvolvedor
programador
software
refatorar
code smell
Comolerosdadosdeumarquivo?Existemdiversasmaneirasdeexecutar
essatarefa.Umadelaslêtodooconteúdodoarquivodeumaúnicavezpara
amemória:
texto = File.read("dicionario.txt")
Podemosdepoisquebrarotextoemumarrayde Stringsseparadas
pelasquebrasdelinha,paraissoseparamos( split)pelasquebrasdenovalinha
(\n):
texto = File.read("dicionario.txt")
todas_as_palavras = texto.split("\n")
Agoraquetemosumarraydepalavraspodemosescolherumnúmero
entre 0eototaldepalavras:
texto = File.read("dicionario.txt")
todas_as_palavras = texto.split("\n")
numero_aleatorio = rand(todas_as_palavras.size)
Eescolherapalavrasecreta:
texto = File.read("dicionario.txt")
todas_as_palavras = texto.split("\n")
numero_aleatorio = rand(todas_as_palavras.size)
palavra_secreta = todas_as_palavras[numero_aleatorio]
Pronto, basta colocarmos esse código em nossa fun ção
sorteia_palavra_secreta. Mas essa função está emUI, não em
lógica:
def sorteia_palavra_secreta
puts "Escolhendo uma palavra..."
palavra_secreta = "programador"
162
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 175

CasadoCódigo Capítulo14. Entradaesaídadearquivo:palavrasaleatóriaseotopplayer
puts "Escolhida uma palavra com #{palavra_secreta.size}
letras... boa sorte!"
palavra_secreta
end
Vamosdefinirduasfun çõesde UI, avisa_escolhendo_palavrae
avisa_palavra_escolhida:
def avisa_escolhendo_palavra
puts "Escolhendo uma palavra..."
end
def avisa_palavra_escolhida(palavra_secreta)
puts "Escolhida uma palavra com #{palavra_secreta.size}
letras... boa sorte!"
palavra_secreta
end
Separamosumafun çãodelógica sorteia_palavra_secreta:
def sorteia_palavra_secreta
avisa_escolhendo_palavra
texto = File.read("dicionario.txt")
todas_as_palavras = texto.split("\n")
numero_aleatorio = rand(todas_as_palavras.size)
palavra_secreta = todas_as_palavras[numero_aleatorio]
avisa_palavra_escolhida palavra_secreta
end
14.2 Limpando a entrada de dados
Osdadosqueestamoslendodenossoarquivoaindapodempossuiralgumas
sujeiras. Porexemplo,nãoqueremosreclamarqueojogadorerroucasoele
chutealetra Pmaiúsculaparaapalavra programador,ouaindaqueapa-
lavraestejaregistradacomo progrAmAdorequeissofa çacomqueochute
aestejaerrado.
Precisamoslimpar,padronizar,normalizar,nossaentradadedados.Po-
demoscome çarcomnossoleitordechutes,ondesimplesmentetransforma-
mosochuteparaletrasminúsculasinvocandoométodo downcase:
163
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 176

14.3. Processamentoememóriadevemserotimizadas? CasadoCódigo
def pede_um_chute
puts "Entre com a letra ou palavra"
chute = gets.strip.downcase
puts "Será que acertou? Você chutou #{chute}"
chute
end
Aolernossoarquivotambémdevemosutilizarminúsculosparagarantir
queochute,agorasempreemminúsculo,encontresuaposi çãocorretanaspa-
lavrassecretas.Paraisso,aoescolherapalavrasecreta,podemostransformá-
laemminúsculo:
def sorteia_palavra_secreta
avisa_escolhendo_palavra
texto = File.read("dicionario.txt")
todas_as_palavras = texto.split("\n")
numero_aleatorio = rand(todas_as_palavras.size)
palavra_secreta =
todas_as_palavras[numero_aleatorio].downcase
avisa_palavra_escolhida palavra_secreta
end
Pronto!Adicionenoseudicionárioapalavra RuByeteste-acomum r
e Y,ambosdevemfuncionar.Vocêpode“roubar”edeixartemporariamente
somenteestapalavranodicionárioparafor çarotesteafazersairapalavra
quequeria.
14.3 Processamento e memória devem ser otimi -
zadas?
Pormaisqueessaabordagemfuncioneesejatotalmenteválida,lerumar-
quivointeiroparaamemóriapodeserruim.Temporariamenteconsumimos
muitamemóriaetambémtodavezqueinvocamosafun çãoparasortearuma
novapalavratemosquepassarportodooarquivo,mesmoqueapalavrasor-
teadaseja,porexemplo,aprimeira.Imaginequeseoarquivopossuidiver-
sosmegas,ocuparemostodoesseespa çonamemóriaparasortearumaúnica
palavra. Outraopçãoserialerprimeiroumnúmeronoarquivo,indicando
quantaspalavrasexistem:
164
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 177

CasadoCódigo Capítulo14. Entradaesaídadearquivo:palavrasaleatóriaseotopplayer
8
alura
casa do codigo
caelum
desenvolvedor
programador
software
refatorar
code smell
Apósleronúmerodelinhasexistentes:
arquivo = File.new("dicionario", "r")
total_de_palavras = arquivo.gets.to_i
Podemossortearumnúmero:
arquivo = File.new("dicionario", "r")
total_de_palavras = arquivo.gets.to_i
aleatoria = rand(total_de_palavras)
Agoravamosatéalinhaadequada,ignorandodiversasdelas:
arquivo = File.new("dicionario", "r")
total_de_palavras = arquivo.gets.to_i
aleatoria = rand(total_de_palavras)
for i = 1..aleatoria
arquivo.gets
end
Finalmentelemosapalavrasecreta,limpando-a,efechamosoarquivo:
arquivo = File.new("dicionario", "r")
total_de_palavras = arquivo.gets.to_i
aleatoria = rand(total_de_palavras)
for i = 1..aleatoria
arquivo.gets
end
palavra_secreta = arquivo.gets.strip.downcase
arquivo.close
165
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 178

14.4. Escritaparaarquivo:omelhorjogador CasadoCódigo
[/box]
Cadaabordagemdeleituradearquivoimplicaemumconsumodeme-
móriaeprocessamentomaioroumenor.Nestelivro,nossofoconãoéotimi-
zação,eumdicionáriode1megadepalavrasnãofazcócegasaoscomputado-
resmodernos,nãoprecisamosnospreocuparcomisso.Claro,noseudevido
tempo,àmedidaqueentramosemassuntoscomootimiza çãoeanálisede
algoritmosessapreocupa çãoaumenta,massemprequestionandoseelafaz
sentidoounão.Aquinãohádiferen çapráticanoresultado.
Existemaindaoutrasformasdeacessoaarquivoemdisco,comooacesso
aqualquerposi çãodele,semprecisarnecessariamentelerasprimeiraslinhas
(osprimeirosbytes),masparafazerissovocêdevesaberexatamentepara
quepontodoarquivoquerpular(emquantidadedebytes). Cadaformade
acessoaumarquivopossuiumavantagemedesvantagem,comoquasetoda
funcionalidade.
14.4 Escrita para arquivo: o melhor jogador
Devemosguardarquemfoiomelhorjogadoratéagora,comoformadedesa-
fioaopróximojogador.Primeirovamosacumularospontosporrodada.A
função jogapoderetornarospontosatéagora:
def joga(nome)
# ...
avisa_pontos pontos_ate_agora
pontos_ate_agora
end
Aoinvocarmosemnosso jogo_da_forcadevemosacumularesses
pontos,come çandocomzero:
def jogo_da_forca
nome = da_boas_vindas
pontos_totais = 0
loop do
pontos_totais += joga nome
break if nao_quer_jogar?
166
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 179

CasadoCódigo Capítulo14. Entradaesaídadearquivo:palavrasaleatóriaseotopplayer
end
end
Precisamosavisarojogadortodavezquaissãoseuspontostotais,logo
definimosafun çãoem ui.rb:
def avisa_pontos_totais(pontos)
puts "Você possui #{pontos} pontos."
end
Acadanovarodadamostramosessespontosparaojogador:
def jogo_da_forca
nome = da_boas_vindas
pontos_totais = 0
loop do
pontos_totais += joga nome
avisa_pontos_totais pontos_totais
break if nao_quer_jogar?
end
end
Pronto,aojogarmosnossojogoeacertandoasduasprimeirasvezestemos
oresultadode 200pontosacumulados:
...
Será que acertou? Você chutou refatorar
Parabéns! Acertou!
Você ganhou 100 pontos.
Você possui 200 pontos.
Deseja jogar novamente? (S/N)
Antesdeperguntarmosseousuáriodesejajogarnovamentedevemossal-
varonomedousuárioeseuspontosemumarquivo,algocomo:
def jogo_da_forca
nome = da_boas_vindas
pontos_totais = 0
167
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 180

14.5. Lendoomelhorjogador CasadoCódigo
loop do
pontos_totais += joga nome
avisa_pontos_totais pontos_totais
salva_rank nome, pontos_totais
break if nao_quer_jogar?
end
end
Edefinimosafun ção salva_rank:
def salva_rank(nome, pontos)
end
Definimosoconteúdodoarquivo,queseráonomenaprimeiralinhae
ospontosnasegunda:
def salva_rank(nome, pontos)
conteudo = "#{nome}\n#{pontos}"
end
Porfim,utilizamosafun ção writede Fileparasalvaroconteúdoem
umarquivochamado rank.txt:
def salva_rank(nome, pontos)
conteudo = "#{nome}\n#{pontos}"
File.write "rank.txt", conteudo
end
Rodamosnossojogoeapósvencerduasvezescom 200pontostemosa
saídanoarquivo:
guilherme
200
14.5 Lendo o melhor jogador
Queremosmostrarparaojogadoratualqueménossocampeão,equantos
pontoselejáconquistou.Jásabemoslerosdadosdeumarquivoequebraras
linhas:
168
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 181

CasadoCódigo Capítulo14. Entradaesaídadearquivo:palavrasaleatóriaseotopplayer
def le_rank
conteudo_atual = File.read "rank.txt"
dados = conteudo_atual.split("\n")
end
Agoraquetemososdadosdorankpodemosmostrá-lonocome çodo
programa:
def jogo_da_forca
nome = da_boas_vindas
pontos_totais = 0
avisa_campeao_atual le_rank
loop do
pontos_totais += joga nome
avisa_pontos_totais pontos_totais
salva_rank nome, pontos_totais
break if nao_quer_jogar?
end
end
Edefinirnossafun çãode uiqueavisaocampeãoatual:
def avisa_campeao_atual(dados)
puts "Nosso campeão atual é #{dados[0]} com #{dados[1]}
pontos."
end
Massempresalvamosonomedoúltimojogadorenãoéissoquequere-
mosfazer.Desejamossemprearmazenaromelhordetodososjogadores.Isso
é,seojogadorjáexistenoarquivo,queremosmantersomenteoquepossui
maispontos.
Antesdesalvar,temosqueverificarseonomeeapontua çãoquejáestão
lásãomaisbaixasqueapontua çãoatual.Portanto,antesdesalvarosdados
devemosverificarsuapontua ção:
def jogo_da_forca
nome = da_boas_vindas
169
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 182

14.6. Refatoração:extrairarquivo CasadoCódigo
pontos_totais = 0
avisa_campeao_atual le_rank
loop do
pontos_totais += joga nome
avisa_pontos_totais pontos_totais
if le_rank[1].to_i < pontos_totais
salva_rank nome, pontos_totais
end
break if nao_quer_jogar?
end
end
Pronto! Játemosnossorankdeprimeirolugar. Semprearmazenamos
queméomelhorjogador.
14.6 Refatoração : extrair arquivo
Sófaltaorganizarumpoucomaisnossocódigo.Reparequetemosduasfun-
çõesdelógicaligadasaorank. Naverdademaisdoquelógica,elassãoas
funçõesdearmazenamentodedados( data access),logoisolaremostantoa
le_rankquantoa salva_rankemumarquivochamado rank.rb.
def le_rank
conteudo_atual = File.read("rank.txt")
dados = conteudo_atual.split("\n")
end
def salva_rank(nome, pontos)
conteudo = "#{nome}\n#{pontos}"
File.write("rank.txt", conteudo)
end
Nãopodemosesquecerdealterarnossoarquivo forca.rbparaincluir
relativonosso rank:
170
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 183

CasadoCódigo Capítulo14. Entradaesaídadearquivo:palavrasaleatóriaseotopplayer
require_relative 'ui'
require_relative 'rank'
# ...
Extraircódigoparaoutroarquivonãoéumarefatora çãograndiosa.Ela
simplesmentevarreparaoutrolugaronossocódigo(quecontinuacomfun-
çõesglobais),organizandoempequenasunidades(arquivos)parafacilitar
encontraremanterasfun ções.Veremosemumpróximojogocomoorgani-
zaraindamaisessecomportamento,fugindodaabordagemglobal.
14.7 A pilha de execução
Removaseuarquivo rank.txt.Agorarodenovamenteojogo.Logoapós
entrarcomseunome,aaplica çãopara:
Começaremos o jogo para você, Guilherme
rank.rb:2:in ` read': No such file or directory -
rank.txt (Errno::ENOENT)
from rank.rb:2:in ` le_rank'
from forca.rb:82:in ` jogo_da_forca'
from main.rb:3:in ` <main>'
Comotodamensagemdeerro,olhemoscomcalmaoqueaconteceaqui.
Primeiro,eleindicaqueoproblemaaconteceunoarquivo rank.rb,linha2(
rank.rb:2).Aotentarmosinvocarafun ção read( in ‘read’),ocorreu
umerrocomadescri ção No such file or directory - rank.txt
(Errno: :ENOENT).
Éfundamentalentendermosamensagemdeerroparadescobriroque
aconteceu.Eladizquenãofoiencontradooarquivooudiretório rank.txt.
Fazsentido,elerealmentenãoexiste. Notequeumamensagemdeerrore-
almenteéricadeinforma ções,elanosemquearquivo,quallinhaequala
descriçãoquedeuproblema.
Masoquesãoasinforma çõesquevêmlogodepoisdela?Temosmaistrês
linhasparaentendermelhor:
171
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 184

14.7. Apilhadeexecução CasadoCódigo
from rank.rb:2:in ` le_rank'
from forca.rb:82:in ` jogo_da_forca'
from main.rb:3:in ` <main>'
Apróximalinhaindicaemquearquivoelinhaestávamosquandooerro
ocorreu:
conteudo_atual = File.read("rank.txt")
Apróximalinhaqueeleindicaénoarquivodelógica:
avisa_campeao_atual le_rank
Porfim,alinhadoarquivo main.rb:
jogo_da_forca
Oqueessaslinhasindicam?Reparequealinha3do main.rbéquem
chamaafun ção jogo_da_forca,queéquemchamaafun ção le_rank,
queéquemchama File.read,queéondeaconteceoerro. Issoé,essas
linhasdamensagemdeerroindicamocaminhoqueaexecu çãodoprograma
percorriaquandodomomentodoerro. Aúnicacoisa“estranha”équeela
estádeponta-cabeça:
from rank.rb:2:in ` le_rank'
from forca.rb:82:in ` jogo_da_forca'
from main.rb:3:in ` <main>'
Jásimulamosnossoprogramaumavez, vamossimulá-lonovamente.
Agoracomaindamaiscarinhoeaten ção. Primeirorodamosocomando
ruby main.rb,quecarregaocódigodoarquivo main.rb:
require_relative 'logic'
jogo_da_forca
Aprimeiralinhacarregaoarquivodelógica,queporsuavezcarregaos
arquivosde ranke ui,todosdefinindoumadezenadefun ções,masne-
nhumexecutandoalgumcódigo.
Oprogramachegaatéaterceiralinhadenosso main.rb:
172
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 185

CasadoCódigo Capítulo14. Entradaesaídadearquivo:palavrasaleatóriaseotopplayer
jogo_da_forca
Mascomooprogramasabeemquelinhaeleestá?Assimcomoumacri-
ançaprecisadeseusdedos,umavariável,parasaberemquenúmeroestá,o
programatambémprecisadevariáveisparaindicarondeestánonossocó-
digo.Portanto,emalgumlugardamemória,oprogramaarmazenaondeele
está:
funcao_atual = "main" # funcao sem nome, o código em si
arquivo_atual = "main.rb"
linha_atual = 3
Agoraelevaiexecutaralinha3. Masaotentarexecutaressalinhaele
sedeparacomainvoca çãodeumafun ção:eleprecisairatéondeestáessa
função,noarquivo forca.rb,linha 78:
def jogo_da_forca
nome = da_boas_vindas
pontos_totais = 0
avisa_campeao_atual le_rank
loop do
pontos_totais += joga nome
avisa_pontos_totais pontos_totais
if le_rank[1].to_i < pontos_totais
salva_rank nome, pontos_totais
end
break if nao_quer_jogar?
end
end
O programa troca o conteúdo das variáveisarquivo_atual,
linha_atuale funcao_atual:
funcao_atual = "jogo_da_forca"
arquivo_atual = "forca.rb"
linha_atual = 78
173
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 186

14.7. Apilhadeexecução CasadoCódigo
Alinha78éadefini çãodafun ção,quenãofaznada.Maselelogoexecuta
alinha79,80e81,chegandona82comaseguintememória:
nome = "guilherme"
pontos_totais = 0
funcao_atual = "jogo_da_forca"
arquivo_atual = "forca.rb"
linha_atual = 82
Agoraeleinvocaafun ção le_rank,trocandoovalordasvariáveisno-
vamente:
nome = "guilherme"
pontos_totais = 0
funcao_atual = "le_rank"
arquivo_atual = "rank.rb"
linha_atual = 1
Imaginequeocódigodafun ção le_rankfuncionenormalmente,queo
arquivoexista.Nessecaso,aosairdafun ção le_rank,paraondeoprograma
deveir?Paraorestodalinha 82no forca.rb,queédeondeoprograma
veioeinvocou le_rank.Masessainforma çãojáera,jáfoiperdidaquando
trocamosovalordasvariáveisparadescrever le_rank.Opa.Oprograma
ficariaperdido!
Issosignificaqueaquiloquedescrevinãoéarealdescri çãodecomoum
programafunciona.Elenãopodearmazenarsomentealinhaearquivoatual.
Seeletrocarovalor,fim.Oprogramanãosabeparaondevoltarecontinuar
quandoumafun çãoretorna.
Vamosescreveroproblemacomtodasaspalavras: oprogramaprecisa
saberexatamentequemchamouquem,equemchamouquem,equemcha-
mouquem,...,equemchamouquem,parasaberparaquemeledevevoltar,
umaum.Podemospensarquecadavezquechamamosumafun ção,avan-
çamosumnível,cadavezquesaímosdeumafun ção,saímosdessenível.Por
exemplo,considereocódigoaseguirnoarquivo nomes.rb:
174
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 187

CasadoCódigo Capítulo14. Entradaesaídadearquivo:palavrasaleatóriaseotopplayer
def le_nome
nome = gets # 1
puts "Lido!" # 2
nome
end
def pede_nome
puts "Digite seu nome" # 3
nome_lido = le_nome # 4
puts "Pedido!" # 5
nome_lido
end
def inicio
nome = pede_nome # 6
puts "Bem vindo #{nome}" # 7
puts "Quero conhecer mais alguém"
nome2 = pede_nome # 8
puts "Olá #{nome2}" # 9
end
inicio # 10
O interpretador do Ruby lê a definição das funções le_nome,
pede_nomee inicio. Porfim,elechegaàlinhamarcada 10,ondean-
tesdeinvocarafun ção inicioelecontinuanocódigo principal(main)
denossoarquivo.Portanto,temossóumníveldechamada:
nomes.rb:10 in main
Aoinvocarafun ção inicio,elevaiparaalinhamarcada 6,eanotao
novonível em cimadonívelatual:
nomes.rb:6 in inicio
nomes.rb:10 in main
Essainforma çãonosdizexatamentecomooprogramachegouaondeestá.
Continuemoscomaexecu çãodocódigo,invocandoafun ção pede_nomee
indoparaalinhamarcada 3:
175
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 188

14.7. Apilhadeexecução CasadoCódigo
nomes.rb:3 in pede_nome
nomes.rb:6 in inicio
nomes.rb:10 in main
Eleagoraimprimeamensagem Digite seu nome echegaàlinhamar-
cada4.
nomes.rb:4 in pede_nome
nomes.rb:6 in inicio
nomes.rb:10 in main
nome_lido = le_nome # 4
Essa linha possui dois passos. O primeiro é a invocação da função
le_nome,eosegundoaatribui çãodoresultadodelaaumavariávellocal
chamada nome_lido.Agoraeleinvocaafun ção le_nome:
nomes.rb:1 in le_nome
nomes.rb:4 in pede_nome
nomes.rb:6 in inicio
nomes.rb:10 in main
Notequeagoraleremosonomedousuário,echegamosàlinha2,portanto
temosaexistênciadeumavariávellocal:
def le_nome
nome = gets # 1
puts "Lido!" # 2
end
nomes.rb:2 in le_nome (nome="Guilherme")
nomes.rb:4 in pede_nome
nomes.rb:6 in inicio
nomes.rb:10 in main
Agoraelesaidafun ção,comofazerisso?Simples,bastajogarforaaúltima
funçãoquefoiinvocada,aúltimalinhaquefoi empilhada(push)nessapilha
defun ções( stack):
nomes.rb:4 in pede_nome
nomes.rb:6 in inicio
nomes.rb:10 in main
176
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 189

CasadoCódigo Capítulo14. Entradaesaídadearquivo:palavrasaleatóriaseotopplayer
Ainda existe o segundo passo a ser executado nessa linha. A fun-
çãojáretornou "Guilherme",logoécriadaumavariávellocalchamada
nome_lidocomessevalor:
nomes.rb:4 in pede_nome (nome_lido = "Guilherme")
nomes.rb:6 in inicio
nomes.rb:10 in main
Chegamosàlinhamarcada 5:
nomes.rb:5 in pede_nome (nome_lido = "Guilherme")
nomes.rb:6 in inicio
nomes.rb:10 in main
Notequedurantesuaexecu ção,avariávelantigachamada nomejánão
existemais,afinal,jásaímosdafun ção le_nome,masavariável nome_lido
localexiste.
Terminando a execução da função pede_nome, o valor da variável
nome_lidoéretornado.Comofazemosmesmoasaídadeumafun ção?De-
sempilhamos( pop)aúltimalinhadenossapilhadeexecu ção( stack trace).
nomes.rb:6 in inicio
nomes.rb:10 in main
Asegundapartedalinhamarcada 6éacriaçãodeumavariávelchamada
nome,comovalordoretornoda pede_nome:
nomes.rb:7 in inicio (nome = "Guilherme")
nomes.rb:10 in main
Imprimimoso nomecomamensagemdeboas-vindas.Continuamosa
execuçãoatéalinhamarcada 8:
def inicio
nome = pede_nome # 6
puts "Bem vindo #{nome}" # 7
puts "Quero conhecer mais alguém"
nome2 = pede_nome # 8
puts "Olá #{nome2}" # 9
end
177
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 190

14.7. Apilhadeexecução CasadoCódigo
nomes.rb:8 in inicio (nome = "Guilherme")
nomes.rb:10 in main
Entramosnafun ção pede_nome,queentranafun ção le_nome:
nomes.rb:1 in le_nome
nomes.rb:4 in pede_nome
nomes.rb:8 in inicio (nome = "Guilherme")
nomes.rb:10 in main
def le_nome
nome = gets # 1
puts "Lido!" # 2
end
Oqueaconteceráapósexecutarmosalinhamarcada 1?Teremoscriado
umanovavariávellocalcomvalor,porexemplo, Daniela:
nomes.rb:2 in le_nome (nome = "Daniela")
nomes.rb:4 in pede_nome
nomes.rb:8 in inicio (nome = "Guilherme")
nomes.rb:10 in main
Calmaaí.Duasvariáveiscomomesmonome?Issofazsentido?Claro!
Elassãolocaisàfun ção!Cadaumadelassóévisualizadadentrodeseupró-
prioescopo,nocasolocal.Avariávelchamada nomequeestásendoutilizada
nafun ção inicioéumavariáveltotalmentediferentedavariávelchamada
nomequeestásendoutilizadanafun ção le_nome.
Esteéo localdonomevariável local. Avariávelviveeexistesomente
duranteaquelachamadadafun ção,etemseuespa çodememóriaisoladoda
deoutrométodoquefoichamado.
Assimcomoumaempilhadeira,aexecu çãodeumprogramaempilhaas
diversasfun çõesquevãosendoinvocadas. Oprocessodeempilhar( push)
edesempilhar( pop)éfeitotodavezqueentramosesaímosdeumafun ção,
permitindoqueoprogramasaibaexatamenteondeestáedeondeveio. A
pilhadecoisastambémtemnome,éapilhadeexecu ção( execution stack).E
aquelaslinhasquemostramondeestamos,quenosmostramtodoocaminho
percorrido( trace)napilhadeexecu ção,éo stack trace.
178
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 191

CasadoCódigo Capítulo14. Entradaesaídadearquivo:palavrasaleatóriaseotopplayer
14.8 Resumindo
Aprendemosafazeraleituradeumarquivodetextos,alimpar(normalizar)
osdadoslidosparaevitarsujeira,eaescreveremumarquivoasinforma-
çõesdonossomelhorjogador. Refatoramosnossocódigoparaextrairum
arquivocomasresponsabilidadesdeentradaesaídaparadiscoesimulamos
nossoprogramaparaentenderumconceitofundamentaldetodalinguagem
deprograma ção:apilhadeexecu ção.
179
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 192

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 193

Capítulo15
ArteASCII:jogodaforca
15.1 Melhorando nossa interface com o usuário
Começamoscriandonossoarquivo rank.txtnovamente:
Guilherme
100
Podemosdeixaronossojogomaisatraentemudandoamaneiracomo
noscomunicamoscomnossousuáriofinal.Utilizandonovamente ASCII art
eumpoucodeinforma çãovisualmaisbonitavamoslevarnossojogopara
umnovonível.
Mudamosaaberturapara:
def da_boas_vindas
puts "/****************/"
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 194

15.1. Melhorandonossainterfacecomousuário CasadoCódigo
puts "/ Jogo de Forca */"
puts "/****************/"
puts "Qual é o seu nome?"
nome = gets.strip
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, #{nome}"
nome
end
Nahoradedesenharaforcadesejamosimprimiracabe ça,ocorpo,as
pernaseobra ço:
def desenha_forca(erros)
cabeca = " "
corpo = " "
pernas = " "
bracos = " "
puts " _______ "
puts " |/ | "
puts " | #{cabeca} "
puts " | #{bracos} "
puts " | #{corpo} "
puts " | #{pernas} "
puts " | "
puts "_|___ "
puts ""
end
Nocasodeousuáriotererradopelomenosumavez,desenhamosaca-
beça:
if erros >= 1
cabeca = "(_)"
end
Seeleerroupelomenosduasvezes,desenhamosumcorpinhogrande:
if erros >= 2
bracos = " | "
182
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 195

CasadoCódigo Capítulo15. ArteASCII:jogodaforca
corpo = "|"
end
Comtrêserrosdesenhamososbra ços:
if erros >= 3
bracos = "\\|/"
end
Por fim, com 4 erros desenhamos as pernas, ficando com a função
desenha_forca:
def desenha_forca(erros)
cabeca = " "
corpo = " "
pernas = " "
bracos = " "
if erros >= 1
cabeca = "(_)"
end
if erros >= 2
bracos = " | "
corpo = "|"
end
if erros >= 3
bracos = "\\|/"
end
if erros >= 4
pernas = "/ \\"
end
puts " _______ "
puts " |/ | "
puts " | #{cabeca} "
puts " | #{bracos} "
puts " | #{corpo} "
puts " | #{pernas} "
puts " | "
puts "_|___ "
puts ""
183
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 196

15.1. Melhorandonossainterfacecomousuário CasadoCódigo
end
Eainvocamosnocabe çalho:
def cabecalho_de_tentativa(chutes, erros, mascara)
puts "\n\n\n\n"
desenha_forca erros
puts "Palavra secreta: #{mascara}"
puts "Erros até agora: #{erros}"
puts "Chutes até agora: #{chutes}"
end
def avisa_acertou_palavra
puts "Parabéns, você ganhou!"
puts " ___________ "
puts " '._==_==_=_.' "
puts " .-\\: /-. "
puts " | (|:. |) | "
puts " '-|:. |-' "
puts " \\::. / "
puts " '::. .' "
puts " ) ( "
puts " _.' '._ "
puts " '-------' "
end
AgoranossojogoutilizaASCIIArtparapermitirumaexperiênciamais
agradávelaojogador:
_______
|/ |
|
|
|
|
|
_|___
184
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 197

CasadoCódigo Capítulo15. ArteASCII:jogodaforca
Palavra secreta: _____
Erros até agora: 0
Chutes até agora: []
_______
|/ |
| (_)
| \|/
| |
| / \
|
_|___
Palavra secreta: a___a
Erros até agora: 4
Chutes até agora: ["a", "b", "c", "d", "e"]
Parabéns, você ganhou!
___________
'._==_==_=_.'
.-\: /-.
| (|:. |) |
'-|:. |-'
\::. /
'::. .'
) (
_.' '._
'-------'
185
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 198

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 199

Capítulo16
Exercíciosextras:jogodaforca
Aquivocêencontraexercíciosextrasparasoltarsuaimagina çãoepraticar
lógicadeprograma çãonalinguagemRuby.
16.1 Melhorando o jogo da forca
1) Aoperder,mostreapalavrasecreta.
2) Simuleseujogoumaveznopapel.
3) Seganhou,mostreototaldeacertos.
4) Sevocêviracampeãoenãoeracampeãoatéagora,mostreumamensagem
deparabéns.
5) Sevocêbateuseuprópriorecorde,mostreumaoutramensagemdepara-
béns.
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 200

16.1. Melhorandoojogodaforca CasadoCódigo
6) Nãoleiaoarquivoderankdiversasvezes,armazene-onamemóriaem
algumavariável.
7) Seoarquivonãoexiste,nãomostreinforma çãonenhumasobreorank.
8) Oqueaconteceseoarquivodedicionáriotemumalinhaembrancono
fim?Nomeio?Comotestarfácil?Fa çacomquenãoexistanenhumpro-
blemacomarquivoscomlinhasembranconocome ço,meiooufim.
9) Senoarquivodedicionárioumapalavrapossuirespa çosantesoudepois,
remova-os.
10) Somenteletrasficamescondidascomo _.Todooresto(números,hífen,
pontuaçãoetc.)sãomostradoslogodecaraparaojogador.Paraissovocê
teráqueverificarseocaractereéumaletra. Sefor,confirmaemrela ção
aoschutes,senãoéumaletra,jámostra.
11) Aoinvésdetodavezrecriara Stringsecretacomasletrasnãochutadas
como _,tentemanterotempotodouma Stringcomo ___________.
Àmedidaqueousuáriochutaumaletra,troqueasletrasadequadasdessa
Stringeuse-aparaimprimireajudarousuário.Comissonossoalgo-
ritmopassaafazerapenasumla çoporcadaletraemvezdoqueelefaz
hoje(doisla ços).
12) Sevocêperderojogo,mostreumamensagemdefimdejogo:
def perdeu(palavra_secreta)
puts
puts "Puxa, você perdeu!"
puts "A palavra era **#{palavra_secreta}**"
puts
puts " _______________ "
puts " / \\ "
puts " / \\ "
puts "// \\/\\ "
puts "\\| XXXX XXXX | / "
puts " | XXXX XXXX |/ "
puts " | XXX XXX | "
188
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 201

CasadoCódigo Capítulo16. Exercíciosextras:jogodaforca
puts " | | "
puts " \\__ XXX __/ "
puts " |\\ XXX /| "
puts " | | | | "
puts " | I I I I I I I | "
puts " | I I I I I I | "
puts " \\_ _/ "
puts " \\_ _/ "
puts " \\_______/ "
end
16.2 Outros desafios
1) Considerequeumamáquinadecaixaeletrônicotemdiversasnotasde100,
50,20,10,5e1real. Armazenecadaquantidadeinicialemumavariável
(1de100,2de50,4de20,8de10,16de5e32de1).Pe çaparaousuário
umvalor,queéoquantoeledesejasacar.Apresenteparaeleasolu çãoque
utilizaomenornúmeropossíveldenotasparaentregar-lheodinheirode
queprecisa.Paraissotentesempreutilizarprimeiroasnotasmaiores.
2) Acadasaque,diminuadoseucaixaosvaloresdasnotasqueousuário
pediu.
3) Mudeseucaixaeletrônicoparapedirdiversasvezesaousuáriovaloresa
seremsacados.
4) Faça um programa que lê o arquivoentrada.txt e escreve para
saida.txt. Eledevecompactaroarquivodeentradadaseguintema-
neira:seumaletra(X)apareceumaúnicavez,escreva“1X”,seelaaparece
5vezesseguidas“5X”.Sealetraéumnúmero(porexemplo,umavezo
número5),escreva“1-5”.
5) Façaoprogramaquelêoarquivodesaídaedevolveoarquivodescom-
pactado.
189
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 202

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 203

Capítulo17
Foge-foge,umjogobaseadono
Pacman
17.1 Definindo a base do jogo e o mapa
QueremosdesenvolverumjogobaseadonofamosoPacman,ondeoherói
fogedefantasmasqueassombramsuavida.Nossojogo,brasileiro,sechama
foge-foge.Comodecostume,come çamosojogopedindoonomedenosso
usuário. Jásabemosquedevemosisolarapartedeinterfacecomousuário,
portantocriamosnosso ui.rb:
def da_boas_vindas
puts "Bem-vindo ao Foge-foge"
puts "Qual é o seu nome?"
nome = gets.strip
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 204

17.1. Definindoabasedojogoeomapa CasadoCódigo
puts "\n\n\n\n\n\n"
puts "Começaremos o jogo para você, #{nome}"
nome
end
Alógicadojogoem fogefoge.rb:
require_relative 'ui'
def joga(nome)
# nosso jogo aqui
end
def inicia_fogefoge
nome = da_boas_vindas
joga nome
end
Enosso main.rb,queiniciaojogo:
require_relative 'logic'
inicia_fogefoge
Precisamosdefinirnossomapa. Ojogopossuimurosondeoheróinão
podeandar,fantasmasqueca çamnossojogador,ojogadoremsiecaminhos
porondeelepodepassar trechossemnada.
ChamandoomurodeX,omapaaseguiréumexemplodequatrolinhas
equatrocolunas:
XXXX
X X
X X
XXXX
SechamarmosoheróideH,omapaaseguiréummapadequatrolinhas
equatrocolunas,comoheróinomeio:
XXXX
XH X
192
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 205

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
X X
XXXX
Jáchamandode Fumfantasma,temososeguintemapadifícildeganhar
válido:
XXXX
XH X
X FX
XXXX
Usandoessasdefini ções,oprimeiromapaválidoqueutilizaremosécom
umúnicofantasma. Vamoscriaroarquivo mapa1.txtaseguir. Nãose
esqueçadecolocarosespa çosembranconaslinhascujabordaéumespa ço
embranco.
XXXXX
X H X
X X X
X X X
X X
X
XXX
X
X F X
XXXXX
Ummapamaisinteressantecomdoisfantasmas, mapa2.txtseria:
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXXF F X
XXX XXX X
193
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 206

17.2. Arraydearray:matriz CasadoCódigo
XXX XXX X
XXX X
Estamosusandoletraspararepresentarummapaquenós,comoseres
humanos,conseguimoscompreender.Poderíamosusar0se1s,masseriamais
trabalhosoparaentendermosoqueestamosfazendonesseinstante,oquenão
énossofoco.
17.2 Array de array : matriz
Baseados no segundo mapa, podemos escrever uma função de lógica (
logic.rb)quelêtudoemuma stringequebracadalinhaemumarray
de strings:
def le_mapa(numero)
texto = File.read("mapa#{numero}.txt")
mapa = texto.split("\n")
end
Masqueporcariaéum "mapa#{numero}.txt”. Sim,eusouchatoe
gostodedarnomeamuitosbois. Nessecasoespecífico,seuma string
temumsignificado(umasemântica)outroquenãosejameramenteumtexto,
gostodedeixarissobemclaro.Pareceserumgostobobo,masdeixarclaroo
quealgoéfacilitamuitosuacompreensão.Porexemplo,oquesignificauma
variávelpessoa?Eumavariável usuarioLogado?Ambossãopessoas,masuma
éclaramentealgoespecialparameuprograma,elapossuiumsignificadopara
mim.Portanto, extract variablenele:
def le_mapa(numero)
arquivo = "mapa#{numero}.txt"
texto = File.read(arquivo)
mapa = texto.split("\n")
end
Carregamosomapaduranteojogo:
def joga(nome)
mapa = le_mapa(1)
end
194
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 207

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
Eomostramos:
mapa = le_mapa(1)
desenha mapa
Claro,acadanovarodadaousuáriopoderáandar. Paraadireita,es-
querda,cimaoubaixo. Devemossempreperguntarparaondeelequerir,
emnosso ui.rb:
def pede_movimento
puts "Para onde deseja ir?"
movimento = gets.strip
end
Duranteojogofazemosumla ço,mostrandoomapaeperguntando:
def joga(nome)
mapa = le_mapa(1)
while true
desenha mapa
direcao = pede_movimento
end
end
Precisamosimplementarafun ção desenhaemnosso ui.rb,queébem
simples:
def desenha(mapa)
puts mapa
end
Atéaquiusamossomenterecursosquejáconhecíamosparaleromapae
omovimentodenossojogador.Testamosojogoealeituraestáadequada:
Bem-vindo ao jogo do Pacman
...
Começaremos o jogo para você, Guilherme
XXXXX
X H X
X X X
195
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 208

17.3. Movimento CasadoCódigo
X X X
X X
X
XXX
X
X F X
XXXXX
Para onde deseja ir?
Chamamosumarraydearrays,umarrayde2dimensões,deumamatriz.
Pormaisquenamatemáticaumarraydeumadimensão(comumentecha-
madovetor)sejatambémchamadodematriz,nodesenvolvimentodesoft-
warecostumamosutilizarotermo arrayparaumadimensãoe matrizpara
duasoumaisdimensões.Mastomecuidado:oquetemoséumarraydear-
rayouumarrayde String?
17.3 Movimento
Nossaprimeirafuncionalidadedojogoenvolvepermitiraojogadormovi-
mentarseupersonagem.Queremosutilizarasmesmasteclasquejogosmo-
dernosutilizam: WASDparacima,esquerda,baixoedireitarespectivamente.
Mas como encontrar o jogador no mapa? Vamos varrer o mapa e
encontrá-lo:
def encontra_jogador(mapa)
for linha = 0..(mapa.size-1)
if mapa[linha].include? "H"
# achei!
end
end
# não achei!
end
Casoencontremosocaractere Hdentrodalinhadomapa,precisamos
procuraremqualcoluna,qualposi ção,eleestádentro:
def encontra_jogador(mapa)
for linha = 0..(mapa.size-1)
196
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 209

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
if mapa[linha].include? "H"
for coluna = 0..(mapa[linha].size-1)
if mapa[linha][coluna] == "H"
# achei!
end
end
end
end
# não achei!
end
17.4 Refatorando
Jávicódigofeio,masnossocódigoestáhorrendo.Cadalinhafazduas,três,
quatroouatémesmocincocoisas( if, [], [], ==,definirocaracteremágico
"H"namesmalinha).
Comecemosextraindoo "H",queéoherói:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
for linha = 0..(mapa.size-1)
if mapa[linha].include? caracter_do_heroi
for coluna = 0..(mapa[linha].size-1)
if mapa[linha][coluna] == caracter_do_heroi
# achei!
end
end
end
end
# não achei!
end
Agorapodemosextraira linha_atual:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
for linha = 0..(mapa.size-1)
linha_atual = mapa[linha]
if linha_atual.include? caracter_do_heroi
197
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 210

17.4. Refatorando CasadoCódigo
for coluna = 0..(linha_atual.size-1)
if linha_atual[coluna] == caracter_do_heroi
# achei!
end
end
end
end
# não achei!
end
Extraímosascondi ções:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
for linha = 0..(mapa.size-1)
linha_atual = mapa[linha]
heroi_esta_nessa_linha =
linha_atual.include? caracter_do_heroi
if heroi_esta_nessa_linha
for coluna = 0..(linha_atual.size-1)
heroi_esta_aqui = linha_atual[coluna] ==
caracter_do_heroi
if heroi_esta_aqui
# achei!
end
end
end
end
# não achei!
end
Agoravamospararparapensarumpoucomais.Comofuncionaomé-
todo include??Elepassacaractereacaractere,verificandoseo "H"estálá.
Seéissoqueelefaz,erefazemosissodentrodo if,nãoprecisamosdo if,
afinaljáfazemosonossopróprio forparaencontraraposi çãoadequada.A
variávelheroi_esta_nessa_linhavaiembora:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
198
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 211

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
for linha = 0..(mapa.size-1)
linha_atual = mapa[linha]
for coluna = 0..(linha_atual.size-1)
heroi_esta_aqui = linha_atual[coluna] ==
caracter_do_heroi
if heroi_esta_aqui
# achei!
end
end
end
# não achei!
end
17.5 Ov azio, o nulo
Sejáexisteummétodocomoo include?quedizseumcaractere(ou
String)estádentrodeuma String,seráquenãoexisteumquejádizem
qualposi çãoeleaparecepelaprimeiravez?Procuramosnadocumenta çãoe
encontramosométodo indexquefazexatamenteisso: devolveaposi ção
ondeocaractereestá,ounada( nil)casonãooencontre.Podemosusaressa
funçãoparaencontrarnossoherói:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
for linha = 0..(mapa.size-1)
linha_atual = mapa[linha]
coluna_do_heroi = linha_atual.index caracter_do_heroi
if coluna_do_heroi
# achei!
end
end
# não achei!
end
Vazio,ounulo,édefinidocomo nilemRuby.Nãodevemosnosconfundir
comuma Stringvazia:
string_vazia = ""
nada = nil
199
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 212

17.5. Ovazio,onulo CasadoCódigo
nulo = nil
vazio = nil
Podemosfazerum ifparaverificarovalorvaziotantousandoacompa-
ração:
if coluna_do_heroi != nil
# achei!
end
Quantocomum ifsimples.EmRuby,tudooquenãoénulonemfalso
éconsideradoverdadeiro:
if coluna_do_heroi
# achei!
end
Temosquetomarcuidadoquandotemosum nilemnossasmãos.Su-
ponhaporexemploqueumafun çãoretorneuma Stringou nil. Nesse
caso,setentarmoscalcularseutamanho:
def pega_nome
nil
end
nome = pega_nome
puts nome.size
Temosumerroque,porpadrão,paratodaaaplica ção:
NoMethodError: undefined method ` size' for nil:NilClass
Afinal,umvalorvazio,nulo,nãotemométodo sizecomouma String
tem.Tenhacuidadosemprequepermitiraexistênciadeum nilemseucó-
digo,esempreverifiqueoretornodeumafun çãocujadocumenta çãoindica
quepoderetornar nil.
200
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 213

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
17.6 Laço funcional básico
Nossocódigojáestámaiscompreensível,masaindapodemosmelhorar.Será
quenãoexisteumla çoquejánostraztantoocontador( linha),quantoo
valordaquelela ço?Senãoexistisse,eunãoperguntariaaqui?Talvez.Nesse
caso,existe. Existeummétodode Array(que Stringtambémtem)que
permitepassarporcada( each)elementosdele.Bastadizermoscomoquere-
moschamaressasvariáveis.Cadaelementoénossa linha_atual:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
mapa.each do |linha_atual|
# cade a linha?
coluna_do_heroi = linha_atual.index caracter_do_heroi
if coluna_do_heroi != -1
# achei!
end
end
# não achei!
end
Masqualonúmerodalinha? Usamosométodo each_with_index
paranosdaraposi ção( index)decadaelemento,quechamaremosde linha:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
mapa.each_with_index do |linha_atual, linha|
coluna_do_heroi = linha_atual.index caracter_do_heroi
if coluna_do_heroi != -1
# achei!
end
end
# não achei!
end
Essamaneiradeprogramar,ondechamamosummétodoepassamospara
eleumblocodecódigo(oconteúdodentrodo do)éola çomaisbásicodeuma
maneirafuncionaldeprogramaremRuby.
201
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 214

17.7. Extraindoaposição CasadoCódigo
17.7 Extraindo a posição
Agoraqueencontramosnossoherói,podemosretornarsuaposi ção,tantoa
linhaquantoacoluna. Tomebastantecuidadopoisestamosusandoofor-
matolinha/coluna, enãocoluna/linha. Vamoscolocaranossocódigono
fogefoge.rb:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
mapa.each_with_index do |linha_atual, linha|
coluna_do_heroi = linha_atual.index caracter_do_heroi
if coluna_do_heroi != -1
return [linha, coluna_do_heroi]
end
end
# não achei!
end
Opróximopassoéinvocarafun çãoemnossola çoprincipal:
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
Emovimentardeacordo.Paraisso,seousuáriodigitar W,devemossubir,
diminuindoem 1alinhaatual:
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
case direcao
when "W"
heroi[0] -= 1
end
Seeledigitar S,eledesce,aumentandoem 1alinhaatual:
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
202
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 215

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
case direcao
when "W"
heroi[0] -= 1
when "S"
heroi[0] += 1
end
Jánomovimentohorizontal,aumentamosumquandovamosparaadi-
reitaediminuímosumparaaesquerda:
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
case direcao
when "W"
heroi[0] -= 1
when "S"
heroi[0] += 1
when "A"
heroi[1] -= 1
when "D"
heroi[1] += 1
end
Faltaagorareposicionarnossojogadornomapa.Coloquemosoheróina
novaposi ção:
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
case direcao
when "W"
heroi[0] -= 1
when "S"
heroi[0] += 1
when "A"
heroi[1] -= 1
when "D"
heroi[1] += 1
203
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 216

17.7. Extraindoaposição CasadoCódigo
end
mapa[heroi[0]][heroi[1]] = "H"
Antesdemovimentá-lo,eleétiradodesuaposi ção,ondecolocamosum
espaçoembranco.Ficamoscomafun ção joga:
def joga(nome)
mapa = le_mapa(1)
while true
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
mapa[heroi[0]][heroi[1]] = " "
case direcao
when "W"
heroi[0] -= 1
when "S"
heroi[0] += 1
when "A"
heroi[1] -= 1
when "D"
heroi[1] += 1
end
mapa[heroi[0]][heroi[1]] = "H"
end
end
Testamosojogoeelefunciona!
XXXXX
X H X
X X X
X X X
X X
X
XXX
X
X F X
XXXXX
Para onde deseja ir?
204
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 217

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
D
XXXXX
X HX
X X X
X X X
X X
X
XXX
X
X F X
XXXXX
Para onde deseja ir?
Lembre-se:estamosusandoaletramaiúsculaparamover-nos,nãomi-
núscula!
17.8 Refatorando
Acomplexidadedafun ção jogaaumentourapidamente.Nosso casecom-
plicamuitoacompreensão,portantoextrairemosessecódigo.Oqueelefaz?
Eledefineanovaposi çãodoherói?Vamosdefini-lo:
def calcula_nova_posicao(heroi, direcao)
case direcao
when "W"
heroi[0] -= 1
when "S"
heroi[0] += 1
when "A"
heroi[1] -= 1
when "D"
heroi[1] += 1
end
heroi
end
Einvocarafun ção:
205
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 218

17.9. Passagemporreferênciaouvalor? CasadoCódigo
def joga(nome)
mapa = le_mapa(1)
while true
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
mapa[heroi[0]][heroi[1]] = " "
nova_posicao = calcula_nova_posicao heroi, direcao
mapa[nova_posicao[0]][nova_posicao[1]] = "H"
end
end
17.9 Passagem por referência ou v alor?
Paraverificarasomaqueefetuamosnoarray heroi,retornandoseunovo
valor,vamosimprimirasduasvariáveisquetemos:
def joga(nome)
mapa = le_mapa(1)
while true
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
mapa[heroi[0]][heroi[1]] = " "
nova_posicao = calcula_nova_posicao heroi, direcao
puts "Antes: #{heroi}"
puts "Depois: #{nova_posicao}"
mapa[nova_posicao[0]][nova_posicao[1]] = "H"
end
end
Rodamosojogoemovemosparaadireita:
...
D
Antes: [1, 3]
Depois: [1, 3]
...
206
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 219

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
Comoassim?Osdoisarraystêmomesmovalor?Ovalormovidoparaa
direita?Oqueestáacontecendoaqui?
Vamosolharcomcalmaasimula çãonamemóriadequandoinvocamos
afun ção calcula_nova_posicao,afinaléelaquemdevolveoarray. O
queacontecequandoinvocamosumafun çãocomparâmetros?Écriadauma
novavariável,comonomedoparâmetro,eelapossuiomesmovalorquea
variávelquefoipassadacomoargumento.
Issosignificaque,aopassarmos heroicomoargumento,pegamostodos
osvaloresde heroiecopiamosemumnovo array?Não.Sefizéssemos
isso,imagineinvocarumafun çãocomumarrayde1megacomoargumento.
Acadavezquechamamosumafun ção,eleteriaquecopiaresse1megade
algumamaneira(existemdiversastécnicasdeotimiza ção),masoconteúdo
maiscedooumaistardeseriacopiado!Megasemaismegas!Nadabom.
Setodavezquepassássemosumarraycomoargumentoelefossecopiado
porinteiro,otempodeprocessamentoeoconsumodememóriaseriamuito
alto.
Aomesmotempo,oqueéumarray? Éum“peda ção”dememóriaem
quecabeváriosvalores.Masoqueéumavariávelquereferenciaumarray?
Quandotemosumavariávelquereferenciaumarray,elapossuiumúnico
valor:umapontadorparaondeeleestá.Issoé,todavariávelpossuiumúnico
valor. Nocasodearrays,essevaloréumnúmeroquereferenciaolugarna
memóriaondeestãoascasinhasparacolocardiversosvalores.
Éjustamenteessevalorqueépassadocomoparâmetro.Issosignificaque,
quandopassamosumarraycomoargumento,oqueécopiadoéoseuen-
dereço,oapontador. Ovalordelenãoécopiado,etantoavariávelanterior
quantoanovaestãoapontandoparaomesmo afinalsóexisteum! array.
Qualquermudan çaquefizermosnessearrayafetaasduasvariáveis.Efoiisso
queaconteceu.Nossavariável heroiestáreferenciandoomesmoarrayque
o nova_posicao.
Passamosumareferênciaparanosso arraycomoargumento,nãopas-
samosumacópiadenossoarray.Essefoinossoerro.
Paracorrigi-lo,podemospedirparaoarrayserduplicado( dup)assim
queorecebemos:
207
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 220

17.10. Detecçãodecolisãocomomuroeofimdomapa CasadoCódigo
def calcula_nova_posicao(heroi, direcao)
heroi = heroi.dup
case direcao
when "W"
heroi[0] -= 1
when "S"
heroi[0] += 1
when "A"
heroi[1] -= 1
when "D"
heroi[1] += 1
end
heroi
end
Agorasim:
...
D
Antes: [1, 2]
Depois: [1, 3]
...
Jápodemostirarosdois puts.
17.10 Detecção de colisão com o muro e o fim do
mapa
Aindaexistemalgumassitua çõesquenãotratamos.Aprincipaldelasenvolve
batercomummuro.Nãopodemospermitirquenossoheróitenteandaronde
existeummuro. Pararesolverisso,podemosverificarsesuanovaposi ção
possuiummuroe,sesim,cancelaromovimento.
Agoraquetemosaposi çãoexataàqualiremosnosmovimentar,podemos
conferirseelaéummuroe,sefor,nãoandar:
def joga(nome)
mapa = le_mapa(1)
while true
208
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 221

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
mapa[heroi[0]][heroi[1]] = " "
nova_posicao = calcula_nova_posicao heroi, direcao
if mapa[nova_posicao[0]][nova_posicao[1]] == "X"
next
end
mapa[nova_posicao[0]][nova_posicao[1]] = "H"
end
end
Mascuidado!Sóqueroremoveroheróideseulugarcasoeletenhasido
posicionadonolugarnovo,ouseja,somenteseoremarcarmos. Portanto,
somentelimpamosaposi çãonomapacasoelenãotenhabatidonomuro:
def joga(nome)
mapa = le_mapa(1)
while true
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
nova_posicao = calcula_nova_posicao heroi, direcao
if mapa[nova_posicao[0]][nova_posicao[1]] == "X"
next
end
mapa[heroi[0]][heroi[1]] = " "
mapa[nova_posicao[0]][nova_posicao[1]] = "H"
end
end
Pronto!Nossojogojánãopermitemaismovimentarparadentrodeum
muro.Faltaverificarmosofimdomapa.Comofazerisso?
Ojogadornãopodesubirseestivernalinha 0,nemirparaaesquerdase
estivernalinha 0.Issoé,nãopodeirparaa nova_posicao[0] < 0 ,nem
209
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 222

17.11. Refatorandocom||e&& CasadoCódigo
nova_posicao[1] < 0 :
if nova_posicao[0] < 0
next
end
if nova_posicao[1] < 0
next
end
if mapa[nova_posicao[0]][nova_posicao[1]] == "X"
next
end
Também não podemos deixar o jogador passar para “baixo” da úl-
tima linha do mapa (mapa.size) nem para após a última coluna (
mapa[0].size):
if nova_posicao[0] < 0
next
end
if nova_posicao[1] < 0
next
end
if nova_posicao[0] >= mapa.size
next
end
if nova_posicao[1] >= mapa[0].size
next
end
if mapa[nova_posicao[0]][nova_posicao[1]] == "X"
next
end
Pronto,evitamosacolisãocommurosesairdomapa.
17.11 Refatorando com || e &&
Játemosaprimeirapartedenossojogofuncionando,afinalojogadorécapaz
deandarpelomapa. Masvamosmelhorarnossocódigoaindamaisantes
210
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 223

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
decontinuar,umavezquenossafun ção joganovamenteficoucomplexa
demais.
Apóscalcularanovaposi ção,temosdiversos ifs,quesãoequivalentes
aum switch;sãomuitascondi ções,algocomplicadodeentenderrapida-
mente.Vamosextrairumafun çãoquedizseaposi çãoéválida:
def posicao_valida?(mapa, nova_posicao)
if nova_posicao[0] < 0
return false
end
if nova_posicao[1] < 0
return false
end
if nova_posicao[0] >= mapa.size
return false
end
if nova_posicao[1] >= mapa[0].size
return false
end
if mapa[nova_posicao[0]][nova_posicao[1]] == "X"
return false
end
true
end
Masseriaaindamelhorsepudéssemosagruparalgumasdessascondi ções.
Porexemplo, seaposi çãodalinhaformenorque 0,oumaiorouigualao
númerodelinhas.
def posicao_valida?(mapa, nova_posicao)
if nova_posicao[0] < 0 OU nova_posicao[0] >= mapa.size
return false
end
if nova_posicao[1] < 0 OU nova_posicao[1] >= mapa[0].size
return false
end
if mapa[nova_posicao[0]][nova_posicao[1]] == "X"
return false
end
211
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 224

17.11. Refatorandocom||e&& CasadoCódigo
true
end
NoRubyépossívelfazeracondi ção OUcomooperador ||:
def posicao_valida?(mapa, nova_posicao)
if nova_posicao[0] < 0 OU nova_posicao[0] >= mapa.size
return false
end
if nova_posicao[1] < 0 OU nova_posicao[1] >= mapa[0].size
return false
end
if mapa[nova_posicao[0]][nova_posicao[1]] == "X"
return false
end
true
end
|| e &&
Assimcomoooperador ||(OR)retornaverdadeiroseaprimeiraou
segundacondi çãoforverdadeira,ooperador &&(AND)retornaverda-
deirosomenteseambasforemverdadeiras.
def posicao_valida?(mapa, nova_posicao)
if nova_posicao[0] < 0 || nova_posicao[0] >= mapa.size
return false
end
if nova_posicao[1] < 0 || nova_posicao[1] >= mapa[0].size
return false
end
if mapa[nova_posicao[0]][nova_posicao[1]] == "X"
return false
end
true
end
Pronto,nossafun çãojáestámaisdireta.Seextrairmosalgumasvariáveis
ocódigoficabemmaislegível:
212
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 225

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
def posicao_valida?(mapa, nova_posicao)
linhas = mapa.size
colunas = mapa[0].size
estourou_linha =
nova_posicao[0] < 0 || nova_posicao[0] >= linhas
estourou_coluna =
nova_posicao[1] < 0 || nova_posicao[1] >= colunas
if estourou_linha || estourou_coluna
return false
end
if mapa[nova_posicao[0]][nova_posicao[1]] == "X"
return false
end
true
end
Porfim,renomeamos nova_posicaopara posicao:
def posicao_valida?(mapa, posicao)
linhas = mapa.size
colunas = mapa[0].size
estourou_linha = posicao[0] < 0 || posicao[0] >= linhas
estourou_coluna = posicao[1] < 0 || posicao[1] >= colunas
if estourou_linha || estourou_coluna
return false
end
if mapa[nova_posicao[0]][nova_posicao[1]] == "X"
return false
end
true
end
213
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 226

17.12. Ducktypingnaprática CasadoCódigo
Nossafun ção jogainvocaa posicao_valida?:
def joga(nome)
mapa = le_mapa(1)
while true
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
nova_posicao = calcula_nova_posicao heroi, direcao
if !posicao_valida? mapa, nova_posicao
next
end
mapa[heroi[0]][heroi[1]] = " "
mapa[nova_posicao[0]][nova_posicao[1]] = "H"
end
end
17.12 Duck typing na prática
Atéagorausamosumarrayde Stringspararepresentarnossomapa.Pode-
ríamosusarumarraydearrays.Comononossocasoutilizamosletras,não
pareceexistirnenhumavantagememutilizarnúmeros(oucaracteressoltos
emumarray).Mastambémnãohánenhummétodode Stringqueestamos
utilizando.Tudoindicaqueaúnicacoisaqueutilizaremoséextrairovalorna
posiçãodeuma String,como [],eotamanhodeumalinhacomo size.
Comotantoarrayquanto Stringrespondemaessesmétodos,tantofazpor
enquantonossaabordagem.
Tantofazseéum Arrayou String,sómepreocuposeeleresponde
aocomportamentodequepreciso. Nomundoanimalexisteumaanalogia
famosa(eumtantoestranha)compatos:seelefaz quackcomoumpato,não
meimportaseéumpato,elefaz quackcomoumpato.
Porumlado,oartifíciodeinvocarumcomportamento,independentedo
tipoqueestamosutilizando(chamadode duck typigin),époderoso,maspode
trazerproblemas.Ométodo sizedeum Arraypodetrazeronúmerode
214
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 227

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
elementosdele,ode Stringtambém. Portanto,qualquercoisaquetem
sizemesatisfaz.Será?
Maseseeutenhoumtipochamado Product(Produto),cujotamanho
físicoométodo sizedevolve? sizeemumcontextotemumsignificado,
emoutrotemoutro.Boasorte.
Afraseoriginaldo duck typingera When I see a bird that walks like a duck
and swims like a duck and quacks like a duck, I call that bird a duck..Emtradu-
çãolivre,“Quandovejoumpássaroqueandacomoumpato,nadacomoum
patoegrasnacomoumpato,euchamoessepássarodepato”(JamesWhit-
combRiley).Oproblemaéquemuitodesenvolvedor(inclusiveowikipedia)
interpretaissocomoumaabstra çãototaldatipagem,emumafraseresumida
a“Seandacomoumpato,egrasnacomoumpato,éumpato”.
Repareadiferen çaentreaoriginalearesumida.Nafraseoriginalainda
nospreocupamoscomatipagemdaquilocomqueestamostrabalhando:
aindatemqueserumservivo,maisainda,umanimal,maisainda,umpás-
saro.Seumhomemgrasna,andaenadacomoumpato,elenãoéumpato.E
éaiquemoramoriscoeavantagemdo duck typingemRuby:elenãoverifica
nadadatipagem,eletrabalhacomaversãoreduzidadafrase,enãoaoriginal.
Filosoficamente,nãoexiste“verdade”ou“mentira”nafraseoriginalouresu-
mida.Existemconsequênciaspositivasenegativasdetodafuncionalidadede
umalinguagem,éimportantesempreaprendermostodaselas.
Linguagenscom duck typingnosalegramaopermitirtaisinvoca çõeseao
mesmotempopecamemnãonosprotegeremdeerroscomoesses.Nãosóum
programacomum Productrodaria,comooseuresultadoseriatotalmente
inesperado boasorte.
Tomecuidadocomailusãoqueo duck typingàsvezesnospassa.Nãoseja
enganadoquandoensinaremsomenteoladopositivodeumafuncionalidade
deumalinguagem.Sempreaprendemosobomeoruimparatomarnossas
decisõesconscientemente.Esseéofocodessematerial.Nestecasoatual,você
nãoquersabero tamanhodequalquercoisa,vocêquersaberotamanhode
seumapa,eissoimplicaemumsignificado(umasemântica)bemespecífica,
quealinguagemRubynãofornece.Poroutrolado,elapermitetrocarumtipo
poroutro“semnospreocupar”muito.
215
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 228

17.13. forixforlinha CasadoCódigo
17.13 for i x for linha
Umapráticamuitocomumnomundodeprograma çãoéaabrevia çãoepa-
dronizaçãodonomedevariáveis.Sãodiversosos totsquesãototais,ouos
s_nomequesão stringnome.OpadrãousadopordesenvolvedoresRuby
éodenãoutilizarumcaracterenocome çodeumavariávelparaindicarqual
otipodaquelavariável.
Poroutrolado,existemnomesdemétodosevariáveisabreviadoseoutros
não. Comoboapráticaeregrageral,nãoabrevie. Quantomaiscurto,mais
ambíguoemaiorachancedeconflito. Comocitadoanteriormente, size
éambíguo,mas tamanhoe quantidade_de_elementosnão.Tudode-
pendedoquevocêprecisa,mascomoregrageraleviteaambiguidadeeo
possívelerrododesenvolvedorjustamentepornãoentenderoqueestáfa-
zendo.
Umexemploclássicodeabrevia çãoéousodavariável iparaumla ço:
for i = 0..(mapa.size-1)
puts mapa[i]
end
Seocódigodentrodeseula çoutilizaravariávelquecriouparaalgoim-
portante,nãodeixeseunomecomoummero i,defina-acomovalorreal
queelatem,comseusignificadodentrodocontextoatual:
for linha = 0..(mapa.size-1)
puts mapa[linha]
end
Nãofoisemquererqueatéagoranãovimosnenhum for i.Emtodos
osinstantesquefizemosumla ço,asvariáveispossuíamalgumsignificado
realparanossaaplica ção,eaodarmosumnomereal,deixamosclaroparao
próximodesenvolvedoroqueaquelavariávelrepresenta.
17.14 Resumindo
Adefini çãodeumformatodeentradaesaídaéumpassofundamentalpara
todoprogramaquevaigravardadosemalgumlugar.Essesarquivosdetexto
216
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 229

CasadoCódigo Capítulo17. Foge-foge,umjogobaseadonoPacman
sãosimplesmasjáimplicamementendermoscomofuncionaoprocessode
inpute output(IO).
Vimoscomodefinirarraysdearrays,apesardeusarmosatéagoraum
arrayde Strings.Fomoscapazesdemovimentarnossojogador,entendero
quesignificaovazio,onulo( nil),utilizarumla çofuncionalbásico( each).
Outrabasedaprograma çãofoiapresentadaaqui: apassagemdeparâ-
metrosporvaloreporreferência. Refatoramosnossocódigoparausaros
operadoreschamadosde short-circuit, :&&e ||. Porfim,vimosquaissão
asimplica çõespositivasatéagoraeocuidadoquedevemostomarcom duck
typing.
217
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 230

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 231

Capítulo18
Botandoosfantasmaspara
correr:arraysassociativos,duck
typingeoutros
18.1 Array associativo: case e+1,-1
Jáfalamosanteriormentequesequênciasde ifs,eousode casessãopos-
síveis code smells.Elesindicamquepodeestarpresentealgosujo,quepode
atrapalharamanuten çãodocódigooufacilitaroaparecimentodenovosbugs.
Nossafun ção calcula_nova_posicaodemonstraexatamenteestece-
nário:
def calcula_nova_posicao(heroi, direcao)
heroi = heroi.dup
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 232

18.1. Arrayassociativo:casee+1,-1 CasadoCódigo
case direcao
when "W"
heroi[0] -= 1
when "S"
heroi[0] += 1
when "A"
heroi[1] -= 1
when "D"
heroi[1] += 1
end
heroi
end
Comomudarnossocódigoparaevitaresse case? Reparequeoque
fazemosaquiébasicamentemapearumamudan çadeposi çãoparacadatecla,
eamudan çaéfeitatantonalinha(posi ção 0doarray)quantonacoluna
(posição 1).
def calcula_nova_posicao(heroi, direcao)
heroi = heroi.dup
case direcao
when "W"
heroi[0] -= 1
heroi[1] += 0
when "S"
heroi[0] += 1
heroi[1] += 0
when "A"
heroi[0] += 0
heroi[1] -= 1
when "D"
heroi[0] += 0
heroi[1] += 1
end
heroi
end
Podemospadronizarmaisainda,utilizandosomentesomas,sejadeum
númeropositivoounegativo:
220
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 233

CasadoCódigo Capítulo18. Botandoosfantasmasparacorrer:arraysassociativos,duck...
def calcula_nova_posicao(heroi, direcao)
heroi = heroi.dup
case direcao
when "W"
heroi[0] += -1
heroi[1] += 0
when "S"
heroi[0] += 1
heroi[1] += 0
when "A"
heroi[0] += 0
heroi[1] += -1
when "D"
heroi[0] += 0
heroi[1] += 1
end
heroi
end
Podemostambémpadronizarcriandoduasvariáveis, anda_linhae
anda_coluna:
def calcula_nova_posicao(heroi, direcao)
heroi = heroi.dup
case direcao
when "W"
anda_linha += -1
anda_coluna += 0
when "S"
anda_linha += +1
anda_coluna += 0
when "A"
anda_linha += 0
anda_coluna += -1
when "D"
anda_linha += 0
anda_coluna += +1
end
heroi[0] += anda_linha
221
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 234

18.1. Arrayassociativo:casee+1,-1 CasadoCódigo
heroi[1] += anda_coluna
heroi
end
MasGuilherme,seucódigoestáaindamaiorqueoquepossuíamosantes.
Éverdade,eleestámaior,masmaisclaro.Eledizque,sevocêmepassade-
terminadocaractere,eufa çovocêandarumnúmerodeterminadodelinhas
ecolunas,issoé,eu mapeioumaletra(umachave),paraumnúmero(um
valor).
Wanda-1e0.Sanda+1e0.Aanda0e-1.Danda0e+1.Eucrioumaco-
nexãoentreumachave(nessecaso,ocaractere)eumvalor(oquantoeleanda
emcadadimensão,linhaecoluna).Adivinha?Rubyjátemessaestrutura,al-
guémquemapeiaalgoparaoutracoisa,assimcomoumdicionáriomapeia
palavrasparasuasdefini ções. Aquiumdicionáriomapeará,conectaráum
caracterecomoquantodevemosandar:
heroi = heroi.dup
movimentos = {
"W" => [-1, 0],
"S" => [+1, 0],
"A" => [0, -1],
"D" => [0, +1]
}
Usamosodicionáriocomosefosseumarray,afinaleleéumarray,mas
umarrayqueassociachaveevalor,um array associativo:
heroi = heroi.dup
movimentos = {
"W" => [-1, 0],
"S" => [+1, 0],
"A" => [0, -1],
"D" => [0, +1]
}
movimento = movimentos[direcao]
heroi[0] += movimento[0]
heroi[1] += movimento[1]
222
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 235

CasadoCódigo Capítulo18. Botandoosfantasmasparacorrer:arraysassociativos,duck...
Issoé,trocamosnosso caseousequênciade ifsporumarrayassoci-
ativo:
def calcula_nova_posicao(heroi, direcao)
heroi = heroi.dup
movimentos = {
"W" => [-1, 0],
"S" => [+1, 0],
"A" => [0, -1],
"D" => [0, +1]
}
movimento = movimentos[direcao]
heroi[0] += movimento[0]
heroi[1] += movimento[1]
heroi
end
Existeumaboaeválidadiscussãoaqui,seessarefatora çãoemsiéjustifi-
cável.Ocódigofinalémaisexplícito,masutilizamosumartifícioparachegar
aondequeríamos.Nessecódigo,porexemplo,oqueaconteceseutilizarmos
umateclainválida?Enocódigoanterior,oqueaconteceria?
Claro,tratamentodeteclainválidadeveserfeitodequalquermaneira,
masautiliza çãodedicionários(arraysassociativos,mapasetc.)comoinstru-
mentoparaexecu çãodelógicadenegóciostemquesertratadacomcuidado.
Pensesempreseocódigofinaljustificousuautiliza ção.
Acreditoqueocódigononossoexemploatualémaisexplícitonoqueestá
fazendoequantoaoresultadofinaldafun ção.Masnãoacreditoquearrays
associativospossamserabusadoscomorecursológico. Comoregrageral,
verifiqueaquantidadeextrade ifsquevaiadicionaraoseucódigosomente
porusarumarrayassociativo.Nofinaldascontas,valeuapena?
18.2 Movimento dos fantasmas : o desafio no
duck typing
Chegouahoradenossosinimigossemoverem. Come çaremosalterando
nossocódigoparaqueomapacarregadosejaosegundo:
223
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 236

18.2. Movimentodosfantasmas:odesafionoducktyping CasadoCódigo
def joga(nome)
mapa = le_mapa(2)
# ...
end
Nofimdenossajogada,movemososfantasmas:
def joga(nome)
mapa = le_mapa(2)
while true
# ...
move_fantasmas mapa
end
end
Paraoprimeiropassode“inteligência”denossoinimigo,faremoscom
queosfantasmasandemsempreparaadireita.Comofazerisso?Queremos
pegartodososfantasmaseandarumacasaparaadireita. Quebremosessa
afirmação,comocrian ças,empassosbásicosparacadaumadasfrases:
1) Queremospegartodososfantasmas;
2) eandarumacasaparaadireita.
Ótimo,primeiroqueremostodososfantasmas.Comoencontrá-los?Po-
demosvarrernossoarraydestrings,procurandoocaractere F.Paraisso,
primeiropassamosportodasaslinhas:
def move_fantasmas(mapa)
caracter_do_fantasma = "F"
mapa.each_with_index do |linha_atual, linha|
end
end
Agorapassamosporcadacaracteredeumalinha:
def move_fantasmas(mapa)
caracter_do_fantasma = "F"
224
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 237

CasadoCódigo Capítulo18. Botandoosfantasmasparacorrer:arraysassociativos,duck...
mapa.each_with_index do |linha_atual, linha|
linha_atual.each_with_index do |caractere_atual, coluna|
end
end
end
Verificamosseeleéumfantasmae,sesim,movemos:
def move_fantasmas(mapa)
caracter_do_fantasma = "F"
mapa.each_with_index do |linha_atual, linha|
linha_atual.each_with_index do |caractere_atual, coluna|
eh_fantasma = caractere_atual == caracter_do_fantasma
if eh_fantasma
move_fantasma
end
end
end
end
Agora que encontramos todos eles, precisamos implementar o
move_fantasma com o qual o fazemos andar. Primeiro o tiramos da
posiçãoatual:
def move_fantasma(mapa, linha, coluna)
mapa[linha][coluna] = " "
end
Movemosparadireita:
def move_fantasma(mapa, linha, coluna)
mapa[linha][coluna] = " "
linha += 0
coluna += 1
end
Eocolocamosnanovaposi ção:
def move_fantasma(mapa, linha, coluna)
mapa[linha][coluna] = " "
225
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 238

18.2. Movimentodosfantasmas:odesafionoducktyping CasadoCódigo
linha += 0
coluna += 1
mapa[linha][coluna] = "F"
end
Aoinvocar,passamososparâmetrosnecessários:
move_fantasma mapa, linha, coluna
Pronto.Nossosfantasmaspodemandar.Vamostestarumarodada:
fogefoge.rb:31:in ` block in move_fantasmas':
undefined method ` each_with_index' for
"XXXXXXXXX":String (NoMethodError)
Oqueacontece? Stringnãopossuiométodo each_with_index?
Nemtudoquepareceumpatoéumpato.Anteseuqueriaalguémcom each,
sizee []. Agoraeuquerocom each_with_index. Euenganeiamim
mesmo,mentiparamimquandodissequequeriaalguémqueseparecesse
comumarray,queuma Stringbastava.Eujáestavaatreladoàexistência
esignificadodetrêsmétodosdeumarray,agoraestouaquatro.Nãoparece
serpoucacoisaosuficienteparadizerqueeuqueriasomentealguemquese
comportassecomoumarray.Euqueriaumarray,estoutriste.
Deveríamostertrocadoantes?Agora?Nuncadeveríamostertrabalhado
com String?Adiscussãoélongaecomótimosargumentosparaosdoisla-
dos.Paranossoaprendizadoesseéomomentoidealparaefetuarmosatroca,
evisualizarmosavantagemeumaprimeiradesvantagemdousode duck ty-
ping.Asegundadesvantageméquandoocódigoroda,eoefeitoéinesperado.
Agrandevantagemeraatéagoranãoterprecisadosepreocuparcomisso.
Oquefazerparacorrigirnossoproblema? Umasolu çãoseriaaolero
mapa,transformaraslinhasde Stringsem Arraysdecaractere,utilizando
ométodo charsemcadalinha. Masaimpressãodeumarraydecaracte-
resficariahorrível,teríamosquereconcatenaroscaracteresparaformaruma
String.Notequerealmentequempareceumpatonãoéumpato. T odomo-
mentoqueusamosnossomapa,sabemosqueeleeraumarrayde String.
Mudarotipoémudartudo,nãoémudarpouco.
Nossa solução será, portanto, simples. Ao precisarmos do método
each_with_indexinvocaremosométodo chars:
226
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 239

CasadoCódigo Capítulo18. Botandoosfantasmasparacorrer:arraysassociativos,duck...
def move_fantasmas(mapa)
caracter_do_fantasma = "F"
mapa.each_with_index do |linha_atual, linha|
linha_atual.chars.each_with_index do |caractere_atual,
coluna|
eh_fantasma = caractere_atual == caracter_do_fantasma
if eh_fantasma
move_fantasma mapa, linha, coluna
end
end
end
end
Agorasim,rodamosojogo,movemosumaparaaesquerdaetemosos
fantasmasandandoumacasaparaadireita:
...
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXXF F X
XXX XXX X
XXX XXX X
XXX XPara onde deseja ir?
A
XXXXXXXXX
XH X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
227
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 240

18.3. Movimentodosfantasmas:reutilizaçãodefun ção CasadoCódigo
X X X X
XXX F FX
XXX XXX X
XXX XXX X
XXX X
Para onde deseja ir?
Asacadado duck typingéqueeleégenialaopermitirqueointerpretador
nãosepreocupecomatipagemnememtempodecompila ção(naimple-
metaçãopadrãodoRuby,compila çãoéquandoelevalidaasintaxedoseu
arquivo),nemduranteaexecu çãodocódigo.Ointerpretadorsomenteestá
preocupadoseovalorreferenciadopelanossavariávelrespondeàfun ção,ao
método,emquestão.Sesim,ótimo.
Poroutrolado,nóscomodesenvolvedoresestamospreocupadoscomati-
pagemaoescrevermosnossocódigo.Nãoimportaterumvalorqueresponda
aométodo sizesedaquiapoucoprecisodométodo each_with_index,
oqueeuqueroagoraéalguémquesecomportequasecomoum array,al-
guémquetenhaosmaisemaismétodosde array.Éarriscadoafirmarque
estamostotalmenteatreladosaotipoemsi,masumavezqueestamossubor-
dinadosaosignificadodométodoqueinvocamos,estamosatreladosaalgo
alémdoquesomentesuaexistência,porémointerpretadornãoestápreo-
cupadocomotipo.AssimpodemosdefiniradinâmicadetiposnoRuby:o
interpretadornãosepreocupacomeles,nósnospreocupamossempreque
precisamosescreveroualterarnossocódigo.
18.3 Movimento dos fantasmas : reutilização de
função
Masseandarmosnovamente,agoraparabaixo,osfantasmasmovemmais
umparaadireita,entrandoemcontatocomomuro.
...
XXXXXXXXX
X X
XHX XXX X
X X X X
228
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 241

CasadoCódigo Capítulo18. Botandoosfantasmasparacorrer:arraysassociativos,duck...
X X X X
X X
XXX XX X
X X
X X X X
XXX F FX
XXX XXX X
XXX XXX X
XXX X
Para onde deseja ir?
S
XXXXXXXXX
X X
X X XXX X
XHX X X
X X X X
X X
XXX XX X
X X
X X X X
XXX F F
XXX XXX X
XXX XXX X
XXX X
Faltouvalidarmosaposi çãodenossosfantasmas. Játemosafun ção
posicao_valida?,bastainvocá-laverificandoseoresultadoéválidoantes
demoverofantasma.Come çamoscriandoanovaposi çãoemumarray:
def move_fantasma(mapa, linha, coluna)
posicao = [linha, coluna + 1]
end
Sóalteramososvaloresdenossomapaseaposi çãoforválida:
def move_fantasma(mapa, linha, coluna)
posicao = [linha, coluna + 1]
if posicao_valida? mapa, posicao
mapa[linha][coluna] = " "
mapa[posicao[0]][posicao[1]] = "F"
229
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 242

18.4. Fantasmacontrafantasma? CasadoCódigo
end
end
Casoaposi çãonãosejaválida,ofantasmaficaparado.Testamosnosmo-
vimentarduasvezeseagoraofantasmaficaencostadonaparede,nãopassa
porela:
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXX F FX
XXX XXX X
XXX XXX X
XXX X
Para onde deseja ir?
D
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXX F FX
XXX XXX X
XXX XXX X
XXX X
18.4 Fantasma contra fantasma?
Seandarmosumquartopasso,omapasetorna:
230
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 243

CasadoCódigo Capítulo18. Botandoosfantasmasparacorrer:arraysassociativos,duck...
...
XXXXXXXXX
X X
X X XXX X
X X X X
XH X X X
X X
XXX XX X
X X
X X X X
XXX FX
XXX XXX X
XXX XXX X
XXX X
Oqueaconteceu? Umdosfantasmassumiu. Aconteceque,enquanto
umdosfantasmasficouparado,ooutrotomouseulugar. Comisso,perde-
mosumdeles. Devemosproibirumfantasmadeandarparaaposi çãode
outrofantasma.Asolu çãoinicialénãopermitirqueeleandeparaumacasa
ondejáexisteum Fmarcado.Aliás,nãofazsentidoojogadoriremdire ção
aofantasma.Portantoalteramosnossafun çãode posicao_valida?para
conferirseelapossuimuro( X)oufantasma( F):
if mapa[posicao[0]][posicao[1]] == "X"
return false
end
if mapa[posicao[0]][posicao[1]] == "F"
return false
end
Opa,seestamosusandoessaposi çãoduasvezes, extract variableficamais
claro:
valor_local = mapa[posicao[0]][posicao[1]]
if valor_local == "X" || valor_local == "F"
return false
end
Agorasim,apósandardiversospassosparaadireitaosfantasmasnão
brigammais,ficamencostadosumaooutro:
231
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 244

18.5. Resumindo CasadoCódigo
XXXXXXXXX
X HX
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXX FFX
XXX XXX X
XXX XXX X
XXX X
18.5 Resumindo
Vimoscomofuncionaodicionário,umarrayassociativo,etivemosqueto-
marcuidadocommudan çasde+1e-1,algoextremamenteperigosoempro-
gramação.Entendemosmelhoroquesignificao duck typingesuavantagem
alémdecorrigirumbugquesurgiunojogo,ondedoisfantasmasocupavam
amesmaposi ção.Vimosqueoducktypingpermitequeointerpretadorfique
despreocupadoemrela çãoàtipagem,masquenósaindanospreocupamos
comosignificadoeexistênciadosmétodos,portantocomquemosdefiniu,
seustipos.Vimostambémquetantobugsquantofuncionalidadessãodescri-
tosatravésdeestruturasdelógica,comcontroledefluxoela ços.
232
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 245

Capítulo19
Matrizesememória
19.1 Teletransportando fantasmas : cuidados a
tomar com a memória
Aindafaltaumpoucomaisdeinteligênciaemnossosfantasmas. Elestêm
queandarparaqualquerumadasquatrodire ções,aleatoriamente,esempre
lembrandoquesópodemandaremespa çosválidos.
Comoimplementarisso? Teremosquemudarnosso move_fantasma
paraescolherumanova posicaoválida.Nossocódigoatualsimplesmente
moveofantasmaparaadireita:
def move_fantasma(mapa, linha, coluna)
posicao = [linha, coluna + 1]
if posicao_valida? mapa, posicao
mapa[linha][coluna] = " "
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 246

19.1. Teletransportandofantasmas:cuidadosatomarcomamemória CasadoCódigo
mapa[posicao[0]][posicao[1]] = "F"
end
end
Primeirocalculamosumlado:
def posicoes_validas_a_partir_de(mapa, posicao)
posicoes = []
baixo = mapa[posicao[0] + 1][posicao[1]]
end
Agoraverificamosseelaéválida,adicionandoaonossoarray:
def posicoes_validas_a_partir_de(mapa, posicao)
posicoes = []
baixo = mapa[posicao[0] + 1][posicao[1]]
if posicao_valida? baixo
posicoes << baixo
end
end
Fazemosamesmacoisaparaadireita:
def posicoes_validas_a_partir_de(mapa, posicao)
posicoes = []
baixo = mapa[posicao[0] + 1][posicao[1]]
if posicao_valida? baixo
posicoes << baixo
end
direita = mapa[posicao[0]][posicao[1] + 1]
if posicao_valida? direita
posicoes << direita
end
end
Paracimaeparabaixo:
def posicoes_validas_a_partir_de(mapa, posicao)
posicoes = []
# ...
234
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 247

CasadoCódigo Capítulo19. Matrizesememória
cima = mapa[posicao[0] - 1][posicao[1]]
if posicao_valida? cima
posicoes << cima
end
esquerda = mapa[posicao[0]][posicao[1] - 1]
if posicao_valida? esquerda
posicoes << esquerda
end
end
Porfim,retornamosnossoarray:
def posicoes_validas_a_partir_de(mapa, posicao)
posicoes = []
# ...
posicoes
end
Játemosnossasposi çõesválidasparaofantasma. Agoraprecisamos
utilizá-las:
def move_fantasma(mapa, linha, coluna)
posicoes = posicoes_validas_a_partir_de mapa, [linha, coluna]
posicao = # escolhe uma posicao
mapa[linha][coluna] = " "
mapa[posicao[0]][posicao[1]] = "F"
end
Faremosofantasmaseguiraprimeiraposi çãopossível:
def move_fantasma(mapa, linha, coluna)
posicoes = posicoes_validas_a_partir_de mapa, [linha, coluna]
posicao = posicoes[0]
mapa[linha][coluna] = " "
mapa[posicao[0]][posicao[1]] = "F"
end
Masprecisamosverificarqueexistealgumaposi çãoparaaqualmover,
claro.Perguntamosaonossoarrayseeleestávazio:
235
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 248

19.1. Teletransportandofantasmas:cuidadosatomarcomamemória CasadoCódigo
def move_fantasma(mapa, linha, coluna)
posicoes = posicoes_validas_a_partir_de mapa, [linha, coluna]
if posicoes.empty?
return
end
posicao = posicoes[0]
mapa[linha][coluna] = " "
mapa[posicao[0]][posicao[1]] = "F"
end
Testamosagoraeosfantasmasandam,umparabaixo,umparaadireita:
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXXF F X
XXX XXX X
XXX XXX X
XXX X
Para onde deseja ir?
D
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXX FX
XXX XXX X
236
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 249

CasadoCódigo Capítulo19. Matrizesememória
XXX XXX X
XXX F X
19.2 Corrigindo o teletransporte
Masaconteceumuitomaisdoqueisso.Ofantasmadaesquerdaseteletrans-
portou?Teletransportevale?Nãovale.Oqueestáacontecendo?Vamosana-
lisarmelhoroqueacontececomnossamatrizacadamovimentodeumfan-
tasma.No move_fantasmavamosimprimirnossomapatemporário:
def move_fantasma(mapa, linha, coluna)
# ...
puts "Movendo fantasma encontrado em #{linha} #{coluna}"
desenha mapa
end
Rodamosojogoeacompanhamosoprimeiromovimento:
Ola çodemoverfantasmaspercorrenossoarrayde Stringsatéencon-
trarnossoprimeirofantasmanadécimalinha,quartacoluna( 9, 3). Ele
podeandarparabaixo,portantonossoalgoritmodemovimentodesloca-o
parabaixo:
Movendo fantasma encontrado em 9 3
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXX F X
XXXFXXX X
XXX XXX X
XXX X
237
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 250

19.2. Corrigindooteletransporte CasadoCódigo
Aíoprogramacontinuavarrendoalinha,encontranossosegundofan-
tasma,namesmalinha,sétimacoluna( 6),quenãopodeirparabaixo,eacaba
porirparaadireita:
Movendo fantasma encontrado em 9 6
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXX FX
XXXFXXX X
XXX XXX X
XXX X
Atéaquioalgoritmorodacomooesperado. Oqueaconteceaseguiré
surpreendente:
Movendo fantasma encontrado em 10 3
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXX FX
XXX XXX X
XXXFXXX X
XXX X
Onossoalgoritmoprocurafantasmasnalinhaseguinteeencontraopri-
meironovamente,movendo-omaisumavezparabaixo!Eoprocessoconti-
nua,descendo,descendo:
238
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 251

CasadoCódigo Capítulo19. Matrizesememória
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXX FX
XXX XXX X
XXX XXX X
XXXF X
Aconteceque,aoutilizarmosomesmopeda çodememória,amesmama-
triz,pararepresentarduascoisas,efazercomqueelepossamudarseuvalor,
issoé,elesejamutável( mutable),permitimosquenossoalgoritmofuncio-
nassedeumamaneiraquenãodesejávamos.Elealteraamatrizdeposi ções
atuais,maselapassaarepresentartantoofuturoquantoopassadodenossos
fantasmas. Valoresmutáveis(ematrizescostumamsertratadasassim)são
perigososporisso:tomecuidadoaoalterá-las.
Comoresolvernossoproblema?Precisamossepararomapa,querepre-
sentaasitua çãodosfantasmasnoiníciodarodada,dasitua çãodomapaque
representaosfantasmasapósseusmovimentos.Comofazerisso?Podemos
criarumnovoarrayde Strings,sócomosmuroseosheróis,ecopiaros
fantasmasumaum,àmedidaqueelessemovem.
Seolharmosamatrizantigaparaprocurarosfantasmas,vamosencontrá-
lossomenteumavez,evitandoobugatual.
Masesperauminstante,Guilherme. Ofantasmadesceutudo,maspor
queelenãofoitudoparaadireita?Reparequenofimdoturnoeletermina
em:
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
239
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 252

19.3. Copiandonossomapa CasadoCódigo
X X
XXX XX X
X X
X X X X
XXX FX
XXX XXX X
XXX XXX X
XXX F X
Aconteceque,aoinvocarmosafun ção charsdenossa Stringpara
iterarmoscomo each_with_index,oRubytiraumacópiadenossoarray
decaracteres.Portanto,qualquermudan çaquefizermosnoarrayantigonão
afetaonovoarray.Issoé,degra çajáfizemosacópiaqueteremosquefazer
comaslinhas.
Logo,removemosasduaslinhasqueimprimiamnossaslinhasdeinfor-
mação,voltandoàversãoantiga:
def move_fantasma(mapa, linha, coluna)
posicoes = posicoes_validas_a_partir_de mapa, [linha, coluna]
if posicoes.empty?
return
end
posicao = posicoes[0]
mapa[linha][coluna] = " "
mapa[posicao[0]][posicao[1]] = "F"
end
19.3 Copiando nosso mapa
Vamoscopiarnossomapapararesolveroproblemadosfantasmasteletrans-
portadores. Aoiniciaromovimentodosfantasmas,copiamosnossoarray.
Poderíamosfazerdoisla çosaninhados,dois forspassandoporcadaele-
mentoecopiando-osumaum:
def copia_mapa(mapa)
novo_mapa = []
240
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 253

CasadoCódigo Capítulo19. Matrizesememória
mapa.each do |linha|
nova_linha = ""
linha.chars.each do |caractere|
nova_linha << caractere
end
novo_mapa << nova_linha
end
novo_mapa
end
Precisaríamosaindaverificarseoelementoéumfantasma,removendo-o:
def copia_mapa(mapa)
novo_mapa = []
mapa.each do |linha|
nova_linha = ""
linha.chars.each do |caractere|
if caractere == "F"
nova_linha << " "
else
nova_linha << caractere
end
end
novo_mapa << nova_linha
end
novo_mapa
end
Quehorror.Emvezdisso,podemosutilizaraquelafun çãoquejáconhe-
cemos,queduplicaumvalorqueasuporte(o dup),eoutrafun çãoquetroca,
traduz( tr),os Fsporespa ços:
def copia_mapa(mapa)
novo_mapa = []
mapa.each do |linha|
nova_linha = linha.dup.tr "F", " "
novo_mapa << nova_linha
end
novo_mapa
end
241
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 254

19.4. Movendoosfantasmasnamatrizcopiada CasadoCódigo
Essecódigoaindaestábemgrande.Repareque,sepodemostrocar "F"s
por " ",podemosjuntartodoomapaemumaúnica String,fazendoum
join.O joinjuntadiversas Strings:
nomes = ["guilherme", "de", "azevedo", "silveira"]
puts nomes.join(" ") # guilherme de azevedo silveira
puts nomes.join("\n") # guilherme
# de
# azevedo
# silveira
Juntamosnossomapaemumaúnica String:
def copia_mapa(mapa)
texto = mapa.join("\n")
# e agora?
end
Agoratrocamostodosdeumavez,equebramosnovamente:
def copia_mapa(mapa)
novo_mapa = mapa.join("\n").tr("F", " ").split("\n")
end
19.4 Movendo os fantasmas na matriz copiada
Nossafun çãoquemoveosfantasmasprecisaagoraefetuarasmudan çasno
novomapa:
def move_fantasmas(mapa)
caracter_do_fantasma = "F"
novo_mapa = copia_mapa mapa
# ...
end
Aomoverofantasmaenviaremostantoomapaantigoquantoonovo:
def move_fantasmas(mapa)
caracter_do_fantasma = "F"
242
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 255

CasadoCódigo Capítulo19. Matrizesememória
novo_mapa = copia_mapa mapa
mapa.each_with_index do |linha_atual, linha|
linha_atual.chars.each_with_index do |caractere_atual,
coluna|
eh_fantasma = caractere_atual == caracter_do_fantasma
if eh_fantasma
move_fantasma mapa, novo_mapa, linha, coluna
end
end
end
end
Nossafun ção move_fantasmadevereceberosdoismapas:
def move_fantasma(mapa, novo_mapa, linha, coluna)
posicoes = posicoes_validas_a_partir_de mapa, [linha, coluna]
if posicoes.empty?
return
end
posicao = posicoes[0]
mapa[linha][coluna] = " "
mapa[posicao[0]][posicao[1]] = "F"
end
Olhando o código anterior, onde devemos trocar omapa pelo
novo_mapa?Primeiroavaliamosasposi çõesválidas.Sóéválidoirparauma
posiçãosenãotemnenhumfantasmalá,esenenhumsemoveuparaláno
novomapa. Portanto,temosqueverificarosdoismapas,nãosóumdeles.
Passemososdoismapascomoargumento:
def move_fantasma(mapa, novo_mapa, linha, coluna)
posicoes = posicoes_validas_a_partir_de mapa, novo_mapa,
[linha, coluna]
if posicoes.empty?
return
end
243
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 256

19.4. Movendoosfantasmasnamatrizcopiada CasadoCódigo
posicao = posicoes[0]
mapa[linha][coluna] = " "
mapa[posicao[0]][posicao[1]] = "F"
end
Alteramostambémafun ção posicoes_validas_a_partir_depara
verificarseosdoismapastêmumaposi çãoválida:
def posicoes_validas_a_partir_de(mapa, novo_mapa, posicao)
posicoes = []
baixo = [posicao[0] + 1, posicao[1]]
if posicao_valida? mapa, baixo && posicao_valida?
novo_mapa, baixo
posicoes << baixo
end
direita = [posicao[0], posicao[1] + 1]
if posicao_valida? mapa, direita && posicao_valida?
novo_mapa, direita
posicoes << direita
end
cima = [posicao[0] - 1, posicao[1]]
if posicao_valida? mapa, cima && posicao_valida?
novo_mapa, cima
posicoes << cima
end
esquerda = [posicao[0], posicao[1] - 1]
if posicao_valida? mapa, esquerda && posicao_valida?
novo_mapa, esquerda
posicoes << esquerda
end
posicoes
end
Um fantasma só pode andar para posições nas quais, no novo
mapa,nãohánenhumoutrofantasma,portantonaprimeirainvoca çãoa
posicoes_validas_a_partir_dedevemosusaronovomapa.
Porfim,devemosdesenharofantasmanonovomapa:
244
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 257

CasadoCódigo Capítulo19. Matrizesememória
def move_fantasma(mapa, novo_mapa, linha, coluna)
posicoes = posicoes_validas_a_partir_de mapa, novo_mapa,
[linha, coluna]
if posicoes.empty?
return
end
posicao = posicoes[0]
mapa[linha][coluna] = " "
novo_mapa[posicao[0]][posicao[1]] = "F"
end
Massealteramosumarraydentrodafun ção move_fantasma,seráque
eletambémétrocadoforadafun ção?Pensemosno stack trace:
move_fantasma (mapa = ???, novo_mapa = ???)
move_fantasmas (mapa = ???, novo_mapa = ???)
...
Qualéovalordeumarray?Jávimosqueumavariávelquereferenciaum
arrayésomenteumvalor,eoarrayemsiestáemumúnicocantodamemória.
Paraummapamaissimples,teríamos:
move_fantasma (mapa = 123, novo_mapa = 456)
move_fantasmas (mapa = 123, novo_mapa = 456)
...
Em um canto da memoria:
123: [XXX]
[ F ]
[XXX]
456: [XXX]
[ ]
[XXX]
Sealterarmosumaposi çãonareferência 456,ambaspossuemalgoal-
terado. Essealgonãoéareferênciaemsi,ambascontinuamreferenciando,
apontando,paraomesmovalordamemória:
245
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 258

19.4. Movendoosfantasmasnamatrizcopiada CasadoCódigo
move_fantasma (mapa = 123, novo_mapa = 456)
move_fantasmas (mapa = 123, novo_mapa = 456)
...
Em um canto da memoria:
123: [XXX]
[ F ]
[XXX]
456: [XXX]
[ F]
[XXX]
Devemossemprenoslembrar:seovalordeumavariáveléumvalornu-
méricosimples,passá-locomoparâmetroenviaovaloremsi. Seeleéum
valormaiscomplexo,umobjeto,como String, Arrayououtro,temos
somenteumareferênciaparaessevalormaiscomplexonamemória.
Testamosojogo:
main.rb:1:in ` require_relative': fogefoge.rb:56:
syntax error, unexpected tIDENTIFIER, expecting keyword_do
or '{' or '(' (SyntaxError)
if posicao_valida? mapa, baixo && posicao_valida? novo_mapa,
baixo
ORubyseperdeucomnossainvoca çãoàfun ção posicao_valida.
Noteque,comonãousamosparêntesesparaainvoca ção,eleseperdeucom
o &&ecomanovainvoca çãodefun çãologoapósele.Comofoimencionado
anteriormente,emalgumassitua çõessomosobrigadosausarosparênteses.
Masissojáéumótimoindíciodequenossocódigoestáhorrível.Atacaremos
esseproblemaaseguir.Agora,corrigimosainvoca ção:
def posicoes_validas_a_partir_de(mapa, novo_mapa, posicao)
posicoes = []
baixo = [posicao[0] + 1, posicao[1]]
if posicao_valida?(mapa, baixo) && posicao_valida?(novo_mapa,
baixo)
posicoes << baixo
end
direita = [posicao[0], posicao[1] + 1]
246
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 259

CasadoCódigo Capítulo19. Matrizesememória
if posicao_valida?(mapa, direita) &&
posicao_valida?(novo_mapa, direita)
posicoes << direita
end
cima = [posicao[0] - 1, posicao[1]]
if posicao_valida?(mapa, cima) && posicao_valida?(novo_mapa,
cima)
posicoes << cima
end
esquerda = [posicao[0], posicao[1] - 1]
if posicao_valida?(mapa, esquerda) &&
posicao_valida?(novo_mapa, esquerda)
posicoes << esquerda
end
posicoes
end
Rodamosocódigo:
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXX X
XXX XXX X
XXX XXX X
XXX X
Agoraosfantasmasseforam?Claro!Criamosonossonovoarray,defim
dejogada,masnãootrocamospeloantigo!Quandooturnoacaba,devemos
dizerqueonovoarraydeveserutilizadoparaopróximoturno.Vamosfazer
o move_fantasmasretornaronovomapa:
def move_fantasmas(mapa)
caracter_do_fantasma = "F"
247
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 260

19.5. Refatorandoomovimentodofantasma CasadoCódigo
novo_mapa = copia_mapa mapa
# ...
novo_mapa
end
Aojogar,eleétrocado:
def joga(nome)
mapa = le_mapa(2)
while true
# ...
mapa = move_fantasmas mapa
end
end
Rodamosnovamenteeagoranossosfantasmasnemdesaparecem,nem
seteletransportam:
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X X X X
XXX FX
XXXFXXX X
XXX XXX X
XXX X
19.5 Refatorando o movimento do fantasma
Oúnicoproblemaéquenosso posicoes_validas_a_partir_deestá
horrendo.
def posicoes_validas_a_partir_de(mapa, novo_mapa, posicao)
posicoes = []
248
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 261

CasadoCódigo Capítulo19. Matrizesememória
baixo = [posicao[0] + 1, posicao[1]]
if posicao_valida?(mapa, baixo) &&
posicao_valida?(novo_mapa, baixo)
posicoes << baixo
end
direita = [posicao[0], posicao[1] + 1]
if posicao_valida?(mapa, direita) &&
posicao_valida?(novo_mapa, direita)
posicoes << direita
end
cima = [posicao[0] - 1, posicao[1]]
if posicao_valida?(mapa, cima) &&
posicao_valida?(novo_mapa, cima)
posicoes << cima
end
esquerda = [posicao[0], posicao[1] - 1]
if posicao_valida?(mapa, esquerda) &&
posicao_valida?(novo_mapa, esquerda)
posicoes << esquerda
end
posicoes
end
Assimcomofizemosumarefatora çãodamovimenta çãodojogador,esse
códigopareceterumpadrãoaotestarcadaposi çãoaoredordenossofan-
tasma.Podemoscriarumarraysimplescomosvaloresadequadosparacada
umadasquatroposi ções:
movimentos = [[-1, 0], [0, +1], [+1, 0], [0, -1]]
Eparacadaumadasposi çõespossíveis:
movimentos = [[-1, 0], [0, +1], [+1, 0], [0, -1]]
movimentos.each do |movimento|
end
Calculamosanovaposi ção:
249
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 262

19.5. Refatorandoomovimentodofantasma CasadoCódigo
movimentos = [[-1, 0], [0, +1], [+1, 0], [0, -1]]
movimentos.each do |movimento|
nova_posicao =
[posicao[0] + movimento[0], posicao[1] + movimento[1]]
if posicao_valida?(mapa, nova_posicao) &&
posicao_valida?(novo_mapa, nova_posicao)
end
end
Verificamosseelaéválida,acumulando-aemumarrayqueseráretor-
nadonofimdenossafun ção:
def posicoes_validas_a_partir_de(mapa, novo_mapa, posicao)
posicoes = []
movimentos = [[-1, 0], [0, +1], [+1, 0], [0, -1]]
movimentos.each do |movimento|
nova_posicao =
[posicao[0] + movimento[0], posicao[1] + movimento[1]]
if posicao_valida?(mapa, nova_posicao) &&
posicao_valida?(novo_mapa, nova_posicao)
posicoes << nova_posicao
end
end
posicoes
end
Podemosextrairtambémumafun çãodesomadevetores,quesomaas
duasposi ções:
def soma(vetor1, vetor2)
[vetor1[0] + vetor2[0], vetor1[1] + vetor2[1]]
end
def posicoes_validas_a_partir_de(mapa, novo_mapa, posicao)
posicoes = []
movimentos = [[-1, 0], [0, +1], [+1, 0], [0, -1]]
movimentos.each do |movimento|
nova_posicao = soma posicao, movimento
if posicao_valida?(mapa, nova_posicao) &&
250
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 263

CasadoCódigo Capítulo19. Matrizesememória
posicao_valida?(novo_mapa, nova_posicao)
posicoes << nova_posicao
end
end
posicoes
end
19.6 O fantasma cav aleiro
Esenossofantasmasecomportarcomoumape çadotipocavalonojogode
xadrez? Issoé,emvezdeirparacima,baixo,esquerdaedireita,queremos
queelefa çamovimentosdotipo‘L‘.Oexemploaseguirmostraaposiçãodo
fantasmaemarcandocom *asoitoposi çõesparaondeelepoderiairapós
umúnicomovimento:
XXXXXXX
X * * X
X X
X* *X
X F X
X* *X
X X
X * * X
XXXXXXX
Comoimplementaressalógica?Notequesãooitomovimentosválidos:
movimentos = [[-2, -1], [-2, +1], [+2, -1], [+2, +1],
[-1, -2], [-1, +2], [+1, -2], [+1, +2]]
Pronto,osfantasmasagoraandamcomocavalosdoxadrez.Comessetipo
detécnicasimplesconseguimosinclusiveimplementarmovimentoscomple-
xosdepe çasdetabuleiroemespa ços3d!Bastariaadicionaraterceiradimen-
são.Claro,nonossojogoofantasmanãoéumcavalo,massequiserdificultar
ojogodepois,podealterarosmovimentosválidosdofantasmafacilmente.
251
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 264

19.7. Movimentoaleatóriodosfantasmas CasadoCódigo
19.7 Movimento aleatório dos fantasmas
Precisamosescolherumadasposi ções,aleatoriamente. Jásabemosfazê-lo
comousodo rand:
def move_fantasma(mapa, novo_mapa, linha, coluna)
posicoes = posicoes_validas_a_partir_de mapa, novo_mapa,
[linha, coluna]
if posicoes.empty?
return
end
aleatoria = rand posicoes.size
posicao = posicoes[aleatoria]
mapa[linha][coluna] = " "
novo_mapa[posicao[0]][posicao[1]] = "F"
end
Pronto.Podemostestarojogoduasvezeseverquecadavezosfantasmas
selocomovemdemaneiradiferente.Notequesuasaídapodeser(eprovavel-
menteserá)diferentedaminha.Come çandoojogoemovendooheróiuma
vez:
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X FX X X
XXX F X
XXX XXX X
XXX XXX X
XXX X
Começandonovamenteojogo,movendoumaprimeiravez:
252
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 265

CasadoCódigo Capítulo19. Matrizesememória
XXXXXXXXX
X H X
X X XXX X
X X X X
X X X X
X X
XXX XX X
X X
X FX X X
XXX FX
XXX XXX X
XXX XXX X
XXX X
19.8 Quando o herói perde
Outrasitua çãoimportantequeaindanãodefinimoséquandoonossoherói
entraemcontatocomumfantasma.Issopodeocorrerquandooturnoacabae
tantoofantasmaquantooheróiestãonamesmaposi ção.Mascomodescobrir
queissoocorreu?
Comoofantasmaésempreoúltimoaandar,elevaiaparecer“porcima”
doherói:ojogadorsumirádomapa.Portanto,senãoencontramosojogador
nomapa,sabemosqueeleperdeuojogo.
Nossafun çãoqueencontraumjogadordeveagoraretornarquenãoen-
controu,vazio,nulo:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
mapa.each_with_index do |linha_atual, linha|
coluna_do_heroi = linha_atual.index caracter_do_heroi
if coluna_do_heroi
return [linha, coluna_do_heroi]
end
end
nil
end
Aoterminaroturno,verificamosseojogadornãoestámaisnomapae,
253
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 266

19.8. Quandooheróiperde CasadoCódigo
seforocaso,mostramosamensagemde Game Over.
def joga(nome)
mapa = le_mapa(2)
while true
# ...
mapa = move_fantasmas mapa
if encontra_jogador(mapa) == nil
game_over
break
end
end
end
EmRuby,verificarseumvalorénuloéamesmacoisaqueverificarque
elenãoexiste:
def joga(nome)
mapa = le_mapa(2)
while true
# ...
mapa = move_fantasmas mapa
if !encontra_jogador(mapa)
game_over
break
end
end
end
Masnossafun çãoestábemfeia. Novamentetemosumalinhaquefaz
muitacoisa: if, !einvocaumafun ção.Vamosextrairocódigo,lembre-se
queavariávelédesnecessáriaesóéutilizadaparadeixarclarooqueestamos
retornando:
def jogador_perdeu?(mapa)
perdeu = !encontra_jogador(mapa)
end
def joga(nome)
mapa = le_mapa(2)
254
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 267

CasadoCódigo Capítulo19. Matrizesememória
while true
# ...
mapa = move_fantasmas mapa
if jogador_perdeu?(mapa)
game_over
break
end
end
end
Criamostambémafun çãode game_overnanossainterface:
def game_over
puts "\n\n\n\n\n\n"
puts "Game Over"
end
Pronto,podemosjogaratéomomentoqueperdemos:
XXXXXXXXX
X X
X X XXX X
X X X X
X X X X
X X
XXX XX X
FX F X
X HX X X
XXX X
XXX XXX X
XXX XXX X
XXX X
Para onde deseja ir?
W
Game Over
255
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 268

19.9. Retornonuloouopcional? CasadoCódigo
Comoomovimentodedoisfantasmaséaleatório,demoraparaperde-
mos.
19.9 Retorno nulo ou opcional?
Nossafun ção encontra_jogadorretornanadacasoelenãoencontreum
jogadornomapa.O nilémuitoútilparamarcarqueumafun çãoquere-
tornaalgopode,sobdeterminadascircunstâncias,retornarnada.Oproblema
aconteceaousaresseretorno.Comoodesenvolvedorpodeescrevercódigo
queinvocaafun çãoefazqualquercoisacomoretorno,elenãoéobrigadoa
verificarseovalorretornadoévazio.Senãoforvazio,aaplica çãopodeparar
comumerroouaindasecomportardemaneiratotalmenteinesperada.
Algumaslinguagensdeprograma çãofuncionaiscomoSwiftapresentam
umconceitodeopcional,outraslinguagensorientadasaobjetocomoJava
oferecemtalfuncionalidade,quejáobrigaodesenvolvedoraverificarseo
retornoéválidoantesdeutilizá-lo.
19.10 Resumindo
Vimoscomoéimportantecuidardireitinhodenossasreferênciasnamemó-
ria.Umvalorcomoumarraypodeseralteradoporforaepordentrodeuma
função,causandobagun çanaquiloquequeremosrepresentar.Emjogosba-
seadosemturno( turn-based),assimcomoemprocessosquedevemexecutar
algobaseadoemumestado,écomumqueoestadosejarepresentadoporum
valoreacadanovoestadotiremosumacópiainteiradele.Podemosatévol-
taraoestadoanterior( undo)comtalprática quetemnome, Memento! O
cuidadoquedevemostomarécomamemória,claro.
Implementamosomovimentoaleatórioeofimdojogoquandooherói
perdeparaumfantasma. Emdiversosdessesinstantesutilizamospráticas
típicasdeumprogramadordejogosoudemaratonadeprograma ção,onde
usamosarraysparatrabalharcomoatalhosparadeterminadosresultados.
Comoveremosadiante,estruturas,classeseobjetospodemrepresentaro
mesmotipodeinforma ção,mascommaisvalordesignificado(ummapanão
éumarray,éummapa umheróinãoéumarraydetamanho2,éumherói
256
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 269

CasadoCódigo Capítulo19. Matrizesememória
emumalinhaeumacoluna),algoquepodeserbenéficoparanossocódigo
emlongoprazo.
257
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 270

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 271

Capítulo20
Estruturaseclasses:uma
introduçãoaOrienta çãoa
Objetos
20.1 A bagunça dos defs
Olhemosnossafun çãosoma,quesomadoisvetoresparacalcularumanova
posição:
def soma(vetor1, vetor2)
[vetor1[0] + vetor2[0], vetor1[1] + vetor2[1]]
end
Pormaisqueelasejaumafun çãoquefazsentido,oqueelatememco-
mumcomafun ção copia_mapa?
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 272

20.2. Extraindoumaprimeiraestrutura CasadoCódigo
def copia_mapa(mapa)
mapa.join("\n").tr("F", " ").split("\n")
end
Sãológicasdenegócio,nadamais.Seguindosomenteessecritériodese-
paraçãodelógicadenegócios,éfácilimaginarqueumprojetooujogogrande
vaificarcom“infinitas”funçõesjuntas.Maisainda,quemsabecomosomar
ummovimentoaumaposi çãoéogerenciamentodeposi ções. Quemsabe
copiarummapaéoprópriomapa. Nesseinstante,todasessasresponsabi-
lidadesestãonomesmolugar,jogadasemumúnicoarquivo.Atémesmoo
herói!Comoassimoheróiéumarraydeduasposi ções?Oheróiéumherói,
évocê,soueu.Elenãoéummeroarray.
Apesardenossofocoserumaintrodu çãoacomputa çãoeprograma-
ção,porutilizarmosalinguagemRubycomoexemplo,desenvolveremosum
poucomaisnossojogonosentidodefazê-losuportaromínimodeorienta-
çãoaobjetos... ecome çaremospeloquehádemaisimportanteparanós,o
jogador,nossoherói.
20.2 Extraindo uma primeira estrutura
Atéagorarepresentamosumheróicomumarraydetamanhodois,oqueé
algomuitoestranho. Pensandoemvalores,umheróiéumherói,nãoum
array. Paramovê-la,bastamudarsualinhaecoluna,mandarsemovimen-
tar.Seriainteressantecriarumúnicovalor, Heroi,quetivessedoisvalores
dentrodele,a linhaea colunaatual.
Queremoscriarumaestruturaquerepresentaumherói,umaabstra ção
denossoherói. Essaabstra çãonãoénossoheróideverdade,somenteuma
definiçãodecomoumheróisecomportanomundoreal.Vamoscriaruma
classe:
class Heroi
end
Agorapodemoscriarumherói:
class Heroi
end
260
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 273

CasadoCódigo Capítulo20. Estruturaseclasses:umaintrodu çãoaOrienta çãoaObjetos
heroi = Heroi.new
Masumheróisemlinhanemcolunanãotemgra ça.Queremosdizerque
umheróitemdoisatributos,sualinhaesuacoluna:
class Heroi
attr_accessor :linha, :coluna
end
heroi = Heroi.new
heroi.linha = 3
heroi.coluna = 6
puts heroi.linha # 3
puts heroi.coluna # 6
Teremosumavariávelchamada heroiquetemumvalor.Essevaloréa
referênciaparaumobjeto,umainstânciade Heroi,sendoquedentrodesse
objetoteremososvalores linhae coluna.Nocasodonossoherói,esses
valoressão 3e 6.
Damesmamaneiraquecriamosumherói,umobjetodotipoherói,pode-
moscriardois.Cadaumtemvaloresdiferentes,poistemespa çosdiferentes
namemória:
class Heroi
attr_accessor :linha, :coluna
end
guilherme = Heroi.new
guilherme.linha = 3
guilherme.coluna = 6
paulo = Heroi.new
paulo.linha = 5
paulo.coluna = 3
puts guilherme.linha # 3
puts guilherme.coluna # 6
261
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 274

20.3. Usandoumaestrutura CasadoCódigo
puts paulo.linha # 5
puts paulo.coluna # 3
Oquefizemosatéagora?Definimosumaabstra ção,comofuncionaum
herói,umaclasse Heroi.Eladáasregrasdecomoumheróipodesercriado
(instanciado),quaisseusatributos(variáveisdeinstância),comportamentos
(funções)entreoutros.Paranósjáéótimosaberquenossoheróinosistema
agoraérealmenteumherói,enãoumagambiarradeumvetor.Portanto,o
códigofinaldoarquivo heroi.rbé:
class Heroi
attr_accessor :linha, :coluna
end
20.3 Usando uma estrutura
Devemosusarnossojogadorcomoumainstânciade Heroi,paraissoalte-
raremosomomentoemqueeleéencontrado,o encontra_jogador:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
mapa.each_with_index do |linha_atual, linha|
coluna_do_heroi = linha_atual.index caracter_do_heroi
if coluna_do_heroi
return [linha, coluna_do_heroi]
end
end
nil
end
Quandoencontramosumjogador,instanciamos,criamosumnovoob-
jetodotipo Heroinalinhaenacolunaadequada:
def encontra_jogador(mapa)
caracter_do_heroi = "H"
mapa.each_with_index do |linha_atual, linha|
coluna_do_heroi = linha_atual.index caracter_do_heroi
if coluna_do_heroi
262
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 275

CasadoCódigo Capítulo20. Estruturaseclasses:umaintrodu çãoaOrienta çãoaObjetos
heroi = Heroi.new
heroi.linha = linha
heroi.coluna = coluna_do_heroi
return heroi
end
end
nil
end
Jáqueusamosaclasse Heroi,precisamoscarregá-la:
require_relative 'ui'
require_relative 'heroi'
# ...
Tentamosencontrarojogadornafun ção joga:
heroi = encontra_jogador mapa
nova_posicao = calcula_nova_posicao heroi, direcao
if !posicao_valida? mapa, nova_posicao
next
end
mapa[heroi[0]][heroi[1]] = " "
mapa[nova_posicao[0]][nova_posicao[1]] = "H"
Primeiroausamosparaencontraraposi çãodoheróinomapa,oque
podemosmudarpara:
mapa[heroi.linha][heroi.coluna] = " "
O herói também é passado como argumento para o
calcula_nova_posicao:
nova_posicao = calcula_nova_posicao heroi, direcao
Quebrincacomosvalores [0]e [1]denossoantigoarray.
263
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 276

20.4. Codesmell:featureenvy CasadoCódigo
def calcula_nova_posicao(heroi, direcao)
heroi = heroi.dup
movimentos = {
"W" => [-1, 0],
"S" => [+1, 0],
"A" => [0, -1],
"D" => [0, +1]
}
movimento = movimentos[direcao]
heroi[0] += movimento[0]
heroi[1] += movimento[1]
heroi
end
Issonãofazmaissentido,afinalumheróinãotemmaisessesacessos.Ele
possuiumalinhaeumacoluna,logo:
def calcula_nova_posicao(heroi, direcao)
heroi = heroi.dup
movimentos = {
"W" => [-1, 0],
"S" => [+1, 0],
"A" => [0, -1],
"D" => [0, +1]
}
movimento = movimentos[direcao]
heroi.linha += movimento[0]
heroi.coluna += movimento[1]
heroi
end
20.4 C ode smell: feature envy
Opa. Nosso calcula_nova_posicaotemalgodeestranho. Das6ins-
truçõescontidasnocódigo,4delas(doister ços!) envolvemnossoherói! O
códigonosindicaqueafun ção calcula_nova_posicaoestácominveja
doherói,elaqueriaterasfuncionalidadesdeleeporissoficaperguntando
cinquentacoisasparaele: dupporfavor, linhaporfavor, colunapor
264
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 277

CasadoCódigo Capítulo20. Estruturaseclasses:umaintrodu çãoaOrienta çãoaObjetos
favor, retorna você porfavor. Quantainveja,invejadefuncionalidade,
feature envy.
Essacaracterísticaéumfedordecódigoqueindicaqueessafun çãopo-
deriapertenceraquemelatanto“gosta”.Afinal,perguntemosanósmesmos,
quementendemaisdeumpersonagemheroicodoqueelemesmo? Quem
sabemovimentarumherói?Elemesmo!Alémdisso,nãofaznenhumsentido
afun ção calcula_nova_posicaoserinvocadaseumheróinãoexiste.Por
todosessesmotivos,podemosmoverafun çãoparadentrodenosso Heroi:
class Heroi
attr_accessor :linha, :coluna
def calcula_nova_posicao(heroi, direcao)
heroi = heroi.dup
movimentos = {
"W" => [-1, 0],
"S" => [+1, 0],
"A" => [0, -1],
"D" => [0, +1]
}
movimento = movimentos[direcao]
heroi.linha += movimento[0]
heroi.coluna += movimento[1]
heroi
end
end
Masseafun çãojáestádentrodopróprioherói,nãoprecisamosrecebê-lo
comoargumento.Vamosremoveroargumento:
class Heroi
attr_accessor :linha, :coluna
def calcula_nova_posicao(direcao)
# ...
end
end
Jáqueestamosrodandoessecódigodentrodenossoherói,enãootemos
maiscomoargumento,avariável heroinãoexistemaisparaexecutarmos
265
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 278

20.4. Codesmell:featureenvy CasadoCódigo
o dup.Comoinvocarométodo dupnopróprioobjeto?Comodizerparao
códigodeummétododentrodeumobjetoparainvocaroutrométodonele
mesmo,nelepróprio?Usamosapalavra“próprio”,eminglêsself:
class Heroi
attr_accessor :linha, :coluna
def calcula_nova_posicao(direcao)
heroi = self.dup
movimentos = {
"W" => [-1, 0],
"S" => [+1, 0],
"A" => [0, -1],
"D" => [0, +1]
}
movimento = movimentos[direcao]
heroi.linha += movimento[0]
heroi.coluna += movimento[1]
heroi
end
end
Porfim,quandoinvocamosummétodoemnósmesmos,ousodo self
énaverdadeopcional.Podemos:
class Heroi
attr_accessor :linha, :coluna
def calcula_nova_posicao(direcao)
heroi = dup
movimentos = {
"W" => [-1, 0],
"S" => [+1, 0],
"A" => [0, -1],
"D" => [0, +1]
}
movimento = movimentos[direcao]
heroi.linha += movimento[0]
heroi.coluna += movimento[1]
heroi
end
end
266
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 279

CasadoCódigo Capítulo20. Estruturaseclasses:umaintrodu çãoaOrienta çãoaObjetos
Nossafun ção jogadeveagorainvocarométodonopróprioobjeto:
def joga(nome)
mapa = le_mapa(2)
while true
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
nova_posicao = heroi.calcula_nova_posicao direcao
if !posicao_valida? mapa, nova_posicao
next
end
mapa[heroi.linha][heroi.coluna] = " "
mapa[nova_posicao[0]][nova_posicao[1]] = "H"
mapa = move_fantasmas mapa
if jogador_perdeu?(mapa)
game_over
break
end
end
end
20.5 Boa prática : buscar quem invoca antes de
refatorar
Agoranossa nova_posicaotambéméumobjetodotipo Heroi. Elaé
usadaemnossafun çãotambémaosubstituirmosovalordelanomapa,oque
jásabemosalterarparautilizarosatributos linhae posicao:
mapa[nova_posicao.linha][nova_posicao.coluna] = "H"
Maselatambéméutilizadaparaverificarseanovaposi çãoéválida:
if !posicao_valida? mapa, nova_posicao
next
end
267
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 280

20.5. Boaprática:buscarqueminvocaantesderefatorar CasadoCódigo
Antesderefatorarmosocódigodeumafun ção sempredevemosolhar
quemainvoca.Nessecaso,tantoaquiquantonomomentodemovimentar
umfantasmainvocamosafun ção posicao_valida?. Issosignificaque,
sealterarmosocódigodelaparasuportarum Heroiemvezdeumarray
deduasposi ções,quebraremosocódigodofantasma,enãoqueremosisso
nesseinstantedenossarefatora ção.Oquequeremoséfazeressainvoca ção
funcionar.
Comotransformarum Heroiemumarraydeduasposi çõesparapoder
continuarinvocandoummétodoquefuncionatantoparaoheróiquantopara
ofantasma?
Podemoscriarummétodonovo,seguindoopadrão to_idoRuby,algo
como to_array(emvezde to_aqueéambíguodemais):
class Heroi
attr_accessor :linha, :coluna
def calcula_nova_posicao(heroi, direcao)
# ...
end
def to_array
[linha, coluna]
end
end
Terminamoscomnossoherói:
class Heroi
attr_accessor :linha, :coluna
def calcula_nova_posicao(direcao)
heroi = dup
movimentos = {
"W" => [-1, 0],
"S" => [+1, 0],
"A" => [0, -1],
"D" => [0, +1]
}
movimento = movimentos[direcao]
heroi.linha += movimento[0]
268
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 281

CasadoCódigo Capítulo20. Estruturaseclasses:umaintrodu çãoaOrienta çãoaObjetos
heroi.coluna += movimento[1]
heroi
end
def to_array
[linha, coluna]
end
end
Einvocamosométodo to_arrayaoverificarseanovaposi çãoéválida,
ficandocomométodo joga:
def joga(nome)
mapa = le_mapa(2)
while true
desenha mapa
direcao = pede_movimento
heroi = encontra_jogador mapa
nova_posicao = heroi.calcula_nova_posicao direcao
if !posicao_valida? mapa, nova_posicao.to_array
next
end
mapa[heroi.linha][heroi.coluna] = " "
mapa[nova_posicao.linha][nova_posicao.coluna] = "H"
mapa = move_fantasmas mapa
if jogador_perdeu?(mapa)
game_over
break
end
end
end
Pronto.Nossojogojáestáfuncionando.Agoracomnossoheróibemre-
presentado,epartedocódigoquelhepertence( calcula_nova_posicao)
dentrodele.
269
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 282

20.6. Boaprática:Tell,don’task CasadoCódigo
20.6 B oa prática :T ell, don’t ask
Novamentetemosrepeti çãodecódigo.Dadoumherói,fazemos:
mapa[heroi.linha][heroi.coluna] = " "
Depois,dadaumanovaposi ção,marcamoscom H:
mapa[nova_posicao.linha][nova_posicao.coluna] = "H"
Emvezdepedirinforma ção( ask),parecefazermaissentidomandarexe-
cutaralgo( tell):
heroi.remove_do mapa
nova_posicao.coloca_no mapa
Opadrãoqueestamosadotandoéodemandarexecutaralgo,aoinvésde
perguntar: tell, don’t ask. Nãonosimportaseoheróiéimplementadocom
linhae coluna, xe y,arraydetamanhodois. Nãoimporta. Importa
queumaposi çãoécapazdeseremoverdeummapa.Equeelaécapazdese
colocarnomapa.
Vamosdefinirométodo remove_do,oatodefazerum extract method:
def remove_do(mapa)
mapa[linha][coluna] = " "
end
Eo coloca_no:
def coloca_no(mapa)
mapa[linha][coluna] = "H"
end
20.7 Atributos e attr _accessor
O attr_accessornaverdadecriadoismétodos.Umparaalterareoutropara
lerovalordeumatributo.Comolerumatributodiretamentededentrode
umaclasse?Atravésdeum @,comonocaso:
270
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 283

CasadoCódigo Capítulo20. Estruturaseclasses:umaintrodu çãoaOrienta çãoaObjetos
def coloca_no(mapa)
mapa[@linha][@coluna] = "H"
end
Comoestamosutilizandoum attr_accessor,tantofazmantermoso
@ounão;manteremossemo @.
Alémdo attr_accessor,existemtambémo attr_reader,quefor-
necesomenteumleitor,eo attr_writer,quedisponibilizasomenteomé-
tododeescrita.
20.8 E strutura ou Classe?
Costumamoschamarde estruturaadefini çãodeumconjuntodevalores
agrupados.Nocome çodonossocódigo,utilizamosum Heroiparasomente
agruparvalores,nadamais.Costumamoschamarosvaloresdeumaestrutura
de“dados”ou“estrutura”,mascuidadoparanãoconfundirainstânciadessa
estrutura(comdados)comadefini çãodaestrutura.
Umaclasseéadefini çãodeumagrupamentotantodevalorescomode
comportamentos,fun ções.Nessecasochamamosessasfun çõesde métodos,
comovimosantes.Aocriarmosumainstânciadeumaclasse,chamamosesse
valordeobjeto.
Jáhavíamosutilizadosobjetosantes. Narealidade,todovaloremRuby
éumobjeto.As Strings, Arrays, Fixnume Floatsãotodostipos(classes)dos
quaisforamcriadasinstâncias.Porexemplo,aousarmosovalor 15estamos
comumainstânciade Fixnumcujovalorinternoé 15.Aocriarmosumarray
denúmerostemosnaverdadeumobjeto(oarray)queapontaparadiversos
objetos(cadaumdosnúmeros).
Dependendodalinguagem,adefini çãovariaumpouco,nãoseassuste
aoaprenderumanovalinguagem.Umafuncionalidadedeumapodeterum
nomeumpoucodiferenteemoutra.
271
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 284

20.9. Averdadeportrásdemétodos,fun çõeselambdas CasadoCódigo
Code smell: classes anêmicas
AquiemRuby,acabamosporusarbasicamenteclassescomoclasses
deverdade,enãocomomerasestruturasbobas(comumentechamadas
declassesanêmicas).
20.9 A verdade por trás de métodos , funções e
lambdas
Jáqueumafunçãoéumnomeparaumtrechodecódigo,podemospensarque
umafun çãotambémpoderiaserumtipodevariável,assimcomoumarrayé.
Napráticaéissoqueacontece!Portrásdospanos,tantoumafun çãoquanto
umvalorqualqueréreferenciadoatravésdeumnome,onomedafun çãoou
davariável.
SóqueemRubynãoconseguimosfazerdiretamenteumavariávelrefe-
renciarumafun çãoqueacabadeserdefinidacomovimosatéagora,devido
àregradosparênteses.EmJavascriptissoseriapossível:
function bemvindo(nome) {
println("Bem vindo " + nome + "!");
}
var minhaFuncao = bemvindo;
minhaFuncao("Guilherme");
EmRuby,ocódigoanálogoinvocariaafun ção,sempassarparâmetros,
aotentarreferênciá-la:
def bemvindo(nome)
puts "Bem vindo " + nome + "!"
end
minhaFuncao = bemvindo # tenta invocar a função sem parâmetro!
minhaFuncao "Guilherme" # não faz sentido nenhum
272
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 285

CasadoCódigo Capítulo20. Estruturaseclasses:umaintrodu çãoaOrienta çãoaObjetos
Parafazerisso,Rubypermiteacria çãodefun ções“soltas”,literalmente
umafun ção,chamadasnessecontextode lambda literal,umafun çãoquenão
estáatreladaanenhumobjeto:
bemvindo = -> (nome) {
puts "Bem-vindo " + nome + "!"
}
Podemosagorainvocá-la,comumasintaxebemfeia vendoporoutro
lado,maiseducada deixandoclaroqueestamosinvocando( call)algo:
bemvindo.("Guilherme") # Bem vindo Guilherme!
bemvindo.call("Guilherme") # Bem vindo Guilherme!
Ouaindareatribuí-laaoutravariável:
minhaFuncao = bemvindo
minhaFuncao.("Guilherme") # Bem vindo Guilherme!
Comoométodoéainvoca çãodeumafun çãonoobjeto,temosemRuby
quesempreestamosinvocandométodos.Oconceitodefun çãopuranãofaz
sentido,umavezqueatémesmoo lambda literaléumobjetoondechamamos
ummétodo,ométodo call.Portanto,nãosepreocupe:issonãosignifica
queRubyéounãoéfuncional,somentequetodovaloremRubyéumobjeto
equeasfun çõesqueinvocamossãochamadasdemétodos.
Comovíciodelinguagem,acabamosusandoapalavra funçãoparadizer
queestamosinvocandooudefinindoessesmétodos,afinalumafun çãoestá
maispróximadadefini çãoformaldissoqueestamosinvocando.Novamente,
nãosepreocupe,aoconversarcomseuscolegasuseovocabulárioquedeixe
clarooqueéqueestáfazendo.
EmRuby,definimoseinvocamosmétodos massevocêchamá-losde
função,ninguémsaimachucado.
20.10 Resumindo
Vimoscomocriarumaestruturaquebasicamentearmazenadados,masem
Rubyelajáéumaclasse,commétodoseatributos.Aprendemosautilizá-la,
instanciandoumobjetoapartirdadefini çãodescritadenossaclasse.
273
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 286

20.10. Resumindo CasadoCódigo
Aonotarquenossocódigoutilizavamuitosvaloresdaestrutura,move-
mosocomportamentoparadentrodela,criandonossoprimeirométodo.
Aprendemosoquesignificainvocarummétodoparamandarfazeralgo,em
vezdeperguntarporalgumainforma ção,favorecendooencapsulamentoda
lógicaportrásdocomportamentoeincluindoseusatributos. Vimoscomo
expor,acessandoeescrevendovaloresematributos.
Outraslinguagenspodemdefinirosdoistiposbemdistintos: estrutu-
rasquecostumamsomenteagruparvalores,eclassesqueagrupamvalorese
comportamentos.
Porfim,vimosquetodovaloremRubyédealgumaformaumobjeto,
portantosemprequeutilizamosoconceitodefun çõesestávamosfalando,na
verdade,demétodos conceitualmentenãohánadadeerradoemchamá-las
defun ções,masemRubytaisfun çõessãotambémmétodos.Porfim,vimos
queseumnúmeroeuma Stringpodemservaloresaquedamosnomes
(aplicamosavariáveis),fun çõestambémpodemsertratadasassimatravésde
lambdas.
274
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 287

Capítulo21
Destruindoosfantasmas:o
mundodarecursão
21.1 Destruindo os fantasmas
Nossopróximopassoécolocarumabombanomeiojogo:quandoousuário
passaporela,eledetonaosfantasmaspróximos.Primeirocriamosumnovo
mapa,contendoasbombas( *)emaisfantasmas,nosso mapa3.txt:
XXXXXXXXXXXXXXXXX
X FFF X X
X X XX X X X XX X
X X X* X X X
X X XXXX XXX XX
X XX X X
XXX XX XXX X X X
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 288

21.1. Destruindoosfantasmas CasadoCódigo
X X X X
X X X XXX FFF X
X X XXX XXX X
X X XXX X XXX X
X HXXX X X X X
XXX*FXXFX X X
Passamosacarregaroterceiromapa:
mapa = le_mapa(3)
Primeiro,casoumfantasmaentreemcontatocomumabomba,elesim-
plesmenteacome,enossoheróitemmenoschancesdeganharojogo.Por-
tanto,presteaten ção,ojogadordevecorreratrásdasbombasomaisrápido
possível.
Jáquandoonossoheróiencostaemumabomba,devemosexplodirqua-
troposi çõesparaadireitadeondeabombaestá.Qualquerfantasmanaregião
devedesaparecer,assimcomomuros:
def joga(nome)
# ...
heroi.remove_do mapa
if mapa[nova_posicao.linha][nova_posicao.coluna] == "*"
mapa[nova_posicao.linha][nova_posicao.coluna + 1] = " "
mapa[nova_posicao.linha][nova_posicao.coluna + 2] = " "
mapa[nova_posicao.linha][nova_posicao.coluna + 3] = " "
mapa[nova_posicao.linha][nova_posicao.coluna + 4] = " "
end
nova_posicao.coloca_no map
# ...
end
Umaimplementa çãoinicial,masmuitoruim.Obviamentepodemostro-
carporum for:
heroi.remove_do mapa
if mapa[nova_posicao.linha][nova_posicao.coluna] == "*"
for direita in 1..4
276
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 289

CasadoCódigo Capítulo21. Destruindoosfantasmas:omundodarecursão
mapa[nova_posicao.linha][nova_posicao.coluna + direita]
" "
end
end
nova_posicao.coloca_no mapa
Testamosnossojogocomoterceiromapa,andandoparabaixo,evemos
oresultado,quandoosdoisfantasmaseosmurossãodestruídos:
...
X X XXX X XXX X
X HXXX X X X X
XXX*FXXFX X X
Para onde deseja ir?
...
X X XXX X XXX X
X XXX X X X X
XXXH X X X
21.2 Andando para a direita
Podemosextrairumafun çãoparaestetrechodocódigo,algoqueremova
tudodomapaapartirdestaposi ção,porquatrocasas.Vamosinvocá-la:
heroi.remove_do mapa
if mapa[nova_posicao.linha][nova_posicao.coluna] == "*"
remove mapa, nova_posicao, 4
end
nova_posicao.coloca_no mapa
Eextrairseucódigo:
def remove mapa, posicao, quantidade
for direita in 1..quantidade
mapa[posicao.linha][posicao.coluna + direita] = " "
end
end
Oresultadoaindaéomesmo.Masreparequeestáestranhaessahistória
detodavezsomarumnúmerocadavezmaior. Emvezdisso,poderíamos
277
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 290

21.3. Recursãoinfinita CasadoCódigo
falarparaaposi çãoandarparaadireita. Lembraquenossoheróisabese
movimentar?Elemesmotemométodo calcula_nova_posicao:
def remove mapa, posicao, quantidade
for direita in 1..quantidade
posicao = posicao.calcula_nova_posicao "D"
mapa[posicao.linha][posicao.coluna] = " "
end
end
Mas,Guilherme,aindaestáumpoucoestranho. Passar Dcomoargu-
mento?Estamosprogramandoorientadoa Stringouaobjetos?Seriamais
educadofazer:
def remove mapa, posicao, quantidade
for direita in 1..quantidade
posicao = posicao.direita
mapa[posicao.linha][posicao.coluna] = " "
end
end
Ecriarmosométodo direita:
class Heroi
# ...
def direita
calcula_nova_posicao "D"
end
end
21.3 Recursão infinita
Masreparequealógicadenossafun çãoaindaérazoavelmentecomplexa.
Notequeoqueola çofazépassarcoma direitado 1até 4,issoé,
posicao.coluna+1até posicao.coluna+4.Estamosfazendoumla ço,
mudandoaposi çãoelimpandoumtrechodomapa.Nãoseriapossívelsim-
plificarnossafun ção,removendoessela ço?
278
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 291

CasadoCódigo Capítulo21. Destruindoosfantasmas:omundodarecursão
def remove mapa, posicao, quantidade
for direita in 1..quantidade
posicao = posicao.direita
mapa[posicao.linha][posicao.coluna] = " "
end
end
Oqueseriadenossafun çãoseelasomenteremovesseaprimeiraposi ção
dadireita?
def remove mapa, posicao, quantidade
posicao = posicao.direita
mapa[posicao.linha][posicao.coluna] = " "
end
Nãoseriaosuficiente,poisaindatemosqueremovermaisposi çõesàdi-
reita,claro.Quantasposi çõesfaltamremover?Três.Issoé, quantidade -
1.Invoquemosaprópriafun çãonovamente,agorapassando quantidade
- 1,ouseja, 3:
def remove mapa, posicao, quantidade
posicao = posicao.direita
mapa[posicao.linha][posicao.coluna] = " "
remove mapa, posicao, quantidade - 1
end
Oqueaconteceagora?Afun çãoseráinvocadaparaasegundaposi çãoà
direita,comquantidadevalendo2;apróximaposi çãoàdireitacomquanti-
dadevalendo1;eaúltimaposi çãoàdireitacomquantidadevalendo0,mas
elacontinuasendoinvocadaeternamente!
Vejamoscomofunciona,vamossimularnossapilhadeexecu ção.Minhas
linhasdafun ção removesãocomoaseguir:
def remove mapa, posicao, quantidade
posicao = posicao.direita # linha 109
mapa[posicao.linha][posicao.coluna] = " " # linha 110
remove mapa, posicao, quantidade - 1 # linha 111
end
279
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 292

21.3. Recursãoinfinita CasadoCódigo
Primeiro,chamamosafun ção removecomo mapa,comaposi çãopor
exemplo 5, 7,e quantidadevalendo 4:
fogefoge.rb:remove:109 (mapa =..., posicao = 5,7, quantidade = 4)
Aoterminaraexecu çãodalinha109,indoparaa110,temosqueaposi ção
foialterada:
fogefoge.rb:remove:110 (mapa =..., posicao = 5,8, quantidade = 4)
Portanto, limpamosaposi ção 5,8domapa, oprimeiroquadradoà
direita. Agoraexecutamosalinha111,queinvocaafun ção removecom
quantidadevalendo3:
fogefoge.rb:remove:109 (mapa =..., posicao = 5,8, quantidade = 3)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,8, quantidade = 4)
Primeiro,elemoveaposi çãoparaadireita:
fogefoge.rb:remove:110 (mapa =..., posicao = 5,9, quantidade = 3)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,8, quantidade = 4)
Limpaaposi ção 5,9edepoischamaafun ção removenovamente,em-
pilhandomaisumavezafun ção:
fogefoge.rb:remove:109 (mapa =..., posicao = 5,9, quantidade = 2)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,9, quantidade = 3)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,8, quantidade = 4)
Maisumavezserámovidoparaadireita:
fogefoge.rb:remove:110 (mapa =..., posicao = 5,10,
quantidade = 2)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,9, quantidade = 3)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,8, quantidade = 4)
Omapanaposi ção 5,10élimpo,einvocamosafun çãonovamente:
fogefoge.rb:remove:109 (mapa =..., posicao = 5,10,
quantidade = 1)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,10,
quantidade = 2)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,9, quantidade = 3)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,8, quantidade = 4)
280
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 293

CasadoCódigo Capítulo21. Destruindoosfantasmas:omundodarecursão
Omesmoprocessoocorrepara 5,11:
fogefoge.rb:remove:109 (mapa =..., posicao = 5,11,
quantidade = 0)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,11,
quantidade = 1)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,10,
quantidade = 2)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,9, quantidade = 3)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,8, quantidade = 4)
Eofluxocontinua...
fogefoge.rb:remove:109 (mapa =..., posicao = ...,
quantidade = -576)
...
fogefoge.rb:remove:111 (mapa =..., posicao = 5,13,
quantidade = -1)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,12,
quantidade = 0)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,11,
quantidade = 1)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,10,
quantidade = 2)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,9, quantidade = 3)
fogefoge.rb:remove:111 (mapa =..., posicao = 5,8, quantidade = 4)
Podemosverissoacontecerrodandoojogo:
heroi.rb:4: stack level too deep (SystemStackError)
Opa.Oqueaconteceu?Oníveldeprofundidadefoimuitogrande,pois
chamamosumafun ção,quechamouasimesma,quechamouasimesma,
quechamouasimesma,eternamente.Masclaro,existealgumlimite como
tudoemumcomputador paraotamanhodapilha,eesselimitealgumahora
foialcan çado.Oprogramaparou.
Oqueestamosfazendoéquenossafun çãochamaasimesma,essatécnica
échamadade recursão.
281
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 294

21.4. Abasedarecursão CasadoCódigo
21.4 A base da recursão
Oproblemadeumarecursãoinfinitaéqueumahoraapilhadeexecu ção
estoura,eoprogramapara.Queremosdefinirumpontodeparada;nonosso
caso,sóqueremosexecutarnossafun çãoenquantoaquantidadeformaior
quezero:
def remove mapa, posicao, quantidade
if quantidade == 0
return
end
posicao = posicao.direita
mapa[posicao.linha][posicao.coluna] = " "
remove mapa, posicao, quantidade - 1
end
Unless: trav a de segurança (safeguard)
Outramaneiradeescreveressecódigoseriausandoo unlessde
umalinha
def remove mapa, posicao, quantidade
return unless quantidade > 0
posicao = posicao.direita
mapa[posicao.linha][posicao.coluna] = " "
remove mapa, posicao, quantidade - 1
end
Temosumainversão,umanega ção,oquepodeficarconfuso: não
executeissoseformaiordoquezero.
Essepontodeparadadarecursãoéoquechamamosdebasedarecursão.
Quandoelachegaàqueleponto,elapara. Rodandoagoranossaaplica ção
teríamososeguinte stack trace:
fogefoge.rb:remove:109 (mapa =..., posicao = 5,12,
quantidade = 0)
fogefoge.rb:remove:112 (mapa =..., posicao = 5,11,
282
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 295

CasadoCódigo Capítulo21. Destruindoosfantasmas:omundodarecursão
quantidade = 1)
fogefoge.rb:remove:112 (mapa =..., posicao = 5,10,
quantidade = 2)
fogefoge.rb:remove:112 (mapa =..., posicao = 5,9, quantidade = 3)
fogefoge.rb:remove:112 (mapa =..., posicao = 5,8, quantidade = 4)
Nesseinstante,nanovalinha 109,eleencontraquequantidadevale 0
eparaarecursão.Aoretornardecadaumadasinvoca ções(darecursão),o
jogocontinuanormalmente.Podemostestá-loeverquerealmentefunciona:
...
X X XXX X XXX X
X HXXX X X X X
XXX*FXXFX X X
...
X X XXX X XXX X
X XXX X X X X
XXXH X X X
Recursãoéoatodeumafun çãochamarasimesma.Basedarecursãoéo
critérioondeessarecursãopara,casocontrárioelaexecutariaindetermina-
damente oquepoderiacausarumestourodapilhadeexecu ção.
Reparecomonossocódigofinalnãopossuimaisola ço,utilizaarecursão
eapilhadeexecu çãoparaqueoacumulador( quantidade)contequantas
casasforamlimpasnomapa:
def remove mapa, posicao, quantidade
if quantidade == 0
return
end
posicao = posicao.direita
mapa[posicao.linha][posicao.coluna] = " "
remove mapa, posicao, quantidade - 1
end
Reparequefomoscapazesdeexecutararecursãoeaitera ção(ola ço)para
atingiromesmoresultado.
283
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 296

21.5. Basedarecursão:distânciaquatrooumuro CasadoCódigo
21.5 Base da recursão : distância quatro ou
muro
Naprática,nossabombaéfortedemais,queremosqueelasejaincapazde
explodirummuro.Émuitoincomumqueumjogopermitaessetipodeex-
plosão,portantonãopodemoscontinuarseaposi çãoatualforummuro.
Naimplementa çãoantiga,deumla ço,poderíamosutilizarumacondi ção
eum break:
def remove mapa, posicao, quantidade
for direita in 1..quantidade
posicao = posicao.direita
if mapa[posicao.linha][posicao.coluna] == "X"
break
end
mapa[posicao.linha][posicao.coluna] = " "
end
end
Nanossaversãoatual,recursiva,dafun ção remove,bastaadicionarmos
umanovabase,setemmuro,para:
def remove mapa, posicao, quantidade
if quantidade == 0
return
end
posicao = posicao.direita
if mapa[posicao.linha][posicao.coluna] == "X"
return
end
mapa[posicao.linha][posicao.coluna] = " "
remove mapa, posicao, quantidade - 1
end
Resultandoem:
X X XXX X XXX X
X HXXX X X X X
XXX*FXXFX X X
284
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 297

CasadoCódigo Capítulo21. Destruindoosfantasmas:omundodarecursão
...
X X XXX X XXX X
X XXXFX X X X
XXXH XX X X X
Podemosextrairagoraumafun ção execuca_remocao:
def executa_remocao mapa, posicao, quantidade
if mapa[posicao.linha][posicao.coluna] == "X"
return
end
mapa[posicao.linha][posicao.coluna] = " "
remove mapa, posicao, quantidade - 1
end
def remove mapa, posicao, quantidade
if quantidade == 0
return
end
executa_remocao mapa, posicao.direita, quantidade
end
21.6 Recursão para todos os lados : busca em
profundidade
Pormaisquenossabombarespeitemuros,nossoefeitoaindaébemestra-
nho. Tradicionalmente,emjogos,umabombaexplodeparatodososlados
aomesmotempo,andando,porexemplo,4casasnomáximoparaqualquer
direção,queéseualcance.
Dadoomapaaseguir,o mapa4.txt:
XXXXXX
XHXXXX
X*FX X
XXFX X
XFFFFX
XXXXXX
285
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 298

21.6. Recursãoparatodososlados:buscaemprofundidade CasadoCódigo
Aexplosão andaquatrocasas,detodasasmaneiraspossíveis.Notequão
longeeladeveriaconseguirchegar,somenteatéosfantasmasmarcadocomo
número4nomapaaseguir:
XXXXXX
XHXXXX
X*1X X
XX2X X
X4345X
XXXXXX
Emoutraspalavrassomenteumfantasmasobreviveria. Comocalcular
isso?Queremosandarquatrodedistância,por todos os caminhos possíveis,a
partirdenossabomba.
Umasolu çãoinicial,comquetemosquetomarumcuidado,équenão
podemosfazerdois for,de -4a +4:
for movimento_linha in -4..4
for movimento_coluna in -4..4
linha = nova_posicao.linha + movimento_linha
coluna = nova_posicao.coluna + movimento_coluna
mapa[linha][coluna] = " "
end
end
Omovimentodenossoheróiresultariaem:
XXXXXX
X XXXX
XH X X
XX X X
X X
XXXXXX
Implementaçãocompletamenteerrada.Explodimosparatodososlados.
Nãoéessaadescri çãodaexplosão.Devemospercorrertodososcorredores
emquatrodedistânciadopontodeorigem,elimpartodoseles,nadamais.
Vamosolharparanossaimplementa çãorecursiva:
286
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 299

CasadoCódigo Capítulo21. Destruindoosfantasmas:omundodarecursão
def remove mapa, posicao, quantidade
if quantidade == 0
return
end
executa_remocao mapa, posicao.direita, quantidade
end
Emvezdetentarmosexplodirsomenteadireita,tentamosasquatrodire-
ções,issoé,tentamosandarquatrodedistânciaemtodososcaminhospossí-
veis:estamosbuscandotodasascasasqueconseguimosalcan çarcomquatro
passos.
def remove mapa, posicao, quantidade
if quantidade == 0
return
end
executa_remocao mapa, posicao.direita, quantidade
executa_remocao mapa, posicao.esquerda, quantidade
executa_remocao mapa, posicao.cima, quantidade
executa_remocao mapa, posicao.baixo, quantidade
end
Claro,adicionamosasfun çõesdedire çãoaoherói:
class Heroi
# ...
def cima
calcula_nova_posicao "W"
end
def esquerda
calcula_nova_posicao "A"
end
def baixo
calcula_nova_posicao "S"
end
end
Carregamosoquartomapa:
287
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 300

21.7. Resumindo CasadoCódigo
def joga(nome)
mapa = le_mapa(4)
# ...
end
Eagoratentamosrodar:
XXXXXX
XHXXXX
X*FX X
XXFX X
XFFFFX
XXXXXX
Para onde deseja ir?
S
XXXXXX
X XXXX
XH X X
XX XFX
X X
XXXXXX
21.7 Resumindo
Vimosnestecapítulocomoimplementaroalgoritmodedestrui çãodeum
fantasma,paraissorefatoramosmaisnossocódigo,implementamosumla ço
atravésdeumloopedeinvocaraprópriafun ção,arecursão.
Encontramosabasedarecursãoquandopercebemosqueapilhadeexe-
cuçãoestouravaàmedidaqueentravaemumla çoinfinito(elaseinvocavaaté
estourar).Ecomarecursãofoimuitosimplespermitirandarquatropassos
paratodososlados:foipossívelbuscartodososquadradosdomapaqueestão
aatéquatropassosdistância,umabuscachamada busca em profundidade.
288
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 301

Capítulo22
Exercíciosextras:jogodo
foge-foge
Aquivocêencontraexercíciosextrasparasoltarsuaimagina çãoepraticar
lógicadeprograma çãonalinguagemRuby.
22.1 Melhorando o Jogo do foge-foge
1) Suportetantoletrasmaiúsculasquantominúsculasaosemovimentarno
mapa.
2) Seojogadornãopodesemovimentar,perdeuojogo. Paraverificarse
elenãopodesemovimentar,crieumafun çãoqueconfirasepelomenos
umadasquatroposi çõeséválida.Sepelomenosumaforválida,podese
movimentar,casocontrário,nãopode.
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 302

22.2. Outrosdesafios CasadoCódigo
3) Aumenteospontosdojogador:5pontosparacadamovimentoefetuado.
4) Crieumnovofantasma: elenuncatentaseafastardoherói. Paraisso,
elevê: seoheróiestáacima,nãovaiprabaixo. Seestáabaixo,nãovai
paracimaetc.Notequeporvezesofantasmapoderádecidirficarparado
mesmoquehajaumacasaaoladodele.
5) Graveeleiadeumarquivoqueméojogadorqueobtevemaispontos.
6) Casooarquivoderanknãoexista,considerequenãoháninguémnorank.
7) Perguntequaladificuldadequeojogadordeseja,fácil,normalouimpos-
sível. Nomodofácilojogadorandadoispassoseosfantasmasum. No
impossível,osfantasmasandamdoiseoheróium. Nomodofácilojo-
gadorganhasomente1pontopormovimento,nonormal5pontoseno
difícil20pontos.Paraimplementaressafuncionalidade,vocêprecisaar-
mazenartantoadificuldadequantoonúmerodoturno.Seoturnoforpar
ouímparvocêsabequemdevesemover.
8) Seonúmerodefantasmasforzero,ojogadorganhaeleva 10000pontos.
9) Omapaaseguirapresentaumbug.Seofantasmanãotemparaondeir,
eledesaparece. Queremosque,casoelenãotenhaparaondeir,eledeve
ficarparado:
XXXXXX
XHXXXX
X XXFX
X XXFX
X XXFX
XXXXXX
22.2 Outros desafios
1) Graveemumarquivoos10jogadoresquetiverammaispontos.
Paramanteropadrãode“outrosdesafios”,podiaterpelomenos2nesta
lista....]
290
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 303

Capítulo23
InstalandooRuby
Ainstala çãoemcadaplataformaéfeitademaneiradiferente.Nofinal,para
testaraversãodoRubydisponívelvocêpodeexecutarocomando:
ruby -v
23.1 Instalação no Windows
VocêpodeutilizaroprojetoRubyinstallerparainstalaroRubyemumambi-
enteWindows.http://rubyinstaller.org/
Apósinstalado,nomenuIniciarvocêencontrao Start command prompt
with Ruby, onde será inicializado um terminal do Windows (command
prompt)comocomando rubydisponível.Váparaoseudiretóriodetrabalho
usandoocomando cdepronto, rubyneles!
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 304

23.2. InstalaçãonoLinux CasadoCódigo
23.2 Instalação no Linux
ParaDebianeUbuntuainstala çãoédireta:
sudo apt-get install ruby-full
ParaoutrasversõesdeLinuxsigaotutorialespecíficonadocumenta ção
doRubyem:
https://www.ruby-lang.org/en/documentation/installation/
23.3 Instalação no MacOSX
ApartirdaversãoMaverickdoMacOSX,oRuby2.0jáveminstalado.Basta
abriraaplica çãochamada Terminal. JáasversõesMountainLion,Lion
eSnowLeopardtrazemoRuby 1.8.7. Tudooquefizemosnestelivroé
independentedaversãodoRubyecompatíveldesdea 1.8.7,massedesejar
instalarumaversãomaisrecentevocêpodeutilizarogerenciadordepacotes
HomeBreweexecutar:
brew install ruby
23.4 O editor de texto
AoescreverestematerialutilizamosoeditordetextoSublime.Elefunciona
paraasplataformasMacOSX,LinuxeWindowseéaferramentasugerida
aoacompanharolivro.
Comoalternativa,noambienteMacOSX,outraop çãobastantepopular
nocome çoéoTextmate.
JánoambienteLinux,umaalternativasimpleséoGedit.
NoWindows,jamaisutilizeoblocodenotas( notepad).Senãopordiver-
sosoutrosproblemas,eletrazadificuldadedesalvaroarquivocomaextensão
adequada.ComoalternativaaoSublimetentesolu çõescomooNotepad++,
jEditetc.
Umasolu çãoquefuncionanastrêsplataformas,masmaispesadaeque
seriaumsegundopasso,éoAptana,aIDEbaseadanoEclipse.
292
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 305

CasadoCódigo Capítulo23. InstalandooRuby
NãorecomendoousodeEmacsouVicomoeditoresdetextoduranteo
aprendizadodestematerialemambientesMacOSXouLinuxnesseinstante.
Ofocodestelivroéoaprendizadodelinguagemdeprograma ção,quejátrará
desafiossuficientesparaessaetapa. Nofuturo,sinta-seàvontadeparaen-
contrarqualaferramentaqueseencaixamelhorcomsuamaneira eadesua
equipe detrabalhar.
293
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 306

E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 307

Capítulo24
Comocontinuar
24.1 Praticar
Osconceitosdeprograma çãosãofundamentaisparaodiaadiadeumde-
senvolvedor.Claroqueodomíniovemcomotempo.Simularumcódigode
cabeça,bateroolhoeentenderondeestãoospossíveiserros,tudoissovem
comanosdeexperiência. Assimcomoacomidadenossosavôsédeliciosa
poiselesprepararamomesmopratotodasemanapor60anos,nãoadianta
tentarpularpassos:pratique.Escrevaprogramas,joguinhos,simuladoresetc.
Ocaminhomaiscomuméodepraticarbastante,sentiranecessidadede
aprendermaisestruturas,depoisalgoritmos,refor çaramaneiradetrabalhar
comOrienta çãoaObjetoseentãoteravisãodecomooutraslinguagensde
programaçãofuncionam.
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 308

24.2. Estruturadedadosealgoritmos CasadoCódigo
24.2 Estrutura de dados e algoritmos
Paratrabalharcomdadosnamemória,éimportanteentenderumpouco
comofuncionamestruturasdedadosbásicas. Nestematerialvimoscomo
funcionamumarray,umdicionárioassociativo,eatémesmoumapilha(a
pilhadeexecu ção). Comopassardotempo,conhecermelhoressaseou-
trasestruturasajudaráaentendermelhoroqueacontecenamemóriaecomo
resolverproblemaslógicosdemaneiraelegante,semtentarreinventararoda.
Aomesmotempo,parautilizartaisestruturasdedadosdemaneiraótima,
aprendemosdeterminadosalgoritmosqueresolvemproblemasdediversas
maneiraspossíveis,sempretirandoproveitodoquecadaumadessasestrutu-
rastrazdemelhor.
24.3 Orientação a Objetos?
Ofocodestematerialnãoresidenoensinodeestruturasdedados,masde-
cidimosirumpoucoalémemostrarmétodosemclasses,umavezquetudo
(sim,tudo)emRubyéumobjeto,alémdealgumasboaspráticasecodesmells
ligadosaoassunto. Existemuitomaisnomundodeorienta çãoaobjetos:a
facilidadedemanuten çãodenossocódigodependemuitodeconheceroseu
bomuso. Umpontointeressantedecontinua çãoparaseusestudosemum
tópicomaisavan çadodoqueaintrodu çãoaprograma çãoatualéomundo
deorienta çãoaobjetos masnãoseesque ça,todoensinamentodevecontero
ladobomeruimdediversasfuncionalidadesdemonstradas.NocasodeRuby,
issoenglobaoaspectoorientadoaobjetos,inicializadores,classeaberta,mé-
todosdeclasse,heran ça,mixins,polimorfismo(comoatravésdeducktyping)
emuitomais.
24.4 Competições de programação da ACM
Táticascomoaapresentadaaqui,deutiliza çãodematrizespararesolverum
problemadelógica,sãoextremamentecomunsnascompeti çõesdeprogra-
maçãonomundoafora.
TodoanoérealizadaaACMICPC,acompeti çãomaisfamosadaárea,
cujosexercíciossefocamnodesenvolvimentodealgoritmospararesolverdi-
296
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 309

CasadoCódigo Capítulo24. Comocontinuar
versostiposdeproblemas.Aprovaclassificatóriaparaomundialérealizada
noBrasilcomonomedeMaratonadePrograma ção.Énecessárioseraluno
dealgumafaculdadebrasileira(dequalquerárea)parapoderparticipar.
Oestudoparaessasprovasservecomograndedesafioparanossashabi-
lidadeslógicas,alémdeaprendermosmaisafundosobrealinguagemque
utilizamospararesolverseusproblemas.Porexemplo,oscasosdo +1e -1
queutilizamossãoumperigoparaumaaplica ção:esquecerumdelespode
quebrarojogoecomissoperderumusuáriocompletamente. Oquefazer?
Umatáticasimples,típicademaratona,éseprotegerdasbordas. Seaoler
ummapacolocarmosumabarreirade Xemcadaumdeseuslados,nãopre-
cisamosmaisvalidarcomos ifsdasbordas,afinalelas sempretêmum X!
Técnicascomoessasãoúteisparaquemprogramaumcódigomaismatemá-
tico.
Poroutrolado,osdesafioslógicosincentivamnossacapacidadederesol-
verproblemasededescrevê-losemcomandosparaocomputador. Setiver
achance,treineeparticipe! Nemquesejapeloprazerdeaprender. Nãose
assustecomoníveldedificuldadedosexercícios,comececomosmaisle-
veseàmedidaqueestudaestruturadedados,algoritmoseoutrostópicos,os
exercíciosmaisavan çadosvãosetornandomaisnaturais.
24.5 Outra linguagem?
Apóssesentirfamiliarizadoosuficientecomumalinguagem,umaop çãode
muitosprogramadoresédarumaolhada,ouatémesmoseaventurardecorpo
ealma,emoutralinguagemdeprograma ção. SeRubyfoisuaprimeiralin-
guagem,vocêpodeaprenderagoraJavascriptparaaplicarprograma çãoaos
navegadoresweb,JavaouC #paradesenvolveraplicativosmobileouweb,ou
alinguagemCquetraráumconhecimentomaisavan çadodecomoocom-
putadoreaslinguagensfuncionam.PHPpermiteacria çãodesites,ePython
ébastanteutilizadonacria çãodeprogramasaseremrodadosnoterminal,
serviçosetc.Alémdisso,oJavaébaseparaodesenvolvimentoAndroid,en-
quantoSwiftéparaodesenvolvimentoiOS.
Omundodaslinguagensémuitogrande,dêumpassoporvez.Somente
quandosesentirbemosuficientecomaquestãodeprograma çãoescolhauma
297
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 310

24.6. Compartilheeboajornada CasadoCódigo
próximalinguagemparasaciarsuacuriosidade. Avanceemsuacarreirade
acordocomocaminhoquepretendeseguir.
24.6 C ompartilhe e boa jornada
Compartilheseucódigocomoutros. Useeleparapegarfeedbackdeou-
trosprogramadoreseaprendacomocódigodeles. SitescomooGitHube
softwaresdecontroledeversão(comoogit)ajudamcomessatarefa.Aocriar
suacontagratuitanoGitHubecompartilharseucódigocomoopensource,
poderáfacilmenteconversarcomoutrosamigosprogramadoressobreelee,
quemsabe,atécontribuircomoutrosourecebercontribui çõesemseuspro-
jetos.
Bonsestudos,boajornadaeboacarreira!FiconoaguardopeloTwitter
@guilhermecaelumdesabercomoaprograma çãomudousuavida.
298
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com

## Página 311

CasadoCódigo ÍndiceRemissivo
ÍndiceRemissivo
Boaprática:buscarqueminvocaan-
tesderefatorar,267
Boaprática:earlyreturn,59
Boa prática: encapsulamento de
comportamento,46
Boaprática:explorandoadocumen-
tação,139
Boaprática:Tell,don’task,270
Codesmell:classesanêmicas,272
Codesmell:comentários,28
Codesmell:copyepaste,31
Codesmell:featureenvy,264
Codesmell:Magicnumbers,38
Codesmell:variáveissemcontrolede
escopo e variáveis globais,
49
Oqueérefatora ção,21
Pequenasrefatora çõesespecíficasda
linguagem,60
Refatoração:extrairarquivo,170
Refatoração:extrairvariável,39
299
E-book gerado especialmente para Fabio Oliveira - fabiobom36@hotmail.com