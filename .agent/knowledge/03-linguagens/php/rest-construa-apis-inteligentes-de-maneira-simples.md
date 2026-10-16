---json
{
  "id": "rest-construa-apis-inteligentes-de-maneira-simples",
  "title": "Rest_-_Construa_APIs_inteligentes_de_maneira_simples",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `Rest_-_Construa_APIs_inteligentes_de_maneira_simples.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "apis",
    "construa",
    "inteligentes",
    "linguagens",
    "maneira",
    "php",
    "rest",
    "rest_-_construa_apis_inteligentes_de_maneira_simples"
  ],
  "perguntas_tipo": [
    "Como utilizar Rest_-_Construa_APIs_inteligentes_de_maneira_simples?",
    "Quais as boas praticas de php?"
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
  "dono": "stack-php",
  "prioridade": 2
}
---

# Rest_-_Construa_APIs_inteligentes_de_maneira_simples

> **Arquivo Original:** `Rest_-_Construa_APIs_inteligentes_de_maneira_simples.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

CasadoCódigo Sumário
Sumário
1 P o rq u eutilizar REST? 1
1.1 HTMLtradicional versusREST . . . . . . . . . . . . . . . . . . . . . .1
1.2 W e bservices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2
1.3 REST . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3
1.4 Desenvolvendoum protótipodewebserviceREST . . . . . . . . . . .6
1.5 A v a nçandooprotótipodewebserviceREST . . . . . . . . . . . . . .9
1.6 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2 O protocolo HTTP 13
2.1 OsfundamentosdoHTTP . . . . . . . . . . . . . . . . . . . . . . . . .13
2.2 MétodosHTTP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .15
2.3 Tiposdepassagemdeparâmetros . . . . . . . . . . . . . . . . . . . . .17
2.4 Cabeçalhos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .19
2.5 MediaTypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .21
2.6 Códigosde status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.7 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3 Conceitos de REST 29
3.1 Semânticasderecursos . . . . . . . . . . . . . . . . . . . . . . . . . . .29
3.2 Interaçãopormétodos . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.3 Representações distintas . . . . . . . . . . . . . . . . . . . . . . . . . .32
3.4 U s ocorretode statuscodes. . . . . . . . . . . . . . . . . . . . . . . . .34
3.5 HATEOAS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .35
3.6 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .38
i

## Página 3

Sumário CasadoCódigo
4 T i p o sde dados 39
4.1 XML . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .39
4.2 FerramentalXML:conhecendoosXML Schemas. . . . . . . . . . . .40
4.3 TrabalhandocomXMLutilizandoJAXB . . . . . . . . . . . . . . . . .49
4.4 TestandooXMLgerado . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
4.5 UtilizandoJAXB semumXML Schema . . . . . . . . . . . . . . . . . 55
4.6 JSON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .57
4.7 TrabalhandocomJSONutilizandoJAXB . . . . . . . . . . . . . . . . . 58
4.8 ValidaçãodeJSONcomJSON Schema . . . . . . . . . . . . . . . . . .62
4.9 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
5 Implementando se rviços REST em J a v acom S e r v l e t s 69
5.1 U m aimplementaçãocomServlets . . . . . . . . . . . . . . . . . . . . . 69
5.2 Implementandonegociaçãodeconteúdo . . . . . . . . . . . . . . . . . 81
5.3 Implementandoa buscaporumacervejaespecífica . . . . . . . . . . .83
5.4 Implementandoacriaç ãodeum recurso. . . . . . . . . . . . . . . . . 89
5.5 Implementandonegociaçãodeconteúdo nacriaçãodo recurso. . . . 95
5.6 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
Bibliografia 101
ii

## Página 4

Capítulo1
P o rqueutilizarREST?
“ N ã oémerecedor do f av ode mel aquele q u eevita a colméiaporque as a b e l h a st ê m
f e r rõ e s”
–WilliamShakespeare
V o c êéumempreendedor.Seguindoafilosofiadeuma startup,vocêquerpro-
duzirum siteparaseuproduto,umalojadecervejas finaspelainternet.Assim, você
querfazerumsistema quesejarápidodeproduzire,aomesmotempo,sejaeficiente
efácildereutilizaremváriosambientesdiferentes(vocêestáconsiderandoumaver-
são mobileparaosistema).Assim, vocêexploradiversaspossibilidades.
1.1 HTML tradicional versus REST
V o c êdecideavaliar,antesdetudo,sistemastradicionaisweb,baseadosem formulá-
riosHTML.
Ficaclaroparavocêquefazerumsistematradicional,baseadoem formulários
HTML,estáforadequestão. Issoporqueessetipodeformulárioéclaramenteoti-

## Página 5

1.2.W e bservices CasadoCódigo
mizadoparatrabalharcomsistemasbaseadosnaweb,masvocênãotemcertezaem
relaçãoao quantoeleseráflexívelparatrabalharcomoutrostiposde front-end.Por
exemplo,considereuma telaparacadastrodosclientesdo site:
<html>
<body>
<form action="/cadastrar" method="post">
<input type="text" name="nome" />
<input type="text" name="dataNascimento" />
<input type="submit" value="Cadastrar" />
</form>
</body>
</html>
Estecódigo(comumpouco maisdetratamento)deve teatenderbem. Noen-
tanto,apóssubmeteroformulário,oservidordeve tetrazeruma páginaHTML-
oque,obviamente,não édesejávelnumcenáriocomváriosfront-ends,comoum
aplicativoparaAndroidouiOS.
Suapróximapossibilidade é,portanto,avaliaroutrostiposdesistemas.
1.2 Web services
Opróximocenárioquevemàsuamenteéodeusode web servicestradicionais,ou
seja,baseadosemSOAP (Simple Object Access Protocol).A princípio,tepareceuma
boaidéia,jáqueéomecanismodetráfegodeinformações éviaXMLe,portanto,é
possívelinteragircom serviçosdesse tipoapartirdecódigo javascript(ouseja,pos-
sibilitandoainteraçãotantoapartirdeum browserquantoapartirdecódigopuro).
Porém,estudandomaisvocêpercebequeinteragircomeste tipode web servicenãoé
tãosimplesquantovocêgostaria.Porexemplo,paralistarosclientesdo seusistema,
énecessárioenviaroseguinteXML paraoservidor:
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<listarClientes xmlns="http://brejaonline.com.br/administracao/1.0/service"
</soap:Body>
</soap:Envelope>
Aoquevocêreceberácomoresposta:
<soap:Envelope xmlns:domain="http://brejaonline.com.br/administracao/1.0/domain"
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
2

## Página 6

CasadoCódigo Capítulo1.PorqueutilizarREST?
<soap:Body>
<listarClientesResp onse xmlns="http://brejaonline.com.br/administracao/1.0/
<domain:clientes>
<domain:cliente domain:id="1">
<domain:nome>Alexandre</domain:nome>
<domain:dataNascimento>2012-12-01</domain:dataNascimento>
</domain:cliente>
<domain:cliente domain:id="2">
<domain:nome>Paulo</domain:nome>
<domain:dataNascimento>2012-11-01</domain:dataNascimento>
</domain:cliente>
</domain:clientes>
</listarClientesResponse>
</soap:Body>
</soap:Envelope>
Estecódigo,então, teparececomplicadodemais paraumasimplesrequisiç ão
delistagemdeclientes.Acomplexidade(everbosidade)doprotocoloficaespecial-
menteevidentequandovocêpensanocasoda comunicaçãofeitacomplataformas
móveis,ondeacomunicaçãopelarededeveseramaissucintapossível.
1.3 REST
V o c êestudamaisarespeitode web servicesquandovocêlêsobreservi çosREST.Ao
estudarsobreoassunto,tepareceumatécnicasimples. Porexemplo,pararealizar
alistagemdeclientesdo seusistema,vocêpodeutilizaronavegador(sejaesteo
Chrome, Firefox, Internet Explorer ouqualqueroutro)paraabriraURL
http://localhost:8080/cervejaria/clientes.Aofazerisso,vocêpodeobteroseguinte re-
sultado:
<clientes>
<cliente id="1">
<nome>Alexandre</nome>
<dataNascimento>2012-12-01</dataNascimento>
</cliente>
<cliente id="2">
<nome>Paulo</nome>
<dataNascimento>2012-11-01</dataNascimento>
</cliente>
</clientes>
3

## Página 7

1.3. REST CasadoCódigo
Mas,afinal,comofazerseucódigointeragircomestalistagem?O queaconteceu?
O sprincípios básicosde REST
REST significa REpresentational State Transfer (ou Transferência de
Estado Representativo,emtraduç ãolivre),eéumestilodedesenvolvimento
de web servicesqueteveorigemnatesededoutoradode RoyFielding. Este,por
suavez,éco-autordeumdosprotocolos maisutilizadosnomundo,oHTTP(
HyperText Transfer Protocol ).Assim,énotávelqueoprotocoloRESTégui-
ado(dentre outrospreceitos)peloqueseriamasboaspráticasdeusodeHTTP:
•U s oadequadodosmétodosHTTP;
•U s oadequadodeURL’s;
•U s odecódigosde statuspadronizadospararepresentaçãodesucessos oufa-
lhas;
•U s oadequadode cabeçalhosHTTP;
• Interligaçõesentreváriosrecursosdiferentes.
Opropósitodestelivro é,portanto,exemplificaroquesãoestaspráticaseguiar
você,leitor,atravésdasmesmasefornecerosinsumosdecomoconstruir seuspró-
priosserviços,demaneira queestessejamsempretãoescaláveis,reutilizáveisema-
nuteníveisquantopossível.
A sfundaçõ e sde REST
O“marcozero”deRESTéorecurso.EmREST,tudoédefinidoemtermosde
recursos,sendoestesosconjuntosdedados quesãotrafegadospeloprotocolo.Os
recursossãorepresentadosporURI’s.Noteque,na web,URI’seURL’ssãoessencial-
menteamesmacoisa-razão pelaqualvouusarosdoistermos nestelivrode forma
intercalada.
4

## Página 8

CasadoCódigo Capítulo1.PorqueutilizarREST?
Qu a la diferença entre u m a URL e u m a URI?
URL significa Universal Resource Locator e URI,
Universal Resource Identifier . U m aURI, como diz o
próprionome,podeserutilizadaparaidentificarqualquercoisa- dar
umcaminho paraumdeterminadoconteúdo, darnomeaeste,etc. Já
umaURL podeserutilizadaapenasparafornecercaminhos-sendo
queumaURL é,portanto,umaformadeumaURI.É maisnaturalque
URI’squenãosejamURL’ssejamutilizadasem outroscontextos,como
fornecimentode namespacesXML.
T o m a n d ocomoexemploo casoda listagemdeclientes,épossíveldecompôra
URLutilizada paralocalizaçãodalistagememváriaspartes:
http://localhost:8080/cervejaria/clientes
•http://-Indicaoprotocolo queestásendoutilizado(no caso,HTTP);
•localhost:8080-Indicaoservidorde redequeestásendoutilizadoea porta
(quandoa portanão éespecificada,assume-se queéapadrão- nocasodo
protocoloHTTP,80);
•cervejaria-Indicao contextodaaplicação,ouseja,araiz pelaqualaaplicação
estásendofornecida paraocliente. V o umereferiraesta,daquiem diante,
como contexto da a p l i c açãoouapenas contexto;
•clientes-Éoendere ço,defato,do recurso-nocaso,alistagemdeclientes.
V o umereferira este,daquiem diante,como endereço do recurso.
O protocolo
Oprotocolo,emrealidade, nãoéumarestriçãoemREST-em teoria.Naprá-
tica,oHTTPéoúnicoprotocolo100% compatívelconhecido.V a l edestacarqueo
HTTPS( HyperText Transfer Protocol over Secure Sockets Layer )
não éumavariaçãodoHTTP, masapenas aadiçãodeuma camadaextra-o que
mantémoHTTPS namesmacategoriaqueoHTTP,assimcomoqualquer outro
protocoloquesejautilizadosobreoHTTP,como SPDY.
Aspossíveiscausasparaesta“preferência”podemserapontadas: oautordo
HTTPtambéméoautordeREST e,alémdisso,oprotocoloHTTPéumdos mais
5

## Página 9

1.4. DesenvolvendoumprotótipodewebserviceREST CasadoCódigo
utilizadosnomundo(sendo quea web,demaneirageral,éfornecida porestepro-
tocolo).Estesfatospromoveriamumaaceitaçãograndeerápida absorçãodeREST
pelacomunidadededesenvolvedores.
A URL
AURLescolhidadeve serúnicaporrecurso. Istosignificaque,sempreque
desejarobterarepresentaçãodetodososclientes, vocêdeveutilizaraURL http:
//localhost:8080/cervejaria/clientes. RealizarumaconsultanestaURLpoderetornar
dadosdaseguintemaneira:
<clientes>
<cliente id="1">
<nome>Alexandre</nome>
<dataNascimento>2012-12-01</dataNascimento>
</cliente>
<cliente id="2">
<nome>Paulo</nome>
<dataNascimento>2012-11-01</dataNascimento>
</cliente>
</clientes>
Sevocêdesejar,portanto,retornarumclienteespecífico, vocêdeveutilizaruma
URLdiferente. Suponha,porexemplo,quevocêdesejaretornaroclientecom id
iguala1. Nestecaso,aURLseria http://localhost:8080/cervejaria/clientes/1.Issoretor-
nariaalgocomo:
<cliente id="1">
<nome>Alexandre</nome>
<dataNascimento>2012-12-01</dataNascimento>
</cliente>
1.4 Desenvolvendo u m protótipo de web service
REST
Paradesenvolverum protótipode web serviceRESTbemsimples,nãoénecessário
utilizar-sedealtatecnologia.Bastaqueodesenvolvedortenhaemmenteoresultado
quedesejaalcançarecriarum arquivocontendoarespostadesejada. Porexemplo,
suponhaumarquivo clientes.xml,comoconteúdo:
6

## Página 10

CasadoCódigo Capítulo1.PorqueutilizarREST?
<clientes>
<cliente id="1">
<nome>Alexandre</nome>
<dataNascimento>2012-12-01</dataNascimento>
</cliente>
<cliente id="2">
<nome>Paulo</nome>
<dataNascimento>2012-11-01</dataNascimento>
</cliente>
</clientes>
Para acessá-lopelo browser, basta utilizar a URL file://<caminho
do arquivo>. Porexemplo,nomeu caso(ambienteLinux),o arquivoestáem
/home/alexandre/workspace/rest/cap-01/src/main/resources/clientes.xml.
Assim, a URL completa ficafile:///home/alexandre/workspace/rest/cap-01/src/main/
resources/clientes.xml-notequesão trêsbarrasnocomeço(duas paradelimitação
doprotocoloe outraparaindicararaizdosistemaLinux).
URL para arquivos no Windows
NoWindows,pararenderizarumaURL tambéménecessáriouti-
lizartrêsbarrasnocomeço. Porexemplo,paralocalizarum arquivo
em Documentos,ocaminhoa serinseridono browserficariasimilar
a file:///C:/Users/Alexandre/Documents/clientes.xml. Istoédevidoauma
particularidadedo própriosistemadearquivosdoWindows, quepode
terváriasraízes(C:,D:,eassim pordiante).
Destaforma,oconteúdoérenderizadopelo browser:
7

## Página 11

1.4. DesenvolvendoumprotótipodewebserviceREST CasadoCódigo
Figura1.1:XMLrenderizado pelobrowser
Paradesenvolverumcliente paraestearquivo,bastautilizaraAPIdeI/Odo
próprioJava,come çandopelaclasse java.net.URL,queindicaqualocaminhoa
serseguido:
String caminho = "file:///home/alexandre/workspace/rest/" +
"cap-01/src/main/resources/clientes.xml";
URL url = new URL(caminho);
Feitoisso,opróximopassoéconectar-seaestecaminhoe abriruma i n p u ts t re am,
ouseja,umcanaldeleituradedadosdocaminhoindicado pelaURL.Paraconectar-
se,bastautilizarométodo openConnectiondaURL,e paraabrira i n p u ts t re am,
bastautilizarométodo getInputStream:
java.io.InputStream inputStream = url.openConnection().getInputStream();
Opróximopassoéencapsularestaleituraemum java.io.BufferedReader.
Estaclassepossuiummétodoutilitárioparalerinformações linhaalinha,facilitando
oprocessodeleituradedados. Parautilizá-lo,noentanto,énecessárioencapsulara
InputStreamemum java.io.InputStreamReader:
BufferedReader bufferedReader = new BufferedReader(
new InputStreamReader(inputStream));
8

## Página 12

CasadoCódigo Capítulo1.PorqueutilizarREST?
U m avezfeitoesseprocedimento, bastautilizarométodo readLineemum
laço,atéqueestemétodoretorne null:
String line = null;
while ((line = bufferedReader.readLine()) != null) {
System.out.println(line);
}
Ocódigocompletoficaassim:
package br.com.cervejaria.cliente;
import java.io.*;
import java.net.URL;
public class Cliente {
public static void main(String[] args) throws IOException {
String caminho = "file:///home/alexandre/workspace/rest/"
+ "cap-01/src/main/resources/clientes.xml";
URL url = new URL(caminho);
InputStream inputStream = url.openConnection().getInputStream();
BufferedReader bufferedReader = new BufferedReader(
new InputStreamReader(inputStream));
String line = null;
while ((line = bufferedReader.readLine()) != null) {
System.out.println(line);
}
}
}
1.5 Av ançando o protótipo de web service REST
Paradesenvolverumprotótipoquesejaverdadeiramentebaseadonaweb,bastaum
simples servlet.Nocódigo-fontedestelivro,estouutilizandoaespecificaç ão3.0de
servlets,quemepermiteanotá-losparaquesejamdetectadospelocontêiner.
Pararealizaralistagemdeclientes, bastafazercom queo servletleiao arquivo
clientes.xml,utilizando anteriormente,Assim,o servletserácapazdefornecer
9

## Página 13

1.5.A v a nçandooprotótipodewebserviceREST CasadoCódigo
estasinformações paraocliente.Estefornecimentodedadosvai serfeitoviamétodo
GET(maisàfrente,nocapítuloX,vocêvaientenderomotivo).Ocódigodo servlet
vaificarassim:
package br.com.cervejaria.servlet;
import java.io.*;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
@WebServlet(urlPatterns = "/clientes", loadOnStartup = 1)
public class ClientesServlet extends HttpServlet {
private String clientes;
@Override
protected void doGet(HttpServletRequest req, HttpServletResponse resp)
throws ServletException, IOException {
resp.getWriter().print(clientes);
}
@Override
public void init() throws ServletException {
// Faz aqui a leitura do arquivo clientes.xml
// E coloca na String clientes
}
}
O código-fonte d olivro
No código-fonte do livro (disponível emhttps://github.com/
alesaudate/rest/), vocêencontraum projetoMavencomestecódigo
prontoparaserinicializado.Bastaexecutar mvn jetty:run eacessar
estaURL.
AoacessaraURL http://localhost:8080/cervejaria/clientes, vocêobtémcomo
10

## Página 14

CasadoCódigo Capítulo1.PorqueutilizarREST?
respostaexatamenteoconteúdodo arquivo.Epararealizaristocomcódigo, basta
alterarocódigo fontedoclientecriadoanteriormente paraestamesmaURL:
URL url = new URL("http://localhost:8080/cervejaria/clientes");
1.6 Sumário
Nestecapítulo,vocêpodeconferiralgunsdos principaismotivospelosquaisomo-
deloRESTéselecionado parasetrabalharemaplicações modernas.V o c êconferiu
algunsdosprincípios maisbásicosdeREST,comoo usodeURL’secomorealizaro
acessoaestesdocumentosatravésde browsersecódigoJava.
Resta,ainda,conferirosprincípiosdoprotocoloHTTP(nos quaisRESTéfor-
tementebaseado)eentendercomocriar serviçosmaiscomplexosutilizandoeste
paradigma.
11

## Página 16

Capítulo2
OprotocoloHTTP
“ S ev imais longe, foi por estar de pésobre ombros de gigantes”
–IsaacNewton
Comomencionadoanteriormente,omodeloRESTfoidesenvolvidoporRoyFi-
elding,umdoscriadoresdoprotocoloHTTP. Portanto,ficanaturalmenteevidente,
paraquemconhece ambososmodelos, assemelhançasentreambos-sendo que,
narealidade,RESTéidealmenteconcebido parausocomoprotocoloHTTP. Por-
tanto,paraserumbomusuáriodeREST,énecessárioterumbomconhecimentodo
protocoloHTTP.
2.1 Os fundamentos d oHTTP
OprotocoloHTTP (HyperT ext TransferProtocol-ProtocolodeTransferênciadeHi-
pertexto)datade1996, épocaemqueostrabalhosconjuntosde TimBerners-Lee,
RoyFieldingeHenrik FrystykNielsenlevaramàpublicaç ãodeumaRFC (Request
for Comments)descrevendoesteprotocolo.Trata-sedeumprotocolode camadade

## Página 17

2.1.OsfundamentosdoHTTP CasadoCódigo
aplicação(segundoo modeloOSI)e,portanto,derelativafacilidadedemanipulação
emaplicações.
Esteprotocolofoidesenvolvidodemaneiraa seromaisflexívelpossível para
comportardiversasnecessidadesdiferentes.Emlinhasgerais,esteprotocolosegue
oseguinte formatoderequisições:
<método> <URL> HTTP/<versão>
<Cabeçalhos - Sempre vários, um em cada linha>
<corpo da requisição>
Porexemplo,pararealizararequisiç ãodo capítulopassado,algosemelhanteao
seguintefoienviadoparaoservidor:
GET /cervejaria/clientes HTTP/1.1
Host: localhost:8080
Accept: text/html
Portanto,oquefoipassadonestarequisiçãofoi:
GET /cervejaria/clientes HTTP/1.1
Com isso, o método GET foi utilizado para solicitar o conteúdoda URL
/cervejaria/clientes.Alémdisso,oprotocoloHTTPversão1.1 foiutilizado.
Notequeo host,ouseja,oservidor responsávelporfornecerestesdados,é pas-
sadoemum c a b eçalhoàparte.Nocaso,o hostescolhidofoi localhost,naporta
8080.
Alémdisso,umoutrocabeçalho, Accept,foifornecido.
Aresposta paraasrequisições seguemoseguinte formatogeral:
HTTP/<versão> <código de status> <descrição do código>
<cabeçalhos>
<resposta>
Porexemplo,aresposta paraestarequisiçãofoisemelhanteàseguinte:
HTTP/1.1 200 OK
Content-Type: text/xml
Content-Length: 245
14

## Página 18

CasadoCódigo Capítulo2. OprotocoloHTTP
<clientes>
<cliente id="1">
<nome>Alexandre</nome>
<dataNascimento>2012-12-01</dataNascimento>
</cliente>
<cliente id="2">
<nome>Paulo</nome>
<dataNascimento>2012-11-01</dataNascimento>
</cliente>
</clientes>
Aqui,notequeocódigo200indicou quearequisi çãofoibem-sucedida,eo ca-
beçalho Content-Lengthtrouxeotamanhodaresposta- nocaso,oXML que
contémalistagemdeclientes.Alémdisso,o cabeçalho Content-Typeindicaque
aresposta é,defato,XML-atravésdeum tipoconhecidocomo Media Type.
2.2 Métodos HTTP
AversãocorrentedoHTTP,1.1,defineoficialmente oitométodos-emborao proto-
colosejaextensívelemrelaçãoaestesmétodos. Hoje,estesoitosão:
• GET
• POST
• PUT
• DELETE
• OPTIONS
• HEAD
• TRACE
• CONNECT
Cadamétodopossuiparticularidadeseaplicações deacordocomanecessidade.
Estasparticularidadessãodefinidasemtermosde idempotência, segurançae me-
canismo de passagem de parâmetros.Alémdisso,porcadaumpossuirparticulari-
dadesde uso,considerareinestelivroapenasosseisprimeiros-osmétodos
TRACE
e CONNECTserãoconsiderados foradoescopodestelivro.
15

## Página 19

2.2. MétodosHTTP CasadoCódigo
Idempotência
Aidempotênciadeummétodoérelativaàsmodificações quesãorealizadasem
informações doladodoservidor.Trata-sedoefeito queumamesmarequisiçãotem
doladodoservidor- seamesmarequisição,realizada múltiplasvezes,provocaalte-
rações noladodoservidorcomo sefosseumaúnica,entãoestaéconsideradaidem-
potente.
Porexemplo, considereasquatrooperações debancosdedados: SELECT,
INSERT, UPDATEe DELETE.Realizandoumparalelodestascomoconceitode
idempotência,observeoseguinte:
SELECT * from CLIENTES;
Notequeestarequisição,paraumbancodedados,teráo mesmoefeitotodas
asvezesem queforexecutada(obviamente,assumindo queninguémestáfazendo
alterações nasinformações quejáestavamgravadas).
Agora,observeoseguinte:
INSERT INTO CLIENTES VALUES (1,'Alexandre');
Estarequisição,porsuavez,provocarádiferentesefeitossobreosdadosdo banco
dedadostodasasvezesqueforexecutada,dadoqueestáaumentandootamanhoda
tabela.Portanto,elanãoéconsideradaidempotente.
Notequeesteconceitonãoestárelacionadoàrealizaçãoounãodemodificações.
Porexemplo,considereasoperações UPDATEe DELETE:
UPDATE CLIENTES SET NOME = 'Paulo' WHERE ID = 1;
DELETE FROM CLIENTES WHERE ID = 1;
Noteque,emambososcasos, asalterações realizadassão idênticasàtodasas
subsequentes.Porexemplo,suponhaosdados:
ID NOME
---------
1 Alexandre
Searequisiçãodeatualizaç ãoforenviada,estesdadosficarãoassim:
ID NOME
---------
1 Paulo
16

## Página 20

CasadoCódigo Capítulo2. OprotocoloHTTP
Eentão, casoamesmarequisiç ãosejaenviadarepetidasvezes, aindaassimpro-
vocaráomesmoefeitoquedaprimeiravez,sendoconsiderada, portanto,idempo-
tente.
Segurança
Quantoà segurança,osmétodos são assimconsiderados senão provocarem
quaisqueralterações nosdadoscontidos. Aindaconsiderandooexemplo dasope-
rações debancosdedados, porexemplo,ométodo SELECTpodeserconsiderado
seguro- INSERT, UPDATEe DELETE,não.
Emrelaçãoaestas duascaracterísticas, aseguintedistribuiçãodosmétodos
HTTPéfeita:
Figura2.1:MétodosHTTP,deacordocomidempotênciaeseguran ça
2.3 Tiposde passagem de parâmetros
OsmétodosHTTPsuportamparâmetrossobduasformas:oschamados q u e r ypa-
rameterse body parameters.
Os q u e r yparameterssãopassadosnaprópriaURLdarequisição. Porexemplo,
considereaseguinterequisiç ãoparaoserviçode buscadoGoogle:
http://www.google.com.br/?q=HTTP
Estarequisiçãofazcom queoservidordoGoogle automaticamenteentendaa
string HTTPcomoum parâmetro.InserirestaURL no browserautomaticamente
indicaparaoservidor queumabuscaporHTTPestásendorealizada.
Os q u e r yparameterssãoinseridosa partirdosinaldeinterrogaç ão. Estesinal
indicaparaoprotocoloHTTP que,dealíemdiante,serãoutilizados q u e r yparame-
t e r s.Essessãoinseridoscom formato<chave>=<valor>(assimcomo noexemplo,
17

## Página 21

2.3.Tiposdepassagemdeparâmetros CasadoCódigo
emque qéachavee HTTP,ovalor). Casomaisdeumparâmetrosejanecessário,os
paressãoseparadoscomum &.Porexemplo,arequisiçãoparaoserviçodoGoogle
poderia,também,serenviadadaseguintemaneira:
http://www.google.com.br/?q=HTTP&oq=HTTP
Os q u e r yparameterssãoenviadosnaprópriaURL.Istoquerdizerquearequisi-
çãoparaoGoogleésemelhanteàseguinte:
GET /?q=HTTP&oq=HTTP HTTP/1.1
Host: www.google.com.br
NotequeocaracterdeespaçoéoseparadorentreométodoHTTP,aURLea
versãodoHTTPa serutilizada.Destaforma,sefornecessárioutilizarespaçosnos
q u e r yparameters,énecessárioutilizarumatécnicachamadade codificação da URL.
EstatécnicaadaptaasURL’sparaqueelassejamcompatíveiscomo mecanismode
enviodedados,ecodificam nãoapenasespaçoscomo outroscaracteresespeciaise
caracteresacentuados.
Estacodificaçãosegueaseguinteregra:
•Espaçospodemsercodificadosutilizando +ouastring %20
• Letrasmaiúsculaseminúsculas,númeroseoscaracteres ., -, ~e _sãodeixados
comoestão
• Caracteresrestantessãocodificadosdeacordocom suarepresentaçãoASCII
/UTF-8ecodificadoscomohexadecimal
Assim,a string às vezesécodificadacomo %C3%A0s+vezes(sendoqueos b y t e s
C3eA0representamosnúmeros 195e160que,emcodificaçãoUTF-8,tornam-sea
letra à).
Notequeumalimitaçãodos q u e r yparameterséaimpossibilidadede passarda-
dosestruturadoscomo parâmetro.Porexemplo,nãoháacapacidadederelacionar
um q u e r yparamcomoutro,levandoodesenvolvedoracriarmaneirasde contor-
narestalimitação.Porexemplo,suponhaquesejanecessáriodesenvolverumapes-
quisadeclientesbaseadaemváriostiposdeimpostosdevidos numcertoperíodode
tempo.Estapesquisadeveriafornecer:
• Onomedoimposto
18

## Página 22

CasadoCódigo Capítulo2. OprotocoloHTTP
• Operíodo(datainicialedatafinaldabusca)
Seestapesquisa forbaseadaemumúnicoimposto, nãoháproblemaalgum.
Mastomecomobaseumapesquisa baseadacomoumalistadeimpostos. Elaseria
semelhantea:
/pessoas?imposto.1=IR&data.inicio.1=2011-01-01&data.inicio.2=2012-01-01
Ondeanumeraç ão,nestecaso,seriaoelemento agrupadordosdados- ouseja,
um workaroundparaalimitaçãodedadosestruturados.
Quandoháanecessidadedefornecerdadoscomplexos, noentanto,épossível
fazê-lopelocorpodarequisição.Algocomo:
POST /clientes HTTP/1.1
Host: localhost:8080
Content-Type: text/xml
Content-Length: 93
<cliente>
<nome>Alexandre</nome>
<dataNascimento>2012-01-01</dataNascimento>
</cliente>
Quantoaeste tipodeparâmetro,nãohálimitações.Oservidorfazainterpreta-
çãodosdadosa partirdofatode queessesparâmetrossãoosúltimosdodocumento,
econtrolao tamanhodaleiturautilizandoo cabeçalho Content-Length.
2.4 Cabeçalhos
Oscabeçalhos,emHTTP,sãoutilizadosparatrafegartodootipodemetainforma-
çãoarespeito dasrequisições. Váriosdestescabeçalhossão padronizados;noen-
tanto,elessãofacilmenteextensíveisparacomportarqualquerparticularidade que
umaaplicaçãopossarequerernessesentido.
Porexemplo,aorealizarumarequisiç ão, peloFirefox,paraosite http://www.
casadocodigo.com.br/,asseguintesinformações sãoenviadas:
GET / HTTP/1.1
Host: www.casadocodigo.com.br
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:19.0) Gecko/20100101 Fire
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
19

