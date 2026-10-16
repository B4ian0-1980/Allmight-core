---json
{
  "id": "desenvolvimento_de_jogos_para_ios_explore_sua_imagina__o_com_o_framework_cocos2d",
  "title": "Desenvolvimento de Jogos para iOS Explore sua imaginação com o framework Cocos2D",
  "categoria": "03-linguagens",
  "subcategoria": "go",
  "resumo": "**Arquivo Original:** `Desenvolvimento de Jogos para iOS Explore sua imaginação com o framework Cocos2D.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "cocos2d",
    "com",
    "desenvolvimento",
    "explore",
    "framework",
    "imagina",
    "ios",
    "jogos"
  ],
  "perguntas_tipo": [
    "Como utilizar Desenvolvimento de Jogos para iOS Explore sua imaginação com o framework Cocos2D?",
    "Quais as boas praticas de go?"
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
  "dono": "stack-go",
  "prioridade": 2
}
---

# Desenvolvimento de Jogos para iOS Explore sua imaginação com o framework Cocos2D

> **Arquivo Original:** `Desenvolvimento de Jogos para iOS Explore sua imaginação com o framework Cocos2D.pdf`
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


## Página 5

CasadoCódigo
Agradecimentos
Agradecemostodasaspessoasquenosajudaramdeformadiretaouindiretanesse
projeto.
Obrigadoatodosvocês.
i


## Página 7

CasadoCódigo Sumário
Sumário
1 Introdu ção ao desenvolvimento de jogos no iOS 1
1.1 Oquevocêencontraránestelivro . . . . . . . . . . . . . . . . . . . . . 3
1.2 Quecomeceadiversão!. . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2 Protótipo de um jogo 9
2.1 Iniciandooprojeto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2 Criandoabasedojogo . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.3 Desenhandooobjetoprincipal . . . . . . . . . . . . . . . . . . . . . . 20
2.4 Captandooscomandosdousuárioemovendoobjetos. . . . . . . . . 24
2.5 Criandooinimigo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.6 Detectandocolisõesemostrandoresultados. . . . . . . . . . . . . . . 32
2.7 Adicionandoumplacar . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
2.8 Criandobotõesdeinterfacedousuário. . . . . . . . . . . . . . . . . . 42
2.9 Adicionandomaisvida:imagensdanaveedocéu . . . . . . . . . . . 46
2.10 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
3 História do jogo 51
3.1 14-bis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
3.2 14-bisVS100Meteoros . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4 T ela inicial: Lidando com Background, logo e botões de menu 57
4.1 SobreoCocos2D. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.2 Iniciandooprojeto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.3 ajustandoaorienta ção . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
4.4 Background. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
iii


## Página 8

Sumário CasadoCódigo
4.5 AssetsdaTeladeabertura . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.6 Capturandoconfigura çõesiniciaisdodispositivo . . . . . . . . . . . . 68
4.7 Logo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
4.8 Botões . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
4.9 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5 T ela do jogo e objetos inimigos 77
5.1 GameScene . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
5.2 Transi çãodetelas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
5.3 Engines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
5.4 Meteor. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
5.5 Teladogame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
5.6 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
6 Criando o Player 93
6.1 DesenhandooPlayer . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
6.2 Botõesdecontrole . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
6.3 Atirando . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
6.4 Movendooplayer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
6.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
7 Detectando colisões, pontuando e criando efeitos 111
7.1 Detectandocolisões . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
7.2 Efeitos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
7.3 Playermorre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
7.4 Placar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
7.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
8 Adicionando sons e música 127
8.1 Executandosons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
8.2 Cachedesons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
8.3 Músicadefundo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
8.4 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
iv


## Página 9

CasadoCódigo Sumário
9 Voando com a gravidade! 133
9.1 UsandooAcelerômetro. . . . . . . . . . . . . . . . . . . . . . . . . . . 134
9.2 Controlandoainstabilidade . . . . . . . . . . . . . . . . . . . . . . . . 141
9.3 Calibrandoapartirdaposi çãoinicialdoaparelho . . . . . . . . . . . 142
9.4 Desafioscomoacelerômetro. . . . . . . . . . . . . . . . . . . . . . . . 144
9.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
10 T ela final e game over 147
10.1 Telafinal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
10.2 TelaGameOver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
10.3 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
11 Pausando o jogo 157
11.1 Montandoateladepause. . . . . . . . . . . . . . . . . . . . . . . . . . 158
11.2 ControlandooGameLoop. . . . . . . . . . . . . . . . . . . . . . . . . 161
11.3 Adicionandoobotãodepause . . . . . . . . . . . . . . . . . . . . . . . 162
11.4 Ainterfaceentrejogoepause . . . . . . . . . . . . . . . . . . . . . . . 163
11.5 Pausandoojogo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
11.6 Pausandoosobjetos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
11.7 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
12 Continuando nosso jogo 173
12.1 Utilizandoferramentassociais . . . . . . . . . . . . . . . . . . . . . . . 173
12.2 Highscore. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
12.3 Achievements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
12.4 Desafiosparavocêmelhorarojogo . . . . . . . . . . . . . . . . . . . . 177
12.5 Comoganhardinheiro?. . . . . . . . . . . . . . . . . . . . . . . . . . . 178
12.6 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
Versão:16.4.12
v


## Página 11

Capítulo1
Introduçãoaodesenvolvimentode
jogosnoiOS
RiverRaid,paraAtari,foiprovavelmenteoprimeirojogodevideogamequemuitos
jogaram.Nesseclássicogameda Activisioncriadoem1982,ojogadorcontro-
lavaumanavequesemoviadebaixoparacimanatela,ganhandopontospormatar
inimigos,destruirhelicópteros,navesebalões.Emais:erapossívelencherotanque
passandoporesta çõesdegás.


## Página 12

CasadoCódigo
Figura1.1:RIVERRAIDnoAtari
Incrívelcomoumdesenhosimplese2Dpodiasertãodivertido. Controlara
nave,fazerpontosepassarporobstáculosgarantiamhorasdediversão.
Comopassardotempo,novosjogosforamsurgindoesetornaramcadavezmais
sofisticados.Apesardetodososconceitosdosjogosantigosteremsidomantidos,um
jogodePlaystation3,porexemplo,podeenvolverdezenasdedesenvolvedores.
Atualmente,comocrescimentodos casual gamers,oscelularesetabletssetor-
naramplataformasdesucessosedisputadas. Comeles,odesenvolvimentodeum
jogonãoprecisamaisdeumaquantidadeenormededesenvolvedores. Umaideia
interessanteebemimplementadapodeserosuficienteparaseujogoobtersucesso.
Sódependedevocê.
2


## Página 13

CasadoCódigo Capítulo1. IntroduçãoaodesenvolvimentodejogosnoiOS
Figura1.2:CapadojogoRIVERRAIDde1982
1.1 O que você encontrará neste livro
Estelivroéescritoparadesenvolvedoresquejáconhecemobásicodedesenvolvi-
mentodeaplicativosparaiOS.Eleédivididoem3partesprincipais:
• Umprotótipoinicial
• Umestudodojogoqueserádesenvolvido
• UmjogodesenvolvidocomCocos2D
Aideiaéquesejaumbomguiaparatodosaquelesquequereminiciarnodesen-
volvimentodegames,sejaprofissionalmente,paraevoluirseusconhecimentosou
mesmoporpuradiversão.
3


## Página 14

1.1. Oquevocêencontraránestelivro CasadoCódigo
O que é um Desenvolvedor Apple?
OXcodeéaplataformadedesenvolvimentodeaplicativosiOS.Qualquerpessoa
podebaixá-loecome çaradesenvolverumaplicativo,testando-onosimuladorque
vemjuntodopróprioXcode.Entretanto,paraexecutarumaplicativoemseuapa-
relhoiPhone/iPadoupublicá-lonaAppStore,deve-seserumDesenvolvedorAp-
pleregistradono“iOSDeveloperProgram”(maisemhttps://developer.apple.com/
programs/ios/).
Nocapítulo2destelivrofalaremossobrecomobaixareinstalaroXcode.
Um protótipo inicial
Noiníciodolivro,serádesenvolvidoumjogosimples,programadocomapenas
2classes. Oobjetivoésefamiliarizareterumano çãogeraldosconceitosbásicos
nodesenvolvimentodegames.Essesconceitosaparecememquasetodososjogos,
sejamelessimplesouavan çados.
Nessecapítulonãoseráutilizadonenhum frameworkadicionaldedesenvolvi-
mento,apenasos frameworkspadrõesdequalqueraplicativodeiOS,incluídosauto-
maticamentepeloXcodenacria çãodeumnovoprojeto.Mesmoassim,chegaremos
aumresultadobeminteressante,comoesse:
4


## Página 15

CasadoCódigo Capítulo1. IntroduçãoaodesenvolvimentodejogosnoiOS
Figura1.3:Imagemdonossoprotótipo.
Ocódigodonossoprotótipopodeserencontradoaqui:
https://github.com/BivisSoft/jogos_ios_prototipo
Um estudo do jogo que será desenvolvido
Programaçãoéapenasumapartedodesenvolvimentodegames.Empresasfoca-
dasemdesenvolvimentodejogospossuemroteiristasparacriarahistóriadosgames,
designersparadefiniromelhorvisualdojogo,profissionaisdesomparaatrilhaso-
noraeefeitos,designersdeinterfaceparadefinircomoseráaexperiênciadojogador
nogame,entreoutros.Omarketingedivulga çãosãocasosàparte.
5


## Página 16

1.1. Oquevocêencontraránestelivro CasadoCódigo
Teremosumcapítuloespecialparaplanejarumpoucoahistóriadojogo,deter-
minarastransi çõesdetelaeestudarovisualdojogoaserdesenvolvido,queserá
nessadire ção:
Figura1.4:14bisVS100Meteoros
Tambémveremosumpoucosobrecomodeixarojogovicianteepoderganhar
dinheirocomitens,missõeseupgrades.
Um jogo desenvolvido com Cocos2D
Quandoosprincipaisconceitosjátiveremsidopassadoseahistóriaeplaneja-
mentodojogofinalizada,iniciaremosodesenvolvimentodonossojogoprincipal.
Paraele,utilizaremosum frameworkchamado Cocos2D,quefacilitaeotimizadi-
6


## Página 17

CasadoCódigo Capítulo1. IntroduçãoaodesenvolvimentodejogosnoiOS
versasquestõesusuaisnodesenvolvimentodejogos.
Figura1.5:14bisVS100Meteoros
OcódigodojogocompletocomCocos2Destádisponívelem:
https://github.com/BivisSoft/jogos_ios_14bis
OprotótipoeojogopodemserinstaladosemseuiPhonebaixandooaplicativo
Desenvolvimento de Jogos para iOS,naAppStore:
https://itunes.apple.com/br/app/id697091610
Grupo de Discussão
Existeumgrupodediscussãofocadoexclusivamenteparaosexemplosqueserão
desenvolvidosaqui. Casovocêtenhadúvidasemalgumpasso,oumesmovenhaa
7


## Página 18

1.2. Quecomeceadiversão! CasadoCódigo
implementarmodifica çõesecriaroseuprópriojogocomoqueaprendeu,compar-
tilhe!
https://groups.google.com/group/desenvolvimento-de-jogos-para-ios
CasotenhaumacontadeDesenvolvedorApple,vocêtambémpodeutilizaro
fórumdeDesenvolvedoresApplepararesolversuasdúvidas:
https://developer.apple.com/
1.2 Q ue comece a diversão!
Estelivrovaitedarabaseparacriarumjogo!Vocêsaberáporondecome çareterá
osprincipaisconceitoseaformadepensarnecessáriaparadesenvolverumgame2D
aofinaldestaleitura.Apartirdisso,éasuaprópriacriatividadeedetermina çãoque
poderãofazerdesuasideiasonovojogodesucessonomundodosgames!
8


## Página 19

Capítulo2
Protótipodeumjogo
Vamoscome çaradesenvolverumjogo! Esteseráumcapítulofundamentalpara
todoolivro,focadoemconceitosimportantes,ilustrandocommuitaprática.Nele
percorreremosasprincipaisetapasqueprecisamosteremmenteaodesenvolverum
jogo.
Comosconceitosdessecapítulopoderemosdesenvolverjogosbeminteressan-
tes,porém,oobjetivoagoraéexplorarmosasmecânicasportrásdosgamesesermos
apresentadosàformadepensarnecessária.
Parapercorreressecaminho,iniciaremoscriandoumprotótipo.Criarumpro-
tótiposerábompelasseguintesrazões:
• Conseguiremosumrápidoentendimentodavisãogeralnecessáriaparade-
senvolverumgame.
• Nãoprecisaremosnospreocuparcomcriardiversastelasqueumjogopode
ter,permitindofocarapenasnosconceitosimportantes.


## Página 20

CasadoCódigo
• Permitiráentraremdetalhesmaiscomplexosquandodefatoiniciarmosnosso
game.
Nossoprotótipoteráasfuncionalidadesbásicasencontradasnosgames,vamos
conhecerosobjetivos.
Funcionalidades do protótipo
Penseemumjogo2DtradicionalcomoSuperMarioBrosoumesmoStreetFigh-
ter. Elespossuemumasériedesemelhan ças. Emambosvocêcontrolaalgumele-
mento,quepodemoschamardePlayer. Oplayerrecebealgumtipodeestímulo
(input)paraexecutarmovimentosnatela,comoteclado,joystickoumouse.Apósos
inputsoplayerpodeganharpontossealgoacontecer,normalmenteassociadoaen-
costaremoutroobjetodojogo,oquefazcomquealgumplacarsejaatualizado.Em
determinadomomentooplayerpodeganharouperderojogo,pordiversosmotivos,
comosuperarumtempo,ultrapassarumamarcadepontosouencostaremalgum
outroobjetodogame.
Essassãoasmecânicasbásicasdequalquerjogo. Penseemoutrojogocomas
característicassemelhantesetentefazeresseparalelo.Noprotótipoquecriaremos
nessecapítulo,implementaremosessasmecânicas,entendendocomodesenvolvê-las
emumaplicativoiOS.
Nossojogoteráasseguintesfuncionalidades:
• Umplayerqueserárepresentadoporumacircunferênciaverde,posterior-
mente,anave.
• Moveroplayerdeacordocomumestímulo,nocaso,otoquenatela( input).
• Uminimigoqueserárepresentadoporumacircunferênciaqueaumentará
comopassardotempo.
• Umplacarqueseráatualizadodeacordocomotemponoqualoplayernãoé
capturadopeloinimigo.
• GameOverquandooinimigoencostarnoplayer
• Opçõesde restarte exit
Aofimdessecapítulo,teremosoprotótipoabaixo.
10


## Página 21

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.1:Imagemdojogo.
Temosmuitoparapercorrernesseprotótipo. Reparequeaoentenderalógica
portrásdeumjogo,poderemoscriarqualquertipodegame.Vamosaoprotótipo!
2.1 I niciando o projeto
VamosiniciarcriandoumprojetocomumdeiOS.Comovocêjácrioualgumapli-
cativoiOS,perceberáqueoprocedimentoéomesmo.Nãoénecessárioconfigurar
nadaespecíficoparaesteprotótipoaocriaroprojeto. Lembre-sequevocêprecisa
teroXcodeinstalado,quepodeserbaixadodiretamentepelaAppStoredeseucom-
putadorouutilizandooseguintelink:
http://itunes.apple.com/br/app/xcode/id497799835
11


## Página 22

2.1. Iniciandooprojeto CasadoCódigo
Esseéumlivrofocadoemquemjáconheceobásicododesenvolvimentode
aplicativosiOS,masmesmoassimpassaremospassoapassoemalgunspontose
revisaremosconceitoschave,parafacilitarseuacompanhamento.
AbraoXcodeeváem File,acesseasop çõesem Neweselecione Project...
paracriarumnovoprojeto.Atelaparaescolherumtemplatedeprojetoseráaberta.
Nomenuàesquerda,nase ção iOSselecioneaop ção Application. Àdireita,
selecione Empty Application ecliqueem Next.
Figura2.2:NovoprojetodeaplicativoiOS.
Criaremosumprojetochamado Impossible.Porqueessenome?Sevocêreparou
nalistadefuncionalidades,nossoprotótiponuncatemumfinalfeliz!
Coloqueonomedoprojetocomo impossible,nocampo Product Name.
Como nosso protótipo será apenas para iPhone, no campoDevice escolha
iPhone.Nosdemaiscampos,deixeasop çõesconformeafigura:
12


## Página 23

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.3:Criandooprojeto.
Cliqueem Nexteescolhaolocalondeoprojetoserágravado.
Nessemomentotemosoprojetoiniciado. Vocêjápodeexecutá-lo: selecione
iPhone x.x Simulatorem schemeecliqueem Run.Aoexecutá-lo,seráabertoosimu-
ladordeiPhonecomumatelaembranco:
13


## Página 24

2.2. Criandoabasedojogo CasadoCódigo
Figura2.4:Simuladorcomtelaembranco.
ComodesenvolveremosnossoprotótipoparaoiPhonedetelaretinade4po-
legadas,nosimuladorcliqueem Hardware, Deviceeescolhaaop ção iPhone
(Retina 4-inch).OsimuladorirámudarparacomosefosseumiPhoneretina
de4polegadas.Casoosimuladorfiquemuitograndeemsuatela,cliqueem Window,
Scaleeescolhaumpercentualdezoomquesejamelhorparaquevocêvisualizeo
simuladorinteiro.
2.2 C riando a base do jogo
Horadecome çar!Paraesseprotótipotentaremosmanterascoisassimplesediretas,
semprepensandoemaplicarosconceitosnecessáriosparacriarojogonospróximos
capítulos.
Teremosapenasduasclasses: uma UIViewController,naqualtrataremos
14


## Página 25

CasadoCódigo Capítulo2. Protótipodeumjogo
asa çõesdojogador,eumaoutraclassequeteráalógicadojogoeserárespon-
sávelpordesenharosobjetosnatela. Alémdessasduasclasses,teremosaindaa
AppDelegate,criadaporpadrãoemqualquerprojetoiOS.
Alógicadeumjogonormalmenteédivididaemdiversasclasses. Aquiaori-
entaçãoaobjetosefazrealmentenecessáriaparaumboautiliza çãodoselementos
dogame. Nesseprimeirocapítulo,manteremosascoisassimples,concentrandoa
lógicaemapenasumaclasse.Nospróximoscapítulos,quandojátivermospassado
pelosconceitosimportantes,definiremosaarquiteturadonossojogo,assimcomo
dividiremosasresponsabilidadesemdiversasclasses.
Game ViewController
Aclasse GameViewControllercomeçarásimples. Essaclasseéaportade
entradadonossojogo,entãoelaseráa rootViewControllerdenossoaplicativo.
Vamoscriarestaclassecomoqualquer UIViewControllerécriada,clicandoem
File, Neweselecionando File.Natelaparaescolherotipodearquivoasercriado,
vamosescolher Cocoa Touch nase ção iOS,eselecionar Objective-C Class:
Figura2.5:CriandonovaClasse.
Vamosdaronomedanossaclassecomo GameViewController,subclassede
uma UIViewController:
15


## Página 26

2.2. Criandoabasedojogo CasadoCódigo
Figura2.6:CriandoaGameViewController.
Nonossoarquivo GameViewController.mvamosremoveroqueoXcode
geroudecódigopadrão,comexce çãodométodo viewDidLoad,edeixaraclasse
assim:
# import "GameViewController.h"
@implementation GameViewController
- (void)viewDidLoad
{
[super viewDidLoad];
}
@end
Agora, vamos alterar a classe AppDelegate para que use nossa
GameViewController como rootViewController. Para isto, primeira-
mentedevemosimportara GameViewControlleredepoisalterarométodo
application:didFinishLaunchingWithOptions:. Altere o arquivo
AppDelegate.m.
# import "GameViewController.h"
16


## Página 27

CasadoCódigo Capítulo2. Protótipodeumjogo
// ...
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
self.window = [[UIWindow alloc] initWithFrame:
[[UIScreen mainScreen] bounds]];
// Override point for customization after application launch.
self.window.backgroundColor = [UIColor whiteColor];
GameViewController *gameVC = [[GameViewController alloc] init];
self.window.rootViewController = gameVC;
[self.window makeKeyAndVisible];
return YES;
}
A lógica do Impossible: criando um loop infinito
Aclassequeconteráalógicasechamará Impossible.Essaclassedeveherdar
de UIView. Deixeoheader Impossible.hcomocódigopadrãocriadopelo
Xcode.
# import <UIKit / UIKit.h>
@interface Impossible : UIView
@end
Elimpetodoocódigopadrãogeradono implementation Impossible.m.
# import "Impossible.h"
@implementation Impossible
@end
No iOSumobjetodotipo UIViewpermitequedesenhossejamexecutados
sobreasuperfícieemvezdetrabalharcomumXibouStoryBoard.
Agoraquejátemosa GameViewController,queéaportadeentrada,ea
classe Impossible,querepresentaalógicadojogo,vamoscriarolinkentreelas.
Paraisso,naclasse GameViewController.hcriaremosumapropriedadequear-
mazenaráa Impossibleeachamaremosde impossibleView.
17


## Página 28

2.2. Criandoabasedojogo CasadoCódigo
# import <UIKit / UIKit.h>
# import "Impossible.h"
@interface GameViewController : UIViewController
@property (nonatomic, strong) Impossible *impossibleView;
@end
Na GameViewController.minicializaremosnossa impossibleVieweadi-
cionaremoselaàtela:
- (void)viewDidLoad
{
[super viewDidLoad];
// Instancia um objeto do tipo Impossible
self.impossibleView = [[Impossible alloc] init];
// Define o tamanho dele, com base no tamanho da tela
self.impossibleView.frame = CGRectMake(0.0f,
0.0f,
self.view.frame.size.width,
self.view.frame.size.height);
[self.view addSubview:self.impossibleView];
}
Poderodarseuprojetonovamente,masaindanãotemosbonsresultados!Parece
queumjogoaindaestálongedeseconcretizar,masatéofinaldocapítulovocêjá
teráumprotótipoparamostrar.
Game Loop
Normalmente os jogos têm um primeiro conceito importante: umloop
infinito,conhecidocomo game loopou main loop.
Ojogoéumasériedeitera çõesnesse loopinfinito.Nele,ojogodefineposi ções
deelementos,desenha-osnatela,atualizavalorescomoplacar,verificacolisõesen-
treelementos. Issotudoérealizadodiversasvezesporsegundo,emquecadatela
desenhadaéchamadade frame. Umaboaanalogiasãoosdesenhosfeitosemblo-
cosdepapel,ondecadadesenho( frame)éumpeda çodaanima ção.Aopassartudo
rapidamentetemosaimpressãodemovimento.
18


## Página 29

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.7:Desenhoanimadoemblocodepapel.
Esseconceitoéextremamenteimportantee,comopassardotempo,difícilde
lidarnodesenvolvimentodeumjogo. Comváriosobjetostendodiversaspossibi-
lidadesnatelaachancedeperderocontroleégrande.Porisso,tentesemprecriar
métodospequenos,compoucaresponsabilidade.Dessaforma,encontraroquepode
estarerradoficamuitomaisfácil.
Vamoscolocaronosso loopinfinitodentrodaclasse Impossible. Paraisto,
criaremosumtimerquechamaráummétodo60vezesporsegundo,repetidamente.
Tambémteremosapropriedade runningquecontrolaráseojogoestáemexecu ção
ounão.Primeiramente,incluaocódigoabaixono Impossible.h:
@property (nonatomic, strong) NSTimer *gameRunTimer;
@property (nonatomic) BOOL running;
Entãoalteretambémo Impossible.m:
- (id)init
{
self = [super init];
19


## Página 30

2.3. Desenhandooobjetoprincipal CasadoCódigo
if (self) {
// Timer que executa o Game Loop ("run") 60 vezes por segundo
self.gameRunTimer = [NSTimer
scheduledTimerWithTimeInterval:1.0f/60.0f
target:self
selector:@selector(run)
userInfo:nil
repeats:YES];
// Variável para controlar a execução do jogo
self.running = YES;
}
return self;
}
// Game Loop
- (void)run
{
if (self.running == YES) {
NSLog(@"Impossible Running...!");
}
}
Como criamos nossotimer dentro do init, no momento em que a
Impossibleforcriadaelajácome çaráarepetiro run60vezesporsegundo.
Rodeoprojetonovamente. Temosnossaprimeirasaída,aindanãomuitoem-
polgante.Oconsoleexibe Impossible Running...! infinitamente.
2.3 D esenhando o objeto principal
Omotordonossojogojáestáligado,funcionandoatodovapor,porémnadaacon-
tecenatela.Nossopróximopassoserádefiniroobjetoprincipal,quechamaremos
dePlayer.Nossoplayerserábemsimples,apenasumelementográfico,nocasoum
círculo. Podeparecersimplesmasjogos2Dsãoobjetostriviaisquesãoanimados
muitasvezesporsegundo. Nonossocasotemosumcírculo,maspodemostrocar
porqualquerrecursoouimagemmelhortrabalhadoparadefinirumpersonagem
interessante.
Comapopulariza çãodossmartphonesedosjogoscasuais,essetipodeplayer
simplesdejogos2Dreapareceucommuitafor ça.Onomeatribuídoaessesobjetos
20


## Página 31

CasadoCódigo Capítulo2. Protótipodeumjogo
é Sprite,quenadamaissãoqueimagens,normalmenteretangularesoumesmo
quadradas,comfundostransparentes.
Vocêpodeencontrar Spritesdediversosjogosclássicosnainternet.Procure
noGooglepor‘sprites’maisonomedeumjogoquevocêgoste.Comeceaimaginar
comoessejogofuncionacomoquefalamosatéaqui.
Figura2.8:SpritesdofamosoMarioBros.
Utilizando iOS UIView e CGContext
ParadesenharelementosnateladojogonoiPhone,temosalgumasop ções.Po-
deríamoscriarosobjetopelopróprioXibouStoryBoarddoXcode.Porém,paraque
possamosentendercomofuncionaodesenhodosobjetosdeumgame,realizaremos
todoodesenhoatravésdecódigos.
Quandodesenhamosnavidareal,precisamosdeferramentascomopincéiseum
lugarparautilizá-las,comopapeloutelas.Oelemento UIViewnoiOSrepresenta
essatela,naqualpodemosdesenhardiversasformasoumesmo Sprites.Parater
acessoaesseelemento,podemosdeclararnossaclassecomosendoumatela,por
meioda UIView.
21


## Página 32

