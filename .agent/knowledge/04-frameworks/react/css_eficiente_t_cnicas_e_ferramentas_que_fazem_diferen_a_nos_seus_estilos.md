---json
{
  "id": "css_eficiente_t_cnicas_e_ferramentas_que_fazem_diferen_a_nos_seus_estilos",
  "title": "CSS Eficiente Técnicas e ferramentas que fazem diferença nos seus estilos",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Arquivo Original:** `CSS Eficiente Técnicas e ferramentas que fazem diferença nos seus estilos.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "cnicas",
    "css",
    "diferen",
    "eficiente",
    "estilos",
    "fazem",
    "ferramentas",
    "frameworks"
  ],
  "perguntas_tipo": [
    "Como utilizar CSS Eficiente Técnicas e ferramentas que fazem diferença nos seus estilos?",
    "Quais as boas praticas de react?"
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
  "dono": "stack-react",
  "prioridade": 2
}
---

# CSS Eficiente Técnicas e ferramentas que fazem diferença nos seus estilos

> **Arquivo Original:** `CSS Eficiente Técnicas e ferramentas que fazem diferença nos seus estilos.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

52571


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
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 3

E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 4

E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 5

CasadoCódigo Sumário
Sumário
1 Introdu ção 1
2 Seletores CSS 7
2.1 EspecificidadeCSS. . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2 ComoseletoresCSSsãointerpretados . . . . . . . . . . . . . 12
2.3 NãouseIDscomoseletoresCSS. . . . . . . . . . . . . . . . . 17
3 CSS orientado a objetos 23
3.1 PrincípiosbásicosdeCSSorientadoaobjetos . . . . . . . . . 25
3.2 Exemplosdeobjetos. . . . . . . . . . . . . . . . . . . . . . . . 27
3.3 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4 SMACSS 31
4.1 Introdu çãoaSMACSS . . . . . . . . . . . . . . . . . . . . . . 32
4.2 Nomenclatura . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.3 Base . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.4 Layout. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
4.5 Módulo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
4.6 Estado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4.7 Tema. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
4.8 MaisexemplosdapráticadeSMACSS . . . . . . . . . . . . . 43
4.9 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
i
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 6

Sumário CasadoCódigo
5 BEM 49
5.1 PensandoBEM. . . . . . . . . . . . . . . . . . . . . . . . . . . 50
5.2 EscrevendoBEM. . . . . . . . . . . . . . . . . . . . . . . . . . 54
5.3 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
6 Pré-processadores CSS 59
6.1 Oquesãopré-processadoresCSS?. . . . . . . . . . . . . . . . 60
6.2 Aninhamentoderegras . . . . . . . . . . . . . . . . . . . . . . 63
6.3 Variáveis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
6.4 Mixins. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
6.5 Extensão/Heran ça . . . . . . . . . . . . . . . . . . . . . . . . . 72
6.6 Importa ção . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
6.7 MaissuperpoderesdeSass . . . . . . . . . . . . . . . . . . . . 80
7 CSS namespaces 83
7.1 OsCSSnamespacesmaiscomuns . . . . . . . . . . . . . . . . 84
7.2 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
8 Task Runners 99
8.1 OquesãoTaskRunners? . . . . . . . . . . . . . . . . . . . . . 100
8.2 ComoinstalaroGulp . . . . . . . . . . . . . . . . . . . . . . . 101
8.3 GulpAPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
8.4 ExemplodetarefascomGulp . . . . . . . . . . . . . . . . . . 104
8.5 SugestõesdepluginsGulp . . . . . . . . . . . . . . . . . . . . 110
8.6 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
9 ITCSS 113
9.1 OqueéITCSS?. . . . . . . . . . . . . . . . . . . . . . . . . . . 114
9.2 Ascamadasdotriânguloinvertido . . . . . . . . . . . . . . . 115
9.3 Organiza çãodocódigocomITCSS . . . . . . . . . . . . . . . 124
9.4 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
10 O fim 129
Versão:18.5.25
ii
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 7

Capítulo1
Introdução
Ah,asCSSs!Asqueridasfolhasdeestiloquetantoamamos e,àsvezes,odi-
amos,queestãoconosco,osdesenvolvedores front-end,namaioriadosdias
denossotrabalho!
Desdequenossocoleganorueguês Håkon Wium Liebrindouomundo
comsuainven çãointeligentementechamadade Cascading Style Sheets(CSS),
muitacoisajáaconteceucomessasdanadinhas!
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 8

CasadoCódigo
Fig.1.1:H åkonWiumLietentandoconvenceroW3CaaprovarasCSS
Atualmente,épossívelalcan çarcomaCSSoque,aténãomuitotempo
atrás,nãosepassavadesonhooudousodemuitoscódigosJavaScript.Devido
àssuasmodernascaracterísticasrecentes,elassepopularizarameganharam
oscora çõesdemuitosdesenvolvedoreseentusiastasportodoomundo!
Asfolhasdeestilonãosãotãocomplicadasdeseaprender.Aocontrário,
sãopopularesjustamentepelasuafacilidadeerápidoinício,aliadoàvisuali-
zaçãoimediatadoqueseestáfazendo!Emsuma:aCSSéfamosa!
Entretanto,comoqualquercoisaemnossasvidas,tambémexisteolado
ruim.Comopassardotempo,essafacilidadedeusotrouxeumladonegativo
aoecossistemadeestiliza çãoparaweb:aado çãoinvoluntáriademáspráti-
casdeuso.Nãoqueissotenhasidoalgomaquiavélico,umaconspira çãode
meiadúziade webdevsmaléficosrumoàdissemina çãodepráticasruins.Sim-
2
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 9

CasadoCódigo Capítulo1. Introdução
plesmenteaconteceu.Porcontadissoeporninguémteravisadoquenãoera
certo,elasimplesmentepropagou-seecontinuouassim.
Com a palavra: quem entende do assunto
Tenhoafelicidadedetercontatocomalgunsdosgrandesnomesdocená-
riomundialquandooassuntoéCSS.Certamente,oquepessoascomo Harry
Robertse Jonathan Snookpensamsobreboaspráticascontabastante!
Paraenfatizaroquãoimportanteéadotarasboaspráticasqueestãopre-
sentesnestelivro,pergunteiaestasduassumidades: Por que uma Arquitetura
CSS é importante? E por que precisamos de uma?
Harry Roberts,do CSS Wizardry(http://goo.gl/sXt93d),criadordame-
todologiaITCSS(9)quechegaaoBrasilcomexclusividadepormeiodeste
livro,respondeu:
CSS é incrivelmente fácil de escrever incrivelmente fácil , mas possui uma
ordem de magnitude mais difícil para se gerir, manter e escalar. Como os proje-
tos ficam mais maduros e maiores, CSS pode realmente começar a “comer pelas
beiradas”, causando quantidades incalculáveis de confusão, dores de cabeça e
frustrações para os desenvolvedores responsáveis por geri-los.
Isso se dá, principalmente, devido a uma série de princípios fundamentais
de CSS que tornam inerentemente mais difícil a gestão de qualquer projeto de
UI não trivial: é impossível encapsular totalmente regras, então todas elas têm a
capacidade de herdar ou repassar estilização de e para outras; nada é imutável,
logo, é possível acidentalmente desfazer ou interferir com outras regras no pro-
jeto; não existe fluxo de controle ou lógica, o que significa que não há nenhuma
pista sobre a forma ou o estado do projeto; sua sintaxe liberal (loose syntax)
torna muito fácil que as pessoas façam a coisa errada; há total dependência
da ordem do código, o que significa que, se por ções de código são movidas (ou
adicionadas em partes erradas do projeto), um monte de outras coisas podem
(potencialmente) quebrar; a especificidade trabalha contra alguns dos outros
princípios de design do core da linguagem; e o fato de ser tão simples significa
que todo mundo que mexe com CSS, muitas vezes, tem sua opinião de como as
coisas devem ser feitas, o que leva a colisões e confusão.
Quando todos esses problemas se reúnem em grande escala, cada um é am-
pliado e se torna ainda mais evidente. Uma arquitetura CSS nos fornece uma
3
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 10

CasadoCódigo
forma estruturada de escrita e gerenciamento de CSS de uma forma que tanto
contorna ou doma essas esquisitices, quanto dá aos desenvolvedores um con-
junto de regras e diretrizes a seguir a fim de continuar a escrever CSS que é
amigável, são, simples de compreender e mais fácil de escalar.
Jonathan Snook,criadordoSMACSS(4),disse:
Sistemas grandes, complexos, em crescimento, precisam de organização. T o-
dos estes precisam de alguma maneira de dar sentido à complexidade. Progra-
mação orientada a objetos existe há décadas como uma maneira de estabelecer
a ordem em meio ao caos. Desenvolvimento server-side tem sido por anos a
ascensão popular de frameworks MVC. JavaScript tem sido a ascensão de fer-
ramentas para gerenciamento de dependência.
Somente nos últimos anos, temos visto qualquer tentativa de organizar CSS
de uma forma sensata. Abordagens como OOCSS e SMACSS surgiram para
proporcionar entendimento mais facilitado de projetos, permitindo qualquer
um a, rapidamente, “pular dentro” e ser mais produtivo, a ser capaz de fazer
isso sem a sensa ção de que tudo vai desmoronar quando alguma mudan ça é
feita.
Estassãopalavrasdeeminentesdesenvolvedoresfront-enddoplaneta
Terra.Seelasnãosãoosuficienteparafazervocêchegaràconclusãodeque
umaArquiteturaCSSmaisrobustaé imprescindívelparaprojetosfront-end
profissionais,entãonãohámaisnadanomundoquefará.
Conclusão
Estelivrotemoobjetivodeajudar,pelomenosumpouquinho,adisse-
minaralgumasboaspráticasetecnologiasinteressantíssimasparaseescrever
emanutenirprojetosCSSparavocêquejátrabalha(outrabalhou)comas
folhasdeestiloequeraprimorarseutrabalho,passandoaescrever CSS efici-
ente.
Portanto,nelevocê não vaiencontrarexplica çõesbásico-teóricascomo:
oqueéecomoéformadaumaregraCSS;regrasdeusuário,denavegadore
deautor;comparativoentreCSSinline,incorporadoeexterno;qualadife-
rençaentreIDseclasses;oquesãopseudoclassesepseudoelementos;quais
aspropriedadesCSSexistentesevalorespossíveisparacadaetc.Naverdade,
muitasdessasinforma çõesnemserãoúteisaqui.Logo,fa çamosumcombi-
4
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 11

CasadoCódigo Capítulo1. Introdução
nado:ficarásubentendidoquevocêéumapessoaquejáestudoutudoissoe
agoraaprimorarásuashabilidades.
Imaginequeestamoscuspindoemnossasrespectivasmãoseasapertando
numchacoalharamistosoparaselaressepacto.
Aproveitealeitura!
5
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 12

E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 13

Capítulo2
SeletoresCSS
Amaioriadosdesenvolvedoresfront-end,principalmenteosquedãome-
norimportânciaàteoria,criasuasprópriasregrasCSScomosenãohouvesse
amanhã.Emboraissosejaverdadeemrela çãoaalgunsprazosestabelecidos
peladoceecarismáticafiguradogerentedeprojetos,asfolhasdeestilosão
escritassemplanejamento,semprepara ção,semconsciênciaesemmuitos
outrosatributosessenciaisparaqueumtrabalhobemfeitopossaserexecu-
tado.
Sevocêseenquadranessainfelizdescri ção,estecapítuloéimportantís-
simo,jáquevaiabordartemascomoespecificidadeCSS,explica çãodecomo
osseletoresCSSsãointerpretadoseoutrasdicasgerais.Ointuitoéadissemi-
naçãodapráticadeplanejaraescritaderegrasCSSantesdeescrevercódigo
àscegas.Ouseja,pensarantesdefazer.
Alémdavantagemóbviadeadquirirmaisconhecimentosepassaraes-
creverCSSsmelhores,vocêtambémterácondiçõesdeargumentarcomoseu
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 14

2.1. EspecificidadeCSS CasadoCódigo
gerentedeprojetossobrecomoéimportanteplanejarsuasfolhasdeestilo
paraobterumCSSmaiseficienteeprofissional.
Ese,aindaassim,nãoadiantar,pe çaaelequemeenvieume-mailpara
lerumaouduasverdades!
2.1 E specificidadeCSS
ÉsimplesescreverregrasCSS:primeiroescrevaoelemento,classeouIDque
sequerestilizar(aísãoinclusosseletoresavan çados)eapliqueasproprieda-
descabíveis.Porém,jáaconteceudevocêcriarumaregrae,poralgummo-
tivo,elanão“entrouemação"?Querdizer,vocêacriouesperandoquetudo
corressebem,mas,poralgummotivo,elanãofoiaplicadaeoutraregrateve
precedência?
ProvavelmenteissoacontececomtodosquetrabalhamcomCSS.Édevido
à especificidade de CSSqueissoocorre.Umdosmotivosdehaver“Cascata”
em“FolhadeEstiloemCascata”éreferente,justamente,aquãoespecífica
determinadaregraé,paraser“maisimportante”queoutraseentraremação
emdetrimentoàsdemais.
O que é a especificidade CSS?
NãoentenderateoriaeapráticadaespecificidadeCSS,raramente,não
levaaconfusões,desgostosefalsasacusa çõesdebugs “Jácrieiaregra,mas
elanãofunciona!”,jáhavendorelatosdeaumentodepressãoenáuseas.En-
tretanto,nãoéalgotãodifícildeseentender.
PensenaespecificidadeCSScomoum sistema de pesosqueservepara
determinarqualregraCSStemprecedênciaquandováriaspodemseraplica-
dasaomesmoelemento.Regrascommaiorpesotêmpreferênciasobreregras
demenorpesoeporisso“ganharão”eentrarãoemaçãoquandoonavegador
renderizaosestilos.
T odaregraCSStemsuaespecificidadeimplícita;portanto,mesmonão
sabendo,vocêjásevaledaespecificidade! Aideiaéque,apartirdeagora,
vocêfaçaissoconscientemente.
8
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 15

CasadoCódigo Capítulo2. SeletoresCSS
Entendendo a especificidade CSS
Existem4categoriasquedefinemoníveldeespecificidadeaumdadose-
letor.Presteaten çãonaordem,poiséimportante.Parafacilitarasexplica ções,
vamosatribuirletrasacadauma:
a) Estilosinline;
b) IDs;
c) Classes,pseudoclasseseatributos;
d) Elementosepseudoelementos.
Porexemplo,seriapossívelvisualizaraespecificidadedeumelemento h1
daseguintemaneira:
h1 = (a=0), (b=0), (c=0), (d=1)
Querdizer,noseletor h1existe0estilosinline;0IDs;0classes,pseudo-
classeseatributos;1elementooupseudoelemento.
Paraficarmenosverboso,issopoderiasermostradocomo:
h1 = 0,0,0,1
Parafacilitaraindamais,tambémépossível“transformar”issoemum
númerointeiro:
h1 = 0001
Seoseletorfosse #content h1,teríamos:
#content h1 = 0,1,0,1
Ou:
#content h1 = 0101
9
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 16

2.1. EspecificidadeCSS CasadoCódigo
Issosignificaque,seambasasregrasexistissememumconjuntodeestilos
deumapágina, #content h1 teriaprecedênciaemrelaçãoa h1,dadoque
0101 > 0001.
Atente-seaofatodequeamatemáticaenvolvidaésomenteparademons-
traralógicaqueacontece“nosbastidores”.Seriacompletamenteincoerente
se,porpadrão,CSSpriorizasseaestiliza çãodeumelementopuroemde-
trimentoàestiliza çãodestemesmoelementodentrodeumcontêiner(neste
caso,umID),queéumseletormaisespecífico.
Maisum:
#sidebar ul li a.myclass:hover = 0,1,2,3
0estilosinline;1ID;2classes,pseudoclassesouatributos;3elementosou
pseudoelementos.
Penserápido: qualopesodoseletoruniversal *? 0! Elenãotem
estilosinline,IDs,classes,pseudoclassesouatributos,nemelementosou
pseudoelementos.Simplesassim!
Paraajudarafixa çãodoconceito,tenteresponder: dadoumconjunto
deregrasCSS,entreosseletores #content article ul e #content
.list,ambosservindoperfeitamenteparaestilizarlistasdentrodeumcon-
têiner,qualdosdoisteriamaispesoeentrariaema ção?
Fazendooscálculos:
#content article ul = 0,1,0,2
#content .list = 0,1,1,0
Noseletor #content article ul existe0estilosinline;1ID;0classes,
pseudoclasseseatributos;2elementooupseudoelemento.Jáno #content
.list,0estilosinline;1ID;1classe,pseudoclassesouatributo;0elemento
oupseudoelemento.
Como 0110 > 0102,aregracomoseletor #content .list teriamais
peso,alémdetambémserumseletorCSScommelhorperformance,comose
veráaseguir.
10
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 17

CasadoCódigo Capítulo2. SeletoresCSS
Paratreinarbastante,inventealgunsseletoressempensarnopesoede-
poistentechegaraoseucálculo.Paraconferirsevocêacertou,useaCalcula-
doradeespecificidadeCSS:http://goo.gl/ekN1G0.
Casos especiais na especificidade CSS
ExistemalgunscasosespeciaisnaespecificidadeCSS:
• Empate;
•!important.
Nocasodeacontecerumempate,ouseja,duasoumaisregrasemum
mesmoconjuntodefolhasdeestilocomomesmopeso,acascataCSSentra
ema ção.
Aousar !important,ovalordarespectivapropriedadeganhapriori-
dadesobrequaisquerefeitosdaespecificidade.Havendoconflitoentrevários
!important,novamenteentraema çãooefeitocascata,comprecedência
dasCSSdeusuárioàsdeautor.
!importantfoioriginalmentecriadoparaserusadosomentecomo
umamaneiradesobreporregrasdefolhasdeestilodeautor. Infeliz-
mente,seuusoseespalhoudamaneiraerradae,atualmente,eleéusado
indiscriminadamente:porpregui çae/oudesconhecimentodaespecifi-
cidadeCSS.
Agoraquevocêjáconhecesobreaespecificidade, comece a usar
!important somente para o fim a que se destina!
Comoexplicadoanteriormente, todaregraCSStemsuaespecificidade
implícita;ouseja,vocêjáestavavalendo-sedissomesmosemsaber.Aideia
éque,apartirdeagora,vocêfa çausodosbenefíciosdaespecificidadeCSS
conscientemente.Aoutilizá-la,vocêescreverámelhoresseletoreseescapará
desitua çõesemque,semesteconhecimento,nãosecompreendebempor
que“tal”ou“qual”propriedadenãoestásendoapresentada,mesmotendo
sidodeclarada.
11
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 18

