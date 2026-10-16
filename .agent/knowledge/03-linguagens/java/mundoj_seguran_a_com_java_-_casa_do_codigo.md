---json
{
  "id": "mundoj_seguran_a_com_java_-_casa_do_codigo",
  "title": "MundoJ Segurança com Java - Casa do Codigo",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `MundoJ Segurança com Java - Casa do Codigo.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "casa",
    "codigo",
    "com",
    "java",
    "linguagens",
    "mundoj",
    "seguran"
  ],
  "perguntas_tipo": [
    "Como utilizar MundoJ Segurança com Java - Casa do Codigo?",
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

# MundoJ Segurança com Java - Casa do Codigo

> **Arquivo Original:** `MundoJ Segurança com Java - Casa do Codigo.pdf`
> **Data Conversão:** 1643798097.0

---


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

## Página 3

CasadoCódigo Sumário
Sumário
1 Defendendo aplicaç ões web de ataques 1
1.1 Naturezadeumaaplicaç ãoweb . . . . . . . . . . . . . . . . . 2
1.2 Alteraçãodeparâmetros . . . . . . . . . . . . . . . . . . . . . 5
1.3 Descobrindosenhasdeusuário . . . . . . . . . . . . . . . . . 9
1.4 SQLInjection . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
1.5 ScriptInjectioneCrossSiteScripting . . . . . . . . . . . . . . 21
1.6 CookiePoisoning . . . . . . . . . . . . . . . . . . . . . . . . . 25
1.7 ServletFilters . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
1.8 Consideraçõesfinais . . . . . . . . . . . . . . . . . . . . . . . . 27
1.9 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2 Evitando acessos automatizados com CAPTCHA 29
2.1 TestedeTuring . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
2.2 JCaptcha . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
2.3 SimpleCaptcha . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
2.4 Kaptcha . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
2.5 QuebrandooCAPTCHA . . . . . . . . . . . . . . . . . . . . . 39
2.6 Consideraçõesfinais . . . . . . . . . . . . . . . . . . . . . . . . 40
2.7 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3 Certificaç ão digital com Java Cryptographic Architecture 43
3.1 Acertificaç ãodigital . . . . . . . . . . . . . . . . . . . . . . . . 44
3.2 Criptografia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
i

## Página 4

Sumário CasadoCódigo
3.3 Assinaturadigital . . . . . . . . . . . . . . . . . . . . . . . . . 49
3.4 Certificadodigital . . . . . . . . . . . . . . . . . . . . . . . . . 53
3.5 Seguran çanaplataformaJava . . . . . . . . . . . . . . . . . . 58
3.6 Padrõesdeassinaturas . . . . . . . . . . . . . . . . . . . . . . 63
3.7 Consideraçõesfinais . . . . . . . . . . . . . . . . . . . . . . . . 67
3.8 Referências. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
ii

## Página 5

Capítulo1
Defendendoaplicaçõeswebde
ataques
“Asegurançadeumaaplica çãowebémuitomaisdoquecolocá-laatrásdeum
firewalleconfigurarowebserverparautilizarSSL.Duranteaimplementa ção
daaplicação,deve-seestarsempreatentoparaentradasquepodemfazercom
queaaplica çãoajadeformainesperada.Existemataquesqueexploram
aplicaçõeswebobtendooacessoadadosefuncionalidadesaosquaisnãose
possuipermissão.Nesteartigo,serávistoofuncionamentodessesataqueseo
quepodeserfeitoduranteodesenvolvimentoparagarantiraprote çãodeuma
aplicaçãoweb.”
–porEduardoGuerra
Segurançaéumrequisitonão-funcionalmuitosério!Existeumarespon-
sabilidadeporpartedosdesenvolvedoresaoimplementarumaaplicaç ãoweb

## Página 6

1.1. Naturezadeumaaplicaçãoweb CasadoCódigo
queserádisponibilizadanainternet.Umaaplicaç ãoquetrabalhacominfor-
maçõesimportantesparaumaorganizaç ãonãopodeterseusdadoscorrom-
pidosouacessadosporquemnãopossuipermissão. Muitosdesenvolvedo-
res,provavelmentepordesconhecimento,nãosedãocontadessaresponsa-
bilidadeenãodãoadevidaaten çãoparaaseguran çaduranteaimplementa-
ção.Damesmaforma,queméresponsávelpelaseguran çadarede,também
pordesconhecimento,acabaignorandoasaplicaçõeswebcomoumpossí-
velpontovulnerável.Comonenhumacorrenteémaisfortequeseuelomais
fraco,aquelaaplicaçãowebacabasendoumalvopreferencialdepessoasmal
intencionadasquedesejamobterinformaçõessigilosasdaorganizaç ão.
Aprote çãocontraessesataqueséalgoquenormalmenteéfeitoporinici-
ativadosdesenvolvedores,vistoqueéincomumencontrarumrequisitonão-
funcionalcomo“Aaplicaçãodevebarrartentativasdeinje çãodeSQL”.Requi-
sitosnão-funcionaisdeseguran çanormalmentesãorelativosaomecanismo
deautenticaçãoedecontroledeacesso,masraramenteenvolvemataques,
mesmoporquequemfazaespecificaç ãomuitasvezesnãosabedaexistência
deles.Setodosessesfatoresaindaseuniremcomumcronogramaapertado,
tem-seumcenárioperfeitoparaqueaseguran çadaaplicaç ãosejadeixada
delado. Nesteartigo,veremosquaissãoosprincipaisataquesquepodem
serfeitoscontraumaaplicaç ãowebequemecanismospodemsercriados
parabarrá-los.Nãoserávistocomoéfeitaaseguran çadeclarativapelo :de-
ploymentdescriptor(oarquivo web.xml)oucomoseconfiguraumservidor
webparausaroprotocoloHTTPS.Apesardeessesaspectostambémserem
importantes,esteartigodarámaisênfaseaquestõesdeimplementaç ão,que
normalmentesãodeixadasdelado,doqueaconfiguraçõesparaseguran ça.
1.1 N atureza de uma aplicação web
Grandepartedosproblemasdeseguran çaqueumaaplicaç ãowebpodeapre-
sentartemrelaç ãocomoseumecanismodefuncionamento. Ofunciona-
mentobásicodoprotocoloHTTPéumcliente,normalmenteumnavegador,
enviarumarequisiçãoaumservidoreesseservidorenviarumarespostacom
ainformaçãosolicitada.Apósisso,nenhumaconexãoémantidaentreocli-
enteeoservidor,deformaque,paraoservidormanterinformaçõesdasessão
2

## Página 7

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
dousuárioentreasrequisições,éprecisoquealgumidentificadorsejaenvi-
adoacadarequisiç ão.Normalmente,éutilizadoum cookieouareescritade
URL.Depossedesseidentificador,épossível,dequalquermáquina,entrar
dentrodasessãodesseusuáriosemanecessidadedeautenticaç ão.
Emumaaplicaçãoweb,oservidorsimplesmenterespondeàsrequisições
recebidaseonavegadoréresponsávelpelaexibiç ãodapáginaemformato
HTMLepelaexecuç ãodoJavascript. Oquenãosepodeesqueceréqueo
navegadoréumavariávelforadecontroleequeosparâmetrosenviadospe-
lasrequisiçõespodemserqualquercoisa. Porexemplo: oparâmetrorela-
tivoaumcampodeumformulárioquelimitaa50onúmerodecaracteres
podechegaraoservidorcomumaquantidademuitomaiorqueisso. Esse
fatoocorre,poisnãosepodegarantirocomportamentononavegador,sendo
queosparâmetrospodemseralteradoslivrementeporumaoutraaplicaç ão,
como,porexemplo,usandoo SPIKE Proxy(vejaquadro).Emrelaç ãoaoJa-
vascript,ousuáriopodesimplesmenteoptarpornãoexecutareatémesmo
alterarocódigo,oquefazcomquenãosejaconfiávelautilizaç ãodeJavascript
paraaimplementaçãodequalquerregradenegócioimportante.Érecomen-
dadoutilizarJavascriptparatornarainterfacecomousuáriomaisinterativa
emaisresponsiva,porém,seumavalidaç ãoéfeitanoclienteparaaumentar
odesempenho,amesmavalidaç ãodeveserfeitanoservidorporquestõesde
segurança.
Comosenãobastassemessesproblemas,aindaexistemataquesdefor ça
bruta,deinje çãodeSQLeatémesmodeinje çãodeJavascript.Omaiorpro-
blemadetodosesseséque,muitoprovavelmente,elesserãoconsiderados
pelofirewallcomoumacessolegítimoàsuaaplicaç ão. Aúnicaop çãoque
restaécolocarnaprópriaaplicaç ãomecanismosdeseguran çaparaimpedir
essesataques,eéjustamenteoqueserámostradonesteartigo.
3

## Página 8

1.1. Naturezadeumaaplicaçãoweb CasadoCódigo
SPIKE Proxy
OSPIKEProxyéumproxy httppararealizaçãodetestesdesegu-
rançaemaplicaçõesweb. Elearmazenaaspáginasvisitadasepermite
que,depois,osmesmosrequestssejamreenviados,porémcomparâme-
trosmodificados.Aferramentasuportatestesdefor çabruta,SQL injec-
tioneCross-Site-Scripting.AversãomaisrecentedoSPIKEProxypode
serencontradanaURL:
http://www.immunitysec.com/resources-freesoftware.shtml.
Apósodownloaddaaplicaç ão,oarquivodeveserdescompactadono
diretório SPIKEProxye,naversãoWindows,éexecutadoatravésdo
arquivo runme.bat.Depoisdeiniciado,deveserconfiguradoonave-
gadorparautilizarcomoproxyoIP127.0.0.1eaporta8080.Ainterface
gráficapodeseracessadaapartirdaURL http://spike/,vejaafigura 1.1.
Navegandopelosdiretórios,pode-seteracessoàsURLsjáacessadase
osrequestspodemserreescritosapartirdeumformulárioHTML.Essa
ferramentaseráutilizadaparatestaraaplicaç ãodosexemplosmostrados
nesteartigo.
4

## Página 9

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
Fig.1.1:InterfacedoSPIKEProxy
1.2 A lteração de parâmetros
Aformamaissimplesdeburlarofuncionamentonormaldeumaaplicaç ão
webéatravésdaalteraçãodeparâmetrosdeumaformamaliciosa.Comessa
alteração,ousuáriopodeignorarvalidaçõesfeitasporJavascript,acessarin-
formaçõessempossuirpermissão,corromperdadoseatémesmocontornar
regrasdenegócio. Paraalterarosparâmetrosdeumarequisiç ão,elanão
precisaenviá-losviaquerystring,utilizandoométodo GET.Comométodo
POST,osparâmetrospodemserfacilmentealteradoscomoauxíliodeuma
ferramentacomooSPIKEProxy.
O controle de permissões declarativo feito através dodeployment
descriptoremumaaplicaç ãowebdefinediversosperfiseaautorizaç ãode
acessoacadaumdos servletsdosistema.Umusuárioautenticadoutilizando
aAPI JAASsópodeacessarumservletcasopossuaumdosperfisque
tenham autorização de acesso à URL mapeada para aquele recurso. Na
5

## Página 10

1.2. Alteraçãodeparâmetros CasadoCódigo
listagemaseguir,podeservistapartedeum deploymentdescriptor coma
configuraçãodeseguran ça.Observequeestãoressaltadasadefiniç ãodeum
papeleaautorizaç ãodeacessodessepapelpararecursosdaaplicaç ãoweb.
Normalmente,emaplicaçõesquenãoutilizamoJAASparaautenticaç ãoe
controledepermissões,aautorizaç ãodeacessocostumaserverificadano
níveldefuncionalidade(porexemplo:inserirusuário,excluirusuário)ouno
nívelderecurso(porexemplo: listaUsuario.jsp,servletmapeadopara
criarUsuario.do). Muitasvezes,essetipodecontrolenãoésuficiente
paraasregrasdenegóciodecontroledepermissãodaaplicaç ão.
Listagem 1.1- Exemplo de parte de um deployment descriptor com a
configuraçãodepapéisepermissões:
<?xml version="1.0" encoding="UTF-8"?>
<web-app ...>
...
<security-role>
<role-name>Admin</role-name>
</security-role>
<security-constraint>
<web-resource-collection>
<web-resource-name>Funcionalidade</web-resource-name>
<url-pattern>/insere.do</url-pattern>
<url-pattern>/exclui.do</url-pattern>
<http-method>POST</http-method>
</web-resource-collection>
<auth-constraint>
<role-name>Admin</role-name>
</auth-constraint>
</security-constraInt>
...
</web-app>
Vamossuporumaaplicaç ãode e-commerceemqueousuáriotemacesso
apenasasuasordensdecompra,masnãoadeoutrosusuários.Dessaforma,
mesmoousuáriotendoacessoàfuncionalidadedeconsultadeordens,nãoé
atodasasordensqueelepossuipermissãodeacesso.Nessecaso,apermissão
deixadesernoníveldafuncionalidadeepassaasernoníveldainformaç ão.
6

## Página 11

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
Imaginequenessaaplicaç ãoousuárioacesseumapáginacomalistagemde
suasordenseemcadalinhaexistaumlinkparaacessarosdadosdetalhados
daordem.Aoacessá-lo,seráfeitaumarequisiç ãoaumaoutrapágina,para
aqualserápassadocomoparâmetrooidentificadordaordemselecionada.
Seaaplicaç ãonãoverificarseousuáriologadopossuipermissãodeacessoà
ordemqueestátentandoabrir,serápossíveloacessoaqualquerordemdosis-
temasimplesmentealterandooparâmetropassadonaURL.Nafigura 1.2está
ilustradaasituaç ãodescritanesteparágrafo.Ofatodeumaordemnãoestar
listadanatabelanãosignificaquenãosejapossívelobteroacessoalterando
oparâmetro.Pormaisqueissopossaparecerinofensivonessecaso,imagine
queépossívelconstruirumaaplicaç ãoquerealizediversosacessosaessesis-
tema,criandorelatóriosquecompilaminformaçõescomtodasasordensde
suaempresa.
Fig.1.2:Exemplodousodaalteraç ãodeparâmetroparaoacessoaumain-
formaçãoàqualnãosetemautorizaç ão
OscamposocultosedesabilitadosemumapáginaHTMLnormalmente
possuemessecomportamentoparaimpedirasuaalteraç ãoporpartedousuá-
rio.Porém,comojáfoiditoanteriormente,essesparâmetrospodemserfa-
cilmentealteradosutilizandoumaferramentacomooSPIKEProxy.Node-
senvolvimentodeumaaplicaç ãoweb,essefatordeveserlevadoemconside-
7

## Página 12

1.2. Alteraçãodeparâmetros CasadoCódigo
ração. Porexemplo,imaginequeumformuláriodeediç ãodeinformações
deusuárioarmazeneoidentificadoremumcampoocultoeuseesseidentifi-
cadorparalocalizaraentidadenobancodedadosquedevesermodificada.
Quandooparâmetroquecarregaoidentificadorforalteradomaliciosamente
eoformulárioforsubmetido,casoaaplicaç ãonãopossuaalgumaprote ção
paraessetipodesituaç ão,podemsercorrompidosdadosaosquaisousuário
sequertinhaacesso.Aolocalizaraentidadenobancodedadospeloidentifi-
cador,comoessefoialterado,serãofeitasasmodificaçõesnaentidadeerrada,
oquepodeviolardiversasregrasdenegóciodasuaaplicaç ão. Afigura1.3
ilustraesseexemplo.
Fig.1.3:Exemplodousodaalteraç ãodeparâmetroparaacorrup çãodedados
Sabendodafacilidadedealterarqualquerparâmetrodaaplicaç ão,não
éconfiávelimplementarqualquerregradenegócioemJavascript. Umtipo
muitocomumderegradenegócioimplementadaemJavascriptéavalidaç ão
decamposdeumformulário. Essapráticaébastantecomum,muitasvezes
atéporquestõesdeperformance,poisousuárionãoprecisariairevoltarao
servidorparadizerqueoformatodeumdoscamposestáinválidoouque
umcamponãopreenchidoéobrigatório.Poroutrolado,essasvalidaçõesem
Javascriptpodemsercompletamenteignoradasedadosinválidospodemaca-
barsendoaceitospelaaplicaç ão.OJavascriptdeveserutilizadoparatornar
8

## Página 13

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
maisamigávelainteraçãodousuáriocomosistema.Nessecaso,éparaque
nãosejanecessárioesperarasinformaçõesiremevoltaremdoservidorpara
queumasimplesvalidaç ãosejarealizada.Porém,éprecisovalidaressasinfor-
maçõestambémnoservidor,paraquerequisiçõesmaliciosasnãoconsigam
executarumafuncionalidadecomparâmetrosinválidos.
Aseguir,háumapequenalistaderecomendaçõesparaquesuaaplicaç ão
nãosetornevulnerávelaumaalteraç ãodeparâmetros:
• Validesempreaspermissõesdousuárioaoacessarumafuncionalidade
naqualexistamregrasdenegóciopararestringiroacessodousuário
baseadonosdadosenãosomentenorecurso.
• Eviteguardaremcamposocultosinformaçõescríticasaofunciona-
mento da aplicação, que o usuário não poderia modificar normal-
mente,comoidentificadores,pre çosestatus.
• Casoousodecamposocultossejarealmentenecessário,façaumava-
lidaçãoqueosverifiqueassimquearequisiç ãochegaraoservidor.
• Valideasinformaçõessemprenoservidor,inclusiveotamanhodos
campos,independentementedeexistirounãoumavalidaç ãonona-
vegadorutilizandoJavascript.
• NãoutilizeJavascriptparaimplementarregrasdenegócioimportantes
eessenciaisparaseguran ça.Seforrealmentenecessário,lembre-sede
replicaralógicaevalidarasinformaçõesnoservidor.
1.3 D escobrindo senhas de usuário
Umdosobjetivosmaiscomunsdeumataqueaumaaplicaç ãocostumasera
obtençãodesenhasdeacesso.Umadasideiasmaissimplesdesefazerisso,
equemuitasvezesfuncionamuitobem,étentarváriaspossibilidadesdese-
nhaatéacertar.Issopodeserfeitocomautilizaç ãodetodasascombinações
possíveis,tambémconhecidocomoataquedefor çabruta,ouapartirdeuma
listapredefinidadepossíveissenhas,oquetambéméchamadodeataquede
dicionário. Noataquededicionário,oataquecostumaserdirecionadoao
9

## Página 14

1.3. Descobrindosenhasdeusuário CasadoCódigo
usuário,incluindonalistadepossíveissenhas:datasimportantes,nomesde
familiares,nomesdeanimaisdeestimaç ão,filmesfavoritosetc.
Essesataquessebaseiamnofatodequeépossívelrealizarváriastentativas
falhasdeautenticaç ãonosistema. Umadasformasdeimpediressetipode
ataqueéevitandoqueissosejapossível,bloqueandooacessodepoisdeum
númeromáximodetentativas. Essebloqueio,aprincípio,poderiaserfeito
nofirewall,porémmuitasvezesessanãoéumavariávelsobocontroledos
desenvolvedores. Dessaforma,amelhorop çãoseriacriarummecanismo
naprópriaaplicaç ãoquebloqueasseoacessotemporariamentecomvárias
tentativasfalhasdeautenticaç ão.
Umaformadeinseriressaverificaç ãoseminterferirnapartefuncional
dosistemaécomautilizaç ãodeumfiltro(paramaioresdetalhessobrefiltros,
vejaase ção Servlet Filtersnofinaldesseartigo).Napróximalistagem,está
umfiltroqueguardainformaçõesdasautenticaçõesfalhasdeusuáriosno
contextonaaplicaç ãoweb.Sãoparâmetrosdeconfiguraç ão,onúmeromá-
ximodetentativaseotempoemmilissegundosqueousuárioficabloqueado.
Listagem1.2-Filtroparaimpedirataquesdefor çabruta.:
public class ForcaBrutaFilter implements Filter {
private long tempoMilisegundos;
private int numeroTentativas;
public void init(FilterConfig config)
throws ServletException {
tempoMilisegundos = Long.parseLong(
config.getInitParameter("tempoMilisegundos"));
numeroTentativas = Integer.parseInt(
Config.getInitParameter("numeroTentativas"));
}
public void destroy() { }
public void doFilter(ServletRequest request,
ServletResponse response,
FilterChain chain) throws IOException, ServletException {
10

## Página 15

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
ServletContext context = ((HttpServletRequest)request)
.getSession().getServletContext();
ForcaBrutaControl control = null;
if(context.getAttribute("ForcaBrutaControl") == null){
control = new ForcaBrutaControl(
tempoMilisegundos,numeroTentativas);
context.setAttribute("ForcaBrutaCoNtrol", control);
} else {
control = (ForcaBrutaControl)
context.getAttribute("ForcaBrutaControl");
}
if(!control.podeLoggar(request)){
throw new ServletException("Seu IP está bloqueado.");
}
try {
chain.doFilter(request, response);
} catch (ServletException e) {
control.registraFalha(request);
throw e;
}
}
}
O filtro primeiramente busca uma instância da classe
ForcaBrutaControl, apresentada na listagem a seguir, no contexto
e,seainstânciaaindanãoexistir,elaécriada.Antesdeserchamadooservlet
queiráprocessaralógicadelogindaaplicaç ão,éverificadoseousuário
seencontrabloqueadoe,emcasopositivo,oacessoébarradonesseponto,
comolan çamentodeumaexce ção.Comousuárionãobloqueado,oservlet
responsáveléchamadoe,casoocorraalgumaexce çãoemsuaexecuç ão,é
registradaumafalhadeautenticaç ão.
Listagem1.3-Filtroparaimpedirataquesdefor çabruta.:
public class ForcaBrutaControl {
11

## Página 16

1.3. Descobrindosenhasdeusuário CasadoCódigo
private Map<String, RegistroFalha> tentativaPorIP =
new HashMap<String, RegistroFalha>();
private long tempoMilisegundos;
private int numeroTentativas;
public ForcaBrutaControl(long tempoMilisegundos,
int numeroTentativas) {
this.tempoMilisegundos = tempoMilisegundos;
this.numeroTentativas = numeroTentativas;
}
public void registraFalha(ServletRequest request) {
if (possuiIP(request) && !isTempoExpirado(request)) {
RegistroFalha falha = tentativaPorIP.get(
request.getRemoteHost());
falha.setTentativa(falha.getTentativa() + 1);
falha.setUltimaTentativa(System.currentTimeMillis());
} else {
RegistroFalha falha = RegistroFalha
.criarRegistroFalha(request);
tentativaPorIP.put(request.getRemoteHost(), falha);
}
}
public boolean podeLoggar(ServletRequest request) {
return !possuiIP(request) || isTempoExpirado(request)
|| !atingiuMaximoTentativas(request);
}
private boolean possuiIP(ServletRequesT request) {
return tentativaPorIP.containsKey(
request.getRemoteHost());
}
private boolean atingiuMaximoTentativas(
ServletRequest request) {
12

## Página 17

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
return tentativaPorIP.get(
request.getRemoteHost()).getTentativa()
> numeroTentativas;
}
private boolean isTempoExpirado(ServletRequest request) {
return tentativaPorIP.get(
request.getRemoteHost()).getTempo()
> tempoMilisegundos;
}
}
Aclassemostradanalistagemanterioréquepossuirealmentearegra
denegóciospararegistrarumafalhaeverificarseousuárionãoseencontra
bloqueado.Aclasse ForcaBrutaControlpossuium Mapparaarmazenar
astentativasfalhasdelogin, sendoqueachaveéoIPdeondeoacesso
foi realizado, e o objeto é uma instância da classeRegistroFalha,
representadanapróximalistagem. Aclasse RegistroFalhaéumbean
querepresentaasinformaçõesdeumatentativadeautenticaç ãosemsucesso.
Listagem 1.4- Classe que armazena informações sobre falhas de auten-
ticaçãonaaplicaç ão.:
public class RegistroFalha {
private String ip;
private int tentativa;
private long ultimaTentativa;
public static RegistroFalha criarRegistroFalha(
ServletRequest request) {
RegistroFalha falha = new RegistroFalha();
falha.setIp(request.getRemoteHost());
falha.setTentativa(1);
falha.setUltimaTentativa(System.currentTimeMillis());
return falha;
}
13

## Página 18

1.3. Descobrindosenhasdeusuário CasadoCódigo
public String getIp() {
return ip;
}
public void setIp(String ip) {
this.ip = ip;
}
public int getTentatIva() {
return tentativa;
}
public void setTentativa(int tentativa) {
this.tentativa = tentativa;
}
public long getUltimaTentativa() {
return ultimaTentativa;
}
public void setUltimaTentativa(long ultimaTentativa) {
this.ultimaTentativa = ultimaTentativa;
}
public long getTempo(){
return System.currentTimeMillis() - ultimaTentativa;
}
}
A próxima listagem mostra um exemplo de como configurar o filtro
ForcaBrutaFilterparaexecutarantesdoservletdeautenticaç ãoemuma
aplicaçãoweb.
Listagem 1.5- Exemplo de configuração do filtro da Listagem 2 em
umaaplicaçãoweb.:
<?xml version="1.0" encoding="UTF-8"?>
<web-app ...>
<display-name>AplIcacaoWeb</display-name>
<servlet>
<servlet-name>LoginServlet</servlet-name>
<servlet-class>
org.mundojava.servlet.LoginServlet
</servlet-class>
</servlet>
14

## Página 19

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
<filter>
<filter-name>ForcaBrutaFilter</filter-name>
<filter-class>
org.mundojava.filter.ForcaBrutaFilter
</filter-class>
<init-param>
<param-name>tempoMilisegundos</param-name>
<param-value>1200000</param-value>
</init-param>
<init-param>
<param-name>numeroTentativas</param-name>
<param-value>3</param-value>
</init-paRam>
</filter>
<filter-mapping>
<filter-name>ForcaBrutaFilter</filter-name>
<servlet-name>LoginServlet</servlet-name>
</filter-mapping>
<servlet-mapping>
<servlet-name>LoginServlet</servlet-name>
<url-pattern>/Login.do</url-pattern>
</servlet-mapping>
</web-app>
Oexemploapresentadofazdistin çãodeusuáriopeloIPdoqualfoiori-
ginadaarequisiç ão.Umfiltroparecidopoderiasercriadopararealizaressa
distinçãopelonomedeloginoupelasenha. Dessaforma,ficarárealmente
complicadoderealizarumataquedefor çabrutanosistema,mesmoseesse
ataqueforsofisticadoealterarmaliciosamenteoIPdeorigemdarequisiç ão.
Alémdessaprote ção,existemalgumasoutrasrecomendaçõesparadificultar
aindamaisataquesdessetipoaosistema:
• Imporumnúmeromínimodecaracteresnasenhaéumaboaprática,
poisonúmerodepossibilidadesqueprecisamsertestadasaumentaex-
ponencialmentecomonúmerodecaracteresdasenha.
• Obrigarousuárioapossuirnúmeros,letrasecaracteresespeciaisdi-
minuiapossibilidadedeeleutilizarumasenhafraca,oquetambém
reduzoriscodesucessodeumataquedotipodicionário.
15

## Página 20

1.4. SQLInjection CasadoCódigo
• Exigirtrocasdesenharegularmentefazcomqueousuárioacabenão
utilizandoasenhadasuaaplicaç ãoparaoutrossistemasereduztam-
bémoriscoemataquesdedicionário.
Valeressaltarqueprote çõesutilizadasemataquesdefor çabrutapodem
serutilizadasparaataquesdenegaç ãodeserviço(DoS).Emoutraspalavras,
oatacantebloqueiadeformapropositalusuáriosparaimpedirqueelesaces-
semosistema.Poressemotivo,algunssistemasevitambloquearusuários,e
emvezdissoestabelecemumtempomínimoentretentativasfalhasdelogin.
Dessaforma,alémdenãoabrirbrechaparaumataquedenegaç ãodeserviço,
evitaosdefor çabrutanosquaismilharesdetentativassãofeitasporsegundo.
Alémdessesataquesqueexploramsuaaplicaç ão,tambémexistemosque
exploramofatorhumanoenvolvidonautilizaç ãodeseusistema.Nessecaso,
tenta-seadquirirasenhatentandosepassarporumapessoaouumsistema,
deformaainduzirousuárioafornecê-lavoluntariamente.Aessapráticase
dáonomede engenharia socialeasuautilizaç ãosetornamaiscomumacada
dia.Éfrequente,porexemplo,receberume-mailfalsodealguémsepassando
porumbanco,comumlinkquedirecionaaumapáginaquesolicitaasenha
dousuário. Apesardenãoestarnoescopodesteartigo,essetipodeataque
nãopoderiadeixardesercitadoeoinvestimentonaeducaç ãodosusuáriosé
essencialparaqueoriscodessetipodeataquediminua.
1.4 SQL I njection
Essenãoéumataqueexclusivodeaplicaçõesweb,equalqueraplicaç ãona
qualoscomandosSQLsãoconstruídoscomconcatenaç ãodestringspodeso-
freresseataque.OSQLInjectionconsistenoenviodeparâmetrosdeformaa
alterarasinstruçõesSQL,fazendoaaplicaç ãosecomportardeformainespe-
rada.Osparâmetrossãoenviadosdeformaque,aoseremconcatenadoscom
umainstruçãoSQL,resultememumcomandoqueiráexecutarumainstru-
çãomaliciosanobancodedados.Afigura 1.4representaofuncionamentode
umaaplicaçãoqueutilizaaconcatenaç ãodestringsparaaformaç ãodeum
comandoSQLparaautenticaç ãodeumusuário. O containerwebrecebea
requisiçãocomosparâmetros,aaplicaç ãoosconcatenacomainstruç ãoSQL
eessaéenviadaparaexecuç ãonobancodedados. Nafigura 1.5,tem-seo
16

## Página 21

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
exemplodeSQLInjectionnamesmaaplicaç ão.Oparâmetroenviadocomo
login(quepodeservistonafigura 1.5)primeiramentefechaasaspasquedeli-
mitariaoparâmetro,depoisacrescentaumainstruç ãocondicionalquetorna
acláusula WHEREsempreverdadeirae,porfim,adicionadoistraçosparaco-
mentarorestodocomandooriginal. Comisso,consegue-seaautenticaç ão
naaplicaçãosemidentificadoresenhaválidos.
Fig.1.4: Representaçãodeumaaplicaç ãowebqueusaaconcatenaç ãode
stringsparaformarcomandosSQL
Fig.1.5:RepresentaçãodousodeSQLInjectionparaobteraautenticaç ãoem
umaaplicação
Otamanhodoestragoquepodeserfeitoporumataquedessetipode-
pendebastantedobancodedadosedodriverJDBCutilizado.Existemdri-
versque,porexemplo,nãoaceitamquesejamenviadasduasinstruçõesSQL
separadasporpontoevírgula.Outrosnãoaceitamquesejaminseridosdois
17

## Página 22

1.4. SQLInjection CasadoCódigo
traçosparacomentarpartedocomando.Obancodedadosutilizadotambém
podeinfluenciarnosdanoscausadospeloataque.OusodoSQLServer,por
exemplo,poressepossuir storedproceduresqueacessamdiretamentefunci-
onalidadesdosistemaoperacional,aumentaopotencialdedanoscausados
porumataquedesses. OSQLInjectionpodeserutilizadodediversasfor-
masecomobjetivosdistintos.Nasreferências,existeumartigoquedetalha
bastanteasváriasformasdeSQLInjection. Aseguir,estáapresentadauma
brevelistadediferentesmaneirasdesefazeroSQLInjection,lembrandoque
algunsdositenspodemnãofuncionaremvirtudedobancodedadosedo
driverJDBCutilizado:
• InserirumapartedoSQLdentrodeumparâmetrodeformaacriaruma
condicionalquesejasempreverdadeiraparaqueumaautenticaç ãoseja
realizadacomsucesso.
• CompletarcomandoSQLdaformadesejadaecomentarorestante.
• Colocarpontoevírgulaeinserirumnovocomandoadicionalcomo
criarouexcluirumatabela.
• InserirumacláusulaUNIONparaqueemumaconsultasejamretor-
nadosresultadosadicionaisaosdaconsultaoriginal,comoalistade
usuáriosesenha.
A utilização do mecanismo da classePreparedStatement para
a inserção dos parâmetros resolve esse problema, pois os caracteres são
codificadosdeformaanãosereminterpretadoscomopartedocomando
SQL.Alistagemaseguirmostraumtrechodecódigodecomoamesma
instruçãoSQLpoderiasercriadautilizando Statement(maisvulnerável
aSQLInjection)e PreparedStatement(comatraduç ãodecaracteres
especiais).
Listagem 1.6- Diferentes abordagens para execução de uma consulta
comJDBC.:
//Com Statement
String query = "select * from USUARIO where LOGIN=’"+login+
18

## Página 23

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
"’ and SENHA=’"+senha+"’ "
Statement stmt = c.createStatement();
ResultSet rSet = stmt.executeQuery(query);
//Com PreparedStatement
String query = “select* from USUARIO where LOGIN=? and SENHA=? "
PreparedStatement stmt = con.prepareStatement(updateString);
stmt.setString(1, login);
stmt.setString(2, senha);
ResultSet rSet = stmt.executeQuery();
Osframeworksdeacessoadados,comooHibernateeoiBatis,eAPIs
comooJPAtambémeliminamoriscodeataquesutilizandoSQLInjection.
Porém,deve-seteremmenteque,algumasvezes,surgemconsultascomvá-
riosparâmetrosquedevemserinseridoscondicionalmenteeaconcatenaç ão
destringsacabasendoamelhoralternativaparaasuacriaç ão. E,mesmo
tendograndepartedaaplicaç ãoprotegida,senãohouverodevidocuidado,
essaconsultaemqueasstringssãoconcatenadaspodeacabarsetornandoum
pontovulneráveldosistema.
Mesmocomautilizaç ãodeframeworkseAPIsqueprotegemaaplicaç ão
desse tipo de ataque, é interessante saber quando alguém está tentando
realizarumataqueàsuaaplicaç ão. Nalistagemaseguirestáumfiltroque
procuraindíciosdeumatentativadeSQLInjectionemtodososparâmetros
deumarequisiç ãoelan çaumaexce çãoquandoencontraalgo. Apesarde
poderhaverfalsospositivos(ouseja,seremidentificadosataquesquenão
realmenteosão),essefiltrojáéumapequenadicadecomoessetipode
ataquepodeseridentificadosemqueessaverificaç ãosemisturecomalógica
denegócios.Sãofiltradososcaracteresaspassimples,quesãoutilizadosna
delimitaçãodeparâmetrosemformatotexto, doistraços, queindicamo
iníciodeumcomentário,eopontoevírgula,quepodeserutilizadoparaa
separaçãodedoiscomandos.
Listagem 1.7- Filtro que busca indícios de SQL Injection nos parâme-
trosdeumaaplicaç ãoweb.:
public class SQLInjectionFilter implements Filter{
19

## Página 24

1.4. SQLInjection CasadoCódigo
public void init(FilterConfig arg0) throws ServletException{}
public void destroy() {}
public void doFilter(ServletRequest request,
ServletResponse response, FilterChain chain)
throws IOException, ServletException {
for(Object paramName : request.getParameterMap()
.keySet()){
String[ ] params =
(String[ ])request.getParameterMap()
.get(paramName);
for(String param : params)
if(param.indexOf("’")>=0
|| param.indexOf("--")>=0
|| param.indexOf(";")>=0){
throw new ServletException("SQL Injection");
}
}
chain.doFilter(request, response);
}
}
SegueumalistaderecomendaçõesqueajudamaevitaroSQLInjectione
adiminuirosdanoscasoumataqueocorra:
• UtilizaraclassePreparedStatementouframeworksdepersistência
quejáfazematraduç ãodecaracteres-chaveparaqueelesnãosejam
consideradospartedocomandoSQL.
• Filtrarevalidarosparâmetrosnoservidornachegadadasrequisições
pararejeitá-laoueliminaroriscodeSQLInjection.
• Alteraralgoritmodeautenticaçãodeformaarecuperarsomentease-
nhadousuárioedepoiscompará-lacomasenharecebidacomoparâ-
metro.
• Nãoexibirnatelamensagensdeexceçõesvindasdiretamentedobanco
dedados,poisessaspodemdarpistasdecomoestáaestruturadobanco
equalocomandoqueestásendoexecutado.
20

## Página 25

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
• Nãoutilizarasenhadeadministradorparaacessarobancodedados,
poisoatacantepoderáteracessoirrestritoàsinformações.
• Gravarassenhasdeusuárionobancodedadosutilizandoumalgo-
ritmode hashing,comooSHA1ouMD5,poismesmoseumatacante
obtiveracessoaessainformaç ão,assenhasestarãoprotegidas(oter-
ceiroartigodesselivromostracomogerarohashdeuma Stringem
Java).
1.5 S cript Injection e Cross Site Scripting
EssetipodeataqueexploraaformacomooconteúdoHTMLégeradopela
aplicaçãoecomoeleéinterpretadopelonavegador.Oatacanteenvianare-
quisiçãoparaaaplicaç ãowebparâmetroscompedaçosdeHTMLescripts
embutidos. Comisso,épossívelexecutarcódigonobrowserdousuárioda
aplicação,semqueeletenhaconhecimento.Umadaspossíveisconsequências
éosequestrodesessão,queérealizadoatravésdaobten çãodoiddesessão
peloatacante,pormeiodoqualoatacanteconsegueacessaraaplicaç ãoutili-
zandoasessãodooutrousuário.
Nafigura1.6podeservistaumarepresentaç ãodeumataquequeutiliza
oScriptInjectionparaalterarocomportamentodeumapáginanonavegador
dosusuários.Emalgummomentodaaplicaç ão,imaginequeumatacantein-
siranabasededadosumtextoqueserávisualizadoporoutrosusuáriosem
umapáginaHTML.Noexemplomostradonafigura,essetextoéexibidoem
umalertaquandoumdeterminadobotãoépressionado.Enviandoumtexto
malicioso,oatacantemodificaoJavascriptqueeraparaserexecutadoori-
ginalmenteeconsegueincluiroutroscomandosparaseremexecutados.No
exemplo,ocódigoinjetadoprovocaaexecuç ãodeoutrosalertas,incluindo
umqueexibeocookiecomoidentificadordesessãodousuário.
Damesmaformacomoovalordoidentificadordasessãopodeserexi-
bidonatela,eletambémpodeserenviadoparaumoutrositecontroladopelo
atacante,oqueéconhecidocomo CrossSiteScripting. Substituindoovalor
docookie JSESSIONIDemumarequisiç ão,pode-seentrarnasessãodesse
usuário.Essapráticaéconhecidacomosequestrodesessãoefazcomquea
aplicaçãoreconhe çaoatacantecomoumusuáriojáautenticado.Existeminú-
21

## Página 26

1.5. ScriptInjectioneCrossSiteScripting CasadoCódigo
merasformasdeseinjetarcódigoemumapáginaHTMLfazendocomquea
mesmasecomportedeformainesperada.Nocasodeumtextoqueserásim-
plesmenteexibidonapágina,seriapossívelinjetartagsHTMLcomfiguras,
elementosdescripteatémesmoapplets.Existeumartigonasreferênciasque
oferecemaisdetalhesdecomoessetipodeataquepodeserrealizado.
Fig.1.6:RepresentaçãodousodeSQLInjectionparaobteraautenticaç ãoem
umaaplicação
Paraprevenirqueessavulnerabilidadesejaexploradaemumaaplicaç ão,
existembasicamenteduasabordagens. Aprimeiraébloquearqualquerre-
quisiçãocomalgumparâmetrodequesesuspeitequepossuascriptinjetado.
Aimplementaçãodessebloqueiopodeserfeitacomumfiltroequivalenteao
22

## Página 27

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
utilizadoparabloquearataquesdeSQLInjectionmostradonase çãoanterior.
Aúnicamudan çaseriaoscaracteresprocurados,quenestecasoincluiriam
<e >,porexemplo. Adesvantagemdessaabordageméapossibilidadede
detecçãodefalsospositivos.Asegundaabordagemseriatrocaroscaracteres-
chaveporentidadesHTML,deformaqueoconteúdodavariávelsejasempre
consideradotexto,enuncaumatagoupartedeumscript.Adesvantagemé
quenãoseriapossívelidentificaratentativadeumataque,eesseseriasim-
plesmenteevitado.Parausaressasegundamaneira,umaop çãoéautilizaç ão
datag <out>da“Core”librarydoJSTL.Essatagpossuiafunçãodesim-
plesmenteimprimirumvalornapágina,porém,comoatributo escapeXML
iguala true,éfeitaatradu çãodoscaracteresespeciais.Noexemplodafigura
1.6poder-se-iasubstituirousodaEL ${obs}por:
<c:out escapeXml="true" value=’${obs}’></c:out>
Osequestrodesessãoéumadaspioresconsequênciasdosataquesde
ScriptInjection. Mesmoutilizandotécnicasparaevitarainje çãodescripts,
aindaépossívelsequestrarasessãocapturandooidentificadordealgumaou-
traforma,comointerceptandoumpacotenaredeouinvadindoamáquina
dousuário.Umapráticadesegurançausadaemalgumasaplicaçõeséaimple-
mentaçãodeummecanismodentrodaaplicaç ãoqueimpe çaousodamesma
sessãopordoisIPsdiferentes. Comisso,casooidentificadordasessãoseja
capturado,natentativadesefazeroacessoapartirdeumaoutramáquina,a
sessãoseráencerradaeoacessoserábloqueado.Oproblemadessaaborda-
gem,queatornanemsempreadequada,équeemredesmóveisdeoperadoras
decelular,eaomudarderedesemfio,oIPpodeseralterado,eumacessolegí-
timoseriaconsideradoinválido,gerandoanecessidadedeousuáriorealizar
novamenteaautenticação.
Na listagem a seguir temos o exemplo de um filtro que realiza essa
tarefa. Inicialmente,ofiltrorecuperaoobjetoquerepresentaasessãodo
usuário,porémsemcriarumanova,casoessaaindanãoexista. Nasessão,
é armazenado um atributohost que contém o IP de onde foi feito o
primeiroacesso. Nocasodeoatributo hostserdiferentedapropriedade
remoteHostdorequest,issosignificaqueaquelasessãoestásendoacessada
deumamáquinadiferentedeondeelafoicriada. Quandoissoacontecer,
23

## Página 28

1.5. ScriptInjectioneCrossSiteScripting CasadoCódigo
seráinvalidadaelan çadaumaexce ção. Seasessãoforcriadaduranteo
processamentodarequisiç ão,nofinaldofiltroéinseridooatributo host
paraarmazenaroIPparaoqualelafoicriada.
Listagem 1.8- Filtro que impede o sequestro de sessão não deixando
queumamesmasessãosejaacessadadeumIPdiferente.:
public class SessionHijackingDetectionFilter implements Filter {
public void init(FilterConfig arg0) throws ServletException {
}
public void destroy() {
}
public void doFilter(ServletRequest request,
ServletResponse response, FilterChain chain)
throws IOException, ServletException {
HttpSession session = ((HttpServletRequest)request)
.getSession(false);
if(session != null){
String sessionHost =
(String)session.getAttribute("host");
String requestHost = request.getRemoteHost();
if(!sessionHost.equals(requestHost)){
session.invalidate();
throw new ServletException(
"Possível sequestro de sessão!");
}
}
chain.doFilter(request, response);
session= ((HttpServletRequest)request).getSession(false);
if(session != null
&& session.getAttribute("host") == null){
24

## Página 29

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
String requestHost = request.getRemoteHost();
Session.setAttribute("host",requestHost);
}
}
}
1.6 C ookiePoisoning
Comofoivistonosataquesanteriores,grandepartedeleséfeitaapartirda
alteraçãodeparâmetrosdeumarequisiç ãoàaplicaç ãoweb.Comoessespa-
râmetrosestãosobocontroledousuário,elepodemodificá-losdeformama-
liciosavisandoexploraralgumavulnerabilidadequeexistanaaplicaç ão.Não
podemosesquecerqueoscookiestambémsãoumtipodeparâmetroqueé
enviadocomarequisiç ãoequeestãosobocontroledousuário. O Cookie
Poisoningconsistenaalteraçãomaliciosadecookies,quepodemvisaràexe-
cuçãodequalquerumdosataquesacima,comooSQLInjection,porexemplo.
Portanto,osmesmoscuidadosquesuaaplicaç ãopossuircomparâmetrosdo
requestelatambémdevetercomasinformaçõescontidasnoscookies.
1.7 S ervlet Filters
UmfiltronaAPIdeServletséumcomponentequeinterceptaumarequisi-
çãoepodeexecutarcomandosantesedepoisdeelasertratadaporumSer-
vlet.Umfiltroprecisaimplementarainterface Filter,quepossuiosmé-
todos init(), destroy()e doFilter().Ométodo doFilter(),que
échamadoquandoumarequisiç ãoéinterceptada,possuiumparâmetrodo
tipo FilterChain,querepresentaacadeiadefiltrosqueestáprocessando
estarequisição. Váriosfiltrospodemserexecutadosemsequênciaemuma
mesmarequisição,conformemostradonodiagramadesequênciadafigura
1.7.Aoreceberumarequisiç ão,ofiltropodefazeralgumpré-processamento
e,emseguida,aochamarométodo doFilter()dainstânciadaclasse
FilterChain,invocaropróximofiltroouoServletqueirátratá-la.Quando
essemétodo doFilter()retorna,ofiltroretomaocontroleepoderealizar
algumpós-processamentonarequisiç ão.
Ousodefiltroséumaop çãointeressantequandoseestáimplementando
25

## Página 30

1.7. ServletFilters CasadoCódigo
umaaplicaçãoweb.Característicasnão-funcionais,ouseja,quenãosãodi-
retamenterelacionadascomregrasdenegócio,sãoexcelentecandidataspara
seremimplementadasdentrodefiltros.Dentrodessacategoria,estãoincluí-
dasverificaçõesdeseguran çaparaprocurarparâmetrosmaliciososemuma
requisição.Nesteartigo,foramvistosexemplosdefiltrosquefazemverifica-
çõesdeseguran çaecomopodemserconfiguradosparainterceptaraexecu-
çãodeumServletno deploymentdescriptordeumaaplicaçãoweb.Segueuma
listadevantagensdousodefiltros:
• Desacoplaosaspectosnão-funcionaisdasregrasdenegócio.
• Evitaduplicaçãodecódigo,vistoqueumfiltropodeinterceptarrequi-
siçõesdediversosServlets.
• Podeserreutilizadoemváriasaplicações,poissuaexecuçãoétranspa-
renteparaosServlets.
• Podeserhabilitadoedesabilitadocomconfiguraçõesno deployment
descriptor.
26

## Página 31

CasadoCódigo Capítulo1. Defendendoaplicaçõeswebdeataques
Fig.1.7:Diagramadesequênciademonstrandocomoumacadeiadefiltrosé
chamadaantesdeumServlet
1.8 C onsiderações finais
Gostariamuitodepoderterminaresteartigodizendoquecomessasreco-
mendaçõessuaaplicaç ãowebestarátotalmentesegura.Infelizmente,issonão
éverdade,poisquemprotegeumaaplicaç ãodevesepreocuparemtapartodos
osburacos,porémquemfazoataquesóprecisadescobrirum.Nesteartigo,
forammostradasváriastécnicasparaeliminarosprincipaistiposdevulne-
rabilidadequepodemexistiremumaaplicaç ãoweb. Oquepossoafirmar
éque,comcerteza,comessescuidadosvocêaumentarábastanteonívelde
segurançadasuaaplicaç ão.Segueumalistacomexemplosdeoutrosfatores
quedevemserlevadosemconsideraç ãoparaaseguran çadeumaaplicaç ão
web:
• Segurançadaredeemqueaaplicaç ãoestálocalizada,bloqueandopor-
tasdeadministraç ão,porexemplo.
27

## Página 32

1.9. Referências CasadoCódigo
• Modelodecontroledeacessoquepermitabloquearoacessoàsinfor-
maçõesàsquaisumusuárionãopossuirpermissão(observarapossi-
bilidadedaalteraç ãodeparâmetros).
• Comunicaçãocomoutrasaplicaçõesoucamadasremotas,comouma
camadaEJBouoacessoaumWebService.
• Gerenciamentodasexceçõesdeseguran çaqueforemlan çadasnaapli-
cação,paraquesepossaterconhecimentodosataquesqueestãosendo
feitoscontrasuaaplicaç ão.
• Auditoriadasaçõesdosusuáriosdosistema,tornandopossívelrastrear
açõesdeusuárioseencontrarresponsáveisporaçõesindevidasquefo-
remexecutadasnosistema.
Alémdequestõesrelativasàseguran ça,nesteartigotambémfoivisto
comoisolarotratamentodeseguran çadorestodaaplicaç ão. Comoesses
problemascomseguran çadeaplicaçõeswebsãorecorrentes,émuitobom
poderisolaralógicadedetecç ãodeataquesparaqueelapossaserreutilizada
emváriasaplicações. Nesteartigo,utilizamososfiltrosdaAPIdeServlets
paraisolaressetipodefuncionalidade,porémpode-seutilizarqualquertipo
decomponentequeintercepterequisições,comoos InterceptorsdoStruts,ou
atémesmoumaspecto. Isolandoasregrasdenegóciodocódigoquefazo
tratamentodeseguran ça,épossívelobternãosóumaaplicaç ãomaissegura,
mastambémumaaplicaçãocomumamodelagemflexíveledequalidade.
1.9 R eferências
• SegurançacontraHackers:J2EEeJava;ArtTaylor,BrianBuege,Randy
Layman;EditoraFutuRa.
• Segurança contra Hackers: Aplicações Web; Joel Scambray, Mike
Shema;EditoraFutura.
• SiteSeguro–AplicaçõesWeb;JeffForristal;AltaBooks.
28

## Página 33

Capítulo2
Evitandoacessosautomatizados
comCAPTCHA
“CAPTCHA(CompletelyAutomatedPublicTuringtesttotellComputersand
HumansApart)éumrecursoutilizadoparadeterminarseumusuárioé
humanoounão.Asuaimplementa çãomaisconhecidasãoimagens
distorcidasemqueousuárioprecisalê-laedigitá-laparaprosseguircoma
operação.Éumrecursocadavezmaisusadoemsitesdainternetetempor
principalobjetivoevitarqueferramentasautomatizadasacessemum
determinadorecursodosite.Oobjetivodesteartigoéapresentaroconceitopor
trásdeCAPTCHAetambémmostraralgumasalternativasdecódigoaberto
paraimplementá-loemaplicaçõesJava.”
–porMateusBahiaeRodrigoCunhadePaiva

## Página 34

2.1. TestedeTuring CasadoCódigo
Ainternetéumambientebastantehostil.Ataquesaumdeterminadosite
vêmdetodososlados,comarmascadavezmaispoderosas,natentativade
degradarperformance,comprometerdados,derrubarservidoresetc. Você
podeseprotegercom patchesdeseguran ça,validaçãodecampos,criptogra-
fiaeoutrastécnicas,massempreexistemnovostiposdeataqueseéneces-
sárioestarpreparado. Umadasprincipaisferramentasdeataqueéopoder
computacional.Avelocidadecomqueumcomputadorpodefazermilhares
derequisiçõesparamilharesdesiteséincrível.Frequentemente,issoéusado
ofensivamente,masseusadocommoderaç ãopodenãoparecerumataqueao
site.Umexemploclássicoocorrecomsitesqueoferecemendere çodee-mail
gratuito. Épossívelconstruirumprogramaqueregistremilharesdecontas
dee-mail,comobjetivodefazerspam. Paraessessites,édifícil,senãoim-
possível,diferenciarumbrowsercontroladoporumserhumanoouporum
programa.Qualasoluç ão?Comoumsitepodediferenciarrequisiçõesinici-
adasporhumanosderequisiçõesgeradasporumprograma?
Nesteartigo,vocêvaiconhecerateoriasobreoCAPTCHA,amelhor
formapararesolveroproblemaapresentado.Alémdisso,vocêvaisaberpor
queelefoicriadoealgumasalternativasparaimplementá-loemJava,usando
JCaptcha,SimpleCaptchaeKaptcha.Nofinal,vamosapresentaralgumastéc-
nicasquepodemserutilizadasnatentativadesequebrarumCAPTCHA.
2.1 T este de Turing
AlanTuringapresentouaideiaparamáquinasdeTuring.Eleacreditavaque
umdiacomputadoresteriaminteligênciacomparáveisàhumana.Elepropôs
umjogodeimitaç ão.Coloqueumcomputadoremumasala,eumhumano
emoutra,ambosseparadosporuminterrogadorhumano(quenãosabequem
estáemcadasala).Esteinterrogadorfazperguntasparaambose,quandosa-
tisfeito,eleadivinhaemqualsalaestáocomputadoreemqualsalaestáo
humano.Seointerrogadornãoconsegueacertararespostacorretamaisda
metadedasvezes,ocomputadorpassanotesteeéconsideradotãointeli-
gentequantooserhumano.OTestedeTuringébaseadonoproblemadeum
humanodiferenciarumcomputadordeoutrohumano.Nonossoproblema,
nósprecisamosdocontrário. Umcomputadorprecisadiferenciarentreum
30

## Página 35

CasadoCódigo Capítulo2. EvitandoacessosautomatizadoscomCAPTCHA
humanoeoutrocomputador,oqueémuitomaiscomplexo. Estecenárioé
conhecidocomo T este de Turing Reverso.
Pararesolveresseproblema,em2000,cientistascriaramoCAPTCHA.
CAPTCHAéumacrônimodaexpressão CompletelyAutomatedPublicTuring
testtotellComputersandHumansApart (TestepúblicodeTuringcompleta-
menteautomatizadoparasepararcomputadoresehumanos). Éumtipode
teste“desafio-resposta”usadoparagarantirquearespostanãoégeradapor
computador.
Comooutroscomputadoressãoincapazesdegerararesposta,qualquer
usuárioqueentrecomasoluç ãocorretaépresumidamentehumano. Um
tipocomumdeCAPTCHArequerqueousuárioidentifiqueasletrasdeuma
imagemdistorcida.Masexistemoutrasop ções,incluindosons(usadospara
deficientesvisuais),reconhecimentodeanimaisouatéderostoshumanos.
Asfiguras2.1e 2.2mostramalgunsexemplosdeCAPTCHA.Afigura 2.1
éumtipomaiscomplexodeCAPTCHAemqueousuárioprecisaidentificar
oqueestásendomostradonaimagem.Afigura 2.2éumtipomaiscomum,
noqualousuárioprecisaidentificarasletrasqueestãoexibidasnaimagem.
Naspróximasse çõesserãoapresentadasalgumasferramentasparaseimple-
mentarCAPTCHAemJava.
Fig.2.1:ExemplodeCAPTCHAmaiscomplexo:Qualotipodeanimal?
31

## Página 36

2.2. JCaptcha CasadoCódigo
Fig.2.2:ExemplodeCAPTCHAmaiscomum:Digiteoscaracteresexibidos.
2.2 JC aptcha
UmdosframeworksJavamaistradicionaisparaimplementaç ãodeCAPT-
CHAéoJCaptcha,distribuídosob GNULesserGeneralPublicLicense.Uma
grandevantagemdeleéser multi-typechallenge,oquesignificaqueelepode
gerardesafioscomimagens,textosousons.Issoéumdiferencialsevocêes-
tiverimplementandoumsitelargamenteutilizado,ouumsiteemquevocê
precisasepreocuparcomacessibilidadeedeficientesvisuaisestariamimpos-
sibilitadosdepassarnotestedasimagens.
VejaospassosnecessáriosparaintegraroJCaptchaàsuaaplicaç ão:
Passo 1:adicione jcaptcha-all.jare commons-collection-3.2
ousuperiornodiretório WEB-INF/libdoseusite;
Passo 2: implementeo CaptchaService(precisaserum singleton),
mostradonapróximalistagemnaclasse CaptchaServiceSingleton;
Listagem2.1-ImplementaçãodoCaptchaServiceparaoJCaptcha.:
import com.octo.captcha.service.image.ImageCaptchaService;
import com.octo.captcha.service.image
.DefaultManageableImageCaptchaService;
public class CaptchaServiceSingleton {
private static ImageCaptchaService instance =
new DefaultManageableImageCaptchaService();
public static ImageCaptchaService getInstance(){
return instance;
32

## Página 37

CasadoCódigo Capítulo2. EvitandoacessosautomatizadoscomCAPTCHA
}
}
Passo 3: implemente o servlet gerador da imagem do CAPTCHA,
mostradonalistagemseguintenométodo doGet();
Listagem2.2-ImplementaçãodoCaptchaServiceparaoJCaptcha.:
protected void doGet(HttpServletRequest httpServletRequest,
HttpServletResponse httpServletResponse)
throws ServletException, IOException {
byte[] captchaChallengeAsJpeg = null;
// saída do stream para escrever a imagem captcha dentro
ByteArrayOutputStream jpegOutputStream =
new ByteArrayOutputStream();
try {
//Obtém Id da sessão que vai identificar o captcha gerado
//O mesmo id precisa ser usado para validar a resposta
String captchaId = httpServletRequest.
getSession().getId();
// Chama o método ImageCaptchaService getChallenge
BufferedImage challenge = CaptchaServiceSingleton
.getInstance().getImageChallengeForID(captchaId,
httpServletRequest.getLocale());
// jpeg encoder
JPEGImageEncoder jpegEncoder = JPEGCodec
.createJPEGEncoder(jpegOutputStream);
jpegEncoder.encode(challenge);
} catch (IllegalArgumentException e) {
httpServletResponse.sendError(
HttpServletResponse.SC_NOT_FOUND);
return;
} catch (CaptchaServiceException e) {
httpServletResponse.sendError(
HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
return;
33

## Página 38

2.2. JCaptcha CasadoCódigo
}
captchaChallengeAsJpeg = jpegOutputStream.toByteArray();
// resposta da requisição
httpServletResponse.setHeader("Cache-Control", "no-store");
httpServletResponse.setHeader("Pragma", "no-cache");
httpServletResponse.setDateHeader("Expires", 0);
httpServletResponse.setContentType("image/jpeg");
ServletOutputStream responseOutputStream =
httpServletResponse.getOutputStream();
responseOutputStream.write(captchaChallengeAsJpeg);
responseOutputStream.flush();
responseOutputStream.close();
}
Passo 4: adicioneno web.xmlareferênciaaoservletcriadoanterior-
mente,comomostradonalistagemseguinte;
Listagem2.3-Alteraçãodoweb.xmlparaoJCaptcha:
<servlet>
<servlet-name>jcaptcha</servlet-name>
<servlet-class>ImageCaptchaServlet</servlet-class>
<load-on-startup>0</load-on-startup>
</servlet>
<servlet-mapping>
<servlet-name>jcaptcha</servlet-name>
<url-pattern>/jcaptcha</url-pattern>
</servlet-mapping>
Passo 5:crieoformuláriocontendoodesafio,comonalistagemseguinte;
Listagem2.4-Formuláriocomodesafio,paraoJCaptcha:
<img src="/jcaptcha">
<input type=’text’name=’resposta_captcha’value=’’>
Passo 6:criearotinadevalidaç ão,mostradanalistagemaseguir.
34

## Página 39

CasadoCódigo Capítulo2. EvitandoacessosautomatizadoscomCAPTCHA
Listagem2.5-Rotinadevalidaç ãoparaoJCaptcha.:
Boolean respostaCorreta = Boolean.FALSE;
//Lembre-se que usamos um ID, no servlet?
//Aqui usaremos o mesmo para recuperar.
String captchaId = httpServletRequest.getSession().getId();
//Recupera a resposta
String response =
httpServletRequest.getParameter("resposta_captcha");
// Chama o serviço
try {
respostaCorreta = CaptchaServiceSingleton.getInstance()
.validateResponseForID(captchaId, response);
} catch (CaptchaServiceException e) {
//Este erro não deve ocorrer,
//a menos que você tenha usado um id inválido
}
Afigura2.3apresentaexemplosdeimagensgeradaspeloJCaptcha.
Fig.2.3:ExemplosdeimagensgeradaspeloJCaptcha.
2.3 S impleCaptcha
OSimpleCaptchaéumaimplementaç ãoJavaopensource(distribuídosob
BSDLicense),comopropósitodegerarbonsCAPTCHAscomomínimode
35

## Página 40

2.3. SimpleCaptcha CasadoCódigo
programaçãoeconfiguraç ão. Aimplementaçãopadrãopermiteconfigurar
coresdobackground,fontes,bordas,geradoresdecaracteres,entreoutras
opções.
Aconfiguraçãoéfeitapormeiodo web.xml.Todososvalorespodem
serdeixadosembranco,eaimplementaç ãopadrãoseráusada.Oservletdo
CAPTCHAcolocaránasessãoumachavequepodeserobtidaporum con-
troller.
Basicamente,oquevocêprecisafazeréconfigurarum ServletMappingno
web.xmlepronto.Oservletmapeadoéresponsávelporreceberarequisiç ão,
colocarovalordoCAPTCHAnasessãoeretornaraimagemparaobrowser.
Paraintegraçãocomsuaaplicaç ão,bastaseguirospassosadiante:
Passo 1:copieo simplecaptcha.jardentrodo WEB-INF/libdesua
webapp;
Passo 2:crieummapeamentodeservletno web.xml,comonalistagem
aseguir;
Listagem2.6-Alteraçãoaserfeitanoweb.xmlparaoSimpleCatpcha:
<servlet>
<servlet-name>jcaptcha</servlet-name>
<servlet-class>ImageCaptchaServlet</servlet-class>
<load-on-startup>0</load-on-startup>
</servlet>
<servlet-mapping>
<servlet-name>jcaptcha</servlet-name>
<url-pattern>/jcaptcha</url-pattern>
</servlet-mapping>
Passo 3:noseu jsp,crieumatagdeimagemeumacaixadetextopara
obteraentradadousuário,comonotrechomostradoaseguir;
Listagem2.7-ImagemecaixadetextonoJSPparaoSimpleCaptcha:
<img src="Captcha.jpg"> <input type=”text”name=”captcha”/>
**Passo4
Listagem2.8-Rotinadevalidaç ãoparaoJCaptcha.:
36

## Página 41

CasadoCódigo Capítulo2. EvitandoacessosautomatizadoscomCAPTCHA
String kaptchaExpected = (String)session.getAttribute(
nl.captcha.servlet.Constants.SIMPLE_CAPCHA_SESSION_KEY);
String kaptchaReceived = request.getParameter("kaptcha");
if (kaptchaReceived == null ||
!kaptchaReceived.equalsIgnoreCase(kaptchaExpected)) {
setError("kaptcha", "Invalid validation code.");
}
Pronto. Agorafaçaotratamentoenviandoousuárioparaapáginade
sucessooumostrandoumamensagemdeerro.
Vocêaindapodefazerdiversasconfiguraçõesno web.xml,taiscomo
cor,borda,fonte,tamanhodaimagemetc.Acesseositedoprojeto(videre-
ferências)paramaisdetalhessobrecomofazeressasconfigurações.Afigura
2.4mostraalgunsexemplosdeCAPTCHAsgeradospeloSimpleCaptcha.
Fig.2.4:ExemplosdeCAPTCHAsgeradospeloSimpleCaptcha.
UmaobservaçãoimportantesobreoSimpleCaptchaéqueoprojetofoi
descontinuadoenãoestámaissendomantido. Alémdisso,elesófunciona
paraJDK1.6.Mesmosendomuitosimplesdeusar,essesfatorespodeminvi-
abilizaroseuuso.
2.4 K aptcha
OKaptchaéumaversãomodernadoprojetoSimpleCaptcha,distribuídosob
ApacheLicense2.0.OusobásicodoKaptchanasuawebappémuitosimples
emuitoparecidocomoSimpleCaptcha.Tudooquevocêprecisafazeréadi-
cionaro jarparaseuprojeto,fazerreferênciaao kaptcha servlet no
37

## Página 42

2.4. Kaptcha CasadoCódigo
seu web.xmlecompararovalorCAPTCHAgeradonasessãocomoqueo
usuáriosubmeteunoseuformulário.
Nota:seestiverusandoJCaptchanamesmaaplica çãoqueoKaptcha,você
teráconflitoscomabibliotecadegera çãodeimagem.
VejaaseguirosdetalhesdecomointegraroKaptchaàsuaaplicaç ão:
Passo 1:coloqueo .jar file nodiretório WEB-INF/libdasuaapli-
cação;
Passo 2: coloqueareferênciadoservletnoseu web.xml, comona
listagemaseguir;
Listagem2.9-Alteraçãoaserfeitanoweb.xmlparaoKaptcha:
<servlet>
<servlet-name>Kaptcha</servlet-name>
<servlet-class>
com.google.code.kaptcha.servlet.KaptchaServlet
</servlet-class>
</servlet>
<servlet-mapping>
<servlet-name>Kaptcha</servlet-name>
<url-pattern>/kaptcha.jpg</url-pattern>
</servlet-mapping>
Passo 3:coloqueatagdeimagemecaixadetextonasuapágina,como
napróximalistagem;
Listagem2.10-ImagemecaixadetextonoJSPparaoKaptcha.:
<form action="submit.action">
<img src="kaptcha.jpg" />
<input type="text" name="kaptcha" value="" />
</form>
Passo 4: noseucontroller,compareovalorinseridopelousuáriocom
ovalordachavedeCAPTCHAarmazenadanasessão,usandoumcódigo
comoodalistagemaseguir.
Listagem2.11-Filtroparaimpedirataquesdefor çabruta.:
38

## Página 43

CasadoCódigo Capítulo2. EvitandoacessosautomatizadoscomCAPTCHA
String kaptchaExpected = (String)request.getSession()
.getAttribute(
com.google.code.kaptcha.Constants.KAPTCHA_SESSION_KEY);
String kaptchaReceived = request.getParameter("kaptcha");
if (kaptchaReceived == null ||
!kaptchaReceived.equalsIgnoreCase(kaptchaExpected)) {
setError("kaptcha", "Invalid validation code.");
}
Nota: tenha certeza de que você inicializou o jdk com
-Djava.awt.headless=true.
DamesmaformacomonoSimpleCaptcha,vocêpodefazerdiversascon-
figuraçõesno web.xml,taiscomocor,borda,fonte,tamanhodaimagemetc.
Acesseositedoprojeto(videreferências)paramaisdetalhessobrecomofa-
zeressasconfigurações.Afigura 2.5mostraalgunsexemplosdeCAPTCHAs
geradospeloKaptcha.
Fig.2.5:ExemplosdeimagensgeradospeloKaptcha.
2.5 Q uebrando o CAPTCHA
ÉilusãoacharqueoCAPTCHAvaieliminar100%daschancesdealguém
criarumprogramaquepossadesvendarodesafioeconseguirsepassarpor
umserhumano. Nãohácomogarantirqueapenashumanosvãopassarno
teste.Naverdade,háalgumasvulnerabilidadesconhecidasnamaioriadasim-
plementações.Hoje,jáexistemserviçosnainternetquesepropõemadesven-
dardesafiosdosCAPTCHAs(conhecidospor SoftwareasaService –Saas).
ExistemservidoresqueaceitamumaimagemCAPTCHAdecomputadorese
tentamresolvê-las(porumataxacobrada).Ataxadesucessodosserviçosé
muitoboa–umaemcincosoluçõesretornadas.
39

## Página 44

2.6. Consideraçõesfinais CasadoCódigo
Quebrando com uso de OCR
UmaabordagemparaquebrarCAPTCHAéamesmausadaparareco-
nhecimentodeobjetos,comoasaplicaçõesquereconhecempessoasemum
vídeo.Aessênciadosproblemasésimilar.Nonossocaso,queremosencon-
trarasletras“A”,“B”,“C”emumaimagem.Adistorçãodaimagemésuficiente
paraconfundiroOCR(OpticalCharacterRecognition),masusandotécnicas
decomputaçãoépossívelidentificarcorretamentecercade90%dasimagens.
Issotudoempoucossegundos.
Quebrando sem uso de OCR
A maioria das implementações de CAPTCHAs não destrói a sessão
quandoafrasecorretaéinserida. Logo,reutilizandooiddasessãodeuma
imagemCAPTCHAconhecida,épossívelautomatizarrequisiçõesaumapá-
ginaprotegidaporCAPTCHA.
Portanto,umaboapráticaésempreremoverovalordoCAPTCHAda
sessão,depoisqueafrasecorretaéinserida.IssonemsempreéfeitopelaAPI
e,portanto,deveficaracargododesenvolvedor.
2.6 C onsiderações finais
EsteartigoapresentouoconceitodeCAPTCHAemostroualgumasop ções
deAPIsJavaparasuageraç ão.Alémdisso,tambémcomentamossobrecomo
umdesafioCAPTCHApodeserquebrado.
DasAPIsapresentadasnesteartigo,sevocêforusaraimplementaç ãopa-
drão,amelhorop çãoéaAPIKaptcha,poiselaémuitofácildeconfigurare
produzumtestedifícildeserquebradopormáquina.Sevocêquiseralterara
aparênciadaimagem,existemváriasopçõesdeconfiguraçõesquepodemser
facilmentealteradasno web.xml.
OSimpleCaptchatambéméumaótimasolução.Contudo,parecequenão
estásendomantidoetambémháerrosaoexecutaroprojetocomJDK1.5eo
headerHTTPdesaídadoservlet.Existemalgunserrosreportados, patchese
mensagensdefórumnotificandoproblemas.
OJCaptchatambéméumgrandeproduto,masémaisumabiblioteca
doqueumasoluç ãorápida.AsimagensCAPTCHApadrãoproduzidassão
40

## Página 45

CasadoCódigo Capítulo2. EvitandoacessosautomatizadoscomCAPTCHA
muitodifíceisparaumserhumanoler,oufáceisdeseremquebradasporcom-
putador.Alémdisso,suaAPIsuportadesafiosnãoapenascomimagens,mas
tambémcomsons.
2.7 R eferências
• Wikipédiahttp://en.wikipedia.org/wiki/Captcha
• JCaptchahttp://jcaptcha.sourceforge.net/
• SimpleCaptchahttp://simplecaptcha.sourceforge.net/
• Kaptchahttp://code.google.com/p/kaptcha/
• Configuração do Kaptcha http://code.google.com/p/kaptcha/wiki/
ConfigParameters
41

## Página 47

Capítulo3
CertificaçãodigitalcomJava
CryptographicArchitecture
“Acertificaçãodigitaltemsidobastantecomentadanosúltimostemposeem
diferentesesferasdogovernoeempresasprivadas.Elatemporobjetivo
asseguraraidentidadedeumapessoaatravésdeprocedimentoslógicose
matemáticosconsiderados,atéentão,seguros.Opresenteartigotempor
objetivoapresentarosconceitosbásicosenvolvidosnatecnologia,bemcomo
algumascaracterísticasefuncionalidadesdisponibilizadaspelaplataforma
Javaqueagregamconfiabilidadenasaplica çõesqueexigemaltograude
segurança.”
–porAmanRathieeDiegoAugustoRodriguesGomes
Ainternet,desdeosprimórdios,éumaformacolaborativadecompar-
tilharinformaçõesedefacilitaracomunicaç ãoentrediferentespontosdo

## Página 48

3.1. Acertificaçãodigital CasadoCódigo
globo. Entretanto,suasfuncionalidadesnãoselimitamapenasaisso: elas
foramsendoincrementadascomodesenrolardotempoecomodesenvolvi-
mentodatecnologia.Comocrescimentodainternet,cadavezmaisaspes-
soasrealizamsuastransaçõesbancáriaseefetuamcomprassemsairdecasa,
tudoatravésdaweb.Issofazsurgirnovasoportunidadesdenegócio.Neste
contexto,foinecessáriocriarmecanismosdeseguran çamaiseficientesque
cobrissemtaistransações.Crimesvirtuaissetornaramcomunseperigosos;
pragasvirtuaissedisseminamfacilmente;pessoascome çaramasepassarpor
outrasparaaplicargolpes.Enfim,aseguran çadesteambientesetornouum
pontobastantequestionávelecrítico.Atrocadedocumentossigilosos,por
exemplo,sefeitademaneirainsegura,permitequesejaminterceptadospor
terceiros,causandodanosimprevisíveis.
Acertificaçãodigitalsurgiucomoumaformaderealizarumatrocase-
guradeinformaçõesentrediferentespontosnãoconfiáveis,deformaqueo
destinatáriodamensagemsoubessequeméoremetenteevice-versa.Tendo
emvistaacrescenteutilizaç ãodomeioeletrôniconerealizaç ãodeoperações
queexigemmaiorgraudeseguran ça,asempresasqueprestamtaisserviços
prezamcadavezmaispelaconfiabilidadeemsuasaplicaçõeseorientamos
seusclientesaseprotegeremdefraudesatravésdacertificaç ãodigital.
Naprimeirapartedoartigo,serãoabordadososconceitosteóricosde
criptografia,assinaturaecertificadosdigitais.Maisadiante,mostraremosum
poucodaarquiteturaedosuportequeaplataformaJavaprovêparaousoda
certificaçãodigital.Boaleitura!
3.1 A certificação digital
Acertificaçãodigitaltemcomoobjetivocobrirbasicamentequatroaspectos
deseguran çanomeiodigital:autenticidade,integridade,privacidadeenão-
repúdio.Aseguir,descrevemoscadaumdessesobjetivos:
•Autenticidade:garantequeoconteúdodamensagemenviadaé,real-
mente,doremetentequeaenviou.Visagarantirqueninguémse“pas-
sou”peloverdadeiroemissor.
•Integridade:garantequeamensagemnãosofreualteraçõesnocami-
nhoentreoremetenteeoreceptor.
44

## Página 49

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
•Privacidade ou confidencialidade:impedequeoconteúdodamensa-
gemsejalidoporpessoasnãoautorizadas.
•Não-repúdio: registrodaprovadaparticipaç ãoedainten ção. No
mundoreal,trata-sedeumterceirodeconfian çaqueregistracompro-
missos(testemunhas,porexemplo).
Paraentendercomoessesobjetivossãoaplicadosnacertificaç ãodigital,
éimportanteconheceralgunsconceitosbásicossobrecriptografia.
3.2 C riptografia
Emperíodosdeguerrasésemprevantajosoparaumladoconhecerinforma-
çõessecretasdoseuinimigo.Nodecorrerdotempo,muitastécnicasforam
elaboradasparaevitarqueumladodoconflitoconseguisseinformaçõesso-
breoseuoponente.E,mesmoquandoestasinformaçõeseramconseguidas,
elasdeveriamserinúteisparatal,ouseja,nãopoderiamsercompreendidas
poraquelesaosquaiselasnãosedestinavam.Taisobjetivos,hojelargamente
utilizadosemaplicaçõescomerciais,sãoalcan çadospelacriptografiadasin-
formações.
Muitojáseouviufalaremcriptografia,masqualoconceitoportrásdesta
palavraequaissãoastécnicasutilizadas?Acriptografia(dogrego kryptós,“es-
condido”,egráphein,“escrever”)nasceudestanecessidadeemesconderalgo
escritoparaoutraspessoas.Amensagemécodificadadeformaqueapenaso
seudestinatáriotenhacondiçõesdecompreendê-la,poissomenteeledetéma
chavequeirádecodificarainformação.Emtermosmaistécnicos,acriptogra-
fiaéoestudodeprincípiosetécnicasdesetransformarainformaç ãoapartir
deumaformalegível(plaintext oucleartext)paraumaformacodificadaou
cifrada(ciphertext oucodetext).Estainformaç ãoemformacodificadageral-
mentetemumaspectoilegível,ouseja,nãofazomenorsentidoparaquem
estálendo.
Criptografia simétrica
Acriptografiasimétrica,tambémconhecidacomocriptografiadechave
secreta,éotipomaisintuitivodentreoutrostipos. Ométodosimétricoda
45

## Página 50

3.2. Criptografia CasadoCódigo
criptografiatemsetornadobastantefortecomodesenvolvimentodama-
temáticaeocrescimentodopodercomputacional. Issotempossibilitadoa
criaçãodecifrasquesãopraticamenteinquebráveiscomopoderdeproces-
samentodasmáquinasatuais.
Acriptografiasimétricaenvolveousodeumachavesecretaconhecida
apenaspelosparticipantesdacomunicaç ãosegura. Oemissorcriptografaa
mensagemcomestachave,conhecidaapenasporeleeporseudestinatário,e
enviaamensagemcriptografadaparaodestinatário.Odestinatário,deposse
damesmachave,decodificaamensagemetemacessoaoseuconteúdo.
Ousodacriptografiasimétricanãoestárestritoapenasaoenviodemen-
sagensporummeiodetransmissãoinseguro.Elatambémpodeserutilizada
pararealizarumaautenticaç ãomútuaforte. Estaautenticaçãomútuaforte
éagarantiadequeasduaspontasdacomunicaç ãosãoaspontasdequese
esperaqueestabele çamacomunicaç ãoequeestãoseguras.Exemplo:‘João’
e‘Maria’definemumachavesecretaparaacriptografiadasmensagens.Esta
chavesecretapodeserumapalavra,umafrase,umasequênciadenúmeros,
enfim,estáacargodelesemdefinirestachavequesetornaráumsegredo
compartilhado.
Paratercertezadeque‘Maria’e‘João’secomunicamdeformaseguraem
umcanalinseguro,elespodemrealizaroseguinteprocedimento:
• ‘João’enviaumamensagempara‘Maria’dizendo: “Oi,meunomeé
João";
• ‘Maria’geraumamensagemaleatóriaeenviapara‘João’;
• ‘João’iráreceberestamensagem,irácriptografá-lautilizandoachave
secretacompartilhadacom‘Maria’eiráretornaressamensagemcrip-
tografadaparaela;
• ‘Maria’ vai receber a mensagem criptografada de ‘João’ e irá
descriptografá-lacomachavecompartilhada.Verificandoqueamen-
sagemrecebidaéamesmamensagemenviadaanteriormente.Verifica-
seque,defato,apessoadooutroladodaconversaéo‘João’.Nestemo-
mento,‘Maria’sabequeapessoacomquemsecomunicapossuiconhe-
cimentodachavesecreta.Comosepressupõequeachaveéconhecida
46

## Página 51

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
apenaspelosrespectivosemissorereceptor,infere-sequeoreceptoré
‘João’;
• ‘João’realizaomesmoprocedimentodeenviodeumamensagempara
‘Maria’;
• ‘Maria’criptografaamensagemcomachavesecretaeretornaamen-
sagemcriptografadapara‘João’;
• ‘João’decifraamensagemeconfirmaqueestásecomunicandocom
‘Maria’.
Esteéumprocedimentobásicodeautenticaç ãomútua. Oleitorqueti-
verinteressepodeconferiroprojetoKerberosdoMIT(http://web.mit.edu/
Kerberos/). OKerberoséumprotocolodeautenticaç ãomútuaqueutiliza
criptografiaparagarantirautenticidadeeprivacidadeemumcanaldecomu-
nicaçãoinseguro.
Tendoemvistaqueexistemoutrasformasdecriptografia,éimportante
destacaralgumasdasvantagensedesvantagensdacriptografiasimétrica.
V antagens:
• Osalgoritmosdecriptografiasimétricasãogeralmentemaisrápidos.
• Sãomaisapropriadosparaoprocessamentodestreamsdedadosgran-
des.
• Chavessimples.
Desvantagens:
• Presume-sequeambasaspartestenhamconcordadonaescolhadeuma
chaveeestejamhabilitadasacompartilharemessesegredodeforma
segura.
• Háoperigode,nocompartilhamentodachave,essasinformaçõesse-
remindesejavelmenteinterceptadasporterceiros.
47

## Página 52

3.2. Criptografia CasadoCódigo
Existemdiversosalgoritmosdecriptografiasimétricaquesãoampla-
menteutilizadosnosprotocolosderedehojeemdia:DES,3DESeAESsão
algunsdeles.OAES(AdvancedEncryptionStandard )foiselecionadoemum
concursorealizadopeloNIST(NationalInstituteofStandardsandTechno-
logy),emmeadosde2000,comooalgoritmopadrãodecriptografiasimé-
trica.
Criptografia assimétrica
Acriptografiaassimétrica,tambémconhecidaporcriptografiadechave
pública,utilizaduaschavesdiferentesnoprocessodecriptografiaedescripto-
grafia.Estesistemadecriptografiadechaveassimétricafoipublicadoprimei-
ramenteem1976porWhitfieldDiffieeMartinHellman.Osparticipantesde
umacomunicaçãosegurautilizandocriptografiaassimétricadevempossuir
umpardechavesúnico,conhecidocomochavepúblicaechaveprivada.
•Chave pública:quepodeseracessadaporqualquerum.Comoopró-
prionomediz,épúblicaetodostêmdireitoatê-laouaacessá-la.
•Chave privada:deveserapenasacessadaeconhecidapeloseupropri-
etário.Nãopodeserdisponibilizadaparaterceiros.
Estas duas chaves são matematicamente dependentes uma da outra,
sendoqueumamensagemcriptografadacomachaveprivadasópoderáser
descriptografadacomsuachavepúblicacorrespondenteevice-versa.
V antagens:
• Maiorsegurança,poisachavequecompartilhamoséachavepública.
Nãoexisteproblemaalgumemsuadistribuiç ão.
Desvantagens:
• Geralmentemaislentosqueosalgoritmosdecriptografiasimétrica.
Algunsalgoritmosassimétricosconhecidossão:osdecurvaselípticas,El
Gamal,DSAeRSA.OpoderdoalgoritmoRSA,nomedadoemhomena-
gemaoscriadoresRonRivest,AdiShamireLenAdleman,sebaseianalógica
48

## Página 53

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
dafatoraçãodoprodutodedoisnúmerosprimosgrandes,algocomputaci-
onalmentecomplexoparaosprocessadoresatuaiscalcularem. Poressara-
zão,quantomaioronúmerodebitsdaschaves,maisdifícilserádequebrá-la.
UmestudofeitopelaUniversityofBritishColumbiamostrouque,paraque-
brarumachaveassimétricade1024bits,considerando-seumcomputador
quepossaprocessarummilhãodeinstruçõesporsegundo,seriamnecessá-
rios300bilhõesdeanos.Notequeouniversopossui“apenas”13,7bilhõesde
anos.
3.3 A ssinatura digital
Paramelhorentenderoprocessodeassinaturadigital,podemosfazeruma
analogiaaoprocessodeassinaturaconvencional.Quandoassinamosumdo-
cumento,porexemplo,anexamosumtipodeidentificaç ãoqueéteoricamente
únicaepessoal,equepodeserverificadaatravésdeoutrodocumento,como,
porexemplo,acarteiradeidentidadeouumpassaporte. Oproblemaéque
aassinaturamanualnãoédifícildeserforjada,oquediminuisuaconfiabili-
dade.
Aassinaturadigitalvisasolucionarosproblemasdeautenticaç ãoeinte-
gridadedosdadossendotransmitidosdigitalmente.Paragarantiraautenti-
cidade,precisamosdeumcódigodigitalquesejaúnicoparaotransmissor.
Comovimosanteriormente,esterecursoéachaveprivada,queseráutilizada
para“assinar”umamensagemouarquivosendoenviadopelarede.Quando
assinamosumdocumentodigital,anexamostambémnossocertificadodigi-
tal,queiráconterdiversasinformações,taiscomonossachavepública,au-
toridadecertificadoraqueemitiuocertificado,validadedocertificado,da-
dospessoaiseoutros(falaremossobrecertificadosdigitaismaisadiante).De
possedessasinformações,oreceptordamensagempoderealizardiversosti-
posdeverificações,taiscomoseaautoridadecertificadoraéconfiável,seo
certificadoexpirououatémesmoseocertificadofoicriadoparaaquelefim
específico.
Ousuárioquedesejaassinarumdeterminadodocumentoutilizasua
chaveprivadaparageraroutrodocumento,estecontendoagorasuaassina-
turaeodocumentooriginal. Existemcasosemqueaassinaturaeodocu-
49

## Página 54

3.3. Assinaturadigital CasadoCódigo
mentooriginalnãosãocolocadosemumúnicoarquivo,massim,enviados
separadamente.Nãoexistenenhumproblemanisso,poisnoatodaverifica-
ção,comoveremosmaisafrente,qualquermodificaç ãonodocumentoinvi-
abilizasuavalidaç ão.
Umavezenviadososdados(odocumentooriginaleaassinaturadigital),
oreceptorpodeverificaraautenticidadedosdadosatravésdachavepública
doemissor,esuaintegridade,garantindoqueodocumentonãofoiviolado
durantesuatransmissão.
Processo de assinatura digital
SuponhaqueDiegodesejaenviarumamensagemparaRoger,comacer-
tezadequeseRogerareceber,saberáquefoiDiegoqueaenviou. Oque
Diegofazinicialmenteégeraro hashdesuamensagemutilizandoalgunsdos
algoritmosdehashconhecidos(paraentendermelhor,leiaase çãosobre hash
aseguir).Depossedesuachaveprivada,Diegocriptografaohashdamen-
sagemgerada,resultandonoqueconhecemoscomoaassinaturadigitalda
mensagem.Notequenessecasonãoestamospreocupadoscomaprivacidade
damensagem.
DiegoenviaamensagemeaassinaturadigitalparaRoger.Depossedos
dados,RogerutilizaachavepúblicadeDiegoparadescriptografaraassina-
turadigitalrecebida,resultandonohashoriginaldamensagem. Paraveri-
ficarqueoarquivonãofoicorrompidooualteradoduranteoenvio,Roger
calculaohashdamensagemnovamenteutilizandoomesmoalgoritmode
Diegoecomparacomaquelequeacaboudedescriptografar.Seosdoistive-
remomesmovalor,RogerteráacertezadequeosdadosvieramdeDiegoe
quenãoforamalterados.
Essefoiumexemplobásicodecomoaassinaturadigitalgaranteaauten-
ticidadeeaintegridadedamensagem(verfigura 3.1).Éimportantenotarque
aassinaturaporsisónãogaranteaprivacidadedamensagem.Nocaso,para
queDiegopudesseteracertezadequesomenteRogeriráleramensagem,ele
teriaquecriptografartambémamensagem,enãosomenteohashdela.Esta
criptografiaseriafeitautilizando-seachavepúblicadeRoger.Assimsendo,
somenteRogerpoderiadescriptografá-lacomsuachaveprivada(vejafigura
3.2).
50

## Página 55

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
Fig.3.1:Assinaturadigitalsemprivacidade.
51

## Página 56

3.3. Assinaturadigital CasadoCódigo
Fig.3.2:Assinaturadigitalcomprivacidade.
Hash
Umhashnadamaisédoqueumasequência“única”decaracteresgera-
dosapartirdeumadeterminadaentrada. Paraasseguraraintegridadeda
informaçãosendotransmitidaentreduasentidades,utiliza-seumafun ção
dehash. Umafun çãodehashrecebecomoentradaumainformaç ão,que
podeserdesdeumsimplestextoouatémesmoumarquivo,eproduzcomo
saídaatalsequênciadecaracteres,conhecidatambémcomo messagedigest
oudigitalfingerprint.Elapodeserproduzidapordiversosalgoritmosdehash
existentes,dentreosquaisosmaisconhecidossãooSHA-1eoMD5.Ohash
produzidocontémumtamanhofixodebits,definidopeloalgoritmo.Qual-
queralteraçãonamensagem,pormínimaqueseja,deveproduzirumhash
totalmentediferente.
Umbomalgoritmodehashdeveseguirasseguintespropriedades:
52

## Página 57

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
• dadox,deveserdifícilencontrarm,talquex=hash(m). Emoutras
palavras,nãosepodeencontraramensagemoriginalapartirdoseu
hash(PreimageResistant);
• deveserdifícilencontrarduasentradasdiferentesm1em2talque
hash(m1)=hash(m2)(CollisionResistant ).
Dessaforma,qualqueralteraç ãoquehouveremumamensagemfarácom
queohashgeradosejadiferentedooriginal,resultandonaquebradaintegri-
dadedainformaç ão. Raramente,podeocorrerdedoisarquivosdiferentes
geraremhashesiguais.Issoéconhecidocomocolisãodehashepodesermi-
nimizadoutilizando-sealgoritmoseficientesequegeremsequênciasmaiores
decaracteresparaohash.
Otrechodecódigoaseguir,mostracomopoderíamosobterohashMD5
deumastringqualquer(noteatotaldiferen çanohashquandoalteramosum
pequenotrechodastring):
String msg1 = "mensagem qualquer";
String msg2 = "mensagem qualquer 2";
MessageDigest md = MessageDigest.getInstance("MD5");
BigInteger hash1 = new BigInteger(1, md.digest(msg1.getBytes()));
BigInteger hash2 = new BigInteger(1, md.digest(msg2.getBytes()));
System.out.println("hash md5 msg1 = " + hash1.toString(16));
System.out.println("hash md5 msg2 = " + hash2.toString(16));
Resultado:
hash md5 msg1 = c421076352a520329710f24772205b0b
hash md5 msg2 = 1af4017ba84dfbc3f1fb922906282f20
3.4 C ertificado digital
Umcertificadodigitaléumdocumentoeletrônicoquetemporfinalidade
identificarpessoasfísicas,jurídicaseatémesmoservidores(deaplicaç ão,web
etc.). Quandoassinamosumdocumento,“anexamos”nossocertificadodi-
gitalàassinatura,paraqueestepossaserlidopeloreceptor. Ocertificado
digitalcontémdiversasinformaçõesqueidentificamaentidadeemquestão,
53

## Página 58

3.4. Certificadodigital CasadoCódigo
taiscomonomeeCPFemumcertificadodeumapessoafísica. Outrasin-
formaçõesidentificamavalidadeearevogaç ãodocertificado. Entretanto,
duasinformaçõesmerecemdestaque:a chave públicaea AC (Autoridade
Certificadora).
Achavepúblicaéutilizadapeloreceptordeumamensagemparavalidar
aassinaturadoemissorecertificar-sedesuaidentidade.
UmaACéumaentidadedeconfian çaqueemitecertificadosdigitaisde
diversostipos,determinaprazosdevalidadeecuidadarenovaç ãodosmes-
mos.QuandoumaACemiteumcertificado,elaoassina,criandoumacadeia
deconfian ça.Quandoumusuáriotemdúvidasobreaconfiabilidadedocer-
tificado,eleiráolharparaacadeiadaquelecertificado(alémdesuavalidade),
afimdeaveriguarqueaquelecertificadofoiemitidoporumaACnoqualele
confia. UmaACpodeserassinadadigitalmenteporoutraAC,eassimpor
diante,atéquesechegueaumaACraiz,queporsuavezéautoassinada.No
Brasil,aACraizérepresentadapeloITI(InstitutoNacionaldeTecnologia
daInformação),órgãoqueditaasregrasdaInfraestruturadeChavesPúbli-
casBrasileira(ICPBrasil).Paraaobten çãodeumcertificadoválidopelaICP
Brasil,énecessárioquevocêentreemcontatocomumadasdiversasautori-
dadescertificadorascredenciadasexistentes.Alistapodeservisualizadano
seguinteendere ço:http://acraiz.icpbrasil.gov.br/.
V alidação de um certificado digital
Avalidaçãodeumcertificadoéimportanteparaassegurarmossuacon-
fiabilidade. Paraqueumcertificadosejaconsideradoválido,levam-seem
conta:
•data de expiração–cadacertificadoemitidopossuiumadatadevali-
dade.Geralmente,variamdeumatrêsanos.Casoessadatajátenha
sidoultrapassada,ocertificadoéconsideradoinválido;
•CRL ou OCSP –tantoaCRL(CertificateRevocationList )quantoa
OCSP(OnlineCertificateStatusProtocol )sãomeiosquedisponibilizam
achecagemdecertificadosqueforamrevogadospelasautoridadescer-
tificadoras. Umcertificadopodeserrevogadopordiversosmotivos,
54

## Página 59

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
taiscomoperdaouroubodachaveprivada(queestejamemdispo-
sitivos,comotokensousmartcards,porexemplo)ouousoimpró-
prio/ilegaldocertificado.ACRLédisponibilizadaemumarquivoque
éatualizadoperiodicamentepelaAC.JáaOCSP,ummodelonovo,pos-
sibilitaaconsultaon-linedostatusdocertificado;
•cadeia de certificados –visagarantirqueocertificadoemitidofaz
partedeumacadeiaqueéconsideradaconfiável. Poderíamos, por
exemplo,aceitarsomentecertificadoscujaraizdacadeiafosseoITI,
recusandotodososoutros.Amaioriadosbrowserseoutrasaplicações
jáincorporamumasériedeautoridadescertificadorasnasualistade
confiabilidade.Porisso,existeumesfor çocontínuoparaquearaízda
ICP-Brasilsejaincoporadaporpadrãonomaiornúmerodeaplicações
possíveis.
Afigura3.3mostraoexemplodeuma appletquefoivalidadapelobrowser
eapresentaamensagem“Thedigitalsignaturehasbeenvalidatedbyatrusted
source”.Quandovocêaceitaqueaappletsejaexecutada,vocêdápermissões
paraqueelapossaacessarváriosrecursosdoseusistema(inclusiveoenviode
dadosparaoservidor).Poressarazão,éimportantequeaappletsejavalidada
(oquemesmoassimnãoimpedequeelacontenhaalgumcódigomalicioso).
Valeapenalembrarqueumcertificadoquenãopasseemumdessescritérios
aindapodeserutilizadoouaceito,masporcontaeriscopróprio.Oleitorque
estiverinteressadonaassinaturadigitaldeappletsdevedarumaolhadano
comando jarsignerdoJava.Vejaasreferênciasparamaisinformações.
Outrousoextensodecertificadosdigitaiséfeitonoprotocolodesegu-
rançaSSL.Apróximase çãosobreSSLmostraumexemplodecriaç ãodeuma
conexãosegurautilizandocertificadosdigitais.Alémdessescritérios,éneces-
sárioverificarinformaçõesconstantesdentrodocertificadocomo,porexem-
plo,seocertificadofoicriadoparaaassinaturadedocumentosouapenaspara
aautenticação.Estasinformaçõesgeralmenteestãopresentesdentrodocer-
tificadoemcamposdenominados CertificatePolicieseCertificateExtensions
(segundoopadrãoX.509).
55

## Página 60

3.4. Certificadodigital CasadoCódigo
Fig.3.3:Appletcomcertificadoconfiável.
SSL
OSSLéumprotocolocriptográficoqueprovêcomunicaçõessegurasna
internet(e-mail,acessoapáginasweb,mensagensinstantâneas)equevisa
proverconfiabilidadeeprivacidadeatravésdeumcanaldeconexãoseguraen-
treosparticipantes.Utilizaalgoritmosdecriptografiasimétricaparaacodi-
ficaçãodosdadostransmitidos,ealgoritmosdecriptografiaassimétricapara
codificaçãodachavesimétricaeparafinsdeassinaturadigital.Deformasu-
cinta,asetapasenvolvidasemumaconexãoSSLsãoasseguintes(vejaafigura
3.4paraumexemploilustrativo):
• Oclienteenviaumamensagemparaoservidorinformandoumasé-
riedeinformaçõesreferentesaoprotocolosuportadoporele(versão,
algoritmosdecriptografiaefun çõesdehash).
• Oservidorescolheoalgoritmodecriptografiaeafun çãodehashmais
forteinformadospeloclienteeoinformaàquelesqueforamseleciona-
dos.
56

## Página 61

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
• Oservidorenviaseucertificadodigitalparaocliente.Estaéasuaiden-
tificação.Opcionalmente,oservidorpodesolicitarocertificadodocli-
enteparafinsdeautenticaç ão.
• Parageraraschavesdesessãoutilizadasnestaconexãosegura,ocliente
criptografaumnúmeroaleatóriocomachavepúblicadoservidore
enviaoresultadoparaoservidor.
Apartirdestenúmeroaleatório,ambososladosdacomunicaç ãorealizam
acriptografiaedescriptografiadainformaç ão.Feitoesseprocesso,conhecido
tambémcomohandshake,clienteeservidorestabelecemumaconexãosegura
emquedadosserãotransmitidosdeformacriptografada.
Fig.3.4:SSLHandshake.
57

## Página 62

3.5. SegurançanaplataformaJava CasadoCódigo
3.5 S egurança na plataforma Jav a
AplataformaJavafoiprojetadacomumaforteênfasenaseguran ça.Averi-
ficaçãoeocarregamentodeclassesgarantequeapenascódigoJavaqueseja
legítimopossaserexecutado.Atualmente,aarquiteturadeseguran çadapla-
taformaJavaincluigrandesconjuntosdeAPIs,ferramentas,implementações
dealgoritmos,protocolosemecanismosdeseguran ça.Dentreasváriasfren-
tesdeseguran çaoferecidas,iremosfocarnapartedaplataformaquetrabalha
comdispositivosdeseguran çaecertificadosdigitais.
JCA/ Providers
Aosetrabalharcomdispositivosdeseguran çadigitalutilizandoaplata-
formaJava,éimportanteconhecerosconceitos,assiglaseasAPIsenvolvidas.
AprimeiradelaséaJCA(JavaCryptographyArchitecture)eemseguidaserão
vistosalgunsconceitosrelacionadosaos providers.
JCA – Java Cryptography Architecture
AJCA,éumapartedaplataformaJavaquecontémumconjuntodeAPIs
utilizadasemprocessosdeassinaturadigital,hashesdemensagens,validações
decertificados,criptografia,geraçãoegerenciamentodechaves,dentreoutros
serviçoscriptográficos.AJCAfoiprojetadasegundoalgunsprincípios:
• interoperabilidadeeindependênciadeimplementação;
• extensibilidadeeindependênciadealgoritmos.
Aindependênciadeimplementaçãoedealgoritmossãoconceitoscom-
plementaresesignificamdizerqueodesenvolvedornãoprecisaconheceros
detalhesdeimplementaç ãodosalgoritmosqueformamabasedosserviços
criptográficos.Entretanto,acompletaindependênciadeimplementaçãonão
épossível.Pararesolverisso,aJCAprovêapossibilidadedeutilizaç ãodeAPIs
específicasnaschamadasaestesserviços.Emoutraspalavras,aJCApermite
queodesenvolvedorescolhaaAPIqueimplementaoserviçodesejadoeque
realizaráefetivamenteaexecuçãodoserviçocriptográficodesejado.
58

## Página 63

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
Aindependênciadealgoritmoséalcançadapormeiodadefiniç ãodeclas-
sescriptográficaschamadasdeclassesengines(tambémchamadasdeserviços
criptográficos). Algunsexemplossão: Signature, KeyPairGenerator
e Cipher. AsclassesenginessãoclassesdefinidaspelaJCA,masquesão
implementadasporum provider.
Ainteroperabilidadesignificadizerquequalquerartefatogeradoporum
providerpoderáserutilizadoemoutro.Aextensibilidadeéacapacidadede
seimplementaremnovosalgoritmosquesãosuportadospelasclasses engine.
Providers
Oproviderrefere-seaumpacoteouconjuntodepacotesqueimplemen-
tamserviçoscriptográficos,como,porexemplo,osalgoritmosdeassinaturas
digitais. Sãoosreaisfornecedores,provedoresdosserviçoscriptográficos.
Aclasse java.lang.Provideréaclasseprincipalparatodososprovi-
ders. Cadaprovider,tambémconhecidocomo CryptographicServiceProvi-
der(CSP)contémumainstânciadestaclassecomoseunomeeosserviços
disponibilizadosporele.
AinstalaçãodoJDKcontémumoumaisproviders-padrãoconfigurados
einstalados.Aordemdepreferênciaemqueosprovidersserãopesquisados
podeserdefinidanoambientedeexecuç ãodaplataformaJava.Autilizaç ão
destessedápormeiodechamadasàsclassesenginescomotipodealgoritmo
ouserviçoespecificado.Nestaarquitetura,seguindoaordemdepreferência
dosproviders,oprimeiroqueimplementaroserviçosolicitadoseráseleci-
onado.Entretanto,háapossibilidadededeterminarumproviderespecífico
paraforneceroserviçodesejado.Segueoexemplodeum MessageDigest,
classeengineresponsávelporextrairovalordohashdealgumainformaç ão
segundoumalgoritmo:
MessageDigest md = null;
md = MessageDigest.getInstance(“MD5”);
md = MessageDigest.getInstance(“MD5”,“ProviderC”);
Noprimeirocaso,oprimeiroproviderqueimplementaoalgoritmoMD5
naclasse MessageDigestseráutilizado. Nosegundo,utiliza-seaimple-
mentaçãodoprovider ProviderC.Afigura 3.5representaasduaschamadas
59

## Página 64

3.5. SegurançanaplataformaJava CasadoCódigo
demétodosmostradasantes.
Fig.3.5:Exemplodechamadadeumserviçoedisponibilizadospordiferentes
providers.
OJDKdaSuncontémprovidersqueimplementamalgunsserviçoscrip-
tográficos.Dentreeles,podemosdestacar:
• SUN: contém serviços de hash (MessageDigest) e assinatura (
Signature);
• XMLDSig:contémserviçosdeassinaturadigitalbaseadaemXML;
• SunMSCAPI:permitequeaplicaçõesusemaAPIpadrãodaJCApara
acessarbibliotecascriptográficasnativaserepositóriodechavesecer-
tificadosdaplataformaWindows;
60

## Página 65

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
• SunPKCS11:estabeleceacomunicaçãoentreoambienteJavaeospro-
vidersPKCS11nativos(nãocontémasfuncionalidadescriptográficas);
• SunRsaSign:contémaimplementaçãodotipodeassinaturaRSA.
Talvezaindatenhaficadoumpoucovagaaideiadofuncionamentodos
providersemumaaplicaç ãoreal.Oexemploaseguir(mostradonafigura 3.6)
tentaapresentardeformaclaracomotudofunciona.
Imagineumaaplicaç ãonaqualsejanecessárioverificaraintegridade
deumamensagemqualquer. Comofoivisto,fun çõesdehashsãoutiliza-
dasparafazerestaverificaç ão. Paraisso,écriadaumainstânciadaclasse
MessageDigestcomoalgoritmo“SHA-1”. Aoinvocarométodoestático
MessageDigest.getInstance(“SHA-1”)quecriaestainstância,aJCA
buscaemsualistadeprovidersaquelequecontémaimplementaç ãodoalgo-
ritmo“SHA-1”.
61

## Página 66

3.5. SegurançanaplataformaJava CasadoCódigo
Fig.3.6:Representaçãodosproviders.
62

## Página 67

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
Paracadaclasseengine,existeumaclasseabstrataSPI(ServiceProvider
Interface)correspondente.Aclassequeimplementaumserviçocriptográfico
emumprovideréumasubclassedaSPIdarespectivaclasseengine.Node-
senvolvimentodeprojetosdeseguran çautilizandoaplataformaJava,muitas
vezesénecessárioutilizarprovidersqueimplementamcertafuncionalidade
nãocontempladapelosproviderspadrão. Exemplosdestesproviderssãoo
BouncyCastleeoJSS,ambosgratuitosedecódigoaberto.
OBouncyCastlepossuitodaumaestruturaparaamanipulaç ãodecerti-
ficadosX.509,umabibliotecaparaaleituraeescritadeobjetoscodificadosem
ASN.1(presenteemalgunscamposdentrodeumcertificadodigital),classes
paraacriaç ãoeverificaç ãodepacotesdeassinaturasnoformatoCMS,além
deoutrasfuncionalidadesquenãosãoencontradasemproviderspresentes
noJDK.
OJSS(NetworkSecurityServicesforJava)éumainterfaceJavaparaoNSS
(NetworkSecurityServices –projetoMozillacompostoporumconjuntode
bibliotecasqueimplementamdiversospadrõesdeseguran ça).
3.6 P adrões de assinaturas
Oprocessodeassinaturadigitalpermitequetaisassinaturassejamempaco-
tadasemdiferentesformatos. Dentreestes,destacamosospadrõesCMSe
XMLDSig.
CMS
OCMS(CryptographicMessageSyntax )ébaseadonasintaxedoPKCS#7
eestáespecificadonaRFC3852. Podeserutilizadoemassinaturasdigitais,
hashes,autenticaçãooucriptografiadequalquerinformaç ãodigital. Pode-
mosdizerqueoCMSéumaatualizaç ãodoPKCS#7.OPKCS#7(PublicKey
CryptographyStandards #7)éumpadrãodefinidopelaRFC2315eéusado
naassinaturaecriptografiademensagenssobumainfraestruturadechaves
públicas.
Arquivos de assinaturas CMS (ou PKCS#7) possuem extensão.p7s.
Um exemplo de assinatura de uma informação qualquer em formato
CMSéapresentadonalistagemaseguir. Paraesteexemplo,foiutilizada
63

## Página 68

3.6. Padrõesdeassinaturas CasadoCódigo
a API do Bouncy Castle (ver referências). O método cria um reposi-
tório de certificados a partir da cadeia de certificados recebida como
um argumento da sua chamada. Este repositório é representado pela
classe java.security.cert.CertStore. Em seguida, uma ins-
tância de org.bouncycastle.cms.CMSSignedDataGenerator é
criada, representando um gerador de assinaturas CMS. Após a criação
de um objeto desta classe, informações do assinante, da cadeia de cer-
tificados e da lista de certificados revogados são adicionadas a ele. A
informaçãoqueseráassinadaéencapsuladaporumainstânciadaclasse
org.bouncycastle.cms.CMSProcessableByteArray. Em seguida,
é gerada uma assinatura CMS e armazenada em uma entidade do tipo
org.bouncycastle.cms.CMSSignedData. Este método recupera o
arraydebytesreferentesàassinaturageradaeoretornanofimdaexecuç ão
do método. O sistema operacional Windows, por exemplo, possui um
programaqueidentificaarquivos .p7seapresentaacadeiadecertificados
queparticipoudoprocessodeassinatura(figura 3.7).
Listagem3.1-AssinandonopadrãoCMS.:
/**
* Método responsável por assinar um array de bytes
*
* @param arquivo bytes que formam a informação/arquivo
* que será assinado
* @param cadeiaDeCertificados cadeia de certificados do
* responsável pela assinatura
* @param chavePrivada chave privada do responsável pela
* assinatura
* @param nomeDoProvider nome do provider que implementa
* esta operação de assinatura
*/
public byte[] assinaturaAttached(byte[] arquivo,
X509Certificate[] cadeiaDeCertificados,
PrivateKey chavePrivada,
String nomeDoProvider) {
byte[] informacaoAssinada = null;
64

## Página 69

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
// repositório de certificados
CertStore certsStore = null;
// classe geradora de uma assinatura PKCS#7
CMSSignedDataGenerator signedDataGenerator = null;
// interface contendo método que copia os dados
CMSProcessable content = null;
// classe geral para gerenciar um pacote de assinatura PKCS#7
CMSSignedData cmsSignedData = null;
List<X509Certificate> certList = null;
try {
certList = Arrays.asList(cadeiaDeCertificados);
// é criado um repositório de certificados com a cadeia
// de certificados do assinante
certsStore = CertStore.getInstance("Collection",
new CollectionCertStoreParameters(certList), "SUN");
// cria uma classe geradora do pacote de assinatura CMS
signedDataGenerator = new CMSSignedDataGenerator();
// classe geradora adiciona um assinante, passando chave
// privada, seu certificado (posição 0 da cadeia de
// certificados) e o algoritmo de hash utilizado na
// assinatura (SHA-1)
signedDataGenerator.addSigner(chavePrivada,
cadeiaDeCertificados [0],
CMSSignedDataGenerator.DIGEST_SHA1);
// classe geradora adiciona o repositório de certificados
// e listas de certificados revogados
signedDataGenerator.addCertificatesAndCRLs(certsStore);
// criação da classe que contém os dados (arquivo)
content = new CMSProcessableByteArray(info);
// o gerador de assinaturas CMS gera um objeto assinado
// O valor true significa que uma cópia da
// informação assinada
// será incluída na assinatura
65

## Página 70

3.6. Padrõesdeassinaturas CasadoCódigo
cmsSignedData = signedDataGenerator
.generate(content, true, nomeDoProvider);
informacaoAssinada = cmsSignedData.getEncoded();
} catch (Exception e) {
e.printStackTrace();
}
return informacaoAssinada;
}
Fig.3.7:CadeiadecertificadosdoarquivoassinadonoformatoCMS.
XMLDSig
AassinaturadigitalbaseadaemXML,alémdeserumarecomendaç ãoda
W3C,éumpadrãolargamenteutilizadoemprocessosdeassinaturadigital.
Opadrãopodeserusadoparaassinarqualquerformatodearquivo,nãose
limitandoaassinaturadearquivosXML.
AssinaturasdigitaisXMLhabilitamumapessoaqueestáenviandomen-
sagensaassinarinformaçõescriptograficamente,easassinaturaspodemser
utilizadascomocredenciaisdeautenticaç ãooucomoformadechecarainte-
gridadedosdadosenviados.ComoadventodopadrãoXMLpararepresen-
taçãodedadosedainteroperabilidadeentreaplicaçõesatravésdousodeWeb
services,opadrãoXMLDSigécadavezmaisutilizadonacertificaç ãodigital.
A partir da versão 6, o Java incorporou o suporte ao XMLD-
Sig em sua API(JSR 105) nos pacotes javax.xml.crypto e
javax.xml.crypto.dsig. Apesar disso, o suporte é limitado. Para
oleitorquequeiraseaprofundarmais,recomendamosdarumaolhadana
bibliotecaApacheXMLSecurity(http://santuario.apache.org/).
66

## Página 71

CasadoCódigo Capítulo3. CertificaçãodigitalcomJavaCryptographicArchitecture
3.7 C onsiderações finais
Acertificaçãodigitalvemagregandoconfiabilidadeemtransaçõesrealizadas
nomeiodigital.Atravésdainfraestruturadechavespúblicas,cria-seumam-
bientecapazdeagregarautenticidade,integridade,privacidadeenão-repúdio
aomeiodigital.Suaconfian çaestádiretamenteatreladaaopoderdaschaves
criptográficasutilizadas,queemboapartesãoimpossíveisdeseremquebra-
dascomopoderiocomputacionalexistente.Omodotradicionaldeautenti-
cação(baseadonoenviodeloginesenha)ésubstituídopeloenviodocerti-
ficadoedaassinaturadigital,demodoqueinterceptá-losnãorepresentariaa
princípio,umrisco.
Obviamente,nemtudoéperfeito. Acertificaç ãodigitalaindaencontra
algumasbarreiras,comoafaltadeinformaç ãodosusuáriosarespeitodos
benefíciosdatecnologiaeocustorazoávelparaaaquisiç ãodecertificados
deentidadesconfiáveis.Comoqualquermudan çadeparadigma,suaado ção
serágradual,einiciativascomoadeclaraç ãodoimpostoderendapormeio
decertificadosdigitaistendemadisseminá-la.
3.8 R eferências
• XMLDSIG http://java.sun.com/javase/6/docs/technotes/guides/
security/xmldsig/XMLDigitalSignature.html
• E-CommerceBrasilhttp://www.e-commerce.org.br/STATS.htm
• Java Cryptography Architecture (JCA) Reference Guide
http://java.sun.com/javase/6/docs/technotes/guides/security/crypto/
CryptoSpec.html
• BouncyCastlehttp://www.bouncycastle.org/
• JSS (Network Security Services for Java)http://www.mozilla.org/
projects/security/pki/jss/
• ApacheXMLSecurity (http://santuario.apache.org/)
• JarSigner http://java.sun.com/j2se/1.4.2/docs/guide/plugin/
developer_guide/rsa_signing.html
67