2.3. Desenhandooobjetoprincipal CasadoCódigo
Aoutilizaruma UIView,temosumtipodeViewespecializadoemexibirdese-
nhosnatela. Oprincipalpropósitoda UIViewéforneceroqueprecisamospara
querenderizarasatualiza çõesdojogoatodomomento.Uma UIViewdesenhaos
objetosemseumétodo drawRect:. EstemétodoéchamadotodavezqueoiOS
identificarqueanossa UIViewdeveserredesenhada.
Paradesenharvamosusarasfun çõesda CGContext,presenteno framework
CoreGraphicsdaApple.Comela,conseguiremosdefinirelementoscomotextos,
linhas,figurasgeométricas,coresetudoqueforreferenteacolocaroselementosdo
jogonatela.Chamamosde contextocontextoatualondeoiOSestádesenhando
objetos.
Vamos começar sobrescrevendo o métododrawRect: em nossa classe
Impossible.m,edeclarandoumavariávelparabuscarocontextoatualondees-
tãosendodesenhadososobjetos:
- (void)drawRect:(CGRect)rect
{
CGContextRef context = UIGraphicsGetCurrentContext();
// desenha o player
// o que fazer aqui??? já vamos aprender
}
Nomomentoemquesobrescrevemosométodo drawRect:da UIView,temos
totalcontroledoqueiremosdesenharounãoemnossatela.
Finalmentevamosdesenharoplayer! Utilizaremosnossospincéis,nocaso,as
funçõesdo CGContext.Paranãodeixarométodo drawRect:muitolongo,vamos
criarumoutrométodo:
- (void)drawPlayerInContext:(CGContextRef)context
{
UIGraphicsPushContext(context);
CGContextBeginPath(context);
CGContextAddArc(context,
160,
275,
25,
0,
(2 * M_PI),
YES); // Circulo de 360 ° (0 ~ 2pi)
22


## Página 33

CasadoCódigo Capítulo2. Protótipodeumjogo
CGContextSetRGBFillColor(context, 0.0f, 0.9f, 0.0f, 1.0f);
CGContextFillPath(context);
UIGraphicsPopContext();
}
Paradesenharnossoplayer,criamosumcírculocompletoepreenchemosele
comumacor.
Agorabastainvocarométodo drawPlayerdedentrodonosso drawRect.
Reparequesóprecisamosalterarumaúnicalinha,aqueestavacomumcomentário:
- (void)drawRect:(CGRect)rect
{
CGContextRef context = UIGraphicsGetCurrentContext();
[self drawPlayerInContext:context];
}
Rodenovamenteoseuprojeto.Obtivemosnossoprimeiroresultado!
23


## Página 34

2.4. Captandooscomandosdousuárioemovendoobjetos CasadoCódigo
Figura2.9:Playernatela.
2.4 C aptando os comandos do usuário e movendo
objetos
Existemdiversasmaneirasdeinteragircomumjogoecomoplayerprincipal.Mover
omouseeclicar,utilizaroteclado,tocaratelaoumesmocapturaromovimentode
umaparelho,usandoporexemplo,oacelerômetro. Noprotótipo,utilizaremoso
toquenatelaparamoveroplayer.Vamoscapturarcadatoquecomosendoum input
dousuárioe,acadavezqueissoocorrer,iremosdarumcomandoaonossojogo.
Nessemomentovamosexploraresseconceitode inputsdousuárionoiOS,
e novamente reparar na importância daUIViewController principal como
24


## Página 35

CasadoCódigo Capítulo2. Protótipodeumjogo
porta de entrada do jogo. Utilizaremos um objeto do próprio iOS chamado
UITapGestureRecognizerparaidentificarostoquesnatela. Todavezqueum
toquefordetectado,o UITapGestureRecognizerchamaráummétodopassando
ascoordenadastocadasnasuperfíciedatela.Edepossedessascoordenadas,pode-
mostomara çõessobreosobjetosnateladojogo.
Nessemomento,aodetectarumtoque,moveremosparabaixonossoplayer.Re-
parequeaquipoderíamosutilizarainforma çãoquerecebemosparatomara ções
interessantesnojogo,comomoverparaumladoouparaououtro,movermaisrá-
pidoetc. Parafimdeentendimentodeconceitoeprototipa ção,seremossimples
nessaimplementa ção.
Antesdemaisnada,precisamossaberemqueposi çãonossoplayerestá.Declare
oatributo playerYno Impossible.h:
@property (nonatomic) int playerY;
Definatambémumvalorinicialparaelequandonossaclasseforcriada,nomé-
todo initda Impossible.m:
- (id)init
{
self = [super init];
if (self) {
// Timer que executa o Game Loop (método "run") 60x por segundo
self.gameRunTimer = [NSTimer
scheduledTimerWithTimeInterval:1.0f/60.0f
target:self
selector:@selector(run)
userInfo:nil
repeats:YES];
// Posição inicial do jogador
self.playerY = 275;
// Variável para controlar a execução do jogo
self.running = YES;
}
return self;
}
E,todavezqueinvocaremo drawPlayerInContext:, vamosdesenhá-lo
nessaaltura,emvezdaquelenúmerofixo.Na Impossible.maltere:
25


## Página 36

2.4. Captandooscomandosdousuárioemovendoobjetos CasadoCódigo
// Desenha o Player
- (void)drawPlayerInContext:(CGContextRef)context
{
UIGraphicsPushContext(context);
CGContextBeginPath(context);
CGContextAddArc(context,
160.0f,
self.playerY,
25.0f,
0,
(2 * M_PI),
YES); // Círculo de 360 ° (0 ~ 2pi)
CGContextSetRGBFillColor(context, 0.0f, 0.9f, 0.0f, 1.0f);
CGContextFillPath(context);
UIGraphicsPopContext();
}
Aindana Impossible.mteremosummétodoquepodeserinvocadoparamo-
veroplayerparabaixo(ateladoiPhonepossuiaposi ção 0,0nocantosuperior
esquerdo):
- (void)moveDown:(int)pixels
{
if (self.running == YES) {
self.playerY += pixels;
}
}
Como este será um método público que deverá ser chamado pela nossa
GameViewController,temostambémquedeclará-lona Impossible.h:
- (void)moveDown:(int)pixels;
Para podermos receber a informação de que a tela foi tocada, em nossa
GameViewController.mcriaremosnossoobjetoparareconhecertoquesnatela:
- (void)viewDidLoad
{
//...
// Instancia um objeto para reconhecimento de gestos do tipo "Tap"
// e a ação a ser executada quando o usuário realizar o gesto
26


## Página 37

CasadoCódigo Capítulo2. Protótipodeumjogo
UITapGestureRecognizer *tapGesture =
[[UITapGestureRecognizer alloc] initWithTarget:self
action:@selector(handleTapGesture:)];
// Adiciona o reconhecimento de gestos à view com a qual o
// usuário irá interagir
[self.impossibleView addGestureRecognizer:tapGesture];
}
Aclasseaindanãovaifuncionarpoisestáfaltandoométodode callbackdenosso
UITapGestureRecognizer,quedefinimoscomo handleTapGesture:. Va-
mosimplementá-lo:
- (void)handleTapGesture:(UITapGestureRecognizer *)gesture
{
if (gesture.state == UIGestureRecognizerStateEnded) {
[self.impossibleView moveDown:10];
}
}
Rodeojogo. Mastemosumproblema: aotocarnatela,nossoplayerainda
não está se movendo. Isto acontece porque não estamos pedindo para nossa
Impossibleredesenharatela.
Vamoscorrigiresteproblema!No runda Impossible.mvamosinformarque
atelaprecisaserredesenhada:
- (void)run
{
if (self.running == YES) {
NSLog(@"Impossible Running...!");
// Informa ao iOS que a tela deve ser redesenhada
[self setNeedsDisplay];
}
}
Rodeojogo.Algojádeveocorreraotocarnatela:nossoplayerdevetersuaposi-
çãoalterada.Masagoratemosumoutroproblema,vejacomooplayersemovimenta
eoqueacontececomatela:
27


## Página 38

2.4. Captandooscomandosdousuárioemovendoobjetos CasadoCódigo
Figura2.10:Playermovendonatela,mastemosumproblema.
Importante: Limpando a tela
Lembradarela çãodeumjogocomosdesenhosemblocosdepapel?Oquedáa
impressãodemovimentoemumblococomoesseéquecadaimagemédesenhada
comumapequenavaria çãodesuaposi çãoanterior.Nenhumdesenho,sevistoin-
dividualmente,daaimpressãodemovimentooucontinuidadedodesenhoanterior.
Écomosecadafolhadoblocofossetotalmenteredesenhadaacadaframe.
Oquefaremosparaqueoplayersemovanatelaézeraratelatodavezque
formosrenderizarumnovoframe.Comonossoprotótipoésimplesenãotemum
fundocomimagenssemovendo,podemosapenasiniciaroframecomumfundo
preto.Parajogoscombackgroundsmaiscomplexosaestratégiadelimparatelaserá
28


## Página 39

CasadoCódigo Capítulo2. Protótipodeumjogo
maiscomplexa.
Naclasse Impossible.m,altereométodo drawRect:parapintaroback-
grounddateladepreto,chamandoonovométodo drawBackgroundInContext:
queiremoscriar:
- (void)drawRect:(CGRect)rect
{
CGContextRef context = UIGraphicsGetCurrentContext();
[self drawBackgroundInContext:context];
[self drawPlayerInContext:context];
}
// Desenha o Plano de Fundo
- (void)drawBackgroundInContext:(CGContextRef)context
{
UIGraphicsPushContext(context);
CGContextSetRGBFillColor(context, 0.0, 0.0, 0.0, 1.0);
CGContextFillRect(context, CGRectMake(0, 0,
self.frame.size.width, self.frame.size.height));
UIGraphicsPopContext();
}
Rodeagoraetoquenatela.Oplayersemoveráacadatoque!
2.5 C riando o inimigo
Chegamosàparteperigosa!Sãoosinimigosquefazemumjogosermaisdesafiador,
quenosinstigamasuperaralgo.Oinimigoemumjogopodeestarrepresentadode
diversasmaneiras.Podeserotempo,podeserumalógicacomplexaaserresolvida
oumesmooutrosobjetosepersonagens.
Apartirdosinimigospodemosconhecerdiversosconceitosimportantespara
umjogofuncionar.Assimcomooplayerprincipal,osinimigospossuemseuspró-
priosmovimentos,porém,diferentementedoplayer,osmovimentosdoinimigocos-
tumamserdefinidosporlógicasinternasdojogo.Ointeressanteéque,pormaisque
os inputsdousuárionãodeterminemdiretamenteomovimentodoinimigo,quanto
maisinteligenteelefordeacordocomamovimenta çãodoplayer,maisinteressante
edesafiadorpodeserojogo.
Paraoprotótipodojogo,nossoinimigoseráumoutrocírculo,porém,comofa-
lamosanteriormente,essecírculoterásuapróprialógica.Elecrescerácomotempo,
29


## Página 40

2.5. Criandooinimigo CasadoCódigo
ouseja,deacordocomopassardojogo,seuraioiráaumentandoeconsequente-
mente,ocupandocadavezmaisaregiãodojogo.
Vamoscriar,naclasse Impossible.h,umapropriedadequerepresentaoraio
doinimigo:
@property (nonatomic) int enemyRadius;
Assim como temos um método separado que desenha o player, na classe
Impossible.mteremosumquedesenhaoinimigo:
- (void)drawRect:(CGRect)rect
{
CGContextRef context = UIGraphicsGetCurrentContext();
[self drawBackgroundInContext:context];
[self drawPlayerInContext:context];
[self drawEnemyInContext:context];
}
//...
// Desenha o Inimigo
- (void)drawEnemyInContext:(CGContextRef)context
{
UIGraphicsPushContext(context);
CGContextBeginPath(context);
CGContextAddArc(context,
100,
100,
self.enemyRadius,
0,
(2 * M_PI),
YES); // Círculo de 360 ° (0 ~ 2pi)
CGContextSetRGBFillColor(context, 0.4f, 0.4f, 0.4f, 1.0f);
CGContextFillPath(context);
UIGraphicsPopContext();
}
Paraestegame,queremosqueacadanovo frameoraiodoinimigocres çaem1.
Paraisto,vamosalteraro run:
30


## Página 41

CasadoCódigo Capítulo2. Protótipodeumjogo
- (void)run
{
if (self.running == YES) {
// Aumenta raio do inimigo
self.enemyRadius++;
// Informa ao iOS que a tela deve ser redesenhada
[self setNeedsDisplay];
}
}
Aorodarojogo,nossoinimigocrescesozinhoeoplayerseafastacomo touch
natela!
31


## Página 42

2.6. Detectandocolisõesemostrandoresultados CasadoCódigo
Figura2.11:Inimigoaparecenatela.
Nessemomentoconseguimosmoveroplayerprincipaletentarseafastardoini-
migoquecrescecadavezmaiscomopassardotempo.Agoraprecisamosdetectara
colisão!
2.6 D etectando colisões e mostrando resultados
Jápassamospeloconceitodemoverobjetos,nocaso,pelotoquenatelaejátambém
porterumoutroobjetoquerepresentaoinimigoetemsuaprópriainteligência.
Agra çadojogoagoraéconseguiridentificarquandoumadeterminadasitua ção
acontece,situa çãoessaqueoplayerestá“lutandocontra”.
Nonossocaso,oplayernãopodeencostarnocírculoquecrescecadavezmais.
32


## Página 43

CasadoCódigo Capítulo2. Protótipodeumjogo
Reparequeaquiaindanãotemosumahistóriaparaqueessacolisãofa çarealmente
sentidoemserevitadanojogo,porém,éaiqueaimagina çãofazojogosetornar
divertido. Jogosantigos,em2D,nãopossuíamgráficosincríveis,massim,ideias
interessantesrepresentadasporobjetossimplesnatela.
Poderíamosestardesenvolvendoumjogonoqualoplayerestáfugindodealgo.
Comoumvulcãoentrouemerup çãoenossoherói(player)devesalvaroshabitantes
dessavila,porexemplo.Ouseja,sabendoosconceitos,iremosincrementarovisual
paraquerepresenteumahistóriainteressante.
Detectando colisões
Precisamosentãoreconhecerqueocirculomaior,querepresentaoinimigo,con-
seguiuencostarnocirculomenor,movidopelousuário,querepresentaoplayer.De-
tectarcolisõeséumassuntomuitoamplo. Existemdiversostiposdedetec çãode
colisõespossíveis.
Umamaneirabemtradicionaléconsiderarquecadaelementoéumquadrado
ouretânguloeverificaratravésdegeometriaseumelementosobrepõeooutro.Essa
formaconsideramesmoelementosquenãocontornamumobjetocomopartedo
mesmo.Naimagemabaixo,umanavedejogosdetiro.Paradetectarquealgocolide
comela,aáreaanalisadapodesergeneralizadaparaumquadradoaoredordela.
33


## Página 44

2.6. Detectandocolisõesemostrandoresultados CasadoCódigo
Figura2.12:Regiãodetectadapelojogo.
Pode-sequestionarseessemétodoébom.Seráque,sealgoencostarnaquinado
quadrado,quenãofazpartedanave,umacolisãoserádetectada?Emmuitoscasos
essaaproxima çãoéfeitapordoismotivos.
• Simplificaçãoparadetectaracolisão.
• Menorexigênciacomputacional.
Simplificaradetec çãoporcontadesimplificaroalgoritmodacolisãoéumaprá-
ticabemcomum. Alémdisso,ébemmaisbaratocomputacionalmentedoqueter
queanalisarcadaitemrealdeumaimagemdeumplayer.
Colisões no protótipo
Chegamosaumdosconceitosmaisimportantesnodesenvolvimentodeum
game! Precisamosidentificaracolisãoentreoplayereoinimigo. Esseéoitem
34


## Página 45

CasadoCódigo Capítulo2. Protótipodeumjogo
chavedonossoprotótipoenormalmentenamaioriadosjogos. Existemdiversas
formasdepontuar,emuitasdelasutilizamacolisãoentredoisoumaisobjetospara
isso. Jogosdetiropontuampelacolisãodotirocomoobjetoatirado. Jogoscomo
SuperMarioBroseStreetFighterpontuampelascolisõesdoplayercommoedasou
cominimigos.
Existemdiversasformasdedetectarcolisões,algumasmaiscomplexasoutras
maissimples.Paraonossoprotótipo,utilizaremosacolisãodeduascircunferências.
Acolisãodedoiscírculoséumadasmaissimples,porém,érelacionadaaalguns
conceitosmatemáticoscomoo Teorema de Pitágoras .
Figura2.13:TeoremadePitágoras.
Nafiguraanterior,existeumamaneiramatematicamentesimplesdedeterminar
35


## Página 46

2.6. Detectandocolisõesemostrandoresultados CasadoCódigo
seascircunferênciasestãosobrepostas.Precisamosidentificarosvaloresaseguir:
• Somadosraiosdasduascircunferências
• Valordahipotenusa,oudistânciaentreosdoisraios
Depossedasduasinforma çõesacima,conseguimosidentificarseasomados
raiosémaiorqueahipotenusagerada.Seformaior,nãoexistecolisão.
Vamosaocódigo!
Primeirocriaremosalgumaspropriedadesparaessecálculo.Asvariáveissere-
feremàsposi çõesXeYdeambasascircunferências,tantodoplayerquantoado
inimigo.
Alteresuaclasse Impossible.hparatertodosessesatributos.Reparequejá
possuíamos enemyRadiuse playerY:
@property (nonatomic) int playerX;
@property (nonatomic) int playerY;
@property (nonatomic) int playerRadius;
@property (nonatomic) int enemyX;
@property (nonatomic) int enemyY;
@property (nonatomic) int enemyRadius;
No initda Impossible.m,vamosdefinirosvalorespadrãodestasproprie-
dades:
- (id)init
{
//...
// Posição inicial do jogador
self.playerRadius = 25;
self.playerX = 160;
self.playerY = 275;
// Posição inicial do inimigo
self.enemyX = 0;
self.enemyY = 0;
self.enemyRadius = 0;
//...
}
36


## Página 47

CasadoCódigo Capítulo2. Protótipodeumjogo
Altereosmétodosdedesenhodoplayereinimigoparaqueutilizemasvariáveis
queforamcriadas:
// Desenha o Player
- (void)drawPlayerInContext:(CGContextRef)context
{
UIGraphicsPushContext(context);
CGContextBeginPath(context);
CGContextAddArc(context,
self.playerX,
self.playerY,
self.playerRadius,
0,
(2 * M_PI),
YES); // Círculo de 360 ° (0 ~ 2pi)
CGContextSetRGBFillColor(context, 0.0f, 0.9f, 0.0f, 1.0f);
CGContextFillPath(context);
UIGraphicsPopContext();
}
// Desenha o Inimigo
- (void)drawEnemyInContext:(CGContextRef)context
{
UIGraphicsPushContext(context);
CGContextBeginPath(context);
CGContextAddArc(context,
self.enemyX,
self.enemyY,
self.enemyRadius,
0,
(2 * M_PI),
YES); // Círculo de 360 ° (0 ~ 2pi)
CGContextSetRGBFillColor(context, 0.4f, 0.4f, 0.4f, 1.0f);
CGContextFillPath(context);
UIGraphicsPopContext();
}
Ométodoqueidentificaacolisãosegueamatemáticaquejávimoseutilizaas
funções pow(power)parapotencia çãoeafun ção sqrt(square root)pararaizqua-
drada.
// Verifica Colisões
37


## Página 48

2.6. Detectandocolisõesemostrandoresultados CasadoCódigo
- (void)checkCollision
{
double distance = 0.0f;
// Teorema de Pitágoras
distance = pow(self.playerY - self.enemyY, 2)
+ pow(self.playerX - self.enemyX, 2);
distance = sqrt(distance);
if (distance <= (self.playerRadius + self.enemyRadius)) {
self.running = NO;
}
}
Adicioneachamadaaométodoquedetectaráacolisão,dentrodonosso run:
// Game Loop
- (void)run
{
if (self.running == YES) {
// Aumenta raio do inimigo
self.enemyRadius++;
// Checa colisões
[self checkCollision];
// Informa ao iOS que a tela deve ser redesenhada
[self setNeedsDisplay];
}
}
Rodeojogo,quandohouvercolisãoentreoinimigoenossoplayer,ojogoirá
parar! Istoaconteceporquequandoocorreacolisãonósalteramosapropriedade
runningparafalso,queéchecadanoiníciodosmétodos rune moveDown.
SeriamaisbonitoumGameOvermaisconvincente,não?Vamoscolocarnatela
umamensagemdeGameOver.Paraostextosdenossogameutilizaremosaclasse
UILabelprópriadoiOS.
Crieumapropriedadequeexibiráotextodegameoverna Impossible.h.
@property (nonatomic, strong) UILabel *gameOverLabel;
38


## Página 49

CasadoCódigo Capítulo2. Protótipodeumjogo
Noinitda Impossible.mvamosinstanciaro label gameOverLabel,sóque
semnenhumtextoparaqueelenãoapare çanatelanestemomento.
- (id)init
{
//...
// Criação do Label que exibirá a mensagem de "Game Over!"
self.gameOverLabel = [[UILabel alloc]
initWithFrame:CGRectMake(20.0f, 40.0f, 300.0f, 50.0f)];
self.gameOverLabel.font = [UIFont systemFontOfSize:40.0f];
self.gameOverLabel.textColor = [UIColor lightGrayColor];
self.gameOverLabel.backgroundColor = [UIColor clearColor];
self.gameOverLabel.text = @"";
[self addSubview:self.gameOverLabel];
//...
}
Aindana Impossible.m,altereométodo checkCollisionparaqueexiba
amensagemdeGameOverquandoocorrerumacolisão.
// Verifica Colisões
- (void)checkCollision
{
double distance = 0.0f;
// Teorema de Pitágoras
distance = pow(self.playerY - self.enemyY, 2)
+ pow(self.playerX - self.enemyX, 2);
distance = sqrt(distance);
if (distance <= (self.playerRadius + self.enemyRadius)) {
self.gameOverLabel.text = @"GAME OVER!";
self.running = NO;
}
}
Apartirdaqui,ojogojádetectaascolisõeseparaemGameOvercasooinimigo
alcanceoplayer. Essaéumamaneiradesepensaremgamesquefoiutilizadapor
muitotempo. Atualmente,comoavan çodohardwareecomvelocidadesdepro-
cessamentocadavezmaiores,detec çõesdecolisõesmuitomaiscomplexasforam
criadas.
39


## Página 50

2.7. Adicionandoumplacar CasadoCódigo
Figura2.14:Playeraparecenatela.
2.7 A dicionando um placar
Vamosveragoraumpróximoconceitoimportanteparaamaioriadosjogos,aatuali-
zaçãodoplacar.Amaioriadosjogosatualizaalgumaformadepontua çãodetempos
emtempos.Essaatualiza çãodeplacarpodeocorrerdediversasformas,comopela
detecçãodecolisõesentreobjetos,porexemplo.Noprotótipooplacarserásimples,
acadatoquenatelaoplayerseafastadoinimigoesemovimenta,ganhandopontos.
Crieapropriedade scorena Impossible.h,alémdeum UILabelqueexi-
biráotextodoscore.Crietambémummétodoqueaumentaoscore:
@property (nonatomic) int score;
40


## Página 51

CasadoCódigo Capítulo2. Protótipodeumjogo
@property (nonatomic, strong) UILabel *gameScoreLabel;
- (void)increaseScore:(int)points;
Na Impossible.mvamosinstanciaro labeldoscoreeimplementarométodo
queaumentaoscore:
- (id)init
{
//...
// Criação do Label que exibirá o score do jogador
self.gameScoreLabel = [[UILabel alloc]
initWithFrame:CGRectMake(20.0f, 85.0f, 300.0f, 30.0f)];
self.gameScoreLabel.font = [UIFont systemFontOfSize:25.0f];
self.gameScoreLabel.textColor = [UIColor whiteColor];
self.gameScoreLabel.backgroundColor = [UIColor clearColor];
self.gameScoreLabel.text = @"0";
[self addSubview:self.gameScoreLabel];
//...
}
// Soma Pontos
- (void)increaseScore:(int)points
{
if (self.running == YES) {
self.score += points;
self.gameScoreLabel.text = [NSString stringWithFormat:@"%d",
self.score];
}
}
Nométodoquerecebeoeventodetoque,incrementaremosospontos.Atualize
ométodo handleTapGesture:doarquivo GameViewController.m:
- (void)handleTapGesture:(UITapGestureRecognizer *)gesture
{
if (gesture.state == UIGestureRecognizerStateEnded) {
[self.impossibleView moveDown:10];
[self.impossibleView increaseScore:100];
}
}
41


## Página 52

2.8. Criandobotõesdeinterfacedousuário CasadoCódigo
Ojogodeveestarassim:
Figura2.15:Scoreaparecenatela.
2.8 C riando botões de interface do usuário
Outroconceitoimportanteemjogoséapossibilidadedeinteragircomelementos
deconfigura çãodogame.Poderpausarojogo,entraremumatelaparamudar,por
exemplo,adificuldadeoumesmofecharesairdojogosãopartesimportantedo
desenvolvimento.
Noprotótipo,ilustraremosesseconceitocomduasop çõesnatela,para Restart
(reiniciar)e Stop(parar).Simplificaremosparaentenderoconceito,edepois,pode-
remosconverterparabotõesmaisinteressantes.
42


## Página 53

CasadoCódigo Capítulo2. Protótipodeumjogo
Noarquivo GameViewController.mcrieosbotõesemétodosparao Restart
e Stop:
- (void)viewDidLoad
{
//...
// Botão para Reiniciar o jogo
UIButton *buttonRestart =
[UIButton buttonWithType:UIButtonTypeCustom];
[buttonRestart setTitle:@"Restart"
forState:UIControlStateNormal];
buttonRestart.contentHorizontalAlignment =
UIControlContentHorizontalAlignmentLeft;
buttonRestart.frame = CGRectMake(20.0f, 170.0f, 80.0f, 35.0f);
[buttonRestart addTarget:self
action:@selector(restart:)
forControlEvents:UIControlEventTouchUpInside];
[self.view addSubview:buttonRestart];
// Botão para Parar o jogo
UIButton *buttonStop =
[UIButton buttonWithType:UIButtonTypeCustom];
[buttonStop setTitle:@"Stop" forState:UIControlStateNormal];
buttonStop.contentHorizontalAlignment =
UIControlContentHorizontalAlignmentLeft;
buttonStop.frame = CGRectMake(20.0f, 250.0f, 80.0f, 35.0f);
[buttonStop addTarget:self
action:@selector(stop:)
forControlEvents:UIControlEventTouchUpInside];
[self.view addSubview:buttonStop];
}
- (void)restart:(id)sender
{
// Reinicia o jogo
// Já vamos aprender o que fazer aqui!
}
- (void)stop:(id)sender
{
// Para o jogo
43


## Página 54

2.8. Criandobotõesdeinterfacedousuário CasadoCódigo
// Já vamos aprender o que fazer aqui!
}
Rodeojogoevejaqueosbotõesde Restarte Stopjáaparecemnatela.
Figura2.16:BotõesdeRestarteStopnatela.
Agora,precisaremosdeumaformadepararereinicializaraspropriedadesdo
game.Noarquivo Impossible.hdefinaosmétodos restarte stopGame:
- (void)restart;
- (void)stopGame;
Noarquivo Impossible.mimplementeestesmétodos. Repareque,parao
restart,utilizaremosumaabordagemsimplesdereinicializa ção.
44