2.2. ComoseletoresCSSsãointerpretados CasadoCódigo
2.2 C omo seletores CSS são interpretados
NodiaadiadetrabalhocomCSS,infelizmente,nãoétãocomumodesenvol-
vedorprestaraten çãoemcomoestáescrevendoseusseletoresCSS.Aimensa
maiorianãorecordaqueaformacomoosseletoressãoescritosinfluenciaa
performancedeseuCSS,afetandodiretamenteaqualidadedocódigoecomo
(dequemaneira)essasregrassãoavaliadaspelointerpretador.Émaisoume-
noscomoaconteciacomaespecificidadeCSSantesdevocêterlidootópico
anterior.
Valesemprelembrarquepelomenos80%dasquestõesdeperformance
dewebsitessãoreferentesafront-end(http://goo.gl/mNbo45).Portanto,é
interessantee,emalgunscasos,vitalparaosucessodeumsite,queosseletores
CSSsejamescritoseotimizadosdemodoagarantiromelhordesempenho
possível!
Éverdadequeasdicasapresentadasaseguiraplicam-se,principalmente,
asitesdealtodesempenho,nosquaisavelocidadeéumacaracterísticaim-
prescindívelemilelementospodemestarpresentesnoDOM.Porém,não
importasevocêestádesenvolvendoopróximoFacebookouumsiteparao
decoradorlocal:asmelhorespráticassãoasmelhorespráticas!
SeletoresCSSnãosãonovidadesparavocê. Osseletoresmaisbásicos
sãodetipo(exemplo: div), ID(exemplo: #header)eclasse(exem-
plo: .tweet),respectivamente. Osmaisincomunsincluempseudoclas-
sescomuns(exemplo: :hover)eseletoresCSS3maiscomplexos,incluindo
:first-childou [class^="grid-"].
Seletorestêmumaeficiênciainerenteque,partindodosmaiseficientes
paraosmenoseficientes,são:
• ID(#header);
• Classe(.promo);
• Tipo(div);
• Irmãoadjacente(h2 + p );
• Filho(li > ul );
12
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 19

CasadoCódigo Capítulo2. SeletoresCSS
• Descendente(ul a);
• Universal(*);
• Atributo([type="text"]);
• Pseudo-classe/Pseudo-elemento(a:hover).
Éimportantenotarque,apesarde,tecnicamente,umIDsermaisrápidoe
maisperformático,estadiferen çaémínima,atédesprezível(comoserámos-
tradonodecorrerdolivro).
Combinando seletores CSS
Épossívelterseletoresindependentes,como #nav,quevãoselecionar
qualquerelementodeID“nav”,ouvocêpodecombinarseletores,como#nav
a,quevãocorresponderaqualquerlink/âncoradentrodequalquerelemento
deIDde“nav”(nocaso,seriasomente1porpágina,portratar-sedeID).
Podeparecerestranhoeumpoucodifícildeseentenderrapidamente,
mas,diferentementedoqueamaioriadosocidentais,quecostumamlerda
esquerdaparaadireita, seletores CSS são lidos da direita para a esquerda
pelosnavegadores.Paratentarcompreenderomotivopeloqualosbrowsers
fazemisso,lembremo-nosdaquelesjogosde“encontreocaminho”quebrin-
cávamosnasrevistasdanossainfância. Todosnósiniciávamosaresolu ção
peloobjetivofinaldoemaranhadodetrajetórias,retrocedendoatéumdos
pontosiniciaispossíveis.
Fig.2.1:Vocêjábrincoucomisso,admita!
13
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 20

2.2. ComoseletoresCSSsãointerpretados CasadoCódigo
Émaiseficienteparaumnavegadorcome çarsuaprocuraporcombina-
çõesapartirdoelementomaisàdireita(oqueelesabequereceberáoestilo)
etrabalharoseucaminhodevoltaatravésdaárvoredeDOM,doquecome-
çarnoaltodessaárvoreepercorrerocaminhoparabaixo,poispoderianem
mesmoacabarnoseletorqueprecisareceberaestiliza ção(tambémconhecido
como seletor-chave).
Jádeupraterumano ção,mas,casoqueiraumaexplica çãomaisdeta-
lhada,confiraotópico CSS Selectors parsed right to left. Why?noStackOver-
flow(http://goo.gl/IXCgic).
O seletor-chave
Oseletor-chave, comodiscutido, éapartemaisàdireitadeumsele-
torCSS.Eleéoqueointerpretadordobrowserprocuraemprimeirolugar.
Lembre-sedaordemdosseletoresmaiseficientesqueabordamosanterior-
mente.Sejaqualforoseletor-chavedavez,aoescreverCSSeficiente,éeste
seletorquecontémosegredodoaltodesempenho!
Umseletorcomo:
#content .intro { }
Onavegadorprocurarátodasasinstânciasde .introe,depois,come çar
asubirnoDOMatéencontraroelemento #content.
Noentanto,oseguinteseletornãoémuitoperformático:
#content * { }
O que ele faz é olhar para cada elemento da página (para cada um,
mesmo!) e, em seguida, checar se qualquer um deles é descendente de
#content.Esteéum seletor com performance ruime,comoseletor-chave,
émuito“expensivo”. Usandoesteconhecimento,épossíveltomarmelhores
decisõesquantoaomododeclassificareselecionarelementos.
Vamosdizerque,emumapáginarealmentegrandedeumsiterealmente
enorme,hácentenasou,mesmo,milharesdeelementos a.Há,também,uma
pequenase çãodelinksdemídiasocialemum ulcomumID“social”,com3
links,digamosque:Twitter,FacebookeGoogle+,alémdeincontáveisoutras
âncoras.
14
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 21

CasadoCódigo Capítulo2. SeletoresCSS
Portanto,seriaexcessivamentecustosoenadaperformáticoumseletor
como:
#social a { }
Oquevaiaconteceraquiéqueonavegadorvaiavaliartodososmilhares
delinksnapáginaantesdefazero matchcomosde #social. Oseletor-
chavecorrespondeamuitosoutroselementosquenadatêmavercomaesti-
lizaçãopretendida.
Pararemediarasitua ção,umasolu çãopossívelseriaadicionarumseletor
maisespecíficoeexplícito, .social-link,paracadaumdos adaárea
social.Porém,issoiriacontraofatodequenãoéaconselhadocolocarclasses
desnecessáriasnamarcaçãoquandoépossívelusarumasolu çãomaisenxuta.
Éporissoqueo desenvolvimento web focado em desempenho éalgo
tãointeressante.Umestranhoequilíbrioentremelhorespráticasdepadrões
webeperformance!
ConsidereoseguintecódigoHTML:
<ul id="social">
<li><a href="#" class="twitter">Twitter</a></li>
<li><a href="#" class="facebook">Facebook</a></li>
<li><a href="#" class="gplus">Google+</a></li>
</ul>
ComoseguinteCSS:
#social a { }
Agora,vejaesteoutroHTML:
#social .social-link { }
Ou,dependendodamarca çãopresente:
.social-link { }
Essenovoseletor-chavevaicorresponderapoucoselementos,oquesig-
nificaqueonavegadorconseguiráinterpretaraestiliza çãomaisrapidamente
epassarparaapróximacoisaaserfeita.
15
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 22

2.2. ComoseletoresCSSsãointerpretados CasadoCódigo
Lembre-sedequeseletores-chavedeterminamquantotrabalhoonavega-
dorterádefazer.Prestebastanteaten çãoneles!
Superqualificando seletores
Vocêjáviuoqueéumseletor-chaveequeénelequeestáamaiorpartedo
trabalhoqueointerpretadordeCSSdonavegadortemdefazer.Aboanotícia
équeépossíveltrabalharparaotimizá-loaindamais!Amelhorcoisasobre
terbonsseletores-chaveexplícitosecriarCSSeficienteedequalidadeéqueé
possívelevitara“superqualificação”deseletores.
Umseletorsuperqualificadoseparececom:
html body .wrapper #content a { }
Onavegadortemqueolharparatodososelementos a,verificarseestá
emumelementodeID contentrespectivamenteeassimpordiante,atéchegar
em html.Issoestáfazendocomqueelepasseporcaminhosque,realmente,
nãoprecise,sendopelomenos3desseselementosnoseletortotalmentedes-
necessários.
#content a { }
Umoutroexemplo,infelizmente,bastantecomum:
ul#nav li a { }
Jásesabeque,seo aestádentrode li,quetemqueestardentrode
#nav,demodoqueépossível,eliminaro lidoseletorlogodecara.Comoo
#navéumID(ejásabemosquesópodemexistirIDsúnicoseexclusivamente
nominadosnapágina),oelemento ultambémpodesereliminado.
Umaformamelhor(masaindanãoideal)deseescrever,seria:
#nav a { }
Seletoressuperqualificadosfazemcomqueonavegadortrabalhemais
doqueprecisaedeveria.Construaseletoresmaisenxutosedealtode-
sempenho,eliminandoaspartesdesnecessárias.
16
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 23

CasadoCódigo Capítulo2. SeletoresCSS
T oda essa otimização de seletores é realmente necessária?
Arespostacurtaé:provavelmente,não.
Arespostamaislongaéquedependedositequeestásendodesenvol-
vido.Sevocêestátrabalhandonopróximoprojetodeseuportfóliopessoal,
dêpreferênciaaescreverumcódigolimpoemdetrimentoàperformancede
CSS,porque,nestecaso,nãofarátantadiferen ça. Agora,sevocêestácons-
truindoapróximaAmazon,microssegundosdevelocidadesnapáginafarão
adiferen ça!
Entretanto,independentementedotamanhodoseuprojeto,osnavega-
doresinterpretarãodeformaigualeterãoomesmotrabalhodeanálisedas
regrasCSS.Seestiverescrevendoalgocomo:
div:nth-of-type(3) ul:last-child li:nth-of-type(odd) * {
font-weight: bold;
}
Você,muitoprovavelmente,estáfazendoacoisaerrada!
Porém,seseuhumildeprojetowebcome çaaexpandireatercadavez
maisacessos,crescendoexponencialmenteacimadoesperadodeumahora
paraaoutra,osrecursosdespendidosparaotimizaroCSSserãoomelhor
investimentoaserfeito? Seráquenãohaveráarrependimentospornãoter
escritoumbomCSSdesdeocome çoseissoacontecer?Ficaaquestão.
2.3 N ão use IDs como seletores CSS
QuandoseestáaprendendoatrabalharcomCSS,écomumqueseestudelogo
noinícioasdiferen çasentreIDseclasses;quaisvantagensedesvantagens
cadaumapresenta;comoequandousarumououtroeassimpordiante.
Mas,apósarealiza çãodealgunstestesdeperformance,podeserqueesse
aprendizadooriginalprecisedeumapequenarevisão.
Quandoseédesenvolvedorweb,fazercomquecódigose/oumarca ções
sejamcadavezmelhores,independentedeemquallinguagemestiverem,é
praticamenteinerenteaoofício.Comissoemmente,algumasconsidera ções
interessantespodemserencontradas,principalmenteemrela çãoaousode
17
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 24

2.3. NãouseIDscomoseletoresCSS CasadoCódigo
seletoresdeIDemCSS,apóssefazeralgunstestescomperformanceemfolhas
deestilo.
Porém,existemalgunspontosquemerecemserlevadosemconsidera ção:
• Performance;
• Fragmentação;
• Tradição.
Performance
PergunteparaqualquercodificadorCSSeeleresponderáqueosseletores
deIDsãoosmaisrápidos.Entretanto,issovemcomumagrandelimita ção:
IDssãoosseletoresmaisrápidossomenteseforemosseletores-chave.
Paraumseletor #home a,chegaaseraténormalsuporqueobrowser
vailocalizaroelementodeID homeeaplicarosvaloresdaspropriedadesem
todosseuslinks.Rapidíssimo,nãoé?Agora,vejaoquerealmenteacontece:
elepegatodososelementos aeverificasesãodescendentesimediatosde
#home.Casonãoseja,vaichecandoosascendentesatéchegara <html>.
Seráqueadiferen çadeperformanceétãograndemesmo?Paratercer-
teza,foramfeitos3testesusandoo Criador de T estes CSSdeSteveSouders
(http://goo.gl/DwfTuC).Cadaumdelesutilizou1000elementosqueforam
selecionadosapartirdeIDsindividuais,classesouIDscomosseletores a.As
páginasforamrecarregadasdiversasvezesparapegaramédiadosresultados
(númerosemms).
18
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 25

CasadoCódigo Capítulo2. SeletoresCSS
Fig.2.2:Médiaderesultadosdostestes(ms)
Paraas1000regrastestadas,osIDsmostraram-secercade1milésimode
segundomaisrápidodoqueasclassescomoumseletor-chave. Emoutras
palavras, a diferença de desempenho entre IDs e classes é irrelevante!
OcenáriomaiscomumdeseusarumIDcomo namespacedeumele-
mento(sendoesteoseletor-chave)érealmentemaislentodoqueusando
umaclasse. Mas,novamente,somentecom13milissegundosdediferen ça.
Isso também é válido para os poucos bytes extras para adicionar uma
classeaumelementoquejátenhaumID,porexemplo,mudando <div
id="search">para <div id="search" class="search"> .
Porém,issonãoquerdizerquetodososseletoressejamiguais. Osele-
toruniversal *ealgunsCSS3têmdesempenhorelativamentefracoquando
usadoscomoseletores-chave.
19
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 26

2.3. NãouseIDscomoseletoresCSS CasadoCódigo
Fig.2.3:Desempenhodeseletores:porcentagemportipodeseletor
Noentanto,usandoseletoresCSS,nãosetornaumproblemaseforpara
1a2seletores(elementose/ouclasses).Oimpactonasuaperformanceépe-
quenosecomparadoaoutrascoisas,comootimiza çãodeimagensouredu ção
derequisi çõesHTTP.Essetipodecoisaéoquerealmenteimportaquandose
tema performance do sitecomofatorpreponderante.
Fragmentação
Alémdeserem“anzóisdeestilo”,IDssãoutilizadoscomoidentificadores
defragmentosespecíficosdapágina(um hrefqueterminaem #ancora
levaaoelementodeID âncora)eparausodeJavaScript.SejáexistemIDsna
páginaporoutrasrazões,porquenãoreutilizá-losparaestilizar?Oproblema
équeissotornaocódigofragmentado:hádependênciasentreCSSeJavaS-
cripte/ouumidentificadordefragmento.Usandoclasses,épossíveldecidir
mudarparaum(novo)esquemadenomea çãoaqualquermomentoetudo
comqueéprecisosepreocuparéalteraralgunsnomesnoCSSeHTML.
ExistemmuitopoucoscasosemqueestilosbaseadosemIDnuncaserão
reutilizados. Umexemploéusar #searchparaacaixadebuscadosite.
Pode-sedecidirmaistardequeumanovacaixadebuscaseráadicionadaem
outrolocal(abaixodosresultadosdebusca,porexemplo).
Mesmoelesendoúniconesseprojeto,talvezvocêqueiraumpoucode
CSSrápidoparacopiarecolaremumprojetofuturo,quetambémpodeter
umacaixadepesquisanorodapédapágina.Aindaqueparaumgrupocom-
plexodefolhasdeestilo,épossíveldividiressespadrõesemváriostrechos
reutilizáveisdeCSS.UsarclassesemvezdeIDsimpedequeessesproblemas
potenciaisvenhamàtona.
20
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 27

CasadoCódigo Capítulo2. SeletoresCSS
AocontráriodeIDs, não há nenhuma restrição em usar várias classes,
tantoemmaisdeumaveznapágina,quantováriasdelasemummesmoele-
mento. NavegadoresaindaestilizarãoIDs,mesmose,porengano,houver
duplicaçãoemumapágina.Masaventurar-seforadoHTMLválidootorna
propensoaproblemas.
Tradição
EstilizarcomIDseclassessãoumadasprimeirascoisasqueaprendemos
sobreCSS.Porisso,podeserumdesafiolerquenãosedeveusarIDsem
seletoresCSS.Oramododesenvolvimentowebestásempremudando.Oca-
sionalmente,precisamosreavaliaroquefuncionaounão,emvezdeapenas
ficarcomoqueestánosservidobem,semquestionamentos.
No momento, estamos passando por um renascimento maciço com
HTML5,CSS3,desempenhodeJavaScripteoutroseventos.Logo,éumbom
momentoparaesserepensar.Éimportanteexaminarasrazõesdeformara-
cionaledecidirseasquestõesapresentadassãorealmenteválidas,emvezde
rejeitá-lasdeantemão.
Conclusão
Comopôdeserconstatado,parecequenãohárazõesconvincentespara
seusarIDsemseletoresCSS(anãoserpara namespaces,usode widgetse
pluginsespecíficosemCMSsecasossimilares).Classespodemfazertudoo
queIDsfazem! Pensenissonapróximavezqueiniciarumprojetoetente
trabalharcomclasses,deixandoosIDsparaidentificadoresdefragmentosou
hooksparaJavaScript.
Agoraquejávimosmaissobreespecificidadeealgumasboaspráticas,
veremosnopróximocapítulocomodaropróximopassonaeficiênciadeseu
CSSconhecendoCSSorientadoaobjetos.
P .S.:aquelaconversadepedirparaseugerentedeprojetosmeenviare-
mailsfoibrincadeira.Ésério.Nãofa çaisso!
21
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 28

E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 29

Capítulo3
CSSorientadoaobjetos
Apesardeserpossívelencontraralgunsdesenvolvedoreswebquepraticam
asduasartesmilenaresprincipaisdaprofissão(front-endeback-end),omais
comuméqueseescolhaumadessasáreasparainvestireseguircomosestu-
dos.Mesmoquevocênãosejaversadonosmísticosconhecimentosdoback-
end,pelomenosjádeveterouvidofalarem Orientação a Objetos.
Tentandoabstrairesimplificaromáximopossível,oobjetivodopara-
digmaé evitar repetição de código.Tenhototaldesapre çoàpalavra‘para-
digma’,maspesquisasmostramquelivrosqueatêm,empelomenosuma
ocorrência,contamcomvendagem12,73%superior.
Nofinaldodia e,por“dia”,leia-se:décadasdeesforçoscombinadospor
desenvolvedoresdomundointeiro,aOrienta çãoaObjetosestáaíparaajudá-
losanãorepetircódigoe,consequentemente,facilitarsuaexpansãoemanu-
tenção,pormeiodeseusinúmerosmétodosetécnicas.
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 30

CasadoCódigo
Em2009,devidoàcomprovadaeficiênciadoparadigma,adesenvolve-
dora Nicole Sullivan(ex-Yahoo!)teveaideiadetrazerositeparaofront-end
paraqueoobjetivoprincipaltambémpudesseseralmejadoemCSS.Assim
surgiuo CSS orientado a objetos.Naverdade,elachamoude Object Oriented
CSS(OOCSS);issoéumatradu ção.
DêumaboaolhadanocódigosCSSdeseusúltimosprojetosevejaque
hámuitarepetiçãodesnecessáriadepropriedades.Quantasdeclara çõespara
definirfontes,espa çamentoseposicionamentosrepetidas,linhaporlinha,
existem? Calma,nãoprecisacontarrealmente;éapenasparaenfatizarque
écomumdeacontecer. Issoacabagerandoproblemasdemédioprazoque
atrapalhamoandamentodequalquerprojetoquesepreze.
Aboanotíciaéqueexisteumacura: CSS orientado a objetos.
Paradeixarbemclaro,nãosetratademudarasintaxedoCSSouins-
talaralgumpacotemágicoqueofarámelhor.CSSorientadoaobjetosé
umametáforaparaindicarqueépossívelescreverumCSSmaiseficiente,
semrepeti ções,queensejeaprojetosmaisprofissionais.Nocasodoqueé
mostradonestecapítulo,éconsideradoporalgunsatécomo framework.
CSSorientadoaobjetosvisaresolveralgunsproblemasclássicosdeCSS,
taiscomo:
• Adificuldadedetocarprojetosdemédio/grandeporte;éprecisoser
umexpdertparaisso;
• OtamanhodosarquivosCSSécadavezmaiorconformeoprojetoevo-
lui;
• Reúsodecódigoquaseinexistente(pessoasnãoconfiamemcódigo
alheio);
• Códigofrágil(atéomelhorcódigopodeseperderquandoumnãoex-
pertmexenele).
24
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 31

CasadoCódigo Capítulo3. CSSorientadoaobjetos
Sevocêanalisarestesitens,facilmenteconstataráqueoproblemaqueos
originaé,alémdafaltadepadroniza çãodecódigo,nãoplanejarparaescrevê-
los!Ouseja,nãohámaisreflexãoarespeitodaaplica çãodatecnologiaCSS,
ou,sepreferir,onãoamadurecimentoprofissionaldamaioriadosqueaapli-
cam.
Segundo aDona Sullivan (http://goo.gl/VUV2xA) , as soluções que
emergemdousodeOOCSSsãoinúmeras(etentadoras),tornandoseuCSS:
•Modular:combinável,reusáveleextensível;
•Leve:relacionamento1:NentreCSSepotenciaislayouts;
•Rápido:poucasrequisi çõesHTTPetamanhosmínimosdearquivos;
•Pronto para o futuro:manutenível,semânticoepadronizado;
•Simplificado e acessível:umbombonzinho!
Se,nasuaopinião,essassãocaracterísticasdesejáveisaumcódigoCSS,
continuelendo.
3.1 P rincípios básicos de CSS orientado a obje -
tos
DentrodapropostadeOOCSS,existemdoisprincípiosmaisimportantes:
• Separarestruturaeskin;
• Separarcontêinereconteúdo.
Separar estrutura e skin significarepetircaracterísticasvisuaiscomo
“skins” separadas, que podem ser combinadas em vários “objetos” para
conseguir-seumaextensagamadevaria çõesvisuaissemmuitocódigo.Por
exemplo,backgroundseestilosdeborda.
Adiretriztambémpodesignificarousodeclassesparanomearobjetos
ecomponentes,emvezdeconfiarsomentenasemânticaHTML.Porexem-
plo,umobjetodemídiacom class="media"eseuscomponentescom
25
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 32

3.1. PrincípiosbásicosdeCSSorientadoaobjetos CasadoCódigo
class="img"(paracomponentesdeimagemevídeo)e class="bd"(para
componentesdetexto). Aoreferenciaressasclassesnasfolhasdeestilo,o
HTMLganhaumaflexibilidademaior;ouseja,seumnovoelementodemí-
diasurgirnospróximosanos(como <svg>),elepodereceberaestiliza ção
semquesejaprecisomexerem1linhadeCSS!
Separar contêiner e conteúdoessencialmentequerdizer:raramenteuse
estilosquedependamdelocaliza ção.Idealmente,umobjetodeveparecer-se
igual,independentementedeondeestivernapágina,oumesmosetrocarde
página.
Emvezdeestilizarumtítulosecundárioespecíficocom .myObject h2
{ },crieeapliqueumaclasseque descrevaoelementoemquestão,como
<h2 class="category-title">.Issogaranteque:
• Todosos<h2>semaclassenãosejamafetadosinadvertidamente;
• Todosos<h2>comaclassetenhamomesmoestilo;
• Nãoéprecisocriarestilosextrasparaoscasosemquesejaprecisoque
um .myObjectsepare çacomum <h2>nãoestilizado.
O que é “objeto” em OOCSS?
ContinuandocomametáforadeOrienta çãoaObjetos(OO),umobjeto
emCSSéanálogoaumainstânciadeumaclasseJavaouPHP,porexemplo.
UmobjetoCSSéformadopor4elementos:
• HTML,quepodeser1oumaisnósdoDOM;
• DeclaraçõesCSS,queestilizamestesnós,come çandocomonomeda
classereferenteao wrapper;
• Componentescomoimagensdebackgroundesprites,porexemplo;
• ComportamentosJavaScript,listenersoumétodosassociados.
IssopodeserconfusoporquecadaclasseCSSnãoéumobjetonecessari-
amente,maspodeserumapropriedadedeumaclasse wrapper.Porexemplo:
26
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 33

CasadoCódigo Capítulo3. CSSorientadoaobjetos
<div class="mod">
<div class="inner">
<div class="hd">Bloco Head</div>
<div class="bd">Bloco Body</div>
<div class="ft">Bloco Foot</div>
</div>
</div>
Oobjetoéummódulo,indicadopelaclasse mod. Elecontém4nós-
propriedades(quenãopodemexistirsemomódulo),incluindo2regiões
obrigatórias( innere bd)e2regiõesopcionais( hde ft).
OOCSS e performance
Valer-sedeOOCSStambémtrazobenefíciodaperformance,queéduplo:
•Intenso reúso de código:oquesignificamenoscódigoCSS,arquivos
menoresetransferênciasmaisrápidas;
•Menos repaints e reflows:senãosabeoqueissosignifica,leiaoar-
tigo: O que todo desenvolvedor front-end deve saber sobre renderização
de páginas web(http://goo.gl/9rCo4B).
3.2 E xemplos de objetos
Existemdiversostiposde“objetos”emOOCSS.Vejaexemplosdealgunsdeles
aseguirparafixarmelhorosconceitosealiarteoriaàprática.
Media
Oobjeto Mediapermitequevocêtenhaumaimagem(ouflash)ououtro
tipodemídiacomtamanhofixoàesquerdaoudireitacomalgumconteúdo
queadescrevanocentro.
Classes:
•.media:wrapperdoobjetoMedia;
•.img:nó-filhodoobjetoMedia,sendogeralmenteumlinkouimagem,
aparecendoàesquerdadonó .bd(opcionalmenteconstanoobjeto);
27
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 34

3.2. Exemplosdeobjetos CasadoCódigo
•.bd:áreaprincipaldeconteúdodoobjetoMedia,podeconterquais-
queroutrosobjetos(obrigatórioconstarnoobjeto);
•.imgExt:nó-filhodoobjetoMedia,sendogeralmenteumlinkouima-
gem,aparecendoàdireitadonó .bd(opcionalmenteconstanoob-
jeto).
HTML:
<div class="media">
<a href="http://twitter.com/stubbornella" class="img">
<img src="http://a3.twimg.com/image.jpg"
alt="Stubbornella">
</a>
<div class="bd">
<a href="http://twitter.com/stubbornella">
@Stubbornella
</a>
<span class="detail">14 minutos atr&aacute;s</span>
</div>
</div>
Data Table
Oobjeto Data Table sedestinaaformatarumatabelacorretamente
paradeterminadostiposdedados.
Classes:
•.data:wrapperdo Data Table;
•.txtL:alinhaàesquerda,sendoopadrão(aplicávelem table, tr,
tdou th);
•.txtR:alinhaàdireita(aplicávelem table, tr, tdou th);
•.txtC:alinhaaocentrohorizontal(aplicávelem table, tr, tdou
th);
•.txtT:alinhaaotopo(aplicávelem table, tr, tdou th);
28
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 35

CasadoCódigo Capítulo3. CSSorientadoaobjetos
•.txtB:alinhaaofundo(aplicávelem table, tr, tdou th);
•.txtM:alinhaaocentrovertical(aplicávelem table, tr, tdou th).
HTML:
<div class="data">
<table class="txtC"><!-- alinhamento da tabela ao centro -->
<tr class="odd txtL">
<th scope="row" class="txtR">
Alinhado &agrave; direita
</th>
<td>Alinhado &agrave; esquerda</td>
</tr>
<tr class="even">
<th scope="row">Alinhado ao centro</th>
<td>Alinhado ao centro</td>
</tr>
</table>
</div>
Existembemmaisobjetos,mas,comoinformadoanteriormente,estes
exemplosforamsomenteparaseveralgoaplicadonaprática. Noreposi-
tóriooficial(http://goo.gl/6ZqGKo),épossívelencontrartudoemaisum
poucosobreOOCSS.Contudo,paraconseguirmexercomseguran ça,você
precisaconhecerumpoucosobrepré-processadoresCSS,assuntodeumca-
pítulovindouro.
3.3 C onclusão
ASra. Sullivan naverdade,nãoseiseelaécasada,masmantenhooSra.
emsinalderespeito gentilmentedisponibilizouumwikinoGitHub(http:
//goo.gl/rBwNjN).Orepositóriocontémumprojetobemferramentadopara
brincarcomOOCSS,contandocomumaconfigura çãodeVMcomVagrant,
comandos makeeoutrascaracterísticasbonitasdesever,eumdomíniocom
exemplospráticosdosconceitosdeOOCSSparafacilitaradissemina çãode
suasideias(http://goo.gl/cCFAhH).Acessandoessasreferências,vocêpode
29
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 36

3.3. Conclusão CasadoCódigo
encontrarmaisinforma çõesarespeitodeCSSorientadoaobjetosecontinuar
seusestudos.
AideiadetrazerconceitosdeOrienta çãoaObjetosparaCSSfoilouvá-
vel,mas,naprática,apropostaapresentadaporNicoleéumtantoengessada,
dadoqueéprecisoconheceroqueestádisponíveletrabalharcomclassese
estruturaspredefinidas. Nãoseriainteressantesetudoissofosseumpouco
maisflexívele,comoplus,tivessealgumtipodeaprimoramentodearquite-
tura?
OOCSSinspiroumuitosdesenvolvedoresarealizartrabalhosmelhores
e,até,adesenvolvernovassolu çõesinspiradas/baseadasnaideiadedesaco-
plamentoereúsointensodeCSS.Éocasode SMACSS,quevocêveráno
próximocapítulo.
30
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 37

Capítulo4
SMACSS
Jonathan Snookéumdesenvolvedorcanadenseque,assimcomovocê,per-
cebeuqueamaneiracomooCSSéescritoegerenciadopoderiasermelhor.
Evidentemente,ofatodetertrabalhadoduranteanosemumsem-númerode
projetosinclusiveparagrandesempresas,comoYahoo!,mesmaempresaque
Sullivan,doCSSorientadoaobjetos,docapítulo3)oajudouaconstatarisso.
Antetamanhaindigna çãoecomintuitodeauxiliaroscolegasdesenvolvedo-
res,comotambémasipróprio,decidiunormatizardeterminadasregraspara
queissofossepossível. Em2011,2anosdepoisdosurgimentodeOOCSS,
surgiaa SMACSS.
SMACSS(pronuncia-se“smacks”)significaScalable and Modular Archi-
tecture for CSS(ouArquiteturaEscaláveleModularparaCSS).Elaestámais
parauma normatização,comofoidito,doqueparauma“inven çãoCSS”.Foi
algoquesurgiuemvirtudedaanálisedotrabalhodopróprioSnookedecole-
gasaoobservarasmelhorespráticasparaestruturarcódigoCSSemgrandes
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 38

4.1. IntroduçãoaSMACSS CasadoCódigo
projetos,masque,comovocêverálogoaseguir,podeserusadoemprojetos
dequalquerporte.
NaspalavrasdopróprioJonathan,SMACSSestámaisparaumguiado
queparaumframework,comoalgunscostumamconsiderar. Nãosetrata
denenhumarquivoquepreciseserbaixadoouserinstalado. Trata-se,na
verdade,detentardocumentarumaabordagemprática,útileconsistenteao
escreverCSS.
Poressemesmomotivo,nãoprecisaserseguidoàriscanecessariamente:
pode-se,depoisdeaprenderSMACSS,aplicaroquesejulgamaisconveniente
paradeterminadoprojetoouincorporarsomenteaspartesquefazemsentido
para vocêaoseupróprio know-howdedesenvolvimento.
Estecapítulonãotemapretensãodesubstituiroconhecimentoquese
encontranolivrooficial,quepodeseradquiridoemhttps://smacss.com/por
umprecinhomuitocamarada.Aocontrário,pretendeapresentarSMACSSe
passarporsuasprincipaisdiretrizesparaquevocêpossaconhecermaisares-
peito.Aoconstatarqueéummétodoquerealmentevaleapenaseraprendido
maisafundo,vocêpodeoptarporadquirirolivroesaberdemaisdetalhese
nuancesarespeito.
4.1 I ntrodução a SMACSS
UmdosprimeirosconhecimentosqueseadquireemSMACSSéarespeitoda
estruturaeorganiza çãodeseusarquivos.Mesmoemprojetosdemédioporte,
raramenteépossívelencontrartodasasregrasCSSemumúnicoarquivode
desenvolvimento!EmSMACSS,existem5categoriasbásicasdeorganiza ção
decódigoCSS:
• Base;
• Layout;
•Module(Módulo);
•State(Estado);
•Theme(Tema);
32
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 39

CasadoCódigo Capítulo4. SMACSS
Regras Basesãoasregraspadrão.Sãoquasequeexclusivamenteseletores
deelementos,mastambémpodehaverseletoresdeatributos,pseudoclasses
ouseletoresmaisavan çados,comoseletores-irmãos.
Regras Layoutdividemapáginaemse ções,podendoconter1oumais
módulos.
Módulocontémasregrasprincipaisdeumprojeto,asquedãoo“vo-
lume”deCSS.Elassão,comoindicaopróprionome,aspartesmodularese,
consequentemente,asmaisusadas.
Regras Estadodescrevemcomodeterminadolayoutoumódulosecom-
portaemdeterminadacondi çãoou“estado”(ativoouinativo;ocultoouvisí-
vel).Tambémdescrevemcomoummódulopodeserdiferentedependendo
dapáginaemqueestá;porexemplo,serapresentadodeumjeitonapágina
inicialedeoutroemumainterna.
Asregras T emasãosimilaresàs Estado,hajavistaquedescrevemcomo
layoutsoumódulosdevemsepareceremdeterminadassitua ções.Amaioria
dossitesnãoprecisadetemas,masébomestarpreparadoparaquandoforo
caso.
Nãoénecessáriopreocupar-seemdecorarascategorias;vocêasfixará
comotempoepráticadeSMACSS.Preocupe-se,nestemomento,emsaber
queaideiaéqueoCSSsejaorganizadoemváriosarquivos,separadospor
“função”,comregras/linhas-guiaespecíficasqueseaplicamacada“tipo”e
suarazãodeexistir.
Comessaorganiza ção,torna-sepossívelevitarrepeti çõesderegraseo
códigoficamuitomaisorganizadoemanutenível,alémdetambémfacilitar
bastanteoperíododeadapta çãoeentendimentodeprojetodenovospartici-
pantesquetambémconhe çamSMACSS.Criam-se padrões,certamentealgo
dequetodoprojetoquealmejecontarcomostatus“profissional”precisa.
4.2 N omenclatura
Valer-sededeterminadasregrasdenomenclaturaéconvenienteaoseseparar
asregrasnestas5categorias,porqueajudaaidentificar,deimediato,aqual
delascertafolhadeestilopertenceeseupapelnoescopogeraldoprojeto.
Convencionou-seusarumprefixoparadiferenciarentreLayout,Módulo
33
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 40

4.3. Base CasadoCódigo
eEstado:
• Usarl-(ou layout-)paraLayouts;
• Usaris-paraEstados(exemplo: is-hidden, is-collapsed);
• Nãousarprefixom-ou module-paraMódulos;porseremasfolhas
deestiloemmaiornúmeroemprojetos,torna-sedesnecessário.
Vejaalgunsexemplos:
/* Módulo "Example" */
.example { }
/* Módulo "Callout" */
.callout { }
/* Módulo "Callout" com Estado */
.callout.is-collapsed { }
/* Módulo de campo de formulário */
.field { }
/* Layout "Inline" */
.l-inline { }
4.3 B ase
Regras Basesãoaplicadasaelementosusandoseletordeelemento,deseletor-
descendenteoudeseletor-filho,alémdepseudoclasses. Nãoestãoinclusos
seletoresdeIDeclasses.
Servemparadefinircomoéaaparênciapadrãodedeterminadoselemen-
tostodasasvezesemqueestesaparecemnaspáginasdoprojeto. Incluem
especificaçõesdetamanhosdetítulos,aparênciapadrãodelinks,estilosde
fontes,backgroundsgeraisetc. Geralmente,nãohánecessidadedeseusar
!importantemestilosBase.
Exemplo:
34
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 41

CasadoCódigo Capítulo4. SMACSS
body,
form {
margin: 0;
padding: 0;
}
input[type="text"] {
border: 1px solid #999;
}
a {
color: #039;
}
a:hover {
color: #03c;
}
Tambémservemdeexemploaqueles CSS reset,comregrasque“zeram”
determinadaspropriedadesparatentaruniformizaraapresenta çãoentrena-
vegadores. Emboraeuconsidereaabordagemdeusarum“padronizador”,
como normalize.css(http://goo.gl/TxmiBv),maiseficiente.
VejaoutroexemplodeumafolhadeestiloBase,extraídodeumprojeto
realmeu:
*,
*:before,
*:after { box-sizing: border-box; }
/* @see http://stackoverflow.com/a/2610741/922143 */
::-webkit-input-placeholder { /* WebKit browsers */
color: #333;
}
:-moz-placeholder { /* Mozilla Firefox 4 to 18 */
color: #333;
opacity: 1;
}
35
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 42

4.4. Layout CasadoCódigo
::-moz-placeholder { /* Mozilla Firefox 19+ */
color: #333;
opacity: 1;
}
:-ms-input-placeholder { /* Internet Explorer 10+ */
color: #333;
}
body {
font-family: Arial, sans-serif;
overflow-x: hidden;
}
h1,
h2,
h3,
h4,
h5,
h6 {
letter-spacing: 1px;
}
figure {
margin: 0;
}
input,
select,
textarea {
font-size: 1rem;
}
4.4 L ayout
Layoutpodeserentendidodemuitasmaneirasdiferentes,dependendodeseu
contextoedaáreadeatua çãoemqueapalavraéusada.NocasodeSMACSS,
36
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 43

CasadoCódigo Capítulo4. SMACSS
éprecisodiferenciarentreoscomponentesmaioresemenoresqueformam
umapágina,sendoaquelesasregrasLayoute,estes,Módulos,queserãovistos
logoemseguida.
Para facilitar o entendimento, relembre da explicação dada anterior-
mente: layoutspodemconter1oumaismódulos. Elestambémpodemser
divididosentre“maiores”e“menores”(bemmenoscomuns),baseando-sena
suafrequênciadereúsonaspáginasdeumprojeto.
ApesardaqueleprincípiodequenãosedeveusarIDscomoseletoresCSS
(2.3),emSMACSSnãoétãoincomumseuusoparadesignarlayoutsmaiores,
comoheaders,footersetc. Contudo,nãohánenhumtipodeproblemaem
continuarnãousandoIDscomoseletoresCSS.
ExemploderegrasdeLayout:
#header,
#article,
#footer {
margin: auto;
width: 960px;
}
#article {
border: solid #ccc;
border-width: 1px 0 0;
}
Geralmente,seletoresdelayoutsãoúnicos(razãodaleniênciaaousar
IDs),mashácasosemqueeleprecisaresponderaalgunsfatores.Porexemplo,
umsitepodeapresentarlayoutsdiferentesbaseadonapreferênciadequemo
estáacessando. Nessecaso,essaregracontinuariasendoumaregraLayout
emSMACSS,masusadaemcombina çãocomoutroestilodelayout.
Veja:
article {
float: left;
}
#sidebar {
37
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 44

4.5. Módulo CasadoCódigo
float: right;
}
.l-flipped #article {
float: right;
}
.l-flipped #sidebar {
float: left;
}
Noexemplo, .l-flippedseriaaplicadoaumelementoemnívelacima,
como body,oquepermitiriaqueoposicionamentodosprincipaiscompo-
nentesfossealternado.
Ou,emumexemplomaiscondizenteàs(irrefreáveiseirreversíveis)ten-
dênciasdewebdesignresponsivo:
#article {
float: left;
width: 80%;
}
#sidebar {
float: right;
width: 20%;
}
.l-fixed #article {
width: 600px;
}
.l-fixed #sidebar {
width: 200px;
}
4.5 M ódulo
Comojácitadobrevemente,regras Módulosãoocernedesuaaplica ção,co-
mumenteoquemaissetrabalhaemprojetosqueutilizamSMACSS.Sãocom-
38
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 45

