---json
{
  "id": "criando_aplica__es_para_o_seu_windows_phone_edi__o_windows_runtime",
  "title": "Criando aplicações para o seu Windows Phone Edição Windows Runtime",
  "categoria": "04-frameworks",
  "subcategoria": "mobile",
  "resumo": "**Arquivo Original:** `Criando aplicações para o seu Windows Phone Edição Windows Runtime.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "criando",
    "edi",
    "frameworks",
    "mobile",
    "para",
    "phone",
    "runtime"
  ],
  "perguntas_tipo": [
    "Como utilizar Criando aplicações para o seu Windows Phone Edição Windows Runtime?",
    "Quais as boas praticas de mobile?"
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
  "dono": "stack-mobile",
  "prioridade": 2
}
---

# Criando aplicações para o seu Windows Phone Edição Windows Runtime

> **Arquivo Original:** `Criando aplicações para o seu Windows Phone Edição Windows Runtime.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

62598


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
E-book gerado especialmente para 


## Página 3

E-book gerado especialmente para 


## Página 4

E-book gerado especialmente para 


## Página 5

CasadoCódigo Sumário
Sumário
1 Antesdetudo 1
1.1 Sobreoautor . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Agradecimentos . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2 EstamosnaEraMobile 3
2.1 EessetaldeWindowsPhone? . . . . . . . . . . . . . . . . . . 4
2.2 PorquedesenvolverparaWindowsPhone? . . . . . . . . . . 5
2.3 Oquevocêencontraránestelivro . . . . . . . . . . . . . . . . 6
2.4 Antesdecome çarmos. . . . . . . . . . . . . . . . . . . . . . . 7
3 ConhecendooSDKecriandonossaprimeiraaplica ção 9
3.1 Criandonossaprimeiraaplica çãoeconhecendooemulador 11
3.2 Configurandoseudispositivoesuacontacomodesenvolvedor 15
3.3 Blend . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4 Utilizandocomponentesdosistemaparamelhoraraexperiência
dousuário 19
4.1 Princípiosdedesign . . . . . . . . . . . . . . . . . . . . . . . . 20
4.2 Começandonossoaplicativo . . . . . . . . . . . . . . . . . . . 21
4.3 Gerenciadoresdelayout . . . . . . . . . . . . . . . . . . . . . . 22
4.4 Criandoapáginadeboas-vindas . . . . . . . . . . . . . . . . 28
5 Designdeaplica ções 41
5.1 Melhoriasdeusabilidade . . . . . . . . . . . . . . . . . . . . . 41
5.2 ConhecendooscontrolesdoWindowsPhone . . . . . . . . . 45
i
E-book gerado especialmente para 


## Página 6

Sumário CasadoCódigo
6 GerenciamentodedadosemumaplicativoWindowsPhone 55
6.1 Carregandoosdadosparaaaplica ção . . . . . . . . . . . . . 56
6.2 Vinculandoosdadoscomoscontrolesdeusuário . . . . . . 62
6.3 ArmazenandodadosemarquivosJSONnoWindowsPhone 79
6.4 Armazenandoconfigura çõeseosimpactosemnossoaplicativo 90
7 Navegaçãoeciclodevida 95
7.1 Navegaçãoentrepáginas . . . . . . . . . . . . . . . . . . . . . 95
7.2 Ciclodevidadaaplica ção . . . . . . . . . . . . . . . . . . . . 103
7.3 NavigationHelpereSuspensionManager . . . . . . . . . . . . 105
7.4 Inicializaçãorápida . . . . . . . . . . . . . . . . . . . . . . . . 111
8 Integraçãocomosistemaoperacional 117
8.1 Finalizandoasfuncionalidadesjácriadas . . . . . . . . . . . . 118
8.2 EntendendoosLivetiles . . . . . . . . . . . . . . . . . . . . . 124
8.3 Criandotilessecundários. . . . . . . . . . . . . . . . . . . . . 129
8.4 ConhecendooShareContract . . . . . . . . . . . . . . . . . . 134
9 Mapaselocaliza ção 139
9.1 Criandoapáginaparafinalizarcompra . . . . . . . . . . . . . 139
9.2 EntendendoocomponenteMap . . . . . . . . . . . . . . . . . 144
9.3 Finalizandonossoaplicativo . . . . . . . . . . . . . . . . . . . 148
10 DicasparapublicaçãonalojadoWindowsPhone 155
10.1 Passosparapublicação . . . . . . . . . . . . . . . . . . . . . . 155
10.2 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
Versão:17.4.23
ii
E-book gerado especialmente para 


## Página 7

Capítulo1
Antesdetudo
Estaobraéresultadodotrabalhoeesfor çodiretoeindiretodediversaspes-
soas.Esteprimeirocapítuloédedicadoaagradecimentosàspessoasenvolvi-
dasetambémparaquevocêpossasabermaissobreoautor.
1.1 Sobre o autor
Eu,GabrielSchadeCardoso,souumjovemde23anos(2014),graduadoem
CiênciadaComputação,estudantedemestradoemInteligênciaArtificiale
amantedatecnologia,emespecialdaáreadedesenvolvimentodesoftware.
Meuprimeirocomputadorfoiaos10anosdeidade,umpresentequemudou
minhavida.Comoquasetodososgarotosdessaidade,eugostavamuitode
vídeogamesedejogarRPGcommeusamigos.Issomeinfluenciouautilizar
meucomputadorparapesquisarsobrecomoosjogoseramcriadose,mesmo
semperceber,aos11anoseujáestavaestudandoprograma çãoecriandojogos
E-book gerado especialmente para 


## Página 8

1.2. Agradecimentos CasadoCódigo
simples.
Depoisdissonãofoidifícildecidiroqueeuqueriafazerdavida.Comecei
aexploraraprograma çãoforadaáreadejogosesoufascinadoporissoaté
hoje.Tenhosortedeconseguirtrabalharcomoquegosto,estoucomcinco
anosdeexperiêncianaáreadedesenvolvimentodesoftwareenessetempo
acumuleiconhecimentosnaslinguagensJava,C++,Javascripte,claro,C #.
Atualmente, além de trabalhar na área de desenvolvi-
mento de software, também escrevo com frequência no blog:
www.programadorpoliglota.com.br e busco participar de eventos na
comunidadetécnicaecientífica,atravésdeartigos,palestraseapresenta ções.
1.2 Agradecimentos
Seriamuitoegoísmodeminhapartenãoagradeceratodasaspessoasqueme
ajudamdiretaeindiretamenteemtodasasminhastarefas.
Agradeço: Àminhamãe,Eulália,porsempreestarcomigoeporcon-
seguirsuportarpesosabsurdosparamanterseusfilhossegurosesaudáveis,
mesmonosmomentosmaisdifíceis.
ÀminhamelhoramigaeirmãDaniela,porserminhaconselheiraecon-
fidente.
Atodaminhafamília,porseraluzquemeguia,aténosmomentosmais
escuros.
Aosmeusamigosdaépocadefaculdade,Jhony,RodrigoeJoão,pessoas
dasquaiseutenhoorgulhodechamardeamigoecomcertezaaspessoasmais
brilhantesqueeuconhe ço.
Atodososmeusamigosepessoasqueridas,quesãoaestruturavitalque
meempurraparacimaemefazserquemeusou.
ÀEditoraCasadoCódigo,poroferecermaisumaoportunidade,criar
todaaestruturanecessáriaparaarealiza çãodestaobraeporacreditarem
mimenesteprojeto.
Atodasessaspessoasficaomeumaissincero obrigado.
2
E-book gerado especialmente para 


## Página 9

Capítulo2
EstamosnaEraMobile
Estamosnaera mobile:hojeemdianãoénadasurpreendenteterumsmart-
phone.Oatualcenáriodespertariabastantecuriosidadepoucotempoatrás,
masofatoéqueagoracarregarumsmartphoneemumbolsodacal çaéquase
tãocomumquantoacarteiraquesecarreganooutrobolso.Aspessoasestão
cadavezmaisconectadas,compartilhandocoisas,lendonotíciasee-mails,
gravandovídeos,conversandocomosamigosdistantesefazendoatévideo-
conferências.
Comumdispositivorazoavelmentepequenoconseguimosfazergrande
partedastarefasqueexecutamosemumcomputador,queébemmaispesado
emenosportátil. DeacordocomaForbes,estima-sequeem2017maisde
80%dosdispositivosconectadosàinternetserãotabletsesmartphones.Para
nós,desenvolvedoresdesoftware,éimportantíssimoinvestirnessemercado
emanter-seatualizadoparaestenovoparadigma.
E-book gerado especialmente para 


## Página 10

2.1. EessetaldeWindowsPhone? CasadoCódigo
2.1 E esse tal deWindows Phone?
VocêjáouviufalardoWindowsPhone?Casonão,saibaqueeleéosistema
operacionalparadispositivossmartphonesdaMicrosoft,sendoumaalterna-
tivaaossistemasmaisconhecidosejáconsolidados,comooIOSdaApplee
AndroiddaGoogle.
Apesardeseremdiferentes,dispositivosAndroideIOSpossuemmuitas
similaridadesemquestãodeinterfaceedeexperiênciacomousuário.OWin-
dowsPhonechegoupraticamentetrêsanosdepoisdessessistemascomuma
propostabemdiferente.Nafigura 2.1podemoscompararatelainicialdasúl-
timasversõesatéadatadapublica çãodestelivrodossistemassupracitados,
Android,IOSeWindowsPhone,respectivamente.
Figura2.1:Sistemasoperacionaismóveis
Estesistemafocabastantenaexperiênciadousuárioeemumaproposta
diferenciadadeinterface. Natelainicialpodemosverdiversosquadros,no
lugardeícones—estesquadrossãoconhecidospor tiles.Estestilespodem
mostrarinforma çõesatualizadasatodomomento,tantocominforma ções
locaisdosistema,quantocominforma çõesonline.
Diferentedosíconesdasaplica ções,ostilesnãoselimitamaumpor
4
E-book gerado especialmente para 


## Página 11

CasadoCódigo Capítulo2. EstamosnaEraMobile
aplicativo.Ousuáriopodedecidirfixartilesdiversosparaomesmoaplicativo.
Umexemplodissoseriaoaplicativo pessoas,queagrupaasinforma çõessobre
seuscontatos.Casovocêqueira,podeinserirumtileparaabriresteaplicativo,
ouatémesmoparaabri-lodiretamentenoperfildedeterminadapessoa.Por
estesmotivosaMicrosoftconsideraseusistemaoperacionalcomoosistema
maispersonalizáveldomercado.
Antesdestesistema,aMicrosoftjáhaviacriadoumapropostaparasis-
temasoperacionaismóveis,tantoparasmartphonesquantoparapocketPCs.
Estesistemaeraconhecidocomo WindowsMobile.Diferentedoquemuitas
pessoaspensam,oWindowsPhonenãoéumacontinua çãodoWindowsMo-
bile;eleéumsistemanovo,totalmentereescritoeatémesmoincompatível
comseu“irmãomaisvelho”. Entretanto,apartirdoWindowsPhone8,o
sistemapossuium kernelcompartilhadocomoprópriosistemaoperacional
Windows,conhecidocomo WindowsNT.
2.2 Por que desenvolver para Windows Phone?
Essaéumaperguntamuitoválidaequetododesenvolvedordevesefazer
antesdeinvestirtempoparaaprenderumanovaplataforma.Arespostapara
estaperguntapodeparecersimplória,masétotalmenteválida. Esteéum
sistemanovoepoucoexplorado,diferentedaslojasdeaplicativosjásatu-
radasnosconcorrentes. Claroqueissonãoquerdizerquevocênãodeva
desenvolverparaasoutrasplataformas,pelocontrário,naminhaopinião,as
trêsplataformasqueciteisãototalmenteválidasparaumdesenvolvedornelas
apostar.
Alémdisso,omarketsharedoWindowsPhonevemaumentandomaisde
100%aoanodesde2011,oquefazcomqueelesetorneosegundosistemaop-
eracionalmaispopularemdiversospaíses(incluindoBrasil),perdendoape-
nasparaoAndroiddaGoogle.AlgumaspesquisasindicamqueoWindows
PhonedeveultrapassaroIOSdaAppleemlargaescalaaté2015.
CasovocêjáconheçaC #eaplataforma.NET,vocêjápossuiumagrande
vantagem,poiscomoháestekernelcompartilhadoentreoWindowseoWin-
dowsPhone,épossívelcompartilharboapartedeseucódigoentreasdifer-
entesplataformas.Sejáconheceaplica çõesWPFouaplica çõesWindows8/8.1
5
E-book gerado especialmente para 


## Página 12

2.3. Oquevocêencontraránestelivro CasadoCódigo
queutilizamalinguagemXAMLcomointerface,vocêsóterádeaprender
comoutilizarasAPIsdisponíveisparaconsumirosrecursosdodispositivo.
ÉpossívelpublicarseusaplicativosfacilmenteatravésdalojaWindows
Store. Todososusuáriospodemacessá-laatravésdeseusdispositivoseen-
contrarseusaplicativoslá.Casovocêjápossuaumacontadedesenvolvedor
paraalojadeaplicativosdoWindows8/8.1,vocêpodeutilizaramesmaconta
parapublicarseusaplicativosmóveis.
2.3 O que você encontrará neste livro
Estelivroéescritoparadesenvolvedoresquejápossuemconhecimentodos
principaisconceitosrelacionadosàorienta çãoaobjetosequejátiveramcon-
tatocomalinguagemC #epreferencialmentecomaWindowsRuntime.
Parafacilitaracompreensãodedesenvolvedoresmenosexperientesnessa
linguagem,serãodadaspequenasexplica çõessobrealgunsaspectosdalin-
guagem.
Nocapítuloinicialiremosdesenvolverumaaplica çãodetesteparatermos
nossaprimeiraexperiência,edepoisvamosconstruirumaaplica çãoatéofim
dolivro.
Oscapítulosseguintesirãoabordarconceitosqueenvolvemdesdeacri-
açãodeumaboainterfaceatéaconexãocomdados,GPS,integra çãodesis-
temasemuitomais.Éimportantefomentarqueasaplica çõesnestelivronão
vãoconsiderartodosospossíveispadrõesarquiteturaisemelhoriasdeperfor-
mance.Comoesteéumguiaparainiciantesnaplataforma,serãopriorizados
exemploscomclareza,facilidadeefuncionalidadesdiversasdosistema.
Todos os exemplos apresentados aqui poderão ser encontrados no
repositório:
https://github.com/gabrielschade/LivroWindowsPhone8.1.
Qualquerdúvidaquevocêencontrarvocêésóbuscarajudanogrupode
discussão:
http://bit.ly/WPgrupo
Ametadestelivroéencorajareiniciaroleitoracriaraplica çõesmóveis,
nãosónosistemaabordado,masemqualqueroutro,sendoumprimeiro
passoparaodesenvolvimentonestanovaeradedispositivos.Esperoquevocê
6
E-book gerado especialmente para 


## Página 13

CasadoCódigo Capítulo2. EstamosnaEraMobile
consigaaproveitaroconteúdodestelivrodeformafluida,simplesedivertida,
equeelepossaserumbomguiaparasuanovajornada.
2.4 Antes de começarmos
Antesdecome çarmosafalardeaplica çõesmóveis,paradigmasdeprogra-
maçãoetudomais,énecessárioquevocêjátenhafeitoodownloaddasfer-
ramentasnecessárias. Primeiroprecisamosterumambientededesenvolvi-
mento:nestelivroseráutilizadoo VisualStudio2013Ultimate —casonão
possuaestaferramenta,vocêpodebaixarumaversãogratuitadoVisualStu-
dio2012:
http://www.visualstudio.com/en-us/downloads#
d-express-windows-phone
EoSDK(softwaredevelopmentkit)podeserbaixadoaqui:
http://dev.windowsphone.com/en-us/downloadsdk
ÉimportantesalientarquevocênãoprecisadeumdispositivoWindows
Phoneparatestarsuasaplica ções,jáqueoVisualStudiopossuiumemulador
queiránosajudarcomisso.Entretanto,apesardeserumbomemulador,eu
aconselhoaodesenvolvedorter,sim,umdispositivocomestesistemapara
testarsuasaplica çõesquepossuamfinscomerciais,bemcomoparagarantir
umaboaexperiênciaeusabilidade.
Tendoessasferramentasemmãoseumaboano çãodeprograma ção,você
estaráaptoaseguirnestelivro,criandonopróximocapítulosuaprimeira
aplicaçãoparaWindowsPhone.
7
E-book gerado especialmente para 


## Página 14

E-book gerado especialmente para 


## Página 15

Capítulo3
ConhecendooSDKecriando
nossaprimeiraaplica ção
Nestecapítuloiremosconhecerumpoucomelhorokitdedesenvolvimento
paraWindowsPhone(SDK)eseusprincipaisrecursos.Teremosumaintro-
duçãoaoambientededesenvolvimentonoVisualStudioecriaremosuma
primeiraaplica ção. Dessaforma,vamosteraexperiênciadetestarnosso
aplicativoeconheceroemulador,bemcomooutrasferramentasquenosaju-
darãoaolongodoprocessodedesenvolvimento.
NoVisualStudio,vocêdevesercapazdecriarprojetosquepossuema
plataformaWindowsPhonecomoalvo. Parafazerisso,selecioneaop ção
File -> New -> Project ,edepois,otipodeprojeto WindowsPhone
Apps,conformeafigura 3.1.
E-book gerado especialmente para 


## Página 16

CasadoCódigo
Figura3.1:NovoprojetoparaWindowsPhone
Vocêveráqueexistemdiversostemplatesdeaplicativos,masnãoseas-
suste:todoselestêmumpropósitodefinido—algunsirãoapenascriaratal-
hosparaprojetos,comoporexemplo, Hub Appou Pivot App. Masmesmo
quevocêescolhaaop ção Blank App,vocênãoestaráprivadodestesrecur-
sos.Abordaremosestescomponentesaolongodolivro,porémagorairemos
escolheraop ção Blank Appcomotemplateparanossoprimeiroprojeto.
Apóscriarseuprojeto,vocêveráqueestaIDEfornecetudooquepre-
cisamosparaconstruirmosnossaApp,desdeacria çãodainterface,deseu
code behindeatéferramentasdeteste. Aolongodolivroiremosexplorar
váriosdestesrecursosparaquevocêpossacriaromelhoraplicativopossível.
Agoravocêjápodeexecutarsuaaplicação!Quandofizerisso,seráaberto
umemuladordoWindowsPhoneemseuWindowsDesktop,queficaráem
umambienteisoladoevirtualizado,imitandoumdispositivototalmentesep-
aradodeseucomputador. Obotãoparainiciaroemuladortambéméuma
listadesele ção;nelapoderemosescolherdiversasop çõesdiferentesdeemu-
ladoreatémesmotestaremnossodispositivo.Afigura 3.2ilustraisso.
10
E-book gerado especialmente para 


## Página 17

CasadoCódigo Capítulo3. ConhecendooSDKecriandonossaprimeiraaplica ção
Figura3.2:EmuladoresparaWindowsPhone
3.1 Criando nossa primeira aplicação e con -
hecendo o emulador
Comovocêdeveternotadoaocriaroprojeto,tambémfoicriadooarquivo
MainPage.xaml. Comoonomesugere,eleéapáginaprincipaldonosso
aplicativo,mascomovocêpodever,nãoéoúnicoarquivoquepossuímosno
projeto.VamosagoraconheceraestruturabásicadeumaplicativoWindows
Phone.
Oarquivo MainPagenãoéoúnicoquepossuiextensão XAML(eX-
tensible Application Markup Language), nossoprojetotambémcontacom
oarquivo App.xaml. Elepermitequedeclaremosrecursosglobais, ou
seja, quepoderãoseracessadosatravésdediferentespáginasecontroles
em nosso aplicativo. Este arquivo por padrão vem preenchido apenas
comasdeclara çõesdenamespaces. Alémdo App.xamltambémháum
App.xaml.cs,queéo code-behinddestearquivo,istoé,énelequeestãoas
definiçõesdosmétodosC #queafetamtodaaaplica çãoemumcontextomais
amplo.Porexemplo,énestearquivoquesãodefinidososmanipuladoresdos
eventosdisparadosduranteociclodevidadaaplica ção,taiscomo, Closinge
Deactivated.
11
E-book gerado especialmente para 


## Página 18

3.1. Criandonossaprimeiraaplicaçãoeconhecendooemulador CasadoCódigo
VocêtambémpoderánotarapastaAssetsnaraizdeseuaplicativo.Elajá
estarácomalgunsarquivos,comoasimagensqueserãoutilizadasnostilese
comoíconedesuaaplica ção.
Alémdosjácitados,háumcomponenteimportantíssimoparaqualquer
aplicaçãoWindowsPhone:trata-sedoarquivo Package.appxmanifest.
Elepossuiosmetadadossobresuaaplica ção,oqueenvolveoíconedesua
aplicação,otipodotilequeseráexibido,quaisrecursosdosistemaopera-
cionalsuaaplica çãoprecisaparafuncionarcorretamente(listadecontatos,
porexemplo),recursosdehardware(giroscópioouNFC,porexemplo)eaté
osdadossobreopacotedeseuaplicativonaloja.OVisualStudiopossuiuma
interfacebastanteamigávelparaalterarestasconfigura ções,comoilustraa
figura3.3.
Figura3.3:ArquivoManifest
Agoraquejáconhecemosaestruturadenossoprojeto,vamosabrirnova-
menteoarquivo MainPage.xamleadicionarotítulodenossapáginacomo
“HelloWorld”.Tambémexploreumpoucoacaixadeferramentaseinsiraal-
gunscontrolesnapáginadoaplicativo. Éinteressanteincluirumcampode
12
E-book gerado especialmente para 


## Página 19

CasadoCódigo Capítulo3. ConhecendooSDKecriandonossaprimeiraaplica ção
textoparavermosocomportamentodoteclado.Noexemploaseguirforam
adicionadosalgunselementosnapágina:
<Grid>
<Grid.RowDefinitions>
<RowDefinition Height= "Auto" />
<RowDefinition Height= "*" />
</Grid.RowDefinitions>
<StackPanel x:Name= "TitlePanel" Grid.Row= "0"
Margin= "12,17,0,28" >
<TextBlock Text= "PRIMEIRA APP"
Style= "{ThemeResource TitleTextBlockStyle}" Margin= "12,0" />
<TextBlock Text= "Hello World" Margin= "9,-7,0,0"
Style= "{ThemeResource HeaderTextBlockStyle}" />
</StackPanel>
<StackPanel x:Name= "TitlePanel" Grid.Row= "0"
Margin= "12,17,0,28" >
<TextBlock Text= "PRIMEIRA APP"
Style= "{ThemeResource TitleTextBlockStyle}"
Margin= "12,0" />
<TextBlock Text= "Hello World"
Style= "{ThemeResource HeaderTextBlockStyle}"
Margin= "9,-7,0,0" />
</StackPanel>
<StackPanel Grid.Row= "1" Margin= "12,0" >
<StackPanel Orientation= "Horizontal" >
<TextBox TextWrapping= "Wrap" Text= "TextBox"
Margin= "10" Width= "220" />
<Button Content= "Button" Foreground= "White" />
</StackPanel>
<RadioButton Margin= "10,0" Content= "RadioButton" />
<CheckBox Margin= "10,0" Content= "CheckBox" />
13
E-book gerado especialmente para 


## Página 20

3.1. Criandonossaprimeiraaplicaçãoeconhecendooemulador CasadoCódigo
</StackPanel>
</Grid>
Agoravamoscome çaraconheceroemulador,paraissoprecisamosexe-
cutarnossaaplica ção!
Figura3.4:Primeiraaplica çãoexecutando
Nestemomentoéinteressantequevocêexploreumpoucooemuladore
dêumapasseadapelosistema.Paravoltaràtelainicialdosmartphoneemu-
lado,pressioneatecla Windows.Vocêtambémpodeutilizaromousepara
simulareventosdetouch;aoclicar,manterocliquepressionadoemovero
mouseparaaesquerda,vocêveráalistadeaplicativosinstaladosnoemu-
14
E-book gerado especialmente para 


## Página 21

CasadoCódigo Capítulo3. ConhecendooSDKecriandonossaprimeiraaplica ção
ladoreiráencontrar,inclusive,anossaaplica ção.
Dica: utilizar o teclado do computador
Nafigura3.4,vocêpodenotarqueotecladoestávisívelequepara
digitarvocêpodepressionarasteclascorrespondentesnoemuladorcom
omouse.Masotecladodoseucomputadortambéméumaalternativa
paradigitartextos. Alémdisso,háumamaneiradeocultaroteclado
virtualdoemulador,paraissovocêdevepressionaratecla Page Down.
Casoqueiraativarotecladodoemuladornovamente,utilizeatecla Page
Up.Apesardeserumrecursointeressante,nãoébommantê-losempre
ligado,poisvocêpoderáesquecerdeutilizarotecladocorretoparade-
terminadocampo.FalaremosdissoquandoabordarmosoassuntoUser
Experience4.
Observequeaoladodoemuladordosmartphoneháumasériedebotões
queexecutamfun çõescomogirarosmartphonevirtual,simularmultitouch
ouaplicarzoom.OúltimobotãoabreumanovajanelachamadaAdditional
Tools,naqualvocêpodetestaroacelerômetro,GPS,baterscreenshotsdeseu
aplicativoeoutros.
3.2 Configurando seu dispositivo e sua conta
como desenvolvedor
Certo,agoranósjáexperimentamosdeumaformamuitobrevecomoéde-
senvolverparaWindowsPhoneetestaroaplicativoatravésdeumemulador.
Entretanto,comoeujáhaviamencionado,podeserimportantetestarseus
aplicativosemumdispositivoreal,principalmenteopera çõesqueenvolvem
câmerasesensoresdosmartphone. Masparaisso,vocêprecisarádeuma
contadedesenvolvedorWindowsPhone,oquelhedarádireitoafazero
deploydesuaaplica çãoemumdispositivoreale,claro,permitiráquevocê
publiqueseuaplicativonaloja.
Primeiro,énecessárioterumacontaMicrosoft,comoume-maildoOut-
look,porexemplo. Tendoisso,bastapreencheroregistronapágina http:
15
E-book gerado especialmente para 


## Página 22

3.3. Blend CasadoCódigo
//migre.me/hCfN4epagaraquantianecessária. Apósjáterumacontade
desenvolvedor,vocêpodeprocurarpeloaplicativo Windows Phone Developer
Registration,quefoiinstaladojuntocomoSDK.Conectandoseudispositivo
einformandoosdadosdesuacontadedesenvolvedor,épossívelcadastrá-
lo,demodoquevocêpossafazerostestesdeseuaplicativoemseupróprio
dispositivo.
Comacontadedesenvolvedorativa, vocêtambémpodeacessarum
dashboardnoportaldedesenvolvedoresdoWindowsPhone,nolink http:
//dev.windowsphone.com/. Nelaépossívelpublicarsuasaplica çõeseveri-
ficarrelatóriossobresuasvendas.
3.3 Blend
UmoutrocomponentedoSDKquevocêtambémvaigostardeconheceréo
BlendforVisualStudio . Estaferramentadeveserutilizadaparaprojetare
criartodoodesigndesuaaplica ção.OBlendeoVisualStudiosãototalmente
integrados,ouseja,trabalhamcomosmesmostiposdearquivosemanipulam
osmesmoselementosdeinterface.Vocêpode,porexemplo,abriraaplica ção
queacaboudecriarnoBlendeveráumatelaparecidacomadafigura 3.5.
Figura3.5:BlendparaWindowsPhone
16
E-book gerado especialmente para 


## Página 23

CasadoCódigo Capítulo3. ConhecendooSDKecriandonossaprimeiraaplica ção
Apesardestevisualde“softwareparadesigners”,nãoseengane:oBlend
tambémé,sim,umcomponenteimportantíssimoparadesenvolvedores.As-
simcomooVisualStudio,elefazpartedaconstru çãodeseuaplicativo,du-
ranteasmudan çasnasuainterface. Vocêpodetestareexecutá-lonoemu-
lador,assimcomofaznoVisualStudio.
Apesardeserpossívelcriaranima çõesatravésdecódigonoVisualStudio,
vocêpodecriarumStoryBoardetrabalharcomanima çõesdeformavisuale
maisamigávelnoBlend.Asabas Projectse Assetssãomuitosimilaresàsabas
existentesnoVisualStudio,entãovocêpodeexplorá-lasporsisóeperceber
aspequenasdiferen çasentreelas.
Aaba Statesserveparacriarestadosdiferentesemsuainterface,sendo
quecadaestadopossuiumconjuntodevaloresparaumdeterminadogrupo
depropriedades. Lávocêtambémpodecriartransiçõesentreeles,oqueé
outrafuncionalidadeinteressanteparasetestaragora.
Porfim,naaba Device,pode-sealterarasconfigura çõesdodispositivo
virtualexibidoparatestarsuainterfaceemdiferentestemaseconfigura ções.
Façaalgumasaltera çõesemsuapáginaeteste-anovamente.Casovocêvolte
paraoVisualStudio,seránotificadodequehouvemudan çasnoprojetoeque
eleserárecarregado.
Estafoinossaprimeiraaplica ção!Vocêpodeencontrá-laemhttp://bit.ly/
primeiraApp8-1.
17
E-book gerado especialmente para 


## Página 24

3.3. Blend CasadoCódigo
Figura3.6:Primeiraaplica çãoparaWindowsPhone
18
E-book gerado especialmente para 


## Página 25

Capítulo4
Utilizandocomponentesdo
sistemaparamelhorara
experiênciadousuário
VocêjáouviufalardoconceitoUX( User eXperience)?Esteconceito,muito
difundidonaáreadeengenhariadeusabilidade,trata-sedecomosuaapli-
caçãointeragecomousuárioedecomoelesesenteaousarseuaplicativo.A
experiênciadousuárioéalgoimportantíssimoparaqualqueraplica ção,mas
nomercadodeaplicativosmóveisissoéaindamaiscrítico,poisvocêconcorre
comoutrosmilharesdeaplicativosquesãomuitofáceisdesereminstaladose
testados.Vocêprecisagarantirqueaexperiênciadousuáriocom seuaplica-
tivosejaótima. Nestecapítuloveremosalgunspontosquepodemajudá-lo
nisso.
E-book gerado especialmente para 


## Página 26

4.1. Princípiosdedesign CasadoCódigo
ÉimportantevocêsempreteremmentequeosprincípiosdedesigneUX
definidosparaoWindowsPhonenãosãoregra,esim,umguia.Aplicativos
comooFacebook,porexemplo,utilizampoucoscomponentesdosistema,
mastrazemumaexperiênciaagradável. Entãolembre-se,sãoguiasedicas,
nãopadrõeseregras.
4.1 Princípios de design
CasovocêpossuaumsmartphoneWindowsPhoneoujátenhautilizadoum,
vocêdeveternotadoqueatipografiaeaspáginasdesenhadasparaWindows
Phonepossuemumaspectosemelhante.Elasutilizammuitodoconceitode
clean,ouseja,atelapossuipoucaslinhas,grades,bordasetc.,focandomais
noconteúdoquedevesermostrado.Asanima çõesetransi çõestambémsão
amplamenteutilizadasnasaplica çõesenoprópriosistemaoperacional,oque
vocêpodenotarutilizandooemulador.
Nossoaplicativojáestáaptoparaserexecutadotantonomodoretrato
quantonomodopaisagem.Aoalternarentreumeoutroatravésdoemulador
vocêveráqueháumaanimaçãodetransi ção,issotudoparaqueosistema
pareçamaisvivoemelhoreaexperiênciadousuárioaoutilizarosaplica-
tivos. Aspróprias live tilesdasaplicaçõestambémestãoconstantementese
alterandoparamostrarnovasinforma çõesaousuário. Issocriaumainter-
açãomútua,dousuáriocomosistemaedosistemacomousuário.
Oúltimopontoetalvezomaisimportanteparaaexperiênciadousuário
nestaplataformaé: tireproveitodosistemaoperacional . Existemalguns
recursosconhecidoscomo Contracts,quepermitemquevocêinterajacom
asoutrasaplica çõesjáinstaladasnodispositivodeformaindiretaatravés
dosistemaoperacional aolongodestelivroveremoso ShareContract 8.4.
Porexemplo,sevocêcriarumaplicativodefotos,nãoprecisarácriarinte-
graçõescomoFacebookouInstagram,massimapenassecomunicarcomo
sistemaoperacionaleelesaberáondevocêpodepublicarsuasfotos,sendo
umamaneirabastantesimpleseconvenientedeintegrarseusaplicativos.
Osprincípiosdedesignnãoterminamaqui. Vamosvê-losapartirda
construçãodeumaplicativoaolongodestelivro,masagorairemoscome çar
onossonovoaplicativo.
20
E-book gerado especialmente para 


## Página 27

CasadoCódigo Capítulo4. Utilizandocomponentesdosistemaparamelhorara...
4.2 Começando nosso aplicativo
Vamos começar a construir nosso aplicativo real. Ele será desenvolvido
aolongodetodoolivroecomeleexemplificareiasprincipaisfuncionali-
dadesparaodesenvolvimentodeaplicativosnestaplataforma.Criaremosum
aplicativodecompras,noqualvocêpoderáprocurarporprodutos,cadastrar
umperfildecomprador,indicarosprodutosaumamigoeumasériedefun-
cionalidadesqueiremosveraolongodolivro.
Umaplicativomóvelnestalinhanormalmentevemacompanhadode
umainfraestruturaparaoswebservices, para, porexemplo, fazeracon-
sultadosprodutos. Estasinforma çõesprecisamestaremalgumabasede
dados—geralmentelocalizadananuvem—paraquepossaseracessada
dequalquerlocalapartirdosmartphone. Vamoscriarumaestruturalo-
calcompoucosdadosparaquevocêpossavisualizarcomoseriaaaplica ção
real,masdeixaremosclaroviacomentárionocódigo-fonteospontoschaves
ondechamaríamososservi çosweb,paraquevocêcompreendacomoseriao
cenárioemumaaplicaçãoreal.
Paracomeçar,criaremosumapáginainicial,naqualousuáriopoderá
decidirentrecriarumacontadecomprador,entrarcomumacontajáexis-
tente,ouaindaentrarnalojasemcriarumaconta(nesteúltimomodoele
nãopoderáfazercomprassemefetuarologin). Comovocêdeveterperce-
bido,estatelaseráextremamentesimples,precisandoapenasdetrêsbotões
edotítulodanossaaplica ção. Vamoscriarumnovoprojetoeconstruira
páginadozero.
Jávimosoprocessodecria çãoanteriormente.Vocêdeverárepeti-losele-
cionandonovamenteotemplate Blank Appsnomódulo Windows Phone Apps,
masdestavezdaremosonome CompreAquiparaoaplicativo.Aofazerisso,
teremosamesmaestruturadeprojetoqueconhecemosnocapítuloanterior.
Vamoseditaroarquivo MainPage.xamlparaquecumpranossasnecessi-
dades,masantesdesairalterandoolayoutcomofizemosnaoutraaplica ção,
vamosconhecerosgerenciadoresdelayout.
21
E-book gerado especialmente para 


## Página 28

4.3. Gerenciadoresdelayout CasadoCódigo
4.3 Gerenciadores de layout
Osgerenciadoresdelayoutsãocomponentesdetelanãovisuaisquenosauxil-
iamnaorganiza çãodositensnapágina.Elessãoespecialmenteúteisquando
falamosdedispositivosquepodemcontertamanhoseresolu çõesdeteladifer-
entes. Paraqueoscontrolesnãofiquemdistorcidosouemlocaisdedifícil
acessoparaousuário,nósosutilizamos.
Todososgerenciadoresdelayoutseencontramnamesmacaixadefer-
ramentaquevocêutilizaparaadicionarumbotãonapágina,porexemplo.
Elessãotratadosdamesmaformaqueosoutroscontroles;alémdisso,cada
gerenciadorfuncionadeumaformaparticular.Ireiexplicá-losparaquevocê
possaaproveitaromelhordecadaumdeles.
OcontroleGridéumgerenciadordelayoutbastanteutilizado.Aocriar
umapáginapadrão,jápodemosverqueelautilizaestecomponente. Ele
servebasicamenteparasepararasuapáginaemumlayouttabular,ouseja,
emformatodetabela.Vocêpodedefinirlinhasecolunasecadacontroleirá
preencheroconteúdodesuarespectivacélula,comoafigura 4.1ilustra.
22
E-book gerado especialmente para 


## Página 29

CasadoCódigo Capítulo4. Utilizandocomponentesdosistemaparamelhorara...
Figura4.1:GerenciadordelayoutGrid
Comovocêpôdevernafiguraanterior,oGridestádefinidoparaterduas
linhaseduascolunas,ecadacélulapossuiumretângulodeumacordiferente.
Issotudoédefinidonocódigo XAMLaseguir.
<Grid x:Name= "ContentPanel" >
<Grid.ColumnDefinitions>
<ColumnDefinition/>
<ColumnDefinition/>
</Grid.ColumnDefinitions>
<Grid.RowDefinitions>
23
E-book gerado especialmente para 


## Página 30

4.3. Gerenciadoresdelayout CasadoCódigo
<RowDefinition Height= "*" />
<RowDefinition Height= "*" />
</Grid.RowDefinitions>
<Rectangle Fill= "blue" ></Rectangle>
<Rectangle Grid.Column= "1" Fill= "green" ></Rectangle>
<Rectangle Grid.Row= "1" Fill= "Red" ></Rectangle>
<Rectangle Grid.Row= "1" Grid.Column= "1" Fill= "yellow" >
</Rectangle>
</Grid>
Nãohánenhummistérionocódigoparagerarumgerenciadordestetipo:
bastacriá-lo,definirsuasconfiguraçõesparalinhasecolunaseinseriroscom-
ponentes.Entretanto,algumasobserva çõesdevemserlevadasemconta.Note
quenadefini çãodecolunaseunãoespecifiqueiapropriedade Width;desta
forma,elasocupamexatamenteomesmoespa ço. Omesmoacontececom
aalturadaslinhasdefinidascomocaractere * (asterisco),queéutilizado
comocoringaparainformarqueaalturadalinha(oularguradacoluna)dev-
eráocupartodooespa çorestante.Nocasodeasduasutilizaremesserecurso,
oespaçorestanteécompartilhadoentreelas.
Umpontoimportantequedeveserlembradosempreéqueestesgeren-
ciadoresdelayoutcomumentesãoaninhados,ouseja,émuitocomumque
hajaváriosdestescomponentesdentrodeoutrosgerenciadoresouatédentro
deumcomponentedomesmotipo. Noexemploaseguirveremososcom-
portamentosdo StackPaneleoaninharemosaumcomponente Grid.
O StackPanel,comoopróprionomejásugere,éumpainelparaempilhar
componentes. Ocomportamentodestecomponenteestáfortementevincu-
ladoàsuapropriedade Orientation,quedefineseelevaiempilharoscompo-
nentesumacimadooutroouumaoladodooutro.
Nestegerenciadordelayout,diferentedo Grid,éobrigatórioopreenchi-
mentodaspropriedadesdedimensõesdoselementos.Noexemploanterior,
nãoprecisamosdefinirnemaalturaenemalarguradosretângulosno Grid
—elesocuparamacélulatodaautomaticamente. Mascomonãoháocon-
ceitodecélulaemum StackPanel,énecessárioinformarmosapropriedade
referenteàorienta çãodopainel,ouseja,casoopainelestejanavertical,pre-
24
E-book gerado especialmente para 


## Página 31

CasadoCódigo Capítulo4. Utilizandocomponentesdosistemaparamelhorara...
cisamospreencherovalordealtura,ecasoestejanahorizontal,precisamos
informaraomenosovalordalargura.
Afigura4.2ilustradoispainéisdestetipo,cadaumcomaorienta çãodifer-
ente,eambosestãoseparadosemlinhasdeum Gridqueoscircunda.
Figura4.2:GerenciadordelayoutStackPanel
Apesardenãotersidoexemplificado,quandoaorienta çãodopainelestá
definidacomo Horizontal,nóspodemosescolherseoscomponentessãoem-
pilhadosdaesquerdaparaadireitaoudadireitaparaaesquerda,atravésda
propriedade FlowDirection.Vejaocódigoparacriarapáginailustrada:
<Grid>
25
E-book gerado especialmente para 


## Página 32

4.3. Gerenciadoresdelayout CasadoCódigo
<Grid.RowDefinitions>
<RowDefinition Height= "*" />
<RowDefinition Height= "*" />
<Grid.RowDefinitions>
<StackPanel Grid.Row= "1" >
<Rectangle Fill= "blue" Width= "75" Height= "75" ></Rectangle>
<Rectangle Fill= "green" Width= "75" Height= "75" ></Rectangle>
<Rectangle Fill= "Red" Width= "75" Height= "75" ></Rectangle>
<Rectangle Fill= "yellow" Width= "75" Height= "75" ></Rectangle>
</StackPanel>
<StackPanel Grid.Row= "2" Orientation= "Horizontal" >
<Rectangle Fill= "blue" Width= "75" Height= "75" ></Rectangle>
<Rectangle Fill= "green" Width= "75" Height= "75" ></Rectangle>
<Rectangle Fill= "Red" Width= "75" Height= "75" ></Rectangle>
<Rectangle Fill= "yellow" Width= "75" Height= "75" ></Rectangle>
</StackPanel>
</Grid>
Oterceirocomponentequeiremosmostraraquiéo Canvas.Elepossui
layoutlivre,ouseja,aposi çãodoselementoséabsolutaeédefinidapelas
propriedades Canvas.T ope Canvas.Left,queindicamodeslocamentodoele-
mentodabordasuperioredabordaesquerda,respectivamente.
Estegerenciadorgeralmenteéutilizadoparapainéisondehámovimen-
taçãodositenspormeiodeumgesto,ouparafazerdesenhos. Deve-seter
cuidadoaoutilizarestetipodecomponente,poiselepodesecomportarde
maneirainesperada,devidoàposi çãoabsolutadoselementosnelecontidos.
Afigura4.3mostraosretângulosemumpaineldotipo Canvas.
26
E-book gerado especialmente para 


## Página 33

CasadoCódigo Capítulo4. Utilizandocomponentesdosistemaparamelhorara...
Figura4.3:GerenciadordelayoutCanvas
OCanvasébastantelivree,comopodemosver,ocódigoparainserirel-
ementosneleébemsimples:bastacolocaroelementoaninhadoedefiniras
propriedadessupracitadas.Tambémépossívelmoveroscomponenteslivre-
mentecomomouseatravésdainterfacedoVisualStudio.Paragerarafigura
4.3,foiutilizadoocódigoaseguir.
<Canvas Grid.Row= "1" >
<Rectangle Fill= "blue" Width= "175" Height= "175"
Canvas.Left= "272" Canvas.Top= "262" ></Rectangle>
<Rectangle Fill= "green" Width= "175" Height= "175"
27
E-book gerado especialmente para 


## Página 34

4.4. Criandoapáginadeboas-vindas CasadoCódigo
Canvas.Left= "38" Canvas.Top= "45" ></Rectangle>
<Rectangle Fill= "Red" Width= "175" Height= "175"
Canvas.Left= "272" Canvas.Top= "45" ></Rectangle>
<Rectangle Fill= "yellow" Width= "175" Height= "175"
Canvas.Left= "38" Canvas.Top= "262" ></Rectangle>
</Canvas>
4.4 Criando a página de boas -vindas
Comisso,nósjáconhecemososprincipaisgerenciadoresdelayoutqueire-
mosutilizarparaacria çãodaspáginasdenossoaplicativo. Comocitamos
anteriormente,aprimeirapáginaseráapáginadetítulodoaplicativo.Nela,
ousuáriopoderáescolherentrefazerlogin,criarumacontadeusuárioou
entrarnalojasemcriarumaconta.
Nãoseráexigidoquevocêcrieapáginaexatamenteigualàqueiremos
mostrarcomoexemplo,maslembre-sedeutilizarosgerenciadoresparaque
seulayoutcomporte-sedemaneiracorreta.Aoterminarsuapágina,eladeve
separecercomafiguraaseguir.
28
E-book gerado especialmente para 


## Página 35

CasadoCódigo Capítulo4. Utilizandocomponentesdosistemaparamelhorara...
Figura4.4:Páginadeboas-vindas
<Page>
<!--Declaração de Namespaces-->
<Grid.RowDefinitions>
<RowDefinition Height= "Auto" />
<RowDefinition Height= "*" />
</Grid.RowDefinitions>
<StackPanel Grid.Row= "0" Margin= "10,15,0,0" >
<TextBlock Text= "COMPREAQUI"
Style= "{ThemeResource TitleTextBlockStyle}" />
<TextBlock Text= "Bem-vindo"
29
E-book gerado especialmente para 


## Página 36

4.4. Criandoapáginadeboas-vindas CasadoCódigo
Style= "{StaticResource HeaderTextBlockStyle}" />
</StackPanel>
<StackPanel Grid.Row= "1" Margin= "0,40,0,0" >
<Button HorizontalAlignment= "Stretch" >
Entrar com uma conta
</Button>
<Button HorizontalAlignment= "Stretch" >
Entrar sem uma conta
</Button>
<Button HorizontalAlignment= "Stretch" >
Criar uma conta
</Button >
</StackPanel>
</Page>
Oprojetopodeserencontradonomeugithubpelolink: http://bit.ly/
8-1GITcap4ParteI
Observeafigura 4.4,elaéanossaprimeirapáginadoaplicativo.Como
vocêpodever,elaseguecorretamenteotemplatedepáginasdisponíveise
utilizaosgerenciadoresdelayout,conformeocódigocitadoanteriormente.
Entretanto,estapáginanãoéatrativaparaousuário,elaestásemvida,ex-
tremamentesimplóriaesemnenhumatrativo.
Podemosmelhorarissoatravésdeimagens,corese,claro,ideias.Nova-
mentepeçoparaquetentepensaremalgoantesdeseguircomolivro—tente
pensaremcomoestatelapodesetornarmaisatraenteparaousuárioetente
implementaroquevocêpensouutilizandooVisualStudioeoBlend.Apesar
deestelivroserumguiainicial,ébastanteimportantevocêconfiaremsuas
ideiaseexperimentarporcontaprópria.
Aprimeiracoisaquefaremoséutilizarumaimagemdefundoecriarum
íconeparanossaaplica ção.Tambémvamosalterarumpoucooformatodo
layoutdapágina,removerocabe çalhocomonomedaaplica çãoeosdizeres
“Bem-vindo”.DeixemosqueoGridprincipalquejáécriadoporpadrãocon-
tinuetendoduaslinhas,masvamosfixarotamanhodalinhainferiorpara
30
E-book gerado especialmente para 


## Página 37

CasadoCódigo Capítulo4. Utilizandocomponentesdosistemaparamelhorara...
270.
Opainelinferiorcomosbotõesdeintera çãodeverãoserjogadosparaa
segundalinhado Grid,oquefazcomqueelesfiquemnaparteinferiorda
página,sobrandoumespaçoembrancoconsiderável.Vamospreencheresse
espaçocomoplanodefundoecomotítulodaaplica ção“CompreAqui”.Veja
nafigura4.5comonossapáginajámelhoroubastante.
Figura4.5:Páginadeboasvindas2.0
Linkdoprojetonomeugithub: http://bit.ly/8-1GITcap4ParteII
Nolinkdoprojetosupracitado,vocêpoderáencontrarasimagensque
foramutilizadasparaoplanodefundoecomoícone.Comojávimosante-
riormente,elasestarãonapasta Assetsdonossoprojeto. Atéagorafizemos
31
E-book gerado especialmente para 


## Página 38

4.4. Criandoapáginadeboas-vindas CasadoCódigo
alteraçõesbaseadasemlayouteinserimosalgumasimagens,oquejámuda
bastanteaaparênciadestajanela.
Aindaassim,podemosverqueosbotõesdea çãopermanecemiguaise
tambémpodemosdar-lhesumaaparênciadiferentedopadrão. Paraisso,
podemosutilizardoisconceitosdiferentes: estiloetemplate.
Sevocêjátrabalhoucomweb,vocêdeveestarfamiliarizadocomestecon-
ceito.Eletambémestápresenteno XAMLatravésdatag Style.Comnovos
estilos,podemoscriaraparênciasdiferenciadasparacomponentesjáexis-
tentes,eessesestilospodemserutilizadosemdiferentesníveis.Podemoscriar
umestiloparaumúnicocomponente(quandoalteramossuaspropriedades,
comoporexemplo, Background),podemoscriarumestiloereutilizá-loem
umapáginatodaoupodemoscriarumestiloquepoderemosacessaremtodas
aspáginasdaaplicação.
Templatedecomponentestambéméumestilo—éumconceitopare-
cido,porémmaispoderoso.Oestilovaiselimitaradefiniraspropriedades
doscomponentesdosistema.Porexemplo,vocêpodealteraracordefundo
dobotão,mascomtemplatesvocêpoderáalteraraformadobotão,ouaté
mesmoinserirnovoscomponentesnele. Adefini çãodeumtemplatepara
umcomponentetambéméfeitaatravésdatag Style.
Agoravamosutilizarumtemplatedecomponenteparaalterarmosos
botõesdenossapágina. Parafazerisso,utilizeajanela Document Outline
doVisualStudio(oatalhoparaabri-laé Ctrl + Alt + T ).Estajanelaé
muitoútilparavisualizarmosaorganiza çãodoscontrolesegerenciadoresde
layoutemnossapágina.Parafacilitaracria çãodeumtemplate,procurepor
umdosbotõesdenossapáginaepressioneobotãodireitodomouse. No
menuflutuante,selecioneaop ção Edit Template > Edit a Copy...
conformefigura4.6.
32
E-book gerado especialmente para 


## Página 39

CasadoCódigo Capítulo4. Utilizandocomponentesdosistemaparamelhorara...
Figura4.6:Editarumacópiadotemplatedeumcomponente
Document Outline
Estajanelanosajudaaorganizarmososcontrolesvisuaiseosgeren-
ciadoresdelayoutdenossapágina.Alémdisso,atravésdela,utilizando
obotãodireitodomousepodemoseditartemplateseestilos. Podeser
bastanteútilcasovocênãoconhe çaosestilosquefazempartedosis-
temaoperacional—vocêpode,porexemplo,selecionarumcontrole
TextBlockeescolheracor,tamanhoounomedafonteatravésdeste
atalho.
Apersonalizaçãodetemplateséalgoexcelentepoisvocêpoderáfazeras
33
E-book gerado especialmente para 


## Página 40

4.4. Criandoapáginadeboas-vindas CasadoCódigo
ediçõesnocomponenteapartirdocomponentepadrão,garantindoquesó
perderáocomportamentodoscomponentesqueremover. Aoselecioná-la,
seráexibidaumajanelaparaquesejaminformadosalgunsdadosarespeito
dotemplatequepretendecriar.Insiraonomedotemplatequepreferirese-
lecioneaop ção Applicationnogrupo Define in,issoirágarantirque
otemplatepossaserusadoportodaaaplica ção.
VocêseráredirecionadoparaoarquivoApp.xaml,jáqueéláondeficam
todososrecursosquepodemserutilizadosemtodaaaplica ção.Vocêveráque
háumestilodefinidocomapropriedade T argetType,comovalor Button,e
comapropriedade x:Key,comovalorquevocêinformounajanelaanterior.
Estaéadefini çãodotemplatequeestamoseditando. Vamosfazeralgumas
modificaçõesparaqueobotãofiquedamaneiracomopretendemos.
Antesdefazermosasaltera ções,vamosconhecerumpoucomaissobreos
estilos.Segueocódigo-fonteresumidodoestiloquedefineotemplatepadrão
dosbotões:
<Style x:Key= "LargeButton" TargetType= "Button" >
<Setter Property= "Background" Value= "Transparent" />
<Setter Property= "BorderBrush"
Value= "{ThemeResource PhoneForegroundBrush}" />
<Setter Property= "Template" >
<Setter.Value>
<ControlTemplate TargetType= "Button" >
<Grid Background= "Transparent" >
<VisualStateManager.VisualStateGroups>
<VisualStateGroup x:Name= "CommonStates" >
<VisualState x:Name= "Normal" />
<VisualState x:Name= "Pressed" >
<Storyboard>
<PointerDownThemeAnimation
34
E-book gerado especialmente para 


## Página 41

CasadoCódigo Capítulo4. Utilizandocomponentesdosistemaparamelhorara...
Storyboard.TargetName= "Grid" />
<ObjectAnimationUsingKeyFrames
Storyboard.TargetProperty= "Foreground"
Storyboard.TargetName= "ContentPresenter" >
<DiscreteObjectKeyFrame KeyTime= "0"
Value= "{ThemeResource
ButtonPressedForegroundThemeBrush}" />
</ObjectAnimationUsingKeyFrames>
<ObjectAnimationUsingKeyFrames
Storyboard.TargetProperty= "Background"
Storyboard.TargetName= "Border" >
<DiscreteObjectKeyFrame KeyTime= "0"
Value= "{ThemeResource
ButtonPressedBackgroundThemeBrush}" />
</ObjectAnimationUsingKeyFrames>
</Storyboard>
</VisualState>
<Border x:Name= "ButtonBackground"
BorderBrush= "{TemplateBinding BorderBrush}" >
<ContentPresenter x:Name= "ContentPresenter"
ContentTemplate= "{TemplateBinding ContentTemplate}"
Content= "{TemplateBinding Content}"
Foreground= "{TemplateBinding Foreground}" />
</Border>
</Grid>
</ControlTemplate>
</Setter.Value>
</Setter>
35
E-book gerado especialmente para 


## Página 42

4.4. Criandoapáginadeboas-vindas CasadoCódigo
</Style>
Agoravamosdestrincharestecódigoparacompreendermososignificado
decadacoisa. Asprimeirastagsqueaparecemsãoos Setters,quesimples-
menteaplicamovaloraalgumapropriedade.Oexemploanteriorindicaque
apropriedade Backgrounddobotãoiniciacomovalor Transparent.Alguns
Settersutilizamumanota çãoumpoucodiferente(“ThemeResource~”),que
serveparaobterascores,tamanhosepadrõesdoprópriosistemaoperacional.
Notequetambémpodemosestenderatag Setter,paraocasodeeditarmoso
templatedobotão.Dentrodestatag,nósdefinimososcomponentesvisuais
queformamobotão,comoporexemplo,o Gridprincipalesuasbordas( Bor-
der).
VocêtambémnotaráqueháumgrupodetagschamadoVisualState,sobre
osquaisfalaremosmelhornoscapítulosfuturos.Porenquanto,bastasaber-
mosqueeletratadeumestadodocomponente.Issoquerdizerquecada Visu-
alStatepodeconterdiferentesvaloresparaasmesmaspropriedades,edurante
ofluxodenossaaplica çãopodemosalterarentreestesestados,queapágina
irásereorganizarcompletamentedeacordocomasnovaspropriedades.
TambémháatagStoryBoard,queserefereaanima çõesdeelementos.No
casodoexemploanterior,acordafontedobotãoéalteradaparaumade-
terminadafontequandoeleépressionado.Tambémfalaremosmelhordisso
futuramente.
Apósestaexplica çãosobreosestilos,vocêdeveestaraptoafazerpeque-
nasmudançasnaaparênciadobotão. Emnossoexemplo,vamosremover
o Setterdapropriedade Padding,poisqueremosqueobotãoocupetodoo
espaçodisponível.Tambémcriaremosum Setterparaapropriedade Height
edefiniremosseuvalorpadrãocomo90.Alémdisso,vamosalterarovalor
dos Setters FontFamilye FontSizepara PhoneFontFamilyLighte PhoneFont-
SizeLarge,respectivamente.
Removeremososestados(VisualState) Pressede Disabled,poisnãova-
moscriarumasitua çãoemqueestebotãopossaserdesabilitadoeelenão
deveráalterarsuacorparaospadrõesdosistemaaoserpressionado. Por
fim,removeremostodasaspropriedadesdocomponente Border,excetopela
propriedade Background.
36
E-book gerado especialmente para 


## Página 43

CasadoCódigo Capítulo4. Utilizandocomponentesdosistemaparamelhorara...
Voltando ao nosso formulário e aplicando o template para todos os
botões,podemosvermudan çasemsuaaparência,maselesestãotodoscom
ofundotransparente,dandoumasensa çãodevazio.Parafinalizarestaetapa,
vamospreencherapropriedade Backgrounddosbotõescomosrespectivos
valores: #B2C80000, #B20000C8e #BF0E6400.Estesvaloressãotonstrans-
parentesdevermelho,azuleverde,dandoumpoucomaisdevidaànossatela
inicial,quenestepontodeveestarparecidacomafigura 4.7.
Figura4.7:Páginadeboas-vindasversãofinal
<StackPanel Grid.Row= "1" Margin= "0,40,0,0"
VerticalAlignment= "Bottom" >
<Button Style= "{StaticResource BotaoSemBorda}"
Background= "#B2C80000" HorizontalAlignment= "Stretch" >
37
E-book gerado especialmente para 


## Página 44

4.4. Criandoapáginadeboas-vindas CasadoCódigo
Entrar com uma conta
</Button>
<Button Style= "{StaticResource BotaoSemBorda}"
Background= "#B20000C8" HorizontalAlignment= "Stretch" >
Entrar sem uma conta
</Button>
<Button Style= "{StaticResource BotaoSemBorda}"
Background= "#BF0E6400."
HorizontalAlignment= "Stretch" >
Criar uma conta
</Button >
</StackPanel>
Linkdoprojetonomeugithub: http://bit.ly/8-1GITcap4ParteIII
Oprincipalobjetivodestecapítuloéquevocêconsigadominaroscon-
ceitosbásicossobretemplateseestilos,alémdeentenderqueosprotótipos
queoVisualStudioentregafeitonãosãoregras,elesãoapenasguias.Pode
serinteressanteparaseuaplicativoutilizarascoresdosistemaoperacionaleo
temadousuário—issopodesimoferecerumaótimaexperiênciaecomuma
boaimersão—,masnestecapítuloquismostrarqueestanãoéaúnicaforma
correta.
Existemdiversostutoriaispelainternetfalandosobrecomoseguiros
padrõeseguiasdeinterfacedoWindowsPhone,maspodemosverclara-
mentequeaplicativoscomooFacebook,Twitteretantosoutrospossuemsua
própriaidentidade. Émaisimportanteserumaplicativoqueofereceuma
boaexperiênciadoqueseguirtodosospadrõesjápropostos .
Afigura4.8ilustracomoaspáginasparacriarcontaeentrarcomuma
contadevemseparecer.Tentefazê-lassozinhosenopróximocapítulopas-
saremosporalgunspontosexplicandomelhorcomopodemoscriaraspági-
nasdestetipo.
38
E-book gerado especialmente para 


## Página 45

CasadoCódigo Capítulo4. Utilizandocomponentesdosistemaparamelhorara...
Figura4.8:Páginasparacriarumacontaeentrarnoaplicativo
39
E-book gerado especialmente para 


## Página 46

E-book gerado especialmente para 


## Página 47

Capítulo5
Designdeaplica ções
Jáfalamossobreexperiênciadeusuárioedesigndeaplica ções,masvamos
continuarseguindoestatrilhaparaquenossosaplicativostransmitamuma
boaexperiênciaparaousuário.Nocapítuloanteriorforammostradasduas
páginasjácriadas,agoravamosavaliaraaplica çãosendoexecutadaeapós
issofaremosmelhoriasnocódigo-fonte.
Nesteponto,peçoqueexecuteaaplica çãoqueseencontraemmeugithub
atravésdolink:http://bit.ly/8-1GITcap5ParteI
Efa çaalgunstestescomela,comoporexemplo,navegarnaspáginas,
preencherosformuláriosetc.
5.1 Melhorias de usabilidade
Depoisdefazerestestestes,apontareialgunsproblemasdeusabilidadeque
talvezvocêtambémtenhapercebido.
E-book gerado especialmente para 


## Página 48

5.1. Melhoriasdeusabilidade CasadoCódigo
Navegação:ébastantefácildetectarumproblemacomanavega çãoen-
treaspáginas,apósentraremumadaspáginasqueforamcriadasnãocon-
seguimosvoltarparaapáginainicial. Quandopressionamosobotãovoltar
doemuladoroaplicativoestásendofechado.Felizmenteébastantesimples
solucionaresteproblema,bastacapturarmosomomentoemqueousuário
pressionaestebotãoefazermosaa çãodevoltarapágina.
Abra o arquivo App.xaml.cs, nele há um manipulador para
o evento OnLaunched. Neste método você precisa vin-
cular um manipulador ao evento BackPressed da classe
HardwareButtons ( HardwareButtons.BackPressed +=
HardwareButtons_BackPressed;). O código para implementar
estafuncionalidadeébastantesimples.
private void HardwareButtons_BackPressed ( object sender,
BackPressedEventArgs e)
{
Frame rootFrame = Window.Current.Content as Frame;
if (rootFrame != null && rootFrame.CanGoBack)
{
rootFrame.GoBack();
e.Handled = true ;
}
}
Apesardenãoserumcódigocomplicado,vocênãoprecisasepreocupar
ementendê-loagora,aodecorrerdolivroiremosentendercomofuncionaa
navegaçãoentreaspáginasdoaplicativoeesteconceitoficaráclaroparavocê.
Orientação: nestas novas páginas, a orientação do dispositivo influ-
enciaaorganiza çãodoselementosnapágina. Apágina Entrar.xaml
nãopossuinenhumproblema, entretantoaspáginas MainPage.xamle
CriarConta.xamlpossuemumproblemaseriíssimo. Quandoodisposi-
tivoseencontranomodopaisagem,ouseja,estánahorizontal,algunscam-
posestãosetornandoinalcan çáveisaousuário.
Felizmente, háumgerenciadordelayoutdoqualaindanãofalamos,
chamado ScrollViewer, quecircundaelementosououtrosgerenciadorese
ativabarrasderolagemquandonecessário.Aocircundaropainelquecontém
oselementosnestapágina,nossoproblemaestaráresolvido.
42
E-book gerado especialmente para 


## Página 49

CasadoCódigo Capítulo5. Designdeaplicações
<!-- Início da página -->
<ScrollViewer>
<StackPanel Margin= "10,0" >
<TextBlock FontSize= "{ThemeResource
TextStyleExtraLargeFontSize}" >
Email
</TextBlock>
<TextBox></TextBox>
<!--Outros componentes-->
</StackPanel>
</ScrollViewer>
<!-- Continuação da página -->
Nestamesmapágina,tambémháumoutropequenoproblema:aosele-
cionarocampoe-mail,éexibidootecladoconvencional,masexistemoutros
tiposdeteclado. Ocontextodasitua çãopoderádefinirqualtipodeinfor-
maçãoqueotecladodeveráinserir,porexemplo,paraumcamposomente
numériconãofazsentidoqueotecladoapresenteletras.
Para definir o tipo de teclado que será exibido, utilizaremos a pro-
priedade InputScope.Quandoselecionamosovalordestapropriedadecomo
EmailSmtpAddress,aoserexibido,otecladoexibeumateclapara @eoutra
para.com,conformeilustrafigura 5.1.
43
E-book gerado especialmente para 


## Página 50

5.1. Melhoriasdeusabilidade CasadoCódigo
Figura5.1:Escoposdeteclado
No capítulo anterior, vimos o conceito de estilo e template de com-
ponentes. Váriaspropriedadesdefinidasnostemplatesdoscomponentes
padrõesdoWindowsPhonepossuemsuacolora çãovinculadaaopróprio
smartphone.Emnossaaplica çãonãoédiferente:entrandonasconfigura ções
dodispositivoealterandoascoresdotemapoderemosvermudan çasem
nossainterface.
Casovocêprefiraqueoscomponentessemantenhamiguaismesmocom
aalteraçãodotema,énecessárioquevocêcrieestilos/templatesquenãoeste-
jamvinculadosaosistemaoperacional.Comojávimosaformadecriarum
templateparaumcomponenteedefinirpadrõesparaaspropriedadesdele,
nãoiremosentraremdetalhesagora.
44
E-book gerado especialmente para 


## Página 51

CasadoCódigo Capítulo5. Designdeaplicações
Jápodemosvertodasestasmelhoriasemnossoaplicativo. Paravero
código-fontedoprojetocompletocomestasimplementa çõesacesse: http://
bit.ly/8-1GITcap5ParteII.
Vamosseguiradiante,masfiqueàvontadeparafazeraindamaismelho-
riasnoaplicativo,comoporexemplo,fazercomquesejapossívelacessara
páginadecriaçãodecontaatravésdapáginaparaentrarcomumacontaex-
istente(issoébemcomum,poiscriaumatalhoparaousuárioqueaindanão
possuicontaeentrounestapágina).
5.2 Conhecendo os controles do Windows
Phone
Atéestepontojáconstruímosnossaspáginasdeboas-vindas,criaçãodeconta
eparaentrarnoaplicativoutilizandoumaconta. Agorairemosconstruira
páginaprincipaldenossoaplicativo,ondeousuáriopoderáverosprodutos,
aspromoçõesetudomaisquefazpartedoconceitoprincipaldaaplica ção.
Paraatelaprincipal,utilizaremosum Hub(nasversõesanterioreseste
componenteéconhecidocomo Panorama).Esteéumcontrolebastantecar-
acterísticodoWindowsPhonequejáenglobaboapartedosconceitosdede-
signdosistemaoperacional.
Oconceitodo Hubébastantesimplesdecompreender:bastaimaginar
queapáginadaaplica çãoémaislargaqueoprópriosmartphone. Apesar
devocêterdenavegarnelanahorizontal,trata-sedomesmoconteúdo.Este
conceitoéutilizadoemdiversosaplicativosnativos,comoporexemplo,ohub
depessoasoudefotos,queestáilustradonafigura 5.2.
45
E-book gerado especialmente para 


## Página 52

5.2. ConhecendooscontrolesdoWindowsPhone CasadoCódigo
Figura5.2:HubdefotosdoWindowsPhone
Todaaimplementa çãodegestosparanavegaratravésdo Hubéimple-
mentadanativamentenocontrole,entãoébastantesimplesdeusá-loevocê
veráqueoefeitovisualdeleémuitobacana. Vamosagoracriarumanova
páginaemnossoaplicativoechamá-lade ProdutosHub.
Apóscriarapáginabastaadicionarocontrole Hubeadicionarasse ções
dehub. Cadase çãocorrespondeauma“subpágina”dentrodoHub. Cri-
aremososseguintes: “classificações”,“promoção”e“produtos”,conformeo
códigoaseguir.
<Hub Header= "CompreAqui" >
<HubSection Header= "classificações" >
</HubSection>
<HubSection Header= "promoção" >
</HubSection>
46
E-book gerado especialmente para 


## Página 53

CasadoCódigo Capítulo5. Designdeaplicações
<HubSection Header= "produtos" >
</HubSection>
</Hub>
Porpadrão,ofundodo Hubévazio,assumindoacordefundodoseu
tema(pretooubranco),maspodemospreenchê-locomumaimagempara
melhorarsuaaparência.Porenquanto,deixaremosositenssemnenhumcon-
teúdo,eoresultadodevesersemelhanteàfigura 5.3.
Figura5.3:Hub
Agoravamosconhecerocontrole CommandBar,que,comoonomesug-
ere,éumabarradecomandosparasuaaplica ção.Estabarradecomandosfica
naparteinferiordapáginanomodoretrato,eounocantodireitonomodo
paisagem.
47
E-book gerado especialmente para 


## Página 54

5.2. ConhecendooscontrolesdoWindowsPhone CasadoCódigo
Na CommandBardevemosinserira çõesque,apesardefazerempartedo
contexto,nãoseencaixamemalgumpontonapágina. Emnossoexemplo,
vamoscolocaremnossocomponenteumbotãoparaacessarmosapáginade
pesquisaeumitemdemenuparaacessarmosapáginaparagerenciamentode
conta.Paraadicionarmosestecomponente,precisamosacessarapropriedade
BottomAppBardapágina. Parafazerisso,utilizamosotrechodecódigoa
seguir.
<Page.BottomAppBar>
<CommandBar >
</CommandBar>
</Page.BottomAppBar>
Dentroda CommandBar,podemosinserirnossoscomponentes.Comojá
ditoantes,seráfeitoumbotãoparapesquisaeumitemdemenuparaacessar
asconfiguraçõesdesuaconta.Nestabarra,oscomponentessãoclassificados
comoprimáriosesecundários.Ositenssecundáriossóserãomostradosao
usuáriocasoelepressioneo“...”nocantodireitodabarra,ouseja,sãoclassi-
ficadoscomoa çõesmenosimportantes.
Paracriarobotãodepesquisa(primário),vocêdeveusarocomponente
AppBarButton,umbotãocircularquefoiprojetadoparaserutilizadoneste
componente,dentrodoqualénecessárioincluirum BitmapIconcomo
íconedobotão. Esteíconeseencontranogrupo features iconsdoSDKdo
WindowsPhone.Nesteponto,sua CommandBardeveestarsimilaraocódigo
quesegue.
<Page.BottomAppBar>
<CommandBar>
<CommandBar.PrimaryCommands>
<AppBarButton Label= "pesquisar" >
<AppBarButton.Icon>
<BitmapIcon
UriSource=
"ms-appx:///Assets/CommandBar/feature.search.png" />
</AppBarButton.Icon>
48
E-book gerado especialmente para 


## Página 55

CasadoCódigo Capítulo5. Designdeaplicações
</AppBarButton>
</CommandBar.PrimaryCommands>
</CommandBar>
</Page.BottomAppBar>
Para finalizar, vamos incluir mais um AppBarButton, mas desta vez
comocomandosecundário. Apósfazerissodiminuiremosaopacidadeda
CommandBarem50%,dandoumefeitotransparente.Agoranossabarrade
açõesestáfinalizada,conformeocódigoeafigura 5.4.
<Page.BottomAppBar>
<CommandBar Opacity= "0.5" >
<CommandBar.PrimaryCommands>
<AppBarButton Label= "pesquisar" >
<AppBarButton.Icon>
<BitmapIcon
UriSource=
"ms-appx:///Assets/CommandBar/feature.search.png" />
</AppBarButton.Icon>
</AppBarButton>
</CommandBar.PrimaryCommands>
<CommandBar.SecondaryCommands>
<AppBarButton Label= "sua conta" />
</CommandBar.SecondaryCommands>
</CommandBar>
</Page.BottomAppBar>
49
E-book gerado especialmente para 


## Página 56

5.2. ConhecendooscontrolesdoWindowsPhone CasadoCódigo
Figura5.4:CommandBar
Oúltimocomponentedosistemaoperacionalqueiremosexplicaréo
Pivot,queéumagrupadordepáginascomumfuncionamentoparecido
como Hub,porémcompropósitosdiferentes.Enquantoo Hubservecomo
umacentraldeinforma ções,o Pivotservecomoumseparadordeconteú-
dos,fazendocomquecadaitemseupossuaitensrelacionadosemumcon-
textomaisamplo,masdiferentesentresi.
Vamoscriaragoraapáginaparagerenciamentodeconta.Elacontarácom
umcomponentedotipo Pivotparaorganizarseusconteúdos.Nestapágina,
vamosutilizaromesmoplanodefundodapáginaanterior,eporhorahaverá
umitemchamado“Senha”eoutrochamado“Entrega”.Suapáginadeveconter
otrechodecódigosemelhanteaoquesegue:
50
E-book gerado especialmente para 


## Página 57

CasadoCódigo Capítulo5. Designdeaplicações
<Grid>
<Grid.Background>
<ImageBrush Stretch= "UniformToFill"
ImageSource= "/Assets/Images/Background.jpg" />
</Grid.Background>
<Pivot Title= "SUA CONTA" >
<PivotItem Header= "Senha" >
</PivotItem>
<PivotItem Header= "Entrega" >
</PivotItem>
</Pivot>
</Grid>
Nesteponto,vamospreencheroitem“Senha”comoscamposparaque
ousuáriodigitesuasenhaatual,umanovasenhaeumaconfirma çãoparaa
novasenha.Alémdisso,éclaro,vamosfazerumbotãoparaefetuaratroca
desenha,conformeafigura 5.5.
51
E-book gerado especialmente para 


## Página 58

5.2. ConhecendooscontrolesdoWindowsPhone CasadoCódigo
Figura5.5:Pivot
Agoravamosfazercomqueobotãoqueinserimosnoscomandosse-
cundáriosda Commandnosleveatéesteformulário. Paraissoprecisamos
inserirummanipuladorparaoevento Click.Issoéfeitotantonoarquivo
XAMLquantonoarquivoC #.Vejaoscódigosaseguir:
<CommandBar.SecondaryCommands>
<AppBarButton Label= "sua conta" Click= "btnSuaConta_Click" />
</CommandBar.SecondaryCommands>
private void btnSuaConta_Click ( object sender, RoutedEventArgs e)
{
this .Frame.Navigate( typeof (SuaConta));
}
52
E-book gerado especialmente para 


## Página 59

CasadoCódigo Capítulo5. Designdeaplicações
Falaremosmelhorsobrenavega çãonoscapítulosfuturos,entãonãose
preocupecomtodososconceitosenvolvidosnestafuncionalidade. Neste
ponto,bastavocêsaberqueháumobjetoencarregadodestetipodefun ção.
Elesechama Framee,nele,háométodo Navigate,noqualtemosde
informarotipodapáginaporparâmetro,conformecódigomostradoanteri-
ormente.
Vocêpodeacessarocódigo-fontedoaplicativoatéaquiatravésdomeu
github:http://bit.ly/8-1GITcap5ParteIII
53
E-book gerado especialmente para 


## Página 60

E-book gerado especialmente para 


## Página 61

Capítulo6
Gerenciamentodedadosemum
aplicativoWindowsPhone
Apesardejátermoscriadodiversaspáginas,nossoaplicativoaindanãopos-
suinenhumaliga çãocomosdados. Comojáfoimencionado,vamoscriar
umabasededadosfictíciasimulandooacessoaumservi ço.Parafazerisso,
vamosresgatarosdadosdeumarquivoJSONque,juntocomXML,sãoas
formasmaiscomunsdeentregasdedadosatravésdeservi ços. Nocasode
aplicativosmóveis,autiliza çãodeJSONémaisrecomendadadevidoaum
consumomenordebanda.
E-book gerado especialmente para 


## Página 62

6.1. Carregandoosdadosparaaaplica ção CasadoCódigo
JSON:J av aScriptObjectNotation
JSONéumpadrãoabertoparatransferênciadedadosmuitocomum.
Éutilizadoprincipalmenteparatransferirdadosdeumservidorpara
umaplicativoweboumóvel. Estepadrãoutilizaumalinguagemsim-
plesatravésdoformatochave:valoreéumaalternativaaopadrãoXML.
6.1 Carregando os dados para a aplicação
Antesdepodermosutilizarosdados,precisamosdeumarepresenta çãodeles
emnossaaplica ção.Parafazerisso,criaremosclassesC #quedefinamnossos
dados.Emalgunspadrõesarquiteturais,essesdadossãochamadosde mod-
elos,eopadrãomaiscomumutilizadoemaplicativosparaWindowsPhone
éoMVVM.
MVVM:M odel-View-ViewModel
MVVMéumpadrãodearquiteturadeaplicativosquepodeseruti-
lizado na plataforma .NET. Ele consiste em três camadas principais:
Model,queéacamadadedados, View,queéacamadadeinterface(po-
dendoserpáginasweb,WindowsouWindowsPhone)e ViewModel,
queéumaabstraçãodeummodeloquepossuiintera çãocomainterface
daaplicação.Éumpadrãosimilaraosmaisconhecidos:MVC(Model-
View-Controller)eMVP(Model-View-Presenter).
Érecomendado,porémnãoobrigatório,separarascamadasdoaplica-
tivoempastas,comojáfizemoscomnossaspáginas. Vamoscriarapasta
Modeloseosmodelos: Produto, Categoriae Loja,conformeocódigo
aseguir.
public class Produto
{
public int Id { get ; set ; }
56
E-book gerado especialmente para 


## Página 63

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
public string Descricao { get ; set ; }
public double Preco { get ; set ; }
public string DescricaoDetalhada { get ; set ; }
public double AvaliacaoMedia { get ; set ; }
public Categoria Categoria { get ; set ; }
public string Icone { get ; set ; }
}
public class Categoria
{
public int Id { get ; set ; }
public int Descricao { get ; set ; }
public int DescricaoDetalhada { get ; set ; }
public List<Produto> Produtos { get ; set ; }
}
public class Loja
{
private Loja ()
{}
private static Loja dados;
public static Loja Dados
{
get
{
if (dados == null )
dados = new Loja();
return dados;
57
E-book gerado especialmente para 


## Página 64

6.1. Carregandoosdadosparaaaplica ção CasadoCódigo
}
set
{
dados = value ;
}
}
public List<Produto> Produtos { get ; set ; }
}
Aclasse Lojadeclaradaaquiutilizaopadrãodeprojeto Singleton,que
éutilizadoparagarantirqueaclassepossuasomenteumainstânciadurante
todaaaplica ção.Casovocêqueirasabermaissobreisso,acesseolink: http:
//bit.ly/padraoSingleton.
Alémdestasclasses,tambémprecisamoscriarumaformadeextrairos
dadosdoarquivoJSONqueseráembutidoemnossoaplicativo. Paraisso,
utilizamosasclasses Streame StreamReaderdo.NET—nãoentrareiem
detalhesparaexplicarestafuncionalidade,poiselaseráfeitadamesmaforma
quequalqueroutraaplica ção.NET.Vejaocódigoaseguir.
public static class LeitorArquivo
{
public async static Task< string > LerAsync()
{
try
{
var arquivo =
await Package.Current.InstalledLocation
.GetFileAsync( @"Resources\dados.txt" );
return await FileIO.ReadTextAsync(arquivo);
}
catch
{
throw ;
}
}
}
58
E-book gerado especialmente para 


## Página 65

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
Aclasse LeitorArquivopossuiadeclara çãode statice async.
Casovocênãoestejafamiliarizadocomestestermos:
Static
Trata-se de uma classe que não pode ser instanciada;
você utiliza seus métodos a partir dela própria, por exemplo:
LeitorArquivo.Ler("caminhoArquivo"). Se quiser obter
maisinformações,sugiroaleituraem: http://bit.ly/staticClass.
Async eAw ait
NoC #,podemosutilizaroscomandos asynce awaitparaexecu-
tartarefasemparalelo.Estaéumacaracterísticabastantesingulardalin-
guagem:aocriarmosummétodoqueretornauma Taskcomoocódigo
anterior,podemosdefini-locomométodoassíncronoatravésdapalavra
reservada async.Apesardenãoserregra,porconven çãoestesmétodo
possuemosufixoAsyncemseunome.Paraentendermelhorofunciona-
mentodeprocessamentoparalelo,acesse: http://bit.ly/msdnAsyncAwait.
Para continuar a desenvolver a aplicação, é necessário que você faça
downloaddoarquivoquecontémnossosdados.Elepodeserbaixadoatravés
dolinkhttp://bit.ly/dataJSONedeveserincluídonapasta Resourcesde
seuaplicativo. Alémdisso,tambéménecessáriofazerodownloaddapasta
quecontémosíconesdosnossosprodutos,quepodemserencontradosno
linkhttp://bit.ly/dataIcones.
Comissofeito,jáconseguiremostrabalharcomosdadosdoarquivo,en-
tãodevemosinserirotrechodecódigoquecarregaosdadosduranteainicial-
izaçãodenossaaplica ção.Issoseriafeitodamesmaformacasoestivéssemos
chamandoumservi çoreal—adiferençaéque,emvezdefazermosumareq-
uisiçãoparaumaURLnainternet,vamosutilizarumleitordearquivolocal.
59
E-book gerado especialmente para 


## Página 66

6.1. Carregandoosdadosparaaaplica ção CasadoCódigo
Agoravamoscriarumnovométodonaclasse MainPage.xaml.cs.
Estemétodoiráutilizaronossoleitordearquivodeformaassíncrona,con-
formeocódigo:
private static async Task< string > LerArquivoDadosAsync()
{
return await LeitorArquivo.LerAsync();
}
Neste ponto faremos uma chamada para o método descrito anteri-
ormente, que deve ser inserida no métodoOnNavigatedTo da classe
MainPage.xaml.cs.
protected override void OnNavigatedTo (NavigationEventArgs e)
{
string dados = LerArquivoDadosAsync().Result;
}
Comessecódigo,jápossuímosumastringcontendotodooJSONdenos-
sosdados,entretantoaindaprecisamosconverterestetextoparaobjetosC #.
Éoquefaremosutilizandoaclasse JsonConvert.Elanãoédisponibilizada
nopacoteinicial,entãoteremosdebuscá-laempacotes NuGet.
NuGet
ONuGetéumgerenciadordepacotesincorporadoaoVisualStudio,
queécapazdebuscarbibliotecasatravésdainternetemumrepositório,
incorporandoasreferênciasmaisatualizadasdabibliotecaaoseuprojeto
noVisualStudio.
Pressioneobotãodireitosobreasreferênciasdeseuprojetoeselecione
aopção Manage NuGet Packages . Apósisso,pesquisepor Json.NET
—atualmenteelaestánalistadebibliotecasmaisbaixadas,demodoqueé
bastantefácilencontrá-la.Feitoisso,podemosfinalmenteconcluirnossaex-
traçãodedadosdoarquivocomoseguintecódigo:
60
E-book gerado especialmente para 


## Página 67

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
protected async override void
OnNavigatedTo (NavigationEventArgs e)
{
string dados = await LerArquivoDadosAsync();
Loja.Dados = JsonConvert.DeserializeObject<Loja>(dados);
}
Antesdeprosseguirmos,vamosvermaisumadicadeusabilidade: em
umcenárioreal,nóspoderíamosestarcarregandoumagrandequantidadede
dadosnestemomento,portanto,podemosadicionarumateladeboas-vindas
paraevitarafrustra çãodousuáriodepermanecernapáginadecarregamento
denossaaplica ção.
Estatelaéchamadade Splash Screen. NoWindowsPhoneexistemtrês
tiposdeSplashScreen.Vocêpodeescolhercriarumaimagemdiferentepara
cadapossívelresoluçãodosistemaoperacional,oucriarapenasumaimagem
edeixarqueosistemaaredimensioneparacadaresolu ção.
Vamosoptarpelasegundaforma,utilizandoapenasumaimagem. Em
nossaaplicaçãojáexisteuma Splash Screenpadrãoqueestásendoexibida,
entãovocêterádealteraraimagemdelaparaaimagemcorreta.
Afigura6.1jáapresentaaSplashScreendenossaaplica çãosendoexibida!
61
E-book gerado especialmente para 


## Página 68

6.2. Vinculandoosdadoscomoscontrolesdeusuário CasadoCódigo
Figura6.1:SplashScreen
Vocêpodeencontrarocódigo-fontedaaplica çãojáaptaacarregaros
dadosecomaSplashScreenprontaemmeugithubatravésdolink: http:
//bit.ly/8-1GITcap6ParteI.
6.2 Vinculando os dados com os controles de
usuário
Nesteponto,jáestamosaptosparautilizarosdadosemnossoaplicativo. A
primeiracoisaafazerévoltarmosànossapágina ProdutosHub.xamleadi-
cionarmosummanipuladorparaoevento Loadeddealgunscomponentes.
62
E-book gerado especialmente para 


## Página 69

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
Esteeventoédisparadoquandoocomponenteterminadeserconstruídoe
nestemomentovamosbuscarasinforma çõesparapreencheraspáginasdo
nossohub.
Vamosao HubSection classificações.Aquiexibiremosumalista
contendoadescri çãodascategoriasdosprodutosdenossaloja.Umcontrole
deusuárioexcelenteparaestetipodenecessidadeéo ListView,quepermiteao
usuáriovisualizarumalistadeinforma ções,ondecadaelementoiráreplicar
umtemplatecriadonapágina.
Parainserirelementosemalgunstiposdecontrolesénecessáriocriarum
DataTemplate,estestemplatesdefinemoselementosqueestãodentrodo
controledetela,ocódigoaseguirmostracomocriarumtemplateparaum
HubSectioneadicionarumalista.
<HubSection Header= "classificações" >
<DataTemplate>
<Grid>
<ScrollViewer>
<Grid Margin= "10,0" >
<ListView x:Name= "Categorias" >
<ListView.ItemTemplate>
<DataTemplate>
</DataTemplate>
</ListView.ItemTemplate>
</ListView>
</Grid>
</ScrollViewer>
</Grid>
</DataTemplate>
</HubSection>
Dentrodatag DataTemplatepodemoscriarumaformadevisualiza-
çãodenossodado.Nesteexemplo,iremosaninhardoiselementosdestetipo
deformabastantesimples,poiscomodesejamosmostrarapenasadescri ção
dascategoriasnalista,vamosadicionarsomenteumcomponentedotipo
TextBlock.
63
E-book gerado especialmente para 


## Página 70

6.2. Vinculandoosdadoscomoscontrolesdeusuário CasadoCódigo
Jásabemosquetemosqueadicionarum TextBlockcomotemplateda
lista,mascomovamospreencherovalordotextodestecomponente?Are-
spostaparaessaperguntaestánoconceitode Bindingimplementadopelo
XAML.Ovalordotextoserávinculadocomapropriedade Descricaodos
dadosqueserãoconectadosaestecomponente.Parafazerisso,utilizeotre-
chodecódigoaseguir:
<HubSection Header= "classificações" >
<DataTemplate>
<Grid>
<ScrollViewer>
<Grid Margin= "10,0" >
<ListView>
<ListView.ItemTemplate>
<DataTemplate>
<TextBlock Text= "{Binding Path=Descricao}"
Style=
"{ThemeResource ListViewItemTextBlockStyle}" />
</DataTemplate>
</ListView.ItemTemplate>
</ListView>
</Grid>
</ScrollViewer>
</Grid>
</DataTemplate>
</HubSection>
Agorasóprecisamosconectarnossosdadosaestecomponentenomanip-
uladormétodo OnNavigatedToquevimosanteriormente.Todososnossos
dadosestãoarmazenadosemmemórianapropriedade Dadosdonossoob-
jeto Loja. Háumaformabastantesimplesdebuscá-losnoC #,conhecida
comoLINQ.
64
E-book gerado especialmente para 


## Página 71

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
LINQ:L inguage-Integrated Query
LINQéumpadrãodeconsultadesenvolvidonaplataforma.NETpara
buscar,unir,armazenareatualizardados.Atravésdelevocêpodemanip-
ulardadostantoemcole çõesdeobjetos,bancodedadoseatéXMLs.Para
sabermaissobreLINQacesse: http://bit.ly/msdnLINQ.
Nestaprimeiraconsulta,iremosselecionaroIdeadescri çãodascatego-
riasdosprodutos,massemrepeti-las,portantolembre-sedeutilizarométodo
Distinct(),conformeoexemplo.
private void ListaCategoria_Loaded ( object sender,
RoutedEventArgs e)
{
ListView lista = sender as ListView;
lista.ItemsSource = ( from produtos in Loja.Dados.Produtos
select new
{
Id = produtos.Categoria.Id,
Descricao =
produtos.Categoria.Descricao
}).Distinct().ToList();
}
Comisso,jápodemosverosdadosemnossaaplica ção!
65
E-book gerado especialmente para 


## Página 72

6.2. Vinculandoosdadoscomoscontrolesdeusuário CasadoCódigo
Figura6.2:Primeirosdadosemnossaaplica ção
Comovocêpodevernocódigoanterior,alistadeobjetosvinculadaàlista
decategoriasédeumobjetoanônimo,ouseja,umobjetoresultantedeuma
consultaquenãopossuiumaclassedefinida. Entretanto,éinteressanteque
vocêutilizeobjetostipados,eéimportantelembrar-sedequeosobjetosde
modelonãodevempossuirnenhumaliga çãocomapágina.Nestemomento,
entraojáapresentado view model.
Vamoscriarumapastachamada ViewModelseadicionarnelaaclasse
ViewModelBase. Estaclasseseráutilizadacomobaseparatodososview
modelsdenossaaplica ção. Paraqueumobjetoviewmodelnotifiqueain-
terfacequandoovalordesuaspropriedadesforalterado,énecessárioquea
classeimplementeainterface INotifyPropertyChanged.Alémdisso,já
66
E-book gerado especialmente para 


## Página 73

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
criaremosummétodoparanotificarapropriedadequefoialterada,conforme
ocódigoaseguir.
public class ViewModelBase : INotifyPropertyChanged
{
protected void NotificarAlteracao ( string propriedade)
{
if (PropertyChanged != null )
PropertyChanged( this ,
new PropertyChangedEventArgs (propriedade));
}
public event PropertyChangedEventHandler PropertyChanged;
}
Nesteprimeiroexemplodeviewmodel,nãoseránecessáriaautiliza ção
dométodo NotificarAlteracao,poisousuárionãovaiconseguiralterar
osdadosdosprodutosoudascategorias,entãoanossaclasseficarábastante
similaraumaclassecomum.Vejaocódigo.
public class CategoriaVM : ViewModelBase
{
public int Id { get ; set ; }
public string Descricao { get ; set ; }
public override bool Equals ( object obj)
{
if (obj is CategoriaVM)
return Id == ((CategoriaVM)obj).Id;
return false ;
}
public override int GetHashCode ()
{
return this .Id;
}
}
67
E-book gerado especialmente para 


## Página 74

6.2. Vinculandoosdadoscomoscontrolesdeusuário CasadoCódigo
Além das propriedades, nós sobrescrevemos os métodosEquals e
GetHashCode,paraalteraraformacomqueoC #comparaobjetosdeste
tipo. Portanto, não teremos repetição ao utilizar o métodoDistinct.
Agora já podemos alterar a consulta LINQ para retornar dados do tipo
CategoriaVM,conformeocódigo:
private void ListaCategoria_Loaded ( object sender,
RoutedEventArgs e)
{
ListView lista = sender as ListView;
lista.ItemsSource = ( from produtos in Loja.Dados.Produtos
select new CategoriaVM
{
Id = produtos.Categoria.Id,
Descricao =
produtos.Categoria.Descricao
}).Distinct().ToList();
}
Agoravamoscriarumtemplatededadosmaiscomplexoparaoitem pro-
moção. Aquivamoslistartodosositensquepossuempre çopromocional,
comseutítulo,suaimagemecomopercentualdedesconto.
Umaboapráticaparadesenvolvertemplatesmaiscomplexosécriá-los
foradalista,comosefossemcomponentesfixos,atévocêficarcontentecom
odesign.Somentedepoisdissoinsira-onotemplateealtereovalordaspro-
priedadesparaasrespectivaspropriedadesvia Binding.
Primeirovamoscriarum Gridedividi-loemduascolunas:naesquerda
ficaráaimagemdoprodutoenadireitaficarãoosdadosquecitamosanteri-
ormente.Nacolunadaimagem,vamosinserirum Gridcomacorbranca,
paradarumfundoaoíconedoproduto.Observeocódigo:
<Grid Height= "150" >
<Grid.ColumnDefinitions>
<ColumnDefinition Width= "130" />
<ColumnDefinition Width= "*" />
</Grid.ColumnDefinitions>
<Grid Background= "White" >
68
E-book gerado especialmente para 


## Página 75

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
<Image Source= "/Icones/camera.png" Height= "75" />
</Grid>
</Grid>
Agoravamosinseriroscomponentesnacolunadadireita.Comoexibire-
mosdiversosdados,vamoscriarum Gridaninhadodamesmaformaque
fizemoscomaimagem,conformeocódigoaseguir.
<Grid Grid.Column= "1" Margin= "10" >
<Grid.RowDefinitions>
<RowDefinition Height= "90" />
<RowDefinition Height= "*" />
</Grid.RowDefinitions>
<TextBlock Text= "Teste produto exemplo exemplo"
FontSize= "24" TextWrapping= "Wrap" Grid.RowSpan= "2" />
<StackPanel Orientation= "Horizontal" Grid.Row= "1" >
<TextBlock Text= "Desconto de: "
VerticalAlignment= "Center" />
<TextBlock Text= "50" FontSize= "24"
VerticalAlignment= "Center" />
<TextBlock Text= "%" FontSize= "24"
VerticalAlignment= "Center" />
</StackPanel>
</Grid>
Percebacomooconceitodegerenciadoresdelayoutaninhadoséutilizado
combastantefrequência.Paracriarmosumasimpleslistagemjáutilizamos
diversosGridseStackPanels. Comoscódigosfinalizados,játemosnosso
templatededados,bastafazero bindingdasinformações.
Oprimeiroiteméo TextBlockcomafontemaior,querepresentaade-
scriçãodoproduto,logo,faremosobindingcomapropriedade Descricao.
Nestepontovocêjádeveternotadoqueprecisamosfazerobindingcomo
69
E-book gerado especialmente para 


## Página 76

6.2. Vinculandoosdadoscomoscontrolesdeusuário CasadoCódigo
percentualdedescontodoprodutoe,naverdade,nãotemosestedadodo
produto.
Noentanto,podemosextrairestainforma çãoapartirdaspropriedades
Precoe PrecoPromocao.Parapodermosfazerobinding,vamoscriarum
viewmodelparaaclasse Produtoquepossuaestapropriedade,sendoque
elaserásomenteleituraedeveretornarovalorcalculadopelospre ços.Veja
ocódigo:
public class ProdutoVM : ViewModelBase
{
public int Id { get ; set ; }
public string Descricao { get ; set ; }
public double Preco { get ; set ; }
public double PrecoPromocao { get ; set ; }
public string DescricaoDetalhada { get ; set ; }
public double AvaliacaoMedia { get ; set ; }
public int CategoriaId { get ; set ; }
public string CategoriaDescricao { get ; set ; }
public string Icone { get ; set ; }
public double Desconto
{
get
{
return Math.Round( 100 - (PrecoPromocao * 100 / Preco), 2 );
}
}
}
Comovocêpodever,nossapropriedadepossuiapenasométodo get,
jáquenãoépossívelinserirumvalornela. Agoravocêpodeutilizaresta
70
E-book gerado especialmente para 


## Página 77

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
propriedadeparafazerobindingnormalmente.
Porfim, teremosquevincularaimagemdoprodutoaocomponente
Image. Aquitemosumproblemadiferentenomomentodefazerobind-
ing. Ocomponenteesperaqueovalorvinculadosejauma Urioualgum
outrotipodefontedeimagens,enquantoqueapropriedadedonossoobjeto
éumtipo string.
Parasolucionaresseproblema,utilizaremosumrecursochamado Value
Converter,quefacilitaovínculodedadosdetiposdiferentes. Vamoscriar
uma pasta chamadaConverter e adicionar nela uma classe chamada
ImageSourceConverter—nãohánenhumaobrigatoriedadequantoà
palavra“Converter”nonomedaclasse, masémuitocomumqueelasse
chamemassim.
Nossaclassedeveimplementarainterface IValueConverter,queestá
nonamespace Windows.UI.Xaml.Data;.Aofazerisso,vocêterádeim-
plementarosdoismétodosdessainterface,conformeocódigo:
public class ImageSourceConverter :IValueConverter
{
public object Convert ( object value , Type targetType,
object parameter, string language)
{
throw new NotImplementedException ();
}
public object ConvertBack ( object value , Type targetType,
object parameter, string language)
{
throw new NotImplementedException ();
}
}
Estes métodos são utilizados para converter o valor para a interface
XAMLeconverternovamenteparaocódigoC #,respectivamente.Emnosso
exemplo,nãoprecisaremosimplementarométodo ConvertBack,maso
método Convertéessencial. Teremosdeutilizarovalordapropriedade
queviráatravésdoparâmetro valueetransformá-loemuma Uripara
encontraroíconedoproduto,conformecodifica çãoaseguir.
71
E-book gerado especialmente para 


## Página 78

6.2. Vinculandoosdadoscomoscontrolesdeusuário CasadoCódigo
public object Convert ( object value , Type targetType,
object parameter, string language)
{
string valor = value as string ;
return new BitmapImage (
new Uri ( string .Concat( @"ms-appx:/Icones/" , valor),
UriKind.Absolute));
}
Éumcódigobastantesimples,porémaltamentenecessárioparaofun-
cionamentodenossobinding.Agoravoltaremosàpáginaqueestávamosim-
plementandoeadicionaremosonamespacedenossoconverter.
xmlns:converter="using:CompreAqui.Converter"
Para finalizar, devemos preencher a propriedadeSource do objeto
Imagefazendoobindingcomapropriedade Icone. Porém,utilizaremos
nossoconversordevalorestambéme,parafazerisso,éprecisodeclará-lo
comorecursodaaplica ção,páginaoucomponente. Nestecaso,optaremos
porfazerdeleumrecursoapenasdocomponente,comoilustraocódigoa
seguir.
<Grid Background= "White" >
<Grid.Resources>
<converter:ImageSourceConverter x:Key= "converter" />
</Grid.Resources>
<Image Source= "{Binding Path=Icone,
Converter={StaticResource converter}}" Height= "75" />
</Grid>
Porfim,criaremosmaisummanipuladorparaoevento Loaded,desta
vezparaanovalista,efaremosaconsultaparaencontrarosprodutosque
estãocomopre çoempromo ção,ordenando-osdomaiordescontoparao
menor:
private void ListaPromocoes_Loaded ( object sender,
RoutedEventArgs e)
{
72
E-book gerado especialmente para 


## Página 79

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
ListView lista = sender as ListView;
lista.ItemsSource = ( from produtos in Loja.Dados.Produtos
where produtos.PrecoPromocao != 0
select new ProdutoVM
{
Id = produtos.Id,
Descricao = produtos.Descricao,
Preco = produtos.Preco,
PrecoPromocao = produtos.PrecoPromocao,
Icone = produtos.Icone
})
.OrderByDescending(
produto => produto.Desconto)
.ToList();
}
Agorajápodemosverosdadosdosprodutosqueestãoempromo ção,
comoilustraafigura 6.3.
73
E-book gerado especialmente para 


## Página 80

6.2. Vinculandoosdadoscomoscontrolesdeusuário CasadoCódigo
Figura6.3:Produtosempromo ção
Como você deve ter notado na imagem, a lista de produtos ultra-
passaaalturadapágina,entãonãoseesque çadeadicionarocomponente
ScrollViewernesteponto,comojáfizemosanteriormente.
Osdoisprimeirositensdonosso Hubjáestãomontados. Agoravamos
preencheroterceiroitemcomumanovalista,porémcomumtemplatesemel-
hanteaotemplatedepromo ções.Mostraremosaimagemeotítulo,masem
vezdeexibiraquantidadededesconto,vamosmostraropre ço.
Apesardonomedesteitemser produtos,nãovamosmostrartodosos
produtosnestatela,masapenaspegardoisprodutossorteadoseadicionar
umlinkparaqueousuáriopossavisualizartodososprodutosemumaoutra
página. Emumcenárioreal,estatécnicaégeralmenteutilizadaparaqueo
74
E-book gerado especialmente para 


## Página 81

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
usuárionãoesperemuitotempoduranteaconsultadedados.
Aprimeiracoisaafazeréadicionaro Gridnesteitemedividi-loemduas
linhas. Jápodemospreencheralinhainferiorcomum TextBlockcomo
texto“todososprodutos”.
<HubSection Header= "produtos" >
<DataTemplate>
<ScrollViewer>
<Grid Margin= "10,0" >
<Grid.RowDefinitions>
<RowDefinition Height= "*" />
<RowDefinition Height= "50" />
</Grid.RowDefinitions>
<TextBlock Text= "todos os produtos"
FontSize=
"{ThemeResource TextStyleExtraLargePlusFontSize}"
Grid.Row= "1" Margin= "0" />
</Grid>
</ScrollViewer>
</DataTemplate>
</HubSection>
Agoravamosutilizaromesmotemplatenalinhasuperior,fazendoalgu-
maspequenasmodifica çõesparaqueeleencaixemelhornestapágina.Altere
aalturado Gridquedefineotemplatedecadaitemdalistade150para130,
ediminuaasmargensverticaisde10para5.Porúltimo,altereoconteúdodo
StackPanelqueexibiaodescontoparaexibiropre çodoproduto.
<Grid Grid.Column= "1" Margin= "10" >
<Grid.RowDefinitions>
<RowDefinition Height= "90" />
<RowDefinition Height= "*" />
</Grid.RowDefinitions>
<TextBlock Text= "{Binding Path=Descricao}" FontSize= "24"
TextWrapping= "Wrap" Grid.RowSpan= "2" />
75
E-book gerado especialmente para 


## Página 82

6.2. Vinculandoosdadoscomoscontrolesdeusuário CasadoCódigo
<StackPanel Orientation= "Horizontal" Grid.Row= "1" >
<TextBlock Text= "por: " VerticalAlignment= "Center" />
<TextBlock Text= "{Binding Path=PrecoAPagar}" FontSize= "24"
VerticalAlignment= "Center" />
<TextBlock Text= " R$" FontSize= "24"
VerticalAlignment= "Center" />
</StackPanel>
</Grid>
Nestetrecho,apartequenãotevealtera çõesemrela çãoaotemplateuti-
lizadonoitem“promoção”foisuprimidaparafacilitaraleituradocódigoe
paradarmaisênfaseaoquefoialterado.Vocêpodeternotadoqueumdos
textosestávinculadoàpropriedade PrecoAPagareelaaindanãoexisteem
nossaclasse ProdutoVM.
Vamoscriá-lapararetornaropre çoqueocompradorirápagarnopro-
duto. A regra é bastante simples: esta propriedade vai retornar o valor
dapropriedade Precodoprodutoquando PrecoPromocaoestivercom
ovalorzero; casocontrário,ovalorretornadodeveserodapropriedade
PrecoPromocao.
public double PrecoAPagar
{
get
{
double valor;
if (PrecoPromocao != 0 )
valor = PrecoPromocao;
else
valor = Preco;
return Math.Round(valor, 2 );
}
Agoravamoscriarmaisummanipuladordoevento Loadedeadicionara
fontededadosparaestalista.Estejaàvontadeparadesenvolverumalgoritmo
76
E-book gerado especialmente para 


## Página 83

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
quebusqueprodutosaleatórios,masparafinsdedemonstra çãovamosapenas
selecionarosprodutoscomosidentificadores3e4. Dessaforma,sempre
serãoselecionadososmesmosprodutos,jáquenossabasededadoséestática.
private void ListaProdutos_Tapped ( object sender,
TappedRoutedEventArgs e)
{
ListView lista = sender as ListView;
lista.ItemsSource = ( from produtos in Loja.Dados.Produtos
where produtos.Id == 3 ||
produtos.Id == 4
select new ProdutoVM
{
Id = produtos.Id,
Descricao = produtos.Descricao,
Icone = produtos.Icone,
Preco = produtos.Preco,
PrecoPromocao = produtos.PrecoPromocao
})
.ToList();
}
Afigura6.4ilustraoresultadodenossaimplementa ção.
77
E-book gerado especialmente para 


## Página 84

6.2. Vinculandoosdadoscomoscontrolesdeusuário CasadoCódigo
Figura6.4:Listagemdeprodutos
Ésempreumaboapráticacircundaraslistascomgerenciadoresdelay-
outdotipo ScrollViewer,poisaslistampodemaumentardetamanhoao
decorrerdousodaaplica ção.
Casovocêqueiraacessarocódigo-fontedoprojetoatéesteponto,você
podeencontrá-lonogithubatravésdolink: http://bit.ly/8-1GITcap6ParteII
Jámostramoscomoutilizardadosparaexibirinforma ções.Agoravamos
verificarcomoumaplicativoWindowsPhonepodearmazenarinforma ções
localmente.Emumcenárioreal,todaapartedecria çãodecontasdeusuários
deveriaserarmazenadaemumbancodedadosnanuvem. Parafinsdeex-
emplo,utilizaremosarmazenamentodedadoslocaldoWindowsPhonepara
guardarestetipodeinforma ção.
78
E-book gerado especialmente para 


## Página 85

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
CadaaplicativoemumdispositivoWindowsPhonepossuialgunsre-
cursosparaarmazenamentodedados, entreeles: localutilizadoparaar-
mazenarconfigurações Local/Roaming Settings,acessoaarquivos,cartãoSD
eo Credential Locker. Casosejadeseuinteresse,vocêtambémpode
utilizarobancodedados SQLite,umbancodedadosqueéamplamente
utilizadoemoutrasplataformas,comoAndroideIOs.
Estebancodedadoséindividualporaplicativo,oqueimpossibilitao
compartilhamentodedadosarmazenadosnestebancodedadosentredifer-
entesaplicativos.
6.3 Armazenando dados em arquivos JSON no
Windows Phone
OWindowsPhonepossuiumaAPIcompletaparamanipula çãodearquivos.
EstaAPIfacilitaogerenciamentodearquivosemtrêsprincipaisdiretórios:
local,roamingetemp,sãorespectivamentearmazenamentonodispositivo,
armazenamento na nuvem e armazenamento em uma pasta temporário.
EstescaminhossãoacessíveisviaAPIC #ouatravésdeURIscomo(“ms-
appdata:///local/”)porexemplo.
Agoravamosvoltarparanossoaplicativoecriarasclasses Usuario,na
pasta Modelos,e BancoDados(utilizandoojávistopadrão Singleton,na
pasta Resources,conformeocódigo:
public class Usuario
{
public int Id { get ; set ; }
public string Email { get ; set ; }
public string NomeUsuario { get ; set ; }
public string Senha { get ; set ; }
public bool EntrarAutomaticamente { get ; set ; }
}
public class BancoDados
{
private BancoDados ()
79
E-book gerado especialmente para 


## Página 86

6.3. ArmazenandodadosemarquivosJSONnoWindowsPhone CasadoCódigo
{}
private static BancoDados instancia;
public static BancoDados Instancia
{
get
{
if (instancia == null )
instancia = new BancoDados();
return instancia;
}
set
{
instancia = value ;
}
}
public List<Usuario> Usuarios { get ; private set ; }
}
AclasseBancoDadosseráresponsávelpormanteralistadeusuárioen-
quantoaaplica çãoestivernoaretambémseráaclassequeforneceráos
métodosdeleituraeescritadosdadosparaJSON.Porserumaaplica ção
fechada,nãoiremosnospreocuparcomseguran çaearmazenaremostodos
osdadosemarquivosJSON.Nocasodeumaaplica çãorealutilizeorecurso
Credential Locker.
Este recurso é basicamente um pequeno espaço de memória
que é utilizado para armazenar nomes de usuário e senhas de uma
forma segura. A API é bastante simples funcionando como a maior
parte dos dicionários de dados, esta API se encontra no namespace
Windows.Security.Credentials.
Antesdecolocarmosnossobancodedadosempráticaprecisamoscriaros
métodoparaarmazenamentoebuscadestesdados,faremosissonaclasseque
criamosanteriormente.Primeirovamosfazerométodoparaarmazenamento
deinformações,elesechamará GravarDados,conformeocódigoaseguir.
public async Task GravarDados ()
80
E-book gerado especialmente para 


## Página 87

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
{
StorageFolder pasta = ApplicationData.Current.LocalFolder;
StorageFile arquivo =
await pasta.CreateFileAsync(DATA_FILE,
CreationCollisionOption.OpenIfExists);
await FileIO.WriteTextAsync(arquivo,
JsonConvert.SerializeObject(Usuarios),
Windows.Storage.Streams.UnicodeEncoding.Utf8);
}
Noteque,nocódigoexibido,onomedoarquivoseencontraemuma
constantechamada“DATA_FILE”,énecessárioquevocêincluaestaconstante
naclasse. Elaseráutilizadaparagarantirqueexistirásomenteumarquivo
paracontrolarosdados. Vocêpodeescolheronomequequiserparaseus
dados,masestaéadeclara çãoutilizadanolivro private const string
DATA_FILE = "data.JSON"; .
Agoravamoscriarummétodoparaabuscadenossosdados,queserá
executadaduranteainicializa çãodaaplica ção. Faremosissoparaacessaro
arquivosomenteumavezcasonãohajaaltera çõesetambémiremosgarantir
quesemprehajapelomenosumusuárionabasededados,oqualnomeare-
mosdeadmin.
public async Task BuscarDados ()
{
StorageFolder pasta = ApplicationData.Current.LocalFolder;
StorageFile arquivo =
await pasta.CreateFileAsync
(DATA_FILE, CreationCollisionOption.OpenIfExists);
string resultado = await FileIO.ReadTextAsync(arquivo);
if ( string .IsNullOrEmpty(resultado))
{
Usuario admin = new Usuario();
admin.NomeUsuario = "admin" ;
admin.Senha = "admin" ;
admin.Email = "admin@compreaqui.com.br" ;
81
E-book gerado especialmente para 


## Página 88

6.3. ArmazenandodadosemarquivosJSONnoWindowsPhone CasadoCódigo
admin.Id = 1 ;
Usuarios.Add(admin);
await GravarDados ();
await BuscarDados ();
}
else
Usuarios = JsonConvert
.DeserializeObject<List<Usuario>>(resultado);
}
Vamosdestrincharessecódigo. Primeiro,acessamosamemórialocale
delacriamosouabrimosoarquivodosdados.Apósisso,aleituradosdadosé
feitae,casooarquivoJSONestejavazio,énecessáriocriarousuáriofixoque
nomeamoscomo“admin”,depoisdecriarlemososdadosnovamente,para
quedessavezalistadeusuáriossejacarregada.
Tambéménecessárioinicializaralistadeusuáriosquandoainstânciado
bancodedadosécriada,conformecódigo.
public static BancoDados Instancia
{
get
{
return CriarOuObterInstancia ();
}
set
{
instancia = value ;
}
}
public static BancoDados CriarOuObterInstancia ()
{
if (instancia == null )
{
instancia = new BancoDados();
instancia.Usuarios = new List<Usuario>();
}
82
E-book gerado especialmente para 


## Página 89

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
return instancia;
}
Por fim devemos incluir uma chamada para o método
CriarOuObterInstancia na classe App.xaml.cs, no mesmo local
ondecriamosomanipuladordoevento BackPressed.
Agoracomnossogerenciadorpronto, vamosvoltarparaapáginade
criaçãodecontasefazeraliga çãodosdados. Assimfaremoscomqueo
nossoobjetorecebaosvaloresdapágina,seguindoojámencionadopadrão
MVVM.Vamoscriarmaisumaclassenapasta ViewModelsquesechamará
UsuarioVM.
Lembre-se de que o view model deve conter apenas as propriedades
que são acessíveis pela interface, então esta classe possuirá uma pro-
priedadeparaocampo“confirmaçãodesenha”. Ocódigoaseguirmostra
a estrutura que as propriedades devem seguir, exceto pela propriedade
EntrarAutomaticamente,poiselapossuiovalor truecomopadrão.
public class UsuarioVM : ViewModelBase
{
private string _email;
public string Email
{
get { return _email; }
set
{
_email = value ;
NotificarAlteracao( "Email" );
}
}
//Outras propriedades
//...
private bool _entrarAutomaticamente = true ;
public bool EntrarAutomaticamente
{
get { return _entrarAutomaticamente; }
set
83
E-book gerado especialmente para 


## Página 90

6.3. ArmazenandodadosemarquivosJSONnoWindowsPhone CasadoCódigo
{
_entrarAutomaticamente = value ;
NotificarAlteracao( "EntrarAutomaticamente" );
}
}
}
Comaclasse UsuarioVMcriada,jáestamosaptosavincularosdados
napáginadecria çãodecontas. Comojávimoscomofazerobindingdas
propriedades,nãoprecisamosentraremdetalhesnesteponto.
Depoisdeligaroscontrolesdeusuáriocomasdevidaspropriedadesda
classe,vocêprecisacriarummanipuladorparaoevento Tappeddobotão
“Criarconta”eintroduzirumtrechodecódigoparaserexecutadoquandoa
páginaforcarregada.NocódigoC #denossapágina,vamoscriarumatributo
dotipo UsuarioVM,queseráatribuídonapropriedade DataContextda
páginaduranteoevento Loaded.
protected override void OnNavigatedTo (NavigationEventArgs e)
{
if (_usuarioVM == null )
_usuarioVM = new UsuarioVM();
this .DataContext = _usuarioVM;
}
Após fazer isso, vamos criar um método chamado
ValidarCamposCadastro na classe UsuarioVM. Ele deve ser do
tipo stringedeverávalidaropreenchimentodetodasaspropriedades,
bemcomoaigualdadeentreoscampos Senhae ConfirmacaoSenha.
Vamosconcatenarumamensagemcomosproblemasqueencontrarmose
retornaramensagemcompletanométodo.
public string ValidarCamposCadastro ()
{
StringBuilder validacoes = new StringBuilder();
if ( string .IsNullOrEmpty(Email))
84
E-book gerado especialmente para 


## Página 91

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
validacoes.AppendLine(
"- É necessário preencher o campo Email" );
if ( string .IsNullOrEmpty(Nome))
validacoes.AppendLine(
"- É necessário preencher o campo Usuário" );
if ( string .IsNullOrEmpty(Senha) ||
string .IsNullOrEmpty(ConfirmacaoSenha))
validacoes.AppendLine(
"- É necessário preencher os campos Senha e
Confirmação de Senha ");
else
if (Senha != ConfirmacaoSenha)
validacoes.AppendLine(
"- Os campos Senha e Confirmação de senha estão com
valores diferentes ");
return validacoes.ToString();
}
Acria çãodométodo ValidarCamposCadastronaclassedeview
modelpodeserquestionável—algunsdesenvolvedorespreferemcriarum
métododentrodaclassemodelo—mas,pessoalmente,prefiroqueaclasse
modelotenharesponsabilidadepelasregrasdenegócioepelasinforma ções,
enquantooviewmodelfaztodoointermédiodapáginacomomodelo,in-
clusiveemsuavalida ção.
Agora voltaremos para o código da página de criação de contas e
preencheremosométodo Button_Tapped.Aprimeirapartedestemétodo
consiste em utilizar a validação que criamos e exibir uma mensagem ao
usuárioquandohouveralgumproblema.
private async void Button_Tapped ( object sender,
TappedRoutedEventArgs e)
{
string validacoes = _usuarioVM.ValidarCamposCadastro();
if (! string .IsNullOrEmpty(validacoes))
85
E-book gerado especialmente para 


## Página 92

6.3. ArmazenandodadosemarquivosJSONnoWindowsPhone CasadoCódigo
{
string mensagem = string .Concat(
"Não foi possível gravar esta conta por um ou mais motivos
abaixo: ",
Environment.NewLine, validacoes);
MessageDialog messageDialog = new MessageDialog(mensagem);
await messageDialog.ShowAsync();
}
else
{
}
}
Vamostestarnossaaplica çãoparaverificarcomoelasecomporta.
Sevocêtentouexecutarostestesdevalida ção,vaiperceberquemesmo
preenchendooscamposamensagemaindaépreenchida, comoilustraa
figura6.5.
86
E-book gerado especialmente para 


## Página 93

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
Figura6.5:Problemacomvalida ção
Issoaconteceporqueomodopadrãodobindingapenasvinculaosdados
nomomentoemqueocontextodedadoséatribuído.Paraqueoobjetoreceba
atualizaçõesconformeovalordoscampos,precisamosdemaisumdetalhe
emnossainterface. Apósselecionarmosapropriedade Pathdobinding,
tambémvamosatribuirapropriedade Modecomovalor TwoWay,conforme
oexemplo:
<TextBox InputScope= "EmailUserName"
Text= "{Binding Path=Email,Mode=TwoWay}" />
Sefizermosumtesteparecido,masdeixandoapenasocampo“Usuário”
embranco,teremosoresultadocorreto.
87
E-book gerado especialmente para 


## Página 94

6.3. ArmazenandodadosemarquivosJSONnoWindowsPhone CasadoCódigo
Figura6.6:Valida çãocorreta
Agoravamosadicionarométodo AdicionarUsuarioemnossaclasse
BancoDados. Eledevereceberoviewmodelporparâmetroetransformar
suasinformaçõesemumdadoparaserarmazenado,conformeocódigo:
public async void AdicionarUsuario (UsuarioVM usuarioVM)
{
Usuario novoUsuario = new Usuario();
novoUsuario.Email = usuarioVM.Email;
novoUsuario.NomeUsuario = usuarioVM.Nome;
novoUsuario.Senha = usuarioVM.Senha;
novoUsuario.EntrarAutomaticamente =
88
E-book gerado especialmente para 


## Página 95

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
usuarioVM.EntrarAutomaticamente;
novoUsuario.Id = Usuarios.Count + 1 ;
Usuarios.Add(novoUsuario);
await GravarDados ();
}
Agoravamoscompletarométodoparaarmazenarousuáriocriadona
páginaCriarContaedirecioná-loparaapágina ProdutosHub.xaml.
private async void Button_Tapped ( object sender,
TappedRoutedEventArgs e)
{
string validacoes = _usuarioVM.ValidarCamposCadastro();
if (! string .IsNullOrEmpty(validacoes))
{
string mensagem = string .Concat(
"Não foi possível gravar esta conta por um ou mais motivos
abaixo: ",
Environment.NewLine, validacoes);
await ExibirMensagem (mensagem);
}
else
{
try
{
BancoDados.Instancia.AdicionarUsuario(_usuarioVM);
this .Frame.Navigate( typeof (ProdutosHub));
}
catch
{
string mensagem =
"Houve um problema ao tentar criar sua conta,
tente novamente mais tarde. ";
ExibirMensagem(mensagem);
}
}
89
E-book gerado especialmente para 


## Página 96

6.4. Armazenandoconfiguraçõeseosimpactosemnossoaplicativo CasadoCódigo
}
private async Task ExibirMensagem ( string mensagem)
{
MessageDialog messageDialog =
new MessageDialog (mensagem);
await messageDialog.ShowAsync();
}
Utilizamosasinstru ções tryecatchparaexibirumamensagemmais
amigávelaousuáriocasoaconteçaalgumproblema,masvocêdeveternotado
queestamosapenaspassandoasinforma çõesdoviewmodelparaomodelo.
Emumaaplica çãoreal,asenha jamaisdeveserarmazenadadestaforma—é
extremamenteimportantequevocêutilizeumacriptografianomomentode
armazená-laouutilizeo Credential Locker.
Outracoisaqueaindaestáemabertoéousuárioautenticado. Apesar
defazermosaautentica çãonomomentodacria çãodaconta,nãoestamosar-
mazenandoestainformaçãoemnenhumlugar,oquenosimpededeconhecer
qualousuárioqueestáautenticadoemnossaaplica ção.
Utilizaremosumoutroconceitoparaarmazenarestainforma ção:trata-se
doarmazenamentolocaldeconfigura ções.
6.4 A rmazenando configurações e os impactos
em nosso aplicativo
Neste ponto será abordado um conceito que é utilizado para armazenar
informações simples em um modelo chave-valor. Nós o utilizaremos
para armazenar qual usuário está autenticado no momento. Essas con-
figurações são acessíveis através da propriedadeSettings da classe
IsolatedStorageSettings.
Vamossimplesmentearmazenarapropriedade Iddousuárioautenti-
cado.Omecanismoétãosimplesquepodemosfazerissoutilizandoapenas
umalinhadecódigo,entretanto,ésemprenecessárioverificarseachavejá
existe,poisousuáriopodecadastrarmaisdeumacontanomesmodisposi-
tivo.
90
E-book gerado especialmente para 


## Página 97

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
Este método será criado dentro da classeUsuario e se chamará
Autenticar,conformeocódigo:
public void Autenticar ()
{
Windows.Storage.ApplicationDataContainer configuracoes =
Windows.Storage.ApplicationData.Current.LocalSettings;
if (configuracoes.Values.ContainsKey( "usuarioId" ))
{
configuracoes.Values[ "usuarioId" ] = this .Id;
}
else
{
configuracoes.Values.Add( "usuarioId" , this .Id);
}
}
Teremosdefazerumachamadaparaestemétodologoapósarmazenar
ousuárionobancodedados,paragarantirqueteremosoidentificadordo
usuáriocriadoeautenticado.
Comisso,jáconseguiremosdetectarseháumusuárioautenticadono
aplicativoeagoraprecisamoscercarospontosondeissoéimportante. O
primeiropassoéumanovaregraemnossaaplica ção:casoousuárioesteja
autenticadonoaplicativoepressioneobotão voltardodispositivo,temos
defecharoaplicativo,poisassumiremosqueeleestásaindo.
Atualmente,secriarmosumusuário,conectarmosnaaplica çãoepres-
sionarmosobotão voltardodispositivo,seremosredirecionadoparaa
páginadecriaçãodeusuário.Paraalterarocomportamentopadrãodobotão
voltartemosdemodificarapilhadenavega çãodenossaaplica ção.Faremos
issologoapósainstru çãoparanavegarmosparaapáginadeprodutos.
private async void Button_Tapped ( object sender,
TappedRoutedEventArgs e)
{
// Código inalterado
try
{
91
E-book gerado especialmente para 


## Página 98

6.4. Armazenandoconfiguraçõeseosimpactosemnossoaplicativo CasadoCódigo
BancoDados.Instancia.AdicionarUsuario(_usuarioVM);
this .Frame.Navigate( typeof (ProdutosHub));
this .Frame.BackStack.Clear();
}
// Código inalterado
}
Dessaformaevitamosoproblemadeousuárioretornaratéapáginade
criaçãodecontasoumesmoatéapáginainicial. Eleterádesairdaconta
atualparapodervisualizarestaspáginasnovamente,eestaop çãoserácri-
adanapágina“suaconta”.Masantesdisso,vamosfazercomqueamarcação
“Lembrar-me”funcione.
Paraisso,teremosquevoltaraténossapáginainicialeinserirumtre-
chodecódigonométodo OnNavigatedTo,queédisparadosemprequeo
usuárioéenviadoparaapágina,sejaqualforomotivo,inclusiveporeleabrir
aaplicação.Vamosinterceptarestemétodoefazercomqueousuáriovápara
apágina ProdutosHubquandoaregrasecumprir.
protected async override void
OnNavigatedTo (NavigationEventArgs e)
{
string dados = await LerArquivoDadosAsync();
Loja.Dados = JsonConvert.DeserializeObject<Loja>(dados);
await BancoDados.Instancia.BuscarDados();
Windows.Storage.ApplicationDataContainer configuracoes =
Windows.Storage.ApplicationData.Current.LocalSettings;
if (configuracoes.Values.ContainsKey( "usuarioId" ) &&
Convert.ToInt32(configuracoes.Values[ "usuarioId" ]) != 0 )
{
Usuario ultimoUsuario =
BancoDados.Instancia
.Usuarios
.FirstOrDefault
(usuario =>
92
E-book gerado especialmente para 


## Página 99

CasadoCódigo Capítulo6. GerenciamentodedadosemumaplicativoWindowsPhone
usuario.Id ==
Convert.ToInt32(
configuracoes.Values[ "usuarioId" ]));
if (ultimoUsuario.EntrarAutomaticamente)
{
this .Frame.Navigate( typeof (ProdutosHub));
this .Frame.BackStack.Clear();
}
else
configuracoes.Values[ "usuarioId" ] = 0 ;
}
}
Com esta implementação, caso o usuário tenha deixado a opção
“Lembrar-me”marcada,semprequeeleentrarnoaplicativojáseráredire-
cionadodiretamenteparaohubdeprodutos.
AgoravocêjáestáaptoamodificarapáginaEntrar.xamlparavalidaro
usuárioesenhaetambémarmazenaraautentica ção.Alémdisso,vocêdeverá
criarumnovoitemde Pivotnapágina SuaConta.xamlcomotítulode
“Informações”.
Esteitemdeveseroprimeirodapáginaedeverámostrarosdadosdo
usuárioautenticadonomomento,bemcomoaop çãoparasair,quedevecan-
celaraautentica çãodousuárionaaplica ção.Paraestasegundaop ção,você
deveutilizara CommandBar.Éimportantequevocêfa çaissoantesdeseguir
nolivro,poisnopróximocapítuloestasaltera çõesjáestarãoimplementadas.
Caso queira acessar o código-fonte do projeto até o fim deste capí-
tulo, você pode encontrá-lo no github através do link: http://bit.ly/
8-1GITcap6ParteIII.
93
E-book gerado especialmente para 


## Página 100

E-book gerado especialmente para 


## Página 101

Capítulo7
Navegaçãoeciclodevida
Atéestecapítulo,nossaaplica çãojáestáboaparteimplementada,masainda
temosquecriarapáginaparavisualizartodososprodutoseparaorganizá-
losporcategorias.Entretanto,estasduaspáginaspodemserapenasuma.Isso
podeserfeitoatravésdepassagemdeparâmetrosentreaspáginas.
7.1 Navegação entre páginas
Nósjáutilizamososprincípiosbásicosdenavega çãonoscapítulosanteriores.
Agoravamoscompreendermelhorcomoissofunciona.
CadaaplicaçãoWindowsPhonepossuiumainstânciadeum Frame.Este
componentetornapossívelanavegabilidadeentreaspáginasatravésdeuma
pilhadenavegação,quefazcomqueobotão voltardodispositivodirecione
ousuárioparaapáginacorretaaoutilizarométodo GoBack.
E-book gerado especialmente para 


## Página 102

7.1. Navegaçãoentrepáginas CasadoCódigo
Existembasicamentedoistiposdenavega ção: forwardebackward. A
navegaçãoforwardéutilizadasemprequedirecionamosousuárioparauma
páginaatravésdo Frameouquandoousuárioabrenossoaplicativo. Jáa
navegaçãobackwardéativadaquandoutilizamosométodo GoBack,como
porexemploquandoousuáriopressionaobotãovoltardeseudispositivo.
Vamoscriarumapáginachamada Produtos.xaml. Apliqueaelao
mesmoplanodefundodaspáginas Pivote Hubedeixeapenascomotítulo
otexto“produtos”,comoilustraafigura7.1.
Figura7.1:Novapágina
Paraacessarestapáginaousuáriodevepressionarotexto“todosospro-
dutos”daHubSection“Produtos”,entãotambémimplementeanavegação
96
E-book gerado especialmente para 


## Página 103

CasadoCódigo Capítulo7. Navegaçãoeciclodevida
paraestapágina,conformeocódigo:
private void TodosProdutos_Tapped ( object sender,
TappedRoutedEventArgs e)
{
this .Frame.Navigate( typeof (Produtos));
}
Paralistarosprodutos,criaremosumtemplatesemelhanteaoutilizado
no HubSection“produtos”,masvamosfazerpequenasalteraçõesnaformade
exibirasinforma ções,mostrandoalémdonomeedopre çoaavalia çãomédia
doproduto.Vejaocódigo.
<DataTemplate>
<Grid Height= "150" VerticalAlignment= "Top" Margin= "0,5" >
<Grid.ColumnDefinitions>
<ColumnDefinition Width= "110" />
<ColumnDefinition Width= "*" />
</Grid.ColumnDefinitions>
<Grid Background= "White" >
<Grid.Resources>
<converter:ImageSourceConverter x:Key= "converter" />
</Grid.Resources>
<Image Source= "{Binding Path=Icone,
Converter={StaticResource converter}}" Height= "75" />
</Grid>
<StackPanel Grid.Column= "1" Margin= "10" >
<TextBlock Text= "{Binding Path=Descricao}"
FontSize= "{ThemeResource TextStyleExtraLargeFontSize}"
TextWrapping= "Wrap" />
<StackPanel Orientation= "Horizontal" >
<TextBlock Text= "por: " VerticalAlignment= "Center" />
97
E-book gerado especialmente para 


## Página 104

7.1. Navegaçãoentrepáginas CasadoCódigo
<TextBlock Text= "{Binding Path=PrecoAPagar}"
FontSize= "24" VerticalAlignment= "Center" />
<TextBlock Text= " R$" FontSize= "24"
VerticalAlignment= "Center" />
<TextBlock Text= "Avaliação média: "
VerticalAlignment= "Center" Margin= "10,0,0,0" />
<TextBlock Text= "{Binding Path=AvaliacaoMedia}"
FontSize= "24" VerticalAlignment= "Center" />
</StackPanel>
</StackPanel>
</Grid>
</DataTemplate>
Agoraquejátemosodesigndestapáginacriadovamosvincularosdados
paraexibiralistagem.Faremosissocriandoummanipuladorparaoevento
Loadeddalista,comojáfizemosemoutraspáginas.
private void ListaProdutos_Loaded
( object sender, RoutedEventArgs e)
{
ListView lista = sender as ListView;
List<ProdutoVM> produtos =
( from produto in Loja.Dados.Produtos
select new ProdutoVM
{
Id = produto.Id,
Descricao = produto.Descricao,
Preco = produto.Preco,
PrecoPromocao = produto.PrecoPromocao,
AvaliacaoMedia = produto.AvaliacaoMedia,
CategoriaId = produto.Categoria.Id,
CategoriaDescricao = produto.Categoria.Descricao,
98
E-book gerado especialmente para 


## Página 105

CasadoCódigo Capítulo7. Navegaçãoeciclodevida
Icone = produto.Icone
}).ToList();
lista.ItemsSource = produtos;
}
Comestaimplementa ção,jápodemosveralistagemdetodososprodu-
tos,comoilustraafigura 7.2
Figura7.2:Listagemdosprodutos
Agoraprecisamoscriarumaformaparareutilizarestapáginacomfiltros
porcategoria.Éahoradeutilizarpassagemdeparâmetroentreaspáginas.
Primeiro, vamos voltar até o item Categorias na página
ProdutosHub.xaml.Vamosadicionaraotemplatequelistaadescri çãodas
categoriasummanipuladorparaoevento Tapped,conformeocódigo.
<ListView Loaded= "ListaCategoria_Loaded" >
<ListView.ItemTemplate>
<DataTemplate>
<TextBlock Text= "{Binding Path=Descricao}"
Style= "{ThemeResource ListViewItemTextBlockStyle}"
Tapped= "Categoria_Tapped" />
</DataTemplate>
</ListView.ItemTemplate>
</ListView>
DentrodestemétodoC #,teremosqueobtertodasasinforma çõesque
vamospassarporparâmetro.Issoéfeitoatravésdoparâmetro sender,que
99
E-book gerado especialmente para 


## Página 106

7.1. Navegaçãoentrepáginas CasadoCódigo
éenviadonométododisparadopeloevento Tapped. Vamosconvertero
objeto senderparaseutipooriginal( TextBlock)paraentãoextrairmos
asinformações.
Parafazerafiltragemealtera çãodotítulonapágina,precisaremosdo
Iddacategoria.Entretanto,nossocomponente TextBlocknãopossuiesta
informação.Existemdiversasmaneirasdiferentesdefazerisso,vamossele-
cionarumabastantesimples.
Damesmaformaquearmazenamosadescri çãodacategorianapro-
priedade Text,vamosarmazenarseuidentificadornapropriedade Tag
atravésdobinding.
<TextBlock Text= "{Binding Path=Descricao}"
Style= "{ThemeResource ListViewItemTextBlockStyle}"
Tag= "{Binding Path=Id}" Tapped= "Categoria_Tapped" />
Comisso,jápodemosextrairasinforma çõesdocomponenteeenviá-las.
Paraenviarmosousuárioparaumapágina,utilizamosométodo Navigate,
comojávimosanteriormente.Elepossuiumasobrecargaondeépossívelen-
viarparâmetrospararecuperá-losemoutrapágina,conformecódigoaseguir.
private void Categoria_Tapped ( object sender,
TappedRoutedEventArgs e)
{
TextBlock categoriaClicada = sender as TextBlock;
int categoriaId = Convert.ToInt32(categoriaClicada.Tag);
this .Frame.Navigate( typeof (Produtos), categoriaId);
}
Precisamos voltar mais uma vez para o código da página
Produtos.xaml para capturarmos os parâmetros enviados a ela. Os
parâmetros são armazenados na propriedade Parameter do objeto
NavigationEventArgs. Este objeto pode ser recuperado no método
OnNavigatedTodapágina,entãocriaremosumatributoprivadoparaesta
classeeiremospreencherseuvalorcomoparâmetrorecebido,conformeo
código:
protected override void OnNavigatedTo (NavigationEventArgs e)
{
100
E-book gerado especialmente para 


## Página 107

CasadoCódigo Capítulo7. Navegaçãoeciclodevida
_categoriaId = Convert.ToInt32(e.Parameter);
}
Agoraquejávimosaformadeobtermosovalor,vamosalteraromanipu-
ladordoevento Loadeddenossalistaparapegarmosoparâmetroeutilizá-lo
paramodificarositensqueserãoexibidosnapágina.
private void ListaProdutos_Loaded
( object sender, RoutedEventArgs e)
{
ListView lista = sender as ListView;
List<ProdutoVM> produtos =
( from produto in Loja.Dados.Produtos
select new ProdutoVM
{
Id = produto.Id,
Descricao = produto.Descricao,
Preco = produto.Preco,
PrecoPromocao = produto.PrecoPromocao,
AvaliacaoMedia = produto.AvaliacaoMedia,
CategoriaId = produto.Categoria.Id,
CategoriaDescricao = produto.Categoria.Descricao,
Icone = produto.Icone
}).ToList();
if (_categoriaId != 0 )
{
produtos =
produtos.Where(produto =>
produto.CategoriaId ==
Convert.ToInt32(_categoriaId)).ToList();
Titulo.Text = produtos.FirstOrDefault().CategoriaDescricao;
}
lista.ItemsSource = produtos;
}
Nossapáginajáestáprontaparaseajustarconformeosparâmetrosuti-
101
E-book gerado especialmente para 


## Página 108

7.1. Navegaçãoentrepáginas CasadoCódigo
lizados!Afigura 7.3ilustraasdiferentesformasdestapágina.
Figura7.3:Páginarecebendoparâmetros
Porfimiremosacrescentarumaanima çãodecontinuidadeemnossa
páginaparamelhoraraexperiênciadousuário. Dessaforma, quandoo
usuáriopressionarumitemdalistadecategoriasocamposairádapágina
evoltaráquandoapróximapáginaabrir,dandoasensa çãodecontinuidade
noaplicativo.
Napágina Produtos.xamlvocêterádeincluirumcódigoparatran-
siçãodepágina,apósadeclara çãodocomponente Page.
<Page.Transitions>
<TransitionCollection>
<NavigationThemeTransition>
<NavigationThemeTransition
.DefaultNavigationTransitionInfo >
<ContinuumNavigationTransitionInfo/>
</NavigationThemeTransition
.DefaultNavigationTransitionInfo>
</NavigationThemeTransition>
</TransitionCollection>
</Page.Transitions>
102
E-book gerado especialmente para 


## Página 109

CasadoCódigo Capítulo7. Navegaçãoeciclodevida
Agoraénecessárioidentificaroscontrolesdetelaquefazemestatran-
siçãocontínua. Napágina Produtos.xamlbastaincluirapropriedade
ContinuumNavigationTransitionInfo.IsEntranceElement com
o valor true no componente de título da página. Na página
ProdutosHub.xamlénecessárioidentificaralistaeoitemdalista,con-
formeotrechodecódigo:
<ListView Loaded= "ListaCategoria_Loaded"
ContinuumNavigationTransitionInfo.ExitElementContainer= "True" >
<ListView.ItemTemplate>
<DataTemplate>
<TextBlock Text= "{Binding Path=Descricao}"
Style= "{ThemeResource ListViewItemTextBlockStyle}"
Tag= "{Binding Path=Id}" Tapped= "Categoria_Tapped"
ContinuumNavigationTransitionInfo.IsExitElement= "True" />
</DataTemplate>
</ListView.ItemTemplate>
</ListView>
Comissovocêjápossuiatransi çãodepáginas! Casovocêqueiravero
código-fontedaaplica çãoatéestemomento,acessemeugithubatravésdo
link:http://bit.ly/8-1GITcap7ParteI.
7.2 Ciclo de vida da aplicação
Émuitoimportantequevocêentendaociclodevidadeumaaplica çãoWin-
dowsPhoneparaquevocêpossamanterumaexperiênciaagradávelparao
usuário.Cadaaplicativopossuiumciclodequatroeventos: launch,suspend
eresume.
Originalmente,todoaplicativoestáemseuestado fechado.Nesteestado,
oaplicativonãoconsomememóriaerecursosdosmartphone.
Quandoousuárioabreoaplicativo,elepassapeloevento launch.Você
podeinjetarcódigoC #duranteestatransi çãocriandoummanipuladorpara
oeventoLaunchednaclasse App.xaml.cs.
103
E-book gerado especialmente para 


## Página 110

7.2. Ciclodevidadaaplica ção CasadoCódigo
Depoisdeaberto,oaplicativopodeconsumirrecursosdodispositivoati-
vamente,conformesuademanda. Esteestadopermaneceativoenquantoo
usuárioutilizaosoftware. Casoousuáriopressioneobotãovoltardodis-
positivoefecheseuaplicativo,elepassarápeloevento suspend,ouseja,seu
aplicativoestaráembackgroundnosistemaoperacional.
Casoousuáriopressioneobotão“windows”dodispositivooucliqueem
algumlinkparaoutroaplicativo,suaaplica çãotambémentraráemsuspensão.
Independentedaformaqueissoocorra,oevento Suspendingsempreé
disparado.
Oestadosuspensopodeserconsideradoumestadodepausa,ouseja,ele
nãoestásendoexecutado,porémtodooestadoatualpermanecearmazenado
namemória.Dessaforma,casoousuáriopressioneobotãovoltareretorne
paraseuaplicativo,eleéabertorapidamente,comosenuncativessesidopau-
sado.
Conformeousuárionavegaentrediferentesaplicativos,maisaplicativos
passamparaoestadode suspensão,fazendocomquemaismemóriaerecur-
sossejamconsumidos.Casoousuárioretorneparaseuaplicativoenquanto
eleestánoestadode suspensão,oevento Resumingédisparado.
Enquantosuaaplica çãoseencontraembackground,oWindowsPhone
iráfazerdetudoparaqueoaplicativocorrenterecebatodososrecursos
necessáriosparaqueelesejaexecutadodeformafluidaeissoincluialterar
oestadodeseuaplicativoestadopara terminado.
Oestadoterminadopodeserconsideradoumestadofinaldoaplicativo,
entretanto,apáginanaqualvocêestava,oestadodaaplica çãoeoestadoda
navegaçãosãoarmazenados.Casosejaabertonovamenteestandonessees-
tado,épossívelrecuperarasinforma çõesdoaplicativonamemória,passando
aimpressãoaousuáriodequenuncafoifechado.
Pararecuperarasinforma ções,podemosutilizarosmanipuladorespara
oseventosOnLaunched,queédisparadoquandoousuárioretornaasuaapli-
cação.Vocêdeveternotadoqueaopassarparaoestado terminadonenhum
eventoédisparado,oquetornaoevento Suspendingextremamenteimpor-
tante.
Afigura7.4ilustraofluxodescritonosparágrafosanteriores.
104
E-book gerado especialmente para 


## Página 111

CasadoCódigo Capítulo7. Navegaçãoeciclodevida
Figura7.4:Ciclodevidadeumaplicativo
7.3 NavigationHelper eSuspensionManager
Nesteponto,vocêjáaprendeuateoriasobreociclodevidadoseuaplicativo.
Agoraestánahoradevermosoquepodemosimplementarparamelhorara
experiênciadousuáriocomoestenovoconhecimento.
Oscomponentes NavigationHelpere SuspensionManagersão
fundamentaisparaaplicarmosestesconceitos. Elessãoutilizadosparaar-
mazenamentoegerenciamentodoestadoatualdapágina,ouseja,aspro-
priedadesdecadacampo.Quandoumaaplica çãoentranoestado suspenso,
estaspropriedadespermanecem,masquandoelaentranoestado terminado
perdemosestesvalores,algoquepodecausarfrustra çãoaousuáriofinal.
Vamosvisualizarcomoissofuncionanapáginaparacria çãodecontas.Vá
atéelaemseuemulador,preenchaoscamposepressioneatecla pesquisar
dodispositivo.Depoisdisso,pressioneobotão voltarevejaoqueacontece.
105
E-book gerado especialmente para 


## Página 112

7.3. NavigationHelpereSuspensionManager CasadoCódigo
Figura7.5:Aplicativosendorestauradodoestadodesuspensão
Comopodemosvernafiguraanterior,todooestadodapáginacontinuava
salvo,mesmoapóssairdoaplicativo.Issoaconteceupoisoaplicativoentrou
apenasnomodo suspenso. Felizmenteconseguiremossimularoaplicativo
nomodoterminadocomaajudadoVisualStudio.
Quandoseuaplicativoestiveremexecu çãovocêpoderávisualizarum
botãochamado“LifecycleEvents”comasseguintesopções:Suspend,Resume
eSuspendandshutdown(parafazersuaaplica çãoentrarnoestado termi-
nado),conformeilustrafigura 7.6
106
E-book gerado especialmente para 


## Página 113

CasadoCódigo Capítulo7. Navegaçãoeciclodevida
Figura7.6:Colocandosuaaplica çãonoestadoterminada
Apósfazerisso,refa çaotesteanteriorevocêperceberáque,aovoltar,seu
aplicativoseráabertocomodaprimeiravez.Vamosresolverissoutilizando
armazenandooestadodesuaaplica çãoutilizandooscomponentescitados
anteriormente.
Anteriormente no livro nós já sobrescrevemos o método
OnNavigatedTo, que ocorre quando o usuário é direcionada para
esta página. Agora, além dele, também vamos sobrescrever o método
OnNavigatedFrom, queéchamadoquandoousuáriosaidapágina, ou
seja, vamosarmazenarasinforma çõesquandoousuáriosaireinseri-las
novamentequandoousuárioretornarparaela.
Antesdemaisnadaprecisamosincorporaroscomponentesmenciona-
dos.Elessãoadicionadosautomaticamentequandovocêcriaumapáginado
tipo BasicPage iremoscriá-laparavisualizarmoscomoéfeitaautiliza ção
destescomponentes.
AocriarapáginaoVisualStudioirácriaremnossoprojetoapasta
Common,queconteráoscomponentescitados. Agoravamosabrirocódigo
danossa BasicPageevisualizaralgunspontos.
No construtor dessa página há a inicialização de um atributo pri-
107
E-book gerado especialmente para 


## Página 114

7.3. NavigationHelpereSuspensionManager CasadoCódigo
vadodotipo NavigationHelperetambémháaassinaturadoseven-
tos LoadStatee SaveStatedestecomponente. Alémdisso,nofimde
cadamétodo OnNavigateTo/Fromháumachamadaparaummétododo
mesmonomeparao NavigationHelper.Issoénecessárioparaqueseja
possívelarmazenaroestadodapáginaedoaplicativo.Agoraveremoscomo
fazerissoemnossaspáginasjáexistentes.
Antesdeimplementarmoso NavigationHelperprecisamosfazercom
queaaplica çãoconsigaidentificarapáginaemqueousuárioestavaquandoo
modosuspensãofoiativado,paraissoutilizamoso SuspensionManager.
Vamosatéoarquivo App.xaml.csnométodo OnLaunched.
Apósainicializa çãodo Framedeseuaplicativo,énecessárioregistrá-
lo no SuspensionManager, você pode fazer isso através do método
RegisterFrame.Alémdisso,vocêprecisaráfazerumachamadaaométodo
RestoreAsync()quandoaaplica çãoestivercomoestadoanterioriguala
terminado,conformeocódigo:
// Código padrão já implementado na criação do projeto
// Create a Frame to act as the navigation context and navigate
// to the first page
rootFrame = new Frame();
SuspensionManager.RegisterFrame(rootFrame, "AppFrame" );
rootFrame.CacheSize = 1 ;
if (e.PreviousExecutionState ==
ApplicationExecutionState.Terminated)
{
try
{
await SuspensionManager.RestoreAsync();
}
catch (SuspensionManagerException)
{
}
}
108
E-book gerado especialmente para 


## Página 115

CasadoCódigo Capítulo7. Navegaçãoeciclodevida
// Place the frame in the current Window
Window.Current.Content = rootFrame;
Comoagoraháumachamadaaummétodoassíncrono, énecessário
incluir a palavra reservadaasync na assinatura do método. Por fim,
seránecessáriofazerumachamadaaométodo SaveAsync()nométodo
OnSuspendingtambémdaclasse App.xaml.cs.
private async void OnSuspending ( object sender,
SuspendingEventArgs e)
{
var deferral = e.SuspendingOperation.GetDeferral();
await SuspensionManager.SaveAsync();
deferral.Complete();
}
Comissojágarantimosquealgumasinforma çõesdaaplica çãoserãosal-
vasquandoelaentraremmododesuspensão. Masagoravamosvoltarà
páginadecriaçãodecontaseimplementaromomentoemqueocorreasaída
dousuáriodestapágina.
O primeiro passo é incluir um atributo privado do tipo
NavigationHelper, inicializá-lo no construtor, criar um manipu-
ladorparaoseventos LoadStatee SaveStateefazerachamadaparaos
métodos OnNavigateTo/Fromdomesmomodoquenapáginadeexem-
plo.Tendoistoverificado,vamosarmazenarasinforma çõesnapropriedade
PageState.
private void NavigationHelper_SaveState
( object sender, SaveStateEventArgs e)
{
e.PageState[ "email" ] = _usuarioVM.Email;
e.PageState[ "usuario" ] = _usuarioVM.Nome;
e.PageState[ "senha" ] = _usuarioVM.Senha;
e.PageState[ "confirmacao" ] = _usuarioVM.ConfirmacaoSenha;
e.PageState[ "lembrarme" ] = _usuarioVM.EntrarAutomaticamente;
}
109
E-book gerado especialmente para 


## Página 116

7.3. NavigationHelpereSuspensionManager CasadoCódigo
O código anterior obtém todos os dados através doview model da
página. Da mesma forma, vamos preencher as informações do objeto
quandoousuáriovoltarparaapágina. Anteriormentehavíamosutilizado
oevento SaveState,masparaocarregamentodosdadosutilizaremoso
LoadState.
private void NavigationHelper_LoadState ( object sender,
LoadStateEventArgs e)
{
if (e.PageState != null )
{
_usuarioVM = new UsuarioVM();
if (e.PageState.ContainsKey( "email" ))
_usuarioVM.Email = e.PageState[ "email" ] as string ;
if (e.PageState.ContainsKey( "usuario" ))
_usuarioVM.Nome = e.PageState[ "usuario" ] as string ;
if (e.PageState.ContainsKey( "senha" ))
_usuarioVM.Senha = e.PageState[ "senha" ] as string ;
if (e.PageState.ContainsKey( "confirmacao" ))
_usuarioVM.ConfirmacaoSenha =
e.PageState[ "confirmacao" ] as string ;
if (e.PageState.ContainsKey( "lembrarme" ))
_usuarioVM.EntrarAutomaticamente =
Convert.ToBoolean(e.PageState[ "lembrarme" ]);
}
}
Agora,casovocêrefaçaotestepropostonocome çodestase ção,veráque
osdadossãorecuperadosassimqueapáginaéreaberta,oferecendoumasen-
saçãodequeelanuncahaviasidofechada.
Ocódigodoaplicativoatéestepontopodeserencontradoemmeugithub
atravésdolink:http://bit.ly/8-1GITcap7ParteII
110
E-book gerado especialmente para 


## Página 117

CasadoCódigo Capítulo7. Navegaçãoeciclodevida
7.4 Inicialização rápida
Caso você tenha testado oSuspensionManager em todas as páginas
veráqueaconteceumproblemaaotentarabrirautomaticamenteapágina
ProdutosHub. Issoocorrepoisestamoscarregandoosdadosapenasna
páginaprincipalenãoduranteainicializa çãodoaplicativo.
Vocêpodepensareminserirométododebuscadosdadosnomanipu-
ladordoevento Launched,masinfelizmenteissopodesetornarumprob-
lemaemumcenáriorealquandoaconexãoestiverlenta,porexemplo.Caso
esteeventodemoretempodemaisparaexecutar,osistemaoperacionalirá
fecharseuaplicativoeprovavelmenteelenãoirápassarpelasbateriasdetestes
antesdeentraroficialmentenalojaparadownload.
Outropontointeressanteéquenãoprecisamoscarregarosdadosdo
aplicativo até que o usuário precise deles, então vamos fazer com que
os dados sejam carregados somente quando o usuário entrar na página
ProdutosHub.xaml. Como já mostramos anteriormente, faremos isso
atravésdométodo OnNavigatedTo.
Vamoscriarummétodochamado CarregarDadosAsync(naclasse
Loja),queiráfazeroquenósestávamosfazendonoeventodeaberturada
aplicação.Porém,jávamosprepará-loparaserchamadodeformaassíncrona,
atravésdaspalavras-chaves asynce await,quevimosaodecorrerdolivro.
public async Task CarregarDadosAsync ()
{
string dados = await LeitorArquivo.LerAsync();
Loja.Dados = JsonConvert.DeserializeObject<Loja>(dados);
await Task.Delay( 3000 );
}
Notequenocódigoanteriorfoiinseridaumaesperadetrêssegundos,
apenasparaquenossocarregamentofiqueumpoucomaislentoeparecido
comumcenáriocommaiorquantidadededados.Agorateremosdealterar
umpouconossocódigonapágina ProdutosHub.Primeiro,criaremostrês
atributosprivadosparaarmazenaroscomponentesdotipo ListView.
public sealed partial class ProdutosHub : Page
{
111
E-book gerado especialmente para 


## Página 118

7.4. Inicializaçãorápida CasadoCódigo
private ListView listaCategorias;
private ListView listaProdutos;
private ListView listaPromocoes;
//Código já existente ...
}
Agoracriaremosométodo VincularDadosondeiremosfazerovín-
culodessaslistasutilizandoosLINQsqueatualmenteestãonomanipulador
deeventode Loadeddecadaumadaslistas. Alémdisso,removeremos
ocódigodestesmanipuladores,fazendocomqueelessirvamapenaspara
preencherosatributosinternosdaclasse,evalidemomomentoemquetodos
osatributosestãopreenchidosparaqueosdadospossamserconectados.
private void ListaCategoria_Loaded ( object sender,
RoutedEventArgs e)
{
listaCategorias = sender as ListView;
CarregarDadosAsync();
}
private void ListaPromocoes_Loaded ( object sender,
RoutedEventArgs e)
{
listaPromocoes = sender as ListView;
CarregarDadosAsync();
}
private void ListaProdutos_Loaded ( object sender,
RoutedEventArgs e)
{
listaProdutos = sender as ListView;
CarregarDadosAsync();
}
public void VincularDados ()
{
listaCategorias.ItemsSource =
112
E-book gerado especialmente para 


## Página 119

CasadoCódigo Capítulo7. Navegaçãoeciclodevida
( from produtos in Loja.Dados.Produtos
select new CategoriaVM
{
Id = produtos.Categoria.Id,
Descricao = produtos.Categoria.Descricao
}).Distinct().ToList();
listaPromocoes.ItemsSource =
( from produtos in Loja.Dados.Produtos
where produtos.PrecoPromocao != 0
select new ProdutoVM
{
Id = produtos.Id,
Descricao = produtos.Descricao,
Preco = produtos.Preco,
PrecoPromocao = produtos.PrecoPromocao,
Icone = produtos.Icone
})
.OrderByDescending(produto => produto.Desconto)
.ToList();
listaProdutos.ItemsSource =
( from produtos in Loja.Dados.Produtos
where produtos.Id == 3 || produtos.Id == 4
select new ProdutoVM
{
Id = produtos.Id,
Descricao = produtos.Descricao,
Icone = produtos.Icone,
Preco = produtos.Preco,
PrecoPromocao = produtos.PrecoPromocao
})
.ToList();
}
Note que estamos utilizando em nosso código o método
CarregarDadosAsyncdapáginaenãodoobjeto Loja. Nestemétodo,
vamosverificarseaslistasjáestãoprontaseseosdadosestãocarregados.
113
E-book gerado especialmente para 


## Página 120

7.4. Inicializaçãorápida CasadoCódigo
Casonãoestejam,faremoscomqueelessejamcarregadosdeformaassín-
crona,ouseja,emumathreaddiferentedathreadprincipaldaaplica ção.
Dessaforma,nãoiremosbloquearnossainterface,evitandoaimpressãode
queoaplicativoestátravado.
Para fazer isso, vamos criar mais um métodoasync, chamado
CarregarDadosAsync,aindanapágina ProdutosHub.xaml.Eleiráver-
ificarseosdadosjáestãocarregadose,casonãoestejam,iráchamarométodo
assíncronodaclasse Lojaparacarregá-loseentãochamaremosométodo
VincularDadosparafazeraliga çãodasinforma ções.Vejaocódigo:
private async void CarregarDadosAsync ()
{
if (listaCategorias != null &&
listaPromocoes != null &&
listaProdutos != null )
{
if (Loja.Dados.Produtos == null )
{
await Loja.Dados.CarregarDados();
VincularDados();
}
else
{
VincularDados();
}
}
}
Nestepontovocêjápoderáverosdadossendocarregadosquandoabrir
apágina. Aindanãoremovaodelayinseridoduranteocarregamento,pois
eleseráútilparavermosaimportânciadoarmazenamentodoestadodaapli-
cação.
Aindatemosumamelhoriadeusabilidadeparafazer: enquantoosda-
dosestiveremsendocarregados, ousuárionãoveránenhumamensagem
avisandoomotivodeosdadosnãoestaremaparecendo. Vamoscriaruma
mensagemeumabarradeprogressoqueficaráemumpainelsobreapágina
enquantoosdadosestiveremsendocarregados.
114
E-book gerado especialmente para 


## Página 121

CasadoCódigo Capítulo7. Navegaçãoeciclodevida
Faremos isso adicionando um componente que irá conter um
TextBlock e um ProgressRing, que estarão visíveis por padrão e
serãoescondidosapósaexecu çãodométodoquevinculaosdados.
<Grid x:Name= "pnlCarregando" >
<Grid.RowDefinitions>
<RowDefinition Height= "*" />
<RowDefinition Height= "150" />
<RowDefinition Height= "*" />
</Grid.RowDefinitions>
<StackPanel Grid.Row= "1" Background= "#7F000000" >
<TextBlock Margin= "20"
FontSize= "{ThemeResource TextStyleExtraExtraLargeFontSize}"
HorizontalAlignment= "Center" >
Carregando dados...
</TextBlock>
<ProgressRing IsActive= "True" Background= "{x:Null}" />
</StackPanel>
</Grid>
Comisso,temosumresultadobastanteagradávelaousuário,comoilustra
afigura7.7.
115
E-book gerado especialmente para 


## Página 122

7.4. Inicializaçãorápida CasadoCódigo
Figura7.7:CarregandoDados
Ocódigodoaplicativoatéestepontoseencontraemmeugithubatravés
dolink:http://bit.ly/8-1GITcap7ParteIII.
116
E-book gerado especialmente para 


## Página 123

Capítulo8
Integraçãocomosistema
operacional
Nestecapítulovamoscriardiversasformasdeintegrarnossoaplicativocom
osistemaoperacionalparadisponibilizarumamelhorexperiênciaparao
usuário. Masantesdepartirmosparaestetópico,vamosfinalizarasfun-
cionalidadesemabertoemnossaaplica ção,istoé,vamosfazerumanova
páginanoaplicativo. Seráumapáginaparadetalhamentodeproduto,que
deveráserchamadaquandoousuárioselecionarumprodutodequalquer
lista.Alémdisso,faremoscomqueapesquisadeprodutosnapáginadehub
passeafuncionar.
E-book gerado especialmente para 


## Página 124

8.1. Finalizandoasfuncionalidadesjácriadas CasadoCódigo
8.1 Finalizando as funcionalidades já criadas
Vamoscomeçarcriandoumapáginaparaodetalhamentodoproduto. Ela
devecontertodasaspropriedadesdeumproduto,eseráutilizadasempre
queousuárioselecionarumprodutoemumadaslistas.Éclaroquecriaremos
apenasumapáginaebuscaremososseusdadosdeacordocomoparâmetro
querecebermosaoabri-la.
Não entraremos em muitos detalhes, pois já fizemos todas estas im-
plementações anteriormente. Vamos criar uma página que recebe como
parâmetroo Iddoprodutoeexibesuaspropriedades,algoquevocê,neste
ponto,jáestáaptoafazer.Tentefazê-lasemelhanteàilustradapelafigura 8.1.
Figura8.1:Detalhesdeumproduto
118
E-book gerado especialmente para 


## Página 125

CasadoCódigo Capítulo8. Integraçãocomosistemaoperacional
Tambémdevemoscriarumapáginaparaqueousuáriopossapesquisar
osprodutos.Noscapítulosanteriores,criamosumbotãona CommandBarno
hubdeprodutos;agoracriaremosasuafuncionalidade.
Nestecaso,nãoénecessáriaumapáginanova,jáquetemosapágina
que lista todos os produtos, ou mesmo os produtos por categoria. Va-
mosaproveitá-latambémparalistarosresultadosdapesquisa,entãovamos
prepará-laparareceberumnovotipodeparâmetro,chamado Pesquisa.
Para fazer isso devemos criar a classePesquisa em nossa pasta
Auxiliar,eledeveráconterpropriedadesparaarmazenaroidentificador
deumacategoriaeadescri çãodeumproduto,conformeocódigo:
public class Pesquisa
{
public int CategoriaId { get ; set ; }
public string DescricaoProduto { get ; set ; }
}
Agoranossoparâmetroqueanteseradotipo intecontinhaapenaso
identificadordacategoriapossuiumtipomaiscomplexo,masoprincípio
defuncionamentocontinuaigual.Paramelhoraraexperiência,faremoscom
queapesquisaportextonãosejasensívelamaiúsculas,ouseja,vamossempre
compararasinforma çõesemminúsculo(utilizandoométodo ToLower),
tornandoestadiferen çairrelevante.Vejaocódigo:
if (_parametrosPesquisa != null )
{
if (_parametrosPesquisa.CategoriaId != 0 )
{
produtos = produtos.Where(produto =>
produto.CategoriaId ==
_parametrosPesquisa.CategoriaId).ToList();
Titulo.Text = produtos.FirstOrDefault().CategoriaDescricao;
}
else
if (! string .IsNullOrEmpty(
_parametrosPesquisa.DescricaoProduto))
{
119
E-book gerado especialmente para 


## Página 126

8.1. Finalizandoasfuncionalidadesjácriadas CasadoCódigo
produtos = produtos.Where
(produto =>
produto.Descricao.ToLower()
.Contains(
_parametrosPesquisa.DescricaoProduto.ToLower()))
.ToList();
Titulo.Text = "resultados" ;
}
}
Estasegundaparteseráumpoucomaisdetalhada,poisaindanãofizemos
nadaparecido.Criaremosumpainelcomvisibilidadedinâmica,ouseja,ela
ficaráinvisívelnamaiorpartedotempo,masquandoousuáriopressionaro
botão pesquisardabarradaaplica ção,elesetornarávisíveleousuário
poderádigitarsuapesquisaemumcampo.
Aprimeiracoisaafazerécircundartodoocomponentede Hubcomum
Griddivididoemduaslinhas,umaparao Hubjáexistenteeoutraparao
paineldepesquisa.Vamospermitirqueo Hubocupeasduaslinhas,poisna
maiorpartedotempoopaineldepesquisaestaráoculto.Issoéfeitoatravés
dapropriedade Grid.RowSpan.
Nasegundalinhadestenovo Grid,adicionaremosmaisum Gridque
ficaráocultoporpadrão.Nestecomponente,devehaverum TextBoxqueo
usuáriopossautilizaremsuaspesquisas.Vocêtambémdevecriarummanip-
uladorparaoseventos KeyUpe LostFocusdeste TextBox,além,éclaro,
decriarummanipuladorparaoeventode Clickdobotão pesquisarda
barradaaplica ção.
<Grid>
<Grid.RowDefinitions>
<RowDefinition Height= "*" />
<RowDefinition Height= "90" />
</Grid.RowDefinitions>
<Hub Title= "CompreAqui" Grid.RowSpan= "2" >
<!--<Componente Hub já existente >-->
</Hub>
120
E-book gerado especialmente para 


## Página 127

CasadoCódigo Capítulo8. Integraçãocomosistemaoperacional
<Grid Grid.Row= "1" x:Name= "PainelPesquisa"
Background= "#FF1F1F1F" Visibility= "Collapsed" >
<TextBox Margin= "10"
VerticalAlignment= "Top" x:Name= "CampoPesquisa"
KeyUp= "CampoPesquisa_KeyUp"
LostFocus= "CampoPesquisa_LostFocus" />
</Grid>
</Grid>
Apartevisualdestapáginajáestápronta.Agoraprecisamosimplementar
ocódigoC #.Vamoscome çarcriandodoismétodos: ExecutarPesquisa
e DesaparecerPainelPesquisa.
Ambos são bastante simples: no método
DesaparecerPainelPesquisa, basta limparmos o campo de texto
dapesquisaevoltarmosavisibilidadedopainelpara Collapse.
Jánométodo ExecutarPesquisa,devemosobterasinforma çõesdo
TextBox,direcionarousuárioparaapágina Produtos.xamlpassando
osparâmetrosdepesquisae,porfim,desaparecercomopaineldepesquisa
utilizandoométodocitadoanteriormente.Observeocódigo:
private void ExecutarPesquisa ()
{
Pesquisa pesquisa = new Pesquisa();
pesquisa.DescricaoProduto = CampoPesquisa.Text;
this .Frame.Navigate( typeof (Produtos), pesquisa);
DesaparecerPainelPesquisa();
}
private void DesaparecerPainelPesquisa ()
{
CampoPesquisa.Text = string .Empty;
PainelPesquisa.Visibility = Visibility.Collapsed;
}
121
E-book gerado especialmente para 


## Página 128

8.1. Finalizandoasfuncionalidadesjácriadas CasadoCódigo
Comisso,játemosasduasprincipaisfun çõesparapesquisaimplemen-
tadas; agoradevemossaberomomentodeutilizá-las. Quandoousuário
pressionar(evento KeyUp)atecla Enterdoteclado,devemosconfirmara
pesquisae,quandoousuárioselecionaroutrocamponapágina,foraocampo
detextodapesquisaeobotãoda CommandBar(evento LostFocus),deve-
mosfazeropaineldesaparecer,conformeocódigo:
private void CampoPesquisa_LostFocus
( object sender, RoutedEventArgs e)
{
if ( btnAppBar.FocusState ==
Windows.UI.Xaml.FocusState.Unfocused)
DesaparecerPainelPesquisa();
}
private void CampoPesquisa_KeyUp
( object sender, KeyRoutedEventArgs e)
{
if (e.Key ==
Windows.System.VirtualKey.Enter)
{
ExecutarPesquisa();
}
}
Agora,parafinalizarmosaimplementa çãonestapágina,precisamosim-
plementaromanipuladordoevento Clickdobotãodabarradaaplica ção.
Estemétodoterácomportamentosdistintosconformeavisibilidadedopainel
depesquisa:casoeleestejainvisível,devemosmostrá-loaousuário;casoele
jáestejavisível,devemosexecutarapesquisacomasinforma çõesjáinseridas
nocampo.
private void ApplicationBarIconButton_Click
( object sender, EventArgs e)
{
if (PainelPesquisa.Visibility ==
System.Windows.Visibility.Collapsed)
122
E-book gerado especialmente para 


## Página 129

CasadoCódigo Capítulo8. Integraçãocomosistemaoperacional
{
PainelPesquisa.Visibility =
System.Windows.Visibility.Visible;
CampoPesquisa.Focus();
}
else
{
ExecutarPesquisa();
}
}
Agorajápodemosfazernossaspesquisas,comoilustraafigura 8.2.
Figura8.2:Pesquisandoprodutos
Mesmo com a funcionalidade pronta, ainda temos trabalho a fazer:
quandoousuárioexecutarumapesquisaquenãoretornanenhumdado,ele
seráenviadoparaestapáginavazia.Ésempremaisagradávelaousuáriore-
ceberumamensagemdequenãoforamencontradosdadoscomapesquisa
digitada—vejaadiferençanafigura8.3.
123
E-book gerado especialmente para 


## Página 130

8.2. EntendendoosLivetiles CasadoCódigo
Figura8.3:Pesquisasemdados
Estaseráumaimplementa çãomuitosimples,bastacircundaralistade
produtoscomum StackPaneleinserirocomponentedetextocomamen-
sagem. Estecomponenteficaráinvisívelporpadrãoe,nomomentodevin-
cularosdados,bastafazerumaverifica ção.Casonãohajadados,tornamoso
campovisível.
Agoraqueterminamosnossasimplementa çõespendentes,voltaremosao
assuntoprincipaldestecapítulo.Casovocêdesejaobterouverificarocódigo
doprojetoatéesteponto,eleseencontranomeugithubnolink: http://bit.ly/
8-1GITcap8ParteI.
8.2 Entendendo os Live tiles
SevocêjáestáacostumadooujáconheceoWindowsPhone,provavelmente
jáouviufalardas live tiles.Tratam-sederetângulosquerepresentamosícones
daaplicaçãocomonosoutrossistemasoperacionais.Entretanto,oslivetiles
vãoalémdoquesóabriroaplicativo:elespodemserumaboafontedeco-
124
E-book gerado especialmente para 


## Página 131

CasadoCódigo Capítulo8. Integraçãocomosistemaoperacional
municaçãoentreoaplicativoeousuário,mesmoquandoousuárioestácom
oaplicativofechado.
Os live tiles podem receber atualizações de informações contínuas,
mesmocomoaplicativofechado. Ousuáriotambémpodeescolherentre
tamanhosdiferentesparaotiledeseuaplicativo.
Alémdisso,umaaplicaçãopodegerarmaisdeumtipodelivetile,ouseja,
dentrodamesmaaplica çãovocêpodetertilessecundários.Umbomexemplo
deutilizaçãodesterecursoéoaplicativopessoas,comoqualvocêpodegerar
umtilediferenteparacadacontatodoseusmartphone.
Antesdecome çarmosaimplementarénecessáriocompreendermosas
terminologiasqueenvolvemotermotile. Emvárioscasososlivetilespos-
suemumaanimação,emgeralestaanima çãoconsisteemgirarotileemostrar
apartedetrásdotile.Aestasegundapartedamosonomede Peek.
Emalgunscasososlivetilestambémprecisamexibirumnúmerogrande,
estenúmeroéconhecidocomo Block,eleéutilizadoparafazerumacon-
tagemdee-mailsporexemplo.Algunsaplicativospossuemforteliga çãocom
imagensoufotos,paraestescasosháumobjetochamado ImageCollection,
afigura8.4ilustraestescomponentesemumlivetile.
Figura8.4:TileutilizandootemplateIconic
125
E-book gerado especialmente para 


## Página 132

8.2. EntendendoosLivetiles CasadoCódigo
Existemdiversostiposdiferentesdetemplatesdetilesparaaplataforma
Windows,nãocabeaoescopodestelivrodescrevercadaumdeles,masé
aconselhávelqueparaacria çãodeumaaplica çãorealvocêbusquepormais
informações.Atravésdolink: http://bit.ly/tileTemplatevocêpodevisualizar
umcatálogodetemplatesdisponibilizadopelaMicrosoft.
Noexemplodolivro,vamosimplementarumtemplatesimples,masesteja
àvontadecasoqueiratestarasoutraspossibilidades.Issoéfácildefazer,uma
vezquevocêconheceaspropriedadesreferenciadasnafiguraanterior.
Primeiro,vamosabriroarquivo Package.appxmanifestquejávimos
anteriormente.Eleseencontranodiretórioraizdesuaaplica ção.Naaba Vi-
sual Assets,podemosverdiversaspropriedadesdenossoaplicativo,conforme
afigura8.5:
Figura8.5:ArquivoManifest
Iremosfazerdiversasmodifica çõesemnossoaplicativo.Primeiro,vamos
escolherumnovoíconeparanossaaplica ção—énecessárioutilizarasima-
genscomotamanhoindicadoparacadatemplate,dessaformaelanãosofrerá
126
E-book gerado especialmente para 


## Página 133

CasadoCódigo Capítulo8. Integraçãocomosistemaoperacional
nenhumadistorção—,entãoiremosaproveitaroíconequejácriamospara
colocarmosnapáginadeaberturaevamosredimencioná-losparaasdimen-
sõescorretasemcadatile.
Notetambémque,aofazercomqueofundodaimagemsejatransparente,
osistemafazcomqueotileautomaticamenterecebaacordotemadousuário,
casoqueirautilizarumacordefundoespecíficaésópreencherapropriedade
Backgroundtambémexibidanestatela.
Vamosselecionarparatodosostemplatesoscampos ShowName,issoirá
fazercomqueonomedenossaaplica çãosejaexibidonostiles.
Comissojáconseguimosvisualizaroíconeeosdiferentesformatosdetile
denossaaplica ção,inclusivecomtemasdiferentesselecionadospelousuário,
conformeilustraafigura 8.6
Figura8.6:Tiles
Apesardequenãoiremosutilizarestatécnicaparabenefíciodenosso
aplicativo,éimportantequevocêconhe çaumaformadeatualizarosdados
deseulivetile.Portanto,vamoscriarumexemplo,apenasparafinsdeapren-
dizagem.
Vamosfazercomque,quandoousuáriocriarumanovacontanoaplica-
tivo,elepossaveroseunomedeusuárioee-mailnotile. Então,vamos
voltaràpágina CriarConta.xamleadicionarumnovométodo,chamado
AtualizarLiveTile.Estemétodoreceberáonomeeoe-maildousuário
porparâmetroefarásuasatualiza ções.
DiretamentepeloSDKénecessáriocriaroXMLdolivetileatravésde
strings.Felizmenteháumabibliotecaquejáautomatizaesteprocesso,aqual
podemosobtervia NuGet.Elachama-se NotificationExtensionsetambém
estaráincorporadanoprojetodisponívelnogithub.
127
E-book gerado especialmente para 


## Página 134

8.2. EntendendoosLivetiles CasadoCódigo
Háumobjetochamado TileContentFactory,quepossuidiversos
métodosparacria çãodetilesnostemplatesdisponíveis. Iremosutilizá-lo
paracriarumtilelargo(wide)eotilequadradodetamanhomédio. Nesta
bibliotecavocêdevesemprecriardomaiorparaomenor,jáqueumengloba
ooutro.Depoisutilizaremosoobjeto TileUpdateManagerdaAPInativa
paraatualizarosdadosdenossotile.
private void AtualizarLiveTile ( string usuario, string email)
{
ITileWide310x150ImageAndText01 wideTile =
TileContentFactory.CreateTileWide310x150ImageAndText01();
wideTile.TextCaptionWrap.Text =
string .Concat(usuario, " - " ,email);
wideTile.Image.Src =
@"ms-appx:/Assets/WideLogo.scale-240.png" ;
ITileSquare150x150PeekImageAndText01 squareTile =
TileContentFactory
.CreateTileSquare150x150PeekImageAndText01();
squareTile.TextBody1.Text = usuario;
squareTile.TextBody2.Text = email;
squareTile.Image.Src =
@"ms-appx:/Assets/Square71x71Logo.scale-240.png" ;
wideTile.Square150x150Content = squareTile;
TileUpdateManager.CreateTileUpdaterForApplication().
Update(wideTile.CreateNotification());
}
Agoracolocaremosumachamadaaestemétodoapósenviarousuário
paraapágina ProdutosHub.Afigura 8.7mostraadiferen çaentreostiles
daaplicaçãoantesedepoisdestaatualiza ção.
128
E-book gerado especialmente para 


## Página 135

CasadoCódigo Capítulo8. Integraçãocomosistemaoperacional
Figura8.7:Atualiza çãodolivetile
Éimportanteteremmentequeestaatualiza çãonãoseriabem-vindaem
umaplicativoreal,poisdevemserexibidasapenasinforma çõesrelevantesao
usuário.Lembramosqueesseexemplofoicriadoapenasparaaprendizagem.
8.3 Criando tiles secundários
Jáaprendemosacriarotileprincipaldenossoaplicativoeafazeratualiza ções
nestetile.Agoravamosvercomocriartilessecundários,comosquaispoder-
emosdirecionarousuárioparaumapáginaespecíficaemnossoaplicativo.
Nós criaremos tiles secundários para as páginasProdutos.xamle
ProdutoDetalhe.xaml. Napáginadelistagemdeprodutos, ousuário
poderáarmazenarumatalhoparaverificarosprodutosdeumacategoriaou
deumresultadodepesquisa. Jánapáginadedetalhamentodeproduto,o
usuáriopoderácriarumatalhoparaumúnicoproduto,paraacompanhar,
porexemplo,omomentoemqueeleentraemumapromo ção.
129
E-book gerado especialmente para 


## Página 136

8.3. Criandotilessecundários CasadoCódigo
Vamoscomeçarcomapágina Produtos.xaml.Primeiro,habilitamos
a CommandBardestapáginaeinserimosumbotãoparafixarnatelainicial.
Vocêtambémdevecriarummanipuladorparaoevento Clickdestebotão.
Nós utilizamos anteriormente o objetoTileUpdateManager, cuja
funçãoégerenciarotileprincipal,masagoraprecisaremosdeumcompo-
nenteconhecidocomo SecundaryTile,quegerenciaostilessecundários
desuaaplica ção.Vamoscriarométodo CriarTileSecundarianocódigo
destapágina,quedevecriarumalivetileconformefizemosanteriormente.
Otítulodonovotileseráomesmoqueotítulodestapágina,alémde
conteralgumasinforma çõessobreonossoaplicativo,conformeocódigo:
public async void CriarTileSecundaria ()
{
SecondaryTile tileSecundaria =
new SecondaryTile ( "pesquisa" );
tileSecundaria.DisplayName =
string .Concat( "Pesquisa: " , Titulo.Text);
tileSecundaria.Arguments =
string .Concat( "Produtos:" ,
_parametrosPesquisa.CategoriaId, ":" ,
_parametrosPesquisa.DescricaoProduto);
tileSecundaria.VisualElements
.ShowNameOnSquare150x150Logo = true ;
tileSecundaria.VisualElements
.Square150x150Logo =
new Uri ( "ms-appx:///Assets/Logo.scale-240.png" );
if (SecondaryTile.Exists(tileSecundaria.TileId))
{
await tileSecundaria.UpdateAsync();
}
else
{
await tileSecundaria.RequestCreateAsync();
130
E-book gerado especialmente para 


## Página 137

CasadoCódigo Capítulo8. Integraçãocomosistemaoperacional
}
}
Note que na criação desse tile nós preenchemos uma propriedade
chamada Argument,queéutilizadaparaquepossamospassarosparâmetros
queoaplicativoiráreceberquandoeleforaberto.Porfimvamoscompletaro
manipuladordoeventode Click,simplesmentefazendoumachamadapara
ométodoanterior,vejaocódigo:
private void Fixar_Click ( object sender, RoutedEventArgs e)
{
CriarTileSecundaria();
}
Você já conseguirá fixar seus tiles secundários através da página de
listagemdeprodutos,entretantoeleteráamesmafuncionalidadequeotile
padrãodaaplica ção,emnossoexemploédesejávelqueousuáriosejadi-
recionadoparaapáginadelistagem. Parafazerisso,precisamosalteraro
comportamentodométodomanipuladordoevento Launchedecapturaros
parâmetrosenviadospornossatile.
Vocêjápoderáfixarseustilessecundáriosatravésdapáginadelistagem
deprodutosatravésdobotãoda ApplicationBar,conformeilustraafigura
8.8.
131
E-book gerado especialmente para 


## Página 138

8.3. Criandotilessecundários CasadoCódigo
Figura8.8:ArquivoManifest
Ométodo OnLauncheddaclasse App.xaml.csemumdeterminado
momentoavaliaseoconteúdodoframedoaplicativoestánulo,oquesignifi-
cariaqueoaplicativoestásendoabertoagorasemrestaura çãodeestado.Após
estaverificaçãoaclassedirecionaousuárioparaa MainPagedoaplicativo.
Vamosalterarestaverifica çãoparatambémverificarseexistemparâmet-
rosdeinicializa ção,casoexistamdevemosvalidarosparâmetroseenviaro
usuárioparaapáginacorreta. Estamodifica çãofoifeitacomotrechode
códigoaseguir.
protected async override void OnLaunched
(LaunchActivatedEventArgs e)
{
// Código inalterado ..
132
E-book gerado especialmente para 


## Página 139

CasadoCódigo Capítulo8. Integraçãocomosistemaoperacional
// ...
if ( rootFrame.Content == null ||
! string .IsNullOrEmpty(e.Arguments))
{
// Código inalterado ..
// ...
rootFrame.Navigated += this .RootFrame_FirstNavigated;
if ( string .IsNullOrEmpty(e.Arguments))
IrParaPagina(rootFrame, typeof (MainPage),e.Arguments);
else
{
string [] argumentos = e.Arguments.Split( ' : ' );
if (argumentos[ 0 ] == "Produtos" )
{
Type pagina = typeof (Produtos);
Pesquisa pesquisa = new Pesquisa();
pesquisa.CategoriaId = Convert.ToInt32(argumentos[ 1 ]);
pesquisa.DescricaoProduto = argumentos[ 2 ];
IrParaPagina(rootFrame, pagina, pesquisa);
}
}
}
}
private static void IrParaPagina
(Frame rootFrame, Type page, object arguments)
{
if (!rootFrame.Navigate(page, arguments))
throw new Exception ( "Failed to create initial page" );
}
Apesardeafuncionalidadedecriarumtilesecundáriotersidofeitacom
sucesso,aindanosrestaresolveralgunsproblemas.Agora,casoousuárioen-
trenoaplicativoatravésdeumatilesecundária,eleiráreceberumaexce ção
nãotratada,issoocorreporquesóestamosverificandoseosdadosestãocar-
regadosnapágina ProdutosHub.
133
E-book gerado especialmente para 


## Página 140

8.4. ConhecendooShareContract CasadoCódigo
Bastainserirumaverifica çãosimplesecriarumpainelparanotificarque
osdadosestãosendocarregados,comojáfazemosnohubdeprodutos.Tam-
bémháoutrocaso,quandoousuárioentranoaplicativoatravésdeumatile
secundáriaeoaplicativoestiveremmodoterminado,elenãoiráconseguir
acessarorestodaaplica ção,casoelepressioneobotãovoltaraaplica çãoserá
fechada,poisnãoexistenadanapilhadenavega ção. Issopodesercontor-
nadoadicionandoumcomandosecundárionabarradecomandosparalevar
ousuárioatéapáginainicial.
Esteitemdemenudeveservisívelapenasquandoaaplica çãoforaberta
atravésdotilesecundário.Vamosadicioná-loefazercomqueousuárioseja
direcionadoparaapágina MainPage.xaml,lembrandoque,seelejáestiver
autenticado,eleseráredirecionadoparaapágina ProdutosHub.xaml.
Estemesmoprocedimentodeveráserfeitonapáginadedetalhamentode
produto,desdeacria çãodatileatéotratamentonacargadosdados.Nãoé
necessáriomeprolongarexplicandocomofazerestemesmoprocedimento
napáginadedetalhamentodeproduto,poisoprocedimentoseráomesmo.
Apenasaltereosdadosdotilequevocêjulgarimportanteetenteimple-
mentarissosozinho. Seprecisar,voltealgumaspáginasereleiaomodode
criação.Lembre-se:programarseaprendepraticando!
Casovocêtenhamaisexperiênciaemprogramação,sugiroquetodases-
tasfunçõesrepetidassejamimplementadasemumobjeto. Nestelivro,elas
sãoimplementadasseparadamenteparafinsdidáticos,masemumaimple-
mentaçãoreal,oreaproveitamentodocódigoébastanteimportante.
Depois de já ter implementado essa funcionalidade, você pode con-
ferirocódigoqueseencontraemmeugithubatravésdolink: http://bit.ly/
8-1GITcap8ParteII.
8.4 Conhecendo o ShareContract
Oscontratosou Contractsfazempartedeumconceitomuitoimportante
nodesenvolvimentoparaaplataformaWindows/WindowsPhone. Através
deles,épossívelreutilizarfun çõesquejáexistemnodispositivoemoutros
aplicativos. Porexemplo,casosejanecessárioenviarmosume-mailatravés
denossoaplicativo,nãoprecisaríamosimplementarestafuncionalidadeno
134
E-book gerado especialmente para 


## Página 141

CasadoCódigo Capítulo8. Integraçãocomosistemaoperacional
próprioaplicativo,poisjáexistemalgunsquetratamespecificamenteeste
problema.
Basicamente,reaproveitamosfuncionalidadesqueoutrosaplicativosjá
fazemparaquenossoaplicativosepreocupesomenteemresolveroproblema
queelesepropõearesolver.Dessaforma,nãoretiramosofocododesenvolvi-
mento.
Comojávimosnocapítuloanterior,sobrenavega ção,semprequeuma
novaaplica çãoéaberta,oestadodanossaaplica çãoéalterada. Portanto,
tenhaciênciadequeseuaplicativopodeentrarnoestado terminated(apesar
denãosercomum)evocêprecisarárestaurarseuestado.
Oscontratoscitadosanteriormentesãosubdivididosemdoistipos: Tar-
geteSource.Elestêmumadiferen çabastantesignificativaentresi:asapli-
caçõesqueimplementamocontratodotipo targetsãoaspublicadorasde
conteúdo,ouseja,Facebook,Twitter,e-mailsetc. emgeralexistirãomenos
aplicaçõesdestetipoquedotipo source.Asimplementa çõesdotipo source
sebaseiamemcompartilhardadosouarquivos,ouseja,suaaplica çãoéuti-
lizadacomofontededadosporalgumaoutra.
Paratermosaexperiênciadeimplementarumcontratodotipo source,
vamosexplorarumexemplobastantesimples.Napáginadedetalhamentodo
produto,vamosinserirumaop çãona CommandBarparacompartilharmos
oprodutoemredessociais( share targets).Vocêveráqueissopodeserfeito
deumamaneiraincrivelmentesimples.
Primeiro,vamosalterarapáginaparainserirobotãoparacompartilhar,
conformeocódigo:
<AppBarButton
Label= "compartilhe"
Click= "Compartilhar_Click"
Icon= "ReShare" >
</AppBarButton>
NocódigoC #dapágina,teremosdefazeralgumasmodifica ções,lembra-
sequefoiditoqueocompartilhamentodeinforma çõeséfeitadeformain-
diretaatravésdosistemaoperacional?Agoraéexatamenteissoqueteremos
defazer,precisamosnotificarosistemaqueiremoscompartilhardadosnesta
135
E-book gerado especialmente para 


## Página 142

8.4. ConhecendooShareContract CasadoCódigo
página,paraquequandoforselecionadoum targetdocontratoelesaibaonde
buscarosdados.
Parafazerisso,vamoscriarummétodochamado OnDataRequested,que
recebedoisparâmetros:umobjetodotipo DataTransferManagereoutro
dotipo DataRequestedEventArgs.Esteseráométodoqueseráchamado
pelosistemaoperacionalpararequisitarosdadosdenossoaplicativo.
private void OnDataRequested
(DataTransferManager sender, DataRequestedEventArgs args)
{
}
Antesdeinserirmosalgumcódigonestemétodoprecisamosnotificaro
sistemaoperacionalqueestapáginacompartilhadados. Alémdissotam-
béménecessárionotificarosistemaquandoeladeixadecompartilharda-
dos,ouseja,quandoousuáriosaidestapágina. Parafazerissovamosin-
serirumtrechodecódigonométodo OnNavigatedToesobrescrevero
método OnNavigatedFromvinculandoométodorecém-criadoaoevento
DataRequested.
protected async override void
OnNavigatedTo (NavigationEventArgs e)
{
// Código já existente
DataTransferManager
.GetForCurrentView()
.DataRequested += OnDataRequested;
}
protected override void OnNavigatedFrom (NavigationEventArgs e)
{
base .OnNavigatedFrom(e);
DataTransferManager
.GetForCurrentView()
.DataRequested -= OnDataRequested;
}
136
E-book gerado especialmente para 


## Página 143

CasadoCódigo Capítulo8. Integraçãocomosistemaoperacional
Comissofeitojápodemosimplementarométodocriado,vamoscriar
umchamado“pacotededados”paracompartilhamento,oqueéfeitoatravés
doobjeto DataRequestdisponívelnoparâmetro args.Vocêpodecom-
partilhartiposdiferentesdeconteúdos:imagens,Uris,linksparaaplica çõese
textos.Paramantermosoexemplosimples,vamoscompartilharapenastex-
tos.
private void OnDataRequested
(DataTransferManager sender, DataRequestedEventArgs args)
{
ProdutoVM dataContext = DataContext as ProdutoVM;
DataRequest dataRequest = args.Request;
dataRequest.Data.Properties.Title = txtTitulo.Text;
dataRequest
.Data
.Properties
.Description = string .Concat( "Compartilhamento do produto " ,
dataContext.Descricao);
string texto = string .Concat( "Confiram o produto " ,
dataContext.Descricao, " no aplicativo CompreAqui,
está custando apenas ", dataContext.PrecoAPagar, " R$. ");
dataRequest.Data.SetText(texto);
}
Tambéménecessáriofazerachamadaparaosistemaoperacionalativar
os share targetsquandoousuáriopressionarobotãona CommandBar,basta
inseriraseguintelinhadecódigo:
private void Compartilhar_Click ( object sender,
RoutedEventArgs e)
{
DataTransferManager.ShowShareUI();
}
Comestecódigo-fonte,vocêjáestaráaptoacompartilharnasredessoci-
aiseemtodososoutrossharetargetsaosquaisseusmartphoneestáconec-
137
E-book gerado especialmente para 


## Página 144

8.4. ConhecendooShareContract CasadoCódigo
tado,comoporexemplo,Facebook,Twitter,OneNote,SMSetc.Infelizmente,
vocêprecisarádeumdispositivofísicoparatestarestafuncionalidadepor
completo,jáqueoemuladornãopossuiumacontaMicrosoftvinculadae,
porsuavez,nãohaveráautentica çãoemnenhumaredesocial. Entretanto,
vocêestaráaptoacompartilharasinforma çõesviaSMSeviaOneNotecon-
formeafigura8.9.
Figura8.9:Compartilhamentodeconteúdo
Vocêpodeconferirocódigoqueseencontraemmeugithubatravésdo
link:http://bit.ly/8-1GITcap8ParteIII.
138
E-book gerado especialmente para 


## Página 145

Capítulo9
Mapaselocaliza ção
Atéestemomentojácriamosdiversasfuncionalidadesemnossoaplicativo,
comoconsultadeprodutos,cria çãodecontasdeusuário,compartilhamento
informaçõesetc.Entretanto,vocêdeveterpercebidoque,apesardesetratar
de um aplicativo de compra, ainda não fizemos a funcionalidade para o
usuáriopoderefetuarsuacompra.
9.1 Criando a página para finalizar compra
Vamosvoltarànossapágina ProdutoDetalhe.xaml.Nela,ousuáriocon-
segueverificarasinforma çõesdetalhadasdeumdeterminadoproduto,bem
comocompartilharinforma çõesecriarumlivetileparaentrarnoaplicativo
diretonapáginadesteproduto.
Agoravamosadicionarumúltimobotãona CommandBardestapágina,
queseráutilizadoparainiciaroprocessodecompra.Comoofocodenossa
E-book gerado especialmente para 


## Página 146

9.1. Criandoapáginaparafinalizarcompra CasadoCódigo
aplicaçãoémeramentedidático,vamoslimitaracompraparaapenasumpro-
duto,eliminandotodaacria çãodefuncionalidadesparagerenciarumcar-
rinhodecompras.
Quando o usuário pressionar este botão, ele será direcionado para a
páginaondeiráinformaroendere çoparaentregadamercadoria,ejáfi-
nalizará a compra. Claro que, antes de direcionarmos o usuário para
estapágina,precisamosverificarseeleestáautenticadonoaplicativo,pois
usuáriosanônimosnãopodemrealizarcompras.
Jáimplementamosestetipodevalida çãoantes:bastaverificarmosseháa
configuração usuarioIdarmazenadaeseoIdéválido.Dependendodares-
oluçãodestacondi ção,vamosdirecionarousuárioparaapáginadefinalizar
comprasouparaapáginadeefetuarlogin,conformeocódigo:
private async void Comprar_Click ( object sender,
RoutedEventArgs e)
{
Windows.Storage.ApplicationDataContainer configuracoes =
Windows.Storage.ApplicationData.Current.LocalSettings;
if ( configuracoes.Values.ContainsKey( "usuarioId" ) &&
Convert.ToInt32(configuracoes.Values[ "usuarioId" ]) != 0 )
{
this .Frame.Navigate( typeof (FinalizarCompra));
}
else
{
await ExibirMensagem (
"Ops, desculpe, mas você não pode efetuar uma
compra sem estar autenticado no aplicativo. " );
this .Frame.Navigate( typeof (Entrar));
}
}
Percebaquenotrechodecódigoanteriornósestamosdirecionandoo
usuárioparaapágina FinalizarCompra.xaml. Estapáginaaindanão
existe,entãotemosdecriá-la.
140
E-book gerado especialmente para 


## Página 147

CasadoCódigo Capítulo9. Mapaselocalização
Elaserácriadanomesmodiretóriodasdemais. Alémdisso,vocêdeve
executaralgumasdastarefasquejáaprendeu,como,porexemplo,preparara
páginaparaabrirdeformaanimadaealteraro Backgroundparamantera
consistênciadainterfacedoaplicativo.
Estapáginadevepossuiroscampos: logradouroecidade,paraqueo
usuáriopossainformaroendere çodeentregae, parafinsdidáticos, adi-
cionaremosummapaquemostraráaposi çãoatualdousuárioeoendere ço
queeledigitar.Issoseráfeitoutilizandoocomponente Map.
Comojáfoiexplicadonocome çolivro, énecessárioinformarnoar-
quivo Package.appxmanifesttodasaspermissõesparaqueseuaplica-
tivopossautilizarfuncionalidadesdosistemaoperacional. Parapodermos
utilizaromapaeogerenciamentodelocaliza ção,precisamosativara Capa-
bilitie Location,ilustradapelafigura 9.1.
Figura9.1:Capabilitieparalocaliza ção
141
E-book gerado especialmente para 


## Página 148

9.1. Criandoapáginaparafinalizarcompra CasadoCódigo
Casovocênãohabiliteestecapabilitie,suaaplica çãoirádispararumaex-
ceçãodotipo Exceptioncomamensagemindicandofaltadepermissão
parautilizarorecurso.
Comelashabilitadas,podemosvoltarànossapáginaecome çaracriar
oscomponentes. Vamosprojetarolayoutbaseadoemum StackPanel,
envolvendotodososcomponentesdoconteúdodapágina. Nãoseesque ça
decircundarestepainelcomum ScrollViewerparaevitarproblemasde
navegação.
Aprimeirapartedacria çãoserábastantesimplesesimilaraoquejáfize-
mosatéagora:vamosempilharoscamposparaousuáriodigitarologradouro
eacidadee,depoisdestescampos,teremosobotão Adicionar Endereço,
conformeotrechoaseguir.
<ScrollViewer Grid.Row= "1" Margin= "10" >
<StackPanel>
<TextBlock FontSize= "{ThemeResource
TextStyleExtraLargeFontSize}" >
Logradouro
</TextBlock>
<TextBox x:Name= "Logradouro" />
<TextBlock FontSize= "{ThemeResource
TextStyleExtraLargeFontSize}" >
Cidade
</TextBlock>
<TextBox x:Name= "Cidade" />
<Button HorizontalAlignment= "Stretch" >
Adicionar Endereço
</Button>
</StackPanel>
</ScrollViewer>
Comisso,osprimeiroscomponentesdapáginajáforaminseridos.Agora
142
E-book gerado especialmente para 


## Página 149

CasadoCódigo Capítulo9. Mapaselocalização
utilizaremosalgunscomponentesumpoucodiferentesdoquefizemosaté
agora,masnãoseránadacomplicado. Apróximacoisaafazeréincluiro
namespaceparamapasemseuXAML.
xmlns:maps="using:Windows.UI.Xaml.Controls.Maps"
Feitoisso,podemosutilizarocomponente MapControlquefoicitado
anteriormente.Vamosincluirestemapadentrodopaineljáexistentee,além
disso,mesmoocomponente MapControljápossuindoumrecursodezoom
atravésdogestodepin ça, criaremosbotõesparafacilitaroaumentoea
diminuiçãodozoom.
<maps:MapControl x:Name= "Mapa" Height= "400" Grid.ColumnSpan= "2" >
<StackPanel Margin= "10" >
<Button Height= "90" FontSize= "32" > + </Button>
<Button Height= "90" FontSize= "32" > - </Button>
</StackPanel>
</maps:MapControl>
Paracompletarnossapáginateremosobotãoparafinalizaracompra.
<StackPanel>
...
<maps:MapControl x:Name= "Mapa" Height= "400"
Grid.ColumnSpan= "2" >
<StackPanel Margin= "10" >
<Button Height= "90" FontSize= "32" > + </Button>
<Button Height= "90" FontSize= "32" > - </Button>
</StackPanel>
</maps:MapControl>
<Button HorizontalAlignment= "Stretch" >
Finalizar Compra
</Button>
</StackPanel>
143
E-book gerado especialmente para 


## Página 150

9.2. EntendendoocomponenteMap CasadoCódigo
Com este layout definido, sua página deve estar bastante similar à
ilustradanafigura9.2.
Figura9.2:Páginaparafinalizarcompra
9.2 Entendendo o componente Map
Antesdeseguirmoscomaimplementa çãodenossapágina,éinteressante
quevocêconheçaalgumasdasfuncionalidadesecomportamentosdocom-
ponente MapControl.
144
E-book gerado especialmente para 


## Página 151

CasadoCódigo Capítulo9. Mapaselocalização
Estecomponenteébastantericoemtermosdefuncionalidades. Épos-
sívelincluirdiferentestiposdeconteúdoemummapaemumaplicativopara
WindowsPhone.Noprópriomapanativamentejáexistemosnomesdasruas
ealgunsíconesdelocaisimportantes,comoporexemplometrôs,conforme
ilustraafigura9.3.
Figura9.3:Locaisnomapa
Vocêtambémpodealteraroesquemadecoresdomapaatravésdapro-
priedade ColorScheme.Elapossuidoisvalorespossíveis, Darke Light
(padrão).Afigura 9.4mostraisso.
145
E-book gerado especialmente para 


## Página 152

9.2. EntendendoocomponenteMap CasadoCódigo
Figura9.4:Locaisnomapa
Alémdisso, tambémháopçõesparaquepossamosvisualizarascon-
struçõesimportantesemumavisãotridimensionalcomlegendas, indica-
tivosparapedestres,comoporexemplopassarelasouescadasefluxodotrá-
fico.Essasfuncionalidadespodemserativadasalterandoovalorpara true
daspropriedades LandmarksVisible, PedestrianFeaturesVisible
e TrafficFlowVisiblerespectivamente.Afigura9.5ilustratodasasfun-
cionalidadesativassimultaneamente.
146
E-book gerado especialmente para 


## Página 153

CasadoCódigo Capítulo9. Mapaselocalização
Figura9.5:Funcionalidadesativasnomapa
Tambémépossíveladicionarelementosnomapaemtempodeexecu ção,
devidoaoconceitodecamadasqueexistenocomponente MapControl.
A visualização do componente MapControl pode ser considerada
umasomatóriadediferentescamadas,cadaumacomumaresponsabilidade
própriaparaexibi çãodeconteúdos. Acamadamaisinferioréresponsável
porsubstituirobackgroundcasosuaaplica çãoprecisealteraristo.Acamada
sobreestaéobackgroundpadrão,queseencarregadeexibirosterrenoseos
mares.Porpadrãotodacamadapossuiumasobrecamadaparacustomiza ção,
então,acimadobackgroundháasobrecamadadebackground.
Apósestastrês,temosacamadadeáreas,queéresponsávelporexibir
informaçõessobreindústrias,parques,elocaisimportantes,eacimadela(e
desuasobrecamada)háacamadaqueexibeasrodovias.Depoisdelas,existe
aindaacamadaquemostraostextosdeidentifica ção,paradarmaissentido
147
E-book gerado especialmente para 


## Página 154

9.3. Finalizandonossoaplicativo CasadoCódigo
àsdemaiscamadas.
Porfim,temosacamadadoselementosquesãoadicionadosviaprogra-
maçãoedoselementosadicionadosviaXAML.Afigura 9.6exibetodasem
ordem.
Figura9.6:Camadasdomapa
Agorairemosfinalizarnossoaplicativoadicionandoitensnacamadade
elementosdomapa.
9.3 Finalizando nosso aplicativo
Vamoscriarummétodoemnossapágina FinalizarCompra.xaml.cs
para marcar uma posição no mapa. Este método deverá receber por
parâmetro dois valores: a posição na qual o objeto deve ser marcado (
Geopoint)eotextoqueseráexibidosobreoobjetonomapa.Vejaocódigo:
private void MarcarPosicaoNoMapa
(Geopoint posicao, string texto)
{
MapIcon marcacao = new MapIcon();
marcacao.Title = texto;
marcacao.Location = posicao;
Mapa.MapElements.Add(marcacao);
}
148
E-book gerado especialmente para 


## Página 155

CasadoCódigo Capítulo9. Mapaselocalização
Vejaquenessecódigoutilizamosacamada MapElementsparaadicion-
armosonosso MapIcon.Agoracriaremosométodoparaalterarozoomdo
mapa.Eleseráutilizadonoevento Tappeddosbotões“+”e“-”.Estemétodo
ébemsimples:bastaacumularumvaloraozoomatualdomapaevalidarseo
valoracumuladonãoultrapassaoslimitesdezoomdomapa(1-20),conforme
ocódigo:
private void AlterarAcumulativoZoom ( double zoomLevel)
{
double zoomLevelLimite = Mapa.ZoomLevel + zoomLevel;
if (zoomLevel > 0 )
zoomLevelLimite = Math.Min( 20 , zoomLevelLimite);
else
zoomLevelLimite = Math.Max( 1 , zoomLevelLimite);
Mapa.ZoomLevel = zoomLevelLimite;
}
Notequesempreestamossomandoovaloraozoomatualeissofun-
cionarátantoparaoaumentoquantoparaadiminui çãodozoom—para
fazerisso,bastainformarumnúmeronegativonasoma.Agoravamosfazer
comqueosbotõesdeauxíliodomapafuncionem.Paraisso,vocêdevecriar
ummétodomanipuladordoevento Tappedparacadaumdelesefazeruma
chamadaaestemétodoinformandooaumentoouadiminui çãoqueseráapli-
cada.
private void AumentarZoom_Tapped
( object sender, TappedRoutedEventArgs e)
{
AlterarAcumulativoZoom( 3 );
}
private void DiminuirZoom_Tapped
( object sender, TappedRoutedEventArgs e)
{
AlterarAcumulativoZoom(- 3 );
}
149
E-book gerado especialmente para 


## Página 156

9.3. Finalizandonossoaplicativo CasadoCódigo
Primeiro vamos implementar a função para obter a localização do
usuário,utilizandoumobjetodotipo Geolocator.Esteobjetonospermite
buscaraposi çãodousuárioemcoordenadas,ouseja,latitudeelongitude.
A precisão desta busca varia de acordo com a propriedade
DesiredAccuracy. Ele poderá buscar a posição do usuário através
demétodosdiferentes, comoIPoutriangula çãodeantenas. Paranosso
exemplo,vamosdeixarovalor Default.
O método para obtermos a localiza ção se chama
GetGeopositionAsync. Como já foi dito, por convenção os méto-
dosassíncronosutilizamosufixo Async,logoesteéummétodoassíncrono.
Depoisdeobteraposi çãogeográfica,vamosutilizarométodoparacriaruma
marcaçãonomapa—masnãoseesque çadecircundartudoissocomuma
cláusulatry-catch,poisousuáriopodeestarcomorecursodelocaliza ção
desligadoemseudispositivo.Ocódigoaseguirilustraestemétodo:
private async void ObterPosicaoAtual ()
{
Geolocator localizador = new Geolocator();
localizador.DesiredAccuracy = PositionAccuracy.Default;
try
{
Geoposition posicaoAtual =
await localizador.GetGeopositionAsync();
BasicGeoposition posicao =
new BasicGeoposition ();
posicao.Latitude =
posicaoAtual.Coordinate
.Point
.Position.Latitude;
posicao.Longitude =
posicaoAtual.Coordinate
.Point
.Position.Longitude;
150
E-book gerado especialmente para 


## Página 157

CasadoCódigo Capítulo9. Mapaselocalização
Geopoint posicaoEspacial = new Geopoint(posicao);
MarcarPosicaoNoMapa(posicaoEspacial, "VOCÊ" );
Mapa.Center = posicaoEspacial;
Mapa.ZoomLevel = 15.5 ;
localizacaoUsuario = posicaoEspacial;
}
catch
{
MessageDialog dialogo =
new MessageDialog ( "Não foi possível encontrar sua
localização.Por favor, verifique se suas configurações de
localização estão habilitadas. ");
dialogo.ShowAsync();
}
}
Notequeocódigotambémcentralizaomapa,aplicaozoomemtornoda
posiçãoatualdousuárioeguardaalocaliza çãodousuárioemumatributoda
classeiremosutilizá-lomaistarde.Agoradevemosfazerumachamadadeste
métodonométodo OnNavigatedTodestapágina.
Vamosimplementarobotão Adicionar Endereço paraqueelecrie
umpontoidentificandonomapaoendere çoqueousuáriodigitar.Paraex-
ecutarmosapesquisa,utilizaremosoobjeto GeocodeQuery,quebuscapor
localizaçõesutilizandotermosdelinguagemnatural,conformeocódigo:
private async void BuscarPorEndereco
( string logradouro, string cidade)
{
MapLocationFinderResult resultado =
await MapLocationFinder
.FindLocationsAsync(
string .Concat(logradouro, ", " ,cidade),
localizacaoUsuario, 1 );
foreach (MapLocation local in resultado.Locations)
151
E-book gerado especialmente para 


## Página 158

9.3. Finalizandonossoaplicativo CasadoCódigo
MarcarPosicaoNoMapa(local.Point, "ENDEREÇO BUSCADO" );
Logradouro.Text = string .Empty;
Cidade.Text = string .Empty;
}
Agorabastaquevocêadicioneummanipuladoraoevento Tappedno
botãoefa çaumachamadaparaométodo BuscarPorEndereco,passando
porparâmetroostextosdoscomponentesdapágina,comoilustraafigura
9.7.
Figura9.7:Endere çoadicionado
Porfim,vamosfazeraúltimafuncionalidadedenossoaplicativo:exibir
umamensagemquandoousuáriopressionarobotãoparafinalizarumacom-
152
E-book gerado especialmente para 


## Página 159

CasadoCódigo Capítulo9. Mapaselocalização
pra.
private async void FinalizarCompra_Tapped
( object sender, TappedRoutedEventArgs e)
{
MessageDialog dialogo =
new MessageDialog ( "Compra efetuada com sucesso!" );
await dialogo.ShowAsync();
this .Frame.GoBack();
}
Ocódigocompletodoaplicativoquedesenvolvemosaolongodestelivro
seencontraemmeugithubnolink: http://bit.ly/8-1GITversaoFinal.
153
E-book gerado especialmente para 


## Página 160

E-book gerado especialmente para 


## Página 161

Capítulo10
Dicasparapublica çãonalojado
WindowsPhone
Apóscompletarseuaplicativo,vocêpoderápublicá-lonalojadoWindows
Phone! Esteúltimocapítuloédedicadoaexplicarbrevementequaispassos
vocêdeveexecutarparaqueestapublica çãosejafeitaealgumasdicasesug-
estõesarespeitodisso.
10.1 Passos para publicação
Oprimeiropassoparaquevocêefetuesuapublica çãoéterumacontaMi-
crosoftecadastrá-lacomoumacontadedesenvolvedor.Énecessárioefetuar
umpagamentoanual,entãocrieumacontasomentequandoestivercertode
queirápublicaralgumaplicativo.
E-book gerado especialmente para 


## Página 162

10.2. Conclusão CasadoCódigo
Osegundopassoévocêvalidarseoconteúdodesuaaplica çãoéaceito
pelaspolíticasdaMicrosoft,ouseja,seuaplicativonãopodeconterlogos
ounomesdeterceiros,nenhumconteúdoofensivo,apologiaaalgumcrime
(sobalegisla çãodopaísqueoaplicativoestásubmetido)eváriosoutros
problemasdeconteúdo. Vocêpodeverificaralistacompletanolink: http:
//bit.ly/WPvalidacaoConteudo.
Vocêtambémterádevalidartodososaspectostécnicosdeseuaplicativo.
Todasasregraspodemserencontradasnestelink: http://bit.ly/WPregras.
Oterceiropassoépromoverseuaplicativodaformacorreta:dêumtítulo
queencaixecomsuafuncionalidadeequesejachamativo,utilizeacatego-
rizaçãodosaplicativosnalojaparaqueelesejaencontradocomfacilidade,
dêaspalavras-chavesmaisimportantesparaseuaplicativoefa çausodeuma
versãogratuitaparatestes.Issoauxiliaráapromoverseuapp.
Oquartopassoévocêpensarcomcuidadoaformadereceberretorno
financeiro.Escolhaentrepropagandas,aplicativospagosoucomprasdefun-
cionalidadesdentrodoaplicativo.Sempretenhaemmenteopúblicoquevocê
queratingiresefoquenisso.
Talvezoquintopassosejapensaremseuaplicativoparaaplafatorma
Windows,afinal,vocêdesenvolveuumaplicativocompletosobreaWindows
Runtime, ocompartilhamentodecódigoserábastantegrande, tentetirar
proveitodisto.
Por fim, submeta seu aplicativo na loja do Windows Phone (https://
dev.windowsphone.com)efa çacorreçõestantoparaqueseuaplicativoseja
aprovadonalojaquantoparatornaraexperiênciadousuáriocadavezmel-
hor.
10.2 Conclusão
Neste livro, você passou pelas principais funcionalidades introdutórias
necessáriasparasecriarumaplicativoparaWindowsPhonebaseadonaWin-
dowsRuntime,focandosemprenadidáticaetentandotrazeressasfuncional-
idadesdaformamaissimplespossível.
Nestepontovocêjádeveestaraptoacriarseusaplicativossozinho,uti-
lizandoprocessamentosassíncronos,vínculodedados,umaboalivetilee
156
E-book gerado especialmente para 


## Página 163

CasadoCódigo Capítulo10. DicasparapublicaçãonalojadoWindowsPhone
tudomais. Éimportanteressaltarqueváriospadrõesarquiteturaisdeapli-
caçãoforamignoradoscomoobjetivodefazercomqueoleitorseconcentre
apenasnoconteúdoprincipalabordado.
Esperoqueestelivrosejaapenasumgatilhoparasuabuscaporconhec-
imentoparaaplicativosparaWindowsPhone.Estematerialpossuiumfoco
bastanteintrodutórioenãocobredeformanenhumatodasasáreaspossíveis
doWindowsPhone. Alémdisso,nãoseprendaaumaúnicaplataforma,é
umaboadicavocêconheceromáximodeplataformasqueconseguir.
Odesenvolvimentodeaplica çãoparaWindowsPhoneébastantepráticoe
divertido.Acreditoqueunirdesenvolvimentocomtodasasno çõesdeexper-
iênciadeusuáriosejaumtrabalhobastantericoeproveitosoparaumdesen-
volvedor. Busquetambémporfuncionalidadesecódigosnãomencionados
nestelivro,comoaabordagemdecompras in-app,processamentoemback-
ground,pushnotificationseváriasoutras.
Comoautor,eubusqueicompartilharmeuconhecimentodaformamais
didática,simpleseenxuta.Esperoqueestelivrosejaproveitosoparavocêe
que,apartirdeagora,vocêsetorneoficialmenteumdesenvolvedorparaa
plataformaWindowsPhone.
157
E-book gerado especialmente para 