## Página 23

2.4. Cabeçalhos CasadoCódigo
Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Co m o checar o tráfego via HTTP
Paravisualizarotráfegodestesdados,váriastécnicasestãoàdisposi-
ção. Asmaissimplessãoainstalaçãodeum plugindoFirefox chamado
Live HTTP Headers ouapertar F12noChrome.
Portanto,osseguintescabeçalhossãoenviados: Host, User-Agent, Accept,
Accept-Language, Accept-Encodinge Connection. Cadaumdesses tem
umsignificado paraoservidor- noentanto,oprotocoloHTTP nãoexigenenhum
deles. Aoestabelecerestaliberdade, tantoocliente quantooservidorestãolivres
paranegociaroconteúdodamaneiracomoacharem melhor.
Obviamente,istonão querdizerqueestescabeçalhosnãosãopadronizados.Da
listaacima, cadacabeçalhopossuiumaexplicaç ão:
•Host-mostra qualfoioDNSutilizadoparachegaraesteservidor
•User-Agent-forneceinformações sobreomeioutilizado paraacessareste
endereço
•Accept-realizanegociaç ãocomoservidorarespeitodoconteúdoaceito
(maisinformações naseção2.4).
•Accept-Language-negociacomoservidor qualoidiomaa serutilizadona
resposta
•Accept-Encoding-negociacomoservidor qualacodificaçãoa serutilizada
naresposta
•Connection-ajustaotipodeconexãocomoservidor(persistente ounão).
Tecnicamentefalando,os cabeçalhossãoutilizadosparatráfegodemeta dados
-ouseja,informações arespeito dainformação“ d everdade”.T o m eumcenáriode
enviode emails:odestinatário,oassuntoeoutrasinformaçõessãoapenas meta dados
-averdadeirainformaç ãoéoconteúdodo email.Destaforma,umarequisiçãopara
umserviçoHTTPdeenviode emailspoderiaserfeitadaseguinteforma:
20

## Página 24

CasadoCódigo Capítulo2. OprotocoloHTTP
POST /email HTTP/1.1
Host: brejaonline.com.br
Destinatario: alesaudate@gmail.com
Assunto: Quanto custa a cerveja dos Simpsons?
VáriosusosdiferentessãodadosparacabeçalhosemHTTP.Aolongodestelivro,
voumencioná-losquandonecessário.
2.5 MediaTypes
Aorealizarumarequisiç ão paraosite http://www.casadocodigo.com.br,o Media
Type text/html éutilizado,indicando paraonavegador qualéotipodainfor-
maçãoqueestásendotrafegada(nocaso,HTML).Istoéutilizadoparaqueocliente
saibacomotrabalharcomoresultado(e não comtentativaeerro, porexemplo),
dessamaneira,os Media Types sãoformaspadronizadasdedescreverumadeter-
minadainformação.
Os Media Types sãodivididosem tipose subtipos,eacrescidosdeparâmetros
(sehouverem).Sãocompostoscomoseguinte formato: tipo/subtipo.Sehouverem
parâmetros,o ;(ponto-e-vírgula)seráutilizadoparadelimitara áreadosparâme-
tros.Portanto,umexemplode Media Type seria text/xml; charset="utf-8”(para
descreverumXML cujacodificaçãosejaUTF-8).
Ostiposmaiscomunssão:
•application
•audio
•image
•t e x t
•video
•v n d
Cadaumdesses tiposéutilizadocomdiferentespropósitos. Applicationéuti-
lizadoparatráfegodedadosespecíficosdecertasaplicações. Audioéutilizadopara
formatosdeáudio. Imageéutilizadoparaformatosdeimagens. T e x téutilizado
paraformatosdetextopadronizadosoufacilmenteinteligíveisporhumanos. Video
21