CasadoCódigo Capítulo4. SMACSS
ponentesmaisespecíficos,comobarrasdenavega ção,widgetseassimpor
diante.
Módulosseencontrarãodentrodelayoutsquasesempre.Tambémépos-
sívelqueelessejamusadosdentrodeoutrosmódulos,oque,naverdade,éaté
comumdeacontecer.Porém,tenhasempreemmenteque,aosercriado,seu
objetivoéconseguirfuncionarcomoumcomponenteisolado( standalone).
Idealmente,deveserpossívelusarquantosmódulosforemnecessáriosem
umapágina, ouatémesmotrocarumdelugarou,mesmo,deumapágina
paraoutra semquesejaprecisorealizarnenhumajuste. Emfun çãodisto,
paraelesé estritamente proibidousarIDse/ouseletoresdeelementos!
Sótomecuidadoparanãoincorrernoerrodefazeralgocomo:
<div class="module">
<span>Tipo de Informa&ccedil;&atilde;o</span>
</div>
.module > h2 {
padding: 5px;
}
.module span {
padding: 5px;
}
Emumprimeiromomento,eleatendeaosrequisitosdeummódulodeser
possívelalterá-lodelugaroupáginaeserindependente,nãosendoafetado
porestiloscondicionaisbaseadosemsualocaliza ção. Porém,alémdeessa
soluçãoapresentarumseletorineficiente,podesernecessáriooacréscimode
outrasinforma çõesque,nãonecessariamente,sãoapresentadasdamesma
maneira,como:
<div class="module">
<span>Tipo de informa&ccedil;&atilde;o</span>
<span>Outro tipo de Informa&ccedil;&atilde;o</span>
</div>
[...]
39
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 46

4.6. Estado CasadoCódigo
Osegundo <span>equaisqueroutrosquealiforemcolocadossemain-
tençãodereceberessamesmaestiliza çãoserãoafetadospelasmesmasregras
queoprimeiro.Senãoforainten ção,serápreciso“remendar”asituaçãocom
outrasregrasoucomoinfame !important.Portanto,aten çãoaessetipode
“tentação”que,apesardesermaisfácildeplanejareescrever,podereservar
surpresasdesagradáveisparaumfuturopróximo!
Sevocêestiverseperguntando:“Mascomoresolverisso?”,nãosepreo-
cupe,poisantesdeterminarestelivrovocêjáterávistobastantecoisasobre
nomenclaturaesemânticaemCSS.
4.6 E stado
EmSMACSS, Estadoéalgoqueserveparaincrementar/sobrescreveroutros
estilos,geralmente(eporconven ção)comclassesprefixadascom is-.Por
exemplo,ummenuouse çãocomaaparência accordionpodeestarnoestado
abertooufechado;umamensagemdosistemapodeestaremumestadode
sucessoouerro.
Geralmente,estadossãoaplicadosaomesmoelementocomoumaregra
delayoutoumódulo.Porexemplo:
<div id="header" class="is-collapsed">
<form>
<div class="msg is-error">Mensagem de erro!</div>
<label for="searchbox" class="is-hidden">Buscar</label>
<input type="search" id="searchbox">
</form>
</div>
Outropontoimportanteaoqualficaratentoéquegeralmenteestados
possuemvínculocomJavaScript(JS).Afinal,comosetratadeumelemento
quepossuiestadosdiferentes,éprecisoalternarentreestesdealgumamaneira
quandoalgum triggeréacionado.Naatualtecnologiawebdisponível,issoé
feitoviaJS.
Estaémaisumaconven çãoqueajudabastante:(quase)semprequevir
umprefixo is-sendousado,automaticamentevocêjápodeidentificarque
setratadeestadocomdependênciadecódigoJavaScript.
40
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 47

CasadoCódigo Capítulo4. SMACSS
Porém,tambémépossívelsevalerdoatributo data-paratrabalharcom
estados,dadoqueseletoresdeatributotambémpodemdesempenharbem
essepapel.Entretanto,mesmousando-os,oJSaindaénecessáriopararealizar
aalternância.Veja:
.btn[data-state="default"] {
color: #333;
}
.btn[data-state="pressed"] {
color: #000;
}
.btn[data-state="disabled"] {
opacity: .5;
pointer-events: none;
}
<button class="btn" data-state="disabled">Desabilitado</button>
Como observação final, tratando-se de estados, na perspectiva de
SMACSSnãohárestri çõesemseusar !important,embora,paraCSS,você
devaevitarsemprequepossível.
Exceções e flexibilidade com regras de Estado
Haverácasosemqueumestadoserábastanteespecíficoeterárela ção
comsomenteummóduloemparticular.
Paraessescasosemqueumaregradeestadoéfeitaespecialmentepara
algummódulo,onomedasuaclassedeveteromesmonomedele.Também,a
regrapodeestarnomesmoarquivoemqueeleestá,nãohavendonecessidade
deficarseparadojuntocomosoutrosarquivosdeestado.
Porexemplo:
.tab {
background-color: #800080;
color: #fff;
}
41
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 48

