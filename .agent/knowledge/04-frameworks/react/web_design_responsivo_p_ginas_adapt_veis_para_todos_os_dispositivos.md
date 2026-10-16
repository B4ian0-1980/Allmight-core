---json
{
  "id": "web_design_responsivo_p_ginas_adapt_veis_para_todos_os_dispositivos",
  "title": "Web Design Responsivo Páginas adaptáveis para todos os dispositivos",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Arquivo Original:** `Web Design Responsivo Páginas adaptáveis para todos os dispositivos.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "adapt",
    "design",
    "dispositivos",
    "frameworks",
    "ginas",
    "para",
    "react",
    "responsivo"
  ],
  "perguntas_tipo": [
    "Como utilizar Web Design Responsivo Páginas adaptáveis para todos os dispositivos?",
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

# Web Design Responsivo Páginas adaptáveis para todos os dispositivos

> **Arquivo Original:** `Web Design Responsivo Páginas adaptáveis para todos os dispositivos.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© 2012, Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610,de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográﬁcos,
eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8ºandar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 5

CasadoCódigo
Prefácio
Aerapós-PCdacomputa çãopessoalchegoucomtudo.Nostabletsesmartphones,
aWeb,/f_inalmente,temachancedesetornarverdadeiramenteubíquaeonipresente.
Aindaestamosnocome çodessanovafasedatecnologia,masofuturoéinegavel-
mentedaWebmóveledosmaisdiversosaparelhosdenavega ção.
Essanovaperspectivatrazdesa/f_iosimportantes.Atéontem,Websigni/f_icavaum
navegadorinstaladonumDesktopcontroladopormouseetecladonumateladeta-
manhoconfortável. Nossossitesforamconstruídospensandonessecenário. Mas,
agora,temostelaspequenas,touchscreen,redesmóveisemuitasoutrasdiferen ças.
PrecisamosdeumanovaWeb.UmaWebquesuporteessaexplosãodedispositivos
e,maisainda,estejapreparadaparaofuturodedispositivosqueaindanemconse-
guimosantever.
OWebDesignResponsivoéachaveparaessanovaWeb.Épensarempáginas
queseadaptematodotipodedispositivoecontextodeuso. Ésairdaslimita ções
deumbrowserDesktopeseutamanhoprevisível,epensarempáginascom/f_lexi-
bilidadequesuportemtodotamanhodetela,qualquertipoderesolu ção,interfaces
comtouchoumouse.PensarresponsivamenteérepensaraWebparaofuturo.
Eestelivroéaferramentaquevocêprecisapraentenderosdesa/f_iosdoWebDe-
signResponsivo.OTárciomostraospilaresdeumainterfaceresponsiva,exploraos
aspectostécnicosdoHTMLeCSS,emostraideiasparaumainterfacemóvelusá-
vel.ÉumlivroquerecomendoparatododesenvolvedorWebquequeiraparticipar
ativamentedanovaWeb.Esperoquevocêaproveitealeituracomoeuaproveitei.
Sérgio Lopes - @sergio_caelum
Instrutor e desenvolvedor na Caelum
i

## Página 7

CasadoCódigo Sumário
Sumário
/one.oldstyle Introdução /one.oldstyle
/one.oldstyle . /one.oldstyle E s t a t í s t i c a sd om u n d om o b i l e....................... /one.oldstyle /zero.oldstyle
/one.oldstyle . /two.oldstyle U m aq u e s t ã od ec o n c e i t o.......................... /one.oldstyle /three.oldstyle
/one.oldstyle./three.oldstyle MasmeusitejáestábomparaAndroideiPhone!. . . . . . . . . . . . /one.oldstyle/four.oldstyle
/one.oldstyle . /four.oldstyle P a r aq u e mée s t el i v r o ?........................... /one.oldstyle /five.oldstyle
/one.oldstyle . /five.oldstyle P a r aa p r o v e i t a rm e l h o re s t el i v r o...................... /one.oldstyle /five.oldstyle
/two.oldstyle Princípiosdeumwebdesignresponsivo /one.oldstyle/seven.oldstyle
/two.oldstyle . /one.oldstyle C o m os u r g i uow e bd e s i g nr e s p o n s i v o.................. /one.oldstyle /seven.oldstyle
/two.oldstyle./two.oldstyle Atrincatecnológicadowebdesignresponsivo . . . . . . . . . . . . . /one.oldstyle/eight.oldstyle
/two.oldstyle./three.oldstyle Resoluçõ e sd et e l a.............................. /one.oldstyle /nine.oldstyle
/three.oldstyle layout/f_luído /two.oldstyle/three.oldstyle
/three.oldstyle . /one.oldstyle T i p o sd em e d i d ae mC S S........................../two.oldstyle /four.oldstyle
/three.oldstyle./two.oldstyle Afórmulamágicadowebdesignresponsivo. . . . . . . . . . . . . . . /two.oldstyle/six.oldstyle
/three.oldstyle . /three.oldstyle E x e m p l od eu ml a y o u t/f_i x o......................... /two.oldstyle /seven.oldstyle
/three.oldstyle . /four.oldstyle M e t a t a gv i e w p o r t.............................. /three.oldstyle /seven.oldstyle
/three.oldstyle./five.oldstyle Convertendoumlayout/f_ixoemlayout/f_luído . . . . . . . . . . . . . . /four.oldstyle/five.oldstyle
/four.oldstyle Imagenserecursos/f_lexíveis /five.oldstyle/five.oldstyle
/four.oldstyle . /one.oldstyle C S Sp a r ai m a g e n s/f_l e x í v e i s......................... /five.oldstyle /five.oldstyle
/four.oldstyle . /two.oldstyle C S Sp a r ao u t r o sr e c u r s o s/f_l e x í v e i s..................... /five.oldstyle /nine.oldstyle
/four.oldstyle./three.oldstyle Oproblemadeimagensemlayouts/f_luídos. . . . . . . . . . . . . . . . /six.oldstyle/six.oldstyle
/four.oldstyle./four.oldstyle Técnicasparaimagens/f_lexíveisemwebdesignsresponsivos . . . . . /six.oldstyle/seven.oldstyle
/four.oldstyle./five.oldstyle Imagensemaltaresoluçã o......................... /seven.oldstyle /two.oldstyle
/four.oldstyle . /six.oldstyle T i p o sd ei m a g e mp a r aw e b......................... /seven.oldstyle /three.oldstyle
iii

## Página 8

Sumário CasadoCódigo
/five.oldstyleMediaQueries /eight.oldstyle/one.oldstyle
/five.oldstyle./one.oldstylePrimeiro,osMediaTypes. . . . . . . . . . . . . . . . . . . . . . . . . . /eight.oldstyle/one.oldstyle
/five.oldstyle./two.oldstyleMediaQueries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /eight.oldstyle/five.oldstyle
/five.oldstyle./three.oldstyleParâmetrosparatrabalharcomMediaQueries . . . . . . . . . . . . . /eight.oldstyle/five.oldstyle
/five.oldstyle./four.oldstyleOperadoresLógicos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /nine.oldstyle/three.oldstyle
/five.oldstyle./five.oldstyleVáquebrandoseudesignembreakpointsbempensados. . . . . . . . /nine.oldstyle/four.oldstyle
/five.oldstyle./six.oldstyleGerenciamentodeerros. . . . . . . . . . . . . . . . . . . . . . . . . . . /nine.oldstyle/eight.oldstyle
/five.oldstyle./seven.oldstyleUsoconscientedeMediaQueries . . . . . . . . . . . . . . . . . . . . ./one.oldstyle/zero.oldstyle/zero.oldstyle
/five.oldstyle./eight.oldstyleMediaQueriesnaprática . . . . . . . . . . . . . . . . . . . . . . . . . ./one.oldstyle/zero.oldstyle/six.oldstyle
/six.oldstyleTópicosdeWebMobile /one.oldstyle/one.oldstyle/one.oldstyle
/six.oldstyle./one.oldstyleOqueéMobileFirst? . . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/one.oldstyle/two.oldstyle
/six.oldstyle./two.oldstylePorqueMobileFirst? . . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/one.oldstyle/two.oldstyle
/six.oldstyle./three.oldstyleNotasgeraissobreMobileFirst . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/one.oldstyle/three.oldstyle
/six.oldstyle./four.oldstyleComoaspessoasusamdispositivosmóveis?. . . . . . . . . . . . . . . /one.oldstyle/one.oldstyle/five.oldstyle
/six.oldstyle./five.oldstyleOconteúdoéorei . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/one.oldstyle/nine.oldstyle
/six.oldstyle./six.oldstylePadrõesdenavegaçãomobile . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/two.oldstyle/zero.oldstyle
/six.oldstyle./seven.oldstyle/one.oldstyle/zero.oldstyleprincípiosdedesignparainterfacesmobile. . . . . . . . . . . . . . /one.oldstyle/two.oldstyle/seven.oldstyle
/seven.oldstyleContinuandoseusestudos /one.oldstyle/three.oldstyle/three.oldstyle
/seven.oldstyle./one.oldstyleArtigos/Tutoriais. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/three.oldstyle/three.oldstyle
/seven.oldstyle./two.oldstyleBookmarklets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/three.oldstyle/five.oldstyle
/seven.oldstyle./three.oldstyleEsboçoeplanejamento . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/three.oldstyle/five.oldstyle
/seven.oldstyle./four.oldstyleFerramentas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/three.oldstyle/six.oldstyle
/seven.oldstyle./five.oldstyleInspiração. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/three.oldstyle/seven.oldstyle
/seven.oldstyle./six.oldstyleJavaScriptpuro. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/three.oldstyle/seven.oldstyle
/seven.oldstyle./seven.oldstylePluginsjQuery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/three.oldstyle/eight.oldstyle
/seven.oldstyle./eight.oldstyleTestesderesponsividade . . . . . . . . . . . . . . . . . . . . . . . . . ./one.oldstyle/four.oldstyle/zero.oldstyle
/seven.oldstyle./nine.oldstyleTemplateseFrameworks . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/four.oldstyle/one.oldstyle
/seven.oldstyle./one.oldstyle/zero.oldstylePalavras/f_inais. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . /one.oldstyle/four.oldstyle/two.oldstyle
Bibliogra/f_ia /one.oldstyle/four.oldstyle/two.oldstyle
iv

## Página 9

C/a.sc/p.sc/iacute.sc/t.sc/u.sc/l.sc/o.sc/one.oldstyle
Intro dução
Épossíveldesenvolverumasóapresenta çãoparaumsite,umsó web design. Mais
além:queessedesignsejabemapresentadoemquaisquerdispositivose,conforme
setenhaplanejado,queseadapteaosdiferentesmeiosemqueestesiteéacessado.
Sim,épossível,masnãoéoquevemosporaí.
ReparenositedaCNN,em/two.oldstyle/zero.oldstyle/one.oldstyle/two.oldstyle,emumbrowser:

## Página 10

CasadoCódigo
Eagoraomesmosite,quandovistoemumdispositivoquenãoumcomputador:
/two.oldstyle

## Página 11

CasadoCódigo Capítulo/one.oldstyle. Introdução
Apáginanodispositivomóvelaparececortadaeparaverapartequeestáfal-
tandoénecessáriofazero scrollhorizontal.Jánaversãoqueéabertaemum Desktop,
ositeabrecompleto.ApáginadaCNNnãoseadaptouaosdiferentesmeiospelos
quaiseleéacessado,jáque,naversãomóvel,nóssomosobrigadosaentrarema ção
paravisualizaroconteúdorelevante.
RepareomesmoefeitonositedaEditoraCasadoCódigo:
Eomesmosite,emdispositivomóvelpodeservisualizadodaseguinteforma:
/three.oldstyle

## Página 12

CasadoCódigo
Paraumaimagemmaisimpactante,vejaositedolivrodearquiteturaJava,do
pessoaldaCaelum,emdiversosdispositivos:
/four.oldstyle

## Página 13

CasadoCódigo Capítulo/one.oldstyle. Introdução
Vejaoutrosexemplosincríveisdesitescomessascaracterísticas,quearevista
TripWirereuniu:
/five.oldstyle

## Página 14

CasadoCódigo
/six.oldstyle

## Página 15

CasadoCódigo Capítulo/one.oldstyle. Introdução
/seven.oldstyle

## Página 16

CasadoCódigo
/eight.oldstyle

## Página 17

CasadoCódigo Capítulo/one.oldstyle. Introdução
Sitescomestascaracterísticaspossuem webdesignresponsivo.
Umsitecomwebdesignresponsivo-ou responsive web design-podeseraces-
sadodeumPC,notebook,smartphone,tablet,TV,geladeira,banheira-sim,real-
menteexistemgeladeirasebanheirasqueacessamainternet!-,emsuma,dequal-
querdispositivocomacessoàrede,independentementedesuaresolu ção,desua
capacidadedecores,seé touchounão. E,mesmocomessasdiferen çasdosdis-
positivosquepodemacessarseusite,elecontinuabemapresentado,inclusivecom
possibilidadedesealteraraordememqueosconteúdosapareceme,atémesmo,se
determinadosconteúdosserãoounãomostradoslogodecara!
/nine.oldstyle

## Página 18

/one.oldstyle./one.oldstyle. Estatísticasdomundomobile CasadoCódigo
Diganãoamaisversõesespecí/f_icasparacelulares;bastadelinguagenspróprias
paramobile;chegadesubdomíniosoudiretóriosespecí/f_icosparaatenderao“ público
móvel”!Nãoexisteuma“ web mobile”( mobile web).Awebéúnica .Então,naminha
opinião-enademilharesdeoutrosdesenvolvedoreswebpelomundo-,owebdesign
responsivoéarespostaúnicaparaumawebúnica!
Nãosetratadeuma“moda”ouumhypedainternet;nãosetratadealgoque
chegou,vaiangariaralgunsfãsesumirnapróximaesta ção.Owebdesignrespon-
sivoéumanovaformade pensaraweb e,dentrodepoucotempo,serátãovitale
importanteaosdesenvolvedoreseàexperiênciadousuárioquantoopróprioHTML
ouoCSS.
Aoterminardelerestelivroe/f_ixarseusconteúdos,vocêfarápartedoroldepro-
/f_issionaisdewebcapazesdedesenvolversites responsivosepoderágritar,aplenos
pulmões,quevocê,também,contribuiparaumawebeparaummundomelhor!
/one.oldstyle./one.oldstyle E/s.sc/t.sc/a.sc/t.sc/iacute.sc/s.sc/t.sc/i.sc/c.sc/a.sc/s.sc /d.sc/o.sc /m.sc/u.sc/n.sc/d.sc/o.sc /m.sc/o.sc/b.sc/i.sc/l.sc/e.sc
Enãoésomenteporqueusaressatecnologiaéalgodivertidodesefazer.Existeuma
fortebaseestatísticaquejusti/f_icaporquedevemosprestarmuitoaten ção-eatuar!-
nomercado mobile.
Porexemplo,haviaumaprevisãodequeasvendasdecelularesultrapassariam
asvendascombinadasdedesktopsenotebooksem/two.oldstyle/zero.oldstyle/one.oldstyle/two.oldstyle. Bem,aprevisãoestava
errada:issoaconteceuem/two.oldstyle/zero.oldstyle/one.oldstyle/zero.oldstyle(http://ow.ly/awhu/three.oldstyle),mesmoanoemqueonúmero
decelularese smartphonesbateuacasados /two.oldstyle/zero.oldstyle/zero.oldstylemilhõesnoBrasil!Emais:casonão
aconteçaantes,aprevisãoédequeoacesso mobileàinternetultrapasseoviaPCse
notebooksem/two.oldstyle/zero.oldstyle/one.oldstyle/three.oldstyle(http://ow.ly/awi/zero.oldstylec)!
É interessante notar que, conforme é destacado num artigo muito interes-
santesobreomercadomobiledoBrasil(http://ow.ly/bg/seven.oldstyleWp),em/two.oldstyle/zero.oldstyle/one.oldstyle/one.oldstyle,avendade
smartphonescresceu/one.oldstyle/seven.oldstyle/nine.oldstyle/percent.oldstylenoBrasil,comdestaqueparaasinforma çõesdeque:
• /three.oldstyle/three.oldstyle/percent.oldstyledaspessoasjátinhamsmartphones;
• /two.oldstyle/zero.oldstyle/percent.oldstylecomfunçõesconsideradasavan çadas,comoWi/f_i,GPSetc;
• /four.oldstyle/one.oldstyle/percent.oldstyleacessavaainternet;
• Noúltimoquadrimestre,onúmerodeusuários mobilecresceu/four.oldstyle/zero.oldstyle/percent.oldstyle.
/one.oldstyle/zero.oldstyle

## Página 19

CasadoCódigo Capítulo/one.oldstyle. Introdução
Podeparecerincrível,massecompararmosasvendasdeaparelhosmóveiscom
ataxadenatalidade,osdispositivos mobiletêmumataxadecrescimento /four.oldstylevezes
maiorqueadapopula çãomundial!
E,partindoparaolado/f_inanceiro(http://ow.ly/awinf):
• OPayPalmovimentaUS /dollar.oldstyle/one.oldstyle/zero.oldstylemilhõespordiaempagamentosmobile;
• AsvendasmundiaisatravésdedispositivosmóveisnoeBaychegaramperto
deUS /dollar.oldstyle/two.oldstylebilhõesem/two.oldstyle/zero.oldstyle/one.oldstyle/zero.oldstyle(sãofeitoscercade/nine.oldstyle/four.oldstylelancespor minuto);
• Emdezembrode/two.oldstyle/zero.oldstyle/one.oldstyle/zero.oldstyle,onúmerodeusuáriosdoaplicativodoYelpestavana
casados/three.oldstyle,/two.oldstylemilhõese/three.oldstyle/five.oldstyle/percent.oldstyledasbuscasfeitasnositesãoatravésdesseapp.
Levandoemcontacomoéfeitoousodo mobilepelaspessoas,tambémháalguns
númerosrecolhidospeloGoogleemsoloestadunidensequemerecematen ção(http:
//ow.ly/awkw/seven.oldstyle):
• /seven.oldstyle/nine.oldstyle/percent.oldstyleusamsmartphonecomoauxílionahoradefazercompras(/seven.oldstyle/zero.oldstyle/percent.oldstyledentroda
loja);
/one.oldstyle/one.oldstyle

## Página 20

/one.oldstyle./one.oldstyle. Estatísticasdomundomobile CasadoCódigo
• /five.oldstyle/four.oldstyle/percent.oldstyleparaprocuraroendereçodeumaloja;
• /four.oldstyle/nine.oldstyle/percent.oldstyleparacompararpreços;
• /four.oldstyle/four.oldstyle/percent.oldstyleparalerreviewsdeprodutos;
• /seven.oldstyle/four.oldstyle/percent.oldstyle tomam a decisão da compra baseados em informaçõesobtidas no
smartphone;
• /three.oldstyle/five.oldstyle/percent.oldstyledosquepesquisamnosmartphonecompramoprodutoatravésdele;
• /eight.oldstyle/eight.oldstyle/percent.oldstylequeencontraminformaçõesno smartphonetomamainiciativanomesmo
dia;
• /seven.oldstyle/one.oldstyle/percent.oldstyledosquebuscamalgoemumsmartphoneofazemapósveremumanúncio;
• /seven.oldstyle/nine.oldstyle/percent.oldstyledosanunciantesaindanãotêmumsiteotimizadoparamobile(!).
“NossoPlanetaMobile:Brasil"
Emmaiode/two.oldstyle/zero.oldstyle/one.oldstyle/two.oldstyle,aGoogleliberou,nomundotodo,umapesquisachamadade
“NossoPlanetaMobile”.Felizmente,oBrasiltambémfoicontempladoeumdocu-
mentofoidisponibilizadocomosresultadosobtidos.Éaltamenteaconselhávelque
vocêtenhaacessoeestudeorelatório“ NossoPlanetaMobile:Brasil-Comoen-
tenderousuáriodecelular ”(http://ow.ly/bg/nine.oldstyle/three.oldstyleQ). Jáadiantandoalgunsnúmeros
importantes:
/one.oldstyle/two.oldstyle

## Página 21

CasadoCódigo Capítulo/one.oldstyle. Introdução
• Adifusãodos smartphonesatinge/one.oldstyle/four.oldstyle/percent.oldstyledapopulaçãoeessesproprietáriosde
smartphonesdependemcadavezmaisdeseusdispositivos. /seven.oldstyle/three.oldstyle/percent.oldstyleacessama
internettodososdiasno smartphoneemuitosnuncasaemdecasasemele;
• /eight.oldstyle/eight.oldstyle/percent.oldstyledosusuáriosdesmartphonesprocuraminformaçõeslocaisemseustele-
fonese/nine.oldstyle/two.oldstyle/percent.oldstyletomamdecisõesemdecorrênciadisso,comofazerumacompra
ouentraremcontatocomaempresa;
• /three.oldstyle/one.oldstyle/percent.oldstyledosusuáriosdesmartphones/f_izeramumacomprapelocelular;
• Anúnciosparacelularsãovistospor/nine.oldstyle/four.oldstyle/percent.oldstyledosusuáriosdesmartphones;
• /seven.oldstyle/five.oldstyle/percent.oldstyledosusuáriosrealizaramumapesquisaemseussmartphonesdepoisde
visualizarumanúnciooﬀ-line.
/one.oldstyle./two.oldstyle U/m.sc/a.sc /q.sc/u.sc/e.sc/s.sc/t.sc/atilde.sc/o.sc /d.sc/e.sc /c.sc/o.sc/n.sc/c.sc/e.sc/i.sc/t.sc/o.sc
Comovimos,jáéumarealidadequeosmaisdiversosdispositivos mobilechegaram
para/f_icar,estãoassumindoseulugar(eodeoutros)e,daquianãomuitotempo,
prometemseropadrãoparaacessoaweb!Jáéhoradecome çaraolharparaodesk-
topcomumolharsaudosista,agradecendoportudooqueelefezportodosnósaté
hoje,mas,aomesmotempo,jásepreparandoparaoqueofuturo(breve)trará.
Emnossodia-a-dia,jáépossívelperceberisso.Noteque,noslugaresmaisinu-
sitados,aspessoasestãoandandonãosomentecomseus smartphonesligadoseem
plenouso,mas,também,comseu tablets, e-Readersemuitosoutrosdispositivoscom
nomesextravagantes.Masnãopensesomenteemdispositivoscom d i s p l a y smenores
doqueostamanhosdemonitorconvencionais.Ouaindanãoouviufalarnas S m a r t
T V senemviualguémacessandositesatravésdeumvideogame?
Emquaisquerdoscasoscitados,asitua çãoidealéqueossitesdesenvolvidos
sejambemapresentados(e,até, o t i m i z a d o s)conformeo devicequeoestáacessando
nomomento.Seráqueasinforma çõesexibidasparaquemacessaumsitedejogos
atravésdeseuvideogamedevemserapresentadasexatamentedamesmamaneirade
quemrealizaesseacessousandoumcelularou tablet?Obviamentequenão!
Maséaíqueestáograndeproblemadodesenvolvimentoweb“tradicional":os
sitesnãosãoidealizados,desdesuaconcep ção,paraserem/f_lexíveisemostradosde
formaadequada,sejaláporquemeiodeacessoapessoaosestejamacessando.Per-
cebaque,maisdoqueumaquestãotécnica,estamostratandodealgo conceitual!
/one.oldstyle/three.oldstyle

## Página 22

/one.oldstyle./three.oldstyle. MasmeusitejáestábomparaAndroideiPhone! CasadoCódigo
Eparacome çarapensaremwebdesignresponsivo,oprimeiropassoécome çar
amudarseusconceitos!
Qualasolu ção?
Asolução(ousolu ções)paraqueawebpossaevoluireosdesenvolvedorespos-
samatualizarseu know-howteóricoepráticoé,justamente,oqueétratadoneste
livro. Atravésdosconteúdosaquiapresentados,équeospro/f_issionaisdewebto-
marãoconhecimentosobretécnicascomo layout/f_luído,imagens/f_lexíveis,Media
Queriesemuitasoutrasdicasúteissobreodesenvolvimentode websitesresponsi-
vos!
Preparado?
/one.oldstyle./three.oldstyle M/a.sc/s.sc /m.sc/e.sc/u.sc /s.sc/i.sc/t.sc/e.sc /j.sc/aacute.sc /e.sc/s.sc/t.sc/aacute.sc /b.sc/o.sc/m.sc /p.sc/a.sc/r.sc/a.scA/n.sc/d.sc/r.sc/o.sc/i.sc/d.sc /e.sc /i.scP/h.sc/o.sc/n.sc/e.sc/exclam.sc
Vocêpodeterumsitefocadoparacadadispositivo,mashádiversasdesvantagens
nessaabordagem. Emespecial,equandohouverumnovodispositivomóvel,com
umatelabemdiferente?Equandoprecisarfazerumaaltera ção,terádetomarcui-
dadocomcadaumadasváriasversõesdoseusite.
TomemoscomoexemplooWikipédiaque,atualmente,vairedirecioná-loparaa
páginahttp://en.m.wikipedia.org/seoacessofor mobile.Chamamosistodeestratégia
do“mponto”( m.website.com).Sevocêabri-lanodesktop,apágina/f_luieocupaa
telatoda.Ficafeioemeioruimdeusar,maséaceitável.Elesnãousam media queries
(queaindaveremosnesteLivro)enemnadamaisavan çadopara responsivar.Masé
responsivo?Ninguémsabedizeraocerto,/f_icanumaáreacinza...
Umoutroconceitoumpoucodiferenteéode OneWeb.Quedevemosteruma
URLsópratudo,umsistemasóeservirmesmoconteúdopratodomundo.ODe-
signResponsivocostumaserumaformadeimplementarOneWebcomusabilidade
adequadapratodomundo.
Háaindaquemfaledeumaoutratécnicachamada RESS-Responsivedesign+
ServerSidecomponents .VocêserveamesmaURL,mesmapágina,masajustano
server-sidealgumascoisassabendoqual browseré.Faz-se user-agent sniﬃng,queé
menospreciso,masajudaemalgumascoisas,comodecidirseumlinkparaliga ção
diretanocelulardeveserexibido.
Vocêpodeusar server-sidepramanteramesmaURL(OneWeb),masservirpá-
ginasespecí/f_icas(nãoresponsivas).Ouseja,hácombinaçõesdiversasdessastécnicas
(oneweb+responsivo,onewebnãoresponsivo,doissiteseresponsivo,etc).
/one.oldstyle/four.oldstyle

## Página 23

CasadoCódigo Capítulo/one.oldstyle. Introdução
Nesselivro,focaremosemDesignResponsivocomOneWeb.Ouseja,explora-
remososexemplosecenáriosdesitesúnicosseadaptandoatravésMediaQueries,
CSS/f_lexívelerecursos/f_lexíveis.Essecenárioninguémquestionaseéresponsivoou
não.
/one.oldstyle./four.oldstyle P/a.sc/r.sc/a.sc /q.sc/u.sc/e.sc/m.sc /eacute.sc /e.sc/s.sc/t.sc/e.sc /l.sc/i.sc/v.sc/r.sc/o.sc/question.sc
Webdesignresponsivo éumassuntoque,principalmentenoBrasil,aindaénovi-
dade.Atéosmaisveteranos(e,talvez,principalmenteeles)desconhe çamastécnicas
e/ou,mesmo,seuconceito-gostariadeacreditarquenãoéocasodamaioriados
desenvolvedores,mas,casoseja,temosumtrabalhodeconscientiza çãoaindamaior
afazer! Porisso,querendoounão,estelivrodestina-seaquemjápossuialguns
conhecimentosespecí/f_icosnaáreadedesenvolvimentoweb.
Estelivroédestinadoatodoequalquerpro/f_issional,estudanteouaspirantea
desenvolvedorwebquedesejacome çarouaprofundarseusestudosemwebdesign
responsivo.Atravésdostópicos,tentamosencontraramelhormaneiradeexporeste
assunto-que,naverdade,nãoétãããocomplexo,assim-daformaque,paranós,foi
acronologicamenteadequadaedidaticamentesatisfatória.
Portanto,casoqueiraterseuprimeirocontatocomdesignresponsivoou,casojá
otenhatido,mas,poralgummotivo,nãotenhaentendidomuitobemcomoascoisas
funcionam,relaxe,prossigacomaleituraetenhaacertezaque,ao/f_inaldoprocesso,
vocêserámaisumconhecedordosmistériosprofundosdowebdesignresponsivo!
/one.oldstyle./five.oldstyle P/a.sc/r.sc/a.sc /a.sc/p.sc/r.sc/o.sc/v.sc/e.sc/i.sc/t.sc/a.sc/r.sc /m.sc/e.sc/l.sc/h.sc/o.sc/r.sc /e.sc/s.sc/t.sc/e.sc /l.sc/i.sc/v.sc/r.sc/o.sc
Paraentendereabsorverbemoconteúdo,ébomquevocêjáestejaumpoucofamili-
arizadocomHTMLeCSS.SaberumpoucodeJavaScriptédesejável,nãoparaacom-
panharosconteúdosprincipaisemaisimportantesdolivro,massimparaacompa-
nharoconteúdocomplementar,dicasextras,o p l u sdodesignresponsivo,quemuitas
vezesprecisadeumjsparaserfeito.
Mas/f_iquetranquilo!Nãoénamaioriadastécnicasqueissoéprecisoe,quando
ofor,tratam-sedemateriaisnão-essenciais,semosquaisvocêaindaconseguiráen-
tendercomofuncionaodesignresponsivoparaweb.
Então,sevocêjáépro/f_issionaldoramoejápassou(ouseencontraouseinte-
ressa)pelaáreadefront-end,nãoterámaioresproblemasaocontinuarcomaleitura.
Sevocêédoback-endenãoseinteressatantopeloqueacontece“lánafrente”,
acreditoque,aindaassim,poderáaproveitarosconteúdos,dadoque,geralmente,
/one.oldstyle/five.oldstyle

## Página 24

/one.oldstyle./five.oldstyle. Paraaproveitarmelhorestelivro CasadoCódigo
mesmoopro/f_issionalnãosendoexclusivamentealocadoaumaáreadeatua ção,co-
nhece,pelomenos,as“nuances”dotrabalhodosoutroscolegasdeequipe.
Caso seja você um praticante-militante de web design, pro/f_issional de usa-
bilidade, UX e a/f_ins, então, ou você dá uma lidinha em alguns tutoriais sobre
HTML/CSS(casojánãosaibaalgumacoisa)ou,/f_iquesabendodesdejá,seuapro-
veitamentomaiorserásobrecomoplanejarumsite,desdesuaconcep ção,paraser
responsivo-principalmente,na/f_iloso/f_iamobile /f_irst,queseráapresentada-,jáque,
desdequesejaprecisoouacordadonaequipeque“tal”ou“qual”projetocontará
comwebdesignresponsivo,seráobriga çãosua(oudaequipeaqualvocêfa çaparte)
pensareapresentarassolu çõesvisuaisparaosdiferentes“breakpoints”dodesign.
Querdizer,nãoimporta,tanto,emqueáreadentroda“linhadeprodu ção”de
desenvolvimentowebvocêseencontrenomomento. Oquedeve/f_icarclaroéque
vocêprecisaconheceramarca çãoesintaxedoHTML,sabendoquandoaplicare
paraqueservemasdiferentestagsdalinguagem;deveconhecerCSS,seusseletores
easrespectivaspropriedadesepossíveisvalorese;porúltimo(e,nocaso,menos
importante),umpoucodeJavaScript,casoqueiraseaprofundarumpoucomaisem
designresponsivoeaprenderalgumastécnicasinteressantes,tambémmostradase
explicadasnolivro.
/one.oldstyle/six.oldstyle

## Página 25

C/a.sc/p.sc/iacute.sc/t.sc/u.sc/l.sc/o.sc/two.oldstyle
Princípiosdeumwebdesign
responsivo
JáchegamosacomentarnaIntrodu çãooqueéumwebdesignresponsivo,queé
aquelewebdesignque respondeaquaisquerdispositivos/resolu çõese,devidoauma
sériedecaracterísticastécnicasbemespecí/f_icas,ébemapresentadoemqualquerum
deles.
Vamosnosaprofundarumpoucomaisemsuasorigens,raízeseinspira ções,e
emcomoaplicá-lo.
/two.oldstyle./one.oldstyle C/o.sc/m.sc/o.sc /s.sc/u.sc/r.sc/g.sc/i.sc/u.sc /o.sc /w.sc/e.sc/b.sc /d.sc/e.sc/s.sc/i.sc/g.sc/n.sc /r.sc/e.sc/s.sc/p.sc/o.sc/n.sc/s.sc/i.sc/v.sc/o.sc
Existeumsitemuito,muitobometradicionalnaweb,queéo AListApart :http:
//www.alistapart.com/
Eleexistedesde/one.oldstyle/nine.oldstyle/nine.oldstyle/eight.oldstylee,comopassardosanos,nuncadeixoudebrindarseus
leitorescomartigoselivrosdeexcelentequalidade.

## Página 26

/two.oldstyle./two.oldstyle. Atrincatecnológicadowebdesignresponsivo CasadoCódigo
UmdosescritoresdoAListAparté EthanMarcotte que,emmeadosde/two.oldstyle/zero.oldstyle/one.oldstyle/zero.oldstyle,
publicouumartigointitulado Responsive Web Designquemudaria,parasempre,a
formacomosefazdesignparaweb.
http://www.alistapart.com/articles/responsive-web-design/
Numatraduçãolivre,esteartigocome çaassim:
"O controle que os designers têm no meio impresso e, muitas vezes, desejam ter
no meio web, é simplesmente um re/f_lexo da limitação da página impressa. Devemos
aceitar o fato de que a web não tem as mesmas restrições e projetar (o web design) para
essa /f_lexibilidade”
E,nodecorrerdoartigo,Ethanexplicaseusconceitosesugestões(usandotecno-
logiaquejáeraexistenteàépocadesuapublica ção)paraqueaspáginasfossempro-
jetadasusandooqueelechamoude webdesignresponsivo.Atéumsitedeexemplo
foimostradonoartigo(http://ow.ly/ate/nine.oldstyleK),oquedeixouacomunidadededesen-
volvedoresempolvorosa!
Inspiradoporconceitosdearquiteturae/f_iloso/f_ia,apropostadeEthancoma
publicaçãodaqueleartigofoimostrarumconjuntodetécnicasquegarantemres-
ponsividadeaumwebdesign.
Devidoaoenormefeedbackpositivoeàânsiadacomunidadepormaioresex-
plicaçõesepormenoressobreoassunto,noanoseguinte,foilan çadoolivroque,
porrazõesóbvias,levouomesmonomedoartigoquerevolucionaraamaneirade
sefazerdesignnaweb:o ResponsiveWebDesign.
E,comonãopoderiadeixardeser,muitoda“inspira ção”destelivroveiodo
quefoicompartilhadoporEthanemseusescritos.Portanto,nadamaisnaturaldo
queprestarnossahomenagemaohomemqueliberouparaomundoenergiasde
conhecimentowebprofundo,baseandováriosdosconteúdosqueaquiconstamem
seusensinamentos.
/T_hank you, Ethan!
/two.oldstyle./two.oldstyle A/t.sc/r.sc/i.sc/n.sc/c.sc/a.sc /t.sc/e.sc/c.sc/n.sc/o.sc/l.sc/oacute.sc/g.sc/i.sc/c.sc/a.sc /d.sc/o.sc /w.sc/e.sc/b.sc /d.sc/e.sc/s.sc/i.sc/g.sc/n.sc /r.sc/e.sc/s.sc/p.sc/o.sc/n.sc/s.sc/i.sc/v.sc/o.sc
Paraconseguirdesenvolverumdesignresponsivoparaaweb,/three.oldstyletecnologiasprinci-
pais(oumodosdeaplicaressastecnologias,sepreferir)estãoenvolvidas:
/one.oldstyle) Layout/f_luído;
/two.oldstyle) Imagenserecursos/f_lexíveis;e
/one.oldstyle/eight.oldstyle

## Página 27

CasadoCódigo Capítulo/two.oldstyle. Princípiosdeumwebdesignresponsivo
/three.oldstyle) MediaQueries.
Desenvolversitescom layouts/f_luidos(/f_luent layout,tambémchamadosde grids
/f_lexíveis),ouseja,desdeaconcep çãodoprojeto,primarpelanãoespeci/f_ica çãode
medidas/f_ixasnolayoutdoprojeto,tornapossívelquehajaumaadapta ção“natural”
eautomáticadoqueseapresentanatela.Portanto,sejaqualforaresolu çãododis-
positivoquefezoacesso,evitamosbarrasderolageminconvenientese/ouconteúdos
“cortados”,nãoexibidosemsuacompletude.
Masdenadaadiantariaseoconteúdoseadaptasseàsmaisdiferentesresolu ções
seasimagens(eoutrosrecursos)dositetambémnãoseadaptassemenãofossem
/f_lexíveis,nãoéverdade?Então,atravésdetécnicasvariadas,épossívelfazercomque
os assets(recursoscomoimagens,vídeos,etc)dositetambémsejam/f_lexíveispara
garantirqueaexperiênciadovisitanteprimepelaexcelência,independentemente
dodispositivoqueestejausando.
Paraasmaisdiferentesresolu çõesdosaparelhos,asnecessidadesedesejosde
usodositepodemsealterar.A/f_inal,umapessoanãoestariaerradaaoimaginarque
alguémqueacessaumsiteatravésdeumcelular,cujatelanãotenhaumaboaresolu-
ção,nãoprecisadeuma sidebar(menunalateral).Oqueesseusuárioprovavelmente
estáprocurandosãoosconteúdosprincipais;então,nadamaisjustoquenãoonerara
visitacomaexibi çãodeumabarralateral.Asop çõespresentesna sidebarpoderiam,
porexemplo,seremapresentadasno/f_imdetodooconteúdo.
Écomas MediaQueriesqueépossívelocultar,fazeraparecerereposicionarele-
mentoseintera çõesconformearesolu çãoatualqueestejasendousadanomomento
davisitação. A/f_inal,ositenãoprecisa(e,naverdade,nãodeve)ter,exatamente,a
mesmaaparênciaedisposi çãodeseuselementosemqualquerresolu ção.UmiPad,
umcelularNokiaeummonitorde/two.oldstyle/seven.oldstylepolegadaspossuemespaços,resoluçõesene-
cessidadesbemdiferentes.
Sabendousaressa trinca tecnológicaépossívelcriardesignsresponsivosparaa
web. Éobjetodestelivrofazeraapresenta çãoerespectivasexplica ções(eintegra-
ções)decadaumadessasprincipaistecnologias.Mas,antes,éinteressanteteruma
noçãodealgunsproblemascomunsquetrouxeramosdesenvolvedoreswebatéeste
pontoeconheceralgunsfatosnotáveissobredispositivos,aweb,arela çãoentreestes.
/two.oldstyle./three.oldstyle R/e.sc/s.sc/o.sc/l.sc/u.sc/ccedilla.sc/otilde.sc/e.sc/s.sc /d.sc/e.sc /t.sc/e.sc/l.sc/a.sc
Comosepôdeverquandoapresentamosalgumaestatísticasdomundo mobilena
seção/one.oldstyle./one.oldstyle,osnúmerosenvolvendoessenovomarcotecnológicosãosurpreendentes!
/one.oldstyle/nine.oldstyle

## Página 28

/two.oldstyle./three.oldstyle. Resoluçõesdetela CasadoCódigo
Eestesnúmerosmostram,também,queatendênciaéquemaisemaisdispositivos
surjam,muitosacadaano.Então,juntandoosjáexistentescomosquesãolan çados
acadaperíodoprogramadodetempo,temosumbocadode devicesparaprestar
atenção...Ounemtanto?
Demaneiraóbvia,éhumanamenteimpossívelprestaraten çãoedarsuportea
todoequalquerdispositivomobileexistenteequeestejaporexistir. Naverdade,
neméprecisoqueissosejafeito.
Oatual(enãoe/f_iciente)paradigmadeacessomultidispositivo
Semessaideiaemmenteparaodesenvolvimento,mesmoantesdesecome çar
aescreveroprimeirocaracteredecódigo,oquesefazéoseguinte:escolhe-seuma
técnica,qualquer,paraidenti/f_icarqualéaresolu çãododispositivo(ouodispositivo,
emsi)e,apartirdoresultado,carrega-serecursoscondizentes(CSS,JavaScript,ima-
gens,etc)àrealidadedaquele device. Algoquetambémnãoédifícildeacontecer:
apessoaéredirecionadaparaumsiteàparte,feitoparaumaresolu çãooudisposi-
tivoespecí/f_ico-sepreferir:um“sitecompatível”...Nãoéprecisoescreverparágrafos
in/f_indáveissobreoscustosdeproduçãoeretrabalhoenvolvidosaoseusarestaabor-
dagem,nãoéverdade? Semcontarque,muitasvezes,queríamosumaexperiência
parecida,enãoalgocompletamentediferentedosite“normal”.
Oequívococomuméaindanãoterentendidoque,naverdade,oqueimporta
nãoéotamanhofísicodatelaouodispositivo,emsi,massua resolução! Tendo
aatençãovoltadaàs r e s o l uções,épossível,comfacilidademuitomaior,desenvolver
paraumagamaincríveldedispositivos,semsepreocuparcom,necessariamente,
quedispositivossãoessesouotamanhofísicodesuastelas.
Ouvocêquerterqueatualizarseus scriptsdeidenti/f_icaçãode devicessempreque
omaisnovo smartphonedomomentoforlan çadonopróximomês?Claroquenão!
E,certamente,qualquerpro/f_issionaldaáreadedesenvolvimentoweb,passandopelo
estagiáriodeHTMLaogestordonegócio,tambémnão.
Paraseterumaideia,peguemosumapesquisafeitacomaparelhosvendidos
entre/two.oldstyle/zero.oldstyle/zero.oldstyle/five.oldstylee/two.oldstyle/zero.oldstyle/zero.oldstyle/eight.oldstyle,quecontemplouanálisede/four.oldstyle/zero.oldstyle/zero.oldstyledevicesdiferentes(http://ow.ly/
b/seven.oldstyle/two.oldstyleAt),comintençãodelevantarasprincipaisresolu çõesdedispositivosusadospara
acessoàweb,tambémlevandoemconsidera çõesasorienta çõesdessesdispositivos:
portrait(retrato)e landscape(paisagem).
Constataçõesinteressantesforamfeitas,como,porexemplo,adiferen çadeta-
manhoentreomenoreomaiordispositivoqueparticiparamdaamostra,quechega
/two.oldstyle/zero.oldstyle

## Página 29

CasadoCódigo Capítulo/two.oldstyle. Princípiosdeumwebdesignresponsivo
aserdemaisde /two.oldstyle/three.oldstylevezeseoaumentoconsiderávelde ppi(“Pixels per inch” ,densidade
de pixels)conformeoavan çodastecnologias.
Para/f_icarmaisclaroetrazeroentendimentocomexemplosmaisconcretos,to-
memosoexemplodealgunsdispositivos,especi/f_icamente,paraseterno çãodasdi-
ferençasderesolu çãoquepodemexistir.Vejamosquaisasresolu çõesespecí/f_icasde
algunsdosaparelhoscomuns,quepodemserencontradosemqualquerlugar.Para
facilitar,ográ/f_icodisponibilizadonoblogWebDev-il(http://ow.ly/bazAV),fazuma
separaçãológicados devicesporSistemaOperacional.
/two.oldstyle/one.oldstyle

## Página 30

/two.oldstyle./three.oldstyle. Resoluçõesdetela CasadoCódigo
Percebaque,nestegrá/f_ico,existem/two.oldstyleindicaçõesparaiPhone:umaéoretângulo
querepresentaaresolu çãode/three.oldstyle/two.oldstyle/zero.oldstylex/four.oldstyle/eight.oldstyle/zero.oldstyleeomaiordetodos,/six.oldstyle/four.oldstyle/zero.oldstylex/nine.oldstyle/six.oldstyle/zero.oldstyle,também! A
diferençaéqueaoiPhone/four.oldstyletemumaresoluçãobemsuperior.EoiPhone/five.oldstyleaumentou
aindamaisessadiversidade,comseus/six.oldstyle/four.oldstyle/zero.oldstylex/one.oldstyle/one.oldstyle/three.oldstyle/six.oldstylepixels.
Oqueimportanãoéotamanhofísicodatelaouodispositivoemsi,massimsua
resolução.Fixou?
/two.oldstyle/two.oldstyle

## Página 31

C/a.sc/p.sc/iacute.sc/t.sc/u.sc/l.sc/o.sc/three.oldstyle
layout/f_luído
U mlayout/f_luídoou,comooriginalmentechamadoporEthanMarcotte, grid/f_lexí-
vel,éoprimeiropassoparadesvendarosmistériosdowebdesignresponsivo.Para
seconseguirumlayout/f_luídonumprojetoweb,aprincipalmedidaasertomadaé:
nãousarmedidasabsolutasnoCSS !
Aliás,vocêmesmo,aocome çaracodi/f_icarseusprimeirosexemplosdeHTML,
jánotouisso,masapostoqueesqueceu!Ounãoselembradecomoaqueleparágrafo
cheiode“ Lorem ipsum...”seadaptavaaqualquertamanhodejaneladonavegador?
Eporquê?Porquenãohavianenhumaespeci/f_ica çãodelargura!Simplesassim.

## Página 32

/three.oldstyle./one.oldstyle. TiposdemedidaemCSS CasadoCódigo
Portanto,aoespeci/f_icartamanhos,espaçamentos,margens,paddings,en/f_im,ao
estipularqualquermedidareferenteaolayoutdaspáginasdosite,éprecisousarva-
loresrelativos,como porcentagenseems,comoveremos.
Antesdeprosseguirmos,vamosverquaissãoostiposdemedidasemCSS.
/three.oldstyle./one.oldstyle T/i.sc/p.sc/o.sc/s.sc /d.sc/e.sc /m.sc/e.sc/d.sc/i.sc/d.sc/a.sc /e.sc/m.scCSS
EmboraexistamoutrostiposdemedidasemCSS,vamosbasearestaexplica çãonas
/four.oldstyleprincipais:pixels,pontos,porcentagenseems.
• Pixel(px). Éaunidadedemedida/f_ixamaisusadanasCSS.Comumente
falando,umpixeléumpontoindivisívelnateladeexibi çãodeumdispo-
sitivo-embora,maisrecentemente,tenhamosvários“tiposdepixel”(http:
//ow.ly/atmIu).Nãoraramente,webdesignerspreferemusarestetipodeme-
didaparafazerumaestruturaHTML/CSSem p i x el p e r f e c t,nãomedindoes-
forçosparaestruturarseusdocumentosparaque/f_iquemidênticosàimagem
dowebdesign.
/two.oldstyle/four.oldstyle

## Página 33

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
• Ponto(point). PontossãotradicionalmenteutilizadosparaCSSsdeimpres-
são. Umpontoéiguala/one.oldstyle//seven.oldstyle/two.oldstylepolegadas. Assimcomoospixels,pontossão
unidadesdetamanho/f_ixo.
• Ems(em). O“ em”éumaunidadeescalável.Quandosetratadotamanhoda
fonte,/one.oldstyleeméigualaotamanhoatualdafontedoelemento-pai.Porexemplo,se
otamanhodafontedoelementoé/one.oldstyle/two.oldstylept,/one.oldstyleeméiguala/one.oldstyle/two.oldstylept.E m ssãoescaláveis
pornatureza./two.oldstyleemseriaiguala/two.oldstyle/four.oldstylept,/zero.oldstyle./five.oldstyleseria/six.oldstylept,etc.
• Porcentagem(/percent.oldstyle).Aunidadeporcentoémuitoparecidacomaunidade“ em” ,
maspossuialgumasdiferen çasfundamentais.Emprimeirolugar,oatualta-
manhodafonteéiguala/one.oldstyle/zero.oldstyle/zero.oldstyle/percent.oldstyle(ouseja/one.oldstyle/two.oldstylept=/one.oldstyle/zero.oldstyle/zero.oldstyle/percent.oldstyle).Duranteousodaunidade
porcento,otextopermanecetotalmenteescalávelparadispositivosmóveis.
Comofoivisto,adiferen çabásicaentrepontos,pixels, emseporcentagenséque
osdoisprimeirossãounidadesdemedida/f_ixaseosdoisúltimos,variáveis. Eles
sãorelativos,escaláveiseseadaptamemantêmrela çõesdetamanhocomoutros
elementosdeumdocumento-elespossuemum contexto.
Portanto,/f_icaclaroqueusarptsoupxsnãoéoadequadoparadesignsresponsi-
vos(numprimeiromomento,jáque,comapráticae/ouexperiênciae/oudemanda
doprojeto,podesernecessárioespeci/f_icaralgunsvalores/f_ixosemdeterminadassi-
tuações),oquenosdeixacomas/two.oldstyleoutrasopções. Masqualadiferen çaentreusar
emsouporcentagens?
EmsxPorcento
Devido às características que foram analisadas previamente, parece que é a
mesmacoisausaremouporcentagem. Entretanto,existemalgumaspequenasdi-
ferenças.
Oimportanteésaberque,quandofalamosemlayout,marcarunidadescompor-
centoforneceumaexibi çãomaisconsistenteeacessívelparaosvisitantes.Quando
ascon/f_iguraçõesdeexibi çãodoclientesealteram,asmedidasmarcadascom/percent.oldstyleseal-
teramdemaneiramaisrazoável,permitindoquealegibilidadesejapreservada,bem
comoaacessibilidadeeodesignvisual.
Portanto,apesardeserpossívelusarqualquerumdostipodemedidasrelativas,
émeioqueconsensoentreosdesenvolvedores-e,acredito,este“consenso”surgiu
atravésdemuitostesteseexperiênciacomresponsividade- usarporcentagempara
lidarcomtamanhosnolayout (larguras,margens,espa çamentos,etc)e usarems
/two.oldstyle/five.oldstyle

## Página 34

/three.oldstyle./two.oldstyle. Afórmulamágicadowebdesignresponsivo CasadoCódigo
paralidarcomfontes . empodeatéserusadoforadetextos,masvaisersempre
umamedidarelativaao font-size;jáoporcentoérelativoao font-sizequando
usadaem font-size,mas,quandousadacomoutrasmedidas,é relativaàlargura
doelemento-pai.
/three.oldstyle./two.oldstyle A/f.sc/oacute.sc/r.sc/m.sc/u.sc/l.sc/a.sc /m.sc/aacute.sc/g.sc/i.sc/c.sc/a.sc /d.sc/o.sc /w.sc/e.sc/b.sc /d.sc/e.sc/s.sc/i.sc/g.sc/n.sc /r.sc/e.sc/s.sc/p.sc/o.sc/n.sc/s.sc/i.sc/v.sc/o.sc
Quando,desdesuaconcep ção,umprojetotemporobjetivocontarcomdesignres-
ponsivo,éimportantequeosdesenvolvedoresenvolvidospensemde“formarela-
tiva”,ouseja,emimplementarestelayoutsevalendodemedidasrelativasnoCSS.
Relembrando,deve-sepensarematribuirasmedidasdolayoutem porcentagense
otamanhodefontesem emsaoinvésdepixels.
Se,na“antigamaneiradepensar”,houvesse,porexemplo,umtítulocomtama-
nhodefontede/two.oldstyle/four.oldstylepx,então,seriaprecisoconverteressamedidaemem.E,sevocê
estáprestandoaten çãonosconteúdosquenostrouxeramatéesteponto,vocêdeve-
riaestarseperguntando: "Mas como converter para em e continuar com a aparência
de /two.oldstyle/four.oldstylepx?”.Eessa,meucarocolegadepro/f_issão,é,realmente,aperguntacertaase
fazer!
Existeuma fórmulapararealizaressecálculo.Umaformasimpleserápidade
realizaraconversãodetamanhosabsolutosparatamanhosrelativosemlayoutspara
aweb.Enãoénadacomquevocêdevasepreocuparousentirumarrependimento
profundoaoimaginarquedeveriaterprestadomaisaten çãoàsaulasdematemática
daépocadocolégio.Éumafórmulatãosimplesque,porsisó,contémabelezaea
elegânciadodesignresponsivo.
SeestivéssemosemalgumpontopróximodaIdadeMédia,algunsdiriamque
essaéumafórmulamágica!Mas,não,nãoémagia.
F/oacute.sc/r.sc/m.sc/u.sc/l.sc/a.sc /m.sc/aacute.sc/g.sc/i.sc/c.sc/a.sc /d.sc/o.sc /w.sc/e.sc/b.sc /d.sc/e.sc/s.sc/i.sc/g.sc/n.sc /r.sc/e.sc/s.sc/p.sc/o.sc/n.sc/s.sc/i.sc/v.sc/o.sc
Alvo/Contexto=Resultado
• Alvo.Elemento-alvocomamedidaatual;
• Contexto.Ondeoelemento-alvoestá(baseadonoelemento-pai);
• Resultado.Ovalorrelativoqueseestáprocurando.
/two.oldstyle/six.oldstyle

## Página 35

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
Comessafórmularápida,épossívelrealizarcálculossimplesparasaberoresul-
tadodeconversõesdemedidasabsolutasdoCSSparamedidasrelativas.Eissovale
tantoparaocálculode tamanhodefontes -existeumacertaconven çãodequeo
tamanhopadrãodefontesem browsers desktopéde/one.oldstyle/six.oldstylepx-,quantoparamedidasde
layout!
Então,voltandoaonossoexemplo,agora/f_icasimplesdescobrirqualaequiva-
lênciaememsde/two.oldstyle/four.oldstylepx.Bastaaplicarmosafórmula.
/two.oldstyle/four.oldstyle//one.oldstyle/six.oldstyle=/one.oldstyle,/five.oldstyle
Ouseja,aopegarnossoalvo(otítulo)de 24pxedividirpelocontexto(nocaso,
seuelemento-pai,queé body,possuitamanhofontede/one.oldstyle/zero.oldstyle/zero.oldstyle/percent.oldstyle,ou,nocaso,16px),
temoscomoresultado/one.oldstyle,/five.oldstyle. Comoestamostratandodetamanhorelativodefontes
emCSS,oresultado/f_inalé 1.5em.
Imaginemosquehajaumlinkdentrodotítulo,que,noplanejamento,teria 11px
detamanho. Éprecisoconverterissoparamedidarelativa. Aplicandoafórmula
obtemos 11 / 16 = 0,6875 ,certo? Errado!
Jáqueolinkseencontradentrodotítulo, ocontextomudou! Agora,oelemento-
alvonãoestámaisno“contextogeral”dapágina( body). Então,paraconseguiro
resultadocorreto,avariáveldecontextodafórmulamuda.
/one.oldstyle/one.oldstyle//two.oldstyle/four.oldstyle=/zero.oldstyle,/four.oldstyle/five.oldstyle/eight.oldstyle/three.oldstyle/three.oldstyle/three.oldstyle/three.oldstyle/three.oldstyle/three.oldstyle/three.oldstyle/three.oldstyle/three.oldstyle/three.oldstyle/three.oldstyle
O elemento que, em medidas absolutas, deveria ter11px, está dentro do
contexto do título (que, em medidas absolutas, teria24px), que resulta em
0.45833333333333em.
EthanMarcottesugereque,quandooresultadodadivisãocontivertantosnúme-
rosdepoisdavírgula,paranão/f_icarmostentadosaarredondareusarumnúmero
“maisenxuto”,deixandooresultadocomtantosnúmerosquantosuacalculadora
conseguiuexibir.Noentanto,oAutorcortapra/f_icarcom/four.oldstylenúmerosdepoisdavír-
gulaenuncateveproblemas.Fa çaseusprópriostesteseoptepeloquelhetrouxer
melhoresresultados.
/three.oldstyle./three.oldstyle E/x.sc/e.sc/m.sc/p.sc/l.sc/o.sc /d.sc/e.sc /u.sc/m.sc /l.sc/a.sc/y.sc/o.sc/u.sc/t.sc /f.sc/i.sc/x.sc/o.sc
Comovocêjádeveterpercebidoaestaalturadocampeonato,épossívelaplicarnossa
fórmulamágicatantoparadescobriraequivalênciarelativadetamanhosdefontes,
quantoparadesenvolverumlayout/f_luído. Paraummelhorentendimento,vamos
nosbasearemummodelodepágina/f_ictícia,queajudarábastanteparaaplicarmos
osconceitosqueestamosvendo.
/two.oldstyle/seven.oldstyle

## Página 36

/three.oldstyle./three.oldstyle. Exemplodeumlayout/f_ixo CasadoCódigo
HTMLdeumlayout/f_ixo
Vejamosumexemplodoqueencontramosnodia-a-diadanavega çãonaweb:
umsitecom layout/f_ixo.Ainten çãoémostrar,atravésdeum layoutsimples,amar-
caçãodeHTMLeCSSqueseencontracomumente,poraí.
HTML /e.scCSS
Oobjetivodestelivronãoédiscutirteorias,técnicasoucondutasdees-
critadeHTMLeCSS.Questõescomoespa çamentos,usoounãodeclas-
sesouIDs,espa çamentos,identação,etc,fogemdoescopodolivro.
Sevocêquerconhecermais,nãodeixedeconhecerolivrodoLucas
Mazza,deHTML/five.oldstyleeCSS/three.oldstyle,tambémpelaCasadoCódigo.
Então,imaginemosumapáginadeumsitecom layout/f_ixoquesepare çacom
isso:
SeuHTMLésimples-comotodoHTMLdeve(ria)ser-enãoapresentanada
diferentedoconvencional.ProvavelmentevocêjádeveconhecerHTML,mas,para
deixarbemclarosobreafun çãodenossocódigo,vamosaumasucintaexplica ção.
/two.oldstyle/eight.oldstyle

## Página 37

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
Primeiramente,temostodaaestruturadapágina“englobada”porumcontêiner.
Essaéumatécnicamuitocomum:
<div class="container">
[...]
</div>
Existem/three.oldstyledivisõesprincipais,dentrododiv container:umcabe çalho,oespa ço
paraainser çãodosconteúdosprincipaiseumrodapé.Novamente,semnenhuma
novidadeparaastécnicasmaisbásicasdeestrutura çãoemHTML:
<div class="container">
<header class="header">
[...]
</header>
<div class="content">
[...]
</div>
<footer class="main-footer">
[...]
</footer>
</div>
NestemodelodeestruturaHTML, headere footercostumamsempretero
mesmoconteúdo, independentementedapáginadositequeestásendovisitada
nomomento. Portanto,/f_icaóbvioqueosconteúdosprincipaisdosite/f_icamem
content.
Dentrode content,tambémtemos/two.oldstyle“porçõesdeconteúdo":apartedosconteú-
dosprincipais,propriamenteditos,euma sidebar-tambémconhecidacomo“barra
lateral”.
<div class="container">
<div class="content">
<div class="content-main">
[...]
</div>
<aside class="content-sidebar">
[...]
/two.oldstyle/nine.oldstyle

## Página 38

/three.oldstyle./three.oldstyle. Exemplodeumlayout/f_ixo CasadoCódigo
</aside>
</div>
</div>
Portanto, a estrutura deste site simples, demonstrada através desta
página-exemplo, basicamente teria a mudança de conteúdos acontecendo em
content-main. Nestapágina,háumachamadaparaoconteúdomaisrecenteou
maisimportanteemdadomomento(aquechamamos,nocaso,de hero),seguido
dechamadasparaoutrosconteúdos,cadaumamostrandoseurespectivotítulo,um
resumo/chamarizeumlinkparaseacessarapágina,naíntegra.
Comoaestruturafoiidealizadaparasermantidaeserepetiremtodasaspáginas
dosite,paraosoutrostiposdepáginas,bastaalteraroselementosHTMLdentrode
content.
Nocaso,essapáginadeexemplofoiestruturadacom/six.oldstyledestas“chamadas”,mas
aestruturapermitequesejamfeitasquantassejamprecisas(preferencialmente,em
quantidadepar,paramantersuaestruturadeapresenta ção).
<div class="content">
<div class="content-main">
<article class="hero">
<h2>
Título Importante
</h2>
<p class="brief">
Descrição ou resumo de um conteúdo
importante, que precisa ser mostrado para evidenciar
a notoriedade deste conteúdo.
</p>
</article>
<div class="last-contents">
<article class="last-content-call">
<h2 class="secondary-title">
Título de Conteúdo
</h2>
<p class="brief">
Resumo ou
descrição deste conteúdo.
/three.oldstyle/zero.oldstyle

## Página 39

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
Deve ser algo que chame a atenção!
</p>
<a href="#">Leia mais </a>
</article>
<article class="last-content-call">
<h2 class="secondary-title">
Título de Conteúdo
</h2>
<p class="brief">
Resumo ou
descrição deste conteúdo.
Deve ser algo que chame a atenção!
</p>
<a href="#">Leia mais </a>
</article>
[...]
</div>
</div>
<aside class="content-sidebar">
<nav class="main-nav">
<ul>
<li><a href="#">Menu 1 </a></li>
<li><a href="#">Menu 2 </a></li>
<li><a href="#">Menu 3 </a></li>
<li><a href="#">Menu 4 </a></li>
<li><a href="#">Menu 5 </a></li>
<li><a href="#">Menu 6 </a></li>
</ul>
</nav>
</aside>
</div>
Ocódigocompletopodeservistonestelink:https://gist.github.com//three.oldstyle/six.oldstyle/three.oldstyle/zero.oldstyle/six.oldstyle/zero.oldstyle/five.oldstyle
Atéentão,tudonormal. Inclusivequandoalguémredimensionaajanela-ou,
oqueémaiscomum,acessausandoumaresolu çãomenordoqueamostradano
/three.oldstyle/one.oldstyle

## Página 40

/three.oldstyle./three.oldstyle. Exemplodeumlayout/f_ixo CasadoCódigo
exemplo-,oconteúdocontinuanomesmolugar,eventuaisbarrasderolagemdo
navegadoraparecem.En/f_im,tudonormalecomooesperado:
Quandoalguémacessaatravésdeumdispositivomóvel,principalmentecomos
quetemosatualmente,opróprio deviceseencarregadefazersuamágicaparaque
todoositesejaapresentadonatelinhacomoseaplicasseum zoom outneletodo.
Comisso,apessoatemumavisãogeraldosite(poroestarvendo“pequenininho”)
e,casoalgosejadoseuinteresse,atravésdeumbotãopressionadoougestofeitona
teladodispositivo,conseguedarum zoom inevermelhoroqueédeseuinteresse
nomomento.
Apartirdomomentoqueapessoajáviuoquequeria,ouvai“deslizando”osite
paraencontraroutrascoisasdointeresse,oudáum zoom outparaternovamente
a“visãotopográ/f_ica”.Esseprocessopodeacontecermaisvezes,casoousuárionão
consigaencontrarainforma çãocomrapidez.
Essafacilidadequeosdispositivosmóveisnosoferecemrealmentefacilitaopro-
cessodenavega ção,jáquenemtodosossitesestãotecnicamentepreparadospara
apresentarseusconteúdosnasmaisdiversasresolu çãopossíveis. Sim,realmenteé
umprocessoque,depoisdealgumtempo,écansativo,repetitivoe,concordemos,
nãoatendeaospadrõesegostosdeusabilidadeumpoucomaisrigorosos.
/three.oldstyle/two.oldstyle

## Página 41

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
Oidealéqueolayoutdosite-e,logicamente,seuconteúdo-sejabemapresen-
tadoemtodosostiposderesolu ção. Odesejável-e,muitasvezesecadavezcom
maisfrequência,o esperado-équeositesejainteligenteobastanteparaapresentar
omelhorconteúdoatravésdamelhormaneirapossível,nãoimportandoqualdispo-
sitivoouqualresolu çãoestejamsendoutilizadosnomomentodoacesso.
CSSdeumlayout/f_ixo
EsseHTMLdeexemploquemostramosdeveseracompanhadoporumpouco
deCSS,eéjustamenteissoqueiremosabordaragora.Comovocêverá,éumCSS
quenãotemabsolutamentenadademais,servindoparadarumaleveestilizadae
apresentarnossapáginadeumlayout/f_ixodeumamaneiraumpoucomaisagradável
eorganizada.
ComeçaremoscomaformamaisbásicadeCSSreset,servindosomentepara
ilustraranecessidadedequehajaumesfor çoinicialnacria çãodasfolhasdeestilode
umapadronizaçãoentreosdiferentesnavegadores. Pessoalmentepre/f_iro,aoinvés
deumreset,um“padronizadordeCSS”,talcomooCSSquepodemosencontrar
noHTML/five.oldstyleBoilerplate(http://html/five.oldstyleboilerplate.com/);mas,para/f_insdeexemplo,
vamostrabalharcomumresetbásico.Alémdisso,vamoscolocarumafontecomum
paraoselementos.
* {
margin: 0 ;
padding: 0 ;
}
html {
font-family: Arial, Helvetica, sans-serif;
}
Começandoamexernoselementosespeci/f_icadosnoHTML,vamostrabalhar
como .container,queéo w r a pdetodaapágina.Aideiaétermosumsitecentrali-
zado,bastantecomumnosdiasdehoje.Alargura“ideal”paratalmodelodepágina
nãoexiste,portanto,podemosarbitraroquemelhornosaprouver.
.container {
margin: 0 auto;
width: 960px ;
}
/three.oldstyle/three.oldstyle

## Página 42

/three.oldstyle./three.oldstyle. Exemplodeumlayout/f_ixo CasadoCódigo
Aproveitando,vamosmexer,também,notítuloprincipaldestapágina,colo-
candoumtamanhodefonteconsiderávelparaquenãohajadúvidasquantoasua
importância.
h1 {
font-size: 32px ;
}
Comoteremosumapadroniza çãoparaelementosdotipo .brief,nãohámal
algumemjáestilizaresteelemento“genérico”denossosite-exemplo.
.brief {
margin: 5px 0 ;
}
Osconteúdosprincipaisdosite/f_icamem .contentque,porsuavez,abriga
.content-maine .content-sidebar,respectivamente(lembra-sedoSEO?).E,den-
trodeambos,maisestilosparaquenossoexemplo/f_iquenumaestruturainteressante
efuncional.
.content-main {
float: left;
width: 593px ;
}
.hero {
margin: 25px 0 ;
}
.last-contents {
font-size: 12px ;
}
.last-content-call {
float: left;
margin: 15px 15px 15px 0 ;
width: 280px ;
}
.last-content-call .secondary-title {
margin-bottom: 0 ;
/three.oldstyle/four.oldstyle

## Página 43

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
}
.last-content-call .brief {
margin: 5px ;
}
.content-sidebar {
background-color: #F0F0F0 ;
float: right;
padding: 10px ;
width: 322px ;
}
.main-nav ul {
list-style-type: none;
}
.main-nav li {
background-color: #F9F9F9 ;
float:left;
margin: 15px ;
outline: 1px solid #DEDEDE;
text-align: center;
width: 130px ;
}
.main-nav a {
display: block;
padding: 10px ;
text-decoration: none;
}
Por/f_im,temosnosso.main-footerque,nomomento,servesomenteparaexibir
algumasinformaçõesde copyle/f_t,masnadaimpediriadeconterummenusecundá-
rio,comlinksdemenorimportânciaquenossomenuprincipal,localizadonabarra
lateral.
.main-footer {
background-color: #F0F0F0 ;
clear: both;
float: left;
/three.oldstyle/five.oldstyle

## Página 44

/three.oldstyle./three.oldstyle. Exemplodeumlayout/f_ixo CasadoCódigo
font-size: 12px ;
margin: 15px 0 ;
padding: 15px ;
text-align: center;
width: 100% ;
}
Comoprometido,éumCSSbastantesimples,semimplementa çõespolêmicas
e/outécnicasmirabolantesparaconseguirefeitosdiversos. Oobjetivodestelivro
nãoéesse.NossoCSSdeumlayout/f_ixocompletopodeserencontradoem:https:
//gist.github.com//three.oldstyle/six.oldstyle/three.oldstyle/zero.oldstyle/eight.oldstyle/two.oldstyle/eight.oldstyle
Comisso,terminamosnossoarquivo style.cssque,comovocêbemobservou
nocódigocompletodoHTML,éreferenciadoefarácomqueacamadadeconteúdo
recebasuadevidaestiliza ção.Abrindoambososarquivosemumbombrowser,você
serápremiadocomumatelamuitaparecidacom:
Finalizamosoesqueletodenossapáginadeexemplo.Nãofoinadademais,ob-
viamente,mas,nesteponto,vocêpodeestarseperguntando:“Eagora,comotrans-
formaresselayout/f_ixoemumlayout/f_luído?”.Eessaéexatamenteaperguntacerta
asefazer.
/three.oldstyle/six.oldstyle

## Página 45

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
/three.oldstyle./four.oldstyle M/e.sc/t.sc/a.sc/t.sc/a.sc/g.sc /v.sc/i.sc/e.sc/w.sc/p.sc/o.sc/r.sc/t.sc
Veremoscomoconverterumlayout/f_ixoemlayout/f_luído. Primeiro,devemosnos
ateraumdosmaisimportantesdetalhestécnicosquandooassuntoéwebdesign
responsivo:ametatagviewport .
Metatags
Teoricamente,sevocêestálendoestelivro,jádevesaberoqueéuma metatag
HTML.Dequalquerforma,umabreverevisãopodeserútil.
Otermo meta tagé,naverdade,formadopor/two.oldstylepalavrinhasquesejuntampara
darseusigni/f_icado.E,paraentenderestesigni/f_icado,éprecisoentenderas/two.oldstylepalavras,
emseparado:
• Metaéumpre/f_ixogregoquesigni/f_icaalgocomo“após”,“queultrapassa”,“que
engloba”,“queestáalém”.Estenãoéumpre/f_ixoutilizadosomentenodesen-
volvimentoweb;vocêjádeveterouvidoelidopalavrascomo“metabolismo”
e“metamorfose”.Estepre/f_ixometarefere-seà“coisasobreaprópriacoisa”ou,
emoutraspalavras,dadossobredados,informa çãosobreainforma ção.
• T a géumapalavradoinglêsquesigni/f_ica“etiqueta”ou“rótulo”. Tantonos
EUA,noBrasilouemqualquerpartedomundo,etiquetasservemparaiden-
ti/f_icar,nomearemarcaralgooualgumacoisaparaquepossaseridenti/f_icado
e/oucorretamentecatalogado.
Então,juntandoos/two.oldstyletermos,“meta”e“tag”,temosmeta tag,quesão t ag sque
descrevemodocumentowebaqualpertencem(“informa çãosobreainforma ção”);
asmetatagssãoparadescreverinforma çõessobresitesepáginasqueascontém;
informamsobrequalconteúdoestáaliemostrainforma çõesextrasarespeitodeste
conteúdo.
Asmetatagssãocolocadascomoelementos-/f_ilhode headnoHTML.Suasintaxe
obedeceàseguinteconven ção:
<meta name="nome-da-meta" content="conteudo-da-meta">
Então,paraqualquerdasmetatagsexistentesquevocêforusar,aconven ção
paraseuusoéesta,ondeseinforma,primeiramente,dequalmetaseestáinserindo
e,posteriormente,qualvalorsedá.
NodocumentodoW/three.oldstyleC,“Visualformattingmodel”(http://ow.ly/baEmW),éex-
plicadoque:
/three.oldstyle/seven.oldstyle

## Página 46

/three.oldstyle./four.oldstyle. Metatagviewport CasadoCódigo
"Agentes do usuário de mídia contínua em geral oferecem aos usuários uma view-
port (uma janela ou outra área de visualiza ção na tela) através do qual os usuários
consultam um documento. Os agentes podem alterar o layout do documento quando o
viewport é redimensionado. Quando a viewport é menor que a área da tela em que o
documento é renderizado, o agente deve oferecer um mecanismo de rolagem”
Ouseja,dentrodocontextodedesenvolvimentoweb, viewportéapartevisível
dapáginawebqueérenderizadapelosnavegadores(desprezandopainéis,barrasde
menu,plugins,barraderolagem,etc).
Oqueéametatagviewport
Os browsers mobiletentamexibirpáginaswebfeitassomentepara desktop(no
momento,aimensamaioriadetodaselas)ajustando,automaticamente,o zoomdo
d i s p l a y,eissopodeserproblemáticoparaossitesquejáforamplanejados/otimizados
paratelaspequenas-todososquevocêfaráapartirdaleituradestelivro,certo?
Felizmente,existeumametatagparacontornaressacaracterísticadosnavega-
dores. Éa meta tag viewport. Assimcomoqualqueroutrametatag,elapossuio
formato:
<meta name="viewport" content="">
Sendoque,em content,épossívelespeci/f_icarumadiversidadedeparâmetros
evaloresconformeotipodevisualiza çãoquesecon/f_iguraràspáginas.Sepreferir,
pensequecoma meta tag viewport,épossívelapresentar“resolu çõespersonalizadas”
aosvisitantesparadeterminados devices.Osprincipaisemaisusadosparâmetrosde
contentsão:
• width:de/f_inealargurada viewport;
• height:de/f_ineaalturada viewport;
• initial-scale:de/f_ineaescalainicial( zoom)inicialda viewport.
Sendoqueépossívelusarmaisdeumparâmetro,oumesmotodos,comovalor
de contentda meta tag viewport.
/three.oldstyle/eight.oldstyle

## Página 47

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
Exemplosdeusodametatagviewport
AprópriaApple,queoriginalmentepropôsecolocouemusoa meta tag viewport,
apresentaalgunsexemplosqueelucidambastanteaquestão(http://ow.ly/baGbr).
Vejaumaimagemde 320x356px,apresentadanumiPhone,renderizadausandoas
con/f_igurações defaultde viewport.
Agora,apáginacomo zoomna viewportsendoomesmododaprópriaimagem.
<meta name="viewport" content="width=320,initial-scale=1">
/three.oldstyle/nine.oldstyle

## Página 48

/three.oldstyle./four.oldstyle. Metatagviewport CasadoCódigo
Noentanto,comosetratadecon/f_iguraçõesquepodemserescolhidasconforme
anecessidadedoprojeto,o zoomna viewportpodesermaioroumenordoquea
áreavisível. Seo zoomémaiordoqueaáreavisível,entãoserápossíveldeslizara
telaparavermaisdapágina.
<meta name="viewport" content="width=320,initial-scale=1.5">
/four.oldstyle/zero.oldstyle

## Página 49

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
E,comocitado,tambémépossívelde/f_inirum zoommenorparaa viewport.
<meta name="viewport" content="width=320,initial-scale=0.5">
/four.oldstyle/one.oldstyle

## Página 50

/three.oldstyle./four.oldstyle. Metatagviewport CasadoCódigo
Nosdispositivosmóveis,apessoatambémpodefazer zoom ine zoom outusando
gestos.Quandoissoacontece,elanãoalteraotamanhoda viewport;alterasua escala!
Consequentemente,osgestosde pane zoomnãoalteramolayoutdapágina.
/four.oldstyle/two.oldstyle

## Página 51

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
Acon/f_iguraçãoidealdeviewport
Observandoatabelaanterior,épossívelobservarquediferentescon/f_igura çõesde
viewport(ede zoomna viewport)produzemdiferentesresultadosepossibilidadesde
apresentaçãodositeemcondi çõescontroladas.Masháumaquestãoquenãoajuda
emnadaquandopensamosempossibilidadesdeusode width: paracontemplar
todososdispositivosmóveis,seriaprecisoconheceralarguradecadaumdeles!
OiPhone,nosexemplosdetelaapresentados,temlargurade 320px. Masto-
mandocomoexemplosomenteos devicesexempli/f_icadosnográ/f_icoderesoluçãode
aparelhos,comovistona/f_igura/two.oldstyle./one.oldstyle,seriamuitotrabalhosoidenti/f_icar,marcarefazer
manutençõesnocódigocomtodosospossíveistamanhos.
Mas,nãosepreocupe,pois,maisumavez,atecnologianosauxilia:existeuma
formadeespeci/f_icarautomaticamenteotamanhodo device. Écomoseestivésse-
mosprogramandoeusandoumavariávelque,porpadrão,jácontémalargurado
dispositivoqueestárealizandooacessonaquelemomento.Bastausar:
<meta name="viewport" content="width=device-width">
Issoindicaaonavegadorqueo widthda meta tag viewportéotamanhodalar-
guradodispositivo!
/four.oldstyle/three.oldstyle

## Página 52

/three.oldstyle./four.oldstyle. Metatagviewport CasadoCódigo
Emcondiçõesnormais,tambéméinteressanteque,assimqueapáginarenderize,
nãohajaaltera çõesnaescalainicial.Porisso,juntamentecom width=device-width
da meta tag viewport,ébomusara initial-scaleem 1.Eesta,paraamaioriados
sitesdesenvolvidossegundoa/f_iloso/f_iadodesignresponsivo,éacon/f_iguraçãoideal
deviewport.
<meta name="viewport" content="width=device-width,initial-scale=1">
Valorespossíveisdametatag
Aseguir,vejaatabela-originalmenteexibidanoNokiaDeveloper(http://ow.
ly/baLZP)-comosparâmetrospossíveisda meta tag viewport,exemplosdevalores,
respectivosvalores-padrãoeadescri çãodecadaumdeles.
Lembrandoparatomarcuidadoeprestarbastanteaten çãonousocombinado
dosparâmetrospossíveisparanãocausarefeitosdesagradáveise/ounãoplanejados.
Porexemplo,aoespeci/f_icar:
<meta name="viewport"
content="width=device-width,initial-scale=1,maximum-scale=1">
/four.oldstyle/four.oldstyle

## Página 53

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
Issoimpossibilitariaapessoaqueestáfazendooacessodedar zoomnaspáginas
dosite.Seesseforrealmenteoobjetivopropostonosite,tudobem;mas,repetindo:
atençãoaousarparâmetroscombinados.
/three.oldstyle./five.oldstyle C/o.sc/n.sc/v.sc/e.sc/r.sc/t.sc/e.sc/n.sc/d.sc/o.sc /u.sc/m.sc /l.sc/a.sc/y.sc/o.sc/u.sc/t.sc /f.sc/i.sc/x.sc/o.sc /e.sc/m.sc /l.sc/a.sc/y.sc/o.sc/u.sc/t.sc /f.sc/l.sc/u.sc/iacute.sc/d.sc/o.sc
Construirlayouts/f_luídos(ougrids/f_lexíveis)énossomaiorobjetivoaolerestelivro.
Depoisqueosconceitosaquimostradosjáestiverem internalizadosebastanteprá-
ticativersidofeita,vocêconseguirá,antesmesmodecolocarodedoparadigitara
primeiraregraCSS,jáimaginarcomfocoàconstru çãodelayouts/f_luídos.
Enquantoissonãoacontece,vamosfazerumexercíciosinteressante,quevaicla-
rearbastantealgunsdosprincipaisconceitosdedesignsresponsivos:vamosconver-
terolayout/f_ixoquevimosanteriormenteparaumlayout/f_luído. Como?Simples-
menteaplicandonossafórmulamágicadowebdesignresponsivo!Masprimeiro...
Comovamosmexermaiscomasmedidasqueespeci/f_icamosanteriormente,não
hánecessidadederevisarmostodooCSSmostrado.Aoinvésdisso,vamosnosater
aostrechosquemaisinteressamaonossoexercíciodeconversão,come çandocom
nosso .container.
Alargurade .containeréde 960px. Obviamente,issonãoajudaemnadaa
montagemdeumgrid/f_lexíveldadoque,comojáfoivisto,aprincipaleprimeira
medidaasertomadaparaseconstruirumlayout/f_lexívelé usarsomentemedidas
relativasnoCSS.Revisandonossafórmula: Alvo/Contexto=Resultado .
Nocaso,comosetratadoelementocontêiner,nãotemosumcontextoquesirva
comobase.Então,damesmaformaque,arbitrariamente,especi/f_icamosessalargura
paraoelemento,vamostentarumalarguracommedidarelativaque,quandovista
no browser,separe çaomáximopossívelcomovalorquetemosatualmente.Depois
dealgunstestes,aencontramos:
.container {
margin: 0 auto;
width: 67.5% ; /* +/- 960 */
}
Comopôdeservistonestesucintotrechodecódigo, umaexcelenteprática,
quandoestamostrabalhandocomlayouts/f_luídos,éfazerumcomentárionafrente
dovalorconvertido(ouconstruído)paranãoperderano çãodoqueseestáfazendo.
Ficaadica.
/four.oldstyle/five.oldstyle

## Página 54

/three.oldstyle./five.oldstyle. Convertendoumlayout/f_ixoemlayout/f_luído CasadoCódigo
Emrelaçãoaestevalorde/six.oldstyle/seven.oldstyle./five.oldstyle/percent.oldstyleparaocontêiner,foitotalmenteopcionaleser-
vindosomenteparailustrarnossosite-exemplo.Didaticamente,oAutoracreditaser
interessantepreservaracaracterísticade sitescentralizadosparaaadapta çãoemais
fácilassimilaçãodosconceitosde web designresponsivo.Entretanto,outrasaborda-
genspoderiamtersidousadas:
• Deixaro widthem 960px/f_ixosetransformartodoorestoem/percent.oldstyleeem. Não
tãoe/f_iciente,jáquevai/f_icarcomestalarguraindependentementedatelaser
maioroumenorque 960px.Nãoseriaumasolu çãoresponsiva.
• “Responsivar”pratelas mobilemenoresque 960px,masmanteros 960pxpara
telasmaiores.Usaria-se max-width:960pxecontinuariaigualpararesolu ções
“desktop-like”,mas,aoserexibidoemresolu çõesmenores,vaiseajustarpor
nãoterlargura/f_ixa.
• A solução anterior é responsiva para telas pequenas, mas limita em /nine.oldstyle/six.oldstyle/zero.oldstyle
pra telas maiores. Também é possível responsivar para todas, colocando
width:100/percent.oldstylenocontêiner. Paraprojetosqueprecisam/queiramcontarcom
larguratotalemquaisquerresolu ções,estaabordagemseriaaideal.
Dandoprosseguimento,agoraéprecisopassarotamanhodafontede h1para
medidasrelativas.Acoisaestácome çandoa/f_icarmaisfáciljáque,nestecaso,temos
todasvariáveisdanossafórmula! Lembre-sequeexisteumcertopadrãoentreos
browsersdecolocarotamanhoinicialdasfontesem 16px?Issoétudoqueprecisamos
nomomento.
Querdizer, 32(Alvo)divididopor 16(Contexto)éiguala 2(Resultado)-lem-
brandodaquelaoutraobserva çãoimportante:quandosetratademedidasrelativas
parafontes,usamosamedida em;quandoéparamedidasde layout,porcento.
/* Antes */
h1 {
font-size: 32px ;
}
/* Depois */
h1 {
font-size: 2em ; /* 32 / 16 */
}
/four.oldstyle/six.oldstyle

## Página 55

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
Depois disso, chegamos ao próximo elemento de nosso layout:.content.
Usandonossafórmula,novamente,ouseja: /one.oldstyle/five.oldstyledivididopor/nine.oldstyle/six.oldstyle/zero.oldstyle(amedidadenossa
já/f_inadalargura/f_ixa)éiguala/zero.oldstyle./zero.oldstyle/one.oldstyle/five.oldstyle/six.oldstyle/two.oldstyle/five.oldstyle.Mas,espere!Aoseaplicarestevalorín/f_imo
aolayout,ascoisasnãofuncionamcomooesperado!Bem,comoestamoslidando
comporcentagens,precisamos multiplicarovalorpor/one.oldstyle/zero.oldstyle/zero.oldstyle. Matemágicapura!
/* Antes */
.content {
margin: 15px 0 ;
}
/* Depois */
.content {
margin: 1.5625% 0 ; /* 15 / 960 */
}
Finalmente,nossasmargens/f_luídasestãodevidamentecon/f_iguradaseprontas
paraoquederevier!Comissoemmente,oelemento .content-mainnãovaire-
presentarnenhumperigo. Massevocêestiver,realmente,prestandoaten çãoaos
códigosdeexemplo,poderáestarcomumaperguntaintriganteemsuamente:onde
estáoContexto?!
C/o.sc/m.sc/o.sc /c.sc/a.sc/l.sc/c.sc/u.sc/l.sc/a.sc/r.sc /o.scC/o.sc/n.sc/t.sc/e.sc/x.sc/t.sc/o.sc /e.sc/m.sc /e.sc/l.sc/e.sc/m.sc/e.sc/n.sc/t.sc/o.sc/s.sc /s.sc/e.sc/m.scC/o.sc/n.sc-
/t.sc/e.sc/x.sc/t.sc/o.sc /i.sc/m.sc/e.sc/d.sc/i.sc/a.sc/t.sc/o.sc
QuandooContextoesperadonãoexiste,istoé,oelemento-contêiner
nãoapresentalargurade/f_inida,éprecisoprocurarnoelementoimedia-
tamenteascendenteatéqueseencontreade/f_ini çãodeumalargura.
Ou seja, como o Contexto de.content-main, que é o elemento.content,
nãopossuideclara çãoexplícitadelargura,éprecisoveri/f_icaropróximoelemento-
ascendente.Nocaso,éo .container.Estesimcomdeclara ção(prévia)delargura
de 960px.Porisso,nestecaso,oContextoseráde /nine.oldstyle/six.oldstyle/zero.oldstyle:
/* Antes */
.content-main {
float: left;
width: 593px ; /* Medida maior da Proporção Áurea aplicada ;-) */
/four.oldstyle/seven.oldstyle

## Página 56

/three.oldstyle./five.oldstyle. Convertendoumlayout/f_ixoemlayout/f_luído CasadoCódigo
}
/* Depois */
.content-main {
float: left;
width: 61.7708% ; /* 593 (.content-main) / 960 (.container) */
}
Oelemento .hero(eseudescendente .brief),dentrode .content-main,tam-
bémprecisatersuasmedidasconvertidas. Algointeressanteaselevaremcontaé
queocálculodarelatividadede .hero .brief é 5 / 593 = 0.008431 . Contudo,
apesardeestaserumaciência(pretensiosamente)exata,hámuitodo fatorhumano
envolvido.Portanto,quandoestiverdesenvolvendo grids/f_lexíveisealgumresultado,
apesardepreciso,nãofordoagrado,nãohánadademaisem(casoissosejarespon-
sabilidadesua)arredondarestevalor.
/* Antes */
.hero {
margin: 25px 0 ;
}
.brief {
margin: 5px 0 ;
}
/* Depois */
.hero {
margin: 4.2158% 0 ; /* 25 / 593 */
}
.brief {
margin: 1% 0 ; /* 5 / 593 */
/* = 0.8431%, que, opcionalmente, pode ser arredondado para 1% */
}
Prosseguindo com a conversão dos outros elementos descendentes de
.content-main:
/* Antes */
.last-contents {
font-size: 12px ;
/four.oldstyle/eight.oldstyle

## Página 57

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
}
.last-content-call {
float: left;
margin: 15px 15px 15px 0 ;
width: 280px ;
}
.last-content-call .brief {
margin: 5px ;
}
/* Depois */
.last-contents {
font-size: .75em ; /* 12 / 16 */
}
.last-content-call {
float: left;
margin: 2.5295% 2.5295% 2.5295% 0 ; /* 15 / 593 (.content-main) */
width: 47.2175% ; /* 280 / 593 */
}
.last-content-call .brief {
margin: 1.7857% 0 ; /* 5 / 280 */
}
Aconversãodabarralateral,comtodosseusdescendentes,/f_icaassim:
/* Antes */
.content-sidebar {
background-color: #F0F0F0 ;
float: right;
padding: 10px ;
width: 322px ;
}
.main-nav ul {
list-style-type: none;
}
.main-nav li {
/four.oldstyle/nine.oldstyle

## Página 58

/three.oldstyle./five.oldstyle. Convertendoumlayout/f_ixoemlayout/f_luído CasadoCódigo
background-color: #F9F9F9 ;
float: left;
margin: 15px ;
outline: 1px solid #DEDEDE;
text-align: center;
width: 130px ;
}
.main-nav a {
display: block;
padding: 10px ;
text-decoration: none;
}
/* Depois */
.content-sidebar {
background-color: #F0F0F0 ;
float: right;
padding: 1.0416% ; /* 10 / 960 */
width: 33.5416% ; /* 322 / 960 */
}
.main-nav ul {
list-style-type: none;
}
.main-nav li {
background-color: #F9F9F9 ;
float: left;
margin: 4.6583% ; /* 15 / 322 (.content-sidebar) */
outline: 1px solid #DEDEDE;
text-align: center;
width: 40.3726% ; /* 130 / 322 */
}
.main-nav a {
display: block;
padding: 7.6923% ; /* 10 / 130 */
text-decoration: none;
}
/five.oldstyle/zero.oldstyle

## Página 59

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
Por/f_im,nossohumilderodapé:
/* Antes */
.main-footer {
background-color: #F0F0F0 ;
clear: both;
float:left;
font-size: 12px ;
margin: 15px 0 ;
padding: 15px ;
text-align: center;
width: 100% ;
}
/* Antes */
.main-footer {
background-color: #F0F0F0 ;
float:left;
font-size: .75em ; /* 12 / 16 */
margin: 1.5625% 0 ; /* 15 / 960 */
padding: 1.5625% ; /* 15 / 960 */
text-align: center;
width: 100% ;
}
AopegarnossoCSSconvertidoeoabrircomoestiliza çãodoHTMLquejáte-
mos,numprimeiromomento,nãodápranotarnadademais. Comexce çãode
algunspoucospixelspraláoupracá,estáamesmacoisaquevisualizamosemnosso
layout/f_ixo.
/five.oldstyle/one.oldstyle

## Página 60

/three.oldstyle./five.oldstyle. Convertendoumlayout/f_ixoemlayout/f_luído CasadoCódigo
Mas,aoredimensionarajanela,oscaminhosdaresponsividadeparaawebco-
meçamaserrevelados:
Percebaque,aoredimensionarajanelado browser-e,claro,casoaconte çao
/five.oldstyle/two.oldstyle

## Página 61

CasadoCódigo Capítulo/three.oldstyle. layout/f_luído
fatodealgumapessoajáacessarnossapágina-exemplousandoresolu çõesdasmais
diversas-,oqueaconteceéqueaapresenta çãoestáagradavelmentepadronizadae
responsiva!
Comissovocêdáoprimeirograndepassoparaaconstru çãodelayoutsrespon-
sivosparaaweb,meusparabéns!
Masapesardejáserumenormepassoemnossajornadaresponsiva,nemso-
mentedeumgrid/f_lexívelsedáodesenvolvimentodeumsiteresponsivo. Como
vimos,aindaexistemaisprincípiosdeumwebdesignresponsivoaseremexplora-
dos:recursos/f_lexíveiseMediaQueries.
/five.oldstyle/three.oldstyle

## Página 63

C/a.sc/p.sc/iacute.sc/t.sc/u.sc/l.sc/o.sc/four.oldstyle
Imagenserecursos/f_lexíveis
/four.oldstyle./one.oldstyle CSS/p.sc/a.sc/r.sc/a.sc /i.sc/m.sc/a.sc/g.sc/e.sc/n.sc/s.sc /f.sc/l.sc/e.sc/x.sc/iacute.sc/v.sc/e.sc/i.sc/s.sc
ContinuandocomodesenvolvimentodenossoHTMLdeexemplo,suponhamosque
agorafoidecididoquecada .last-content-callterá,logoabaixodotítulo,uma
imagemparailustrarseuconteúdo.Comojáestamosnumviésdedesenvolvimento
atravésda/f_iloso/f_iadeumwebdesignresponsivo,éprecisoencontrarumasolu ção
quefaçacomqueasimagensseadequemaoespa çodevidoe,independentemente
daresolução,sejambemapresentadas.
Paracomeçar,vamosvercomo/f_icaráoexemplocomumaimagemcolocadana
primeirachamada.OHTMLmudapara:
<article class="last-content-call">
<h2 class="secondary-title">
Título de Conteúdo
</h2>
<img src="cute-dogs.jpg" width="350">

## Página 64

/four.oldstyle./one.oldstyle. CSSparaimagens/f_lexíveis CasadoCódigo
<p class="brief">
Resumo ou
descrição deste conteúdo.
Deve ser algo que chame a atenção!
</p>
<a href="#">Leia mais </a>
</article>
Eoresultadoé:
Vejaquecoisa:aimagem,corretamentemarcadacomseu widthnoHTML,pos-
sui/three.oldstyle/five.oldstyle/zero.oldstylepxdelargura.Aconteceque,sejaqualforaresoluçãoemqueapáginaestiver
sendovista,essaquebraacontecerá...
/five.oldstyle/six.oldstyle

## Página 65

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
Podeparecerincrívelmas,paraconseguirmosumefeitointeressantedeimagens
/f_lexíveis,sóéprecisoumpouquinhodeCSS.Nadaderegrasextravagantes,nemde
propriedadesrecém-lançadasanteontemquenenhum browseraindasuporta;éo
bomevelhoCSS,compropriedadesfamiliaresaqualquerumcompoucotempode
estudosemfolhasdeestilo.VamosacrescentarnoiníciodenossoCSS:
img {
max-width: 100% ;
}
Segundoadocumenta çãosobre max-widthdoW/three.oldstyleC(http://ow.ly/bcKdv),essa
propriedadeCSSpermiterestringirlargurasdeconteúdodentrodeumdeterminado
intervalo.Nocaso,nosso“intervalo”foi/one.oldstyle/zero.oldstyle/zero.oldstyle/percent.oldstyle.Emoutraspalavras,nossaregrage-
néricadeCSSsigni/f_icaalgocomo: “ as imagens podem ter qualquer largura até no
máximo /one.oldstyle/zero.oldstyle/zero.oldstyle/percent.oldstyle”.Mas“/one.oldstyle/zero.oldstyle/zero.oldstyle/percent.oldstyle”dequê?Doelementoemqueestãocontidas!
No caso da imagem dos cachorrinhos que usamos, ela é /f_ilha de
.last-content-call. Portanto, a regra vale para a largura deste elemento
ou,nocasodesuafalta,nalarguradoelementoascendenteeassimpordiante.
Depoisdeaplicadaaregra max-width: 100%; ascoisasjácome çama/f_icarmais
interessantes:
/five.oldstyle/seven.oldstyle

## Página 66

/four.oldstyle./one.oldstyle. CSSparaimagens/f_lexíveis CasadoCódigo
Comessaregraemuso,jáépossívelcomplementarnossolayout/f_luídoever
comoeste/f_icacomtodosos .last-content-callcomsuasrespectivasimagens:
/five.oldstyle/eight.oldstyle

## Página 67

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
Umaobservaçãoimportanteéque,casosejaprecisosepreocuparcomoIE/eight.oldstylena
implementaçãodeimagensresponsivas,éprecisocolocar width:autoemimagens
dentrodeelementoscom floatsemdeclara çãoexplícitadelargura(http://ow.ly/
cO/three.oldstylefP).
/four.oldstyle./two.oldstyle CSS/p.sc/a.sc/r.sc/a.sc /o.sc/u.sc/t.sc/r.sc/o.sc/s.sc /r.sc/e.sc/c.sc/u.sc/r.sc/s.sc/o.sc/s.sc /f.sc/l.sc/e.sc/x.sc/iacute.sc/v.sc/e.sc/i.sc/s.sc
E,maisumavez,umarequisi çãofoifeitaàequipededesenvolvimentodosite.Dessa
vez,seráprecisoqueumvídeosejasemprecarregadonabarralateral,logoabaixo
dosmenuprincipal.Nosso asideentãomudaparaoseguinte:
<aside class="content-sidebar">
<nav class="main-nav">
<ul>
<li><a href="#">Menu 1 </a></li>
<li><a href="#">Menu 2 </a></li>
<li><a href="#">Menu 3 </a></li>
<li><a href="#">Menu 4 </a></li>
<li><a href="#">Menu 5 </a></li>
<li><a href="#">Menu 6 </a></li>
</ul>
</nav>
<iframe src="http://www.youtube.com/embed/1YLKyVwExOs" width="560"
height="315" frameborder="0" allowfullscreen></iframe>
</aside>
Ovídeoescolhidoabsolutamentenãoimporta.Ofatoéqueocódigofoicopi-
adodiretamentedorecursodecompartilhamentodoYouTube(maspoderiatersido
qualqueroutroservi çodecompartilhamentodevídeos).Dojeitoquedeláveio,cá
está.Aoobservamosoresultadodisso,épossívelperceberquealgonãosaiucomo
deveria.
/five.oldstyle/nine.oldstyle

## Página 68

/four.oldstyle./two.oldstyle. CSSparaoutrosrecursos/f_lexíveis CasadoCódigo
O embeddedestácomotamanhototalmenteforadoaceitávelparaocasoeestá
quebrandoolayout. Nocaso,elenãopodeextrapolaroslimitesdo asideedeve
aparecercorretamenteemqualquerresolu çãoedispositivoemqueositeforaces-
sado.Podeparecerincrível,masamesmaregraqueaplicamosanteriormentepara
imagenstambémpodeseraplicadaparaoutrostiposdemídiaerecursos,incluindo
iframe, object, embede video!Entãobastaatualizarpara:
img,
iframe,
object,
embed,
video {
max-width: 100% ;
}
/six.oldstyle/zero.oldstyle

## Página 69

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
E, assim como o esperado, nosso HTML contempla boa apresenta-
ção/posicionamento em qualquer resolução. Em outras palavras, agora temos
umvídeo/f_lexível!
Épossívelaindaincrementarnossaregra.Nostestesrealizados,aresponsividade
dosrecursosnãoécomprometidadenenhumamaneira;oacréscimofacultativosó
alteraumpoucocomooselementossãoapresentados.
img,
iframe,
object,
embed,
video {
height: auto;
max-width: 100% ;
}
/six.oldstyle/one.oldstyle

## Página 70

/four.oldstyle./two.oldstyle. CSSparaoutrosrecursos/f_lexíveis CasadoCódigo
Semmuitasaltera çõesnocomportamentodoselementos,épossívelmudaro
valordapropriedade heightde autopara 100% .Ficaaocritérioe/ounecessidades
doprojetoadecisãodamudan ça.
OYouTubecoloca,automaticamente,tarjaspretasemcimaeembaixodovídeo
aoseredimensionar,preservandoo r a t i ooriginaldovídeo.Entretanto,casosejapre-
cisousarvídeosdeoutrasfontes(ou,até,mesmo,vídeoscomhospedagemprópria),
existemalgumassolu ções:
• CreatingIntrinsicRatiosforVideo. Artigomuitointeressantede /T_hierry
Koblentzqueapresentaumatécnicaquepermiteaosnavegadoresdetermi-
naremasdimensõesdevídeoscombasenalarguradoelementoqueestão
contidos:http://ow.ly/eqra/four.oldstyle.
• FitVids.js.PluginjQuerysimplíssimodeusarquedáaqualidadedarespon-
sividadeavídeosincorporadosemqualquerpágina:http://ow.ly/eqrpN.
• FluidWidthVideo. Artigode ChrisCoyier queabordaainser çãodevídeos
comas t ag siframe, objecte embed:http://ow.ly/eqrT/nine.oldstyle.
/six.oldstyle/two.oldstyle

## Página 71

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
Exceçãoàvelharia:imagensredimensionadascomqualidadeemIE/six.oldstyle`
Aproveitemaexce çãodoqueacaboudeserdevidamenteenfatizado:umasolu-
çãodecomomelhoraraqualidadedeimagensredimensionadasexibidasemambi-
enteWindows(antesdo/seven.oldstyle),sobretudocomusodeIE/six.oldstyle`.
Aconteceque,usandoa websobestascondi ções,imagensredimensionadas/f_i-
camcomaqualidademuitocomprometida.ComadevidareferênciaaEthanMar-
cotte,reproduzoaimagemdeexemploemqueogurudowebdesignresponsivo
mostraumexemplodestaquestão.
Existemmuitasboastentativasporpartedacomunidadeparasolucionarisso.
InclusiveopróprioEthandesenvolveuumJavaScriptparatratarestassitua ções.
Basicamente o script varre todo o documento, troca as imagens pelo famoso
pixel transparente de /one.oldstylepx quadrado e aplica o /f_iltro proprietário da Microso/f_t
AlphaImageLoaderemcadauma. Apartirdisso,semprequeajaneladonavega-
dorforredimensionada,oscriptrecalcula,adequadaeproporcionalmente,largura
ealturadasimagens,redimensionandoopixel spacer.Aseguir,oscriptdeEthan.
var imgSizer = {
Config : {
imgCache : []
,spacer : "/path/to/your/spacer.gif"
}
/six.oldstyle/three.oldstyle

## Página 72

/four.oldstyle./two.oldstyle. CSSparaoutrosrecursos/f_lexíveis CasadoCódigo
,collate : function(aScope) {
var isOldIE =
(document.all && ! window.opera && ! window.XDomainRequest)
?1:0 ;
if (isOldIE && document.getElementsByTagName) {
var c = imgSizer;
var imgCache = c.Config.imgCache;
var images = (aScope && aScope.length) ? aScope :
document.getElementsByTagName("img");
for (var i = 0 ; i < images.length; i ++) {
images[i].origWidth = images[i].offsetWidth;
images[i].origHeight = images[i].offsetHeight;
imgCache.push(images[i]);
c.ieAlpha(images[i]);
images[i].style.width = "100%";
}
if (imgCache.length) {
c.resize(function() {
for (var i = 0 ; i < imgCache.length; i ++) {
var ratio = (imgCache[i].offsetWidth /
imgCache[i].origWidth);
imgCache[i].style.height =
(imgCache[i].origHeight * ratio) + "px";
}
});
}
}
}
,ieAlpha : function(img) {
var c = imgSizer;
if (img.oldSrc) {
img.src = img.oldSrc;
}
var src = img.src;
img.style.width = img.offsetWidth + "px";
img.style.height = img.offsetHeight + "px";
/six.oldstyle/four.oldstyle

## Página 73

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
img.style.filter =
"progid:DXImageTransform.Microsoft.AlphaImageLoader
(src='" + src + "', sizingMethod= 'scale')"
img.oldSrc = src;
img.src = c.Config.spacer;
}
// Ghettomodified version of Simon Willison 's addLoadEvent() --
http://simonwillison.net/2004/May/26/addLoadEvent/
,resize : function(func) {
var oldonresize = window.onresize;
if (typeof window.onresize != 'function') {
window.onresize = func;
} else {
window.onresize = function() {
if (oldonresize) {
oldonresize();
}
func();
}
}
}
}
E,atravésdeumcomentáriocondicional,fazeroscriptentrarema çãosomente
quandoobrowserforInternetExplorer:
<!--[if IE]>
<script src="imgsizer.js"></script>
<![endif]-->
Depoisdaimplementa çãodoscript,adiferen çanaqualidadedasimagensren-
derizadassobascondi çõesexpostasénítida:
/six.oldstyle/five.oldstyle

## Página 74

/four.oldstyle./three.oldstyle. Oproblemadeimagensemlayouts/f_luídos CasadoCódigo
Frequentemente,apartirdesugestõesecasosdacomunidade,oscriptérevi-
sadoeatualizado. Portanto,passeaacompanharoartigoemque,originalmente,
Ethandisponibilizouoscript,“FluidImages”(http://ow.ly/bg/five.oldstylehO),eaproveitepara
conhecermaisdetalhesepormenoresdecomoatécnicafoidesenvolvidaecomo
funciona.
/four.oldstyle./three.oldstyle O/p.sc/r.sc/o.sc/b.sc/l.sc/e.sc/m.sc/a.sc /d.sc/e.sc /i.sc/m.sc/a.sc/g.sc/e.sc/n.sc/s.sc /e.sc/m.sc /l.sc/a.sc/y.sc/o.sc/u.sc/t.sc/s.sc /f.sc/l.sc/u.sc/iacute.sc/d.sc/o.sc/s.sc
Comastécnicasapresentadasparaimagens/f_lexíveisemwebdesignsresponsivos,é
possívelfazerumbomnúmerodetestespara/f_ixarosconhecimentos,poisissojáé
abasearespeitodegrá/f_icosparaaresponsividadenaweb. Entretanto,surgeuma
questão(senão, aquestão)sobreapresentarimagensemqualquerresolu ção:pesoe
tamanho!
Quandooacessoétradicional,feitovia desktopou notebook,éjusti/f_icávelsupor
queousuárioestávendoapáginaatravésdeummonitordetamanhorelativamente
confortável. Isso,juntamentecomofatodequeavelocidademédiadeconexãoà
internetnoBrasiléde/five.oldstyle/one.oldstyle/two.oldstyleKba/two.oldstyleMb(http://ow.ly/bg/seven.oldstyle/eight.oldstylej),nãotrazmaioresproblemas
paraapessoaquenavegaemsitescomimagens.
Jáquandooacessosegueatendênciacrescentedeacesso mobile,temosquestões
eproblemasseríssimos.Essesaparelhoscostumamterumatelamenore,muitasve-
zes,resoluçõesnãomuitoboas.Alémdisso,avelocidadedaconexãomóveléinferior
adeoutrosmeiosdeacessoàInternet.Comtudoisso,temosquepensararespeito
/six.oldstyle/six.oldstyle

## Página 75

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
decomoservirimagensadequadamenteaosvisitantes,levandoemcontaseu peso
(tamanho,emKB,dasimagens)eseu tamanho(númerodepixelsqueformama
imagem).
Segundoastécnicasmostradasatéentão,umamesmaimageméapresentadaseja
praqualresolu çãofore,conformeocaso,estaéredimensionadaparaseadaptarà
realidadedaresolu çãodo devicequeestásendousado. Issoquerevelaumponto
crítico:o mesmoarquivodeimagem queéapresentadonumaboavelocidadede
conexão,vistaemumateladetamanhoconsiderável,tambéméoservidoerenderi-
zadoemdispositivosmóveis!
Mesmoquesemquerer,pessoasutilizandodispositivos mobilequeacessamo
siteserãopenalizadaspornãodisporemdeum d i s p l a ymaiore/ouumaconexão
maisveloznomomentodoacesso.Ocidadãoacessandoseusitepseudo-otimizado
paradispositivosmóveisseráobrigadoaesperarcarregaraquelaimagemde/one.oldstyle/five.oldstyle/zero.oldstyle/zero.oldstylepx,
pesando/eight.oldstyle/zero.oldstyleKb,sóparavê-lasendolentamenterenderizada,járedimensionada(e
distorcida),demorandomuitomaistempoparaterminardeserbaixadaeexibida
emsuaconexão/three.oldstyleGdoqueeleparadecidirprocuraroqueprecisanositedaconcor-
rente...
Seoacessoéfeitovia mobile,émaislógico(emelhorparaquemacessa)que
umaversãoreduzidadaimagem,demenorpesoetamanho,sejaenviadaa/f_imde
aprimoraraexperiênciadavisita. A/f_inal,/seven.oldstyle/one.oldstyle/percent.oldstyledaspessoasesperamqueoacessoa
umsitemóvelsejatãorápidoquantonodesktop(http://ow.ly/bg/seven.oldstyleWp)!
/four.oldstyle./four.oldstyle T/eacute.sc/c.sc/n.sc/i.sc/c.sc/a.sc/s.sc /p.sc/a.sc/r.sc/a.sc /i.sc/m.sc/a.sc/g.sc/e.sc/n.sc/s.sc /f.sc/l.sc/e.sc/x.sc/iacute.sc/v.sc/e.sc/i.sc/s.sc /e.sc/m.sc /w.sc/e.sc/b.sc /d.sc/e.sc/s.sc/i.sc/g.sc/n.sc/s.sc
/r.sc/e.sc/s.sc/p.sc/o.sc/n.sc/s.sc/i.sc/v.sc/o.sc/s.sc
Tendovistoobásiconecessárioparaapresentarimagens/f_lexíveisemdesignsrespon-
sivosparaaweb,caberessaltarqueexistemdiversastécnicasparaqueessaentregade
imagenssejaamaisadequadapossível(dentrodaperspectivadequemdesenvolveu
arespectivatécnica,evidentemente).Aseguir,épossívelconhecerumasériedetéc-
nicasparaimagens/f_lexíveis;comosempre,nãoexiste“amelhor”técnica,esimaque
maisseenquadraaoseuestilodedesenvolvimento,dentrodeumprojetoespecí/f_ico.
Riloadr
Riloadrseauto-intitulaumframeworkindependentecarregadordeimagensres-
ponsivas.Elerealmentepossuimuitasboascaracterísticas.Sóparacitaralgumas:
/six.oldstyle/seven.oldstyle

## Página 76

/four.oldstyle./four.oldstyle. Técnicasparaimagens/f_lexíveisemwebdesignsresponsivos CasadoCódigo
• Relativamentefácildeaprendereusar;
• Oferecebastantecontrolesobrecomoasimagensresponsivasirãosecompor-
tar;
• Opçãodecarregamentosobdemanda(“lazyload”)dasimagens;
• SuportabrowserscomJavaScriptdesabilitado(ousemJavaScript);
• Nãofazmúltiplasrequisiçõesparaamesmaimagem.
AideiaprincipaldoRiloadrédeixaroatributo srccompletamenteforadas t ag s
deimagem,substituindo-opeloatributo data-src.AtravésdamágicadoJavaScript,
épossívelobterresultadossatisfatórioscommarca çãodotipo:
<img data-src="pessoa.jpg">
<noscript>
<img src="img/small/pessoa.jpg">
</noscript>
Realmente,oRiloadrapresentaumadastécnicasmaise/f_icientesparaimagens
responsivasou,pelomenos,éumadasquemaisoferecemop çõesdepersonaliza ção
ecustomizaçõesparaesteobjetivo.Paraveradocumenta çãocompletaeexemplos
deuso,visiteorepositórioo/f_icialdoRiloadr(http://ow.ly/cO/three.oldstyleHZ).
jQueryPicture
jQueryPictureéumpluginparajQuery(desomente/two.oldstyleKB)paraadicionarsu-
porteaimagensresponsivasnos layouts.Elesuportaoelemento <figure>(usando
alguns data-*)e,até,noelementoproposto <picture>(http://ow.ly/cO/five.oldstylelY). Um
exemplodeusoseria:
<figure class="responsive" data-media="assets/img/small.png"
data-media440="assets/img/medium.png"
data-media600="assets/img/large.png">
<noscript>
<img src="assets/img/large.png" alt="">
</noscript>
</figure>
E,seguindoamelhorformaenxutadeiniciarpluginscomjQuery:
/six.oldstyle/eight.oldstyle

## Página 77

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
$(function(){
$('figure.responsive').picture();
})
Aboanotíciaéque,alémdeserbastantesimplesefácildeseusar,eletemsuporte
pelosmelhoresnavegadoresepeloInternetExplorerapartirdesuaversão/nine.oldstyle.Para
maioresinformações,dêumaolhadanorespositórioo/f_icialdojQueryPicture(http:
//ow.ly/cO/four.oldstyleOW).
Picture/f_ill
Picture/f_illéumaabordagemdeimagensresponsivasqueépossívelutilizaratu-
almentesemmaiorescomplica ções(em browserscomsuporteaMediaQueries,que
seráabordadofuturamente).Paratanto,eleexigeumamarca çãodiferentedausual
paraimagens:
]
<div data-picture data-alt= "Descrição da imagem" >
<div data-src="small.jpg"></div>
<div data-src="medium.jpg" data-media="(min-width: 400px)" >
</div>
<div data-src="large.jpg" data-media="(min-width: 800px)" >
</div>
<div data-src="extralarge.jpg" data-media="(min-width: 1000px)" >
</div>
<!-- Conteúdo para JavaScript desabilitado/não suportado -->
<noscript><img src="assets/img/small.jpg" alt="Descrição da imagem" >
</noscript>
</div>
A p e s a r d a m a r c açãoincomum(edotrabalhodemanuten çãoqueestaacarreta),
apropostaébeminteressantee,paramaisdetalhesarespeito,bastaacessarorepo-
sitóriodoPicture/f_ill(http://ow.ly/cO/five.oldstyleEn).
/six.oldstyle/nine.oldstyle

## Página 78

/four.oldstyle./four.oldstyle. Técnicasparaimagens/f_lexíveisemwebdesignsresponsivos CasadoCódigo
AdaptiveImages
AdaptiveImages,deMattWilcox(http://ow.ly/cNXkD),éumadastécnicasque,
naopiniãodocriador(edemilharesdepessoaspelomundoqueautilizam),mais
fazemmaissentido.AdaptiveImagesdetectaotamanhodateladovisitanteeauto-
maticamentecria,fazcacheeentregaversõesredimensionadasdeimagensreferen-
ciadasemtags <img>,apropriadasaodispositivoqueestásendousado.
AtécnicaenvolveousodePHP,JavaScripteumpoucodeconteúdoemseu
arquivo .htaccess. Alémdeserbastantee/f_icienteporservirdiferentestamanhos
damesmaimagemdependendododispositivousadoparaavisualiza çãodosite,um
outropontoforteéquenenhumaaltera çãonamarca çãoHTMLsefaznecessária.
Parainstru çõesmaisdetalhadasecomoinstalareusaratécnica,visiteosite
o/f_icialdaAdaptiveImages(http://ow.ly/cNVks).
Qualtécnicaparaimagensresponsivasusar?
Estasforamsomentealgumasrecomenda çõesdetécnicasparaimagensrespon-
sivaspossíveis.Existem,literalmentedezenasdelase,acadadiaquepassa,maispes-
soasdesenvolvemnovastécnicas,fazempropostasdepadrõesdemarca çãoetentam
desenvolversoluçõese/f_icientesparaaquestãodeimagensresponsivasparaweb.
E,dentretantastécnicasdiferentes,/f_icaapergunta: qualdelausar? Comojá
comentado,nãoexisteumarespostaúnicaparaestaquestão,esimumaanálisedo
projetoemqueseestáenvolvidoparaqueadecisãosejatomada.Paraajudarnesta
decisão,algumaconsidera çõesdevemserfeitas:
• ÉimportantequefuncionesemJavaScript?
• SendoJavaScript,podeserumpluginoudeveserumasolu ção“nativa"?
• Pode-seusarmarcaçãoespecial?
• Semânticaéessencial?
• AspáginasprecisamservalidadasnovalidadordoW/three.oldstyleC?
• Tem-seacessoaarquivosserversidee.htaccess?
• Deve-seprimarpelaperformance?
/seven.oldstyle/zero.oldstyle

## Página 79

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
Respondendoaessasperguntasetendoemmentequeaspessoasesperamque
oacessoaumsitemóvelsejatãorápidoquantonodesktop(http://ow.ly/bg/seven.oldstyleWp),é
possívelescolherumasolu çãoquesejaamelhorparaoprojeto,emespecí/f_ico,quese
estejatrabalhandonomomento.Existeumaplanilhapúblicacomumacompila ção
dealgumassolu çõespossíveisparaaquestãodasimagensresponsivas.Éinteressante
quevocêdêumaolhadae,quemsabe,jáencontrealgumasolu çãoqueseadequea
seuprojetoatual:http://ow.ly/cO/seven.oldstyle/five.oldstyle/eight.oldstyle.
NaspalavrasdeEthanMarcotte...
Parafecharcomchavedeouroestaquestãoimportantíssimasobreimagens
responsivas,cabelermos(epesquisarmosere/f_letirmos)sobreaspalavrasdopró-
prioEthanMarcottequandoparticipoudeumaentrevistaà.NETMagazine(http:
//ow.ly/cSCTR),quandooentrevistador,OliverLindberg,disse“ Eu quero saber qual
a abordagem mais prática e robusta para exibição de imagens responsivas em vários
dispositivos”.Arespostafoi:
Bem, há muita atividade em toda a área de “imagens responsivas” agora. Detecção
de largura de banda é um ponto cego para todos nós se estamos trabalhando no fron-
tend ou backend. navigator.connection não está amplamente implementado ou (eu
diria) é especí/f_ico o su/f_iciente para ser útil e todos nós estamos assistindo a Device APIs
Working Group (http://ow.ly/cSDta) com interesse.
Dito isto, eu estou realmente animado com a discussão [do elemento] “picture”,
que tem sido habilmente conduzida por Mat Marquis (http://ow.ly/cSEky) no W/three.oldstyleC
community group for responsive images (http://ow.ly/cSEc/zero.oldstyle). E a solução ‘Picture/f_ill’,
de Scott Jehl, signi/f_ica que podemos começar a experimentar isso hoje.
Claro que ainda não temos, sequer, uma especi/f_icação para um novo padrão de
marcação, muito menos uma solução nativa funcional. Então, talvez a curto prazo,
precisemos con/f_iar em negociação de conteúdo server-side - embora, se esse for o caso,
espero que haja uma mentalidade mais “mobile /f_irst”, à Brett Jankord’s Categorizr
(http://ow.ly/cSFcA).
M a se up e r g u n t os eh áo u t r ao pção disponível para nós: por que não podemos
perguntar aos nossos usuários o que eles preferem? Eles estão acostumados a tomar
decisões “cosméticas” de UI sempre que visitam o Gmail ou a escolher a qualidade de
vídeo no Y ouTube. Cada vez que clicam em um link “móvel” ou “desktop” em seus tele-
fones, eles estão optando por experiências e conjuntos de recursos que são radicalmente
diferentes um do outro. Então, eu estou querendo saber se há uma solução mais “ma-
tizada” aqui: poderíamos pedir aos nossos usuários para, bem, dizer-nos que tipo de
/seven.oldstyle/one.oldstyle

## Página 80

/four.oldstyle./five.oldstyle. Imagensemaltaresolução CasadoCódigo
decisões de largura de banda tomar?
Ofuturo
Amaioriadassolu çõesapresentadasanteriormentepossuemalgumpontofalho;
a/f_inal,assimcomoopróprioweb designresponsivo,astécnicasquelhesãoinerentes
aindaestãonoinício,nãoestão“maduras”eaindanãosechegouaumasolu ção
“perfeita”.AboanotíciaéquejáexistempropostasnoW/three.oldstyleCparatentarpreencher
estalacuna,comoatributo srcsetnoHTML(http://ow.ly/eqwpe)eapropriedade
image-setparaCSS(http://ow.ly/eqwjs).
Esperemossomentemaisalgumtempoeusarimagensem web designresponsivo
serátãosimplesquantoescreveralgumaslinhasdeHTMLouCSSatualmente!
/four.oldstyle./five.oldstyle I/m.sc/a.sc/g.sc/e.sc/n.sc/s.sc /e.sc/m.sc /a.sc/l.sc/t.sc/a.sc /r.sc/e.sc/s.sc/o.sc/l.sc/u.sc/ccedilla.sc/atilde.sc/o.sc
Devidoàtecnologiaatual,somentealgunsdispositivospossuem d i s p l a y sdealtare-
solução,capazesdeapresentarcorretamenteimagensdealtíssimaresolu ção.Noca-
pítulocomreferênciasderecursosparawebdesignresponsivo/seven.oldstyle,vocêvaiencontrar
soluçõesparaservirimagensdealtaresolu çãoparadispositivosquepossuem retina
d i s p l a y,oqueébeminteressante,maséprecisoteremmentequeatendênciaéque
maisaparelhoscomecemaapresentarumatelacomessascaracterísticas.
Portanto,éimportanteterconhecimentosdealgunspontoscruciaisparaaqueles
projetosemqueimagensdealtaresolu çãoestãocontempladaspeloplanejamento.
Adam Bradleyapresentadiretrizesdemuitointeressesobreaquestão(http://ow.ly/
e/zero.oldstyletkE)que,independentementedequalsoluçãoseopteporusar,devemserlevadas
emconsideração:
Nãofazerrequisi çãodamesmaimagensváriasvezes. Quandoonavegadorvê
pelaprimeiravezumelemento imgnoDOM,ele,imediatamentefazumarequisi ção
aoservidorparaestaimagem(mesmoantesdeoDOMestarpronto). Oatributo
srcdeveseralteradoantesmesmodeonavegadorpassarpeloelementodeimagem
oujáserátardeearequisi çãojáterásidofeita.Alémdisso,seváriospedidosesta-
vamsendofeitosparaumaimagem,issonãosóretardaonavegadoreimpactana
performance,mas,também,aumentao“estresse”adicionalsobreosservidores.
Nãousarcookienemoelemento<base>. Nãosedeveusarporcausado look-
ahead parserdosnavegadoresquejádisparamasrequisi çõesdas <img>antesmesmo
deoJavaScriptentrarema ção.Ouseja,o downloaddaimagemcome çaantesdeo
códigoqueespeci/f_icaocookieou baserodar.
/seven.oldstyle/two.oldstyle

## Página 81

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
ManipulaçãomínimadoDOM. ManipularoDOMrequertempoeretardaa
atuaçãodonavegador,portanto,asolu çãousadadevefazertãopoucasatualiza ções
noDOMquantopossívelparagarantirquetodososdispositivos,especialmenteos
debaixacapacidadedeprocessamento,possamlidarcomestamanipula ção.
ImagensdevemcontinuarvisíveissemJavaScript. SeoJavaScriptnãoestiver
habilitado,onavegadoraindadevesercapazdeinterpretarerenderizartodasas
imagensdapáginaemseutamanho default.
Nãoapresentarimagensemaltaresolu çãoparatodos. Amaioriadosusuá-
riosnãotêm d i s p l a y sdealtaresolu ção,issoéfato.Terservidoresservindoimagens
maioresparatodososusuáriosadicionauma“pressãoextra”nosservidores,clien-
tes,larguradebanda,etc.Sóapresenteimagensdealtaresolu çãoparaaquelesque
realmentepodemsevalerdesterecurso.
Comodito,estassãosomentediretrizes,nãoregrasrígidaseimutáveisdeproce-
dimentos.Então,semprequeforpossível,levandoemconsidera çãoapartetécnica
edeplanejamento,seguirestasdicastrarábenefíciosaosprojetosquesevalemde
imagensemaltaresolu ção.
/four.oldstyle./six.oldstyle T/i.sc/p.sc/o.sc/s.sc /d.sc/e.sc /i.sc/m.sc/a.sc/g.sc/e.sc/m.sc /p.sc/a.sc/r.sc/a.sc /w.sc/e.sc/b.sc
Sim,foram(econtinuamsendo)desenvolvidastécnicasquevisamsanaroproblema
deapresentarumaimagemquemelhorcondizao devicequeapessoausaaovisitar
umsite.Masumpassoanterioraissoésaberescolherqual tipodeimagem usarem
qualsituação.
Atualmente,/three.oldstylesãoosprincipaisformatosdeimagemusadosnaweb-GIF,JPGe
PNG-econhecerasdiferentescaracterísticasdessesformatosdeimagemmaisco-
munsparapoderoptarconscientementeentreumououtro,conformeanecessidade,
éoprimeiropassorumoàotimiza çãodeumsite-nãosomenteosdewebdesign
responsivo!
GIF
GIFquerdizer Graphics Interchange Format(Formatodeintercâmbiodegrá/f_i-
cos).Imagensnoformatosãoconhecidascomo“ i n d e x e d”,dadaacaracterísticado
formatodesuportaraté/two.oldstyle/five.oldstyle/six.oldstylecores(/eight.oldstylebits)indexadasnumapaleta,provendoimagens
depequenopeso,bastanteusadaseideaisparaoambiente onlineeusado,principal-
mente,paraícones,ilustra ções,logos,imagens“chapadas”equalqueroutranecessi-
dadequepossasersupridacomascaracterísticasinerentesaoformato.
/seven.oldstyle/three.oldstyle

## Página 82

/four.oldstyle./six.oldstyle. Tiposdeimagemparaweb CasadoCódigo
GIFéumformatosemperda,oquesigni/f_icaque,quandovocêmodi/f_icaesalvaa
imagem,nãohámudan çanaqualidade.GIFsuporta“transparênciabinária”,ouseja,
pixelsemumaimagemGIFousãototalmentetransparentesoutotalmenteopacos.
Alémdisso,oformato,depoisdeumarevisãopoucosanosdepoisdeseulan çamento,
passouasuportaranima ções,oqueconsolidouseusucessoàépocada,entãono-
vidadee,certamente,contribuiu,juntamentecomsuasoutrasboascaracterísticas,
paraa“consagra ção”doformatoeamplousonaweb.
Devidoasuascaracterísticas,ousodoformatoGIFjáfoiindicadopara:
• Logos
• Ícones
• Desenhos
• Ilustraçõessimples
• Imagenscompoucascores
Atualmente,devidoaoadventodoPNG/eight.oldstyle(queserávistoaseguir),ousodo
formatoGIFdevesedarmaisparaimagensanimadas.
JPG(ouJPEG)
JPEGéoacrônimode Joint Photographic Experts Groupeéumdosmaisusados
nomundonãosomenteemambientesvirtuais,mastambémporcâmerasdigitaise
dispositivosdiversosdecapturadeimagem. Eesseíndicedeusonãoéemvão,já
/seven.oldstyle /four.oldstyle

## Página 83

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
queoformato,de/two.oldstyle/four.oldstylebits,permiteousodeaté/one.oldstyle/six.oldstylemilhõesdecores,oquegarante
imagensdeboaexcelentequalidade.
ApesardeoJPGpodertermilhõesdecoreseaindaconseguirumaexcelentetaxa
decompressão,diferentementedoGIF,éumformato comperda.Ouseja,cadavez
quesesalvaoarquivo,acompressãoérefeitaeumpoucodequalidadeseperde.A
vantageméqueépossívelescolheroníveldequalidadedasimagenssalvasemJPG,
conformeanecessidade. Amesmaimagemcomumaqualidadeexcepcionalque
podeservirparaimpressãodeumbanner,apóssersalvacomqualidadeinferior,
tambémpodeservirparaexibi çãoetransferêncianaweb.
Infelizmente,oformatonãoaceitatransparência,mas,devidoàscaracterísticas
mostradas,seuusomaisindicadoé:
• Fotogra/f_ias
• Imagenscommuitascores
• Imagensdealtacomplexidade
• Aliarqualidadeepesodoarquivo
• Usodamesmaimagememváriosmeiosdeacesso(ajustandoaqualidade)
PNG
PNG,ou Portable Network Graphics,éomaisrecenteformatodeimagemdos
maiscomunsusadosnawebe,comoobjetivodesuprirdeterminadasrestri ções
(técnicaselegais)doGIF,oformatotrouxeconsigocaracterísticasdesejáveisdoGIF
/seven.oldstyle/five.oldstyle

## Página 84

/four.oldstyle./six.oldstyle. Tiposdeimagemparaweb CasadoCódigo
eJPG.Oformatopodevircomo PNG/eight.oldstylebitsou PNG/two.oldstyle/four.oldstylebits,cadaumtendosuas
característicasprópriaseservindoparadeterminadospropósitos.
PNG-/eight.oldstylepegamuitodoGIF,sendoumformatosemperda,provendosuportea
/two.oldstyle/five.oldstyle/six.oldstylecoresetransparênciabinária(sendoqueconseguegerararquivosdepesomenor
queGIF).
PNG-/two.oldstyle/four.oldstylejunta“omelhordosmundos”,jáqueéumformatosemperdadequali-
dade,aceita/one.oldstyle/six.oldstylemilhõesdecorese,umadasmaisinteressantes,aceitadiferentesníveis
detransparência!Obviamentetudoissoacarretaemumaimagemdepesomaior.
DependendosesevaiusarPNG/eight.oldstyleouPNG/two.oldstyle/four.oldstyle,suasrecomendaçõesdeusosão,
respectivamente,iguaisàdosformatosGIFeJPG-lembrandoqueparaimagens
complexasoudemuitascoresqueexigemtransparência,PNG/two.oldstyle/four.oldstyleéoideal.
SVG
SVGéumalinguagemdemarca çãoparadescrevergrá/f_icosbidimensionaise
imagens.SegundoaWikipédia(http://ow.ly/ev/four.oldstyleBa):
/seven.oldstyle/six.oldstyle

## Página 85

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
SVG é a abreviatura de Scalable Vector Graphics que pode ser traduzido do inglês
como grá/f_icos vetoriais escaláveis. Trata-se de uma linguagem XML para descrever de
forma vetorial desenhos e grá/f_icos bidimensionais, quer de forma estática, quer dinâ-
mica ou animada. Umas das principais características dos grá/f_icos vetoriais, é que não
perdem qualidade ao serem ampliados.
Epresteumaaten çãoespecialnaparte“nãoperdemqualidadeaoseremampli-
ados”!Exatamenteoqueéprecisoquandopensamosemgrá/f_icosqueprecisamser
bemapresentadosemdiversasresolu çõesdiretentes,nãoéverdade?
Porserindependentederesolu ção,SVGéótimoparaaapresenta çãodegrá/f_i-
cosnaweb. SVG,sendoumadescri çãoXMLparagrá/f_icoseimagens,écapazde
trabalharbemcomformas,caminhos,cores,gradientesefontes.Filtroseanima ção
tambémpodemserde/f_inidos.Umavezcriadas,imagensSVGpodemserusadasem
qualquerlugar,emqualquerescalaeresolu ção.
AgrandevantagemdeusarSVGemwebdesignsresponsivoséque,apesarde
existiremdiversastécnicasparaimagens/f_lexíveis,nãoéprecisosepreocuparem
usarversõesdetamanhosdiferentesdeumamesmaimagemjáque,conformeexpli-
cado,trata-sedeumformatovetorial,quepodeserredimensionadoàvontadesem
quesuaqualidadesejacomprometida.
VocêvaiconseguirapresentarbemSVGnativamenteemdiversosnavegadores,
como:
• Chrome/four.oldstyle+
• Opera/nine.oldstyle./five.oldstyle+
• Firefox/four.oldstyle+
• Safari/four.oldstyle+
• InternetExplorer/nine.oldstyle+
Icon Fonts
Icon Fontsnaverdadenãoéumformatodeimagem;comosugereopróprio
nome,sãográ/f_icos(geralmente,ícones)que,naverdade,sãofontes!Trata-sedeuma
técnicainteligentíssimaparaprover“imagens”quesãobemapresentadasemquais-
querresoluçõessemanecessidadedeserprecisodiferentesversões,emtamanhos
diferentes,damesmaimagemougrá/f_ico.
/seven.oldstyle/seven.oldstyle

## Página 86

/four.oldstyle./six.oldstyle. Tiposdeimagemparaweb CasadoCódigo
Porexemplo,quandoéprecisousarváriosíconesnum site,geralmenteumar-
quivoéfeitoeusadocomo sprite.UsandoIconFonts,vocêincorporaemsuaspá-
ginas,atravésdapropriedade@font-facedeCSS(http://ow.ly/ev/seven.oldstylelV),fontes“espe-
ciais”,emquecadacaractereé,naverdade,umícone!Ecomo,apesardeseparecer
comumaimagem,trata-sedeumafonte,alémdoconvenientedesepoderaumentar
ediminuiràvontadeseutamanhosemperdadequalidade,tambémépossívelapli-
cartodasaspropriedadesCSSrelativasàfontes,oquedáuma/f_lexibilidadeincrível
nahoradaapresenta çãoeefeitos!
Paraseterumano ção,dêumaolhadanoIconFontsareAwesome(http://ow.ly/
ev/seven.oldstyleSj),queéumdemodeIconFontquerpermitealterar,emtemporeal,algumas
propriedadesCSSparatestes,taiscomotamanho,coreposisionamentoeformato
desombra.
Projetosderenome,como TwitterBootstrap,sevalemdestatécnicaparacon-
ferirmaisdinamismoemodernidadeemseusrecursos.Provavelmentevocêdeveria
fazeromesmo!Aquivãoalgumasreferênciasparavocêcome çar:
• Glyphicons.Excelentes setsdeIconFontsgratuitos:http://ow.ly/ev/nine.oldstyleus.
• FontSquirrel@font-faceGenerator. Tenhacertezadequesuasfontesserão
incorporadasevisualizadascorretamenteemqualquernavegador:http://ow.
ly/ev/nine.oldstylemX.
• FreeIconFontsforWebUserInterfaces. Coletâneaincríveldevários sites
quedisponibilizamIconFonts:http://ow.ly/ev/nine.oldstyleJb.
Brevesconsideraçõessobreformatosdeimagem
Numprimeiromomento,podeparecerumtantoqueinútilabordarosformatos
deimagensmaiscomunsusadosnawebnumlivrosobrewebdesignresponsivo.
Entretanto,pensandomelhor,émuitoimportantesaberescolher,conscientemente,
qualéomelhorformatoparaasdiferentesnecessidadesdosprojetos.
Usandoimagensadequadaseotimizadasparacadasitua ção(porexemplo,JPG
parafotogra/f_ias,PNGparaícones,etc),épossíveltirarmelhorproveitodascarac-
terísticastécnicasdasimagense, aonãousarformatosinadequados, muitosre-
cursos-emdiversossentidosdapalavra-sãopoupados. Vocêdeveria,também,
passarasimagensdositeemotimizadoresdeimagens(quefazemopesodaima-
gem/f_iquemenorsemalterarsuaqualidade),jáque,commenosKBparaserbai-
xadonomomentodoacesso,otempototaldecarregamentoémenor. Existem
/seven.oldstyle/eight.oldstyle

## Página 87

CasadoCódigo Capítulo/four.oldstyle. Imagenserecursos/f_lexíveis
muitasboasferramentasparaisso,comojpegtran(http://ow.ly/dxSyx),JPEGmini
(http://ow.ly/dxSte),TinyPNG(http://ow.ly/dxSpB),OptiPNG(http://ow.ly/dxSmr)
eSmush.it(http://ow.ly/dxSjc).
Outradicaimportantíssimaéousode sprites(http://ow.ly/dxRdy),umatécnica
paracombinaçãodeimagensmenoresemumaimagemmaior.Paramostraraima-
gemcorreta,éprecisoajustarosvaloresdapropriedadeCSS background-position.
Combinandováriasimagensdestaforma,épossívelreduzirospedidosHTTP(e
reduzirrequisiçõesHTTPéumimportantíssimopassorumoàmelhoradeperfor-
manceedesempenhodeumsite).
Épossívelfazer sprites“manualmente”, masháferramentasonlineparaisso,
comoCSSSpriteGenerator(http://ow.ly/dxRt/seven.oldstyle),quedáaopçãodefazeruploadde
imagensparaseremcombinadosemumúnicosprite,gerandoocódigoCSS(osva-
loresdebackground-position)pararenderizarasimagens.
Proverimagensotimizadasparacadacontexto/necessidadeéumpassoimpor-
tanteparaaotimiza ção,emgeral,de web sites.Existemmuitasoutrastécnicaspara
conseguirosmelhoresresultadosdecadaformatoapresentado;técnicasestasque
extrapolamoobjetivodestelivro,mas,certamente,devemserdeinteresseparaqual-
querumqueprocure,sempre,provermelhoresexperiênciasaosvisitantesdeseus
sites,garantindoqueseusprojetossejamrápidosesuperotimizados.
/seven.oldstyle/nine.oldstyle

## Página 89

C/a.sc/p.sc/iacute.sc/t.sc/u.sc/l.sc/o.sc/five.oldstyle
MediaQueries
Nocapítuloanterior,foiapresentadaatécnicaessencialparaseobterimagens(e
outrosrecursos)responsivasnaweb.
Comofoicitadonocapítulo/two.oldstyle,quandofoiabordadaatrincatecnológicadoweb
designresponsivo(se ção/two.oldstyle./two.oldstyle),/three.oldstylesãoastecnologiasnecessáriasparatal.Jáforamabor-
dadosolayout/f_luídoeasimagens(eoutrosrecursos)/f_lexíveis.E,/f_inalmente,temos
asMediaQueries,umape çachavenonossoquebra-cabe ça.
Vamosconhecê-lase,depois,aplicá-lasnapráticaemnossositedeexemplo.
/five.oldstyle./one.oldstyle P/r.sc/i.sc/m.sc/e.sc/i.sc/r.sc/o.sc, /o.sc/s.scM/e.sc/d.sc/i.sc/a.scT/y.sc/p.sc/e.sc/s.sc
Atéondechegamoscomnossositeexemplo,jáconseguimosfazerolayoutser/f_lexí-
vel,ajustandoalarguradoselementosconformeotamanhodatela.

## Página 90

/five.oldstyle./one.oldstyle. Primeiro,osMediaTypes CasadoCódigo
Mas,quandooassuntoédesenvolversitesdequalidadequeseadaptematodo
equalquerdispositivo,éprecisoirumpassoalém.Éprecisoqueositenãosomente
tenhaseuselementos/f_lexíveis,mastambémqueesseselementospossamvariarde
posição,tamanho,seescondamouapare çam,conformeanecessidade/display. É
precisoqueodesignseajuste !
Eéexatamentenestepontoqueentramas Media Queries.Mas,antesdeaden-
trarmosnofascinanteestudodas Media Queries,éinteressanteentenderumpouco
sobreMediatypes.
M e d i a T y p e séumarecomenda çãodaW/three.oldstyleC(http://ow.ly/cQ/three.oldstyleMF)desdeoCSS/two.oldstyle.
ComMediaTypes,épossívelapresentarositedemaneiradiferente,dependendoda
media.Épossívelumaapresenta çãodiferenciada(atravésdefolhasdeestilo)quando
apáginaestásendovistadeumprojetor,quepodeserdiferentesdequandoseusa
umaimpressora,umsintetizadordevoz,umaTV,dentreoutros.Resumidamente,
eisalista:
• all.Afolhadeestiloserveparatodososdipositivos.
• braille.Paradar feedbackquandoseusaalgumdispositivotátil.
• embossed.Impressorasembraillepaginadas.
/eight.oldstyle/two.oldstyle

## Página 91

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
• handheld. Dispositivosmóveis(comumentecomtelapequenaelargurade
bandalimitada).
• print. Paramaterialpaginadoeparadocumentosvisualizadosnatelano
modoVisualizaçãodeImpressão.
• projection.Destinadoaapresenta çõesprojetadascomo,porexemplo,proje-
tores.
• screen.Destinado,principalmente,paratelascoloridasdecomputador.
• speech.Parasintetizadoresdevoz.
• tty. Dipositivosde“grade/f_ixa”paraexibiçãodecaracteres,comoteletypes,
terminaisealgunsoutros.
• tv.Aparelho“tipoTV”(baixaresolu ção,cores, scrolllimitado,som).
Aideiaéque,aoseracessada,apágina websejarenderizadaconformeoestilo
maisapropriadoao devicequeestásendousadopararealizaroacesso,ouseja,se
apessoaestáusandoum handheld,oestiloespeci/f_icadoparaestedispositivo,em
especí/f_ico,entraemação;seéatravésdeumaTV,oestiloapropriadoàTVséusado;
eassimpordiante.
Vamosaumexemplodeimplementa çãodeMediaTypesna <head>deumapá-
gina(aespeci/f_icaçãoda mediadeveseremminúsculo):
<link rel="stylesheet" type="text/css" media="print"
href="print_style.css">
Querdizer,casoa t aglinktenhaoatributode M e d i a T y p eespeci/f_icandop r i nt,
somentequandoalguémquiserimprimiro(s)documento(s)quelevamesta t agé
que print_style.cssentraráema ção;paraosdemaistiposde media,não.
Outroexemploseriacasosequisesseusaramesmafolhadeestiloparadiferentes
medias:
<link rel="stylesheet" type="text/css" media="print, handheld"
href="print_handheld_style.css">
Neste caso, a(s) página(s) somente seria renderizada se valendo de
print_handheld_style.css caso o dispositivo fosse umhandheldou no caso
deapessoaquererimprimí-la(s).
/eight.oldstyle/three.oldstyle

## Página 92

/five.oldstyle./one.oldstyle. Primeiro,osMediaTypes CasadoCódigo
Tambémépossível,dentrodeummesmoarquivodeestilos,especi/f_icarregras
paradiferentes mediasassim(e,obviamente,asregrasquenão/f_icamdentrodealgum
bloco @mediasãoaplicadasatodososdispositivos):
@media print {
body {
font-size: 10pt ;
}
}
@media screen {
body {
font-size: 13px ;
}
}
@media screen , print {
body {
line-height: 1.2 ;
}
}
Mas,comaevolu çãodastecnologiasdedesenvolvimento web,asdiferençasentre
ostiposde devices,antestãodiscrepantes,come çaramadesaparecer.Comoescreveu
DiegoEis emseuartigosobreMediaQueries(http://ow.ly/cQ/eight.oldstyle/five.oldstyleG):
Cada vez mais surgem dispositivos de diversos tamanhos com hardwares bem pa-
recidos com os desktops. Isso faz com que a navega ção destes aparelhos tenha uma
experiência muito próxima de desktop. Um exemplo atual é o iPhone. Sua tela tem
boa qualidade e seu navegador renderiza as páginas como um navegador normal de
desktop. Logo, não tem motivo para prepararmos um layout e um CSS com media type
HANDHELD para o iPhone. Apesar de ele ser um handheld, ele não trabalha como
um. Contudo, ele também não trabalha como um desktop. Mesmo a renderização do
MobileSafari sendo idêntica a de um desktop, o comportamento do usuário e a forma
de navegação são diferentes. Logo, temos um meio termo. Não podemos disponibilizar
um CSS para HANDHELD, nem um CSS totalmente SCREEN.
Asolução?MediaQueries.
/eight.oldstyle/four.oldstyle

## Página 93

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
/five.oldstyle./two.oldstyle M/e.sc/d.sc/i.sc/a.scQ/u.sc/e.sc/r.sc/i.sc/e.sc/s.sc
Querdizer,começouanão/f_icartãoclaraadiferen çaentreosváriostiposde devicese
suascapacidades,deixandoos M e d i a T y p e snumaposiçãode,sozinhos,nãoatende-
remmaisàsnecessidadesdedesenvolvimento,jáquemuitos,comoocitadoiPhone,
acabaram/f_icandonuma“zonacinzenta”de medias,tendocaracterísticastantode
handheld,quantode desktop.
Asolução?MediaQueries.Comomuitobemargumentou SérgioLopesemseu
artigosobre Media Queries(http://ow.ly/cQ/eight.oldstyleDi),Melhor do que separar os dispositi-
vos em desktop (screen) e mobile (handheld), os novosMediaQueries permitem que
foquemos principalmente no tamanho da tela onde vamos exibir o conteúdo.
Ouseja, Media Queries-quejáéumarecomenda çãodoW/three.oldstyleCdesdejunhode
/two.oldstyle/zero.oldstyle/one.oldstyle/two.oldstyle(http://ow.ly/cUjIw)-tornarampossívelaevoluçãoparaumnovoníveldees-
peci/f_icaçãodeestilospara web sites.Porexemplo,épossívelindicarumCSSsomente
para devicescomteladeaté 320px:
<link rel="stylesheet" media="screen and (max-width: 320px)"
href="320.css">
Casosequeirausarváriasdeclara çõesemsomenteumarquivo,podemosfazer:
@media screen and (min-width: 320px) {
body {
font-size: 80% ;
}
}
@media screen and (min-width: 480px) {
body {
font-size: 90% ;
}
}
Masnãosomenteisso.Existeumagamaextensadeparâmetrosde M e d i a Q u e -
ri e s.
/five.oldstyle./three.oldstyle P/a.sc/r.sc/acircumflex.sc/m.sc/e.sc/t.sc/r.sc/o.sc/s.sc /p.sc/a.sc/r.sc/a.sc /t.sc/r.sc/a.sc/b.sc/a.sc/l.sc/h.sc/a.sc/r.sc /c.sc/o.sc/m.scM/e.sc/d.sc/i.sc/a.scQ/u.sc/e.sc/r.sc/i.sc/e.sc/s.sc
Seguindoalgumadassintaxesapresentadasanteriormente,épossívelespeci/f_icaro
usodeestilosseparadosporarquivooublocosdentrodomesmoarquivousandoum
/eight.oldstyle/five.oldstyle

## Página 94

/five.oldstyle./three.oldstyle. ParâmetrosparatrabalharcomMediaQueries CasadoCódigo
ouváriosdosparâmetrosaseguir.Importanteressaltarqueamaioriadosparâmetros
podeserpre/f_ixadocommin-ou max-,querepresentam,respectivamente,“maiorou
iguala”e“menorqueouiguala”(assimcomofoimostradonoexemploanterior).
Vamosveralgunsdessesparâmetros:
aspect-ratio
• V a l o r:<proporção>
• Media:visual,tátil
• Aceitamin/max:sim
Descreveapropor çãodaáreadeexibi çãodo browserusado.Ovalorécomposto
dedoisnúmerosinteirospositivos,separadosporumcaracteredebarra(“/”).Isso
representaapropor çãodepixelsnahorizontal(primeirotermo)parapixelsnaver-
tical(segundotermo).
Porexemplo,paraaplicarregrascomajaneladonavegadorem widescreende
proporção/one.oldstyle/six.oldstyle:/nine.oldstyle:
@media screen and (aspect-ratio: 16/9) {
[...]
}
color
• V a l o r:<cor>
• Media:visual
• Aceitamin/max:sim
Indicaonúmerodebitsporcomponentedecordodispositivo. Seelenãoé
umdispositivodecor,ovaloréiguala/zero.oldstyle.Seoscomponentesdecortêmdiferentes
númerosdebits,omenornúmeroéusado.Porexemplo,seum d i s p l a yutiliza/five.oldstylebits
paraazulevermelhoe/six.oldstylebitsparaverde,odispositivovaiusar/five.oldstylebits.Seodispositivo
usacoresindexadas,onúmeromínimodebitsporcomponentedecornatabelade
coreséusado.
Porexemplo,paraespeci/f_icarregrasparadispositivoscoloridos:
/eight.oldstyle/six.oldstyle

## Página 95

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
@media all and (color) {
[...]
}
Ou,paraestilosquesomenteserãoaplicadosemdispositivoscom,pelomenos,
/four.oldstylebitsdecor:
@media all and (min-color: 4) {
[...]
}
Ouaindacomnomáximo/one.oldstyle/six.oldstylebitsdecores:
@media (max-color: 16) {
[...]
}
color-index
• V a l o r:<inteiro>
• Media:visual
• Aceitamin/max:sim
Descreveonúmerodeentradasnatabeladecoresdodispositivo.Seodispositivo
nãopossuirtabeladecores,entãoovaloré/zero.oldstyle.
Porexemplo,paraespeci/f_icarquealgumasregrasserãoaplicadasatodos devices
comcoresindexadas:
@media all and (color-index) {
[...]
}
Dispositivoscom,pelomenos,/two.oldstylecoresindexadas:
@media (min-color-index: 2) {
[...]
}
Ouincorporarumafolhadeestilospara,somente,dispositivoscommenosde
/two.oldstyle/five.oldstyle/six.oldstylecoresindexadas:
/eight.oldstyle/seven.oldstyle

## Página 96

/five.oldstyle./three.oldstyle. ParâmetrosparatrabalharcomMediaQueries CasadoCódigo
<link rel="stylesheet" media="all and (max-color-index: 256)"
href="http://foo.bar.com/stylesheet.css" />
device-aspect-ratio
• V a l o r:<proporção>
• Media:visual,tátil
• Aceitamin/max:sim
Descreveapropor çãodo d i s p l a ydodispositivo.Ovalorécompostodedoisnú-
merosinteirospositivos,separadosporumcaracteredebarra(“/”).Issorepresentaa
proporçãodepixelsnahorizontal(primeirotermo)parapixelsnavertical(segundo
termo).
Porexemplo,paraaplicarregrasemdispositivos widescreen:
@media screen and (device-aspect-ratio: 16/9),
screen and (device-aspect-ratio: 16/10) {
[...]
}
device-height
• V a l o r:<comprimento>
• Media:visual,tátil
• Aceitamin/max:sim
Descreveaaltura,empixels,do d i s p l a ydoaparelho.Parameioscontínuos,éa
alturadatela;parameiospaginados,éaalturadotamanhodafolhadecadapágina.
Porexemplo,aplicarumafolhadeestiloaumdocumentoquandovisualizado
numatelamenorque/four.oldstyle/eight.oldstyle/zero.oldstylepxdealtura:
<link rel="stylesheet" media="screen and (max-device-height: 379px)"
href="style.css">
/eight.oldstyle/eight.oldstyle

## Página 97

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
device-width
• V a l o r:<comprimento>
• Media:visual,tátil
• Aceitamin/max:sim
Descrevealargura,empixels,do d i s p l a ydoaparelho.Parameioscontínuos,é
alarguradatela;parameiospaginados,éalarguradotamanhodafolhadecada
página.Obviamente,<comprimento>nãopodeserumvalornegativo.
Porexemplo,aplicarumafolhadeestiloaumdocumentoquandovisualizado
numatelamenorque/eight.oldstyle/zero.oldstyle/zero.oldstylepxdelargura:
<link rel="stylesheet" media="screen and (max-device-width: 799px)"
href="style.css">
grid
• V a l o r:<inteiro>
• Media:todas
• Aceitamin/max:não
Determinasesetratadeumdispositivodegradeouumdispositivodemapade
bits(bitmap).Seodispositivoébaseadoemgrade(talcomoumterminalTTYou
umvisordotelefone,comapenasumafonte),ovaloré/one.oldstyle;casocontrário,é/zero.oldstyle.
Porexemplo,paraaplicaralgumasregrasatodosdispositivosassim:
@media (grid) {
[...]
}
Paraaplicarumestiloemdispositivosmóveiscom d i s p l a yde/one.oldstyle/five.oldstylecaracteresou
menos:
@media handheld and (grid) and (max-width: 15em) {
[...]
}
/eight.oldstyle/nine.oldstyle

## Página 98

/five.oldstyle./three.oldstyle. ParâmetrosparatrabalharcomMediaQueries CasadoCódigo
Notequeaunidade“em”temumsigni/f_icadoespecialparadispositivosassim,já
quealarguraexatadeum“em”nãopodeserdeterminada,assume-seque/one.oldstyleeméa
larguradeumacéluladagradehorizontaleaalturadeumacélulavertical.
height
• V a l o r:<comprimento>
• Media:visual,tátil
• Aceitamin/max:sim
Altura,empixels,dajaneladonavegadorsendousado.Parameioscontínuos,éa
alturada viewport,incluindootamanhodabarraderolagem;parameiospaginados,
éalargurada“pagebox”daimpressora. <comprimento>nãopodeserumvalor
negativo.
Porexemplo,especi/f_icaralgumasregrasCSSparadispositivoscomaalturada
janelado browserem/three.oldstyle/zero.oldstyle/zero.oldstylepx:
@media screen and @media (height: 300px) {
[...]
}
Oucomaalturamenorque/six.oldstyle/zero.oldstyle/zero.oldstylepx:
@media screen and @media (max-height: 599px) {
[...]
}
monochrome
• V a l o r:<inteiro>
• Media:visual
• Aceitamin/max:sim
Indicaonúmerodebitsporpixelemdispositivosmonocromáticos(escalade
cinza).Seodispositivonãoformonocromático,ovalorézero.
Porexemplo,paraaplicarestilosemqualquerdispositivomonocromático:
/nine.oldstyle/zero.oldstyle

## Página 99

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
@media all and (monochrome) {
[...]
}
Paraaplicarestilosemqualquerdispositivomonocromáticocom,pelomenos,/two.oldstyle
bitsporpixel:
@media all and (min-monochrome: 2) {
[...]
}
orientation
• V a l o r:landscape|portrait
• Media:visual
• Aceitamin/max:não
Indicaseodispositivoestáemmodo“paisagem”(telaémaislargaquealta)ou
“retrato”(telaémaisaltaquelarga).
Então,paraseaplicarregrasparadispositivosqueestãonomodo“paisagem”,
bastausar:
@media all and (orientation:landscape) {
[...]
}
resolution
• V a l o r:<resolução>
• Media:bitmap
• Aceitamin/max:sim
T r a t a s o b r e a r e s o l ução(densidadedepixels)dodispositivo,quepodeserespeci-
/f_icadaempontosporpolegada(dpi)oupontosporcentímetro(dpcm).Porexemplo:
/nine.oldstyle/one.oldstyle

## Página 100

/five.oldstyle./three.oldstyle. ParâmetrosparatrabalharcomMediaQueries CasadoCódigo
@media (resolution: 72dpi) {
[...]
}
@media (min-resolution: 118dpcm) {
[...]
}
U m a<resolução>semalgumdospre/f_ixos“min-”ou“max-”nuncavaiatuarem
devicescompixelsnão-quadrados( non-square pixels).
scan
• V a l o r:progressive|interlace
• Media:tv
• Aceitamin/max:no
Tratasobreoprocessodeescaneamentoqueumdispositivodotipo“TV”pode
fazer.Porexemplo,paraaplicarumafolhadeestiloapenasparatelevisõescomes-
caneamentoprogressivo:
@media tv and (scan: progressive) {
[...]
}
width
• V a l o r:<comprimento>
• Media:visual,tátil
• Aceitamin/max:sim
Largura,empixels,dajaneladonavegadorsendousado.Parameioscontínuos,
éalargurada viewport,incluindootamanhodabarraderolagem;parameiospagi-
nados,éalargurada“pagebox”daimpressora.<comprimento>nãopodeserum
valornegativo.
Porexemplo,especi/f_icaralgumasregrasCSSparadispositivoscomalargurada
janelado browserem/six.oldstyle/four.oldstyle/zero.oldstylepx:
/nine.oldstyle/two.oldstyle

## Página 101

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
@media screen and @media (width: 640px) {
[...]
}
Oucomalarguramenorque/seven.oldstyle/six.oldstyle/eight.oldstylepx:
@media screen and @media (max-width: 767px) {
[...]
}
/five.oldstyle./four.oldstyle O/p.sc/e.sc/r.sc/a.sc/d.sc/o.sc/r.sc/e.sc/s.scL/oacute.sc/g.sc/i.sc/c.sc/o.sc/s.sc
ApesardealgunsdosOperadoresLógicosdeMediaQueriesjáteremsidosmostra-
dosemexemplosanteriores,para/f_icarclarosobresuaexistência,possibilidadese
utilidade,conformeoW/three.oldstyleC(http://ow.ly/cQVfk),osOperadoresLógicosdeMedia
Queriessão:
• “and”e“or”
• “not”
• “only”
andeor
VáriasMediaQueriespodemsercombinadasemumalista(separadaporvírgu-
las)deconsultas.Seumaoumaisdasconsultassãoverdadeiras,todaalistaéverda-
deira;docontrário,éfalsa.Nasintaxedemediaqueries,apalavra and”expressao
operadorlógicoANDea vírgulaexpressaooperadorlógico OR.
Porexemplo:
/* Telas e impressões coloridos */
@media screen and (color), print and (color) {
...
}
not
Ooperadorlógico NOTéindicadopelapalavra not.Apresen çadapalavra not
noiníciodaconsultanegaoresultado,ouseja,seaconsultademídiaforverdadeira,
semo“not”elasetornafalsa(evice-versa).Osnavegadoresquesuportamsomente
/nine.oldstyle/three.oldstyle

## Página 102

/five.oldstyle./five.oldstyle. Váquebrandoseudesignembreakpointsbempensados CasadoCódigo
MediaTypesnãoirãoreconhecerapalavra-chave noteafolhadeestiloassociada,
portanto,nãoseráaplicada.Exemplo:
<link rel="stylesheet" media="not screen and (color)"
href="style.css">
“only"
Apalavra-chave onlypodeserusadaparaesconderasfolhasdeestilodeagentes
deusuáriomaisantigos.Osagentesdevemcome çaraprocessarasconsultasdemídia
com onlycomoseapalavra-chave onlynãoestivessepresente.
<link rel="stylesheet" media="only screen and (color)"
href="example.css">
/five.oldstyle./five.oldstyle V/aacute.sc /q.sc/u.sc/e.sc/b.sc/r.sc/a.sc/n.sc/d.sc/o.sc /s.sc/e.sc/u.sc /d.sc/e.sc/s.sc/i.sc/g.sc/n.sc /e.sc/m.sc /b.sc/r.sc/e.sc/a.sc/k.sc/p.sc/o.sc/i.sc/n.sc/t.sc/s.sc /b.sc/e.sc/m.sc
/p.sc/e.sc/n.sc/s.sc/a.sc/d.sc/o.sc/s.sc
ApesardeexistirmaisdeumadezenadeparâmetrosparaMediaQueries,averdade
équesomentealgunspoucossãousados.Issoocorrenãopelafaltadecuidadoou
competêncianodesenvolvimento,masprincipalmentedevidoaofatodequeasne-
cessidadesatuaisdamaioriadossitesnãorequeremousodemuitosdosparâmetros.
Defato,amaioriadosutilizadosatualmentedizemrespeitoàlarguraealturado d i s -
p l ayeàorienta çãododispositivo.
E,comofoivistoanteriormente,épossíveldeclararregrasCSSespecí/f_icascon-
formeotamanhododispositivoou browser,atravésdosparâmetros device-width
e width(eseuspre/f_ixos). Issolevaaumadiscussãoimportantesobrequaissãoos
breakpoints(ou“pontosdeinterrup ção”)maise/f_icientes,querdizer,os“pontos”em
quesedevetrataro web designdeformadiferenciadaparaqueaexperiênciadequem
estávisitandoositesejaamelhoremaise/f_icientepossível.
QualéomomentodeparardeescreverregrasCSSparaumaresolu çãoecome çar
paraoutra?Seestouescrevendoestilosqueatendamadiversostiposde devices,em
qualmomento,especi/f_icamente,éo“limitedaresolu ção”deumdispositivoeinício
deoutro? Emquemomentodevemospegarnossosidebarejogá-loparabaixodo
nossoconteúdoprincipal? Quandoalarguradodispositivoobrigadoaousuário
scrollar,porexemplo!Issode/f_iniriaumbreakpoint(ou“pontosdeinterrup ção”).
BreakpointssãoosdelimitadoresdasregrasdeCSSparaatenderemadiferentes
especi/f_icações(feitasporvocê,mesmo,aousarosparâmetrosde Media Queries),
/nine.oldstyle/four.oldstyle

## Página 103

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
querdizer,os“pontos”emquesedeveutilizarestilosdiferentesparatrataro web
designdeformadiferenciadaparaqueaexperiênciadequemestávisitanteositeseja
amelhor/maise/f_icientepossível.
Diferentesabordagenssobrebreakpoints
Quando os estudos de web design responsivo estavam bem no início, al-
guns desenvolvedores propuseram o uso debreakpointsconforme a resolução
que determinados dispositivos tinham. Por exemplo, @media only screen
and (min-device-width : 320px) and (max-device-width : 480px) para
smartphones, @media only screen and (min-width : 1224px) paranotebooks
edesktopseassimpordiante. Comojávimos,malissocome çouefoiconstatado
queessaabordagemnãofuncionamuitobem, jáque, conformeaevolu çãodos
dispositivos, é praticamente impossível determinar qualdevice seestáusando
conformearesolu çãonomomentodavisitaaosite.
Portanto,nãoexisteconsensosobrequaisseriamosmelhoresoumaise/f_icientes
breakpointsem web designresponsivo. Pradizeraverdade,existebastantediscre-
pânciadeopiniões,algunschegandoaa/f_irmarquenãoseriaprecisoaespeci/f_ica ção
de breakpoints,massimodesenvolvimentode layoutsqueseadaptariamaquaisquer
resoluções.
Paraosquepensamdeumamaneiradiferentes,apreferênciaésevalerdore-
cursodos breakpointsparaalteraradisposi çãodo layoutconformeodispositivo(ou
largurado browser)queseestejausandonomomento. Paraestescasos,existem
posiçõesdiferentessobrequaisseriamosmelhores(oupreferencialmenteusados)
breakpoints.
Realmentenãoépossívelespeci/f_icarumconjuntode breakpointsquesejam“os
melhores”. Cadaprojetowebtemsuasprópriaspeculiaridadesepedeumaimple-
mentaçãodiferenciadadosdemais.Algunstentaramchegaraum“pontodepartida
genérico”,especi/f_icandobreakpoints-chave,quepodemfacilitaroiníciodequalquer
projeto.Vamosverosquesãomaisconhecidos:
/three.oldstyle/two.oldstyle/zero.oldstyleandUp
/three.oldstyle/two.oldstyle/zero.oldstyleandUp(http://ow.ly/cSIXX):
@media print { }
@media only screen and (min-width: 480px) { ... }
/nine.oldstyle/five.oldstyle

## Página 104

/five.oldstyle./five.oldstyle. Váquebrandoseudesignembreakpointsbempensados CasadoCódigo
@media only screen and (min-width: 600px) { ... }
@media only screen and (min-width: 768px) { ... }
@media only screen and (min-width: 992px) { ... }
@media only screen and (min-width: 1382px) { ... }
@media only screen and (-webkit-min-device-pixel-ratio: 1.5),
only screen and (min--moz-device-pixel-ratio: 1.5),
only screen and (min-device-pixel-ratio: 1.5)
{ ... }
Percebaqueousode Media Queriessedádeforma“crescente”,ouseja,primeiro
contemplandoestilosparadipositivoscomresolu çõesmenorescom 480pxe 600px
(geralmente, smartphonese netbooks),paradepoisabordarosdemaiorresolu ção,
comoostradicionaisPCsedispositivoscomaltaresolu ção(porexemplo,as S m a r t
T V smaisatuais).
LessFramework
LessFramework(http://ow.ly/cSQIb):
/* Tablet Layout */
@media only screen and (min-width: 768px)
and (max-width: 991px) { ... }
/* Mobile Layout */
@media only screen and (max-width: 767px) { ... }
/* Layout largo de mobile */
@media only screen and (min-width: 480px)
and (max-width: 767px) { ... }
/* Retina display */
@media
only screen and (-webkit-min-device-pixel-ratio: 2),
only screen and (min-device-pixel-ratio: 2) { ... }
OspróprioscomentáriosdoLessFrameworkjáajudambastanteaidenti/f_icar
paraquaistiposdenavega çãoasfolhasdeestiloforamprojetadas.Osdesenvolvedo-
/nine.oldstyle/six.oldstyle

## Página 105

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
resde/f_iniramosbreakpointsnoquechamaramde“TabletLayout”,“MobileLayout”,
“Layoutlargodemobile”e“Retinadisplay”(regrasestas,obviamente,somentepara
ospoucosdispositivosquetemoshojequepossuemestacaracterística).
Skeleton
Skeleton(http://ow.ly/cSQ/seven.oldstyle/eight.oldstyle):
/* Menor que 960 */
@media only screen and (max-width: 959px) { ... }
/* Tablet Portrait ao padrão 960 */
@media only screen and (min-width: 768px)
and (max-width: 959px) { ... }
/* Todos tamanhos de mobile */
@media only screen and (max-width: 767px) { ... }
/* Mobile em landscape a tablet Portrait */
@media only screen and (min-width: 480px)
and (max-width: 767px) { ... }
/* Mobile em portrait a mobile em landscape */
@media only screen and (max-width: 479px) { ... }
O Skeletonébemespecí/f_icoaopropor breakpointsparadispositivoslevandoem
consideração,inclusive,aorienta çãousadanomomento( landscapeou portrait).
Querdizer,umplanejamentodaexperiênciadousuáriomaisdetalhadoebemfeito
que,sebemusado,temmaioreschancesdepromoverumaboaexperiênciaaosvisi-
tantesegarantirumaboadosede“agradabilidade”.
TwitterBootstrap
TwitterBootstrap(http://ow.ly/cSLyw):
/* Telefones em landscape e abaixo */
@media (max-width: 480px) { ... }
/* Telefone em landscape a tablet em portrait */
@media (max-width: 767px) { ... }
/nine.oldstyle/seven.oldstyle

## Página 106

/five.oldstyle./six.oldstyle. Gerenciamentodeerros CasadoCódigo
/* tablet em portrait a landscape e desktop */
@media (min-width: 768px) and (max-width: 979px) { ... }
/* Desktop grande */
@media (min-width: 1200px) { ... }
O Twitter Bootstraptambémteveocuidadodeprojetarparaváriosdispositivos
usandoasvaria çõesdeorienta ção.Apesardecontermenos breakpointsqueo Skele-
ton,dácontadorecadotranquilamente(lembrandoqueissoéoquevempordefault
e,sejaláemqualdelesvocêestejaseinspirando,podeacrescentarouretirarquantos
breakpointsquiser).
/five.oldstyle./six.oldstyle G/e.sc/r.sc/e.sc/n.sc/c.sc/i.sc/a.sc/m.sc/e.sc/n.sc/t.sc/o.sc /d.sc/e.sc /e.sc/r.sc/r.sc/o.sc/s.sc
VimosquaisostipospossíveisdeparâmetrosparaMediaQueriesecomoépos-
sível,atravésdeoperadoreslógicos,“re/f_inar”consultasamídiasespecí/f_icas.Mas,e
quandoascoisasdãoerrado?Ese,poracaso,ocorreralgumerrodesintaxeoualgum
parâmetroinexistenteforespeci/f_icado?
Tiposdemídiadesconhecidosserãoavaliadoscomo false.Efetivamente,eles
sãotratadosdeformaidênticaparaostiposconhecidosdemídiaquenãocorres-
pondemaotipodemídiadodispositivo.Porexemplo,aconsultademídia unknown
vaiseravaliadacomo false,anãoserque unknownsejaumtipodemídiasuportada.
ParâmetrosdeMediaQueriesdesconhecidos
Os agentes de usuário representarão uma consulta de mídia comonot all
quandoalgumdosparâmetrosdemídianãoforconhecido.Porexemplo:
<link rel="stylesheet" media="screen and (max-weight: 3kg)
and (color), (color)"
href="style.css">
Aprimeiraconsultaserárepresentadacomo not all eavaliadacomofalsa;a
segunda,comoseaprimeiranãotivessesidoespeci/f_icada.
Vejaumoutroexemploqueresultaráem not all etentecompreenderomotivo:
@media (min-orientation:portrait) {
[...]
}
/nine.oldstyle/eight.oldstyle

## Página 107

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
Adivinhou?Oparâmetro orientationnãoadmitepre/f_ixomin-!
ValoresdesconhecidosemparâmetrosdeMediaQueries
Talcomoacontececomparâmetrosdesconhecidos,agentesdeusuáriointerpre-
tamcomo not all quandoumdos valoresdealgumparâmetroespeci/f_icadonãofor
conhecido.Porexemplo,essasduasconsultasseriaminterpretadascomo not all:
@media (color: 20example) {
[...]
}
@media (min-width: -100px) {
[...]
}
MediaQueriesmalformadas(errosdesintaxe)
Osagentesdeusuárioconseguemlidarcomsímbolosinesperadasencontrados
aoanalisarumaconsultademídia. Eles“lêem”atéo/f_inaldaconsultaobservando
correspondênciadeparesde (), [], {}, ""e "elidandocorretamentecomescapes.
Consultasdemídiacom tokensinesperadossãointerpretadascomo not all.
/* Aplicado somente a dispositivos "speech" */
@media (example, all,), speech {
[...]
}
/* Aplicado somente a dispositivos "screen" */
@media &test, screen {
[...]
}
/* Sem espaço entre "and" e "(" */
@media all and (color) {
[...]
}
/* Ponto e vírgula?! */
@media test ;,all {
[...]
}
/nine.oldstyle/nine.oldstyle

## Página 108

/five.oldstyle./seven.oldstyle. UsoconscientedeMediaQueries CasadoCódigo
/five.oldstyle./seven.oldstyle U/s.sc/o.sc /c.sc/o.sc/n.sc/s.sc/c.sc/i.sc/e.sc/n.sc/t.sc/e.sc /d.sc/e.scM/e.sc/d.sc/i.sc/a.scQ/u.sc/e.sc/r.sc/i.sc/e.sc/s.sc
MuitacoisafoivistasobreMediaQueries.Evidentemente,nãoseesperaque,numa
primeiralidadetodoesseconteúdo,tudosejaentendidoeabsorvido.Naverdade,
amelhormaneiraparaentendere/f_ixartudoissoécolocandoalgunsprojetosem
prática!
Mas,mesmoantesdesequercome çaramexercomasfantásticasMediaQueries,
éprecisolevaremconsidera çãoalgumasquestõesmuitoimportantessobreseuuso,
taiscomoseusararquivosexternosounão,amelhormaneiradeusar breakpoints,se
émelhorcome çarpelostamanhosmenoresoumaiores,etc.Háalgumconteúdoso-
breissocirculandona webe,felizmente,épossívelencontraralgumasconsidera ções
importantesnoblogdozomig(http://ow.ly/cTV/four.oldstyleJ).Vamosveralgumasdelas.
MediaQueriesemarquivosseparadosounumúnicoarquivo
Segundofoivistoanteriormente, épossívelrealizarconsultasdemídiacha-
mandofolhasdeestiloemseparadoou,dentrodeummesmoarquivo,realizara
diferenciaçãodeestilosusando breakpoints.
<link rel="stylesheet" type="text/css"
media="screen and (min-width:480px)"
href="480.css">
<link rel="stylesheet" type="text/css"
media="screen and (min-width:768px)"
href="768.css">
@media only screen and (min-width: 480px) { ... }
@media only screen and (min-width: 768px) { ... }
Masqualéamelhormaneiradeusar? Chamarváriosarquivosexternos,um
paracada breakpoint,ousomenteumarquivocomtodos breakpointsespeci/f_icados?
Naverdade,arespostanãoétãosimpleseháalgumasconsidera çõesaesserespeito.
Quandoseusachamarváriosarquivosdiferentes,algoimportanteaserlevado
emcontaéque browsersquenãooferecensuporteaMediaQueriesnãoirãobaixar
osarquivos.Também,mesmoquandoháumarquivoquenãoseráusadoparaalgum
tipode media,esteébaixadodequalquermaneira.Porexemplo,umiPadvaibaixar
oarquivocom (max-width:700px).Sobreestaquestão,existemprósecontras.
Prósemseusar/one.oldstylearquivo:
/one.oldstyle/zero.oldstyle/zero.oldstyle

## Página 109

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
• Somente/one.oldstylerequisiçãoHTTP
• Maisdifícildeesquecerdeatualizar
Contrasemseusar/one.oldstylearquivo:
• Tamanhodoarquivo/f_icamaior
• Amedidaqueoprojetocresce,amanuten ção/f_icamaisdifícil
• UsodesoluçõesJavaScriptparafuncionaremIE/eight.oldstyleprabaixo
Prósemseusarváriosarquivos:
• Parabrowsersquenãosuportam,oarquivopadrãoémenor
• Organização/manutenção/f_icammelhores
Contrasemseusarváriosarquivos:
• VáriasrequisiçõesHTTP
• Maisfácildeesquecerdeatualizaralgo
Comoodesenvolvimentoparaweb nãoéfeitodetecnologiasfuncionandoem
separadoelevandoemcontaqueváriasrequisi çõesHTTPacabamsendomaislen-
tasquesomenteumarquivodetamanhomaior,arecomenda çãoéquesejausada
somenteumafolhadeestilos .Valelembrarquenãoháumarespostaúnica,apenas
umarecomendação.Semprevaidependermuitodasuasitua ção.
MediaQueries“sobrepostas”ou“empilhadas"
Apesardenãoseremtermoso/f_iciaisdentrodowebdesignresponsivo,“sobre-
postas”e“empilhadas”traduzembemaspossibilidadesesitua çõesquepodemacon-
tecerquandoseestádesenvolvimentosoba/f_iloso/f_iadoresponsive web design.Então,
independentementedeseusarumouváriosarquivosdeestilo,fatoéqueépossível,
atravésdos breakpoints,sobreporouempilharasregrasusadas.
Vejaesteexemplo:
@media all and (min-width:500px) {
body {
background: blue;
/one.oldstyle/zero.oldstyle/one.oldstyle

## Página 110

/five.oldstyle./seven.oldstyle. UsoconscientedeMediaQueries CasadoCódigo
font-family: serif;
}
}
@media all and (min-width:700px) {
body {
background: red;
color: #FFF ;
}
}
Percebaqueasespeci/f_icaçõesde medianãosãomutuamenteexclusivas-quer
dizer,seo viewportnomomentodoacessofor/eight.oldstyle/zero.oldstyle/zero.oldstylepx,ambasasregrasentrarãoem
ação-e,seissoforfeitodessamaneirasemadevidaconsciênciadequalefeitose
querobter,oquesevaiconseguir,no/f_inal,émuitadordecabe çaehorasamaisde
manutençãodoarquivo...Nãoháproblemaemfazerisso,desdequeestapráticaseja
algoconsciente!
TambémnãoéporqueagoraseestáusandoMediaQueriesnoarquivoqueas
regrasmaiselementaresdeCSSdeixamdevaler.Então,a cascataeaespeci/f_icidade
aindaestãopresentes! Supondoumacessocom viewportde/eight.oldstyle/zero.oldstyle/zero.oldstylepx,numcódigo
comoesse,apáginaserárenderizadacomfundoazulaoinvésdevermelho:
@media all and (min-width:700px) {
body {
background: red;
color: white;
}
}
@media all and (min-width:500px) {
body {
background: blue;
font-family: serif;
}
}
Para/f_insdeorganização,manutençãoefacilidadedeentendimentodalógicados
estilosquecompõemoprojeto,geralmenteémaisfácil“empilhar”os breakpointse
separarasregrasdevidamente,comoem:
/one.oldstyle/zero.oldstyle/two.oldstyle

## Página 111

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
@media all and (min-width:500px) and (max-width:699px) {
body {
background: blue;
font-family: serif;
}
}
@media all and (min-width:700px) {
body {
background: red;
color: white;
font-family: serif;
}
}
Vejaque,paraquesejaaplicadaumafamíliadefonteserifada( font-family:
serif),foiprecisorepetiroparpropriedade/valor,jáqueasregrasparaum b re a k -
pointespecí/f_iconãoentramemaçãoparaoutro.Paraasregrasgenéricas,quedevem
entrarema çãosempre,orecomendadoédeixar“fora”deumdeclara çãode media.
Prósdasobreposi ção:
• Tamanhodearquivomenor(nãoéprecisorepetirregras)
• Fácildeatualizarregrascompartilhada(jáquesãodeclarassóumavez)
Contrasdasobreposi ção:
• Tamanhosdearquivosmaiores
• Imagenssubstituídas/escondidasempartesposterioresdocódigocontinuam
sendobaixadaspornavegadoresbaseadosemWebKit
Prósdoempilhamento:
• Browserssomentebaixamimagenscondizentesao breakpointatual
Contrasdoempilhamento:
• Arquivosmaiores,jáquealgumasregrassãorepetidasemvários breakpoints
• Ematualizações,émaisfácildeesquecerdeatualizarregrasrepetidasemal-
guns breakpoints
/one.oldstyle/zero.oldstyle/three.oldstyle

## Página 112

/five.oldstyle./seven.oldstyle. UsoconscientedeMediaQueries CasadoCódigo
Sobreporestilospodedeixarocódigomaisenxuto,masamanuten çãoeenten-
dimentodocódigo/f_icammaiscomplicados. Empilhardeixaocódigomaior,mas
maissimples(emboraalgumasvezesrepetido). Quandoosestilosentreos b re a k -
pointssãobastantediferentes(sitemuitodiferentepara mobiledoquepara desktop,
porexemplo),éaconselhadoempilhar;docontrário(casosmaiscomuns),sobrepor.
VersõesantigasdoIE:ComentáriosCondicionaisouJavaScript?
ParaversõesdoInternetExploreranterioresà/nine.oldstyle,nãohásuporteparaMediaQue-
ries(poressavocêjáesperava!).ParaamaioriadosprojetosnoBrasil,aindaéim-
portantedarsuportepara,pelomenos,IE/seven.oldstyle+.Éprecisoentãofazerissodealguma
maneira.Paratanto,épossívelusarComentáriosCondicionaisoualgumasolu ção
JavaScript.
EmrelaçãoaosComentáriosCondicionais,nopróprioblogdaMicroso/f_tépos-
sívelencontrarsolu çõesparaespeci/f_icarestilosparaWindowsPhone(http://ow.ly/
cTZ/nine.oldstylei).Umexemploseria:
<link rel="stylesheet" media="all" href="global.css">
<link rel="stylesheet" media="all and (max-width: 700px)"
href="mobile.css">
<!--[if IEMobile 7]>
<link rel="stylesheet" media="all" href="mobile.css">
<![endif]-->
Ou:
<link rel="stylesheet" media="all" href="global.css">
<link rel="stylesheet" media="all and (min-width: 700px)"
href="desktop.css">
<!--[if (lt IE 9)&(!IEMobile 7)]>
<link rel="stylesheet" media="all" href="desktop.css">
<![endif]-->
Quantoasolu çõesJavaScript,existemmuitasemuitas,masalgumasdasmais
conhecidaseusadassão:
• Respond.Suportesomenteosparâmetros min-widthand max-width,masé
bastantee/f_icientenoquesepropõe.
/one.oldstyle/zero.oldstyle/four.oldstyle

## Página 113

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
• css/three.oldstyle-mediaqueries.js.ÉmaispesadoemaislentoqueoRespond,massuporta
maisparâmetrosdeMediaQueries.
Nãoseesque çaque,paraqueosarquivosnãosejamexecutadostambémem
navegadoresdequalidade,éprecisocondicionarsuachamada:
<!--[if (lt IE 9)&(!IEMobile 7)]>
<script src="assets/js/respond.min.js"></script>
<![endif]-->
PrósdeComentáriosCondicionais:
• FuncionasemJavaScript
• Todosos“prós”deMediaQueriesemváriosarquivos
ContrasdeComentáriosCondicionais:
• Usasomente/one.oldstyleestiloparaIEsantigos
• Todosos“contras”deusarMediaQueriesemváriosarquivos
Prósdesolu çõesJavaScript:
• VáriosbreakpointsparaIE(inclusivemudandoemtemporeal)
• Todosos“prós”emseusar/one.oldstylesóarquivoparaMediaQueries
Contrasdesolu çõesJavaScript
• NãofuncionaquandooJavaScriptestádesabilitado
• Todosos“contras”emseusar/one.oldstylesóarquivoparaMediaQueries
NoBrasil,infelizmenteaporcentagemdeusodeIEabaixodo/nine.oldstyleaindaéalta.
U s a r s o l uçõesJavaScriptparaoproblemadenão-suporteaMediaQueriesemIE/eight.oldstyle
parabaixocertamentetornaavidadodesenvolvedormaisfácile,convenhamos,a
maioriausa(oudeveriausar)algumscriptdealertaparaatualiza çãodonavegador
quandosetratadeumavisitaapartirdosantigosInternetExplorers!Conhe çabem
seupúblicoparasaberquaisnavegadoreselesusam.
/one.oldstyle/zero.oldstyle/five.oldstyle

## Página 114

/five.oldstyle./eight.oldstyle. MediaQueriesnaprática CasadoCódigo
/five.oldstyle./eight.oldstyle M/e.sc/d.sc/i.sc/a.scQ/u.sc/e.sc/r.sc/i.sc/e.sc/s.sc /n.sc/a.sc /p.sc/r.sc/aacute.sc/t.sc/i.sc/c.sc/a.sc
Vamosàaplica çãopráticadealgunsdosconceitosdeMediaQueriesvistos.Como
vocêdeveselembrar,nossositedeexemplojácontacommuitascaracterísticasde
umsiteresponsivo,tendoimagens(evídeos)/f_lexíveiseamaioriadasáreasdecon-
teúdopossuemlarguravariável,conformearesolu çãoda viewport.Entretanto,ainda
nãoháaplica çãodeMediaQueries,entãoosite/f_ica“espremido”quandovistoem
determinadasresoluções.
Senadafossefeito,aindaassimseriaumasolu çãoparcialmenteaceitável,jáque
oconteúdoaindaseriacompletamenteacessível,independentedaresolu ção.Entre-
tanto,comojáfoimostrado,atravésdeMediaQueries,nóspodemosplanejarme-
lhorcomoseráaexperiênciadosvisitantes,alterando(ouexibindo;ouocultando)a
disposiçãodoselementos,conformeaexperiênciaquesequeiraoferecer.
Porexemplo,quandoaresolu çãodonavegadornomomentodavisitafordelar-
/one.oldstyle/zero.oldstyle/six.oldstyle

## Página 115

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
guradeaté/six.oldstyle/four.oldstyle/zero.oldstylepx,ositenãoseráapresentadoemcolunas,massimcomoconteúdo
principalvindoemprimeirolugar(lógico)easidebarembaixo.Paratanto,vamos
acrescentaralgumaslinhasdeCSSao/f_inaldoatualarquivodositedeexemplo,cri-
andoum breakpointquecontempleresolu çõesdeaté 640px:
@media all and (max-width: 640px) {
.content-main {
float :none;
}
.content-sidebar {
float: none;
}
}
Comisso,semprequearesolu çãodonavegadordodipositivousadoformenor
ouiguala/six.oldstyle/four.oldstyle/zero.oldstylepx,adivisãode“colunaprincipal”e“colunasecundária”nositenão
maisexistirá,sendoapresentadonumasósequência.
Naverdade,ofatodeomenudenavega çãoprincipalestarsendoapresentado
emduascolunaspodeserumcontratempoparaquemacessausandoumaresolu ção
/one.oldstyle/zero.oldstyle/seven.oldstyle

## Página 116

/five.oldstyle./eight.oldstyle. MediaQueriesnaprática CasadoCódigo
bempequena.Vamosresolver,inserindooseguintetrechodecódigoantesdamedia
queriamostradaanteriormente:
@media all and (max-width: 320px) {
.main-nav li {
float: none;
width: auto;
}
}
Códigoquegarantiráaseguinterenderiza ção:
/one.oldstyle/zero.oldstyle/eight.oldstyle

## Página 117

CasadoCódigo Capítulo/five.oldstyle. MediaQueries
Pensandobem,talvezofatodeasnotíciasseremapresentadasemduascolunas
tambémnãocontribuaparaumaboaexperiênciadosvisitantes.Vamosalterarisso
no breakpointpararesoluçãodeaté 640px,que/f_icaráassim:
@media all and (max-width: 640px) {
.content-main {
float: none;
}
.last-content-call {
float: none;
width: auto;
}
.content-sidebar {
float: none;
}
}
Oqueresultaráem:
Comovocêverádepoisque/f_izeralgunsprojetosepraticarbastante,omaisdifícil
nãoécodi/f_icarsitesresponsivos.Overdadeirodesa/f_ioéfazerumbomplanejamento
/one.oldstyle/zero.oldstyle/nine.oldstyle

## Página 118

/five.oldstyle./eight.oldstyle. MediaQueriesnaprática CasadoCódigo
decadaumdossitesparadiferentes r a n g e sderesoluçõesparagarantirque,emcada
umdeles,ovisitantetenhaumaboaexperiênciadeuso,independentementedequal
dispositivoestejausando.
Seráqueamelhorformadevenceressedesa/f_ioéencararo mobilelogodecara?
/one.oldstyle/one.oldstyle/zero.oldstyle

## Página 119

C/a.sc/p.sc/iacute.sc/t.sc/u.sc/l.sc/o.sc/six.oldstyle
TópicosdeWebMobile
Ocaminhotra çadoatravésdastécnicasparasefazerumbom webdesignresponsivo
foiemocionante!Vimosmuitasdasestatísticasqueprovamqueodesenvolvimento
mobilenãoéumameratendência,comosugeremalguns.Depois,vimosostrêspila-
resdodesenvolvimento mobile:Layout/f_luído,imagens(eoutrosrecursos)/f_lexíveis
eMediaQueries.Conhecendoesabendousarestatrincapoderosa,certamentevocê
estápreparadotecnicamenteparalidarcomwebdesignresponsivo.
Mas,comofoialertadono/f_imdocapítulosobreMediaQueries,odesa/f_iomaior
nãoédominarapartetécnicadowebdesignresponsivo;omaiordesa/f_ioésaber
“como”,“quando”,“se”,“onde”esaberexplicartodosos“porques”deusarumaou
outratécnicaresponsiva.
Umaabordagemimportanteparaseobterowebdesignresponsivoéo Mobile
First!MobileFirst(ou Dispositivo Móvel Primeiro)éumametodologiadedesenvol-
vimentowebqueapregoaquedeve-se primeiroplanejarodesignparadispositivos
móveise,sódepois,ir“aumentando”ospossíveisdispositivos,atésechegarao desk-
t o p.Emtermosmaissimples, domenorparaomaior dispositivo.

## Página 120

/six.oldstyle./one.oldstyle. OqueéMobileFirst? CasadoCódigo
/six.oldstyle./one.oldstyle O/q.sc/u.sc/e.sc /eacute.scM/o.sc/b.sc/i.sc/l.sc/e.scF/i.sc/r.sc/s.sc/t.sc/question.sc
M o b i l e F i r s t(ou“MóvelPrimeiro”)éumametodologia//f_iloso/f_ia/estratégiacriadapor
LukeWroblewski(http://ow.ly/dPqs/two.oldstyle)queapregoaque,nodesenvolvimentoemque
o designresponsivoélevadoemconta(ouseja,todoequalquerprojeto webseua
partirdaleituradesteLivro),deve-se primeiroplanejarparadispositivosmóveis
-e,somentedepois,projetar,gradualmente,paradispositivosmaiores.Emtermos
maissimples: do menor para o maior.
Atualmente,játemosmuitadiversidadededispositivos,desdeosmóveis( p h o -
nes, smartphones, tablets),passandopelosespecializados( eReaders, T V s,etc),até
osmaistradicionais( desktops, laptops, netbooks).Eumdosdesa/f_iosdodesenvolvi-
mento webmoderno(epro/f_issional)édarsuporteatodosestes(eosqueaindaestão
porvir).
Eéporissoqueaabordagem M o b i l e F i r s tétãoe/f_iciente:começarcom mobilee
projetarcommelhoramentoprogressivo( progressive enhancement)permiteabran-
gertodosos devices.Qualquerdispositivocomacessoa webserácapazdeacessaro
siteeterumaexperiênciafuncional.Emseguida,usandodete çãoderecurso,carre-
gamentocondicionalde scripts, Media Queries/five.oldstyleeoutrastécnicas,épossívelpermitir
queaexperiênciasejamelhoradaeotimizadaparaocontextododispositivoqueestá
sendousadonomomentodoacesso.
Projetarlevandoemconta M o b i l e F i r s trequerumarevisãoprofundaefunda-
mentaldeumsitee,maisimportante,requeruma revisãomental. Nãosetrata
deumasolu çãorápidaemilagrosa;pelocontrário, M o b i l e F i r s trequerumplaneja-
mentocuidadoso,tempoeexecu çãosériaecomdisciplina-oque,vocêjádeveter
imaginadodepoisdasúltimaspalavras,éalgodifícil. Podeparecerassustadorno
começo,mas,depoisquevocêinternalizaa/f_iloso/f_iado M o b i l e F i r s t,asrecompensas
adquiridassãoenormes!Aoinvésdeterquecriarintera çõestotalmentenovastoda
vezqueumnovodispositivosai,bastaotimizaraexperiênciaparaonovocontexto
semterquereinventararoda(evirarmadrugadas)paraisso.
/six.oldstyle./two.oldstyle P/o.sc/r.sc /q.sc/u.sc/e.scM/o.sc/b.sc/i.sc/l.sc/e.scF/i.sc/r.sc/s.sc/t.sc/question.sc
Éabsolutamentecomumqueaconte çaumprofundoequasesintomáticoestranha-
mentoquandosetemcontatocomaabordagemdo M o b i l e F i r s t.A/f_inal,antesdessa
históriatodadewebdesignresponsivo,ojeito“normal”deseelaborardesignspara
weberacome çarumwireframede/nine.oldstyle/six.oldstyle/zero.oldstylepx.Sóapartirdaí,quandoodesignjáesti-
vessepronto,come çaríamosapensaremoutrospontosdoprojeto.
/one.oldstyle/one.oldstyle/two.oldstyle

## Página 121

CasadoCódigo Capítulo/six.oldstyle. TópicosdeWebMobile
Depoisquesetevecontatocomo responsive design,opróximopassodopro-
jetoseria“reduzir”aspropostasde layoutquandoode/nine.oldstyle/six.oldstyle/zero.oldstylepxestivessepronto.Por
queentãofazerocontrário? Porquepensaremfocarodesenvolvimentoparate-
laspequenas,toucheoutrasresitri çõesantesmesmoda“versãodesktop"? Hává-
riasvantagens,taiscomoaqueLukeWroblewskimostraemseuexcelentelivro
(http://ow.ly/dmxcd),quesão:
• Estarpreparadoparaocrescimentoexplosivoenovasoportunidades mobile
emergentes(/eight.oldstyle/five.oldstyle/percent.oldstyledostelefonesvendidosem/two.oldstyle/zero.oldstyle/one.oldstyle/one.oldstylevieramcombrowser)
• Obrigavocêaseconcentrarefocarnasprincipaiscaracterísticasdeseuspro-
dutos/sistemas(oquefazerquandoseperde/eight.oldstyle/zero.oldstyle/percent.oldstyledoespaçoemtela?)
• Permite-lheproporcionarexperiênciasinovadorasatravésdenovastecnolo-
gias(geolocalização,eventosdetoque,etc)
AprincipaltalvezsejaofatodeaabordagemMobileFirstfor çá-loafocarnoque
émaisimportanteeessencialdentreasfuncionalidadesdeseuprojetoweb.A/f_inal,
quandosetratadeumacessofeitoatravésdeumdispositivomóvel,ascondi ções
deusoenecessidadessãobemdiferentesdoacessofeitoatravésdeoutrostiposde
dispositivos. Nãoquesejanecessárioextirparosconteúdosefuncionalidadesque
serãoapresentadosnumdesktop,masestaremosdandoprioridadeaomaisdifícil,
aomaislimitado.
VamospassarporalgunspontosparapoderenxergarqueaabordagemMobile
Firstémuitasvezesamaise/f_icienteparaumsiteresponsivo.
/six.oldstyle./three.oldstyle N/o.sc/t.sc/a.sc/s.sc /g.sc/e.sc/r.sc/a.sc/i.sc/s.sc /s.sc/o.sc/b.sc/r.sc/e.scM/o.sc/b.sc/i.sc/l.sc/e.scF/i.sc/r.sc/s.sc/t.sc
Demaneirageral,aspessoasqueusamdispositivosmóveis/f_icamcom“umolho
nogatoeoutronopeixe": estãorealizandooutrasatividadesenquantousamseus
devices.Issodizmuitacoisasobreasdiferen çasdeplanejamentopara mobilee,em
relaçãoaofocoeobjetividadequeseu siteprecisa,issodiztudo!
Lembre-se dos per/f_is de usomobile: Pesquisar, Explorar/Divertir, Check
in/Status,Editar/Criar.Essesper/f_isfazempartedeseupontodepartidaparaade/f_i-
niçãodesuaestratégiamobile,baseadoemqualdestesseupúblico-alvoprimáriose
encaixaeoqueseu site/sistemadeveproporcionar.
/three.oldstyledospontosmaisimportantesemrelaçãoa sitesparadispositivosmóveissão:
foconoconteúdo,foconoconteúdo efoconoconteúdo.Seconseguiratenderaos
/one.oldstyle/one.oldstyle/three.oldstyle

## Página 122

/six.oldstyle./three.oldstyle. NotasgeraissobreMobileFirst CasadoCódigo
/three.oldstyle,praticamentemetadedeseutrabalhojáestaráfeito! Lembre-sequeaspessoas
precisamconseguiracessaroutrasáreasdeseusitedemaneirafácileintuitiva;por-
tanto,sejaqualforoper/f_ilqueseenquadreemseupúblico,proverumsistemade
navegaçãoigualmentefocadoeintuitivoésempreumaboapedida.
Emsetratandodeexperiênciasmóveis,aperformanceganhaumpesoainda
maior,jáqueaspessoasesperamquesites mobilesejamtãorápidosquantositesvistos
no desktop(oumais!).Aperformanceeotimiza çãona web,emespecialnocontexto
móvel,éfatordecisivodesucesso/crescimentodeumnegócio online.Emseuartigo
“/one.oldstyle/four.oldstylefatossobreperformanceWebeotimizações”(http://ow.ly/e/zero.oldstyleCoh),SérgioLopes
lembroubemdealgunsfatosaesserespeito:
• ParaaAmazon,/one.oldstylesamaisnocarregamentodapáginacusta/one.oldstyle,/six.oldstylebilhãodedóla-
resporano;
• OtráfegodoYahoo!aumenta/nine.oldstyle/percent.oldstyleacada/four.oldstyle/zero.oldstyle/zero.oldstylemsdemelhoranavelocidade;
• Aocortar/two.oldstyle,/two.oldstylesdalanding pagedoFirefox,aMozillaaumentouonúmerode
downloadsem/one.oldstyle/five.oldstyle/percent.oldstyle;
• UmexperimentodoGoogleaumentouocarregamentode/zero.oldstyle,/four.oldstylespara/zero.oldstyle,/nine.oldstyles. O
tráfegodebuscascaiu/two.oldstyle/zero.oldstyle/percent.oldstyle;
• AMicroso/f_tmostrouque/two.oldstylesamaisdelatêncianoBingdiminuíamofatura-
mentoem/four.oldstyle,/three.oldstyle/percent.oldstyle;
• Umadiminuiçãode/six.oldstylespara/one.oldstyle,/two.oldstylesnapáginadoShopzillaaumentouasvendas
em/one.oldstyle/two.oldstyle/percent.oldstyle;
• /five.oldstyle/zero.oldstyle/percent.oldstyledosusuáriosmobileabandonamum siteseelenãoabreematé/one.oldstyle/zero.oldstyles. E/three.oldstyle
emcada/five.oldstylenãovoltammais;
• Desde/two.oldstyle/zero.oldstyle/one.oldstyle/zero.oldstyle,oGoogleconsideraavelocidadedecarregamentodossitesno
rankingdebuscas.
Porúltimo,casovocêaindaestejapensandoque“ganhará”seusvisitantesapos-
tandotodassuas/f_ichasem design,entãovocêaindanãoentendeumuitacoisasobre
projetarpara mobile:(naverdade,aindatemmuitoaaprendersobrea web,emsi).
Éevidentequewebdesignéimprescindíveleumbomtrabalhonestecampodode-
senvolvimentowebsempregarantiuumamelhoranaexperiênciadousuárioeuso
dosite.Entretanto,nãoéalgoaserconsideradoprimariamente.
/one.oldstyle/one.oldstyle/four.oldstyle

## Página 123

CasadoCódigo Capítulo/six.oldstyle. TópicosdeWebMobile
Excetuando-seraríssimoscasos, web sitesnãosãofeitosdedesign;sãofeitosde
conteúdo!Porisso,apostena simplicidadedeseu designquandoprojetarparadis-
positivosmóveis.Ésério!
/six.oldstyle./four.oldstyle C/o.sc/m.sc/o.sc /a.sc/s.sc /p.sc/e.sc/s.sc/s.sc/o.sc/a.sc/s.sc /u.sc/s.sc/a.sc/m.sc /d.sc/i.sc/s.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/v.sc/o.sc/s.sc /m.sc/oacute.sc/v.sc/e.sc/i.sc/s.sc/question.sc
Per/f_isdeuso
Nãoéprecisoserumgrandeobservadorparasaberqueaspessoasutilizamdispo-
sitivosmóveisdemaneirasdiferentesdasqueusamdispositivosmaistradicionais.
Mas,comoestamostratandodeconhecimentostécnicosespecí/f_icosnestelivro,o
merofatodesaberqueestecomportamentoédiferentenãocontribuimuito...Épre-
cisomaisdetalhessobreisso,umconhecimentomaisaprofundadosobrecomoas
pessoasusamestesdispositivose,apartirdisso,projetareplanejarmelhoraexperi-
ência mobileparacadaumdosprojetoswebquevocêváfazerparte.
Saibaentãoqueexistemdeterminados per/f_isquandooassuntoécomporta-
mentoemdispositivosmóveis.Atravésdeumasériedeestudoseobserva ções,foram
encontradostrêsprincipaisper/f_isdeusonosdispositivosmóveis:
• Pesquisar(urgente,local). Pessoasqueprecisamdeumainforma ção,sejaela
qualform,demaneiraurgente(informa çãoestafrequentementerelacionada
àlocalizaçãofísicaatualdapessoa). Porexemplo:“Dopontoemqueestou
agora,ondepossoencontrarfarmáciaspróximas?”.
• Explorar/Divertir(entediado,local). Pessoasquetêmalgumtempooci-
oso/livreequeremaproveitarparaprocuraralgumaformadedistra çãooudi-
versão.Porexemplo:“Enquantoesperonesta/f_ila,vouprocurarinforma ções
sobreosúltimoslan çamentosdocinema”.
• Checkin/Status(repeti ção,micro-tarefas). Paraosmais“antenados”e/ou
queprecisam/f_icaratualizadoscasoinformaçõesquelhessãoimportantesse-
jamalteradas. Exemplo: “Precisosaberimediatamenteseostatusdomeu
pedidofoiatualizado”.
• Editar/Criar(mudan çaurgente,micro-tarefas). Quandoéprecisorealizar
umatarefaimportantequetenhaqueserfeitaomaisrapidamentepossível.
Porexemplo,ajustarumainforma çãoincorretaqueapessoatenhapublicado
emseublog.
/one.oldstyle/one.oldstyle/five.oldstyle

## Página 124

/six.oldstyle./four.oldstyle. Comoaspessoasusamdispositivosmóveis? CasadoCódigo
Então,atravésdestesper/f_is,épossívelconhecermelhoresabercomoaspessoas
fazemusodeseus devices. Conhecerestesper/f_isdeusopermitequeummelhor
planejamentodeseuprojetowebsejafeito,semprecomoobjetivodefocaremseu
público-alvoparaproporcionarumamelhorexperiênciadeusodositeousistema
web,independentementedodispositivonomomentodoacesso.
DoisexemplosinteressantessãoosdoBasecampeFlickrque,atravésdeuma
sériedeestudoseanálisesdeestatísticas,conseguirammapearquaisasa çõesmais
importantes,queaspessoasmaisfrequentementeusam.Apartirdisso,projetaram
aexperiência mobiledeseussitesparafocarquasequeunicamentenastarefasque
aspessoasprecisamequeremrealizar.
Decisãoacertadíssimapois,comovimosnosper/f_isdeusono mobile,opúblico
dosservi çosmostradoscomoexemploprecisam,quandoemacesso mobile,agili-
dadeefoconastarefasquepretendemexecutar!
Horaelugar
E,alémdestesprincipaisper/f_isdeusodedispositivosmóveis,tambémfoipos-
sívelavaliaroutrasinforma çõesimportantes,comohoraelugaremqueaspessoas
costumamusarseus smartphones(http://ow.ly/dnNuz):
• /eight.oldstyle/four.oldstyle/percent.oldstyleusamemcasa
• /eight.oldstyle/zero.oldstyle/percent.oldstyleusamemtemposvariadosdeinatividadeduranteodia
/one.oldstyle/one.oldstyle/six.oldstyle

## Página 125

CasadoCódigo Capítulo/six.oldstyle. TópicosdeWebMobile
• /seven.oldstyle/four.oldstyle/percent.oldstyleusamenquantoesperamem/f_ilasouporalgumcompromisso
• /six.oldstyle/nine.oldstyle/percent.oldstyleusamenquantoestãofazendocompras
• /six.oldstyle/four.oldstyle/percent.oldstyleusamnotrabalho
• /six.oldstyle/two.oldstyle/percent.oldstyleusamenquantoestãoassistindoTV
• /four.oldstyle/seven.oldstyle/percent.oldstyleusamenquantosedeslocam
Estatísticasinteressantíssimas,jáque,paragrandeparceladosdesenvolvedores
quetêmcontatocomwebdesignresponsivoe mobile /f_irstpelaprimeiravez,desen-
volverparadispositivosmóveisremeteasitesparaexecutivosdeempresas,investi-
dores,instituições/f_inanceiraseoutros.
Asestatísticassobrehoráriosdeusotambémsãodegrandeimportância.A/f_inal,
émaisdoqueevidenteofatodequeaspessoasusamseusdiferentesdevicesdemodo
diferenteeemhoráriosdiretentes.Tomandoporbaseumasériedeestatísticasfor-
necidaspelo Pocket(http://ow.ly/dnOT/zero.oldstyle)-serviçowebquepermitesalvarartigos
dointeresseparaquepossamserlidosposterioremente-emdispositivosApple,é
possívelterumaboano çãodoqueseestáquerendodizer.
/one.oldstyle/one.oldstyle/seven.oldstyle

## Página 126

/six.oldstyle./four.oldstyle. Comoaspessoasusamdispositivosmóveis? CasadoCódigo
No smartphone,porexemplo,temospicosem:
/one.oldstyle/one.oldstyle/eight.oldstyle

## Página 127

CasadoCódigo Capítulo/six.oldstyle. TópicosdeWebMobile
• /six.oldstyleam.Bemcedo,nahoradocafédamanhã.
• /nine.oldstyleam.Iníciodoexpedienteparamuitaspessoas.
• /five.oldstylepm-/six.oldstylepm.Fimdoexpediente;voltaparaacasa.
• /eight.oldstylepm-/one.oldstyle/zero.oldstylepm.HorárioNobre(nosofá);horadeirparaacama.
Jáosmaiorespicosdo tabletacontecememhoráriosconsideradosmaisdescon-
traídosesemmaiorescompromissoseafazeres. /eight.oldstylepm-/one.oldstyle/zero.oldstylepm,depoisdeumdiade
trabalhointeiro,provavelmentejásetomoubanho,ojantarjáfoiservidoeascrian-
çasestãodistraídas.Emsuma,éummomentomaistranquilo.
Combasenasinforma çõessobrehoraelugaremqueaspessoasmaisusamseus
dispositivosmóveis,épossívelfazerumplanejamentomaisacuradosobreaestraté-
giadoprodutoouservi ço onlinequesequeiracriarouaprimorar.Pensenoseguinte:
quaisseriamoshoráriosmaisindicadosparaatualiza çõesdegrá/f_icosenotíciaspara
umpúblico-alvodeinvestidores?Ou:qualseriamosmelhoreshoráriosparaatuali-
zaçõesnaqueleseusuperaplicativodefofocassobrecelebridades?
/six.oldstyle./five.oldstyle O/c.sc/o.sc/n.sc/t.sc/e.sc/uacute.sc/d.sc/o.sc /eacute.sc /o.sc /r.sc/e.sc/i.sc
Certamentevocêjádeveterescutadooulidoacélebrefrase“Oconteúdoéorei”-
mesmoantesdetercontatocomessahistóriatodade web design responsivoe mobile
/f_i r s t-que,detantorepetidaedivulgadanainternet,jánãoseconhecesuaautoria.
Denadaadiantariaositemaisbonitoeusáveldomundoseoconteúdofosseinútil,
vazioe/ouconfuso.
Quandooassuntoédesenvolvimentowebpensandoemdispositivosmóveis,é
preciso ter atençãoredobradaquantoaisso. Maisdoquenunca,agoraépreciso
darênfasetotalaoconteúdoetarefasmaiscomunsqueosfrequentadoresdosite
ousistemafazem/podemquererfazer. Quandooacessoémóvel,nãoháespa ço
para/f_irulas,elementosquenãoagreguemàexperiênciadeuso,menusinúteisou
qualqueroutrostiposdecomplicadores!
Naverdade,estamáximadeveserlevadaemcontanodesenvolvimentodequal-
quersite,mas,em mobile,estejarealmenteatentoaisso! Seusvisitantesdedispo-
sitivosmobilerealmentevãoquererveroqueseusitetemaoferecernosprimeiros
segundosdesuavisitae,casoencontremalgodiferentedoconteúdoqueestãopro-
curando/querendo,tenhacertezadequeaTaxadeRejei çãodeseusitevaiaumentar.
/one.oldstyle/one.oldstyle/nine.oldstyle

## Página 128

/six.oldstyle./six.oldstyle. Padrõesdenavegaçãomobile CasadoCódigo
/six.oldstyle./six.oldstyle P/a.sc/d.sc/r.sc/otilde.sc/e.sc/s.sc /d.sc/e.sc /n.sc/a.sc/v.sc/e.sc/g.sc/a.sc/ccedilla.sc/atilde.sc/o.sc /m.sc/o.sc/b.sc/i.sc/l.sc/e.sc
Tudobem,aestaalturavocêjádeveterinternalizadoaimportânciamaiordocon-
teúdoemseussites. Depoisdisso,éprecisogarantirqueoesquemadenavega-
çãotambémestejabemprojetado,prontoparatenderàsnecessidadesdosvisitantes
prontamente,demaneirae/f_iciente,agradávelenãodi/f_icultosa.
Apesardeowebdesignresponsivoseralgorelativamentenovo,algunspadrões
denavegaçãojáforamsistematizados. BradFrost(http://ow.ly/dy/five.oldstyle/six.oldstyleA)fezumótimo
trabalhoemorganizaramaioriadeles,elencandoprósecontrasdecadaabordagem.
Organizaçãoestaapresentadaaseguirdemaneiraresumida.
T o p n a v
U m a d a s s o l uçõesmaisfáceisdeimplementarparaanavega çãoésimplesmente
mantê-lanotopo.Porcausadesuafacilidadedeimplementa ção,essaabordagemé
encontradaemmuitos(talvezamaioria)dossitesresponsivos.
Prós
• Fácildeimplementar
• NãoéprecisoJavaScript
• Semnecessidadede“malabarismos”CSS
Contras
• Podeocasionarproblemasdealtura
/one.oldstyle/two.oldstyle/zero.oldstyle

## Página 129

CasadoCódigo Capítulo/six.oldstyle. TópicosdeWebMobile
• Nãoescalável
• Podeocasionarproblemascomoslinksmuitopróximos
Âncoranorodapé
Estasoluçãomantémalistadenavega çãonorodapédositeenquantoocabe ça-
lhocontémumlinkdeâncorasimplesapontandoparaanavega çãonorodapé.
Prós
• Fácildeimplementar
• NãoéprecisoJavaScript
• Semnecessidadede“malabarismos”CSS
• Únicobotãonocabeçalho
Contras
• Anavegaçãoporâncorapodedesorientaralgumaspessoas
• Algunspodemconsiderarasolu ção“nãoelegante”
/one.oldstyle/two.oldstyle/one.oldstyle

## Página 130

/six.oldstyle./six.oldstyle. Padrõesdenavegaçãomobile CasadoCódigo
Menu de seleção
Umamaneiradelidarcommenusdenavega çãoétransformá-losnumalistade
linksemummenudesele çãoparatelasmenores.Issoevitaosproblemasdaabor-
dagemTopnaveéumamaneirainteligentedeeconomizarespa çoemtela.
Prós
•Nãoocupaespa çoemtela
• Mantémtodaainteraçãonocabe çalho
• Facilmentereconhecível
Contras
• Difícildeestilizarelementos select
• Potencialmenteconfuso
• Submenuspodemparecer“estranhos”
• NecessitadeJavaScript
/one.oldstyle/two.oldstyle/two.oldstyle

## Página 131

CasadoCódigo Capítulo/six.oldstyle. TópicosdeWebMobile
Alternância
AabordagemAlternânciaésemelhanteàabordagemÂncoranorodapé,mas,ao
invésdesaltarparabaixoparaumaâncoranaparteinferiordapágina,omenuse
abrenoprópriolocal.Éumaabordagemdeboaaparênciaeérelativamentefácilde
implementar.
Prós
• Mantémainteraçãonumsólocal
• Elegante
• Facilmenteescalável
Contras
• Performance(aorealizaraanima çãodoslide)
• PrecisadeJavaScript
/one.oldstyle/two.oldstyle/three.oldstyle

## Página 132

/six.oldstyle./six.oldstyle. Padrõesdenavegaçãomobile CasadoCódigo
Slideàesquerda
Omenudenavega çãoéacessadoporumíconedomenuque,quandoacessado,
exibeasop çõesdomenuatravésdeumaanima çãode slidequecomeçaàesquerda,
movendooconteúdoprincipalparaadireita.
Prós
•Nãoocupaespa çoemtela
• Mantémainteraçãonumsólocal
• Boaaparência
Contras
• Técnicarelativamenteavançada
• Nãoescalamuitobem
• Potencialmenteconfuso
/one.oldstyle/two.oldstyle/four.oldstyle

## Página 133

CasadoCódigo Capítulo/six.oldstyle. TópicosdeWebMobile
Somentenorodapé
AnavegaçãoSomentenorodapéésemelhanteàabordagemTopnav,sóquesem
aâncoranocabe çalho.
Prós
•Nãoocupaespa çonocabe çalho
Contras
• Difícildeencontrareacessaromenu(deve-sepercorrertodooconteúdo)
/one.oldstyle/two.oldstyle/five.oldstyle

## Página 134

/six.oldstyle./six.oldstyle. Padrõesdenavegaçãomobile CasadoCódigo
NavegaçãoPullDown
Revelaomenudenavega çãonummovimentodeslidequeempurraorestante
doconteúdoparabaixo.
Prós
• Sexy!;-)
• Omovimentodeslide top-downjáéumaconven çãoem smartphones
Contras
• Técnicarelativamenteavançada
• Precisadeinstruçãodeuso(geralmente,um label)
/one.oldstyle/two.oldstyle/six.oldstyle

## Página 135

CasadoCódigo Capítulo/six.oldstyle. TópicosdeWebMobile
Consideraçõessobrepadrõesdenavega çãomobile
Foramapresentadasalgumasdasabordagensmaiscomunsquandofalamosem
sistemasdenavega çãoparasitesquesevalemde webdesignresponsivo . Certa-
mente,nãoforamapresentadastodase,comooassuntoénovo,sugestõesdemelho-
riasenovasabordagensserãodesenvolvidas,propostasediscutidas.Oimportante
étentarchegaromaispróximopossíveldoobjetivodealiarnavega çãoacessível,es-
paçoemtelaefacilidadedeuso(oquenãoéumatarefasimples).
Casoestejainteressadoemcomopodeimplementarcadaumadessasaborda-
gens,oartigo Responsive Menus: Enhancing Navigation On Mobile Websites (http:
//ow.ly/dyb/four.oldstylex)éomaisindicado.
/six.oldstyle./seven.oldstyle /one.oldstyle/zero.oldstyle/p.sc/r.sc/i.sc/n.sc/c.sc/iacute.sc/p.sc/i.sc/o.sc/s.sc /d.sc/e.sc /d.sc/e.sc/s.sc/i.sc/g.sc/n.sc /p.sc/a.sc/r.sc/a.sc /i.sc/n.sc/t.sc/e.sc/r.sc/f.sc/a.sc/c.sc/e.sc/s.sc /m.sc/o.sc/b.sc/i.sc/l.sc/e.sc
Oconsultorde mobileJonathanStark(eestenome,porsisó,jádizmuitosobresua
capacidade)elaborou /one.oldstyle/zero.oldstyle princípios de design de interface móvel(http://ow.ly/dJnk/eight.oldstyle)
quesãobastanteconhecidos.Vamospassarporelesdeformasucinta.
/one.oldstyle.Mentalidademóvel
Devidoàsdiferen çasentre mobilee desktop,éimperativoquevocêfa çauma
imersãonamentalidade mobileantesdecome çar.
Sejafocado. Maisnãoémelhor.Editesuas f e at u re simpiedosamente.Vocêvai
terquedeixaralgumascoisasparafora.
Sejaúnico. Saibaoquefazcomqueseuaplicativosejadiferenteeampli/f_ique
isso.Hámuitospeixesnomardeaplicativosmóveis.Senãohánadadeespecialem
suaaplicação,porquealguémiriaquerê-la?
Sejaencantador. Dispositivosmóveissãointensamentepessoais.Elessãonos-
soscompanheirosconstantes.Aplicativosquesãoamigáveis,con/f_iáveisedivertidos
sãoumadelíciadeusareaspessoasvãosetornarmuitoligadasàexperiência.
Sejaatencioso. Desenvolvedoresde mobilemuitasvezesseconcentramnoque
seriadivertidodesenvolver,noseuprópriomodelomentaldoaplicativoouseusob-
jetivospessoais.Estessãobonslugaresparacome çar,masvocêtemquesecolocar
nolugardeseususuáriossevocêesperacriarexperiênciasenvolventes.
/two.oldstyle.Contextomóvel
Aimagemdopro/f_issionalocupado,correndopeloaeroportocomumsacona
/one.oldstyle/two.oldstyle/seven.oldstyle

## Página 136

/six.oldstyle./seven.oldstyle. /one.oldstyle/zero.oldstyleprincípiosdedesignparainterfacesmobileCasadoCódigo
mãoesmartphonesnooutroéoquemuitaspessoastêmemmentequandosepensa
sobreocontextomóvel.Écertamenteumcontexto,masnãoéoúnico.Paracome-
çaracolocarmo-nosnapeledenossosusuários,temosdeconsiderartrêsgrandes
contextosmóveis:Entediado,OcupadoePerdido.
Entediado.Hámuitaspessoasusandoseus smartphonesnosofádecasa.Neste
contexto,asexperiênciasimersivasedeliciosas,voltadasparaumasessãodemaior
tempodeuso,sãoumgrandepossibilidade. Aindaassim,interrup çõessãoalta-
menteprováveis,então,tenhacertezadequeseuaplicativopodecontinuardeonde
ousuárioparou.Exemplos:Facebook,Twitter,AngryBirds,navegadorweb.
Ocupado.Esteéocenário“atravessandooaeroporto”.Acapacidadederealizar
micro-tarefasdeformarápidaecon/f_iávelcomumamãoemumambienteagitadoé
crítica.Lembre-sedequeousuárioteráa“visãodetúnel”nestecontexto,entãoobje-
tivosclarosedesignarrojadosãoimportantes.Exemplos:TripIt,e-mail,calendário,
internetbanking.
Perdido.Osusuáriosqueestãonotrânsito,emambientesdesconhecidosouem
ambientesfamiliares,masinteressadosemalgoaoredor,seenquadramnessacate-
goria.Nestecontexto,aconectividadeeabateriasãograndespreocupa ções,então
vocêdeveofereceralgumníveldesuporteoﬄineesereconômicocomautiliza ção
degeolocalizaçãoeoutrosgargalosdebateria.Exemplos:Mapas,Yelp,Foursquare.
Paramaioresinforma ções,dadoseestatísticasaesserespeito,relembresobreos
per/f_isdeusodedispositivosmóveis.
/three.oldstyle.Orientaçõesgerais
Diferentesaplicaçõesexigemdiferentesabordagens,designetécnicas.Ditoisto,
anaturezainerentedeumdispositivo touchscreendebolsosugereváriasdiretrizes
globais,ouseja,ascoisasquesempreimportam.
Responsividade.Capacidadederespostaéabsolutamentecrítico.Seousuário
fazalgo,suaaplica çãodevereconheceraintera çãoinstantaneamente.Note-seque
acapacidadederespostaevelocidadenãosãoamesmacoisa. Tudobemsecertas
operaçõeslevaremtempo. Apenascerti/f_ique-sequeousuáriosaibaqueascoisas
estãofuncionando/acontecendo.
Polidez.Polidezéextremamentevaliosa. Emvirtudedanaturezado“compa-
nheiroconstante”danossarela çãocomos smartphones,prestarmuitaaten çãonos
pequenosdetalhes,issoseránotadoeapreciado.
Dedos.Comoadventodasinterfaces touchscreen,todomundoestásemprefa-
landode“toquenisso”e“toquenaquilo”.Narealidade,éparaopolegarquepreci-
/one.oldstyle/two.oldstyle/eight.oldstyle

## Página 137

CasadoCódigo Capítulo/six.oldstyle. TópicosdeWebMobile
samosprojetar.Amenosqueousuárioestejainteragindocomseu smartphonecom
asduasmãos,équaseimpossívelaintera çãocomoutrodedoqualquere,mesmo
quandosemexecomasduasmãos,omaisprovávelédigitarcomosdoispolegares.
Polegaressãoopadrão.
Alvos.Devidoaumasériedeestudossobreotamanhoeformadopolegar,pa-
recequeonúmeromágicoparaoselementosdeUIamigáveisaopolegaréde/four.oldstyle/four.oldstyle
pixels. Existemmuitasexceções,masestaéumaregrageral. Vocêtambémdeve
estarconscientesobreondeondecolocarum targetsemrelaçãoaosoutros(casoha-
jam). Porexemplo,colocarobotão“Apagar”( backspace)diretamenteaoladodo
botãodeenvioemumaplicativoSMSseriaumamáidéia.
Conteúdo.Arevoluçãodasinterfacesdetoqueéqueelasnospermiteminteragir
diretamentecomnossoconteúdo.Issoremoveabstra ções(como mousee trackpad)
eestámaisdeacordocomaformacomonossoscérebrosfuncionam.Umacrian ça
de/two.oldstyleanosconsegueusarumtabletsemdi/f_iculdade,masum laptopjáéummisté-
rio.Aproveiteopoderintuitivodainterfacedetoque,minimizando“di/f_icultadores”
(botões,abas,caixasdesele ção,sliderseassimpordiante)semprequepossívele
colocandoseuconteúdosempreemfoco.
Controles.Quandoéprecisoadicionarcontroles,tentecolocá-losnaparteinfe-
riordatela(emoutraspalavras,soboconteúdo).Penseemumamáquinadesomar,
umabalançadebanheiroouatémesmoumcomputador:oscontrolesestãoabaixo
dovisor.Senãofosse,nãoseríamoscapazesdeveroqueestavaacontecendocomo
conteúdoenquantosedáouso.
Rolagem.Evitearolagem.Terumatelasemrolagemcausaumamelhor“sen-
sação”doqueumatelacomrolagem.Claro,certastelasdevemserprojetadaspara
rolar,masébomevitá-lassemprequepossível.
/four.oldstyle.Modelosdenavegação
Háumaabundânciademodelosdenavega çãoinovadoresparaaplicativosmó-
veis,mas,sevocêestivertendendoausarumdosmodeloscomunsdenavega ção,
certi/f_ique-sedeescolheroquefazmaissentidoemsuaaplica ção.
Maisaesserespeito,leianovamentesobrepadrõesdenavega ção mobilenaseção
.
/five.oldstyle.Inputsdousuário
Digitaçãoécomplicadoatémesmonosmelhoresdispositivos,então,vocêdeve
/one.oldstyle/two.oldstyle/nine.oldstyle

## Página 138

/six.oldstyle./seven.oldstyle. /one.oldstyle/zero.oldstyleprincípiosdedesignparainterfacesmobileCasadoCódigo
fazeroquepuderparatornaressetipointera çãomaisfácilparaosusuários. Por
exemplo:
• Hácercadeumadúziadevaria çõesdetecladoemsmartphonespopulares
(texto,número,e-mail,URLeassimpordiante).Considerecadaumdosseus
camposdeentradaecerti/f_ique-sedeexibirotecladoqueserámaisútilparaa
entradadedadosqueestásendofeita.
• Corretoresortográ/f_icospodemsertãodivertidos,quantofrustrantes. Con-
siderarcadaumdosseuscamposdeentradaedecidirquaiscamposdevem
estarativos(comoauto-corre ção,auto-capitalizaçãoe autocomplete).
• Seseuaplicativoprecisadeummontededigita ção,vocêdevegarantirqueo
tecladonosentidohorizontal( landscape)estejapreparadoparadedos“gordi-
nhos”.
/six.oldstyle.Gestos
Umdosaspectosmaisemblemáticosdeinterfacesdetoquemodernaséqueelas
suportamgestosparaintera ções.Gestossãorealmentemuitolegaiseúteis,mashá
váriascoisasquevocêprecisamanteremconsidera ção:
Invisibilidade. Gestossãoinvisíveis,porissosuadescobertaéumproblema.
Vocêtemquedecidircomorevelarsuaexistênciaparaousuário. Umadasabor-
dagensmaisinteligentesécomonadosiPadspromocionaisexpostosemlojasde
varejodaApple.Quandoumapáginaécarregadaprimeiro,asáreasderolagemfa-
zerumrápido“ scrollreverso”atésuaposi çãopadrão.Istoimediatamenteconvidaa
umgestosúbitodousuáriosemterqueindicar,explicitamente,quaissãoasáreasde
rolagem.
Duasmãos. Gestos multi-touchrequeremousodasduasmãos.Issoéparticu-
larmenteevidenteemaplicativosdemapasdoiOSqueusamogestode“abrirpin ça ”
paradiminuirozoom. Mas,se,porexemplo,vocêestáviajandoemumacidade
estrangeiracomumcafénumamãoeotelefonenaoutra,essaéumalimita çãoirri-
tante.OAndroidtemumaabordagemmelhorsobreestaquestão,incluindobotões
de“zoomin”e“zoomout”próximosaomapa.
Bomdeter. Namaioriadoscasos,gestospodemserconsideradoscomo“bomte
ter”,masnãocríticos.Écomoalgunstiposdeatalhosdeteclado:usuáriosavan çados
vãoamá-los,masamaioriadaspessoassequersabemqueestãolá.
/one.oldstyle/three.oldstyle/zero.oldstyle

## Página 139

CasadoCódigo Capítulo/six.oldstyle. TópicosdeWebMobile
Semsubstituição.Aindanãoexisteumpadrãocomumparagestos,porissoé
muitocedoparaamaioriadosaplicativosdescartaremcontrolesvisíveisquepodem
serusadoscomumúnicodedo.
/seven.oldstyle.Orientação
Aorienta ção portraité,delonge,amaispopular. Porisso,otimizeprimeiro
paraestecaso.Seseuaplicativoprecisademuitadigita ção,vocêdevedarsuportea
orientaçãolandscapeparaaspessoaspoderemacessarotecladomaior.
Quandoaorienta çãomudainesperadamente,issoédesorientador.Sevocêacha
queseuaplicativoseráusadoporlongosperíodosdetempo(porexemplo,oKindle
Reader),considereaadi çãodeumatravadeorienta çãodiretamentenoaplicativo.
/eight.oldstyle.Comunicações
Forneçafeedback. Forneça feedbackimediatoparacadaintera ção.Sevocênão
/f_izerisso,ousuárionãovaisaberseoaplicativotravououseerraramoalvo/intera ção
quetentaraminteragir.O feedbackpodesertátilouvisual.Seousuáriotiversoli-
citadoumaa çãoquevailevarumlongotempo,apresenteumindicadorde loading
paraquesaibamqueasolicita çãofoienviadaeestásendoprocessada.
Alertasmodais. Alertasmodaissãoextremamenteagressivoeinvasivosparao
/f_luxodousuário,assim,vocêsódeveusá-losquandoalgoestiverseriamenteerrado.
Mesmoassim,tentaratenuaraintensidade,mantendoalinguagemreconfortantee
amigável.Lembre-sedenãousaralertasmodaisparamensagensdotipo“Parasua
informação”.
Con/f_irmações.Quandovocêtemquepediraumusuárioparacon/f_irmaruma
ação,éaceitávelexibirumdiálogodecon/f_irmaçãomodal(como“Temcertezadeque
desejaexcluiresteprojeto?”). Ascon/f_irmaçõessãomenosinvasivasdoquealertas
porqueelasaparecememrespostaaumaa çãodousuárioe,portanto,numcontexto
atéesperado. Lembre-sedefazercomqueaobotãopadrãosejaaescolha“mais
segura”dacaixadediálogoparaajudaraevitarinadvertidasa çõesdestrutivas.
/nine.oldstyle.Inicializaçãodoaplicativo
Quandoumusuáriovoltaparaseuaplicativodepoisdejáoterusadoantes,você
deveretomarasopera çõesexatamenteondeousuárioparou.Issodaráa“ilusãode
velocidade”econtribueparaumasensa çãogeraldecapacidadederesposta.
Sepossível,ateladeinicializa çãoexibidaquandooaplicativoéiniciado(ouaces-
/one.oldstyle/three.oldstyle/one.oldstyle

## Página 140

/six.oldstyle./seven.oldstyle. /one.oldstyle/zero.oldstyleprincípiosdedesignparainterfacesmobileCasadoCódigo
sado)deveserumateladesprovidadeconteúdo,apresentandosomenteologoou
algumaimagem.Qualquercoisaquepare çainterativa(comobotões,links,ícones,
conteúdo)vaicriarfrustra çãoaoconvidarparaumintera ção“falha”.
Resistafortementeàtenta çãodecolocarelementos/materiaisde brandingnatela
de launch.Elesfazemousuáriosesentircomoseestivessevendoumanúncioeeles
se“ressentem”comisso,tendendoairembora.
/one.oldstyle/zero.oldstyle.Primeirasimpressões
Seuícone.Seuíconetemdecompetirporaten çãoemummardeoutrosícones.
Sendoesseocaso,pensenissomaiscomoumcartãodevisitasdoqueumaobrade
arte.Sejaliteral:mostreoqueseuaplicativofaz.Useumasilhuetaforteeoptepor
ummínimodetextos. Umíconepolidosugereumaplicativopolido,entãovalea
penadedicartemposérioedinheiroparafazê-lodireito.
Primeirolançamento.Oprimeirolan çamentoéumasitua çãoparaencantarou
decepcionar.Seumnovousuário/f_icaconfusooufrustradoaotentarsefamiliarizar
comseuaplicativo,elesvaiabandoná-loomaisrápidoqueconseguir.Seoaplicativo
fornecefuncionalidadescomplexas,vocêpodequererincluirum“DicaseTruques”
oualgumastelascomorienta çõesgerais.Notequeestasdicasnãoservemparasubs-
tituirumbomprojeto. Sevocêseencontrarcriandoummontedetextodeajuda,
issoéumforteindicativodequeaUIdesuaaplica çãoprecisadeumretrabalho.
/one.oldstyle/three.oldstyle/two.oldstyle

## Página 141

C/a.sc/p.sc/iacute.sc/t.sc/u.sc/l.sc/o.sc/seven.oldstyle
Continuandoseusestudos
Eeisquevocêchegouaoúltimocapítulo,sãoesalvo!Paraajudarnosseusestudos,
apresentamosaquiumacompila çãoderecursossobre web designresponsivo.
/seven.oldstyle . /one.oldstyle A/r.sc/t.sc/i.sc/g.sc/o.sc/s.sc/T/u.sc/t.sc/o.sc/r.sc/i.sc/a.sc/i.sc/s.sc
Lerartigosetutoriaiséabaseparasemanteratualizadosobreoqueaconteceno
mundodaresponsividade.Con/f_iguraalgumasboasreferênciasecontinueosestu-
dos!
ConsiderationsforMobileDesign:Behavior
Oartigo“ConsiderationsforMobileDesign:Behavior”(http://ow.ly/e/zero.oldstyler/nine.oldstyleU)traz
informaçõesdecaráterimportantíssimosobreocomportamentonoambiente mo-
b i l e,diferençasentreformasdeintera ção,UIs mobileemais.Leia!

## Página 142

/seven.oldstyle./one.oldstyle. Artigos/Tutoriais CasadoCódigo
ConvertaMenutoaDropdownforSmallScreens
Nospadrõesdenavega ção mobile/six.oldstyle./seven.oldstyle,vocêviuqueumadastécnicasétransfor-
maromenunumalistade linksemummenudesele çãoparatelasmenores. No
“ConvertaMenutoaDropdownforSmallScreens”(http://ow.ly/dUNa/six.oldstyle),vocêvai
saber,passoapasso,comorealizaresteefeito.
DesignProcessIn /T_heResponsiveAge
Oartigo“DesignProcessIn /T_heResponsiveAge”(http://ow.ly/e/zero.oldstylekZV)aborda
pontosmuitointeressantessobreoprocessode designpara sitescom web designres-
ponsivo.Valeapenadarumaolhada,poisoplanejamentodeumprojetoéumade
suasprincipaiseimprescindíveisetapas!
Hidingandrevealingportionsofimages
Em“Hidingandrevealingportionsofimages”(http://ow.ly/e/zero.oldstyleprm)vocêvai
aprendertécnicasmaisavan çadasdeapresenta çãodeimagensem web designsres-
ponsivosevaiaprendercomoocultardeterminadaspartesdeimagensquandofor
maisadequado.
Optimizingyouremailformobiledeviceswiththe@mediaquery
Notutorial“Optimizingyouremailformobiledeviceswiththe@mediaquery”
(http://ow.ly/dUNmd), vocêvaiaprender comotornarseus e-mailspara mobile
usando Media Queries. A/f_inal,éimportantegarantirmensagense newslettersres-
ponsivosparaumaexperiência mobilecompleta.
ResponsiveDataTables
Notutorial“ResponsiveDataTables”(http://ow.ly/dUN/five.oldstylef),vocêvaiconhecer
algumasideiasexcelentessobrecomotratartabelasedadostabularesemprojetos
com web designresponsivo.
ResponsiveWork/f_low
Em“ResponsiveWork/f_low”(http://ow.ly/e/zero.oldstylexEK),vocêvaiencontraraproposta
deumametodologiasobrecomoplanejar,desenvolverelan çarprojetosresponsivos.
Éumaleiturainteressantequepodeserabasefundamentaldeseusprojetosapartir
deagora!
/one.oldstyle/three.oldstyle/four.oldstyle

## Página 143

CasadoCódigo Capítulo/seven.oldstyle. Continuandoseusestudos
/T_heMobilePlaybook
/T_heMobilePlaybook,UmGuiaparaExecutivosOcupadosVenceremnoMer-
cadoMobile(http://ow.ly/e/zero.oldstyleAK/three.oldstyle),daGoogle,éumlivrointerativocominformações
preciosassobreomundodedispositivosmóveis,marketing mobile,considerações,
dicaseestatísticassobrecomovencernomercadomóvel.
/seven.oldstyle . /two.oldstyle B/o.sc/o.sc/k.sc/m.sc/a.sc/r.sc/k.sc/l.sc/e.sc/t.sc/s.sc
U mbookmarkletéumtrechoemJavaScriptqueéarmazenadocomoumaURLpo-
demsersalvosnosfavoritosdequalquer browser. Éinteressantequevocêtenha
algunstambémparaodesenvolvimentocom web designresponsivo.
MediaQueryBookmarklet
AoativaroMediaQueryBookmarklet(http://ow.ly/dUO/seven.oldstylec),eleanalisaosar-
quivosCSSincluídosdapáginaatualecriaumasériededeclara çõesde media quer y
quesãomostradasnatela,emtemporeal,enquantovocêredimensionaajanelado
navegador.
ResponsiveDesignbookmarklet
ResponsiveDesignBookmarklet(http://ow.ly/e/zero.oldstylekvR)permitequevocêcrieum
bookmarletemtemporealparatestescom web designresponsivo.De/f_inaostama-
nhosquegostariaderealizarseustestesesalveseu bookmarletpersonalizadopara
usofuturo.
/seven.oldstyle . /three.oldstyle E/s.sc/b.sc/o.sc/ccedilla.sc/o.sc /e.sc /p.sc/l.sc/a.sc/n.sc/e.sc/j.sc/a.sc/m.sc/e.sc/n.sc/t.sc/o.sc
Jáque,apartirdeagora,vocêsótrabalhacomwebdesignresponsivoeMobileFirst,
seusesboçostambémdevemsofrerumaaltera çãoparaacompanharestanovafase.
Simplesmenteescolhaumdosmostradosecomeceadesenhar!
ASimpleDeviceDiagramforResponsiveDesignPlanning
ASimpleDeviceDiagramforResponsiveDesignPlanning(http://ow.ly/e/zero.oldstyleg/zero.oldstylew),
comosugereopróprionome,éumdiagramasimplesparaserusadonoplaneja-
mentode web designresponsivo,mostrandouma“régua”comasprincipaisresolu-
çõesdos devicesmaisusadosnomundo.
/one.oldstyle/three.oldstyle/five.oldstyle

## Página 144

/seven.oldstyle./four.oldstyle. Ferramentas CasadoCódigo
ResponsiveDesignSketchbook
Quetalumcadernoquadriculadoespecialmentefeitoparaplanejamentode web
designsresponsivos? Estaé,justamente,apropostadoResponsiveDesignSketch-
book(http://ow.ly/dUMH/nine.oldstyle).Porumpreçoacessível,épossíveladquirirestecaderno
espiralcom/five.oldstyle/zero.oldstylepáginasparaoseuplanejamento.
ResponsiveWebDesignSketchSheets
ResponsiveWebDesignSketchSheets(http://ow.ly/dPHlf)éumconjuntode
modelosdemarcados,indicandováriostamanhosdetela,paraoplanejamentoees-
boçodastelasemsitesresponsivosserembemrápidos.
UXSketchingAndWireframingTemplatesForMobileProjects
UXSketchingAndWireframingTemplatesForMobileProjects(http://ow.ly/
dSBK/zero.oldstyle)éumconjuntode/two.oldstyle/eight.oldstylefolhasparaesboçose wireframesemPDFparadiversas
plataformas,dentreasquaisAndroid,BlackBerry,iOS(iPadandiPhone),Meego,
Symbian,webOSeWindowsPhone/seven.oldstyle.
/seven.oldstyle . /four.oldstyle F/e.sc/r.sc/r.sc/a.sc/m.sc/e.sc/n.sc/t.sc/a.sc/s.sc
Agoraquevocêjásabebastantecoisasobre web design responsivo,éimportante
acrescentarnoseu k i tpessoalalgumasferramentasparaajudarcomodesenvolvi-
mentoresponsivo.
FluidGrids
Jáforammostradosvários fr a mewo r ksquepossuem grids/f_luídosparadesenvol-
vimentode sitesresponsivos.Mas,esevocêquiserteroseupróprio grid?ComFluid
Grids(http://ow.ly/dUOhD)essatarefavaisermaisfácildoquevocêimagina:so-
menteespeci/f_iquequantascolunas,otamanhodecadaumaeoespa çoentreelase
pronto,façao downloaddeseugridpersonalizado!
[PXtoEM]
PXtoEM(http://ow.ly/e/zero.oldstylej/nine.oldstyleU)éumatabelainterativadeconversãodepixels
paraoutrasunidadescomoEMs,porcentagemePontos.Possuialgunsvalorespré-
de/f_inidosepermiteainserçãodevalores-baseparaaconversão.
/one.oldstyle/three.oldstyle/six.oldstyle

## Página 145

CasadoCódigo Capítulo/seven.oldstyle. Continuandoseusestudos
resizeMyBrowser
NoresizeMyBrowser(http://ow.ly/dUNNr),vocêencontrabotõescomasreso-
luçõesmaiscomuns(dos devicesmaispopulares)que,aoseremclicados,abremuma
novajanelacomaqueletamanhoescolhido.
/T_heResponsiveCalculator
Obviamente,vocêselembradafórmulamágicado web design responsivo/three.oldstyle./two.oldstyle.
Mas,casotenhaalgunsproblemas/di/f_iculdadescomcálculos, /T_heResponsiveCal-
culator(http://ow.ly/e/zero.oldstyleeDr)éumaferramentaimprescindívelparavocê,jáquese
tratadeumaespéciedecalculadoraespecí/f_icapara web designresponsivo,ajudando
aconverter p i x el sparaporcentagens.
/seven.oldstyle . /five.oldstyle I/n.sc/s.sc/p.sc/i.sc/r.sc/a.sc/ccedilla.sc/atilde.sc/o.sc
Agoraquevocêjásabebastantesobre web designresponsivo,édeinteresseober-
varalgunsprojetoseexemplosde siteserecursosjádesenvolvidose/oubaseadosna
responsividade.
MediaQueries
Umadasprimeirasemaisconhecidasgaleriasde sitesresponsivos,noMedia
Queries(http://ow.ly/e/zero.oldstyleyev)épossívelcompanharprojetosresponsivosdeexcelente
qualidade.
MobileUIPatterns
Sevocêestácome çandoagora(ou,mesmo,jáestádentro)domundodode-
senvolvimento mobile,vaigostarbastantedeconheceroMobileUIPatterns(http:
//ow.ly/e/zero.oldstyleyyt),queapresentasoluçõesdeUIpara mobileseparadasporcategorias.
/seven.oldstyle . /six.oldstyle J/a.sc /v.sc /a.scS/c.sc/r.sc/i.sc/p.sc/t.sc /p.sc/u.sc/r.sc/o.sc
Emalgunscasos,solu çõesemJavaScriptpurotambémsãoumaótimapedidapara
asoluçãodeproblemascom web designresponsivo.
/one.oldstyle/three.oldstyle/seven.oldstyle

## Página 146

/seven.oldstyle./seven.oldstyle. PluginsjQuery CasadoCódigo
Adapt.js
Adapt.js (http://ow.ly/dUOSy) é um JavaScript muito leve (menos de /one.oldstyleKB
quandomini/f_icado)quedeterminaqualarquivoCSSdevesercarregarantesdeo
navegadorprocessarumapágina.Seonavegadoréredimensionado,Adapt.jssim-
plesmenteveri/f_icaanovalarguraeprovêapenasoCSSnecessário,quandonecessá-
rio.
foresight.js
foresight.js(http://ow.ly/e/zero.oldstylerEY)provêainformaçãoquedizseodispositivoque
estáfazendooacessoécapazdevisualizarimagensemaltaresolu ção(comooiPad
/three.oldstyleªgeração,porexemplo)antesdaimagemsersolicitadonoservidor.
Respond
Respond(http://ow.ly/dPGhQ)éum poly/f_illquefazcomqueIE/six.oldstyle-/eight.oldstylereconheçam
min-widthe max-widthparaousode Media Queries.
RetinaImages
RetinaImages(http://ow.ly/e/zero.oldstyleduN)automaticamenteserveimagensemaltare-
soluçãoparadispositivosquepossuem retina display.Seuusoébastantesimplese,
paraos sitesquequeremsevalerdesteextra,realmentevaleapena!
/seven.oldstyle . /seven.oldstyle P/l.sc/u.sc/g.sc/i.sc/n.sc/s.sc /j.scQ/u.sc/e.sc/r.sc/y.sc
Épossível,sim,fazerbons sitesusandosomenteHTMLeCSS(pelomenosnonível
atualdestastecnologias),masfatoéque,paraproporcionarexperiênciasrealmente
marcanteseenvolventes,umtoquede JavaScriptsefaznecessário.Como,nãopor
acaso,jQueryéabibliotecaJSmaisusadanomundo,aívaiumalistade plugins
relacionadosa web designresponsivo.
Camera
Camera (http://ow.ly/dPCg/six.oldstyle) permite fazerslideshowsresponsivos incríveis.
Contacom loading,miniaturas,op ções, callbackse,seguindooestilojQuerydeser,
ésimplíssimodeusar.
/one.oldstyle/three.oldstyle/eight.oldstyle

## Página 147

CasadoCódigo Capítulo/seven.oldstyle. Continuandoseusestudos
FitText
FitText(http://ow.ly/dPB/four.oldstyleV)tornaapropriedadeCSSfont-size/f_lexível.Uti-
lizeeste pluginemseuprojetoparaconseguirtítulosescaláveis,dalarguratotaldo
elemento-pai.
Flexslider
Flexslider(http://ow.ly/dU/three.oldstyleY/zero.oldstyle)éoutroexcelentepluginpara slideshowsrespon-
sivos. Funcionacommarca çãosimples,dásuporteaváriosefeitosdeanima ção,
slidersmúltiplos,API,callbacksetudoomaisqueum plugincompletopossui.
Isotope
Isotope(http://ow.ly/e/zero.oldstylebNM)éumexcelentepluginquealémdereorganizarele-
mentosnatela(comumefeitobeminteressante)emtemporeal,conformeotama-
nhodajaneladonavegador,permiteusarop çõesde/f_iltragemparaoselementosque
estãosendoapresentados.
scrolldeck
scrolldeck(http://ow.ly/dPEjn)permitefazer siteseapresentaçõescom“ decks
rolantes”,ouseja,vocêclicaemum linkeapáginarolaatéopontoespeci/f_icado.
Supersized!
Supersized! (http://ow.ly/dPEHZ)permiteslideshowdeimagensemtelacheia,
sejaqualforaresolu çãousadaporquemacessaosite.
TinyNav.js
Nospadrõesdenavega ção mobile/six.oldstyle./seven.oldstylevocêviuqueumadastécnicasétransformar
omenunumalistade linksemummenudesele çãoparatelasmenores.TinyNav.js
(http://ow.ly/e/zero.oldstylec/one.oldstyleI)serve,justamente,paraisso!
Wookmark
Wookmark(http://ow.ly/e/zero.oldstylecfE)detectaotamanhodajaneladonavegadorque
estárealizandooacessoe,apartirdisso,rearranjaoselementosdapáginaemcolu-
nas.Naprática,éumaalternativamais“enxuta”ao pluginIsotope.
/one.oldstyle/three.oldstyle/nine.oldstyle

## Página 148

/seven.oldstyle./eight.oldstyle. Testesderesponsividade CasadoCódigo
/seven.oldstyle . /eight.oldstyle T/e.sc/s.sc/t.sc/e.sc/s.sc /d.sc/e.sc /r.sc/e.sc/s.sc/p.sc/o.sc/n.sc/s.sc/i.sc/v.sc/i.sc/d.sc/a.sc/d.sc/e.sc
Existemdiversasferramentaspela webàforaqueauxiliamafazerostestesdeseus
web designsresponsivos,tornandoatarefadeveri/f_icarcomoascoisasestão/f_icando
emdiferentesresolu çõesdemaneiramaisprática.Con/f_iraalgumas.
DemonstratingResponsiveDesign
DemonstratingResponsiveDesign(http://ow.ly/dULxj)permitevisualizarcomo
um site/f_icavistoemumcelularem landscapee portrait, tablettambémcomas/two.oldstyle
orientaçõese desktop,alterando,deformainterativa,asvisualiza çõesparavisualizar.
ResponsivePlay
ResponsivePlay(http://ow.ly/dSD/one.oldstyleb)éumaferramentabrasuca,desenvolvida
porSérgioLopes.Elaajudabastanteatarefadechecarodesenvolvimentocom web
designresponsivoaopermitirvisualizarumaanima çãodeum viewportseesten-
dendoconformeumafaixadelarguraetempode/f_inidosporquemusaaferramenta.
Beminteressante!
ResponsiveWebDesignTestingTool
ComResponsiveWebDesignTestingTool(http://ow.ly/dUNFe),épossívelvi-
sualizarqualquersitenaslargurasde/two.oldstyle/four.oldstyle/zero.oldstyle,/three.oldstyle/two.oldstyle/zero.oldstyle,/four.oldstyle/eight.oldstyle/zero.oldstyle,/seven.oldstyle/six.oldstyle/eight.oldstyle,/one.oldstyle/zero.oldstyle/two.oldstyle/four.oldstylep i x el s.Bastanteútile
economizaumbomtempopormostrartodasas“versões”simultaneamente.
Screen/f_ly
ApartirdeumURLinformado,Screen/f_ly(http://ow.ly/e/zero.oldstylecUU)permiteescolher
avisualizaçãodeum siteemdiversostiposdedispositivos( Desktop, T a b l e t, M o b i l ee
TV),inclusivecomvaria çõesdasprincipaisresolu ções/modelosdecadaum.
Screenqueri.es
Screenqueri.es(http://ow.ly/e/zero.oldstyledh/six.oldstyle)éumaferramentadetestesdesitesemvárias
resoluçõesparaosadoradoresde pixel-perfect. Alémdepermitirvisualizaro site
emdiversasresolu çõespré-de/f_inidaspelosmodelosdeaparelhosmaisconhecidos,
permitearrastarlarguraealturaparavercomoo siteseapresentadentrodeum grid
demarcação.Muitobomparatestarositeemvários breakpointsdiferentes.
/one.oldstyle/four.oldstyle/zero.oldstyle

## Página 149

CasadoCódigo Capítulo/seven.oldstyle. Continuandoseusestudos
/seven.oldstyle . /nine.oldstyle T/e.sc/m.sc/p.sc/l.sc/a.sc/t.sc/e.sc/s.sc /e.scF/r.sc/a.sc/m.sc/e.sc/w.sc/o.sc/r.sc/k.sc/s.sc
Depoisdejáteraprendidobemosprincípiosetécnicasdo web designresponsivo,
vocêpodequereragilizarosprojetosusandomodelosou fr a mewo r ksresponsivos.
Vejaosmelhores/maisusadosnomundo,estudecadaumdeleseencontreoque
melhorseencaixaaoseuestilo.
/one.oldstyle/one.oldstyle/four.oldstyle/zero.oldstyleCSSGrid
/one.oldstyle/one.oldstyle/four.oldstyle/zero.oldstyleCSSGrid(http://ow.ly/dPJw/one.oldstyle)seencaixaperfeitamenteemummonitorde
1280pxe,emmonitoresmenores,torna-se/f_luídoeseadaptaàlarguradonavegador.
Apartirdecertoponto,eleusa Media Queriesparaservirumaversãomóvelque,
essencialmente,empilhatodasascolunasparaqueo/f_luxodeinforma çãoaindafa ça
sentido.
/three.oldstyle/two.oldstyle/zero.oldstyleandUp
/three.oldstyle/two.oldstyle/zero.oldstyleandUp(http://ow.ly/dPLxU)éumdosmodelosparadesignresponsivomais
conhecidos.Alémdascaracterísticasmaisóbvias(comolayout/f_luído,imagens/f_lexí-
veis,etc),eletemavantagemdeagradaraosquegostamdeLESSeSASSparamexer
comoCSSejávemcomModernizreSelectivizr.
Foundation/three.oldstyle
Foundation/three.oldstyle(http://ow.ly/dQqdG)seautointitulao mais avançada framework
responsivo de front-end do mundo.SeupoderososistemadegridéfeitocomSASS,
assimcomoseuselementosdeUIedemaiscaracterísticas.Jácontacomalguns add-
o n s,comotemplatesHTML,íconesdefontes,tabelasresponsivasemais.
Frameless
Frameless(http://ow.ly/dPIZS)éumgridfeitoparadesignsresponsivocomco-
lunasdelargura-/f_ixa,ouseja,aoinvésdetudoser/f_luído,dependendodaresolu ção
maisoumenoscolunassãoexibidasnatela.Seu slogané“Adaptarcolunaporcoluna,
nãopixelporpixel”.
Initializr
Initializr(http://ow.ly/e/zero.oldstyleAjK)éumgeradordetemplatesparaHTML/five.oldstyleparaaju-
daracome çarainiciarnovosprojetos. OkitcontacomHTML/five.oldstyleBoilerplateem
/one.oldstyle/four.oldstyle/one.oldstyle

## Página 150

/seven.oldstyle./one.oldstyle/zero.oldstyle. Palavras/f_inais CasadoCódigo
combinaçãocomTwitterBootstrap,jQueryeModernizr.Elegeraummodelolimpo
personalizávelcomapenasoqueéprecisoparacome çaroprojeto.Altamentereco-
mendado!
inuitCSS
inuitCSS(http://ow.ly/dPKio)éum fr a mewo r kpara designresponsivoqueconta
comumasériede pluginspara b re a d c r u mb, dropdown,navegação,dentreoutros.
ResponsiveGridSystem
ResponsiveGridSystem(http://ow.ly/e/zero.oldstylez/two.oldstyleM)éumamaneirarápida,fácile/f_le-
xíveldecriar web sitesresponsivos.Seusistemade gridsérealmentefácildeentender
eusaratravésdeumamarca çãosimpleserápida.
Skeleton
Skeleton(http://ow.ly/dPID/six.oldstyle)éumacoleçãodearquivosCSSeJSqueformuma
sériedecomponentesdeUIparaajudaradesenvolverrapidamente sitesquesãobem
vistosemqualquerresolu ção.
TwitterBootstrap
TwitterBootstrap(http://ow.ly/dPHWq)éum fr a mewo r kcompletopara fr o n t-
end.PossuidiversoscomponentesdeUI, plugins javascripteum gridresponsivoque
vaiagilizarbastanteodesenvolvimentodeseusprojetosfuturos.
/seven.oldstyle./one.oldstyle/zero.oldstyle P/a.sc/l.sc/a.sc/v.sc/r.sc/a.sc/s.sc /f.sc/i.sc/n.sc/a.sc/i.sc/s.sc
NãodevesernenhumasurpresaqueastécnicaseconhecimentosmostradosnoLi-
vrosãotãodinâmicosemutáveisquantoaprópria web!Então,nadadeacharque
agoravocêéoSr. (ouSra.) Responsividade;vocêestáaapenascome çandoajor-
nadae,comodiria Morpheus, há uma diferença entre conhecer o caminho e trilhar o
caminho.
Bonsestudos!
/one.oldstyle/four.oldstyle/two.oldstyle

## Página 151

CasadoCódigo ReferênciasBibliográ/f_icas
ReferênciasBibliográ/f_icas
/one.oldstyle/four.oldstyle/three.oldstyle