## Página 25

2.5.MediaTypes CasadoCódigo
éutilizadoparaformatosdevídeo. V n déparatráfegodeinformações desoftwares
específicos(porexemplo,oMicrosoftOffice).
EmserviçosREST,váriostiposdiferentesde Media Types sãoutilizados.As
maneirasmaiscomunsderepresentardadosestruturados,em serviçosREST,sãovia
XMLeJSON, quesãorepresentadospelos Media Types application/xml e
application/json,respectivamente.OXML tambémpodeserrepresentadopor
text/xml,desde quepossaserconsideradolegívelporhumanos.
Note que subtipos mais complexos doque isso podem ser representados
com o sinal+ (mais). Este sinal é utilizado em váriossubtipos para delimi-
tação demaisde umsubtipo. Esteé ocaso com XHTML,porexemplo,que
denota otipo HTML acrescidodas regras de XML, ecujo media type é
application/xhtml+xml. Outrocasocomum é o do protocolo SOAP,cujo
media type é application/soap+xml.
Os Media Types são negociados apartir dos cabeçalhos Accept e
Content-Type. Oprimeiroéutilizadoemrequisiç ões,eosegundo,emrespos-
tas.
Aoutilizarocabeçalho Accept,oclienteinformaaoservidor qualtipodedados
esperareceber.Casosejaotipodedados quenãopossaserfornecidopeloservidor,
omesmoretornaocódigodeerro 415(apresentadonaseção2.6),indicandoqueo
M e d i aT y p enãoésuportado.Seotipodedadosexistir,entãoosdados sãofornecidos
eo cabeçalho Content-Typeapresentaqualéotipodeinformaçãofornecida.
Existemváriasformasderealizarestasolicitaç ão.Casooclienteestejadisposto
areceber maisdeum tipodedados,o cabeçalho Acceptpodeserutilizadopara
estanegociação. Porexemplo,seoclientepuderreceberqualquer tipodeimagem,
estasolicitaçãopodeutilizarum curinga,representadopor*(asterisco).Oservidor
iráconverterestasolicitaçãoemum tipoadequado.Estanegociaçãoserásimilarà
seguinte:
Requisição:
GET /foto/1 HTTP/1.1
Host: brejaonline.com.br
Accept: image/*
Resposta:
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 10248
22

## Página 26

CasadoCódigo Capítulo2. OprotocoloHTTP
Além disso,tambémé possível solicitarmaisde umtipo de dadosapenas
separando-ospor ,(vírgula).Porexemplo,umclientedeuma páginawebpoderia
realizarumasolicitaç ãocomoaseguinte:
GET / HTTP/1.1
Host: brejaonline.com.br
Accept:text/html,*/*
Note,assim,queoclientesolicitauma páginaHTMLqueseumanãoestiverdis-
ponível,qualquertipodeconteúdoéaceito-comopodeserobservadopelapresença
dedoiscuringas,em tipoesubtipodedados. Nestecaso,aprioridadeatendidadaé
ada especificidade,ouseja,como text/htmlémaisespecífico,temmaisprioridade.
Emcasodeváriostiposdedados quenãoatendamaestaregra,o parâmetro q
podeseradotadoparaquesepossarealizardiferenciações depeso.Esteparâmetro
recebevaloresvariandoentre0.1e1,contendoaordemdeprioridade. Porexemplo,
suponhaaseguinterequisição:
GET / HTTP/1.1
Host: brejaonline.com.br
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
IstosignificaquetantoHTMLquantoXHTMLtêmprioridademáxima.Nafalta
deumarepresentaç ãodo recursocomqualquerumdesses tiposdedados,oXML
éaceitocomprioridade90%. NaausênciadoXML,qualqueroutrarepresentaçãoé
aceita,comprioridade80%.
2.6 Códigos de status
T o d arequisiçãoqueéenviadaparaoservidor retornaumcódigode status.Esses
códigossãodivididosemcincofamílias:1xx,2xx,3xx,4xxe5xx,sendo:
• 1xx-Informacionais
• 2xx-Códigosdesucesso
• 3xx-Códigosderedirecionamento
• 4xx-Erroscausadospelocliente
• 5xx-Errosoriginadosnoservidor
23

## Página 27

2.6. Códigosdestatus CasadoCódigo
DeacordocomLeonardRichardsoneSamRuby,oscódigos maisimportantese
maisutilizadossão:
2xx
20 0- O K
Indicaqueaoperaçãoindicada tevesucesso.
20 1- Crea t ed
Indicaqueorecursodesejadofoicriadocomsucesso. Deveretornarumcabeça-
lho Location,quedeveconteraURL ondeorecursorecém-criadoestádisponível.
20 2- Accepted
Indicaqueasolicitaçãofoirecebidaeseráprocessadaemoutromomento.Étipi-
camenteutilizadaemrequisições assíncronas,quenãoserãoprocessadasem tempo
real.Poressemotivo,poderetornarumcabeçalho Location,quetraráumaURL
ondeoclientepodeconsultarseorecursojáestádisponívelounão.
20 4- N oContent
Usualmenteenviadoemrespostaaumarequisiç ão PUT, POSTou DELETE,
ondeoservidor poderecusar-seaenviarconteúdo.
206 - Partial Content
Utilizadoemrequisições GETparciais,ouseja,quedemandamapenaspartedo
conteúdoarmazenadonoservidor(caso muitoutilizadoemservidoresde down-
load).
3xx
301 -Moved Permanently
Significaqueorecursosolicitadofoirealocadopermanentemente.U m aresposta
comocódigo 301deveconterum cabeçalho LocationcomaURLcompleta(ou
seja,comdescriç ãodeprotocoloeservidor)de ondeorecursoestáatualmente.
24

## Página 28

CasadoCódigo Capítulo2. OprotocoloHTTP
303 - S e eOther
Éutilizado quandoarequisiçãofoiprocessada,masoservidornãodesejaenviar
oresultadodoprocessamento. Aoinvésdisso,oservidor enviaarespostacomeste
códigode statuseo cabeçalho Location,informando ondearespostadoproces-
samentoestá.
304 - N o tModified
Éutilizado,principalmente,emrequisiç ões GETcondicionais-quandoocliente
desejaveraresposta apenasseelativersidoalteradaem relaçãoaumarequisiç ão
anterior.
307 - T emporaryRedirect
Similarao 301,masindicaqueoredirecionamentoétemporário,não perma-
nente.
4xx
400 - Bad Request
Éumarespostagenérica paraqualquertipodeerrodeprocessamento cujares-
ponsabilidadeédoclientedo serviço.
401 - Unauthorized
Utilizadoquandooclienteestátentandorealizarumaoperaç ãosemterforne-
cidodadosde autenticação(oua autenticaçãofornecida forinválida).
403 - Forbidden
Utilizadoquandooclienteestátentandorealizarumaoperaç ãosemteradevida
autorização.
404 - N o tFound
Utilizadoquandoorecursosolicitadonãoexiste.
25

## Página 29

2.6. Códigosdestatus CasadoCódigo
405 - Method N o tAllowed
UtilizadoquandoométodoHTTPutilizado não ésuportadopelaURL.Deve
incluirum cabeçalho Allownaresposta,contendoalistagemdosmétodos supor-
tados(separados por“,”).
409 - Conflict
Utilizadoquandoháconflitosentredoisrecursos. Comumenteutilizadoemres-
postaacriações deconteúdosquetenhamrestrições dedadosúnicos- porexemplo,
criaçãodeum usuárionosistemautilizandoum loginjáexistente.Seforcausado
pelaexistênciadeoutrorecurso(comonocasocitado),arespostadeveconterum
cabeçalho Location,explicitandoalocalizaç ãodo recursoqueéafontedoconflito.
4 1 0- G o n e
Semelhanteao404,masindicaqueumrecursojáexistiunestelocal.
4 1 2- Precondition failed
Comumenteutilizadoemrespostaarequisições GETcondicionais.
4 1 5- U n s u p p o r t e dM e d i aT y p e
Utilizadoemrespostaaclientes quesolicitamum tipodedados quenãoésu-
portado- porexemplo,solicitarJSON quandooúnicoformatodedados suportado
éXML.
5xx
500 - Internal Server Error
Éumarespostadeerrogenérica,utilizada quandonenhumaoutraseaplica.
503 - Service Unavailable
Indicaqueoservidorestáatendendorequisições, masoserviçoemquestão não
estáfuncionandocorretamente.Podeincluirumcabeçalho Retry-After,dizendo
aoclientequandoeledeveriatentarsubmeterarequisiçãonovamente.
26

## Página 30

CasadoCódigo Capítulo2. OprotocoloHTTP
2.7 Conclusão
V o c êpôde conferir,nestecapítulo,osprincípiosbásicosdoprotocoloHTTP. Estes
princípiossãoousodecabeçalhos,métodos,códigosde statuseformatosdedados
-queformamabasedousoeficientedeREST.
V o c êiráconferir,nospróximoscapítulos,comoREST sebeneficiadosprincípios
desteprotocolode formaatiraromáximo proveitodestatécnica.
27

## Página 32

Capítulo3
ConceitosdeREST
“ Amente q u ese a b r ea u m anova idéiajamais volta a seu tamanho original”
–AlbertEinstein
Comoditoanteriormente,RESTébaseado nosconceitosdoprotocoloHTTP.
Alémdisso,esteprotocoloéa basepara a webcomoaconhecemos,sendo quea
próprianavegaçãonestapodeserencaradacomoum usodeREST.
Noentanto,RESTnãoétãosimplesquantosimplesmenteutilizarHTTP-exis-
temregrasquedevemserseguidasparaserealizarusoefetivodesteprotocolo. A
intençãodeste capítuloéapresentarquaissãoestesconceitos,demaneira quevocê,
leitor,conhe çaastécnicascertasparadesenvolvimentodestetipodeserviço.
3.1 Semânticas de recursos
T o d oserviçoRESTébaseado noschamados recursos,quesãoentidadesbemde-
finidasemsistemas, quepossuemidentificadoreseendere ços(URL’s)próprios.No
casoda aplicaçãoqueestamosdesenvolvendo, brejaonline.com.br,podemos

## Página 33

3.1. Semânticasderecursos CasadoCódigo
assumirqueumacervejaéum recurso.Assim,asregrasdeRESTdizem queascer-
vejasdevemterumaURLprópriaequeestaURLdeve sersignificativa.Destaforma,
umaboaURLparacervejaspodeser /cervejas.
URL ’s no singular ou no plural?
Nãoexistemregrasem relaçãoaestasURL’sestaremnosingularou
noplural- ouseja,nãoimportasevocêprefereutilizar /cervejaou
/cervejas.Oideal, noentanto,émanterumpadrão- tenhatodas as
suasURL’snosingularoutodasnoplural,masnãomisturas.
Deacordocomo modeloREST,estaURLrealizaráinteraçãocom todasascerve-
jasdosistema. Paratratardecervejasespecíficas, sãousadosidentificadores. Estes
identificadorespodemterqualquerformato-porexemplo,suponhaumacerveja
ErdingerWeissbiercomcódigode barras123456.Notequeonomedacervejanão
servecomoidentificador(existemvárias“instâncias”deErdingerWeissbier),maso
códigodebarras,sim.
Destaforma,deveserpossívelbuscarestacervejaatravésdocódigodebarras,
comaURL /cervejas/123456. Lembre-se,regrassemelhantesaplicam-sea
qualquerrecurso.Oidentificadora serutilizadonaURLpodeserqualquercoisa
quevocêassimdesejar,e maisdeum tipodeidentificador podeserusadoparaal-
cançarumrecurso.Porexemplo,suponhaqueasuabasedeclientestenhatantoum
identificadorgeradopelobancodedados quantoosCPF’sdosclientes:
• Clientenúmero1:CPF445.973.986-00
• Clientenúmero2:CPF428.193.616-50
• Clientenúmero3:CPF719.760.617-92
Assim,parabuscaroclientedenúmero1,deve serpossívelutilizartantoaURL
/cliente/1quantoaURL /cliente/445.973.986-00.
Podemhavercasos,também,deidentificadorescompostos. Nestecaso,amelhor
práticaseriasepará-losutilizando;(ponto-e-vírgula).Porexemplo,um serviçode
mapasemquesejapossívelacharumpontoporlatitudeelongitude teriaURL’scomo
/local/-23.5882888;-46.6323259.
Maisàfrente,detalhareicasosmaiscomplexosdeURL’s.
30

## Página 34

CasadoCódigo Capítulo3. ConceitosdeREST
3.2 Interação p o rmétodos
ParainteragircomasURL’s,osmétodosHTTPsãoutilizados.Aregrade ouropara
estainteraçãoéque URL ’ssão substantivos, e métodos HTTPsão verbos.Istoquer
dizerqueosmétodosHTTPsãoosresponsáveisporprovocaralteraçõesnosrecursos
identificadospelasURL’s.
Estasmodificações sãopadronizadas,demaneiraque:
•GET-recuperaosdadosidentificados pelaURL
•POST-criaum novorecurso
•PUT-atualizaum recurso
•DELETE-apagaumrecurso
CRUD
Notequeestesquatrométodosprincipaispodemserdiretamenterelacionadosa
operaçõesdebancosdedados.Assim, pararecuperaroclientedenúmero1do banco
dedados,bastautilizarométodo GETemconjuntocomaURL /cliente/1;para
criarum novocliente,bastautilizarométodo POSTsobreaURL /cliente(o
identificadorserácriadopelobancodedados); paraatualizareste cliente,utilizeo
método PUTsobreaURL /cliente/1e,finalmente,paraapagarocliente,utilize
ométodo DELETEsobreaURL /cliente/1.
Notequetodasestasoperações são lógicas.Istoquerdizerqueutilizarométodo
DELETE,porexemplo,não significanecessariamenteexcluirodadodo bancode
dados-significa apenasindisponibilizarorecursoparaconsumopelométodoGET.
Ouseja, DELETEpodeapenasmarcarodado nobancodedadoscomo desativado.
Tarefas
CriarserviçosRESTqueexecutemtarefasdenegócio(ex: enviarume-mail,criar
umamáquinaemum serviçode cloud computing,validarumCPFe outrastarefas
quenãonecessariamenteenvolvaminteraçãocomum bancodedados)étarefa mais
complexa. Exigecertograudedomínio dateoriasobreREST,e muitasvezesnão
existemrespostas100% assertivasemrelaçãoàcorretude dasolução.
Paraobterresultadossatisfatórios,deve-se sempreteropensamentovoltado
paraaorientaçãoarecursos. Tomemoscomoexemploo casodoenviodee-mails:a
31

## Página 35

3.3. Representaçõesdistintas CasadoCódigo
URLdeve sermodeladaemformatodesubstantivo,ouseja,apenas /email.Para
enviaroe-mail,ocliente podeusarométodo POST-ouseja,como seestivesse
“criando”ume-mail.Damesmaforma,inicializarumamáquinaemum serviçode
cloud computingpodeterumaabordagemmaissimilaraumCRUD: parainicializar
amáquina,oclienteutilizaométodo POSTnaURL /maquinas.Paradesligá-la,
utilizaométodo DELETE.
Existem,também,casosemqueassoluções podemnão parecertriviaisàpri-
meiravista.U mcasoclássicoéodevalidações (deCPF,porexemplo).AURL pode
serclaramenteorientadaa substantivos( /validacao/CPF,porexemplo),mase
quantoaosmétodos?
Asolução paraestecasoépensardaseguintemaneira: “ e upreciso o b t e ruma
validação?Oucriaruma,ouapagar,ouatualizar?”.Destamaneira,arespostanatural
paraaquestão parececonvergirparaométodo GET.Noteque,nestecaso,entraem
cenao usodométodo HEAD-poderíamosutilizarométodo GETparaconseguir
resultadosdetalhadoseométodo HEADparaobterapenasocódigode statusda
validação(lembre-sede queestemétodonãoretornacorpo!).
3.3 Representações distintas
U mdospilaresdeRESTéo usode media typesparaalterarasrepresentações de
ummesmoconteúdo,sobperspectivasdistintas.Estaóticaficaevidente quandose
respondeàpergunta: “ q u eladodorecursoestouprocurandoeuqueroenxergar?
Precisodeumafotodeumacerveja, oudadescriçãodela?”.Porexemplo,aorealizar
umabuscaporumacervejanosistema,pode-setantodesejarumXMLcomosdados
dacerveja,quantoumJSON quantoumafotodacerveja:
32

## Página 36