4.7. Tema CasadoCódigo
.is-tab-active {
background-color: #fff;
color: #000;
}
4.7 T ema
Osignificadode T emaemSMACSSéomesmoqueemqualqueroutrosite
quenãoautiliza:umconjuntodiferenciadodecores,imagenseelementosde
UIquecaracterizamo look & feeldaspáginasdeumsite.
Quantoàelabora çãodeSMACSS,oautorJonathanSnookficouemdú-
vidaemdestinarumacategoriaespecificamenteparatemas,dadoqueapor-
centagemdeprojetoswebqueadotamseuusonãoétãoaltaassim.Dequal-
quermaneira,parafinsdeorganiza ção,eleoptoupordestinarespa çopara
estetipodesitua ção,consequentementetornandoSMACSSumaarquitetura
maisrobusta.
Nofinaldascontas,foiumadecisãointeligente,jáqueestasepara çãoen-
sejaaumatroca/substitui çãofácildetemas,quandonecessário,geralmente
emocasiõesemqueoprojetoquerservirumaskindiferenciadacomalgumas
“alteraçõescosméticas”. Porexemplo,ocasiõessazonais(datascomemorati-
vas,comoPáscoa,Nataletc.);alternativasparaquemusaosite(disponibilizar
umaskinmasculinaeumafeminina);umesquemadecoresdiferenteacada
seçãoetc.
Paraqueessasaltera ções incluídas,aqui,fontes possamserfeitasdentro
daarquiteturaSMACSS,Temapodealterarqualqueroutracategoria,umavez
que,paraatenderaumanecessidadedecria çãodetemas,podeserpreciso
alterarestilosBase,Layout,MóduloouEstado.
Naprática,oqueaconteceéoarquivodeumtemasobrescreverasre-
grasjáestipuladasemquaisquerdasoutrascategoriasSMACSSparaquea
estilizaçãonecessáriasejafeita.Vejaumexemplodeumtemaalterandouma
característicadeummódulo:
/* module-name.css */
42
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 49

CasadoCódigo Capítulo4. SMACSS
.mod {
border: 1px solid #000;
}
/* theme.css */
.mod {
border-color: #00f;
}
Sim,étãosimplesquantosevalerdasprópriascaracterísticasdecascata
deCSS!Tendoumarquivodetemapronto,paraqueestesobrescrevaasre-
grasdeumaregrabase,layout,móduloouestado,bastacarregarseuarquivo
dinamicamente(viaJavaScript)ounão.
Tambémexisteoutrapossibilidade,casosedemandemuitapersonaliza-
ção:regrasespecíficasparaotema.Umavantagemadicionalparaessapossi-
bilidadeéconseguirumajustefinodeaparência,aocolocarasclassessomente
nosbase,layout,móduloouestadoquesequeira.
Umexemploprático:
/* theme.css */
.theme-border {
border-color: #800080;
}
.theme-background {
background: linear-gradient(...);
}
Atenteaofatodeque,casoopteporusarclassesespecíficasdetema,existe
aconven çãodeseusaroprefixo theme-.
4.8 M ais exemplos da prática de SMACSS
Comojácitadoanteriormente,estecapítulonuncateveapretensãodesubs-
tituiroconhecimentoqueseencontranolivrooficialdeSMACSS.Aparte
43
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 50

4.8. MaisexemplosdapráticadeSMACSS CasadoCódigo
teóricaarespeitojáestádebomtamanhocomopropostadestelivro.Porém,
paraajudarnafixa çãodoquefoiexplicado,algunsexemplospráticospodem
serdebastanteajuda.
Estrututa de diretórios
Emprojetosdomundoreal,nãoimportandoqualsejaaestruturadopro-
jetoqueabrigaosestilos,geralmentecadaumadascategoriasdeSMACSSfica
separadaporumdiretório.Algocomo:
Fig.4.1:EstruturadediretóriosSMACSS
Nãoháquaisquerrestri çõesemhaveroutrosdiretóriosnomesmonível
hierárquicodosqueconstituemascategoriasdeSMACSS.
Comofoivisto,nemtodososprojetosprecisamde themee,paraoscasos
emqueestadossãofeitosespecificamenteparaummódulo,podemestarno
mesmoarquivoqueele.ComoSMACSSnãoérígida,nadaimpededeodire-
tório statetambémserdispensável,casoessasejasuapreferência.Oquenos
trazpara:
Fig.4.2:EstruturadediretóriosSMACSSsemstateetheme
44
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 51

CasadoCódigo Capítulo4. SMACSS
ValelembrarnovamentequeSMACSSésobreconven çõesnãorígidas,
entãofa çacomo vocêesuaequipeacharemmelhor.Épossívelaténãoque-
reremusar statee themeemumprimeiromomento,masdeixarosdiretórios
presentesnaestruturacasosedecidamouprecisemsevalerdeles.
SevocêestiverusandoGitparacontrolarasversõesdoprojeto,bastaadi-
cionarumarquivo .gitkeepemcadaumdosdiretóriosparaqueelessejam
consideradosnorepositóriomesmonãotendooutrosarquivos.
Arquivos na estrutura SMACSS
Dentrodecadadiretório,portanto,constamosrespectivosarquivosrefe-
rentesàquelacategoriaSMACSS.Emumprojetofictício,poderíamosteralgo
como:
Fig.4.3:EstruturadediretóriosSMACSScomexemplosdearquivos
Nesteprojeto-exemplo,nodiretório“base”afunçãodosarquivos,além
dosóbvios fonts.csse forms.css,seriam: base.csscomregrasmais
geraisreferentesaelementos,taiscomoestiliza çãodelinks,tamanhosdetítu-
los,parágrafoselistas,entrelinhasetc.;e generics.cssparaclassesgenéri-
cas,quepodemserusadasemqualquerpontodositeparasurtirdeterminado
efeitovisualquesequeira.Umtrechodesse generics.csspoderiaser:
45
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 52

4.8. MaisexemplosdapráticadeSMACSS CasadoCódigo
[...]
.bold {
font-weight: bold !important ;
}
.italic {
font-style: italic !important ;
}
.uppercase {
text-transform: uppercase !important ;
}
.font-size-extra {
font-size: 150% !important ;
}
[...]
Noteapresen çade !importantemcadaumadessasregras. Neste
exemplo,omotivodaexistênciadessasclasseséqueelasserãousadasem
momentosemquesuasrespectivasestiliza çõessefizeremnecessárias,sem
queocorramrepeti çõesdesnecessárias.Ébemmaisrápido,práticoeperfor-
máticodefinirumaregrasomenteumavez,usandoumaclassequefa çaseus
efeitosvisíveis,doquerepetirpropriedadesevaloresemváriasdiferentes.
Comosãogenéricas,podeserqueoelementoemquesejamaplicadasjá
tenharecebidoalgumadiretrizemcontrário. Porexemplo,sedeterminado
elementofoiestilizadocom text-transform: capitalize;, depen-
dendodorestantedosestilospodenãoadiantarinseriraclasse uppercase.
Logo,esse !importantgarantequearegragenéricatenteprioridadee,de
antemão,entreema çãosemquesejaprecisomexeremmaisestilos.
46
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 53

CasadoCódigo Capítulo4. SMACSS
Saiba quando quebrar regras
Foiditoanteriormenteque,emestilosBase,geralmentenãoháne-
cessidadedeseusar !important. Estepoderiaserumcasoemque
seoptariaporusar.Nãohánenhumproblemaemquebrarregras,desde
quesejaalgocoerenteejustificado,talcomoofoi.
Quantoaosarquivosnodiretório layout,geralmentesãosomentedefi-
niçõesdasestruturasprincipaisdaspáginasdosite.Mesmoquenãosetenha
quaisquerestiliza çõesreferentesaalgumlayout,muitosadeptosaSMACSS
criamosrespectivosarquivosedefinemumaregravazia,somentepara“de-
marcarterritório”e,dequebra,aindapouparumpoucodetrabalhofuturo,
casosejapreciso.
Dessaforma,nãohaveriaqualquercontraindica çãoemsetersomente
istonoarquivo footer.css:
.l-footer { }
Emborasejamaiscomumhaveralgumaspropriedadesevalores,como
em:
.l-footer {
background-color: #d0d0d0;
color: #333;
}
Emrela çãoaosarquivosem modules,comojáexplicado,estessãoocerne
dasfolhasdeestilodentrodeumaarquiteturaSMACSS;sãoosarquivosque
conterãoamaioriadasregras. Porisso,esseéodiretóriomaisvolumoso.
Façacomojáestáacostumadoeescrevalindas,concisasepensadasregras
CSSparaaplicaremseuprojeto!
4.9 C onclusão
Comoficouevidente,SMACSSéumaarquiteturaflexível,elaboradacombase
emanosdeobserva çãoeexperiênciaemprojetosdealtonível.
47
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 54

4.9. Conclusão CasadoCódigo
SeestafoiaprimeiravezquevocêtevecontatocomSMACSS,oconse-
lhoéqueabraceametodologiaemalgunsprojetosparaexperimentarseus
resultados.Sejáhaviaouvidofalar,masaindanãosabiabemdoquesetra-
tava,dêumachanceaSMACSSe,certamente,veráoníveldeorganiza çãoe
produtividadedeseusprojetosmelhorarembastante!
Aindaépossíveliralémcomaeficiênciadeseucódigoearquitetura.
Lembre-se:muitodaqualidadedecódigovemdapadroniza ção. Nãoseria
muitobomcasohouvesseumamaneiradeseusarumapadroniza çãojácon-
sagradanahoradecriarsuasclassese,debrinde,essaabordagemaindaga-
rantirquevocêidentifiqueaestruturadesuamarca çãonoCSSinstantanea-
mente?
Nopróximocapítulo,conhe ça BEM.
48
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 55

Capítulo5
BEM
VocêjáouviufalarnoY andex?Sevocêérusso,aprobabilidadeébemmaior;
senãoé,saibaquesetratadobuscadorcommaior market sharedaterrade
Putin(60%).Eletambéméumdosmaisusadosbuscadoresdomundo,con-
tandocomcentenasdemilhõesdebuscaspordia.
AYandextambémofereceoutrosservi ços,contandocomumecossistema
webbastantesignificativo.Quandocome çouacresceresentiranecessidade
deaprimoraremanterofront-enddessesistema,surgiu BEM(acrônimopara
Block, Element, Modifierou Bloco, Elemento, Modificador).
Na verdade, BEM é uma metodologia completa; um verdadeiro fra-
meworkdefront-end,queabarcadiversasregraseferramentasúteis.Tecni-
camente,trata-sedeumaarquiteturabaseadaemtemplatesDSLconstruídos
sobre Node.js(saibamaisarespeitoemhttp://bem.info/).
Noocidente,geralmentequandosefalasobreBEM,estásefalandoso-
brea convenção de nomenclaturausadae,consequentemente,amaneirade
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 56

5.1. PensandoBEM CasadoCódigo
pensarasestruturas(ou módulos,sevocêjáconheceSMACSS,mostradono
capítulo4).
Éessaconven çãodenomenclaturaparaBloco,ElementoeModificador
quevocêconheceráagora.
NãofazpartedasregrasestabelecidaspelaBEM;mas,paraosexem-
plos,serãousadaspalavraseminglês,oque,dependendodoalcancee
intençãodeseusprojetos,vocêtambémdeveriafazer.
5.1 P ensando BEM
ComosesabedesdeocapítulosobreCSSorientadoaobjetos(3),osconceitos
deNicoleSullivaninspiraramdiversosdesenvolvedores,técnicasemetodolo-
gias.Coincidênciaounão,aessênciadeOOCSStambémpodeserencontrada
emBEM:desacoplamentoereúsodecódigoatravésdeumasériedepadrões
preestabelecidos.
EmsetratandodeBEM,seuusovemnamudan çadecomoseenxergamas
estruturas/módulosqueseestádesenvolvendoe,obviamente,conhecersuas
convençõesdenomenclatura.
Emtermossimples,temos:
•Bloco:entidadeindependentecomseuprópriosignificado;éaabstra-
çãomaisgeraldeumcomponente/módulo;
•Elemento:descendente(eparte)deumBloco;ajudaaformá-lo,como
umtodo;
•Modificador: umestadoou“versão”diferentedeumBlocoouEle-
mento.
Segundoimagensdisponibilizadasporumadasdesenvolvedorasdapró-
priaYandex, V arvara Stepanova,nomemorávelartigoescritoem2012, A
New Front-End Methodology: BEM(http://goo.gl/ZiBO0B),serápossívelvi-
sualizareentendermelhoressesconceitos.
Vejaarepresenta çãodeumapáginafictíciaqualquer:
50
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 57

CasadoCódigo Capítulo5. BEM
Fig.5.1:Umapáginafictíciaqualquer
É possível “dividir” essa página (em um primeiro momento, mental-
mente)emdiversosBlocos:
51
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 58

5.1. PensandoBEM CasadoCódigo
Fig.5.2:Umapáginafictíciaqualquermentalmente‘dividida’
Vejamaisdeperto,porexemplo,oBlococirculadodeazul,Busca:
Fig.5.3:Blocodebuscamentalmenteseparadoemazul
ÉpossívelencontrarosElementosqueformamessebloco:
52
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 59

CasadoCódigo Capítulo5. BEM
Fig.5.4:ElementosdoBlocodebusca
Comoexemplodemodificador,poderíamosterumaapresenta çãodife-
renciadaparaquandoofocono inputaconteceouquandosesubmetemese
buscaminforma çõesdinamicamente.
VejaoBlocodasabascomseusrespectivosElementos:
Fig.5.5:Blocodeabasmentalmenteseparadoemrosa
NadaimpedequehajaBlocosdentrodeBlocos:
53
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 60

5.2. EscrevendoBEM CasadoCódigo
Fig.5.6:BlocosdentrodeBlocos
Naverdade,elesjáestavamláantesdevocêverasimagenscomasdivisões
emesmonosprojetosemquevocêparticipouantesdeterlidoqualquercoisa
sobretudoisso!Vocêaindasónãotinhaaprendidoa visualizar BEM!;)
Porisso,apartirdomomentoemquesedecidetrabalharcomele,apró-
priamaneiradeenxergarasestruturasdeumapáginasealtera,umavezque
secome çaavisualizá-lasconformeosBlocos,ElementoseModificadores,
automaticamente.
VocêvaisaberoqueéissodepoisdeusarBEMemalgunsprojetos,tenha
certeza!
5.2 E screvendo BEM
Agoraquevocêjáconsegue“visualizarBEM” podedemorarumpoucopara
queissoaconte ça,então,treine!,éhoradeaprendera“escreverBEM”.Quer
dizer,tomarconhecimentodecomoéaconven çãodasuasintaxe.
Ésimples:
.block {}
54
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 61

CasadoCódigo Capítulo5. BEM
.block__element {}
.block--modifier {}
Nasconven çõesdesuanomenclatura,Blocossãoclassescomopróprio
nomedaestrutura;Elementossãodelimitadoscom __;eModificadoresde-
limitadoscom --.
PegandooexemplomostradoantesdoBlocodebusca:
.search {} /* Bloco */
.search__field {} /* Elemento */
.search--searching {} /* Modificador */
Essa convenção garante que todos os desenvolvedores que conheçam
BEMidentifiquemaestruturaemqueoestiloatuaráinstantaneamente. O
opostotambémvale:aoseolharoHTML,pelonomedasclasses,jásesabeo
queesperardoCSSqueestilizaaquelepeda çodecódigo.
Voltandoàmetaexemplos,vejaalgunsseletoresparaajudarafixarocon-
ceito:
.person {}
.person__hand {}
.person--female {}
.person--female__hand {}
.person__hand--left {}
OBloco persontemváriosElementos,como hand,epodeterMo-
dificadores,como female. Porsuavez,osElementostambémpodemter
modificadores,taiscomo left.
Sódeterolhadoparaestemetacódigo,vocêjáfoicapazdesaberqueal-
gumasdasestruturasHTMLcorrespondentespoderiamser:
55
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 62

5.2. EscrevendoBEM CasadoCódigo
<div class="person">
<div class="person__hand">
[...]
</div>
</div>
<div class="person--female">
<div class="person__hand">
[...]
</div>
</div>
<div class="person">
<div class="person__hand--left">
[...]
</div>
<div class="person__hand">
[...]
</div>
</div>
Earecíprocaéverdadeira:setivesseolhadoprimeirooHTML,jápoderia
inferircomoseriaoCSS.
Outragrandevantageméque,usandoBEM,vocêconsegueescreverse-
letoresmenoresenãoconflitantes,evitandomuitosdosproblemasdeespeci-
ficidadeCSS(2.1)quepoderiamacontecer,fazendoseucódigoseguiraquelas
boaspráticasmencionadas.
Emoutraspalavras, cada classe BEM é única e autossuficiente!Afinal,
umseletorcomoeste:
html #content > .person .hand {}
Émuitomaisverbosoemenoseficiente(pensandoemmanutenibilidade
eperformance)doqueeste:
.person__hand {}
Issosendoqueambosserviriamparaestilizarexatamenteosmesmosele-
mentos!
56
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 63

CasadoCódigo Capítulo5. BEM
NotequenãoéprecisoquetodaaestruturadoDOMestejarepresen-
tadanosseletores.MesmoqueoHTMLtivessemaisníveis,nãoseriapreciso
umaclasse .person__body__arm__hand;uma .person__handjácon-
seguiriaestilizaroquefossenecessário,etornaraclasseúnicaeaestrutura
inteligível.
Idealmente, cadaBlocodeveserabsolutamenteindependente; ou
seja,deveserpossívelmudá-lodeposi çãonapáginaoudepágina,sem
quenenhumaaltera çãodeCSSpreciseserfeita.
LembradoobjetoMediadocapítulosobreCSSorientadoaobjetos(3)?
UsandoBEM,seusseletoresCSSpoderiamserescritosmaisoumenosassim:
.media {}
.media__img {}
.media__img--rev {}
.media__bd {}
Percebaquemuitostambémgostamdecolocarníveisdeindenta çãoex-
trasparaajudaraindamaisaidentificaraestruturadecódigos.Comousem
esseplus,sãopoucasasaltera çõesquetrazemmuitasvantagens!
5.3 C onclusão
Comovocêviu,aconven çãodenomenclaturadeBEMtemmuitodeOOCSS:
garantedesacoplamentoereúsointensodecódigopormeiodeumasérie
depadrõespreestabelecidos;padrões,estes,facílimosdeseremaprendidose
fixados.
Algunsdesenvolvedorestêmumareclama ção:“BEMéfeio!”.Pareceque
tervários __e --portodooHTMLeCSS(e,inevitavelmente,JavaScript)
nãoagradaatodos.Emminhaopinião,issonãoatrapalhaemabsolutamente
nadae,decertaforma,éatédivertido.
Masse,paravocê,usaressasintaxeformenoscompensatórioque:
57
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 64

5.3. Conclusão CasadoCódigo
• Códigodesacoplado;
• Reúsoautomáticodecódigo;
• Menosrepetições;
• RápidaidentificaçãodeestruturasHTMLatravésdoCSSevice-versa;
• Independênciaabsolutadeclasses;
• Seletoresmenoresemaisperformáticos;
• CSSmaismanutenível.
Adecisãoficaporsuaconta.EsperamosqueescolhaBEM!;)
Entretanto,seráque,depoisdeconhecerosconceitossobreOOCSS(3),
SMACSS(4)eBEM,aindaépossívelaprimorarseuscódigose workflowao
desenvolverCSS?Éoquevocêvaidescobrirnopróximocapítulo,sobre pré-
processadores CSS.
58
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 65

Capítulo6
Pré-processadoresCSS
Sevocêestiverlendoestelivronasequênciadoscapítulos,nestepontovocê
jáconhecesobreCSSorientadoaobjetos(3),SMACSS(4)eBEM(5). Para
osacostumadosafazersóofeijãocomarrozdeCSS,sãoevolu çõesbastante
consideráveis!
Porém,mesmoquevocêjátenhavistoalgoarespeitodessastécnicasou
tenhapesquisadoeseaprofundadomais,aindaépossívelaprimorarseuscó-
digoseworkflowaodesenvolverCSS!Existeumamaneiradeusarcaracte-
rísticascomquesópessoasqueconhecemlinguagensdeprograma çãoestão
acostumadas,eaplicarconceitosetécnicasdeprograma çãoasuasfolhasde
estilo!
Respire fundo, acomode-se e seja bem-vindo ao mundo dospré-
processadores CSS!
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 66

