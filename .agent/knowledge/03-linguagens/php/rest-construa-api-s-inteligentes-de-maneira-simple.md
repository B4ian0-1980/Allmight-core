---json
{
  "id": "rest-construa-api-s-inteligentes-de-maneira-simple",
  "title": "REST Construa API_s inteligentes de maneira simples",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Arquivo Original:** `REST Construa API_s inteligentes de maneira simples.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "api",
    "api_s",
    "construa",
    "inteligentes",
    "linguagens",
    "maneira",
    "php",
    "rest"
  ],
  "perguntas_tipo": [
    "Como utilizar REST Construa API_s inteligentes de maneira simples?",
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

# REST Construa API_s inteligentes de maneira simples

> **Arquivo Original:** `REST Construa API_s inteligentes de maneira simples.pdf`
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

CasadoCódigo Sumário
Sumário
1 P o rq u eutilizar REST? 1
1.1 HTMLtradicionalversusREST . . . . . . . . . . . . . . . . . . . . . . 1
1.2 W e bservices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 REST . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 DesenvolvendoumprotótipodewebserviceREST. . . . . . . . . . . 6
1.5 A v a nçandooprotótipodewebserviceREST . . . . . . . . . . . . . . 9
1.6 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2 O protocolo HTTP 13
2.1 OsfundamentosdoHTTP . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.2 MétodosHTTP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.3 Tiposdepassagemdeparâmetros. . . . . . . . . . . . . . . . . . . . . 17
2.4 Cabeçalhos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.5 MediaTypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.6 Códigosdestatus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.7 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3 Conceitos de REST 29
3.1 Semânticasderecursos . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.2 Interaçãopormétodos . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.3 Representações distintas . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.4 U s ocorretodestatuscodes. . . . . . . . . . . . . . . . . . . . . . . . . 34
3.5 HATEOAS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.6 Sumário. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
i

## Página 6

Sumário CasadoCódigo
4 T i p o sde dados 39
4.1 XML. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
4.2 FerramentalXML:conhecendoosXMLSchemas. . . . . . . . . . . . 40
4.3 TrabalhandocomXMLutilizandoJAXB . . . . . . . . . . . . . . . . . 49
4.4 TestandooXMLgerado. . . . . . . . . . . . . . . . . . . . . . . . . . . 54
4.5 UtilizandoJAXBsemumXMLSchema . . . . . . . . . . . . . . . . . 55
4.6 JSON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.7 TrabalhandocomJSONutilizandoJAXB. . . . . . . . . . . . . . . . . 58
4.8 ValidaçãodeJSONcomJSONSchema . . . . . . . . . . . . . . . . . . 62
4.9 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
5 Implementando se rviços REST em J a v acom S e r v l e t s 69
5.1 U m aimplementaçãocomServlets. . . . . . . . . . . . . . . . . . . . . 69
5.2 Implementandonegociaçãodeconteúdo. . . . . . . . . . . . . . . . . 81
5.3 Implementandoabuscaporumacervejaespecífica. . . . . . . . . . . 83
5.4 Implementandoacriaçãodeumrecurso. . . . . . . . . . . . . . . . . 89
5.5 Implementandonegociaçãodeconteúdonacriaçãodorecurso. . . . 95
5.6 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
Bibliografia 101
Versão: 16.3.8
ii

## Página 7

Capítulo1
P o rqueutilizarREST?
“ N ã oémerecedor do f av ode mel aquele q u eevita a colméiaporque as a b e l h a st ê m
f e r rõ e s”
–WilliamShakespeare
V o c êéumempreendedor.Seguindoafilosofiadeuma startup,vocêquerpro-
duzirum siteparaseuproduto,umalojadecervejasfinaspelainternet.Assim,você
querfazerumsistemaquesejarápidodeproduzire,aomesmotempo,sejaeficiente
efácildereutilizaremváriosambientesdiferentes(vocêestáconsiderandoumaver-
são mobileparaosistema).Assim,vocêexploradiversaspossibilidades.
1.1 HTML tradicional versus REST
V o c êdecideavaliar,antesdetudo,sistemastradicionaisweb,baseadosemformulá-
riosHTML.
Ficaclaroparavocêquefazerumsistematradicional,baseadoemformulários
HTML,estáforadequestão. Issoporqueessetipodeformulárioéclaramenteoti-

## Página 8

1.2.W e bservices CasadoCódigo
mizadoparatrabalharcomsistemasbaseadosnaweb,masvocênãotemcertezaem
relaçãoaoquantoeleseráflexívelparatrabalharcomoutrostiposde front-end.Por
exemplo,considereumatelaparacadastrodosclientesdo site:
<html>
<body>
<form action="/cadastrar" method="post">
<input type="text" name="nome" />
<input type="text" name="dataNascimento" />
<input type="submit" value="Cadastrar" />
</form>
</body>
</html>
Estecódigo(comumpoucomaisdetratamento)deveteatenderbem.Noen-
tanto,apóssubmeteroformulário,oservidordevetetrazerumapáginaHTML-
oque,obviamente,não édesejávelnumcenáriocomváriosfront-ends,comoum
aplicativoparaAndroidouiOS.
Suapróximapossibilidadeé,portanto,avaliaroutrostiposdesistemas.
1.2 Webservices
/>
Opróximocenárioquevemàsuamenteéodeusode web servicestradicionais,ou
seja,baseadosemSOAP(Simple Object Access Protocol).Aprincípio,tepareceuma
boaidéia,jáqueéomecanismodetráfegodeinformações éviaXMLe,portanto,é
possívelinteragircomserviçosdessetipoapartirdecódigo javascript(ouseja,pos-
sibilitandoainteraçãotantoapartirdeum browserquantoapartirdecódigopuro).
Porém,estudandomaisvocêpercebequeinteragircomestetipode web servicenãoé
tãosimplesquantovocêgostaria.Porexemplo,paralistarosclientesdoseusistema,
énecessárioenviaroseguinteXMLparaoservidor:
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<listarClientes xmlns="http://brejaonline.com.br/administracao/1.0/service"
</soap:Body>
</soap:Envelope>
Aoquevocêreceberácomoresposta:
<soap:Envelope xmlns:domain="http://brejaonline.com.br/administracao/1.0/domain"
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
2

## Página 9

CasadoCódigo Capítulo1.PorqueutilizarREST?
>
<soap:Body>
<listarClientesResponse xmlns="http://brejaonline.com.br/administracao/1.0/service"
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
Estecódigo,então, teparececomplicadodemaisparaumasimplesrequisição
delistagemdeclientes.Acomplexidade(everbosidade)doprotocoloficaespecial-
menteevidentequandovocêpensanocasodacomunicaçãofeitacomplataformas
móveis,ondeacomunicaçãopelarededeveseramaissucintapossível.
1.3 REST
V o c êestudamaisarespeitode web servicesquandovocêlêsobreserviçosREST.Ao
estudarsobreoassunto,tepareceumatécnicasimples.Porexemplo,pararealizar
alistagemdeclientesdoseusistema,vocêpodeutilizaronavegador(sejaesteo
Chrome, Firefox, Internet Explorerouqualqueroutro)paraabriraURL
http://localhost:8080/cervejaria/clientes.Aofazerisso,vocêpodeobteroseguintere-
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

## Página 10

1.3.REST CasadoCódigo
Mas,afinal,comofazerseucódigointeragircomestalistagem?Oqueaconteceu?
O sprincípios básicosde REST
REST significa REpresentational State Transfer (ou Transferência de
Estado Representativo,emtraduçãolivre),eéumestilodedesenvolvimento
de web servicesqueteveorigemnatesededoutoradodeRoyFielding. Este,por
suavez,éco-autordeumdosprotocolosmaisutilizadosnomundo,oHTTP(
HyperText Transfer Protocol).Assim,énotávelqueoprotocoloRESTégui-
ado(dentreoutrospreceitos)peloqueseriamasboaspráticasdeusodeHTTP:
•U s oadequadodosmétodosHTTP;
•U s oadequadodeURL’s;
•U s odecódigosdestatuspadronizadospararepresentaçãodesucessosoufa-
lhas;
•U s oadequadodecabeçalhosHTTP;
•Interligações entreváriosrecursosdiferentes.
Opropósitodestelivroé,portanto,exemplificaroquesãoestaspráticaseguiar
você,leitor,atravésdasmesmasefornecerosinsumosdecomoconstruirseuspró-
priosserviços,demaneiraqueestessejamsempretãoescaláveis,reutilizáveisema-
nuteníveisquantopossível.
A sfundaçõ e sde REST
O“marcozero”deRESTéo recurso.EmREST,tudoédefinidoemtermosde
recursos,sendoestesosconjuntosdedadosquesãotrafegadospeloprotocolo.Os
recursossãorepresentadosporURI’s.Noteque,na web,URI’seURL’ssãoessencial-
menteamesmacoisa-razãopelaqualvouusarosdoistermosnestelivrodeforma
intercalada.
4

## Página 11

CasadoCódigo Capítulo1.PorqueutilizarREST?
Qu a la diferença entre u m a URL e u m a URI?
URL significa Universal Resource Locator e URI,
Universal Resource Identifier. U m aURI, como diz o
próprionome,podeserutilizadaparaidentificarqualquercoisa-dar
umcaminhoparaumdeterminadoconteúdo,darnomeaeste,etc. Já
umaURLpodeserutilizadaapenasparafornecercaminhos-sendo
queumaURLé,portanto,umaformadeumaURI.Émaisnaturalque
URI’squenãosejamURL’ssejamutilizadasemoutroscontextos,como
fornecimentode namespacesXML.
T o m a n d ocomoexemploocasodalistagemdeclientes,épossíveldecompôra
URLutilizadaparalocalizaçãodalistagememváriaspartes:
http://localhost:8080/cervejaria/clientes
•http://-Indicaoprotocoloqueestásendoutilizado(nocaso,HTTP);
•localhost:8080-Indicaoservidorderedequeestásendoutilizadoeaporta
(quandoaportanão éespecificada,assume-sequeéapadrão -nocasodo
protocoloHTTP,80);
•cervejaria-Indicao contextodaaplicação,ouseja,araizpelaqualaaplicação
estásendofornecidaparaocliente. V o umereferiraesta,daquiemdiante,
como contexto da a p l i c açãoouapenas contexto;
•clientes-Éoendereço,defato,dorecurso-nocaso,alistagemdeclientes.
V o umereferiraeste,daquiemdiante,como endereço do recurso.
O protocolo
Oprotocolo,emrealidade,nãoéumarestriçãoemREST-emteoria.Naprá-
tica,oHTTPéoúnicoprotocolo100%compatívelconhecido.V a l edestacarqueo
HTTPS( HyperText Transfer Protocol over Secure Sockets Layer)
não éumavariação doHTTP,masapenasaadição deumacamadaextra-oque
mantémoHTTPSnamesmacategoriaqueoHTTP,assimcomoqualqueroutro
protocoloquesejautilizadosobreoHTTP,comoSPDY.
Aspossíveiscausasparaesta“preferência”podemserapontadas: oautordo
HTTPtambéméoautordeRESTe,alémdisso,oprotocoloHTTPéumdosmais
5

## Página 12

1.4.DesenvolvendoumprotótipodewebserviceREST CasadoCódigo
utilizadosnomundo(sendoquea web,demaneirageral,éfornecidaporestepro-
tocolo).EstesfatospromoveriamumaaceitaçãograndeerápidaabsorçãodeREST
pelacomunidadededesenvolvedores.
A URL
AURLescolhidadeveserúnicaporrecurso. Istosignificaque,sempreque
desejarobterarepresentação detodososclientes,vocêdeveutilizaraURL http:
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
Sevocêdesejar,portanto,retornarumclienteespecífico,vocêdeveutilizaruma
URLdiferente.Suponha,porexemplo,quevocêdesejaretornaroclientecom id
iguala1.Nestecaso,aURLseria http://localhost:8080/cervejaria/clientes/1.Issoretor-
nariaalgocomo:
<cliente id="1">
<nome>Alexandre</nome>
<dataNascimento>2012-12-01</dataNascimento>
</cliente>
1.4 Desenvolvendo u m protótipo de web service
REST
Paradesenvolverumprotótipode web serviceRESTbemsimples,nãoénecessário
utilizar-sedealtatecnologia.Bastaqueodesenvolvedortenhaemmenteoresultado
quedesejaalcançarecriarumarquivocontendoarespostadesejada.Porexemplo,
suponhaumarquivo clientes.xml,comoconteúdo:
6

## Página 13

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
do arquivo>. Porexemplo,nomeucaso(ambienteLinux),oarquivoestáem
/home/alexandre/workspace/rest/cap-01/src/main/resources/clientes.xml.
Assim, aURLcompletafica file:///home/alexandre/workspace/rest/cap-01/src/main/
resources/clientes.xml-notequesão trêsbarrasnocomeço(duasparadelimitação
doprotocoloeoutraparaindicararaizdosistemaLinux).
URL para arquivos no Windows
NoWindows,pararenderizarumaURLtambéménecessáriouti-
lizartrêsbarrasnocomeço. Porexemplo,paralocalizarumarquivo
em Documentos,ocaminhoaserinseridono browserficariasimilar
a file:///C:/Users/Alexandre/Documents/clientes.xml. Istoédevidoauma
particularidadedoprópriosistemadearquivosdoWindows,quepode
terváriasraízes(C:,D:,eassimpordiante).
Destaforma,oconteúdoérenderizadopelo browser:
7

## Página 14

1.4.DesenvolvendoumprotótipodewebserviceREST CasadoCódigo
Figura1.1:XMLrenderizadopelobrowser
Paradesenvolverumclienteparaestearquivo,bastautilizaraAPIdeI/Odo
próprioJava,começandopelaclasse java.net.URL,queindicaqualocaminhoa
serseguido:
String caminho = "file:///home/alexandre/workspace/rest/" +
"cap-01/src/main/resources/clientes.xml";
URL url = new URL(caminho);
Feitoisso,opróximopassoéconectar-seaestecaminhoeabriruma i n p u ts t re am,
ouseja,umcanaldeleituradedadosdocaminhoindicadopelaURL.Paraconectar-
se,bastautilizarométodo openConnectiondaURL,eparaabrira i n p u ts t re am,
bastautilizarométodo getInputStream:
java.io.InputStream inputStream = url.openConnection().getInputStream();
Opróximopassoéencapsularestaleituraemum java.io.BufferedReader.
Estaclassepossuiummétodoutilitárioparalerinformaçõeslinhaalinha,facilitando
oprocessodeleituradedados.Parautilizá-lo,noentanto,énecessárioencapsulara
InputStreamemum java.io.InputStreamReader:
BufferedReader bufferedReader = new BufferedReader(
new InputStreamReader(inputStream));
8

## Página 15

CasadoCódigo Capítulo1.PorqueutilizarREST?
U m avezfeitoesseprocedimento,bastautilizarométodo readLineemum
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
1.5 Av ançando o protótipo de web serviceREST
Paradesenvolverumprotótipoquesejaverdadeiramentebaseadonaweb,bastaum
simples servlet.Nocódigo-fontedestelivro,estouutilizandoaespecificação3.0de
servlets,quemepermiteanotá-losparaquesejamdetectadospelocontêiner.
Pararealizaralistagemdeclientes,bastafazercomqueo servletleiaoarquivo
clientes.xml,utilizandoanteriormente,Assim,o servletserácapazdefornecer
9

## Página 16

1.5.A v a nçandooprotótipodewebserviceREST CasadoCódigo
estasinformações paraocliente.Estefornecimentodedadosvaiserfeitoviamétodo
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
No código-fonte do livro (disponível em https://github.com/
alesaudate/rest/), vocêencontraumprojetoMavencomestecódigo
prontoparaserinicializado.Bastaexecutar mvn jetty:runeacessar
estaURL.
AoacessaraURLhttp://localhost:8080/cervejaria/clientes,vocêobtémcomo
10

## Página 17

CasadoCódigo Capítulo1.PorqueutilizarREST?
respostaexatamenteoconteúdodoarquivo.Epararealizaristocomcódigo,basta
alterarocódigofontedoclientecriadoanteriormenteparaestamesmaURL:
URL url = new URL("http://localhost:8080/cervejaria/clientes");
1.6 Sumário
Nestecapítulo,vocêpodeconferiralgunsdosprincipaismotivospelosquaisomo-
deloRESTéselecionadoparasetrabalharemaplicações modernas.V o c êconferiu
algunsdosprincípiosmaisbásicosdeREST,comoousodeURL’secomorealizaro
acessoaestesdocumentosatravésde browsersecódigoJava.
Resta,ainda,conferirosprincípiosdoprotocoloHTTP(nosquaisRESTéfor-
tementebaseado)eentendercomocriarserviçosmaiscomplexosutilizandoeste
paradigma.
11

## Página 19

Capítulo2
OprotocoloHTTP
“ S ev imais longe, foi por estar de pésobre ombros de gigantes”
–IsaacNewton
Comomencionadoanteriormente,omodeloRESTfoidesenvolvidoporRoyFi-
elding,umdoscriadoresdoprotocoloHTTP.Portanto,ficanaturalmenteevidente,
paraquemconheceambososmodelos,assemelhançasentreambos-sendoque,
narealidade,RESTéidealmenteconcebidoparausocomoprotocoloHTTP.Por-
tanto,paraserumbomusuáriodeREST,énecessárioterumbomconhecimentodo
protocoloHTTP.
2.1 Os fundamentos d oHTTP
OprotocoloHTTP(HyperT extTransferProtocol-ProtocolodeTransferênciadeHi-
pertexto)datade1996,épocaemqueostrabalhosconjuntosdeTimBerners-Lee,
RoyFieldingeHenrikFrystykNielsenlevaramàpublicaçãodeumaRFC(Request
for Comments)descrevendoesteprotocolo.Trata-sedeumprotocolodecamadade

## Página 20

2.1.OsfundamentosdoHTTP CasadoCódigo
aplicação(segundoomodeloOSI)e,portanto,derelativafacilidadedemanipulação
emaplicações.
Esteprotocolofoidesenvolvidodemaneiraaseromaisflexívelpossívelpara
comportardiversasnecessidadesdiferentes.Emlinhasgerais,esteprotocolosegue
oseguinteformatoderequisições:
<método> <URL> HTTP/<versão>
<Cabeçalhos - Sempre vários, um em cada linha>
<corpo da requisição>
Porexemplo,pararealizararequisiçãodocapítulopassado,algosemelhanteao
seguintefoienviadoparaoservidor:
GET /cervejaria/clientes HTTP/1.1
Host: localhost:8080
Accept: text/html
Portanto,oquefoipassadonestarequisiçãofoi:
GET /cervejaria/clientes HTTP/1.1
Com isso, o método GET foi utilizado para solicitar o conteúdoda URL
/cervejaria/clientes.Alémdisso,oprotocoloHTTPversão1.1foiutilizado.
Notequeo host,ouseja,oservidorresponsávelporfornecerestesdados,épas-
sadoemum c a b eçalhoàparte.Nocaso,o hostescolhidofoi localhost,naporta
8080.
Alémdisso,umoutrocabeçalho, Accept,foifornecido.
Arespostaparaasrequisições seguemoseguinteformatogeral:
HTTP/<versão> <código de status> <descrição do código>
<cabeçalhos>
<resposta>
Porexemplo,arespostaparaestarequisiçãofoisemelhanteàseguinte:
HTTP/1.1 200 OK
Content-Type: text/xml
Content-Length: 245
14

## Página 21

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
Aqui,notequeocódigo200indicouquearequisiçãofoibem-sucedida,eoca-
beçalho Content-Lengthtrouxeotamanhodaresposta-nocaso,oXMLque
contémalistagemdeclientes.Alémdisso,ocabeçalho Content-Typeindicaque
arespostaé,defato,XML-atravésdeumtipoconhecidocomo Media Type.
2.2 Métodos HTTP
AversãocorrentedoHTTP,1.1,defineoficialmenteoitométodos-emboraoproto-
colosejaextensívelemrelaçãoaestesmétodos.Hoje,estesoitosão:
•GET
•POST
•PUT
•DELETE
•OPTIONS
•HEAD
•TRACE
•CONNECT
Cadamétodopossuiparticularidadeseaplicações deacordocomanecessidade.
Estasparticularidadessãodefinidasemtermosde idempotência, segurançae me-
canismo de passagem de parâmetros.Alémdisso,porcadaumpossuirparticulari-
dadesdeuso,considerareinestelivroapenasosseisprimeiros-osmétodos TRACE
e CONNECTserãoconsideradosforadoescopodestelivro.
15

## Página 22

2.2.MétodosHTTP CasadoCódigo
Idempotência
Aidempotênciadeummétodoérelativaàsmodificações quesãorealizadasem
informações doladodoservidor.Trata-sedoefeitoqueumamesmarequisiçãotem
doladodoservidor-seamesmarequisição,realizadamúltiplasvezes,provocaalte-
rações noladodoservidorcomosefosseumaúnica,entãoestaéconsideradaidem-
potente.
Porexemplo,considereasquatrooperações debancosdedados: SELECT,
INSERT, UPDATEe DELETE.Realizandoumparalelodestascomoconceitode
idempotência,observeoseguinte:
SELECT * from CLIENTES;
Notequeestarequisição,paraumbancodedados,teráomesmoefeitotodas
asvezesemqueforexecutada(obviamente,assumindoqueninguémestáfazendo
alterações nasinformações quejáestavamgravadas).
Agora,observeoseguinte:
INSERT INTO CLIENTES VALUES (1,'Alexandre');
Estarequisição,porsuavez,provocarádiferentesefeitossobreosdadosdobanco
dedadostodasasvezesqueforexecutada,dadoqueestáaumentandootamanhoda
tabela.Portanto,elanãoéconsideradaidempotente.
Notequeesteconceitonãoestárelacionadoàrealizaçãoounãodemodificações.
Porexemplo,considereasoperações UPDATEe DELETE:
UPDATE CLIENTES SET NOME = 'Paulo' WHERE ID = 1;
DELETE FROM CLIENTES WHERE ID = 1;
Noteque,emambososcasos,asalterações realizadassão idênticasàtodasas
subsequentes.Porexemplo,suponhaosdados:
ID NOME
---------
1 Alexandre
Searequisiçãodeatualizaçãoforenviada,estesdadosficarãoassim:
ID NOME
---------
1 Paulo
16

## Página 23

CasadoCódigo Capítulo2. OprotocoloHTTP
Eentão,casoamesmarequisiçãosejaenviadarepetidasvezes,aindaassimpro-
vocaráomesmoefeitoquedaprimeiravez,sendoconsiderada,portanto,idempo-
tente.
Segurança
Quantoà segurança,osmétodossão assimconsideradossenão provocarem
quaisqueralterações nosdadoscontidos.Aindaconsiderandooexemplodasope-
rações debancosdedados,porexemplo,ométodo SELECTpodeserconsiderado
seguro- INSERT, UPDATEe DELETE,não.
Emrelação aestasduascaracterísticas,aseguintedistribuição dosmétodos
HTTPéfeita:
Figura2.1:MétodosHTTP,deacordocomidempotênciaesegurança
2.3 Tiposde passagem de parâmetros
OsmétodosHTTPsuportamparâmetrossobduasformas:oschamados q u e r ypa-
rameterse body parameters.
Os q u e r yparameterssãopassadosnaprópriaURLdarequisição. Porexemplo,
considereaseguinterequisiçãoparaoserviçodebuscadoGoogle:
http://www.google.com.br/?q=HTTP
EstarequisiçãofazcomqueoservidordoGoogleautomaticamenteentendaa
string HTTPcomoumparâmetro.InserirestaURLno browserautomaticamente
indicaparaoservidorqueumabuscaporHTTPestásendorealizada.
Os q u e r yparameterssãoinseridosapartirdosinaldeinterrogação. Estesinal
indicaparaoprotocoloHTTPque,dealíemdiante,serãoutilizados q u e r yparame-
t e r s.Essessãoinseridoscomformato<chave>=<valor>(assimcomonoexemplo,
17

## Página 24

2.3.Tiposdepassagemdeparâmetros CasadoCódigo
emque qéachavee HTTP,ovalor).Casomaisdeumparâmetrosejanecessário,os
paressãoseparadoscomum &.Porexemplo,arequisiçãoparaoserviçodoGoogle
poderia,também,serenviadadaseguintemaneira:
http://www.google.com.br/?q=HTTP&oq=HTTP
Os q u e r yparameterssãoenviadosnaprópriaURL.Istoquerdizerquearequisi-
çãoparaoGoogleésemelhanteàseguinte:
GET /?q=HTTP&oq=HTTP HTTP/1.1
Host: www.google.com.br
NotequeocaracterdeespaçoéoseparadorentreométodoHTTP,aURLea
versãodoHTTPaserutilizada.Destaforma,sefornecessárioutilizarespaçosnos
q u e r yparameters,énecessárioutilizarumatécnicachamadade codificação da URL.
EstatécnicaadaptaasURL’sparaqueelassejamcompatíveiscomomecanismode
enviodedados,ecodificamnãoapenasespaçoscomooutroscaracteresespeciaise
caracteresacentuados.
Estacodificaçãosegueaseguinteregra:
•Espaçospodemsercodificadosutilizando +ouastring %20
•Letrasmaiúsculaseminúsculas,númeroseoscaracteres ., -, ~e _sãodeixados
comoestão
•CaracteresrestantessãocodificadosdeacordocomsuarepresentaçãoASCII
/UTF-8ecodificadoscomohexadecimal
Assim,a string às vezesécodificadacomo %C3%A0s+vezes(sendoqueos b y t e s
C3eA0representamosnúmeros195e160que,emcodificaçãoUTF-8,tornam-sea
letra à).
Notequeumalimitaçãodos q u e r yparameterséaimpossibilidadedepassarda-
dosestruturadoscomoparâmetro.Porexemplo,nãoháacapacidadederelacionar
um q u e r yparamcomoutro,levandoodesenvolvedoracriarmaneirasdecontor-
narestalimitação.Porexemplo,suponhaquesejanecessáriodesenvolverumapes-
quisadeclientesbaseadaemváriostiposdeimpostosdevidosnumcertoperíodode
tempo.Estapesquisadeveriafornecer:
•Onomedoimposto
18

## Página 25

CasadoCódigo Capítulo2. OprotocoloHTTP
•Operíodo(datainicialedatafinaldabusca)
Seestapesquisaforbaseadaemumúnicoimposto,não háproblemaalgum.
Mastomecomobaseumapesquisabaseadacomoumalistadeimpostos.Elaseria
semelhantea:
/pessoas?imposto.1=IR&data.inicio.1=2011-01-01&data.inicio.2=2012-01-01
Ondeanumeração,nestecaso,seriaoelementoagrupadordosdados-ouseja,
um workaroundparaalimitaçãodedadosestruturados.
Quandoháanecessidadedefornecerdadoscomplexos,noentanto,épossível
fazê-lopelocorpodarequisição.Algocomo:
POST /clientes HTTP/1.1
Host: localhost:8080
Content-Type: text/xml
Content-Length: 93
<cliente>
<nome>Alexandre</nome>
<dataNascimento>2012-01-01</dataNascimento>
</cliente>
Quantoaestetipodeparâmetro,nãohálimitações. Oservidorfazainterpreta-
çãodosdadosapartirdofatodequeessesparâmetrossãoosúltimosdodocumento,
econtrolaotamanhodaleiturautilizandoocabeçalho Content-Length.
2.4 Cabeçalhos
Oscabeçalhos,emHTTP,sãoutilizadosparatrafegartodootipodemetainforma-
ção arespeitodasrequisições. Váriosdestescabeçalhossão padronizados;noen-
tanto,elessãofacilmenteextensíveisparacomportarqualquerparticularidadeque
umaaplicaçãopossarequerernessesentido.
Porexemplo,aorealizarumarequisição, peloFirefox,paraositehttp://www.
casadocodigo.com.br/,asseguintesinformações sãoenviadas:
GET / HTTP/1.1
Host: www.casadocodigo.com.br
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
19

## Página 26

2.4. Cabeçalhos CasadoCódigo
Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Co m o checar o tráfego viaHTTP
Paravisualizarotráfegodestesdados,váriastécnicasestãoàdisposi-
ção. Asmaissimplessãoainstalaçãodeum plugindoFirefoxchamado
Live HTTP Headersouapertar F12noChrome.
Portanto,osseguintescabeçalhossãoenviados: Host, User-Agent, Accept,
Accept-Language, Accept-Encodinge Connection. Cadaumdessestem
umsignificadoparaoservidor-noentanto,oprotocoloHTTPnãoexigenenhum
deles. Aoestabelecerestaliberdade,tantooclientequantooservidorestão livres
paranegociaroconteúdodamaneiracomoacharemmelhor.
Obviamente,istonãoquerdizerqueestescabeçalhosnãosãopadronizados.Da
listaacima,cadacabeçalhopossuiumaexplicação:
•Host-mostraqualfoioDNSutilizadoparachegaraesteservidor
•User-Agent-forneceinformações sobreomeioutilizadoparaacessareste
endereço
•Accept-realizanegociação comoservidorarespeitodoconteúdoaceito
(maisinformações naseção2.4).
•Accept-Language-negociacomoservidorqualoidiomaaserutilizadona
resposta
•Accept-Encoding-negociacomoservidorqualacodificaçãoaserutilizada
naresposta
•Connection-ajustaotipodeconexãocomoservidor(persistenteounão).
Tecnicamentefalando,oscabeçalhossãoutilizadosparatráfegode meta dados
-ouseja,informações arespeitodainformação“ d everdade”.T o m eumcenáriode
enviode emails:odestinatário,oassuntoeoutrasinformaçõessãoapenas meta dados
-averdadeirainformaçãoéoconteúdodo email.Destaforma,umarequisiçãopara
umserviçoHTTPdeenviode emailspoderiaserfeitadaseguinteforma:
20

## Página 27

CasadoCódigo Capítulo2. OprotocoloHTTP
POST /email HTTP/1.1
Host: brejaonline.com.br
Destinatario: alesaudate@gmail.com
Assunto: Quanto custa a cerveja dos Simpsons?
VáriosusosdiferentessãodadosparacabeçalhosemHTTP.Aolongodestelivro,
voumencioná-losquandonecessário.
2.5 MediaTypes
Aorealizarumarequisição paraosite http://www.casadocodigo.com.br,o Media
Type text/htmléutilizado,indicandoparaonavegadorqualéotipodainfor-
maçãoqueestásendotrafegada(nocaso,HTML).Istoéutilizadoparaqueocliente
saibacomotrabalharcomoresultado(enão comtentativaeerro,porexemplo),
dessamaneira,os Media Typessãoformaspadronizadasdedescreverumadeter-
minadainformação.
Os Media Typessãodivididosem tipose subtipos,eacrescidosdeparâmetros
(sehouverem).Sãocompostoscomoseguinteformato: tipo/subtipo.Sehouverem
parâmetros,o ;(ponto-e-vírgula)seráutilizadoparadelimitaraáreadosparâme-
tros.Portanto,umexemplode Media Typeseria text/xml; charset="utf-8”(para
descreverumXMLcujacodificaçãosejaUTF-8).
Ostiposmaiscomunssão:
•application
•audio
•image
•t e x t
•video
•v n d
Cadaumdessestiposéutilizadocomdiferentespropósitos. Applicationéuti-
lizadoparatráfegodedadosespecíficosdecertasaplicações. Audioéutilizadopara
formatosdeáudio.Imageéutilizadoparaformatosdeimagens. T e x téutilizado
paraformatosdetextopadronizadosoufacilmenteinteligíveisporhumanos. Video
21

## Página 28

2.5.MediaTypes CasadoCódigo
éutilizadoparaformatosdevídeo. V n déparatráfegodeinformações desoftwares
específicos(porexemplo,oMicrosoftOffice).
EmserviçosREST,váriostiposdiferentesde Media Typessãoutilizados.As
maneirasmaiscomunsderepresentardadosestruturados,emserviçosREST,sãovia
XMLeJSON,quesãorepresentadospelos Media Types application/xmle
application/json,respectivamente.OXMLtambémpodeserrepresentadopor
text/xml,desdequepossaserconsideradolegívelporhumanos.
Note que subtipos mais complexos do que isso podem ser representados
com o sinal + (mais). Este sinal éutilizado em váriossubtipos para delimi-
tação de maisde um subtipo. Esteéo caso comXHTML,porexemplo,que
denota o tipo HTML acrescido das regras de XML, e cujo media type é
application/xhtml+xml. OutrocasocomuméodoprotocoloSOAP,cujo
media typeé application/soap+xml.
Os Media Types são negociados a partir dos cabeçalhos Accept e
Content-Type. Oprimeiroéutilizadoemrequisições, eosegundo,emrespos-
tas.
Aoutilizarocabeçalho Accept,oclienteinformaaoservidorqualtipodedados
esperareceber.Casosejaotipodedadosquenãopossaserfornecidopeloservidor,
omesmoretornaocódigodeerro 415(apresentadonaseção2.6),indicandoqueo
M e d i aT y p enãoésuportado.Seotipodedadosexistir,entãoosdadossãofornecidos
eocabeçalho Content-Typeapresentaqualéotipodeinformaçãofornecida.
Existemváriasformasderealizarestasolicitação.Casooclienteestejadisposto
arecebermaisdeumtipodedados,ocabeçalho Acceptpodeserutilizadopara
estanegociação. Porexemplo,seoclientepuderreceberqualquertipodeimagem,
estasolicitaçãopodeutilizarum curinga,representadopor*(asterisco).Oservidor
iráconverterestasolicitaçãoemumtipoadequado.Estanegociaçãoserásimilarà
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

## Página 29

CasadoCódigo Capítulo2. OprotocoloHTTP
Alémdisso, tambémépossívelsolicitarmaisde um tipo de dados apenas
separando-ospor ,(vírgula).Porexemplo,umclientedeumapáginawebpoderia
realizarumasolicitaçãocomoaseguinte:
GET / HTTP/1.1
Host: brejaonline.com.br
Accept:text/html,*/*
Note,assim,queoclientesolicitaumapáginaHTMLqueseumanãoestiverdis-
ponível,qualquertipodeconteúdoéaceito-comopodeserobservadopelapresença
dedoiscuringas,emtipoesubtipodedados.Nestecaso,aprioridadeatendidadaé
ada especificidade,ouseja,como text/htmlémaisespecífico,temmaisprioridade.
Emcasodeváriostiposdedadosquenãoatendamaestaregra,oparâmetro q
podeseradotadoparaquesepossarealizardiferenciações depeso.Esteparâmetro
recebevaloresvariandoentre0.1e1,contendoaordemdeprioridade.Porexemplo,
suponhaaseguinterequisição:
GET / HTTP/1.1
Host: brejaonline.com.br
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
IstosignificaquetantoHTMLquantoXHTMLtêmprioridademáxima.Nafalta
deumarepresentaçãodorecursocomqualquerumdessestiposdedados,oXML
éaceitocomprioridade90%.NaausênciadoXML,qualqueroutrarepresentaçãoé
aceita,comprioridade80%.
2.6 Códigos de status
T o d arequisiçãoqueéenviadaparaoservidorretornaumcódigodestatus.Esses
códigossãodivididosemcincofamílias:1xx,2xx,3xx,4xxe5xx,sendo:
•1xx-Informacionais
•2xx-Códigosdesucesso
•3xx-Códigosderedirecionamento
•4xx-Erroscausadospelocliente
•5xx-Errosoriginadosnoservidor
23

## Página 30

2.6. Códigosdestatus CasadoCódigo
DeacordocomLeonardRichardsoneSamRuby,oscódigosmaisimportantese
maisutilizadossão:
2xx
20 0- O K
Indicaqueaoperaçãoindicadatevesucesso.
20 1- Crea t ed
Indicaqueorecursodesejadofoicriadocomsucesso.Deveretornarumcabeça-
lho Location,quedeveconteraURLondeorecursorecém-criadoestádisponível.
20 2- Accepted
Indicaqueasolicitaçãofoirecebidaeseráprocessadaemoutromomento.Étipi-
camenteutilizadaemrequisições assíncronas,quenãoserãoprocessadasemtempo
real.Poressemotivo,poderetornarumcabeçalho Location,quetraráumaURL
ondeoclientepodeconsultarseorecursojáestádisponívelounão.
20 4- N oContent
Usualmenteenviadoemrespostaaumarequisição PUT, POSTou DELETE,
ondeoservidorpoderecusar-seaenviarconteúdo.
206 - Partial Content
Utilizadoemrequisições GETparciais,ouseja,quedemandamapenaspartedo
conteúdoarmazenadonoservidor(casomuitoutilizadoemservidoresde down-
load).
3xx
301- Moved Permanently
Significaqueorecursosolicitadofoirealocadopermanentemente.U m aresposta
comocódigo301deveconterumcabeçalho LocationcomaURLcompleta(ou
seja,comdescriçãodeprotocoloeservidor)deondeorecursoestáatualmente.
24

## Página 31

CasadoCódigo Capítulo2. OprotocoloHTTP
303 - S e eOther
Éutilizadoquandoarequisiçãofoiprocessada,masoservidornãodesejaenviar
oresultadodoprocessamento.Aoinvésdisso,oservidorenviaarespostacomeste
códigodestatuseocabeçalho Location,informandoondearespostadoproces-
samentoestá.
304 - N o tModified
Éutilizado,principalmente,emrequisições GETcondicionais-quandoocliente
desejaverarespostaapenasseelativersidoalteradaemrelaçãoaumarequisição
anterior.
307 - T emporaryRedirect
Similarao301,masindicaqueoredirecionamentoétemporário,não perma-
nente.
4xx
400 - Bad Request
Éumarespostagenéricaparaqualquertipodeerrodeprocessamentocujares-
ponsabilidadeédoclientedoserviço.
401 - Unauthorized
Utilizadoquandooclienteestátentandorealizarumaoperaçãosemterforne-
cidodadosdeautenticação(ouaautenticaçãofornecidaforinválida).
403 - Forbidden
Utilizadoquandooclienteestátentandorealizarumaoperaçãosemteradevida
autorização.
404 - N o tFound
Utilizadoquandoorecursosolicitadonãoexiste.
25

## Página 32

2.6. Códigosdestatus CasadoCódigo
405 - Method N o tAllowed
UtilizadoquandoométodoHTTPutilizadonão ésuportadopelaURL.Deve
incluirumcabeçalho Allownaresposta,contendoalistagemdosmétodossupor-
tados(separadospor“,”).
409 - Conflict
Utilizadoquandoháconflitosentredoisrecursos.Comumenteutilizadoemres-
postaacriações deconteúdosquetenhamrestrições dedadosúnicos-porexemplo,
criaçãodeumusuárionosistemautilizandoum loginjáexistente.Seforcausado
pelaexistênciadeoutrorecurso(comonocasocitado),arespostadeveconterum
cabeçalho Location,explicitandoalocalizaçãodorecursoqueéafontedoconflito.
4 1 0- G o n e
Semelhanteao404,masindicaqueumrecursojáexistiunestelocal.
4 1 2- Precondition failed
Comumenteutilizadoemrespostaarequisições GETcondicionais.
4 1 5- U n s u p p o r t e dM e d i aT y p e
Utilizadoemrespostaaclientesquesolicitamumtipodedadosquenãoésu-
portado-porexemplo,solicitarJSONquandooúnicoformatodedadossuportado
éXML.
5xx
500 - Internal Server Error
Éumarespostadeerrogenérica,utilizadaquandonenhumaoutraseaplica.
503 - Service Unavailable
Indicaqueoservidorestáatendendorequisições, masoserviçoemquestãonão
estáfuncionandocorretamente.Podeincluirumcabeçalho Retry-After,dizendo
aoclientequandoeledeveriatentarsubmeterarequisiçãonovamente.
26

## Página 33

CasadoCódigo Capítulo2. OprotocoloHTTP
2.7 Conclusão
V o c êpôde conferir,nestecapítulo,osprincípiosbásicosdoprotocoloHTTP.Estes
princípiossãoousodecabeçalhos,métodos,códigosdestatuseformatosdedados
-queformamabasedousoeficientedeREST.
V o c êiráconferir,nospróximoscapítulos,comoRESTsebeneficiadosprincípios
desteprotocolodeformaatiraromáximoproveitodestatécnica.
27

## Página 35

Capítulo3
ConceitosdeREST
“ Amente q u ese a b r ea u m anova idéiajamais volta a seu tamanho original”
–AlbertEinstein
Comoditoanteriormente,RESTébaseadonosconceitosdoprotocoloHTTP.
Alémdisso,esteprotocoloéabaseparaa webcomoaconhecemos,sendoquea
próprianavegaçãonestapodeserencaradacomoumusodeREST.
Noentanto,RESTnãoétãosimplesquantosimplesmenteutilizarHTTP-exis-
temregrasquedevemserseguidasparaserealizarusoefetivodesteprotocolo.A
intençãodestecapítuloéapresentarquaissãoestesconceitos,demaneiraquevocê,
leitor,conheçaastécnicascertasparadesenvolvimentodestetipodeserviço.
3.1 Semânticas de recursos
T o d oserviçoRESTébaseadonoschamados recursos,quesãoentidadesbemde-
finidasemsistemas,quepossuemidentificadoreseendereços(URL’s)próprios.No
casodaaplicaçãoqueestamosdesenvolvendo, brejaonline.com.br,podemos

## Página 36

3.1.Semânticasderecursos CasadoCódigo
assumirqueumacervejaéumrecurso.Assim,asregrasdeRESTdizemqueascer-
vejasdevemterumaURLprópriaequeestaURLdevesersignificativa.Destaforma,
umaboaURLparacervejaspodeser /cervejas.
URL ’s no singular ou no plural?
NãoexistemregrasemrelaçãoaestasURL’sestaremnosingularou
noplural-ouseja,nãoimportasevocêprefereutilizar /cervejaou
/cervejas.Oideal,noentanto,émanterumpadrão-tenhatodasas
suasURL’snosingularoutodasnoplural,masnãomisturas.
DeacordocomomodeloREST,estaURLrealizaráinteraçãocomtodasascerve-
jasdosistema.Paratratardecervejasespecíficas,sãousadosidentificadores.Estes
identificadorespodemterqualquerformato-porexemplo,suponhaumacerveja
ErdingerWeissbiercomcódigodebarras123456.Notequeonomedacervejanão
servecomoidentificador(existemvárias“instâncias”deErdingerWeissbier),maso
códigodebarras,sim.
Destaforma,deveserpossívelbuscarestacervejaatravésdocódigodebarras,
comaURL /cervejas/123456. Lembre-se,regrassemelhantesaplicam-sea
qualquerrecurso.OidentificadoraserutilizadonaURLpodeserqualquercoisa
quevocêassimdesejar,emaisdeumtipodeidentificadorpodeserusadoparaal-
cançarumrecurso.Porexemplo,suponhaqueasuabasedeclientestenhatantoum
identificadorgeradopelobancodedadosquantoosCPF’sdosclientes:
•Clientenúmero1:CPF445.973.986-00
•Clientenúmero2:CPF428.193.616-50
•Clientenúmero3:CPF719.760.617-92
Assim,parabuscaroclientedenúmero1,deveserpossívelutilizartantoaURL
/cliente/1quantoaURL /cliente/445.973.986-00.
Podemhavercasos,também,deidentificadorescompostos.Nestecaso,amelhor
práticaseriasepará-losutilizando ;(ponto-e-vírgula).Porexemplo,umserviçode
mapasemquesejapossívelacharumpontoporlatitudeelongitudeteriaURL’scomo
/local/-23.5882888;-46.6323259.
Maisàfrente,detalhareicasosmaiscomplexosdeURL’s.
30

## Página 37

CasadoCódigo Capítulo3.ConceitosdeREST
3.2 Interação p o rmétodos
ParainteragircomasURL’s,osmétodosHTTPsãoutilizados.Aregradeouropara
estainteraçãoéque URL ’ssão substantivos, e métodosHTTP são verbos.Istoquer
dizerqueosmétodosHTTPsãoosresponsáveisporprovocaralteraçõesnosrecursos
identificadospelasURL’s.
Estasmodificações sãopadronizadas,demaneiraque:
•GET-recuperaosdadosidentificadospelaURL
•POST-criaumnovorecurso
•PUT-atualizaumrecurso
•DELETE-apagaumrecurso
CRUD
Notequeestesquatrométodosprincipaispodemserdiretamenterelacionadosa
operaçõesdebancosdedados.Assim,pararecuperaroclientedenúmero1dobanco
dedados,bastautilizarométodoGETemconjuntocomaURL /cliente/1;para
criarumnovocliente,bastautilizarométodo POSTsobreaURL /cliente(o
identificadorserácriadopelobancodedados);paraatualizarestecliente,utilizeo
método PUTsobreaURL /cliente/1e,finalmente,paraapagarocliente,utilize
ométodo DELETEsobreaURL /cliente/1.
Notequetodasestasoperações são lógicas.Istoquerdizerqueutilizarométodo
DELETE,porexemplo,não significanecessariamenteexcluirodadodobancode
dados-significaapenasindisponibilizarorecursoparaconsumopelométodoGET.
Ouseja, DELETEpodeapenasmarcarodadonobancodedadoscomo desativado.
Tarefas
CriarserviçosRESTqueexecutemtarefasdenegócio(ex:enviarume-mail,criar
umamáquinaemumserviçode cloud computing,validarumCPFeoutrastarefas
quenãonecessariamenteenvolvaminteraçãocomumbancodedados)étarefamais
complexa. ExigecertograudedomíniodateoriasobreREST,emuitasvezesnão
existemrespostas100%assertivasemrelaçãoàcorretudedasolução.
Paraobterresultadossatisfatórios,deve-sesempreteropensamentovoltado
paraaorientaçãoarecursos.Tomemoscomoexemploocasodoenviodee-mails:a
31

## Página 38

3.3.Representações distintas CasadoCódigo
URLdevesermodeladaemformatodesubstantivo,ouseja,apenas /email.Para
enviaroe-mail,oclientepodeusarométodo POST-ouseja,comoseestivesse
“criando”ume-mail.Damesmaforma,inicializarumamáquinaemumserviçode
cloud computingpodeterumaabordagemmaissimilaraumCRUD:parainicializar
amáquina,oclienteutilizaométodo POSTnaURL /maquinas.Paradesligá-la,
utilizaométodo DELETE.
Existem,também,casosemqueassoluções podemnão parecertriviaisàpri-
meiravista.U mcasoclássicoéodevalidações (deCPF,porexemplo).AURLpode
serclaramenteorientadaasubstantivos( /validacao/CPF,porexemplo),mase
quantoaosmétodos?
Asolução paraestecasoépensardaseguintemaneira:“ e upreciso o b t e ruma
validação?Oucriaruma,ouapagar,ouatualizar?”.Destamaneira,arespostanatural
paraaquestãoparececonvergirparaométodo GET.Noteque,nestecaso,entraem
cenaousodométodo HEAD-poderíamosutilizarométodo GETparaconseguir
resultadosdetalhadoseométodo HEADparaobterapenasocódigode statusda
validação(lembre-sedequeestemétodonãoretornacorpo!).
3.3 Representações distintas
U mdospilaresdeRESTéousode media typesparaalterarasrepresentações de
ummesmoconteúdo,sobperspectivasdistintas.Estaóticaficaevidentequandose
respondeàpergunta: “ q u eladodorecursoestouprocurandoeuqueroenxergar?
Precisodeumafotodeumacerveja,oudadescriçãodela?”.Porexemplo,aorealizar
umabuscaporumacervejanosistema,pode-setantodesejarumXMLcomosdados
dacerveja,quantoumJSONquantoumafotodacerveja:
32

## Página 39

CasadoCódigo Capítulo3.ConceitosdeREST
Figura3.1:Podesermaisinteressanteobterumafotodacervejadoqueadescrição
dela
ComREST,tudoissopodeserfeitoutilizando-seamesmaURL,porexemplo,
/cervejas/1. Oquevaimodificaroresultadoéasolicitação queoclientefi-
zer,atravésdocabeçalho Accept: seoclientefizerumasolicitação paraaURL
/cervejas/1passandoocabeçalho Acceptcomovalor application/xml,
eleiráobterumarepresentaçãodacervejacomoXML.Masseoclientepassarfizer
estarequisiçãopassandoovalor image/*,eleiráobterumafotodacerveja.
33

## Página 40

3.4.Us ocorretodestatuscodes CasadoCódigo
O cabeçalho Accept e os curingas
Noteque,nesteexemplo,euestoufalandodeobterumaimagempas-
sandoocabeçalho Acceptcomovalor image/*.Istosedádevidoao
fatodeque,muitasvezes,nãoestamosinteressadosnotipodaimagem
(JPG,GIF,PNG,etc.),masapenasnofatodeela se rumaimagem!
LeonardRichardsoneSamRuby[1]tambémdefendem,emumaabordagem
maispragmática,queéinteressanteoferecerdistinções entreessestiposdedados
naprópriaURL,apartirdeextensões (similaràsextensões dearquivosnosistema
operacional).Porexemplo,nocasodascervejas,paraobterumarepresentaçãodas
cervejascomoXML,utilizaríamosaURL /cervejas.xml;paraobterarepresen-
taçãocomoumaimagemjpg,utilizaríamosaURL /cervejas.jpg.Notequeesta
abordagempossuivantagensedesvantagens:aopassoqueatestabilidadeésimpli-
ficada(jáquepodemostestarosresultadospelonavegador),aimplementaçãopode
sermaiscomplexaetambémpodeinduzirdiferenciações nasimplementações (ou
seja,terlógicasdistintasparabuscardadossemelhantes).
3.4 Uso correto de status codes
AlgoqueRESTtambémprevêéousocorretodos status codesHTTP.Naprática,
issosignificaconhecê-loseaplicardeacordocomasituação.Porexemplo,ocódigo
200( OK)éutilizadoemgrandepartedassituações (oquepodeacabar“viciando”o
desenvolvedor),masacriaçãoderecursosdeveretornar,quasesempre,ocódigo201
( Created)eocabeçalho Location,indicandoalocalizaçãodorecursocriado.
Ainda,sedoisclientesrealizaremcriaçãoderecursosdeformaqueestesforne-
çamachaveutilizadaparareferenciarorecurso(ouseja,existeumarestriçãodeque
achavedeveserúnicaporrecurso),eestesdoisclientesforneceremamesmachave
nacriaçãodorecurso,ocódigode status409( Conflict)deveserutilizado.
34

## Página 41

CasadoCódigo Capítulo3.ConceitosdeREST
Posso utilizar a chave primária d omeu banco dedados
como ID d o srecursos?
Éerradoassumirqueachaveutilizadanosrecursosserásempreo
IDdobancodedados.Éperfeitamenteaceitávelutilizarestachave,mas
istodeveseruma coincidência,demaneiraqueoseucliente jamaisse
sintacomoseestivessesimplesmenteutilizandoumainterfacediferente
paraacessarumbancodedados.Estarestriçãoécondizentecomoque
mencioneiemmeulivroSOAAplicado:integrandocomwebservicese
além[2],dequeoclientenuncadevesentirosefeitosdeumamodificação
nainfra-estruturadoserviço.
Porexemplo,suponhaqueacriaçãodosclientesnacervejariautilizeoCPFcomo
chavedosrecursos.Sedoisclientesdosserviçostentaremsecadastrarcomomesmo
CPF,umdosclientesdevereceberocódigo409. Arespostacomessecódigodeve
conterocabeçalho Location,indicandoondeestáorecursoqueoriginouocon-
flito.
Aolongodolivro,apresentareisituaçõesondeousocorretodoscódigosde status
faráadiferençanoconsumodosserviços.
3.5 HATEOAS
AúltimadastécnicasmencionadasporRoyéousode Hypermedia A sThe Engine
Of Application State-HATEOAS.Trata-sedealgoquetododesenvolvedor webjá
conhece(apenasnãoporessenome).
T o d avezqueacessamosumapáginaweb,alémdotextodapágina,diversos links
paraoutrosrecursossãocarregados.Estesrecursosincluem scripts JavaScript,
CSS,imagenseoutros.Alémdisso,muitaspáginastêmformulários,queencami-
nhamdadosparaoutrasURL’s.
Porexemplo,considereoseguintetrechodepáginaHTML:
<html>
<head>
<link rel="icon" href="/assets/favicon.ico" type="image/ico" />
<link href="/assets/fonts.css" rel="stylesheet" type="text/css" />
</head>
35

## Página 42

3.5.HATEOAS CasadoCódigo
<body>
<img src="/assets/header.jpg" />
</body>
</html>
Nela,existeumareferênciaparaoíconedapágina(referenciadocoma t ag link
eatributo rel="icon"),umareferênciaparaumarquivoCSSeumareferênciapara
umaimagem.
HATEOASconsideraestes linksdamesmaforma,atravésdareferênciaaações
quepodemsertomadasapartirdaentidadeatual.Porexemplo,vamosmodelaro
sistemadecomprasdanossacervejaria.Paracriarumpedidodecompra,énecessá-
riofornecerumXMLcontendoosdadosdarequisição:
<compra>
<item>
<cerveja id="1">Stella Artois</cerveja>
<quantidade>1</quantidade>
</item>
</compra>
Seestacompraforaceitapeloservidor,oseguintepodeserretornado:
<compra id="123">
<item>
<cerveja id="1">Stella Artois</cerveja>
<quantidade>1</quantidade>
</item>
<link rel="pagamento" href="/pagamento/123" />
</compra>
Noteapresençada t ag link.SeoclienteutilizaraURLpresentenoatributo
href,podeinformaraoservidoromeiodepagamentoaceitoparaacompra.Acri-
açãodomeiodepagamentoseráfeitaatravésdométodoHTTP POST,conforme
mencionadoanteriormente. Esseconhecimento“prévio”fazpartedoquesecon-
vencionouchamar,emREST,de interface uniforme.
Estes links,emHATEOAS,têmdoissegmentos: links estruturaisou transicio-
nais. Oslinksestruturais,comodizonome,sãoreferentesàestruturadopróprio
conteúdo.Porexemplo,suponhaquevocêbusqueumalistagemdeendereçosdeum
determinadocliente:
36

## Página 43

CasadoCódigo Capítulo3.ConceitosdeREST
<cliente>
<enderecos>
<link href="/cliente/1/endereco/1" title="Endereço comercial" />
<link href="/cliente/1/endereco/2" title="Endereço residencial" />
<link href="/cliente/1/endereco/3" title="Endereço alternativo" />
</endereco>
</cliente>
Esteslinksproduzemdiversosbenefíciosparaocliente.
Oprimeirobenefício,etalvezomaisóbvio,éareduçãodoacoplamentoentre
oclienteeoservidor,jáqueoclientepodeseguiresteslinksparadescobrironde
estãoosendereços.CasoaURLdeendereçosmude,oclientenãodeverásentiros
impactosseseguiros links.
Osegundobenefícioéqueelesexercemumaaçãointeligentedopontodevista
docliente,jáqueestenãoprecisarecuperardadosdequenãoprecisa.Seeleprecisar
apenasdoendereçocomercial,bastaseguirsomenteo linkquecontémoendereço
comercial,enãotodososoutros.
Oterceiroédopontodevistadaperformance.Alémderecuperarumvolume
menordedados,emcasodeumalista(comonesteexemplo,deendereços),ocliente
podeparalelizarasrequisições e,assim,diminuirotempodeobtençãodasinforma-
ções. Obviamente,issodependedalatênciadarede(ouseja,otempodecorridoem
relaçãoàsaídadarequisiçãodamáquinaclienteechegadaaoservidor,evice-versa),
masissopodebeneficiar-sedocacheamentodorecurso.
Jáoslinkstransicionaissãorelativosaações, ouseja,aações queoclientepode
efetuarutilizandoaquelerecurso.V o c êjáviuesteexemploquandoeumereferíao
pagamentodacompra.
Existemcincoatributosimportantesparaoslinks:
•href
•rel
•title
•method
•type
37

## Página 44

3.6. Sumário CasadoCódigo
Existe alguma especificação para estes links?
Existeumaespecificação formalparatratamentodesteslinkscha-
madaXLink(disponívelemhttp://www.w3.org/TR/xlink/).Osatributos
href, titlee methodestãodefinidoslá.Osoutrossãousadoscomo
convenção.
Oatributo hreffazreferênciaàURLondeorecursoestálocalizado(apenas
comolembrete,estaURLpodeserabsoluta-comespecificaçãodeprotocolo, host,
porta,etc.-ourelativa-ouseja,oclientedevebuscarorecursonomesmoservidor
ondefezaprimeirarequisição.
Oatributo reléutilizadocomumtextodeauxílioparaouso,quenãodeve
serlidopeloclientefinal. Ovalordesteatributodeveserutilizadopelocliente
paradetectarotipodeinformação presentenaURL.Porexemplo,oNetflixuti-
lizaURL’spararealizarestadistinção,algocomohttp://schemas.netflix.com/catalog/
people.directors. Casotenhacuriosidade,consulteaURLhttp://developer.netflix.
com/docs/REST_API_Reference-ondeestápresenteadocumentaçãodereferência
parautilizaçãodaAPIdoNetflix.
Oatributo titlecontémumadescrição,legívelporhumanos,dainformação
queestápresentenaURL.
Oatributo methodéumdostiposmenosutilizados;quandooé,indicaquais
tiposdemétodosHTTPsãosuportadospelaURL(separadosporvírgula).
Finalmente,oatributo typeindicaquais media typessãosuportadospelaURL,
etambémsãodosmenosutilizados.
3.6 Sumário
V o c êconheceu,nestecapítulo,astécnicasbásicasdeREST-ouseja,oqueénecessá-
rioconhecerantesdecomeçaratrabalharcomREST.Obviamente,muitasquestões
aindanãoforamrespondidas-comolidarcomclientesconcorrentes?Comotraba-
lharcom cache?Comomodelarcasosmaisavançados?
Aolongodospróximoscapítulos,vocêconheceráarespostaparaestaseoutras
questões. V a m o semfrente?
38

## Página 45

Capítulo4
Tip osdedados
“Conhecimentoépoder”
–FrancisBacon
Paratrabalhardemaneiraeficientecomseusdados,énecessárioconhecer,an-
tes,ostiposdedadosmaiscomunsaseremutilizados-suasvantagens,desvantagens,
usosmaiscomuns,etc.Alémdisso,énecessáriosabercomoutilizá-losnasualin-
guagemdeprogramação.
4.1 XML
XMLéumasiglaquesignifica eXtensible Markup Language,ou linguagem
de marcação extensível. Porterestanaturezaextensível,conseguimosexpressar
grandepartedenossasinformações utilizandoesteformato.
XMLéumalinguagembastantesemelhanteaHTML( HyperText Markup
Language),porém,comsuasprópriasparticularidades.Porexemplo,todoarquivo

## Página 46

4.2. FerramentalXML:conhecendoosXMLSchemas CasadoCódigo
XMLtem um e apenas umelemento-raiz(assimcomoHTML),comadiferençade
queesteelemento-raizéflexívelobastanteparaterqualquernome.
Alémdisso,umXMLtemseções específicasparafornecimentode instruçõ e sde
processamento-ouseja,seções queserãointerpretadasporprocessadoresdeXML
que,noentanto,nãofazempartedosdados.Estasseções recebemosnomesde p r ó -
logo(quandoestãolocalizadasantesdosdados)e epílogo,quandoestãolocalizadas
depois. Porexemplo,écomumencontrarumprólogoquedeterminaaversão do
XMLeo charsetutilizado.Esteprólogotemoseguinteformato:
<?xml version="1.0" encoding="UTF-8" ?>
Ouseja,diferentede t ag sregularesdeXML(quetêmoformato <tag></tag>),
umainstruçãodeprocessamentotemoformato <?nome-da-instrução ?>.No
exemplo,euestouespecificandoaversãodeXMLutilizada(1.0)eo charset(UTF-8).
Aforaestainformação,asestruturasmaisbásicasemumXMLsãoas t ag seos
atributos,deformaqueumXMLsimplestemoseguinteformato:
<?xml version="1.0" encoding="UTF-8" ?>
<tag atributo="valor">conteúdo da tag</tag>
Comoobservadonoexemplo,osdadostransportadospelasuaaplicação po-
demestarpresentestantonaformadeatributoscomodeconteúdodas t ag s.Emum
exemplomaispróximodo casedecervejaria,umacervejapodesertransmitidada
seguinteforma:
<?xml version="1.0" encoding="UTF-8" ?>
<cerveja id="1">
<nome>Stella Artois</nome>
</cerveja>
4.2 Ferramental XML: conhecendo os XML Schemas
Porserumformatoamplamenteutilizadopordiversostiposdeaplicação,XMLcon-
témdiversostiposdeutilitáriosparaváriosfins,asaber:
•Validaçãodeformatoeconteúdo;
•Buscadedados;
•Transformação
40

## Página 47

CasadoCódigo Capítulo4. Tiposdedados
A ferramenta XML mais utilizada quando se trata de XML são os XML
Schemas.Trata-sedearquivoscapazesdedescreveroformatoquemumdetermi-
nadoXMLdeveter(lembre-se,XMLéflexívelapontodepermitirqualquerinfor-
mação).U mXML Schema,comoumtodo,éanálogoàdefiniçãodeclassesemJava:
define-seospacotes(que,emum XML Schema,sãodefinidoscomo namespaces)e
asclasses,propriamenteditas(que,em XML Schemas,sãoostipos).
Utiliza-se XML Schemasparaquetantooclientequantooservidortenhamum
“acordo”arespeitodoqueenviar/receber(emtermosdaestruturadainformação).
Porexemplo,suponhaquecadaumadascervejariaspossuaumanodefundação,
assim:
<cervejaria>
<fundacao>1850</fundacao>
</cervejaria>
Seoclientenãotiverumareferênciaarespeitodoqueenviar,elepodeenviaros
dadosassim:
<cervejaria>
<anoFundacao>1850</anoFundacao>
</cervejaria>
Noteque,destaforma,ainformaçãonãoseriainteligíveldopontodevistado
clientee/oudoserviço.Assim,paramanteramboscientesdoformatoaserutilizado,
pode-seutilizarum XML Schema.
U mXML Schemasimplespodeserdefinidodaseguinteforma:
<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema"
targetNamespace="http://brejaonline.com.br/comum/v1"
xmlns:tns="http://brejaonline.com.br/comum/v1">
</schema>
U mXML Schemaésempredefinidodentroda t ag schema. Esta t agdeve
conter,obrigatoriamente,areferênciaparao XML Schema http://www.w3.org/2001/
XMLSchemaeoatributo targetNamespace,queapontaqualdevesero namespace
utilizadopeloXMLqueestiversendovalidadoporeste XML Schema.Alémdisso,
porconvenção,opróprio namespaceéreferenciadonodocumentoatravésdadecla-
ração xmlns:tns,indicandoqueoprefixo tnspoderáserutilizadonoescopo
deste XML Schema.Estapráticanãoéobrigatória,masésemprerecomendada.
41

## Página 48

4.2. FerramentalXML:conhecendoosXMLSchemas CasadoCódigo
Aestruturadosdados,em XML Schemas,sãodefinidasemtermosde elemen-
t o s.Oselementossãoutilizadosparadefinirinformações arespeitodas t ag s:nome
da t ag,númeroderepetições permitido,quais sub-tagssãopermitidas,quaisatribu-
tosuma t agdeveter,etc.
Paradefinirumelementodentrodeum XML Schema, bastautilizara t ag
element.Porexemplo,paradefiniruma t ag nomenum XML Schema,bastautili-
zaroseguinte:
<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema"
targetNamespace="http://brejaonline.com.br/comum/v1"
xmlns:tns="http://brejaonline.com.br/comum/v1">
<element name="nome" type="string" />
</schema>
Conformemencionadoanteriormente,adefiniçãodosdadospropriamentedi-
toséfeitaatravésdetipos.Estestipossãodivididosentresimplesecomplexos,sendo
ossimplesaquelesquesão strings,datas,númerosouderivadosdestes;jáoscomple-
xos,sãodefinidosapartirdajunçãodeelementosdetipossimplese/ououtrostipos
complexos.
Tiposnovospodemsercriadosouestendidosàvontade,sejamestestipossim-
plesoucomplexos.Porexemplo,paracriarumtiposimplesnovo,bastautilizaro
seguinte:
<simpleType name="CEP" />
Nestemesmo schema,umtipocomplexopodesercriadodaseguinteforma:
<complexType name="Endereco">
<sequence>
<element name="cep" type="tns:CEP" />
<element name="logradouro" type="string" />
</sequence>
</complexType>
Notequeadefiniçãodotipocomplexoenvolvea t ag sequence.Esta t agéuti-
lizadaparadeterminarqueoselementosnelaenvolvidosdevemserinseridosnesta
ordem.Porexemplo,aoimplementarestetipocomplexo,oseguinteéaceito:
<endereco>
<cep>12345-678</cep>
42

## Página 49

CasadoCódigo Capítulo4. Tiposdedados
<logradouro>Rua das cervejas</logradouro>
</endereco>
Porém,oinversonãoéaceito:
<endereco>
<logradouro>Rua das cervejas</logradouro>
<cep>12345-678</cep>
</endereco>
Definindo formas de validação p a r atipos simples
Ostipossimples,comoditoantes,oferecemextensibilidadeemrelaçãoaoutros
tipossimples.Estaextensãopodeserfeitaparaosfinsmaisdiversos,sendoqueo
usomaiscomumdestafacilidadeéparaproverrestrições sobreestestipossimples.
Porexemplo,nocasodoCEP,sabemosqueestesegueumaestruturabemclarade
validação,queéopadrão cinco dígitos (traço) três dígitos.Ouseja,
umaexpressãoregularpodeserutilizadaparaestavalidação.
Estarestriçãoérepresentadautilizando-sea t ag restriction.Esta t ag,por
suavez,possuiumatributo base,queéutilizadoparaindicarqualseráo“tipopai”
aserutilizadoporestedado.Porexemplo,nocasodeumCEP,otipoaserutilizado
comotipopaiserá string. Assim,oelemento CEPpodeserrepresentadoda
seguinteforma:
<simpleType name="CEP">
<restriction base="string">
</restriction>
</simpleType>
Finalmente,dentroda t ag restrictionéquepodemosdefinirotipoderes-
triçãoqueseráaplicadaaoutilizarestetipo.Podemosdefinirumasériederestrições,
comoenumerações dedados(ouseja,sóépossívelutilizarosvaloresespecificados),
comprimentomáximodastring,valoresmáximosemínimosquenúmerospodem
ter,etc.Comoqueremosutilizarumaexpressãoregular,utilizamosa t ag pattern,
quedefineumatributo value. Atravésdesteatributo,especificamosaexpressão
regular.
Assimsendo,definimosonossotipoCEPdaseguinteforma:
<simpleType name="CEP">
<restriction base="string">
43

## Página 50

4.2. FerramentalXML:conhecendoosXMLSchemas CasadoCódigo
<pattern value="\d{5}-\d{3}" />
</restriction>
</simpleType>
Expressões regulares
Expressõesregularessãoutilizadasparadeterminarformatosquecer-
tasstringsdevemter.Porexemplo,estasexpressõespodemserutilizadas
paravalidarendereçosdee-mail,númerosdecartão decrédito,datas,
etc. Porserumassuntodemasiadocomprido(querendemlivrosape-
nassobreisso),melimitoaquiaapenasexplicarosignificadodopadrão
acima.
Osímbolo \dsignificaumdígito(qualquerum).Aoterosinal {5}
anexado,indicaquecincodígitossão aceitos. Otraçorepresentaasí
próprio.
Explorando tipos complexos
Comoapresentadoanteriormente,umtipocomplexo,emum XML Schema,é
semelhanteaumaclasseJava. Porexemplo,adefinição deumendereçopodeser
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
Ostiposcomplexoscomportamdiversasfacilidades,comoherançaedefinição
deatributos.Porexemplo,considereotipocomplexo Pessoa:
<complexType name="Pessoa">
</complexType>
44

## Página 51

CasadoCódigo Capítulo4. Tiposdedados
Supondoqueuma Pessoasejaumasuperdefinição paraumapessoafísica
oujurídica,queremosqueotipo Pessoasejaabstrato.Assim,podemosdefiniro
atributo abstract:
<complexType name="Pessoa" abstract="true">
</complexType>
Noteque,destaforma,nãohaveráumaimplementaçãodoquefordefinidoneste
tipo,apenasdeseussubtipos.Paracriarumaextensãodestetipo,utiliza-seas t ag s
complexContente extension,assim:
<complexType name="PessoaFisica">
<complexContent>
<extension base="tns:Pessoa">
</extension>
</complexContent>
</complexType>
Assim,épossíveldefinirelementostantonosupertipoquantonosubtipo.Por
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
Assim,aimplementaçãodestetipopodeficarassim:
<pessoaFisica>
<nome>Alexandre</nome>
45

## Página 52

4.2. FerramentalXML:conhecendoosXMLSchemas CasadoCódigo
<cpf>123.456.789-09</cpf>
</pessoaFisica>
Alémdisso,épossíveldefiniratributosnostiposcomplexos.Porexemplo,con-
sidereoseguinte:
<complexType name="Pessoa" abstract="true">
<attribute name="id" type="long" />
</complexType>
Assim,aimplementaçãodestetipoficariaassim:
<pessoaFisica id="1" />
U mXML Schematambémpodeimportaroutros,notavelmentepararealizar
composições entreváriostiposdiferentes.Porexemplo,considereasduasdefinições
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
Notequeeste XML Schemapossuio targetNamespacedefinidocomohttp:
//brejaonline.com.br/endereco/v1.
Agora,considereumsegundo XML Schema:
46

## Página 53

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
pessoa/v1(ouseja,diferentedo namespacedeendereços).
Parautilizaro XML Schemadeendereçosno XML Schemadepessoas,éne-
cessárioefetuardoispassos:oprimeiro,édefinirumprefixoparao namespacede
endereços.Porexemplo,paradefiniroprefixo end,utiliza-seoseguinte:
<?xml version="1.0" encoding="UTF-8"?>
<schema targetNamespace="http://brejaonline.com.br/pessoa/v1"
xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:tns="http://brejaonline.com.br/pessoa/v1"
xmlns:end="http://brejaonline.com.br/endereco/v1">
47

## Página 54

4.2. FerramentalXML:conhecendoosXMLSchemas CasadoCódigo
<!-- restante -->
</schema>
Opróximopassoéinformaraomecanismoalocalizaçãodooutro XML Schema,
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
Assim,parautilizarostiposdefinidosnonovoarquivo,bastautilizaroprefixo
end:
<complexType name="Pessoa">
<sequence>
<element name="endereco" type="end:Endereco" />
</sequence>
</complexType>
Ostiposcomplexostambémpodemdefinironúmerodeocorrênciasdeseus
elementos.Porexemplo,paradeterminarqueumelementotemnúmeromínimode
ocorrênciaszero(ouseja,éopcional),utiliza-sea tag minOccurs:
<complexType name="Pessoa">
<sequence>
<element name="endereco" type="end:Endereco" minOccurs="0"/>
</sequence>
</complexType>
Damesmaforma,épossívelutilizara tag maxOccursparadeterminaronú-
meromáximodeocorrências(ouseja,queumdadoelementorepresentaumalista).
Onúmeromáximodeocorrênciaspodeserdelimitadoapartirdeumnúmerofixo
ou,casonãohajaumlimitedefinido,utiliza-seovalor unbounded. Assim,para
determinarqueumapessoapossuiváriosendereços,pode-seutilizaroseguinte:
48

## Página 55

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
<logradouro>Rua Dois</logradouro>
</endereco>
</pessoaFisica>
Aesteponto,vocêdeveternotadoqueoelementoraiz pessoaFisicanão
foiespecificado. Oelementoraizédefinidoforadetiposemum XML Schema,
utilizandoa t ag element.Destaforma,épossívelteroseguinte:
<complexType name="PessoaFisica">
<!-- definição de pessoa física -->
</complexType>
<element name="pessoaFisica" type="tns:PessoaFisica" />
4.3 Trabalhando co m XML utilizando J A X B
AAPI(ApplicationProgrammer Interface)padrãoparatrabalharcomXML,emJava,
éoJAXB(J a v aArchitecture for XML Binding). EstaAPItrabalhaessencialmente
comanotações sobreclassesJava,quedãoinstruções arespeitodecomoconverter
osdadosemXMLatravésdageraçãode XML Schemas.
Paratransformarum XML SchemaemclassesJavacompatíveiscomJAXB,
existeum utilitáriopresentena JDKchamado xjc. Supondoqueseus XML
Schemas estejamestruturadoscomoMaven,ouseja, presentesemumapasta
src/main/resources,épossívelcolocarestasclassesnapastacertausandooar-
gumento -d:
49

## Página 56

4.3.TrabalhandocomXMLutilizandoJAXB CasadoCódigo
xjc -d ../java Pessoa.xsd
Oquedeveproduzirumaestruturacomoaseguinte:
Figura4.1:Arquivosgeradospeloxjc
Como vocêpode observar, uma classe para cada tipo complexo presente
nos XML Schemas foigerada, alémdasclasses ObjectFactory eoarquivo
package-info.java.Elesatuam,respectivamente,comoumaclassefábricapara
objetosrecém-criados(ouseja,seráutilizadonomomentodatraduçãoXML->Java)
ecomoummecanismodefornecimentodeinformações válidasparatodoopacote.
50

## Página 57

CasadoCódigo Capítulo4. Tiposdedados
O arquivo package-info.j a v a
EstearquivoépadronizadopelaespecificaçãoJava(ouseja,nãoédefi-
nidopelaespecificaçãoJAXB).Elecontémapenasadeclaraçãodenome
dopacote,compossíveisanotações. NocasodoJAXB,estearquivoé
geradocomaanotação @XMLSchema,quetrazinformações queserão
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
Aanotação @XMLAcessorTypeindicaparaoJAXBqualomecanismoaser
utilizadopararealizaratradução dosdadosparaXML.Comoa enginedoJAXB
utilizaaAPIde reflectionspararealizarestemapeamento,oacessoaosdadospode
serfeitotantodiretamentepelovalordosatributospresentesnaclasse(sejamestes
privadosounão)comopor getterse setters.
AAPIdisponibilizaquatroformasdistintasdeacesso:
•Porcampos:mapeiatodososatributosdeclasse,independentedesuavisibili-
dadeedeestaremanotadoscomanotações doJAXB.Casonãoestejammape-
adoscomnenhumainformaçãoarespeitodenomenclatura,serãomapeados
51

## Página 58

4.3.TrabalhandocomXMLutilizandoJAXB CasadoCódigo
comonomedoprópriocampo.Ficamexcluídosdestaapenasatributosestá-
ticosouquesejamdefinidoscomo transient;
•Porpropriedades: a enginedetecta getterse settersemapeiatodosospares
encontrados;
•Pormembrospúblicos:mapeiatodasos getterse settersquetenhamvisibili-
dadeajustadapara publicetambémtodososatributosdeclassepúblicos.
Esteéopadrão,quandonenhumdosoutrostiposédefinido;
•Nenhum:mapeiaapenasosmembrosqueestejamanotadoscomanotações
doJAXB.
Aanotação XmlTypeéutilizadanomomentodaconversãodasclassesem XML
Schemas.Elafazmençãodiretaaousodetiposcomplexosem XML Schemas,e
éutilizada,nestecontexto,paradescreveronomedotipocomplexoeaordemdas
propriedades(quedevem,obrigatoriamente,estarpresentesnaclasse).
Aanotação XmlElementéutilizadaparadeclararapropriedadecomoelemento
(queéocomportamentopadrão)eoutraspropriedadesarespeitodoelemento,como
aobrigatoriedadedeseterconteúdo,onomedoelemento,valorpadrão,etc.Neste
caso,comooelemento cpfnãotevedeclaradoonúmeromínimodeocorrências
comozero,foiassumidoovalorpadrão, um. Assim,oJAXBentendeoelemento
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

## Página 59

CasadoCódigo Capítulo4. Tiposdedados
protected List<Endereco> endereco;
@XmlAttribute(name = "id")
protected Long id;
// getters e setters
}
Comovocêpodenotar,aclasse Pessoaéabstrata.Istoédevidoaofatodeotipo
complexotersidodeclaradotambémcomoabstrato,easduascoisassãoequivalentes
emcadacontexto(istoé,umaclasseabstratanãopoderserinstanciada,emJava,e
umtipocomplexonãopoderserdiretamenteutilizadoemXML).
Sendoumaclasseabstrata,oJAXBprecisasaberquaissãosuassubclassespara
quea enginetenhacondições defazeromapeamentoXML->Javaadequadamente.
ComopróprialinguagemJavanãopermitetaldetecção,entraemcenaaanotação
@XmlSeeAlso,queindicaparaa engineJAXBquaisclassesestãorelacionadasaesta
(nocaso,aclasse PessoaFisica,vistaanteriormente).
Outraanotaçãonovaé @XmlAttribute.Estaanotaçãoindicaqueoatributo
daclasseémapeadocomoumatributoXML,enãocomoelemento(comportamento
padrão).
Alémdisso,noteapresençadoatributo endereco,quefoidefinidocomouma
lista. Estecomportamentoédevidoaofatodequeoelemento endereco,decla-
radocomnúmeromínimodeocorrênciasigualazeroesemlimitesuperior-oque,
automaticamente,caracterizaoelementocomoumalista.
Alémdisso,notequeaclasse Enderecoestásendoutilizada,masnãodeclarada
naanotação @XmlSeeAlso. Istoédevidoaofatodeque,comoestaclassejáé
referenciadapeloprópriocódigo(ouseja,nadeclaração List<Endereco>),nãoé
necessáriorealizaradeclaraçãonaanotação.
O arquivo package-info.java
Oarquivo package-info.javadevetersidogeradocomoseguintecon-
teúdo:
@javax.xml.bind.annotation.XmlSchema
(namespace = "http://brejaonline.com.br/pessoa/v1",
elementFormDefault = javax.xml.bind.annotation.XmlNsForm.QUALIFIED)
package br.com.brejaonline.pessoa.v1;
53

## Página 60

4.4. TestandooXMLgerado CasadoCódigo
Noteque,conformeexplicadoanteriormente,apenasadeclaraçãodonomedo
pacoteépermitidanestearquivo.Assim,aanotação @XmlSchemacontémdados
quesãocomunsatodasasclassesdopacote,ouseja,adeclaraçãodo namespaceeo
formatodosdados,queéqualificado.
XML qualificadoversus XML n ã o -qualificado
QuandodizemosqueumXMLéqualificado,nosreferimosaofor-
matofinalcomqueeleseráformado.EmumXMLqualificado,todosos
elementosdevemmencionaraqual namespacepertencem,porexemplo:
<pes:pessoaFisica xmlns:pes="http://brejaonline.com.br/pessoa/v1">
<pes:cpf>123.456.789-09</pes:cpf>
</pes:pessoaFisica>
Noteapresençadoprefixo pesnoatributo cpf.SeoXMLnãofosse
qualificado,elepoderiaserescritodaseguintemaneira:
<pes:pessoaFisica xmlns:pes="http://brejaonline.com.br/pessoa/v1">
<cpf>123.456.789-09</cpf>
</pes:pessoaFisica>
Nestecaso,ofatodenão serqualificadoimplica,automaticamente,
queo namespacedoelemento cpféigualaode pessoaFisica,ou
seja, http://brejaonline.com.br/pessoa/v1.
ÉsempreumaboapráticautilizarXML’squalificados.
4.4 Testando o XML gerado
ParatestaroformatodosdadosqueseráproduzidopeloJAXB,existeumaclasseuti-
litáriachamada javax.xml.bind.JAXB.Elatemmétodospararealizar marshal
(ouseja,transformaçãodasclassesJavaemXML)e unmarshal(ouseja,transforma-
çãodeXMLemJava).
Alerta sobre a classe j a v a x.xml .bind.JAXB
Comopodeserconferidonaprópriadocumentaçãodestaclasse,esta
deveserutilizadaapenasparatestes,nãoparaprodução.
54

## Página 61

CasadoCódigo Capítulo4. Tiposdedados
Pararealizaroteste,bastainstanciarumobjetodeumaclasseanotadacomJAXB
eutilizarométodomarshal,passandoesteobjetoeuma s t re amcomoparâmetros.
Porexemplo,paramostraroresultadonoconsole,bastautilizaroseguintecódigo:
public static void main(String[] args) {
PessoaFisica pessoaFisica = new PessoaFisica();
pessoaFisica.setCpf("12345678909");
pessoaFisica.setNome("Alexandre Saudate");
Endereco endereco = new Endereco();
endereco.setCep("12345-678");
pessoaFisica.getEndereco().add(endereco);
JAXB.marshal(pessoaFisica, System.out);
}
Deacordocomocódigoacima,oseguintedeveserapresentado:
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
muitotrabalhosogerarum.Nestescasos,épossíveltrabalharcomJAXBsemutili-
zar XML Schemas.Paraisto,bastagerarasclassesaseremutilizadasnormalmente
eutilizaraanotação javax.xml.bind.annotation.XmlRootElement.
Nestecaso,podemosrefatoraraclasse PessoaFisica,porexemplo,paraser
araiz,erefatoramostodaaestruturapararemoverosarquivosprópriosdoJAXB
(ouseja,asclasses ObjectFactorye package-info).Aestrutura,então,fica
noseguinteformato:
Asclassestambémforamrefatoradas,paraficarcomoseguinteformato:
55

## Página 62

4.5.UtilizandoJAXBsemumXMLSchema CasadoCódigo
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
Eaclassequeirámodelaroendereço:
public class Endereco {
private String cep;
private String logradouro;
}
Oresultadodotesteficasemelhanteaoanterior:
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<pessoaFisica id="1">
56

## Página 63

CasadoCódigo Capítulo4. Tiposdedados
<endereco>
<cep>12345-678</cep>
</endereco>
<nome>Alexandre Saudate</nome>
<cpf>12345678909</cpf>
</pessoaFisica>
4.6 JSON
JSONéumasiglapara JavaScript Object Notation. Éumalinguagemdemarcação
criadaporDouglasCrockfordedescritonaRFC4627,eservecomoumacontrapar-
tidaaXML.T e mporprincipalmotivaçãootamanhoreduzidoemrelaçãoaXML,e
acabatendousomaispropícioemcenáriosondelarguradebanda(ouseja,quanti-
dadededadosquepodesertransmitidaemumdeterminadointervalodetempo)é
umrecursocrítico.
Atendeaoseguintemodelo:
•U mobjetocontémzerooumaismembros
•U mmembrocontémzerooumaisparesezerooumaismembros
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
Casosejaumalistagem,oformatoéoseguinte:
57

## Página 64

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
Notequeasquebrasdelinhaeosespaçosnãosãoobrigatórios-servemapenas
comoelementosparafacilitaravisualização.
T a m b é mvaleapenadestacarqueadeclaração doelementoraiz(comoade-
claração pessoaFisica)éestritamenteopcional.Muitas enginessãocapazesde
trabalharcomapenasosatributosdoelemento.Porexemplo,adefiniçãodepessoa
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
Existemdiversasimplementações de parsersJSONparaJava.Algumasdelassãoas
seguintes:
58

## Página 65

CasadoCódigo Capítulo4. Tiposdedados
•GSON
•Jackson
•Jettison
•XStream
Amaneiradeusodecadaumatemvantagensedesvantagens.U m avantagem
bastanteinteressantedealgumaséacapacidadedeutilizaranotações JAXBcomo
instruções parageração doJSON,gerandoapenasumúnicoesforçoquandoque-
remostrabalhartantocomJSONquantocomXML.Parademonstrarousodes-
tasferramentas,adicioneimaisumcamponaclasse PessoaFisica,chamado
dadoTransiente.Estecampofoianotadocom @XmlTransient,indicandoque
estedadonãodeveserapresentadoquandoo parserutilizarasanotações doJAXB,
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
VejamosocódigocomGSON.Paratransformarumainstânciadestaclasseem
JSONcomGSON,ocódigoaseguiréutilizado:
PessoaFisica pessoaFisica = Parser.criarPessoaFisicaTeste();
Gson gson = new Gson();
System.out.println(gson.toJson(pessoaFisica));
Oqueproduzoseguinteresultado(formatadopormimparaoferecermelhor
legibilidade):
59

## Página 66

4.7.TrabalhandocomJSONutilizandoJAXB CasadoCódigo
{"cpf":"123.456.789-09",
"dadoTransiente":"dadoTransiente",
"nome":"Alexandre",
"endereco":[{"cep":"12345-678","logradouro":"Rua Um"}],
"id":1
}
Comoobservado,éfácilgeraroconteúdoJSONutilizandoGSON;noentanto,
ainformaçãotransienteestápresentenoJSONgerado,ouseja,oGSONnãooferece
suporteàsanotações JAXB.
JáocódigocomJacksonficadaseguinteforma:
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
Destaforma,ainformaçãotransientefoidetectadaeretiradadoJSON.Noen-
tanto,ocódigoestádemasiadocomplicado.
VejamosocódigonecessárioparaavaliarestainformaçãocomJettison:
PessoaFisica pessoaFisica = Parser.criarPessoaFisicaTeste();
JAXBContext context = JAXBContext.newInstance(PessoaFisica.class);
MappedNamespaceConvention con = new MappedNamespaceConvention();
Writer writer = new OutputStreamWriter(System.out);
XMLStreamWriter xmlStreamWriter = new MappedXMLStreamWriter(con, writer);
Marshaller marshaller = context.createMarshaller();
marshaller.marshal(pessoaFisica, xmlStreamWriter);
Ocódigo utilizadopeloJettisonéaindamaiscomplicado. Noentanto,ele
possuiumaafinidademaiorcomoJAXB(comoobservadopelousodasclasses
JAXBContexte Marshaller,quesãoprópriasdaAPIdoJAXB).Istoérefletido
noresultadodaexecuçãodestecódigo:
60

## Página 67

CasadoCódigo Capítulo4. Tiposdedados
{"pessoaFisica":
{"@id":"1",
"endereco":{"cep":"12345-678","logradouro":"Rua Um"},
"nome":"Alexandre",
"cpf":"123.456.789-09"
}
}
NotequeoJSONgeradoémaissemelhanteaumXML.Estápresenteum
elemento-raiz, pessoaFisica,eoatributo idfoidestacadoatravésdoprefixo
@,indicandoqueesteéequivalenteaumatributoXML.
Finalmente,vejamosocódigoutilizadopeloXStream:
PessoaFisica pessoaFisica = Parser.criarPessoaFisicaTeste();
XStream xStream = new XStream(new JettisonMappedXmlDriver());
System.out.println(xStream.toXML(pessoaFisica));
Aqui,noteoseguinte:o d r i v e rutilizadopeloXStreamparageraçãodoJSONéo
doJettison,ouseja,oXStreamreutilizaoutro fr a mewo r kparageraçãodoJSON.O
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
NotequeoXStream,porpadrão,colocaosnomesdasclassesutilizadasnatradu-
çãoenãorespeitaasanotações doJAXB.T o d aestainformaçãopodesercontrolada,
mascomcódigoeanotações própriasdoXStream.
61

## Página 68

4.8. ValidaçãodeJSONcomJSONSchema CasadoCódigo
4.8 Validação de JSON co m JSON Schema
AssimcomoemXML,JSONtambémpossuiumsistemadevalidação,conhecido
como JSON Schema.Trata-sedeumtipodearquivoque,como XML Schemas,
tambémpossuiumformatopróprioparaespecificaçãodetiposJSON.Essaespeci-
ficaçãoestádisponívelnoseu site,
U mJSON Schemapossuicomodeclaraçãomaiselementaro título(descrito
no JSON Schemacomoumapropriedade title).Otítuloéoquedenominaeste
arquivodevalidação.Porexemplo,supondoquedesejamoscomeçaradescreverum
JSON Schemaparapessoas,odescritivoteráoseguinteformato:
{
"title":"Pessoa"
}
Nasequência,énecessáriodefinir,paraesteformato,o tipo(descritono JSON
Schemacomoumapropridade type).Otipopodeserumdosseguintes:
•array-ouseja,umalistadedados
•boolean-ouseja,umvalorbooleano(trueou false)
•integer-umnúmerointeiroqualquer.NotequeJSONnãodefineumnúmero
de b i t spossível,apenasofatodeserumnúmeropertencenteaoconjuntodos
númerointeiros.
•number-umnúmeropertencenteaoconjuntodosnúmerosreais. Seguea
mesmaregrade integer,sendoque n u m b e rtambémcontempla integers
•null-umvalornulo
•object-ouseja,umelementoquecontémumconjuntodepropriedades
•string-ouseja,umacadeiadecaracteres
Comopessoaéumobjeto,podemosdefinirotipodaseguinteforma:
{
"title":"Pessoa",
"type":"object"
}
62

## Página 69

CasadoCódigo Capítulo4. Tiposdedados
Obviamente,umobjetoprecisaconterpropriedades. Estaspodemserdefini-
dasapartirdaproprieade properties. Porexemplo,sequisermosdefiniruma
propriedade nomeparaumapessoa,podemosutilizaroseguinteformato:
{
"title":"Pessoa",
"type":"object",
"properties":{
"nome": {
"type":"string"
}
}
}
Noteque,definidaapropriedade nome,oconteúdodestepassaateromesmo
formatodaraiz pessoa,ouseja,existeumarecursividade.Épossível,portanto,de-
finirumatributo titledentrodenome,definirnomecomoumobjetocomsub-
propriedades,etc.
Assimsendo,podemos,portanto,definirumelemento enderecodentrode
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

## Página 70

4.8. ValidaçãodeJSONcomJSONSchema CasadoCódigo
Finalmente,valeapenaobservarque,porpadrão,o JSON Schemanãotelimita
aosformatospré-defidos(aocontráriodo XML Schema,queapenasseatémao
definido).Porexemplo,deacordocomo JSON Schemaacima,oseguinteJSON
seriaconsideradoválido:
{
"nome":"Alexandre",
"cpf":"123.456.789-09"
}
Noteque,aindaqueocampo cpfnãoestejadescrito,apresençadomesmonão
invalidaoJSON,tornandooscamposmeramentedescritivos(ouseja,encarados
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
Destaforma,oJSONdescritoseriaconsideradoinválido.
Para realizar os testes de validação JSON, épossível utilizar o programa
disponívelemhttps://github.com/fge/json-schema-validator, ouainda, utilizara
64

## Página 71

CasadoCódigo Capítulo4. Tiposdedados
plataforma onlinedeste, disponívelatéa data da escrita deste livro em http://
json-schema-validator.herokuapp.com/.
Paragerarcódigo apartirdeste JSON Schema,épossívelutilizarumpro-
gramadisponívelemhttps://github.com/joelittlejohn/jsonschema2pojo.Estepro-
gramaestádisponível,atéadatadeescritadestelivro,sobosformatos online(em
http://www.jsonschema2pojo.org/),como pluginMaven,como pluginGradle,como
tarefaAnt,comoumprogramadelinhadecomandooucomumaAPIJava.
Sepreferir,podeconfigurarnoMavencomaseguinteinstrução:
<build>
<plugins>
<plugin>
<groupId>com.googlecode.jsonschema2pojo</groupId>
<artifactId>jsonschema2pojo-maven-plugin</artifactId>
<version>0.3.7</version>
<configuration>
<sourceDirectory>${basedir}/src/main/resources/schema</sourceDirectory>
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
Alémdisso, tambémépreciso configurar dependênciascom os artefatos
common-lange jackson-databind,queserão utilizadosnasclassesgeradas.
OXMLutilizadopormimparaconfiguraçãodestasdependênciasfoi:
<dependency>
<groupId>commons-lang</groupId>
<artifactId>commons-lang</artifactId>
<version>2.4</version>
</dependency>
<dependency>
<groupId>com.fasterxml.jackson.core</groupId>
65

## Página 72

4.9. Conclusão CasadoCódigo
<artifactId>jackson-databind</artifactId>
<version>2.0.0</version>
</dependency>
Destaforma,bastaexecutarocomando mvn generate-sourcesparaqueas
classes Pessoa(cujonomeégeradoapartirdonomedoarquivo-nomeucaso,
Pessoa.json)e Endereco(nomedefinidoapartirdapropriedade endereco).
Figura4.2:ClassesgeradaspeloplugindoMavenparaJSONSchema
4.9 Conclusão
Nestaseção,vocêconheceumaisarespeitodosformatosmaisutilizadosemREST,
ouseja,XMLeJSON.V o c êconheceumaisarespeitodoecossistemaqueoscerca,ou
seja,nocasodoXML, XML SchemaseJAXB.NocasodeJSON,os JSON Schemas
easferramentashabilitadasatrabalharemcomesteformato.
66

## Página 73

CasadoCódigo Capítulo4. Tiposdedados
Destemomentoemdiante,vocêjátememmãososmeiosqueserãoutilizados
paraconstruçãodeserviçosREST,ouseja,vocêjáconheceosprincípiosdeRESTe
jásabeutilizarostiposdedadosdisponíveisparautilizaçãodeste.Masaindafaltao
primordial:comocombinartudoisso?
Nopróximocapítulo,vocêverácomocombinaressatécnicaatravésdautilização
de servletsJava.Maisadiante,vocêverácomoutilizarAPI’saindamelhores.V a m o s
emfrente?
67

## Página 75

Capítulo5
ImplementandoserviçosRESTem
J a v acomServlets
“ Oú n i c ohomem q u enão erra éaquele q u enunca f e znada”
–FranklinRoosevelt
AgoraquevocêjáconheceosconceitosondeRESTestáenvolvido,estánahora
devercomoimplementaristoemumsistemareal.Comojáépraxe,voucomeçar
pelaformamaissimplese,depois,partiremosparaaimplementaçãousandoAPI’s
própriasparaconstruçãodeserviçosREST.
5.1 Uma implementação co m Servlets
Oleitorquejátemexperiênciacom servletsJavaprovavelmentejáimaginou,atéaqui,
umaimplementaçãocomestatecnologia.Mesmoseforesteoseucaso,leiaestaseção
atéofim-podetetrazerinformações úteismesmoarespeitodofuncionamentodo
mecanismodaAPIRESTdeJava.

## Página 76

5.1.UmaimplementaçãocomServlets CasadoCódigo
Senãoforocaso,saibaqueaespecificaçãoJavaEEpossuidefinidaousode ser-
vlets,ouseja,trechosdecódigoespecíficosparaseremexecutadosnoladodoservi-
dor.Os servletssão,pornatureza,construídosparaatenderemaqualquerprotocolo
deaplicação quesejatransmitidopelarede;noentanto,existeumaextensão des-
tesparatrabalharespecificamentecomoprotocoloHTTP,queéjustamenteoque
precisamos.
Estaextensãoéaclasse javax.servlet.http.HttpServlet,quepossuios
métodosconhecidoscomo doXXX(ondeXXXéonomedeummétodoHTTP).Por
exemplo,paraatenderaumarequisiçãoqueuseométodo GET,pode-seestendera
classe HttpServleteimplementarométodo doGet,assim:
package br.com.brejaonline.servlets;
import javax.servlet.http.*;
public class CervejaServlet extends HttpServlet {
public void doGet (HttpServletRequest req, HttpServletResponse resp)
throws ServletException, java.io.IOException {
// Coloque aqui a implementação do seu código
}
}
Estemétodovaicarregar,então,aimplementaçãodoquesedesejaparaumser-
viçoREST.Lembre-sedequeométodoGETéutilizadopararealizarbuscasnolado
doservidor.Sendoesteum servletquebuscadadosdecervejas,deve-seimplementá-
lodemaneiraarealizarestaação.
V a m o sutilizar,aqui,umconceitopresenteem Domain-Driven Design,queéode
repositório:umaclassedenegócioespecializadanoarmazenamentodeentidades
denegócio.
70

## Página 77

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
O que é Domain -Driven Design
Domain-Driven Designsignifica,numatraduçãolivre, designorien-
tadoaodomínio.Istoquerdizer,numasimplificaçãogrosseira,queas
classesquevocêconstruirdevemsempreatenderaomáximopossível
objetivosdenegócio-oquepodesertraduzido,porexemplo,eminser-
ção decomportamentodenegócionasentidadesqueserão persistidas
nobancodedados,oquetrazganhosemtermosdecoesãodosobjetos.
Parasabermais,sugirolerolivrodeEricEvans,Domain-DrivenDesign
-AtacandoAsComplexidadesnaCriaçãodoSoftware.
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
Aseguir,vamosrealizaradefinição donossorepositóriodecervejas(ouseja,
umestoquedecervejas):
package br.com.brejaonline.model;
import java.util.*;
public class Estoque {
private Collection<Cerveja> cervejas = new ArrayList<>();
71

## Página 78

5.1.UmaimplementaçãocomServlets CasadoCódigo
public Collection<Cerveja> listarCervejas() {
return new ArrayList<>(this.cervejas);
}
public void adicionarCerveja (Cerveja cerveja) {
this.cervejas.add(cerveja);
}
}
V a m o sincrementaronossoestoqueparacomeçarcomalgumascervejas(afinal
decontas,ninguémgostadeumestoquevazio:) ). Paraisso,vamosmodificara
classe Cervejaparacriarumconstrutorparaarmazenarosparâmetrose,depois,
modificaroconstrutordeestoqueparacriarestascervejas.Então,aclasse Cerveja
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
Eaclasse Estoqueficaassim:
public class Estoque {
private Collection<Cerveja> cervejas = new ArrayList<>();
public Estoque() {
Cerveja primeiraCerveja = new Cerveja("Stella Artois",
"A cerveja belga mais francesa do mundo :)",
72

## Página 79

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
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
Assim,utilizamosaclasse Estoquenonosso servletdecervejas,ficandoassim:
public class CervejaServlet extends HttpServlet {
private Estoque estoque = new Estoque();
public void doGet (HttpServletRequest req, HttpServletResponse resp)
throws ServletException, java.io.IOException {
// Coloque aqui a implementação do seu código
}
}
Ma seste exemplo n ã o segue o MVC...
Obviamente,esteexemplonão ébomnoquesito“acoplamento”.A
idéia,aqui,éapenasserdidático,enão mostrarumexemploreal. Os
exemplosreaiscompletoserefatoradosestarãodisponíveisalgunscapí-
tulosadiante,aguarde.
Finalmente,parafacilitaranossavidanoquesitodescritividadedacerveja,va-
mossobreescreverométodo toStringdacerveja:
public class Cerveja {
// o código já mostrado anteriormente
public String toString() {
73

## Página 80

5.1.UmaimplementaçãocomServlets CasadoCódigo
return this.nome + " - " + this.descricao;
}
}
Agora,podemosutilizaresteconjuntodemecanismosparalistarnossascerve-
jasapartirdonosso servlet. Paraisso,vamosutilizaromecanismodeimpressão
dos servlets,queéaobtenção deum java.io.PrintWriterapartirdaclasse
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
Resta,agora,realizaromapeamentodeste servletdemaneiraadequada. Se-
guindoospreceitosdeREST,oidealseriamapeá-loparaaURL /cervejaou
/cervejas,jáqueanossanecessidadeébuscarosdadosdascervejaspresentes
nosistema.
Pela especificação 3.0 de servlets, é possível utilizar a anotação
javax.servlet.annotation.WebServlet para descrevê-losperante o
container,criandoomapeamentoadequado.Portanto,nossaclassemapeadapode
ficardaseguinteforma:
// Declaração de package e imports
7 4

## Página 81

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
@WebServlet(value = "/cervejas/*")
public class CervejaServlet extends HttpServlet {
// código
}
Dicade uso
Casotenhadificuldadesemconferirofuncionamentodestecódigo,
bastairnorepositóriodecódigo-fontedolivroemhttps://github.com/
alesaudate/rest,baixarocódigoetestá-loemseuambiente.
Finalmente,paraconferirofuncionamentodocódigo,bastaabrircomonave-
gadoroendereçohttp://localhost:8080/cap-05/cervejaria:
Noentanto,notequealgoestáerrado... paratestaroserviçodeumamaneira
maiscômoda,sugiroainstalaçãodo plugin Poster,paraonavegadorMozillaFi-
refox,disponívelemhttps://addons.mozilla.org/pt-br/firefox/addon/poster/.
Uso outro navegador , o que f a ç o ?
O plugintambémestádisponívelparaoGoogleChrome,emhttp:
//tinyurl.com/chrome-poster.Nãosepreocupe,ousonosdoisnavega-
doresérealizadodamesmaforma.
U m avezinstaladoo pluginnoseuFirefox,bastaabrí-loapontandoparaomenu
Ferramentas(ou T o o l s,dependendodoidiomadoseunavegador)eclicandoem
Poster:
75

## Página 82

5.1.UmaimplementaçãocomServlets CasadoCódigo
Figura5.1:Poster,umpluginparaoFirefox
Como Poster,temosumainterfacegráficaparatestarosnossosserviços!
76

## Página 83

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
Nacaixa URL,insiraaURLdo servletdecervejas,ouseja,http://localhost:8080/
cervejaria/cervejas.Nasequência,cliquenobotão GET.Oresultadodeveaparecer
demaneiraidênticaàmaneiracomoapareceunonavegador.
Porém,algonãoestácerto.Ocabeçalho Content-Typenãoestápresente,ou
seja,nemsequerexisteumadefiniçãodotipodedados.Alémdisso,oresultadofoi
impressocomotextopuro-ouseja,oclientenãoterámeiosparaidentificarostipos
dedadostrafegados,etc.
Ouseja,nossaprimeiramissão éajustarotipodedados. Pararepresentaros
dados,podemosutilizaros MIME T y p e stext/xmlou application/xmlpara
XMLe application/jsonparaJSON.V o c êviunocapítulo4comomanipular
estestipos.Assim,suponhaqueoretornodesejadodessalistagemsejaumconteúdo
XML.Duascoisassãonecessárias:criarumelemento-raizparaoselementosere-
alizarasadaptações paratrafegarestesdadosnoformatodesejado. Paratermoso
menorimpactopossível,portanto,temoscomoopçãomaisfácilutilizaroJAXB:a
APIjávemembutidanasimplementações da V i r t u a lMachineJavaetambémoferece
compatibilidadecomcertosmecanismosgeradoresdeJSON.
Assim,vamoscriarumaclassequeencapsuleasoutrascervejas,denominada
Cervejas. Estaclasseseráapartadadomodelo,eficarálocalizada nopacote
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

## Página 84

5.1.UmaimplementaçãocomServlets CasadoCódigo
motivosimportantesparaexistir:
•Elaseráusadaparaencapsularosoutroselementos;
•Futuramente,utilizaremosessaclasseparaadicionarHATEOAS.
Agora,éhorademodificaraimplementaçãodonosso servletparaqueeleseja
capazdeatenderaosclientes.Paraqueissoaconteça,bastaimplementarnovamente
ométodo doGetnoservlet,comocódigodeescritadexmlvistonocapítulo4:
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

## Página 85

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
Prevenindo problemas
Nocódigoacima,notequeadefinição do Content-Typeacom-
panhaadefinição do charset. Casonão sejadefinido,ocontainer(no
meucaso,o Jetty)normalmenteselecionaumpré-definido.Observe
queaordememqueascoisassãofeitastambéminfluenciaestadefini-
ção -nocasodo Jetty,seesteajusteforfeitodepoisdainvocação a
resp.getWriter,ocontainervaiignoraradefiniçãodo charset.
Observequea enginedoJAXBdepositaoXMLgeradodiretamentenasaída
oferecidapelaAPIde servlets. Paratestarestecódigo,recorremosnovamenteao
Poster:
79

## Página 86

5.1.UmaimplementaçãocomServlets CasadoCódigo
Figura5.2:Enviandoumarequisiçãodetestecomoposter
Arespostaseráaseguinte:
80

## Página 87

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
Figura5.3:Respostatesteposter
5.2 Implementando negociação de conteúdo
Noexemploanterior,aURL /cervejasestáhabilitadaaenviarparaoclienteum
conteúdoapenasemformatoXML.Masoqueacontecesequisermosenviardados
81

## Página 88

5.2.Implementandonegociaçãodeconteúdo CasadoCódigo
deoutrasmaneiras?DigamosqueeuqueiraenviardadoscomoJSON,também,o
quefaço?
AsaídanãoécriarnovasURL’s,massim,implementarumatécnicaconhecida
como negociação de conteúdo.Nestatécnica,oclientedizparaoservidorquetipo
dedadosdeseja(atravésdocabeçalho Accept)e,então,oservidorproduzotipo
deconteúdonoformatodesejado.
Paraimplementarnegociaçãodeconteúdocom servletsémuitofácil;bastain-
vocarométodo HttpServletRequest.getHeader,assim:
String acceptHeader = req.getHeader("Accept");
Apartirdeentão,éprecisotestaroresultado.Lembre-se(deacordocomoca-
pítulo2)queessanegociaçãopodeserpotencialmentecompliada.Paraevitarum
códigodemasiadamentecomplexo,vamosapenastrabalharcoma existênciaounão
deformatosesperadosnestecabeçalho.Assim,testamosprimeiroparaasolicitação
deXML.CasonãohajaXMLnarequisição,testamosparaJSONe,seotestefalhar,
devolvemosocódigodeerro415(aindadeacordocomocapítulo2,significandoque
foisolicitadoumformatodedadosquenãoésuportado).
Ocódigoficaassim:
if (acceptHeader == null || acceptHeader.contains("application/xml")) {
escreveXML(req, resp);
} else if (acceptHeader.contains("application/json")) {
escreveJSON(req, resp);
} else {
// O header accept foi recebido com um valor não suportado
resp.sendError(415); // Formato não suportado
}
Agora,restaescreverosmétodosescreveXMLe escreveJSON.Aestaaltura,
istonãodevesernenhummistérioparavocê;maslistoabaixocasovocêaindatenha
dúvidasarespeito:
private void escreveXML(HttpServletRequest req, HttpServletResponse resp)
throws ServletException, IOException {
Cervejas cervejas = new Cervejas();
cervejas.setCervejas(new ArrayList<>(estoque.listarCervejas()));
try {
82

## Página 89

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
resp.setContentType("application/xml;charset=UTF-8");
Marshaller marshaller = context.createMarshaller();
marshaller.marshal(cervejas, resp.getWriter());
} catch (JAXBException e) {
resp.sendError(500); //Erro interno inesperado
}
}
//Este código assume o Jettison como provedor de mapeamento JSON
private void escreveJSON(HttpServletRequest req, HttpServletResponse resp)
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
Pararesolverestaquestão, orecomendadoémodelaraURLdemaneiraque,
83

## Página 90

5.3.Implementandoabuscaporumacervejaespecífica CasadoCódigo
se o clientefornecero ID da cerveja na URL, apenasuma únicaéretornada.
Porexemplo,seeuquiserbuscaraStellaArtois, possofazê-loatravésdaURL
/cervejas/Stella+Artois(notequeestaURLjáestácodificadaparaserusada
emum browser).
Parafazerisso,noentanto,énecessáriorealizaralgumasmodificações, acome-
çarpelaclasse Estoque:estadevesermodificadaparaencararosnomesdascerve-
jascomoidentificadores.Assim,substituímosaimplementaçãodaclasse Estoque
paraarmazenarascervejasemummapa,enãoemumalista:
private Map<String, Cerveja> cervejas = new HashMap<>();
public Collection<Cerveja> listarCervejas() {
return new ArrayList<>(this.cervejas.values());
}
public void adicionarCerveja (Cerveja cerveja) {
this.cervejas.put(cerveja.getNome(), cerveja);
}
Assim,podemosacrescentarummétodonestaclassepararecuperarascervejas
pelonome:
public Cerveja recuperarCervejaPeloNome (String nome) {
return this.cervejas.get(nome);
}
Opróximopassoéincluirno servletummétodoparaextrairoidentificador(ou
seja,onomedacerveja)daURLenviadapelocliente. Parafazerisso,precisamos
utilizarométodo HttpServletRequest.getRequestURI:
String requestUri = req.getRequestURI();
DepossedaURIinvocada,precisamosextrairoconteúdoqueestádepoisda
últimabarra.MasestaURLpodeterváriosformatos:
•/cervejas
•/cervejas/
•/cervejas/Stella
•/cervejas/Stella+Artois
84

## Página 91

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
Ouseja,precisamosdeummétodoquesejainteligenteosuficienteparaextrair
oquevemdepoisde /cervejas.Existemváriasmaneiradefazerisso;ométodo
criadopormimfoidividira stringpelosseparadores(ouseja, /)e,depois,iterar
pelalistadepedaçosatédetectarocontextodo servlet,ouseja, cervejas. U m a
vezlocalizadoocontexto,ajustaumavariávelbooleanaindicandoque,casohaja
qualquercoisanaURLdepoisdestepedaço,éumidentificador.Ocódigoficaassim:
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
Noentanto,estecódigosólevaemconsideraçãoocasodoidentificadorexistir.
ParaocasodaURLestarcodificada,ouseja,estarcomo Stella+Artois(que,de-
codificado,representa Stella Artois),otratamentoaindanãoestáimplemen-
tado.Masdecodificaréfácil,bastautilizaraclasse java.net.URLDecoder:
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
o mais elegante seria modelar uma exceção própria, algo como
RecursoSemIdentificadorException.Ocódigofinalizadoficaassim:
private String obtemIdentificador(HttpServletRequest req)
throws RecursoSemIdentificadorException {
85

## Página 92

5.3.Implementandoabuscaporumacervejaespecífica CasadoCódigo
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
throw new RecursoSemIdentificadorException("Recurso sem identificador");
}
Opróximopassoéalterarosmétodosdebuscaparatrataremoenviotantode
uma Cervejaquantodaclassequepodecontertodas,ouseja, Cervejas.Para
isso,bastacriarummétodopararealizaralocalização.Comoestasclassesnãopos-
suemparentescoentreelas,utilizamosaclasse Objectcomoretornodométodo:
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

## Página 93

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
return objeto;
}
Finalmente,bastaalterarosmétodosdeescritaparautilizaremestenovomé-
todo.Observequeexisteumapossibilidadedoobjetoretornadosernulo,ouseja,
casoumidentificadortenhasidofornecidomasoobjetonãotenhasidolocalizado
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
Ma sé possívelenviar u m Object para o J A X B?
Sevocêteveumadúvidaemrelaçãoaoenviodaclasseparaométodo
marshal,vocêestáindonocaminhocerto:).Naverdade,nestecaso
estamosconfiandosemprequeoobjetoaserenviadoparaestemétodo
écompatívelcomJAXB,eestefaráadetecçãoem t e m p ode execução,
enãoemtempodecompilação.Destaforma,podemospassarqualquer
objetoparaométodo marshale,casoestenão sejacompatível,uma
JAXBExceptionserálançada.
87

## Página 94

5.3.Implementandoabuscaporumacervejaespecífica CasadoCódigo
Agora,bastatestar.U s enovamenteo Poster,passandoaURL http://localhost:
8080/cervejaria/cervejas/Stella+Artois comoparâmetro.Oseguintedeveráserretor-
nado:
Figura5.4:Retornodotestedoservletdecervejas
88

## Página 95

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
5.4 Implementando a criação de u m recurso
Oseu servletjábuscarecursos,masseráqueestáaptoarealizaracriaçãodestes?
Comovocêviuantes,tipicamenteascriações derecursossão feitasatravésda
utilizaçãodométodo POST.Sendoassim,vocêdeveapenasimplementarométodo
doPostno servlet:
protected void doPost(HttpServletRequest req, HttpServletResponse resp)
throws ServletException, IOException
Paracriaçãoderecursos,vocêtemduasopções demodelagem:fazercomqueo
clientepasseumidentificador,jácriadoporele,oucriaroidentificadornoladodo
servidor.Comonossaaplicaçãoédecervejas,fazsentidodeixarcomqueocliente
crieoidentificador,jáqueosidentificadoresdascervejassãoosnomes.
Co m o acontece em aplicações reais?
NamaiorpartedasaplicaçõesREST,oservidorcriaosidentificadores,
especialmenteseo backenddaaplicaçãoestiverimplementadocomum
bancodedadosrelacionaleosID’ssãogeradosporestebanco.Masvocê
devetomaromáximocuidadopossívelcomestaabordagem,poissua
aplicaçãopodecrescereutilizaroutrostiposdebancodedados.Oideal
équevocêsemprefaçaoprojetodasuaAPIdemaneiraquevocêconsiga
modificarqualquerpartedasuainfra-estrutura.
Destaforma,aprimeiracoisaquevocêteráqueimplementaréarecuperação
doidentificador(istodevesertrivial,jáquevocêjátinhafeitoummétodoparaisto
quandocriouométododerecuperaçãodecervejas).Casooidentificadornãoseja
encontrado,envieumerro400 Bad Requestparaocliente,indicandoqueare-
quisiçãodeveseralteradaere-enviada:
String identificador = null;
try {
identificador = obtemIdentificador(req);
} catch (RecursoSemIdentificadorException e) {
//Manda um erro 400
resp.sendError(400, e.getMessage());
}
89

## Página 96

5.4.Implementandoacriaçãodeumrecurso CasadoCódigo
Opróximotratamentoaserrealizadoéparaocasodacervejajáexistir;neste
caso,umerro409 Conflictdeveserlançado:
if (identificador != null &&
estoque.recuperarCervejaPeloNome(identificador) != null) {
resp.sendError(409, "Já existe uma cerveja com esse nome");
return ;
}
Finalmente,vocêdeverealizaraleituradocorpodarequisiçãoetransformarem
umobjeto Cerveja.Pararecuperarocorpodarequisição,bastaexecutarométodo
HttpServletRequest.getInputStream.Felizmente,orestantedoprocessojá
éfacilitadopeloJAXB:
Unmarshaller unmarshaller = context.createUnmarshaller();
Cerveja cerveja = (Cerveja)unmarshaller.unmarshal(req.getInputStream());
Opróximopassoégarantirqueacervejatenhaomesmonomequeofornecido
peloidentificadore,então,adicioná-laaoestoque:
cerveja.setNome(identificador);
estoque.adicionarCerveja(cerveja);
T a m b é ménecessárioenviarparaoclienteocódigo201 Created,comocabeça-
lho Location,indicandoaURLondeanovacervejaestádisponível.Comonosso
servletjárecebeaURLdevidamenteajustada,bastaajustaraURLdarequisiçãono
cabeçalho Locationatravésdométodo HttpServletResponse.setHeader:
String requestURI = req.getRequestURI();
resp.setHeader("Location", requestURI);
resp.setStatus(201);
T a m b é méumaboapráticaenviardevoltaparaoclienteorecursocriado,jáque
algopodetersidoalteradonafasedecriaçãodorecurso.Esteprocessoserábastante
facilitadoatravésdousodométodo escreveXML,criadoanteriormente:
escreveXML(req, resp);
Ométodocompletoficaassim:
90

## Página 97

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
) != null) {
protected void doPost(HttpServletRequest req, HttpServletResponse resp)
throws ServletException, IOException {
try {
String identificador = null;
try {
identificador = obtemIdentificador(req);
} catch (RecursoSemIdentificadorException e) {
resp.sendError(400, e.getMessage()); //Manda um erro 400 - Bad Request
}
if (identificador != null && estoque.recuperarCervejaPeloNome(identificador
resp.sendError(409, "Já existe uma cerveja com esse nome");
return ;
}
Unmarshaller unmarshaller = context.createUnmarshaller();
Cerveja cerveja = (Cerveja)unmarshaller.unmarshal(req.getInputStream());
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

## Página 98

5.4.Implementandoacriaçãodeumrecurso CasadoCódigo
Figura5.5:ExemplodeutilizaçãodoPosterparacriaçãodeumrecurso
Casoométodotenhasidoimplementadocorretamente,algocomooseguinte
92

## Página 99

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
deveserretornado:
Figura5.6:Resultadodacriaçãodorecurso
Alémdisso,noteque,casoamesmarequisiçãosejasubmetidaumasegundavez,
ocódigo409deveserretornado:
93

## Página 100

5.4.Implementandoacriaçãodeumrecurso CasadoCódigo
Figura5.7:Respostadeerroindicandoqueorecursojáhaviasidocriado
94

## Página 101

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
5.5 Implementando negociação de conteúdo n a cri-
ação d orecurso
Paraimplementarnegociação deconteúdonacriação dorecurso,oclientedeve
ajustarocabeçalho Content-Typedemaneiraqueindiqueotipodoconteúdo
presentenarequisição. Oservidordeverecuperaroconteúdodestecabeçalhoe
trataresteconteúdo.Parafazerissocomnosso servlet,bastaexecutarométodo
HttpServletRequest.getContentType:
String tipoDeConteudo = req.getContentType();
Opróximopassoéumincluirum if/ else if/ else.Oprimeirovaifazero
testeseoconteúdoédotipoXML( text/xmlou application/xml);osegundo
vaitestarseoconteúdoédotipoJSON( application/json)eoterceirovaienviar
umerro,informandoqueotipodedadonãofoidetectado.
NocasodoconteúdoserXML,ocódigojápreparadodeveserutilizado.Nocaso
deserJSON,vocêdeveutilizarumcódigosemelhanteaodeescrita. Noentanto,
paralerJSON,devemosrealizaraleituradocorpodarequisiçãomanualmente-o
modelodoJettisonnãocomportaaleituradeuma s t re am.Nestecaso,utilizamosa
classe org.apache.commons.io.IOUtilspararealizaraleituradaslinhasde
dadospresentesna s t re am:
List<String> lines = IOUtils.readLines(req.getInputStream());
StringBuilder builder = new StringBuilder();
for (String line : lines) {
builder.append(line);
}
95

## Página 102

5.5.Implementandonegociaçãodeconteúdonacriaçãodorecurso CasadoCódigo
Meu p r o j e t on ã o tem a bibliotecad a Apache, o que
f a ç o ?
CasovocêutilizeoMaven,bastaadicionaradependência:
<dependency>
<groupId>commons-io</groupId>
<artifactId>commons-io</artifactId>
<version>2.4</version>
</dependency>
Senãoforseucaso,vocêtambémpodefazero downloaddestabibli-
otecanosite:http://commons.apache.org/proper/commons-io/
Nasequência,bastautilizarométododeleituradoJettisonparatransformaro
JSONemumobjeto Cerveja:
MappedNamespaceConvention con = new MappedNamespaceConvention();
JSONObject jsonObject = new JSONObject(builder.toString());
XMLStreamReader xmlStreamReader = new MappedXMLStreamReader(jsonObject, con);
Unmarshaller unmarshaller = context.createUnmarshaller();
Cerveja cerveja = (Cerveja)unmarshaller.unmarshal(xmlStreamReader);
Apartirdaqui,ométodojáestápraticamentepronto.Basta,agora,repetiros
passosrealizadosparaleituradeXML(nãoesquecendodesubstituirométodofinal
por escreveJSON,aoinvésde escreveXML):
cerveja.setNome(identificador);
estoque.adicionarCerveja(cerveja);
String requestURI = req.getRequestURI();
resp.setHeader("Location", requestURI);
resp.setStatus(201);
escreveJSON(req, resp);
Paratestar,bastarepetiroprocedimentofeitoanteriormente,mascomumare-
quisiçãoJSON:
96

## Página 103

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
Figura5.8:RequisiçãoJSON
Seestivercorreto,oresultadodeveseroseguinte:
97

## Página 104

5.5.Implementandonegociaçãodeconteúdonacriaçãodorecurso CasadoCódigo
Figura5.9:Resposta
Notequeorecursoestápresentenoservidorindependentedoseuconteúdo,
ouseja,searequisição forfeitaumasegundavezenão houvertipodeconteúdo
definido,seráretornadoumXML.
98

## Página 105

CasadoCódigo Capítulo5.ImplementandoserviçosRESTemJavacomServlets
5.6 Conclusão
V o c êviunestecapítulocomoimplementarserviçosRESTapartirde servletsJava.
Estesserviçosfazemapenasacriaçãoerecuperaçãodeconteúdo(orestantesãoape-
nasvariações destesdoistipos).
Noentanto,vocêdeveternotado:édemasiadocomplexorealizaresteprocesso,
mesmoparaumrecursosimples. V o c êdeveestarseperguntando:existealguma
maneira,maissimples,derealizaresteproceso?Sim,há!
Nospróximoscapítulos,vocêverácomoutilizaraespecificaçãoJavaparacriação
deserviçosREST,oJAX-RS.Alémdisso,vocêtambémverácomoincluir linksHA-
TEOASnosseusrecursosdemaneiraeficiente,comotestaressesserviços,tópicos
sobrecasoscomplexosdemodelagememuitomais.V a m o semfrente?
99

## Página 107

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
[1]SamRubyLeonardRichardson.Restfulwebservices.2007.
[2] AlexandreSaudate.Soaaplicado:integrandocomwebservicesealém.2013.
101