---json
{
  "id": "desenvolva_jogos_com_html5_canvas_e_javascript",
  "title": "Desenvolva jogos com HTML5 Canvas e JavaScript",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Desenvolva jogos com HTML5 Canvas e JavaScript.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "canvas",
    "com",
    "desenvolva",
    "html5",
    "java",
    "javascript",
    "jogos",
    "linguagens"
  ],
  "perguntas_tipo": [
    "Como utilizar Desenvolva jogos com HTML5 Canvas e JavaScript?",
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

# Desenvolva jogos com HTML5 Canvas e JavaScript

> **Arquivo Original:** `Desenvolva jogos com HTML5 Canvas e JavaScript.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

CasadoCódigo
Introdução
Sevocêchegouatéestelivro,éporqueestáinteressadoemdesenvolverjo-
gos. Aquifocareinodesenvolvimentodejogosparaaweb,usandoatec-
nologia Canvas,presentenaespecificaç ãodoHTML5esuportadaporto-
dososmaioresbrowsersmodernos,emsuasversõesmaisatualizadas. Pre-
tendomostrarquedesenvolverjogoséumatarefanarealidadesimples,eque
nãoexigegrandescurvasdeaprendizadoscomframeworksmonstruosos—
obásicooferecidopeloambientedonavegadoréosuficienteparacome çar!
Tudooquevocêprecisaráédeumbrowseratualizadoeumbomedi-
tordetextos.EmambienteWindows,émuitocomumousodo Notepad++
(http://notepad-plus-plus.org).CasovocêuseLinux,ébemprovávelquesua
distribuiçãojávenhacomumeditorquesuportecoloraç ãodesintaxepara
váriaslinguagens(GEdit,KWrite,etc.).Noentanto,eurecomendoveemente-
menteousodo Brackets(http://brackets.io),quefoiondeeucrieioscódigos.
Émultiplataforma(funcionaemWindows,Linux,MacOSX)erealizaauto-
completaremcódigoJavaScriptdeformabastanteeficiente.
Ojogoquevocêvaicriarjáestádisponívelnaweb.Vocêpodejogá-loa
qualquermomentoem:
http://gamecursos.com.br/livro/jogo
EstareisemprepresenteeatuantenoseguintegrupodoGoogleGroups,
comoformadeinteragircommeusleitores:
http://groups.google.com/forum/#!forum/livro-jogos-html5-canvas
Porfim,todososcódigoseimagensestãodisponíveisem(emboraeu
aconselhevocêa digitaroscódigoseusarosprontosnodownloadapenas
parareferênciaemcasodedúvidas):
http://github.com/EdyKnopfler/games-js/archive/master.zip
i

## Página 3

CasadoCódigo
Bomestudo!
ii

## Página 4

CasadoCódigo Sumário
Sumário
1 Fundamentos 1
1.1 IntroduçãoaoHTML5Canvas . . . . . . . . . . . . . . . . . . 3
1.2 Come çandoadesenhar . . . . . . . . . . . . . . . . . . . . . . 6
1.3 Animaçõescom requestAnimationFrame. . . . . . . . . . . . 22
1.4 OrientaçãoaobjetoscomJavaScript . . . . . . . . . . . . . . 26
2 O loop de animaç ão 35
2.1 Introduçãoesprites . . . . . . . . . . . . . . . . . . . . . . . . 35
2.2 TesteparaaclasseAnimacao . . . . . . . . . . . . . . . . . . . 38
2.3 DesenvolvaaclasseAnimacao . . . . . . . . . . . . . . . . . . 41
2.4 ImplementeaclasseBola . . . . . . . . . . . . . . . . . . . . . 45
3 A interaç ão com o jogador — leitura apurada do teclado 49
3.1 EventListenerseoseventoskeydownekeyup . . . . . . . . . 50
3.2 Detectandoseumateclaestáounãopressionada . . . . . . . 55
3.3 Efetuandodisparos—detectandosomenteoprimeirokeydown 58
4 Folhas de sprites — spritesheets 69
4.1 Conceitoeabordagemutilizada . . . . . . . . . . . . . . . . . 69
4.2 Carregandoimagensefazendorecortes(clipping) . . . . . . 72
4.3 Animaçõesdesprite—aclasseSpritesheet . . . . . . . . . . 75
4.4 Controleoheróipelotecladoevejasuaanimaç ão . . . . . . 80
iii

## Página 5

Sumário CasadoCódigo
5 Detec ção de colisões 87
5.1 Colisãoentreretângulos . . . . . . . . . . . . . . . . . . . . . 87
5.2 TestedaclasseColisor . . . . . . . . . . . . . . . . . . . . . . . 90
5.3 AclasseColisor . . . . . . . . . . . . . . . . . . . . . . . . . . 93
5.4 Criandoumspritecolidível . . . . . . . . . . . . . . . . . . . . 95
5.5 Melhorandoocódigo . . . . . . . . . . . . . . . . . . . . . . . 98
6 Iniciando o desenvolvimento do jogo 107
6.1 Animaçãodefundocomefeitoparallax . . . . . . . . . . . . 107
6.2 Controledanavenahorizontalenavertical . . . . . . . . . . 118
6.3 Efetuandodisparos . . . . . . . . . . . . . . . . . . . . . . . . 123
7 Criando inimigos 129
7.1 Primeirotestecomnaveeinimigos . . . . . . . . . . . . . . . 130
7.2 AclasseOvni . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
7.3 Adicionandofundoemparallax . . . . . . . . . . . . . . . . . 135
7.4 Adicionandocolisão . . . . . . . . . . . . . . . . . . . . . . . . 139
7.5 Estamosexperimentandolentidão! . . . . . . . . . . . . . . . 145
7.6 Excluindoosobjetosdesnecessários . . . . . . . . . . . . . . . 151
8 Incorpore animaç ões, sons, pausa e vidas extras ao jogo 155
8.1 Organizandoocódigo . . . . . . . . . . . . . . . . . . . . . . . 156
8.2 Animaçãocronometrada . . . . . . . . . . . . . . . . . . . . . 162
8.3 Animandoanavecomspritesheets . . . . . . . . . . . . . . . 165
8.4 Criandoexplosões . . . . . . . . . . . . . . . . . . . . . . . . . 169
8.5 Pausandoojogo . . . . . . . . . . . . . . . . . . . . . . . . . . 175
8.6 Sonsemúsicadefundo . . . . . . . . . . . . . . . . . . . . . . 179
8.7 Teladeloading . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
8.8 Vidasextras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
8.9 Pontuação(score) . . . . . . . . . . . . . . . . . . . . . . . . . 190
8.10 TeladeGameOver . . . . . . . . . . . . . . . . . . . . . . . . 192
iv

## Página 6

CasadoCódigo Sumário
9 Publique seu jogo e torne-o conhecido 197
9.1 Hospede-oemumserviçogratuito . . . . . . . . . . . . . . . 197
9.2 Linkandocomasredessociais . . . . . . . . . . . . . . . . . . 203
Bibliografia 213
v

## Página 8

Capítulo1
Fundamentos
Aquicome çaumafascinantejornadapelossegredosdeumatecnologiaque,
naverdade,nãopossuisegredoalgum.Trata-sedo Canvas,umadasmaravil-
hasdoHTML5.
OCanvaséumaárearetangularemumapáginawebondepodemos
criardesenhosprogramaticamente,usandoJavaScript(alinguagemdepro-
gramaçãonormaldaspáginasHTML).Comestatecnologia,podemoscriar
trabalhosartísticos,animaçõesejogos,queéoassuntocentraldestelivro.
ComoCanvas,aolongodoscapítulos,iremosdesenvolverojogoda
figura1.1:

## Página 9

CasadoCódigo
Figura1.1:Jogodesenvolvidoaolongodolivro
Estelivroécompostopelosseguintescapítulos:
1. Fundamentos:nestecapítulo,aprendacomofuncionaoCanvas,como
criaranimaçõesviaprogramaç ãoetambémno çõesdeOrientaç ãoaobje-
tosemJavaScript,paraquenossoscódigossetornemmaisorganizadose
reaproveitáveis;
2. O loop de animação: controleaanimaç ãodeseusjogosdeformaefi-
ciente.Conhe çaoconceitode spriteseaprendaagerenciá-losemumaani-
mação;
3. A interação com o jogador — leitura apurada do teclado: saibacomo
capturareventosdotecladodemaneiraeficienteparajogos;
4. Folhas de sprites — spritesheets: animeoselementosdeseujogoindi-
vidualmenteusandoimagenscontendotodososquadrosdeumaanimaç ão;
5. Detecção de colisões: aprendaadetectarquandooselementosdeum
jogo“tocam”unsaosoutrosnatelaeexecuteasaçõesadequadas;
6. Iniciando o desenvolvimento do jogo: umjoguinhodenavecome çará
atomarformausandotodososelementosaprendidosatéentão;
7. Criando inimigos: adicioneverdadeiraemo çãoaoseujogo,dando
2

## Página 10

CasadoCódigo Capítulo1. Fundamentos
aoheróialguémaquemenfrentar. Usaremosintensivamenteadetecç ãode
colisões;
8. Incorpore animações, sons, pausa e vidas extras ao jogo: comtodosos
conceitosaprendidosebemfixados,vocêverácomoéfácilestenderojogoe
adicionarnovoselementos.Aofimdocapítulo,vocêterásugestõesdemel-
horiasquevocêmesmopoderátentarrealizar,comoexercício;
9. Publique seu jogo e torne-o conhecido: umpassoapassodecomo
publicarseujogonawebedivulgá-lonasredessociais.
Importante:prepareiumpacotedearquivoscontendotodososcódigos,
imagensesonsutilizados. Emcadanovoarquivoquecriarmos,indicareio
nomedorespectivoarquivonessepacote.Realizeseudownloadnoendere ço:
http://github.com/EdyKnopfler/games-js/archive/master.zip
Antesdecome çarmosadesenvolverumjogoemespecífico,éimportante
noshabituarmosaalgumasfun çõesdatecnologiaCanvas. Oqueestáes-
perando?Vamoscome çaroaprendizado!
1.1 I ntrodução ao HTML5 Canv as
ParacriarumCanvasemumapáginaHTML,utilizamosatag <canvas>.Os
atributos widthe heightinformamalarguraeaaltura,respectivamente,
daáreadedesenho.Éimportantetambéminformarum idparapodermos
trabalharcomelenocódigoJavaScript:
<canvas id="nome_canvas" width="largura" height="altura">
</canvas>
Entreastagsdeaberturaefechamento,podemoscolocaralgumamen-
sagemindicandoqueobrowsernãosuportaessatecnologia.Casoobrowser
asuporte,esseconteúdoéignorado:
<canvas id="meu_canvas" width="300" height="300">
Seu navegador não suporta o Canvas do HTML5. <br>
Procure atualizá-lo.
</canvas>
Osatributos widthe heightdatag <canvas>sãoobrigatórios,pois
sãoosvaloresusadosnageraç ãodaimagem.OCanvaspodereceberdimen-
3

## Página 11

1.1. IntroduçãoaoHTML5Canvas CasadoCódigo
sõesdiferentesviaCSS,noentanto,seuprocessamentosempreseráfeitous-
andoasdimensõesinformadasnatag.SeasdimensõesnoCSSforemdifer-
entes,obrowserampliaoureduzaimagemgeradaparadeixá-ladeacordo
comafolhadeestilo.
DadoumCanvascomdimensões100x100pixels:
<canvas id="meu_canvas" width="100" height="100"></canvas>
AseguinteformataçãoCSSfaráaimagemserampliada:
#meu_canvas {
width: 200px;
height: 200px;
}
Contexto gráfico
ParadesenharnoCanvas,éprecisoexecutarumscriptapóseletersido
carregado.Nestescript,obteremoso contexto gráfico,queéoobjetoquere-
alizadefatoastarefasdedesenhonoCanvas.
Umamaneiraécriarumatag <script>apósatag <canvas>:
<!DOCTYPE html>
<html>
<head>
<title>Processando o Canvas após a tag</title>
</head>
<body>
<canvas id="meu_canvas" width="200" height="200"></canvas>
<script>
// Aqui obteremos o contexto gráfico e trabalharemos com o
// Canvas
</script>
</body>
</html>
4

## Página 12

CasadoCódigo Capítulo1. Fundamentos
Tambémémuitocomumdesenharmosemeventosqueocorremapósa
páginatersidocarregada. Istoéútilcasoqueiramoscolocarosscriptsna
seção <head>dodocumentoHTML:
<!DOCTYPE html>
<html>
<head>
<title>Processando o Canvas na seção HEAD</title>
<script>
window.onload = function() {
// Aqui trabalharemos com o Canvas
}
</script>
</head>
<body>
<canvas id="meu_canvas" width="200" height="200"></canvas>
</body>
</html>
Nocódigo,nósreferenciamosoCanvaseobtemosocontextográfico.O
Canvaséreferenciadocomoqualquerelementoemumapágina;ocontexto
éobtidopelométodo getContextdoCanvas.Comoparâmetro,passamos
umastringidentificandoocontextodesejado. Nestelivro,usaremosocon-
texto 2d(“d”emminúsculo!):
<canvas id="meu_canvas" width="200" height="200"></canvas>
<script>
// Referenciando o Canvas
var canvas = document.getElementById('meu_canvas');
// Obtendo o contexto gráfico
var context = canvas.getContext('2d');
</script>
5

## Página 13

1.2. Começandoadesenhar CasadoCódigo
O sistema de coordenadas do Canvas
ParaposicionarmososdesenhosnoCanvas,pensamosnelecomoum
enormeconjuntodepontos.Cadapontopossuiumaposiç ãohorizontal(x )
eumavertical(y ).
Oponto(0,0)(lê-se: zeroem xezeroem y)correspondeaocanto
superioresquerdodoCanvas:
Figura1.2:SistemadecoordenadasdoCanvas
1.2 C omeçando a desenhar
MétodosfillRect e strokeRect
Umavezobtidoocontextográfico,podemosconfigurarváriaspropriedadese
chamarneleosmétodosdedesenho.Porexemplo,paradesenharretângulos,
podemosusarosmétodos:
•fillRect(x, y, largura, altura):pintacompletamenteuma
árearetangular;
•strokeRect(x, y, largura, altura): desenhaumcontorno
doretângulo.
Osvalores xe ycorresponderãoàposiç ãodocantosuperioresquerdo
doretângulo.Apartirdaí,oretângulovaiparaadireita(largura)eparabaixo
(altura).
6

## Página 14

CasadoCódigo Capítulo1. Fundamentos
VejaumexemplodecódigoparadesenharumretângulonoCanvas,
nossoprimeiroexemplopráticocompleto:
<!-- arquivo: retangulos-1.html -->
<!-- este código vai dentro do body -->
<canvas id="meu_canvas" width="200" height="200"></canvas>
<script>
// Canvas e contexto
var canvas = document .getElementById('meu_canvas');
var context = canvas.getContext('2d');
// Desenhar um retângulo
context.fillRect(50, 50, 100, 100);
</script>
Nãoésimplesdefazer?Oresultadoseráumsimplesretângulopreto.Seu
cantosuperioresquerdolocaliza-senoponto(50,50),eelepossui100pixels
delargurapor100pixelsdealtura:
Figura1.3:Retângulodesenhadocom fillRect
Setrocarmos fillRectpor strokeRect,veremosapenasocontorno:
Figura1.4:Retângulodesenhadocom strokeRect
7

## Página 15

1.2. Começandoadesenhar CasadoCódigo
Propriedades fillStyle, strokeStyle e lineWidth
Podemosconfiguraralgumaspropriedadesdocontexto,deformaaescol-
herascoreseespessuras:
•fillStyle: cordopreenchimento
•strokeStyle: cordalinha
•lineWidth:espessuradalinhaempixels
<!-- arquivo: retangulos-2.html -->
<canvas id="meu_canvas" width="200" height="200"></canvas>
<script>
// Canvas e contexto
var canvas = document .getElementById('meu_canvas');
var context = canvas.getContext('2d');
// Preenchimento vermelho
context.fillStyle = 'red';
context.fillRect(50, 50, 100, 100);
// Contorno azul, com espessura de 3px
context.lineWidth = 3;
context.strokeStyle = 'blue';
context.strokeRect(50, 50, 100, 100);
</script>
Figura1.5:Configurandoaspropriedadesdopreenchimento(fillStyle)econ-
torno(strokeStyle)
8

## Página 16

CasadoCódigo Capítulo1. Fundamentos
Paths (caminhos)
Desenhosmaiscomplexospodemserdesenhadoscomo paths(camin-
hos).Um pathéumconjuntodecomandosdedesenhoqueficamregistrados
namemória,aguardandoosmétodos fill(preencher)ou stroke(contornar)
seremchamados.
Porém,antesdetudo,devemoschamarométodo beginPath(iniciarcam-
inho)paraapagarostraç adosfeitospreviamente.Senãofizermosisso,elesfi-
carãonamemóriaeserãodesenhadosnovamentejuntocomopróximopath:
// Exemplo teórico
// Passo a passo para criar um path:
// Iniciar novo path (apagando desenhos anteriores)
context.beginPath();
// Aqui faço meu desenho
// ...
// Preencher toda a área desenhada
context.fill();
// Contornar a área desenhada
context.stroke();
Porexemplo,podemosdesenharumaestrelausandoosseguintescoman-
dos:
•moveTo(x, y): posiciona a caneta virtual em um determinado
ponto;
•lineTo(x, y):traçaumalinhadopontoatualatéopontoindicado.
9

## Página 17

1.2. Começandoadesenhar CasadoCódigo
Figura1.6:Estrelacriadausando moveT oe lineT o
Esses comandos não desenham as linhas imediatamente, apenas ar-
mazenamasinformaçõesnopath.Devemoschamarométodo strokepara
desenhá-lasdefatonoCanvas:
<!-- arquivo: caminhos.html -->
<canvas id="meu_canvas" width="300" height="300"></canvas>
<script>
// Canvas e contexto
var canvas = document .getElementById('meu_canvas');
var context = canvas.getContext('2d');
// Iniciar o caminho (apaga desenhos anteriores)
context.beginPath();
// Desenhar uma estrela
context.moveTo(75, 250); // Ponto inicial
context.lineTo(150, 50);
context.lineTo(225, 250);
context.lineTo(50, 120);
context.lineTo(250, 120);
context.lineTo(75, 250);
// Configurar a linha
context.lineWidth = 2;
context.strokeStyle = 'red';
// Traçar as linhas do caminho
context.stroke();
10

## Página 18

CasadoCódigo Capítulo1. Fundamentos
</script>
Circunferências e arcos
Sãocriadoscomomesmométodo, arc.Umarcoéumapartedeuma
circunferência,eserveparacriarlinhascurvas.Umacircunferência,parao
Canvas,énadamaisqueumarcode360graus.
Ométodo arcrecebeosseguintesparâmetros:
•x, y: ascoordenadasdopontocentraldacircunferência;
•raiodacircunferênciaempixels;
•ângulo inicialemradianos;
•ângulo finalemradianos;
•sentido: aquivocêpodepassar false(sentidoanti-horário)outrue
(sentidohorário).Esteparâmetroéopcional;seomitido,odesenhoé
feitonosentidoanti-horário.
Figura1.7:Localizaçãodopontocentral,ângulosinicialefinaleopontozero
Osângulospodemestaremqualquerposiç ãonacircunferênciaetêm
de ser informados emradianos, não em graus. Lembra-se das aulas de
trigonometria? Eu também não, mas sabemos quepi radianos é meia
volta(180graus),portanto 2 pivaleumavoltacompleta(360graus). Para
11

## Página 19

1.2. Começandoadesenhar CasadoCódigo
nossasorte,oJavaScriptpossuiaconstante Math.PI,quenosdáovalor
3.141592653589793!
Convertendo de graus para radianos
Afórmulaémuitosimples:
var graus = ... ;
var radianos = graus * Math.PI / 180;
Importante:ométodo arcéusadoemumpath,ouseja,nãodesenhao
arcooucírculonahora.
Oprimeiroarcodafigura 1.7podeentãoserdesenhadocomocomando:
// Exemplo teórico
context.arc(
50, // X (centro)
50, // Y (centro)
40, // Raio
90*Math.PI/180, // Início: 90 graus
270*Math.PI /180, // Término: 270 graus
false // Sentido anti-horário
);
Parafazerooutroarco,bastaescrevermos truenoúltimoparâmetro.
Vamosexperimentarnaprática!Primeiro,vamosinicializarasvariáveis
econfigurarocontextocomaaparênciadesejada:
<!-- arquivo: arcos.html -->
<canvas id="meu_canvas" width="300" height="300"></canvas>
<script>
// Canvas e contexto
var canvas = document .getElementById('meu_canvas');
var context = canvas.getContext('2d');
// Cores e espessura da linha
context.fillStyle = 'gray';
12

## Página 20

CasadoCódigo Capítulo1. Fundamentos
context.strokeStyle = 'black';
context.lineWidth = 2;
// continua...
</script>
Parafazerumarco,devemosiniciarumpath,chamarométodo arc
edepoisfazer fille stroke(ousomenteumdestesdois,sequisermos
somentepreenchimentoousomentecontorno):
// Primeiro arco:
// Novo path
context.beginPath();
// Desenha
context.arc(50, 50, 40, 90*Math.PI/180, 270* Math.PI/180,
false);
// Preenchimento
context.fill();
// Contorno
context.stroke();
// continua...
Sequisermosfazeroutroarco,temosqueiniciarmaisumpath;docon-
trário,odesenhoformadoficaráestranho(figura 1.8).Reparequeaposiç ão
xfoideslocadaparadesenharmosàdireitadoanterior:
// Segundo arco
context.beginPath();
context.arc(150, 50, 40, 90*Math.PI/180, 270*Math.PI/180,
true);
context.fill();
context.stroke();
// continua ...
13

## Página 21

1.2. Começandoadesenhar CasadoCódigo
Figura1.8:Doisarcosdesenhadosjuntosnomesmopath:uméacontinuaç ão
dooutro!
Façatambémumacircunferênciacompleta.Nãoprecisasepreocuparem
converter360grauspararadianos,bastafazeroarcodezeroaté 2 pi.Vamos
omitiroúltimoparâmetro,poistantofazfazermosnosentidohorárioou
anti-horário(jáquevamoscomeçarefinalizarnomesmoponto):
// Circunferência completa
context.beginPath();
context.arc(250, 50, 40, 0, 2*Math.PI);
context.fill();
context.stroke();
Pronto!Temososseguintesdesenhosnapágina:
Figura1.9:Arcoemsentidoanti-horário,arcoemsentidohorárioecircun-
ferênciacompleta,compreenchimentoecontorno
Desenhando imagens
Sevocêjáestáficandopreocupado,pensandosetodososgráficosemum
jogosãocriadosviaprogramaç ão,eutenhoumaboanotíciaparavocê:não
14

## Página 22

CasadoCódigo Capítulo1. Fundamentos
são.Agrandemaioriavemdeimagensjáprontas,elaboradasemprogramas
gráficos.
Paradesenharimagenspré-elaboradasemumCanvas,primeirotemosde
carregaroarquivodeimagem.Oobjeto ImagedoJavaScriptéequivalentea
umelemento <img>napágina,porémsomenteemmemória.Apóscriá-lo,
apontamosseuatributo srcparaoarquivodesejado:
// Exemplo teórico
// Carregando uma imagem programaticamente
var imagem = new Image();
imagem.src = 'minha-imagem.png'; // gif, jpg...
// Obtendo de uma imagem na página
var imagem = document .getElementById('id_da_tag_img');
Convémaguardaraimagemsercarregadaantesdedesenhá-la.Oobjeto
Imagepossuioevento onload,queserádisparadoautomaticamentepelo
browserquandoocarregamentoestivercompleto:
// Exemplo teórico
imagem.onload = function() {
// Aqui trabalhamos com a imagem
}
Estandocarregada, aimagempodeserdesenhadaatravésdométodo
drawImagedo context.Estemétodopodeserchamadodeduasformas:
•drawImage(imagem, x, y, largura, altura):desenhaaim-
ageminteira,naposiç ãoetamanhoespecificados;
•drawImage(imagem, xOrigem, yOrigem, larguraOrigem,
alturaOrigem, xDestino, yDestino, larguraDestino,
alturaDestino):desenhapartedaimagem.
Vamosexperimentaraprimeiraforma.Nopacotededownload,napasta
destecapítulo( 01),estápresenteumasubpastadenome img,contendo
oarquivo ovni.png. Esteseráposteriormenteoinimigoqueanaveirá
15

## Página 23

1.2. Começandoadesenhar CasadoCódigo
enfrentaremnossojogo. Aimagempossui64pixelsdelargurapor32de
altura(64x32).VamoscriarumapáginacomumCanvasecarregá-la:
<!-- arquivo: imagens-1.html -->
<canvas id="meu_canvas" width="500" height="100"></canvas>
<script>
// Canvas e contexto
var canvas = document .getElementById('meu_canvas');
var context = canvas.getContext('2d');
// Carregar a imagem
var imagem = new Image();
imagem.src = 'img/ovni.png ';
imagem.onload = function() {
// Aqui usaremos drawImage
}
</script>
Noevento onload,fazemosumloopparadesenharcincoOVNIs,um
aoladodooutro.Avariável xindicaaposiç ãodecadadesenho:
imagem.onload = function() {
// Começar na posição 20
var x = 20;
// Desenhar as imagens
for (var i = 1; i <= 5; i++) {
context.drawImage(imagem, x, 20, 64, 32);
x += 70;
}
}
Figura1.10:Desenhandoimagenscom drawImage
16

## Página 24

CasadoCódigo Capítulo1. Fundamentos
Sequiséssemosdesenharasimagensampliadasoureduzidas,bastaria
modificaralarguraeaaltura:
// Reduzindo para metade do tamanho
context.drawImage(imagem, x, 20, 32, 16);
// Ampliando para o dobro do tamanho
context.drawImage(imagem, x, 20, 128, 64);
Vamosexperimentarasegundaforma,aquerecebeoitovalores!Napasta
img,temosoarquivo explosao.png,quetambémseráusadonojogo.
Estaimagemcontémumasequênciadeanimaç ão(spritesheet),daqualde-
senhamosumaparteporvez:
Figura1.11:Explosãousadanojogodolivro
Atécnicade clippingconsiteemselecionarumaáreadaimagemoriginal
paraserdesenhada:
Figura1.12:Selecionandoumaáreadaimagempararecorte(clipping )
Osquatroprimeirosvalorespassadosao drawImageindicamoretân-
gulodaáreaenquadrada;osoutrosquatrorepresentamaposiç ãoeotamanho
dodesenhonoCanvas:
17

## Página 25

1.2. Começandoadesenhar CasadoCódigo
<!-- arquivo: imagens-2.html -->
<canvas id="meu_canvas" width="300" height="300"></canvas>
<script>
// Canvas e contexto
var canvas = document .getElementById('meu_canvas');
var context = canvas.getContext('2d');
// Carregar a imagem
var imagem = new Image();
imagem.src = 'img/explosao.png';
imagem.onload = function() {
context.drawImage(
imagem,
80, 10, 60, 65, // Área de recorte (clipping)
20, 20, 60, 65 // Desenho no Canvas
);
}
</script>
Figura1.13:ResultadodoclippingnoCanvas
Nocapítulo4,faremosusointensivodoclippingparacriaranimações.
Métodossave e restore
Umrecursodo contextqueconsiderodeextremaimportânciaépoder
facilmenteguardarconfiguraçõeseretornaraelasmaistarde. Éumaexce-
lentepráticaquecadafun çãooumétodoguardeasconfiguraçõesatuaiseas
restaureantesderetornar.Destaforma,umnãoafetaotrabalhodooutro!
Masjáimaginouterquesalvarcadapropriedadeemumavariável?
18

## Página 26

CasadoCódigo Capítulo1. Fundamentos
// Exemplo teórico
// Não faça isto!
function desenharQualquerCoisa() {
// Guardo as configurações
var fillAnterior = context.fillStyle; // strokeStyle, etc.
// Modifico conforme preciso
context.fillStyle = 'pink';
// Desenho
// ...
// Devolvo as configurações anteriores
context.fillStyle = fillAnterior;
}
Paranossasorte,o contextpossuiométodo save.Estemétodoem-
pilhaconfigurações,fazendoumacópiade todasasconfiguraçõesatuaispara
opróximonível.Penseemcadanívelcomoum“andar”nessapilha.Nóssem-
pretrabalhamosnonívelmaisalto,demodoqueconfiguraçõesqueficaram
emníveisinferiorespermaneceminalteradas:
Figura1.14:Método saveempilhandoconfigurações
Quando queremos retornar às configurações anteriores, chamamos o
métodorestore.Elevoltaparaonívelimediatamenteabaixo:
19

## Página 27

1.2. Começandoadesenhar CasadoCódigo
Figura1.15:Voltandoparaconfiguraçõesanteriorescom restore
Comoexemploprático,começamosdesenhandoumquadradoverde.Em
seguida,subimosnapilhacom saveefazemosumquadradoroxo.Depois
queretornamoscom restore,nossacoratualpassaaseroverdenova-
mente:
<!-- arquivo: save-e-restore.html -->
<canvas id="meu_canvas" width="200" height="200"></canvas>
<script>
// Canvas e contexto
var canvas = document .getElementById('meu_canvas');
var context = canvas.getContext('2d');
// Um pequeno quadrado verde
context.fillStyle = 'green';
context.fillRect(50, 50, 25, 25);
// Salvamos a configuração e subimos na pilha
context.save();
// Agora um quadrado roxo
context.fillStyle = 'purple';
context.fillRect(100, 50, 25, 25);
// Voltamos para o nível anterior na pilha
context.restore();
// Voltou para o verde!
20

## Página 28

CasadoCódigo Capítulo1. Fundamentos
context.fillRect(150, 50, 25, 25);
</script>
Figura1.16:Salvamosacorverdenapilha(save),mudamospararoxoevolta-
mosparaoverde(restore)
Referências sobre oCanv as
Nestetópico,nãoquisnemdelongeesgotarosrecursosdoCanvas,
masdarumabaseparainiciarmosodesenvolvimentodejogos.Indico-
lhealgumasreferênciasparavocêaprimorarseusconhecimentoseter
ideias,muitasideias,paraimplementaremseusjogos:
•W3Schools[3] (http://www.w3schools.com/tags/ref_canvas.asp) :
recomendotodosostutoriaisdeles,porseremsimpleseporvocê
poderrodarosexemplosnahora;
•Core HTML5 Canvas[1](http://corehtml5canvas.com):excelente
livrodeDavidGeary, bemaprofundado, foiaminhaprincipal
fonteparaaprendersobreoCanvas.Oautordiscutenãosomente
osrecursosdaferramenta, mastécnicasealgoritmosextrema-
menteavan çadoseúteisparajogos;
•HTML5 2D game development: Introducing Snail Bait [2] (http:
//goo.gl/Ojvi9T - URL encurtada): do mesmo autor do Core
HTML5Canvas,esteéoprimeirodeumasériedeartigosnaqual
somosguiadosnacriaç ãodeumjogodeplataforma.
21

## Página 29

1.3. Animaçõescom requestAnimationFrame CasadoCódigo
1.3 A nimações com requestAnimationF rame
Tradicionalmente, quando queremos executar tarefas periódicas
em páginas web, usamos os métodos window.setTimeout ou
window.setInterval, passando a função desejada e o intervalo em
milissegundos. Os resultados são satisfatórios para tarefas simples, no
entanto, o controle do tempo pelo browser não é totalmente preciso. É
precisolembrarqueossistemasoperacionaismodernossãomultitarefa,e
mesmoosbrowserspodemterváriasguiasabertas. Nãoépossívelgarantir
queaCPUestejasempredisponívelnomomentoexatodesejado,portantoo
intervaloinformadosempreseráaproximado.
Asoluçãoparajogoseoutrasaplicaçõesquerequeremanimaçõesmais
precisasétrabalharcomciclosmaiscurtos,aproveitandocadamomentoem
queaCPUestádisponívelparanossoaplicativo, enessemomentofazer
ocálculodotempo. Paraisso,aespecificaç ãodoHTML5trazométodo
window.requestAnimationFrame,quedelegaparaobrowseratarefade
executarsuaanimaç ãoomaisrápidopossível,assimqueosrecursosdosis-
temaestiveremdisponíveis.Paraestemétodo,passamoscomoparâmetroa
funçãoquefaráosdesenhosnoCanvas.Temosquechamá-lodeformacíclica,
umavezapósaoutra,damesmaformaquefaríamoscasousássemosocon-
hecido setTimeout:
// Exemplo teórico
// Solicito a execução de uma função
// Não é preciso qualificar o "window" :D
requestAnimationFrame(minhaFuncao);
// Função de animação
function minhaFuncao() {
// Faço um desenho qualquer
// ...
// Solicito o próximo ciclo
requestAnimationFrame(minhaFuncao);
}
Parademonstrarnaprática,façamosumabolinhasedeslocandopelatela.
22

## Página 30

CasadoCódigo Capítulo1. Fundamentos
ObtemosasreferênciasdoCanvasedocontextográfico,definimosaposiç ão
inicialdabolaeseuraioe,emseguida,mandamosumaanimaç ãoiniciar,
chamandoafun ção mexerBola:
<!-- arquivo: requestanimationframe.html -->
<canvas id="meu_canvas" width="300" height="300"></canvas>
<script>
// Canvas e contexto
canvas = document .getElementById('meu_canvas');
context = canvas.getContext( '2d');
// Dados da bola
var x = 20;
var y = 100;
var raio = 5;
// Iniciar a animação
requestAnimationFrame(mexerBola);
// Função de animação
function mexerBola() {
// Aqui uma bolinha se deslocará
}
</script>
Nessafun ção,primeirolimpamosoCanvascomométodo clearRect
docontexto,queserveparalimparumaárea(equivaleadesenharumretân-
gulobranco). Fazemosissoparaapagarrastrosanterioresdabolinha. Em
seguida,nósadesenhamosemsuaposiç ãoatual,alteramossuaposiç ão xe
solicitamosaexecuç ãodopróximociclodeanimaç ão:
function mexerBola() {
// Limpar o Canvas
context.clearRect(0, 0, canvas.width, canvas.height);
// Desenhar a bola
context.beginPath();
context.arc(x, y, raio, 0, Math.PI*2);
context.fill();
23

## Página 31

1.3. Animaçõescom requestAnimationFrame CasadoCódigo
// Deslocar 20 pixels para a direita
x += 20;
// Chamar o próximo ciclo da animação
requestAnimationFrame(mexerBola);
}
Façaexperiências!Vocêpode:
•mexer para a direita: someumvalora x(vejaafigura 1.2);
•mexer para a esquerda: subtraiaumvalorde x;
•mexer para baixo: someumvalora y;
•mexer para cima: subtraiaumvalorde y;
•mexer na diagonal: altereasposiçõestantode xquantode y. Você
podesomarousubtrair,usarvaloresdiferentesparacadaumetc.
Controlando o tempo da animação
Repare que a bolinha anda bem depressa. Isto ocorre porque o
requestAnimationFrame trabalha com ciclos curtos, aproveitando o
primeiromomentoemqueaCPUeobrowserpuderemexecutaroprocessa-
mentodafun çãodeanimaç ão.
Podemoslerorelógiodocomputadoremcadacicloparacontrolaro
movimentodabolinha.SabemosqueoJavaScriptpossuioobjeto Date,que
obtémadataeahoraatuais,equeesseobjetopossuiométodo getTime(),
quedevolveesseinstanteexatoemmilissegundos.Parasaberquantotempo
demorouentreumcicloeoutro(lembre-sedequeessetempoésemprevar-
iável),bastariatiraradiferen çaentreoinstanteatualeoanterior.Sabendoo
intervalodecorrido,épossívelcalcularquantoaboladevesedeslocarnesse
tempo:
// Exemplo teórico
// Obter o instante atual
24

## Página 32

CasadoCódigo Capítulo1. Fundamentos
var agora = new Date().getTime();
// O instante anterior tem de ter sido preservado anteriormente
var anterior = agora; // Foi feito antes
// Tempo decorrido = diferença
var decorrido = agora - anterior;
// Deslocamento da bolinha
var velocidade = 20; // Em pixels por segundo
x += velocidade * decorrido / 1000;
Vamoscolocaristoemprática.Primeiro,guardeomomentoinicialantes
dechamarafun çãodeanimaç ãopelaprimeiravez:
// Momento inicial
var anterior = new Date().getTime();
// Iniciar a animação
requestAnimationFrame(mexerBola);
// Função de animação
function mexerBola() {
// ...
}
Noiníciodafun ção,obtenhaoinstanteatualecalculeotempodecorrido
entreeles:
function mexerBola() {
// Momento atual
var agora = new Date().getTime();
// Diferença
var decorrido = agora - anterior;
// ...
}
Aofinaldafun ção,antesdechamaropróximociclo,guardeomomento
docicloanterior:
25

## Página 33

1.4. OrientaçãoaobjetoscomJavaScript CasadoCódigo
function mexerBola() {
// ...
// Guardamos o instante para o próximo ciclo
anterior = agora;
requestAnimationFrame(mexerBola);
}
Agorapodemoscalcularodesclocamentodabola! Apaguealinhaque
aumenta xem20pixels:
// Apague esta linha
// Deslocar 20 pixels para a direita
x += 20;
Nolugar,calculeodeslocamentoapartirdavelocidadede20pixelspor
segundo(ououtraquepreferir):
// Deslocar 20 pixels por segundo
var velocidade = 20;
x += velocidade * decorrido / 1000;
Abolaagoramove-semaislentamente,poisagoraestamostrabalhando
compixelsporsegundo(anteseram20pixelsporciclo,etínhamosinúmeros
ciclosemumsegundo).Parafazê-lamover-semaisrápido,bastaaumentaro
valor.
1.4 O rientação a objetos com Jav aScript
Conceitos básicos
Nãoéinten çãodestelivroensinarateoriadaorientaç ãoaobjetos(O.O.),
masvoudar-lheumabaseparapodermosusá-lacomJavaScript. Estanão
éumalinguagempuramenteO.O.,noentanto,ojogoquecriaremos,está
projetadodessaforma.Diferenciamosaqui projeto orientado a objetos(apli-
cadoemnossojogo)de linguagem orientada a objetos,quedásuportetotal
aoparadigma(nãoéocasodoJavaScript).
26

## Página 34

CasadoCódigo Capítulo1. Fundamentos
Imagineumjogodecarrosdecorrida.Todososcarrossãopadronizados
nassuascaracterísticas,emboraelaspossamvariar(dentrodessepadrão).
Porexemplo,todososcarrospossuemcor,velocidademáximaevelocidade
atual.Contudo,emumdadomomento,cadacarropossui valoresdiferentes
paraestascaracterísticas. Ocarrodojogadorévermelho,estáa150km/he
podealcan çaraté200km/h.Seurivaléazul,estáa170km/hepodealcan çar
até220km/h.Ascaracterísticasquedefinemumcarronojogosãoasmesmas,
mascadaumaestápreenchidacomvaloresdiferentesparacadacarro.
Esseconjuntodecaracterísticascomunsatodocarroéoquechamamos
de classe. Quandofalamos carro,referindo-nosa carros em geral,estamos
falandodeumaclasse.Aclasseéomoldeparaacriaç ãodeobjetos.
Cadacarroéuma instânciadaclasse. Ainstânciaéoobjetoemsi,um
objetoquepertenceaumaclasse.Quandofalodo meu carro,estoufalandode
umainstânciaespecíficadaclasse carro.O carro do vizinhoéoutrainstância.
Cor,velocidadeatualevelocidademáximasãoos atributosdaclasse,ou
seja,todasasinstânciasostêm,mascadaumapossuivaloresprópriospara
essesatributos.
Cadacarroexecutaastarefasdeacelerar,frearevirar.Estastarefassãoos
métodos.Emprogramasorientadosaobjeto,énosmétodosqueescrevemos
oscódigosquerealizamastarefasfundamentaisdoprograma.Elestrabalham
comosdadosnosatributosepodemalteraroestadodoobjeto.
Resumo de conceitos básicos de O.O.
•Classe: umtipodeobjetosdeterminado,compostoporatributos
emétodosdefinidos;
•Instância: cadaobjetopertencenteaumadeterminadaclasse;
•Atributo: cadapropriedadedosobjetoslistadaemumaclasse;
•Método:cadatarefaqueumobjetodeumaclassepodeexecutar.
27

## Página 35

1.4. OrientaçãoaobjetoscomJavaScript CasadoCódigo
Funções construtoras
EmlinguagensO.O.,comoJavaeC#,definimosclassesexplicitamente
(usandoapalavra-chave class). EmJavaScriptnãoháclasses,maspode-
mosusar funções construtorasparacriarosobjetosseguindoasclassesque
projetamos.
Umafun çãoconstrutoraéumafun çãonormaldoJavaScript,porémus-
adacomopropósitodecriarobjetos.Noexemploaseguir,apalavra-chave
thisrecebeosatributosdeumcarro.Apalavra cor,sozinha,serefereao
parâmetrorecebidopelafun ção,masaconstruç ão this.corcriaumatrib-
uto cornoobjeto:
<!-- arquivo: orientacao-objetos.html -->
<body>
<script>
function Carro(cor, velocMaxima) {
this.cor = cor;
this.velocMaxima = velocMaxima;
this.velocAtual = 0;
}
// continua...
</script>
</body>
Nósnãopodemoscriarumcarrosimplesmentechamando:
// Exemplo teórico
// Não faça isto:
Carro('verde', 300);
Quandochamamosumafun çãosemqualificarumobjeto,oJavaScript
entendequeestamosusandooobjeto window. Assim,apalavra thisno
corpodafun çãocriaráoumodificaráosatributosnesteobjeto.
Paracriarnovosobjetostemosdeusarapalavra-chave new. Apósa
funçãoconstrutora,crieasvariáveis meuCarroe oponenteparareferen-
ciarosnovosobjetos:
28

## Página 36

CasadoCódigo Capítulo1. Fundamentos
// Instanciando objetos da classe Carro
var meuCarro = new Carro( 'vermelho', 250);
var oponente = new Carro( 'azul', 300);
Aexpressão new Carro('vermelho', 250)criaumnovoobjetoe
executaneleafun çãoconstrutora. Agoraapalavra thissereferiráaesse
objeto!
Já os métodos, em JavaScript, são apenas atributos que referenciam
funções.Podemos,porexemplo,criarummétodo acelerarqueaumenta
em10unidadesavelocidadedocarro:
function Carro(cor, velocMaxima) {
// Criando os atributos
this.cor = cor;
this.velocMaxima = velocMaxima;
this.velocAtual = 0;
// Criando um método
this.acelerar = function() {
this.velocAtual += 10;
}
}
// ...
Chamandoométodo aceleraratravésdavariávelmeuCarrocriada
anteriormente,essemétodovaialteraroatributo velocAtualdessainstân-
cia,enãodainstância oponente:
// Chamando um método somente em um objeto
meuCarro.acelerar();
Por último, mande exibir as velocidades dos dois carros criados. O
primeiroacelerou,eooutronão!
// Verificando as velocidades
document.write(meuCarro.cor + ': ' + meuCarro.velocAtual);
document.write( '<br>');
document.write(oponente.cor + ': ' + oponente.velocAtual);
29

## Página 37

1.4. OrientaçãoaobjetoscomJavaScript CasadoCódigo
Asaídadessecódigoé:
vermelho: 10
azul: 0
Sintaxe de ponto e de colchetes
ParareferenciarmosatributosdeumobjetoemJavaScript,omais
usualéusarmosa sintaxe de ponto,ouseja,usarumpontoentreonome
doobjetoedoatributo:
meuObjeto.atributo
Tambémépossívelusara sintaxe de colchetes,naqualpodemosusar
stringspararepresentarosatributos.Oobjetotorna-seumaespéciede
arrayassociativo,sendoquecadaelemento(atributo)éassociadoauma
stringespecífica,enãoaumíndicedeposiç ão:
meuObjeto[ 'atributo']
Objetos sem função construtora
OJavaScriptofereceasintaxedechaves( {e })paracriarobjetos:
var meuObjeto = {
atributo1: valor,
atributo2: valor,
metodo1: function() {
},
metodo2: function() {
}
}
Porexemplo,poderíamoscriarumcarrodaseguinteforma:
30

## Página 38

CasadoCódigo Capítulo1. Fundamentos
var meuCarro = {
cor: 'azul',
velocidade : 0 ,
acelerar: function() {
this.velocidade += 10;
}
}
Nósusaremosessaformaalgumasvezesnodesenvolvimentodojogo.
Como,porém,seuprojetoéorientadoaobjetos,pensandoem classes,com
atributosemétodosdefinidos,daremosmaiorpreferênciaàsfun çõescon-
strutoras.
O prototype (protótipo)
Declararmétodoscomofun çõesanônimasdentrodasconstrutorastem
umpre ço:maiorconsumodememória.Cadavezqueexecutamosoconstru-
tor,umacópiadafun çãoanônimaécriadanamemóriaecadainstânciaterá
suacópianãosomentedoatributo,mastambémdafun ção:
function Carro(cor, velocMaxima) {
// ...
// Criando método com função anônima
this.acelerar = function() {
this.velocAtual += 10;
}
}
Pensandonisso,oJavaScripttrazorecursodo prototype(protótipo),queé
umobjetoassociadoaumafun çãoconstrutora.Colocandoosmétodosneste
objeto,todasasinstânciasusarãoasmesmascópiasdecadamétodo.
Vamos nos habituar a colocar a função construtora e oprototypede
umaclasseemumarquivoseparado,comextensão .js. Apalavra-chave
prototypefuncionacomosefosseumatributodafun çãoconstrutora:
// arquivo: carro.js
31

## Página 39

1.4. OrientaçãoaobjetoscomJavaScript CasadoCódigo
// Função construtora
function Carro(cor, velocMaxima) {
this.cor = cor;
this.velocMaxima = velocMaxima;
this.velocAtual = 0;
}
// Prototype com os métodos
Carro.prototype = {
acelerar: function() {
this.velocAtual += 10;
}
}
Escrevemosumpoucomaisdecódigo,porématéganhamosumpouco
maisdelegibilidadeeorganizaç ão:conseguimos“enxugar”afunçãoconstru-
tora,epodemosterofuncionamentocompletodeumcarroemseuarquivo
específico—para istoservemasclasses! Parautilizaressaclasseemuma
páginaHTML,bastausaratag <script>comoatributo src,referen-
ciandooarquivo carro.js:
<!-- arquivo prototype.html -->
<!DOCTYPE html>
<html>
<head>
<title>O prototype</title>
<script src="carro.js"></script>
</head>
<body>
<script>
var meuCarro = new Carro('vermelho', 250);
meuCarro.acelerar();
document.write(meuCarro.cor + ': ' + meuCarro.velocAtual);
</script>
</body>
</html>
32

## Página 40

CasadoCódigo Capítulo1. Fundamentos
Éisso!Comestesconceitosbásicosbemfixados,vamoscome çaraapren-
derconceitosespecíficosdejogos.Nopróximocapítulo,vamosaprenderuma
dasbasesdeumjogo,queconsistenoloopdeanimaç ãoenos sprites.
33

## Página 42

Capítulo2
Oloopdeanimaç ão
2.1 I ntrodução e sprites
Chegouahoradeavan çarmosumpassoalémdeapenasdesenharnoCanvas
emovimentaralgunsobjetos.Vamosdesenvolverpequenosaplicativosecriar
pequenaspe çasque,emalgummomento,irãosejuntaretomaraformade
umjogo!
Nossaabordagemseráaseguinte:
•Primeiro, sempre codificamos o “aplicativo principal”, que realiza um
teste nas classes a serem criadas.
Issoéimportanteparachegarmosacódigosclarosebemestruturados.
Aodesenvolver,sempreprocuramosfocaremumaspectopormomentoe
abstrair(“deixarparalá”)osoutros. Oaplicativodetestedeterminaoque
esperamosdenossasclasses.

## Página 43

2.1. Introduçãoesprites CasadoCódigo
•Em seguida, codificamos as classes e tentamos fazê-las responder como
queremos.
Nessaetapa,sempresurgirãomodificaçõesnaformacomoplanejamos
inicialmente,oquevemoscomoalgonatural. Refatorações(mudançasnaes-
truturadocódigosemalterarseucomportamento)serãorotinaparanós.
Maisdoqueensinarcomosefaz,pretendoapresentá-loaumaforma
detrabalharquedeixaráoresultadomuitomaisclaroeorganizadono
final.Vocêmeagradecerá,garanto-lhe.
Temosdecome çarporalgumlugar,entãoescolhioqueémaiscomuma
todojogo:oloopdeanimaç ão.Criaremosumaclasseresponsávelporcon-
trolaresseloop.
Antesdecome çar,vamosteremmentequeproblemaselaresolverá.“Mas
fazerumloopdeanimaç ãonãoésóchamarométodorepetidamente?”,você
dirá.Dependedoquevocêquerfazer.Emumjogo:
• aanimaçãotemqueserparadaereiniciadaemdiversosmomentos;
• váriosobjetosserãoanimadosemcadaciclo;
• objetospodemserincluídoseexcluídosdaanimação.
Conceito de sprites
Aosobjetostrabalhadosdentrodeumloopdeanimaç ão,damosonome
de sprites.Penseemumspritecomosendoumaimagemcomfundotrans-
parente,quepodeseranimada.Dessaforma,elespodemserinseridossobre
ofundoprincipaldocenário.
36

## Página 44

CasadoCódigo Capítulo2. Oloopdeanimação
Figura2.1:Sprites
Spritessãocriadosedestruídosatodomomento. Por“destruídos”,en-
tendanãoapenasmorto,aniquilado,atingido,masdestruídosna memória
do computador.Porexemplo,uminimigoouitemquesaiudatelapodeser
destruídoerecriadocasooheróiretorneàqueleponto. EmJavaScript,não
fazemosdestruiçãodeobjetos(emoutraslinguagensissoépossível),apenas
anulamosasvariáveisquesereferemaeleeodeixamoslivresparao garbage
collectorapagá-lodamemóriaautomaticamente.
Chegadeconceitos!Éhoradepôramãonamassa.
37

## Página 45

2.2. TesteparaaclasseAnimacao CasadoCódigo
2.2 T este para a classe Animacao
Figura2.2:AnimaçãocontroladaporclasseJavaScript
Comoprometemos,faremosumpequenoaplicativodetestenoqualdefin-
imoscomoqueremos“mandar”nasclassesquecriaremos. Comoestamos
desenvolvendoparaaweb,nossoaplicativoseráumapequenapáginaHTML
comalgunscódigosJavaScript.
ApáginareferenciadoisarquivosJavaScript: animacao.js,queconterá
aclassequecontrolaráoloopdeanimaç ão,e bola.js,ondedefiniremosum
sprite(umabolaquequicanatela).
<!-- arquivo: animacao-teste.html -->
<!DOCTYPE html>
<html>
<head>
<title>Primeiro Teste: Loop de Animação com Sprites</title>
<script src="animacao.js"></script>
<script src="bola.js"></script>
38

## Página 46

CasadoCódigo Capítulo2. Oloopdeanimação
</head>
<body>
<canvas id="canvas_animacao" width="500" height="500">
</canvas>
<script>
// Aqui vai a inicialização do aplicativo
</script>
</body>
</html>
ApósoCanvas,apáginaexecutaráumscriptdeinicializaç ão,cujocódigo
vemaseguir. Comoaprendemosnocapítuloanterior,tópico 1.1,primeiro
temosderecuperaroCanvaseseucontexto 2d.Depois,criamososprimeiros
sprites b1e b2paraasbolas,indicandosuascoordenadasnatela,eoutras
característicascomovelocidade,coreraio.
// Referências para o Canvas
var canvas = document .getElementById('canvas_animacao');
var context = canvas.getContext('2d');
// Criando alguns sprites
var b1 = new Bola(context);
b1.x = 100;
b1.y = 200;
b1.velocidadeX = 20;
b1.velocidadeY = -10;
b1.cor = 'red';
b1.raio = 20;
var b2 = new Bola(context);
b2.x = 200;
b2.y = 100;
b2.velocidadeX = -10;
b2.velocidadeY = 20;
b2.cor = 'blue';
b2.raio = 30;
39

## Página 47

2.2. TesteparaaclasseAnimacao CasadoCódigo
Emseguida, vamoscriaranossaanimaç ãohipotética, incluirnelaos
spriteseligá-la,fazendocomqueseinicieimediatamente:
// Criando o loop de animação
var animacao = new Animacao();
animacao.novoSprite(b1);
animacao.novoSprite(b2);
// "Ligar" a animação
animacao.ligar();
Claroque,aotentarabrirestapáginanonavegador,elaainda não fun-
ciona. TecleCtrl+Shift+JnoGoogleChrome,ou Ctrl+Shift+Kno
Firefox,edelicie-secomestasmensagens:
Figura2.3:ErrosnoConsoledoGoogleChromenafasedeescritadoteste
Arazãoéquenãotemosaindaosarquivos animacao.jse bola.js.
Nósapenasdefinimoscomoqueremosinteragircomasclassesqueaindanão
saíramdoovo.
Ecomoqueremosmandarnessasclasses?Quantoà Bola,queropoder
criarquantasdesejar,configurarposiç ão,velocidadeshorizontalevertical,
raioecor.Quantoà Animacao,nocódigoestoudizendoquequeropoder
incluirspritesàvontadeemandariniciá-lanomomentoqueeuacharopor-
tuno.
40

## Página 48

CasadoCódigo Capítulo2. Oloopdeanimação
2.3 D esenvolv a a classeAnimacao
O“grosso”dotrabalhocomeçaaqui.Játemosbemdefinido o quequeremos
daclassenesteponto,masagorafaltaexplicitar como. Pormaisdesafiador
quepare ça,vamosporetapasbempequenas("baby steps” ),elogoteremos
umresultadoconcreto.
Primeiro,faremosoesqueletodaclasse,comsuafun çãoconstrutoraeos
métodosqueimaginamosnoteste:
// Arquivo: animacao.js
function Animacao() {
}
Animacao.prototype = {
novoSprite : function(sprite) {
},
ligar: function() {
}
}
Paraincluirumspritenaanimaç ão,podemosiniciarumarrayvaziono
construtoreincluirneleossprites:
function Animacao() {
this.sprites = [];
}
Animacao.prototype = {
novoSprite : function(sprite) {
this.sprites.push(sprite);
},
ligar: function() {
}
}
Agoravamoscriaroatributo ligado,quedefiniráseaanimaç ãopode
ou não correr. Aproveitando o ensejo, já criaremos também o método
desligar:
41

## Página 49

2.3. DesenvolvaaclasseAnimacao CasadoCódigo
function Animacao() {
this.sprites = [];
this.ligado = false;
}
Animacao.prototype = {
novoSprite : function(sprite) {
this.sprites.push(sprite);
},
ligar: function() {
this.ligado = true;
this.proximoFrame();
},
// Não esquecer desta vírgula sempre que
// for criar um novo método!
desligar: function() {
this.ligado = false;
}
}
Em ligar, chamo um novo método,proximoFrame, que será o
coraçãodaclasse Animacao. Estemétodoverificasepodecontinuare,se
puder,realizaumciclodaanimaç ãoechamaasimesmonovamente(usando
o requestAnimationFramedoHTML5).
proximoFrame: function() {
// Posso continuar?
if ( ! this.ligado ) return;
// A cada ciclo, limpamos a tela ou desenhamos um fundo
this.limparTela();
// Atualizamos o estado dos sprites
for (var i in this.sprites)
this.sprites[i].atualizar();
// Desenhamos os sprites
42

## Página 50

CasadoCódigo Capítulo2. Oloopdeanimação
for (var i in this.sprites)
this.sprites[i].desenhar();
// Chamamos o próximo ciclo
var animacao = this;
requestAnimationFrame(function() {
animacao.proximoFrame();
});
}
Aquitemosmuitascoisasacontecendo.Acadaciclodeanimaç ão,deve-
mos:
•limpar a tela:senãofizermosisso,aboladeixaráumrastro(figura 2.4).
Éprecisoapagarosdesenhosdocicloanteriorparadesenharabolaem
seunovoestado,nanovaposiç ãoquevaiatualizaredesenharlogoem
seguida.Ométodo limparTelaseráimplementadoembreve;
•atualizar o estado dos sprites: cadaspriteseráresponsávelporseposi-
cionarerealizarseuspróprioscomportamentos.Deixamosacargoda
Bolaafun çãodecalcularsuatrajetória;
•desenhar os sprites: somentedepoisquetodosestiverematualizados;
•chamar o próximo ciclodaanimação.
43

## Página 51

2.3. DesenvolvaaclasseAnimacao CasadoCódigo
Figura2.4:Rastrodeixadopelabolasenãolimparmosatelaacadacicloda
animação
Temosumaimplicaç ãoimportante: todoobjetoquequiserpartici-
pardoloopdeanimaç ão(ouseja,quequiser ser um sprite),teráque
implementarosmétodos atualizare desenhar. Esteéoconceito
de interfacedaOrientaçãoaobjetos:umconjuntodemétodosqueuma
classedeveimplementarparapoderinteragircomoutra.
Parachamaropróximociclo,nãopodemossimplesmentefazer:
requestAnimationFrame(this.proximoFrame);
Afun çãodeanimaç ãoéchamadapeloJavaScriptcomoumafun çãoco-
mum,nãocomoummétododeobjeto—nãopodemosusaro thisden-
trodela,efizemosissováriasvezes! Juro,quandofuifazeristo,quebreia
cabeçaparadescobrirporquenãofuncionava.Asoluç ãoéreferenciaroob-
jetoemumavariávelechamarumafun çãoanônima,queporsuavezchama
proximoFramecomoumverdadeiro métododoobjeto:
44

## Página 52

CasadoCódigo Capítulo2. Oloopdeanimação
var animacao = this;
requestAnimationFrame(function() {
animacao.proximoFrame();
});
Temosagoraqueimplementarométodo limparTela:
limparTela: function() {
var ctx = this.context; // Só para facilitar a escrita ;)
ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}
Estemétodorequerumobjeto contextdoHTML5Canvas,portanto
vamosrecebê-lonoconstrutor:
function Animacao(context) {
this.context = context;
this.sprites = [];
this.ligado = false;
}
Temosentãoquepassá-lonocódigodoaplicativo:
// Criando o loop de animação
var animacao = new Animacao(context);
Procurefazercomqueumaclasserecebadeforaeguardeematribu-
tostudoqueelaprecisaparaexecutarseutrabalho,deformaqueelafique
completamentedesacopladadomeioexterno.Dependerdiretamenteda
variávelcontextdoaplicativoémaunegócio!Esteprincípiochama-se
injeção de dependências.
2.4 I mplemente a classe Bola
Estaclasseimplementaráainterfacedesprites,portantodeveráterosméto-
dos atualizare desenhar:
45

## Página 53

2.4. ImplementeaclasseBola CasadoCódigo
// Arquivo: bola.js
function Bola(context) {
this.context = context;
this.x = 0;
this.y = 0;
this.velocidadeX = 0;
this.velocidadeY = 0;
// Atributos de desenho padrão
this.cor = 'black';
this.raio = 10;
}
Bola.prototype = {
atualizar: function() {
},
desenhar: function() {
}
}
Em atualizar,colocamosoalgoritmoquequicaabolanasbordasdo
Canvas.Reparequesempretemosquedescontaroraiodabola,poisasco-
ordenadas xe ysereferirãoaoseucentro(figura 2.5).Seocentroestiverfora
dolimiteestabelecido,invertemososinaldavelocidade(multiplicamospor
-1)paraqueabolapasseairemsentidocontrário,tantonaverticalquanto
nahorizontal:
atualizar: function() {
var ctx = this.context;
if (this.x < this.raio || this.x >
ctx.canvas.width - this.raio)
this.velocidadeX *= -1;
if (this.y < this.raio || this.y >
ctx.canvas.height - this.raio)
this.velocidadeY *= -1;
46

## Página 54

CasadoCódigo Capítulo2. Oloopdeanimação
this.x += this.velocidadeX;
this.y += this.velocidadeY;
},
Figura2.5:Aposiç ãodabolaécalculadapeloseucentro,portantooslimites
paraquicá-latêmquedescontaroraio.
Em desenhar,usamosométodo arcdo context.Tambémusamos
osmétodos savee restoreparapoderconfigurá-locomacordabola
edepoisretorná-loaoestadooriginal. Casonãoselembredestesmétodos,
revejaase ção1.2.
desenhar: function() {
var ctx = this.context;
// Guardar configurações atuais do contexto
ctx.save();
// Configurar o contexto de acordo com a bola
ctx.fillStyle = this.cor;
// Desenhar
ctx.beginPath();
ctx.arc(this.x, this.y, this.raio, 0, 2 * Math.PI, false);
ctx.fill();
// Voltar às configurações anteriores
ctx.restore();
}
47

## Página 55

2.4. ImplementeaclasseBola CasadoCódigo
Oaplicativoestápronto! Abra-ononavegador. Seestiverusandoo
Chrome,pressione Ctrl+Shift+JedigitenoConsole(parafazerissono
Firefox,vocêdeveinstalarumplugincomooFirebug):
animacao.desligar();
Aanimaçãopara!Agorafaç a:
animacao.ligar();
Nãoéfantástico?Comoexercício,criemaisobjetos Bolacomtamanhos,
coresevelocidadesdiferentes,eacrescente-osàanimaç ão. Vocêpodefazer
issonoarquivoHTMLoudiretamentenoConsole!
Aquinóscriamosumaprimeirabaseparanossojogo,queéoloopde
animação.Nopróximocapítulo,vamosaprendercomoépossívelcriarain-
teraçãodousuáriocomojogo.
48

## Página 56

Capítulo3
Ainteraçãocomojogador—
leituraapuradadoteclado
Nestetópico,vamostratardainteraç ãodousuáriocomojogo.Tratareventos
detecladoemJavaScriptnãoéumatarefadifícil,noentanto,háaspectosque
precisamserconsiderados,emsetratandodejogos.
Faremosumarevisãosobreoseventosdetecladoe,emseguida,tratare-
mosdoistiposespeciaisdeinterações:
•o jogador mantém uma tecla pressionada:muitocomumcomassetas
demovimentação,masnãoselimitaaestas.Ojogodeveresponderde
determinadamaneira(porexemplo,movimentandooherói)enquanto
ateclaestápressionadaepararquandoojogadorsoltaatecla;
•o jogador pressiona e solta rapidamente a tecla:sãoas teclas de disparo,

## Página 57

3.1. EventListenerseoseventoskeydownekeyup CasadoCódigo
comasquaisaaç ãodeveocorrerumaúnicavez,nomomentoexatodo
pressionamento.Seateclacontinuarpressionada,ojogodeveignorar
seuestado.
Istotudoparecemuitoóbviomas,comoveremos,omodelodeeventos
dotecladoemJavaScriptévoltadoparaa digitação de caracteres(lembre-se,a
linguagemfoicriadaparapáginasdaweb)enãonospermitetratarinterações
comunsemjogoscomapenasumcomando.Porém,acoisatambémnãoétão
complicada,requerendoapenasalgumacodificaç ãomanual.
3.1 E ventL isteners e os eventos keydown e
keyup
Qualquerelementoemumapáginadawebpodeter“ouvintes”(listeners)de
eventos.Nocasodoseventosdoteclado,oelementodevetero foco:
Figura3.1:Cursordotecladopiscandonocampodebusca.Ofocodoteclado
pertenceaelenestemomento.
50

## Página 58

CasadoCódigo Capítulo3. Ainteraçãocomojogador—leituraapuradadoteclado
Figura3.2:ApósalgunstoquesnateclaTab,ofocovaiparaobotão Pesquisa
Googleeesteficadestacado. ObrowseraguardaousuárioteclarEnterou
espaçoparaacionarobotão.
Um listeneréumafunçãoJavaScriptqueexecutaumaaç ãoemrespostaa
umevento.Essafun çãopodereceberumparâmetroqueépreenchidoauto-
maticamentecomdadossobreoeventoocorrido.
Paraassociarumlisteneraumelementodapágina,usamosométodo
addEventListener:
// Exemplo teórico
var campo = document.getElementById('campo');
campo.addEventListener('nomedoevento ',
function(parametroEvento) {
// Ações de resposta ao evento vão aqui
});
EmJavaScript,sãotrêsoseventosassociadosaoteclado:
•keydown: ocorrequandoumateclaépressionada(abaixada). Seo
usuárioamantiversegurando,oeventoédisparadorepetidamente.
•keypress:ocorrelogoapós keydown,nocasodeateclaserdecarac-
tere. Seateclacontinuarpressionada,obrowserdisparaoseventos
alternadamente:keydown-keypress-keydown-keypress-etc.
•keyup:ocorreumaúnicavez,quandoumateclaésolta.
51

## Página 59

3.1. EventListenerseoseventoskeydownekeyup CasadoCódigo
Figura3.3:Teclamantidapressionada.Ocomputadorproduzumcaractere,
fazumapausa,edisparaoutrosemsequência.
Para o desenvolvimento de jogos, somente os eventoskeydowne
keyupserãonecessários. Tudooquenósprecisaremossaberserãoos
momentosquandoumateclaépressionadaequandoésolta,parapoder
dispararaçõesaopressionaroudetectarseumateclaestáounãopres-
sionada. Oevento keypresséespecíficoparatratardigitaç ãodecarac-
teres.
Seriatudomuitomaravilhososepudéssemoscodificarnossasaçõesdire-
tamentenoevento keydown!Noentanto,oresultadoficariahorrível.Omod-
elodeeventosparaadigitaç ãodecaracteres(figura 3.3)nãoserveparamovi-
mentarpersonagens. Jávialgunsjoguinhosdetutoriaisnainternetserem
feitosdessamaneira.Faç aumtesteecomproveporsimesmo:
<!-- arquivo teclado-teste-1.html -->
<!DOCTYPE html>
<html>
<head>
<title>Movimentando personagem com keydown</title>
</head>
<body>
<canvas id="canvas_teclado_1" width="500" height="500">
</canvas>
<script>
// Interação com o teclado vai aqui
</script>
</body>
52

## Página 60

CasadoCódigo Capítulo3. Ainteraçãocomojogador—leituraapuradadoteclado
</html>
Agorairemoscriarum listenerparaoevento keydown,quedeslocaum
“personagem”paraadireitaouparaaesquerda.Asteclasdesetasãorecon-
hecidasatravésdapropriedade keyCodedoobjeto evento,recebidocomo
parâmetro.
Natag <script>,quevemlogoapósoCanvas,digite:
// Referências do Canvas
var canvas = document .getElementById('canvas_teclado_1');
var context = canvas.getContext('2d');
// Posição inicial do personagem
var posicao = 0;
desenharPersonagem();
document.addEventListener('keydown', function(evento) {
if (evento.keyCode == 37) { // Seta para esquerda
posicao -= 10;
desenharPersonagem();
}
else if (evento.keyCode == 39) { // Seta para direita
posicao += 10;
desenharPersonagem();
}
});
// Um personagem não muito simpático, mas...
function desenharPersonagem() {
context.clearRect(0, 0, canvas.width, canvas.height);
context.fillRect(posicao, 100, 20, 50);
}
Abraapáginanobrowseremovaoretângulocomassetasdireitaees-
querda. Percebaque,aoiniciaromovimentoparaalgumlado,ocorreuma
pausaapósoprimeirodeslocamento,paradepoiseleocorrernormalmente.
53

## Página 61

3.1. EventListenerseoseventoskeydownekeyup CasadoCódigo
Figura3.4:Nossoheróiparecequeestámanco...
Nãoficoubom,nãoéverdade? Maspodemosaprendermuitascoisas
debruçando-sesobreestetrecho:
document.addEventListener('keydown', function(evento) {
if (evento.keyCode == 37) { // Seta para esquerda
posicao -= 10;
desenharPersonagem();
}
else if (evento.keyCode == 39) { // Seta para direita
posicao += 10;
desenharPersonagem();
}
});
• Primeiro,queroouvireventosdotecladoocorridosemtodoodocu-
mento.Portanto,adicionoolisteneraoelemento document.
• Afunctionrecebeuumparâmetrodenome evento(possodar
qualquernomeparaele).EsseparâmetrorecebeudoJavaScriptauto-
maticamenteumobjetocompropriedadesrelacionadasaoevento.
• ApropriedadekeyCodedesseobjetocontémumvalorúnicopara
cadatecla. Nãoédifícildescobriroscódigosfazendoumarápida
pesquisanainternet,oucriandoumpequenoprogramaparaessefim.
54

## Página 62

CasadoCódigo Capítulo3. Ainteraçãocomojogador—leituraapuradadoteclado
3.2 D etectando se uma tecla está ou não pres-
sionada
Comoaprendemos(ecomprovamos,casovocêtenhadigitadoocódigoan-
terior),omodelodeeventosdetecladodoJavaScriptéeficazparatratardig-
itação,mascompletamentebizarroparajogos. Comonãohánenhumco-
mandoparaeuperguntar:“atecla talestápressionada?”,tenhoquemanter
umregistrodeteclaspressionadasmanualmente.Parafacilitar,seguiremoso
modelodecriarumaclasseparatratardesteproblema.
T este da classe Teclado
Criemosumapáginasemelhanteàanterior, masondenossocorajoso
heróiserácontroladodemaneiramaiseficiente.Imaginepodermosfazer:
// Exemplo teórico
var teclado = new Teclado(document);
if (teclado.pressionada(SETA_DIREITA))
posicao += 10;
Bem,então...faç amos!Reparenasimplicidadecomquequeremoscon-
trolaroteclado.Delegamosàclasse Tecladoaresponsabilidadedesaberse
determinadateclaestáounãopressionada.
<!-- arquivo teste-teclado-2.html -->
<!DOCTYPE html>
<html>
<head>
<title>Movimentando personagem com classe JavaScript</title>
<script src="teclado.js"></script>
</head>
<body>
<canvas id="canvas_teclado_2" width="500" height="500">
</canvas>
<script>
55

## Página 63

3.2. Detectandoseumateclaestáounãopressionada CasadoCódigo
// Aqui virá um controle de teclado mais apurado
</script>
</body>
</html>
OJavaScriptconterápartesbemparecidascomodoexemploanterior,
masintroduzimosaquiumloopdeanimaç ão.Éelequevaiavaliarconstan-
tementeoestadodedeterminadasteclas.
PrimeiroreferenciamosoCanvasnormalmente:
var canvas = document.getElementById('canvas_teclado_2');
var context = canvas.getContext('2d');
Emseguida,definimosaposiç ãoinicialdopersonagememandamosde-
senhar:
var posicao = 0;
desenharPersonagem();
Agoravamoscriarocontroladordoteclado.Queropassarparaeleoele-
mentodapáginaondeoseventosserãoouvidos(nocaso, document):
var teclado = new Teclado(document);
Oloopdeanimaç ãoserábembásico,porenquantoatravésdeumasim-
plesfun ção.Nestafun ção,primeirolemosoestadodasteclasquequeremos
emudamosaposiç ãodopersonagemdeacordo. Emseguida,nósodesen-
hamosechamamosopróximociclo:
requestAnimationFrame(animar);
function animar() {
if (teclado.pressionada(SETA_ESQUERDA))
posicao -= 10;
else if (teclado.pressionada(SETA_DIREITA))
posicao += 10;
desenharPersonagem();
requestAnimationFrame(animar);
}
56

## Página 64

CasadoCódigo Capítulo3. Ainteraçãocomojogador—leituraapuradadoteclado
Afun ção desenharPersonageméamesmacriadaanteriormente:
// Nosso herói continua esbanjando charme! :D
function desenharPersonagem() {
context.clearRect(0, 0, canvas.width, canvas.height);
context.fillRect(posicao, 100, 20, 50);
}
A classe Teclado
Estaclasserecebeumelementoqualquerdapáginanoconstrutoreatribui
aeleoseventosquevãoregistraroestadodasteclasemumarray.Ométodo
pressionadadevolveovalor truecasoateclaconstecomopressionada
nomomento:
// arquivo: teclado.js
// Códigos de teclas - aqui vão todos os que forem necessários
var SETA_ESQUERDA = 37;
var SETA_DIREITA = 39 ;
function Teclado(elemento) {
this.elemento = elemento;
// Array de teclas pressionadas
this.pressionadas = [];
// Registrando o estado das teclas no array
var teclado = this;
elemento.addEventListener('keydown', function(evento) {
teclado.pressionadas[evento.keyCode] = true;
});
elemento.addEventListener('keyup', function(evento) {
teclado.pressionadas[evento.keyCode] = false;
});
}
Teclado.prototype = {
pressionada: function(tecla) {
return this.pressionadas[tecla];
}
}
57

## Página 65

3.3. Efetuandodisparos—detectandosomenteoprimeirokeydown CasadoCódigo
Abraapáginaevejaqueo“personagem”move-secommuitomaissuavi-
dadeefluência!
3.3 E fetuando disparos — detectando somente
o primeiro keydown
Vamosdarumsuperpoderaoherói:atirar.Nesteponto,parafacilitaranossa
vida,vamosusaraclasse Animacaoeoconceitodespritesaprendidosante-
riormente.
Quetalpodermandaroheróiatirardaformamostradaaseguir? Sea
classe Tecladosabeseumateclaestápressionada,elatambémpodesaber
dispararumaaç ãoúnicanomomentodopressionamento!
// Exemplo teórico
teclado.disparou(ESPACO, function() {
heroi.atirar();
});
Figura3.5:Heróiatirando
Vamoscriarumanovapágina. Osscripts bola.jse animacao.js
sãoosmesmosjácriados.Certifique-sedeterumacópiadelesnapastadeste
teste(oulinká-loscorretamenteemseucomputador).
58

## Página 66

CasadoCódigo Capítulo3. Ainteraçãocomojogador—leituraapuradadoteclado
<!-- arquivo: teste-teclado-3.html -->
<!DOCTYPE html>
<html>
<head>
<title>Um herói que atira</title>
<script src="teclado.js"></script>
<script src="heroi.js"></script>
<script src="bola.js"></script>
<script src="animacao.js"></script>
</head>
<body>
<canvas id="canvas_teclado_3" width="500" height="500">
</canvas>
<script>
// Isto vai começar a parecer um jogo!
</script>
</body>
</html>
Vejacomooscriptdotesteésimpleseconciso. Nestaaltura,euespero
sinceramentequevocêestejaentendendooporquêdeestarmosfazendodessa
forma.Criarumanovaaç ão,umnovopersonagem,umnovoinimigodeverá
sercadavezmaissimplesapartirdeagora:
var canvas = document .getElementById('canvas_teclado_3');
var context = canvas.getContext('2d');
var teclado = new Teclado(document);
var animacao = new Animacao(context);
// Um sprite pode ler o teclado para saber
// como se comportar
var heroi = new Heroi(context, teclado);
heroi.x = 0;
heroi.y = 100;
animacao.novoSprite(heroi);
59

## Página 67

3.3. Efetuandodisparos—detectandosomenteoprimeirokeydown CasadoCódigo
teclado.disparou(ESPACO, function() {
heroi.atirar();
});
animacao.ligar();
Precisamoscriarométodo disparounaclasse Teclado. Paraque
elefuncionecorretamente,éprecisoregistrarquedeterminadateclafoidis-
parada(paraqueoseventos keydownsubsequentesnãoprovoquemodisparo
novamente).Criamosmaisdoisarrays,umpararegistrarosdisparoseoutro
paraguardarasfun çõesaseremexecutadas:
// Códigos de teclas - aqui vão todos os que forem necessários
var SETA_ESQUERDA = 37 ;
var SETA_DIREITA = 39;
var ESPACO = 32;
function Teclado(elemento) {
this.elemento = elemento;
// Array de teclas pressionadas
this.pressionadas = [];
// Array de teclas disparadas
this.disparadas = [];
// Funções de disparo
this.funcoesDisparo = [];
// continua...
}
No eventokeydown, verificamos se a tecla pressionada possui uma
funçãodedisparoassociadaeseseudisparojáfoiprocessado. Ainstruç ão
this.funcoesDisparo[tecla] () ;executaafun çãoguardadanoar-
raydevidoaosparêntesesnofinal:
var teclado = this;
60

## Página 68

CasadoCódigo Capítulo3. Ainteraçãocomojogador—leituraapuradadoteclado
elemento.addEventListener('keydown', function(evento) {
var tecla = evento.keyCode; // Tornando mais legível ;)
teclado.pressionadas[tecla] = true;
// Disparar somente se for o primeiro keydown da tecla
if (teclado.funcoesDisparo[tecla] &&
! teclado.disparadas[tecla]) {
teclado.disparadas[tecla] = true;
teclado.funcoesDisparo[tecla] () ;
}
});
Noevento keyupsetamosoestado“disparada”parafalse,demodoa
tornarpossíveisnovosdisparos:
elemento.addEventListener('keyup', function(evento) {
teclado.pressionadas[evento.keyCode] = false;
teclado.disparadas[evento.keyCode] = false;
});
Enfim,ométodo disparounecessitaapenasguardarumafun çãode
disparoparaumatecla.Oevento keydownestácuidandodetudo!
disparou: function(tecla, callback) {
this.funcoesDisparo[tecla] = callback;
}
Emcasodedúvidas,vejaonovocódigocompletodaclasse Teclado:
// arquivo teclado.js - versão final
// Códigos de teclas - aqui vão todos os que forem necessários
var SETA_ESQUERDA = 37;
var SETA_DIREITA = 39 ;
var ESPACO = 32;
function Teclado(elemento) {
this.elemento = elemento;
// Array de teclas pressionadas
61

## Página 69

3.3. Efetuandodisparos—detectandosomenteoprimeirokeydown CasadoCódigo
this.pressionadas = [];
// Array de teclas disparadas
this.disparadas = [];
// Funções de disparo
this.funcoesDisparo = [];
var teclado = this;
elemento.addEventListener('keydown', function(evento) {
var tecla = evento.keyCode; // Tornando mais legível ;)
teclado.pressionadas[tecla] = true;
// Disparar somente se for o primeiro keydown da tecla
if (teclado.funcoesDisparo[tecla] &&
! teclado.disparadas[tecla]) {
teclado.disparadas[tecla] = true;
teclado.funcoesDisparo[tecla] () ;
}
});
elemento.addEventListener('keyup', function(evento) {
teclado.pressionadas[evento.keyCode] = false;
teclado.disparadas[evento.keyCode] = false;
});
}
Teclado.prototype = {
pressionada: function(tecla) {
return this.pressionadas[tecla];
},
disparou: function(tecla, callback) {
this.funcoesDisparo[tecla] = callback;
}
}
Ébastanteabstrato,masseconseguirmosprogramardemaneiramais
geralagora,teremosumgameenginebastanterobustoepráticoparacriar
62

## Página 70

CasadoCódigo Capítulo3. Ainteraçãocomojogador—leituraapuradadoteclado
novosjogosdemaneiraextremamenteveloz!
Crie a classe Heroi como um sprite
Paranossocódigofuncionar,temosquecriarospritedoherói. Como
ospriteéresponsávelpeloseuprópriocomportamento,eledeverecebero
objetoquecontrolaotecladoparapoderdecidiroquevaifazeremcadaciclo
daanimação.
Oheróitambémdeveterométodo atirar,chamadonoteste.
// arquivo: heroi.js
function Heroi(context, teclado) {
this.context = context;
this.teclado = teclado;
this.x = 0;
this.y = 0;
}
Heroi.prototype = {
atualizar: function() {
},
desenhar: function() {
},
atirar: function() {
}
}
Nométodoatualizar,lemosoestadodotecladoemovemosoperson-
agemdeacordo. Tambémnãocustanadaimpedirqueultrapasseasbordas
datela:
atualizar: function() {
if (this.teclado.pressionada(SETA_ESQUERDA) && this.x > 0)
this.x -= 10;
else if (this.teclado.pressionada(SETA_DIREITA) &&
this.x < this.context.canvas.width - 20)
this.x += 10;
},
63

## Página 71

3.3. Efetuandodisparos—detectandosomenteoprimeirokeydown CasadoCódigo
Nométododesenhar...bem,euvoucontinuarmantendoascoisassimples
efazerumsimplesretângulo.Nocapítulosobre spritesheets(4)acoisavai
ficarmaisinteressante,prometo!
desenhar: function() {
this.context.fillRect(this.x, this .y, 20, 50);
},
Agora,apartemaisinteressante:fazê-loatirar.Nesteponto,devemosler
novamenteoestadodotecladoparasaberparaqueladootirovai. Vamos
aproveitaraclasse Bolaquejátemos:
atirar: function() {
var tiro = new Bola(this.context);
tiro.x = this.x + 10;
tiro.y = this.y + 10;
tiro.raio = 2;
tiro.cor = 'red';
if (this.teclado.pressionada(SETA_ESQUERDA))
tiro.velocidadeX = -20;
else
tiro.velocidadeX = 20;
// Não tenho como incluir nada na animação!
this.animacao.novoSprite(tiro);
}
Comooheróivaiacrescentarumtiroàanimaç ãosemumareferênciaa
ela?Vamosrecebê-latambémnoconstrutor:
function Heroi(context, teclado, animacao) {
this.context = context;
this.teclado = teclado;
this.animacao = animacao;
this.x = 0;
this.y = 0;
}
Epassá-lanoaplicativodeteste:
64

## Página 72

CasadoCódigo Capítulo3. Ainteraçãocomojogador—leituraapuradadoteclado
var heroi = new Heroi(context, teclado, animacao);
Façaoteste. Sevocêfeztudocorreto,oheróideveatiraraoteclarmos
espaço.Masaindatemosdoispequenosproblemas:
1) aclasseBolaestáprogramadaparaquicar,portantonãovemosostiros
sumiremdatela(figura 3.6);
2) quandoparado,oheróiatirasempreparaadireita.
Figura3.6:Ostirosficamquicandonatela,aoinvésdesumirem
Pararesolveroprimeiroproblema,vamosmudaroalgoritmodométodo
atualizardaclasse Bola.Recomendoqueestetestereferenciesuaprópria
cópiadoarquivo bola.js,paranãoalterarocomportamentodostestes
anteriores.
atualizar: function() {
// Tiramos os testes que quicam a bola na borda do Canvas
this.x += this.velocidadeX;
this.y += this.velocidadeY;
},
65

## Página 73

3.3. Efetuandodisparos—detectandosomenteoprimeirokeydown CasadoCódigo
Quantoàdire çãodotiro,criamosno Heroiumatributoqueguardaa
suadire ção:
// Códigos únicos para as direções
var DIRECAO_ESQUERDA = 1;
var DIRECAO_DIREITA = 2;
function Heroi(context, teclado, animacao) {
this.context = context;
this.teclado = teclado;
this.animacao = animacao;
this.x = 0;
this.y = 0;
// Direção padrão
this.direcao = DIRECAO_DIREITA;
}
Destaforma,aomovimentaroherói,guardamosadire çãoemqueelese
encontranesseatributo:
atualizar: function() {
if (this.teclado.pressionada(SETA_ESQUERDA)
&& this.x > 0) {
this.direcao = DIRECAO_ESQUERDA;
this.x -= 10;
}
else if (this.teclado.pressionada(SETA_DIREITA) &&
this.x < this.context.canvas.width - 20) {
this.direcao = DIRECAO_DIREITA;
this.x += 10;
}
},
Porfim,bastaleressadire çãoaosoltarotiro,emvezdoestadodedeter-
minadatecla:
atirar: function() {
// ...
66

## Página 74

CasadoCódigo Capítulo3. Ainteraçãocomojogador—leituraapuradadoteclado
// Lendo a direção atual
if (this.direcao == DIRECAO_ESQUERDA)
tiro.velocidadeX = -20;
else
tiro.velocidadeX = 20;
// ...
}
Pronto! Temosumheróiquesemovimentaeatiradentrodeumloop
deanimação. Emboraaindaestejamuitobásico,éprecisoqueosconceitos
aprendidosfiquembemfixadosparaseguirmosparaaspróximasetapas.Pro-
curerelererefazeroscódigosdecadacapítulodiversasvezes. T ente tam-
bém fazer algumas coisas diferentes, como mover ou atirar na vertical!
Paraisso,oscódigosdeteclassão38(acima)e40(abaixo),easalterações
naposição ydosspritesserãoasmesmasjáfeitaspara x,somenteincremen-
tandoapartirda velocidadeY.Experimente!
Nopróximocapítulo,introduzireiasfolhasdesprites(spritesheets),que
nospermitirãoanimarnossoheróiapartirdeimagens.
67

## Página 76

Capítulo4
Folhasdesprites—spritesheets
4.1 C onceito e abordagem utilizada
Umpequeno game engineestácomeçandoatomarforma.Játemosummodo
robustodecontrolaroloopdeanimaç ãoecapturaraentradadousuáriono
tecladodeumamaneiraeficienteparajogos.
Nestecapítulo,avan çaremosumpoucoalémefaremosalgomuitointer-
essanteefundamental: as spritesheets(folhasdesprites). Umsprite,como
vocêaprendeunocapítulo2.1,écadaelementocontroladopeloloopdean-
imação(oherói,uminimigo,umblocoouplataformaetc.). Umafolhade
spriteséumaimagemcontendováriaspartesdeumaanimaç ão.Essaspartes
sãoalternadasconstantementeparaproduziromovimentodeumoumais
sprites.

## Página 77

4.1. Conceitoeabordagemutilizada CasadoCódigo
Figura4.1:Folhadesprites(spritesheet)
Éumaboapráticacarregarimagensmaiorescontendoumapor çãode
outrasmenores,emvezdetercadapequenaimagememseupróprioarquivo.
Lembre-sedeque,emambienteweb,cadaimagemrequernovaconexãodo
browsercomoservidor.
Programaranimaçõescomspritesheetspodesertãosimplesoutãotra-
balhosoquantovocêdesejarouprecisar, dependendodaabordagemuti-
lizada. NolivroCoreHTML5Canvas[1],deDavidGeary,asposiçõesde
cadafigurinha(x,y,larguraealtura)dentrodaspritesheetsãochumbadas
emgrandesarrays:
var sprite = [ [0, 71, 90, 80],
[40, 71, 80, 85], ... ]; // Continua...
Essaabordagemébastanteeconômicaemtermosdoespaçoocupado
pelas imagens, mas gera muito trabalho extra para coletar a posição de
cadaimageme,principalmente,paraenquadrá-lasadequadamente. Aqui,
adotaremosumaabordagembastantesistematizada:
• cadaspritesheetserádivididaemespaçosiguais,porissoasimagens
devemestarcorretamentedistribuídas;
• cadalinhadaspritesheetcorresponderáaum estadodosprite(ex.:
parado,correndoparaadireita,correndoparaaesquerda);
• aanimaçãodeumestadousarásomenteasfigurasnasualinhaprópria.
70

## Página 78

CasadoCódigo Capítulo4. Folhasdesprites—spritesheets
Issogeragrandequantidadedeespaçovazionaimagem,aumentandoo
tamanhodoarquivo,mascertamentefacilitarámuitoaprogramaç ão.Tenha
emmentequeestanãoéaúnicaabordagemválida,masparafinsdidáticos
éaqueiremosutilizarVconvenhamos,omodomaiseconômicodescritono
livroCoreHTML5Canvasétotalmenteimprodutivo,emespecialquandoo
focoéoaprendizadodastécnicasdeprogramaç ão,nãodeenquadramentode
imagens.
Figura4.2:Spritesheetdivididaempartesiguaiseorganizandoosestadospor
linhas
OCorelDrawpossuiaferramenta Papel Gráfico,quecriaumquadric-
uladodividindoumaáreaempartesiguais.Nesteprogramaetambém
noPhotoshop,Illustratoreemoutros,podemosusarasréguaselinhas-
guia.Sevocênãoconheceestesrecursos,sugiroquepesquisearespeito.
Sugestões:
http://coreldrawtips.com/site/using-the-graph-paper-tool-in-coreldraw
http://helpx.adobe.com/br/photoshop/using/grid-guides.html
71

## Página 79

4.2. Carregandoimagensefazendorecortes(clipping) CasadoCódigo
4.2 C arregando imagens e fazendo recortes
(clipping)
Carregar uma imagem do servidor pelo JavaScript é bastante simples.
Primeiroinstanciamosumobjeto Image,emseguida,setamosseuatributo
srcparaocaminhodaimagem:
var imgSonic = new Image();
imgSonic.src = 'spritesheet.png';
Aimagempossuioevento onload,queédisparadoquandoocarrega-
mentodaimagemestácompleto:
imgSonic.onload = function() { ... }
Quandotivermosmuitasimagens,oeventoonloaddecadaumapode
incrementarumaporcentagemoubarrinhade“carregando”.Issoficarápara
outrahora!
Vamosagorafazero clipping(enquadramento),queéorecortedaparte
exatadaspritesheetquequeremos. Porexemplo,suponhaquequeremosa
figurinhanalinha2,coluna7(contadosapartirdezero). Nahoradepro-
gramarasanimações,ficarámuitomaisfácilexpressardessamaneira. No
entanto,precisaremoscalcularaposiç ão(x,y)dorecortedaimagem.
<!-- arquivo: clipping.html -->
<!DOCTYPE html>
<html>
<head>
<title>
Spritesheet - recorte e enquadramento (clipping)
</title>
</head>
<body>
<canvas id="canvas_clipping" width="500" height="500">
</canvas>
<script>
72

## Página 80

CasadoCódigo Capítulo4. Folhasdesprites—spritesheets
var imgSonic = new Image();
imgSonic.src = 'spritesheet.png';
imgSonic.onload = function() {
// Aqui faremos o clipping!
}
</script>
</body>
</html>
Noevento onloaddaimagem,calcularemosasposições xe ydorecorte.
Comoestamosconsiderandoquadrosdetamanhosiguais, bastadividira
larguratotalpelonúmerodecolunasparaobteralarguradeumquadro.De-
poisbastamultiplicarestevalorpelacolunadesejada,etemosaposiç ãox
ondeorecorteseinicia. Paraaposiç ãoy,oprocessoéanálogoapartirda
alturatotalenúmerodelinhas:
imgSonic.onload = function() {
// Passo estes valores conforme a minha spritesheet
var linhas = 3;
var colunas = 8;
// Dimensão de cada quadro
var largura = imgSonic.width / colunas;
var altura = imgSonic.height / linhas;
// Quadro que eu quero (expresso em linha e coluna)
var queroLinha = 2;
var queroColuna = 7;
// Posição de recorte
var x = largura * queroColuna;
var y = altura * queroLinha;
// Continua...
}
Tendo calculado x, y, largura e altura, basta lembrarmos do método
drawImagedo context(vejaocapítulo 1.2).Estemétodopodeserchamado
73

## Página 81

4.2. Carregandoimagensefazendorecortes(clipping) CasadoCódigo
deduasmaneiras:
• Desenhandoumaimageminteira:
context.drawImage(imagem, x, y, largura, altura);
• Fazendoclipping:
context.drawImage(
imagem,
xOrigem,
yOrigem,
larguraOrigem,
alturaOrigem,
xDestino,
yDestino,
larguraDestino,
alturaDestino
);
Finalizemos,então,onossocódigo:
var context =
document.getElementById( 'canvas_clipping').getContext( '2d');
context.drawImage(
imgSonic,
x,
y,
largura,
altura,
100, // Posição no canvas onde quero desenhar
100,
largura,
altura
);
Vejaoresultadonobrowser:
74

## Página 82

CasadoCódigo Capítulo4. Folhasdesprites—spritesheets
Figura4.3:Fazendoclippingnaspritesheet(quadronalinha2,coluna7)
4.3 A nimações de sprite — a classe Spritesheet
Daremos prosseguimento à confecção do nosso game engine. A classe
Spritesheetseráresponsávelpor:
• Avançaraanimação,escolhendoqualoquadroaserdesenhadonomo-
mento;
• Calcularasposiçõesderecorteerealizaroclipping,dadososnúmeros
delinhasecolunas;
• Gerenciarotempoentreumquadroeoutro.
Comodecostume,escreveremosprimeiroumcódigodeteste,comoqual
tentamosmanterainterfacedaclasseomaisenxutapossível. Inicialmente,
faremosoSoniccorrerparaadireita.Cadaquadroteráaduraç ãode60milis-
segundos,podendoserajustadoposteriormente.
75

## Página 83

4.3. Animaçõesdesprite—aclasseSpritesheet CasadoCódigo
Figura4.4:Soniccorrendonatela
Dessaforma,aclasse Spritesheetdeveráalternarparanósosquadros
dasegundalinha(índice1,contadoapartirdezero—vejafigura 4.2).Ainda
nãousaremosaclasse Animacao,apenasumafun çãosimplesqueservirá
comogameloop.
<!-- arquivo: teste-spritesheet-1.html -->
<!DOCTYPE html>
<html>
<head>
<title>Testando a classe Spritesheet</title>
<script src="spritesheet.js"></script>
</head>
<body>
<canvas id="canvas_spritesheet_1" width="500" height="500">
</canvas>
<script>
// Vamos tentar mandar na Spritesheet
// da maneira mais simples!
76

## Página 84

CasadoCódigo Capítulo4. Folhasdesprites—spritesheets
</script>
</body>
</html>
NoJavaScript,queremosdizeràclasse Spritesheetosnúmerosdelin-
hasecolunas,eescolhemosquallinhaqueremosanimar.Ascolunasdeverão
seralternadasautomaticamente.
Tambémpassamosnoconstrutoro contextdoCanvaseaimagemaser
desenhada:
var context = document.getElementById('canvas_spritesheet_1')
.getContext('2d');
var imgSonic = new Image();
imgSonic.src = 'spritesheet.png';
// Quero passar: context, imagem, linhas, colunas
var sheet = new Spritesheet(context, imgSonic, 3, 8);
// Duração de cada quadro
sheet.intervalo = 60;
// "correndo para direita"
sheet.linha = 1;
// Animação
imgSonic.onload = gameLoop;
Nafun ção gameLoop,ordenoà Spritesheetqueavanceumquadro
equedesenheoquadroatualnaposiç ãoqueeumandar:
function gameLoop() {
context.clearRect(0, 0, context.canvas.width,
context.canvas.height);
// Avançar na animação
sheet.proximoQuadro();
77

## Página 85

4.3. Animaçõesdesprite—aclasseSpritesheet CasadoCódigo
// Onde desenhar o quadro atual
sheet.desenhar(100, 100);
requestAnimationFrame(gameLoop);
}
Testepronto,passemosaoesbo çodaclasse Spritesheet:
function Spritesheet(context, imagem, linhas, colunas) {
this.context = context;
this.imagem = imagem;
this.numLinhas = linhas;
this.numColunas = colunas;
this.intervalo = 0;
this.linha = 0;
this.coluna = 0;
}
Spritesheet.prototype = {
proximoQuadro: function() {
},
desenhar: function(x, y) {
}
}
Ocálculodoquadroatualébemsimples,bastandoincrementaracoluna
atualevoltarparazeroquandoexcederonúmerodecolunas:
proximoQuadro: function() {
if (this.coluna < this.numColunas - 1)
this.coluna++;
else
this.coluna = 0;
},
Masháumporém:comotemosum intervalodetempodefinidoparaa
mudançadequadro,temosquelevá-loemconta! Issonãoédifícil:vamos
manterumregistrodaúltimamudan çae,acadaciclo,verificarsejápassou
otempoespecificado:
78

## Página 86

CasadoCódigo Capítulo4. Folhasdesprites—spritesheets
proximoQuadro: function() {
// Momento atual
var agora = new Date().getTime();
// Se ainda não tem último tempo medido
if (! this.ultimoTempo) this.ultimoTempo = agora;
// Já é hora de mudar de coluna?
if (agora - this.ultimoTempo < this.intervalo) return;
if (this.coluna < this.numColunas - 1)
this.coluna ++;
else
this.coluna = 0;
// Guardar hora da última mudança
this.ultimoTempo = agora;
},
Nométodo desenhar,bastafazeroclippingcomoaprendemos:
desenhar: function(x, y) {
var larguraQuadro = this.imagem.width / this.numColunas;
var alturaQuadro = this.imagem.height / this.numLinhas;
this.context.drawImage(
this.imagem,
larguraQuadro * this.coluna,
alturaQuadro * this.linha,
largura,
altura,
x,
y,
largura,
altura
);
}
Nesteponto,játemosoSoniccorrendonatela,masaindasemalterarsua
posição.
79

## Página 87

4.4. Controleoheróipelotecladoevejasuaanimaç ão CasadoCódigo
4.4 C ontrole o herói pelo teclado e veja sua
animação
Chegouahoradejuntara Spritesheetcomasoutrasclassescriadasan-
teriormente( Animacaoe Teclado).VamoscontrolaroSoniccorrendo!
OspritedoSonicterásafun çõesde:
• Configurarsuarespectivaspritesheet;
• Leroestadodasteclasdesetaemudaroestadodosprite;
• Selecionaralinhanaspritesheetcorrespondenteaoestadodesejado;
• Responderaoloopdeanimação,implementandoosvelhosmétodos
atualizare desenhar.
<!-- arquivo: teste-spritesheet-2.html -->
<!DOCTYPE html>
<html>
<head>
<title>Personagem controlável e animado</title>
<script src="spritesheet.js"></script>
<script src="animacao.js"></script>
<script src="teclado.js"></script>
<script src="sonic.js"></script>
</head>
<body>
<canvas id="canvas_sonic" width="500" height="500"></canvas>
<script>
// Mover um personagem nunca foi tão fácil!
</script>
</body>
</html>
Primeiro,façamosasreferênciasdoCanvas,comodecostume. Depois,
criamososcontrolesdeteclado,deanimaç ãoeoSonic.Esteprecisarálero
80

## Página 88

CasadoCódigo Capítulo4. Folhasdesprites—spritesheets
tecladoparamovimentar-se.Esperoquevocêestejapercebendoquepratica-
mentetudoquecriaremosseguiráestepadrão:
var canvas = document .getElementById('canvas_sonic ');
var context = canvas.getContext('2d');
var teclado = new Teclado(document);
var animacao = new Animacao(context);
var sonic = new Sonic(context, teclado);
sonic.x = 0;
sonic.y = 200;
animacao.novoSprite(sonic);
animacao.ligar();
Crie a classe Sonic
PeloscomandosdadosaoSonicanteriormente,seuesqueletoconteráso-
menteo context,oteclado,aposiç ão(x,y)eosmétodosdesprite:
// arquivo: sonic.js
function Sonic(context, teclado) {
this.context = context;
this.teclado = teclado;
this.x = 0;
this.y = 0;
}
Sonic.prototype = {
atualizar: function() {
},
desenhar: function() {
}
}
Umadasfun çõesdaclasseSonicécontrolarsuaspritesheet,portantova-
moscriá-lanoconstrutor.Opteiporsemprereceberasimagenspeloconstru-
tor,poisassimoaplicativoprincipalterácontrolesobreseuevento onload
81

## Página 89

4.4. Controleoheróipelotecladoevejasuaanimaç ão CasadoCódigo
(porexemplo,paraanimarumateladeloadingqueserácriadaposterior-
mente).
function Sonic(context, teclado, imagem) {
this.context = context;
this.teclado = teclado;
this.x = 0;
this.y = 0;
// Criando a spritesheet a partir da imagem recebida
this.sheet = new Spritesheet(context, imagem, 3, 8);
this.sheet.intervalo = 60;
}
Arrumemosotesteparaforneceraimagem:
var imgSonic = new Image();
imgSonic.src = 'spritesheet.png';
var sonic = new Sonic(context, teclado, imgSonic);
Vamostambémligaraanimaç ãono onload:
// No final do script
imgSonic.onload = function() {
animacao.ligar();
}
Estados do sprite
Jásabemosmovimentarumspritenatelaapartirdoteclado.Noentanto,
ospritedoSonicsódeveráseranimadosealgumasetaestiverpressionada;
docontrário,aanimaçãodespritesnãodeveocorrer.Eeledeveseranimado
nadire çãocorreta.Aíentraanecessidadedetermosbemdefinidosquaisos
estadospossíveisparaosprite Sonic.
82

## Página 90

CasadoCódigo Capítulo4. Folhasdesprites—spritesheets
NateoriadaOrientaç ãoaobjetos,um estadoéumaformaemque
umobjetoseencontraequedeterminaseucomportamento. Emesta-
dosdiferentes,amesmamensagem(chamadademétodo)enviadaaum
objetopodeproduzircomportamentosdiferentes.
Osestadossãodefinidosapartirdeumoumaisatributosdeum
objeto. Porexemplo, umacontabancáriapodeestaremumestado
NO_VERMELHOcasoosaldosejamenorquezero.
OestadodoSonicdependerádedoisatributos: direcaoe andando.
Estandoparadoouandando,elepodeestarviradoparaadireitaouparaa
esquerda.Dessaforma,temosquatroestadospossíveisparaselecionarasim-
agenseanimar(ounão)apartirdaspritesheet.
Vamosdefinirosasdire çõesdoSoniccomvaloresúnicoseiniciaroes-
tadoatualnoconstrutor:
var SONIC_DIREITA = 1 ;
var SONIC_ESQUERDA = 2;
function Sonic(context, teclado, imagem) {
this.context = context;
this.teclado = teclado;
this.x = 0;
this.y = 0;
// Criando a spritesheet a partir da imagem recebida
this.sheet = new Spritesheet(context, imagem, 3 , 8);
this.sheet.intervalo = 60;
// Estado inicial
this.andando = false;
this.direcao = SONIC_DIREITA;
}
QueroagoratestarasetaparadireitaemovimentaroSonicdeacordo.
CasooSonicjánãoestejanesseestado,eutenhoqueiniciararespectivaan-
imaçãonaspritesheet. Aodispararumamudan çadeestado,semprepode-
83

## Página 91

4.4. Controleoheróipelotecladoevejasuaanimaç ão CasadoCódigo
moschecaroestadoanterioretomarasmedidasnecessárias. Nométodo
atualizar,fazemos:
if (this.teclado.pressionada(SETA_DIREITA)) {
// Se já não estava neste estado...
if (! this.andando || this.direcao != SONIC_DIREITA) {
// Seleciono o quadro da spritesheet
this.sheet.linha = 1;
this.sheet.coluna = 0;
}
// continua ...
}
Posicionamosanossaspritesheetnaprimeiracoluna(zero),dalinharel-
ativaaoSonicindoparaadireita. Aindadentrodoprimeiro if,devemos
entãodefiniroestadoatual,animaraspritesheetedeslocaroSonic:
if (this.teclado.pressionada(SETA_DIREITA)) {
// ...
// Configuro o estado atual
this.andando = true;
this.direcao = SONIC_DIREITA;
// Neste estado, a animação da spritesheet deve rodar
this.sheet.proximoQuadro();
// Desloco o Sonic
this.x += this.velocidade;
}
Usamosumnovoatributo, velocidade.Vamosiniciá-locomumvalor
padrãonoconstrutor:
// Pode ser ao final do construtor
this.velocidade = 10;
Omesmoraciocínioseráusadoparatrataramovimentaç ãoparaaes-
querda.Continuandoométodo atualizar:
84

## Página 92

CasadoCódigo Capítulo4. Folhasdesprites—spritesheets
else if (this.teclado.pressionada(SETA_ESQUERDA)) {
if (! this.andando || this.direcao != SONIC_ESQUERDA) {
this.sheet.linha = 2; // Atenção, aqui será 2!
this.sheet.coluna = 0;
}
this.andando = true;
this.direcao = SONIC_ESQUERDA;
this.sheet.proximoQuadro();
this.x -= this.velocidade; // E aqui é sinal de menos!
}
Finalmente,senenhumateclademovimentaç ãoestiverpressionada,o
Sonicestáparado.Devemos,noentanto,checarsuadire çãoatualparasaber
qualimagemdoSonicparadodevemosusar,seviradoparaaesquerdaou
paraadireita. Tambémnãochamamosométodo proximoQuadro,pois
nesteestadonãoháanimaç ão.
else {
if (this.direcao == SONIC_DIREITA)
this.sheet.coluna = 0;
else if (this.direcao == SONIC_ESQUERDA)
this.sheet.coluna = 1;
this.sheet.linha = 0;
this.andando = false;
}
Todoesteprocessamentoestáocorrendo,massequerpodemosverore-
sultado:ométodo desenharnãofoiimplementado!Aqui,podemossim-
plesmentechamaro desenhardaclasse Spritesheet:
desenhar: function() {
this.sheet.desenhar(this.x, this.y);
}
Issoétudo!Divirta-secontrolandooSonicparaoslados.Elecome çaini-
cialmenteparadoeviradoparaadireita,poisassimdefinimosnoconstrutor,
comoestadoinicial.
85

## Página 93

4.4. Controleoheróipelotecladoevejasuaanimaç ão CasadoCódigo
Nopróximocapítulo,falareisobredetecç ãodecolisões,umaspectofun-
damentaldagrandemaioriadosjogos.Sejaparagolpearuminimigo,oupara
coletarargolas,ainteraç ãodospritedopersonagemcomosoutros(inimigos,
blocos,plataformas)sedaráatravésdacolisãoentreasáreasqueocupamna
tela.
Figura4.5:Spritecontroladopeloteclado
86

## Página 94

Capítulo5
Detecçãodecolisões
Chegouahoradedetectarmoscolisões,ouseja,saberquandoumelemento
tocaoutronatela. Issotornarápossívelsaberquandouminimigoatacouo
heróioufoiatingido,ouquandooheróicoletouumitem.Apartirdecolisões,
disparamosinúmerosacontecimentosquesãoabasedosjogos,emespecial
osdeaventuraeaç ão.
5.1 C olisão entre retângulos
Umdosmétodosmaissimplesparadetectarcolisõesécriarumacaixadelim-
itadora(bounding box)aoredordecadaspriteeverificaraintersecç ãoentre
osretângulos:

## Página 95

5.1. Colisãoentreretângulos CasadoCódigo
Figura5.1:Spritescolidindo:retângulos(boundingboxes)apresentaminter-
secção
Figura5.2:Semintersecç ão,nãohácolisão
Mas,quemderaquetudofosseperfeito!Issopodenostrazeralgunsprob-
lemasdevidoàsáreasvaziasdossprites:
88

## Página 96

CasadoCódigo Capítulo5. Detecçãodecolisões
Figura5.3: Retângulosintersectandosemhaveracolisãorealdesejada. O
dragãocolidecomumaáreavaziadospritedoherói.
Aabordagemqueadotaremospararesolveresteproblemaéaseguinte:
cadaspritepoderáter váriosretângulosdecolisão,demarcandosuasprinci-
paisáreas:
Figura5.4:Definindováriosboundingboxesparaobjetosirregulares
Nossocontroleagoraficarámuitomaisprecisoecomqualidadebastante
satisfatóriaparaamaioriadoscasos.Colisãoempequenasáreasvaziasserão
imperceptíveisdevidoàvelocidadecomqueocorremasanimações(esempre
poderemosdefinirmaisumretânguloondeacharmosnecessário).
Ganhamostambémumbônus:nafigura5.4,temosumaaç ãodeataque(o
heróitentandosocarodragão).Podemosdiferenciarquemconseguiuatacar
quematravésdequalretângulodoheróicolidiucomoretângulododragão.
89

## Página 97

5.2. TestedaclasseColisor CasadoCódigo
Interseção de retângulos
Figura5.5:Intersecçãoderetângulos
Pelageometria,doisretângulosseintersectamse:
• (x1+largura1)>x2E
• x1<(x2+largura2)E
• (y1+altura1)>y2E
• y1<(y2+altura2)
Nopróximotópico,iniciaremosodesenvolvimentodeumaclasseque
aplicaessasfórmulasparadetectarcolisõesentresprites.
5.2 T este da classe Colisor
Iniciaremos o desenvolvimento da classe responsável por colidir objetos.
Comodecostume, iniciaremosporumpequenoaplicativodetesteonde
definimoscomoqueremosinteragircomaclasse.
90

## Página 98

CasadoCódigo Capítulo5. Detecçãodecolisões
Criaremos uma classe para essa nova funcionalidade. Começaremos
criandooaplicativodeteste,ondedefinimosdequeformaqueremosinteragir
comaclasse Colisor:
<!-- arquivo: teste-colisao-1.html -->
<!DOCTYPE html>
<html>
<head>
<title>Detecção de colisões</title>
<script src="colisor.js"></script>
<script src="bola.js"></script>
</head>
<body>
<canvas id="canvas_colisao" width="500" height="500">
</canvas>
<script>
// As bolinhas, além de quicar, baterão umas nas outras
</script>
</body>
</html>
NoJavaScript,obtemosocanvaseseu context,ecriamosalgumasbolin-
has:
var canvas = document .getElementById('canvas_colisao');
var context = canvas.getContext('2d');
var b1 = new Bola(context);
b1.x = 200;
b1.y = 200;
b1.velocidadeX = 10;
b1.velocidadeY = -5;
b1.cor = 'blue';
b1.raio = 20;
var b2 = new Bola(context);
91

## Página 99

5.2. TestedaclasseColisor CasadoCódigo
b2.x = 300;
b2.y = 300;
b2.velocidadeX = -5;
b2.velocidadeY = 10;
b2.cor = 'red';
b2.raio = 30;
Opróximopassoécriaroobjeto Colisorecolocarneleossprites:
var colisor = new Colisor();
colisor.novoSprite(b1);
colisor.novoSprite(b2);
Agora,façamosoloopdeanimaç ão. Porenquanto,esteloopseráuma
simplesfun ção. Percebaque,acadaciclo,apenasrealizamosastarefasque
nossosloopsjáfazeme,emseguida,mandamosocolisorrealizarseupro-
cessamento. Ocolisorseencarregarádeenviarmensagensaosobjetosque
colidirem.
requestAnimationFrame(animar);
function animar() {
// Limpando a tela
context.clearRect(0, 0, canvas.width, canvas.height);
// Atualizando os sprites
b1.atualizar();
b2.atualizar();
// Desenhando
b1.desenhar();
b2.desenhar();
// Processar colisões
colisor.processar();
requestAnimationFrame(animar);
}
92

## Página 100

CasadoCódigo Capítulo5. Detecçãodecolisões
5.3 A classe Colisor
A classe Colisor, como definimos antes, terá inicialmente 2 métodos:
novoSpritee processar. Manteremosumarraydesprites,damesma
formaqueaclasse Animacao:
function Colisor() {
this.sprites = [];
}
Colisor.prototype = {
novoSprite : function(sprite) {
this.sprites.push(sprite);
},
processar: function() {
// Aqui faremos a verificação de colisão
}
}
Ocoraçãodaclasseéométodo processar. Aqui,precisamostestar
quaisspritesestãocolidindoentresi.Faremosumalgoritmodotipo“todos
contratodos”noarraydesprites,usandodoisloops foraninhados. Para
cadaelementonoarray(primeiroloop),étestadasuacolisãocontratodosos
outros(segundoloop).Notequeaindaestamosabstraindoalógicadecálculo
dacolisão:
processar: function() {
for (var i in this.sprites) {
for (var j in this.sprites) {
// Não colidir um sprite com ele mesmo
if (i == j) continue;
// Abstrair a colisão
this.testarColisao(this.sprites[i], this.sprites[j]);
}
}
}
Onovométodo testarColisaoiráfazermaisum“todoscontrato-
dos”,agoraentreosretângulosdoprimeirospriteeosdosegundo.Lembre-
sedequecadaspritepoderádefinirmaisdeumretângulo(figura 5.4).Dessa
93

## Página 101

5.3. AclasseColisor CasadoCódigo
forma,criamosumlabel colisoesparapodermospararosdoisloopslogo
naprimeiracolisãoentreretângulosdetectada:
testarColisao: function(sprite1, sprite2) {
// Obter os retângulos de colisão de cada sprite
var rets1 = sprite1.retangulosColisao();
var rets2 = sprite2.retangulosColisao();
// Testar as colisões entre eles
colisoes:
for (var i in rets1) {
for (var j in rets2) {
// Ainda abstraindo a fórmula!
if (this.retangulosColidem(rets1[i], rets2[j])) {
// Eles colidem, vamos notificá-los
sprite1.colidiuCom(sprite2);
sprite2.colidiuCom(sprite1);
// Não precisa terminar de ver todos os retângulos
break colisoes;
}
}
}
}
Estaparteémuitoimportante,poisdefinimosumanova interfacequeos
spritesdeverãoseguirparapoderemparticipardocolisor. Essainterfaceé
formadapordoismétodos:
•retangulosColisao:devedevolverumarraycomosdadosdecada
retângulo;
•colidiuCom(sprite): recebeanotificaçãodequeospritecolidiu
comoutro(recebidocomoparâmetro)
Nósabstraímosmaisumpouco,deixandoparaofinalafun çãoqueveri-
ficasedoisretânguloscolidem.Consideroumaexcelentepráticairisolando
aspartes“difíceis”ouquenãotêmmuitoavercomoalgoritmosendocriado:
94

## Página 102

CasadoCódigo Capítulo5. Detecçãodecolisões
retangulosColidem: function(ret1, ret2) {
// Fórmula de interseção de retângulos
return (ret1.x + ret1.largura) > ret2.x &&
ret1.x < (ret2.x + ret2.largura) &&
(ret1.y + ret1.altura) > ret2.y &&
ret1.y < (ret2.y + ret2.altura);
}
5.4 C riando um sprite colidível
Agoraquetemosnosso Colisor,vamoscriarumanovaversãodaclasse
Bolaseguindoainterfaceexigidaporeste,alémdainterfacedeanimaç ãojá
vistaanteriormente:
function Bola(context) {
this.context = context;
this.x = 0;
this.y = 0;
this.velocidadeX = 0;
this.velocidadeY = 0;
this.cor = 'black';
this.raio = 10;
}
Bola.prototype = {
// Interface de animação
atualizar: function() {
},
desenhar: function() {
},
// Interface de colisão
retangulosColisao: function() {
},
colidiuCom : function(sprite) {
}
}
95

## Página 103

5.4. Criandoumspritecolidível CasadoCódigo
Os métodosatualizare desenharnão mudaram em nada. O
método atualizarmudaaposiç ãodaboladeacordocomsuasveloci-
dadeshorizontaleverticaleinverteasvelocidadesquandoelaestáquicando
noCanvas. Ométodo desenharusaaAPIdocontexto“2d”paradesen-
harabolaemsuaposiç ão,comacoreoraiodefinidos.Emcasodedúvida,
consultease ção2.4:
atualizar: function() {
var ctx = this.context;
if (this.x < this.raio || this.x >
ctx.canvas.width - this.raio)
this.velocidadeX *= -1;
if (this.y < this.raio || this.y >
ctx.canvas.height - this.raio)
this.velocidadeY *= -1;
this.x += this.velocidadeX;
this.y += this.velocidadeY;
},
desenhar: function() {
var ctx = this.context;
ctx.save();
ctx.fillStyle = this.cor;
ctx.beginPath();
ctx.arc(this.x, this.y, this.raio, 0, 2 * Math.PI, false);
ctx.fill();
ctx.restore();
}
Paraabola,ométodo retangulosColisao,criaráumúnicoretân-
guloque,mesmoassim,deveestarcontidoemumarray. Sóparalembrar,
emJavaScript,oscolchetesdelimitamarrayseaschavesdelimitamobjetos.
Temos,portanto,umobjetodentrodeumarray:
retangulosColisao: function() {
return [
{
96

## Página 104

CasadoCódigo Capítulo5. Detecçãodecolisões
x: this.x - this.raio, // this.x é o centro da bola
y: this.y - this.raio, // this.y idem
largura: this.raio * 2,
altura: this.raio * 2
}
];
},
Comoaposiç ão(x,y)daboladefineseucentro, descontamosoraio
paraacharaposiç ãodoseuretângulocircundante,quenarealidadeéum
quadrado.Oladodessequadradoéigualaodobrodoraiodabola:
Figura5.6:Retângulocircundantedabola
Faltaagoraométodo colidiuCom.Porenquanto,vamosmostraruma
mensagemdealerta:
colidiuCom: function(sprite) {
alert('PÁ! ');
}
Façaotesteevejaseamensagemaparece:
97

## Página 105

5.5. Melhorandoocódigo CasadoCódigo
Figura5.7:Colisãodetectada
Noentanto,amensagemaparecemuitasvezespelosseguintesmotivos:
• Estamosdetectandocolisõesrepetidas.TestamosAevimosquecolidiu
comB.AotestarB,nãoprecisamoscolidi-locomAnovamente!
• Sãoduasbolinhasdandoamesmarespostaàcolisão,entãotudoisso
ocorreemdobro!
• Resultado:quatro“PÁ!”porcolisão.
• Fora o fato de as bolinhas continuarem seu trajeto normalmente,
fazendocomquepassemuma“dentro”daoutraeprovoquemnovas
colisões.
5.5 M elhorando o código
Resolvendo a detecção repetida
Dojeitoqueestamosprogramando,cadacolisãoédetectadaduasvezes.Fize-
mosaseguintesequênciadeações:
• Pegamosoprimeirosprite(vamoschamá-lodeA);
98

## Página 106

CasadoCódigo Capítulo5. Detecçãodecolisões
• FazemosumloopemtodososoutrosetestamoscontraA;
• Detectamosumacolisãocomoutrosprite(quechamaremosde B);
• EnviamosumamensagemparaAeparaB.
Masoprocessonãoparaaí,chegouavezdetestarB!
• TestamosBcontraosoutros;
• DetectamossuacolisãocomA(quejáfoidetectadaanteriormente);
• EnviamosasmensagensnovamenteparaAeparaB.
Pararesolveroprimeiroproblema,vamosmanterumregistrodecolisões
játestadas.Istopodeserfeitodediversasformas,masqueimandoneurônios
euacheimaisfácilusarumobjetoassociativocontendoarrays,ondeeuasso-
cioumspriteaosoutroscomquemelejácolidiu.Veja:
// Exemplo teórico
// Crio um objeto vazio
var jaTestados = new Object();
// Associo um sprite a um array de outros
// Estou dizendo que a nave já colidiu com o meteoro e o item
var jaTestados[nave] = [meteoro, item];
Infelizmente,oselementosde jaTestadosnãopodemseroutrosob-
jetos.Nessecódigo, navedeveserumastring,poisaspropriedadesdeum
objetopodemserexpressasporstringsusandoasintaxede [colchetes](vejaa
seção1.4).
Prestebastanteaten çãoaoexemploteóricoaseguir. Segerarmosuma
stringúnicaparacadasprite,podemosassociarcadaumaaumarrayden-
trodesseobjetoassociativo. Tendoasstringsdevidamentearmazenadasno
objeto,podemosverificarseacolisãojáfoitestada:
99

## Página 107

5.5. Melhorandoocódigo CasadoCódigo
// Exemplo teórico
// A cada ciclo do loop estamos testando 2 sprites
// Criar as identificações
var id1 = stringUnica(sprite1);
var id2 = stringUnica(sprite2);
// Criar os arrays se não existirem
if (! jaTestados[id1]) jaTestados[id1] = [];
if (! jaTestados[id2]) jaTestados[id2] = [];
// Testar a colisão se já não foi testado id1 com id2
testarSeNaoRepetido(id1, id2);
// Registrando o teste para evitar repetição
jaTestados[id1].push(id2);
jaTestados[id2].push(id1);
Paraverificarseotesteatualnãoérepetido,podemosusarométodo
indexOfdosarrays. Porexemplo, jaTestados[id1].indexOf(id2)
devolveaposiç ãodastring id2dentrodoarrayassociadoà id1noobjeto,
ouovalor-1casoaindanãoexista:
// Exemplo teórico (parte final)
// Verificar se id1 com id2 já foi testado
if (! (jaTestados[id1].indexOf(id2) >= 0 ||
jaTestados[id2].indexOf(id1) >= 0) ) {
// Aqui testamos a colisão
}
Vamos, finalmente, para a parte prática. Primeiro, crie o método
stringUnica,quegeraráumastringparaospriteapartirdosdadosdeseus
retângulosdecolisão:
stringUnica : function(sprite) {
var str = '';
var retangulos = sprite.retangulosColisao();
100

## Página 108

CasadoCódigo Capítulo5. Detecçãodecolisões
for (var i in retangulos) {
str += 'x:' + retangulos[i].x + ',' +
'y:' + retangulos[i].y + ',' +
'l:' + retangulos[i].largura + ',' +
'a:' + retangulos[i].altura + '\n';
}
return str;
}
Acompanheanovaimplementaç ãodométodo processar,acrescen-
tandoosnovostestes.Iniciamoscomumobjetovazioe,acadaverificaç ão,
geramosumastringparacadasprite,verificamosseseusarraysjáexisteme
sejáfoitestadaessacolisão.Casonão,nósatestamosearegistramos:
processar: function() {
// Inicio com um objeto vazio
var jaTestados = new Object();
for (var i in this.sprites) {
for (var j in this.sprites) {
// Não colidir um sprite com ele mesmo
if (i == j) continue;
// Gerar strings únicas para os objetos
var id1 = this.stringUnica(this.sprites[i]);
var id2 = this.stringUnica(this.sprites[j]);
// Criar os arrays se não existirem
if (! jaTestados[id1]) jaTestados[id1] = [];
if (! jaTestados[id2]) jaTestados[id2] = [];
// Teste de repetição
if (! (jaTestados[id1].indexOf(id2) >= 0 ||
jaTestados[id2].indexOf(id1) >= 0) ) {
// Abstrair a colisão
this.testarColisao(this.sprites[i],
this.sprites[j]);
101

## Página 109

5.5. Melhorandoocódigo CasadoCódigo
// Registrando o teste
jaTestados[id1].push(id2);
jaTestados[id2].push(id1);
}
}
}
},
Sevocêrodaroprogramaagora,veráquereduzimosparadois“PÁ!”por
colisão,poissãoduasbolinhasrespondendo.
Um tratador geral de colisões
Porquesomenteasbolinhas(sprites)podemresponderàcolisão? Há
casos,porexemplo,emqueeuqueroumarespostaúnicaenãoénecessário
queosdoisobjetosrespondam.Quetalpoderfazer:
// Exemplo teórico
colisor.aoColidir = function(sprite1, sprite2) {
// Resposta única
};
Oatributo aoColidirseriaumafun çãodecallbackexecutadaemtoda
equalquercolisão. Estafun çãoreceberiacomoparâmetrososspritesque
colidiram.
Noconstrutordaclasse Colisor,inicieoatributo aoColidircom
null,somenteparadocumentá-lo:
function Colisor() {
this.sprites = [];
this.aoColidir = null;
}
Nométodo testarColisao,nopontoemqueasmensagenssãoenvi-
adas,acrescenteachamadaaessecallback.Usamosum ifparaverificarse
foiatribuídaumafun ção:
//...
102

## Página 110

CasadoCódigo Capítulo5. Detecçãodecolisões
if (this.retangulosColidem(rets1[i], rets2[j])) {
// Eles colidem, vamos notificá-los
sprite1.colidiuCom(sprite2);
sprite2.colidiuCom(sprite1);
// Tratador geral
if (this.aoColidir) this.aoColidir(sprite1, sprite2);
// Não precisa terminar de ver todos os retângulos
break colisoes;
}
//...
Noaplicativodeteste,logoapósacriaç ãodocolisor,podemosatribuira
seguintefun ção:
var colisor = new Colisor();
colisor.novoSprite(b1);
colisor.novoSprite(b2);
colisor.aoColidir = function(s1, s2) {
alert('PÁ');
};
Eométodo colidiuComda Bolaficarácomocorpovazio(poren-
quanto):
colidiuCom: function(sprite) {
}
Nesteponto,temosapenasum“PÁ!”paracadadeslocamento.Lembre-se
dequeasbolinhascontinuamsuatrajetóriaemlinharetaeprovocamnovas
colisõesenquantopassamumapelaoutra.
Fazendo os sprites quicarem
Sefizermosasbolinhasquicaremumanaoutra,resolvemoscompleta-
menteoproblemadoexcessodecolisões. Osegredo,aqui,éverificarqual
103

## Página 111

5.5. Melhorandoocódigo CasadoCódigo
bolinhaestáemquelado,efazercomquepasseairnessesentido(nãoim-
portaemquesentidoestejaindo).Afigura 5.8representaissonahorizontal:
Figura5.8: Ospritequeestáàesquerdavaiparaaesquerda,eoqueestáà
direitavaiparaadireita
Omesmovaleparaavertical:
Figura5.9:Ospritequeestáacimavaiparacima,eoqueestáabaixovaipara
baixo
104

## Página 112

CasadoCódigo Capítulo5. Detecçãodecolisões
Faremosistonométodo colidiuComdaclasse Bola. Paraforçara
bolaairparaumdeterminadolado,obtemososmódulosdasvelocidades
com Math.absecolocamosumsinalnegativonoscasosemqueavelocidade
passaasernegativa(paraesquerdaeparacima):
colidiuCom: function(sprite) {
if (this.x < sprite.x) // Estou na esquerda
this.velocidadeX = -Math.abs(this.velocidadeX); // -
else
this.velocidadeX = Math.abs(this.velocidadeX); // +
if (this.y < sprite.y) // Estou acima
this.velocidadeY = -Math.abs(this.velocidadeY); // -
else
this.velocidadeY = Math.abs(this.velocidadeY); // +
}
Temosagoraumaúnicamensagem“PÁ!”porcolisão.Sevocêquiserver
apenasasbolinhasquicarem,bastacomentaro alertousimplesmentere-
moverotratadorgeral:
// Remova este código ou comente o corpo da função:
colisor.aoColidir = function(s1, s2) {
//alert('PÁ');
};
Aqui,aspossibilidadessãoinfinitas.Nodecorrerdodesenvolvimentode
nossojogo,faremososobjetosatingidosportirossumirem,criaremosnovos
sprites(explosões),aumentamosindicadoresnatela(coletadeitem)etc.
Nopróximocapítulo,faremosasprimeirasexperiênciasparaojogode
naveilustradonoprimeirocapítulo.
105

## Página 114

Capítulo6
Iniciandoodesenvolvimentodo
jogo
Apartirdestepontodaremosinícioaodesenvolvimentodenossojogode
nave. Ogame engineaindaterámuitosacréscimosemelhorias,conforme
formosprecisandodenovosrecursos.Emalgummomento,eleficarámaduro
eprontoparauso,masminhaideiaémostrarcomoelepodesemprecontinuar
evoluindoconformevamosdesenvolvendojogoscomele.
6.1 A nimação de fundo com efeito parallax
Aprimeiracoisaquefaremoséofundo.Sevocêaindanãofezodownload
dosarquivosdestelivro,faç aemhttp://github.com/EdyKnopfler/games-js/
archive/master.zip,poisusaremosasimagenscontidasali.

## Página 115

6.1. Animaçãodefundocomefeitoparallax CasadoCódigo
Ocenáriodojogoteráoseguinteaspecto,emresoluç ãode500por500
pixels:
Figura6.1:Cenáriodojogodenave
Ofundo,noentanto,serácompostopor3imagensseparadas:umapara
ogradiente,outraparaasestrelaseoutraparaasnuvens. Estasduasúlti-
masterãofundotransparente,parapodermosencaixarumassobreasoutras,
comocamadas:
Figura6.2:Combinandooselementosdofundo
108

## Página 116

CasadoCódigo Capítulo6. Iniciandoodesenvolvimentodojogo
Cadaimagempossui500pixelsdelargurapor1000pixelsdealtura(por-
tanto,odobrodaáreadojogo).Elasrolarãopelocenário a velocidades difer-
entes,criandoumefeitodenominado parallax(paralaxe):
Figura6.3:Oselementosdofundorolamavelocidadesdiferentes
109

## Página 117

6.1. Animaçãodefundocomefeitoparallax CasadoCódigo
Paralaxe
Umaviãonocéuparecevoaraumavelocidadeincrivelmentelenta.
Noentanto,seestivéssemosláemcimaeelepassassepornós,overíamos
atodavelocidade.
Damesmaforma,viajandoporumaestrada,omatodiantedomeio-
fioeasplacaspassamvelozmente,enquantoaserraaolongeseafasta
devagar.
Esse efeito de velocidade aparente, na Física, é denominadopar-
alaxe. Quanto mais distante está um objeto, menor será sua veloci-
dade percebida por nós.
OlivroCoreHTML5Canvas,deDavidGeary,trazumexemplomuito
bemfeito,quepodeserconferidoaqui:
http://corehtml5canvas.com/code-live/ch05/example-5.17/example.
html
Obs.:entredesenvolvedoresdejogos,omaiscomuménosreferir-
mosaoefeitopelonomeeminglês(parallax ),razãopelaqualusareiesta
formadaquiparafrente.
Durantearolagem,cadaimagemdeveráserdesenhadanomínimoduas
vezes,deformaacobrirtodaaáreadedesenhodurantearolagem(figura
6.4). Sefosseumaimagemmenor,teríamosquedesenhá-lamaisvezes. A
cadaciclo,nósemendamososdesenhosaumaalturadiferente(marcadacom
umalinhavermelha):
110

## Página 118

CasadoCódigo Capítulo6. Iniciandoodesenvolvimentodojogo
Figura 6.4: Cada imagem de fundo é desenhada quantas vezes forem
necessáriasparacobriraáreadojogo.ComimagensmaioresqueoCanvas,
duasvezessãosuficientes
Reparequeospontosinicialefinaldogradientetêmdepossuiramesma
corparaserememendados(lembre-sedissoaocriarasimagensemseupro-
gramagráficopredileto). Damesmaforma,osextremosdasoutrasfiguras
precisamencaixar-seperfeitamente!Porexemplo,paracriarasnuvens,pode-
mosprocederdamaneiradescritanasfiguras 6.5e6.6:
111

## Página 119

6.1. Animaçãodefundocomefeitoparallax CasadoCódigo
Figura6.5:Quebramosumanuvempelocentro
Figura6.6:Viramoscadametadedecabe çaparabaixoeencaixamosnasbor-
dasdaimagem
Tomandoessescuidadosaoproduzirasimagensdefundodeseusgames,
112

## Página 120

CasadoCódigo Capítulo6. Iniciandoodesenvolvimentodojogo
aprogramaçãoficarámuitofácil.Vamoscriaraclasse Fundo,queserábasi-
camenteumspritecomotodososoutros.
T este para a classe Fundo
Paraacriaç ãodesteteste,crieumapastadenome imgnamesmapasta
ondeoHTMLserásalvo,ecopienelaosarquivos fundo-espaco.png,
fundo-estrelas.pnge fundo-nuvens.pngdopacotequevocêbaixou.
Vocêpodecriarouprocuraroutrasimagenscomfundotransparentetam-
bém,mascertifique-sederecortá-lasoudimensioná-laspara500x1000.
Figura6.7:CrieumapastajuntoaoHTMLecopieasimagensnela
OHTMLparaotestenãotemnadadeespecial:
<!-- arquivo: teste-fundo.html -->
<!DOCTYPE html>
<html>
<head>
<title>Fundos rolando em Parallax</title>
<script src="animacao.js"></script>
<script src="fundo.js"></script>
</head>
113

## Página 121

6.1. Animaçãodefundocomefeitoparallax CasadoCódigo
<body>
<canvas id="canvas_fundo" width="500" height="500"></canvas>
<script>
// Primeiro temos que carregar as imagens
</script>
</body>
</html>
Observ ação
Ao incluir arquivos já criados anteriormente (no caso,
animacao.js), pegue sempre o do capítulo mais recente. Neste
caso,aversãomaisrecentedaclasse Animacaoédocapítulo4.Acada
capítulooutópico,ogameenginepoderásofreralterações.
NoJavaScript,inicialmentemandamoscarregarasimagens:
var imgEspaco = new Image();
imgEspaco.src = 'img/fundo-espaco.png';
var imgEstrelas = new Image();
imgEstrelas.src = 'img/fundo-estrelas.png';
var imgNuvens = new Image();
imgNuvens.src = 'img/fundo-nuvens.png';
Emseguida,temosqueesperartodasseremcarregadas.Comojáapren-
demos,istoéfeitoatravésdoevento onload. Mantemosumcontadorde
quantasjáestãocarregadase,quandotodasestiveremprontas,aaplicaç ão
podedefato“iniciar":
var carregadas = 0;
var total = 3;
imgEspaco.onload = carregando;
imgEstrelas.onload = carregando;
114

## Página 122

CasadoCódigo Capítulo6. Iniciandoodesenvolvimentodojogo
imgNuvens.onload = carregando;
function carregando() {
carregadas ++;
if (carregadas == total) iniciar();
}
Nafun ção iniciar,fazemosasoperaçõeshabituais: inicializamoso
Canvas,criamosossprites(queaquiserãoosfundosrolando)eosincluímos
noobjetoanimador:
function iniciar() {
var canvas = document.getElementById('canvas_fundo');
var context = canvas.getContext('2d');
// Passo o context e a imagem para os objetos Fundo
var fundoEspaco = new Fundo(context, imgEspaco);
var fundoEstrelas = new Fundo(context, imgEstrelas);
var fundoNuvens = new Fundo(context, imgNuvens);
// Cada um a uma velocidade diferente
fundoEspaco.velocidade = 3;
fundoEstrelas.velocidade = 7;
fundoNuvens.velocidade = 10;
var animacao = new Animacao(context);
animacao.novoSprite(fundoEspaco);
animacao.novoSprite(fundoEstrelas);
animacao.novoSprite(fundoNuvens);
animacao.ligar();
}
Iniciando a classe Fundo
Apróximaetapaéiniciaraclasse Fundo. Sempreadotamosaprática
dereceberasimagenspeloconstrutor,parapermitirqueaaplicaç ãocontrole
quandotodasestãocarregadas:
// arquivo: fundo.js
function Fundo(context, imagem) {
115

## Página 123

6.1. Animaçãodefundocomefeitoparallax CasadoCódigo
this.context = context;
this.imagem = imagem;
this.velocidade = 0;
}
Fundo.prototype = {
atualizar: function() {
},
desenhar: function() {
}
}
Lembre-sedequecadafundodeveserdesenhadoduasvezes,emenda-
dospelasextremidadesemposiçõesdiferentes(figura 6.4). Crieoatributo
posicaoEmendaeoinicializenoconstrutorcomovalorzero:
function Fundo(context, imagem) {
this.context = context;
this.imagem = imagem;
this.velocidade = 0;
this.posicaoEmenda = 0;
}
Nométodo desenhar,desenhamosasduascópiasdaimagememen-
dadasnessaposiç ão:
desenhar: function() {
var img = this.imagem; // Para facilitar a escrita :D
// Primeira cópia
var posicaoY = this.posicaoEmenda - img.height;
this.context.drawImage(img, 0, posicaoY, img.width,
img.height);
// Segunda cópia
posicaoY = this.posicaoEmenda;
this.context.drawImage(img, 0, posicaoY, img.width,
img.height);
}
116

## Página 124

CasadoCódigo Capítulo6. Iniciandoodesenvolvimentodojogo
Nométodo atualizar,incrementamosaposiç ãodaemendaeavolta-
mosparazerocasoaimagemdecimades çamaisqueoiníciodoCanvas.A
figura6.8adianteilustraoqueacontece:
atualizar: function() {
// Atualizar a posição de emenda
this.posicaoEmenda += this.velocidade;
// Emenda passou da posição
if (this.posicaoEmenda > this.imagem.height)
this.posicaoEmenda = 0;
},
Figura6.8:Imagensdescerammuito,horadereposicioná-las
117

## Página 125

6.2. Controledanavenahorizontalenavertical CasadoCódigo
Jáestamosviajandopeloespaçosideral!
Figura6.9:Imagensdefundorolandoemparallax
6.2 C ontrole da nave na horizontal e na verti-
cal
Vamoscriarumanavecontrolável,inicialmenteemumnovotesteembranco,
edepoisjuntandocomofundoem parallax.Nopacotededownloaddolivro,
existeoarquivo nave.png(figura6.10),comdimensõesde36por48pixels.
Vocêpodeprocuraroucriaroutraimagem,mascertifique-sedequetenha
fundotransparente.
118

## Página 126

CasadoCódigo Capítulo6. Iniciandoodesenvolvimentodojogo
Figura6.10:Naveespacialcontrolável
Crieumanovapáginaparatestarmosocontroledanave. Estapágina
usaráasclasses Animacao, Tecladoe Nave(asercriada):
<!-- arquivo: teste-nave.html -->
<!DOCTYPE html>
<html>
<head>
<title>Nave Espacial Controlável</title>
<script src="animacao.js"></script>
<script src="teclado.js"></script>
<script src="nave.js"></script>
</head>
<body>
<canvas id="canvas_nave" width="500" height="500"></canvas>
<script>
// A nave andará por toda a tela!
</script>
</body>
</html>
NoJavaScript,temosoquejáfizemosmuitasvezes:
• referenciarocanvaseocontext;
• instanciarasclassesdogameengine;
• instanciarosprite(nocaso,anave)esuaimagem;
• aguardaraimagemcarregar;
119

## Página 127

6.2. Controledanavenahorizontalenavertical CasadoCódigo
• iniciaraanimaçãocomanavecomosprite.
// Canvas e contexto
var canvas = document.getElementById('canvas_nave');
var context = canvas.getContext('2d');
// Teclado e animação (game engine)
var teclado = new Teclado(document);
var animacao = new Animacao(context);
// Sprite da nave e sua imagem
var imgNave = new Image();
imgNave.src = 'img/nave.png';
var nave = new Nave(context, teclado, imgNave);
animacao.novoSprite(nave);
// Quando carregar a imagem, iniciar a animação
imgNave.onload = function() {
animacao.ligar();
}
Aclasse Navereceberánoconstrutorocontext,ocontroladordoteclado
eaimagemparadesenho:
// arquivo: nave.js
function Nave(context, teclado, imagem) {
this.context = context;
this.teclado = teclado;
this.imagem = imagem;
}
Nave.prototype = {
atualizar: function() {
},
desenhar: function() {
}
}
Nométodoatualizar,lemosoestadodecadasetadotecladoemove-
120

## Página 128

CasadoCódigo Capítulo6. Iniciandoodesenvolvimentodojogo
mosanavedeacordo.Paraassetasàdireitaeabaixo,tivemosqueconsiderar
otamanhodocanvasedescontarotamanhodanave,paraquenãoultrapas-
sasseaborda:
atualizar: function() {
if (this.teclado.pressionada(SETA_ESQUERDA) && this.x > 0)
this.x -= this.velocidade;
if (this.teclado.pressionada(SETA_DIREITA) &&
this.x < this.context.canvas.width - this.imagem.width)
this.x += this.velocidade;
if (this.teclado.pressionada(SETA_ACIMA) && this.y > 0)
this.y -= this.velocidade;
if (this.teclado.pressionada(SETA_ABAIXO) &&
this.y < this.context.canvas.height - this.imagem.height)
this.y += this.velocidade;
}
Observ ação
Aquiusamosquatro if,semousodo else,parapermitirquemais
deumasetapossamestarpressionadasaomesmotempo.Istonosper-
mitirámoveranavenadiagonal!
Anossanecessidadecrioutrêsatributos: x, ye velocidade.Vamos
iniciá-losnoconstrutor:
function Nave(context, teclado, imagem) {
this.context = context;
this.teclado = teclado;
this.imagem = imagem;
this.x = 0;
this.y = 0;
this.velocidade = 0;
}
121

## Página 129

6.2. Controledanavenahorizontalenavertical CasadoCódigo
Esetarvaloresadequadosnocódigodeteste,noevento onloaddaim-
agem,poiscalcularemosaposiç ãoapartirdasmedidasdaimageme,por-
tanto,eladeveestarcarregada:
// Quando carregar a imagem, iniciar a animação
imgNave.onload = function() {
// Centralizada na horizontal,
// alinhada embaixo na vertical
nave.x = canvas.width / 2 - imgNave.width / 2;
nave.y = canvas.height - imgNave.height;
nave.velocidade = 5;
animacao.ligar();
}
No método desenhar, copiaremos a imagem da nave sem
redimensioná-la:
desenhar: function() {
this.context.drawImage(this.imagem, this.x, this.y,
this.imagem.width, this.imagem.height);
}
Porúltimo,certifique-sedeque,noarquivo teclado.js,temososcódi-
gosdetodasasteclasdequeprecisamos:
// Códigos de teclas - aqui vão todos os que forem necessários
var SETA_ESQUERDA = 37 ;
var SETA_ACIMA = 38;
var SETA_DIREITA = 39;
var SETA_ABAIXO = 40;
var ESPACO = 32;
Voilà!Nossanavemove-seemtodasasdire ções,semultrapassaroslim-
itesdoCanvas!
122

## Página 130

CasadoCódigo Capítulo6. Iniciandoodesenvolvimentodojogo
Figura6.11:Controlandoanavepelassetasdoteclado
6.3 E fetuando disparos
Agoraacoisavaicome çaraficardivertida:nossanavejásemexe,éhorade
fazê-ladisparartiros!
123

## Página 131

6.3. Efetuandodisparos CasadoCódigo
Figura6.12:Fazendoanaveatirar
Façaumacópiadoarquivodotesteanterior( teste-nave.html)e
renomeie-a para teste-tiros.html. Logo antes doeventoonload
daimagem,coloqueocódigoquemandaanaveatiraraodispararatecla
Espaço:
// Nunca foi tão fácil mandar uma nave atirar!
teclado.disparou(ESPACO, function() {
nave.atirar();
});
// Quando carregar a imagem, iniciar a animação
imgNave.onload = function() {
...
}
Agoravamoscriarométodo atirarnaclasse Nave. Criarumtiroé
fácil,oproblemaéincluí-lonaanimaç ãodesprites. Nãotemosnenhuma
referênciaaoobjeto animacao!
124

## Página 132

CasadoCódigo Capítulo6. Iniciandoodesenvolvimentodojogo
},
// Não esqueça da vírgula no último método quando criar outro
atirar: function() {
var t = new Tiro(this.context);
// Como incluir o novo tiro na animação?
}
Sevocêfezaliçãodecasadireitinho,poderiapensar:recebopeloconstru-
tor!Sim,éumagrandeideia,eeuapoio.Receberascoisaspeloconstrutoré
bemmelhordoquefazerreferênciaàvariável animacaodoaplicativodire-
tamente.Eseeutentoreaproveitarestaclasseondenãotenhoestavariável?
Receberpeloconstrutorfor çariaoaplicativoafornecerumaanimaç ãopara
anave.
No entanto, pensando um pouco mais além, pode ser que eu tenha
dezenas(oucentenas)devariedadesdespritesqueprecisamcriaroutrosna
animação.Porquenãodamosa todoselesumareferênciaàanimacao?Basta
abriraclasse Animacaoemodificarseumétodo novoSprite:
novoSprite: function(sprite) {
this.sprites.push(sprite);
sprite.animacao = this;
},
Agoraqualquerspriteincluídotemumareferênciaaoobjetoquecontrola
aanimação!Nãoélegal?
Podemosvoltaraométodo atirarda Naveeusaroobjetoqueele
recebeu:
atirar: function() {
var t = new Tiro(this.context);
this.animacao.novoSprite(t);
}
Enfim,vamoscriaroesqueletodaclasse Tiro:
// arquivo: tiro.js
function Tiro(context) {
125

## Página 133

6.3. Efetuandodisparos CasadoCódigo
this.context = context;
}
Tiro.prototype = {
atualizar: function() {
},
desenhar: function() {
}
}
Ondeotirovaiaparecer?Napontadanave,vocêvaipensar.Dessaforma,
éinteressanterecebermosanavepeloconstrutor:
function Tiro(context, nave) {
this.context = context;
this.nave = nave;
}
Nométodo atirar,anavepassaasimesmaparaotiroseposicionar:
atirar: function() {
var t = new Tiro(this.context, this);
this.animacao.novoSprite(t);
}
Tendoumareferênciaànave,podemosposicionarotiro. Faremosisso
nopróprioconstrutor:
function Tiro(context, nave) {
this.context = context;
this.nave = nave;
// Posicionar o tiro no bico da nave
this.largura = 4;
this.altura = 20;
this.x = nave.x + nave.imagem.width / 2 - this.largura / 2;
this.y = nave.y - this.altura;
this.velocidade = 10;
}
126

## Página 134

CasadoCódigo Capítulo6. Iniciandoodesenvolvimentodojogo
Paraatualizarotironaanimaç ão,apenasofaremossubirnatela,sub-
traindosuaposiç ão y:
atualizar: function() {
this.y -= this.velocidade;
},
Paradesenhá-lo, faremosumpequenoretângulo. Criamosumnovo
atributo, cor,paraquepossaseralteradoagosto:
desenhar: function() {
var ctx = this.context;
ctx.save();
ctx.fillStyle = this.cor;
ctx.fillRect(this.x, this.y, this.largura, this.altura);
ctx.restore();
}
Noconstrutor,vamosinicializar corcomumacormaisescura,poisa
naveaindaestáemfundobranco:
// Escolha sua cor!
this.cor = 'red';
Porúltimo,nãoseesque çadecolocarareferênciaaoarquivo tiro.js
napáginaHTML:
<head>
<title>Nave Espacial Que Atira</title>
<script src="animacao.js"></script>
<script src="teclado.js"></script>
<script src="nave.js"></script>
<script src="tiro.js"></script>
</head>
Divirta-se! Nopróximocapítulo, iremoscriarinimigosparaonosso
herói.
127

## Página 135

6.3. Efetuandodisparos CasadoCódigo
Exercícios:
Sevocêentendeubemosconceitos,astarefasaseguirnãodeverão
sertãodifíceisassim:
• Tenteintegrarofundoemparallaxcomanavesemexendoeati-
rando.
• Tentetambématirarparaosladoseparaadiagonal.Istorequererá
leroestadodasteclasdedire çãoedarvelocidadehorizontalao
tiro.
Comeceabrincareaexperimentar!
128

## Página 136

Capítulo7
Criandoinimigos
Chegouahoradeadicionarmosumpoucodeemo çãoverdadeiraemnosso
game. Denadaadiantatermosumjogoenãotermosquemcombater,não
émesmo?Portanto,criaremosagoraosprimeirosinimigos.Nestecapítulo,
utilizaremosbastanteaclasse Colisorparadetectarquandoosinimigos
colidiremcomostirosecomanave.
Nopacotedearquivosdolivro,estápresenteaimagem ovni.png.Nosso
objetivoseráfazerOVNIscaíremdoaltodatela,emvelocidadeseposições x
diferentes.

## Página 137

7.1. Primeirotestecomnaveeinimigos CasadoCódigo
Figura7.1:OVNIscairãonatela!
7 .1 P rimeiro teste com nave e inimigos
Comodecostume,vamoscome çarcomapáginacontendooaplicativode
teste. Vejacomoaquantidadedetags <script>estácrescendo! Nosso
protótipoestácadavezmaispertodeumjogo100%funcional.
Figura7.2:CenacomOVNIsenavedoherói
<!-- arquivo: teste-inimigos.html -->
<!DOCTYPE html>
<html>
130

## Página 138

CasadoCódigo Capítulo7. Criandoinimigos
<head>
<title>Inimigos</title>
<script src="animacao.js"></script>
<script src="teclado.js"></script>
<script src="nave.js"></script>
<script src="tiro.js"></script>
<script src="colisor.js"></script>
<script src="ovni.js"></script>
</head>
<body>
<canvas id="canvas_inimigos" width="500" height="500">
</canvas>
<script>
// Inimigos terríveis tentarão destruí-lo!
</script>
</body>
</html>
Paracome çaroJavaScript,vamoscarregarasimagens,poisosspritespre-
cisarãorecebê-laspelosconstrutores.Comosãoduas,usaremosumafun ção
carregandoparadetectarquandoelasestiveremprontas:
// Imagens
var imgNave = new Image();
imgNave.src = 'img/nave.png ';
imgNave.onload = carregando;
var imgOvni = new Image();
imgOvni.src = 'img/ovni.png ';
imgOvni.onload = carregando;
Emseguida,acriaç ãodosobjetosbásicos:canvasecontexto,teclado,an-
imação,spritedanaveecolisor.Tambémconfiguramosodisparopelatecla
Espaço.Podeparecerrepetitivo,masaideiaéessamesmo:tornaronegócio
padronizado(edessaformavocêfixamelhorosconceitos)!
131

## Página 139

7.1. Primeirotestecomnaveeinimigos CasadoCódigo
// Inicialização dos objetos
var canvas = document.getElementById('canvas_inimigos');
var context = canvas.getContext('2d');
var teclado = new Teclado(document);
var animacao = new Animacao(context);
var nave = new Nave(context, teclado, imgNave);
animacao.novoSprite(nave);
var colisor = new Colisor();
colisor.novoSprite(nave);
teclado.disparou(ESPACO, function() {
nave.atirar();
});
Agoracrieasfun ções carregando,quemonitoraocarregamentodas
imagens,e iniciar,chamadapor carregandoquandotodasasimagens
estiveremprontas. Nafunção iniciar,posicionamosanave,iniciamosa
animaçãoedefinimosqueacada1000milissegundosumnovoinimigoserá
criadonatela,usandoafun ção setIntervaldoJavaScript:
// Carregamento e inicialização
var carregadas = 0;
function carregando() {
carregadas ++;
if (carregadas == 2) iniciar();
}
function iniciar() {
nave.x = canvas.width / 2 - imgNave.width / 2;
nave.y = canvas.height - imgNave.height;
nave.velocidade = 5;
animacao.ligar();
setInterval(novoOvni, 1000);
}
132

## Página 140

CasadoCódigo Capítulo7. Criandoinimigos
Quemcriaráoinimigoéafun ção novoOvni. Sabendoqueaimagem
possui64x32pixels,nósaposicionamosacimadaáreavisíveldojogo,de-
scontando32pixelsdealtura. Paradarumpoucodeemo çãoaogame,a
posiçãohorizontaleavelocidadesãodefinidasaleatoriamenteparacadanovo
inimigo,comoauxíliode Math.randome Math.floor.Tambémépreciso
colocaroinimigonocolisor:
// Criação dos inimigos
function novoOvni() {
var ovni = new Ovni(context, imgOvni);
// Mínimo: 5; máximo: 20
ovni.velocidade =
Math.floor( 5 + Math.random() * (20 - 5 + 1 ) );
// Mínimo: 0;
// máximo: largura do canvas - largura do ovni
ovni.x =
Math.floor( Math.random() *
(canvas.width - imgOvni.width + 1) );
// Descontar a altura
ovni.y = -imgOvni.height;
animacao.novoSprite(ovni);
colisor.novoSprite(ovni);
}
133

## Página 141

7.2. AclasseOvni CasadoCódigo
Combinando Math.random e Math.floor
Ométodorandomretornaumnúmeroaleatóriofracionário,entre0
e1.Paragerarumnúmeroaleatóriointeiro,usamosafórmula:
function aleatorio(min, max) {
return min + Math.floor(Math.random() * (max - min + 1));
}
O método floor descarta a parte fracionária do resultado,
arredondando-oparaointeirodemenorvalor(nãoomaispróximo).
Padronizando a codificação
Vamossempreadotaraseguintesequênciadecodificaç ãoaocriar
novosaplicativos:
• Primeiro,carregamosasimagens,poisosobjetosdojogodepen-
demdelas;
• Emseguida,instanciamososobjetosdogameengine(animação,
teclado,colisor)eossprites,usandoasimagensquandonecessário;
• Porúltimo,criamosasfunçõesdeinicializaç ão,quesódevemex-
ecutarquandoasimagensestiveremcompletamentecarregadas.
7 .2 A classe Ovni
Vamoscriaraclasse Ovni,inicialmentesemsepreocuparcomainterfacede
colisão.Comodecostume,come çamosconstruindoumesqueletoapartirdo
queidealizamosparaaclassenapáginaHTML:
134

## Página 142

CasadoCódigo Capítulo7. Criandoinimigos
// arquivo: ovni.js
function Ovni(context, imagem) {
this.context = context;
this.imagem = imagem;
this.x = 0;
this.y = 0;
this.velocidade = 0;
}
Ovni.prototype = {
atualizar: function() {
},
desenhar: function() {
}
}
Seoobjetivoéfazeroinimigodescerpelatela,ométodo atualizar
temdeincrementaraposiç ão y:
atualizar: function() {
this.y += this.velocidade;
},
Jáométodo desenharapenasdesenhaaimagemquefoirecebidano
construtor:
desenhar: function() {
var ctx = this.context;
var img = this.imagem;
ctx.drawImage(img, this.x, this.y, img.width, img.height);
}
Játemosumanavequeatira(programadanocapítuloanterior)eOVNIs
descendonomesmoaplicativo(figura 7.2)!
7 .3 A dicionando fundo em parallax
No capítulo anterior, criamos um fundo consistindo de várias imagens
emmovimento,cadaumaemvelocidadediferente,criandoumefeitoque
135

## Página 143

7.3. Adicionandofundoemparallax CasadoCódigo
chamamos parallax.Chegouahoradeintegraressefundoaonossogame.
Primeiro,façaumacópiadoarquivo teste-inimigos.html,dando-
lheonome teste-inimigos-e-fundo.html.Iremosfazeralgumasal-
teraçõesemdeterminadospontos.
Noiníciodocódigo,ondecarregamosasimagens,adicioneocarrega-
mentodastrêsimagensdefundo:
// Imagens
var imgEspaco = new Image();
imgEspaco.src = 'img/fundo-espaco.png';
imgEspaco.onload = carregando;
var imgEstrelas = new Image();
imgEstrelas.src = 'img/fundo-estrelas.png';
imgEstrelas.onload = carregando;
var imgNuvens = new Image();
imgNuvens.src = 'img/fundo-nuvens.png';
imgNuvens.onload = carregando;
// Imagens da nave e dos ovnis...
Agoratemoscincoimagensnototal,portantotemosquealterarafun ção
carregandoparacontaraté5. Umavariável totalnospermitiráalterar
esteparâmetromaisfacilmente:
// Carregamento e inicialização
var carregadas = 0;
var total = 5;
function carregando() {
carregadas++;
if (carregadas == total) iniciar();
}
Precisamosadicionarosfundosàanimaç ão antesdosoutrossprites,de
formaqueelessejamdesenhadosprimeiro.Nase çãoondeinicializamosos
objetosdogameengineeossprites, antes da criaç ão da nave,adicioneo
código:
136

## Página 144

CasadoCódigo Capítulo7. Criandoinimigos
// Primeiro os objetos do game engine
var canvas = ...
var context = ...
var teclado = ...
var animacao = ...
// Em seguida as imagens de fundo
var fundo1 = new Fundo(context, imgEspaco);
fundo1.velocidade = 3;
animacao.novoSprite(fundo1);
var fundo2 = new Fundo(context, imgEstrelas);
fundo2.velocidade = 7;
animacao.novoSprite(fundo2);
var fundo3 = new Fundo(context, imgNuvens);
fundo3.velocidade = 10;
animacao.novoSprite(fundo3);
// Depois do fundo, a nave e outros sprites
var nave = ...
137

## Página 145

7.3. Adicionandofundoemparallax CasadoCódigo
Figura7.3:CenacomOVNIs,navedoheróiefundorolandoemparallax
Nesteponto,ofundojásemovimentajuntamentecomanaveeosinimi-
gos(figura7.3).Apartirdeagora,comotrabalharemossemprecomumfundo
rolando,nãoéprecisomaisrealizaralimpezadetelaacadaciclodaanimaç ão,
bastandoapenasdesenharofundoparacobriratela. Issonãotraráefeitos
práticosmaseconomizaráalgumprocessamento.Porisso,vamoscomentar
alinhaquelimpaatelanométodo proximoFramedaclasse Animacao.
proximoFrame: function() {
// Posso continuar?
if ( ! this.ligado ) return;
// Comente o comando que limpa a tela
// this.limparTela();
// ...
}
Obs.: recomendoquevocêfaçaumacópiadoarquivo animacao.js
138

## Página 146

CasadoCódigo Capítulo7. Criandoinimigos
especialmenteparaestetópico.Docontrário,testesanterioresserãoafetados
(figura7.4).Paraospróximoscapítulos,vocêpoderáusaranovaversãodesse
arquivo.
Figura7.4:Mantenhaalimpezadetelaparaostestesanteriores,casocontrário
serãoprejudicados.
Experimenterodaroaplicativo. Játemosumprotótipodejogoquase
pronto!
7 .4 A dicionando colisão
Apartequefaltaparatermosumprotótipofuncionalédetectaracolisãoentre
ossprites—maisexatamente,entreoinimigoeanave(causandoamortedo
herói)eentreosinimigoseotiro(causandoadestruiç ãodoinimigo).
Precisamos, em algum ponto de nosso programa, chamar o método
processardo Colisor. Quetalsea Animacaochamarocolisorem
cadaciclo?Assim,teremosumcontrolemaisgeral,queocorreemconjunto
comoprocessamentodosciclosdeanimaç ão.
139

## Página 147

7.4. Adicionandocolisão CasadoCódigo
Indomaisalém,a Animacaopoderiamanterumalistadeprocessamen-
tosaexecutar,dosquaisuméo Colisor.Maisadiante,podemosadicionar
Gravidade, TelaMoveleporaívai.Faç amosisto!
Noconstrutordaclasse Animacao,adicioneocomandoqueiniciaum
arrayvazio processamentos:
this.processamentos = [];
Crieométodo novoProcessamento,parainserirnovosprocessamen-
tosnoarray:
novoProcessamento: function(processamento) {
this.processamentos.push(processamento);
processamento.animacao = this;
}
Nométodo proximoFrame,vamosexecutarestesprocessamentos:
proximoFrame: function() {
// Posso continuar?
if ( ! this.ligado ) return;
// Atualizamos o estado dos sprites
for (var i in this.sprites)
this.sprites[i].atualizar();
// Desenhamos os sprites
for (var i in this.sprites)
this.sprites[i].desenhar();
// Processamentos gerais
for (var i in this.processamentos)
this.processamentos[i].processar();
// Chamamos o próximo ciclo
var animacao = this;
requestAnimationFrame(function() {
animacao.proximoFrame();
});
},
140

## Página 148

CasadoCódigo Capítulo7. Criandoinimigos
Iniciando o teste
Já temos o arquivo teste-inimigos-e-fundo.html, com
tudo o que foi feito até aqui. Faça uma cópia e dê o nome
teste-colisao-inimigos.html. Localize o ponto onde o colisor
écriadoeacrescente-ocomoumprocessamentodaanimaç ão:
var colisor = new Colisor();
colisor.novoSprite(nave);
animacao.novoProcessamento(colisor);
Osinimigosjáestãosendoadicionadosnocolisor,porémfaltamostiros.
Elessãocriadosnométodo atirarda Nave.Modifique-oparaqueotiro
criadosejaincluídonocolisor:
atirar: function() {
var t = new Tiro(this.context, this);
this.animacao.novoSprite(t);
this.colisor.novoSprite(t);
}
Mas... anavetemreferênciaaocolisor? Seriabomquecadaspriteadi-
cionadonocolisortivesseumareferênciaaeste(assimcomoa Animacaojá
faz).Modifiqueométodo novoSpritedo Colisorparafazerisso:
novoSprite : function(sprite) {
this.sprites.push(sprite);
sprite.colisor = this;
},
141

## Página 149

7.4. Adicionandocolisão CasadoCódigo
Referências cruzadas
Vamosadotarapráticade,emqualquerobjetoqueagregueeprocesse
váriosoutrosobjetos( Animacao, Colisoretc.),colocarnelesuma
referênciaaoobjetoagregador.Porexemplo:
// Adiciono um sprite ao colisor
colisor.novoSprite(carro);
// O colisor adiciona-se a si mesmo no sprite
novoSprite: function(sprite) {
this.sprites.push(sprite);
sprite.colisor = this;
},
Adaptando os sprites à interface do colisor
Nesteponto,setentarmosrodaroaplicativo,aanimaç ãoirápararabrup-
tamenteeteremosaseguintemensagemnoconsole( Ctrl+Shift+Jno
GoogleChrome, Ctrl+Shift+KnoFirefox):
Figura7.5:Tentandochamarummétodoquenãoexistenoobjeto
Issoocorreuporqueagoraocolisorestásendochamado,eeste,porsua
vez,chamaosmétodos retanguloColisaoe colidiuCom.Precisamos
implementá-losnasclasses Nave, Tiro,e Ovni. Façaistonastrês,por
enquantodeixandooscorposdosmétodosvazios:
retangulosColisao: function() {
142

## Página 150

CasadoCódigo Capítulo7. Criandoinimigos
},
colidiuCom: function(outro) {
}
Agoraoaplicativovoltouafuncionarcomoaversãoanterior. Vamos
definirosretângulosdecolisãodossprites. Omaisfáciléodo Tiro,que
jáéretangular:
retangulosColisao: function() {
return [ {x: this.x, y: this .y, largura: this.largura,
altura: this.altura} ];
},
Paraanave,vamosfazertrêsretângulos,paraocorpoeasduasasas
(figura7.6). Nãoháumaregrafixadequantosretângulosusar,vocêdefine
apartirdoformatodeseuobjeto.Nocasodeobjetosmaiscomplexos,éin-
teressantedesenharosretângulosnatela,afimdepodermosajustarosvalores
dasposiçõesmaisfacilmente:
retangulosColisao: function() {
// Estes valores vão sendo ajustados aos poucos
var rets =
[
{x: this.x+2, y: this.y+19, largura: 9, altura: 13},
{x: this.x+13, y: this .y+3, largura: 10, altura: 33},
{x: this.x+25, y: this .y+19, largura: 9, altura: 13}
];
// Desenhando os retângulos para visualização
var ctx = this.context;
for (var i in rets) {
ctx.save();
ctx.strokeStyle = 'yellow';
ctx.strokeRect(rets[i].x, rets[i].y, rets[i].largura,
rets[i].altura);
ctx.restore();
}
143

## Página 151

7.4. Adicionandocolisão CasadoCódigo
return rets;
},
Figura7.6:Retângulosdecolisãodanave
Paraanalisarosretângulosdespritesemmovimento,facilitamuitoabrir
oconsole( Ctrl+Shift+JnoChrome;noFirefoxinstaleopluginFirebug)
echamarocomando: animacao.desligar():
Figura7.7:Pareaanimaç ãopeloconsoleparaanalisarosretângulosdecolisão
ParaoOVNI,tambémuseitrêsretângulos:
retangulosColisao: function() {
var rets =
[
{x: this.x+20, y: this.y+1, largura: 25, altura: 10},
{x: this.x+2, y: this.y+11, largura: 60, altura: 12},
{x: this.x+20 , y: this.y+23, largura: 25, altura: 7},
];
144

## Página 152

CasadoCódigo Capítulo7. Criandoinimigos
// Desenho dos retângulos ...
}
Figura7.8:RetângulosdecolisãodoOVNI
Rodeoaplicativoedêalgunstiros.Vocêrapidamenteperceberáumprob-
lema...
7 .5 E stamos experimentando lentidão!
Nossojogochegouemumpontoemquemuitosobjetosestãosendocriados,
mas não estão sendo destruídos! Agora,alémdoloopdeanimaç ão,eles
tambémdevemresponderàschamadasdocolisor.Isso,claro,estásobrecar-
regandooaplicativo.
145

## Página 153

7.5. Estamosexperimentandolentidão! CasadoCódigo
Figura7.9:Experimentedarmuitostiros:nossojogoficarábemlento!
Nossogameengine,emboratenhafuncionadoperfeitamenteatéaqui,
carecedealgobembásico:nãoépossível excluirobjetos,tantodaanimaç ão
quantodocolisor.Estamossemprecriandonovostiroseinimigos,masnão
osdestruímosquandoestesdeixamatela.Resultado:continuamsendopro-
cessados.
Oqueprecisamosparaexcluirtiroseinimigosquejáseforamdatela?
Importante:sigaestetópicocombastanteaten ção,poisfaremosalter-
açõesdelicadasnogameengine.Procure semprefazerbackupsdetodosos
arquivos.
Problema na exclusão de elementos
Antesdecriarométodo excluirSpritenasclasses Animacaoe
Colisor,precisocontar-lheumacoisa. Quandoestavadesenvolvendoo
protótipodejogoparaestelivro,aoimplementaraexclusãodeitensdosar-
rays,euinocentementemandeiexcluiroelementotãologoqueelesaíada
tela:
// Exemplo teórico
146

## Página 154

CasadoCódigo Capítulo7. Criandoinimigos
// Não faça isto!
atualizar: function() {
// Sprite sumiu da tela
if (this.y > this.context.canvas.height) {
this.animacao.excluirSprite(this);
this.colisor.excluirSprite(this);
}
}
Éumcódigosimpleseclaro,masqueprovocouumbugquelevei horas
paradescobriroqueera.Normalmenteeutenhodeixadoosbugsaparecerem
paradiscutirasoluç ãonoprópriocaminhardolivro,masdestaveznãovou
fazerissocomvocê.Voupoupá-lodesteaqui.
Aexplicaçãoéqueestamosexcluindoelementosdeumarray dentro do
loop que percorre esse array!Masondeestáesseloop?Naclasse Animacao,
método proximoFrame, temos váriosloops que chamam os métodos
atualizar, desenhareo processardocolisor,sendoqueestefazoutro
loopemseuarray!
// Trecho do método proximoFrame da classe Animacao
// Atualizamos o estado dos sprites
for (var i in this.sprites)
this.sprites[i].atualizar();
// Desenhamos os sprites
for (var i in this.sprites)
this.sprites[i].desenhar();
// Processamentos gerais
for (var i in this.processamentos)
this.processamentos[i].processar();
Se, por exemplo, eu mando excluir um item de dentro do método
atualizar,oloopquechamao atualizarficaráórfãodaqueleitem!
Comoregrageral,vocênãodeveexcluiritensdeumarraydentrodoloop
queopercorre:
147

## Página 155

7.5. Estamosexperimentandolentidão! CasadoCódigo
// Exemplo teórico
// Você não deve fazer isto
// Criar um array
var meuArray = ['banana', 'laranja', 'limão'];
// Fazer um loop
for (var i in meuArray) {
// Forçar uma exclusão dentro do loop
if (meuArray[i] == 'laranja')
excluirElemento(meuArray[i], meuArray);
// Fazer alguma tarefa com o array
document.write(meuArray[i] + '<br>');
}
Asolução?Manterumalistadeobjetosaexcluir,eexcluí-lossomenteao
fimdociclodeanimaç ão!
Excluindo elementos dos arrays
Vamosentãoimplementaraexclusãodeelementoscombastantecalma.
Destaforma,eliminamosoproblemadalentidãoepoderemos,enfim,tratar
ascolisões,fazendooinimigoeotirosumiremquandosechocarem,por
exemplo.
Temosqueiniciaraslistasdeelementosaseremexcluídos.Noconstrutor
daclasse Colisor,faça:
this.spritesExcluir = [];
Paraaclasse Animacao,hádoisarrays:
this.spritesExcluir = [];
this.processamentosExcluir = [];
Ométodo excluirSpriteapenasincluiráospritenessalista. No
Colisor,temos:
excluirSprite: function(sprite) {
this.spritesExcluir.push(sprite);
}
148

## Página 156

CasadoCódigo Capítulo7. Criandoinimigos
Na Animacao, temos que ter excluirSprite e
excluirProcessamento:
excluirSprite: function(sprite) {
this.spritesExcluir.push(sprite);
},
excluirProcessamento: function(processamento) {
this.processamentosExcluir.push(processamento);
}
Nofimdométodo processardo Colisor,colocamosumachamada
a processarExclusoes:
processar: function() {
// ...
this.processarExclusoes();
},
Evamoscriaressemétodo processarExclusoes.Comopodehaver
váriosspritesaseremeliminados,vamosnaverdademontarumnovoarray
contendotodososelementos,menosaquelesqueforamexcluídos. Oarray
antigopoderáserdescartadoeficarálivreparaocoletordelixo(garbage col-
lector)doJavaScriptapagá-lodamemória:
processarExclusoes: function() {
// Criar um novo array
var novoArray = [];
// Adicionar somente os elementos não excluídos
for (var i in this.sprites) {
if (this.spritesExcluir.indexOf(this.sprites[i]) == -1)
novoArray.push(this.sprites[i]);
}
// Limpar o array de exclusões
this.spritesExcluir = [];
// Substituir o array velho pelo novo
149

## Página 157

7.5. Estamosexperimentandolentidão! CasadoCódigo
this.sprites = novoArray;
}
Paraa Animacao, oprocedimentoémuitosemelhante. Nofimdo
métodoproximoFrame,logoantesdachamadadopróximociclo,chame
tambémométodoprocessarExclusoes:
proximoFrame: function() {
// ...
// Processamento de exclusões
this.processarExclusoes();
// Chamamos o próximo ciclo
var animacao = this;
requestAnimationFrame(function() {
animacao.proximoFrame();
});
},
Evamoscriaressemétodo.Elesegueomesmoalgoritmodeseuequiva-
lenteno Colisor,sóéumpoucomaiorporqueestamoslidandocomdois
arrays.
processarExclusoes: function() {
// Criar novos arrays
var novoSprites = [];
var novoProcessamentos = [];
// Adicionar somente se não constar no array de excluídos
for (var i in this.sprites) {
if (this.spritesExcluir.indexOf(this.sprites[i]) == -1)
novoSprites.push(this.sprites[i]);
}
for (var i in this.processamentos) {
if (this.processamentosExcluir.indexOf
(this.processamentos[i]) == -1)
novoProcessamentos.push(this.processamentos[i]);
150

## Página 158

CasadoCódigo Capítulo7. Criandoinimigos
}
// Limpar os arrays de exclusões
this.spritesExcluir = [];
this.processamentosExcluir = [];
// Substituir os arrays velhos pelos novos
this.sprites = novoSprites;
this.processamentos = novoProcessamentos;
}
Aexclusãoestáimplementada! Estapartefoifogo,nãofoi? Masagora
podemosfacilmentemandarexcluirobjetosqueestãosobrandonamemória,
paraqueelesnãoprovoquemmaislentidão!
7 .6 E xcluindo os objetos desnecessários
Vamoscomeçarpelo Tiro.Quandosumirdatela,eledeveserexcluído.Em
seumétodo atualizar,verificamossuaposiç ão yeotiramosdaanimaç ão
edocolisorquandosuaposiç ãofornegativa(excedendoabordadoCanvas):
atualizar: function() {
this.y -= this.velocidade;
// Excluir o tiro quando sumir da tela
if (this.y < -this.altura) {
this.animacao.excluirSprite(this);
this.colisor.excluirSprite(this);
}
},
O Ovnitambémdeveserexcluído,mascomoseumovimentoéemsen-
tidocontrário,eledevepassardaalturadoCanvas:
atualizar: function() {
this.y += this.velocidade;
if (this.y > this.context.canvas.height) {
this.animacao.excluirSprite(this);
151

## Página 159

7.6. Excluindoosobjetosdesnecessários CasadoCódigo
this.colisor.excluirSprite(this);
}
},
Também,tantoo Tiroquantoo Ovnidevemserexcluídosemcasode
colisãoentreeles. Afinal,estaéumaregradenegócioóbviadenossojogo!
Podemosimplementaristonométodo colidiuComdequalquerumadestas
classes.Escolhiaclasse Ovni,conferindoseooutroobjetoéum Tiro:
colidiuCom: function(outro) {
// Se colidiu com um Tiro, os dois desaparecem
if (outro instanceof Tiro) {
this.animacao.excluirSprite(this);
this.colisor.excluirSprite(this);
this.animacao.excluirSprite(outro);
this.colisor.excluirSprite(outro);
}
}
Porúltimo,acolisãoentrea Naveeo Ovni. Nossoherói,queerain-
vencível,agorapodemorrer!Programenaclasse Nave:
colidiuCom: function(outro) {
// Se colidiu com um Ovni...
if (outro instanceof Ovni) {
// Fim de jogo!
this.animacao.desligar();
alert('GAME OVER ');
}
}
Esteéummomentoparasecomemorar!Sevocêfeztodasastarefasaté
aquicomcalmaeaten ção,vocêtemagoraumgameenginemaduroparauso
eumexemplodejogototalmentefuncional,emboraaindanãoestejapronto.
Experimentejogar. Jáépossíveldestruirosinimigoseseratingidopor
eles. Nopróximocapítulo,realizaremosesteeoutrosdiversosajustesque
deixarãonossojogocomaspectoprofisisonal.
Exercício: tentefazeranavesofrer3colisõesantesdeserdestruída.Para
isso,bastacriarumatributo(sugestõesdenome: energia, pontosVida)
152

## Página 160

CasadoCódigo Capítulo7. Criandoinimigos
eirdecrementandoseuvaloracadacolisão.Quandochegarazero... GAME
OVER!
153

## Página 162

Capítulo8
Incorporeanimações,sons,
pausaevidasextrasaojogo
Umaboanotícia:nestecapítulo,nossojogodenaveseráconcluído!Játemos
umprotótipototalmentefuncional,masaindahámuitooquesermelhorado
paradar-lheumaspectoprofissional.Serãofeitasasseguintesmelhorias:
•Organização do código: nossojogoestácrescendoe, porisso, a
páginainicialvaicome çaraficarumpoucolongaedesorganizada.
Faremosalgumasrefatoraçõesparaacomodarmaisfacilmenteasmu-
dançasqueestãoporvir.
•Animação cronometrada: paraaanimaçãocorreravelocidadescon-
stantes,enãonoritmodaCPU(dojeitoqueestá,avelocidadedaani-
maçãopoderáoscilarmuito).

## Página 163

8.1. Organizandoocódigo CasadoCódigo
•Uso de spritesheets:nósaprendemoscomousá-lasnocapítulo 4,mas
nãoaplicamosaindaemnossojogo! Comelas,criaremosexplosões
edaremosanimaç ãoànave,deixandonossojogomuitomaisinteres-
sante.
•Pausa: comoseriaaexperiênciadejogarumjogosempoderpausá-lo?
Péssima,nãoémesmo?
•Som e música de fundo:vocênãoestavasentindoafaltadisto,não?
•T elas de loading e Game Over: umjogoutilizamuitasimagens.
Quandovocêhospedá-lonainternet,nãovaiquererqueousuárioveja
umatelaparadaenquantoasimagenscarregam,nãoéverdade? Um
aviso“Carregando...” eumabarrinhaaumentandonatelafarãocom
queointernautanãodesistadoseujogo;aocontrário,aumentarásua
expectativa!Eumatelaqueindicaquandoojogoacabou,cairámuito
bem.
•Vidas extras: porqueojogotemqueacabarnaprimeiracolisãoda
nave?Vamosdarmaischancesaojogador!
•Pontuação (score): estasimplesregradenegócioserábemfácilde
implementar.
Primeiro,vamosorganizartodoonossotrabalho. Seráumaexcelente
oportunidadederevisão.Mãosàobra!
8.1 O rganizando o código
Nocapítuloanterior, ocódigodapáginaHTMLdenossojogoficouum
tantoextenso,poisjuntamosquasetudooqueaprendemosemumúnicoar-
quivofuncional.Consideroestaumaboahorapararefatoraressecódigo(e
praticarumpoucotambém),deixando-oumpoucomaisorganizadoefácil
paraacrescentarasmelhoriasqueestãoporvir.
CrieumanovapáginaHTML.Osarquivosdescriptdevemsercopiados
desuasversõesmaisatualizadas.
156

## Página 164

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
<!-- arquivo: jogo-definitivo.html -->
<!DOCTYPE html>
<html>
<head>
<title>Jogo de Nave</title>
<script src="animacao.js"></script>
<script src="teclado.js"></script>
<script src="colisor.js"></script>
<script src="fundo.js"></script>
<script src="nave.js"></script>
<script src="ovni.js"></script>
<script src="tiro.js"></script>
</head>
<body>
<canvas id="canvas_animacao" width="500" height="500">
</canvas>
<script>
// Vamos organizar um pouco este aplicativo!
</script>
</body>
</html>
Vamoscontinuarexecutandoastarefasnestaordem:carregarasimagens,
iniciarosobjetos,iniciaraanimaç ão. Quetalcriarfun çõesseparadas? No
JavaScript,faça:
// Canvas e Context
var canvas = document .getElementById('canvas_animacao');
var context = canvas.getContext('2d');
// Variáveis principais
var imagens, animacao, teclado, colisor,
nave, criadorInimigos;
var totalImagens = 0, carregadas = 0;
// Começa carregando as imagens
157

## Página 165

8.1. Organizandoocódigo CasadoCódigo
carregarImagens();
Nafun ção carregarImagens,facilitamuitocarregarumobjetoouar-
raycomosnomesdasimagensefazerumloopnele.Opteiporusarumob-
jeto,poisassimpossoassociarcadaimagemaseunome(emvezdeusarum
númerosemsignificado).Apóscarregarcadaimagem,onomeésubstituído
peloobjetodaimagem:
function carregarImagens() {
// Objeto contendo os nomes das imagens
imagens = {
espaco: 'fundo-espaco.png',
estrelas: 'fundo-estrelas.png',
nuvens: 'fundo-nuvens.png',
nave: 'nave.png',
ovni: 'ovni.png'
};
// Carregar todas
for (var i in imagens) {
var img = new Image();
img.src = 'img/' + imagens[i];
img.onload = carregando;
totalImagens++;
// Substituir o nome pela imagem
imagens[i] = img;
}
}
Temosentãoquecriarajáconhecidafun ção carregando,quevaimoni-
torarocarregamentodasimagenseiniciaracriaç ãodosobjetosquandotodas
estiveremprontas:
function carregando() {
carregadas++;
if (carregadas == totalImagens) iniciarObjetos();
}
158

## Página 166

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
Afun ção iniciarObjetosiniciaráosprincipaisobjetosdojogo,da
formacomovocêjáestáacostumadoafazer:
function iniciarObjetos() {
// Objetos principais
animacao = new Animacao(context);
teclado = new Teclado(document);
colisor = new Colisor();
espaco = new Fundo(context, imagens.espaco);
estrelas = new Fundo(context, imagens.estrelas);
nuvens = new Fundo(context, imagens.nuvens);
nave = new Nave(context, teclado, imagens.nave);
// Ligações entre objetos
animacao.novoSprite(espaco);
animacao.novoSprite(estrelas);
animacao.novoSprite(nuvens);
animacao.novoSprite(nave);
colisor.novoSprite(nave);
animacao.novoProcessamento(colisor);
configuracoesIniciais();
}
Foichamadaafun ção configuracoesIniciais,queconfiguraas
velocidades dos fundos, posiciona a nave, configura o disparo pela tecla
Espaçoeiniciaaanimaç ão:
function configuracoesIniciais() {
// Fundos
espaco.velocidade = 3;
estrelas.velocidade = 5;
nuvens.velocidade = 10;
// Nave
nave.x = canvas.width / 2 - imagens.nave.width / 2;
nave.y = canvas.height - imagens.nave.height;
nave.velocidade = 5;
159

## Página 167

8.1. Organizandoocódigo CasadoCódigo
// Tiro
teclado.disparou(ESPACO, function() {
nave.atirar();
});
animacao.ligar();
}
Façaoteste:nestepontovocêjádeveteranavecontroláveleatirando,eo
fundorolando.Vamosagoraconfiguraracriaç ãodosinimigoscomoumpro-
cessamentodaanimaç ão. Aofinaldafun ção configuracoesIniciais,
acrescenteachamadaa criacaoInimigos:
function configuracoesIniciais() {
// ...
criacaoInimigos();
}
Evamoscriaressafun ção. Elacriaumobjetosemconstrutor,como
métodoprocessar,eoinserecomoumprocessamentogeralnaanimaç ão:
function criacaoInimigos() {
criadorInimigos = {
processar: function() {
}
};
animacao.novoProcessamento(criadorInimigos);
}
Nométodo processardesseobjeto,criaremosuminimigoacadase-
gundo.Mas,paraisso,necessitamossaberoinstanteemqueoúltimoinimigo
foigerado.Esteinstanteéguardadonoatributo ultimoOvnieatualizado
quandootempodecorridoultrapassar1000milissegundos:
function criacaoInimigos() {
var criador = {
160

## Página 168

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
ultimoOvni: new Date().getTime(),
processar: function() {
var agora = new Date().getTime();
var decorrido = agora - this .ultimoOvni;
if (decorrido > 1000) {
novoOvni();
this.ultimoOvni = agora;
}
}
};
animacao.novoProcessamento(criador);
}
Sepassarumsegundodesdeageraç ãodoúltimoinimigo,échamadaa
função novoOvni,queémuitosemelhanteàdocapítuloanterior.Elagera
inimigosemposiçõesecomvelocidadesaleatórias.Senãolembracomofazer
isso,consulteotópico 7.1.
function novoOvni() {
var imgOvni = imagens.ovni;
var ovni = new Ovni(context, imgOvni);
// Mínimo: 5; máximo: 20
ovni.velocidade =
Math.floor( 5 + Math.random() * (20 - 5 + 1 ) );
// Mínimo: 0;
// máximo: largura do canvas - largura do ovni
ovni.x =
Math.floor( Math.random() *
(canvas.width - imgOvni.width + 1) );
// Descontar a altura
ovni.y = -imgOvni.height;
animacao.novoSprite(ovni);
161

## Página 169

8.2. Animaçãocronometrada CasadoCódigo
colisor.novoSprite(ovni);
}
Agoraestamosmuitomaisorganizados,comcadaetapadainicializaç ão
dojogoemumafun çãoespecífica. Estamosprontosparaimplementaras
novidades.
8.2 A nimação cronometrada
Paradarumaspectomaisprofissionalanossojogo,devemoscronometrar
asanimações.Vocêpodeternotadoque,àsvezes,avelocidadeoscila.Istoé
comumembrowsersejogosquerodamemsistemasoperacionaismultitarefa:
aCPUpodeestarocupadaenquantoojogoesperaomomentodeprocessar
opróximociclo.
Pararesolverisso,precisamosprimeirosaberotempodecorridoentre
umcicloeoutro. Noconstrutordaclasse Animacao, crieosatributos
ultimoCiclo(paraguardaroinstantedocicloanterior,lidodorelógio)e
decorrido(paraguardarotempodecorridoentreocicloanterioreoatual):
function Animacao(context) {
// ...
this.ultimoCiclo = 0;
this.decorrido = 0;
}
Parafazeroscálculos,obtemosoinstanteatualdorelógiodocomputador
(dadopor Date.getTime()emmilissegundos)ecalculamosadiferen ça
entreesseinstanteeoinstantedocicloanterior. Faremosissonométodo
proximoFrame,logoantesdeprocessarossprites:
proximoFrame: function() {
// Posso continuar?
if ( ! this.ligado ) return;
var agora = new Date().getTime();
if (this.ultimoCiclo == 0) this.ultimoCiclo = agora;
this.decorrido = agora - this.ultimoCiclo;
162

## Página 170

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
// ...
}
Nofimdométodo proximoFrame,atualizeoatributo ultimoCiclo,
imediatamenteantesdechamaropróximociclo:
proximoFrame: function() {
// ...
// Atualizar o instante do último ciclo
this.ultimoCiclo = agora;
// Chamamos o próximo ciclo
var animacao = this;
requestAnimationFrame(function() {
animacao.proximoFrame();
});
},
Agoraosspritessabemquantotempolevouentreumcicloeoutro!Vamos
fazero Fundomover-seaumavelocidadeconstante.Paraisso,modifiqueo
métodoatualizar:
atualizar: function() {
// Atualizar a posição de emenda
this.posicaoEmenda +=
this.velocidade * this.animacao.decorrido / 1000;
// ...
},
163

## Página 171

8.2. Animaçãocronometrada CasadoCódigo
Fórmula para animação cronometrada
Oincrementodaposiç ãodosprite,empixels,édadopelafórmula:
velocidade * tempoDecorrido / 1000
Sendo:
•velocidadeempixelsporsegundo;
•tempoDecorrido em segundos (como o tempo dado por
Date.getTime()éemmilissegundos,dividimosessevalorpor
1000).
Note que agora o fundo move-se em velocidade constante, porém
bem devagar, pois passamos a trabalhar com pixels por segundo.
Podemos ajustar novas velocidades com valores maiores na função
configuracoesIniciaisdapáginaHTML.Vocêpodefazerváriostestes
e atribuir os valores que desejar, dependendo da sensação de velocidade
quequerpassar. Comoasnuvensestãomaispróximas,deiaelasamaior
velocidade,masnadaimpedequecoloquemosasestrelasemprimeiroplano,
porexemplo:
function configuracoesIniciais() {
// Fundos
espaco.velocidade = 60;
estrelas.velocidade = 150;
nuvens.velocidade = 500;
// ...
}
Vamoscronometrartambémomovimentoda Nave.Apliqueafórmula
emseumétodo atualizar:
atualizar: function() {
var incremento =
164

## Página 172

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
this.velocidade * this.animacao.decorrido / 1000;
// Use a variável incremento em todas as mudanças de x e y
if (this.teclado.pressionada(SETA_ESQUERDA) && this.x > 0)
this.x -= incremento;
// ...
}
NapáginaHTML,deiaelaavelocidadede200pixelsporsegundo:
// Nave
nave.x = canvas.width / 2 - imagens.nave.width / 2;
nave.y = canvas.height - imagens.nave.height;
nave.velocidade = 200;
Exercício:façavocêmesmooajusteparao Ovnieo Tiro!Dê-lhesas
velocidadesquedesejar. Ado Tiroéconfiguradanoconstrutor,easdos
Ovnis,nométodo novoOvnidapágina. Dica: nopacotededownload,a
páginajáestácomasoluçãoimplementada.
8.3 A nimando a nave com spritesheets
Nopacotededownloaddolivroháoarquivo nave-spritesheet.png
(figura8.1).Iremosusá-loparamelhoraroaspectodenossanave.Conven-
hamos,elaestámuitoparada...nemofogoemsuacaudasemexe!
165

## Página 173

8.3. Animandoanavecomspritesheets CasadoCódigo
Figura8.1:Spritesheetparaanave
Nocapítulo4,definimosqueaslinhasdaspritesheetrepresentamdifer-
entesestadosdosprite. Aquitemosanaveparada,movendo-separaaes-
querda emovendo-se para adireita. Em umalinha, a animação ocorre
avançandoascolunas.Emcadaumadestaslinhas,háduascolunasqueani-
mamofogonacauda.
Iniciando o teste
Paracome çaraprogramarcomspritesheets,primeiroacrescentearefer-
ênciaaoarquivo spritesheet.js,criadonocapítulo 4:
<script src="spritesheet.js"></script>
Nafun ção carregarImagens,mudeaimagemdanaveparaoarquivo
nave-spritesheet.png:
imagens = {
// ...
nave: 'nave-spritesheet.png',
// ...
};
Agoranãopodemosmaisusarasdimensõesdaimagemparaposicionar
anave.Em configuracoesIniciais,vamospassarvaloresabsolutosref-
erentesacadaquadro(considerandoquecadanavetem36x48pixels):
166

## Página 174

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
function configuracoesIniciais() {
// ...
// Nave
nave.x = canvas.width / 2 - 18; // 36 / 2
nave.y = canvas.height - 48;
nave.velocidade = 5;
// ...
}
Noconstrutordaclasse Nave,vamosiniciaroobjetoquecontrolaa
spritesheet.Usaremosinicialmentealinhazero,querepresentaanaveparada.
Ointervaloentreumquadroeoutropodeserajustadoaospoucosconforme
oseugosto:
function Nave(context, teclado, imagem) {
// ...
this.spritesheet = new Spritesheet(context, imagem, 3, 2);
this.spritesheet.linha = 0;
this.spritesheet.intervalo = 100;
}
Altereagoraométodo desenharparausaraspritesheet. Paradefinir
qualalinhaaseranimada,lemosoestadodassetasdoteclado:
desenhar: function() {
if (this.teclado.pressionada(SETA_ESQUERDA))
this.spritesheet.linha = 1;
else if (this.teclado.pressionada(SETA_DIREITA))
this.spritesheet.linha = 2;
else
this.spritesheet.linha = 0;
this.spritesheet.desenhar(this.x, this.y);
this.spritesheet.proximoQuadro();
},
Tambémprecisamosalterarométodo atualizar, poiseletambém
estáusandoasdimensõesdaimagemparanãodeixá-lapassardaborda
167

## Página 175

8.3. Animandoanavecomspritesheets CasadoCódigo
do Canvas. Nós substituímos as referências athis.imagem.widthe
this.imagem.heightpelosvaloresabsolutos36e48,respectivamente:
atualizar: function() {
// ...
if (this.teclado.pressionada(SETA_DIREITA) &&
this.x < this.context.canvas.width - 36)
this.x += this.velocidade;
// ...
if (this.teclado.pressionada(SETA_ABAIXO) &&
this.y < this.context.canvas.height - 48)
this.y += this.velocidade;
},
Porúltimo,percebaqueotirosaiumpoucodeslocado,poissuaposiç ão
écalculadapelotamanhodaimagemantiga. Vamosajustarparaumvalor
absoluto,noconstrutordaclasse Tiro.Tambémaproveiteiomomentopara
mudaracoredeixá-loumpoucomenor:
function Tiro(context, nave) {
this.context = context;
this.nave = nave;
// Posicionar o tiro no bico da nave
this.largura = 3;
this.altura = 10;
this.x = nave.x + 18; // 36 / 2
this.y = nave.y - this.altura;
this.velocidade = 10;
this.cor = 'yellow';
}
Experimentejogarepercebaqueomovimentodanaveganhoumaisdi-
namismo!
168

## Página 176

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
8.4 C riando explosões
Vamosaproveitaroembalodasspritesheetsecriarexplosões. Usaremoso
arquivo explosao.png,quecontémaspritesheetnafigura 8.2:
Figura8.2:Spritesheetparaexplosão
Também será preciso acrescentar uma referência ao script
explosao.js,asercriadologomais:
<script src="explosao.js"></script>
Nafun ção carregarImagens,acrescenteaimagemdaexplosão:
imagens = {
// ...
ovni: 'ovni.png', // uma vírgula aqui
explosao: 'explosao.png'
};
Nométodo colidiuComdaclasse Ovni,ondeesteédestruídopelo
Tiro,vamoscriarumaexplosão:
colidiuCom: function(outro) {
// Se colidiu com um Tiro, os dois desaparecem
if (outro instanceof Tiro) {
// ...
var explosao = new Explosao(this.context,
this.imgExplosao, this.x, this.y);
this.animacao.novoSprite(explosao);
}
}
169

## Página 177

8.4. Criandoexplosões CasadoCódigo
Osobjetosqueexplodemprecisamreceberaimagemdaexplosão,para
podercriarossprites.Mudeoconstrutordo Ovni:
function Ovni(context, imagem, imgExplosao) {
// ...
this.imgExplosao = imgExplosao;
}
Epasseaimagemnafun ção novoOvnidapáginaHTML:
var ovni = new Ovni(context, imgOvni, imagens.explosao);
Agora,crieaclasse Explosaonoarquivo explosao.js:
function Explosao(context, imagem, x, y) {
this.context = context;
this.imagem = imagem;
this.spritesheet = new Spritesheet(context, imagem, 1, 5);
this.spritesheet.intervalo = 75;
this.x = x;
this.y = y;
}
Explosao.prototype = {
atualizar: function() {
},
desenhar: function() {
}
}
Nométodo desenhar,nósdesenhamosoquadroatualeanimamosa
spritesheet:
desenhar: function() {
this.spritesheet.desenhar(this.x, this.y);
this.spritesheet.proximoQuadro();
}
Masassimaexplosãoficarápiscandonatelaeternamente! Oquequer-
emoséque,quandotodososquadrosforemexibidos,aexplosãotermine.
170

## Página 178

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
Mascomosaberseaspritesheetchegouaoúltimoquadro? Vamoscriar
nelaumafuncionalidadecomaqualelaprópriaavisaisto. Noconstrutor
da Explosao,crieumcallbackquerecebeesseaviso:
function Explosao(context, imagem, x, y) {
// ...
var explosao = this;
this.spritesheet.fimDoCiclo = function() {
explosao.animacao.excluirSprite(explosao);
}
}
Agoracrieoatributo fimDoCiclonoconstrutorda Spritesheet:
function Spritesheet(context, imagem, linhas, colunas) {
// ...
this.fimDoCiclo = null;
}
Emodifiqueométodo proximoQuadro()parachamaressecallback
quandovoltaraoquadrozero:
proximoQuadro: function() {
// ...
if (this.coluna < this.numColunas - 1) {
this.coluna ++;
}
else {
this.coluna = 0;
// Avisar que acabou um ciclo!
if (this.fimDoCiclo) this.fimDoCiclo();
}
// ...
},
Experimentejogar!O Ovnijáexplodeaoseratingidopelotiro.Agora
vamosexplodirtantoa Navequantoo Ovniquandoelescolidirem. No
métodocolidiuComda Nave,vamoscriarduasexplosões:
171

## Página 179

8.4. Criandoexplosões CasadoCódigo
colidiuCom: function(outro) {
// Se colidiu com um Ovni...
if (outro instanceof Ovni) {
this.animacao.excluirSprite(this);
this.animacao.excluirSprite(outro);
this.colisor.excluirSprite(this);
this.colisor.excluirSprite(outro);
var exp1 = new Explosao( this.context, this.imgExplosao,
this.x, this.y);
var exp2 = new Explosao( this.context, this.imgExplosao,
outro.x, outro.y);
this.animacao.novoSprite(exp1);
this.animacao.novoSprite(exp2);
// Por enquanto tire o término da animação
}
}
Claro,a Navetambémprecisaráreceberaimagemdaexplosãonocon-
strutor:
function Nave(context, teclado, imagem, imgExplosao) {
// ...
this.imgExplosao = imgExplosao;
}
Portanto,passe-aaocriaranave(método iniciarObjetosdapágina
HTML):
nave = new Nave(context, teclado, imagens.nave,
imagens.explosao);
A Naveeo Ovnijáexplodemjuntos. Gostaríamosdepararaani-
maçãoedaramensagem“GAMEOVER”somentequandoessasexplosões
finalizarem.Portanto,osprite Explosaotambémpoderiareceberumcall-
back.Completeo colidiuComda Naveparapassaressecallback:
172

## Página 180

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
colidiuCom: function(outro) {
// Se colidiu com um Ovni...
if (outro instanceof Ovni) {
// ...
exp1.fimDaExplosao = function() {
animacao.desligar();
alert('GAME OVER ');
}
}
}
Emodifiqueoconstrutorda Explosaoparachamaressecallbackaofim
dociclodaspritesheet:
function Explosao(context, imagem, x, y) {
// ...
var explosao = this;
this.fimDaExplosao = null;
this.spritesheet.fimDoCiclo = function() {
explosao.animacao.excluirSprite(explosao);
if (explosao.fimDaExplosao) explosao.fimDaExplosao();
}
}
Nãoélegal?A Spritesheetinformaà Explosaoquandocompletou
aanimaçãodosquadros,ea Explosaoseretiradaanimaç ãoenotificaa
queminteressar.
Brinqueumpouco,achoquevocêmerece!
173

## Página 181

8.4. Criandoexplosões CasadoCódigo
Figura8.3:Agoraascolisõestêmemo ção!
174

## Página 182

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
8.5 P ausando o jogo
Figura8.4:Jogopausadocomindicativonatela
Nósjátemospausaimplementadaemnossogameengine:osmétodos ligar
e desligardaclasse Animacao.Noentanto,éprecisotrataralgunsacon-
tecimentosqueestãoocorrendonaanimaç ão,aosepausarojogo.
Vamosdefinirqueojogadorpausaráojogoatravésdatecla Enter,cujo
códigoé13(sepreferirusaroutratecla,fiqueàvontade).
Noiníciodoarquivo teclado.js,acrescenteumavariávelparaguardar
ocódigodo Enter:
// Códigos de teclas - aqui vão todos os que forem necessários
var SETA_ESQUERDA = 37;
var SETA_ACIMA = 38;
var SETA_DIREITA = 39 ;
var SETA_ABAIXO = 40;
175

## Página 183

8.5. Pausandoojogo CasadoCódigo
var ESPACO = 32;
var ENTER = 13;
Agora,nométodo configuracoesIniciais,configureaaç ãodatecla
Enter:
// Pausa
teclado.disparou(ENTER, pausarJogo);
Ecrieafun ção pausarJogo,queéquemfaráotrabalho:
function pausarJogo() {
if (animacao.ligado)
animacao.desligar();
else
animacao.ligar();
}
Façaoteste:nestepontoojogojádevepausaredespausar.Noentanto,
vocêpoderánotaralgunsbugs.Primeiro,pauseenquantoumdiscovoador
estánatela,eemseguidadespause: elesome! Issoocorreporquesuaani-
maçãoestácronometrada,eotempodapausaestásendocontadoparacal-
cularseumovimento.Quandoaanimaç ãoreinicia,odiscojádeveestarlonge,
eassimojogooposiciona.
Pararesolverisso,naclasse Animacao,nométodo ligar,reinicieo
atributo ultimoCicloparazero.Istofaráacontagemdetemposerreinici-
ada:
ligar: function () {
this.ultimoCiclo = 0;
this.ligado = true;
this.proximoFrame();
},
Umoutroproblemaé: fun çõesdedisparo(nocaso,otiro)continuam
sendopossíveis! Istonãoocorrecomamovimentaç ãopelassetas,poissão
lidasnométodo atualizarda Nave,dentrodoloopdeanimaç ão(que
estariapausado).
Modifiquemosafun çãoparadesativaroureativaratecla Espaço(tiro)
conformepausamosedespausamosojogo:
176

## Página 184

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
function pausarJogo() {
if (animacao.ligado) {
animacao.desligar();
ativarTiro(false);
}
else {
animacao.ligar();
ativarTiro(true);
}
}
Afun ção ativarTirovaimodificaroseventosdoteclado,configu-
randoatecla Espaço:
function ativarTiro(ativar) {
if (ativar) {
teclado.disparou(ESPACO, function() {
nave.atirar();
});
}
else
teclado.disparou(ESPACO, null);
}
Para não ficarmos com código repetido, em
configuracoesIniciais,removaaslinhas:
// Remova estas linhas
// Tiro
teclado.disparou(ESPACO, function() {
nave.atirar();
});
Ecoloqueestanolugar:
// Tiro
ativarTiro( true);
Tambémocorrequeuminimigoégeradoimediatamenteapósadespausa,
poisestamosgerandouminimigoporsegundoeapausafazessetempose
177

## Página 185

8.5. Pausandoojogo CasadoCódigo
exceder.Antesdeligaraanimaç ão,reinicieomomentodageraç ãodoúltimo
inimigoparaoinstanteatual,paraevitarqueissoocorra:
function pausarJogo() {
// ...
else {
criadorInimigos.ultimoOvni = new Date().getTime();
animacao.ligar();
ativarTiro(true);
}
}
Quantosdetalhesumasimplespausanosobrigaatratar!Paraficarmais
interessante,vamosexibirotexto“Pausado”natela:
function pausarJogo() {
if (animacao.ligado) {
animacao.desligar();
ativarTiro(false);
// Escrever "Pausado"
context.save();
context.fillStyle = 'white';
context.strokeStyle = 'black';
context.font = '50px sans-serif';
context.fillText("Pausado", 160, 200);
context.strokeText("Pausado", 160 , 200);
context.restore();
}
else {
criadorInimigos.ultimoOvni = new Date().getTime();
animacao.ligar();
ativarTiro(true);
}
}
Usesuaimaginaç ão! Coloquequalquerimagem,texto,oucombinaç ão
dosdois.Podeatéinstanciaroutra Animacao,colocaralgunsspritesespecí-
ficoseexibiralgunsmovimentosduranteapausa.
178

## Página 186

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
8.6 S ons e música de fundo
Estaparteémuitofácildeimplementar.OHTML5,alémdoCanvas,possui
umaAPIdeáudiomuitosimples.Nopacotedearquivos,napastadestecapí-
tulo( 08),háumasubpastacomonome sndcontendoalgunsarquivosde
som,emformatoMP3.
Bancos de sons grátis e direitos autorais
Jamaisusesonsdeterceirossemadevidaautorizaç ão! Criadores
dejogosindependentes,semmeiosouconhecimentosparagerarseus
própriossons,podemcontarcominúmerosbancosdesonsgratuitoses-
palhadospelainternet.
Ossonsparaojogodestelivroforamobtidosem http://freesound.org.
Primeiro,vamosproduzirosomdostiros. Abraoarquivo tiro.jse
coloqueasinstruçõesparacarregarosomlogonoiníciodoarquivo.Instan-
ciamosumobjeto Audio(presentenaAPIdoHTML5),setamosseuatributo
srcparaoarquivo tiro.mp3(presentenopacotededownload)eajustamos
ovolumecomoumvalorentre0e1.Porúltimo,chamamosométodo load
parainiciarocarregamentodoarquivo,evitandoquesejacarregadosomente
nomomentodareproduç ão:
var SOM_TIRO = new Audio();
SOM_TIRO.src = 'snd/tiro.mp3 ';
SOM_TIRO.volume = 0.2;
SOM_TIRO.load();
Depois,vamosreproduziressesomcadavezqueumtiroécriado. No
construtor,rebobinamososomajustandooatributo currentTimepara
zero.Esseatributoindicaoinstanteatualdereproduç ão,dadoemsegundos.
Emseguida,bastachamarométodo play:
function Tiro(context, nave) {
// ...
179

## Página 187

8.6. Sonsemúsicadefundo CasadoCódigo
SOM_TIRO.currentTime = 0.0;
SOM_TIRO.play();
}
Ostirosjáfazembarulho!Vamosfazeromesmoprocedimentoparaas
explosões.Noiníciodoarquivo explosao.js,coloqueasinstruções:
var SOM_EXPLOSAO = new Audio();
SOM_EXPLOSAO.src = 'snd/explosao.mp3';
SOM_EXPLOSAO.volume = 0.4;
SOM_EXPLOSAO.load();
Enoconstrutor,manderebobinarereproduzir,damesmaformaquecom
o Tiro:
function Explosao(context, imagem, x, y) {
// ...
SOM_EXPLOSAO.currentTime = 0.0;
SOM_EXPLOSAO.play();
}
Vamostambémcolocarumamúsicadefundoparadarmaisemo çãoao
jogo.NoiníciodapáginaHTML,acrescenteavariável musicaAcao:
// Variáveis principais
var imagens, animacao, teclado, colisor, nave, criadorInimigos;
var totalImagens = 0, carregadas = 0;
var musicaAcao;
Emseguida,logoapósachamadapara carregarImagens,coloque
tambémumachamadapara carregarMusicas:
// Começa carregando as imagens e músicas
carregarImagens();
carregarMusicas();
Ecrieafun ção carregarMusicas.Aqui,setamosoatributo looppara
true,fazendocomqueamúsicarepitaincessantementeduranteaaç ãodo
jogo.
180

## Página 188

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
function carregarMusicas() {
musicaAcao = new Audio();
musicaAcao.src = 'snd/musica-acao.mp3';
musicaAcao.load();
musicaAcao.volume = 0.8;
musicaAcao.loop = true;
musicaAcao.play();
}
Viucomoébemfácil?Divirta-semaisumpouco!
Dica:vocêpodepararamúsicanomomentodapausausandoométodo
pause.
8.7 T ela de loading
Figura8.5:Indiqueparaojogadorqueojogoestácarregando
181

## Página 189

8.7. Teladeloading CasadoCódigo
Vamosmodificarafun ção carregandodapáginaHTMLparaincrementar
umabarraconformeasimagensvãosendocarregadas.Primeiro,comovamos
desenhar,guardeaconfiguraç ãoatualdocontexto(método save)ecrieum
fundo.Aqui,fizumfundosimples,comaimagemdoespaço.Setivervontade
façaumdesenhomaiselaborado.Sinta-selivre!
function carregando() {
context.save();
// Fundo
context.drawImage(imagens.espaco, 0, 0, canvas.width,
canvas.height);
// continua ...
}
Emseguida,vamoscriarotexto“Carregando":
function carregando() {
// ...
// Texto "Carregando"
context.fillStyle = 'white';
context.strokeStyle = 'black';
context.font = '50px sans-serif';
context.fillText("Carregando...", 100, 200);
context.strokeText("Carregando...", 100, 200);
// continua ...
}
Opróximopassoédesenharabarra.Nesteponto,precisamosincremen-
taravariável carregadas,parapodercalcularalarguraatualdabarra:
function carregando() {
// ...
// Barra de loading
carregadas ++;
182

## Página 190

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
var tamanhoTotal = 300;
var tamanho = carregadas / totalImagens * tamanhoTotal;
context.fillStyle = 'yellow';
context.fillRect(100, 250, tamanho, 50);
// continua ...
}
Porúltimo,restauramosasconfiguraçõesanterioresdocontexto(método
restore)e,emvezdeiniciarojogoimediatamente,vamosmostrarumlink
“Jogar”,asercriadologoadiante,paraojogadorclicarquandoestiverpronto:
function carregando() {
// ...
context.restore();
if (carregadas == totalImagens) {
iniciarObjetos();
mostrarLinkJogar();
}
}
Comoojogonãovaiiniciarautomaticamente,tireocomandoqueinicia
aanimaçãodafun ção configuracoesIniciais:
// Remova esta linha
animacao.ligar();
Etambémachamadaaométodo playdafun ção carregarMusicas:
// Remova esta linha
musicaAcao.play();
Crieentãoumlinkparainiciarojogo.Logoapósatag <canvas>,insira
esselink,comumachamadaparaafun ção iniciarJogo:
<a id="link_jogar" href="javascript: iniciarJogo()">Jogar</a>
183

## Página 191

8.7. Teladeloading CasadoCódigo
VamosconfigurarsuaaparênciaeposiçãoviaCSS.Vocêpodeconfigurar
essebotãodaformaquequiser,enãoéofocodestelivroficardetalhando
formataçõesemCSS.Casonãotenhamuitaprática,aíestáumaformataç ão
sugerida. Nopacotededownloads,existeaimagem botao-jogar.png,
queuseicomofundo.
Nase ção <head>dodocumento(podeserapósosscripts),crieumatag
<style>.Omaisimportanteéqueobotãoinicieocultoetenhaposiciona-
mentoabsoluto,parapodermoscolocá-loporcimadoCanvas:
<style>
#link_jogar {
/* Inicia oculto */
display: none;
/* Cores e fundo */
color: yellow;
background: url(img/botao-jogar.png);
/* Fonte */
font-size: 20px;
font-family : sans-serif;
/* Sem sublinhado e com sombra */
text-decoration: none;
text-shadow : 2px 2px 5px black;
/* Posicionamento */
position: absolute;
left: 220px;
top: 330px;
/* A imagem do botão é 72x72, descontamos os paddings */
width: 52px;
height: 26px;
padding: 23px 10px ;
}
</style>
184

## Página 192

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
Ecrieafun ção mostrarLinkJogar,quemandarámostraresselink,
modificandoseuatributoCSS displayparaovalor block.
function mostrarLinkJogar() {
document.getElementById( 'link_jogar').style.display =
'block';
}
Afun ção iniciarJogo,chamadapelolink,iráesconderolink“Jogar”,
iniciaramúsicaeligaraanimaç ão:
function iniciarJogo() {
document.getElementById( 'link_jogar').style.display =
'none';
musicaAcao.play();
animacao.ligar();
}
Façaoteste! Enquantovocêestivertestandoojogoemseucomputa-
dor,atelacarregarábemrapidamente.Noentanto,elafará(muita)diferen ça
quandohospedarmosnossojogonaweb.
Aindatemosumproblema: atecla Enterdáinícioaojogosemfazer
sumirobotãoJogar!Issoocorreporqueelaestádespausandoojogoemum
momentoemqueaanimaç ãonãoestárodando.
Para corrigir isso, vamos tirar as seguintes linhas de
configuracoesIniciais:
// Remova estas linhas
// Tiro
ativarTiro( true);
// E estas também
// Pausa
teclado.disparou(ENTER, pausarJogo);
Vamosativá-lasem iniciarJogo:
function iniciarJogo() {
// Tiro
185

## Página 193

8.8. Vidasextras CasadoCódigo
ativarTiro(true);
// Pausa
teclado.disparou(ENTER, pausarJogo);
// ...
}
8.8 V idas extras
Figura8.6:Dêmaischancesaojogadorcomvidasextras!
Programarvidasextrasnãoétãocomplicado,tudoéquestãodemexernos
algoritmosdanave.Parafacilitar,vamoscriarumatributodecallbackonde
a Navenosinformaquandoacabaramasvidas.Noconstrutor,crieessecall-
backeoatributo vidasExtras:
function Nave(context, teclado, imagem, imgExplosao) {
// ...
this.acabaramVidas = null;
this.vidasExtras = 3;
}
Nométodo colidiuCom,ondedetectamossuacolisãomortal,retireas
linhasquemandamfinalizarojogo:
// Retire estas linhas:
exp1.fimDaExplosao = function() {
animacao.desligar();
alert('GAME OVER ');
}
Esubstitua-aspelocódigoaseguir. Nósvamosdecrementaroatributo
vidasExtras,everificarseasvidasacabaram(enotificar,seforocaso).
186

## Página 194

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
Casoojogocontinue,nósrecolocamosanavenaanimaç ãoenocolisorea
reposicionamos:
var nave = this;
exp1.fimDaExplosao = function() {
nave.vidasExtras--;
if (nave.vidasExtras < 0) {
if (nave.acabaramVidas) nave.acabaramVidas();
}
else {
// Recolocar a nave no engine
nave.colisor.novoSprite(nave);
nave.animacao.novoSprite(nave);
nave.posicionar();
}
}
Oposicionamentodanaveéexatamenteoquejáestamosfazendona
função configuracoesIniciaisdapáginaHTML.Retireaslinhas:
// Nave
// Retire as duas linhas abaixo
nave.x = canvas.width / 2 - 18; // 36 / 2
nave.y = canvas.height - 48;
Ecoloquenolugarumachamadaaométodo posicionar:
// Nave
nave.posicionar();
nave.velocidade = 200;
Vamoscriarométodona Nave,fazendoessamesmatarefa:
posicionar: function() {
var canvas = this.context.canvas;
this.x = canvas.width / 2 - 18; // 36 / 2
this.y = canvas.height - 48;
}
187

## Página 195

8.8. Vidasextras CasadoCódigo
Porfim,em configuracoesIniciais,insiraaslinhasquefinalizam
ojogo,respondendoaocallback acabaramVidasda Nave:
function configuracoesIniciais() {
// ...
// Game Over
nave.acabaramVidas = function() {
animacao.desligar();
alert('GAME OVER ');
}
}
Exercício:implemente,atravésdaleituradoteclado,um cheat codeque
dêmaisvidasaojogador!
Um mostrador de vidas
Legal, nossa nave já tem vidas extras! Vamos criar agora o arquivo
painel.js,paramostraressasvidasextras.Seuesqueletofica:
// arquivo: painel.js
function Painel(context, nave) {
this.context = context;
this.nave = nave;
}
Painel.prototype = {
atualizar: function() {
},
desenhar: function() {
}
}
Claro,insiraoscriptnase ção <head>:
<script src="painel.js"></script>
Nafun ção iniciarObjetos, crieopaineleinsira-onaanima ção.
Opteipordeixaranaveporúltimo,paraqueelasemprefiqueacimadopainel:
188

## Página 196

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
function iniciarObjetos() {
// Objetos principais
// ...
painel = new Painel(context, nave);
// Ligações entre objetos
// ...
animacao.novoSprite(painel);
animacao.novoSprite(nave);
// ...
}
Noconstrutordo Painel,vamoscriarumaspritesheetapartirdaim-
agemdanave.Nósusaremossomenteaprimeiraimagem,quecorresponde
ànaveparada:
function Painel(context, nave) {
// ...
this.spritesheet =
new Spritesheet(context, nave.imagem, 3, 2);
this.spritesheet.linha = 0;
this.spritesheet.coluna = 0;
}
Nométododesenhar,obtemosonúmerodevidasextrasedesenhamos
aimagemessenúmerodevezes:
desenhar: function() {
var x = 20;
var y = 20;
for (var i = 1; i <= this.nave.vidasExtras; i++) {
this.spritesheet.desenhar(x, y);
x += 40;
}
}
Euacheiqueosdesenhosdasvidasestãomuitograndes.Vouusaraquio
métodoscaledo contextparadesenhá-loscommetadedotamanho:
189

## Página 197

8.9. Pontuação(score) CasadoCódigo
desenhar: function() {
// Reduz o desenho pela metade
this.context.scale(0.5, 0.5);
var x = 20;
var y = 20;
for (var i = 1; i <= this.nave.vidasExtras; i++) {
this.spritesheet.desenhar(x, y);
x += 40;
}
// Torna a dobrar
this.context.scale(2, 2);
}
Vocêpodeusarotamanhoquepreferir,oumesmousarumarquivode
imagemapenasparaisso,emtamanhomenor. Mascomo scaleébem
maiseconômico,nãoacha?
8.9 P ontuação (score)
Aproveitandoquetemosumpainelmostradordevidas,podemoscriarnele
umatributo pontuacao.Emsuafun çãoconstrutora,coloqueainstruç ão:
this.pontuacao = 0 ;
Em configuracoesIniciais,vamoscriarumtratadorgeraldecol-
isõesqueverificaseéum Tiroeum Ovniqueestãocolidindo. Emcaso
positivo,incrementamosessapontuaç ãonopainel:
function configuracoesIniciais() {
// ...
// Pontuação
colisor.aoColidir = function(o1, o2) {
// Tiro com Ovni
if ( (o1 instanceof Tiro && o2 instanceof Ovni) ||
(o1 instanceof Ovni && o2 instanceof Tiro) )
190

## Página 198

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
painel.pontuacao += 10;
// Use o incremento que desejar
}
}
Agora,modifiqueométodo desenhardopainelparaescreverapontu-
açãoaoladodosíconesdasvidas:
desenhar: function() {
// ...
// Para facilitar um pouco...
var ctx = this.context;
// Pontuação
ctx.save();
ctx.fillStyle = 'white';
ctx.font = '18px sans-serif ';
ctx.fillText(this.pontuacao, 100, 27);
ctx.restore();
}
Porúltimo,nãoseesque çadezeraropainelcadavezqueojogoinicia,
docontrárioapontuaçãoficaláparaapróximapartida.Em iniciarJogo,
coloqueocomando:
painel.pontuacao = 0;
191

## Página 199

8.10. TeladeGameOver CasadoCódigo
8.10 T ela deGame Over
Figura8.7:Quepena...fimdejogo!
Vamos finalizar nosso jogo criando uma tela de Game Over! Em
configuracoesIniciais, tireaquelealertahorríveletroqueporuma
chamadaàfun ção gameOver:
function configuracoesIniciais() {
// ...
// Game Over
nave.acabaramVidas = function() {
animacao.desligar();
gameOver();
}
}
Nessafun ção,vamosdesativarasteclasdedisparo,pararamúsicaecriar
umatelamaisadequada.Olink“Jogar”devevoltaraaparecer,eanavedeve
192

## Página 200

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
serrecolocadanogameengine(poisfoitiradanomomentodacolisão):
function gameOver() {
// Tiro
ativarTiro(false);
// Pausa
teclado.disparou(ENTER, null);
// Parar a música e rebobinar
musicaAcao.pause();
musicaAcao.currentTime = 0.0;
// Fundo
context.drawImage(imagens.espaco, 0, 0, canvas.width,
canvas.height);
// Texto "Game Over"
context.save();
context.fillStyle = 'white';
context.strokeStyle = 'black';
context.font = '70px sans-serif';
context.fillText("GAME OVER", 40, 200);
context.strokeText("GAME OVER", 40, 200);
context.restore();
// Volta o link "Jogar"
mostrarLinkJogar();
// Restaurar as condições da nave
nave.vidasExtras = 3;
nave.posicionar();
animacao.novoSprite(nave);
colisor.novoSprite(nave);
}
Vocêperceberáumacoisa:Ovnisquesobraramnaanimaç ão,continuam
láparaopróximojogo! Aofimde gameOver,chameumanovafun ção,
removerInimigos:
193

## Página 201

8.10. TeladeGameOver CasadoCódigo
function gameOver() {
// ...
removerInimigos();
}
Nestafun ção,nósmandamosexcluirtodosos Ovnisdaanimaç ão:
function removerInimigos() {
for (var i in animacao.sprites) {
if (animacao.sprites[i] instanceof Ovni)
animacao.excluirSprite(animacao.sprites[i]);
}
}
Finalmente, reinicie o instante da geraç ão de inimigos em
iniciarJogo, para que não surja umOvni de repente quando o
jogoforreiniciado.Faç aistoantesdeligaraanimaç ão:
function iniciarJogo() {
criadorInimigos.ultimoOvni = new Date().getTime();
// ...
}
Podesoltarfogosdeartifício!Temosumjogosimples,emboracompleto
emtermosdeanimaç ão,engineealgoritmos.
194

## Página 202

CasadoCódigo Capítulo8. Incorporeanimações,sons,pausaevidasextrasaojogo
Exercícios
Agoraficaráporsuacontamelhorarojogo!Aquiestãoalgumassug-
estõesdoquevocêpodefazer:
• Criarnovostiposdeinimigos;
• Fasesecenáriosdiferentes;
• Tiposdiferentesdenavesetiros;
• Coletadeitens;
• Eoquemaissuaimaginaçãopermitir!
Comosconhecimentosquevocêadquiriu, essastarefasnãodev-
erãosertãoárduasassim.Sevocêsentirquenãotembomdomíniodo
gameengine,sugiroquerefaç aacriaç ãodojogo,quantasvezesforem
necessárias,atésentir-seseguro.
195

## Página 204

Capítulo9
Publiqueseujogoetorne-o
conhecido
9.1 H ospede-o em um serviço gratuito
Talvezvocê,sendodesenvolvedorweb,játenhaosmeiosdeterseujogopub-
licadonaweb. Noentanto,paratirarquaisquereventuaisdúvidas,oucaso
vocêsejainiciantenestamatéria,queromostrarummeiodevocêcolocarseu
jogonainternet,usandoumdosinúmerosserviçosdehospedagemgratuita
existentes.
Nossojogonãoémaisdoqueumapáginawebestática,usandoapenas
tecnologiasdoladocliente(umpoucodeHTMLeCSS,emuitoJavaScript).
Destaforma,podesercolocadonawebcomoqualquersitecomum.
Escolhio Hostinger(http://www.hostinger.com.br),porconsiderá-lofá-

## Página 205

9.1. Hospede-oemumserviçogratuito CasadoCódigo
cildeusarejáestarhabituadoaele. Noentanto,vocêpodeescolheroutro
serviço,sepreferir.Acesseositeecliquenolink Criar conta:
Hospedagens gratuitas
Algunsexemplosdehospedagensgratuitasdisponíveis:
• Hostinger:http://www.hostinger.com.br
• Hospedagratis.net:http://hospedagratis.net
• Qlix:http://www.qlix.com.br
Figura9.1:CriandoumacontanoHostinger
Oformuláriodecadastronãoémuitodiferentedosformuláriosmais
básicosexistentesnaweb:
198

## Página 206

CasadoCódigo Capítulo9. Publiqueseujogoetorne-oconhecido
Figura9.2:CadastronoHostinger
Apósisto,éprecisoacessarseue-maileclicarnolinkdeativaç ãoen-
viadopelaHostinger. Casonãoapare ça,confirasuapastadespamoulixo
eletrônico.
Dolink,vocêirádiretoparaaescolhadoplanodehospedagem. Para
pequenosaplicativos,podemosusaroplanogratuitosemmedo:
Figura9.3:Vocêestá‘comprando’oplanogratuitopeloincrívelpreçodezero
reais!
Emseguida,vocêtemaop çãodeusarumsubdomíniogratuito,aoinvés
199

## Página 207

9.1. Hospede-oemumserviçogratuito CasadoCódigo
deadquirirumnomededomínio(lembre-sedeque,paraterseuendere ço
próprionainternet,éprecisopagarataxaderegistro). Foiestaop çãoque
usei,emboraeuimaginequevocê,comofuturodesenvolvedordejogos,vá
umdiaquererterodomínio www.jogosdo(seunomeaqui).com.br:
Figura9.4:Criandoosubdomínio
Apróximatelaseráapenasumaconfirmaç ãodosdadosdodomínio.Dig-
iteasletraseaceiteostermoscomodecostume.
Odomínioestácriado! Cliqueemseunomeeemseguidaapareceráo
ícone Gerenciar:
Figura9.5:AbraodomínioeentreemGerenciar
Vocêteráquerolarumpoucoapáginaparaencontraro Gerenciador
de Arquivos:
200

## Página 208

CasadoCódigo Capítulo9. Publiqueseujogoetorne-oconhecido
Figura9.6:ÍconedoGerenciadordeArquivos
Seoserviçosolicitarumaconfirmaç ãoparainstalarogerenciador,clique
em Instalar.
Crieassubpastasdojogo.Useobotão Nova Pastaecrieaspastas img
e snd:
Figura9.7:Criandoumanovapastanahospedagem
Figura9.8:Crieaspastasimgesnd
201

## Página 209

9.1. Hospede-oemumserviçogratuito CasadoCódigo
Useobotão Fazer Uploadesubaosarquivosdapastaprincipal.Em
seguida,entrenaspastas imge snderepitaoprocesso. Vocêpodesubir
váriosarquivosdeumavez.
Figura9.9:Botãodeuploaddearquivos
Renomeieoarquivo jogo-definitivo.htmlpara index.html.É
poressenomequeoservidorreconheceapáginainicialdeseusite:
Figura9.10:Apáginaprincipaldevesechamarindex.html
Porúltimo,deleteaantigapáginaprincipalcolocadapelaHostinger(ar-
quivo default.php).
Pronto, pode navegarno site recém-criado epublicar seu URLonde
quiser!
202

## Página 210

CasadoCódigo Capítulo9. Publiqueseujogoetorne-oconhecido
Figura9.11:Jogopublicadoemhospedagemgratuita
9.2 L inkando com as redes sociais
Obtendo uma ID do Facebook
ParapoderinteragircomoFacebookemsuasaplicações,vocêdevepossuir
um App ID,queéumcódigodecadastronoFacebookassociadocomseu
aplicativo.
Primeiro, faça o login no Facebook como de costume. Em seguida,
acessehttp://developers.facebook.comeabraomenu Aplicativos. Se
vocêaindanãoédesenvolvedor,seráapresentadaaop ção Register as
a Developer:
203

## Página 211

9.2. Linkandocomasredessociais CasadoCódigo
Figura9.12:Registre-secomodesenvolvedornoFacebook
Suacontaseráconfirmadacomodesenvolvedor.Agoravocêtemaop ção
Create a New App:
Figura9.13:CriandoumaplicativonoFacebook
Emseguida,vocêteráquepreencherosdadoscomoonome,umaiden-
tificação(namespace)quedeveserúnicaparacadaaplicativo,acategoriaetc.
204

## Página 212

CasadoCódigo Capítulo9. Publiqueseujogoetorne-oconhecido
Figura9.14:Cadastreseuaplicativo
Pronto,vocêjátemumaID!Guardeocódigoemalgumlugarseguro.
Figura9.15:IDdeaplicaç ãonoFacebook
Agora,temosqueconfiguraraURLdenossositeparaevitarproblemas
depermissão.Váaolink Configuraçõesecliquenobotão Adicionar
Plataforma.Selecione SiteepreenchaaURLdeseusitenocampoque
foiaberto:
205

## Página 213

9.2. Linkandocomasredessociais CasadoCódigo
Figura9.16:ConfigureaURLdeseusite
Porúltimo,nocampo App Domains,insiraoendere çoquevocêacabou
deconfigurar(oFacebookjálistaautomaticamenteasURLsconfiguradas):
Figura9.17:ConfigureaURLnocampoAppDomains
Estamos prontos para inserir funcionalidades do Facebook em nosso
jogo!
Inicializando a API
Ocódigodeinicializaç ãodaAPIpodeserobtidodopróprioFacebook,no
endereçohttp://developers.facebook.com/docs/javascript/quickstart/v2.0.A
própriadocumentaçãorecomendaquesejacoladologoapósaaberturada
tag <body>:
<body>
<script>
window.fbAsyncInit = function() {
FB.init({
// Esta é sua ID
appId : '256351554550031',
206

## Página 214

CasadoCódigo Capítulo9. Publiqueseujogoetorne-oconhecido
xfbml : true,
version : 'v2.0'
});
};
(function(d, s, id){
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) {return;}
js = d.createElement(s); js.id = id;
js.src = "http://connect.facebook.net/pt_BR/sdk.js";
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
</script>
...
</body>
Botão Compartilhar
Em http://developers.facebook.com/docs/plugins/share-button, você
podegerarumbotão“Compartilhar”parasuapágina. Ocódigogeradoé
semelhanteaomostradoaseguir. Coloque-onolocalqueacharmelhor,
dando-lhebastantedestaquenapágina:
<div id="botao_compartilhar"
class="fb-share-button"
data-href="http://sua_hospedagem_aqui"
data-type="button_count"></div>
Compartilhando a pontuação
Umacoisamuitointeressanteépodermospostarqualquerinformaç ão
programaticamente. Porexemplo,podemoscolocarumlinkparapostaro
scorenateladeGameOver!
Primeiro,criamosesselink:
<a id="postar_pontuacao" href="javascript: postarPontuacao()">
Compartilhar Pontuação
207

## Página 215

9.2. Linkandocomasredessociais CasadoCódigo
</a>
Estelinkdevecome çarescondido,portanto,crieumaformataç ãoCSS
queooculte:
<style>
...
#postar_pontuacao {
/* Ocultar o link */
display: none;
/* Visual a gosto! */
color: yellow;
position: absolute;
left: 180px;
top: 410px;
}
</style>
Emande-oaparecernafun ção gameOver:
function gameOver() {
// ...
// Link de postar pontuação
document.getElementById( 'postar_pontuacao')
.style.display = 'block';
}
Afun ção postarPontuacaochamaaAPIdoFacebookparaabriruma
janelaquecompartilhatexto:
function postarPontuacao() {
// Aqui obteríamos a pontuação do jogo
var pontuacao = 100000;
// API de feed do Facebook
FB.ui(
208

## Página 216

CasadoCódigo Capítulo9. Publiqueseujogoetorne-oconhecido
{
method: 'feed',
name: 'Jogo de Nave',
caption: 'Jogue e compartilhe com seus amigos! ',
description : (
'Minha pontuação foi: ' + painel.pontuacao
),
link: 'http://sua_hospedagem_aqui'
},
function(response) {}
);
}
Porúltimo,mandeolinkdesaparecernafun ção iniciarJogo:
function iniciarJogo() {
document.getElementById( 'postar_pontuacao').style.display =
'none';
// ...
}
Dêaolinkumvisualbemagradáveleveja-onateladeGameOver:
209

## Página 217

9.2. Linkandocomasredessociais CasadoCódigo
Figura9.18:TeladeGameOvercomlinkparapostarapontuaç ãonoFace-
book
Figura9.19:PopupdecompartilhamentodoFacebook
210

## Página 218

CasadoCódigo Capítulo9. Publiqueseujogoetorne-oconhecido
Agoraseujogoestáprontoparaserdivulgadonasredessociaispelosseus
jogadores!
211

## Página 220

CasadoCódigo ReferênciasBibliográficas
Referências Bibliográficas
[1] DavidGeary.Core HTML5 Canvas - Graphics, Animation and Game De-
velopment.2012.
[2] DavidGeary.Html52dgamedevelopment:Introducingsnailbait.2012.
[3] W3Schools.Html5canvas.
213