## Página 55

CasadoCódigo Capítulo2. Protótipodeumjogo
// Para o Jogo
- (void)stopGame
{
self.running = NO;
}
// Reinicia o jogo, redefinindo as variáveis
- (void)restart
{
self.enemyX = 0;
self.enemyY = 0;
self.enemyRadius = 0;
self.playerRadius = 25;
self.playerX = 160;
self.playerY = 275;
self.score = 0;
self.gameScoreLabel.text = @"0";
self.gameOverLabel.text = @"";
self.running = YES;
}
Precisamosagoraalterarparaqueotoquedosbotõeschameestesmétodosda
classe Impossible.Na GameViewController.m,altereosmétodos restart:
e stop::
- (void)restart:(id)sender
{
[self.impossibleView restart];
}
- (void)stop:(id)sender
{
[self.impossibleView stopGame];
}
Atelafinaldoprotótipodeveestarassim:
45


## Página 56

2.9. Adicionandomaisvida:imagensdanaveedocéu CasadoCódigo
Figura2.17:Protótipofinal.
2.9 A dicionando mais vida: imagens da nave e do céu
Temostodaalógicadoprotótiporodandoejápodemos,finalmente,alteraralguns
elementosvisuaisparafinalizaroprotótipodojogoefecharosconceitosbásicos.
Vamosdesenharum backgroundquesimuleumcéuescurocomestrelas.Para
isso,utilizaremosaimagem sky.png.Umpontoimportanteérepararquequanto
maisspritesforemadicionadosaojogo,maisesfor çocomputacional,oquepode
tornarojogomaislento.Maisafrente,utilizaremos frameworksqueotimizamessa
questão.
Adicioneosarquivos sky.pnge nave.pngnodiretóriodoprojeto.Vocêpode
46


## Página 57

CasadoCódigo Capítulo2. Protótipodeumjogo
fazeristopeloXcodeclicandonapasta Impossibledoprojeto,eacessandoomenu
File, Add Files to "Impossible"... .
Vamos alterar algumas linhas para utilizar as imagens. No método
drawBackgroundInContext:daclasse Impossibleadicioneaslinhasquede-
senharãoumaimagemcomo backgrounddogame.
// Desenha o Plano de Fundo
- (void)drawBackgroundInContext:(CGContextRef)context
{
// UIGraphicsPushContext(context);
// CGContextSetRGBFillColor(context, 0.0, 0.0, 0.0, 1.0);
// CGContextFillRect(context, CGRectMake(0, 0,
// self.frame.size.width,
// self.frame.size.height));
// UIGraphicsPopContext();
// Utiliza uma imagem do projeto e a desenha em um
// determinado ponto da tela
UIImage *image = [UIImage imageNamed:@"sky.png"];
[image drawAtPoint:CGPointMake(0.0f, 0.0f)];
}
Altereométodo drawPlayerInContext:pararenderizaraimagemdanave.
// Desenha o Player
- (void)drawPlayerInContext:(CGContextRef)context
{
// UIGraphicsPushContext(context);
// CGContextBeginPath(context);
// CGContextAddArc(context,
// self.playerX,
// self.playerY,
// self.playerRadius,
// 0, (2 * M_PI),
// YES); // Círculo de 360 ° (0 ~ 2pi)
// CGContextSetRGBFillColor(context, 0.0f, 0.9f, 0.0f, 1.0f);
// CGContextFillPath(context);
// UIGraphicsPopContext();
// Utiliza uma imagem do projeto e a desenha em um
// determinado ponto da tela
47


## Página 58

2.9. Adicionandomaisvida:imagensdanaveedocéu CasadoCódigo
UIImage *image = [UIImage imageNamed:@"nave.png"];
[image drawAtPoint:CGPointMake(
(self.playerX - (image.size.width / 2)),
(self.playerY - (image.size.height / 2)))];
}
Altereacordoinimigoparavermelho.
// Desenha o Inimigo
- (void)drawEnemyInContext:(CGContextRef)context
{
UIGraphicsPushContext(context);
CGContextBeginPath(context);
CGContextAddArc(context,
self.enemyX,
self.enemyY,
self.enemyRadius,
0,
(2 * M_PI),
YES); // Círculo de 360 ° (0 ~ 2pi)
//CGContextSetRGBFillColor(context, 0.4f, 0.4f, 0.4f, 1.0f);
CGContextSetRGBFillColor(context, 1.0f, 0.0f, 0.0f, 1.0f);
CGContextFillPath(context);
UIGraphicsPopContext();
}
Poderodarojogo,oprotótipoestácomspriteseconceitosfundamentaisdeum
jogo!
48


## Página 59

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.18:Imagemdojogo.
2.10 C onclusão
Umjogopossuidiversosconceitosbemespecíficos,quenãosãocomunsemoutros
tiposdeprojetosde softwarecomo webou desktop.Paradesenvolverumjogoéinte-
ressanteterbemesclarecidasaspartesprincipaisquecompõemoquebra-cabe çado
mundodaprograma çãoparagames.
Umjogoocorrenormalmenteemum loop infinito,noqual inputs,ouseja,
entradasdecomandos,sãointerpretadoseutilizadosparaexecutaraslógicasdo
game.Omovimentodoplayer,normalmenteumaimagemchamada spritecos-
tumaserdadoapartirdesses inputs,assimcomoomovimentodosinimigos,que
49


## Página 60

2.10. Conclusão CasadoCódigo
indiretamente,tambémécalculado.
Conceitosperiféricoscomo atualização da tela , limpeza da tela e
botões de comandos tambémsãoimportantesedevemsertodosmuitobem
pensadosnaexecu çãodojogo.
Comissoemmente, podemosplanejarnossojogoeiniciarseudesenvolvi-
mento.
50


## Página 61

Capítulo3
Históriadojogo
Jogossãofeitosdemagia,deilusão,defantasia.Sãohistóriasqueenvolvemaspes-
soasdeumaformapoderosa,naqualousuáriosesenteoprotagonistaestandono
comandodasa ções.
Nocome çodolivrofalamossobreumjogofantásticochamado River Raid,
alémdedesenvolverumprotótipodejogodeaviãonocapítuloanterior.Poisbem,
chegouahora!
Massecriarmosumjogodenave,qualapeloeleterá?Oqueodiferenciarádos
miloutrosjogosquepodemosencontrarnaAppStore?Oquefaráprenderaaten ção
dojogador?
Oenredo,ospersonagenseacarismasãope çasfundamentaisquevestemum
jogo.Érealmenteimportanteconsiderarumtemachamativoquesejadiferentedo
quejáestamosacostumados.Comofazeralgoumpoucodiferenteemumjogode
naves?Comotrazerissoparaumcontextocomoqualosnossosjogadoresestejam
familiarizados?
Criaremosumjogotambémcomatemáticadeaviões,comoumahomenagem


## Página 62

3.1. 14-bis CasadoCódigo
aumimportantebrasileiroqueparticipoudoiniciodessarevolu çãoaérea.
Em1873nasciaAlbertoSantosDumont,umpiloto,atletaeinventorbrasileiro.
Figura3.1:AlbertoSantosDumont
SantosDumontprojetou,construiuevoouosprimeirosbalõesdirigíveiscom
motoragasolina,conquistandooPrêmioDeutschem1901,quandocontornoua
TorreEiffel. Setornouentãoumadaspessoasmaisfamosasdomundoduranteo
séculoXX.
3.1 14- bis
Em1906,SantosDumontcriouumaviãohíbridochamado14bis,consideradoo
primeiroobjetomaispesadoqueoarasuperaragravidadeterrestre.
52


## Página 63

CasadoCódigo Capítulo3. Históriadojogo
Figura3.2:14-bisdobrasileiroSantosDumont
O pesadelo de Santos Dumont
Emagostode1914come çavaaPrimeiraGuerraMundialeosaviõescome çaram
aserutilizadosemcombatesaéreos. Aguerraficoucadavezmaisviolenta,com
metralhadorasebombas.SantosDumontviuseusonhosetransformarempesadelo.
Em1932,umconflitoentreoestadodeSãoPauloeogovernodeGetúlioVargas
foiiniciadoeaviõesatacaramacidade. EssavisãocausoumuitaangustiaaSantos
Dumont,quecometeusuicídio.
3.2 14- bisVS 100 Meteoros
SantosDumontinventouo14-bisnãocomointuitodeguerra.Nessejogo,homena-
gearemosDumontesuainven çãoutilizandosuaaeronaveparasalvaroplaneta!
DepoisdometeoroShoemaker-Levy-9quecaiuemJúpiter,depoisdometeoro
quecaiunaRússiaem2013,tudoindicavaqueofimestavapróximo. Oexército
brasileirodetectouapresen çade100meteorosentrandonaórbitaterrestre! Esses
meteorosacabarãocomaexistênciadetodaformadevidaqueconhecemoscasonão
sejamdetidosurgentemente.
53


## Página 64

3.2. 14-bisVS100Meteoros CasadoCódigo
Figura3.3:14-bisVS100Meteoros
Oplanetaestáemapuros!Todasaspartesdomundosófalamnesseassuntoe
buscamformasdeevitarofim.Eisquesurgeumbrasileiro,comseuinvento14-bis,
paraenfrentaroperigoetentarsalvaratodosnós.Munidodeumaarmapoderosa
paradestruirosmeteorosquecaemsobreaTerra,vocêcomandaráaaeronave14-bis
nessaaventura!
54


## Página 65

CasadoCódigo Capítulo3. Históriadojogo
Figura3.4:Fluxodogame14-bisVS100Meteoros
55


## Página 67

Capítulo4
Telainicial:Lidandocom
Background,logoebotõesdemenu
Horadecome çarojogodeverdade!Agoraquejápassamospelosconceitosbásicos
dedesenvolvimentodejogoscomo game loop, sprites,colisõese inputs,podemosir
umpoucomaisafundonodesenvolvimento.
Vamoscriarumjogobaseadonogamedocapítuloanterior,porémdessavez
utilizandoum frameworkdedesenvolvimentodejogoschamadoCocos2D.Omotivo
deutilizarum frameworkdaquiprafrenteéotimizardiversosaspectos,dentreeles:
• Nãosepreocuparcomaposiçãoexataempontos/pixelsdosobjetos,como
botões,porexemplo
• Utilizarcomportamentosjáimplementadosparasprites,paranãoterproble-
mascomposicionamentodasimagens
• Eliminardalógicaaquestãodalimpezadetela,deixandoissocomorespon-
sabilidadedo framework


## Página 68

CasadoCódigo
• ConseguirefeitosinteressantesjáimplementadospeloCocos2D
• Trabalharmaisfacilmentecomsonseefeitos
Nessecapítulocriaremosatelainicial,queserácompostaporumlogo,umback-
ground,equatrobotões.Veremosaquicomoposicionarcadaumdesseselementos
natelaecomodetectaros inputsdosbotõesutilizandooCocos2D.Aofimdocapí-
tulo,devemosteratelainicialcomoaseguir:
Figura4.1:Teladeabertura.
Vocêpoderáencontrarocódigocompletodojogo,juntocomalgumasmelho-
rias,noGitHub:
https://github.com/BivisSoft/jogos_ios_14bis
58


## Página 69

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
Masprefiravocêmesmoescrevê-lo!Serámenostrabalhosodoquevocêimagina,
ecertamenteajudarámuitonoseuaprendizado.
4.1 S obre o Cocos2D
OCocos2Dé framework open sourcededesenvolvimentodejogos.Aversãooriginal
foicriadaemPythonedesdeentãofoiportadaparadiversaslinguagenscomoC++,
JavaScript,Objective-CeJava.Émuitopoderosoesimples.
ParautilizaraversãoparaiOS,bastabaixá-lonoseguinteendere ço:
http://www.cocos2d-iphone.org/download/
Apósbaixado,vocêdeveinstalarostemplatesdoCocos2Dparaquepossainiciar
umprojetojáutilizandoo framework. Extraiaoarquivobaixado,abraoTerminal
enavegueatéodiretórioondeoCocos2Dfoiextraído.Depois,executeocomando
./install-templates.sh -f.
$ cd cocos2d-iphone
$ ./install-templates.sh -f
4.2 I niciando o projeto
VamosiniciarcriandoumnovoprojetonoXcode,porém,destavezutilizaremosum
templatedoCocos2Dcomobase.AbraoXcodeeváem File,acesseasop çõesem
Neweselecione Project...paracriarumnovoprojeto.
Atelaparaescolherumtemplatedeprojetoseráaberta.Nomenuàesquerda,na
seção iOSselecioneaop ção cocos2d v2.x.Àdireita,selecione cocos2d iOS
ecliqueem Next.
59


## Página 70

4.2. Iniciandooprojeto CasadoCódigo
Figura4.2:NovoprojetodeCocos2D.
Criaremosumprojetochamado Bis.Onomedobundleficaráàseucritério,mas
vocêpodeseguirasugestãodeusar br.com.casadocodigo.bis.Dessaforma
vocêpoderásempreacompanharcomfacilidadeocódigofontecompletoqueestá
noGitHubemhttps://github.com/BivisSoft/jogos_ios_14bis.Comonossojogoserá
apenasparaiPhone,nocampo Deviceescolha iPhone.
60


## Página 71

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
Figura4.3:CriandooprojetoCocos2D.
Cliqueem Nexteescolhaolocalondeoprojetoserágravado.
Nessemomentotemosoprojetoiniciado.Execute-oeosimuladordeveráexibir
umatelaescrito Hello World:
Figura4.4:SimuladorcomHelloWorlddoCocos2D.
61


## Página 72

4.3. ajustandoaorientação CasadoCódigo
Vocêpercebeuosnúmerosqueaparecemnocantoinferioresquerdodosimula-
dor?Estesnúmerosindicamoconsumodememória,tempoentreum game loope
outro,eaquantidadede framesporsegundo.Estasinforma çõessãobastanteúteis
casovocêpercebaqueseujogoestámuitolentoequeiraverificaraquevelocidade
eleestásendoexecutado.
Para nosso game, vamos retirar estes números da
tela. Para isto, no arquivo AppDelegate., no método
application:didFinishLaunchingWithOptions: vamos alterar a op-
çãodeexibirFPSpara não:
//...
// Display FSP and SPF
[director_ setDisplayStats:NO];
//...
4.3 ajustando a orientação
Porpadrão,oCocos2Diniciaumnovoprojetocomaorienta çãodoaparelhoem
modopaisagem. Paranossogame, alteraremosoprojetopararodarojogoem
modoretrato. Abraasconfigura çõesdoprojetoem Supported Interfaces
Orientationsemarqueapenasaop ção Portrait:
Figura4.5:Configurandoprojetoemmodoretrato.
No AppDelegate.m, dentro do @implementation da
MyNavigationController, altere os seguintes métodos padrões para que a
telanãogirequandooaparelhomudardeposi ção:
- (NSUInteger)supportedInterfaceOrientations
{
return UIInterfaceOrientationMaskPortrait;
}
62


## Página 73

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
- (BOOL)shouldAutorotateToInterfaceOrientation:
(UIInterfaceOrientation)interfaceOrientation
{
return interfaceOrientation == UIInterfaceOrientationPortrait;
}
RodeogameeagoraoHelloWorlddeveráapareceremmodoretrato:
Figura4.6:SimuladorcomHelloWorldemmodoretrato.
63


## Página 74

4.4. Background CasadoCódigo
4.4 B ackground
Aprimeirateladogameéateladeabertura,enoCocos2D,utilizamosumaclasse
chamada CCLayerparaidentificarcadateladojogo. Aoherdardessaclassedo
framework,ganhamosalgunsreconhecimentosdoCocos2D,comoconseguirfazer
atransi çãoentreastelascomapenasumalinhadecódigo.
Umaclassequeherdade CCLayernãoprecisatermuitoscódigosdo framework,
podemoscriarnossatelainicialcomobementendermos,apenasutilizandoesse
comportamentoparainformarao frameworkquetipodeobjetoestamosrepresen-
tando.
Layers
Criartelascomo CCLayerdoCocos2Décriartelaspensandoemcamadasque
sesobrepõem.Essascamadassãotransparentes,amenosquandodefinidasdeoutra
forma,equandocolocadasumasobreasoutrasdefinematelafinal.
Nateladeabertura,podemospensaremcamadasparaaimagemde background,
paraologoeparaomenu.
Criaremosumaclassechamada TitleScreen.Vocêpodecriá-lanodiretório
ougrupodoprojetoquedesejar.Nonossoprojeto,utilizamosodiretório Scenes.
Lembre-sedeorganizarsuasclassesemgrupossignificativos.
Nestaclasse,utilizaremosumsegundocomponentedoCocos2D.Parainstanciar
umatelano framework,utilizamosaclasse CCScene,queédevolvidajáprontapara
utilizarmosquandoinvocamosométodo node.
Scenes
OutroobjetoimportantedoCocos2Dsãoas Scenes.Comelas,conseguimos
inicializartelasdojogo.Umjogopodeterquantas Scenesforemnecessárias,po-
rémapenasumaestaráativaporvez.
Porexemplo,nonossojogoteremosateladeabertura,ateladojogo,atelade
ajuda,ateladepauseetc.Cadaumadelaséum Scene.
Vamosaocódigoinicialdateladeabertura.Precisamosdeumaclassequesaiba
trabalharcomcamadasedeumatela. Criaremosaclasse TitleScreenquere-
ceberáessasdefiniçõesdecamadaseaadicionaremosemuma Scene,formandoa
basedatelainicial.
Criaremosométodo scene,responsávelporinstanciarnossaclasseeretorná-la
dentrodeuma Scene. Vocêperceberáaolongodolivroquetodasasscenesque
64


## Página 75

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
criarmosterãoestemétodo.
Noheader TitleScreen.hiremosdeclararométodo scene:
# import "cocos2d.h"
@interface TitleScreen : CCLayer
+ (CCScene *)scene;
@end
Eno implementation TitleScreen.mvamosimplementarométodo. Você
podecopiá-lodaclasse HelloWorldLayer,criadapeloCocos2D.
+ (CCScene *)scene
{
// 'scene' is an autorelease object.
CCScene *scene = [CCScene node];
// 'layer' is an autorelease object.
TitleScreen *layer = [TitleScreen node];
// add layer as a child to scene
[scene addChild:layer];
// return the scene
return scene;
}
Ocódigoanteriorpreparaatelaparautiliza çãoeposicionamentodoselementos,
nonossocaso,esseselementosserão background,logoebotões.
Vamosiniciarconfigurandoo backgrounddogame.Assimcomobotõesoulogo,
o backgroundtambéméumobjetorepresentadoporumaimagem.Lembre-seque
paramanipularimagenstemosoconceitode Sprites,quebasicamenteéumob-
jetoassociadoàumafigura.
Sprites
Um SpritenoCocos2DécomoqualqueroutroSprite,ouseja,umaimagem
2Dquepodesermovida,rotacionada,animada,tersuaescalaalteradaetc.Umasdas
65


## Página 76

4.4. Background CasadoCódigo
vantagensdeutilizar SpritescomoobjetosdoCocos2Déqueganhamosalgumas
possibilidadesdeanima ção,queveremosmaisàfrente.
Criaremosentãoumspritequerepresentanosso backgroundeiremosadicioná-
loàteladeabertura. Paraisto,instanciamosumobjetodotipo CCSpriteinfor-
mandoqualaimagemdesejadaeconfiguramossuaposi ção. Aqui,utilizaremos
otamanhodatela,tantolarguraquantoaltura,paraposicionaro backgroundde
formacentralizada.FaremosissocomumelementomuitoimportantedoCocos2D,
o CCDirector,queseráaprofundadomaisàfrente.Vamosadicionaro background
nateladeabertura,instanciando-ono initda TitleScreen.m:
- (id)init
{
self = [super init];
if (self) {
// Imagem de Background
CCSprite *background =
[CCSprite spriteWithFile:@"background.png"];
background.position =
ccp([CCDirector sharedDirector].winSize.width / 2.0f,
[CCDirector sharedDirector].winSize.height / 2.0f);
[self addChild:background];
}
return self;
}
DamesmaformaqueacontecenosdemaisaplicativosdeiOS,podemosteruma
imagemparaaparelhosdetelanão-retinaeoutracomodobroderesolu çãopara
aparelhoscomtelaretina.Entretanto,aoinvésdeutilizararquivoscomfinal“@2x”,
oCocos2Dutilizaarquivoscomfinal“-hd”paraidentificarumaimagemparatela
retina.
OCocos2Djávemhabilitadoparautilizarimagensretinaereconhecê-lascomo
arquivos com final “-hd”. Estas configurações vêm definidas como padrão no
Appdelegate.m.Bastaapenasincluirasimagensemambasresolu çõesnoprojeto
eoCocos2Dvaiutilizarumaououtraautomaticamente.
Precisamosentãodo background.pnge background-hd.pngdonosso
jogo. Criamosalgumasimagenseutilizamosoutrasdefontesgratuitasparanosso
jogo.Vocêpodebaixarumzipqueascontémnesseendere ço:
https://github.com/bivissoft/jogos_ios_14bis
66


## Página 77

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
Coloqueosarquivos background.pnge background-hd.pngdentrododi-
retório Resourcesdoseuprojeto.Vocêprecisarárepetiresseprocedimentopara
outrasimagens,sonsearquivosdosquaisprecisaremosnodecorrerdodesenvolvi-
mentodenossojogo.
4.5 A ssets da Tela de abertura
Ateladeaberturadogameterá6 assets(arquivoscomoimagensefiguras)queserão
utilizadosparacomporlogoemenus.
Paracome çar,vamosorganizarnaclasse Assetsosarquivosdeimagensque
utilizaremosnogame.Crieaclasse Assets,subclassedeum NSObject,eemseu
headerdeclareasimagensqueutilizaremos:
@interface Assets : NSObject
# define kBACKGROUND @"background.png"
# define kLOGO @"logo.png"
# define kPLAY @"play.png"
# define kHIGHSCORE @"highscore.png"
# define kHELP @"help.png"
# define kSOUND @"sound.png"
@end
Parafacilitar,importaremosaclasse Assetsemnossoarquivo Prefix.pch.
Desta forma, todas as classes de nosso projeto automaticamente importarão a
Assets. Tambémincluiremosna Prefix.pcho importda cocos2d.h,outra
classequeserábastanteutilizadaemnossoprojeto.
//...
# ifdef __OBJC__
# import <UIKit / UIKit.h>
# import <Foundation / Foundation.h>
# import "cocos2d.h"
# import "Assets.h"
# endif
Sempreapósalteraroarquivo Prefix.pch,precisamosrecompilarnossopro-
jetoparaqueasclassesidentifiquemasaltera ções.Vocêpodefazeristoacessandoo
menu Productsegurandoatecla optioneselecionando Clean Build Folder .
Apósisto,acessenovamenteomenu Producteselecione Build.
67


## Página 78

4.6. Capturandoconfiguraçõesiniciaisdodispositivo CasadoCódigo
Agora,alterealinhada TitleScreen.mquechamavao background.png
parautilizaraconstantedaclasse Assets:
//...
CCSprite *background = [CCSprite spriteWithFile:kBACKGROUND];
//...
Utilizaremosessaclasseparaadicionaroutros assetsposteriormente,quandoos
objetosinimigoseoplayerforemdesenhados. Éimportanteterumaclassecomo
essaparanãoespalharsuasimagenspelocódigo. Porexemplo,imaginequevocê
queiraalteraraimagemdanaveprincipal.Émelhoralterá-laemapenasumlugar,e
fazerreferênciaaessavariávelnasclassesnecessárias.
4.6 C apturando configurações iniciais do disposi -
tivo
ExistemdiversosdispositivosiOSatualmente, comdiferentestamanhosdetela.
Existemalgumastécnicasparatentarlimitaresseproblemaduranteodesenvolvi-
mentodojogo.Utilizaremosaquiumatécnicasimplesparaadaptarnossoconteúdo
aosdiversosdispositivos,capturandoasmedidaseutilizando-ossemprequeforne-
cessáriolidarcomessaquestão.
Parainiciarasconfigura çõesdetelaecriaratelainicial,criaremosalgumasma-
cros:
•SCREEN_WIDTH():Retornaalarguradatela
•SCREEN_HEIGHT():Retornaaalturadatela
•WIN_SIZE():Retornaotamanho(larguraealtura)datela
OCocos2Dnosajudanessemomento,poisjápossuiobjetospreparadospara
executaressafun ção. Podemosutilizaraclasse CCDirectorparaconseguiros
parâmetrosdatela.
Avantagemdeutilizarumamacro,équecasohajanecessidade,poderemos
alterá-lapararesponderpordiferentestamanhosdetelaparacadatipodeaparelho.
68


## Página 79

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
Director
O CCDirectoréocomponenteprincipalqueexecutaogame. Éelequem
controlaoFPS,tamanhodatela,resolu ção,etambémcuidadastransi çõesentre
scenes,ouseja,transi çõesdetelasdojogo. Eleéum Singletonquesabequal
telaestáativanomomentoegerenciaumapilhadetelas,aguardandosuaschamadas
parafazerastransi ções.
Vamos criar a classe DeviceSettings, responsável por acessar o
CCDirectoreretornarasmedidaseconfigura çõesdodispositivo.
Crieaclasse DeviceSettings,subclassedeum NSObject,enoheaderdela
declareasseguintesmacros:
# define SCREEN_WIDTH() \
[CCDirector sharedDirector].winSize.width
# define SCREEN_HEIGHT() \
[CCDirector sharedDirector].winSize.height
# define WIN_SIZE() \
[CCDirector sharedDirector].winSize
Comoimportaremosa DeviceSettingsemdiversasoutrasclassesdoprojeto,
vamosaproveitareincluí-laemnossoarquivo Prefix.pch:
//...
# ifdef __OBJC__
# import <UIKit / UIKit.h>
# import <Foundation / Foundation.h>
# import "cocos2d.h"
# import "Assets.h"
# import "DeviceSettings.h"
# endif
Comisso,podemosrefatoraroposicionamentodo backgroundno initda
TitleScreen.mparaficarcomoaseguir.
//...
background.position = ccp(SCREEN_WIDTH() / 2.0f, SCREEN_HEIGHT() / 2.0f);
//...
O CCDirectorétambémresponsávelpelainicializaçãodateladeabertura.
69


