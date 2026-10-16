---json
{
  "id": "microsoft_kinect_criando_aplica__es_interativas_com_o_microsoft_kinect",
  "title": "Microsoft Kinect Criando aplicações interativas com o Microsoft Kinect",
  "categoria": "07-design-hardware",
  "subcategoria": "iot",
  "resumo": "**Arquivo Original:** `Microsoft Kinect Criando aplicações interativas com o Microsoft Kinect.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "aplica",
    "com",
    "criando",
    "design",
    "hardware",
    "interativas",
    "iot",
    "kinect"
  ],
  "perguntas_tipo": [
    "Como utilizar Microsoft Kinect Criando aplicações interativas com o Microsoft Kinect?",
    "Quais as boas praticas de iot?"
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
  "dono": "stack-iot",
  "prioridade": 2
}
---

# Microsoft Kinect Criando aplicações interativas com o Microsoft Kinect

> **Arquivo Original:** `Microsoft Kinect Criando aplicações interativas com o Microsoft Kinect.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográficos,
eletrônicos, mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 3

CasadoCódigo Sumário
Sumário
1 IntroduçãoàInterfacesNaturais 1
1.1 ApresentandooKinect . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Oquevocêencontraránestelivro . . . . . . . . . . . . . . . . . . . . . 5
1.3 Antesdecome çar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 Primeiraaplicaçãocomosensor 7
2.1 CriandooprojetoAuxiliarKinect . . . . . . . . . . . . . . . . . . . . . 9
2.2 Criandoaregradenossaaplicaç ão . . . . . . . . . . . . . . . . . . . . 11
2.3 Testandoedepurandonossaaplicaç ão . . . . . . . . . . . . . . . . . . 14
2.4 Continuando . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3 AcelerômetroeEixoMotorizado 17
3.1 Acelerômetro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.2 EixoMotorizado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4 FluxodeCores 27
4.1 Formatos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.2 Aplicação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.3 Refatoração . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
5 FluxodeProfundidade 49
5.1 Formatos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
5.2 Entendendoumpoucomaissobreaprofundidade . . . . . . . . . . . 50
5.3 Aplicação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
i

## Página 4

Sumário CasadoCódigo
6 FluxodeEsqueletodoUsuário 63
6.1 EsqueletodoUsuário . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
6.2 DesenhandooEsqueletodoUsuário . . . . . . . . . . . . . . . . . . . 66
7 RastreandoeIdentificandoMovimentos 83
7.1 IniciandoaEstruturaBaseparaDetectarMovimentos . . . . . . . . . 84
7.2 UtilizandoPosesemNossaAplicaç ão . . . . . . . . . . . . . . . . . . . 89
7.3 FinalizandoaEstruturaBaseparaDetectarMovimentos . . . . . . . . 104
7.4 UtilizandoGestosemNossaAplicaç ão . . . . . . . . . . . . . . . . . . 116
8 Interagindocomaaplicaç ãoatravésdoKinectInteractions 119
8.1 PrincipaisConceitos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
8.2 MelhorandoNossaAplicaç ãocomosControlesdoKinectInteractions 121
8.3 UtilizandooFluxodeInteraç ão . . . . . . . . . . . . . . . . . . . . . . 127
9 UtilizandoosMicrofonesdoSensor 143
9.1 InicializandoaFontedeÁudioeDetectandoaDire çãodoSom . . . 144
9.2 DetectandoComandosdevoz . . . . . . . . . . . . . . . . . . . . . . . 149
9.3 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
ii

## Página 5

Capítulo1
IntroduçãoàInterfacesNaturais
Formasinovadorasdeinteraç ãocomousuáriotêmsidopropostasporinterfacesfo-
cadasaoparadigmadeinterfacenaturalaolongodosanos.Ossoftwaresemdiversas
áreasnãodevemexigirqueousuáriotenhagrandeconhecimentoemcomputaç ão
parausá-lo,devemsemprebuscarporsimplicidadeefacilidade.
AprimeirainterfacecomousuárioaaparecerfoiaCLI(CommandLineInter-
face)queutilizacomandosdeentradatextuaisespecíficasparadesempenharfun ções
emumaplicativo,algoqueexigiaumagrandecurvadeaprendizado.Algumtempo
depoissurgiuafamosaGUI(GraphicalUserInterface)queutilizajanelasgráficas,
mouse,botõesediversosoutroscomponentesvisuais,arriscodizerquegraç asàGUI
oscomputadoresconseguiramatingirtantaspessoasesepopularizartãorápido.
Hojeemdiaesteconceitoéomaisutilizadoemsistemasoperacionaiseaplicações.
Devidoàquantidadedeusuáriosedemandaporaplicaçõescadavezmaisintui-
tivasesimplessurgiuoconceitodeNUI(NaturalUserInterface)ousimplesmente
interfacesnaturais. Estetipodeinterfacefocaemutilizarumalinguagemnatural
paraainteraç ãohumanacomoaplicativo,comogestos,posesecomandosdevoz.

## Página 6

1.1. ApresentandooKinect CasadoCódigo
1.1 Apresentando o Kinect
Comopropostadeinterfacenaturalinicialmentefocadaparaaáreadejogos,aem-
presaMicrosoftemparceriacomaempresaisraelitaPrimeSenseconstruiuosensor
demovimentosquehojeéchamadodeKinect.OhardwaredoKinectteveboaparte
herdadopelohardwaredoPrimeSense. Nafigura 1.1podemosvisualizaro“irmão
maisvelho”doKinect.
Figura1.1:SensordaPrimeSense
OKinectcertamentecausouumarevoluç ãonaáreadeinteraçõescomjogos,
poisapartirdeagora,nãoémaisnecessárioutilizarumcontrole: osensorcapta
movimentosecomandosdevozdousuário,abrindoumlequedepossibilidadesto-
talmentenovo,utilizandoalinguagemnaturalparaainteraç ãocomosjogos.
InicialmenteosensorKinecteraconhecidopelocodinomeProjetoNatal,fa-
zendoreferênciaàcidadebrasileiraNatal,issoocorreudevidoaofatodequeum
dosidealizadoresdoprojetofoiumbrasileirochamadoAlexKipman.
Afigura1.2exibeosensorconcebidopelaMicrosoft,podemosnotarque,apesar
deumdesignmaiseleganteerobustoelepossuigrandessemelhan çascomoPrime-
Sense.
2

## Página 7

CasadoCódigo Capítulo1. IntroduçãoàInterfacesNaturais
Figura1.2:MicrosoftKinect
Emfevereirode2011,quatromesesapósosensortersidolan çadonoBrasil,a
Microsoftanunciavaolan çamentooficialdeumSDK(softwaredevelopmentkit)
quepodeserobtidodeformagratuita.ComestekitdedesenvolvimentoaMicro-
softpermitequedesenvolvedorespossamcriaraplicativosparacomputadoresnas
linguagensC++,C# eVisualBasicutilizandoohardwareKinect,ouseja,alimita-
çãodequeoKinecteraumdispositivoapenasparaaáreadejogosnãoeramais
verdadeira.
AtualmenteexistemtrêstiposdiferentesdeKinect,iremosdiferenciá-lospelos
seguintesnomes: Kinect,KinectforWindows eKinectforXbox360. Osensor
conhecidocomercialmentecomoKinectforWindowspossuiumhardwarediferen-
ciado,seusmicrofonespossuemumamelhorqualidadeeeleécapazderastrearo
usuáriomaispróximoaosensorouquandoeleestiversentado. Explicaremosme-
lhorsobreissoaodecorrerdolivro.
Adiferen çamaisimportantequevocêdeveteremmenteagoraéentreoKinect
forXbox360eosoutros.Estadiferen çatrata-sedocabodeconexãodosensor,esta
versãoévendidasomentejuntocomumconsoleXbox360eseucabodeconexão
possuiumaentradaespecífica,casoseusensorsejadestetipoénecessáriocomprar
umadaptadorparaconectaroKinectemumcomputador,afigura 1.3ilustraocabo
eoadaptadorparaestetipodesensor.
3

## Página 8

1.1. ApresentandooKinect CasadoCódigo
Figura1.3:KinectforXbox360eseuadaptador
Osensorpossuiumhardwarequeoferecediversosrecursosqueiremosexplorar
aolongodolivro,osprincipaissão:Emissordeluzinfravermelho,sensorRGB,sen-
sorinfravermelho,eixomotorizadoeumconjuntodemicrofonesdispostosaolongo
dosensor.Afigura 1.4apresentaumavisãodointeriordosensorcomindicativosde
ondeestãolocalizadosestesrecursos.
4

## Página 9

CasadoCódigo Capítulo1. IntroduçãoàInterfacesNaturais
Figura1.4:Kinectpordentro
1.2 O que você encontrará neste livro
Estelivroéescritoparadesenvolvedoresquejápossuemconhecimentoreferente
aosprincipaisconceitosrelacionadosàorientaç ãoaobjetosequejátiveramcon-
tatocomàlinguagemC#,parafacilitaracompreensãodedesenvolvedoresmenos
experiêntesnessalinguagemserádadopequenasexplicaçõessobrealgunsconcei-
tosdalinguagem. Noscapítulosiniciaisiremosdesenvolveraplicaçõesdetestes
eapartirdocapítulo4iremosconstruirumaaplicaç ãoatéofimdolivro. Estas
implementaçõesserãofocadasemconceitosdeinterfacesnaturaisespecíficosutili-
zandoumsensorKinect. Asaplicaçõescriadasnestelivronãoirãolevaremcon-
sideraçãopadrõesarquiteturaisemelhoriasdeperformance,serálevadoemcon-
sideraçãoaclarezaefacilidadedeentendimentodoleitoretodasasimplementa-
çõesterãoseucódigocentralizadonorepositório: https://github.com/gabrielschade/
CrieAplicacoesInterativascomoMicrosoftKinect.
Aolongodestelivronoscapítulosmaisavan çadosiremosconstruirumaaplica-
çãoutilizandotodososconceitoserecursosestudados,nofimdolivroteremosuma
aplicaçãocompletautilizandooKinect.
Agrandemetadestelivroéencorajareiniciaroleitoraingressarnestemundo
desafiador(emuitodivertido!)daprogramaç ãoseguindoosconceitosdeNUIatra-
vésdosensorKinect,oqueinvariavelmenteiráenvolverbastanteteoriaeprática,de
5

## Página 10

1.3. Antesdecomeçar CasadoCódigo
umaformafluída,simplesedivertida!
1.3 Antes de começar
Antes de começarmos a falar da nossa primeira aplicação, é necessário que
você tenha feito o download do SDK, ele é gratuito e pode ser baixado
através deste link:http://www.microsoft.com/en-us/kinectforwindows/develop/
developer-downloads.aspx. AlémdaultimaversãodoSDK,tambéméaconselhá-
veljáfazerodownloaddo developer toolkitedo Microsoft Speech Platform SDKpara
utilizarmosemnossasfuturasimplementações.
Nestelivroutilizaremoso VisualStudio2012 comoIDEdedesenvolvimento,
casovocêaindanãopossuaestaferramenta,existeumaversãogratuitaquepode
serbaixadaatravésdolink: http://www.microsoft.com/visualstudio/eng/products/
visual-studio-express-products.
ÉimportantelembrarquecasovocêpossuaumKinectforXbox360épreciso
quevocêtenhaumadaptadorparaconectá-loaoseucomputador.
6

## Página 11

Capítulo2
Primeiraaplicaçãocomosensor
Nestecapítuloaprenderemosacodificaretestarumaaplicaç ãoqueutilizeosensor
Kinect. Estaaplicaçãoserábastantesimpleseteráointuitodetermosoprimeiro
contatocomestetipodeprogramaç ão.Elaterácomofun çãoreconhecerseousuário
estácomamãodireitaacimadaalturadesuacabe çaenotificarousuárioexibindo
umamensagememumdiálogoquandoissoacontecer,simplesnão?
Aprimeiracoisaquetemosquefazerécriarnossoprojetodotipo WPF Appli-
cationnoVisualStudioeadicionarareferênciaparaoSDKdoKinect.

## Página 12

CasadoCódigo
WPFA pplications
Windows Presentation FoundationousimplesmenteWPFéumtipo
deprojetopropostonoVisualStudioparaaplicaçõesdesktopparaWin-
dows,apesardoKinectnãoselimitaraaplicaçõesWPF,existemdiver-
sasferramentasinclusasnoSDKquenosauxiliamnestetipodeprojeto.
ParasabermaissobreWPFacesse: http://msdn.microsoft.com/pt-br/
/library/ms754130.aspx
ParaadicionarareferênciaparaoSDKdoKinectbastapressionarobotãodireito
domousesobreoseuprojetoeselecionaraop ção“Add Reference...”. Seráaberta
umajanelaparaselecionaroassemblyquedesejaadicionaremseuprojeto,pesquise
pelapalavraKinect,selecioneoassemblyMicrosoft.KinectepressioneobotãoOK,
conformeilustraafigura 2.1.Comissonossoprojetojáestápreparadoparaaimple-
mentação,vamoscodificar!
Figura2.1:AdicionandoreferênciaaoassemblyMicrosoft.Kinect
8

## Página 13

CasadoCódigo Capítulo2. Primeiraaplicaçãocomosensor
2.1 Criando o projeto AuxiliarKinect
Antesdaimplementaçãodequalquerregraénecessárioimplementaroprocessode
configuraçãodosensorKinectqueestáconectadoaocomputador,nãoiremostra-
taragoracenáriosdeexce ção,entãoparaqueumasituaç ãoinesperadanãoocorra
emsuaaplicaç ão,tenhacertezaqueseuKinectestádevidamenteconectadoaoseu
computadoreàenergia.
Parafacilitaraconfiguraç ãodosensorparaaspróximasaplicaçõesiremoscriar
umprojetoseparadoparanosauxiliaremalgumastarefascomunsdoKinect.Para
fazerissoabraumanovainstânciadoVisualStudioecrieumprojetodotipo Class
Library. EsteprojetoirágerarnossaDLLqueconterádiversasfun çõesdoKinect,
vamoschamá-lodeAuxiliarKinect.
Comodescrevemosanteriormentenesteprojetotambéménecessárioareferên-
ciaparaoSDKdoKinect.Notequenoprojetojáexisteumaclassechamada Class1,
iremosexcluí-la. Pressioneobotãodireitosobreoprojetoecrieumanovapasta
chamada FuncoesBasicas.
Antesdecome çarmosaimplementaréimportanteteremmentequenãoexiste
limitaçãonoquedizrespeitoàquantidadedesensoresconectadosemseucompu-
tadorsimultaneamente.Épossívelidentificarosdiferentessensoresporumidenti-
ficadorúnicoquecadasensorpossui,masnestelivroiremosfocarnocenáriomais
comum,ondeasaplicaçõesutilizamapenasumsensor.
Pensandonestecenário,aMicrosoftcriounaclasse KinectSensoraproprie-
dadechamada KinectSensors. Estapropriedadeéumacole çãodeobjetosdotipo
KinectSensor,ouseja,todosossensoresconectadosnocomputadorserãolistados
nestacole ção.Tendoconhecimentodestapropriedadeesabendoquepossaexistir
maisdeumsensor,éfácilperceberqueénecessáriofazerumabuscaparaidentificar
quantossensoresestãoconectadosnocomputador.Estecódigopodeserescritode
maneiramuitosimplesatravésdeumaexpressãolambda.
9

## Página 14

2.1. CriandooprojetoAuxiliarKinect CasadoCódigo
ExpressõesLambdas
Expressãolambdaéumrecursomuitopoderosodisponívelnalin-
guagemC#,trata-sedeumanotaç ãoparaescritadefun çõesanônimas
quepodemrealizarasmaisdiversastarefas,comosuporteparaalingua-
gemdeconsultaLINQeescritasimplificadademétodosrecursivos,por
exemplo.Paramaisinformaçõessobreexpressõeslambdaacesseolink:
http://msdn.microsoft.com/pt-br/library/vstudio/bb397687.aspx
Sabendoqueutilizaremosapenasumsensornaaplicaç ãopodemosfazeruma
buscanacole çãodesensoresparaobtermosoprimeiroKinectconectadoaocom-
putador(quenestecasosempreseráoúnico). Apósencontrarosensorépreciso
inicializá-loatravésdométodo Startdaclasse KinectSensor.Feitoainiciali-
zaçãoiremosfor çaroKinectamanteroeixomotorizadodosensordeacordocom
umainformaçãoparametrizada. Éimportantesaberque,paraalteraroângulodo
eixomotorizadodosensor,énecessárioinicializá-loantes,casocontrárioumaex-
ceçãoserádisparada.
Agora criaremos a classeInicializadorKinect dentro da pastaFun-
coesBasicas. Além de ter adicionado a referência ao assemblyMicrosoft.Kinect
adicione também a diretivausing para este mesmo assembly dentro da classe
InicializadorKinect. Setudoestivercorretovocêjápoderáacessaraclasse
KinectSensor,estaclasseédeextremaimportância,poiselaéarepresenta ção
virtualdosensorKinectemsuaaplicaç ão.
Aclasse InicializadorKinectdeveserpúblicaparapodermosacessá-laem
nossaaplicação,portantonãoesque çadeutilizarapalavrareservada publicnade-
claraçãodaclasse.Vamoscriarummétodoestáticoparafazerasoperaçõesdescritas
anteriormente(inicializarosensoreconfigurarseuângulodeelevaç ão).Nossomé-
todosechamará InicializarPrimeiroSensoreleiráreceberporparâmetroo
ângulodeelevaçãoinicialdosensoredeveráretornaroprimeirosensorconectado
nocomputador.
public static KinectSensor
InicializarPrimeiroSensor(int anguloElevacaoInicial)
{
KinectSensor kinect =
KinectSensor.KinectSensors.First(sensor =>
10

## Página 15

CasadoCódigo Capítulo2. Primeiraaplicaçãocomosensor
sensor.Status == KinectStatus.Connected );
kinect.Start();
kinect.ElevationAngle = anguloElevacaoInicial;
return kinect;
}
Notoucomofoisimples?Apenascomalgumaslinhasdecódigopodemosobter
onossosensor,iniciaroseuprocessamentoealteraraangulaç ãodoeixomotorizado.
Agoravocêdevecolocarumachamadaparaestemétodoemnossaaplicaç ão.
ProcurepelaclasseMainWindow,apesardeelaserumajanelanãoiremosalte-
raremnadaapartevisual,entãosepreocupeapenascomoarquivoC# (MainWin-
dow.xaml.cs).Alémdeteradicionadoareferênciaaoassembly Microsoft.Kinectadi-
cionetambémareferênciaparaaDLLquecriamosnoprojeto AuxiliarKinect.
Lembre-setambémdeutilizaradiretiva usingparaestesmesmosassemblysdentro
daclasseMainWindow.
Nestaaplicação,alémdeinicializarmoscomaconfiguraç ãopadrãodoKinect
precisamoshabilitarorastreamentodeesqueleto,poiséistoqueiránospermitir
verificaraposiç ãoespacialdamãoedacabe çadousuário. Entãovamoscriarum
métodochamado InicializarKinectparafazerasoperaçõessupracitadas.
private void InicializarSensor()
{
KinectSensor kinect = InicializadorKinect
.InicializarPrimeiroSensor(10);
kinect.SkeletonStream.Enable();
}
ComnossaDLL,ficoumuitosimplesinicializarosensor!Agoranoconstrutor
daclasseapósachamadadométodo InitializeComponentquejáestápresente
porpadrãoemtodasasjanelas,crieumachamadaparaestemétodo.Depoisconecte
osensoraoseucomputadoreexecuteaaplicaç ão,viuoqueaconteceu?Aaplicaç ão
jáestáreconhecendoosensoreposicionandooângulodeelevaç ãodeseueixomo-
torizado!
2.2 Criando a regra de nossa aplicação
Paraarmazenaroresultadodacomparaç ãodealturaentreamãodireitadousuárioe
suacabe çairemoscriarapropriedade bool MaoDireitaAcimaCabeca.Jácon-
11

## Página 16

2.2. Criandoaregradenossaaplicaç ão CasadoCódigo
figuramososensorecriamosapropriedadequeiráarmazenaroresultadodenossa
regra,masaindanãoescrevemosocódigoque,defato,validaestaregraeexibea
mensagemparaousuário.Ondeestaregradeveserescrita?Antesderespondermos
precisamosentendermaisumconceitoenvolvidonaprogramaç ãocomoKinect.
Nãoiremosentraremmuitosdetalhesnestaprimeiraaplicaç ão,maséimpor-
tantesaberqueoKinectatualizaumconjuntodeinformaçõesemformadequadros
ou frames.Emsuaconfiguraç ãopadrão,acadasegundooKinectcria30quadros,e
cadaquadropossuiseuconjuntoprópriodeinformações.
Agoracriaremosométodoqueexecutanossaregra,parafazerestavalidaç ão
precisamosdasinformaçõesreferentesaoesqueletodousuário. Elasestãoencap-
suladasnaclasse SkeletonFrame,entãoométodoqueiráexecutararegradeve
receberumobjetodestetipoporparâmetro.
O rastreamento de esqueleto do usuário do Kinect pode identificar até
seis esqueletos simultâneos e todos estes esqueletos estão no objeto da classe
SkeletonFrame. Teremosqueextrairainformaç ãosobreosesqueletosdoqua-
droelogoemseguida,vamosbuscarpeloprimeiroesqueletodeusuárioqueoKi-
nectestejavisualizando—casoexistaalgum,faremosavalidaç ãoparanossaregra
eexibiremosamensagem. Ocódigoaseguirdescrevecomoestemétododeveser
escrito.
private void ExecutarRegraMaoDireitaAcimaDaCabeca
(SkeletonFrame quadroAtual)
{
Skeleton[] esqueletos = new Skeleton[6];
quadroAtual.CopySkeletonDataTo(esqueletos);
Skeleton usuario =
esqueletos.FirstOrDefault( esqueleto =>
esqueleto.TrackingState == SkeletonTrackingState.Tracked );
if (usuario != null)
{
Joint maoDireita = usuario.Joints[JointType.HandRight];
Joint cabeca = usuario.Joints[JointType.Head];
bool novoTesteMaoDireitaAcimaCabeca =
maoDireita.Position.Y > cabeca.Position.Y;
if ( MaoDireitaAcimaCabeca !=
novoTesteMaoDireitaAcimaCabeca)
12

## Página 17

CasadoCódigo Capítulo2. Primeiraaplicaçãocomosensor
{
MaoDireitaAcimaCabeca =
novoTesteMaoDireitaAcimaCabeca;
if (MaoDireitaAcimaCabeca)
MessageBox
.Show("A mão direita está acima da cabeça!");
}
}
}
Nocódigoanteriorcopiamostodasasinformaçõesdosesqueletosdeusuário
paraumarray,depoisverificamosseexistealgumesqueletoquepossuaoestado
tracked(rastreado),casoexistaexecutamosnossaregraparaesteesqueleto.
Agoraprecisamosinserirumachamadaaestemétodoemalgumlugardanossa
aplicação,ondedevemosfazerisso?
Cada vez que o Kinect processa as informações a respeito do esqueleto
de todos os usuários e gera um novo quadro, a classeKinectSensor dis-
para um evento que teremos que interpretar. Neste evento é fornecido um
objeto do tipo SkeletonFrameReadyEventArgs. Este objeto possui di-
versas propriedades e entre eles está o objetoSkeletonFrame que deve-
mos enviar para nosso método criado anteriormente. Portanto, no método
que interpreta este evento é que devemos fazer uma chamada para o método
ExecutarRegraMaoDireitaAcimaDaCabeca!
A primeira alteração em nosso código é inserir a linha de có-
digo kinect.SkeletonFrameReady += KinectEvent; no método
InicializarSensor() entre a inicialização do rastreamento de esqueleto e
a inicialização do sensor. Você pode utilizar o Visual Studio para autogerar o
métodoqueinterpretaoevento. Aúnicaresponsabilidadedestemétodoéabriro
novoquadroqueoKinectestáenviandoechamarnossométododeregra,conforme
códigoaseguir.
private void KinectEvent(object sender, SkeletonFrameReadyEventArgs e)
{
using (SkeletonFrame quadroAtual = e.OpenSkeletonFrame())
{
if (quadroAtual != null)
{
ExecutarRegraMaoDireitaAcimaDaCabeca(quadroAtual);
13

## Página 18

2.3. Testandoedepurandonossaaplicação CasadoCódigo
}
}
}
Vocêpodenotarquenocódigoanteriorverificamosseoquadroatualestánulo.
Issoocorrequandonãoháinformaçõessobreonovoquadro,ouseja,nãohánenhum
usuárioemfrenteaosensor.
Executesuaaplicaç ãoevejaoresultado! Agoraoficialmentetemosaprimeira
aplicaçãoutilizandoosensorKinecteseurastreamentodeesqueleto,nãoélegal?
Figura2.2:Aplicaçãosendoexecutada
2.3 Testando e depurando nossa aplicação
Vocênãoterámuitasdificuldadesemtestarestaaplicaç ão,bastaposicionar-seem
frenteaosensorelevantarobraçoatéquesuamãodireitaestejaacimadesuaca-
beça,massemutilizaraferramentacertavocêpodeterumproblemacom depura-
ção.Comofazeradepuraç ãodanossaaplicaç ãodeformasimples,semprecisarnos
levantarmosdacadeiraefazertodososgestosquegostaríamosdetestaracadanovo
14

## Página 19

CasadoCódigo Capítulo2. Primeiraaplicaçãocomosensor
teste?
ArespostaparaesteproblemafoiinstaladaemseucomputadorjuntocomoSDK
indicadonocome çodestelivro,elachama-se KinectStudio. AaplicaçãoKinect
Studionospermitegravaraçõesparaexecutaremumteste,sendoassim,podemos
gravaromovimentoapenasumavezetestá-loquantasvezesfornecessário.
Apósexecutarsuaaplicaç ãoexecuteoKinectStudioenotequeseráexibidauma
janela. Estajaneladevecontersuaaplicaç ãolistada,casosuaaplicaç ãonãoesteja
sendoapresentada,certifique-sedequeelarealmenteestáemexecuç ãoepressione
obotão Refresh,apósterfeitoissoajanelamostradadeveseparecercomafigura 2.3.
Figura2.3:Conectandosuaaplicaç ãonoKinectStudio
Pressioneobotão Connecteasquatrojanelasqueestavamaofundosãomos-
tradas,nafigura 2.4astrêsjanelasinferioresrepresentamasvisõesdosensor. A
janela Color Viewernãoestáapresentandonenhumaimagemporquenãoativamos
acâmeradecoresdoKinectemnossaaplicaç ão.
Najanelasuperiorestãooscontrolescomosquaisvocêpodegravar,abrireexe-
cutararquivoscomaextensão .xed.Atravésdestaferramentavocêpodedaro play-
backdeseustestesgravadosfacilitando(emuito)adepuraç ãoeotestedesuasapli-
caçõescomoKinect,nãoireimaiscitarestaferramenta,masaconselhofortemente
utilizá-laaodecorrerdolivro.
15

## Página 20

2.4. Continuando CasadoCódigo
Figura2.4:KinectStudio
2.4 Continuando
Comissovocêjátemumano çãobásicasobreoqueéosensorKinect,qualseuhard-
wareecomodesenvolveretestarumaaplicaç ãoqueutilizeseusrecursos.Apartir
destaetapaolivroirásepararasfuncionalidadesporcapítulosintercalandoentrea
explicaçãodohardwareedosoftwareenvolvidoemcadaumadestasfuncionalida-
deseaofinaldetudoiremosconstruirumaaplicaç ãoqueagregadiversosconceitos
queiremosver.
16

## Página 21

Capítulo3
AcelerômetroeEixoMotorizado
NestecapítuloiremosentendercomofuncionaoacelerômetrodoKinectequando
podemosnosbeneficiarcomesterecurso.Alémdisso,tambémseráexplicadosobre
ocampodevisãodosensoresobrecomopodemosadaptaroseufocoutilizando
orecursodisponívelnoSDKparamanipulaç ãodoeixomotorizado—oquetorna
estecomponente,apesarderelativamentesimples,muitoimportanteparaquemestá
pensandoemumaaplicaç ãoNUIcomoKinect.
3.1 Acelerômetro
Umacelerômetronadamaiséque,comoonomejásugere,umsensorparamedira
aceleraçãosobreumobjeto.OKinectpossuiumacelerômetrocapazdefazermedi-
dasnastrêsdimensões:X,YeZ.Alémdissoeleestáconfiguradoparasuportarum
intervalode2g,ondegéafor çaqueagravidadeimplicasobreosensor,issopermite
queestepequenosensorconsigainformarasuaorientaç ãoemrelaç ãoàgravidade.
Estesensordeaceleraç ãopossuiumasensibilidadeparatemperaturas,ovalorde
seuseixospodevariarematétrêsgrauspositivaounegativamente.Paracompensar

## Página 22

3.1. Acelerômetro CasadoCódigo
estedesvioénecessáriofazerumacomparaç ãoentreoeixoYdoacelerômetroeos
dadosdeprofundidade.
Ok,masemqueumacelerômetropodenosajudar? Bom,estaperguntapode
viracabe çanestemomento,maséimportantetermosemmentequeasaplicações
doKinectvãoalémdeumcomputadorounotebook,existemdiversosprojetosem
queoKinectéutilizadoemumtotemouemumdispositivoquesemove,ouseja,
ousodoacelerômetroseestendeportodososcasosemqueorientaç ãodosensoré
alterada.
EntendendooacelerômetronoSDK
As informações do acelerômetro no SDK são disponibilizadas atra-
vés de um método da já conhecida classeKinectSensor. O método
AccelerometerGetCurrentReading() retorna as informações sobre o
acelerômetroemumvetorde4posições(X,Y,ZeW)sendoqueWsempreteráo
valorzero.
Apesardeparecerestranhoemumprimeiromomentoquehajaaposiç ãoWno
retornodealgoquedeveriaestaremumsistemasdecoordenadasdetrêsdimensões,
faztotalsentidoseconhecermosoconceitodecoordenadashomogêneas.Trata-se
deumaideiabemsimplesepoderosa:basicamentevocêrepresentaascoordenadas
X,YeZemumaquádruplaordenada*[X,Y,ZeW] ondeX=X/W+1,Y=Y/W+1
eZ=Z/W+1.Estesistemapermiterepresentarproje çõesconhecidascomopontos
impróprios,quesãoutilizadospararepresentarofeixederetasparalelasaumoutro
eixo. Existemdiversasoutrasvantagensparaissoserutilizado,masnãocabeao
escopodestelivrodescrevertodas.
Osistemadecoordenadasdoacelerômetrodosensorestácentralizadocomo
dispositivo.Porpadrãooretornodestemétodo,casooKinectestejaemumasuper-
fícieplana,serápróximoa(x:0,y:-1.0,z:0ew:0).
Infelizmentenãoháumeventonativoparaquandoestasinformaçõessãoalte-
radas,énecessáriomonitorarmosmanualmente,maspodemoseiremoscriarum
sistemadeeventosparafazerisso.
Aplicação
Vamoscriarumaaplicaç ãoparamediroresultadodoacelerômetrodetempos
emtempos,serábemsimpleserápidoenosajudaráaperceberasvariaçõesque
ocorremquandomovimentamososensor(dependendodaquantidadedeprecisão
18

## Página 23

CasadoCódigo Capítulo3. AcelerômetroeEixoMotorizado
quevocêutilize,ocorrerãopequenasvariaçõesmesmocomodispositivoparado).
A primeira coisa a fazer é criar um novo projeto WPF no visual studio,
comojáfizemosnocapítulo 2. Ospassosparaconfigurarosensorserãomuito
simples, bastacriarumareferênciaparanossaDLLauxiliareutilizarométodo
InicializarPrimeiroSensordescritoem 2.1.Destaveznãoprecisamosativar
nenhumoutrorecursodoKinect,entãopoderemossimplesmenteutilizarométodo
jácriadonoconstrutordajanela,conformeocódigoaseguir.
public MainWindow()
{
InitializeComponent();
kinect = InicializadorKinect.InicializarPrimeiroSensor(0);
}
Você pode notar que não estamos declarando o objetoKinectSensor
kinectnoescopodoconstrutordajanela,vocêdevedeclará-lonoescopodaclasse,
poisiremosreutilizá-loemoutrométodo.Feitoisso,játemosnovamentenossaini-
cializaçãodosensor,agorairemoscriaroscomponentesdetelaparaexibirosvalores
doacelerômetronoseixosX,YeZ,ignoraremosoeixoW,poiscomocitadoacima
elesempreestaráem0(zero).
AocriarumnovoprojetoWPFoformuláriodeveestarapenascomumpainel
dotipo Grid,vamosutilizarestemesmopainelparaconstruirumlayoutemforma
detabelacujaprimeiracolunairálistaroseixoseasegunda,ovalordecadaum.
XAML
OsprojetosWPFutilizamoXAML (eXtensible Application Markup
Language)paraaconstruçãodainterface,estaéumalinguagemdemar-
caçãosimplesquepossuifocoemaplicaçõesdesktopcomumpapelsi-
milaraoHTMLeCSSparaaplicaçõesWeb.
Paraqueestajanelaocupeapenasoespaçonecessário,iremosdiminuiroseu
tamanho,paraissovamosalterarosvaloresdaspropriedades Widthe Height
paraosvalores300e150respectivamente. Comisso,ajanelaficoubempequena,
masésuficienteparamostrarmosessasinformações.
Feitoisso,jápodemosescolherotamanhodaslinhasecolunasparaexibiras
informações.ComojáditoantesiremosmostrarosvaloresdoseixosX,YeZ,por-
19

## Página 24

3.1. Acelerômetro CasadoCódigo
tantoprecisamosdetrêslinhasdomesmotamanho.Parafazerissovocêdevecriar
adefiniçãodaslinhas,conformeocódigoaseguir.
<Grid>
<Grid.RowDefinitions>
<RowDefinition Height="*"/>
<RowDefinition Height="*"/>
<RowDefinition Height="*"/>
</Grid.RowDefinitions>
</Grid>
Estaéasintaxeparaacriaç ãodasdefiniçõesdelinhas.Notequeapropriedade
Heightestácomovalor (*),estevalorindicaproporcionalidade,ouseja,todasas
linhasficarãocomomesmotamanho—casoumalinharecebaovalor (2*),elateria
odobrodotamanhodasoutras.
Agorairemosdefinirasduascolunas. Asintaxeémuitosimilar,masaoinvés
deutilizarmosapropriedade Heightqueindicaaltura,iremosutilizaraproprie-
dade Widthqueindicalargura.Alémdisso,ascolunasnãoirãopossuirosmesmos
valoresproporcionalmente,poisaprimeirairáexibirapenasumaletrareferenteao
seueixoeasegundairáreceberumnúmerocomdiversascasasdecimais.Otama-
nhodaprimeiracolunaseráfixoem50pixelsenquantoqueasegundairáocupar
todoorestantedajanela,ocódigoaseguirmostracomoatag Gridficouapósestas
definições.
<Grid>
<Grid.RowDefinitions>
<RowDefinition Height="*"/>
<RowDefinition Height="*"/>
<RowDefinition Height="*"/>
</Grid.RowDefinitions>
<Grid.ColumnDefinitions>
<ColumnDefinition Width="50"/>
<ColumnDefinition Width="*"/>
</Grid.ColumnDefinitions>
</Grid>
Nossaestruturadolayoutjáestápronta!Agoravamosincluiroscomponentes
paraexibirasinformações.Umcomponentesimpleseútilparaexibirinformações
éocampo Label.Teremos6camposdestetipoeiremosdefiniralgumaspropri-
edadesvisuaisparaeles. OstrêsprimeiroscamposdevemreceberosvaloresX,Y
20

## Página 25

CasadoCódigo Capítulo3. AcelerômetroeEixoMotorizado
eZnapropriedade Contenteostrêsúltimoscamposdevemreceberosvalores
labelX,labelYelabelZnapropriedade Nameparaqueelessetornemacessíveisno
codebehinddenossajanela.Precisamosdissoporquevamosatualizarovalordapro-
priedade ContentcomovalordoacelerômetroemnossocódigoC#,alémdisso,é
importanteutilizaraspropriedadesdealinhamentoeaspropriedadesherdadasdo
componente Gridparaposicionarainformaç ãoadequadamentenonossolayout.
Comtudoterminado,ocódigodestajaneladeveficarsemelhanteaocódigoaseguir.
<Window x:Class="Acelerometro.MainWindow"
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
Title="MainWindow" Height="150" Width="300">
<Grid>
<Grid.RowDefinitions>
<RowDefinition Height="*"/>
<RowDefinition Height="*"/>
<RowDefinition Height="*"/>
</Grid.RowDefinitions>
<Grid.ColumnDefinitions>
<ColumnDefinition Width="50"/>
<ColumnDefinition Width="*"/>
</Grid.ColumnDefinitions>
<Label Content="X" HorizontalAlignment="Center"
FontSize="24" VerticalAlignment="Center" />
<Label Content="Y" HorizontalAlignment="Center"
FontSize="24" VerticalAlignment="Center"
Grid.Row="1"/>
<Label Content="Z" HorizontalAlignment="Center"
FontSize="24" VerticalAlignment="Center"
Grid.Row="2"/>
<Label Name="labelX" HorizontalAlignment="Left"
FontSize="24" VerticalAlignment="Center"
Margin="10,0" Grid.Column="1" />
<Label Name="labelY" HorizontalAlignment="Left"
FontSize="24" VerticalAlignment="Center"
Margin="10,0" Grid.Column="1" Grid.Row="1"/>
21

## Página 26

3.1. Acelerômetro CasadoCódigo
<Label Name="labelZ" HorizontalAlignment="Left"
FontSize="24" VerticalAlignment="Center"
Margin="10,0" Grid.Column="1" Grid.Row="2"/>
</Grid>
</Window>
Agoranossajanelajáestápronta.Podemosimplementarocódigoqueiráatu-
alizarestescamposcomosvaloresdoacelerômetrodosensor.Parafazerissocria-
remosummétodochamado AtualizarValoresAcelerometro(),noqualire-
mosobterosvaloresatravésdométododisponívelnaSDKeinseri-losnaproprie-
dade ContentdoscomponenteslabelX,labelYelabelZ,conformeocódigoaseguir.
private void AtualizarValoresAcelerometro()
{
Vector4 resultado = kinect.AccelerometerGetCurrentReading();
labelX.Content = Math.Round(resultado.X, 3);
labelY.Content = Math.Round(resultado.Y, 3);
labelZ.Content = Math.Round(resultado.Z, 3);
}
Estaéaformadeobterosvaloresdoacelerômetro,bemsimplesnãoé?Agorate-
mosqueobservarumpontoimportante,quandoestemétodoseráexecutado?Con-
formeditoanteriormentenãoháeventosparaaatualizaç ãodoacelerômetro,poisele
sofrevariaçõesconstantemente,paraatualizarmosovaloriremoscriarnossopróprio
timer.
Oobjeto DispatcherTimerfuncionacomoumcronômetro:cadavezqueo
tempodefinidocomoseuintervalopassa,oevento Tickéchamado.Vamosinter-
pretaresteeventoedentrodelechamaremosométodocriadoanteriormente.Para
criarum timeremC# bastautilizaroobjetomencionado,preencherapropriedade
Intervalqueirádefinirointervalocomqueoevento Tickéchamadoeinvocar
ométodo Startparaqueo timerinicie.Vejacomoométododeinicializaç ãodo
timereométodoqueinterpretaoevento Tickficaramsimples.
private void InicializarTimer()
{
DispatcherTimer timer = new DispatcherTimer();
timer.Interval = TimeSpan.FromMilliseconds(100);
timer.Tick += timer_Tick;
timer.Start();
22

## Página 27

CasadoCódigo Capítulo3. AcelerômetroeEixoMotorizado
}
private void timer_Tick(object sender, EventArgs e)
{
AtualizarValoresAcelerometro();
}
Agorabastaqueoconstrutordenossajanelainvoqueosmétodosparainicializar
osensorKinecteo timerquetudoiráfuncionar. Executesuaaplicaç ãoevejaos
valoresdoacelerômetrosendoalteradosconformevocêmexenosensor.Afigura 3.1
ilustraajaneladanossaaplicaç ão.
Figura3.1:AplicaçãoAcelerômetro
3.2 EixoMotorizado
OEixomotorizadoéumape çaimportantenoKinect,atravésdeleépossívelalteraro
ângulodeelevaçãodocomponenteondeficamascâmerasdosensor,alterandoassim
avisãoqueosensorpossuidoambiente.Esteeixomovimentaosensorapenaspara
cimaeparabaixo,atualmentenãoháumaformademovimentá-lohorizontalmente.
OKinectpossuiumraiodevisãode57.5grausnahorizontale43.5grausnaver-
tical,contudoesteeixomotorizadopodemovimentaravisãoverticalpara27graus
paracimaouparabaixo,conformeilustradonafigura 3.2.
23

## Página 28

3.2. EixoMotorizado CasadoCódigo
Figura3.2:VisãodoKinect
AsinformaçõesligadasaoeixomotorizadosãodisponibilizadasnoSDKde
formabastantesimples.
Existem três propriedades na classeKinectSensor: ElevationAngle,
MaxElevationAnglee MinElevationAngle.Asduasúltimascitadaspossuem
ovalorfixode27e-27respectivamente.Apropriedade ElevationAnglepossui
ovalorigualaovalordaalturadoângulodeelevaç ãodoeixomotorizado. Nósjá
autilizamosnosexercíciosanterioresevocêviuoquantoésimplesalterarouobter
estevalor.
problema com o Elev ationAngle
Casoumasegundaalteraç ãonapropriedadeElevationAnglesejafeita
semqueaprimeiratenhasidofinalizadaélan çadaumaexce çãonaapli-
cação.
24

## Página 29

CasadoCódigo Capítulo3. AcelerômetroeEixoMotorizado
Aplicação
Construiremosoutraaplicaç ãoWPF,entãovocêdevefazerospassosjáconhe-
cidosparaacriaç ãodoprojeto,incluindoainclusãoechamadaparaainicializaç ão
dosensordescritaem 2.1. Nestaaplicaçãoiremosconstruirumcomponenteque
nospermitiráalterarovalordoângulodeelevaç ãodoeixomotorizadopelaprópria
interface!
Como na aplicação anterior também utilizaremos o componente de layout
Grid,dessavezprecisamosapenasdeduascolunas,sendoqueasegundairáocupar
odobrodeespaçodaprimeira.Parafazerisso,utilizeocaracteredepropor ção(*).
Naprimeiracolunadajanelainserimosumcomponente Slider,queiráseencar-
regardealterarapropriedade ElevationAngleenaoutracolunavamosinserir
umcomponente Labelparamostrarovalordoângulodeelevaç ãodoKinect.
Éimportantelembrarqueprecisamosinserircomovalormáximoemínimo
do Slider27e-27respectivamente,poisesteéovalorlimitedoângulodeele-
vação.Porop çãoireiinicializarapropriedade Valuedo Slidercomovalor0,
ouseja,comoKinectcentralizado.AtravésdoXAML,tambémpodemosinterpre-
taroseventosdoscomponentes:comoteremosqueatualizarovalordapropriedade
ElevationAngletodavezqueo Slidertiverseuvaloralterado,temosqueinter-
pretaroevento Thumb.DragCompleted,queseráchamadotodavezqueousuário
interagircomocomponente.
Tambémprecisamospreencherapropriedade Namedosdoiscomponentes,pois
iremosutilizá-losnocódigoC# dajanela.Apósasconfiguraçõesdelayoutfeitaso
códigodajaneladeveestarsemelhanteaocódigoaseguir.
<Window x:Class="EixoMotorizado.MainWindow"
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
Title="MainWindow" Height="230" Width="180">
<Grid>
<Grid.ColumnDefinitions>
<ColumnDefinition Width="*"/>
<ColumnDefinition Width="2*"/>
</Grid.ColumnDefinitions>
<Slider Name="slider" Margin="10,0" Height="150"
HorizontalAlignment="Left" VerticalAlignment="Center"
Orientation="Vertical" Minimum="-27" Maximum="27"
25

## Página 30

3.2. EixoMotorizado CasadoCódigo
Value="0" Grid.Column="0"
Thumb.DragCompleted="slider_DragCompleted"/>
<Label Name="label" FontSize="64"
FontFamily="Segoe UI Light"
HorizontalAlignment="Center" VerticalAlignment="Center"
Content="0" Grid.Column="1" />
</Grid>
</Window>
Tendoajanelapronta,podemospartirparaaimplementaç ãoemC# destaapli-
cação. Criaremosummétododentrodanossajanelaparaatualizarosvaloresda
propriedade ElevationAngledosensoredotextoexibidonolabel. Chamare-
mosestemétodode AtualizarValoreseseucódigodeveficarsimilaraocódigo
aseguir.
private void AtualizarValores()
{
kinect.ElevationAngle = Convert.ToInt32(slider.Value);
label.Content = kinect.ElevationAngle;
}
Simples,nãoémesmo?Agorabastacriarumachamadaparaestemétododentro
dométodo slider_DragCompletedetudojáiráfuncionar!
Figura3.3:AplicaçãoEixoMotorizado
26

## Página 31

Capítulo4
FluxodeCores
Nostrêscapítulosseguintesserãoapresentadasasfuncionalidadeseprocessamentos
quegeramosfluxos(streams)quefazempartedaclasse KinectSensor.Elessão:
fluxodecores( ColorStream),fluxodeprofundidade( DepthStream)efluxode
esqueletodeusuário( SkeletonStream).Todospossuemalgumascaracterísticas
emcomumeestãoligadosaumoumaissensoresqueenvolvemseuprocessamento.
AmbosprecisamserligadosparaqueoKinectcomeceaprocessá-losepossuemdois
caminhosparaseobterumquadro,ouutilizandoummétodoparasolicitaroúltimo
quadrojáprocessado,ouatravésdeumeventoqueédisparadocadavezqueumnovo
quadrodestefluxoestápronto,ouseja,jácompletousuaetapadeprocessamento.
Alémdisso,podemseracessadosatravésdoevento AllFramesReady,quepossui
informaçõesdestestrêstiposdefluxos.
Ofluxogramadefuncionamentodetodososfluxossupracitadoséilustradopela
figura4.1.

## Página 32

4.1. Formatos CasadoCódigo
Figura4.1:Fluxogramadeprocessamento
NestecapítulovamosentendercomofuncionaacâmeradecoresdoKinect,
comoutilizá-laparacapturarfotosevídeos,comotratarasimagensbitporbite
comoaplicarestasfuncionalidadesemumaaplicaç ãoreal.
4.1 Formatos
AcâmeradecoresdoKinectpossuiumasériedeconfigurações,queinfluênciadi-
retamentenaqualidadedaimagemenaquantidadedequadrosporsegundoqueo
Kinectconsegueprocessar.Atabela 4.2ilustraestasresoluções.
28

## Página 33

CasadoCódigo Capítulo4. FluxodeCores
Figura4.2:TabeladeConfiguraçõesdaCâmeraRGB
VocêprovavelmentejáouviufalarsobreoformatoRGBou(Red-Green-Blue),
bastanteconhecidonoramodacomputaç ão.Nesteformato,cadapixeldaimagem
possuiumaquantidadedacorvermelha,umaquantidadedacorverdeeumaquan-
tidadedacorazul,asomadestestrêsvaloresrepresentamacordopixel.
OformatoYUVcodificaumaimagemouvideolevandoemcontaapercep ção
humana. Elepermiteumareduç ãodalarguradebandadeumatransmissãopois
utilizasomente16bitsporpixel,entãoémuitoútilparacomprimirimagens,poisa
perdaémascaradapelapercep çãohumana,enquantoqueoRGBpossuiodobrode
tamanhoporpixelenemsemprefazdiferen çaparanossosolhos.NasiglaYUV,oY
representaaluminânciadeumpixel,ouseja,quantidadedeluminosidadepercebida
peloolhohumanonaquelepixel,enquantoqueassiglasUeVrepresentamdois
componentesdiferentesdecrominância,queéaformacomonossosolhospercebem
ascores.
Afigura4.3 ilustraaimagemcomoscomponentesseparados.
29

## Página 34

4.1. Formatos CasadoCódigo
Figura4.3:ImagemYUV
OformatoBayerébastantesimilaraoRGB,maselealteraaimagemproporci-
onalmenteànossapercep çãoparacores,entãooverde(queéacorquemaisper-
cebemos)émaislevadoemconsideraç ãodoqueovermelhoouazul.Asdiferen ças
visuaisentreosformatosRGB,YUVeBayersãobemsutis,afigura 4.4ilustrauma
mesmaimagemnostrêsformatoscomaresoluç ãomáxima.
30

## Página 35

CasadoCódigo Capítulo4. FluxodeCores
Figura4.4:Comparaç ãoentreformatosdaCâmeraRGB
Oformato InfraRedouinfravermelhoébemdiferentedoscitadosanteriormente.
Quandoacâmeraéhabilitadacomesteformato,podemosvisualizaraformacom
queoKinect“vê”oambiente.Oresultadoéumaimagemescuracomdiversospontos
luminosos,querepresentamospontosinfravermelhosquesãolan çadospeloemissor
deluzinfravermelhonoambiente.
4.2 Aplicação
Nestecapítuloiremoscriarumaaplicaç ãoumpoucomaiscomplexa,quecontará
comasfun çõesmencionadasanteriormente:baterumafotoeexibirnaaplicaç ãoa
imagem(queseráfeitoutilizandoofluxodecoressobdemanda),exibirnaaplicaç ão
umovídeodoqueacâmeraRGBestávendo(queseráfeitoutilizandooevento)e
criaremosumaop çãoparautilizarumfiltrodeescalacinzasobreaimagem.
Comovocêjádeveestaracostumadocriaremosumanovaaplicaç ãoWPFeno-
vamenteiremosincluirasreferênciasparanossoprojetoauxiliareparaaSDKdo
Kinect.Nossaaplicaç ãoseráconstruídaporetapas—primeiramenteiremosfazer
comqueelaapenasbatafotosobdemanda.
Criandoolayout
OLayoutdestaaplicaç ãoserárelativamentesimples.Primeirovamosdividiro
componente Gridemduaslinhas,utilizandoo Grid.RowDefinitionsquejá
mencionamosanteriormente.Alinhainferiornãodevereceberumvalormuitoalto
31

## Página 36

4.2. Aplicação CasadoCódigo
parasuaaltura(50ésuficiente),poiselairáservirapenasparainserirmosnossobo-
tãoquebateráafoto,todoorestodaalturadajaneladevepertenceralinhasuperior,
jáqueelateráocomponentequeiráexibiraimagemdenossafoto.Ocódigodesua
teladeveficarsimilaraocódigoaseguir.
<Window x:Class="SensorRGB.MainWindow"
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
Title="MainWindow" Height="350" Width="525">
<Grid>
<Grid.RowDefinitions>
<RowDefinition Height="*"/>
<RowDefinition Height="50"/>
</Grid.RowDefinitions>
<Button Content="Bater Foto" Grid.Row="1" Margin="10,10"
Width="70" HorizontalAlignment="Left"
Click="Button_BaterFoto"/>
<Image Name="imagemCamera" />
</Grid>
</Window>
Utilizandoumquadrosobdemanda
Note que, no código anterior, já foi atribuído um evento para o bo-
tão que irá bater a foto, vamos então ao código. Como padrão, após o
método InitializeComponent da janela devemos inicializar o sensor de
nossa aplicação. No caso desta aplicação, iremos criar um método cha-
mado InicializarKinect(), pois além de fazermos a inicialização pa-
drão temos que inicializar o fluxo de cores. Para isso, basta utilizarmos o
método Enable() do objeto ColorStream que pertence ao sensor, ele
pode receber por parâmetro o formato que a câmera irá utilizar (RGB, YUV,
Bayer ou IR). Caso você não informe nada ele assumirá o formato padrão (
ColorImageFormat.RgbResolution640x480Fps30).
Ocorpodométodocriadodeveficarsimilaraocódigoaseguir.
private void InicializarKinect()
{
32

## Página 37

CasadoCódigo Capítulo4. FluxodeCores
kinect = InicializadorKinect.InicializarPrimeiroSensor(10);
kinect.ColorStream.Enable();
}
Nestecasoopteiporlevantaroeixodosensor10graus,masissopodeficara
seucritério.Vocêpodenotarqueainicializaç ãodosfluxosdoKinectpodeserfeita
demaneirabastanteintuitivaesimples.Essaformaéamesmaparaostrêstiposde
fluxocitadosanteriormente.
Agora iremos criar o método que irá receber um quadro de cores do sen-
sorRGBeiráobteraimagemdestequadro. Vocênotaráqueapesardeparecer
complicado,tambéméumatarefabastantesimples. Estemétodoirásechamar
ObterImagemSensorRGB,eledeveretornarum ImageSourcequeseráinserido
comofontededadosparaocomponentedeimagemereceberáporparâmetroum
objetodotipo ColorImageFrame,querepresentaumquadrodosensorRGB.
Umobjetodotipo ColorImageFrameéumobjetoquepodeserclassificado
comorecurso,eleimplementaainterface IDisposable,ouseja,vocêdeveutilizar
ométodo Dispose()paradestruiroobjetoousimplesmenteutilizarocomando
using. Paratornarocódigomaislegível,utilizaremosnoexemploasegundaop-
ção. Dentrodoescopodobloco usingteremosquecriarumarraydebyteseo
converteremosparaafontedocomponentedeimagem.
private BitmapSource ObterImagemSensorRGB(ColorImageFrame quadro)
{
using (quadro)
{
byte[] bytesImagem = new byte[quadro.PixelDataLength];
quadro.CopyPixelDataTo(bytesImagem);
return BitmapSource.Create(quadro.Width, quadro.Height,
96, 96, PixelFormats.Bgr32, null, bytesImagem,
quadro.Width * quadro.BytesPerPixel);
}
}
Comovocêpodevernométodoanterior,praticamentetodaainformaç ãorefe-
renteàimageméretiradadoobjeto quadro.Ométodoestático Createdaclasse
BitmapSourcerecebeumasériedeparâmetros,agorairemosentenderosignifi-
cadodecadaumdeles.
33

## Página 38

4.2. Aplicação CasadoCódigo
Osdoisprimeirossãorespectivamentealarguraeaalturadaimagem,bastare-
tirarestasinformaçõesdoquadro. Osdoisseguintesqueestãonoexemplo:96,96
sãoaquantidadedepontosporpolegadas(dpi)noseixosXeY.Oparâmetrose-
guinteserefereaoformatodecadapixeldaimagem—casovocêaltereoformatode
inicializaçãodofluxodecorespossivelmentetambémterádealteraroformatodos
pixelsdaimagem.Oparâmetroqueestásendoenviadocomo nulléutilizadopara
passarumapossívelpaletedecores,oquenestecasonãoéinteressante.Apóseste,
sãoenviadosporparâmetroosbytesqueaimagemcontémefinalmenteporúltimo
éenviadoo stridedaimagem.
Stride
Quandoumaimagemouvídeoéarmazenadonamemóriadeum
computador,seubufferequivalentenamemóriapodeconterinforma-
çõesextras,alémdaprópriaimagemapósofimdecadalinhadepixels.
Estasinformaçõesextrasgeralmentesãoutilizadasparaafetaraforma
comoaimageméarmazenadanamemóriaenãotêmavercomaforma
comqueaimageméexibida.
http://msdn.microsoft.com/en-us/library/windows/desktop/
aa473780
Apósterfeitoestemétodo,precisamosinvocá-lonoeventoqueinterpretao
clique do botão. Ele irá conter apenas uma linha que fará com que a propri-
edade Sourcede nosso componente de imagem receba o retorno do método
ObterImagemSensorRGB.Lembre-sequeesteúltimométodocitadoprecisare-
ceberporparâmetrooquadroatualdosensorRGB.Parafazermosisso,utilizamoso
método OpenNextFramedoobjeto ColorStreamdosensor,querequerumpa-
râmetroquerepresentaotempodeespera(emmilissegundos)atéqueoframeseja
aberto.Nesteexemploutilizaremosovalor0(zero),poisdesejamosqueafotoseja
tiradainstantaneamente.
private void Button_BaterFoto(object sender, RoutedEventArgs e)
{
imagemCamera.Source =
ObterImagemSensorRGB(kinect.ColorStream.OpenNextFrame(0));
}
34

## Página 39

CasadoCódigo Capítulo4. FluxodeCores
Agorapodemosexecutaraaplicaç ãoeaoclicarnobotão“BaterFoto”játemos
oresultadoesperado!
Figura4.5:AplicaçãoutilizandoosensorRGB
Utilizandooeventodequadrosnovosemumfluxodecores
Jávimoscomopodemosbuscarquadrosdosfluxossobdemanda,quetalrefato-
rarestaimplementaçãoparautilizaroevento?Comissoteremosumanovaimagem
acadaquadro,ouseja,30vezesporsegundo. Primeiramenteremovemosobotão
parabaterfoto(eseumétodorelacionadoaoevento Click)denossaaplicaç ão,já
queelenãofazmaissentido.Depoisdissofaremosumpequenoajustenométodo
InicializarKinect,iremosinterpretaroevento ColorFrameReadydoobjeto
ColorStreamapósinicializarofluxodesteobjeto.
Ométodoqueinterpretaráesteeventorecebeporparâmetroumobjetodotipo
ColorImageFrameReadyEventArgseédesteobjetoqueteremosqueretiraro
novoquadrodeimagemutilizandoométodo OpenColorImageFrame,ouseja,
35

## Página 40

4.2. Aplicação CasadoCódigo
faremosumachamadamuitosimilaràqueexistianométododobotãodebaterfoto,
porémdestavez,utilizaremosoquadrodoobjetoqueéenviadoporparâmetroenão
diretamentedoobjetodefluxo.
private void kinect_ColorFrameReady(object sender,
ColorImageFrameReadyEventArgs e)
{
imagemCamera.Source =
ObterImagemSensorRGB(e.OpenColorImageFrame() );
}
CasooKinectlevemaistempoparainicializarqueaprimeirachamadadomé-
tododescritoanteriormente,aaplicaç ãolan çaráumaexce ção,então,antesdoco-
mando usingnométodo ObterImagemSensorRGBéinteressantefazerumava-
lidaçãodoquadroatual,ouseja,verificarseoquadronãoestánulo.
Sevocêfeztudocertoeexecutaraaplicaç ãojáiráverovídeoemtemporealdo
queoKinectestávendo!
Utilizandoumfiltrodeimagem
Quetalincrementaraindamaisnossaaplicaç ãoutilizandoumfiltrodeimagem?
Iremosfazeroexemploutilizandoumfiltrosimplesparadeixaraimagememescala
cinza(popularmentechamadodepretoebranco).Primeirofaremoscomqueofiltro
paraescalacinzasejaopcional,entãocriaremosumcomponentedotipo CheckBox
nomesmolocalondeficavaobotãoparabaterfotoeestecomponenteiránosindicar
quandodeveremosaplicarofiltro.
Para aplicarmos o filtro, é preciso refatorar o método
ObterImagemSensorRGB. Como você deve ter percebido nós podemos ma-
nipularcadapixeldaimagemdoquadroatual,entãovamosutilizarumalgoritmo
simplesparaconverterascoresRGBdestepixelemescalacinza.
Após copiarmos os dados da imagem para o array de pixelbyte[]
bytesImagem,faremosumlaçoderepetiç ãoparapercorrertodosospixelssubs-
tituindoovalordascoresR,GeBpelovalormaisaltodostrês(utilizeométodo
Math.Max). Issoseráfeitoporquetodaaescalacinzadecorespossuiosvalores
RGBidênticos.
Éimportanteteremmentenestaimplementaç ãoqueumpixelnãoénecessari-
amenteumbyte.Dependendodoformatodecoressãonecessáriosmaisdeumbyte
parapreencherumpixel—estainformaç ãopodeserobtidaatravésdapropriedade
36

## Página 41

CasadoCódigo Capítulo4. FluxodeCores
BytesPerPixeldoobjeto ColorImageFrame.Nocasodoformatopadrão,cada
pixelérepresentadopor4bytes,umparaoR,umparaoG,umparaoBeumpara
oAlpha(transparência),sendoassim,nossolaçoderepetiç ãodevepularde4em
4bytes. Casovocêtenhatentadorefatorarométodo,eledeveestarsemelhanteao
códigoaseguir.
private BitmapSource ObterImagemSensorRGB(ColorImageFrame quadro)
{
if (quadro == null) return null;
using (quadro)
{
byte[] bytesImagem = new byte[quadro.PixelDataLength];
quadro.CopyPixelDataTo(bytesImagem);
if (chkEscalaCinza.IsChecked.HasValue &&
chkEscalaCinza.IsChecked.Value)
for (int indice = 0;
indice < bytesImagem.Length;
indice += quadro.BytesPerPixel)
{
byte maiorValorCor = Math.Max(bytesImagem[indice],
Math.Max(bytesImagem[indice + 1],
bytesImagem[indice + 2]));
bytesImagem[indice] = maiorValorCor;
bytesImagem[indice + 1] = maiorValorCor;
bytesImagem[indice + 2] = maiorValorCor;
}
return BitmapSource.Create(quadro.Width, quadro.Height,
96, 96, PixelFormats.Bgr32, null, bytesImagem,
quadro.Width * quadro.BytesPerPixel);
}
}
OcomponentedetelanomeucasosechamachkEscalaCinzaeeleéutilizadona
verificaçãoantesdolaçoderepetiç ão.Comisso,jápodemosexecutarnossocódigo
eaomarcaro CheckBoxteremosumresultadosemelhanteaodafigura 4.6.
37

## Página 42

4.3. Refatoração CasadoCódigo
Figura4.6:Filtroparaescalacinza
4.3 Refatoração
Você deve se lembrar que na seção 1.3 havia sido mencionado o Kinect
toolkit; pois bem, utilizaremos o toolkit (Microsoft.Kinect.Toolkit, Micro-
soft.Kinect.Toolkit.Controls e Microsoft.Kinect.Toolkit.Controls.Interaction) para
fazerumarefatoraçãoemnossocódigo.
RefatorandoaDLLAuxiliarKinect
Primeirovamosrefatorarnossoprojeto AuxiliarKinect,vocêselembraqueo
métododeinicializaç ãonãoprevênenhumtipodeproblema? Bom, jáestána
horaderesolvermosisso. PrimeiroadicioneareferênciasomenteàDLLMicro-
soft.Kinect.Toolkit.NestaDLLháumaclassechamada KinectSensorChooser,
queéfeitaparaserutilizadacomoumseletordosensorKinecteelamesmajáge-
renciaaspossíveisexce ções.
38

## Página 43

CasadoCódigo Capítulo4. FluxodeCores
Refatoração
Nestase çãoiremosrefatoraraDLLAuxiliarKinect,entãocasovocê
queiramanterasimplementaçõesantigassugiroquefaç aumacópiadeste
projetoantesdeefetuarestasnovasalterações.
Aprimeiracoisaquefaremosnanossaclasse InicializadorKinectécriar
umapropriedadedaclasse KinectSensorChooserchamada SeletorKinect.
Sugiroqueestapropriedadetenhaométodo getpúblicoeométodo setprivado.
Tambémcriaremosumapropriedadetotalmentepúblicanesteclassedotipo
Action<KinectSensor>.Estapropriedadeéumdelegateparaafun çãoquepre-
cisaráserinvocadasemprequeosensorforinicializado,falaremosmaissobreela
maistarde.
Criaremos também um construtor para nossa classe, que deve instanciar a
propriedade SeletorKinect, associar um método que interprete o evento
KinectChangedeinicializaroseletor,conformeocódigoaseguir.
public Action<KinectSensor> MetodoInicializadorKinect
{ get; set; }
public KinectSensorChooser SeletorKinect
{ get; private set; }
public InicializadorKinect()
{
SeletorKinect = new KinectSensorChooser();
SeletorKinect.KinectChanged += SeletorKinect_KinectChanged;
SeletorKinect.Start();
}
Ométodo SeletorKinect_KinectChangedéinvocadotodavezqueum
sensoréconectadooudesconectado(porqualquermotivo)easinformaçõesrefe-
rentesaestesensorestãoencapsuladasnaspropriedades OldSensore NewSensor
doobjeto KinectChangedArgsqueérecebidoporparâmetro. Nestaaplicaç ão,
iremosinvocarométodoqueinicializaosensorcadavezqueumnovosensoré
descobertoedesligarasfun çõesdeumsensorquefoidesconectado,apenaspara
segurança,poisnãoéemtodososcasosqueosensorfoidesconectadodaenergia
39

## Página 44

4.3. Refatoração CasadoCódigo
—mesmoestandoemumestadoinválidoeleaindapodeconsumirrecursodamá-
quina.
Paradesligartodososfluxosutilizaremosométodo Disable()decadafluxo,
masantesdedesligá-losénecessárioverificarseosmesmosestãoligadosatravés
dapropriedade IsEnabled.Énecessárioqueestedesligamentoestejasendofeito
dentrodeumbloco try catch,poisosensorpodeentraremumestadoinválido
durantealgumaoperação.
private void SeletorKinect_KinectChanged(object sender,
KinectChangedEventArgs kinectArgs)
{
if (kinectArgs.OldSensor != null)
{
try
{
if (kinectArgs.OldSensor.DepthStream.IsEnabled)
kinectArgs.OldSensor.DepthStream.Disable();
if (kinectArgs.OldSensor.SkeletonStream.IsEnabled)
kinectArgs.OldSensor.SkeletonStream.Disable();
if (kinectArgs.OldSensor.ColorStream.IsEnabled)
kinectArgs.OldSensor.ColorStream.Disable();
}
catch (InvalidOperationException)
{
// Captura exceção caso o KinectSensor entre
// em um estado inválido durante a desabilitação
// de um fluxo.
}
}
if (kinectArgs.NewSensor != null)
{
if (MetodoInicializadorKinect != null)
MetodoInicializadorKinect(SeletorKinect.Kinect);
}
}
40

## Página 45

CasadoCódigo Capítulo4. FluxodeCores
RefatorandoaAplicaçãoSensorRGB
Agora iremos refatorar nossa aplicação para se adequar a este novo
AuxiliarKinect. Basicamente o que precisamos fazer é alterar o método
InicializarKinectparaque,aoinvésdeutilizarométodoestáticodeantes,
passeautilizarnossonovoseletor.
Antes de alterarmos este método, criaremos um novo método nesta apli-
cação, chamado InicializarSeletor. Ele irá instanciar um novo objeto
InicializadorKinecteinvocarométodojáexistente InicializarKinect
queagoranãodevemaisconterachamadaparaoantigométodoestáticodaclasse
InicializadorKinectedevereceberoobjetoKinectdoseletorporparâmetro.
Seucódigoficarásimilaraocódigoaseguir.
private void InicializarSeletor()
{
InicializadorKinect inicializador = new InicializadorKinect();
InicializarKinect(inicializador.SeletorKinect.Kinect);
}
private void InicializarKinect(KinectSensor kinectSensor)
{
kinect = kinectSensor;
kinect.ColorStream.Enable
(ColorImageFormat.RgbResolution640x480Fps30);
kinect.ColorFrameReady += kinect_ColorFrameReady;
}
Agoranoconstrutorpassaremosainvocarométodoparainicializaroseletor
enãomaisosensor,poisestemétodojáseráchamadointernamente. Talvezvocê
estejacomdúvidasquantoaomotivodetermosdoismétodosseparados,umpara
apenasosensoreumparaoseletor(quechamainternamenteométododosensor),
estaperguntaserárespondidaembreve.
Notequeapenasduaslinhasforamcriadas,eseráqueaaplicaç ãocontinuaa
mesma?Arespostaé não,agoracasoaconte çaalgumproblemacomosensoraapli-
caçãonãodisparaexce çõesnãotratadas,esim,apenasparadeatualizarosquadros
dovídeo.Porémaindaexisteumproblemanãoresolvidonestarefatoraç ão:casoo
sensorvolteaseuestadofuncional,elenãoretornaráaligarofluxodecoresenão
voltaráaatualizaraimagem.Faç aoseguinteteste:removaseusensordeseucom-
putador(asimagensirãoparardeseratualizadas)eemseguidareconecteosensor
(nadadeveacontecer).
41

## Página 46

4.3. Refatoração CasadoCódigo
Pararesolveresteproblema,precisamosinformaraoobjeto inicializador
quetemosummétodoqueénecessárioexecutarsemprequeumsensorfordesco-
berto,paraisso,utilizaremosapropriedade MetodoInicializadorKinect.En-
tãonométodo InicializarSeletorapósinstanciaroobjetodevemosatribuirà
propriedade MetodoInicializadorKinectométodo InicializarKinect.
Feitoissonãoserámaisnecessárioinvocá-lodentrodométodoqueinicializaose-
letor.
Refaçaotestederemoverereconectarosensoremseucomputadorevocêper-
ceberáqueagoraelevoltaafuncionarassimqueoKinectéreconectado!Masainda
nãoacabamos,vamosànossajanelanovamente.
No Gridprincipaldenossajanelacrieumanovalinhaacimadopaineldeima-
gemcomamesmaalturadalinhaondeestáamarcaç ãoparaescalacinza(nãoes-
queçadeincluirapropriedade Grid.Row = "1" noobjeto Image).Agorausare-
moso Microsoft.Kinect.T oolkit.Controls.Interactionsparaalterarainterfacedenossa
janela.
Apóstercriadoanovalinhano Gridvamosadicionarareferênciaao T ool-
kit.Controls.InteractionsdentrodaprópriajanelanalinguagemXAML.Procurepela
linha xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml” ,estaéasintaxede
umareferênciaparaumschemaemXAML.Abaixodela,adicioneaseguintelinha;
xmlns:k="http://schemas.microsoft.com/kinect/2013” comissojátemosareferência
paraonamespaceondeseencontracomponentevisualdoseletor.
Vamosadicioná-loàlinhacriadano Grideiremosposicionarverticalmente
notopoehorizontalmentenocentro.Lembre-sequeparaacessarumcomponente
emXAMLquepertenceaumnamespaceénecessárioinformaronamespaceantes,
utilizandoaseguintesintaxe: namespace:componente,seuXAMLdeveterficado
similaraocódigoaseguir.
<Window x:Class="SensorRGB.MainWindow"
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
xmlns:k="http://schemas.microsoft.com/kinect/2013"
Title="MainWindow" Height="350" Width="525">
<Grid>
<Grid.RowDefinitions>
<RowDefinition Height="50"/>
<RowDefinition Height="239*"/>
<RowDefinition Height="50"/>
</Grid.RowDefinitions>
42

## Página 47

CasadoCódigo Capítulo4. FluxodeCores
<Image Name="imagemCamera" Grid.Row="1" />
<CheckBox Name="chkEscalaCinza" Content="Escala cinza"
HorizontalAlignment="Left" Margin="10,10,0,10" Grid.Row="2"/>
<k:KinectSensorChooserUI Name="seletorSensorUI"
HorizontalAlignment="Center" VerticalAlignment="Top" />
</Grid>
</Window>
Porúltimotemosdeligaranossaclasseseletoraaonossocomponentevisual,
iremosfazerissoapósaúltimalinhadométodo InicializarSeletor.
private void InicializarSeletor()
{
InicializadorKinect inicializador = new InicializadorKinect();
inicializador.MetodoInicializadorKinect = InicializarKinect;
seletorSensorUI.KinectSensorChooser = inicializador.SeletorKinect;
}
Agora,aoexecutarnovamenteaaplicaç ãovocêiráperceberocomportamento
destecontrole(eleexibeapenasumícone,mascasovocêpasseomouseacimado
íconeéexibidoumpaineldetalhado).Casovocêdesconecteosensorcomofizemos
antes,eleiráexibirumalertaconformefigura 4.7(amensagemdoalertavariade
acordocomoerro),ecasoreconecte,elemostraqueosensorestáprontonovamente.
Estecomponenteémuitoútilparacriarumainterfaceagradávelcomousuárioe
tornarsuaaplicaçãomaisresponsiva.
43

## Página 48

4.3. Refatoração CasadoCódigo
Figura4.7:SeletordoKinect
Quetalincrementarmosnossaaplicaç ãoutilizandooqueaprendemosnoca-
pítuloanterior? Vamosinserirumcomponente Sliderparapodermosalteraro
ângulodeelevaç ãodosensornestaaplicaç ão.Destaveziremosfazerospassosum
poucomaisrápido,poisjáfizemosumaimplementaç ãoparecida.
Primeiroiremosalterarolayoutdenossaaplicaç ão,adicionandoumacolunaao
Gridprincipal. Estacolunaseráadicionadanoladodireitodajanelaedeveráter
umalarguradetamanho25.Nestacolunairemosadicionarocomponente Slider
seguindoasmesmasconfiguraçõesdaaplicaç ãoanterior(Valormáximoemínimo).
Parafinsestéticosiremosfazerum Bindingnapropriedade Heightdocomponente
Slidercomapropriedade ActualHeightdocomponente Imagedoformulário.
44

## Página 49

CasadoCódigo Capítulo4. FluxodeCores
Binding
Bindingsignifica“fazerligação”.Esterecursogeralmenteéutilizado
parafazerumaligaç ãoentreumdadodobancodedadoseumcom-
ponentevisualemumajanela,masemaplicaçõesWPFpodemosuti-
lizarestatécnicaparavincularinformaçõesdequalquertipo. Nocaso
citadoanteriormente,ovalordapropriedadequerepresentaaalturado
componente Slidersemprepossuiráomesmovalordapropriedade
querepresentaaalturadaimagembuscadapeloKinect,harmonizando
olayoutdaaplicaç ão.
Tambémparafinsestéticosiremosalterarapropriedade Stretchdocompo-
nenteimagemparaovalor "Fill".Comisso,aimagemserá“esticada”paraocupar
todoespaçodocomponente.ApósfazerestasimplementaçõesoarquivoXAML,sua
janeladeveestarparecidacomocódigoaseguir.
<Window x:Class="SensorRGB.MainWindow"
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
xmlns:k="http://schemas.microsoft.com/kinect/2013"
Title="MainWindow" Height="350" Width="525">
<Grid>
<Grid.ColumnDefinitions>
<ColumnDefinition Width="*"/>
<ColumnDefinition Width="25"/>
</Grid.ColumnDefinitions>
<Grid.RowDefinitions>
<RowDefinition Height="50"/>
<RowDefinition Height="240*"/>
<RowDefinition Height="50"/>
</Grid.RowDefinitions>
<Image Name="imagemCamera" Grid.Row="1" Stretch="Fill"/>
<CheckBox Name="chkEscalaCinza" Content="Escala cinza"
HorizontalAlignment="Left" Margin="10,10,0,10" Grid.Row="2"/>
<k:KinectSensorChooserUI Name="seletorSensorUI"
HorizontalAlignment="Center" VerticalAlignment="Top" />
45

## Página 50

4.3. Refatoração CasadoCódigo
<Slider Name="slider" Width="20" Orientation="Vertical"
Minimum="-27" Maximum="27" SmallChange="1" Value="0"
Height="{Binding ElementName=imagemCamera, Path=ActualHeight}"
Thumb.DragCompleted="slider_DragCompleted"
Grid.Column="1" Grid.Row="1"/>
</Grid>
</Window>
Comovocêpodeternotado,nocódigoanteriorocomponentenomeadoslider,
interpretaoevento DragCompleted.Esteéomesmoeventoqueutilizamosnoca-
pítuloanterior,agoratemosdeimplementá-loparaqueelesincronizeapropriedade
ElevationAngledoKinectcomovalordocomponenteslider.
private void slider_DragCompleted
(object sender,
System.Windows.Controls.Primitives.DragCompletedEventArgs e)
{
kinect.ElevationAngle = Convert.ToInt32(slider.Value);
}
Apósestasimplementaçõesvocêjápodeutilizaraaplicaç ãoealteraroângulo
deelevaçãodosensoratravésdocomponentevisual!
46

## Página 51

CasadoCódigo Capítulo4. FluxodeCores
Figura4.8:Aplicaç ãocomocomponenteSlider
Antesdepassarmosparaonovoassuntoeusugiroquevocêfaç amaistestescom
outrostiposdeformatoparaofluxodecores.Faremosumapequenaalteraç ãopara
oformato infraredapenasparatermoscontatocomesteformatoqueébemdiferente
dosdemais.
Paraalteraroformatodofluxodecoresbastapassarporparâmetronométodo
Enableoformato InfraredResolution640x480Fps30,alémdisso,emnossa
criaçãodo BitmapSourceprecisamosalteraro PixelFormatpara Gray16.
Comestassimplesalterações,aimagemqueseráexibidanocomponentejáseráto-
talmentediferente,conformeafigura 4.9.
47

## Página 52

4.3. Refatoração CasadoCódigo
Figura4.9:Fluxodecoresinfravermelho
Éimportantelembrar-sequeoSDKnãopermiteainicializaç ãodedoisformatos
diferentesparaomesmofluxo,entãonãoépossívelhabilitaroinfravermelhoeo
RGB,porexemplo,vistoqueoinfravermelhoapesardeserbastantediferentenãoé
umfluxoaparte,esimumaconfiguraç ãodofluxodecores.
48

## Página 53

Capítulo5
FluxodeProfundidade
Nestecapítuloiremosincrementaraaplicaç ãoanteriorutilizandoalgunsconceitos
deprofundidade. Veremoscomoutilizaremosasinformaçõesdestefluxoparade-
tectarmosusuárioseadistânciaqueosobjetosestãodosensor.
5.1 Formatos
OsensordeprofundidadedoKinecttambémpossuidiferentestiposdeformatoe
parautilizarumformatoéexatamenteigualaosensorRGB,ouseja,oparâmetro
referenteaoformatopodeserinformadonométodo Enabledofluxodeprofundi-
dade( DepthStream).
Noformatodestefluxo,épossívelalterarsomentearesoluç ão,poisemtodos
osformatoso FPS (frames per second) ouquadrosporsegundopermanece30ea
quantidadedebitsporpixelpermanece16.Afigura 5.1ilustraadiferen çaentreos
formatos.

## Página 54

5.2. Entendendoumpoucomaissobreaprofundidade CasadoCódigo
Figura5.1:TabeladeConfiguraçõesdosensordeprofundidade
5.2 Entendendo um pouco mais sobre a profundi-
dade
Aconfiguraçãode near modedisponívelsomentenaversãodoKinectparaWindows
afetadiretamenteestefluxo,poisoKinectpossuiumadistânciamínimaemáxima
paraqueelepossaverificaradistânciasdosobjetos. Estavariaç ãodedistânciano
formatonormalédenomínimo0,8menomáximo4m.No near modeestadistância
mudapara0,5mnomínimoenomáximo3m. Vocêdeveoptarpeloformatoque
maisseencaixaemsuaaplicaç ão,ouutilizarsomenteomodopadrãocasoaversão
deseuKinectsejaaversãoparaXbox360.
AimagemreconhecidapeloKinectpodeserdescritaemumformatoconhecido
comoRGBD,ouseja, Red-Green-Blue-Depth.Todopixeldeprofundidadepossui16
bits,sendo13bitsparainformaçõesreferentesàprofundidadee3bitsqueidentificam
seopixelpertenceàumhumano.
Estaáreade3bitsqueidentificaoshumanoséconhecidapor player segmen-
tation data,ouseja,segmentodedadosdeumjogadorouusuário. Acâmerade
profundidadeécapazdereconheceraté6usuáriosemfrenteaosensoretodasestas
informaçõescitadassãoobtidasatravésdaclasse DepthImagePixel.
Ofluxodeprofundidadeestáintimamenteligadoaofluxodeesqueleto,poisam-
bosutilizamrecursosunsdosoutrosparaobtereminformações,umexemplodissoé
opróprio player segmentation data.Paraqueestasinformaçõesestejamdisponíveis
noquadrodeprofundidadeénecessárioqueofluxodeesqueletoestejaativo.
TodasestasinformaçõesreferentesàprofundidadesãocapturadaspeloKinect
50

## Página 55

CasadoCódigo Capítulo5. FluxodeProfundidade
utilizandoumatécnicaconhecidacomo EfeitoParallax.Esteefeitoocorrenatural-
menteemnossaprópriavisãoparaidentificaradistânciadosobjetos.Nãocabeao
escopodestelivroaexplicaç ãodesteefeito,masparaquevocêpossacompreendê-lo
demaneirasimplesesuperficialimagineoseguintecenário,vocêestáemumcarro
emumarodoviaeaoladodestarodoviaexistemdiversasárvoresemontanhas,ao
olharpelajanelavocêconsegueperceberqueasárvoresqueestãomaispróximasà
rodoviapassammaisrápidodoqueamontanhaqueestáaofundo,estapercep ção
quetemoséo efeitoparallax citadoanteriormente.
Osensorutilizaesteefeito,seusdoissensoresdeprofundidadeeumalgoritmo
paradetectaraprofundidadedecadaobjetonaimagem. Tantooefeitoparallax
quantoatécnicautilizadapeloKinectsãomaiscomplexosdoqueestasbrevesexpli-
cações,masiremosfocarnaimplicaç ãodissoemumaaplicaç ãofinalenãonomodo
comooKinectfoiconcebido.
5.3 Aplicação
Agorairemosporempráticaosconceitosvistosanteriormentenestecapítulo,uti-
lizaremosamesmaaplicaç ãodocapítuloanterior,masinicialmentevamosdesa-
bilitar o fluxo de cores e habilitar o fluxo de profundidade. O primeiro passo
seráalterarométodo InicializarKinect, queinformamosnapropriedade
MetodoInicializadorKinectdenossoinicializador.
Vamoscomentaraslinhasqueiniciaofluxodecoresesubstituí-lasporlinhas
queiniciamofluxodeprofundidadeecriamummétodoparainterpretarseuevento,
conformecódigoaseguir.
private void InicializarKinect(KinectSensor kinectSensor)
{
kinect = kinectSensor;
slider.Value = kinect.ElevationAngle;
kinect.DepthStream.Enable();
kinect.DepthFrameReady += kinect_DepthFrameReady;
//kinect.DepthStream.Range = DepthRange.Near;
//kinect.ColorStream.Enable();
//kinect.ColorFrameReady += kinect_ColorFrameReady;
}
51

## Página 56

5.3. Aplicação CasadoCódigo
private void kinect_DepthFrameReady
(object sender, DepthImageFrameReadyEventArgs e)
{
}
CasovocêpossuaumKinectnaversãoparaWindowsedesejarativaromodo
deproximidadevocêdeveremoveroscomentáriosdalinhadecódigoqueatribuio
valor Nearparaapropriedade Rangedofluxodeprofundidade.Nesteponto,caso
vocêinicializeaaplicação,iráperceberqueaimagemdecoresnãoestámaissendo
exibida.
Aprimeirafuncionalidadequevamosimplementarseráoreconhecimentode
humanospeloKinectutilizandoo player segmentation data. Vamoscriarummé-
todoparafazerisso,masantesénecessáriotambéminicializaro fluxodeesqueleto,
conformemencionamosanteriormente.
Este método se chamaráReconhecerHumanos, ele receberá por parâme-
troumquadrodeprofundidade( DepthImageFrame)edeveráretornarumob-
jeto BitmapSourcepara preencher o componente de imagem de nossa apli-
cação. Para poder fazer a validação do pixel de acordo com oplayer seg-
mentation data, devemos criar um array do tipoDepthImagePixel, que irá
receber todas as informações do quadro de profundidade através do método
CopyDepthImagePixelDataTo. Cadapixeldestearraypossuiaspropriedades
PlayerIndex, Depthe IsKnownDepth,querepresentamrespectivamente:oín-
dicedousuárioaqualopixelpertence(zeroquandoopixelnãopertenceanenhum
usuário),adistânciadopixelaosensoremmilímetroseseosensorconsegueiden-
tificaradistânciadopixel.
Apósreceberestasinformaçõesprecisamoscriarumnovoarraydebytespara
geraraimagemqueseráretornadanométodo. Estearraydeveterquatrovezeso
tamanhodoarrayquerepresentaospixelsdeprofundidade,poisconformevimos
antes,cadapixeldecorpossui4bytes.Iremospercorrerestenovoarrayeverificare-
mosseobytereferenteaomesmopixelnaimagemdeprofundidadepertenceaum
usuárioounão,casoperten çairemospintarestepixeldeverde.Ocódigoaseguir
ilustracomoestaimplementaç ãodeveserfeita.
private BitmapSource ReconhecerHumanos
(DepthImageFrame quadro)
{
52

## Página 57

CasadoCódigo Capítulo5. FluxodeProfundidade
if (quadro == null) return null;
using (quadro)
{
DepthImagePixel[] imagemProfundidade =
new DepthImagePixel[quadro.PixelDataLength];
quadro.CopyDepthImagePixelDataTo(imagemProfundidade);
byte[] bytesImagem = new byte[imagemProfundidade.Length * 4];
for (int indice = 0; indice < bytesImagem.Length; indice+=4)
{
if (imagemProfundidade[indice / 4].PlayerIndex != 0)
{
bytesImagem[indice + 1] = 255;
}
}
return BitmapSource.Create(quadro.Width, quadro.Height,
96, 96, PixelFormats.Bgr32, null, bytesImagem,
quadro.Width * 4);
}
}
Você não deve ter muitos problemas em compreender o código do mé-
todo ReconhecerHumanos, poisemdiversospontoseleésimilaraométodo
ObterImagemSensorRGBcriadonocapítuloanterior.Notequenestaimplemen-
taçãoinserimosovalor255apenasnobytereferenteàcorverdedoRGB.Feitoisso,
vocêjádeveconseguirexecutaraaplicaç ãoeobterumresultadosemelhanteaoda
figura5.2.
53

## Página 58

5.3. Aplicação CasadoCódigo
Figura5.2:ReconhecedordeHumanos
Comovocêpodenotar,estafuncionalidadenãoéperfeita,maspossuiumre-
sultadomuitobom.Quetalagorafazermosumacombinaç ãoentreosdoissensores
utilizadosnestecapítuloenocapítuloanterior? Poisbem,estanovaimplementa-
çãofarácomqueonossocomponentedeimagemdaaplicaç ãoexibatodoocenário
atravésdosensordecores(comofizemosnocapítuloanterior),masutilizaráescala
cinzasomentenospixelsqueestãoemumadistânciamenorque2metrosdosensor.
Oprimeiropassoparacumprirestaimplementaç ãoéreativarofluxodecores.
Agoranossostrêsfluxosestarãoligadossimultaneamente,masnãoiremosinterpre-
taroseventos ColorFrameReadye DepthFrameReady. Aoinvésdissoutili-
zaremosoevento AllFramesReady,poisatravésdelepoderemosacessartantoo
quadrodeprofundidadequantooquadrodecores.
private void InicializarKinect(KinectSensor kinectSensor)
{
kinect = kinectSensor;
54

## Página 59

CasadoCódigo Capítulo5. FluxodeProfundidade
slider.Value = kinect.ElevationAngle;
kinect.DepthStream.Enable();
kinect.SkeletonStream.Enable();
kinect.ColorStream.Enable();
kinect.AllFramesReady += kinect_AllFramesReady;
}
private void kinect_AllFramesReady
(object sender, AllFramesReadyEventArgs e)
{
}
Precisamosalterarométodo ObterImagemSensorRGBpararetornaroarray
debytesdaimagemenãomaisoobjeto BitmapSource,poisagoraprecisamos
reutilizarosbytesdaimagemnométodoquereconheceráadistânciadosobjetos—
alémdisso,nãoémaisnecessáriodeixaralógicadeprogramaç ãoreferenteàescala
cinzanestemétodo. Apósestasalteraçõesométodoiráseparecercomométodo
ilustradoaseguir.
private byte[] ObterImagemSensorRGB(ColorImageFrame quadro)
{
if (quadro == null) return null;
using (quadro)
{
byte[] bytesImagem = new byte[quadro.PixelDataLength];
quadro.CopyPixelDataTo(bytesImagem);
return bytesImagem;
}
}
Ométodoficoumaissimples,poisagoraeleapenasretornaosbytesdaimagem.
Agora,éavezdecriarmosumnovométodochamado ReconhecerDistância,
quedevereceberporparâmetroosbytesdaimagemeadistânciamáximadosobjetos
paraaplicaraescalacinza.Alógicaparaaescalacinzaquefoiremovidadométodo
anteriordeveserincorporadaparaestemétododentrodoblocodevalidaç ãoda
distânciadosensorconformecódigo.
55

## Página 60

5.3. Aplicação CasadoCódigo
private void ReconhecerDistancia
(DepthImageFrame quadro, byte[] bytesImagem, int distanciaMaxima)
{
if (quadro == null || bytesImagem == null) return null;
using (quadro)
{
DepthImagePixel[] imagemProfundidade =
new DepthImagePixel[quadro.PixelDataLength];
quadro.CopyDepthImagePixelDataTo(imagemProfundidade);
for (int indice = 0;
indice < imagemProfundidade.Length;
indice++)
{
if (imagemProfundidade[indice].Depth < distanciaMaxima)
{
int indiceImageCores = indice * 4;
byte maiorValorCor =
Math.Max(bytesImagem[indiceImageCores],
Math.Max(bytesImagem[indiceImageCores + 1],
bytesImagem[indiceImageCores + 2]));
bytesImagem[indiceImageCores] = maiorValorCor;
bytesImagem[indiceImageCores + 1] = maiorValorCor;
bytesImagem[indiceImageCores + 2] = maiorValorCor;
}
}
}
Note que este método não retorna mais o objetoBitmapSource, isso
ocorre pois criaremos a imagem dentro do método que interpreta o evento
AllFramesReady. Neste método, sempre iremos captar a imagem do sen-
sor de cores, mas aplicaremos o filtro de escala cinza criado no método
ReconhecerDistânciaapenasquandoo CheckBox“Escalacinza”estivermar-
cado,conformeocódigoaseguir.
private void kinect_AllFramesReady
(object sender, AllFramesReadyEventArgs e)
{
56

## Página 61

CasadoCódigo Capítulo5. FluxodeProfundidade
byte[] imagem = ObterImagemSensorRGB(e.OpenColorImageFrame());
if (chkEscalaCinza.IsChecked.HasValue &&
chkEscalaCinza.IsChecked.Value)
ReconhecerDistancia(e.OpenDepthImageFrame(), imagem, 2000);
if (imagem != null)
imagemCamera.Source =
BitmapSource.Create(kinect.ColorStream.FrameWidth,
kinect.ColorStream.FrameHeight,
96, 96, PixelFormats.Bgr32, null,
imagem,
kinect.ColorStream.FrameBytesPerPixel
* kinect.ColorStream.FrameWidth);
}
Setudofoiimplementadodemaneiracorreta,oresultadoqueteremosdeverá
sersimilaraoresultadoilustradopelafigura 5.3.
57

## Página 62

5.3. Aplicação CasadoCódigo
Figura5.3:Escalacinzapordistância
Vocêdeveterpercebidoqueospixelsemescalacinzanãoestãoperfeitamente
alinhadosondedeveriam,issoficabastanteclaronafigura5.3. Esteproblemade
alinhamentoocorredevidoaofatodequeosdoissensores:coreprofundidadeficam
emlocaisfísicosdiferentes.Paranosajudarcomesteproblema,existemtécnicasde
mapeamento,quesãofeitasatravésdaclasse CoordinateMapper.
Aclasse CoordinateMapperfazatransformaçãodeumsistemadecoordena-
dasparaoutroentreosfluxosdoKinect.Infelizmenteparafazerissoháumaperda
notamanhototaldaimagem,jáqueparaequalizarospontoséobrigatórioqueseja
feitaumaintersecçãoentreasvisõesdosdiferentessensores.
Utilizaremosaclasseparamapearospontosdaimagemdeprofundidadeem
umarraydetamanho640x480(devidoaoformatodosfluxosselecionados)everifi-
caraprofundidadeatravésdestespontosmapeados.Alémdisso,umaoutratécnica
quenosajudaamelhoraraqualidadedoresultadoéverificarseopontodepro-
fundidadeéumpontoreconhecidopeloKinect. Apósestasmudan çasométodo
ReconhecerDistanciadeveficarcomoocódigoadiante.
58

## Página 63

CasadoCódigo Capítulo5. FluxodeProfundidade
private void ReconhecerDistancia
(DepthImageFrame quadro, byte[] bytesImagem, int distanciaMaxima)
{
if (quadro == null || bytesImagem == null) return;
using (quadro)
{
DepthImagePixel[] imagemProfundidade =
new DepthImagePixel[quadro.PixelDataLength];
quadro.CopyDepthImagePixelDataTo(imagemProfundidade);
DepthImagePoint[] pontosImagemProfundidade =
new DepthImagePoint[640 * 480];
kinect.CoordinateMapper
.MapColorFrameToDepthFrame(kinect.ColorStream.Format,
kinect.DepthStream.Format, imagemProfundidade,
pontosImagemProfundidade);
for (int i = 0; i < pontosImagemProfundidade.Length; i++)
{
var point = pontosImagemProfundidade[i];
if ( point.Depth < distanciaMaxima &&
KinectSensor.IsKnownPoint(point) )
{
var pixelDataIndex = i * 4;
byte maiorValorCor =
Math.Max(bytesImagem[pixelDataIndex],
Math.Max(bytesImagem[pixelDataIndex + 1],
bytesImagem[pixelDataIndex + 2]));
bytesImagem[pixelDataIndex] = maiorValorCor;
bytesImagem[pixelDataIndex + 1] = maiorValorCor;
bytesImagem[pixelDataIndex + 2] = maiorValorCor;
}
}
}
}
59

## Página 64

5.3. Aplicação CasadoCódigo
Nestepontovocêdeveexecutaraaplicaç ãoeobterumresultadosimilaraoda
figura5.4.
Figura5.4:Escalacinzapordistância(Melhorado)
Nouniversodossensorespraticamentenadaéexato,infelizmentenãopodemos
obterumresultadoperfeito,mascomovocêdeveternotadoapósaplicarestastéc-
nicas,oresultadosetornatotalmenteaceitávelecomumníveldeprecisãobastante
impressionante.
Antesdefinalizarmosestecapítuloéinteressanteressaltarumtestenestaapli-
cação. Casovocêaproximedemaissuamãodosensorelavoltaráaficarcolorida,
conformefigura 5.5,mesmocomadistânciasendomenordoqueadistânciamá-
ximaparaaplicarescalacinza.Vocêconsegueimaginarporqueissoocorre?
60

## Página 65

CasadoCódigo Capítulo5. FluxodeProfundidade
Figura5.5:Escalacinzapordistância(Teste)
Isso ocorre por conta de nossa verificaç ão
KinectSensor.IsKnownPoint(point). No início deste capítulo foi men-
cionadoqueoKinectpossuiumadistânciamínimaeumamáximaparaconseguir
identificaraprofundidadedeumponto.Emnossoteste,quandoamãodousuário
seaproximavamaisdoqueadistânciamínimadosensorelapassavaafazerparte
dospontoscujadistânciaosensornãoconhece.
61

## Página 67

Capítulo6
FluxodeEsqueletodoUsuário
Ofluxodeesqueletodousuárioéumfluxosemelhanteaosdemaisjáapresentados
noscapítulosanteriores,entretantonãoháumsensorfísicoqueocria. Diferente
dosoutros,estefluxoéumconjuntodeprocessamentosedesensoresquetornamo
Kinectcapazdeidentificarusuários.Otermoesqueletodeusuáriorefere-seàcapa-
cidadedoKinectqueperceberousuárioesuasarticulações,ouseja,comestefluxo
conseguimosidentificarporexemplo,ascoordenadasX,YeZdamãodousuário.
Paraefetuaroreconhecimentodediferentestiposetamanhosdeesqueletosa
Microsofttreinouumaredeneuralartificialqueprocessaasinformaçõesdoambi-
entetentandoencontraralgumusuário.DeacordocomaprópriaMicrosoftsuarede
neuralfoitreinadautilizandooconceitodeMotionCapture(mocap)dediversosti-
pos.
Estefluxoéutilizadoparacriaraplicaçõesbaseadasemmovimentos,sendoas-
sim,elepodeserconsideradoofluxomaisimportantedoKinect,poispraticamente
todaaplicaçãoutilizandooKinectéfeitabaseadaemmovimentos.

## Página 68

6.1. EsqueletodoUsuário CasadoCódigo
6.1 Esqueleto doUsuário
AsinformaçõesdousuáriosãodisponibilizadasatravésdecoordenadasX,YeZno
espaçodecoordenadasdoKinect.Comovimosnocapítuloanterior,osensorécapaz
dereconheceraté6usuáriossimultaneamente,entretanto,apenas2destesusuários
terãooesqueletodisponívelparaaaplicaç ão.
Oesqueletodousuáriocontacomvintearticulações(frequentementechamadas
deJoints),sendoquecadaumapossuisuasprópriascoordenadas. Asarticulações
sãopontosjulgadosimportanteseatravésdelesobtemosadescriç ãotridimensional
dousuário.Afigura 6.1ilustratodasasarticulaçõesquepodemserobtidasatravés
dosensor.
64

## Página 69

CasadoCódigo Capítulo6. FluxodeEsqueletodoUsuário
Figura6.1:Articulaçõesdousuário
TodasasarticulaçõesdoUsuárioestãointerligadas—essasligaçõesnocontexto
decomputaçãográficasãochamadasde ossosoubones,mesmoquealigaç ãonão
tenhaumossofísicopropriamenteditoparaligá-las.
Movimentos
Existemdoistiposdemovimentosquesãoutilizadosapartirdoesqueletodo
usuário:poses/posturasegestos.
Umapose(tambémpodeserchamadadepostura)éumaformademantero
65

## Página 70

6.2. DesenhandooEsqueletodoUsuário CasadoCódigo
corpoparadopordeterminadotempoatéqueistotenhaalgumsignificado, por
exemplo,quandoumauxiliardearbitragemnofutebolnotaqueoatacanteestáem
posiçãodeimpedimentoeleerguesuabandeiraesemantémassimatéqueoárbi-
trovejaeapliquearegra. Gestossãoosmovimentospropriamenteditos,comopor
exemplo,umacenodedespedida.
Apesardeserbastantesimplesobterinformaçõesarespeitodousuário,não
seengane,umaaplicaç ãobaseadaemmovimentosfogebastantedatrivialidade.
Lembre-sequegeralmenteénecessáriofazercomqueosmovimentossejamdetec-
tadosindependentedoesqueletodousuário,oquepodesetornarumproblema,já
queaspessoaspossuemtamanhostotalmentediferentes,tantoemtamanhototal,
quantoemtamanhodeum osso.Alémdisso,quandofalamosdegesto,hámaisum
complicador:o tempodeexecução.
6.2 Desenhando o Esqueleto doUsuário
Vamoscontinuarcomnossaaplicaç ãodoscapítulosanteriores. Agoraacrescenta-
remosimplementaçõesutilizandoofluxodeesqueleto. Nossaimplementaç ãoirá
desenharasarticulaçõeseoesqueletodousuáriosobreaimagemdacâmeraquejá
estáimplementada.
Aprimeiracoisaaserfeitaédesenharoesqueletodousuário.Nãoháummé-
todonativoquefaç aestedesenhoparanós,entãoquetalcriarmosummétodode
extensãoparaaclasse SkeletonFrame?Faremosisso,masdessavezvamosfazer
aimplementaçãoemoutrasclassesemnossaprópriaaplicaç ãoenãoemnossaDLL
AuxiliarKinect.IssoporqueodesenhoseráfeitoutilizandoobjetosWPFenão
vamosacoplarnossaDLLauxiliarnestetipodeprojeto.
Para come çar vamos criar uma classe chamada
EsqueletoUsuarioAuxiliar. Esta classe irá implementar os métodos
para desenhar o esqueleto do usuário, além disso, ela deve receber um objeto
dotipo KinectSensoremseuconstrutor,poisprecisaremosdeleparafazero
mapeamentodoesqueleto,conformeoexemplodecódigo.
public class EsqueletoUsuarioAuxiliar
{
private KinectSensor kinect;
public EsqueletoUsuarioAuxiliar(KinectSensor kinect)
{
66

## Página 71

CasadoCódigo Capítulo6. FluxodeEsqueletodoUsuário
this.kinect = kinect;
}
}
Agora precisamos criar dentro desta classe o método
ConverterCoordenadasArticulacao. Ele irá retornar as coordenadas de
uma articulação convertidas para um plano de duas dimensões. Utilizaremos
novamente o CoordinateMapper para fazer esta conversão, mas dessa vez
converteremosum SkeletonPointparaum ColorImagePoint. Estenosso
novométodoiráreceberporparâmetroaarticulaç ãocujascoordenadassedeseja
obteredoisvaloresdotipo doublequedevemconterosvaloresreferentesàaltura
elarguradocomponentedajanelaemqueiremosdesenharasarticulações.
Éimportantelembrar-sedefazerumaregradetrêsparaqueaposiç ãodaarticu-
laçãoseenquadrenotamanhodocomponentequeiremosdesenharnossoesqueleto,
estaetapapodeserignoradacasoocomponentetenhaexatamenteomesmotama-
nhodaimageminseridanoformatoda ColorStreamdoKinect,ométododeve
ficarsimilaraocódigoaseguir.
private ColorImagePoint ConverterCoordenadasArticulacao
(Joint articulacao, double larguraCanvas, double alturaCanvas)
{
ColorImagePoint posicaoArticulacao =
kinect.CoordinateMapper.MapSkeletonPointToColorPoint
(articulacao.Position, kinect.ColorStream.Format);
posicaoArticulacao.X = (int)
(posicaoArticulacao.X * larguraCanvas) /
kinect.ColorStream.FrameWidth;
posicaoArticulacao.Y = (int)
(posicaoArticulacao.Y * alturaCanvas) /
kinect.ColorStream.FrameHeight;
return posicaoArticulacao;
}
Comestemétodoprontojápodemosconverteraposiç ãodenossasarticulações,
agoraprecisamoscriarocomponentequeserádesenhadonajanela.Criaremosum
métodoquesechama CriarComponenteVisualArticulacaoparafazereste
67

## Página 72

6.2. DesenhandooEsqueletodoUsuário CasadoCódigo
trabalho.Estenovométodotambémdeveserinseridonaclassequeestamostraba-
lhando.Paraquesejapossíveldesenharasarticulaçõesemformadecírculosemum
painelWPFiremosutilizaroobjeto Ellipse,logoestemétododeveretornarum
objetodestetipo. Paraumamaiorpersonalizaç ãoiremosfazercomqueométodo
recebaporparâmetro:odiâmetrodocírculo,alarguradabordaeacorqueocírculo
serádesenhado.Afun çãodestemétodoseráutilizarestesparâmetrosparaacriaç ão
econfiguraçãodo Ellipse,conformeocódigo.
private Ellipse CriarComponenteVisualArticulacao
(int diametroArticulacao, int larguraDesenho, Brush corDesenho)
{
Ellipse objetoArticulacao = new Ellipse();
objetoArticulacao.Height = diametroArticulacao;
objetoArticulacao.Width = diametroArticulacao;
objetoArticulacao.StrokeThickness = larguraDesenho;
objetoArticulacao.Stroke = corDesenho;
return objetoArticulacao;
}
Jáconseguimosobterascoordenadasdaarticulaç ãoecriarocomponentevisual
pararepresentá-la,agoracriaremosummétodoqueutilizeestesdoiscriadosante-
riormenteparafazerodesenhodaarticulaç ãoemsuaposiç ão. Chamaremoseste
novométodode DesenharArticulacao,eledevereceberporparâmetroumob-
jeto Jointqueéarepresentaç ãodaarticulaç ãodousuárioeumobjeto Canvas
queéopainelWPFqueutilizaremosparadesenharoesqueletodousuário.
public void DesenharArticulacao
(Joint articulacao, Canvas canvasParaDesenhar)
{
int diametroArticulacao =
articulacao.JointType == JointType.Head ? 50 : 10;
int larguraDesenho = 4;
Brush corDesenho = Brushes.Red;
Ellipse objetoArticulacao =
CriarComponenteVisualArticulacao(
diametroArticulacao, larguraDesenho,
corDesenho);
68

## Página 73

CasadoCódigo Capítulo6. FluxodeEsqueletodoUsuário
ColorImagePoint posicaoArticulacao =
ConverterCoordenadasArticulacao(articulacao,
canvasParaDesenhar.ActualWidth, canvasParaDesenhar.ActualHeight);
double deslocamentoHorizontal =
posicaoArticulacao.X - objetoArticulacao.Width / 2;
double deslocamentoVertical =
(posicaoArticulacao.Y - objetoArticulacao.Height / 2);
if ( deslocamentoVertical >= 0 &&
deslocamentoVertical < canvasParaDesenhar.ActualHeight &&
deslocamentoHorizontal >= 0 &&
deslocamentoHorizontal < canvasParaDesenhar.ActualWidth )
{
Canvas.SetLeft(objetoArticulacao, deslocamentoHorizontal);
Canvas.SetTop(objetoArticulacao, deslocamentoVertical);
Canvas.SetZIndex(objetoArticulacao, 100);
canvasParaDesenhar.Children.Add(objetoArticulacao);
}
}
Agorajátemosummétodoparadesenharumaarticulaç ãodousuário,vamosfa-
zerumteste?Aprimeiracoisaaserfeitaemnossajanelaésubstituirocomponente
Imageporumcomponentedotipo Canvaserenomeá-lopara canvasKinect.
Apenascomestasubstituiç ãojáencontraremosumproblemadecompilaç ão,poiso
componente Canvasnãopossuiapropriedade Source.Nométodoqueinterpreta
oevento AllFramesReadyvamossubstituiralinhaqueatribuíaestapropriedade
docomponente Imageporumalinhaquealtereapropriedade Backgrounddo
componente Canvas.TambémfaremoscomqueoCanvaslimpeosseuscompo-
nentescadavezqueométodoéchamado,paraqueorastrodousuáriossejaapagado
eredesenhadoacadaquadro,conformecódigoaseguir.
private void kinect_AllFramesReady
(object sender, AllFramesReadyEventArgs e)
{
byte[] imagem =
ObterImagemSensorRGB(e.OpenColorImageFrame());
69

## Página 74

6.2. DesenhandooEsqueletodoUsuário CasadoCódigo
if( chkEscalaCinza.IsChecked.HasValue &&
chkEscalaCinza.IsChecked.Value)
ReconhecerDistancia(e.OpenDepthImageFrame(),
imagem, 2000);
if (imagem != null)
canvasKinect.Background = new ImageBrush(
BitmapSource.Create(kinect.ColorStream.FrameWidth,
kinect.ColorStream.FrameHeight,
96, 96, PixelFormats.Bgr32, null,
imagem,
kinect.ColorStream.FrameBytesPerPixel
* kinect.ColorStream.FrameWidth
)
);
canvasKinect.Children.Clear();
}
Apósfazerissoiremoscriarométodo DesenharEsqueletoUsuarioquere-
ceberáo SkeletonFrameporparâmetroe,assimcomoosoutrosmétodosque
utilizamoquadrodeoutrosfluxos,tambémdevemosutilizarocomando using.
Aclasse Skeletondefineaimplementaçãovirtualdoesqueletodousuário,então
iremosutilizá-laparaobteraarticulaç ãodamãodousuário.Issopodeserfeitoatra-
vésdapropriedade Joints.Estapropriedadepossuiumindexadordeacordocom
otipodaarticulaç ãoconformedescritonafigura 6.1.Agoraapenasparatestes,ire-
mosdesenharaselipsesnaposiç ãodasarticulaçõesdasmãosdousuário,conforme
ocódigo.
private void DesenharEsqueletoUsuario
(SkeletonFrame quadro)
{
if (quadro == null) return;
using (quadro)
{
Skeleton[] esqueletos =
new Skeleton[quadro.SkeletonArrayLength];
70

## Página 75

CasadoCódigo Capítulo6. FluxodeEsqueletodoUsuário
quadro.CopySkeletonDataTo(esqueletos);
IEnumerable<Skeleton> esqueletosRastreados =
esqueletos.Where( esqueleto =>
esqueleto.TrackingState ==
SkeletonTrackingState.Tracked);
if (esqueletosRastreados.Count() > 0)
{
Skeleton esqueleto =
esqueletosRastreados.First();
EsqueletoUsuarioAuxiliar funcoesEsqueletos =
new EsqueletoUsuarioAuxiliar(kinect);
funcoesEsqueletos.DesenharArticulacao(
esqueleto.Joints[JointType.HandRight],
canvasKinect );
funcoesEsqueletos.DesenharArticulacao(
esqueleto.Joints[JointType.HandLeft],
canvasKinect );
}
}
}
Parafinalizarmosprecisamosfazerachamadaparaométodoacima,apósalim-
pezadoscomponentesdoCanvas.Paraobtermosonovoquadrodoesqueletoque
iremosenviarporparâmetroprecisamosutilizar e.OpenSkeletonFrame()no
métodoqueinterpretaoeventodetodososquadros. Comestasimplementações
prontas,jápodemosobterresultadosconformeafigura 6.2.
71

## Página 76

6.2. DesenhandooEsqueletodoUsuário CasadoCódigo
Figura6.2:Desenhandoaarticulaç ãodasmãos
Nesteponto,játemosrecursosparadesenhartodasasarticulaçõesdousuá-
rio, mas iremos adicionar na classeEsqueletoUsuarioAuxiliar a funcio-
nalidadeparadesenharos ossosentreasarticulações. Vamosfazê-laatravésde
doismétodos: DesenharOssoe CriarComponenteVisualOsso. Ométodo
CriarComponenteVisualOssodeveretornarumobjetodotipo Lineerece-
berporparâmetroalarguraecordalinhaqueiremosutilizarparadesenhá-laeas
coordenadasXeYdasarticulaçõesdedestinoeorigem,conformeoexemplo.
private Line CriarComponenteVisualOsso
(int larguraDesenho, Brush corDesenho,
double origemX, double origemY, double destinoX, double destinoY)
{
Line objetoOsso = new Line();
objetoOsso.StrokeThickness = larguraDesenho;
objetoOsso.Stroke = corDesenho;
72

## Página 77

CasadoCódigo Capítulo6. FluxodeEsqueletodoUsuário
objetoOsso.X1 = origemX;
objetoOsso.X2 = destinoX;
objetoOsso.Y1 = origemY;
objetoOsso.Y2 = destinoY;
return objetoOsso;
}
Agoratemosquecriarométodo DesenharOsso,eleutilizaráduasarticulações
paracriarumossoentreelaseinseri-lonoCanvas.Alógicadestemétodoébastante
similaraométodo DesenharArticulacao,poisteremosqueconverterascoorde-
nadas3Ddasduasarticulaçõesparaumplano2Dutilizandoo CoordinateMapper
eusaremosométododescritoanteriormenteparacriaroobjeto Linequeseráadi-
cionadoaoCanvas.Oresultadodevesersimilaraocódigoaseguir.
public void DesenharOsso
(Joint articulacaoOrigem, Joint articulacaoDestino,
Canvas canvasParaDesenhar)
{
int larguraDesenho = 4;
Brush corDesenho = Brushes.Green;
ColorImagePoint posicaoArticulacaoOrigem =
ConverterCoordenadasArticulacao(
articulacaoOrigem,
canvasParaDesenhar.ActualWidth,
canvasParaDesenhar.ActualHeight);
ColorImagePoint posicaoArticulacaoDestino =
ConverterCoordenadasArticulacao(
articulacaoDestino,
canvasParaDesenhar.ActualWidth,
canvasParaDesenhar.ActualHeight);
Line objetoOsso =
CriarComponenteVisualOsso(larguraDesenho, corDesenho,
posicaoArticulacaoOrigem.X, posicaoArticulacaoOrigem.Y,
posicaoArticulacaoDestino.X, posicaoArticulacaoDestino.Y);
73

## Página 78

6.2. DesenhandooEsqueletodoUsuário CasadoCódigo
if (Math.Max(objetoOsso.X1, objetoOsso.X2) <
canvasParaDesenhar.ActualWidth &&
Math.Min(objetoOsso.X1, objetoOsso.X2) > 0 &&
Math.Max(objetoOsso.Y1, objetoOsso.Y2) <
canvasParaDesenhar.ActualHeight &&
Math.Min(objetoOsso.Y1, objetoOsso.Y2) > 0)
canvasParaDesenhar.Children.Add(objetoOsso);
}
Agora sim, temos todos os métodos preparados. O próximo passo é criar
uma nova classe no namespace Auxiliar chamadaExtensao. Ela irá utilizar
osmétodosquepreparamosacimaparacriarummétododeextensãonaclasse
SkeletonFrameparadesenharoesqueletodousuárioemumCanvasdeforma
coerente.
Métodos deExtensão
NalinguagemC# épossívelcriarmétodosdeextensão.Estesméto-
dossãoumtipoespecialdemétodosestáticosquepermitemaodesen-
volvedoradicionarfuncionalidadesemumtipoexistentesemquevocê
crieumtipoderivado,recompileoumodifiqueocódigooriginal.Esteé
umrecursopoderosoebastanteutilizadonestalinguagem,nãocabeao
escopodestelivrodefinirtodasaspossibilidades.
Para mais informações visite o link:http://msdn.microsoft.com/
en-us/library/vstudio/bb383977.aspx
Para que a classeExtensao possa criar métodos de extensão para ou-
tros tipos é necessário que ela seja declarada como estática — para isso,
utilize a palavra reservada static. Nesta classe iremos declarar o mé-
todo estático DesenharEsqueletoUsuario para servir de extensão para a
classe SkeletonFrame. Estemétododevereceberviaparâmetrososensor(
KinectSensor)queeleutilizaráparamapearoesqueletoeocanvas( Canvas)
emqueoesqueletodeveserdesenhado,além,éclaro,dopróprioobjetodeextensão.
Paradeclararoobjetoqueseráestendidovocêdeveincluí-locomoprimeiropa-
râmetroantecedidopelapalavrareservada this.Destaforma,estemétodoseráum
métododeextensãodeumainstânciadaclasse SkeletonFrame.Paragarantirque
74

## Página 79

CasadoCódigo Capítulo6. FluxodeEsqueletodoUsuário
nãohaveráparâmetrosinválidos,énecessáriofazerumavalidaç ãonosparâmetros
informadosnométodo.
Caso todas as validações sejam cumpridas, iremos utilizar a lógica defi-
nida para obter o esqueleto do usuário no teste anterior e utilizar nossa classe
EsqueletoUsuarioAuxiliarparaprimeiramentedesenhartodasasarticula-
çõessemosossos,seumétododeveficarsimilaraocódigoseguinte.
public static void DesenharEsqueletoUsuario
( this SkeletonFrame quadro,
KinectSensor kinectSensor,
Canvas canvasParaDesenhar )
{
if (kinectSensor == null)
throw new ArgumentNullException("kinectSensor");
if (canvasParaDesenhar == null)
throw new ArgumentNullException("canvasParaDesenhar");
Skeleton[] esqueletos =
new Skeleton[quadro.SkeletonArrayLength];
quadro.CopySkeletonDataTo(esqueletos);
IEnumerable<Skeleton> esqueletosRastreados =
esqueletos.Where( esqueleto =>
esqueleto.TrackingState ==
SkeletonTrackingState.Tracked);
if (esqueletosRastreados.Count() > 0)
{
Skeleton esqueleto =
esqueletosRastreados.First();
EsqueletoUsuarioAuxiliar esqueletoUsuarioAuxiliar =
new EsqueletoUsuarioAuxiliar(kinectSensor);
foreach (Joint articulacao in esqueleto.Joints)
esqueletoUsuarioAuxiliar
.DesenharArticulacao(articulacao, canvasParaDesenhar);
}
75

## Página 80

6.2. DesenhandooEsqueletodoUsuário CasadoCódigo
Estemétodoficoubastantesimilaraoquejáhavíamoscriadoemnossajanela,
masalémdepassarmosalógicaparaummétododeextensão,podemosmelhorar
separandoalógicaempartes.Obteroesqueletodoprimeirousuárioéumatarefaco-
mumebastanteutilizada,entãocriaremosmaisummétododeextensão,que,dessa
vez,retornaráoesqueletodoprimeirousuáriodosensor.Parafazerisso,bastautili-
zarmosalógicajáfeitanométododescritoanteriormente.
public static Skeleton ObterEsqueletoUsuario
(this SkeletonFrame quadro)
{
Skeleton esqueletoUsuario = null;
Skeleton[] esqueletos =
new Skeleton[quadro.SkeletonArrayLength];
quadro.CopySkeletonDataTo(esqueletos);
IEnumerable<Skeleton> esqueletosRastreados =
esqueletos.Where( esqueleto =>
esqueleto.TrackingState ==
SkeletonTrackingState.Tracked);
if (esqueletosRastreados.Count() > 0)
esqueletoUsuario =
esqueletosRastreados.First();
return esqueletoUsuario;
}
Agora,iremosalterarométodo DesenharEsqueletoUsuarioparaqueele
reaproveiteestemétodo,demodoque,quandoprecisarmossomentedoesqueleto
dousuáriosemdesenhá-lo,podemosobtê-loatravésdométododestemétodode
extensão.
public static void DesenharEsqueletoUsuario
( this SkeletonFrame quadro,
KinectSensor kinectSensor,
Canvas canvasParaDesenhar )
{
if (kinectSensor == null)
throw new ArgumentNullException("kinectSensor");
76

## Página 81

CasadoCódigo Capítulo6. FluxodeEsqueletodoUsuário
if (canvasParaDesenhar == null)
throw new ArgumentNullException("canvasParaDesenhar");
Skeleton esqueleto = ObterEsqueletoUsuario(quadro);
if (esqueleto != null)
{
EsqueletoUsuarioAuxiliar esqueletoUsuarioAuxiliar =
new EsqueletoUsuarioAuxiliar(kinectSensor);
foreach (Joint articulacao in esqueleto.Joints)
esqueletoUsuarioAuxiliar
.DesenharArticulacao(articulacao, canvasParaDesenhar);
}
Agoraprecisamosatualizarométodo DesenharEsqueletoUsuariodenossa
janela.Todaalógicaparaobteroesqueletodousuáriojáfoitransferidaparaosmé-
todosmostradosanteriormente,entãonãoémaisnecessáriomantê-lanocódigoda
janela,bastaquedentrodobloco usingutilizemosométododeextensão,conforme
oexemplo.
private void DesenharEsqueletoUsuario(SkeletonFrame quadro)
{
if (quadro == null) return;
using (quadro)
quadro.DesenharEsqueletoUsuario(kinect, canvasKinect);
}
Notequeretiramostodaacomplexidadedestemétodoeencapsulamosemum
métododeextensão,agoraficarámuitomaisfácildesenharoesqueletosempreque
fornecessário. Sevocêexecutaraaplicação,veráquetodasasarticulaçõesjásão
exibidasequeaarticulaç ãodacabe çapossuiumdiâmetrobemmaiorqueasoutras,
conformeilustraafigura 6.3
77

## Página 82

6.2. DesenhandooEsqueletodoUsuário CasadoCódigo
Figura6.3:Desenhandotodasasarticulações
Comopodemosnotarnaimagemacimajáépossívelterumaboano çãodecomo
ficaránossoresultado,agoraparafinalizarmosestafuncionalidadeprecisamosde-
senhartodososossosdoesqueleto.Antesdefazermosisso,éprecisosaberquehá
umahierarquiacoerenteentreasarticulações.Essahierarquiadefinearelaç ãoentre
asarticulações,porexemplo,aarticulaç ãodacabe çaestárelacionadaaarticulaç ão
docentrodosombros,queporsuavezestárelacionadacomoombrodireitoees-
querdoeassimpordiante.Afigura 6.4ilustraestahierarquia.
78

## Página 83

CasadoCódigo Capítulo6. FluxodeEsqueletodoUsuário
Figura6.4:Hierarquiadosossos
Atravésdestahierarquiatambémconseguimosobterinformaçõessobreare-
laçãodasarticulações, comoporexemplo, arotaç ãodeumaarticulaç ãoemre-
laçãoaoutra. Paraacessarmosestasinformaçõesdevemosutilizarapropriedade
BoneOrientationsdaclasse Skeleton,estapropriedadeéumacole çãodeob-
jetosdotipo BoneOrientation. Utilizaremosesteobjetoparaobtermosaarti-
culaçãoinicialefinaldecadaossodenossoesqueleto,entãopodemosalterarolaço
derepetiçãodonossométododeextensãoparapercorreracole çãodeossos.Dessa
forma,teremosasinformaçõessobreosossosesobreasarticula ções,fazendoode-
senhocompletodoesqueletodousuário,deacordocomocódigoabaixo.
public static void DesenharEsqueletoUsuario
( this SkeletonFrame quadro,
79

## Página 84

6.2. DesenhandooEsqueletodoUsuário CasadoCódigo
KinectSensor kinectSensor,
Canvas canvasParaDesenhar )
{
if (kinectSensor == null)
throw new ArgumentNullException("kinectSensor");
if (canvasParaDesenhar == null)
throw new ArgumentNullException("canvasParaDesenhar");
Skeleton esqueleto = ObterEsqueletoUsuario(quadro);
if (esqueleto != null)
{
EsqueletoUsuarioAuxiliar esqueletoUsuarioAuxiliar =
new EsqueletoUsuarioAuxiliar(kinectSensor);
foreach (BoneOrientation osso in esqueleto.BoneOrientations)
{
esqueletoUsuarioAuxiliar
.DesenharOsso(esqueleto.Joints[osso.StartJoint],
esqueleto.Joints[osso.EndJoint],
canvasParaDesenhar);
esqueletoUsuarioAuxiliar
.DesenharArticulacao
(esqueleto.Joints[osso.EndJoint], canvasParaDesenhar);
}
}
Enfimtemosoresultadoesperado. Oesqueletojápodeserdesenhadototal-
mentecomumasimpleschamadaaométododeextensão,oresultadoéilustrado
pelafigura 6.5.
80

## Página 85

CasadoCódigo Capítulo6. FluxodeEsqueletodoUsuário
Figura6.5:Desenhandooesqueletodousuário
Agoravamoscriarumnovo CheckBoxparaidentificarquandooesqueletodo
usuáriodeveserdesenhado.Emnossajanelairemosagruparo CheckBoxjáexis-
tenteparaaplicarofiltrodeescalacinzaemum StackPanel.OtrechodeXAML
desuajaneladeveficarsimilaraeste:
<StackPanel Grid.Row="2" Orientation="Horizontal">
<CheckBox Name="chkEscalaCinza"
Content="Escala cinza" Margin="10,10,0,10"
HorizontalAlignment="Left" />
<CheckBox Name="chkEsqueleto"
Content="Esqueleto do Usuário"
HorizontalAlignment="Left"
Margin="10,10,0,10"/>
</StackPanel>
Alémdeinserirocomponentenajanela,tambéménecessáriofazeravalidaç ão
81

## Página 86

6.2. DesenhandooEsqueletodoUsuário CasadoCódigo
deste CheckBoxantesdeutilizarométodoparadesenharoesqueleto,entãonosso
métodoqueinterpretaoevento AllFramesReadydeveficarassim:
private void kinect_AllFramesReady
(object sender, AllFramesReadyEventArgs e)
{
byte[] imagem = ObterImagemSensorRGB(e.OpenColorImageFrame());
if( chkEscalaCinza.IsChecked.HasValue &&
chkEscalaCinza.IsChecked.Value )
ReconhecerDistancia(e.OpenDepthImageFrame(),
imagem, 2000);
if (imagem != null)
canvasKinect.Background = new ImageBrush(
BitmapSource
.Create( kinect.ColorStream.FrameWidth,
kinect.ColorStream.FrameHeight,
96, 96, PixelFormats.Bgr32, null,
imagem,
kinect.ColorStream.FrameBytesPerPixel
* kinect.ColorStream.FrameWidth
)
);
canvasKinect.Children.Clear();
if ( chkEsqueleto.IsChecked.HasValue &&
chkEsqueleto.IsChecked.Value )
DesenharEsqueletoUsuario(e.OpenSkeletonFrame());
}
Feitoisso,porpadrãovisualizaremosapenasaimagemdacâmeradoKinecte
temosaop çãodemarcaro CheckBox“EsqueletodoUsuário”paraquandodese-
jarmosvisualizaroesqueletodousuário.
82

## Página 87

Capítulo7
RastreandoeIdentificando
Movimentos
Nestecapítulocontinuaremosautilizarofluxodeesqueletocomonocapítuloante-
rior,masdessavezfocaremosnainteraç ãocomoaplicativoatravésdemovimentos.
Estemétododeinteraç ãopodetrazerumagrandeexperiênciaaousuário,porém
temosdelevaremconsideraç ãoqueháalgunsdesafiosparaimplementarumaboa
usabilidadecomnossosmovimentos. Éimportanteparaousuárioqueosmovi-
mentostenhamdificuldadesdeacordocomseucontexto,porexemplo,emumjogo
podeserqueummovimentocomplicadofaç apartedodesafio,porémseousuário
estáutilizandomovimentosparanavegaremumaplicativoouacionaratalhos,eles
devemserfáceisenaturais.
Osmovimentosprecisamserbemdiferenciados,evitecriarmovimentossimila-
rescomfuncionalidadesdiferentes,poisainterpretaç ãodemovimentosestásujeita
aerroseéfrustranteparaaexperiênciadousuárioacionarumafuncionalidadepor
acasoaotentarexecutaroutra.

## Página 88

7.1. IniciandoaEstruturaBaseparaDetectarMovimentos CasadoCódigo
Éimportanteconheceropúblicoalvodesuaaplicaç ãoeénecessáriotomarpre-
cauçõesquantoaotamanhodoesqueletodecadausuárioeotamanhodoossoentre
asarticula çõesdecadausuário. Procuresemprefazercomparaçõesproporcionais
aopróprioesqueleto,dessaformaainterpretaç ãodogestosemantémconsistente
independentedotamanhodoesqueleto.
Testareexperimentaréfundamentalquandosefaladeaplicaçõesvoltadasain-
terfacesnaturais. Vocêpodedesenvolverumaaplicaç ãobaseadaemmovimentos
quefuncionaperfeitamenteparavocê,masquenãoatendeseupúblicoalvo,por-
tantoprocurefazertestes,avaliarereimplementarquantasvezesforemnecessárioa
fimdemelhorarcadavezmaisaexperiênciadousuário.
Aideiaprincipaldaimplementaç ãodocapítuloanterioréqueousuáriovisua-
lizeseuesqueletoapenasquandodesejar,issoéumaboaideia,masháumproblema
deusabilidadeemnossaimplementaç ão.Quandoousuárioestiversevendonoví-
deoexibidopornossaaplicaç ão,elepoderáestarlongedeseucomputadoreisso
iráimpossibilitá-lodevisualizarseuesqueletonaquelemomento.Estemesmopro-
blematambémpodeseraplicadoparaquandoousuáriodesejaaplicarofiltrode
escalacinza.
Pararesolvermosissoiremosimplementarorastreamentoeaidentificaç ãode
movimentosparaacionaratalhos,oquepodeserbastantetrabalhoso,masmonta-
remosumaestruturanaDLL AuxiliarKinectparanosajudar.
7.1 Iniciando aEstrutura Base paraDetectarMovi-
mentos
Primeiro vamos criar uma nova pasta no projetoAuxiliarKinectchamada
Movimentos. Nelaserãocriadastodasasclassesligadasàlógicapararastreare
identificarasposesegestosquedesenvolveremosaolongodestelivro.
Todososmovimentosemnossaaplicaç ãopoderãoestaremumdostrêsesta-
dosderastreamento:nãoidentificado,emexecuç ãoeidentificado.Parapodermos
teressesvaloresemnossaaplicaç ãoiremoscriarumarquivocomaenumeraç ão
EstadoRastreamento,conformeocódigoaseguir.
public enum EstadoRastreamento
{
NaoIdentificado,
EmExecucao,
84

## Página 89

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
Identificado
}
Apósisso,criaremosaprimeiraclassequesechamará Movimento,elaseráuma
classebaseparatodososmovimentos(posesegestos)denossaaplicaç ão.Estaclasse
deveserabstrataepossuiraspropriedadesemétodosquetodotipodemovimento
tem.Todoequalquertipodemovimentoenvolvetempodeexecuç ão,sendoassim,
énecessárioqueaclasse Movimentotenhaumcontadorparaquadrosemqueo
movimentoestáemexecuç ão. Alémdisso,eledeveconterumnomeedevepos-
suirmétodosquepermitamvalidarseaposiç ãodousuárioestádeacordocomo
movimentoqueeleestátentandoexecutar.Aclassedeveficarsimilaràabaixo:
public abstract class Movimento
{
protected int ContadorQuadros { get; set; }
public string Nome { get; set; }
public abstract EstadoRastreamento Rastrear(
Skeleton esqueletoUsuario);
protected abstract bool PosicaoValida(
Skeleton esqueletoUsuario);
}
Paraqueumaposetenhavalidadeénecessárioqueelaestejasendofeitaporum
períododetempo. Aetapaqueavaliaaposeaolongodotempochama-se rastre-
amentoeaetapaqueocorrequandoaposeéreconhecidacomoválidachama-se
identificação.
Agoracriaremosaclasseabstrataquedeveráserutilizadacomobaseparato-
dasasposesdenossaaplicaç ão. Eladeveráserchamadade Poseedeveherdara
classe Movimento,bemcomopossuirapropriedadequemarcaemqualframea
poseéreconhecidaeaimplementaç ãodométodo Rastrearherdadopelaclasse
Movimento.Masporenquantodeixaremosométodo Rastrearembrancoevol-
taremosaquimaistarde.
public abstract class Pose : Movimento
{
protected int QuadroIdentificacao { get; set; }
public override EstadoRastreamento Rastrear(
85

## Página 90

7.1. IniciandoaEstruturaBaseparaDetectarMovimentos CasadoCódigo
Skeleton esqueletoUsuario)
{
}
}
Alémdasclassesbasesparaosmovimentostambémprecisamosdeumaclasse
queirárastreareidentificarasposes,entãononamespace Movimentoscriaremos
ainterface IRastreadoreaclasse Rastreador.
Ainterface IRastreadordeveserimplementadaportodososrastreadores.
Emseucorpodeveserdefinidoométodo Rastrear,querecebeporparâmetroo
esqueletodousuárioenãoprecisaretornarnenhumtipodevalor,eapropriedade
EstadoAtual,quedevesersomenteleitura.
public interface IRastreador
{
void Rastrear(Skeleton esqueletoUsuario);
EstadoRastreamento EstadoAtual { get; }
}
Aclasse Rastreadoriráfazerorastreamentodeumdeterminadomovimento,
sejaeleposeougesto,implementandoométodo Rastreardainterfacecriadaante-
riormente.Paraconfigurarmosquetipodeposeougestoiremosrastrearénecessária
autilizaçãode generics.
Generics
GenericséumafuncionalidadedalinguagemC# quepermiteaode-
senvolvedorcriarumdesigndeclassesquepodemaplicarfuncionali-
dadesaumdeterminadotipoqueserádefinidoapenasnaaplicaç ãofi-
nal.Classesgenéricasmaximizambastanteareutilizaç ãodecódigo,um
exemplodeutilizaçãoéacole çãoList<T>,ondeTpodeserumtipoqual-
quer.Dessaforma,épossívelcriarlistasdequalquertipodeobjetoeela
teráosmesmosmétodos.Paramaisinformaçõesacesse:
http://msdn.microsoft.com/en-us/library/512aeb7t
Apesardeusargenerics,nossaclasse Rastreadordeverastrearapenasobjetos
queherdemdaclasse Movimentoequesejamobjetosconcretos.Podemosdefinir
86

## Página 91

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
issonaprópriadeclaraç ãodaclasseutilizandoapalavrareservada whereedefi-
nindoascondiçõesdesejadas,conformeocódigo.
public class Rastreador<T> : IRastreador where T : Movimento, new()
{
}
Comestecabe çalhodefinimosqueaclasse Rastreadorpodeserutilizadacom
umtipogenérico,queelaimplementaainterface IRastreadorequeelapermite
somentetiposqueherdemaclasse Movimentoequepossuemumconstrutor.Inter-
namente,nossoconstrutorterádeterumatributoprivadoparacontrolaropróprio
objetoreferenteaomovimentoqueestásendorastreado.Alémdisso,precisaremos
criarumeventoparaquandoomovimentoéreconhecidoeoutroparanotificaro
progressodorastreamento. Noconstrutorpadrãodestaclasseiremosinicializaro
objetoquearmazenaomovimentoqueserárastreado.
public class Rastreador<T> where T : Movimento, new()
{
private T movimento;
public EstadoRastreamento EstadoAtual { get; private set; }
public event EventHandler MovimentoIdentificado;
public event EventHandler MovimentoEmProgresso;
public Rastreador()
{
EstadoAtual = EstadoRastreamento.NaoIdentificado;
movimento = Activator.CreateInstance<T>();
}
}
Aclasse Activatoréutilizadaparainvocaroconstrutordotipodefinidocomo
genéricodenossaclasse(existemformasmaisperformáticas,masporsimplicidade
utilizaremosestanoexemplo).Parafinalizaraimplementaç ãodenossorastreador
iremosimplementarométodo Rastreardainterfaceeneleiremosverificaratravés
dométodo Rastreardaclasse Movimentoseomesmofoiidentificadoouestá
emprogresso. Deacordocomoestadodorastreamento,chamaremososeventos.
Nãoesque çaqueénecessárioverificarseoeventoestánuloantesdechamá-lo. O
códigofinaldestaclassedeveficarsemelhanteaocódigoaseguir.
public class Rastreador<T> : IRastreador where T : Movimento, new()
{
87

## Página 92

7.1. IniciandoaEstruturaBaseparaDetectarMovimentos CasadoCódigo
private T movimento;
public EstadoRastreamento EstadoAtual { get; private set; }
public event EventHandler MovimentoIdentificado;
public event EventHandler MovimentoEmProgresso;
public Rastreador()
{
EstadoAtual = EstadoRastreamento.NaoIdentificado;
movimento = Activator.CreateInstance<T>();
}
public void Rastrear(Skeleton esqueletoUsuario)
{
EstadoRastreamento novoEstado =
movimento.Rastrear(esqueletoUsuario);
if (novoEstado == EstadoRastreamento.Identificado &&
EstadoAtual != EstadoRastreamento.Identificado)
ChamarEvento(MovimentoIdentificado);
if (novoEstado == EstadoRastreamento.EmExecucao &&
(EstadoAtual == EstadoRastreamento.EmExecucao ||
EstadoAtual == EstadoRastreamento.NaoIdentificado))
ChamarEvento(MovimentoEmProgresso);
EstadoAtual = novoEstado;
}
private void ChamarEvento(EventHandler evento)
{
if (evento != null)
evento(movimento, new EventArgs());
}
}
Comisso,nossaestruturabásicaparaposesjáestápronta,voltaremosmaistarde
paraimplementarapartedegestosdenossaestrutura,agoravamosimplementaras
posesquedefatoserãorastreadas.
88

## Página 93

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
7.2 UtilizandoPoses em NossaAplicação
Aprimeiraposequeiremoscriaréumaposesimples,conhecidacomo“T”.Esta
poseconsisteemmanterosdoisbraçosesticadosparaosladosemalturaparalela
aosombros,fazendocomqueoformatodoesqueletodousuárioseassemelhecom
aletra“T”(motivodonomedapose).
Agorairemoscriarumanovapastachamada Poses,quedeveficardentroda
pasta Movimentoseneladevemserinseridastodasasclassesreferentesaposes
interpretadaspornossaaplicaç ão.Nelairemosincluiraclasse PoseT,lembre-sede
queaclasse PoseTdeveserumaclasseconcretaeherdaraclasse Pose.
Noconstrutordaclasse PoseTjápodemosinserirosvaloresnasproprieda-
des Nomee QuadroIdentificacao—nesteexemploutilizerespectivamenteos
valores“PoseT”e10.Quandovocêincluiuaherançadaclasse Posevocêtornoune-
cessárioqueaclasse PoseTimplementeasobrescritadométodo PosicalValida
(nãoénecessáriosobrescreverométodo Rastrearpoisestejáfoisobrescritona
classe Pose).Nessemomentosuaclassedeveestarsemelhanteàclasseaseguir.
public class PoseT : Pose
{
public PoseT()
{
this.Nome = "PoseT";
this.QuadroIdentificacao = 10;
}
protected override bool PosicaoValida(Skeleton esqueletoUsuario)
{
}
}
Precisamosagoraimplementarestesmétodos,masantesdecome çarmoséim-
portanteteremmentequeascomparaçõesentreasarticulaçõesnãodevemserfei-
tasdeformaexata,ouseja,éinviávelexigiraousuárioqueasposiçõessejamexa-
tamenteiguais. Pararesolverissodevemosutilizarumamargemdeerronacom-
paraçãodosvaloresentrequaisquerposições. Antesdeimplementarométodo
PosicaoValidairemoscriarumanovaclasseestáticachamada Utilnonames-
pace FuncoesBasicas.Aclasse Utilseráutilizadaparafazeroperaçõescomuns,
comoporexemplo,acomparaç ãoutilizandomargemdeerro.
89

## Página 94

7.2. UtilizandoPosesemNossaAplicação CasadoCódigo
Apóscriaraclasse Utilcriaremosométodo CompararComMargemErroque
devereceberporparâmetrotrêsvaloresdotipo double,umvalorparaserutilizado
comomargemdeerroeosdoisvaloresqueserãocomparados.Segueaimplemen-
taçãodestaclasse.
public static class Util
{
public static bool CompararComMargemErro
(double margemErro, double valor1, double valor2)
{
return valor1 >= valor2 - margemErro &&
valor1 <= valor2 + margemErro;
}
}
Podemosvoltaragoraparanossaclasse PoseTefinalmenteimplementaromé-
todo PosicaoValida.Estemétododeveutilizarasarticulaçõesdoesqueletodo
usuárioqueérecebidoporparâmetroparavalidarseousuárioestánaposiç ãorela-
tivaàposeemquestão,nestecaso,apose“T”.
Navalidaçãodestaposedevemoscompararaaltura(eixoY)eadistância(eixo
Z)dasmãosedoscotovelosemrelaç ãoaocentrodosombroseseoeixoXdas
mãosestãomaisdistantesdeseurespectivocotovelo.Todasessascomparaçõesque
envolvemigualdadedevemutilizarmargemdeerro—nestecasoutilizaremoscomo
margemdeerroovalor0.30,masvocêpodeajustá-loconformesuanecessidadede
precisão,conformeocódigo.
protected override bool PosicaoValida
(Skeleton esqueletoUsuario)
{
Joint centroOmbros =
esqueletoUsuario.Joints[JointType.ShoulderCenter];
Joint maoDireita =
esqueletoUsuario.Joints[JointType.HandRight];
Joint cotoveloDireito =
esqueletoUsuario.Joints[JointType.ElbowRight];
Joint maoEsquerda =
esqueletoUsuario.Joints[JointType.HandLeft];
90

## Página 95

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
Joint cotoveloEsquerdo =
esqueletoUsuario.Joints[JointType.ElbowLeft];
double margemErro = 0.30;
bool maoDireitaAlturaCorreta =
Util.CompararComMargemErro(margemErro,
maoDireita.Position.Y, centroOmbros.Position.Y);
bool maoDireitaDistanciaCorreta =
Util.CompararComMargemErro(margemErro,
maoDireita.Position.Z, centroOmbros.Position.Z);
bool maoDireitaAposCotovelo =
maoDireita.Position.X > cotoveloDireito.Position.X;
bool cotoveloDireitoAlturaCorreta =
Util.CompararComMargemErro(margemErro,
cotoveloDireito.Position.Y, centroOmbros.Position.Y);
bool cotoveloEsquerdoAlturaCorreta =
Util.CompararComMargemErro(margemErro,
cotoveloEsquerdo.Position.Y, centroOmbros.Position.Y);
bool maoEsquerdaAlturaCorreta =
Util.CompararComMargemErro(margemErro,
maoEsquerda.Position.Y, centroOmbros.Position.Y);
bool maoEsquerdaDistanciaCorreta =
Util.CompararComMargemErro(margemErro,
maoEsquerda.Position.Z, centroOmbros.Position.Z);
bool maoEsquerdaAposCotovelo =
maoEsquerda.Position.X < cotoveloEsquerdo.Position.X;
return maoDireitaAlturaCorreta &&
maoDireitaDistanciaCorreta &&
maoDireitaAposCotovelo &&
cotoveloDireitoAlturaCorreta &&
maoEsquerdaAlturaCorreta &&
91

## Página 96

7.2. UtilizandoPosesemNossaAplicação CasadoCódigo
maoEsquerdaDistanciaCorreta &&
maoEsquerdaAposCotovelo &&
cotoveloEsquerdoAlturaCorreta;
}
Comestemétodoimplementadojáconseguimosvalidarsenossousuárioestáou
nãonaposi çãocorretaemrelaç ãoàpose“T”,masaindaprecisamosimplementaro
método Rastrearnaclasse Pose.Estemétododeveverificarseousuárioestána
posecorretadeacordocomométodo PosicaoValidaeretornaroestadodapose
deacordocomonúmerodequadrosqueousuárioestánaposiç ãocorreta.
Alógicaparaidentificaç ãodetodasasposeséigual,porestemotivooptou-se
porimplementarométodo Rastrearnaclassebasedetodasasposes. Éneces-
sárioverificarseoesqueletodousuárioaindaestásendorastreadoeseaposiç ão
emqueeleestáéválidaparaaposequeestamosrastreando.Comojámencionado
issopodeserfeitoatravésdenossométodo PosicaoValida.Casoousuárioes-
tejaemumaposiç ãoválida,énecessáriovalidartambémonúmerodequadrosem
queeleestánestaposiç ão;seonúmerodequadrosjáatingiuonúmerodefinido
napropriedade QuadroIdentificacao,oestadodaclassedeveseralteradopara
Identificado;casoaindanãotenhaatingido,oestadodaclassedeveseralterado
para EmExecucaoeocontadordeveserincrementado.Seaposiç ãodousuárionão
forválidanaprimeiracondiç ãooestadodaposedeveser NaoIdentificadoeo
contadordequadrosdevezerar.
public override EstadoRastreamento Rastrear
(Skeleton esqueletoUsuario)
{
EstadoRastreamento novoEstado;
if ( esqueletoUsuario != null &&
PosicaoValida(esqueletoUsuario) )
{
if (QuadroIdentificacao == ContadorQuadros)
novoEstado = EstadoRastreamento.Identificado;
else
{
novoEstado = EstadoRastreamento.EmExecucao;
ContadorQuadros += 1;
}
}
else
92

## Página 97

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
{
novoEstado = EstadoRastreamento.NaoIdentificado;
ContadorQuadros = 0;
}
return novoEstado;
}
Por fim, criaremos uma propriedade que contenha o percentual de pro-
gresso de nossa pose de acordo com as propriedadesContadorQuadros e
QuadroIdentificacao,conformeocódigo.
public int PercentualProgresso
{
get
{
return ContadorQuadros * 100 / QuadroIdentificacao;
}
}
Agorajápodemoscompilaresteprojetoeretornarparanossajanelaparafazer
usodestecódigo!
Damesmaformaquecriamosumatributonajanelaparacontrolarokinectem
todososmétodosfaremosissocriandoumobjetodotipo List<IRastreador>,
queconterátodososrastreadoresdemovimentosqueserãoexecutados. Iremos
criarummétodoemnossajanelachamado InicializarRastreadores. Ele
deveinicializarosrastreadoresdenossajanela(porenquantosóhaveráum)edefi-
nirométodoqueseráchamadonodisparodoevento MovimentoIdentificado
e MovimentoEmProgresso,quandohouver. Nestecaso,ométodoqueserádis-
paradoquandoomovimentoforidentificadoapenasdevealterarapropriedade
IsCheckeddenosso CheckBoxrelacionadoaoesqueletodousuário. Aimple-
mentaçãodessasfuncionalidadesdeveseguirconformeoseguintecódigo.
private void InicializarRastreadores()
{
rastreadores = new List<IRastreador>();
Rastreador<PoseT> rastreadorPoseT = new Rastreador<PoseT>();
rastreadorPoseT.MovimentoIdentificado += PoseTIdentificada;
rastreadores.Add(rastreadorPoseT);
93

## Página 98

7.2. UtilizandoPosesemNossaAplicação CasadoCódigo
}
private void PoseTIdentificada(object sender, EventArgs e)
{
chkEsqueleto.IsChecked = !chkEsqueleto.IsChecked;
}
Noteque,quandocriamosumobjetodotipo Rastreador,jádefinimosqual
omovimentoqueeleirárastrearatravésdousodegenerics. Apesardotrechode
códigoacimanãoilustrar,énecessárioquevocêdefinaoobjeto rastreadoresno
escopodaclasseequechameométodo InicializarRastreadoresnocons-
trutordajanela.
Agoravocêdeverenomearométodo DesenharEsqueletoUsuariopara
FuncoesEsqueletoUsuario,poiseletambémiráfazerorastreamentodosmo-
vimentosdefinidosemnossalista.Dentrodobloco usingdestemétododevemos
chamarométododeextensãoparaobtermosoprimeiroesqueletoepercorreralista
rastreadorespassando-oporparâmetroaométodo Rastrear.Apósissojápode-
remostestarorastreamentodenossosmovimentos.
private void DesenharEsqueletoUsuario(SkeletonFrame quadro)
{
if (quadro == null) return;
using (quadro)
{
Skeleton esqueletoUsuario =
quadro.ObterEsqueletoUsuario();
foreach (IRastreador rastreador in rastreadores)
rastreador.Rastrear(esqueletoUsuario);
if ( chkEsqueleto.IsChecked.HasValue &&
chkEsqueleto.IsChecked.Value )
quadro.DesenharEsqueletoUsuario(kinect, canvasKinect);
}
}
Agoravocêjádeveconseguirutilizarapose“T”paraativaroudesativaravisu-
alizaçãodoesqueletodousuário,conformeilustraafigura 7.1
94

## Página 99

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
Figura7.1:IdentificandoPoseT
Comtodaaestruturapararastreamentodeposesprontaficamuitomaisfácil
criaraidentificaç ãodeumanovapose.Implementaremosumanovaposeparaque
possamosalteraraop çãoparaexibiraimagememescalacinzasemprecisarmos
tocarnocomputador.Aposeemquestãoécomumenteutilizadaparapausarjogos
noXbox,masnossocasoelairáservirparaalternarentreimagemcomumeescala
cinza,chamaremosestaposede“pause”,ousuáriodeveficarnaposiçãoilustradana
figura7.2.
95

## Página 100

7.2. UtilizandoPosesemNossaAplicação CasadoCódigo
Figura7.2:PosedePause
Naposequeimplementamosanteriormenteutilizamosapenascomparaçõesen-
treasposiçõesdasarticulaçõesemseuseixos,masháumoutrotipodeabordagem
paracomparaçãodeposesmaiscomplexas,comoporexemplo,aposedepauseque
criaremos.Estaabordagemcomparaalémdarelaç ãoentreduasarticulações,oân-
guloentretrêsarticulações,quepodedefinir,porexemplo,oquãoabertodeveestar
obraçodousuário,queéoquefaremosnestapose.
Paracalcularoânguloentretrêsarticulaçõesutilizaremosummétodoconhecido
comoprodutoescalar. Estemétodoéutilizadoparacalcularângulosentredois
vetores(VeW)emumespaçodetrêsdimensões.Parafazerocálculoénecessário
aplicarafórmuladoprodutoescalar,ilustradapelafigura 7.3.
96

## Página 101

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
Figura7.3:FórmuladoProdutoEscalar
Apesardeparecerumcálculopequenoéumafórmulabastantecomplexa,iremos
desenvolvê-lapassoapassoparafacilitaracompreensão.
Paragerarmososvetoresnecessáriosparaocálculoénecessárioutilizarasposi-
çõesX,YeZdastrêsarticulaçõesenvolvidas,sendoqueovetorVdevesergerado
pelasarticulações1e2eovetorWdevesergeradopelasarticulações2e3. Cada
eixodosvetoresécalculadopeladiferen çaentreoseixosdasarticulaçõesenvolvi-
das,masénecessárioelevaroresultadoaoquadradoecalcularsuaraizquadrada,
issofarácomquetodoresultadosetornepositivo,jáqueadistânciaentredoispontos
nãodevesernegativa.
Implementaremos o produto escalar na classeUtil de nosso projeto
AuxiliarKinect,entãocriaremosummétodoprivadoparaobterosvetores,con-
formeocódigoaseguir.
private static Vector4 CriarVetorEntreDoisPontos
(Joint articulacao1, Joint articulacao2)
{
Vector4 vetorResultante = new Vector4();
vetorResultante.X = Convert.ToSingle(
Math.Sqrt(
Math.Pow( articulacao1.Position.X -
articulacao2.Position.X, 2
)));
vetorResultante.Y = Convert.ToSingle(
Math.Sqrt(
Math.Pow( articulacao1.Position.Y -
articulacao2.Position.Y, 2
)));
vetorResultante.Z = Convert.ToSingle(
Math.Sqrt(
97

## Página 102

7.2. UtilizandoPosesemNossaAplicação CasadoCódigo
Math.Pow( articulacao1.Position.Z -
articulacao2.Position.Z, 2
)));
return vetorResultante;
}
AgorajáconseguimosobterovalordosvetoresVeWdescritosnafórmula.
Precisamoscalcularoprodutodosvetoreseoprodutodomódulodosvetores.Para
calcularmosoprodutodosvetoressoma-seoresultadodoprodutodecadacoorde-
nadadosvetoresenvolvidos,conformeafigura 7.4.
Figura7.4:ProdutodosVetores
Vamoscriarummétodoparacalcularoresultadodoprodutodedoisvetores,
quetambémpodeserprivado,poisutilizaremosapenasparaoprodutoescalarque
tambémserácriadonestaclasse.Seumétododeveficarsimilaraocódigoaseguir.
private static double ProdutoVetores
(Vector4 vetorV, Vector4 vetorW)
{
return vetorV.X * vetorW.X +
vetorV.Y * vetorW.Y +
vetorV.Z * vetorW.Z;
}
Paracalcularoprodutodomódulodosvetoreséumpoucomaiscomplicado.
Parafazerissoénecessáriomultiplicararaizquadradadoresultadodasomado
quadradodecadaeixodovetor,conformeafórmulailustradapelafigura7.5
Figura7.5:ProdutodoMódulodosVetores
98

## Página 103

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
Tambémcriaremosummétodoparacalcularesteresultado,conformeocódigo.
private static double
ProdutoModuloVetores(Vector4 vetorV, Vector4 vetorW)
{
return Math.Sqrt(
Math.Pow( vetorV.X, 2) +
Math.Pow( vetorV.Y, 2) +
Math.Pow( vetorV.Z, 2))
*
Math.Sqrt(
Math.Pow( vetorW.X, 2) +
Math.Pow( vetorW.Y, 2) +
Math.Pow(vetorW.Z, 2));
}
Olhandonafórmulaprincipaldocálculovocêdeveternotadoqueháumcos-
senoelevadoamenosum,estaoperaç ãoéchamadadearcocossenoeestádisponível
naclasse Mathatravésdométodo Acos.Agoraimplementaremosométodoprin-
cipalparacalcularoprodutoescalar,lembrandoqueoresultadodoprodutoescalar
seráemradianoseoconverteremosparagraus,parafazerissoénecessárioefetuar
amultiplicaçãopor180edividirpelonúmeroPI.Seumétododeveficarsemelhante
aométodoaseguir.
public static double
CalcularProdutoEscalar(Joint articulacao1,
Joint articulacao2,
Joint articulacao3)
{
Vector4 vetorV =
CriarVetorEntreDoisPontos(articulacao1, articulacao2);
Vector4 vetorW =
CriarVetorEntreDoisPontos(articulacao2, articulacao3);
double resultadoRadianos =
Math.Acos(
ProdutoVetores(vetorV, vetorW)
/
ProdutoModuloVetores(vetorV, vetorW));
99

## Página 104

7.2. UtilizandoPosesemNossaAplicação CasadoCódigo
double resultadoGraus = resultadoRadianos * 180 / Math.PI;
return resultadoGraus;
}
Nestepontojáconseguimoscalcularoprodutoescalarentretrêsarticulações,
entãoprecisamoscriaraclassequerepresentanossaposeparaativaraescalacinza.
Ométododevalidaçãodestaposedeveutilizaroprodutoescalarparavalidaroân-
guloentreoquadrilesquerdo,ombroesquerdoemãoesquerda.Alémdisso,éne-
cessárioverificarseamãoestánamesmadistânciaqueoquadrileseelaestádepois
docotovelo.Nossaclasseficaráigualaocódigoaseguir.
public class PosePause : Pose
{
public PosePause()
{
this.Nome = "PosePause";
this.QuadroIdentificacao = 30;
}
protected override bool
PosicaoValida(Microsoft.Kinect.Skeleton esqueletoUsuario)
{
const double ANGULO_ESPERADO = 25;
double margemErroPosicao = 0.30;
double margemErroAngulo = 10;
Joint quadrilEsquerdo =
esqueletoUsuario.Joints[JointType.HipLeft];
Joint ombroEsquerdo =
esqueletoUsuario.Joints[JointType.ShoulderLeft];
Joint maoEsquerda =
esqueletoUsuario.Joints[JointType.HandLeft];
Joint cotoveloEsquerdo =
esqueletoUsuario.Joints[JointType.ElbowLeft];
double resultadoAngulo =
Util.CalcularProdutoEscalar(quadrilEsquerdo,
100

## Página 105

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
ombroEsquerdo, maoEsquerda);
bool anguloCorreto =
Util.CompararComMargemErro(margemErroAngulo,
resultadoAngulo, ANGULO_ESPERADO);
bool maoEsquerdaDistanciaCorreta =
Util.CompararComMargemErro(margemErroPosicao,
maoEsquerda.Position.Z, quadrilEsquerdo.Position.Z);
bool maoEsquerdaAposCotovelo =
maoEsquerda.Position.X < cotoveloEsquerdo.Position.X;
bool maoEsquerdaAbaixoCotovelo =
maoEsquerda.Position.Y < cotoveloEsquerdo.Position.Y;
return anguloCorreto &&
maoEsquerdaDistanciaCorreta &&
maoEsquerdaAposCotovelo &&
maoEsquerdaAbaixoCotovelo;
}
}
Apenascomestaclassejáépossívelrastreá-lajáquetodaaimplementaç ãoda
estruturaderastreamentojáfoifeita.Agoravamosvoltarànossajanelaealteraro
método InicilizarRastreadoresparaquecrieumrastreadortambémparaa
posedepause,conformeocódigo.
private void InicializarRastreadores()
{
rastreadores = new List<IRastreador>();
Rastreador<PoseT> rastreadorPoseT = new Rastreador<PoseT>();
rastreadorPoseT.MovimentoIdentificado += PoseTIdentificada;
Rastreador<PosePause> rastreadorPosePause =
new Rastreador<PosePause>();
rastreadorPosePause.MovimentoIdentificado +=
PosePauseIdentificada;
rastreadores.Add(rastreadorPoseT);
rastreadores.Add(rastreadorPosePause);
101

## Página 106

7.2. UtilizandoPosesemNossaAplicação CasadoCódigo
}
private void PosePauseIdentificada(object sender, EventArgs e)
{
chkEscalaCinza.IsChecked = !chkEscalaCinza.IsChecked;
}
Comissojápodemosexecutarnossaaplicaç ãoetestaraposeemquestão,con-
formeilustraafigura 7.6
Figura7.6:IdentificandoPoseT
Otempoatéqueestaposesejadetectadaédeaproximadamenteumsegundoe,
enquantoousuárioestáparadonela,elenãorecebenenhumfeedbackdaaplicaç ão.
Issopodetornaraexperiênciaprejudicada,poisousuárionãosabeestáexecutando
aposedeformacorreta,entãoiremosfornecerumaformadefeedbackaousuário
atravésdoevento MovimentoEmProgresso.
Todososobjetosqueherdamdotipo Posejápossuemapropriedadequein-
dicaopercentualdeprogresso,entãobastacriarmosumaformadenotificaressa
informaçãoaousuário.Faremosissoatravésdeumabarradepercentual,criaremos
102

## Página 107

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
estabarrasomentequandoousuárioestivercomaposeemprogresso.Basicamente
iremosobteraposequeéenviadaporparâmetronoeventoecriaremosdoisretân-
gulos,umparafazerofundodabarraeoutroparamostraroprogresso.Seucódigo
deveficarsimilaraocódigoaseguir.
private void
PosePauseEmProgresso(object sender, EventArgs e)
{
PosePause pose = sender as PosePause;
Rectangle retangulo = new Rectangle();
retangulo.Width = canvasKinect.ActualWidth;
retangulo.Height = 20;
retangulo.Fill = Brushes.Black;
Rectangle poseRetangulo = new Rectangle();
poseRetangulo.Width =
canvasKinect.ActualWidth * pose.PercentualProgresso / 100;
poseRetangulo.Height = 20;
poseRetangulo.Fill = Brushes.BlueViolet;
canvasKinect.Children.Add(retangulo);
canvasKinect.Children.Add(poseRetangulo);
}
Apesar de não estar descrito no código anterior lembre-se de alte-
rar o método InicializarRastreadores para interpretar o evento
MovimentoEmProgresso,comissovocêjápodetestareperceberáquequando
vocêestánaposiçãocorretaabarradeprogressoéexibidanotopodenossocanvas,
conformeilustraafigura 7.7.
103

## Página 108

7.3. FinalizandoaEstruturaBaseparaDetectarMovimentos CasadoCódigo
Figura7.7:FeedbackdaPosedePause
Agoraausabilidadedenossoaplicativojámelhoroubastante,poisousuário
percebequandoaposeestásendoexecutadadeformacorretaequantotempoé
necessárioatéqueelasetorneativa.
Criaremosoreconhecimentodeumgestoparaqueissoativeumafun çãona
aplicação. Parafinsdidáticosiremosimplementarogestodeaceno,comumente
utilizadoparadespedir-sedepessoas. Masantesdeimplementarmosénecessário
finalizarmosanossaestruturabaseparadetecç ãodemovimentos.
7.3 Finalizando a Estrutura Base para Detectar
Movimentos
Nestaetapairemosfinalizarnossaestruturaparadetecç ãodemovimentosimple-
mentandoaparteparadetecç ãodegestos.Existemdiversasformasparaadetecç ão
degestos,asmaisconhecidassão:redesneuraisartificiais,comparaç ãoaumgesto
previamentearmazenadoedetecç ãoporalgoritmoespecializado.
Oprocessodedetecç ãoutilizandoatécnicadeinteligênciaartificialconhecida
104

## Página 109

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
porredesneuraisartificiaiséutilizadoemdiferentestiposdesensores,incluindoo
Kinect.Estaéumaformadedetecç ãonãotrivialecomplexa,nãoindicadaparaapli-
caçõessimples.Comumaredebemtreinada,orastreamentoedetecç ãodeumgesto
éclassificadoefeitocomboaprecisão.Porémoprocessodecriaç ãoetreinamento
deumaredeneuralpodeserbastantecustosoepoderáserutilizadoemsomenteum
gestoespecífico.
Oprocessodedetecç ãoutilizandocomparaç ãoaumexemploprévioconsiste
emregistrarosmovimentosdeumusuárioatravésdeumsoftwareespecializadoem
captura.Duranteaexecuç ãodesuaaplicaç ão,seránecessárioutilizardeAPIspara
interagircomoarquivopreviamentegravadoecompararemtemporeal.
Osdoisexemplosacimafogemdoescopodestelivro,entãoutilizaremosaabor-
dagemutilizandoalgoritmoespecializado. Estaéaformamenoscomplexaeque
possuiumbomresultadoseoalgoritmoforimplementadodaformacorreta.Esta
abordageméutilizadageralmenteemgestosmaissimples.
Iremosutilizaralgoritmosespecializados,masalémdisso,énecessárioescolher
qualalgoritmoiremoscriar.Nestecaso,parareaproveitarmosocódigo,iremosutili-
zarumalgoritmoconhecidocomo keyframes.Nestealgoritmopodemosinterpretar
umgestocomoumasériedeposesaseremreconhecidasemseguidaemdetermi-
nadoespaçodetempo,ouseja,umgestoéumacole çãodeposesquesãoexecutadas
umaapósaoutraetodaselaspossuemumamargemdetempoparaexecuç ão.Caso
essasvalidaçõessejamcumpridasogestoéaceito.
Paracadaquadrochavedogestoénecessáriotermosumapose,queéaposeque
ousuáriodeveestaredoisvaloresparacontrolaraquantidademínimaemáxima
dequadrosquedevemtersepassadodesdequeoquadrochaveanteriorfoiaceito.
Estaspropriedadessãoparaidentificaravelocidadecomqueousuáriodevefazeras
posescontidasnogesto.
Vamosabrirnovamenteoprojeto AuxiliarKinectecriaremosnonamespace
Movimentosaclasse GestoQuadroChave,essaclasseiráidentificarcadaquadro
chavedeumgesto. Conformedescrevemosnoparágrafoanterior,estaclassedeve
conteraposequeousuáriodeveráestarnessequadrochaveeostemposlimites
inferioresuperiorparaqueestequadrochavesejareconhecidoapósoquadrochave
anterior.Suaclassedeveficarsemelhanteaocódigoaseguir.
public class GestoQuadroChave
{
public int QuadroLimiteInferior { get; private set; }
public int QuadroLimiteSuperior { get; private set; }
105

## Página 110

7.3. FinalizandoaEstruturaBaseparaDetectarMovimentos CasadoCódigo
public Pose PoseChave { get; private set; }
public GestoQuadroChave
(Pose poseChave, int limiteInferior, int limiteSuperior)
{
this.PoseChave = poseChave;
this.QuadroLimiteInferior = limiteInferior;
this.QuadroLimiteSuperior = limiteSuperior;
}
}
Agora vamos criar a classe abstrata que será base para todos os gestos de
nossaaplicação, elasechamará Gestoetambémdeverásercriadanonames-
pace Movimentos. Aclasse Gestoassimcomoaclasse Posedeveherdar
de Movimentoesobrescreverométodo Rastrear,queporenquantoficaráem
branco,comofizemosanteriormente.
Nocasodegestosénecessáriopossuirumacole çãodequadroschave,poiseste
seráoprincípioparaadetecç ãodequalquergestoimplementado. Alémdisso,te-
remosquecriarumapropriedadeparaarmazenaremtempodeexecuç ãoqualo
quadrochaveatualdogestoqueousuárioseencontra.Porfim,parapodermospas-
saralgum feedbackaousuário,devemosterumcontadordequadroschaveseduas
propriedadesparaquesejapossívelobteraquantidadedeetapastotaldogestoeo
percentualdeetapasquejáforamconcluídas,conformeocódigoabaixo.
public abstract class Gesto : Movimento
{
protected LinkedList<GestoQuadroChave> QuadrosChave { get; set; }
protected LinkedListNode<GestoQuadroChave> QuadroChaveAtual
{get;set;}
private int contadorEtapas;
public int QuantidadeEtapas
{
get
{
return QuadrosChave.Count;
}
}
public int PercentualEtapasConcluidas
106

## Página 111

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
{
get
{
return contadorEtapas * 100 / QuantidadeEtapas;
}
}
public override EstadoRastreamento Rastrear
(Skeleton esqueletoUsuario)
{
}
}
Observe que armazenamos os quadros chave em uma coleção do tipo
LinkedList.Faremosissoparafacilitaratarefadeencontrarapróximaetapada
lista,jáquenestacole çãocadaelementoconheceseusucessoreantecessor.
Temosnossabaseparacriaç ãodegestos,queutilizaráfortementenossaestru-
turajápronta, tantoparadetectarasposesdeseusquadroschave, quantopara
utilizarosrastreadoresparaexecutaremsuadetecç ão. Criaremosdentrodapasta
Movimentos,apasta Gestosassimcomofizemoscomasposes.
Apasta Gestosseráorganizadadeformadiferentedapasta Poses.Nocaso
deumapose,apenasumaclasseerautilizadaparaacriaç ãodeumaposeparaa
aplicação,jánocasodosgestosénecessáriaacriaç ãodeumaclassequeherdeda
classe Gestoedetodasasposesquesãoutilizadasemseusquadroschave. Para
queaestruturadoprojetonãofiqueconfusairemoscriarapasta Acenodentroda
pasta Gestoseneladevemestartodasasclassesutilizadasparaogestodeaceno
queiremosimplementar.
Nossogestodeacenoserácompostoporsetequadrochaves,porémcomoilus-
traafigura 7.8teremosquecriarapenastrêsposes,poiselassãoreaproveitadasao
decorrerdosgestos.
107

## Página 112

7.3. FinalizandoaEstruturaBaseparaDetectarMovimentos CasadoCódigo
Figura7.8:QuadrosChavedoGestoAceno
Diferentedasposesquecriamosanteriormente,asposesquecompõemogesto
deacenosãobemmaissimples. Come çaremoscriandoaposeparaidentificaros
quadroschavesumecincodafigurailustradaanteriormente.Nessesquadroséne-
cessárioverificarseamãodousuárioestámaislongedocorpoemaisaltaqueseuco-
tovelo.Estaclasseseráimplementadacomoqualqueroutrapose,masiremosincluí-
lanonamespace Gestos.Aceno,jáqueelaseráutilizadaexclusivamenteparao
gesto.Seucódigodeveficarsimilaraocódigoaseguir.
public class AcenoMaoAposCotovelo : Pose
{
protected override bool PosicaoValida
(Skeleton esqueletoUsuario)
{
Joint maoDireita =
esqueletoUsuario.Joints[JointType.HandRight];
Joint cotoveloDireito =
esqueletoUsuario.Joints[JointType.ElbowRight];
108

## Página 113

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
bool maoDireitaAposCotovelo =
maoDireita.Position.X > cotoveloDireito.Position.X;
bool maoDireitaAcimaCotovelo =
maoDireita.Position.Y > cotoveloDireito.Position.Y;
return maoDireitaAcimaCotovelo && maoDireitaAposCotovelo;
}
}
Notequenãohádiferen çaalgumadacriaç ãodeumaposequeseráutilizada
comoquadrochaveedeumaposeindependente.Agorafaremosumaclassebastante
similaraela,masqueirávalidarseamãodousuárioestámaispróximadocorpodo
usuárioaoinvésdemaislonge,estecasoéutilizadonosquadroschavetrêsesetedo
aceno.
public class AcenoMaoAntesCotovelo : Pose
{
protected override bool PosicaoValida
(Skeleton esqueletoUsuario)
{
Joint maoDireita =
esqueletoUsuario.Joints[JointType.HandRight];
Joint cotoveloDireito =
esqueletoUsuario.Joints[JointType.ElbowRight];
bool maoDireitaAntesCotovelo =
maoDireita.Position.X < cotoveloDireito.Position.X;
bool maoDireitaSobreCotovelo =
maoDireita.Position.Y > cotoveloDireito.Position.Y;
return maoDireitaSobreCotovelo && maoDireitaAntesCotovelo;
}
}
Porfim,iremosimplementaraposeutilizadanosquadroschavedois,quatroe
seis.Nestapose,énecessáriovalidarseamãodousuárioestámaisaltaealinhada
verticalmentecomseucotovelo,lembrandoqueemcomparaçõesdeigualdadeéne-
cessárioutilizarmargemdeerronacomparaç ão,conformeocódigoaseguir.
109

## Página 114

7.3. FinalizandoaEstruturaBaseparaDetectarMovimentos CasadoCódigo
public class AcenoMaoSobreCotovelo : Pose
{
protected override bool PosicaoValida
(Skeleton esqueletoUsuario)
{
double margemErro = 0.30;
Joint maoDireita =
esqueletoUsuario.Joints[JointType.HandRight];
Joint cotoveloDireito =
esqueletoUsuario.Joints[JointType.ElbowRight];
bool maoDireitaAntesCotovelo =
maoDireita.Position.X > cotoveloDireito.Position.X;
bool maoDireitaSobreCotovelo =
Util.CompararComMargemErro(margemErro,
maoDireita.Position.Y, cotoveloDireito.Position.Y);
return maoDireitaSobreCotovelo && maoDireitaAntesCotovelo;
}
}
Comissojátemostodasasposesqueserãoutilizadaspararastreareidentificar
umacenodousuário! Agoracriaremosaclasse Acenoquedeveherdardaclasse
Gesto.Iremoscriarummétodochamado InicializaQuadrosChave,queserá
utilizadoparainstanciaranossalistaencadeadaquearmazenaosquadroschavee
preenchê-lacomosquadroschavequecompõenossogesto. Alémdisso,iremos
inicializaraspropriedades Nome, ContadorQuadrose QuadroChaveAtual.
Aoherdaraclasse Gesto,torna-senecessáriaaimplementaç ãodométodo
PosicaoValida,quedeverecuperaroretornodométodo Rastreardaposeque
estáemseuquadroatualeretornarseaposequeestánoquadroatualfoireconhe-
cida,conformeocódigoabaixo.
public class Aceno : Gesto
{
public Aceno()
{
InicializaQuadrosChave();
110

## Página 115

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
Nome = "Aceno";
ContadorQuadros = 0;
QuadroChaveAtual = QuadrosChave.First;
}
private void InicializaQuadrosChave()
{
QuadrosChave = new LinkedList<GestoQuadroChave>();
QuadrosChave.AddFirst(
new GestoQuadroChave(new AcenoMaoAposCotovelo(), 0, 0)
);
QuadrosChave.AddLast(
new GestoQuadroChave(new AcenoMaoSobreCotovelo(), 1, 25)
);
QuadrosChave.AddLast(
new GestoQuadroChave(new AcenoMaoAntesCotovelo(), 1, 25)
);
QuadrosChave.AddLast(
new GestoQuadroChave(new AcenoMaoSobreCotovelo(), 1, 25)
);
QuadrosChave.AddLast(
new GestoQuadroChave(new AcenoMaoAposCotovelo(), 1, 25)
);
QuadrosChave.AddLast(
new GestoQuadroChave(new AcenoMaoSobreCotovelo(), 1, 25)
);
QuadrosChave.AddLast(
new GestoQuadroChave(new AcenoMaoAntesCotovelo(), 1, 25)
);
}
protected override bool PosicaoValida(Skeleton esqueletoUsuario)
{
EstadoRastreamento estado =
QuadroChaveAtual.Value.PoseChave.Rastrear(esqueletoUsuario);
111

## Página 116

7.3. FinalizandoaEstruturaBaseparaDetectarMovimentos CasadoCódigo
return estado == EstadoRastreamento.Identificado;
}
}
Notequeinserimoscomotempolimiteinferiorovalordeumquadro.Como
gestoimplementadodestaformanãohaverálimitesparaavelocidademáximado
usuárioexecutarogesto.Casodesejacontrolarmelhoravelocidadedeexecuç ãodo
gesto,controleessaspropriedadesaseugosto.
Agoraparafinalizaraestruturabasedegestosprecisamosretornaràclasse
Gestoeimplementarométodo Rastrear. Diferentedapose,aimplementa ção
pararastreiodeumgestoébastantecomplexaeiráexigirumpoucomaisdeaten ção
nessaparte.Parafacilitaracompreensãofoifeitoumfluxogramadasregrasilustrado
pelafigura7.9.
112

## Página 117

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
Figura7.9:FluxogramadeRegrasparaRastrearumGesto
Antesdecome çarmosadefinirasregrasparaométodo Rastreariremoscriar
osmétodosquealteramoestadodorastreamentoeumatributointernoparacon-
trolaronovoestadoqueogestoiráadquirirapósachamadaparaométodorastrear.
Oprimeirométodoasercriadoseráchamadode ReiniciarRastreamento.Ele
seráinvocadosemprequefornecessárioreiniciarorastreamentodogesto,edeverá
reiniciaroquadrochaveatualeacontagemdequadroseetapas.Alémdisso,onovo
estadoadquiridodeveser NaoIdentificado,conformeocódigo.
113

## Página 118

7.3. FinalizandoaEstruturaBaseparaDetectarMovimentos CasadoCódigo
private void ReiniciarRastreamento()
{
ContadorQuadros = 0;
QuadroChaveAtual = QuadrosChave.First;
contadorEtapas = 0;
novoEstado = EstadoRastreamento.NaoIdentificado;
}
Note que, apesar de não ter sido ilustrado em nenhum código, o campo
novoEstadodeveserdeclaradonoescopodaclasse. Apósisso,criaremosomé-
todoparaavan çarparaopróximoquadrochave,conformeocódigoaseguir.
private void ProximoQuadroChave()
{
novoEstado = EstadoRastreamento.EmExecucao;
ContadorQuadros = 0;
QuadroChaveAtual = QuadroChaveAtual.Next;
contadorEtapas++;
}
Porfim,criaremosummétodoparapermaneceremfasederastreamentosem
alteraroquadrochave,segueocódigo.
private void PermanecerRastreando()
{
ContadorQuadros++;
novoEstado = EstadoRastreamento.EmExecucao;
}
Agoraquejátemososmétodosparaalterarmosoestadoderastreamentodo
gestovamosimplementarométodoprincipal,seguindoasregrasilustradaspeloflu-
xograma,conformeocódigo.
public override EstadoRastreamento Rastrear
(Skeleton esqueletoUsuario)
{
if (esqueletoUsuario != null)
{
if (PosicaoValida(esqueletoUsuario))
{
novoEstado = EstadoRastreamento.EmExecucao;
114

## Página 119

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
if (QuadroChaveAtual.Value == QuadrosChave.Last.Value)
novoEstado = EstadoRastreamento.Identificado;
else
{
if (ContadorQuadros >=
QuadroChaveAtual.Value.QuadroLimiteInferior &&
ContadorQuadros <=
QuadroChaveAtual.Value.QuadroLimiteSuperior)
ProximoQuadroChave();
else
if ( ContadorQuadros <
QuadroChaveAtual.Value.QuadroLimiteInferior)
PermanecerRastreando();
else if (ContadorQuadros >
QuadroChaveAtual.Value.QuadroLimiteSuperior)
ReiniciarRastreamento();
}
}
else
if (ContadorQuadros <
QuadroChaveAtual.Value.QuadroLimiteSuperior)
ReiniciarRastreamento();
else
PermanecerRastreando();
}
else
ReiniciarRastreamento();
return novoEstado;
}
Agorajápodemosvoltarparanossaaplicaç ão,criarorastreadorparanossogesto
deacenoetomarumaaç ãoquandoogestoforreconhecido!
115

## Página 120

7.4. UtilizandoGestosemNossaAplicação CasadoCódigo
7.4 UtilizandoGestos em NossaAplicação
Comtodaaestruturajápreparada,aalteraç ãoemnossaaplicaç ãoserábastantepe-
quena—bastaalterarmosométodo InicializarRastreadoresparaqueele
passeacriartambémumrastreadorparaogestodeacenoeimplementarmosum
métodoparaexecutarumaaç ãoquandooevento MovimentoIdentificadofor
disparado.
Vamoscome çarrefatorandoométodoqueinicializaosrastreadoresdenossa
aplicaçãoparaadicionarmosmaisumrastreadoremnossalista rastreadores.
Bastaseguiromesmopadrãodosjáimplementadosrastreadores,comonocódigoa
seguir.
private void InicializarRastreadores()
{
rastreadores = new List<IRastreador>();
Rastreador<PoseT> rastreadorPoseT =
new Rastreador<PoseT>();
rastreadorPoseT.MovimentoIdentificado += PoseTIdentificada;
Rastreador<PosePause> rastreadorPosePause =
new Rastreador<PosePause>();
rastreadorPosePause.MovimentoIdentificado += PosePauseIdentificada;
rastreadorPosePause.MovimentoEmProgresso += PosePauseEmProgresso;
Rastreador<Aceno> rastreadorAceno =
new Rastreador<Aceno>();
rastreadorAceno.MovimentoIdentificado += AcenoIndentificado;
rastreadores.Add(rastreadorPoseT);
rastreadores.Add(rastreadorPosePause);
rastreadores.Add(rastreadorAceno);
}
private void AcenoIndentificado(object sender, EventArgs e)
{
}
Nocódigoilustradoanteriormente,jáfoicriadoométodoqueédisparadono
executardoeventodeidentificaç ãodogestodeaceno,masaindanãohánenhuma
116

## Página 121

CasadoCódigo Capítulo7. RastreandoeIdentificandoMovimentos
açãodefato.Iremosfazercomqueaaplicaç ãosejafechada,semprequeogestode
acenodedespedidaforreconhecido.Paraqueaaplicaç ãosejafechada,utilizealinha
decódigo Application.Current.Shutdown();.
Abrasuaaplicaçãoeteste!Percebaquenossaaplicaç ãojápossuidiferentesfor-
masdeinteraçõesnaturaisparaativaralgumasfun ções,utilizandoposesegestos.
117

## Página 123

Capítulo8
Interagindocomaaplicaç ãoatravés
doKinectInteractions
Háumpacotedefuncionalidadeschamado KinectInteractions,quefoilan-
çadonaatualizaç ão1.7doSDK,porémelenãoédisponibilizadojuntocomoSDK
padrão—paraacessá-loénecessárioutilizaroKinectToolkit.Atravésdele,épossí-
veldetectarumasériedecomportamentosrelacionadosàsmãosdousuárioetam-
bémsãodisponibilizadosdiversoscomponentesdetelaquedevemserutilizados
paracriarumainterfaceadequadaaoKinect.Todasestasfuncionalidadesecompo-
nentesforamcriadosparafacilitaremelhoraranavegabilidadeentreasaplicações
queutilizamosensorcomoformadeinteraç ão.
Partedessasfuncionalidadesédisponibilizadaatravésdeumfluxodeinteraç ão,
queseráapresentadonestecapítuloeiremosnotarqueeleéumpoucodiferentedos
fluxosmostradosanteriormente.Estetipodefluxonãoéumapropriedadedaclasse
KinectSensoresimumobjetoquedevesercriadoindependente,devidoaofato
dequeo KinectInteractionsnãofazpartedoSDKpadrão.

## Página 124

8.1. PrincipaisConceitos CasadoCódigo
8.1 PrincipaisConceitos
Dentrodo KinectInteractionsháumasériedeconceitosqueprecisamserco-
nhecidosparapodermosavan çarcomnossaaplicaç ão.Éimportanteterboafamili-
aridadecomelesprapodermosaproveitaraomáximotodoseurecurso.
RastreamentoAvançadodaMão
Comojávimosanteriormente,atravésdofluxodeesqueletopodemosrastrear
diversasarticulaçõesdousuário,entreelassuasmãos.O KinectInteractions
forneceumaformamaisavan çadapararastrearmosamãodousuário,paraissoéne-
cessárioqueambososfluxosesqueletoeprofundidadejáestejamhabilitados.Com
estetipoderastreamentoépossívelidentificarmaisinformaçõesalémdoposicio-
namento. Estasinformaçõessão:identificarseousuárioestácomamãofechada,
identificarseousuárioestavacomamãofechadaeagoraeleaabriueidentificarse
ousuárioestáfazendoogestodepressionar,queéutilizadogeralmenteparaativar
afun çãodebotõesoutiles.
FluxodeInteração
Ofluxodeinteraç ãoprovêumfluxocontínuodequadrosdeinteraç ão,seme-
lhanteaomodelojávistonosoutrosfluxos,porémestenecessitadeinformaçõesdo
fluxodeesqueletoedofluxodeprofundidade.Cadaquadrodeinteraç ãoprovêin-
formaçõesrelacionadasaorastreamentoavan çadodamãoetambémépossívelobter
qualocomponentedetelaqueamãodousuárioestáalvejando,tornandoainteraç ão
comatelaalgomaissimples.
Diferente dos outros fluxos, não há apenas uma classe chamada
InteractionStream. Além dela também existe uma interface chamada
IInteractionClient,quedeveserimplementadaporcomponentesquepodem
serinterativosatravésdoKinect. Veremoscomoimplementá-laaolongodeste
capítulo.
ControlesdeTela
Há uma série de controles de tela que já implementam a interface
IInteractionClient, eles podem ser utilizados para facilitar as tarefas
maiscomuns,comoporexemplo,umpainelqueexibeoponteironaposiç ãoda
mãodousuárioouumbotãoparaserpressionado.Todosestesclientesdeinteraç ão
devemestardentrodeumcomponenteconhecidocomo KinectRegion, que
120

## Página 125

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
éumtipodepainelquepermitecriarumvínculocomosensorKinecteatravés
dele é possível interagir com os controles de tela que implementam a interface
IInteractionClient.
8.2 Melhorando NossaAplicação com os Controles
doKinectInteractions
Aprimeiracoisaafazerserámelhorarausabilidadedenossaaplicaç ãoparapoder-
mosutilizá-lacomoKinectdeformamaisnatural.Nosguiasparadesenvolvimento
deaplicaçõesnaturaisfornecidospelaprópriaMicrosoftsempreéaconselhadoofe-
recermaisdeumaformaparaexecutaramesmafuncionalidade,entãoéissoque
iremosfazer.Jáconseguimosativarasfuncionalidades“EscalaCinza”e“Esqueleto
doUsuário”atravésdeposes,masoscontrolesdetelaqueativamissonecessitamde
mousee/outeclado.Agorairemosalterarestescomponentesparapodermosativá-
loscomoKinect.
AprimeiracoisaafazerétercertezadequeasDLLs Microsoft.Kinect.T oolkit,Mi-
crosoft.Kinect.T oolkit.Controlse Microsoft.Kinect.T oolkit.Interactionsestejamsendo
referenciadasnoprojeto,alémdisso,énecessáriocopiarparaaspastas ~\bin\Debug
e ~\bin\ReleaseaDLL KinectInteractions_170_64ouaDLL KinectInteractions_170_32
dependendodaarquiteturadeseucomputador,x64oux86respectivamente.
ComtodasasreferênciaseDLLscopiadaspodemoscome çarnossaimplementa-
ção.Comojáditoantes,ofocodestaalteraç ãoémodificaroscontrolesdetelapara
queelespossamserutilizadosdeformanaturalcomoKinectenãomaisatravés
demouseeteclado. Infelizmentenoscontrolesnativosnãoháumsubstitutopara
o CheckBox,entãocriaremosumtipodebotãoqueécomumentechamadode
ToggleButton,estetipodebotãopossuiestadodepressionadoenãopressionado,
funcionandodeformasimilaraum CheckBox.
Para fazermos isso devemos criar uma nova classe em nosso namespace
Auxiliar,elasechamará KinectToggleButtonedeveherdardeumcompo-
nentejápresenteno T oolkit,chamadode KinectTileButton. Estaclassedeve
conterumapropriedadeparaidentificarseobotãoestáounãopressionadoedeve
implementaroevento Clickdesuaclassebaseparaalteraroestadodessapro-
priedade.Paraidentificaçãovisual,alteraremostambémapropriedadeBackground
destecomponente,deacordocomseuestado.
public class KinectToggleButton : KinectTileButton
{
121

## Página 126

8.2. MelhorandoNossaAplicaçãocomosControlesdoKinectInteractions CasadoCódigo
public bool IsChecked { get; set; }
public KinectToggleButton()
{
Click += AlterarEstado;
this.Background = Brushes.RoyalBlue;
}
private void AlterarEstado
(object sender, System.Windows.RoutedEventArgs e)
{
IsChecked = !IsChecked;
if (IsChecked)
this.Background = Brushes.DarkBlue;
else
this.Background = Brushes.RoyalBlue;
}
}
Ébastantesimplesimplementarestecomponente,poisgrandepartedasfunci-
onalidadesjásãoherdadasdaclasse KinectTileButton. Agorapodemosvol-
tarparanossajanelaprincipalparaalterarmososeulayout.Aprimeiracoisaafa-
zerégarantirqueosnamespacesdenossocomponente KinectToggleButton
edoscomponentespadrãodo Interactionsestejamsendoimportadosemnossaja-
nela.Parafazerisso,devemosincluí-losnadeclaraç ãodajanelanoarquivoXAML,
conformeotrechodecódigo.
<Window x:Class="Interacao.MainWindow"
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
xmlns:k="http://schemas.microsoft.com/kinect/2013"
xmlns:my="clr-namespace:Interacao.Auxiliar"
Title="MainWindow" Height="800" Width="1000"
WindowState="Maximized">
Osnamespacesdo KinectInteractionsedenossocomponenterecebemosapeli-
dosde ke myrespectivamente.Noteque,alémdeincluirosnamespaces,alteramos
oestadodajanelaparaqueelasejaabertanomodomaximizado,issoporqueopai-
nelinferiorquepossuioscontrolesterádeaumentardetamanho,poisaprecisãodo
cursorutilizandooKinectémenorqueadomouse,entãovocêdevealterarovalor
dapropriedade Heightdoterceiro RowDefinitionsdoGridde50para180.
122

## Página 127

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
Agoranajanelatemosquecircundaro StackPanelqueoscomponenteses-
tavamsendoinseridosporum KinectRegion,alémdissoprecisamosalteraro
tipodoscomponentesde CheckBoxpara my:KinectToggleButton,conforme
otrechodecódigo.
<k:KinectRegion Name="kinectRegion" Grid.Row="2" Grid.ColumnSpan="2">
<StackPanel Orientation="Horizontal" >
<my:KinectToggleButton x:Name="btnEscalaCinza"
Content="Escala Cinza" Height="130" Foreground="White"/>
<my:KinectToggleButton x:Name="btnEsqueletoUsuario"
Content="Esqueleto do Usuário" Height="130"
FontSize="20" Foreground="White"/>
</StackPanel>
</k:KinectRegion>
Precisamosalteraragoranossaclassereferenteàjanela,ealterartodasasantigas
referênciasaosCheckBoxesparanossos KinectToggleButtons,apósfazerisso
vocêjápodeexecutaraaplicaç ãoparatestá-la. Seuresultadoserásemelhanteao
ilustradopelafigura 8.1.
123

## Página 128

8.2. MelhorandoNossaAplicaçãocomosControlesdoKinectInteractions CasadoCódigo
Figura8.1:KinectToggleButtons
Aoclicarcomomousenobotão,elefuncionaránormalmente,masaindanãohá
formasdeinteragircomelesatravésdoKinect,issoporqueaindanãovinculamoso
sensorKinectaonosso KinectRegion.Nocapítuloanterior,vinculamosoevento
deidentificaçãodogestodeacenoaummétodoquefechaaaplicaç ão. Iremosal-
terarestecomportamento,paraque,quandoousuárioexecuteogestodeaceno,o
KinectRegionrecebaoobjetodo KinectSensor.Destaforma,antesdeintera-
girmoscomosbotõesénecessárioexecutarogestodeaceno.Parafazerissovamos
alterarométodoométodo AcenoIndentificadoconformecódigo.
private void AcenoIndentificado(object sender, EventArgs e)
{
if (kinectRegion.KinectSensor == null)
kinectRegion.KinectSensor = kinect;
}
AofazerissojáconseguiremosinteragircomosbotõesutilizandooKinect,
124

## Página 129

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
masaindanãotemosapossibilidadededesativarmosainteraç ãocomoscontroles.
Parapodermosfazerisso,vamosadicionarao StackPanelumcontroledotipo
KinectTileButton,queserviráparadesligarovínculoentreosensoreocom-
ponente KinectRegion.Comessaalteraç ão,o StackPaneldoscomponentesjá
existentesdeveficarsemelhanteaoaseguir.
<StackPanel Orientation="Horizontal" >
<my:KinectToggleButton x:Name="btnEscalaCinza"
Content="Escala Cinza" Height="130" Foreground="White"/>
<my:KinectToggleButton x:Name="btnEsqueletoUsuario"
Content="Esqueleto do Usuário" Height="130"
FontSize="20" Foreground="White"/>
<k:KinectTileButton Content="Desligar" Height="130" Width="150"
Foreground="White" Click="btnVoltarClick"/>
</StackPanel>
Percebaquedeclaramosocomponentejuntocomosdemais,equejávincula-
mosummétodoparaseueventode Click. Estemétodoestádefinidonaclasse
querepresentanossajanelaparadesvincularosensordenossopainel,conformeo
código.
private void btnVoltarClick(object sender, RoutedEventArgs e)
{
if (kinectRegion.KinectSensor != null)
kinectRegion.KinectSensor = null;
}
Comissojátemosapossibilidadedeinteragircomaaplicaç ãoatravésdoKinect
eoscontrolesdeteladisponibilizadosnoInteractions,masaindafaltamantermosa
funcionalidadeparafecharmosaaplicaç ão.Paraisso,circundaremosnovamenteo
StackPanel,masdestavezcomocomponente DockPanel.Estepainelpermite
utilizarmosumlayoutbaseadoembordaseutilizandoesterecursofaremoscomque
onovo KinectTileButton,queseráutilizadoparafecharmosaaplicaç ão,fique
semprepresoàbordadadireita,distanciando-sedosdemaisbotõeseevitandoque
elesejapressionadopelousuárioporengano. Ocódigoabaixoilustracomodeve
ficarahierarquiadeseu KinectRegion.
125

## Página 130

8.2. MelhorandoNossaAplicaçãocomosControlesdoKinectInteractions CasadoCódigo
<k:KinectRegion Name="kinectRegion" Grid.Row="2" Grid.ColumnSpan="2">
<DockPanel>
<k:KinectTileButton Content="Fechar"
Height="130" Width="150" Foreground="White"
DockPanel.Dock="Right" Click="btnFecharClick"/>
<StackPanel Orientation="Horizontal" >
<my:KinectToggleButton x:Name="btnEscalaCinza"
Content="Escala Cinza" Height="130"
Foreground="White"/>
<my:KinectToggleButton x:Name="btnEsqueletoUsuario"
Content="Esqueleto do Usuário" Height="130"
FontSize="20" Foreground="White"/>
<k:KinectTileButton Content="Desligar"
Height="130" Width="150"
Foreground="White" Click="btnVoltarClick"/>
</StackPanel>
</DockPanel>
</k:KinectRegion>
O KinectTileButtonparafecharaaplicaç ãotambémdeveterummétodo
vinculadoaseueventode Clickeseumétododevefazeramesmacoisaquefazía-
mosnadetecç ãodogestodeaceno,conformeocódigo.
private void btnFecharClick(object sender, RoutedEventArgs e)
{
Application.Current.Shutdown();
}
Comisso,vocêjápodetestarnovamentesuaaplicaç ão,oresultadodeveserse-
melhanteaoilustradopelafigura 8.2.
126

## Página 131

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
Figura8.2:AplicaçãoutilizandooInteractions
Paraativarosbotões,énecessáriofazerogestodepressionar,parafazerisso
bastaesticaramãocomoafiguraanteriorilustra.
8.3 Utilizando oFluxo deInteração
Jávimoscomoépossívelutilizaroscontrolesdisponíveisparamelhorarausabilidade
denossaaplicaç ãocomoKinect,agoraveremoscomoutilizaroprópriofluxode
interação.Valelembrarque,paraqueestefluxosejaprocessado,énecessárioqueos
fluxosdeprofundidadeeesqueletoestejamhabilitadostambém.
Comopropostaparaumanovafuncionalidadeiremosfazercomquesejapos-
sívelparaousuáriocriardesenhosnaimagemqueestásendoexibidanaaplicaç ão,
ouseja,alémdaimagemdacâmera,serápermitidoaousuáriocriardesenhosuti-
lizandousasmãoscomopincéis.Masparaqueamãosetornedefatoumpincelo
127

## Página 132

8.3. UtilizandooFluxodeInteração CasadoCódigo
usuárioterádefechá-la—parareconheceroestadodamãodousuário(abertaou
fechada)iremosaproveitarorecursodisponibilizadopelofluxointeraç ão.
Vocêjádeveterpercebidoqueparadesenharelementosutilizamosocompo-
nente Canvas,masestecomponentenãotemintegraç ãocomofluxodeinteraç ão,
entãocriaremosumanovaclassequeherdedaclassedocomponente Canvase
implementeainterface IInteractionClient,criandoassimumnovo Canvas
queterátodasasfuncionalidadesdooriginalemaisacompatibilidadecomofluxo
deinteração.
Vamos criar no namespace Auxiliar a classe CanvasInteracao,
seguindo o que foi dito no parágrafo anterior. Ao implemen-
tar a interface IInteractionClient, será criado o método
GetInteractionInfoAtLocation em sua classe. Este método deve retor-
narumobjetodotipo InteractionInfo,quedescreveostiposdeinteraç ãoque
podemserfeitosnestecontroledetela.Comoiremosfazercomqueousuáriodese-
nheapenasquandoamãodeleestiverfechada,devemosmarcarcomoverdadeiro
apropriedade IsGripTarget,comeladefinidacomoverdadeiroocomponente
passaaidentificaroestadodamão(aberta,fechadaourecémaberta).
Nocorpodométododevemosapenascriaroobjetodotipo InteractionInfo
emarcarapropriedadecitadaacima,seucódigodeveficarsimilaraocódigoaseguir.
public class CanvasInteracao : Canvas, IInteractionClient
{
public InteractionInfo GetInteractionInfoAtLocation
(int skeletonTrackingId, InteractionHandType handType,
double x, double y)
{
InteractionInfo info = new InteractionInfo();
info.IsGripTarget = true;
return info;
}
}
Agorapodemosutilizarestecomponenteemnossaaplicaç ãodamesmaforma
queutilizamosum Canvas.Nãoiremossubstituirocanvasquejáestánaaplicaç ão,
masapenasinserirestenossocomponenteacimado Canvasjáexistente,poiso
canvasjáexistenteprecisalimpareredesenharoscomponentesacadaquadroeeste
novomanteráodesenhoenquantoousuárioestivernomodopintura.Entãobasta
128

## Página 133

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
colocá-lonamesmaposiçãodo Canvasquejáexiste.Alémdisso,iremoscriarmais
um KinectToggleButtonparaativarafun çãodedesenhar.Paraqueousuário
nãocriedesenhosporenganoiremoshabilitarestafuncionalidadeapenasquandoo
botãomencionadoestiverativo,oarquivoXAMLdesuajanelacompletadeveficar
similaraoaseguir.
<Window x:Class="Interacao.MainWindow"
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
xmlns:k="http://schemas.microsoft.com/kinect/2013"
xmlns:my="clr-namespace:Interacao.Auxiliar"
Title="MainWindow" Height="800" Width="1000"
WindowState="Maximized">
<Grid>
<Grid.ColumnDefinitions>
<ColumnDefinition Width="*"/>
<ColumnDefinition Width="25"/>
</Grid.ColumnDefinitions>
<Grid.RowDefinitions>
<RowDefinition Height="50"/>
<RowDefinition Height="240*"/>
<RowDefinition Height="180"/>
</Grid.RowDefinitions>
<Canvas Name="canvasKinect"
Grid.Row="1" Grid.ColumnSpan="1"/>
<my:CanvasInteracao x:Name="canvasDesenho"
Grid.Row="1" Grid.ColumnSpan="1"/>
<k:KinectRegion Name="kinectRegion"
Grid.Row="2" Grid.ColumnSpan="2">
<DockPanel>
<k:KinectTileButton Content="Fechar"
Height="130" Width="150" Foreground="White"
DockPanel.Dock="Right" Click="btnFecharClick"/>
<StackPanel Orientation="Horizontal" >
<my:KinectToggleButton x:Name="btnEscalaCinza"
129

## Página 134

8.3. UtilizandooFluxodeInteração CasadoCódigo
Content="Escala Cinza" Height="130"
Foreground="White"/>
<my:KinectToggleButton x:Name="btnEsqueletoUsuario"
Content="Esqueleto do Usuário" Height="130"
FontSize="20" Foreground="White"/>
<my:KinectToggleButton x:Name="btnDesenhar"
Content="Desenhar" Height="130"
Foreground="White" Click="btnDesenharClick"/>
<k:KinectTileButton Content="Desligar"
Height="130" Width="150"
Foreground="White" Click="btnVoltarClick"/>
</StackPanel>
</DockPanel>
</k:KinectRegion>
<k:KinectSensorChooserUI Name="seletorSensorUI"
HorizontalAlignment="Center" VerticalAlignment="Top" />
<Slider Name="slider" Width="20" Orientation="Vertical"
Minimum="-27" Maximum="27" SmallChange="1" Value="0"
Height="{Binding ElementName=imagemCamera, Path=ActualHeight}"
Thumb.DragCompleted="slider_DragCompleted" Grid.Column="2"
Grid.Row="1" Margin="3,0,2,0"/>
</Grid>
</Window>
Se você prestou atenção no código de nossa janela verá que o
KinectToggleButton btnDesenhar possuiummétodoassociadoaoeventode
clique.Estemétodoseráutilizadoapenasparalimparodesenhoquandoousuário
desativarafun çãodesenhonatela,conformeocódigoaseguir.
private void btnDesenharClick(object sender, RoutedEventArgs e)
{
if (!btnDesenhar.IsChecked)
canvasDesenho.Children.Clear();
}
130

## Página 135

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
Tambémprecisaremosadicionaraonamespace Auxiliarumaclassechamada
ConfiguracaoDesenho. Comoopróprionomejásugere,estaclasseteráares-
ponsabilidadedeconfigurarodesenho(forma,coretamanho).Emnossaaplicaç ão,
iremosutilizardoisconfiguradores,umparacadamãodousuário.Paradefinircor
etamanho,temosobjetosjápreparadosnalinguagem,mastambémdevemosadi-
cionarumenumerador( enum)paraasformas. Oenumeradorseráchamadode
FormaDesenhoeseucódigodevesersemelhanteaocódigoaseguir.
public enum FormaDesenho
{
Retangulo,
Elipse
}
Simples,não?Criamosissoparafacilitaraidentificaç ãodaformaquedeveser
desenhada.Agoracriaremosnossaclassedeconfiguraç ão,conformeocódigo.
public class ConfiguracaoDesenho
{
public FormaDesenho Forma { get; set; }
public SolidColorBrush Cor { get; set; }
public int Tamanho { get; set; }
public bool DesenhoAtivo {get; set;}
}
Estaclasseapenasirágerenciaraconfiguraç ãododesenho,enãopossuiráne-
nhumtipodecomportamento. Aindaprecisamosfazerumaúltimacoisaantesde
implementarmosainteraçãocomnossonovo Canvas:precisamosdeummétodo
quecrieodesenhodeacordocomasconfiguraçõesdaclassecriadaanteriormente.
Paraacriaç ãodestenovométodovamosreaproveitarnossocódigoescritona
classe EsqueletoUsuarioAuxiliar,váriostrechosjáescritosnocorpodeum
métodopodemserrefatoradosparapermitirsuareutilizaç ão.Vamosanalisarnosso
códigojáexistentenométodo DesenharArticulacao.
public void DesenharArticulacao
(Joint articulacao, Canvas canvasParaDesenhar)
{
int diametroArticulacao =
articulacao.JointType == JointType.Head ? 50 : 10;
131

## Página 136

8.3. UtilizandooFluxodeInteração CasadoCódigo
int larguraDesenho = 4;
Brush corDesenho = Brushes.Red;
Ellipse objetoArticulacao =
CriarComponenteVisualArticulacao
(diametroArticulacao, larguraDesenho, corDesenho);
ColorImagePoint posicaoArticulacao =
ConverterCoordenadasArticulacao(articulacao,
canvasParaDesenhar.ActualWidth, canvasParaDesenhar.ActualHeight);
double deslocamentoHorizontal =
posicaoArticulacao.X - objetoArticulacao.Width / 2;
double deslocamentoVertical =
(posicaoArticulacao.Y - objetoArticulacao.Height / 2);
if ( deslocamentoVertical >= 0 &&
deslocamentoVertical < canvasParaDesenhar.ActualHeight &&
deslocamentoHorizontal >= 0 &&
deslocamentoHorizontal < canvasParaDesenhar.ActualWidth )
{
Canvas.SetLeft
(objetoArticulacao, deslocamentoHorizontal);
Canvas.SetTop
(objetoArticulacao, deslocamentoVertical);
Canvas.SetZIndex
(objetoArticulacao, 100);
canvasParaDesenhar.Children.Add(objetoArticulacao);
}
}
Analisandoocódigoanterior,notamosqueparadesenharumaarticulaç ãopre-
cisamoscriaralgumasconfigurações,depoisdissocriamosumcomponentevisual
(nocasoumaelipse)deacordocomasconfiguraçõescitadasanteriormenteepor
fimposicionamosocomponenteno Canvas.
A configuração do componente e seu posicionamento não estão direta-
mente relacionados com a operação de desenhar uma articulação. Vamos se-
132

## Página 137

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
parar estes passos em métodos menores e faremos chamadas para eles de
dentro do método maior. A primeira coisa a ser feita é alterar o método
CriarComponenteVisualArticulacaoparaqueelenãocriemaisumobjeto
dotipo Ellipseemseucorpoepasseaapenasconfigurarumcomponentevisual
informadoporparâmetro,facilitandoassimseureuso,conformeocódigoabaixo.
private void ConfigurarComponenteVisualArticulacao
(Shape forma, int diametroArticulacao,
int larguraDesenho, Brush corDesenho)
{
forma.Height = diametroArticulacao;
forma.Width = diametroArticulacao;
forma.StrokeThickness = larguraDesenho;
forma.Stroke = corDesenho;
}
Oobjetopassadoparaométodoexibidoanteriormenteédotipo Shape.Desta
forma,podemosconfigurardiversostiposdeformasenãoapenasobjetoscirculares,
comoerafeitoanteriormente.Agoraprecisamoscriarumnovométodoparaexecu-
tarospassosnecessáriosparaposicionaroelementono Canvas.Chamaremoseste
métodode PosicionarDesenho.Nele,seránecessárioreceberporparâmetroa
articulaçãoqueiráserdesenhada,o Canvasnoqualocomponenteserádesenhado
eocomponentepropriamentedito,conformeocódigoabaixo.
private void PosicionarDesenho
(Joint articulacao, Canvas canvasParaDesenhar, Shape objetoArticulacao)
{
ColorImagePoint posicaoArticulacao =
ConverterCoordenadasArticulacao(articulacao,
canvasParaDesenhar.ActualWidth, canvasParaDesenhar.ActualHeight);
double deslocamentoHorizontal =
posicaoArticulacao.X - objetoArticulacao.Width / 2;
double deslocamentoVertical =
(posicaoArticulacao.Y - objetoArticulacao.Height / 2);
if ( deslocamentoVertical >= 0 &&
deslocamentoVertical < canvasParaDesenhar.ActualHeight &&
deslocamentoHorizontal >= 0 &&
deslocamentoHorizontal < canvasParaDesenhar.ActualWidth)
133

## Página 138

8.3. UtilizandooFluxodeInteração CasadoCódigo
{
Canvas.SetLeft
(objetoArticulacao, deslocamentoHorizontal);
Canvas.SetTop
(objetoArticulacao, deslocamentoVertical);
Canvas.SetZIndex
(objetoArticulacao, 100);
canvasParaDesenhar.Children.Add(objetoArticulacao);
}
}
Eométodo DesenharArticulacaodeveficarsemelhanteaoseguintecódigo.
public Ellipse DesenharArticulacao
(Joint articulacao, Canvas canvasParaDesenhar)
{
int diametroArticulacao =
articulacao.JointType == JointType.Head ? 50 : 10;
int larguraDesenho = 4;
Brush corDesenho = Brushes.Red;
Ellipse objetoArticulacao = new Ellipse();
ConfigurarComponenteVisualArticulacao
(objetoArticulacao, diametroArticulacao,
larguraDesenho, corDesenho);
PosicionarDesenho(articulacao, canvasParaDesenhar,
objetoArticulacao);
return objetoArticulacao;
}
O método acima passou a ter um corpo muito menor e suas responsabi-
lidades foram separadas, o que facilita a criação de novos métodos para dese-
nharelementosemumcanvas. Iremosreaproveitá-lasagoraparacriarométodo
InteracaoDesenhar. Estemétodoiráreceberporparâmetroumaarticulaç ão,
134

## Página 139

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
um Canvaseumobjetodeconfiguraç ãodedesenho—atravésdelespodemosob-
tertodainformaç ãonecessáriaparadesenharmosnossasformasemnopainel.
O corpo deste novo método ficará bastante similar ao método
DesenharArticulacao, porém, diferente do citado, o objeto que será dese-
nhadodependedaconfiguraç ãoepoderánãoserdotipo Ellipse.Segueocódigo
destenovométodo.
public Shape InteracaoDesenhar
(Joint articulacao, Canvas canvasParaDesenhar,
ConfiguracaoDesenho configuracao)
{
int larguraDesenho = 4;
Shape objetoArticulacao;
if (configuracao.Forma == FormaDesenho.Elipse)
objetoArticulacao = new Ellipse();
else
objetoArticulacao = new Rectangle();
ConfigurarComponenteVisualArticulacao(objetoArticulacao,
configuracao.Tamanho, larguraDesenho, configuracao.Cor);
objetoArticulacao.Fill = configuracao.Cor;
PosicionarDesenho(articulacao, canvasParaDesenhar,
objetoArticulacao);
return objetoArticulacao;
}
Agorajátemostudoqueprecisamosparaalterarocódigodenossajanela,mãos
àobra! Comojáfoiditonoiníciodocapítulo,ofluxodeinteraç ãoéumpouco
diferentedosdemais,entãoprecisamoscriaremnossaclasseumobjetodotipo
InteractionStreamparagerenciá-lo.Alémdisso,iremoscriardoisobjetoscon-
figuradores,umparacadamão.
public partial class MainWindow : Window
{
KinectSensor kinect;
List<IRastreador> rastreadores;
InteractionStream fluxoInteracao;
135

## Página 140

8.3. UtilizandooFluxodeInteração CasadoCódigo
ConfiguracaoDesenho configuracaoMaoDireita;
ConfiguracaoDesenho configuracaoMaoEsquerda;
...
Seguindoosmesmosprincípiodosoutrosobjetosquegerenciamosemnossa
janela, vamos criar um método para inicializar os configuradores, chamado
InicializarConfiguracoesDesenho,conformeocódigo.
private void InicializarConfiguracoesDesenho()
{
configuracaoMaoDireita = new ConfiguracaoDesenho();
configuracaoMaoDireita.Cor = Brushes.Red;
configuracaoMaoDireita.Forma = FormaDesenho.Elipse;
configuracaoMaoDireita.Tamanho = 20;
configuracaoMaoEsquerda = new ConfiguracaoDesenho();
configuracaoMaoEsquerda.Cor = Brushes.Blue;
configuracaoMaoEsquerda.Forma = FormaDesenho.Retangulo;
configuracaoMaoEsquerda.Tamanho = 20;
}
Esteéapenasumexemplodeconfiguraç ão,estejalivreparacolocarascores,
formasetamanhosquedesejarenãoesque çadeinserirachamadadestemétodono
construtordajanela.Agoraprecisamostambéminicializaronossofluxodeintera-
ção.Paraqueelesejainicializado,énecessárioterumobjetoquerepresenteosensor
eumobjetoquerepresenteum IInteractionClient.Játemososdoisdisponí-
veisemnossajanela,maslembre-sequeosensorpodeserdesconectadoouinserido
aqualquermomentoenquantoaaplicaç ãoestiverrodando,então,paragarantirque
tudocontinuefuncionando,precisaremosreinicializarofluxodeinteraç ãosempre
queumnovosensorforconectado,oquequerdizerqueachamadaparasuainicia-
lizaçãodeveestarnométodo InicializarKinect.
Comotodososoutrosfluxos,estetambémpossuiumeventoparaquandoum
novoquadroestápronto,quesechama InteractionFrameReady. Nele,po-
demosobterumobjetodotipo InteractionFrameeatravésdeleobtermosas
informaçõesdousuário( UserInfo)quepossuidiversasinformações,comopor
exemplo,oestadodasmãosdousuário.
Paracapturarestasinformaçõesdoquadrodeinteraç ão,executamospassossi-
milaresaosutilizadosparacapturamosoesqueletodousuárioatravésdeseuqua-
dro. Precisamoscopiartodainformaç ãoparaumarrayelogoemseguidafazer
136

## Página 141

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
umavalidaçãonestearrayparaencontraroobjetoreferenteaousuárioqueestá
sendorastreado. Apósfazerisso,podemosextrairasinformaçõesatravésdoar-
ray HandPointers. Estearraypossuisomenteduasposiçõesecadaumdeseus
elementospossuiinformaçõesarespeitodeumadasmãosdousuário. Atravésda
propriedade HandEventTypedecadamãopodemosverificarseuestado. Neste
eventoapenasiremosalterarapropriedade DesenhoAtivodosconfiguradoresde
desenho,paraqueodesenhofiqueativosomentequandoousuáriofecharamão,
conformeocódigo.
private void InicializarFluxoInteracao()
{
fluxoInteracao =
new InteractionStream(kinect, canvasDesenho);
fluxoInteracao.InteractionFrameReady +=
fluxoInteracao_InteractionFrameReady;
}
private void fluxoInteracao_InteractionFrameReady
(object sender, InteractionFrameReadyEventArgs e)
{
using (InteractionFrame quadro = e.OpenInteractionFrame())
{
if (quadro == null) return;
UserInfo[] informacoesUsuarios = new UserInfo[6];
quadro.CopyInteractionDataTo(informacoesUsuarios);
IEnumerable<UserInfo> usuariosRastreados =
informacoesUsuarios.Where(
info => info.SkeletonTrackingId != 0);
if (usuariosRastreados.Count() > 0)
{
UserInfo usuarioPrincipal =
usuariosRastreados.First();
if ( usuarioPrincipal.HandPointers[0].HandEventType ==
InteractionHandEventType.Grip)
configuracaoMaoDireita.DesenhoAtivo = true;
137

## Página 142

8.3. UtilizandooFluxodeInteração CasadoCódigo
else if ( usuarioPrincipal.HandPointers[0].HandEventType ==
InteractionHandEventType.GripRelease)
configuracaoMaoEsquerda.DesenhoAtivo = false;
if ( usuarioPrincipal.HandPointers[1].HandEventType ==
InteractionHandEventType.Grip)
configuracaoMaoDireita.DesenhoAtivo = true;
else if ( usuarioPrincipal.HandPointers[1].HandEventType ==
InteractionHandEventType.GripRelease)
configuracaoMaoEsquerda.DesenhoAtivo = false;
}
}
}
Nestepontoencontramosamaiordiferen çaentreofluxodeinteraç ãoeosou-
tros,diferentedosfluxospadrõesdosensor,ofluxodeinteraç ãonãoéprocessado
automaticamentenosensor,porexemplo,ofluxodeprofundidadeédependentedo
fluxodeesqueletoparapoderobtero player segmentation dataquejávimosanteri-
ormentenestelivro,masparaqueessadependênciasejacumprida,bastaqueofluxo
deesqueletoestejaligado.Estaformaautomáticadesuprirdependênciasnãoocorre
nofluxodeinteraç ão—precisamosexplicitaroprocessamentodosdados,tantono
quadrodeesqueleto,quantonoquadrodeprofundidade.
Parafazermoscomqueestasinformaçõessejamprocessadas,teremosderefato-
rarosmétodosqueutilizamosquadrosdeprofundidadeeesqueleto.Come çaremos
comaprofundidade. Atéomomentonossafun çãoparaprofundidadeéutilizada
apenasquandoafun çãodeescalacinzaestáativa,precisamosalterarestecompor-
tamentoparaqueométodoqueutilizaoquadrodeprofundidadesempresejacha-
mado,permitindoqueseprocesseainformaç ãonecessáriaparaofluxodeinteraç ão.
Vamosprimeirorenomearométodode ReconhecerProfundidadepara
FuncoesProfundidadeassimcomofizemoscomoesqueleto.Depoisderenome-
armos,criaremosumnovométodochamado ReconhecerProfundidade,que
deveserchamadopelo FuncoesProfundidadeeexecutarapenasaparteemque
aregraparareconhecerprofundidadeéaplicada,tornandoométodoidênticoao
códigoaseguir.
private void FuncoesProfundidade
(DepthImageFrame quadro, byte[] bytesImagem, int distanciaMaxima)
138

## Página 143

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
{
if (quadro == null || bytesImagem == null) return;
using (quadro)
{
DepthImagePixel[] imagemProfundidade =
new DepthImagePixel[quadro.PixelDataLength];
quadro.CopyDepthImagePixelDataTo(imagemProfundidade);
if (btnEscalaCinza.IsChecked)
ReconhecerProfundidade
(bytesImagem, distanciaMaxima, imagemProfundidade);
}
}
private void ReconhecerProfundidade
(byte[] bytesImagem, int distanciaMaxima,
DepthImagePixel[] imagemProfundidade)
{
DepthImagePoint[] pontosImagemProfundidade =
new DepthImagePoint[640 * 480];
kinect.CoordinateMapper
.MapColorFrameToDepthFrame(kinect.ColorStream.Format,
kinect.DepthStream.Format, imagemProfundidade,
pontosImagemProfundidade);
for (int i = 0; i < pontosImagemProfundidade.Length; i++)
{
var point = pontosImagemProfundidade[i];
if ( point.Depth < distanciaMaxima &&
KinectSensor.IsKnownPoint(point) )
{
var pixelDataIndex = i * 4;
byte maiorValorCor =
Math.Max(bytesImagem[pixelDataIndex],
Math.Max(bytesImagem[pixelDataIndex + 1],
bytesImagem[pixelDataIndex + 2]));
139

## Página 144

8.3. UtilizandooFluxodeInteração CasadoCódigo
bytesImagem[pixelDataIndex] = maiorValorCor;
bytesImagem[pixelDataIndex + 1] = maiorValorCor;
bytesImagem[pixelDataIndex + 2] = maiorValorCor;
}
}
}
Vocênãodeveseesquecerderemoveracondiç ãodachamadadestemétodono
evento kinect_AllFramesReady.Agoraestemétododeveserchamadosempre
quehouverumnovoquadrodisponível.Quandoousuárioativarafun çãodedese-
nho,tantoofiltrodeescalacinzaquantoaexibiç ãodoesqueletoserãocancelados,
entãoestesmétodosnãodevemserchamadoscasoafun çãodedesenhoestejaativa.
Vamoscobrirestarestriç ãoeinserirotrechoquefazoprocessamentodosdadosde
interação,ambosserãofeitosnométodo FuncoesProfundidadedentrodobloco
using.
...
using (quadro)
{
DepthImagePixel[] imagemProfundidade =
new DepthImagePixel[quadro.PixelDataLength];
quadro.CopyDepthImagePixelDataTo(imagemProfundidade);
if (btnDesenhar.IsChecked)
fluxoInteracao.ProcessDepth
(imagemProfundidade, quadro.Timestamp);
else if (btnEscalaCinza.IsChecked)
ReconhecerProfundidade
(bytesImagem, distanciaMaxima, imagemProfundidade);
}
...
Comissonósfor çamosoprocessamentodosdadosdeinteraç ão.Agorapreci-
samosfazerumaoperaç ãosimilarnométodo FuncoesEsqueletoUsuario,mas
nesteúltimocaso,tambéménecessárioinvocarosmétodosparadesenharasformas,
casoosdesenhosestejamativos,conformeocódigoaseguir.
private void FuncoesEsqueletoUsuario(SkeletonFrame quadro)
{
140

## Página 145

CasadoCódigo Capítulo8. InteragindocomaaplicaçãoatravésdoKinectInteractions
if (quadro == null) return;
using (quadro)
{
Skeleton esqueletoUsuario =
quadro.ObterEsqueletoUsuario();
if (btnDesenhar.IsChecked)
{
Skeleton[] esqueletos = new Skeleton[6];
quadro.CopySkeletonDataTo(esqueletos);
fluxoInteracao.ProcessSkeleton(esqueletos,
kinect.AccelerometerGetCurrentReading(),
quadro.Timestamp);
EsqueletoUsuarioAuxiliar esqueletoAuxiliar =
new EsqueletoUsuarioAuxiliar(kinect);
if (configuracaoMaoDireita.DesenhoAtivo)
esqueletoAuxiliar.InteracaoDesenhar
(esqueletoUsuario.Joints[JointType.HandRight],
canvasDesenho, configuracaoMaoDireita);
if (configuracaoMaoEsquerda.DesenhoAtivo)
esqueletoAuxiliar.InteracaoDesenhar
(esqueletoUsuario.Joints[JointType.HandLeft],
canvasDesenho, configuracaoMaoEsquerda);
}
else
{
foreach (IRastreador rastreador in rastreadores)
rastreador.Rastrear(esqueletoUsuario);
if (btnEsqueletoUsuario.IsChecked)
quadro.DesenharEsqueletoUsuario(kinect, canvasKinect);
}
}
}
Agorajápodemosexecutarnossoaplicativoeverosresultados,crieetestedi-
141

## Página 146

8.3. UtilizandooFluxodeInteração CasadoCódigo
versasconfiguraçõesdedesenhosdiferentes,vocêiránotarquecomoquasetudono
sensor,háumacertaimprecisão,masépossívelterótimosresultadosdesenhando
comoKinect!
Figura8.3:DesenhandonoCanvasutilizandoInteractions
142

## Página 147

Capítulo9
UtilizandoosMicrofonesdoSensor
Alémdetodaapartedemovimentos,osensorKinecttambémcontacomquatro
microfonesecomumacapacidadegrandeparaidentificarossonsdoambiente.Essa
identificaçãopodeserseparadaemduaspartes:identificaç ãoda direçãodosom ea
depalavrasefrases.
DuranteoprocessodecaptarsonsdoambienteatravésdoKinect,épossível
fazerocancelamentode20decibéisdealtura.Issoajudaasuprimirosomambiente
emelhorarafidelidadedasinformaçõescaptadas.Alémdisso,épossívelconfigurar
programaticamenteosensorparacaptarossonsdeumadeterminadadire ção.Por
padrão,osensornãodáprioridadeparanenhumadire çãoealteraaprioridadepara
afontedeáudiocomovolumemaisalto.
AutilizaçãodecomandosdevozcomosensorKinectpermitequeaaplicaç ão
compreendaalgumaspalavrasefraseseexecuteaçõesbaseadasnisso.Estaformade
interaçãopodesermuitonaturalaousuário,masodesigndestetipodeinterfacedeve
serbemprojetadopararetornarumresultadosatisfatório.Umerrobastantecomum
éautilizaçãodepalavrascomafonéticasimilar—semprequevocêencontrara

## Página 148

9.1. InicializandoaFontedeÁudioeDetectandoaDire çãodoSom CasadoCódigo
necessidadedepalavrassimilaresbusqueporsinônimoscomfonéticasdiferentes,
paraevitarerrosnainterpretaç ãodecomandos.
Aolongodosensor,osmicrofonesatingemumraiototalde100grauspelafrente
eadire çãodosomqueestávindodafontedoáudioéidentificadadentrodestaan-
gulação.Destaforma,podemosfazercomqueaaplicaç ãopercebaadire çãodesons,
conformeilustraafigura 9.1.
Figura9.1:RaiodeDetecç ãodeSomdoKinect
9.1 Inicializando aFonte de Á udio eDetectando a
Direção do Som
Oprimeiroprocessoqueiremosfazeréainicializaç ãodafontedeáudiodosensor.
Afontedeáudioéutilizadaparaligarosmicrofoneseparaobterofluxodeentrada
desom.Existemdiversasconfiguraçõesquepodemosfazernafontedeáudio,como
porexemplo,ajámencionadasupressãoderuídosatravésdocancelamentode20
decibéis.
Paracapturaroáudio,oKinectrecebesonsdoambientepordiversasdire ções.
Entretanto,háapropriedade BeamAnglequecorrespondeaumafaixade10graus
emqueoKinectestáaptoacaptarsonsmelhores.Asondasdesomquesãopropa-
gadasdentrodestafaixasãoseparadasdasondasquesepropagamforadela.Você
podeutilizarestapropriedadeparaatribuirmanualmenteumadire çãoquesejain-
144

## Página 149

CasadoCódigo Capítulo9. UtilizandoosMicrofonesdoSensor
teressanteparasuaaplicaç ãoprestarmaisaten çãoeisolaroáudio,ouvocêpode
utilizarasformasautomáticas.
Nasformasautomáticas( Automatice Adaptive),estafaixadefocoéatu-
alizadaconstantementeealteradaparaadire çãoondeafontedeáudioémaisalta.
Porpadrão,aforma Automaticéselecionada. Eladeveserutilizadaparaambi-
entescompoucobarulhoeruído. Jáaforma Adaptive,apesardetambémser
automatizada,émaisindicadaparalocaisbarulhentos.
Alémdo BeamAngle,existeapropriedade SoundSourceAnglequemuitas
vezestemsuasfuncionalidadesconfundidas.Estapropriedadeéatualizadacomuma
frequênciabemmaior,poiselaindicaadire çãodeondeumnovoruídoestávindo,
ouseja,semprequeháumruídoperceptívelpeloKinectestapropriedadeéalterada.
Emcasosemqueodesenvolvedoroptaporutilizaro BeamAnglemanual,écomum
utilizaro SoundSourceAngleparaajustarsuaposiç ão.
Aprimeirapartedenossaimplementaç ãoseráinicializarafontedeáudiodo
sensor,come çaracaptaradire çãodoáudioecriarumaformavisualparamostrar
issoaousuário,tantoo BeamAnglequantoo SoundSourceAngle.Faremosisso
utilizandoumabarrasimilaràbarradeprogressodenossapose,ecriaremostambém
doisindicadores,umparacadapropriedade.
VamosaoarquivoXAMLdenossajanelaprincipaleiremosalteraraalturada
ultimalinhado Gridde180para200.Abarraqueindicaráadire çãodosomficará
acimadosbotõespreviamentecriados.Depoisdefazerisso,iremoscircundarocom-
ponente KinectRegioncomumnovo Grid.Estepaineldevepossuiduaslinhas,
umacom20pixelsdealturaeoutracomtodoorestante(*). O KinectRegion
deveocuparasegundalinhacomtodooespaçorestante,enquantoquenaprimeira
linhacriaremosumcanvasparamostrarabarraeosindicadoresmencionadosan-
teriormente.
Otrechonoqualanteshaviaapenaso KinectRegiondeveficarsimilarao
trechodecódigoaseguir.
<Grid Grid.Row="2" Grid.ColumnSpan="1">
<Grid.RowDefinitions>
<RowDefinition Height="20"/>
<RowDefinition Height="*"/>
</Grid.RowDefinitions>
<Canvas Name="barraDirecaoAudio" Background="BlueViolet">
145

## Página 150

9.1. InicializandoaFontedeÁudioeDetectandoaDire çãodoSom CasadoCódigo
<Rectangle Name="ponteiroBeamAngle"
Width="7" Height="20" Fill="DarkGray"/>
<Rectangle Name="ponteiroSoundSourceAngle"
Width="3" Height="20" Fill="White"/>
</Canvas>
<k:KinectRegion Name="kinectRegion" Grid.Row="2" Grid.ColumnSpan="2">
<DockPanel>
<k:KinectTileButton Content="Fechar"
Height="130" Width="150" Foreground="White"
DockPanel.Dock="Right" Click="btnFecharClick"/>
<StackPanel Orientation="Horizontal" >
<my:KinectToggleButton x:Name="btnEscalaCinza"
Content="Escala Cinza" Height="130"
Foreground="White"/>
<my:KinectToggleButton x:Name="btnEsqueletoUsuario"
Content="Esqueleto do Usuário" Height="130"
FontSize="20" Foreground="White"/>
<my:KinectToggleButton x:Name="btnDesenhar"
Content="Desenhar" Height="130"
Foreground="White" Click="btnDesenharClick"/>
<k:KinectTileButton Content="Desligar"
Height="130" Width="150"
Foreground="White" Click="btnVoltarClick"/>
</StackPanel>
</DockPanel>
</k:KinectRegion>
</Grid>
Comocódigoanterior,játemosapartevisualdenossaimplementaç ão.Agora
oqueiremosfazeréinicializarafontedeáudiodosensoreposicionarosponteiros
146

## Página 151

CasadoCódigo Capítulo9. UtilizandoosMicrofonesdoSensor
semprequeaspropriedadesforemalteradas. Tudoquetangeafontedeáudiodo
sensorpodeseracessadoatravésdapropriedade AudioSourcedeumobjetodo
tipo KinectSensor.Nocasodenossaaplica ção,criaremosummétodochamado
InicializarFonteAudio.Nele,iremosativarasupressãoecancelamentodeeco,
interpretaroseventosdealteraç ãonovalordaspropriedadeseinicializarafontede
áudiopropriamentedita.Seucódigodeveficarsimilaraocódigoaseguir.
private void InicializarFonteAudio()
{
kinect.AudioSource.EchoCancellationMode =
EchoCancellationMode.CancellationAndSuppression;
kinect.AudioSource.BeamAngleChanged
+= AudioSource_BeamAngleChanged;
kinect.AudioSource.SoundSourceAngleChanged
+= AudioSource_SoundSourceAngleChanged;
kinect.AudioSource.Start();
}
private void AudioSource_SoundSourceAngleChanged
(object sender, SoundSourceAngleChangedEventArgs e)
{
}
private void AudioSource_BeamAngleChanged
(object sender, BeamAngleChangedEventArgs e)
{
}
Você também deve lembrar-se de inserir uma chamada ao método
InicializarFonteAudio no método InicializarKinect. Agora ire-
mosimplementaralógicaparaposicionarosponteirosnolocalcorretodeacordo
comovalordapropriedaderespectiva( BeamAngleou SoundSourceAngle).
Ocálculoparaqueoponteirofiqueemsuaposiç ãoébastantesimples,apenas
iremosfazeraconhecidaregradetrêsparaescalarovalordoânguloquevariade
-50até50graus,paraotamanhodabarraqueexibeosponteiros,quevariade0até
147

## Página 152

9.1. InicializandoaFontedeÁudioeDetectandoaDire çãodoSom CasadoCódigo
alarguraatualdabarra.Aregradetrêsgeralmenteiniciacomumaescaladezero
atédeterminadonúmero,emnossocasonãoserádiferente—apesardaescalade
ângulosvariarde-50até50,podemosassumirqueelavariade0até100,ouseja,
manteremosapropor çãonomomentodaregradetrês.
Apósaregradetrês,énecessáriosomaraoresultadoovalorquecorrespondeà
metadedalargura.Essasomasefaznecessáriaparareajustaraescaladeângulos.Por
fim,diminuiremosodeslocamentocorrespondenteàmetadedalarguradoponteiro,
paraqueomesmofiquenocentrodaposiç ão.
Alémdisso,deveserfeitoumreajusteparaasbordas,ouseja,ocomponente
nãodeveestaremumaposiç ãomenorquezeroenemaltaosuficienteparaqueele
ultrapasseabordadadireita. Iremosencapsularestasregrasemummétodocha-
mado AjustarPonteiroPorAngulo,quereceberáporparâmetroumobjetodo
tipo double,correspondenteaovalordoânguloeumobjetodotipo Rectangle,
correspondenteaoponteirodapropriedade.Seguindoestespassos,seucódigodeve
ficarsimilaraocódigoaseguir.
private void AjustarPonteiroPorAngulo(double angulo, Rectangle ponteiro)
{
double calculoPosicao =
(barraDirecaoAudio.ActualWidth * angulo / 100) +
(barraDirecaoAudio.ActualWidth / 2) -
ponteiro.ActualWidth / 2;
double deslocamento =
Math.Min(calculoPosicao,
barraDirecaoAudio.ActualWidth - ponteiro.ActualWidth);
deslocamento = Math.Max(calculoPosicao, 0);
Canvas.SetLeft(ponteiro, deslocamento);
}
Emcadaeventoqueinterpretamosanteriormenteiremosfazerumachamadaa
estenovométodo,conformeocódigo.
private void AudioSource_SoundSourceAngleChanged
(object sender, SoundSourceAngleChangedEventArgs e)
{
AjustarPonteiroPorAngulo(e.Angle, ponteiroSoundSourceAngle);
}
148

## Página 153

CasadoCódigo Capítulo9. UtilizandoosMicrofonesdoSensor
private void AudioSource_BeamAngleChanged
(object sender, BeamAngleChangedEventArgs e)
{
AjustarPonteiroPorAngulo(e.Angle, ponteiroBeamAngle);
}
Vocêjápodetestarsuaaplicação!Osresultadosdevemsersemelhantesaoilus-
tradopelafigura 9.2
Figura9.2:Detectandoadire çãodoáudioatravésdoKinect
9.2 Detectando Comandos de voz
Agoraquejáaprendemosacaptaradire çãodoáudio,vamosparaasegundaparte
dafontedeaudiodoKinect.Vamosaprenderafazercomquenossaaplicaç ãoutilize
osensorparareconhecercomandosdevozetomaraçõesbaseadasnoscomandos
reconhecidos.
OreconhecimentodecomandosdevozatravésdoKinectemumaaplicaç ão
.NETéfeitaatravésdoengenhodereconhecimentodevoz.Éimportantesaberque
esteengenhofuncionaindependentedosensor,porissoénecessárioodownload
daDLL Microsoft.Speech.Háumpacotedeextensãodeidiomasparaoreconheci-
mentodevoz,masinfelizmenteaindanãoháop çõesparafazeroreconhecimento
149

## Página 154

9.2. DetectandoComandosdevoz CasadoCódigo
decomandosemportuguês,entãoutilizaremosoidiomapadrão(inglêsdosEstados
Unidos).
Énecessárioentenderqueosensornãoirácompreenderoáudiodeformali-
vreeidentificartudooqueousuáriofala.Aoiniciarmosoengenho,iremosdefinir
umasériedeescolhasdecomandosquenossaaplicaç ãopodecompreendereabso-
lutamentetudoqueousuáriofalaroengenhotentaráencaixarnamelhorescolha
entreasqueexistem. Oresultadodeumainterpretaç ãopossuiocomandoquefoi
escolhidoeaconfian çaqueaaplicaç ãotemdequefoiaquiloqueousuáriodisse.
Oprimeiropassoparadetectarcomandosdevoznaaplicaç ãoéinicializaroen-
genhodereconhecimentodevozmencionadonoparágrafoanterior.Parainicializá-
lo,énecessárioencontrarereconheceroidiomaqueseráutilizado,carregarosco-
mandosqueserãointrepretadospelaaplicaç ão(oconjuntodecomandoséchamado
degramática),inserirofluxodoáudiodokinectnoengenhoeativardefatooreco-
nhecimento.
Vamos implementar os passos descritos anteriormente em nossa DLL
AuxiliarKinect,naclasse InicializadorKinect.Damesmaformaquecri-
amosumapropriedadeparainserirométododeinicializaç ãodosensor,faremos
umapropriedadeparainserirométodoquegeraagramáticadoengenho. Depois
disso,criaremosoutrapropriedadeparaarmazenaroengenhopropriamenteditoe
ummétodo InicializarReconhecimentoVoz.
A propriedade EngenhoReconhecimentoVoz deve ser do tipo
SpeechRecognitionEngine.Apropriedade MetodoInicializadorKinect
édotipo Action,issoporqueelaserefereaummétodoquenãopossuiretorno.
Casoométodopossuaumretorno,queéocasodapropriedadequeserácriada,é
necessárioutilizarodelegate Func.Aspropriedadesdevemficarcomoocódigoa
seguir.
public SpeechRecognitionEngine EngenhoReconhecimentoVoz
{ get; private set; }
public Func<Grammar> MetodoGerarGramatica
{ get; set; }
Agora já podemos vincular um método para gerar a gramática dos co-
mandos em nosso inicializador, mas ainda precisamos criar o método que
inicializa o reconhecimento de comandos de voz. Este método se chamará
InicializarReconhecimentoVozedevereceberumobjetodotipo Stream
150

## Página 155

CasadoCódigo Capítulo9. UtilizandoosMicrofonesdoSensor
porparâmetro,queconteráofluxodeáudiodoKinect.Alémdisso,dentrodomé-
todofaremosospassosdescritosanteriormente.
public void InicializarReconhecimentoVoz(Stream fluxoAudio)
{
Func<RecognizerInfo, bool> encontrarIdioma = reconhecedor =>
{
string value;
reconhecedor.AdditionalInfo.TryGetValue("Kinect", out value);
return "True".Equals(value, StringComparison
.InvariantCultureIgnoreCase) &&
"en-US".Equals(reconhecedor.Culture.Name,
StringComparison.InvariantCultureIgnoreCase);
};
RecognizerInfo recognizerInfo =
SpeechRecognitionEngine.InstalledRecognizers()
.Where(encontrarIdioma)
.FirstOrDefault();
EngenhoReconhecimentoVoz =
new SpeechRecognitionEngine(recognizerInfo.Id);
EngenhoReconhecimentoVoz.LoadGrammar(MetodoGerarGramatica());
EngenhoReconhecimentoVoz.SetInputToAudioStream
(fluxoAudio,
new SpeechAudioFormatInfo
(EncodingFormat.Pcm, 16000, 16, 1, 32000, 2, null));
EngenhoReconhecimentoVoz.RecognizeAsync(RecognizeMode.Multiple);
}
Comovocêpodever,foicriadaumfun çãoparabuscaroidiomaentreosidiomas
instaladosnoengenhodereconhecimentodevoz,eapósissooengenhofoiinicia-
lizadopassandoasinformaçõesdereconhecimento.Tambémutilizamosaproprie-
dadecriadaanteriormenteparacarregaragramáticaeemseguidainserimosofluxo
deáudiodoKinectnoengenhocomasdevidasconfigurações.
Osparâmetrosinformadosnoobjeto SpeechAudioFormatInfopassadopor
parâmetronométodo SetInputToAudioStreamindicamaconfiguraçãodosen-
sorKinectparacodificaç ãodeáudio,quantidadedeexemplosporsegundo,quan-
151

## Página 156

9.2. DetectandoComandosdevoz CasadoCódigo
tidadedebits,porexemplo,quantidadedecanaisdeáudio,médiadebytesporse-
gundo,alinhamentodosblocosdeáudioeumamatrizdebytescontendooformato
específicodosdados,respectivamente.
Eporfim,iniciamosoreconhecimentoassíncronodecomandosdevoz.Agora
nossaDLL AuxiliarKinectjáestáprontaparaserutilizadaemnossajanela.Vol-
tamosnovamenteaonossoprojetodaaplicaç ãoeiremosfazermodificaçõesnosmé-
todos InicializarSeletore InicializarFonteAudio.Alémdisso,deve-
mostornaroseletordosensorumatributodajanela,paraqueelepossaseracessado
dequalquermétododenossaclasse MainWindow.
Ométodo InicializarSeletordeveserrefatoradoparaqueeleatribua
tambémapropriedade MetodoGerarGramaticaparaummétododajanela.Por
enquanto,deixaremosestemétodoembranco,conformeocódigoaseguir.
private void InicializarSeletor()
{
inicializador = new InicializadorKinect();
inicializador.MetodoInicializadorKinect = InicializarKinect;
inicializador.MetodoGerarGramatica = GerarGramatica;
seletorSensorUI.KinectSensorChooser = inicializador.SeletorKinect;
}
private Grammar GerarGramatica()
{
}
Ométodo InicializarFonteAudiotambémdeveserrefatorado.Nósutili-
zamosométodo Startdapropriedade AudioSource,masnãoprecisávamosob-
terseuretorno.Apartirdeagora,iremosobterofluxodeáudioqueéretornadodeste
métodoparapodermosinicializarnoengenhodereconhecimentodevoz. Apóso
inicializarmos,devemosinterpretaroeventodecomandoreconhecido,conformeo
códigoaseguir.
private void InicializarFonteAudio()
{
kinect.AudioSource.EchoCancellationMode =
EchoCancellationMode.CancellationAndSuppression;
kinect.AudioSource.BeamAngleChanged
+= AudioSource_BeamAngleChanged;
152

## Página 157

CasadoCódigo Capítulo9. UtilizandoosMicrofonesdoSensor
kinect.AudioSource.SoundSourceAngleChanged
+= AudioSource_SoundSourceAngleChanged;
Stream fluxoAudio = kinect.AudioSource.Start();
inicializador.InicializarReconhecimentoVoz(fluxoAudio);
inicializador.EngenhoReconhecimentoVoz
.SpeechRecognized +=
KinectSpeechRecognitionEngine_SpeechRecognized;
}
private void KinectSpeechRecognitionEngine_SpeechRecognized
(object sender, SpeechRecognizedEventArgs e)
{
}
Noexemplodestelivroiremostratarapenascomandosidentificados,mascaso
vocêqueira,háoutrostiposdeeventosdisponíveis,comoporexemplo,todavezque
umcomandoéhipotetizado,ourejeitado.
Antesdeimplementarmosométododereconhecimentodecomandoséneces-
sárioqueostenhamosdefinidoe,comovistoanteriormente,nossométodopara
geraragramáticaaindaestáembrancoechegouahoradeoimplementarmos.Exis-
temdoiscomandosquequasesempredevemsercriadosemumagramática,quesão
utilizadosparaativaredesativarainterpretaç ãodosoutroscomandos.
Imagineoseguintecenário:vocêestácomsuaaplicaçãoabertaeestátendouma
conversacomalguém.Seriafrustrantesesuaaplicaç ãoexecutasseumaaç ãobaseada
emumafrasequevocêdisseemsuaconversa.Paraevitaresteproblemageralmente
háumapalavrachave—nocasodoKinectnoconsoleXbox360,apalavrachave
paraativaçãodecomandosdevozé“Xbox”.Emnossaaplicaçãoaspalavraschaves
serão:KinecteCancel,paraativaredesativarainterpretaç ãodecomandos.
Nocapítuloanterior,criamosumamaneiradousuáriodesenharformasecores
usandoofluxodeinteraç ão,masinfelizmente,umavezdefinidaaconfiguraç ãode
desenho,elapermaneceportodaaaplicaç ão.Iremosutilizarcomandosdevozpara
permitiraalteraç ãodascoreseformasdeambasasmãosdousuário. Paraqueo
usuárioaltereumacorouumaforma,eledevedizerumasenten çacompleta,indi-
candoqualamãoqueteráaconfiguraç ãoalterada,oqueseráalterado(corouforma)
153

## Página 158

9.2. DetectandoComandosdevoz CasadoCódigo
equalovalorqueapropriedadeassumirá.Assenten çasficarãonoseguinteformato:
“Change(left/right)hand(color/shape)to(valor)”.
Iremoscriardoismétodospararetornarmososvalorespossíveisdetodasascores
edetodasasformasemumalistade string.Nesteexemploiremosnoslimitara
umpequenogrupodeop ções. Vocêpodeaumentarotamanhodalistasedesejar,
masaestruturadeseusmétodosdeveficarsemelhanteaocódigoaseguir.
private List<string> GerarListaCores()
{
List<string> cores = new List<string>();
cores.Add("red");
cores.Add("blue");
cores.Add("yellow");
cores.Add("green");
cores.Add("pink");
return cores;
}
private List<string> GerarListaFormas()
{
List<string> formas = new List<string>();
formas.Add("rectangle");
formas.Add("ellipse");
return formas;
}
Comisso,játemosospossíveisvaloreseaestruturadenossoscomandos,agorajá
éhoradeimplementarmosométodo GerarGramatica.Paragerarmosumagra-
máticaénecessárioutilizaraclasseChoices,quepermiteadicionarmosasescolhas
decomandosqueaaplicaç ãoirácompreender.Estescomandospodemseradicio-
nadosemformadestrings.Apóspopularmostodasasescolhasquenossaaplicaç ão
possui,énecessáriocriarumobjetodotipo GrammarBuilderparaconstruiragra-
máticautilizandooscomandose,porfim,criarumobjetodotipo Grammar,queé
agramáticapropriamentedita,conformeocódigoaseguir.
private Grammar GerarGramatica()
{
Choices comandos = new Choices();
154

## Página 159

CasadoCódigo Capítulo9. UtilizandoosMicrofonesdoSensor
List<string> listaFormas = GerarListaFormas();
List<string> listaCores = GerarListaCores();
comandos.Add("Kinect");
comandos.Add("Cancel");
for (int indice = 0; indice < 2; indice++)
{
StringBuilder sentencaBase = new StringBuilder();
string direcaoMao = indice == 0 ? "right" : "left";
sentencaBase.Append("Change ");
sentencaBase.Append(direcaoMao);
sentencaBase.Append(" hand ");
string inicial = sentencaBase.ToString();
for ( int indiceLista = 0;
indiceLista < listaCores.Count;
indiceLista++)
{
StringBuilder sentencaFinal =
new StringBuilder(inicial);
sentencaFinal.Append("color to ");
sentencaFinal.Append(listaCores[indiceLista]);
comandos.Add(sentencaFinal.ToString());
}
for ( int indiceLista = 0;
indiceLista < listaFormas.Count;
indiceLista++)
{
StringBuilder sentencaFinal =
new StringBuilder(inicial);
sentencaFinal.Append("shape to ");
sentencaFinal.Append(listaFormas[indiceLista]);
comandos.Add(sentencaFinal.ToString());
}
155

## Página 160

9.2. DetectandoComandosdevoz CasadoCódigo
}
GrammarBuilder construtor =
new GrammarBuilder(comandos);
construtor.Culture =
inicializador.EngenhoReconhecimentoVoz.RecognizerInfo.Culture;
Grammar gramatica = new Grammar(construtor);
return gramatica;
}
Comocódigoanterior,nossagramáticajáestáprontaenossaaplicaçãojáestáre-
conhecendooscomandos,porémaindanãotomamosnenhumaaç ão,independente
docomandoqueéreconhecido.Agorairemosimplementarométodoassociadoao
eventodereconhecimentodecomandodevozquecriamosanteriormente.
Comojáfoiditoantes,todavezqueumcomandodevozéreconhecido,oresul-
tadoenviadoparanossoeventopossuiumníveldeconfian ça.Esteníveldeconfian ça
deveserlevadoemconsideraç ãoparaevitarqueaçõessejamtomadasindesejada-
mente.OrecomendadopelaMicrosoftéqueoscomandosreconhecidosdevemter
umníveldeconfian çade80%oumais,mascomonãoestamosutilizandonossoidi-
omanativo,eosotaquetambémélevadoemconsideraç ão,iremosaceitarqualquer
comandocomníveldeconfian çade50%oumais.
Então,nométodoqueédisparadoquandoaaplicaç ãoreconheceumcomando
devoz,énecessáriovalidaroníveldeconfian ça.Parafazerisso,utilizeapropriedade
Confidence,quevariade0até1,sendoque1éequivalentea100%deconfian ça.
Apósvalidaraconfian ça,énecessárioverificarseocomandoreconhecidoéumco-
mandochave,casosejairemosnotificarousuárioquenossaaplicaç ãopassouaescu-
tarouanãoescutaroscomandosdevoz.Parafazerisso,utilizaremosapropriedade
IsListeningdocomponentevisual seletorSensorUI.Casonãosejaumco-
mandochave,iremospassaroresultadoadianteparaummétodoquechamaremos
de InterpretarComandoConfiguracaoCor,conformeocódigoaseguir.
private void KinectSpeechRecognitionEngine_SpeechRecognized
(object sender, SpeechRecognizedEventArgs e)
{
156

## Página 161

CasadoCódigo Capítulo9. UtilizandoosMicrofonesdoSensor
RecognitionResult resultado = e.Result;
if (resultado.Confidence > 0.5)
{
if (resultado.Text == "Kinect")
seletorSensorUI.IsListening = true;
else if (resultado.Text == "Cancel")
seletorSensorUI.IsListening = false;
else if (seletorSensorUI.IsListening)
InterpretarComandoConfiguracaoCor(resultado);
}
}
private void InterpretarComandoConfiguracaoCor
(RecognitionResult resultado)
{
}
Sevocêexecutarsuaaplicaç ão,jápoderánotarqueaodizerocomandodevoz
Kinectelapassaanotificarousuárioqueosensorestáprontoparaescutarcomandos
devoz,conformeafigura 9.3.
Figura9.3:Kinectprontopararecebercomandosdevoz
Agorairemosimplementarométodoqueinterpretaoscomandosdeconfigura-
157

## Página 162

9.2. DetectandoComandosdevoz CasadoCódigo
ção.Parafazerissoserábastantesimples:primeiro,iremosverificarseocomando
possuiasubsenten ça“lefthand”ou“righthand”,comissojádescobrimosqualcon-
figuraçãodevemosalterar. Depois,buscamospelapalavra“color”ou“shape”para
descobrirmosqualapropriedadequedeveráseralterada. Eporfim,buscamosa
ultimapalavradasenten çaeaplicamososeuvalorparaarespectivapropriedade,
conformeocódigoaseguir.
private void InterpretarComandoConfiguracaoCor
(RecognitionResult resultado)
{
ConfiguracaoDesenho configuracao;
if (resultado.Text.Contains("left hand"))
configuracao = configuracaoMaoEsquerda;
else
configuracao = configuracaoMaoDireita;
if (resultado.Text.Contains("color"))
{
string cor =
resultado.Text.Substring(resultado.Text.LastIndexOf(" ") + 1);
SolidColorBrush novaCor = Brushes.Red;
switch (cor)
{
case "red":
novaCor = Brushes.Red;
break;
case "blue":
novaCor = Brushes.Blue;
break;
case "yellow":
novaCor = Brushes.Yellow;
break;
case "green":
novaCor = Brushes.Green;
break;
case "pink":
novaCor = Brushes.Pink;
break;
}
158

## Página 163

CasadoCódigo Capítulo9. UtilizandoosMicrofonesdoSensor
configuracao.Cor = novaCor;
}
else if (resultado.Text.Contains("shape"))
{
string forma =
resultado.Text.Substring(resultado.Text.LastIndexOf(" " ) + 1);
FormaDesenho novaForma = FormaDesenho.Retangulo;
switch (forma)
{
case "rectangle":
novaForma = FormaDesenho.Retangulo;
break;
case "ellipse":
novaForma = FormaDesenho.Elipse;
break;
}
configuracao.Forma = novaForma;
}
}
Agoranossaaplicaç ãojápodereceberalteraçõesdeconfiguraç ãododesenho
dasmãosemtempodeexecuç ãoviacomandosdevoz!Vocêpodecriardiferentes
resultados,comoporexemplo,oresultadoilustradonafigura 9.4.
159

## Página 164

9.3. Conclusão CasadoCódigo
Figura9.4:PinturaFinal
9.3 Conclusão
Terminandoaimplementaçãoanterior,nósfinalizamosaaplicaç ãodestelivro.Du-
rantealeiturapassamospelasfuncionalidadesmaisimportantesdosensordemo-
vimentosKinectsemprefocandonadidática.Ospadrõesarquiteturaisdeaplicaç ão
foramtotalmenteignorados,comoobjetivodemantervocêconcentradoapenasno
sumodoconteúdo.Umdemeusobjetivosaoescreverestelivroédispararumgati-
lhoparasuabuscaporconhecimento.Estematerialpossuiapenasumaparcelade
todooconteúdodomundoNUI,atémesmoasimplementaçõesreferentesaosensor
Kinectnãoforamabordadasem100%.
OdesenvolvimentocomoKinectéumatarefabastantecomplexaedivertida:
acreditoserumaótimaformadeunirmosmatemática,criatividadeeprogramaç ão,
sendoqueamaiorlimitaç ãoésuaimaginaç ão. Busquetambémporcódigosnão
mencionadosaqui,comoporexemplo,rastreamentodeface,compreensãodese-
mânticaemcomandosdevozegeraç ãodegramáticaporarquivoXML.Todaaárea
deNUIaindaémuitonovaeinexploradaeécertoqueteremosdiversasnovidades
tantoemsoftwarecomoemhardwareparabuscaramelhorusabilidadenaturaldas
aplicações.
Comoautoreubusqueicompartilhardeformadidática,simpleseenxutaomá-
ximodeinformaçõeseideiascomointuitodeauxiliarosmaisdiversosprograma-
160

## Página 165

CasadoCódigo Capítulo9. UtilizandoosMicrofonesdoSensor
doresquebuscamingressarnomundodaNUIatravésdosensorMicrosoftKinect.
161