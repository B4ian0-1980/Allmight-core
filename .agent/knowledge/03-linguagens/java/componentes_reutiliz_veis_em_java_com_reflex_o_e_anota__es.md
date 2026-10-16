---json
{
  "id": "componentes_reutiliz_veis_em_java_com_reflex_o_e_anota__es",
  "title": "Componentes Reutilizáveis em Java com Reflexão e Anotações",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `Componentes Reutilizáveis em Java com Reflexão e Anotações.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "anota",
    "com",
    "componentes",
    "java",
    "linguagens",
    "reflex",
    "reutiliz",
    "veis"
  ],
  "perguntas_tipo": [
    "Como utilizar Componentes Reutilizáveis em Java com Reflexão e Anotações?",
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

# Componentes Reutilizáveis em Java com Reflexão e Anotações

> **Arquivo Original:** `Componentes Reutilizáveis em Java com Reflexão e Anotações.pdf`
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
Conceitos Básicos 1
1 Conhecendo a Reflexão 3
1.1 Aindafaltaalgumacoisanaorientaçãoaobjetos?. . . . . . . . . . . . 5
1.2 Reflexão,muitoprazer! . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.3 OprimeirocontatocomaAPIReflection . . . . . . . . . . . . . . . . 12
1.4 U s a rreflexãotemumpreço? . . . . . . . . . . . . . . . . . . . . . . . . 18
1.5 Considerações finais. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
2 J a v aReflection API 25
2.1 Obtendoinformações sobreasclasses. . . . . . . . . . . . . . . . . . . 26
2.2 Trabalhandocomclasses . . . . . . . . . . . . . . . . . . . . . . . . . . 32
2.3 Manipulandoobjetos . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
2.4 Procurandométodoseatributosparavalidação . . . . . . . . . . . . . 50
2.5 Coisasquepodemdarerrado . . . . . . . . . . . . . . . . . . . . . . . 53
2.6 Considerações finais. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
3 Metadados e Anotaçõ e s 5 7
3.1 Definiçãodemetadados . . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.2 Criandoanotações . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
3.3 Lendoanotações emtempodeexecução . . . . . . . . . . . . . . . . . 7 4
3.4 Limitações dasanotações . . . . . . . . . . . . . . . . . . . . . . . . . . 79
3.5 Mapeandoparâmetrosdelinhadecomandoparaumaclasse . . . . . 80
3.6 Considerações finais. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
i

## Página 6

Sumário CasadoCódigo
4 P r o x yDinâmico 89
4.1 Oqueéumproxy?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
4.2 ProxydinâmicocomaAPIReflection . . . . . . . . . . . . . . . . . . 92
4.3 Gerandoaimplementaçãodeumainterface . . . . . . . . . . . . . . . 97
4.4 ProxydeclassescomCGLib . . . . . . . . . . . . . . . . . . . . . . . . 102
4.5 Consumindoanotações emproxies . . . . . . . . . . . . . . . . . . . .109
4.6 Outrasformasdeinterceptarmétodos. . . . . . . . . . . . . . . . . . 113
4.7 Considerações finais. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
B o a sP r á t i c a s 117
5 T estandoclasses q u eusam Reflexão 119
5.1 Variandoestruturadaclasseparateste . . . . . . . . . . . . . . . . . . 122
5.2 T e s t edeproxiesdinâmicos . . . . . . . . . . . . . . . . . . . . . . . . . 136
5.3 Testandoaconfiguraçãodemetadados . . . . . . . . . . . . . . . . . . 138
5.4 GerandoclassescomClassMock. . . . . . . . . . . . . . . . . . . . . . 144
5.5 Considerações finais. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
Bibliografia 151
Versão: 16.9.7
ii

## Página 7

P a r t eI
Conceitos Básicos
Essaprimeirapartedolivrovaiensinarosconceitosarespeitodereflexãoeme-
tadadosassimcomoousodasAPIsdalinguagemJavaparaautilizaçãodessesre-
cursos.Apartirdaleituradessesquatroprimeiroscapítulos,espera-sequeoleitor
obtenhafamiliaridadecomousodereflexãonalinguagemJava,sabendocomoobter
emanipularseusprincipaiselementos,utilizando-osparadesenvolvercomponentes
reutilizáveisemdiferentescontextos.
Ocapítulo1falasobreasdeficiênciasdaorientaçãoaobjetosefazumaintrodu-
çãoareflexãocomputacional,mostrandoseupoderatravésdeumpequenoexem-
plo.Jáocapítulo2entraemdetalhesarespeitodaAPIReflectiondalinguagemJava,
mostrandoseusprincipaiselementosecomopodemserutilizados.Emseguida,o
capítulo3abordaaconfiguraçãodemetadadosadicionais,falandosobreasdiferentes
alternativasparadefini-loseentrandoemdetalhessobrecomoasanotações funci-
onamnalinguagemJava.Finalizandoessaprimeiraparte,ocapítulo4falasobreo
recursodeproxiesdinâmicos,quaisasformasdeimplementá-losecomocombiná-
loscomastécnicasmostradasnoscapítulosanteriores.Nofinaldecadacapítuloé
apresentadoumexemplorealistaqueaplicaosconceitosapresentados.

## Página 9

Capítulo1
ConhecendoaReflexão
“ Om u n d oécomo u mespelho q u edevolve a cada pessoa o reflexo de seus próprios
pensamentos. ”
–LuísFernandoVeríssimo
Melembroatéhojequandoestavacomeçandoaamadurecernosconceitosda
orientaçãoaobjetos.U mfatoquememarcoumuitofoiquandopelaprimeiravez
euvianecessidadedecriarumainterfaceparaencapsularumcomportamento.Foi
comoseumnovomundoseabrissenaminhafrente.Comodizaexpressãoemlin-
guagempopular,“ afichacaiu”.Eufinalmentecompreendiacomoutilizaraquelas
funcionalidadesdaorientaçãoaobjetosparaimplementardeumaformainteligente
osrequisitosdeumsistema. Comoestudodospadrões deprojeto,esseconheci-
mentofoicadavezmaisserefinando,atéserconcretizadonolivro“DesignPatterns
comJava:Projetoorientadoaobjetosguiadoporpadrões”.Sóqueaminhajornada
paradesenvolversoftwaredeumaformacadavezmelhornãoparounaorientação
aobjetos...
Comotempo,eufuivendoqueapenascomautilizaçãodaorientaçãoaobjetos

## Página 10

CasadoCódigo
muitosproblemasaindanão eramresolvidos. Foiaíqueconheciareflexãoeum
novomundoseabriunovamenteaminhafrente!Apartirdareflexãoépossível,em
tempodeexecução,conheceraestruturadeumaclasseeutilizaressasinformações
paraaexecuçãodeumalógica.Dessaforma,algunstiposdecódigoquedependiam
decadaclasse,masqueeramrepetitivosemsuaessência,agorapodemsercriados
deformamaisgeralereutilizadosemdiversoscontextos.
Apartirdesseconhecimentodereflexãoedasferramentasparaaplicarissona
linguagemJava,comeceiadesenvolversoluções reutilizáveisnomeudia-a-dia,en-
xergandoopotencialdessatécnicaemaumentarareutilizaçãodecódigoapartirda
eliminaçãodetarefasrepetitivas.Deformacomplementar,comeceiautilizarmeta-
dados,aprincípioapenascomanotações decódigo,eemseguidacombinandoessas
informações comfontesexternasepadrões denomenclatura.Comopoucoestudo
sobreessetipodesoluçãohaviasidoconduzidoatéomomento,decidiassumiresse
desafioemmeusestudosdedoutorado.Comeceientãoaestudarocódigodediver-
sosframeworksutilizadosnomercadoeabstraindosuassoluções conseguienxergar
diversospadrões, tantoparasuaestruturainterna,quantoparaidentificarcenários
ondeessetipodesoluçãoéaplicável.
Sendoassim,oobjetivodesselivroéapresentarpassoapassotodooconheci-
mentoqueadquirinessajornada!Desdeosprimeirospassosnoconhecimentoda
reflexãoatétécnicasavançadasparaautilizaçãodosmetadados.Oqueesselivrose
diferenciadeoutrosqueensinamautilizarreflexãoemJava,équeelenãoselimita
amostrarcomofuncionamasAPIs,mastambémapresentamcomoelaspodemser
utilizadasnoprojetodeumsoftwareparaaumentarareutilizaçãoe,consequente-
mente,aprodutividadedaequipe.Emoutraspalavras,serámostradonãosócomo
usar,mascomoutilizá-ladaformacorretaemaiseficiente!
Essecapítuloexploraalgunsproblemasqueaorientação aobjetosnão conse-
gueresolverdeformadireta,eintroduzoconceitodereflexão,mostrandocomoela
funciona,especialmentenalinguagemJava.Paraqueosleitorespossamcomeçara
saborearopoderdareflexão,algunsexemplosdecódigoirãomostrarumpoucodo
queépossívelfazercomreflexão. Emseguida,essecapítulomostraquetudotem
umpreço,efazumaanálisecomparativadedesempenhonainvocaçãodeummé-
todoviareflexãocomsuachamadadireta.Parafinalizar,éfeitaumaapresentaçãode
comoolivroestáorganizado,fazendoumapréviadoqueseráapresentadoemcada
capítulo.
4

## Página 11

CasadoCódigo Capítulo1.ConhecendoaReflexão
1.1 Ainda f a l t aalguma coisan a orientação a obje-
tos?
Aorientaçãoaobjetospossuidiversosrecursospoderosos,quenospermitemodelar
umsistemadeformaaaumentaroreuso,permitindoacriaçãodeumcódigocom
melhorqualidade.Autilizaçãodepadrõespotencializaaindamaisautilizaçãodesses
recursos,poissãosoluções recorrentesquepossuemumaestruturaadequadapara
umconjuntodecenários.Porém,mesmoassim,aindaexistemcenáriosemquea
orientaçãoaobjetosnãoajudamuito.
L e n d oparâmetros de a p l i c açõ e sW e b
U mexemplocomumdessetipodecódigoéarecuperaçãodasinformações de
umarequisiçãowebparasereminseridasemumoutroobjeto.Otrechodecódigo
aseguirilustraessasituação comocódigodedoisservlets,sendoqueumdeles
recebeinformações referentesaumprodutoeooutroreferenteaumcliente. Se
observarmososdoiscódigos,elessão bemparecidos,porémapenasutilizandoas
técnicasdeorientaçãoaobjetos,nãoépossívelareutilização.
Listagem 1.1-Códigosdeservletsparapopularpropriedadesdeobjetos:
// código em um servlet que recupera informação de um produto
@WebServlet("/novoProduto")
public class NovoProdutoServlet extends HttpServlet{
protected void doPost(HttpServletRequest rq, HttpServletResponse rp)
throws ServletException, IOException {
Produto p = new Produto();
p.setNome(rq.getParameter("nome"));
p.setCategoria(rq.getParameter("categoria"));
p.setPreco(Double.parseDouble(rq.getParameter("preco"));
p.setDescricao(rq.getParameter("descricao"))
//outras informações
}
}
// código em um servlet que popula informações de um novo cliente
@WebServlet("/cadastro")
public class CadastroClienteServlet extends HttpServlet{
5

## Página 12

1.1.Aindafaltaalgumacoisanaorientaçãoaobjetos? CasadoCódigo
protected void doPost(HttpServletRequest rq, HttpServletResponse rp)
throws ServletException, IOException {
Cliente c = new Cliente()
c.setNome(rq.getParameter("nome"));
DateFormat formatadorData = new SimpleDateFormat("MM/dd/yy");
c.setDataNascimento(
(Date)formatter.parse(rq.getParameter("dataNascimento"));
c.setLogin(rq.getParameter("login"));
c.setSenha(rq.getParameter("senha"));
//outras informações
}
}
U mfatointeressantedesernotadoéqueambososcódigosseguemumamesma
lógica,ouseja,nosdoiscódigosparâmetrosdarequisição websão recuperadose
inseridosnoobjetoemumapropriedadecomomesmonome.Existemalgunsca-
sosespeciais,comoaconversãopara doubledopreçodoprodutoeaconversão
para Datedadatadenascimentodocliente. Mas,dequalquerforma,éfácilde
notarasimilaridadeentreoscódigos.Essetipodecódigonormalmenteémassante
desercriado,principalmentequandoonúmerodeparâmetrosaseremrecupera-
doségrande.Comoconsequência,frequentementesãocometidoserrosondeuma
Stringacabasendoescritaerradaouumadaspropriedadesacabasendoesquecida
pelodesenvolvedor.
U m aoutraquestãoéqueseporacasoforadicionadomaisumatributoemal-
gumadasclasses,issovaiacarretaremumamudançadecódigonoServlet,ondeum
novoparâmetrovaiprecisarserlidoeatribuídoaele.Essanecessidadedemudança
éumsintomadequeessecódigopoderiasermelhoradoousimplificadodealguma
forma.
Criando proxies p a r aexecutar métodosde forma assíncrona
V a m o sagoraconsiderarumexemplobemdiferentedoanterior.Imagineque
umsistemapossuaumserviçodelogging,ouseja,paraoregistrodeinformações de
auditoria,quepossuamétodospararegistrarinformações eerros.Ocontratodesse
serviçoérepresentadopelainterface LoggingService. Nessesistema,existem
váriasimplementações desseserviço,quepodem,porexemplo,armazenarasinfor-
mações embancodedados,emarquivoseetc...Devidoaquestões dedesempenho,
decidiu-sequeesseserviçodeveriaexecutardeformaparalelaafuncionalidadeprin-
cipal.
6

## Página 13

CasadoCódigo Capítulo1.ConhecendoaReflexão
Seguindoumbomdesignorientadoaobjetos,eprincipalmenteporexistirem
diversasimplementações dessainterface,decidiu-sefazerum p rox yqueencapsula
aclasseoriginaleexecutaseusmétodosemumanova thread. Segueabaixocomo
seriaocódigodessaclasse.Elaimplementaainterface LoggingServiceepossui
umatributodessemesmotipo,queiráconteroobjetoencapsuladopelo p rox y.
Observequeacadachamadademétodo,omesmométododoobjetoencapsulado
éinvocadoemumathreaddiferente.
Listagem 1.2-Proxyparaexecutarasfunções deloggingdeformaassíncrona:
public class LoggingAsyncProxy implements LoggingService{
private final LoggingService service;
public LoggingAsyncProxy(LoggingService service){
this.service = service;
}
public void registerInformation(String info){
new Thread(
public void run(){
service.registerInformation(info);
}
).start();
}
public void registerError(Exception error){
new Thread(
public void run(){
service.registerError(error);
}
).start();
}
}
Seobservarocódigodo p rox ycriado,épossívelperceberqueexisteumacerta
duplicaçãonosmétodos,porémessaéumaduplicaçãodifícildeserremovidapois
ométodoqueéinvocadoédiferente.Imagineagoraquesejanecessáriocriaressa
mesmafuncionalidadeparaumaclassequepossuiumainterfacediferente.Imagine,
porexemplo,emumaclassedotipoDAO, Da ta Access Object,responsávelpor
persistirerecuperarobjetos,quesedesejeexecutaruma threaddiferenteosmétodos
quenão tenhamretorno. Ocódigoresultantedocódigocriadoestámostradoa
7

## Página 14

1.1.Aindafaltaalgumacoisanaorientaçãoaobjetos? CasadoCódigo
seguir.
Listagem 1.3-Proxyparaexecutarasfunções deloggingdeformaassíncrona:
public class ProdutoDAOAsync implements ProdutoDAO{
private final ProdutoDAO dao;
public ProdutoDAOAsync(ProdutoDAO dao){
this.dao = dao;
}
public void inserir(Produto p){
new Thread(
public void run(){
dao.inserir(p);
}
).start();
}
public Produto recuperar(int id){
return dao.recuperar(id);
}
public void excluir(Produto p){
new Thread(
public void run(){
dao.excluir(p);
}
).start();
}
public void atualizar(Produto p){
new Thread(
public void run(){
dao.atualizar(p);
}
).start();
}
}
Secompararmos,épossívelobservarqueosdoiscódigossãomuitoparecidos,
porémpodemostambémverqueédifícildereaproveitarocódigodeumnooutro
caso.Omotivodessadificuldadeéquepormaisqueafuncionalidadesejaparecida,
elaprecisainvocarummétododaclassequeestásendoencapsuladanomeiodesua
8

## Página 15

CasadoCódigo Capítulo1.ConhecendoaReflexão
execução. Dessaforma,éatépossívelreutilizaressamesmaclassedeproxypara
classesqueimplementemumamesmainterface,masparainterfacesdiferentesfica
maiscomplicado.
1.2 Reflexão , muito prazer!
“Vápara o seu negócio, o prazer, enquanto eu vou para meu prazer, negócios. ”
–WilliamWycherley
Anoçãodereflexãocomputacionalfoiintroduzidapelaprimeiravez,aindano
contextodelinguagensprocedurais,em1982[5]. Porémfoiem1987,queoartigo
"Concepts a n dExperiments i nComputational Reflection”[3]consolidouoconceito.
Reflexãopodeserdefinidacomooprocessonoqualumprogramadecomputador
podeobservaremodificarsuaprópriaestruturaecomportamento.Autilizaçãode
reflexãotambéméconhecidacomometaprogramação,poiscomsuautilizaçãoum
programapoderealizarcomputações arespeitodelepróprio.
Aintrospecçãoéumsubconjuntodareflexãoquepermiteumprogramaaob-
terinformações arespeitodesipróprio. Apartirdasinformações obtidascoma
introspecção,épossívelmanipularinstânciasacessandoseusatributoseinvocando
seusmétodos.Dessaforma,épossívelcriarcriarumcódigoquelidacomumaclasse
cujaestruturaelenãoconhece.
Areflexãotambémjáfoidocumentadacomoumpadrãonoprimeirolivrodasé-
rie“Pattern-OrientedSoftwareArchitecture”,conhecidoinformalmentecomoPOSA
[2].Segundoessafonte,umdosbenefíciosdesuautilizaçãoestánaflexibilidadee
adaptabilidadedocódigo. Seumcódigoqueutilizareflexãosebaseianaestrutura
deumaclasse,porexemplo,eleseadaptarámaisfacilmenteamudançasnessaestru-
tura.Aindasegundoessepadrão,apioranodesempenhoéumadasdesvantagens
deseuuso,assimcomoumaumentonacomplexidadedocódigo.
Todososprogramadoressabemqueparaexecutarumprograma,umcomputa-
dordevecarregarseuscomandosnamemória.Adicionalmente,eletambémutiliza
amemóriaparaarmazenarvariáveisquesãomanipuladascomopartedaexecução
dosoftware.Dentrodessecontexto,areflexãonadamaisédoqueoprogramaaces-
saremodificarassuasinstruções. Esseéumrecursopoderoso,masqueprecisaser
utilizadocombastanteresponsabilidade.
9

## Página 16

1.2.Reflexão,muitoprazer! CasadoCódigo
Reflexão em J a v a
EmJava,asclassesqueimplementamfuncionalidadesrelacionadasareflexãofi-
camnopacote java.lang.reflectesãoconhecidascomo API Reflection.A p e -
sardonome,grandepartedessasclassesnaverdadeimplementamapenasfunções
deintrospecção. Emoutraspalavras,épossívelobterinformações sobreasclasses
deumsoftware,masnãoépossívelmodificá-las.Grantepartedesselivrofocaprin-
cipalmentenessasfuncionalidades.
AalteraçãodeclassesemJavanãoésuportadapelaAPIpadrãodereflexão,mas
podeserfeitaatravésdamanipulação debytecode. Deumaformamaissimples,
aaplicaçãomodificaocódigocompiladoqueserácarregadopelamáquinavirtual.
Issopodeserfeitoestaticamentedepoisdacompilaçãodocódigo,nomomentodo
carregamentodaclasseouemtempodeexecução. Comoécomplicadosubstituir
namáquinavirtualumaclassequejáfoicarregada,quandoamodificaçãoéfeitaem
tempodeexecução,normalmenteécarregadaumanovaclassecomasmodificações
feitasnaclasseexistente.Openúltimocapítulodesselivroédedicadoatécnicade
manipulaçãodebytecode,porémemcapítulosanterioressãoapresentadasalgumas
ferramentasqueutilizamesserecursodeumaformaencapsulada.
10

## Página 17

CasadoCódigo Capítulo1.ConhecendoaReflexão
Diferença em Relação a Linguagens Dinâmicas
Otermo linguagem dinâmicaéutilizadoparadescreverlinguagens
dealtonívelqueexecutamemtempodeexecuçãocomportamentosque
aslinguagensnormalmentefazemduranteacompilação. Dentreesses
comportamentosnormalmenteestáaadição decódigoemobjetosea
modificaçãodetipos. Nessetipodelinguagemessetipodeoperaçãoé
comumemuitasvezesésuportadaapartirderecursoseferramentasda
próprialinguagem.ExemplosdessetipodelinguagemsãoRuby,Python
eGroovy.
Autilizaçãodereflexãoemlinguagensdinâmicasacabasendomais
simplesdoqueemlinguagensestaticamentetipadascomoJava.Emal-
gunscasos,ainvocaçãodinâmicademétodoseamodificaçãodetiposé
utilizadacomomecanismopadrãodalinguagem,enãoapenasemsitua-
ções quesedesejaumamaiorflexibilidade.Astécnicasmostradasnesse
livrofocamemcomoutilizarcomsegurançaosrecursosdareflexãoem
Java,queéumalinguagemestaticamentetipada.Dessaforma,aaplica-
ção podeusufruirderecursosquepermitemumamaiorsegurançade
códigoeaplicarareflexãosomenteempontosondeumamaiorflexibili-
dadeénecessária.Pormaisqueousodessesrecursossejadiferenteem
linguagensdinâmicas,acreditoquealgunsconceitosaquiapresentados
tambémpodemserutilizadosnessecontexto.
C o m oa reflexão pode me a j u d a r ?
Autilizaçãodareflexãoémuitoútilemsituações emqueocódigoprecisalidar
comclassescominterfacesdiferentes,porémsuacriaçãoérepetitivaesegueumaló-
gica.Paraessetipodecódigoacabasendodifícilautilizaçãodetécnicastradicionais
daorientaçãoaobjetos,poisosobjetospossuemcontratosdiferenteseosmétodos
queprecisamserinvocadosdependemdosobjetos. Osexemplosapresentadosno
começodessecapítuloilustramdoiscenáriosondeissoocorre.
Aideiadousodereflexãoétornarocódigoadaptávelaestruturadosobjetose
comissopermitirqueelepossasermaisreutilizável.Dessaforma,épossívelsubsti-
tuiracriaçãodeumcódigoqueprecisariaserrepetidoparacadaclasse,pelachamada
aummétodoouumaclassequeutilizereflexão.Dessaformaépossíveldiminuira
11

## Página 18

1.3.OprimeirocontatocomaAPIReflection CasadoCódigo
quantidadedecódigo,aumentandoavelocidadededesenvolvimentodaequipe.
Pormaisqueautilizaçãodereflexãosejaumatécnicamaiscomplexa,seuuso
podeserfeitodeformabemlocalizada. Emoutraspalavras,épossívelencapsular
suautilizaçãodentrodeclassesoucomponentes,deformaqueissofiquetranspa-
renteparaorestodosoftware.U mgrandeexemplodissosãoosframeworks,pois
grandepartedelesutilizamessesrecursosdereflexãodeformaencapsuladaeisso
nãoprecisaserconhecidopelodesenvolvedorqueestáoutilizando.
1.3 O primeiro contato co m a API Reflection
Comotambémsouprogramador,seiquegrandepartedosleitoresdevemestaran-
siososparaverumpoucodecódigocomareflexãosendoutilizadanaprática.Essa
seçãoapresentaumapequenapréviasobreofuncionamentodaAPIdereflexãoem
Java,mostrandoumpequenoexemploqueilustraasuautilização. Aquitambém
falaremosdasanotações ecomopodemserutilizadasemconjuntocomareflexão.
Peçoparaquenessemomentosepreocupemapenasementenderosconceitoseo
exemplo,poismaioresdetalhessobreessasAPIsserãodadosnospróximoscapítulos.
Transformando as propriedades de uma classe em mapas
Oexemploquevamosexplorarnesseprimeirocapítuloenvolveageraçãodeum
mapadepropriedadesapartirdeumaclassenoformatoJavaBean,ouseja,com
métodosdeacessonoformatogeteset.Aocriarumalgoritmoutilizandoreflexão,a
ideiaéverqualseriaoprocedimentoqueumdesenvolvedorutilizariaparaescrever
ocódigomanualmenteetentarreproduziressemesmoprocedimentonocódigo.
Nocasodageraçãodomapa,oprocedimentoébasicamenteinvocarcadamétodo
getterdaclasseeadicionarnomapaovalorretornadocomachavedonomeda
propriedade.
Esseexemplo,decertaforma,éparecidocomoquevimosanteriormentepara
arecuperação dosparâmetrosdoServlet. Noexemploanteriorprecisávamosre-
cuperarosparâmetrospassadosparapáginadeformaapopularaspropriedadesdo
objetoeaquiiremosrecuperaraspropriedadesdeumobjetoparainserirmosemum
mapa.Emambososcasos,casofossedesenvolvidoumcódigoparacadaclasse,esse
códigoseriarepetitivoechatodesercriado.Oobjetivoéautomatizaressetipode
tarefa,deformaqueessetipodecódigonãoprecisesercriado,diminuindoachance
deerroseaumentandoaprodutividadedosdesenvolvedores.
Aclasseapresentadaaseguirmostraumapossívelimplementaçãodessecódigo
12

## Página 19

CasadoCódigo Capítulo1.ConhecendoaReflexão
parageraromapadepropriedades. Ométodo gerarMapa()percorretodosos
métodosdoobjetopassadocomoparâmetro,recuperandocomoretornosomente
osmétodosidentificadoscomogetterseinserindonomapa.Parapoderacessaros
dadosdeumaclasse,oprimeiropassoérecuperarainstânciadaclasse Classre-
lativaaclassedoobjeto,oqueéfeitoatravésdométodo getClass(). Apartir
dessainstância,osmétodossãorecuperadosatravésde getMethods()eessalista
deinstânciasde Methodépercorridaprocurandoosquepodemserclassificados
comogetter.
OmétodoisGetter()acessaasinformações dométodoverificandoporsuas
informações sesetratadeummétodogetter.Asinformações consideradasparaisso
são:senomedométodoseiniciacom“ g e t ” ,seoretornoédiferentede voideseele
nãopossuiparâmetros.Casoométodosejaidentificadocomogetter,eleéinvocado
apartirdométodo invoke()eseuvalorrecuperadoparaserinseridonomapa.
Observequeonomedométodoétransformadononomedapropriedadepelo
método deGetterParaPropriedade()paraadição nomapa. Outraquestão
interessantedesernotadaéqueainvocaçãodométodoviareflexãoestáenvoltapor
umbloco try/catch,oqueindicaqueexistemerrosquepodemocorrernessa
invocação(oqueseráabordadomaisafrentenesselivro).
Listagem 1.4-Classequeutilizareflexãoparaageraçãodeummapa:
public class GeradorMapa {
public static Map<String, Object> gerarMapa(Object o){
Class<?> classe = o.getClass();
Map<String, Object> mapa = new HashMap<>();
for(Method m: classe.getMethods()){
try {
if(isGetter(m)){
String propriedade = deGetterParaPropriedade(
m.getName());
Object valor = m.invoke(o);
mapa.put(propriedade, valor);
}
} catch (Exception e) {
throw new RuntimeException(
"Problema ao gerar o mapa",e);
}
}
return mapa;
13

## Página 20

1.3.OprimeirocontatocomaAPIReflection CasadoCódigo
}
private static boolean isGetter(Method m) {
return m.getName().startsWith("get") &&
m.getReturnType() != void.class &&
m.getParameterTypes().length == 0;
}
private static String deGetterParaPropriedade(String nomeGetter){
StringBuffer retorno = new StringBuffer();
retorno.append(nomeGetter.substring(3, 4).toLowerCase());
retorno.append(nomeGetter.substring(4));
return retorno.toString();
}
}
Apróximalistagemmostraautilização dessemétodocriadoparaageração
demapas. Aclasse Produto,amesmadoexemplodoServlet, possuiquatro
propriedadescommétodosgetesetparasuarespectivarecuperaçãoemodificação.
Emseguidaéapresentadoumcódigo quecriaumanovainstânciadessaclasse,
recuperaomapacomométodocriadoeimprimeaspropriedadesrecuperadasno
console.Sendoassim,épossívelverquecomreflexãofoipossívelcriarumarotina
queacessamétodosdeumaclassesemdependerdiretamentedela.
Listagem 1.5-Utilizaçãodométododegeraçãodomapadepropriedades:
// Classe para ser utilizada como base
public class Produto {
private String nome;
private String categoria;
private Double preco;
private String descricao;
public Produto(String nome, String categoria, Double preco,
String descricao) {
this.nome = nome;
this.categoria = categoria;
this.preco = preco;
this.descricao = descricao;
}
//metodos get e set omitidos
}
14

## Página 21

CasadoCódigo Capítulo1.ConhecendoaReflexão
//Código que executa o método de geração do mapa e imprime
public static void main(String[] args){
Produto p = new Produto("Design Patterns","LIVRO",59.90,
"Publicado pela Casa do Codigo");
Map<String,Object> props = GeradorMapa.gerarMapa(p);
for(String prop : props.keySet()){
System.out.println(prop+" = "+props.get(prop));
}
}
Conhecendo anotaçõ e s
Quandovocêimplementaummétodoparacadaclasse,pormaisqueelesejare-
petitivo,tem-sealiberdadederealizaralterações paraatendernecessidadesdenegó-
cio.T o m a n d ocomoexemploageraçãodomapa,poderiasernecessárioquealguma
propriedadeprecisasseserignoradaouqueumapropriedadefosseadicionadacom
umnomediferente. Aocriarcadamétodoindividualissoéfácildefazer,porém,
utilizandoreflexão,comofazerparaqueoalgoritmotratealgumaspropriedadesdi-
ferentes? A p e s a rdareflexão permitiradefinição deummétodogenéricoparaa
geraçãodemapas,elenãoatendeosrequisitosquandoalgumelementoprecisaser
tratadodeformadiferente.
Énessepontoqueentramasanotações! Elaspermitemmarcaroselementosde
formaqueumalgoritmoqueutilizereflexãopossaidentificaroselementosqueele
devetratardeformadiferente.Asanotações permitemadicionarnovasinformações
emelementosdeprogramação. Essasinformações sãochamadasdeespecíficasde
domínio,poiselassãodizemrespeitoaointeressedaclassequeiráconsumi-las.É
importantejádeixarclaroqueumaanotaçãonãopossuicomportamentoesomente
suapresençanãofaznadaalémdeadicionarumainformação,porémelaspodem
seracessadasporoutrasclassesecomponentesparapermitirqueelesadaptemseu
comportamentodeacordocomsuapresença.
Asduaslistagensaseguirmostramcomoasanotações poderiamsercriadas,
sendo a primeira para ignorar uma propriedadee a segunda para definir um
nomediferenteparaumapropriedade. Novamentepeçoparaosleitoresnão se
preocuparemmuitocomosdetalhesdeimplementação,queserão explicadosnos
próximoscapítulos.Oqueéimportantepercebernessasanotações équeaprimeira
não possuipropriedadeseasegundapossuiumapropriedadedotipo String
15

## Página 22

1.3.OprimeirocontatocomaAPIReflection CasadoCódigo
chamada value.
Listagem 1.6-Anotação quedefinequandoumapropriedadeprecisaser igno-
rada:
@Retention(RetentionPolicy.RUNTIME)
public @interface Ignorar {
}
Listagem 1.7-Anotaçãoquedefineumnomediferenteparaapropriedade:
@Retention(RetentionPolicy.RUNTIME)
public @interface NomePropriedade {
String value();
}
Comojáfoiditoanteriormente,nadaadiantacriaranotações semumcódigo
queasconsome, poissozinhas elasnão fazem nada. Dessa forma, apróxima
listagemmostracomoocódigodogeradordemapaspoderiasermodificadopara
considerara presença das anotações. Nométodo isGetter() foiacrescen-
tadaumacondição queverificaseaanotação @Ignorarestápresente,fazendo
comqueosmétodosgetterscomessaanotação não sejamconsiderados. Adi-
cionalmente, nométodoprincipal gerarMapa(), antesde chamaro método
deGetterParaPropriedade()éverificadaseaanotação @NomePropriedade
estápresentee,emcasopositivo,ovalorconfiguradoérecuperadoeutilizado.
Listagem 1.8- Modificação da classequegerao mapaparaconsideraras ano-
tações:
public static Map<String, Object> gerarMapa(Object o){
Class<?> classe = o.getClass();
Map<String, Object> mapa = new HashMap<>();
for(Method m: classe.getMethods()){
try {
if(isGetter(m)){
String propriedade = null;
if(m.isAnnotationPresent(NomePropriedade.class)){
propriedade =
m.getAnnotation(NomePropriedade.class).value();
}else{
16

## Página 23

CasadoCódigo Capítulo1.ConhecendoaReflexão
propriedade = deGetterParaPropriedade(m.getName());
}
Object valor = m.invoke(o);
mapa.put(propriedade, valor);
}
} catch (Exception e) {
throw new RuntimeException("Problema ao gerar o mapa",e);
}
}
return mapa;
}
private static boolean isGetter(Method m) {
return m.getName().startsWith("get") &&
m.getReturnType() != void.class &&
m.getParameterTypes().length == 0 &&
!m.isAnnotationPresent(Ignorar.class);
}
Apartirdessanovaversão,épossível,apartirdaadição deanotações, alterar
parte do comportamentodo algoritmoreflexivo,comofazendo-o ignoraruma
propriedadeoumudandoonomequeéadicionadonomapa. Aseguirestáum
exemplodecomoalgunsdosmétodosdaclasse Telefoneseriamanotadospara
queocódigodogeradordemapasconseguissecapturarasanotações. Masesse
exemplofoisóparadarumgostinhodoqueviránospróximoscapítulosdolivro,
ondeserámostradonãosócomoutilizarreflexãoeanotações, mastambémemque
situações equaistécnicaspodemserutilizadas.
Listagem 1.9-Exemplodousodasanotações pelaclasseTelefone:
public class Telefone {
//atributos e outros métodos omitidos
@NomePropriedade("codigoInternacional")
public String getCodigoPais() {
return codigoPais;
}
@Ignorar
public String getOperadora() {
return operadora;
17

## Página 24

1.4.Us a rreflexãotemumpreço? CasadoCódigo
}
}
1.4 Usar reflexão tem u m preço?
“There’sno s u c hthing as a fr eelunch. (Não existe esse negócio de a l m oço grátis.)”
–Expressãopopularqueexpressaaideiadequeéimpossívelconseguiralgosemdarnada
emtroca
U mdosprincipaispreçosquesepagaaoseutilizarreflexãoéodesempenho.
Invocarummétodoapartirdereflexãoémaisdemoradodoqueinvocarummé-
tododiretamentenoobjeto. Issoéumfato! Porémsomenteessainformação não
ésuficienteparaavaliarseissopodegerarumproblemadedesempenho.Parater-
mosnoção doprejuízoaodesempenhotrazidopelareflexão,essaseção apresenta
umtestequecomparaotempodeumainvocaçãodemétodofeitadiretamentecom
formasdeinvocaressemétodoutilizandoaAPIdereflexão.
T e s t ep a r amedida de desempenho
Pararealizaresseteste,foicriadaumaclassechamada ClasseTestequepossui
ummétodochamado metodoVazio().Comoopróprionomedométodosugere,
seuconteúdoévazioparaqueotempomedidosejaapenasrelativoasuainvoca-
ção.Emseguida,foicriadaumainterfacechamada InvocadorMetodo,queseráo
contratodeclassesqueirãoinvocaressemétodorepetidasvezesutilizandodiferen-
tesabordagens.Ométodo invocarMetodo()recebecomoparâmetroonúmero
devezesqueométodoprecisaserinvocadoeochamarepetidasvezes.
A primeira implementação dessa interface estárepresentada na listagem a
seguir. A classe InvocadorNormal faz a invocação do métododiretamente
atravésdeumainstânciadaclasse. Essaimplementação servirácomobasepara
compararmoscomainvocaçãodométodoutilizandoreflexão.
Listagem 1.10-Implementaçãoqueinvocaométododiretamente:
public class InvocadorNormal implements InvocadorMetodo {
public void invocarMetodo(int vezes) {
ClasseTeste ct = new ClasseTeste();
for(int i=0; i<vezes; i++){
ct.metodoVazio();
}
18

## Página 25

CasadoCódigo Capítulo1.ConhecendoaReflexão
}
}
As duas listagens a seguir, InvocadorReflexao e
InvocadorReflexaoCache, utilizam reflexão para invocar o método. Em
ambas,aclassedoobjetoérecuperadaatravésdométodogetClass()eométodo
recuperadopeloseunomeatravésdeumachamadaa getMethod().Emseguida,
ométodoéinvocadonainstânciachamando-seométodo invoke(),passando-a
comoargumento.Adiferençaentreessasduasimplementações équenaprimeiraa
representaçãodométodoérecuperadaacadaiteraçãoenasegundaelaérecuperada
umavezereaproveitada.
Listagem 1.11-Implementação queacada iteração buscaométodoeoinvoca
utilizandoreflexão:
public class InvocadorReflexao implements InvocadorMetodo {
public void invocarMetodo(int vezes) {
try {
ClasseTeste ct = new ClasseTeste();
for(int i=0; i<vezes; i++){
Method m = ct.getClass().getMethod("metodoVazio");
m.invoke(ct);
}
} catch (Exception e) {
throw
new RuntimeException("Não consegui invocar o método",e);
}
}
}
Listagem 1.12-Implementaçãoquebuscaométodoumavezeoinvocautilizando
reflexãoacadaiteração:
public class InvocadorReflexaoCache implements InvocadorMetodo {
public void invocarMetodo(int vezes) {
try {
ClasseTeste ct = new ClasseTeste();
Method m = ct.getClass().getMethod("metodoVazio");
for(int i=0; i<vezes; i++){
m.invoke(ct);
}
19

## Página 26

1.4.Us a rreflexãotemumpreço? CasadoCódigo
} catch (Exception e) {
throw
new RuntimeException("Não consegui invocar o método",e);
}
}
}
Para comparar as formas de invocação das implementações de
InvocadorMetodo, foi criada a classe TesteDesempenho apresentada a
seguir. O métodoestático executaTeste() recebe como parâmetro uma
instânciade InvocadorMetodo para realizar o teste. Ele chama o método
invocarMetodo() para que o métodoseja invocado 100.000 vezes, e mede
otempoqueelelevaparaexecutaremnanosegundos. Alémdeimprimiresse
resultadonoconsole,eleretornaotempomedido.
Listagem 1.13-Classequecomparaasformasdeinvocação:
public class TesteDesempenho {
public static void main(String[] args){
double normal = executaTeste(new InvocadorNormal());
double reflection = executaTeste(new InvocadorReflexao());
System.out.println(
(reflection/normal) + " vezes mais que o normal"
);
double reflectionCache = executaTeste(
new InvocadorReflexaoCache());
System.out.println(
(reflectionCache/normal) + " vezes mais que o normal"
);
}
public static double executaTeste(InvocadorMetodo invoc){
long millis = System.nanoTime();
invoc.invocarMetodo(100000);
String nomeClasse = invoc.getClass().getName();
long diferenca = System.nanoTime() - millis;
System.out.println("A classe "+nomeClasse+
" demorou " + diferenca + " nano segundos");
return diferenca;
}
}
20

## Página 27

CasadoCódigo Capítulo1.ConhecendoaReflexão
Ométodoprincipaldessaclasseinvocaométodoparaexecuçãodotestepara
cadaumadasimplementações de InvocadorMetodo. Adicionalmente,elefaz
adivisão dotempoquecadaimplementação queutilizoureflexão pelotempode
referênciadaimplementação queinvocouométododiretamente. Dessaforma,
conseguimosverquantasvezesmaisainvocaçãocomreflexãoemcadacasodemora.
Oresultadoquefoiimpressonoconsolequandoexecuteiotesteemminhamáquina
estáapresentadonalistagemaseguir.
Listagem 1.14-Resultadodaexecuçãodacomparaçãodedesempenho:
A classe InvocadorNormal demorou 2334000 nano segundos
A classe InvocadorReflexao demorou 90823000 nano segundos
38.913024850042845 vezes mais que o normal
A classe InvocadorReflexaoCache demorou 6934000 nano segundos
2.9708654670094257 vezes mais que o normal
Osresultadosemnanosegundosacabamsendoumpoucoconfusospoissãonú-
merosmuitograndes. Andandoseiscasasdecimaisaesquerdatemosoresultado
emmilissegundos,quefoiaproximadamente2ms,90mse7msparaasrespecti-
vasclasses.Porém,esseresultadopodevariardeacordocomamáquinaenãoétão
interessantequantoaproporçãoentreessesvalores.Peloquefoiimpressonocon-
sole,podemosobservarquaquandoarecuperaçãodométodoéincluídaemcada
iteração, otempoécercade39vezesmaior. Porém,quandoométodoérecupe-
radoapenasumavez,essadiferençacaisignificativamente,sendoaproximadamente
apenas3vezesmaior.
Reflexões s o b r ea p e r d ade desempenho com reflexão
“Escreva seu código da forma mais simples, mais f á c i lde manter e mais eficiente
possível. Só depois f aça a medição de seu desempenho, encontre o n d eestão os
problemas e comece a introduzir o t i m i z ações. ”
–DannySimmons
Incluíadiscussãosobredesempenhologonoprimeirocapítulodolivropoisse
vocêvaiutilizarreflexãoemalgumasolução,vocêprecisasaberopreçoquevaiestar
pagando.Ofatodeumainvocaçãodemétodocomreflexãodemorarcercadetrês
vezesmaisdoqueumainvocaçãodiretadométodo,issonãosignificaqueotempo
21

## Página 28

1.4.Us a rreflexãotemumpreço? CasadoCódigo
deexecuçãodeumalgoritmoirátriplicarseutilizarreflexão.Éprecisoavaliarcada
casoelevaremconsideraçãooimpactoqueissoteránoresultadofinal.
Seobservarmosovalorbrutoobtidocomainvocaçãodeummétodoporrefle-
xão,podemosverqueovalordeumaúnicainvocaçãoénaordemdenanosegundos.
Issoéumvalorbempequenosecompararmoscomotempoparaexecuçãodetare-
fasdeentradaesaída,comoleituradeumarquivo,acessoabancodedadoseenvio
dedadospelarede.Emoutraspalavras,emrelaçãoaotempototaldeexecuçãode
umafuncionalidadequeenvolverfunções deentradaesaída,aperdacomousode
reflexãopodeserdesprezível.
Essadiferençanodesempenhopodesetornarsignificativa,quandoumaopera-
çãorealizadacomreflexãoéexecutadadentrodeumalooprepetidasvezes.Nesse
caso,apequenadiferençamultiplicadapormilharesdevezespodesetransformarem
umgargalosignificativo.Porém,mesmonessescasos,muitasvezesépossívelfazer
otimizações. Peloexemploapresentado,ficouclaroquearecuperaçãodarepresen-
taçãodométodolevamaistempodoquesuaexecução.Nocasodeumainvocação
repetidademétodosporreflexão,umaotimizaçãoseriaarmazenarpreviamenteem
umavariávelosmétodosqueseriaminvocados.
T o m a n d ocomoexemploageraçãodomapadepropriedades,imaginequeem
umaaplicaçãoessatransformaçãopreciseserfeitaemumalistacommilharesdeob-
jetos.U m apossívelotimizaçãoseria,aoinvésdebuscarosmétodosgettersdaclasse
duranteacriação domapa,fazerissopreviamenteereutilizarparatodososobje-
tos.Mesmoquenalistahouvessemobjetosdediferentesclasses,essasinformações
poderiamserarmazenadasporclasseereaproveitadasparatodasassuasinstâncias.
U mexemplodessetipodeotimizaçãodedesempenhofoifeitocomogerador
demapasnapróximalistagem.Aoinvésdereceberoobjeto,recuperarsuaclassee
executaroprocessamento,essanovaimplementaçãorecebeaclassenoconstrutor
ejácriaummapacomaspropriedadeseosmétodosparaparaseremutilizados
posteriormente. Dessaforma, aoexecutarogeradordemapaseleiráverificar
inicialmenteseoobjetopassadorealmenteédaquelaclasseedepoisiráutilizaros
métodosarmazenadosnomapa.Issoevitaráooverheaddaobtençãodosmétodos,
tornandoageração domapamaiseficienteseexecutadoparadiversosobjetosda
mesmaclasse.
Listagem 1.15-Geradordemapasquefazcachedosmétodos:
public class GeradorMapaPerformance {
22

## Página 29

CasadoCódigo Capítulo1.ConhecendoaReflexão
private Map<String, Method> propriedades = new HashMap<>();
private Class<?> classe;
public GeradorMapaPerformance(Class<?> classe) {
this.classe = classe;
for (Method m : classe.getMethods()) {
if (isGetter(m)) {
String propriedade = null;
if (m.isAnnotationPresent(NomePropriedade.class)) {
propriedade = m.getAnnotation(NomePropriedade.class)
.value();
} else {
propriedade = deGetterParaPropriedade(m.getName());
}
propriedades.put(propriedade, m);
}
}
}
public Map<String, Object> gerarMapa(Object o) {
if (!classe.isInstance(o)) {
throw new RuntimeException("O objeto não é da classe"
+ classe.getName());
}
Map<String, Object> mapa = new HashMap<>();
for (String propriedade : propriedades.keySet()) {
try {
Method m = propriedades.get(propriedade);
Object valor = m.invoke(o);
mapa.put(propriedade, valor);
} catch (Exception e) {
throw
new RuntimeException("Problema ao gerar o mapa", e);
}
}
return mapa;
}
}
Comoafrasenoiníciodessaseçãosugere,inicialmentedeve-sedesenvolvero
códigodaformamaislimpaesimplespossível.Emseguida,casoosrequisitosde
desempenhonãoestejamsendoatendidos,deve-seprocurarondeestáogargaloe
23

## Página 30

1.5.Considerações finais CasadoCódigo
realizaraotimizaçãodaquelapartedocódigo.Aotimizaçãodedesempenhoprecoce
éumamáprática,poispodefocaresforçosnaotimizaçãodeumapartedocódigoque
nãoésignificativanopanoramageraldaaplicação.Adicionalmente,essaotimização
podeterefeitoscolateraisnegativosnocódigo,comoprejudicarasualegibilidadeou
suaflexibilidade.
Esselivroiráfocarnousodetécnicasdereflexãoparaaelaboraçãodesoluções
flexíveiseinteligentes,compotencialdesimplificaracriaçãodeaplicações eaumen-
taraprodutividadedaequipe.Ofoconãoseránaperdaouganhodedesempenho
trazidoporcadaumadastécnicas,anãoserqueissosejaumfatorrelevantenotópico
queestiversendoapresentado.Porém,sugere-sequequandoareflexãoforutilizada
emumasolução,queosrequisitosdedesempenhosejamverificadosequetécnicas
deotimizaçãosejamutilizadasquandonecessário.
1.5 Considerações finais
Esseprimeirocapítuloteveoobjetivodeapresentaroconceitodereflexãocomputa-
cionaleutilizaçãodemetadados,mostrandocenáriosemqueastécnicasdeorien-
taçãoaobjetosnãosãosuficientesparacriarumasoluçãoreutilizáveleinteligente.
Paraosquenãosecontentamsenãoveremumpoucodecódigo,foiapresentado
umexemplosimplesdecomoareflexãoeousodemetadadospodemauxiliarna
criaçãodeumasolução. Paraosqueolhamparareflexãocomosefosseumbicho
desetecabeças,peçoquenãoseassustemcomocódigo,poistudoquefoiutilizado
seráexplicadocombastantedetalhenospróximoscapítulos.Sedesejarem,poderão
revisitaresseexemplomaistardedepoisdeleremosdoispróximoscapítulos.
Porfim,essecapítulofalarsobreumaquestãodelicadanautilizaçãodereflexão,
queéoseu trade-offemrelaçãoaodesempenho.Comofoimostrado,aflexibilidade
dousodessatécnicatemseucustoemtermosdedesempenho,eéporissoqueé
importanteterciênciadissoparautilizá-ladeformaadequada.U moutroefeitodo
usodareflexãoéoaumentodacomplexidadedocódigo,porémissoéalgoquepode
serfacilmentecontroladoencapsulandoseuusoemclassesecomponentesquesão
utilizadospelorestodocódigo.Afinal,quantosframeworksqueutilizavamreflexão
vocêjáutilizousemnemsabercomoeleestavafazendoaquelascoisas?
24

## Página 31

Capítulo2
J a v aReflectionAPI
“ D i g aespelho meu se hána avenida a l g u é mmais f el i zq u eeu”
–“ÉHoje”,DidieMaestrinho
Reflexãoéconsideradoumtemaavançado,poistrabalhacommetaprogramação,
ouseja,éumcódigoquetrabalhacomoprópriocódigo. Poressemotivo,éum
temaevitadoetemidopormuitosprogramadores. Seporumladoidentificaras
situações adequadasparaousodessatécnicarealmentenãoéfácileexigeumacerta
experiência,aAPIReflectiondoJavaparamanipularessasestruturasnãoédifícil.
Porexemplo,imaginequevocêestejacomeçandoatrabalharcomumaAPIpara
manipularobjetosem3dimensões. CertamenteessaAPIexigiráumacertacurvade
aprendizadoatéqueseobtenhaproficiêncianela.Porémadificuldadenãoésaber
quaissãoasclassesequaismétodoschamar,massimcompreenderosconceitosque
elarepresentaparaquesesaibacomoutilizá-ladeformaadequada.Sevocêjátra-
balhoucomobjetosem3dimensões comoutraferramentaqueutilizavaosmesmo
conceitos,certamenteessacurvadeaprendizadoserámuitomaissuave. Amaior

## Página 32

2.1.Obtendoinformações sobreasclasses CasadoCódigo
dificuldadeemseaprenderumaAPIestánacompreensãodosconceitosqueelare-
presentaenãoemsaberquaissãoseusmétodoseclasses.
AAPIReflectiondalinguagemJavatrabalhacomconceitosfamiliaresaqual-
querprogramador,quesão ospróprioselementosdalinguagem. U m aclasse,por
exemplo,possuiinformações comosuasuperclasse,suasinterfaces,seunome,seu
pacote,seusmétodoseseusatributos.V o c êpodefazercomela,oquesefazcom
umaclasse,instanciar.Damesmaforma,ummétodopossuiretorno,nome,parâ-
metro,modificadoreseexceções, eoquesepodefazercomeleéinvocar.Porisso,ao
começaratrabalharcomaAPIReflection,qualquerprogramadorsesenteemcasa,
trabalhandocomconceitosquejásãofamiliares.
EssecapítulotemoobjetivodeapresentarasprincipaisfuncionalidadesdaAPI
Reflection.Nãosetemaintençãodesercompletoecobrircadamétodoecadaclasse,
porémaideiaéapresentarasprincipaisclassescomsuasrespectivasfuncionalidades,
mostrandoatravésdeexemploscomopodemserutilizadas. Aofimdocapítulo,é
apresentadoumexemplomaiscompletoqueutilizadiversasfuncionalidadesque
foramapresentadas.
2.1 Obtendo informações sobre a sclasses
“Informação não éconhecimento”
–AlbertEinstein
QuandosecomeçaadesenvolverumsoftwareemJava,opontoinicialésempre
umaclasse.Paratrabalharcomreflexãonãoédiferente,poisaclasseprincipalqueé
opontodepartidaparaobtermosinformações sobreoselementosdeumprograma
éaclasse java.lang.Classquerepresentajustamenteumaclasse.Sendoassim,
oprimeiropassoparacomeçaratrabalharcomreflexãoéobtermosainstânciade
Classdaclassequequeremostrabalharcomela.
Paraentendermoscomoissofunciona,considereumobjetoqualquerdeuma
aplicação. Esseobjetoédescritopelasuaclasse,quedeterminaquaissão osseus
métodoseseusatributos,eporissopodemosdizerqueaclassepossuiasmetainfor-
mações arespeitodosobjetosdela.Porémquetipodecoisaessaclassepodeter?Se
aclassedescreveoobjeto,quemédescreveaclasse?
Aíéqueentraainstânciadaclasse Classquepossuitodasasinformações de
umaclasse.Essainstânciapossuiasmetainformações, nãodoobjeto,masdaclasse.
Comoquaissãoseusatributos,quaissãoosseusmétodosequalésuasuperclassee
suasinterfaces.Edaísurgemaisumadúvida:quemdescreveainstânciade Class?
26

## Página 33

CasadoCódigo Capítulo2. JavaReflectionAPI
Comovimos,osobjetossãodescritosporsuasclasses,entãoessainstânciaédescrita
pelaclasse Class. Equemdescreveaclasse Class? U m ainstânciadaprópria
classe Class!
Euseiqueissotudopodecausarumgrandenónanossacabeça,eaFigura2.1
mostradeformaesquemáticaoquefoidescritonosparágrafosanteriores. Oque
éimportanteentenderaquiéquequandotrabalhamoscomreflexão,estamostra-
balhandoumnívelacimadoquecostumamostrabalhar. Enquantonormalmente
trabalhamoscomobjetosquesão descritosporclasses,comreflexãotrabalhamos
comclassescujasinstânciasdescrevemasnossasclasses.
Figura2.1:Quempossuiasmetainformações dequem
Utilizando referênciasestáticas
Aformamaisdiretadeobtermosumainstânciade Classéatravésdeumarefe-
rênciaestáticadaclasse.Issoéutilizadoquandosabemosemtempodecompilação
qualclasseprecisaserreferenciada.Paraqueissosejafeito,utilizamosonomeda
classeseguidopor .class,oqueretornaainstânciade Classrespectiva.
27

## Página 34

2.1.Obtendoinformações sobreasclasses CasadoCódigo
Ocódigoapresentadoaseguirmostracomoasreferênciasestáticasaclasses
podemserutilizadas. Inicialmenteécriadaumainstânciade Classquerecebe
ainstânciareferenteaclasse String, daqualéimpressoonomenoconsole.
Podenão parecermuitoútilutilizarreferênciasestáticasdaclasse,poissejásei
comqualclassevoutrabalhar,paraqueprecisoutilizarreflexão?Porém,essasrefe-
rênciasestáticassão muitoutilizadasquandoprecisamospassarumainstânciade
Classcomoparâmetroparaummétodo,comotambéméapresentadonalistagem.
Listagem 2.1-UtilizandoreferênciasestáticasdeClass:
public class ReferenciaEstaticaClasse {
public static void main(String[] args) {
Class<String> classe = String.class;
System.out.println(classe.getName());
imprimeNomeClasse(Integer.class);
}
public static void imprimeNomeClasse(Class<?> classe){
System.out.println("Chamado o método com " +classe.getName());
}
}
Oquetalveztenhachamadoatençãonoexemploéofatodaclasse Classpossui
umtipogenérico.Essetipogenéricoérelativoaclassequeestásendorepresentada.
Dessaforma,comoserávistoposteriormentenessecapítulo,issopermiteainferên-
ciaderetornodealgunsmétodos,oqueevitaquesejamfeitoscastsdesnecessários.
Nocasodenãosabermosqualéotipo,podemossempreutilizarowildcard“?”
paradizerquenão sabemosotipodeclassequeserápassado. U mexemploéo
método imprimeNomeClass()querecebecomoparâmetrootipo Class<?>,
significandoquequalquertipopodeserpassadocomoparâmetro.Ousodetipos
genéricostambémpossibilitaquesejafeitaumacertarestriçãonotipodeclasseque
podeserpassadacomoparâmetro.Porexemplo,sedefinirmosotipodoparâmetro
como Class<? extends Serializable>,aceitamoscomoparâmetrosomente
instânciasde Classdetiposqueimplementamainterface Serializable.
A p e s a rdetiposprimitivosemJavanão seremconsideradosclasses,épossível
obterumarepresentação de Classparaeles. Paraisso,areferênciaestáticades-
sestipospodeserutilizada,comoporexemplo int.classe char.class.A t é
mesmoo voidpossuiumarepresentaçãodeClass,sendoobtidoatravésdaexpres-
28

## Página 35

CasadoCódigo Capítulo2. JavaReflectionAPI
são void.class.Naseção1.3,ondefizemosageraçãodomapa,essareferênciafoi
utilizadanométodo isGetter()paraverificarseelepossuíaretorno.
Recuperando a classe de um objeto
U m aoutraformamuitocomumdeseobterumainstânciade Classéatravésde
umobjetodessaclasse.Aclasse ObjectdefineométodogetClass()queretorna
arepresentaçãodaclassedaqueleobjeto.Arecuperaçãoda Classdessaformaé
muitocomumquandoserecebeoobjetocomoparâmetroedeseja-seinformações
sobresuaclasse. U mexemplodissofoimostradonocódigodageração domapa,
querecebiacomoparâmetroum Objecteutilizavaométodo getClass()para
obterasuaclasse.
Normalmente,essaformaderecuperaraclasseéutilizadaemmétodosmais
geraisquerecebemum Objectcomoparâmetroeutilizareflexãoparaconhecer
maissobreaclasseesaberquaismétodosinvocarouquaisatributosacessar.Isso
possibilitaqueobjetosdequalquerclassepossamserpassadoscomoparâmetroe
utilizadospelalógicadométodo.
Alistagemaseguirmostraumexemplodarecuperaçãodaclasseapartirdoob-
jeto.Otipogenéricoretornadopelométodo getClass()serásempre Class<?
extends Tipo>,onde“Tipo”representaotipodavariávelnaqualométodoestá
sendoinvocado.Issofazsentido,poisumavariáveldeumdeterminadotipopode
armazenarobjetosdeumsubtipo.Noexemplo,oobjetoédotipo Integer,mas
estásendoatribuídoaumavariáveldotipo Number.Sendoassim,apesardotipo
retornadopelo getClass()ser Class<? extends Number>,aoimprimiro
nomedoobjeto Classobtido,seráimpressonoconsole“java.lang.Integer”.
Listagem 2.2-Recuperandoasclassespelosobjetos:
public class RecuperandoPeloObjeto {
public static void main(String[] args) {
Number object = new Integer(100);
Class<? extends Number> c = object.getClass();
System.out.println(c.getName());
//...
}
}
29

## Página 36

2.1.Obtendoinformações sobreasclasses CasadoCódigo
U m aString com o nome da classe
Aúltimaformaqueseráapresentadadeseobterumainstânciade Classé
atravésdeum Stringcomonomecompletodaclasse. Essaformaémuitoútil
paraobternomesdeclassesdearquivosdeconfiguraçãoeinstanciaressasclassesa
partirdareflexão.Parafazerisso,éprecisochamarométodoestáticoforName()
daclasse Classpassandoonomedaclassecomoparâmetro.Aofazerisso,aclasse
seráprocuradapelamáquinavirtual,carregadacasoissoaindanãotenhasidofeitoe
retornada.Achamadadessemétodopodelançarum ClassNotFoundException
casoaclassenãosejaencontrada.
Uso d oCl a s s.forName () no JDBC
Talvez alguns sintam alguma familiaridade com a chamada
Class.forName(),poisjáviramissoserutilizadoemalgumlugar.
U musocomumdessachamadaéparacarregarodriverJDBCparao
acessoaobancodedados. Muitosdesenvolvedoresacabamutilizando
essachamadacomopartedeumareceitadeboloparaacessarumbanco
dedados,semsaberexatamenteoqueelaestáfazendo. Nessecaso,a
chamadafazcomqueodriverdeacessoaobancosejacarregadopela
máquinavirtual. Ocarregamentodessaclasseresultanaexecução de
umblocoestáticoqueregistraodrivernaclasse DriverManager,o
quefazcomqueasURLsdeconexãodaquelebancosejamrepassadas
paraaquelaclasse.
Para exemplificarmos o uso dessa abordagem, a listagem a seguir mostra
uma classe que lêum arquivode propriedades (o qual em cada linha possui
propriedade=valor), cominterfacesesuasrespectivasimplementações. Nesse
arquivo,as propriedadesseriam os nomesdas interfacese o valor o nomede
sua respectiva implementação que deve ser utilizada na aplicação. A classe
FornecedorImplementacoesrecebeonomedoarquivonoconstrutoreutiliza
aclasse Properties parafazeraleituradoarquivo. Paracadapropriedade,
o Class.forName()éutilizadoparaobterinstânciade Classdainterfacee
suarespectivaimplementação, adicionandoambasemummapaparaposterior
recuperação.
30

## Página 37

CasadoCódigo Capítulo2. JavaReflectionAPI
Listagem 2.3- Classe que lêarquivo de propriedades com interfaces e imple-
mentações:
public class FornecedorImplementacoes {
private Map<Class<?>, Class<?>> implementacoes = new HashMap<>();
public FornecedorImplementacoes(String nomeArquivo)
throws IOException, ClassNotFoundException{
Properties p = new Properties();
p.load(new FileInputStream(nomeArquivo));
for(Object interf : p.keySet()){
Class<?> interfType = Class.forName(interf.toString());
Class<?> implType = Class.forName(p.get(interf).toString());
implementacoes.put(interfType, implType);
}
}
public Class<?> getImplementacao(Class<?> interf){
return implementacoes.get(interf);
}
}
A classe FornecedorImplementacoes pode ser utilizada para confi-
gurar em uma aplicação qual a implementação de cada interface. O método
getImplementacao()recebecomoargumentoainterfaceeretornaaclasseda
implementação.Ocódigoaseguirmostracomoaclasseseriautilizada.Elaécriada
passando como parâmetroo arquivo “implementacoes.prop”e tenta recuperar
a implementação de uma interfacechamada DAO. Caso a implementação seja
retornada,onomedaclasseseráimpressonoconsole,ecasocontrárioamensagem
deerroseráexibida.
Listagem 2.4-ExemplodeusodaclasseFornecedorImplementacoes:
public static void main(String[] args){
try {
FornecedorImplementacoes f =
new FornecedorImplementacoes("implementacoes.prop");
Class<?> impl = f.getImplementacao(DAO.class);
System.out.println("Implementação recuperada: "+impl.getName());
} catch (ClassNotFoundException | IOException e) {
31

## Página 38

2.2.Trabalhandocomclasses CasadoCódigo
System.out.println(
"Problemas ao obter implementacões:" + e.getMessage());
}
}
2.2 Trabalhando co m classes
Depoisdeobterarepresentaçãodeumaclasseatravésdeumainstânciade Class,
épossívelobterdiversasinformações alémdecriarinstâncias.Comofoiditonain-
trodução,aAPIReflectiondalinguagemJavanãopermitequeasclassesexistentes
sejammodificadasoumanipuladas,sendotodasasinformações somenteparalei-
tura. OquepodesermanipuladoapartirdaAPIReflectionsão osobjetosdessas
classes,nosquaisosatributospodemsermodificadoseosmétodospodemserinvo-
cados.Nessaseçãoserávistoquaisinformações podemserextraídasdeumaclasse
equaissãoasformasparainstanciá-laatravésdereflexão.
Acessando informaçõ e sde classes
Atravésdeumainstânciadeumobjetodotipo Classépossívelrecuperardi-
versasinformações deumaclasse.Como Classéutilizadaparaarepresentaçãode
qualquertipo,mesmoqueessenãosejaexatamenteumaclasse,existemmétodosque
podemserutilizadosparaverificaroqueaquelainstânciaestárepresentando,como
isInterface(), isPrimitive(), isEnum()e isArray().Arecuperaçãode
métodoseatributosseráabordadanasseções seguintesdessecapítulo.
Arecuperaçãodosmodificadoresdeumaclassejáéumpouquinhomaiscom-
plicada,poisométodo getModifiers()retornauminteiroquepossuiumare-
presentaçãodequaissãoosmodificadoresdaclasse.Essesmodificadoresincluem,
paraumaclasse, public, protected, private, final, static, abstracte
interface.Paramétodoseatributosarecuperaçãodemodificadoresésimilar,po-
rémosatributostambémpossuemmodificadorescomo volatilee transient
eosmétodospodempossuirosmodificadores synchronized, strictfp e
native.Essesoutrosmodificadorestambémsãoincluídosquandoaplicável.
Paradecodificarosmodificadores,verificandosealgumestápresente,aclasse
Modifierprecisaserutilizada.Essaclassepossuimétodosestáticosquerecebemo
inteiroretornadoeverificamseummodificadorespecíficoestápresente.Alistagem
aseguirmostraumcódigoqueexemplificaesseprocesso,verificandoseaclasseé
32

## Página 39

CasadoCódigo Capítulo2. JavaReflectionAPI
abstrata.
Listagem 2.5-Acessandoosmodificadoresdaclasse:
int modificadores = clazz.getModifiers()
if(Modifier.isAbstract(modificadores)){
//codigo se a classe for abstrata
}
U mtipodeverificação quefrequentementeprecisamosrealizaremrelação a
umaclasseéarespeitodasuarelação comoutrostiposeobjetos. Aoperação
instanceofépossívelserrealizadacomumobjetoeumareferênciaestáticade
umaclasse.OmétodoisInstance()possuiumalógicasimilar,porémutilizando
umainstânciade Class.Eleverificaseoobjetopassadocomoparâmetroéuma
instânciadaquelaclasse.
Outrométodorelacionadoatipagem,verificaseumobjetodaclassepassada
comoparâmetropodeserconvertidonaclasseondeométodoestásendochamado.
Ométodo isAssignableFrom()iráretornar truecasoaclasseondeeleestá
sendochamadosejaumasuperclasse,umainterfaceouaprópriaclassequeestá
sendopassadacomoparâmetro.
Paraexemplificararecuperação deinformações daclasse, abaixosegueum
exemplodeaplicaçãoemqueousuárioescreveonomedaclassenoconsoleeele
imprimeahierarquiadeclasseseinterfaces. Nométodo main()oprograma
lêonomedaclasseutilizandoaclasse Scannereobtémainstânciade Class
comométodo forName().Emseguida,ométodo imprimirHierarquia()é
chamadopassandoaclassecomoparâmetro.
Listagem 2.6-Classequeimprimeahierarquiadeclasseseinterfaces:
public class InformacaoClasse {
public static void main(String[] args) {
System.out.println(
"Entre com o nome da classe que deseja informação:"
);
Scanner in = new Scanner(System.in);
String nomeClasse = in.nextLine();
try {
Class<?> c = Class.forName(nomeClasse);
33

## Página 40

2.2.Trabalhandocomclasses CasadoCódigo
imprimirHierarquia(c, 1);
} catch (ClassNotFoundException e) {
System.out.println(
"A classe "+nomeClasse+" não foi encontrada"
);
}
in.close();
}
private static void imprimirHierarquia(Class<?> c, int nivel){
List<Class<?>> lista = getSuperclasseEInterfaces(c);
String recuo = "";
for(int i=0; i<nivel; i++){
recuo+=" ";
}
for(Class<?> clazz : lista){
System.out.println(recuo+"|-> "+clazz.getName());
if(clazz != Object.class){
imprimirHierarquia(clazz, nivel+1);
}
}
}
private static List<Class<?>> getSuperclasseEInterfaces(Class<?> c){
List<Class<?>> lista = new ArrayList<>();
if(c.getSuperclass() != null)
lista.add(c.getSuperclass());
lista.addAll(Arrays.asList(c.getInterfaces()));
return lista;
}
}
OmétodoimprimirHierarquia()possuiumalógicarecursivaeirásercha-
madonovamenteparacadaclasseouinterfaceencontrados,parandoaoseencontrar
aclasse Object.Oparâmetro nivelrepresentaaprofundidadedaclassenahi-
erarquiaeéutilizadoparadeterminaraquantidadedeespaçosantesdaclasseser
impressanoconsole.Dessaforma,aimpressãodasclassesficarácomumformato
similaraodeumaárvore.Acadachamadarecursiva,adiciona-seumnoparâmetro
nivel.
Ométodo getSuperclasseEInterfaces()retornaumalistade Class
comsuasuperclasseeasinterfacesdiretamenteimplementadasporela. Observe
queosmétodos getSuperclass()e getInterfaces()são utilizadospara
34

## Página 41

CasadoCódigo Capítulo2. JavaReflectionAPI
isso. Ométodo getInterfaces() iráretornarasinterfacesimplementadas
caso o Class representeuma classe e as interfacesestendidascaso seja uma
interface. Ocódigo abaixoapresentaasaídadosoftwarecasosejafornecidaa
entrada“java.util.ArrayList”.
Listagem 2.7-SaídadoprogramaparaaclasseArrayList:
Entre com o nome da classe que deseja informação:
java.util.ArrayList
|-> java.util.AbstractList
|-> java.util.AbstractCollection
|-> java.lang.Object
|-> java.util.Collection
|-> java.lang.Iterable
|-> java.util.List
|-> java.util.Collection
|-> java.lang.Iterable
|-> java.util.List
|-> java.util.Collection
|-> java.lang.Iterable
|-> java.util.RandomAccess
|-> java.lang.Cloneable
|-> java.io.Serializable
Criando instâncias
U m aclassenão énadasemassuasinstâncias! Sequeremoscarregarclasses
dearquivosdeconfiguração parautilizarmosnaaplicação, éprecisocriarinstân-
ciasdelas. Issopodeserfeitofacilmenteatravésdométodo newInstance()de
Class! Essemétodocriaumanovainstânciadaclasseapartirdeumconstru-
torvazio. Aoinvocaressemétodoexistemduasexceções queprecisamsertrata-
das: InstantiationExceptione IllegalAccessException. Aprimeira
serálançadacasonão existaumconstrutorvazioouainstânciade Classrepre-
senteumaclasseabstrata,interface,tipoprimitivoouarray.Asegundaexceçãojá
serálançadacasooconstrutornãoestejaacessível,porexemplo,porserprivado.
35

## Página 42

2.2.Trabalhandocomclasses CasadoCódigo
Frameworks que pedem construtores se m parâmetros
Existemváriosframeworksqueemsuadocumentação dizemque
parasuasclassespoderemsermanipuladasporele,queprecisampos-
suirumconstrutorsemparâmetro.Agoravocêjásabequeissoéporque
eleutilizaessemétodo newInstance()parainstanciá-la.Repareque
issoécomumquandooframeworkprecisainstanciarclassesdasuaapli-
cação.Issoécomum,porexemplo,emframeworkswebparaclassesque
representamcontrollers,quesãocriadasegerenciadaspeloframework
paratratarrequisições. Outroexemploocorreemframeworksdemape-
amentoobjeto-relacional,osquaisprecisaminstanciarasclassesmape-
adasparaobancoquandoinformações sãorecuperadas.
Ométodo newInstance()temumsérioproblemaemrelação aexceções!
Casooconstrutorlanceumaexceção,mesmoquechecada,essaexceçãoserápro-
pagadadiretamenteparaométodoquetentoucriarainstância.Issosemexigirque
essaexceçãosejatratada!V e j aumexemplodissonocódigoapresentadonalistagem
aseguir. Quandoeleforexecutado,a IOExceptionlançadanoconstrutorserá
propagadaparaométodo main()semcairemnenhumdosblocos catch.Para
conseguirtrataressaquestão,deve-seutilizardiretamenteaclasse Constructor.
Listagem 2.8-Tratamentodeexceções comométodonewInstance():
public class CriacaoClasse {
public CriacaoClasse() throws IOException{
throw new IOException();
}
public static void main(String[] args){
try {
CriacaoClasse obj = CriacaoClasse.class.newInstance();
} catch (InstantiationException e) {
e.printStackTrace();
} catch (IllegalAccessException e) {
e.printStackTrace();
}
}
}
36

## Página 43

CasadoCódigo Capítulo2. JavaReflectionAPI
Os construtores podem ser obtidos de uma classe atravésdos métodos
getConstructor()ou getConstructors().Oprimeirométodorecebecomo
parâmetroostiposdosparâmetrosdoconstrutor,permitindorecuperarumconstru-
torespecífico.Essemétodoutilizaorecursodalinguagemde varargsparapermitir
quesepassediversosparâmetroscomostipos. Osegundométodorecuperauma
listacomtodososconstrutoresdaclasse. Parautilizaroconstrutor,bastachamar
ométodo newInstance()passandoosparâmetrosadequados.Damesmaforma
quearecuperaçãodoconstrutor,essemétodotambémutiliza varargsparaquese
possapassarquandoparâmetrosforemnecessários.
Em relação as exceções, a recuperação de um construtor específicopode
lançar o erro NoSuchMethodException caso aquele construtor não exista.
A invocação de um construtor,alémdas duasexceções que podem ser lança-
das pelo newInstance() de Class, duas outras exceções podem ser lan-
çadas. A exceção IllegalArgumentException élançada quandoa quan-
tidade e os tipos dos parâmetros não corresponderem aos do construtor e
InvocationTargetExceptionéaexceçãoqueencapsulaumaexceçãoqueélan-
çadapeloconstrutor.Nessecaso,aexceçãooriginalpodeserrecuperadaatravésdo
método getTargetException().
O código abaixo mostra o exemplo do uso de um construtor. A classe
UsoConstrutorpossuiumconstrutorquerecebeuma Stringcomoargumento.
O método getConstructor() éutilizado para recuperar o construtor e o
método newInstance()paraacriaçãodoobjeto.Observequenotratamentode
InvocationTargetExceptionaexceção originalérecuperadaeimpressano
console.
Listagem 2.9-Exemplodecriaçãodeinstânciacomconstrutores:
public class UsoConstrutor {
public UsoConstrutor(String s){
System.out.println("Construtor invocado com: "+s);
}
public static void main(String[] args)
throws NoSuchMethodException, SecurityException {
Class<UsoConstrutor> c = UsoConstrutor.class;
Constructor<UsoConstrutor> constr =
c.getConstructor(String.class);
try {
37

## Página 44

2.2.Trabalhandocomclasses CasadoCódigo
UsoConstrutor obj = constr.newInstance("teste");
} catch (InstantiationException e) {
e.printStackTrace();
} catch (IllegalAccessException e) {
e.printStackTrace();
} catch (IllegalArgumentException e) {
e.printStackTrace();
} catch (InvocationTargetException e) {
System.out.println(
"Exceção lançada pelo construtor: "+e.getTargetException());
}
}
}
Quando criar objetos utilizando reflexão?
Acriaçãodeobjetosutilizadoreflexãoéindicadaquandonãoseco-
nheceemtempodecompilaçãoaclassequevaiserinstanciada.Nocaso
dehaveremdiversasimplementações paraumaclasse,mastodasserem
conhecidas,umpadrão decriação, comoFactoryMethodouBuilder,
podeserutilizadoparadeterminaraclassequeserácriada.Acriaçãode
objetosatravésdereflexãoéindicadaquandosedesejaquenovasclas-
sespossamsercriadaseconfiguradascomopluginsdeumsoftwareou
frameworkexistente.
Melhorando o fornecedor de implementaçõ e s
Apartirdoquefoivistonesseseção podemosmelhoraraimplementação da
classe FornecedorImplementacoes. Aprimeiraverificação seránaleiturado
arquivo,ondepodemosverificarseaclasseutilizadacomochaveérealmenteuma
interfaceouumaclasseabstrataeaclassepassadacomovalorérealmenteumaim-
plementaçãoconcretadela.Outramodificaçãoéqueaoinvésderetornarsomente
aclassedaimplementação,vamostertambémmétodosparajáretornarinstâncias
dasimplementações.
Começando pelas verificações, inicialmentevamos criar métodosauxiliares
queverificampropriedadesdasclasses,conformemostradonalistagemaseguir.
O método isInterfaceOuAbstract() verificase o Class passado como
38

## Página 45

CasadoCódigo Capítulo2. JavaReflectionAPI
parâmetroéumainterfaceouumaclasseabstrata. Observequeaclasseauxiliar
Modifiersfoiutilizadaparaverificarseomodificador abstractestápresente.
Emseguidatemosométodo isAbstracaoEImplementacao()queverificase
aprimeiraclasseéumaabstração,seasegundaclasseéumaimplementaçãoesea
implementaçãoédotipodaabstração.
Listagem 2.10-Métodosauxiliaresparaverificação:
private boolean isInterfaceOuAbstract(Class<?> c){
return c.isInterface() || Modifier.isAbstract(c.getModifiers());
}
private boolean isAbstracaoEImplementacao
(Class<?> interf, Class<?> impl){
return isInterfaceOuAbstract(interf) && !isInterfaceOuAbstract(impl)
&& interf.isAssignableFrom(impl);
}
A listagem a seguir mostra como o construtor da classe
FornecedorImplementacoes pode ser modificado para incluir a verifica-
ção. Observe que depois que os objetos Class são criados, caso o método
isAsbtracaoEImplementacao() retorne false, umaexceção serálançada
paraindicarumerrodeconfiguraçãonoarquivo.
Listagem 2.11-Construtormodificadoparafazerasverificações:
public FornecedorImplementacoes(String nomeArquivo) throws Exception{
Properties p = new Properties();
p.load(new FileInputStream(nomeArquivo));
for(Object interf : p.keySet()){
Class<?> interfType = Class.forName(interf.toString());
Class<?> implType = Class.forName(p.get(interf).toString());
if(!isAbstracaoEImplementacao(interfType, implType)){
throw new Exception("Erro na configuração do arquivo " +
nomeArquivo + " : " + interfType.getName() +
" não é abstração de " + implType.getName());
}
implementacoes.put(interfType, implType);
}
}
39

## Página 46

2.2.Trabalhandocomclasses CasadoCódigo
Asegundapartequeseráadicionadanofornecedordeimplementações éaque
criaosobjetosapartirdaclassedarespectivaimplementação.Porémnãoqueremos
quesejautilizadoapenasoconstrutorsemparâmetros.Oobjetivoéqueapartirdos
parâmetrospassadosparaacriaçãodoobjeto,sejaencontradoumconstrutorque
possareceberaquelesparâmetros.Alistagemaseguirapresentaummétodoauxi-
liarqueseráutilizadoparaacharumconstrutoradequadoaosparâmetrospassados.
Listagem 2.12-Métodosauxiliarquebuscaumconstrutoradequado:
private Constructor<?> acharConstrutor(Class<?> c, Object... objs)
throws Exception{
for(Constructor<?> constr : c.getConstructors()){
Class<?>[] params = constr.getParameterTypes();
if(params.length == objs.length){
boolean erro = false;
for(int i=0; i<objs.length && !erro; i++){
if(!params[i].isInstance(objs[i]))
erro = true;
}
if(!erro)
return constr;
}
}
throw new Exception("Construtor não encontrado");
}
Inicialmente,ométodorecuperaalistadeconstrutoresapartirdométodo
getConstructors().Eseguida,paracadaconstrutorsãofeitasverificações para
verseeleéadequadoaosparâmetros.Aprimeiraquestãoverificadaéseonúmerode
parâmetrosdoconstrutoréigualaonúmerodeobjetospassadoscomoparâmetro.
Emseguida,paracadaparâmetroéverificadoseoobjetopossuiotipoexigidopara
oparâmetro,utilizandoométodo isInstance().Casoaverificaçãosejapositiva
paratodososparâmetros,oconstrutoréretornadoparaométodo.Emcasonega-
tivo,umaexceçãoélançadaindicandoqueumconstrutorparaaquelesparâmetros
nãofoiencontrado.Pelalógica,épossívelperceberqueoprimeiroconstrutorque
seencaixeseráretornado.
Paracompletaressafuncionalidade,apróximalistagemapresentaométodo
criarInstancia()queefetivamentecriaoobjeto. Essemétodoinicialmente
utiliza o método getImplementacao() para recuperar a implementação da
40

## Página 47

CasadoCódigo Capítulo2. JavaReflectionAPI
interfaceouclasseabstratapassadacomoparâmetro.Emseguida,ométodocriado
nalistagemanterioréutilizadopararecuperaroconstrutor,oqualéutilizadopara
acriaçãodainstânciaatravésdométodo newInstance().
Listagem 2.13-Criaçãodainstânciaatravésdoconstrutor:
public Object criarInstancia(Class<?> interf, Object... objs)
throws Exception{
Class<?> impl = getImplementacao(interf);
Constructor<?> constr = acharConstrutor(impl, objs);
return constr.newInstance(objs);
}
U m aressalvaemrelaçãoaessaimplementaçãoéqueelanãoiráfuncionarcaso
oconstrutorrecebatiposprimitivoscomoparâmetros. Oproblemaéqueotipo
primitivoseráconvertidoparasuarespectivaclasse w r a p p e raoserpassadoparao
varargsnoarraydeobjetos.Dessaforma,ainvocaçãodométodo isInstance()
iráretornar falseporcausadessaconversão. Deixocomoexercícioaosleitores
fazeressaimplementaçãofuncionarparaconstrutoresquerecebemtiposprimitivos.
Cuidado com os tipos primitivos!
Ostiposprimitivossãoumagrandepedranosapadodequemtraba-
lhacomreflexão.A p e s a rdoseutiposerrepresentadopelaclasse Class,
muitasvezeséprecisofazeradistinçãodostiposprimitivosetratá-los
comocasosespeciais. Oexemplodabuscadeconstrutoreséumcaso
emqueostiposprimitivosprecisariamsertratadosseparadamente,tro-
candoseutipopelodeumaclasse w r a p p e rouutilizandoumcondicional
paracadatipoprimitivo.Sendoassim,nãoseincomodeaoterquecriar
umasériadecondicionaisparatratardeformaespecialcadaumdosti-
posprimitivos,poisnosframeworksquedesenvolvipreciseifazerisso
algumasvezes.
2.3 Manipulando objetos
Nasseçõesanterioresvimoscomorecuperarareferênciadeumaclasse,comoacessar
suasinformações ecomocriarnovasinstâncias.Essaseçãomostracomoépossível
41

## Página 48

2.3.Manipulandoobjetos CasadoCódigo
manipularosobjetoscomreflexãoatravésdoacessoaosseusatributosedainvo-
caçãodeseusmétodos.Existemalgumasquestões mostradasparaumaclasse,cuja
recuperaçãoésimilarquandolidamoscomatributosemétodos.Porexemplo,are-
cuperaçãodemodificadoresemmétodoseatributostambéméfeitacomométodo
getModifiers()etambémédecodificadacomaclasse Modifier.Essasques-
tões quesãomuitosimilaresnãoserãoapresentadasnovamente.
Acessando e alterando valores de atributos
AtravésdaAPIReflectionépossívelrecuperarosatributosdeumaclasse,que
são representadospelaclasse Field. Apartirdessasreferênciasdosatributos
seus valores podem ser acessados e modificados. Existem dois métodospara
retornaralistadeatributosdeumclasse: getFields()queretornatodosos
atributospúblicose getDeclaredFields()queretornatodososatributosque
foramdeclaradosnaquelaclasse.Paraexemplificarmosadiferençaentreessesdois
métodos,considereocódigoapresentadonalistagemseguinte.
Listagem 2.14- Programaque mostra a diferença entregetFields() e getDecla-
redFields():
public class SuperclasseAtributo {
private int atributoSuperclasseUm;
public String atributoSuperclasseDois;
}
public class AcessoAtributo extends SuperclasseAtributo{
private int atributoUm;
public String atributoDois;
public static void main(String[] args) {
System.out.println("Retornado pelo getFields()");
for(Field f : AcessoAtributo.class.getFields()){
System.out.println(
"- "+f.getType().getSimpleName() + " " + f.getName());
}
System.out.println("Retornado pelo getDeclaredFields()");
for(Field f : AcessoAtributo.class.getDeclaredFields()){
System.out.println(
"- "+f.getType().getSimpleName() + " " + f.getName());
42

## Página 49

CasadoCódigo Capítulo2. JavaReflectionAPI
}
}
}
O resultado da execução desse programa estáapresentado na listagem a
seguir. Observequeométodo getFields()retornatodososatributospúbli-
cos,incluindotantoosdaprópriaclassequantoosdasuperclasse. Jáométodo
getDeclaredFields()retornatodososatributosdeclaradosnaprópriaclasse,
incluindoosquesão privados, porémnão incluindonenhumdeclaradonasu-
perclasse. Sequisermostodososatributos,incluindoosprivadosdaclasseedas
superclasses, precisamos ir percorrendo a hierarquia de classes e recuperando
osatributosdecadaumacom getDeclaredFields(). Deformasimilar,se
quisermosacessarumatributoespecíficodaclasse,tambémtemosdoismétodos
comcomportamentoanálogo,sendoeles getField()e getDeclaredField().
Listagem 2.15- Saídado programacom a diferença de getFields()para getDe-
claredFields():
Retornado pelo getFields()
- String atributoDois
- String atributoSuperclasseDois
Retornado pelo getDeclaredFields()
- int atributoUm
- String atributoDois
Asduasações quepodemosfazercomoatributodeumobjetosãoarecuperação
eamodificaçãodeseuvalor.Aclasse Fieldpossuidoismétodosqueexecutam
respectivamenteessasações, sendoelesométodo get() eométodo set().
Ambososmétodosrecebemcomoparâmetrooobjetonoqualesseatributodeve
seracessado. Paraexemplificaroacessodosvaloresdeumatributo,considerea
classechamada ExemploClasserepresentadanapróximalistagem.Observeque
elapossuiumatributopúblico,umatributoprivadoeumatributoestáticoepúblico.
Listagem 2.16- Exemplo de classe com atributosa serem acessados por refle-
xão:
public class ExemploClasse {
public String publico;
private String privado;
43

## Página 50

2.3.Manipulandoobjetos CasadoCódigo
public static String estatico;
}
Alistagemaseguir,mostraumcódigoqueacessacadaumdessesatributos,
inserindocomovalorseupróprionomeeemseguidarecuperandoessevalore
imprimindo-onoconsole. Ométodo escreverLerAtributo()recebecomo
parâmetroo Fieldeoobjetonoqualeleprecisaserrecuperado. Essemétodo
usaosmétodos sete getparaprimeiroatribuironomedoatributocomovalor
edepoisrecuperá-lo.Aexceção IllegalArgumentExceptioniráacontecer
quandoumobjetodeumtipoerradoforpassadoparaosmétodosde Field,o
quenão precisamosnospreocuparmuitonessecaso. Poroutrolado,aexceção
IllegalAccessExceptioniráocorrercasoocorraatentativadeacessoaum
atributocujoacessonãoépermitido.
Listagem 2.17-Acessoadiferentestiposdeatributosporreflexão:
public class EscrevendoLendoAtributos {
public static void main(String[] args)
throws NoSuchFieldException, SecurityException {
ExemploClasse instancia = new ExemploClasse();
Class<?> clazz = instancia.getClass();
escreverLerAtributo(clazz.getField("publico"), instancia);
escreverLerAtributo(
clazz.getDeclaredField("privado"), instancia);
escreverLerAtributo(clazz.getField("estatico"), null);
}
public static void escreverLerAtributo(Field f, Object instancia){
try {
f.set(instancia, f.getName());
Object valor = f.get(instancia);
System.out.println("Escrito e lido o atributo = "+valor);
} catch (IllegalArgumentException e) {
System.out.println("Problemas ao acessar atributo "
+f.getName()+": "+e.getMessage());
} catch (IllegalAccessException e) {
System.out.println("Problemas de acesso no atributo "
+f.getName()+": "+e.getMessage());
}
}
44

## Página 51

CasadoCódigo Capítulo2. JavaReflectionAPI
}
Ométodo main()criaumainstânciadaclasse ExemploClasseerecupera
suarespectivainstânciade Class,apartirdaqualosatributossãorecuperados.Ob-
servequeoatributoprivadoprecisaserrecuperadocom getDeclaredField(),
poisométodo getField()sóiráencontrarosatributospúblicos.Outraobserva-
çãoimportanteéquenãoénecessáriaumainstânciaparaqueumatributoestático
sejaacessado,vistoqueeleestávinculadoaclasse.
Aoexecutaresseprograma,oatributoprivadonãoconseguiráseracessadoea
exceção IllegalAccessExceptionserálançada.Casoessecódigoestivessena
própriaclasse ExemploClasse,esseatributoestariaacessíveleoerronãoaconte-
ceria.Éimportanteressaltarquepormaisqueosatributosprivadosestejamacessí-
veisparaserrecuperadosviareflexão,nemsempreelespoderãoseracessados.Isso
vaidependerdeondeocódigoestásendoexecutadoeasmesmasrestrições quese
aplicariamaoacessodireto,tambémseaplicamareflexão.Oúltimocapítulodesse
livromostracomoessaregrapodeserburladaparapermitiroacessodemembro
privadosatravésdaAPIReflection.
Invocando métodos
Aofalarsobremétodos,nãosobroumuitacoisaaserdita,poisarecuperaçãodos
métodosésimilararecuperação deatributoseainvocação dosmétodostambém
nãoémuitodiferentedachamadadeconstrutores.Arecuperaçãodeumconjunto
demétodosésimilararecuperaçãodeatributos,havendodoismétodoschamados
getMethods()e getDeclaredMethods().EmJava,ummétodoéidentificado
unicamentepeloseunomeepelosseusparâmetros,poispodemexistirmétodos
comomesmonomeequerecebeparâmetrosdiferentes.Dessaforma,osmétodos
getMethod()e getDeclaredMethod()recebemcomoprimeiroparâmetroo
nomeeemseguidaumnúmerovariáveldeobjetosdotipo Classpararepresentar
ostiposdosparâmetros.
Osmétodossãorepresentadospelaclasse Methodepossuemdiversasinforma-
ções interessantesdeseremrecuperadas,quepodemserutilizadasquandoprocu-
ramosummétodoadequadoparaserinvocada. Ométodo getReturnType()
retornaotipodoretornodométodo,quepodeserutilizadoparasaberoque
deve se esperar de sua invocação. Se o métodoem questão não possuir re-
torno,essemétodoiráretornarotipo void.class. Outrométodointeressante
éo getParameterTypes()queretornaumarraycomostiposdosparâme-
45

## Página 52

2.3.Manipulandoobjetos CasadoCódigo
tros. Noexemploapresentadonaintrodução desselivro,essesdoismétodosfo-
ramutilizadosparaverificarseométodocomeçadocom“ g e t ”retornavaalgodi-
ferentede voidenão possuíaparâmetros. U m aoutrainformação importante
dosmétodossão ostiposdeanotações lançados,oquepodeserrecuperadocom
getExceptionTypes().
Ainvocaçãodemétodoséfeitaapartirdométodoinvoke(),querecebecomo
primeiroparâmetrooobjetoemqueométododeveserinvocadoeemseguidaos
valoresquedevemserpassadoscomoargumento.Essemétodoiráretornarore-
tornodométodoqueestásendoinvocado.Assimcomonainvocaçãodeconstruto-
res,casoumaexceçãosejalançadapelométodo,serálançadaumaexceçãodotipo
InvocationTargetException,atravésdaqualaexceçãooriginalpodeserrecu-
peradacomométodo getTargetException(). Eassimcomooacessoaatri-
butosestáticos,ummétodoestáticopodeserinvocadopassandocomo nullopri-
meiroparâmetro,oqualrepresentaoobjetoondeométododeveserinvocado.
Paraexemplificarainvocaçãodemétodosporreflexão,vamosmostrarumexem-
ploondeousuárioescolheaclasseeométodoqueeledesejaexecutar.Apartirdessa
escolha,oprogramairáverificarquaissãoosparâmetrosnecessáriosparaparaexe-
cução daquelemétodoepedirqueousuárioentrecomcadaumdeles. Porfim,
ométodoseráinvocadocomosparâmetrospassadoseoretornoseráexibidono
console.Éimportanteressaltaraquiqueoobjetivodesseexemploésimplesmente
ilustrarcomcódigoainvocaçãodemétodosviareflexão,enãorealmentesuportara
invocaçãodequalquertipodemétodovialinhadecomando.
Paracomeçaroexemplo,apartirdaentradadousuáriodonomedométodo
precisaremosprocurar esse métodoentreos métodosda classe. Como não é
possívelrecuperarummétododiretamentede Classapenaspeloseunome,pois
ostiposdosparâmetrosseriamtambémnecessários,seránecessáriopercorrertoda
listademétodosprocurandoummétodoentradopelousuário.Sendoassim,o
métodoauxiliarapresentadonalistagemaseguirrealizaessaprocurademétodo
emumaclasse,retornandooprimeiroqueforencontradocomonomepassado
comoparâmetro.
Listagem 2.18-Métodoauxiliarqueprocuraométodopeloseunome:
private static Method acharMetodoPeloNome(Class<?> c, String nome)
throws Exception{
for(Method m : c.getMethods()){
if(m.getName().equals(nome)){
46

## Página 53

CasadoCódigo Capítulo2. JavaReflectionAPI
return m;
}
}
throw new Exception("Método "+nome+" não encontrado");
}
Nalistagemaseguir,estáapresentadoocorpoprincipaldoprogramaqueexe-
cutaométododeacordocomasentradasdousuário.Inicialmenteelesolicitaao
usuárioonomedaclasseeemseguidaonomedométodo.Ométodoserápro-
curadoutilizandoométodo acharMetodoPeloNome()apresentadonalistagem
anterior.
Apartirdométodorecuperado,ostiposeaquantidadedosparâmetrossãore-
cuperadosparaseremsolicitadosaousuário.Paracadaparâmetro,ésolicitadopara
ousuárioqueentrecomumvalor.Essevalorélidocomouma Stringeéutilizado
paracriaçãodoobjetoqueseráovalordoparâmetro,atravésdainvocaçãodeum
construtorquerecebeuma Stringcomoargumento.Sendoassim,seotipodopa-
râmetrofor Integer,seráinvocadoseuconstrutorpassandoa Stringlidacomo
parâmetro.
Depoisquetodososparâmetrosforemlidos,ométodoéinvocadoutilizando
método invoke()eseuresultadoéimpressonoconsole.
Listagem 2.19- Código que executada um métodode acordocom as entradas
dousuário:
public class ExecutaMetodo {
public static void main(String[] args) throws Exception{
System.out.println(
"Entre com o nome da classe "
+ "com método que deseja executar:");
Scanner in = new Scanner(System.in);
String nomeClasse = in.nextLine();
Class<?> c = Class.forName(nomeClasse);
System.out.println("Entre com o nome do método:");
String nomeMetodo = in.nextLine();
Method m = acharMetodoPeloNome(c, nomeMetodo);
Object[] params = new Object[m.getParameterTypes().length];
for(int i=0; i<params.length; i++){
Class<?> paramType = m.getParameterTypes()[i];
47

## Página 54

2.3.Manipulandoobjetos CasadoCódigo
System.out.println("Parametro "+(i+1)+
" ("+paramType.getName()+")");
String valor = in.nextLine();
params[i] = paramType.
getConstructor(String.class).newInstance(valor);
}
Object retorno = m.invoke(c.newInstance(), params);
System.out.println("O método retornou: " + retorno);
in.close();
}
}
V a l eressaltarquediversascoisaspoderiamdarerradonaexecução dessemé-
todo,queestásimplesmentedeclarandoquepodejogarumaexceção enão estão
sendotratadasdaformaapropriada.Eleassume,porexemplo,queaclasseentrada
pelousuáriopossuiráumconstrutorvazioequeostiposdosparâmetrosterãocons-
trutoresquerecebemuma Stringcomoparâmetro.Emumaaplicaçãoreal,seria
importantetrataroscasosemqueessaspremissasnão são verdade. Porexemplo,
sequiséssemosdarsuporteaparâmetrosquesãotiposprimitivos,precisaríamosde
umtratamentoespecialparacadaumdeles.
A classe apresentadaa seguir, chamada Utilitaria, possui um método
queseráutilizadoparatestarmosaexecução de métodosatravésdoprograma
desenvolvido.Ométodo repetir()dessaclasserecebetrêsparâmetrosepossui
umalógicabemsimples.Eleiráretornaruma Stringemqueoparâmetro base
érepetidosegundooparâmetro vezes,separadopeloparâmetro divisor.
Listagem 2.20-Classeutilizadaparatestaraexecuçãodemétodos:
public class Utilitaria {
public String repetir(String base, String divisor, Integer vezes){
String retorno = base;
for(int i=1; i<vezes; i++){
retorno += divisor+base;
}
return retorno;
}
}
Alistagemaseguirapresentaasaídadoconsoleapartirdaexecução dessa
48

## Página 55

CasadoCódigo Capítulo2. JavaReflectionAPI
programa. Observequeonomedaclasse Utilitariaeonomedométodo
repetir()sãoentradoscomoasduasentradasiniciaisdousuário.Emseguida,o
programapedeovalorparacadaparâmetro,mostrandootipoesperadoparaele.
Porfim,depoisdeentrarcomvaloresparaostrêsparâmetros,éexibidooretorno
dométodocomoesperado.
Listagem 2.21-Saídadoprogramaqueexecutaométodorepetir():
Entre com o nome da classe com método que deseja executar:
org.casadocodigo.Utilitaria
Entre com o nome do método:
repetir
Parametro 1 (java.lang.String)
teste
Parametro 2 (java.lang.String)
##
Parametro 3 (java.lang.Integer)
4
O método retornou: teste##teste##teste##teste
Quando executar métodos p o rreflexão?
Aorientaçãoaobjetosprovêmeiosdevocêinvocarmétodosemum
objetoquevocênãoconhecepreviamente.Issopodeserfeitodefinindo
umaabstração,comoumainterfaceouumaclasse,quepossuaessamé-
todoeutilizandoopolimorfismoparainvocaressemétodoemqualquer
objetoqueobedeçaaessaabstração.Nessescasos,quandoépossívelter
umaabstraçãoquerepresentaométodoquedeveserinvocado,areflexão
nãoprecisaserutilizada.Poroutrolado,sevocêprecisalidarcomclas-
sesquepossuemmétodosdiferentesenãofazsentidocompartilharem
umamesmaabstração,essaéadeixaparaainvocaçãodessesmétodos
porreflexão. U mbomexemplodessecasosãoosJavaBeans,quepos-
suemdiversosmétodosgetteresetterdiferentesenão épossívelcriar
umainterfacecomumquecaptureessacaracterística.
49

## Página 56

2.4. Procurandométodoseatributosparavalidação CasadoCódigo
2.4 Procurando métodos e atributos para v alida-
ção
Duranteasseções anterioresforamapresentadosváriosexemplosquedemonstra-
ramofuncionamentodaAPIReflection. Oobjetivodessaseçãoéconsolidaresse
conhecimentoatravésdeumexemplomaisrealista.Orequisitoprincipalécriaruma
classequeinvocaparaumdeterminadoobjetorotinasdevalidação.Essasrotinasde
validaçãopodemsermétodosdefinidosnaprópriaclasseouatravésdeatributosque
implementamainterface Validador,querecebeopróprioobjetocomoparâmetro
eestáapresentadanalistagemaseguir.
Aideiaéqueosvalidadoresarmazenadosematributospossamserreutilizados
emdiferentesclassesequeosdefinidosemmétodospossuamvalidações mais
específicasdaprópriaclasse. Oobjetivoéquenavalidação todososvalidadores
presentesnaclassesejaminvocadose,casoexistamerros,umalistacomelesseja
retornada.
Listagem 2.22-Interfaceparaatributoscomvalidadores:
public interface Validador {
public void validar(Object o) throws Exception;
}
V a m o scomeçaroexemplopelométodoqueexecutaosvalidadoresqueestão
presentesnosatributos.Essemétododevepercorrerosatributosdaclasseebuscar
pelosqueimplementamainterface Validador. Amedidaqueessesvalidadores
foremsendoencontrados,elesdevemirsendoexecutadose,casoumaexceção
sejalançada,esseerrodeveserarmazenadoeretornado. Aimplementação desse
métodoestáapresentadanalistagemaseguir. U mfatoraserobservadoéqueo
métodovalidar()nãoéinvocadoutilizandoreflexãoesimpolimorfismoatravés
daprópriainterface. Comootipodoatributoeraconhecido,não foinecessário
utilizarreflexãoparaessainvocação.
Listagem 2.23-Métodoqueexecutaosvalidadoresematributosdaclasse:
private List<Exception> chamarValidadores(Object obj, Class<?> clazz){
List<Exception> erros = new ArrayList<>();
for(Field f : clazz.getFields()){
if(Validador.class.isAssignableFrom(f.getType())){
50

## Página 57

CasadoCódigo Capítulo2. JavaReflectionAPI
try {
Validador v = (Validador) f.get(obj);
v.validar(obj);
} catch
(IllegalArgumentException | IllegalAccessException e) {
throw new RuntimeException(e);
} catch (Exception e) {
erros.add(e);
}
}
}
return erros;
}
Emseguida, foicriadoométodoqueinvocaosmétodosdevalidação pre-
sentes na própria classe. Porconvenção, esses métodosdevem começar com
apalavra“validar”enão possuíremparâmetros,vistoquecomoestão napró-
priaclassepodemacessarseusatributos. Alistagemaseguirmostraométodo
chamarMetodosValidacao(),quepercorreosmétodosdaclassebuscandoos
métodosdevalidação einvocando-os. Observequecasoométodo invoke()
lance uma InvocationTargetException, essa écapturada pela cláusula
catcheaexceçãooriginalérecuperadapelométodo getTargetException()
eadicionadanalistadeerros.
Listagem 2.24-Métodoquechamaosmétodosvalidadoresdaclasse:
private List<Exception> chamarMetodosValidacao
(Object obj, Class<?> clazz){
List<Exception> erros = new ArrayList<>();
for(Method m : clazz.getMethods()){
if(m.getName().startsWith("validar")
&& m.getParameterTypes().length == 0){
try {
m.invoke(obj);
} catch
(IllegalAccessException | IllegalArgumentException e) {
throw new RuntimeException(e);
} catch (InvocationTargetException e) {
51

## Página 58

2.4. Procurandométodoseatributosparavalidação CasadoCódigo
erros.add((Exception)e.getTargetException());
}
}
}
return erros;
}
Parafinalizarprecisamosterumamétodoprincipalqueinvocaosdoismétodos
ereúneoserros.Paraquesejapossívelfazerisso,precisamosdefinirumaexceção
devalidação quereúnaesseserrosepossaserlançadaaqueminvocarométodo.
Dessaforma,alistagemaseguirmostraaclasse ValidacaoException, que
possuiumatributoquerecebeumalistadeexceções emseuconstrutorepermite
suaposteriorrecuperação.
Listagem 2.25-Exceçãoquereúnediversoserrosdevalidação:
public class ValidacaoException extends Exception {
private List<Exception> erros;
public ValidacaoException(List<Exception> erros) {
this.erros = erros;
}
public List<Exception> getErros() {
return erros;
}
}
Finalmente,alistagemaseguirapresentaométodo validarObjeto()que
orquestraainvocação dosoutrosdoismétodosdesenvolvidos. Inicialmente,o
métodoextraiainstânciade Classdoobjetorecebidocomoargumentoecriauma
listaparaarmazenaroserrosretornadospelosmétodos.Emseguidaosmétodos
sãoinvocados,tendooserrosretornadosadicionadosnalista.Nofim,casoalista
possuaalgumerro,écriadaumanova ValidacaoExceptioncomessalistae
lançadaparaométodoqueoinvocou. Sendoassim,casoométodocaptureessa
exceção,eleteráacessoaatodososerroslançadospelosvalidadores.
Listagem 2.26-Métodoprincipalquefazavalidaçãodoobjeto:
public class ValidadorObjetos {
52

## Página 59

CasadoCódigo Capítulo2. JavaReflectionAPI
public void validarObjeto(Object obj) throws ValidacaoException {
Class<?> clazz = obj.getClass();
List<Exception> erros = new ArrayList<>();
erros.addAll(chamarMetodosValidacao(obj, clazz));
erros.addAll(chamarValidadores(obj, clazz));
if(erros.size() > 0){
throw new ValidacaoException(erros);
}
}
}
Diferentementedosexemplosanteriores,ondemostroométododesenvolvido
sendoutilizado,dessavezdeixareiissocomoexercícioparaosleitores.Procurecriar
umaclassequepossuatantométodosdevalidaçãoquantoatributosquetenhaotipo
Validator.T e n t etambémcriarcontraexemplos,ouseja,métodoseatributosque
nãodeveriamserincluídosevejaserealmentesãodeixadosdefora.
2.5 Coisasque podem d a rerrado
“ C o mgrandes poderes vêmgrandes responsabilidades”
–BenParker,tiodoHomem-Aranha
Quandotrabalhamoscomreflexão,existemdiversoserrosquepodemacontecer
quenormalmentesãovalidadosemtempodecompilação.Porexemplo,ummétodo
podeserinvocadocomquantidadeoutiposdeparâmetrosinválidos,pode-setentar
acessarumatributoemumobjetodeumaclassequenãoopossuioumesmopode-
setentaracessarmembrosdeclassequenãoestãoacessíveis.Duranteosexemplos,
podemosverdiversassituações emqueerrosdessetipoerampossíveiseforamtra-
tados.
Aoutilizarreflexão conseguimosumamaiorflexibilidade,porémessepoder
deveserutilizadocomresponsabilidade.Todosesseserrosdevemserverificados,
tratadoseevitadosquandopossível.Porexemplo,seocódigoassumequeométodo
ouconstrutorchamadopossuiparâmetrosdeumdeterminadotipo,procureveri-
ficarseessapremissaéverdadeiraantesdeinvocá-lo.Emoutraspalavras,procure
verificarascondições comantecedênciaetratarascondições excepcionais,aoinvés
desimplesmentechamarosmétodosedeixaroserrosacontecerem.
Quandolidamoscomreflexão,aprópriaestruturadaclasseéumparâmetro,en-
tãodevemosestarpreparadosparalidarcomqualquertipodeclasse.Tiposcomo
53

## Página 60

2.6. Considerações finais CasadoCódigo
arrayseprimitivoscostumamexigirtratamentoespecialemalgunscasos. Dessa
forma,ocódigodeveconsideraretrataressescasos,emesmoquenãosedesejedar
suporteaessescasos,deve-severificarseaestruturadaclasseoumétodoéade-
quadaelançarumerrocasonãoseja.Quandodesenvolviminhasprimeirasclasses
queutilizavamreflexão,melembrodereceberalgunsbugsrelacionadosaestrutu-
rasdeclassequeeunãohaviapensado.Sendoassim,criartestesquecontemplam
diversostiposdeclasseéessencialparaquesetenhaumaboasegurançanocódigo
desenvolvido.
Porfim,procureevitarescondererrosdousuário,deformaquesuaclasse“falhe
gentilmente”semqueeleperceba.Imaginequeumarquivodeconfiguraçãopossua
umalistadeatributosdeumaclassequeprecisamserutilizadosemumalgoritmo
queutilizereflexão,umexemplode“falhargentilmente”seriasimplesmentepular
umatributoquenão existirnaclasse,realizandooprocessamentoparaosoutros.
Pormaisqueissopodeparecerajudarevitandoqueodesenvolvedorenfrenteuma
sériedeexceções antesdetudofuncionarpelaprimeiravez,naverdadeissomascara
umerroquepodeserdifícildeserdetectadodepois. Sendoassim,seencontrar
algumacoisaquenãoestácorreta,lanceoerrocomamaiorquantidadededetalhes
possível,deformaapermitirqueodesenvolvedorqueutilizarasuaclasseidentifique
oqueestáerradoerealizeacorreçãoomaiscedopossível.
Ocapítulo5apresentaformasderealizarostestesdeclassesqueutilizamreflexão.
Paraaquelesquepretendemutilizarreflexãoemprojetosreais,astécnicasapresen-
tadasnessecapítulosãoessenciaisparaajudarnavalidaçãoeverificaçãodessetipo
decódigo.
2.6 Considerações finais
EssecapítuloapresentouoprincipaldaAPIReflectiondalinguagemJava.A p e s a rde
umanoçãoinicialjátersidodadanaintrodução,essecapítulofoimaisfundonos
detalheseapresentouosprincipaisdetalhesdessaAPI.Ocapítulocomeçouapresen-
tandoasformasemqueumareferênciadeumaclassepodeserobtida,sendoessas
atravésdeumreferênciaestática,umobjetoeuma Stringcomseunome.Através
dainstânciade Classfoimostradocomoobterinformações arespeitodaclassee
comocriarinstânciasdela.Apartirdasinstânciasfoimostradocomoareflexãopode
serutilizadaparaoacessoaosseusatributoseparaainvocaçãodeseusmétodos.
Emtodocapítulo,acadanovoconceitoapresentado,víamosumexemploque
demonstrassedeformasimplescomoelefuncionava.Amedidaqueocapítulofoi
54

## Página 61

CasadoCódigo Capítulo2. JavaReflectionAPI
seguindo,osnovosexemplosprocuravamincluirquestões relacionadasafuncio-
nalidadesdaAPIapresentadaspreviamente,mostrandocomoelasseencaixavame
podiamserutilizadasemconjunto.Nofinaldocapítulo,umexemplomaispróximo
dorealfoidesenvolvidoutilizandooquehaviasidoapresentadopreviamente.
Parafecharocapítulo,foiressaltadaaimportânciaemsetomarcuidadocomas
situações excepcionaisquepodemaconteceraoseutilizarreflexão.Comodiversos
errosquenormalmentesão pegosemtempodecompilaçãopodemocorrer,éim-
portantetomarcuidadoparaquetodasassituações sejamtratadasadequadamente.
55

## Página 63

Capítulo3
MetadadoseAnotações
“ A oprocurar u m acitação sobre metadados, só encontrei metadados sobre citações”
–metalinguagemsobreaescritadolivro
Oprefixo metaéfrequentementeutilizadojuntocomumapalavraparasigni-
ficarqueelaestásereferindoasiprópria.Melembrodasaulasdeliteratura,onde
aprofessorafrequentementefalavaemmetalinguagem.Seeumedirijoavocê,lei-
tor,emerefiroaomomentoemqueescrevoesseparágrafo,estouescrevendoum
textoqueestásereferindoaoprópriotexto,sendoassimeupossodizerqueissoé
metalinguagem.
Dessaforma,podemosdizerque metadadossãodadosquesereferemaospró-
priosdados.Apalavrametadadosémuitoutilizadaemcomputaçãodentrodedife-
rentescontextoseporissoprecisamosserumpoucomaisespecíficosemrelaçãoa
quetipodemetadadosestamosnosreferindo.Seestamosfalandodebancodedados,
osdadossãoaquelesqueestãoarmazenadosnobancoeosmetadadossãoadescri-
çãodessesdados,emoutraspalavras,aestruturadastabelas.Paraumdocumento

## Página 64

3.1.Definiçãodemetadados CasadoCódigo
XML,osmetadadossãorepresentadospelodocumentoquedescreveaestruturado
documentoXML,comooDTDouXMLSchema.
Quandoocontextoéumaaplicaçãoorientadaaobjetos,podemosdizerqueos
dadossãorepresentadospelasinstânciaseosmetadadossãoosdadosquedescrevem
essasinstâncias,emoutraspalavras,asinformações arespeitodasclasses.Sendoas-
sim,osatributos,métodos,interfacesesuperclassesão metadadosrelacionadosa
classe.Dessaforma,trabalharcomreflexãoénaverdadetrabalharcomosmetada-
dosdoprograma,utilizando-osparacriaralgoritmosquetrabalhamcomumaclasse
quenãoconhecempreviamente.
Aquestãoéquesomenteosmetadadosdaprópriaclassemuitasvezesnãosão
suficientesparaumcomponentequeutilizareflexão. Podemsernecessáriasmais
informações parasaberaoqueumatributoestásereferindo,quandoummétodo
precisaserinvocadoecomoumadeterminadaclassedeveserutilizadapelocompo-
nente.
Essecapítulonãoiráfalarsobreosmetadadosdaprópriaclasse,queforamvistos
nocapítuloanterior,masdecomodefinirmetadadosadicionaisparaseremutiliza-
dosparadiferenciarunselementosdeumprogramadosoutros.Essesmetadados
sãochamadosdemetadadosespecíficosdedomínio,poiselespossuemumasemân-
ticaespecíficaparaseremlidosetratadosporumcomponentecomumobjetivo
específico.
Essecapítulofalasobreessetipodemetadados,asformasqueelespodemser
definidoseasvantagensedesvantagensdecadaabordagem.Adicionalmente,será
dadoumaênfasenasanotações, queéummecanismodalinguagemJavaparaade-
finição demetadadosdiretamentenocódigo. Serámostradocomodefinirnovas
anotações, inseri-lasnoselementosdecódigoeconsumi-lasemtempodeexecução
atravésdaAPIReflection.
3.1 Definição de metadados
“ S ea l g u m acoisa i r ávariar de forma previsível, guarde a descrição dessa variação em
u mbanco de dados de forma q u eseja f á c i lde mudar. ”
–RalphJohnson
Nocontextodaorientação aobjetos,osmetadadossão informações sobreos
elementosdocódigo. Essasinformações podemserdefinidasemqualquermeio,
bastandoqueosoftwareoucomponenteasrecupereeasutilizeparaagregarnovas
informações noselementosdocódigo.Essaseçãoiráabordardiferentesformasde
58

## Página 65

CasadoCódigo Capítulo3.MetadadoseAnotações
definição demetadados,falandosobreasvantagensedesvantagensdecadauma
delas.
C o n v e nçõ e sde código
Aprimeiraformadedefiniçãodemetadadosqueacabamosutilizandosemper-
cebermuitoquandocomeçamosautilizarreflexãosãoasconvençõesdecódigo.Essa
estratégiautilizaasprópriasconstruções dalinguagemparacriarumasemântica
particularaserutilizadapelocomponente.Emoutraspalavras,apresençadedeter-
minadoselementos,comoumpadrãodenome,umtipoderetornoouaimplemen-
taçãodeumainterface,passamaterumsignificadoespecialparaocomponente.A
partirdessasinformações épossívelfazeradistinçãodesseselementos,tratando-os
deformadiferentedosoutros.
Osprópriosexemplosquevimosnoscapítulosanteriores,acabamutilizando
convenções decódigodealgumaforma. Ocomponentequeexecutaasrotinasde
validação,consideraoprefixo verificarcomoformadeidentificarosmétodos
devalidação eaimplementação dainterface Validadorparaidentificação dos
atributoscomobjetosqueprecisamserexecutados. U moutropadrão decódigo
amplamenteutilizadopeloscomponenteséoJavaBeans[4],quedefinequemétodos
derecuperação deinformações devemcomeçarcom getemétodosparainserir
valoresempropriedadesdevemsercomeçadoscom set,conformeilustradona
próximalistagem.Essaconvençãofoiutilizadanoexemplodageraçãodomapade
propriedadeseéutilizadaemdiversosoutroscomponenteseframeworks.
Listagem 3.1-ExemplodeconvençãodecódigodeumJavaBean:
public class JavaBean {
private String propriedade;
public String getPropriedade(){
return propriedade;
}
public void setPropriedade(String s){
this.propriedade = s;
}
}
U moutroexemplodeconvençãodecódigomuitoutilizadafoioprefixo test
noJUnit3. Nessaversão enasanteriores,ummétodocomesseprefixo,como
ilustradonapróximalistagemeraconsideradoummétododetesteeinvocadopelo
59

## Página 66

3.1.Definiçãodemetadados CasadoCódigo
framework. Emversões posteriores,ousodesseprefixofoisubstituídoporuma
anotação.
Listagem 3.2-DefiniçãodeumtestenoJUnit3:
public class TesteSomador extends TestCase {
//identificado como teste pelo prefixo "test"
public void testSoma(){
Somador s = new Somador();
int resultado = s.somar(2,2,4);
assertEquals(8,resultado);
}
}
Porémnãoexistemsomenteconvenções queutilizamprefixosesufixosnosno-
mes.U mexemplocomuméutilizaropróprionomedoelementodecódigoparaque
elecorrespondaaonomeutilizadoemalgumaoutraentidadequeeleestámapeando.
Noexemplodogeradordemapadepropriedades,onomedométodofoiutilizado
parageraronomedapropriedade.Deformaanáloga,épossívelmapearonomede
umaclasseparaonomedeumatabelanobancodedadosqueelarepresentaoupara
umaURLdeumaaplicaçãowebqueelaprecisatratar.
Asinterfacesdemarcaçãoforamumapráticacomumparadefinirummetadado
antesde Javater suportenativoa anotações. A interfacede marcação éuma
interfacesemmétodos,aqualasclassesimplementamparateremumsignificado
especialparaalgumcomponente.U mexemplodissoéainterface Serializable,
quemarcaasclassesquesão serializáveis.Essainterfacenão possuimétodoseé
adicionadaaclasseapenascomointuitodemarcá-lacomotendoumadeterminada
propriedade. Apróximalistagemmostraumaclasseválidaqueimplementaessa
interface,nãoprecisandoimplementarnenhummétodo.Emoutraspalavras,essa
interfaceservemaisparaadicionarummetadadodoquepararealmenterepresentar
umaabstração.
Listagem 3.3-CódigoválidoqueimplementaainterfaceSerializable:
public class Serializavel implements Serializable {
public int numero;
public String texto;
//sem métodos omitidos
}
60

## Página 67

CasadoCódigo Capítulo3.MetadadoseAnotações
U m adascaracterísticasdousodasconvenções decódigoéutilizarmecanismos
dapróprialinguagemparaadefiniçãodosmetadados.Oladopositivodissoéqueos
desenvolvedoresnãoprecisamfazernadaadicionarparaqueocomponenteentenda
osmetadadosdaquelaclasse,bastandoseguirasconvenções nadefiniçãodosnomes
eelementosdocódigo.Oladoruimdessacaracterísticaéqueosmetadadosficam,
decertaforma,implícitoseprecisamsercompartilhadosportodaequipeparaseu
usoserefetivo.Porexemplo,podenãoserclaroparaumdesenvolvedorqueamu-
dançadenomedeummétodopodecausarumamudançadecomportamentoem
umcomponentequeinvocaaquelaclasse.
Devidoafacilidadedeutilizaçãodeconvençõesdecódigo,essapráticaébastante
utilizadaporframeworkseAPIs,porémessaéraramenteumatécnicaqueéutilizada
sozinha. U mdosmotivoséqueaexpressividadedessatécnicaébastantelimitada
eapenasmetadadossimplesconseguemserrepresentadosdessaforma.Sendoas-
sim,oquecostumaserutilizadosãoalgumasconvenções decódigoquesãocomple-
mentadascomalgumadasoutrasformasdedefiniçãodemetadados.Noexemplo
dageraçãodomapadepropriedades,umaconvençãodecódigoconsideravaqueo
nomedachavedomapaseriaigualaonomeutilizadonométodogetter,porémuma
anotaçãopermitiaqueumnomediferentefosseutilizado.
Definição programática
U m aoutraformadedefiniçãodemetadadoséatravésdeumarotinaqueinsere
asinformações relativasaosmetadadosdiretamenteaocomponente.Seriaalgoque
comoachamadadeumamétodoqueinserisseainformaçãodequeumaclassepos-
suiumadeterminadainformação,ouquealgumdeseusmétodospossuemumdado
associado.Essaabordagemtiraaresponsabilidadedoprogramadelerosmetadados,
poiséoprogramaquedeveinseri-los.Emumprogramaqueutilizaressecompo-
nente,arotinadeinserçãodessesmetadadosdeveocorrerantesqueessecomponente
utilizeumaclasse,emalgumcódigoquenormalmenteécolocadonainicialização
daaplicação.
NãoexistemmuitosexemplosdeframeworkseAPIsqueutilizamessaaborda-
gem.Dopontodevistadequemutilizaocomponente,pessoalmentenãoachomuito
intuitivoutilizarumcódigoimperativoparaconfigurarinformações quesãoestáti-
cas.U mframeworkbrasileiroqueutilizaessetipodetécnicaéoMentawai.
Nalistagemaseguirestáumexemploobtidodotutorialdesseframeworkque
fazomapeamentodeumaclasseparaabasededados. Nesseexemplo,aclasse
Usuarioémapeadoparaatabela Usuarioseseusatributossãomapeadospara
61

## Página 68

3.1.Definiçãodemetadados CasadoCódigo
astabelas. Cadachamadadométodo field()passacomoparâmetroonome
doatributo,opcionalmenteonomedacolunacasosejadiferentedoatributoeo
tipodocamponobancodedados.A p e s a rdeseremchamadasdemétodo,épossí-
velperceberqueelesestãodefinindoinformaçõesarespeitodoselementosdaclasse.
Listagem 3.4 - Exemplo de configuração programáticade metadados de per-
sistêncianoframeworkMentawai:
@Override
public void loadBeans() {
bean(Usuario.class, "Usuarios")
.pk("id", DBTypes.AUTOINCREMENT)
.field("login", DBTypes.STRING)
.field("senha", DBTypes.STRING)
.field("dataNascimento", "nascimento", DBTypes.DATE);
}
A p e s a rdessadefiniçãoprogramáticademetadadosnãoserdiretamenteutilizada
pelosdesenvolvedores,elaacabaexistindointernamenteemdiversoscomponentes
eframeworks. Issoaconteceporquesehouverafuncionalidadedelerosmetada-
dosdefinidosdealgumaoutraforma,aclassequefazissoprecisarádessainterface
programáticaparapoderinseri-los.
F o n t e sexternas
Outraformadedefinirosmetadadoséutilizandofontesexternasdedados.
Dessaforma,ocomponenteouframeworkdeveacessaressafonteexternadeda-
doserealizaraleituradessasinformações. Dealgumaforma,elasdevemreferenciar
oselementosdecódigo,comoclasses,métodoseatributos,paraquequemrealizar
essaleiturapossareferenciarametainformação àquemelapertence. Essaleitura
tambémdeveserfeitaantesqueocomponentesejautilizado,poisnessemomento
essasinformações jádevemestarpresentes.
U m adasformasmaiscomunsdesedefinirmetadadosemumafonteexternaé
atravésdearquivosdeconfiguração,sendoquearquivosXMLacabamsendoosmais
utilizados.Essesarquivoscostumampossuirumformatobemdefinidoparapode-
remserlidospelospeloscomponentes.A p e s a rdeXMLserconsideradoumformato
dearquivo“amigávelparapessoas”,muitasvezesaconfiguraçãodasinformações é
complicadaetediosa.Ofatodasinformações precisaremreferenciaroselementos
docódigofazcomqueoarquivoacabeficandoverboso,sendoquecomosãoraros
62

## Página 69

CasadoCódigo Capítulo3.MetadadoseAnotações
oscasosemqueexistealgumsuportedeferramentaparatrabalharcomessearquivo,
émuitofácilcometerumerroemumnomedeclasseoumétodo.
Outraalternativaparaarmazenarosmetadadossãoosbancosdedados.Seeles
podemarmazenardadosdaaplicação,porquenãoarmazenardadossobreaaplica-
ção. A p e s a rdessanãoserumaalternativamuitoutilizadaporframeworksdemer-
cadodevidoadificuldadedeconfiguraçãoinicial,emcomponentescaseiros,ouseja,
desenvolvidosdentrodaaplicação,essaacabasendoumaalternativabastanteutili-
zada.Principalmenteparametainformações quepodemseralteradasemtempode
execução,comopermissões desegurançademétodosdenegócio,terumcontrole
transacionalecentralizadodessesdadospodeserumaboaideia.
Paraexemplificaraconfiguraçãodosmetadadosemfontesexternasaocódigo,
apróximalistagemtrásosmetadadosdeummapeamentoobjeto-relacionalfeito
peloframeworkHibernate.Observequeoelemento <class>referenciaaclasse
com.casadocodigo.Usuario e, em seguida, os elementos <property>
referenciamosatributos,associando-osarespectivacolunanabasededados. Os
metadadosrepresentadosaquiemXMLpossuemomesmoobjetivodosdefinidos
deformaprogramáticanalistagemanterior.
Listagem 3.5- Exemplo de definição de metadados de persistênciaem arqui-
vosXML:
<hibernate-mapping>
<class name="com.casadocodigo.Usuario" table="USUARIO">
<id column="USER_ID" name="id" type="java.lang.Long">
<generator class="org.hibernate.id.TableHiLoGenerator">
<param name="table">idgen</param>
<param name="column">NEXT</param>
</generator>
</id>
<property column="LOGIN" name="login" type="java.lang.String"/>
<property column="SENHA" name="senha" type="java.lang.String"/>
<property column="NASCIMENTO" name="dataNascimento"
type="java.util.Date"/>
</class>
</hibernate-mapping>
U m adasdesvantagensdadefiniçãodemetadadosemfontesexternaséqueosda-
dosprecisamreferenciaroselementosdocódigotornandoessaconfiguraçãotediosa
esujeitaaerros,principalmentesenãohouverumaferramentadeapoio.Utilizando
63

## Página 70

3.1.Definiçãodemetadados CasadoCódigo
essaabordagemacabahavendoumadistânciaentreoselementosdocódigoeosme-
tadados.Issocausadificuldadesnasuaconfiguraçãoe,principalmente,quandofor
necessáriaalgumamanutenção. U m aalteração inofensivanoselementosdeuma
classepodequebrarumareferêncianosarquivosdeconfiguração egerarumbug
indesejadonaaplicação.
Osmetadados,deumacertaforma,acabamsendoresponsáveisporpartedo
comportamentodaaplicação.Dessaforma,elesdevemserversionadosjuntocoma
aplicaçãoparapoderemgerarocomportamentodesejado.ParadocumentosXML
issonãoéumgrandeproblema,masparabancosdedadospodeseralgobastante
complicado.Principalmentequandoosusuáriosdealgumaformapodemmodificar
osmetadadoseéprecisofazerumajunçãoouadaptaçãodosmetadadosdevidoa
novasclassesoumodificações emclassesexistentes.
Poroutrolado,adefinição demetadadosemfontesexternaséumaboaalter-
nativaquandoéprecisodarsuporteaconfiguração demetadadosparaclassesde
terceirosequenãosetemacessodemodificaçãodocódigofonte.Nessecaso,essa
desvinculaçãoentreosmetadadoseasclasseséumavantagem.Adicionalmente,essa
abordagemtambéméadequadaparapermitirqueosmetadadospossamseraltera-
dossemanecessidadederecompilaçãodaaplicação. Issoéidealparaquandosão
necessáriosajustesnosmetadadosemtempodedeployouemtempodeexecução.
Anotaçõ e s
Asanotações sãoumrecursodalinguagemJavaintroduzidasnaJDK5paraper-
mitiraadiçãodemetadadosdiretamentenocódigo.Essapráticatambéméconhe-
cidatambémcomoprogramaçãoorientadaaatributos.Apartirdesserecursoépos-
sívelmanterocódigoeosmetadadosnomesmolocal,simplificandosuaadminis-
tração.Essaabordagemacabatambémdiminuindoaverbosidadedesuadefinição,
vistoquecomoosmetadadossãoadicionadosnospróprioselementosdecódigo,não
énecessárioreferenciá-los.Esserecursodelinguagemtambémestápresenteemou-
traslinguagenscomonoC#,ondeéchamadode attributes. AlinguagemPhyton
possuiummecanismoumpoucodiferentechamadode decorator,masquetambém
éutilizadoparaaadiçãodemetadadosdiretamentenocódigo.
NalinguagemJava,aprogramaçãoorientadaaatributoscomeçouantesdasano-
tações, comaferramentaXDoclet. NoJavaEE1.4,quenaépocaaindarecebiao
nomedeJ2EE,acriaçãodeEJBsdemandavaacriaçãodediversosdescritoresXML
einterfaces.Euchegueiadesenvolverparaessaplataformaepossoafirmarquereal-
menteeramuitocomplicadodesenvolversemumaboaferramentadeapoio.Nessa
64

## Página 71

CasadoCódigo Capítulo3.MetadadoseAnotações
época,umaalternativaquesurgiuparaodesenvolvimentodeEJBsfoiautilização
daferramentaXDoclet.
OXDocletéumaenginedegeração decódigo queprocessaocódigo fonte
permitindoaadição demetadadosemtagsJavaDoc,quesão adicionadasdentro
decomentários.Comoresultadodesseprocessamentoépossívelgerardescritores
XMLeocódigofontedeoutrasclasses. Existiaumgrandeconjuntodetags,por
exemplo,queeramdestinadasaodesenvolvimentoparaaplataformaJ2EE.No
casodeumEJBdesessão, porexemplo,eramgeradasasinterfacesauxiliareseos
descritoresXMLemqueaquelaclassedeveriaestarpresente. Alistagemaseguir
mostraoexemplodeumaclasseanotadacomastagsJavaDocdoXDoclet.
Listagem 3.6-UtilizaçãodoXDocletparageraçãodeEJBs:
/**
* @ejb.bean
* name="CustomerService"
* jndi-name="CustomerServiceBean"
* type="Stateless"
**/
public abstract class CustomerServiceBean implements SessionBean {
/**
* @ejb.interface-method tview-type="both"
*/
public void createCustomer(CustomerVO customer) {
}
/**
* @ejb.interface-method tview-type="both"
*/
public void updateCustomer(CustomerVO customer) {
}
}
Nãoseiexatamentequalfoiamotivaçãoparaaintroduçãodasanotações noJava
5,masexistiamdiversasforçasqueacabaramempurrandoalinguagemnessadire-
ção.Porumladohaviaumagrandecriticadevidoagrandequantidadededescritores
doJavaEEeaprogramaçãoorientadaaatributoscomoXDocletsemostravacomo
umaalternativaviável.Poroutrolado,alinguagemC#jápossuíaomecanismode
65

## Página 72

3.1.Definiçãodemetadados CasadoCódigo
atributoseestevinhasendoutilizadocomsucessoparaodesenvolvimentodeapli-
cações corporativas.
Asanotações foramanunciadasnalinguagemJavacomoorecursoqueiriasim-
plificarodesenvolvimentodeaplicações corporativas. Hojeépossívelverquere-
almenteelasconseguiramcumpriressapromessa,eliminandoaobrigatoriedadede
diversosdescritoresXMLquetornavamodesenvolvimentodessetipodeaplicação
bastanteburocrático.Atualmente,grandepartedosframeworkseAPIsparaalin-
guagemJavafazemousodeanotações. Esserecursodelinguagemacaboupopulari-
zandoautilizaçãodeframeworksbaseadosemmetadados,poisfacilitouadefinição
dosmetadadosparaosseususuários,tornandoousodessaabordagemmaisviável.
Para exemplificar a utilização de anotações para definição de metadados,
considerealistagemaseguirquemostracomoomapeamentoparaumbanco
dedadoséfeitocomasanotações daAPIJPA.Observe,porexemplo,quenada
precisouserfeitoparaosatributos logine senha,quenosexemplosanteriores
precisaramserreferenciadosexplicitamentenadefiniçãodemetadados.Aanotação
@Table,porexemplo,sóprecisaseradicionadacasoonomedatabelasejadiferente
donomedaclasse. Omesmoseaplicaaanotação @Column,quetambémsóé
necessáriaquandoacolunatemonomediferentedoatributo.
Listagem 3.7-Mapeamentoobjeto-relacionalcomJPAutilizandoanotações:
@Entity
@Table(name="Usuarios")
public class Usuario {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private int id;
private String login;
private String senha;
@Column(name="nascimento")
private Date dataNascimento;
//métodos get e set omitidos
}
A p e s a rdeseremmaisfáceisdeseremconfiguradasporficarempróximasaos
66

## Página 73

CasadoCódigo Capítulo3.MetadadoseAnotações
elementosdecódigo,essaprópriacaracterísticatambémpodeserumadesvanta-
gemdasanotações. Quandoelassão utilizadas,paraaalteração dosmetadadosé
necessáriorecompilarasclasses,oquepodenãoserviávelparaajustesemtempo
deimplantaçãooualteraçãoemtempodeexecução. Issotambémpodedificultara
reutilizaçãodaclasseemumcontextoemqueasanotações nãosejamnecessáriasou
queoutrosmetadadosprecisemserconfigurados.
Ousodeanotaçõesnasclassestalvezsejafamiliaragrandepartedosdesenvolve-
dores,porémacriaçãodenovasanotações eodesenvolvimentodecomponentesque
recuperamefazemprocessamentosbaseadosnelas,talveznãosejamtãopopulares.
Orestodessecapítulosededicaamostrarcomoasanotações podemsercriadase
comoutilizaraAPIReflectionpararecuperá-las.
Misturando mecanismos de definição de metadados
Comopodeservisto,cadaformadedefiniçãodemetadadospossui
suasvantagensedesvantagens,emuitasvezesficadifícilequilibrarosre-
quisitosapartirdeumadasformas.Porexemplo,enquantoasanotações
oferecemumaformamenosverbosadedefinirosmetadados,asfontes
dedadosexternaspermitemaalteração dosmetadadossemarecom-
pilaçãodasclasses.Felizmente,oscomponentesnãoprecisamescolher
apenasumaformadedefinição demetadados,sendopossívelcombi-
narmetadadosdediferentesfontes.Ocapítulo ??falacomoestruturar
ocomponenteparapermitiracombinaçãodemetadadosdediferentes
fontes.
3.2 Criando anotações
Asanotações emJavasão definidasemarquivosseparadoscomextensão .java
que precisam ter seu mesmo nome, assim como as classes, as interfaces e as
enumerações. Paradefinirumanovaanotação, éprecisoutilizarapalavrachave
@interface.Alistagemaseguirmostraumexemplosimplesdecomosedefinir
umaanotação.
Listagem 3.8-DefiniçãodeumasimplesanotaçãochamadaMetadado:
public @interface Metadado {
}
67

## Página 74

3.2.Criandoanotações CasadoCódigo
U m aanotaçãopodepossuiratributos,ouseja,vocêpodeagregarinformações
aosmetadados,porémnão équalquerclassequeéaceitacomotipodoatributo.
Porémumaanotaçãonãopodepossuircomportamento,sendoumainformaçãoes-
táticaqueéadicionadaaclasses.Existemtambémanotações quepodemseradici-
onadasasprópriasanotações paraparametrizarcomoelasdevemsertratadaspelo
compiladorepelamáquinavirtual.Aspróximassubseções irãoapresentardetalhes
arespeitodecomosãocriadasasanotações.
U m acoisaimportantedasanotaçõesé:elas não fazem nada!!!Paraquemutiliza
umframeworkqueutilizaanotações, podeparecerqueaconfiguraçãodeanotações
adicionacomportamentosnaclasse,porémaverdadeéqueelassomenteestãoagre-
gandonovasinformações sobreoselementosdaclasse.Paraqueelastenhamalgum
efeitosobreofuncionamentodoprograma,alguémprecisarecuperaressasanota-
ções efazeralgumacoisaarespeito,poissozinhasasanotações nãofazemnada.
Definindo a t éq u a n d oa anotação estádisponível
U m adasprincipaisconfigurações deumaanotação éatéquandoelavaiestar
disponívelpararecuperação.Dependendodousoqueseráfeitodelaedomomento
emqueessainformaçãoseráconsumida,diferentestiposderetençãopodemserne-
cessárias.Segueumalistacomostrêsdiferentestiposderetençãoqueumaanotação
podepossuir:
•SOURCE:U m aanotaçãocomessetipoderetençãoficadisponívelapenasno
códigofonte. Nomomentoemqueaclasseécompilada,aanotação não é
transferidaparaoarquivo .class. Essetipodeanotação énormalmente
utilizadaparafinsdedocumentaçãoeparausodeferramentasquefazempro-
cessamentodiretodecódigofonte.U mexemplosãoferramentasquefazem
validações emtempodecompilação.
•CLASS: Anotações comesse tipo de retenção são mantidasnos arquivos
.class,porémnão são carregadaspelamáquinavirtual. Nessecaso,elas
ficamdisponíveisatéomomentodocarregamentodaclasse. Essetipode
anotaçãoéutilizadaporferramentasquefazemprocessamentodobytecode
daclasse,podendoesseprocessamentoserfeitodeformaestáticacomouma
etapaposterioracompilação,ounomomentodocarregamentodasclasses.
Essetipodepráticaserávistonocapítulo ??.
68

## Página 75

CasadoCódigo Capítulo3.MetadadoseAnotações
•RUNTIME:Paraumaanotaçãoestardisponívelparaarecuperaçãoemtempo
deexecução,elaprecisateressetipoderetenção. Nessecaso,amáquinavir-
tualvaicarregaressaanotaçãoemmemóriaetorná-laacessívelatravésdaAPI
Reflection.Essetipodeanotaçãoéotipoutilizadoporframeworksquepre-
cisamteracessoasanotações emtempodeexecução. Seráotipoqueiremos
utilizarcommaiorfrequênciaaquinesselivro.
Paraconfigurarotipoderetenção deumaanotação éprecisoanotá-lacoma
anotação @Retention. Essaanotação recebecomoparâmetroumaenumeração
dotipo RetentionPolicy,quepodepossuirosvalores SOURCE, CLASSou
RUNTIME descritos acima. A listagem a seguir exemplificacomorealizar essa
configuração. Nessecapítuloiremosabordarsomenteasanotações comretenção
dotipo RUNTIME,ficandoasanotações dotipo CLASSparaocapítulo ??. O
processamentodeanotações diretamentenocódigofontecomopartedoprocesso
decompilação,queutilizariaanotações dotipo SOURCE,estãoforadoescopodesse
livro.
Listagem 3.9-Configurandootipoderetençãodeumaanotação:
@Retention(RetentionPolicy.RUNTIME)
public @interface Metadado {
}
Casoumaanotaçãonãopossuaumaretençãoconfigurada,pordefiniçãoelaserá
dotipo SOURCE.Sendoassim,sevocêestiverdesenvolvendoumcódigoquecon-
someumaanotação eporalgummotivoessaanotação não estiversendoencon-
trada,muitoprovavelmenteéporquevocêesqueceudeconfigurararetençãopara
RUNTIME.Eujácrieidiversosframeworksqueconsomemanotações, emesmoassim
detemposemtempoissoacabaacontecendocomigo.
T i p ode elementos anotados
Outraconfiguração importanteparaumaanotação são ostiposdeelementos
quepodemseranotadosporela.Senadafordito,aanotaçãopoderáseradicionada
emqualquertipodeelemento.Pormaisqueessaconfiguraçãonãosejaobrigatória,
ésempreumaboapráticaadicioná-laparaevitarqueosseususuáriosadicionem-na
nolocalerrado.Porexemplo,umaanotaçãoquedeveseradicionadanosmétodos
deacessopodeseradicionadaporenganoemumatributo,oquevaifazerquenão
sejaencontradapelaclassequeaprocurar.
69

## Página 76

3.2.Criandoanotações CasadoCódigo
Segueabaixoumalistacomostiposdeelementoquepodemseranotados,sendo
cadaumdelesumelementodaenumeração ElementType:
•TYPE:qualquerdefiniçãodetipo,comoclasses,interfaceseenumerações.
•PACKAGE:pacotes.
•CONSTRUCTOR:construtores.
•FIELD:atributos.
•METHOD:métodos.
•PARAMETER:parâmetrosdemétodoseconstrutores.
•LOCAL_VARIABLE:variáveislocais.
•ANNOTATION_TYPE:anotações.
Paraconfigurarotipodeelementoqueumaanotação podeanotar,épreciso
configurá-lacomaanotação @Target.Essaanotaçãopodereceberumarraycom
diversostiposondeelafazsentidoseradicionada. Alistagemaseguirmostraum
exemplodeconfiguração,ondeaanotaçãopodeseradicionadaemummétodoou
emumatributo.
Listagem 3.10-Configurandootipodeelementoquepodeseranotado:
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.METHOD, ElementType.FIELD})
public @interface Metadado {
}
Em relação ao tipo LOCAL_VARIABLE, como as variáveislocais não são
acessíveisporreflexão,essetipodeanotação sófazsentidocomretenção dotipo
SOURCEou CLASS.Outrotipodeanotaçãocurioso,éaanotaçãodotipo PACKAGE
queéutilizadaparaadicionarmetainformações emumapacote.Paraadicioná-la,é
precisocriarumarquivonopacotechamado package-info.javaparadefinira
anotação.Alistagemaseguirmostracomoseriaoconteúdodessearquivo.
Listagem 3.11- Conteúdodo arquivo package-info.java para adicionar anota-
çãoaopacote:
70

## Página 77

CasadoCódigo Capítulo3.MetadadoseAnotações
@Metadado
package org.casadocodigo;
import org.anotacoes.Metadado;
Outras definiçõ e s
Alémdasanotações @Targete @Retentionexistemoutrasquepodemser
adicionadasnasanotações paraconfigurarcomoasferramentasdaJDKdevem
encará-las.U m adelaséaanotação @Documentedquedeveserutilizadaquando
aanotaçãoprecisarserincorporadaadocumentaçãodoselementosanotados.Por
exemplo,umaanotaçãoquedeterminaosvaloresválidosparaumatributo,certa-
menteéinteressantedeseradicionadanadocumentação. Outrasanotações muito
específicas,queporexemplomarcaummétodoparatersuasinvocações incluídas
nolog,talveznãopreciseentrarnadocumentação.
Outraanotação quepodeseradicionadanaanotação é @Inherited. Nesse
caso,aanotaçãoserápropagadaparaassubclassesdaclassequeapossuir.U m anota
importanteéqueissosóiráfuncionarcomanotações com @Targetdotipo TYPE.
Aocontráriodoqueseesperaria,ummétodosobrescritoporumasubclassenãoirá
herdarasanotações dotipo @Inheriteddométodoqueestásobrescrevendo.
Atributos da anotação
Emalgunscasos,apenasapresençadaanotaçãojáésuficienteparaconfigurar
umapropriedadedoelementoanotado,comoseaclasseépersistenteounão.Porém
emoutroscasos,sãonecessáriasinformações adicionais,como,porexemplo,qualo
nomedatabeladobancodedadosparaaqualessaclasseémapeada.Sendoassim,as
anotações podempossuiratributosparaaconfiguraçãodevaloresquefazemparte
dometadado.Diferentementedeumatributodeclasse,apenasalgunstipospodem
sertiposdeatributosdeumaanotação. Essessãotiposprimitivos,enums, Class,
String,outrasanotações earraysdequalquerumdessestipos.
T o d oatributodeumaanotaçãoprecisapossuirumvalor.Dessaforma,seoatri-
butoestiverpresente,eleprecisadeumvalor. Épossívelconfigurarumvalor de-
f au l tparaoatributoequandoissoéfeito,aquelevalornãoprecisaobrigatoriamente
terumvaloratribuídoquandoaanotaçãoéutilizada. Osatributossão configura-
dosatravésdeparesnomeevaloradicionadosnaanotação noseguinteformato:
@Anotacao(nome=valor).Existeumnomeespecialdeatributo, value,quecaso
sejaoúnicoatributoconfiguradodaanotaçãopodeterseunomeomitidodaseguinte
71

## Página 78

3.2.Criandoanotações CasadoCódigo
forma: @Anotacao(valor).
Paraentendermelhoroqueéválidoeoquenão é,nadamelhordoquever
algunsexemplos. Alistagemaseguir,mostraumaanotação comumatributo
chamado value. Aodefiniraanotação semoatributoem atributo1,issoé
inválidopoisovalorprecisaserdefinidoobrigatoriamente. Comooatributoda
anotaçãosechama value,entãoelepodeserexplicitamentereferenciadoounão,
respectivamentenaforma @Metadado(value=13)ou @Metadado(13),sendo
asduasformasválidas.
Listagem 3.12-Exemplodeanotaçãocomatributovalue:
//definição da anotação
public @interface Metadado {
int value();
}
//Exemplos de uso
public class Exemplo{
@Metadado //inválido pois não definiu atributo
public String atributo1;
@Metadado(value=13) //válido
public String atributo2;
@Metadado(13) //válido
public String atributo3;
}
Oexemploapresentadonapróximalistagemapresentaumaanotação como
atributo tipo,quepossuiadefinição deumvalor defaultigualauma String
vazia. Nessecaso,adefinição daanotação daforma @Metadado,semdefinição
deumvalorparaoatributo,éválidaporcausadeumvalortersidodefinidopor
definiçãonaprópriaanotação.Paraessaanotação,aomissãodonomedoatributoé
inválidaquandoeleéconfigurado,poisonomedoatributonãoé value.
Listagem 3.13-Exemplodeanotaçãocomatributovalueevalordefault:
//definição da anotação
public @interface Metadado {
72

## Página 79

CasadoCódigo Capítulo3.MetadadoseAnotações
String tipo() default "";
}
//Exemplos de uso
public class Exemplo{
@Metadado //válido
public String atributo1;
@Metadado(tipo="OK") //válido
public String atributo2;
@Metadado("OK") //inválido porque o atributo não chama value
public String atributo3;
}
Comoúltimoexemplodedefinição deatributos,apróximalistagemmostra
umaanotação comumatributo valueeumatributochamado tipocomvalor
default. Aanotaçãoem atributo1éinválidapoisoatributo valueprecisater
umvalordefinidoeaanotação em atributo2éválidapoisquandosomenteo
atributo valueédefinido,seunomepodeseromitido.Nosdoisexemplosdeuso
seguintes,podemosverqueoatributo valuesópodeseromitidoquandoéoúnico
atributodefinidonaanotação. Sendoassim,quandooatributo tipoédefinido,o
nomedoatributo valueprecisaserdefinidoexplicitamente.
Listagem 3.14-Exemplodeanotaçãocomatributovalueevalordefault:
//definição da anotação
public @interface Metadado {
Class value();
String tipo() default "";
}
//Exemplos de uso
public class Exemplo{
@Metadado //inválido porque value não tem valor default
public String atributo1;
@Metadado(String.class) //válido
public String atributo2;
73

## Página 80

3.3.Lendoanotações emtempodeexecução CasadoCódigo
@Metadado(value=String.class, tipo="OK") //válido
public String atributo3;
@Metadado(String.class, tipo="OK")
//inválido pois value só pode ser omitido quando é o único atributo
public String atributo4;
}
3.3 Lendo anotações em tempo de execução
Depoisdevernaseção anteriorcomocriaranotações, essaseção mostracomo
recuperá-lasatravésdaAPIReflection.Maisumavezressaltoqueparaissoserpossí-
veléprecisoqueaanotaçãopossuaadefinição @Retentioncomovalor RUNTIME,
poiscasocontrárioamáquinavirtualnãoirácarregaradefiniçãodometadadojunto
comaclasse.
Recuperando anotaçõ e s
Existeumainterfacechamada AnnotatedElementquedefineosmétodospara
arecuperaçãodeanotações. Essainterfaceéimplementadaportodasasclassesque
representamelementosdecódigoquepodemseranotados,comoasclasses Class,
Method, Field, Packagee Constructor. Sendoassim,essesmétodosque
serãoapresentadospodemserinvocadosemqualquerumadessasclasses.
Existemdoismétodosnessainterfacequenospermitetrabalharcomumaanota-
çãoespecífica.Oprimeirodelesé isAnnotationPresent(),quepodeserutili-
zadoparaverificarseumadeterminadaanotaçãoestápresenteounãonoelemento.
Essemétodoretornaumvalorbooleanodizendoseaanotaçãoexistenaqueleele-
mento.OoutrométodoégetAnnotation(),querecebecomoparâmetroaclasse
daanotaçãoeretornaaanotaçãodesejada.Ainstânciaretornadapossuiotipoda
anotação,eseusatributospodemserrecuperadosatravésdosmétodoscomseusno-
mes.
A listagem a seguir mostra um exemplo de código onde uma anotação é
recuperadaeseusatributosimpressosnoconsole. Antesdeimprimiraanotação,
ométodo isAnnotationPresent()éutilizadoparaconfirmarapresençada
anotação. Observequequandoométodo getAnnotation() éinvocado,ele
recebeaclassedaanotaçãocomoparâmetroeutilizaseutipogenéricoparainferir
otipodoretorno,queéoprópriotipodaanotação. Apartirdessainstânciacom
7 4

## Página 81

CasadoCódigo Capítulo3.MetadadoseAnotações
otipodaanotação,épossívelobterosseusatributosinvocandométodoscomseus
nome,conformemostradonoexemplo.
Listagem 3.15-Recuperaçãodaanotação:
//definição da anotação
@Retention(RetentionPolicy.RUNTIME)
public @interface Metadado {
String nome();
int numero();
}
//Uso e recuperação de anotação
@Metadado(nome="classe", numero=17)
public class RecuperaAnotacao {
public static void main(String[] args) {
Class<RecuperaAnotacao> c = RecuperaAnotacao.class;
if(c.isAnnotationPresent(Metadado.class)){
Metadado m = c.getAnnotation(Metadado.class);
System.out.println("Propriedade nome = "+ m.nome());
System.out.println("Propriedade numero ="+ m.numero());
}
}
}
Os outros métodosdefinidos em AnnotatedElement para recuperação
de anotações retornam a lista de anotações de um elemento. O método
getAnnotations()iráretornarumalistacomtodasasanotações deumdeter-
minadoelementodecódigoeométodo getDeclaredAnnotations()iráretor-
narsomenteasanotações declaradasnoelemento,excluindoascom @Inherited
queforamherdadasdasuperclasse.Comoaherançadeanotações funcionasomente
paraclasses,paraoutrostiposdeelementooretornodosdoismétodosserásempre
omesmo.
Anotaçõ e sem parâmetros
Asanotações emparâmetrossãorecuperadasdeformadiferente,poisnãoexiste
umaclassenaAPIReflectionquerepresentaumparâmetro.Ométodoparaarecu-
peraçãodeanotações emparâmetrossechama getParameterAnnotations()e
75

## Página 82

3.3.Lendoanotações emtempodeexecução CasadoCódigo
estápresentenasclasses Methode Constructor.Essachamadaretornaumarray
deduasdimensões de Annotation,sendoqueaprimeiradimensãorepresentam
osparâmetroseasegundadimensãorepresentaasanotações daqueleparâmetro.
Asanotações emparâmetrossão muitoúteisparaidentificarqualinformação
precisaserpassadaparaele.Dessaforma,quandoummétodoforserinvocadouti-
lizandoreflexão,essainformaçãopodeserutilizadaparadescobrirqueinformação
seesperareceber.Nosexemplosqueforamvistosatéagora,eramutilizadasconven-
ções paradeterminarquaisseriamosparâmetrosdosmétodosinvocados,porém
utilizandoessasinformações épossívellidarcomdiversascombinações deparâme-
tros,reconhecendo-osemtempodeexecução.
Paraexemplificaresseprocedimento,apróximalistagemapresentaadefinição
deumaanotação deparâmetros.Essaanotação sechama @Parameoobjetivoé
queumnomeparaoparâmetrosejadefinidoemseuatributo value.
Listagem 3.16-Anotaçãoparanomearosparâmetros:
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.PARAMETER)
public @interface Param {
String value();
}
A próxima listagem estáum métodochamado invocarMetodo() que
recebeum Method,umobjetoeummapadeinformações comoparâmetro,e
executaométodorecuperandoosseusargumentosdomapadeacordocomo
nomeconfiguradonaanotação. Observequeessemétodoinicialmenterecupera
as anotações dos parâmetrospelo método getParameterAnnotations() e
emseguidacriaumarraychamado paramValuesparaarmazenarosvaloresa
serempassadosnachamadadométodo.Paracadaparâmetro,ométodoauxiliar
getNomeParâmetro() recebealistadeanotações daqueleparâmetroebusca
entreelasaanotação @Param,retornandooseuvalor.Emseguida,érecuperadodo
mapaoobjetocomachavetendoomesmonomeconfiguradonaanotação. A p ó s
recuperartodososparâmetros,ométodoéinvocadopassandooarrayresultante.
Listagem 3.17-Invocaçãodemétodorecuperandoosparâmetrosdeummapa:
public static Object invocarMetodo(Method m, Object obj,
Map<String,Object> info) throws Exception{
76

## Página 83

CasadoCódigo Capítulo3.MetadadoseAnotações
Annotation[][] paramAnnot = m.getParameterAnnotations();
Object[] paramValues = new Object[paramAnnot.length];
for(int i=0; i<paramValues.length; i++){
String name = getNomeParametro(paramAnnot[i]);
paramValues[i] = info.get(name);
}
return m.invoke(obj, paramValues);
}
public static String getNomeParametro(Annotation[] ans){
for(Annotation a : ans){
if(a instanceof Param){
return ((Param)a).value();
}
}
throw new RuntimeException("Anotação @Param não encontrada");
}
Alistagemaseguirmostraumexemplodeusodessemétodo.U mmétodo
chamado metodocomdoisparâmetrosanotadosfoicriadoparatestarmosainvo-
cação. Nométodo main(),inicialmenteécriadoummapacomdiversosvalores
paraarecuperação dosparâmetros. Emseguida, umreferênciaparaométodo
metodoérecuperadaeométodo invocarMetodo()éinvocadopassandoesse
método,ainstânciadaclasseeomapa.
Listagem 3.18-Testandoainvocaçãodemétodoscomparâmetrosnomeados:
public class AnotacaoParametro {
public static void main(String[] args) throws Exception {
Map<String,Object> info = new HashMap<>();
info.put("inteiro", 13);
info.put("numero", 23);
info.put("string", "OK");
info.put("texto", "NOK");
AnotacaoParametro ap = new AnotacaoParametro();
Method m = ap.getClass().getMethod(
"metodo", Integer.class, String.class);
invocarMetodo(m, ap, info);
}
public void metodo(
77

## Página 84

3.3.Lendoanotações emtempodeexecução CasadoCódigo
@Param("inteiro") Integer i, @Param("texto") String s){
System.out.println("Parametro inteiro = "+i);
System.out.println("Parametro texto = "+s);
}
}
Deixocomoobservaçãodesseexemploquemuitascoisaspodemdarerradocaso
otipodoobjetorecuperadodomapanãosejaomesmodoesperadopeloparâmetro.
Deixocomoexercícioaoleitorcomplementaresseexemplo,verificandoseostipos
são compatíveisefazendoumaconversão quandopossível. Comosabercomoa
conversãodeveserfeita? T e n t eutilizarumaanotação nopróprioparâmetropara
indicarmétodosouclassesquedevemserutilizadosparafazeressaconversão.
L e n d oatributos de uma anotação com reflexão
Damesmaformaqueumaclassepodeserlidaatravésdereflexãosemaconhe-
cermospreviamente,tambémépossívelobtermosaclasserelativaaanotaçãopara
descobrirmosseusatributosemtempodecompilação. Aprincipaldiferençaéque
paraobtermosinstânciade Classquerepresentaaanotação,devemoschamaro
método annotationType()aoinvésde getClass(). Emseguida,osatribu-
tosdaanotaçãopodemserrecuperadosatravésdosmétodosquesãoutilizadospara
retorná-los.
Paraexemplificaresseprocesso,alistagemaseguir mostraumcódigo que
recuperaasanotações deumelementoeimprimenoconsolecomseusatribu-
tos. Observequeométodorecebeum AnnotatedElementcomoparâmetro,
permitindoquerecebaqualquerclassequerepresenteumelementoquepossater
anotações. Aorecuperarainstânciade Classreferenteaanotação utilizando
annotationType(),ométodoimprimeonomedaanotação eemseguidaitera
pelosseusmétodosimprimindoonomeeovalorretornado. Observequeutili-
zando getDeclaredMethods()recuperamossomenteosmétodosdeclarados
naanotação,ouseja,osquedefinematributos.
Listagem 3.19-Métodoqueimprimeosatributosdasanotações deumelemento:
public static void imprimeAnotacoes(AnnotatedElement ae)
throws Exception{
Annotation[] ans = ae.getAnnotations();
for(Annotation a : ans){
Class<?> c = a.annotationType();
78

## Página 85

CasadoCódigo Capítulo3.MetadadoseAnotações
System.out.println("@"+c.getName());
for(Method m : c.getDeclaredMethods()){
Object o = m.invoke(a);
System.out.println(" |->"+m.getName()+"="+o);
}
}
}
A listagem a seguir mostra um exemplo de uma classe com duas anota-
ções, para a qual a respectiva instânciade Class épassada para o método
imprimeAnotacoes(). Emseguidaémostradoasaídadoconsolegeradapor
esseprograma,ondeasduasanotações eseusatributossãoimpressos.
Listagem 3.20-Anotaçãoparanomearosparâmetros:
@Metadado(nome="teste",numero=34)
@Anotacao(String.class)
public class ImprimeAnotacoes {
public static void main(String[] args) throws Exception {
imprimeAnotacoes(ImprimeAnotacoes.class);
}
}
Listagem 3.21-Saídadoprogramaqueimprimeasanotações:
@Metadado
|->nome=teste
|->numero=34
@Anotacao
|->value=class java.lang.String
3.4 Limitações d a sanotações
“ A c e i t eessas limitações e se submeta a e l a sem vez de continuar insistindo em fazer a
s u avontade. ”
–Emersonnatal
Duranteessecapítulomuitacoisafoiditaarespeitodoquesepodefazercom
asanotações. Essaseção falaumpoucosobreaslimitações dessafuncionalidade
79

## Página 86

3.5.Mapeandoparâmetrosdelinhadecomandoparaumaclasse CasadoCódigo
dalinguagem,falandooquenãoseconseguefazer.Nocapítulo ??serãoabordadas
algumastécnicasquesãofrequentementeutilizadasparacontornaressaslimitações.
Aprimeiralimitação équesópodehaverumaanotação deumdeterminado
tipoparaumelemento.Imagine,porexemplo,queumaanotaçãoaponteumaclasse
parafazerumavalidaçãodeseusdados.Apartirdessaanotaçãonãoseriapossível
configurarduasclassesparafazeravalidação,poissomenteumaanotaçãodaquele
tipopodeseradicionada.Paraqueissosejapossível,umaalternativaseriaaprópria
anotaçãodarsuporteaconfiguraçãodediversasclasses.Outraalternativafrequen-
tementeutilizada,éutilizarumaoutraanotaçãoquepossuacomo valueumarray
daanotaçãooriginal,permitindoagregardiversasanotações dotipoanterior.
Outralimitação dasanotações équeelasnão possuemnenhumamecanismo
quepermitageneralizá-las,comoherançaoualgumoutrotipodeabstração. Com
essemecanismo,seriapossível,porexemplo,aobuscarumaanotação,procurarpor
todasquepossuemumadeterminadaabstração.Porém,oprincipalpontoondeisso
prejudica,équenãoépossívelestenderasanotaçõesparaadicionarnovassemânticas
enovasinformações.
Porexemplo,imaginequeumaanotação @Apossuaumaatributodotipode
umaanotação @B.Seaherançafossepossível,essetipo @Bpoderiaserestendido
poroutrasanotaçõesquepoderiamseradicionadasnolugardele.Issopermitiriaum
mecanismodemetadadosextensível,ondenovasinformações poderiamseragrega-
das,comoemumdocumentoXML,porexemplo.Comoissonãoépossível,fica-se
restritoasinformações presentesnaanotação @B,nãosendopossívelqualquertipo
deextensão.
3.5 Mapeando parâmetros de linha de comando
para u m a classe
Oobjetivodessaseçãoémostrarumexemplocompletoerealistaenvolvendoano-
tações. U mtipodeaplicaçãocomumdosframeworksbaseadosemmetadadossão
pararealizaromapeamentoentrediferentesrepresentaçõesdeumaentidadedaapli-
cação. Comofoimostradonoiníciodessecapítulo,existemdiversosframeworks
queutilizamdiferentesabordagensparamapearclassesdaaplicaçãoparatabelasdo
bancodedados. Deformasimilar,existemoutrosframeworksquemapeiamclas-
sesparaentidadesdedocumentosXML,mapeiammétodosparawebservicese,até
mesmo,mapeiamclassesdediferentesaplicações querepresentamomesmocon-
ceito.
80

## Página 87

CasadoCódigo Capítulo3.MetadadoseAnotações
Seguindoessetipodeaplicação,oexemploqueserádesenvolvidoirámapearos
parâmetrosrecebidoparaaplicaçãonalinhadecomandoparaumaclassecompro-
priedadesparafacilitarsuarecuperaçãoposteriormente.Osparâmetrosdelinhade
comandosãorecebidospelométodo main()comumarrayde Stringnaordem
quesãopassadosparaaplicação.Usualmente,utiliza-seletrasnaforma -xparain-
dicarqueapróximapalavraseráovalordaquelapropriedade.Oexemploqueserá
desenvolvidoirárecebercomoparâmetrooarrayde Stringcomosparâmetrose
iráinserirosdadosemumainstância,deacordocomasanotações desuaclasse,que
indicarãoqueatributodevereceberqualparâmetro.
Apróximalistagemmostraaanotação queseráutilizadaparamapearmosos
atributosparaosparâmetros. Observequecomotodaanotação queprecisaser
consumidaemtempodeexecução, elapossuiaretenção como RUNTIME.Outro
pontoimportanteéqueessaanotação éparaserutilizadaematributos,portanto
énesseselementosqueomapeamentodeveserfeito. A p e s a rdomapeamento
ser feitonos atributos, comoesses normalmentesão privadospor questões de
encapsulamento,serãoosrespectivosmétodossettersquedevemserutilizadospara
ainserçãodoparâmetronaclasse.
Listagem 3.22-Anotaçãoparamapearparâmetrosparaatributos:
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Parametro {
String value();
}
Paraexplicarmelhorcomoomapeamentoseráfeito,aclasseaseguirmostra
oexemplodeumaclassemapeada. Ocomponentedesenvolvidodarásuportea
trêstiposdeparâmetros: booleanos, Stringearrayde String. Nocasode
parâmetrosbooleanos,apresençaounãodesuamarcaçãoindicaseeleéverdadeiro
oufalso.Porexemplo,se -pestiverpresenteentreosparâmetros,precisa-seatribuir
ovalorverdadeironoatributo possui.Nocasodeuma String,deve-sepassar
amarcaçãodoparâmetroseguidodeseuvalor,como,porexemplo, -s console
paraconfigurarovalordoatributo saída. Ofuncionamentoserásimilarpara
arraysde String,excetopelofatodediversosvalorespoderemserpassadosdepois
damarcaçãodoparâmetro.
Listagem 3.23-Exemplodeumaclasseanotadaparareceberosparâmetros:
81

## Página 88

3.5.Mapeandoparâmetrosdelinhadecomandoparaumaclasse CasadoCódigo
public class ParamApp {
@Parametro("-p")
private boolean possui;
@Parametro("-n")
private boolean naoPossui;
@Parametro("-a")
private String[] arquivos;
@Parametro("-s")
private String saida;
//métodos get e set omitidos
}
Parainiciarodesenvolvimentodessecomponentedeleituradeparâmetros,
vamoscomeçardesenvolvendooseuconstrutor,queiráreceberaclassemapeada
comaanotação @Parametroejávaiefetuaraleituradosseusmetadados.Como
resultado,serágeradoummapacujachaveéamarcação doparâmetro,queé
passadocomovalordaanotação,earespectivainstânciade Field.Observequea
classe MapeamentoParametrospossuiumtipogenérico,quedeveseromesmo
daclassepassadacomoparâmetro. Esseparâmetrogenéricoseráutilizadopara
determinaroretornodométodoquemapearosparâmetrosparaumainstância
dessaclasse.
Listagem 3.24-Exemplodeumaclasseanotadaparareceberosparâmetros:
public class MapeamentoParametros<E> {
private Map<String, Field> parametros;
private Class<E> clazz;
public MapeamentoParametros(Class<E> c) {
parametros = new HashMap<>();
clazz = c;
Class<?> current = c;
while (current != Object.class) {
for (Field f : current.getDeclaredFields()) {
82

## Página 89

CasadoCódigo Capítulo3.MetadadoseAnotações
if (f.isAnnotationPresent(Parametro.class)) {
Parametro p = f.getAnnotation(Parametro.class);
parametros.put(p.value(), f);
}
}
current = current.getSuperclass();
}
}
}
Segundoosrequisitos,édesejadoquetodososatributossejampesquisados,in-
cluindoosquesãoprivadoseosdasuperclasse.Dessaforma,doislaçossãoutiliza-
dosparapercorrerosatributos,sendoqueoprimeiroiteradaclassepassadacomo
parâmetroseguindopelassuassuperclassesaté Object,eosegundoiterasobreos
atributosdecadaclasserecuperadoscom getDeclaredFields().
Seguindoumaabordagem bottom-updedesenvolvimento,naqualprimeiro
sedesenvolveasfunções auxiliaresedepoisafunção principal,vamoscomeçar
pordesenvolverummétodoqueretornaainstânciade Methodquerepresenta
ométodosetterdo Fieldpassadocomoparâmetro. Comopodeservistono
códigodapróximalistagem,inicialmenteégeradoonomedométodosetterapartir
donomedoatributoeemseguidapercorre-setodaalistademétodosdaclasse
buscandoummétodocomessenome. Comonão sesabeexatamentequalseráo
tipodoparâmetro,nãoépossívelbuscarométododiretamente.Casoométodonão
sejaencontrado,umaexceçãoserálançada.
Listagem 3.25-Métodoquerecuperaosetterreferenteaumatributo:
private Method getSetter(Field f) {
String nomeMetodo = "set"
+ Character.toUpperCase(f.getName().charAt(0))
+ f.getName().substring(1);
for(Method m : clazz.getMethods()){
if(m.getName().equals(nomeMetodo))
return m;
}
throw new MapeamentoException(nomeMetodo +"() não encontrado");
}
U moutrométodoauxiliaraserdesenvolvidoéqueinserenaclasseovalordo
parâmetro. Elerecebeainstânciadaclassemapeada,onomedoparâmetroea
83

## Página 90

3.5.Mapeandoparâmetrosdelinhadecomandoparaumaclasse CasadoCódigo
listadevaloresqueforampassadosdepoisdele.Comopodeservistonalistagema
seguir,ométodo inserir()inicialmenterecuperao Fieldrelacionadocomo
nomedoparâmetroeemseguidaométodosetterrelacionadoao Fieldatravés
dométodo getSetter(). Porfim,paraquesejapossívelinvocarométodo,o
método recuperarValor()retornaovaloraserutilizadocomoparâmetrode
acordocomotipoesperadopelométodo.
Listagem 3.26-Métodoqueinsereumparâmetronaclasse:
private void inserir(E instancia, String nomeParametro,
List<String> valores) {
Field f = parametros.get(nomeParametro);
if(f == null){
throw new MapeamentoException(nomeParametro +
": parâmetro não previsto");
}
Method m = getSetter(f);
Object valor = recuperarValor(nomeParametro, valores, m);
try {
m.invoke(instancia, valor);
} catch (IllegalAccessException | IllegalArgumentException
| InvocationTargetException e) {
throw new MapeamentoException(
"Problemas ao invocar "+m.getName(), e);
}
}
Alistagemaseguirmostraarecuperaçãodovalordalistade Stringdeacordo
comotipodoparâmetroesperadopelométodo.Diferentementedosexemplos
anteriores,essesepreocupaemvalidarseaentradaestádeacordocomoesperado.
Nessecaso,onúmerodeparâmetrosnalista,quesãopassadosdepoisdomarcador,
devesercompatívelcomotipodoparâmetro.Sendoassim,seotipoforbooleano
nãodevehavernenhumparâmetro,sefor Stringdevehaverumvalor,eseforum
arrayde Stringpodehaverqualquernúmero.Observequeotipoconsiderado
éodoparâmetrorecebidopelométodosetterenãoodoatributo.Sendoassim,o
atributopoderiaterumtipodiferenteeserconvertidoapartirdovalorrecebido
pelométododeatribuição.
Listagem 3.27- Métodoque retorna o valor de acordo com o parâmetrodo
84

## Página 91

CasadoCódigo Capítulo3.MetadadoseAnotações
métodosetter:
private Object recuperarValor(String nomeParametro,
List<String> valores, Method m) {
if(m.getParameterTypes()[0] == boolean.class ||
m.getParameterTypes()[0] == Boolean.class){
if(valores.size() > 0){
throw new MapeamentoException(nomeParametro +
" não pode possuir valor");
}else {
return true;
}
}else if(m.getParameterTypes()[0].isArray()){
return valores.toArray(new String[valores.size()]);
}else{
if(valores.size() != 1){
throw new MapeamentoException(nomeParametro +
" só pode possuir um valor");
}else {
return valores.get(0);
}
}
}
Parafinalizaroexemplo,alistagemaseguirmostraométodo mapear(),que
éométodoprincipalparaarealização domapeamento. Inicialmente,ométodo
criaumainstânciadaclasseparainserirosparâmetros,assumindoqueelapossui
umconstrutorvazio. Emseguidapercorreoarrayde Stringrecebidocomo
parâmetrobuscandopormarcadores,queseriamcomeçadoscom“-” .Aoencontrar
ummarcador,ospróximosvaloresserão inseridosnalistadevaloresatéqueum
novomarcadorsejaencontradoouatéquesechegueaofinaldoarray.Aofinalizar
deguardarosvaloresrelacionadoscomummarcador,ométodo inserir(),
mostradoanteriormente,éinvocadoparainserirovalornaclassecorretamente.
Listagem 3.28-MétodoquerecebearraydeStringeretornainstânciadeclasse
mapeada:
public E mapear(String[] args) {
String nomeParametro = null;
List<String> valores = new ArrayList<>();
85

## Página 92

3.6. Considerações finais CasadoCódigo
E instancia = null;
try {
instancia = clazz.newInstance();
} catch (InstantiationException | IllegalAccessException e) {
throw new MapeamentoException(clazz.getName()
+ " não pode ser instanciada", e);
}
for (int i = 0; i < args.length; i++) {
String token = args[i];
if (token.startsWith("-")) {
nomeParametro = token;
} else {
valores.add(token);
}
if (args.length == i + 1 || args[i + 1].startsWith("-")) {
inserir(instancia, nomeParametro, valores);
nomeParametro = null;
valores.clear();
}
}
return instancia;
}
Observequeocódigocriadonesseexemplopoderiaserutilizadoemprogramas
reaisdelinhadecomandoparaarecuperaçãoeinterpretaçãodeseusparâmetros.
Semaconfiguraçãodemetadadosadicionaisaosdaclassenãoseriapossívelimple-
mentaressafuncionalidade,poisasinformações daprópriaclassenão seriamsu-
ficientesparasaberqueparâmetroérelacionadocomcadaatributo.Versões mais
sofisticadaspoderiamproversuporteaparâmetrosdeoutrostipos,oumesmopro-
veranotações queconfiguramcomoa Stringrecebidaseriaconvertidaparaotipo
desejado.Esseincrementoficacomoexercícioparaosleitores.
3.6 Considerações finais
Essecapítulofalousobreaconfiguraçãodemetadadosadicionaisaosdaclassepara
seremconsumidoseutilizadosporalgoritmosqueutilizamreflexão.Inicialmente,o
capítulofalousobreasopções existentesparadefiniçãodemetadados,ressaltandoas
vantagensedesvantagensdecadauma.Ousodeconvenções decódigoéfácildeser
utilizado,maspossuiexpressividadelimitadaenemsempreésuficiente.Adefinição
86

## Página 93

CasadoCódigo Capítulo3.MetadadoseAnotações
programáticademetadadospermiteumamaiorflexibilidade,masacabanãosendo
produtivaporutilizarcódigoimperativoparaumaconfiguraçãodeclarativa.Fontes
externasdemetadadospodemsermaisfacilmentemodificadas,masadefiniçãode
metadadosémaisverbosaeficadistantedocódigo.Porfim,asanotaçõesminimizam
aquantidadedeconfigurações, mascomplicaoreúsodaclasseemoutroscontextos
enãopodemserutilizadasparaclassesquenãosetemacessoaocódigo.
Emseguida,ocapítulofocouemmostrarcomoasanotações sãodefinidaseuti-
lizadasemJava.Inicialmentefoimostradocomoumanovaanotaçãopodesercriada
equaissãoasopções quepodemserconfiguradas.Emseguidafoimostradocomo
asanotações podemserrecuperadaspelaAPIdereflexãoparaseremutilizadaspor
umaclasseoucomponente.Porfim,umexemplomaiscompletomostroucomoo
mapeamentoentrerepresentações deumaentidadepodeserfeitoatravésdaconfi-
guraçãodemetadados.
87

## Página 95

Capítulo4
ProxyDinâmico
“Nuncaf aça por u mintermediárioo q u evocêpode fazer vocêmesmo”
–provérbioitaliano
NoscapítulosanterioresforammostradasasprincipaisfuncionalidadesdaAPI
dereflexão.Inicialmentefoimostradocomoobterareferênciaparaasclassesecomo
utilizarsuasinformações paramanipularsuasinstâncias.Emseguida,falou-sesobre
adefinição demetadadosecomoelespodemserutilizadosparaadicionarnovas
informações sobreoselementosdeumprograma.Apartirdessasfuncionalidades
mostrou-sealgunsexemplosmaiscompletodecomoessasfuncionalidadespodem
serutilizadasparagerarcomponentesreutilizáveisquepoderiamserutilizadosem
softwaresreais.
U m adasfuncionalidadesmaisimpressionantesdaAPIReflectiondalinguagem
Javaéacriaçãodeproxiesdinâmicos.Deumaformabeminformal,apartirdelesé
possívelcriarumainstânciaqueimplementaumainterfaceemtempodeexecução.
Emoutraspalavras,elepodeimplementarainterfacequevocêquiser,tendouma
formadetrataraschamadasdemétodofeitasparaosmétodosdessainterface. A

## Página 96

4.1.Oqueéumproxy? CasadoCódigo
partirdissoépossívelterumaúnicaclassequepodeencapsularoutrasclassescom
diferentesmétodoseinterfaces.
Melembroqueaminhareação aoverousodeumproxydinâmicopelapri-
meiravezfoialgocomo:“M a spode fazer isso? V a l efazer isso?” .Eracomodescobrir
umanovaregranomeiodojogo,quecertamentepoderiameajudaravencê-lode
formabemmaisfácilemaisinteligente.Apartirdealgunsexemplos,essecapítulo
irámostrar,nãosomentecomoutilizaressatécnica,mastambémcomoelapodeser
usadaparaintroduzirnovoscomportamentosnasclassesdeformatransparente.É
essaa“magia”quealgunsframeworksutilizamparaquecertascoisassimplesmente
aconteçamaoinvocarmosummétododasclassesdaprópriaaplicação.
AlémdousodaAPIReflectionparagerarproxiesdinâmicosapartirdeinterfa-
ces,essecapítulotambémvaimostrarousodaferramentaCGLibparagerarproxies
dinâmicosapartirdeclasses,oqueémuitoútilparaclassescomoJavabeans.Ele
tambémiráfalarsobreousodeanotações paraauxiliarnodesenvolvimentodafun-
cionalidadedoproxydinâmicoecomoessafuncionalidadepodeserutilizadapara
geraremtempodeexecução umimplementação deumainterface,semhaverne-
nhumaclassecompiladarealmentequeaimplemente.Comooscapítulosanteriores,
aofinalseráapresentadoumexemplomaiscompletoqueconsolidaoconhecimento
emproxiesdinâmicos,relacionando-oscomoquevimosnoscapítulosanteriores.
4.1 O que é u m p r o x y ?
Antesdeentrarmosnodetalhedecomofuncionaumproxydinâmico,primeirova-
mosrevisaroconceitodeproxy.OProxyéumpadrãodeprojetoquetemoobjetivo
deprotegeroacessodeobjetos,deformatransparenteasclassesqueoutilizam.O
padrãoDecorator,apesardepossuirumobjetivodiferente,queédeadicionarno-
vasfuncionalidadesaclasse,possuiumaestruturamuitosimilar.Ambosospadrões
encapsulamaclasseoriginal,intermediandooacessoaela.Dessaforma,enquanto
ocontroleestivercomaclasseintermediária,elapodeexecutarverificações dese-
gurançaououtrasfuncionalidades,antesderepassarocontroledaexecuçãoparaa
classeoriginal.
Apalavra p rox yeminglêssignifica intermediário,oqueéumametáforaade-
quadaparaessepadrão,vistoqueoproxyintermediaoacessoentreoobjetocliente
eoobjetooriginal.Muitaspessoasestãoacostumadascomousodonome p rox ypara
osproxiesderede,quedecertaformapossuemumcomportamentoanálogo.Nesse
caso,quandoexisteumproxy,aoinvésdeenviarospacotesderedeparaoendereço
90

## Página 97

CasadoCódigo Capítulo4. ProxyDinâmico
dedestino,elessãoenviadosparaoproxy,queentãoredirecionaparaoendereçoori-
ginalservindocomoumintermediário.T a n t oparaocliente,quantoparaodestino
original,étransparenteaexistênciadoproxy.Porémapesardessatransparência,o
proxypodeprestardiversosserviçosestandonomeiodocaminho,comoafiltragem
deconteúdos,controledousodebanda,autenticação,entreoutros.
Afigura4.1ilustraofuncionamentodeumproxy.Oprimeiropontoimportante
équeoobjetoquefazopapeldoproxydevepossuiramesmainterfacedaclasse
original,deformaqueelepossaassumirolugardelanaclasseclientedeformatrans-
parente.
Outropontoquedeveserressaltadoéqueoproxydevepossuirumareferência
paraumobjetodaclasseencapsulada,deformaapoderrepassaraschamadaspara
elequandonecessário.Sendoassim,quandoaclasseclienteinvocaralgummétodo
noproxy,esteiráexecutaralgumafuncionalidadee,senecessário,irárepassara
chamadaparaoobjetodaclasseencapsulada.V a l eressaltarquequalquerobjetoque
implementarainterfacepodeserencapsuladodentrodoproxy,oquepermiteque
diversosproxiespossamserencadeados.
Figura4.1:Funcionamentodeumproxy
Exemplosdessetipodeproxyforammostradosnaseção 1.1,maisespecifica-
mentecomasclasses LoggingAsyncProxye ProdutoDAOAsync,queimple-
91

## Página 98

4.2. ProxydinâmicocomaAPIReflection CasadoCódigo
mentavamproxiesqueexecutavamométododaclasseencapsuladaemumathread
diferente.Observequeessasclassesimplementamamesmainterfacequeoobjeto
queelasestãoencapsulandoerecebememseuconstrutor.Emcadamétodo,oproxy
executaasuafuncionalidade,quenocasoécriarumanovathread,edepoisinvocao
métodonoobjetooriginal.Paraosclientequeesperamumobjetoqueimplementea
interface,étransparenteofatodoproxyestarpresenteounão.Dessaforma,écomo
seessafuncionalidadepudesseserplugadanoobjetooriginal.
Oproxyimplementadodessaformafuncionamuitobemquandoprecisaser
aplicadoaclassesquecompartilhamumamesmainterface,pois,nessecaso,uma
únicaimplementação doproxypoderiaserutilizadaparaqualquerclasse. Opro-
blemadessaabordagemestáquandoasclassesqueoproxyprecisaencapsularnão
possuemumainterfaceemcomum.Nessecaso,paracadainterfacediferentepreci-
sariasercriadaumaclassedeproxy,oquepoderiagerarrepetiçãodecódigocomo
nocasodasclasses LoggingAsyncProxye ProdutoDAOAsync,quepossuemum
códigomuitosimilar.
4.2 Pr o x ydinâmico co m a API Reflection
AAPIReflectionpossuiumrecursoquepermiteacriaçãodeumobjetoqueimple-
mentaumainterfaceemtempodeexecução. Esseobjetoécriadoporumaclasse
daAPI,porémtodasaschamadasdemétodorecebidasporelesãoredirecionadas
paraumaimplementaçãodainterface InvocationHandler.Essaimplementação
équemcontémafuncionalidadedoproxyeredirecionaaschamadasparaaclasse
original.Aseguirémostradopassoapassoacriaçãodeumproxydinâmicoeexpli-
cadocommaisdetalhecomoelefunciona.
Receita p a r acriar um p r o x ydinâmico
V a m o smostrarnessaseção,passoapassocomocriarumproxydinâmicocom
aAPIdereflexão.Comoexemploserámostradaaimplementaçãodeumproxyque
executaosmétodosdaclasseencapsuladadeformaassíncrona,ouseja,emumanova
thread. Aideiaéqueessaclasseimplementeamesmafuncionalidadedasclasses
LoggingAsyncProxye ProdutoDAOAsync,porémdeformaapoderserreutili-
zadaparaqualquerinterface.
Primeiropasso para implementaro proxydinâmicoéa implementação da
interface InvocationHandler,comomostradonalistagemaseguir.Essainter-
facetemapenasummétodochamado invoke(),paraoqualserãodirecionadas
92

## Página 99

CasadoCódigo Capítulo4. ProxyDinâmico
todasaschamadasdemétodo.Essemétodorecebeostrêsparâmetrosaseguir:
umainstânciadoobjetogeradodinamicamente(quenãoéoobjetoencapsulado);
ométodoquefoiinvocado;eumarraydeobjetoscomosparâmetrosqueforam
passadosparaele.
Listagem 4.1-ImplementaçãodainterfaceInvocationHandler:
public class AsyncProxy implements InvocationHandler {
public Object invoke(Object proxy, Method method, Object[] args)
throws Throwable {
return null;
}
}
Osegundopassoéencapsularoobjetooriginalnessaclasse.Observenalistagem
aseguir,quecomplementaocódigoanterior,quefoiadicionadoumatributopara
armazenaroobjetoencapsulado,oqualépassadonoconstrutor.Esseconstrutor
foidefinidocomoprivado,paraqueelesópossaserinstanciadopelemétodoque
criaoproxydinâmicoqueserádefinidonopróximopasso. Aimplementação do
método invoke()agoradelegaaexecuçãoparaoobjetoencapsulado,chamando
neleomesmométodocomosmesmosargumentos.
Listagem 4.2-Implementandooencapsulamentodoobjetooriginal:
public class AsyncProxy implements InvocationHandler {
private Object obj;
private AsyncProxy( Object obj) {
this.obj = obj;
}
public Object invoke(Object proxy, Method method, Object[] args)
throws Throwable {
return method.invoke(obj,args);
}
}
Oterceiropassoécriarummétodoestáticoqueefetivamentecriaoproxydi-
nâmico. Essemétodorecebecomoparâmetroumobjetoeretorna-oencapsu-
93

## Página 100

4.2. ProxydinâmicocomaAPIReflection CasadoCódigo
ladocomoproxy. Acriação doproxypodeserfeitaapartirdométodoestático
newProxyInstance()daclasse Proxy.
Essemétodorecebecomoprimeiroparâmetroumainstânciade ClassLoader,
paraaqualnormalmenteépassadaomesmodaclassedoobjetoqueseráencapsu-
lado,recuperadoapartirdométodo getClassLoader()de Class.
Osegundoparâmetrosãoasinterfacesasquaisoproxydinâmicodeveserapli-
cado.Noexemplo,todasasinterfacesdoobjetosãorecuperadasapartirdométodo
getInterfaces()epassadascomoparâmetro,porémpode-sepassarapenasas
interfacescujosmétodosdevemserinterceptadospeloproxy. Oúltimoparâme-
troéumainstânciade InvocationHandler,quenocasoéumainstânciada
própriaclassequeestamoscriandoencapsulandooobjetopassadocomoparâmetro.
Listagem 4.3-Métodoqueretornaobjetoencapsuladonoproxydinâmico:
public class AsyncProxy implements InvocationHandler {
public static Object criarProxy(Object obj){
return Proxy.newProxyInstance
(obj.getClass().getClassLoader(),
obj.getClass().getInterfaces(),
new AsyncProxy(obj));
}
//parte já mostrada omitida
}
Comoúltimopasso,faltaapenasadicionaraométodo invoke()afuncionali-
dadedeexecuçãoassíncronaaosmétodosdoobjetoencapsulado.Nesseexemplo,
ométodosóseráexecutadoemumathreaddiferentecasoretorne void,porque
nessecasonãoénecessárioaguardarsuaexecuçãoparapoderretornar.Ocódigoa
seguirmostraaimplementaçãodessafuncionalidadecomplementandoocódigojá
iniciadonaslistagensanteriores.
Listagem 4.4-Adicionandoafuncionalidadedeinvocaçãoassíncrona:
public class AsyncProxy implements InvocationHandler {
//método de criação do proxy omitido
94

## Página 101

CasadoCódigo Capítulo4. ProxyDinâmico
private Object obj;
private AsyncProxy( Object obj) {
this.obj = obj;
}
public Object invoke(Object proxy, Method method, Object[] args)
throws Throwable {
if(method.getReturnType() == void.class){
new Thread(
public void run(){
method.invoke(obj,args);
}
).start();
return null;
} else {
return method.invoke(obj,args);
}
}
}
Éisso!SãoessesospassosparasecriarumproxydinâmicocomaAPIReflection!
Ostrêsprimeirospassossãosempremuitosimilareseoquemudaéoúltimopasso,
ondeafuncionalidadeadicionadapeloproxyéimplementada.Essafuncionalidade,
dependendodocaso,podeserimplementadaantes,depoisouaoredordainvocação
dométododoobjetooriginal.Observequecomotemoscontroledosparâmetrosque
sãopassadoparaoobjetooriginaledoretornoqueédadoainvocaçãodométodo,
essespodemsermodificadosemanipuladospeloproxy.
Repassando exceçõ e sdo objeto original
U merrocomumaoseimplementarumproxydinâmicoestáemnãosepropagar
corretamenteasexceções lançadaspeloobjetooriginal.Podeparecerquesomente
chamandoométodonoobjetoencapsuladoepassandoosmesmosargumentosque
oresultadoseriaomesmo,porémissonão éverdadedevidoasexceções. Épre-
cisolembrarqueaexceçãolançadapelométodooriginalseráencapsuladaemuma
InvocationTargetException.
Sendoassim,apróximalistagemmostracomoseriaumproxyquenãofaznada,
somenterepassandoaschamadasparaoobjetoencapsuladoerepassandoassuas
respostas.Paraisso,alémdedevolveroretornodachamadade invoke,épreciso
capturaraexceção InvocationTargetExceptionelançaraexceção contida
95

## Página 102

4.2. ProxydinâmicocomaAPIReflection CasadoCódigo
getTargetException().Dessaforma,casooobjetooriginallanceumaexceção,
oproxyiráarepassarparaaclassecliente.
Listagem 4.5-Lançandoasmesmasexceções queoobjetooriginal:
public class NaoFAzNadaProxy implements InvocationHandler {
private Object obj;
private NaoFAzNadaProxy(Object obj) {
this.obj = obj;
}
public Object invoke(Object proxy, Method method, Object[] args)
throws Throwable {
try{
return method.invoke(obj,args);
} catch(InvocationTargetException e) {
throw e.getTargetException();
}
}
}
Funcionamento de um p r o x ydinâmico
Paraentendermelhorcomofuncionaoproxydinâmico,afigura4.2apresenta
umarepresentaçãodecomoaschamadassão realizadas. U m aconfusãocomumé
acharqueoproxydinâmicoéaimplementaçãodainterface InvocationHandler.
Naverdadeeleéumaclassecriadapelamáquinavirtualapartirdosparâmetros
passadosparaométodo newProxyInstance()daclasse Proxy.Ainstânciado
proxyseráutilizadanolugardoobjetooriginaldeformatransparenteparaaclasse
cliente,vistoqueimplementaainterfaceesperadaporele.Sendoassim,oproxyirá
receberaschamadasdemétodosnormalmentecomoqualquerclasse.
96

## Página 103

CasadoCódigo Capítulo4. ProxyDinâmico
Figura4.2:Funcionamentodoproxydinâmico
Aoreceberessachamadademétodo,ométodo invoke()daimplementação
de InvocationHandleréchamado.Oprimeiroparâmetroqueépassadopara
essemétodo,comojáfoiditoanteriormente,éoobjetodoproxyquefoigeradodi-
namicamente.Alémdisso,essemétodotambémrecebeométodoeseusparâmetros,
dandocondições dereplicarachamadadométodonoobjetoencapsulado.Sendo
assim,aimplementaçãode InvocationHandlerpodeexecutarasuafuncionali-
dadeerepassarachamadaparaoobjetoencapsuladoquandoforadequado.
4.3 Gerando a implementação de u m a interface
U mproxydinâmiconormalmenteencapsulaumobjetoparaacrescentarumafun-
cionalidadeaele,independentedasuainterface. Porém,comopodeservistono
exemplomostradonaseção anterior,todoesseencapsulamentoéfeitonaimple-
mentaçãode InvocationHandler. Sendoassim,seriapossívelgerarumproxy
dinâmicoparaumainterface,tratandoaschamadasparatodososseusmétodos,
semrealmenteestarencapsulandoumaimplementaçãoconcretadessainterface.
97

## Página 104

4.3.Gerandoaimplementaçãodeumainterface CasadoCódigo
Talvezvocêestejaseperguntandonessemomento:comovousaberqualdeveser
ocomportamentoparaosmétodosdeumainterface?Arespostaésimples:através
deseusmetadados!Onomedaclasse,onomedométodo,seusparâmetrosesuas
anotações podemfornecerinformações suficientesparaqueoproxysaibaalógica
queeleprecisaexecutarquandoumdeterminadométodoforinvocado.Dessaforma,
adefinição daassinaturadométodojuntamentecommetadadosadicionaisserão
responsáveispordefinirseucomportamento.ÉcomoseelesdefinissemumaDSL
internaparaadefiniçãodocomportamentodaquelasclasses.
O que é u m a DSL interna?
OacrônimoDSLsignifica Domain Specific Language,queemportu-
guêsseriatraduzidocomo linguagem específica de domínio. Diferente-
mentedeumalinguagemdepropósitogeral,comoJava,quepodeser
utilizadaparadesenvolverqualquertipodeprograma,umaDSLpos-
suiumpropósitomaisespecífico,sendoutilizadasomentedentrodeum
domínio.U mexemplodeumaDSLéalinguagemSQL,quepossuio
propósitodeexecutaroperações embasesdedadosrelacionais.
U m aDSLinternaéumalinguagemespecíficadeumdomínioque
écriadadentrodeumalinguagemdepropósitogeraljáexistente. No
casodacriaçãodeumproxyquegeraumaimplementaçãobaseadana
assinaturadeummétodo,oselementosdessaassinaturapassamapos-
suirumasemânticaespecíficadodomíniodoproxy,quevaigerar,nesse
caso,umcomportamentoemtempodeexecução.Alimitaçãodessalin-
guageminternaacabasendoalimitaçãodasintaxedapróprialinguagem
queestásendoutilizadacomobase.Esse“jeito”decriaraassinaturado
método,nadamaiséqueumanovalinguagemmaisespecíficaqueestá
sendocriadaparaodomíniodoproxy.
Paraexemplificarmosautilizaçãodessaabordagem,vamosverumexemplode
umproxyquegeraaimplementaçãodeumainterfacequeapartirdosnomesdos
métodosretornaumapropriedadedesistema.Porexemplo,seainterfacepossuirum
método getUserHome(),eleiráretornarapropriedadedesistema user.home.
Dessaforma,oproxyprecisainterpretaronomedométodoparaextraironomeda
propriedadequeprecisaretornar.
Oprimeirométodoauxiliardesenvolvido,separaa Stringcomonomedo
98

## Página 105

CasadoCódigo Capítulo4. ProxyDinâmico
métodoemumarrayde String,comospedaçosquesão separadosporletras
maiúsculas.Porexemplo,ocódigotransformaria "getCamelCase"em {"get",
"camel", "case"}.Aimplementaçãoestáapresentadanalistagemaseguir.Os
caracteresda Stringsãopercorridoseadicionadosnavariávelcorrente,queé
adicionadaalistaezeradaaoseencontrarumcaracteremaiúsculo.
Listagem 4.6-MétodoqueseparaaStringporsuasletrasmaiúsculas:
public String[] separaPorMaiusculas(String nome){
List<String> lista = new ArrayList<>();
String corrente = "";
for(int i=0; i<nome.length(); i++){
if(Character.isUpperCase(nome.charAt(i))){
lista.add(corrente);
corrente = "";
corrente += Character.toLowerCase(nome.charAt(i));
}else{
corrente += nome.charAt(i);
}
}
lista.add(corrente);
return lista.toArray(new String[lista.size()]);
}
Osegundométodoauxiliar,apresentadoaseguir,éoquerecebea String
divididaeretornaonomeesperadoparaapropriedade. Elepegacada String
eadicionaemumaúnica,dividindo-asporum ".". Observequeobloco for
começasuaiteraçãopelosegundoelementoparapularaprimeira Stringqueseria
o "get". Porexemplo,ocódigotransformaria {"get", "camel", "case"}
em "camel.case".
Listagem 4.7-TransformaçãodoarraydeStringemnomedapropriedade:
public String nomePropriedade(String[] strs){
String nomeProp = "";
for(int i=1; i<strs.length; i++){
if(i != 1){
nomeProp += ".";
}
nomeProp += strs[i];
99

## Página 106

4.3.Gerandoaimplementaçãodeumainterface CasadoCódigo
}
return nomeProp;
}
Porfim,aclasse SystemPropertiesRetrievernapróximalistagemrealiza
aimplementação doproxypropriamentedito. Ométodo invoke()chamao
métododeseparação pormaiúsculas,extraionomedapropriedadeearetorna,
utilizandoachamada System.getProperty(). Ométodoestático criar()
quefazacriação doproxy,recebecomoparâmetroo Classquerepresentaa
interfaceeretornaumobjetoqueaimplementadinamicamente. Observequena
chamadade newProxyInstance()umarraycomaprópriainterfaceépassado
comoosegundoparâmetroeumainstânciadaprópria classeépassadocomo
terceiroparâmetro.
Listagem 4.8 - Implementação do proxyque retornaa propriedadedo sistema
deacordocomonomedométodo:
public class SystemPropertiesRetriever implements InvocationHandler {
public static <E> E criar(Class<E> interf){
return (E) Proxy.newProxyInstance
(interf.getClassLoader(),
new Class[]{interf},
new SystemPropertiesRetriever());
}
@Override
public Object invoke(Object proxy, Method method, Object[] args)
throws Throwable {
String[] split = separaPorMaiusculas(method.getName());
String nomeProp = nomePropriedade(split);
return System.getProperty(nomeProp);
}
}
Paraexemplificarautilizaçãodoproxydesenvolvido,alistagemaseguirmostra
uminterfacequepossuimétodospararecuperação dediversaspropriedadesdo
sistema. Aseguir,éapresentadoummétodo main()quecriaoproxybaseado
nessainterfaceeimprimeaspropriedadesdosistemanoconsole.V a l eobservarque
essaimplementação não fazmuitasverificações adicionaisemrelação aométodo
100

## Página 107

CasadoCódigo Capítulo4. ProxyDinâmico
recebidocomoparâmetro. Ométodopoderia,porexemplo,possuirparâmetros
ouumtipoderetornonãoadequado.Deixoaimplementaçãodessetratamentode
errocomoexercícioaosleitores.
Listagem 4.9-Exemplodeusodoproxydesenvolvido:
public interface SystemProperties {
public String getUserCountry();
public String getUserLanguage();
public String getUserHome();
public String getJavaVmSpecificationVersion();
public String getJavaHome();
public String getFileSeparator();
}
public class Principal {
public static void main(String[] args) {
SystemProperties sp =
SystemPropertiesRetriever.criar(SystemProperties.class);
System.out.println(sp.getUserHome());
System.out.println(sp.getUserCountry());
System.out.println(sp.getUserLanguage());
System.out.println(sp.getFileSeparator());
System.out.println(sp.getJavaHome());
System.out.println(sp.getJavaVmSpecificationVersion());
}
}
101

## Página 108

4.4. ProxydeclassescomCGLib CasadoCódigo
Framework Esfinge Query Builder
Paraperceberopotencialdessapráticaéinteressanteverumexemplo
maisavançadodeutilização.OframeworkEsfingeQueryBuilderutiliza
aassinaturadosmétodosparagerarconsultasparadiferentestiposde
bancodedados. Paraisso,são combinadasinformações daassinatura
dométodo,anotações nosparâmetrosedosprópriostiposdosparâme-
tros.Épossível,porexemplo,definiratravésdeumaanotaçãoemuma
interface,novostermosdedomínioparaseremutilizadosnosnomesdos
métodos.Devidoadiversidadedepossibilidadesquesechegoucomessa
DSLinterna,estãoemdesenvolvimentopluginsparaEclipsequefazem
averificaçãodonomedosmétodosemtempodecompilaçãoequees-
tendemomecanismoderefatoraçãoderenomeaçãoparaqueosnomes
dosmétodossejamtambémmodificadosquandonomesnasclassesper-
sistentesforemalterados.
4.4 Pr o x yde classes co m C G Lib
“ Q u e mnão t e mcão, caça com gato. ”
–ditadopopular
U mdosproblemasdoproxydinâmicodaAPIReflectiondalinguagemJavaéque
elesópodeseraplicadoparamétodosdeinterfaces.A t émesmoclassesquepossuem
umainterface,nãopodemserinterceptadaspeloproxydinâmicoemmétodosfora
dessainterface.IssoéumproblemaespecialmenteparaclassesnosestiloJavaBeans,
poisnãofazmuitosentidopossuirumainterfaceparaosmétodosdeacessoaosseus
atributos. Imagineprecisarcriarumainterfaceparacadaclassededomíniocom
todosseusmétodosgettersesetterssomenteparapoderutilizarumproxydinâmico
emseusmétodos.
Felizmenteexisteumaalternativa!AbibliotecaCGLib,umacrônimopara Code
Generation L i b r a r y,possibilitaacriaçãodeproxiesdinâmicosparaclassesapartirde
geraçãodebytecode.Emtermosdeprogramação,odesenvolvimentodeumproxy
dinâmicocomCGLibnãoémuitodiferentedeumproxydinâmicocomaAPIRe-
flection.Nãovamosentrarmuitoemdetalhesaquisobrecomofuncionaoprocesso
degeraçãodebytecodeecarregamentodinâmicodeclassesemtempodeexecução,
porémesseprocessoserámelhordetalhadonocapítulo ??.
102

## Página 109

CasadoCódigo Capítulo4. ProxyDinâmico
P r o x yp a r aarmazenar histórico de valores
Para utilizar o CGLib em um projeto, basta adicionar o arquivo
cglib-nodep-3.1.jaremseuclasspath.Paraexemplificarousodoproxy,será
desenvolvidaumaclassequeguardaohistóricodevaloresqueforamatribuídosa
umapropriedadedeumJavaBean,permitindosuarecuperaçãoposterior.Antesde
criaroproxy,vamosdefinirumainterfaceparapermitirarecuperaçãodohistórico
devaloresdeumapropriedade. Adefinição dessainterfaceestáapresentadana
listagemaseguir.Elaseráutilizadaparaserincorporadanaclassequeserágerada
dinamicamente. Dessaforma,quandoachamadadométododessainterfacefor
redirecionadaparaoproxy,eleretornaovalordohistóricoaoinvésderedirecionar
achamada.
Listagem 4.10-Interfacepararecuperaçãodohistórico:
public interface RecuperadorHistorico {
public List<Object> getHistorico(String prop);
}
ParacriaroproxycomoCGLib,ainterfacequeprecisaserimplementadaé
MethodInterceptorquepossuiapenasométodo intercept(),oqualserá
chamadoacadachamadadométodo.Aúnicadiferençadométodointercept()
paraométodo invoke()de InvocationHandleréseuquartoparâmetrodo
tipo MethodProxy.Essaclasseéumaoutraformadeacessarmétodosprovidopelo
CGLib.PorenquantovamosignoraresseparâmetroeutilizaraAPIdereflexão,mas
voltaremosaissonocapítulo ??queiráabordaroutrasfuncionalidadesdoCGLib.
Apróximalistagemapresentaoproxyquearmazenaohistórico devalores
daspropriedadesdeumJavaBean. Aclassearmazenacomoatributosoobjeto
encapsulado,deformasimilaraoquefoimostradoparaoproxydaAPIReflection,
eummapaqueparacadapropriedadeguardaumalistadevalores. Nessaversão
do código, o método intercept() ainda estáincompleta, apresentandoem
comentárioscom PARA FAZER,questões queserão implementadasnapróxima
listagem. Naimplementaçãodessemétodo,oprimeirocondicionalidentificaseo
métodoédainterface RecuperadorHistorico,eemcasopositivo,assume-se
queométodoexecutadoéo getHistorico(), eohistórico dapropriedade
passada comoparâmetrodeveser retornado. Nocondicionalseguinte, caso o
métodointerceptadosejaumsetter,identificadopelosufixo "set"eporreceber
umparâmetro,ovalordoparâmetroéarmazenadonohistórico. A p ó sisso,o
103

## Página 110

4.4. ProxydeclassescomCGLib CasadoCódigo
métododoobjetoencapsuladoéexecutadonormalmente.
Listagem 4.11-Proxyparaarmazenamentoerecuperaçãodohistórico:
public class Historico implements MethodInterceptor{
private Object encapsulated;
private Map<String, List<Object>> historico = new HashMap<>();
public Historico(Object encapsulated) {
this.encapsulated = encapsulated;
}
public Object intercept(Object obj, Method m, Object[] args,
MethodProxy proxy) throws Throwable {
if(m.getDeclaringClass().equals(RecuperadorHistorico.class)){
//PARA FAZER: retorna o histórico
}
if(m.getName().startsWith("set") &&
m.getParameterTypes().length == 1){
String prop = deSetterParaPropriedade(m.getName());
//PARA FAZER: armazena valor no histórico para propriedade
}
try {
return m.invoke(encapsulated, args);
} catch (InvocationTargetException e) {
throw e.getTargetException();
}
}
private static String deSetterParaPropriedade(String nomeSetter){
StringBuffer retorno = new StringBuffer();
retorno.append(nomeSetter.substring(3, 4).toLowerCase());
retorno.append(nomeSetter.substring(4));
return retorno.toString();
}
}
U m aquestãoaserressaltadaéotratamentoespecialcasoométodosejadain-
terface RecuperadorHistorico,queseráadicionadanoproxyindependenteda
classeoimplementarounão. Essecasoespecialexemplificacasosemquedeseja-
mosadicionarmétodosnoproxyqueserágerado. Comoessesmétodonão po-
demserrepassadosaoobjetoencapsulado,elesdevemseridentificadosdentrodo
104

## Página 111

CasadoCódigo Capítulo4. ProxyDinâmico
intercept()eumalógicaadequadadeveserexecutadaemresposta.Nessecaso,o
resultadoéumvalordoproxyquedeveserretornado.A p e s a rdesseexemploutilizar
aCGLib,umaestratégiaparecidapodeserutilizadaquandofornecessárioadicionar
métodosnoproxygeradocomaAPIReflection.
A listagem a seguir, mostra o código do método intercept() com-
pleto. Dentrodoprimeirocondicional,queverificaseométodoédainterface
RecuperadorHistorico,éretornadaalistadevaloresarmazenadanomapa.
Observe que como nesse caso o métodointerceptado éconhecido, no caso
getHistorico(),épossívelsaberqueoprimeiroparâmetroserefereaproprie-
dade,eutilizá-locomochavederecuperação nomapa. Nosegundocondicional,
quedevefazeroarmazenamentodohistórico,éfeitaaverificaçãosejáexisteuma
listacomosvaloresdapropriedade.Casonãoexista,umalistaécriadaeinserida
nomapa,ecasojáexistaalistasimplesmenteérecuperada. Empossedalista,o
valorrecebidopelométodosettercomoparâmetro,éinseridonohistórico.
Listagem 4.12-Completandoométodointercept()doproxyHistorico:
public Object intercept(Object obj, Method m, Object[] args,
MethodProxy proxy) throws Throwable {
if(m.getDeclaringClass().equals(RecuperadorHistorico.class)){
return historico.get(args[0]);
}
if(m.getName().startsWith("set") &&
m.getParameterTypes().length == 1){
String prop = deSetterParaPropriedade(m.getName());
List<Object> list = null;
if(!historico.containsKey(prop)){
list = new ArrayList<Object>();
historico.put(prop, list);
}else{
list = historico.get(prop);
}
list.add(args[0]);
}
try {
return m.invoke(encapsulated, args);
} catch (InvocationTargetException e) {
throw e.getTargetException();
}
105

## Página 112

4.4. ProxydeclassescomCGLib CasadoCódigo
}
A listagem a seguir mostra o métodode criação do proxy, chamado de
guardar(), ondeoCGLib geradinamicamenteaclassequeirádirecionaras
chamadasparao MethodInvoker. Aclasse Enhancergera,decertaforma,
umaversãoincrementadadeumacertaclasse.Observequeéconfiguradoparaque
eleutilizeaclassedoobjetoencapsuladocomosuperclasse,quetenhaainterface
RecuperadorHistorico e que utilize uma instânciada classe Historico
pararedirecionaraschamadas. Emseguida,éretornadoumobjetodessanova
classecriadaemtempodeexecução. A p e s a rdeserdiferentedageraçãodoproxy
dinâmicocomaAPIReflection,essaéumareceitadeboloquemudamuitopouco
entrediferentesproxies.
Listagem 4.13-MétododecriaçãodoproxycomCGLib:
public static <E> E guardar(E obj) {
try {
Historico proxy = new Historico(obj);
Enhancer e = new Enhancer();
e.setSuperclass(obj.getClass());
e.setInterfaces(new Class[]{RecuperadorHistorico.class});
e.setCallback(proxy);
return (E) e.create();
} catch (Throwable e) {
throw new Error(e.getMessage());
}
}
Finalizandooexemplo,alistagemaseguirmostraumexemplodeutilização
doproxycriado. Aclasse Produto,umJavaBeancomumeseminterfaces,será
utilizadacomobaseparaageração doproxy. Observequeparaaobtenção da
instânciautilizadanoexemplo,achamada Historico.guardar()foirealizada
parageraroproxydinâmicoeencapsularoobjetopassadocomoparâmetro.Nesse
código,ovalordopreçodoprodutoéalteradodiversasvezesparatestarmosseo
históricoestásendorealmentearmazenado.
Listagem 4.14-Exemplodeutilizaçãodoproxy:
public class Principal {
106

## Página 113

CasadoCódigo Capítulo4. ProxyDinâmico
public static void main(String[] args) {
Produto p = Historico.guardar(new Produto());
p.setNome("Design Patterns com Java");
p.setMarca("Casa do Código");
p.setPreco(59.90);
//blackfriday
p.setPreco(49.90);
//normal
p.setPreco(59.90);
//natal
p.setPreco(54.90);
List<Object> lista =
((RecuperadorHistorico)p).getHistorico("preco");
for(Object valor : lista){
System.out.println(valor);
}
}
}
A p e s a rde Produtonãoimplementarainterface RecuperadorHistorico,
oproxygeradoimplementa.Então,parapoderacessarosmétodosdessainterface,
bastafazerum casteinvocarométododesejado,comomostradonalistagem.Exe-
cutandoométodo main()épossívelobservarquetodohistóricodevaloresda
propriedade precoseráimpressonoconsole.
Esseexemplopodeparecersimples,mascompequenasadições épossíveladici-
onarumareferênciadedataaohistóricodevalores,registrandoomomentodamo-
dificação.Apartirdessasinformações, épossívelgerarumacópiadoobjetocomos
valoresdaspropriedadesquepossuíaemumdeterminadomomento.Dessaforma,é
possívelrecuperaraversãoqueumdeterminadoobjetopossuiaqualquermomento
notempo.
Funcionamento de um p r o x ygerado com C G L i b
OfuncionamentodeumproxydinâmicocomCGLibéanálogoaoproxydinâ-
micocriadocomaAPIReflection,comopodeservistonaFigura4.3.Aprincipal
diferençaéquenessecasonãoexisteumainterfaceparaserumaabstraçãocomum
entreoproxyeoobjetoencapsulado.Dessaforma,asoluçãoéqueaclassegerada
pelo Enhancerestendaaclasseencapsulada,sendo,dessaforma,umasubclasse
107

## Página 114

4.4. ProxydeclassescomCGLib CasadoCódigo
dela.V a l eressaltarqueaclasse Enhancerpermitequediversasoutrasquestões se-
jamconfiguradasparaaclassegerada,porémnãoestánoescopodesselivroabordar
essasquestões.
Figura4.3:ProxydinâmicocomCGI
A cada método invocado será interceptado pela instância de
MethodInterceptorpassadonométodosetCallback()daclasse Enhancer.
De formasimilarasimplementações da interface InvocationHandler, essa
classe équemefetivamenteimplementaa funcionalidadedo proxydinâmicoe
redirecionaaschamadasaoobjetoencapsulado.
108

## Página 115

CasadoCódigo Capítulo4. ProxyDinâmico
Maturidade d oPr o j e t oC G Lib
Antesdeutilizaralgumanovabibliotecaemumprojeto,umquesti-
onamentocomuméarespeitodamaturidadedaquelabiblioteca.Muito
provavelmentesevocêdesenvolveparaaplicações corporativasjátemo
CGLibnoclasspathdasuaaplicação,poiseleéutilizadoporframeworks
degrandeaceitaçãonomercado,comooHibernateeoSpring. Sendo
assim,fiquetranquiloqueoCGLibéumabibliotecamuitomaduraejá
foiutilizadaemframeworksquesão utilizadosnodesenvolvimentode
aplicações degrandeporte.
4.5 Consumindo anotações em proxies
Nassoluções deproxydinâmicoqueforamapresentadas,todasaschamadassão
direcionadasparaomesmométododetratamento.Essemétodorecebeométodo
invocadonaclasseoriginaleseusparâmetros.Devidoanãosabermaisdométodo
doqueoqueestánosseusmetadados,oproxyacabatratandotodoselesdamesma
forma.Nosexemplos,algumasconvenções decódigoforamutilizadasparadistin-
guirosmétodos,porém,comofoiditonaseção3.1,aexpressividadedessaaborda-
gemélimitada.
Sendoassim,aconfiguração demetadadoséumaexcelentealternativapara
distinguirosmétodosdeumaclasse,permitindoqueoproxypossaterumcompor-
tamentodistintoparacadaumdeles.V a m o simaginaroexemplodeumproxyque
armazeneoresultadodechamadasdemétodoseretorneomesmoresultadocaso
umachamadasemelhantesejarealizada. Porémconsideretambémqueexistam
métodosquealteramaclasseencapsuladainternamenteeinvalidamosresultados
quejáforamarmazenados.Aodesenvolveresseproxy,oprimeiropassoseriadefinir
anotações queconfiguramsedeve-sefazercachedosretornosdeummétodo,ouse
essecachedeveserinvalidadoapartirdachamadadaquelemétodo.Essasanotações
estãoapresentadasnalistagemaseguir.
Listagem 4.15-Anotações paramarcarosmétodosinterceptadospeloproxy:
@Retention(RetentionPolicy.RUNTIME)
public @interface Cache {
}
109

## Página 116

4.5.Consumindoanotações emproxies CasadoCódigo
@Retention(RetentionPolicy.RUNTIME)
public @interface InvalidaCache {
}
Paraarmazenarosdadosdeumainvocaçãodemétodosparaoarmazenamento
docacheseráutilizadoummapa.Essemapadeveutilizarumachavequeidentifica
unicamenteaschamadasdemétodo,incluindoométodoinvocadoeosseusparâ-
metros.Dessaforma,ométodogerarChave(),apresentadonapróximalistagem,
criauma Stringapartirdonomedométodoedovalordeseusparâmetros
paraseremutilizadoscomochave. Deixocomonotaqueessageração dechaves
vaidependermuitodosobjetosteremumaimplementação adequadadométodo
toString(). Paraarrays,porexemplo,essageração dechavesnão funcionaria
muitobem.
Listagem 4.16- Métodopara geração da chave de armazenamento da invoca-
çãodométodo:
private String gerarChave(Method method, Object[] args){
StringBuilder sb = new StringBuilder();
sb.append(method.getName());
for(int i=0; i<args.length; i++)
sb.append(args[i]);
return sb.toString();
}
A listagem a seguir mostra a implementação do proxy que faz o cache se
baseandonasanotações dosmétodos.Observequenométodo invoke(),que
nessaversão aindaestáincompleto,existeumcomandocondicionalquerealiza
diferentesações dependendodaanotaçãopresentenométodo.Oprimeirocondi-
cionalverificaapresençadaanotação @InvalidaCache,eocachedaschamadas
demétodoarmazenadasatéomomentodeveserlimpoquandoeleéchamado.
Osegundocondicionalverificaapresençadaanotação @Cache, casonoqual
deveserretornadoovalordocache,casoexista,ouexecutadoométodonoobjeto
encapsuladoearmazenadoseuresultado. Observequesenão houvernenhuma
anotaçãopresente,ométodoéexecutadonormalmente.
Listagem 4.17- Implementação do proxy que faz o cache das chamadas de
método:
110

## Página 117

CasadoCódigo Capítulo4. ProxyDinâmico
public class CacheProxy implements InvocationHandler {
private Object obj;
private Map<String,Object> cache = new HashMap<>();
public CacheProxy(Object obj) {
this.obj = obj;
}
public Object invoke(Object proxy, Method method, Object[] args)
throws Throwable {
try {
if(method.isAnnotationPresent(InvalidaCache.class)){
//PARA FAZER: limpar cache
}else if(method.isAnnotationPresent(Cache.class)){
//PARA FAZER: armazenar ou retornar objeto do cache
}
return method.invoke(obj, args);
} catch (InvocationTargetException e) {
throw e.getTargetException();
}
}
public static Object criar(Object obj){
return Proxy.newProxyInstance (obj.getClass().getClassLoader(),
obj.getClass().getInterfaces(), new CacheProxy(obj));
}
}
Alistagemaseguir,apresentaométodo invoke()daclasse CacheProxy
finalizado. Observequeométodo clear()domapaquearmazenaocacheé
chamadoparalimparocachenapresençadaanotação @InvalidaCache. Jána
presençadaanotação @Cache,oprimeiropassoégerarachaverelativaainvocação
utilizandoométodo gerarChave() mostradoanteriormente. Emseguida, é
verificadoseomapaquearmazenaocachejápossuiachave.Casoachaveexista,
ovalorarmazenadonomapaéretornadoeométodonoobjetoencapsuladonemé
invocado.Poroutrolado,seachavenãoexistir,oobjetoencapsuladoéinvocado,o
seuretornoearmazenadonomapae,porfim,essevaloréretornadopeloproxy.
Listagem 4.18-Implementaçãodométodoinvoke()doCacheProxy:
public Object invoke(Object proxy, Method method, Object[] args)
throws Throwable {
111

## Página 118

4.5.Consumindoanotações emproxies CasadoCódigo
try {
if(method.isAnnotationPresent(InvalidaCache.class)){
cache.clear();
}else if(method.isAnnotationPresent(Cache.class)){
String chave = gerarChave(method, args);
if(cache.containsKey(chave)){
return cache.get(chave);
}else{
Object retorno = method.invoke(obj, args);
cache.put(chave, retorno);
return retorno;
}
}
return method.invoke(obj, args);
} catch (InvocationTargetException e) {
throw e.getTargetException();
}
}
Parafinalizaroexemplo,vamosmostrarcomoumainterfaceseriaanotadapara
autilizaçãodoproxy.Alistagemaseguirmostraainterface Operacaoquepossui
asanotações emseusmétodos.Aideiaéqueessainterfacesejaimplementada
porclassesquearmazenamumvalorinternamenteeexecutemoperações nesse
valorretornandooresultado.Nessecaso,métodos somar()e multiplicar()
queretornamumvalorbaseadonovalorinternoenoparâmetropodemterseus
retornosarmazenadosnocache.Poroutrolado,ométodo mudar()quealterao
valorinternodeveinvalidarocache,poisosretornosarmazenadosinternamente
deixamdeserválidos.
Listagem 4.19-Anotações paramarcarosmétodosinterceptadospeloproxy:
public interface Operacao<E> {
@InvalidaCache public void mudar(E obj);
@Cache public E somar(E obj);
@Cache public E multiplicar(E obj);
}
Esseproxydesenvolvidonesseexemplopodesermuitoútilparaclassesquere-
alizamchamadasremotasouexecutaoperações emumabasededados.Nessecaso,
chamadasquerecuperamdadosbaseadasnoestadodobancooudoobjetoremoto
112

## Página 119

CasadoCódigo Capítulo4. ProxyDinâmico
podemseradicionadasnocacheeasquealteramesseestados,devemserutilizadas
parainvalidarocache.Dequalquerforma,antesdedecidirutilizarumcachedesse
tipoemumaaplicaçãorealéimportantefazerumamediçãodedesempenhobaseada
emcenáriosdeusodosoftware,poisapesardocachepoderacelerarotempomédio
deretornodeummétodo,osresultadosarmazenadosocupammemória.Sendoas-
sim,paravalerapena,oganhoemvelocidadedevecompensaresseespaçoutilizado.
E se eu quiser a sanotações d ométodo d aclasse e n ã o
d ainterface?
U m aobservação importanteemrelação aoproxydinâmicodaAPI
Reflectionéqueainstânciade Methodpassadacomoparâmetroédain-
terfacequeestásendoencapsulada,enãodoobjetoquefoiencapsulado.
Comoelespossuemamesmaassinatura,muitasvezesissonãotemmuita
importância,porémessaquestãopassaaserrelevantequandoestamos
buscandoanotações, poisnessecasoimportaseforamadicionadasna
interfaceounaclasse.Porém,ofatodométodopassadoserodainter-
face,nãosignificaquedevemossempreutilizaranotações nainterface.
Quandoosmetadadosforemreferentesaabstração devemseradicio-
nadosnainterface,porémquandoforemespecíficosdaimplementação
devemseradicionadosnaclasse.
Com base no métodorecebido como parâmetro, não édifí-
cil de recuperar o mesmo métododeclarado na classe. Ima-
ginando que a variável obj represente o objeto encapsulado
e a variável m represente o métodorecebido como parâme-
tro, o métododa classe poderia ser recuperado com a chamada
obj.getClass().getMethod(m.getName(),m.getParameterTypes()).
Assimasanotações poderiamserfacilmenterecuperadasdadeclaração
dométodonaclasseeutilizadasnoproxy.
4.6 Outras formas de interceptar métodos
“ A slaranjas não são as ú n i c a sfru t as ”
–títulodeumlivrodeJeanetteWinterson
A p e s a rdeestarforadoescopodesselivro,achoimportantedizerqueexistem
113

## Página 120

4.6. Outrasformasdeinterceptarmétodos CasadoCódigo
outrasformasdeinterceptaraexecuçãodemétodosemJava.Dependendodaplata-
formaparaaqualvocêestádesenvolvendooudotipodecomponentequeestásendo
criado,aprópriaAPIpodefornecerumaalternativaparainterceptaçãodosmétodos.
Nessecaso,osmesmosconceitosapresentadosparaacriaçãodosproxiesdinâmicos
apresentadosaquipodemserutilizados.Oobjetivodessaseçãoéapresentaralguns
exemplosdessasoutrastecnologiaspara
Porexemplo,naplataformaJavaEE,existeumtipodecomponentechamado
interceptorque funciona de forma similar a um proxy dinâmico, porémpara
instânciasquesão gerenciadaspelocontainerJavaEE.Paraseruminterceptor,a
classeprecisareceberaanotação @Interceptorepossuirummétodoanotado
com @AroundInvoke,quenecessariamenteprecisareceberumparâmetrodotipo
InvocationContexteretornar Object.Ainstânciade InvocationContext
éque contémtodas as informações relacionadasa invocação, comoo método
interceptadoeosparâmetrosrecebidos.
Listagem 4.20-ExemplodeInterceptordaplataformaJavaEE:
@Interceptor
public class ExemploInterceptor {
@AroundInvoke
public Object interceptaMetodo(InvocationContext ctx)
throws Exception {
//implementa lógica a ser acrescentada
}
}
ComoosobjetosdocontainerJavaEEsãocriadosporele,nãoénecessárioim-
plementarnenhummétodoqueinsereo interceptornaclasse.U m aformadeligar
uminterceptoremumaclasseéatravésdaanotação @Interceptors,querecebeas
classesdeinterceptorsquedevematuaremumaclassouemummétodo.U m aoutra
formamaissofisticadaéatravésdacriaçãodeanotações quefazemaligaçãoentreos
interceptorseasclassesinterceptadas.Paracriaressaanotaçãodeligação,elaprecisa
seranotadacom @InterceptorBindingedeveseradicionadanaprópriaclasse
dointerceptor.Sendoassim,asclassesemétodosquereceberemessaanotaçãoserão
interceptadas.
U m aoutraformadeinterceptação demétodoséutilizandoaprogramação
orientadaaaspectos. Aorientação aaspectospossuioutrascoisasalémdainter-
114

## Página 121

CasadoCódigo Capítulo4. ProxyDinâmico
ceptação demétodos,porémaquiiremosfocarmaisexclusivamentenessaparte.
Aprincipalimplementação daorientação aaspectosemJavaéo A s p e c t J,oqual
disponibiliza duas diferentesopções de sintaxe, sendo uma delas uma sintaxe
própriaeaoutrabaseadaemanotações. Alistagemaseguirexemplificaasintaxe
baseadaemanotações.
Listagem 4.21- Exemplode aspecto com AspectJ utilizando a sintaxe de ano-
tações:
@Aspect
public class AspectoRegistro{
@Before("execution(* br.casadocodigo.*.*(..))")
public void antes(JoinPoint jp) {
//executa antes
}
@After("execution(* br.casadocodigo.*.*(..))")
public void depois(JoinPoint jp) {
//executa depois
}
@Around("execution(* br.casadocodigo.*.*(..))")
public Object emVolta(ProceedingJoinPoint jp) throws Throwable{
//executa antes
Object returno = jp.proceed();
//executa depois
return returno;
}
}
Asanotações @Before, @Aftere Aroundconfiguramométododoaspecto,
quenessecasoéchamadodeadendoou advice,paraexecutarrespectivamenteantes,
depoisouavoltadométodointerceptado.Cadaanotaçãodessarecebecomoparâ-
metroumaexpressãoquedefineumconjuntodejunção,ou pointcut,quenadamais
équeoconjuntodemétodosqueserãointerceptadosporaqueleadendodoaspecto.
Ograndediferencialdosaspectosemrelação asoutrastécnicaséqueosmétodos
interceptadossãodefinidosnoaspecto,havendoumdesconhecimentodaaplicação
dasuaexistência.Aligaçãodasclassescomosaspectospodeocorrernacompilação,
quandoasclassessãocarregadas,oumesmoemtempodeexecuçãocomousodo
frameworkSpring.Ocapítulo??iráapresentarumaoutrafuncionalidadedoAspectJ
quepodeserutilizadaparaomapeamentodeanotações.
115

## Página 122

4.7.Considerações finais CasadoCódigo
Queromaisumavezdeixarclaroqueessaseçãofoimesmoparaapresentaraexis-
tênciadeoutrasabordagens,queacabamsendoumpoucomaisespecíficas.Nãoéo
objetivoensinarautilizaçãodessastécnicascomonorestantedocapítulo.Acredito
queentendendomelhoressasoutrasimplementações épossívelterumpanorama
geraldecomoessetipodefuncionalidadeéimplementadoemdiferentescontextos.
Assim,sevocêestivertrabalhandocomalgumaplataformaouframeworkquedê
suporteaessetipodefuncionalidade,vaisabermaisfacilmenteosconceitosvistos
nessecapítulopodemserencaixadoslá.
4.7 Considerações finais
Osproxiesdinâmicossãoumrecursopoderosodareflexãoquepodemserutiliza-
dosparaadicionarcomportamentoemclassesexistentes,eaindafazerissodeforma
reutilizávelparaqualquerinterface.Comofoivisto,paraimplementarumproxydi-
nâmiconãoémuitocomplicado,bastandoseguirumareceita.Essecapítuloprocu-
rouexplorardiferentestiposdeproxydinâmico,desdeoquenãoencapsulanenhum
objetoatéoquefazusodemetadadosparadiferenciarosmétodosinterceptados.No
finaldocapítulomostrou-serapidamentealgumasoutrasabordagensparaainter-
ceptaçãodemétodos.
Essecapítulofinalizaaprimeirapartedolivroondeosconceitosbásicosdere-
flexãoedousodemetadadossãoapresentados.Nessesprimeiroscapítulostambém
foramapresentadasasAPIsbásicasquesãoutilizadasemJavaparaautilizaçãodes-
sesconceitos.Chegandonesseponto,esperoqueosleitoresjáestejamfamiliaresao
usodareflexãoejáconsigamdarsuasprimeiraspinceladasemcomponentesque
autilizam.Prepare-sequenapróximapartedesselivrovocêvaiaprenderoquese
precisaparafazerumaobraprima...
116

## Página 123

P a r t eII
B o a sP r á t i c a s
NoscapítulosanterioresdolivroforamabordadasasAPIserecursosdalingua-
gemquepodemserempregadosparaousodereflexãodalinguagemJava.Porém,se
suaintençãoérealmentecriarumcomponenteouframeworkreutilizávelcomrefle-
xãoemetadados,conhecerasclassesemétodosqueserãoutilizadosésóocomeço.
FaçoumparalelodequandoseaprendeherançaepolimorfismoemJava,poissaber
somenteissonãoésuficienteparacriarumbomdesignorientadoaobjetos.
Essapartedolivroapresentaboaspráticasquepodemserutilizadasnodesen-
volvimentodessetipodecomponente. Ospróximoscapítulos,compilamdeuma
formafluidaedidática,algumaspráticasdescobertascomopartedapesquisaque
realizeievenhorealizando.Essapesquisaenvolvenãosomenteaanálisedaspráti-
casutilizadasemdiversosframeworksexistentes,comotambémsuautilizaçãono
desenvolvimentodenovosframeworksparaconfirmaraadequabilidadedaaplica-
çãodecadaumadelas.

## Página 125

Capítulo5
TestandoclassesqueusamReflexão
“ Umdesenvolvedor como eu se importa com escrever código novo e fazê-loo mais
interessante e eficiente possível. M a sm u i t opoucas pessoas querem fazer os testes. ”
–LinusTorvalds
Comofoiditoanteriormente,existemvárioserrosquesãopegosjáemtempode
compilaçãoquequandolidamoscomreflexãopodemaconteceremtempodeexe-
cução. Sendoassim,pelosprópriosexemplosqueforammostradosnoscapítulos
anteriores,épossívelperceberqueseaclasseoumétodonãopossuiaestruturaes-
peradapelocomponente,muitascoisaspodemdarerrado. Porexemplo,pode-se
tentarinstanciarumaclassecomumconstrutorqueelanãopossuiouinvocarum
métodocomaquantidadeerradadeparâmetro.Asclassesdesenvolvidascomrefle-
xãodevemestarpreparadasparalidarcomqualquertipodeclasse,eexistemmuitas
coisaspossíveisdeacontecer.U m apremissaerradaoualgumaestruturainesperada,
podecausarumbugsérionaaplicaçãoqueutilizaocomponente.
Ofatodeumcomponenteouclassequeutilizereflexãopoderserreutilizadoem
diferentescontextosdentrodeumaaplicação,apesardeserumacoisamuitoboa,

## Página 126

CasadoCódigo
aumentaapreocupaçãocomaqualidadedessecódigo.Muitasvezes,mesmoquea
classejátenhasidoreutilizadaváriasvezes,umasituaçãodistintaaindapodecausar
erros. Alémdisso,éprecisonão somentequeocomponentequeutilizareflexão
estejacorreto,comotambémqueaclassedaaplicaçãotenhaaestruturaadequadae
possuaosmetadadosconfiguradosdeformaagerarocomportamentodesejado.
Dessaforma,essecapítulosededicaaabordarquestões relativasaotestedeclas-
sesecomponentesqueutilizamreflexão,abordandotambémotestedasaplicações
queutilizamessescomponentes.V o uconsiderarqueosleitoresestejamfamiliariza-
doscomosconceitosdetestesautomatizadosecomocriá-loscomoJUnit4(paraos
quenãoconhecem,leiamoquadro).Porém,sevocêestálendoumlivroavançadode
programaçãocomoesseenãosabecriartestesdeunidadeainda,achoquevocêestá
emapuros!Sugirofortementequecorraatrásdesseconhecimento,porémacredito
quecomumconhecimentobásicodeJUnitépossívelacompanharolivro.
120

## Página 127

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
JUnit 4 em menos de u m minuto!
ParacriartestesdeunidadecomoJUnit4,oprimeiropassoéadici-
onarsuabibliotecanoclasspath. Paraimplementarostestes,crieuma
classecomumeadicionemétodosquerealizamostestes.Paraserconsi-
deradoumteste,ométodoprecisaseranotadocom @Test.Cadateste
deveprepararocenáriodoteste,executarafuncionalidadequedeseja-se
testarocomportamentoeverificarseocomportamentofoioesperado.
Paraverificarocomportamento,aclasse Assertpossuidiversosméto-
dosestáticosquepermitemfazercomparações entrevalores.Alistagem
aseguirmostraumexemplosimplesdeclassedeteste.
Listagem 5.1-ExemplosimplesdefuncionamentodoJUnit:
public class ClassDeTeste {
@Test
public void metodoDeTeste() {
ClassTestada testada = new ClassTestada();
String resultado = testada.metodoTestado();
assertEquals("valor esperado",resultado);
}
}
OJUnitpossuiumgrandesuportedetodososIDEsexistentes,ondepara
rodarumaclassedetestes,bastaclicarnelaesolicitarsuaexecução.Isso
éosuficienteparaacompanharosexemplos! Casoalgodiferenteseja
utilizado,aprópriaseçãoiráexplicarofuncionamento.
Paramostrarcomofazerostestesautomatizadosdessetipodeclasse,essecapí-
tulovaifocarmuitoemexemplos.Nocaso,vamospegarclassesdesenvolvidasnos
capítulosanterioresemostrarcomopoderiaserfeitootesteparaelas.Osexemplos
escolhidospossuemcaracterísticasdistintas,justamenteparamostraradiversidade
desituações quesepodeencontraraosetestaressetipodecomponentedesoftware.
121

## Página 128

5.1.Variandoestruturadaclasseparateste CasadoCódigo
5.1 Variando estrutura d aclasse para teste
Quandotemosumaclasseoucomponentebaseadoemreflexãoemetadados,nor-
malmenteoseucomportamentovaidependerdaclassepassadacomoparâmetro.
Sendoassim,paratestá-loséprecisopassarclassescomdiferentesestruturascomo
parâmetro.Dessaforma,ocenáriodecadatestevaienvolveracriaçãodeumanova
classe,equandocabívelvaicriarumobjetodessaclasse.Aaçãoquedefineafun-
cionalidadequeserádefinidanessetesteenvolveainvocação docomponenteque
utilizareflexão.Porfim,averificaçãoiráchecarseocomportamentofoioesperado,
oquepodeenvolveraverificaçãodovalordeumretorno,doestadodeumobjeto,
oumesmoseumdeterminadométodofoiinvocado.
Paracomeçar,vamosimplementarostestesautomatizadosdogeradordemapas
apresentadonaseção 1.3. Paraessecomponente,otestemaissimplesseriagerar
o mapade propriedadesde um JavaBean simples, comalgumas propriedades
e sem anotações. A próxima listagem mostra como esse primeiro teste seria
implementado. Inicialmente,definimosaclasse B e a nqueseráconsumidapela
classedegeração demapas. Observequeelapossuidoisatributoscommétodos
deacessogettersesetters. Emseguidaécriadaumainstânciadessaclasse, as
suas propriedadessão configuradase, por fim, o objeto épassado ao método
gerarMapa(). Paraverificarseocomportamentofoicorreto,são inseridassuas
asserções queverificamseomaparetornadopossuiaspropriedadesesperadas.
Listagem 5.2-T e s t edafuncionalidadebásicadogeradordemapas:
public class TesteGeradorMapa {
@Test
public void mapaDeClasseSimples() {
class Bean{
private String prop1;
private int prop2;
public String getProp1() {
return prop1;
}
public void setProp1(String prop1) {
this.prop1 = prop1;
}
public int getProp2() {
return prop2;
122

## Página 129

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
}
public void setProp2(int prop2) {
this.prop2 = prop2;
}
}
Bean b = new Bean();
b.setProp1("teste");
b.setProp2(25);
Map<String,Object> mapa = GeradorMapa.gerarMapa(b);
assertEquals("teste",mapa.get("prop1"));
assertEquals(25,mapa.get("prop2"));
}
}
Comofoidescrito,éprecisodefinirumaclasseparaarealizaçãodaverificação.
Noexemplomostrado,elaécriadadentrodoprópriométododeteste,sendoválida
suautilização somentedentrodeseuescopo. Asprincipaisvantagensdessaabor-
dageméqueaclassedefinidaficapróximaaoseuuso,equeomesmonomepode
serutilizadoemoutrosmétodossemhaverconflito.Porém,essaéumadaspossi-
bilidades,eelapodeserdefinidaemoutrosescopos,comoforadométodoouem
seupróprioarquivo.U m aclassedefinidaemumcontextomaisamplopodeseruti-
lizadaemmaismétodosdetestes,masporoutrolado,adefiniçãodentrodomesmo
arquivoaumentaalegibilidadedocódigotornandomaisfácildeverocenárioque
estásendodefinido.Sendoassim,éprecisopesaressasquestõesparaverqualolocal
maisadequadoparasuadefinição.
Continuandoadefinição dostestes,apróximalistagemverificaautilização
da anotação @Ignorar. A diferença na definição da classe Bean para esse
testeestánaadição daanotação @Ignorarnométodo getProp1(). Observe
queacriação doobjetoeadefinição dapropriedadesão iguaisàsdométodo
anterior.Nasasserções, éverificadoseomapanãopossuiachave "prop1"através
dométodoassertFalse(),eaoutraverificaçãoéamesmaquejáhavíamosfeito.
Listagem 5.3-Testandoousodeanotação@Ignorar:
@Test
public void ignoraPropriedade() {
class Bean{
123

## Página 130

5.1.Variandoestruturadaclasseparateste CasadoCódigo
private String prop1;
private int prop2;
@Ignorar
public String getProp1() {
return prop1;
}
public void setProp1(String prop1) {
this.prop1 = prop1;
}
public int getProp2() {
return prop2;
}
public void setProp2(int prop2) {
this.prop2 = prop2;
}
}
Bean b = new Bean();
b.setProp1("teste");
b.setProp2(25);
Map<String,Object> mapa = GeradorMapa.gerarMapa(b);
assertFalse(mapa.containsKey("prop1"));
assertEquals(25,mapa.get("prop2"));
}
Porfim,otesteseguinteapresentadonapróximalistagemexercitaocasoem
queaanotação @NomePropriedadeéutilizadaparamudaronomedachave
usadanomapa.Observeque,nessecaso,asasserções verificamseexisteaentrada
nomapacomonomeconfiguradonaanotaçãoesenãoexisteachavecomonome
doatributo.
Listagem 5.4-Testandoamudançadenomedapropriedadedomapa:
@Test
public void mudaNomePropriedade() {
class Bean{
private String prop1;
private int prop2;
public String getProp1() {
return prop1;
124

## Página 131

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
}
public void setProp1(String prop1) {
this.prop1 = prop1;
}
@NomePropriedade("propriedade2")
public int getProp2() {
return prop2;
}
public void setProp2(int prop2) {
this.prop2 = prop2;
}
}
Bean b = new Bean();
b.setProp1("teste");
b.setProp2(25);
Map<String,Object> mapa = GeradorMapa.gerarMapa(b);
assertEquals("teste",mapa.get("prop1"));
assertEquals(25,mapa.get("propriedade2"));
assertFalse(mapa.containsKey("prop2"));
}
Esseexemplodemonstraoprocessobásicodesetestarumaclassequeutiliza
reflexão. Comofoimostradonoexemplodessestrêstestes,acriaçãodoobjetoea
invocaçãodosmétodosacabamsendoasmesmas,eoquemudanoprocessodeteste
éaestruturadaclassepassadacomoparâmetro.Aideiaéutilizarumaclassecomo
baseeirmodificandoaestruturadeformaamudarocomportamentoesperado.
Verificandochamadas de método
U mtipodefuncionalidadefrequentementefeitaporclassesqueutilizamrefle-
xãoenvolveainvocaçãodemétodosemclassesqueelasóreconheceemtempode
execução.Sendoassim,umtestequeprecisaráserfeitoparavalidaressetipodefun-
cionalidadeenvolve,comopartedaverificação,assegurarqueosmétodoscorretos
foraminvocados.Issoimplicanãosomenteverificarainvocaçãodosmétodoscertos,
mastambémsecertificarqueoutrosmétodosnãoforaminvocados.
Aqui, utilizaremos como exemplo o validador de objetos apresentado da
seção 2.4. U m adasfuncionalidadesdessaclasseenvolveainvocação demétodos
começadoscom "validar" equenão recebamparâmetros. Sendo assim, a
próximalistagemmostradoistestesparaverificaressafuncionalidade. Observe
125

## Página 132

5.1.Variandoestruturadaclasseparateste CasadoCódigo
queoprimeirotesteverificaseométodocorretoéinvocado,eosegundoverifica
sesomentemétodosqueobedecemaosrequisitossãoinvocados.Paraverificarsea
invocaçãoéfeitaounão,écriadaumavariávelbooleananaclasseparateste,queé
alteradanomomentoqueométodoéinvocado.Sendoassim,vendoovalordessa
variávelconseguimosverseométodofoiinvocadoounão.
Listagem 5.5-Testandoainvocaçãodemétodosnovalidador:
public class TesteValidador {
@Test
public void testInvocaMetodo() throws ValidacaoException {
class ParaValidar{
public boolean invocou = false;
public void validarInformacao(){
invocou = true;
}
}
ValidadorObjetos v = new ValidadorObjetos();
ParaValidar pv = new ParaValidar();
v.validarObjeto(pv);
assertTrue(pv.invocou);
}
@Test
public void naoInvocaMetodo() throws ValidacaoException {
class ParaValidar{
public boolean invocouA = false;
public boolean invocouB = false;
public void validarParamErrado(String s){
invocouA = true;
}
public void nomeErrado(String s){
invocouB = true;
}
}
ValidadorObjetos v = new ValidadorObjetos();
ParaValidar pv = new ParaValidar();
v.validarObjeto(pv);
assertFalse(pv.invocouA);
assertFalse(pv.invocouB);
}
126

## Página 133

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
}
U m aoutrafuncionalidadedaclasse ValidadorObjetosenvolveainvocação
deatributoscujotipoimplementeainterface Validador.Nessecaso,aideiaéa
mesmadotestemostradoanteriormente,porémcomoainvocaçãoéfeitanoobjeto
queestánoatributo,omecanismodeveseradicionadonesseobjeto,enãonaclasse
queestásendocriada. Alistagemaseguirmostraaimplementaçãodotestedessa
funcionalidade.
Observe queaclasse ValidadorTeste écriada parasimularumaclasse
que implementaa interface Validador e possui um atributobooleano para
verificarseométodofoiinvocadoounão.Emseguida,dentrodométododeteste,é
criadaumaclassecomtrêsatributos,dostipos ValidadorTeste, Validadore
Object,sendoquetodosrecebemumainstânciade ValidadorTeste.Segundo
osrequisitos,paraserinvocado,otipodoatributodeveimplementarainterface
Validador,oqueérefletidopelasasserções, ondesomenteoatributodotipo
Objectnãodeveserinvocado.
Listagem 5.6-T e s t edainvocaçãodeatributosdotipoValidador:
//Declaração fora da classe
public class ValidadorTeste implements Validador {
public boolean invocou;
public void validar(Object o) throws Exception {
invocou = true;
}
}
//método de teste
@Test
public void invocaAtributos() throws ValidacaoException {
class ParaValidar{
public ValidadorTeste v1 = new ValidadorTeste();
public Validador v2 = new ValidadorTeste();
public Object v3 = new ValidadorTeste();
}
ValidadorObjetos v = new ValidadorObjetos();
ParaValidar pv = new ParaValidar();
v.validarObjeto(pv);
assertTrue(pv.v1.invocou);
assertTrue(((ValidadorTeste)pv.v2).invocou);
127

## Página 134

5.1.Variandoestruturadaclasseparateste CasadoCódigo
assertFalse(((ValidadorTeste)pv.v3).invocou);
}
Posso utilizar mock objects nesse tipo de teste?
Sevocêéumdesenvolvedorqueéfamiliarcomacriaçãodetestes,talvezdeva
estarseperguntandoseessacriaçãodeclassesmostradanaslistagensanterioresnão
seriaomesmoquecriarum mock o b j e c t. U mmockobjectéumobjetoqueécri-
adoparasimularumadependênciadaqueestásendoclassetestada.Essasimulação
envolvedarasrespostasparasimulardiferentescenáriosdetesteeverificarseasin-
vocações demétodoforamfeitasdeacordocomasesperadas. Emumaclasseque
nãoutilizareflexão,adependênciapossuiumcontratoesperado,determinadopor
umaclasseouumainterface.Sendoassim,omockobjectimplementaessemesmo
contratodeformaapodersubstituiressadependência.
Nocasodotestedeclassesqueutilizamreflexão,oobjetoutilizadocomode-
pendêncianãopossuiumainterfacedefinida.Sendoassim,nessecasooqueprecisa
serfeitoemcadacasodetesteéadefinição declassescomestruturasdiferentes,
enãocomportamentosdiferentesparaamesmaestrutura. A p e s a rdeissonãoser
umtermotãousual,umartigocientíficodefiniuessetipodeclassecriadaparateste
como mock c l a s s[1].Sendoassim,omockobjectserefereàsimulaçãodecomporta-
mentoparaadependênciadaclassetestadaemockclass,àsimulaçãodeestruturas
diferentesdeclassesparateste. Decertaforma,épossívelcriarummockobject
deummockclass,poisdiferentestestespodemusarumamesmaestruturadeclasse
mascomdiferentescomportamentos.Issoécomumquandoamockclassrepresenta
umainterfaceeomockobjectéumaimplementaçãodela.
Nosexemplosmostrados,cadatestecriavasuamockclassjácomocompor-
tamentoesperadoparaoteste. Muitasvezes,comoumanovaclasseprecisaráser
definidadequalquerforma,émaisfáciljádefini-lafazendoonecessárioparage-
rarocenáriodoteste.Omelhorexemplodemockobjectnostestesjáapresentados
nessecapítulofoiaclasse ValidadorTeste,pois,nessecaso,ainterfaceesperada
éfixa,pormaisqueosatributossejamlidosporreflexão.
Nocasodosmockobjects,umaalternativaàimplementaçãomanualdenovas
classesparaasimulaçãodecomportamentosãoosframeworksdecriaçãodemocks.
Essesframeworksnormalmenteutilizamproxiesdinâmicosparagerarocomporta-
mentoesperadopelaclasseeverificarseaschamadasrealizadasforamasesperadas.
ExemplosdeframeworksJavaqueimplementamessetipodefuncionalidadesãoo
JMock,o EasyMockeo Mockito.Avantagememutilizaressetipodeframework
128

## Página 135

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
estáemnãonecessitarcriardiversasclassesparasimulardiferentescomportamen-
tosparaostestes,permitindoqueadefiniçãodocomportamentoeverificações do
mocksejamfeitosnoprópriométododeteste.
OsexemplosdesselivroirãoutilizaroJMockparamostrarautilizaçãodessetipo
deframeworkemtestesdeclassequeutilizamreflexão,porémestáforadoescopo
desselivroexplicarofuncionamentodesseframework.
129

## Página 136

5.1.Variandoestruturadaclasseparateste CasadoCódigo
JMo c kem menos de cincominutos!
ParautilizaroJMock,aclassedetestedevepossuiralgumatributo
quetenhaumtipoderivadodaclasse Mockery,queseráutilizadona
criaçãodosmocks. Emversões maisantigasdoJUnit,aclassedeteste
eraanotadacom @RunWith(JMock.class)paraqueasverificações
dosmocksrodassemdepoisdométododeteste. Emversões maisno-
vasbastacriarumatributodotipo JUnitRuleMockeryeoanotar
com @Rule. Paracriaromockdeumainterfacebastautilizaromé-
todo mock()passandoo Classcorrespondente,sendoqueseforcriar
maisdeummockdamesmaclasseprecisapassarumparâmetroadicio-
nalcomuma Stringquenomeiaainstânciadomock.
Para definir as expectativas e comportamento do mock, a cha-
mada checking(new Expectations(){{ ... }}) éutilizada,
sendoquetodasasdefinições são feitasnolugardostrêspontos. O
JMockutilizaumaDSLinternaparadefiniraschamadasesperadase
seucomportamento,incluindoonúmerodeinvocações, ordemdeinvo-
cação,parâmetrosesperadoseoresultadodainvocação,comoretorno
oulançamentodeexceção. Asexpectativasutilizadasemcadaexem-
plodolivroserão explicadascomdetalhe,possibilitandoquemesmo
quemnãoconheçaoframeworkpossaacompanhá-los.Nositedopro-
jetoJMock,existeumresumodesuasintaxeemuma c h e a tsheetnoen-
dereçohttp://jmock.org/cheat-sheet.html.Alistagemaseguirmostraa
estruturabásicadeusodoJMock.
Listagem 5.7-ExemplodeusodoJMock:
public class TesteComJMock {
@Rule
public JUnitRuleMockery ctx = new JUnitRuleMockery();
@Test
public void testeComMock() throws Exception {
ClasseMock mock= ctx.mock(ClasseMock.class);
ClasseTestada c = new ClasseTestada();
c.setClasseMock(mock);
ctx.checking(new Expectations() {{
//expectativas do mock
//retornos dados pelo mock
}});
c.metodoTestado();
}
}
130

## Página 137

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
Paravermoscomootesteusandomockobjectpodeserfeitosimulandoos
objetosdainterface Validador,apróximalistagemmostracomooframework
JMockpoderiaserutilizado.Paraqueosmockspossamsercriadosesuasexpecta-
tivasverificasnofinaldecadateste,aclassedetestedeveterumatributodotipo
JUnitRuleMockeryanotadacom @Rule. Nométododeteste,observequea
mockclass ParaValidarécriadarecebendomockobjectsemseusdoisatributos,
apartirdachamadadométodo mock()daclassdoJMock. Emseguida, são
definidasasexpectativas:ométodo validar()doatributodetipo Validador
deveserinvocadoumavezeométodo validar()doatributodetipo Object
nãodeveserinvocado.
Listagem 5.8- U s ode framework de mock para criação de teste com Valida-
dor:
public class TesteValidador {
@Rule public JUnitRuleMockery ctx = new JUnitRuleMockery();
@Test
public void invocaAtributosJMock() throws Exception {
class ParaValidar{
public Validador v1 = ctx.mock(Validador.class, "v1");
public Object v2 = ctx.mock(Validador.class, "v2");
}
ValidadorObjetos v = new ValidadorObjetos();
final ParaValidar pv = new ParaValidar();
ctx.checking(new Expectations() {{
oneOf (pv.v1).validar(pv);
never (((Validador)pv.v2)).validar(pv);
}});
v.validarObjeto(pv);
}
}
131

## Página 138

5.1.Variandoestruturadaclasseparateste CasadoCódigo
Lidando com testes q u eenvolvem exceçõ e s
Asexceções são umtipoderetornoqueumainvocação demétodopodedar
comoresultado,significandoaexistênciadealgumtipodeerronaexecuçãodafun-
cionalidade.Aexceçãolançadapodeindicarumasituaçãoemqueafuncionalidade
nãopodeserexecutada,masquefazpartedeumcenáriocomumdenegócio.Exem-
plossãoinformações inválidasfornecidaspelousuário,umaautenticaçãofalhaou
atentativadeacessoaumafuncionalidadeàqualousuárionão éautorizado. A
ocorrênciadessasexceções não significaqueexisteumerronosoftware,masque
umaexecução dafuncionalidadenãopodesercompletadadevidoaumasituação
excepcionalprevista.
Outrotipodeexceçãoéaquelequeindicaqueosoftwarenãoestáfuncionando
corretamentedevidoaumproblemainterno,querepresentaumerroouumbug.
Muitasclassesecomponentespossuemumaabordagemdefensiva,naqualnãocon-
fiamemoutrasclasseseverificamseaschamadasestãosendofeitasdaformacorreta.
Nessecaso,olançamentodeumaexceçãosignificaqueousodaquelaclassenãoestá
sendofeitodaformacorreta.Nessecaso,éimportantequeamensagemdeerroseja
bemdescritivaparapossibilitarqueodesenvolvedordetecteafalhaepossacorrigi-
la.Emcasodeclassesqueutilizamreflexão,essetipodeverificaçãoémuitoimpor-
tantepoisaclasserecebidacomoparâmetropodepossuirumaestruturainadequada
ouerrosnaconfiguraçãodemetadados.
Paraexemplificaroprimeirotipodeexceção,serãoutilizadososprópriostestes
daclasse ValidadorObjetos(). Comofoimostradoemseudesenvolvimento,
essaclassedevepegarasexceções lançadaspelosmétodoseclassesdevalidação,
encapsulando-asemumalistaqueélançadaemuma ValidaçãoException.A
listagemaseguirmostraumtestequesimulaumcenárioemqueumaexceção é
lançadadeummétododevalidação, chamado validarInformacao(),euma
implementação de Validator da qual écriado um mock como framework
JMock.Observequeparafazeromocklançaraexceção,nasexpectativaséutilizada
achamada will(throwException(...)).
Listagem 5.9-Verificandoinformações dasexceções recebidas:
@Test
public void capturaExcecoes() throws Exception {
class ParaValidar{
public Validador v = ctx.mock(Validador.class);
132

## Página 139

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
public void validarInformacao() throws Exception{
throw new Exception("mensagem A");
}
}
ValidadorObjetos v = new ValidadorObjetos();
final ParaValidar pv = new ParaValidar();
ctx.checking(new Expectations() {{
oneOf (pv.v).validar(pv);
will(throwException(new Exception("mensagem B")));
}});
try {
v.validarObjeto(pv);
fail();
} catch (ValidacaoException e) {
List<Exception> erros = e.getErros();
assertEquals("mensagem A", erros.get(0).getMessage());
assertEquals("mensagem B", erros.get(1).getMessage());
}
}
Nessecaso,comoexistemverificações paraseremfeitasnaexceçãolançada,o
método validarObjeto()precisaserenvoltoemumbloco try. Comoées-
peradoqueumaexceção sejalançada,ométodo fail()éinvocadologoapósa
chamadade validarObjeto(),poisseelanão forlançadaotestedevefalhar.
Dentrodobloco catch,alistadeexceções érecuperadaeéverificado,atravésda
mensagemdeerro,seasexceções lançadaspelométododaclasseepelomockestão
nalista.
Comoexemplodetestedeexceções quesãolançadasporumaestruturainade-
quadadaclasse,serãoutilizadostestesda MapeamentoParametrosapresentada
naseção3.5.Esseexemplofoiescolhidoporqueforamfeitasváriasverificações no
formatodaclasse,lançandoexceções quandoasuaestruturanão condiziacomo
queeraesperado.Nalistagemaseguirmostraoexemplodedoistestesquefazem
essaverificação. Oprimeiroverificaocasoemqueotipodapropriedadeseja
inteiro,sendoqueoesperadoésomente String,eosegundoexploraocasodeo
métodosetterreceberdoisparâmetros.
133

## Página 140

5.1.Variandoestruturadaclasseparateste CasadoCódigo
Listagem 5.10- Exemplo de testes que verificam classes com estrutura inade-
quada:
public class TesteMapeamentoParametros {
@Test(expected=MapeamentoException.class)
public void testTipoErrado() {
class Param{
@Parametro("-i")
private int info;
public int getInfo() {
return info;
}
public void setInfo(int info) {
this.info = info;
}
}
String[] a = {"-i","23"};
MapeamentoParametros<Param> map =
new MapeamentoParametros<>(Param.class);
Param p = map.mapear(a);
}
@Test(expected=MapeamentoException.class)
public void testQuantidadeParamErrado() {
class Param{
@Parametro("-i")
private String[] info;
public String[] getInfo() {
return info;
}
public void setInfo(String infoA, String infoB) {
this.info = new String[]{infoA, infoB};
}
}
String[] a = {"-i","textoA","textoB"};
MapeamentoParametros<Param> map =
134

## Página 141

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
new MapeamentoParametros<>(Param.class);
Param p = map.mapear(a);
}
}
Nessecaso,não existenenhumaverificação adicionalqueprecisaserfeitaem
relaçãoàsinformações daexceçãolançadapelométodo mapear().Sendoassim,
podeserutilizadooparâmetro expecteddaanotação @Test.Nele,deveserpas-
sadaaclassedaexceçãoqueseesperaquesejalançada.Dessaforma,otestesóirá
passarcasoaexceçãosejalançadadentrodométododeteste.U m aressalvaemre-
laçãoaousodoatributo expectedéqueotesteirápassarseaexceçãoforlançada
emqualquerpontodométododeteste.Portanto,recomenda-seutilizaressaabor-
dagemapenasnocasodeaexceçãopoderserlançadaemapenasumadaschamadas
demétododoteste.
Finalizoessaseção ressaltandoaimportânciadarealização dessetipodeteste
paraclassesqueutilizamreflexão. Éimportanteverificarcomoocomponenteestá
lidandocomdiferentesestruturasdeclasse,sejafazendoalgumtratamentoespecial,
oulançandoumaexceção informativadizendoomotivodeaquelaclassenão ser
aceita.Quandoaclasseprecisarlidarcomtipos,testesenvolvendotiposprimitivos
earrayssãosempreimportantesdeseremincluídos,poiselesnamaioriadasvezes
requeremumtratamentoespecial.Acriaçãodetestesautomatizadosqueabrangem
diversoscenáriosdiferenteséprimordialparaaumentaraqualidadedaimplementa-
ção,oqueéespecialmenteimportanteseelaforreutilizadaemdiferentescontextos.
Para que complicar se o teste podese r simples?
Osexemplosapresentadosparaostestesatéomomentonesselivro
possuemaestruturamaisbásicapossívelparaexercitarafuncionalidade
desejada.Podeparecerqueissoestásendofeitoparamanteraslistagens
pequenasouparapodersermaisdidáticos,porémnaverdadeéumaboa
práticaqueostestessejamsimpleseobjetivosdentrodafuncionalidade
queestásendoexercitada.Dessaforma,porquecriarumJavaBeancom
diversaspropriedades,seduasjásão osuficiente? Oidealé,aprincí-
pio,mantercadatestesimplesefocadoemapenasumafuncionalidade,
eposteriormentecriarumtestemaiscomplexoqueenvolveaexecução
dediversasfuncionalidadescombinadas.
135

## Página 142

5.2.T e s t edeproxiesdinâmicos CasadoCódigo
5.2 Teste de proxiesdinâmicos
U moutrotipodetesteimportantequandotrabalhamoscomreflexãoéotestede
proxiesdinâmicos.Adificuldadedetestedoproxydinâmicoestáemsuaprópria
naturezadeencapsularumoutroobjeto. Sendoassim,umaimportantepartedo
testeenvolveainvocação demétodosnesseobjetoencapsulado. Dessemodo,de-
pendendodafuncionalidadedoproxy,éimportanteverquaisequantaschamadas
foramrealizadas,quaisparâmetrosforampassadosàclasseencapsuladaemesmo
simulardiferentescenáriosquandoelaretornardiferentesvaloreselançarexceções.
V a l eressaltarque,comooproxyédinâmico,eleprecisaestarpreparadopara
lidarcomdiferentestiposdeclasse.Portanto,devemosconsiderarqueosmétodos
quevão serrecebidospeloproxypodempossuirqualquertipodeestrutura,com
diferentesquantidadesetiposdeparâmetrosediferentestiposderetorno.Casovocê
decidanãodarsuporteadeterminadostiposdemétodoéimportanteverificarisso
elançarumerroseainterfacepossuirummétodoemumformatonãoaceito.
Aestratégiabásicaparaotestedeumproxydinâmicoécriarumainterfaceque
captureumacaracterísticaquesequeiratestarecriarummockobjectdessainter-
face.Emseguida,criaroproxyencapsulandoomockeutilizá-loparaasverificações
relacionadasàsinvocações demétododoproxynoobjetoencapsulado.
Para exemplificar esse tipo de teste, essa seção apresenta testes da classe
CacheProxymostradanaseção 4.5. Nessecaso,omockiráajudaraverificaras
situações emqueoobjetoencapsuladoéinvocadoeoscasosemqueoresultado
éobtidodocachearmazenadopeloproxy.Parainiciaroteste,alistagemaseguir
apresentaainterface CacheMe,queiráservircomoamockclassparaostestes
criados.
Listagem 5.11-Verificandoinformações dasexceções recebidas:
public interface CacheMe{
@Cache int metodoComCache(int param);
@InvalidaCache void anulaCache();
}
Oprimeiroteste,implementadonométodo cacheSimples()dapróxima
listagem,verificaseoproxyarmazenaeretornaovalordocachecorretamente
parachamadasdemétodoscomdiferentesparâmetros. Asexpectativasdomock
objectéque metodoComCache()sejainvocadoumavezcomoparâmetro 1
eumavezcomoparâmetro 2, sendoqueelevairetornarrespectivamenteos
136

## Página 143

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
valores 10 e 20. Comoação doteste, ométodo metodoComCache() será
invocadoduasvezescomcada parâmetroeprecisareceberosvalorescorretos
comoretorno.Dessaforma,seráverificadoseométododomockobjectfoiinvo-
cadosomentenaprimeiravez,eseocachearmazenadofoiretornadocorretamente.
Listagem 5.12-Verificandoinformações dasexceções recebidas:
public class TesteCacheProxy {
@Rule public JUnitRuleMockery ctx = new JUnitRuleMockery();
@Test
public void cacheSimples() {
final CacheMe mock = ctx.mock(CacheMe.class);
CacheMe proxy = (CacheMe) CacheProxy.criar(mock);
ctx.checking(new Expectations() {{
oneOf (mock).metodoComCache(1);
will(returnValue(10));
oneOf (mock).metodoComCache(2);
will(returnValue(20));
}});
assertEquals(10, proxy.metodoComCache(1));
assertEquals(20, proxy.metodoComCache(2));
assertEquals(10, proxy.metodoComCache(1));
assertEquals(20, proxy.metodoComCache(2));
}
}
Osegundométododetesteverificaainvocação deummétodoqueanulao
cachearmazenadopeloproxyeestáapresentadonalistagemaseguir. Dessavez,
iremosinvocarométodometodoComCache()duasvezes,eemseguida,ométodo
anulaCache()eporfim,ométodo metodoComCache()maisduasvezes. A
expectativaéque metodoComCache(0)sejainvocadoapenasduasvezesnomock
object,retornandoovalor 10naprimeiravezeovalor 20dasegundavez,isso
alémdachamadadométodo anulaCache().Observequeexistemasserções que
verificamseasduasprimeiraschamadasretornam 10eseasduasúltimasretornam
20.Essetesteverificaseocacheélimpodepoisdachamadadeummétodoanotado
com @InvalidaCache.
137

## Página 144

5.3.Testandoaconfiguraçãodemetadados CasadoCódigo
Listagem 5.13-Verificandoinformações dasexceções recebidas:
@Test
public void invalidaCache() {
final CacheMe mock = ctx.mock(CacheMe.class);
CacheMe proxy = (CacheMe) CacheProxy.criar(mock);
ctx.checking(new Expectations() {{
exactly(2).of(mock).metodoComCache(1);
will(onConsecutiveCalls(returnValue(10),returnValue(20)));
oneOf(mock).anulaCache();
}});
assertEquals(10, proxy.metodoComCache(1));
assertEquals(10, proxy.metodoComCache(1));
proxy.anulaCache();
assertEquals(20, proxy.metodoComCache(1));
assertEquals(20, proxy.metodoComCache(1));
}
Éimportanteficarclaroqueessesdoistestesapenasilustramaabordagemparao
testedeumproxydinâmico.Emumasuitedetestesmaiscompletaparaesseproxy,
seriamtestadoscenáriosmaiscomplexos,comoumainterfacequepossuimétodos
comomesmonome,métodoscomváriosparâmetros,métodoscomquantidadeva-
riáveldeparâmetros,retornoeparâmetroscomobjetoscomplexos,entreoutros.Por
exemplo,imaginedoismétodoscommesmonomequerecebemrespectivamente
umedoisinteiroscomoparâmetro,seráqueoproxyusariaovalordoretornoda
chamadacomparâmetros (1,1)paraachamadacom (11)?Deixocomoexer-
cícioparaoleitorimplementaresseteste,ecorrigiraimplementação doproxyse
necessário.
5.3 Testando a configuração de metadados
Asseções anterioresdessecapítuloabordaramacriaçãodetestesqueverificamos
componentesouclassesqueutilizavamreflexãoemetadados.Porém,quemgarante
queessecomponentevaisecomportarconformeodesejadoparaumdeterminada
classe?Porexemplo,sevocêquerqueosparâmetrosdasuaaplicaçãosejammape-
adosparaumaclasse,éprecisosaberseissoestásendofeitodaformacorreta.Da
138

## Página 145

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
mesmaforma,sevocêdesejaqueocachesejafeitoparaumadeterminadaclasseuti-
lizandoaclasse CacheProxy,éprecisoverificarseparaaestruturacriadaparaa
classeeasanotações configuradasrefletemessecomportamento.
Quandoestamosutilizandoumcomponentequeutilizareflexãoemetadados,
aprópriaestruturadaclasseeosmetadadosvãodeterminaroseucomportamento
quandoessaclasseouumdeseusobjetosforempassadoscomoparâmetro.Pormais
quepareçaestranhotestarmosalgodeclarativo,éimportantesaberseosmetadados
estãodeclaradosdeformaagerarocomportamentoadequado.Enquantoostestes
daclasseoudocomponentesãofeitospelosseusdesenvolvedores,essetipodeteste
dosmetadadosdeveserfeitoporquemoestáutilizando.
C o m otestar o comportamento gerado p e l o smetadados
Paracriarmosumtestequeverifiqueseosmetadadosestãoconfiguradoscorre-
tamente,deveserchecadoocomportamentodaclassequeutilizareflexãoaoreceber
umadeterminadaclassedaaplicação.Otesteébemparecidocomosqueforammos-
tradosnasseções anteriores,comadiferençaquenãoseráutilizadaumamockclass
esimumaclasserealdaaplicação. Oobjetivotambémédiferente,poisnãoquere-
mosverificarseaclassequeutilizareflexãofuncionacorretamentequandorecebe
umaclassecomumadeterminadaestruturaeanotações; massim,assumindoque
ocomponentefoitestadoefuncionacorretamente,deseja-severificarquaissão a
estruturaeanotações queaclasseprecisariaterparaseobterumdeterminadocom-
portamento.
Imaginequeemminhaaplicação,eupreciserecebercomoparâmetrosnalinha
decomandoumalistadearquivosdeentradaeapenasumarquivodesaída.Para
facilitaraimplementaçãodaleituradessesparâmetros,seráutilizadoocomponente
demapeamentodeparâmetrosapresentadonaseção 3.5. Sendoassim, oteste
envolveráinvocar a classe MapeamentoParametros com a classe da minha
aplicaçãoeverseelarecebeasinformações daformacorreta. Alistagemaseguir
mostraotestequepoderiaserfeitoparaessaverificação.
Listagem 5.14-Verificandoseomapeamentofoifeitodeformacorreta:
@Test
public void arquivosEntradaSaida() {
String[] a =
{"-in","entradaA.txt","entradaB.txt","-out","saida.txt"};
MapeamentoParametros<ParametrosArquivo> map =
139

## Página 146

5.3.Testandoaconfiguraçãodemetadados CasadoCódigo
new MapeamentoParametros<>(ParametrosArquivo.class);
ParametrosArquivo p = map.mapear(a);
assertEquals("entradaA.txt", p.getArquivosEntrada()[0]);
assertEquals("entradaB.txt", p.getArquivosEntrada()[1]);
assertEquals("saida.txt", p.getArquivoSaida());
}
Naposição de quem estáimplementandoa aplicação, édesejávelque seja
lançadaumaexceçãoquandoforempassadosmaisdeumarquivodesaída.Dessa
forma,maisummétododetesteéadicionadoparaverificaressecenário.Alistagem
aseguirmostraaverificaçãoparasaberseumaexceçãoélançadanocasodedois
arquivosdesaídaserempassadoscomoparâmetro.
Listagem 5.15- Verificandose o componente lança exceção com parâmetros
errados:
@Test(expected=MapeamentoException.class)
public void maisDeUmArquivoDeSaida() {
String[] a =
{"-in","entradaA.txt","-out","saidaA.txt", "saidaB.txt"};
MapeamentoParametros<ParametrosArquivo> map =
new MapeamentoParametros<>(ParametrosArquivo.class);
ParametrosArquivo p = map.mapear(a);
}
U m aquestãoimportantenessetipodetesteéqueaverificaçãoéfeitadeacordo
comosrequisitosdaaplicação. Sendoassim, ocomportamentodesejadopode
serobtidoatravésdeumacombinação entremetadadoseocomportamentodo
componentequeutilizareflexão. Porexemplo,imaginequeessaaplicação possua
umparâmetroopcionalparaotimeoutdoprocessamento,queédotipointeiro,
porémocomponentesóaceitaparâmetrosdotipo String,arrayde Stringe
booleano. Alistagemaseguirmostracomoseriaotesteeaimplementação para
esseexemplo.
Listagem 5.16- Verificandose o componente lança exceção com parâmetros
errados:
@Test
public void parametroTimeout() {
140

## Página 147

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
String[] a = {"-time","5000"};
MapeamentoParametros<ParametrosArquivo> map =
new MapeamentoParametros<>(ParametrosArquivo.class);
ParametrosArquivo p = map.mapear(a);
assertEquals(5000, p.getTimeout());
}
//implementação
public class ParametrosArquivo {
@Parametro("-time")
private int timeout;
public void setTimeout(String timeout) {
this.timeout = Integer.parseInt(timeout);
}
}
Observequeotesteexpressasomenteocomportamentoesperado,nãoseimpor-
tandoseafuncionalidadeseráimplementadasomentepelocomponenteousevai
precisarsercomplementadanasclassesdaaplicação. Nocaso,éesperadoqueseja
retornadoumvalorinteiropelométododeacessonaclasse ParametrosArquivo.
Sendoassim,parageraresseresultadoesperado,comomostradonalistagem,essa
classeprecisariafazeraconversãodovalornomomentoquerecebessea Stringda
classe MapeamentoParametros.
C o m oreutilizar código de teste
Quandoutilizamoscomponenteseclassesbaseadosemreflexãoemetadados,é
possívelreutilizá-loparaexecutarfuncionalidadeparadiversasclassesdaaplicação.
A p e s a rdessereúsopoupartempodedesenvolvimento,ostestesdofuncionamento
docomponenteparacadaclassedaaplicação podesertrabalhosoetomarmuito
tempo.Porém,seavaliarmosotestedomesmocomponenteparadiferentesclasses,é
possívelpercebemqueelespossuemmuitoemcomum,comoachamadadopróprio
métododocomponente.Nessaseção,vamosvercomoépossívelreutilizarcódigo
dessetipodeteste,paraquesepossapoupartempodedesenvolvimentotambém
nessaetapa.
Alistagemaseguirmostraoexemplodeumtestequeverificaageraçãodomapa
paraaclasse Produto. Nessecaso,oatributo descricaoprecisaserignorado
141

## Página 148

5.3.Testandoaconfiguraçãodemetadados CasadoCódigo
eoatributo categoriadeveterserinseridonomapacomo "tipo". Observe
queasasserções verificamasinformações queestãonomapaeosatributosquenão
devemestarnomapa.Comojáfoidito,éimportantelembrarqueoqueestásendo
testadonãoéo GeradorMapa,masosmetadadosconfigurados.
Listagem 5.17-TestandoageraçãodomapaparaaclasseProduto:
public class TesteMapaProduto {
@Test
public void geracaoMapa() {
Produto p = new Produto();
p.setNome("Tablet APX10");
p.setPreco(500.00);
p.setDescricao("10 pol, 16GB, 800x600");
p.setCategoria("Eletrônicos");
Map<String,Object> mapa = GeradorMapa.gerarMapa(p);
assertEquals(mapa.get("nome"), "Tablet APX10");
assertEquals(mapa.get("preco"), 500.00);
assertEquals(mapa.get("tipo"), "Eletrônicos");
assertFalse(mapa.containsKey("descricao"));
assertFalse(mapa.containsKey("categoria"));
}
}
Paraserpossívelreutilizaraclassedeteste,oprimeiropassoésepararapartedo
testequeémaisgeraldoqueaqueéespecíficaparaaclasse Produto.Aideiaéque
métodosauxiliaresforneçamasinformações específicasparaseremutilizadasem
ummétododetestegenérico.Nalistagemaseguir,issofoifeitoparaaclassedeteste
mostradaanteriormente.Ométodo getObjeto()criaepopulaoobjetoqueserá
utilizadoparaoteste,eosmétodos getConteudoMapa()e getExcluidos()
retornamrespectivamenteasentradasesperadasparaomapaeaschavesquenão
devemestarpresentesnomapa.
Listagem 5.18- Separando a parte geral do teste da parte específica para a
classeProduto:
public class TesteMapaProduto {
142

## Página 149

CasadoCódigo Capítulo5.TestandoclassesqueusamReflexão
@Test
public void geracaoMapa() {
Object o = getObjeto();
Map<String,Object> mapa = GeradorMapa.gerarMapa(o);
Map<String,Object> esperado = new HashMap<>();
getConteudoMapa(esperado);
for(String s : esperado.keySet()){
assertEquals(esperado.get(s), mapa.get(s));
}
List<String> excluidos = new ArrayList<>();
for(String s : excluidos){
assertFalse(mapa.containsKey(s));
}
}
protected Object getObjeto() {
Produto p = new Produto();
p.setNome("Tablet APX10");
p.setPreco(500.00);
p.setDescricao("10 pol, 16GB, 800x600");
p.setCategoria("Eletrônicos");
return p;
}
protected void getConteudoMapa(Map<String, Object> esperado){
esperado.put("nome", "Tablet APX10");
esperado.put("preco", 500.00);
esperado.put("tipo", "Eletrônicos");
}
protected void getExcluidos(List<String> excluidos){
excluidos.add("descricao");
excluidos.add("categoria");
}
}
Aseguir,comomostradonapróximalistagem,pode-seextrairumasuperclasse
abstrataquecontémaimplementação dométododetesteeadeclaração abstrata
dosmétodosmaisespecíficos.Dessaforma,aclasse TesteMapaProdutoapenas
implementaessesmétodosauxiliares,provendoinformações paraotestequefoi
definidonasuperclasse. Comoachamadademétodoéamesma,épossívelfazer
isso,poisoquemudaéapenasoobjetopassadoparaométodoeoqueéesperado
paraoretorno.
143

## Página 150

5.4.GerandoclassescomClassMock CasadoCódigo
Listagem 5.19- Criando uma classe modelo para a criação de testes do gera-
dordemapas:
public abstract class TesteMapaGenerico {
@Test
public void geracaoMapa() {
Object o = getObjeto();
Map<String,Object> mapa = GeradorMapa.gerarMapa(o);
Map<String,Object> esperado = new HashMap<>();
getConteudoMapa(esperado);
for(String s : esperado.keySet()){
assertEquals(esperado.get(s), mapa.get(s));
}
List<String> excluidos = new ArrayList<>();
for(String s : excluidos){
assertFalse(mapa.containsKey(s));
}
}
protected abstract Object getObjeto();
protected abstract void getConteudoMapa(Map<String,
Object> esperado);
protected abstract void getExcluidos(List<String> excluidos);
}
Pormaisqueaquantidadedelinhasdecódigonãomudemuito,terapenasmé-
todossimplesparaimplementarcertamenteaumentaavelocidadedecriação dos
testesdeoutrosobjetos.Esseefeitosepotencializa,quandoexistemoutrosmétodos
eoutroscenáriosaseremtestados.
5.4 Gerando classes co m Cl a s sMo c k
U m adasdificuldadesdetestarclassesecomponentesqueutilizamreflexãoéofatode
precisaracadatestedefinirumaclasseparaserpassadacomoparâmetro.Algumas
vezes,adiferençaentreclassesdefinidasemdiferentestesteséapenasaassinatura
deummétodoouapresençadeumaanotação.Infelizmente,nãodáparareutilizar
adefiniçãodeumaclasseparaaoutra,pormaisqueelassejammuitosimilares.Isso
acabatornandoadefiniçãodetesteparaessetipodeclassemaistrabalhosaemais
verbosa,poisasclassesprecisamserdefinidassempreporinteiro.
144

## Página 151

CasadoCódigo Capítulo5. TestandoclassesqueusamReflexão
Visandosimplificaressetipodeteste,oframework ClassMock[1]geraclasses
emtempodeexecu çãoparaserempassadascomoparâmetro.Esseframeworkpode
serbaixadonoendere çohttp://classmock.sf.net. Aoinvésdecriarumaclasseda
formausual,comofoivistonasse çõesanteriores,apartirdaclasse ClassMock
sãoinseridasasinforma çõesdaclassequesedesejacriar,comopropriedades(que
incluematributoemétodosdeacesso),interfaces,superclasse,métodos,anota ções,
entreoutros.Dessaforma,épossívelreutilizarumadefini çãoinicialcomobasepara
gerarasvaria çõesnecessáriasparaummétodo,oumesmocriarmétodosqueinsiram
determinadasestruturasemumamockclass. Oobjetivodessase çãoéapresentar
aabordagemutilizadapeloClassMock,semnecessariamenteapresentartodosos
métodosdisponíveisemsuaAPI.Paraumconhecimentomaisaprofundadodetodas
asfuncionalidadesdessaferramenta,sugere-seacessaradocumenta çãodisponível
nositedoprojeto.
Utilizando o ClassMock no gerador de mapas
ParaexemplificarousodoClassMock,alistagemaseguirmostraosmesmos
testes desenvolvidos para a classeGeradorMapa na seção 5.1, criados agora
utilizandoesseframework.Observequeométodo criarMockClass()éanotado
com @Beforeeporissoseráexecutadoantesdetodososmétodosdeteste.Nesse
método,écriadoumaclassebaseparaostesteschamadade Beanequepossui
aspropriedades prop1dotipo Stringe prop2inteira,damesmaformaque
noexemplooriginal.Umatributodaclassedetestechamado mockClassdotipo
ClassMockéutilizadoparaguardaressasinforma ções.
Listagem 5.20-TestesdogeradordemapasutilizandooClassMock:
public class TesteGeradorMapaClassMock {
private ClassMock mockClass;
@Before public void criarMockClass(){
mockClass = new ClassMock("Bean");
mockClass.addProperty("prop1", String.class)
.addProperty("prop2", int.class);
}
@Test public void mapaDeClasseSimples() {
Object instance = ClassMockUtils.newInstance(mockClass);
ClassMockUtils.set(instance,"prop1","teste");
145
E-book gerado especialmente para maria cristina alves - cristinaalves.melo@gmail.com

## Página 152

5.4. GerandoclassescomClassMock CasadoCódigo
ClassMockUtils.set(instance,"prop2",25);
Map<String,Object> mapa = GeradorMapa.gerarMapa(instance);
assertEquals("teste",mapa.get("prop1"));
assertEquals(25,mapa.get("prop2"));
}
@Test public void ignoraPropriedade() {
mockClass.addAnnotation(
"prop1", Ignorar.class, Location.GETTER);
Object instance = ClassMockUtils.newInstance(mockClass);
ClassMockUtils.set(instance,"prop1","teste");
ClassMockUtils.set(instance,"prop2",25);
Map<String,Object> mapa = GeradorMapa.gerarMapa(instance);
assertFalse(mapa.containsKey("prop1"));
assertEquals(25,mapa.get("prop2"));
}
@Test public void mudaNomePropriedade() {
mockClass.addAnnotation("prop2", NomePropriedade.class,
Location.GETTER, "propriedade2");
Object instance = ClassMockUtils.newInstance(mockClass);
ClassMockUtils.set(instance,"prop1","teste");
ClassMockUtils.set(instance,"prop2",25);
Map<String,Object> mapa = GeradorMapa.gerarMapa(instance);
assertEquals("teste",mapa.get("prop1"));
assertEquals(25,mapa.get("propriedade2"));
assertFalse(mapa.containsKey("prop2"));
}
}
Emseguida,emcadamétododetesteécriadoumnovoobjetoapartirdamock
classdefinida,noqualsãoconfiguradaspropriedades.Comoaclasseédefinidaem
tempodeexecu ção,éprecisoutilizarreflexãoparamanipularseusmétodoseains-
tanciar,porémopróprioClassMockpossuiumaclassechamada ClassMockUtils
commétodosauxiliaresquepodemserutilizadosparaisso.Noexemplo,sãousados
osmétodos newInstance(),queretornaumainstânciadeumaclassedefinida
com ClassMock,e set(),queinsereumvaloremumapropriedade.Outrosmé-
todosdessaclassesão get(),querecuperainforma ções,e invoke(),queexecuta
métodos.Casoométodotestadonãorecebaumainstânciadaclasse,masumains-
tânciade Classrepresentandoaclasse,elapodeserrecuperadaapartirdométodo
createClass()daprópriaclasse ClassMock.
Observe no exemplo de classe de teste mostrada que os métodos de teste
146
E-book gerado especialmente para maria cristina alves - cristinaalves.melo@gmail.com

## Página 153

CasadoCódigo Capítulo5. TestandoclassesqueusamReflexão
ignoraPropriedade()e mudaNomePropriedadea()adicionamumaanota-
çãonamockclassantesdecriaremumainstânciadela.Dessaforma,épossívelapro-
veitaraestruturainicialdaclassedefinidanométodoanotadocom @Beforepara
depoisfazerasmodifica çõesnecessáriasnosmétodosdeteste. Pe çoaoleitorpara
voltarnase ção5.1evercomodessaformaépossíveldefinirostestesdeformamais
objetivaemenosverbosa.
ClassMock + JMock = testes de proxies dinâmicos
AideiaprincipaldoClassMockécriaraestruturademockclassesparaserem
utilizadasparateste.Quandosãoadicionadaspropriedades,oClassMockgeranão
sóoatributo,mastambémaimplementa çãodosdoismétodosdeacesso. Porém,
nãoéoseuobjetivogerarocomportamentodemétodos,massomenteasuaestru-
tura.Quandoénecessáriosimularalgumcomportamento,éprecisoutilizaralgum
frameworkdemockobjects,comooJMock,paracriaromockobjectdamockclass
definida.Essetipodeprática,comofoivistonase ção5.2,éocaminhoquedeveser
utilizadoparaacria çãodetesteparaproxiesdinâmicos.
Alistagemaseguirmostracomoessaabordagemseriautilizadacombinando
ousodosframeworksClassMockeJMockparaotestedaclasse CacheProxy.
Inicialmente,aclasse ClassMockéutilizadaparacriarumainterfacechamada
CacheMe. Osegundoparâmetro trueindicaqueumainterfaceserácriada. Em
seguida, éadicionadoummétodoabstratochamado comCache()queretorna
inteiro,indicadopeloprimeiroparâmetro,erecebeuminteiro,indicadopeloúltimo
parâmetro. Porfim,éadicionadaaanota ção @Cachenométodo comCache().
Todosessesparâmetrosserãoutilizadosparaagera çãodinâmicadainterfacepara
serutilizadapeloteste,queéfeitanomomentoqueométodo createClass()é
chamado.
Listagem 5.21-TestesdogeradordemapasutilizandooClassMock:
public class TesteCacheProxyClassMock {
@Rule public JUnitRuleMockery ctx = new JUnitRuleMockery();
@Test
public void cacheSimples() throws Throwable {
ClassMock cm = new ClassMock("CacheMe", true);
cm.addAbstractMethod(int.class, "comCache", int.class)
147
E-book gerado especialmente para maria cristina alves - cristinaalves.melo@gmail.com

## Página 154

5.5. Consideraçõesfinais CasadoCódigo
.addMethodAnnotation("comCache", Cache.class);
Class<?> interf = cm.createClass();
final Object mock = ctx.mock(interf);
Object proxy = CacheProxy.criar(mock);
ctx.checking(new Expectations() {{
ClassMockUtils.invoke(one(mock),"comCache",1);
will(returnValue(10));
}});
assertEquals(10, ClassMockUtils.invoke(proxy,"comCache",1));
assertEquals(10, ClassMockUtils.invoke(proxy,"comCache",1));
}
}
Opróximopassodepoisdacria çãodamockclass,éacria çãodorespectivomock
objectparadefinirasexpectativaseocomportamentodoobjetoqueseráencapsu-
ladopeloproxydinâmico. Ométodo mock()échamadorecebendoainterface
criadadinamicamente,eretornaumainstânciadelacontroladapeloJMock.Emse-
guida,oproxyécriadoapartirdoencapsulamentodomockobject.Depoisdisso,
alógicadotesteéamesma,porém,comoainterfacefoicriadadeformadinâmica,
éprecisoutilizarométodo invoke()daclasse ClassMockUtilsparafazera
invocaçãodosmétodos.Notequeessemétodoéutilizadonasasser çõeseinclusive
paradefinirasexpectativasdomockobject.
5.5 C onsiderações finais
Essecapítuloapresentouastécnicasbásicasparaotestedeclassesqueutilizamre-
flexãoemetadadosparaseuprocessamento.Inicialmentefoimostradaacria çãode
classesparasimulardiferentesestruturasqueserãoconsumidaspelostestes,eemse-
guidacomoasinvoca çõesdemétodospoderiamserverificadas.Baseadonosexem-
plosapresentados,foiintroduzidooconceitode mock classqueparaotestedesse
tipodeclasseédiferenteecomplementaraos mock objects.Tambémfoiabordado
otestedeproxiesdinâmicos,quecombinamosconceitosdemockclassemockob-
jectparaadefini çãodoteste.Porfim,vimosotestedaconfigura çãodemetadados,
quedeveserfeitopelasaplica çõesqueutilizamessescomponentesparaverificarse
osmetadadosestãoconfiguradoscorretamenteparaqueocomportamentosejao
esperado.
148
E-book gerado especialmente para maria cristina alves - cristinaalves.melo@gmail.com

## Página 155

CasadoCódigo Capítulo5. TestandoclassesqueusamReflexão
Emgeral,otestedessetipodecomponenteédifícildeserrealizadopoisdepende
defatoresdinâmicosnasclasses,quemuitasvezessãodifíceisdeseremprevistose
simulados.Porém,essadificuldadeéumobstáculoquenãopodeimpediracria ção
dessestestes,pois,porserreutilizadoemdiversaspartesdosistema,éprecisoque
elepossuaumaboaqualidade.FrameworkscomooJMockouoClassMockajudam
adiminuiralgumasdificuldadesinerentesaessetipodeteste,porémdependendo
dafuncionalidadedaclasse,novasdificuldadespodemsurgir,epodemdemandar
atéacria çãodeoutrasclassesauxiliaresparaviabilizaracria çãodoteste.
149
E-book gerado especialmente para maria cristina alves - cristinaalves.melo@gmail.com

## Página 156

E-book gerado especialmente para maria cristina alves - cristinaalves.melo@gmail.com

## Página 157

CasadoCódigo ReferênciasBibliográficas
Referências Bibliográficas
[1] Clovis Fernandes Eduardo Guerra, Fabio Silveira. Classmock: A
testing tool for reflective classes which consume code annotations.
WorkshopBrasileirodeMétodosÁgeis(WBMA2010),2010.
[2] HansRohnertPeterSommerladMichaelStalFrankBuschmann,RegineMeu-
nier. Pattern-Oriented Software Architecture Volume 1: A System of Patterns.Wi-
ley,1996.
[3] Pattie Maes. Consepts and experiments in computational reflection.
ProceedingsoftheInternationalConferenceonObjectOrientedProgramming,
Systens,LanguagesandApplications,1987.
[4] JavaCommunityProcess. Javabeans(tm)specification1.01finalrelease. http:
//download.oracle.com/otndocs/jcp/7224-javabeans-1.01-fr-spec-oth-JSpec/,
1997.
[5] Brian Smith. Reflection and semantics in a procedural language.
TesedeDoutorado-DepartmentElectricalandComputerScienceEngineering,
MassachusettsInstituteofTechnology,1982.
151
E-book gerado especialmente para maria cristina alves - cristinaalves.melo@gmail.com