## Página 80

4.6. Capturandoconfiguraçõesiniciaisdodispositivo CasadoCódigo
Iniciando a tela de abertura
Telainicialpreparada! Agoraprecisamosfazeratransi ção,ouseja,devemos
informaraoCocos2Dparainiciarateladeabertura.
Sempre após iniciar o game, o Cocos2D irá chamar a scene padrão
IntroLayer.Estasceneéumatelabemsimpleseleve,queérapidamentecarre-
gadaaoabriroaplicativo,evitandoqueatela“pisque”atransiçãoentrenossa Splash
Screeneatelainicialdogame.
Primeiramente, vamos ajustar a orientação da imagem exibida em nossa
IntroLayer. Altereométodo initda IntroLayer.mparanãogirarnossa
imagemdeabertura:
-(id) init
{
if( (self=[super init])) {
// ask director for the window size
CGSize size = [[CCDirector sharedDirector] winSize];
CCSprite *background;
if( UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPhone ) {
background =
[CCSprite spriteWithFile:@"Default-568h@2x.png"];
//background = [CCSprite spriteWithFile:@"Default.png"];
//background.rotation = 90;
} else {
background =
[CCSprite spriteWithFile:@"Default-Landscape~ipad.png"];
}
background.position = ccp(size.width/2, size.height/2);
// add the label as a child to this Layer
[self addChild: background];
}
return self;
}
Agoravamosalterara IntroLayer.mparaquechamenossa TitleScreen
apósaberturadogame.UmobjetomuitoimportantedoCocos2Dseráutilizadopara
70


## Página 81

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
essecontrole. Utilizaremoso CCDirectornovamente,dessavezparaapresentar
umanovatela,utilizandoométodo replaceScene:epassandocomoparâmetro
a TitleScreen,queénossatelainicial.
# import "TitleScreen.h"
//...
@implementation IntroLayer
//...
-(void) onEnter
{
[super onEnter];
[[CCDirector sharedDirector] replaceScene:
[CCTransitionFade transitionWithDuration:1.0
scene:[TitleScreen scene] ]];
}
@end
Jáépossívelrodaroprojetoeverateladeaberturacomo backgroundconfigu-
rado!Fa çaoteste.
4.7 L ogo
Vamosutilizaramesmaideiaecolocarumlogodojogonotopodatela.
Ologoéumaimagemsimpleseimagenssãocoordenadasporobjetosquecha-
mamosde Sprites. Criaremosum Spritedeformasimplesparaposicionar
ologoeutilizaremosométodo setPosition:paraqueoCocos2Dsaibaonde
colocaroelemento.
Prafinalizar,bastaadicionarologoàtelainicialcomométodo addChild:.
Mudeo initdesua TitleScreen.m:
- (id)init
{
self = [super init];
if (self) {
//...
// Imagem de Logo
CCSprite *title = [CCSprite spriteWithFile:kLOGO];
title.position =
ccp(SCREEN_WIDTH() / 2.0f, SCREEN_HEIGHT() - 130.0f);
71


## Página 82

4.8. Botões CasadoCódigo
[self addChild:title];
}
return self;
}
@end
Aorodaroprojetojátemosasimagensdebackgroundelogodojogoposicio-
nados.
4.8 B otões
Osbotõessãopartesimportantíssimasdojogo.Éapartirdelesqueousuáriointerage
comogameequerecebemoscomandosparatransicionarastelase,maisàfrente,
moveroplayer,atiraretc.
UtilizandooCocos2Dotrabalhocom inputsdebotõesficabemmaissimples,
nãoprecisandodetectaraposi çãodotoquenatelaecompararcomoposiciona-
mentodos Sprites.Essetrabalhoseráfeitopelo frameworkeojogopodesepre-
ocuparcomalógicaemsi.
NoCocos2D,aclasse CCMenuItemesuassubclassesrepresentamosbotões,ea
classe CCMenurepresentaomenuondeestesbotõesestarãoposicionados.Comestas
classes,oCocos2Djásabeseestamostocandoemumbotão,seestamossegurando-
o,ouseosoltamos.
Oqueprecisamosagoraé:
• Criaros4botões:Play,Highscore,HelpeSound.
• Configurarsuasposições
• Adicioná-losàtelainicial
No initda TitleScreen.m,criaremosnossomenucomosbotões:
- (id)init
{
self = [super init];
if (self) {
//...
72


## Página 83

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
// Cria os botões
CCMenuItemSprite *playButton = [CCMenuItemSprite
itemWithNormalSprite:[CCSprite spriteWithFile:kPLAY]
selectedSprite:[CCSprite spriteWithFile:kPLAY]
target:self
selector:@selector(playGame:)];
CCMenuItemSprite *highscoreButton = [CCMenuItemSprite
itemWithNormalSprite:[CCSprite spriteWithFile:kHIGHSCORE]
selectedSprite:[CCSprite spriteWithFile:kHIGHSCORE]
target:self
selector:@selector(viewHighscore:)];
CCMenuItemSprite *helpButton = [CCMenuItemSprite
itemWithNormalSprite:[CCSprite spriteWithFile:kHELP]
selectedSprite:[CCSprite spriteWithFile:kHELP]
target:self
selector:@selector(viewHelp:)];
CCMenuItemSprite *soundButton = [CCMenuItemSprite
itemWithNormalSprite:[CCSprite spriteWithFile:kSOUND]
selectedSprite:[CCSprite spriteWithFile:kSOUND]
target:self
selector:@selector(toggleSound:)];
// Define as posições dos botões
playButton.position = ccp(0.0f, 0.0f);
highscoreButton.position = ccp(0.0f, -50.0f);
helpButton.position = ccp(0.0f, -100.0f);
soundButton.position = ccp((SCREEN_WIDTH() / -2.0f) + 70.0f,
(SCREEN_HEIGHT() / -2.0f) + 70.0f);
// Cria o menu que terá os botões
CCMenu *menu = [CCMenu menuWithItems:playButton,
highscoreButton,
helpButton,
soundButton,
nil];
[self addChild:menu];
}
return self;
}
@end
73


## Página 84

4.9. Conclusão CasadoCódigo
Perceba que nossos botões foram criados utilizando a classe
CCMenuItemSprite, que representa um botão com uma imagem (sprite).
Existemdiversostiposdebotões,taiscomoo CCMenuItemLabelparatextos,o
CCMenuItemImagepara UIImages,entreoutros.Porpadrão,osbotõesincluídos
nomenuserãocentralizadosnomeiodatela.Ouseja,aoposicionarumbotãona
posição (0,0),eleapareceránocentrodatela.
Quandocriamososbotões,informamososparâmetros targete selector,
queindicamosmétodoschamadoscadavezqueumbotãoforselecionado. Falta
apenascriarestesmétodosemnossa TitleScreen.m:
- (void)playGame:(id)sender
{
NSLog(@"Botão selecionado: Play");
}
- (void)viewHighscore:(id)sender
{
NSLog(@"Botão selecionado: Highscore");
}
- (void)viewHelp:(id)sender
{
NSLog(@"Botão selecionado: Help");
}
- (void)toggleSound:(id)sender
{
NSLog(@"Botão selecionado: Som");
}
Rodeoprojetoeconfiraosbotõesrecebendoos inputsno console.
4.9 C onclusão
Ojogodeveestarcomomostradonatelaabaixo,com backgroundelogoconfigura-
dos. Alémdisso,4botõesforamimplementados:Play,Highscore,Helpecontrole
deSom.
74


## Página 85

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
Figura4.7:Teladeabertura.
O coredodesenvolvimentodeumjogonãoéfácil.Reparenaevolu çãodopro-
tótipoparaojogorealqueestamoscriandoeperceberáquepartescomplexasforam
encapsuladaspeloCocos2D.
Nesse capítulo, fomos um pouco mais a fundo em questões como telas (
CCScene),camadas( CCLayer),menus( CCMenu)ebotões( CCMenuItem).Uti-
lizamostambémumimportanteelementodoCocos2D,o CCDirector.
Aseguir,faremosatransi çãoparaateladojogoeteremosnossosprimeiros
elementosdogame.
75


## Página 87

Capítulo5
Teladojogoeobjetosinimigos
Horadeadicionarperigoaonossogame! Nessecapítuloiremosentrarnatelado
jogodefato,ondetodaaa çãoocorrerá.Essaseráaprincipalpartedojogoeporisso
trataremosemalgunscapítulos.
Parainiciar,passaremospelatransi çãodateladeaberturaparaateladejogo.
Alémdisso,colocaremososinimigosnatela.AlgunsconceitosimportantesdoCo-
cos2Dserãoutilizadosnessecapítulo,cujoobjetivoéterateladogamerodando,
comalgunsinimigossurgindo.
Utilizaremosmuitodoquejáfoivistoatéaqui,como CCLayerspararepresen-
tarcamadasdeumatela, CCSpritesparacontrolarobjetose CCSceneparacriar
ateladojogo.Alémdissoo CCDirectorseráutilizadonovamente.
Nofimdessecapítuloteremosatransi çãoentreteladeaberturaeteladogame,
alémdosobjetosinimigosaparecendonatela.


## Página 88

5.1. GameScene CasadoCódigo
Figura5.1:Meteorosinimigos.
5.1 G ame Scene
Precisamosdeumatelaparaojogo,paraconteroselementosprincipaisdeitera ção
dogamecomoplayer,inimigosecontroles.Assimcomoanteriormente,criaremos
umatelaherdandodaclasse CCLayerdoCocos2D,paraquepossamosterdiversas
camadasatuantes,comobotões,inimigos,player,scoreetc.
Tambémcomoanteriormente,adefini çãodeumatelaécriadaatravésdeum
CCScene,quesaberálidarcomascamadasdanossaclasse.
78


## Página 89

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
O Maestro
Idealmente,essaclassenãodevetermuitasresponsabilidades,massimfunci-
onarcomoumorquestradordetodososelementos,ouseja,ummaestroemuma
orquestra,quedirigeecomandaoquetodososoutroselementosfazemecomoeles
interagementresi.
Elaseráaclassequeinicializaobjetosnojogo,quecolocaobjetosnatela,porémo
comportamentodecadaumdelesserárepresentadoindividualmenteemcadaclasse
correspondente.
Algumasdasresponsabilidadesda GameScene,aclassemaestrodojogo,devem
ser:
• Iniciarateladogameeorganizarascamadas
• Adicionarobjetoscomoplayer,inimigosebotõesàessascamadas
• Inicializarcadaumdessesobjetos
• Checarcolisõesentreobjetos
Aclasse GameScenetemmuitaresponsabilidade,porémnãodetémregrase
lógicasdecadaelemento. Outrafun çãoimportantedessaclasseéaplicarumdos
conceitosvistosanteriormente,do game loop.
Vamosentãocriaraclasse GameScenejácolocandoumbackgroundcomofi-
zemosanteriormentenateladeabertura.O header GameScene.hficaráassim:
@interface GameScene : CCLayer
+ (CCScene *)scene;
@end
Eo implementation GameScene.m
# import "GameScene.h"
@implementation GameScene
+ (CCScene *)scene
{
// 'scene' is an autorelease object.
79


## Página 90

5.2. Transiçãodetelas CasadoCódigo
CCScene *scene = [CCScene node];
// 'layer' is an autorelease object.
GameScene *layer = [GameScene node];
// add layer as a child to scene
[scene addChild:layer];
// return the scene
return scene;
}
- (id)init
{
self = [super init];
if (self) {
// Imagem de Background
CCSprite *background = [CCSprite spriteWithFile:kBACKGROUND];
background.position =
ccp(SCREEN_WIDTH() / 2.0f, SCREEN_HEIGHT() / 2.0f);
[self addChild:background];
}
return self;
}
@end
5.2 T ransição de telas
Paraqueojogocomece,precisamosfazerolinkentreateladeaberturaeatelado
game!
Aquiutilizaremoso CCDirectorquesabemanteruma CCSceneativaporvez.
Alémdetrocardeumatelaparaoutra,oCocos2Dnospermiteescolhereconfigurar
detalhesdessatransi ção.
Utilizaremosométodo replaceScene:quefaráumatransi çãocomotempo
depausaentreumatelaeoutro,gerandoumefeitosuave.
Paraisso,naclasse TitleScreen,mudamoso playGame:paraquebotãode
playcomeceojogo.Importea GameScenena TitleScreen.h
# import "GameScene.h"
80


## Página 91

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
Emudeométodo playGame::
//...
- (void)playGame:(id)sender
{
NSLog(@"Botão selecionado: Play");
[[CCDirector sharedDirector]
replaceScene:[CCTransitionFade transitionWithDuration:1.0
scene:[GameScene scene]]];
}
Rodeojogoecliquenobotão play.Oqueacontece?Porenquanto,sótemosa
telade background!
5.3 E ngines
Temosaclassequeorquestraráosobjetosdogameecriaremosagoraclassesres-
ponsáveisporgerenciaroutroselementos.Oprimeiroelementoqueteremosserão
osinimigos.Nossosinimigosserãometeorosquecairãoeprecisarãoserdestruídos
peloplayer.
Criaremos uma nova camada, um novolayerpara representar esses inimi-
gos. Comoutilizadoanteriormente,camadassãorepresentadasporheran çasao
CCLayerdoCocos2D.
Engine de objetos inimigos
Nossacamadadeobjetosinimigos,osmeteoros,seráresponsávelporcriarini-
migoseenviaràteladojogo.Essa enginedemeteorosnãoéresponsávelpelomovi-
mentodometeoroemsi,massimdecontrolaraapari çãodelesnatelaefazerolink
entreobjeto MeteoroeteladoGame.
precisaremosmanterolinkentreatelaprincipaldogameea enginedeinimigos.
Essaéumapartecomplexadodesenvolvimentodegames.Nãoésimplescoordenar
objetoscomciclosdevidadiferentesquerodampelaaplica ção.Oquefaremosaqui
éutilizaroDesignPatternde delegateparaauxiliarnacomunica çãoentreosobjetos.
Delegatessãomuitoutilizadosemgameseaplica çõesiOS.Vocêjádeveter
vistoesteconceitoemdiversasoutrasclassesdoiOS,comoa UITableViewe
UIScrollViewporexemplo.
A enginedeinimigossabecomoequandocriarosinimigos. Masapenasisto.
81


## Página 92

5.3. Engines CasadoCódigo
Nossatelaprincipaléquesabeemqualcamadaincluiroinimigo,alémdeconhecer
todososdemaisobjetos(players,tirosetc)parapoderchecaracolisãoentreeles.
Emnossogame,atelaprincipaldojogoseráo delegateda enginedeinimigos.
Ouseja,atelaprincipaldojogoseráresponsávelpor“escutar”etratarasinstruções
da enginedeinimigo.Pensedaseguintemaneira:a enginedeinimigosirádizer“Ei
delegate!Euquerocriaroinimigo!”,eatelaprincipaliráresponder“OK!Voucriar
oinimigo.Deixecomigoquedaquiprafrenteeucuidodele!”.
Éimportantequeuma Enginesaibaquandoéomomentodecolocarumnovo
elementonojogo. Muitasvezes,principalmenteparaobjetosinimigos,utilizamos
númerosrandômicosparadefinirahoradecolocarumnovoinimigonatela.
Essaideiafoimuitoutilizadaporjogosemqueonívelmaisdifícileraapenasuma
equaçãonaqualonúmerorandômicogeradosatisfaziaumacondi çãodeentradaem
um if.Nocódigodanossa engineabaixo,faremosexatamenteisso.
Valecitarquea engineéocódigoresponsávelpormanteroloopdeobjetos,e
comoCocos2D,utilizamosmétodosdeagendamentoparaisso.Ouseja,criaremos
um scheduleparaquea engineanalisesedeveounãoatualizareincluirumnovo
objetoinimigonatela.
Abaixo,ocódigodaprimeira Enginedogame,aclasse MeteorsEngine.No
header MeteorsEngine.hiremosdefinirum protocolo,queéométodoqueo de-
legate(a GameScene)teráqueimplementarpararesponderàsrequisi çõesda engine
deinimigos:
@protocol MeteorsEngineDelegate;
@interface MeteorsEngine : CCLayer
@property (nonatomic, assign) id<MeteorsEngineDelegate>delegate;
+ (MeteorsEngine *)meteorEngine;
@end
@protocol MeteorsEngineDelegate <NSObject>
- (void)meteorsEngineDidCreateMeteor:(CCNode *)meteor;
@end
No implementation MeteorsEngine.m,vamosescreveralógicadecria çãode
meteoros:
82


## Página 93

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
# import "MeteorsEngine.h"
@implementation MeteorsEngine
+ (MeteorsEngine *)meteorEngine
{
return [[[MeteorsEngine alloc] init] autorelease];
}
- (id)init
{
self = [super init];
if (self) {
[self schedule:@selector(meteorsEngine:) interval:(1.0f/10.0f)];
}
return self;
}
- (void)meteorsEngine:(float)dt
{
// sorte: 1 em 30 gera um novo meteoro!
if(arc4random_uniform(30) == 0) {
if ([self.delegate respondsToSelector:
@selector(meteorsEngineDidCreateMeteor:)]){
// Pede para o delegate criar o meteoro
// (por enquanto, não estamos informando qual o meteoro)
[self.delegate meteorsEngineDidCreateMeteor:nil];
}
}
}
@end
Para fechar olinkentre ambas as camadas, implementaremos o protocolo
MeteorsEngineDelegatenateladojogo,oqueobrigaráelaaterummétodo
parareceberosobjetoscriadosporessa Engineecolocá-losnatela.
Primeiramente,vamosinformarna GameScene.hqueeladeveráimplementar
oprotocolo:
# import "MeteorsEngine.h"
83


## Página 94

5.3. Engines CasadoCódigo
@interface GameScene : CCLayer <MeteorsEngineDelegate>
+ (CCScene *)scene;
@end
Ena GameScene.mcrieométodoqueseráresponsávelpelosmeteorosque
criaremosemseguida.
- (void)meteorsEngineDidCreateMeteor:(CCNode *)meteor
{
// Aqui incluiremos o meteoro na tela
}
Mantendo as referências
Umoutropontoimportanteparaocontroledojogoetodaaorquestra çãoéman-
tertodososobjetoscriadosdeumaformafácilparaquepossamseranalisadosde-
pois. Umexemplonessecasoéacompara çãocomotirooucomopróprioplayer
paradetectarcolisões,queserãotratadosmaisàfrente.
Vamosguardarareferênciadecadameteorocriadoemumapropriedade&&NS-
MutableArray na classe GameScene , e também uma propriedade com
referência à engine de inimigos. Declare estas propriedades
na GameScene.h
# import "MeteorsEngine.h"
@interface GameScene : CCLayer <MeteorsEngineDelegate>
+ (CCScene *)scene;
// Engines
@property (nonatomic, retain) MeteorsEngine *meteorsEngine;
// Arrays
@property (nonatomic, retain) NSMutableArray *meteorsArray;
@end
OCocos2Dnãosuporta ARC(Automatic Reference Counting),porisso,todas
aspropriedadesquecriarmoscomo retaindeverãoserretiradasdamemóriano
método deallocdenossasclasses.
84


## Página 95

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
Crieométodo deallocnofinalda GameScene.meinclua:
- (void)dealloc
{
[_meteorsEngine release];
[_meteorsArray release];
[super dealloc];
}
Lembre-sedeincluiro deallocemtodasasdemaisclassesquecriarmoscom
propriedadesdeclaradascom retain.
5.4 M eteor
Chegamosaoobjetoinimigopropriamentedito. Asprincipaisresponsabilidades
desseobjetosão:
• Carregarimagem(CCSprite)
• Posicionarelementonatela
• Guardaraposiçãodoobjetoparaqueomesmopossasermovimentadocom
otempo
Esseéoprimeiroobjetodejogorealmentequecriaremos.Atéomomento,cri-
amostelaspreenchendo-ascomelementos,botõesdemenueclassesde enginepara
darabaseaesseselementosprincipaisdojogo.
Aprimeiracoisaasefazeréadicionaro assetdometeorona Assets.h.
@interface Assets : NSObject
# define kMETEOR @"meteor.png"
@end
Vamoscriaraclasse Meteor.Inicialmente,cadameteoronascenotopodatela
(éovalorde SCREEN_HEIGHT()),enumaposi ção xrandômica.Declareno header
Meteor.hduaspropriedadesparaguardaraposi ção xe ydometeoro,ométodo
construtor meteorWithImage:eométodo start,queseráimplementadopos-
teriormente:
85


## Página 96

5.4. Meteor CasadoCódigo
# import "CCSprite.h"
@interface Meteor : CCSprite
@property (nonatomic, assign) float positionX;
@property (nonatomic, assign) float positionY;
+ (Meteor *)meteorWithImage:(NSString *)image;
- (void)start;
@end
No implementation Meteor.h,nossoconstrutorirásortearumaposi çãoinicial
dometeoro:
# import "Meteor.h"
@implementation Meteor
+ (Meteor *)meteorWithImage:(NSString *)image
{
Meteor *meteor = [Meteor spriteWithFile:image];
meteor.positionX = arc4random_uniform(SCREEN_WIDTH());
meteor.positionY = SCREEN_HEIGHT();
meteor.position = ccp(meteor.positionX, meteor.positionY);
return meteor;
}
@end
Reparequeoobjetometeoropermanecevivonamemóriaporumbomtempo.
Eleécriadoe,acada frame,renderizadoemumaposi çãodiferente,dandoaimpres-
sãodemovimento.
Aquimaisumavezo frameworknosajuda.Paraquecada framesejarenderizado
duranteojogo,eaposi çãodoobjetomudecomopassardotempo,oCocos2D
nospermiteescolherummétodoqueseráinvocadodetempoemtempo.Issoserá
definidono start,fazendo scheduleUpdate,queinvocaráométodo update.
86


## Página 97

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
//...
- (void)start
{
[self scheduleUpdate];
}
- (void)update:(float)dt
{
self.positionY -= 1;
self.position = ccp(self.positionX, self.positionY);
}
Variável dt dos updates
OCocos2Dvai tentarinvocaroseumétodo updatedexemxmilis-
segundos,issoé,emcadaframe.Mas,porumasériedemotivos,opro-
cessadorpodeestarocupadocomoutrascoisas,fazendocomqueessa
chamadaagendadanãoocorraquandovocêqueria. Elepodedemorar
mais.Nessecaso,vaidarumaimpressãoqueseujogoestálento,jáque
atelaserárenderizadacomosesótivessepassadootempodeum frame,
masnaverdadepodeterpassadoalgunssegundos.
Numjogoprofissional,vocêdeveguardaressainforma çãoparadeci-
dircorretamentequantos pixelscadaobjetodevemudar.Nonossocaso,
seo dtformaiorqueode1 frame,deveríamosdescerometeoromais
que1pixel,fazendoaregrade3.
5.5 T ela do game
Agora que temos nossa classe Meteor, vamos alterar o protocolo da
MeteorsEngine.hparaquepasseumobjetometeorocomoparâmetro:
# import "Meteor.h"
//...
@protocol MeteorsEngineDelegate <NSObject>
- (void)meteorsEngineDidCreateMeteor:(Meteor *)meteor;
@end
Na MeteorsEngine.mpassaremosumnovometeorocomoparâmetroparao
delegate:
87


## Página 98

5.5. Teladogame CasadoCódigo
- (void)meteorsEngine:(float)dt
{
// sorte: 1 em 30 gera um novo meteoro!
if(arc4random_uniform(30) == 0) {
if ([self.delegate respondsToSelector:
@selector(meteorsEngineDidCreateMeteor:)]){
// Pede para o delegate criar o meteoro
[self.delegate meteorsEngineDidCreateMeteor:
[Meteor meteorWithImage:kMETEOR]];
}
}
}
Parafecharecriaro linkentreaclassedateladojogo,coma enginedemeteoros
ecomosobjetosmeteoroscriados,modificaremosaclasse GameScene.
Primeiramente,vamoscriarummétodoqueconteráainicializa çãodosobjetos
dejogo.Crieométodo addGameObjects:
- (void)addGameObjects
{
// Inicializa os Arrays
self.meteorsArray = [NSMutableArray array];
// Inicializa a Engine de Meteoros
self.meteorsEngine = [MeteorsEngine meteorEngine];
}
Noconstrutor,criaremosum layerespecialmenteparaosmeteoroseadiciona-
remosateladojogovia addChild. Declareapropriedade meteorsLayerna
GameScene.h:
//...
// Layers
@property (nonatomic, retain) CCLayer *meteorsLayer;
No initda GameScene.mcriaremosa layerdemeteoroseinvocaremoso
addGameObjetos.Ficaráassim:
- (id)init
{
self = [super init];
88


## Página 99

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
if (self) {
// Imagem de Background
CCSprite *background = [CCSprite spriteWithFile:kBACKGROUND];
background.position =
ccp(SCREEN_WIDTH() / 2.0f, SCREEN_HEIGHT() / 2.0f);
[self addChild:background];
// CCLayer para os Meteoros
self.meteorsLayer = [CCLayer node];
[self addChild:self.meteorsLayer];
[self addGameObjects];
}
return self;
}
Eagorapodemosalterarométodo meteorsEngineDidCreateMeteor:para
incluirometeoronatelaeiniciá-lo:
- (void)meteorsEngineDidCreateMeteor:(Meteor *)meteor
{
// A Engine de Meteoros indicou que um novo Meteoro foi criado
[self.meteorsLayer addChild:meteor];
[meteor start];
[self.meteorsArray addObject:meteor];
}
Ummétodoimportantequeutilizaremosaquiéo onEnter.Eleéinvocadopelo
Cocos2Dassimqueateladogameestáprontaparaorquestrarosobjetosdojogo.
Eleseráaportadeentradadojogo. Porenquanto,simplesmenteadicionaremoso
meteorsEngineeindicaremoso delegatecomo self,parasermosavisados
quandonovosmeteorosforemcriados:
//...
- (void)onEnter
{
[super onEnter];
[self startGame];
}
- (void)startGame
89


## Página 100

5.6. Conclusão CasadoCódigo
{
[self startEngines];
}
- (void)startEngines
{
[self addChild:self.meteorsEngine];
self.meteorsEngine.delegate = self;
}
5.6 C onclusão
Temosagoraateladeaberturaeateladejogo(ondeo game loopéexecutado)em
funcionamento. Nossogame loopinicializaosinimigos. Precisamosdeumplayer
parajogarcontraeles,éoqueveremosaseguir!
90


## Página 101

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
Figura5.2:Meteorosinimigos.
91


## Página 103

