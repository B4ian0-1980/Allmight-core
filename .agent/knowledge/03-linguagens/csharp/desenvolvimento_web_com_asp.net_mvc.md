---json
{
  "id": "desenvolvimento_web_com_asp-net_mvc",
  "title": "Desenvolvimento web com ASP.NET MVC",
  "categoria": "03-linguagens",
  "subcategoria": "csharp",
  "resumo": "**Arquivo Original:** `Desenvolvimento web com ASP.NET MVC.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "asp",
    "asp.net",
    "com",
    "csharp",
    "desenvolvimento",
    "linguagens",
    "mvc",
    "net"
  ],
  "perguntas_tipo": [
    "Como utilizar Desenvolvimento web com ASP.NET MVC?",
    "Quais as boas praticas de csharp?"
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
  "dono": "stack-csharp",
  "prioridade": 2
}
---

# Desenvolvimento web com ASP.NET MVC

> **Arquivo Original:** `Desenvolvimento web com ASP.NET MVC.pdf`
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

CasadoCódigo
Agradecimentos
Umaobracomoestaésemprefrutodoesfor çodiretoouindiretodemuitaspessoas.
Assim,nadamaisjustoquededicaralgumaspoucas,masexpressivas,palavrasaelas.
FabrícioLopesSanchez
ADeus,pelacapacidadeintelectualmínimapararealizarumprojetocomoeste.
Àminhafamília,poratuaremcomoluzesquandotudoemvoltaseapaga.
AoMárcioFabioAlthmann(muitomaisdoqueumprofissionalderenome,um
amigo),pelaparcerianesteprojeto.
ÀeditoraCasadoCódigo,poracreditarnoprojetoefornecertodosuportede
queprecisamosdurantetodooprocessodecomposiç ãodestaobra.
MárcioFabioAlthmann
Atodaminhafamíliaeamigos.
EmespecialàminhaesposaJulianeMateusCosta.Sempremeapoiandoedando
forçasparaencararevencerosobstáculos.
AoFabrícioSanchezquefelizmenteaceitouconstruircomigoesseprojeto.
i

## Página 5

CasadoCódigo
Sobreosautores
Estelivroéoresultadofinaldeanosdeestudoeacúmulodeexperiênciadedois
profissionaisdomercadodetecnologia,maisespecificamente,dovolátileevolutivo
universodedesenvolvimentodesoftware.Estase çãoédedicadaavocêquedeseja
sabermaissobreosautoresdestaobra.
FabrícioLopesSanchez
FabrícioLopesSanchez égraduadoemCiênciadaComputaçãoemestreem
ProcessamentoDigitaldeSinais.Commaisde15anosdeexperiêncianomercadode
desenvolvimentodesoftwares,Fabrícioacumulouconhecimentossólidosemdife-
rentesplataformastecnológicas(C/C++,Java,PHP),emboratenhaseespecializado
emdesenvolvimentoparawebnaplataformaMicrosoft.Desenvolvedor,arquitetoe
diretordetecnologiadeumastartup(cargoqueexercenosdiasatuais)sãoalgumas
dasfunçõesexercidasporFabrícionosúltimosanos.Atuoutambémcomoespeci-
alistatécnicodeprojetosdecomputaçãoemnuvemnaMicrosoftBrasil,ondepôde
participardegrandesprojetosutilizandoaplataformadaempresaparaestefim(a
saber,WindowsAzure).Em2011,FabríciofoinomeadopelaMicrosoftcomo:Most
ValuableProfessional:(MVP)nacategoriaASP.NET/IIS,prêmioqueaempresacon-
cedeaprofissionaisaosquaiselajulgadestaquesemsuastecnologias.
Fabrícioescrevedeformarecorrenteemseublog: http://fabriciosanchez.com.br.
Alémdisso,elepodeserencontradotambémnoTwitteratravésdousuário@San-
chezFabricio.
MárcioFabioAlthmann
MárcioFábioAlthmannpossuimaisde10anosdeexperiêncianomercadode
desenvolvimentodesoftwareeéespecialistanaplataforma.NET.
Coautordolivro Desenvolvendo para web usando o Visual Studio 2008 noqual
iii

## Página 6

CasadoCódigo
abordouotemaExplorandooAcessoaDadosUtilizandoLINQToSQL.
VencedordoconcursoWinThe7realizadopelaMicrosoftBrasil,nacategoriaDe-
senvolvimento.GraçasaoconcursoteveaoportunidadedeconhecerasededaMi-
crosoftemRedmondnosEUA.
AtualmentetrabalhanaequipedetecnologiadaBennerSistemas,equipeque
éresponsávelpordesenvolverasferramentasutilizadaspelosdesenvolvedoresda
empresa.
Blog: http://www.marcioalthmann.net GitHub: http://github.com/
marcioalthmannTwitter:@marcialthmann
iv

## Página 7

CasadoCódigo
Prefácio
A plataforma ASP.NET continua a evoluir e expandir, acompanhando a web.
Quandoomodelo web formsdedesenvolvimentofoiintroduzido,eletrouxeàpro-
gramaçãowebdesenvolvedoresquejápossuíamamplaexperiênciacomdesenvolvi-
mentopara desktops.OASP.NET web formscolocaumacamadadeabstraçãosobre
oprotocoloHTTP,possibilitandoassimummodelodedesenvolvimentobaseado
emeventos.Algomaisfamiliarparaestesdesenvolvedores.Comoawebsemodi-
ficoueintroduziunovastécnicas, tagseapresentouoamplopoderdoJavaScript,a
plataformaASP.NETprecisouacompanhartalevolução.
O frameworkASP.NETMVCvalorizacoisasdiferentesdoASP.NET web forms.
EnquantoaplicaçõesASP.NETweb formspossibilitamacriaçãodeinterfacesricas
utilizandoHTML5eJavaScriptutilizandoummodelobaseadoemcontrolesdeser-
vidorvinculadosatrechosdecódigosespecíficos,oASP.NETMVCdisponibiliza
omesmopoderdeformadiferente,trazendoodesenvolvedormaispara“pertodo
metal”.AplicaçõeswebbaseadasnoframeworkMVCnosdáocontroleabsolutode
todososelementosHTMLedecadabyteafio.AplicaçõesMVCexigemquedesen-
volvedoresconheçammaissobreweb,poiselepermite“abraçar”cadadetalhedela.
TodosasaplicaçõesconstruídascomatecnologiaASP.NET—WebFormse
MVC—sãobaseadasnomesmonúcleo.Cadaumdestesmodeloscompartilhacon-
ceitoscomuns,comodiretóriospadrão,editoresmodeloseorepositóriospadrão.
ParaentenderdeformaassertivaoASP.NETecomtodososseusaspectos,épreciso
recorreramanuaiselivrosquepossamajudar.Éaíquelivroscomoesteentramem
cena.
Comoaamplaado çãodoASP.NETMVCemtodoomundo,oslivros,comoo
quevocêestásegurando,sãomuitomaisimportantes.OFabrícioeoMárciomon-
taramumexcelenteguiatécnico,quelhedarátodaainformaç ãonecessáriapara
expandirsuacompreensãodoASP.NETMVCbemcomoconceitosmaioresquecer-
camaplataformaASP.NET.Àmedidaqueavan çamosparamelhorunificaraplata-
v

## Página 8

CasadoCódigo
formaASP.NET,vocêcertamentevaiquererterumavisãoclaraeprofundadoque
ASP.NETMVCtemparaoferecer. Euesperoquevocêsedivirtacomvolumede
aprendizadosobreASP.NETqueoesperanestelivro.AproveiteolivrodoFabricio
edoMárcio.
ScottHanselman
Principal Program Manager – Azure and Web T ools
Microsoft Corp.
vi

## Página 9

CasadoCódigo Sumário
Sumário
1 Suaprimeiraaplicaç ão 1
1.1 Eentão,vamoscome çar? . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Códigofonteelistadediscussão . . . . . . . . . . . . . . . . . . . . . . 8
2 Entendendoaestruturadeumaaplicaç ãoASP.NETMVC 9
2.1 ASP.NETMVC?Porquê? . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.2 Voltandoànossaprimeiraaplicação . . . . . . . . . . . . . . . . . . . 12
2.3 Umpoucomaissobreconven ções. . . . . . . . . . . . . . . . . . . . . 13
2.4 Navegaçãobaseadaemrotas . . . . . . . . . . . . . . . . . . . . . . . . 15
2.5 Concluindoedesafiando . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3 Projetandoaaplicaç ão“Cadêmeumédico?” 19
3.1 Cadêmeumédico? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.2 Criandoaaplicação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.3 Referenciandobibliotecas . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.4 Criandoo layoutdaaplicação . . . . . . . . . . . . . . . . . . . . . . . 30
3.5 Concluindoedesafiando . . . . . . . . . . . . . . . . . . . . . . . . . . 39
4 Models:Desenhandoosmodelosdanossaaplicaç ão 41
4.1 Model?! . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
4.2 Abordagensparaacriaçãode Models . . . . . . . . . . . . . . . . . . . 42
4.3 O Entity Framework. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
4.4 Omodeloprimeiro? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.5 Bancodedadosprimeiro? . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.6 ModelfirstxCodefirst:Quandoutilizarumououtro? . . . . . . . . . 69
4.7 Adicionandoatributosdevalidaçãonosmodelos . . . . . . . . . . . . 71
vii

## Página 10

Sumário CasadoCódigo
5 Controllers:Adicionandocomportamentoanossaaplicaç ão 77
5.1 Vamos‘controlar’aaplicação? . . . . . . . . . . . . . . . . . . . . . . . 78
5.2 EntendendoopapeldosControllerseActions . . . . . . . . . . . . . . 79
5.3 Cadêmeumédico:oquefaremos? . . . . . . . . . . . . . . . . . . . . 83
5.4 Cadêmeumédico:CRUDs . . . . . . . . . . . . . . . . . . . . . . . . . 84
6 Views:interagindocomousuário 105
6.1 Visões?! . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
6.2 Conceitode“Engenhoderenderização”. . . . . . . . . . . . . . . . . 106
6.3 ASPXouASP.NETRazor? . . . . . . . . . . . . . . . . . . . . . . . . . 107
6.4 ASP.NETRazor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
6.5 Diferençasnaprática . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
6.6 Helpers?! . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
6.7 Algumasoutrasvantagens . . . . . . . . . . . . . . . . . . . . . . . . . 117
6.8 Mobilidade:Suaconsultademédicosemdispositivosmóveis . . . . . 120
7 Segurança:Criandosuaáreaadministrativa 127
7.1 Áreaadministrativa?! . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
7.2 Criandoaáreaadministrativa . . . . . . . . . . . . . . . . . . . . . . . 128
7.3 Apesardologin,nadaébloqueado.Eagora?! . . . . . . . . . . . . . . 139
7.4 Filtrosdeação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
7.5 Implementandoofiltro‘AutorizacaoDeAcesso’. . . . . . . . . . . . . 139
7.6 Concluindoedesafiando . . . . . . . . . . . . . . . . . . . . . . . . . . 145
8 Publicandosuaaplicaç ão 147
8.1 Pré-requisitosparahospedaraplicaçõesASP.NETMVC4 . . . . . . . 148
8.2 Ambientesdehost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
8.3 Computaçãoemnuvem.Porquê? . . . . . . . . . . . . . . . . . . . . . 150
8.4 OWindowsAzure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
8.5 WindowsAzureWebsites . . . . . . . . . . . . . . . . . . . . . . . . . . 152
8.6 Publicandoaaplicação‘CadêMeuMédico?’. . . . . . . . . . . . . . . 154
8.7 Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
8.8 Códigofonteelistadediscussão . . . . . . . . . . . . . . . . . . . . . . 166
Bibliografia 167
viii

## Página 11

Capítulo1
Suaprimeiraaplicação
Háalgunsanos,aweberaumambientelúdico.Estaafirmaç ãopodeserfacilmente
comprovadaaoidentificarmosoprincipalobjetivodosusuáriosdaqueleperíodo:
“entreter”. Eramuitocomumouvirafirmaçõesdotipo: “Internet? Issoécoisade
desocupadoquenãotemoquefazer!”.Evidentemente,oquefazalgoacontecerde
fatonomercadoéademandae,paraademandadaquelemomento,astecnologias
disponíveis(HTML,JavaScripteumalinguagemdeprogramaç ãodoserver-side)
eramsuficientes. Destacavam-senaquelemomentocomolinguagensserver-side:
PHP,ASP,CGI,Java(Servletseposteriormente,JSP)eoutras.
Otempopassoueainternetdeixoudeserumambienteestritamentevoltado
paraoentretenimentoepassouaserumambientetambémdenegócios.Evidente-
mentequeoperfildousuáriotambémsofreualterações.Ousuárioqueantesaces-
savaumwebsiteapenasparalersuasnotícias(porexemplo),agoraacessavawebsites
tambémparaconsultarpreçosdeprodutos,reservarpassagensaéreas,solicitarorça-
mentosparaserviçosetc.Édesnecessáriomencionaraquiqueumanovademanda
haviasidocriadaeque,oswebsites,passaramatertraçosdeaplicações(porinércia,

## Página 12

1.1. Eentão,vamoscomeçar? CasadoCódigo
commaiorcomplexidadeassociada).
FalandoespecificamentedaMicrosoft,comestanovademandadomercadopor
“aplicaçõesweb”,eisquesurgeem2002oASP.NET,trazendoconsigoomodeloWeb-
Formsdeprogramareestruturaras web apps. Sim,naquelaépocaosWebForms
causaramespanto.Comodesenvolvimentodasaplicaçõestotalmentevoltadopara
amanipulaçãodecomponentesdoladoservidor(TextBox,GridView,DropDown-
List,Labeletc.)eafacilidadedeinje çãodecomportamentosdestesatravésdeseus
eventosproporcionadapeloVisualStudio(arrastaocomponente,duplocliqueno
mesmoeinser çãodecódigonoevento),aMicrosoftarrebanhouumagrandefa-
tiadedesenvolvedores,principalmenteaquelesjáacostumadoscomessemodelo
(“Delphistas”e“VBistas”). Assim,asaplicaçõeswebtornaram-secorporativistas,
fatoestequeagradouomercadoeresultouemumagrandeado çãodaplataforma
tecnológica(a.k.a,.NET).
Jáparaosdesenvolvedoreswebtradicionais,acostumadoscomoamanipula-
çãodiretadoselementosHTML,JavaScriptelinguagensserverside,oASP.NET
WebFormsapresentou-secomoumsercompletamenteestranho,principalmente
pelofatode“tirar”dodesenvolvedorocontroletotaldoselementoscitadosacima.
Ganhava-seemprodutividadeefamiliaridade,entretanto,perdia-seemessência.Na
verdade,paraestes,aimpressãoqueosWebFormscausavamera:“issonãoéweb”.
Olhandoatravésdesteprismaetambémoantigoefuncionalmodelodedesen-
volvimento(propostoparautilizaçãocomalinguagemSmalltalk),omodeloMVC
(Model-View-Controller),aMicrosoftapresentouem2007,àcomunidadetécnica,a
primeiraversãopúblicadeseunovíssimo frameworkparadesenvolvimentodeapli-
caçõesweb,oASP.NETMVC.Naocasiãoemqueestelivrofoiescrito,atecnologia
encontrava-senaversão4.
1.1 Eentão , v amos começar?
Nesteponto,algumasinformaçõesbásicas(masfundamentais,éimportanteobser-
var)necessáriasparaseguircomosestudosacercadomodeloMVCdedesenvolvi-
mentojáseencontramreunidas.Estamosaptos,portanto,asubiroprimeirodegrau
nestainteressanteedivertidaescadadoconhecimento.Criaremos,assim,nossopri-
meiroprojetoASP.NETMVC.
Oquevocêprecisaráparaexecutarosexemplosdestelivro?
Paraseguirosexemplosapresentadosnestelivro,vocêdeverápossuiralgunsele-
2

## Página 13

