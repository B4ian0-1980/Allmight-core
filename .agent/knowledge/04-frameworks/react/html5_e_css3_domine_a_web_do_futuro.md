---json
{
  "id": "html5_e_css3_domine_a_web_do_futuro",
  "title": "HTML5 e CSS3 Domine a web do futuro",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Arquivo Original:** `HTML5 e CSS3 Domine a web do futuro.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "css3",
    "domine",
    "frameworks",
    "futuro",
    "html5",
    "react",
    "web"
  ],
  "perguntas_tipo": [
    "Como utilizar HTML5 e CSS3 Domine a web do futuro?",
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

# HTML5 e CSS3 Domine a web do futuro

> **Arquivo Original:** `HTML5 e CSS3 Domine a web do futuro.pdf`
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
Agradecimentos
“Nothing of me is original. I am the combined effort of everybody I’ve ever known. ”
–ChuckPalahniuk,InvisibleMonsters(1999)
Duranteacria çãodestelivro,recebiajudadeváriaspessoas,esouextremamente
gratoaelaspelasuaparticipa çãonosmesesemquetrabalheinele:
AoAdrianoAlmeidaeaoPauloSilveirapelaoportunidadeúnicadeescrevereste
livro,eaajudadetodosdaCasadoCódigoedaCaelum.
Àminhafamíliaeàminhanamorada,pelapaciênciaeajudaduranteestesmeses,
portodasasnoitesefinaisdesemanadedicadosaesteprojeto.Aincrívelequipeda
Plataformatec,queémuitoboanoquefaz. Portodososprojetos,apresenta ções,
cafésechoppscompartilhadosatéentão-quemuitosoutrosvenhamnofuturo!
Atodososmeuscolegaseamigosdeprojetoseempresaspassadas-devomuito
atodospeloconhecimentocompartilhadoaolongodosanos,quesemdúvidafoi
muitoimportanteparaeuchegaratéaqui.
Eavocê,leitor,queestáprestesaleromeulivro.Muitoobrigadopordedicaro
seutempoeasuaaten çãoaele.Esperocontribuirparaquevocêcrieótimosprojetos
efaçaasuaparteparacriarumawebmelhor.
i


## Página 7

CasadoCódigo Sumário
Sumário
1 Odesenvolvimentowebhoje 1
1.1 PorquevocêdeveaprenderHTMLeCSS . . . . . . . . . . . . . . . . 2
1.2 Oestadodosnavegadores . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 Acomplica çãodosprefixosproprietários . . . . . . . . . . . . . . . . 3
1.4 Alongaesinuosaestradadestelivro . . . . . . . . . . . . . . . . . . . 4
2 Osprimeirospassoscomonossosite 7
2.1 EscrevendoHTML,dedentroparafora . . . . . . . . . . . . . . . . . 8
2.2 Adicionandoformata çõesbásicas . . . . . . . . . . . . . . . . . . . . . 10
2.3 Bordasemargens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.4 Umpoucodecorsempreébom . . . . . . . . . . . . . . . . . . . . . . 14
2.5 Primeirocontatocomimagens. . . . . . . . . . . . . . . . . . . . . . . 18
2.6 Adicionandoelementossecundários . . . . . . . . . . . . . . . . . . . 22
2.7 Façaparasuacidadetambém! . . . . . . . . . . . . . . . . . . . . . . . 25
3 HTML5:oquemudou? 27
3.1 Escrevendomenosefazendomais. . . . . . . . . . . . . . . . . . . . . 27
3.2 Atributospersonalizados . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.3 Tagsnovasparaelementosantigos . . . . . . . . . . . . . . . . . . . . 29
3.4 RefatoraçãodapáginadeSãoPaulo. . . . . . . . . . . . . . . . . . . . 31
3.5 Sejapragmático . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4 OquetododesenvolvedorprecisasabersobreCSS 35
4.1 AincompatibilidadedosbrowsersearazãodosresetsdeCSS . . . . 35
4.2 CompreendendooBoxmodel . . . . . . . . . . . . . . . . . . . . . . . 38
iii


## Página 8

Sumário CasadoCódigo
4.3 Utilizandopseudoelementos. . . . . . . . . . . . . . . . . . . . . . . . 41
4.4 Desenhandoumafaixacom“before” e “after” . . . . . . . . . . . . . . 41
4.5 Decorandomensagens . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.6 CriandoconteúdoatravésdeCSS . . . . . . . . . . . . . . . . . . . . . 47
4.7 ArquiteteoseuCSSparaofuturo . . . . . . . . . . . . . . . . . . . . . 49
4.8 Gererelatóriosinteligentesesimplescomosestilosdeimpressão . . 52
5 OquevocêconseguefazercomCSS3 61
5.1 Aregra@font-face. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
5.2 Comoutilizarservi çosdedistribui çãodefontes. . . . . . . . . . . . . 63
5.3 Substituiçãodeíconesporfontes . . . . . . . . . . . . . . . . . . . . . 64
5.4 Explorenovaspossibilidadescombordas . . . . . . . . . . . . . . . . 67
5.5 Manipulaçãodecorescomrgbaegradientes. . . . . . . . . . . . . . . 71
5.6 Trabalhecomsombrasecriemenuselegantes . . . . . . . . . . . . . . 79
5.7 Combinandotudo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
6 Tomandocontroledaestruturavisual 95
6.1 Apropriedade‘display’ . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
6.2 Flutueelementos. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
6.3 Oclearfix,umaclasseobrigatóriaemseusprojetos . . . . . . . . . . . 106
6.4 Compreendaousodeposition. . . . . . . . . . . . . . . . . . . . . . . 107
6.5 Crieasuaprópriajanelamodal . . . . . . . . . . . . . . . . . . . . . . 110
6.6 Comoescolherosmétodosparaposicionarosseuselementos . . . . 116
6.7 Grids-umpadrãodeestruturaparaassuaspáginas . . . . . . . . . . 117
6.8 PosicionandoelementoscomCSS3 . . . . . . . . . . . . . . . . . . . . 118
7 Melhorandoosseusformulários 123
7.1 OquetemosnoHTML5 . . . . . . . . . . . . . . . . . . . . . . . . . . 123
7.2 FormuláriosHTML5nosdispositivosmóveis. . . . . . . . . . . . . . 124
7.3 Criaçãodoprimeiroformulário . . . . . . . . . . . . . . . . . . . . . . 125
7.4 Alinhamentoeestilosvisuaisnoscamposeformulários . . . . . . . . 127
7.5 Exibiçãodemensagensdeajuda . . . . . . . . . . . . . . . . . . . . . . 129
7.6 Mostremensagensdeerro . . . . . . . . . . . . . . . . . . . . . . . . . 132
7.7 Levandoousuáriodiretoaoqueimportacomoautofocus . . . . . . 134
7.8 Aflexibilidadedoatributoplaceholder . . . . . . . . . . . . . . . . . . 134
7.9 AplicandoCSS3embotões . . . . . . . . . . . . . . . . . . . . . . . . . 140
iv


## Página 9

CasadoCódigo Sumário
8 Efeitos101:Trabalhandocomanima çõesetransi ções 149
8.1 Transformandoelementos . . . . . . . . . . . . . . . . . . . . . . . . . 150
8.2 Osefeitosrotate,scale,skewetranslateemumagaleriadefotos . . . 150
8.3 Transiçõesdeestilos. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
8.4 Transiçõesnagaleriadefotos . . . . . . . . . . . . . . . . . . . . . . . 156
8.5 Umdetalheimportantesobretransi çõeseJavaScript . . . . . . . . . . 160
8.6 Transformaçõesem3D . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
8.7 Girarformulárioscomapenasumclique. . . . . . . . . . . . . . . . . 161
8.8 Utilizandoanima ções . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
8.9 Começandocomkeyframes . . . . . . . . . . . . . . . . . . . . . . . . 170
9 Ouniversoforadosdesktopsenotebooks 175
9.1 Oqueé“ResponsiveWebDesign”eporquêvocêdevesepreocupar . 176
9.2 Ofuncionamentodosmediaqueries . . . . . . . . . . . . . . . . . . . 177
9.3 Nãoéumaquestãodeaparelhos. . . . . . . . . . . . . . . . . . . . . . 178
9.4 Porumfuturomelhor. . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
10 Ferramentas-Frameworks,PluginsePré-processadores 181
10.1 TwitterBootstrap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
10.2 HTML5Boilerplate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
10.3 PluginsemJavaScript . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
10.4 Modernizr . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
10.5 Polyfills . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
10.6 Pré-processadores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
10.7 ÉtudoCSSeHTML. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
11 Nãopareporaqui 191
ÍndiceRemissivo 196
Bibliografia 197
Versão:16.2.5
v


## Página 11

Capítulo1
Odesenvolvimentowebhoje
Talvezeusejaumotimista,masacreditoquenosencontramosemumaépocarevo-
lucionáriaparaodesenvolvimentoweb.Ainternetseproliferoupelomundogra ças
aosavançosdebandalargaeosdiversosdispositivoscapazesdenavegarpelarede
-celulares,tablets,televisõesevideogames. Diversasempresasdomundodigital
impulsionamaevolu çãodastecnologiasqueusamosparacriarumawebmelhor.
ProfissionaisemempresascomoGoogle,Microsoft,AppleeFacebooktrabalham
exclusivamenteemmelhoriasparaosnavegadoresmaisutilizados,alémdepartici-
paremdadefini çãodenovospadrõesedisseminarembastanteconhecimentojunto
àcomunidadededesenvolvedores.
Etudovaicontinuaraseexpandir.Novasempresas,novospadrões,novosdis-
positivos. Aindústriadainternetestáemcontínuocrescimentoeprecisamosde
bastanteajudaparadarprosseguimentoaessetrabalho. Eémuitofácilgarantiro
seuespaçonesteuniversoquesemovecomoumtrembala.Bastaparticipar.


## Página 12

1.1. PorquevocêdeveaprenderHTMLeCSS CasadoCódigo
1.1 Por que você deve aprender HTML eCSS
Casovocêsejaumdesignersemmuitaexperiênciacomdesenvolvimento,ouum
programadormaisacostumadoatrabalharcomlinhasdecomandoecompilado-
resdoquenavegadores,deixe-meexplicarumpoucoaimportânciadeseaprender
HTMLeCSS.Sevocêestivertrabalhandooupretendetrabalharcomtecnologia,
acreditoqueboaparte-outudo-dosseusprojetosseráutilizadaatravésdeumna-
vegador.Sejaumsistemainternodeumbanco,umaredesocial,umgrandeportal
denotíciasousitesparacampanhasdepublicidade,omeiocomumhojeemdiaé
aweb,eébastanteinteressanteterumaótimabasedeconhecimentosobredesen-
volvimento front-end(umdostermosusadosparasereferenciaràinterfacedeuma
aplicação)paracontribuirparaosucessodosprojetosdequevocêestiverpartici-
pando.
Porisso,recomendomuitoquevocêaprendasobreoquefazawebfuncionar.
Alémdelivroscomoeste,existemdiversoscursosesitesparavocêaprendermaisa
respeitoououtrastecnologiasrelacionadas.Imaginecuidardeumparquedeservi-
doressemterbonsconhecimentosdesistemasoperacionaisedetopologiaderedes,
outrabalharempropagandaimpressasementendersobreascoresouopapelusado.
1.2 O estado dos navegadores
TodooHTMLeoCSSqueescrevemosganhavidadentrodosnavegadoresutilizados
porquemacessanossaspáginasesites,porissoébastanteimportanteterumbom
entendimentodecomoelesfuncioname,principalmente,dosburacosnomeiodo
caminho.DesdeostemposdoMosaic(queeventualmentesetornouoNetscape)e
dasprimeirasversõesdoInternetExplorerem1995sempreenfrentamosumaguerra
deincompatibilidadeentreosnevegadoreseanecessidadedepadrõesparagaran-
tirainteroperabilidadedawebentreclientesdiferentes.Enquantoessabrigapode
custaralgunscabelosnossos,elatambémimpulsionaaevolu çãodastecnologiasque
fazemosnavegadoresfuncionar. OGoogleChromemudouaperspectivasobreo
processodeatualiza çãocontínua,garantindoqueamaioriadeseususuáriospossua
aúltimaversãodonavegador,eoFirefoxcome çouaadotarumprocessosimilar.E
ocomponentededebugeinspe çãodoFirefox,oFirebug,definiuomodelobásico
paraqueosoutrosnavegadoresimplementassemferramentassimilares.
Atualmente,oGoogleChromecostumaserocampeãodostestesdecompatibili-
dadecomasúltimasespecifica ções,sempreseguidodepertodasúltimasversõesdo
Firefox,SafarieOpera.BoapartedasinclusõesdoHTML5eCSS3jáestádisponível
2


## Página 13

CasadoCódigo Capítulo1. Odesenvolvimentowebhoje
nessesnavegadoresporcompletoouatravésdeprefixosproprietários. OInternet
Explorer,atualmentenaversão9(nomomentodaescritadesselivroaversão10está
emdesenvolvimento),aindaseencontrabematrásdosdemais,masaspromessas
paraasuapróximaversãosãointeressantes.
Osperigosmoramnoscasosemqueprecisamosiralémdasúltimasversõese
trabalharcommaisantigas,comoversõesdoFirefoxanterioresa8eosfamigerados
InternetExplorer6e7.Adiferen çaentreosnavegadoreseaperformancedoJavaS-
criptemcomparaçãocomassuasúltimasversõeséassombrosa,masemalgunscasos
aaudiênciadesejadasemantémpresaaessesnavegadores,porcomplica çõesparase
atualizaronavegadorouatéosistemaoperacional-AsúltimasversõesdoInternet
ExplorernãosãocompatíveiscomoWindowsXPporexemplo,oqueatrapalhaa
atualizaçãoemalgunsambientescorporativos.
Porisso,éimportantedefinirasfronteirasdosnavegadorescomquevocêpre-
tendetrabalhar,eseaproveitardastécnicasadequeadasoudassolu çõesexistentes
paraproblemasrelacionadosaeles.
1.3 A complicação dos prefixos proprietários
Paraquemestáacompanhandoacristadaonda,diversaspropriedadesefunciona-
lidadesnovasnãoseencontramcompletamentedefinidaseimplementadasnosna-
vegadores.Masissonãonosimpededeutilizarversões“experimentais”delas.Para
isso,cadanavegadorcostumaexporessasnovidadescomprefixosespecíficospara
diferenciardaimplementa çãofinal.Oqueaprincípiopodesoarcomoumaótima
ideiasetornouumfardoparatodososdesenvolvedores:escreverasmesmaslinhas
deCSS(até)4vezes,assim:
.button {
/* Prefixo para o Firefox. */
-moz-transition: all 0.2s linear;
/* Prefixo para o Chrome, Safari, Safari Mobile e Android. */
-webkit-transition: all 0.2s linear;
/* Prefixo para o Opera. */
-o-transition: all 0.2s linear;
/* Versão final, ainda nao suportada em todos os browsers */
transition: all 0.2s linear;
}
Enquanto hackscomoessepodemparecerdesnecessárioseculpadosporsujaro
código,éprecisoentendersuaimportância.Jáestamosdesfrutandoetestandoessas
3


## Página 14

1.4. Alongaesinuosaestradadestelivro CasadoCódigo
propriedadesenquantoelassãodefinidaserefinadas.Oobjetivoé,eventualmente,
nãoprecisarmaisdasversõesprefixadaseseutilizarapenasaversãocanônicadas
propriedades.
Masnemtodosparamparaacompanharoprogressodessesitens. Proprieda-
descomo border-radiuse box-shadownãoprecisammaisdeprefixosparaos
principaisnavegadoresdedesktops,eatéofinalde2012outraspropriedadescomo
animation, transitione transformestarãofinalizadasedevidamenteimple-
mentadas.
Paraisso,precisa-selevaremconsidera çãodoisitens:mantenha-seatualizado
sobreosuportedosnavegadoresparanovasfuncionalidades-minhareferênciafa-
voritaéohttp://caniuse.com/,quepossuiarela çãodenavegadorescomsuporte
completo,parcialouinexistente,equecostumovisitardetemposemtempos,prin-
cipalmenteaocome çarnovosprojetos,parameatualizarsobreesseassunto.Outro
pontoimportanteéquevocêdevemitigarouautomatizaroruídoeoretrabalhoge-
radopelousodeprefixos,sejacomsolu çõescomopré-processadoresouferramentas
emJavaScript,efocaroseutrabalhonoqueétidocomopadrão,poisemalgummo-
mentoosprefixosnãoserãomaisnecessários.
Paraissovamostrabalharcomospadrõesdefinidoseeventualmentecitandoos
prefixosquandonecessários.
1.4 A longa e sinuosa estrada deste livro
Nestelivro,passaremospordiversasreceitasetécnicasparavocêutilizaremseus
projetos,evamoslereescrever muitocódigo-muitomesmo.Usaremostagsepro-
priedadesqueestãoemusoaanos,alémdepassarporadi çõesrecentesdoHTML5
edoCSS3.Aminhainten çãoémostrarexemplospráticosqueprovavelmentevocê
chegouaverouiráusarnoseudia-a-dia,masdeixoessaavalia çãoavocê.Euseique
váriosdelesjámeajudaramumaouduasvezesporaí.
Paratudoisso,precisamosdeumpontodesaída,umatelaembrancoparao
nossotrabalho. AlémdaestruturabásicadeHTMLabaixo,vamosutilizaralgu-
masferramentasparaajudaronossotrabalhoedeixaralgumaspartesnãotãointe-
ressantesdodesenvolvimentowebdelado,assimpodemosfocarnoquerealmente
importa.Utilizaremoso Normalize.css(http://necolas.github.com/normalize.css/)
comoumestilodebase,paragarantirumaconsistênciamelhorentrenavegado-
res diferentes e o-prefix-free(http://leaverou.github.com/prefixfree/) , que será
responsávelportratarosprefixosproprietáriosparaaspropriedadesdeCSS3que
4


## Página 15

CasadoCódigo Capítulo1. Odesenvolvimentowebhoje
aindanãosetornaramumpadrãoentrenavegadores. Alémdeles,precisamosde
umpoucodeJavaScriptparafinalizaralgunsdosnossosexemplos,eaío jQuery
(http://jquery.com/)entraráemação.
Masnãotema! Casotudoissopare çademaisparavocê,fiqueseguroporque
iremosentraremdetalhessobreresetsdeCSSesobreo-prefix-free.Porenquanto,
possolhegarantirqueelesirãoajudarbastanteonossotrabalhonodecorrerdeste
livro.Abaixo,segueomínimonecessáriodecódigoHTMLqueiremosprecisar.
Vocêpodebaixarestetemplateemhttp://lucasmazza.github.com/template.zip.
<!doctype html>
<html lang= 'pt-BR'>
<head>
<meta charset="UTF-8">
<title></title>
<link rel="stylesheet" href="normalize.css">
<script src="prefixfree.min.js"></script>
</head>
<body>
<!-- O seu HTML vem aqui! -->
<script src="jquery.min.js"></script>
</body>
</html>
ParaoCSSespecíficodecadaexemplo,vocêpodecriarumarquivocomum
nomerelacionadoaoqueestiverfazendoeadicionarumareferênciaaele, logo
abaixodo normalize.css. Assim,noexemplodeanima ções,vocêpodecriar
umarquivo animacoes.cssecolocarumatag linkdentrodatag head.
<!doctype html>
<html lang= 'pt-BR'>
<head>
<meta charset="UTF-8">
<title>Trabalhando com animações!</title>
<link rel="stylesheet" href="normalize.css">
<link rel="stylesheet" href="animacoes.css">
<script src="prefixfree.min.js"></script>
</head>
<body>
<!-- O seu HTML vem aqui! -->
<script src="jquery.min.js"></script>
5


## Página 16

1.4. Alongaesinuosaestradadestelivro CasadoCódigo
</body>
</html>
Semprequeficaremdúvida,vocêpodetambémconsultarocódigofontedos
exemplos,queestádisponívelemhttp://lucasmazza.github.io/htmlcss-exemplos/.
Comissoemmãos,horadecome çaratrabalharnoquerealmenteinteressa!
6


## Página 17

Capítulo2
Osprimeirospassoscomonosso
site
Antesdemergulharmosdecabe çaemtécnicasespecíficas,propriedadesdeCSSe
combinaçõesdetagseestilos,vamospraticarumpoucode front-endarrozcomfei-
jãoparagarantirqueestamosprontosparaosdemaisassuntosequeasbasesde
desenvolvimentowebestãobemclarasparavocê.
SãoPaulo,SãoPaulo
Quandovocêmorabastantetempoemumamesmacidadevocêsempredefine
umalistadelugareseregiõesdasuapreferência,esempreosindicaparaosseusami-
gosdeforaquandoeleschegamparapassaralgunsdias.Paradeixaraminhalistade
paradasobrigatóriasdeSãoPauloumpoucomaisinteressantedesevervamoscriar
oOqueeumaisgostoemSãoPaulo... ,umsitedeumapáginasóparafalarsobre
algunslugaresdacidade.Apáginateráumalistade3lugaresdemaiorimportância,
comumabrevedescri ção,umafoto,eumalistaadicionaldemaiscoisasaseverna


## Página 18

2.1. EscrevendoHTML,dedentroparafora CasadoCódigo
cidade.Nósvamoscriá-ladozero,eaversãofinalficaráassim:
Figura2.1:OnossositesobrelugaresdeSãoPauloquenãosepodedeixardevisitar.
A versão final da nossa página também está disponível online em http://
saopaulo.herokuapp.com.
2.1 Escrevendo HTML, de dentro para fora
Vamoscomeçarpelapartemaisimportantedapágina,oconteúdo.Quenocaso,são
os3lugaresquevocênãopodedeixardevisitaremSãoPaulo.Oprimeiro,aAvenida
Paulista,ficaráassim:
<h2>Passear na Avenida Paulista!</h2>
<p>
Um dos principais centros financeiros da cidade, a avenida Paulista
também possui diversas opções de entretenimento. Endereço do Museu
de Arte de São Paulo, <em>MASP</em>, do Teatro Gazeta e muitos outros,
a região é de fácil acesso graças às diversas linhas de ônibus que
cruzam a avenida e à linha de metrô que passa por baixo dela.
</p>
<p>
A Avenida Paulista sempre é assunto. O que será que estão falando a
8


## Página 19

CasadoCódigo Capítulo2. Osprimeirospassoscomonossosite
respeito no <a href= 'https://twitter.com/#!/search/Avenida Paulista '
target='_blank'>Twitter</a>?
</p>
Oquetemosaqui?Primeiro,umtítulosecundárioutilizandoatag h2,acompa-
nhadodedoisparágrafoscomtexto,delimitadospelatag p.Dentrodosparágrafos,
alémdoprópriotexto,temosoutrastagsparadefinirmaiselementos.Umadelaséa
tag em,utilizadaparaindicarênfase,queteráoseutextoexibidoemitáliconapá-
gina.Ooutroelemento,umlinkparasenavegaraosresultadosdebuscadoTwitter
paraotermo“Av.Paulista”,écriadopelataga(derivadadapalavra âncoraeminglês,
anchor). Oatributo hrefindicaqualoendere çoqueolinkaponta,eo target
indicaqueolinkdeveserabertoemumanovapágina.Estassãoalgumasdasprin-
cipaistagsutilizadasparasedefinirelementosdeconteúdo,entãovocêirávê-las
bastanteporaqui.
Seguindoemfrente,podemosadicionarorestodonossoconteúdo,outros2lu-
gares.UmdeleséaregiãodaVilaMadalena,eoúltimoéoParquedoIbirapuera.
<h2>Os bares da Vila Madalena</h2>
<p>
Depois de um dia de trabalho, nada melhor do que um bom chopp, um
petisco e uma conversa em uma mesa de bar. Opções de sobra na região
das ruas Aspicuelta, Fradique Coutinho e Wisard.
</p>
<p>
Veja quais os melhores bares e restaurantes da região no
<a href= 'http://vejasp.abril.com.br/busca?chn=bares&qu=
&nbh=Pinheiros%20/%20Vila%20Madalena' target='_blank'>
Guia da VEJA São Paulo.
</a>
</p>
<h2>O Parque do Ibirapuera</h2>
<p>
Um dos cartões postais da cidade, o parque dispõe de mais de 1,5 km ²
de área verde, lagos artificiais e pistas de cooper e ciclismo. E se
isso não fosse o suficiente, o parque costuma ser palco de diversos
eventos culturais ao longo do ano.
</p>
<p>
Veja no <a href= 'http://goo.gl/maps/HoH8' target='_blank'>mapa</a>
9


## Página 20

2.2. Adicionandoformataçõesbásicas CasadoCódigo
como chegar ao parque.
</p>
Nadadenovoatéomomento.Novosparágrafos,títuloselinksparaoutrosluga-
res-abuscadebaresdositedaVejaSãoPauloealocaliza çãodoParquenoGoogle
Maps. Comaparteprincipalnoseulugar,vamoscontinuarnalistademelhorias
afazerparaanossapágina.Todositeprecisadeumtítulo,certo?Paraissovamos
utilizaratag h1,querepresentaumtítuloprincipal.Alémdisso,dentrodoelemento
head,podemospreencheratag titlecomumtítuloparaajaneladonavegador.
<!doctype html>
<html lang= 'pt-BR'>
<head>
<!-- outras tags do head aqui -->
<title>O que eu mais gosto em São Paulo</title>
</head>
<body>
<h1>O que eu mais gosto em São Paulo</h1>
<!-- o nosso conteúdo aqui... -->
</body>
</html>
Figura2.2:Todoonossoconteúdo,semestilos.
Ótimo!Jápodemosdizerqueestamoscomumapáginaemmãos,certo?Bem,
oHTMLestánoseulugar,masprecisamosdeumpoucodeCSSparamelhorara
apresentaçãodonossoconteúdo.
2.2 Adicionando formatações básicas
ParacomeçaroCSSdanossapáginavamosfixaralarguradisponívelparaoconteúdo
ecentralizaromesmonapágina,deixandoumespa çoembranconaslaterais.Para
10


## Página 21

CasadoCódigo Capítulo2. Osprimeirospassoscomonossosite
isso,adicionamosumatag divemvoltadetodooHTMLquecriamosdentrodo
body,comumaclassechamada container
<div class= 'container'>
<!-- Todo o corpo da página vem aqui... -->
</div>
EoCSSparacentralizaresta divnapágina:
.container {
margin: 0 auto;
width: 960px;
}
Apropriedade widthfixaalargurapara 960px,adequandooconteúdoatelas
depelomenos1024pxdelargura,comotabletsenetbooks. Amargemsuperiore
inferiorestácom0,easmargenslateraisem autocuidamdecentralizaroelemento
napágina.Opróximopassoémelhoraraexibi çãodostextos,ajustandoumpouco
oestilodasfontescomoseguintecódigo,quedeveseradicionadoacimadoCSS
anterior:
body {
font-family: "Lucida Grande", "Lucida Sans Unicode", Verdana,
sans-serif;
line-height: 1.6;
}
Aqui,estamostrocandoa famíliadefontesutilizadasparaumalistade4fontes
diferentesquesãoutilizadasdaseguintemaneira:casoaprimeirafontelistadanão
estejadisponívelnosistemaoperacionaldousuário,onavegadortentaráutilizara
próximaeassimsucessivamente.A Lucida GrandeseráafonteutilizadapeloMac
OSXaoexibiranossapágina,enquantoa Lucida Sans Unicodeserávistapor
usuáriosdoWindows,jáqueestesistemaoperacionalnãopossuiaprimeirafonte
danossalista.Emcasosmaisextremos, Verdanaseráutilizadoouonavegadorirá
exibirumafontesemserifaporpadrão.Umaformadesecontornarissoéinstalando
diversasfontesdiferentesporcontaprópria,masnãopodemoscontarcomisso.En-
quantoo line-heightde 1.6,semnenhumamedidaespecífica-como pxou
em-,indicaparaaalturadaslinhasficaremcom160%daalturadafonte.Casoela
estejaem 16px,o line-heightserá25px.Casoaalturadafontemude,aaltura
11


## Página 22

2.3. Bordasemargens CasadoCódigo
dalinhadetextoiráacompanharessamudan ça,respeitandoaregradesempreser
1.6daalturadafonte.
Não estamos alterando a altura da fonte por enquanto - a propriedade
font-size,parautilizarovalorpadrãodonavegador,quecostumaserde 16px
emdesktopsenotebooks,enquantooutrosaparelhosounavegadorescomconfigu-
raçõesdiferentespossuemumoutrotamanhopadrão.Outrodetalheimportanteé
queestamosadicionandoestesestilosàtag body.Destaforma,todososelementos
dapáginairãoherdaressasregras“padrões”danossapágina,epodemosalterá-las
conformeanecessidadedecadaelemento.
Figura2.3:Ocontainerde960pxdelarguraeaaltera çãodefonte.
2.3 Bordas e margens
Seanalisarmoscommaisdetalheonossoconteúdo,estamosfalandosobre3lugares
diferentes,sendoquecadaumpossuiumtítuloeumadescri ção.Paraessadefini ção
transparecernonossocódigo,podemoscolocaroselementosdecadalugardentro
deumnovoelemento,paraagruparcadaum.
<div class= 'place'>
<!-- O título e a descrição da Avenida Paulista... -->
</div>
<div class= 'place'>
<!-- O título e a descrição da Vila Madalena... -->
</div>
<div class= 'place'>
<!-- O título e a descrição do Parque do Ibirapuera... -->
</div>
Estaalteraçãonãotemimpactonenhumnovisualdanossapágina,masnosdá
porondeadicionarumestiloparacadaumdos3lugares,jáqueagoraexisteum
12


## Página 23

CasadoCódigo Capítulo2. Osprimeirospassoscomonossosite
elementoespecíficoqueenglobaoseuconteúdo.Assim,adicionamosumpoucode
espaçamentoebordasacadaumdeles.
.place {
border-color: #CCC #999 #999 #CCC;
border: 1px solid #CCC;
margin-bottom: 20px;
padding: 10px;
}
Agora,cadaelementoquecontenhao class='place',oulugar,teráuma
bordasólida-umalinha-de 1px.Aprincípiotodasasbordassãodomesmotomde
cinza,masvamosmudarasbordasdadireitaedebaixoparaoutrotomdecor,repe-
tindoomesmocinzaparaasoutrasbordas,atravésdo border-color.Alémdisso,
o margin-bottom,coloca 20pxabaixodecadaumdoselementos,adicionando
espaçoentreeleseaotérminodalista.Enquantoapropriedade margin-bottom
adicionaoespa çamentodoladodeforadoselementos,apropriedade padding
adicionaoespa çamentodentrodele,quenocasoéde 10pxemtodososlados.
Astrêspropriedades- padding, margine border-funcionamdemaneira
similar,sendopossíveldefinirumvalorespecíficoparacadaumdos4ladosdoele-
mento.Casovocêqueriadefinirovalorparaapenasumdeles,épossívelutilizara
variação -top/right/bottom/left,comoo margin-bottom.Ousodapro-
priedadesemosufixovaiaplicaromesmovalorparatodososladosdoelemento,ou
vocêpodeinformarumalistadevaloresdiferenteseelesserãoaplicadosemsentido
horário-oprimeiroseráparaotopo( top),osegundoparaoladodireitoeassim
pordiante.
Apesardos 10pxde padding,oespa çamentoentreabordaeotítuloaparenta
sermaisdoqueisso.Issoéresultadodo marginpadrãodoelemento h2somado
como paddingda divqueencapsula.Paraajustarisso,podemosremoveramar-
gemdo h2completamente. Debrinde,adicionamosumabordaverdeabaixodo
título.
.place h2 {
border-bottom: 1px dashed #7E9F19;
margin: 0;
}
Assim,todososladosdoelemento .placeterãoomesmoespa çamentode
10px.Esteestilosóseaplicaráàsocorrênciasde h2dentrodeoutroelementoque
13


## Página 24

2.4. Umpoucodecorsempreébom CasadoCódigo
possuaaclasse place.Ediferentedabordasólidadeantes,utilizamoso dashed
nolugarde solid,paracriarumefeitodiferente,comumabordatracejada.
Figura2.4:Asbordaseoespa çamentodaclasse‘.place’.
2.4 Um pouco de cor sempre é bom
Horadetrocaropretoebrancodanossapáginaecolocaralgumascores.Primeiro,
cuidaremosdofundodapágina.Alémdeumanovacor,vamoscombinarissocom
umaimagemcomumefeitoderuído,queseráaplicadoemcimadacordefundo,
assim:
body {
background: #FFF1D6 url(images/noise.png);
font-family: "Lucida Grande", "Lucida Sans Unicode", Verdana,
sans-serif;
line-height: 1.6;
}
14


## Página 25

CasadoCódigo Capítulo2. Osprimeirospassoscomonossosite
Figura2.5:Ofundodanossapágina.
Como a imagem irá preencher todo o fundo dobody, não preci-
samos nos preocupar com as propriedades debackground-repeat ou
background-position,quesãousadasparacontrolarmaisdetalhessobreaapli-
caçãodasimagensdefundo.Lembre-sedeteraimagem noise.pngnocaminho
correspondenteaoqueestánocódigo-nonossocaso,emumdiretório images
queestájuntoaoarquivo .htmldapágina. Vocêpodebaixarestearquivoem
http://saopaulo.herokuapp.com/images/noise.png.
Agora,oselementos .placeprecisamdeumfundodiferente,paraajudarna
leituradostextos.Podemosentãocolocarumfundobranconeles.
.place {
background-color: #FFF;
border: 1px solid #CCC;
border-color: #CCC #999 #999 #CCC;
margin-bottom: 20px;
padding: 10px;
}
Melhor,certo?Comoestamosapenasmudandoacordefundo,podemosutilizar
tantoapropriedade backgroundquantoo background-color,aescolhaélivre.
15


## Página 26

2.4. Umpoucodecorsempreébom CasadoCódigo
Figura2.6:Ofundobrancodadivemcimadofundodapágina.
Podemostambémmudaracordoslinksexistentesnonossoconteúdo. Desde
queelesmantenhamumadiferen çaemrela çãoaorestodotexto,essamudan çanão
prejudicaausabilidadeouovisualdapágina. Pode-setrocarotomdeazul(cor
padrãodosnavegadoresparalinks),emudaroslinksparanegrito,oqueébastante
simples.
.place a {
color: #2C88A7;
font-weight: bold;
}
Figura2.7:Onovoestilodoslinks.
Assim,os3linksestãocomumestilopróprio,masdeixamosumlinkimportante
defora,odaprópriapágina. Écomumadicionaraotítuloumlinkquelevepara
apáginaprincipaldosite,quenonossocasoéaprópriapáginaemqueestamos.
MudemosocódigoHTMLdonosso h1paraadicioná-lo.
<h1><a href= ''>O que eu mais gosto em São Paulo</a></h1>
16


## Página 27

CasadoCódigo Capítulo2. Osprimeirospassoscomonossosite
Eéclaro,umacorespecialparaestelink:
h1 a {
color: #7E9F19;
text-decoration: none;
}
Figura2.8:Agoraonossotítuloestáverde!
Reutilizamosacorverdedasbordastracejadasquevimosanteriormente,eti-
ramososublinhadodotextodolink.Tambémpodemosmudaracordolinkpara
quandoseposicionarocursoremcimadele,utilizandoumpseudo-seletordoestado
hoverdoelemento.
h1 a:hover {
background-color: #7E9F19;
color: #FFF;
}
Agora,aoseposicionarocursordomousenotítulodapágina,overdequeantes
estavanotextoirápreencherofundodoelemento,eobrancoirátomarolugardo
verdedotexto.Quandoocursorsairdecimadotítulodapágina,olinkvoltaráao
seuestilotradicional.
Alémdo hover,existempseudoseletoresquepodemserutilizadosparaadi-
cionarumestiloespecíficoaoutrosestadosdelinksououtroselementos,eosmais
tradicionaissão:
•:focus,paraelementosqueestejamfocadospeloteclado,comolinksoucam-
posdeumformulário;
•:visited,paraendere çosjávisitadospelousuário;
•:active,paraoinstanteemqueoelementoestásendopressionadopelo
mouse.
17


## Página 28

2.5. Primeirocontatocomimagens CasadoCódigo
Figura2.9:Oefeitode:hoverdotítulo.
Sefornecessáriotrocarascoresdosite,seriaocasodealterarapenasasocor-
rênciasdecolor, background, background-coloretalvezde border.
2.5 Primeiro contato com imagens
Umdoselementosclássicosquenãoutilizamosatéagoraéo img,utilizadopara
exibirimagensquefazempartedoseuconteúdo-diferentesdeimagensutilizadas
noestilodasuapágina,quesãoaplicadasutilizandoapropriedade backgroundvia
CSS.Vamosdarumaolhadanissoenquantoadicionamosalgumasfotosnadescri ção
decadaumdoslugaresdeSãoPaulodequeestamosfalando.Adicionamosumatag
imgentrecada h2eosparágrafosdecadaumdoselementos .place.
<div class= 'place'>
<h2>Passear na Avenida Paulista!</h2>
<img src= 'images/paulista.jpg' alt="O céu da avenida Paulista,
foto por http://www.flickr.com/photos/jairo_abud">
<!-- os parágrafos vem aqui... -->
</div>
<div class= 'place'>
<h2>Os bares da Vila Madalena</h2>
<img src= 'images/piola.jpg' alt="A varanda do Armazém Piola,
foto por Fernando Moraes">
<!-- os parágrafos vem aqui... -->
</div>
<div class= 'place'>
<h2>O Parque do Ibirapuera</h2>
<img src= 'images/ibirapuera.jpg' alt="O Parque do Ibirapuera,
por http://www.flickr.com/photos/soldon/">
<!-- os parágrafos vem aqui... -->
</div>
18


## Página 29

CasadoCódigo Capítulo2. Osprimeirospassoscomonossosite
Oatributo srcdeveconterocaminhoparaoarquivodaimagem,enquantoo
altéoumtextoalternativoparaaimagemcasoelanãosejacarregadapelonave-
gador(nocasodocaminhoestarerradooualgumproblemanarededousuário).
Estemesmotextopodeviraserusadonoatributo title,paraexibirum tooltipna
imagem,masodeixamosdeladoparamanteroexemplosimples.
Enquantoonavegadorseencarregadedescobriralarguraeaalturadaimagem,
tambémpodemosfixaressesvalorescomosatributos widthe height-casoo
tamanhorealdaimagemsejadiferente,onavegadoriráredimensionaraimagem
conformeonecessário. FixaraalturaelarguradaimagemnoHTMLtambémé
útilparaqueonavegadorjá“reserve”ospixelsnecessáriosparaexibiraimagem,
evitandoqueoconteúdosejaempurradoparaosladosconformeéfeitoo download
daimagem,evitandoochamado repaintdapágina.Casoqueirapraticarisso,nossas
imagensestãocom 156pxdelarguraedealtura.
Atenção aos tamanhos
Imagensdetamanhomuitograndesãoumdosprincipaisresponsá-
veisporproblemasdeperformancenaweb.Mesmosevocêfixarumta-
manhoparaassuasimagensquesejamenordoqueoseutamanhoreal,o
arquivooriginalserátransferidopelaredeepodecausarumacertalenti-
dãocasoelassejampesadas,entãofiqueatentoaotamanhodasimagens
defundo,íconesefotosdassuaspáginas.
Porisso,nãodeixedecomprimirassuasimagensparaeconomizar
diversosbytesdetráfego.CasovocêutilizeoMacOSX,aconselhoausar
oImageOptim(http://imageoptim.com/)paraestatarefa
19


## Página 30

2.5. Primeirocontatocomimagens CasadoCódigo
Figura2.10: afotodaAvenidaPaulista,masparecequequebramosalgononosso
layout.
Criamosumproblemanolayoutdanossapáginacomessasimagens.O imge
osparágrafosnãoficamumdoladodooutro,eotextosóaparecelogoabaixoda
foto.Istoocorreporqueaimageméumelemento inlineeoelemento péblock.
Vamosentraremmaisdetalhesarespeitodissonase ção6.3,masoqueprecisamos
agoraéumasoluçãoparaanossapágina.Primeiro,aplicamosalgunsestilosàsima-
genseutilizamosapropriedade floatparaalinharoselementoshorizontalmente.
.place img {
border: 1px solid #7E9F19;
float: left;
margin: 10px 10px 0 0;
padding: 2px;
}
Issovaiadicionarumabordaverdenaimagem,eumespa çamentoentreelaeos
demaiselementos-comoasbordasda diveo h2acimadela. Apesardesoluci-
onaroproblemadeposi çõesdentroda divsobreaAvenidaPaulista,nosdemais
elementosaimagemvazaparaforada div-umdosproblemasclássicosdeseusar
apropriedade float.Vamosresolveristoadicionandoumelementovaziocoma
classe clearlogoapósosparágrafos. Eleirágarantirqueasimagenscontinuem
dentrodoseurespectivo divequeelesterãoaalturaadequadaparacontertodoo
seuconteúdo.
20


## Página 31

CasadoCódigo Capítulo2. Osprimeirospassoscomonossosite
<div class= 'place'>
<h2>Passear na Avenida Paulista!</h2>
<!-- a foto e os parágrafos aqui... -->
<div class= 'clear'></div>
</div>
<div class= 'place'>
<h2>Os bares da Vila Madalena</h2>
<!-- a foto e os parágrafos aqui... -->
<div class= 'clear'></div>
</div>
<div class= 'place'>
<h2>O Parque do Ibirapuera</h2>
<!-- a foto e os parágrafos aqui... -->
<div class= 'clear'></div>
</div>
EoCSSdaclasse .clear:
.clear {
clear: both;
}
Esteéumtruquebastanteconhecidoeutilizado,masnãosoumuitofãdelede-
vidoaoelementovazioextraqueéadicionadoaoHTML,semnenhumvalorsemân-
tico,queexisteapenaspararesolverumproblemadoestilodapágina.Vamosvoltar
aesteassuntosobreo floateaprenderumasolu çãomaispráticaeelegantepara
isto.
21


## Página 32

2.6. Adicionandoelementossecundários CasadoCódigo
Figura2.11:Afotocomseuestilo,posicionadacorretamente.
2.6 Adicionando elementos secundários
Bem,játemostodooconteúdodanossapáginanoseudevidolugarcomumpouco
deCSSparadeixartudomaisapresentável. Precisamosagorademaisalgunsele-
mentosadicionaisparacomplementá-la,comoumrodapéeumabarralateralcom
maisconteúdo,nocasoumalistaadicionaldeoutroslugaresdeSãoPaulo,massem
descriçõesoufotoscomoosquetemosatualmente. Vamosprimeiroaorodapé,o
maissimplesdosdois,comoseguintecódigo,aseradicionadonofinaldoelemento
.container.
<div class= 'footer'>
<p>Parte do livro "HTML5 e CSS3: Domine a web do futuro."</p>
</div>
EumpoucodeCSS,éclaro.
.footer {
font-size: 12px;
text-align: center;
}
Orodapéteráumafontemenoreserácentralizado. Diferentedamargemau-
tomáticaqueutilizamosno .containeranteriormente,estamoscentralizandoo
texto,enãooelementodorodapéinteiro.
22


## Página 33

CasadoCódigo Capítulo2. Osprimeirospassoscomonossosite
Opróximodanossalistaéabarralateral. OHTMLdeladeveseradicionado
antesdorodapéqueacabamosdecriar.
<div class= 'sidenote'>
<h3>E existem muitos outros lugares interessantes na cidade...</h3>
<ol>
<li>O Mercado Municipal.</li>
<li>A Sala São Paulo.</li>
<li>Os estádios dos principais times de futebol da cidade.</li>
<li>Diversos museus, como o Memorial da América Latina, Museu da
Língua Portuguesa e o Museu do Ipiranga.
</li>
<li>E mais!</li>
</ol>
</div>
Maisuma div,umtítuloemum h3eumalistaordenada,atag ol,comalguns
itensamais.EéclaroqueesteelementoacompanhaumpoucodeCSS.
.sidenote {
background-color: #FFFBE4;
border: 1px solid #C9BC8F;
padding: 10px;
}
.sidenote h3 {
font-size: 14px;
margin-top: 0;
}
.sidenote ol {
font-size: 12px;
}
23


## Página 34

2.6. Adicionandoelementossecundários CasadoCódigo
Figura2.12:Oestilodanossabarralateral.
Umpoucodecoreespa çamento,damesmaformaquevimosanteriormente,e
algunsajustesdotamanhodasfontesjáqueesteelementonãodevechamarmais
atençãodoqueonossoconteúdoprincipal. Eporserumabarra lateral,elanão
deveriapegartodaalarguradisponível,eseencaixaraoladodonossoconteúdo
principal.Éoutrocasodeusoparao float,comoutilizamosnocasodasimagens.
Primeiro,precisamoscolocartodooselementoscomaclasse placedentrodeuma
divnovaparasepará-losdorestodoconteúdo,eentãoadicionaroestilonecessário
paraesteelementoficarsempreàesquerdadapágina.
<div class= 'places'>
<!-- conteúdo principal vem aqui... -->
</div>
.places {
float: left;
width: 660px;
}
Agora,oconteúdoprincipalterá 660pxdelargura,eorestante(dos 960pxque
definimosparaalarguratotaldanossapágina)ficadisponívelparaabarralateral.
Entãovamosatualizaroestilodelaparaposicioná-lanoseulugardedireito.
.sidenote {
background-color: #FFFBE4;
border: 1px solid #C9BC8F;
float: right;
padding: 10px;
width: 260px;
}
24


## Página 35

CasadoCódigo Capítulo2. Osprimeirospassoscomonossosite
Comapropriedade floatcomovalor right,abarralateralvaificarsempre
noladodireito,enquantooconteúdoestáàesquerda.Ealargurafixa,queémenos
doqueoespa çorestantedapágina,deixaumespa çoamaisentreoselementose
garantequeassuasbordasnãovãosejuntaredeixarovisualumpoucoconfuso.
Sóoquefaltaécolocarorodapédevoltanoseulugar.Comousodo floatnos
outroselementos,eleagorafoipararabaixodabarralateral,enquantodeveriaestar
abaixodetudo,comoantes.Simplesmenteadicionamosaclasse clearaoelemento
dorodapé,evoilà!
<div class= 'footer clear '>
<p>Parte do livro "HTML5 e CSS3: Domine a web do futuro."</p>
</div>
Figura2.13:Abarralateral,noseudevidolugar.
2.7 Faça para sua cidade também!
Foisimples,não?Apósapenasalgumaspáginas,játemosumexemplosimples,ele-
ganteefuncionaldeumlayoutcomumapequenapitadadeCSS.Vamosapren-
dermuitomaisnospróximoscapítulos,inclusivetécnicasquepoderiamdeixaresse
exemplomuitomaisinteressante.
CasovocêestejacomeçandonessemundodeHTMLeCSS,quetalimplementar
umapáginasimilarparaasuacidade?Coloque-anoareeuficareimuitocontente
defazerumlinkparaela. Apenasmecontepore-mailoendere çodasuapágina.
Vocêpodeenviarparacasadocodigohtmlcss@gmail.com.
25


## Página 37

Capítulo3
HTML5:oquemudou?
OsurgimentodoHTML5mudoumuitascoisasnomundododesenvolvimentoweb,
comnovoselementos,novasfuncionalidadesediversasoutrasnovidadesquepos-
sibilitamexperiênciasmelhoreseintegra çõesqueanteseramapenasdesejoseso-
nhosdosdesenvolvedoresporaí. Mesmocomalgumasfuncionalidadesaindaem
processodedefini ção,jápodemosaproveitardiversasdasnovidadesqueoHTML5
trouxeparaomundo.
Vamospassarporumasdelas,inclusivealgumasquesãoreferentesaocódigo
queescrevemos:novoselementos,mudan çasdesintaxeeatributospersonalizados.
Masnãodeixedeconferirnocapítulo11sobreporondeaprendermaisarespeitode
outrasnovidades.
3.1 Escrevendo menos e fazendo mais
Umadasminhasmudan çasprediletasécomoatarefadeescreverHTMLficoumais
simples.Diversospontospequenossetornaramopcionaisoudesnecessárioseoque


## Página 38

3.1. Escrevendomenosefazendomais CasadoCódigo
anteserarepetitivodeixoudeserpartedanossarotinae,comoconsequência,onosso
códigosetornoumaissimplesefácildeseler.
Umótimoexemplodissoéo DoctypedoHTML5,ainstru çãoqueinformaaos
navegadorescomoeledeveprocessarocódigoHTML,queficoubastantesimples
emrelaçãoaoseusantecessores.NoHTML4ounoXHTML1,alinhado Doctype
éalgoassim:
<!- DTD do HTML 4, em modo "strict".
<!DOCTYPE HTML
PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
<!-- DTD transitional do XHTML -->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
Dificilmentealguémvaiconseguirlembrardetudoisso,egeralmentedeixamos
aresponsabilidadedeescreveralinhado Doctypeparaferramentasdegera çãode
projetosoudecódigo.Agora,eleestátãopequenoqueébemfácilescrevê-lodecor.
<!DOCTYPE html>
NãoexistemaisURLde dtdoutipode Doctypeparasepreocupar.Bastante
simples!
Alémdisso,astagsde linke scripttambémemagreceramumpouco.Agora,
parareferenciararquivosdeCSSeJavaScript,vocênãoprecisamaisinformaroatri-
buto type.Casoelenãoestejapresente,onavegadorirápresumirqueoarquivoé
dotipo text/cssou text/javascript.
<!-- O que antes era assim... -->
<link rel="stylesheet" href="normalize.css" type="text/css" />
<script src="prefixfree.min.js" type="text/javascript"></script>
<!-- ...pode ser escrito assim -->
<link rel="stylesheet" href="normalize.css">
<script src="prefixfree.min.js"></script>
Sevocêcompararosexemplosanterioresdatag link,podenotarqueabarrano
finaldatagtambémnãoestámaispresente-maisumdetalhequesetornouopcional
noHTML5.Tagsquenãoprecisamserfechadas,como link, input, img, bre
meta,nãoprecisammaisterminarem />,apenas >.
28


## Página 39

CasadoCódigo Capítulo3. HTML5:oquemudou?
3.2 Atributos personalizados
Emalgunscasosprecisamosadicionarmetadadosouinforma çõesextrasnonosso
HTML,masnãoqueremosdependerdeelementosadicionaisquenãopossuemvalor
deverdadenanossapágina. Umexemplomuitocomuméfazercomquealguma
bibliotecaleiaumatagàprocuradealgunsatributosespecíficos,comoporexemplo,
umatributoindicandoquearequisi çãodeumlinkdeveserfeitaassincronamente
viaAJAX.
<a href= 'posts/2' remote='true'>Apagar</a>
Oatributo remotenãoexistenadefini çãodatag a.Estaabordagemfuncionaria
empáginasdeHTML4,porexemplo,masoseucódigoestariainválidodeacordo
comaferramentadevalida çãodoW3C.
Umaformaderesolverissosãocomatributospersonalizados,quefazemparte
dodomíniodoseuprojetoeaomesmotempomantêmoseucódigoválido. Por
exemplo,paradefinirumlinkqueiráapagarumpostdoseublog,podemosutilizar
algumasconfiguraçõesviaatributospersonalizadoscomoprefixo data-.
<a href= 'posts/2' data-remote='true' data-method='delete'
data-confirm='Você tem certeza disto? '>Apagar</a>
Destaforma,oseuJavaScriptpodelerosatributosde data-*eexecutarocó-
digonecessárioparaapagaropost,pedindoumaconfirma çãodousuáriocomuma
mensagempersonalizada.
3.3 Tags nov as para elementos antigos
Nocampodasemânticaexisteumproblemacomplicadodeselidar,queéousoex-
cessivodatag div. UmverdadeirocoringadoHTML,queporserumelemento
genérico,acabamosutilizando-oparadefinirquasetodaaestruturadasnossaspá-
ginas,desdeocabe çalhoaorodapé.
Emboraissonuncatenhaimpedidoninguémdecolocarumsitedesucessono
ar,acabagerandoumcertoruídoeumanecessidadedeseutilizarclassesCSSpara
identificaropapeldecada divdentrodoquecriamos. Comisso,oHTML5traz
algunselementosparasupriressafaltadetagsmaissemânticasedescritivaspara
algunselementosclássicosemdiversoscenários,comocabe çalhos,menusdenave-
gaçãoeáreasdeconteúdosecundário.
Algumasdasalternativasexistentessão:
29


## Página 40

3.3. Tagsnovasparaelementosantigos CasadoCódigo
•section-utilizadopararepresentarumase çãogenérica,geralmentecom
umcabeçalhopróprioeoseuconteúdo;
•nav-representaçãodeumblocoprincipaldelinksdenavega ção-nemtodo
grupodelinksdevesertratadocomoum nav;
•aside-atagpodeserutilizadapararepresentarumase çãodeconteúdose-
cundárioouauxiliaroutropeda çodemaiorimportância. Cita ções,linksde
referênciaounotasadicionais,porexemplo;
•header-referenteaocabe çalhodeumase çãoespecífica(oudaprópriapá-
gina),contendotítulos,introdu çõeseoutroselementossimilares;
•footer-orodapéreferenteaumblocodeconteúdo;
•article-identificaoconteúdoemsi,comoumanotíciadeumportal,um
postemblogouumcomentárioemumalistadecomentários.
Figura3.1:Opapeldecadaelementonovoemumapáginacompleta.
30


## Página 41

CasadoCódigo Capítulo3. HTML5:oquemudou?
Umpontocrucialdessasmudan çaséquepodemosdefinirdiversasse çõesinde-
pendentesentresi,cadaumacomasuahierarquiaprópria.Porexemplo,podemos
ter2elementos h1,cadaumemsuase ção,oupodemoscriarum headerparao
cabeçalhodeumblog,comotítuloelinksdenavega ção,ecadapost,devidamente
criadoemum article,terum headercomotítulodoposteadataemqueele
foipublicado,porexemplo. Issopodeserbastanteútilparasearquitetarpáginas
maismodulares,paramelhoraraqualidadeeafacilidadedemanuten çãodonosso
código.
Figura3.2:Ummockupdoexemplodescrito-atag‘<header>’podeaparecerem2
seçõesdiferentes.
Combasenessalistaficafácildepensaremdiversoslugaresondeumatag div
foiutilizadacomalgumaclasseparaidentificaroseupropósito.Oqueachadepra-
ticarumpoucoesseselementosnovosnanossapáginasobreSãoPaulo?
3.4 Refatoração da página de São Paulo
Nossapágina O que eu mais gosto em São Paulo temalgunspontosemquepode-
mossubstituirousodatag divporalgunsdoselementosnovosdoHTML5.Não
teremosnenhumamudan çavisualnapágina;apenasasemânticadocódigoescrito
31


## Página 42

3.4. RefatoraçãodapáginadeSãoPaulo CasadoCódigo
irámudar.Adiferençanotamanhodoarquivoounaquantidadedecódigoescrito
éinsignificante,entãonãovamosnospreocuparcomisso.
Vamoscomeçarpelonossoconteúdoprincipal,os3lugaresdeSãoPauloquesão
descritoscomaclasse .place.Podemosalteraresseselementosparautilizaratag
article,removendoanecessidadedaclasseparaidentificaresteselementos.
<article>
<h2>Passear na Avenida Paulista!</h2>
<img src= 'images/paulista.jpg' alt="O céu da avenida Paulista, foto
por http://www.flickr.com/photos/jairo_abud">
<p>
Um dos principais centros financeiros da cidade, a avenida Paulista
também possui diversas opções de entretenimento. Endereço do Museu de
Arte de São Paulo, <em>MASP</em>, do Teatro Gazeta e muitos outros,
a região é de fácil acesso graças às diversas linhas de ônibus que
cruzam a avenida e à linha de metrô que passa por baixo dela.
</p>
<p>
A Avenida Paulista sempre é assunto. O que será que estão falando a
respeito no <a href= 'https://twitter.com/#!/search/Av.%20Paulista'
target='_blank'>Twitter</a>?
</p>
</article>
Eclaro,alteraronossoCSSpararefletirestamudan ça,trocandoondeantesusá-
vamosaclasse placepelatag article.
Opróximolugarquepodemosalteraréoelementocomaclasse .sidenote,
anossabarralateral,quepossuiumconteúdoadicionalaoquemexemosanterior-
mente.Umótimocandidatoasetornarum aside.
<aside>
<h3>E existem muitos outros lugares interessantes na cidade...</h3>
<ol>
<li>O Mercado Municipal.</li>
<li>A Sala São Paulo.</li>
<li>Os estádios dos principais times de futebol da cidade.</li>
<li>Diversos museus, como o Memorial da América Latina, Museu da
Língua Portuguesa e o Museu do Ipiranga.</li>
<li>E mais!</li>
32


## Página 43

CasadoCódigo Capítulo3. HTML5:oquemudou?
</ol>
</aside>
SemdeixardealteraroCSS,trocandoasreferênciasaclasse .sidenotepela
tag aside.
aside {
background-color: #FFFBE4;
border: 1px solid #C9BC8F;
float: right;
padding: 10px;
width: 260px;
}
aside h3 {
font-size: 14px;
margin-top: 0;
}
aside ol {
font-size: 12px;
}
Eporfim,ousodaclasse .footernonossorodapééoutrocasoóbviode
mudança.
<footer class= 'clear'>
<p>Parte do livro "HTML5 e CSS3: Domine a web do futuro."</p>
</footer>
footer {
font-size: 12px;
text-align: center;
}
ExistemoutrospontosquepoderíamosmudarnonossoHTML:substituira div
comaclasse .placesporum section,ecolocarum headeremvoltadotítulo
danossapágina h1,masnãoprecisamoschegaratanto.
Nossosusuáriosnãonotariamessamudan ça,masestamosagregandomaisse-
mânticaaonossocódigoefacilitandosualeitura,paramanuten çõesfuturas.
33


## Página 44

3.5. Sejapragmático CasadoCódigo
Preenchendo alguns buracos
Quandoumnavegadornãopossuisuporteaumatagdesconhecida
paraele,oelementoéexibidonapágina,poremnenhumestiloéaplicado.
ÉassimqueversõesantigasdoInternetExplorer,porexemplo,tratam
elementos novoscomoo sectioneo header. Sevocêforutilizar
algumasdessastagseprecisadarsuporteanavegadoresqueaindanão
entendemelementosnovosdoHTML5,asolu çãoéutilizarumpoucode
JavaScriptparafor çaraaplica çãodeestilopelonavegador.
Oscriptmaisutilizadoparaistoéo html5shiv(https://github.com/
aFarkas/html5shiv/),quealémdetrataraaplica çãodeestilosnessesele-
mentostambémtrataalgunsproblemasrelacionadosàimpressãodapá-
ginaqueutilizetagsdoHTML5.
3.5 Seja pragmático
Enquantoessemundodenovaspossibilidadesetagsànossadisposi çãopodepa-
recerasolu ção,émuitofácilseperdernoméritodasdiscussõesedefini çõesdo
tipode "isto aqui deveria ser um article ou um section?” . Continuarutilizaratag
divnãocausamalnenhum,evocêsemprepodevoltarnoseucódigodepoisetro-
caralgumatagporoutraquevocêconsideremaisadequada. DivyaManianfala
bastantesobreosproblemasqueessabuscaincessanteporsemânticapodecausar
emumpostnaSmashingMagazinehttp://coding.smashingmagazine.com/2011/11/
11/our-pointless-pursuit-of-semantic-value/. Opontoimportanteénãoperdero
focodoquerealmenteprecisamosfazer.
34


## Página 45

Capítulo4
Oquetododesenvolvedorprecisa
sabersobreCSS
EntenderasintaxeeaspropriedadesdoCSSévital,porémmaisimportantedoque
issoéaprenderalgunstruquesetécnicaspararesolverproblemasdodiaadia.Saber
apenasalinguagemnãoéosuficiente,éprecisosabercomousá-laequaissãoassuas
opçõesquandoprecisarcolocaramãonamassa.
4.1 A incompatibilidade dos browsers e a razão dos
resets deCSS
Todososnavegadores,dasprimeirasversõesdoInternetExploreraosnavegadores
decelularesetablets,possuemestilospadrõesquesãoaplicadosemtodasaspági-
nas,comoonegritodatag strong,abordado legendeostamanhosdefonte
diferentesdo h1ao h6. Eéclaroqueexistemdiferen çasentreospadrõesdeum
navegadorparaoutro.Algumasdessasdiferen ças,pormenoresquepossamser,cos-


## Página 46

4.1. AincompatibilidadedosbrowsersearazãodosresetsdeCSS CasadoCódigo
tumamafetaronossotrabalho,impactandonoresultadofinaldaspáginasquando
visualizadasemdiferentesnavegadores.Solu çõesespecíficasparaessescenáriospre-
cisamserutilizadas.
Paraentendermelhorestasitua ção,podemostestarumpoucodeHTML,sem
estilos,evercomoeleseráexibidonoGoogleChromeenoFirefox,porexemplo.
<h1>Título</h1>
<fieldset>
<legend>Campos do formulário</legend>
<abbr title="Hypertext Markup Language">HTML</abbr>
<p><label>Faça a sua pesquisa:</label><input type="search"></p>
<textarea>Um pouco de texto</textarea>
</fieldset>
Figura4.1:OresultadonoFirefox9.0.1
Figura4.2:OresultadonoChrome19.0
Conseguimosnotarlevesdiferen ças,quepodemimpactaronossotrabalhofinal.
Asbordasdo fieldset,aausênciadosublinhadonoelemento abbrnoChrome
easdiferen çasdoscamposdebuscaedetexto.
36


## Página 47

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
Comoqualquerproblemarecorrentenomundodedesenvolvimento,solu ções
jáforamcriadasparanãonospreocuparmoscomcoisasassimefocarmosnotraba-
lhodeverdade. Osarquivosde reset,comosãochamados,possuemumagamade
regrasparaalinharosnavegadoresemummesmopatamardeestilo,sejacorrigindo
problemasouresolvendoinconsistências.
Talvezomaisfamosodos resetssejaoEscritopeloEricMeyer,quecriouaversão
1.0em2008-bastantetempo,não?-suaúltimaatualiza çãofoifeitaem2011,evocê
podeencontrá-lanopróprioblogdoseucriador,http://meyerweb.com/eric/tools/
css/reset/.
OsdesenvolvedoresdoYahoo!tambémcriaramum resetsólido,partedo Y ahoo!
User Interface Library,disponívelnositehttp://yuilibrary.com/.Umpontonegativo
do resetdoYahoo!équeeleremovealgunspadrõesqueeuconsideroimportanteem
algunselementos,comoonegritodatag strongeamarca çãolateraldeitensem
umalista.
Normalize.css
ONormalize.css(http://necolas.github.com/normalize.css/),éo resetqueesta-
mosutilizandonestelivroetomaumaabordagemdiferenteparaesseproblema.No
lugardesobrescreverdiversaspropriedadesparadefinirumnovopadrãodeestilo
paraosnavegadores,eleapenasadequaospontosdiferentes,preservandodiversos
estilosaplicadospelosnavegadores,alémdeaproveitarparadefiniralgumasmelho-
riassutis,removendoo outlinedelinksemelhorandoaformata çãodeelementos
pre,porexemplo.[3]
OcódigofontedoNormalizeémuitobemescritoedocumentado,oquelhe
permiteremoverpartesquenãoteinteressemouentendermelhoroqueelefazpor
debaixodospanos.Confiraoexemplodecódigoaseguir:
/*
* 1. Improves usability and consistency of cursor style between
image-type 'input' and others
* 2. Corrects inability to style clickable 'input' types in iOS
* 3. Removes inner spacing in IE7 without affecting normal text inputs
* Known issue: inner spacing remains in IE6
*/
button,
input[type="button"],
37


## Página 48

4.2. CompreendendooBoxmodel CasadoCódigo
input[type="reset"],
input[type="submit"] {
cursor: pointer; /* 1 */
-webkit-appearance: button; /* 2 */
*overflow: visible; /* 3 */
}
Cadapropriedadeédevidamentedocumentada,esabemosquaisversõesdos
navegadoresprecisamdascorre ções.Casovocênãoqueriasepreocuparcomversões
doInternetExplorerabaixoda8,porexemplo,vocêpoderemoverdocódigofonte
doNormalizeasregrasespecíficasdestasversões.
Figura4.3:OnossoHTMLdeteste,agoracomoNormalize.css
Nãosaiadecasasemoseu
Independentedequal resetvocêforusar,omaisimportanteéestarusandoum,e
façadissopartedoseuprocessodedesenvolvimentoaoparticipardenovosprojetos.
Istonãotiraaresponsabilidadedetestarmanualmenteaspáginasemdiversos
navegadores,masimpedequealgunsproblemasrelacionadosaposicionamento,ta-
manhosefontesapare çamdonadaevocêtenhaquededicartempoaelesaoinvés
desededicaraoqueprecisasercriado.
4.2 Compreendendo o Box model
Nãoimportaquaiscores,imagensdefundoouposi çãovocêadicionaremumele-
mento,elesempreserátratadocomoumacaixa. Issopodenãoserperceptívelà
primeiravista,masbastacome çarausaruminspetordeelementoscomooFirebug
ouoconsoledoWebKitevocêiráseacostumarcomestaabordagem.O Boxmodel
écomoaspropriedadesdeCSScompõemasdimensões,ondealémdo widthedo
38


## Página 49

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
height,aspropriedades bordere paddingtambéminfluenciamnoresultado
final,masdeumaformaumtantoquantoconfusa.Considereocódigoaseguir.
.button {
border: 1px solid #999;
height: 26px;
padding: 5px 15px;
width: 90px;
}
Estaclasse button, aoseraplicadaemumelementoqualquer, iráocupar
122pxdelargurae 38pxdealturanasuapágina. Issoaconteceporqueosvalo-
resde paddinge bordersãosomadosàlarguraeàalturadefinidas,fazendocom
queaspropriedades widthe heightsejamresponsáveispordefinirapenasalar-
guraeaalturadoseuconteúdo,enãodoelementocomoumtodo.Alémdaconfu-
sãoquepodesergeradaaosecalcularostamanhosdeantemão,issotornabastante
complicadoousodevalorescomporcentagemnestaspropriedades-umelemento
com 100% de widthe 2pxdebordasficarámaiordoqueos 100% definidos.
Complicado,não?
Outroexemploparailustraresteproblema:amboselementospossuemomesmo
valorde width,masovalordo paddingdosegundoodeixacom 300pxde
largura.
.box {
background-color: LimeGreen;
width: 250px;
}
.box-with-padding {
background-color: LightBlue;
padding: 0 25px;
width: 250px;
}
<div class= 'box'>elemento sem padding</div>
<br>
<div class= 'box-with-padding'>elemento com padding</div>
39


## Página 50

4.2. CompreendendooBoxmodel CasadoCódigo
Figura4.4:Opaddingdosegundoelementoexpandeasualargura.
EstaéaregradoBoxmodel: aplicarestesvaloresapenasaoconteúdoenão
utilizarcomolimitesfixosdoelementocomoumtodopodecomplicardiversosca-
sosdediagrama çãodeelementosempáginascomplexas.Masépossívelalterareste
comportamentoenãoficarrecalculandolargurasealturasbaseadoembordasees-
paçamentos. Apropriedade box-sizing,umadasnovidadesdoCSS3,permite
alterarestaregrade content-boxparaovalor border-box,quefor çaonavega-
dorarespeitaresteslimiteseocuparoespa çointernodoelementocomosvalores
de bordere padding,nolugardeexpandiroelemento.
Destaforma,asduasdefini çõesabaixoirãogerarelementoscomamesmalar-
gura
* {
box-sizing: border-box;
}
.box {
background-color: LimeGreen;
width: 250px;
}
.box-with-padding {
background-color: LightBlue;
padding: 0 25px;
width: 250px;
}
40


## Página 51

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
Figura4.5:Obox-sizingtornandoamboselementosdomesmotamanho.
4.3 Utilizando pseudo elementos
Existemcasosemqueastagsqueutilizamosparadefinironossoconteúdonãosão
osuficienteparaestruturaroselementosdeinterfacequedesejamos.Sejaparatratar
problemasdefloat,definirbordasadicionaisoualgosimilar,muitasvezesacabamos
dependendodeelementosvaziospararesolveressesproblemas. Porexemplo,ao
trabalharcombordasarredondadassemousodeCSS3,jávi(eescrevi),coisasassim,
emqueo spanéutilizadoparacriarasbordasdoladodireitodeumbotão.
<div class= 'button'>
<a href= '#'>Clique aqui</a>
<span></span>
</div>
Jáfoimuitocomumutilizarsolu çõesassimparatrabalharcomsombras,bordas
arredondadas,letrasiniciaisdetítuloseoutrosdetalhesdeinterfacequenãocon-
seguimoscriarapenascomomínimodecódigoHTML.Masexistemalternativas
bastanteinteressantesparaisto,utilizandoapenasCSS.São pseudo elementos,que
nãoexistemnonossocódigoHTML,masquepodemreceberestilosespecíficose
auxiliaraestruturarelementosmaiscomplexosnasnossasinterfaces.Osmaistra-
dicionaisdelessãooselementos ::beforee ::after,quevivemantesedepois
doconteúdodeumatag(enãoantesedepoisdatagemsi),eestãodisponíveispara
todasastagsqueadicionarmosao bodydanossapágina.
4.4 Desenhando uma faixa com “before ” e “after”
Vamoscriarumafaixaquedáailusãodequeelacontornaum sectionqueo
contém,eoselementos ::beforee ::afterirãofazerotrabalhopesadoparaa
gente.Come çamoscomomínimodeHTMLnecessário,umatag sectioneum
títuloparaafaixa.
41


## Página 52

4.4. Desenhandoumafaixacom“before” e “after” CasadoCódigo
<section>
<h1>Um exemplo de pseudo elementos</h1>
</section>
AdicionemosumpoucodeCSSparadefiniralargurado sectioneaposi ção
dotítulo.
section {
border: 1px solid #000;
height: 100px;
margin: 40px auto;
width: 400px;
}
h1 {
font-size: 1.2em;
text-align: center;
}
Figura4.6:Oelementosectioncom400pxdelargura.
Começaremosatransformaronosso h1nafaixaquequeremoscriar.Alémda
cor,vamosposicionaraslateraisdafaixaparaforadase ção.
h1 {
background-color: #990000;
color: #FFF;
font-size: 1.2em;
left: -10px;
padding: 5px 0;
position: relative;
text-align: center;
width: 420px;
}
42


## Página 53

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
Figura4.7:Oladofrontaldafaixavermelha.
Agora,temos 10pxdecadaladodafaixa vazandopelaseção,sóprecisamoscriar
oefeitodafaixacontornandoo section,utilizandopseudo-elementos.Primeiro,
vamoscriaresseefeitoparaoladoesquerdodafaixa,utilizandoo ::before.
h1::before {
border: 5px solid #7C0000;
content: "";
left: 0;
position: absolute;
top: -10px;
}
Figura4.8: Desenhamosumquadradonocantodafaixacomopseudoelemento
‘::before’.
Fazemosreferênciaaobeforeutilizandoamesmasintaxedepseudoclassesque
utilizamosparalinks,como :separandooselementos.
Utilizandoo positionjuntodecoordenadasexatascomaspropriedades left
e top,conseguimosposicionaroelementoexatamentenocantosuperioresquerdo
dafaixaecomumabordade 5px,desenhamosumquadradode 10pxnolugar.
Apropriedade contentéutilizadaparadefiniroconteúdodoelemento-já
quenãoestamosadicionandooelementopeloHTML-enestecasonãoprecisamos
deconteúdoalgum.Paraconseguiroefeitoquequeremos,énecessáriotransformar
oquadradoquecriamosemumtriângulo.Sóprecisamosdeumajustenascoresdas
bordas.
43


## Página 54

4.4. Desenhandoumafaixacom“before” e “after” CasadoCódigo
h1::before {
border-color: transparent #7C0000 #7C0000 transparent;
border-style: solid;
border-width: 5px;
content: "";
left: 0;
position: absolute;
top: -10px;
}
Figura4.9:Oquadradosetornouumaabadafaixa.
Trocandoalgumasdascorespara transparent,conseguimosdesenharum
triângulonolugardoquadradovermelho. Paraduplicaresseefeitonooutrolado
dafaixa,utilizandoo ::after,sóprecisamosinverteralgunsdetalhes-oqueera
feitocomapropriedade leftseráfeitocoma right,easposi çõesdalistadecores
tambémprecisamsermodificadas,destaforma.
h1::after {
border-color: transparent transparent #7C0000 #7C0000;
border-style: solid;
border-width: 5px;
content: "";
position: absolute;
right: 0;
top: -10px;
}
44


## Página 55

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
Figura4.10:Afaixacompleta,utilizando‘before’ e ‘after’.
Feito! Criamosoefeitodafaixacontornandoase ção,semprecisardenovos
elementosnoHTML.
“:after”ou“::after"?
Écomumverporaiousodospseudo-elementos beforee after
emduasformasdiferentes: prefixadacomdoispontos( :before)ou
quatropontos( ::before).Vocêsabeadiferençaentreeles?
Efetivamente,nenhuma.Aespecifica çãodoCSS2criouaversãocom
doispontos,maselafoimudadanoCSS3paraserdiferentedasdefini-
çõesdepseudo-seletores.Navegadoresmodernospossuemsuporteaos
doisformatos,enquantoalgumasversõesantigassóentenderoformato
dedoispontosdoCSS2.
4.5 Decorando mensagens
Outrautilidadedospseudo-elementosécriarformasdebotõesqueantessóerapos-
sívelcomousodeimagensdefundo. Usandoumalógicasimilaràutilizadano
exemplodafaixa,podemoscriarumbalãodeajudacomumaindica çãoarespeito
doqueeleé.Imagineoseguinteparágrafo,sendousadoemumformuláriodeca-
dastrodeumsitedeumconcursoqualquer:
<p class= 'help'>
Preencha o campo com um e-mail válido, assim poderemos entrar em
contato com você para informar o resultado do nosso concurso.
</p>
Podemosadicionarumpoucodeestiloetransformaresteparágrafoemuma
caixadeajuda.
45


## Página 56

4.5. Decorandomensagens CasadoCódigo
.help {
background-color: #F1EFE6;
border: 1px solid #D3CDAE;
font-size: 0.9em;
padding: 10px;
position: relative;
width: 300px;
}
Figura4.11:Oestilodacaixadeajuda.
Considerandoqueesseelementoestáaoladodeumcampodee-mail,podemos
simularumasetanalateraldacaixadeajudaapontandoparaocampodoformulário,
demonstrandoarela çãoentreamensagemeocampoqueousuárioirápreencher.
Utilizaro ::beforeparacriarestasetaéumaótimaop ção.
.help::before {
border-color: transparent #D3CDAE transparent transparent;
border-style: solid;
border-width: 14px;
content: "";
left: -28px;
margin-top: -14px;
position: absolute;
top: 50%;
}
Figura4.12:Asetalateraldacaixadamensagemdeajuda.
46


## Página 57

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
Utilizamosamesmalógicadasbordasdafaixaquecriamosanteriormentepara
transformaresseelementoemumtriângulo,edefinimosaposi çãoexatadelecoma
combinaçãodapropriedade positionedascoordenadascom tope left.Mas
partedotruqueéapropriedade topcom 50% ea margin-topnegativa,oque
oforçaaficarsemprecentralizado,independentedaalturadoparágrafo.
4.6 C riando conteúdo através de CSS
Além de serem bastante úteis para desenhar novos elementos na página, esses
pseudo-elementostambémpodemgerarconteúdoparacomplementarseuselemen-
tosdereferência.Apropriedade contentaceitapedaçosdetextoparapreencher
oseuconteúdo-masvocênãopodeadicionarcódigoHTML,infelizmente.
Talvezoexemplomaisclássicodessafuncionalidadeéodeexibiroendere çode
linksdapáginalogoapósoseutexto-umaótimapedidaparaestilosdeimpressão,
queveremoslogomaisnestecapítulo. Mastambémpodemosadicionaríconese
outrostiposdeelementosdecorativosparacomplementaronossoconteúdo. Por
exemplo,emumtextoinformativonãotãorelacionado,conseguimosadicionara
indicaçãodeumamãoapontandoparaotexto,assim:
<p class= 'tip'>Você sabia que...</p>
Paraposicionarumaindica çãopróximaaotexto,bastaousodo ::before
juntodeumsímboloUnicodequerepresentaumamãoapontandoodedo.
.tip::before {
content: "\261E";
margin-right: 10px;
}
Figura4.13:Adicionamososímbolounicodeatravésdapropriedade‘content’.
Pronto-nãoprecisamosdeumaimagemdeumíconeespecíficoparaisso.
Outrocasodeusoparagerarconteúdocompseudo-elementoséaoadicionar
estiloaelementosdecita ção,comoo blockquote. Ébastantesimplesadicionar
47


## Página 58

4.6. CriandoconteúdoatravésdeCSS CasadoCódigo
aspasemtornodotextoparaindicarqueaqueleconteúdosetratadeumacita ção.
ComeçandocomomínimonecessáriodeHTML:
<blockquote>
O problema com citações na Internet é que você não pode
confirmar a sua veracidade.
</blockquote>
EumpoucodeCSSparaformataracita ção:
blockquote {
color: #444;
font-style: italic;
}
Figura4.14:Umblocodecita çãolevementeformatado.
Podemoscolocaraspasaoredordotexto,comumafontemaioreumacordi-
ferente,apenasadicionandooconteúdonecessáriono ::beforee ::aftere
ajustandooseuestilocomonecessário.
blockquote::before, blockquote::after {
color: #000;
font-size: 3em;
}
blockquote::before {
content: "\201C";
}
blockquote::after {
content: "\201D";
}
48


## Página 59

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
Figura4.15:Asaspasadicionaisviapseudoelementos.
Comoo ::beforeeo ::afterherdamaspropriedadesdoseuelemento,
precisamossobrescreveracordotextoedefinirumtamanhodefonte(trêsvezes)
maior.
Um ponto chave para posicionar pseudo -elementos
Comovocêpodeternotadoemalgunsdosnossosexemplos,aspro-
priedades position, tope leftsãobastanteimportantesparaga-
rantirquenossospseudo-elementosestejamemseuslugaresexatos.Não
deixedeconferirase ção6.4,naqualiremosconferiremdetalhesouso
destaspropriedades.
4.7 Arquitete o seu CSS para o futuro
EscreverCSSpodeserfácil,masescreverCSSbemescritoéumahabilidaderela-
tivamenteraraepreciosa. Conformeosseusprojetosvãoganhandonovasfunci-
onalidadesesofrendomudan çasvisuais,vocêpodeseencontraremsitua çõesem
quealterarosestilosdeumelementoouadicionarumavaria çãodealgoexistente
podeserumatarefaherculana,eaduplica çãodecódigosótrazmaiscomplica ções
eproblemasparaasuaequipeeoseuprojeto.Porisso,éimportanterefletirsobreo
códigoCSSescritoetratarasuamanuten çãocomamesmaaten çãoquesecuidado
códigodasuaaplica ção,independentedalinguagemquevocêutiliza.
Escolhabemseusseletores
UmdosvilõesclássicosdeumCSSmalcuidadoéacomplexidadedeseletores
usados.Alémdadegrada çãodaperformancedassuaspáginas,compreenderoes-
copodeumaseletorparaalteraralgumapropriedadepodesercomplicado.
49


## Página 60

4.7. ArquiteteoseuCSSparaofuturo CasadoCódigo
Paraentenderoimpactodeperformanceénecessárioentendercomoosnavega-
doresprocessamosseletoresqueescrevemos.Considereoseguinteseletor: ul#nav
li a.
Onavegadorcome çaráaleroseletordetrásparafrente-aocontráriodoque
nósestamosacostumadosaler,oquesurpreendediversosdesenvolvedores-eirá
procurarnapágina todososelementosdatag a. Apósisso,eleiráfiltrarestalista
portodosqueestejamcontidosemumelemento li,eentãoportodosquetambém
estejamdentrodeumelementocomid nav.Eporfim,todosemqueoelemento
comoid navsejadatag ul.
ConsiderandoqueoHTMLparaumaestruturadessasseriaumalistanãoor-
denadaapenascomlinks,algocomo #nav aseriaumasolu çãomaissimplespara
onavegadorprocessar,ecomomesmoefeito.Ouatémesmoutilizandoumaclasse
nav-link,porexemplo,diretamentenoselementos adentrodalistacomoid nav.
Outropontoquegeramuitadiscussãoeconfusãoentredesenvolvedores:utilizar
idsouclasses? Enquantoidspodemsermaisrápidosparaonavegadorprocurar
oselementosnecessáriosnaárvoredoDOM,adiferen çadeperformanceéínfima,
entãoadiscussãoacabamaisnoassuntodepreferênciapessoal.Classessãoótimas
paracompordiversosaspectoscompartilhadosentrevárioselementos,eidsajudam
aindicarqueoseletoréespecíficoparaumelementoúnicodapágina.
Umaregrapessoalqueeutentoseguiréevitarseletorescommaisde3partes,
como header .nav a. Casovocêseencontreescrevendoseletoresmaioresque
algoassim,pareerevejaasuaestruturaparaquenãosejanecessárioescreverseleto-
restãograndes-sejautilizandomaisclassesoureduzindoaespecificidadedosseus
seletores.
Compondopadrõesvisuaisatravésdeclasses
NicoleSullivanpopularizouumaabordagemnaescritadeCSSecomposi çãode
estilos,similaraOrienta çãoaObjetos,queéutilizadaemlinguagensdeprograma-
ção.OOOCSS-ObjectOrientedCSS-propõeasepara çãodaestruturadosestilos
eos containersdeseuconteúdo.
Oobjetivoéescreverumcódigomaisfragmentadoereutilizável,noqualclasses
diferentessãoutilizadasparaformarocomportamentofinaldeumelemento,inde-
pendentedatagqueelepossuaouocontextoemqueeleseencontre-dentrodeuma
lista,umformulárioouocabe çalhodapágina.
Tomecomoexemploos2botõesaseguir.
50


## Página 61

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
Figura4.16:ComovocêestruturariaoCSSparaesteselementos.
Podemossepararosaspectosdesseselementosem4classesdiferentes:umapara
definirosestilosbásicosdeumbotão,umaparaascoresdobotãoprincipal,eoutras
duasparacontrolarostamanhosdecadaum,assim:
<a href="#" class= 'button primary-button big-button '>Enviar mensagem</a>
<a href="#" class= 'button small-button '>Cancelar</a>
.button {
background-color: #999999;
color: white;
display: inline-block;
font-weight: bold;
padding: 0.5em 1em;
text-decoration: none;
}
.primary-button {
background-color: #389739;
}
.big-button {
font-size: 1.1em;
}
.small-button {
font-size: 0.9em;
}
Destaforma,botõesemoutraspáginasequepossuamdetalhesdiferentes(como
umacordefundodiferente,ouumíconeposicionadoaoladodotexto)podemcom-
partilharosestilosbásicosdeumbotãoeaplicarosseuspontosespecíficoscomou-
trasclasses,como danger-buttonou icon-button.Estaabordagempodeser
estendidaparamenusdenavega çãoouconteúdosrelacionados,ouumarela çãode
posts-ofamoso mediaobject dosexemplostradicionaisdeOOCSS.[7]
51


## Página 62

4.8. Gererelatóriosinteligentesesimplescomosestilosdeimpressão CasadoCódigo
4.8 Gere relatórios inteligentes e simples com os
estilos de impressão
Osnavegadoresnospermitemadicionarestilosespecíficosparaquandoumapágina
forimpressapelousuário. Istopodeserfeitodeduasmaneiras: Comoatributo
medianatag linkoucriandoumblocodeCSSdentrodadiretiva @media print,
conformeosexemplosaseguir.
@media print {
/* Este CSS só será aplicado quando a página for impressa */
}
<!-- O atributo "media" indica que estes estilos
só devem ser aplicado para impressões -->
<link href="print.css" media="print">
Aprimeiraformaéamaisadequada,jáqueevitamosumanovarequisi çãoao
arquivodeimpressão.Ecomoosestilosdeimpressãocostumamserpequenos,não
existemproblemasemadicionaresteCSSaofinaldoestilopadrãodasuapágina.
Pode-seconsiderarqueaimpressãodepáginaséalgodopassado,masdepen-
dendodotipodeconteúdocomquevocêtrabalha,eoseupúblico,issopodeser
bastanteimportanteparaoseuprojeto.
Porexemplo,aoutilizaro Airbnb(http://airbnb.com)paraalugarumaparta-
mentoparaumaviagemaosEstadosUnidos,éinteressanteimprimiroitinerário
daviagem,quepossuiendere ços,datasetelefonesúteiscasovocêtenhaalgumpro-
blemaaopousarnoseudestino,ondevocêprovavelmentenãoteráumaconexãode
internetdisponívellogoaochegar. OuaocriarumtrajetopelacidadenoGoogle
Maps,vocêpodeimprimiromapacomoseuroteiroparateremmãosaodirigir.
Alémdissoaimpressãodaspáginasnãoficaresumidaateroconteúdoemuma
folhadepapel,jáquehojeemdiaébastantesimplesdeseexportarumapáginada
webparaumarquivo .pdfutilizandooprocessodeimpressãodosnavegadores.
Vocêconseguecompartilharpáginasee-mailsouarquivarpáginasderecibosde
comprasoupagamentosdeservi çospelainternet.
Independentedotipodeconteúdocomquevocêestivertrabalhando,existem
práticasrecomendadasparatratarosestilosdeimpressão,visandoalegibilidadee
tirandoelementosdesnecessáriosdafrentedecoisasmaisimportantes. Vamosre-
passaralgunsdeles.
52


## Página 63

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
Nãocontecomcores
Nãopodemosdependerdaqualidadeedagamadecoresdisponíveisaoimprimir
apágina,poisnãotemoscontroleouinforma çõessobreaqualidadedohardwareou
dadisponibilidadedetinta,entãoorecomendadoésemanternobrancoepretode
praxe.Entãopodemosremovertodotipodecorouimagemdefundo,efor çaracor
donossotexto,assim:
@media print {
* {
background: transparent !important ;
color: #000 !important ;
}
}
Ousodo !importantéparagarantirqueestaregrasobrescrevaqualquerou-
troseletormaisespecíficodoseuCSSpadrão,paragarantirquetudosemantenha
nacorpreta. Alémdisso,érecomendadoremoverqualqueroutrapropriedadede
estilovisual,como box-shadowe text-shadow,alémderevisaracordasbordas
utilizadas.
@media print {
* {
background: transparent !important ;
border-color: #000 !important ;
box-shadow: none !important ;
color: #000 !important ;
text-shadow: none !important ;
}
}
Aoremoverapropriedade backgroundcompletamente,tambémestamosre-
movendoimagensdefundo.Casoalgumadestasimagensdevesseestarpresentena
suaversãodeimpressão,consideremovê-laparaumatag img.Eocontráriotam-
bém-navegaçõescriadascomimagensdeveriamsertrocadasportextosimplesao
serimpresso.
53


## Página 64

4.8. Gererelatóriosinteligentesesimplescomosestilosdeimpressão CasadoCódigo
Figura4.17:Ocabe çalhodoLast.fm,queutilizadiversasimagensparacomporologo
eomenuprincipal.
Figura4.18:Ocabe çalhoimpresso,semologoecomasimagensdomenunolugar
deumtextocomum.
Linksdevemserlinks
Comaausênciadecores,todososseuslinksazuis,verdesouvermelhosterão
amesmacorpretadoseuconteúdo. Umaformadediferenciaroslinksdotexto
comumésublinhando-os,casovocêtenharetiradoistodoestilodosseuslinks.
a {
text-decoration: underline !important ;
}
Outratécnicarecomendadaparatratarlinksemcasosdeimpressãoéexibiro
caminhoqueelespossuemlogoapósoseutexto.Istoépossívelutilizandoopseudo-
elemento ::afterdoslinks,juntodafun ção attr(),quepermitelerosatributos
deumelementoatravésdeCSS.
a[href]::after {
content: " (" attr(href) ")";
}
Destaforma,todososlinkscomum hrefpresenteterãooseucaminhoexibido
entreparêntesesaoseulado.Linksquenãopossuemumaurlaseguir,comolinks
queutilizamfun çõesdeJavaScriptnãodevemreceberesteefeito,entãoprecisamos
54


## Página 65

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
removeropseudo-elementonestescasos,utilizandoumseletormaisespecíficoque
oanterior:
a[href]::after {
content: " (" attr(href) ")";
}
a[href^="javascript:"]::after, a[href^="#"]::after {
content: "";
}
Controlandoquebrasdepáginas
Enquantononavegadoronossoconteúdoexisteemapenasumapágina,na
impressãoexisteanecessidadedesequebraroconteúdoempáginasdeacordo
comaconfigura çãodousuário. Porpadrãoissoseráfeitodeacordocomotama-
nhodasuapágina,masépossíveltomarcontrolesobreissoedefinirregrasespe-
cíficasparainformaremqualpartedoseuconteúdoaquebraseráfeita. Atual-
mente,existem3propriedadesdisponíveisnamaioriadosnavegadoresparaisso:
page-break-before, page-break-insidee page-break-after.
O page-break-beforee page-break-afterdefinemseaquebradepá-
ginadeveocorrerantesoudepoisdoelemento. Apropriedadeaceitaosvalores
always,utilizadoparafor çaraquebra,ou avoid,indicandoparaonavegador
queaquebradeveserevitada. Comelesépossívelinformar,porexemplo,queao
imprimirumarela çãodepostsdeumblog,deveexistirumaquebradepáginaentre
umposteoutro.
article {
page-break-after: always;
}
Oucasovocêprecisedeumcontrolemaisrefinadodasquebras,vocêpodede-
finirumelementovazioparaposicionarasquebrasempontosespecíficosdoseu
conteúdo.
.page-break {
display: none;
}
@media print {
55


## Página 66

4.8. Gererelatóriosinteligentesesimplescomosestilosdeimpressão CasadoCódigo
.page-break {
display: block;
page-break-before: always;
}
}
Eentãoadicionarumatag div,porexemplo,comaclasse .page-breakonde
fornecessárioforçaraquebradepágina.
Jácomo page-break-inside,queaceitaapenasasop ções autoe avoid,
podemosdefinirqueoconteúdodeumparágrafo nãodeveserquebradoentreduas
páginas.
p {
page-break-inside: avoid;
}
Estetipodecontroleéinteressanteparablocosdeconteúdoextensos,comoma-
nuais,documenta çõesoumesmoe-bookscriadosemHTML.Alémdestas3pro-
priedadesexistemoutrasduas,utilizadasparadefiniroslimitesdelinhasquedeve
ficaremumapáginaouemoutra: orphanse widows.Masinfelizmenteelasnão
possuemumsuporteextensopelosnavegadores.
Impressãodetabelas
Vamospraticarumpoucoemelhorarumatabeladeumrelatóriofinanceirocom
débitoselucrosobtidos.Alémdosvalores,atabelapossuialgunslinksparanavegar
entreosdadosetomaroutrasa çõesnosistema. OHTMLébemsimples,tendo
apenasumatabelaealgumaslinhas.
<h1>Transações de Maio, 2011</h1>
<table>
<tr>
<td>
<a href= 'http://exemplo/transacao/1'>Transação 1</a>
</td>
<td class= 'expense'>R$ 100,00</td>
<td class= 'actions'>
<a href= 'http://exemplo/transacao/1/editar'>Editar</a>
</td>
</tr>
<tr>
56


## Página 67

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
<td>
<a href= 'http://exemplo/transacao/2'>Transação 2</a>
</td>
<td class= 'profit'>R$ 200,00</td>
<td class= 'actions'>
<a href= 'http://exemplo/transacao/2/editar'>Editar</a>
</td>
</tr>
</table>
EumpoucodeCSSparamelhoraroestilodatabela,definindosualargura,cores
paraasbordasdascélulas,alinhamentosetambémadefini çãodelinks:
table {
width: 500px;
}
td {
border: 1px dotted #666;
padding: 5px;
}
td a {
color: #3B5998;
}
.expense, .profit, .actions {
text-align: right;
}
.expense, .profit {
font-weight: bold;
}
.expense { color: red; }
.profit { color: green; }
.actions a {
font-size: 0.9em;
color: white;
padding: 2px 5px;
background-color: #3B5998;
57


## Página 68

4.8. Gererelatóriosinteligentesesimplescomosestilosdeimpressão CasadoCódigo
text-decoration: none;
}
Figura4.19:Atabeladorelatóriofinanceiro,emsuaversãopadrão.
Alémdedefinirumalarguraparaatabelaedefiniralgumasregrasdealinha-
mento,registrosdelucroficarãocomacorverdeegastosserãoexibidosemverme-
lho.Aoimprimirestapáginaempretoebranconãopossuímosnenhumadistin ção
visualdissoeoslinksnãoestarãodisponíveisnopapel. Vamosescreveralgumas
regrasdeCSSparaimpressãoeajustaristo.
Primeiro,garantimosquetodooconteúdoestejanacorpreta,equeatabela
ocupeomáximodeespa çopossível.
@media print {
* {
color: #000 !important ;
}
table {
width: 100%;
}
td {
border-color: #000;
}
}
Tambémpodemostrabalharumpouconoslinksexistentesnapágina. Osda
primeiracolunapodemserexpandidosutilizandoatécnicadopseudo-elemento.Já
acolunacomoslinksdeedi çãoédispensávelparaanossavisãodeimpressão,por
serumelementodenavega çãosemnenhumconteúdorelevanteparaestecenário.
Podemosentãoesconderestacolunainteira.
58


## Página 69

CasadoCódigo Capítulo4. OquetododesenvolvedorprecisasabersobreCSS
a::after {
content: "(" attr(href) ")";
margin-left: 2px;
}
.actions {
display: none;
}
Porfim,temosacolunadereceitasedébitosatratar.Indonaondadepseudo-
elementos,podemosadicionarduascaracterísticasàcéluladestacoluna.Umsinal
de-ou+,dependendodocaso,antesdovalor,eostermos ReceitaeDespesa.
Comousodovermelhoedoverderemovidonosestilosdeimpressão,estas
indicaçõesserãoúteisparaidentificarotipodetransa çãodecadalinha.OCSSpara
adicionaresteconteúdoéoseguinte:
.expense::before {
content: "- ";
}
.expense::after {
content: " - Despesa";
}
.profit::before {
content: "+ ";
}
.profit::after {
content: " - Receita";
}
Figura4.20:Aversãodeimpressãofinalizada.
59


## Página 70

4.8. Gererelatóriosinteligentesesimplescomosestilosdeimpressão CasadoCódigo
Assimépossíveladequardiversosaspectosdovisualdasnossaspáginasparao
mododeimpressão,deacordocomasnecessidadesdosseususuárioseosobjeti-
vosdoprojetoquevocêestiverfazendo. Claroqueestetipodetratamentonãoé
necessárioemtodososprojetos,maséumacartavaliosanasuamanga.
60


## Página 71

Capítulo5
OquevocêconseguefazercomCSS
3
Diversasadi çõesdoCSS3sãoextremamenteúteisparasubstituirváriostiposde
imagensqueutilizávamosparaadicionarcoreseformasaoselementosHTML,o
quenãoconseguíamosatingircomapenasCSS.Alémdaredu çãodearquivosparase
trabalhareaausênciadedependênciasexternasqueimpactamnaperformancedos
sites,aflexibilidadedessaspropriedadespermitediversascombina ções,quegeram
diferentesestilosquevocênãoimaginariasertãosimplesdesecriarcomapenas
CSS.
O poder de propriedades como box-shadow e funções como o
linear-gradient é tão grande que é comum encontrar designers e desen-
volvedores-eufa çopartedestegrupo-queaposentaramoseditoresdeimagens
e criam as formas, cores e efeitos das páginas direto no código, conferindo os
resultadosaovivoemseusnavegadores.


## Página 72

5.1. Aregra@font-face CasadoCódigo
5.1 Aregra @font-face
Umadasfuncionalidadesqueadicionamuitaflexibilidadeaodarvidaaosdesigns
dasnossaspáginaséaregra @font-face. Elapermitedefinirnovasfamíliasde
fontesqueasnossaspáginasutilizam,einformaaonavegadoreaosistemaoperaci-
onaldousuárioondeestãolocalizadosoarquivonecessárioparadesenharostra ços
dasuafonte.Adefini çãodeumanovafonteéaseguinte:
@font-face {
font-family: "Lobster";
font-style: normal;
font-weight: 400;
src: local( 'Lobster'), url(/fonts/lobster.woff) format( 'woff');
}
Utilizandoasmesmaspropriedadesusadasparaalterarosestilosdefontede
umelemento,podemosdefinirosdetalhesdanovafonte.Nocasodedefinirfontes
comitálicoounegrito,precisamosinformarosvalorescorretosparaasproprieda-
des font-stylee font-weightdeacordocomouso.Jáapropriedade srcé
responsávelpordefiniralocaliza çãodafonte:afun ção localinformaumpossível
nomeparaafontequeserápesquisadonamáquinadousuário,ouumaURLex-
ternaparaqueafontesejabaixadacomoumrecursoadicional,igualaumaimagem
defundo,porexemplo.
Comafontedefinida,podemosutilizá-lanormalmente:
h1 {
font-family: "Lobster", cursive;
}
Casoanossafonte Lobsternãoestejadisponível,porumproblemaderede
ouafaltadeumarquivocompatível,umafontealternativacomo cursivedeveser
definidaparaseraplicadaaoelemento.Acompatibilidadedeformatosdiferentesé
umpontoirritante: existemdiversosformatosdefontesdiferentesquevocêpode
quererdependendodosnavegadorescomquevocêpretendeatender: .eotpara
algumasversõesdoInternetExplorere .svg, .ttfounovamenteo .eotparao
navegadornativodoAndroid,ouversõesdesatualizadasdoSafari,tantoemdesktops
comonoiOS.Oformatotomadocomopadrão,suportadoportodososnavegadores
modernos,éo woff.
62


## Página 73

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
Figura5.1:Asdiferen çasda‘Lobster’parao‘cursive’,umaalternativaaceitávelcasoa
fontenãoestejadisponível.
5.2 Como utilizar serviços de distribuição de fon -
tes
Existemalgunsservi çosdisponíveisnaInternetquefacilitamousodefontesadi-
cionais,disponibilizandoocódigonecessário,servindoosarquivosdefonteetra-
tandodeassuntosrelacionadosalicen çasdeuso, porexemplo. Osmaisfamo-
sosnestecamposãoo Typekit(https://typekit.com)eo GoogleWebFonts (http:
//www.google.com/webfonts).
Algunssitesalternativosdisponibilizamodownloaddosarquivosnecessários
e um exemplo de uso das fontes em CSS, mas sem servir os arquivos direta-
mentedosseusservidores, deixandoestaresponsabilidadeanósdesenvolvedo-
res,comoo FontSpring(http://www.fontspring.com/)eFontSquirrel(http://www.
fontsquirrel.com/).
Podemosutilizaroservi çodefontesdoGoogle,oGoogleWebFonts,parapra-
ticarumpouco.ComececomoseguinteHTML.
<h1>HTML & CSS</h1>
Agora, vamoscarregarafonte Press Start 2P(http://www.google.com/
webfonts/specimen/Press+Start+2P),paraadicionarumvisualnostálgicode8bits
aotítulo.AdicioneaseguintelinhadeHTMLao headdasuapágina.
<link href= 'http://fonts.googleapis.com/css?family=Press+Start+2P'
rel='stylesheet'>
Sevocêacessaroendere çodestafolhadeestilo, http://fonts.googleapis.com/css?
family=Press+Start+2P,veráqueelanãofaznadaalémdedefinirafonte Press
Start 2P,referenciandoumarquivo .woffpresentenosservidoresdoGoogle.
Podemosentãoutilizarestafonteno h1quecriamos.
63


## Página 74

5.3. Substituiçãodeíconesporfontes CasadoCódigo
h1 {
font-family: 'Press Start 2P ', cursive;
}
Figura5.2:Afonte‘PressStart2P’emuso.
5.3 Substituição de ícones por fontes
Outrousobastanteinteressanteparafontesésubstitui çãodepacotesdeícones.No
lugardeumapilhadeimagens,vocêpodeutilizarumafontecompostadeícones,e
nãocaracteresnormais.Comissovocêganhaopoderdecontrolarotamanhoecor
doseusíconessemprecisareditarimagenseexportarnovosarquivosparadentrode
seusprojetos.
Existemdiversasfonteseferramentasexistentesparaajudaracomporgruposde
íconeseadicioná-losàssuaspáginassemmuitotrabalho.Algumasdascole çõesde
íconesmaisinteressantesporai: Pictos(http://pictos.cc/),FontAwesome(http://
fortawesome.github.com/Font-Awesome/)eIconic(http://somerandomdude.com/
work/iconic/). Eparacomporoupesquisaroutrasop ções,existemop çõescomo
Fontello (http://fontello.com/) , IcoMoon (http://keyamoon.com/icomoon/) e o
Shifticons(https://www.shifticons.com/).
PegueafonteIconic,porexemplo,paratestarumpouco. Vocêpodebaixaro
pacotediretodositedoseucriador,P.J.Onori,emhttp://somerandomdude.com/
work/iconic/,oupegaraúltimaversãodafontenoseurepositórionoGitHub-https:
//github.com/somerandomdude/Iconic.
EmvezdeutilizaroCSSqueoprojetojádisponibilizaparavocê,vamosescrever
umexemplodozeroparaverousodafonte.Come çandocomadefini çãodafonte
noCSS.
@font-face {
font-family: 'IconicFill';
src: url( 'iconic_fill.woff') format( 'woff');
font-weight: normal;
font-style: normal;
}
64


## Página 75

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
Então,adicionamosumelementoeumaclasseparadefinirqualíconeseráexi-
bidojuntodonossotítulo.Umaótimaformadeexibirtaisíconesdefonteséutili-
zandoapropriedade contentdospseudo-elementos:
<h1 class= 'icon-next'>Avançar</h1>
.icon-next::after {
content: '\2192';
font-family: 'IconicFill';
margin-left: 10px;
}
Figura5.3:Oíconecriadoutilizandoafonte‘Iconic’.
Utilizandoumpseudo-elementoeumsímboloUnicode,oíconedeumaflecha
paraadireitaéexibidoaoladodotítulo.Qualquermudan çadosestilosdotextodo
elementooudoseupseudo-elementoiráafetaroícone,adequandocoresetama-
nhos.Podemostrocaracordetodososíconesassociadosaum h1eatéutilizaro
íconeemoutroelemento,comoum p,adicionandooseguintecódigo:
<p class= 'icon-next'>Ir para a próxima página</p>
h1.icon-next {
color: blue;
}
Figura5.4:Osíconesrefletemoestilodoelementoqueoscontém.
65


## Página 76

5.3. Substituiçãodeíconesporfontes CasadoCódigo
Destaformaconseguimosposicionareestilizartodososíconesdisponíveisno
IconicfacilmentecomCSS.Outroexemplosãoosclássicosíconesparaa çõesfeitas
comsucessoouerrosdevalida çõesdeformulários.
.icon-ok {
color: #489D00;
}
.icon-ok:before {
content: "\2714";
font-family: 'IconicFill';
margin-right: 10px;
}
.icon-invalid {
color: #990000;
}
.icon-invalid:before {
content: "\2718";
font-family: 'IconicFill';
margin-right: 10px;
}
<p class= 'icon-ok'>E-mail enviado com sucesso!</p>
<p class= 'icon-invalid'>Atenção, preencha todos os campos do
formulário
</p>
Figura5.5:Combinandoíconesecoresparacriarmensagens.
EnquantooIconicutilizasímbolosUnicodecomocaracteresparaosseusíco-
nes,outrasfontespodemutilizaroutroscaracteresparaisto.Énecessárioconferira
documentação-casoexistauma-arespeitodecadafonteantesdeutilizá-la.
66


## Página 77

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
5.4 Explore nov as possibilidades com bordas
TodoelementoHTMLécomparadoaumacaixa,masnemtodososelementosdas
nossasinterfacesprecisamserquadrados. Emvezdeseutilizarimagensatortoe
direito,podemosutilizaro border-radiusparaarredondaroscantosdosseus
elementos.Apropriedadeaceitaaté4valores,seguindoomodelodeoutroscomo
margine padding,sendoqueaúnicadiferen çaéqueoprimeirovaloréreferente
aocantosuperioresquerdodoelemento,seguindoemdiantenosentidohorário.
Enquantoalgunscantosarredondadospodemparecerapenasumpequenodetalhe
estético,o border-radiusconseguecriarmaisdoqueisso.Vejaaseguir.
<h3 class= 'tnt'>TNT</h3>
.tnt {
border-radius: 50%;
border: 5px solid #000;
height: 50px;
line-height: 50px;
text-align: center;
width: 50px;
}
Figura5.6:Utilizandoborder-radiusparacriarcírculos
Podemosutilizarporcentagensecriarcírculosouelipses,independentedota-
manhorealdoelemento.Foraisto,cadacantodoelementopodereceberdoisvalores
paradefinirexatamentequalseráoraioutilizadoparacriaroefeito.
<span class= 'counter'>37</span>
.counter {
background-color: #000;
border-top-left-radius: 25px 10px;
border-top-right-radius: 25px 10px;
color: white;
display: block;
67


## Página 78

5.4. Explorenovaspossibilidadescombordas CasadoCódigo
font-size: 1.7em;
height: 50px;
line-height: 50px;
text-align: center;
width: 50px;
}
Figura5.7:Umexemplodeusomaisrefinadodoborder-radius.
Esseéumcasodeusomaisrarodeseencontrar,vistoqueamaioriadasapli-
caçõesde border-radiussãoperfeitamentecirculares,egeralmentefeitaspara
realçardetalhesdecertoselementos,comobotões,caixasdetextooucaixasdemen-
sagens.
Criandonuvens
Não,nãovamosfalarsobre Cloud Computingnestelivro.Masvamosdesenhar
umíconedeumanuvemutilizandopseudo-elementoseo border-radius,para
demonstrarcomoépossívelcriaríconeseoutrasformasquegeralmenteseutiliza
comoimagensnoseucódigo. NossoHTMLserábastantesimples,semnenhum
conteúdo.
<div>
<span class= 'cloud'></span>
</div>
Primeiro,como spandesenhamosabasedanuvem,ea divservirácomoum
fundodonossoícone.
div {
background-color: #000;
width: 50px;
height: 10px;
padding: 20px 50px;
}
68


## Página 79

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
.cloud {
background-color: #FFF;
border-radius: 48px;
display: inline-block;
height: 16px;
position: relative;
width: 48px;
}
Figura5.8:Abasedanuvem,criadacomborder-radius.
Opontochavedessesvaloreséo border-radiusde 48px,queé3vezeso
valordaalturadele- 16px. Casofossenecessárioumanuvemmaior,sóiríamos
manterestapropor çãodevaloresaodefinirnovostamanhos. Vamosaopróximo
pedaço:
.cloud::before {
background-color: red;
border-radius: 50%;
content: '';
height: 14px;
position: absolute;
right: 7px;
top: -6px;
width: 14px;
}
Figura5.9:Opseudoelementoposicionadoacimadabase.
Utilizandoo ::before,desenhamosumaesferade 14pxposicionadadecerta
formaadeixarmetadedoelementoparaforadabase. Ofundovermelhoservirá
69


## Página 80

5.4. Explorenovaspossibilidadescombordas CasadoCódigo
apenasparaajudaradistinguircadaumdos3elementosentresi.Precisamosagora
deoutrocírculo,umpoucomaior,posicionadoaoladodireitodo span.Podemos
reaproveitarasdefiniçõesdeposi çãoetamanhodo ::beforeesobrescreverapenas
algunsvaloresparacriaroutroelementomaior.
.cloud::before, .cloud::after {
background-color: red;
border-radius: 50%;
content: '';
height: 14px;
position: absolute;
right: 7px;
top: -6px;
width: 14px;
}
.cloud::after {
background-color: blue;
height: 23px;
left: 7px;
right: auto;
top: -10px;
width: 23px;
}
Figura5.10:Maisumapartedanuvem,posicionadanooutroladodabase.
O ::after,utilizandodamesmatécnicaparasedesenharcírculos,ocupao
ladodireitodanuvem. Agorabastaalterarospseudo-elementosparaqueambos
fiquemcomamesmacordefundodo span- #FFF-everoresultadofinaldo
experimento.
70


## Página 81

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
Figura5.11:Trocandoosfundosparabrancoconseguimosveraformacompletada
nuvem.
Umcasoclássicodeusopara border-radiusénacriaçãodeestilosparacom-
ponentesdeformulários: decaixasdetextoabotões. Estaaplica çãomereceuma
aprofundamentomaior,quevocêencontranase ção7.9destelivro.
5.5 Manipulação de cores com rgba e gradientes
Alémdefontesebordas,outroartifíciovisualganhoumuitocomachegadadoCSS
3-ascores. Antigamenteeramlimitadasaapenastextosefundos,oquesempre
resultavanamesmasitua çãodasbordasarredondadas-usodeimagensparacriar
gradienteseopacidades,oqueimpactavanaperformanceenaflexibilidadedema-
nutençãodoseucódigo.Fun çõesmuitoúteissurgiramparasuprirdiversoscasosde
usodeimagens,comoo rgbaeo linear-gradient.
Primeiro,ao rgba. Afunçãopermitedefiniraopacidadedeumacor,permi-
tindocriarefeitosdetransparênciasutilizandoapenasacordefundoouasbordas
deumelemento.Umpontocrucialéqueafun çãonãorecebeumvalorhexadecimal,
como #000000,esimutilizandoos3decimaisquerepresentamacor,nocasodo
pretosão 0,0,0.Oquartoargumentodafun çãoéaopacidadedesejada,de 0.0a
1.0.
Vamosàação.ComoHTMLaseguir,nóstemosumafotoeumalegenda,utili-
zandonovastagscomoo figureeo figcaptionparaagruparo imgcomasua
legenda.
<figure>
<img src="/images/sf.jpg" alt="A Golden Gate.">
<figcaption>
San Francisco, Califórnia
<small>
Por Salim Virji (http://www.flickr.com/photos/salim/402618628/)
</small>
</figcaption>
</figure>
71


## Página 82

5.5. Manipulaçãodecorescomrgbaegradientes CasadoCódigo
NossoprimeiropassocomoCSSseráposicionaramensagemporcimadafoto,
algunspixelsdedistânciadofinaldela.
figure {
position: relative;
}
img {
display: block;
}
figcaption {
bottom: 5px;
margin: 0 5px;
padding: 5px;
position: absolute;
width: 300px;
}
Figura5.12:Posicionamosalegendasobreafoto,masnãoéfácilleroqueestáescrito.
Destaformanãotemoscontrastenenhumparalerotextodalegenda.Horade
aplicarumfundopretoetrocarafontedalegendaparabranco,melhorandosua
leitura.Vamosaproveitartambémedeixarofundoumpoucotransparente,fazendo
umefeitoelegante.
72


## Página 83

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
figcaption {
background-color: #000;
background-color: rgba(0,0,0,0.5);
color: #FFF;
}
Figura5.13:Nãoficoumelhorparaleralegendadafoto?
Como 0.5deopacidadedofundopretoconseguimosleralegendanormal-
menteeaomesmotempoidentificaraspartesdafotoqueficaramportrásdela.
Casoonavegadorutilizadonãotenhasuportea rgba,seráusadoadefini çãodeum
fundopretosólido,utilizandoaclássicadefini çãodacoremhexadecimal.
Combinetransparênciaebordas
Umaoutraaplica çãointeressanteparao rgbaépodercombinartonsdepretoe
brancoparaescurecerouclarearoutrascores,comocriandodivisóriasentrese ções
ouelementosdeummenu.Apraticidadedestaabordageménãosepreocuparcom
acordefundoportrásdabordaoufundocomtransparência,permitindoutilizaro
mesmoCSSemcontextoselugaresdiferentes.Umaformamelhordeentenderisto
écolocandoamãonamassa.
Vamosmontarumalista,ealinhartodosositenshorizontalmente.
<ul>
<li>Um</li>
73


## Página 84

5.5. Manipulaçãodecorescomrgbaegradientes CasadoCódigo
<li>Dois</li>
<li>Três</li>
<li>Quatro</li>
</ul>
Cadaitemdalistaocupará 50px,comoseutextocentralizado:
ul {
height: 35px;
list-style:none;
padding: 0;
width: 210px;
}
li {
float: left;
line-height: 35px;
font-size: 0.9em;
width: 50px;
text-align: center;
}
Figura5.14:Ositensdomenudevidamenteposicionados.
Simples,certo? Horadeadicionarcores. Iremosmudaracordotextopara
brancoeaplicarumfundocinzanalista.
ul {
background-color: #CCC;
color: white;
}
Figura5.15:Omenucomumfundocinza.
74


## Página 85

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
Agoraquealistapossuiumacorsólidadefundo,podemosaplicarasbordas
comtransparência.Iremosaplicarumabordapretacomapenas30%deopacidade
nalista,eumasequênciadebordasbrancasepretasentreoselementos.
ul {
border: 1px solid rgba(0,0,0,0.3);
}
li {
border-left: 1px solid rgba(255,255,255, 0.3);
border-right: 1px solid rgba(0,0,0, 0.3);
}
li:first-child {
border-left: none;
}
li:last-child {
border-right: none;
}
Figura5.16:Asbordascomopacidadenositensdomenu.
Osseletoresde :first-childe :last-childsãoutilizadospararemover
abordaesquerdadoprimeiroitemdalistaeabordadireitadoúltimoelemento,
evitandoqueelasentrememcontatocomabordado ul. Épossívelnotarquea
bordapretapodeserconsideradacomoumaversãomaisescuradofundocinza,
enquantoabordabrancasetornaumcinzamaisclaro,deformabastantesutil.Seas
bordasfossemsólidas,utilizando #000000e #FFFFFF,oresultadoseriabastante
diferenteenadainteressante.
Figura5.17:Asbordascomcoressólidas-nãoéamesmacoisa.
75


## Página 86

5.5. Manipulaçãodecorescomrgbaegradientes CasadoCódigo
Vocêpodeagoraalteraracordefundodalista,utilizandodesdecoresprimárias
comoazulouvermelhooutonsespecíficosdeverdeoularanja.Oefeitoquevimos
nofundocinzaéreplicávelemdiversosoutroscenáriosefundos.Fa çaalgunstestes
vocêmesmoeconfira!
Figura5.18:Variaçõesdomenutrocandoapenasacordefundo.
Utilizandoolinear-gradient
TalvezumadaspartesdoCSS3quefoimaisesperadapordiversosdesenvolve-
dores,o linear-gradientéumafunçãocapazdecriarimagenscomgradientes
apartirdeumalistadecoreseposi ções.Extremamenteútilparasubstituirimagens
defundo,osgradientescriadosviaCSSconseguemseadequaraotamanhodosseus
elementosepodemsercompostosdediversascoresemdiversasposi ções,oquefa-
cilitatraduzirumgradientecriadoemumeditor,comooAdobePhotoshop,parao
seucódigoCSS.
Asintaxedafun çãoébastantedireta.Primeiroinforma-seadire çãoemqueo
gradienteseráprojetado,aceitandopalavraschavecomo topou left(paragra-
dientesnaverticalouhorizontal)oucombina çõesdesentidosverticalehorizontal,
como top right,paracriargradientesnadiagonal. Casovocêprecisedemais
controlesobreadire çãodosseusgradientes,vocêpodeinformarumvaloremgraus
(deg)também.
Alémdadireção,énecessárioinformarpelomenosduascores,ouoschamados
color-stops,umpardecoreposi ção(em pxouporcentagem),indicandoem
qualposiçãoacordeveráterminaroucome çar. Todaatransiçãodeumacorpara
outraficaacargodonavegador.
Apesardaflexibilidadedafun ção,vocênãoprecisautilizarmuitasop çõesou
coresparachegaragradientestradicionais,comoosutilizadosembotõesoubarras
76


## Página 87

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
deaçõesoutítulos.
div {
font-weight: bold;
height: 50px;
line-height: 25px;
margin-bottom: 10px;
padding: 5px;
text-align: center;
width: 220px;
}
.blue {
background-image: linear-gradient(top, #4377FA, #0537B7);
}
.reverse-blue {
background-image: linear-gradient(top, #0537B7, #4377FA);
}
.omg-pink {
background-image: linear-gradient(top right, #FC0050, #FF79A3);
}
.stops {
background-image: linear-gradient(top, #F5B951 48%, #F2A31C 56%);
}
<div class= 'blue'>
Um gradiente azul clássico, utilizando 2 tons similares.
</div>
<div class= 'reverse-blue'>
Uma versão inversa do gradiente azul.
</div>
<div class= 'omg-pink'>
Combinando "top" e "right" para a direção.
</div>
<div class= 'stops'>
Utilizando posições específicas para as cores.
77


## Página 88

5.5. Manipulaçãodecorescomrgbaegradientes CasadoCódigo
</div>
Figura5.19:Osexemplosde‘linear-gradient’.
Ocasoclássicodafun çãosãoosgradientesverticais(geralmenteutilizando top
comodireção),partindodeumtommaisclarodeumacorparaumtommaisescuro.
Umaregrasimplesparanãosedarmalcomgradientesémanterostonsdecores
bastantesimilares,criandoumaleveilusãodeumasuperfíciearredondadaesob
oefeitodealgumafontedeluz. Paraisto,tenhaemmãosalgumaferramentade
manipulaçãodecoresparamontarascombina çõesnecessárias.Comonoexemplo
anterior,oprimeirogradienteécompostodeumtomespecíficodeazuledeuma
versãomaisescuradelemesmo.
Umaalternativaparagarantirqueoselementoscomgradientenãofiquemsem
fundoalgumemnavegadoresquenãopossuamsuporteafun çãoéfixaracorde
fundodoelementoparaacorpredominante,destaformaoelementoteráumfundo
sólidocasoogradientenãosejaexibido.
.blue {
background-color: #4377FA; /* A cor superior do gradiente como fundo */
background-image: linear-gradient(top, #4377FA, #0537B7);
}
78


## Página 89

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
Figura5.20:Adiferen çadogradienteedacordefundo. (exibidaemnavegadores
semsuporte)
Outrasolu çãoseriadefinirum background-imageantesdadeclara çãodo
gradiente,contendoocaminhoparaumaimagemaserutilizadacasoafun çãonão
sejaexecutada.
Apesardavantagemdequeaimagemsóseráacessadapelonavegadorneste
cenáriodefalha,oesforçoemmanterasimagensjuntodosgradientesnãomeparece
umaboaideia,aindamaiscomoaumentodeusodenavegadoresquesuportamtais
gradientes,estasimagenssetornarãoobsoletaslogo.
5.6 Trabalhe com sombras e crie menus elegantes
Apropriedade box-shadowpermiteadicionarmúltiplassombrasaelementosdas
suaspáginas.ExistemdoistiposdesombrasquepodemostrabalharcomCSS:som-
brasexternaseinternas. Sombrasexternas,quesãoocomportamentopadrãodo
box-shadow,sãoexibidasatrásdoelemento,similaraoefeitoqueéchamadode
drop shadowemeditoresdeimagens. Assombrasinternas,quesãoexibidasden-
trodasbordasdoselementoseacimadoseufundo,secomparaaosefeitosde inner
shadow.
Parasecriarumasombravocêprecisa,primeiro,dascoordenadasemqueasom-
braficaráposicionada.Emseguidavocêpodedefinirdoisvaloresopcionais:aden-
sidadedasombra(geralmentechamadode blur),eumtamanhoadicionalparacon-
trairouexpandiroefeitodasombra. Apesardeopcional,sombrassemoseu blur
nãopassamdemaisumabordaaoredordoelemento,entãoelesempreestápresente
nassuassombras.Apóstodososvaloresnuméricosvocêdeveinformarumacor-
quepodeserumvalorhexadecimalouumachamadadafun ção rgba.
79


## Página 90

5.6. Trabalhecomsombrasecriemenuselegantes CasadoCódigo
Osefeitosdesombrasãoúteisparareal çarasobreposi çãodeumelementosobre
outro,oquecaicomoumaluvanacaixadeajudaquecriamosnocapítulo4.5.Basta
adicionarousodo box-shadownaclasse .help.
.help {
box-shadow: 3px 3px 3px #AAA;
}
Figura5.21:Aaplica çãodo‘box-shadow’namensagemdeajuda.
Valorespositivosmovemasombraparabaixoouparaoladoesquerdodoele-
mento,enquantovaloresnegativostomamocaminhocontrário.Oângulodasombra
écrucialparacriaroapelovisualquevocêquer,eumusoincorretodosvalorespode
trazervisuaismenosinteressantes.
.help {
box-shadow: -3px -3px 3px #AAA;
}
Figura5.22:Asombrainvertidanãocombinacomoelementocomoaanterior.
Sombrasinternaspodemserutilizadasparacriarumefeitodeprofundidade
dentrodeumelemento. Comistovocêpodecriarailusãodealgo“pressionado”,
comoumbotãodeumformulárioouoitemdemenuqueestáselecionado,oureal-
çaraindica çãoqueumelementoéumcampodetexto,porexemplo.
80


## Página 91

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
Faça a sua pesquisa aqui: <input type="text">
input {
border: 1px solid #999;
box-shadow: 2px 2px 2px rgba(0,0,0, 0.25) inset;
padding: 2px 5px;
}
Figura5.23:Asombrainternadacaixadetexto.
Oefeitoébastantesutil,maséumaop çãoeleganteparaosestilosdosseusfor-
mulários.
Outracombinaçãointeressantedecamposdeformuláriose box-shadowécriar
umasombraposicionadacom 0 0,criandoumbrilhoaoseuredor,quandoousuá-
rioestivercomocursordentrodocampodetexto.Alteraracordabordadocampo
paraamesmadasombraajudaaconsolidaresteefeito.
input:focus {
border-color: #35861B;
box-shadow: 0 0 5px #35861B;
outline: none;
}
Figura5.24:Obrilhodacaixadetexto,masasombrainternanãoestápresente.
Masassim,asombraquecriamosanteriormenteparaocampodeixadeserexi-
bida,jáquesobrescrevemosapropriedade.Asolu çãoérepetirasombraexistente,
separando-asporvírgula. Assimépossívelmanteraconsistênciadosestadosdo
elemento.
81


## Página 92

5.6. Trabalhecomsombrasecriemenuselegantes CasadoCódigo
input:focus {
border-color: #35861B;
box-shadow: 0 0 5px #35861B, 2px 2px 2px rgba(0,0,0,0.25) inset;
outline: none;
}
Figura5.25:Asduassombrasdacaixadetextoaoreceberfoco.
Seutilizandoaposi ção 0 0criamosumefeitodebrilhoemsombrasexternas,
fazendoomesmocomsombrasinternasépossívelalcan çarumefeitodeprofundi-
dademaispesado,comoseasuperfíciedasuapáginanãofosseplana.Vamoscriar
ummenudenavega çãoparafazeresteteste.Come çandocomoHTMLdeumalista
simples.
<ul class= 'nav'>
<li><a href="#">Home</a></li>
<li><a href="#">Contato</a></li>
<li><a href="#">Sobre</a></li>
</ul>
Alinhamososelementoshorizontalmenteutilizando float,edefinimosum
tamanhopadrãoparacadalinkdomenueumacordefundo.
.nav {
background-color: #B9522D;
height: 30px;
list-style:none;
padding: 0;
width: 210px;
}
.nav li {
float: left;
font-weight: bold;
height: 30px;
line-height: 30px;
82


## Página 93

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
text-align: center;
width: 70px;
}
.nav a {
color: white;
}
Figura5.26:Omenuhorizontalquecriamos.
Digamosquevocêestánapáginaprincipal,eomenudeveterumaindica ção
visualdequeolink Homeéodapáginaatual.Alémdemudan çasnoestilodotexto
enofundodoelemento,umasombrainternapodeserutilizadaparacriarestaim-
pressão.Primeiro,precisamosdeumaclasseparaindicarqualdoslinkséoatual:
<ul class= 'nav'>
<li class= 'current'><a href="#">Home</a></li>
<li><a href="#">Contato</a></li>
<li><a href="#">Sobre</a></li>
</ul>
Agora,utilizamosamesmatécnicadobrilhoaoredordacaixadetexto,sóque
utilizandoo inset.
.nav .current {
background-color: #A64A28;
box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
}
Figura5.27:Olink‘Home’nãoaparentaestarpressionado?
83


## Página 94

5.6. Trabalhecomsombrasecriemenuselegantes CasadoCódigo
Alémdamudançaparaumfundomaisescuro,asombracontribuiparadiferen-
ciarolink Homedosdemais.
Cuidado com sombras pesadas
Acombinaçãode box-shadowe rgbapodetrazerresultadosinte-
ressantesparaassuasinterfaces,mascuidadoaoabusardeopacidadee
blurjuntos.RossAllen,daequipedoAirbnb,percebeuqueaonavegar
pelositedaempresautilizandoumChromebook,umnotebookcriado
peloGooglequeeradisponívelparaclientesdaVirginAmericadurante
osseusvoos,arolagemdapáginaeradrasticamentemaisdevagardoque
emseucomputadorpessoal.Utilizandoferramentasdedesenvolvimento
paraidentificaroqueestariacausandoestalentidão,elechegouàconclu-
sãoqueousodo box-shadowcom 10pxde bluremalgumaspartes
dositeerarelativamentepesadoparaonavegadorexibirereconstruir
conformearolagemerafeita,eistoeraperceptívelemumcomputador
depoderdeprocessamentoinferior,comooChromebook.
Reduzindoadensidadeecontandocomaposi çãodassombras,enão
oseutamanho,paracriarosefeitosdesejados,oproblemadeperfor-
mancefoiresolvidoeaexperiênciadeusodoAirbnbemoutrosdisposi-
tivosfoimelhoradacomapenasmudan çasnousode box-shadow.[1]
Trabalhandocomsombrasemtextos
Nãotãopoderosaquantoo box-shadow,apropriedade text-shadowper-
miteaplicarsombrasaotextodasuapágina,enãoaoselementos. Ousodaspro-
priedadesébastantesimilar:vocêpodeposicionarasombraàvontadeecombinar
diversosefeitoscomdiversassombras,maso text-shadownãopossuiaquarta
opçãodetamanhodo box-shadoweotermo insetnãoésuportado.Então,se
vocêjásedeubemcomumadestaspropriedades,utilizaraoutraserácomoum
passeiodebicicleta.
<h1>HTML & CSS</h1>
h1 {
background-color:#1D9AC0;
84


## Página 95

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
color: #FFF;
padding: 10px;
text-shadow: 2px 4px 2px rgba(0,0,0,0.3);
}
Figura5.28:Umexemplosimplesde‘text-shadow’.
Ousodo text-shadowpodeseguiramesmalinhado box-shadow:realçar
sobreposiçõeseadicionarefeitossutisparamelhoraraleituradecertostextosem
fundosdiferentes.
Imagineumalojavirtual,ondecadacomprafeitapodeestaremumdetrêsesta-
dos: Pagamento recusado, Produto enviadoou Em aprovação.Naexibi çãodosdados
deumacompra,podemosexibiroseuestadocomumacordefundorelacionadaa
ele,utilizandooseguintecódigo
<span class= 'status failed '>Pagamento recusado</span>
<span class= 'status shipped '>Produto enviado</span>
<span class= 'status processing '>Em aprovação</span>
.status {
display: inline-block;
font-weight: bold;
padding: 7px 10px;
}
.failed {
background-color: #BD2C00;
}
.shipped {
background-color: #6CC644;
}
.processing {
85


## Página 96

5.7. Combinandotudo CasadoCódigo
background-color: #FC9800;
}
Figura5.29:Asindica çõesdeestado-nãoachaqueestetextopretoestáruim?
Paradarmaisaten çãoaotexto(enãoaofundo),podemostrocaracordotexto
parabrancoecombinarcomumasombra,trazendoaten çãoepreservandoaleitura
dostextosaomesmotempo.Paraestecasoasombracom rgbaéumaótimapedida.
.status {
color: white;
display: inline-block;
font-weight: bold;
padding: 7px 10px;
text-shadow: 0 1px 2px rgba(0, 0, 0, 0.7);
}
Figura5.30:Ostextosdeestadoutilizando‘text-shadow’.
5.7 Combinando tudo
Passamospordiversaspropriedadesmuitointeressantes,queutilizadassozinhasjá
produzemresultadosvisuaissensacionais.Masaoutilizaralgumas(outodas)você
conseguecomporse çõesecomponentesvisualmenteelegantes,ecombinandoalgu-
masdastécnicasapresentadasnestecapítulojuntodenovosusosdaspropriedades
doCSS3conseguimoschegaraoseguinteresultado:umase çãoparaexibirolivro
Ruby on Rails: coloque sua aplicação web nos trilhos,disponibilizandoopçõesdecom-
praeasitua çãodolivroemestoque. Esteseráumótimoexercícioparacombinar
algumasdascoisasqueaprendemos.
86


## Página 97

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
Figura5.31:Oresultadofinaldase çãoqueiremoscriar.
VamoscomeçarcompartedoHTML,juntodonomedolivroedoautor.OCSS
paraestestextoserábemsimples,similaraoquejávimosanteriormente.
<article class="book">
<header>
<h1>Ruby on Rails: coloque sua aplicação web nos trilhos</h1>
<h2>Vinicius Baggio</h2>
</header>
</article>
h1 {
color: #BD2C00;
font-size: 1.2em;
margin: 0;
}
h2 {
font-size: 1em;
margin: 5px 0;
}
Figura5.32:Osestilosparaotítuloeoautordolivro.
87


## Página 98

5.7. Combinandotudo CasadoCódigo
Em seguida, o estado deDisponível pode ser baseado nos exercícios de
text-shadowquefizemos,comaadi çãodeum border-radiusparaarredondar
oscantosdoelemento.Aplicamosumfundoverde,acorbrancaeumalevesombra
notexto,juntodealgunsajustesdeespa çamentosetamanhos.
<article class="book">
<header>
<h1>Ruby on Rails: coloque sua aplicação web nos trilhos</h1>
<h2>Vinicius Baggio</h2>
<span class= 'available'>Disponível</span>
</header>
</article>
.available {
background-color: #6CC644;
border-radius: 3px;
color: white;
font-size: 0.8em;
font-weight: bold;
padding: 3px 7px;
text-shadow: 0 1px 2px rgba(0, 0, 0, 0.7);
}
Figura5.33:Aindica çãodadisponibilidadedolivro.
Depois,criaremosomenudecompras,quecombinadiversostruques.OHTML
utilizadoseráumasimpleslistanãoordenada:
<ul>
<li><a href="#" class= 'icon paper '>Comprar a versão física</a></li>
<li><a href="#" class= 'icon digital '>Comprar a versão digital</a></li>
<li>
<a href="#" class= 'icon package '>Comprar o pacote completo!</a>
88


## Página 99

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
</li>
</ul>
Aplicamosum linear-gradientazulparaofundodomenu,juntodeajustes
aespaçamentoeposi ção:
ul {
background-color: #56B4EF;
background-image: linear-gradient(top, #56B4EF,#148EDA);
float: left;
list-style: none;
margin: 10px 10px 0 0;
padding: 0;
width: 230px;
}
Eparaosícones,iremosreaproveitarafonte Iconiceutilizaralgunsdeseusíco-
nesnomenu.
@font-face {
font-family: 'IconicFill';
src: url( 'iconic_fill.woff') format( 'woff');
font-weight: normal;
font-style: normal;
}
.icon::before {
font-family: 'IconicFill';
margin: 0px 5px;
}
.paper::before {
content: "\e00b";
}
.digital::before {
content: "\e044";
}
.package::before {
content: "\e022";
}
89


## Página 100

5.7. Combinandotudo CasadoCódigo
Figura5.34:O‘linear-gradient’eosíconesdomenu.
Paraapresentaroslinksdeumaformamaisinteressante,precisamosmudara
suacoreespa çarmelhorostextosdos3itens-outrolugarondeo text-shadow
caicomoumaluva.
.icon {
color: #FFF;
display: block;
font-size: 0.9em;
font-weight: bold;
padding: 5px;
text-decoration: none;
text-shadow: 0 1px 0 rgba(0, 0, 0, 0.9);
}
Opróximopassoécriarasbordasentreoslinks,aplicando rgbapretoebranco.
Importanteremoverabordasuperiordoprimeirolinkeainferiordoúltimo,apro-
veitandoasclassesutilizadasparaexibirosícones.
.icon {
border-bottom: 1px solid rgba(0,0,0, 0.3);
border-top: 1px solid rgba(255, 255, 255, 0.3);
}
.icon.paper {
border-top: none;
}
.icon.package {
border-bottom: none;
}
90


## Página 101

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
Figura5.35:Umaversãomelhoradadomenuutilizando‘text-shadow’ebordascom
‘rgba’.
Podemosutilizaramesmacorem rgbausadano border-topdoslinkspara
contornaromenuinteiro,alémdeadicionarum border-radiusaoseuestilo.
ul {
border-radius: 5px;
border: 1px solid rgba(0,0,0, 0.3);
}
Oúltimodetalhedomenu-umaindica çãode :hoverparaoslinks.Podemos
aplicarumfundopretocomtransparêncianolink,queiráaplicarumefeitodeque
ofundoazulsetornamaisescuro.
.icon:hover {
background-color: rgba(0, 0, 0, 0.1);
}
Figura5.36:Aversãofinaldomenucombordasarredondadas.
E o nosso menu está pronto, combinando bons usos de rgba,
linear-gradient, text-shadowe border-radius.
Adescri çãodolivroseráapenasumparágrafo,semestilopróprioalgum,que
deveráirlogoapósoHTMLdomenu,quedevidoàsuadefini çãode float,irá
alinharos2elementoshorizontalmente.
91


## Página 102

5.7. Combinandotudo CasadoCódigo
<p>
Uma ótima leitura para iniciantes afins de se aventurar no ecossistema
de Ruby.
</p>
Otoquefinalseráoacabamentodase çãointeira,identificadapelaclasse book.
Vamosseguirumestilosimilaraodomenu-bordasarredondadas,fundocomgra-
dienteeumabordaumpoucomaisescuraqueofundo,alémdefixaralargurada
seçãoeespa çarumpoucooseuconteúdo.
.book {
background-color: #FAFAFA;
background-image: linear-gradient(#FAFAFA,#EEE);
border-radius: 5px;
border: 1px solid #CCC;
padding: 10px;
width: 600px;
}
Comoonossomenuestáutilizando float,precisamoscorrigiraalturadase ção
paraquetodooselementosfiquemdevidamentecontidosno article.Podemos
repetirousodeumelementovaziocomaclasse clearaofinaldoconteúdo.
<div class= 'clear'></div>
.clear {
clear: both;
}
Figura5.37:Aversãofinaldase çãosobreolivro.
92


## Página 103

CasadoCódigo Capítulo5. OquevocêconseguefazercomCSS3
Estessãoalgunsdosexemplosdoqueépossívelcriarjuntandogradientes,som-
brasesimilares.Combina çõessemelhantespodemserúteisparacriarbotões,cabe-
çalhoserodapés,barraslateraisediversosoutroscomponentesdeinterfacedeque
vocêprecisenosseusprojetos.
93


## Página 105

Capítulo6
Tomandocontroledaestrutura
visual
Umadasmaiorescomplica çõesemprojetosgrandesecomplexoséestruturareposi-
cionarcorretamentetodososelementosexistentesemumapágina.Encaixarmenus,
barraslaterais,imagensetextosnosseusdevidoslugarespoderesultaremumHTML
complexoeumCSSmuitoextensosenãoforfeitocorretamente.Éimportantecom-
preenderanecessidadedecadagrupodeelementoseocontextodoelemento pai
queosenvolvem. Existemsolu çõessimilaresparacertoscasos,masoimpactode
cadaopçãodeveserlevadoemconsidera ção.
Temos3propriedadesbastanteimportantesparasecontrolarofluxoeaposi ção
dosseuselementos: display, positione float.Utilizamo-lasemoutrosca-
pítulos,masnãochegamosnosdetalhesdeseusmotivosedoqueelasestãofazendo
comosnossoselementos.Horadeolharcadaumadelaseentendermelhoroseus
papéisnaestruturaçãodosseuselementos.


## Página 106

6.1. Apropriedade‘display’ CasadoCódigo
6.1 A propriedade‘display’
Apropriedade displaydeterminacomoumelementoseráexibidopelonavega-
dor. Elementosdetexto,como a, spane small,possuemumvalor inline,
quepermitequeelementosseguintessemantenhamnamesmalinhaqueoatual,
enãosãoafetadosporpropriedadescomo heighte width. Containerscomo
div, p, sectionesimilaressãotratadoscomoblocos-comovalorpadrão
de block-quebrandoofluxodoselementosemumanovalinhaeocupando
alarguramáximaquelheépermitida. Elementosdeumatabela, como td%,
thead e tr possuem seus próprios valores de display , como table-
cell e table-rowmassecomportamcomoelementosdebloco. Umaformadese
testarocomportamentodoselementosésimplesmenteadicionarumacordefundo
paracadaumdeleseobservaroespa çopreenchido.
p {
background-color: LimeGreen;
}
span {
background-color: LightBlue;
}
<span>inline</span>
<span>inline</span>
<p>block</p>
Figura6.1:Adiferen çadeelementos‘inline’e‘block’.
Alémdosvalorespadrões,existemduasoutraspossibilidadesbastanteúteispara
apropriedade display:o noneeo inline-block.
O nonefazcomqueoelementoetodooseuconteúdosumamdapágina,como
senãoestivessempresentesnoHTML,enquantoo inline-blockmisturaocom-
portamentodosvalores blocke inline-oselementosnãogeramquebras,mas
96


## Página 107

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
possuemasdimensõesequivalentesaocomportamentodasuapropriedade block.
Eleseriaumasolu çãoperfeitaparamuitosproblemassenãofosseumdetalhe:oes-
paçoentreoselementosnoHTMLimpactanaexibi çãodeles.ConsiderandooCSS
aseguir:
span {
display: inline-block;
}
EoHTMLcomoestiloaplicado:
<span>inline-block</span>
<span>inline-block</span>
<span>inline-block</span>
<br>
<span>inline-block</span><span>inline-block</span>
Figura6.2:Ocomportamentodo‘inline-block’comesemquebradelinhasentreos
elementos.Complicado,não?.
Casoexistaumaquebradelinhaouumespa çoentreoselementosnoHTML,
arenderiza çãodelescom inline-blockirápossuirumespa çoembranco-o
quemuitasvezesnãoéodesejado. ChrisCoyier,doCSS-Trickspropõediversas
soluções[2]paraesteproblema,masnenhumamepareceválidaosuficientepara
serutilizadacomfrequência.Souadeptodeoptarpelousode floatnestescasos.
6.2 Flutue elementos
Apropriedade floatéumadassolu çõesmaisversáteisquandosetratadealinhar
eposicionarelementos.Teveorigemnadiagrama çãodetextosnomundodamídia
impressaondeébastantecomumverimagens flutuandoaoladodepeda çosdetexto,
comoemumamatériadeumarevista. Naweb,essatécnicaevoluiuesoluciona
diversoscasosdeposicionamentodeelementos.
97


## Página 108

6.2. Flutueelementos CasadoCódigo
Ocasomaissimpleséparaalinharelementoshorizontalmente,flutuandoparte
delesedeixandoqueorestoacompanhepelalateral,dessaforma,comoseguinte
HTML:
<h2>#1</h2>
<h4>500 pontos</h4>
<p>Prêmio para o campeão: 1 MacBook Pro 15".</p>
EoCSS:
h2 {
float: left;
margin: 0 20px 20px 0;
}
h4 {
margin-top: 5px;
}
Teremos:
Figura6.3:Alinhandoelementoscom‘float:left’.
Elementoscomapropriedade floatsãotratadoscomoelementosdebloco
(lembrado display: block?),massemocuparos100%delarguratradicionais
desseselementos.Edamesmaformaqueelepodeflutuarparaesquerda,elepodeir
paraadireita.
h2 {
float: right;
}
98


## Página 109

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
Figura6.4: Vocêtambémpodejogarosseuselementosparaadireitacom‘float:
right’.
Paragarantirqueumelementonãováseguiraorienta çãodeumantecessorque
estejacom float,vocêprecisautilizarapropriedade clear.Vocêpodeinformar
omesmosentidoqueosseuselementosestãoflutuando- leftou right-ou
utilizar both,que quebraofluxoemambosossentidos.
p {
clear: both;
}
Figura6.5:Oefeitodapropriedade‘clear’-oparágrafonãoestámaisalinhadocom
otítulo.
Outraaplicaçãotradicionaldapropriedade floatéparaalinharimagensetex-
tos,similaraumamatériadejornal,emqueaimagemficaaoladodotextoquea
acompanha.
99


## Página 110

6.2. Flutueelementos CasadoCódigo
<h3>How I Met Your Mother</h3>
<img src="himym.jpg">
<p>
A série gira em torno da vida de Ted Mosby e dos seus amigos,
que é narrada pelo próprio aos seus filhos, 25 anos mais tarde.
Bob Saget, como Ted Mosby do futuro, conta então aos filhos as
histórias e peripécias que o levaram a conhecer a mãe deles.
As outras personagens principais são Marshall Eriksen,
Robin Scherbatsky, Lily Aldrin e Barney Stinson.
</p>
<p>
Em 2005, aos 27 anos, o jovem Ted Mosby (Josh Radnor), após o
seu melhor amigo, Marshall Eriksen (Jason Segel), ficar noivo,
decide finalmente ir em busca da sua cara-metade. Com gestos
românticos questionáveis, Ted conhece Robin Scherbatsky
(Cobie Smulders), no bar que costumavam frequentar,
Maclaren's Pub.
</p>
100


## Página 111

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
Comumsimplesusode floateumamargem(paraotextonãoficar colado
comaimagem)otextoseposicionaaoladodaimagem,fluindoperfeitamentecaso
otextosejamuitogrande,exatamentecomoonossoexemplo.
img {
float: left;
margin-right: 10px;
}
Figura6.6:Porpadrão,otextoficaráabaixodaimagem,ocupandobastanteespa ço
vertical.
Damesmaformaqueorganizamoselementosemexemplomenores,podemos
organizarosprincipaiselementosdapáginautilizando float.Horadepôramão
namassaeverissoema ção:
<section class= 'posts'>
<article>
<h1><a href= '#'>Título do post #1</a></h1>
<span class= 'timestamp'>3 semanas atrás</span>
<p>
Uma breve descrição sobre o assunto abordado no post número 1...
</p>
</article>
101


## Página 112

6.2. Flutueelementos CasadoCódigo
<article>
<h1><a href= '#'>Título do post #2</a></h1>
<span class= 'timestamp'>3 semanas atrás</span>
<p>
Uma breve descrição sobre o assunto abordado no post número 2...
</p>
</article>
</section>
Vamosdedicarumaáreade 600pxparaestalistagem,posicionandoainforma-
çãodadatadopostàdireitadotítulo,devidamentealinhado.
.posts {
width: 600px;
}
h1 {
float: left;
margin: 0 0 20px;
}
.timestamp {
background-color: #000;
color: #FFF;
float: right;
font-size: 0.9em;
margin-top: 10px;
padding: 5px 10px;
}
Figura6.7:Osprimeirosestilosdalistagemdeposts,organizandooselementoscom
‘float’.
102


## Página 113

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
Otítuloeainforma çãodadataestãonosseusdevidoslugares,masadescri-
çãonãodeveficarentreeles,esimabaixodotítulo.Horadeaplicarapropriedade
clear.
p {
clear: both;
}
Figura6.8:Corrigindoaposi çãodosparágrafos.
Vamosincrementaronossocenário:posicionamosumarela çãodelinksaolado
direitodase çãodeposts.Comofizemosnase ção2.6,aformamaissimplesdetratar
esteposicionamentodeelementoséflutuandocadaum-oconteúdoprincipalea
barralateral-paraladosdiferentes.Então,temosoHTMLcomalistadeposts:
<aside>
<h3>Veja outros posts</h3>
<ol>
<li><a href="#">Post #3</a></li>
<li><a href="#">Post #4</a></li>
<li><a href="#">Post #5</a></li>
<li><a href="#">Post #6</a></li>
</ol>
</aside>
OCSScolocaalistacomoutrosposts,queestarãodentrodo aside,nolado
direito,enquantoquealistagemdospostsquehavíamosfeitoantesseráexibidado
ladoesquerdo.
.posts {
float: left;
103


## Página 114

6.2. Flutueelementos CasadoCódigo
width: 600px;
}
aside {
background-color: #FFFBE4;
border: 1px solid #C9BC8F;
float: right;
padding: 10px;
width: 200px;
}
aside h3 {
margin: 0;
}
Figura6.9:Ovisualdase çãolateraldelinks.
Comcadase çãoflutuandoparaumlado,vamoscolocaramboselementosem
umanova div,paradefinirumalarguralimiteparaoconteúdoecentralizá-lo.
<div class= 'page'>
<section class= 'posts'>
<!-- ... os 2 posts principais ... -->
</section>
<aside>
<!-- ... e a lista de links para outros posts ... -->
</aside>
</div>
.page {
padding: 10px;
margin: 0 auto;
width: 940px;
}
104


## Página 115

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
Simples,certo?agoraaplicamosumacordefundoànovadivquecriamos,que
deverápreenchertodoofundodoconteúdodapágina.
.page {
background-color: #E8E8E8;
}
Figura6.10:Acordefundonãofoiaplicadacorretamentenapágina...
Masessenãoéoresultadoquequeremos!Umelementocom floatnãocon-
tribuicomaalturadoseu container,entãoelementoscomoonosso .pageapa-
rentamterapenasalguns pxdealtura,devidoaoseu padding,eoseuconteúdo
com floataparentatervazadodoelemento.Asolu çãoparaestecomportamento
estranhoéterumelementocom clearlogoapósoselementoscom floatque
causaramtalefeito.
Emexemplosanterioresissofoifeitoutilizandoumelementovazio,masessa
soluçãoacabasujandoonossoHTMLcomelementosvaziosparaajustarcasoscomo
esse.Aseguiriremosconhecerumasolu çãomaisadequadaparaoproblema.
105


## Página 116

6.3. Oclearfix,umaclasseobrigatóriaemseusprojetos CasadoCódigo
6.3 O clearfix, uma classe obrigatória em seus pro -
jetos
Esteproblemaclássicodeusode floatpodesersolucionadocomumelemento
vazioapósoconteúdoqueflutua,masnãoprecisamosadicionartagsvaziasaonosso
código,poisesteselementosadicionaisjáestãopresentesnapágina-ospseudo-
elementos,queforamapresentadosnase ção4.3.
Ochamado clearfix hackconsisteemadicionarestilosespecíficosparaos
pseudo-elementosdeum containerquetenhaelementoscom floateprecisetera
suaalturaadequadaaoconteúdo.
OcódigoCSSnecessárioébempequeno,masbastanteefetivo:
.clearfix::before,
.clearfix::after {
content: "";
display: table;
}
.clearfix::after {
clear: both;
}
.clearfix {
*zoom: 1;
}
Esteusoespecíficodovalor tableparaapropriedade displayservepara
ajustarbugsdemargementreo containereoselementoscom float,eousode
clear: bothno ::afterproduzomesmoresultadodesecolocarumelemento
vazioapósoconteúdo.
Aúltimaparte-apropriedade zoom,éumatécnicaespecíficaparaversõesan-
tigasdoInternetExplorer(6e7,paraserexato)epodeserignoradacasovocênão
precisetrabalharcomessasversõesdonavegador.
Semprecisardenovoselementos,podemosadicionaraclasse clearfixna
divdoexemploanterior,assimsolucionamosoproblemadasuacordefundo.
<div class= 'page clearfix '>
<section class= 'posts'>
<!-- ... os 2 posts principais ... -->
106


## Página 117

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
</section>
<aside>
<!-- ... e a lista de links para outros posts ... -->
</aside>
</div>
Figura6.11:Sucesso!problemadecordefundoresolvido.
Eventualmente,algunsdesenvolvedoresacabamutilizandoalgumoutronome
paraaclasse clearfix,como cf,reduzindoonomeparaseescrevermenos,ou
group,paraexpressarmelhorocontextodeuso. Independentedonome,sempre
atenhanosseusprojetosparatrataresseproblemaclássicodeusodapropriedade
float.
6.4 C ompreenda o uso de position
Outraformadecontrolaroposicionamentodosseuselementosécombinarousoda
propriedade positionedaspropriedadesdecoordenadas top, right, bottom
e left.Deacordocomovalordo position,ascoordenadassãoaplicadasdeuma
formadiferente,oquemudatodaaperspectivadeusodessegrupodepropriedades.
Dosquatrovalorespossíveis,omaissimpleséo static.Éovalorpadrãopara
todososelementos,easuaposi çãonãoéafetadapornenhumadaspropriedades
decoordenadas,deixandoqueonavegadorposicioneoelementonoseulugarde
origem.
Ovalor fixedremoveoelementodasuaposi çãooriginal(reorganizandoos
elementosadjacentes,casosejanecessário)efixaasuaposi çãonajaneladonavega-
dor.
Aposiçãodoelementoépreservadaconformeousuárionavegaparacimaepara
baixocomarolagemdapágina,útilparacaixasdemensagemquedevemsobrepor
107


## Página 118

6.4. Compreendaousodeposition CasadoCódigo
oconteúdoouelementosquedevemacompanharofluxodousuáriopelapágina,
comoumacaixadelinksdenavega ção.
Osdoisoutrosvalorespossíveissãoosquemaisconfundemosdesenvolvedores:
relativee absolute.
Comovalor relative,ascoordenadassãoaplicadasapartirdopontooriginal
doelemento,assim:
<div class= 'box'>
Teste
</div>
.box {
background-color: PapayaWhip;
height: 100px;
width: 100px;
position: relative;
top: 30px;
left: 5px;
}
Figura6.12: Acombinaçãodo‘position: relative’e‘top’afetandoaposiçãodeum
elemento.
Diferentedousode margin,oelementocom position: relativenãoirá
afetaraposi çãodoselementospresentesaoseuredor.Porexemplo,ousode top
nãoempurraoselementosseguintesparabaixo,masposicionaa divporcimadeles,
dessaforma:
108


## Página 119

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
<div class= 'box'>
Teste
</div>
<p>Um parágrafo de texto logo abaixo</p>
Figura6.13:Oelementocompositionpodeacabarporcimadeoutroselementos.
Jáovalor absolutepossuiumcomportamentomaiscomplicadodeseacos-
tumar.
Elementosabsolutamenteposicionadossãoafetadospelascoordenadasdaspro-
priedades top, bottomeafins.Noentanto,elassãoaplicadasapartirdoseupri-
meiroelementopaiquenãotenha position: static-então,elementos absolu-
tossão relativosaumelementopai.Casonenhumelementoacimadelenahierarquia
dasuapáginaatendaaestecritério,o bodyseráutilizadocomoreferência.
<h1>Posicionado com "absolute"</h1>
h1 {
background-color: LightBlue;
position: absolute;
top: 20px;
left: 30px;
}
Nesteexemplo,o h1estásendoposicionadodeacordocomo body.Masseo
colocarmosdentrodeoutroelementoqueestejaposicionadocomo relative,por
exemplo,aposi çãodo h1seráafetada.
<header>
<h1>Posicionado com "absolute"</h1>
</header>
109


## Página 120

6.5. Crieasuaprópriajanelamodal CasadoCódigo
header {
margin-top: 30px;
position: relative;
}
Figura6.14:Aoutilizaro‘position:relative’noheader,aposiçãodoh1muda.
Estapeculiaridadedousode absolutepodeapresentarmuitosproblemas,mas
tambémadicionamuitaflexibilidadeaousodessevalor.
Comooselementoscom absolutee fixedsãoremovidosdofluxopadrão
dapágina,elesnãoafetamaalturadoselementosquesupostamenteoscontêm,o
quegeraumproblemasimilaraousode float,massemumasolu çãosimilarao
truquedo clearfix.
6.5 Crie a sua própria janela modal
Janelasmodaissãoelementosrecorrentesemdiversossitesesãobonsexemplosde
aplicaçãode position.
Vamoscomeçarcomuma diveumparágrafo,queserãooconteúdodonosso
modal.
<div class= 'notice'>
<h1>Atenção</h1>
<p>Aqui você pode exibir alguma mensagem importante, que ela irá
sobrepor todo o conteúdo do seu site.</p>
</div>
Definimosalgunsestilosbásicosparaoformatodacaixaqueiráconterestecon-
teúdo,paragarantirquea divtenhaumaalturaelargurafixa,oqueiráfacilitarseu
posicionamento.
.notice {
background-color: #FFF;
border: 1px solid #000;
110


## Página 121

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
height: 130px;
padding: 10px;
width: 380px;
}
Horadeposicionaromodalnocentrodapágina,combinandoapropriedade
positioncomascoordenadas tope left.
.notice {
position: fixed;
top: 50%;
left:50%;
}
Nestecaso,éindicadoutilizarovalor fixedenãoo absolute-apesarde
aposiçãodoelementoseramesma,avantagemdeseutilizaro fixedéquecaso
asuapáginaexibaabarraderolagemvertical,omodaliráacompanhararolagem
paracimaeparabaixodousuário.
Comasporcentagensno tope left,ocantosuperiordireitodomodalestá
posicionadonocentrodapágina,masprecisamosalinharoelementotodo.Como
fixamosalarguraealturadomodal,ficasimplescorrigirissoutilizandomargens
negativas,finalizandooCSSparaestapartedomodal.
.notice {
background-color: #FFF;
border: 1px solid #000;
height: 130px;
padding: 10px;
width: 380px;
position: fixed;
top: 50%;
left: 50%;
margin: -75px 0 0 -200px;
}
111


## Página 122

6.5. Crieasuaprópriajanelamodal CasadoCódigo
Figura6.15:Oconteúdodonossomodal,devidamentecentralizadonapágina.
Apropriedade marginéaplicadademetadedaalturadoelemento( 150px)
notopoemetadedalargura( 400px)namargemesquerda( margin-left)do
elemento,naqualambososvaloressãonegativos,paraoelementoretrocederalguns
pxdevoltaparaocentrodapágina.
Outrocomportamentoquesempreacompanhaasjanelasmodaiséumasobre-
posiçãodecor-geralmentepretaoubrancaecomumacertaopacidade,entreo
conteúdodasuapáginaeasuajanelamodal.
Comasobreposi çãodecores,épossívelenfatizaradiferen çadomodalemrela-
çãoaorestodapágina,eatémesmoimpedirqueousuáriointerajacomoconteúdo.
Istocostumaserfeitocomoutroelementofixo,ocupandotodooespa çoútildona-
vegador,quecostumamoschamarde overlay.
<div class= 'notice'>
<h1>Atenção</h1>
<p>Aqui você pode exibir alguma mensagem importante, que ela irá
sobrepor todo o conteúdo do seu site.</p>
</div>
<div class= 'overlay'></div>
PodemosfazerumCSSparanosso overlay:
.overlay {
position: fixed;
top: 0;
left: 0;
background-color: rgba(0, 0, 0, 0.5);
width: 100%;
height: 100%;
}
112


## Página 123

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
Figura6.16:Adicionamosooverlay,maseleestásobrepondoomodal.
Masanossaimplementa çãolevantouumproblema-o .overlayficoupor
cimado .notice.
Comooselementoscom position: fixedou position: absolutesão
empilhadosporcimadapágina,aordemdoposicionamentoédadapelaordemdos
elementosnoHTML-entãocomo .overlayaparece apóso .notice,eleserá
posicionadoporcimadetudo.
Podemoscorrigiristodeduasmaneiras-oucolocamosocódigoHTMLda div
antesdoHTMLdonossomodal,oupodemoscontrolaraordemdasposi çõescom
apropriedade z-index,daseguinteforma:
.notice {
z-index: 1;
}
Figura6.17:Problemadesobreposi çãoresolvido!
Apropriedade z-indexredefineaordemdoselementosqueestãoposicionados
nomesmocontexto(nocasodosnossoselementos,estãoposicionadosdeacordo
como body).
113


## Página 124

6.5. Crieasuaprópriajanelamodal CasadoCódigo
Elementossemapropriedade z-indexsempreficarãoatrásdaquelesqueapos-
suem;eentreosquepossuemo z-indexdefinido,osquetiveremumvalormaior
serãoposicionadosafrentedosdevalormenor.
Elementosemcontextosdiferentes-comodoiselementoscom position:
absolute,porémcontidosemelementosdiferentescom position: relative
-nãocompartilhamdamesma sequênciadeaplicaçãodo z-index,entãoébem
fácilsecomplicarcomaordemdoselementosquandosepossuiumapáginamuito
complexa.
Paracasosassim, éindicadoqueoselementosdoseumodalsejamosúlti-
moselementosde todooseuHTML.Alémdeevitarproblemascomamudan ça
de positiondeoutroselementos,vocêgarantequeeleestaráporcimadoseu
conteúdodeacordocomaordempadrãodoselementos.
OcomportamentodomodalviaJavaScript
Comestecódigopronto,podemoscome çaraadicionarocomportamentoem
JavaScriptparaexibirouesconderomodal.Escondemosos2elementoseadiciona-
mosum linkparaexibiromodalquandonecessário.
<a id= 'show-modal' href='javascript:;'>Exibir modal</a>
.notice, .overlay {
display: none;
}
Figura6.18:Olinkparaexibiromodal,semestilonenhum.
OcódigoJavaScriptparaexibiromodalébastantesimplescasovocêestejauti-
lizandojQuery.
$('#show-modal').on('click', function() {
$('.overlay, .notice ').show();
});
114


## Página 125

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
EstaslinhasdeJavaScriptsãoresponsáveispeloseguintecomportamento:ire-
mosassociarumafun çãoaoeventode clickdequalquerelementoqueatendao
seletor #show-modal(obotão,nestecaso).Essafun çãoiráselecionaroselemen-
tosdonossomodaleirámodificarapropriedade displayparaexibi-losparao
usuário.
Agoraqueconseguimosexibiromodal,precisamosescondê-lotambém,certo?
Paraisso,vamosprecisardeumbotãodefechar,dentrodele,quepodeserposicio-
nadoporcimadocantosuperiordireitodoelemento,quasequesaindodoespa ço
domodal.SeuHTMLéumsimpleslink:
<div class= 'notice'>
<h1>Atenção</h1>
<p>Aqui você pode exibir alguma mensagem importante, que ela irá
sobrepor todo o conteúdo do seu site.
</p>
<a href= 'javascript:;' class='close'>Fechar</a>
</div>
EoseuCSS:
.notice .close {
background-color: #FF1A2D;
color: #FFF;
padding: 5px;
position: absolute;
right: -25px;
top: -12px;
}
Figura6.19:Obotãoparafecharonossomodal.
Comoo .noticejápossuiumadefini çãode position,ficafácilposicio-
narobotãode "Fechar”emrelaçãoàposi çãodomodalcomoutracombina çãode
position+coordenadas.Oquerestaéadicionaroeventode clickdestebotão
paraesconderoselementosdomodal.
115


## Página 126

6.6. Comoescolherosmétodosparaposicionarosseuselementos CasadoCódigo
$('.overlay, .close ').on('click', function() {
$('.overlay, .notice ').hide();
});
Vamosassociaroeventode clickdedoiselementos-o .overlayeo
.close,separandoosdoisseletorescomumavírgula-eoeventoiráescondertanto
o .overlayquantoo .notice.Assim,casoousuárioclique foradajanela,elaserá
fechada,eestaa çãonãoficaráreduzidaparaapenasopoucoespa çoocupadopelo
botão.Eépossíveliralém:associaroeventode keydowndotecladodoseuusuário
paraesconderomodalcasoeletecle ESC.Tenteadicionarestecomportamentoe
vejacomoficaoresultadofinal!
6.6 C omo escolher os métodos para posicionar os
seus elementos
Passamos por algumas opções diferentes de como estruturar e posicionar os
nossos elementos nos layouts, mas a escolha de se devemos usardisplay:
inline-blockou position: absoluteemumdeterminadocasopodelhe
custaralgunsminutos,porissoébomteremmenteemquaiscenárioscadacombi-
naçãodepropriedadesémaisindicada.
Enquantoresultadossimilarespodemseralcan çadoscomtécnicasparecidas,so-
luçõesmaissimplesequerequeremmenoscódigosãosemprerecomendadaspara
facilitaramanuten çãodoseuprojeto.
Seoespa çamentoentreelementoscom display: inline-blocknãofor
umproblemaparavocê,comonaestrutura çãodecamposerótulosemumformu-
lários,utilizeestapropriedade,porseraimplementa çãomaissimples. Paracasos
dealinhamentohorizontalmaiscomplicados,emqueoespa çamentocausadopelo
inline-blocknãosejaumaop ção,combine floatcomalgumelementocom
clearouuseotruquedo clearfixno containerdoselementosemquestão.
Paracasosdesobreposi çãodeelementosoucenáriosondevocêprecisaposicio-
narumelementoemumpontoespecífico,comonousodepseudo-elementoscomo
íconesoudecora çõesvisuais,oubotõesetítulosquevazamoespa çodeseus contai-
ners,combineo position: absolutecomo position: relativeparater
totalcontroledaposi çãodosseuselementos.
116


## Página 127

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
6.7 Grids- um padrão de estrutura para as suas pá -
ginas
Gridssãoumsistemaderegrasparadefinirumnúmerodecolunasdisponíveisnos
seuslayouts,paradefiniralarguraeespa çamentodosseuselementosdeacordocom
otamanhopadrãoeespa çamentoentreumacolunaeoutra.Vocêpodeutilizarqual-
quertipodegrid,de12ou16colunas,delargurasfixasourelativas,comespa çamento
entrecolunasounão.
Diversasimplementaçõeseframeworksestãodisponíveisporai,comooclássico
960.gs(http://960.gs/),TwitterBootstrapouoFoundation(vocêpodelermaisa
respeitodestesúltimosnase ção10.1),masvocêpodecriaroseuprópriogridpara
osseusprojetos.
Pegaremososeguintegridcomoexemplo:9colunasde 50pxcada,com 10px
demargenslaterais.Podemosdefinirqueacolunaprincipaldeconteúdoiráocupar
oespaçode6colunasdogrid,enquantoabarralateralocupará3colunas.
<article class= 'column six-columns '>
<!-- Conteúdo principal... -->
</article>
<aside class= 'column three-columns '>
<!-- links de navegação -->
</aside>
Figura6.20:Umexemplodeconteúdodistribuídoentrecolunasdeumgrid.
117


## Página 128

6.8. PosicionandoelementoscomCSS3 CasadoCódigo
Asdefiniçõesdeclassesparaaquantidadedecolunasqueumelementopode
ocuparsãoasregrasdelarguraqueosseuselementosdevemseguir.Nesteexemplo,
nãopodemosterumabarralateralqueocupe 200pxouespaçarseçõesadjacentes
emmaisdoque 20px.Taispadrõesdetamanhoeespa çamentopodemeconomizar
muitotrabalhonadefini çãodoslayoutsenaescritadoseuCSS.
Entretanto,antesdeabra çarousodegridscomoumasolu çãoperfeitaparaos
seusproblemas,nãodeixeseatentarapontosimportantesaocolocaramãonamassa:
éoseugridquedeveseadequaraoseuconteúdo,enãoocontrário.Eémuitofácil
desecomplicardefinindoumnúmeromaiordecolunasdoqueonecessário-um
gridde3ou5colunaspodeserosuficienteparaamaioriadosseusprojetos.
6.8 Posicionando elementos com CSS3
Existemváriastécnicasdiferentesquepodemosutilizarparadiagramareposicionar
oselementosnosnossosprojetos,masnemtodososcenárioseproblemaspossuem
soluçõessimpleseelegantes-écomumencontrarajustesecorre çõesfeitasviaJa-
vaScriptparaproblemasquedeveriamsersolucionadoscomCSS.
AlgumasadiçõesdoCSS3permitemqueproblemasantigossejamsolucionados
comcódigosnovos,oqueérazãodefestaparaqualquerdesenvolvedor.
Masatenção,poisosmódulosdoCSS3relacionadosàposi çãoecontroledecon-
teúdonãoestãotãomadurosquantoaosdepropriedadescomo box-shadowou
border-image,entãoéimportanteconferirasitua çãodosuportedosnavegadores
aessasnovidades.
Distribuiçãodeconteúdoemcolunas
Distribuirumblocodeconteúdo-textos,linksouimagens-emdiversascolunas
ficoumuitofácil.Emvezdedividiroconteúdomanualmenteemelementossepara-
dosesepreocuparcomalarguraeespa çamentoentreelesvocêpodesimplesmente
deixarestatarefaparaonavegador,comapropriedade column-count,comaqual
vocêdefineaquantidadedecolunasqueoseuelementoterá,eficaacargodonave-
gadordistribuiroconteúdoedimensionarcadauma,independentedotamanhodo
seuelemento.
Alémdisso,existempropriedadesadicionaisparadefinirnovosdetalhesdocom-
portamentodassuascolunas,como column-gap(espaçamentoentrecolunas),
column-rule(abordaquedividiráascolunas)ou column-fill(aregrauti-
lizadaparadistribuiroconteúdoentreascolunas).Umexemploaseguirdemonstra
118


## Página 129

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
quãosimplesédividirumpeda çodeconteúdoentrecolunas.
<p>
Firefly é uma série de ficção científica criada pelo escritor/diretor
Joss Whedon, criador de Buffy: A Caça Vampiros, Angel e Dollhouse,
com sua companhia de produção Mutant Enemy Productions. Seu ambiente
futurista naturalista, modelado a partir de temas dos filmes de Western
tradicionais, apresenta um cenário de ficção científica atípico para a
narrativa. Whedon também trabalhou como produtor executivo,
junto com Tim Minear.
</p>
EoCSSqueutilizaasnovasregrasparacolunas:
p {
column-count: 3;
column-gap: 10px;
column-rule: 1px solid #666;
font-size: 0.9em;
width: 500px;
}
Figura6.21:AdivisãoautomáticadoconteúdoemcolunascomCSS3.
Elementosflexíveis
UmmódulobastanteinteressantedoCSS3éo CSSFlexibleBoxLayoutModule ,
queintroduzdiversasnovaspropriedadesparadefinirregrasdeposicionamentoe
alinhamentorelativas,emqueoselementospresentesemum container flexse-
rãoorganizadosautomaticamentepelonavegador,deacordocomasdefini çõesfei-
tas,semanecessidadedesefixartamanhosoufor çaralinhamentoscom floatou
position.
119


## Página 130

6.8. PosicionandoelementoscomCSS3 CasadoCódigo
Tudosebaseianonovovalordapropriedade display: flex.Comele,agama
depropriedadesdo flexboxestarãodisponíveisparaoselementoscontidosdentro
deste container.Como,porexemplo,for çarumaorienta çãoverticalouhorizontal,
semanecessidadedeaplicarapropriedade floatnoselementos.Ou,então,dis-
tribuiralarguradoelementoentreseusfilhos,alteraraordemdeexibi çãooufor çar
umespaçamentoigualparatodos.
Mascomonemtudosãoflores,aespecifica çãodessemódulosofreuumare-
escritapesadaeaindaestáemconstanteatualiza ção,oquepodefazercomqueos
códigosaseguir,frustrantemente,nãofuncionem,dependendodaversãodonave-
gadoremqueforaberto.
Aversãoantigadaespecifica çãofoiimplementadaemdiversosnavegadores,mas
onovoformatoaindanãoestámaduroosuficienteparaseutilizaremseusprojetos.
Maseusugiroquevocêfiquedeolhonasnovidadesrelacionadasao flexbox,já
quelogomaiselepoderáseradotadoemprojetosfuturos.
Vamosdarumaolhadadepertonoqueépossívelfazercomo flexbox:pri-
meiro,vamosprecisardeum containercom3elementos,ondeelesirãopreencher
todaalarguradisponíveligualmente:
<div class= 'flexbox'>
<span class= 'one box '>1</span>
<span class= 'two box '>2</span>
<span class= 'three box '>3</span>
</div>
Esse containerterá300pxdelargura,entãocadaumdoselementosiráocupar
100px.
.flexbox {
/*
De acordo com a nova especificação, o valor "flexbox"
deverá ser substituído por apenas "flex".
*/
display: flexbox;
height: 60px;
width: 300px;
}
.box {
color: #FFF;
display: block;
120


## Página 131

CasadoCódigo Capítulo6. Tomandocontroledaestruturavisual
flex: auto;
font-weight: bold;
height: 30px;
line-height: 30px;
text-align: center;
}
Paraidentificarmelhorcadaumdoselementos,vamosdefinircoresdefundo
diferentesparacadaumdeles.
.one { background-color: #8820DD; }
.two { background-color: #2BB15A; }
.three { background-color: #755322; }
Figura6.22:Trêselementosflexíveis,distribuídospor300pxdelargura.
Nesteexemplotemosduasnovidades:ovalor flexbox(queserásubstituído
por flexnofuturo),quemarcao containercomoumelementoflexível,eapropri-
edade flex,naqualvocêpodedefinirdiversoscomportamentosdiferentesparao
elemento.
Nestecaso,ovalor autodefinequeeleiráocuparomáximodeespa çopossível,
distribuindoos 300pxentrecadaumdeles.Masissopodeseralcan çadoutilizando
porcentagensnapropriedade widtheflutuandooselementos,certo?
Éaquiquemoraadiferen çaentreestesmétodos.Comonãoestamosdefinindo
largurasfixasparaoselementosflexíveis,podemosadicionarmaisconteúdocoma
classe .box,quealarguradoselementosseráajustadapelonavegador-vocênão
precisapularnoCSSerecalcularaslargurasdoselementos.
<div class= 'flexbox'>
<span class= 'one box '>1</span>
<span class= 'two box '>2</span>
<span class= 'three box '>3</span>
<span class= 'four box '>4</span>
<span class= 'five box '>5</span>
</div>
121


## Página 132

6.8. PosicionandoelementoscomCSS3 CasadoCódigo
Nãovamosdeixardeladoascoresdoquartoequintoelemento:
.four { background-color: #02A3A3; }
.five { background-color: #C6363D; }
Figura6.23:Oscincoelementosocupandoos300pxdocontainer.
Nãoterqueajustaraslargurasoudefinirnovasclasseségrandevantagem-os
elementosflexíveispodemsercriadosdinamicamente,variandode3a10,eares-
ponsabilidadedeorganizá-losedefinirosseustamanhosficaacargodonavegador.
122


## Página 133

Capítulo7
Melhorandoosseusformulários
Formuláriossãoumdospontosmaiscríticosdamaioriadossites:alémdeserem
aportadeentradaparaseususuárioseclientessecomunicaremouproveremin-
formaçõesparavocê,sempreestãorelacionadosaprocessosimportantesparaoseu
negócio,sejafinalizandoacompraemum e-commerce,criandoartigosparaumpor-
talouenviandonovasfotosparaumaredesocial.Porisso,devemoscriarformulá-
riosquenãofiquemnocaminhoparaatrapalharnossosusuáriosemsuastarefasnos
projetosquecriamos.
7.1 Oque temos no HTML5
Umadasadi çõesmaisinteressantesdoHTML5sãoosdiversoscamposnovospara
formuláriosenovoscomportamentosparaenriqueceraexperiênciadisponívelpara
osformulários.Novostiposdecampos,como email, searche rangeeatributos
como placeholder, patterne requireddizemmaissobrequetipodeinfor-
maçõesnossosformuláriosprecisamereduzemanecessidadedeusarmosplugins
emJavaScriptparaauxiliaraformata çãodoselementos.


## Página 134

7.2. FormuláriosHTML5nosdispositivosmóveis CasadoCódigo
Noassuntodenovoscampos,temosdiversosnovosvaloresparaoatributo type
datag input.Tiposcomo email, tel, numbere urlagregamasemânticado
seuHTMLparadefinirotipodeinforma çãoqueoformulárioprecisa,apesardenão
causarmudançasdrásticasaovisualdosseuselementos.Ostipos color, range
e datepermitemqueonavegadorrenderizeelementosespecíficosparaescolhero
valorapropriadoparaessestiposdeinforma ção.
Além disso, diversos novos atributos estão sendo adicionados para melho-
raraexperiênciadosusuáriosaointeragircomosformulários,comooatributo
placeholder,queexibeumtextoespecíficoquandoocamponãoestápreenchido
-quedeveserusadoparaexemplificarformatoseexpormaisdetalhessobreoscam-
pos.Paraefetuarvalida çõesnonavegador,osatributos required, maxlengthe
patternpermitemdefinirquaiscamposdevemserpreenchidosantesdeoformu-
lárioserenviadodevoltaparaoservidor;Eparaocamposdotipo file,pode-se
definirqueocampoaceitaváriosarquivoscomoatributo multipleeatérestringir
ostiposdearquivosaceitosatravésdoatributo accept.
Essesdiversosnovostiposeatributosestãosendoconsolidadoseimplementados
aospoucos,entãoconfiracomoestáosuporteaoquevocêprecisadeacordocom
osnavegadoresquevocêdeseja.Porpadrão,casoonavegadornãotenhasuportea
umtiponovodecampo,oelementoserátratadocomoumcampodetextonormal
type='text',paragarantirofuncionamentobásicodosformulários.
7.2 Formulários HTML5 nos dispositivos móveis
Enquantocamposcomoo emailou urlpodemparecerdesnecessáriosoupro-
blemáticosdevidoainconsistênciasentrenavegadores,elespossuemumafuncio-
nalidademuitointeressantequandousadosemnavegadoresdedispositivosmóveis,
comotabletsoucelularescomiOSouAndroid. Osaparelhosapresentamumte-
cladodiferenteaousuárionomomentodeinteragircomcamposespecíficos.Para
umcampocom type='number',otecladojáexibeasteclasdenúmerosenão
asletras. Paraocampodee-mail,otecladopadrãorecebeaadi çãodeumbotão
dearroba( @). Enocasodecamposcom type="url",oiOSgentilmenteexibe
umbotãoparasedigitar‘.com’comapenasumtoque. Apesardenãoserumpa-
drãodefinidoentreosfabricantes,essasmudan çassãomuitoúteisparaosusuários-
lembre-sedetirarproveitodessescamposparafacilitaravidadosseususuáriosque
usamtaisdispositivos.
124


## Página 135

CasadoCódigo Capítulo7. Melhorandoosseusformulários
Figura7.1:ExemplosdotecladonuméricodoiOS5eAndroid4
Referências de quem vive do assunto
OWufooéumsitequepermitecriarformuláriossemprecisarenten-
derouescreverHTMLouCSSevocêconsegueusá-losemoutrossites
pararecebermensagensdecontato,criarpesquisaseatéreceberpaga-
mentos. Comofococonstanteemmelhorarseusformulárioseprover
diversasfuncionalidadesemcimadeles.
OsdesenvolvedoresdoWufoocriaramumaótimareferênciaparaos
novostiposdecamposeasnovasfuncionalidadesdeformuláriospresen-
tesnoHTML5. Acessehttp://wufoo.com/html5/parasabermaissobre
compatibilidadedenavegadores,exemplosdecódigoemais.
7.3 Criação do primeiro formulário
Vamoscomeçarcomumexemplobásicoporémbemrefinadodeumformulário:
umapáginadecontatocontendocamposparae-mail,assuntoemensagem. Esse
125


## Página 136

7.3. Criaçãodoprimeiroformulário CasadoCódigo
formulárioterádicasexplicandocomoainforma çãodeveserpreenchidaemcada
campo.Alémdisso,iremosprepararelementosparanotificarosusuárioscasohaja
problemasdevalida ção-umpassoquesempredeveserlevadoemconsidera çãoao
criarpáginascomoessa.
Figura7.2:Oformulárioquevamoscriaraseguir
Marcaçãobásica
Vamoscomeçarcomatag form,ocampodee-maileumbotãodeenvio:
<form method= 'post' action=''>
<label for= 'email'>E-mail:</label>
<input type= 'email' id='email' name='email'>
<button>Enviar mensagem</button>
</form>
Nossoformulárioestácomomethoddefinidocomo post,jáquepretendemos
criarumamensagemdecontatonosite.Comovalordoatributo actionvazio,o
navegadoriráenviarosdadosdoformulárioparaomesmoendere çodapáginaatual:
seestamosemhttp://meusite/contato,aoclicarnobotãodeenvioosdadosirãopara
omesmohttp://meusite/contatoatravésdométodo post.
Parasepararocampoebotãodeenvio,vamoscolocaroselementosdoformu-
láriodentrodeparágrafoscomatag p.
<p>
<label for= 'email'>E-mail:</label>
126


## Página 137

CasadoCódigo Capítulo7. Melhorandoosseusformulários
<input type= 'email' id='email' name='email'>
</p>
Nomesmomodelo,podemosadicionarosoutroscamposdoformulário-um
campodetextoparaoassuntodamensagemeumacaixadetextoparaocorpoda
mensagem:
<p>
<label for= 'subject'>Assunto:</label>
<input type= 'text' id='subject'>
</p>
<p>
<label for= 'content'>Mensagem:</label>
<textarea id= 'content'></textarea>
</p>
Figura7.3:Oscamposdoformulário
Comaestruturabásicaeoscamposnecessários,podemospassarparaopróximo
passoeadicionarregrasdeestiloparaonossoformulário.
7.4 Alinhamento e estilos visuais nos campos e for -
mulários
Começamosalinhandotodasascaixasdetextonamesmaposi ção.Paraisso,preci-
samosfixaramesmalarguradecada label,evamosaproveitarparadeixá-loscom
otextoemnegrito:
label {
display: inline-block;
127


## Página 138

7.4. Alinhamentoeestilosvisuaisnoscamposeformulários CasadoCódigo
font-size: 0.9em;
font-weight: bold;
width: 90px;
}
Definindoapropriedade displaycomo inline-block,podemosfixaralar-
guraemanteroscamposaoladodoslabels.Utilizandoapenas blockoscampos
ficariamabaixodoseurespectivo label,independentedalarguradefinida.Pode-
mosfazeromesmoparaastags inpute textareaparamantertodososelementos
devidamentealinhados.
input, textarea {
display: inline-block;
width: 200px;
}
Alémdalargura,vamosfixartambémaalturada textarea,garantidoumbom
espaçoparasedigitarumtextocomprido.
textarea {
height: 100px;
}
Figura7.4:OscamposelabelsdevidamentealinhadoscomCSS.
Horademelhoraraaparênciadoscamposdoformulário:vamostrocarasbordas
padrõesdoscampos,adicionarumasombraeespa çamentointernoereduzirum
poucoafonte:
128


## Página 139

CasadoCódigo Capítulo7. Melhorandoosseusformulários
input, textarea {
border: 1px solid #CCC;
box-shadow: inset 2px 2px 2px #EEE;
font-size: 0.9em;
padding: 2px 5px;
}
Figura7.5:Oscamposcomasmudan çasdeestiloquecriamos.
Pronto,alterandopequenosdetalhesdoestilopadrãodoselementosconsegui-
moschegaraumvisualsutilporémbastanteagradável.Paracomporasombra,usa-
mosaop ção inset,quedefinequeasombraseráexibidadentrodoelementoe
nãoforadele.Asombranãoseráexibidaemnavegadoresquenãopossuemsuporte
a box-shadow,masissonãoimpediráoucomplicaráousodoformulário,garan-
tindosuafuncionalidadeemnavegadoressemsuporteaessaspropriedadesdoCSS
3,comoversõesantigasdoMozillaFirefoxedoInternetExplorer.
7.5 Exibição de mensagens de ajuda
Agoraquetemososcamposdevidamenteestilizados,podemosadicionarumnovo
elementoparamostrarumadescri çãodoscampos,paraqueauxilieaspessoasque
forempreencheroformulário-mensagensdeajuda,quepodemexplicararespeito
delimitedecaracteres,formatosespecíficosedetalhesextras.Pararepresentaressas
mensagens,usaremosatag spancomaclasse hint.
<p>
<label for= 'email'>E-mail:</label>
129


## Página 140

7.5. Exibiçãodemensagensdeajuda CasadoCódigo
<input type= 'email' id='email' name='email'>
<span class= 'hint'>por exemplo, seunome@dominio.com.</span>
</p>
<p>
<label for= 'subject'>Assunto:</label>
<input type= 'text' id='subject'>
<span class= 'hint'>Nos diga qual é o seu problema ou ideia.</span>
</p>
<p>
<label for= 'content'>Mensagem:</label>
<textarea id= 'content'></textarea>
<span class= 'hint'>
Escreva a sua mensagem, em até 500 caracteres.
</span>
</p>
Agora,precisamosadicionarumestiloaessasmensagensparaelassedestacarem
nainterface,chamandoaaten çãodosusuários.
.hint {
background-color: #FFFBE4;
border-radius: 3px;
border: 1px solid #CCC;
box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
display: inline-block;
font-size: 0.8em;
margin-left: 20px;
padding: 3px;
}
Umtomdeamarelocomofundo,bordaslevementearredondadas(usandoapro-
priedade border-radius)eumasombra(comautiliza çãode rgbaemvezde
umacorsólida,reduzindobastanteaopacidadedacorpreta).Alémdisso,umamar-
gemde 20pxparadistanciarumpoucoasmensagensdosseuscampos.
130


## Página 141

CasadoCódigo Capítulo7. Melhorandoosseusformulários
Figura7.6:Todasasmensagensdeajudajuntodoscampos.
Decertaforma,exibirtodasessasmensagensaomesmotempopodeatrairaten-
çãodemaiseatrapalharofluxodeusodoformulário. Porquênãoexibirasmensa-
gensconformeoformulárioforpreenchido?IstoépossívelusandoapenasCSS!
Primeiro, vamos esconder todas as mensagens alterando a propriedade
displayde inline-blockpara none.Comtodaselasescondidas,vamosexi-
birapenasamensagemrelacionadaaocampoqueestejaemfoco-aoselecionaro
campode“E-mail”,porexemplo,amensagemdeajudaparaestecamposeráexi-
bida,quandosepassarparaopróximocampo,“Assunto”,amensagemdocampode
“E-mail”desaparecenovamenteeamensagemparaocampode“Assunto”éexibida.
Paraissoutilizaremososeletorde sibling(irmão,nocaso),usandoosímbolode
adição +:
.hint {
display: none;
}
input:focus + .hint, textarea:focus + .hint {
display: inline-block;
}
Oseletorpodeserlidocomo“umelementocomaclasse hint,posicionadoexa-
tamentedepoisdeumelemento input(ou textarea)queestejaemfoconona-
vegador”.Assim,asmensagenssetornarãovisíveis(tendoapropriedade display
sobrescritade nonepara inline-block)conformeoscamposrecebemeperdem
ofoco.
131


## Página 142

7.6. Mostremensagensdeerro CasadoCódigo
Figura7.7:Agora,somenteumamensageméexibidaporvez.
Mas e o atributo “placeholder"?
Oatributo placeholderfoioriginalmentecriadoparaexibirfra-
sesdeajudaeexemplosdeformatosdentrodospróprioscamposcriados
comatag input,mascomelenãopossuímostantaflexibilidadepara
mudançasdeestiloeumamelhorintera çãocomosusuários-nonosso
exemplopodemosatéadicionarlinksparapáginasdeajudamaiscom-
pletaseutilizaroutrasformasdeestilo-comopalavrasemnegritoouem
outrascores-parareal çaramensagemaserexibida.
7.6 Mostre mensagens de erro
Comnossasmensagensdeajudaemposi ção,temosumoutrotipodemensagema
exibirnoformulário: deerrosevalida ções. Nãopretendoentraremdetalhesem
comotaisvalida çõesdevemserfeitas(sejautilizandoJavaScriptnonavegadorou
processandoissocomasualinguagemdeprograma çãopreferidacomoRuby,Python
ouJavaemumservidorexterno),massempredevemosguardarumespa çoparatais
mensagensedefinirumestiloespecíficoparaelas.
Vamossimularqueoformuláriofoienviadosemocampo“E-mail”edevemos
notificarousuáriodisso.Come çamoscomumelemento spancomaclasse error,
paraidentificarexatamentequaiselementos spanestãoexibindotaismensagens.
<p>
<label for= 'email'>E-mail:</label>
132


## Página 143

CasadoCódigo Capítulo7. Melhorandoosseusformulários
<input type= 'email' id='email'>
<span class= 'hint'>por exemplo, seunome@dominio.com.</span>
<span class= 'error'>Preencha o seu e-mail corretamente.</span>
</p>
Posicionamosamensagemexatamenteabaixodo input.
.error {
color: red;
display: block;
font-size: 0.8em;
font-style: italic;
margin: 5px 0 0 90px;
}
Figura7.8:AmensagemdeerroabaixodocampodeE-mail.
Ovalor blocknapropriedade displayvaigarantirqueoelementofique
abaixodosdemais,do label, inputeooutro span. Osvaloresdemargem
posicionameste spanabaixodacaixadetexto,com 5pxdedistânciaentreeles.
Acorvermelhaeotextoemitálico(gra çasao font-style),garantemumcerto
destaqueemrela çãoaooutroselementosqueestãoemtonsdepretoecinza.
Agorabastareplicaromesmoexemploparaosoutroscamposdoformulário-
“Assunto”e“Mensagem”,garantindooespaçoreservadoparasuasmensagensdeerro
devalidações!
Dessamaneira,bastariaquequandoavalida çãofossefeita,sejanoladodoser-
vidorounoladodocliente,houvesseumaregraparadeixaressenovo spanvisível
quandoaconteceoerrodevalida ção.
133


## Página 144

7.7. Levandoousuáriodiretoaoqueimportacomoautofocus CasadoCódigo
7.7 Lev ando o usuário direto ao que importa com o
autofocus
Podemosadicionarmaisumtruqueaoformulário:o autofocus. Aocarregara
página,ocursoriráfocarocampode“E-mail”parafacilitarotrabalhodosusuá-
riosquequeremutilizaroformulário. Aimplementa çãoébemsimples,bastando
adicionarumatributoaocampo:
<input type= 'email' id='email' autofocus>
Sim,apenas autofocus.Nãoprecisamosadicionarnenhumvaloraoatributo
paraativá-lo.Dessaformaocampode“E-mail”receberáofocodajanelaeamen-
sagemdeajudatambémapareceráaocarregarapáginadoformulário.
Apenasalgunspontosimportantesquesedeveprestaraten çãoaousaresteatri-
buto:casovocêtenhamaisdeumcampocom autofocus,eventualmenteoúltimo
campopresentenoHTMLreceberáofoco.Ecasosejanecessáriodescerabarrade
rolagemdajanelaparachegaraocampo,onavegadorirádescerapáginaparaexibir
ocampofocado,pulandoqualquerconteúdoanterioraoformulário.Comexce ção
denavegadoresemdispositivosmóveis(comooMobileSafaridoiOS5eonavega-
dordoAndroid2.3),todasasúltimasversõesdosnavegadoresdedesktoppossuem
suporteao autofocus.
7.8 A flexibilidade do atributo placeholder
Comenteiarespeitodoatributo placeholderecomoutilizamosmeroselementos
parasubstituiroqueesteatributofoicriadoparafazer.Agoravamosinverteroce-
nário-utilizaremoso placeholderdecamposdoformuláriopara,visualmente,
substituiroseu label.Essaabordagempodeserútilparaformuláriosmenorese
simples,quandoseprecisaeconomizaralgunspixelsdasuapágina.
OHTML
OHTMLparaesteformulárioébastantesimples-nãovamosprecisardepará-
grafosparacadacampo,masvamostero labeldecadacampopresente,mesmo
considerandoquenãovamosexibi-losnainterfacefinal:
<form method= 'post' action=''>
<label for= 'username'>Usuário</label>
<input type= 'text' id='username'>
134


## Página 145

CasadoCódigo Capítulo7. Melhorandoosseusformulários
<label for= 'password'>Senha</label>
<input type= 'password' id='password'>
<button>Entrar no site</button>
</form>
Existemduasrazõesparatermoso labeldocampode“Usuário”ede“Senha":
primeiro,precisamosdisponibilizartaiselementosparaauxiliarleitoresdetelaspara
deficientesvisuaisanavegarempelanossapágina.Segundo,casoonavegadorque
forutilizadoparaacessarapáginanãocarreguetodoonossoCSSounãopossua
suporteaoatributo placeholder,oformulárioaindaseráfuncionalparaquemo
utilizar.
Com isso esclarecido, vamos continuar e adicionar os textos para o
placeholderdecadacampo.
<form method= 'post' action=''>
<label for= 'username'>Usuário</label>
<input type= 'text' id='username' placeholder='Usuário'>
<label for= 'password'>Senha</label>
<input type= 'password' id='password' placeholder='Senha'>
<button>Entrar no site</button>
</form>
Comostextosemposi ção,vamosaoCSS.
AplicandooCSSnecessário
NossoprimeiropassoaplicandooCSSnesteformulárioseráescondero label
decadacampoeempilharocampode“Usuário”juntoaode“Senha”,empurrando
obotãoparabaixo:
label {
display: none;
}
input {
display: block;
}
button {
margin-top: 5px;
}
135


## Página 146

7.8. Aflexibilidadedoatributoplaceholder CasadoCódigo
Figura7.9:Oscamposcomoatributo‘placeholder’.
Ecomumpoucomaisdecódigo,embelezamosoformuláriocombordasesom-
bras.
input {
border-radius: 3px 3px 0 0;
border: 1px solid #999;
box-shadow: 1px 1px 5px rgba(0,0,0,0.2);
font-size: 0.8em;
padding: 5px;
}
input[type='password'] {
border-radius: 0 0 3px 3px;
border-top: none;
}
Figura7.10:Nossoformulárioumpoucomaisapresentável.
Bastantesimples,certo?Arredondamosapenasoscantossuperiores(deixando
osdoisúltimosvaloresdo border-radiuscomovalor 0),aplicamosumaborda
cinzaeumalevesombrautilizando rgba.Eparaocampode“Senha”,invertemos
osvaloresdo border-radius.
136


## Página 147

CasadoCódigo Capítulo7. Melhorandoosseusformulários
Podemosalteraroestilodotextodoscampos,masomesmonãoéaplicadoao
textoexibidodo placeholder.Paraisso,precisamosutilizarumpseudo-seletor
específicoparaestetexto.Devidoaproblemasdecompatibilidades,navegadoresdi-
ferentesdãoumnomediferenteparaomesmoseletor,entãoprecisamosespecificar
todoseles,assim:
::-webkit-input-placeholder {
color: red;
}
::-moz-placeholder {
color: red;
}
-ms-input-placeholder {
color: red;
}
Figura7.11:Aplicandoopseudo-seletorparaplaceholders.
O -webkit-input-placeholderédirecionadoparaosnavegadoresbasea-
dosnoWebKit-comoSafarieoGoogleChrome.Osdemais, -moz-placeholder
e -ms-input-placeholder,atendemoMozillaFirefoxeoInternetExplorer10,
respectivamente.Cadanavegadorprocessaráumseletordiferente,eprecisamosre-
petiraspropriedadesentreeles.
Apesardarepeti ção,ganhamostotalcontrolesobreoestilodoplaceholder-po-
demosalterarcores,tamanhosefundos.Porexemplo,podemosdeixarotextodigi-
tadonocampoemnegritoeotextodo placeholderemitálicoecinza,ajudando
adiferenciarentreumcampopreenchidoeumcampoembranco.
input {
font-weight: bold;
137


## Página 148

7.8. Aflexibilidadedoatributoplaceholder CasadoCódigo
}
::-webkit-input-placeholder {
color: #666;
font-style: italic;
font-weight: normal;
}
:-moz-placeholder {
color: #666;
font-style: italic;
font-weight: normal;
}
-ms-input-placeholder {
color: #666;
font-style: italic;
font-weight: normal;
}
Figura7.12:Aversãofinaldoscamposdoformulário.
Oformulárioestácompleto,como placeholderemusoeo labeldecada
campoescondido-apenasvisualmente,utilizandoCSS-deixandooformulárioocu-
parumespa çomínimo.
Temosapenasumponto,opcional,amelhorar:emnavegadoresquenãosupor-
tamousode placeholder,comoversõesdoInternetExploreranterioresa10,
nossoformulárionãoexibeapenasos2campos,semtextoalgumindicandosobreo
queelessão.
Aseguir,vamosadotarumaestratégiaparaidentificaroscasosemquenãose
temsuporteaoatributoeaindasimpodemospermitirqueosusuáriosutilizando
138


## Página 149

CasadoCódigo Capítulo7. Melhorandoosseusformulários
taisnavegadoresconsigamusaroformulárionormalmente.
DetectandofuncionalidadescomJavaScripteajustandooestilo
Paraidentificarqueonavegadoremusonãopossuisuporteao placeholder
vamosutilizarumpoucodeJavaScript,mas,emvezdetentaridentificaremqual
navegadorestamosfazendomalabarismoscomo navigator.userAgent,será
maissegurotestarseonavegadorpossuirealmentesuporteàfuncionalidadeque
precisamos.Eisoporquê:podemosescreverumcódigoespecíficoparaatendero
InternetExplorer,masissonãoatingiráversõesantigasdoMozillaFirefox,por
exemplo. Detectandoafuncionalidadeemvezdepossuirumalistadeversões
denavegadoresqueprecisamdeumacorre çãogaranteumcódigomaissimples
econciso.
Vamosescreverumtesteespecíficoparaoatributo placeholderecasovocê
precisetestaroutrasfuncionalidadesquepossamnãoexistir,talvezseránecessário
usaralgumaoutralógicaespecífica. Abiblioteca10.4 Modernizrfoicriadapara
agrupardiversostestesdefuncionalidadesdiferentesparafacilitaranossavida.Mas
nestecasovamosescreverocódigonósmesmos,porserumtestetãosimples.
function supportsPlaceholder() {
return 'placeholder' in document.createElement( 'input') &&
'placeholder' in document.createElement( 'textarea');
}
Afunçãoébemsimples:casoapropriedade placeholderexistanoselemen-
tos inpute textarea,elaretornarátrue.Casoalgumdoselementos(ouambos)
nãopossuaoatributo,elaretornará false. Otestenãoservirádenadasenãoo
utilizarmos,certo? Vamosfazeroseguinte: casoonavegador não passenoteste
(retornando falseachamadadestafun ção),vamosadicionarumaclasseaoele-
mento html(oelementoraizdapágina)para,atravésdoCSS,aplicarmosumestilo
diferenteparanavegadoressemsuporteao placeholder. UtilizandoojQuery,
bibliotecamaisusadaparatrabalharcomoDOM,ficamoscomoseguintecódigo:
jQuery(function($) {
function supportsPlaceholder() {
return 'placeholder' in document.createElement( 'input') &&
'placeholder' in document.createElement( 'textarea');
}
139


## Página 150

7.9. AplicandoCSS3embotões CasadoCódigo
if(!supportsPlaceholder()) {
$('html').addClass('no-placeholder');
}
});
Assim,onossoCSSpoderáaplicarregrasespecíficasparapáginascomaclasse
no-placeholder. Nestecasopodemosexibiro labeldecadacampoefazer
outrasmudançasnoestilodoformulário.
.no-placeholder input {
border-radius: 3px;
border-top: 1px solid #999;
}
.no-placeholder label {
display: block;
}
Figura7.13:Comoformulárioserávisualizadoemnavegadoressemsuporte.
Dessemodooformuláriosemantémfuncionalquandoonavegadorusadonão
tiversuporteaoqueprecisamos,eosnavegadoresatuaisterãoocomportamento
padrãoquedesenvolvemosanteriormente.
7.9 AplicandoCSS3 em botões
Talvezvocêtenhareparadonosexemplosanterioresquenãochegamosatrabalhar
oestilodosbotõesdosformulários.Deixeioassuntoparasertratadoemseparado
porconsiderá-loumaarteàparte.
Noscapítulosanterioresentramosemdetalhessobregradientes,sombrasebor-
das,quesãoutilizadosemconjuntoparaaprimorarovisualdebotõeselinkssema
necessidadedeseusarimagensparaisso.
140


## Página 151

CasadoCódigo Capítulo7. Melhorandoosseusformulários
Criandoumbotãocompleto
Devoltaaoformuláriodecontatoquecriamosanteriormenteeutilizandooque
aprendemossobregradientesebordasarredondadas,vamoscome çarcomumsutil
botãobranco:
button {
background-color: #E5E5E5;
background-image: linear-gradient(top, #FFF, #E5E5E5);
border: 1px solid #AAA;
border-radius: 3px;
color: #000;
font-size: 0.8em;
font-weight: bold;
padding: 5px 10px;
}
Definimosumgradienteusandobranco( #FFF)ecinza( E5E5E5),deixandoo
cinzacomocordefundocasonãoexistasuporteagradientes.Acrescentamosuma
bordaumpoucomaisescuraqueocinzadogradiente,levementearredondadae
algunstoquesdetamanhodefonteeespa çamentoparachegaraoseguinteresultado:
Figura7.14:Obotãocomgradienteebordas.
Simples,não? Éimportantenãousarcoresmuitodiferentesnogradienteou
deixarobotãograndedemaisparachamarmaisaten çãoqueosdemaiselementos
doformulário.Masaindatemostrabalhoafazernestebotão!
Paraficarmaiselegante,podemosadicionarestilosparaosestadosdeusodo
botão,usandopseudo-seletorescomoo :hovere :active,paragarantirares-
postavisualàintera çãocomoformulário.Vamoscome çarpelo :hover,alterando
ascoresdobotão.
button:hover {
background-color: #285582;
background-image: linear-gradient(top, #3775B3, #285582);
border-color: #204569;
}
141


## Página 152

7.9. AplicandoCSS3embotões CasadoCódigo
Figura7.15:Aoposicionaromouseemcimadobotão,elemudadobrancoecinza
paraoazul.
Dobrancosutilaoazul.Devidoaessainversãobrusca,acordotextodobotão
precisasermudadatambém,assim:
button:hover {
background-color: #285582;
background-image: linear-gradient(top, #3775B3, #285582);
border-color: #204569;
color: #FFF;
text-shadow: -1px -1px 0 rgba(0, 0, 0, 0.6);
}
Figura7.16:Bemmelhoracorbrancanobotãoazul,nãoacha?
Alémdemudaracorparabranco,adicionamosumasombranotextoparaajudar
naleitura-geralmentenãoprecisamosusarmaisdoque1ou2pixelsquandosetrata
de text-shadow,bastaajustarqualoângulodesejado.Ousodo rgbaaquipode
sertrocadopelacorsólida- #000-sequiser.Porúltimo,fechamosoestilodobotão
comumpardesombras:
button:hover {
background-color: #285582;
background-image: linear-gradient(top, #3775B3, #285582);
border-color: #204569;
box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3), 0 0 3px #3775B3;
color: #FFF;
text-shadow: -1px -1px 0 rgba(0, 0, 0, 0.6);
}
142


## Página 153

CasadoCódigo Capítulo7. Melhorandoosseusformulários
Figura7.17:Oestadode‘hover’finalizadocomassombras.
Apropriedade box-shadowcontémduassombrasbastantedistintas-apri-
meiraéumasombrainterna(atente-seao inset)paraclarearumpoucootopodo
botão. Asegunda,emvoltadoelemento,parademonstrarumcertobrilhoaoseu
redor.
Agora,paraoestado :active,vamosescurecer bastanteobotão,dandoailusão
deoelementoestarrealmentepressionadopelomouse.
button:active {
background-color: #204569;
background-image: none;
border-color: #1A3754;
box-shadow: inset 0 2px 1px rgba(0,0,0, 0.15);
}
Trocamosopardesombrasporumasombraescurainterna,removemosogra-
dienteazuldobotãoeescurecemosascoresdasbordasedosfundos.
Figura7.18:Oestilodobotãoquandopressionado.
Pronto,temosos3principaisestadosdonossobotãodevidamenteestilizados
combinandoaspropriedadesdegradienteesombras. Émuitofácilajustarostons
paraalgumaoutracor,comoumvermelhoouverde-simplesmentealterandoos
hexadecimaisusadosnocódigo.
Regrasbásicasparadefinirestadosdebotões
Émuitocomumverpelainternetdiversossitesqueaplicamasmaisvariadas
mudançasemestilospara :hovere :active,enemsempreoresultadoéagra-
143


## Página 154

7.9. AplicandoCSS3embotões CasadoCódigo
dável.TylerGalpin,umdesignercanadense,sugerenoseublogtrêsregrasbásicas
paraessescasos,cabendoacadaumescolherqualdastrêsseguir.
Paraocasode :hover:
1) Obotãodeveficarmaisclaro;
2) Obotãodeveficarmaisescuro;
3) Obotãodevemudardecor.
Eoestadode :active:
1) Obotãodevesemover1ou2pixelsparabaixo;
2) Obotãodeveteroseugradiente(casopresente)invertido;
3) Obotãodeveficaraindamaisescuro.
Noexemploanteriorescolhiaterceiraop çãodecadaum,masvocêpodepraticar
everosresultadosaousaralgumadasoutrasregrassugeridas.Emseublog,Tyler
tambémcomentasobreoquesedeveevitarnestescasosedáoutrasdicasimportan-
tessobrebotões-http://galp.in/blog/2011/08/02/the-ui-guide-part-1-buttons/.
Reaplicandopadrõesemoutroscenários
Noformuláriodeloginquecriamosanteriormente,podemosusarasmesmas
técnicasdobotãoanteriorparacriarumbotãoverdebastantearredondado.Vamos
começarcomCSSsimples,semutilizargradientesousombras.
button {
background-color: #6DA033;
border: 1px solid #588129;
color: white;
font-size: 0.8em;
font-weight: bold;
padding: 5px 10px;
}
Figura7.19:Umsimplesbotãocomfundoebordasverdes.
144


## Página 155

CasadoCódigo Capítulo7. Melhorandoosseusformulários
Agora,deixamosobotãoumpoucomaisinteressantecom border-radius,
text-shadowe box-shadow.
button {
background-color: #6DA033;
border-radius: 13px;
border: 1px solid #588129;
box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4);
color: white;
font-size: 0.8em;
font-weight: bold;
padding: 5px 10px;
text-shadow: -1px -1px 0 rgba(0, 0, 0, 0.6);
}
Figura7.20:Melhorandoobotãoverde.
Ovalorde 13pxparao border-radiuséporqueobotãotem 27pxdealtura
-entãousamosaproximadamentemetadedessevalor.Nãopodemosutilizar 50%
porqueessevaloririalevaremconsidera çãoalarguradoelemento,fazendocom
queeletomasseaformadeumaelipse.Assombrassãoparareal çarotexto(como
text-shadowpretoacimadotextobranco)eabordasuperior.Agora,éavezdo
gradiente.
button {
background-color: #6DA033;
background-image: linear-gradient(bottom, #6DA033 47%, #87C442 55%);
border-radius: 13px;
border: 1px solid #588129;
box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4);
color: white;
font-size: 0.8em;
font-weight: bold;
padding: 5px 10px;
text-shadow: -1px -1px 0 rgba(0, 0, 0, 0.6);
}
145


## Página 156

7.9. AplicandoCSS3embotões CasadoCódigo
Figura7.21:Nossobotãoverdecomumgradiente.
Diferentedogradienteanterior,agoravamosinformarasposi çõesdascores-
47% e 55% .Oprimeirotomdeverdesemantématé 47% daalturadogradiente,
eosegundotomcome çaapartirdos 55%. Oespaçoentreeles-os 8% restantes
-sãopreenchidoscomatransi çãodeumacorparaoutra.Paraaversãode :hover
dobotão,seguindoasindica çõescomentadasanteriormente,vamosescurecer10%
dascoresdogradienteedasbordasdobotão.
button:hover {
background-color: #618F2D;
background-image: linear-gradient(bottom, #618F2D 47%, #79B238 55%);
border-color: #4E7324;
}
Figura7.22:Oestadode‘hover’paraobotãoverde.
Eo :active? Podemosreutilizaratécnicaparaescurecerbastanteobotão
queusamosanteriormente,apenasajustandoascoresparaoverdequeestásendo
aplicadoagora.
button:active {
background-color: #618F2D;
background-image: none;
border-color: #405E1E;
box-shadow: inset 0 2px 1px rgba(0,0,0, 0.15);
}
146


## Página 157

CasadoCódigo Capítulo7. Melhorandoosseusformulários
Figura7.23:Escurecendoobotãoverdeutilizandoo‘box-shadow’.
E...pronto!Osmesmospadrões,masaplicadoscomcoresdiferenteselevesmu-
dançasdeestilo,levamaelementosagradáveisefuncionais. Apesardeusarmos
bastanteCSS3aqui,osbotõesdegradammuitobememnavegadoresquepossam
nãotersuporteasombrasougradientes.Issosedeveprincipalmenteàpresen çado
background-coloredo paddingusadoparamanterotamanhodosbotões.
147


## Página 159

Capítulo8
Efeitos101:Trabalhandocom
animaçõesetransi ções
UmadasminhaspartesfavoritasdoCSS3éaquantidadedeefeitosqueconseguimos
criarapenascomCSSnasnossaspáginascombinandoalgumaspropriedadesnovas
- transform, transitione animation. Semelas,todosessesefeitoseani-
maçõesdeencherosolhoscostumamserfeitosporbibliotecasdeJavaScriptcomoo
jQueryouoscript.aculo.us.Alémdessadependênciaadicional,problemasdeper-
formanceederenderiza çãodeelementoscostumamsurgiremnavegadoresantigos
ouaotrabalharcomelementoscomplexos.Passandoaresponsabilidadedetodoo
trabalhopesadoparaosnavegadores,conseguimosefeitosdemaiorqualidadecom
umataxamenordebugs.
Apesardosuporteexperimental,poisnomomentotodosessas3propriedades
precisamserusadascomprefixosespecíficosparacadaumdosnavegadoresqueos
suportam,diversossiteseaplicativosusamessesrecursosparaefeitossensacionais-
sendoalgunsdelesossitesdoúltimomodelodoiPhoneedoGoogleNexuseainter-


## Página 160

8.1. Transformandoelementos CasadoCódigo
facewebdoTwitter.Nãoexisterazãodetermedooureceioemusá-losemseuspro-
jetos.Vamosrepassarexemplosclássicosdeusosparaapropriedade transform,
comoadicionartransi çõesentrepropriedadesemelementosexistentes,onívelde
refinamentoquetemosemanima çõesecomoexecutartransforma çõesem3dimen-
sões.
8.1 Transformando elementos
Começamoscomtransforma çõesemduasdimensões.Apropriedade transform
aceitadiversasfun çõesdeefeitosdiferentesdefinidospelaespecifica çãodaW3C,tais
como:
1)translate:utilizadoparareposicionarumelemento,movendosuaposi çãonoeixo
XeYpelosvaloresinformados.
2) scale:utilizadapararedimensionarumelemento,aceitandovaloresreferentesao
tamanhodoelemento- scale(2)dobraráotamanhodeumelemento.
3)skew: permitedistorcerasposi çõesdeumelemento,esticandoetorcendode
acordocomosvalorespassados.
4) rotate:usadapararotacionaroângulodoselementos.
5)matrix:omaiscomplexodetodos,permiteexecutarumamatrizdetransforma-
ções.
Asfunções translate, scalee skewpossuemversões Xe Y,quepermi-
temmodificarapenasumeixoenãoambosdeumavez. Asfun çõesde skewe
rotatetrabalhamcomumanovamedida,graus,utilizandoosufixo deg,como
em transform: rotate(90deg).
Amelhorformadecompreenderousodetaisfun çõesénaprática.Vamosuti-
lizaralgumasdelasnoexemploaseguir.
8.2 Os efeitos rotate , scale, skew e translate em
uma galeria de fotos
Nocomeçode2012,aPlataformateccontratou4desenvolvedores-incluindoeu-
parareforçarasuaequipe.Emhomenagemaisso,vamoscriarumagaleriadefotos
150


## Página 161

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
paraapresentarosnovosmembrosdotime.Come çandocomumHTMLcomalista
decontratadosesuasfotos:
<h1>Reforços da Plataformatec em 2012</h1>
<ul>
<li>
<img src= 'pics/galdino.png' alt='Carlos Galdino '>
<span>Carlos Galdino</span>
</li>
<li>
<img src= 'pics/erich.png' alt='Erich Kist '>
<span>Erich Kist</span>
</li>
<li>
<img src= 'pics/lucas.png' alt='Lucas Mazza '>
<span>Lucas Mazza</span>
</li>
<li>
<img src= 'pics/rondy.png' alt='Rondy Sousa '>
<span>Rondy Sousa</span>
</li>
</ul>
EumpoucodeCSSparaalinharasfotosereal çarosnomes:
ul {
list-style: none;
padding: 0;
}
li {
float: left;
margin-left: 10px;
position: relative;
}
span {
color: #153755;
display: block;
font-weight: bold;
margin-top: 5px;
151


## Página 162

8.2. Osefeitosrotate,scale,skewetranslateemumagaleriadefotos CasadoCódigo
text-align: center;
}
Figura8.1:Agaleriacomas4fotosnolugar.
Paradarumadescontraídanagaleria,vamosgirarasfotosutilizandoafun ção
rotate. Sendoqueasfotosímpares(doCarloseaminha)irãoparaumladoe
aspares(doErichedoRondy)paraoutro.Utilizandooseletorde nth-child,o
códigoparaissoficabemenxuto:
li:nth-child(even) {
transform: rotate(5deg);
}
li:nth-child(odd) {
transform: rotate(-5deg);
}
152


## Página 163

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
Figura8.2:Afun ção‘rotate’emação,aplicadanasfotos.
Passandoumvalornegativopodemosrotacionarasimagensnosentidoanti-
horário,enquantovalorespositivossãoparaosentidohorário. Outroefeitoque
conseguimosadicionarfacilmenteéaopassarcomocursorporcimadasfotos,au-
mentarotamanhodaimagemedotexto,atravésdousodo scale.
li:hover {
transform: scale(1.3);
z-index: 1;
}
Figura8.3:Combinandoo‘hover’como‘scale’.
Destaforma,a imgeo spanirãovoltaraposi çãonormaleficarão30%maiores
-eousodo z-indexvaiposicionarafotoemcimadasdemais. Podemostestar
153


## Página 164

8.2. Osefeitosrotate,scale,skewetranslateemumagaleriadefotos CasadoCódigo
outrasfunçõescomoo skeweo translateaqui,maselasnãosãoaplica çõestão
interessantesquantoo rotateeo scalenonossocenário.Masvamosconferir
comoelasficariamnanossagaleria.
li {
transform: skew(10deg, 10deg);
}
Figura8.4:Talvezo‘skew’nãosejaomaisinteressanteparaonossocaso.
li:nth-child(even) {
transform: translateY(10px);
}
li:nth-child(odd) {
transform: translateY(-10px);
}
154


## Página 165

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
Figura8.5:Movimenteoselementoscomafun ção‘translate’.
Emcadacasoénecessárioestudarqualomelhorefeitoaserusado. O skew
podeserútilparadesenharcubosem3Dutilizando3elementos,eo translateé
umaótimaalternativaaousode position: absolutejuntode tope left.
Emnavegadoressemsuportea transform,agaleriaseriaexibidadaforma
queelafoicriadainicialmente-semefeitonenhum.Casovocêprecisetrabalharcom
navegadoressemsuporte,sempretesteassuaspáginassemosefeitosde transform
paraconfirmarqueelascontinuamfuncionais.
8.3 Transições de estilos
Apropriedade transitionpermitevocê“animar”amudança-ouseja,atran-
sição-entreoutraspropriedadesdosseuselementosquandoelasmudamdevalor,
sejaessamudan çafeitaatravésdeJavaScript,alterandoasclassesaplicadasaumele-
mento,oupelasmudan çascausadasporpseudo-seletores,como :focuse :hover.
Transiçõessãoumaótimaadi çãoainterfacesjáexistentes,jáquedependemda
mudançadeestadoexistente,como containersdeslizantesemodaisqueaparecem
edesaparecemdastelas. Sevocêestáacostumadoausaranima çõesemJavaScript
comojQuery,porexemplo,épossívelsubstituirousodefun çõescomo slideDown
e fadeToggleportransiçõesentreclassesespecíficasparamodificaraalturaoua
opacidade,tornandoessesefeitosmaisrápidosegarantindomelhorqualidade.
VamosvoltaraesseassuntodoJavaScriptmaistarde,masprimeirovamosveras
transiçõesema çãoparamelhoraraexperiênciadeinterfacesquejádesenvolvemos
anteriormente.
155


## Página 166

8.4. Transiçõesnagaleriadefotos CasadoCódigo
8.4 Transições na galeria de fotos
Vocêselembradagaleriadefotosdosrefor çosdaPlataformatecquecriamosan-
teriormenteparausarapropriedade transformcomafun ção rotate?Vamos
aprimoraroefeitode scaleadicionadoao :hoverdasfotoscomumatransi ção-
eissoseráabsurdamentesimples-bastaaplicaraseguintelinhaaoseletorda li:
li {
transition: transform 0.2s linear;
}
Abraagalerianoseunavegadorepasseomousepelasfotosnovamente.Incrível,
certo?ApenasumalinhadeCSSeganhamosessaanima ção-masessalinhacontém
bastanteinformaçãosobreoquequeremosfazer.Apropriedade transforméum
atalhoparaas4propriedadesquecompõemaanima ção,damesmaformacomo
usamos marginparadefinir4margensdiferentesemumapropriedadesó,sendo
elas:
1)transition-property:paraqualpropriedadeatransi çãoseráaplicada.Épossível
utilizarovalor allparareferenciartodasaspropriedadesdoelemento;
2) transition-duration:Adura çãoqueatransi çãodeveter,emsegundos;
3)transition-timing-function:Comoavelocidadedatransi çãodeverásercalcu-
lada,osvaloresmaiscomunssão linear, ease, ease-in, ease-oute
ease-in-out;
4) transition-delay:tempodeesperaqueprecedeatransi ção-geralmenteomiti-
mosessapropriedadeparautilizarovalorpadrãodela,0.
Comissoexplicado,ficafácilentenderoqueanossadefini çãofaz:aplicamosa
transiçãocomapropriedade transform,com 0.2sdeduraçãoedeveráserexe-
cutadaemumavelocidade linear.Apesardeexistirummardeop çõespossíveis
queconseguimoscombinarcomessaspropriedades,éfácildefinirumpadrãodeva-
loresparaadura çãoeavelocidade,erepetirosvaloresemdiversoslugareseprojetos
-melhordoquesepreocuparconstantementeemotimizarastransi çõesparacada
usopossível.
156


## Página 167

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
Revisitandoumvelhoamigo
Vamosvoltaraoformuláriodecontatocriadonocapítuloanterior-emqueas
mensagensdeajudasãoexibidasconformeoscamposrecebemfoco-eadicionar
transiçõesàsmensagens. Diferentedoexemploanterior,precisamosfazeralguns
ajustesaoestilodoformulárioepodemoscombinartransi çõesdiferentesparacriar
umefeitomelhor.
Figura8.6:Oformuláriodecontatocriadonocapítuloanterior.
Primeiramente,precisamostrocaradefini çãode display: none;dasmen-
sagens-nãopodemosusaressapropriedadenasnossasanima ções,poiselemen-
tosqueestãoescondidosdessaformanãorecebemosefeitosdetransi çãoquando
mudamosseuvalorpara block.Paracontornarisso,precisamosesconderasmen-
sagensdeoutramaneira,utilizandoapropriedade opacity.Então,oCSSdaclasse
.hintficaráassim:
.hint {
background-color: #FFFBE4;
border-radius: 3px;
border: 1px solid #CCC;
box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
display: inline-block; /* Colocamos o `inline-block` de volta. */
font-size: 0.8em;
margin-left: 20px;
opacity: 0; /* Remove a opacidade do elemento para escondê-lo. */
padding: 3px;
157


## Página 168

8.4. Transiçõesnagaleriadefotos CasadoCódigo
}
Noseletorparaasmensagensquesãoexibidasnoestadode :focusdoscampos,
vamosalteraraopacidadedoelementoparaexibi-locorretamente:
input:focus + .hint, textarea:focus + .hint {
opacity: 1;
}
Alteramosaformaqueescondemoseexibimosamensagem.Agoraénecessário
adicionaradefini çãodatransi çãoaserusada.
.hint {
transition: opacity 0.5s;
}
Figura8.7:Atransi çãodeopacidadesendoaplicadaamensagem.
Umatransiçãodemeiosegundo,linear,napropriedade opacity. Testeno-
vamenteaexibi çãodasmensagensevejaatransi çãoema ção.Masaindapodemos
incrementá-la,adicionandoamargemlateralnajogada.Vamosmoveradefini çãode
margin-leftdaclasse .hintparaoseletorde :focus,deixandooCSSassim:
input:focus + .hint, textarea:focus + .hint {
margin-left: 20px;
opacity: 1;
}
158


## Página 169

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
Agora,alémdo opacity,apropriedade margin-lefttambémsofrerámu-
danças,eprecisamosadicionarumadefini çãode transitionparaela:
.hint {
transition: opacity 0.5s, margin-left 0.5s;
}
Ou,utilizandooatalhodo all,definindoapenasumapropriedadeeumadu-
ração.
.hint {
transition: all 0.5s;
}
Figura8.8:Ambaspropriedadessendo‘animadas’pelatransiçãocriada.
Testandonovamenteoformulário,podemosveranovaversãodanossatran-
sição,cujainten çãoédemonstrarqueamensagemestá“entrando”nainterfacedo
usuário,esaindoquandooutrocamporecebefoco.Apesardasmudan çasnecessárias
nocódigoescritoanteriormente,conseguimosadicionarastransi çõesnoformulário
semperderocomportamentoantigo.
159


## Página 170

8.5. Umdetalheimportantesobretransi çõeseJavaScript CasadoCódigo
8.5 Um detalhe importante sobre transições e Ja-
v aScript
Sevocêpretendesubstituirasanima çõesviaJavaScriptportransi çõesutilizando
CSS,precisolhefalarduascoisas: Primeiro,essaéumaótimaideia,esegundo,
vocêprecisaaprendermaisumtruqueparatercontrolesobreasequênciadecoi-
sasquesãoexecutadas.ViaJavaScript,geralmente,podemosdefinirumafun çãode
callbackparaquandoaanima çãoterminar,podendoencadearanima ções,mudar
oconteúdodeelementosemais-mascomofazerissoquandoseusatransi ções?
Para isso, existe um novo evento disponível via JavaScript chamado
transitionend. Ele será disparado quando a transição de uma propriedade
foifinalizada.AssimcomonoCSS,emqueprecisamosutilizarumprefixoespecí-
ficocomo -moz-, -webkit-e -o,cadanavegador,nomomento,possuiumnome
específicoparaoeventode transitionend: paraoSafarieoGoogleChrome,
baseadosno WebKit, é precisousaronome webkitTransitionEnd, parao
Opera oTransitionEndeparaoInternetExplorer10onomeaserutilizado
éMSTransitionEnd. AsúltimasversõesdoMozillaFirefoxjáutilizamonome
transitionend,apesardanecessidadedeseusaroprefixonoCSS.
Umexemplorápidodisso:digamosquevocêquerexecutarumcódigoespecífico
apósremoveraopacidadedoseuelemento #popup.Umcódigoqueprovavelmente
seriaescritousandoasfun çõesdojQuerydessaforma:
$('#popup').fadeOut(function() {
// o '#popup' já está com opacidade 0;
});
Podeserescritoassim,utilizandoo transitionendemumnavegadorbase-
adonoWebKit,eumaclasse .hiddenquealteraaopacidade:
$('#popup').on('webkitTransitionEnd', function() {
// A transição do '#popup' foi finalizada.
})
$('#popup').addClass('hidden');
160


## Página 171

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
8.6 Transformações em 3D
Asfunçõesde transformem2Dsãointeressantes,masnãosecomparamaosefei-
toscriadospelasfun çõesdetrêsdimensões.Capazesdeusartodoopoderderen-
derizaçãodosnavegadores,comessasfun çõespodemoscriarefeitossimilaresaode
aplicaçõesnativasdoWindowsoudoOSX.
Algumasdasnovasfun çõesdisponíveis:
1)translateZ,queassimcomoseussimilares translateXe translateY,per-
miteareposi çãodoselementosdentrodeumeixoespecífico;
2) rotateX,rotateYpodemserusadaspararotacionaroselementosnoseixosver-
ticaisehorizontais;
3)perspective,quedeixapossívelmanipularaperspectivadoselementosemmeio
astransformações;
4) matrix3d,translate3derotate3d,versõesmelhoradasdefun çõesquevimosan-
teriormente,agoracomsuportea3D.
Alémdasfun çõesnovas,umanovapropriedadefoiadicionadaparamanipu-
laroefeitodatransforma çãoquandoaplicadaaelementoscomoutroselementos
dentrodele, o transform-style. Porpadrão, oselementosfilhosnãocom-
partilhamdoefeito3Dexistentenoelementoqueoscontém-oquelevaaum
comportamentoinesperadodoposicionamento.Podemosmudarissoutilizandoo
transform-stylecomovalor preserve-3d,aplicandoosefeitosaoselementos
internosdoqueestásendotransformado.
Apesardosuporteescassodenavegadores,existemcenáriosondeutilizarefeitos
em3Dsãoumaótimaferramentaparamelhoraraintera çãodosseusprojetoserou-
barelogiospelabelezadosefeitos.Páginasvoltadasparadispositivosmóveisoucuja
audiênciamajoritáriautilizanavegadoresatualizados-comooFirefoxeoChrome
-sãoótimaspedidas.Aconselhoisso,poisalternativasaosefeitosparanavegadores
semsuporteprovavelmentevãorequerermudan çasmaioresnasuainterfacepara
permitirousoemcasosemquenãohásuporteàsfun çõesde3D.
8.7 Girar formulários com apenas um clique
Vamostransitarentredoisformuláriosutilizandoanima ções3D-geralmentevemos
issosendofeitocomefeitosmaissimples,masotrabalhoextraparachegarnoque
161


## Página 172

8.7. Girarformulárioscomapenasumclique CasadoCódigo
vamoscriarnãoétãograndequantosepodeimaginar.Come çamoscomocódigo
paraosformulários.
Primeiro,umformuláriodecadastrotradicional:
<section class= 'signup'>
<form>
<h2>Cadastre-se agora!</h2>
<p>
<label for="account_email">E-mail</label>
<input type= 'email' id="account_email">
</p>
<p>
<label for="account_password">Senha</label>
<input type= 'password' id="account_password">
</p>
<p>
<label for="account_password_confirmation">
Confirme a sua senha
</label>
<input type= 'password' id="account_password_confirmation">
</p>
<p><button>Enviar!</button></p>
<a href= 'javascript:;' class='toggle'>Já estou cadastrado no site</a>
</form>
</section>
Eumformulárioparalogin:
<section class= 'signin'>
<form>
<h2>Entrar no site</h2>
<p>
<label for="user_email">E-mail</label>
<input type= 'email' id="user_email">
</p>
<p>
<label for="user_password">Senha</label>
<input type= 'password' id="user_password">
</p>
<p>
<button>Enviar!</button>
</p>
162


## Página 173

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
<a href= 'javascript:;' class='toggle'>Quero me cadastrar</a>
</form>
</section>
Juntodeles,umpoucodeCSS(devidamenteinspiradoemexemplosanteriores)
paraadicionarestiloaoscamposeposicionartodososelementos:
form {
font-size: 0.8em;
padding: 10px;
}
label {
display: block;
font-weight: bold;
}
input {
border: 1px solid #CCC;
box-shadow: inset 2px 2px 2px #EEE;
font-size: 0.9em;
padding: 2px 5px;
}
163


## Página 174

8.7. Girarformulárioscomapenasumclique CasadoCódigo
Figura8.9:Oformuláriodecadastroeodelogin.
Nadamuitodiferentedoquenosjávimosanteriormente,certo? Oslinksde
“Queromecadastrar”eJá estou cadastrado no siteserãoutilizadospara
transitarentreosformulários,comumaleveajudadeJavaScriptedojQuery.Agora,
vamoscolocarosnossosformuláriosdentrode2elementos-podemparecerdesne-
cessários,maselesterãoumpapelimportanteacumprir.
<div class= 'container'>
<div class= 'card'>
<!-- As seções de 'login' e 'signup' vão aqui... -->
</div>
</div>
Eclaro,umpoucodeCSSparaesseselementos.
.container {
height: 300px;
164


## Página 175

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
position: relative;
width: 200px;
}
.card {
border-radius: 5px;
border: 1px solid #CCC;
height: 100%;
position: absolute;
width: 100%;
}
.card section {
background-color: #FFF;
border-radius: 5px;
position: absolute;
}
Figura8.10:Asse çõesdevidamenteposicionadasumaemcimadaoutra.
Definimosoelementoquevaiconterasse çõeseseusformulários,posiciona-
dasexatamenteumaemcimadaoutra. Parapoder“girar”osformuláriosdeum
165


## Página 176

8.7. Girarformulárioscomapenasumclique CasadoCódigo
ladoparaoutro,precisamoscolocarumdelesdecostas,certo?Então,vamosusaro
rotateY!
.signup {
transform: rotateY(180deg);
}
Figura8.11:Podemosveroformuláriodecadastroinvertidoaofundo.
Feito!Masoformulárioapareceinvertidonofundo,oquepodedeixarascoisas
bastanteestranhas.Entãoprecisamosesconderas“costas”doformulário,atualizado
umdosseletoresquecriamosanteriormente:
.card section {
backface-visibility: hidden;
background-color: #FFF;
border-radius: 5px;
position: absolute;
}
166


## Página 177

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
Figura8.12:Como‘backface-visibility’emação,ase çãodecadastronãoaparece.
Comapropriedade backface-visibilitydefinidacomo hidden,ascostas
doselementos(nonossocaso,dasse ções .signupe .signin)ficaraminvisíveis.
Oqueprecisamosagoraémudardeumformulárioparaoutro,utilizandoumpeda ço
decódigoJavaScript,utilizandoojQuery:
jQuery(function($) {
$('section').on('click', 'a', function() {
$('.card').toggleClass('flipped');
})
});
Todavezquealgumlinkdentrodeuma sectionforclicado,umdos contai-
nersqueforamadicionadosanteriormente-a div .card -iráreceberaclasse
flipped,ouiráperderessaclassecasoelaestejapresente.Masnãoadicionamoso
CSSespecíficodela-queserábemsimples:
.card.flipped {
transform: rotateY(180deg);
}
Assim,todooelementoserárotacionadoporinteiro-entãooformulárioque
estavadecostasficarádefrente,eoqueestavanafrenteficaráparatrás.Sevocêtestar
167


## Página 178

8.7. Girarformulárioscomapenasumclique CasadoCódigo
issoetentarvoltarparaoformuláriodelogin,veráquenãoconseguimosclicarnos
elementosdoformuláriodecadastro.Issoporquea div .cardnãoestánomesmo
espaçodasse çõesdosformulários-ocasodo transform-stylequecomentei
anteriormente. Bastacorrigirepodemostransitardeumformulárioparaoutroà
vontade.
.card {
border-radius: 5px;
border: 1px solid #CCC;
height: 100%;
position: absolute;
transform-style: preserve-3d;
width: 100%;
}
Figura8.13:Agoraconseguimoschegarnoformuláriodecadastro.
Pronto-conseguimosmudardeumformulárioaoutro,masnãotemosanima-
çãonenhuma-horadeumatransi çãoentraremjogo,paraoelemento .card.Uma
transiçãodeumsegundoéosuficienteparaonossoexemplo.
.card {
border-radius: 5px;
168


## Página 179

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
border: 1px solid #CCC;
height: 100%;
position: absolute;
transform-style: preserve-3d;
transition: transform 1s;
width: 100%;
}
Agoraestamoschegandoaalgointeressante,masaindanãoajustamosumponto
importantedousode3D-aperspectiva. Nãoexisteaquelaideiadeprofundidade
edequeoselementosestãogirandoemapenasumeixodentrodoespa çodefinido.
Paradeterminara“profundidade”dasnossaspáginas,precisamosutilizaraproprie-
dade perspective.Comooselementosqueestãosendoutilizadosestãorelativos
aonosso .container,énoCSSnelequedevemosdefiniraprofundidadedonosso
plano.
.container {
height: 300px;
perspective: 500px;
position: relative;
width: 200px;
}
Figura8.14:Aanima çãofinal,comoefeitodeperspectiva.
500pxéumvalordepraxeparaessecenário.Éfácilnotaradiferen çaqueisso
fezparaoefeitoquecriamos-conseguimosnotarosformuláriosgirandonailusão
169


## Página 180

8.8. Utilizandoanimações CasadoCódigo
deprofundidadequecriamosviaCSS.Sequisermudarosentidodaanima ção,basta
trocarousodo rotateYpor rotateX,eosformuláriosirãogirarnahorizontal.
8.8 Utilizando animações
Agoraquejávimossobre transforme transitioneconseguimoscriaral-
gunsefeitosinteressantescomeles,porquesepreocuparemversobreapropri-
edade animation? Apropriedade animationconsegueiralémdastransfor-
maçõesetransi çõesepermiteumcontrolemaiorsobreaexecu çãodasanima ções,
repetiçõeseatéadiarosefeitosporalgunssegundos. Hádiversasop çõesdecon-
figuração,comoo animation-delayparaumtempodeesperaantesdaanima-
ção,o animation-play-stateparadefinirseaanima çãoestásendoexecutada
ounãoeo animation-iteration-countparadefinirquantasvezeseladeve
serexecutada. Alémdisso,podemosdefinirdiversospontosdequebranosefei-
tosquequeremosfazer,enãoapenasoinícioefimcomofazemoscomastransi-
ções. Oquepermitetodaessaflexibilidadeéadefini çãodessasregrasutilizando
@keyframes,naqualdefinimospropriedadesempontosespecíficosdasanima-
ções,utilizandoporcentagens.Vamoscolocaramãonamassaeentendermelhoro
usodos @keyframes.
8.9 C omeçando com keyframes
Nossaprimeiraanima çãoseráfazerumaentradadignadecinemaparaumtítuloda
suapágina.Paraissosóvamosprecisardeum h1.
<h1>Bem vindo!</h1>
Eclaro,jogarumpoucodeCSSemcimaparaacompanhar.
h1 {
color: #000;
font-size: 1.4em;
text-align: center;
}
Umcomeçobastantesimples.Agoravamosadicionaraanima ção,queirátra-
balharaopacidadeeotamanhodoelemento,utilizando transform.
h1 {
animation: appear 2s 0 linear;
170


## Página 181

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
color: #000;
font-size: 1.4em;
text-align: center;
}
Assimcomoo transformeo transitionsãoutilizadoscomoatalhos
para definir várias opções de uma vez só, oanimationpode compor diver-
sos valores. No nosso caso, estamos utilizando a animação chamadaappear(
animation-name),com2segundosdedura ção( animation-duration),aser
executadaimediatamente(como animation-delayem0)ecomumprogresso
linear( animation-timing-function). Masemnenhummomentodefinimos
doqueécompostaessaanima ção.Precisamosdefinirumgrupoderegrasparaela
utilizandoumase çãode @keyframes,assim:
@keyframes appear {
0% {
opacity: 0;
transform: scale(2);
}
70% {
opacity: 1;
transform: scale(1);
}
100% {
transform: scale(1.2);
}
}
Dentrodase çãode @keyframes,épossíveldefinirpeda çosdeCSSqueserão
aplicadosemumpontoespecíficodaanima çãofazendoreferênciaàporcentagem
doprogresso-jáqueadura çãoemsiédefinidaemoutroponto.Atransi çãodeum
pontoeoutroseráfeitadamesmaformaqueastransi çõessãoexecutadas,utilizando
afunçãodeprogressodo animation-timing-function.
Aqui,estamoscome çandoaanima çãocomoelementocomseutamanhodo-
brado(usandoo scale)esemopacidadenenhuma,aos70%daanima ção(com
anossaanima çãode2segundos,issoseriaaos1.4s)oelementodeveterasuaopa-
cidadenormalizadaeotamanhoregular,eaanima çãoseráfinalizada(aocomple-
taros2segundos)comoelementoemumaescalade1.2.Apósisso,qualquermu-
dançapresentenaanima çãoirádesaparecereoelementovoltaráaonormal. Para
171


## Página 182

8.9. Começandocomkeyframes CasadoCódigo
isso,vamoslevaradefini çãode scale(1.2)paraoestilodo h1eadicionarum
transform-originparacentralizaroefeitodeescala.
h1 {
animation: appear 2s 0 linear;
color: #000;
font-size: 1.4em;
text-align: center;
transform: scale(1.2);
transform-origin: 50% 50%;
}
Figura8.15:Os3momentosdaanima çãodonosso‘h1’.
Comocontrolesobrediversospontosdasanima çõesedasdiversasop ções
de configuração, conseguimos criar efeitos que não são possíveis apenas com
transitione transform,apesardanecessidadedeescreverumnúmeromaior
delinhasdependendodoresultadodesejado.
Animaçõesinfinitas
Vocêprovavelmentejáviuouniversodegifsanimadosquesãoutilizadospara
informarquandoalgumprocessamentoestáfeitopordebaixodospanosequede-
vemosesperarapáginacarregaralgonovoemalgummomento-oschamados lo-
aders. Euficomuitofelizemsaberquenãoprecisamosmaisdeimagensassime
172


## Página 183

CasadoCódigo Capítulo8. Efeitos101:Trabalhandocomanima çõesetransi ções
podemosutilizarapenasCSS(etalvezumpoucodeJavaScript),parareplicaresse
componenteeconseguirmudartamanhosecorescomapenasalgumaslinhasdecó-
digo. Casovocênãoacreditenisso,vamoscriarumaversãosimplesdeumdesses
componentes.
Primeiro,precisamosapenasdeum span,jáqueonossoexemploserábastante
minimalista.
<span class= 'loading' title='Carregando...'>Carregando...</span>
.loading {
background-color: #666;
border-radius: 50%;
font: 0/0 serif;
position: absolute;
}
Definimosumfundoescuro,bordasredondasosuficienteparagarantirqueo
elementoapareçacomoumcírculo,eumafontezeradaparaesconderotextodo
span-Maseotamanho? Eosefeitos? Tudoissoiránanossaanima ção,comas
regrasabaixo:
@keyframes pulse {
0% {
width: 0;
height: 0;
opacity: 1;
top: 50px;
left: 50px;
}
100% {
width: 30px;
height: 30px;
opacity: 0;
top: 35px;
left: 35px;
}
}
Enquantoanossaesferavaiaumentandodetamanho-de0a35 px-elavai
sendoapagadapelamudan çadeopacidade.Asmudan çasde tope leftgarantem
queelaficarácentralizadanoseulugarenãoirásemoverporaídevidoamudan çade
173


## Página 184

8.9. Começandocomkeyframes CasadoCódigo
tamanho.Parautilizaressaanima çãopulsenonossoloadercomoefeitodesejado,
precisamosdefinirqueeleseráanimado para sempre.
Sim, para sempre.Assim:
.loading {
animation: pulse 1.5s infinite;
background-color: #666;
border-radius: 50%;
font: 0/0 serif;
position: absolute;
}
Figura8.16:Aanima çãoinfinitadonosso‘loader’.
Podemos usar infinite como um valor para o
animation-iteration-count, e a animação será executada para sempre -
podemosapenasadicionarumpoucodeJavaScriptparaescondereexibiroloader
quandofornecessário. Casosejanecessáriomudaracorouaumentarotamanho
paraadequarainterfacesdiferentes,sóprecisamosalteraralgumaslinhasdeCSS,
semnecessidadedecriarimagensnovasemumeditoreexecutarmaisrequisi ções
HTTPparaservi-las.
174


## Página 185

Capítulo9
Ouniversoforadosdesktopse
notebooks
Apopularizaçãoeevolu çãodos smartphonese tabletsnosúltimos4anosteveum
grandeimpactonastecnologiasenaformacomquedesenvolvemososnossospro-
jetosparaaweb.
Garantirumaexperiênciaadequadaparaonúmerocrescentedeusuáriosque
utilizamessesdispositivossetornouumavantagemcomercialeumdiferencialpara
produtos,empresasedesenvolvedores-ninguémdesejaexcluirumgrupodeusuá-
riosdevidoaotipodeequipamentoqueelesutilizamparaacessaraweb.
Paraentrarnestemundoeabra çaraondado mobile,éprecisoumaevolu ção
tantotécnica-mudan çasdeferramentasetecnologiasutilizadas-quantomental-
oseuprocessodedesenvolvimentoprecisaseadequaraestecenário.


## Página 186

9.1. Oqueé“ResponsiveWebDesign”eporquêvocêdevesepreocupar CasadoCódigo
9.1 O que é“ResponsiveWebDesign”e porquê você
deve se preocupar
EthanMarcottecriouotermo ResponsiveWebDesign emumartigoescritonosite
A List Apart[5],queentãosetornouumlivroqueéreferêncianoassunto:combina-
çãodeelementosfluídos,comdimensõesrelativasaoespa çodisponívelnoaparelho
dousuário,eregrasespecíficasparadefinirestilosespecíficosparatamanhosdetela
diferentesefuncionalidadesvariadas(como,porexemplo,aresolu çãofantásticado
iPhone4edoiPadde3ªgera ção).
Sitesresponsivosadequamosseuselementoseoseucomportamentoparacená-
rios,comodisponibilizandofluxodenavega çãoqueseadequaráaotamanhodatela
utilizadaoumudandoasintera çõesdousuáriocasoeleuseumdispositivosensível
atoqueounão.Alémdeprecisaridentificarotamanho,capacidadeefuncionalida-
desdisponíveis,éimportantequeadisposi çãodoselementossejaflexívelobastante
paraseadequaraqualquerdispositivo.
Oprimeiropassoparasecome çaratrabalharcomdesignsresponsivoséfazera
transiçãodeelementosfixos-dedimensõesfixadasem px-paraelementosfluídos
-quesebaseiamemporcentagense em. Destaforma,asuapáginaconseguese
expandiroudiminuirdeacordocomalarguradisponível,emvezdesefixaremalgo
similara 960pxdelarguramáxima.
Aconversãodetamanhosfixosparafluídoséfeitacombaseemumafórmula
bastante simples: "tamanho fixo"/ "contexto"= "tamanho fluído".
Comelavocêconsegueconverterdimensõesem pxparaporcentagens(paralar-
guras)ou em(parafontes),assim:
body {
/* Utilizando o tamanho de fonte padrão, geralmente 16px */
font: normal 100% Helvetica, Arial, sans-serif;
}
h1 {
font-size: 1.5em; /* 24px / 16px = 1.5em */
}
Aprincípio,estadefini çãoteráomesmoefeitoquedefinirotamanhodafonte
do h1como 24px.Porém,emdispositivosemqueotamanhopadrãodefonteseja
diferente,comoem smartphones, font-sizedoelementoiráacompanharessa
176


## Página 187

CasadoCódigo Capítulo9. Ouniversoforadosdesktopsenotebooks
mudança:emumdispositivoqueutilize 12pxafontedoelementoterá 18pxde
altura,enão 24px.
Essamesmaabordagempodeserusadaparadefinirasregrasdoseugrid-
tornando-oumgridfluído-eoespa çamentoentreelementos. Destaformavocê
conseguefazerosseuslayoutsacompanharemasdiferen çasdelarguraentrediversos
dispositivos,eentãovocêpodetrataraspeculiaridadesdecadacontextoutilizando
media queries.
9.2 O funcionamento dos media queries
Outraferramentado Responsive Web Designsãoos media queries-umaregraespe-
cíficaparaaplicarumblocodeCSScasoaregrasejaatendida.SimilaraousodeCSS
paraestilosespecíficosdeimpressão(se ção4.8),vocêtambémpodeindicarregras
associadasaotamanho,orienta çãoouaresolu çãodetela.
@media only screen
and (min-device-width : 320px)
and (max-device-width : 480px) {
/*
Esta regra será aplicada em
aparelhos com uma largura de 320px a 480px,
o que atende a maioria de smartphones.
*/
}
@media only screen
and (min-device-width : 768px)
and (max-device-width : 1024px)
and (orientation : landscape) {
/*
Além de verificar a largura do dispositivo,
você pode conferir a orientação, utilizando
"landscape" ou "portrait".
*/
}
Utilizando media queries,vocêpodedefinirestilosespecíficosparatamanhosdi-
ferentes,oqueémelhordoquefocaremumsótipodedispositivo.Diversosmode-
losde smartphonespodemseratendidosporummesmo media query,oquetambém
ajudaaatendernovosmodelosqueirãosurgirnofuturo.
177


## Página 188

9.3. Nãoéumaquestãodeaparelhos CasadoCódigo
DamesmaformaqueumCSSdeimpressão,vocêpodesobrescreverdefini ções
globaisdeCSSparaadequarasuapáginaparatamanhosdiferentes. Assimvocê
conseguereordenarelementos,reduzirotamanhodeimagensouexibirelementos
alternativosparamelhoraraexperiênciadeusodosseususuários.
Figura9.1:UmexemplodositedaPlataformatec(http://plataformatec.com.br):a
seçãodefotosmudadetrêscolunasparaapenasumacolunaquandoalargurada
páginaéreduzida.
Osite Media Queries(http://mediaqueri.es/)possuiumacoletâneadesitesque
possuemdiversosformatospara smartphonese tablets,umaótimareferênciaparase
inspirarcomoutrostrabalhos.
9.3 Não é uma questão de aparelhos
Vocêpodeconsiderarquetodaestaaten çãoserveparaadequarosseusprojetospara
diversosdispositivoscomooúltimoiPadouos smartphonesdoGoogle,masesta
filosofiaseaplicaparaomundode notebookse desktopsqueestamostãoacostumados
aver.
178


## Página 189

CasadoCódigo Capítulo9. Ouniversoforadosdesktopsenotebooks
Comdiversasresolu çõesdiferentesporaí,indode11”até27”,eainclusãodoRe-
tina displaynaterceiragera çãodalinhadoMacBookPro,épossívelrefinaraexperi-
ênciadeusoparatirarproveitodaabundânciadepixelsoudaqualidadedaresolu ção
dousuário.Bastapossuirumgrupodeestilosparalargurasacimade 1824px,por
exemplo:
@media only screen and (min-width : 1824px) {
/*
Aqui você pode adicionar estilos para se aproveitar
de uma tela maior: aumentando fontes, ícones, e
largura dos seus elementos
*/
}
9.4 Por um futuro melhor
Amudançadawebparaestesdiversosdispositivoseformasdeusosóestácome-
çando:ofuturoaindaguardaumuniversodeaparelhosnovos,tecnologiasemu-
dançasnaformaemquenosconectamospelaweb,eaindústriadainternetainda
precisaevoluirparaacompanhá-las.
Nósnãopodemospreveroqueviráporaí,maspodemosnosprepararparaseja
láoqueofuturonosreserva.
Em2011foicriadoo Future Friendy[4],ummanifestoassinadopordiversasfi-
gurascarimbadasdomundododesenvolvimentoweb.Láexistem3princípiosque
podemosseguir:
• Vocêdevecompreendereabraçaraimprevisibilidade;
• Penseecomporte-sedeumaformaamigávelparaofuturo;
• Ajudeosoutrosafazeromesmo.
Omanifestoindicaquesedevefocarnoconteúdoqueestáemsuasmãos-o
querealmenteimportaparaosseususuárioseosseusclientes-buscandoservi-lo
daformamaisflexívelpossível,oquefacilitaainclusãodenovosformatoseapare-
lhosquesurgiremcomopassardotempo,semdeixardetirarproveitodeaspectos
específicosparaproverumaexperiênciaadequada.
Todosqueremosqueonossotrabalhodureporanos,eparaalcan çarissopreci-
samostrabalharparaqueasnossascria çõessobrevivamàsmudan çasdetecnologia.
179


## Página 190

9.4. Porumfuturomelhor CasadoCódigo
Imagineterquereescreversitesinteirosdaquia2ou3anosporqueaversãoatual
nãoéadequadaparaocenárioatualdedispositivosecasosdeuso?
180


## Página 191

Capítulo10
Ferramentas-Frameworks,Plugins
ePré-processadores
Atéagora,vimosváriosrecursosinteressantesdeCSS3eHTML5paraquepossa-
moscriarsiteseaplica çõescomvisuaiselegantes.Porém,muitasdasvezes,precisa-
moscriarosestilosdozero,pensarnascoresdosbotões,nasdivisõesdecolunasdo
página,noestilodastabelasouatémesmocoisasquepodemsermaistrabalhosas,
comocuidarparaqueapáginafuncioneembrowsersmaisantigos,quenãopossuam
osnovosrecursosdeCSS3eHTML5.
Paranosajudarnessassitua ções,temosdisponíveldiversasferramentas,como
oTwitterBootstrap,HTML5Boilerplate,-prefix-freeentreoutras.Saberoquecada
umanosofereceémuitoimportante,assimpodemosescolherqualferramentame-
lhorseencaixacomoprojetoqueestásendodesenvolvido.


## Página 192

10.1. TwitterBootstrap CasadoCódigo
10.1 Twitter Bootstrap
UmdosprojetosdemaiorsucessonoGitHub,oTwitterBootstrapéumtoolkitcri-
adopordesignersdoTwittereadotadopordiversasempresaseequipesparaacelerar
oiníciodeprojetosporjáincluirdiversoscomponentesefacilidadesdeCSS,HTML
eJavaScript.Oprojetoincluiumgridfluído(sobreoqualvocêdeveterlidoarespeito
naseção6.7),diversosbotõesecamposdeformulários,abasdenavega ção,plugins
emJavaScriptemuitomais.
OprojetoédesenvolvidousandoLESS,umpré-processadordeCSSquefacilita
aescritadetodooCSSdoBootstrap,masvocêpodebaixaroarquivoCSSfinale
utilizá-loemqualquerdeseusprojetos.
VocêpodeusaroestilopadrãodoTwitterBootstrapsemprecisarescreverne-
nhumalinhadeCSS-apenasutilizandooHTMLeasclassesqueadocumenta ção
doprojetoindica.Depoisdisso,bastasobrescreveroquefornecessárioparaadequar
ovisualàsnecessidadesdoseuprojeto,comocores,tamanhos,bordasetc.
OBootstrapéumaótimapedidaparadesenvolvedoresquenãopossuemtanto
conhecimento(outempoparadedicar)emdesigneCSS.Seoquesitooriginalidade
forimportanteparavocê,dediqueumtempoparapersonalizarovisualdoBootstrap
paraoseuprojeto.Todaadocumenta çãoeexemplospodemserencontradosnosite
http://twitter.github.com/bootstrap/.
182


## Página 193

CasadoCódigo Capítulo10. Ferramentas-Frameworks,PluginsePré-processadores
Comosucessodoprojeto,algumasalternativassurgiramcomotempo,dispo-
nibilizandosoluçõessimilaresparaosmesmoscasosdeusodoBootstrap:
• Foundation,feitopelaZURB-ToolkitsimilaraoBootstrapcriadoporuma
empresacommaisde10anosdeexperiêncianoramodewebdesign-http:
//foundation.zurb.com/.
• HTMLKickstart,criadoporJoshuaGatcke-http://www.99lime.com/.
• Skeleton-umtoolkitminimalista,quepossuiumgridresponsivoealguns
componentessimples,comobotõeseabas.-http://getskeleton.com/.
Valeapenabaixarcadaumdessesframeworks,testarosseuscomponentes,grids
efuncionalidadesparadescobrirsealgumdelesseencaixamaiscomseugostoou
atémesmosevocêpreferecriartodooCSSporsipróprio.
10.2 HTML5B oilerplate
EnquantoframeworkscomooBootstrapeoFoundationpossuemdiversoscompo-
nentescomogrids,botõesusandogradientes,sombraseoutrasnovidadesdoCSS3,o
HTML5Boilerplate,quenãoéexatamenteumframework,segueporoutrocaminho:
umtemplatesimples,construídoemcimadeboaspráticasparagarantircompatibi-
lidadeeperformance.
OHTML5BoilerplateusaoNormalize.css(quevimosnase ção4.1)comoreset
básico,classesutilitáriasadicionais(paracorrigirfloatsesubstitui çãodeimagens,
porexemplo),jQuerydisponibilizadopeloCDNdoGoogleemais.Apesardenão
disponibilizarnenhumcomponentegráfico,eleéumabasesólidaparacome çarum
projetonovo.
183


## Página 194

10.3. PluginsemJavaScript CasadoCódigo
CDN?
UmCDN- Content delivery network-éumaredededistri-
buiçãodearquivoscomoobjetivodeservirconteúdocontandocomalta
disponibilidadeeperformance,comservidoresestrategicamentelocali-
zadosaoredordomundo,sendoumaótimasolu çãoparaservirarquivos
estáticoscomoimagens,scriptsevídeos.
OCDNdoGoogleéfamosopordisponibilizarasprincipaisbiblio-
tecasdeJavaScriptusadasatualmente,comoojQuery,oMooToolseo
Prototype.Alémdisso,épossívelcontratarainfraestruturadeempresas
comoaAmazoneAkamaiparaservirseusprópriosarquivos.
Vejaocódigo,maisdetalhesetutoriaissobrecomoaproveitaroprojetoaomá-
ximonositehttp://html5boilerplate.com/.
10.3 Plugins em Jav aScript
ÀsvezesapenasHTMLeCSSnãosãoosuficiente,poisnomeiodeincompatibili-
dadecomnavegadoreseAPIsnovasquenãoforamimplementadasporcompleto,é
possívelpreencheressaslacunascomJavaScriptouidentificaroqueopodemosou
nãofazercomumnavegadorespecíficousandoJavaScriptparaanalisaro User Agent
outestandoasAPIsdisponíveis.
10.4 Modernizr
Modernizréumabibliotecaquepermiteidentificaroqueésuportadoeoquenãoé
suportadononavegadordosnossosusuárioseadequaraexperiênciadoseusitepara
isso,sejaviaCSSouJavaScript.Porexemplo,identificarosuporteatag <audio>
eaqualformatosedeveusar,como ogg, mp3ou m4a.Ou,paranavegadoresque
nãosuportamanima çõesetransforma ções,aplicarumestiloalternativoparaqueo
seulayoutcontinuefuncionalparaseususuários.
OModernizrpermiteduasabordagens:aprimeiraéatravésdaadi çãodeclas-
sesaoelemento html,identificandoasfuncionalidadesdisponíveis(emnavega-
doressemsuporteàintera çãoportoque,comoosdesktops,eleadicionaaclasse
no-touch)oupelaAPIemJavaScriptnoobjeto Modernizr:
184


## Página 195

CasadoCódigo Capítulo10. Ferramentas-Frameworks,PluginsePré-processadores
if(Modernizr.canvas) {
// Ok, podemos usar Canvas aqui.
} else {
// Canvas não está disponível neste navegador.
}
ParamaisdetalhesdasfuncionalidadesqueoModernizrpodedetectarepara
baixarocódigoparaadicionaraoseuprojeto,visitehttp://modernizr.com/.
-prefix-free
Éfatoquenenhumdesenvolvedorgostaderepetiromesmocódigoparasatisfa-
zer3ou4prefixosdiferentestodavezquesevaiusarumgradienteouumaanima ção
emCSS.
Parasolucionarissodiretonosnavegadores, LeaVerou, umaengenheirade
front-endgrega,desenvolveuumabibliotecaquealteraoCSSdasuapágina,adi-
cionandoapenasosprefixosnecessários. Amaiorvantagemdissoéquevocênão
precisaescreverassuasfolhasdeestilosepreocupandocomqualprefixovocêpre-
cisausarparacadapropriedadenovadoCSS3.
Seinteressouno-prefix-free?Ositedabibliotecaéhttp://leaverou.github.com/
prefixfree/.Interessadoounão,nãodeixedevisitaroblogdaLeaVerou,lotadode
outrasferramentasepostsinteressantessobreJavaScripteCSS3-http://lea.verou.
me/.
10.5 Polyfills
Existemdezenasdeoutrasbibliotecasqueajudamapreencherosburacosdefunci-
onalidadesausentesemdiversosnavegadoresdiferentesqueprecisamosenfrentar,
comosuporteaSVG,LocalStorage,WebSockets,Geolocaliza ção.Asbibliotecasque
implementamessasAPIsemnavegadoresantigosouquenãopossuemsuportere-
ceberamonomede Polyfills.[6]
NaWikidoModernizrnoGitHubexisteumalistaextensadediversasim-
plementaçõesdePolyfillsfeitaspelacomunidade, https://github.com/Modernizr/
Modernizr/wiki/HTML5-Cross-browser-Polyfills.
185


## Página 196

10.6. Pré-processadores CasadoCódigo
10.6 Pré-processadores
Infelizmente,CSSnãopossuiodinamismoealgunsrecursosdelinguagensdepro-
gramaçãocomoRuby,PythonouJavaScript,oquefazmuitasvezescomqueonosso
códigofiqueextensoerepetitivo. Paraamenizarisso,existemlinguagensinterme-
diáriasqueadicionamalgunsrecursosinteressantesnalinguagemeajudamacriar
maisestilos,commenoscódigos. Essaslinguagensintermediáriassãochamadas
depré-processadoresenomomentodaescritadesselivro,possorecomendartrês:
LESS,SasseStylus.
Ostrêspossuemmuitasfuncionalidadesemcomum,oqueajudaatransitarentre
cadapré-processadorparaavaliartodoseescolheroseufavorito.Vejaalgumasdas
principaisfuncionalidadesaseguir:
Seletoresaninhados
Parareduziraduplica çãodeseletores,ospré-processadorespermitemquevocê
aninheosseletoresdeelementoscontidosemoutroelemento(comonocasoabaixo).
// Aninhando os seletores, não precisamos escrever
// 'header nav ' e 'header a ' para alterar o estilo apenas dos elementos
// presentes dentro de 'header'.
header {
padding: 10px 5px;
nav {
float: left;
}
a {
color: red;
}
}
Comesteexemplo,conseguimosgeraroseguinteCSS:
header {
padding: 10px 5px;
}
header nav {
float: left;
186


## Página 197

CasadoCódigo Capítulo10. Ferramentas-Frameworks,PluginsePré-processadores
}
header a {
color: red;
}
Variáveis
Valoresemcomum,comoumacorouumtamanhoespecífico,quevocêtendea
repetircomfrequêncianasuafolhadeestilo,podemserextraídosparaumavariável.
Assim,casovocêprecisemudartodososvermelhosdoseusitepararoxovocênão
terátantotrabalho.
// No LESS, você pode definir variáveis com '@nomedavariavel: valor ',
// e usá-las em qualquer parte do seu código, além de poder manipular
// o seu valor com cálculos ou outras funções
@darkred: #990000;
@grid: 960px;
body {
color: @darkred;
width: @grid;
}
.sidebar {
width: @grid / 3;
}
.container {
width: @grid / 2;
}
QuandoprocessamosesteexemploutilizandooLESS,asdefini çõesdevariáveis
geramosseguintesseletores:
body {
color: #990000;
width: 960px;
}
.sidebar {
width: 320px;
187


## Página 198

10.6. Pré-processadores CasadoCódigo
}
.container {
width: 480px;
}
Mixins
Mixinstrazemmuitaflexibilidadeàsuafolhadeestilopararepetirdefini ções
similares,executarcálculosougerarprefixosespecíficossemrepetirasmesmasde-
finiçõesdiversasvezes.
// Os mixins do Stylus permitem que você escreva CSS sem se preocupar
// se está usando um mixin ou uma propriedade comum, como no caso abaixo
// onde o 'transform' cria todas as variações com os prefixos
// necessários.
// Caso você não precise mais dos prefixos '-moz' ou '-webkit',
// por exemplo, basta alterar o mixin e gerar o seu arquivo '.css'
// novamente.
transform() {
-moz-transform:arguments;
-ms-transform: arguments;
-o-transform:arguments;
-webkit-transform: arguments;
transform:arguments;
}
.slider {
transform: width 0.2s linear;
}
.popup {
transform: opacity 0.5s;
}
Comestadefini çãodemixin,oStylusconseguegeraroseguintecódigo:
.slider {
-moz-transform: width 0.2s linear;
-ms-transform: width 0.2s linear;
-o-transform: width 0.2s linear;
-webkit-transform: width 0.2s linear;
188


## Página 199

CasadoCódigo Capítulo10. Ferramentas-Frameworks,PluginsePré-processadores
transform: width 0.2s linear;
}
.popup {
-moz-transform: opacity 0.5s;
-ms-transform: opacity 0.5s;
-o-transform: opacity 0.5s;
-webkit-transform: opacity 0.5s;
transform: opacity 0.5s;
}
Mascuidado,pré-processadoresnãosãosóunicórniosearco-íris.Ousoexces-
sivoouinadequadodassuasfuncionalidadespodetrazerproblemasparavocêeasua
equipe.Muitoaninhamentocomplicaaleituradoseucódigoegeraseletoresmuito
maioresdoquevocêrealmenteprecisa.Muitosmixinsevariáveisdistanciamdemais
ocódigoquevocêescrevedocódigogerado,oquecomplicao debugearesolu ção
dosproblemasqueapareceremduranteodesenvolvimento.
ComodevidoconhecimentodeCSS,ospré-processadorespodemajudarbas-
tanteatornaroseucódigofontemaisflexíveleinteligente,sejamanipulandocores
parafacilitaracria çãodegradientes,escrevendoprefixosdenavegadoresespecífi-
coscomo -moze -webkitoureduzindoaduplica çãodecódigocommixinsou
funções.
Parafazerasuaescolha,sugiroumapesquisarápidaeum test-drivenospré-
processadoresdoseuinteresse.Confiraqualseadequamelhorasferramentaselin-
guagensquevocêjáusanoseudiaadia.Confiraossitesdecadaumparacome çar
aestudarmelhor:
• LESS-http://lesscss.org/;
• Sass-http://sass-lang.com/;
• Stylus-http://learnboost.github.com/stylus/.
10.7 É tudo CSS eHTML
Ositenscitadosacimasãofrutosdotrabalhodedesenvolvedorescomoeuevocê,
comgrandeinteresseemCSSeHTML.Antesdeteressasferramentasemmãos,
todoselespassaramporapertoseproblemasclássicosqueseencontramnodiaadia
dedesenvolvimento.Antesdeentrardecabe çanessafesta,lembre-sedepraticarum
poucosemtaisferramentas,apenasvocêeseueditorfavorito.
189


## Página 200

10.7. ÉtudoCSSeHTML CasadoCódigo
Desenvolvendoascoisas“namão”vocêconsegueentendermelhorarazãode
taissoluçõesteremsidocriadasequaisosproblemasqueelassolucionam. Quem
sabe,noprocesso,vocêpodecriarferramentasesolu çõesprópriasecompartilhá-las
comacomunidade.
190


## Página 201

Capítulo11
Nãopareporaqui
AbordamosdiversosassuntossobreHTMLeCSSnestelivro,masouniversoem
tornodestastecnologiasévastodemaisparasecomprimirtodasasreferências,ex-
plicaçõesetécnicasemumlivro.Etudoestáevoluindoapassoslargos,oquesigni-
ficaqueprecisamosacompanharessesassuntoseconferirasnovidadesquesurgem
paraaprimorarefacilitarotrabalhodedesenvolvedorescomoeuevocê.Paraisso,
possolheindicarasfontesqueeuediversosoutrosprofissionaisutilizamosparanos
manteratualizados,eacreditoquealgumasdelaspodemlheserbastanteúteis.
Referênciasnainternet
Umafonteincríveldeconteúdosobredesenvolvimentowebéacomunidadecri-
adaemtornodo CSS-Tricks(http://css-tricks.com/),mantidopeloChrisCoyier,
desenvolvedoredesigneramericano,queajudadiversosprofissionaisacriarweb-
sites melhores desde 2007. Outro lugar bastanteinteressante para se encontrar
publicaçõesnosdiversosassuntosdawebéarevistadigital AListApart (http:
//www.alistapart.com/),quetambémpossuiumaeditoradelivrosparadesenvol-


## Página 202

CasadoCódigo
vedores,chamadaABookApart,epreparaumasériedeeventostodoanochamado
AnEventApart.
Parareferênciasrápidaseexplicaçõesenxutassobrefuncionalidadesnovas,tec-
nologiasassociadasaHTML5etudomais,euindicodoissitesincríveisparares-
ponderperguntascomo "Quais navegadores atualmente suportam animações?” ou
"Como eu posso simular o uso de Media Queries no Internet Explorer?” oWhencan
Iuse... (http://caniuse.com/)eo HTML5Please (http://html5please.com/).Atua-
lizadosconformenovasespecifica çõessurgemenovasversõesdenavegadoressão
lançadas,ambosossitespossuemasreferênciasnecessáriasparasabercomoepor
ondecomeçaratrabalharcomcoisasnovas.
Outrositebastanteinteressanteparasetercomoreferênciaéo DiveintoHTML5
(http://diveintohtml5.info/).OriginalmentecriadoporMarkPilgrimecomdiver-
sascontribuiçõesdeoutrosdesenvolvedores,oDiveintoHTML5éumareferência
completaquevaidesdeastagsintroduzidasnoHTML5quantoaAPIsdeJavaScript
disponíveiseadesenhodegráficosem canvas.Omesmopodesedizerdo HTML5
Doctor(http://html5doctor.com/about/),outrositebastantecompletodereferên-
ciaseartigossobreoassunto.
Acompanhequementendedoassunto
Euacreditoqueomundodatecnologiaéfeitoporaquelesqueocompõem,e
nãoapenaspelasempresaspresentesnomercado.Porisso,euconsideromuitointe-
ressanteotrabalhodesenvolvidopordiversaspessoaspelomundoquenosúltimos
anos,independentedocargoouempresaqueelaseencontrasse,compartilhando
conteúdo,criandoprojetosepalestrassobrediversosassuntosrelacionadosawebe
auxiliandootrabalhodemuitosoutros.
Sugiroquevocêpesquiseeacompanheostrabalhos,blogseslidesdealgunsda
listadetalentososprofissionaisabaixo.UmcanalcomumentretodoseleséoTwitter,
entãoadicioneiosseususuáriosnoTwitterparavocêacompanharoqueelesandam
comentandoporlá:
•Paul Irish(@paul_irish), Mathias Bynens(@mathias), Divya Manian
(@divya),NicolasGallagher(@necolas)etodososoutrosenvolvidosnospro-
jetosdoHTML5Boilerplate,HTML5Pleaseeosoutrosrelacionados. Você
podeconferirtudoqueessagaleraestácriandonoperfildaorganiza çãono
GitHub,https://github.com/h5bp.
•LeaVerou(@leaverou),criadorado-prefix-free,Dabblet(http://dabblet.com)
192


## Página 203

CasadoCódigo Capítulo11. Nãopareporaqui
ediversasoutrasferramentasrelacionadasaCSS3. Alémdisso,elaviajao
mundoapresentandosuaspalestrasdediversosassuntos.
•EthanMarcotte(@beep),autordolivro Responsive Web DesigneLukeWro-
blewski(@lukew),autordo Mobile FirstdaABookApart,livrosquesetor-
naramleiturasobrigatóriasemseusrespectivosassuntos.
•BradFrost (@brad_frost),outroentendidonoassuntodedesignresponsivo
deusabilidade,quetrabalhouemdiversosprojetosinteressantesdeaplica ções
paradispositivosmóveis.
•RyanSinger(@rjs),designerda37signals,quepossuiótimaspalestrasearti-
gossobreofluxodetrabalhoeodesenvolvimentodeinterfacesparaaweb.
•EduardoShiota (@shiota),designerquealémdepalestraremdiversoseven-
tosaquinoBrasiltambémministraumcursosobreResponsiveWebDesign
noHowtocode(http://howtocode.com.br/workshops/responsive-design).
•SérgioLopes(@sergio_caelum),quealémdeatuarcomodesenvolvedorna
Caelumtambémécoordenadoreinstrutordeseuscursosdewebdesign.
•KyleNeath(@kneath),BenBleikamp(@bleikamp)etodaaequipededesign
doGitHub,responsáveispordiversosprojetoseinterfacessensacionais.
Outroslivros
Umcaminhointeressanteparaseaprofundaremoutrosassuntosrelacionadosa
HTMLeCSSémergulharembonslivrossobreoquevocêquertantoaprender.A
editoraABookApart possuiumaótimacole çãodelivrosnocampodewebdesign,
abordandodiversosassuntos,desdeHTMLeCSS( HTML5 for Web Designers, CSS
3 for Web Designerseoincrível Responsive Web Design),tipografiaparaaweb( On
Web Typography)eusabilidadeedesign( Designing for Emotion).Sãolivrospequenos
porémbastanteobjetivosemsuasexplica çõesericosemconteúdo.
CasoseinteresseporJavaScript,aO’Reillypossuidiversoslivrossobrealingua-
gemesuautiliza çãonosdiasdehoje,abordandodesdeassuntosbásicoseintrodu-
tóriosaguiasavan çados. Dosdiversostítulosdaeditora,osprincipaisnaminha
opiniãosão: JavaScript:The Good Parts, JavaScript Web Applicationse jQuery Pocket
Reference.
193


## Página 204

ÍndiceRemissivo CasadoCódigo
ÍndiceRemissivo
-prefix-free,185
::after,41
::before,41
:hover,17
3d,161
alt,18
animation,170
article,29
aside,29
background,15
background-color,15
border,13
border-radius,67
Boxmodel|hyperpage,38
box-sizing,38
CDN,184
clear,99
clearfix,106
color,16
column,118
data-*,29
display,96
figcaption,71
figure,71
flexbox,119
float,20,97
FontAwesome,64
font-family,11
font-size,12
Fontello,64
FontSpring,63
FontSquirrel,63
footer,29
Formulários,123
GoogleWebFonts,63
grid,117
header,29
HTML5Boilerplate,183
html5shiv,33
IcoMoon,64
Iconic,64
ImageOptim,19
img,18
impressão,52
LESS,186
margin,13
Modernizr,184
nav,29
Normalize.css,37
onTransitionEnd,160
194


## Página 205

CasadoCódigo ÍndiceRemissivo
OOCSS,50
padding,13
Pictos,64
placeholder,134
Polyfills,185
position,107,110
Pré-processadores,186
preserve-3d,168
PressStart2P,63
pseudoseletor,17
pseudo-elementos,41
reset,35
ResponsiveWebDesign,176
rodapé,22
Sass,186
section,29
Shifticons,64
src,18
Stylus,186
transform,150
transition,155
TwitterBootstrap,182
Typekit,63
width,11
Wufoo,125
z-index,113
195


## Página 207

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1] RossAllen.Cssbox-shadowcanslowdownscrolling.http://nerds.airbnb.com/
box-shadows-are-expensive-to-paint,2011.
[2] ChrisCoyier.Fightingthespacebetweeninlineblockelements.http://css-tricks.
com/fighting-the-space-between-inline-block-elements/,2012.
[3] Nicolas Gallagher. About normalize.css. http://nicolasgallagher.com/
about-normalize-css/,2012.
[4] BradFrostJeremyKeithLyzaD.GardnerScottJehlStephanieRiegerJason
GrigsbyBryanRiegerJoshClarkTimKadlecBrianLeRouxAndreaTrasatti
LukeWroblewski,ScottJenson.Futurefriendly.http://futurefriend.ly/,2011.
[5] EthanMarcotte. Responsivewebdesign. http://www.alistapart.com/articles/
responsive-web-design,2010.
[6] Remy Sharp. What is a polyfill? http://remysharp.com/2010/10/08/
what-is-a-polyfill/,2010.
[7] Nicole Sullivan. The media object saves hundreds of li-
nes of code. http://www.stubbornella.org/content/2010/06/25/
the-media-object-saves-hundreds-of-lines-of-code/,2010.
197