CasadoCódigo Capítulo3. ConceitosdeREST
Figura3.1:Podesermaisinteressanteobterumafotodacervejado queadescrição
dela
ComREST,tudoissopodeserfeitoutilizando-seamesmaURL, porexemplo,
/cervejas/1. Oquevaimodificaroresultadoéasolicitaç ão queoclientefi-
zer,atravésdo cabeçalho Accept: seoclientefizerumasolicitaç ão paraaURL
/cervejas/1passandoocabeçalho Acceptcomovalor application/xml,
eleiráobterumarepresentaçãodacervejacomoXML. Masseocliente passarfizer
estarequisiçãopassandoovalor image/*,eleiráobterumafotodacerveja.
33

## Página 37

3.4.Us ocorretode statuscodes CasadoCódigo
O cabeçalho Accept e os curingas
Noteque,nesteexemplo,euestoufalandode obterumaimagempas-
sandoocabeçalho Acceptcomovalor image/*.Istosedádevidoao
fatode que,muitasvezes,nãoestamosinteressados notipodaimagem
(JPG,GIF,PNG,etc.),masapenas nofatode ela se rumaimagem!
LeonardRichardsoneSam Ruby[1]tambémdefendem,emuma abordagem
maispragmática,queéinteressanteoferecerdistin ções entreesses tiposdedados
naprópriaURL,a partirdeextensões(similar àsextensõesdearquivos nosistema
operacional).Porexemplo,nocasodas cervejas,paraobterumarepresentaçãodas
cervejascomoXML,utilizaríamosaURL /cervejas.xml;paraobterarepresen-
taçãocomoumaimagem jpg,utilizaríamosaURL /cervejas.jpg.Notequeesta
abordagempossuivantagensedesvantagens:ao passoqueatestabilidadeésimpli-
ficada(jáquepodemostestarosresultadospelonavegador),aimplementaçãopode
sermaiscomplexae tambémpodeinduzirdiferenciações nasimplementações (ou
seja,terlógicasdistintas parabuscardadossemelhantes).
3.4 Uso correto de status codes
AlgoqueRESTtambémprevêéousocorretodos status codesHTTP.Naprática,
issosignificaconhecê-loseaplicardeacordocomasituaç ão.Porexemplo,ocódigo
200( OK)éutilizadoemgrande partedassituações (oquepodeacabar“viciando”o
desenvolvedor),masacriaçãoderecursosdeve retornar,quasesempre,ocódigo201
( Created)eo cabeçalho Location,indicandoalocalizaç ãodo recursocriado.
Ainda,sedoisclientesrealizaremcriaç ãoderecursosde formaqueestesforne-
çamachaveutilizadaparareferenciarorecurso(ouseja,existeuma restriçãode que
achavedeveserúnicaporrecurso),eestesdoisclientesforneceremamesma chave
nacriaçãodo recurso,ocódigode status409( Conflict)deve serutilizado.
34

## Página 38

CasadoCódigo Capítulo3. ConceitosdeREST
Posso utilizar a chaveprimária d omeu banco dedados
como ID d o srecursos?
Éerradoassumir queachaveutilizadanosrecursosserá sempreo
IDdo bancodedados.Éperfeitamenteaceitávelutilizaresta chave,mas
istodeveseruma coincidência,demaneiraqueoseucliente jamaisse
sintacomo seestivessesimplesmenteutilizandoumainterfacediferente
paraacessarum bancodedados. Estarestriçãoécondizentecomo que
mencioneiem meulivroSOAAplicado:integrandocom webservicese
além[2],dequeoclientenuncadevesentirosefeitosdeumamodificaç ão
nainfra-estruturado serviço.
Porexemplo,suponhaqueacriaçãodosclientes nacervejariautilizeoCPFcomo
chavedosrecursos. Sedoisclientesdos serviçostentaremsecadastrarcomomesmo
CPF,umdosclientesdevereceberocódigo409.Arespostacomessecódigodeve
contero cabeçalho Location,indicando ondeestáorecursoqueoriginouocon-
flito.
Aolongodolivro,apresentareisituações ondeousocorretodoscódigosde status
faráadiferençanoconsumodosserviços.
3.5 HATEOAS
AúltimadastécnicasmencionadasporRoyéousode Hypermedia A sThe Engine
Of Application State-HATEOAS.Trata-sede algoquetododesenvolvedor webjá
conhece(apenas nãoporessenome).
T o d avezqueacessamosumapáginaweb,alémdotextodapágina,diversos links
paraoutrosrecursossãocarregados.Estesrecursosincluem scripts JavaScript,
CSS,imagenseoutros. Alémdisso, muitaspáginastêmformulários,queencami-
nhamdadosparaoutrasURL’s.
Porexemplo,considereoseguinte trechodepáginaHTML:
<html>
<head>
<link rel="icon" href="/assets/favicon.ico" type="image/ico" />
<link href="/assets/fonts.css" rel="stylesheet" type="text/css" />
</head>
35

## Página 39

3.5. HATEOAS CasadoCódigo
<body>
<img src="/assets/header.jpg" />
</body>
</html>
Nela,existeumareferênciaparaoíconedapágina(referenciadocoma t ag link
eatributo rel="icon"),umareferênciaparaumarquivoCSSeumareferênciapara
umaimagem.
HATEOASconsideraestes linksdamesmaforma,atravésdareferênciaaações
quepodemsertomadasapartirdaentidadeatual.Porexemplo,vamos modelaro
sistemadecompras danossacervejaria.Paracriarumpedidodecompra,énecessá-
riofornecerumXMLcontendoosdados darequisição:
<compra>
<item>
<cerveja id="1">Stella Artois</cerveja>
<quantidade>1</quantidade>
</item>
</compra>
Seestacompraforaceitapeloservidor,oseguinte podeserretornado:
<compra id="123">
<item>
<cerveja id="1">Stella Artois</cerveja>
<quantidade>1</quantidade>
</item>
<link rel="pagamento" href="/pagamento/123" />
</compra>
Noteapresen çada t ag link.SeoclienteutilizaraURLpresente noatributo
href,podeinformaraoservidoromeiodepagamentoaceito paraacompra.Acri-
açãodomeiodepagamentoserá feitaatravésdométodoHTTP POST,conforme
mencionadoanteriormente. Esseconhecimento“prévio”fazpartedoquesecon-
vencionouchamar,emREST,de interface uniforme.
Estes links,emHATEOAS, têmdoissegmentos: links estruturaisou transicio-
nais. Oslinksestruturais,comodizo nome,sãoreferentesàestruturado próprio
conteúdo.Porexemplo,suponhaquevocêbusqueumalistagemdeendere çosdeum
determinadocliente:
36

## Página 40

CasadoCódigo Capítulo3. ConceitosdeREST
<cliente>
<enderecos>
<link href="/cliente/1/endereco/1" title="Endereço comercial" />
<link href="/cliente/1/endereco/2" title="Endereço residencial" />
<link href="/cliente/1/endereco/3" title="Endereço alternativo" />
</endereco>
</cliente>
Esteslinksproduzemdiversosbenefícios paraocliente.
Oprimeirobenefício,e talvezomaisóbvio,éareduçãodoacoplamentoentre
oclienteeoservidor, jáqueocliente podeseguiresteslinks paradescobrironde
estãoosendere ços.CasoaURLdeendere çosmude,ocliente nãodeverásentiros
impactosseseguiros links.
Osegundobenefícioé queelesexercemuma açãointeligentedo pontodevista
docliente,jáqueestenãoprecisarecuperardadosde quenãoprecisa.Seeleprecisar
apenasdoendere çocomercial, bastaseguirsomenteo linkquecontémoendere ço
comercial,e nãotodososoutros.
Oterceiroédo pontodevistada performance.Alémderecuperarum volume
menordedados,em casodeumalista(como nesteexemplo,deendere ços),ocliente
podeparalelizarasrequisições e,assim,diminuiro tempodeobtençãodasinforma-
ções. Obviamente,issodependedalatênciadarede(ouseja,o tempodecorridoem
relaçãoà saídadarequisiçãodamáquinaclienteechegadaaoservidor,evice-versa),
masissopodebeneficiar-sedocacheamentodo recurso.
Jáoslinkstransicionais sãorelativosaações, ouseja,a ações queocliente pode
efetuarutilizandoaquele recurso.V o c êjáviuesteexemplo quandoeumereferíao
pagamentodacompra.
Existemcinco atributosimportantesparaoslinks:
• href
•rel
•title
•method
•type
37

## Página 41

3.6. Sumário CasadoCódigo
Existe alguma especificação para estes links?
Existeumaespecificação formalparatratamentodesteslinks cha-
madaXLink(disponívelemhttp://www.w3.org/TR/xlink/).Osatributos
href, titlee methodestãodefinidos lá.Osoutrossãousadoscomo
convenção.
Oatributo hreffazreferênciaàURL ondeorecursoestálocalizado(apenas
comolembrete,estaURL podeserabsoluta-comespecificaç ãodeprotocolo, host,
porta,etc.- ourelativa-ouseja,oclientedeve buscarorecursonomesmoservidor
ondefezaprimeirarequisição.
Oatributo reléutilizadocomum textodeauxílio paraouso,quenãodeve
serlidopeloclientefinal. Ovalordeste atributodeveserutilizadopelocliente
paradetectaro tipodeinformaçãopresente naURL.Porexemplo,oNetflix uti-
lizaURL’spararealizarestadistin ção,algocomohttp://schemas.netflix.com/catalog/
people.directors. Casotenhacuriosidade,consulteaURL http://developer.netflix.
com/docs/REST_API_Reference-ondeestápresenteadocumentaçãodereferência
parautilizaçãodaAPIdoNetflix.
Oatributo titlecontémumadescrição,legível porhumanos,dainformação
queestápresentenaURL.
Oatributo methodéumdos tiposmenosutilizados;quandooé,indicaquais
tiposdemétodosHTTPsãosuportadospelaURL(separados porvírgula).
Finalmente,oatributo typeindicaquais media typessãosuportadospelaURL,
etambémsãodosmenosutilizados.
3.6 Sumário
V o c êconheceu,nestecapítulo,astécnicasbásicasdeREST- ouseja,oqueénecessá-
rioconhecerantesdecome çaratrabalharcomREST.Obviamente,muitasquestões
aindanãoforamrespondidas-comolidarcomclientesconcorrentes? Comotraba-
lharcom cache?Comomodelarcasosmaisavançados?
Aolongodospróximoscapítulos, vocêconheceráarespostaparaestase outras
questões. V a m o semfrente?
38

## Página 42

Capítulo4
Tip osdedados
“Conhecimentoépoder”
–FrancisBacon
Paratrabalhardemaneiraeficientecom seusdados,énecessárioconhecer,an-
tes,ostiposdedadosmaiscomunsaseremutilizados- suasvantagens,desvantagens,
usosmaiscomuns,etc.Alémdisso,énecessário sabercomoutilizá-losnasualin-
guagemdeprogramação.
4.1 XML
XMLéumasigla quesignifica eXtensible Markup Language ,ou linguagem
de marcação extensível. Porterestanaturezaextensível,conseguimosexpressar
grandepartedenossasinformações utilizandoeste formato.
XMLéumalinguagem bastantesemelhanteaHTML( HyperText Markup
Language),porém,comsuasprópriasparticularidades.Porexemplo,todoarquivo

## Página 43

4.2. FerramentalXML:conhecendoosXML Schemas CasadoCódigo
XMLtem um e apenas umelemento-raiz(assimcomoHTML),comadiferen çade
queesteelemento-raizéflexívelo bastanteparaterqualquernome.
Alémdisso,umXMLtemseções específicasparafornecimentode instruçõ e sde
processamento-ouseja,seções queserãointerpretadas porprocessadoresdeXML
que,noentanto,nãofazempartedosdados. Estasseções recebemosnomesde p r ó -
logo(quandoestãolocalizadas antesdosdados)e epílogo,quandoestãolocalizadas
depois. Porexemplo,écomumencontrarumprólogo quedeterminaaversãodo
XMLeo charsetutilizado.Esteprólogotemoseguinte formato:
<?xml version="1.0" encoding="UTF-8" ?>
Ouseja,diferentede t ag sregularesdeXML(que têmoformato <tag></tag>),
umainstruçãodeprocessamento temoformato <?nome-da-instrução ?>.No
exemplo,euestouespecificandoaversãodeXMLutilizada(1.0)eo charset(UTF-8).
Aforaestainformação,asestruturasmaisbásicasemumXML sãoas t ag seos
atributos,de formaqueumXMLsimples temoseguinte formato:
<?xml version="1.0" encoding="UTF-8" ?>
<tag atributo="valor">conteúdo da tag</tag>
Comoobservadonoexemplo,osdadostransportados pelasuaaplicação po-
demestarpresentes tantonaformadeatributoscomodeconteúdodas t ag s.Emum
exemplomaispróximodo casedecervejaria,umacerveja podesertransmitidada
seguinteforma:
<?xml version="1.0" encoding="UTF-8" ?>
<cerveja id="1">
<nome>Stella Artois</nome>
</cerveja>
4.2 Ferramental XML: conhecendo os XML Schemas
Porserumformatoamplamenteutilizadopordiversostiposdeaplicação,XMLcon-
témdiversostiposdeutilitáriosparaváriosfins,asaber:
• Validaçãode formatoeconteúdo;
•Buscadedados;
• Transformação
40

## Página 44

CasadoCódigo Capítulo4. Tiposdedados
A ferramenta XMLmais utilizada quando se trata de XMLsão os XML
Schemas.Trata-sedearquivoscapazesdedescrevero formatoquemumdetermi-
nadoXMLdeve ter(lembre-se,XMLéflexívela pontodepermitirqualquerinfor-
mação).U mXML Schema,comoum todo,éanálogoàdefiniçãode classesemJava:
define-seospacotes(que,emum XML Schema,sãodefinidoscomo namespaces)e
asclasses,propriamenteditas(que,em XML Schemas,sãoostipos).
Utiliza-se XML Schemas paraquetantooclientequantooservidortenhamum
“acordo”arespeitodoqueenviar/receber(emtermos daestruturadainformação).
Porexemplo,suponhaquecadaumadascervejariaspossuaumanodefundação,
assim:
<cervejaria>
<fundacao>1850</fundacao>
</cervejaria>
Seoclientenãotiverumareferênciaarespeitodo queenviar,elepodeenviaros
dadosassim:
<cervejaria>
<anoFundacao>1850</anoFundacao>
</cervejaria>
Noteque,destaforma,ainformaçãonãoseriainteligíveldo pontodevistado
clientee/oudo serviço.Assim,paramanteramboscientesdoformatoaserutilizado,
pode-seutilizarum XML Schema.
U mXML Schema simplespodeserdefinidodaseguinteforma:
<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema"
targetNamespace="http://brejaonline.com.br/comum/v1"
xmlns:tns="http://brejaonline.com.br/comum/v1">
</schema>
U mXML Schema ésempredefinidodentro da t ag schema. Esta t agdeve
conter,obrigatoriamente,areferênciaparao XML Schema http://www.w3.org/2001/
XMLSchemaeoatributo targetNamespace,queapontaqualdevesero namespace
utilizadopeloXMLqueestiversendovalidado poreste XML Schema.Alémdisso,
porconvenção,o próprio namespaceéreferenciadonodocumentoatravésdadecla-
ração xmlns:tns,indicando queoprefixo tnspoderáserutilizadonoescopo
deste XML Schema.Estapráticanãoéobrigatória,masésemprerecomendada.
41

## Página 45

4.2. FerramentalXML:conhecendoosXML Schemas CasadoCódigo
Aestruturadosdados,em XML Schemas,sãodefinidasemtermosde elemen-
t o s.Oselementossãoutilizadosparadefinirinformações arespeito das t ag s:nome
da t ag,númeroderepetições permitido,quais sub-tagssãopermitidas,quaisatribu-
tosuma t agdeveter,etc.
Paradefinir um elemento dentro de umXML Schema, bastautilizar at ag
element.Porexemplo,paradefiniruma t ag nomenum XML Schema,bastautili-
zaroseguinte:
<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema"
targetNamespace="http://brejaonline.com.br/comum/v1"
xmlns:tns="http://brejaonline.com.br/comum/v1">
<element name="nome" type="string" />
</schema>
Conformemencionadoanteriormente,adefiniçãodosdados propriamentedi-
toséfeitaatravésdetipos.Estestipossãodivididosentresimplesecomplexos,sendo
ossimplesaqueles quesão strings,datas,númerosouderivadosdestes;jáoscomple-
xos,sãodefinidosapartirdajunçãodeelementosde tipossimplese/ououtrostipos
complexos.
Tiposnovospodemsercriadosouestendidosàvontade, sejamestestipossim-
plesoucomplexos.Porexemplo,paracriarum tiposimplesnovo,bastautilizaro
seguinte:
<simpleType name="CEP" />
Nestemesmo schema,um tipocomplexopodesercriadodaseguinteforma:
<complexType name="Endereco">
<sequence>
<element name="cep" type="tns:CEP" />
<element name="logradouro" type="string" />
</sequence>
</complexType>
Notequeadefiniçãodo tipocomplexoenvolvea t ag sequence.Esta t agéuti-
lizadaparadeterminarqueoselementos nelaenvolvidosdevem serinseridosnesta
ordem.Porexemplo,aoimplementareste tipocomplexo,oseguinteéaceito:
<endereco>
<cep>12345-678</cep>
42

## Página 46

CasadoCódigo Capítulo4. Tiposdedados
<logradouro>Rua das cervejas</logradouro>
</endereco>
Porém,oinversonãoéaceito:
<endereco>
<logradouro>Rua das cervejas</logradouro>
<cep>12345-678</cep>
</endereco>
Definindo formas de validação p a r atipos simples
Ostipossimples,comoditoantes,oferecemextensibilidadeem relaçãoa outros
tipossimples.Estaextensãopodeserfeitaparaosfins maisdiversos,sendo queo
usomaiscomumdestafacilidadeé paraproverrestrições sobreestestipossimples.
Porexemplo,nocasodoCEP,sabemos queestesegueumaestrutura bemclarade
validação,queéopadrão cinco dígitos (traço) três dígitos .Ouseja,
umaexpressãoregular podeserutilizadaparaestavalidação.
Estarestriçãoérepresentadautilizando-sea t ag restriction.Esta t ag,por
suavez,possuiumatributo base,queéutilizadoparaindicarqualseráo“tipopai”
aserutilizadoporestedado. Porexemplo,nocasodeumCEP,o tipoaserutilizado
comotipopai será string. Assim,oelemento CEPpodeserrepresentadoda
seguinteforma:
<simpleType name="CEP">
<restriction base="string">
</restriction>
</simpleType>
Finalmente,dentroda t ag restrictionéquepodemosdefiniro tipoderes-
triçãoqueseráaplicadaaoutilizarestetipo.Podemosdefinirumasériede restrições,
comoenumerações dedados(ouseja, sóépossívelutilizarosvaloresespecificados),
comprimentomáximodastring,valoresmáximosemínimos quenúmerospodem
ter,etc.Comoqueremosutilizarumaexpressãoregular,utilizamosa t ag pattern,
quedefineum atributo value. Atravésdesteatributo,especificamosaexpressão
regular.
Assimsendo,definimoso nossotipoCEPdaseguinteforma:
<simpleType name="CEP">
<restriction base="string">
43

## Página 47

4.2. FerramentalXML:conhecendoosXML Schemas CasadoCódigo
<pattern value="\d{5}-\d{3}" />
</restriction>
</simpleType>
Expressões regulares
Expressõesregulares sãoutilizadasparadeterminarformatosquecer-
tasstringsdevemter.Porexemplo,estasexpressões podemserutilizadas
paravalidarendere çosdee-mail,númerosde cartão decrédito,datas,
etc. Porserumassuntodemasiadocomprido(querendemlivros ape-
nassobreisso),melimitoaquia apenasexplicarosignificadodopadrão
acima.
Osímbolo \dsignificaumdígito(qualquerum). Aoterosinal {5}
anexado,indica quecincodígitos são aceitos. Otraçorepresentaasí
próprio.
Explorando tipos complexos
Comoapresentadoanteriormente,umtipocomplexo,emum XML Schema,é
semelhanteauma classeJava. Porexemplo,adefiniç ãodeumendere çopodeser
feitadaseguinteforma:
<complexType name="Endereco">
<sequence>
<element name="CEP" type="tns:CEP" />
<element name="logradouro" type="string" />
</sequence>
</complexType>
Noteareferênciaaotipo“CEP”,definidoanteriormente.Oprefixo tns,con-
formemencionado,fazreferênciaao namespacedopróprioarquivo(semelhantea
umareferênciaaumpacoteJava-que,noentanto,possuiumaformaabreviada,que
éoprefixo).
Ostiposcomplexoscomportamdiversasfacilidades,comoheran çaedefiniç ão
deatributos. Porexemplo,considereo tipocomplexo Pessoa:
<complexType name="Pessoa">
</complexType>
44

## Página 48

CasadoCódigo Capítulo4. Tiposdedados
Supondoqueuma Pessoasejaumasuperdefinição paraumapessoafísica
oujurídica,queremos queotipo Pessoasejaabstrato.Assim,podemosdefiniro
atributo abstract:
<complexType name="Pessoa" abstract="true">
</complexType>
Noteque,destaforma,nãohaveráumaimplementaçãodo quefordefinidoneste
tipo,apenasdeseussubtipos.Paracriarumaextensãodeste tipo,utiliza-seas t ag s
complexContente extension,assim:
<complexType name="PessoaFisica">
<complexContent>
<extension base="tns:Pessoa">
</extension>
</complexContent>
</complexType>
Assim,épossíveldefinirelementos tantonosupertipoquantonosubtipo.Por
exemplo,considereoseguinte:
<complexType name="Pessoa" abstract="true">
<sequence>
<element name="nome" type="string" />
</sequence>
</complexType>
<complexType name="PessoaFisica">
<complexContent>
<extension base="tns:Pessoa">
<sequence>
<element name="cpf" type="tns:CPF" />
</sequence>
</extension>
</complexContent>
</complexType>
Assim,aimplementaçãodeste tipopodeficarassim:
<pessoaFisica>
<nome>Alexandre</nome>
45

## Página 49

4.2. FerramentalXML:conhecendoosXML Schemas CasadoCódigo
<cpf>123.456.789-09</cpf>
</pessoaFisica>
Alémdisso,épossíveldefiniratributosnostiposcomplexos.Porexemplo,con-
sidereoseguinte:
<complexType name="Pessoa" abstract="true">
<attribute name="id" type="long" />
</complexType>
Assim,aimplementaçãodeste tipoficariaassim:
<pessoaFisica id="1" />
U mXML Schema tambémpodeimportaroutros, notavelmentepararealizar
composiçõesentreváriostiposdiferentes.Porexemplo,considereasduasdefinições
de XML Schemas:
<?xml version="1.0" encoding="UTF-8"?>
<schema targetNamespace="http://brejaonline.com.br/endereco/v1"
elementFormDefault="qualified" xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:tns="http://brejaonline.com.br/endereco/v1">
<simpleType name="CEP">
<restriction base="string">
<pattern value="\d{5}-\d{3}" />
</restriction>
</simpleType>
<complexType name="Endereco">
<sequence>
<element name="cep" type="tns:CEP" />
<element name="logradouro" type="string" />
</sequence>
</complexType>
</schema>
Notequeeste XML Schema possuio targetNamespacedefinidocomo http:
//brejaonline.com.br/endereco/v1.
Agora,considereumsegundo XML Schema:
46

## Página 50

CasadoCódigo Capítulo4. Tiposdedados
<?xml version="1.0" encoding="UTF-8"?>
<schema targetNamespace="http://brejaonline.com.br/pessoa/v1"
elementFormDefault="qualified" xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:tns="http://brejaonline.com.br/pessoa/v1">
<simpleType name="CPF">
<restriction base="string">
<pattern value="\d{3}\.\d{3}\.\d{3}-\d{2}" />
</restriction>
</simpleType>
<complexType name="Pessoa" abstract="true">
<sequence>
<element name="nome" type="string" />
</sequence>
<attribute name="id" type="long" />
</complexType>
<complexType name="PessoaFisica">
<complexContent>
<extension base="tns:Pessoa">
<sequence>
<element name="cpf" type="tns:CPF" />
</sequence>
</extension>
</complexContent>
</complexType>
</schema>
Noteque,nestesegundo XML Schema,o namespaceéhttp://brejaonline.com.br/
pessoa/v1(ouseja,diferentedo namespacedeendere ços).
Parautilizaro XML Schema deendere çosno XML Schema depessoas,é ne-
cessárioefetuardoispassos:oprimeiro,édefinirumprefixo parao namespacede
endereços.Porexemplo,paradefiniroprefixo end,utiliza-seoseguinte:
<?xml version="1.0" encoding="UTF-8"?>
<schema targetNamespace="http://brejaonline.com.br/pessoa/v1"
xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:tns="http://brejaonline.com.br/pessoa/v1"
xmlns:end="http://brejaonline.com.br/endereco/v1">
47

## Página 51

4.2. FerramentalXML:conhecendoosXML Schemas CasadoCódigo
<!-- restante -->
</schema>
Opróximopassoéinformaraomecanismoalocalizaçãodo outro XML Schema,
atravésda t ag import:
<?xml version="1.0" encoding="UTF-8"?>
<schema targetNamespace="http://brejaonline.com.br/pessoa/v1"
xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:tns="http://brejaonline.com.br/pessoa/v1"
xmlns:end="http://brejaonline.com.br/endereco/v1">
<import namespace="http://brejaonline.com.br/endereco/v1"
schemaLocation="Endereco.xsd" />
<!-- restante -->
</schema>
Assim,parautilizaros tiposdefinidosnonovo arquivo,bastautilizaroprefixo
end:
<complexType name="Pessoa">
<sequence>
<element name="endereco" type="end:Endereco" />
</sequence>
</complexType>
Ostiposcomplexostambémpodemdefinironúmerodeocorrênciasde seus
elementos.Porexemplo,paradeterminarqueumelementotemnúmeromínimode
ocorrênciaszero(ouseja,éopcional),utiliza-sea tag minOccurs:
<complexType name="Pessoa">
<sequence>
<element name="endereco" type="end:Endereco" minOccurs="0"/>
</sequence>
</complexType>
Damesmaforma,épossívelutilizara tag maxOccurs paradeterminaro nú-
meromáximodeocorrências(ouseja,queumdadoelementorepresentaumalista).
Onúmeromáximodeocorrênciaspodeserdelimitadoa partirdeumnúmerofixo
ou,casonãohaja umlimitedefinido,utiliza-seovalor unbounded. Assim,para
determinarqueumapessoapossuiváriosendereços,pode-seutilizaroseguinte:
48

## Página 52

CasadoCódigo Capítulo4. Tiposdedados
<complexType name="Pessoa">
<sequence>
<element name="endereco" type="end:Endereco" maxOccurs="unbounded"/>
</sequence>
</complexType>
Issoprovocaoseguinteresultado:
<pessoaFisica>
<endereco>
<cep>12345-678</cep>
<logradouro>Rua Um</logradouro>
</endereco>
<endereco>
<cep>87654-321</cep>
<logradouro>Rua Dois </logradouro>
</endereco>
</pessoaFisica>
Aeste ponto,vocêdeveternotadoqueoelementoraiz pessoaFisicanão
foiespecificado. Oelementoraizédefinido foradetiposemum XML Schema,
utilizandoa t ag element.Destaforma,épossívelteroseguinte:
<complexType name="PessoaFisica">
<!-- definição de pessoa física -->
</complexType>
<element name="pessoaFisica" type="tns:PessoaFisica" />
4.3 Trabalhando co m XML utilizando J A X B
AAPI(ApplicationProgrammer Interface)padrão paratrabalharcomXML,emJava,
éoJAXB (J a v aArchitecture for XML Binding). EstaAPItrabalhaessencialmente
comanotações sobreclassesJava,quedãoinstruções arespeitodecomoconverter
osdadosemXMLatravés dageraçãode XML Schemas.
Paratransformarum XML Schema emclassesJavacompatíveiscomJAXB,
existe umutilitáriopresentena JDKchamado xjc. Supondoqueseus XML
Schemas estejamestruturadoscomoMaven, ouseja, presentesemuma pasta
src/main/resources,épossívelcolocarestas classesnapastacertausandooar-
gumento -d:
49

## Página 53

4.3.TrabalhandocomXMLutilizandoJAXB CasadoCódigo
xjc -d ../java Pessoa.xsd
Oquedeveproduzirumaestruturacomoaseguinte:
Figura4.1:Arquivosgerados peloxjc
Como vocêpode observar, umaclasse para cada tipo complexo presente
nos XML Schemas foigerada, alémdasclasses ObjectFactory eo arquivo
package-info.java.Eles atuam,respectivamente,comouma classefábricapara
objetosrecém-criados(ouseja,seráutilizadonomomentodatraduçãoXML->Java)
ecomoum mecanismodefornecimentodeinformaç ões válidasparatodoopacote.
50

## Página 54

CasadoCódigo Capítulo4. Tiposdedados
O arquivo package-info.j a v a
EstearquivoépadronizadopelaespecificaçãoJava(ouseja,nãoédefi-
nidopelaespecificaçãoJAXB). Elecontémapenasadeclaraçãode nome
dopacote,compossíveis anotações. NocasodoJAXB,este arquivoé
geradocoma anotação @XMLSchema,quetrazinformações queserão
válidasparatodasasclassesdopacote,comoo namespacequeseráapli-
cado.
V a m o sanalisarasclassesgeradas:
A classe PessoaFisica
Aclasse PessoaFisicadevetersidogeradacomoseguintecódigo:
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "PessoaFisica", propOrder = {
"cpf"
})
public class PessoaFisica
extends Pessoa
{
@XmlElement(required = true)
protected String cpf;
// getter e setter para cpf
}
Aanotação @XMLAcessorTypeindicaparaoJAXB qualomecanismoaser
utilizadopararealizaratraduç ãodosdados paraXML.Comoa enginedoJAXB
utilizaaAPIde reflectionspararealizareste mapeamento,oacessoaosdados pode
serfeitotantodiretamentepelovalordos atributospresentesnaclasse(sejamestes
privadosounão)como por getterse setters.
AAPIdisponibiliza quatroformasdistintasdeacesso:
•Porcampos:mapeiatodososatributosdeclasse,independentedesuavisibili-
dadeedeestaremanotadoscom anotações doJAXB.Casonãoestejammape-
adoscomnenhumainformaç ãoarespeitodenomenclatura,serãomapeados
51

## Página 55

4.3.TrabalhandocomXMLutilizandoJAXB CasadoCódigo
como nomedoprópriocampo.Ficamexcluídosdesta apenasatributosestá-
ticosouquesejamdefinidoscomo transient;
•Porpropriedades: aenginedetecta getterse settersemapeiatodosos pares
encontrados;
•Pormembrospúblicos:mapeiatodasos getterse settersquetenhamvisibili-
dadeajustadapara publicetambémtodosos atributosdeclassepúblicos.
Esteéopadrão, quandonenhumdos outrostiposédefinido;
• Nenhum:mapeiaapenasosmembros queestejamanotadoscom anotações
doJAXB.
Aanotação XmlTypeéutilizadanomomentodaconversãodasclassesem XML
Schemas.Elafazmençãodiretaao usodetiposcomplexosem XML Schemas,e
éutilizada,nestecontexto,paradescrevero nomedotipocomplexoeaordem das
propriedades(quedevem,obrigatoriamente,estarpresentes naclasse).
Aanotação XmlElementéutilizadaparadeclararapropriedadecomoelemento
(queéocomportamentopadrão)e outraspropriedadesarespeitodoelemento,como
aobrigatoriedadede seterconteúdo,onomedoelemento,valorpadrão,etc. Neste
caso,comooelemento cpfnãotevedeclaradoonúmeromínimodeocorrências
comozero, foiassumidoovalorpadrão,um. Assim,oJAXBentendeoelemento
comoobrigatório.
A classe Pessoa
Aclasse Pessoadeveteroseguintecódigo:
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "Pessoa", propOrder = {
"nome",
"endereco"
})
@XmlSeeAlso({
PessoaFisica.class
})
public abstract class Pessoa {
@XmlElement(required = true)
protected String nome;
52

## Página 56

CasadoCódigo Capítulo4. Tiposdedados
protected List<Endereco> endereco;
@XmlAttribute(name = "id")
protected Long id;
// getters e setters
}
Comovocêpodenotar,aclasse Pessoaéabstrata.Istoédevidoaofatodeo tipo
complexotersidodeclaradotambémcomoabstrato,easduascoisassãoequivalentes
emcadacontexto(isto é,umaclasseabstratanãopoderserinstanciada,emJava,e
umtipocomplexonãopoderserdiretamenteutilizadoemXML).
Sendouma classeabstrata,oJAXB precisasaberquaissãosuassubclassespara
quea enginetenhacondições defazero mapeamentoXML->Javaadequadamente.
ComopróprialinguagemJavanãopermitetaldetecção,entraemcenaa anotação
@XmlSeeAlso,queindicaparaa engineJAXBquaisclassesestãorelacionadasaesta
(nocaso,aclasse PessoaFisica,vistaanteriormente).
Outraanotaçãonovaé @XmlAttribute.Estaanotaçãoindica queoatributo
daclasseémapeadocomoumatributoXML,enãocomoelemento(comportamento
padrão).
Alémdisso,noteapresen çadoatributo endereco,quefoidefinidocomouma
lista. Estecomportamentoédevidoaofatode queoelemento endereco,decla-
radocomnúmeromínimodeocorrênciasigualazeroe semlimitesuperior-o que,
automaticamente,caracterizaoelementocomoumalista.
Alémdisso,notequeaclasse Enderecoestásendoutilizada,masnãodeclarada
naanotação @XmlSeeAlso. Istoédevidoaofatode que,comoesta classejáé
referenciadapeloprópriocódigo(ouseja, nadeclaração List<Endereco>),nãoé
necessáriorealizaradeclaraçãonaanotação.
O arquivo package-info.java
Oarquivo package-info.javadevetersidogeradocomoseguintecon-
teúdo:
@javax.xml.bind.annotation.XmlSchema
(namespace = "http://brejaonline.com.br/pessoa/v1",
elementFormDefault = javax.xml.bind.annotation.XmlNsForm.QUALIFIED)
package br.com.brejaonline.pessoa.v1;
53

## Página 57

4.4. TestandooXMLgerado CasadoCódigo
Noteque,conformeexplicado anteriormente,apenasadeclaraçãodo nomedo
pacoteépermitida nestearquivo.Assim,a anotação @XmlSchemacontémdados
quesãocomunsatodasasclassesdopacote, ouseja,adeclaraç ãodo namespaceeo
formatodosdados, queéqualificado.
XML qualificado versusXML n ã o -qualificado
QuandodizemosqueumXMLéqualificado, nosreferimosao for-
matofinalcomqueeleseráformado.EmumXMLqualificado,todosos
elementosdevemmencionara qual namespacepertencem,porexemplo:
<pes:pessoaFisica xmlns:pes="http://brejaonline.com.br/pessoa/v1">
<pes:cpf>123.456.789-09</pes:cpf>
</pes:pessoaFisica>
Noteapresen çadoprefixo pesnoatributo cpf.SeoXMLnãofosse
qualificado,elepoderiaserescritodaseguintemaneira:
<pes:pessoaFisica xmlns:pes="http://brejaonline.com.br/pessoa/v1">
<cpf>123.456.789-09</cpf>
</pes:pessoaFisica>
Nestecaso,ofatode não serqualificadoimplica, automaticamente,
queo namespacedoelemento cpféigualaode pessoaFisica,ou
seja, http://brejaonline.com.br/pessoa/v1.
ÉsempreumaboapráticautilizarXML’squalificados.
4.4 Testando o XML gerado
ParatestaroformatodosdadosqueseráproduzidopeloJAXB,existeuma classeuti-
litáriachamada javax.xml.bind.JAXB.Elatemmétodospararealizar marshal
(ouseja,transformaçãodasclassesJavaemXML)e unmarshal(ouseja,transforma-
çãodeXMLemJava).
Alerta sobre a classe j a v a x.xml. bind.JAXB
Comopodeserconferidonaprópriadocumentaçãodesta classe,esta
deveserutilizadaapenasparatestes,nãoparaprodução.
54

## Página 58

CasadoCódigo Capítulo4. Tiposdedados
Pararealizaroteste,bastainstanciarumobjetodeumaclasseanotadacomJAXB
eutilizarométodo marshal,passandoesteobjetoeuma s t re amcomoparâmetros.
Porexemplo,paramostraroresultado noconsole,bastautilizaroseguintecódigo:
public static void main(String[] args) {
PessoaFisica pessoaFisica = new PessoaFisica();
pessoaFisica.setCpf("12345678909");
pessoaFisica.setNome("Alexandre Saudate");
Endereco endereco = new Endereco();
endereco.setCep("12345-678");
pessoaFisica.getEndereco().add(endereco);
JAXB.marshal(pessoaFisica, System.out);
}
Deacordocomocódigoacima,oseguintedeve serapresentado:
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<pessoaFisica xmlns:ns2="http://brejaonline.com.br/endereco/v1"
xmlns:ns3="http://brejaonline.com.br/pessoa/v1">
<ns3:nome>Alexandre Saudate</ns3:nome>
<ns3:endereco>
<ns2:cep>12345-678</ns2:cep>
</ns3:endereco>
<ns3:cpf>12345678909</ns3:cpf>
</pessoaFisica>
4.5 Utilizando J A X Bs e m u m XML Schema
Muitasvezes,vocêpodeconsiderardesnecessárioutilizarum XML Schema,ou
muitotrabalhosogerarum.Nestescasos,épossível trabalharcomJAXB semutili-
zar XML Schemas.Paraisto,bastagerarasclassesaseremutilizadas normalmente
eutilizara anotação javax.xml.bind.annotation.XmlRootElement.
Nestecaso,podemosrefatorara classe PessoaFisica,porexemplo,paraser
araiz,erefatoramos todaaestrutura pararemoverosarquivos própriosdoJAXB
(ouseja, asclasses ObjectFactorye package-info). Aestrutura,então,fica
noseguinteformato:
Asclassestambémforamrefatoradas,paraficarcomoseguinte formato:
55

## Página 59

4.5. UtilizandoJAXBsemumXML Schema CasadoCódigo
@XmlRootElement
public class PessoaFisica
extends Pessoa
{
private String cpf;
// getters e setters
}
Adefiniçãode Pessoa:
@XmlSeeAlso({
PessoaFisica.class
})
public abstract class Pessoa {
private String nome;
private List<Endereco> endereco;
private Long id;
@XmlAttribute(name = "id")
public Long getId() {
return id;
}
// getters e setters
}
Ea classequeirámodelaroendere ço:
public class Endereco {
private String cep;
private String logradouro;
}
Oresultadodo testeficasemelhanteaoanterior:
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<pessoaFisica id="1">
56

## Página 60

CasadoCódigo Capítulo4. Tiposdedados
<endereco>
<cep>12345-678</cep>
</endereco>
<nome>Alexandre Saudate</nome>
<cpf>12345678909</cpf>
</pessoaFisica>
4.6 JSON
JSONéumasigla para JavaScript Object Notation. Éumalinguagemde marcação
criadaporDouglasCrockfordedescritonaRFC4627,e servecomoumacontrapar-
tidaaXML. T e mporprincipalmotivaçãoo tamanhoreduzidoemrelaçãoaXML,e
acabatendo usomaispropícioemcenáriosondelargurade banda(ouseja, quanti-
dadededados quepodesertransmitidaemumdeterminadointervalodetempo)é
umrecursocrítico.
Atendeaoseguintemodelo:
•U mobjetocontémzerooumaismembros
•U mmembrocontémzerooumaisparesezero oumaismembros
•U mparcontémumachaveeumvalor
•U mmembrotambémpodeserum a r r a y
Oformatodestadefiniçãoéoseguinte:
{"nome do objeto" : {
"nome do par" : "valor do par"
}
}
Porexemplo,apessoafísicapodeserdefinidadaseguintemaneira:
{"pessoaFisica" : {
"nome" : "Alexandre",
"cpf" : "123.456.789-09"
}
}
Casosejaumalistagem,o formatoéoseguinte:
57

## Página 61

4.7.TrabalhandocomJSONutilizandoJAXB CasadoCódigo
{"nome do objeto" : [
{"nome do elemento" : "valor"},
{"nome do elemento" : "valor"}
]
}
Novamente,apessoafísicapodeserdefinidadaseguintemaneira:
{"pessoaFisica" : {
"nome" : "Alexandre",
[
"endereco" : {
"cep" : "12345-678",
"logradouro" : "Rua Um"
}
],
"cpf" : "123.456.789-09"
}
}
Notequeasquebrasdelinhaeosespaços nãosãoobrigatórios-servem apenas
comoelementosparafacilitaravisualizaç ão.
T a m b é mvalea penadestacarqueadeclaraçãodoelementoraiz(comoade-
claração pessoaFisica)éestritamenteopcional. Muitas enginessãocapazesde
trabalharcomapenasosatributosdoelemento. Porexemplo,adefiniçãode pessoa
físicapoderiaficardaseguinteforma:
{
"nome" : "Alexandre",
[
{
"cep" : "12345-678",
"logradouro" : "Rua Um"
}
]
"cpf" : "123.456.789-09"
}
4.7 Trabalhando co m JSON utilizando J A X B
Existemdiversasimplementações de parsersJSONparaJava.Algumasdelas sãoas
seguintes:
58

## Página 62

CasadoCódigo Capítulo4. Tiposdedados
• GSON
• Jackson
•Jettison
•XStream
Amaneirade usodecadaumatemvantagensedesvantagens. U m avantagem
bastanteinteressantedealgumaséacapacidadedeutilizar anotações JAXBcomo
instruções parageraçãodoJSON,gerando apenasumúnicoesfor çoquandoque-
remostrabalhartantocomJSON quantocomXML. Parademonstraro usodes-
tasferramentas,adicionei maisumcamponaclasse
PessoaFisica,chamado
dadoTransiente.Estecampofoianotadocom @XmlTransient,indicandoque
estedado nãodeveserapresentadoquandoo parserutilizarasanotações doJAXB,
destaforma:
@XmlRootElement
public class PessoaFisica extends Pessoa {
private String cpf;
private String dadoTransiente = "dadoTransiente";
@XmlTransient
public String getDadoTransiente() {
return dadoTransiente;
}
//getter e setters restantes
}
VejamosocódigocomGSON. Paratransformarumainstânciadesta classeem
JSONcomGSON,ocódigoaseguiréutilizado:
PessoaFisica pessoaFisica = Parser.criarPessoaFisicaTeste();
Gson gson = new Gson();
System.out.println(gson.toJson(pessoaFisica));
Oqueproduzoseguinteresultado(formatado pormimparaoferecermelhor
legibilidade):
59

## Página 63

4.7.TrabalhandocomJSONutilizandoJAXB CasadoCódigo
{"cpf":"123.456.789-09",
"dadoTransiente":"dadoTransiente",
"nome":"Alexandre",
"endereco":[{"cep":"12345-678","logradouro":"Rua Um"}],
"id":1
}
Comoobservado,éfácilgeraroconteúdoJSONutilizandoGSON; noentanto,
ainformaçãotransienteestápresente noJSONgerado,ouseja,oGSON nãooferece
suporteàsanotações JAXB.
JáocódigocomJacksonfica daseguinteforma:
PessoaFisica pessoaFisica = Parser.criarPessoaFisicaTeste();
ObjectMapper objectMapper = new ObjectMapper();
AnnotationIntrospector annotationIntrospector = new JaxbAnnotationIntrospector();
objectMapper.setAnnotationIntrospector(annotationIntrospector);
System.out.println(objectMapper.writeValueAsString(pessoaFisica));
Oqueproduzoseguinteresultado:
{"nome":"Alexandre",
"endereco":[{"cep":"12345-678","logradouro":"Rua Um"}],
"id":1,
"cpf":"123.456.789-09"
}
Destaforma,ainformaçãotransiente foidetectadaeretiradadoJSON. Noen-
tanto,ocódigoestádemasiadocomplicado.
Vejamosocódigonecessário paraavaliarestainformaçãocomJettison:
PessoaFisica pessoaFisica = Parser.criarPessoaFisicaTeste();
JAXBContext context = JAXBContext.newInstance(PessoaFisica.class);
MappedNamespaceConvention con = new MappedNamespaceConvention();
Writer writer = new OutputStreamWriter(System.out);
XMLStreamWriter xmlStreamWriter = new MappedXMLStreamWriter(con, writer);
Marshaller marshaller = context.createMarshaller();
marshaller.marshal(pessoaFisica, xmlStreamWriter);
O código utilizadopeloJettisonéaindamaiscomplicado. Noentanto,ele
possuiumaafinidade maiorcomoJAXB(comoobservado pelousodasclasses
JAXBContexte Marshaller,quesãoprópriasdaAPIdoJAXB). Istoérefletido
noresultadodaexecuçãodestecódigo:
60

## Página 64

CasadoCódigo Capítulo4. Tiposdedados
{"pessoaFisica":
{"@id":"1",
"endereco":{"cep":"12345-678","logradouro":"Rua Um"},
"nome":"Alexandre",
"cpf":"123.456.789-09"
}
}
Notequeo JSON gerado émaissemelhantea um XML.Estápresente um
elemento-raiz, pessoaFisica,eo atributo idfoidestacadoatravésdoprefixo
@,indicando queesteéequivalenteaum atributoXML.
Finalmente,vejamosocódigoutilizado peloXStream:
PessoaFisica pessoaFisica = Parser.criarPessoaFisicaTeste();
XStream xStream = new XStream(new JettisonMappedXmlDriver());
System.out.println(xStream.toXML(pessoaFisica));
Aqui,noteoseguinte:o d r i v e rutilizadopeloXStreamparageraçãodoJSONéo
doJettison, ouseja,o XStreamreutilizaoutro fr a mewo r kparageraçãodoJSON.O
resultado,noentanto,éradicalmentediferente:
{"br.com.brejaonline.modelo.pessoa.PessoaFisica":
{"nome":"Alexandre",
"endereco":[
{"br.com.brejaonline.modelo.pessoa.Endereco":
{
"cep":"12345-678","logradouro":"Rua Um"
}
}
],
"id":1,
"cpf":"123.456.789-09",
"dadoTransiente":"dadoTransiente"
}
}
NotequeoXStream,porpadrão,colocaos nomesdasclassesutilizadasnatradu-
çãoe nãorespeitaasanotações doJAXB.T o d aestainformaçãopodesercontrolada,
mascomcódigoe anotações própriasdoXStream.
61

## Página 65

4.8. ValidaçãodeJSONcomJSON Schema CasadoCódigo
4.8 Validação de JSON co m JSON Schema
AssimcomoemXML,JSON tambémpossuiumsistemadevalidaç ão,conhecido
como JSON Schema.Trata-sedeum tipodearquivoque,como XML Schemas,
tambémpossuium formatopróprioparaespecificaçãode tiposJSON.Essaespeci-
ficaçãoestádisponívelnoseu site,
U mJSON Schema possuicomodeclaraç ãomaiselementaro título(descrito
no JSON Schema comoumapropriedade title).O títuloéoquedenominaeste
arquivodevalida ção.Porexemplo,supondoquedesejamoscome çaradescreverum
JSON Schema parapessoas,odescritivoteráoseguinte formato:
{
"title":"Pessoa"
}
Nasequência,énecessáriodefinir,paraesteformato,o tipo(descritono JSON
Schemacomoumapropridade type).O tipopodeserumdosseguintes:
•array-ouseja,umalistadedados
•boolean-ouseja,umvalor booleano(trueou false)
•integer-umnúmerointeiroqualquer. NotequeJSONnãodefineumnúmero
de b i t spossível,apenasofatode serumnúmeropertencenteaoconjuntodos
númerointeiros.
•number-umnúmeropertencenteaoconjuntodosnúmeros reais. Seguea
mesmaregrade integer,sendoque n u m b e rtambémcontempla integers
•null-umvalor nulo
•object-ouseja,umelemento quecontémumconjuntodepropriedades
•string-ouseja,umacadeiadecaracteres
Comopessoaéumobjeto,podemosdefiniro tipodaseguinteforma:
{
"title":"Pessoa",
"type":"object"
}
62

## Página 66

CasadoCódigo Capítulo4. Tiposdedados
Obviamente,umobjetoprecisaconterpropriedades. Estaspodemserdefini-
dasapartirdaproprieade properties. Porexemplo,sequisermosdefiniruma
propriedade nomeparaumapessoa,podemosutilizaroseguinte formato:
{
"title":"Pessoa",
"type":"object",
"properties":{
"nome": {
"type":"string"
}
}
}
Noteque,definidaapropriedade nome,oconteúdodeste passaateromesmo
formatodaraiz pessoa,ouseja,existeumarecursividade.Épossível, portanto,de-
finirum atributo titledentrode nome,definirnomecomoum objetocomsub-
propriedades,etc.
Assimsendo,podemos, portanto,definirumelemento enderecodentrode
pessoa,quetambémseráumobjeto.Dessaforma,temos:
{
"title":"Pessoa",
"type":"object",
"properties":{
"nome": {
"type":"string"
},
"endereco":{
"type":"object",
"properties":{
"cep":{
"type":"string"
},
"logradouro":{
"type":"string"
}
}
}
}
}
63

## Página 67

4.8. ValidaçãodeJSONcomJSON Schema CasadoCódigo
Finalmente,valea penaobservarque,porpadrão,o JSON Schema nãotelimita
aosformatospré-defidos(aocontráriodo XML Schema,queapenasseatémao
definido).Porexemplo,deacordocomo JSON Schema acima,oseguinteJSON
seriaconsideradoválido:
{
"nome":"Alexandre",
"cpf":"123.456.789-09"
}
Noteque,aindaqueocampo cpfnãoestejadescrito,apresen çadomesmonão
invalidaoJSON, tornandooscamposmeramentedescritivos(ouseja,encarados
como“esperados”).Casoestecomportamentonãosejadesejável,épossíveldefiniro
atributo additionalProperties(queédotipobooleano)como false,assim:
{
"title":"Pessoa",
"type":"object",
"additionalProperties":false,
"properties":{
"nome": {
"type":"string"
},
"endereco":{
"type":"object",
"additionalProperties":false,
"properties":{
"cep":{
"type":"string"
},
"logradouro":{
"type":"string"
}
}
}
}
}
Destaforma,oJSONdescrito seriaconsideradoinválido.
Para realizar ostestes de validação JSON, é possível utilizar o programa
disponívelem https://github.com/fge/json-schema-validator,ouainda, utilizara
64

## Página 68

CasadoCódigo Capítulo4. Tiposdedados
plataforma onlinedeste, disponívelatéa data daescrita deste livro emhttp://
json-schema-validator.herokuapp.com/.
Paragerarcódigoa partirdeste JSON Schema, épossívelutilizarum pro-
gramadisponívelem https://github.com/joelittlejohn/jsonschema2pojo.Estepro-
gramaestádisponível,atéadatadeescritadestelivro, sobosformatos online(em
http://www.jsonschema2pojo.org/),como pluginMaven,como pluginGradle,como
tarefaAnt,comoumprogramadelinhadecomando oucomumaAPIJava.
Sepreferir,podeconfigurarnoMavencomaseguinteinstruç ão:
<build>
<plugins>
<plugin>
<groupId>com.googlecode.jsonschema2pojo</groupId>
<artifactId>jsonschema2pojo-maven-plugin</artifactId>
<version>0.3.7</version>
<configuration>
<sourceDirectory>${basedir}/src/main/resources/schema</sourceDirector
<outputDirectory>${basedir}/src/main/java</outputDirectory>
</configuration>
<executions>
<execution>
<goals>
<goal>generate</goal>
</goals>
</execution>
</executions>
</plugin>
</plugins>
</build>
Além disso,tambémépreciso configurar dependências com os artefatos
common-lange jackson-databind,queserãoutilizados nasclassesgeradas.
OXMLutilizado pormimparaconfiguraçãodestasdependênciasfoi:
<dependency>
<groupId>commons-lang</groupId>
<artifactId>commons-lang</artifactId>
<version>2.4</version>
</dependency>
<dependency>
<groupId>com.fasterxml.jackson.core</groupId>
65

## Página 69

4.9. Conclusão CasadoCódigo
<artifactId>jackson-databind</artifactId>
<version>2.0.0</version>
</dependency>
Destaforma,bastaexecutarocomando mvn generate-sources paraqueas
classes Pessoa(cujonomeégeradoa partirdonomedoarquivo-nomeu caso,
Pessoa.json)e Endereco(nomedefinidoapartirdapropriedade endereco).
Figura4.2: Classesgeradaspeloplugindo MavenparaJSONSchema
4.9 Conclusão
Nestaseção,vocêconheceumaisarespeitodos formatosmaisutilizadosemREST,
ouseja,XMLeJSON. V o c êconheceumaisarespeitodoecossistema queoscerca,ou
seja,nocasodoXML, XML Schemas eJAXB.NocasodeJSON,os JSON Schemas
easferramentashabilitadasatrabalharemcomeste formato.
66

## Página 70

CasadoCódigo Capítulo4. Tiposdedados
Destemomentoemdiante,vocêjátememmãososmeios queserãoutilizados
paraconstruçãode serviçosREST,ouseja,vocêjáconheceosprincípiosdeRESTe
jásabeutilizaros tiposdedadosdisponíveis parautilizaçãodeste. Masaindafaltao
primordial:comocombinartudo isso?
Nopróximocapítulo,vocêverácomocombinaressatécnicaatravésdautilização
de servletsJava.Maisadiante,vocêverácomoutilizarAPI’saindamelhores.V a m o s
emfrente?
67

## Página 72

Capítulo5
ImplementandoserviçosRESTem
J a v acomServlets
“ Oú n i c ohomem q u enão erra éaquele q u enunca f e znada”
–FranklinRoosevelt
Agoraquevocêjáconheceosconceitos ondeRESTestáenvolvido,estánahora
devercomoimplementar istoemumsistema real.Comojáépraxe,voucomeçar
pelaformamaissimplese,depois,partiremos paraaimplementaçãousandoAPI’s
própriasparaconstruçãode serviçosREST.
5.1 Uma implementação co m Servlets
OleitorquejátemexperiênciacomservletsJavaprovavelmentejáimaginou,atéaqui,
umaimplementaçãocomestatecnologia.Mesmo seforesteoseucaso,leiaestaseção
atéofim- podetetrazerinformações úteismesmoarespeitodofuncionamentodo
mecanismodaAPIRESTdeJava.

## Página 73

5.1.UmaimplementaçãocomServlets CasadoCódigo
Senãoforocaso,saibaqueaespecificaçãoJavaEEpossuidefinidao usode ser-
vlets,ouseja,trechosdecódigoespecíficos paraseremexecutados noladodoservi-
dor.Os servletssão,pornatureza,construídosparaatenderemaqualquerprotocolo
deaplicação quesejatransmitidopelarede;noentanto,existeumaextensãodes-
tesparatrabalharespecificamentecomoprotocoloHTTP, queéjustamenteoque
precisamos.
Estaextensãoéaclasse javax.servlet.http.HttpServlet,quepossuios
métodosconhecidoscomo doXXX(ondeXXXéonomedeummétodoHTTP). Por
exemplo,paraatenderaumarequisiç ãoqueuseométodo GET,pode-seestendera
classe HttpServleteimplementarométodo doGet,assim:
package br.com.brejaonline.servlets;
import javax.servlet.http.*;
public class CervejaServlet extends HttpServlet {
public void doGet (HttpServletRequest req , HttpServletResponse resp)
throws ServletException, java.io.IOException {
// Coloque aqui a implementação do seu código
}
}
Estemétodovaicarregar,então,aimplementaç ãodo quesedesejaparaumser-
viçoREST.Lembre-sede queométodo GETéutilizadopararealizarbuscasnolado
doservidor.Sendoesteum servletquebuscadadosdecervejas,deve-seimplementá-
lodemaneiraarealizarestaaç ão.
V a m o sutilizar,aqui,umconceitopresenteem Domain-Driven Design,queéode
repositório:uma classedenegócioespecializada noarmazenamentodeentidades
denegócio.
70

## Página 74

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
O que é Domain-D riven Design
Domain-Driven Designsignifica,numatraduçãolivre, designorien-
tadoaodomínio. Istoquerdizer, numasimplificaçãogrosseira, queas
classesquevocêconstruirdevem sempreatenderaomáximopossível
objetivosdenegócio-o quepodesertraduzido,porexemplo,eminser-
çãodecomportamentodenegócio nasentidadesqueserãopersistidas
nobancodedados,o quetrazganhosemtermosdecoesãodosobjetos.
Parasabermais,sugirolerolivrodeEricEvans,Domain-DrivenDesign
-AtacandoAsComplexidadesnaCriaçãodo Software.
V a m o scomeçar,então,peladefiniçãodaentidadequedesejamosbuscar,ouseja,
umacerveja:
package br.com.brejaonline.model;
public class Cerveja {
private String nome;
private String descricao;
private String cervejaria;
private Tipo tipo;
public enum Tipo {
LAGER, PILSEN, PALE_ALE, INDIAN_PALE_ALE, WEIZEN;
}
}
Aseguir,vamosrealizaradefiniç ãodo nossorepositóriodecervejas(ouseja,
umestoquedecervejas):
package br.com.brejaonline.model;
import java.util.*;
public class Estoque {
private Collection<Cerveja> cervejas = new ArrayList<>();
71

## Página 75

5.1.UmaimplementaçãocomServlets CasadoCódigo
public Collection<Cerveja> listarCervejas() {
return new ArrayList<>(this.cervejas);
}
public void adicionarCerveja (Cerveja cerveja ) {
this.cervejas.add(cerveja);
}
}
V a m o sincrementaronossoestoqueparacomeçarcomalgumascervejas(afinal
decontas,ninguém gostadeumestoquevazio:) ). Paraisso,vamosmodificara
classe Cervejaparacriarum construtorparaarmazenarosparâmetros e,depois,
modificaroconstrutordeestoqueparacriarestascervejas.Então,a classe Cerveja
ficaassim:
public class Cerveja {
private String nome;
private String descricao;
private String cervejaria;
private Tipo tipo;
public Cerveja(String nome, String descricao, String cervejaria, Tipo tipo) {
this.nome = nome;
this.descricao = descricao;
this.cervejaria = cervejaria;
this.tipo = tipo;
}
// restante do código
}
Ea classe Estoqueficaassim:
public class Estoque {
private Collection<Cerveja> cervejas = new ArrayList<>();
public Estoque() {
Cerveja primeiraCerveja = new Cerveja("Stella Artois",
"A cerveja belga mais francesa do mundo :)",
72

## Página 76

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
"Artois",
Cerveja.Tipo.LAGER);
Cerveja segundaCerveja = new Cerveja("Erdinger Weissbier",
"Cerveja de trigo alemã",
"Erdinger Weissbräu",
Cerveja.Tipo.WEIZEN);
this.cervejas.add(primeiraCerveja);
this.cervejas.add(segundaCerveja);
}
//restante do código
}
Assim,utilizamosa classe Estoquenonosso servletdecervejas,ficandoassim:
public class CervejaServlet extends HttpServlet {
private Estoque estoque = new Estoque();
public void doGet (HttpServletRequest req , HttpServletResponse resp)
throws ServletException, java.io.IOException {
// Coloque aqui a implementação do seu código
}
}
Ma seste exemplo n ã o segue o MVC...
Obviamente,esteexemplo não ébomnoquesito“acoplamento”. A
idéia,aqui,éapenasserdidático,enão mostrarumexemplo real. Os
exemplosreaiscompletoserefatoradosestarãodisponíveisalguns capí-
tulosadiante,aguarde.
Finalmente,parafacilitara nossavidanoquesitodescritividade dacerveja,va-
mossobreescreverométodo toStringdacerveja:
public class Cerveja {
// o código já mostrado anteriormente
public String toString() {
73

## Página 77

5.1.UmaimplementaçãocomServlets CasadoCódigo
return this.nome + " - " + this.descricao;
}
}
Agora,podemosutilizaresteconjuntodemecanismos paralistarnossascerve-
jasapartirdonosso servlet. Paraisso,vamosutilizaro mecanismodeimpressão
dos servlets,queéaobtençãodeum java.io.PrintWriterapartirdaclasse
javax.servlet.http.HttpServletResponse. Essaobtençãoéfeitaapartir
dométodo getWriter:
package br.com.brejaonline.servlets;
import javax.servlet.http.*;
import java.io.*;
import br.com.brejaonline.model.*;
public class CervejaServlet extends HttpServlet {
private Estoque estoque = new Estoque();
public void doGet (HttpServletRequest req, HttpServletResponse resp)
throws ServletException, java.io.IOException {
PrintWriter out = resp.getWriter();
Collection<Cerveja> cervejas = estoque.listarCervejas();
for (Cerveja cerveja : cervejas) {
out.print(cerveja);
}
}
}
Resta,agora,realizaro mapeamentodeste servletdemaneiraadequada. Se-
guindoospreceitosdeREST,oideal seriamapeá-loparaaURL /cervejaou
/cervejas,jáqueanossanecessidadeébuscarosdados dascervejaspresentes
nosistema.
Pela especificação 3.0 de servlets, é possível utilizar a anotação
javax.servlet.annotation.WebServlet para descrevê-los perante o
container,criandoo mapeamentoadequado.Portanto,nossaclassemapeadapode
ficardaseguinteforma:
// Declaração de package e imports
7 4

## Página 78

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
@WebServlet(value = "/cervejas/*")
public class CervejaServlet extends HttpServlet {
// código
}
Dicade uso
Casotenhadificuldadesemconferirofuncionamentodestecódigo,
bastairnorepositóriodecódigo-fontedolivroem https://github.com/
alesaudate/rest,baixarocódigoetestá-loem seuambiente.
Finalmente,paraconferirofuncionamentodocódigo, bastaabrircomo nave-
gadoroendere çohttp://localhost:8080/cap-05/cervejaria:
Noentanto,notequealgoestáerrado...paratestaroserviçodeumamaneira
maiscômoda,sugiroainstalaç ãodo plugin Poster,paraonavegador MozillaFi-
refox,disponívelem https://addons.mozilla.org/pt-br/firefox/addon/poster/.
Uso outro navegador, o que f a ç o ?
O plugintambémestádisponívelparaoGoogle Chrome,emhttp:
//tinyurl.com/chrome-poster.Nãosepreocupe,ousonosdoisnavega-
doresérealizadodamesmaforma.
U m avezinstaladoo pluginnoseuFirefox,bastaabrí-loapontandoparaomenu
Ferramentas(ou T o o l s,dependendodoidiomado seunavegador)eclicandoem
Poster:
75

## Página 79

5.1.UmaimplementaçãocomServlets CasadoCódigo
Figura5.1:Poster,umplugin paraoFirefox
Como Poster,temosumainterfacegráfica paratestarosnossos serviços!
76

## Página 80

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
Nacaixa URL,insiraaURLdo servletdecervejas,ouseja,http://localhost:8080/
cervejaria/cervejas.Nasequência,cliquenobotão GET.Oresultadodeve aparecer
demaneiraidênticaàmaneiracomo apareceunonavegador.
Porém,algonãoestácerto.Ocabeçalho Content-Typenãoestápresente,ou
seja,nemsequerexisteumadefiniç ãodo tipodedados.Alémdisso,oresultado foi
impressocomotextopuro-ouseja,ocliente nãoterámeiosparaidentificarostipos
dedadostrafegados,etc.
Ouseja,nossaprimeiramissãoé ajustarotipodedados. Pararepresentaros
dados,podemosutilizaros MIME T y p e stext/xmlou application/xmlpara
XMLe application/jsonparaJSON.V o c êviunocapítulo4comomanipular
estestipos.Assim, suponhaqueoretornodesejadodessalistagem sejaumconteúdo
XML.Duascoisassãonecessárias:criarumelemento-raiz paraoselementose re-
alizarasadaptações paratrafegarestesdados noformatodesejado. Paratermoso
menorimpactopossível, portanto,temoscomo opçãomaisfácilutilizaroJAXB:a
APIjávemembutidanasimplementações da V i r t u a lMachineJavaetambémoferece
compatibilidadecomcertosmecanismosgeradoresdeJSON.
Assim,vamoscriaruma classequeencapsuleasoutrascervejas,denominada
Cervejas. Estaclasseseráapartadadomodelo,e ficará localizadanopacote
br.com.brejaonline.model.rest.Teráoseguintecódigo:
//Declaração de pacote e imports
@XmlRootElement
public class Cervejas {
private List<Cerveja> cervejas = new ArrayList<>();
@XmlElement(name="cerveja")
public List<Cerveja> getCervejas() {
return cervejas;
}
public void setCervejas(List<Cerveja> cervejas) {
this.cervejas = cervejas;
}
}
Comovocêpodeobservar,éapenasumacápsulaparacervejas. Elatemdois
77

## Página 81

5.1.UmaimplementaçãocomServlets CasadoCódigo
motivosimportantesparaexistir:
•Elaseráusadaparaencapsularos outroselementos;
• Futuramente,utilizaremosessaclasseparaadicionarHATEOAS.
Agora,éhorademodificaraimplementaç ãodo nosso servletparaqueeleseja
capazdeatenderaosclientes. Paraqueissoaconteça,bastaimplementarnovamente
ométodo doGetnoservlet,comocódigodeescritadexml vistonocapítulo4:
//declaração de pacotes, imports e da classe
private static JAXBContext context;
static {
try {
context = JAXBContext.newInstance(Cervejas.class);
} catch (JAXBException e) {
throw new RuntimeException(e);
}
}
protected void doGet(HttpServletRequest req, HttpServletResponse resp)
throws ServletException, IOException {
try {
Marshaller marshaller = context.createMarshaller();
resp.setContentType("application/xml;charset=UTF-8");
PrintWriter out = resp.getWriter();
Cervejas cervejas = new Cervejas();
cervejas.setCervejas(new ArrayList<>(estoque.listarCervejas()));
marshaller.marshal(cervejas, out);
} catch (Exception e) {
resp.sendError(500, e.getMessage());
}
}
78

## Página 82

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
Prevenindo problemas
Nocódigoacima, notequeadefiniçãodo Content-Typeacom-
panhaadefiniçãodo charset. Casonão sejadefinido,ocontainer(no
meucaso,o Jetty)normalmenteselecionaumpré-definido.Observe
queaordemem queascoisassãofeitastambéminfluenciaestadefini-
ção- nocasodo Jetty,seesteajusteforfeito depoisdainvocaçãoa
resp.getWriter,ocontainervaiignoraradefiniç ãodo charset.
Observequea enginedoJAXBdepositaoXMLgeradodiretamente nasaída
oferecidapelaAPIde servlets. Paratestarestecódigo,recorremos novamenteao
Poster:
79

## Página 83

5.1.UmaimplementaçãocomServlets CasadoCódigo
Figura5.2:Enviandoumarequisiç ãode testecomoposter
Arespostaseráaseguinte:
80

## Página 84

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
Figura5.3:Resposta testeposter
5.2 Implementando negociação de conteúdo
Noexemploanterior,aURL /cervejasestáhabilitadaaenviarparaoclienteum
conteúdoapenasemformatoXML.Masoqueacontecesequisermosenviardados
81

## Página 85

5.2. Implementandonegociaçãodeconteúdo CasadoCódigo
deoutrasmaneiras? Digamosqueeuqueira enviardadoscomoJSON,também,o
quefaço?
AsaídanãoécriarnovasURL’s,massim,implementarumatécnicaconhecida
como negociação de conteúdo.Nestatécnica,oclientediz paraoservidor quetipo
dedadosdeseja(atravésdo cabeçalho Accept)e,então,oservidor produzotipo
deconteúdonoformatodesejado.
Paraimplementarnegociaçãodeconteúdocom servletsémuitofácil;bastain-
vocarométodo HttpServletRequest.getHeader,assim:
String acceptHeader = req.getHeader("Accept");
Apartirdeentão,é precisotestaroresultado.Lembre-se(deacordocomo ca-
pítulo2)queessanegociaçãopodeserpotencialmentecompliada. Paraevitarum
códigodemasiadamentecomplexo,vamos apenastrabalharcoma existênciaounão
deformatosesperadosnestecabeçalho.Assim,testamosprimeiro paraasolicitação
deXML. Casonãohaja XMLnarequisição,testamos paraJSONe,seotestefalhar,
devolvemosocódigodeerro 415(aindadeacordocomo capítulo2,significandoque
foisolicitadoum formatodedados quenãoésuportado).
Ocódigoficaassim:
if (acceptHeader == null || acceptHeader.contains("application/xml")) {
escreveXML(req, resp);
} else if (acceptHeader.contains("application/json")) {
escreveJSON(req, resp);
} else {
// O header accept foi recebido com um valor não suportado
resp.sendError(415); // Formato não suportado
}
Agora,restaescreverosmétodos escreveXMLe escreveJSON.Aestaaltura,
istonão devesernenhummistérioparavocê;maslistoabaixocasovocêaindatenha
dúvidasarespeito:
private void escreveXML(HttpServletRequest req, HttpServletResponse resp)
throws ServletException, IOException {
Cervejas cervejas = new Cervejas();
cervejas.setCervejas(new ArrayList<>(estoque.listarCervejas()));
try {
82

## Página 86

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
resp.setContentType("application/xml;charset=UTF-8");
Marshaller marshaller = context.createMarshaller();
marshaller.marshal(cervejas, resp.getWriter());
} catch (JAXBException e) {
resp.sendError(500); //Erro interno inesperado
}
}
//Este código assume o Jettison como provedor de mapeamento JSON
private void escreveJSON(HttpServletRequest req, HttpServletResponse resp )
throws ServletException, IOException {
Cervejas cervejas = new Cervejas();
cervejas.setCervejas(new ArrayList<>(estoque.listarCervejas()));
try {
resp.setContentType("application/json;charset=UTF-8");
MappedNamespaceConvention con = new MappedNamespaceConvention();
XMLStreamWriter xmlStreamWriter = new MappedXMLStreamWriter(con,
resp.getWriter());
Marshaller marshaller = context.createMarshaller();
marshaller.marshal(objetoAEscrever, xmlStreamWriter);
} catch (JAXBException e) {
resp.sendError(500);
}
}
5.3 Implementando a busca p o ru m a cerveja especí-
fica
A t éaqui,vocêjáviucomolistartodasascervejascadastradasnosistema.Mascomo
buscarumacervejaespecífica?
Pararesolverestaquestão,orecomendadoé modelaraURLdemaneira que,
83

## Página 87

5.3. Implementandoabuscaporumacervejaespecífica CasadoCódigo
se o cliente fornecer o IDda cerveja na URL, apenasuma única é retornada.
Porexemplo,seeu quiserbuscaraStellaArtois, possofazê-lo atravésdaURL
/cervejas/Stella+Artois(notequeestaURLjáestácodificadaparaserusada
emum browser).
Parafazerisso,noentanto,énecessáriorealizaralgumasmodificações,acome-
çarpelaclasse Estoque:estadeve sermodificadaparaencararosnomesdascerve-
jascomoidentificadores.Assim,substituímosaimplementaç ãodaclasse Estoque
paraarmazenarascervejasemum mapa,enãoemumalista:
private Map<String, Cerveja> cervejas = new HashMap<>();
public Collection<Cerveja> listarCervejas() {
return new ArrayList<>(this.cervejas.values());
}
public void adicionarCerveja (Cerveja cerveja) {
this.cervejas.put(cerveja.getNome(), cerveja);
}
Assim,podemosacrescentarummétodo nestaclassepararecuperarascervejas
pelonome:
public Cerveja recuperarCervejaPeloNome (String nome) {
return this.cervejas.get( nome);
}
Opróximo passoéincluirno servletummétodoparaextrairoidentificador(ou
seja,o nomedacerveja)daURLenviadapelocliente. Parafazerisso,precisamos
utilizarométodo HttpServletRequest.getRequestURI:
String requestUri = req.getRequestURI();
DepossedaURIinvocada,precisamosextrairoconteúdo queestádepoisda
últimabarra.MasestaURL podeterváriosformatos:
•/cervejas
•/cervejas/
•/cervejas/Stella
•/cervejas/Stella+Artois
84

## Página 88

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
Ouseja,precisamosdeummétodo quesejainteligenteosuficiente paraextrair
oquevemdepoisde /cervejas.Existemváriasmaneiradefazer isso;ométodo
criadopormimfoidividira stringpelosseparadores(ouseja, /)e,depois,iterar
pelalistade pedaçosatédetectarocontextodo servlet,ouseja, cervejas. U m a
vezlocalizadoocontexto, ajustaumavariávelbooleanaindicandoque,casohaja
qualquercoisanaURLdepoisdeste pedaço,éumidentificador.Ocódigoficaassim:
String[] pedacosDaUri = requestUri.split("/");
boolean contextoCervejasEncontrado = false;
for (String contexto : pedacosDaUri) {
if (contexto.equals("cervejas")) {
contextoCervejasEncontrado = true;
continue; //Faz o loop avançar até o próximo
}
if (contextoCervejasEncontrado) {
return contexto;
}
}
Noentanto,estecódigo sólevaemconsideraç ãoo casodoidentificadorexistir.
ParaocasodaURLestarcodificada, ouseja,estarcomo Stella+Artois(que,de-
codificado,representa Stella Artois),otratamento aindanãoestáimplemen-
tado.Masdecodificaréfácil,bastautilizara classe java.net.URLDecoder:
if (contextoCervejasEncontrado) {
try {
//Tenta decodificar usando o charset UTF-8
return URLDecoder.decode(contexto, "UTF-8");
} catch (UnsupportedEncodingException e) {
//Caso o charset não seja encontrado, faz o melhor esforço
return URLDecoder.decode(contexto);
}
}
Resta apenas o caso onde o identificador não existe. Para isso,
o mais elegante seria modelar uma exce ção própria, algo como
RecursoSemIdentificadorException.Ocódigofinalizadoficaassim:
private String obtemIdentificador(HttpServletRequest req)
throws RecursoSemIdentificadorException {
85

## Página 89

5.3. Implementandoabuscaporumacervejaespecífica CasadoCódigo
String requestUri = req.getRequestURI();
String[] pedacosDaUri = requestUri.split("/");
boolean contextoCervejasEncontrado = false;
for (String contexto : pedacosDaUri) {
if (contexto.equals("cervejas")) {
contextoCervejasEncontrado = true;
continue;
}
if (contextoCervejasEncontrado) {
try {
return URLDecoder.decode(contexto, "UTF-8");
} catch (UnsupportedEncodingException e) {
return URLDecoder.decode(contexto);
}
}
}
throw new RecursoSemIdentificadorException("Recurso sem identificador" );
}
Opróximo passoéalterarosmétodosde buscaparatrataremoenvio tantode
uma Cervejaquantodaclassequepodecontertodas,ouseja, Cervejas.Para
isso,bastacriarummétodopararealizaralocalizaç ão.Comoestasclassesnãopos-
suemparentescoentre elas,utilizamosa classe Objectcomoretornodométodo:
private Object localizaObjetoASerEnviado(HttpServletRequest req) {
Object objeto = null;
try {
String identificador = obtemIdentificador(req);
objeto = estoque.recuperarCervejaPeloNome(identificador);
}
catch (RecursoSemIdentificadorException e) {
Cervejas cervejas = new Cervejas();
cervejas.setCervejas(new ArrayList<>(estoque.listarCervejas()));
objeto = cervejas;
}
86

## Página 90

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
return objeto;
}
Finalmente,bastaalterarosmétodosdeescrita parautilizaremeste novomé-
todo.Observequeexisteumapossibilidadedo objetoretornadosernulo,ouseja,
casoumidentificador tenhasidofornecido masoobjetonãotenhasidolocalizado
noestoque.Assim,énecessárioretornaroerro404( Not Found)casooobjetoseja
nulo.OmétododeescritadeXMLeodeJSONserãosemelhantes:
private void escreveXML(HttpServletRequest req, HttpServletResponse resp)
throws ServletException, IOException {
Object objetoAEscrever = localizaObjetoASerEnviado(req);
if (objetoAEscrever == null) {
resp.sendError(404); //objeto não encontrado
return ;
}
try {
resp.setContentType("application/xml;charset=UTF-8");
Marshaller marshaller = context.createMarshaller();
marshaller.marshal(objetoAEscrever, resp.getWriter());
} catch (JAXBException e) {
resp.sendError(500);
}
}
Ma sé possível enviaru m Object para o J A X B?
Sevocêteveumadúvidaemrelaçãoaoenvio daclasseparaométodo
marshal,vocêestáindonocaminhocerto:). Naverdade,nestecaso
estamosconfiando semprequeoobjetoaserenviadoparaestemétodo
écompatívelcomJAXB,eestefaráadetecç ãoem t e m p ode execução,
enãoemtempodecompilação.Destaforma,podemospassarqualquer
objetoparaométodo marshale,casoestenão sejacompatível,uma
JAXBExceptionserálançada.
87

## Página 91

5.3. Implementandoabuscaporumacervejaespecífica CasadoCódigo
Agora,bastatestar.U s enovamenteo Poster,passandoaURL http://localhost:
8080/cervejaria/cervejas/Stella+Artois comoparâmetro.Oseguintedeverá serretor-
nado:
Figura5.4:Retornodotestedoservletdecervejas
88

## Página 92

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
5.4 Implementando a criação de u m recurso
Oseu servletjábuscarecursos,masseráqueestáaptoarealizaracriaç ãodestes?
Comovocêviuantes,tipicamenteascriações derecursos são feitasatravésda
utilizaçãodométodo POST.Sendoassim, vocêdeveapenasimplementarométodo
doPostno servlet:
protected void doPost(HttpServletRequest req, HttpServletResponse resp)
throws ServletException, IOException
Paracriaçãoderecursos, vocêtemduasopções demodelagem:fazercom queo
clientepasseumidentificador,jácriadoporele,oucriaroidentificador noladodo
servidor.Comonossaaplicaçãoédecervejas,fazsentidodeixarcom queocliente
crieoidentificador, jáqueosidentificadoresdascervejassãoosnomes.
Co m o acontece em aplicações reais?
NamaiorpartedasaplicaçõesREST,oservidorcriaosidentificadores,
especialmenteseo backenddaaplicaçãoestiverimplementadocomum
bancodedadosrelacionaleosID’ssãogeradosporestebanco.Masvocê
devetomaromáximocuidadopossívelcomesta abordagem,poissua
aplicaçãopodecrescereutilizar outrostiposdebancodedados.Oideal
équevocêsemprefaçaoprojetodasuaAPIdemaneira quevocêconsiga
modificarqualquerpartedasuainfra-estrutura.
Destaforma,aprimeiracoisa quevocêteráqueimplementaréarecuperaç ão
doidentificador(istodeve sertrivial,jáquevocêjátinhafeitoummétodoparaisto
quandocriouométododerecuperaç ãodecervejas). Casooidentificador nãoseja
encontrado,envieumerro 400 Bad Request paraocliente,indicandoqueare-
quisiçãodeve seralteradaere-enviada:
String identificador = null;
try {
identificador = obtemIdentificador(req);
} catch (RecursoSemIdentificadorException e) {
//Manda um erro 400
resp.sendError(400, e.getMessage());
}
89

## Página 93

5.4. Implementandoacriaçãodeum recurso CasadoCódigo
Opróximotratamentoa serrealizadoéparaocasoda cervejajáexistir;neste
caso,umerro 409 Conflictdeveserlançado:
if (identificador != null &&
estoque.recuperarCervejaPeloNome(identificador) != null) {
resp.sendError(409, "Já existe uma cerveja com esse nome" );
return ;
}
Finalmente,vocêdeverealizaraleituradocorpo darequisiçãoe transformarem
umobjeto Cerveja.Pararecuperarocorpo darequisição,bastaexecutarométodo
HttpServletRequest.getInputStream.Felizmente,o restantedoprocesso já
éfacilitadopeloJAXB:
Unmarshaller unmarshaller = context.createUnmarshaller();
Cerveja cerveja = (Cerveja)unmarshaller .unmarshal(req.getInputStream());
Opróximo passoégarantirqueacerveja tenhaomesmonomequeofornecido
peloidentificadore,então,adicioná-laaoestoque:
cerveja.setNome(identificador);
estoque.adicionarCerveja(cerveja);
T a m b é ménecessárioenviarparaoclienteocódigo201 Created,como cabeça-
lho Location,indicandoaURL ondeanovacervejaestádisponível.Comonosso
servletjárecebeaURLdevidamenteajustada, bastaajustaraURL darequisiçãono
cabeçalho Locationatravésdométodo HttpServletResponse.setHeader:
String requestURI = req.getRequestURI();
resp.setHeader("Location", requestURI);
resp.setStatus(201);
T a m b é méumaboapráticaenviardevoltaparaoclienteo recursocriado,jáque
algopodetersidoalteradonafasedecriaçãodo recurso.Esteprocessoserábastante
facilitadoatravésdousodométodo escreveXML,criadoanteriormente:
escreveXML(req, resp);
Ométodocompletoficaassim:
90

## Página 94

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
protected
void doPost(HttpServletRequest req, HttpServletResponse resp)
throws ServletException, IOException {
try {
String identificador = null;
try {
identificador = obtemIdentificador(req);
} catch (RecursoSemIdentificadorException e) {
resp.sendError(400, e.getMessage()); //Manda um erro 400 - Bad Request
}
if (identificador != null && estoque.recuperarCervejaPeloNome(identificador
resp.sendError(409, "Já existe uma cerveja com esse nome" );
return ;
}
Unmarshaller unmarshaller = context.createUnmarshaller();
Cerveja cerveja = (Cerveja)unmarshaller .unmarshal(req.getInputStream());
cerveja.setNome(identificador);
estoque.adicionarCerveja(cerveja);
String requestURI = req.getRequestURI();
resp.setHeader("Location", requestURI);
resp.setStatus(201);
escreveXML(req, resp);
}
catch (JAXBException e ) {
resp.sendError(500, e.getMessage());
}
}
Paratestarestemétodo,bastautilizaro Posternovamente,passandooXML
dacervejanocorpodarequisição:
91

## Página 95

5.4. Implementandoacriaçãodeum recurso CasadoCódigo
Figura5.5:Exemplodeutilizaç ãodoPoster paracriaçãodeum recurso
Casoométodotenhasidoimplementadocorretamente, algocomooseguinte
92

## Página 96

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
deveserretornado:
Figura5.6:Resultado dacriaçãodo recurso
Alémdisso,noteque,casoamesmarequisiçãosejasubmetidaumasegundavez,
ocódigo 409deveserretornado:
93

## Página 97

5.4. Implementandoacriaçãodeum recurso CasadoCódigo
Figura5.7:Respostadeerroindicando queorecursojáhaviasidocriado
94

## Página 98

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
5.5 Implementando negociação de conteúdo n a cri-
ação d orecurso
Paraimplementarnegociaçãodeconteúdo nacriaçãodo recurso,oclientedeve
ajustarocabeçalho Content-Typedemaneira queindiqueo tipodoconteúdo
presentenarequisição. Oservidordeverecuperaroconteúdodeste cabeçalhoe
trataresteconteúdo. Parafazerissocomnosso servlet,bastaexecutarométodo
HttpServletRequest.getContentType:
String tipoDeConteudo = req.getContentType();
Opróximo passoéumincluirum if/ else if/ else.Oprimeirovaifazero
testeseoconteúdoédotipoXML( text/xmlou application/xml);osegundo
vaitestarseoconteúdoédotipoJSON( application/json)eoterceirovai enviar
umerro,informando queotipodedado nãofoidetectado.
NocasodoconteúdoserXML,ocódigo jápreparadodeveserutilizado.Nocaso
deserJSON,vocêdeveutilizarumcódigo semelhanteaodeescrita. Noentanto,
paralerJSON,devemosrealizaraleituradocorpo darequisiçãomanualmente-o
modelodoJettisonnãocomportaaleituradeuma s t re am.Nestecaso,utilizamosa
classe org.apache.commons.io.IOUtilspararealizaraleitura daslinhasde
dadospresentesna s t re am:
List<String> lines = IOUtils.readLines(req.getInputStream());
StringBuilder builder = new StringBuilder();
for (String line : lines) {
builder.append(line);
}
95

## Página 99

5.5. Implementandonegociaçãodeconteúdo nacriaçãodo recurso CasadoCódigo
Meu p r o j e t on ã o tem a biblioteca d a Apache, o que
f a ç o ?
CasovocêutilizeoMaven, bastaadicionaradependência:
<dependency>
<groupId>commons-io</groupId>
<artifactId>commons-io</artifactId>
<version>2.4</version>
</dependency>
Senãoforseucaso,vocêtambémpodefazero downloaddestabibli-
otecanosite:http://commons.apache.org/proper/commons-io/
Nasequência,bastautilizarométododeleiturado Jettisonparatransformaro
JSONemum objeto Cerveja:
MappedNamespaceConvention con = new MappedNamespaceConvention();
JSONObject jsonObject = new JSONObject(builder.toString());
XMLStreamReader xmlStreamReader = new MappedXMLStreamReader(jsonObject, con);
Unmarshaller unmarshaller = context.createUnmarshaller();
Cerveja cerveja = (Cerveja)unmarshaller .unmarshal(xmlStreamReader);
Apartirdaqui,ométodo jáestápraticamentepronto.Basta,agora,repetiros
passosrealizadosparaleituradeXML(nãoesquecendodesubstituirométodofinal
por escreveJSON,aoinvésde escreveXML):
cerveja.setNome(identificador);
estoque.adicionarCerveja(cerveja);
String requestURI = req.getRequestURI();
resp.setHeader("Location", requestURI);
resp.setStatus(201);
escreveJSON(req, resp);
Paratestar,bastarepetiroprocedimento feitoanteriormente,mascomuma re-
quisiçãoJSON:
96

## Página 100

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
Figura5.8:RequisiçãoJSON
Seestivercorreto,oresultadodeve seroseguinte:
97

## Página 101

5.5. Implementandonegociaçãodeconteúdo nacriaçãodo recurso CasadoCódigo
Figura5.9:Resposta
Notequeorecursoestápresentenoservidorindependentedo seuconteúdo,
ouseja,searequisição for feitaumasegunda vezenão houvertipodeconteúdo
definido,seráretornadoumXML.
98

## Página 102

CasadoCódigo Capítulo5. ImplementandoserviçosRESTem JavacomServlets
5.6 Conclusão
V o c êviunestecapítulocomoimplementar serviçosRESTa partirde servletsJava.
Estesserviçosfazemapenasacriaçãoerecuperaç ãodeconteúdo(o restantesãoape-
nasvariações destesdoistipos).
Noentanto,vocêdeveternotado:édemasiadocomplexorealizaresteprocesso,
mesmoparaumrecursosimples. V o c êdeveestar seperguntando: existealguma
maneira,maissimples,derealizaresteproceso?Sim, há!
Nospróximoscapítulos,vocêverácomoutilizaraespecificaçãoJavaparacriação
deserviçosREST,oJAX-RS.Alémdisso, vocêtambémverácomoincluir linksHA-
TEOASnosseusrecursosdemaneiraeficiente,como testaressesserviços,tópicos
sobrecasoscomplexosdemodelagememuitomais.V a m o semfrente?
99

## Página 104

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1] SamRubyLeonardRichardson.Restfulwebservices.2007.
[2] AlexandreSaudate.Soaaplicado:integrandocom webservicesealém.2013.
101