6.1. Oquesãopré-processadoresCSS? CasadoCódigo
6.1 O que são pré -processadores CSS?
ConsultandoaWikipédia queestálongedeserumafontedeconsultafide-
digna,mas,paraestecaso,serviu,épossívelsaberque um pré-processador
é um programa que recebe texto e efetua conversões léxicas nele. As con-
versões podem incluir substitui ção de macros, inclusão condicional e in-
clusão de outros arquivos.
Querdizer,vocêescreverácódigonasintaxedopré-processadordesua
preferênciae,atravésdealgunsprocessosdeconversão,eletransforma(ou
compila)essasintaxeespecíficaeprópriaemcódigoCSS,aquetodosjáes-
tamoshabituados.Casocontrário,nãoseterianenhumaestiliza ção,jáque,
paraestefim,osnavegadoresprecisamdearquivos .css.
Aquelavelhahistóriade Input -> Magic -> Output .Nocasoespe-
cíficodospré-processadoresdeCSS,o Inputéocódigodopré-processador
quevocêestiverusandoe,o Output,obomevelhoCSS àsvezes,chamado
de CSS puro.
Nestemomento,sevocêaindanãotinhaouvidofalar(oulido)sobrepré-
processadoresCSS,issopodeparecerexóticoe/oudesnecessário.Afinal,para
queincluirmaisumaetapanoprocessodeescritadeCSSsejásepodeescrever
diretamente,comosempresefez?Éjustamenteaoresponderessaquestãoque
opoderdospré-processadoressemostra!
Senãohouvessequaisquervantagensemusá-los,certamentemilharesde
desenvolvedorespelomundonãoofariam.Elesfazem-nopelosimplesmo-
tivodequeospré-processadoresCSScontamcom featuresqueextrapolamas
capacidadesnativasdoCSS!Algumaspossibilidadescompré-processadores
são:
• Usarvariáveis;
• Usarfunções;
• Aninhamentoderegras;
• Operaçõesaritméticas;
• Estenderregrasapartirderegraspré-existentes.
60
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 67

CasadoCódigo Capítulo6. Pré-processadoresCSS
Sevocêjátemalgumavivênciacomprograma ção,osimplesvislumbre
depoderusarestetipodecoisaemCSSjádeveparecerfantástico;senão,
ofatodeissoparecerfantásticoparaquemjáprogramadeveparecerfantás-
tico!Vamoscombinaroseguinte:pré-processamentodeCSSéfantásticode
qualquerjeito!
Atravésdessaseoutrasfacilidadesqueelesoferecem,muitosdesenvolve-
dorespelomundointeiromuitos,mesmo! estãoadotando-osparamelhorar
seusfluxosdecria çãodeestiloeorganiza çãodeprojetos.Continuelendopara
tambémfazerpartedessagalera!
Os pré-processadores CSS mais conhecidos
Agoraquejáfoientendidoqueessahistóriatodadepré-processadores
resume-seaescreverumpseudo-CSSque,pormeiodeprocessosespecíficos,
serátransformadoemCSSdefato;saibaque,dentreospré-processadores
existentesatualmente,trêsdelessãomaisusados:
• Sass(http://sass-lang.com/);
• Less(http://lesscss.org/);
• Stylus(http://learnboost.github.io/stylus/).
Fig.6.1:Ospré-processadoresCSSmaisusados(eoStylus)
Emfun çãodousoglobal,oStylusconstacomomen çãohonrosa. Nas
rodinhasdebotecodeprogramadoresenoitesdopijamaparamaratonasde
61
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 68

6.1. Oquesãopré-processadoresCSS? CasadoCódigo
SenhordosAnéis,quandooassuntoforpré-processadores,certamentesefa-
larásobreSasseLess.
Estecapítuloreserva-seaexplicaredemonstrarasprincipaiscaracte-
rísticasdepré-processadoresCSS.Parainstru çõessobrecomoinstalá-los
emseusistema,configurá-loseasmaneiraspossíveisdesecompilarcó-
digo,consulteosrespectivossitesoficiais.
Basicamente,SasseLessfornecemquaseomesmoacervodefuncionali-
dades.Háváriascontrovérsiasediscussõesacalouradasentreosadeptosde
umeoutro,masaverdadeéque,nessaquaseconversãodecaracterísticas,ao
optarporusarSassouLess,vocêestarábemservidoeconseguirámelhorar
muitoaorganiza çãoeworkflowdedesenvolvimentodeestilos!
Pequena observação sobre a sintaxe Sass
Tenhoumapreferênciapessoalpor Sass;todososexemplosdecódigose
featuresqueserãomostradosaseguirserãofeitoscomcódigodessasintaxe.
Comoacaboudeserexplicado,Lesstambémprovêasmaneirasdesefazer
igual,demodoquenãohaveráprejuízonoentendimento.
Apequenaobserva çãoéqueSassoferece 2 sintaxes diferentesparase
trabalhar:
• SCSS;
• Sass.
SCSS(SassyCSS) quetemextensãodearquivos .scss podesercon-
sideradacomoumaextensãodeCSS,valendo-sedamesmasintaxe-basee,
praticamente,amesmaformadeescreverregras.Basicamente,sevocêabrir
umarquivo .scsseescreverCSSpuroali,seráumarquivoSassválido.
AsintaxeSass omesmonomedopré-processador,cujaextensãodos
arquivosé .sass,jáébemdiferentedoCSScomqueamaioriadoswebdevs
estáacostumada,primandopelaconcisãoerapideznaescrita. Demora-se
umpoucomaisparaaprenderaescrevê-la,masalgunsgarantemque,uma
vezquesedomina,édifícilvoltaratrás.
62
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 69

CasadoCódigo Capítulo6. Pré-processadoresCSS
Estecapítulopropõe-seaapresentaralinguagem. Portanto,asintaxe
SCSSseráusadaporsermaisparecidacomCSSpuro,facilitandoaassimi-
laçãoefixa çãodosconceitos.
6.2 A ninhamento de regras
LogonoprimeirodiadeestudosdeHTML,éfácilconstatarquesetratade
umalinguagemqueusaelementosaninhadosparafuncionar:oaninhamento
confereestruturaeorganiza çãohierárquicaaodocumento.CSS,porsuavez,
nãopossuitalcaracterística.
OpoderdeSasscome çaasemostrarjáaqui:épossível aninhar regras
CSSparaescreverumcódigomaisconcisoemenor,conferindohierarquia
visualàsregrasefacilitandodaleitura!
Porexemplo,vejaestetrechodeCSS:
nav ul {
list-style: none;
margin: 0;
padding: 0;
}
nav li {
display: inline-block;
}
nav a {
display: block;
padding: 6px 12px;
text-decoration: none;
}
EmSCSS,épossívelescreverassim:
nav {
ul {
margin: 0;
padding: 0;
list-style: none;
63
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 70

6.2. Aninhamentoderegras CasadoCódigo
}
li {
display: inline-block;
}
a {
display: block;
padding: 6px 12px;
text-decoration: none;
}
}
Nãoéincrível? Agoravocêpodeaninharregrasdeestilose,aocompi-
larocódigo,serágeradoomesmoCSSmostradoanteriormente.Aquestão
équevocêpoupouescritaeadeclara çãoestávisualmentemaisinteligível,
evidenciando,emumsógolpedevista,ahierarquiaintrínsecadasregras.
Referência ao ascendente
Emalgumassitua ções,éprecisofazerreferênciaaoascendenteparase
montarumaregraapropriadamente. Porexemplo,dentrodoaninhamento
permitidoporSass,comoseriaparacolocarumaregracom :hover?
Setentaralgocomo:
.selector {
:hover {
}
}
OCSScompiladoserá .selector :hover {} (noteoespa ço),oque
nãoéonecessário.
Paraessescasos,Sassprovêumacaracterísticamuitointeressante,tor-
nandopossívelfazerreferênciaaoelementoascendenteimediatamentesupe-
rior:ocaractere &.
Nesteexemplodo hover,ocódigocorretoseria:
.selector {
&:hover {
64
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 71

CasadoCódigo Capítulo6. Pré-processadoresCSS
}
}
IssogerariaoCSS: .selector:hover {},exatamenteoqueestáse
buscando.
Sempreque,emSass,vocêdeparar-secom &,jásabequeainten çãoé
repetiroseletorascendenteimediatonaregra,independentedequeparte
delaesteja.Veja:
.selector {
.parent-selector--modified & {
}
}
Issovaicompilarpara:
.parent-selector--modified .selector {}
Oseguintecódigo:
#custom-checkbox {
& + label {
}
&:checked + label {
}
}
compilaráoCSS:
#custom-checkbox {
}
#custom-checkbox + label {
}
#custom-checkbox:checked + label {
}
65
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 72

6.2. Aninhamentoderegras CasadoCódigo
Sass e BEM
OpadrãodenomenclaturaBEMtrazdiversasvantagensnodesenvolvi-
mentodefront-end,comoexplicadonocapítulo5.Porém,conformefoimos-
tradoatéagorasobreocaracteredereferênciaaoascendenteimediato,um
trechoSassdotipo:
.selector {
&--modifier {
}
}
Compilariapara:
.selector .selector--modifer {}
oque,definitivamente,nãoéoesperado.
Felizmente,desdeaversãoSass3.4,osadeptosaoBEMcontamcomuma
gratacaracterística:umacompila çãoespecialquandoseusaopadrãodeno-
menclatura!
SassidentificaautomaticamenteospadrõesdeescritaBEMegeraCSS
damaneiraqueseespera! Casoemquesepodeescrevertranquilamenteo
seguinte:
.selector {
&--modifier {
}
&__subelement {
&--submodifier {
}
}
}
Eobterocompilado:
.selector--modifier {
}
66
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 73

CasadoCódigo Capítulo6. Pré-processadoresCSS
.selector__subelement {
}
.selector__subelement--submodifier {
}
Também é possível escrever tantas referências mais aos respectivos
elementos ascendentes imediatos quanto sejam precisas, já que, a partir
dessaversão,oSasscompreendeasintaxeBEMegeraCSScorretamente,
respeitando-oegarantindoregrascomboaperformancedeseletores-chaves
(2.2)!
6.3 V ariáveis
Seopoderdospré-processadoresdeCSSlimitasse-sesomenteapermitiro
usode variáveis,aindaassimseriamtãofamososeusadoscomosãoatual-
mente!Poderusarvariáveisé,simplesmente,umincrívelavan çonaorgani-
zaçãoemanutenibilidadedeumconjuntodefolhasdeestilo!
VariáveisemSasssãocomovariáveisemqualquerlinguagemdeprogra-
mação: referênciasnominaiscapazesdearmazenarvaloresquepodemser
chamadasemtrechosdecódigosubsequentespararesgatareusá-loscon-
formenecessário. Paradeclararumavariável,bastadarumnomequalquer
(semespa çose/oucaracteresespeciais)precedidode $,usar :edarovalor
quesequeira,comoem:
$mainColor: #c0ffee;
Issofeito,bastausaravariávelàvontade!Porexemplo:
$mainColor: #c0ffee;
header {
background-color: $mainColor;
}
a {
67
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 74

6.3. Variáveis CasadoCódigo
color: $mainColor;
}
footer .highlight {
border: 2px solid $mainColor;
}
quecompilaria:
header {
background-color: #c0ffee;
}
a {
color: #c0ffee;
}
footer .highlight {
border: 2px solid #c0ffee;
}
Aimensavantagemépodersubstituirabsolutamentetodasasreferências
àquelacor,alterandosomenteumalinhadecódigo. Mesmonesseexemplo
comsomente3regras,jáseriamuitobom. Imagineemprojetosdomundo
real,emquenãoéraroprecisardealtera çõesdessanaturezaemdezenasde
regras!
VariáveispodemconterquaisquervaloresusadosemCSS,comoem:
$font-stack: Helvetica, sans-serif;
$width: 5em;
Quandonãosãodeclaradasforaderegras comoemtodososexemplos
mostradosatéagora,avariávelficadisponívelemtodoocódigo.Mastam-
bémépossívellimitarseuescopodeatua çãoaodeclará-ladentrodeuma
regra:
.l-main {
$width: 5em;
width: $width;
}
68
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 75

CasadoCódigo Capítulo6. Pré-processadoresCSS
Se tentássemos usar $width em qualquer outro lugar fora de
.l-sidebar,issoresultariaemerro.
A não ser que sejausadoomodificador !global,quefazcomqueela
estejadisponíveltambémemqualquerpontodocódigo. Nessecaso,seria
possívelalgocomo:
.l-main {
$width: 5em !global;
width: $width;
}
.l-sidebar {
width: $width;
}
queseriacompiladopara:
.l-main {
width: 5em;
}
.l-sidebar {
width: 5em;
}
Interpolação de variáveis
Sasspermitequesejapossívelinterpolarvariáveis. Emtermossimples,
seriacomojuntarovalordevariáveiscomoutrasvariáveisouvalores.
Parasefazerisso,referencia-seavariávelusando #{VARIAVEL}e,auto-
maticamente,ainterpola çãoacontece.Paraficarmaisclaro,vejaoexemplo:
$vert: top;
$horz: left;
$radius: 5px;
.rounded-#{$vert}-#{$horz} {
border-#{$vert}-#{$horz}-radius: $radius;
}
69
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 76

6.4. Mixins CasadoCódigo
quegeraoCSS:
.rounded-top-left {
border-top-left-radius: 5px;
}
6.4 M ixins
Mixinspermitemquesefa çamagrupamentosdedeclara çõesCSSparaserem
reusadosondesequeira.Certamente,sãoumadasfeaturesmaispoderosasde
Sass!Sevocêjábrincoucomprogramação,mixinslembrambastantefun ções.
Parasetrabalharcomeles,opar @mixin/ @includesempreestarápre-
sente. Oprimeiroparadefiniromixin,emsi;osegundo,paraindicarem
qualpontodocódigosequerusá-lo.
VejaestetrechodecódigoSasscomummixinparaarredondamentode
bordassendodefinidoeusado:
@mixin border-radius($radius) {
-webkit-border-radius: $radius;
-moz-border-radius: $radius;
-ms-border-radius: $radius;
border-radius: $radius;
}
.box {
@include border-radius(10px);
}
IssogeraráoseguinteCSS:
.box {
-webkit-border-radius: 10px;
-moz-border-radius: 10px;
-ms-border-radius: 10px;
border-radius: 10px;
}
Com6linhasdecódigo,vocêagorapodearredondarbordasemqualquer
regraquequiser,apenasusandoum @include!Comoplus,aindaconsegue
especificarqualseráoraionaprópriachamadaaomixin!
70
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 77

CasadoCódigo Capítulo6. Pré-processadoresCSS
Essapossibilidadedepassarovalorquesequerparaatuaremmixins
(argumentos)certamentefazdelesmaispoderosos.Épossívelpassarquantos
quiser,quenemasfun çõesemlinguagensdeprograma ção.Casosepasseum
argumentojáespecificandoumvalor,esteseráovalorpadrãousadodesde
queelesejaomitidoaoseusaro @include.Veja:
@mixin rounded($vert, $horz, $radius: 10px) {
-webkit-border-#{$vert}-#{$horz}-radius: $radius;
-moz-border-radius-#{$vert}#{$horz}: $radius;
border-#{$vert}-#{$horz}-radius: $radius;
}
.l-footer {
@include rounded(top, left, 5px);
}
.l-sidebar {
@include rounded(top, left, 8px);
}
.navbar li {
@include rounded(top, left);
}
Issocompilapara:
.l-footer {
-webkit-border-top-left-radius: 5px;
-moz-border-radius-topleft: 5px;
border-top-left-radius: 5px;
}
.l-sidebar {
-webkit-border-top-left-radius: 8px;
-moz-border-radius-topleft: 8px;
border-top-left-radius: 8px;
}
.navbar li {
71
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 78

6.5. Extensão/Herança CasadoCódigo
-webkit-border-top-left-radius: 10px;
-moz-border-radius-topleft: 10px;
border-top-left-radius: 10px;
}
Euquaseconsigoouvirosomdesuaslágrimaschocando-secomosolo!
6.5 E xtensão /Herança
Indubitavelmente,Extensão/Heran çaéumadasprincipaiscaracterísticasde
pré-processadoresCSS!
NocasoespecíficodeSass,épossívelusar @extendparacompartilhar
umasériedepropriedades/valoresdeváriasregrasdiferentesemumamesma
regra!Issomantémocódigodentrodoprincípiodanãorepeti ção( DRY),faz
comquesejaprecisoescreverbemmenoscódigoe,dequebra,aindagarante
queoCSScompiladosejamaislógicoeeficiente!
Comoexemplo,suponhaquevocêtenhaestaregra:
.default-box {
background-color: #efefef;
border: 1px solid #000;
color: #333;
}
Casosejaprecisocriarvaria çõesdissocomSass,umadasmaneiraspos-
síveisseriaestendê-laemoutraregra!Assim:
.alert-box {
@extend .default-box;
font-size: 2em;
}
oquecompilariapara:
.default-box, .alert-box {
background-color: #efefef;
border: 1px solid #000;
color: #333;
72
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 79

CasadoCódigo Capítulo6. Pré-processadoresCSS
}
.alert-box {
font-size: 2em;
}
Percebeopoderqueissooferece? Vocêpodeterumarquivocomdefi-
niçõesgenéricasderegrasquepodemserestendidasemquaisqueroutrasdo
projeto!Porexemplo,regrasdotipo:
[...]
.bold {
font-weight: bold;
}
.italic {
font-style: italic;
}
.display-block {
display: block;
}
.display-none {
display: none;
}
.underline {
text-decoration: underline;
}
.no-underline {
text-decoration: none;
}
.text-left {
text-align: left;
}
73
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 80

6.5. Extensão/Herança CasadoCódigo
.text-center {
text-align: center;
}
.text-right {
text-align: right;
}
.text-justify {
text-align: justify;
}
[...]
Sequiséssemosumaregraparaummóduloquepreciseterapresenta ção
embloco,negritoetextojustificado,sóserianecessárioestenderregrasjá
especificadasanteriormente!
.my-module {
@extend .display-block, .bold, .text-justify;
border: 1px solid #ccc;
}
quecompilariapara:
[ ... ]
.bold, .my-module {
font-weight: bold;
}
.display-block, .my-module {
display: block;
}
.text-justify, .my-module {
text-align: justify;
}
74
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 81

CasadoCódigo Capítulo6. Pré-processadoresCSS
[ ... ]
.my-module {
border: 1px solid #ccc;
}
Éounãoéumaeconomiatremendadedigita çãocomumcompiladocon-
dizenteaomelhorqueCSStemaoferecer?
Seletores placeholder
Noexemploanterior,foipossívelobservarquetodasasregrasespecifi-
cadasnoSassestãopresentesnoCSSgerado. Éatéconvenientequeclas-
ses,como .bold, .display-blocketc.sejamgeradas,jáquepodemser
úteisaosetrabalharcomJavaScript,adicionandoeexcluindoclassescon-
formeeventosea ções.
Entretanto,podehaversitua çõesemquedeterminadasregrasqueserão
estendidassóprecisemexistirparaissoenãoprecisemestarpresentesnoCSS
compilado.Paraisso,saibaqueexistemo seletores placeholder(placeholder
selectors).
Criarumplaceholderselectorécomoumaregracomum,comadiferen ça
dequenãosecolocaumelemento,classeouID,massimum%.Porexemplo,
sefosseprecisousarumseletorplaceholderparaestendernosestilosmostra-
dosantes,ficaria:
[ ... ]
%bold {
font-weight: bold;
}
%italic {
font-style: italic;
}
%display-block {
display: block;
}
75
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 82

6.5. Extensão/Herança CasadoCódigo
%display-none {
display: none;
}
%underline {
text-decoration: underline;
}
%no-underline {
text-decoration: none;
}
%text-left {
text-align: left;
}
%text-center {
text-align: center;
}
%text-right {
text-align: right;
}
%text-justify {
text-align: justify;
}
[ ... ]
Paraindicaraextensão:
.my-module {
@extend %display-block, %bold, %text-justify;
border: 1px solid #ccc;
}
Agrandediferen çaestánoCSScompilado,queseriasomente:
76
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 83

CasadoCódigo Capítulo6. Pré-processadoresCSS
.my-module {
font-weight: bold;
}
.my-module {
display: block;
}
.my-module {
text-align: justify;
}
.my-module {
border: 1px solid #ccc;
}
Observandoocompilado,parecequefoiumdesperdíciodefinirvárias
regrascomomesmoseletorcomsomenteumapropriedadedefinida. En-
tretanto,lembre-sedequeosplaceholderselectorspodemserestendidosem
qualquerlugar,consequentementealterandoacompila çãodefolhasdeestilo
conformeseuuso.
Outraocasiãobastanteútilparaeleséquandosetemqueusarfontesper-
sonalizadasemprojetos.Dáprafazeralgocomo:
@font-face {
font-family: 'custom_font';
src: url('font/my-custom-font.eot');
src: url('font/my-custom-font.eot?#iefix')
format('embedded-opentype'),
url('font/my-custom-font.woff2') format('woff2'),
url('font/my-custom-font.woff') format('woff'),
url('font/my-custom-font.ttf') format('truetype');
font-weight: normal;
font-style: normal;
}
%custom-font {
font-family: 'custom_font';
}
77
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 84