Capítulo6
CriandooPlayer
Teladojogopreparadaeinimigosaparecendo!Cenárioperfeitoparainiciarmoso
desenvolvimentodoplayer!Essaéumapartebeminteressantenodesenvolvimento
dejogos,poisprogramaremosoobjetoqueserácontroladopelos inputsdousuário.
Paraisso,utilizaremosamaioriadoselementosdo frameworkCocos2Dquevi-
mosatéagoraparatrabalharcomoplayer.Utilizaremoscamadas,spriteseoscon-
ceitosvistosanteriormente.
Nossateladejogoprecisarádemaisumacamada,utilizaremos Spritespara
oPlayeredetectaremos inputsdousuárioparamovê-lo.
Resumidamente,nessecapítulofaremos:
• Colocaroplayernatela
• Movimentaroplayer
• Eatirar!


## Página 104

6.1. DesenhandooPlayer CasadoCódigo
Daremosumpassoimportantenaconstru çãodojogonessecapítulo,oobjetivo
finaléteracenaaseguir,aindasemdetectarcolisões.
Figura6.1:14bisatirandocontraosmeteoros.
6.1 D esenhando o Player
Iniciaremospelaimagem,adicionandoafiguradoplayerno Assets.h.
@interface Assets : NSObject
# define kNAVE @"nave.png"
@end
94


## Página 105

CasadoCódigo Capítulo6. CriandooPlayer
Criaremosoobjetoprincipale,comoanteriormente,controlamosfiguraseima-
gensherdandodo CCSpritedoCocos2D.
UtilizaremosométodoqueretornaalarguradatelaparacentralizaroPlayer.
Precisamosdevariáveisqueguardemessasposi çõespoisprecisaremosalterá-las
maisàfrente.
Comojáutilizadopelasoutrasclasses,manteremosolinkentreteladeabertura
eplayerutilizandoumdelegate.
Na Player.hiremosdeclararnossaspropriedadesdeposi çãodoplayer,eo
construtor.
@protocol PlayerDelegate;
@interface Player : CCSprite
@property (nonatomic, assign) id<PlayerDelegate>delegate;
@property (nonatomic, assign) float positionX;
@property (nonatomic, assign) float positionY;
+ (Player *)player;
@end
@protocol PlayerDelegate <NSObject>
// Vamos criar os métodos de delegate mais pra frente
@end
A Player.mseráiniciadadaseguintemaneira:
# import "Player.h"
@implementation Player
+ (Player *)player
{
Player *player = [Player spriteWithFile:kNAVE];
// Posiciona o Player recém criado
player.positionX = SCREEN_WIDTH() / 2.0f;
player.positionY = 120.0f;
player.position = ccp(player.positionX, player.positionY);
95


## Página 106

6.1. DesenhandooPlayer CasadoCódigo
return player;
}
OobjetoPlayerjáestáprontoparaserinicializado,masaindanãoexisteuma
camadanateladojogoresponsávelpormostrá-lo. Paraqueoplayerapare çana
teladojogo,temosqueadicionarmaisumacamada. Essacamadateráonomede
playerLayer.
Na GameScene.hvamosdeclararaspropriedadesda layeredoplayer,alémde
informarqueelaimplementaráoprotocolo PlayerDelegate:
# import "Player.h"
//...
@interface GameScene : CCLayer <MeteorsEngineDelegate, PlayerDelegate>
//...
@property (nonatomic, retain) CCLayer *playerLayer;
@property (nonatomic, retain) Player *player;
Na GameScene.ménecessárioadicionaravariáveldelayereiniciá-lanocons-
trutor.Apósisso,adicioneacamadacriadaatravésdométodo addGameObjects.
- (id)init
{
self = [super init];
if (self) {
//...
// CCLayer para o Jogador
self.playerLayer = [CCLayer node];
[self addChild:self.playerLayer];
[self addGameObjects];
}
return self;
}
- (void)addGameObjects
{
// Inicializa os Arrays
self.meteorsArray = [NSMutableArray array];
96


## Página 107

CasadoCódigo Capítulo6. CriandooPlayer
// Inicializa a Engine de Meteoros
self.meteorsEngine = [MeteorsEngine meteorEngine];
// Cria o Player
self.player = [Player player];
self.player.delegate = self;
[self.playerLayer addChild:self.player];
}
Figura6.2:14bisprontoparaa ção.
97


## Página 108

6.2. Botõesdecontrole CasadoCódigo
6.2 B otões de controle
Játemosoplayeraparecendonatela.Alémdisso,elejáestáemumacamadadatela
dogame,oquefazcomquesejarenderizadoduranteojogo.
Vamosagoraadicionaroutroselementosàtela,paraqueoplayerpossaserco-
mandadopelos inputsdousuário. Paraisso,precisaremosdenovasimagenspara
essescontroles.
Iniciaremosadicionando3imagens,duasparamovimentaroplayerentredi-
reitaeesquerdaeoutraqueseráobotãodeatirar.Essasimagensserãoincluídasno
arquivo Assets.h.
@interface Assets : NSObject
# define kLEFTCONTROL @"left.png"
# define kRIGHTCONTROL @"right.png"
# define kSHOOTBUTTON @"shootButton.png"
@end
Paraosbotões,poderíamosutilizarnovamenteaclasse CCMenuItemSprite.
Entretanto,osobjetosdotipo CCMenuItemSpritesãoativadossomentequando
ousuárioretiraodedodobotão. Estecomportamentoéaceitávelparabotõesde
menu,porém,parajogosoidealéqueobotãoexecuteaa çãonomomentoqueo
usuáriotocá-lo,enãoapósretirarodedo.
Paraisto,criaremosaclasse CCMenuItemGameButtonqueirásobrescrever
algunsmétodospadrõesda CCMenuItemSprite,afimdequeasa çõesdosbotões
sejamexecutadaslogoquandoobotãofortocado.
Crieaclasse CCMenuItemGameButton,subclasseda CCMenuItemSprite.
Noarquivoheader CCMenuItemGameButton.hnãoénecessárionenhumaal-
teração. Vamos apenas alterar os métodos de ativação e seleção do botão na
CCMenuItemGameButton.m:
@implementation CCMenuItemGameButton
- (void)selected
{
// Quando está "selected", aciona o "activate" para disparar o botão
// antes de o jogador tirar o dedo da tela
[super activate];
}
98


## Página 109

CasadoCódigo Capítulo6. CriandooPlayer
- (void)activate
{
// Não chama mais o super "activate" aqui, já que este foi
// acionado no método "selected"
// [super activate];
}
@end
Pronto,temosnossobotãocustomizadocriado.Agoravamosincluirosbotões
natelaalterandoaclasse GameScene.Vamosimportaraclassedebotõesedefinir
suacamada,adeclarandona GameScene.h:
# import "CCMenuItemGameButton.h"
//...
@property (nonatomic, retain) CCLayer *gameButtonsLayer;
No arquivo de implementação GameScene.m, vamos instanciar a camada
dos botões e criar o menu. Perceba que os botões serão criados da mesma
forma que fizemos naTitleScreen, mas desta vez utilizaremos nossa classe
CCMenuItemGameButton:
- (id)init
{
self = [super init];
if (self) {
//...
// CCLayer para os Botões
self.gameButtonsLayer = [CCLayer node];
[self addChild:self.gameButtonsLayer];
// Cria os botões
CCMenuItemGameButton *leftControl = [CCMenuItemGameButton
itemWithNormalSprite:[CCSprite spriteWithFile:kLEFTCONTROL]
selectedSprite:[CCSprite spriteWithFile:kLEFTCONTROL]
target:self
selector:@selector(moveLeft:)];
CCMenuItemGameButton *rightControl = [CCMenuItemGameButton
itemWithNormalSprite:[CCSprite spriteWithFile:kRIGHTCONTROL]
selectedSprite:[CCSprite spriteWithFile:kRIGHTCONTROL]
target:self
99


## Página 110

6.2. Botõesdecontrole CasadoCódigo
selector:@selector(moveRight:)];
CCMenuItemGameButton *shootButton = [CCMenuItemGameButton
itemWithNormalSprite:[CCSprite spriteWithFile:kSHOOTBUTTON]
selectedSprite:[CCSprite spriteWithFile:kSHOOTBUTTON]
target:self
selector:@selector(shoot:)];
// Define as posições dos botões
leftControl.position = ccp(-110.0f,
(SCREEN_HEIGHT() / -2.0f) + 50.0f);
rightControl.position = ccp(-50.0f,
(SCREEN_HEIGHT() / -2.0f) + 50.0f);
shootButton.position = ccp((SCREEN_WIDTH() / 2.0f) - 50.0f,
(SCREEN_HEIGHT() / -2.0f) + 50.0f);
// Cria o menu que terá os botões
CCMenu *menu = [CCMenu menuWithItems:leftControl,
rightControl,
shootButton,
nil];
[self.gameButtonsLayer addChild:menu];
[self addGameObjects];
}
return self;
}
Porfim,énecessáriocriarosmétodosquereceberãoos inputsdosbotões:
- (void)moveLeft:(id)sender
{
NSLog(@"Botão selecionado: Esquerda");
}
- (void)moveRight:(id)sender
{
NSLog(@"Botão selecionado: Direita");
}
- (void)shoot:(id)sender
{
100


## Página 111

CasadoCódigo Capítulo6. CriandooPlayer
NSLog(@"Botão selecionado: Atirar");
}
Rodeojogoeaperteosbotões. Vejaqueelesrespondemlogoquandovocêos
toca,enãoquandoretiraodedodatela!
Figura6.3:Controlesdedire çãoetiro.
Imagensposicionadasepreparadas.Horadecome çaraa ção!
6.3 A tirando
Falaremosagoradeumapartedojogoquepodeparecersimplesaprincípio,mas
temimpactoemmuitasoutraspartesparaquefuncione: otiro! Paraqueanave
101


## Página 112

6.3. Atirando CasadoCódigo
atire,precisaremosdeumasériedecoisas,portanto,vamosprimeirolistaroque
seránecessárioparaorganizaropensamentoantesdeirparaocódigo.
• Umnovoasset,ouseja,imagemdotiro
• Umaclassequerepresenteotirocomoum CCSprite
• Definiroposicionamentodotironatela
• Umaengineresponsávelporcriarumtiro
• Umacamadanateladojogoparaostiros
• Associarotiroeoplayer,paraqueotirosaiadoplayer
Hámuitacoisaparaqueotirodefatoaconte ça,porém,selistarmoscadauma
dessasdependênciaspodemossimplificarodesenvolvimento. Iniciaremosadicio-
nandoafiguradotironaclasse Assets.h.
@interface Assets : NSObject
# define kSHOOTBUTTON @"shootButton.png"
@end
Podemosiniciaraprograma çãodotiro.Antesdepensaremfazeranaveatirar
oualgoassim,vamostentarpensarem“oqueéotiro?”.Otiroéum sprite,ouseja,
umaimagem,queandapelateladebaixoparacima. Assim,umavezqueumtiro
aparecenatela,precisamosmovimentá-loparacimacomopassardotempo.
Parageraressasensa çãodemovimentoecontrolaresses updatesdoposiciona-
mentodotironoeixovertical,criaremosummétodocomonome update:.Esse
métodoseráexecutadopeloCocos2Dacadaitera ção. Oframeworkmandacomo
parâmetroumtempodeexecu ção,paraquepossaseranalisadosealgodeveounão
serexecutadodesdeaúltimavezqueeleinvocouessemétodo.Nonossocaso,esse
parâmetronãoseráutilizado,poisalógicadotiroépelotoquenobotãoenãopor
umaregradetempo.
Aclassedetiroprecisamanterolinkcomateladejogo,entãoutilizaremoso
delegate.Criaremostambémummétodochamado start,queseráutilizadopara
indicarqueotiroestáfuncionando.
Declareaspropriedadesemétodosna Shoot.h:
102


## Página 113

CasadoCódigo Capítulo6. CriandooPlayer
@interface Shoot : CCSprite
@property (nonatomic, assign) float positionX;
@property (nonatomic, assign) float positionY;
+ (Shoot *)shootWithPositionX:(float)positionX
andPositionY:(float)positionY;
- (void)start;
@end
Vamosimplementarosmétodosna Shoot.m:
@implementation Shoot
+ (Shoot *)shootWithPositionX:(float)positionX
andPositionY:(float)positionY
{
Shoot *shoot = [Shoot spriteWithFile:kSHOOT];
// Posiciona o Tiro recém criado no ponto indicado
shoot.positionX = positionX;
shoot.positionY = positionY;
shoot.position = ccp(shoot.positionX, shoot.positionY);
return shoot;
}
- (void)start
{
// Inicia a Animação / Movimentação do Tiro
[self scheduleUpdate];
}
- (void)update:(float)dt
{
// Move o Tiro para cima
self.positionY += 2;
self.position = ccp(self.positionX, self.positionY);
}
103


## Página 114

6.3. Atirando CasadoCódigo
@end
Tiro e tela de jogo
Atéaqui,aclassedetirofoidefinida.Agoravamosàteladojogoparaadicionar
essenovoelemento.Duascoisassãonecessáriasnessemomento.Aprimeiraéaca-
madadoCocos2Dparaqueostirosapare çam.Asegundaéum NSMutableArray
queguardaráostirosparaquepossamosdetectaracolisãocomosmeteoros.Altere
a GameScene.h:
# import "Shoot.h"
//...
@property (nonatomic, retain) CCLayer *shootsLayer;
@property (nonatomic, retain) NSMutableArray *shootsArray;
Alémdecriaraspropriedade,énecessárioinicializá-las.Noconstrutorcriare-
mosacamada.
- (id)init
{
self = [super init];
if (self) {
//...
// CCLayer para os Tiros
self.shootsLayer = [CCLayer node];
[self addChild:self.shootsLayer];
}
return self;
}
Enométodo addGameObjectscriaremoso array.
- (void)addGameObjects
{
//...
self.shootsArray = [NSMutableArray array];
//...
}
104


## Página 115

CasadoCódigo Capítulo6. CriandooPlayer
Atirando!
Játemosaclassedotiroetambémaprepara çãonateladejogoparao linkentre
essesdoisobjetos. Oquefizemosatéaquifoiprepararaestruturaparaqueotiro
aconteça.Vamosnosconcentraragoranarela çãoentreotiroeoPlayer.
Nessemomento,iremosdefinirométodoqueoplayernotificaráo delegatede
queeleestáatirando.Incluaométodono PlayerDelegateda Player.h:
# import "Shoot.h"
//...
@protocol PlayerDelegate <NSObject>
- (void)playerDidCreateShoot:(Shoot *)shoot;
@end
Nesse momento, implementaremos a interface PlayerDelegate
na GameScene. Dessa forma, a tela de jogo saberá o que deve fazer
quando for requisitada para atirar. A interface obriga a criação do método
playerDidCreateShoot:.Nele,umnovotiro,queérecebidocomoparâmetro,
éadicionadoàcamadaeao arraydetiros.Alémdisso,chamaométodo startda
classe Shoot,permitindoqueelacontroleoquefornecessárioládentro.
Primeiramente, implemente o método playerDidCreateShoot: na
GameScene.m
- (void)playerDidCreateShoot:(Shoot *)shoot
{
// O Player indicou que um novo Tiro foi criado
[self.shootsLayer addChild:shoot];
[shoot start];
[self.shootsArray addObject:shoot];
}
Criaremosnaclasse Playerummétodochamado shootparadispararosti-
ros.Precisamosdissoporumfatomuitoimportante,queéoposicionamentoinicial
dotiro. Lembre-sequeotirodevesairdanave,portantooPlayereseuposicio-
namentosãomuitoimportantes. Ométodo shootconterátodasasvariáveisde
posicionamentodanavenahoradotiro.
Declareométodona Player.h:
- (void)shoot;
Implementeocódigodetirona Player.m:
105


## Página 116

6.3. Atirando CasadoCódigo
- (void)shoot
{
// Aqui será disparado o tiro!
}
Apertando o botão!
A GameScene.méquemtemomenudebotõeserecebeo inputdousuário,ou
seja,omomentoemqueobotãoépressionado,econsequentementeotirodisparado.
Vamosalterarométodo shoot:,disparadopelobotãodetiro,parachamaro
métododeatirardoPlayer:
- (void)shoot:(id)sender
{
NSLog(@"Botão selecionado: Atirar");
[self.player shoot];
}
Player atirando
Tudoprontoparaatirarapartirdobotãodetiropressionado!Temosaclassede
tirodefinida,obotãodetiroprogramadoeateladejogocomacamadaemétodos
necessáriosprontos.Precisamosquealguémdêocomandodeatirarenadamelhor
queopróprioPlayerparafazerisso!Vamosalterarométodo shootda Player.m
paraquecaptureoposicionamentodanaveechameseu delegateparacria çãodotiro.
Bang!
- (void)shoot
{
// Atira
if ([self.delegate respondsToSelector:
@selector(playerDidCreateShoot:)]) {
[self.delegate playerDidCreateShoot:
[Shoot shootWithPositionX:self.positionX
andPositionY:self.positionY]];
}
}
106


## Página 117

CasadoCódigo Capítulo6. CriandooPlayer
Figura6.4:Playeratirando.
6.4 M ovendo o player
Vamosfecharessecapítulocomumadaspartesmaisimportantesdojogo. Após
atirar,moveremosoPlayerparaesquerdaedireita.Utilizaremosamesmaestratégia
deatirar,masagoraascoisasserãomaissimples.
Parainiciar,o Playerdevesabersemover.Movimentaroplayeréfazercom
quesuaposi çãoXsejaatualizadaquandoumeventofordetectado.
Naclasse Playeradicionaremosdoisnovosmétodos,quequandochamados,
mudamaposi çãohorizontaldanave.Declareosmétodosna Player.h.
- (void)moveLeft;
107


## Página 118

6.4. Movendooplayer CasadoCódigo
- (void)moveRight;
Vamosimplementarosmétodosdemovimenta çãona Player.m:
- (void)moveLeft
{
// Move o Player para a Esquerda
if (self.positionX > 30.0f) {
self.positionX -= 10.0f;
}
self.position = ccp(self.positionX, self.positionY);
}
- (void)moveRight
{
// Move o Player para a Direita
if (self.positionX < SCREEN_WIDTH() - 30.0f) {
self.positionX += 10.0f;
}
self.position = ccp(self.positionX, self.positionY);
}
Na GameScene.malteraremososmétodosparaqueessasa çõessejamchamadas
pelosbotões.
- (void)moveLeft:(id)sender
{
NSLog(@"Botão selecionado: Esquerda");
[self.player moveLeft];
}
- (void)moveRight:(id)sender
{
NSLog(@"Botão selecionado: Direita");
[self.player moveRight];
}
Aorodaroprojeto,devemosteranavesemovimentandoapartirdostoquesno
comandodecontroledanave. Alémdissoelajáatiradeacordocomaposi çãodo
Player.
108


## Página 119

CasadoCódigo Capítulo6. CriandooPlayer
6.5 C onclusão
Esseéumcapítulomuitoimportanteparaodesenvolvimentodojogo.Alémdeusar
diversoselementosdo frameworkCocos2D,comocamadas,spriteseagendamento
(update),diversosconceitosdejogosforamusados,alémdepráticascomo delegates
e engines.
Ojogodeveestarcomonafiguraabaixo.
Figura6.5:14bisatirandocontraosmeteoros.
Éhoradeverificarascolisões!
109


## Página 121

Capítulo7
Detectandocolisões,pontuandoe
criandoefeitos
Colisõessãoocora çãodosgames.Sejaumsocodeumpersonagemnooutro,seja
opersonagemprincipalcapturandoalgumelemento,oucomonojogoqueestamos
programando,umtiroqueatingeummeteoro.
Detectarqueumelementoencostouemoutroéumassuntoquepodesermuito
complexo.Comomostradonocapítulodoprotótipoquedesenvolvemos,podemos
detectarcolisõesconsiderandofigurasgeométricasemvoltadoselementosparafa-
cilitar.
Nocapítuloatual,detectaremoscolisõesemduassitua ções.
• Quandoumtiroatingeummeteoro
• Quandoummeteoroatingeoavião(gameover)
Veremosaquimaisumavezqueutilizarum frameworkdedesenvolvimentode
jogoscomooCocos2Dajudamuitonessetrabalho.


## Página 122

7.1. Detectandocolisões CasadoCódigo
Umavezdetectadasascolisões,utilizaremososefeitosdoCocos2Dparagerar
umaanima çãoquandoadetec çãoocorrer. Emoutraparteimportantedessecapí-
tulo,falaremossobreaatualiza çãodoplacar.Essadeveserumapartetranquilapois
utilizaráconceitosjávistosanteriormente,como camadase sprites.
Essecapítulotraránovoscódigosemaisutiliza çãodo frameworkCocos2D,
sendoumcapítulochaveparaodesenvolvimentodojogo.
7 .1 D etectando colisões
Aprimeiracoisaqueprecisamosparaidentificaracolisãoentreobjetosnogame
édefinirumaestratégiaparaisso. Nessejogo,aestratégiaseráanalisarumgrupo
deobjetosemum array,comcadaobjetodeumoutrogrupo.Ouseja,dadosdois
arrays,verificarsealgumelementodeum arraysobrepõeoutro.
Na GameScene.hcriaremosum NSMutableArrayparaoplayerque,inici-
almente,teráumúnicojogador.
@property (nonatomic, retain) NSMutableArray *playersArray;
Eadicionaremosesseplayerno arraydeobjetosna GameScene.m. Maispra
frentevocêpoderáevoluirojogoecontrolarmaisdeumplayer.
- (void)addGameObjects
{
//...
// Insere o Player no array de Players
self.playersArray = [NSMutableArray array];
[self.playersArray addObject:self.player];
}
Definindo as bordas
Precisamosagoradeumaformadedefinirasbordasoulimitesdotiro,danave
edosmeteoros,paraquesejapossívelfazeradetec çãodacolisão.
Noprotótipo,utilizamosaestratégiadecírculos.Paraojogoatual,utilizaremos
umaestratégiadequadradosouretângulos.
ComoestamosutilizandooCocos2Deseus Spritespodemosmaisfacilmente
conseguiressasinforma ções.
Precisaremosdeummétododo Spritequedevolvaumretângulo,queconte-
nhaasbordasdoelemento.Paraisso,utilizaremosummétodoqueexistenospró-
112


## Página 123

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
prios Spriteschamado boundingBox.Essemétododevolveumtipo CGRect,que
representaoscontornosdafiguramapeadosemformaretangular.
Comessemétodo,sabemosascoordenadasdoposicionamentodoobjetoaser
analisado.
Checando a colisão
Umavezquejáconseguimososvaloresdeumelementodojogo,suasbordas
eposi çãonatela,podemosutilizaraestratégiaquefalamosnocome çodocapítulo
paraidentificarseumelementocolidecomoutroduranteojogo.
Criaremosummétodoimportanteparachecarascolisões,queprecisadealguns
parâmetrosparafuncionar. Osdoisprimeirossão arraysdeobjetosaseremveri-
ficados. Ouseja,sequeremoschecarseostirosestãocolidindocomosmeteoros,
passaremosessesdoisarrays. Outropontoimportanteépassarumareferênciada
teladejogo,nocasoa GameScene. Precisamosdissoparapoderexecutaralgum
métodocasoacolisãosejadetectada,porémcomodiversascolisõespodemserde-
tectas,comonavecomtirooutirocommeteoro,issoserádecididoemtempode
execução. Éexatamenteporissoqueprecisamos,porúltimo,deumparâmetroa
mais,querecebeonomedométodoaserexecutadocasoacolisãoaconte ça.
Oqueteremosentãoéumaverifica çãodecadaelementodoprimeiroarray,com
cadaelementodosegundoarray. Casoadetec çãoaconte ça,faremosumlogpor
enquanto,emostraremosquaiselementostiveramacolisão.
Na GameScene.mteremosocódigoaseguir.
- (BOOL)checkRadiusHitsOfArray:(NSArray *)array1
againstArray:(NSArray *)array2
withSender:(id)sender
andCallbackMethod:(SEL)callbackMethod
{
BOOL result = NO;
for (int i = 0; i < [array1 count]; i++) {
// Pega objeto do primeiro array
CCSprite *obj1 = [array1 objectAtIndex:i];
CGRect rect1 = obj1.boundingBox;
for (int j = 0; j < [array2 count]; j++) {
// Pega objeto do segundo array
CCSprite *obj2 = [array2 objectAtIndex:j];
113


## Página 124

7.1. Detectandocolisões CasadoCódigo
CGRect rect2 = obj2.boundingBox;
// Verifica colisão
if (CGRectIntersectsRect(rect1, rect2)) {
NSLog(@"Colisão Detectada: %@",
NSStringFromSelector(callbackMethod));
result = YES;
// Se encontrou uma colisão, sai dos 2 loops
i = [array1 count] + 1;
j = [array2 count] + 1;
}
}
}
return result;
}
Tendoométodoqueidentificaacolisãocomofizemos,podemosutilizá-lopara
averifica çãodedois arraysquaisquer.Faremosachamadaaeleparadetectarcoli-
sõesentretirosemeteoroseentremeteoroseanave.Essemétododeveserchamado
detemposemtempospeloCocos2D,portanto,utilizaremosmaisumavezoagen-
damentodo framework,passandoessemétodoparao schedule:.
Aindana GameScene.mfaremosessaschamadas.
- (void)checkHits:(float)dt
{
// Checa se houve colisão entre Meteoros e Tiros
[self checkRadiusHitsOfArray:self.meteorsArray
againstArray:self.shootsArray
withSender:self
andCallbackMethod:@selector(meteorHit:withShoot:)];
// Checa se houve colisão entre Jogador(es) e Meteoros
[self checkRadiusHitsOfArray:self.playersArray
againstArray:self.meteorsArray
withSender:self
andCallbackMethod:@selector(playerHit:withMeteor:)];
}
Comocitadoanteriormente,agendaremosométododechecagemdecolisões.
114


## Página 125

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
Paraisso,ométodo schedule:receberáométodocheckHits:comoparâmetro.
- (void)startGame
{
// Ao entrar na GameScene, inicia a checagem de colisões
// e inicia as Engines do jogo
[self schedule:@selector(checkHits:)];
[self startEngines];
}
RodeojogoereparenoconsoledoXcode.Acolisãojáestásendodetectada,e
portanto,podemospartirparaaatualiza çãodoplacarecria çãodosefeitosnecessá-
rios!
7 .2 E feitos
Nomomentoquedetectamosquedoisobjetosdojogocolidiram,algumascoisas
devemserfeitas.Vamoslistarparafacilitarofluxoaseguir.
• Executarumaanimação,comoexplosãoousimilar
• Removeroselementosdosarrays
• Atualizaroplacaroumostrarteladegameover
Vamoscome çarpelaanima ção. Existemdiversaspossibilidadesdeanima ção
utilizandooCocos2D.O frameworkoferecealgunsefeitostradicionaiscomo fadee
scale.Aideiaéconfigurarumasériedea ções,quejuntaseemumespa çocurtode
tempo,criamumaanima ção.
Paraoprimeiroexemplo,vamosanimarometeoroquandoéatingidopelotiro.
Nessemomento,animaremosometeoroparaquefiquepequeno,dandoaimpressão
quesumiuporseratingido.
Oquefaremosabaixoé:
• Reduziraescaladetamanhodaimagem
• Retirardatelacomumefeitoleve,chamadofade out
• Rodarambasemsequência
115