CasadoCódigo Capítulo1. Suaprimeiraaplicação
mentosdesoftwaredevidamenteinstaladoseconfiguradosemseucomputador.Para
tornaroentendimentomaisclaro,vamossegmentaranecessidadederecursoscon-
formeademandadoexemplo,ok?Alistaaseguir,apresentaosrequisitosnecessários
paraacomposiçãodoprimeiroexemplo:
• MicrosoftVisualStudioExpress2012paraweb(http://bit.ly/mvc-vsexpress);
• NETframework4.5(VisualStudiojáincorporaestainstalação);
• Vocêencontraráumtutorialsobrecomorealizarainstalaçãodestesrecursos
noapêndicedestelivro.
Suaprimeiraaplicação
CriaremosumaaplicaçãoASP.NETMVCsimplesque,evidentemente,exibirá
umamensagemdetexto“Olámundo!” (provavelmenteseriamoshostilizadosse
fossediferente). OobjetivoaquiéapresentaroVisualStudioeasferramentaslá
disponíveisparasetrabalharcomASP.NETMVC.
Já conhece o VisualStudio?
VisualStudio(VS)éaprincipalferramentadaMicrosoftparaode-
senvolvimentodeaplicações. Atualmente,aferramentaencontra-sena
versão2012.VisualStudioéumprodutoecomotal,épago.Entretanto,
aMicrosoftdisponibilizaumaversãogratuita(ExpressWeb),quemuito
emborapossuaumnúmeromaisreduzidoderecursos,traztudooque
precisamosparaconstruiraplicaçõeswebconsistenteseeficientes.
VocêpodeencontrarmaisinformaçõessobreoVisualStudiose-
guindoolink: http://bit.ly/mvc-visualstudio.
ComoVisualStudio2012emexecuç ão,navegueatéaop ção File > New >
Project.Nossainten çãoécriarumanovaaplica çãoparaweb—destaforma,na
janelaqueseapresentará,vocêdeveráselecionardoladoesquerdoaop ção“web”e
nasequência(ladodireito),“ASP.NETMVCWebApplication”.Afigura1.1apresenta
ajanelacomasele çãomencionada.
3

## Página 14

1.1. Eentão,vamoscomeçar? CasadoCódigo
Figura1.1:SelecionandootipodeprojetoASP.NET
Tecnologias utilizadas
ApesardeC# nãoseraúnicalinguagemdisponívelem.NET,elaserá
alinguagemutilizadaemtodososexemplosdesselivro. Osexemplos
tambémutilizarãoaúltimaversãodo.NET,queéo4.5.
Nasequência,vocêprecisaráescolherotipodeprojeto(figura 1.2)ASP.NET
MVCquedesejacriar. Istoporque,acopladoaoVisualStudio,aMicrosoftdispo-
nibilizaalguns templatespré-construídosdeprojetosparaajudá-loaendereçarade-
mandadaaplicaçãoe,claro,ajudá-loa“poupartrabalho”naestruturaçãodoprojeto,
trazendo,porexemplo,pluginsnormalmenteutilizados(jQuery,OData,EntityFra-
meworketc.). Paraaconstruçãodesteprimeiroexemplo,utilizaremosomodelo
Internet Application.
4

## Página 15

CasadoCódigo Capítulo1. Suaprimeiraaplicação
Figura1.2:SelecionandootipodeprojetoASP.NETMVC
Apósacriaçãodoprojeto,vocêveráno“SolutionExplorer”(janelaondeosar-
quivosdoprojetosãodispostos)doseuVisualStudio,umaestruturadeprojetopare-
cidacomaquelaapresentadapelafigura 1.3.Nãosepreocupeagoracomosdetalhes
estruturaisdoprojeto,elesserãoexplicadosemdetalhesnospróximoscapítulos.
5

## Página 16

1.1. Eentão,vamoscomeçar? CasadoCódigo
Figura1.3:Estruturainicialdoprojeto
MuitoemboraoVisualStudiojácrieumaestruturadeprojetofuncional,antes
deexecutaraaplicaçãopelaprimeiravez,faremosumapequenamodificaç ãono
corpodamesma. NoSolutionExplorer,navegueatéoarquivo“HomeController”
( SeuProjeto > Controllers > HomeController). No método Index,
faremos uma alteração simples: modificaremos uma mensagem que é exibida
porpadrão,napáginainicial. Modifiqueotextoatribuídoàpropriedade“View-
Bag.Message”para“MinhaprimeiraaplicaçãocomASP.NETMVC”,conforme
apresentadopelalistagem 1.
Listagem 1.1-Alterandootextodeexibiçãonapáginainicial:
public ActionResult Index()
{
ViewBag.Message = "Minha primeira aplicação com ASP.NET MVC";
return View();
}
6

## Página 17

CasadoCódigo Capítulo1. Suaprimeiraaplicação
Compileoprojeto(vocêpodeutilizarateclaF5comoatalhoparaexecutaresta
tarefa)equandoositeforcarregadoemseunavegador,amensagemqueacabamos
deadicionardeveráserexibida,aexemplodoqueapresentaafigura 1.4.
Figura1.4:Primeiraaplicaçãoemfuncionamento
Parabéns!Vocêacaboudecriare“publicar”(localmente,éclaro),suaprimeira
aplicaçãoASP.NETMVC.
Conformemencionadoanteriormente,vocênãodevesepreocuparnestemo-
mentocomosaspectosarquiteturaisdaaplicaç ão,tampoucocomnomenclaturase
convençõesdecódigo.AideiaaquiémostraravocêumaaplicaçãoASP.NETMVC
funcionando.
Recomendamosqueacompanheatentamentecadatópicodonovocapítulo,uma
vezqueeletrarádetalhespreciososescondidosportrásdeumsimples“Minhapri-
meiraaplicaçãocomASP.NETMVC”.
Desafio:AgoraquevocêjásabecomoésimplescriarumprojetoASP.NETMVC
utilizandooVisualStudio2012,gostariadelan çarumdesafioantesdepartirpara
aleituradopróximocapítulo. Odesafioé: CrieumnovoprojetoASP.NETMVC
7

## Página 18

1.2. Códigofonteelistadediscussão CasadoCódigo
dotipo“InternetApplication”e,nolugardamensagem“Minhaprimeiraaplicação
ASP.NETMVC”,adicioneamensagem“Hojeé:{Dataatual}”e,emseguida,compile
eexecuteoprojeto.
1.2 Código fonte e lista de discussão
Ocódigofotedaaplicaçãoqueestamosconstruindonolivropodeserencontrado
noGitHubatravésdesselinkcurto:
http://bit.ly/mvc-livrocodigofonte
Utilizesemprequenecessárioparareferêncianosestudosecontribuacomocó-
digofonte,façaumforkeaguardamosseupullrequest.
Alémdocódigofonte,temosumgrupodediscussão:
http://bit.ly/mvc-livrogrupodiscussao
ElefoicriadoparaconversarmossobreASP.NETMVCedúvidasreferentesao
livro.Aguardamossuaparticipação
8

## Página 19

Capítulo2
Entendendoaestruturadeuma
aplicaçãoASP.NETMVC
Awebpossuicaracterísticasintrínsecas,quenãopodemserdesconsideradasemhi-
pótesealgumaquandoseplanejamaplicaçõesparaseremexecutadasnesteambiente.
Aspectoscomo:ocorretoeprofundoentendimentodoprotocoloHTTP[4],utili-
zaçãodetecnologiasnativasdosnavegadores(entenda-se,HTML,CSSeJavascript),
responsividade,segurança,desempenhoe,claro, design,devemestarsempreentreas
principaispreocupaçõesdedesenvolvedoreswebe,principalmente,dastecnologias
e frameworkscriadosparageraraplicaçõeseficientesparaestemodelo.
ASP.NETMVCéumatecnologia(framework)quefoiconcebidapararespeitar
taispremissasemais,parafacilitar(sim,facilitar)avidadosdesenvolvedoresquea
utilizam,umavezquesepodeescrevercódigosmaislimpos,livresdedependências
esegmentados(separaçãoderesponsabilidades). Isso,porinércia,noslevaauma
estruturadeaplicaçãomaissaudável,fácildemantereotimizar.

## Página 20

2.1. ASP.NETMVC?Porquê? CasadoCódigo
2.1 ASP.NETMVC?Por quê?
Conformemencionamosnocapítulo 1,pormuitosanos,aMicrosoftapostouem
ummodelodiferentedaqueletradicionalmenteconhecidopordesenvolvedoresweb
(asaber,ASP.NETWebforms). Muitoemboraestaposturatenhacolaboradoem
grandeescalaparaarrebanhardesenvolvedoresdeoutrosuniversosparaodainter-
net,issoacabouporgeraralguns“problemas”nasaplicações,dentreosquaiscita-
mos:
•Dificuldadedemanutenç ão: comooníveldeabstração(automatizaçãode
tarefaseencapsulamentodeconceitos)noASP.NETWebFormséelevado,as
aplicaçõestendemanãoutilizarboaspráticasdedesenvolvimento.Estefato,
nagrandemaioriadasvezes,implicaemumaaplicaç ãomuitocomplexade
sermantida;
•Poucocontrolenageraç ãodoHTML:esteéoutrodosproblemasgerados
pelaautomatizaçãodosprocessos.QuandoseutilizaVisualStudioparacriar
aplicaçõesASP.NETclássicas,muitodoHTMLégeradopelaprópriaIDE(In-
tegrated Development Environment)epeloscontrolesdeservidor(GridView,
ComboBoxetc.).Istoprejudicaotrabalhoentre designersedesenvolvedores;
•Difícildetestar: eisaquiumgrandeproblemaencontradonasaplicações
ASP.NETtradicionais:sãodifíceisdetestar.Note,comASP.NETWebForms,
basicamenteoquefazemosemtermosoperacionaiséarrastarumcompo-
nenteparaaáreadetrabalhoeadicionarumcomportamentoprogramático
aomesmo(via code-behind).Porqueestamosmencionandoisso?Paradizer
queestapráticageraaltoacoplamento,eissoinviabiliza,porexemplo,areali-
zaçãodetestesunitários.Eaplicaçãosemtestenosdiasatuaiséinaceitável.
•PreocupaçãocomoViewState:cadaelementodisponibilizadoemumaapli-
caçãoASP.NETtraziaapossibilidadedeseguardaremvaloresassociadosao
mesmoparaevitar gets/postsdesnecessáriosnoservidor.Estacapacidadeéco-
nhecidanoASP.NETcomo ViewState.Umadasimplicaçõesdautilizaçãonão
criteriosadesterecursoeraoimpactonegativonaperformancedaspáginas;
•Não separação de responsabilidades: não era incomum em projetos
ASP.NETWebFormsencontrarpáginasqueacessavambancosdedados,com-
posiçãodeelementosHTMLatravésdestringsemummétododeexibiç ão,
10

## Página 21

CasadoCódigo Capítulo2. EntendendoaestruturadeumaaplicaçãoASP.NETMVC
validaçõesdeCPFsnoservidoretc.Separarresponsabilidadeseramaisdifícil
etambémgeravaaltoacoplamento.
Você sabe o que é“Alto acoplamento"?
Altoacoplamentoénomedadoàocorrênciadealtograudedepen-
dênciaentrepartesdeumsoftware,sendoqueestaspartesdeveriamfun-
cionardeformaindependente.Complicou?!
Pensenaseguintesituaçãoreal,dodiaadia:Vocêprecisaseconectar
aumbancodedadospararealizarumaatividadequalquer,certo?Para
isso,provavelmentevocêpossuiummétodoquerealizaaconexãocom
obanco. Aconteceque,nointeriordeseumétododeconexão,existea
chamadaparaoutrométodo,sendoqueesteúltimoapenasidentificase
ocorreualgumerroeregistraemumarquivooutabeladelogsdosis-
tema.Assim,sabemosqueexisteumadependênciaexplícitadométodo
deconexãoparacomométododeregistrodelog.Umsópodefuncionar
seooutrofuncionar.
Taldependênciachamamosdeacoplamento. Seestefatoocorrede
formasistemáticanoprojetodesoftware,dizemosqueaaplicaç ãoéfor-
temente/altamenteacoplada.
Valeressaltarqueapontardefeitosnãoédizerquedeterminadatecnologiaé
ruim. OASP.NETWebFormsaindaémuitoutilizado,mas—comotudo—tem
prósecontrase,emalgunscenários,osdefeitosapresentadosporelesãomaiores
queosbenefícios.MesmoutilizandoASP.NETWebFormsépossívelterumdesen-
volvimentoquepermitetestesoubaixoacoplamento,masdevidoàformadetraba-
lhocomatecnologia,oesfor çoparagarantiressesideaiséaltoutilizandoASP.NET
WebForms.
Comoocenáriowebtransformou-serápidaeamplamentenosanosposteriores
(mudançaalavancadaprincipalmentepelosnegócios,quetambémpassaramaser
realizadosnesteambiente),fez-senecessáriaaestruturaç ãodeumanovatecnolo-
giaparadesenvolvimentowebdentrodaplataforma.NET,queatendesseàsnovas
demandasdemercadoequepudesseendere çarosproblemasmencionadosanteri-
ormente.Surgiuentão,oASP.NETMVC.
11

## Página 22

2.2. Voltandoànossaprimeiraaplicação CasadoCódigo
2.2 Voltando à nossa primeira aplicação
Noprimeirocapítulo,criamosumaaplicaçãodeexemplo(éclaroquevocêselembra,
certo?!).Evidentemente,aaplicaçãoàqualnosreferimosésimples,afinaldecontas,
apresentaapenasumamensagempersonalizadanatela,nãoémesmo?
Vocêdeveselembrartambémquenossaaplicaçãoexemplofoicriadabaseada
emummodelo(template)pré-construído,disponibilizadopeloVisualStudio.Esta
escolhanãofoiporacaso.O templateaoqualnosreferimostrazumaestruturade
aplicaçãojáprontaeseguealgumaspráticasinteressantes,asquaisestudaremosa
seguir.
Olhandoparaaestruturadediretórios
Oprimeiroaspectoparaoqualgostariadechamaraaten çãonaaplicaçãode
exemploéaestruturadediretórios(apresentadapelafigura 1.3).
Aprimeiraimportanteconsideraçãoemrelaçãoàestruturadediretóriosapre-
sentadaéque,muitoemborasejaumaestruturafuncionalequeatendaaboaparte
dasaplicaçõesASP.NETMVC,elanãoéestáticae/ouobrigatória. Suaaplicaç ão
podepossuiraestruturadediretóriosqueacharmaisconveniente. Entretanto,
respeitando-seasconven çõesdo frameworkMVC,vocêpoderáencontraralguns
benefícios,osquaisserãovistosdeformamaisdiluídanoscapítulosposteriores.
Convenções?
Paraautomatizaralgumasoperações,oASP.NETMVCutilizaalgu-
masconvenções(notequenãosetratamderegras,masdeboaspráticas
aseremrespeitadas).Sejaparanomesdevariáveis,objetos,classeseaté
mesmodiretórios.
Osdiretóriosmaisimportantesdenossaaplicaç ão(justamenteporestaremin-
corporadosàconven ção)são: Models, Views, Controllers, App_Datae App_Start.
Suasrespectivasfun çõessãoapresentadasaseguir:
•Models: responsávelporagruparosmodelosdedadosqueserãoutilizados
pelaaplicação. Vocêpodeentendercomo“modelodedados”tudoquese
aplicaàexpressão,comoporexemplo: arquivosEDMX(modelosdo Entity
Framework,XML’s,webservices,entidadesdenegócio,DTO’s[(]emportu-
guês,“ObjetodeTransferênciadeDados"]etc.);
12

## Página 23

CasadoCódigo Capítulo2. EntendendoaestruturadeumaaplicaçãoASP.NETMVC
•Views:agrupaoselementosaseremvisualizadospelousuáriofinal(asfamo-
sas views).Nomebemsugestivo,não?!
•Controllers:reúneasclasses(eseusrespectivosmétodos)responsáveispor
definiroscomportamentosdaaplicaçãoaníveldeservidor.Sefacilitar,você
podeentenderestediretóriocomosendoocoraç ãodesuaaplicaçãoweb;
•App_Data:aquioMVCentendequevocêpoderáposicionararquivosaserem
consumidosporseuprojeto,comoimagens,vídeos,áudiosetc;
•App_Start:arquivosqueimplementamcomportamentosespecíficosequede-
vemserinicializadosjuntocomoprojeto,devemserposicionadosnestedire-
tório.
ExisteaindaumdiretórioconvencionadopeloASP.NETMVCquenãoaparece
emnossoprojetoexemploeque,portanto,nãofoiapresentadonalistaanterior.
Trata-sedo App_Code.Elenãoaparecenaestruturadediretóriosdaaplicaç ãoexem-
ploporummotivomuitosimples: elerecebearquivosRazor[3]provenientesde
“Helpers”terceiroseaaplicaçãoexemplonãoimplementaqualquerhelperterceiro.
Falaremosmuitodehelpersduranteoscapítulosposteriores,porisso,jáéim-
portantequevocêsefamiliarizecomestetermo.
2.3 Um pouco mais sobre convenções
ConvençãosobreConfiguração,ousomenteCoC,visasimplificarediminuirasde-
cisõesqueprecisamsertomadaspelodesenvolvedor. Otrabalhoficamuitomais
fácilesimplificadojáquealgumasdecisõesestruturaisedenomessãosugeridosou
atéexigidosemalgunscasos,pelo framework.
Os Controllerse Viewssãoótimosexemplos.
No caso dosControllerstemos um diretório sugerido para a sua criação,
e também temos que respeitar a convenção de que todocontrollerdeve pos-
suirosufixo Controller, ouseja, EmailController, ContatoController,
ClientesControlleretc.
As Viewstambémpossuemumdiretóriodefinido,eoMVCfazusodeumacon-
vençãosimplesparaidentificarourelacionar Viewse Controllers.Nocasodocon-
troller EmailController,umapasta Emailserácriadadentrodapasta Views.
13

## Página 24

2.3. Umpoucomaissobreconven ções CasadoCódigo
Podemosobservaressasconven çõesnaestruturadonossoprimeiroprojeto.
Vejanafigura 2.1oscontrollers HomeController, AccountControllereas
pastas Homee Accountparaas Views.
Figura2.1:ConvençãosobreConfiguraçãononossoprimeiroprojeto
Evidentementequeo frameworkMVCseresponsabilizaporindexarosdiretó-
riosdasolução(nomeatribuídopeloVisualStudioparaoambientequepodeagru-
parumoumúltiplosprojetos),deformacomqueseusrespectivosconteúdossejam
facilmenteacessíveisdequalquerpontodaaplicação.
Comovocêpôdeperceber,emrelaçãoàestruturadediretórios,temosummo-
delobemdefinidoesimplificado.Evidentemente,àmedidaqueformosavan çando,
vocêveráestemodelosendoincrementado. Masistoéassuntoparaospróximos
capítulos.
14

## Página 25

CasadoCódigo Capítulo2. EntendendoaestruturadeumaaplicaçãoASP.NETMVC
2.4 Navegação baseada em rotas
Aaplicaçãocriadanoprimeirocapítuloapresentaoutroaspectofundamentalrelaci-
onadoaomodeloMVCdedesenvolvimento:a navegaçãobaseadaemrotas.Volte
suasatençõesnestemomentoparaafigura 1.4docapítulo1,maisprecisamente,na
barradeendere çosexibidapelonavegador.Notequeoendere çoqueestásendoexi-
bidoéhttp://localhost:1153/.Aperguntaquevocêpodeestarsefazendonesteinstante
é:oqueissotemdemais?
Pararesponderobjetivamenteaestapergunta,convido-lheaconsiderarafigura
2.2.Percebaque,mesmoadicionandonovosparâmetrosàURL,aexibiç ãodocon-
teúdopermaneceinalterada.
Figura2.2:AdicionandoparâmetrosàURL
Nãohánadadeerradocomestecomportamento,muitopelocontrário. Na
verdade, esteéumdosgrandesrecursosimplementadospelo framework. Gra-
çasaummecanismoderoteamentoderequisiçõesconvencionado, oASP.NET
MVC consegue entender que as três diferentes chamadas (http://localhost:1153/
, http://localhost:1153/Homee http://localhost:1153/Home/Index) estão na verdade
fazendo referência ao mesmo recurso. Talvez as perguntas que permeiem sua
mentenesteinstantesão:ondeestáconvencionadoomecanismoderotas?Consigo
visualizar e alterar essa configuração? A resposta direta e definitiva para esta
perguntaésim(vejaalistagem 1).
Listagem 2.1-Visualizandoaconfiguraçãoderotas:
public static void RegisterRoutes(RouteCollection routes)
{
15

## Página 26

2.4. Navegaçãobaseadaemrotas CasadoCódigo
routes.IgnoreRoute("{resource}.axd/{*pathInfo}");
routes.MapRoute(
name: "Default",
url: "{controller}/{action}/{id}",
defaults: new { controller = "Home",
action = "Index",
id = UrlParameter.Optional
}
);
}
Sevocênavegaratéodiretório App_Starteexpandi-loatravésda Solution Ex-
plorerdoprojetodeexemplo,visualizaráalgumasclassesescritasemC#.Todaselas
implementamcomportamentosqueserãoexecutadosnainicializaç ãodaaplicação.
Dentreestesarquivos,encontra-seumchamado RouteConfig.cs.Comumdu-
plocliquesobreomesmovocêpoderávisualizarométodoapresentadopelalistagem
1.
Nocódigoapresentadopelalistagemanterior,ficamclarosdoisaspectosemre-
laçãoaomecanismoderotas.Oprimeirofazmen çãoaofatodequesepoderegistrar
novasepersonalizadasrotas(videonomedométodo RegisterRoutes)parauma
aplicação.OsegundoresidejustamentenofatodequeoASP.NETMVCjátrazcon-
sigoaimplementaçãodeumarotapadrãodenavegaç ãoeéelaquegera,defato,o
comportamentoapresentadopela 2.2.
Note que, para a rota Default ( name: "Default"), temos a atri-
buição do valor Home para o atributo Controller ( controller =
"Home"), do valor Index para o atributo Action ( action = "Index")
e do valor UrlParameter.Optional para o atributo id ( id =
UrlParameter.Optional).
Seligarmosospontos,concluiremosquearotaapresentadapornossaaplicaç ão
deexemplo(vernovamentefigura 2.2)atendeaopadrãodefinidopelo framework.
Vejaacomparação,padrãoimplementado:
controller = "Home", action = "Index", id = UrlParameter.Optional
VerifiqueaURLdenossaaplicaçãodeexemplo:
http://localhost:1153/Home/Index
Ousimplesmente:
16

## Página 27

CasadoCódigo Capítulo2. EntendendoaestruturadeumaaplicaçãoASP.NETMVC
http://localhost:1153/
Valelembrarmaisumavezque Homee Indexsãovalorespadrãonarotapa-
drãodoASP.NETMVC.Opcionalmente,seriapossíveladicionaràURLumva-
lorchaveparaidentificaralgumobjeto. Destaforma,poderíamosteralgocomo
http://localhost:1153/Home/Index/200porexemplo.Entretanto,muitoemborasejapos-
sívelrealizartaladição,nocasodoexemplodiscutidonãofazsentidofazê-lo,pois
nãoestamosidentificandodeformaunitáriaalgumelemento(como http://localhost:
1153/Clientes/Perfil/18556).Porestemotivo,oúltimoparâmetrodarotapadrãoéde-
finidocomoopcional( id = UrlParameter.Optional).
Afigura2.3apresentaumesquemafuncionalqueilustra(deformasimplificada)
omecanismoderoteamentoimplementadopeloASP.NETMVC.
Figura2.3:EsquemadomecanismoderotasdoASP.NETMVC
Modeloderoteamentoquegera“URLssemânticas"
ConsidereaseguinteURL: http://seusite.com/Conteudo.aspx?id=987511. A
perguntaaserrealizadaaquié:éfácilmemorizarumaURLcomoesta?Aresposta,
evidentemente,énão.
URLscomoessaapresentadanoparágrafoanteriorsãogeradasautomaticamente
pelossistemaswebparafazerreferênciadeformadinâmicaaosconteúdosdaapli-
cação. Muitoemboranãohajaqualquerproblematécnico(istoé,estaURLfunci-
onaperfeitamente)relacionadoaestetipodeURL,sepensarmosnaexperiênciado
17

## Página 28

2.5. Concluindoedesafiando CasadoCódigo
usuáriofinalaointeragircomela,poderemosencontraralgunsproblemas,dentreos
quaissedestacam:dificuldadedememorizaçãoebaixalegibilidade.
Alémdisso,éimportanteobservaroimpactonegativodestasURLsnastécnicas
de Search Engine Optimization(SEO)[2].Notequeosprincipaisrobôsdeindexa-
çãodeconteúdosdesitesdebusca(Google,Bingetc.),desconsideramURLsque
apresentamalgunscaracteresespeciais,taiscomo: &, @, %etc.
Levando-seemconsideraçãoestesaspectos,ASP.NETMVCimplementaatravés
domecanismoderotasomodelodeURLsamigáveis. Assim,alémtornaraURL
daaplicação indexávelparaosrobôsdebusca,o frameworkmelhoraaexperiência
navegaçãodousuário,umavezqueébemmaisfácildeinteragircomumaURLcomo
http://seusite.com/Conteudos/Artigos/987511.
2.5 Concluindo e desafiando
Entenderaestruturadediretórios,asconven çõesutilizadaspelo frameworkMVC
eomodeloderoteamento,édefundamentalimportânciaparaprojetaraplicações
ASP.NETMVCqueusufruamdopoderdaplataformaemsuaplenitude. Nopró-
ximocapítulo,vocêseráinseridonoprocessodeplanejamentodeumanovaaplica-
çãoASP.NETMVC.Estaaplicaçãoseráutilizadadurantetodoolivroparaapresentar
osdemaisconceitoserecursosdaplataforma.
Nestepontovocêjápossuiinsumossuficientesparaseguiratravésdospróximos
capítulos. Nossapreocupaçãoaquifazercomqueoconhecimentosejaconstruído
evolutivamente,poucoapouco.
Desafio:Imaginequevocêpreciseadicionarum pluginjQuerypararealizaral-
gumatarefaespecífica.Levando-seemconsideraçãoaconven çãodoASP.NETMVC
eaestruturadediretóriospropostapelaaplicaç ãoexemplo,adicioneosarquivosdo
mesmoemseusrespectivoslugaresnoprojeto. Dica: Contentnãoestálápor
acaso.
18

## Página 29

Capítulo3
Projetandoaaplicação“Cadêmeu
médico?”
Nosprimeiroscapítulosdestelivro,vocêfoiapresentadoaosconceitosiniciaisrelaci-
onadosao frameworkASP.NETMVC.Alémdisso,vocêcriousuaprimeiraaplicação
MVCque,muitoemboratenhasidoextremamentesimples,estevecompletamente
funcional.
Apesardebásicos,osconceitosapresentadosatéaquisãodefundamentalim-
portânciaparaodesenvolvimentodeaplicaçõesutilizandoASP.NETMVC.Daqui
pordiante,nãosóutilizaremososconceitosjávistos,comoiremosconhecernovos.
Issoserárealizadoàmedidaqueavan çamosnacriaçãodeumaaplicaçãofictícia,
chamada“Cadêmeumédico?”.
Nospróximoscapítulos,avan çaremosnodesenvolvimentodaaplicação“Cadê
meumédico?”.Vocêseráguiadonãoapenaspelosdetalhesdaaplicação,comoatra-
vésdenovosrecursosdoASP.NETMVC.Apresentaremostambémdicasetruques
quepodemfacilitaremgrandeescalaotrabalhoaoutilizar Models, Viewse Control-

## Página 30

3.1. Cadêmeumédico? CasadoCódigo
lers.
Assimcomoagrandemaioriadasaplicaçõesdomundoreal,vamosconstruir
passoapassoumaáreaadministrativaparanossaaplicaç ão,afinaldecontas,preci-
samossaberquemestáinserindoinformaçõesemnossabasededados—e,claro,
precisamosdeseguran ça.Aoprojetaraaplicação,levaremosemconsideraçãotam-
bémaspectoscomoautilizaçãoemdispositivosmóveis,boaspráticasdeprograma-
çãoe design.
3.1 Cadê meu médico?
Quemnuncaprecisoudescobrirquaissãoosmédicosdedeterminadaespecialidade
disponíveisemsuacidade?“Cadêmeumédico?”implementajustamenteestaideia.
Deformarápidaefácil,osusuáriospoderãorealizarconsultassimplesaosmédicos
disponíveisdeformasegmentadaporespecialidade.
Paraqueapesquisafuncionedeformasatisfatória,médicoseespecialidadesde-
verão,evidentemente,sercadastradosnosistemaeemfun çãodisso,construiremos
um backendcomtodososcadastrosnecessários(oquejáapresentaráumasériede
novosconceitos).
Assim,osseguintesrecursosserãoimplementados:
•Áreaadministrativadaaplicaç ão:áreadeacessorestrito,ondeosusuários
precisarãorealizaroprocessodeautenticaçãoparaterodevidoacesso.Além
domecanismode login,dentrodaáreaadministrativaserãoimplementados
todososcadastros(médicos,especialidades,cidadeseusuários);
•Gerenciamentodemédicos:acopladaàáreaadministrativacriaremosuma
subáreaparaCRUD(Create, Read, Updatee Delete)denovosmédicos;
•Gerenciamentodeespecialidadesmédicas:tambémacopladaàáreaadmi-
nistrativa,serácriadaumasubáreaparaCRUDdeespecialidadesmédicas;
•Páginapúblicaparaconsultademédicosporespecialidade:criaremosuma
páginapública,ondedisponibilizaremososrecursosnecessáriosparaquea
consultademédicospossaserrealizada;
•Versãodositeparadispositivosmóveis: conformemencionadoanterior-
mente,temosapreocupaçãodequenossaaplicaçãopossuaumaexperiência
adequadaparadispositivosmóveis.Destaforma,criaremosumanovapágina
20

## Página 31

CasadoCódigo Capítulo3. Projetandoaaplicação“Cadêmeumédico?”
(tambémpública)deconsultaaosmédicosmas,destavez,voltadaparadis-
positivosmóveis.
Paraqueapropostadaaplicaç ão“Cadêmeumédico?”torne-semaisclarasob
ospontosdevistafuncionalearquitetural,apresentamosalgunsdetalhesacercada
mesma.Assim,convidamosaconsiderarafigura 3.1.
Figura3.1:Visãogeraldaaplicação‘Cadêmeumédico?’
Alémdavisualizaçãodaestrutura,nestemomento,umesfor çoadicionalsefaz
necessário.Trata-sedaconstruçãoeposteriorapresentaçãodeumdiagramadeen-
tidadeseseusrespectivosrelacionamentos.Evidentemente,aorealizarmostalope-
ração,jáestamospensandonaestruturafinaldebancodedadosdenossaaplicaç ão.
A figura3.2 apresenta o DER (Diagrama Entidade-Relacionamento) pro-
posto.Parachegarmosaestemodelo,estamosconsiderandoalgumasregrasdene-
gócioparaosistema.Sãoasprincipais:
21

## Página 32

3.1. Cadêmeumédico? CasadoCódigo
• Ummédicodevepossuirumaespecialidademédica;
• Umaespecialidademédicapodeestarassociadaadiferentesmédicos;
• Ummédicopoderáestarassociadoapenasaumacidade;
• Umacidadepodepossuirdiversosmédicos;
• Osistemadeverácontrolaroacessodeusuáriosaosistemaadministrativo.
Diagrama Entidade-R elacionamento?
DiagramaEntidade-Relacionamento(ousimplesmenteDER)éuma
metodologiaquepermitecriar,eposteriormenteexibir,deformagrá-
ficaesimplificada—níveldeabstraçãomaisalto—umaestruturamais
complexaderegraseagrupamentodedadosemumaaplicaç ão.
AtravésdarepresentaçãográficasimplespossibilitadapelosDER’s,é
possívelentenderalógicadedadose,atémesmo,algumcomportamento
daaplicação. Alémdisso,osdiagramasexpressamosrelacionamentos
entreasentidadesimportantesparaosistema,oquefacilitaoentendi-
mentodasituaçãoproblemaeposteriorimplementação,tantoparade-
senvolvedoresquantoparaadministradoresdebancosdedados.
Resumindo:Trata-sedo“mapa”geradopelosanalistasderequisitos
epassadoparaosdesenvolvedores,arquitetosdesoftwareeadministra-
doresdebancosdedados.
22

## Página 33

CasadoCódigo Capítulo3. Projetandoaaplicação“Cadêmeumédico?”
Figura3.2:DERparaaaplicação‘Cadêmeumédico?’
Sãolegendasparaafigura 3.2:
• [PK]:éoacrônimoparaPrimary Key.Emportuguês,“ChavePrimária";
• [FK]:éoacrônimoparaForeign Key.Emportuguês,“ChaveEstrangeira";
• [PFK]:éoacrônimoparaPrimary Foreign Key.Emportuguês,“ChavePrimá-
riaeEstrangeira";
• Nasequência,vocêpodevisualizarasentidadesparticipantesdomodelo(Mé-
dicos,Especialidadesetc.)
3.2 Criando a aplicação
Agorajásabemostudooqueprecisamos,portanto,éhoradecome çaracriarefetiva-
menteaaplicaçãoCadêmeumédico?.ComoVisualStudioemexecução,navegue
23

## Página 34

3.2. Criandoaaplicação CasadoCódigo
atéomenusuperioreláselecioneaop ção File > New > Project.Najanelaque
seapresentará,selecioneàesquerdaaop ção“web”enasequência,aopção“ASP.NET
MVCApplication”àdireita.Afigura3.3apresentaasele çãoaqualnosreferimos.
Figura3.3:SelecionandootipodeprojetoASP.NET
Istofeito,umanovajanelaseráapresentadapeloVisualStudio.Elaexibealguns
templatesdisponíveisparaacriaçãodeumaaplicaçãoASP.NETMVC.Vocêdevese
lembrarqueemnossaprimeiraaplicaçãodeexemplo,escolhemoso template“Inter-
net Application”.Comoresultadodestaescolha,oVisualStudiocriaumaestrutura
baseeadicionaváriasreferênciasaoprojeto,alémdedefinirumlayoutpadrão.
Paraestesegundoemaiscompletoexemplo,vamosutilizaro template blank,
atravésdoqualoVisualStudiocriaapenasaestruturabásicadediretórios,eadiciona
oscódigosdeinicializaçãodaaplicação(comoaconfiguraçãodoroteamentopadrão,
porexemplo).Afigura 3.4mostraasele çãomencionada.
24

## Página 35

CasadoCódigo Capítulo3. Projetandoaaplicação“Cadêmeumédico?”
Figura3.4:Selecionandootemplatedoprojeto
Utilizandoo templatebásico,temosalgumtrabalhoparacriaro layout,adicionar
referênciasetc.Muitoemboraestejamosconscientesemrelaçãoaestefato,istoestá
sendofeitopropositalmente,umavezqueserviráparaapresentartruqueseexaltar
ferramentasdoVisualStudioquenosauxiliamnaconstruç ãodasaplicações. Vale
lembrarquequandocome çamosumprojeto,nemsemprepodemosutilizaro layout
ebibliotecasqueaferramentasugere.Porissooconhecimentoparacriarumaapli-
caçãodesdeoinícioéimportante!
Apósacriaçãodoprojeto,aestruturadediretóriosapresentadano Solution Ex-
plorerdeverásersemelhanteàapresentadapelafigura 3.5.
25

## Página 36

3.3. Referenciandobibliotecas CasadoCódigo
Figura3.5:EstruturainicialdaaplicaçãoCadêmeuMédico?
3.3 Referenciando bibliotecas
Nodesenvolvimentodequalqueraplicação,webounão,écomumautilizaç ãode
bibliotecasjáprontasqueencapsulamtarefasespecíficasequeauxiliamnodesen-
volvimento. Entreosbenefíciosproporcionadosporestaprática,podemoscitara
produtividadeeoreaproveitamentodecódigo.ComaplicaçõesASP.NETMVCnão
édiferentee,porisso,vocêveráaolongodaconstruç ãodesteprojeto,aadiçãode
váriasreferênciasquefacilitarãoemgrandeescalaarealizaçãodedeterminadasta-
refas.
Quandocriamosnossaprimeiraaplicaçãodeexemplo(vercapítulo 1)eescolhe-
moso template“Internet Application”,vimosoVisualStudiocriarumlayoutpadrão
paraaaplicaçãoetambémadicionar,deformaautomática,referênciasaváriasbibli-
otecasjavascript.Alémdisso,bibliotecasparaquealgunsrecursosnativosdo tem-
platepadrãopudessemfuncionardeformaadequada(autenticaç ãodeusuários,por
exemplo)foramadicionadas.Mencionamosissoapenasparaesclarecerquetraba-
lharcombibliotecasemprojetosASP.NETMVCénormalevocêdeve,sempreque
26

## Página 37

CasadoCódigo Capítulo3. Projetandoaaplicação“Cadêmeumédico?”
necessário,sevalerdestaop ção.
Comoestamosoptandopelautilizaçãodo template“Empty”paracriaraaplica-
çãoCadêmeumédico?,precisaremosadicionarmanualmentetodasasreferências
àsbibliotecasnecessárias.Alémdisso,nãotemosum layoutpré-construído,oque
nosforçaráacriaronossopróprio.
Paraquepossamoscriarumbomníveldeinteratividadeentreousuáriofinale
aaplicaçãoCadêmeumédico?,utilizaremosumconhecido frameworkjavascript,a
saber,jQuery.Paranosauxiliarnacriaç ãodo layoutdaaplicação,utilizaremosum
excelentecomponentedeelementosgráficosqueéamplamentedifundidoeutilizado
emprojetoswebequeédisponibilizadogratuitamentepelotimededesignersdo
Twitter—oBootstrap.
•jQuery:éumadasmaisfamosasefuncionaisbibliotecasbaseadasemjavas-
criptdomundo.Facilitaotrabalhoemanipulaç ãodosobjetosDOM(Docu-
ment Object Model),chamadasAjax,manipulaçãodeeventoseanimações;
•TwitterBootstrap:trata-sedeumabibliotecadeCSS(Cascading Style-Sheet )
ecomponentesjQueryquefacilitaotrabalhodeestruturaroucriarnovos
layoutsparaaplicações;
Encontrareutilizarbibliotecasúteisnosprojetospodeserumatarefacomplexa,
tendoemvistaaenorme“oferta”debibliotecasparasolucionarosmesmostipose
classesdeproblemas.Assim,éprecisoestaratentoparaescolheraquelaquemelhor
atendeàsnecessidadesdoprojeto.Alémdisso,existemoutrosaspectosqueacabam
gerandoproblemasnogerenciamentodebibliotecas:instalação,atualização,depen-
dênciasetc.
Aboanotíciaéqueosproblemasmencionadosanteriormentenãoexistemmais
sevocêéusuáriodoVisualStudio. Issograçasaumaferramentaintroduzidapela
MicrosoftnoVisualStudio2010comsuporteaoASP.NETMVCapartirdaversão
3,chamada NuGet.Alistaaseguirapresentaalgunsdosbenefíciosproporcionados
pelo NuGet.
•Repositóriodebibliotecas:oNuGetpossuiumrepositóriooficialondequal-
querbibliotecapodesercadastradaedisponibilizada.Todapesquisaéreali-
zadanesserepositóriopúblico;
•Ranking:quandoumapesquisaérealizada,asbibliotecassãoordenadaspelo
númerode downloadsrealizados.Logo,osmaisbaixadosaparecemnotopo
dalista;
27

## Página 38

3.3. Referenciandobibliotecas CasadoCódigo
•Instalação: asresponsabilidadesde downloadeinstalaçãosãodo NuGet.
Comousuários,precisamosinformarapenasqualoprojetonoqualabibli-
otecadeveserinstalada;
•Atualização:quandoumabibliotecaéatualizadanorepositóriooficialdo Nu-
Get,elaentranalistadebibliotecasquepodemseratualizadasnoseuprojeto.
Issoémuitoútiljáque,paraamaioriadasbibliotecas,asversõescomcorre-
çõesemelhoriasdedesempenhosãoliberadasfrequentemente;
•Dependências:imaginequevocêprecisadabiblioteca A,masparafuncionar
eladependeda B—aautomatizaçãodo downloadeinstalaçãodasdependên-
ciastambéméfeitaautomaticamentepelo NuGet.
Aprincípio,o NuGetnosajudaránosprocessosdeinstalaçãodojQueryedo
TwitterBootstrap. Paraisso,navegueatéomenu Tools > Library Package
Manager > Manage NuGet Packages for Solution.Najanelaqueseapre-
sentará, selecione do lado esquerdo a opção OnLine:> NuGet official
package source,enocantosuperiordireitopesquisepor jQuery.Nocentroda
janelaserãoapresentadososresultadosdapesquisa.Noitem jQuerycliquenobotão
Install.Afigura 3.6ilustraesteprocesso.
Aoclicarnobotão Install,umajanelaseráapresentadacomosprojetosdanossa
solução.Escolhaoprojetonoqualabibliotecadeveráserinstalada,conformeilustra
afigura3.7.
Figura3.6:PesquisandoeinstalandojQuerycomoNuGet
28

## Página 39

CasadoCódigo Capítulo3. Projetandoaaplicação“Cadêmeumédico?”
Figura3.7:DefinindoemqualprojetooNuGetiráinstalarabiblioteca
Agoraquejátemoso jQuerydevidamenteinstaladoemnossoprojeto,realiza-
remosomesmoprocedimentoparaoTwitterBootstrap.Pesquisepor“Bootstrap”e
nasequência,efetuesuainstalação.Afigura 3.8ilustraesteprocesso.Estamosutili-
zandoaversão3.0.0.0doBootstrap,queéaúltimaversãolan çadaatéapublicação
desselivro.Casosuapesquisaretorneumaversãosuperior,fiqueatentoaositeoficial
porpossívelguiasdemigraçãodeumaversãoparaoutra.
Figura3.8:PesquisandoeinstalandoTwitterBootstrapcomoNuGet
Épertinenteobservarnestepontoofatodeque,parainstalarasbibliotecasne-
cessáriasaonossoprojetoviaNuGet,estamosutilizandoaferramentagráficadispo-
nibilizadapeloVisualStudioparaestefim.Muitoemboratalferramentasejafun-
cionaleatendaàsnecessidades,valemencionarqueestanãoéaúnicaformade
trabalhodisponível. Desenvolvedoresquepossuempreferênciaportrabalharcom
linhasdecomandotambémsãoatendidospeloVisualStudio.Issoéfeitoatravésda
ferramenta Package Manager Console,acessívelatravésdomenusuperiornaop ção
Library Package Manager.
Aoacessaraop çãomencionada,oVisualStudioapresentaráum consolenoqual
oscomandospoderãoserdigitados.Vocêpoderáfazerpraticamentequalquerope-
29

## Página 40

3.4. Criandoolayoutdaaplicação CasadoCódigo
raçãocomNuGetvialinhadecomandos. A“linguagem”aceitapeloNuGetpara
os inputsdecomandoséo PowerShell.Vocêpodeencontrarumguiadereferência
completosobreoscomandosaceitospeloNuGetvia PowerShellseguindoolink:
http://bit.ly/referenciapowershell
Parasabermaissobreo PowerShell,vocêdevepodeutilizar:
http://bit.ly/guiapowershell
3.4 Criando o layout da aplicação
Nossoprojetojáseencontracriadoesuasrespectivasbibliotecasiniciais(indispen-
sáveisparainiciaraconstruçãodenossaaplicação)jáestãoreferenciadas.Estamos
aptos,portanto,aavan çaremnossoprojeto.Iniciaremospelapartevisualpoisatra-
vésdelatiraremosliçõespreciosasacercado frameworkASP.NETMVC.
Ositensanterioresdestecapítuloapresentaramacriaç ãodoprojetoeomodelo
dereferenciamentovia NuGet.Comopróximaetapa,precisamostestarseareferên-
ciaestáfuncionandodeformaadequada.Paraisso,vamoscriarum layoutinicial-
mentedetesteeclaro,nasequência,iremosincrementá-lo.Assim,alémdevalidar-
mosofuncionamentodasbibliotecas,definimostambémaestruturabásicadetoda
aaplicação.
Muitoemboratenhamosnofuturoumcapítulodedicadoespecificamentepara
tratardoassunto“views”,construiremosagoraalgumasdelas,queservirãodebase
paranossoaplicativo. Éimportantenotarqueoobjetivonãoéapresentardeta-
lhessobre views,massim,sobreoprocessodeestruturaç ãodeum layoututilizando
ASP.NETMVC.
Tambémutilizaremosalgumasfun çõesdoASP.NET Razor,queéomotorde
renderizaçãodaspáginascriadascomo ASP .NET MVC.Masnãosepreocupecom
issonestemomento.Nocapítulo9vocêseráguiadotambémpelosdetalhesacerca
do Razor.
Umdosmuitosconceitosinteressantesintroduzidospelo ASP .NETfoiode Mas-
ter Pages(páginasmestras).Atravésdasfamosas master pages,conseguimosreapro-
veitarmuitodo layoutqueécomumaosite.Porexemplo,nãoprecisamosconstruir
omenuemcadapáginadosite.Aoinvésdisso,podemoscolocaromenuemuma
:master pagee“dizer”aoASP.NETquetodasaspáginasqueherdamosestilosde
determinadapáginamestradevemexibiromesmomenu.Deigualforma,estatéc-
nicapoderiaserutilizadaparaestruturarquaisquerconteúdosdepropósitosgerais,
permitindoassimamanuten çãodofoconoconteúdoespecíficodapáginacorrente.
30

## Página 41

CasadoCódigo Capítulo3. Projetandoaaplicação“Cadêmeumédico?”
Omodelodetrabalhocom master pagesoferecidopeloASP.NETMVCéligeira-
mentediferentedaqueleproporcionadopelos web forms.Vocêpodeencontrarum
bomtextodereferênciaacercadautilizaçãode master pagescom web formsseguindo
olinkapresentadopelareferência[5].
Muitoemboraasabordagenssejamdiferentes,oconceitoérigorosamenteo
mesmoeiremosutilizá-loamplamenteemnossoprojeto. Assim,na Solution Ex-
plorer,cliquecomobotãodireitodomousenapasta Viewsenaveguepelasop ções
Add > View.Afigura 3.9ilustraesteprocesso.
Figura3.9:CriandoumanovaView
Nasequência,umajanelaondeiremosinformarmaisdetalhesacercadenossa
Viewseráapresentada.Informeonome Layout,edesmarqueaop ção Use a layout
or master page.Essaop çãoéjustamenteaquevamosmarcarnacriaç ãodealguma
ViewqueiráutilizarnossaMasterPage.Feitoisso,cliquenobotão Ok.Afigura 3.10
mostraessaetapa.
31

## Página 42

3.4. Criandoolayoutdaaplicação CasadoCódigo
Figura3.10:CriandoumanovaView
Apósacriaçãodoarquivo,oVisualStudiovaiabriranossaViewparaediç ão.
Vocêdeveráverumcódigoparecidocomocódigodalistagem 1.
Listagem 3.1-Códigoinicialdamasterpage:
@{
Layout = null;
}
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>Layout2</title>
</head>
<body>
<div>
32

## Página 43

CasadoCódigo Capítulo3. Projetandoaaplicação“Cadêmeumédico?”
</div>
</body>
</html>
AntesdemodificaroHTMLgeradopeloVisualStudioparaa master page,é
precisonotarumaspectoimportante.Noteque,noiníciodocódigo,àpropriedade
“Layout”éatribuídoovalor“null”.Poiséjustamenteestaapropriedadequerecebe
aindicaçãodo layoutpadrão,ouseja,a master pagedaqualapáginaherdará.
Precisamosconcordar,nesteponto,queexecutartalatribuiç ãoemtodasaspá-
ginasdeumaaplicaçãonãoélámuitoprodutivo.Imagineumprojetogrande,com
muitas views.Estapráticatornariaonerosasdemaistantoaimplementaç ãoquanto
amanutençãodosarquivosde layoutdoprojetonocasodeumapossíveltrocade
master page.Alémdisso,saltaàvistaaausênciadoconceitodereutilizaç ãodecó-
digo.
Oquefaremosagoraécriarumanova viewqueseráresponsávelpordefiniressa
propriedadeemtodasas viewsdanossaaplicação. Paraisso,novamenteváatéa
Solution Explorer,cliquecomobotãodireitodomousenapasta Viewsenavegue
pelasopçõesAdd > View.Afigura 3.11ilustraesteprocesso.
Figura3.11:CriandoumanovaView
Agora,najanelaondeinformaremososdetalhesacercadenossanova view,uti-
lizaremosonome _ViewStart.Aindanestajanela,desmarquetambémaop ção
Use a layout or Master Page,ecliqueem Ok.
Noteque,novamente,a Convenção sobre Configuraçãonosajudanestecaso.Por
quê? Umaviewchamada _ViewStartseráexecutadanoiníciodarenderização
de todas asviews da aplicação. Voltando à configuração, vamos configurar a
propriedade Layoutnanossa _ViewStart,conformeapresentaalistagem 2.
Listagem 3.2-Propriedadequedefineamasterpage:
@{
33

## Página 44

3.4. Criandoolayoutdaaplicação CasadoCódigo
Layout = "~/Views/Layout.cshtml";
}
Podemos voltar agora e definir a estrutura padrão delayout da aplicação
no arquivo “Layout.cshtml”. Já utilizamos um pouco deRazor na criação da
_ViewStarteagorairemosavan çarumpoucomais. Alistagem 3apresentao
layoutpadrãodanossaaplicação.
Listagem 3.3-Layoutpadrãodaaplicação:
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta name="viewport" content="width=device-width" />
<title>Cade meu medico? - @ViewBag.Title</title>
<link href="@Url.Content("~/Content/bootstrap/bootstrap.min.css")"
rel="stylesheet" />
<style>
body {
padding-top: 60px;
}
</style>
</head>
<body>
<div class="navbar navbar-inverse navbar-fixed-top">
<div class="container">
<div class="navbar-header">
<a class="navbar-brand" href="#">Cade meu medico?</a>
</div>
<div class="collapse navbar-collapse">
<ul class="nav navbar-nav">
<li class="active"><a href="#">Home</a></li>
<li id="menuPaises">
@Html.ActionLink("Países", "Index", "Paises")
</li>
</ul>
</div>
</div>
</div>
<div class="container">
34

## Página 45

CasadoCódigo Capítulo3. Projetandoaaplicação“Cadêmeumédico?”
@RenderBody()
</div>
<script src="@Url.Content("~/Scripts/jquery-2.0.2.min .js")">
</script>
<script src="@Url.Content("~/Scripts/bootstrap.min.js")">
</script>
@RenderSection("script", required: false);
</body>
</html>
Alémdebásico,oHTMLdenossaestruturacontémareferênciaàsbibliotecas
deCSSeJavaScriptqueutilizaremosnaaplicaç ão.Alémdisso,vocêdeveternotado
queemalgunspontosutilizamosocaractere "@”.Poissaibaqueéexatamentenestes
pontosqueestamosutilizandooASP.NET Razor.
Outro aspecto a ser notado reside na definição do título das páginas de
nossa aplicação. Estamos concatenando o texto “Cadê meu médico?” com
"@ViewBag.Title".Comovocêdeveselembrar,quandopersonalizamosamen-
sagemdanossaprimeiraaplicação,utilizamosapropriedade ViewBagparaenviar
nossamensagemparaa view.Agoraestamosutilizandonovamentea ViewBag,mas
paramostrarnaspáginasosvalorespredefinidos.
O Razorpossuiumagrandequantidadedemétodosqueauxiliamos desenvol-
vedoresemgrandeescalanoprocessodeconstruç ãodeaplicações. Umdeleséo
"@Url.Content()”,queconverteumdiretóriovirtualrelativoparaumdiretórioab-
solutonaaplicação.Atravésdisso,podemosvincularnossosarquivos.csse.js(por
exemplo)semnospreocuparmoscomaestruturadepublicaç ãodaaplicaçãonoIIS
(Internet Information Services).
Lembre-sequetodasaspaginasirãoutilizaro layoutpadrão,portanto,nãopreci-
samosrepetiralgunscódigoscomuns,maséprecisodefiniremnosso layoutondeo
códigodaspáginasserárenderizadoemnosso layoutpadrão.Éissoqueestamosfa-
zendoaoutilizarmosométodo "@RenderBody()”doASP.NET Razor.Quandouma
viewforrenderizada,seucódigoseráadicionadonaquelepontodapáginaHTML.
Umoutrotruquemuitointeressantedo Razorsãoas Sections. Atravésdelas,
podemosdefinirse çõesondedeterminadoscódigosserãorenderizados.Asfuturas
viewsdenossaaplicaçãopossuirãocódigoJavaScriptpróprio,eelesprecisamserren-
derizadosapósadefiniçãodasbibliotecasJavaScriptqueestamosutilizando.Desta
forma,como @RenderSection("script", required:false),criamosuma
35

## Página 46

3.4. Criandoolayoutdaaplicação CasadoCódigo
seçãoondeosscriptsserãorenderizados. Comonemtodapáginapossuiráalgum
script,essase çãonãoéobrigatóriaeporisso,utilizamoso "required:false”.
Layoutpadrãocriado,éhoraentãodetestaromesmocomumapáginadeteste
emnossaaplicação.Na Solution Explorer,cliquecomobotãodireitonapasta Con-
trollersenavegueatéasop çõesAdd > Controller.Afigura 3.12ilustraestepro-
cesso.
Figura3.12:AdicionandoumnovoController
Najanelaqueseráexibidaaseguir,definaonomedo controllercomo“Teste-
LayoutController”.Lembre-se,todocontrollerdevepossuirosufixoController(mais
umavezoCoCatuando).Afigura 3.13representaisso.
Figura3.13:AdicionandoumnovoController
Apósexecutarmosacriaçãodo controller,oVisualStudioabriráocódigodo
36

## Página 47

CasadoCódigo Capítulo3. Projetandoaaplicação“Cadêmeumédico?”
arquivo.Evidentemente,eledeveráseparecercomocódigodalistagem 4.
Listagem 3.4-Controllerdotestedolayout:
public class TesteLayoutController : Controller
{
public ActionResult Index()
{
return View();
}
}
Opróximopassoconsistirádacriaçãodeumanova view,queseráapresentada
quandoométodo Actiondo Controllerforchamado. RecordequeumadasCon-
vençõessobreConfiguraçãoéquea viewdeveráficaremumapastacomonome
do Controller,ea Viewdeveráteronomeda Action. FelizmenteoVisualStudio
automatizaessetrabalho!
Maisumavezéimportanteobservarquevocênãodeveestartãopreocupadose
estiverachandoestranhoostermos Controller, Actionetc. Elesserãoapresentados
deformadetalhadanoscapítulosaseguir.
Cliquecomobotãodireitodomousesobreocódigo View()enavegueatéa
opção Add View.Afigura 3.14ilustraesteprocesso.
Figura3.14:AdicionandoumanovaView
Najanelaqueseráapresentada,vocêpoderánotarqueonomeda viewjáestará
definido,eseaop ção "Use a layout or master page”nãoestiverselecionada,vocêdeve
fazê-lo.Nãoinformenenhumvalornocampo.Comocampoembranco,oMVCvai
usarporpadrãooarquivocriadoanteriormente(asaber, _ViewStart).Afigura
3.15mostraessaetapa.
37

## Página 48

3.4. Criandoolayoutdaaplicação CasadoCódigo
Figura3.15:AdicionandoumanovaView
Apósacriaçãodoarquivo, oVisualStudioabriráocódigoeeledeveestar
parecidocomalistagem 5.Reparequepodemosalterarnaprópria viewovalordo
ViewBag.Title,queseráconcatenadocomotítulodaspáginas. Altereovalor
para "T este de layout”
Listagem 3.5-Códigodaviewdetestedolayout:
@{
ViewBag.Title = "Teste de layout";
}
<h2>Index</h2>
Feitoisso,compileseuprojeto,atravésdopressionardatecla F5noVisualStu-
dio.Quandooaplicativoforcarregado,provavelmenteumapáginadeerroserámos-
38

## Página 49

CasadoCódigo Capítulo3. Projetandoaaplicação“Cadêmeumédico?”
trada,jáquenãodefinimosumControllerpadrão.Mastudobem,istoéproposital.
DigiteaofinaldaURLafraç ãode string“/testelayout”quenossapáginadeteste
seráexibida.Afigura3.16 ilustraesteprocesso.
Figura3.16:Executandoapáginacomotestedolayout
3.5 Concluindo e desafiando
Oobjetivodestecapítulofoiapresentaravocêalgumasdasprincipaisop çõesparase
estruturar layoutsdeaplicaçõeswebutilizandooASP.NETMVCcoma engineRazor.
Vocêaprendeutambémque,muitoemboraoprocessodeutilizaç ãodasfamosas
master pagessejadiferentena frameworkMVC,eleestápresenteeéamplamente
utilizadonoprocessodeconstruçãodeaplicaçõesweb.
Notesteanterior,aocarregaroaplicativoumerrofoiapresentao,pelafaltado
Controllerpadrão.Pararesolveressepequenoproblemaprecisamoscriarumnovo
controllercomumaviewquerepresente /home/index.Comoquevocêaprendeu
aqui,crieesse controllere viewjáutilizandoamasterpagedosite.
39

## Página 51

Capítulo4
Models:Desenhandoosmodelosda
nossaaplicação
Atéaquivocêfoiapresentadoaumasériedeimportantesconceitoserecursosre-
lacionadosaodesenvolvimentodeaplicaçõescomASP.NETMVC.Jáfalamossobre
convenções(CoC)daframework,sobreomodeloderoteamento, master pages,refe-
renciamentodebibliotecasvia NuGet,dentreoutros.Estesconceitosserãodefun-
damentalimportânciaparaexecutarasoperaçõesquefaremosdaquiatéofinaldo
livro.
Nocapítulo 3,tivemosaoportunidadedevisualizarosaspectosgerais(estru-
turais,inclusive)daaplicaçãodeexemploquenortearátodoodesenrolardosfatos
daquipordiante. Umdosaspectosapresentadosrelacionadoaestaaplicaç ãono
capítuloanteriorfoioDER(verfigura 3.2).Conformemencionamosnaquelemo-
mento,oDERtraztodainformaçãodequeprecisaremosparacriarabasededados
denossaaplicação.
Nestecapítulo,comoopróprionomesugere,iremosdetalharumpoucomais

## Página 52

4.1. Model?! CasadoCódigo
oassunto models,ousimplesmente,modelo,jáqueeleéparteintegrantedasigla
MVCeconstituiparteimportantedasaplicaçõesconstituídasnesteformato.Tendo
istoemmente,estamosprontosparaprosseguir!
4.1 Model?!
Umdosgrandesobjetivosqueo frameworkASP.NETMVCpretendealcan çaréase-
paraçãoderesponsabilidadesentreascamadasdeumaaplicaç ão. Nestecontexto,
apalavra“separação”poderiatranquilamentesersubstituídapelapalavra“isola-
mento”,umavezqueestaúltimapassamaisosentidoquepretendeendere çar.
Comojásabemos,os modelssãoapartedeumprojetoASP.NETMVCresponsá-
velporagrupar—tendoemmenteestemodeloseparatistado framework—asfontes
dedadosdeumaaplicação,sejaestafontededadosforumbancodedados,um web-
service,umarquivoXML,umarquivotexto,entreoutros.Aideiafundamentaléque
asfontesdedadosfiquemisoladasdeformaliteraldasdemaiscamadas.
Masparaquepossamosentenderos modos operandido frameworkjuntoaos
models,apresentaremosalgumasabordagenspossíveisdeformaatreladaaonosso
projetodeexemplo.Mãosàobra?!
4.2 Abordagens para a criação de Models
Emtermospráticos,quandooassuntoé“conexãocomfontesdedados”emuma
aplicaçãoASP.NETMVC,estamosfalandonecessariamenteemconexãoatravésde
modelsafontesdedadosheterogêneas(serviços,arquivosetc.),conformehavíamos
mencionadonoiníciodestecapítulo. Semudarmosestaexpressãopara“conexão
combancosdedados”(queéoquefaremosdefatoemnossaaplicaçãoexemplo)em
umaaplicaçãoASP.NETMVC,aindaassim,estaremosfalandodeconexãoatravés
de models,entretanto,édefundamentalimportânciaentenderqueparaestaabor-
dagem,existemdiferentesformatosparaserealizartalprocedimento.Ostrêsmais
difundidosnomercadosão:
• AtravésdautilizaçãodiretadasclassesADO.NET;
• AtravésdeORM’s(nomodelodatabase first);
• AtravésdeORM’s(nomodelocode-first);
• AtravésdeORM’s(nomodelomodel-first).
42

## Página 53

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
UmapitadinhadeADO.NET
ADOéoacrônimopara ActiveX Data Object.Trata-sedeumconjuntodeclasses
erecursospertencentesaoconjuntode namespacesdaplataforma.NET(daíonome
ADO.NET),disponibilizadoparapossibilitaroacessoàsestruturasdebancosde
dadosporpartedasaplicações. Atravésdela,épossívelrealizardiferentestiposde
acessos.Vocêpodeoptar,porexemplo,entrebuscardadosnamemóriadoservidor
ouiratéobancodedadosacadarequisiç ão,dentrediversosoutrosrecursos. A
figura4.1apresentaumavisãoconceitualgeraldo namespaceSystem.Data.
Figura4.1:VisãoconceitualdoADO.NET
EmaplicaçõesASP.NETMVC,vocêpodeoptarporcriarseusrepositóriosde
acessoadadosutilizando,deformadireta,asclasseserecursosdoADO.NET.Neste
caso,bastaquevocêcrieseumétododeconexãoaobancoeosdemaismétodosde
acessoeexecuçãodassenten çasSQL.
Sevocêestásendoapresentadoaeste setderecursosatravésdestetexto,ostre-
chosdecódigoapresentadosnasequênciapoderãoajudaraentendero modos ope-
randidestemodelo.
Sehouvesseanecessidadedenosconectarmosaumbancodedados,levando-se
emconsideraçãoofatodequea stringdeconexãopudessevariar,porexemplo,
poderíamosterummétododeconexãofictício“ConectaNoBancoDeDados”. Ele
utilizaaclasse“SqlConnection”presentenonamespace“System.Data.SqlClient”,
conformeapresentaalistagem 1.
43

## Página 54

4.2. Abordagensparaacriaçãode Models CasadoCódigo
Listagem 4.1-MétodofictícioparaconexãocomobancodedadosviaADO.NET:
using System.Data.SqlClient;
public bool ConectaNoBancoDeDados(string stringDeConexao)
{
SqlConnection objetoDeConexao = new SqlConnection(stringDeConexao);
try
{
objetoDeConexao.Open();
if(objetoDeConexao.State == ConnectionState.Open)
{
return true;
}
}
catch(Exception ex)
{
throw new Exception(ex.Message)
}
}
Destaforma,bastariaircompondosua(s)classe(s)deacessoadados. Emum
projetoASP.NETMVC,estasestruturaçõesdeveriam(deacordocomaconven ção
do framework)ocorrernodiretório Models.
Valelembrarnestemomentoquenossoobjetivoaquinãoéapresentardeta-
lhesacercadoADO.NET,massim,apresentaraabordagemcomoumapossibi-
lidadedentrodeaplicaçõesASP.NETMVC.Vocêpodeencontrarmaisinforma-
çõesacercado setderecursosdisponibilizadospeloADO.NETatravésdolink:
http://bit.ly/mvc-adonet.
ORM’sentrandoemação
Sevocêjápossuialgumaexperiênciacomdesenvolvimentode software,por
certojáouviufalarsobreumaspectodesumaimportânciaparaprojetosde soft-
ware:osORM’s(Object Relational Modeleminglêse“ObjetoModelo-Relacional”
emportuguês).
ORM’ssãorecursos(ferramentas)criadosparafacilitaraosdesenvolvedoreso
processodeconexãoporpartedesuasaplicações,àsfontesdedados.Emlinhasge-
rais,oqueestasferramentasfazemécriarumacamadadeabstraç ãoemrelaçãoao
44

## Página 55

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
bancodedados,disponibilizandoportantoummodeloemnívelmaisalto(progra-
mático)paraacessaremanipularosdados.
ORM’sapresentamcaracterísticasfuncionaisimportantesquecontribuemem
grandeescalaparasuaado çãoemprojetosde softwaresmodernos.Dentreestasca-
racterísticasdestacam-se:
•Simplicidade:talvezaprincipalcaracterísticaproporcionadapelosORM’séa
simplificaçãodomodelodeacessoaosdados.Graç asaestasimplificação,de-
senvolvedorespodemtrabalharcomasaplicaçõessemnecessariamentepos-
suíremconhecimentosavançadosdeSQLebancosdedados;
•Produtividade:comoodesenvolvedoracessaemanipulaosdadosatravésde
ummodeloprogramáticosimplificado,desenvolvedorestendemasermais
produtivos,umavezqueomodelodedesenvolvimentolheéfamiliar;
•Reduçãodecódigo:comooacessoaosdadoséfeitoemumnívelmaisalto,
automaticamenteonúmerodelinhasdecódigoescritasparaacessarosda-
dosreduzdrasticamente.Vocêpoderáconstatarestefatonamedidaemque
avançamoscomacriaçãodaaplicaçãoCadêmeumédico;
•Facilitaamanutenção:omodelodisponibilizadopelosORM’sfacilitaemuito
amanutençãodaaplicação,poisamanipulaçãodasoperaçõessedáatravésde
códigojáconhecido(objetoseseusrespectivosmétodos);
•Códigoelegante:ofatodeomodelomescladodesenten çasSQLechamadas
demétodosdeobjetosdarlugaraumcódigomaislegívelesemânticotornao
códigofontedaaplicaçãomaiselegante.
Parajustificarasafirmaçõesapresentadasnalistaanterior,utilizaremosexem-
plospráticos. Imagine,porexemplo,queprecisamosadicionarumnovocliente
natabelafictíciade Clientes. Seoptarmospelautilizaçãodasclassesnativas
daplataforma.NET(ADO),poderíamosterumtrechodecódigosemelhanteao
apresentadopelalistagem 2.
Listagem 4.2 - Conectando ao banco de dados e adicionado um novo cliente
viaADO:
string stringDeConexao =
"string para conexão com o banco de dados aqui";
45

## Página 56

4.2. Abordagensparaacriaçãode Models CasadoCódigo
SqlConnection objetoDeConexao = new SqlConnection(stringDeConexao);
SqlCommand objetoDeComando = objetoDeConexao.CreateCommand();
string sql = "INSERT INTO Clientes (NomeCompleto, Email)
values (@NomeCompleto, @Email)";
objetoDeComando.CommandText = sql;
objetoDeComando.CommandType = CommandType.Text;
objetoDeComando.Parameters.Add("@NomeCompleto", NomeCompleto.Text);
objetoDeComando.Parameters.Add("@Email", Email.Text);
objetoDeComando.ExecuteNonQuery();
Ocódigoapresentadopelalistagem 2,comoépossívelobservar,ébastantesim-
ples,entretanto,extensoeverboso.Pararealizaramesmaoperaç ãoutilizandoum
ORMpara.NET,poderíamosterumtrechodecódigosemelhanteaoapresentado
pelalistagem 3.
Listagem 4.3 - Conectando ao banco de dados e adicionando um cliente atra-
vésdeumORM:
Clientes.Add();
Clientes.NomeCompleto = NomeCompleto.Text;
Clientes.Email = Email.Text;
Clientes.Save();
Tantoalistagem 2quantoalistagem 3apresentamcódigosqueexecutama
mesmaoperação:adicionarumnovoclienteaobancodedados. Nãoédifícilob-
servaradiferen çaexorbitanteentreasabordagens. Enquantotemosmuitocódigo
naprimeira,temosumareduçãoconsiderávelnasegunda.Enquantotemosmuitos
objetosemaçãonaprimeiraabordagem,temosbempoucosnasegunda.
Éimportanteobservar,entretanto,quemesmopossuindoasvantagensjámen-
cionadasnestecapítulo,existemalgunsgargalosrelacionadosaosORM’seque,por-
tanto,devemsercuidadosamenteanalisadosparanãoimpactardeformacríticadu-
ranteociclodevidadaaplicaç ão.Oprincipalaspectoaserconsideradoolhando-se
poresteprismaéaperformance.Masnãosepreocupe,voltaremosadiscutirsobre
issoquandoestivermostrabalhandocomo modeldenossaaplicaçãoexemplo.
ExisteumgrandenúmerodeORM’sdisponíveisnomercadoparaotrabalho
dentrodaplataforma.NET.Vocêdeveráanalisarcuidadosamentecadaop çãopara
escolheraquelequemelhoratendeàsnecessidadesdoprojeto. Evidentemente,al-
gunsdelessedestacamporseremreconhecidamenterobustos,comboadocumenta-
46

## Página 57

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
çãodisponívele,também,porpossuíremsuporte.Emfun çãodisso,sãoamplamente
utilizadosemprojetosmundoafora.
ParaaaplicaçãoCadêmeumédico,utilizaremoso Entity Framework(EF),um
ORMdistribuídogratuitamentepelaMicrosoftequetemsidoamplamenteutilizado
emprojetos.NET.Naocasiãoemqueestelivrofoiescrito,aversãoestávelmaisatual
doEFeraa4.0.
4.3 O Entity Framework
EF,comoopróprionomesugere,éum frameworkdotipoORMquepermitetratare
manipulardadoscomoclasseseobjetosdedomínio.Porserdesenvolvido,mantido
edisponibilizadopelaMicrosoft,eleseintegradeformaotimizadaàstecnologias
disponíveisnaplataforma.NETcomperformance,seguran çaerobustez.Porseresta
integraçãonativa,desenvolvedorespodemutilizartambémdeformanaturaldois
grandesrecursosda.NET framework:LINQeexpressõesLambdapararecuperare
manipularosdadosnecessáriosàaplicação.
VocêpodesabermaissobreoEntityFrameworkatravésdolink:
http://bit.ly/mvc-ef
Códigoprimeiro?
UmadasvantagensproporcionadasporboapartedosORMsepropositalmente
nãomencionadanasse çãoanterioréapossibilidadedeescolheraformadetrabalho
doORM.Istoé,vamosnosbasearprimeironobancodedadosfísicoouobanco
dedadosqueserágeradoseráumreflexodenossaestruturadeclasses?Nestase ção
discutiremosumpoucosobreasdiferen ças,vantagensedesvantagensentreestas
abordagens.
Ofamoso code first
Imaginepodercriarumaestruturabemdefinidadeclasses(Clientes,Usuários,
Fornecedoresetc.)cujosatributosemétodos(Codigo,Nome,RazãoSocialetc.)po-
derãoatuaremummomentoposterior,comoestruturasprimárias(tabelas,chaves
primárias,estrangeirasetc.)nacriaçãodaestruturafísicadebancodedadosnoser-
vidor.Legal,não?
Estaéumadascaracterísticasfuncionaisdo Entity Frameworkeéconhecido
como code first(códigoprimeiro,emportuguês).Paraqueestaideiatorne-semais
47

## Página 58

4.3. OEntity Framework CasadoCódigo
clara,vamosàprática.Criaremosumprojetoparalelo,emnadarelacionadoao Cadê
meumédico. Faremosdestaformaporquepara Cadêmeumédicoutilizaremos
outraestratégia.
ComVisualStudiojáemexecução,crieumnovoprojetoASP.NETMVC4(se-
guindoospassosjáapresentadosnoscapítulosanterioresaeste). Sugestivamente
nomearemosestaaplicaçãodeexemplocomo“AplicacaoComCodeFirst”.Valeob-
servarquevocêprecisaráestarcomMicrosoftSQLServer2012Expressinstalado
paracompletaresteexercício. Oprojetoqueestamosutilizandoparaexemplificar
ofuncionamentodo code firstédotipo internet application.Eleutiliza view engine
Razorenãoutilizaprojetodetestes.A solution explorerdesteprojetopodeservisu-
alizadapelafigura 4.2.
Figura4.2:SolutionexplorerdoprojetoAplicacaoComCodeFirst
Porsetratardeumprojetodotipo internet application,quandoexecutada,a
aplicaçãotratáum templatepadrão(semelhanteàqueleapresentadonocapítulo 1).
48

## Página 59

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
Você conhece oSQLS erver2012?
OMicrosoftSQLServer2012éaversãomaisatualdaplataformade
dadosrelacionaisdaMicrosoft.Atravésdela,épossívelgerenciarqual-
querocorrênciarelacionadaaosbancosdedadosrelacionais,incluindo
ferramentasparamineraçãoeextraçãodedadosnãoconvencionais,bu-
sinessintelligence[1],interfacegráficaparaadministração(SQLMana-
gementStudio),entrediversosoutrosrecursos.
Aversão ExpressdoSQLServer2012édisponibilizadagratuitamente
esuportabancosdedadoscomcapacidadedeaté10GB.Parasabermais,
vocêpodeseguirolink:
http://bit.ly/mvc-sqlexpress
Umbomexemploparaquepossamosentenderdeformaclaraepráticaofunci-
onamentodomecanismode code firstcom Entity Frameworkdentrodaplataforma
.NETemprojetosASP.NETMVCéumafraçãodasfuncionalidadesde blog,ouseja,
postsesuasrespectivascategorias.Destaforma,imaginandoaestruturamaissimples
possívelparaestetipodefuncionalidade,poderemosteraseguinterelaç ão:umaca-
tegoriapodepossuirmúltiplos postsenquantoum postpodeestaratreladoaapenas
umacategoria.
Alémdacardinalidade1para nconfiguradapelarelaçãoapresentadanopará-
grafoanterior,temosnotoriamentevisíveisduasentidades: Categoriase Posts.
Muitoemboraestasejaumarelaçãosimples,elanospossibilitaráapresentaralguns
importantesrecursosdo frameworkMVC,aléméclaro,deapresentaro code firstem
ação.
CriandoasclassesPOCO
Quandofalamosem code first,automaticamentefalamosemclassesPOCO.Isso
porquenãoépossíveldissociarumacoisadaoutra.
POCOéoacrônimopara Plain Old CLR Object.Otermoéumaderivaç ãodo
termoPOJO(Plain Old Java Object),originalmenteutilizadopelacomunidadeJava,
comovocêpodeimaginar.Aideiadestetipoespecialdeclasseéserumagentein-
dependentede frameworkse/oucomponentesdentrodaplataforma.NET.Assim,
classespodemherdarseuscomportamentos,interfacespodemserimplementadase
ainda,atributospodemserpersistidos.
49

## Página 60

4.3. OEntity Framework CasadoCódigo
TendoemmenteaimportânciadasclassesPOCOprincipalmenteparaocon-
textodeORM’s(claro,especialmenteparaoEF),iniciaremosnossasatividadescri-
andonossasduasclassesPOCOprincipais: Categoriase Posts.Nomomento
posterior,elasservirãodebaseparaqueoEFimplementeasentidadesnobancode
dadosdaaplicação.
Destaforma,aprimeiraaçãonestesentidoserácriaraclasse Categorias.Para
isso,bastaadicionarumanovaclasseàpasta Modeldaaplicaçãoenomeá-lacoma
palavra Categorias,conformeilustraafigura 4.3.
Figura4.3:Adicionandoumaclasseaodiretório Model
Uma classe com estrutura básica será automaticamente gerada pelo Visual
Studio.Substituaesteconteúdoporaqueleapresentadopelalistagem 4.
Listagem 4.4-ClassePOCOpara’Categorias’:
public class Categorias
{
[Key]
public int CategoriaID { get; set; }
50

## Página 61

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
public string Categoria { get; set; }
public string Descricao { get; set; }
public virtual ICollection<Posts> Posts { get; set; }
}
Comovocêpodeperceber,aestruturadaclasseébemsimplesedispensariaco-
mentáriosparaumdesenvolvedorcomcertaexperiêncianotratocomORM’s.En-
tretanto,épossívelqueasobservaçõesaseguirsejamúteisparavocêquenãose
enquadranasituaçãoapresentadahápouco.
•Atributo [Key]:indicaaoEntityFrameworkqueapropriedadeimediata-
mentenasequência(nocaso, CategoriaID)deveráserconsideradachave
primárianomomentodageraçãodobancodedadosnoservidordedestino.
Épossívelparametrizaresteatributoconformeanecessidadeparaemplacar
comportamentosespecíficos(comoaadiçãoounãodacláusula identity).
Paraacriaçãodonossoexemplo,manteremosopadrãoutilizadopeloEFpara
estageração;
•public virtual ICollection<Posts> Posts { get; set; }:
em uma ferramenta tradicional para composição de banco de dados re-
lacionais, conseguimosexplicitarosrelacionamentosde1paramuitosou
muitosparamuitosdeformabemsimples. Paraexpressaressetipoderela-
cionamentoatravésde code first,utilizamosumacole çãodeobjetostipada;
justamenteoqueestamosfazendocomalinhaemdestaquenestetópico.
EstamosdizendoaoEFqueuma Categoriadeverásuportarmúltiplos
Posts.Legal,não?!
Paraqueaclasse Categoriaspossaexistir,éprecisoque Poststambém
exista. Destaforma,vocêpodeconferiratravésdalistagem 5aestruturadaclasse
Posts.
Listagem 4.5-ClassePOCOquerepresenta’Posts’:
public class Posts
{
[Key]
51

## Página 62

4.3. OEntity Framework CasadoCódigo
public long PostID { get; set; }
public string TituloPost { get; set; }
public string ResumoPost { get; set; }
public string ConteudoPost { get; set; }
public DateTime DataPostagem { get; set; }
public int CategoriaID { get; set; }
[ForeignKey("CategoriaID")]
public virtual Categorias Categorias { get; set;
}
Aobservaçãoválidaemrelaçãoàlistagem 5ficaporcontadaúltimapropriedade.
Diferentementedaclasse Categoriasondepossuímosumacole çãodeobjetos
(sim,uma Categoriapodepossuirvários Posts),aqui,possuímosumainstância
de Categoria,jáque,peladefiniçãodaregradenegócio,um Postpodepertencer
aapenasuma Categoria.Oatributo [ForeignKey("CategoriaID")],como
vocêjádeveestarimaginando,informaaoEFqueapropriedadeimediatamentea
seguirassumiráocomportamentodechaveestrangeiraeque,portanto,seráoelo
comoutratabela—emnossocaso,atabela Posts.
Paraquea enginedoEntityFrameworkpossasercapazdegeraraestrutura
debancodedadoscombasenasclassesPOCO,éprecisoqueexistaumaclassede
amarração, naqualsãoinformadosparâmetroscruciaisnoprocessodegeraç ão
daestruturafinal.EstaclassefoiconvencionadapeloEFcomo classedecontexto.
Nela,implementamosalgumasaçõesquesãofundamentaisparaquetudofuncione
deformaadequada.Confiraocódigoapresentadopelalistagem 6.
Listagem 4.6-ClassedecontextoparaoEntityFramework:
public class BlogContext : DbContext
{
public DbSet<Posts> Posts { get; set; }
public DbSet<Categorias> Categorias { get; set; }
}
52

## Página 63

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
Aclassedecontextoaqualnosreferimosfoicriadanosmesmosmoldesdas
demaisapresentadasatéaqui.Emsetratandodemodelosdedados,evidentemente
estádentrododiretório Models.
Estaéaestruturamaissimplificadapossívelparaaclassedecontexto. Aqui
estamos “dizendo” ao EF, através das diretivasDbSet, que as classesPostse
Categoriasdeverãosercriadasnobancodedadosdedestino.
Umaperguntaquenaturalmentesurgenestepontoé:“Obancodedadosserá
criadoemqualservidor?”.
Estaéumaperguntainteressanteearespostaestádiretamenteatreladaaomo-
delodeconven çõesdoqualfalamosnosegundocapítulo.Porpadrão,seguindouma
convençãodoEFenãodoASP.NETMVC,senenhumastringdeconexãocomoser-
vidordedestinoforinformadaparaoORM,nomomentodacriaç ão,oEFcriaráa
estruturadebancodedadosnoSQLLocalDBouExpressEdition.Aquelequeestiver
disponível—seambosestiveremdisponíveis,LocalDBseráaescolha.
Se for preciso apontar a criação da estrutura de banco de dados para um
servidorespecífico,umadaspossibilidadesdisponíveisparaserealizartaloperaç ão
éatravésdaimplementaçãodeummétodoconstrutornaclasse BlogContext.A
listagem7apresentaestaalteração.
Listagem 4.7 - Classe de contexto adaptada para utilizar um servidor especí-
fico:
public class BlogContext : DbContext
{
public BlogContext() : base("name=BlogContext")
{
Database.Connection.ConnectionString =
@"data source=FABRCIOSANC36FC\SQLEXPRESS;
initial catalog=BlogBDLivro; Integrated Security=SSPI";
}
public DbSet<Categorias> Categorias { get; set; }
public DbSet<Posts> Posts { get; set; }
}
Amudançaemrelaçãoàlistagem 6anteriorésimples:adicionamosométodo
construtordaclassedecontextoe,emseuinterior,apontamosa enginedoEntity
53

## Página 64

4.3. OEntity Framework CasadoCódigo
Frameworkparaoservidorlocal FABRCIOSANC36FC\SQLEXPRESSparaacriação
dobancodedados BlogBD.
Testandoafuncionalidadedocodefirst
Agoraquejápossuímosainfraestruturanecessáriaparaaaplicaç ãoexemplo,
podemosdaropassonosentidodeveroEntityFramework code firstfuncionando.
Paraisso,criaremosdoisnovos controllers: Categoriase Posts.Paracadaum
deles,criaremosoperaçõesdeCRUD(acrônimopara Create, Read, Updatee Delete)
utilizandoumrecursomuitointeressantedisponíveldesdeaversão2da framework
MVC: Scaffold.
Mais sobreScaffold
ScaffoldéorecursodoASP.NETMVCquepermitecriaroperações
decriação,leitura,atualizaçãoeremo çãoderegistrosnobancodedados
deformaautomatizada,utilizandoboaspráticasdedesenvolvimentoea
view-enginepadrão(asaber,Razor).Combasenaestruturadebancode
dadosmapeada,oASP.NETMVCécapazdegeraras actionserespectivas
viewsparapossibilitararealizaçãodasoperaçõesdeCRUD.
Nocasoespecíficono code first,nomomentoemqueapontarmosparao fra-
meworkocontextodedadosparaoqualoCRUDdeverásergerado,automatica-
menteobancodedadosfísicoserágeradonoservidordedestino.
Éimportanteobservarnestepontoque,paraqueasclassesPOCOpossamser
incorporadasao coredoprojeto,seráprecisoexecutarum buildparaela. Esteéo
primeiropasso.
Nasequência,adicioneo controller Categoriasàaplicação(vocêjásabecomo
fazer,bastaclicarcomobotãodireitosobreodiretório“Controller ”,adicionarum
novoitemenomeá-lonasequência).Apósexecutarestespassos,oVisualStudiolhe
apresentaráumanovajanela.Paraocasodo controller Categorias,nobox“Scaf-
fold options”,paraaopção“T emplate”,selecionenalistasuspensaaopção“MVC con-
troller with read/write actions and views, using Entity Framework”.Naopçãoseguinte
(Model class),selecioneaop ção“Categorias”,enaseguinte(Data context class),aop-
ção“BlogContext”.Afigura4.4apresentaasele çãodestasop ções.
54

## Página 65

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
Figura4.4:Adicionandoocontroller‘Categorias’comScaffold
Parao controller Posts,amesmasequênciadeprocedimentosdeveráserreali-
zada.
Aoconcluirestespassos,vocêpoderávisualizaroVisualStudiocriarcódigos
deformaautomática,tantoparao controllerquantoparaas viewsassociadas.Além
disso,seconfigurarmosaguia“Database Explorer”doVisualStudioparanosconec-
tarmosàinstânciadeSQLServerapontadanocódigodalistagem 7apósaexecu-
çãodaaplicação,podemoscomprovaracriação,porpartedoEntityFramework,do
bancodedados BlogBDLivro(afigura4.5apresentaestefato).
55

## Página 66

4.3. OEntity Framework CasadoCódigo
Figura4.5:Bancodedadoscriadovia code first
Paratestarofuncionamentodo scaffold,bastaexecutaraaplicaçãoechamaras
URLsrespectivaspara Categorias(“/Categorias”)ePosts(“/Posts”),conforme
ilustraafigura 4.6.
56

## Página 67

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
Figura4.6:Cadastrandoumanovacategoriacomscaffold
Desafiando:quetalcriaragoraummodelodeclassesdotipo“muitosparamui-
tos”viacode firste,utilizandoorecursode scaffold,geraroperaçõesdeCRUDbase-
adanelas?
4.4 O modelo primeiro?
Senaabordagemanteriorpartíamosdocódigofonteparaobancodedadosfísico,
quandotemosumambienteondeomodelovemprimeiro(comoéocasodo mo-
del first),somosobrigadosapensarquetudopartedeummodelopredefinidopara
chegar,emummomentoposterior,aobancodedados.
ComEntityFrameworktambémpossuímosestapossibilidade.Nestecaso,basta
quecriemosummodelovazio(nosmoldesdoquefaremosnase çãoseguinte)eque,
conformenecessário,adicionemosasentidades.Assim,emummomentoposterior,
oEFcombasenomodelocriadogeraráoselementosnobancodedadosfísico.
Comoesteformatodetrabalhoestálongedeseromaisutilizado,nãoentraremos
emmaioresdetalhesnestelivro.Entretanto,existemalgumasboasfontesdeconsulta
internetafora.Algumasdelasencontram-selistadasaseguir:
57

## Página 68

4.5. Bancodedadosprimeiro? CasadoCódigo
•Model First with Entity Framework — MSDN: http://bit.ly/
mvc-ef-modelfirst
•EntityFrameworkTutorial: http://bit.ly/mvc-ef-tutorial
4.5 Banco de dados primeiro?
Aseçãoanterior,apresentouumdosmodelospossíveisparaotrabalhocomoEntity
Framework—ocode first.Comovocêpôdecomprovarnaqueleformato,saímosde
ummodeloprogramáticoechegamosháummodelodebancodedadosfísico.
Nestaseção,apresentaremosoutraformadetrabalhocomoEF—o database
firstque,deformaopostaaomodelovistoanteriormente,nospermitesairdeum
modelofísicodebancodedadosparachegarmosaummodeloprogramático.
Voltandoàaplicação“Cadêmeumédico?"
Comovocêdeveselembrar,nocapítulo 3,elaboramoseapresentamosaestru-
turadaaplicaçãoCadêmeumédico.Nestaestruturação,umdosaspectosapresen-
tadosfoioseuDER,ondeelucidamosdeformagráficaeconceitualaestruturafutura
dobancodedadosdaaplicação(verfigura 3.2).Valenotarque,emrelaçãoaobanco
dedados,nadafoiimplementadoainda.
Comoestamosfalandonestemomentode database first,parecefazertotalsen-
tidoimplementar,antesdequalqueroutracoisa,obancodedadosdaaplicaç ãoCadê
meumédico.Alistagem 8apresentao scriptSQLquedeuorigemaobancodedados
aoqualnosreferimos.
Parafacilitarautilização,estamosdisponibilizandoo scriptonline,atravésdo
link:
http://bit.ly/mvc-script-bd
Listagem 4.8 - Script SQL que deu origem ao banco de dados da aplicação
’Cadêmeumédico’:
CREATE DATABASE CadeMeuMedicoBD
GO
USE CadeMeuMedicoBD
GO
58

## Página 69

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
CREATE TABLE Usuarios
(
IDUsuario BIGINT IDENTITY(1,1) NOT NULL,
Nome VARCHAR(80) NOT NULL,
Login VARCHAR(30) NOT NULL,
Senha VARCHAR(100) NOT NULL,
Email VARCHAR(100) NOT NULL,
PRIMARY KEY(IDUsuario)
);
GO
CREATE TABLE Medicos
(
IDMedico BIGINT IDENTITY(1,1) NOT NULL,
CRM VARCHAR(30) NOT NULL,
Nome VARCHAR(80) NOT NULL,
Endereco VARCHAR(100) NOT NULL,
Bairro VARCHAR(60) NOT NULL,
Email VARCHAR(100) NULL,
AtendePorConvenio BIT NOT NULL,
TemClinica BIT NOT NULL,
WebsiteBlog VARCHAR(80) NULL,
IDCidade INT NOT NULL,
IDEspecialidade INT NOT NULL,
PRIMARY KEY(IDMedico)
);
GO
CREATE TABLE Especialidades
(
IDEspecialidade INT IDENTITY(1,1) NOT NULL,
Nome VARCHAR(80) NOT NULL,
PRIMARY KEY(IDEspecialidade)
);
GO
CREATE TABLE Cidades
(
59

## Página 70

4.5. Bancodedadosprimeiro? CasadoCódigo
IDCidade INT IDENTITY(1,1) NOT NULL,
Nome VARCHAR(100) NOT NULL,
PRIMARY KEY(IDCidade)
);
GO
ALTER TABLE Medicos
ADD CONSTRAINT fk_medicos_cidades
FOREIGN KEY(IDCidade)
REFERENCES Cidades(IDCidade)
GO
ALTER TABLE Medicos
ADD CONSTRAINT fk_medicos_especialidades
FOREIGN KEY(IDEspecialidade)
REFERENCES Especialidades(IDEspecialidade)
GO
INSERT INTO Cidades (Nome) VALUES ('Blumenau')
INSERT INTO Cidades (Nome) VALUES ('São José do Rio Preto ')
GO
INSERT INTO Especialidades (Nome) VALUES ('Cardiologista')
INSERT INTO Especialidades (Nome) VALUES ('Neurologista')
GO
INSERT INTO Usuarios (Nome, Login, Senha, Email)
VALUES ('Administrador',
'admin',
'40BD001563085FC35165329EA1FF5C5ECBDBBEEF',
'admin@cdmm.com')
GO
Afigura 4.7apresentaoresultadoobtidoaoexecutarmosocódigoapresentado
pelalistagem 8noSQLServer2012Express.
60

## Página 71

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
Figura4.7:ServerexplorerdoSQLServerManagementStudio
Agoraquejápossuímosobancodedadosfísicoparaaaplicaç ão,estamosaptos
adaropróximopasso,istoé,criarseumapeamentoviaEntityFrameworkparaque
aaplicaçãopossautilizá-lo. Paraisso,adicionareiàpasta Modelsumnovotipode
arquivo,chamado“ADO Entity Data Model”,conformeilustraafigura4.8.
61

## Página 72

4.5. Bancodedadosprimeiro? CasadoCódigo
Figura4.8:Selecionandoaop çãoadequadaparaacriaçãodomodelodedados
Aorealizartalprocedimento,vocêestaráautomaticamenteiniciandooprocesso
demapeamentorequeridopeloEF.Comopartedesteprocedimento,umanovaja-
nelasolicitandootipodemapeamentoqueserárealizado(figura 4.9)seráapresen-
tada.Paraaconstruçãodesteexemplo,vocêdeveráselecionaraprimeiraop ção,isto
é,“Generate from database”eprosseguir.
62

## Página 73

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
Figura4.9:Selecionandootipodemapeamentoqueserárealizado
Apróximajanelasolicitainformaçõesde stringdeconexão.Oquefaremosaqui
éapontaroEFparaobancodedadosquecriamosrecentemente.Paraisso,cliqueno
botão“New connection”.Nela,vocêdeveráinformaralgunsdadosdeconexão,como
endereçoparaoservidordebancodedados,usuárioesenha(sepossuir)paraacesso
eonomedobancodedadosaoqualdesejaseconectar.Afigura 4.10apresentaatela
devidamentepreenchida.
63

## Página 74

4.5. Bancodedadosprimeiro? CasadoCódigo
Figura4.10:Adicionandoinformaçõesdeconexão
Aoclicarem OKvocêserálevadodevoltaàtelaanterior,masagora,coma string
deconexãojáselecionada.Bastanomearavariávelqueserásalva(eposteriormente
referenciada)noarquivo Web.configdaaplicaçãoeprosseguir(verfigura 4.11).
64

## Página 75

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
Figura4.11:SelecionandostringdeconexãoenomeandoavariávelparaWeb.config
Apróximatelasolicitaráquevocêselecioneosobjetosdobancodedadosque
serãomapeados.Emnossocaso,selecionaremostodasastabelas,conformesugere
afigura4.12.Vocêtambémdeveránomearo namespaceaoqualestãoagrupadosos
arquivosdomodelo.Utilizaremosonome CadeMeuMedicoBDModel.Apósisso,
cliqueem“Finish”.
65

## Página 76

4.5. Bancodedadosprimeiro? CasadoCódigo
Figura4.12:Selecionandoosobjetosaseremmapeadosdobancodedados
Aofinalizaroprocesso,oEntityFrameworkirácriartodaaestruturadeclasses
necessáriaparaquesepossautilizarobancodedadosemumnívelmaisalto.Setudo
correubem,vocêdeveráestarvisualizandoumaimagemsemelhanteàapresentada
pelafigura4.13.
66

## Página 77

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
Figura4.13:ModelodeclassesgeradopeloEntityFramework
Alémdisso,algumasmodificaçõesestruturaisnoprojetopoderãoserclaramente
notadasatravésda solution explorer. Nodiretório“References”,porexemplo,você
perceberáaadiçãodeumanovaDLL,asaber, System.Data.Entity.Amudan ça
maisimportanteentretanto,estáevidentementenapasta Models.IssoporqueoEF
adicionaautomaticamenteumarquivocomaextensão .edmxeestegrandearquivo
éoobjetofinaldomapeamentorealizado. Agrupam-se,portanto,todasasclasses
necessáriasparaotrabalhocomobancodedados.
Afigura 4.14apresentaaestruturadoarquivoedmxgerado. Comumduplo
cliquesobreasclasses,épossívelvisualizarsuasestruturas,queseguemfielmenteo
modelofísicodobancodedados.
67

## Página 78

4.5. Bancodedadosprimeiro? CasadoCódigo
Figura4.14:AestruturadoarquivoEDMX
Outramudançaquepodeserpercebidanaestruturadaaplicaç ão,masquenão
évisívelatravésda solution explorer,éaadiçãoda stringdeconexãonoarquivo
Web.config,conformeilustraalistagem 9.
Listagem 4.9 - Adição da string de conexão no arquivo Web.config pelo Entity
Framework:
<connectionStrings>
<add name="EntidadesCadeMeuMedicoBD"
connectionString="metadata=res://*/Models.ModeloDeDados.csdl|
res://*/Models.ModeloDeDados.ssdl|
res://*/Models.ModeloDeDados.msl;provider=System.Data.SqlClient;
provider connection string=&quot;
data source=.\SQLEXPRESS;initial catalog=CadeMeuMedicoBD;
integrated security=True;
MultipleActiveResultSets=True;App=EntityFramework&quot;"
providerName="System.Data.EntityClient" />
</connectionStrings>
Pronto.Nestemomento,temostudooqueprecisamosparaconseguirtrabalhar
comobancodedadostendocomofocoomodelorecém-gerado.Paraestecapítulo,
járeunimostodainformaçãonecessáriaparaseguircomospróximospassos.Àme-
didaqueaaplicaçãoforganhandoforma,vocêentenderácomosedáoprocessode
interaçãocomomodeloquecriamosaqui.
68

## Página 79

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
4.6 Model first x Code first: Quando utilizar um
ou outro?
Nasseçõesanteriores,apresentamososdoismodelosdetrabalhomaisusuaisquando
oORMemquestãoéoEntityFramework. Levando-seemconsideraç ãoofatode
queambososmodelossãofuncionaiseobjetivamamesmacoisa(istoé,manipular
dados),umaperguntanaturalsurgenacabe çadegrandepartedosdesenvolvedores:
“quandoutilizaraabordagemXouY?”
Comoédeseesperarparaperguntasdestetipo,arespostamaisprudenteé: de-
pende.
Existemdiversosaspectosquedevemserconsideradosemumprojetodesoft-
wareaoseoptarpordeterminadatecnologiae/oumetodologia.Algunsdosquede-
vemserconsideradossão:robustez,conectividade,seguran ça,performanceepro-
dutividade.Issosemfalarnapreferênciadogestordoprojetoatreladoao expertise
deseutime.
QuandofalamosdeestratégiadeacessoadadosutilizandoEF,osaspectosmen-
cionadostambémsãodecisivos. Assim,senãopodemosdarumarespostadefini-
tivaparaaperguntainicialdestase ção,podemosaomenosapresentarvantagense
desvantagensdecadamodeloparaquevocêpossareunirinsumosparaescolherde
formamaisassertivaaestratégiadeacessoadadosparasuaaplicaç ão.
Codefirst:vantagensedesvantagens
Quandofalamosemummodeloemqueocódigodaaplicaç ãopoderágerara
estruturadobancodedados,imediatamentealgumascaracterísticaspositivasjános
vêmacabeça,certo?Vamosaelas:
•Isolamentodocódigofontedaaplicaç ãoemrelaçãoaobancodedados:esta
é,semdúvida,agrandevantagemdoEF code first. Comoomodeloétodo
baseadoemclasseseseusrespectivosobjetos,épossívelquedesenvolvedores
consigamcriaraplicaçõescomestruturasdebancosdedadoscomplexassem
escreverumalinhasequerdeSQL(Structured Query Language);
•Produtividade:comoomodelodedesenvolvimentoproporcionadopelo code
firstébemfamiliar,deformageral,épossívelobterboaprodutividadepor
partedosdesenvolvedores;
•Códigolimpo:acriaçãodasclassesPOCOajudamamanterocódigolimpo,
69

## Página 80

4.6. ModelfirstxCodefirst:Quandoutilizarumououtro? CasadoCódigo
umavezqueosdesenvolvedorespodemseguirospadrõesdedesenvolvimento
deseusprojetos;
•Controlecompletodecódigo:comoasclassesPOCOsãocriadasemantidas
peloprópriodesenvolvedor,ocontrolesobreaquiloqueégeradonobanco
dedadosébemmaisfácildeserrealizado.Classesgeradasautomaticamente
tendemaserdedifícilmanuten ção;
•Simplicidade:deformageral,otrabalhocom code firsttendeasermaissim-
ples. Issoporquenãoexisteanecessidadedesemanterumarquivo .edmx.
Qualquerproblemageradonestearquivoimplicaránecessariamenteempro-
blemascoma enginedeacessoadados.
Masnemtudosãoflores. Code firstpossuium“problema”intrínseco,proveni-
entedoseuesquemadetrabalhoquelimitasuautilizaç ãoemboapartedosprojetos:
deformageral,elepodeseraplicadoapenasanovosprojetos,jáque,dependendo
dacomplexidadedobancodedadosdeaplicaçõesjáexistentes,ficainviávelgerar
classesPOCOmanualmenteparaobteraequivalêncianobancodedadosfísico.
Dica:Seumnovoprojetoforseuobjetodeestudo,considereutilizaromodelo
code first.Osresultadosdestetipodeabordagemparaestanaturezadeprojetocos-
tumamrenderexcelentesfrutos.
Databasefirst:vantagensedesvantagens
Éclaroqueexistemmuitosnovosprojetosdesoftware.Atodoinstantenosde-
paramoscomeles.Entretanto,existemprojetosqueprecisampassarporcomplexos
processosdemigração,porexemplo,e,paraestetipodecenário, database firstseen-
quadraperfeitamente.Assim,aooptarpormodelodetrabalho,osdesenvolvedores
poderãousufruirdosseguintesbenefícios:
•Isolamentocompletodasatividades:seosistemajápossuiumbancodeda-
doscriadoe/oumantidoporDBA’s,utilizaromodelo database firstpermitirá
separaraindamaisasresponsabilidadesdoprojeto,umavezqueaatualizaç ão
domodelobaseadonasalteraçõesrealizadasdiretamentenobancodedados
funcionammuitobem;
•Reduzdrasticamenteotempodemapeamentodebancospré-existentes:
database firstreduzdeformadrásticaotempodispensadoaomapeamentode
bancosdedadospreexistentes;
70

## Página 81

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
•PersonalizaçãodeclassesPOCO:muitoemboraasclassesPOCOsejamge-
radasdeformaautomáticapeloEntityFramework,épossívelpersonalizá-las
atravésdeclassesparciaisouatémesmoatravésdotemplatedeclassesdispo-
nibilizadopeloEF;
•Possibilidadedemúltiplosmodelosnomesmoprojeto:sim,épossívelpos-
suirdiferentesmapeamentos,dediferentesbancosdedados,namesmaapli-
cação.
Oprincipalproblemarelacionadoaomodelodisponibilizadopor database first
residenaconcentraçãodetudodentrodeumúnicoarquivo(o edmx).Conformeo
bancodedadosdeorigemcresceemtamanhoecomplexidade,oarquivotambémo
faz,oquedificultaamanuten ção.Emfun çãodisso,nagrandemaioriadasvezes,é
precisoqueasmáquinasquemanipulamestesarquivospossuamboasconfigurações
dememória.
Dica:Deformageral,omodelo database firsttendeasermelhoraplicávelem
situaçõesemqueexistemaplicaçõescomseusbancosdedadosjáemfuncionamento
(migração,reengenhariaetc.),mas,diferentementedomodelo code firstquepode
seraplicadonamaioriaesmagadoradasvezesapenasemnovasaplicações,sevocê
desejapossuircontroletotaldasocorrênciasnobancodedados, database firstpode
seraplicáveltambémparanovosprojetos.Assim,nofinaldascontas,estemodelo
acabasetornandomaisflexível.
4.7 Adicionando atributos de v alidação nos mode-
los
A framework .NET disponibiliza através do namespace Sys-
tem.ComponentModel.DataAnnotationsvários atributos de validação que podem
seremmodelosdeclassesdoEntityFrameworkeLinqToSQL.
Adicionandoessesatributosdevalidaçãonos models(modelos)danossaaplica-
ção,oMVCfaráessavalidaçãodeformatransparente,semnecessidadedecodifica-
çãoadicionalporpartedoprogramadorparaavalidaç ãobásicassobreo model.
Anteriormente,utilizamosomodelo database firstparageraros modelsdanossa
aplicação,ouseja,os modelssãoautomaticamentegerados,baseadonaestruturado
bancodedados. Umaboapráticaénãocolocarosatributosdevalidaç ãodireta-
mentenasclassesgeradasautomaticamentepeloVisualStudio.Issoporquesempre
queomodelodoEntityFrameworkforatualizadocombasenobancodedados,
71

## Página 82

4.7. Adicionandoatributosdevalidaçãonosmodelos CasadoCódigo
asclassesserãorecriadas,ecomissoqualquermodificaç ãofeitaanteriormenteserá
perdida.
Seguindoessaboaprática,nãoiremosadicionardiretamentenaclassegerada
peloVisualStudioosatributosdevalidaç ão. Criaremosumaclassedemetadados
contendoasvalidaçõese,utilizandoorecurso Partial Classou Classes Parciais,va-
mosvincularaclassedemetadadocomaclassecriadaautomaticamente.
ClassesParciais
Dentreváriosrecursosdisponibilizadospelaplataforma.NET,encon-
tramosasPartialClassouClassesParciais.Graç asàsclassesparciaispo-
demosdividiradefiniçãodeumaclasseemváriosarquivosfísicos. A
keyword partialdeveráserutilizadanadefiniçãodaclassepara“di-
zer”queaclasseéparcial.
Todas as classes geradas automaticamente utilizando Entity Fra-
meworkrecebemakeyword partialnasuadefinição.Devidoaessere-
cursoconseguimosestenderessasclassessemalteraroarquivofísicoque
épassíveldemodificaçãopeloEntityFramework.
Paracriarasvalidaçõesreferentesao modelMédico, cliquecomobotãodi-
reitodomousenapasta Modelsda Solution Explorer ecliqueem Add. Naja-
nelaqueseráapresentadaselecioneotipo Class,edefinaonomedaclasseiguala
MedicoMetadado.Afigura 4.15representaesseprocesso.
72

## Página 83

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
Figura4.15:AdicionandoaclassedemetadadoparaomodelMedico
Apósacriação,oarquivoseráabertoautomaticamentepeloVisualStudio. A
listagem10representaocódigoquedeveráseradicionadonaclasseMedicoMeta-
dado.cs.
Reparequeoarquivo MedicoMetadado.cspossuiadefiniçãodasclasses
MedicoMetadadoeaclasseparcial Medico.
Naclasseparcial Medicoutilizamosoatributo MetadataTypeparainformar
qualotipodaclassequepossuiosmetadadosqueserãoutilizados,eécomesses
atributosqueinformamosqueaclasse MedicoMetadadodeveráserutilizada.
Aclasse MedicoMetadadopossuiasmesmaspropriedadesdaclasse Medico,
afinalénelaquecolocaremosasvalidaçõesdaspropriedades.Emcadapropriedade,
utilizamososatributosnecessáriosparafazeravalidaçãoquedesejamos.
Em todos os exemplos estamos utilizando só dois atributos, o atributo
Requireddefinequeaquelapropriedadeéobrigatória,ejádefinimosneleamen-
sagemdeerroqueseráapresentadacasoapropriedadenãoestejainformada.Além
davalidaçãodecampoobrigatório,podemosutilizaroatributo StringLenght
paravalidarotamanhodostextosinformados,ecasootamanhoultrapasseolimite
informado,definimostambémamensagemdeerroqueseráapresentada.
Listagem 4.10-DefiniçãodosMetadadosdomodelMedico:
namespace CadeMeuMedico.Models
{
73

## Página 84

4.7. Adicionandoatributosdevalidaçãonosmodelos CasadoCódigo
[MetadataType(typeof(MedicoMetadado))]
public partial class Medico
{
}
public class MedicoMetadado
{
[Required(ErrorMessage="Obrigatório informar o CRM")]
[StringLength(30, ErrorMessage="O CRM deve possuir no
máximo 30 caracteres")]
public string CRM { get; set; }
[Required(ErrorMessage = "Obrigatório informar o Nome")]
[StringLength(80, ErrorMessage = "O Nome deve possuir no máximo
80 caracteres")]
public string Nome { get; set; }
[Required(ErrorMessage = "Obrigatório informar o Endereço")]
[StringLength(100, ErrorMessage = "O Endereço deve possuir no
máximo 100 caracteres")]
public string Endereco { get; set; }
[Required(ErrorMessage = "Obrigatório informar o Bairro")]
[StringLength(60, ErrorMessage = "O Bairro deve possuir
no máximo 60 caracteres")]
public string Bairro { get; set; }
[Required(ErrorMessage = "Obrigatório informar o E-mail")]
[StringLength(100, ErrorMessage = "O E-mail deve possuir no
máximo 100 caracteres")]
public string Email { get; set; }
[Required(ErrorMessage = "Obrigatório informar se Atende
por Convênio")]
public bool AtendePorConvenio { get; set; }
[Required(ErrorMessage = "Obrigatório informar se Tem Clínica")]
public bool TemClinica { get; set; }
[StringLength(80, ErrorMessage = "O Website deve possuir no
74

## Página 85

CasadoCódigo Capítulo4. Models:Desenhandoosmodelosdanossaaplicação
máximo 80 caracteres")]
public string WebsiteBlog { get; set; }
[Required(ErrorMessage = "Obrigatório informar a Cidade")]
public int IDCidade { get; set; }
[Required(ErrorMessage = "Obrigatório informar a
Especialidade")]
public int IDEspecialidade { get; set; }
}
}
Vimosatéaquiaspossíveisformasdecriaç ãodosmodelosdaaplicaç ão,além
deadicionaratributosdevalidaçãoaspropriedadesdomodelo.Masnossaaplicaç ão
nãopossuisóo modelMedico—aindatemosUsuários,CidadeseEspecialidades.
Repitaoprocessoapresentadoefaçaasclassesdemetadadosreferenteacadamodelo
daaplicação.
Lembre-seque,casosejanecessário,oscódigosfontescompletosdaaplicaç ão
estãonogithub:
http://bit.ly/mvc-livrocodigofonte
Maséumexcelenteexercíciovocêmesmocriartodasasentidades.
75

## Página 87

Capítulo5
Controllers:Adicionando
comportamentoanossaaplicação
Ouniversodedesenvolvimentodesoftwaredisponibilizadiferentesabordagenspara
aconstruçãodasaplicações(sobreoquejádiscutimosumpouconoprimeirocapí-
tulodestelivro). Taisabordagenspodemvariaremfun çãodediversosaspectos,
sendoosdoisprincipais: oparadigmafuncionaldalinguagem(orientadaaobje-
tos,funcional,proceduraletc.) easmetodologiaseferramentasassociadasparao
trabalhoconjuntocomaslinguagenseIDE’s.
Nestecontexto,podemosconcluirque,evidentemente,existemdiferentesfor-
masparaquesepossaimplementaroscomportamentosdesejadosparaasaplicações.
Comovocêdeveselembrar,nomodelodeprogramaç ãopropostopeloASP.NET
WebForms,porexemplo,taiscomportamentosestavamdiretamenteligados(via
code-behind)acomponentesdeservidorqueerampredefinidospelaMicrosoft.Tal
modeloéconhecidopormuitoscomo“programaçãoorientadaaeventos”(herança
deplataformasdedesenvolvimentocomoDelphi,VB,dentreoutras).

## Página 88

5.1. Vamos‘controlar’aaplicação? CasadoCódigo
QuandofalamosemASP.NETMVC,referimo-nosnecessariamenteàimple-
mentaçãodecomportamentosparaasaplicaçõesatravésdeelementosdo framework
conhecidoscomo controllers(emportuguêsbrasileiro,“Controladores”). Evidente
queonome controllernãofoiatribuídoporacaso.Seunomeresumedeformasin-
tética,porémperfeita,suaatuaçãodentrodopadrãoarquiteturalMVC.
Nestecapítulodiscutiremosdeformamaisaprofundadaautilizaç ãodos con-
trollersnocontextodeaplicaçõesconstruídasatravésdoASP.NETMVC.Aofinal,
deverãoestarclarosparavocêosseguintesaspectosrelacionadosaesteselementos:
• OquesãocontrollersesuaimportâncianosprojetosASP.NETMVC;
• Oquesãoactionsesuarelaçãocomos controllers;
• Entenderocomportamentoidealdoscontrollersemaplicaçõesbemconstruí-
das;
• Mododeativaçãoechamadade controllers;
• Criarviewsapartirde actionspresentesnos controllers;
•Actionsquepodemnãodarorigema viewsmasquesãomuitoimportantes.
Compreenderofuncionamentodos controllersesuas actionsédefundamental
importânciaparaaconstruçãodeaplicaçõesutilizando ASP .NET MVC.Definimos
nocapítuloanterioros models(modelos)danossaaplicação,chegouomomentode
adicionarmosumpoucodevidaaela.
Vamoscomeçar?!
5.1 Vamos ‘controlar’a aplicação?
Umorquestradordeoperaçõesdiversas.Estaéumaboadefiniçãoparaos controllers
dentroda frameworkASP.NETMVC,jáquesãoelesqueagrupamtodososcompor-
tamentosdaaplicação.
Comovocêdeveselembrar,nocapítulo2 falamosumpoucosobreomodelode
rotasimplementadopeloASP.NETMVC.Naquelaocasião,mencionamosofatode
que,aoreceberdeterminadarequisição,oMVCprocurariao controllerquerespon-
deriaparaela,determinariaqual actionaprocessariaeentão,gerariaavisualizaç ão
paraocliente.
78

## Página 89

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
Emtermostécnicos,um controllernadamaisédoqueumaclassequeherda
comportamentosdeoutra(asaber, Controller)disponívelnaBCL.Cadamétodo
disponívelnestaclasseespecialéchamadode Action.As Actionssão,efetivamente,
amenorunidadedeaçãodentrodeum controller.Sãoelasqueencapsulamoscom-
portamentosquesãoinvocadosatodomomento,pelaclassecontroladora.
5.2 Entendendo o papel dos Controllers e Actions
Fazendoumaanalogiasimples,podemosdizerqueos controllersserãoosmediado-
resdasconversasentreasvisõesdaaplicaç ão(views)eosmodelos(models).
Os controllersserãoresponsáveisporreceberetransformarasrequisiçõesen-
viadaspelas viewseminformaçõesqueserãoutilizadaspelasregrasdenegócioda
aplicação,ouseja,os models.Ocontráriotambéméverdadeiro,os controllerstêma
responsabilidadedeselecionara viewcorretaparaapresentaçãodeinformaçõesao
usuário.
Aoreceberumarequisição,oscontrollersdevemefetuaralgumaaç ãoparaque
arequisiçãosejaprocessada,essasaçõessãoas actions.Asactionssãométodosde-
finidosnocontroller,eocontrollerpodeterváriasactions.
Paraexemplificarautilizaçãodos controllerse actions,criaremosemnossaso-
luçãodeexemplo(Cadêmeumédico),um controllerfictíciocomalgumas actions.
Masantesdeiniciarmos,éaltamenterecomendávelquevocêentendaemsuapleni-
tudeoconceitoderoteamento(jáapresentadonocapítulo 2).
Lá você pôde entender que o roteamento padrão do MVC é definido por
{controller}/{action}/{id}. Emnossoexemplo,queremosqueasseguin-
tesURLsestejamrespondendonaaplicação:
•http://localhost/mensagens/bomdia
•http://localhost/mensagens/boatarde
Oprocessodecriaçãodenovoscontroladoresésimples,bastaquevocêrepita
ospassosjáinformadosanteriormente,istoé,cliquecomobotãodireitodomouse
nodiretório Controllers(na Solution Explorer)enasequência,nomenuqueserá
apresentado,escolhaasop çõesAdd > Controller.
Umanovajanelaondepodemosdefiniralgunsparâmetrosepropriedadesdo
novo controllersemostrará.Vocêdeveráfornecercomoentradaparaocampo Con-
troller Nameovalor MensagensControllere,paraogrupo Scaffold optionsno
79

## Página 90

5.2. EntendendoopapeldosControllerseActions CasadoCódigo
campo T emplate,aopção Empty MVC controller.Aofinal.ajanelacomosvalores
configuradosdeveestarparecidacomaapresentadapelafigura 5.1.
Figura5.1:CriandooControllerMensagens
Apósisso, vocênotaráqueoVisualStudioabriráoarquivorecém-criadoe
quenointeriordenosso controller MensagensControlleruma actionchamada
indexjáestarácriada.Assim,seu controllerdeveráestarparecidocomoapresen-
tadopelalistagem 1.
Listagem 5.1-CódigopadrãodoMensagensController:
public class MensagensController : Controller
{
//
// GET: /Mensagens/
public ActionResult Index()
{
return View();
}
80

## Página 91

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
}
Oquefaremosagoraéexcluira action indexpredefinidaecriarnovasduas
novas,chamadas BomDiae BoaTarderespectivamente.Oscódigosquecompõem
tais actionsdeverãoapresentaralgumainformaçãoparaousuário. Estasserãoas
funçõesdeambas.
Nãosepreocupe,otipoderetorno ActionResulteadiretivaderetorno
Contentqueutilizaremosemnossosexemplosserãodiscutidasemmaioresdeta-
lhesàmedidaqueavan çamosnestecapítulo.
A listagem2apresenta o código dasactionsque executarão as tarefas que
o usuário final solicitará e que você deverá adicionar ao seucontrollerpara a
visualizaçãodoexemplo.
Listagem 5.2-Actionsqueretornammensagensparaousuário:
public class MensagensController : Controller
{
public ActionResult BomDia()
{
return Content("Bom dia... hoje você acordou cedo!");
}
public ActionResult BoaTarde()
{
return Content("Boa tarde... não durma na mesa do trabalho!");
}
}
Pronto.Nossoprojetojápodeserexecutado.Compile-outilizandoatecla F5.
Seunavegadorpadrãoserátrazidoàexecuç ãoeiráapresentarumamensagemde
errodizendoque“Não foi possível encontrar o recurso”.Muitoemboraamensagem
deerrosejaemitida,elajáeraesperada.Issoaconteceporqueaindanãocriamoso
controllerpadrãoconfiguradonoroteamentodonossoprojeto.
Nestemomento,paraquevocêpossavisualizaroexemploemexecução,descon-
sidereamensagemdeerroe,nabarradeendere çodeseunavegador,completeaURL
apresentadacomosvalores /mensagens/bomdiaou /mensagens/boatarde.
Percebaqueestamossolicitandoespecificamenteum /{controller}/{action}
e,comisso,oMVCfazoroteamentoparao controllere actionquesolicitamoseque
podemseraplicados.
81

## Página 92

5.2. EntendendoopapeldosControllerseActions CasadoCódigo
Vejaatravésdafigura5.2umexemplodeumamensagemsendoexibidaaousuá-
rio.
Figura5.2:Usuáriovisualizandoamensagemdefinidanaaction
Como você pôde perceber, quando digitamos a URLhttp://localhost:1063/
mensagens/boatarde,obtivemosaresposta“Boa tarde... não vá dormir na mesa do
trabalho”.Issoocorreuporque,aoreceberarequisição,o controller mensagensdi-
recionouofluxodeprocessamentoparaa actionsolicitada,istoé, boatarde.Por
suavez,a action boatardeexecutouaoperaçãoquelheeradevidaeenviouum
retornode conteúdo(noteautilizaçãodadiretiva Content),nestecaso,uma string
simples.
82

## Página 93

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
ActionR esult eContentR esult, quais as diferenças?
ActionResultéotipoderetornomaisgenéricoexistentedentrodo
frameworkASP.NETMVC.Elesuportaqualquertipoderesultadoque
possaserretornado,sendoosmaiscomuns: JsonResult,ContentResult,
EmptyResult,FileResult,JavaScriptResult,RedirectResult.Cadaum
dosmencionadosnadamaisédoqueaextensão(atravésdeheran ça)
deActionResult.Suaimplementaçãoéextremamentesimples,contendo
apenasummétodoparaserimplementadonaclassequeaherda,haja
vistaqueActionResultéumaclasseabstrata.
Destaforma, ContentResulttrata-sedeumaimplementaçãoexten-
sivadaclasseActionResult,quepermiteformatarqualquertipodecon-
teúdoquesedesejaretornar,especificandoinclusive,seu ContentType.
Textos simples (como nosso exemplo) até sentenças mais complexas
(comonodosdeXML,porexemplo)podemserretornadosatravésde
Content.
Agoraquevocêjáfoiapresentadoaosconceitosiniciaisrelacionadosaos control-
lers,échegadoomomentodevoltarasaten çõesparanossaaplicaçãodeexemplo.
Issoseráfeitonapróximase ção.
5.3 Cadê meu médico: o que faremos?
Apartirdaqui,apresentaremosalgumasformaspráticasparaotrabalhocom control-
lers,utilizandoexemplosreais(todosnocontextodaaplicaç ãoCadêmeumédico).
Apresentaremososdiferentesmodelosdeinteraçãoentre viewse controllerse,aofi-
nal,vocêterápresenciadoalgumasdasdiversasformasdetrabalhocom controllers.
Comojámencionamos,existemdiferentesformaspararealizarainteraçãoentre
controllerse viewsemaplicaçõesASP.NETMVC.Nestecapítulo,apresentaremosas
principais(comumenteutilizadasemprojetosreais).Assim,paraquevocêpossaes-
truturardeformaaindamelhorseusestudos,listamosaseguirosprincipaisaspectos
relacionadosaos controllersqueveremosaqui.Sãoeles:
• Comopassardadosdeumcontrollerparauma view;
• Comopassardadosdeumaviewparaum controller;
83

## Página 94

5.4. Cadêmeumédico:CRUDs CasadoCódigo
• Passandodadosdeumformulárioparacontroller;
• Comunicaçãode controllerscomarquivosderepositórios;
• CRUDsutilizandooScaffolddoASP.NETMVC.
Paraquetodasessasaçõespossamserimplementadas,criaremosCRUDspara
cadaumdoselementosdaaplicaçãoCadêmeumédico(vocêselembra:Usuários,
Médicos,EspecialidadeseCidades).
5.4 Cadê meu médico:CRUD s
Iniciaremosodesenvolvimentodo backenddaaplicação Cadê meu médicocriando
oCRUDessencialparaofuncionamentodaaplicaç ão,istoé,ocadastrode Médicos.
Faremosdestaformaporqueéessencialcompreendermos,nestemomento,ofluxo
detrabalhobásicoutilizandooASP.NETMVC.
Atravésdocadastrode Médicosserápossívelentenderomodeloatravésdoqual
enviamoserecebemosinformaçõesdosformuláriosHTML,alémdecriartodaaló-
gicabásicanas actionsdonosso controllerparaqueocadastrofuncionedeforma
adequada.Muitoemboratenhamosumcapítulointeirodedicadoaoestudodas vi-
ews,jánocadastrode Médicosfaremosalgumasmodificaçõesnas viewsgeradasau-
tomaticamentepela frameworkMVC.
Horadecome çaraconstruçãodocadastrode Médicos. Bastaquevocêrepita
ospassosjáinformadosanteriormente,istoé,cliquecomobotãodireitodomouse
nodiretório Controllers(na Solution Explorer)enasequência,nomenuqueserá
apresentado,escolhaasop çõesAdd > Controller.
Najaneladecriaçãodo controller,nomeie-ocomo MedicosController.Não
seesqueçada CoCassociadaaos controllersemrelaçãoaosseusnomes. Estesno-
mesdevempossuirosufixo Controller.Seguindocomaparametrização,naop ção
T emplate,selecioneovalor Empty MVC controller.Ajanelacompletamenteparame-
trizadadeveseparecercomafigura 5.3.
ApesardoASP.NETMVCpossuirummecanismode Scaffoldingpoderosoque
criaautomaticamente controllers/actions/views,construiremosmanualmentetodoo
controlleredemaisrecursosnecessários.Issofarácomqueoentendimentodetodo
ofluxodecriaçãoefuncionamentodoMVC,sejafacilitado.
84

## Página 95

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
Figura5.3:CriaçãodoMedicosController
Éimportantenotarofatodeque,muitoemboraestejamosutilizandoo template
Empty MVC controller paraesteprimeiro controllerdeexemplo,aosercriado,o
MedicosControllerjátrazemseuinterioruma actionpadrãochamada Index.
Ocódigopadrãodo controllerdeveestarparecidocomodalistagem 3.
Listagem 5.3-CódigopadrãocriadopeloVisualStudio:
public class MedicosController : Controller
{
//
// GET: /Medicos/
public ActionResult Index()
{
return View();
}
}
QuandooadministradordoaplicativonavegaratéaURL /Medicos/,será
possívelvisualizaralistadetodososmédicosjácadastrados.Osmodelosdanossa
85

## Página 96

5.4. Cadêmeumédico:CRUDs CasadoCódigo
aplicaçãoforamcriadosutilizando Entity Frameworkeéatravésdelequeobteremos
alistademédicosjácadastradosparaque,emummomentoposterior,possamos
enviá-losparaa view.
Evoluirépreciso,assim,continuandoaconstruçãodo MedicosController,
precisamosagoracriarumainstânciadoobjeto EntidadesCadeMeuMedicoBD
que possibilitará todo o trabalho de comunicação dos nossos modelos (mo-
dels)comobancodedadosdaaplicaç ão. Lembre-sedeadicionaronamespace
CadeMeuMedico.Modelsnos usingsdo controller MedicosController.Coma
instânciadocontextodeentidadesdo Entity Frameworkcriada,podemosna action
IndexobterumalistacomtodososMédicoscadastradose,noinstanteseguinte,
passarestesdadosparaa view.Alistagem 4representaisso.
Listagem 5.4-ActionIndexretornandoalistademédicoscadastrados:
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using CadeMeuMedico.Models;
namespace CadeMeuMedico.Controllers
{
public class MedicosController : Controller
{
private EntidadesCadeMeuMedicoBD db =
new EntidadesCadeMeuMedicoBD();
public ActionResult Index()
{
var medicos = db.Medicos.Include(m => m.Cidade)
.Include(m => m.Especialidade).ToList();
return View(medicos);
}
}
}
Ocódigoapresentadopelalistagem 4ésimples.Oaspectoaserressaltadoaqui
éoretornoda action Index.Comovocêpodeperceber,estamosretornandouma
lista( .ToList())detodososmédicos( .Medicos)disponíveisnocontexto(db).
86

## Página 97

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
Outro detalhe interessante na listagem4 é a utilização dos métodos
.Include(). Autilizarométodo .Include,informamosao Entity Framework
quealémdomodelo(tabela)queestamoscarregando,queremosobterseusrelacio-
namentos,ouseja,nessecasoestamoslistandoosmédicoseobtendosuarespectiva
“Especialidade”e“Cidade”.
Agoraquejápossuímosa action Indexcriadaefuncionando,podemosadici-
onara viewqueresponderávisualmenteàsolicitaçãode Indexnonavegador—
aquelaquemostraráalistademédicoscadastradosparaousuáriofinal.Parareali-
zartaloperação,faremosumavezmaisousodo scaffoldingda frameworkASP.NET
MVC.
Cliquecomobotãodireitodomousesobreométodo Viewdentroda action
Index,nomenudecontextoqueseráexibidoselecioneaop ção Add View...,afigura
5.4demonstraesseprocesso.
Figura5.4:AdicionandoumanovaView
Najanelaqueseráapresentada,configuraremososdetalhesreferentesanova
view.Configurea viewdaseguinteforma:
•View name:automaticamenteoMVCvaisugeriromesmonomeda action,
nessecaso Index;
•Create a strongly-typed view:marqueessaop çãopois,atravésdela,criaremos
uma viewfortementetipada,fatoquefacilitaránossotrabalho,permitindoa
utilizaçãodiretado modelna view;
•Model class:selecioneo modelqueservirádebaseparaacriaçãoda view.Nesse
caso,suaop çãodeveserpor“Medico";
•Scaffold template:definequaltemplatede viewserácriado.Nestecaso,seleci-
oneaop ção List.Comoconsequência,oMVCcriaráautomaticamenteuma
viewcomumatabelaprontaparademonstrarosregistrosexistentes;
•Reference script libraries:desmarqueessaop ção.Todareferênciadescriptne-
cessáriaparaofuncionamentodoaplicativofoirealizadana Master Page;
87

## Página 98

5.4. Cadêmeumédico:CRUDs CasadoCódigo
•Use a layout master page:essaop çãodeveserselecionadaparacriaruma view
queutilizea Master Pagejádefinidaanteriormente.
Afigura5.5representaesseprocesso.Todasas viewscriadasnoaplicativoapartir
deagoraseguirãoeste template,ondealteraremossomenteaspropriedadesde model
classe Scaffold template.
Figura5.5:AdicionandoumanovaView
Apósclicarnobotão Add,oVisualStudiocriaráeautomaticamenteabriráa view
paraedição.Alistagem 5apresentaocódigogeradoparaa view Index.
Opróximocapítuloserádedicadointegralmenteàapresentaç ãodedetalhes
relacionadosàs viewseàsuaenginepadrão—oASP.NET Razor.Nãosepreocupe
88

## Página 99

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
agoracomasparticularidadesdo Razormencionadas,faremospoucasalteraçõessó
paraterumcadastroemplenofuncionamento.
Listagem 5.5-CódigopadrãogeradopeloMVCpraaview:
@model IEnumerable<CadeMeuMedico.Models.Medico>
@{
ViewBag.Title = %%Index%%;
}
<h2>Index</h2>
<p>
@Html.ActionLink("Create New", "Create")
</p>
<table>
<tr>
<th>
@Html.DisplayNameFor(model => model.IDMedico)
</th>
<th>
@Html.DisplayNameFor(model => model.CRM)
</th>
<th>
@Html.DisplayNameFor(model => model.Nome)
</th>
<th>
@Html.DisplayNameFor(model => model.Endereco)
</th>
<th>
@Html.DisplayNameFor(model => model.Bairro)
</th>
<th>
@Html.DisplayNameFor(model => model.Email)
</th>
<th>
@Html.DisplayNameFor(model => model.AtendePorConvenio)
</th>
<th>
@Html.DisplayNameFor(model => model.TemClinica)
89

## Página 100

5.4. Cadêmeumédico:CRUDs CasadoCódigo
</th>
<th>
@Html.DisplayNameFor(model => model.WebsiteBlog)
</th>
<th>
@Html.DisplayNameFor(model => model.IDCidade)
</th>
<th>
@Html.DisplayNameFor(model => model.IDEspecialidade)
</th>
<th></th>
</tr>
@foreach (var item in Model) {
<tr>
<td>
@Html.DisplayFor(modelItem => item.IDMedico)
</td>
<td>
@Html.DisplayFor(modelItem => item.CRM)
</td>
<td>
@Html.DisplayFor(modelItem => item.Nome)
</td>
<td>
@Html.DisplayFor(modelItem => item.Endereco)
</td>
<td>
@Html.DisplayFor(modelItem => item.Bairro)
</td>
<td>
@Html.DisplayFor(modelItem => item.Email)
</td>
<td>
@Html.DisplayFor(modelItem => item.AtendePorConvenio)
</td>
<td>
@Html.DisplayFor(modelItem => item.TemClinica)
</td>
<td>
@Html.DisplayFor(modelItem => item.WebsiteBlog)
90

## Página 101

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
</td>
<td>
@Html.DisplayFor(modelItem => item.IDCidade)
</td>
<td>
@Html.DisplayFor(modelItem => item.IDEspecialidade)
</td>
<td>
@Html.ActionLink("Edit", "Edit",
new { /* id=item.PrimaryKey */ }) |
@Html.ActionLink("Details", "Details",
new { /* id=item.PrimaryKey */ }) |
@Html.ActionLink("Delete", "Delete",
new { /* id=item.PrimaryKey */ })
</td>
</tr>
}
</table>
Porpadrão,oscaffolddoMVCcriaumatabelacomumacolunaparacadapro-
priedadedomodelo,nessecaso,temosumgridqueirámostrartodososdadosdos
médicos.Nocasodaaplicação Cadê meu Médico,osdadosquedeveremosmostrar
nogriddevemserapenas:Nome,CidadeeEspecialidade.
Modifiqueocódigoda viewIndexremovendoascolunasdesnecessárias,man-
tendosomenteascolunasparaNome,CidadeeEspecialidade. Alistagem 6apre-
sentaocódigoesperado.Reparetambémque,nascolunasCidadeeEspecialidade,
modificamosovalorapresentado.Originalmenteoscaffoldadicionouasproprieda-
desIDEspecialidadeeIDCidade,oqueparaousuárionãofazsentido—paraelea
informaçãonecessáriaéonomereferenteaessasinformações.
Nalistagem 4utilizamosorecurso .Include()doEntityFrameworkpara
carregarosrelacionamentosdomodelo,comissoficafácilnavegarentreosrelacio-
namentosdomodeloeapresentaroutrasinformaçõesaousuário.
Listagem 5.6-Listagemdemédicosmostrandosóosdadosnecessários:
@model IEnumerable<CadeMeuMedico.Models.Medico>
@{
ViewBag.Title = %%Index%%;
91

## Página 102

5.4. Cadêmeumédico:CRUDs CasadoCódigo
}
<h2>Index</h2>
<p>
@Html.ActionLink("Create New", "Create")
</p>
<table>
<tr>
<th>
@Html.DisplayNameFor(model => model.Nome)
</th>
<th>
@Html.DisplayNameFor(model => model.IDCidade)
</th>
<th>
@Html.DisplayNameFor(model => model.IDEspecialidade)
</th>
<th></th>
</tr>
@foreach (var item in Model) {
<tr>
<td>
@Html.DisplayFor(modelItem => item.Nome)
</td>
<td>
@Html.DisplayFor(modelItem => item.Cidade.Nome)
</td>
<td>
@Html.DisplayFor(modelItem => item.Especialidade.Nome)
</td>
<td>
@Html.ActionLink("Edit", "Edit",
new { /* id=item.PrimaryKey */ }) |
@Html.ActionLink("Details", "Details",
new { /* id=item.PrimaryKey */ }) |
@Html.ActionLink("Delete", "Delete",
new { /* id=item.PrimaryKey */ })
</td>
</tr>
92

## Página 103

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
}
</table>
Antesdecompilaroprojetocomoobjetivodetestarofuncionamentoda view,
voltaremosà master pageondeseencontradefinidaaestruturade layoutdoaplica-
tivoeadicionaremosumnovoitemaomenuprincipalparaqueestenosleve,então,
atéocadastrodemédicos.
Paraisso,na Solution Explorer,abraoarquivo“Layout.cshtml”queseencontra
nodiretório Views. NotequenaestruturaHTMLdapágina,possuímosumalista
(<ul>)comaclasse“nav”atribuída.Éjustamentenestalistaqueositensdomenu
devemseradicionados.Comovocêpoderánotar,elejápossuiumlinkparaapágina
inicialdosite.
Alistagem 7mostraocódigonecessárioparaacriaç ãodomenu. Nele,você
utilizaráuma HTML Helperdo Razorquecriaumlinknomomentodarenderi-
zação,ouseja,atag<a>doHTML.Paraqueo helperchamadoActionLinkpossa
funcionarcorretamente,devemosinformar3parâmetros:otextoaserexibidopelo
link,a actionqueseráchamadaporeleeo controlleraoquala actionpertence.
Listagem 5.7-CriaçãodoitemdemenuparaMédicos:
<ul class="nav navbar-nav">
<li class="active"><a href="#">Home</a></li>
<li id="menuMedicos">
@Html.ActionLink("Médicos", %%Index%%, "Medicos")
</li>
</ul>
Agorasim.Aocompilaroprojeto,vocêveráqueaaplicaç ãoexibeumitemde
menuchamado Médicos. Aoclicarnomenu,vocêseráredirecionadoparaaURL
/medicos. Evidentemente,nenhummédicoseráexibidonapágina,umavezque
nãoadicionamosmédicosainda.Oimportanteaquiénotarquejáépossívelvero
títulodapágina,umlinkparacriarnovosmédicoseocabe çalhodatabela(grid).A
figura5.6demonstraapáginaemexecução.
93

## Página 104

5.4. Cadêmeumédico:CRUDs CasadoCódigo
Figura5.6:CadastrodeMédicos
Comojápossuímosnossaprimeira actione viewconstruídas(ondeousuário
poderáveralistademédicoscadastrados),estamosaptosadaropassoseguinte,isto
é,construiroformuláriodecadastrodenovosmédicos.Estateladecadastroestará
disponívelatravésdaURL /Medicos/Adicionar.CombasenestaURLeno CoC
doMVC,sabemosqueonomedenossapróxima actiondeveráser Adicionar.
Assim,noarquivo MedicosControllerna Solution Explorer,adicioneuma
nova Actionchamada Adicionar.Esta actionpossuinaturezaumpoucodiferenteda-
quelaquecriamosnospassosanteriores:alémderetornaruma viewparaocadastro
domédico,utilizaremosdoisnovosrecursoqueo frameworkMVCdisponibiliza—
o ViewBage SelectedList.
Vimosnamodelagemdosistemaqueosmédicospossuememsuasinformações
básicasaCidadedeatuaçãoesuaEspecialidade.NoformuláriodecadastrodoMé-
dicos,essasinformaçõesserãoapresentadasemumComboBox(ouDropdownlist).
NocasodeHTML,oComboBoxérepresentadopeloelemento select.
Podemosutilizaro ViewBagparatransferirdadosdo Controllerparaa View.Ele
éumapropriedadedotipo dynamic,porissopodemoscriarpropriedadesdinami-
camente.Emnossa actioncriamosduaspropriedades,IDCidadeeIDEspecialidade,
cadaumacomalistadeCidadeseEspecialidadesquemaisadianteseráapresentada
aousuário.
94

## Página 105

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
Naspropriedadesdinâmicasda ViewBagretornarmosjáoelementoqueserá
apresentadona View.Paraissoutilizamosohelper SelectList—vocêverámais
sobreosHelpersnopróximocapítulosobre Views.
Alistagem 8apresentaocódigoreferenteà action Adicionar.
Listagem 5.8-Actionadicionar:
public ActionResult Adicionar()
{
ViewBag.IDCidade = new SelectList(db.Cidades, "IDCidade", "Nome");
ViewBag.IDEspecialidade = new SelectList(db.Especialidades,
"IDEspecialidade",
"Nome");
return View();
}
Damesmaformaquefizemosparaadicionara view Index,faremostambém
paracriara view Adicionar,comadiferen ça,entretanto,dequeagoraescolhere-
moso template Create.
Apósefetuaracriação,oVisualStudioabriráautomaticamenteoarquivoda
view. Seucódigodeveráestarparecidocomaqueleapresentadopelalistagem 9.
Noteque,nolugardeumatabelaparalistarregistrosjácadastrados,o template
Creategerouumformulárioparaopreenchimentodosdadosdo model.
Listagem 5.9-ViewAdicionar:
@model CadeMeuMedico.Models.Medico
@{
ViewBag.Title = "Adicionar";
}
<h2>Adicionar</h2>
@using (Html.BeginForm()) {
@Html.AntiForgeryToken()
@Html.ValidationSummary(true)
<fieldset>
<legend>Medico</legend>
95

## Página 106

5.4. Cadêmeumédico:CRUDs CasadoCódigo
<div class="editor-label">
@Html.LabelFor(model => model.IDMedico)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.IDMedico)
@Html.ValidationMessageFor(model => model.IDMedico)
</div>
<div class="editor-label">
@Html.LabelFor(model => model.CRM)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.CRM)
@Html.ValidationMessageFor(model => model.CRM)
</div>
<div class="editor-label">
@Html.LabelFor(model => model.Nome)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.Nome)
@Html.ValidationMessageFor(model => model.Nome)
</div>
<div class="editor-label">
@Html.LabelFor(model => model.Endereco)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.Endereco)
@Html.ValidationMessageFor(model => model.Endereco)
</div>
<div class="editor-label">
@Html.LabelFor(model => model.Bairro)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.Bairro)
@Html.ValidationMessageFor(model => model.Bairro)
</div>
96

## Página 107

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
<div class="editor-label">
@Html.LabelFor(model => model.Email)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.Email)
@Html.ValidationMessageFor(model => model.Email)
</div>
<div class="editor-label">
@Html.LabelFor(model => model.AtendePorConvenio)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.AtendePorConvenio)
@Html.ValidationMessageFor(model =>
model.AtendePorConvenio)
</div>
<div class="editor-label">
@Html.LabelFor(model => model.TemClinica)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.TemClinica)
@Html.ValidationMessageFor(model => model.TemClinica)
</div>
<div class="editor-label">
@Html.LabelFor(model => model.WebsiteBlog)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.WebsiteBlog)
@Html.ValidationMessageFor(model => model.WebsiteBlog)
</div>
<div class="editor-label">
@Html.LabelFor(model => model.IDCidade)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.IDCidade)
@Html.ValidationMessageFor(model => model.IDCidade)
</div>
97

## Página 108

5.4. Cadêmeumédico:CRUDs CasadoCódigo
<div class="editor-label">
@Html.LabelFor(model => model.IDEspecialidade)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.IDEspecialidade)
@Html.ValidationMessageFor(model => model.IDEspecialidade)
</div>
<p>
<input type="submit" value="Create" />
</p>
</fieldset>
}
<div>
@Html.ActionLink("Back to List", %%Index%%)
</div>
Analisandoocódigorecém-criado,épossívelnotarqueoformulárioapresenta
umcampochamado IDMedicoparapreenchimento. Veja,estecamporefere-se
aum identitynobancodedados,ouseja,estevalorserágeradoautomaticamente
pelo GBD (Gerenciador de Banco de Dados) quando chegar a requisição de
gravação.Assim,faremosumapequenaalteraç ãonoHTMLgeradoparaendere çar
este“problema”. Removeremosdaviewtodoocódigoreferenteaessecampono
formulário.Alistagem10apresentaotrechodecódigoquedeveráserremovido.
Listagem 5.10-Códigoquedeveserremovido:
<div class="editor-label">
@Html.LabelFor(model => model.IDMedico)
</div>
<div class="editor-field">
@Html.EditorFor(model => model.IDMedico)
@Html.ValidationMessageFor(model => model.IDMedico)
</div>
Faremos ainda outra pequena alteração no HTML gerado. Utiliza-
remos as propriedades da ViewBag para criar os Combos de nossa
tela. Altere a linha @Html.EditorFor(model => model.IDCidade)
para @Html.DropDownList("IDCidade", String.Empty), e a li-
98

## Página 109

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
nha @Html.EditorFor(model => model.IDEspecialidade) para
@Html.DropDownList("IDEspecialidade", String.Empty).
Pronto. Agoraquepossuímosofomulárioprontoefuncionando,precisamos
gravarosdadosprovenientesdelenobancodedados. Paraisso,éprecisocriara
actionquereceberáum modeljácomosdadosqueousuáriopreencheuutilizandoo
formuláriodaview.Primeiro,énecessáriocompreenderosverbos GETe POSTdo
doprotocoloHTTP.ApesardemaisverbosestaremdisponíveisnoHTTP(DELETE,
OPTIONS,entreoutros),paraanossaaplicaçãodeexemploutilizaremosapenas GET
e POST.
Emlinhasgerais,overbo GETéutilizadoparaobterumrecursodoservidor,
enquantooverbo POSTserveparaadicionarumnovorecurso.Porrecurso,entenda
páginas,imagens,estilos,scripts,dadosetc.
Alistagem 11demostraocódigoda actionquereceberá, emumparâmetro,
o modelpreenchidopelousuáriona view. Alémdevalidaromodeloeadicionar
nobancodedadossenenhumainconsistênciaforencontrada,notequea action
também possui o nomeAdicionar, entretanto, encontra-se decorada com o
atributo HttpPost. Destaforma, peloatributodecorativoda Action, oASP.NET
MVCconseguediferenciarosmétodoscommesmonome.
Listagem 5.11-ActioncomatributoHttpPost:
public ActionResult Adicionar()
{
ViewBag.IDCidade = new SelectList(db.Cidades, "IDCidade", "Nome");
ViewBag.IDEspecialidade = new SelectList(db.Especialidades,
"IDEspecialidade",
"Nome");
return View();
}
[HttpPost]
public ActionResult Adicionar(Medico medico)
{
if (ModelState.IsValid)
{
db.Medicos.Add(medico);
db.SaveChanges();
return RedirectToAction(%%Index%%);
}
99

## Página 110

5.4. Cadêmeumédico:CRUDs CasadoCódigo
ViewBag.IDCidade = new SelectList(db.Cidades, "IDCidade",
"Nome",
medico.IDCidade);
ViewBag.IDEspecialidade = new SelectList(db.Especialidades,
"IDEspecialidade",
"Nome",
medico.IDEspecialidade);
return View(medico);
}
Oatributo HttpPostna actiondizao frameworkMVCqual actioneledeveexe-
cutarquandoarequisiçãoHTTPpossuiroverbo POST.Issoénecessárioporquea
URL /Medicos/Adicionaréutilizadaparamostraroformulárioetambémpara
enviarosdadospreenchidos.Oquemudanasrequisiçõessãoosverbosexecutados
eosvaloresenviadosparaoservidor.
Alistagem 11tambémpossuia actionqueseráexecutadaquandoarequisição
possuiroverbo GETeéelaquemretornaapáginacomoformulário.Apesardeo
atributo HttpGetexistir,elenãoprecisaseradicionadoporque actionssematributo,
porconvenção,sãoconsideradas HttpGet.
Estamosquaseprontosparatestarnossoprimeirocadastro.Antesporém,pre-
cisamosfazerumapequenaalteraçãonoarquivo“Index.cshtml”queestánapasta
Views > Medicos da Solution Explorer.O frameworkMVCcriatodosos templates
utilizandooidiomainglês.Assim,porinércia,elesempreirácriarlinksapontando
para actions Create, Edit, Delete.Comovocêdeveselembrar,substituímos Create
por Adicionar.Assim,precisamossubstituirna viewaschamadaspara Create
por Adicionar.
No arquivo Index.cshtml, encontre o código
@Html.ActionLink("Create New", "Create") e troque por
@Html.ActionLink("Adicionar novo médico", "Adicionar"). O
queestamosfazendoétrocarotextodolink:eemvezdeeleapontarparaaaction
Create,agoraapontaparaaction Adicionar.
Compileseuprojeto,navegueatéapáginadePaíses,ecliquenobotão Adicionar
novo médico.Apágina /Medicos/Adicionarserácarregada;informesóonome
domédicoecliquenobotão Create.Afigura 5.7representaesseprocesso.
100

## Página 111

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
Figura5.7:Validaçãoaoadicionarmédicos
Omédiconãoseráadicionado,jáquecamposobrigatóriosnãoforaminforma-
dos.Lembre-sequenocapítulosobreos modelsadicionamosatributosdevalidação
naspropriedadesdasentidades. Nessemomento,osatributosestãosendoutiliza-
dospeloMVCparafazerautomaticamenteavalidaç ãodosdadosinformadosno
formulário.Essavalidaçãoéfeitapelalinha“if(ModelState.IsValid)”dalistagem11.
Nocasodeummodeloválido,o Entity Frameworkadicionaráomesmoaobanco
dedados.Casoalgumproblemasejaencontradonavalidaç ãodomodelo,a viewserá
101

## Página 112

5.4. Cadêmeumédico:CRUDs CasadoCódigo
apresentadanovamenteparaousuáriocomosdadosanteriormenteinformadose
comasmensagensdavalidação.
Informeosdadosobrigatóriosnoformulário,cliquenobotão Createe,apósa
inclusãodoregistro,vocêseráredirecionadoparaa viewIndex,naqualomédico
recém-adicionadoseráapresentado.
Comainclusãodomédicoconcluída,éhoradeavan çarefazeroformulário
para a alteração dos cadastros. A listagem12demonstra o código dasactions
paraaalteraçãodosmédicos. Sigaospassosapresentadosanteriormenteecriea
View Editar. Lembre-sedeutilizarotemplate Editnacriaçãoda viewefazeras
alteraçõesnoHTMLconformeapresentadasanteriormente. Umadiferen çaéque
depoisdeexcluirocampoIDMedico,ocódigo @Html.HiddenFor(model =>
model.IDMedico)deveseradicionado. A viewdevepossuirtodososdadosdo
modeloemedição—nocasodoIDMedico,ousuárionãoprecisaserexibidoao
usuário,masprecisaestarpresentenoformulário.
Listagem 5.12-
:
public ActionResult Edit(long id)
{
Medico medico = db.Medicos.Find(id);
ViewBag.IDCidade = new SelectList(db.Cidades, "IDCidade",
"Nome",
medico.IDCidade);
ViewBag.IDEspecialidade = new SelectList(db.Especialidades,
"IDEspecialidade",
"Nome",
medico.IDEspecialidade);
return View(medico);
}
[HttpPost]
public ActionResult Editar(Medico medico)
{
if (ModelState.IsValid)
{
db.Entry(medico).State = EntityState.Modified;
102

## Página 113

CasadoCódigo Capítulo5. Controllers:Adicionandocomportamentoanossaaplicação
db.SaveChanges();
return RedirectToAction(%%Index%%);
}
ViewBag.IDCidade = new SelectList(db.Cidades, "IDCidade",
"Nome",
medico.IDCidade);
ViewBag.IDEspecialidade = new SelectList(db.Especialidades,
"IDEspecialidade",
"Nome",
medico.IDEspecialidade);
return View(medico);
}
Apósacriaçãodas actionseda view Editar,sónosrestarealizarmaisumaalte-
ração. Elaprecisaserfeitana view Index. Cadalinhadatabelaquerepresentaum
médicocadastradopossuiumlinkparasuaEdiçãoeExclusão.Vamosprimeiroalte-
raracriaçãodolinkparaedição.Altereocódigo @Html.ActionLink("Edit",
"Edit", new { / * id=item.PrimaryKey */ }) paraocódigocorretoque
direcionaparaa action Editar: @Html.ActionLink("Editar", "Editar",
new { id=item.IDMedico }).
Feitoisso,compilesuaaplicaçãoetesteaalteraçãodoregistrorecém-criado.
ParafinalizarasoperaçõesdocadastrodeMédicos,sórestaacriaç ãoda action
paraaexclusãodosregistros.Alistagem 13representaocódigoda action Excluir.
Ocódigoémaissimplesdoqueosapresentadosanteriormente: a actionretorna
trueoufalsedeacordocomoresultadodaexclusão.Essesvaloresserãoutilizados
nopróximocapítulo,assimcomoachamadaparaa action Excluirqueseráfeita
porAjaxnocapítulosobre Views.
Listagem 5.13-
:
[HttpPost]
public string Excluir(long id)
{
try
{
Medico medico = db.Medicos.Find(id);
db.Medicos.Remove(medico);
db.SaveChanges();
103

## Página 114

5.4. Cadêmeumédico:CRUDs CasadoCódigo
return Boolean.TrueString;
}
catch
{
return Boolean.FalseString;
}
}
Vimosatéaquiasoperaçõesparaocadastrodemédicos.Utilizeoquefoiapre-
sentadoatéomomentoparacriartambémoscadastrosdeCidadeseEspecialidades.
AproveitetambémparatraduziroselementoscriadoseminglêspeloMVCnas Views
autogeradas.Apartirdeagoraveremoscommaisdetalhesosrecursosdisponíveis
nas viewsdoMVC.
104

## Página 115

Capítulo6
Views:interagindocomousuário
Nocapítulo4,vocêteveaoportunidadedeseaprofundarnotema“models”.Lá,você
pôdeentenderumpoucomaissobrecomoo frameworkMVCtrabalhacomfontes
dedados,principalmenteutilizandooORMdaMicrosoft—o Entity Framework.
Assim,vocêpôdecompreenderaimportânciadaletra“M”noacrônimoMVC.
Emseguida,vocêfoiapresentadodeformamaisíntimaaogrupodeconceitos
envolvidosnautilizaçãodos controllers.Atravésdeexemplospráticosecomexplica-
çõesdiretasemcimadecadalinhadecódigo,procuramostornarevidenteo“peso”
impostopelaletra“C”nocontextodeaplicaçõesASP.NETMVC.
Assim,apósentenderaformacomquepodemosnosconectaraosbancosdeda-
doseposteriormenteimporcomportamentosàsaplicações,échegadoomomento
emquepoderemosentenderdeformamaisclaracomoo frameworkendereçaore-
sultadofinaldaintegraçãoentreasduasetapasmencionadasnosdoisparágrafosan-
teriores,istoé,aexibiçãodosdadosparaousuáriofinal.Éclaroqueestamosfalando
daletraMVC,querefere-seàpalavra Views(emportuguêsbrasileiro,“Visões”).

## Página 116

6.1. Visões?! CasadoCódigo
6.1 Visões?!
Visões(oucomoagrandemaioriadosdesenvolvedorespreferechamar— views)são
oselementosqueconstituema“pontaexternado iceberg”nasaplicaçõesASP.NET
MVC.Aassociaçãoépertinente,umavezquesãoosponteirosdastaisestruturas
degeloquepodemservistasaolhonusemquesequerpossaimaginaracomplexa
estruturaquehápordebaixod’água.Omesmoocorrecomas viewsemaplicações
ASP.NETMVC.
Comojámencionamosanteriormentenestelivro,oprincipalobjetivodo fra-
meworkMVCésepararresponsabilidades.Assim,temosbasicamentetrêscamadas,
sendoqueumadelas(as views)sãodedicadasexclusivamenteàexibiçãodeinforma-
çõesaousuáriofinal.Nãoháprocessamentoaníveldeservidornestacamada,jáque,
paraisso,temosos controllers.Deigualforma,acessosadadosnãodevemserreali-
zadosnestacamada,umavezquepossuímosos modelsparatal.Assim,restaa view
recebermassasdedadosjáprontasesimplesmenteexibi-las.Afigura 6.1apresenta
ofluxodeoperaçãoatéa view.
Figura6.1:OfluxodeoperaçãodoframeworkMVCatéaview.Fonte: http://www.
arrangeactassert.com/
Levando-seemconsideraçãoosconceitosapresentadosnosparágrafosiniciais
destase ção,umaperguntaobrigatoriamentedeveserrespondida:seafun çãodas
viewséunicamenteexibirdadosjáformatados,comopodemosexibirtaisinforma-
ções? Nasseçõesseguintes,tentaremosresponderprincipalmenteaestaquestão.
Evidentemente,nestecontexto,muitosnovosconceitosserãoapresentados.
6.2 Conceito de“Engenho de renderização”
Asfamosas view engines ousimplesmente“engenhosderenderização”,sãomeca-
nismospresentesemtodasasversões frameworkASP.NET.Aquichamamosde view
106

## Página 117

CasadoCódigo Capítulo6. Views:interagindocomousuário
engineomecanismointernodaplataforma(emnossocaso,ASP.NET)quepossibilita
atransformaçãodediretivasexclusivamentedeservidoremcódigoHTML,legível
pelonavegador,aindano containerwebparaposteriorexibiçãoaousuáriofinal.
Aideiafundamentalnestecasoéadeproporcionaraodesenvolvedoroaltopo-
derprogramáticooferecidopelaslinguagensdeservidor—comoastagsdoscom-
ponentesdeservidordoASP.NET,porexemplo—epassararesponsabilidadede
geraçãodocódigoobjetono browserparao containerweb.
6.3 ASPX ouASP.NETRazor?
JámencionamosofatodeASP.NETsetratardeumaplataformaenãoumalingua-
gemdeprogramação. Justamenteporestemotivo,todasastecnologiasagrupadas
naplataformarecebemoprefixo“ASP.NET”,comoASP.NETMVC.
Falandoespecificamentede view engines,atualmenteencontram-sedisponíveis
naplataformaASP.NETduasop çõesdelas: ASP.NET(dosfamososarquivoscom
extensão *.ASPX)eASP.NETRazor(estaúltima,maisrecente). Assim,aocriar
umnovoprojetowebutilizandoqualquerdastecnologiasdisponíveisnaplataforma
ASP.NET,odesenvolvedorpoderáoptarpelautilizaçãodaquela view enginequeme-
lhoratendeàssuasnecessidades.
Éevidentequecadaumadas view enginesmencionadaspossuisuaspeculiarida-
desecaracterísticasintrínsecasqueatornaadequadaaosdiferentestiposdeprojetos.
Muitoemborasejapossívelutilizara view engineASPXemprojetosASP.NETMVC,
estenãoéopadrãorecomendadopelo framework.Assim,comoestelivromantém
seufoconoestudodaversão4do frameworkMVC,ecomoparaestaversãoa view
enginepadrãoéaASP.NETRazor,naspróximasse çõesdestecapítulonosconcen-
traremosnaapresentaçãodasprincipaiscaracterísticaserecursosdisponíveisneste
motordevisualização. Porinércia,deverãoficarevidentesasfuncionalidadesque
fizeramcomqueaMicrosoftnãoapenasincorporasseorecursoao frameworkcomo
fizessedelea view enginepadrão.
6.4 ASP.NETR azor
AversãofinaldoASP.NETMVC3(entregueaomercadoemJaneirode2011)trouxe
umasériedenovoseimportantesrecursos.Vocêpodeencontrararelaç ãodenovi-
dadestrazidaspelaversãoatravésdolink:
http://www.asp.net/mvc/mvc3#overview
107

## Página 118

6.5. Diferençasnaprática CasadoCódigo
Dentreestasnovidades,aquelaquerecebeumaiordestaqueequecontribuiuem
grandeescalaparaaado çãodo framework,foiaintroduçãodanova view engine—
aASP.NETRazor.
Diferentementedoquevocêpodeestarpensando,ASP.NET Razornãoéuma
linguagemdeprogramação.É,sim,umanovaformadeestruturar viewsquepreci-
samdealgumapor çãodecódigoprocessadanoservidordeaplicaç ão.
Costuma-sedizerque Razoréummodelodeescritadecódigopornãopossuir
umalinguagempredefinida. Épossívelutilizaromodelodeprogramaç ãoofere-
cidopelo Razorutilizandoasduasprincipaislinguagensda.NET framework: C#
ouVB.Nocaso,arquivos RazorestruturadoscombaseemC# possuemaextensão
“*.cshtml”,enquantoarquivosestruturadoscombaseemVBpossuemaextensão
“*.vbhtml”.
Comovocêjápôdeperceber,emprojetosASP.NETMVC,as viewspossuema
funçãodeexibirdadosprocessadospelos controllers.Capturarvaloresprovenientes
destesdos controllerséumatarefaamplamentesimplificadapelo Razor.
6.5 Diferenças na prática
ParaquepossamosapresentarosconceitoschavesrelacionadosaoRazorqueo
diferenciamdasdemaisabordagens,apresentaremosdoistrechosdecódigo,que
realizamrigorosamenteamesmaoperaç ão: repetiritensemumalistafictíciavia
foreach.Alistagem 1apresentaotrechodecódigoescritocomASPX.
Listagem 6.1-RepetindoitensemumalistacomASPX:
<% foreach(var item in itens) { %>
<span>
<%: item.ValorUnitario %>
</span>
<% } %>
A listagem2a seguir apresenta um trecho de código que realiza a mesma
operaçãorealizadapelocódigoda 1,mas,utilizando Razor.
Listagem 6.2-RepetindoitensemumalistacomRazor:
@foreach(var item in itens) {
<span>
108

## Página 119

CasadoCódigo Capítulo6. Views:interagindocomousuário
@item.ValorUnitario
</span>
}
Estestrechosdecódigossãodecisivosparaapresentarmosalgumasconceitosini-
ciaisimportantesacercada view engine Razor.Aprimeiraobservaçãopertinenteem
relaçãoàsabordagenséadiferen çaquedemarcaosblocosdecódigo.Enquanto views
queutilizamASPXutilizamdelimitadores“<%%>”,Razorutilizaapenasamarcação
de“@”.Outraobservação(nãomenosimportante)équeomotorderenderizaç ão
do Razoré“inteligente”.Percebaque,enquantoASPXtemumaseparaçãoexplícita
entresuastagseasHTML, Razornãoapossui.Issoocorreporqueomotorderende-
rizaçãodo RazorseparadeformaautomáticaHTMLdecódigoC# (ouVisualBasic
quetambémésuportado,éimportantequesediga).
Evidentemente,estanãoéaúnicaformadeseescrevercódigo Razor.Existem
casosemqueblocosdeinstruçõesdevemseragrupadoemblocosmaiores(multili-
nhas)paraseconseguirumamelhororganizaç ãodocódigona view,porexemplo.
Paraestescasos,poderíamosutilizarumaabordagemconhecidacomo“Blocode
múltiplaslinhas”.Casoumalinhasejasuficienteparaexpressarumcomportamento
atravésdoRazor,ométodoconhecidocomo“inline”podeserutilizado.Alistagem
3apresentaadiferen çaentreasabordagens.
Listagem 6.3-MultilinhasversusInline:
@{
//Multi-linhas
ViewBag.Title = "Teste de layout";
var Data = DateTime.Now.DayOfWeek;
string StringConcatenada = "Hoje é '" + Data.ToString()
+ "'. Seja bem vindo(a)!";
}
<!-- Inline -->
<h2>@StringConcatenada</h2>
Como você pôde perceber, com a utilização do Razor é possível declarar
variáveiseinstanciarobjetos,emuitomais.Épossíveltambém,conformevimosna
listagem2,criarestruturasderepetiç ãoquepermitemaodesenvolvedornavegar
entreestruturasdedadossimples(arrays,porexemplo)oucomplexas(dicionários
dedados,listasmulti-valoradasetc.).SetodaaestruturaC#/VBésuportadana view
109

## Página 120

6.6. Helpers?! CasadoCódigo
queutiliza Razor,estruturasdetomadasdedecisão(falamosif/else,switch/casee
suasvariações)tambémassão—verlistagem4.Tudoissoutilizandonãoapenaso
modelodeprogramaçãoorientadoaobjetos,jáfamiliarparaquemtrabalhacom
.NET,masprincipalmente,utilizandoamesmasintaxe.
Listagem 6.4-Verificandovalordeentradanaviewcomif/else:
@{
ViewBag.Title = "Teste de layout";
var Data = DateTime.Now.DayOfWeek;
string StringConcatenada = Data.ToString();
}
<!-- Verificando o dia retornado -->
@if (StringConcatenada == "Friday") {
<h2>Sexta-feira</h2>
}
else
{
<h2>Outro dia qualquer da semana.</h2>
}
TrabalharcomASP.NETRazorésimplesenãoexigedodesenvolvedor(desig-
ner)conhecimentosadicionais. Bastaqueseentendaomodelodetrabalho. Nas
próximasseçõesapresentaremosalgunsoutrosaspectosfuncionaisdisponibilizados
pelatecnologia.Vocêiráadorar!
6.6 H elpers?!
Nãohádúvidasentreaquelesqueutilizam Razoremseudiaadiaquantoàutilidade
dos helpersnocontextodasaplicações.
Acriaçãode helperséumrecursoqueseencontradisponívelnocontextodo
ASP.NETRazordesdeaprimeiraversão.Inicialmente, Razorpermitiaqueos helpers
apenasretornassem stringsparaas views.Felizmente,estarealidademudoue,hoje,
podemoscriar helpersqueretornampor çõeseHTMLcomobjetosatrelados.Issodá
aodesenvolvedormaiorpodere,consequentemente,maiorrobustezàs views.
Deformadireta,sãoos helpersquepermitemcriaroperaçõesecomportamen-
tosespecíficosquepoderãoserreutilizadosaolongodetodaaaplicaç ão.Considere
110

## Página 121

CasadoCódigo Capítulo6. Views:interagindocomousuário
novamentenossoprojeto“Cadê meu médico”. Imagine,porexemplo,quequere-
mosexibiraolongodetodaaaplicaç ãoum boxdepublicidade,ondeexibiremosos
dois bannersmaisrecentes.Comoobjetivodedesacoplaroscomponentesda viewe
reutilizaremoutrasaplicações,inclusive,poderíamoscriarum helper“BannersPu-
blicitarios”.
Antesdecriarmosnosso helperdeexemplo,éimportantesaberqueexistemdois
modelosparaacriaçãode helpers.Asaber,naprópria viewondeeleseráutilizado
oudeformaqueelepossaserreaproveitadoaolongodemúltiplas views. Comoo
objetivoprincipaldos helperséservircomomecanismode refactoringdecódigosna
view,apresentaremosnoexemploaseguirapenasasegundaabordagem.
Criandoohelper“BannersPublicitarios"
Comoprojeto“Cadê meu médico”emexecução,váatéa Solution Explorereso-
breonomedoprojeto,cliquecomobotãodireito.Selecioneasop çõesAdd > Add
ASP.NET Folder > App_Code. Claro,vocêdeverárealizaresteprocedimento
apenasseodiretóriomencionadonãoexistiremsua Solution Explorer.Odiretório
“App_Code”éoutradasconvenções(CoC)implementadaspeloframeworkASP.NET
MVCparadiretórios.Aoadicionarumaclasseouarquivo Razor,oprojetoMVCen-
tenderáqueoreferidoarquivotrata-sedeumscriptquepoderáserreutilizadoem
outraspartesdaaplicaçãocomoumcódigoagregadodefun çãoespecífica(comoé
ocasodos helpers).
Nopassoseguinte,sobreodiretório“App_Code”,cliquecomobotãodireitoese-
lecioneasequênciadeopções:Add > New item.Najanelaqueseabrir,selecione
aopção MVC 4 View Page (Razor)eanomeiecomo“BannersPublicitarios.cshtml”,
conformeapresentaafigura 6.2.
111

## Página 122

6.6. Helpers?! CasadoCódigo
Figura6.2:AdicionandooarquivodohelperBannersPublicitarios
Antesdeirmosaoscódigos,relembremos:oquefaremosaquiéumpainelque
exibe bannerspublicitários.Paraqueistopossaserdinâmico,adicionareiumanova
tabelaaonossobancodedadoschamada“BannersPublicitarios”eapreenchereicom
doisregistros:umpara“ConioSoluçõesemTecnologia”comsuarespectivaimagem
eoutro“CasadoCódigo”tambémcomsuaimagem. Sóentãopartiremosparaa
codificaçãodenosso helper.
OSQLparaacriaç ãodatabelaeosrespectivos insert’ssãoapresentadospela
listagem5.
Listagem 6.5-ScriptparacriaçãodatabelaBannersPublicitarioseseusrespectivos
inserts:
CREATE TABLE BannersPublicitarios
(
IDBanner BIGINT IDENTITY NOT NULL,
TituloCampanha VARCHAR(60) NOT NULL,
BannerCampanha VARCHAR(200) NOT NULL,
LinkBanner VARCHAR(200) NULL,
PRIMARY KEY(IDBanner)
);
112

## Página 123

CasadoCódigo Capítulo6. Views:interagindocomousuário
INSERT INTO BannersPublicitarios
(TituloCampanha, BannerCampanha, LinkBanner) VALUES
('Campanha Conio ', 'logo-conio-cademeumedico.png','http://conio.com.br')
INSERT INTO BannersPublicitarios
(TituloCampanha, BannerCampanha, LinkBanner) VALUES
('Campanha Casa do Código', 'banner-cdc-cademeumedico.png',
'http://casadocodigo.com.br')
Os bannersqueaparecemnosdois insertsencontram-senoprojetocompletono
GitHubevocêpodeutilizá-losparacompletaroexemplo.
Agoraquepossuímosnossainfradebancodedadosmontada,podemosvoltar
aoVisualStudioparaimplementar,defato,o helperqueexibiráestasinformaçõesna
aplicação.Apósatualizaromodelodaaplicaç ão(sim,issoéprecisoparaqueo Entity
Framework“enxergue”anovatabela),abraoarquivo“BannersPublicitarios.cshtml”
localizadoem“App_Code”.Substituaoconteúdogeradodeformaautomáticapelo
VisualStudiopeloapresentadopelalistagem 6.
Listagem 6.6-ActionqueretornaemViewBagsosbannerspublicitários:
@using CadeMeuMedico.Models;
@helper RetornaDoisBannersMaisRecentes() {
var bd = new CadeMeuMedico.Models.EntidadesCadeMeuMedicoBD();
var banners = bd.BannersPublicitarios.
OrderByDescending(b => b.IDBanner).Take(2);
<div style="width:100%; text-align:left; border:1px
solid #efefef; padding:10px; display:inline-block;">
@foreach(var b in banners) {
<div style="width:125px; height:125px;
float:left; margin-right:10px;">
<a href="@b.LinkBanner">
<img src="~/Uploads/Banners/@b.BannerCampanha"
title="@b.TituloCampanha" />
</a>
</div>
}
113

## Página 124

6.6. Helpers?! CasadoCódigo
</div>
}
Algunspontosimportantesrelacionadosaocódigoapresentadopelalistagem 6:
• Utilizamosadiretivausingdiretoda view.Lembre-se,aquiéprogramaçãoC#
daformacomovocêjáconhece.Oque Razorfazépossibilitartalmecanismo
emuma view.Nuncaédemaislembrar;
• Atravésdadiretiva“@helper”informamosaoframeworkqueotrechodecó-
digoaseguirdeverásecomportarcomoum helper;
• Nasequência,crioumainstânciadomodelodedados,buscoosdoisbanners
maisrecenteseexibojánaestruturaHTMLcom Razor.
Issoposto,resta-nosapresentaraformaatravésdaqualinvocamoso helperem
nossaaplicação. Antesdeapresentarmosocódigo,entretanto,éprecisoentender
que,umavezcriadodaformacorreta,o helperpoderáserinvocadoemqualquer
parteda viewdaaplicação(views comunsou master pages). Ocódigoqueinvoca
o helperrecém-criadopodeservisualizadoatravésdalistagem 7. Pararealizara
demonstração,estamosinvocandoo helper“BannersPublicitários”naview“Index”
do controller“Home”.
Listagem 6.7-Invocandoohelperdebannerspublicitários:
@BannersPublicitarios.RetornaDoisBannersMaisRecentes();
Notequeachamadaésimplesdeserrealizada. Bastainformaronomedoar-
quivo helper(nocaso“BannersPublicitarios”)e,nasequência,invocarométodo
“RetornaDoisBannersMaisRecentes()”.Issoautomaticamentenosdizqueumhelper
podeimplementarváriosmétodos. Emnossoexemplo,poderíamostertranquila-
mente,umsegundométodochamado“RetornaSeisBannersMaisRecentes()”etc.O
resultadogeradopelaimplementaçãodeste helperpodeservisualizadoatravésda
figura6.3.
114

## Página 125

CasadoCódigo Capítulo6. Views:interagindocomousuário
Figura6.3:Helperincorporadoaviewprincipaldaaplicaç ãoexemplo
Umaobservaçãosefaznecessárianesteponto,antesdeprosseguirmos: Antes
quevocênoscrucifiqueporestarmosrealizandoumacessoaobancodedadosdire-
tamenteda view,éimportanteentenderquetalprocedimentofoirealizadoapenas
parasimplificaroprocesso,facilitandooentendimentodoconceitoquedesejamos
passar.Valeobservaraquiqueomodeloidealseriaretornarosdadosatravésdeum
controllere,aísim,comosdadosjádisponíveis,navegarentreelesatravésda view
utilizando Razor.
Helpersnativos
Aindasobreos helpers,éimportantenotaroseguinte: existemaquelesperso-
nalizados(criadossobdemanda,aexemplodoquefizemosnotópicoanterior)e
existemoshelpersnativosdo framework,quepodemserutilizadosparaotimizaral-
gumasoperaçõescom views.Vocêjáestáemcontatocomelesdesdeoiníciodeste
livroetalvezaindanãosaiba.Paraexemplificarsuautilizaç ãoeimportância,vamos
considerarnovamentealistagem 5.
Se você é um bom observador, por certo percebeu que o formulá-
rio foi gerado basicamente através de um componente “@Html”. @Html
115

## Página 126

6.6. Helpers?! CasadoCódigo
é umhelper nativo que encapsula a criação de componentes HTML atra-
vés de código comRazor. O que queremos dizer com isso é que, quando
você escreve a linha @Html.ActionLink("Edit", "Edit", new { / *
id=item.PrimaryKey */ }),porexemplo,vocêestádizendoaomotorderen-
derizaçãodo Razorqueeledeverárealizarum renderparaatag <a>doHTMLem
tempodeexecução.
Muitoemboravocênãoprecisenecessariamentedestes helpersparaconstruir
suas views(sim,vocêpodeutilizarHTMLpuroeutilizar Razorapenasparapegaras
informaçõesprovenientesdocontroller),aoutilizaros helpers Razorépossívelobter
ganhosprincipalmenteemduassituações:
•Quandomudançasestruturaisocorrerem:paramuitostiposdeprojetos,o
modeloderotaspadrãonãoendere çaasdemandas.Assim,aoadicionaruma
rotapersonalizadaparasuaaplicação,porexemplo,nocasodea viewestar
estruturadacom helperscomoo@Html,deformaautomáticao frameworké
capazdeajustaroslinksdasaplicações.
•Linguagemmaisfamiliarparadesenvolvedoresescreverem views:HTML
é,deformageral,maisnaturalpara designersdoquepara desenvolvedores.
Comoanomenclaturaparaautilizaç ãodos helpersémaispróximadoC#,o
processodeescritade viewsparadesenvolvedoresacabasendomaissuave.
Deformageral,opre çoasepagarpelousoexcessivode helpersnas viewséasin-
gelaperdadedesempenho,umavezque,aofazê-lo,colocamosumacamadaamais
deprocessamentosobreoprocessoderenderizaç ão(lembre-se, Razoréprocessado
noservidor).
Estetipode helperpodeaindaserestendido(sim,vocêpodecriarsuasextensões)
atravésdosextension methods,recursodisponívelno.NET frameworkdesdeaversão
3.5.Vocêpodeencontrarumaboaleituraacercadissoatravésdestelink(eminglês):
http://bit.ly/15Zr9cs.
Valemencionar,ainda,queexisteumagrandequantidadede helpersjáprontos,
querealizamdiferentestarefas,disponíveisdeformagratuitanorepositóriopúblico
doNuGet.Dentreosmaisbaixados,podemoscitar:integraç ãocomTwitter(a.k.a.,
Twitter.Goodies),Facebook,PayPaleAmazon.Oprocessodeinstalaç ãodestes hel-
persjáéconhecidoporvocê,umavezquesegueomesmopadrãoimpostopelo“Li-
braryPackageManager”(NuGet)doVisualStudio,apresentadonoscapítulosinici-
aisdolivro.
116

## Página 127

CasadoCódigo Capítulo6. Views:interagindocomousuário
Parainvocá-lo,vocêdeveráseguiromesmopadrãoapresentadopornósno
exemplodacriaçãoeutilizaçãodo helper“BannersPublicitarios”. Aliás,esteéum
bommomentoparatreinar!VáatéorepositóriodoNuGetatravésdoVisualStudio,
busquepelohelper“Twitter.Goodies”einstale-o.Issofeito,adicione-oaumaview
qualquerdoprojetodeexemploevejaoresultado“mágico”daintegração.
6.7 Algumas outras v antagens
Evidentemente,utilizaruma view enginepropostapelaMicrosofttemsuasvantagens
(sejaASPXou Razor).Existemrecursosdisponíveisnelasquenãorecebemgrande
atençãoporpartedamaioriadosdesenvolvedoresmasque,seutilizadosdaforma
correta,podemacarretaremganhodeprodutividade,melhoraraqualidadedocó-
digoe,ainda,melhoraraperformancedaspáginas. Aseguirdiscutiremosalguns
destesaspectos.
Recursosparaexplicitarcaminhos(path’s)
Sevocêjátrabalhoucomwebemqualquernível(enósimaginamosquesim),
comcertezajáconstatouquedeterminarcaminhosdearquivosparaasaplicações
nãoéládascoisasmaissimples.Issoocorreporalgunsfatores.Porexemplo,deter-
minadosprovedoresde hostparaaplicaçõeswebbloqueiamautiliza çãodorecurso
de parent pathporquestõesdeseguran ça.Dessaforma,oscaminhosdevemserin-
formadosdeformaabsolutaenãorelativa.Oproblemanestecasoéquecomoaapli-
caçãoédesenvolvidalocalmenteeoscaminhoslocaispodemserdiferentesdaqueles
utilizadospeloservidorweb,aorealizarapublicaç ãodaaplicaçãonoambientere-
moto,écomumencontraraocorrênciadepáginascomreferênciasquebradas.Em
aplicaçõesgrandes,issoacabatornando-seumproblemacomplexodeserresolvido.
Alémdisso,utilizarcaminhosrelativosemaplicaçõesdegrandeportequepos-
suemmuitosdiretóriosaninhadospodeserumatarefacomplexa,quetomamuito
tempodemanuten çãodocódigo.
Reconhecendoestadificuldade,aMicrosoftpropôsummodeloextremamente
funcionaleelegantepararealizarestatarefaemsuas view engines. Paraqueuma
referênciaadeterminadoarquivopossaserrealizada,bastaadicionarosímbolo“~”
(til)noiníciodocaminhoabsoluto.Destaforma,paraumcaminhoabsoluto“/Uplo-
ads/Imagens/”teríamosumanovaespecificaçãodestemesmocaminhodaseguinte
forma:“~/Uploads/Imagens”. Aoassimfazer,estamos“dizendo”aoIISque,inde-
pendentedodiretórioatual,eledevedevebuscarorecursoinformadoapartirda
117

## Página 128

6.7. Algumasoutrasvantagens CasadoCódigo
raizatéopontoespecificado.Simples,não?!
Renderizaçõesparciais
Quandoiniciamosacriaçãodaaplicação“Cadê meu médico?”,comovocêdeve
selembrar,umadenossasprimeirasprovidênciasfoiadecriarapáginamestra,co-
nhecidaentreosprogramadores/designerscomo master page.Estapáginafoicriada
comoobjetivodeservirdepadrãovisualparatodasasdemais views,quecarrega-
riamseusconteúdosdentrodeumaáreaespecificada master page. Adiretivaque
possibilitouarealizaçãodestamágicafoia“@RenderBody()”.Certo?!
Nosentidodedesacoplaraindamaisa master page(vocêselembradahistória
do“dividirpraconquistar"?),encontra-sedisponívelnas view enginesdaMicrosoft
umrecursoconhecidocomo“renderizaçõesparciais”.
Aideiacomesterecursoéquevocêrenderizepor çõesespecíficasdecódigoem
pontosdistintosda master page. Imagine,porexemplo,quesejaimportantequeo
menudaaplicaçãosejacarregadodeformaassíncronaenquantoorestanteda view
sejacarregadonoprimeiro post.
Vocêpoderiautilizaradiretiva“@RenderSection()”ou“@RenderPartial()”para
buscaruma view parcialquecarrega(deformaassíncronacomjQuery,porexemplo)
seumenu. Autilizaçãode“@RenderPartial()”jáfoidemonstradanestelivro,no
capítulo3.Adiferen çabásicade“@RenderPartial”para“@RenderSection”équea
primeiratemopoderderenderizaruma viewparcialcompleta,easegundarenderiza
seçõesespecificas.Para“@RenderPartial”,vocêdeveráespecificaraviewparcialque
serárenderizadanaqueleponto.
Agregaçãoeminificaç ão
Nosdiasatuaisécomumqueumaaplicaç ãowebpossuamilharesdelinhasde
códigoJavaScript,CSS,XMLeafins.Diariamentenoscercamosde pluginsparaoti-
mizartarefaseproporcionaraousuáriofinalmaiorresponsividade.
Éclaroque,quantomaioréaquantidadedecódigodestanaturezaemumaapli-
cação,invariavelmente,maiscomprometidaestaráaperformancedaspáginas.Desta
forma,novamenteaMicrosoftpropôsumrecursointeressanteparaminimizareste
problema:trata-sedaagregaçãoeminificação.
Jáquepararealizararenderizaçãoosmotoresrealizamaverificaçãodoarquivo
fonte,linhaalinha,aideiabásicaéqueopróprioservidordeaplicaç ãosejacapaz
derealizar,emtempodeexecução,aremo çãodaquiloquepodeserdesprezadosem
118

## Página 129

CasadoCódigo Capítulo6. Views:interagindocomousuário
comprometeroresultadofinal.Estamosfalandodeespaçosembranco,comentários
euniãodaslinhas(minificaç ão),assimcomo,ajun çãoemumúnicoarquivoem
memória(bundle)detodososrecursosdestetipo(agrega ção).
Paraqueestaideiatorne-semaisclara,nadamelhorqueumexemplo,nãoé
mesmo? OexemploqueapresentareiaseguirfoiretiradodoblogoficialdoScott
Guthrieeestádisponíveltambématravésdolink: http://bit.ly/19I5ODr.
Imagineque,emseuprojeto,vocêpossuia solution explorercomumasériede
arquivosCSS(conformeilustraafigura 6.4),todoselesutilizadosporsuaaplicaç ão.
Figura6.4:SolutionexplorerapresentaosarquivosCSS
No modelo deweb page tradicional, para que estes arquivos possam entrar
ematividadeéprecisoquehajaumareferênciamanualparacadaumdeles,como
ilustradoatravésdalistagem 8.
Listagem 6.8-Referenciandoosarquivosdeformamanualemumaview:
<link href="~/styles/reset.css" rel="Stylesheet" />
<link href="~/styles/styles.css" rel="Stylesheet" />
<link href="~/styles/content.css" rel="Stylesheet" />
<link href="~/styles/globals.css" rel="Stylesheet" />
<link href="~/styles/forms.css" rel="Stylesheet" />
<link href="~/styles/menu.css" rel="Stylesheet" />
Muitoemboraestaabordagemfuncioneperfeitamente,oproblemaevidenteestá
119

## Página 130

6.8. Mobilidade:Suaconsultademédicosemdispositivosmóveis CasadoCódigo
nofatodeque,sequencialmente,sãorealizadasseisrequisiçõesaoservidordeapli-
cação.Nãoéprecisopensarmuitoparaentenderquemilhõesdeacessos—quando
falamosemperformanceésemprebomimaginarseaestruturaatualsecomportaria
bemcommilhõesdeacessos—requisitandoseisarquivostodasasvezesébempior
queumarequisição,certo?
Nestesentido,aoconstruirmos viewscom RazorouASPXpodemossimples-
mentefazerdaseguinteforma(listagem 9).
Listagem 6.9-Modelodereferenciacontemplandoagregaçãoeminificação:
<link href="~/styles" rel="Stylesheet" />
Quandoa view RazorouASPXencontrarestemodelodereferência,oqueela
(framework)faráéverificartodososarquivosCSSdentrododiretórioapontado
(nestecaso“styles”),combiná-los,minificá-lose,nasequência,devolverumares-
postaHTTPdeumúnicoarquivoCSS.Assim,aoinvésdeseischamadasseremre-
alizadasjuntoaoservidor,estenúmerocaiparaapenasumachamada.Legal,não?!
6.8 Mobilidade:Sua consulta de médicos em dispo-
sitivos móveis
Noiníciodestelivro,falamosumpoucosobrealgumasdasprincipaisnecessidades
dawebatual.Comovocêdeveselembrar,dentreosprincipaisaspectosmenciona-
dosnaquelaocasião,encontrava-sea“mobilidade”.Defato,aplicaçõesqueadaptam
seuscomportamentosdeacordocomodispositivomerecemumpontinhoamais
noquesitoqualidade,hajavistaapopularizaç ãodos smartphonese tablets.
AoestruturaraplicaçõesutilizandoASP.NETMVC(apartirdaversão4)você
podeutilizarrecursosnativosparaaconstruç ãode viewsquerespondamdeforma
adequadaparadispositivosmóveis.Alémdisso,sevocêutilizaum frameworkcomo
aquelequeestamosutilizando(TwitterBootstrap)paraaestruturaç ãovisualdaapli-
caçãoexemplo“Cadê meu médico?”,poderáseservirtambémdeformanativa,deste
tipoderecurso.Destaforma,apresentaremosaseguiraslinhasgeraisparaquepos-
samosestruturarnossasaplicaçõesparafuncionaremdeformaadequadaindepen-
dentedodispositivoexecutor.Claro,utilizaremosaaplicaç ão“Cadê meu médico?”
comobaseparaisso.
120

## Página 131

CasadoCódigo Capítulo6. Views:interagindocomousuário
Bootstrapcomoplataformademobilidade
Jáapresentamosformalmenteháalgunscapítulos(quandocriamosnossapri-
meiraaplicaçãoMVC)oTwitterBootstrap.Comoeste frameworkfoiescolhidopor
nósparanosajudaracomporoselementosvisuaisdaaplicaç ão“Cadêmeumédico?”,
faztodosentidofalarsobreoseuaspecto mobile.
Atualmente,oTwitterBootstrapencontra-senaterceiraversão.Muitoembora
hojeo frameworkofereçasuportecompletoeirrestritoàmobilidade,nemsempre
foiassim.Aprimeiraversãoemnadacontemplavamobilidade.Nasegundaversão,
algunscomponentesjásuportavamaautoadequação.Hoje,comooprópriotimedo
Bootstrapgostadeafirmar,“Amobilidadevemprimeiro.(Bootstrap is mobile first.)”.
Agrandeperguntaaquié: comoépossívelfazercomqueuma viewseajuste
deformaautomáticaàteladodispositivocomBootstrap? Arespostaéobjetivae
extremamentesimples: adicioneuma meta tag comosparâmetroscorretos. Ao
fazê-lo,oCSSpadrãodoBootstrapencaminharáoestiloadequadoaodispositivo
queestárequisitandooacessoefaráoajusteparasuatela.Umexemploda meta tag
àqualnosreferimospodeservisualizadanalistagem 10.
Listagem 6.10-Metatagqueindicaamobilidade:
<meta name="viewport" content="width=device-width,
initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
Emlinhasgerais,estamosdizendoaonavegadoroseguinte:“Porfavor,execute
oCSSadequadocombaseneste viewporteapliqueosparâmetrosexplicitadosno
atributo content.” Nãoentraremosemmaioresdetalhesacercadecadaumadestas
propriedadesesuasrespectivasfun ções,jáqueestenãoéoobjetivodolivro.Entre-
tanto,vocêpoderáencontrarexcelentesleiturasacercadestesassuntosatravésdos
seguinteslinks:
• Manipulandoameta tagviewport:http://bit.ly/metatagviewport
• CSSBootstrap(eminglês):http://bit.ly/cssbootstrap
• CSSMediaQuery:http://bit.ly/cssmediaquery
121

## Página 132

6.8. Mobilidade:Suaconsultademédicosemdispositivosmóveis CasadoCódigo
MobilidadenativacomASP.NETMVC
Comojámencionamos,oprojeto“Cadêmeumédico?”estáestruturadosobre
o frameworkTwitterBootstrap,portanto,naturalmente,elejáseencontraautoajus-
távelparaodispositivoutilizadopelousuário(vejaafigura 6.5).Entretanto,o fra-
meworkASP.NETMVCoferecesuportenativoparamobilidadedeaplicaçõesweb.
Aseguir,discutiremosospossíveisformatosdetrabalhoparaqueissoocorra.
Figura6.5:Projeto‘Cademeumédico?’emfuncionamentonoemuladordeiPhone
QuandofalamosemmobilidadecomASP.NETMVC,podemosimaginaraome-
nostrêsabordagensdistintas,passíveisdeimplementação. Estassãoapresentadas
resumidamentenalistaaseguir:
•Utilizarosmesmos controllerse viewscomdiferentes layouts Razordepen-
dendododispositivodousuário. Aideiaaquiéquevocêutilizeamesma
lógicaimplementadanos controllerse actions,assimcomoasmesmas views.
122

## Página 133

CasadoCódigo Capítulo6. Views:interagindocomousuário
Nestecaso,seriamrenderizadosemtempodeexecuçãoapenasos layouts.Esta
abordagemérecomendada,deformageral,quandosedesejaapenasexibirda-
dos(grids,porexemplo)deformapersonalizada,ajustadaaodispositivo;
•Utilizarosmesmos controllers,entretanto,renderizando viewsespecíficas,
deacordocomodispositivo.Nestecaso,aoinvésderenderizarmos layouts
personalizados,renderizamos viewsespecíficas. Estaopçãodevesersuaes-
colhasevocêidentificaranecessidadedemodificarmuitooHTMLparaos
diferentesdispositivos.Outroaspectoimportanteaserobservadoéseépre-
cisomanterofluxodeoperaçõesdaaplicaçãoaolongodosdispositivos;
•Criaráreasseparadasparaprojetos mobileeprojetos desktop.Esteéomo-
deloondeaseparaçãodecamadasémaisdefinitiva.Existemdiferentespro-
jetos, mobilee desktop(comdiferentes controllers, actionse views)emuma
mesmasolução. Aoreceberasolicitação,o frameworkidentificaaresolução
dodispositivoedirecionaofluxodeoperaç ãoparaoprojetoadequadona
solução.
Paraqueestaideiapossaficarmaisclara,vamosaalgunsexemplospráticos.
Imagine que para a aplicação “Cadê meu médico?”, escolhêssemos a primeira
abordagem apresentada pela lista anterior. Para que a aplicação seja capaz de
renderizar olayout correto (claro, imaginando que exista umlayout chamado
“_LayoutMobile.cshtml”)bastariaescreverocódigoapresentadopelalistagem11no
interiordoarquivo“_ViewStart.cshtml”.
Listagem 6.11-Verificandoolayoutaserrenderizado:
@{
Layout = Request.Browser.IsMobileDevice ?
"~/Views/Shared/_LayoutMobile.cshtml"
: "~/Views/Shared/_Layout.cshtml";
}
Ocódigoésimplesedispensacomentáriosdetalhados.Bastadizerqueestamos
verificandoaresoluçãodonavegador.Casoseja mobile,“solicitamos”aoframework
queconsidereo layoutintitulado“_LayoutMobile.cshtml”.
Seoptássemospelasegundaabordagem,poderíamoscriarumasobrecargado
método “FindView” (de “ViewEngineResult”) para encontrar aview adequada,
conformeapresentaalistagem 12.
123

## Página 134

6.8. Mobilidade:Suaconsultademédicosemdispositivosmóveis CasadoCódigo
Listagem 6.12 - Encontrando views específicas (sugestão de Scott Hanselman
emseublog):
public class MobileCapableWebFormViewEngine : WebFormViewEngine
{
public override ViewEngineResult FindView(
ControllerContext controllerContext,
string viewName, string masterName, bool useCache)
{
ViewEngineResult result = null;
var request = controllerContext.HttpContext.Request;
if (request.Browser.IsMobileDevice)
{
result = base.FindView(controllerContext, "Mobile/" +
viewName, masterName, useCache);
}
if (result == null || result.View == null)
{
result = base.FindView(controllerContext, viewName,
masterName, useCache);
}
return result;
}
}
Éclaroqueocódigoacimaapresentaapenasumaideiadoquesepodefazer.Este
tipodeoperaçãopodeserimplementada,porexemplo,emum controllerbasedesua
aplicação(queherdede controller).
Escolhendoaterceiraop ção,poderíamoscriarumaáreaespecíficaparauma
aplicaçãomóveldentrodenossoprojeto.Paraisso,bastariaclicarcomobotãodireito
sobreeleeclicarnaop ção Add > Area (nosmoldesdoquejáfizemosdurantetodo
olivro).
No interior dessa área podemos adicionarcontrollerse views normalmente,
comosefosseumprojetoàparte. Assim,parafinsdidáticos,podemosadicionar
um controller“HomeController”dentrodanovaárea. Estecontrollerpoderáatuar
comoonovocontroladorpadrãodaaplicaç ãoemdispositivosmóveis. Bastaria,
124

## Página 135

CasadoCódigo Capítulo6. Views:interagindocomousuário
apósisso,realizardoispequenosajustesnopadrãorotasdaaplicaç ão(atravésdos
arquivos“RouteConfig.cs”),paragarantirquetalcontrollerpoderáseralcançado.
Estesajustespodemservisualizadosnalistagem 13.
Listagem 6.13-Ajustandoarotapadrãodaaplicaç ão:
//Alterando a rota padrão...
public override void RegisterArea(AreaRegistrationContext context)
{
context.MapRoute(
"Mobile",
"Mobile/{controller}/{action}/{id}",
new { controller = "Home", action = "Index",
id = UrlParameter.Optional }
);
}
//Dando prioridade para o controller de desktop
public static void RegisterRoutes(RouteCollection routes)
{
routes.IgnoreRoute("{resource}.axd/{*pathInfo}");
routes.MapRoute(
"Default",
"{controller}/{action}/{id}",
new { controller = "Home", action = "Index",
id = UrlParameter.Optional },
// Adicione o namespace dos controladores desktop a seguir
new[] { "CadeMeuMedico.Controllers" }
);
}
Nasequência,paracoroarotrabalho,bastariacriarumfiltroqueredirecionaria
ousuárioparaoconteúdo mobile,seistoforpertinente,claro.Comovocêdevese
lembrardoiníciodestelivro,estamostrabalhandooconceitodepersonalizaç ãode
rotas,comofimdedefinirasprioridadesdechamadaseexecuções,umavezque
possuímosdois controllers“Home”emnossaaplicação.
125

## Página 136

6.8. Mobilidade:Suaconsultademédicosemdispositivosmóveis CasadoCódigo
Concluindoedesafiando
Nestecapítuloapresentamostodososprincipaisconceitosparaquevocêpossa
ampliarseusconhecimentosemrelaçãoàmaneiracomqueo frameworkMVCtrata
omecanismode views. Apresentamostambémimportantesconceitosacercado
ASP.NET Razor, view engine padrãodaMicrosoftparaprojetosweb. Finalmente
concluímosapresentandoconceitosdemobilidadedentrodoASP.NETMVC.
Ficacomodesafioparaestecapítuloreproduzirnapráticaqualquerumdostrês
mecanismosdemobilidadenativosdoASP.NETMVCmencionadosaqui.Dica:nós
recomendamosoterceiromodelo.
126

## Página 137

Capítulo7
Segurança:Criandosuaárea
administrativa
Quandoelencamosasprincipaisnecessidadesdawebnosdiasatuais(evocêdevese
lembrardoiníciodestelivro),“segurança”éumitemqueaparecenotopodalistae,
claro,nãopoderiaserdiferente.Asseguraraousuáriodedeterminadosistemaqueo
acessoaseusdadoserecursosestãoprotegidos,deixoudeserapenasumdiferencial
competitivo,massim,éumaobrigação.
Especialmentenaweb,seguran çaédefatoumdosaspectosmaisimportantesde
umaaplicação,hajavistaanaturezadoambiente:umlugarpúblico.
ASP.NETMVCofereceumaamplagamaderecursosquepodemlheajudara
criaraplicaçõesrealmenteseguras.Evidentemente,nãoserápossívelapresentarem
detalhes,todosestesrecursos,entretanto,vocêseráguiadopeloprocessodeconstru-
çãodeumaáreadeacessorestritoqueutilizaclaro,osprincipaisrecursosdisponíveis
no frameworkMVCparaestefim.Vamoscome çar?!.

## Página 138

7.1. Áreaadministrativa?! CasadoCódigo
7.1 Á rea administrativ a?!
Comovocêdeveselembrar,aaplicaç ão“CadeMeuMedico?” sedivideemduas
frentes:umainterfacepública(website)acessadapelousuáriofinalpararealizara
consultadomédicodesejado;umaárearestritaatravésdaqualérealizadaaadmi-
nistraçãodestewebsite.
Atéaqui,váriasrotinasparaaáreaadministrativa(comoocadastrodemédicos
apresentadonocapítulo 5)foramcriadasmas,daformacomoestão,elaspodemser
acessadasporqualquerusuário.Precisamosagoraadicionar“muros”e“portões”a
estaaplicaçãodeformaapermitirapenasaentradadepessoasautorizadas.
7.2 Criando a área administrativ a
Iniciaremosnossasatividadescriandoa“portadeentrada”daáreaadministrativade
nossaaplicação,jáquesuassubáreasserãoprotegidasporusuárioesenha.
Existemdiferentesmaneirasparaseconstruirmecanismosdeautenticaç ãoe
persistirosdadosdousuárioautenticadoutilizandoASP.NETMVC.Poderíamos
utilizaromecanismodeautenticaçãodopróprio ASP .NET Membership(vocêpode
encontrarumbomtextosobreoassuntonolink: http://bit.ly/aspnetmembership),
poderíamoscriarnossoprópriomodelodeautenticaçãoutilizandoojásuperdifun-
didoconceitode sessions(vocêpodelerumbomtextosobreestaabordagematravés
dolink: http://bit.ly/aspnetsessions),poderíamosutilizarrecursosdecache,tabela
deumbancodedadosrelacional,enfim.
Paraaconstruçãodenossaaplicação,utilizaremosumrecursoamplamenteuti-
lizado webafora: oscookies. Seesteconceitoénovoparavocê,recomendamosa
leituradotextocontidonestelink: http://bit.ly/conceitodecookies.
ExecuteoVisualStudio.Emseguida,navegueatéa Solution Explorerenaraiz
doprojeto,adicioneumnovodiretório. Nomeie-ocomo“Repositorios”. Emseu
interior,adicioneumanovaclasseeatribuaaelaonome“RepositorioUsuarios.cs”.
Emseuinterior,adicioneométodoapresentadopelalistagem 1.
Listagem 7.1-Adicionandoométodoqueverificaaexistênciadousuário:
public static bool AutenticarUsuario(string Login, string Senha)
{
var SenhaCriptografada =
FormsAuthentication.
128

## Página 139

CasadoCódigo Capítulo7. Segurança:Criandosuaáreaadministrativa
HashPasswordForStoringInConfigFile(Senha, "sha1");
try
{
using (EntidadesCadeMeuMedicoBD db =
new EntidadesCadeMeuMedicoBD())
{
var QueryAutenticaUsuarios =
db.Usuarios.
Where(x => x.Login == Login && x.Senha == Senha).
SingleOrDefault();
if (QueryAutenticaUsuarios == null)
{
return false;
}
else
{
RepositorioCookies.RegistraCookieAutenticacao(
QueryAutenticaUsuarios.IDUsuario);
return true;
}
}
}
catch (Exception)
{
return false;
}
}
Ocódigoapresentadopelalistagem 1ésimplesmasapresentaalgunsaspectos
importantes.Aorecebermososdadosde“Login”e“Senha”,verificamosatravésde
umaexpressãolambda—umbompostsobreesteassuntopodeserencontradoatra-
vésdestelink:http://bit.ly/expressoeslambda—seexistenabasededadosalgumre-
gistroqueatendedeformaúnicaaosdadosinformadospelousuário.Seencontrar,
gravamosocódigodousuárioemum cookieeoregistramosnonavegadoreretor-
namosovalor trueparaindicarosucessodaoperação,casocontrário,retornamoso
valor falseparaindicarafalha.
Duas observações importantes aqui. A primeira
diz respeito à linha “ var SenhaCriptografada =
FormsAuthentication.HashPasswordForStoringInConfigFile(Senha,
129

## Página 140

7.2. Criandoaáreaadministrativa CasadoCódigo
"sha1");”. Estamos fazendo desta forma por imaginar que a senha
de acesso do usuário encontra-se criptografada no banco de dados —
sim, esta é uma boa prática. Desta forma, estamos realizando a verifi-
cação da senha já criptografada. A segunda observação está relacionada
à utilização de repositórios para realizar a tarefa de gravação/registro do
cookie (“ RepositorioCookies.RegistraCookieAutenticacao(
QueryAutenticaUsuarios.IDUsuario);”).
Repositórios?O que é isso?
Umnovoconceitoimportanteestápresentepropositalmentenocó-
digoapresentadopelalistagem 1—Repositórios.Note,osrepositórios
agrupamemclassesespecíficas,métodosqueexecutamaçõesdemesma
natureza.Emnossoexemplo,paraagrupartodasasoperaçõesrelaciona-
dasa“Usuarios”,criamosumaclassederepositóriochamada“Reposito-
rioUsuarios”.Parafacilitaramanutençãodecódigo,criamosumdiretó-
rioemnossoprojetochamado“Repositorios”,quereúnetodasasclasses
derepositóriodoprojeto.
Repositórios são amplamente utilizados em projetos desoftwares,
umavezqueajudamamelhoraro design(entenda-se,arquitetura)dos
mesmos.
Outraobservaçãoimportanteemrelaçãoàutilizaçãodosrepositórioséane-
cessidadededeclaraçãoexplícitade“CadeMeuMedico.Repositorios”. Claro,issoé
precisoparaqueosmétodosdorepositóriosetornemvisíveisnocontextodaclasse
queestáutilizandoorecurso.
Apóscriarmosométodoqueiráatéobancodedadosefaráaverificaç ãoda
existênciaounãodousuário,échegadoomomentodeimplementarmosocompor-
tamentodeautenticaçãono controller.Lembre-se,estes“caras”sãoosresponsáveis
porgerirtodasasrequisiçõesquechegamao framework.
Continuando,navegueatéodiretório Controllerse,lá,adicioneumnovo control-
ler.Noteque,najanelaexibidacomooresultadodestaaç ão,oVisualStudiojátraz
consigoosufixo Controller.Comonomearemosnossocontroladorcomo“Usuarios”,
teremososeguintenomeexibidonocampo Controller name:UsuariosController.
Namesmajanela,nocampo T emplate,selecioneaop ção“Empty MVC controller”.
EstaémaisumadasCoC’sdasquaisfalamosnosegundocapítulodestaobra. O
130

## Página 141

CasadoCódigo Capítulo7. Segurança:Criandosuaáreaadministrativa
ASP.NETMVCutilizaestesufixoparaidentificardeformaautomáticaaquelaclasse
comocontroladoraeautomaticamenteherdaroscomportamentosdaclasse Control-
lerdaBCL(BaseClassLibrary).Afigura 7.1apresentaestaparametrização.
Figura7.1:Adicionandoocontrollerdeusuários
Substituaagoraa action“Index”docontrollerrecém-criadopela“Autenticacao-
DeUsuario”,apresentadapelalistagem2.
Listagem 7.2-CriandoométodoAutenticacaoDeUsuario:
[HttpGet]
public JsonResult AutenticacaoDeUsuario(string Login, string Senha)
{
if (RepositorioUsuarios.AutenticarUsuario(Login, Senha))
{
return Json(new {
OK = true,
Mensagem = "Usuário autenticado. Redirecionando..." },
JsonRequestBehavior.AllowGet);
}
131

## Página 142

7.2. Criandoaáreaadministrativa CasadoCódigo
else
{
return Json(new {
OK = false,
Mensagem = "Usuário não encontrando. Tente novamente." },
JsonRequestBehavior.AllowGet);
}
}
Principaisaspectosdocódigoapresentadopelalistagem 2:
• Naprimeiralinhadecoramosaaction“AutenticacaoDeUsuario”comoatri-
buto [HttpGet],indicandoqueométodoapenasdevolverádadosparao
chamador. Senãodecorássemosa actioncomesteatributo(ououtroqual-
quer),oASP.NETMVCautomaticamenteimprimiráocomportamentode
[HttpGet];
• Aoreceberosdadosdeentrada,utilizamosométodo“AutenticarUsuario”do
“RepositorioUsuarios”,criadonalistagem1;
• Ao receber a resposta da verificação (veja o if), retornamos em for-
mato JSON ostatus do processo: sucesso (repare na linhareturn
Json(new { OK = true, Mensagem = "Usuário autenticado.
Redirecionando..."}, JsonRequestBehavior.AllowGet);) ou
falha (note a linha return Json(new { OK = false, Mensagem
= "Usuário não encontrando. Tente novamente."},
JsonRequestBehavior.AllowGet);). Bacana, não?! Simples e di-
reto.
Aperguntaquepodeterseformadoemsuacabe çanesteinstanteé:aresposta
voltaparaquem?Veja,nocasodaaplicaç ão“Cadêmeumédico?”,utilizaremosuma
chamadaassíncronacomjQueryparadispararoprocessodeverificaç ãodaexistên-
ciaounãodousuário,portanto,quemreceberáarespostafinaldo controllerseráo
objetojQueryqueoriginouoprocesso. Apartirdaí,serásimplesexibirosdados
paraousuáriofinal.Poisbem,jáquepossuímosainfraestruturade backendpronta,
precisamosmontaraestruturade frontend.
Prosseguindocomoprocessodecriaçãodenossaáreaprotegida,abraoarquivo
“HomeController”eemseuinterior, adicioneumanovaactionqueretornaum
ActionResulte, nasequência, nomeie-acomo“Login”. Alistagem3apresentaa
132

## Página 143

CasadoCódigo Capítulo7. Segurança:Criandosuaáreaadministrativa
estruturadamesma.
Listagem 7.3-Actionqueretornaráaviewdelogin:
public ActionResult Login()
{
ViewBag.Title = "Seja bem vindo(a)";
return View();
}
Clicandocomobotãodireitosobreométododeretorno( View())esele-
cionandoaop ção“Add view...”, vocêseráapresentadoàjáconhecidajanelade
parametrização de views. Desta vez, não adicionaremos qualquer configuração
aela,tãopoucoherdaremosalgumpadrão. Oquefaremosnestajanelaapenas,
serádesmarcaraop ção“Use a layout or master page”—sim,criaremosumaview
foradopadrão.Ocódigodestanova viewpodeservisualizadoatravésdalistagem 4.
Listagem 7.4-Teladelogindosistema:
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta name="viewport" content="width=device-width" />
<title>Cade meu medico? - @ViewBag.Title</title>
<link href="@Url.Content("~/Content/bootstrap/bootstrap.min.css")"
rel="stylesheet" />
<style>
body {
padding-top: 60px;
}
</style>
</head>
<body>
<div class="navbar navbar-inverse navbar-fixed-top">
<div class="container">
<div class="navbar-header">
<a class="navbar-brand" href="#">
Cade meu medico? - Área Administrativa
</a>
</div>
<div class="collapse navbar-collapse">
133

## Página 144

7.2. Criandoaáreaadministrativa CasadoCódigo
<ul class="nav navbar-nav">
<li id="menuMedicos">
</li>
</ul>
</div>
</div>
</div>
<div class="container">
<div class="jumbotron">
<div class="container">
<h1>Quem é você?</h1>
<p>&nbsp;</p>
<div id="status"></div>
<p>&nbsp;</p>
<div>
<form id="form-login" name="form-login"
method="get"
action="javascript:function()">
<label for="txtLogin">Login</label>&nbsp;
<input type="text" id="txtLogin" name="txtLogin" />
&nbsp;
<label for="txtSenha">Senha</label>&nbsp;
<input type="password" id="txtSenha"
name="txtSenha" />&nbsp;
<a id="botao-entrar" class="btn btn-primary btn-lg">
Entrar
</a>
</form>
</div>
</div>
</div>
<p style="text-align:center;">
@Html.ActionLink(
"Esqueceu sua senha?",
"EsqueceuSuaSenha",
"Home",
null,
134

## Página 145

CasadoCódigo Capítulo7. Segurança:Criandosuaáreaadministrativa
new { @style = "text-align: center;" })
</p>
</div>
<script src="@Url.Content("~/Scripts/jquery-2.0.2.min .js")"></script>
<script src="@Url.Content("~/Scripts/bootstrap.min.js")"></script>
</body>
</html>
Oresultadodarenderizaçãodocódigoda view Razorapresentadopelalistagem
4podeservisualizadoatravésdafigura 7.2.
Figura7.2:ViewdelogindosistemaCadêmeumédico?
Agora que possuímos parte de nossa infraestrutura defrontend necessária
pronta,podemosseguircomasegundapartedestequebra-cabe ças,istoé,criaros
comportamentos. Paraisso, criaremosumnovoarquivoJavascriptnodiretório
“Scripts”denossaaplicação. Oprocessodecriaçãodoarquivosegueomesmo
padrãojáutilizadoparacriaroutrostiposdearquivos,ouseja,botãodireitono
diretório Scripts > Add > New Item. Selecioneàesquerdaaop ção“Web”
e à direita, “JavaScript File”. Nomearemos sugestivamente este arquivo como
“Login.Home.js”.Emseuinterior,adicioneocódigoapresentadopelalistagem5.
Listagem 7.5-CódigoJavascriptquedisparaoprocessodevalidaç ão:
$(document).ready(function () {
$("#status").hide();
$("#botao-entrar").click(function () {
135

## Página 146

7.2. Criandoaáreaadministrativa CasadoCódigo
$.ajax({
url: "/Usuarios/AutenticacaoDeUsuario",
data: { Login: $("#txtLogin").val(),
Senha: $("#txtSenha").val() },
dataType: "json",
type: "GET",
async: true,
beforeSend: function () {
$("#status").html("Estamos autenticando o usuário.
Só um instante...");
$("#status").show();
},
success: function (dados) {
if (dados.OK) {
$("#status").html(dados.Mensagem)
setTimeout(function () { window.location.href =
"/Home/Index" }, 5000);
$("#status").show();
}
else {
$("#status").html(dados.Mensagem);
$("#status").show();
}
},
error: function () {
$("#status").html(dados.Mensagem);
$("#status").show()
}
});
});
});
Oquefazemosnocódigoapresentadopelalistagem 5é:
1) RealizamosumachamadaassíncronautilizandoométodojQueryAjax;
2) Informamoso controllerea actionquedeverãoserexecutadasdeformaassín-
crona,otipoderetornoeotipodeoperaç ão;
3) Informamosaonavegadoroquedeveráserrealizadoantesdachamadaserre-
alizada( beforeSend),casoarespostasejadesucesso( success)oufalha(
error).Simples!
136

## Página 147

CasadoCódigo Capítulo7. Segurança:Criandosuaáreaadministrativa
Paratestarofuncionamentodetudoquefoifeitoatéaqui,precisamosadicionar
umusuárioqualquernobancodedadosdaaplicaç ãoparaquepossamossimular
a situação de sucesso (usuário encontrado), certo?! Faremos tal procedimento
adicionandooregistrodeusuárionobancodedadosdeformadiretacomacláusula
INSERT,apresentadapelalistagem 6.Sevocêutilizouoscriptdecriaç ãodobanco
de dados disponibilizado pode pular esse passo, o script adiciona esse registro
automaticamentenacriaçãodobancodedados.
Listagem 7.6-
:
Insert Into Usuarios
(Nome, Login, Senha, Email)
Values
('Administrador', 'admin',
'40BD001563085FC35165329EA1FF5C5ECBDBBEEF', 'admin@cdmm.com')
Todososmecanismosestãoprontosefuncionandoeousuáriodetestedevida-
mentecadastrado. Estamosprontospararealizarostestes. Noprimeiroteste,in-
formaremosusuárioesenhaincorretose,então,verificaremosocomportamentodo
sistema.Afigura 7.3apresentaarespostadosistema.
Figura7.3:Respostadosistemaaentradasincorretasparaosistema
137

## Página 148

7.2. Criandoaáreaadministrativa CasadoCódigo
Quandoadicionamosasinformaçõescorretas—paraquevocêpossatestar,é
importantesaberqueasenhaé“123”—,compatíveiscomasqueseencontramca-
dastradasnobancodedados,obtemosarespostaapresentadapelafigura 7.4.
Figura7.4:Respostadosistemaparaumaentradacorreta
Otestefinalaserrealizadoparaquepossamosverificarsedefatotudoestáfun-
cionandoconformeoesperadoéaverificaçãodaexistênciado cookiequearmazena
ainformaçãodousuáriorecém-autenticado. Afigura7.5comprovaquetudoestá
correto.
Figura7.5:Verificandoseocookiedeapoiofoicriadocorretamente
138

## Página 149

CasadoCódigo Capítulo7. Segurança:Criandosuaáreaadministrativa
Ok,mecanismodeloginimplementando.
7.3 Apesar do login, nada é bloqueado.E agora?!
Muitoemboratenhamos“cercado”nossaaplicaçãoatravésdaimplementaçãodo
mecanismodeautenticaçãovia login,facilmentepodemosnotarumafalhadese-
gurançagrave:seinvocarmosdeterminadorecursodeformadireta(pelaURL,por
exemplo),mesmonãoestandoautenticadonosistema,orecursosemostrarádispo-
nível.Esteéocaso,porexemplo,do controller/action“Home/Index”,quedeveriaser
exibidoapenasparausuáriosregistrados.
Nestecontexto,umrecursodoASP.NETMVCdisponíveldesdeaversão2do
frameworkseapresentacomoumaboaalternativaparasolucionaroproblemacitado
noparágrafoanterior:os action filters(emportuguêsbrasileiro,filtrosdeação).
7.4 Filtros de ação
Filtrosdeaçãosão,deformadireta,comportamentosespecíficosquepodemseratre-
ladosa actionse controllers.Atravésdeumaformadeclarativasimples(entenda-se
atributos),épossívelincorporarrobustezanaturezadasaplicações.
Umdosgrandesbenefíciosproporcionadospelosfiltrosdeaçãoéamelhoriasig-
nificativado design(arquitetura)daaplicação,umavezquepermiteretirarde actions
e controllerscomportamentosquenãosãorestritosaeles.Umexemploclarodesta
situaçãoencontra-sejustamentenoquefaremosaseguirparaaaplicaç ão“Cadêmeu
médico?”.Note,validarapermissãoounãodedeterminadousuárioparaacessara
páginainicialdaáreaadministrativa(Home/Index)nãoéfun çãoda action“Index”,
certo?Destaforma,asoluçãoéencapsulartalcomportamentoemumfiltro.Vamos
àsuaconstrução?
7.5 Implementando o filtro ‘AutorizacaoD eAcesso’
Ocomportamentoquepretendemosimprimirparanossos controllerse actionsé:se
determinadousuáriotentaracessarumrecursodeformadireta,osistemadeverá
repeli-lo,ouseja,redirecionarousuárioparaateladeautenticaç ãodosistemacom
ocaminhopretendidopreservadonabarradenavegaç ão.
139

## Página 150

7.5. Implementandoofiltro‘AutorizacaoDeAcesso’ CasadoCódigo
Criandoaclasse‘AutorizacaoDeAcesso’
Comoprimeiramedidanosentidoestruturarmosnossofiltrodeaç ão,adiciona-
remosumdiretóriochamado“Filtros”àárvoredediretóriosdenossoprojeto.Em
seuinterior,adicionaremosumanovaclasse,chamada“AutorizacaoDeAcesso”. Se
tudocorreubemnesteprocesso,vocêdeveráestarvisualizandoumatelasemelhante
àapresentadapelafigura 7.6.
Figura7.6:EstruturageradaparaofiltroAutorizacaoDeAcesso
Agora,deixaremosoarquivorecém-criadotemporariamentedelado.Faremos
issoporqueprecisamosimplementardoismétodosauxiliares,ambosnorepositório
deusuários(“RepositórioUsuarios”)quecriamosnasegundaseçãodestecapítulo.
Estesmétodosnosajudarãoaverificarseousuáriojáseencontraautenticadono
sistemae,combasenestaresposta,decidirmosserejeitamosoupermitimosoacesso.
Osmétodosaosquaisnosreferimossãoapresentadosnasequênciaaolongoda
listagem7.
Listagem 7.7-Métodosdeapoioparaverificaçãodostatusdousuário:
public static Usuario RecuperaUsuarioPorID(long IDUsuario)
{
try
{
using (EntidadesCadeMeuMedicoBD db =
new EntidadesCadeMeuMedicoBD())
{
var Usuario =
db.
Usuarios.
Where(u => u.IDUsuario == IDUsuario).
SingleOrDefault();
return Usuario;
}
}
140

## Página 151

CasadoCódigo Capítulo7. Segurança:Criandosuaáreaadministrativa
catch (Exception)
{
return null;
}
}
public static Usuario VerificaSeOUsuarioEstaLogado()
{
var Usuario = HttpContext.
Current.
Request.
Cookies["UserCookieAuthentication"];
if (Usuario == null)
{
return null;
}
else
{
long IDUsuario = Convert.
ToInt64(RepositorioCriptografia.
Descriptografar(Usuario.Values["IDUsuario"]));
var UsuarioRetornado = RecuperaUsuarioPorID(IDUsuario);
return UsuarioRetornado;
}
}
Osnomesdeambososmétodosapresentadospelalistagem 7jádãoideiadesuas
funçõesnocontextodaaplicação. Oprimeirotentarecuperaroregistroúnicode
usuáriobaseadonocódigoprovenientedoparâmetrodomesmo.Osegundotoma
comobaseousuáriorecuperadopeloprimeirométodoeverificaseousuáriojáse
encontraautenticadonosistema.Simplesefuncional.
Agora possuímos os métodos auxiliares de nosso filtro, portanto, podemos
partirparasuaimplementaçãodefato. Paraisso,volteaoarquivodofiltroque
criamosalgunsparágrafosatrásesubstituaseuconteúdoporaqueleapresentado
pelalistagem 8.
Listagem 7.8-Implementandoofiltrodeação:
using System;
141

## Página 152

7.5. Implementandoofiltro‘AutorizacaoDeAcesso’ CasadoCódigo
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using CadeMeuMedico.Repositorios;
namespace CadeMeuMedico.Filtros
{
[HandleError]
[AttributeUsage(AttributeTargets.Class |
AttributeTargets.Method,
Inherited = true,
AllowMultiple = true)]
public class AutorizacaoDeAcesso :
ActionFilterAttribute
{
public override void OnActionExecuting(
ActionExecutingContext FiltroDeContexto)
{
var Controller = FiltroDeContexto.
ActionDescriptor.
ControllerDescriptor.
ControllerName;
var Action = FiltroDeContexto.
ActionDescriptor.
ActionName;
if (Controller != "Home" || Action != "Login")
{
if (RepositorioUsuarios.
VerificaSeOUsuarioEstaLogado() == null)
{
FiltroDeContexto.
RequestContext.
HttpContext.
Response.
Redirect("/Home/Login?Url=" +
FiltroDeContexto.H
ttpContext.
Request.
Url.
142

## Página 153

CasadoCódigo Capítulo7. Segurança:Criandosuaáreaadministrativa
LocalPath);
}
}
}
}
}
Nossaprimeiraprovidênciaaocriarométodoédecoraraclassecomoumgeren-
ciadordeerrosautomatizado(vide [HandleError]).Nasequência,informamos
atravésdadiretiva“AttributeUsage”eseusatributos,qualocomportamentoquees-
peramosencontraraoutilizarofiltro.Apósisso,sobrescrevemosométodo“OnAc-
tionExecuting”epersonalizamosocomportamentodarequisiçãoquechegaao con-
troller.
Comovocêpodenotar,atravésdeumaverificaçãosimples(if ),verificamosse
arequisiçãoéporumrecursoprotegidoporusuárioesenha. Senãofor,oacesso
aorecursoéliberado,casocontrário,direcionamosousuárioparaaáreadeentrada
(login)preservandooendere çobuscadopelousuárionarequisiçãooriginal.
Criandoocontrollerbase
Agora,paraqueoprocessopossasercompletado,precisamosimprimiromesmo
comportamentoparatodosos controllersdaaplicação.Comofaremosisso?Simples:
iremosdecoraro controllerbasecomofiltrorecém-criadoe,apartirdaí,paracada
novo controller,herdaremosde controllerbase.
Paraisso,adicionaremosumnovo controllerchamado“Base”emseurespectivo
diretórioe,emseuinterior,implantaremosocódigoapresentadopelalistagem 9.
Listagem 7.9-Comportamentodocontrollerbase:
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using CadeMeuMedico.Filtros;
namespace CadeMeuMedico.Controllers
{
[AutorizacaoDeAcesso]
143

## Página 154

7.5. Implementandoofiltro‘AutorizacaoDeAcesso’ CasadoCódigo
public class BaseController : Controller
{
protected override void OnActionExecuting(
ActionExecutingContext filterContext)
{
base.OnActionExecuting(filterContext);
}
}
}
Bastaagora,nos controllersdaaplicação,mudaraheran ça.Aoinvésdeherdar
diretamentede Controller, estescontroladoresdeverãoherdarde BaseController,
conformeapresentaoexemplodalistagem 10.
Listagem 7.10-Modificandoaheran çadoscontroladores:
public class HomeController : BaseController
{
//
// GET: /Home/
public ActionResult Login()
{
ViewBag.Title = "Seja bem vindo(a)";
return View();
}
public ActionResult Index()
{
return View();
}
}
Agora podemos testar o comportamento de nossa aplicação. Para isso, re-
movaos cookiesdeseunavegadore,semrealizar login,tenteacessaroendere ço“
http://localhost: [sua_porta]/Home/Index”.Setudocorreubem,vocêseráre-
direcionadoparaatelade logincomoendere çobuscadopreservadonabarrade
navegação,conformeapresentaafigura 7.7.
144

## Página 155

CasadoCódigo Capítulo7. Segurança:Criandosuaáreaadministrativa
Figura7.7:Omecanismodevalidaçãoemfuncionamento
7.6 Concluindo e desafiando
Comesteconglomeradodeconceitos,nossoobjetivoémostrarumadasformaspos-
síveisparaquesepossaprotegerasaplicaçõesASP.NETMVCdeacessosindevi-
dos.Éclaroqueestesconceitoserecursosnãoparamporaqui.Existeumaampla
gamaderecursosparasetrabalharcomestesconceitosdisponíveisno framework
MVC.Vocêpodeencontrarumtextoapresentandoestesrecursosatravésdestelink:
http://bit.ly/segurancamvc.
Desafio:imagineagoraquevocêpreciseadicionarnovosconteúdosquenãone-
cessariamentesãoprotegidosporsenha(comoorecursode“RecuperarSenha”,por
exemplo).Ondevocêalterariaaestruturadaaplicaçãoparaqueaaplicaçãonãore-
cusasseoacessoaomesmo?!Mãosàobra.
145

## Página 157

Capítulo8
Publicandosuaaplicação
Sevocêseguiuàriscatodososexemplosapresentadosporestelivro,nestemomento
devepossuiremmãosboapartedaaplicaç ão“Cadêmeumédico?”.Sevocêacessaro
endereço[lugar onde disponibilizaremos o exemplo completo],vocêpoderáencontrar
aaplicaçãocompletaparaseguircomoconteúdodestecapítulo— Publicaçãoda
aplicação.
Optamospordeixaraapresentaçãodoprocessodepublicaçãodaaplicaçãocomo
últimocapítulonãopelofatodesermenosimportantequeosdemaismassim,por
umaquestãológicamuitosimples:comopodemospublicaralgosemqueestealgo
exista? Oprocessodepublicaçãodeaplicaçõeséimportante,principalmentenos
diasatuaisemquetantostiposdeambientesdistintosseapresentamcomoop ções
para host.
Nestecapítuloapresentaremosalgunscenárioseferramentasdisponíveisno
mundodatecnologiaparaquepossamospublicaraplicaçõesASP.NET,especial-
mente,ASP.NETMVC4.Especialmentenestecapítulo,manteremosofoconapu-
blicaçãoparaumambienteespecífico,umaplataformaespecíficadecomputaç ãoem

## Página 158

8.1. Pré-requisitosparahospedaraplicaçõesASP.NETMVC4 CasadoCódigo
nuvem,criadaemantidapelaMicrosoft—oWindowsAzure.
8.1 Pré-requisitos para hospedar aplicações
ASP.NETMVC4
ParaqueasaplicaçõesASP.NETMVC4possamfuncionardeformaadequadaem
umambienteremoto,éprecisoquehajanesteambienteum setdeconfigurações
járealizadasecertogrupodeferramentasdisponíveis.Alistaaseguirapresentao
conjuntomínimoderequisitosquedevemestardisponíveisnoservidordeaplicaç ão
paraquetudofuncioneperfeitamente.
•Windows(7,7comSP1,Server2003comSP2,Server2008,Server2008
R2,Server2008R2comSP1,VistacomSP1,XPcomSP3):vocêjáconhece
oWindows,certo?
•.NETFramework4(+):o.NETFrameworkéomodelodeprogramaç ãocom-
pletoeconsistentedaMicrosoftparaacriaç ãodeaplicativosqueoferecem
umaexperiênciavisualmentesurpreendenteaosusuários,comunicaçãose-
guraeseminterferênciaseacapacidadedemodelarumavariedadedepro-
cessosdenegócios;
•ASP.NETMVC4: frameworkASP.NETMVCemsuaversão4;
•InternetInformationServices6.0(+): o Internet Information Services (ou
simplesmenteIIS)éocomponentequefazdoservidorumservidordeaplica-
çõesweb;
•MicrosoftDataAccessComponents2.8(+):umconjuntodeDLL’sutilizada
peloADOpararealizaroacessoadados;
•WindowsInstaller3.1(+): éumcomponentequeautomatizaoprocessode
instalaçãodosrecursosnosistemaoperacional;
•InternetExplorer5.01(+):éonavegadorwebdaMicrosoft.Estecomponente
vemnativamenteinstaladonoWindows;
•Pentium1GHz(+): clockdeprocessadormínimoesperado;
•RAM512MB(+):quantidademínimadememóriaRAMexigida;
148

## Página 159

CasadoCódigo Capítulo8. Publicandosuaaplicação
•x86,x64eia64:arquiteturassuportadaspelosrecursosanteriores.
Vocêpoderealizaro setupdoambientemanualmente(instalandomanualmente
cadaumdoscomponentesmencionadosnalistaanterior)oupodeutilizarumafer-
ramentadisponibilizadagratuitamentepelaMicrosoft,oWebPI(acrônimopara Web
Platform Installer),queautomatizatodooprocessodeinstalaç ãoeconfiguraçãode
ambientenoservidorremoto,gerenciandoinclusive,asdependênciasdecadaele-
mento.Vocêpodeencontrarmaisinformaçõessobreestaferramentaseguindoeste
link:http://bit.ly/webpiaspnetmvc.
8.2 Ambientes de host
Omercadodetecnologiadisponibilizaumasériedeambientesdistintosparaque
sejapossívelhospedaraplicaçõesASP.NET(MVC).Sãoosprincipais:
•Hospedagemcompartilhada(amaiscomum):existempraticamenteinfini-
tasopçõesnoBrasilouforadelepararealizaro hostdeaplicaçõesASP.NET.
UmarápidabuscanoGoogledaráveracidadeaestaafirmação.Omodelotra-
dicionalde host(conhecidocomo“compartilhado”)contemplamúltiplosweb-
sitesemummesmoambiente,compartilhandotodososrecursosde hardware
e softwaredisponíveisnoservidor;
•VirtualPrivateServer(VPS):nestecaso,o deploydaaplicaçãoASP.NETé
realizadoemumservidorvirtualdedicadoparaaaplicaç ão.Nestesambientes,
deformageral,aconfiguraçãoficaporcontadequemcontrata;
•Servidordedicado:nestecaso,temosumservidorfísico. Esteservidorterá
todososrecursosdisponíveisparaexecutaroservidordeaplicaç ãoe“rodar”
aaplicaçãoASP.NETMVC.Aúnicadiferen çaemrelaçãoàsVPS’séofatode
queumévirtualizadoeooutroéfísico;
•AmbientesdeCloud:nosambientesdecomputaç ãoemnuvem(emampla
expansãonomercado)existemdiferentesmodelospara hostdeaplicações
ASP.NETMVC.Discutiremosalgunsdelesmaisadiantenestecapítulo.
Paracadaumdestescenários,paraqueasaplicaçõespossamserenviadasaoser-
vidorremoto,existemdiferentesabordagens,taiscomoFTP,SFTP,WebDeployetc.
Paracadaumdestesmodelos,existemdiversasferramentaspararealizaresteenvio.
149

## Página 160

8.3. Computaçãoemnuvem.Porquê? CasadoCódigo
ParaFTP,porexemplo,podemoscitaropróprioVisualStudioExpress,FileZilla,
CuteFTP,dentreoutros. SeaescolhaforpeloVisualStudio,existeaindaaop ção
degerarumpacotedepublicaç ãolocal(parapublicarmaistarde)utilizandooutra
ferramentaqualquer.
Parademonstrarapublicaçãodaaplicação“Cadêmeumédico?”,utilizaremoso
próprioVisualStudio.Vocêentenderáoporquênomomentoadequado.
8.3 Computação em nuvem.P or quê?
Oconceitodecomputaçãoemnuvem,indiscutivelmente,revolucionouomercado
detecnologia. Atransformaçãodeambienteserecursoscomplexos(queemmo-
mentoanterior,eramprivilégiosapenasdegrandesempresas)emserviçoscombaixo
custoeportanto,acessíveisaqualquertipodeempresa,foiogrande“pulodogato”
nomundodatecnologia.
Aideiaaquiéque,assimcomoarquivos,servidoresedemaisserviçosassociados
fiquemdistribuídosaoredordomundoeque,deumaforma“mágica”,proporcionem
altadisponibilidade,tolerânciafalhas,conexõesresilientes,seguran ça,performance
deaplicaçõeseprincipalmente,baixocusto—tambémemfunçãodadiminuiçãoda
complexidadeparagerirestesserviçoserecursos.
Parafacilitaroentendimentodosconceitosrelacionadosàcomputaç ãoemnu-
vem,osserviçoserecursosoferecidosporelasãosubdivididosemtrêsgrandesver-
ticais: Infrastructure as a Service(IaaS), Platform as a Service(PaaS)e Software as a
Service(SaaS).
Noprimeirogrupo(IaaS)encontram-seagrupadostodososserviçoserecursos
associadosdiretamenteaomodelodeinfraestrutura,comoporexemplo,servidores
virtuais.Éclaroque,nesteprimeirogrupo,oesfor çoimpressoporquemestáadqui-
rindooserviçodenuvemémaior,umaveztodaaconfiguraç ãodoambientedeve
serrealizadaporele.Deformageral,buscamserviçosnestaverticalempresasque
desejampossuirumaltograudepersonalizaç ãodeambiente.
Osegundogrupo(PaaS)incorporaserviçoserecursosdenívelmaisalto.Aqui,
oclientecontrataumaplataformajápronta,pré-configurada,esimplesmenteenvia
aaplicaçãoparaqueexecutenesteambiente.Todoesfor çodemanutençãodoambi-
enteficaporcontadofornecedordaestruturadecomputaç ãoemnuvem.Ficasob
aresponsabilidadedoclienteapenasrealizaro deploydaaplicação.Deformageral,
quembuscaestesambientessãoempresasde software,quenãoqueremdispender
esforçoscomapartedeinfraestrutura.
150

## Página 161

CasadoCódigo Capítulo8. Publicandosuaaplicação
Oterceirogrupo(SaaS)nadamaisédoqueoresultadofinal,apósapublicaç ão.
Sãoos softwaresconstruídosespecificamenteparaaplataformadenuvemequetem
comportamentoótimonesteambiente.Exemplos:Office365,GoogleDocs,Educa-
Netetc.“CadêMeuMédico?”tambémseráumsoftwarecomoserviçonofimdeste
capítulo.
Afigura 8.1apresentaarelaçãoentreasvertentesdecomputaçãoemnuvemeo
esforçoquedeveráserdispendidoentrequemcompraequemforneceestesserviços.
Figura8.1:Pilhaderesponsabilidadesdacomputaçãoemnuvem
8.4 OW indows Azure
OWindowsAzureéumaplataformadecomputaç ãoemnuvem,criadaemantida
pelaMicrosoft. Nomercadodecomputaçãoemnuvem,aMicrosoftélider,divi-
dindoahonrariacomaAWS(AmazonWebServices).
Apalavra“plataforma”nãoéutilizadaaquiporacaso.WindowsAzureoferece
umaamplagamaderecursosqueatendemàgrandemaioriadasdemandasdemer-
cadocomqualidadeebompre ço,sejaparaodesenvolvimentodeaplicaçõesoupara
aáreadeinfraestrutura.Parafinsdetestes,aMicrosoftoferececomodegustaç ão,um
vouchernovalordeUS$ 200,00durantetrêsmeses. Vocêpoderáencontrartodas
151

## Página 162

8.5. WindowsAzureWebsites CasadoCódigo
asinformaçõesrelacionadasaoWindowsAzureatravésdositeoficialdoproduto:
http://windowsazure.com/.
8.5 Windows AzureWebsites
UmdosgrandesrecursosdisponíveisnoWindowsAzureéoqueaMicrosoftchama
de“WindowsAzureWebsites”.
Emlinhasgerais,WindowsAzureWebSiteséumnovoambientedisponibilizado
dentrodaplataformaAzurecomcaracterísticasespecíficasparaexecutaraplicações
webdepequenoemédioportes. Aocriarumnovowebsitenestemodelo,assim
comoemumahospedagemcompartilhadatradicional,suaaplicaç ãocompartilhará
recursos(disco,RAM,processamentoetc.) comoutrasaplicaçõesemummesmo
servidor—dealtacapacidade,éimportantequesediga.Aideiaéque,atravésdo
WAWS,sejapossívelrealizarodeploydeaplicaçõeswebdeformasimplificadae
rápida,utilizandoocontroladordecódigodesuapreferência.Algunsaspectosim-
portantesaseremconsideradosemrelaçãoaoWAWSsão:
•GitouTFSdeployment:comWAWSépossívelutilizarGitouTFSparaefe-
tuarapublicaçãodesuasaplicaçõesdeformadireta. Comalgumaspoucos
comandosecliques,épossívelhabilitaroambienteparadeployatravésdestas
ferramentas;
•Escolhadapublicaçãoativa:oportaldoWAWSarmazenacronologicamente
àsúltimaspublicaçõesrealizadas. Comalgunscliquesvocêpodeselecionar
qualdentreelaséaquelaquedeveestarativa;
•Gerenciamentodeconfiguraçãodeaplicaç ões:gerenciarosdiversosvalores
eatributosdearquivosdeconfigurações(web.config’s)ésempreumadorde
cabeçaàparte.ComWAWSesteproblemafoireduzidodrasticamenteatravés
deummecanismosimplesdeparametrização;
•Log’sdosite: WAWSarmazenalog’sdossitesláarmazenados. Vocêpode
monitorara“saúde”desuaaplicaçãoanalisando-os.Esteacessopodeserrea-
lizadoviaclientdeFTPouviaferramentadelinhadecomando;
•BasesdedadosMySQL:WAWSsuportatambémbancosdedadosMySQL.
Vocêcriarumanovabasededadosou,ainda,utilizarumabasejáexistente
152

## Página 163

CasadoCódigo Capítulo8. Publicandosuaaplicação
paraconectarsuaaplicação.ParaqueMySQLpudessefuncionarcomperfor-
manceeseguran çanomodelodecloud,aMicrosoftestabeleceuumaparceria
comumaempresaespecializada,chamadaClearDB;
•Escalabilidade:WindowsAzureWebSitesdisponibilizadoismodelospossí-
veisparaconseguirescala:compartilhadoereservado. Nomodocomparti-
lhadoépossívelaumentaronúmerodeprocessosreferentesàaplicaç ãoweb,
enquantonoreservadoépossívelpassaraaplicaç ãoparamáquinasvirtuais
dedicadasesubironúmerodemáquinasquerespondemparaasaplicaçõeslá
hospedadas;
•Segurança:WAWStrabalhaemmodo full trust.Istosignificadizerquetodas
asaplicaçõesque“rodam”emambientecompartilhadoencontram-secomple-
tamenteisoladasumasdasoutras.Esteéumcritérioimportanteaseravaliado
nomomentodeplanejarseuwebsite;
•Linguagenseframeworks:vocêjádeveterouvidofalarqueWAWSsuporta
nativamenteASP.NET,ASP.NETMVC,PHP,Node.js.Talvezoquevocênão
saibaéquesuasaplicaçõesASPclássicase2.0tambémsãosuportadas,logo,
seuscódigoslegadossãobem-vindosdentrodoWindowsAzureWebSites;
•WebDeploy:outracaracterísticaimportanteagregadaaoWAWSéaaceitação
depublicaçãodeaplicaçõesvia web deploy.Assim,sevocêutilizaasferramen-
tasdaMicrosoftparagerenciamentodecódigo(VS2010,VS2012,VS2013ou
WebMatrix),poderápublicardiretamenteatravésdelasnoWindowsAzure;
•NuGet:aorealizarodeploydesuaaplicaç ãonoWAWS,nãoémaisnecessário
enviarospacotesdeformaagregada.OWindowsAzureseencarregadereali-
zartaltarefaemtempodeexecuç ãonomomentodaimplantação;Domínios
personalizados:umadificuldadeencontradaporboapartedosdesenvolve-
doreswebqueutilizamwebrolesnoWindowsAzureéacriaç ãodedomínios
personalizados.ComWindowsAzureWebSites,aespecificaç ãodedomínios
personalizadostornou-seextremamentesimples,podendoutilizaropróprio
portaldeadministraçãoparaestefim.Entretando,éimportanteobservarque,
paraqueestafeaturefuncione,owebsitedeveestar“rodando”emmodore-
servado;
•Certificados:WindowsAzureWebSitesoferecemsuportenativoparautili-
zaçãodeSSLparadomíniosexternoseinternos;
153

## Página 164

8.6. Publicandoaaplicação‘CadêMeuMédico?’ CasadoCódigo
•IIS8,WindowsServer2012e.NET4.5:paraesteprimeiropreview,WAWS
nãoimplementaIIS8,WindowsServer2012e.NET4.5.Muitoemboraasno-
vasversõesaindanãosejamsuportadas,estasdeverãoserautomaticamente
implementadasàmedidaquesetornaremestáveis.Hojeoambienteé:IIS7.5,
WindowsServer2008R2e.NET4.5.
Umaperguntaquedeveestarperturbandosuacabe çanesteinstantedeveser:
“SeoWindowsAzurejápossuíaaswebroles,oquejustificaaexistênciademaisum
modeloprahostdeaplicaçõesweb?“.Acertei?
Arespostaésimples: Web rolessãoambientesquepermitemaltograudeper-
sonalizaçãoatravésde startup tasks. Oobjetivodas web rolesédisponibilizarum
ambientepara hostdeaplicaçõeswebmaisrobustoetotalmentepersonalizável,ao
passoqueoWAWSapresentaoutroviésemtermosdedemanda:asimplicidadeem
detrimentodapersonalização.
Sevocêprecisadeumambientepersonalizadocomo,porexemplo,implementar
característicasespecíficasnoIISou,ainda,adicionarnovasconfiguraçõesdeambi-
ente,WAWSnãosãoparavocê.Nestecaso,recomendamosconsiderarduashipóte-
ses: Web Rolesouorecursodemáquinasvirtuais.
8.6 P ublicando a aplicação ‘CadêMeuMédico?’
Vocêdeveestarseperguntandoaestaaltura:porquetantasinformaçõesacercado
WindowsAzureWebSites? Simples. Eleseráoambienteparaoqualfaremosa
publicaçãodaaplicação“CadêMeuMédico?”.
Criandooambientedepublicaç ãonoWindowsAzure
Iniciaremosoprocessodepublicaçãodenossaaplicaçãopelacriaçãoeprepa-
raçãodoambientede hostnoWAWS.Paraisso,comoprimeiropasso,sevocênão
possuiumaassinaturadoWindowsAzure,vocêdeverácriaruma.Parafazê-lo,basta
acessarowebsitedoWindowsAzure(http://windowsazure.com)eclicarnobotão
“Free Trial”.Natelaseguinte,cliquenobotão“Try it now”.Aofazê-lo,vocêserádi-
recionadoparaateladeautenticaçãodoWindowsAzure.Vocêprecisarádeum Live
IDparaacessaroserviço. Preenchaoformulárioqueseapresentará(incluindoo
númerodecartãodecréditointernacional).Nãosepreocupe,nadaserácobradoem
seucartão.Afigura 8.2apresentaaprimeiratelacomdadosaserempreenchidos.
154

## Página 165

CasadoCódigo Capítulo8. Publicandosuaaplicação
Figura8.2:AssinandooWindowsAzurepor3meses
Apósconcluiroprocessodeassinatura,oWindowsAzureliberaráumaquota
deUS$200,00paraquevocêpossautilizardaformaqueacharmelhor.Claro,utili-
zaremosparacriarnossoambientede host.
Comopróximopasso,acesseoendere çodoportaladministrativodoWindows
Azure:http://manage.windowsazure.com.Lá,informeseusdadoso Live ID(osmes-
mosqueutilizouparaassinaroWindowsAzure)ecliqueem“Sign In”.Setudocorreu
bem,vocêvisualizaráumatelasemelhanteàapresentadapelafigura 8.3.
155

## Página 166

8.6. Publicandoaaplicação‘CadêMeuMédico?’ CasadoCódigo
Figura8.3:PortaldeadministraçãodoWindowsAzure
Afigura8.3apresentaatelainicialdoportaladministrativodoWindowsAzure.
Notequeàesquerdaencontra-seomenuprincipaldoportal.Comocriaremosum
novosite,éclaroqueclicaremosnaop ção“Web sites”. Natelaqueseapresentará,
vocêdeveráclicarnolink“Create a web site”.Umajanelaseabriránorodapécomas
devidasopçõesselecionadas.Apenasadicionaremosonomedenossa“áreadehost”
(sugestivamente“livroaspnetmvc”).Aregiãoselecionadaserá“EastUS”.Afigura8.4
apresentaestatela.
156

## Página 167

CasadoCódigo Capítulo8. Publicandosuaaplicação
Figura8.4:Criandoumnovowebsite
Sevocêrepararbemnorodapédoportaladministrativo,veráumabarrade status
quenotificaousuáriofinalacercadoqueestáocorrendo.Setudocorrerbem,você
visualizaráonovoambientecriado,conformeapresentadopelafigura 8.5.
Figura8.5:Novoambientedehostcriadocomsucesso
Pronto!Ambientedehostcriado.Parafinalizarestaetapa,cliquenonomedo
ambientedehospedagem. Natelaqueseapresenta,cliquenolink“Download the
publish profile”.Aofazerisso,umarquivoXMLcomasconfiguraçõesdepublicação
serábaixado.Guardebemolocalondeestearquivoserásalvo.Eleseráutilizadono
157

## Página 168

8.6. Publicandoaaplicação‘CadêMeuMédico?’ CasadoCódigo
processodepublicação.Atelaqueexibeestaop çãopodeservisualizadaatravésda
figura8.7.
Figura8.6:Baixandooperfildepublicaç ão
Publicandoaaplicaç ão
Agoraquejápossuímosoambientede hostcriado,podemospublicarnossaapli-
cação.Comovocêiráconstatar,apublicaçãodeumaaplicaçãonoWindowsAzure
WebSitescomoVisualStudioéextremamentesimples.Nãopoderiaserdiferente,
jáqueosprodutossãodomesmofabricante.
Comoprojeto“Cadêmeumédico?”aberto(masnãoemexecução),cliquecom
obotãodireitosobreonomedoprojeto.Nomenuqueseabrirá,selecioneaop ção
“Publish...”.Aofazê-lo,umanovajaneladeparametrizaçãoseráexibida.Cliqueno
botão“Import”,disponívelimediatamenteafrentedocombo box.Najanelaquese
apresentará,selecioneaopção“Import from a publish profile file”ecliquenobotão
“Browse”.Navegueatéoarquivodepublicaçãoquebaixamosquandocriamosoam-
bientedepublicaçãoecliqueem“Open”.Aoselecionaroarquivoeclicarem“Ok”,
automaticamenteoVisualStudioalternaráaabade“Profile”para“Connection”,con-
formeapresentaafigura 8.7.
158

## Página 169

CasadoCódigo Capítulo8. Publicandosuaaplicação
Figura8.7:Informaçõesdepublicaçãoimportadas
Aoclicarem“Next”,owizardalternaráparaaaba“Settings”. Aquipoderemos
configurara stringdeconexãoparaobancodedados.Nestemomento,vocêpoderá
indicarumbancodedadosremotoaoqualsuaaplicaç ãoseconectará.Guardeeste
ponto.
Faremosumapausanestemomentoparapublicarmosobancodedadosdaapli-
cação.Oquefaremosaquiécriarumainstânciadobancodedadosde“CadeMeu-
MedicoBD”noSQL Databaseparasódepois,voltaraoVisualStudioparaapontara
aplicaçãoparaeste.
Migrandoobancodedadosdoambientelocalparaoonline
VoltandoaopaineladministrativodoWindowsAzure,nomenuprincipaldo
painel,cliquenaop ção“SQL Databases”.Natelaqueseabrir,cliquenaopção“Create
a SQL Database”.Informeonomedobancodedados,aedição(selecione“Web”),
otamanho,o collationeoservidorondeobancoserácriado.Atelaparametrizada
podeservisualizadaatravésdafigura 8.8.
159

## Página 170

8.6. Publicandoaaplicação‘CadêMeuMédico?’ CasadoCódigo
Figura8.8:Janelaparametrizadanacriaçãodobancodedados
Aoclicarnasetinhade“Next”,umajanelasolicitandoosdadosdoservidorde
bancodedadosseráapresentada. Informeusuárioesenhadeacessoaoservidor,
selecioneo datacenterondeesteservidorseráalocadoe,nasequência,cliqueem
“Ok”.Aetapadoisparametrizadapodeservisualizadaatravésdafigura8.9.
160

## Página 171

CasadoCódigo Capítulo8. Publicandosuaaplicação
Figura8.9:Segundajanelaparametrizadanacriaç ãodobancodedados
Setudocorreubem,vocêveráseubancodedadoscriadonatelaqueexibetodos
osrecursos,conformeilustraafigura 8.10.
Figura8.10:Bancodedadoscriadocomsucesso
Antesdemigrarmosobancodedadosdoambientelocalparaoonline,preci-
samosliberaroacessodosIP’spermitidosaobancodedadosnoWindowsAzure.
Claro,estebloqueioéfeitopormedidadeseguran ça.Entretanto,paraquepossamos
exemplificarofuncionamento,liberaremostodososIP’s.Paraisso,nocontextodo
bancodedadosrecém-criado,cliquenaaba“Dashboard”,localizadaimediatamente
abaixodonomedobancodedados.Najanelaqueseabrirá,cliquenaop ção“Manage
161

## Página 172

8.6. Publicandoaaplicação‘CadêMeuMédico?’ CasadoCódigo
allowed IP addresses”.Natelaqueseabrirá,vocêdeveráespecificarointervalodeIP’s
permitidos.Paraliberartodos,informamososvalores“0.0.0.0”até“255.255.255.255”,
istoé,todos.Afigura 8.11ilustraestaparametrização.
Figura8.11:EspecificandoIPspermitidosnobancodedadosdoAzure
Opassoseguinteconsistenamigraçãodobancodedadoslocalparaoambiente
online. Existemdiferentesformasparaserealizartalprocedimento. Optamospor
gerarum scriptutilizandoopróprio management studioe,então,executá-loneste
novoambiente.Vocêpodeencontrarumbomtextosobrecomogerar scriptsapartir
dobancodedadosatravésdestelink: http://bit.ly/gerandoscriptssql.
DepossedosdadosdeconexãocomobancodedadosnoWindowsAzure,utili-
zareiopróprio management studiopararealizaramigração,conformeilustraafigura
8.12.
Figura8.12:ConectandoaobancodedadosnoWindowsAzure
162

## Página 173

CasadoCódigo Capítulo8. Publicandosuaaplicação
Jáconectadoaobandodedados,selecioneocontextodobancodedados“Cade-
MeuMedicoBD”ecrieumanovaquery.Copieocódigogeradonoparágrafoanterior,
colenaabarecém-criadaeexecute-o.Setudocorreubem,vocêestarávisualizando
àesquerda(najanela Object Explorer)algosemelhanteaoqueéapresentadopela
figura8.13.
Figura8.13:Migrandoobancodedados
Voltandoàpublicação...
AgoraquejápossuímosobancodedadosjápublicadonoWindowsAzure,po-
demosseguircomoprocessodepublicaç ãodenossaaplicaçãoatravésdoVisual
Studio.Estávamosnaetapaondeconfigurávamosobancodedados,certo?Oque
precisaremosfazeragoraéapontarparaobancoqueacabamosdemigrar.Afigura
8.14apresentaaparametrização(queapontaparaobancoonline).
163

## Página 174

8.6. Publicandoaaplicação‘CadêMeuMédico?’ CasadoCódigo
Figura8.14:ApontandoaaplicaçãoparaobancodedadosnoWindowsAzure
Nasequência,cliqueem“Ok”e,aovoltarparaajanelaanterior,cliqueem“Next”.
Aúltimatelado wizardlheapresentaráaopçãodo preview.Estaetapanãoéobriga-
tóriamas,sevocêoptarporsuaexecução,oVisualStudioiráfazerumavarredurano
ambienteonlineecompararcomosarquivosdoprojetolocal.Assim,vocêpoderá
teradimensãoexatadequaisarquivosserãopublicados. Legal,não?! Aorealizar
estaoperação,oVisualStudioexibiuatelaapresentadapelafigura 8.15(semelhante
àquevocêdeveráestarvisualizando).
164

## Página 175

CasadoCódigo Capítulo8. Publicandosuaaplicação
Figura8.15:Previewdosarquivosqueserãopublicados
Porfim,cliquenobotão“Publish”.Aofinal,setudocorrerbem,oVisualStudio
abriráaaplicaçãojánoambienteonlinedoWindowsAzure,conformeilustraafigura
8.16.
Figura8.16:AplicaçãopublicadanoWindowsAzureWebSites
Comovocêpodenotar,oWindowsAzurecriaumsubdomínio(*.azurewebsi-
tes.net)paraaaplicação.Sequiséssemospersonalizarodomínio(http://seudominio.
165

## Página 176

8.7. Conclusão CasadoCódigo
com.br), bastarianosdirigirmosatéositeRegistro.breadicionarmosregistros
CNAMEqueapontariampara“http://livroaspnetmvc.azurewebsites.net/”.
8.7 Conclusão
Comovocêpôdeperceber,existemdiversasmaneirasparaquesepossapublicar
aplicaçõesASP.NETMVC.NopróprioWindowsAzure,existempelomenos3ma-
neirasdistintasparaexecutaresteprocedimento. Estecapítuloapresentouapenas
umadelas—amaissimples.Entretanto,éimportantemencionarqueaideiageral
nãomuda.
Esperamosque,aocompletaraleituradestelivro,vocêpossaterampliadoseus
horizontesemrelaçãoaosconhecimentostécnicosnoquesito“desenvolvimento
web”e,principalmente,considereutilizarASP.NETMVCaoprojetaraplicaçõesfu-
turas.
8.8 Código fonte e lista de discussão
OcódigofotedaaplicaçãoqueconstruímosnolivropodeserencontradonoGitHub
(http://bit.ly/mvc-livrocodigofonte),utilizesemprequenecessárioparareferência
nosestudosecontribuacomocódigofonte,faç aumforkeaguardamosseupull
request.
Além do código fonte um grupo de discussão (http://bit.ly/
mvc-livrogrupodiscussao) foi criado para conversarmos sobre ASP.NET MVC
edúvidasreferentesaolivro,aguardamossuaparticipação
166

## Página 177

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1] MicrosoftVirtualAcademy.Introduçãoàbusinessintelligence.2012.
[2] EricEnge. A arte de SEO.2010.
[3] SteveLydford.Building ASP .NET Web Pages with Microsoft WebMatrix.2011.
[4] W3CProtocols.Hypertexttransferprotocol-http/1.1.1999.
[5] FabrícioLopesSanchez. Enriquecendoovisualdesuaaplicaç ãocommaster
pages(blog).2010.
167