6.6. Importação CasadoCódigo
Semprequeprecisarquealgumelemento,classeouIDsejaagraciadocom
afontediferenciada,estendaoseletorplaceholder.
Emsuma, placeholder selectors não aparecem no CSS compilado,ser-
vindoexclusivamenteparapropósitosdeExtensão/Heran ça.
6.6 I mportação
Levandoemcontaoqueseaprendeunocapítulo(4)sobreSMACSSeasvan-
tagensdoSassaopermitirExtensão/Heran ça,nãosurpreenderiasevocêjá
tivessechegadoàconclusãodeque,emprojetosmaisprofissionais,épreciso
quesetenhadiversosarquivosdiferentes,cadaumcomseupropósitoecon-
tendosuasrespectivasregrasdeestilo.
Paraessasocasiões,oSassofereceumrecursodeimporta ção,usando
@import.
Noexemplodeplaceholderselectorsmostradoagorahápouco,certa-
mentehaveriaumarquivoSasscomtodoselese,conformeanecessidadeea
organizaçãodoprojetoporexemplo,ousodametodologiaSMACSS,acria-
çãodemaisarquivosparaconteremasregrasdevidas.Emumademonstra ção
simples,2arquivos:
Fig.6.2:Demonstra çãosimplescom2arquivos
Logonoiníciodoarquivo style.scss,bastariacolocar:
@import 'generics';
Tudooqueestádentrode _generics.scsspoderiaseracessado.Não
éprecisocolocaro _nem .scssnasintaxedeimporta ção.Tambémépos-
sívele,quasesempre,necessárioimportarváriosarquivos,separando-ospor
vírgulanadeclara çãodo @import.
78
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 85

CasadoCódigo Capítulo6. Pré-processadoresCSS
Nesteponto,cabemduasobserva çõesimportantes.
Aprimeiraéquesedeveteraten çãoaonomedoarquivoquefoiimpor-
tado,quecome çacomumsubtra ço( underline).DentrodadinâmicadoSass,
issoéchamadode partialesignificaque,nacompila ção,somenteseráge-
radoumarquivoCSSde style.scss.Emoutraspalavras,nacompila ção,
partialsnãogeramsuacontraparte .css.
Asegundaéqueéimportantenãoconfundiresse @importcomaimpor-
taçãodearquivosquejáexisteemCSSpuro. Estafazumarequisi çãoextra
noservidor,chamandoumarquivoàparte;aquelajuntatodososarquivos
importadosnoimportador,garantindoagera çãodeumarquivoúnicocom
todasasregras.
Porpadrão,Sassnãopermiteimportararquivos .cssdiretamente.
Parafinalizar,épossívelaimporta çãodearquivosemsubdiretórios.Em
umprojetocomestruturaSass,porexemplo,poderiahaverumarquivoúnico
queimportassetodosospartialsnecessários:
Fig.6.3:Exemplodeestruturacomarquivos.scss
Noiníciodoarquivo style.scss,colocaríamos:
79
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 86