## Página 126

7.2. Efeitos CasadoCódigo
Apósrodarasequênciadeanima ções,precisamosretirarometeorodoarray
edamemória,poiselenãoexistemais.Precisamostambémpararoagendamento
desseobjeto,querodadetemposemtemposatualizandosuaposi çãoegerandoo
movimento.
Teremosumnovométodona Meteor,queseráinvocadoquandohouveraco-
lisão.Defina-ona Meteor.h:
- (void)gotShot;
Agoraimplementeométodona Meteor.m:
- (void)gotShot
{
// Para o agendamento
[self unscheduleUpdate];
// Cria efeitos
float dt = 0.2f;
CCScaleBy *a1 = [CCScaleBy actionWithDuration:dt scale:0.5f];
CCFadeOut *a2 = [CCFadeOut actionWithDuration:dt];
CCSpawn *s1 = [CCSpawn actionWithArray:
[NSArray arrayWithObjects:a1, a2, nil]];
// Método a ser executado após efeito
CCCallFunc *c1 = [CCCallFunc actionWithTarget:self
selector:@selector(removeMe:)];
// Executa efeito
[self runAction:[CCSequence actionWithArray:
[NSArray arrayWithObjects:s1, c1, nil]]];
}
Nométodoacimacancelamosoagendamentodaatualiza çãodeposi çãoecria-
mosasa çõesquejuntasfarãooefeitodesumirdometeoro.
OCocos2Dpossuiaindaummétodoquepodeserinvocadoparaqueoobjeto
sejaliberadodamemória.Essemétodoéo removeFromParentAndCleanup:e
seráinvocadologoapósaanima çãoacabar. Fazemosissovia CCCallFunc,pois
queremosqueométodo removeMe:sejainvocadodepoisdeaanima çãoterminar.
- (void)removeMe:(id)sender
{
116


## Página 127

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
// Quando o Meteoro é removido, limpa a memória utilizada pelo mesmo
[self removeFromParentAndCleanup:YES];
}
Animando o tiro
Utilizaremosomesmopensamentoparaanimarotiroquandocolidircomum
meteoro.Paraisso,criaremosométodo explodenaclasse Shoot,alterandoape-
nasalgunsparâmetros.
Essemétodoteráqueexecutaralgumasa ções:
• Pararoagendamentodamovimentaçãodometeoro
• Animaraexplosãodometeoro
• Limparoobjetodamemória
Vamosdeclararométodona Meteor.h:
- (void)explode;
Agoraimplementeométodona Meteor.m:
- (void)explode
{
// Para o agendamento
[self unscheduleUpdate];
// Cria efeitos
float dt = 0.2f;
CCScaleBy *a1 = [CCScaleBy actionWithDuration:dt scale:2.0f];
CCFadeOut *a2 = [CCFadeOut actionWithDuration:dt];
CCSpawn *s1 = [CCSpawn actionWithArray:
[NSArray arrayWithObjects:a1, a2, nil]];
// Método a ser executado após efeito
CCCallFunc *c1 = [CCCallFunc actionWithTarget:self
selector:@selector(removeMe:)];
// Executa efeito
[self runAction:[CCSequence actionWithArray:
[NSArray arrayWithObjects:s1, c1, nil]]];
}
117


## Página 128

7.2. Efeitos CasadoCódigo
Paralimparoobjetodamemória,chamaremosnovamenteométododoCo-
cos2Dchamado removeFromParentAndCleanup:.
- (void)removeMe:(id)sender
{
// Quando o Tiro é removido, limpa a memória utilizada pelo mesmo
[self removeFromParentAndCleanup:YES];
}
Já temos o código que o meteoro deve executar quando uma co-
lisão for detectada. Agora precisamos fazer a chamada a ele nos mo-
mento de colisão. Voltando à classe GameScene temos o método
checkRadiusHitsOfArray:againstArray:withSender:andCallbackMethod:,
quepercorredoisarrayseverificaintersec ções.
Nessemétodo,quandodoisobjetosestiveremcolidindo,algodeveserfeito.Essa
éumaparteimportantedojogoeprecisademuitocuidado. Reparequeonosso
métododedetec çãoégenérico,ouseja,elerecebedois arraysdeobjetoseanalisa
seocorrecolisãoentreeles.Nomomentoqueessacolisãoédetectada,eleprecisará
executaralgoquepodeseraexplosãodanaveouaexplosãodeummeteoro.
Éimportanteperceberqueadecisãodequalmétodorodarapósdetectadaaco-
lisãoéemtempodeexecu ção,eprecisaremosinvocá-lovia performSelector:.
No arquivo GameScene.m altere o método
checkRadiusHitsOfArray:againstArray:withSender:andCallbackMethod:.
//...
// Verifica colisão
if (CGRectIntersectsRect(rect1, rect2)) {
NSLog(@"Colisão Detectada: %@",
NSStringFromSelector(callbackMethod));
result = YES;
// Se o sender possui o método indicado na chamada do método,
// executa o mesmo com os objetos encontrados nos arrays
if ([sender respondsToSelector:callbackMethod]) {
[sender performSelector:callbackMethod
withObject:[array1 objectAtIndex:i]
withObject:[array2 objectAtIndex:j]];
}
// Se encontrou uma colisão, sai dos 2 loops
118


## Página 129

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
i = [array1 count] + 1;
j = [array2 count] + 1;
}
Apartirdaqui,bastafazeraschamadasaosmétodos gotShote explode.Na
GameScene.madicioneométodo meteorHit:withShoot::
- (void)meteorHit:(id)meteor withShoot:(id)shoot
{
// Quando houve uma colisão entre Meteoro e Tiro, indica que
// o Meteoro foi atingido e que o Tiro deve explodir
if ([meteor isKindOfClass:[Meteor class]]) {
[(Meteor *)meteor gotShot];
}
if ([shoot isKindOfClass:[Shoot class]]) {
[(Shoot *)shoot explode];
}
}
Rodeoprojetoetesteoquefizemosatéaqui!
Removendo objetos
Precisamoslembrarqueemboraosobjetosnãoestejammaisaparecendonatela
elescontinuamalocadosnamemória,ouseja,aindanãoforamremovidos. Cria-
remosagoraocódigoqueeliminaráosobjetosdosarraysapóscolisãoentretiroe
meteoro.
Primeiramente,vamoscriarum delegateparanossaclasse Meteorparaqueela
avisequandodeveráserremovida.Declareoprotocoloe delegatena Meteor.h:
@protocol MeteorDelegate;
@interface Meteor : CCSprite
@property (nonatomic, assign) float positionX;
@property (nonatomic, assign) float positionY;
@property (nonatomic, assign) id<MeteorDelegate>delegate;
+ (Meteor *)meteorWithImage:(NSString *)image;
119


## Página 130

7.2. Efeitos CasadoCódigo
- (void)start;
- (void)gotShot;
@end
@protocol MeteorDelegate <NSObject>
- (void)meteorWillBeRemoved:(Meteor *)meteor;
@end
Altereométodo gotShotparaqueometeoronotifiqueseudelegatedequeele
seráremovido:
- (void)gotShot
{
//...
// Notifica delegate
if ([self.delegate respondsToSelector:
@selector(meteorWillBeRemoved:)]) {
[self.delegate meteorWillBeRemoved:self];
}
}
Faremosamesmacoisaparaaclasse Shoot.Declareoprotocoloedelegatena
Shoot.h:
@protocol ShootDelegate;
@interface Shoot : CCSprite
@property (nonatomic, assign) id<ShootDelegate>delegate;
@property (nonatomic, assign) float positionX;
@property (nonatomic, assign) float positionY;
+ (Shoot *)shootWithPositionX:(float)positionX
andPositionY:(float)positionY;
- (void)start;
- (void)explode;
@end
120


## Página 131

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
@protocol ShootDelegate <NSObject>
- (void)shootWillBeRemoved:(Shoot *)shoot;
@end
Altereométodo explodeparaqueometeoronotifiqueseu delegatedequeele
seráremovido:
- (void)explode
{
//...
// Notifica delegate
if ([self.delegate respondsToSelector:
@selector(shootWillBeRemoved:)]) {
[self.delegate shootWillBeRemoved:self];
}
}
Agora,nanossa GameScene,todavezquecriarmosumnovo Meteorou
Shoot,queremospossibilitarqueelesavisemaprópria GameScenedequese-
rãoremovidos. Emoutraspalavras,a GameSceneseráodelegatedo Meteor
edo Shoot. Informena GameScene.hdequeelaimplementaráosprotocolos
MeteorDelegatee ShootDelegate:
@interface GameScene : CCLayer <MeteorsEngineDelegate,
PlayerDelegate,
MeteorDelegate,
ShootDelegate>
Agora altere os métodos playerDidCreateShoot: e
meteorsEngineDidCreateMeteor:na GameScene.mparaqueeledefinaos
delegates:
- (void)playerDidCreateShoot:(Shoot *)shoot
{
// O Player indicou que um novo Tiro foi criado
[self.shootsLayer addChild:shoot];
shoot.delegate = self;
[shoot start];
[self.shootsArray addObject:shoot];
}
121


## Página 132

7.3. Playermorre CasadoCódigo
- (void)meteorsEngineDidCreateMeteor:(Meteor *)meteor
{
// A Engine de Meteoros indicou que um novo Meteoro foi criado
[self.meteorsLayer addChild:meteor];
meteor.delegate = self;
[meteor start];
[self.meteorsArray addObject:meteor];
}
Feitoisso,bastafazeraremo çãodosobjetosna GameScene.m,implementando
osmétodos meteorWillBeRemoved:e shootWillBeRemoved:dosprotoco-
los:
- (void)meteorWillBeRemoved:(Meteor *)meteor
{
// Após atingido, um Meteoro notifica a GameScene
// para que seja removido do Array
meteor.delegate = nil;
[self.meteorsArray removeObject:meteor];
}
- (void)shootWillBeRemoved:(Shoot *)shoot
{
// Após explodir, um Tiro notifica a GameScene
// para que seja removido do Array
shoot.delegate = nil;
[self.shootsArray removeObject:shoot];
}
7 .3 P layer morre
Utilizandoamesmaestratégiavamosanimaroplayerquandoummeteorocolidir
comele. Paraisso,naclasse Playerteremosométodo explodecomoabaixo.
Declare-ona Player.h:
- (void)explode;
Eoimplementena Player.m:
- (void)explode
{
122


## Página 133

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
// Para o agendamento
[self unscheduleUpdate];
// Cria efeitos
float dt = 0.2f;
CCScaleBy *a1 = [CCScaleBy actionWithDuration:dt scale:2.0f];
CCFadeOut *a2 = [CCFadeOut actionWithDuration:dt];
CCSpawn *s1 = [CCSpawn actionWithArray:
[NSArray arrayWithObjects:a1, a2, nil]];
// Executa efeito
[self runAction:s1];
}
Para que seja executado, crie o métodoplayerHit:withMeteor: na
GameScene.m.Reparequeesteéométodode callbackquedefinimosquandoche-
camosascolisõesentreos arraysdeplayersemeteoros.
- (void)playerHit:(id)player withMeteor:(id)meteor
{
// Quando houve uma colisão entre Player e Meteoro,
// indica que ambos foram atingidos
if ([player isKindOfClass:[Player class]]) {
[(Player *)player explode];
}
if ([meteor isKindOfClass:[Meteor class]]) {
[(Meteor *)meteor gotShot];
}
}
Rodeoprojetoeverifiqueateladojogo!
7 .4 P lacar
Parafecharessecapítulo,vamosadicionarumapontua çãoparacadameteorodes-
truídoapósseratingidoporumtiro.Utilizaremosalgunsconceitosjávistosanteri-
ormente.
Primeiramente,trataremosovalordepontosqueaparecenatelacomoumanova
camada,ecamadasparaoCocos2Dsãoclassesqueherdamde CCLayer.
123


## Página 134

7.4. Placar CasadoCódigo
Essacamadaapresentaráospontosemnúmeroparaojogador.Paraisso,preci-
samosdeduasvariáveis.Aprimeiraédotipointeiro,queguardaospontosatuais.
Asegundaéumcampodetextoparacolocaressevalornatela.
Alémdisso,veremoscomoutilizarumtipodeletra( font type)diferenteparafa-
zerisso.ExistenoCocos2Dumaclassechamada CCLabelBMFont.Essaclassepos-
suiummétodochamado labelWithString:fntFile:querecebeuma stringe
umafonteaserusada.Depoisdisso,bastaconfigurarotamanhodaletraeposicio-
namento.
Alteraremosovalordo scorecomummétodochamado increase.Essemé-
todopoderáserchamadosemprequeumacolisãoentretiroemeteorofordetectada.
Crieaclasse Scoreedefinaaspropriedadesemétodosemseu header Score.h.
@interface Score : CCLayer
@property (nonatomic, assign) int score;
@property (nonatomic, retain) CCLabelBMFont *text;
+ (Score *)score;
- (void)increase;
@end
No initda Score.mcrieo labeldetexto:
+ (Score *)score
{
return [[[Score alloc] init] autorelease];
}
- (id)init
{
self = [super init];
if (self) {
// Inicializa a pontuação com o valor "0"
self.score = 0;
// Posiciona o Placar recém criado
self.position =
ccp(SCREEN_WIDTH() - 50.0f, SCREEN_HEIGHT() - 50.0f);
124


## Página 135

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
// Adiciona o Player na tela, como um texto para o jogador
self.text = [CCLabelBMFont labelWithString:
[NSString stringWithFormat:@"%d", self.score]
fntFile:@"UniSansSemiBold_Numbers_240.fnt"];
self.text.scale = (float)(240.0f / 240.0f);
[self addChild:self.text];
}
return self;
}
Implementetambémométodo increase.Seucódigoésimples,apenasincre-
mentaavariável scoreeconfiguranovamenteotextodoplacar.
- (void)increase
{
// Aumenta a pontuação e atualiza o Placar
self.score++;
self.text.string = [NSString stringWithFormat:@"%d", self.score];
}
Agoraquetemosacamadadoplacarpreparada,vamosadicioná-laàtelaprinci-
pal.Paraisso,criaremosdoisobjetos:umdotipo CCLayereoutrodotipo Score.
Na GameScene.hadicione:
# import "Score.h"
//...
@property (nonatomic, retain) CCLayer *scoreLayer;
@property (nonatomic, retain) Score *score;
Énecessárioiniciaracamadaeadicioná-laatela.No initda GameScene.m
adicione:
- (id)init
{
self = [super init];
if (self) {
//...
// CCLayer para o Placar
self.scoreLayer = [CCLayer node];
[self addChild:self.scoreLayer];
}
125


## Página 136

7.5. Conclusão CasadoCódigo
return self;
}
Parafinalizar,bastacriaroobjetodotipo Scoreeadicionaracamadacorres-
pondente.
Ainda na classe GameScene adicione essa chamada ao método
addGameObjects:
- (void)addGameObjects
{
//...
// Cria o Placar
self.score = [Score score];
[self.scoreLayer addChild:self.score];
}
Agoraaltereométodo meteorHit:withShoot:paraqueaumenteoscore
quandohouvercolisãoentreumtiroeummeteoro:
- (void)meteorHit:(id)meteor withShoot:(id)shoot
{
//...
// Aumenta a pontuação
[self.score increase];
}
7 .5 C onclusão
Detectarcolisõesdeformamanual,comofeitonocapítulodoprotótipo,nãoétão
simpleseenvolvemuitoscálculosmatemáticos. Porém,utilizandoum framework
comooCocos2Dascoisassãofacilitadas.
Nessecapítulopassamospeloquepodeserconsideradoocora çãodojogo,a
detecçãodecolisões.Apartirdelas,executamosefeitoseatualizamosatelaparao
jogador.
Opróximocapítulotratarádeumapartemuitoimportanteparadarvidaaos
jogos,ossonseefeitos.
126


## Página 137

Capítulo8
Adicionandosonsemúsica
Ossonssãodefundamentalimportâncianodesenvolvimentodeumgame. Hoje
existemprofissõescomo sound designersquetrabalhamespecificamentecriandoos
sonsdosgames.Muitosjogosutilizamorquestrasparaexecutarsuatrilhasonora.
Amúsicadávidaaojogo,torna-omaisdivertidoedárespostasaojogadorpara
aspartesimportantes.
Existemduasformasprincipaisdesonsnomundodosgames:músicaeefeitos.
Quandoojogocome ça,umamúsicadefundonormalmentedáoclimadojogo.
Essamúsicaénormalmenteexecutadaem backgroundeserepeteinúmerasvezesao
longodogame.Alémdela,existemosefeitosdesomgeradosemmomentosimpor-
tantes,comoquandoumacolisãoédetectadaouquandooplacaréalterado
Paraonossojogo,utilizaremossonsencontradosgratuitamentenositehttp://
www.freesound.org/.Vocêpodebuscardiversostiposdesonsnessesiteparaoseu
próximogame!


## Página 138

8.1. Executandosons CasadoCódigo
8.1 E xecutando sons
Nessaprimeiraetapautilizaremoso frameworkCocos2Dparaadicionarsoma3
eventosdojogo.Utilizaremos3arquivosdesonsdiferentes:
• Disparodeumtiro
• Colisãodotirocomummeteoro
• Colisãoentremeteoroeavião
Podemos utilizar os formatos mais comuns para adicionar sons ao nosso
jogo, eaquioformatoescolhidoserá wav. Colocaremosossonsnodiretório
Resources/Soundsdonossoprojeto.
Vocêpodeencontrartodosossonsqueserãoutilizadosnessecapítulonesse link:
https://github.com/bivissoft/jogos_ios_14bis
SoundEngine
Para lidar com sons, o Cocos2D disponibiliza uma classe chamada
SimpleAudioEngine, que possui diversos métodos que possibilitam traba-
lharcomsonsemúsicanogame. Parautilizaressaclassenãoénecessáriocriar
umainstância,massimutilizarum Singletondisponibilizadopelo framework.
Paraissoexecutamos [SimpleAudioEngine sharedEngine] tendoacessoàs
opçõesdesonsdequeprecisamos.
Comesseacesso,podemosexecutarmúsicasesons,parareiniciararquivosde
áudio,aumentarediminuirovolumeetc.Nessemomento,iniciaremosexecutando
3sonsutilizandoométodo playEffect:.Essemétodorecebecomoparâmetroo
nomedoarquivodeáudio.
Para facilitar, importaremos a classeSimpleAudioEngine no arquivo
Prefix.pch:
# ifdef __OBJC__
//...
# import "SimpleAudioEngine.h"
# endif
Oprimeiroefeitodesom,otiro,serácolocadonaclasse Shoot. Adicioneo
códigoabaixoaométodo startda Shoot.m:
128


## Página 139

CasadoCódigo Capítulo8. Adicionandosonsemúsica
- (void)start
{
//...
// Som do Tiro
[[SimpleAudioEngine sharedEngine] playEffect:@"shoot.wav"];
}
Opróximosomseráexecutadoquandoocorreracolisãoentremeteoroetiro.
Noarquivo Meteor.madicioneocódigoabaixonoiníciodométodo gotShot:
- (void)gotShot
{
// Som ao ser atingido
[[SimpleAudioEngine sharedEngine] playEffect:@"bang.wav"];
//...
}
Parafinalizar,adicionaremosumsomquandoummeteoroatingiroavião.No
arquivo Player.madicioneocódigoabaixonoiníciodométodo explode:
- (void)explode
{
// Som ao explodir
[[SimpleAudioEngine sharedEngine] playEffect:@"over.wav"];
//...
}
Agoraogamejáexecutaráossonsquandoumdos3eventosacima(tiroecoli-
sões)acontecerem!
8.2 C ache de sons
VimoscomoexecutarsonsutilizandooCocos2D.Porém,vocêdeveterreparadoem
umproblemagrave:aprimeiravezqueumdossonsprecisasertocado,eledemora
muito.Issosedeveaofatodo frameworkinicializarosomapenasnomomentoque
foinecessário.Existeumaestratégiaeboapráticaparasolucionaresseproblema,o
cachedesons.
Paracolocarumsomnocachedevemosiniciá-lojánoiníciodogame. Cria-
remosentãoummétodocomessaresponsabilidadena GameScene.mchamado
preloadCache. Essemétodofaráocachedos3sonsqueestamosutilizandoaté
aqui.
129


## Página 140

8.3. Músicadefundo CasadoCódigo
- (void)preloadCache
{
// Cache de sons do Jogo
[[SimpleAudioEngine sharedEngine] preloadEffect:@"shoot.wav"];
[[SimpleAudioEngine sharedEngine] preloadEffect:@"bang.wav"];
[[SimpleAudioEngine sharedEngine] preloadEffect:@"over.wav"];
}
Adicione a chamada do método preloadCache no construtor da
GameScene.m,naúltimalinhadométodo:
- (id)init
{
self = [super init];
if (self) {
//...
// Cache de sons do Jogo
[self preloadCache];
}
return self;
}
Rodenovamenteoprojetoeverifiquequeagoraossonsrespondemperfeita-
menteaomomentodostirosecolisões!
8.3 M úsica de fundo
Agoraquejátrabalhamoscomossonsdogame, vamosvercomolidarcoma
músicadojogo. Amúsicaseráiniciadaquandoojogadorentrarnateladejogo.
Paraisso,usaremosamesmaclasse SimpleAudioEngineporémcomométodo
playBackgroundMusic:loop:.
Noconstrutorda GameScene.madicioneachamadaamúsica.
- (id)init
{
self = [super init];
if (self) {
//...
// Música do Jogo
[[SimpleAudioEngine sharedEngine]
playBackgroundMusic:@"music.wav" loop:YES];
130


## Página 141

CasadoCódigo Capítulo8. Adicionandosonsemúsica
}
return self;
}
Outrométodoimportanteéoqueparaamúsica. Essemétodoéchamado
pauseBackgroundMusic.Faremosissologoapósoefeitodeexplosãoentreme-
teoroeaviãonaclasse Player.m:
- (void)explode
{
//...
// Pausa a música de fundo
[[SimpleAudioEngine sharedEngine] pauseBackgroundMusic];
}
Rodeoprojetoevejacomoosomadicionavidaaojogo.Tiro,colisõesemúsica
devemestarfuncionandonessemomento!
8.4 C onclusão
Sonsemúsicasãomuitoimportantesparaosjogos. Reparenosjogosfamososou
mesmoosquevocêmaisgostaereparenatrilhasonora. Mesmoosjogosantigos
possuíamsonsmuitoespeciaisparacadajogo.
Éimportantíssimodefinirumaboatrilhasonoraeefeitosparaoseupróximo
game!
131


## Página 143

Capítulo9
Voandocomagravidade!
Omundodosgamesfoitotalmenterevitalizadocomos smartphones.Jogosque
atéentãoeramsimplesejánãoatraiammaistantoaaten çãodosjogadoresforam
remodeladoscomasnovaspossibilidadesdeexperiênciaqueosaparelhosmodernos
podemproporcionar.
Amaioriadosjogosquefazemsucessonoscelulareshojefazusodealgumre-
cursodoaparelho,como touch screen,arrastandoobjetosnatelaouutilizando
agravidadecomoacelerômetro,emovimentandooselementosdeumamaneira
diferentedosjogosparaconsoles.
Nessecapítulotrocaremosamovimenta çãodoaviãofeitaporbotõespelocon-
trolebaseadonamovimenta çãodocelular!Aexperiênciaserálevadaaoutronível,
nãomaissendoumsimplesjogocombotões,massim,utilizandoumrecursonativo
doaparelhoquefazcomqueogametenhaumamelhorjogabilidade!
Paraestecapítulo,parapoderrodarojogonoseupróprioaparelhoetestaro
acelerômetro,vocêprecisaráserum“Desenvolvedor Apple Registrado”. Aofimdo
capítulo,nossoaviãopoderápercorreratela,ficandocomonafiguraaseguir:


## Página 144

9.1. UsandooAcelerômetro CasadoCódigo
Figura9.1:Controleporacelerômetro.
9.1 U sando o Acelerômetro
Vamosiniciarplanejandoousodoacelerômetroesabendoondequeremoschegar.
Nossoobjetivoéretirarosbotõesquemovimentamoaviãoparaesquerdaedireita.
Semessesbotões,moveremosoaviãoapartirdascoordenadasqueocelularcaptar
demovimentonoaparelho.Dividiremosessetrabalhoem3partesprincipais.
• Capturarascoordenadasdemovimentaçãohorizontaleverticaldoaparelho
• Controlarainstabilidadedomovimentodoavião
• Calibraressascoordenadasparaocontrolefuncionaremposiçõesdiferentes
134


## Página 145

CasadoCódigo Capítulo9. Voandocomagravidade!
Capturando as coordenadas
Aprimeiracoisaqueprecisamossaberécomoo iOSpodenosenviarinfor-
maçõesdoacelerômetro.Issoéfeitoatravésdaclasse CMMotionManagerdo fra-
mework CoreMotion,própriodoiOS.Oqueocorrequandousamosestaclasse?
Semprequeiniciamosa CMMotionManager,elacome çaacolherasinforma-
çõesdoacelerômetrodoaparelhoemumintervalodetempoquedefinirmos.Assim,
acadamovimenta çãododispositivo,asinforma çõesdeacelera çãosãoatualizadas
nométodo startAccelerometerUpdatesToQueue:withHandler:,ondeo
blocodo handlerpossuidoisobjetos,sendoumdelesum CMAccelerometerData,
queemnossocódigochamaremosde accelerometerData.
Essaéumapartemuitoimportante,evocêdeverepararqueacadachamada
desteblocopelo CMMotionManager,oobjeto accelerometerDataéatualizado,
comosnovosvaloresdeposi çãodoaparelho.Essesvaloresserãoinformadosem3
variáveis,querepresentamoseixosX,YeZdoaparelho,comodemostradonafigura
aseguir.
Figura9.2:EixosX,YeZ.
Depossedessasinforma ções,conseguiremossaberseoaparelhosemoveupara
umdeterminadoladoeatualizaraposi çãodoavião.Essaéumaconclusãoimpor-
tante,ouseja,quandopercebemosqueocelularestáinclinadoparaumdeterminado
lado,atualizamosessaposi çãodoavião.
135


