---json
{
  "id": "dominando_javascript_com_jquery",
  "title": "Dominando JavaScript com jQuery",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Dominando JavaScript com jQuery.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "com",
    "dominando",
    "java",
    "javascript",
    "jquery",
    "linguagens"
  ],
  "perguntas_tipo": [
    "Como utilizar Dominando JavaScript com jQuery?",
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

# Dominando JavaScript com jQuery

> **Arquivo Original:** `Dominando JavaScript com jQuery.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© 2012, Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográficos,
eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 5

CasadoCódigo
Prefácio
--Ah,vocêprogramaemjQuery?
Mesmoqueessafraseirriteumdesenvolvedorexperiente,elaéaprincipalprova
dequeumframeworkdefinitivamentefoiadotadoemmassapelomercado,aoponto
deserconfundidocomumalinguagemdeprograma ção.Eesseédefinitivamenteo
casoquandofalamosdojQuery-umframeworkquesemdúvidasrevolucionouo
desenvolvimentoweb,simplificandoabsurdamentetarefascorriqueirasdodesen-
volvimentoweb.
AmelhormaneiradeconseguirexplorartodoopotencialqueojQuerypode
oferecer,éconhecendomelhorJavaScript-alinguagemdaweb,eoambienteonde
todoessecódigoéexecutado:navegadoresepáginasHTML.Valelembrarqueesse
mesmoJavaScriptextrapolouoslimites,esefazpresentenobackend,emjogos,
servindodemotorparaimplementa çõesdenovasmáquinasvirtuais,emula çãode
hardwaresantigoseatécomolinguagempadrãodeplataformasinteiras,comoFire-
foxOSeWindows8!
Sim,oJavaScriptpassoudoestigmadelinguagemodiadaemalcompreendida
aumadasmaisinteressanteseessenciais.EojQueryécertamenteumdoscatalisa-
doresdessamudan ça.
Nestelivro,PlínioBalduinopartedeumcódigoJavaScript,queestavaprestesa
setornarimpossíveldemanter,parasimplificá-locomousodejQuery,enquanto
apresentaofuncionamentodoframeworkpordebaixodospanos. Aaplica çãoJa-
vaScripttemaquelesaborquetantoconhecemos: muitamanipula çãodeDOMe
invocaçõesAJAX,deondecome çamabrotarIFsetécnicaspoucoortodoxas(asco-
nhecidasgambiarras)paraseprotegerdasincompatibilidadesentrenavegadorese
suasidiossincrasias.
Muitosfizeramapostasparaofuturodaslinguagensdeprograma ção;Hojeve-
mosqueosqueapostaramforteemlinguagensestáticasestãoobservando,boqui-
abertos,avelocidadeemqueoJavaScripttomaespa çonomercado.Justamenteos
i

## Página 6

CasadoCódigo
pontosfracosdalinguagemforamosquepossibilitaramqueelaresistisseàerosão
dotempo;suapermissividadeajudoudesenvolvedoresdediversasépocasafornece-
remfuncionalidadesquenãoestavamdisponíveis(maisconhecidoscomo shimsou
polyfills),enofimdascontas,um“projetode10dias”comquase20anosdeidadese
tornassenadamenosdoqueumadasmaisimportanteslinguagensdaprograma ção
moderna.
OJavaScriptveiopraficar,enãovaidesaparecertãocedo. ComooBrendan
Eich,criadordalinguagemdiz:
--“alwaysbetonJS”
Douglas ’ qmx’Campos
ii

## Página 7

CasadoCódigo
Agradecimentos
Agradeçoaosmeuspais,LuiseIsabel,pelosuportedeumavidainteiraepelaexce-
lenteeducação.
ObrigadoPauloSilveira,AdrianoAlmeidaeSérgioLopes,pelaconfian çaaoen-
tregaremtamanharesponsabilidadenasminhasmãosepeloapoioesensocrítico
durantetodaaprodu çãodestelivro.
Muitoobrigado,AndréNoel,pelagentilezadecederumdeseustrabalhospara
ilustrarestelivro.CasovocênãosejaoAndréNoeleaindanãoconheceotrabalho
dele,recomendofortementeumavisitaaohttp://www.vidadeprogramador.com.br
Thankyoumr.BrendanEichforyourworkandthankyouforansweringmy
questionssopromptlyandkindly.I’llpayyousomebeersnexttimeyou’llbeinSão
Paulo.
Fazendoum momentoMaguila,eunãopoderiadeixardeagradecertambéma
AlexandreBorba,AndréFaria,BrunoOliveira,DiegoPlentz,DouglasCampos,Edu-
ardoCintra,FrancelinoGuilherme,IgorHercowitz,LucasCarvalho,MarceloTar-
deli,OsniOliveira,RicardoMassuia,RodrigoLorca,ViniciusBaggio,aosamigosdo
GURU-SP,GURU-ESeAdapti.
Minhaesposaemeusfilhossentiramopesoepre çodetodootempoqueinvesti
nesselivro,masaindaassimficaramaomeulado,meapoiandoeempurrandopara
frente.Sentimuitomaisafaltadevocêsdoquerealmenteaparentou.
Finalmente,agradeçotambémavocê,leitor.Esperoquevocêssedivirtamtanto
lendoquantoeumedivertiescrevendo.
// Plínio Balduino
(enjoy)();
iii

## Página 9

CasadoCódigo
Sobreoautor
Desenvolvosoftwaresprofissionalmentedesdeoséculopassadoejápasseiporquase
todasasplataformasdedesenvolvimentoparadesktop,webemobile.
Apartirde2004comeceiaperceberopoderportrásdoJavaScriptedoAJAX,
masaindaestavaquebrandoacabe çafazendotudonamão,semaajudadefra-
meworksoubibliotecasespecializadas.
Deunsanosparacá,aprendendoScheme(umdialetoLISPvoltadoparaoapren-
dizado)ecolaborandonosprimórdiosdodynjs(implementa çãodoJavaScriptpara
amáquinavirtualdoJava),conseguienxergarmelhoropotencialdalinguagem,e
comeceiafalararespeitoemeventoseconferências.
v

## Página 11

CasadoCódigo Sumário
Sumário
1 Apresentação 1
1.1 PorqueumlivrosobreJavaScriptejQuery? . . . . . . . . . . . . . . . 1
1 . 2 C o m ool i v r oe s t áo r g a n i z a d o....................... 2
1 . 3 A l g u m a sp a l a v r a ss o b r eJ a v a S c r i p t .................... 2
1 . 4 L i s t ad ed i s c u s s ã oec ó d i g of o n t e...................... 3
2 Refazendoumalojavirtual 5
2 . 1 Al o j av i r t u a ld aR o g u sM u s i c....................... 5
2 . 2 U ms i t es e mJ a v a S c r i p t........................... 6
3 AdicionandoJavaScript 9
3 . 1 U mn o v ol a y o u t............................... 9
3 . 2 E n t e n d e n d oI D sec l a s s e s.......................... 1 1
3 . 3 U m aq u e s t ã od eD O M........................... 1 1
3 . 4 L o c a l i z a n d oov a l o rt o t a ld oc a r r i n h o................... 1 2
3 . 5 U s a n d o= = =e= =.............................. 1 6
3 . 6 A l t e r a n d ooc a m p od ot o t a l ........................ 1 7
3.7 IncluindoumarquivoJavaScriptnapágina . . . . . . . . . . . . . . . 18
3.8 Brincandocomocódigodeumjeitomaisprofissional . . . . . . . . . 18
3.9 Meubrowsernãotemconsole.Eagora? . . . . . . . . . . . . . . . . . 19
3 . 1 0C a l c u l a n d oo ss u b t o t a i sd o si t e n s.....................2 0
3 . 1 1 E n t e n d e n d oe v e n t o s............................. 2 5
3.12 Aseguir,cenasdopróximocapítulo. . . . . . . . . . . . . . . . . . . . 26
vii

## Página 12

Sumário CasadoCódigo
4 UmJavaScriptdiferenteemcadanavegador 27
4 . 1 N e mt u d os ã ofl o r e sn or e i n od aW e b................... 2 7
4.2 Quandonãoexisteumadeterminadafun çã o.............. 2 8
4.3 Funçõ e sa n ô n i m a sen o m e a d a s...................... 3 1
5 SimplifiquecomjQuery 33
5 . 1 Oq u eéj Q u e r y................................ 3 3
5.2 EntendajQueryemcincominutos . . . . . . . . . . . . . . . . . . . . 34
5.3 Nossocódigoantigo,agoracomjQuery . . . . . . . . . . . . . . . . . 37
5 . 4 P r o g r a m a n d od ef o r m af u n c i o n a l.....................4 0
5 . 5 E v e n t o sec a l l b a c k s.............................. 4 1
5 . 6 Eoq u ev e ma g o r a ?............................. 4 3
6 Dominandoeventosemanipula çãodeDOMcomjQuery 45
6 . 1 C r i a n d ou m al i s t ad et a r e f a s........................ 4 5
6.2 Usandoeventosdeumjeitomaisprofissional . . . . . . . . . . . . . . 47
6 . 3 D e s a s s o c i a n d oe v e n t o s...........................4 9
6 . 4 R e m o v e n d oi t e n sc o me s t i l o........................ 5 1
6 . 5 E d i t a n d oi t e n s................................ 5 4
6 . 6 E d i t a n d oa p e n a su mi t e md ec a d av e z................... 5 5
6.7 Disparandomaisdeumeventoaomesmotempo. . . . . . . . . . . . 57
6 . 8 S a l v a n d oat a r e f a............................... 5 8
6.9 Indoaindamaisfundonamanipula çã od eD O M............ 5 9
6 . 1 0A d i c i o n a n d ot a r e f a s.............................6 0
7 NãotenhamedodoAJAXedoJSON 63
7 . 1 A J A X ?Q u eb i c h oée s s e ?.......................... 6 3
7 . 2 U s a n d ooj s F i d d l e..............................6 6
7 . 3 N o s s op r i m e i r oc ó d i g oc o mA J A X.....................6 8
7 . 4 E n v i a n d op a r â m e t r o sc o mA J A X.....................6 9
7 . 5 Oo b j e t oj q X H R............................... 7 1
7 . 6 Eoq u eéoJ S O N ?.............................. 7 4
7 . 7 J u n t a n d oJ S O NeA J A X........................... 7 8
7.8 Políticasdeseguran çad o sb r o w s e r s....................8 0
viii

## Página 13

CasadoCódigo Sumário
8 UmgerenciadordetarefascomAJAX 83
8 . 1 M e l h o r a n d on o s s og e r e n c i a d o r...................... 8 3
8 . 2 C a r r e g a n d oa st a r e f a sd os e r v i d o r.....................8 4
8 . 3 U s a n d op a r â m e t r o so p c i o n a i s.......................8 9
8 . 4 A l t e r a n d ot a r e f a s............................... 9 1
8.5 Umaintrodu çã oa oR E S T..........................9 4
8.6 UtilizandoPUTeDELETEnobrowser. . . . . . . . . . . . . . . . . . 95
8 . 7 A d i c i o n a n d ot a r e f a sc o mR E S T...................... 9 5
8 . 8 E x c l u i n d ot a r e f a s............................... 9 7
9 jQueryUI 99
9 . 1 U s a n d ooj Q u e r yU I.............................9 9
9 . 2 A sd i v e r s a sp a r t e sd oj Q u e r yU I......................1 0 1
9 . 3 T e m a s.....................................1 0 2
9.4 Organizandoseusdadoscomaccordion . . . . . . . . . . . . . . . . . 103
9 . 5 A u t o - c o m p l e t a n d o..............................1 0 5
9 . 6 U s a n d ob o t õ e sm a i sb o n i t o s........................1 0 6
9 . 7 E s c o l h e n d oad a t ac o moc a l e n d á r i o...................1 0 7
9 . 8 E x i b i n d oj a n e l a sd e n t r od aj a n e l a.....................1 1 0
9 . 9 Op r o b l e m ac o moj Q u e r yU I.......................1 1 2
10 jQueryMobile 115
1 0 . 1 E n f r e n t a n d oom o b i l e............................1 1 5
10.2 Cuidadocomotempodecarregamento . . . . . . . . . . . . . . . . . 117
11 OrientaçãoaobjetosnoJavaScript 119
1 1 . 1 O b j e t o sn oJ a v a S c r i p t............................1 1 9
11.2 Funçõ e sp a r aq u e mn ã ot e mc l a s s e....................1 2 3
11.3 Entendendoprototipaçã o..........................1 2 5
11.4 Usandoherança...............................1 2 8
1 1 . 5 M i x i nn oJ a v a S c r i p t.............................1 3 3
ix

## Página 14

Sumário CasadoCódigo
12 Umpoucodeprogramaçãofuncional 139
12.1 Oqueéprogramaçãofuncional . . . . . . . . . . . . . . . . . . . . . . 139
12.2 Highorderfunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . .140
12.3 Escopo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
12.4 Closures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
12.5 Currying . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
13 CriandopluginsparajQuery 147
13.1 Oquesãoplugins?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
13.2 Aanatomiadeumplugin. . . . . . . . . . . . . . . . . . . . . . . . . . 148
13.3 Escrevendoadeclaraçãodoplugin . . . . . . . . . . . . . . . . . . . . 151
13.4 OalgoritmodeCPF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
13.5 Adicionandofuncionalidadeaoplugin . . . . . . . . . . . . . . . . . . 156
13.6 Personalizandooplugin . . . . . . . . . . . . . . . . . . . . . . . . . . 159
13.7 Maisplugins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
13.8 Ondeaprendermais. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
14 DicasparausarmelhorojQuery 163
14.1 Porqueperformanceéimportante?. . . . . . . . . . . . . . . . . . . . 163
14.2 U s esempreaversãomaisrecente . . . . . . . . . . . . . . . . . . . . . 164
14.3 Escolhaosseletorescorretosparaatarefa . . . . . . . . . . . . . . . . 165
14.4 Nãoseesqueçadocache . . . . . . . . . . . . . . . . . . . . . . . . . . 166
14.5 Asvezes,menosémais . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
15 Eoquevemagora? 173
15.1 jQuery2.0. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
15.2 Recomendações deleitura . . . . . . . . . . . . . . . . . . . . . . . . . 174
15.3 Fim? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
ÍndiceRemissivo 179
Bibliografia 180
x

## Página 15

Capítulo1
Apresentação
“Umbomcomeçoémetadedotrabalho. ”
–Provérbioholandês
1.1 Por que um livro sobre Jav aScript e jQuery?
ExistemmuitoslivrosnomercadosobreJavaScriptejQuery,masamaioriadeles
acabapecandopornãomostrarrealmentealinguagem,ouporapresentarosassun-
tosdemaneiraengessada,ousimplesmenteporseremmanuaisdereferênciaque
jogamtodooconteúdosobreoleitorsemmostrarcasosreaisdeusoesemapresen-
tarumamotiva çãoparaquesejafeitodaquelaforma.
Obviamente,existemlivrosmuitobonsqueeurecomendofortemente,comopor
exemplooJavascript:TheGoodParts [4],deDouglasCrockford,masquepodemser
traumáticosparaquemestácomeçandoagora.
Minhaideianãoéabra çaromundoeescreverolivrodefinitivosobreJavaScript
ejQuery,masapresentardemaneiradidáticacomoresolverproblemascotidianos,

## Página 16

1.2. Comoolivroestáorganizado CasadoCódigo
semtrataroleitorcomocrian ça. Apresentarosassuntosdamaneiramaisfluídae
agradávelpossívelseráomeudesafio.
Eusempregosteidelivrosquemeapresentamumatecnologia,memostram
comoutilizá-laecomosobreviverquandoestoucome çando,eaindacontinuamúteis
depoisqueeujápasseiaestarconfortávelnaqueleambiente.Éexatamenteissoque
euqueroqueesselivrosejaparavocê,leitor.
1.2 Como o livro está organizado
Olivrocome çacomahistóriadeumalojavirtualbemantigaque,porumasériede
razões,nãoutilizouJavaScriptemsuaversãooriginal.Noscapítulos3e4euapre-
sentoalinguagemenquantoreescrevoocarrinhodecomprasutilizandoJavaScript
puro,sembibliotecasadicionaisecomtodaadificuldadedeseescrevercódigopara
múltiplosbrowsers.
Apartirdocapítulo5,apresentoabibliotecajQueryesubstituoquasetodoo
trabalhoquefizemoscomJavaScriptpuroporchamadasmaissimples.
Nocapítulo6nósvamosdesenvolverumalistadetarefasparaaprendermos
comomanipularafundooselementosdasuapáginaHTML.Aquivamosvoltarao
nossocarrinhodecompraseadicionarefeitosparadeixarovisualmaisatraente.
Voltaremosàlistadetarefasnocapítulo8,dessavezadicionandorecursosdeAJAX
eJSONqueaprenderemosnocapítulo7,alémdetermosumabreveintrodu çãoao
RESTecomoutilizarcomjQuery.
VamosfalartambémsobrejQueryUI,seusefeitosecomponentesvisuaisno
capítulo9esobrejQueryMobilenocapítulo10.
Finalmente,temosoqueeuconsideroacerejadobolo:nocapítulo11eudemons-
trocomoutilizarorienta çãoaobjetosnoJavaScript,indoalémdofeijãocomarroze
ensinandoausarprototipa ção,herançaclássicaeherançamúltipla;nocapítulo12eu
apresentoalgunsfundamentosdeprograma çãofuncionalenocapítulo13vocêusa
tudooquefoimostradonolivroeaprendeacriarseusprópriospluginsparajQuery.
Nofinaldolivrovocêencontraocapítulo14quedádicasdecomoescrevercó-
digocomjQueryqueexecutemaisrapidamente.
1.3 Algumas palavras sobre Jav aScript
Daslinguagensfamosaselargamenteusadas,talvezoJavaScriptsejaamenoscom-
preendida.
2

## Página 17

CasadoCódigo Capítulo1. Apresentação
Issosedeve,aomeuver,aopreconceitoqueafezsertratadacomoumaversão
simplificadadoJava.OfatodamaioriadoscriadoresdepáginasparaWeb,naépoca
chamadosde Webmasters,nãoteremumbomentendimentodoquealinguagem
podefazertambémauxiliou.Elessimplesmentecopiavamocódigodealgumsitee
colavamnaprópriapágina.
QuandoBrendanEichdesenvolveuaprimeiraversãodoJavaScriptparaobrow-
serMozilla,em1995,aideiaeraquealinguagemrealmentetivesseumasintaxepare-
cidacomJava,pegandoemprestadoatémesmoalgunsobjetosemétodoscomnomes
iguais.Opróprionome,JavaScript,foiumajogadademarketingparaquealingua-
gempudessepegarcaronanosucessodoJava,quebrandoaresistênciadaspessoas
emaprenderumanovalinguagem.
Poroutrolado,somadoaissoumasériedeescolhasruinsdedesign,pratica-
mentedoister çosdalinguagemacabaramignorados,sejapelaresistênciaemapren-
der,sejapelosimpleshábitodecopiarecolarousejapelofatodequeodesenvolvi-
mentoparaWebnãoeraalgomaduronaépoca.
NaspalavrasdeDouglasCrockford[3]:
“AmaioriadaspessoasqueescrevecódigoemJavaScriptnãoédeprogramadora.
Lhesfaltaotreinamentoeadisciplinaparaescreverbonsprogramas.JavaScripttemé
umalinguagemtãopoderosaqueaindaassimelesconseguemfazeralgoútil.Issodeu
aoJavaScriptareputa çãodeserusadaunicamenteporamadores,equenãoserve
paraprogramaçãoprofissional.Issosimplesmentenãoéverdade.”
–DouglasCrockford
Apósalgunsanos,alinguagempassouasermelhorcompreendida,come çoua
perderostatusde linguagemdebrinquedo.Issoaconteceuespecialmentedepoisdo
desenvolvimentoepopulariza çãodeferramentascomooRhino,quepermiteque
vocêexecutecódigoJavaScriptnaMáquinaVirtualdoJava;node.js,quepermite
quevocêdesenvolvaservidorescomJavaScript;efinalmenteojQuery,queabstraie
simplificamuitoodesenvolvimentonobrowser.
1.4 Lista de discussão e código fonte
Disponibilizamosumalistadediscussãosobreolivro,ondevocêpoderátirardúvi-
das,apontarcorre ções,indicarmelhoriaseoquemaisacharqueforrelevantepara
ooutrosleitores:
https://groups.google.com/d/forum/casadocodigo-js-jquery
3

## Página 18

1.4. Listadediscussãoecódigofonte CasadoCódigo
OcódigofonteestarádisponívelnoGitHub,noendere çoabaixo:
https://github.com/pbalduino/livro-js-jquery
Sinta-seàvontadeparaenviardúvidasealterarosfontesconformevocêforavan-
çandonolivro.
Figura1.1:Eessahistóriacome çoumaisoumenosassim
4

## Página 19

Capítulo2
Refazendoumalojavirtual
“Soumuitobomcomopassado.Éopresentequeeunãoconsigoentender. ”
–NickHornby-HighFidelity
2.1 A loja virtual daRogus Music
Nosidosde1998,aRogusMusic,quejátinhalojasdeCDseDVDsemváriosshop-
pingsdacapital,inovouelan çouumalojavirtual. Alojapermitiuqueseusclien-
tespudessemencomendartítulosimportados,lan çamentosepresentearsemsairde
casa.
Duranteanos,odonodaRogusnãosepreocupouematualizarosite,sempre
dizendoque“emtimequeestáganhandonãosemexe”.Otempopassou,osfilhos
assumiramonegócioeaempresapassouasechamarapenasRogus. Hojeemdia
ninguémmaiscompraCDs,eDVDsjánãofazemmaistantosucesso.ARogusagora
vendeBlu-rays,jogoseeletrônicos.
Agora,osdonosdaRogusquerematualizarositeemelhoraraexperiênciado
usuário.ComoelestêmpoucaexperiênciacomdesenvolvimentoparaWeb,resolve-

## Página 20

2.2. UmsitesemJavaScript CasadoCódigo
ramregistraroserroseacertos.Comodisseomaisvelho,“Quemsabeumdiaisso
nãoviraumlivro?”.
2.2 Um site sem Jav aScript
Figura2.1:SiteoriginaldaRogusMusic
AversãooriginaldositenãotemsequerumalinhadeJavaScript. Segundouma
crençaexistentenaépocaemqueositefoicriado,JavaScriptpoderiainfectarocom-
putadordousuáriocomvírus.Dequalquermaneira,osbrowsersficarammuitomais
seguros,ehojeemdiaéimprovávelquealgumcomputadorsejainfectadoporum
6

## Página 21

CasadoCódigo Capítulo2. Refazendoumalojavirtual
códigoJavaScript.
Umproblemaqueissocausanonossositeéquecadaaltera çãonacomprado
usuário,cadaverificaçãodeCPFecadacliqueemumlinkéenviadoaoservidor,
sobrecarregando-o,tornandooprocessomaislentoefazendocomqueaexperiência
dousuáriosejaruim,poisatodomomentoapáginainteiraérecarregada.Vocêjá
nãopreencheulongoscadastrosnainternetque,acadapróximopasso,atelatodaé
renderizada,causandoaimpressãodelentidão?
Umaformaderesolvermosissoédeixandoqueoprópriobrowserfa çaumaparte
dotrabalho,diminuindoacarganoservidoredeixandoousuáriocomaimpressão
dequeositeficoubemmaisrápido.Comoumefeitocolateral,oservidorvaisuportar
maiscomprassimultâneassemanecessidadedeumupgrade.
Afigura2.2nosdáumaideiamelhordecomooservidorvairecebermenos
requisições.
7

## Página 22

2.2. UmsitesemJavaScript CasadoCódigo
Figura2.2:Esquemaderequisi çõesaoservidor
Nospróximoscapítulos,vamosacompanharosdesafiosencontradospararees-
creveralojavirtual,prestandoaten çãonotrabalhofeitocomocarrinhodecompras.
8

## Página 23

Capítulo3
AdicionandoJavaScript
“JavaScripthadto‘looklikeJava’onlylessso,beJava’sdumbkidbrotheror
boy-hostagesidekick.Plus,Ihadtobedoneintendaysorsomethingworsethan
JavaScriptwouldhavehappened.”
–BrendanEich
3.1 Umn o v ol a y o u t
Oprimeiropassoaserfeitofoimudarcompletamenteodesigndatela.Podemosver
nafigura3.1comoocarrinhoficou.

## Página 24

3.1. Umnovolayout CasadoCódigo
Figura3.1:Designnovodocarrinhodecompras
Ocódigodocarrinhoé,basicamente,umatabela. ForamadicionadosIDse
classes,quenãoexistiamnolayoutantigo,paraquepossamosmanipularosdados
maisfacilmentecomJavaScript.
Listagem3.1:
<!-- -->
<table>
<tbody>
<tr>
<td>
<div>R$ 29,90 </div>
</td>
<td>
<input type="number">
</td>
</tr>
</tbody>
<tr>
<td></td>
10

## Página 25

CasadoCódigo Capítulo3. AdicionandoJavaScript
<td>Total da compra </td>
<td><div>R$ 29,90 </div></td>
<td></td>
</tr>
</table>
Agoraqueremospegarovalordecadaproduto,assimcomopegarovalortotalda
compra.ComopodemosacessarcadaumdessesvaloresatravésdoJavaScript?Pre-
cisaremosterumaformadeidentificarcadaelementodonossodocumentoHTML.
VamosprecisaradicionarIDseclassesconformeanecessidade.Paraquevocêen-
tendamelhorcomoissofunciona,vouadicioná-lospoucoapouco,conformeformos
avançandonoaprendizado.
3.2 Entendendo IDs e classes
ClasseseIDssãousadosparaidentificaroselementos.Conformeveremoscommais
detalhes,pensenumelementocomocadapedacinhodonossoHTMLformadopor
umatag.ÉimportanteutilizarclasseseIDstantoparaaplicarmoscores,posiciona-
mentoeformataçãousandoCSS,quantoparalocalizarmosvaloresquequeremosler
oualterarnonossocarrinhodecompras.
UmIDéumidentificadorúnicoutilizadoparaapontarumelementoespecífico
danossapágina.ÉumaboapráticanuncausardoiselementoscomomesmoIDna
mesmapágina.Casovocêuse,apáginavaicontinuarsendodesenhadaeseubrowser
nãovaiexplodir,masnãoesperequenossosscriptsfuncionemcorretamente. Um
elementosódeveterumID,eumIDsódevepertenceraumelemento.
Jáumaclasseéutilizadaparaapontarumoumaiselementos. Émuitousada
quandovocêquerusaramesmaformata çãoparaumgrupodeelementos. Uma
classepodepertencerainúmeroselementos,eumelementopodeterinúmerasclas-
ses.
3.3 Uma questão de DOM
Nafigura3.2nóspodemosvercomoocódigoHTMLdonossocarrinhodecompras
1érepresentadointernamentepelobrowser.
Essarepresentaçãointernadapáginaéchamada DOM,quesignifica Document
ObjectModel,ouObjetoModelodoDocumento,eécriadaautomaticamentepelo
browsertodavezquecarregamosumarquivoXMLouHTMLválido.Essearquivo
11

## Página 26

3.4. Localizandoovalortotaldocarrinho CasadoCódigo
échamadodeDocumento,ecadaitemdentrodele(textos,imagens,botões,caixas
detexto)échamadogenericamentede Elemento.
QuandoutilizamosJavaScriptparalerouescreverdadosnumapáginaHTML,
estamosnaverdademanipulandooDOM.ÉnavegandoemanipulandooDOMque
vamosconseguirdesenvolveronossocarrinhodecompras.
Figura3.2:ExibindooDOMcomoumaárvore
Ditotudoisso,vamosaoquerealmenteinteressa:descobrircomocalculareal-
terarovalor totaldonossocarrinhodecompras.
3.4 Localizando o v alor total do carrinho
Paralocalizarovalortotaldonossocarrinhodecompras,vamosadicionarum IDà
tag divcorrespondente,aoqualvamoschamarde total.Relembrando,vamosusar
umIDaquiporqueocarrinhotemapenasumvalortotal,oquetornaesseIDúnico
emtodoodocumento.
OtrechocorrespondentedonossoHTMLdeveficarassim:
<tr>
<td></td>
<td>Total da compra </td>
<td><div id="total">R$ 29,90 </div></td>
<td></td>
</tr>
</table>
12

## Página 27

CasadoCódigo Capítulo3. AdicionandoJavaScript
Vamosescreverumcódigobemsimplesparaexibirovalordototaldascompras.
Paraisso,primeiroprocuramosoelementodeID totale,emseguida,alteraremos
ovalorcontidodentrodoelementoquetemesseID.
LocalizarumelementopeloIDéaformamaisfácilparasetrabalharcomo
DOM.Paraisso,nósusamosafun ção getElementById()queoobjeto document
possui.
Depoisderecuperadooelemento,usamosapropriedade innerHTML.Essapro-
priedadefazexatamenteoquepromete:retornaotextoqueestáentreastagHTML
queformamoelemento.
Onde colocaremos nosso Jav aScript?
ApósofechamentodatagBODY,vamosabrirumespa çoparaescrever-
mosessesprimeiroscódigosJavaScript.Existemsolu çõesmaiselegantes
ecorretas,masnessesprimeirospassosvamosfazerdojeitorápido.
Lembre-sede nuncafazerissonoseucódigodeprodu ção,correndoo
riscodeservítimade bullyingporpartedoscolegas.
<!-- -->
</body>
<script type="text/javascript">
// aqui dentro vem o JavaScript
</script>
</html>
var total = document.getElementById("total");
alert(total.innerHTML);
Everemosamensagemdafigura3.3,exibindoovalortotaldacompranocarri-
nho.
13

## Página 28

3.4. Localizandoovalortotaldocarrinho CasadoCódigo
Figura3.3:Visualizandoovalordacompra
Agoravamosbrincarumpoucocomovalorquerecebemos. Tudodentrode
umarquivoHTMLétexto ,forçando-nosmuitasvezesafazerasdevidasconver-
sões.Faremosaconversãodotextoparanúmero,parapodermanipularovalorem
dinheiroeescrevê-lodevoltanodocumento.
Paraconverterotextoemumnúmeronãotemmuitosegredo. Bastaremo-
vermososímbolodemoeda,substituiravírgulaporpontoeusarmosafun ção
parseFloatpararetornarumnúmero. Honestamenteachoesseprocessochatoe
repetitivo,entãopoderíamosaproveitaretransformarissonumafun ção,quevaifi-
carassim:
function moneyTextToFloat(text) {
var cleanText = text.replace("R$ " , "").replace(",", ".");
return parseFloat(cleanText);
}
14

## Página 29

CasadoCódigo Capítulo3. AdicionandoJavaScript
Por que usar v ar?
SevocêjáviualgumcódigoJavaScriptantes,deveterpercebidoqueàs
vezesumavariáveléinicializadasemapalavrachave varemesmoassim
ocódigofunciona.
Quandovocêinicializaavariávelusando var,comoestamosfazendo
aqui,vocêestádeclarando-anomenorescopopossível,ouseja,elaéape-
nasumavariávellocal.
Quandovocênãoutiliza var,avariávelécriadanomaiorescopopossí-
vel,quegeralmenteéoobjeto window,quesimbolizaajaneladobrowser
queestamosusando.Issopodepermitirqueoutrocódigoemoutrolugar
altereessevalor,tornandoocomportamentodoseucódigoimprevisível.
Aregrageralé:use varedurmatranquilo.
Podemosaproveitareescreverumafun çãoquefazooposto,pegandoumvalor
numéricoejáformatandocomotexto.Assimficamosprontosparalerovalorcomo
texto,efetuartodososcálculosqueprecisarmosegravarovaloralteradodevoltano
documento.
Existeminúmerasformasdeseconverterumvalornuméricoparaumtexto
formatado. Euvouusaraabordagemdemultiplicarovalorpor100eemseguida
truncá-lousandoafun ção Math.floor,umavezquevamoslidarcomapenasduas
casasdecimais.Sevocêtivernecessidadedearredondarovalorparacima,useafun-
ção Math.ceiling.Emseguida,voufazerumadicionarosinaldemoedaeinserir
avírgulanaantepenúltimaposi ção,usandoométodo substr.Noteque,quandoeu
utilizo -2naposiçãodo substr,aposi çãoécontadadofimparaocome çodaString.
Nofinal,anossafun çãovaificarcomessacara:
function floatToMoneyText(value) {
var text = (value <1? "0" : "") + Math.floor(value * 100 );
text = "R$ " + text;
return text.substr(0, text.length - 2 ) + "," + text.substr(-2);
}
Seconsiderarmosqueafun ção moneyTextToFloatfazexatamenteoopostoda
função floatToMoneyText,evice-versa,podemosfazerumtestebemsimplespara
avaliarseelasestãofazendooquequeremos:
15

## Página 30

3.5. Usando===e== CasadoCódigo
var total = document.getElementById("total");
var formattedText = floatToMoneyText(moneyTextToFloat(total.innerHTML));
alert(formattedText === total.innerHTML);
Tudoissoficamelhoraindasecriarmosumafun çãoquesirvaparanosretornar
ovalordototaldocarrinho,semqueprecisemosficarrepetindocódigo.Usandoo
quejáfizemosacima,afun çãoficariaassim:
function readTotal() {
var total = document.getElementById("total");
return moneyTextToFloat(total.innerHTML);
}
3.5 Usando === e==
Noteque,paraefetuarmosacompara ção,usamos ===(trêssinaisdeigual),enão
==(doissinaisdeigual).Issoaconteceporqueooperador ==,aocontráriodeoutras
linguagensbaseadasnasintaxedoC, significaequivalência,enãoigualdade .
Issosignificaque,quandovocêusa ==,oJavaScripttentaconverterumdosva-
loresparaotipodooutro,comopodemosverabaixo. Alinhainiciadapor=>indica
oresultadodaexpressão,enãodeveserdigitada:
2 == 2 ;
=> true
1 == "1";
=> true
0 == [];
=> true
0 == "";
=> true
Porém,quandovocêutiliza===,oJavaScriptnãoconvertetiposeverificaaigual-
dadedosvalores,semtruques:
2 === 2 ;
=> true
16

## Página 31

CasadoCódigo Capítulo3. AdicionandoJavaScript
1 === "1";
=> false
0 === [];
=> false
0 === "";
=> false
Amenosquevocêtenhaummotivorealmentebomparautilizarooperadorde
equivalência,usesempre ===paraevitarqueerrosestranhosapare çamparapuxar
oseupé.Damesmaforma,casovocêqueiraverificarvaloresdiferentes,utilize !==
(comdoissinaisdeigual)aoinvésde !=(comumsinaldeigual).
3.6 Alterando o campo do total
Paraalterarovalordototaldocarrinho,vamoscriarumafun çãoquerecebeumva-
lornumérico,formata-ousandoocódigoquejácriamoseoescrevenoespa çoreser-
vadoparaovalortotal.Faremosissousandoajáconhecidapropriedade innerHTML,
quetambémpermitequevocêatribuaumvalor. Vamoschamarnossafun çãode
writeTotal.
function writeTotal(value) {
var total = document.getElementById("total");
total.innerHTML = floatToMoneyText(value);
}
Apenasparatestaroslimitesdonossocódigo,vamosusarovalorde PIcomo
totaldacompra:
writeTotal(3.14159);
Efinalmentepodemosveronossovalortotalformatadoealteradonafigura3.4
Figura3.4:
17

## Página 32

3.7. IncluindoumarquivoJavaScriptnapágina CasadoCódigo
3.7 Incluindo um arquivo Jav aScript na página
Agoraquetemosalgumasfun çõesprontasealgumafuncionalidade, éumaboa
práticasepararmosocódigoJavaScriptemumoutroarquivo. Vamoschamarde
rogus.js,eogravamosnodiretório javascripts.
Paraadicionaressearquivonanossapágina,vamosadicionaralinhaabaixoden-
trodase ção headdonossocódigo:
<script src='javascripts/rogus.js' type='text/javascript'></script>
Podemosapagaraquelase ção <script type="text/javascript"></script>
queficouvazialogoapósofechamentodatag body.
VamostambémretirardonossocódigoJavaScriptalinhacomo alertealinha
emquealteramosovalortotaldocarrinhopara PI.Comisso,ficamosapenascom
declaraçõesdefun çõesdentrodocódigo.
3.8 Brincando com o código de um jeito mais profis -
sional
Encheroseucódigode alertéumapéssimapráticaquesótinhajustificativaquando
sedesenvolviapara NetscapeeInternetExplorer5.Atualmente,browsersmodernos
comoo Firefox,o GoogleChromeeo Operatêmferramentasmuitoboasparadepu-
raçãoeverifica çãodecódigoJavaScriptdemodotransparente.
Parao Firefox,vocêvaiprecisardo Firebug,quepodeserbaixadoemhttps:
//getfirebug.com/.JáoChrome3.5,comosDeveloperToolseoOpera,como Drangon-
fly,jávêmcomferramentasdedesenvolvimentoembutidasenãoexigemainstala ção
deextensõesadicionais.
OInternetExplorerpassouateralgumasferramentasdedesenvolvimentoem-
butidasapartirdaversão8,masaindanãosãotãomaduraseeficientesquantoas
dosbrowsersacima.
18

## Página 33

CasadoCódigo Capítulo3. AdicionandoJavaScript
Figura3.5:ConsoleJavaScriptnoChrome
Usandoobrowserdesuapreferência,vamosusarasfun çõesquejácriamospara
manipularovalortotaldocarrinhodecompras,paraemseguidaexibiromesmo
valorparademonstrarquenossaaltera çãofuncionou. Semprequeutilizarmoso
Console,considerequealinhainiciadapor =>éoresultadodocomando,enão
deveserdigitada.
readTotal();
=> 189.7
writeTotal(123.45);
=> undefined
readTotal();
=> 123.45
Ototaldocarrinhoapareceráalteradoautomaticamentenanossapágina,con-
formepodemosvernaimagem3.6.
Figura3.6:Totalalteradopelonossocódigo
3.9 Meu browser não tem console .E agora?
NumasituaçãoemqueseubrowsernãoofereceumconsoleJavaScriptevocênão
podeinstalarumnovo,umaalternativaéaproveitarabarradeendere çoscomo
19

## Página 34

3.10. Calculandoossubtotaisdositens CasadoCódigo
prompt.
Vamosdigitarmosnobrowseroseguinteendere ço:
javascript:alert(readTotal());
Todooconteúdoapósosdoispontosserãoenviadosao engineJavaScriptdo
browser,quevaiinterpretareexecutar,conformeaimagem3.7.
Figura3.7:Resultadodocomandoviabarradeendere ços
Nãoétãobomquantoumconsole,masaindaémelhordoqueapráticadees-
palhar alertspelocódigo.
3.10 Calculando os subtotais dos itens
Paracalcularosubtotaldecadaproduto,vamosprecisardaquantidadeedovalor
unitáriodecadaprodutoqueestivernocarrinhodecompras.
Umaboaabordagemparafazermosissoélerprodutoaprodutodocarrinho,
calcularosubtotalearmazenaressevalorparaquepossamosutilizá-lonocálculo
dovalortotal.
Paraquepossamossaberoqueéumprodutodentrodenossapágina,vamos
voltaraonossocódigoHTMLeadicionaraclasse produtoacadalinhadatabela
quecontémonossocarrinhodecompras.
Precisamostambémdemarcarondepodemosencontrarovalorunitárioea
quantidadeasercompradapelousuário. Paraisso,vamosadicionar,respectiva-
mente,asclasses pricee quantity.
Teríamosalgoassim:
20

## Página 35

CasadoCódigo Capítulo3. AdicionandoJavaScript
<table>
<tbody>
<tr class="produto">
<td>
<div class="price">R$ 29,90 </div>
</td>
<td>
<input type="number" class="quantity">
</td>
</tr>
<!-- um produto de 59,90 -->
<!-- um produto de 99,90 -->
</tbody>
<tr>
<td></td>
<td>Total da compra </td>
<td><div id="total">R$ 189,70 </div></td>
<td></td>
</tr>
</table>
Vamosutilizarummétodoirmãodo getElementByIdparanosretornarosele-
mentosquecontémaclasse produto.Comovárioselementospodemteramesma
classe,ométodo getElementsByClassNamevainosretornarum arraydeelementos.
var produtos = document.getElementsByClassName("produto");
console.log(produtos);
=> [<tr class="produto">...</tr>]
Vamosprocuraroelementocomaclasse pricedentrodecadaumdositensdo
array. Comonessecaso getElementsByClassNamevainosretornarum arrayde
umaposição,podemosacessardiretamenteaprimeiraposi çãosemmaiorespreocu-
pações.
Comatagemmãos,vamosextrairovalorunitáriodoprodutocomafun ção
moneyTextToFloateexibi-lanoconsole.
21

## Página 36

3.10. Calculandoossubtotaisdositens CasadoCódigo
Console
NoChrome,FirebugeOpera,vocêpodeadicionarmensagensdedepu-
raçãonocódigousando console.debug(mensagem).
NoInternetExplorereno FirefoxsemFirebug,ocomandovaicausarum
erroepararaexecu çãodoseuscript.
Comisso,nossocódigovaificarassim:
for(var pos = 0 ; pos < produtos.length; pos ++) {
var priceElements = produtos[pos].getElementsByClassName("price");
var priceText = priceElements[0].innerHTML;
var price = moneyTextToFloat(priceText);
console.log(price);
}
Veremosalistagemdepre ços,comonafigura3.8.
Figura3.8:Totaislistadosnoconsole
Vamosentãolistarasquantidades,dentrodomesmo forqueacabamosdees-
crever:
var qtyElements = produtos[pos].getElementsByClassName("quantity");
var qtyText = qtyElements[0].value;
var quantity = moneyTextToFloat(qtyText);
console.log(quantity);
22

## Página 37

CasadoCódigo Capítulo3. AdicionandoJavaScript
Agoravemosaquantidadedositensnafigura3.9.Esse 3dentrodeumcírculo
indicaqueovalorfoirepetidotrêsvezes.Oconsoleevitouimprimirovalorrepetidas
vezes,jáqueissoajudaamanterasaídalegível.
Figura3.9:Quantidadeslistadasnoconsole
Temosentãoaquantidadeeopre çounitáriodecadaproduto.Multiplicamosum
pelooutroesomamosaumavariávelquevainosretornarovalortotaldosprodutos.
Precisamosdeclararavariável totalProdutosantesdo for,zerandoovaloran-
tesdecome çarmosaacumular.
var totalProdutos = 0 ;
for(var pos = 0 ; pos < produtos.length; pos ++) {
// e o código continua.
Finalmentesomaremososvaloresparaobtermosototal:
var subtotal = quantity * price;
totalProdutos += subtotal;
}
Apósofechamentodo for,vamosexibirototalquecalculamos:
console.log(totalProdutos);
Eisqueagora,nafigura3.10,temosovalorcalculadodetodososprodutosdo
nossocarrinho.
Figura3.10:Totaldosprodutosdocarrinho
23

## Página 38

3.10. Calculandoossubtotaisdositens CasadoCódigo
Paraficarbommesmo,vamosencapsularessecódigotododentrodeumafun-
ção,quevamoschamarde calculateTotalProducts. Onossocódigo,depoisde
todootrabalho,vaificarassim:
function calculateTotalProducts() {
var produtos = document.getElementsByClassName("produto");
var totalProdutos = 0 ;
for(var pos = 0 ; pos < produtos.length; pos ++) {
var priceElements = produtos[pos].
getElementsByClassName("price");
var priceText = priceElements[0].innerHTML;
var price = moneyTextToFloat(priceText);
var qtyElements = produtos[pos].
getElementsByClassName("quantity");
var qtyText = qtyElements[0].value;
var quantity = moneyTextToFloat(qtyText);
var subtotal = quantity * price;
totalProdutos += subtotal;
}
return totalProdutos;
}
Fiquetranquilo!Códigoslongoscomoesseserãoumaexce çãoporaqui.
Onde encontrar os códigos do livro
Oscódigosdolivropodemserencontradosnoendere çoabaixo,separa-
dosporcapítulos:
https://github.com/pbalduino/livro-js-jquery
Fiqueàvontadeparaalterá-losdaformaqueacharmelhor.
24

## Página 39

CasadoCódigo Capítulo3. AdicionandoJavaScript
3.11 Entendendo eventos
Eventossãochamadasdecódigoqueocorremquandoousuárioouobrowserexe-
cutamdeterminadasa ções. Temoseventosparaquandoousuárioclicaemalgum
lugar,paraquandomoveoponteirodomousesobreumaregiãoouquandoopon-
teirodomousesaidessaregião.
Aprenderatrabalharcomeventoséparteimportantedodesenvolvimentocom
JavaScript.
Vamosadicionarumcódigoqueatualizaovalortotaldocarrinhodecompras
semprequeousuáriomodificaraquantidadedeumproduto,semqueparaissoele
tenhaqueclicaremalgumbotão.
Vamoscomeçarcriandoafun çãoquedeveráserchamadatodavezquealguém
modificarumaquantidade:
function quantidadeMudou() {
writeTotal(calculateTotalProducts());
}
Mascomofazercomqueessafun çãosejainvocada? Bastapegarmostodosos
camposquetemaclasse quantityefalarque,semprequehouverumamudan ça
(onchange),afun ção quantidadeMudoudeveserchamada:
function onDocumentLoad() {
var textEdits = document.getElementsByClassName("quantity");
for(var i = 0 ; i < textEdits.length; i ++) {
textEdits[i].onchange = quantidadeMudou;
}
}
Pronto! Todavezquehouverumamudan çanessecampodeedi ção,anossa
função quantidadeMudouseráexecutada.
Masquemvaichamaressafun ção onDocumentLoadqueacabamosdecriar?
Bastadizerqueeladeveserexecutadaassimqueoeventodocarregamentodaja-
nelaacontecer!Paraissofazemos:
window.onload = onDocumentLoad;
Paratestar,atualizeapáginaealtereovalordequalquerumdositens.
25

## Página 40

3.12. Aseguir,cenasdopróximocapítulo CasadoCódigo
3.12 Aseguir, cenas do próximo capítulo
NossocódigoficoubacanaefuncionaredondinhonoChromeenoSafari. Mas,e
nosoutrosbrowsers?
NoInternetExplorer,porexemplo,elenãovainemserinterpretadoatéofinal.
Nopróximocapítuloestudaremosasparticularidadesdosprincipaisbrowserse
vamosmostrarcomoescrevercódigoquesejacompatívelcomeles.
26

## Página 41

Capítulo4
UmJavaScriptdiferenteemcada
navegador
“Anyonewhoslapsa‘thispageisbestviewedwithBrowserX’labelonaWebpage
appearstobeyearningforthebadolddays,beforetheWeb,whenyouhadverylittle
chanceofreadingadocumentwrittenonanothercomputer,anotherwordprocessor,
oranothernetwork.”
–TimBerners-Lee
4.1 Nem tudo são flores no reino da Web
Nossocarrinhodecomprarutilizarumapesquisaporclassesparacalcularototaldo
pedido,eatualizaautomaticamenteessevalorsemprequeousuárioalteraraquan-
tidadedeprodutos.
Porém,essapesquisaporclassessimplesmentenãofuncionanoInternetExplo-
rer8eversõesanteriores.IssosedeveaofatodequeapenasrecentementeaMicrosoft

## Página 42

4.2. Quandonãoexisteumadeterminadafun ção CasadoCódigo
começouasepreocuparcomospadrõesdaWeb,fazendocomquetenhamosque
escrevercódigoextraparaquenossositefuncionenoInternetExplorer.
Limitações dos browsers
Paradescobriressaseoutraslimita ções,vocêpodeusarosite CanIUse...:
http://caniuse.com/
Lávocêpodeverqueafun ção getElementsByClassNamesófoiimple-
mentadanessenavegadorapartirdaversão9.
Oquefazeragora?Abandonaressaversãodonavegadoreperderpossíveiscli-
entesqueusamumaversãomaisantiga?Utilizaroutraabordagem?
Asoluçãoquevaiserescrevernossoprópriocódigoquefa çaaanálisedetodos
oselementosdonossodocumentoeretornesomenteaquelesquepertencemàclasse
quequeremos.Sim,vaidartrabalho.Dequalquermaneirapodemosaproveitaros
navegadoresquejápossuemafun ção getElementsByClassNameenãocriaruma
nova.
Nopróximocapítulovamosdemonstrarcomopassarporcimadaincompati-
bilidadequeexisteentreosdiferentesnavegadoresesuasversões.Percebaqueisso
ocorremesmoparaasfun çõesmaisbásicas,paraasnecessidadesmaissimplesdo
nossowebsite.
4.2 Quando não existe uma determinada função
Vamoscriarnossoprópriocódigo[11]quefa çaessasele çãonoInternetExplorerin-
ferioràversão9.Emmuitaslinguagensprecisaríamoscriarumafun çãoe,fazendo
usodeum if,escolherqualdelasutilizar.Felizmente,comJavaScriptvocêconsegue
detectaremtempodeexecu çãoseaquelafun çãoestádisponívelounãoe,seneces-
sário,criarumafun çãocomomesmonomedaquelaqueestáfaltando. Paraisso,
vamosexecutarocódigoabaixo:
alert(document.getElementsByClassName === undefined);
VeremosamensagemnoInternetExplorer,conformeafigura4.1:
28

## Página 43

CasadoCódigo Capítulo4. UmJavaScriptdiferenteemcadanavegador
Figura4.1:IEnãoconheceogetElementsByClassName
Semprequevocêverificarumafun çãoouumavariávelquenãoexiste,você
receberá o valorundefined como resposta. Perceba que não usamos() após
getElementsByClassName,poisissofazcomqueafun çãosejaexecutada,oquevai
causarumerrocasoelanãoexista.
if (document.getElementsByClassName == undefined) {
alert("getElementsByClassName not found" );
}
Dentrodesse if,vamoscriarométodo getElementsByClassNameparaoobjeto
document. Paraisso,bastaatribuirmosuma funçãoanônima aonomedométodo.
Essafunçãoprecisareceberonomedaclassecomoparâmetro,comoacontececom
osoutrosbrowsers.
document.getElementsByClassName = function(className) {
alert("Regozijai-vos, usuários de Internet Explorer" );
}
Vamosentãousarométodo getElementsByTagNamecomocaracterecoringa
asteriscoparacriarum arraycomtodososelementosdonossodocumento. Em
seguida,vamosverificarcadaumdessesitensesepararemoutro arraysomente
aquelesquetenhamaclassequeestamosprocurando.
Comoumaboaprática,quandovocêprecisaracessarmaisdeumavezseguidao
mesmovalordeumapropriedadeoumétodo,jogueessevalornumavariávellocale
passeausá-la,comovamosfazercom elementClass.OJavaScriptconsomeumbom
tempolocalizandopropriedadesdentrodeumobjetoeissonosfazganharalguma
performance.
29

## Página 44

4.2. Quandonãoexisteumadeterminadafun ção CasadoCódigo
Declaração de v ariáveis dentro ou fora de um for
Existemalgumasdiscussõesemfórunsespecializadosegruposdeusuá-
riossobresermelhordeclararumavariáveldentroouforadeum forou
qualqueroutrotipodeitera ção.
Se,porumlado,existemargumentosdizendoqueadeclara çãodavariá-
velacadaitera çãotornaoprocessomaislento,existemoutrosemigual
quantidadedizendoqueofatodavariávelnãoestarnomenorescopo
possíveltambémcausaperdadeperformance.
Nofinaldascontas,efetuandotestesemdiferentesbrowsersesistemas
operacionais, nãonoteiquaisquerdiferen çassignificativasdeperfor-
manceedetempodeexecu ção.Como aotimizaçãoprematuraéaraizde
todososmales ,useaformaquedeixarseucódigomaislegíveleexpres-
sivo.
Se o elemento que está sendo verificado nofor não tiver uma classe,
elementClassseráundefinedefuncionarácomo falsedentrodo if. Ouseja,
if(elementClass)e if(elementClass !== undefined) sãoequivalentes.
var todosElementos = document.getElementsByTagName("*");
var resultados = [];
var elemento;
for (var i = 0 ; (elemento = todosElementos[i]) != null; i ++) {
var elementoClass = elemento.className;
if (elementoClass &&
elementoClass.indexOf(className) != -1 ) {
resultados.push(elemento);
}
}
return resultados;
Paraoqueprecisamosfazernanossalojavirtual,essecódigoémaisdoquesu-
ficiente,maseleapresentaumproblemaquevoudeixarparavocêresolver,como
formadeexercício:oqueaconteceseeupesquisarelementosquetenhamduasclas-
sessimultaneamente,comonocódigoabaixo?
30

## Página 45

CasadoCódigo Capítulo4. UmJavaScriptdiferenteemcadanavegador
<span class="message alert" >Lembre-se que a tag span não é spam </span>
Eseeutiverdoiselementoscomasmesmasduasclassesdeclaradasemordem
diferente?Considereaseguintelistagemdebandasderock:
<span class="product hot" >Screaming Trees </span>
<span class="hot product" >Sweet Oblivion </span>
Aimplementaçãode getElementsByClassNameretornaosdoiselementos span,
independentementedaordemdeclarada. Seuexercícioémelhoraranossaimple-
mentaçãoparaqueelapossafazeromesmo.
4.3 Funções anônimas e nomeadas
Existemdoistiposdefun çõesnoJavaScript: anônimasenomeadas.
Asfunçõesnomeadassãoasquejáconhecemos,esãoinvocadasatravésdopró-
prionome:
function olaMundo() {
console.log("Ola");
}
olaMundo();
Jáasfunçõesanônimasnãotêmumnomeparasereminvocadasdiretamente,
massãomuitousadascomoparâmetrosparaoutrasfun ções,ousãoatribuídasa
umavariável,queacabafuncionandocomoumnome.
function() {
console.log("Nunca serei executado : '( " )
}
var olaMundo = function() {
console.log("Serei executado =D" );
}
olaMundo();
Passaremosmuitasfun çõesanônimascomoargumento,comojáveremoscom
ojQuery.Emmuitoscasoselessãooscallbacks,aquelasfun çõesquesãochamadas
quandoqueremosserinformadosdequealgoocorreu.
31

## Página 46

4.3. Funçõesanônimasenomeadas CasadoCódigo
Vamosrevercomofizemosocallbackdase çãoanterior. Primeirodeclaramos
afun ção quantidadeMudouedepois,dentrodeumaoutrafun ção,definimosque
todososeventos onChangedevemchamarocallback quantidadeMudou:
function quantidadeMudou() {
writeTotal(calculateTotalProducts());
}
function onDocumentLoad() {
var textEdits = document.getElementsByClassName("quantity");
for(var i = 0 ; i < texts.length; i ++) {
textEdits[i].onchange = quantidadeMudou;
}
}
Aquiutilizamosumafun çãocomnomebemexplícito. MasemJavaScript,
quandoumafun çãosóéchamadaumavezeelaérelativamentesimplesecurta,
éfrequentenãodeclará-ladessaforma.Fazemostudojunto,deformaanônima.Re-
pare:
function onDocumentLoad() {
var textEdits = document.getElementsByClassName("quantity");
for(var i = 0 ; i < texts.length; i ++) {
textEdits[i].onchange = function() {
writeTotal(calculateTotalProducts());
};
}
}
Ficoumenor,masemalgumasvezespodecomplicaraleitura.Ficaadecisãodo
programador,mashabitue-sealercódigodessaforma.
32

## Página 47

Capítulo5
SimplifiquecomjQuery
“Nãoinvente.Façaobásico!”
–ProfessorLúcioAntoniodosSantos
Resolveressesnossospequenosproblemasqueaparecemnosdiferentesnave-
gadoresnãoseriafácil.SãodiversosInternetExplorers,Safaris,FirefoxeChromes,
alémdeoutrosmenores.Adivinhe?Alguémjáquebrouacabe çacomummontede
ifsecasosparticularesecriouumabibliotecacheiodecomandospararesolveros
casosmaiscomunsnodesenvolvimentoweb.OjQueryésemdúvidaolíderdesse
tipodebiblioteca.
5.1 Oq u eéjQuery
Numatraduçãolivre,deacordocomoprópriositedaferramenta,jQueryéuma
bibliotecaJavaScriptquesimplificaamanipula çãodedocumentosHTML,eventos,
animaçõeseintera çõescomAJAXparadesenvolvimentorápidodeaplica çõesweb.

## Página 48

5.2. EntendajQueryemcincominutos CasadoCódigo
Devidoàsuasimplicidadeeflexibilidade,ojQueryacabousetornandoabibli-
otecaJavaScriptmaisutilizada[17]. Em2008passouaserabibliotecapadrãodo
ASP.NETMVC,daMicrosoft,eoRubyonRails,apartirdaversão3,substituiuo
PrototypepelojQuery.
AmaneiramaissimplesdeutilizarojQueryéfazendoodownloaddoarquivo
JavaScriptnoendere ço:
http://jquery.com/download/
AmenosquevocêpretendaalterarouestudarocódigodojQuery,selecione
aopção production/minified,queécompactadaefazcomqueseusitelevemenos
tempoparaseraberto.
5.2 Entenda jQuery em cinco minutos
UmaexpressãojQueryéformadadeduaspartesprincipais: oquêvaisermanipulado
ecomoissovaiacontecer.
Vamosconsiderarquenossapáginatenhaotrechoabaixo,comdoisparágrafos
eumacaixadetexto.Oexemploaseguirestádisponívelnoendere ço
http://jsfiddle.net/pbalduino/MVAY3/
<p class="par">Primeira linha </p>
<p class="impar">Segunda linha </p>
<input type="text" id="texto" class="par" value="um texto qualquer" >
Quevaificarcomacaradaimagem5.1.
Figura5.1:NossapáginaantesdeusarmosojQuery
Noprimeiroexemplo,vamos selecionartodososparágrafos,quesãoosele-
mentoscomatag p,emudaracordefundoparaverde.Vocêpodeexecutaresses
exemplosnoconsoledoseubrowser.
$("p").css("background-color", "lightgreen");
34

## Página 49

CasadoCódigo Capítulo5. SimplifiquecomjQuery
Etemosoresultadonaimagem5.2.
Figura5.2:Depoisdeselecionarmosealterarmosatag’p
Simples,não?
O que significa o$, afinal?
Ocaractere $éusadocomoummodobemcurtodedizer jQuery.
Semprequevocêver$("p"),saibaqueissofazexatamenteamesmacoisa
que jQuery("p").Então,leiao $como jQueryetudobem.
Agoravamosselecionartodososelementosquecontenhamaclasse parevamos
mudarsuacordefundoparaazul.
$(".par").css("background-color", "lightblue");
Evemoscomoficounaimagem5.3.
Figura5.3:Depoisdeselecionarmosealterarmosaclasse’par’
ReparequeselecionamoselementospelaclasseoupelatagHTMLutilizandoa
mesmaforma $("alguma_coisa"),masnocasodaclasseutilizamosumpontona
frente.
35

## Página 50

5.2. EntendajQueryemcincominutos CasadoCódigo
Eadivinhe?Podemostambém selecionarumelementotambématravésdoID,
bastandoutilizaro #nafrentedastring. Paraexemplificar,vamosalteraracorda
fonteeoconteúdodanossacaixadetexto:
$("#texto").css("color", "white").val("esse é o novo texto" );
Notequeagora,apósselecionarmosoelementocom .css(...),usamosduas
funçõesjuntasparaalteraracordafonteeotexto.Aissochamamos encadeamento
defunções,eéumadasprincipaiscaracterísticasdojQuery:afun ção cssretorna
opróprioelementojácomaaltera çãoquefizemos,eassimvocêpodecontinuar
alterandooutrosvalores,comoestamosfazendocomo val,quealteraovalordeum
campode input.
Aimagem5.4mostracomonossapáginaficadepoisdedasaltera ções:
Figura5.4:Depoisdealterarmosacordafonteeotextousandooid’texto’
Nosexemplosquevimos,selecionamososelementosusandoastrêsformasmais
comuns:pesquisandopelatagHTML,simplesmenteinformandoatag;pelaclasse,
usandoumpontofinalantesdonomedaclasse;epeloID,usandoocaractere #antes
doidentificador.
Sim,essessãoosfamososselectors!
Essasformasdeselecionaroselementossãochamados selectors,esãoparte
fundamentaldojQuery. Osselectorsindicamoquênósvamosmanipular. Basi-
camente,entendendooconceitode selectors,vocêentendeamaiorpartedofunci-
onamentodoframework.
Amelhorpartedosexemplosqueexecutamoséqueelesrodamsemaltera ções
emqualquerbrowsermoderno.Sabendodisso,vamosvercomoficariaonossocar-
rinhodecomprasusandojQuery?
36

## Página 51

CasadoCódigo Capítulo5. SimplifiquecomjQuery
5.3 Nosso código antigo , agora com j Query
AgoraquevocêentendeucomousarojQuery,vamosreescrevernossocarrinhode
comprasusandoabiblioteca.
Oprimeiropontoquevocêvainotar,conformejárepetimosaqui,équevocênão
vaiprecisardeumcódigoespecíficoparaoInternetExplorer.Osdesenvolvedores
dojQueryjáfizeramotrabalhopesadoparanós.
Vamosseguiramesmaordemdocapítulo3,demonstrandocomopodemosre-
tornarovalortotaldocarrinhodecompras:
function readTotal() {
var total = $("#total").text();
return moneyTextToFloat(total);
}
Assimcomoo vallêealteraapropriedade valuedeumelemento input,afun-
ção texttrabalhacomotextoqueestádentrodasoutrastags,ignorandoformata ção
equaisqueroutrastagsqueestejamdentrodoelemento.
Vamosreescreverafun çãoquealteraovalortotal. Notequeométodo text
servetantoparalerquantoparaescreveronovotextodentrodoelemento total.O
jQueryusamuitodesseartifícioparatrabalharcompropriedades.
function writeTotal(value) {
var text = floatToMoneyText(value);
$("#total").text(text);
}
Intuitivo,não?
Sabendocomolerovalordeum inputecomolerotextodasoutrastags,vamos
reescreverafun çãoquecalculaovalortotaldositens.
Primeiro,vamosselecionaroselementoscomatag produto,quecontémaima-
gemdoproduto,descri ção,pre çounitárioequantidade. Avariável produtosvai
conterumelementoparacadaprodutodocarrinhodecompras.
var produtos = $(".produto");
Dentrodecadaprodutodocarrinho,precisamospegaropre çounitárioeaquan-
tidade.Paraencontrarmosovalordeumelemento(pre çoouquantidade)queestá
dentrodeoutroelemento(produtodocarrinhodecompras),precisamosusaromé-
todo find.
Vamostentarleraquantidadedoprimeiroprodutodocarrinho.
37

## Página 52

5.3. Nossocódigoantigo,agoracomjQuery CasadoCódigo
var primeiroProduto = produtos[0];
primeiroProduto.find(".quantity").val();
Hmm...algodeuerrado,conformepodemosvernaimagem5.5.
Figura5.5:Algonãofuncionoucomoesperado
O que acontece aqui é que, assim como o método
document.getElementsByClass, a instrução $(".produto") retornou um
ArraydeelementosdoDOM ,enãode objetosjQuery,eométodo findsóexiste
paraobjetosjQuery. Pararesolverisso,bastacolocaroelementodentrodo $(),e
eleéconvertidoparaumobjetojQuery,permitindoquepossamosusartodasas
funcionalidadesdabiblioteca.
var primeiroProduto = produtos[0];
$(primeiroProduto).find(".quantity").val();
Naimagem5.6vemosaquantidadeasercompradadoprimeiroprodutodocar-
rinho.
Figura5.6:Agorafuncionou
Agoraqueestamosatentosaessasutilezadabiblioteca,podemosreescrevera
funçãoquecalculaototaldopedidousandoamesmaabordagemdocapítuloante-
rior,masdemodomaisconciso.
38

## Página 53

CasadoCódigo Capítulo5. SimplifiquecomjQuery
function calculateTotalProducts() {
var produtos = $(".produto");
var total = 0 ;
for(var pos = 0 ; pos < produtos.length; pos ++) {
var $produto = $(produtos[pos]);
var quantity = moneyTextToFloat(
$produto.find(".quantity").val());
var price = moneyTextToFloat(
$produto.find(".price").text());
total += quantity * price;
}
return total;
}
Comparecomocódigoquetínhamosanteriormenteesurpreenda-se.
Boas práticas e convenções com j Query
Àsvezespodeficarcomplicadodescobrirqualvariáveléumelemento
DOMequaléumelementojQuery. Apesardenãoserumaconven-
çãoaceitaportododesenvolvedor,algumaspessoasindicamusaro $na
frentedavariávelquefordojQuery.Nessecasonossocódigoficaria var
$produto = $(produtos[pos]); .Dessaforma,todavezquevocêlesse
nocódigo $produto,saberiaquesetratadeumelementojQuery.
Hámaissugestõesdeconven çõesaqui:http://www.jameswiseman.com/
blog/2010/04/20/jquery-standards-and-best-practice/
E aqui um argumento contra essa prática: http://bears-eat-beets.
blogspot.com.br/2011/08/jquery-naming-conventions-dont-prefix.html
Nósusaremosoprefixo $nolivroparaauxiliaroleitoraentendermelhor
ocódigo,masfiqueavontadeparadecidiroqueformelhorparavocêou
parasuaequipe.
39

## Página 54

5.4. Programandodeformafuncional CasadoCódigo
5.4 Programando de forma funcional
Apesardonosso forresolverbemoproblema,ébastantecomumumdesenvolvedor
jQueryutilizarumaabordagemumpoucomaisfuncional. Emvezdefazeruma
iteraçãoporumloop,vamospassarumafun çãocomoargumentoparaalguémque
aexecutaráparacadaumdositens.Essaéafun ção each:
function calculateTotalProducts() {
var produtos = $(".produto");
var total = 0 ;
$(produtos).each(function(pos, produto) {
var $produto = $(produto);
var quantity = moneyTextToFloat(
$produto.find(".quantity").val());
var price = moneyTextToFloat(
$produto.find(".price").text());
total += quantity * price;
});
return total;
}
Essa function()quepassamoscomoargumentoparao eachseráinvocadapara
cadaumdosnossositensdocarrinho. Vocêjádeveestarcansadodesaber,masé
muitocomumpassarfun çõescomoargumentoparaoutrasfun ções.Fazemosissoo
tempotodo,emespecialcomos callbacks(exemplo:clicouemumbotãodeexcluir
produto,chameafun ção compraAtualizada()).Onometécnicodissoatéassusta,
sãoaschamadas highorderfunctions.
Mascomosaberoqueafun ção eachrecebecomoargumento?Assimcomoo
JavaScriptpossuiumaexcelentedocumenta çãonositedaMozilla,ojQuerytemsua
própriadocumentação!Repare:
http://api.jquery.com/each/
40

## Página 55

CasadoCódigo Capítulo5. SimplifiquecomjQuery
Figura5.7:Documenta çãodoeachdeumselectorjQuery
Éaíquevocêficasabendoqueo eachrecebeumafun ção.Alémdisso,essafun-
çãoreceberácomoparâmetroum indexeum Element,querepresentam,respec-
tivamente,aposi çãoqueoelementoocupaeoelementoemsi. Nonossocaso,o
Elementéoprodutoatualdaitera ção.
NavegadoresquesuportamopadrãoECMAScriptmaismodernojápermitem
quevocêchameafun ção eachemumaarray,alémdeimplementaremdiversasou-
trasinteressantesfuncionalidades. Mas,comojáaprendemos,diversosnavegado-
resaindanãopossuemessesrecursosmaisrecenteseporissoaindaéinteressante
utilizá-losatravésdeumabibliotecacomoojQuery.
5.5 Eventos e callbacks
Assimcomoacontececomamanipula çãodoDOM,ojQuerytambémnosauxilia
notratamentodeeventos.Recebemosaschamadasinformandodesseseventosem
callbacks,atravésdefun çõesquesãopassadascomoparâmetro.
Oprimeiropontoquevamosnotardediferenteéquenãoprecisamosdefinir
oseventosdecadaumdoselementos,comofizemosusandoJavaScriptpuro.Basta
selecionarmosaclassequequeremoseojQueryseencarregadedefiniroevento
paratodososelementosqueforemencontrados.
Paradefinirmosque,cadavezqueumcampodaclasse quantityforalterado,o
totaldocarrinhosejarecalculado,nósvamospassarumafun çãocomoparâmetro
paraométodo change.Todavezqueocampoforalterado,essafun çãoseráexecu-
tadaeototaldonossocarrinhoserárecalculado.
41

## Página 56

5.5. Eventosecallbacks CasadoCódigo
$(".quantity").change(function() {
writeTotal(calculateTotalProducts());
});
Compareissocomaversãoanteriordocódigo!olhesó:
function onDocumentLoad() {
var textEdits = document.getElementsByClassName("quantity");
for(var i = 0 ; i < texts.length; i ++) {
textEdits[i].onchange = function() {
writeTotal(calculateTotalProducts());
};
}
}
AversãodojQueryésemdúvidamaissucintaeatémaisfácildeler.Semcontar
avantagemdetrabalhardamesmaformaemdiferentesnavegadores.
Agora,paradefinirmosesseeventoassimqueodocumentoterminardesercar-
regado,vamosusaroutrafuncionalidademuitoimportantedojQuery.
OjQuerytemumeventochamado ready,queéexecutadoassimqueodocu-
mentoterminardesercarregado.Ofuncionamentoéigualaqualqueroutroevento:
passamosumafun çãocomoparâmetro,queseráexecutadaassimqueoeventofor
disparado.
Nossocódigoentãoficariaassim:
jQuery(document).ready(function() {
// faça alguma coisa
});
Porém,vocêdeveselembrarqueeudisseque jQuerye $sãoequivalentes.Então
podemossubstituirumpelooutro,deixandoocódigoaindamenor:
$(document).ready(function() {
// faça alguma coisa
});
Comoseissonãobastasse,osdesenvolvedoresdojQueryforampregui çososo
bastanteparadeixaressaexpressãomenorainda. Vocêpodesimplesmenteomitir
o ready,passandoumafun çãocomoparâmetrodiretamenteparao $. Comisso,
usandoanossadeclara çãodeeventoládecima,nossocódigofinalmentevaificar
comessacara:
42

## Página 57

CasadoCódigo Capítulo5. SimplifiquecomjQuery
$(function() {
$(".quantity").change(function() {
writeTotal(calculateTotalProducts());
});
});
Epronto!Temosonossocarrinhodecomprasfuncionandoemtodososnave-
gadoresmodernosusandomuitomenoscódigo.Claro,seseucódigoaídentrofor
grande,eramelhorquebraremumafun çãoquetenhaumnomeexpressivo.
5.6 E o que vem agora?
OquevimosatéagoraserviuparanosmostrarasvantagensdojQueryeoquantoele
agilizarodesenvolvimentodonossocódigo,masaindanãoéobastante.Nospró-
ximoscapítulosvamosvercomomanipularoDOM,comocalcularofreteusando
AJAXecomoadicionarefeitosvisuaisinteressantesnonossocarrinhodecompras.
Omelhordetudoéquevocêpodeficartranquiloqueissovairodaremqualquer
browsermoderno.
43

## Página 59

Capítulo6
Dominandoeventosemanipula ção
deDOMcomjQuery
6.1 Criando uma lista de tarefas
ParaaprendermosmaisafundocomomanipularoDOMusandojQuery,vamos
desenvolverumaaplica çãoquegerencienossastarefascotidianas.
Relembroquevocêpodeencontrarocódigodessecapítuloedeoutrosnorepo-
sitóriodolivro:
https://github.com/pbalduino/livro-js-jquery/tree/master/capitulo_06
Masescreverdozerosempreagregamaisaoaprendizado,refor çandoalguns
conceitosjávistosnaprática.
Anossaaplica çãovaiterumacaixadetextoondepodemosdigitarumanova
tarefaelogoabaixoalistadetarefasquejáincluímos.Aideiaétermosainterface
maislimpaesimplespossívelparafocarmosnocódigoquevamosescrever.

## Página 60

6.1. Criandoumalistadetarefas CasadoCódigo
Figura6.1:Acaradanossalistadetarefas
OcódigoHTMLdanossalistateráumelemento inputcomid tarefa,queva-
mosusarparainserirastarefaseteremosumelemento divcomid tarefa-lista,
quevaicontertodosastarefas.
Cada tarefa vai ficar dentro de um outro elementodiv que terá a classe
tarefa-item,queterámaistrêselementos div: umquecontémadescri çãoda
tarefa,queteráaclasse tarefa-texto;outroelemento divqueserviráparaexcluir
atarefaquandoforclicado,quevaiteraclasse tarefa-delete;porfim,apenaspara
finsdeformata ção,teremosumterceiroelemento divqueconteráaclasse clear.
Listagem6.1:
<h2>TODO List </h2>
<input type="text" id="tarefa">
<div id="tarefa-lista">
<div class="tarefa-item">
<div class="tarefa-texto">Comprar pão </div>
<div class="tarefa-delete"></div>
<div class="clear"></div>
</div>
</div>
Comesseselementosdefinidos,conformeocódigo1,vamoscome çaradesen-
volvernossalistadetarefas.
46

## Página 61

CasadoCódigo Capítulo6. Dominandoeventosemanipula çãodeDOMcomjQuery
6.2 Usando eventos de um jeito mais profissional
Paraadicionarnovastarefas,ousuárioprecisadigitarumtextoepressionar ENTER.
Paraquepossamosdetectarousodessatecla,vamosusaroevento keydown.
Notequeessemétodorecebeumobjetocontendoasinforma çõesdoevento.Isso
vaisermuitoútilparadescobrirmosqueteclaestásendopressionada. Esseobjeto
temumapropriedade which,queretornaocódigoUnicodedateclausada.
Vamosbrincarumpoucocomesseeventoparavercomoelesecomporta.Você
podefazeressestestesdiretonoconsoledoseunavegador:
$('#tarefa').keydown(function(event) {
console.log(event.which, String.fromCharCode(event.which));
});
Aoescrevermos eventoepressionarENTER,veremosasaídadafigura6.2. O
métodoString.fromCharCode,quandopossível,converteocódigodateclapressi-
onada,queéumnúmero,paraorespectivocaractere,tornandoonossoexemplo
maislegível.
Figura6.2:Keydown
O event.whichdasletraséorespectivocódigo Unicode[14],masnoENTER
recebemosovalor 13.Sabendodisso,vamosfazeronossoexemplotrabalharapenas
quandofordetectadoqueousuáriopressionouessatecla,digitandoocódigoabaixo
noconsoledobrowser.
Listagem6.2:
$('#tarefa').keydown(function(event) {
if(event.which === 13 ) {
47

## Página 62

6.2. Usandoeventosdeumjeitomaisprofissional CasadoCódigo
console.log("Aqui vamos adicionar nossa tarefa" );
}
}
Digitandoomesmotexto“evento”epressionandoENTER,teremosasaída
abaixo:
Figura6.3:Keydowncomdoiseventos
Masnãoestávamosesperandoque,aodispararoevento,ojQueryexecutasse
asduasfun çõesqueescrevemos.Issopermitequevocêatribuafun çõesdecallback
diferentesparaomesmoeventosemqueumasobrescrevaaoutra. Imaginecomo
seriaruimsevocêdefinisseumafun çãoparaesseevento keydowne,nasequênciaum
códigofeitoporoutrapessoasimplesmenteapagasseoquevocêfezparaexecutaro
códigodele.
Casovocêqueiraremoverasfun çõesqueestãoassociadasaumevento,você
deveusarusarométodo off,passandoonomedoeventocomoparâmetro. Você
podeusar $("#tarefa").off("keydown");nessecaso.Hátambémafun ção off,
maisrecente,recomendadaaserusadaapartirdojQuery1.7.
Seexecutarmosnovamenteocódigodalistagem3,veremosasaídaexibidana
figura6.4
Listagem6.3:
$('#tarefa').off();
$('#tarefa').keydown(function(event) {
if(event.which === 13 ) {
48

## Página 63

CasadoCódigo Capítulo6. Dominandoeventosemanipula çãodeDOMcomjQuery
console.log("Aqui vamos adicionar nossa tarefa" );
}
}
Figura6.4:Keydownnovamentecomumevento
6.3 Desassociando eventos
Podeacontecerdeumcódigodeterceirosatribuirumeventoparaumelementoe
vocêprecisaratribuiroseuprópriocódigoparaomesmoeventodomesmoele-
mento.Comojávimos,ojQueryvaiexecutarosdoisemsequência,semproblema
algum.
Asituaçãocome çaaficarruimquandovocê,ouocódigodeterceiros,precisa
removersomenteumdoscódigosdoevento.Comofazerisso?
Vamosvernapráticacomofunciona,usandoomesmocódigoHTMLquejá
temospronto.Paraisso,atualizesuapáginapressionando F5ou Command R evamos
usarnovamenteoconsoledojQuery:
$("#tarefa").keydown(function() {
console.log("Esse é o primeiro evento" );
});
$("#tarefa").keydown(function() {
console.log("Esse é o segundo evento" );
});
Aopressionaralgumacoisatecla,veremosasduasmensagensexibidasnafigura
6.5.
Figura6.5:Eventosencadeados
49

## Página 64

6.3. Desassociandoeventos CasadoCódigo
Seusarmoso off,tantooprimeiroquantoosegundoeventoserãoeliminados.
Pararesolvermosissousamosalgochamado namespaces.
Parautilizaro namespaceemumevento,vamosutilizarométodo on,informar
oeventoquequeremosdeclarareonomedo namespace,separadosporponto,e
tambémafunçãoaserexecutadaquandooeventofordisparado.
Aproveitandooexemploqueusamosanteriormente,atualizenovamenteajanela
doseubrowserevamosdigitarocódigoabaixonoconsole:
$("#tarefa").on("keydown.primeiro", function() {
console.log("Esse é o primeiro evento" );
});
$("#tarefa").on("keydown.segundo", function() {
console.log("Esse é o segundo evento" );
});
bind e unbind
SevocêjáutilizoueventoscomjQuery,ouencontroualgumcódigoque
faziaisso,devetervistoosmétodos binde unbind.
Apartirdaversão1.7dojQuery,érecomendadoquevocêuse onnolugar
de binde offnolugarde unbinde,comocostumaacontecer,emalgum
momentonofuturoosmétodosantigosserãoremovidosdabiblioteca.
Asintaxede one offétotalmentecompatívelcom binde unbind,oque
facilitamuitoaatualiza çãodocódigo.
Aopressionarmosqualquertecla,veremosexatamenteamesmasaídadoexem-
ploanterior,masadiferen çaéqueagorapodemosdesassociarsomenteumdoseven-
tos,conformeoexemploaseguir:
$("#tarefa").off("keydown.primeiro");
Agora,aopressionaralgumatecla,vamosverapenasamensagemdosegundo
evento,conformeafigura6.6. Dessaforma,vocêpodeassociaredesassociarseus
eventosconformeanecessidadesemsepreocuparemquebrarocódigodeterceiros.
50

## Página 65

CasadoCódigo Capítulo6. Dominandoeventosemanipula çãodeDOMcomjQuery
Figura6.6:Primeiroeventoremovido
6.4 R emovendo itens com estilo
Apesardeparecerqueestamoscome çandodofinal,ocódigoqueremoveumitemda
nossalistadetarefaséomaissimples,eaindaporcimausatudooqueaprendemos
sobreassociaçãoedesassocia çãodeeventos.
Dentrodonossoprojeto,vamoscriarumdiretóriochamado javascriptse,
dentrodele,umarquivocomonomede todo.js.Vamosusaressenomedearquivo
pelofatodonossoprojetoteroriginalmenteonomedeTODOList,oulistadecoisas
afazereminglês.Nãoexisteumapadroniza çãoformalparanomesdearquivosJa-
vaScript,entãosinta-seavontadeparausaraquelequedescrevermelhoropropósito
doseucódigoouprojeto.
Ocomeçovocêjáconhece.Vamosusaraquelemétodo $(document).ready()
paraassociarmostodasoseventosnecessáriosassimqueodocumentoestivercarre-
gado.
Dentrodessemétodo,vamosassociaralgumcódigoaoevento clickdaquele
elemento divquevaiexibiroíconedalixeira.
$(function() {
function onTarefaDeleteClick() {
console.log("Adeus mundo cruel!" );
}
$(".tarefa-delete").click(onTarefaDeleteClick);
}
Aquivocêpodeperceberquecriamosumafun çãonomeadaparaatribuirao
evento click.Eupoderiamuitobemterutilizadoumafun çãoanônimamas,con-
formeonossocódigoforcrescendo,vaificarpraticamenteimpossívelnosencon-
trarmosdentrodefun çõesanônimasdeclaradasdentrodefun çõesanônimas.
Aessabagun çageneralizadaosdesenvolvedoresderamonomede Callback
hell[15]ou,numatradu çãolivre, oinfernodoscallbacks . Vocêpodeacessarolink
abaixoparaentenderoqueéo Callbackhell ecomofugirdele:
51

## Página 66

6.4. Removendoitenscomestilo CasadoCódigo
http://callbackhell.com/
Outropontoquevocêdeveterpercebidoéonomequedeiparaafun çãoque
seráexecutadaquandooevento clickfordisparado.Nãoexisteumpadrãooficial
paranomearfun çõesnojQuery,masconformemefoiditopelaprópriaequipede
desenvolvimentodabiblioteca, adoteumpadrãoesiga-oatéofim .
Opadrãoadotadonesselivroparanomearfun çõesqueserãoassociadasaeven-
tos,osnossosjáconhecidoscallbacks,é:
on<identificadordoelemento><nomedoevento>
Nocasodocódigoacima,oelementousaaclasse tarefa-deleteparaserse-
lecionado,entãovamosconverteressenomeparaopadrãoJavaScript,queéusar
aprimeiraletradapalavraemmaiúsculaeasdemaisemminúsculas,eelepas-
sará a serTarefaDelete. On o m ed oe v e n t oéclick, portanto vamos mudar
aprimeiraletraparamaiúsculaeusaremos Click. Juntandotudoissoteremos
onTarefaDeleteClick.
Dessaforma,aoleronomedafun ção,vocêautomaticamentevaisaberdoque
setrataeparaqueelaserve.
Quandovocêclicanoíconedalixeira,vocêquerquealinhatodasejaexcluída,e
nãoapenasoícone.Paraisso,precisamosencontrarumaformadeselecionaroitem
datarefaquecontémaquelalixeira.Paraessatarefa,usaremosométodo parent,que
retornao elementopai,ouseja,oprimeiroelementoqueestivercontendoonosso
elementoatualequerespeiteasregrasdoseletorqueutilizarmos.
Olhandooexemplovemosqueébemmaissimplesdoqueparece:
function onTarefaDeleteClick() {
console.log($(this).parent('.tarefa-item').text().trim());
}
Everemosotextoqueestácontidonanossatarefa,indicandoqueselecionamos
todaalinha. O trimnofinaldasenten çaestáaliapenasparaeliminarosespa ços
embranconocome çoenofimdotexto,tornandoaexibi çãomaislegível,como
podemosvernafigura6.7.
Figura6.7:Comprarpão.Boaideia.
52

## Página 67

CasadoCódigo Capítulo6. Dominandoeventosemanipula çãodeDOMcomjQuery
Vamosusarométodo hideparaesconderoelemento. Essemétodoesconde,
masnãoexcluioelementodoDOM.
function onTarefaDeleteClick() {
$(this).parent('.tarefa-item').hide();
}
Oproblemaaquiéqueoitemsumiuderepente,maselecontinuafazendoparte
doDOM.Usarométodo removeteriaomesmoefeitovisualeaindaporcimaelimi-
nariaoelementodeumavez.Avantagemdo hideéquepodemosadicionarefeitos
paraquandoclicarmosnoíconedalixeira.Parafazermoscomqueaelimina çãoda
tarefasejafeitaemcâmeralenta,vamospassaroparâmetro 'slow'paraométodo
hide.
function onTarefaDeleteClick() {
$(this).parent('.tarefa-item')
.hide('slow');
}
Agoravamosclicarnoíconedalixeiraeapreciaraanima çãodoitemsendoeli-
minadodanossalista.
Ométodo hidepermitequeumsegundoargumentosejapassado. Eleéuma
funçãoqueseráexecutadaassimqueaanima çãoterminar,umcallback. Vamos
aproveitarissoepassarumafun çãoqueeliminadevezoitemdatarefadedentro
doDOM:
function onTarefaDeleteClick() {
$(this).parent('.tarefa-item')
.hide('slow', function() {
$(this).remove();
});
}
Mas,umavezqueeunãovejomaisatarefanatela,precisomesmoapagá-lo
doDOM?EuinsistotantonessaquestãodeeliminarmosoelementodoDOMpelo
simplesfatodeque,comotempo,onossoDOMvaificarabarrotadodeelementos
quenãoservemparamaisnada,ocupandocadavezmaismemóriaedeixandonosso
códigomaislento. Eliminandooquenuncamaisvaiserusadoéumaformade
mantermosacasalimpaeoconsumodememóriasemprebaixo.
53

## Página 68

6.5. Editandoitens CasadoCódigo
Muita atenção ao usar o this
Nonossocódigo,percebaqueusamoso thisduasvezes,masemcada
umadelasestávamosfalandodeelementosdiferentes. O thiséuma
palavrareservadaqueindicaqualelementosestamosmanipulandono
momento.
Noprimeiro thisestamostratandoumeventodoíconedalixeira,então
eleestásereferindoaoelemento divquetemaclasse tarefa-delete.
Jánosegundoitemestamostratandoumeventodoitemdalistade
tarefas,entãoestamosnosreferindoaoelementoquecontémaclasse
tarefa-item.
Omodocomoo thisfuncionaéumadaspartesconfusasdoJavaScript
mas,prestandoaten çãoaocódigoeentendendocomofuncionaessapa-
lavrachave,podemosevitarmuitadordecabe çanofuturo.
6.5 Editando itens
Paraeditarumatarefaqueremosquesejasuficienteclicaremcimadoitem.Aoclicar,
devemosfazercomqueapare çaumacaixadetextoondeousuáriopodealteraro
conteúdo,pressionandoENTERemseguidaparagravaronovotexto.
Vamoscomeçardeclarandooeventodentrodométodo $(document).ready
e, seguindo o padrão que explicamos, criaremos uma função chamada
onTarefaItemClick para ser executada quando o eventoclick for disparado
poralgumelementodaclasse tarefa-item:
$(function() {
function onTarefaItemClick() {
console.log("Aqui vamos editar a tarefa" );
}
$(".tarefa-item").click(onTarefaItemClick);
});
Vamosguardarotextodatarefanumavariávelpara,emseguida,criarmosum
campodetextochamado tarefa-editparaeditá-lo.Notecomoalteramosocon-
teúdodanossatarefasubstituindoocódigoHTMLqueficadentrodoelemento.Para
54

## Página 69

CasadoCódigo Capítulo6. Dominandoeventosemanipula çãodeDOMcomjQuery
issonósmontamosoHTMLdentrodeumavariávelesubstituímosoconteúdoda
nossatarefausandoométodo html.
function onTarefaItemClick() {
var text = $(this).children('.tarefa-texto').text();
var html = "<input type= 'text' " +
"class='tarefa-edit' value='" +
text + "'>";
$(this).html(html);
$(".tarefa-edit").keydown(onTarefaEditKeydown);
}
Precisamos também criar uma fun ção, que vamos chamar de
onTarefaEditKeydownparasalvaraaltera çãodatarefaquandoousuáriopressionar
ENTER.
function onTarefaEditKeydown(event) {
if(event.which === 13 ) {
savePendingEdition($(this));
}
}
Vamoscriartambémumafun çãochamada savePendingTarefa,quevaiseen-
carregardesalvarnalistaotextodatarefaqueestamoseditando.
function savePendingEdition(tarefa) {
console.log("E aqui vamos salvar nossa tarefa" );
}
Notequeprecisamosdeclararoseventosdoselementosrecém-criados. Isso
aconteceporqueaquelenossocódigoqueéexecutadono jQuery(document).ready
édisparadoapenasumavez,quandoobrowserterminadecarregarodocumento.
Apósisso,todaaltera çãoqueprecisarmosfazernoDOMdeveserseguidadares-
pectivadeclaraçãodeeventos.
6.6 E ditando apenas um item de cada vez
Agoravamostestarclicandonatarefaeveremosumacaixadetextocomelaládentro,
prontaparaseralterada.
55

## Página 70

6.6. Editandoapenasumitemdecadavez CasadoCódigo
Masfaçaoseguinteteste:cliqueumavezdentrodessacaixadetextoevocêvai
verqueoconteúdodanossatarefadesaparece.Temosumproblema!
Issoaconteceporque,aoclicarnatarefaasereditada,vocêacabadisparando
novamenteumachamadaàfun ção onTarefaItemClick.Dessavezelanãovaien-
contrarnenhumelementocomaclasse tarefa-textodentrodaqueleitem,evai
entenderqueotextodasuatarefaestávazio.Nasequênciaserácriadanumanova
caixadetextocomotextovazioevocêacaboudeperderoconteúdoantigodasua
tarefa!
Oquefazer?
Primeiro,precisamossabersejáestamoseditandoounãoumatarefa. Vamos
criarumavariável $lastClickedparaarmazenaratarefaqueestamoseditando.Se
atarefaqueclicarmosforamesmaquejáestamosalterando,vamosignoraroclique.
Seclicarmosemoutratarefa,aqueestásendoeditadadevesersalvaeaoutradeve
serabertaparaaltera ção.
Dessaformateremoscertezadequesomenteumatarefaseráeditadaporvez,e
dequenãovamosperderoqueestamosescrevendoporcausadeumerrosimples.
$(function() {
var $lastClicked;
// aqui continua todo o código que já escrevemos
});
Dentrodafun ção onTarefaItemClick,vamosverificarseoitemasereditado
agoraéomesmoquejáestamoseditando,ouseéalgumitemnovo.OjQuerynos
ofereceométodo isparaverificarmosseoelementoéomesmo.Casoseja,simples-
mentevamosignoraroeventoeagircomosenadativesseacontecido.
Temosqueverificartambémseavariável $lastClickedéundefined. Nesse
caso,nãoestamosalterandonenhumatarefaaoentrarnessafun çãoenãoprecisamos
nospreocuparemsalvarnada.
function onTarefaItemClick() {
if(!$(this).is($lastClicked)) {
if($lastClicked !== undefined) {
savePendingEdition($lastClicked);
}
$lastClicked = $(this);
56

## Página 71

CasadoCódigo Capítulo6. Dominandoeventosemanipula çãodeDOMcomjQuery
Nofinaldafun ção,vamosusaromesmocódigoquejátínhamosantes,mas
alterandoo $(this)para $lastClickedque,aessaalturadocódigo,significarãoa
mesmacoisa.
// continuando onTarefaItemClick
var text = $lastClicked.children('.tarefa-texto').text();
var html = "<input type= 'text' class='tarefa-edit' value='" +
text + "'>";
$lastClicked.html(content);
$(".tarefa-edit").keydown(onTarefaEditKeydown);
}
}
Agora que criamos essa variável$lastClicked, precisamos alterar também
aquelafunção onTarefaEditKeydown,paracontinuarmosgravandootextodata-
refacorreta
function onTarefaEditKeydown(event) {
if(event.which === 13 ) {
savePendingEdition($lastClicked);
$lastClicked = undefined;
}
}
Agorasimficoubonito. Maslembradoeventoqueadicionamosparaexcluir
umatarefa?
6.7 Disparando mais de um evento ao mesmo tempo
Comooíconedalixeirafica dentrodonossoitemdalistadetarefas,aoclicarmosali
dispararemosdoiseventos,o clickdoelementoquecontémaclasse tarefa-delete
etambémo clickdoelemento tarefa-item,queacabamosdedesenvolver.
Oproblemaéque,enquantoexecutamosaqueleefeitobacanaaoexcluiruma
tarefa,nóstambémvamosverumacaixadetextosendocriada,comoseestivéssemos
editandoatarefa.Nasequênciaatarefadesaparecee,comela,acaixadetexto.Nada
queatrapalheanossavida,masconvenhamosqueoefeitoficabemfeio.
57

## Página 72

6.8. Salvandoatarefa CasadoCódigo
Resolverissonãotemsegredo.Primeiro,precisamosdesassociartodososeven-
tos clickdoelementocomaclasse tarefa-item. Comojávimos,nóspodemos
resolverissousandoométodo off.Usandotambémaboapráticadoencadeamento
demétodos,nossocódigovaificarcomessacara:
function onTarefaDeleteClick() {
$(this).parent('.tarefa-item')
.off('click')
.hide('slow', function() {
$(this).remove();
});
}
6.8 Salv ando a tarefa
Ficoufaltandoescrevermosafun çãoquesalvaatarefaqueestásendoeditada.Nos
códigosacima,simplesmentemandamosexibirumamensagemnoconsole.
Salvaratarefasignificaquevamospegaroquefoiescritonacaixadetextoe
vamosmontarumitemdalistadetarefas,comapossibilidadedepermitiraedi ção
quandoousuárioclicarnotextoetambémquesejaexcluídoquandoousuárioclicar
noíconedalixeira.
Vamoscomeçarguardandootextoemumavariávelchamada text.Emseguida
vamoseliminartodoocódigoHTMLqueestádentrodoelemento divquecontém
oitemdatarefausandoométodo empty.
function savePendingEdition($tarefa) {
var text = $tarefa.children('.tarefa-edit').val();
$tarefa.empty();
Vamosadicionaraquelestrêselementos divqueforamexplicadoslánoinício
docapítulo:umquevaiconterotextodatarefa,umquevaiexibiroíconedalixeira
eumqueserveapenasparalimparaformata çãodoCSSedeixaroscomponentes
alinhadosnatela.
Paraadicionaroselementos,vamosusarométodo append,queadicionacon-
teúdoaoHTMLdoelemento.
Porexemplo,ocódigo $("<b></b>").append("bacana")vairetornaroHTML
<b>bacana</b>.
//
$tarefa.append("<div class= 'tarefa-texto'>" + text + "</div>")
58

## Página 73

CasadoCódigo Capítulo6. Dominandoeventosemanipula çãodeDOMcomjQuery
.append("<div class= 'tarefa-delete'></div>")
.append("<div class= 'clear'></div>");
E,finalmente,vamosdeclararoseventosparaoelementosrecémcriados,fa-
zendocomqueatarefasejaeditadaaoserclicada,ouexcluídaquandoousuário
clicarnoíconedalixeira.
//
$(".tarefa-delete").click(onTarefaDeleteClick);
$tarefa.click(onTarefaItemClick);
}
Agoraanossalistadetarefaspermiteedi çãodeumitemporvezeexclusãocom
umefeitobatuta.Certamenteprecisaríamosdepoisenviaressasinforma çõesparao
servidor,porexemploatravésdeAJAX.Veremoscomotrabalharcomoservidorem
breve,usandoasfacilidadesdojQuery.
Precisamosfinalizaronossodesenvolvimentopermitindoainclusãodetarefas.
6.9 I ndo ainda mais fundo na manipulação de DOM
Vamosaproveitarocódigoqueutilizamosparaadicionaroselementos divnonosso
itemdetarefasparaensinarmaismaneirasdemanipularoDOMusandojQuery.
Listagem6.4:
$tarefa.append("<div class= 'tarefa-texto'>" + text + "</div>")
.append("<div class= 'tarefa-delete'></div>")
.append("<div class= 'clear'></div>");
Nãoestamosdizendoaquiqueéumaboaprática,queémaisrápidoouqueseja
maissimplesdeler,apesardeeuacharqueémaislegível,maséinteressantequevocê
conheçanapráticamaisformasdeutilizarojQuery.E,nofinaldascontas,quanto
maispretextosparaquevocêaprenda,melhor.
OjQuerypermitequevocêmanipuleumelementodoDOMsimplesmentepas-
sandoocódigoHTMLcomoparâmetroparaafun ção $().Vamosusarumelemento
divparatestar. Notequetantofazescrevermos <div /> ou <div></div>. Vamos
executaroexemploaseguirnoconsole.
59

## Página 74

6.10. Adicionandotarefas CasadoCódigo
Vamosusarométodo addClassparaadicionarumaclasse CSSaonossoele-
mentoHTMLeojáconhecidométodo textparaadicionarmosumtextonesse
mesmoelemento.
$("<div />" )
.addClass("tarefa-texto")
.text("Lavar o banheiro" );
PodemosverocódigoHTMLquefoigeradonafigura6.8.
Figura6.8:Lavarobanheiro.=(
Extrapolando esse exemplo de volta para o nosso código da função
savePendingEdition, podemos reescrevê-lo da seguinte forma, adicionando
oqueaprendemosaquiaoobjeto $tarefas,querecebemosporparâmetro:
$tarefa.append($("<div />" )
.addClass("tarefa-texto")
.text("Lavar o banheiro" ))
.append($("<div />" )
.addClass("tarefa-delete"))
.append($("<div />" )
.addClass("clear"));
6.10 Adicionando tarefas
Paraadicionarumatarefa,ousuáriodigitaalgonumacaixadetextoquetemoID
tarefaepressionaENTER.Emseguidaadicionamosnalistaumatarefacomotexto
quefoidigitadoeacaixadetextovoltaaficarembranco.
Usandooquejáaprendemossobrecomocapturaratecla ENTER,vamosterum
códigocomoesse:
function onTarefaKeydown(event) {
if(event.which === 13 ) {
60

## Página 75

CasadoCódigo Capítulo6. Dominandoeventosemanipula çãodeDOMcomjQuery
addTarefa($("#tarefa").val());
$("#tarefa").val("");
}
}
Notequejogamosotrabalhopesadoparaumafun ção addTarefa.Nessafun ção
nósvamoscriarumelemento divcomaclasse tarefa-item,eemseguidaadicionar
aquelestrêselementosdivquejáapresentamos:umquecontémotexto,outropara
oíconedalixeiraeumterceiroqueexisteapenasparafinsdeformata ção.
Porumaquestãodelegibilidade,eparausaroquejáaprendemos,vamosescre-
verocódigoHTMLusandooconteúdodase çãoanterior.Aoterminarmosdegerar
oselementosdanossatarefa,vamosadicioná-loaoelementoquerepresentaalista
detarefas,quevaiteraclasse tarefa-lista.
Finalmente,vamosadicionaroseventosparaquandoousuárioclicarnoícone
dalixeiraeparaquandoousuárioclicarnatarefaparaeditá-la.
function addTarefa(text) {
var $tarefa = $("<div />" )
.addClass("tarefa-item")
.append($("<div />" )
.addClass("tarefa-texto")
.text(text))
.append($("<div />" )
.addClass("tarefa-delete"))
.append($("<div />" )
.addClass("clear"));
$("#tarefa-list").append($tarefa);
$(".tarefa-delete").click(onTarefaDeleteClick);
$(".tarefa-item").click(onTarefaItemClick);
}
Casovocêtenhaachadoconfuso,vocêpodeusaraformatradicional,queécriar
umavariávelcontendotodooHTMLedepoisinserirdeumavezsóusandoomé-
todo append.Euachoessasegundaformamaisbagun çada,masfiqueavontadepara
usaraformaquevocêacharmaisexpressivaefácildeentender.
Comaformatradicionalficariaassim:
61

## Página 76

6.10. Adicionandotarefas CasadoCódigo
function addTarefa(text) {
var tarefa = '<div class="tarefa-item"> '
+ '<div class="tarefa-texto"> ' + text + '</div>'
+ '<div class="tarefa-delete"></div> '
+ '<div class="clear"></div> '
+ '</div>';
$("#tarefa-list").append(tarefa);
$(".tarefa-delete").click(onTarefaDeleteClick);
$(".tarefa-item").click(onTarefaItemClick);
}
Noteque,nasegundaforma,euchameiavariávelde tarefaaoinvésde $tarefa,
poisestamoslidandocom String,enãocomumobjetojQuery.
Agora,depoisdetodoonossoesfor ço,temosumalistadetarefastotalmente
funcional.Umademonstra çãodocódigoapresentadoestánoendere çoabaixo:
http://jsfiddle.net/pbalduino/faWn4/
Nopróximocapítulovamosaprenderanoscomunicarcomoservidorsemque
sejanecessáriorecarregarapágina. Assimpoderemosnãosóenviarinforma ções
sobreoqueestamosfazendo,comotambémpoderemosreceberdadosdoservidor
eatualizaranossapáginademodorápidoeagradávelaousuário.
62

## Página 77

Capítulo7
NãotenhamedodoAJAXedo
JSON
“AJAXnãoéumatecnologia,massimumconjuntoformadoporváriastecnologias,
cadaumasedesenvolvendoporcontaprópria,sejuntandodeformasnovase
poderosas.”
–JesseJamesGarrett
PormaisquejátenhamostrabalhadocomAJAXeJSON,semprehápontosa
conhecermelhor.
7.1 AJAX?Que bicho é esse?
Antigamente,cadavezquevocêquisesseatualizaralgumainforma çãonasuapágina,
pormenorquefosse,vocêprecisavaatualizartodaapágina.Istoé,cadacliquefaziao
navegadorcarregarumanovapáginainteiramente,carregandocabe çalhos,rodapés,
conteúdoemcomumeàsvezesatémesmoimagens,javascriptsecss.Umtrabalho

## Página 78

7.1. AJAX?Quebichoéesse? CasadoCódigo
desgastantetantoparaoclientequantoparaoservidor.Maisainda:ficanotável,para
ousuário,umacertalentidão.Ositeacaba“respondendo”nãomuitorapidamente.
Tudocomeçouamudarcom,quemdiria,olan çamentodoInternetExplorer5,
queimplementavaumobjetoActiveXchamado XMLHTTP.Apesardenãotercha-
madoaatençãonaépoca,esseobjetofoilogoimplementadonoMozilla(oantecessor
doFirefox),OperaeoutrosbrowsersatravésdoobjetoJavaScript XMLHttpRequest.
Porsuavez,eleapareceudessamesmaformanoInternetExplorer7[18].
Essetalobjeto XMLHttpRequestpermitequeseudocumentoHTMLacesseou-
traspáginasouarquivosporbaixodospanos,trazendoinforma çõesatualizadassem
anecessidadederecarregartodaumapágina.
Somandoissoàmanipula çãodeDOM,quejávimosnoscapítulosanteriores,
quepermitequepor çõesdodocumentosejamatualizadossemanecessidadedese
recarregarapágina,foicriadooqueconhecemospor AJAX.UtilizandoAJAX,pode-
mosfazeronossositetrabalhardamaneiraqueplanejamosnocapítulo2,quando
apresentamosográfico2.2derequisi çõesaoservidoreatualiza çõesnonavegador.
EssetermofoicunhadopeloespecialistaemexperiênciadeusuárioJesseJames
Garrett,em2005,emseuartigo Ajax:ANewApproachtoWebApplications [7].
Nesseartigo,JesseJames(que,segundoopróprio,nãotemqualquerrela çãocom
oladrãodebancosamericano[8])explicaqueAJAXnãoéuma,masumconjunto
detecnologiasqueincluemamanipula çãodoDOMeoacessoadadosdeummodo
transparenteparaousuário.
Atítulodecuriosidade,otermo AJAXéumacrônimopara AsynchronousJa-
vaScriptandXML ,apesardeatualmenteoXMLserpoucoutilizadoedequenão
háobrigatoriedadedequeoprocessosejaassíncrono.
64

## Página 79

CasadoCódigo Capítulo7. NãotenhamedodoAJAXedoJSON
Síncrono e assíncrono
ImaginequevocêlideraumaequipeepedeparaqueJoão,queéumde
seusprogramadores,corrijaumbugnosistema,avisandoassimqueter-
minaratarefa.
Enquantoeletrabalha,vocêestálivreparaparticipardeumareunião,
responderemails,telefonarparaalgunsfornecedores,sairparatomarum
caféedarbroncaemalgumoutromembrodaequipe.
Enquantoisso,vocêrecebeumemailenviadoporJoãoinformandoque
obugestácorrigido.Percebaquevocêdisparouumatarefaeficoulivre
parafazerváriasoutrascoisasenquantoelanãoestavapronta.
Comonãofoinecessárioficarparadoenquantoatarefaeraexecutada,
dizemosqueelaé assíncrona.
ImagineagoraquevocêpasseoutratarefaparaoJoãoetenhaqueficar
sentadoaoladodele,esperandoqueelasejaconcluída. Enquantoisso
vocênãopodefazermaisnadaatéqueJoãotermineoquefoipassado.
Dizemosentãoqueessatarefaé síncrona.
Normalmenteousodetarefasassíncronasfazcomqueasuaaplica ção
termineoconjuntodetarefasmaisrapidamente.
Poroutrolado,comolíderdaequipe,vocêpercebeuquenemsempreé
bomdeixarJoãotrabalhandosozinhoesemsupervisão.
IssotemalgoavercomatalWeb2.0?
Temsim.OtermoWeb2.0estavaligadoaousodediversaspráticasnaWeb,eo
AJAXeraumadessaspráticas.OtermoWeb2.0jáperdeuafor ça.Atémesmoasigla
AJAX,porserbasicamenteonipresentenasaplica çõeswebmodernas,fazmenos
barulho. Alémdisso,ébastanteraro,senãoimpossível,veralguémmanipulando
diretamenteoobjeto XMLHttpRequest,dadasuacomplexidadeeincompatibilidade
entrediferentesnavegadores.
ParaexecutarnossoscódigosJavaScriptsemprecisarinstalarouconfigurarum
servidor,vamosusarumsitechamadojsFiddle,quevamosexplicaraseguir.
65

## Página 80

7.2. UsandoojsFiddle CasadoCódigo
7.2 Usando o jsFiddle
O jsFiddleéumsitequenospermiteescrevercódigoJavaScript,HTMLeCSSna
mesmatela,executareveroresultadoimediatamente,semquehajanecessidadede
instalarmosnadanamáquina.
Paraexecutarosexemplosaseguir, selecioneaúltimaversãodisponíveldo
jQueryondeestáescrito ChooseFramework,conformeafigura7.1.
Figura7.1:Selecioneoframework
AinterfacedojsFiddle,conformepodemosvernafigura7.2écompostaporqua-
tropainéis:umaparavocêdigitarocódigo HTMLeoutraparaocódigo CSSnaparte
decima,umaparaoseucódigo JavaScripteoutraparaoresultadonapartede
baixo.Osquadrosvêmidentificadosevocênãovaiterproblemanenhumemselo-
calizar.Notopodatelaexisteumbotão Run,queserveparaexecutaroscódigosque
vocêinseriueexibiroresultado.
66

## Página 81

CasadoCódigo Capítulo7. NãotenhamedodoAJAXedoJSON
Figura7.2:InterfacedojsFiddle
Vamosescreverumcódigobemsimplesparaentendermosmelhorcomousara
ferramenta.
NopainelqueestiverescritoJavaScript,quecostumaseroprimeirodalinhade
baixo,escrevaocódigoabaixo.Emseguida,cliqueem Run,queéoprimeirobotão
notopodapágina.
alert("Olá jsFiddle!" );
Aoexecutarveremosamensagem,comonafigura7.3
Figura7.3:jsFiddleemfuncionamento
Experimentebrincarumpoucocomessaferramenta.Euaconsideromuitoútil
parademonstrarrecursosdoJavaScriptoumesmoreproduzirerrosdealgumabi-
bliotecaquevocêestejausando.
67

## Página 82

7.3. NossoprimeirocódigocomAJAX CasadoCódigo
7.3 Nosso primeiro código com AJAX
Comojádissemos,apesardoXdoAJAXsignificarXML,oretornodoservidorpode
serqualquerinforma ção,mesmoemformatextopuro.
Vamosaprenderaexecutaraformamaissimplesderequisi çãoAJAXusando
jQuery.Primeiro,vamosacessaroendere çoabaixo:
http://livro-capitulo07.herokuapp.com/hello
Evamosverasaídadafigura7.4.Podemosverquearespostaéumtextosimples,
semformataçãonemnadadeespecial.
Figura7.4:Olá!
VamosfazercomquenossocódigocarregueessetextousandoAJAXeoexiba
nanossatela.
OjQuerynosdisponibilizaummétodo get,queaceitaatétrêsparâmetros.
Oprimeirocontéma URL,oendere çodositequevamosacessarparapegaros
dados. Apáginaquenosforneceasinforma çõesparaseremusadascomAJAXé
chamadaserviço.
Osegundoparâmetro,opcional,éondevocêinformaosparâmetrosaserem
passadosparaoservi ço. Comoestamosusandoo AJAXmaissimplesquepoderia
funcionar,vamosdeixarparaexplicaressesparâmetrosmaisparafrente.
Noterceiroparâmetro,tambémopcional,nóspassaremosumcallbackquere-
cebecomoparâmetroosdadosqueforamlidosdoservi ço.Maisparafrentevamos
68

## Página 83

CasadoCódigo Capítulo7. NãotenhamedodoAJAXedoJSON
explicartambémcomotrabalharsemesseterceiroparâmetro,masnomomentova-
mosmanterascoisassimples.
Vamosentãoacessaroservi çoqueestáemhttp://livro-capitulo07.herokuapp.
com/helloeexibirotextoqueéretornado:
var servico = "http://livro-capitulo07.herokuapp.com/hello";
$.get(servico, function(data) {
alert(data);
});
Aoexecutarmosessecódigo,veremosamensagemdaimagem7.5
Figura7.5:Olá!
7.4 Enviando parâmetros com AJAX
Lembraqueeufaleisobreosegundoparâmetro,queéopcional,ondepodemospas-
sarparâmetrosparaoservi ço? Vamosaprenderausá-loagorapararetornaruma
mensagemumpoucodiferente.
Oendereçodoservi çoéomesmo,massepassarmosumnomeparaele,usando
umparâmetrochamado nome,amensagemderetornoserádiferente,repetindoo
nomequevocêinformou.
Onossoparâmetrovaiserdefinidocomoum dicionário,separandoonomedo
valorutilizandoocaracterededoispontos.
69

## Página 84

7.4. EnviandoparâmetroscomAJAX CasadoCódigo
Dicionário
Dicionários,comovocêprovavelmentejásabe,sãoestruturascomuns
emváriaslinguagensefuncionamcomo Arrays,comadiferen çaque,
emumdicionário,oidentificadorpodeserqualquervalor,enquantoem
umArrayoidentificadorésempreumnúmero.Éohashtable,oumapa,
dealgumasoutraslinguagens. Nestelivropodemosutilizarostermos
objetoedicionáriocomosinônimos,amenosqueeuestejaexplicitamente
dizendoocontrário.
Sedeclararmosumavariávelcontendoumdicionáriocomonocódigo
abaixo
var parametros = {nome: "Paulo", idade : 33 };
Quandoacessarmosovalorusando parametros["nome"], teremoso
texto"Paulo”.Analogamente, parametros["idade"]devolve 33.
Vamosdefinironomeaserpassadodaformaaseguir:
var parametros = {nome: "Caro Leitor" };
Agorapassamosoparâmetronométodo get:
var parametros = {nome: "Caro Leitor" };
var servico = "http://livro-capitulo07.herokuapp.com/hello";
$.get(servico, parametros, function(data) {
alert(data);
});
Agora,vejasó,afigura7.6mostraqueamensagemfoialteradadeacordocomo
parâmetroquepassamos.
70

## Página 85

CasadoCódigo Capítulo7. NãotenhamedodoAJAXedoJSON
Figura7.6:Mensagemalterada
Notecomoésimplesfazerrequisi çõesAJAXparaumservidorusandoparâme-
trosquandonecessário.
Comofoiditoantes,oterceiroparâmetrodaquelemétodo gettambéméopci-
onal.
$.get(servico, parametros);
Aoexecutarmosessecódigo,vamosverque...nãoaconteceunada.Senãopas-
sarmosumcallbackparaserexecutadoquandoovalorretornar,comovamossaber
oqueretornou,oumesmoseoservi çoretornoualgumacoisa?
PoiséaquiquevamosaprendercomousarAJAXdeumaformamaisprofissional
nojQuery.
7.5 Oobjeto jqXHR
VamosdescobrircomotrabalharcomAJAXdeummodomaissofisticado,permi-
tindoinclusivequepossamostratararespostadoservidordeacordocomaresposta.
Podemosexecutarumcódigocasooservidorretorneumerroeoutrocódigosetudo
correrbem.
Noiníciodocapítulofalamossobreosobjetos XMLHTTP,usadopeloInternetEx-
ploreratéaversão7,e XMLHttpRequest,usadospelosbrowsersmodernosepelo
InternetExplorerapartirdaversão8. Paraevitarqueodesenvolvedortenhaque
ficarlidandocomumoucomoutro,ojQuerynosofereceumobjeto jqXHR,queé
omodocurtoqueosdesenvolvedoresdojQueryacharamparanomearo jQuery
XMLHttpRequestObject.
71

## Página 86

7.5. OobjetojqXHR CasadoCódigo
Apesardasopadeletrinhas,decoraronomenãovaiserimportanteparanós.
Oimportanteévocêsaberqueesseobjetopodeintermediarecontrolartodaa
conversaçãoentreoseucódigoJavaScripteoservidorquevainosfornecerosda-
dos.NósorecebemoscomoretornotodavezqueusamosalgummétododojQuery
queefetuaumarequisi çãoAJAX,comoporexemplo,ométodo get,quevimosnos
exemplosanteriores.
Oobjeto jqXHRpermitequesejamdefinidoscallbacksparaquandoarequisi-
çãocorreubemeparaquandohouvealgumerro. Vamosreescreverosexemplos
anterioresparaentendercomoissofunciona.
Paratratarosdadosrecebidosquandotudocorrebem,vamosusaroevento done.
var parametros = {nome: "Caro Leitor" };
var servico = "http://livro-capitulo07.herokuapp.com/hello";
var $xhr = $.get(servico, parametros);
$xhr.done(function(data) {
alert(data);
});
Aoexecutarmos,veremosamesmarespostadafigura7.5. Sóqueessecódigo
podeficaraindamelhor.Essanovavariável xhrquecriamospodeserevitada,con-
catenandochamadasdefun ções:
var parametros = {nome: "Caro Leitor" };
var servico = "http://livro-capitulo07.herokuapp.com/hello";
$.get(servico, parametros)
.done(function(data) {
alert(data);
});
Lembrandoquedevemostomarcuidadoemencadearmuitasfun çõesdessa
forma,evitandotornarocódigoilegível.
72

## Página 87

CasadoCódigo Capítulo7. NãotenhamedodoAJAXedoJSON
Figura7.7:Erro404éumdosmaiscomuns
Podemoscriarumcallbackespecíficoparaquandooservidornosretornarum
erro. Eucrieiumendere çoquevainosretornarerrotodavezqueoacessarmos.
Poderíamossimplesmenteinformarumendere çoquenãoexiste,maspreferinão
complicarascoisas.Oeventoquetrataoscasosdeerroéo fail.
var servico = "http://livro-capitulo07.herokuapp.com/error";
$.get(servico)
.fail(function(data) {
alert(data.responseText);
});
Vamosverentãoamensagemdafigura7.8.
73

## Página 88

7.6. EoqueéoJSON? CasadoCódigo
Figura7.8:Foimesmoumerroproposital
Mas o que é considerado um erro?
Todarequisição HTTP,queéoprotocolosobreoqualoAJAXtrabalha,
retornaumcódigodetrêsdígitosquenosinformasetudocorreubem,
seapáginanãofoiencontrada,seoservidorapresentouerrooumesmo
sevocêdeveserredirecionadoparaoutroendere ço.
Quandoarequisi çãotrazumcódigoquecome çacom1,2ou3,dizemos
queacomunica çãoocorreucomsucesso. Ocódigo 200,porexemplo,
significaquetudocorreubem,oconteúdofoienviado,enormalmente
vemacompanhadodotexto“OK”.
Quandoretornacomumcódigoquecome çacom4ou5,sabemosque
houvealgumerronarequisi ção. Oserrosmaiscomunssãoo 404,que
indicaqueorecursoouapáginanãofoiencontrada,eoerro 500,que
indicaquehouveumerroqualquernoservidor.
UmalistadecódigosHTTPpodeserencontradaemhttp://goo.gl/VJz74
Jásabemoscomotransportartextodeumladoparaooutro.Tambémficoufácil
descobrirseachamadaAJAXfoifeitacomsucesso.Agorafaltasabercomoorganizar
osdadosquevamostransmitirdeumladoparaooutro.FaremosissocomJSON.
7.6 E oq u eéoJSON?
“EunãodigoqueinventeioJSON...Oqueeufizfoiencontrar,nomear,descrever
comoaquiloerautil...Aideiajáestavaentrenósháalgumtempo.Oqueeufizfoi
74

## Página 89

CasadoCódigo Capítulo7. NãotenhamedodoAJAXedoJSON
criaraespecifica çãoecriarumpequenositesobreoassunto. ”
–DouglasCrockford
Namaioriadasvezes,transmitirapenasumafraseouumnúmeronãoéosufi-
cienteparaquenossocódigoJavaScriptsecomuniquecomoservidor.Nessescasos,
precisamosenviarereceberlistas,valoreseobjetoscomplexoscontendotodaainfor-
maçãonecessária.Existeminúmerassolu çõesparaisso,sendoqueasmaiscomuns
sãoXMLeJSON.
OformatoXMLnãoésimplesdeserlidoporhumanos,eascoisassópioramse
estivermoslidandocomobjetoscontendoobjetos.Já JSONéumaformadeserializar,
ouconverterparatexto,objetosJavaScriptdemodoquesejamlegíveisinclusivepor
humanos.
EsseformatofoiespecificadoedefinidooriginalmenteporDouglasCrockford,
aquelefamosoautordolivro JavaScript:TheGoodParts[4],porvoltadoanode2001.
AgrandevantagemdoJSONsobrequalqueroutraformadeserializa çãoéque
oJavaScriptlidacomoformatodemodotransparente,convertendoainforma ção
emformatotextoparaumtiponativodalinguagem,evitandoousodebibliotecase
ferramentasquepossamcomplicaroseucódigo.
Podemostrabalharcomseistiposdedados: textos;números,quepodemser
inteirosoudecimais; lógicos,oubooleanos,quesão trueou false;listas,quefun-
cionamcomo ArraysJavaScript;objetos,quefuncionamcomo dicionáriosJavaS-
cript,conformevimosnestemesmocapítulo;e null,quesimbolizaaausênciade
umvalor.
Vocêpodecombinarlivrementeobjetoselistascomosseistiposdedadosvá-
lidos,representandovalorescomplexosquecontémtodaainforma çãonecessária
paraasuarequisi ção.
Maisdetalheseaespecifica çãocompletapodemserencontradosemhttp://json.
org/
ParademonstrarquecaratemoJSON,vamosusarosdadosdesselivroparaque
vocêentendamelhorcomofunciona:
{
"autor" : "Plínio Balduino",
"titulo" : "Dominando JavaScript com jQuery",
"ano" : 2013,
"editora" : "Casa do Código",
"usa_drm" : false,
75

## Página 90

7.6. EoqueéoJSON? CasadoCódigo
"capitulos": [
"Apresentação",
"Refazendo uma loja virtual",
"Adicionando JavaScript",
"Um JavaScript diferente em cada navegador",
"Simplifique com jQuery"
]
}
Umrecursomuitobacanaquepodenosajudaravisualizarmelhorumobjeto
JSONéositehttp://www.jsoneditoronline.org/
Figura7.9:JSONeditoronline
Essesitetemdoispainéis. NodaesquerdavocêescreveocódigoJSON,pres-
sionaobotãocomasetaparaadireitae,nopaineldaesquerda,vocêvaiveruma
representaçãointerativadoobjeto.
Épossíveltambémmontarumobjetodoladodireito,pressionarobotãocom
asetaparaoladoesquerdoeverocódigoJSONequivalentenopainelesquerdo.
AoentrarmoscomocódigoJSONdonossolivro,conformedemonstramosacima,
teremosarepresenta çãovisualdafigura7.10
76

## Página 91

CasadoCódigo Capítulo7. NãotenhamedodoAJAXedoJSON
Figura7.10:RepresentaçãodocódigoJSON
Lembraqueanteriormentenósfalamossobre dicionáriosemJavaScript? Se
olharmoscommaisaten çãoaoconteúdodonossocódigoJSON,vamosverqueseu
conteúdonadamaisédoqueum dicionário,contendo Strings,valoresnuméricose
lógicos,oubooleanos.Esse dicionáriocontémtambémumArraycomalgunscapi-
tulosdolivro.
Nãoporcoincidência,oformatoJSONéumcódigoJavaScriptválido,podendo
seratribuídoaumavariáveletratadocomoumobjetoqualquer,comofizemosna
figura7.11. Dessaforma,podemosacessarcadavalorusandoachavecomouma
propriedadedeumobjetoJavaScript.Paraacessarosnomesdoscapítulosdolivro,
podemosacessarcadaumdelescomoum ArraydoJavaScript,exatamenteporque
JSONéJavaScriptpuro.
77

## Página 92

7.7. JuntandoJSONeAJAX CasadoCódigo
Figura7.11:UsandoJSONcomoumobjetoJavaScript
7.7 Juntando JSON eAJAX
UsarAJAXcomJSONéalgomuitosimplescomjQuery.
VamosusarumsitedeconsultadeCEPchamadoPostmonparademonstrar.Ao
informarumCEP,oservi çovairetornarumJSONcomosdadosdologradourose
ocódigoforválido,ouumerroseoCEPnãoforencontradonabasedosCorreios.
Paraacessarmososervi çousandooCEP 04101-300, vamosusaroendere ço
abaixo:
http://api.postmon.com.br/v1/cep/04101-300
Oserviçovairetornaroconteúdoabaixo,emformatoJSON.Formateioresul-
tadoparaficarmaisfácilentendermos.
{
"complemento": "de 2771 a 5049 - lado \u00edmpar",
"bairro" : "Vila Mariana",
"cidade" : "S\u00e3o Paulo",
"logradouro" : "Rua Vergueiro",
"cep" : "04101300",
"estado" : "SP"
}
Aúnicadiferençaemrela çãoaoquejávimosatéagoraéquevamosusaromé-
todo getJSONpararetornarumvalorJSON.Osparâmetroseofuncionamentosão
iguaisaosdométodo get.
78

## Página 93

CasadoCódigo Capítulo7. NãotenhamedodoAJAXedoJSON
Vamoscriarumafun ção onCepDoneparaexibirologradouro(nomedarua,
praçaouavenida)casoovalorpassadosejaválido.Aídizemosquequandoacha-
madaforconcluída,ocallback onCepDonedeveserexecutado:
var servico = "http://api.postmon.com.br/v1/cep/";
var cep = "04101-300";
function onCepDone(data) {
console.log("A Casa do Código fica na " + data.logradouro);
}
$.getJSON(servico + cep)
.done(onCepDone);
Aoexecutarmosessecódigo,teremospartedoendere çodaeditora,conformea
figura7.12.
Figura7.12:RetornodaconsultadeCEP
Percebaqueavariável data,quecontémoretornodoservi ço,jáestáconvertido
emumobjetoJavaScript. Comissovocêpodeacessarqualquerinforma çãoretor-
nada,comobairrooucidade,comoseumapropriedadedoobjeto.Foiexatamente
oquefizemosparaexibirologradouro.
VamosprepararnossocódigotambémparalidarcomCEPsquenãoexistemna
basedosCorreios.Paraisso,comojávimosantes,vamosusaroevento fail.
Aproveitandoocódigodoexemploanterior,teremos:
var servico = "http://api.postmon.com.br/v1/cep/";
var cep = "12345-789";
function onCepDone(data) {
console.log("A Casa do Código fica na " + data.logradouro);
}
79

## Página 94

7.8. Políticasdesegurançadosbrowsers CasadoCódigo
function onCepError(error) {
console.log("Erro: " + error.statusText)
};
$.getJSON(servico + cep)
.done(onCepDone)
.fail(onCepError);
Executandoessecódigo,veremosamensagemdeerrodobrowsereoconteúdo
doerro,queestaránavariável error,conformeafigura7.13
Figura7.13:Erronoretorno
ParavocêveroAJAXfuncionandocomorealmenteacontecenodiaadia,basta
vocêcriarum input text efazercomque,assimqueeleperderofocus,umcall-
backdeveexecutaro $.getJSONpassandooargumentodacaixadetexto!Seore-
tornoinformarquehouvesucesso,podedeixarabordadacaixadetextoverde.Sea
requisiçãoretornaralgumerro,podedeixaremvermelho!Fa çaesseexercício!
Reparequenessecasofazemosachamadaassíncrona:oservi çoqueverificao
CEPsóvaiserchamadodepoisdapáginatersidocarregada.Maisainda,vaiacon-
tecersomentequandoumeventofordisparadoecairnasuafun çãodecallback.
Éexatamentedessaformaque,porexemplo,abuscadoGooglepreenchesuges-
tõesparavocênabarradepesquisa.Quandoumdeterminadoeventoacontece(por
exemplo,vocêdigitoumaisde3caracteres),umcallbackfazumachamadaparao
servidormandarassugestõesquecome çamcomaquelas3letras.Nocasodesucesso,
oGooglelistaasop çõesparavocênoHTML.
7.8 Políticas de segurança dos browsers
PorqueusamosumservidorpragerarosJSONsquequeríamostrabalhar?Poisnão
podemosfazerissoacessandoarquivoslocaisdeteste!
Porumaquestãodeseguran ça,osbrowsersmodernosnãopermitemquevocê
façachamadasAJAXapartirdeumarquivolocalouquevocêacesseumendere çoem
80

## Página 95

CasadoCódigo Capítulo7. NãotenhamedodoAJAXedoJSON
umservidordiferentedoseu[19].Afigura7.14nosmostraumamensagemdeerro
exibidaquandotentamosfazerumachamadaAJAXatravésdeumarquivolocal,ou
seja,queestánanossaprópriamáquina. Arquivoslocaissãoexibidosnabarrade
endereçosdobrowsercom file://aoinvésdehttp://noiníciodoendere ço.
Existemalgumasformasdepassarmosporcimadessaspolíticasdeseguran ça.
Figura7.14:Chamadaapartirdeumarquivolocal
A primeira é chamada deCross-Origin Resource Sharing,eéh a b i l i -
tada quando o servidor que está nos fornecendo os dados insere o cabeçalho
Access-Control-Allow-Origin: * narespostaHTTP.Essaéaformamaislimpa
epadronizadadeacessarmosoutrodomíniousandoAJAX,mastemumasériede
problemaselimita ções.Amaiordelas,semdúvida,équandoestamosacessandoum
servidorquenãoincluiessecabe çalhonaresposta.OutroproblemaéqueoInternet
Explorer7nãodásuporteaessafuncionalidade.Asversões8e9,deacordocomo
siteCanIuse... ,dãoapenassuporteparcial.
http://caniuse.com/#feat=cors
Asegundaformadeseevitaraspolíticasdeseguran çaéusandoumatécnica
chamadaJSONP,queéumcomplementoaoformatoJSON,equevamosvercom
detalhesmaisparafrente.Essasduasformasexigemalgumacolabora çãoporparte
doservidor.
Existeaindaumaterceiraforma,queéamenossegurae deveserusadaapenas
parafinsdedesenvolvimentoetestes ,consisteemdesabilitarosmecanismosde
segurançadobrowser.
Se você estiver usando o Chrome, inicie seu browser com o parâmetro
--disable-web-security.
Se você estiver usando o Firefox, entre no endereço about:config e adi-
cione a chavecapability.policy.default.XMLHttpRequest.open com o valor
allAccess.
Lembre-sederemoveroparâmetroouachaveassimquevocêterminarseus
81

## Página 96

7.8. Políticasdesegurançadosbrowsers CasadoCódigo
testes.NãoqueremosqueninguémaltereseuperfilnoFacebookoupubliquealgo
semautorizaçãonoTwitter,nãoémesmo?
Nomundorealnãopodemosficardesabilitandotravasdeseguran çanasmáqui-
nasdocliente,entãoésemprebomsabermoscomoinstalarumservidorlocalpara
podermosexecutarnossosscriptsenquantoestamosdesenvolvendoaaplica ção.
Alternativamente,vocêpodeusaro jsFiddleparatestarseusscriptssemane-
cessidadedeinstalarumservidor.
VamosveragoracomoutilizarAJAXcomJSONeRESTnumaaplica çãoreal.
OqueéREST?Vocêvaiaprendernopróximocapítulo.Fiqueatento!
82

## Página 97

Capítulo8
Umgerenciadordetarefascom
AJAX
“Tudodeveriaserfeitodaformamaissimplespossível,masnãomaissimplesdoque
isso.”
–AlbertEinstein
8.1 Melhorando nosso gerenciador
AgoraqueaprendermoscomousarAJAXeoqueéJSON,vamosvamosvoltarao
nossogerenciadordetarefasdocapítulo6paraadicionarmaisrecursos. Vamos
aproveitarparaaprendertambémcomousaralgunsrecursosavan çados.
Nãoseriabomseconseguíssemosverasnossastarefasmesmodepoisdetermos
fechadoobrowseroudepoisdetermosrecarregadoobrowser?
Podemosgravarcadaumadastarefasnumservidorqueeuprepareiespecial-
menteparaessaocasiãousandoAJAX.Astarefasserãoenviadasparaoservidor

## Página 98

8.2. Carregandoastarefasdoservidor CasadoCódigo
assimqueelasforematualizadas.
Vamospermitirtambémqueastarefassejamlidasassimquealistadetarefas
sejacarregada,exibindotodosositensqueestãogravadosnoservidor.
Usaremososite jsFiddleeoconsoledobrowserparaescreveretestarosnossos
exemplosabaixo.Sevocêjátiverexperiênciaconfigurandoumservidorwebnasua
máquina,fiqueavontadeparaexecutarseusexemplosatravésdele.
Oresultadofinaldocapítuloanteriorpodeserencontradonoendere çoabaixo,
evaiserabasedoquevamosdemonstrarnestecapítulo.
http://jsfiddle.net/pbalduino/faWn4/
8.2 Carregando as tarefas do servidor
Apesardeestarmostrabalhandonomesmogerenciadordetarefas,onossocódigo
HTMLvaificarumpoucodiferentedocódigousadonocapítulo6,umavezque
precisaremosapenasdalistadetarefasvazia.
Figura8.1:Carregandoastarefas
Ocódigodessecapítuloestádisponívelnoendere çoabaixo:
http://jsfiddle.net/pbalduino/RcRMv/
Vamosapagartudooqueestiverdentrodoelemento divquetemo idiguala
tarefa-lista.O divcomid tarefa-listacontinuaaexistir,masvaificarvazio.
OnossocódigoHTMLvaificarassim:
<div class="todo">
<h2>TODO List </h2>
84

## Página 99

CasadoCódigo Capítulo8. UmgerenciadordetarefascomAJAX
<input type="text" id="tarefa">
<div id="tarefa-list">
</div>
</div>
Vamoscomeçarcarregandonossastarefasassimquealistaéexibidapelapri-
meiravez.Paraisso,vamoscriarechamarumafun ção loadTarefasdentrodonosso
velhoamigo,oevento $(document).ready.
Comonossoservi çoquearmazenadastarefasficanumservidorcompartilhado,
usaremosumidentificadorparaousuário.Podeseroseunome,seuemailouqual-
quertextocurtoquefa çaassuastarefasnãosemisturaremcomasdosoutrosusuá-
rioseleitores.Vamosgravaresseidentificadornumavariávelchamada meu_login.
Vamosgravartambémonomedoservidornumavariávelchamada(adivinhe?)
servidor. Issovaiajudarbastanteparaocasodevocêpreferirutilizaropróprio
servidor,ouparaeventualidadedoservidormudardeendere ço.
Comtodasessasinforma ções,nossocódigovaificarassim:
$(function() {
var meu_login = "seu@email.com";
var server = "http://livro-capitulo07.herokuapp.com";
var $lastClicked;
Emseguidatemostodoocódigodocapítulo6,quevamosrelembrarrapida-
menteparaquevocênãoseperca.
Criamos a função onTarefaDeleteClick, que será executada sempre que o
usuárioclicarnoíconedalixeira.
function onTarefaDeleteClick() {
$(this).parent('.tarefa-item')
.off('click')
.hide('slow', function() {
$(this).remove();
});
}
Emseguidatemosafun ção addTarefa,querecebeumtextoeadicionaatarefa
àlista.
85

## Página 100

8.2. Carregandoastarefasdoservidor CasadoCódigo
function addTarefa(text) {
var $tarefa = $("<div />" )
.addClass("tarefa-item")
.append($("<div />" )
.addClass("tarefa-text")
.text(text))
.append($("<div />" )
.addClass("tarefa-delete"))
.append($("<div />" )
.addClass("clear"));
$("#tarefa-list").append($tarefa);
$(".tarefa-delete").click(onTarefaDeleteClick);
$(".tarefa-item").click(onTarefaItemClick);
}
Criamostambémdoiseventos:um,chamado onTarefaKeydown,paraquando
o usuário pressionarENTER na inclusão de novas tarefas e outro chamado
onTarefaEditKeydownparaquandoousuáriopressionar ENTERduranteaedi ção
datarefa.
function onTarefaKeydown(event) {
if(event.which === 13 ) {
addTarefa($("#tarefa").val());
$("#tarefa").val("");
}
}
function onTarefaEditKeydown(event) {
if(event.which === 13 ) {
savePendingEdition($lastClicked);
$lastClicked = undefined;
}
}
Criamostambémumcallbackchamado onTarefaItemClickqueseráinvocado
quandoousuárioclicaremalgumatarefa,permitindoaaltera ção.
function onTarefaItemClick() {
86

## Página 101

CasadoCódigo Capítulo8. UmgerenciadordetarefascomAJAX
if(!$(this).is($lastClicked)) {
if($lastClicked !== undefined) {
savePendingEdition($lastClicked);
}
$lastClicked = $(this);
var text = $lastClicked.children('.tarefa-text').text();
var content = "<input type= 'text' class='tarefa-edit' value='" +
text + "'>";
$lastClicked.html(content);
$(".tarefa-edit").keydown(onTarefaEditKeydown);
}
}
Criamosumafun çãochamada savePendingEditionparafazercomqueasta-
refasquetenhamedi çãopendentesejamgravadas.
function savePendingEdition($tarefa) {
var text = $tarefa.children('.tarefa-edit').val();
$tarefa.empty();
$tarefa.append("<div class= 'tarefa-text'>" + text + "</div>")
.append("<div class= 'tarefa-delete'></div>")
.append("<div class= 'clear'></div>");
$(".tarefa-delete").click(onTarefaDeleteClick);
$tarefa.click(onTarefaItemClick);
}
Finalmentevamosatribuiroscallbacksaosrespectivoseventos.
$(".tarefa-delete").click(onTarefaDeleteClick);
$(".tarefa-item").click(onTarefaItemClick);
$("#tarefa").keydown(onTarefaKeydown);
87

## Página 102

8.2. Carregandoastarefasdoservidor CasadoCódigo
E,finalmente,vamosadicionarafun ção loadTarefas,quevaicarregarastarefas
queestãogravadasnoservidor.
function loadTarefas() {
// calma que já chegaremos aqui
}
loadTarefas();
});
Nafunção loadTarefas,vamoseliminartodosositensqueporalgummotivo
estejamnalistae,usandoométodo getJSONvamosinformaroendere çodoservi ço
queretornartodasastarefasdaqueleusuário.Aten çãoparaasletrasmaiúsculasao
utilizarosmétodosdojQuery,jáqueoJavaScriptdiferencialetrasmaiúsculasde
minúsculas.
Paradeixarotrabalhoomaissimplespossível,nossoservi çoquevairetornaras
tarefaschama-se tarefas,evamospassarumparâmetro usuariocontendoonome
dousuárioquevocêescolheunoiníciodaexplica ção.
OmétodogetJSONpoderecebertrêsparâmetros:oprimeiroparâmetroéaURL
doserviçoousitequevaifornecerosdados;osegundocontémosparâmetrosase-
remenviadosaoservidoremformatoJSON;eoterceirorecebeumcallbackqueserá
executadoassimqueométodoterminardereceberosdadoscomsucesso,passando-
osporparâmetroparaocallback.
Umaformabemcomume,naminhaopinião,maislimpadeseusaressemétodo
éencadearosmétodos done,paraquandoachamadaretornarumvalor, fail,para
quandoacontecerumerroqualquernacomunica çãoounachamada.
Ocallbackdoevento donevaireceberum Arraycontendotodasastarefas.Você
vaireceberduastarefaslogonaprimeiravezquevocêexecutaroexemplocomo
seulogin,mesmosemtercadastradonenhumatarefa.Oresultadopodeservistona
figura8.2
88

## Página 103

CasadoCódigo Capítulo8. UmgerenciadordetarefascomAJAX
Figura8.2:Tarefasvindasdoservidor
Sevocêvoltarnafigura8.2,vaiperceberqueoservi çonosenviatambémum
valor idparacadaumadastarefas. Essevalorserveparaque,aoalterarmosou
incluirmosumatarefa,obancodedadosqueestánoservidorsaibadequaltarefa
estamosfalando.Comocadatarefatemum idquenãoserepete,podemostercerteza
dequeoservidornãovaiapagaroualterarumatarefaerrada.
Comonocapítulo6nósaindanãoestávamospensandoemgravarissonum
bancodedados,vamosterquealteraralgumasfun çõesdonossoscriptparaque
possamoslidarcomessevalor id.
Aalteraçãoquevamosfazerconsisteemadicionarmaisumelemento divdentro
doitemdatarefa.Comoesseelemento divnãodeveservisívelaousuário,vamos
adicionaraslinhasabaixonofinaldonosso CSS.
.tarefa-id {
visibility: hidden;
}
8.3 Usando parâmetros opcionais
Emseguida,vamosalterarafun ção addTarefaparaqueelapermitaquepossamos
informaro iddatarefa.Vamosfazerdeumaformaqueoparâmetro idsejaopcional.
Casoelenãosejainformado,vamosconsiderarqueo idéigualazero,indicandoque
89

## Página 104

8.3. Usandoparâmetrosopcionais CasadoCódigo
atarefaaindanãoexistenobancodedados.Issotambéméútilparaquetenhamos
quealteraromínimopossíveldocódigoquejáexiste.
Quandovocêdeixadeinformarumparâmetronumafun ção,eleficacomova-
lor undefinedque,noJavaScript,significaqueavariávelnãotevevalornenhum
atribuído.Falandoassimsoabemóbvio,não?
Vamosverificarlogonoiníciodafun çãoseovalorde idrecebeuumvalorou
não.Ocódigoparaissoficaassim:
id = id || 0 ;
Ooperador ||éumOUbooleano(oulógico,sepreferir).Éumaformaresumida
eelegantedeescrevermosocódigoabaixo:
if(id !=== undefined) {
id = id;
} else {
id = 0 ;
}
Vocêdeveconcordarcomigoqueosegundocódigo,alémdemaioremaisdi-
fícildeler,aindatemum id = id muitoesquisitoalinomeio. "Seavariáveltiver
umvalorquenãoseja undefined,continuecomomesmovalorcomosenadativesse
acontecido”.
Apresentaçõesfeitas,afun çãovaificarassim:
function addTarefa(text, id) {
id = id || 0 ;
var $tarefa = $("<div />" )
.addClass("tarefa-item")
.append($("<div />" )
.addClass("tarefa-id")
.text(id))
.append($("<div />" )
.addClass("tarefa-text")
.text(text))
.append($("<div />" )
.addClass("tarefa-delete"))
.append($("<div />" )
.addClass("clear"));
90

## Página 105

CasadoCódigo Capítulo8. UmgerenciadordetarefascomAJAX
$("#tarefa-list").append($tarefa);
$(".tarefa-delete").click(onTarefaDeleteClick);
$(".tarefa-item").click(onTarefaItemClick);
}
Vamosaproveitarafun ção addTarefaparaincluirnossastarefas,passandoo id
querecebemosnanossarequisi çãoAJAX:
function loadTarefas() {
$("#tarefa").empty();
$.getJSON(server + "/tarefas", {usuario : meu_login})
.done(function(data) {
console.log("data: " , data);
for(var tarefa = 0 ; tarefa < data.length; tarefa ++) {
addTarefa(data[tarefa].texto, data[tarefa].id);
}
});
}
Existemmaiscoisasqueprecisamsermexidasparapoderlidarcomo id,mas
vamosalterarorestantedocódigoconformeanecessidade,paraquevocênãotenha
quelidarcomummontedecódigosemnecessidade.
8.4 Alterando tarefas
Paraalterarumatarefa,vamosenviarotextoeoiddatarefaparaoservi ço /tarefa,
nosingular,usandoométodo postdojQuery.
Ométodo postfuncionaexatamentecomoosjáconhecidosmétodos gete
getJSON:oprimeiroparâmetroindicaoendere çodoservi çoquevamosacessar,o
segundocontémosparâmetrosquevamosenviaraoservidoreoterceiro,opcio-
nal,recebeumcallbackqueseráexecutadoquandoarequisi çãoforconcluídacom
sucesso.Oseventos donee failtambémpodemserusadoscomométodo post.
91

## Página 106

8.4. Alterandotarefas CasadoCódigo
Figura8.3:Alterandoouincluindoumatarefa
Vamoscriarumafun ção updateTarefa,queenviaatarefaatualizadaparaoser-
vidor,quedevegravá-lanumbancodedadosparaquepossamosrecuperá-lana
próximavezqueentrarmosnogerenciador.
Essafunçãovaireceberotextoeoiddatarefacomoparâmetros.Comovocêsó
alteraumatarefaquejáexiste,eumatarefaquejáexistesempredeveterumid,não
fazsentidotrataroparâmetro idcomoopcional.
Oserviço /tarefarecebedoisparâmetros: tarefa_id,quecontémoiddatarefa
aseralterada,e texto,quecontémotextodatarefa.
function updateTarefa(text, id) {
$.post(server + "/tarefa", {tarefa_id : id, texto : text});
}
Bemsimples,não?
Alteraremosonossocódigojáexistenteparaquepossamosusaressanovafun-
ção.
Primeiramente,vamosalterarafun ção onTarefaItemClickparapermitirqueo
idsejamantidoenquantoousuárioalteraotextodatarefa.Vamosfazerissocriando
umelemento divquetenhaaclasse tarefa-id.Esseelementovaificarinvisívelpara
ousuárioevaiguardarovalordoiddatarefaeditada.
function onTarefaItemClick() {
if(!$(this).is($lastClicked)) {
if($lastClicked !== undefined) {
92

## Página 107

CasadoCódigo Capítulo8. UmgerenciadordetarefascomAJAX
savePendingEdition($lastClicked);
}
$lastClicked = $(this);
var text = $lastClicked.children('.tarefa-text').text();
var id = $lastClicked.children('.tarefa-id').text();
var content = "<div class= 'tarefa-id'>" + id + "</div>" +
"<input type= 'text' class='tarefa-edit' value='" +
text + "'>";
$lastClicked.html(content);
$(".tarefa-edit").keydown(onTarefaEditKeydown);
}
}
Vamosalterartambémafun ção savePendingEdition,queéresponsávelpor
geraroHTMLdoitemdatarefaqueestavasendoalteradaesumircomacaixade
textousadanaedi ção.
Tambémfaremoscomqueessafun çãosejaaresponsávelporenviarosdados
paraoservidor,atravésdafun ção updateTarefa.
function savePendingEdition($tarefa) {
var text = $tarefa.children('.tarefa-edit').val();
var id = $tarefa.children('.tarefa-id').text();
$tarefa.empty();
$tarefa.append("<div class= 'tarefa-id'>" + id + "</div>")
.append("<div class= 'tarefa-text'>" + text + "</div>")
.append("<div class= 'tarefa-delete'></div>")
.append("<div class= 'clear'></div>");
updateTarefa(text, id);
$(".tarefa-delete").click(onTarefaDeleteClick);
$tarefa.click(onTarefaItemClick);
}
Agoraasnossastarefasjáestãosendocarregadasautomaticamenteegravadas
noservidorassimqueelassãoalteradas. Paratestar,fa çaoseguinte: altereuma
93

## Página 108

8.5. UmaintroduçãoaoREST CasadoCódigo
tarefa,grave-ae,emseguida,recarreguesuapágina.Vocêveráqueotextoalterado
datarefacontinuarásendoexibidonatela. Antesdasnossasmelhorias,todasas
mudançaseramignoradaseovalororiginaldatarefavoltavaaserexibido.
8.5 Uma introdução ao REST
VocêjádeveterouvidofalardeRESTemalgumdessessitesoublogsquefalam
sobrearquiteturadesoftwareoudesenvolvimentoparaWeb.Senuncaouviufalar,
recomendoquevocêcorraatrásdotempoperdidoparaentenderdoquesetrata.
RESTéumassuntotãovastoecheiodeconteúdoquedariaparaencherum
livrointeirotranquilamente. Aminhainten çãoaquinãoéexplicarRESTemseus
detalhesoutornaroleitorumespecialistanoassunto.Aideiaéquevocêtenhauma
visãogeraldoquesignificae,principalmente,entendacomoissoseencaixananossa
aplicação.
OpadrãoRESTsetornouconhecidoapósRoyFieldingpublicarsuadisserta ção
dedoutorado[5],ondeexplicaosprincípiosepadrõesparasedesenvolvereutilizar
umaaplicaçãousandoREST.
Comovocêjádevesaber,umaaplica çãoWeb,epraticamentetodoorestodos
sitesdoWorldWideWeb,secomunicaatravésdeumprotocolochamadoHTTP
(ProtocolodetransferênciadeHipertexto).Esseprotocolousaduaspartesdistintas
emsuaschamadas:um métodoeumrecurso.
Ummétodoindicaaa çãoaserexecutadasobreo recursoindicado.Porissoé
podeserchamadode verbo.
Jáumrecursoindicaoarquivo,páginaouservi çoquedeveseracessadopelo
porumbrowserouporumaaplica ção.
Exemplificando,vamosentenderoqueacontecequandofazemosumarequisi-
çãoaoservi çodeconsultadeCEPs,comofizemosnocapítulo7.
Nósusamosométodo get,paraacessaroendere çohttp://api.postmon.com.br/
cep/04101300.Porbaixodospanos,oqueobrowserfezfoiseconectaraoservidor
queestánoendereço api.postmon.com.br.Deverdademesmoexisteumasériede
outrospassosnessemeiotempoenvolvendoservidoresdenomes,masissoficacomo
liçãodecasaparavocê.
Apósseconectarnoservidor,obrowservaienviarocomando:
GET /v1/cep/04101300
Ouseja,arequisi çãoéfeitapeloverbo GETeorecurso /v1/cep/04101300. É
porissoqueométododojQuerysechama get.Damesmaforma,quandousamos
94

## Página 109

CasadoCódigo Capítulo8. UmgerenciadordetarefascomAJAX
ométodojQuery post,oqueestásendoenviadoparaoservidoréoverbo POST.
Figura8.4:Aspartesdeumendere ço
ExistemoutrosverbosHTTPquesãousadoscomRESTalémdoGETedoPOST.
Quandoestamostrabalhandocomopera çõesdecadastro(criar,ler,atualizaredele-
tar,conjuntodeopera çõesconhecidocomo CRUD),usamosquatroverbosHTTP:
•GETparaler
•POSTparaatualizar
•PUTparaincluir
•DELETEparaexcluir
Comovocêvaiperceberdaquiapouco,podemosusaro mesmorecurso para
váriasoperações,desdequeestejamosutilizando verbosdiferentes.
RESTnãoéapenasisso,masparaoquevamosprecisarémaisdoquesuficiente.
8.6 UtilizandoPUT eDELETE no browser
ApesardojQuerypermitirousodePUTeDELETE,amaioriadosnavegadores
aceitaapenasosprotocolosGETePOSTemsuasrequisi ções,oquenosobrigaa
usaralgunstruquesparadesenvolveraplica çõesusandoRESTquefuncionemem
qualquerbrowser.
Boapartedasbibliotecasatuaisusadasparadesenvolveraplica çõesWebconse-
guementenderquevocêestáquerendousarPUTouDELETEsevocêinformarisso
numparâmetroespecialchamado _methodefizersuasrequisi çõesusando POST.Os
nossosserviçosforamfeitoscomRails,quesegueessaprática.
8.7 Adicionando tarefas com REST
Oprocessodeadicionartarefasnãoémuitodiferentedoquefizemosparatrabalhar
comalterações,comadiferen çaqueatarefaaindanãoexistenobancodedados,
95

## Página 110

8.7. AdicionandotarefascomREST CasadoCódigo
eo idteráserázeroantesdeenviarmosparaoservidor,ereceberáumnovovalor
assimqueeleforgravadonobancodedados.Issovainospermitirqueatarefaseja
alteradaegravadanormalmentecomoqualqueroutratarefaquevimosatéagora.
Vamoscriarumafun çãochamada newTarefa,quevairecebercomoparâme-
trootextodatarefaeumobjetojQuerycontendooelemento divquecontémo
id. Assim,afunçãovaipoderatualizarovalordoidassimquereceberaresposta
doservidor.Lembre-sequeestamostrabalhandocomprocessosassíncronosenão
sabemosquantotempovailevarparaessarespostachegaraobrowser.
Conformevimosanteriormente,nãopodemosnosesquecerdeinformaroverbo
HTTPquevamosusar.Nessecaso,comosetratadeumainclusão,usaremosPUT.
function newTarefa(text, $div) {
$.post(server + "/tarefa",
{usuario: meu_login,
texto: text,
_method: "PUT"})
.done(function(data) {
$div.text(data.id);
});
}
Vamosalterarafun ção addTarefaparaquepossamosenviaranovatarefapara
oservidor.Vamosadicionarumaverifica çãonafun çãoparatermoscertezadeque
apenastarefascomidigualazerosejamincluídas,poisestamosusandoessamesma
funçãoparaadicionarnatelaastarefasquevieramdoservidoraocarregarmosa
lista.
function addTarefa(text, id) {
id = id || 0 ;
var $tarefa = $("<div />" )
.addClass("tarefa-item")
.append($("<div />" )
.addClass("tarefa-id")
.text(id))
.append($("<div />" )
.addClass("tarefa-text")
.text(text))
.append($("<div />" )
.addClass("tarefa-delete"))
96

## Página 111

CasadoCódigo Capítulo8. UmgerenciadordetarefascomAJAX
.append($("<div />" )
.addClass("clear"));
$("#tarefa-list").append($tarefa);
$(".tarefa-delete").click(onTarefaDeleteClick);
$(".tarefa-item").click(onTarefaItemClick);
if(id === 0 ) {
var div = $($tarefa.children(".tarefa-id"));
console.log("id", div);
newTarefa(text, $(div));
}
}
Incluaalgumastarefasecarreguenovamenteapáginaparatestar.
8.8 Excluindo tarefas
Finalmente, vamos aprender a excluir uma tarefa. Vamos alterar a função
onTarefaDeleteClick.Tudooqueprecisamossaberéoiddatarefaeenviá-lopara
oservidor.
Figura8.5:Excluindoumatarefas
Aquitambémvamosusarométodo post,dojQuery,eoverboHTTP delete,
passandooiddoelementoatravésdoparâmetro tarefa_id.Fiqueatentoparain-
97

## Página 112

8.8. Excluindotarefas CasadoCódigo
formaroiddatarefa antesdeexcluiroelementodoDOM,ouentãovocêvaificar
semsaberoquefoiexcluído.
Nossocódigovaificarassim:
function onTarefaDeleteClick() {
$(this).parent('.tarefa-item')
.off('click')
.hide('slow', function() {
$this = $(this);
$.post(server + "/tarefa",
{usuario: meu_login,
tarefa_id: $this.children(".tarefa-id").text(),
_method: "DELETE"});
$(this).remove();
});
}
Vamosexcluirumatarefaerecarregarapágina. Vocêvaiperceberqueelafoi
realmenteexcluída.
Finalmenteterminamosdedesenvolveronossogerenciadordetarefas.
Aessaaltura,vocêjádevesercapazdedesenvolversuasprópriasaplica çõescom
jQueryeentenderocódigodeaplica çõesfeitasporoutraspessoas,masaindatemos
umbomcaminhopelafrenteatéquevocêconhe çatodososrecursosqueojQuery
podeoferecer.
NopróximocapítulovamosapresentarojQueryUI,queéumabibliotecade
componentesvisuaisquetrabalhasobreojQuery.
98

## Página 113

Capítulo9
jQueryUI
“Seprecisadeum‘jeitinho’deusar,éporqueainterfacecomousuárioestáquebrada.”
–DouglasAnderson
9.1 Usando o jQueryUI
AbibliotecajQueryUIfoicriadaparapermitirarápidacria çãoeutiliza çãodecom-
ponentesvisuais,efeitosetemas,aproveitandotodaafacilidadequeojQuerytraz
emrelaçãoadiferentestiposeversõesdenavegadores.
Existemduasformasdefazerodownloaddabibliotecaparaoseuprojeto,con-
formepodemosvernafigura9.1.

## Página 114

9.1. UsandoojQueryUI CasadoCódigo
Figura9.1:Essascoresficaramestranhas...
Aprimeiraéclicarnolink Stable,queestásobainscri ção QuickDownloads.
Essaopçãoémuitoboaparaquemestácome çandoequerexperimentartodosos
recursosqueabibliotecaoferece.Poroutrolado,abibliotecainteiradojQueryUI
égrande,epodedeixaranossaaplica çãobempesadaquandoforacessadaporuma
conexãolenta.
Aoladode Stable(estável),vocêtemopção Legacy(legado),quepermiteque
vocêfaçadownloaddaversãoanterioredesatualizadadabiblioteca.Amenosque
vocêtenhaumbommotivoparaprecisardessaversão,ignore-asolenemente.
Asegundaformaajudaaresolveroproblemadoexcessodepesodabiblioteca.
Clicandoem CustomDownload (downloadpersonalizado),vocêserádirecionado
paraumaferramenta,chamada DownloadBuilder,quepermitequevocêbaixeape-
nasoqueénecessário,tornandoabibliotecamenore,consequentemente,maisrá-
pidadesercarregada.SemprequeeuprecisousarjQueryUIemumaaplica ção,eu
geroumdownloadespecíficoparaasnecessidadesdoprojeto. Vocêpodeacessar
essedownloadpersonalizadotambémpelolink:
http://jqueryui.com/download/
NoDownloadBuildervocêpodeselecionarosmódulos,componenteseefeitos
quedesejautilizar.Épossíveltambémselecionarotemaqueseráusadoparaalterar
ovisualdoscomponentes. Épossíveltambémcriarummódulodeacordocoma
identidadevisualdasuaaplica ção.
Apósodownload,bastaincluirnoseuHTMLoarquivoJavaScriptquecontém
ojQueryUI.Lembre-sede sempreincluirojQueryUI depoisdojQuery.
100

## Página 115

CasadoCódigo Capítulo9. jQueryUI
<script src="js/jquery-1.9.0.js"></script>
<script src="js/jquery-ui-1.10.0.custom.js"></script>
Obviamente,olocalondeestãoseusarquivosJavaScripteseusrespectivosnomes
podemserligeiramentediferentes.
9.2 As diversas partes do jQueryUI
OjQueryUIéformadodequatromódulos,quepodemserselecionadosautoma-
ticamentepeloDownloadBuilderconformevocêescolheoscomponentesquevai
utilizar.
UICore
ContémonúcleodojQueryUI.Todososdemaiscomponentesdependemdesta
parte.
Interactions
Éapartequedásuporteacoisascomo drag-and-drop(quandovocêarrastae
soltaalgumcomponentepelatela),ordenaritensnumatabelausandoomousee
mesmomudarotamanhodealgumelementodatelasevocêdesejar.
Widgets
WidgetssãocomponentesvisuaisquejávemcomojQueryUI.Dentreosmuitos
componentesdisponíveis,vocêtemacessoamenu,abas,botõesejanelasquesó
existemdentrodasuapágina.
Vamosdarmaisaten çãoaos widgetsmaisparafrente.
Effects
OjQueryjávemcomalgunsefeitossimples,masojQueryUItraztrezeefeitos
novosparaquevocêpossaimpressionarousuário.
Comoficadifícildemonstrarosefeitosemumlivro,recomendoquevocêacesse
apáginadedemonstraçãodojQueryUInoendere çoabaixo:
http://jqueryui.com/demos/
101

## Página 116

9.3. Temas CasadoCódigo
9.3 Temas
Pormelhorquesejaasuaaplica ção,elaestaráfadadaaofracassosetiverumvisual
desagradável.Paraajudaradeixaroseudesigncomaparênciaconsistenteeprofis-
sional,ojQueryUIpermiteousodetemas.
Temassãoconjuntosdefontesecoresquesãoaplicadasemtodososcompo-
nentescriadospelojQueryUI,epodemsertrocadosecriadosconformeasuane-
cessidade,fazendocomquetodaasuaaplica çãotroquedeaparênciadeumavez
só.
Abaixotemosumexemplodediferentestemasaplicadosaumamesmatela,con-
formevocêpodeobservarnasfiguras9.2e9.3.
Figura9.2:TemaUILightness
102

## Página 117

CasadoCódigo Capítulo9. jQueryUI
Figura9.3:TemaRedmond
Vocêpodeexperimentarecriartemasusandoumaferramentachamada Theme
Roller,queestánoendere ço:
http://jqueryui.com/themeroller/
Selecioneaaba RollYourOwn,algocomoCrieseuprópriotema,ou Gallerycaso
queiraexperimentartemasjáexistentes.
Figura9.4:Detalhedo ThemeRoller
9.4 O rganizando seus dados com accordion
Accordion,ousanfonasevocêtraduzirporcamente,éumcomponentequesetornou
popularcomoMicrosoftOffice,eexibeumapartedoconteúdoenquantooculta
todasasoutraspartes.Émuitousadoparaexibirumtextoporvezouumconjunto
decomponentesdeacordocomumdeterminadoassuntooufun ção.
103

## Página 118

9.4. Organizandoseusdadoscomaccordion CasadoCódigo
Parautilizaro accordion,vocêprecisadefinirumelemento divquevaicontero
componenteeutilizarelementos h3paradefinirostítulosdasse ções,queterãoo
conteúdotambémdentrodeelementos div.
Nocódigoabaixonósvamosmontarumapequenapáginaparaaempresa Zeca
UrubuS/A.Eusinceramenterecomendoquevocênãocomprenadaquetenhaa
marcadeles.Ocódigocompletopodeserencontradoem:
http://jsfiddle.net/pbalduino/A2zxZ/
<div id="accordion">
<h3>Quem somos </h3>
<div>
<p>Somos uma empresa que escreve aquelas coisas bonitas de
visão e missão, mas fazemos diferente na vida real. </p>
</div>
<h3>O que fazemos </h3>
<div>
<p>Criamos produtos que são vendidos com um ano de garantia e
quebram após um ano e meio de uso. </p>
</div>
<h3>Trabalhe conosco </h3>
<div>
<p>Se você é do tipo que venderia um gato morto para a própria
avó, venha trabalhar conosco!
</p>
</div>
</div>
OcódigoJavaScriptseráesseabaixo.Considerequevocêjátenhaadicionadoos
arquivosdojQueryedojQueryUInocabe çalhodoHTML.
$(function() {
$("#accordion").accordion();
});
Nafigura9.5podemosvercomoficariaessapágina.
104

## Página 119

CasadoCódigo Capítulo9. jQueryUI
Figura9.5:PáginadaZecaUrubuS/A
Vocêpodeencontraradocumentaçãodessecomponentenoendere çoabaixo:
http://jqueryui.com/accordion/
9.5 Auto-completando
UmrecursomuitobacanaqueficoubemconhecidocomosurgimentodaWeb2.0
éodeauto-completarumtexto.
Paraqueorecursofuncione,vocêprecisainformaraojQueryUIquaissãoos
valoresaseremexibidosnalistaqueapareceabaixodacaixadetexto. Vocêpode
fazerissopassandoumalistapronta,comofizemosnoexemplo,ouusandooquejá
aprendemosatéaquiecarregandodinamicamenteviaAJAX.
Oexemplofuncionalpodeserencontradonolinkabaixo:
http://jsfiddle.net/pbalduino/srN2f/
ParaoHTML,vamosprecisarapenas
<div class="ui-widget">
<label for="linguagens">Linguagem: </label>
<input id="linguagens" />
</div>
var linguagens = [
"Clojure",
"Common LISP" ,
"Erlang",
"F#",
"Haskell",
105

## Página 120

9.6. Usandobotõesmaisbonitos CasadoCódigo
"JavaScript",
"OCaml",
"Scala",
"Scheme"
];
$("#linguagens").autocomplete({source: linguagens});
Figura9.6:Autocompletesimples
Adocumentaçãocompletadessecomponenteestáem:
http://jqueryui.com/autocomplete/
http://jsfiddle.net/pbalduino/NFprU/
9.6 Usando botões mais bonitos
OjQueryUItambémpermitequevocêdeixeosbotõesmaisbonitos. Éotipode
situaçãoemquevocêvaiusarumcanhãoparamatarumamosca,masnãocusta
mostrarcomofica.
Ocódigocompletopodeserencontradoem:
http://jsfiddle.net/pbalduino/RxM94/
<button class="chique">Um botão bonito </button>
<button>Um botão normal </button>
<hr />
<input type="submit" class="chique" value="Um submit bonitão" >
<input type="submit" value="Um submit normal" >
<hr />
106

## Página 121

CasadoCódigo Capítulo9. jQueryUI
<a href="#" class="chique">Um link em forma de botão </a>
<a href="#">Um link qualquer </a>
OcódigoJavaScripttambémébemsimples:
$(function() {
$(".chique").button();
});
Podemosvernafigura9.7
Figura9.7:Botõeselegantes
Existemváriasoutrasopçõesdebotões.Vocêpodesabermaisem:
http://jqueryui.com/button/
Experimenteaplicaressesnovosbotõesnanossaaplica çãodetarefas!
9.7 Escolhendo a data com o calendário
Umgrandeproblemaparaquemescrevecódigoparao back-end,queéapartedasua
aplicaçãoquerodanoservidor,égarantirqueadatainformadapelousuárioesteja
numformatocorretoesejaválida.
Porpadrão,umacaixadetextoaceitaqualquertipodetexto,permitindoinclu-
sivequeousuárioescrevaopróprionomenolugardadatadenascimento.
OHTML5resolveparcialmenteesseproblemaadicionandoumnovotipode
campo input,específicoparadatas.Podemosusá-locomocódigoabaixo:
<label for="nascimento">Data de nascimento : </label>
<input id="nascimento" type="date" value="2010-02-08"/>
107

## Página 122

9.7. Escolhendoadatacomocalendário CasadoCódigo
Teremosumresultadocomoodafigura9.8. Deacordocomadocumenta ção
oficial[2],nãotemoscomoformataradata,alémdenãotermosgarantianenhumade
queobrowserdousuáriosuportaessenovoelemento.Atéadataemqueescreviisso,
apenasoChrome20,oumaisnovo,eoOpera11,oumaisnovo,exibiamcorretamente
ocampodata.OFirefoxnaversão18.0.2,oSafari6eoInternetExploreraindanão
reconhecemotipo date.
Figura9.8:CampoDatedoHTML5
Vocêpodetestarousodocomponentenoseubrowsernolinkabaixo:
http://jsfiddle.net/pbalduino/fz6Lk/
Paratermoscertezadequeobrowserdousuáriovaiexibircorretamenteoca-
lendário,vamosusarocomponente DatePickerdojQueryUI,queéumcalendário
altamenteconfigurávelecomvisualintegradoaotemaquevocêescolher.
Vamosabusardasop çõesdeconfigura çãoparaquevocêpossavercomodeixar
ocalendáriototalmenteemportuguêsecomonossoformatodedata.
Novamente, basta declarar uma caixa de texto no HTML. Vamos atribuir
nascimentoao id.
Casovocêtenhaseperguntado,esseelemento divcomaclasse ui-widgetfaz
comqueoseuconteúdoobede çaàformata çãodotemaescolhido.
<div class="ui-widget">
<label for="nascimento">Data de nascimento: </label>
<input id="nascimento" type="text">
</div>
108

## Página 123

CasadoCódigo Capítulo9. jQueryUI
ParaocódigoJavaScript,vamosusarométodo datepicker,querecebeumob-
jetocontendoasconfigura ções,quesãototalmenteopcionais.Claroquenãovaificar
tãolegalsevocênãopassarconfigura çãonenhuma,masvaifuncionardequalquer
maneira.
$(function () {
$("#nascimento").datepicker({
showWeek: true,
firstDay: 0 ,
dateFormat: "dd/mm/yy",
dayNames: ["Domingo",
"Segunda-Feira",
"Terça-Feira",
"Quarta-Feira",
"Quinta-Feira",
"Sexta-Feira",
"Sábado"],
dayNamesMin: ["D", "S", "T", "Q", "Q", "S", "S"],
monthNames: ["Janeiro",
"Fevereiro",
"Março",
"Abril",
"Maio",
"Junho",
"Julho",
"Agosto",
"Setembro",
"Outubro",
"Novembro",
"Dezembro"],
monthNamesShort: ["Jan",
"Fev",
"Mar",
"Abr",
"Mai",
"Jun",
"Jul",
"Ago",
"Set",
"Out",
"Nov",
109

## Página 124

9.8. Exibindojanelasdentrodajanela CasadoCódigo
"Dez"],
showButtonPanel: true,
currentText: "Hoje",
closeText: "Fechar",
weekHeader: "#"
});
});
Notequenocódigopedimosparaadicionarumacolunacomonúmerodase-
mana,traduzimostodososdiasdasemanaemesesdoano,nasformaslongaecurta,
mandamosexibirdoisbotõesnapartedebaixo,sendoqueumdelesmoveocalen-
dárioparaodiadehoje,edissemostambémqueasemanacome çanoDomingo(use
onúmero1sevocêquiserquecomecenaSegunda-Feira).
Podemosveroresultadonafigura9.9.
Figura9.9:Calendário
Vocêpodeverificartodasasop çõesdoDatePickernoendere çoabaixo:
http://api.jqueryui.com/datepicker/
9.8 E xibindo janelas dentro da janela
Épossívelexibirpequenasjanelasdentrodobrowser,chamadasde Dialogs,oucaixas
dediálogo.EssasDialogssãoúteisparaexibirmensagensdosistema,confirmara ções
110

## Página 125

CasadoCódigo Capítulo9. jQueryUI
oumesmoparaexibirdiferentesprocessamentosaomesmotempo,dependendoda
suanecessidadeecriatividade.
Vamosusarcomoexemploumamensagemdosistemaqueexigequeousuário
escolhaentreduasop ções.Primeirovamoscriarumelemento divquevaiguardar
todooconteúdodaDialog. Todootexto,imagemouqualqueroutrainforma ção
quevocêquerqueapareça,estarádentrodesse div.
<div id="dialog" title="Aviso do sistema" >
<p>Você acha que esse é o melhor
livro de JavaScript que já existiu? </p>
</div>
Emseguida,vamosusarométodo dialogparaconfiguraraDialog,passando
umobjetocontendoasconfigura ções. Nonossocaso,vamosinformarquetemos
doisbotões,cadaumexecutandoseuprópriocallback.Paramanterocódigolegível
efácildeentender,eusepareiasconfigura çõesnumavariável opcoes,ecrieiuma
funçãoparacadacallback.
Onossocódigovaificarassim:
$(function () {
function onSimClick() {
alert("Uhu! Você escolheu 'Sim'!");
$(this).dialog("close");
};
function onClaroClick() {
alert("\\o/");
$(this).dialog("close");
};
var opcoes = {
buttons: {
"Sim": onSimClick,
"Claro!": onClaroClick
}
};
$("#dialog").dialog(opcoes);
});
Ocódigocompletopodeserencontradonoendere çoabaixo:
111

## Página 126

9.9. OproblemacomojQueryUI CasadoCódigo
http://jsfiddle.net/pbalduino/s4X4B/
Veremosamensagemcomonafigura9.10
Figura9.10:AíousuárioapertaESC=(
Adocumentaçãocompletadessecomponentepodeserconsultadanoendere ço
abaixo:
http://api.jqueryui.com/dialog/
9.9 O problema com o jQueryUI
VocêjádeveterouvidoalguémcriticarojQueryeojQueryUIpor seremmuito
pesados.
Defato,sevocêbaixarabibliotecacompletacomalgumtemaparaasuaaplica-
ção,vocêpodeengordá-laematé300KBdesnecessariamente.
Sevocêestiverpensandoapenasemusuárioscombandalarga,navegadoresmo-
dernosecachesquefuncionam,oproblematododesapareceapósumoudoissegun-
dosamaisnacargadaaplica ção.
Porém,sevocêpensarqueemnossopaísabandalarganãoétãolargaassim,
queaquantidadedeusuáriosqueacessamaInternetatravésdedispositivosmóveis
estáaumentandoconsideravelmenteacadamêsequeaqualidadeeavelocidadeda
conexãooferecidapelasempresasdetelefoniaéumapiadademaugosto,chegaremos
àconclusãodequequantomenos,melhor.
SevocênãotemnecessidadedeutilizartemasdamaneiracomoojQueryUI
apresenta,eurecomendoquevocêentreemhttp://plugins.jquery.com/eprocure
poralternativasmaislevesparaoquevocêprecisa.
Emalgunscasosextremos,érecomendávelquevocêrepenseainterfacecomo
usuárioparaqueelafiqueleveefácildeusar.Serámesmoquevocêprecisadeuma
112

## Página 127

CasadoCódigo Capítulo9. jQueryUI
telacarregadadecomponenteseop ções,comosefosseumMicrosoftWordcom
todasasbarrasdeferramentas,ouvocêpoderiaapresentarasmesmasinforma ções
deumaformamaisinteligenteesimplificada?
Jáquefalamosemdispositivosmóveis,vamosfalarrapidamentesobrejQuery
Mobilenopróximocapítulo.
113

## Página 129

Capítulo10
jQueryMobile
“Nãouse.Simplesassim.”
–SérgioLopes
10.1 Enfrentando o mobile
Deacordocomo CiscoVisualNetworkingIndex [1],umrelatóriopublicadoanual-
mentepelaCisco,em2012presenciamosumaumentode81%nousodesmartpho-
nes. Deacordocomomesmorelatório,ovolumetrafegadoporsmartphonesno
mesmoanofoioitovezesmaiordoqueovolumedetodaaInternetnoano2000.
HáalgumtempoosdispositivosmóveisdeixaramdeserfigurantesnaInternet
parasetornarpartedodiaadiadedesenvolvedoresdeaplica çõesWeb,empresase
usuários.
Atentosaisso,osdesenvolvedoresdojQuerylan çaramemNovembrode2011a
primeiraversãoestáveldojQueryMobile,visandoatenderaocrescentemercadode
Internetmóvel.

## Página 130

10.1. Enfrentandoomobile CasadoCódigo
ParaquemjáutilizouojQueryUIouacompanhouocapítuloanterior,ojQuery
Mobilenãovaicausarnenhumasurpresa.
Figura10.1:jQueryMobileacessadodeumcelular
AocontráriodoqueacontececomojQuerypuroemrela çãoaosnavegadores
116

## Página 131

CasadoCódigo Capítulo10. jQueryMobile
maisutilizados,ojQueryMobilenãogarantequesuaaplica çãoousitevãoserexe-
cutadoscorretamenteemtodososdispositivos.Vocêpodeacessaroendere çoabaixo
paraverificarquaisdispositivossãocompatíveiscomabiblioteca:
http://jquerymobile.com/gbs/
ApáginainicialdojQueryMobile(http://jquerymobile.com/)ofereceumafer-
ramentaparaquevocêpossaexperimentarosdiversoscomponentesnumsimulador
dedispositivomóvel.
AssimcomoacontececomojQueryUI,ojQueryMobiletambémtemo Theme
Roller,paraquevocêcrieseusprópriostemasedeixeaaplica çãocomascoresque
vocêquiser.
O Theme Roller para jQuery Mobile está em http://jquerymobile.com/
themeroller/
10.2 Cuidado com o tempo de carregamento
Casovocêestejautilizandoumaaplica çãoempacotadacomumaferramentacomo
oPhoneGap,otempodecarregamentonãoéalgopreocupante,umavezquetodos
osseusarquivosjáestarãoinstaladosnoseuaparelho.Oproblemaexiste,eégrave,
quandovocêestiverusandojQueryMobileparadesenvolveroseusite.
OjQueryMobiletambémofereceumaop çãoparaquevocêfa çaodownload
apenasdaquiloqueforrealmentenecessário.Acesseolinkabaixoparaexperimen-
tar:
http://jquerymobile.com/download-builder/
Sóqueissoaindanãoresolveoproblema. Pormaisenxutaquesejaasuains-
talaçãodojQueryMobile,vocêaindaéobrigadoacarregartodoopesodojQuery,
queaindanãoémodularizadoecontémquilosdecódigoque,possivelmente,você
nuncavaiprecisar.
SérgioLopes,instrutordaCaelum,escreveuumartigomuitobom,noblogda
Caelum,sobreospontosnegativosdeseutilizarjQueryMobile[13].Tomeialiber-
dadedecitarotrechodesseartigoemqueeleapresenta,deformaconcisa,umbom
motivoparanãousarmosjQueryemsitesparadispositivosmóveis.
“[ComojQuery]são32KBdedadosgzipadosparasetransferirnumarede
potencialmenteruimcomo3G.Equandoosdadoschegam,ocupam95KBsemgzip
(mesmominificado).Etudoissotemqueserlidoeparseadoantesmesmodese
pensaremexecutarseucódigo.AsestatísticasdecarregamentodojQueryem
117

## Página 132

10.2. Cuidadocomotempodecarregamento CasadoCódigo
dispositivosmóveissãoassustadoras.NumiPad2topodelinha,sóoparsingeevaldo
jQuerydemora5xmaisquenoDesktop.UmiPhone3,que,apesardeantigo,émelhor
queamaioriadoscelularesqueaspessoastêmemseubolso,demoraincríveis850ms.
EmesmoumiPhone4gastaumaeternidadesecomparadoaoDesktop–320msvs.
35ms.”
–SérgioLopes
Comoalternativa,podemosusarumaferramentachamadaZepto.js,quepode
serencontradanoendere çoabaixo:
http://zeptojs.com/
Praticamentetudooquevocêaprendeusobreseletores,callbacks,AJAXeeven-
tospodeseraplicadonoZeptoJS,comavantagemdeterumarquivoquatrovezes
menorparabaixaratravésdeumaredeproblemática(90.5KBdojQuery1.9.1contra
23.5doZepto1.0rc1).
Éclaroquenãoexistebaladeprataeque,emalgunscasosoZeptosimplesmente
nãovaisersuficienteparasubstituirojQuery.
Apesardevocêjáterlidoissoantes,umasaídamaisefetivaérepensarasuainter-
face,tornando-amaissimplesedireta,utilizandoJavaScriptpuroondeforpossível.
Quandonãoforpossívelselivrardousoumabiblioteca,experimenteousode
microframeworkscomooHammer.js,disponívelemhttp://eightmedia.github.com/
hammer.js/,oualgumdalistado microjs,disponívelemhttp://microjs.com/.
Independentedaferramentaquevocêqueirautilizar,tenhasempreemmente
queodesenvolvimentoparaWebparadispositivosmóveisémuitosemelhanteao
quetínhamoshádezouquinzeanos,quandoaspessoasutilizavamdiscadoresem
linhastelefônicasesimplesmentenãopodiam,enãoqueriam,esperardezsegundos
paraqueumapáginafossecarregada.
118

## Página 133

Capítulo11
OrientaçãoaobjetosnoJavaScript
“JavaScriptéumalinguagemcriadasemmuitocuidado,masdentrodelaháuma
linguagemeleganteemuitomelhor.”
–DouglasCrockford
11.1 Objetos noJav aScript
ApesardeJavaScriptserumalinguagemorientadaaobjetos,oconceitodeobjeto
éumpoucodiferentedoquevocêpodeestaracostumado. Emespecialseveiode
linguagenscomoJava,C #,C++,Ruby,Pythonououtralargamentedifundidano
mercado.
Primeiramente,nãoexisteoconceitode classesnoJavaScripttalcomooconhe-
cemosnaslinguagensquecitei,entãovocênãoprecisadeumaclasseparacriarseus
objetos.
Emsegundolugar,oquenormalmentetratamoscomoobjetosnoJavaScriptnão
sãonecessariamenteobjetos,masfun çõescompropriedades. Eosobjetosquesão
realmenteobjetossãodiferentesdosobjetosdeoutroslinguagens.

## Página 134

11.1. ObjetosnoJavaScript CasadoCódigo
Agoraqueeuconfundioquevocêjásabia,voumostrarpassoapassoquenãoé
nadadisso.
Umobjetosimples
OjeitomaissimplesdecriarmosumobjetoemJavaScriptéutilizandoum dici-
onário,ousepreferir,mapaouhashtable.Nósutilizamosobjetosassimduranteos
capítulosemquefalamossobreJSONeAJAX,etambémparapassarmosconfigura-
çõesparaosmétodosdojQueryMobile.
Oobjetomaissimplesquepodemoscriarésimplesmenteo { }.Elenãofaznada,
nemguardavalornenhum,maspodemosadicionarfuncionalidadesneleconforme
asnossasnecessidades.
var simples = { };
simples.nome = "Plínio";
simples.oi = function() {
console.log("Olá, " + this.nome + "!");
}
simples.oi();
Oresultadopodeservistonafigura11.1.
Figura11.1:Oi!
Percebaque,exatamenteporestarmoslidandocomumdicionário,podemos
adicionarpropriedadesemétodosaonossoobjetoaqualquermomento.ParaoJa-
vaScript,umobjetoéapenasumdicionáriocontendochavesevalores.
Podemosreescreverocódigoacimadaformaabaixo,oqueparecemaisfamiliar
paraquemvemdelinguagenscomorienta çãoaobjetosbaseadasemclasses:
var outro_simples = {
nome: "Plínio",
120

## Página 135

CasadoCódigo Capítulo11. OrientaçãoaobjetosnoJavaScript
oi: function() {
console.log("Olá, " + this.nome + "!");
}
};
outro_simples.oi();
Percebaque,nosdoiscasos,foinecessáriousar thisparaacessarmosoconteúdo
de nome.Issoindicaquedevemosprocurar,dentrodoobjetoatual,porumavariável
oupropriedadechamada nome.Sevocênãousar this,oJavaScriptvaiprocurarpor
umavariávelchamada nome,oquenãoexistenonossocódigo.
Daformacomocriamosoobjeto,épossíveltambémqueonomesejaalterado,
bastandoacessar outro_simples.nome,comovemosnafigura11.2. Sequisermos
protegerovalorde nomeenãopermitirqueousuárioaltereovalordapropriedade,
teremosproblemas,jáqueasintaxedodicionárionãopermitequecriemosuma
variávelalidentro.
Figura11.2:Um’olámundo’maisbacana
Outroproblemaquepodemosencontrarusandoessaabordageméquenãohá
umamaneiradetermosdoisobjetosdomesmotipoquemantenhamseusvalores
isoladossemrepetirquasetodoocódigo.
Imaginequetemosdoisfuncionários. Cadaumtemseupróprionome,cargo
esalário.Vamostentarimplementarissocomoqueaprendemossobreobjetosaté
agora.
var paulo = {
nome: "Paulo",
cargo: "Analista de Sistemas" ,
salario: 5000
};
Aoexibirmosonomedoobjeto paulo,teremosasaídajáesperadanafigura11.3.
121

## Página 136

11.1. ObjetosnoJavaScript CasadoCódigo
Figura11.3:OnomedepauloéPaulo
Agoraimaginequeousuárionãoquerrepetirtodoocódigousadoparacriaro
objeto pauloetentefazerumacópiaparaoobjeto pedro.Nacabe çadele,cadaobjeto
continuarásendoúnicoeassim,elepoderáfazerquantascópiasforemnecessárias
paraquetodososfuncionáriosdaempresasejammapeados.
Entãoousuáriofazoseguinte:
var pedro = paulo;
pedro.nome = "Pedro";
pedro.cargo = "Gerente de contas" ;
pedro.salario = 4500 ;
Aoexibirovalorde nomede pedro,ousuáriorecebeu“Pedro”devolta.Excelente,
não?
Mas,aoexibirovalorde nomede paulo,eleteveumasurpresacomoadafigura
11.4.
Figura11.4:OnomedepedroéPedro.Eodepaulo?
Claro!issoacontecepoisa varguardaumareferênciaaoobjeto,enãooobjeto
emsi.
Masesequiséssemoscriarumnovoobjetoquejápossuaasmesmasfun çõese
atributosdeoutroobjeto?Issoé,comofazeralgoparecidocomumaclasse?
122

## Página 137

CasadoCódigo Capítulo11. OrientaçãoaobjetosnoJavaScript
11.2 Funções para quem não tem classe
EmJavaScriptnãoexisteoconceitodeclasses,masasfun çõespodemmuitobem
assumiressepapel,oquesignificaquepodemoscriarobjetosapartirdefun ções.
Vamosreescreveronossoprimeiroexemplo,odo "Olá,fulano!”,usandouma
funçãoaoinvésdeumdicionário.
function OlaSimples() {
this.nome = "Plínio";
this.oi = function() {
console.log("Olá, " + this.nome + "!");
}
}
Vamosinstanciarumobjeto simplesparademonstrarcomopodemosusaresse
objeto.Aessafun çãousadaparacriarumobjetochamamosde Construtor.Notea
semelhançacomoJava,C #ouC++:
var simples = new OlaSimples();
simples.oi();
Figura11.5:Umolácomcaradeorienta çãoaobjetos
Sequisermosalteraronome,aindapodemosacessarapropriedade nome. Po-
rém,aocontráriodoexemploanterior,podemosesconder nomeparaqueseuvalor
nãopossaseralterado.Paraisso,devemosdeclararapropriedade nomecomouma
variável.
function OlaSimples(seuNome) {
var nome = seuNome;
this.oi = function() {
console.log("Olá, " + nome + "!");
}
123

## Página 138

11.2. Funçõesparaquemnãotemclasse CasadoCódigo
}
simples = new OlaSimples("Plínio");
simples.oi();
Nafigura11.6vocêpodeseroresultadodonossocódigo.Agoraonomesópode
serdefinidonacria çãodoobjeto. Aessapropriedadedepodermosguardarasin-
formaçõesdentrodeumobjetoe,eventualmente,escondê-lasdomundoexterior,
chamamosdeencapsulamento,eéumdosconceitosfundamentaisdaorienta çãoa
objetos.
Figura11.6:Umolácomparâmetronoconstrutor
Umacaracterísticadoencapsulamentoéquecadaobjetoguardasuaspróprias
informações,fazendocomqueaaltera çãoemumobjetosejainvisívelaosdemais
objetos.Vamosusaroexemplodosfuncionáriosparaexemplificar.
Primeiro,vamoscriarumconstrutorparaosobjetosquesimbolizamosem-
pregados. Nãovamosnospreocuparcomofatodepodermosalterarosdadosdo
funcionárioapóscriarmosoobjeto,poisagoravocêsabecomoalteraroconstrutor
paraqueasinforma çõessejamalteradassomentequandovocêquiser:
function Funcionario(nome, cargo, salario) {
this.nome = nome;
this.cargo = cargo;
this.salario = salario;
}
var paulo = new Funcionario("Paulo", "Analista de sistemas" , 5000);
var pedro = new Funcionario("Pedro", "Gerente de contas" , 4500);
console.log("O nome de paulo é " + paulo.nome);
console.log("O nome de pedro é " + pedro.nome);
124

## Página 139

CasadoCódigo Capítulo11. OrientaçãoaobjetosnoJavaScript
Comopodemosvernafigura11.7,cadaobjetotemseusprópriovalores,eum
nãoinfluencianooutro,queéexatamenteoqueesperamosaolidarcomobjetos.
Figura11.7:pauloéPaulo,pedroéPedro
Notequenãofoiprecisorepetircódigoparacriarmosdoisobjetosdistintos,mas
domesmotipo.
11.3 Entendendo prototipação
OJavaScriptéumalinguagemquefazusode prototipação,oquesignificaque,ao
invésdetermosumaclasseherdandocaracterísticasdeoutraclasse,osobjetosher-
damsuascaracterísticasdeoutrosobjetos.
Vamosusaroexemplodosfuncionáriosparaexemplificarcomousarprototipa-
çãousandoJavaScript.
VamoscriarumconstrutorFuncionario,semnenhumapropriedadeoumétodo.
Conformeoesperado,setentarmosacessaronome,cargoousalário,queaindanão
existem,receberemos undefined,comopodemosvernafigura11.8
function Funcionario() {
};
var paulo = new Funcionario();
console.log(paulo.nome, paulo.cargo, paulo.salario);
Figura11.8:Ofuncionárioanônimo
Usandoocódigoacima,vamosusarprototipa çãoparaadicionarcaracterísticas
aobjetosquejáexistem.
125

## Página 140

11.3. Entendendoprototipação CasadoCódigo
Funcionario.prototype.nome = "<sem nome>" ;
Funcionario.prototype.cargo = "<sem cargo>" ;
Funcionario.prototype.salario = NaN;
Vamosexibirnovamenteoqueofuncionário paulotem:
console.log(paulo.nome, paulo.cargo, paulo.salario);
Agoraaspropriedadesde Funcionarioexistem,comopodemosvernafigura
11.9,econtémvalorespadrãoquevocêpodealterarconformesuasnecessidades.
Figura11.9:Ofuncionáriopadrão
Reparequeusando prototypevocêpodeadicionarcaracterísticasemtodosos
objetosqueforemcriadoscomoconstrutor Funcionarioemesmonosquejáha-
viamsidocriados.
Aquivocêdeveestarseperguntandoqualavantagemdessatalprototipa ção.
Umadasprincipaisvantagenséapossibilidadedepoderadicionarcaracterísticasa
classesjáexistentes,fazendocomqueseucódigofiquemaislimpoereutilizável.
Vamosimaginarquevocêqueiraquecadanomedeumalistatenhaaprimeira
letraemmaiúsculaeasdemaisminúsculas.VamosverseoJavaScriptjánosfornece
algoassim:
var lista = ["vermelho", "marrom", "azul", "preto", "amarelo"];
lista.capitalize();
Comoométodo capitalizenãoexiste,receberemosoerrodafigura11.10.
Figura11.10:Nãoexisteométodocapitalize
126

## Página 141

CasadoCódigo Capítulo11. OrientaçãoaobjetosnoJavaScript
Vocêpodefazerdeforma procedural,criandoumafun ção capitalizequere-
cebeumalistacomoparâmetroeretornaoutralistacomaprimeiraletradecada
nomeemmaiúscula:
function capitalize(list) {
var resultado = new Array();
for(var pos = 0 ; pos < lista.length; pos ++) {
var primeiro = lista[pos].slice(0, 1);
var resto = lista[pos].substr(1);
resultado.push(primeiro.toUpperCase() + resto);
}
return resultado;
}
Agorapodemoschamarafun ção capitalizepassandoamesmalistacomopa-
râmetro.Funciona,masnãoestamosusandoorienta çãoaobjetosaqui.
var lista = ["vermelho", "marrom", "azul", "preto", "amarelo"];
capitalize(lista);
Podemosveroresultadonafigura11.11.
Figura11.11:Usandoumafun ção
Umproblemaquetemosaquiéqueafun ção capitalize,apesardetersidofeita
paratrabalharcom Arrays,aceitaqualquercoisacomoparâmetro,podendocausar
errosestranhosequepodemserdifíceisdeencontrar.
Usandoprototipação,podemosfazercomqueum Arraytenhaummétodocha-
mado capitalize.Executandoomesmocódigodafigura11.10,receberemosuma
listacomaprimeiraletradecadanomeemmaiúscula,aoinvésdeumerro.
Array.prototype.capitalize = function() {
var resultado = new Array();
127

## Página 142

11.4. Usandoherança CasadoCódigo
for(var pos = 0 ; pos < this.length; pos ++) {
var primeiro = this[pos].slice(0, 1);
var resto = this[pos].substr(1);
resultado.push(primeiro.toUpperCase() + resto);
}
return resultado;
}
Finalmentepodemosexecutarométodo capitalizepararetornaralistadojeito
quequeremos,comopodemosvernafigura11.12. Alémdeestarmosusandouma
abordagemrealmenteorientadaaobjetos,podemostercertezadequesempreesta-
remostrabalhandoemcimadeumalista,evitandoerroscausadosporalgumtipo
dedadoerrado.
Figura11.12:Usandoummétodo
Comocautelaecaldodegalinhanuncafizerammalaninguém(apesardenin-
guémterpedidoaopiniãodagalinha),nãoédemaislembrarquealterarqualquer
objetopadrãodalinguagemétãoperigosoquantopoderoso.Vocêpodefacilmente
quebrarcompletamenteasuaaplica çãoalterandoumobjetoqueéusadoporbibli-
otecasdeterceiros.
“Comgrandespoderesvêmgrandesresponsabilidades”
–BenjaminParker
11.4 Usando herança
Comoagoravocêjásabecomocriarobjetosusandoumconstrutorejásabecomo
usarprototipação,porquenãoaprendertambémacomosimularheran çaclássica
comJavaScript?
Afigura11.13éumdiagramadeclasses.
128

## Página 143

CasadoCódigo Capítulo11. OrientaçãoaobjetosnoJavaScript
AtravésdelepodemosverquetodoMamíferoéumAnimal,etodoGatoéum
Mamífero.Porinferência,podemosdizerquetodoGatoéumAnimal,certo?
IssosignificaqueaclasseGatoherdatodasascaracterísticas,propriedadesemé-
todosdasclassesMamíferoeAnimal.Chamamosissode‘heran çaclássica’.
Figura11.13:Umgatoéumanimal
Se,conformejáfoidito,JavaScriptnãotemclasses,comopodemosusarheran ça
clássica?
Simples. Comofoiexplicadoaofalarmossobreprototipa ção,vamosherdaras
característicasdeoutroobjetoparasimularaheran çaclássica.
Primeiro,vamoscriarumconstrutor Animal.Um animaltemcomocaracterís-
ticaasa ções comere respirar.
function Animal() {
129

## Página 144

11.4. Usandoherança CasadoCódigo
this.comer = function() {
console.log("Eu como" );
};
this.respirar = function() {
console.log("Eu respiro" );
};
}
var animal = new Animal();
animal.respirar();
Figura11.14:ImplementandoumAnimal
Agoravamoscriarumconstrutor Mamifero,quetemcomocaracterísticaaa ção
de mamar.Aimplementa çãoébemparecidacomafun ção Animal:
function Mamifero() {
this.mamar = function() {
console.log("Eu mamo" );
}
}
Nafigura11.15podemosverqueométodo mamaréexecutadocorretamente,mas
nossomamíferonãocome.Seeleéumanimal,éesperadoqueelecoma.
130

## Página 145

CasadoCódigo Capítulo11. OrientaçãoaobjetosnoJavaScript
Figura11.15:Sóqueelenãocome
Comopodemosfazerparaqueonosso Mamiferoajacomoum Animalsemque
tenhamosquereescreverocódigo?Arespostaestánoprotótipo.
Vamosusaroqueaprendemossobreprotótiposparaherdarascaracterísticasde
Animal:
Mamifero.prototype = new Animal();
mamifero = new Mamifero();
mamifero.mamar();
mamifero.comer();
mamifero.respirar();
Agoraonossomamíferomamacomoqualquer Mamifero,comeerespiracomo
qualquer Animal.Podemosverissonapráticapelafigura11.16.
Figura11.16:AgoraonossoMamiferoéumAnimal
Vamosfazeromesmocom Gatoe Cachorroparacomprovarmosseum Gatoe
um Cachorrocontinuamcomascaracterísticasde Animal. Vamosalterarocom-
131

## Página 146

11.4. Usandoherança CasadoCódigo
portamentodométodo comerdo Cachorro. Aissochamamosde sobrescritade
métodooumethodoverride.
function Gato() {
this.miar = function() {
console.log("Miau!");
}
}
Gato.prototype = new Mamifero();
function Cachorro() {
this.latir = function() {
console.log("Au au!" );
}
this.comer = function() {
console.log("Eu como ração" );
}
}
Cachorro.prototype = new Mamifero();
var bichano = new Gato();
var rex = new Cachorro();
Agora,nafigura11.17vamosdemonstrarqueum Gatoéum Mamiferoeum
Animal.
Figura11.17:GatofazendocoisasqueGatofaz
132

## Página 147

CasadoCódigo Capítulo11. OrientaçãoaobjetosnoJavaScript
Enafigura11.18demonstramosque,alémde Cachorroser Mamiferoe Animal,
tambémmudamosocomportamentodométodo comer.
Figura11.18:Cachorroensinandooverride
11.5 Mixin noJav aScript
Mixinéumaformadeadicionarcomportamentosecaracterísticasaumaclassejá
existente,evitandoquevocêtenhaquereescreveromesmocódigováriasvezesem
lugaresdiferentes.Mixintambémpodeserconsideradocomoumaformadeseim-
plementarherançamúltipla,queéquandoumaclasseherdaascaracterísticasde
maisdeumaclasseaomesmotempo.Nafigura11.19podemosvercomoissofunci-
onanaprática.
Assimcomonafigura11.13, quevimosnase çãoanterior, temosumaclasse
Mamiferoqueherdaascaracterísticasecomportamentosde Animal.
133

## Página 148

11.5. MixinnoJavaScript CasadoCódigo
Figura11.19:Herançamúltiplaéumaconfusãosó
Comovocêjádeveterimaginado,oJavaScriptnãoimplementaheran çaclássica
e,comisso,tambémnãodásuporteaheran çamúltipla.
Oquevocênãodeveterimaginadoéque,sendooJavaScriptumalinguagemtão
poderosaeflexível,épossívelquevocêmesmoaprogrameparapermitirousode
herançamúltiplanaformademixin.
ComotodososobjetosdoJavaScriptherdamascaracterísticasde Object,vamos
criarummétodo includesnoprotótipode Objectparaquevocêpossausá-locom
todososobjetosdoJavaScript.
Vamosfazeressemétodoaceitarumparâmetrochamado constructor,quere-
presentaoobjetodeondevocêquerherdaroscomportamentosepropriedades.
Object.prototype.includes = function (constructor) {
};
Comojásabemos,umobjetoherdaascaracterísticasdeoutroobjeto,entãote-
mosquecriá-loapartirdoconstrutorquerecebemosporparâmetro:
var objeto = new constructor();
Agoravemapartequefaztodootrabalhopesado.
134

## Página 149

CasadoCódigo Capítulo11. OrientaçãoaobjetosnoJavaScript
Vamosusarum forparapegarcadaumadaspropriedadesquequeremosherdar
paraonossoobjeto.Vamosusarométodo hasOwnPropertyparatermoscertezade
queapropriedadequevamosherdarvemmesmodoconstrutorquerecebemospor
parâmetro. Seoconstrutorherdoualgumacaracterística,vamosignorá-la. Você
podeignoraressepasso,sesouberoqueestáfazendo.
Emseguida,vamosadicionarapropriedadeaoprotótipodonossopróprioob-
jeto.LembraquandodissemosqueobjetosJavaScriptsãodicionários,equedicio-
náriospodemseracessadoscomoArrays,sóquecomqualquertipodevalorcomo
chave?Poisfoiexatamenteoquefizemos,passandoonomede propriedadecomo
sendoachaveecopiandoapropriedadeaserherdadaparadentrodonossoobjeto.
for (var propriedade in objeto) {
if (objeto.hasOwnProperty(propriedade)) {
this.prototype[propriedade] = objeto[propriedade];
}
}
Onossocódigovaificarassim:
Object.prototype.includes = function (constructor) {
var objeto = new constructor();
for (var propriedade in objeto) {
if (objeto.hasOwnProperty(propriedade)) {
this.prototype[propriedade] = objeto[propriedade];
}
}
};
Vamoscriaronossoconstrutor Animal:
function Animal() {
this.comer = function() {
console.log("Eu como" );
};
this.respirar = function() {
console.log("Eu respiro" );
};
}
135

## Página 150

11.5. MixinnoJavaScript CasadoCódigo
Vamoscriarumconstrutorpara Peixe,lembrandoquetodo PeixeéumAnimal.
Vamossobrescreverométodo respirareassimsabermosquetudoestáfuncio-
nandoconformeoprevisto:
function Peixe() {
this.respirar = function() {
console.log("Eu respiro embaixo d 'água");
};
}
Peixe.prototype = new Animal();
var peixe = new Peixe();
peixe.nadar();
Figura11.20:Essepeixeaindanãonada
Queremosqueonosso Peixenade,oqueaindanãoacontece,comopodemos
vernafigura11.20.Podemosescreverummétodo nadardentrode Peixe,edepois
repetirocódigonoconstrutor Baleia(queaindanãoescrevemos,masestánodia-
gramadeclasses),queé Mamifero,oupodemoscriarumconstrutor Nadador.
function Nadador() {
this.nadar = function() {
console.log("Eu nado" );
}
}
Noteque Nadadoréumconstrutorcomum,semnadadeespecial.Vamosusar
aquelemétodoincludesparaincluirascaracterísticasde Nadadornosnossosobje-
tosdotipo Peixe.
Peixe.includes(Nadador);
136

## Página 151

CasadoCódigo Capítulo11. OrientaçãoaobjetosnoJavaScript
var peixe = new Peixe();
peixe.nadar();
Agorasim.Comopodemosvernafigura11.21,onossopeixerespiracomoum
Animal,enadacomoum Nadador. Usandomixin,herdamosascaracterísticasde
doisobjetosdiferentesdentrode Peixe.
Figura11.21:Essepeixeaindanãonada
Agoraquevocêjásabecriarobjetosetrabalharcomencapsulamento,prototi-
pação,heran çaemixin,vamosaproveitaropróximocapítuloeaprendertambéma
usarprogramaçãofuncionalcomJavaScript.
137

## Página 153

Capítulo12
Umpoucodeprograma ção
funcional
“JavaScriptéLISPdisfarçadodeC”
–DouglasCrockford
12.1 Oque é programação funcional
Programaçãofuncionalé,assimcomoaorienta çãoaobjetos,umaformadesepensar
emcomoresolverproblemas.
Abasedoquehojeéaprograma çãofuncionalfoicriadaparalelamenteporAlan
TuringeAlonzoChurchnadécadade1930,antesmesmodaexistênciadoscompu-
tadorescomooconhecemos[12].
Infelizmente,aprograma çãofuncionalpassoumuitotemporestritaaosmeios
acadêmicos,oquefazcomqueoiniciantenoassuntofiqueassustadocomtoda
aquelanotaçãomatemáticaecomostermosincompreensíveis.

## Página 154

12.2. Highorderfunctions CasadoCódigo
Figura12.1:Notaçãomatemáticaassusta
Paranossasorte,oconceitodeprograma çãofuncionalémuitosimples.Assim
comonaorienta çãoaobjetosamenorpartedeumsistemaéumobjeto,vocêpode
atribuirobjetosavariáveis,podepassá-losporparâmetroetermétodosretornando
objetos,naprograma çãofuncionalamenorpartedoseusistemaéumafun ção.
Issoimplicaquevocêpodeatribuirfun çõesavariáveis,podepassá-lasporparâ-
metroemesmofazercomqueumafun çãoretorneoutrafun ção.Algumalinguagens
implementamtambémimutabilidade,queéquandotodovalorétratadocomose
fosseumaconstante,eoutrosconceitosperiféricos,masnãoéocasodoJavaScript.
Todososdemaisconceitosdeprograma çãofuncionalderivamdofatodevocêlidar
comfunçõescomosefossemumvalorcomoqualqueroutro.
12.2 High order functions
Umahighorderfunction(nãoacheiumatradu çãodecenteparaoPortuguês),ape-
sardonomeintimidador,ébasicamenteumafun çãoquerecebeoutrafun çãocomo
parâmetrooudevolveumafun çãocomoresultado.Quandovocêusacallbacksno
JavaScriptenojQuery,vocêestáfazendousodehighorderfunctions.
$("button.mallandro")
.click(function() {
alert("Ié ié!" );
});
Ométodo clickéumahighorderfunction,eafun çãoanônimaquefaz Iéié!é
umcallback.
Sim,estamosapenasdandonomesaartifíciosquejáestamosutilizandoháum
bomtempo.
140

## Página 155

CasadoCódigo Capítulo12. Umpoucodeprogramaçãofuncional
12.3 Escopo
Apesardoconceitodeescoponãoserexclusivodaprograma çãofuncional,éimpor-
tantíssimoquevocêentendacomofuncionaoescoponoJavaScriptparaquenão
fiqueconfusoaover closuresecurrying.
Comonamaioriadaslinguagenscomerciais,umavariáveldeclaradaemumes-
copomaiorévisívelemumescopomenor,enquantoocontrárionãoéverdadeiro.
Napráticasignificaqueumavariávelglobalévisívelportodomundo:
var x = 1 ;
function variavelGlobal() {
console.log(x);
}
variavelGlobal();
Figura12.2:Valordexnãomuda
Significatambémqueumavariávellocalsóévistadentrodoescopoemquefoi
criada,mesmoquetenhaomesmonomedeumavariávelglobal:
var x = 1 ;
function variavelLocal() {
var x = 99 ;
var y = 42
console.log(x, y);
}
variavelLocal();
console.log(x);
console.log(y);
141

## Página 156

12.3. Escopo CasadoCódigo
Figura12.3:Valorlocaldex
Quandoumafun çãoalteraovalordeumavariávelglobal,issoafetatodaaapli-
cação.Porissoousodevariáveisglobaisnãoéconsideradoumaboaprática.Porém,
umavariávelglobalpassadaporparâmetroparaumafun çãonãotemoseuvaloral-
terado:
var x = 1 ;
var y = 11 ;
function incremento(x) {
console.log("Dentro: " , x, y);
x++;
y++;
console.log("Dentro: " , x, y);
}
incremento(x);
// Dentro: 1 11
// Dentro: 2 12
console.log("Fora: " , x, y);
// Fora: 1 12
142

## Página 157

CasadoCódigo Capítulo12. Umpoucodeprogramaçãofuncional
Figura12.4:Variávelglobalsendoalterada
12.4 Closures
Outracaracterísticadoescopoéqueumafun çãoguardaasvariáveisdocontextoem
quefoicriada.Issosignificaqueumafun çãopodecontinuaracessandovariáveisque
sóexistiamnomomentoemqueelafoicriada.
function counter() {
var x = 0 ;
return function () {
return ++x;
}
}
var count = counter();
console.log(count());
console.log(count());
console.log(count());
console.log(count());
console.log(x);
143

## Página 158

12.5. Currying CasadoCódigo
Figura12.5:Contadorusandoclosure
Oqueaconteceaquiéque countrecebeumafun çãoqueincrementaovalor
davariável x,sóqueessavariávelexisteapenasdentrodafun ção counter. Oque
aconteceuaquiéqueafun çãoarmazenadaem countselembra davariávelquefoi
criadaemoutrafun ção,masquenãoestámaissendoexecutada.
Aotentarmosexibirovalordavariável x,recebemosumerro,poiselanãoexiste
noescopoglobal,comopodemosvernaimagem12.5.
12.5 Currying
Juntandotudooquevimosatéaquisobrehighorderfunctions,escopoeclosures,
chegamosao currying.Curryingéumaopera çãoemquevocêtransformaumafun-
çãoquereceberiamaisdeumparâmetroemumasériedechamadasdefun çõescom
apenasumparâmetrocada.
Umdosusosdessatécnicaéevitar,deformaelegante,queomesmoparâmetro
sejapassadoparaamesmafun ção.
Vamospegarumexemploescritodeformaimperativa.Temosumafun ção hey,
querecebeosparâmetros textoe nomee,apartirdisso,imprimeumasauda ção.
function hey(texto, nome) {
console.log(texto + ", " + nome);
}
144

## Página 159

CasadoCódigo Capítulo12. Umpoucodeprogramaçãofuncional
hey("Bom dia" , "João");
hey("Bom dia" , "José");
hey("Bom dia" , "Nicolau");
Figura12.6:Bomdiaimperativo
Vocêpodedizerquepoderíamosguardar Bomdia emumavariável.Concordo,
masissonãomudarianadadentrodoqueestamosapresentando.
Emalgumaslinguagens,curryingéalgonaturalepodeserfeitodeformatrans-
parente.NoJavaScriptprecisamosfazermanualmente,masissotornaacoisatoda
maisfácildesercompreendida.
Reescrevendoamesmafun çãousandocurrying,teremosocódigoabaixo:
function hey(texto) {
return function (nome) {
console.log(texto + ", " + nome);
}
}
var bomDia = hey("Bom dia" );
bomDia("João");
bomDia("José");
bomDia("Nicolau");
145

## Página 160

12.5. Currying CasadoCódigo
Figura12.7:Bomdiafuncional
Programaçãofuncionalémuitomaisdoqueosconceitosqueapresenteiaqui,
mascomoumprimeirocontatojádáparafazermuitacoisabacana.
Recomendoquevocêestudeepesquisearespeito.Mesmoquevocênãouseuma
linguagemfuncionalnoseudia-a-dia,ofatodeconhecerumnovomododepensar
acabaalterandoaformacomovocêresolveproblemas,fazendocomquevocêtenha
ideiasmelhoresemaiselegantes.
Hálinguagensquevãolevaralgunsdessesconceitosparadentrodelamesma,
tornandocurrying,closureeoutrosartifícioscompletamentetransparente.
Agoraquevocêjádominaorientaçãoaobjetoseprograma çãofuncionalnoJa-
vaScript,criarseusprópriospluginsnojQueryvaiparecerbrincadeiradecrian ça.E
éexatamenteissoquevamosfazernopróximocapítulo.
146

## Página 161

Capítulo13
CriandopluginsparajQuery
“Porfavor,nãotentedeixaroseucódigoilegível.Eugarantoqueeleficaráilegívelo
bastantesemquevocêseesforce.”
–“Cowboy”BenAlman
13.1 Oque são plugins?
OjQuerynãofoidesenvolvidopararesolvertodososproblemas,imaginadosounão,
queumdesenvolvedorpodeencontraraocriarumaaplica çãoparaWeb.
Aoinvésdedesperdi çartempoeesfor çonessatarefaimpossível(oquealguns
frameworksfamososcontinuamtentandofazer),JohnResigeosdesenvolvedores
dojQueryresolveramcriarumnúcleobemdefinidoefacilmenteextensível.
Comisso,qualquerumcomumpoucomaisdecuriosidadepodeutilizarabase
queojQueryforneceparacriarmétodosqueresolvamseusproblemas.Essesméto-
dossãointegradosdetalformaaojQueryquepassamasertratadoscomosefossem
partedabiblioteca.Cadaconjuntodemétodosdesseséchamadodeplugin.

## Página 162

13.2. Aanatomiadeumplugin CasadoCódigo
UmdosmotivosparaojQuerysertãopopularéaimensaquantidadedeplu-
ginsdesenvolvidospelacomunidadeeempresasespecializadas. Existemplugins
paraquasetudooquevocêimaginare,senãoexistir,vocêpodemuitobemcriar
ecompartilhar.
Paratodososcódigoseexemplosquevamosapresentaraqui,énecessárioque
vocêincluaojQuerynoseuHTMLounojsFiddle.
13.2 Aanatomia de um plugin
Umpluginéumobjetoquevocêagregaaoobjeto jQuery,equedeveseguiralgu-
masboaspráticasparamanterumaboarela çãocomosoutrosmilharesdeplugins
existentes.
Algumasdessasboaspráticassãotidascomopadrãopelosdesenvolvedorese
usuáriosmaisexperientes.Outrassãoapenasquestãodebomsensoesurgemdepois
devocêcansardeterpluginsdandoproblemaemprodu çãoeentrandoemconflito
comoutrospluginsoubibliotecas.
AprimeiracoisaquevocêdevesabersobreumpluginjQueryéquetodasas
chamadas,consultaseconfigura çõesdeumplugindevemserfeitasatravésdeum
únicométodo.
Usandocomoexemploumdosprimeirospluginsquedesenvolvi,voudemons-
traramaneiraerradadeusarequeacabasendofeitapormuitosincautosdesenvol-
vedores.
Oplugin,quevamoschamarde jeitoErradotemumaop çãoparaseraplicado
eoutraop çãoparaserremovido.
Ojeitoerradoconsisteemcriarummétodoparacadaopera ção. Nocaso,um
métodoparaaplicareoutropararemover.
$(".qualquer").jeitoErrado();
$(".qualquer").removerJeitoErrado();
Segundoadocumenta çãodojQuery[10],essaformaencheoobjeto jQueryde
sujeira,aumentandoaschancesdeseupluginafetarofuncionamentodeoutrosplu-
gins.
Ocorretoseriapassarocomandoderemo çãoporparâmetroparaopróprio
métodojeitoErrado.
148

## Página 163

CasadoCódigo Capítulo13. CriandopluginsparajQuery
$(".qualquer").jeitoCerto();
$(".qualquer").jeitoCerto("remove");
Outraboapráticaépermitirqueopluginfuncionesemquehajaanecessidade
desepassarparâmetrosnométodoqueaplicaoplugin.Obviamenteelepodenão
funcionarcomovocêgostaria,masésempreumaboapráticadefinirvalorespadrão
paracadaparâmetro,paraoqueopluginfuncionesempre.
$(".bonito").textoBonito();
$(".bonito").textoBonito({corDaLetra: "#00ff00"});
$(".bonito").textoBonito({corDaLetra: "#00ff00", corDeFundo : "#ff00ff"});
Apesardenãosersemprepossível,éumaboapráticapermitirquevocêaltere
parâmetrosdepoisqueopluginjáfoiaplicado.Paraisso,devemoslembrardeusar
sempreomesmométodo.
$(".bonito").textoBonito();
$(".bonito").textoBonito("corDeFundo", "#ff00ff");
Semprequepossível,fa çacomqueousuáriopossaconsultarovaloratualde
algumadasconfigura ções.Paraisso,useopróprionomedaconfigura çãocomoum
parâmetro.
$(".bonito").textoBonito();
$(".bonito").textoBonito("corDeFundo", "#ff00ff");
alert($(".bonito").textoBonito("corDeFundo"));
149

## Página 164

13.2. Aanatomiadeumplugin CasadoCódigo
Figura13.1:OvalordecorDeFundo
UmadascoisasmaisbacanasnojQuery,comojámostramos,éofatodevocê
poderselecionaroselementosapenasumavezeexecutarquantasopera çõesforem
necessáriasemcimadeles. Alémdoseucódigoficarmaislimpo,vocêganhaem
performance,poissóvaigastartemposelecionandooselementosumavez.
Porcontadisso,nuncaseesque çadefazercomqueoseupluginseja encadeável
(interfacefluente),fazendooseumétodoretornaroobjeto jQueryquevocêalterou.
Aindausandoaquelemeupluginerradocomoexemplo,vejacomoelefoifeito.
Seeutentasseencadearqualquerchamadaapóso pluginErrado,eureceberiaum
erro.Issomeobrigavaaselecionaroselementosmaisdeumavez.
Apenasatítulodedemonstra ção,apartirdojQuery1.9vocêpodeenviarum
objetoparaométodo cssaoinvésdefazerváriaschamadasseguidas.
$(".qualquer").pluginErrado();
$(".qualquer")
.pluginQualquer()
.css({"color": "red", "text-shadow": "0.5em #ccc" });
Ojeitocorreto,mantendoapolíticadaboavizinhan ça,émanteromeuplugin
encadeávelenãoquebraracorrente .
$(".qualquer")
.bomVizinho()
.pluginQualquer()
.css({"color": "red", "text-shadow": "0.5em #ccc" });
150

## Página 165

CasadoCódigo Capítulo13. CriandopluginsparajQuery
Use nomes em inglês
Apesardeeuterusadonomesdemétodosepropriedadesemportuguês,
comoúnicoobjetivodeapresentarclaramenteasboaspráticas,eureco-
mendofortementequevocêsempreusenomeseminglês.
Deixandodeladotodaadiscussãosobresoberanianacionaleimperia-
lismo,tenteimaginarquevocêencontrouumpluginmuitobacanacom
nomesemchinêsoutailandês.Quaisaschancesdevocêutilizá-lo?
Gostandoounão,oinglêséoidiomaoficialdaInternetedodesenvolvi-
mentodesoftwares.
Porfim,lembre-sedequevocênãoestásozinhonomundoequeoseupluginé,
porenquanto,apenasumtijolinhoinsignificantenumamuralhadeop çõeseplugins
disponíveis.
Agoravoumostrarcomocriarnossoprópriopluginusandoessasboaspráticas.
13.3 Escrevendo a declaração do plugin
Comojádissemos,umpluginéinvocadoatravésdeummétodoquevamosadici-
onarnoobjeto jQuery.Adiferen çaaquiéque,aoinvésdeadicionarométodoem
prototype,vamosadicionarem fn.
Nãosepreocupe,poisnãohánovidadenenhumaaqui. Esse fnéapenasum
apelidopara prototype,conformepodemosveremumtrechodocódigofontedo
jQuery:
jQuery.fn = jQuery.prototype = {
// e mais uma tonelada de código
VamoscriarumpluginqueverificaseoCPFinformadoestácorretoe,noaugeda
criatividade,vamoschamarde validador.Vamospermitirtambémqueousuário
utilizeasprópriasvalida ções.
151

## Página 166

13.3. Escrevendoadeclaraçãodoplugin CasadoCódigo
Figura13.2:Comonossovalidadorvaificar
Paracriarumplugin,come çamoscriandoummétodochamado validador,que
adicionaremosaoprotótipo fndoobjetojQuery. Comoserápossívelaousuário
informarumafun çãopersonalizadacasoelequeirausaroutrotipodevalida ção,
vamosreceberasop çõescomoparâmetro:
jQuery.fn.validador = function(options) {
// esse é o menor plugin que existe
}
Maspercebaqueestamosusando jQueryoinvésdeusarmosaformareduzida
$.Oproblemadeusar $équeoutrasbibliotecastambémusamessesímbolocomo
umaformareduzida.Abiblioteca Prototypeéumaquefazusodessesímbolootempo
todo.
Parausarmososímbolo $semmedodecausarconflitocomoutrasbibliotecas,
vamosusarumatécnicachamada IIFE,queemtradu çãolivresignifica Invocação
imediatadefun çãoou,numaexplica çãobemmaissimples, umafunçãoqueinvocaa
simesma.
Apesardonomepomposo, IIFEsignificaquevamosdefinirumavariável $den-
trodoescopodeumafun çãoparaquepossamosusá-lasemquehajainterferência
dequalqueroutrabiblioteca.Vamospassar jQuerycomoparâmetroparaavariável
$enãoprecisaremosnospreocuparmaiscomisso.
Naprática,vamosdeclararafun çãoentreparênteses,passandooobjeto jQuery
comoparâmetro:
152

## Página 167

CasadoCódigo Capítulo13. CriandopluginsparajQuery
(function($) {
// e aqui vem todo o código do nosso plugin
})(jQuery);
Apesardeparecerconfusoepoucolegívelàprimeiravista,essecódigofazexa-
tamenteomesmoqueotrechoabaixo,massemcriarnenhumavariável:
var escopo = function($) {
// e aqui vem todo o código do nosso plugin
}
escopo(jQuery);
Quandovocêdeixadecriarumavariávelparaguardarafun ção,vocêreduzas
chancesdecausarconflitocomcódigodeterceiros.Imaginequealgumoutroplugin
definiuumavariávelnoescopoglobalcomomesmonomequeasua.
Umaoutraboaregradizquedevemosinserirumponto-e-vírgula antesdocó-
digononossoplugin. Comoasregrasquedefinemousoopcionaldeponto-e-
vírgula[16]nofinaldeumainstru çãonãosãointeiramentecompreendidaspelamai-
oriadosdesenvolvedores,éseguroencerrarmosqualquerinstru çãoqueestejaaberta
comumponto-e-vírgulanocome çodonossocódigo.
Mesmoqueocódigodeterceirosqueestiverimediatamenteantesdonossotiver
sidofechadocorretamente,onossoponto-e-vírgulaamaisnãovaifazeramenor
diferença.
Lembre-sedequenãofazemosamenorideiadoambienteedascondi çõesem
quenossopluginseráusado.
Comissopodemosalterarocódigodonossopluginparausarosímbolo $:
;(function($) {
$.fn.validador = function(options) {
// esse é o segundo menor plugin que existe
}
})(jQuery);
VamoscriarumacaixadetextocomHTMLefazercomqueonossopluginseja
aplicadoaele.
AdeclaraçãoHTMLnãotemsegredonenhum.Oelementoteráum idcomo
valor cpf,queusaremosnahoradeaplicaroplugin.
153

## Página 168

13.4. OalgoritmodeCPF CasadoCódigo
<p>
<label for="cpf">CPF: </label>
<input type="text" id="cpf" maxlength="14" size="18">
</p>
Eapósocódigodonossoplugin,vamosfazerojQueryaplicá-loaoelemento
assimqueodocumentoforcarregado
$(function() {
$("#cpf").validador();
})
Agoravamostestare,nadaacontece.Comonãoescrevemoscódigoparaoplu-
gin,elefoiaplicadocorretamente,masaindanãofaznada.
13.4 Oalgoritmo de CPF
Apesardenãofazerpartedoassuntoprincipaldestelivro,vouexplicarrapidamente
comofuncionaoalgoritmodevalida çãodeCPFparaquevocêpossaacompanharo
códigodestecapítulo.
Vamoscriarumafun çãochamada validaCpf,quevaireceberumtextoeretor-
narverdadeirosomenteseoCPFforválido.
Vamosdeixaressafun çãodentrodonossoescopo,paraquenãohajaoriscode
haveroutrafun çãocomomesmonome,criadaporterceiros.
;(function($) {
var validaCpf = function(text) {
}
// código do plugin
})(jQuery);
Onossotextopodeterqualquercaracterecomoseparador.Ousuáriopodeusar
ponto,traço,barraouqualqueroutracoisaquepassarpelacabe ça.Aoinvésdeima-
ginarmostodasaspossibilidades,vamosarrancardotextotudooquenãosejaum
dígito.Paraisso,vamosusarométodo replacecomumrecursochamado expres-
sõesregulares .
154

## Página 169

CasadoCódigo Capítulo13. CriandopluginsparajQuery
Expressõesregularessãoassuntosuficienteparaumlivrointeiro.Oquepreci-
samossabernoJavaScriptéqueumaexpressãoregularédelimitadapor / /,assim
comoumtextoédelimitadoporaspas.Existeumcódigo \Dparaselecionarumca-
racterequenãoéumdígitoe,porfim,vamospassaroparâmetro gapósaúltima
barraparadizerqueaaltera çãoéglobal,ouseja,deveseraplicadaemtodootexto.
Umavezextraídososdígitos,vamosverificarseotextotemexatamente11dígi-
tos.Casocontrário,retornaremos falsesemverificarmaisnada.
text = text.replace(/\D/g, "");
if(text.length === 11 ) {
// aqui vem o algoritmo de verificação
}
return false ;
Vamosconverterotextoparaum Arraydedígitos.Umaformarápidadecon-
verterumdígitoemformatotextoparanúmeroésubtrairoASCIIdocaracterepor
48,queéocódigododígito 0.
var digitos = [];
for(var pos = 0 ; pos < text.length; pos ++) {
digitos[pos] = text.charCodeAt(pos) - 48 ;
}
Noprimeiropasso,vamoscalcularoprimeirodígitoverificador.Paraissovamos
multiplicarosnoveprimeirosdígitospor10,9,8,eassimpordianterespectivamente,
somarosresultadosdamultiplica çãoecalcularorestodedivisãopor11paraobter
oprimeirodígito.Seorestodadivisãofor10,vamosconsiderarodígitocomo0.Se
oprimeirodígitonãoestiverdeacordo,encerramosoalgoritmoretornando false.
var soma = 0 ;
for(var pos = 0 ; pos < 9 ; pos ++) {
soma += digitos[pos] * (10 - pos);
}
var primeiroDigito = 11 - (soma % 11 );
if(primeiroDigito > 9 ) {
155

## Página 170

13.5. Adicionandofuncionalidadeaoplugin CasadoCódigo
primeiroDigito = 0 ;
}
if(digitos[9] !== primeiroDigito) {
return false ;
}
Paracalcularmososegundodígitoverificador,multiplicaremososdezprimeiros
dígitosdoCPFpor11,10,9,eassimpordianterespectivamente,somamososvalores
obtidosecalculamosorestodadivisãopor11. Seorestodadivisãofor10,vamos
considerarodígitocomo0.
Finalmente,retornamosovalordafun çãocomosendoacompara çãodonúmero
obtidocomosegundodígitoverificador.
// continuação do código
soma = 0 ;
for(var pos = 0 ; pos < 10 ; pos ++) {
soma += digitos[pos] * (11 - pos);
}
var segundoDigito = 11 - (soma % 11 );
if(segundoDigito > 9 ) {
segundoDigito = 0 ;
}
return digitos[10] === segundoDigito;
}
13.5 Adicionando funcionalidade ao plugin
Parafinsdemanterosexemplossimples,considerequeocódigoqueapresentar-
mosapartirdaquiestarádentrodométodo validador. Aofinaldocapítulo,nós
mostraremosocódigocompletoparaesclarecerqualquerdúvidaqueapare ça.
Aprimeiracoisaqueprecisamosprestaraten çãoéquenãosabemosseojQuery
vaiselecionarumoumaiselementosparaonossoplugin.Vamosconsiderarsempre
opiorcaso,queéquandoojQuerynosretornaumalistadeelementos.Mesmoque
156

## Página 171

CasadoCódigo Capítulo13. CriandopluginsparajQuery
elenosretorneumounenhumelemento,ocódigoaseguirvaicontinuarfuncio-
nando.Vamosusaronossojáconhecido eachparamodificarcadaumdoselemen-
tos.
OobjetojQuery thisreferenciaoselementosqueforamselecionadosparaque
opluginsejaaplicado.
Parafazermoscomqueonossopluginnãoquebreacorrente,retorneovalordo
métodoeach.Essemétodoretornaoobjetoqueestásendoiterado,deixandotudo
prontoparaqueousuáriopossaencadearmaismétodosfuturamente.
Vamoscriarumafun ção init,queconfiguraoplugineadicionaoseventosne-
cessáriosaoselementosselecionados.Comisso,ométodo eachapenasrecebe init
comoumcallback.
var init = function() {
}
return this .each(init);
Nafunção init,vamoscriarumavariável elementparanãotermosqueficar
acessando $(this)todasasvezesqueprecisarmos.Essavariávelvaiconterarefe-
rênciaaoobjetoaoqualopluginestásendoaplicado.
Vamostambémdefinirosparâmetrosdoplugin,usandoométodo extenddo
jQuery.Ométodo extendrecebedoisparâmetros:oprimeiroéumobjetocontendo
aspropriedadesdoplugineseusvalorespadrão,enquantoosegundoparâmetrocon-
témumobjetocontendoasop çõespassadaspelousuário.Oresultadoéumobjeto
contendotodasasop çõesdoobjetomescladacomosvaloresalteradospelousuário.
Nocasodonossoplugin,teremosapenasumparâmetro function,quevaiindi-
carafun çãoaserexecutadaparavalidaroconteúdodacaixadetexto.Porpadrão,
opluginverificaavalidadedoCPFinformado.
Asconfiguraçõesdoobjetoestarãodisponíveisnavariável settings.
var element = $(this);
var settings = $.extend({
"function" : validaCpf
}, options);
Apenasparamelhoraralegibilidadedocódigo,vamoscriarumafun çãocha-
mada isValid,queexecutaafun çãoindicadanoparâmetro function.
157

## Página 172

13.5. Adicionandofuncionalidadeaoplugin CasadoCódigo
var isValid = function(text) {
return settings["function"](text);
};
Vamoscriartambémumcallbackqueseráexecutadoquandooelementoperder
ofoco.Naprática,significaquequandooelementoperderofoco,avalida çãoserá
feitaeaclasseCSS erroseráaplicadacasoovalorsejainválido,ou validoquando
ovalorestiverdeacordocomavalida ção.
var onElementBlur = function() {
var text = element.val();
if(isValid(text)) {
element.removeClass("erro");
element.addClass("valido");
} else {
element.removeClass("valido");
element.addClass("erro");
}
}
Porfim,encerramosocódigodopluginatribuindoocallback onElementBlur
aoevento blur.Notequeestamosusandoumnamespace validador,paraqueisso
nãocauseconflitocomnenhumoutroplugin.
element.on("blur.validador", onElementBlur);
Nafigura13.3podemosvercomoficouonossoplugin.OsarquivosCSSeima-
gensadicionaisestãodisponíveisnorepositóriodoGitHub,cujolinkeuapresentarei
maisaofinaldocapítulo.OCPFusadocomotestefoicriadoaleatoriamenteporum
geradordeCPF.
Figura13.3:UmCPFválidoeuminválido
158

## Página 173

CasadoCódigo Capítulo13. CriandopluginsparajQuery
13.6 Personalizando o plugin
Comovocêselembra,nóscriamosapossibilidadedeusarvalida çõespersonalizadas
nonossoplugin.
Parademonstrarcomoissofunciona,vamoscriarumafun çãomuitosimples,
queapenasverificaseocampoestávazioounão.Casoeleestejavazio,faremoscom
queopluginreclameeacuseumerro.
Vamoscriarumafun çãochamada obrigatorio,queserápassadaemumadas
opçõesdoplugin.
function obrigatorio(text) {
return text.trim() !== "";
}
E,parausarmosnoplugin,bastadeclararmosoparâmetro function,selecio-
nandoumacaixadetextocomaclasseiguala obrigatorio.O iddoelementoeo
nomedafun çãoficamaoseucritério.
$(".obrigatorio").validador({function: obrigatorio});
Paratestar,eucrieiduascaixasdetextoeobtiveasaídaapresentadanafigura
13.4.
Figura13.4:Campoobrigatório
13.7 Mais plugins
Ositehttp://plugins.jquery.coméorepositóriooficialdepluginsdojQuery.Lávocê
encontradesdepluginsmuitobemescritosatéalgunsquepoderiamtersidotratados
commaiorcuidado.
159

## Página 174

13.7. Maisplugins CasadoCódigo
Atítulodeexemploereferência,vouindicaralgunspluginsqueeuutilizoere-
comendo.
Máscara
NossocolegaDiegoPlentzreescreveurecentementeoplugin MaskMoney,do
qualtiveoprazerdecontribuir.Ébasicamenteumpluginquepermiteaformata ção
decamposdetextoparapermitiradigita çãodevaloresmonetários.
Mexendoumpouconasconfigura ções,vocêconsegueusaropluginparaqual-
quertipodenúmero,inteirooudecimal.
Parausarmosoplugin,vocêdevebaixaroarquivonorepositóriodoGitHube,
considerandoquevocêcriouumacaixadetextocomo idiguala valor,ocódigo
JavaScriptparalidarcomvaloresemRealé:
$("#valor").maskMoney({symbol: "R$",
thousands: ".",
decimal: ","});
Figura13.5:MaskMoneyemfuncionamento
OrepositóriodoGitHubficanoendere çoabaixo:
https://github.com/plentz/jquery-maskmoney
Gráficos
OjqPlotéumaferramentadegera çãodegráficosqueutilizaocomponenteCan-
vasdoHTML5.
Existemcentenasdepossibilidadesdiferentesdegráficosetemas.Vouapresentar
umgráficobemsimples,ondevocêprecisainformarascoordenadasXeYemum
Array:
$.jqplot('chartdiv',
[[[1, 2],
160

## Página 175

CasadoCódigo Capítulo13. CriandopluginsparajQuery
[3, 5.12],
[5, 13.1],
[7, 33.6],
[9, 85.9],
[11, 219.9]]]);
Oresultadopodeservistonafigura13.6.
Figura13.6:UmgráficosimplescomjqPlot
Vocêpodefazerodownloadeconsultaradocumenta çãonoendere çoabaixo:
http://www.jqplot.com/
13.8 Onde aprender mais
Ocódigocompletoparaopluginestánocapítulo13dorepositóriodolivrono
GitHub,noendere çoabaixo:
https://github.com/pbalduino/livro-js-jquery
Existemmaispossibilidadesparadesenvolverseupróprioplugin. Recomendo
quevocêleiaadocumenta çãooficialnoendere çoabaixoe,comodiversão,escreva
pluginsparaajudarafixaroqueaprenderdenovo.
161

## Página 176

13.8. Ondeaprendermais CasadoCódigo
http://docs.jquery.com/Plugins/Authoring
Disponibilizeiumexemplodesteplugin,comavalida çãodeCPFeachecagem
decampoobrigatórionoendere çoabaixo:
http://jsfiddle.net/pbalduino/LLret/
162

## Página 177

Capítulo14
DicasparausarmelhorojQuery
“Thereismoretolifethansimplyincreasingitsspeed. ”
–MahatmaGandhi
14.1 Por que performance é importante?
Alémdeterumdesignimpecável,éimportantíssimoqueasuaaplica çãonãodemore
paracarregarouexecutarastarefas.Ousuárioassociadiretamentearesponsividade
eavelocidadeaparentedeumsiteàqualidadedoprodutoeàcompetênciadaem-
presa.
ÉsabidoqueoGooglepodealterararelevânciadoseusitedeacordocoma
performance.Sitesmaislentossãoconsideradosmenosrelevantes.
RecomendoaleituradeumexcelentepostdoSérgioLopessobrecarregamento
assíncronoderecursosnoendere çohttp://goo.gl/fu88T,paraquevocêmelhorea
responsividadedoseusiteemtodososaspectos.
Sabendodisso,énecessárioquetenhamosemmentecomofazerparaqueanossa
aplicaçãoexecutenomenortempopossível,usandoaferramentadomelhormodo.

## Página 178

14.2. Usesempreaversãomaisrecente CasadoCódigo
Paranãoficarmosnocampodasespecula ções,vamosusaraferramenta jsPerf
paraexecutarasavalia çõesdetempo.Vocêpodecriarseusprópriostestesemhttp:
//jsperf.com/
14.2 Use sempre a versão mais recente
EmcadanovaversãodojQuery,informadapelosdoisprimeirosnúmeros,sãoin-
cluídasmelhoriasdeperformanceelimpezadecódigo.Suporteabrowsersantigos
sãoremovidos,partedocódigoéreescritadeformaqueexecutemaisrapidamente.
Asversõesmenores,indicadaspeloterceironúmero,contémcorre çõesdebugs
efalhasdeseguran ça.
QuandovocêutilizaaversãomaisrecentedojQuery,vocêfazusodetodasas
melhoriasdedesempenhoeseguran çaemrela çãoaversõesmaisantigas.
Nafigura14.1podemosveracompara çãodedesempenhoentreasversões1.4.2,
1.8.0,1.9.0e1.9.1,queéamaisrecenteenquantoescrevoesselivro.
Figura14.1:Versão-Opera çõesporsegundo(maisémelhor)
OptesemprepelaúltimaversãodojQuery.Achancedeseusscriptsquebrarem
costumasermínimasevocêadotaressaprática.
164

## Página 179

CasadoCódigo Capítulo14. DicasparausarmelhorojQuery
14.3 Escolha os seletores corretos para a tarefa
Semprequevocêselecionaumoumaiselementos,ojQuerypercorreaárvoredo
DOMatéencontraroquevocêprocura.
Alguns seletores usam funções nativas do browser, como é o caso do
getElementById,eémuitorápido.Outrosdependemdoquãonovoéoseubrowser,
podendovariarentreo rápidoeoridiculamentelento,comoacontececomométodo
getElementsByClass.SevocêestiverusandoumaversãodesatualizadadoInternet
Explorer,umabuscaporclassesemostrarálentaepesada.
Outrosseletoressãolentosdequalquermaneira,comoéocasodos pseudo-
seletores,queselecionamaslinhasparesouímparesdeumatabela,porexemplo.
Figura14.2:Seletores-Opera çõesporsegundo(Maisémelhor)
Nafigura14.2temosaconfirma çãodequeselecionarumelementoatravésde
seu idémuitomaisrápido.
Quandoqueremosselecionarmaisdeumelemento,oseletordeclasseséuma
boaescolha,sevocêestiverusandoumbrowsermoderno.
Opiorcasodetodoséquandoselecionamoselementosdeumformuláriousando
otipo,comonocódigoabaixo:
$("input[type='text']");
165

## Página 180

14.4. Nãoseesqueçadocache CasadoCódigo
Semprequepossível,utilizeclassesaoinvésdeselecionarelementosatravésde
algumapropriedade.
14.4 Não se esqueça do cache
Aindamaisefetivodoqueescolherosseletorescorretoséentendercomousaro
cachedeobjetos .
Fazercache,nocontextodojQuery,nadamaisédoquearmazenaroresultado
dosseletoresemumavariável.
Aoinvésdeperdertemposelecionandováriasvezesomesmoconjuntodeele-
mentos,vocêpodemuitobemselecionarumavez,guardaroresultadonumavariável
para,emseguida,efetuartodasasopera çõesnecessárias.
Afigura14.3mostraadiferen çadedesempenhoentrediferentesabordagens.
Figura14.3:Cache-Opera çõesporsegundo(maisémelhor)
Paravocêentenderoquefoifeito,vamosusarumcódigoHTMLbemsimples,
contendoumelemento div:
<div id="teste"></div>
Vamosescreverumcódigoqueefetuaumasériedeopera çõessobreesseele-
mento.Apenasatítulodeexplica ção,vamosfazê-lodesaparecereapareceralgumas
166

## Página 181

CasadoCódigo Capítulo14. DicasparausarmelhorojQuery
vezes.
Ignoreofatodequepoderíamosusarum for.Aideiaaquiéapenasapresentar
umaboaprática.
$("#teste").hide();
$("#teste").show();
$("#teste").hide();
$("#teste").show();
$("#teste").hide();
$("#teste").show();
Oqueaconteceaqui,internamente,équeojQueryvaicriarumobjeto,parsearo
seletorquefoipassado,usarasfun çõesnativasdobrowserparalocalizaroelemento
quevocêestáprocurandoatravésdo idesóentãoretornaroobjetoquecontémo
elementoquebuscamos.
Depois,usandooobjetojQuery,seráexecutadaaopera çãodesejada.Nonosso
caso,osmétodos hideou show.
Issovaiacontecerseisvezes.Eolhequeaquieunãoentreinaquestãodeterque
alocarmemóriaacadavezqueoobjetoécriadoeliberá-laassimqueoprocessa-
mentotermina.
Comcache,nossocódigovaiselecionaroelementoapenasumavez,comtodos
osprocedimentosaquetemdireito:criarumobjetojQuery,parsearoseletor,usar
asfunçõesnativasdobrowser,retornaroobjetocomoelementodentroedeixá-la
confortavelmentenumavariável.
Então,nasmesmasseisvezes,vamosapenasacessaravariáveleexecutarasope-
raçõesdesejadas.
$cache = $("#teste")
$cache.hide();
$cache.show();
$cache.hide();
$cache.show();
$cache.hide();
$cache.show();
167

## Página 182

14.5. Asvezes,menosémais CasadoCódigo
Essasegundaabordagemchegaaserduasvezesmaisrápidadoqueaprimeira,
conformeapresentamosnafigura14.3.
Comojádemonstramosváriasvezes,ojQuerynospermiteencadearaschama-
dasdemétodos,fazendocomqueusemososeletorapenasumavez.
Existemduasformasdeseusarencadeamento. Aprimeiraéencadeardireta-
mentenoseletor:
$("#teste")
.hide()
.show()
.hide()
.show()
.hide()
.show();
Easegundaformaéfazerumcachedesseobjetoeencadearosmétodosnava-
riável.
$cache = $("#teste");
$cache.hide()
.show()
.hide()
.show()
.hide()
.show();
Comoéobrigaçãodeumdesenvolvedordesoftwaressercurioso,euquissaber
qualdasduasversõesofereceamelhorperformance.Aconclusãoéquetantofaz.
Opesodoqueestamosfazendoestánoprocessodecriarobjeto,parsearepro-
curar.Umavezquevocêotimizeoseucódigofazendocomqueesseprocessoseja
executadoapenasumavez,tantofazseoresultadovaiestarnumavariáveloudire-
tamentenoretornodoseletor.
Vocêpodeveressetestecomdetalhesnoendere çoabaixo:
http://jsperf.com/good-jquery-code-cache-dom-selectors/2
14.5 As vezes, menos é mais
Comovimosatéaqui,ojQueryresolvequasetodososnossosproblemasdeincom-
patibilidadesentrebrowsersesimplificamuitoamanipula çãodeDOMeacomuni-
caçãodedadosusandoAJAX.
168

## Página 183

CasadoCódigo Capítulo14. DicasparausarmelhorojQuery
Porém,comovocêdevetercansadodeouvir,nãoexistebaladeprata.Vocênão
podeacharqueojQueryéasolu çãoparatodososseusproblemas. Emalgumas
vezes,asolu çãomaisrápidaétambémamaissimples.
Noscasosemquepodeocorrerincompatibilidadeentrebrowsers,useojQuery
parafugirdetodososproblemasquevimosnoscapítulos3e4.
HTML
Emcasosemquevocêpreciseapenasleroumodificaroconteúdodeumele-
mentoquevocêacessaatravésdo id,considereapossibilidadedeusarJavaScript
puroaoinvésdedelegaratarefaaojQuery.
Afigura14.4mostraoresultadodotestecomparandoousodejQueryeJavaS-
criptpuroparaalterareleroconteúdodeumelemento.
Considerandoquevocêtenhaumelemento divqualquercom idiguala teste,
usamosasinstru çõesabaixoparaostestesdegrava ção:
document.getElementById("teste").innerHTML = "texto";
$("#teste").html("texto");
Aprimeirainstru çãofoiquaseduasvezesemeiamaisrápidadoqueaprimeira.
Selevarmosemcontaquepraticamentetodososbrowsersemusoatualmentetemo
métodogetElementByIdimplementado,temosaiumganhoconsiderável.
Paraotestedeleitura,usamosocódigoabaixo:
document.getElementById("teste").innerHTML;
$("#teste").html();
Comoeradeseesperar,aleituraémuitomaisrápidaqueagrava ção. Oque
impressionoufoiadiferen çadeperformanceentreasversões:ocódigoqueusaJa-
vaScriptpurofoiquaseonzevezesmaisrápidoqueaversãojQuery.
169

## Página 184

14.5. Asvezes,menosémais CasadoCódigo
Figura14.4:HTML-Opera çõesporsegundo(maisémelhor)
Namesmalinha,temosnafigura14.5adiferen çadeperformanceentreduas
instruçõesqueretornamo iddeumelemento.
Figura14.5:ID-Opera çõesporsegundo(maisémelhor)
170

## Página 185

CasadoCódigo Capítulo14. DicasparausarmelhorojQuery
Usamosocódigoabaixoparaoteste:
var elemento = $("#teste");
$(elemento).attr("id");
elemento[0].id;
Aprimeiraformaacessaro idapóscriarumobjetojQuery,enquantoasegunda
acessaapropriedadediretamentenoDOM.
Existemváriasoutrasformasemqueépreferívelacessardiretamenteoobjeto
DOMouusarJavaScriptpuro.Nadúvida,crieseusprópriostestesusandoojsPerf.
171

## Página 187

Capítulo15
Eoquevemagora?
15.1 jQuery2.0
TodoocódigoqueapresentamosétotalmentecompatívelcomojQuery1.9.1,que
eraaversãomaisrecentedeprodu çãonadatadolan çamentodolivro.
Porém,enquantoterminodeescreveressaslinhas,aversão 2.0.0estáemBeta.
Seoseucódigofoiescritodeacordocomaspráticasindicadasnestelivro,fique
tranquilocomaquestãodacompatibilidade. Asversões 1.9.1e 2.0.0sãototal-
mentecompatíveis.
Casovocêestejausandocódigoantigo,recomendofortementequevocêleiao
guiademigra çãoparaaversão 1.9.1,nolinkabaixo:
http://jquery.com/upgrade-guide/1.9/
Aprincipaldiferen çaentreaversãoatualea 2.0.0serefereaganhosdeperfor-
mance,comojáécomumentreumaversãoeoutra.

## Página 188

15.2. Recomendaçõesdeleitura CasadoCódigo
15.2 Recomendações de leitura
Nofinaldolivroháumalistadesiteselivrosqueserviramdereferênciaparaa
composiçãodestelivro.
Algunslivrosforammuitoúteisparatirardúvidaseentenderconceitos,masnão
foramcitadosnodecorrerdoscapítulos. Porissoeuvousugeriralgunsdelespara
quevocêpossacontinuarestudandoeavan çandonoaprendizado,setornandoum
profissionalcadavezmelhoremaiscompleto.
InfelizmenteoslivrosrecomendadosaquiestãoemInglês,oquevaiexigirum
esforçoamaisdesuaparte.Eunãoconhe çonenhumtítulonacionalquesejadidático
equetenhaconteúdoobastanteparaqueeupossarecomendar.
MesmoentreostítulosemInglês,pormaisnumerososquesejam,ficadifícil
encontrarlivrosquenãorepitamsempreasmesmascoisasefiquemnaquelemais
domesmo.
JavaScript:TheGoodParts
Figura15.1:JavaScript: TheGoodParts
EscritoporDouglasCrockford,ocriadordoJSON[4].
Euconsideroesseomelhorlivrojáescritosobreoassunto.Nocome çodolivro
eucomenteiqueoconteúdopoderiasertraumáticoparaquemestácome çando.A
174

## Página 189

CasadoCódigo Capítulo15. Eoquevemagora?
boanotíciaéque,agoraquevocêpassouportodososcapítulos,olivrodoCrockford
vaiparecerbemsimplesdelereentender.
Nelesãoapresentadasboaspráticasemesmoojeitocertodesefazerascoisas
emJavaScript,alémdemostrartambémtécnicasdecomotrabalharcomJSON.
SecretsoftheJavaScriptNinja
EscritoporJohnResig,criadordojQuery,eBearBibeault[9].
Esselivroapresentaalgumastécnicasdedepura çãoetestes,expressõesregulares
ecomolidarcomthreads.Sevocêquiseraprendermaissobrecomoutilizartécnicas
avançadascomJavaScriptdentrodeumbrowser,recomendoaleitura.
Apenascomoumcomentário,aimagemdacapaédeumsamurai,enãodeum
ninja.
Figura15.2:SecretsoftheJavaScriptNinja
ProJavaScriptforWebApps
Escrito por Adam Freeman, autor de outros dezenove livros pela mesma
editora[6].
Omaisinteressantedesselivroéqueoautordemonstratécnicasqueatualmente
nãosãocomunsnousodeJavaScript. Porexemplo,édemonstradocomoutilizar
MVCcomJavaScript,comofazerseusitetrabalharofflineefazerasuaaplica ção
175

## Página 190

15.3. Fim? CasadoCódigo
utilizarURLspersonalizadassemqueissosejaenviadoparaoservidoretambém
comoutilizararmazenamentolocaldedadosemconjuntocomHTML5.
Recomendopeloconteúdoavan çadoepoucousual,mesmoquevocêacheque
dificilmenteváaplicarissonassuasaplica ções.
Olivroébemrecheadocomtrechosdecódigoeimagens,oquetornaafixa ção
doconteúdobemmaisefetiva.
Figura15.3:ProJavaScriptforWebApps
15.3 Fim?
Sinta-seavontadeparabuscarmaislivrosalémdosqueeuciteieparairalémdoque
foimostradonestelivro.
Olimitedoconhecimentosódependedoquantodevontadeetempovocêin-
vestir.
Casoqueiraentraremcontatocomigo,oucomeditora,acesseoslinksqueeu
disponibilizeinocapítulo1.Nãopenseduasvezesantesdeenviarcríticas,dúvidas,
sugestõesoumesmosequisermepagarumacerveja.
Boasorteemseusprojetoseobrigadopelaconfian ça.Nosvemosporaí.
176

## Página 191

CasadoCódigo ÍndiceRemissivo
ÍndiceRemissivo
==,16
===,16
Access-Control-Allow-Origin,81
AdamFreeman,175
AJAX,63
AlanTuring,139
AlonzoChurch,139
array,21
Assíncrono,64
BearBibeault,175
BenAlman,147
BrendanEich,3
Callbackhell,51
Callbacks,40,41
Cross-OriginResourceSharing,81
document.getElementById,13,17,21
document.getElementsByClassName,21,
28,29,31
document.getElementsByTagName,29
DOM,11
DouglasCrockford,1,3,74,174
Efeitos,53
Eventos,41
Expressõesregulares,154
for,22
fromCharCode,47
Funçõesanônimas,31
Funçõesnomeadas,31
GitHub,3
GoogleGroups,3
HighOrderFunction,40
HTMLclass,11
HTMLID,11
IIFE,152
innerHTML,13,17
Java,3
JesseJamesGarrett,64
JohnResig,147,175
jQuery,3,33,35
jQuery1.9,150
jQuery(document).ready,42
jQuery(objeto).is,56
jQuery(seletor),39
jQuery(seletor).addClass,59
jQuery(seletor).append,58
jQuery(seletor).blur,158
jQuery(seletor).change,42
jQuery(seletor).click,52
jQuery(seletor).css,34–36,150
jQuery(seletor).each,40
jQuery(seletor).empty,58
177

## Página 192

ÍndiceRemissivo CasadoCódigo
jQuery(seletor).find,37
jQuery(seletor).hide,52
jQuery(seletor).html,54
jQuery(seletor).keydown,47
jQuery(seletor).off,48,50
jQuery(seletor).on,50
jQuery(seletor).parent,52
jQuery(seletor).remove,53
jQuery(seletor).text,37
jQuery(seletor).val,36
jQuery.each,156
jQuery.extend,157
jQuery.get,68
jQuery.getJSON,88
jQuery.post,91
jsFiddle,65
JSON,74
KeyEvent.which,47
Math.ceiling,15
Math.floor,15
Mozilla,3
Namespace,50
Parâmetrosopcionais,89
parseFloat,14
PI,17
Plugindegráficos,160
Plugindemáscara,160
Plugins,147
Programaçãofuncional,40,139
Prototype,152
replace,154
Síncrono,64
script,13
Seletordeclasse,35
Seletordeid,35
Seletordetag,34
Seletores,36
String,47
substr,15
trim,52
var,14
Web2.0,65
window,15
XMLHTTP,64
XMLHttpRequest,64
178

## Página 193

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1] Cisco.Ciscovisualnetworkingindex.http://www.cisco.com/en/US/solutions/
collateral/ns341/ns525/ns537/ns705/ns827/white_paper_c11-520862.html,2013.
[2] W3Consortium. Html:Themarkuplanguage(anhtmllanguagereference).
http://www.w3.org/TR/html-markup/input.date.html,2012.
[3] DouglasCrockford.Javascript:Theworld’smostmisunderstoodprogramming
language.http://www.crockford.com/javascript/javascript.html,2001.
[4] DouglasCrockford.JavaScript:TheGoodParts .O’ReillyMedia,2008.
[5] RoyThomasFielding. Architecturalstylesandthedesignofnetwork-based
software architectures. http://www.ics.uci.edu/~fielding/pubs/dissertation/
top.htm,2007.
[6] AdamFreeman.ProJavaScriptforWebApps .Apress,2012.
[7] JesseJamesGarrett. Ajax:Anewapproachtowebapplications. http://www.
adaptivepath.com/ideas/ajax-new-approach-web-applications,2005.
[8] JesseJamesGarrett.Aboutme.http://www.jjg.net/about/,2006.
[9] BearBibeaultJohnResig. SecretsoftheJavaScriptNinja .Manning,2012.
[10] jQuerydocumentation. Authoringplugins. http://docs.jquery.com/Plugins/
Authoring,2013.
[11] "KorRedDevil".getelementsbyclassnameimplementationforinternetexplorer.
http://bit.ly/RgTzlV,2005.
[12] DavidLeavitt.Ohomemquesabiademais .EditoraNovoConceito,2011.
179

## Página 194

ReferênciasBibliográficas CasadoCódigo
[13] SérgioLopes.Nãousejquerynoseusitemobile:conhe çaozepto.js.http://blog.
caelum.com.br/nao-use-jquery-no-seu-site-mobile-conheca-o-zepto-js/,
2012.
[14] Mozilla. Geckokeypressevent. https://developer.mozilla.org/en-US/docs/
Gecko_Keypress_Event,2008.
[15] MaxOgden.Callbackhell.http://callbackhell.com/,2012.
[16] Michael"sideshowbarker"Smithetal. Automaticsemicoloninsertion. http:
//es5.github.com/#x7.9,2012.
[17] W3Techs. Usageofjavascriptlibrariesforwebsites. http://w3techs.com/
technologies/overview/javascript_library/all,2010.
[18] Wikipedia. Ajax-history. http://en.wikipedia.org/wiki/Ajax_(programming)
#History,2012.
[19] Wikipedia. Sameoriginpolicy. http://en.wikipedia.org/wiki/Same_origin_
policy,2012.
180