6.7. MaissuperpoderesdeSass CasadoCódigo
@import
'base/base',
'base/fonts',
'base/forms',
'base/generics',
'layout/content',
'layout/footer',
'layout/header',
'layout/menu',
'module/button',
'module/pagination',
'module/search'
;
Cadaarquivoimportadopoderiatambémterdeclara çõesde @import,o
quecausariaumefeitoboladenevedeimporta çãoe,comooesperado,ainda
continuariacompilandosomenteoarquivo style.css.
6.7 M ais superpoderes deSass
Sasséumalinguagempoderosíssima,quefacilmenteencheriaumlivroin-
teiro,alémdoquejáfoiapresentado:
• Operadoresaritméticos(+, -, *, /);
• Estruturasdecontrole(if, while, for, each);
• Diferentesresultadosdecompilação( nested, expanded, compact, com-
pressed);
• Funçõespersonalizadas.
TudoissovocêencontranositeoficialdoSass(http://sass-lang.com/).
Parajáirbrincandoumpouquinhosemterqueinstalaraferramentariane-
cessáriaparasetrabalhar,acesseoSassMeister(http://goo.gl/aQYSpg).De-
poisdisso,paracontinuarosestudos,háartigosdegrandeutilidadeno The
Sass Way(http://goo.gl/GEjBGe).
80
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 87

CasadoCódigo Capítulo6. Pré-processadoresCSS
ParaaprimoraraindamaisaArquiteturaCSSdeseusprojetos,deuma
maneiraquepermitaumamelhoridentifica çãodasuaestruturaemanuten-
ção,nopróximocapítulo,vejasobre CSS Namespaces.
81
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 88

E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 89

Capítulo7
CSSnamespaces
Comovisto,SMACSS(4)eBEM(5)podemfazermaravilhaspelaarquitetura
eorganiza çãodeseusprojetos. Porém,épossívelirmaisalém! Esperoque
nãofiquesurpreso!
Emdiversaslinguagensdeprograma çãobastanteusadasnomundoin-
teiro,existeoconceitode namespaces.Algumasosuportamnativaeexplici-
tamente,como,porexemplo,amaioriadaslinguagensde backendmodernas;
mas,outras,comoJavaScript,nãooaceitam.Entretanto,épossívelfazeralgu-
masmaroticesnocódigo(leia-se:gambiarras)paraquenamespacingpossa
seraplicadoeconseguirseusbenefíciosintrínsecosobtidos.
Porém,oquesãonamespacesequaléasuafinalidade?
Tentandoexplicardemaneirasimplesesucinta,namespacessãocomo
regiõesnocódigo,nasquaisnomes devariáveis,defun çõesetc. sãoválidos
dentrodestaslinguagensdeprograma ção.Apesardenãotercertezaquantoà
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 90

7.1. OsCSSnamespacesmaiscomuns CasadoCódigo
acuidadedatradu ção,emterrastupiniquins,algunscostumamusarotermo
espaços de nomes.
Naprática,issoquerdizerque,dentrodedeterminado“espaçodenome”,
épossívelatribuirnomesainstânciaseentidadessemqueocorraalgumcon-
flitocasotermosidênticossejamescolhidosemoutrosespa çosdenomes.
Ouseja,torna-sepossívelusartermosidênticosdentrodenamespaces
diferentessemquehajaconfusão.Adicionalmente,essasuadiferencia çãotraz
avantagemextradeserpossívelidentificarimediatamenteaqualespa çode
nometalentidadepertencecomumsógolpedevista.
Evidentemente,nomomento,umCSSquenãosejaumalinguagemde
programaçãonãopodevaler-sedosbenefícioscompletosdenamespacing.
Mas,talcomoacontececomOOCSS(3),pormeiodealgumasconven ções
bastanteinteressantes,épossíveltrazerpartedosseusbenefíciosparaalin-
guagemetentarencontraralgumavantagemnisso.
Émaissimplesdoquevocêpoderiaimaginar.
EstecapítulonãoésobreoNamespaceModuledaW3C(http://goo.
gl/EoQjvt);massobreconven çõesdenomesdeclassesparaajudarna
leituraecompreensãodecódigos.
7 .1 O s CSS namespaces mais comuns
Comovocêdevesaber,pornãosetratardeumalinguagemdeprograma ção,
aplicarnamespacingemCSSépossívelatravésde convenções de nomes as-
simcomomuitodebomqueaconteceemCSS.Naprática,trata-seapenas
decolocarumprefixonosnomesdosseletoresparaconseguiratribuirum
namespaceecome çarasevalerdosbenefíciosdeimediataidentifica çãoe
melhorcompreensãodocódigo.
OsnamespacesdeCSSmaiscomuns mostradospor Harry Robertsem
umconhecidoartigoarespeito(http://goo.gl/917hCW) são:
•o-:objeto;
•c-:componente;
84
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 91

CasadoCódigo Capítulo7. CSSnamespaces
•u-:utilitário;
•t-:tema;
•s-:escopo( scope);
•is-/has-:estado/condi ção;
•_:hack(!);
•js-:JavaScript;
•qa-:qualityassurance(QA).
Sódeobservaressalista,jáépossívelperceberoquãomaiscomunicativo
seucódigopodeserao,simplesmente,prefixarosnomesdesuasclasses!Veja
maisdetalhessobrecadaumdosnamespacesaseguir.
Alémdisso,háumavantagemextra:usarnamespacesemCSScombina
perfeitamentecomBEM(5)! Querdizer,vocêpodecontinuarescrevendo
códigoCSScomBloco,ElementoeModificador,aprimorandoaarquitetura,
legibilidadeeentendimentodocódigo,somenteaousaressaconven çãode
prefixos!
Objeto: o-
Formato:
.o-object-name[<element>|<modifier>] {}
Exemplo:
.o-layout {}
.o-layout__item {}
.o-layout--fixed {}
Onamespace Objetoéespecialmenteútilparapessoasquesevalemdo
OOCSS,que,aestaaltura,vocêjádeveconhecerdepoisdeterlidoocapítulo
3.
85
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 92

7.1. OsCSSnamespacesmaiscomuns CasadoCódigo
DadoumprojetofictícioqueseguealgumasdasboaspráticasparaCSS
eficientejámostradas,imaginequesejaprecisoquesealtereo paddingdas
recomendaçõesdadasporpessoas,porexemplo.Encontra-seoseguintetre-
chodecódigo:
<blockquote class="media testimonial">
</blockquote>
Emrela çãoaoCSScorrespondente,foidecididocolocaro paddingem
.testimonialpararesolveraquestão. Dariacerto,mas,fazendoalguns
testes,opta-seporfazeraadi çãodapropriedadeem .media,jáqueissotraz
oresultadoesperado.
Agrandequestãonesseexemploéque .mediaésomenteumaabstra ção
deOOCSS.Eletemdemantersuascaracterísticasdeserreusáveledenãore-
ceber“cosméticos”quepoderiamalterarseuvisualdependendodeondeseja
colocado. Mesmoqueocódigomostradojátenhaaaplica çãodealgumas
técnicasdeCSSeficiente,épossívelmelhorá-loetorná-lomaisclaroecomu-
nicativo.
Bastariafazer:
<blockquote class="o-media testimonial">
</blockquote>
Somentecomaadi çãodoprefixodonamespaceObjeto,agoraocódigo
comunicaaqualqueroutrodesenvolvedorsobresuanaturezadeobjeto/abs-
traçãoetambémqueelenãodeveserestilizado.Issoevitariaaltera çõesne-
fastasnele.Logo,vemosque:
• Objetossãoabstratos;
• Objetospodemserusadosemqualquernúmeroaolongodoprojeto;
• Tenhacuidadoeatençãoredobradaquandosedepararcomelementos
o-.
86
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 93

CasadoCódigo Capítulo7. CSSnamespaces
Componente: c-
Formato:
.c-component-name[<element>|<modifier>] {}
Exemplo:
.c-modal {}
.c-modal__title {}
.c-modal--gallery {}
Onamespace ComponenteidentificaamaiorpartedoselementosdeUI
quequalquerumpodeolhareidentificarimediatamente,porexemplo:“Isso
éumbotão”,“Issoéummodal”etc.).AocontráriodeObjetos,alteraçõesde
estiloemComponentesnãoafetamnadaalémdocomponenteemsi,como
vemosnesseúltimoexemplo,nadaalémdomodal. Enquantoobjetossão
abstrações,componentessãoimplementa çõesespecíficas.
Paraaprimoraroexemplodadoanteriormente,bastaria:
<blockquote class="o-media c-testimonial">
</blockquote>
Sequandoasolicita çãodeaumentode paddingtivessesidofeitacom
essamarca çãopresente,imediatamentejáseteriapercebidoqueelaprecisaria
serfeitaa .testimonial,dadasuaprefixa çãodecomponente.Teríamosa
garantiadequetodaequalquermodifica çãorealizadaafetariasomentecom-
ponentes .testimonialenadamais!Assim:
• ComponentessãoimplementaçõesespecíficasdeUI;
• Podemosmodificá-losdemaneirasegura;
• Qualquercoisacomprefixoc-éalgoespecífico.
87
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 94

7.1. OsCSSnamespacesmaiscomuns CasadoCódigo
Utilitário: u-
Formato:
.u-utility-name {}
Exemplo:
.u-clearfix {}
Onamespace Utilitárioéusadopararegrasquetêmresponsabilidade
única,servindoapropósitosmuitoespecíficosediretosefazendouma,eso-
menteuma,coisa.Porexemplo, .u-text-centerparaalinharaocentro
umtexto.Nãoéincomumquetenham !importantparagarantirquega-
nharãonabatalhadaespecificidadeCSS(2.1).
Devidoàsuanaturezadeestiliza çãofocada,excepcional,única,diretae
quetambémpermitesuautiliza çãoglobalmentenoprojeto,émuitoimpor-
tanteusaresseprefixoquandoestevale-sedenamespacesCSS.
Porexemplo,vejaestetrechodecódigo:
.footer .text-center {
font-size: 75%;
}
Oproblemaéque .text-centeragoratemduasresponsabilidades
quandoapareceemqualquerlugardentrode .footer. Issocausaefeitos
colaterais,algoqueumutilitáriojamais jamais! podeter.
IssonostrazaumaconclusãoóbviaarespeitodousodonamespaceUti-
litário:secomeçacom u-, jamais reatribua!Utilitáriosdevemserdefinidos
umavezparanuncamaisprecisaremseralterados.
VejaesteexemplodeHTML:
<div class="font-size-large">
<blockquote class="pullquote">
</blockquote>
</div>
Somenteolhandoparaocódigo,podeserconfusoparaumdesenvolvedor
perceberoporquêdeotamanhodafontedo blockquoteserdiferentedo
88
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 95

CasadoCódigo Capítulo7. CSSnamespaces
queestavasendoesperado.Omotivoéqueeleestáherdandoessetamanho
de .font-size-large.
Vejacomoépossívelclarearocódigoegarantirqueestetipodedúvida
nãoocorra,somenteusandoprefixosdenamespacesdeCSS:
<div class="u-font-size-large">
<blockquote class="c-pullquote">
</blockquote>
</div>
Logo,vimosque:
• Utilitáriossãoestilosdapesada!
• Alerteaoutrosdesenvolvedoressobreeles,colocandooprefixo u-.
• Nuncaosreatribuaaqualquerelementoquetenhaumprefixo u-.
T ema: t-
Formato:
.t-theme-name {}
Exemplo:
.t-light {}
Onamespace T ema,comosugereopróprionome,éparaauxiliarnamar-
caçãoHTMLenacria çãodeseletoresCSSemprojetosquesuportamtemas.
Amaioriadosprojetosquesuportamtemastrabalhamcomoconceito
de StatefulThemes(http://goo.gl/Vrpyt0).Querdizer,temasquepodemser
habilitadosedesabilitados;porexemplo,penseemsitesqueemcadapágina
ouse çãotemumapaletadecoresouumseletordetemasnumpaineldecon-
troles.Geralmente,issoéfeitocolocando-sealgumaclassequeindicaqueo
temaestánoelemento body.
Valendo-nosdoquefoivistosobrepré-processadoresCSS(9),épossível
pensaremcódigoscomo:
89
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 96

7.1. OsCSSnamespacesmaiscomuns CasadoCódigo
.c-btn {
background-color: #333;
color: #e4e4e4;
display: inline-block;
padding: 1em;
.t-light & {
background-color: #e4e4e4;
color: #333;
}
}
Ouseja,oelemento .c-btnpossuideterminadoestiloporpadrão,mas,
quandootemalightestáativo aclasse .t-lightécolocadanoelemento
body,ascoresdebackgroundeforegroundinvertem-se.Comomostrado,a
vidaaindaficamuitomaisfácilaoutilizarpré-processadores.Casoseprecise
editaroaspectodealgumelementoemumtemaespecífico,jásesabeonde
encontrarsuadefini ção,umavezqueficamtodasvinculadasaoelementopa-
drão(nomesmoarquivo).Assim:
• Namespacesdetemasãodealtonível;
• Elesproveemcontexto/escopoparadiversasoutrasregras;
• SãoúteisparasinalizaracondiçãoatualdaUI.
Escopo: s-
Formato:
.s-scope-name {}
Exemplo:
.s-cms-content {}
Onamespace Escopo(scope)deveserusadosomenteemalgunscasos
bastanteespecíficos. Prestemuitaaten çãoparanãousá-lodemaneiraina-
propriada.
90
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 97

CasadoCódigo Capítulo7. CSSnamespaces
Namaioriadasvezes,escopopodeserutilizadoparaespecificarumcon-
textoparaalgumase çãoparticulardaUI.UmexemploseriaocódigoHTML
geradoporumCMSque,sabemos,nemsempreédamelhorqualidade.Você
podeutilizarumnamespacedeescopocomoumcontêinere,comapor ção
deelementoscontextualizada,estilizarapartirdaí.
Umapor çãodecódigodeexemplo:
<nav class="c-nav-primary">
...
</nav>
<section class="s-cms-content">
<h1>...</h1>
<p>...</p>
<p>...</p>
<ul>
...
</ul>
<p>...</p>
</section>
<ul class="c-share-links">
...
</ul>
<a href="#" class="c-btn c-btn--primary">
Pr&oacute;ximo artigo
</a>
Vejaque .s-cms-contentservecomoumcontêinerparaoconteúdo
automáticogeradoe,comisso,abre-seapossibilidadedeumaestiliza çãofina
paraadequá-loàsdiretrizesdeUIdoprojeto.
Umexemplo(comSass):
.s-cms-content {
91
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 98

7.1. OsCSSnamespacesmaiscomuns CasadoCódigo
font: 16px/1.5 serif;
h1, h2, h3, h4, h5, h6 {
font: bold 100%/1.5 sans-serif;
}
a {
text-decoration: underline;
}
}
Comovocêjádevesaberaestaaltura,estilizarelementosdiretamente
nãoéláconsideradoumaboapráticaparaseterCSSeficiente. Porém,em
casoscomoesse,nãodeixadeserumasolu çãoaceitávelparaconseguir-se
umaestiliza çãoapropriada.
EmvirtudedissoedosproblemasdeCSSquepodemaparecerporcon-
sequência,éimportantelembrarqueonamespaceEscopodeveserusadocom
cautelaesomentequandorealmentenecessário.Portanto:
• Escoposdevemserraramenteusados,logo,tenhacertezaabsolutade
queprecisadeles;
• Elesdependeminteiramentedeaninhamento;estejacientedisso.
Estado/Condição: is-/has-
Formato:
.[is|has]-state {}
Exemplos:
.is-open {}
.has-dropdown {}
Onamespace Estado/ CondiçãoadvémdoSMACSS(4)e,comoexpli-
cado,serveparaindicarestadostemporáriosdaUIqueprecisamserestiliza-
dosdeacordocomessacondi ção.
92
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 99

CasadoCódigo Capítulo7. CSSnamespaces
Nãoraramente,aousaruminspetordecódigo(porexemplo,Chrome
DevTools)parasabermaissobrealgumelementointerativodeUI,comoum
modal,écomumvermosclasses/elementosaparecendoedesaparecendo,“li-
gando”e“desligando”.Aoinspecionar-seumcódigo,ébastanteesclarecedor
verumaclassecomo is-openapareceredesaparecer,poisinformadema-
neiramuitoclaraoqueestáacontecendonaqueletrechoespecíficodainter-
face.
<div class="c-modal is-open">
...
</div>
TambémnãosomentequandoseolhaparaoHTML.Aoolharparaum
arquivodeestiloscomessenamespace,tudoficamuitomaisclaro.
.c-modal {
&.is-open { ... }
&__content {
&.is-loading { ... }
}
}
Algoimportanteasaberéqueumestado/condi çãodiferencia-sedeum
ModificadordeBEM(5)devidoàcaracterísticadesertemporário.Ouseja,
umestado/condi çãopodemudardeummomentoparaooutro,devidoaal-
gumaa çãotomadapelovisitante(porexemplo, .is-expanded)oualguma
interaçãocomoservidor,como .is-updating.Logo,vimosque:
• Estado/condiçãoétemporário;
• Certifique-se de que sejam facilmente percebidos e entendidos no
HTML;
• Nuncaescrevaumaclassedeestado/condi ção“pura”. Eleésempre
atreladoaoutra.
93
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 100

7.1. OsCSSnamespacesmaiscomuns CasadoCódigo
Hack: _
._<namespace>hack-name {}
Exemplo:
._c-footer-mobile {}
Onamespace Hack,devidoaseupróprionomeeobjetivoquedecorre
daí,deveserusadosomenteemcasosraros. Teressamarca çãonocódigo
ajudatodosaidentificarquesetratadeumhackque(teoricamente)deveser
resolvidodemaneirasconvencionais,assimquepossível.
Exemplo:
@media screen and (max-width: 30em) {
// É preciso forçar o footer a ter uma largura fixa
// em viewports menores
._c-footer-mobile {
height: 80px;
}
}
Resumindo:
• Hackssãofeios;
• Hacksdevemsertemporários,portantonãofaçareúsoouvincule-osa
suasclasses;
• Fiqueatentoaonúmerodehacksnocódigo.
JavaScript: js-
Formato:
.js-component-name {}
Exemplo:
.js-modal {}
94
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 101

CasadoCódigo Capítulo7. CSSnamespaces
Onamespace JavaScript,comovocêdeveimaginar,indicaqueháalgum
tipodeintera çãocomJavaScriptassociadaaoelementoemqueseencontra.
Emteoria,nãosedeveterestiloecomportamentoassociadosaomesmo hook
nocódigo,logo,geralmenteessenamespaceéusadoparafazera separação
de preocupações (Separation of Concerns).
Usá-lotambémtrazumatranquilidadeextraaoprojeto,jáquedesen-
volvedorespodemmexernoCSSàvontadesemsepreocuparcomalguma
possívelquebraemJSevice-versa.
Portanto,naprática,classescomo .js-modalpoucotêmavercomCSS
eestiliza ção,servindomaiscomohooksJavaScript,propriamenteditos.De-
pendendodoguiadeestilosadotadoeconven çõesdaequipe,nadaimpede
quesejam .jsModal.Assim:
• JavaScripteCSStêmpreocupaçõesdiferentes( Separation of Concerns),
entãousehooksdiferentes;
• TendohooksdiferentesparaCSSeJS,acodificaçãoemcadaumdeles
torna-semaissegura.
Quality Assurance (QA): qa-
Formato:
.qa-node-name {}
Exemplo:
.qa-error-login {}
Onamespace Quality Assurance (QA),apesardenãoseromaisusado
dalista,podeserextremamenteútilevaliosoquandoseestátrabalhando
comtestesdeUIecomferramentasdeautomatiza çãocomo Selenium(http:
//goo.gl/N7523e).Ouatémesmocomumnavegador headless,emqueéex-
tremamentecomumscriptsdotipo:
1) Visitesite.dev/login;
2) Insiraumnomedeusuárioincorreto;
95
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 102

7.2. Conclusão CasadoCódigo
3) Insiraumasenhaincorreta;
4) Espere(Expect)porumerronoDOM.
Atéaqui,nenhumanovidade. Mas,pensebem: seostestessãofeitos
usandocomohooksnomesdeclassesCSS eéissomesmooquegeralmente
acontece,umasimplestrocadenomespodefazercomqueelescomecema
falhar!
Fazendoumparalelocomonamespace js-,aquitambémseriaconve-
nientequeacontece-seumasepara çãodepreocupa ções.Issopermitiriaque
diferentespessoasouequipespudessematuardemaneiraindependente,fa-
zendooquequerquefossepreciso.
Paramelhorarasitua ção,umamedidainteressantíssimaasertomadaé
começarausaronamespaceQAe,paraosquefazemostestes,autilizaressas
classescomohooks;emvezdasnormaispresentesnocódigo,ficandocom
classescomonesteexemplo:
<strong class="c-message c-message--error qa-error-login">
Resumindo:
• Usarhooksdeestiloparatesteséumtantoobscuro,então,nãofa ça
isso;
• Use-oscomohooksclassesespecíficasparatestes;
• GarantaquequalquerrefatoraçãodeUInãoafeteoshooksdeQA.
7 .2 C onclusão
ComomuitasdasboaspráticasdeCSS, CSS Namespacesnadamaissãodo
queconven çõesdecodifica çãoque,sebemusadas,trazemnumerosasvan-
tagensaosprojetosquesevalemdelas,almejandoumCSSeficiente. Tecni-
camente,sãoapenaspseudonamespaces,mas,dequalquerforma,dentrodas
atuaislimita çõesdeCSS,ajudambastante.
Existematévantagensnãoexplícitas,comoofatodeconseguir-semais
produtividadecomeditores/IDEscom autocomplete.
96
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 103

CasadoCódigo Capítulo7. CSSnamespaces
Fig.7.1:Poressavocênãoesperava!
Se,porqualquermotivo,sejaprecisodestacarvisualmenteumoumais
namespaces,issotorna-sepossívelcomumasimplesregras,como:
[class^="c-"],
[class*=" c-"] {
outline: 5px solid red;
}
Alistadenamespacesapresentadosnãoéfixaenemimutável,sórefleteo
queémaiscomumenteusadoporaí,enquantovocêestálendoestaspalavras.
Apesardenãoserúnica,comosepodeverem FUN(http://goo.gl/G0cWkX)
eoutraspropostasexistentes.
DevidoàfacilidadedeaprendizadoedeusodeCSSNamespaces,soma-
dosaosimensosbenefícioseganhosquesãotrazidosaosprojetos,realmente
nãohámotivosparaqueosnamespacestambémnãofa çampartedoseurol
deconven çõesCSS,apesardeserpossívelusarsomenteoutrasdastécnicas
deCSSeficientemostradasnolivro.
Automatizartarefasésemprealgobomasefazerecertamenteusar Task
Runnersemseusprojetoséumpassointeligenteaserdado,oqueveremosa
seguir.
97
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 104

E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 105

Capítulo8
TaskRunners
Sevocêestiverlendoestelivrosequencialmente,vocêjáviuCSSorientadoa
objetos(3),SMACSS(4),BEM(5),pré-processadoresCSS()eCSSnamespa-
ces(7).UmbelocaminhorumoàescritadeCSSmaiseficiente!
Algoquepodepassaressaeficiênciaaumoutroníveléa automatização.
Ébastantecomumosdesenvolvedoresteremdefazertarefasrepetitivas,seja
aoiniciarprojetosoudurantetodoseuciclodedesenvolvimento.Muitasde-
lassãorecorrentes,tendodeserexecutadasatodomomento,porexemplo,
compilarSassparaCSS.
Felizmente,épossíveldarumpassoalémnaeficiênciaeprodutividade
front-endpormeiodosautomatizadoresdetarefas,maisconhecidoscomo
Task Runners.
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 106

8.1. OquesãoTaskRunners? CasadoCódigo
8.1 O que são Task Runners?
Comojácitado,taskrunnerssãoferramentasquesedestinamaautomatizar
tarefasvariadasquedevemaconteceremdeterminadosmomentosdodesen-
volvimento.Issovaletambémparaoback-end,apesardenãoserofocodeste
livro.
TarefascomocompilarCSSdepré-processadores,verificarerrosdeJavaS-
cript,combinareminificar assets,otimizarimagens,emuitasoutraspodem
serautomatizadas!Sim,elaspodemserexecutadaspelostaskrunnersdema-
neiratransparenteeindolor,fazendocomqueaprodutividadedaspessoas
envolvidasnoprojetoatinjalimitesnuncaantesimaginados!
Elespermitemquesecriemtarefasquepodemserchamadaseexecutadas
atravésdalinhadecomando,alémdeficaremrodandoembackground,só
esperandovocêsalvardeterminadotipodearquivo,paradarinícioàexecu ção
deumasériedeinstru çõesautomatizadas,previamenteprogramadas!
Parecebomdemaisparaserverdade,masrealmenteé!
Grunt e Gulp
Demaneirasemelhanteaospré-processadoresCSS(),nomundodaauto-
matizaçãodetarefas,tambémhádoistaskrunnersquesãousadospelamai-
oriadaspessoas:
• Grunt(http://gruntjs.com/);
• Gulp(http://gulpjs.com/).
Naprática,ambospodemexecutarasmesmastarefasecontamcomquase
amesmagamadepossibilidades.Oquerealmentemudaéamaneiracomose
escreveecomosedãoasinstru ções,paraquecadaumfa çaoquedevefazer.
Grunttemsintaxemaisparecidacomumarquivodeconfigura ção,sendo
maisverbosoe,consequentemente,gerandoarquivosmaiores. Gulp,por
suavez,remetemaisaquemgostadedarinstru ções,deprogramarmesmo,
tendocomocaracterísticasprincipaisumasintaxemaisenxutaeperformance
espantosa. Estamos falando demicrossegundos e, caso não saiba,1s =
1.000.000s!
OGulpbaseia-seemalgunsprincípiosbásicos:
100
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 107

CasadoCódigo Capítulo8. TaskRunners
• Fácildeusar:aopreferircódigo,emvezdeconfigura ção,elemantém
simplesoqueésimplesefaztarefascomplexasbemmaisadministrá-
veis;
• Eficiente: Gulpusaopoderdestreamsde Node.js,oquepermite
buildsmuitomaisrápidosedispensaanecessidadedegrava çãodear-
quivosintermediáriosemdisco;
• Altaqualidade:asdiretrizesestritasparapluginsdoGulpgarantemque
elespermane çamsimplesetrabalhemdamaneiraqueseespera;
• Fácildeaprender:comumaAPImínima,aprende-seatrabalharcom
elequasequenahora!
Códigoemvezdeconfigura ção( code over configuration)significaquere-
almenteéprecisoprogramar,montarscripts.
AeficiênciadoGulpmuitosedáemfun çãodeesteusarstreamsdoNode
(http://goo.gl/gGcxVW).Tecnicamente,streaméumainterfaceabstrataim-
plementadaporváriosobjetos.Porém,pensenelescomoospipesdesistemas
*NIX,emqueépossíveljogaroresultadodeumcomandodiretamenteem
outro.
Suaaltaqualidadeefacilidadedeaprendizadogarantempluginsigual-
menteeficientes.Também,devidoaoprópriomodocomooGulpfunciona,
essafacilidadedeaprendereusarsãoabsurdas;éumacurtíssima(quaseine-
xistente)curvadeaprendizadoparacome çaramexercomumadasmaispo-
derosasferramentasdedesenvolvimentofront-endquesurgiramnosúltimos
tempos!
Emvirtudedessascaracterísticasedomeugostopessoal,atéofimdo
capítulo,seráfocadonoGulp.Entretanto,lembre-sedequeépossívelrealizar
tudooqueserámostradotambémcomoGrunt,alterandoeadaptandouma
coisaaquieali.
8.2 C omo instalar o Gulp
GulpéJavaScriptcomNode.Aprimeiracoisaquevocêprecisaráéinstalaro
Node.jsinstruçõesemhttp://nodejs.org/.Tomandoporbasequevocêestá
101
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 108

8.2. ComoinstalaroGulp CasadoCódigo
mexendoemumsistemadegentegrande,issoétãosimplesquandodigitar
umalinhadecomandonoterminal(casojáaténãootenhainstalado).Depois
disso,instaleoGulpglobalmentenosistemacom:
npm install -g gulp
JáqueestamoslidandocomNode,umarquivo package.jsonnaraiz
doprojetofaz-senecessárioparaindicarquaismódulosserãousados.Épos-
sívelqueoNodeocrieautomaticamentecom npm init,oqueiniciaráum
promptinterativoqueperguntaráummontedecoisas(taiscomo:nomedo
projeto,versão,descri ção,licen ça,autoretc.). Naverdade,paracome çara
adicionarmódulos,sóéprecisoqueessearquivosejaumJSONválido(mais
sobreJSONemhttp://goo.gl/bofIoU). UmJSONválidomínimonãopassa
de {}.Casoqueirasermaisprático,bastaexecutar:
echo "{}" > package.json
Jácomoarquivo package.jsonnaraizdoprojetocomumJSONvá-
lido,execute:
npm install --save-dev gulp
Comisso,oGulpjáestáinstaladoeprontoparaserusadonoprojeto.
Revisando:
•npm install -g gulp
•echo "{}” > package.json
•npm install --save-dev gulp
Depoisdisso,seu package.jsondeveestarassim(logicamente,aver-
sãopodesealterar):
{
"devDependencies": {
"gulp": "~3.8.10"
}
}
102
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 109

CasadoCódigo Capítulo8. TaskRunners
Comovocêviu, parainstalarmódulos, ocomandoé npm install
--save-dev [MÓDULO].Naverdade,ainstala çãopropriamenteditadis-
pensaousode --save-dev,masusaresseparâmetrogarantequeadefi-
niçãodomódulosejagravadano package.json.Issotornaascoisasmais
fáceisaoseiniciarumprojetoqueusaGulp.
Casoestejausandocontroledeversão,nãoéprecisoincluirodire-
tório node_modules,jáque,aoseclonarumprojetoquetenhaum
package.json,bastaexecutar npm install paraqueelesejacriado
automaticamentejuntocomosmódulos/dependênciasqueserãousa-
dos.
gulpfile.js
AgoraqueobásicoparasemexercomGulpestápreparado,éhorado
gulpfile.js. Nessearquivo,quetambémdeveficarnaraiz,éondeos
scriptsdastarefasinstaladasconstam.Éaqui,efetivamente,queoscomandos
sobreoquefazerecomofazersãopassadosparaoGulp.
Um boilerplateparao gulpfile.jspoderiaser:
var gulp = require('gulp');
gulp.task('default', function() {
// Tarefas
});
Primeiramente,requere-seomódulo gulp.Issodeveserfeitocomtodos
módulosquevocêpretendeusar.Depois,cria-seumatarefa defaultcom
asinstru çõesqueserãorealizadascomsuaexecu ção.Dojeitoqueestá,você
jápodeexecutarnoterminal: gulp.
Apesardeserumatarefanadaútil,elajádeveretornaralgocomo:
[gulp] Using file [...]/gulpfile.js
[gulp] Working directory changed to [...]
[gulp] Running 'default'...
[gulp] Finished 'default' in 85 s
103
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 110

8.3. GulpAPI CasadoCódigo
Atente-seàmaneiradeexecutarumatarefa,queéusar gulpseguidode
seunome.Porexemplo,sevocêtivessecriadoumatarefa concatAssets,
vocêaexecutariacom gulp concatAssets. Nocaso,funcionouexecu-
tandosomente gulp,porquefoiusadoumnomedetarefaespecial.Quando
umatarefa defaultestádefinida,éelaqueseráexecutadacasonenhum
outronomesejapassado.
8.3 G ulp API
JáestáclaroqueumdosprincípiosnorteadoresdoGulpéasimplicidade.
Indoaoencontrodisso,suaAPIéextremamentesimpleseenxuta,limitando-
seaquatrofun çõesprincipais:
•src():arquivo(s)queentrará(ão)nasequênciadepipesparaserem
tratados/manipulados;
•task():definetarefasnoGulp;
•dest():destino(s)do(s)arquivo(s)quepassoupelospipes;
•watch():observaarquivo(s)efazalgumacoisaquandoesse(s)é(são)
alterado(s).
Obviamente,cadaumtemsuasop ções,possibilidadeedetalhestécni-
cos. Apesardeessasbrevespalavrassobrecadajádaremumano çãoso-
breasrespectivasfun ções,seriainteressanteolharapáginadaAPIdoGulp
(http://goo.gl/7cviok).
8.4 E xemplo de tarefas com Gulp
Basicamente,vocêjásabecomotrabalharcomGulp!Apartirdeagora,éusar
osmódulosGulpdisponíveis(e,quemsabe,atécriaralguns)econheceras
peculiaridadesdeusodecadaum.Umexemplovaiajudaraclarearascoisas
efixaroconhecimento.
OGulp,paraesteexemplo,vaitrabalharcomosmódulos:
•gulp-ruby-sass:paracompilarSass(http://goo.gl/Qbf0hq);
104
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 111

CasadoCódigo Capítulo8. TaskRunners
•gulp-autoprefixer:paracolocarautomaticamente vendor prefixes
emseletores(http://goo.gl/eCrNp5);
•gulp-minify-css:paraminificarCSS(http://goo.gl/Ln6JL3);
•gulp-livereload: para recarregar a página automaticamente
quandoumarquivoforsalvo(http://goo.gl/tK9Lak).
Paradescobrirmaispluginsemódulos,acessehttp://gulpjs.com/plugins/.
Usandoafun ção watch()doGulp,tudoissovaiacontecer automati-
camenteaosesalvaralgumarquivoSass.
Instalando módulos Gulp
Parainstalarosmódulosnecessáriosaoexemplo:
npm install --save-dev gulp-ruby-sass gulp-autoprefixer
gulp-minify-css gulp-livereload tiny-lr
Valelembrarque,parausaro gulp-ruby-sassqueésóumpouquinho
maislentoque gulp-sass(http://goo.gl/I8D18V),maspossuiop çõesmais
interessantes,éprecisoquevocêtenhaRubyinstalado.
TambéméprecisoteraextensãoLiveReloadparaChrome(http://goo.gl/
FXPwAL),poiso gulp-livereloadusa tiny-lr.Porisso,eleconstana
listademódulosasereminstalados.
Fig.8.1:ÉprecisohabilitaroLiveReloadnoChrome
Depoisderodarocomando,seu package.jsondeveestarparecido
com:
105
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 112

8.4. ExemplodetarefascomGulp CasadoCódigo
{
"devDependencies": {
"gulp": "~3.8.10",
"gulp-ruby-sass": "~0.7.1",
"gulp-autoprefixer": "2.1.0",
"gulp-minify-css": "~0.4.3",
"gulp-livereload": "~3.6.0",
"tiny-lr": "0.1.5"
}
}
Estrutura do projeto-exemplo
Paraesseprojeto-exemplo,considereaseguinteestrutura:
Fig.8.2:Exemplodeestruturadediretórios
index.html:
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Gulp test</title>
<link href="style.css" rel="stylesheet">
</head>
<body>
<p>Texto do teste.</p>
106
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 113

CasadoCódigo Capítulo8. TaskRunners
</body>
</html>
_variables.scss:
$backgroundColor: tomato;
$defaultTextColor: #fff;
style.scsss:
@import 'variables';
body {
background-color: $backgroundColor;
color: $defaultTextColor;
}
Editar o gulpfile.js
Agoraseráprecisoeditaro gulpfile.jsparaquefiqueadequadoaos
propósitosdoprojeto-exemplo.Paracome çar,éprecisorequererosmódulos
eosatribuirasuasrespectivasvariáveis:
var gulp = require('gulp'),
sass = require('gulp-ruby-sass'),
prefix = require('gulp-autoprefixer'),
minifycss = require('gulp-minify-css'),
refresh = require('gulp-livereload'),
server = require('tiny-lr')();
Repareque,parao gulp-livereloade tiny-lr,foramdadosnomes
devariáveisdiferentes,emborasejaumaconven çãonomearumavariávelcom
onomedomóduloqueelarecebe;daquiapoucovocêvaientender.
Agora,chegouomomentodeindicaraoGulpoquefazer,efetivamente.
Lembre-sedospipes:o(s)arquivos(s)indicado(s)em src()passa(m)por
umcomandoeoresultadodissoéjogadoparaopróximo,eassimpordiante.
gulp.task('compileStyles', function() {
gulp.src('src/style.scss')
107
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 114

8.4. ExemplodetarefascomGulp CasadoCódigo
.pipe(sass({
noCache : true,
precision : 4,
unixNewlines : true
}))
.pipe(prefix('last 3 version'))
.pipe(minifycss())
.pipe(gulp.dest('dist'))
.pipe(refresh(server));
});
Percebaqueháop çõesdefinidaspara gulp-ruby-sass.Issoéperfei-
tamentenormalparaváriosmódulosGulp.Geralmenteoqueestádisponí-
velequaisasop çõespossíveissãoinforma çõesdisponibilizadasnaprópria
páginadomódulo.Também,vejaomotivodeaquelasvariáveisteremrece-
bidonomesdiferentesdonomedomódulo:ficamaisentendívelquandose
lêrefresh(server),nãoéverdade?
Finalmente,apartemágicaqueautomatizainclusiveorecarregardepá-
gina,poupandoatédeterquedarofoconajaneladonavegadoreapertar F5
oupior:clicarnobotão Recarregar.
gulp.task('watch', function() {
server.listen(35729, function( err ) {
if ( err ) { return console.log( err ); }
gulp.watch('src/**/*.{sass,scss}', [
'compileStyles'
]);
});
});
Atarefachamada watchiniciaumservidorLiveReload,escutandona
porta35729(aportapadrãodesseserver)ecolocandonoconsolealgumacon-
tecimentoinesperado. Ofilémignonéapartequeindicaque,casoqual-
querarquivoSasssejaalteradoemqualquerpartedodiretório src,atarefa
compileStylesdeveserexecutadaeapáginarecarregada. Afinal,épara
issoqueoLiveReloadserve.
Oarquivo gulpfile.jsfinaldeveparecer-secom:
108
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 115

CasadoCódigo Capítulo8. TaskRunners
var gulp = require('gulp'),
sass = require('gulp-ruby-sass'),
prefix = require('gulp-autoprefixer'),
minifycss = require('gulp-minify-css'),
refresh = require('gulp-livereload'),
server = require('tiny-lr')();
gulp.task('compileStyles', function() {
gulp.src('src/style.scss')
.pipe(sass({
noCache : true,
precision : 4,
unixNewlines : true
}))
.pipe(prefix('last 3 version'))
.pipe(minifycss())
.pipe(gulp.dest('dist'))
.pipe(refresh(server));
});
gulp.task('watch', function() {
server.listen(35729, function( err ) {
if ( err ) { return console.log( err ); }
gulp.watch('src/**/*.{sass,scss}', [
'compileStyles'
]);
});
});
Comessasquase30linhasdecódigo,agoraépossívelabrir index.html,
executar gulp watch,ativaraextensãoLiveReloadnonavegador,epartir
paraoabra ço(leia-se:editarumarquivoSassem src).Quasequeinstanta-
neamente,vocêveráasalteraçõesaparecendonateladeseunavegador.
AgoravocêentendeaquelespreceitosdoGulp: Velocidade, Eficiênciae
Simplicidade.
109
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 116

8.5. SugestõesdepluginsGulp CasadoCódigo
8.5 S ugestões de plugins Gulp
Existemcentenasdemódulos/pluginsparaoGulpe,acadadia,maisemais
aparecempelaweb. Nãoseriaviávelmanterumalistacompleta,mas,cer-
tamente,algumasindica çõesdemódulosúteisparatarefascomunsébem-
vinda.
•gulp-util:fun çõesúteisvariadas(http://goo.gl/fH3Qhq);
•gulp-jshint: detecta erros e problemas potenciais de JavaScript
(http://goo.gl/9GG5JQ);
•gulp-uglify:minificaarquivos(http://goo.gl/iVLc8p);
•gulp-imagemin:minifica/otimizaimagens(http://goo.gl/GT8rNO)
;
•gulp-replace: substitui strings em arquivos (http://goo.gl/
tuhD8v);
•gulp-concat:concatenaarquivos(http://goo.gl/UGpyfZ);
•delete-files-folder:removearquivosediretórios(http://goo.gl/
OV2SCB);
•gulp-rev:adicionahashaleatórioemnomesdearquivos(http://goo.
gl/9HTXri).
8.6 C onclusão
Kronoséimplacável, principalmentequandosetratadedesenvolvimento
web. Nãohácomoevitarquenovastecnologiasapare çamcomnovaspro-
postas,solicitandoumanovamaneiradepensarefazer,afimdetentarsanar
problemasjáconhecidos.Esteé,precisamente,ocasodoGulp:comainten-
çãodeajudarnaautoma çãodetarefasrepetitivaseliberaramentecriativa
dosdesenvolvedores,éumadasmelhoresemaiseficientesferramentaspara
front-enddosúltimosanos!
110
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 117

CasadoCódigo Capítulo8. TaskRunners
Aprofundeseusconhecimentosnaferramentaecertamenteperceberá
que,quandotiverseacostumadoàsfacilidadeseaoimensoganhodepro-
dutividadeproporcionadopelostaskrunners,nãotemcomovoltaratrás!
Agora,quetalconhecerumaformainovadoradeorganizarsuaArquite-
turaCSSpormeiodeumametodologiainéditanoBrasil? Conhe ça ITCSS
nopróximocapítulo.
111
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 118

E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 119

Capítulo9
ITCSS
Nestepontodolivro,vocêjáconheceuCSSorientadoaobjetos(3),SMACSS
(4),BEM(5),pré-processadoresCSS(),CSSnamespaces(7)eváriaspráticas
edicassobrecomoescreverCSSmaiseficiente.
Sãoconhecimentos/técnicasquepodemserusadoseaplicadosconforme
anecessidadedecadaprojetoou,melhor,comoumknow-howdetécnicas
quepodemserusadasemqualquercombina çãoparaquevocêconsigalevar
aarquiteturaCSSdelesparaopróximonível.
Porfalarempróximonível,algonovochegouaomundodasboaspráti-
casdeCSS;algobastanterecenteque,comexclusividadeeemprimeiramão,
sendotratadapelaprimeiravezemumapublica çãonacional,vocêvaiconhe-
ceragora: Inverted Triangle CSSou ITCSS.
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 120

9.1. OqueéITCSS? CasadoCódigo
9.1 O que é ITCSS?
ITCSSéumametodologiacriadapor Harry Robertsquevemsendotraba-
lhadaeaprimoradapormaisde4anos,atravésdeexperiênciasemprojetosde
front-enddegrandeporte.Lembra-sedequalfoiarespostadopróprioHarry
quandopergunteiporqueumaarquiteturaCSSeraimportante?Refrescando
suamemória,foi:
CSS é incrivelmente fácil de escrever incrivelmente fácil , mas possui uma
ordem de magnitude mais difícil para se gerir, manter e escalar. Como os proje-
tos ficam mais maduros e maiores, CSS pode realmente começar a “comer pelas
beiradas”, causando quantidades incalculáveis de confusão, dores de cabeça e
frustrações para os desenvolvedores responsáveis por geri-los.
Isso se dá, principalmente, devido a uma série de princípios fundamentais
de CSS que tornam inerentemente mais difícil a gestão de qualquer projeto de
UI não trivial.
Consulteocapítulo1ereleiaarespostacompleta.
Pensandojustamentenessetipodelimita çãoinerenteàsCSSfoique
Harrycriou ITCSS.Comosugereopróprionome,éarepresenta çãoabstrata
daarquiteturaCSSdeumprojetopormeiodeumtriânguloinvertido.Esse
triângulopossuicamadasque,conformeavan çam,tornam-semaisespecífi-
casefocadasemrealizartarefas.
ITCSSnãoéumanovatecnologiaaseraprendida,tampoucoalgumpro-
gramaquesedevainstalar.Trata-sedeumametodologiaouummodelo ou,
diriamalguns,um metaframeworkbastantesimplesdesetrabalhar,quepro-
põeumaarquiteturaCSSdiferenteemaiseficiente.
114
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 121

CasadoCódigo Capítulo9. ITCSS
Fig.9.1:Triânguloinvertidodivididoemcamadas
AlgunsdosprincipaisbenefíciosdeusarITCSSsão:
• Porsersimplíssima,éumametodologiaacessívelaqualquerum;
• Organizaegerenciaocódigoemcascata;
• Criaumaorganização,naqualsesabeondecadapartedocódigodeve
estar;
• Reduzperdaseredundânciadecódigo;
• EvitadoresdecabeçacomespecificidadeCSS(2.1).
Parecemuitobomparaserverdade,masacredite:simplesmenteé!
9.2 A s camadas do triângulo invertido
As7camadasdotriânguloinvertidosão:
•Configurações (Settings):variáveiseconfigura çõesglobais;
115
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 122

9.2. Ascamadasdotriânguloinvertido CasadoCódigo
•Ferramentas(T ools):fun çõesemixins;
•Genérico(Generic):estilosgenéricos(resets,normalizesetc.);
•Elementos(Elements):estiliza çãodeelementosHTMLdiretamente;
•Objetos(Objects):padrõesnãocosméticos(maissobreOOCSSem3);
•Componentes(Components):pe çasdeUIisoladas(menudropdown,
carouseletc.);
•Trumps:utilitários,helpers,sobrescritasehacks.
Fig.9.2:Camadasdotriânguloinvertido
116
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 123

CasadoCódigo Capítulo9. ITCSS
Percebaque Trumpsnãotevetradu ção.Naverdade,opróprioHarry
Robertsexplicaqueestaéumapalavraque,eminglês,ésinônimode
beat,que,nessecontexto,seriaalgocomo ultrapassar alguém ou al-
guma coisa por dizer ou fazer algo melhor.
Parafinsdeconcisãoeestilo,acreditoque,quandoITCSSformais
popularnaTerradosPapagaios,nãohaverámaioresquestõesemconti-
nuarusandootermo Trumpsqueéatébemsimpáticoeagradáveldese
pronunciar,diga-sedepassagem.
Alémdestaorganiza çãomaisformal,ITCSSénorteadoporalgunsprin-
cípiosgerais:
• SemusodeIDs,somenteclasses;
• Criaçãomodulardecomponentes,emvezdepáginas;
• UsoeabusodeclassesnoHTML(nadadeeconomiadecaracteres
aqui).
Para complementar sua robustez, ITCSS é construída em cima de 3
métricas-chave:
•Geral para explícito: começa-sepelosestilosmaisgeraisegenéricos
possíveise,apartirdaí,vão-secolocandocamadasdeestiloadicionais;
•Baixa Especificidade para alta Especificidade:regrascomespecifici-
dademenoraparecememcamadasmaisgenéricas;regrasdemaior,em
camadasmaisespecíficas/focadas;
•Muito alcance para pouco alcance: asregraspresentesemcamadas
maisgenéricasafetamgrandepartedoDOMe,àmedidaquevãose
afunilando,alcan çamcadavezmenospor ções.
117
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 124

9.2. Ascamadasdotriânguloinvertido CasadoCódigo
Fig.9.3:Métricas-chavedotriânguloinvertido
Comoseráconstatadoaseguir,construiroCSSbaseadonessasmétricas-
chavegarantequequestõescomespecificidadesejammitigadasequeocó-
digosejaescritoemumaordemlógicaeprogressiva.Comoseverá,issotraz
grandecapacidadedeextensãoemenosredundância.
Sepudesserepresentararela ção especificidade x localização na folha de
estilospormeiodeumgráficoparaumprojetocomum,esteseriamaisou
menosassim:
118
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 125

CasadoCódigo Capítulo9. ITCSS
Fig.9.4:Especificidadeporlocaliza çãoemprojetossemITCSS
JáusandoITCSSetodasasvantagensquesuaarquiteturatraz:
Fig.9.5:Especificidadeporlocaliza çãoemprojetosusandoITCSS
Issoilustranitidamenteasvantagensqueestãoaoseualcanceequevocê
aprenderáagora,sabendomaissobrecadaumadascamadasdeITCSS.
119
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 126

9.2. Ascamadasdotriânguloinvertido CasadoCódigo
Configurações (settings)
EmITCSSnãoéobrigatórioquesefa çausodepré-processadoresCSS.
Porém,devidoatodasasvantagensjávistasnocapítulo9,éextremamente
aconselhávelquevocêuse.Nestecaso,énacamada configurações quevocê
começaráotrabalho.
QuandopensarnacamadaConfigura ções,pensenotermo estilos globais,
jáqueéexatamenteondeessetipodeestilodeveestar.
Exemplo:
$environment: dev;
$rem-base: 16px !default;
$main-color: #c00fee;
$module-size: rem-calc(20px);
Ferramentas (tools)
A camadaFerramentasdeve conter funções e mixins olha os pré-
processadoresCSSaí! relativosaoprojeto. Essacamadavemlogoapósa
deConfigura ções,porquepodesernecessárioquealgumafun çãooumixin
façausodeumaconfigura çãoglobalqualquer.
Exemplo:
@function strip-unit($num) {
@return $num / ($num * 0 + 1);
}
@function convert-to-rem($value, $base-value: $rem-base) {
$value: strip-unit($value) / strip-unit($base-value) * 1rem;
@if ($value == 0rem) { $value: 0; } // Turn 0rem into 0
@return $value;
}
120
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 127

CasadoCódigo Capítulo9. ITCSS
@function rem-calc($values, $base-value: $rem-base) {
$max: length($values);
@if $max == 1 {
@return convert-to-rem(nth($values, 1), $base-value);
}
$remValues: ();
@for $i from 1 through $max {
$remValues: append(
$remValues,
convert-to-rem(
nth($values, $i),
$base-value
)
);
}
@return $remValues;
}
Genérico (generic)
Nacamada GenéricoéqueoCSSqueefetivamentevaientrarema ção o
resultadodacompila çãodopré-processador,diga-sedessaforma come çaa
serescrito.Aquiéondesedefinirãoeventuais CSS resets;ondesecolocaum
Normalize.css(http://goo.gl/YFPLMO);eondeum box-sizinggeral
édefinido.
EssacamadaafetaaimensamaioriadoDOM,porisso,devesermais
amplaegenérica,estandomaisparaabasedotriânguloinvertido.
Exemplo:
* {
-webkit-box-sizing: border-box;
-moz-box-sizing: border-box;
box-sizing: border-box;
}
121
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 128

9.2. Ascamadasdotriânguloinvertido CasadoCódigo
Elementos (elements)
Nacamada Elementos,constaaestiliza çãodeelementosHTML,propria-
menteditos.SeguindonametodologiadoITCSS,éumacamadaligeiramente
maisespecíficaquecomportaestiliza çõesdeelementosHTMLdiretamente,
conformeasnecessidadesdoprojeto.
Devidoaotipodeestiliza çãoquehánela,geralmentedepoisdedefinidos
osestilos,nãoénecessárioquesemexamaiscomeles,ficandoessatarefapara
ascamadasmaisespecíficasdotriângulo.
Exemplo:
img,
iframe,
object,
embed,
video {
height: auto;
max-width: 100%;
}
Objetos (objects)
Acamada Objetoscomportaestilosnãocosméticos/abstratos, reme-
tendomaisaOOCSS(maisinforma çõesem3),grids,contêinereseoutros
destanatureza.
Exemplo:
.media {
margin: 10px;
&, .bd {
overflow: hidden;
_overflow: visible;
zoom: 1;
}
.img {
float: left;
122
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 129

CasadoCódigo Capítulo9. ITCSS
margin-right: 10px;
&--ext {
float: right;
margin-left: 10px;
}
}
.img img {
display: block;
}
}
Componentes (components)
Acamada Componenteséaquecomportaomaiornúmerodeestiliza-
ções,jáqueneladevemconstaroscódigosdoselementosdeUIdoprojeto
(menus,carousels,slideretc.).Parafacilitaroentendimento,fa çaumparalelo
comosMódulosdeSMACSS(4.5).
SeguindoapropostadoITCSS,essaéumacamadamaisespecífica,quefaz
usodetudooquefoidefinidonasanteriores,tendoumníveldeespecificidade
maior.
Trumps
Parater-seumcódigototalmenteeleganteeformal,acamadaCompo-
nentespoderiatersidoconsideradaaúltima. Porém,como“naprática,a
teoriaéoutra”,ITCSSusaacamada Trumpscomoumamaneiradevencer
(beats)osestilosdasanteriores(senecessário),tornando-seoúltimobastião
deestiliza çãodentrodametodologia.
Estacamadacontémutilitários,helpers,sobrescritasehackse,devidoao
propósitopeloqualexiste,nãoseacanheemusar !importantsenecessário.
Trumpséapontadotriânguloe,emdecorrênciadisso,acamadacomas
regrasmaisespecíficas,explícitasefocadas.
Exemplo:
.half-width {
width: 50% !important ;
123
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 130

9.3. OrganizaçãodocódigocomITCSS CasadoCódigo
}
9.3 O rganização do código com ITCSS
Comofoipossívelperceber,aestruturatriangularinvertidadeITCSSpermite
aorganiza çãodocódigo,nãomaisporfun ção estilosparatipografia,para
formuláriosetc.,agora,organiza-sepor explicitudee especificidade.
Emfun çãodaorganiza çãodeITCSS,ahierarquia,acascataeaespecifi-
cidadeCSStrabalhamafavordodesenvolvedor,jáquecadacamadasomente
dáprosseguimentoaoqueaanteriorjádefiniu!
ComosugestãodoprópriocriadordeITCSS,recomenda-seque,naprá-
tica,cadacamadasejaformadaporumasériedepartials(Smacss)comase-
guinteconven çãodenome: _<camada>.<partial>.scss.
Exemplos:
_settings.colors.scss
_elements.headings.scss
_components.tabs.scss
Cada partial deve ser o mais granular e específica possível, con-
tendosomenteocódigonecessárioparacumprirafun çãoaquesedes-
tina. Porexemplo,umarquivo _elements.headings.scssdevecon-
ter tão somente regras para os títulos (h1-h6) e nada mais. Caso haja,
por exemplo, uma seção em que títulos e subtítulos sejam apresenta-
dos de maneira diferente, isso poderia constar em um outro arquivo,
como _components.page-title.scss, por meio de classes como
.page-titlee .page-title-sub.
EssaéamaneiracomoITCSSfuncionaeparaaqualsuaestruturade
triângulofoiconcebida:nãosecolocamtodososestilosdecabe çalhosjuntos;
colocam-seosestilosreferentesaelementosjuntosetudooqueébaseado
emclassesemumoutroagrupamento! Comisso,organiza-seoprojetoem
métricasúteisdeCSSenãoemblocostemáticos,que,namaioriadasvezes,
trazemquestõesdecascataeespecificidade.
Naprática,usandoSass,todasascamadasfuncionamjuntaspormeio
daimporta çãodessesváriosarquivos respeitando-seaordemdotriângulo
invertido,obviamente:
124
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 131

CasadoCódigo Capítulo9. ITCSS
@import
'settings.colors',
'settings.global',
'tools.functions',
'tools.mixins',
'generic.box-sizing',
'generic.normalize',
'elements.headings',
'elements.links',
'objects.grid',
'objects.wrappers',
'components.buttons',
'components.carousel',
'components.main-nav',
'trumps.clearfix',
'trumps.ie8'
'trumps.utilities',
;
DentrodaestruturadecamadasdeITCSS,vocêpodeusaraordemde
importaçãoquequiser,desdequesejamobedecidososseguintescritériosde
similaridade:
•Especificidade:todososseletoresdeelementosoudeclassesoutodos
utilitárioscom !importantetc.;
•Explicitude:estilizartodososelementosbaseHTMLoudeUIetc.;
•Alcance:capacidadedeafetartodooDOM(porexemplo, * {});par-
tesdoDOM(exemplo, a {});umase çãodoDOM( .carousel {});
ouumnóespecíficodoDOM( .clearfix {}).
125
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 132

9.4. Conclusão CasadoCódigo
9.4 C onclusão
Comovisto,ITCSSéumanovamaneiradepensareorganizaraarquitetura
CSSdeseusprojetos.Suaestruturapermiteparardeordená-losportemase
passarausarmétricasúteisdeCSS.Paraisso,eleéorganizadofuncionalmente
emcamadasqueaproveitamahierarquia,cascataeespecificidadeCSS.
Comoqualquermetodologia,nãosetrataderegrasrígidasnemconceitos
escritosempedra.Casotenhagostado,masgostariadealterarumaououtra
coisa,sinta-seàvontade!Porexemplo,emvezdeusaraestruturadenomes
departialsindicada,vocêpodequererorganizartudoemsubpastascomo
nomedoarquivosimplificado:
126
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 133

CasadoCódigo Capítulo9. ITCSS
Fig.9.6:Organizeosprojetoscomoformelhorparavocêesuaequipe:não
hánormasrígidas
Isso, obviamente, alteraria a importação dos partials em seu
style.scss:
@import
'settings/colors',
'settings/global',
'tools/functions',
'tools/mixins',
'generics/box-sizing',
127
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 134

9.4. Conclusão CasadoCódigo
'generics/normalize',
'elements/headings',
'elements/links',
'objects/grid',
'objects/wrappers',
'components/buttons',
'components/carousel',
'components/main-nav',
'trumps/clearfix',
'trumps/ie8'
'trumps/utilities',
;
Percebaqueo generictambémfoialteradopara generics. Uma
adaptaçãomeramentematerialaogostodequemestáusando,quedeixaa
propostadearquiteturaCSSmaispersonalizadasemseabsterdosbenefícios
queelaoferece!
Ametodologiafoicriadaparaajudar,nãoparaatrapalhar.Portanto,teste,
experimente,use,reúseeadapte-aconformesejanecessário,sempreaprovei-
tandooquedemelhorITCSStemaoferecer!
128
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 135

Capítulo10
Ofim
Esteéofim.OfimdoiníciodeseusestudossobrecomoescreverCSSmelhor
ecome çarausarumaarquiteturaCSSdecente!
Seleuolivronaíntegraeprestouaten ção,agoravocêjáconhecemaisa
fundosobreseletoresCSS(2),CSSorientadoaobjetos(3),SMACSS(4),BEM
(5),pré-processadoresCSS(9)eonovíssimoITCSS(9).
ParaosacostumadosafazersóofeijãocomarrozdeCSS,sãoevolu ções
bastanteconsideráveis,que,semsombradedúvidas,farãocomquevocêpasse
paraopróximonívelnosconhecimentosetécnicasdefront-end!
Vocênãoprecisausartudooquefoivistodeumavez. Fa çasuasexpe-
rimentações.Testeusaralgumasdastécnicas/metodologiasemumprojeto,
depoistroqueparaoutrasemoutro.Aexperimenta çãotrouxeahumanidade
atéaquievocêpodeseraquelequeajudaráomundoadarumpassoalém!
Aproveitequeadquiriuestelivroe alémdesugeriraoscolegasquetam-
bémfaçamomesmo,volteaoscapítulosefa çaconsultasquantasvezesforem
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com

## Página 136

CasadoCódigo
necessárias.Sigaoslinksesugestõesmostradosesemprecontinueestudando!
Algoaselevaremconsidera ção,quetambémajudaaproduzir CSS efici-
ente,étentarmanterocódigofielaum guia de estilos.Istoé,umasériede
orientaçõesdeescritadecódigoquedeveserseguidaporaquelesquemexem
nosestilosdoprojeto. Existeumamáximaquantoaisso: O código de um
projeto deve parecer que foi escrito por uma só pessoa.Seguirumguiade
estiloajudabastantequantoaisso,tenhacerteza!
Guiasdeestilosfacilmentepoderiamtersidoumcapítuloincluídoneste
livro, mas como são muitos e bastante variados para CSS e para pré-
processadoresCSS,émaisconvenientequevocêosencontreemumabusca
edecidaporaquelesqueseadequemmaisàsuamaneiraeaseushábitosde
codificação.
Paracome çar,dêumaolhadanoIdiomaticCSS(http://goo.gl/gLJI8e)eno
artigo CSS Style Guides(http://goo.gl/HVTY5K),quecontacomreferências
aalgunsnotórios,comoGitHub,GoogleeWordPress.
Nãodevesernenhumasurpresaqueastécnicaseconhecimentosmostra-
dosaquipodemsertãodinâmicosemutáveisquantoaprópriaweb!Ademais,
queexistemmuitosmaisconceitos/metodologiasporaíque,apesardebem
parecidoscomoquefoimostradodurantetodoolivro,tambémpossamser
dignosdesuaaten çãocomoAtomicDesign(http://goo.gl/d7BJQs)ouOrga-
nicCSS(http://goo.gl/PHQCJJ).
Logo,nadadeacharqueagoravocêéoSr.(ouSra.)front-end;vocêestá
apenasdandocontinuidadeàjornada.Apartirdessasinforma çõesesomente
com muita prática,vocêconseguiráefetivamentedarospróximospassosna
melhoriaenaevolu çãodeconhecimentossobrefront-endparasetornarum
profissionalmelhor.
Comodiria Morpheus, há uma diferença entre conhecer o caminho e
trilhá-lo.
Bonsestudos!
130
E-book gerado especialmente para André Martins - andreluis22.ap@gmail.com