## Página 146

9.1. UsandooAcelerômetro CasadoCódigo
A classe Accelerometer
Vamoscriarumaclasseresponsávelporinstanciarum CMMotionManagere
capturarseusvalores.Maisàfrente,veremoscomofazerolinkentreelaeamovi-
mentaçãodoavião.
Paracome çar,precisamosimportaro framework CoreMotionparanossopro-
jeto. Paraimportarum framework,nomenuàesquerdaselecioneseuprojetoe
depoiscliqueno target bis. Naaba Build Phases,em Link Binary With
Librariescliquenobotãodeadicionareescolhao CoreMotion.framework.
Pronto!temoso frameworkimportadoemnossoprojeto.
Agoracriaremosaclasse Accelerometerbemsimples,comosubclasseda
NSObject.Nestaclasse,vamosinstanciaro CMMotionManagerecriarmétodos
parainiciarepararomesmo.Tambémvamosvercomocapturarasposi çõesXeY
doaparelho.Paraisso,criaremos2propriedadesquevãoguardarasinforma çõesdo
acelerômetro.O header Accelerometer.hficaráassim:
# import <CoreMotion / CoreMotion.h>
@interface Accelerometer : NSObject
@property (nonatomic, retain) CMMotionManager *motionManager;
- (void)startAccelerometerUpdates;
- (void)stopAccelerometerUpdates;
@property (nonatomic, assign) float currentAccelerationX;
@property (nonatomic, assign) float currentAccelerationY;
@end
Na Accelerometer.mvamosinstanciara CMMotionManagerno inite
criarosmétodosqueretornamasacelera çõesXeY:
@implementation Accelerometer
- (id)init
{
self = [super init];
if (self) {
self.motionManager =
136


## Página 147

CasadoCódigo Capítulo9. Voandocomagravidade!
[[[CMMotionManager alloc] init] autorelease];
self.motionManager.accelerometerUpdateInterval = 0.01f; // 100Hz
}
return self;
}
- (void)startAccelerometerUpdates
{
// Verifica se o dispositivo possui acesso ao Acelerômetro e o inicia
if ([self.motionManager isAccelerometerAvailable]) {
// Zera as propriedades
self.currentAccelerationX = 0.0f;
self.currentAccelerationY = 0.0f;
// Inicia atualizações do acelerômetro
[self.motionManager
startAccelerometerUpdatesToQueue:[NSOperationQueue mainQueue]
withHandler:^(CMAccelerometerData *accelerometerData,
NSError *error)
{
self.currentAccelerationX = accelerometerData.acceleration.x;
self.currentAccelerationY = accelerometerData.acceleration.y;
}];
}
}
- (void)stopAccelerometerUpdates
{
// Quando os dados do Acelerômetro não são mais necessários,
// deve-se parar as atualizações
if ([self.motionManager isAccelerometerActive]) {
[self.motionManager stopAccelerometerUpdates];
}
}
@end
Oquetemosatéaqui? Umaclassequerecebeinforma çõesdemovimenta ção
doaparelho.Elanãofoiinicializadaainda,maslogomaispoderáserutilizadapara
atualizaraposi çãodanave.
137


## Página 148

9.1. UsandooAcelerômetro CasadoCódigo
Paracontinuar,faremosqueessaclassesecomportecomoum Singleton,
tendoapenasumobjetodotipo Accelerometernojogo. Paraisso,noarquivo
Accelerometer.hdeclareummétodoestáticoqueretornaráainstânciaúnicada
classe:
+ (Accelerometer *)sharedAccelerometer;
Noarquivo Accelerometer.madicioneoseguintecódigo:
static Accelerometer *sharedAccelerometer = nil;
+ (Accelerometer *)sharedAccelerometer
{
if (!sharedAccelerometer) {
sharedAccelerometer = [[Accelerometer alloc] init];
}
return sharedAccelerometer;
}
Dessaforma,nãocorremosriscosdemaisdeumobjetodessetiposerinstanci-
adonojogo.Agora,jápodemospensaremfazero linkcomaclasse Player.
Configurando o player
Todavezqueoacelerômetroatualizarasposi çõesdevemosmoveroavião.Isso
ocorreráemumaquantidademuitograndedevezesporsegundo,dandoaimpressão
demovimento. Comoemoutrasclasses,iremosagendarométodo updatepara
queoplayerbusqueasacelera çõesXeYdaclasse Accelerometereatualizesua
posição.
Criaremosométodo monitorAccelerometerparaqueoplayerinicieaclasse
deacelerômetroeagendeseupróprioupdate.Definaométodona Player.h:
# import "Accelerometer.h"
//...
- (void)monitorAccelerometer;
Na Player.mimplementeestemétodoeoupdate:
- (void)monitorAccelerometer
{
// Inicia a Atualização do Acelerômetro
[[Accelerometer sharedAccelerometer] startAccelerometerUpdates];
138


## Página 149

CasadoCódigo Capítulo9. Voandocomagravidade!
// Inicia a Animação / Movimentação do Player
[self scheduleUpdate];
}
- (void)update:(float)dt
{
NSLog(@"X: %f", [[Accelerometer sharedAccelerometer]
currentAccelerationX]);
NSLog(@"Y: %f", [[Accelerometer sharedAccelerometer]
currentAccelerationY]);
}
Agoravamosalterarométodo startGameda GameScene.mparaquepe ça
aoplayerparamonitoraroacelerômetroquandoojogoforiniciado:
- (void)startGame
{
//...
// Ao entrar na GameScene, inicia o monitoramento do Acelerômetro
[self.player monitorAccelerometer];
}
VocêpodeexecutaroprojetoagoraeolharnoconsoledoXcodeascoordenadas
sendoimpressas.
Oquetemosnestemomento?Aclasse Accelerometerquerecebecoordena-
dasdoaparelhoeaclasse Playerpreparadaparaleressesvalores.
Movendo o player
Agoraquejáestamoslendoascoordenadasdoacelerômetronaclasse Player
jápodemosmovimentá-lo. Ométodoupdateéquemalteraaposi çãodoavião,
então,vamosalterá-lo.
Aideiaaquiserámoverumadasquatropossíveiscoordenadasdoavião,sejaho-
rizontal(direitaouesquerda)ouvertical(cimaoubaixo).Ascoordenadasenviadas
peloacelerômetroseguemopadrãodoseixos,fazendocomquemovimenta çõespara
umladosejamnúmerospositivoseparaoladoopostonúmerosnegativos.Omesmo
ocorreparaoeixoX,enviandonúmerospositivosparaumadire çãoenegativospara
aposi çãooposta.
139


## Página 150

9.1. UsandooAcelerômetro CasadoCódigo
Combasenessainforma ção,analisaremosascoordenadasqueoacelerômetro
enviouealteraremosaposi çãodoavião.
Naclasse Playeraltereométodo update::
- (void)update:(float)dt
{
if ([[Accelerometer sharedAccelerometer]
currentAccelerationX] < -0.0f) {
self.positionX--;
}
if ([[Accelerometer sharedAccelerometer]
currentAccelerationX] > 0.0f) {
self.positionX++;
}
if ([[Accelerometer sharedAccelerometer]
currentAccelerationY] < -0.0f) {
self.positionY--;
}
if ([[Accelerometer sharedAccelerometer]
currentAccelerationY] > 0.0f) {
self.positionY++;
}
// Checa limites da tela
if (self.positionX < 30.0f) {
self.positionX = 30.0f;
}
if (self.positionX > SCREEN_WIDTH() - 30.0f) {
self.positionX = SCREEN_WIDTH() - 30.0f;
}
if (self.positionY < 30.0f) {
self.positionY = 30.0f;
}
if (self.positionY > SCREEN_HEIGHT() - 30.0f) {
self.positionY = SCREEN_HEIGHT() - 30.0f;
}
// Configura posição do Avião
self.position = ccp(self.positionX, self.positionY);
}
140


## Página 151

CasadoCódigo Capítulo9. Voandocomagravidade!
Jáépossívelrodarojogoeveroaviãosemovendoapartirdamovimenta çãodo
aparelho!Fa çaoteste.
Experimentedeixaratelaparalelaaumamesa.Algoestranho,não?Pareceque
eleestáenfrentandoumacerta“turbulência”.
9.2 C ontrolando a instabilidade
Vocêdeveterpercebidoqueocontroledoaviãoficouinstável.Issoocorreporque
nãoestamosusandonenhumatolerânciaparamoveroavião,ouseja,movemossem-
preindependentedeserumamovimenta çãorealmenteválidadoaparelho.Oace-
lerômetronãoéperfeito,alémdequeelepegamovimenta çõesminúsculas,sempre
gerandoeventos!
Paramelhorarisso,vamosusarumlimite.Emvezdecompararcomzero,utili-
zaremosumaconstantedetolerância.Chamaremosessaconstantede kNOISE.Ela
definiráovalormínimoqueoacelerômetrodeveseralteradopararealmentemover
oavião.
Crieaconstanteealtereométodo update:na Player.m.
# define kNOISE 0.15f
//...
- (void)update:(float)dt
{
if ([[Accelerometer sharedAccelerometer]
currentAccelerationX] < -kNOISE) {
self.positionX--;
}
if ([[Accelerometer sharedAccelerometer]
currentAccelerationX] > kNOISE) {
self.positionX++;
}
if ([[Accelerometer sharedAccelerometer]
currentAccelerationY] < -kNOISE) {
self.positionY--;
}
if ([[Accelerometer sharedAccelerometer]
currentAccelerationY] > kNOISE) {
self.positionY++;
}
//...
}
141


## Página 152

9.3. Calibrandoapartirdaposi çãoinicialdoaparelho CasadoCódigo
Apartirdestemomento, devemosterumbomcontroledoavião, podendo
movimentá-loportodaatela. Oúnicoinconvenienteéquenãotemosumacali-
braçãoparautilizaroacelerômetro,ouseja,elefuncionabemparaaposi çãoinicial
zero,queéaaquelaquandodeixamosoaparelhoparadoemumamesa,porexemplo.
9.3 C alibrando a partir da posição inicial do apa -
relho
Vamosutilizarumaestratégiadecalibra çãonojogo!Aideiaénãosebasearapenas
naposi çãoenviadapeloacelerômetroparamoveroplayer,masfazerantesalgumas
contasparaentenderaposi çãoqueojogadorestásegurandooaparelhoeconsiderá-
lacomoaposi çãoZERO,ouposi çãoinicial.
Paraissofaremosalgumasaltera çõesnaclasse Accelerometer. Criaremos
novaspropriedadesqueserãoresponsáveisporguardarinforma çõessobreacalibra-
ção.Essaspropriedadesguardarãoasinforma çõesiniciaisesejátemosacalibra ção
concluída.
Na Accelerometer.hcrieasseguintespropriedades:
@property (nonatomic, assign) int calibrated;
@property (nonatomic, assign) float calibratedAccelerationX;
@property (nonatomic, assign) float calibratedAccelerationY;
Alteraremos também o método startAccelerometerUpdates na
Accelerometer.m. Nele, calibraremos o acelerômetro recebendo as 30 pri-
meirasinforma çõesdoacelerômetro.Comesses30primeirosvaloresguardaremos
aposi çãoinicialdoaparelho.
Apartirdisso,faremosumaaltera çãonovalorqueéenviadoparamoveroavião.
Aoinvésdeenviarovalordiretamenteinformadopeloacelerômetro,vamostirara
posiçãoinicial,paraterapenasamudan çarelativaàquelamovimenta ção.
# define kCALIBRATIONCOUNT 30
- (void)startAccelerometerUpdates
{
// Verifica se o dispositivo possui acesso ao Acelerômetro e o inicia
if ([self.motionManager isAccelerometerAvailable]) {
// Zera as propriedades
self.currentAccelerationX = 0.0f;
142


## Página 153

CasadoCódigo Capítulo9. Voandocomagravidade!
self.currentAccelerationY = 0.0f;
self.calibrated = 0;
self.calibratedAccelerationX = 0.0f;
self.calibratedAccelerationY = 0.0f;
// Inicia atualizações do acelerômetro
[self.motionManager
startAccelerometerUpdatesToQueue:[NSOperationQueue mainQueue]
withHandler:^(CMAccelerometerData *accelerometerData,
NSError *error)
{
if (self.calibrated < kCALIBRATIONCOUNT) {
// Soma posições do acelerômetro
self.calibratedAccelerationX +=
accelerometerData.acceleration.x;
self.calibratedAccelerationY +=
accelerometerData.acceleration.y;
self.calibrated++;
if (self.calibrated == kCALIBRATIONCOUNT) {
// Calcula a média das calibrações
self.calibratedAccelerationX /= kCALIBRATIONCOUNT;
self.calibratedAccelerationY /= kCALIBRATIONCOUNT;
}
} else {
// Atualiza aceleração atual
self.currentAccelerationX =
accelerometerData.acceleration.x -
self.calibratedAccelerationX;
self.currentAccelerationY =
accelerometerData.acceleration.y -
self.calibratedAccelerationY;
}
}];
}
}
Porque30vezes?Ojogadoracaboudeapertarobotãoplayeestáajeitandosua
melhorposi ção. Entãovamosdarumatolerânciaparaler30atualiza çõesdoace-
lerômetroetirarumamédiadelas.Comisso,conseguiremosdefinirqualaposi ção
inicialdoaparelho.
143


## Página 154

9.4. Desafioscomoacelerômetro CasadoCódigo
Vocêpodemanteros logsporumtempoparaentenderosvaloresenviadose
depoisapagá-los.Nessemomentooaviãojádeveestarsendocontroladopelamo-
vimentaçãodoaparelho!
Retirando os botões
Provavelmentevocênãovaiquerermovermaisoaviãoutilizandoosbotõeses-
querdaedireita. Umaformasimplesderemovê-losénãoincluí-losnomenude
botões,alterandoaslinhasaseguir,nométodo initda GameScene.m:
// CCMenu *menu = [CCMenu menuWithItems:leftControl,
// rightControl,
// shootButton,
// nil];
CCMenu *menu = [CCMenu menuWithItems:shootButton,
nil];
9.4 D esafios com o acelerômetro
Utilizarrecursoscomoacelerômetropodetornarojogomuitomaisdivertidoeen-
gajador,sendoumdaquelesdetalhesquefazemaexperiênciadogamesertotalmente
única.Quetalmelhoraraindamaisessaexperiênciacomassugestõesabaixo?
• Controledevelocidade:Vocêpodefazerque,quantomaisinclinado,oavião
deslizemais.Seeleestiverpoucoinclinado,emvezdeincrementaravariável
xem1,vocêincrementariaem0.5oualgoproporcionalàacelera çãoindicada
peloacelerômetro.
• Oacelerômetropodemandarsinaisinvertidosdeacordocomainclina ção.
Dependendodacalibra ção,vocêprecisadetectarseissoestaocorrendo,para
nãomudaraorienta çãodoaviãorepentinamente!Issodáumcertotrabalho...
9.5 C onclusão
Esseéumcapítulotrabalhoso,masmuitogratificante.Utilizarrecursosdosapare-
lhoséumdosprincipaisapelosdarevolu çãodosjogosparacelular.Sabertrabalhar
bemcomessespoderososrecursospodeelevarojogoaumníveldejogabilidade
muitomaisinteressante!
144


## Página 155

CasadoCódigo Capítulo9. Voandocomagravidade!
Figura9.3:Controleporacelerômetro.
145


## Página 157

Capítulo10
Telafinalegameover
Todoofluxodojogoestábemencaminhado,desdeateladeabertura,passando
pelascolisões,efeitos,sonseacelerômetro.Agoracriaremosduastelasquefecharão
ocicloprincipaldogame.
Aprimeiratelaasercriadaseráatelamostradaquandoojogoacabar,ouseja,
quandoo14bisvenceros100meteoros.
Essatelaserácompostaporumamúsicafinal,porumaimagemnovaeumbotão
deiniciodojogo.
Aofinal,deveremosteratelacomoabaixo.


## Página 158

10.1. Telafinal CasadoCódigo
Figura10.1:Teladofinaldojogo.
10.1 T ela final
Para montar a tela de final de jogo precisaremos de mais uma imagem, a
finalend.png(esuaversãoHD finalend-hd.png). Importeessasimagens
paraoprojetoeincluaadefini çãopadrãona Assets.h.
# define kFINALEND @"finalend.png"
Vamoscriaraclassequerepresentaráatelafinal.Elaseráumanova CCLayer
eseunomeserá FinalScreen.
Comotodascene,declareno FinalScreen.hoconstrutor:
148


## Página 159

CasadoCódigo Capítulo10. Telafinalegameover
@interface FinalScreen : CCLayer
+ (CCScene *)scene;
@end
Na FinalScreen.mimplementaremosométododecria çãodascene.Apro-
veitaremoso initparainicializarosobjetos background,someimagemdelogo.
Faremosissocomojáfizemosemoutrastelas:
- (id)init
{
self = [super init];
if (self) {
// Imagem de Background
CCSprite *background = [CCSprite spriteWithFile:kBACKGROUND];
background.position =
ccp(SCREEN_WIDTH() / 2.0f, SCREEN_HEIGHT() / 2.0f);
[self addChild:background];
// Som
[[SimpleAudioEngine sharedEngine] playEffect:@"finalend.wav"];
// Imagem
CCSprite *title = [CCSprite spriteWithFile:kFINALEND];
title.position =
ccp(SCREEN_WIDTH() / 2.0f, SCREEN_HEIGHT() - 130.0f);
[self addChild:title];
}
return self;
}
Configuraremos,aindano init,obotãoqueiniciaojogonovamente:
//...
// Cria o botão para reiniciar o jogo
CCMenuItemSprite *beginButton = [CCMenuItemSprite
itemWithNormalSprite:[CCSprite spriteWithFile:kPLAY]
selectedSprite:[CCSprite spriteWithFile:kPLAY]
target:self
selector:@selector(restartGame:)];
149


## Página 160

10.1. Telafinal CasadoCódigo
// Define a posição do botão
beginButton.position = ccp(0.0f, 0.0f);
// Cria o menu que terá o botão
CCMenu *menu = [CCMenu menuWithItems:beginButton, nil];
[self addChild:menu];
Quandoojogadorselecionarobotãodereiniciarojogo,eleretornaráàtelaini-
cial TitleScreen.Vamosimportaratelainicialna FinalScreen.h:
# import "TitleScreen.h"
Voltandoà FinalScreen.m, obotãochamaráométodo restartGame:
quandoselecionado,paraqueretorneàtelainicialdenossogame. Vamosimple-
mentarestemétodo.
- (void)restartGame:(id)sender
{
// Pausa a música de fundo
[[SimpleAudioEngine sharedEngine] pauseBackgroundMusic];
// Transfere o Jogador para a TitleScreen
[[CCDirector sharedDirector] replaceScene:
[CCTransitionFade transitionWithDuration:1.0
scene:[TitleScreen scene]]];
}
Paraqueessaclassepossaservistanojogo,aclasse GameScenedeveestarciente
einicializá-la.Paraisso,vamosimportara FinalScreenemnossa GameScene.h
# import "FinalScreen.h"
Agorana GameScene.mteremosométodo startFinalScreenquefaza
transiçãoparaatelafinal.
- (void)startFinalScreen
{
// Transfere o Jogador para a FinalScreen
[[CCDirector sharedDirector] replaceScene:
[CCTransitionFade transitionWithDuration:1.0
scene:[FinalScreen scene]]];
}
150


## Página 161

CasadoCódigo Capítulo10. Telafinalegameover
Equandoteremosateladefinaldojogo? Faremosissoquando100meteoros
foremdestruídos!Porém,parafacilitarostestes,mostraremosatelafinalquando5
meteorosforemdestruídos.
Aindana GameScene.m,nométodo meteorHit:withShoot:vamosincluir
achamadadatelafinalapósaumentaroscore,casoestesejamaiorouiguala5:
- (void)meteorHit:(id)meteor withShoot:(id)shoot
{
//...
// Verifica o máximo score para vencer o jogo
if (self.score.score >= 5) {
[self startFinalScreen];
}
}
Aodestruir5meteorosjádevemosteratelafinalcomosomdavitória!
151


## Página 162

10.2. TelaGameOver CasadoCódigo
Figura10.2:Teladofinaldojogo.
10.2 T elaGame Over
Ateladegameoverseguiráamesmalógicadatelafinal,porémdeveráserinici-
alizadaemumoutromomento. Quando? Simples,quandoummeteoroatingiro
avião!
Vamosaocódigo.Primeiro,importeaimagem gameover.png(esuaversão
HD gameover-hd.png)eincluaadefini çãopadrãona Assets.h.
# define kGAMEOVER @"gameover.png"
Crieaclasse GameOverScreenqueéuma CCLayer.Nessaclasse,utilizaremos
amesmaideiadateladefinaldejogo.A GameOverScreen.hficaráassim:
152


## Página 163

CasadoCódigo Capítulo10. Telafinalegameover
# import "TitleScreen.h"
@interface GameOverScreen : CCLayer
+ (CCScene *)scene;
@end
O initda GameOverScreen.mtambémébemsimples,parecidocomoque
jáconhecemos:
+ (CCScene *)scene
{
// 'scene' is an autorelease object.
CCScene *scene = [CCScene node];
// 'layer' is an autorelease object.
GameOverScreen *layer = [GameOverScreen node];
// add layer as a child to scene
[scene addChild:layer];
// return the scene
return scene;
}
- (id)init
{
self = [super init];
if (self) {
// Imagem de Background
CCSprite *background = [CCSprite spriteWithFile:kBACKGROUND];
background.position =
ccp(SCREEN_WIDTH() / 2.0f, SCREEN_HEIGHT() / 2.0f);
[self addChild:background];
// Som
[[SimpleAudioEngine sharedEngine] playEffect:@"finalend.wav"];
// Imagem
CCSprite *title = [CCSprite spriteWithFile:kGAMEOVER];
title.position =
153


## Página 164

10.2. TelaGameOver CasadoCódigo
ccp(SCREEN_WIDTH() / 2.0f, SCREEN_HEIGHT() - 130.0f);
[self addChild:title];
// Cria o botão para reiniciar o jogo
CCMenuItemSprite *beginButton = [CCMenuItemSprite
itemWithNormalSprite:[CCSprite spriteWithFile:kPLAY]
selectedSprite:[CCSprite spriteWithFile:kPLAY]
target:self
selector:@selector(restartGame:)];
// Define a posição do botão
beginButton.position = ccp(0.0f, 0.0f);
// Cria o menu que terá o botão
CCMenu *menu = [CCMenu menuWithItems:beginButton, nil];
[self addChild:menu];
}
return self;
}
Para que o botão de reiniciar o jogo funcione, implemente o método
restartGame:.
- (void)restartGame:(id)sender
{
// Pausa a música de fundo
[[SimpleAudioEngine sharedEngine] pauseBackgroundMusic];
// Transfere o Jogador para a TitleScreen
[[CCDirector sharedDirector] replaceScene:
[CCTransitionFade transitionWithDuration:1.0
scene:[TitleScreen scene]]];
}
Achamadaaessateladeveserfeitaquandoacolisãoentremeteoroeaviãofor
detectada.Paraisso,importea GameOverScreenna GameScene.h:
# import "GameOverScreen.h"
Agora adicione a transição ao método playerHit:withMeteor: da
GameScene.m:
154


## Página 165

CasadoCódigo Capítulo10. Telafinalegameover
- (void)playerHit:(id)player withMeteor:(id)meteor
{
//...
// Ao ser atingido, o Jogador é transferido à GameOverScreen
[[CCDirector sharedDirector] replaceScene:
[CCTransitionFade transitionWithDuration:1.0
scene:[GameOverScreen scene]]];
}
Ateladegameoverdeveestaraparecendoquandoometeorocolidecomoavião,
comomostradoaseguir.
Figura10.3:Teladegameover.
155


## Página 166

10.3. Conclusão CasadoCódigo
10.3 C onclusão
Esseéumcapítulosimples,poisjáconhecemostudoqueénecessárioparacria ção
detelasetransi ções.Vocêpodeusarsuaimagina çãoecriardiversasnovastelasno
game!
156


## Página 167

Capítulo11
Pausandoojogo
Nessecapítulofalaremosdemaisumaparteimportantíssimadeumjogo,atelade
pause.Essatelanãocostumaserdasmaisdivertidasdeserdesenvolvida,atémesmo
pelafalsaimpressãodequepodeserumatelasimples.Porém,tenhaaten çãoaqui!
Teremosmuitosconceitosimportantesnessemomento.
Paranãoseenganar,vamosàlistadefuncionalidadesqueumateladepausedeve
ter.
• Construirumanovacamadaparaateladepause
• Criarumaclassequeentenderáseojogoestáempauseourodando
• Criarmaisumbotãonateladejogo,obotãopause
• Fazerolinkentreateladepauseeteladejogo
• Pararrealmenteosobjetosnatela


## Página 168

11.1. Montandoateladepause CasadoCódigo
Vejacomoateladepausepodeenganar. Sãomuitascoisasaseremfeitaspara
quetudofuncionebem.
Repareque,semprequepossível,fazerumalistadefuncionalidadesesperadas
natelapodeajudaravercommaisprofundidadeotrabalhoqueseránecessário
desenvolver.
Aofinaldessecapítuloateladeveráestarcomoabaixo:
Figura11.1:Teladepause.
11.1 M ontando a tela de pause
Vamoscome çardeformasimplesecomoquejávimosatéomomento. Atelade
pauseénaverdademaisumacamadadentrodeumatela,ouseja,nãomudaremos
158


## Página 169

CasadoCódigo Capítulo11. Pausandoojogo
decena( CCScene).Comoanteriormente,todanovacamadanoCocos2Dpodeser
representadapelaclasse CCLayer.
Umaparteimportantedessatelaéqueelaterá2botões:o“continuar”,quevolta
projogo,eo“sair”,quevaiparaateladeabertura.
Criaremososdoisbotõesnessacamadacomaclassejáutilizadaemoutraspartes
dogame,a CCMenuItemSprite.
Crieaclasse PauseScreen,subclasseda CCLayer,comoheaderabaixo:
@interface PauseScreen : CCLayer
+ (PauseScreen *)pauseScreen;
@end
Apróximaetapaéadicionaraseguintelistanessatela:
• Definirumbackground,nessecasoumpretotranslúcido
• Colocarologo,comonateladeabertura
• Adicionarosbotões
• Posicionarosbotões
Importeaimagem exit.png(esuaversãoHD exit-hd.png)paraoprojeto
eincluaadefini çãopadrãona Assets.h:
# define kEXIT @"exit.png"
Agora,na PauseScreen.m,implementeométodo pauseScreeneadicione
osbotõesno init,comoabaixo:
+ (PauseScreen *)pauseScreen
{
return [[[PauseScreen alloc] init] autorelease];
}
- (id)init
{
self = [super init];
if (self) {
159


## Página 170

11.1. Montandoateladepause CasadoCódigo
// Cor de Background
CCLayerColor *background =
[CCLayerColor layerWithColor:ccc4(0, 0, 0, 175)
width:SCREEN_WIDTH()
height:SCREEN_HEIGHT()];
[self addChild:background];
// Imagem de Logo
CCSprite *title = [CCSprite spriteWithFile:kLOGO];
title.position =
ccp(SCREEN_WIDTH() / 2.0f, SCREEN_HEIGHT() - 130.0f);
[self addChild:title];
// Cria os botões
CCMenuItemSprite *resumeButton = [CCMenuItemSprite
itemWithNormalSprite:[CCSprite spriteWithFile:kPLAY]
selectedSprite:[CCSprite spriteWithFile:kPLAY]
target:self
selector:@selector(resumeGame:)];
CCMenuItemSprite *quitButton = [CCMenuItemSprite
itemWithNormalSprite:[CCSprite spriteWithFile:kEXIT]
selectedSprite:[CCSprite spriteWithFile:kEXIT]
target:self
selector:@selector(quitGame:)];
// Define as posições dos botões
resumeButton.position = ccp(0.0f, 0.0f);
quitButton.position = ccp(0.0f, -100.0f);
// Cria o menu que terá os botões
CCMenu *menu = [CCMenu menuWithItems:resumeButton,
quitButton,
nil];
[self addChild:menu];
}
return self;
}
Nessemomentotemosateladepause,porémessaésóaprimeiraparte.Repare
quecriarumateladepausenãoéalgodiferentedastelasanterioresdojogo,porém,
fazerocontrolequeelaprecisademandaránovosconceitos.Vamosaeles.
160


## Página 171

CasadoCódigo Capítulo11. Pausandoojogo
11.2 C ontrolando o Game Loop
Lembradaanalogiadedesenhosemblocosdepapeldocapítulosobreprotótipos?
Falamosqueumjogopodesercomparadoaumasequênciadeimagensquesão
desenhadasacadamudan çanoposicionamentodosobjetosdojogo,gerandoaim-
pressãodemovimento.
Oqueissoimportaparaateladepause?Precisamosterumcontroledoqueo
jogoestárodando,ouseja,objetosrealmentedojogoenãoemtelasdeabertura,
porexemplo.Alémdisso,precisamossaberseojogoestápausadoounãonaquele
momento.
Comumavariáveldecontroledeestado,podemosdefinirsedevemosmostrar
ateladepause,sedevemosparalisarosobjetosnatela,retomarosmovimentosdos
objetosetc.
Faremosessecontrolecomumaclassequeteráapenasessaresponsabilidade.
Crieaclasse Runner,subclasseda NSObject,edefinaavariáveldecontroleem
seu header Runner.h:
@interface Runner : NSObject
@property (nonatomic, assign, getter = isGamePaused) BOOL gamePaused;
+ (Runner *)sharedRunner;
@end
Essaclasseteráalgumaspeculiaridades.Umadelaséqueelasóteráumainstân-
ciaativanoprojeto,paraquenãoocorramconfusõesentreosestados.Ouseja,ela
seráum Singleton.
Paraisso,definaométodo sharedRunnerna Runner.hparaqueretornea
instânciaúnicadenossaclasse:
+ (Runner *)sharedRunner;
Na Runner.mimplementeestemétodo:
static Runner *sharedRunner = nil;
+ (Runner *)sharedRunner
{
if (!sharedRunner) {
sharedRunner = [[Runner alloc] init];
161


## Página 172

11.3. Adicionandoobotãodepause CasadoCódigo
}
return sharedRunner;
}
Semprequeprecisarmosfazeraverifica çãodoestadodogame,chamaremoso
método sharedRunnerquenosdevolveráareferênciaqueestácuidandodisso.
Casoaindanãotenhasidocriada,serácriadanessemomento.
Comaclasse Runnersendoum Singleton,podemosaqualquermomento
acessarapropriedade gamePausedparasaberoestadodogame.
Essaclassepodeparecersimples.Um Singletoncomumaúnicapropriedade.
Porém,suafuncionalidadeédeextremaimportâncianogame.Vamosutilizá-laem
váriosmomentos.
Comoutilizaremoso Runneremdiversasclasses,importe-ona Prefix.pch:
# import "Runner.h"
11.3 A dicionando o botão de pause
Apróximaetapaérelativamentesimples.Iremosadicionarobotãopausenatelado
jogo.Paraissoprecisamosdeumnovoarquivo,aimagemdobotãopause.Importe-o
paraoprojetoeadicione-onoarquivo Assets.h.
# define kPAUSE @"pause.png"
Adicionaremosessenovobotãonomenudaclasse GameScene. Oobjetivoé
criarumanovavariáveldotipo CCMenuItemSprite,adicioná-lanacamadade
botões,configurarométodode callbackeposicioná-lanatela.
Vamoscriarobotãono initda GameScene.m,juntocomosdemais:
- (id)init
{
self = [super init];
if (self) {
//...
// Cria os botões
//...
CCMenuItemGameButton *pauseButton = [CCMenuItemGameButton
itemWithNormalSprite:[CCSprite spriteWithFile:kPAUSE]
selectedSprite:[CCSprite spriteWithFile:kPAUSE]
162


## Página 173

CasadoCódigo Capítulo11. Pausandoojogo
target:self
selector:@selector(pauseGame:)];
// Define as posições dos botões
//...
pauseButton.position = ccp(-120.0f,
(SCREEN_HEIGHT() / 2.0f) - 30.0f);
// Cria o menu que terá os botões
//...
CCMenu *menu = [CCMenu menuWithItems:shootButton,
pauseButton,
nil];
[self.gameButtonsLayer addChild:menu];
}
return self;
}
Parafechar,vamoscriarométodo pauseGame:,chamadoquandoobotão
pausefortocadona GameScene.m:
- (void)pauseGame:(id)sender
{
NSLog(@"Botão selecionado: Pausa");
}
11.4 A interface entre jogo e pause
Defatoumateladepausenãoétãosimplescomopodeparecer,certo? Recapitu-
lando,nessecapítulocriamosatéaqui3coisas:ateladepause,umaclassedecontrole
deestadoseadicionamosobotãodepausenateladejogo.
Ésemprebomparareanalisaroquejáfoifeitoemtarefasquesãograndescomo
essaseenvolvemdiversasclasses.
Tendoaclassedateladepauseeosbotões,precisamosfazerojogoentender
quandoeledevemostrá-la.
11.5 P ausando o jogo
Começaremosafazero linkentretudoquefoivistonessecapítuloagora!Aprincipal
ideiaéorquestrartudoquefizemospelaclasse GameScene,queéateladojogo,
163


## Página 174

11.5. Pausandoojogo CasadoCódigo
receberáoeventodepauseeativaráa PauseScreen.
Paraqueateladepausepossaservista,precisaremosadicionarumanovaca-
madana GameScene.Criaremosumacamadadotipo CCLayereumobjetodo
tipo PauseScreen.
Na GameScene.hcrieaspropriedades:
# import "PauseScreen.h"
//...
@property (nonatomic, retain) CCLayer *topLayer;
@property (nonatomic, retain) PauseScreen *pauseScreen;
No initda GameScene.miniciaremosacamadaevamosadicionaramesma
àcenaatual.
- (id)init
{
self = [super init];
if (self) {
// CCLayer para o exibição da tela de Pause
self.topLayer = [CCLayer node];
[self addChild:self.topLayer];
}
}
Feitoisso,umanovacamadaexistenateladejogo,masaindasemrela çãoque
queremoscomateladepause.
Métodos de pause
Vamosseguirfazendoesse link.Faremosateladejogosaberquealgunsmétodos
depausesãonecessários,nessecaso, pause, resumee quit.
Vamosimplementarcadaumdos3métodosdepauseagora.Oprimeiroseráo
pauseGame:,jácriado.Oqueessemétododevefazeréverificarseogameestáro-
dando,ouseja,seojogonãoestáempause.Casoissosejaverdadeiro,configuramos
avariáveldepausepara YES.
Na GameScene.maltereométodo pauseGame::
- (void)pauseGame:(id)sender
{
NSLog(@"Botão selecionado: Pausa");
164


## Página 175

CasadoCódigo Capítulo11. Pausandoojogo
if ([Runner sharedRunner].isGamePaused == NO) {
[Runner sharedRunner].gamePaused = YES;
}
}
Agoravamosfazerateladepauseavisarateladejogoquandoobotãode resume
ou quitfoiselecionado.Faremosistoatravésde delegate.Anossateladejogoseráo
delegatedateladepause.
Na PauseScreen.hdeclareoprotocolo PauseScreenDelegateeapropri-
edade delegate:
@protocol PauseScreenDelegate;
@interface PauseScreen : CCLayer
@property (nonatomic, assign) id<PauseScreenDelegate>delegate;
+ (PauseScreen *)pauseScreen;
@end
@protocol PauseScreenDelegate <NSObject>
- (void)pauseScreenWillResumeGame:(PauseScreen *)pauseScreen;
- (void)pauseScreenWillQuitGame:(PauseScreen *)pauseScreen;
@end
Vamosinformarquenossa GameSceneimplementaráosmétodosdoprotocolo
dateladepause,alterandooarquivo GameScene.h:
@interface GameScene : CCLayer <MeteorsEngineDelegate,
PlayerDelegate,
MeteorDelegate,
ShootDelegate,
PauseScreenDelegate>
Opróximopassoécriarosmétodosdoprotocolona GameScene.m. Pri-
meiro,ométodoqueremoveateladepauseparacontinuarojogo. Nele,confi-
guramosopausepara NO.Adicioneométodo pauseScreenWillResumeGame:
na GameScreen.m:
165


## Página 176

11.5. Pausandoojogo CasadoCódigo
- (void)pauseScreenWillResumeGame:(PauseScreen *)pauseScreen
{
if ([Runner sharedRunner].isGamePaused == YES) {
// Continua o jogo
self.pauseScreen.delegate = nil;
self.pauseScreen = nil;
[Runner sharedRunner].gamePaused = NO;
}
}
Parafechar,implementaremosométodo pauseScreenWillQuitGame:,o
maissimplesentreos3.Nele,vamospararossonsqueestamostocando.Alémdisso,
faremosumatransi çãoparaateladeabertura.
- (void)pauseScreenWillQuitGame:(PauseScreen *)pauseScreen
{
[SimpleAudioEngine sharedEngine].effectsVolume = 0.0f;
[SimpleAudioEngine sharedEngine].backgroundMusicVolume = 0.0f;
// Transfere o Jogador para a TitleScreen
[[CCDirector sharedDirector] replaceScene:
[CCTransitionFade transitionWithDuration:1.0
scene:[TitleScreen scene]]];
}
Iniciando tudo
Precisamosconfiguraravariáveldecontroledeestadologonocome çodojogo.
Nométodo startGameda GameScreen.mvamosadicionaraconfigura çãode
pauseabaixo:
- (void)startGame
{
// Configura o status do jogo
[Runner sharedRunner].gamePaused = NO;
//...
}
Ajustaremosagoraométodoresponsávelporiniciarateladepause,queserá
acionadopelobotãodepause. Paraisto,altereométodo pauseGame:naclasse
GameScreen.m:
166


## Página 177

CasadoCódigo Capítulo11. Pausandoojogo
- (void)pauseGame:(id)sender
{
NSLog(@"Botão selecionado: Pausa");
if ([Runner sharedRunner].isGamePaused == NO) {
[Runner sharedRunner].gamePaused = YES;
}
if ([Runner sharedRunner].isGamePaused == YES &&
self.pauseScreen == nil) {
self.pauseScreen = [PauseScreen pauseScreen];
self.pauseScreen.delegate = self;
[self.topLayer addChild:self.pauseScreen];
}
}
Agoraquejátemososmétodosdepausecriadosna GameScreen,vamosvoltar
àclasse PauseScreen.mereferenciarasa çõesdosbotões,paraquenotifiquemo
delegate:
- (void)resumeGame:(id)sender
{
if ([self.delegate respondsToSelector:
@selector(pauseScreenWillResumeGame:)]) {
[self.delegate pauseScreenWillResumeGame:self];
[self removeFromParentAndCleanup:YES];
}
}
- (void)quitGame:(id)sender
{
if ([self.delegate respondsToSelector:
@selector(pauseScreenWillQuitGame:)]) {
[self.delegate pauseScreenWillQuitGame:self];
}
}
Aorodaroprojeto,ateladepausedeveaparecermasaindatemostrabalhoa
fazer.
167


## Página 178

11.6. Pausandoosobjetos CasadoCódigo
11.6 P ausando os objetos
Temostodaaarquiteturapreparadaparaopause,masalgomuitoimportanteainda
nãofoifeito.Aorodaroprojetoeapertaropause,temosatelaaparecendo,porém,
nãotemososobjetosparando.
Precisamosusaraclasse Runnerquecontrolaoestadodogameparaisso.Será
atravésdoscontrolesdessaclassequepoderemosdefinirseosobjetoscomometeo-
ros,tiroseaviãodevemsemoverno game loop.
Alógicaparaissoserásempreigual. Apenasmovimentaremosumobjetona
teladejogoseojogonãoestiverempause. Alémdisso,sópodemoscriarnovos
elementosseessacondi çãotambémforsatisfatória.
Na MeteorsEngine.madicioneaverifica çãoabaixo:
- (void)meteorsEngine:(float)dt
{
// Checa se o jogo está em execução
if ([Runner sharedRunner].isGamePaused == NO) {
// Sorte: 1 em 30 gera um novo meteoro!
if(arc4random_uniform(30) == 0) {
if ([self.delegate respondsToSelector:
@selector(meteorsEngineDidCreateMeteor:)]) {
[self.delegate meteorsEngineDidCreateMeteor:
[Meteor meteorWithImage:kMETEOR]];
}
}
}
}
Na Meteor.madicioneaverifica çãoabaixoduranteo update:
- (void)update:(float)dt
{
// Checa se o jogo está em execução
if ([Runner sharedRunner].isGamePaused == NO) {
// Move o Meteoro para baixo
self.positionY -= 1.0f;
self.position = ccp(self.positionX, self.positionY);
}
}
Na Shoot.madicioneaverifica çãoabaixo:
168


## Página 179

CasadoCódigo Capítulo11. Pausandoojogo
- (void)update:(float)dt
{
// Checa se o jogo está em execução
if ([Runner sharedRunner].isGamePaused == NO) {
// Move o Tiro para cima
self.positionY += 2;
self.position = ccp(self.positionX, self.positionY);
}
}
Naclasse Playeradicioneasverifica çõesabaixo:
- (void)update:(float)dt
{
// Checa se o jogo está em execução
if ([Runner sharedRunner].isGamePaused == NO) {
//... Demais códigos
}
}
- (void)moveLeft
{
// Checa se o jogo está em execução
if ([Runner sharedRunner].isGamePaused == NO) {
//... Demais códigos
}
}
- (void)moveRight
{
// Checa se o jogo está em execução
if ([Runner sharedRunner].isGamePaused == NO) {
//... Demais códigos
}
}
- (void)shoot
{
// Checa se o jogo está em execução
if ([Runner sharedRunner].isGamePaused == NO) {
//... Demais códigos
169


## Página 180

11.7. Conclusão CasadoCódigo
}
}
Muitotrabalho,não? Ateladepausepodeenganar,mascomofoivisto,éum
pontochavenodesenvolvimentodosgames.Rodeoprojetoeverifiqueocompor-
tamentodessanovatelanojogo.
11.7 C onclusão
Fazerumateladepauseénormalmenteumapartequeosdesenvolvedoresdeixam
deladonaconstru çãodeumgameedepoispercebemacomplexidadedesuaimple-
mentação.Essatelausaconceitosquesepropagamportodoogameedeveserfeita
comcuidadoeplanejamento.
Anotíciaboaéquesevocêchegouatéaquivocêjátemosconceitosprincipais
paradesenvolverumjogo!Imagens, loop,camadas,sons,colisõesetc.Nãosãocoisas
fáceis,mascomapráticaviramconceitosqueserepetemportodoogame.
170


## Página 181

CasadoCódigo Capítulo11. Pausandoojogo
Figura11.2:Teladepause.
171


## Página 183

Capítulo12
Continuandonossojogo
Depoisdesabercomocriarabasedeumjogoesuaestrutura,montaroscenárioe
iteraçõesecriartelasdefluxodogame,muitacoisapodeserdesenvolvidadeacordo
comasuaimagina ção.Apartemaislegaldeagoraemdianteserápensaremideias
quepossamtornarojogocadavezmaisdivertidoemotivante.Omundodosgames
ésempreummundodenovidades,deinova ções,emquecadanovaideiadámargem
paramilharesdenovosjogos.
Essecapítulomostrarásugestõesdecomotornarogamemaissocial,dinâmico
e,quemsabe,rentável.
12.1 U tilizando ferramentas sociais
Para tornar o jogo mais engajador podemos adicionar diversas funcionalidades
como rankings,ondeosusuáriosdisputamqueméomelhor, achievementsqueser-
vemcomomedalhasparaprovarconquistasduranteojogoeatémonetizaroapli-
cativocomitensespeciais.


## Página 184

12.2. Highscore CasadoCódigo
AAppleforneceestasferramentasdeformanativa,simplificandomuitotodo
essedesenvolvimento, comos frameworks GameKit(parao Game Center)e
StoreKit(paraos In-App Purchases,quesãoasvendasdentrodojogo).
12.2 H ighscore
Os rankingsou highscoresno Game Center sãochamadosde Leaderboards.Aideia
écriarummuralondetodososusuáriossãoordenadosparasaberquemsãoos
melhores.
Aimplementa çãoésimpleseconsistebasicamentenospassosexemplificadosa
seguir.Primeiro,deve-seautenticarousuáriono Game Center:
GKLocalPlayer *localPlayer = [GKLocalPlayer localPlayer];
localPlayer.authenticateHandler = ^(UIViewController *viewController,
NSError *error)
{
if (viewController != nil) {
[self showAuthenticationDialogWhenReasonable:viewController];
} else if (localPlayer.isAuthenticated) {
[self authenticatedPlayer:localPlayer];
} else {
[self disableGameCenter];
}
}];
Apósaautentica ção,pode-seenviarapontua çãoparao Game Center,indi-
candoemqual Leaderboardamesmaseráregistrada:
GKScore *scoreReporter = [[GKScore alloc]
initWithCategory:br.com.casadocodigo.bis.meteoros];
scoreReporter.value = meteorosDestruidos;
[scoreReporter reportScoreWithCompletionHandler:^(NSError *error)
{
// Código executado após reportar o score
}];
ParaexibiroGameCenterdentrodoseujogo,pode-seimplementarocódigo
abaixo:
174


## Página 185

CasadoCódigo Capítulo12. Continuandonossojogo
GKGameCenterViewController *gameCenterVC =
[[GKGameCenterViewController alloc] init];
if (gameCenterVC != nil) {
gameCenterVC.gameCenterDelegate = self;
gameCenterVC.viewState = GKGameCenterViewControllerStateLeaderboards;
gameCenterVC.leaderboardTimeScope = GKLeaderboardTimeScopeToday;
gameCenterVC.leaderboardCategory = br.com.casadocodigo.bis.meteoros;
[self presentViewController:gameCenterVC
animated:YES
completion:nil];
}
Figura12.1:CriandoLeaderboards.
Maisdetalhessobreo Game Center e Leaderboardspodemserencontradosna
documentaçãodaApple:
https://developer.apple.com/library/ios/#documentation/NetworkingInternet/
Conceptual/GameKit_Guide/Introduction/Introduction.html
175


## Página 186

12.3. Achievements CasadoCódigo
12.3 A chievements
Imagineseapósdestruir10meteorosojogadorganhasseotítulode Piloto Pró,
eapósdestruir50ganhasseotítulode Piloto Master.Quetal,aofimdojogo,
entregaro Achievement Santos Dumont aojogador?Essascria çõestornamojogo
maisatrativo,commaisobjetivos,einclusivepodemsercompartilhadasemredes
sociais.
Acria çãode Achievementsusandoo Game Center tambéméfácil.Vocêape-
nasdefineos Achievementsdojogoeinformaaporcentagemcompletadaatravésdo
Game Center.
if (meteorosDestruidos == 50) {
GKAchievement *achievement = [[GKAchievement alloc]
initWithIdentifier:br.com.casadocodigo.bis.pilotomaster];
if (achievement) {
achievement.percentComplete = 100;
[achievement reportAchievementWithCompletionHandler:
^(NSError *error) {
if (error != nil) {
NSLog(@"Erro: %@", error);
}
}];
}
}
Crie ideias interessantes deAchievements e implemente-as com oGame
Center.
176


## Página 187

CasadoCódigo Capítulo12. Continuandonossojogo
Figura12.2:CriandoAchievements.
Maisdetalhessobreo Game Center e Achievementspodemserencontradosna
documentaçãodaApple:
https://developer.apple.com/library/ios/#documentation/NetworkingInternet/
Conceptual/GameKit_Guide/Introduction/Introduction.html
12.4 D esafios para você melhorar o jogo
Aquivãoalgumassugestõesquevisamdesafiaroleitorasolidificarosconhecimentos
adquiridoscomolivroeampliaroengajamentodojogo14bis.
Novos tiros
Todojogadoradoraincrementarsuamuni ção. Crieumtiroduploparao14
bis! Essestirosdevemsairnãomaisemlinharetamassimformandoumangulo
de45grausparacadalado. Interessantefazeressetiroserdadoaojogadorapós
algumaconquistadogame,comodestruirumnúmerodemeteoros,ouatirarem
umelementoespecialquedêessepoder!
177


## Página 188

12.5. Comoganhardinheiro? CasadoCódigo
Diferentes meteoros
Quemdissequetodososmeteorossãoiguais?Quetalimplementartamanhos
diferentesdemeteoros,quepontuamdeformadiferente,deacordocomseutama-
nho?Comecesimples,meteorosmaioresvalem2pontosemeteorosmenorescon-
tinuamvalendo1.Comissoimplementado,mudeaimagemdosmeteoroseatéco-
loqueesporadicamenteoutroselementosquepodemvaler5ou10pontos,masque
apareçamcomumafrequênciamenor.Valetambémfazercomqueosmeteoroste-
nhamvelocidadesdiferentesentresi!
Armaduras
Morrercomapenasummeteoroéchato,maspodemoscapturarumelemento
quefortifiqueoavião!Crieumelementoquefuncionecomoumaarmaduraeper-
mitaacolisãoentreummeteoroeoavião.Lembre-sedemostraraojogadorqueele
estáequipadocomesseelemento,mudandoacordoavião,porexemplo.
Efeitos nos sprites
Atualmente,osobjetossãoestáticosnonossogame. Quetaladicionarefeitos
comofazerometeorodescergirandoouluzesnoavião? Essespequenosdetalhes
fazemojogoparecermuitomaisatraente.
12.5 C omo ganhar dinheiro?
Omundodosgamesmoveumvalorenormeeéhojeumadasmaioresmovimen-
taçõesfinanceirasdomundo.Esselivronãovisatrazeranálisessobreessemercado
financeiro,porémhojeascifrasdosgamessuperamosnúmerosdocinema.
Paramonetizarogamevocêpodeseguirpordiversasabordagens,comoestabe-
lecerumvalordevendaquandoousuáriobaixá-lo.
Umaoutraformabeminteressantedeganhardinheirocomojogoédeixando-o
gratuitooucobrandoumvalorbembaixo,comoqualousuáriovaiinstalarojogo
semmuitoesfor ço.Apósisso,ojogodevecativarousuárioeentãopode-seoferecer
itensaseremcompradosquemelhoremaexperiênciaeperformancedojogo.
O framework StoreKitdaAppleofereceumaformabeminteressanteefácilde
aplicarparamonetizarogame.Vocêpodeadicionaressesitenscompoucaslinhas
decódigo,comodescritoaseguir.
178


## Página 189

CasadoCódigo Capítulo12. Continuandonossojogo
Iniciealojainternadeseuaplicativojáno AppDelegate.m,garantindoque
quaisquertransa çõespendentessejamprocessadas.
[[SKPaymentQueue defaultQueue] addTransactionObserver:self];
BusquenoiTunesConnecttodososseusprodutos,obtendoentãoquaisestão
disponíveis(ativos)eseuspre çosatuaisparaalojadopaísdousuário.
SKProductsRequest *request = [[SKProductsRequest alloc]
initWithProductIdentifiers:(NSSet *)productsID];
request.delegate = self;
[request start];
Quandoojogadorescolherumitemparaacompranaloja,comouma“Super
Bomba”,ojogodevecomunicar-secomoiTunesConnect,solicitandoacomprado
item.
SKPayment *payment = [SKPayment
paymentWithProduct:br.com.casadocodigo.bis.SUPER_BOMBA];
[[SKPaymentQueue defaultQueue] addPayment:payment];
OiTunessolicitaoAppleIDeasenhadousuárioautomaticamente,casoneces-
sário.Apósprocessaracompra,ojogoénotificadoe,casotenhasidoefetivadacom
sucesso,vocêdeveliberarparaojogadoroqueelecomprou,comoa“SuperBomba”
doexemplo. Entãovocêdeveremoveressatransa çãodafiladepagamentos,para
quenãosejaprocessadanovamente.
[[SKPaymentQueue defaultQueue] finishTransaction:transaction];
Figura12.3:Exemplodeitenspagos.
Detalhessobre In-App Purchase podemserencontradosnadocumenta ção
daApple:
https://developer.apple.com/library/ios/#documentation/NetworkingInternet/
Conceptual/StoreKitGuide/Introduction/Introduction.html
179


## Página 190

12.6. Conclusão CasadoCódigo
12.6 C onclusão
Desenvolverjogoséumatarefacomplexaeaomesmotempodivertida,alémdeser
umaótimamaneiradeelevaroconhecimentodeprograma ção.Atualmente,oscelu-
laresmodernostrouxeramumaoportunidadeúnicaparaquedesenvolvedorespos-
samteressaexperiência,criandoseusprópriosgames,umarevolu çãosimilaràque
awebeoscomputadorespessoaisgeraramalgunsanosatrás.
Alémdisso,criarjogoséumexercíciodecriatividadequepermiteexplorara
nossaimagina çãoecriarhistóriasinterativaseúnicas.Esselivrotentacompartilhar
essesconhecimentoseideias,esperandoserdefatoútilatodosaquelesqueestão
ingressandonessemágicomundodejogosparaiOS.
Ficanovamenteoconviteparavocêparticipardanossalistadediscussão:
https://groups.google.com/group/desenvolvimento-de-jogos-para-ios
Boadiversão!
180
