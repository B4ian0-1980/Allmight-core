---json
{
  "id": "vraptor_desenvolvimento__gil_para_web_com_java",
  "title": "VRaptor Desenvolvimento Ágil para Web com Java",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "**Arquivo Original:** `VRaptor Desenvolvimento Ágil para Web com Java.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "com",
    "desenvolvimento",
    "gil",
    "java",
    "linguagens",
    "para",
    "vraptor",
    "web"
  ],
  "perguntas_tipo": [
    "Como utilizar VRaptor Desenvolvimento Ágil para Web com Java?",
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

# VRaptor Desenvolvimento Ágil para Web com Java

> **Arquivo Original:** `VRaptor Desenvolvimento Ágil para Web com Java.pdf`
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
1 Introdu ção 1
1.1 Umpoucodehistória ............................ 1
1.2 Ondevocêvaichegarcomesselivro? ................... 2
2 O come ço de um projeto com VRaptor 3
2.1 Vantagensedesvantagens .......................... 4
2.2 Oprojeto—Lojadelivros ......................... 4
2.3 Criandoosprojetos ............................. 5
2.4 CriandoumHelloWorld .......................... 1 0
2.5 Criandoosprojetosdalivraria ....................... 1 1
3 Crie o seu primeiro cadastro 17
3.1 Cria çãodosmodelos ............................ 1 7
3.2 CriandooCadastro ............................. 1 9
3.3 Complementandoocadastro ........................2 6
4 Organiza ção do código com Inje ção de Dependências 33
4.1 CompletandoofuncionamentodoController .............. 3 3
4.2 InversãodeControle:Inje çãodeDependências .............4 0
4.3 ImplementandoaEstante .......................... 4 3
4.4 Criandoobjetoscomplicados-ComponentFactory ...........4 8
4.5 Tempodevidadoscomponentes-Escopo ................ 5 0
4.6 Callbacksdeciclodevida .......................... 5 3
4.7 Outrostiposdeinje çãodedependênciae@PostConstruct ...... 5 5
i

## Página 6

Sumário CasadoCódigo
5 T omando o controle dos resultados 5 7
5.1 Redirecionandoparaoutrométododomesmocontroller ....... 5 7
5.2 Disponibilizandováriosobjetosparaasjsps ............... 5 9
5.3 Maissobreredirecionamentos .......................6 0
5.4 Outrostiposderesultado .......................... 6 1
6 V alidando o seu domínio 67
6.1 Internacionaliza çãodasmensagens .................... 7 2
6.2 Valida çãofluente ............................... 7 4
6.3 Organizandomelhorasvalida çõescomoBeanValidations ...... 7 7
6.4 Boaspráticasdevalida ção .........................8 0
7 Integra ção entre Sistemas usando o VRaptor 85
7.1 Serializandoosobjetos ........................... 8 7
7.2 Recebendoosdadosnosistemacliente .................. 9 3
7.3 Consumindoosdadosdoadmin ..................... 9 5
7.4 TransformandooXMLemobjetos ....................9 9
7.5 AproveitandomelhoroprotocoloHTTP-REST ............1 0 1
7.6 Usandométodoserecursosdamaneiracorreta .............1 0 4
7.7 UsandoRESTnonavegador ........................1 0 8
8 Download e Upload de arquivos 109
8.1 Enviandoarquivosparaoservidor:Upload ...............1 0 9
8.2 Recuperandoosarquivossalvos:Download ...............1 1 5
8.3 Outrasimplementa çõesdeDownload ..................1 1 8
9 Cuidando da infraestrutura do sistema: Interceptors 121
9.1 Executandoumatarefaemváriospontosdosistema:Transa ções . . . 121
9.2 Controlandoosmétodosinterceptados ..................1 2 5
9.3 Evitandoinstancia çãodesnecessáriadeinterceptors:@Lazy ......1 2 8
10 Melhorando o design da aplica ção: Conversores e T estes 137
10.1 Populandoobjetoscomplexosnarequisi ção:Conversores .......1 3 8
10.2 TestesdeunidadeemprojetosqueusamVRaptor ...........1 5 3
11 Próximos passos 157
ii

## Página 7

CasadoCódigo Sumário
12 Apêndice:Melhorando a usabilidade da aplicação com AJAX 161
12.1 Executantoumaoperaçãopontual:Remoçãodelivros. . . . . . . . . 163
13 Apêndice:Containers de Injeção de Dependência 171
13.1 PicoContainer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
13.2 SpringIoC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
13.3 GoogleGuice. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
13.4 CDI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
14 Apêndice:Plugins para o VRaptor 181
14.1 VRaptorJPA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
14.2 VRaptorHibernateeVRaptorHibernate4. . . . . . . . . . . . . . . . 183
14.3 VRaptorEnvironment. . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
14.4 VRaptorSimpleMaileVRaptorFreemarker. . . . . . . . . . . . . . . 187
14.5 Agendamentodetarefas:VRaptorTasks . . . . . . . . . . . . . . . . . 189
14.6 Controledeusuários:VRaptorSACI . . . . . . . . . . . . . . . . . . . 191
14.7 Criandooseupróprioplugin . . . . . . . . . . . . . . . . . . . . . . . 194
15 Apêndice:Funcionamento interno do VRaptor 197
15.1 InicializaçãodoServidor . . . . . . . . . . . . . . . . . . . . . . . . . . 197
15.2 Definindoospapéisdoscomponentes:estereótipos . . . . . . . . . .202
15.3 TratamentodeRequisições . . . . . . . . . . . . . . . . . . . . . . . . .207
15.4 CatálogodeInterceptors . . . . . . . . . . . . . . . . . . . . . . . . . .208
15.5 Maisinformações sobreofuncionamentodoVRaptor. . . . . . . . . 215
iii

## Página 9

Capítulo1
Intro dução
1.1 U m pouco de história
Hámuitotempo,desenvolverumaaplica çãowebemJavaeraumatarefamuitotra-
balhosa.Porumlado,tínhamososServletseJSP,nosquaistodootratamentodas
requisiçõeseramanualecadaprojetoouempresaacabavacriandoseupróprio fr a-
mework—“O”framework—paratrabalhardeumaformamaisagradável.Poroutro
lado,tínhamosváriosframeworksquesepropunhamaresolverosproblemasdadifi-
culdadedesetrabalharcomosServlets,masquelheobrigavamaescrevertoneladas
deXML,arquivos .propertieseaestenderclassesouimplementarinterfaces
parapoderagradaraesseframework.
Nessecenáriosurgiuaideiadeumframeworkmaissimples,quefacilitasseo
desenvolvimentowebsemtornaroprojetorefémdassuasclasseseinterfaces.Sur-
giaoVRaptor,criadopelosirmãosPauloSilveiraeGuilhermeSilveira,em2004na
UniversidadedeSãoPaulo.Em2006foilan çadaaprimeiraversãoestável:oVRap-
tor2,comaajudadoFabioKung,doNicoSteppateváriosoutrosdesenvolvedores,
absorvendováriasideiaseboaspráticasquevieramdoRubyonRails.

## Página 10

1.2. Ondevocêvaichegarcomesselivro? CasadoCódigo
Em2009,oVRaptorfoitotalmentereformulado,levandoemcontaaexperiên-
ciaobtidacomoserroseacertosdaversãoanterioredemuitosoutrosframeworks
daépoca.Aversão3levaaoextremoosconceitosdeConven çãosobreConfigura-
çãoeInje çãodeDependências,emquetodososcomportamentosnormaispodem
sermudadosfacilmenteusandoanota çõesousobrescrevendoumdoscomponen-
tesinternos—bastando,paratanto,implementarumaclassecomainterfacedesse
componente. Alémdisso,estanovaversãopossibilitacriardeumamaneirafácil
nãoapenasaplica çõeswebquerodamno browser,mastambémservi çoswebque
seguemasideiasdeservi çosRESTful,facilitandoacomunica çãoentresistemasea
implementaçãodeAJAXnobrowser.
1.2 O nde você v ai chegar com esse livro?
OobjetivodesselivroémostrarmuitoalémdousobásicodoVRaptoresuascon-
venções. Maisimportantequeaprenderessasconven çõeséentenderaarquitetura
internadoVRaptorecomocriarsuasprópriasconven ções,adaptandooVRaptor
paraasnecessidadesespecíficasdoseuprojeto.Sabercomoascoisasfuncionamin-
ternamenteémetadedocaminhoandadoparaquevocêtenhaumdomíniosobreo
frameworkesesintaconfortávelparafazeroquequisercomele.
DuranteessesmaisdetrêsanosdoVRaptor3,tenhorespondidoasmaisvari-
adasdúvidassobreoseuusonoGUJ( http://www.guj.com.br),oquenosajudou
muitoamodelarasnovasfuncionalidadesedescobrir bugs. Mas,muitomaisdo
queisso,mostrou-nostodoopoderdaextensibilidade:mesmoosproblemasmais
complexosenecessidadesmaisespecíficasdosprojetosconseguiramserresolvidos
sobrescrevendoocomportamentodoVRaptorusandoosmeiosnormaisdasuaAPI
ousobrescrevendoumdeseuscomponentes.
Nestelivrovocêvaiverousobásicoeesperado,juntocomoqueconsidero
boaspráticaseusoprodutivodasferramentasqueesseframeworkproporciona.
Mastambémcompartilharvárioscasosdousonãoesperadoecomotambéméfácil
implementá-los.
Portanto,esselivroépraquemquerentendercomofuncionaoVRaptorecomo
aproveitartodooseupoderesuaextensibilidadeparatornarodesenvolvimentode
aplicaçõesomaisfácileprodutivoquantopossível.
Estáprontoparacome çar?
2

## Página 11

Capítulo2
Ocome çodeumprojetocom
VRaptor
Umgrandeproblemanodesenvolvimentodeumprojetoéjustamentecomo(e
quando)come çá-lo.Issonãosónapartetécnica,éprecisodefinirmuitobemqual
éoproblemaaserresolvido,qualéoperfildousuáriodosistema,comoseráausa-
bilidade,ondeseráinstalado,emuitosoutrosdetalhesquedeveminfluenciarnas
escolhasquevocêdevefazer.
Hojeemdiatemosmuitasferramentas—bibliotecas,frameworks,linguagensde
programação,servidoresetc—ànossadisposi ção,oquetornamuitodifícildefinir
oqueusar.Muitasdestasferramentassãoboaseadequadaspararesolveroseupro-
blema.Maisimportantedoquesaberquandousarumaferramentaésaberquando
nãousá-la,ouquandoelavaiatrapalharmaisdoqueajudar.

## Página 12

2.1. Vantagensedesvantagens CasadoCódigo
2.1 V antagens e desv antagens
OVRaptoréumframeworkfeitoparadesenvolveraplica çõesWebetambémmuito
bomparadesenvolverAPIsHTTP/RESTparacomunica çãoentresistemas. Éum
frameworkMVCquedáumsuportemuitobomàpartedoModelo—asclassesque
contémalógicadenegóciodasuaaplica ção.Comele,émuitofácilaplicarasmelho-
respráticasdeorienta çãoaobjetos,jáquenãoimpõerestri çõesno designdassuas
classes,alémdefacilitarapráticadeInversãodeControleporInje çãodeDependên-
cias.
ÉtambémumdosframeworksmaisextensíveisqueexisteemJava.Praticamente
todososcomportamentosdoVRaptorpodemsersobrescritoscommuitopouco
códigoesemconfigura çõesemXMLouarquivos .properties.
Alémdisso,éumframeworkquenosdeixatotalmentelivreparaescolhersua
camadadeVisualiza ção. Oquetambémsignificaquenãonosajudarámuitopara
desenvolveroHTMLdaspáginas,diferentedealgunsoutrosframeworkscomo,por
exemplo,oJSF.VocêpodeusarJSP,Velocity,Freemarkerparagerarostemplates,
masoscomponentesvisuaisprecisamserfeitosmanualmente,ouusandoalguma
bibliotecaexternacomoojQueryUI,YUIouExtJS.Cadavezmais,essasbibliotecas
setornammaissimplesdeseremusadas,entãoatémesmocompoucoconhecimento
deJavascript,HTMLeCSS,épossívelcriarumainterfacericaeinteressante.
2.2 O p r o j e t o— L oja de livros
Naspróximaspáginas,desenvolveremosumalojadelivrosonlinequeteráduaspar-
tes:aadministrativa,naqualserãogerenciadostodososlivros,quantidadeemes-
toqueetc;eapartedevendas,emqueserãomostradostodososlivrosparaqueo
usuáriopossaescolhê-losecomprá-los.
Essasduaspartesserãofeitasemprojetosseparados,quetrocarãodadossempre
quenecessário.Aparteadministrativaguardarátodososdadosreferentesaoslivros,
numbancodedados.Apartedevendasnãoteráacessoaessebancodedados,apenas
consultaráosdadosdolivrousandoaAPIdaparteadministrativa.
Aideiadesseprojetoésersimplesosuficienteparaqueconsigamoscome çara
desenvolvê-losemmuitocontextoinicial,masaomesmotempotratandodediversos
aspectosreaisdodesenvolvimentodeaplica çõesweb,comocadastros,uploadsde
imagens,integra çãoentresistemas,comunica çãocomobancodedados,transa ções,
segurança,entreoutros.
4

## Página 13

CasadoCódigo Capítulo2. OcomeçodeumprojetocomVRaptor
2.3 C riando os projetos
ExistemváriasformasdecriarumprojetocomVRaptor,cadaumacomseuspré-
requisitoseflexibilidades.Portanto,mostraremosaseguirasmaneirasmaiscomuns
esuaslimita ções.
VRaptor Blank Project
OVRaptorBlankProjectéumprojetopreparadocomomínimonecessáriopara
rodaroVRaptor. Parabaixá-lo,iremosnapáginade DownloadsdositeVRaptor:
http://vraptor.caelum.com.brlink Download. Esseprojetoestáemumzipcomo
nome vraptor-blank-project-3.x.y.zip,noqual3.x.yéaúltimaversãodo
VRaptorejáestáconfiguradoparaEclipseeNetbeans,bastandoimportarozippara
poderrodá-lo.NocasodoEclipse:
1) Acesseomenu Fi le>> I m p o r t;
2) SelecioneExisting projects into Workspace;
3) Marqueaopção Select archive fileecliqueem Browse...;
4) Escolhao vraptor-blank-project-3.x.y.zip;
5) CliqueemFinish.Umprojetocomonome vraptor-blank-projectdeveaparecer;
6) Cliquecomobotãodireitonoprojetoeescolha R u n A s>> Run On Server;
7) Escolhaalgumservidorexistenteoucrieum;
8) Deveaparecerumateladizendo:“Itworks!!VRaptor!/vraptor-blank-project/";
9) OprojetocomoVRaptorestáconfiguradocomsucesso!
Apartirdeagora,vocêpodedesenvolveroseuprojeto.Essaéamaneiramaisrá-
pidadeverumprojetofuncionandocomoVRaptor,masdáumtrabalhoumpouco
maiorparatransformaremumoutroprojeto.Isso,noEclipse,envolverenomearo
vraptor-blank-projectpara seu-projetoeajustaralgumasconfigura ções.
5

## Página 14

2.3. Criandoosprojetos CasadoCódigo
Zip do VRaptor
Também na página de Downloads do VRaptor existe um arquivo chamado
vraptor-3.x.y.zip,quecontémadistribui çãocompletadaúltimaversãodo
VRaptor. Nessezippodemosencontrarojardovraptor,suasdependências,sua
documentação,javadocecódigofonte.Assim,jáépossívellinkaressesartefatosna
suaIDE[footnoteEclipse,Netbeansetc]efacilitarodesenvolvimento.
Paracriarumprojetousandoessezip,vocêprecisacriarumnovoprojetoweb
nasuaIDE.NocasodoEclipse:
1) Crieumnovoprojetoweb.Aperte Ctrl+Neescolha Dynamic Web Project;
2) Escolhaumnomedeprojeto,porexemplo livraria;
3) SelecionecomoTarget RuntimeumservidorcompatívelcomServlet3.0,como
oTomcat7;
4) Selecione3.0como Dynamic web module version;
5) CliqueemFinish;
6) Abra o zip do VRaptor e copie o arquivo vraptor-3.x.y.jar para a pasta
WebContent/WEB-INF/lib;
7) Também no zip do VRaptor, abra a pastalib/ e copie todos os jars para
WebContent/WEB-INF/lib;
8) Atualizeoprojeto( F5)erodeesseprojetonoservidor;
9) Façao Hello World,seguindoospassosdase ção2.4;
10) Projetoconfiguradocomsucesso!
6

## Página 15

CasadoCódigo Capítulo2. OcomeçodeumprojetocomVRaptor
Rodando o VRaptor em ambientes Servlet 2.5
Asconfigura çõesacimasãoparaambientes Servlet 3.0.Sequiser
rodaroVRaptoremumservidor Servlet 2.5,comooTomcat6,
precisatambémacrescentarno web.xmlasseguinteslinhas:
<filter>
<filter-name>vraptor</filter-name>
<filter-class>br.com.caelum.vraptor.VRaptor</filter-class>
</filter>
<filter-mapping>
<filter-name>vraptor</filter-name>
<url-pattern>/*</url-pattern>
<dispatcher>FORWARD</dispatcher>
<dispatcher>REQUEST</dispatcher>
</filter-mapping>
Esseprocessoéumpoucomaismanual,masébemmaisflexívelenãoprecisa
denadainstaladoamaisnosistema.
Maven
Outrobomjeitodecome çarumprojetojavaéusandooMaven,umaferra-
mentadebuildegerenciamentodedependências. OsjarsdoVRaptorestãono
repositóriodoMaven,portantopodemosacrescentá-locomodependêncianoMa-
ven. Paraisso, precisamosdeleinstaladonocomputador( http://maven.apache.
org/download.html),ounaIDE( http://maven.apache.org/eclipse-plugin.htmlou
http://maven.apache.org/netbeans-module.html). ParacriarumprojetoVRaptor
comoMavensigaospassos:
1) RodeoplugindearchetypedoMaven.Nalinhadecomando:
mvn archetype:generate
NoEclipse: Ctrl+N,escolha Maven Projecteaperte N e x taté a tela de seleçãodo
archetype.
7

## Página 16

2.3. Criandoosprojetos CasadoCódigo
2) Selecioneo maven-archetype-webapp(nalinhadecomandovocêpodedigitar
issoemvezdonúmero)
3) Escolhaum groupId(ex. br.com.casadocodigo),um artifactId(ex.
livraria)eumpacote(ex. br.com.casadocodigo.livraria).
4) Nopom.xmldoprojetocriado,adicioneadependênciadoVRaptor(editandoo
xmloupeloswizardsdoeclipse):
<project ....>
<dependencies>
...
<dependency>
<groupId>br.com.caelum</groupId>
<artifactId>vraptor</artifactId>
<version>3.5.1</version><!-- ou a última versão -->
</dependency>
</dependencies>
</project>
5) Façao H e l l o W o r l d,nase ção2.4.
6) Projetocriadocomsucesso!
OMavenémuitoprodutivosevocêquisertrabalhardojeitodele,masseprecisar
fazeralgomaispersonalizadoparaseuprojeto,prepare-separasedivertiravalercom
toneladasdeconfigura çõesemXML.Etambémreserveumespa çonoseuHDpra
fazerobackupdainternetacadacomando.
VRaptor Scaffold
O VRaptor Scaffold é uma extensão criada pelo Rodolfo Liviero (http://
rodolfoliviero.com.br),inspiradopelafuncionalidadede scaffoldingdo R u b y o n
R a i l s. Comele,acria çãodeprojetoscomoVRaptorficabemmaissimplesefle-
xível. Adocumentaçãocompletaestáem: http://vraptor.caelum.com.br/pt/docs/
vraptor-scaffold-pt/.Parausá-lo,énecessárioteroRubyGems(http://rubygems.org)
instaladonosistemaeseguirosseguintespassos:
1) Instaleagemvraptor-scaffold:
gem install vraptor-scaffold
8

## Página 17

CasadoCódigo Capítulo2. OcomeçodeumprojetocomVRaptor
2) Crieumnovoprojeto:
vraptor new livraria --package=br.com.casadocodigo.livraria
3) Entrenapastadoprojetoebaixeasdependênciascom:
cd livraria
ant resolve
4) ImporteoprojetonoEclipse(ouNetbeans)
5) FaçaoHelloWorld(se ção2.4)epronto!
Oprojetocriadousaoant( http://ant.apache.org)paragerenciarobuildeoivy
(http://ant.apache.org/ivy)paragerenciarasdependências.Masépossívelmudá-lo
parausaroMavenouoGradlecomoferramentadebuild.
Ovraptor-scaffoldgeraváriosarquivosnoprojeto,entreeles:
• arquivosdeconfiguraçãodeprojetodoeclipse(.project,.classpathe.settings)
•build.xmle build.properties—arquivosdeconfiguraçãodoantcomalgumas
targetsjáconfiguradas,como compileparacompilarasclasses, warparagerar
oware jetty.runparasubiraaplica çãonumjetty.
•ivy.xmle ivy.jar—arquivosdeconfiguraçãodoivy.Editeoarquivoivy.xml
paraacrescentardependênciasaoprojetoerodeo ant resolve parabaixá-
las.
• emsrc/main/javaforamcriadostrêspacotes: controllers, modelse
repositories,earquivospadrãosevocêusarocomando v r a p t o rs c a ff o l d
paracriarosmodelosdasuaaplica ção.
• emsrc/main/resourcesforamcriadososarquivosdeconfigura çãodohiber-
nate,jpaelog4j.
• emsrc/main/webappforamcriadosarquivosjavascriptecsspadronizados
parafacilitaroiníciodoprojeto.Tambémestáconfiguradoositemesh( http://
sitemesh.org),quefacilitaacria çãodetemplates(comocabe çalhoserodapés,
menuspadronizadosetc).
9

## Página 18

2.4. CriandoumHelloWorld CasadoCódigo
2.4 C riando um HelloWorld
Comoprojetocriado,podemosveroVRaptorfuncionandorapidamente,apenas
usandoassuasconven çõesbásicas.OobjetivodoVRaptoréseintrometeromínimo
possívelnasclassesdasuaaplica ção,entãovamoscriarumaclassejavanormal,que
façaumsimples“Olámundo":
public class Mundo {
public void ola() {
System.out.println("Olá Mundo!" )
}
}
Quandoestamosemumaaplica çãoweb,queremospoderexecutaralgumcódigo
quandoousuáriofazumarequisi çãoaosistema—aoacessarumaURLnonavega-
dor,porexemplo.Paraqueométodo ola()sejaacessívelporumaURL,tudoque
precisamosfazeréanotaraclasse Mundocom @Resource:
@Resource
public class Mundo {
public void ola() {
System.out.println("Olá Mundo!" )
}
}
Seguindoaconven çãodoVRaptor, podemosacessaressemétodopelaURL
http://localhost:8080/livraria/mundo/ola. Asclassesquerecebemrequisi çõesweb
nonossosistematêmumpapelespecialnaarquitetura MVC—sãoosControllers.
Paradeixarmosmaisclaroessepapeldanossaclasse Mundo,podemosdizerissono
nomedaclasse,ouseja, MundoController.
OVRaptorexcluiosufixo Controllerdasconven çõesparadefiniraURL,
podemosrenomearnossaclasseetudocontinuaráfuncionando:
@Resource
public class MundoController {
public void ola() {
System.out.println("Olá Mundo!" )
}
}
10

## Página 19

CasadoCódigo Capítulo2. OcomeçodeumprojetocomVRaptor
Dessa forma, continuamos acessando o métodoola() pela URLhttp://
localhost:8080/livraria/mundo/ola.Essemétodoimprime“OláMundo!”,sóqueno
consoledoservidor,precisamosmostrarumatelaparaousuárioqueacessouaURL
dométodoe,seguindoopadrãoMVC,geramosessatelaemoutroarquivo,por
exemploumJSP.Essaéaparte VdoMVC,avisualiza ção. Porpadrão,aofinal
dainvoca çãodométodo ola,oVRaptorredirecionaarequisi çãoparaojspem
/WEB-INF/jsp/mundo/ola.jsp.
Osjspsficamem /WEB-INF/jspparanãoseremacessíveisdiretamentepelo
navegador,for çandotodasasrequisi çõesapassarempelociclocompletodo MVC.
Depoisdisso,vemonomedocontroller(semapalavraController)seguidopelo
nomedométodoeaextensãojsp.Todasessasconven çõespodemserconfiguradas
emodificadaseveremosmaisdissoadiante.
Criandoentãoajspcorrespondenteaométodo ola()do MundoController,
em /WEB-INF/jsp/mundo/ola.jsp:
<html>
<h1>Olá Mundo!!! </h1>
</html>
Paravertudofuncionando,vamossubiroservidoreacessar http://localhost:
8080/livraria/mundo/ola.Apáginaqueacabamosdecriardeveráaparecer:
Epronto!Temostodoocódigonecessárioparaprocessarumarequisi çãocomo
VRaptor.Agoravamoscriarosprojetosnecessáriosparacriarnossalivraria.
2.5 C riando os projetos da livraria
Onossosistemaserádivididoemduaspartes,umaquecuidarádositeondeosusuá-
rioscomprarãooslivros—oprojeto livraria-site—eoutraquecuidarádo
11

## Página 20

2.5. Criandoosprojetosdalivraria CasadoCódigo
cadastrodoslivros—oprojeto livraria-admin.Alémdisso,usaremosoTomcat
comoservidoreoMySQLcomobancodedados.
Paracriaressesprojetos, podemosusarqualquerumdosmétodosdescritos
na seção 2.3, mas para facilitar um pouco a configuração inicial vamos usar o
vraptor-scaffold.Nasuapasta workspace,execute:
vraptor new livraria-site
vraptor new livraria-admin
cd livraria-site
ant resolve
cd ../livraria-admin
ant resolve
Casonãopossaounãoqueirainstalaro vraptor-scaffoldnasuamá-
quina,vocêpodebaixarosprojetosgeradosem: https://github.com/lucascs/livraria/
archive/projetos-criados.zip
Vocêtambémpodeacompanharaevoluçãodoprojetonavegandopeloscommits
desserepositóriodoGIT: https://github.com/lucascs/livraria/commits/master
Agora, podemos importar esses dois projetos no Eclipse, usando o menu
File >> Import >> Existing projects into workspace . Selecione a
suapasta workspace,ondevocêrodouoscomandosdo scaffold,eselecioneos
projetosemseguida.
Provavelmenteseránecessáriocorrigiro build path dosprojetosparaapon-
tarparaojavaeoTomcatconfiguradosnoseucomputador. NocasodoEclipse,
cliquecomobotãodireitoemcadaumdosprojetoseváem B u i l d P a t h>> Confi-
gure Build Patheselecioneaaba Libraries.
12

## Página 21

CasadoCódigo Capítulo2. OcomeçodeumprojetocomVRaptor
Cliqueem A d d L i b r a r y,selecione JRE System Libraryeselecioneopadrãodo
seusistema.Sea Server Libraryestiver (unbound)comonaimagem,cliqueemcima
dela,depoisem E d i teselecioneumdosservidoresinstaladosnoseueclipse.Senão
houvernenhum,épossívelcriarumnomenu N e w>> Server(Ctrl+Neescreva
server),seguindoospassosdowizardqueapareceu.Tambémseránecessárioalterar
o Targeted Runtimedosprojetosparaoservidorescolhidoacima,ouseja,oservidor
ondeosprojetosvãorodar.
Eparaquesejapossívelcolocarosdoisprojetosnomesmoservidor,precisamos
configurarocontextoraizdecadaprojeto.Aindanaspropriedadesdecadaprojetoe
13

## Página 22

2.5. Criandoosprojetosdalivraria CasadoCódigo
entãoem Web Project Settingsvamosmudaro Context root:paraonomedecada
projeto,ouseja, livraria-admine livraria-site.
NessesistemavamosusaraJPA,aespecifica çãodepersistênciadojava,para
guardarosdadosdanossaaplica çãonobancodedados,comoHibernateservindo
comoimplementa çãodaJPA.OVRaptorScaffoldjágeraumesqueletodaconfi-
guraçãonecessáriaparaqueoHibernatefuncionecomaJPA,juntamentecomas
dependênciasdeclaradasnoivy.xmlquejáforambaixadasquandorodamosoco-
mando ant resolve.
Asconfiguraçõessãooarquivo src/main/resources/META-INF/persistence.xml,
noqualdeclaramoso persistence-unit default paraquepossamostraba-
lharcomaJPA,eoarquivo src/main/resources/hibernate.properties,
noqualcolocamosascredenciaisdobancodedadosedemaisconfigura çõesdo
hibernate. Sóiremosusarbancodedadosnoprojeto livraria-admin, portanto
podemosapagaressesarquivosdeconfigura çãodoprojeto livraria-site.
O hibernate.propertiesgerado pelov r a p t o r - s c a ff o l dvem configurado para
usarobancodedados HSQLDB,queéumbancobemsimples,bastanteútilpara
fazermostestesnanossamáquinadedesenvolvimento,masnãodeveserusadoem
sistemasdeprodu ção. Essebancoéosuficienteparacontinuarmosodesenvolvi-
14

## Página 23

CasadoCódigo Capítulo2. OcomeçodeumprojetocomVRaptor
mentodosprojetosdestelivro,poisusaremosapenasconsultassimplesaobancode
dados,massequisermosusaroutrobancodedados,comooMySQL,oPostgresou
oOracle,énecessárioseguirospassosabaixo:
• Mude as propriedades de conexão com o banco, as que começam com
hibernate.connection,paraasdobancoescolhido.NocasodoMySQL
são:
hibernate.connection.driver_class=com.mysql.jdbc.Driver
hibernate.connection.url=jdbc:mysql://localhost/livraria
O localhoste livrariasão,respectivamente,oendere çodamáquinadobanco
eonomedabasededados.Essabasededadosprecisasercriadaantesdeser
usadanoprojeto.
• Configureascredenciaisdousuário.NoMySQLousuáriopadrãoérootea
senhavazia:
hibernate.connection.username=root
hibernate.connection.password=
Useousuárioeasenhaquevocêconfigurouparaabasededadoscriada.
• Adicioneojardodriverdobancodedados.Nonossocaso,bastaadicionar
nonoivy.xmldoprojeto livraria-admin:
<dependency org="mysql" name="mysql-connector-java"
rev="5.1.15" conf="default"/>
Erodarocomando ant resolve nesseprojeto.
Parafinalizaraconfigura çãodosprojetos,vamosapagarosarquivosdopacote
a p pdaspastas src/main/javae src/test/javadosdoisprojetos,poisvamoscriartodos
osoutrosarquivosdaaplica çãosemaajudado v r a p t o r - s c a ff o l d.
Agorasim,podemoscontinuarodesenvolvimentodasduaspartesdonossosis-
tema:o livraria-admineo livraria-site,queveremosnospróximoscapítulos,aco-
meçarpelocadastrodelivros,noadmin.
15

## Página 25

Capítulo3
Crieoseuprimeirocadastro
Agoraquejátemosoprojetocriado,completamenteconfiguradoejáfizemosatéum
“olámundo”paragarantirquetudofunciona,podemoscomeçaraimplementarde
fatonossaaplica ção.Vamosfazeracria çãodocadastroprincipal,comoqualiremos
podergravaremanipularasinforma çõesdoslivros.
Passaremospordiversascaracterísticasdoframeworkeveremostodaselasem
detalhesnodecorrerdolivro.Omaisimportanteéqueagoravocêpercebaafacili-
dadeeobjetividadedoframework.Preparado?
3.1 C riação dos modelos
Onossosistemaseráumalojadelivros,logoumdosdadosmaisimportantesque
teremosqueguardaréacole çãodelivrosdosistema. Cadalivroteráumtítulo,
umadescri ção,umISBN,umpre çoeumadatadepublica ção.Dandoumaaten ção
especialaosdoisúltimosatributos:

## Página 26

3.1. Criaçãodosmodelos CasadoCódigo
•preço:umvaloremdinheiro.Vamosrepresentá-locomotipo BigDecimal,
comoqualpodemosmanterprecisãoqueagenteescolherpraeleequetam-
bémpossuialgumasfacilidadesseprecisarmosrealizarcálculos.
•data de publicação :Podemosrepresentaressadatausandoasclassesjá
embutidasnojava: Dateou Calendar. Escolheremosnessemomentoa
classe Calendar,porserumpoucomaiscompleta,possuindométodospara
manipularadatasemterqueficarfazendocontascomtimestamps.
Melhor alternativ a para as datas
T a n t o a c l a s s ejava.util.Datecomo java.util.Calendar
possuemdoisproblemasfundamentais:ainterfacedosobjetosémuito
ruimdesetrabalhareelassóconseguemrepresentardataehora.Para
resolveresseproblema,existeumprojetochamadoJoda-time( http://
joda-time.org),quepossuirepresenta çõesbemmaiscompletaseflexí-
veisparaabstra çõesdetempo. Porexemplo,nonossocasosóprecisa-
mosdadata,semahora,entãopoderíamosusaraclasse LocalDatedo
Joda-time.
Vamoscriaraclassequerepresentaesselivronoprojeto livraria-admin.
package br.com.casadocodigo.livraria.modelo;
import java.math.BigDecimal;
import java.util.Calendar;
public class Livro {
private String titulo ;
private String descricao ;
private String isbn ;
private BigDecimal preco ;
private Calendar dataPublicacao ;
//getters/setters
}
Paracadastraroslivrosnonossosistema,precisamosarmazená-losemalgum
lugar.Nomomento,aformacomaqualvamosconseguirfazeressearmazenamento
18

## Página 27

CasadoCódigo Capítulo3. Crieoseuprimeirocadastro
nãoimportamuito,portantovamoscriarumaclassequerepresentaumconjuntode
livros—umrepositório,conformeexplicadonolivroDomainDrivenDesigndoEric
Evans.Navidareal,guardamoslivrosnumaestante,entãonadamaisjustoqueusar
essenomeparaabstrairolugarondeguardamoslivros. Criaremosumainterface
comtodasasopera çõesquequeremoster,jáqueaindanãosabemosaindacomo
seráaimplementação.
package br.com.casadocodigo.livraria.modelo;
public interface Estante {
void guarda(Livro livro );
List<Livro> todosOsLivros();
}
3.2 C riando o Cadastro
Paracriarumlivroagoranonossoprojetoweb,precisamoscriarumapáginacomo
formuláriodeadiçãodolivro.
<form action="?" method="post">
...
</form>
Formulárioscomoessepodemconteralgumapartemaisdinâmica,porexemplo
alistadecategoriasemqueumlivropodeestar.Poressemotivo,semprequecria-
mosumapágina,passamosprimeiroporumaclassejavaquevaipopularosdados
necessáriosparaela. CriaremosentãoumControlador,quevaicontrolaronosso
cadastrodelivros,esseseráonosso LivrosController,comummétodopara
forneceracessoaoformulário.
package br.com.casadocodigo.livraria.controlador;
public class LivrosController {
public void formulario() {}
}
19

## Página 28

3.2. CriandooCadastro CasadoCódigo
ParaqueoVRaptorpasseagerenciaressaclassecomoumcontrolador,preci-
samosanotá-lacom @Resource. Issosignificaqueessaclassecontrolaumdos
recursosdaaplica ção,nocasooslivros.Chamamosderecursososdadosqueaapli-
caçãoproduze/ougerenciae,aocolocarmoso @Resouceemumaclassedizemos
aoVRaptorqueessaclasseseráopontodeacessoviaWebdealgumdosrecursosdo
sistema.
import br.com.caelum.vraptor.Resource;
@Resource
public class LivrosController {
public void formulario() {}
}
A partir desse momento, seguindo as convenções do VRaptor, con-
seguimos executar o que está dentro do método formulario, aces-
sando a URI /livros/formulario. Lembrando que a conven ção é:
/<nome_do_recurso>/<nome_do_metodo>. O nome do recurso é o nome
daclassesemapalavra Controller, Livros,comaprimeiraletraminúscula:
livros.Onomedométodoéexatamenteonomedométodo.Ocaminhocompleto
nonossocasoseria http://localhost:8080/livraria-admin/livros/formulario.
Ométodo formularionãofaznadadeinteressanteainda,masvamosusá-lo
parachegaratéapáginadoformulárioque,segundoaconven çãodoVRaptor,estará
em WEB-INF/jsp/livros/formulario.jsp.Essaconven çãoéparecidacom
adaURI: WEB-INF/jsp/<nome_do_recurso>/<nome_do_metodo>.jsp.O
caminhocompletoparaajspseria:
livraria-admin/src/main/webapp/WEB-INF/jsp/livros/formulario.jsp
SeoprojetofoicriadodiretopeloEclipse,semomavenouovraptor-scaffold,
emvezde src/main/webappuse WebContent.
Podemosseguircomacria çãodoformulário.Precisamoscriarumobjetolivroa
partirdele,eparaissoconseguimosusarmaisumaconven çãodoVRaptornonome
dosinputs. Paraisso,precisamosdeumnomedevariávelparaolivrocriado,por
exemplo, livro.Cadainputdeveterseuatributo namecomeçandocomonome
dessavariável,ecadapropriedadeacessíveldelimitadaporpontos.Parapopularo
20

## Página 29

CasadoCódigo Capítulo3. Crieoseuprimeirocadastro
títulodolivro,usamos livro.titulo,paraopre ço, livro.precoeassimpor
diante:
<form method="post">
<h2>Formulário de cadastro de livros </h2>
<ul>
<li>Titulo: <br/>
<input type="text" name="livro.titulo" /></li>
<li>Descricao: <br/>
<textarea name="livro.descricao"></textarea></li>
<li>ISBN: <br/>
<input type="text" name="livro.isbn" /></li>
<li>Preco: <br/>
<input type="text" name="livro.preco" /></li>
<li>Data de publicacao: <br/>
<input type="text" name="livro.dataPublicacao" /></li>
</ul>
<input type="submit" value="Salvar" />
</form>
21

## Página 30

3.2. CriandooCadastro CasadoCódigo
Assimpodemoscriarométododocontrollerquevaireceberopostdessefor-
mulário.Sequisermosolivropopulado,oparâmetrodessemétododevesechamar
livro,queéoprefixodosinputsdoformulário:
@Resource
public class LivrosController {
public void formulario() {}
public void salva(Livro livro ) {
Estante estante = new UmaEstanteQualquer();
estante.guarda(livro);
}
}
22

## Página 31

CasadoCódigo Capítulo3. Crieoseuprimeirocadastro
Criando a classe Uma Estante Qualquer
O código acima não compila, pois não existe a classe
UmaEstanteQualquer. Masépossívelrapidamentecriá-lausandoa
suaIDE(porexemplooEclipseouoNetbeans). NocasodoEclipse,
comocursorem UmaEstanteQualquer,aperte Ctrl + 1 eescolha
aop çãodecriaraclasse. Aclassecriadajáimplementará Estante
ejávaiestarcomosmétodosdainterfaceimplementados,porémem
branco.
Por enquanto você pode deixar esses métodos em branco. No
próximocapítulo,vamosimplementá-losfazendoacomunica çãocom
bancodedadoseaprendendocomooVRaptorpodenosajudarnessa
tarefa.
Comoométodosechamasalva,vaireceberarequisi çãoem /livros/salva,
porissoprecisamoscolocarissonaactiondoformulario. EssaURI,noentanto,
estásemo context-path, entãopodemosusaratag <c:url, ouusaravariável
${pageContext.request.contextPath}paraacrescentá-lo:
<form action="<c:url value=" /livros/salva"/>" method="post">
ou
<form action="${pageContext.request.contextPath}/livros/salva"
method="post">
Melhor ainda, se você não quer lembrar qual é a URI de um dos méto-
dos do controller, você pode usar olinkTo, com o qual você passa o con-
troller e o método e ele retorna a URI correspondente, já com ocontext-path.
Passamos o nome do controller entre colchetes e o nome do método após:
${linkTo[NomeDoController].nomeDoMetodo}. Nonossocaso,ficariaas-
sim:
<form action="${linkTo[LivrosController].salva}" method="post">
Dessaformaficamaisclarooquevaiserexecutado:aa çãodoformulárioéum
linkparao LivrosControllermétodosalva. Quandoousuáriopreenchero
formulárioeclicarem Salvar,oVRaptorvaipegarcadaumdosvaloresdigitados
23

## Página 32

3.2. CriandooCadastro CasadoCódigo
nosinputs(comoprefixo livro)epreencherumainstânciade Livrocomesses
valores.Essainstânciaserápassadaparaométodosalva,comoqualguardamoso
livrona Estante.Apósexecutarométodo salva,oVRaptorautomaticamente
redirecionaparaapágina WEB-INF/jsp/livros/salva.jsp,naqualpodemos
indicarqueolivrofoisalvo:
<h2>Livro adicionado com sucesso! </h2>
<p>Veja aqui a
<a href="${linkTo[LivrosController].lista}">
lista de todos os livros
</a>
</p>
Colocamosumlinkparaalistadetodososlivros,assimpodemosvertudoo
quefoicadastrado.Agoraprecisamoscriaressalistagem,primeiramentecriandoo
métodoquecolocamosnolink:
class LivrosController {
//...
public void lista() {
}
}
Nessecasoqueremosmostraralistadetodososlivros,quevamosbuscarde
algumlugar—daEstanteondeestamosguardandooslivros—equeremosdeixar
essalistadisponívelparausarna jsp. Comoestamosexecutandoummétodona
requisição,podemosusarojeitonaturaldoJava,retornandoovalor,nocasoalista
delivros:
public List<Livro> lista() {
Estante estante = new UmaEstanteQualquer();
return estante.todosOsLivros();
}
Porpadrão,oVRaptordeixaoretornodosmétodosdocontrollerdisponívelna
JSP,seguindooutraconven ção.Seoretornodométodoéumobjetodotipo Livro,
eleserácolocadonumavariávelchamada ${livro},ouseja,nomedaclassecom
aprimeiraletraemminúsculo.
24

## Página 33

CasadoCódigo Capítulo3. Crieoseuprimeirocadastro
Nocasodoretornoseruma List<Livro>,onomedavariávelnoJSPserá
${livroList},ouseja,onomedaclassedoselementosdalistacomaprimeira
minúscula,seguidode List.
Podemoscriaro lista.jspdentrode WEB-INF/jsp/livros,queéojsp
padrãoparaessemétodo lista:
<h3>Lista de Livros </h3>
<ul>
<c:forEach items="${livroList}" var="livro">
<li>${livro.titulo} - ${livro.descricao} </li>
</c:forEach>
</ul>
Por enquanto, para ver essa lista preenchida, precisamos modificar a classe
UmaEstanteQualquerpararetornarumalistadelivros.
@Override
public List<Livro> todosOsLivros() {
Livro vraptor = new Livro();
vraptor.setIsbn("123-45");
vraptor.setTitulo("VRaptor 3" );
vraptor.setDescricao("Um livro sobre VRaptor 3" );
Livro arquitetura = new Livro();
arquitetura.setIsbn("5678-90");
arquitetura.setTitulo("Arquitetura");
arquitetura.setDescricao("Um livro sobre arquitetura" );
return Arrays.asList(vraptor, arquitetura);
}
25

## Página 34

3.3. Complementandoocadastro CasadoCódigo
3.3 C omplementando o cadastro
Oslivrossãoocarro-chefedonossosistemaeparapodervendê-losprecisamosque
assuasinforma çõessejamcompletasedequalidade.Jácriamosalistagemdelivrose
oformuláriodecria çãodeumlivro.Issonãoéobastanteparamanternossalivraria
funcionando,poiselespodemsofreraltera çõesaolongodotempo,principalmente
noseupre ço,entãovamoscriarapossibilidadedeeditaroslivrosexistentes.
Vamosmodificaralistagemadicionandoumlinkparapermitiraaltera çãode
umlivro.Colocaremosumlinkparaaedi çãoemcadalivromostrado:
<h3>Lista de Livros </h3>
<ul>
<c:forEach items="${livroList}" var="livro">
<li>${livro.titulo} - ${livro.descrição}
<a href="${linkTo[LivrosController].edita}">Modificar</a></li>
</c:forEach>
</ul>
Esselinkdeveráabrirumformuláriodeedi ção,queébemparecidocomfor-
muláriodecria ção,masprecisavircomosdadosdolivroqueestamosquerendo
modificarjápreenchidos.Paraisso,precisamosidentificá-lodealgumaforma,por
exemplo,usandooISBN.Parapassaressevalorparaométodo edita,usamosa
formaqueestamosacostumadosparareceberumvalor—atravésdeumparâmetro
nométodo:
public class LivrosController {
public void formulario() {}
public void edita(String isbn ) {}
}
Comochamamosoparâmetrodométodode isbn,podemospassaressepa-
râmetronolink“Modificar”,passandoumparâmetronaURIcomomesmonome
—isbn.Dessaforma,oVRaptorsaberáqueovalorpassadonaURIserápassado
comoparâmetrodométodo:
<a href="${linkTo[LivrosController].edita}?isbn=${livro.isbn}">
Modificar
</a>
26

## Página 35

CasadoCódigo Capítulo3. Crieoseuprimeirocadastro
Assim, se o ISBN do livro é 123-45, o link gerado será
/livros/edita?isbn=123-45. O valor 123-45 será passado como pa-
râmetro do método, e podemos usá-lo para buscar o livro desejado na nossa
Estante.
Paramostraressa Estantenapáginavamosusaramesmaestratégiadalista-
gem:retornarolivronométodo edita.
public Livro edita(String isbn ) {
Estante estante = new UmaEstanteQualquer();
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
return livroEncontrado;
}
Criando o método busca Por Isb n
Novamenteocódigoacimanãocompilaeométodo buscaPorIsbn
ficacomerrodecompila ção.Paracriá-lonainterface Estante,useo
Ctrl + 1 noEclipseeescolhaaop çãodecriaressemétodo.Esseatalho
funcionatodavezquealgoestácomerrodecompila çãopornãoexistir,
eéapresentadaumasolu çãorápidaparaoproblema( Quick Fix). Ex-
perimenteusá-loparafazeraclasse UmaEstanteQualquercompilar.
Queremos,agora,mostrarosdadosdesselivronumformulário,assimvamos
poder modificá-lo. Poderíamos simplesmente copiar oformulario.jsp pra
edita.jspedeixaresseformuláriopreenchido,mascomotodaaltera çãoemum
formuláriovaiterqueserrefeitanooutro,vamosaproveitaromesmoarquivopara
osdoisformulários.Paraisso,precisamosmodificaro formulario.jspparaque
sirvatantoparacriarumlivronovoquantoparaeditarumjáexistente.
Noresultadodométodo editapodemosusar ${livro.titulo}paramos-
trarotítulodolivro, ${livro.preco}paramostraropre çoeassimpordiante.
Parapreencherosinputscomessesvalores,colocamo-losnoatributo valuedecada
um:
<form action="${linkTo[LivrosController].salva }" method="post">
<h2>Formulário de cadastro de livros </h2>
<ul>
27

## Página 36

3.3. Complementandoocadastro CasadoCódigo
<li>Titulo: <br/>
<input type="text" name="livro.titulo"
value="${livro.titulo}"/></li>
<li>Descricao: <br/>
<textarea name="livro.descricao">${livro.descricao
}</textarea></li>
<li>ISBN: <br/>
<input type="text" name="livro.isbn"
value="${livro.isbn}"/></li>
<li>Preco: <br/>
<input type="text" name="livro.preco"
value="${livro.preco}"/></li>
<li>Data de publicacao: <br/>
<input type="text" name="livro.dataPublicacao"
value="${livro.dataPublicacao}"/>
</li>
</ul>
<input type="submit" value="Salvar" />
</form>
Noresultadodométodo formularionãoexisteum Livroretornado,então
asexpressões ${livro.titulo}, ${livro.preco}etcficarãoembranco,que
éoesperadonoformuláriodeadi ção. AgorasófaltafalarparaoVRaptorusaro
formulario.jspcomoresultadodométodo edita.Paramodificaroresultado
padrãodeummétodo,oVRaptorpossuiaclasse Result,quepodemosreceber
comoparâmetrodométododea ção:
public Livro edita(String isbn , Result result ) {
//...
}
Falaremosmaissobreo Resultnocapítulo5,porenquantosóqueremosusar
amesmapáginadométodo formulario,ouseja,omesmo resultadodométodo
formulariodessemesmo controller.Dizemosissocomométodo ofdo Result:
public Livro edita(String isbn , Result result ) {
Estante estante = new UmaEstanteQualquer();
28

## Página 37

CasadoCódigo Capítulo3. Crieoseuprimeirocadastro
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
result.of(this).formulario();
return livroEncontrado;
}
Traduzindo,queremosoresultado( result)dessecontroller( of(this))no
métodoformulário( .formulario()). Comomodificamosoresultadopadrão,
nãopodemosmaisretornaro Livronessemétodo,poisoretornoaconteceria
apósamudan çadoresultado.Retornamoso livroEncontradoporquequeremos
incluí-lonapáginadoformulário,ouseja,incluí-lonoresultadodométodo,então
podemosusaro Resultparaexpressaressainten çãocomométodo include:
public void edita(String isbn , Result result ) {
Estante estante = new UmaEstanteQualquer();
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
result.include(livroEncontrado);
result.of(this).formulario();
}
Dessaforma,incluímoso livroEncontradonoresultado,damesmaforma
quefazíamosnoretornodométodo,mas antesderedirecionarparaapáginado
formulário.Apesardavariávelnocódigojavaser livroEncontrado,esseobjeto
passaráa jspcomo ${livro},queéonomedaclassecomaprimeiraletrami-
núscula.Eapáginausadaseráa WEB-INF/jsp/livros/formulario.jspenãomaisa
edita.jsp.Nessecaso,sómodificamosojspaserutilizado—ométodo formulario
nãoseráexecutado.
Paraconseguirmosveroformuláriopreenchidoadequadamente,podemosmo-
dificarométodo buscaPorIsbndaclasse UmaEstanteQualquer,retornando
umdoslivros:
@Override
public Livro buscaPorIsbn(String isbn ) {
return todosOsLivros().get(0);
}
29

## Página 38

3.3. Complementandoocadastro CasadoCódigo
Apósmodificarosdadosdoformulárioeclicarem“Salvar”,oVRaptorvaiexe-
cutarométodo salva,conformeoqueestáconfigurado,eapósguardarolivro
naestanteapáginadesucessoémostrada.Sequisermoscontinuarcadastrandoou
modificandolivros,precisamosclicarnolink“Vertodososlivros”.
Paratornaroprocessomaisprático,jáqueconseguimosalteraroresultadopa-
drão,vamoseliminaressapáginadesucessoeretornardiretoparaalistagemde
livros,mostrandoumamensagemdesucessoemcimadalistagem.
Seguindoamesmaideiadométodo edita,poderíamosmodificaro salva
pararecebero Resultemudaroresultadoparaalistagem:
public void salva(Livro livro , Result result ) {
Estante estante = new UmaEstanteQualquer();
estante.guarda(livro);
result.of(this).lista();
}
Mas,comofoiditoanteriormente,essamudan çaderesultado nãoexecutariao
método listae,portanto,nãomostrariaalistadetodososlivros—sóapágina
lista.jspsemavariável ${livroList}queiriaserpreenchidapelométodo
lista.Sequeremosexecutarométodo,costumamosfalarquevamos redirecionar
30

## Página 39

CasadoCódigo Capítulo3. Crieoseuprimeirocadastro
aexecu çãodeummétodoparaoutro.Nonossocasoqueremosredirecionarparao
método lista,entãoachamadanecessáriaéo redirectTo:
public void salva(Livro livro , Result result ) {
Estante estante = new UmaEstanteQualquer();
estante.guarda(livro);
result.redirectTo(this).lista();
}
Ouseja,comoresultadodométodo salvavamosredirecionarparaométodo
listadessemesmo controller.Paraindicarqueolivrofoisalvo,vamosadicionar
umamensagemantesdoredirecionamento:
public void salva(Livro livro , Result result ) {
Estante estante = new UmaEstanteQualquer();
estante.guarda(livro);
result.include("mensagem", "Livro salvo com sucesso!" );
result.redirectTo(this).lista();
}
Nesse caso, estamos incluindo aString “Livro salvo com sucesso!” no
result,eusandoavariável ${mensagem}.Assimpodemosmodificarnossalis-
tagemparamostraressamensagem:
<c:if test="${not empty mensagem}" >
<p class="mensagem">
${mensagem}
</p>
</c:if>
<h3>Lista de Livros </h3>
<ul>
<c:forEach items="${livroList}" var="livro">
<li>
${livro.titulo} - ${livro.descrição}
<a href="${linkTo[LivrosController].edita}">Modificar</a>
</li>
</c:forEach>
</ul>
31

## Página 40

3.3. Complementandoocadastro CasadoCódigo
Conseguimosconstruiratéaquiasopera çõesmaisimportantesdocadastrode
livros,praticamentesóusandoasconven çõesbásicasdoVRaptor. CriamosURLs
paraexecutarocódigodo LivrosController,usandoaanota ção @Resource.
Comosjspsnocaminhocerto,conseguimoslinkarparaosmétodosdoscontrollers
usandoo ${linkTo[NomeDoController].metodo}.Comosinputsdeumfor-
mulárioseguindoaconven çãodenomes,conseguimospreencherobjetoseusá-los
nocontroller,comovimosnométodo salva. E,porfim,conseguimosalteraro
resultadodeummétododocontrollerusandoo Result.
NospróximoscapítulosveremosqueoVRaptornosajudamuitomais,nãoso-
mentenocontroledasrequisi ções,mastambémnaorganiza çãodoscomponentesda
suaaplica ção,afinalodesenvolvimentodeumaaplica çãovaimuitoalémdesimples
cadastros.Veremostambémcomointegraroquefizemoscomobancodedadose
outrosservi ços.
32

## Página 41

Capítulo4
OrganizaçãodocódigocomInje ção
deDependências
4.1 C ompletando o funcionamento do Controller
Nocapítuloanterior,osmétodosdo LivrosControllerforamimplementados
usandoumaclassechamada UmaEstanteQualquer,paraexecutarasopera ções:
public List<Livro> lista() {
Estante estante = new UmaEstanteQualquer();
return estante.todosOsLivros();
}
Issofoifeitoporque,nesteprimeiromomento,paraconstruirmososmétodos
do controller,bastavaapenasqualquerimplementa çãode Estantefornecendoa
interfacenecessária.Porém,paratermososistemafuncionando,precisamosdefinir
umaimplementa çãorealde Estante,quevaiguardaroslivrosparapodermos
mostrá-losemseguida.Sãováriasasmaneirasdefazerisso.Porexemplo,guardando

## Página 42

4.1. CompletandoofuncionamentodoController CasadoCódigo
oslivrosemarquivosouusandoalgumservi çodearmazenamentodedados,masa
formamaiscomuméusarumaimplementa çãoqueguardaoslivrosnum ba n c o de
dados. Vamos,então,mudaraimplementa çãode Estantedocontrollerparaa
EstanteNoBancoDeDados.
public List<Livro> lista() {
Estante estante = new EstanteNoBancoDeDados();
return estante.todosOsLivros();
}
Masparaseconectaraumbancodedadoseconseguirsalvarlivroslá,éneces-
sárioinformarqualéosistemadebancodedadosutilizado,usuárioesenhapara
fazeraconexãoequaléabasededados,logopoderíamosteroseguintecódigo:
public List<Livro> lista() {
Estante estante = new EstanteNoBancoDeDados(BDs.MySQL,
"usuario", "senha", "db_livraria");
return estante.todosOsLivros();
}
Eseessaestanteabriuumaconexãocomobancodedadoseeujátermineide
usá-la,eudeveriaavisaraestante,senãoelacorreriaoriscodemanteraconexão
abertaindefinidamente. Então,precisamoscolocarocódigoparafecharessaco-
nexão.Uma Estantenãoprecisaserfechada,masaimplementa çãodobancode
dadossim,entãoométodopraissosódeveriaestarnaimplementa ção.Dessaforma,
ocódigoficaria:
public List<Livro> lista() {
Estante estante = null;
try {
estante = new EstanteNoBancoDeDados(BDs.MySQL,
"usuario", "senha", "db_livraria");
return estante.todosOsLivros();
} finally {
((EstanteNoBancoDeDados)estante).fechaConexao();
}
}
Reparecomoocódigoficoubemmaiscomplexoqueantes,issousandoapenas
a Estante.Imagineagoraessecódigoespalhadoporcadamétododoseusistema
quedependedobancodedado.Acomplexidadedessecódigosedáporumacoisa:
34

## Página 43

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
aclasse LivrosControllerestácriandoainstânciade Estanteparapodertra-
balhar.Paraisso,o LivrosControllerprecisasaberqualéaimplementa çãode
Estanteadequada,quaissãoasconfigura çõesnecessáriasparacriarumainstância
dessaimplementa çãoe,aofinal,saberseprecisasinalizaràinstânciaahoradefe-
charosrecursosabertos.Essetipodecódigoestálongedeserresponsabilidadeda
LivrosController,portantonãodeveriaestaraqui.
Alémdisso,seprecisarmosumdiatrocarobancodedadosusado,oupassar
ausarumservi çodearmazenamento,teríamosquepassarportodosospontodo
sistemaqueusamestantestrocandoasimplementa ções. Esequisermosguardar
oslivrossónamemórianasmáquinasdosdesenvolvedores,masnamáquinade
produçãousarumbancodedados?
Aocriaruma EstanteNoBancoDeDadosno LivrosControllerestamos
acoplandoessasduasclasses:todavezqueprecisarmosalteraraformadetrabalhar
da EstanteNoBancoDeDadostemosquemudartambéma LivrosController.
Nocapítuloanteriorusamos UmaEstanteQualquerjustamenteporquenãofazdi-
ferençaparao LivrosControllerqualéaimplementa çãoda Estante,sópre-
cisadeuma Estanteprontapraserusada.Poderíamos diminuir o acoplamento
fazendoo LivrosControllerdependerapenasdoestritamentenecessáriopara
elatrabalhar:a interface Estante.
Alguémteráquecriaruma Estanteepassarparao LivrosController,
assimo controllerpodeseconcentrarnaquiloparaoquefoifeito:controlarasope-
raçõescomoslivros. Mudamosumcenárioondeocontrolleriaatrásdecriare
gerenciaravidada Estanteparaumondeaestanteécriadaporoutraclassee
simplesmentepassadaparao LivrosControllerusar.
Recapitulando,saímosdeum controllerqueestavaassim:
@Resource
public class LivrosController {
public void formulario() {}
public void salva(Livro livro , Result result ) {
Estante estante = new UmaEstanteQualquer();
estante.guarda(livro);
result.include("mensagem", "Livro salvo com sucesso!" );
result.redirectTo(this).lista();
}
35

## Página 44

4.1. CompletandoofuncionamentodoController CasadoCódigo
public List<Livro> lista() {
Estante estante = new UmaEstanteQualquer();
return estante.todosOsLivros();
}
public void edita(String isbn , Result result ) {
Estante estante = new UmaEstanteQualquer();
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
result.include(livroEncontrado);
result.of(this).formulario();
}
}
Que,aotrocarmosparaa EstanteNoBancoDeDados,ficouassim:
@Resource
public class LivrosController {
public void formulario() {}
public void salva(Livro livro , Result result ) {
Estante estante = null;
try {
estante = new EstanteNoBancoDeDados(BDs.MySQL,
"usuario", "senha", "db_livraria");
estante.guarda(livro);
} finally {
((EstanteNoBancoDeDados) estante).fechaConexao();
}
result.redirectTo(this).lista();
}
public List<Livro> lista() {
Estante estante = null;
try {
estante = new EstanteNoBancoDeDados(BDs.MySQL,
"usuario", "senha", "db_livraria");
36

## Página 45

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
return estante.todosOsLivros();
} finally {
((EstanteNoBancoDeDados) estante).fechaConexao();
}
}
public void edita(String isbn , Result result ) {
Estante estante = null;
try {
estante = new EstanteNoBancoDeDados(BDs.MySQL,
"usuario", "senha", "db_livraria");
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
result.include(livroEncontrado);
} finally {
((EstanteNoBancoDeDados) estante).fechaConexao();
}
result.of(this).formulario();
}
}
E,pararemoveraduplica çãodacria çãodaestanteemtodososmétodos,vamos
moverissoparaoconstrutor,transformandoa estanteemumatributodaclasse:
@Resource
public class LivrosController {
private Estante estante ;
public LivrosController() {
estante = new EstanteNoBancoDeDados(BDs.MySQL,
"usuario", "senha", "db_livraria");
}
public void formulario() {}
public void salva(Livro livro , Result result ) {
try {
estante.guarda(livro);
} finally {
((EstanteNoBancoDeDados) estante).fechaConexao();
}
37

## Página 46

4.1. CompletandoofuncionamentodoController CasadoCódigo
result.redirectTo(this).lista();
}
public List<Livro> lista() {
try {
return estante.todosOsLivros();
} finally {
((EstanteNoBancoDeDados) estante).fechaConexao();
}
}
public void edita(String isbn , Result result ) {
try {
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
result.include(livroEncontrado);
} finally {
((EstanteNoBancoDeDados) estante).fechaConexao();
}
result.of(this).formulario();
}
}
Masnãoqueremosqueo LivrosControllersepreocupecomacria çãoda
Estante,vamospassararecebê-la,peloconstrutor:
@Resource
public class LivrosController {
private Estante estante ;
public LivrosController(Estante estante ) {
this.estante = estante;
}
// ...
}
Ecomoagorao LivrosControllernãosabemaisqualéaimplementa çãode
Estanterecebida,elenãomandamaisaestantefecharaconexão.Ocódigofica:
@Resource
public class LivrosController {
38

## Página 47

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
private Estante estante ;
public LivrosController(Estante estante ) {
this.estante = estante;
}
public void formulario() {}
public void salva(Livro livro , Result result ) {
estante.guarda(livro);
result.redirectTo(this).lista();
}
public List<Livro> lista() {
return estante.todosOsLivros();
}
public void edita(String isbn , Result result ) {
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
result.include(livroEncontrado);
result.of(this).formulario();
}
}
Agoraocódigodocontrollersótemoqueénecessário. Seucódigoficabem
maissimplesefácildeentenderemanter.
Poroutrolado,quemcriavaumainstânciade LivrosController,antessó
faziaum new,comoem:
LivrosController controller = new LivrosController();
controller.lista();
Agora,eleprecisatambémescolherumaimplementa çãode Estante,gerenciar
essaimplementa ção,epassarparaocontroller,antesdepoderusá-lo:
EstanteNoBancoDeDados estante = null;
try {
39

## Página 48

4.2. InversãodeControle:Inje çãodeDependências CasadoCódigo
estante = new EstanteNoBancoDeDados(BDs.MySQL,
"usuario", "senha", "db_livraria");
LivrosController controller = new LivrosController(estante);
controller.lista();
} finally {
estante.fechaConexao();
}
Removemostodaessacomplexidadedo controller,queagoraestábemmaisfácil
desetrabalhar,mastransferimosessacomplexidadeparaoutraclasse,queteráque
fazerotrabalhosujo.
4.2 I nversão de Controle : Injeção de Dependências
Apráticaquevimosanteriormenteéchamadade Inversão de Controle. Elacon-
sisteemextrairtrechosmaisvoltadosàinfraestruturadascamadasmaisexternasda
aplicação—porexemplo,nossoscontrollers.Essestrechossãoisoladosemclasses
especializadas,queinteragememumacamadamaisinterna,ondetêmcondi ções
decentralizarogerenciamentodascomplexidadesqueantesficavamespalhadaspor
todososistema.
inwhichobjectcouplingisboundatruntimebyanassemblerobjectandis
typicallynotknownatcompiletimeusingstaticanalysis.”( http://en.wikipedia.org/
wiki/Inversion_of_control).PM]
Umadastécnicasparainverterocontroleéjustamenteaqueusamos,eelase
chama I n j eção de Dependências. Nessatécnica,evitamosqueaclassecontrolea
criaçãoeogerenciamentodassuasdependências.Emvezdisso,declaramosquais
sãooscomponentesnecessáriosparaofuncionamentodecadaclasseeconfiamos
queinstânciasfuncionaisdoscomponentesserãoinjetadosantesqueaclasseseja
usada.Assim,aresponsabilidadedecriaregerenciaroscomponentesdosistemavai
sendoempurradaparacamadasinferioresatéqueacentralizamosnumcomponente
especializadoquecoordenaráainje çãodasdependênciasnoslugarescertos.
Essecomponenteespecializadoéchamadode containerou provedor(p ro v i -
der)dedependências.Dessaforma,cadacomponentedeclaraquaissãoassuasde-
pendências,sepossívelcomo interfacesparaficarmoslivresparausarqualquerim-
plementação,eregistramosessecomponentecomoumaimplementa çãodisponível
paraainje çãonocontainer.
40

## Página 49

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
Aotentarinstanciarocomponente,ocontainerbuscarácadadependênciae,se
necessário,criaráumanovainstânciadessadependência,quetambémtemsuaspró-
priasdependênciaseesseprocessosegueatéquetodasasdependênciassejamresol-
vidase,então,ocomponenterequisitadoestarácriadoeprontoparausar.
UmadasfilosofiasdoVRaptoréfacilitareincentivarasmelhorespráticasde
desenvolvimentodesoftwaree,paraincentivara I n j eção de Dependências,opró-
prioVRaptorpossuiumcontainerdeinje çãodedependênciasembutido.Todosos
componentesdosistemaquesãogerenciadospeloVRaptorpodemusaressatéc-
nicaedeixaroVRaptorcuidardaresolu çãodasdependências.Paravercomoisso
funciona,vamosvoltaraocontroller.
@Resource
public class LivrosController {
private final Estante estante ;
public LivrosController(Estante estante ) {
this.estante = estante;
}
// resto do código, substituindo as criações de
// estantes por this.estante
}
Ao recebermos uma Estante no construtor, estamos declarando que o
LivrosControllernãopodesercriadosemantesreceberuma Estantepreen-
chidaefuncionando,ouseja,declaramosque Estanteéumadependência.Como
ocontrolleréumaclassegerenciadapeloVRaptor(porcausado @Resource),o
VRaptortentarábuscarumaimplementa çãode Estantecandidataaserinjetada.
Como Estanteéumainterface,precisamosindicarqualéaimplementa çãodessa
interfacequedesejamosusarnosistema.Fazemosissoescolhendoaclassequeim-
plementa Estantemaisapropriadaeanotando-acom @Component:
@Component
public EstanteNoBancoDeDados implements Estante {
//...
}
Agoraquesabemosqueessaimplementa çãousaráumbancodedados,precisa-
mosdefinircomoseráoacessoaessesdados.EmJavaexistemváriasmaneirasde
41

## Página 50

4.2. InversãodeControle:Inje çãodeDependências CasadoCódigo
fazerisso,porexemplousando JDBC,queéaespecifica çãodecomonosconectamos
aobancodedadoseexecutamosSQL,ou H i b e r n a t e,quemapeiaosdadosdeclasses
Javaparatabelas,ouaindaa JPAqueéaespecifica çãoparafazertalmapeamento.
Comoaformadeacessarobancodedadosémuitodiferente,eàsvezesmuito
extensa,emcadaumadessaspossibilidades,nãoqueremosdeixaressetipodecódigo
espalhadopelosistema,entãoencapsulamosesse acessoaos dadosnum objetoque
nosdaráumainterfaceindependentedaferramentaqueusamosparaisso.Onome
quedamosaessetipodeobjetoqueacessadadosé D A O(DataAccessObject).
A EstanteNoBancoDeDadosprecisaráacessarosdadosdelivrosnobanco,
portantoeladependedeum DAOdelivros—um LivroDAO.Paradeclararessa
dependênciafazemoscomonocontroller,recebendoo DAOnoconstrutor:
@Component
public EstanteNoBancoDeDados implements Estante {
private final LivroDAO dao ;
public EstanteNoBancoDeDados(LivroDAO dao ) {
this.dao = dao;
}
//...
}
Aoanotara EstanteNoBancoDeDadoscom @Componentelapassaaser
gerenciadapeloVRaptor,quetentaráprocuraralgumcomponentegerenciadoque
sejaum LivroDAO,ouseja,queimplementeessainterface.Seformosusara JPA
paraacessoaosdados,podemoscriarumaimplementa çãobaseadanisso,eanotar
com @ComponentparaqueelasejagerenciadapeloVRaptorepossaserinjetada
na EstanteNoBancoDeDados.
@Component
public class JPALivroDAO implements LivroDAO {...}
PorusaraJPA,esseDAOprecisadeum EntityManagerparaquetudofun-
cione,logo,recebê-lo-ánoconstrutor. Econtinuamosindicandooscomponentes
gerenciadosatéquetodasasdependênciassejamsatisfeitaseentãoo Controlleré
criadoepodemosusá-loparaatenderumarequisi çãopara,porexemplo,mostrara
páginadalistadetodososprodutos.
42

## Página 51

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
Numprimeiromomento,podeparecermuitotrabalhosodeclarartodosesses
componentes,mas,umavezcriado,ummesmocomponentepodeserusadoemto-
dasasclassesquenecessitamdelesemnenhumcódigoadicional,apenasrecebendo-
onoconstrutor.
4.3 I mplementando a Estante
Agora que sabemos como o VRaptor gerencia as dependências, vamos co-
meçar a criar as implementações reais dos nossos componentes. A classe
LivrosControllerprecisadeuma Estantecomasseguintesopera ções:
public interface Estante {
void guarda(Livro livro );
List<Livro> todosOsLivros();
Livro buscaPorIsbn(String isbn );
}
Comoanossaimplementa çãoguardaráoslivrosnobancodedados,criaremosa
classe EstanteNoBancoDeDados,anotando-acom @ComponentparaoVRaptor
43

## Página 52

4.3. ImplementandoaEstante CasadoCódigo
usá-lacomodependênciadasoutrasclasses:
@Component
public class EstanteNoBancoDeDados implements Estante {
//...
}
Essaclasseacessaosdadosdolivronobancodedados,portantopodemosusar
umaclassequetemessaresponsabilidade,serum DAOdelivros:
@Component
public class EstanteNoBancoDeDados implements Estante {
private final LivroDAO dao ;
public EstanteNoBanco(LivroDAO dao ) {
this.dao = dao;
}
@Override
public void guarda(Livro livro ) {
this.dao.adiciona(livro);
}
@Override
public List<Livro> todosOsLivros() {
return this .dao.todos();
}
@Override
public Livro buscaPorIsbn(String isbn ) {
return this .dao.buscaPorIsbn(isbn);
}
}
44

## Página 53

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
Diminuindo o acoplamento
Reparequeocódigodo LivrosControllernãoprecisasermu-
dadoagoraqueadicionamosaimplementa çãode Estante.Podemos
criaressaimplementa çãousandoqualquertecnologia, comqualquer
classedonossosistemae,aofinal,anotaraclassecom @Component
epronto! Nenhumadasclassesquedependemde Estanteprecisará
sermodificada.
Conseguimosissoporqueoacoplamentodocontrolleréapenascom
a interface Estante,ouseja,éapenascom o que a Estantecon-
seguefazerenãoem comoéfeitaaimplementa ção. Poressemotivo,
prefirareceberinterfacescomodependênciadassuasclasses,principal-
mentequandoaimplementa çãodependedeumatecnologiaoubiblio-
tecaexterna,comoFTPouJPA.
Paraessaclassefuncionar,precisamosdeum LivroDAOcomaseguinteinter-
face:
public interface LivroDAO {
void adiciona(Livro livro );
List<Livro> todos();
Livro buscaPorIsbn(String isbn );
}
Nonossosistema,acessaremosobancodedadoscomaajudadaJPA,aespe-
cificaçãodoJavaparapersistênciadeobjetos. Essesobjetospersistidosnobanco
recebemonomede entidade,então,paraindicarqueum Livrotemessepapel,
anotamosaclassecom @Entity.
Comoestamoslidandocombancosdedados,aosalvarumaentidade,precisa-
mosdeumvalorqueaidentifiquedeformaúnica,demodoquepodemosrecuperar
ovalorsalvodeformafácil.Porissoéobrigatórioqueumdoscamposdaentidade
estejaanotadocom @Id,indicandoqualéoidentificadordaentidade.Nocasodo
livro,temosoISBNquejáéumidentificador,entãopoderíamosusá-locomo @Id,
masparaconseguirmosdistinguirfacilmenteumlivroquejáestásalvonobancode
umqueestásendocriado,vamoscriarumatributoid,numéricoeautomaticamente
geradopelobanco,paraatuarcomoidentificador. Aclasse Livro,então,ficaria
assim:
45

## Página 54

4.3. ImplementandoaEstante CasadoCódigo
@Entity
public class Livro {
@Id @GeneratedValue
private Long id ;
@Column(unique=true)
private String isbn ;
private String titulo ;
private String descricao ;
private BigDecimal preco ;
private Calendar dataPublicacao ;
//getters/setters
}
Colocando o id no formulário
Paraqueoformuláriocontinuefuncionandoparaaedi ção,precisa-
mosacrescentarumcampoquerepresenteoid. Comoessecampovai
serautomaticamentegerado,nãoqueremosqueousuárioaltereoid.Por
essemotivo,vamosacrescentarum inputdotipo hiddennoformu-
lárioparaguardaroid:
<form ....>
<input type="hidden" name="livro.id" value="${livro.id}" />
...
</form>
Comoo Livroéumaentidade, a JPAdisponibilizaogerenciadordeen-
tidades para realizar as operações de persistência. Esse gerenciador se chama
EntityManager,eseránecessárioparaqueo LivroDAO,baseadonaJPA,realize
oseutrabalho.Ouseja,umadependênciaquetambémserárecebidanoconstrutor.
@Component
public class JPALivroDAO implements LivroDAO {
private final EntityManager manager ;
46

## Página 55

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
public JPALivroDAO(EntityManager manager ) {
this.manager = manager;
}
@Override
public void adiciona(Livro livro ) {
if (livro.getId() == null) {
this.manager.persist(livro);
} else {
this.manager.merge(livro);
}
}
@Override
public List<Livro> todos() {
return this .manager
.createQuery("select l from Livro l" , Livro.class)
.getResultList();
}
@Override
public Livro buscaPorIsbn(String isbn ) {
try {
return this .manager
.createQuery("select l from Livro l where l.isbn = :isbn" ,
Livro.class)
.setParameter("isbn", isbn)
.getSingleResult();
} catch (NoResultException e ) {
return null ;
}
}
}
Agora nosso JPALivroDAO funciona, desde que lhe seja passado um
EntityManagerprontoparaserusado.Masaindanãoregistramosnenhumcom-
ponentequesejaum EntityManager.
Setentarmosrodarosistemadojeitoqueestá,oVRaptorprocuraráporum
EntityManagermasnãovaiencontrar.Nessecaso,aconteceráumerronaaplica-
çãofalandoqueoDAOprecisadeum EntityManager,masoVRaptornãosabe
47

## Página 56

4.4. Criandoobjetoscomplicados-ComponentFactory CasadoCódigo
comocriá-lo.
Masseo EntityManageréumcomponentedaJPA,comodevemosregistrá-lo
noVRaptor,sendoquenãoépossívelanotá-locom @Component,jáquenãotemos
seucódigofonte?
4.4 C riando objetos complicados - C omponent Fa c-
tory
Onosso LivroDAOnecessitadeum EntityManagerparaconseguiracessaro
bancodedadose,seguindoainje çãodedependências,recebemosumobjetodessa
classenoconstrutor.
Precisamosagoradeumaimplementa çãode EntityManager, paraqueo
VRaptorconsigainjetaressadependência.Masessaimplementa çãoseráfeitapela
nossaaplica ção? Não! UsaremosoHibernatecomoimplementa çãodaJPA,dessa
forma,oVRaptorteriaqueinstanciarumaclassedoHibernate. Podemoscolocar
@ComponentnumaclassedoHibernate?
Nocasoemqueaimplementa çãodanossadependêncianãoéumaclasseda
nossaaplica ção,nãopodemosmaisusaraestratégiadeanotaraimplementa çãocom
@Componentparagerenciá-la—temosqueusaralgoumpoucomaisflexível.Além
disso,criarum EntityManagernãoésimplesmentedarum newemalgumaclasse
determinada.Ocódigoparaissoéalgoparecidocom:
EntityManagerFactory factory = Persistence
.createEntityManagerFactory("default");
//...
EntityManager manager = factory.createEntityManager();
ParainstruiroVRaptoraexecutarocódigoacimatodavezqueprecisarde
um EntityManager,podemosimplementarainterface ComponentFactory,
quepossibilitaacria çãodeumobjetoexecutandoumcódigoqualquer.Essecódigo
48

## Página 57

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
devesercolocadodentrodométodo getInstance()deum @Componentque
implementaessainterface,tipadaem <EntityManager>:
@Component
public class FabricaDeEntityManager
implements ComponentFactory<EntityManager> {
@Override
public EntityManager getInstance() {
EntityManagerFactory factory = Persistence
.createEntityManagerFactory("default");
EntityManager manager = factory.createEntityManager();
return manager;
}
}
Dessaforma,todavezqueoVRaptorprecisardeum EntityManagerpara
passarnoconstrutordealgumaclasse,eleinvocaráométodo getInstance()do
nosso ComponentFactoryeusaráoseuresultado.Dojeitoqueestáimplemen-
tado,cadaclassequeprecisardeum EntityManagerteráumacópiadiferente—
o getInstance()sempreretornaum EntityManagernovo.Sequisermosre-
tornaromesmo,precisamoscriá-loforadométodo,porexemplo,noconstrutorda
classe:
@Component
public class FabricaDeEntityManager
implements ComponentFactory<EntityManager> {
private final EntityManager manager ;
public FabricaDeEntityManager() {
EntityManagerFactory factory = Persistence
.createEntityManagerFactory("default");
this.manager = factory.createEntityManager();
}
@Override
public EntityManager getInstance() {
return this .manager;
49

## Página 58

4.5. Tempodevidadoscomponentes-Escopo CasadoCódigo
}
}
Assim, enquanto estivermos usando a mesma instância da
FabricaDeEntityManager, o mesmo EntityManager será retornado.
Masquantotempodeveráduraressainstância?
4.5 T empo de vida dos componentes - Escopo
Quandoestamosemumambientedeinje çãodedependências,temosqueindicar
comooscomponentesserãocriados,paraqueonosso containerpossafazerisso
quandonecessário. Entretanto,nãoésóo comoqueimporta,precisamossaber
tambémq u a n d ooscomponentesserão criadosequandoelesnãoserãomaisne-
cessários,ouseja,omomentodeserem destruídos.
Issoéoquechamamosde escopodocomponente,otempoemqueeleseráusado
nosistemaeapósoqualsuainstânciapoderáserjogadafora.
Duranteumescopo,todasasclassesquedependeremdeumcomponentere-
ceberãoamesmainstânciadestecomponente.Comoestamosnumambiente W e b,
todaintera çãocomousuário,comocliquesemlinksousubmissõesdeformulários,
sedáatravésderequisiçõ e s.Logoumescoponaturaléode requisição:todoobjeto
queprecisarsercriadoduranteumarequisi çãoserádestruídoaofinaldela,ouseja,
apósarespostaserdevolvidaparaousuário.
Sendo assim, toda classe gerenciada pelo VRaptor, como as anotadas com
@Resourceou @Component,éporpadrãodeescopoderequisi ção,ouseja,suas
instânciascriadasdurantearequisi çãoserãodestruídasquandoelaacabar. Mas
existemoutrosescoposinteressantesquepodemosusaremqualquercomponente,
usandoasanota çõeslistadasabaixonaclassedocomponente:
•@SessionScoped: escopodesessão. Oobjetoserácriadoporusuáriodo
sistema,atreladoàsuasessãoHTTP( HttpSession). Aofinaldasessão,
sejaporinatividadeouporchamadaexplícita,oobjetoserádestruído.
•@ApplicationScoped:escopodeaplica ção.Apenasumainstânciadocom-
ponenteserácriadanaaplica ção.Tambémchamadode singleton,emalusão
ao Design Patterncomomesmonome.
50

## Página 59

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
•@PrototypeScoped: escopodeprotótipo. Umainstânciadocomponente
serácriadaacadavezqueeleforusadocomodependência,ouseja,cadaobjeto
teráumainstânciadiferentedessecomponente.
•@RequestScoped: escopoderequest,oescopopadrão. Cadarequestterá
umainstânciadiferentedessecomponente.Vocêpodeusaressaanota çãopara
deixarmaisclarooescopodocomponente.
Duranteesselivrovocêaprenderásituaçõesemquecadaumdosescoposseen-
caixammelhorequandousarcadaumdeles.
Atenção : compatibilidade de escopos
Comoalgunsescopossãomaioresqueoutros,temosumarestri ção
importante:umcomponentenãopodeserdependênciadeumoutrode
escopomaior.Porexemplo,seumcomponenteédeescopoderequisi-
ção,nãopodeserdependênciadeumcomponentedeescopodesessão
ouaplica ção,poiselevaiserdestruídoantesdoobjetoquedependedele
eooutroobjetoficaránumestadoinválido.
Seexisteumcomponente ColetorDeEstatisticasqueéúnico
paratodaaaplica ção( @ApplicationScoped),elenãopodereceber
uma Estantenoconstrutor,poisa EstanteNoBancoDeDadoséde
escopoderequisi ção(oescopopadrão).Seissoacontecesse,naprimeira
requisiçãoemqueo ColetorDeEstatisticasfosseusado,eleiria
receberuma Estante.Napróxima,eleusariaamesma Estanteda
últimarequisição,quejáfoijogadafora,poisoseuescopoacabou.
Existe outra particularidade quando estamos trabalhando com uma
ComponentFactory. O escopo é dado à fábrica e não ao objeto fabricado.
O método getInstance será chamado sempre, independente do escopo da
ComponentFactory. Na FabricaDeEntityManagermovemosocódigode
criaçãodo EntityManagerparaoconstrutorjustamenteporessemotivo:
@Component
public class FabricaDeEntityManager
implements ComponentFactory<EntityManager> {
51

## Página 60

4.5. Tempodevidadoscomponentes-Escopo CasadoCódigo
private final EntityManager manager ;
public FabricaDeEntityManager() {
EntityManagerFactory factory = Persistence
.createEntityManagerFactory("default");
this.manager = factory.createEntityManager();
}
@Override
public EntityManager getInstance() {
return this .manager;
}
}
Instânciasdessafábricaserãocriadasacadarequisi ção, ecadainstânciavai
criar seu próprioEntityManager. Só que cada instância também cria uma
EntityManagerFactory,queéumobjetodecria çãocara,quedeveriaserúnico
naaplica çãointeira,ouseja,seuescopodeveriaserodeaplica ção.Paraaproveitar
amesma factoryemtodososrequestsdaaplica ção,precisamosgerenciá-lade
formaseparada.Vamoscome çarrecebendoa factorycomodependência:
@Component
public class FabricaDeEntityManager
implements ComponentFactory<EntityManager> {
public FabricaDeEntityManager(EntityManagerFactory factory ) {
this.manager = factory.createEntityManager();
}
//...
}
Agora precisamos criar a factory em outro lugar — outra
ComponentFactory,comoescopocorreto:
@Component
@ApplicationScoped
public class FabricaDeEntityManagerFactory
implements ComponentFactory<EntityManagerFactory> {
private final EntityManagerFactory factory ;
52

## Página 61

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
public FabricaDeEntityManagerFactory() {
this.factory = Persistence.createEntityManagerFactory("default");
}
@Override
public EntityManagerFactory getInstance() {
return this .factory;
}
}
Assim, a fábrica será única na aplica ção inteira e, como a
EntityManagerFactory está sendo criada no construtor, a factory
também será única na aplicação. Refor çando: mesmo que a fábrica seja
@ApplicationScoped, o método getInstance() será chamado sempre
queoVRaptorprecisardeum EntityManagerFactory.
4.6 C allbacks de ciclo de vida
Criamosuma ComponentFactoryquecria EntityManager,masexisteoutro
fatoimportantesobreele:o EntityManagerabreconexõescomobancodeda-
doseessasconexões precisamserfechadas. Paraisso,precisamoschamaroseu
método close()assimqueacabarmosdeusá-lo,paraevitarovazamentodes-
sasconexões.Mas q u e mvaichamaressemétodo?Algumaclassequedependedo
EntityManager?Nãopodemosfazerdessemodo,poisváriasoutrasclassespodem
estarusandoessemesmo manager.
Aregradeouropararecursosqueprecisamserfechados/liberados,comoco-
nexões,éaseguinte:seumaclasseabriu/adquiriuesserecurso,elaéaresponsável
porfechá-lo/liberá-lo.Poressemotivo,sea FabricaDeEntityManagercriouo
EntityManager,eladeveriafechá-lo.Vamoscriarummétodoparaisso:
@Component
public class FabricaDeEntityManager
implements ComponentFactory<EntityManager> {
private final EntityManager manager ;
//...
public void fechaManager() {
53

## Página 62

4.6. Callbacksdeciclodevida CasadoCódigo
this.manager.close();
}
}
Ométodoestácriado,mas q u a n d oeledeveserchamado? Eledevesercha-
madoquandoacabarmosdeusaro manager,ouseja,aofinaldoescopodafábrica.
Conseguimosfazerissocomocallback @PreDestroy. Ummétododequalquer
componentequeestiveranotadocom @PreDestroyseráchamadologoantesdo
objetoserdestruído,muitoútilparaliberarosrecursosabertos.Essemétodo precisa
retornar voidenãoterargumentos.Nonossocaso,queremoschamarométodo
fechaManageraofinaldoescopodafábrica,entãovamosanotá-lo:
@Component
public class FabricaDeEntityManager
implements ComponentFactory<EntityManager> {
private final EntityManager manager ;
//...
@PreDestroy
public void fechaManager() {
this.manager.close();
}
}
Pronto, agoratemosonossocriadorde EntityManagerimplementadoe,
comoeleeraocomponentequefaltavaparao JPALivroDAOfuncionar,consegui-
mossubiroservidorecome çarcadastraroslivrosdiretamentenobancodedados.
Faltaapenasumdetalhe: quandoestamostrabalhandocombancosdedadossóé
possívelrealizarmodifica çõesaosdadosdentrodeumatransa ção.
Porenquanto,pararesolveresseproblemavamosalteraro JPALivroDAOpara
usartransa ções,masadotaremosumasolu çãomelhornocapítulo 9.Oúnicométodo
quemodificaobancodedadoséométodoadiciona,portantovamoscontrolara
transaçãodentrodele:
@Override
public void adiciona(Livro livro ) {
this.manager.getTransaction().begin();
this.manager.persist(livro);
this.manager.getTransaction().commit();
}
54

## Página 63

CasadoCódigo Capítulo4. OrganizaçãodocódigocomInje çãodeDependências
4.7 O utros tipos de injeção de dependência e @Post -
Construct
OVRaptorinjetadependênciasviaconstrutor,amaneiraescolhidaporexigiromí-
nimodeconfigura ção:nãoépossívelcriaroobjetosempassartodososargumentos
doconstrutor,logotudoqueestánoconstrutorjáéumadependênciadaclasse.Mas
existemoutrasmaneirasdefazerinje çãodedependênciasquesãousadasporoutras
55

## Página 64

4.7. Outrostiposdeinje çãodedependênciae@PostConstruct CasadoCódigo
bibliotecas:
•P o r s e t t e r: bemcomumnoSpring,vocêcriaumsetterparaadependência
eindicaqueessesetterprecisaserinvocado,usandoumaanota çãoouuma
configuraçãoemxml.
•Por atributo:usadonosEJBsenoCDI,adependênciaéinjetadadiretamente
noatributo,viareflection.
•Por método de inicialização: ummétodoquerecebedeumaveztodasas
dependênciasdaclasse.
Emtodosessesoutrostipos,sequisermosexecutaralgumcódigonainicializa-
ção,nãopodemosusaroconstrutor:asdependênciasaindanãoforampreenchidas.
Nessecasopodemosterummétodoanotadocomocallback @PostConstruct.
Essemétodoseráchamadologoapóstodasasdependênciasserempreenchidas,
quandooobjetoestáprontoparaserusado.
@Inject
public void setDependencia(Dependencia dependencia ) {...}
@PostConstruct
public void inicializa() {
logger.info("Classe inicializada" );
dependencia.fazAlgo();
}
OVRaptornãosuportaoficialmenteessesoutrostiposdeinje ção,mascomoele
usaoutrabiblioteca(Spring,GuiceouPicoContainer)paraimplementarainje ção
dedependências,vocêpodeusaraformadabibliotecaescolhidaparausaroutros
tiposdeinje ção. Aanotação @javax.inject.Injectfuncionaemtodasessas
bibliotecas,poisfazpartedaespecifica çãodojavaparainje çãodedependências—
bastacolocá-lanosetter,atributooumétododeinicializa çãodesejado.
56

## Página 65

Capítulo5
Tomandoocontroledosresultados
Temosagoranonossosistemaocadastrodelivrostotalmentefuncional,comto-
dasaspáginaseoslivrossendosalvoserecuperadosdobancodedados. Nesse
cadastro,vimosqueoVRaptortemaconven çãoderetornarparaumajspcomo
mesmonomedométodoexecutado,napastacomonomedocontrollerdentrode
/WEB-INF/jsp.
Essaéumaconven çãomuitointeressantenocasogeralemqueoresultadoda
requisiçãoéumapáginaHTML,masnemsempreéissoquequeremoseparaesses
cenários.Vamosprecisarsobrescreveressaconven ção.
5.1 R edirecionando para outro método do mesmo
controller
Umdosresultadospossíveisquejávimoséreutilizarapáginadeoutrométodo,como
fizemosnométodo edita:

## Página 66

5.1. Redirecionandoparaoutrométododomesmocontroller CasadoCódigo
public void edita(String isbn , Result result ) {
//...
result.of(this).formulario();
}
Nessalinha,estamosdizendoparaoVRaptorusaroresultadodo( result.of)
método formuláriodessemesmoobjeto( (this).formulario()). Conse-
quentemente,ojspusadoseráo /WEB-INF/jsp/livro/formulario.jsp.Ou-
tramudan çadaconven çãoquevimosfoinométodo salvaque,aofinaldarequi-
sição,redirecionaparaalistagem:
public void salva(Livro livro , Result result ) {
//...
result.redirectTo(this).lista();
}
Ouseja,oresultadoseráumredirecionamentopara( result.redirectTo)o
método listadessemesmocontroller( (this).lista()).
Essaclasse ResultéocomponentedoVRaptorresponsávelpelapersonaliza-
çãodoresultadofinaldaexecu çãodométododocontroller. Alémdereceberno
método,podemosrecebê-lonoconstrutordaclasse,principalmenteseformosusar
o Resultnamaioriadosmétodos:
@Resource
public class LivrosController {
public final Estante estante ;
public final Result result ;
public LivrosController(Estante estante , Result result ) {
this.estante = estante;
this.result = result;
}
//...
}
Atravésdisso,opróprioVRaptorseencarregarádeinstanciaredisponibilizaro
objeto Resultparanós.Narealidade,o Resultéum @Component,comovimos
nocapítuloanterior,masquejávemimplementadodentrodopróprioVRaptor.
58

## Página 67

CasadoCódigo Capítulo5. Tomandoocontroledosresultados
5.2 D isponibilizando v ários objetos para as jsps
Outraconven çãoquevimosésobreoretornodométodo.Porexemplo,nométodo
lista:
public List<Livro> lista() {
return this .estante.todosOsLivros();
}
Essalistadelivrosserádisponibilizadaemumatributodarequisi çãochamado
livroList,acessívelnajsppor ${livroList}. Masese,alémdessalistade
livros,quisermosacrescentartambémolivroempromo çãododia?Nãopodemos
simplesmenteretornardoisobjetos,poisissonãoéválidoemjava,entãoprecisamos
novamentedo Resultparaalteraressaconven ção,comométodo include.Com
ele,podemosadicionarquantosobjetosforemnecessários,edarnomesdiferentes
daconven çãoparaelestambém:
public List<Livro> lista() {
this.result.include("promocao", this.estante.promocaoDoDia());
return this .estante.todosOsLivros();
}
Paranãomisturarasconven ções,podemosusaro resultparaalistadelivros
também:
public void lista() {
this.result.include("promocao", this.estante.promocaoDoDia());
this.result.include("livros", this.estante.todosOsLivros());
}
Dessaforma,alistadelivrosnãoficarámaisacessívelpor ${livroList},mas
apenaspor ${livros}.Umasobrecargadessemétodonãorecebecomoparâmetro
onome,comofoiusadonométodo editadocontroller:
public void edita(String isbn ) {
Livro livroEncontrado = this.estante.buscaPorIsbn(isbn);
result.include(livroEncontrado);
result.of(this).formulario();
}
59

## Página 68

5.3. Maissobreredirecionamentos CasadoCódigo
Nessecaso,oVRaptorusaráaconven çãoparanomes: nomedaclassecoma
primeiraletraminúscula. Ouseja,oatributosechamará livro. Essaconvenção
nãofuncionará,noentanto,setentarmosusarumalista:
List<Livro> livros = this.estante.todosOsLivros();
result.include(livros);
Nãoépossíveldescobrirotipogenéricodavariável livros,poisoJavaoapaga
emtempodeexecu ção,logoavariávelaquiseriaapenas“list”aoinvésde“livroList”.
Paradarumnomemelhordevemosusaraversãodométodo includequerecebe
umastring:
List<Livro> livros = this.estante.todosOsLivros();
result.include("livros", livros);
5.3 M ais sobre redirecionamentos
Vimos como redirecionar para outros métodos do mesmo controller mas isso
não resolve todos os nossos problemas. Por exemplo, se estivermos no
LivrosController,invocandoummétodochamado comprarque,aofinalda
compra,redirecionaparaapáginainicialdosistema.Paraisso,podemosusarore-
direcionamentoquerecebeaclassedocontrolleremvezde this:
public void comprar(Livro livro ) {
//todo o processo de comprar o livro
result.redirectTo(HomeController.class).paginaInicial();
}
IssofuncionaparatodosostrêstiposderedirecionamentoqueoVRaptorsu-
portaequepodemserusadosaofinaldométododo controller.Essesredireciona-
mentossão:
•result.of(this).metodo()
ou
result.of(UmController.class).metodo()
apágina jspdométodoindicadoserárenderizada,semexecutarométodo.
Útilquandoqueremoscompartilharamesmajspentredoisoumaismétodos.
60

## Página 69

CasadoCódigo Capítulo5. Tomandoocontroledosresultados
•result.forwardTo(this).metodo() ou
result.forwardTo(UmController.class).metodo(): executa o
métodoindicadoatéofinaleusaoseuresultado. Esseredirecionamentoé
transparenteparaousuário,poisaURLquepermanecenobrowseréado
primeirométodochamado.Éumredirecionamentodotipo FORW ARD,que
éexecutadodoladodoservidor.
•result.redirectTo(this).metodo() ou
result.redirectTo(UmController.class).metodo: redireciona
paraométodoindicado,doladodocliente,ouseja,arequisi çãovoltaparao
browsereaURLétrocadaparaadonovométodo.Éumredirecionamento
dotipo REDIRECT,queéexecutadodoladodocliente.
Redirecionamento no cliente versus Redireciona-
mento no servidor
Osredirecionamentosdotipo REDIRECT,ouseja,doladodocli-
entevoltamparaobrowsereexecutamumanovarequisi çãolimpa,bas-
tanterecomendadoquandoqueremosusarcomoresultadodeummé-
todo(porexemplo,ométodo salvadocontroller)outrométodo(por
exemplo,ométodo lista).Seousuáriorecarregarapágina,arequi-
siçãoirádiretoparaométodo lista,nãopassarámaispelométodo
salva,assimonavegadornãopediráparaelesubmeteroformulário
novamente.
Jáosredirecionamentosdotipo FORW ARD,istoé,doladodoservi-
dor,executamosegundométododentrodamesmarequisi ção,reapro-
veitandotodooestadodessarequisi ção.Deveserusadoquandoquiser-
mosexecutarasduaslógicasnamesmarequisi çãoequando,aorecarre-
garapágina,quisermosexecutarasduaslógicasnovamente.
5.4 O utros tipos de resultado
Acabamosdeverousobásicodo Result,paraasopera çõesmaiscomunsdode-
senvolvimentodeumaaplica çãoweb.Noentanto,existemoutrostiposdemudan ças
deresultadoquesãobastanteúteisemdeterminadassitua ções.Porexemplo,seto-
marmosométodo editado LivrosController:
61

## Página 70

5.4. Outrostiposderesultado CasadoCódigo
public void edita(String isbn ) {
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
result.include(livroEncontrado);
result.of(this).formulario();
}
Oquefazerseforpassadoum isbnquenãopertenceanenhumlivro?Pode-
ríamoscriarumapáginadiferentepraissoeredirecionarparaela:
public void naoEncontrado() {}
public void edita(String isbn ) {
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
if (livroEncontrado == null) {
result.forwardTo(this).naoEncontrado();
} else {
result.include(livroEncontrado);
result.of(this).formulario();
}
}
Mas, emaplicaçõesweb, jáexisteumapáginapadrãopararedirecionarmos
quandotentamosacessaralgoquenãoexiste: apágina404. Sequisermosredire-
cionarparaessapágina,podemosusarométodo notFounddo Result. Assim
seráusadaapágina404configuradanosistema.
public void edita(String isbn ) {
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
if (livroEncontrado == null) {
result.notFound();
} else {
result.include(livroEncontrado);
result.of(this).formulario();
}
}
62

## Página 71

CasadoCódigo Capítulo5. Tomandoocontroledosresultados
63

## Página 72

5.4. Outrostiposderesultado CasadoCódigo
Customizando as páginas de erro
Épossívelcustomizaraspáginasdeerro404ou500padrãodosite,
colocandonoarquivoweb.xml:
<error-page>
<error-code>404</error-code>
<location>/404.jsp</location>
</error-page>
Dessemodo,podemosmostrarumapáginade404comacarado
sistema,aoinvésdapáginapadrãodotomcatoudoservidorescolhido.
Alémdessemétodo,existeo usedoResult,quenospermiteusardiversostipos
deresultado,daseguinteforma:
result.use(umTipoDeResultado).configuracaoDesseResultado();
OstiposderesultadoquejávêmimplementadosnoVRaptorestãodisponíveis
atravésdemétodosestáticosnaclasse Results.Essesresultadossão:
•Results.http():possibilitaaaltera çãodaspartesHTTPdaresposta,como
status code, headers,ouatémesmoretornarumcorpodarequisi ção.Porexem-
plo:
result.use(Results.http()).body("Deu tudo certo" );
Assim,aoinvésdeirparaumaJSP,arespostadarequisi çãoseráotexto“Deu
tudocerto”.
•Results.status():possibilitaaaltera çãodo status codedarequisi ção.Por
exemplo:
result.use(Results.status())
.forbidden("Você não está autorizado a acessar esse conteúdo" );
•Results.json():retornaosdadosdeumobjetoserializadosemJSON.Por
exemplo:
64

## Página 73

CasadoCódigo Capítulo5. Tomandoocontroledosresultados
result.use(Results.json()).from(livro).serialize();
Nessecasoarespostaseráalgocomo:
{ "livro": {
"titulo": "VRaptor 3" ,
"descricao": "Um livro legal sobre VRaptor" ,
"isbn": "12345-6"
} }
•Results.jsonp():semelhanteaoresultadodeJSON,mascomaop çãode
passarumcallbackdeJSONP.
•Results.xml(): semelhanteaoresultadodeJSON,masserializaoobjeto
emXML.
•Results.representation():tentadecidir,deacordocomoqueveiona
requisição,seooobjetopassadoseráserializadoemXML,JSONouseserá
redirecionadoparaaJSP.OusoésimilaraoresultadodeXMLedeJSON.
•Results.nothing(): retornaumarespostavazia. Existeumatalhopara
issonopróprioresult:
result.use(Results.nothing());
//ou
result.nothing();
•Results.referer():possibilitaoredirecionamentodevoltaparaapágina
quegerouarequisi ção. Esseresultadousao Header Refererdarequisi ção,
queemgeraléenviadopelosnavegadores,coma URLdapáginaatual. No
entanto,esseheadernãoéobrigatórioe,senãoestiverpresentenarequisi ção,
esseresultadogeraráumerro.
•Results.page():agrupaosredirecionamentosparapáginas,aquelesque
nãoexecutammétodosdecontrollers.Porexemplo:
result.use(Results.page()).of(UmController.class).metodo();
// que é o mesmo que:
result.of(UmController.class).metodo();
65

## Página 74

5.4. Outrostiposderesultado CasadoCódigo
•Results.logic():agrupaosredirecionamentosparamétodosdeumcon-
troller.Porexemplo:
result.use(Results.logic()).redirectTo(UmController.class).metodo();
// que é o mesmo que:
result.redirectTo(UmController.class).metodo();
Todosessesresultadospossuemmaisop ções,vocêpodeexplorá-lasusandoo
auto-completedasuaIDE.NocasodoEclipse,vocêpodefazer,porexemplo:
result.use(Results.status()).<Ctrl + Espaço>
Evocêconsegueveralistademétodosqueesseresultadodisponibiliza.
66

## Página 75

Capítulo6
Validandooseudomínio
Nossosistemapossuiumcadastrodelivros,comtodososdadoseditáveisnoformu-
lárioimplementadopelo LivrosController.Noentanto,nãopodemosvender
qualquerlivrocadastradonesseformulário. Nomomentoépossívelcadastrarum
livrosemtítuloousempre ço,quenãopodesercolocadoàvendanosite.
Poderíamosficaremtodasaspartesdosistemaverificandoseosdadosdoli-
vro(ouqualqueroutromodelodosistema)estãocorretosantesdeusá-los,masisso
deixaosistemabastantecomplicado,cheiode ifsde‘segurança’.Omelhorafazeré
simplesmentenãoguardarum Livroseelenãosatisfizeralgumasrestri çõesconsi-
deradasnecessáriasparao Livroserusadonosistema.Assim,norestodocódigo
nãoprecisamosnospreocuparemchecarosdadosdolivro:seumlivrochegoupara
nós,eleestáprontoparaserusado.
Paraimplementaressasrestri ções,porexemploaobrigatoriedadedotítulodo
livro,vamosmodificarométodo salvadonosso LivrosController:
public void salva(Livro livro ) {
if (livro.getTitulo() == null) {

## Página 76

CasadoCódigo
//não deixa salvar!
}
estante.guarda(livro);
result.redirectTo(this).lista();
}
Oquesignificanãodeixarsalvar?Essemétodo salvaéinvocadoapartirdo
formuláriodecadastrodo Livroe,seexistealgumcampoinválido,precisamos
avisarparaapessoaqueestápreenchendooformuláriooqueestáerrado.Voltando
paraométodo:
public void salva(Livro livro ) {
if (livro.getTitulo() == null) {
//volta para o formulário dizendo que o título é obrigatório
}
estante.guarda(livro);
result.redirectTo(this).lista();
}
Se,noentanto,existiremmaisvalida ções:
public void salva(Livro livro ) {
if (livro.getTitulo() == null) {
//volta para o formulário dizendo que o título é obrigatório
}
if (livro.getPreco() == null
|| livro.getPreco().compareTo(BigDecimal.ZERO) < 0) {
//volta para o formulário dizendo que o preço é obrigatório e
//deve ser positivo
}
estante.guarda(livro);
result.redirectTo(this).lista();
}
Nãopodemosvoltarparaoformulárioacadacampoqueestáerrado,senãoo
usuáriovaipreencheroformulário,clicarem“Salvar”everqueotítuloestáinválido;
entãoelearrumaotítuloeclicanovamenteem“Salvar”eapáginafalaqueopre ço
estáinválido;eassimpordianteparacadacampodolivro.Melhorseriaacumular
68

## Página 77

CasadoCódigo Capítulo6. Validandooseudomínio
todososerrosqueacontecerememostrartodosdeumaveznoformulário,sehouver
algumerroparasermostrado. Senãoexistiremerrospodemosguardarolivroe
continuarcomoprocesso.
public void salva(Livro livro ) {
if (livro.getTitulo() == null) {
//adiciona o erro "título é obrigatório"
}
if (livro.getPreco() == null
|| livro.getPreco().compareTo(BigDecimal.ZERO) < 0) {
//adiciona o erro "preço é obrigatório e deve ser positivo"
}
if (houverem erros ) {
//volta para o formulário mostrando os erros
}
estante.guarda(livro);
result.redirectTo(this).lista();
}
Poderíamoscontrolartudoissomanualmente,somenteusandoo resultpara
mudarofluxo,mascomoessatarefadevalidarseoobjetoasersalvoébemcomum,
existeumcomponentedoVRaptorespecializadoemexecutaressasvalida ções: o
Validator.Nele,podemosadicionarmensagensdeerrodevalida çãoe,sehouver
erros,redirecionararequisi çãodevoltaparaoformulário,ouseja,exatamenteoque
agentequeria.Parateracessoaessecomponente,recebemo-lonoconstrutor:
@Resource
public class LivrosController {
private Estante estante ;
private Result result ;
private Validator validator ;
public LivrosController(Estante estante , Result result ,
Validator validator ) {
this.estante = estante;
this.result = result;
this.validator = validator;
}
}
69

## Página 78

CasadoCódigo
Paraadicionarumavalida ção,usamosométodo adddo Validator,passando
uma Message. Umadasmensagenspossíveiséa ValidationMessage,coma
qualpassamosotextodamensagemeocampoondeelaocorreu:
if (livro.getTitulo() == null) {
validator.add(new ValidationMessage("título é obrigatório" , "titulo"));
}
if (livro.getPreco() == null
|| livro.getPreco().compareTo(BigDecimal.ZERO) < 0) {
validator.add(new ValidationMessage("preço é obrigatório " +
"e deve ser positivo" , "preco"));
}
Epararedirecionarparaoformulário,fazemosalgobemparecidocomosredire-
cionamentosdo Result.No Validatorfalamosque,sehouvererros,queremos
redirecionarparaoformulário:
validator.onErrorRedirectTo(this).formulario();
Issosegueamesmalógicado Result:estamosredirecionandoparaessemesmo
controller,nométodo formulario.Aovoltarparaoformulário,todososerrosque
ocorreramvãoestardisponíveisnavariável ${errors}.Paramostraroserrosno
formulário,podemosfazer:
<ul class="errors">
<c:forEach items="${errors}" var="error">
<li>
<!-- o campo em que ocorreu o erro, ou o tipo do erro -->
${error.category}:
<!-- a mensagem de erro de validação -->
${error.message}
</li>
</c:forEach>
</ul>
Onossométodo salvaficariaassim:
public void salva(Livro livro ) {
if (livro.getTitulo() == null) {
validator.add(
new ValidationMessage("título é obrigatório" , "titulo")
70

## Página 79

CasadoCódigo Capítulo6. Validandooseudomínio
);
}
if (livro.getPreco() == null
|| livro.getPreco().compareTo(BigDecimal.ZERO) < 0) {
validator.add(new ValidationMessage("preço é obrigatório " +
"e deve ser positivo" , "preco"));
}
validator.onErrorRedirectTo(this).formulario();
estante.guarda(livro);
result.redirectTo(this).lista();
}
Nadaqueestáabaixodalinhado onErrorRedirectToseráexecutadocaso
existaalgumerrodevalida ção.
71

## Página 80

6.1. Internacionalizaçãodasmensagens CasadoCódigo
6.1 I nternacionalização das mensagens
Em Livro,temostítuloepre çocomocamposobrigatórios.Podemosdizertambém
queoISBNéobrigatório,jáqueéonossoidentificadordolivro.Seformospararpra
pensar,cadaclassequeformossalvarnobancovaiteralgunscamposobrigatóriose,
emtodoseles,vamosfazerumavalida çãocomamensagembemparecida:
if (livro.getTitulo() == null) {
validator.add(new ValidationMessage("título é obrigatório" , "titulo");
}
Oqueaconteceagoraseforprecisoalteraramensagemdoscamposobrigatórios
de“campoéobrigatório”para“campodeveserpreenchido"?Vamosterquepassar
pelosistematodomudandoasmensagensdecampoobrigatório.Eseprecisarmos
mostrarasmensagensoraemportuguês,oraemespanholeoraeminglês?Opro-
cessodegera çãodasmensagensficariabemcomplicadoeespalhadopelosistema.
Para resolver esse tipo de problema, o Java possui uma classe chamada
ResourceBundle,quefoipensadaparasepararessetipodemensagensdomeio
docódigo,alémdepossibilitarainternacionaliza ção( i18n)dessasmensagens.Para
fazerisso,precisamoscriarumconjuntodearquivos .properties,umparacada
línguaqueformossuportarnosistema.
messages.properties => as mensagens na língua padrão
messages_en.properties => as mensagens em inglês
messages_es.properties => as mensagens em espanhol
messages_pt_BR.properties => as mensagens em português do Brasil.
Seusarmososarquivosexatamentenessepadrão,come çandocom messages
ecolocando-osno classpath,oVRaptorpossibilitausarasmensagensdessebundle,
comaclasse I18nMessage.Nela,passamosprimeiroocampoqueocorreuoerro
edepoisachavedamensagem:
if (livro.getTitulo() == null) {
validator.add(new I18nMessage("titulo", "campo.obrigatorio"));
}
if (livro.getPreco() == null) {
validator.add(new I18nMessage("preco", "campo.obrigatorio"));
}
if (livro.getIsbn() == null) {
validator.add(new I18nMessage("isbn", "campo.obrigatorio"));
}
72

## Página 81

CasadoCódigo Capítulo6. Validandooseudomínio
Enoarquivo messages.properties(ouemalgumadaslínguas):
campo.obrigatorio = deve ser preenchido
Podemos,ainda,passarparâmetrosparaamensagem,usandoospróximosargu-
mentosdoconstrutordo I18nMessageeusando {0}, {1}, {2} etcnoarquivo
demensagens,representandocadaumdosparâmetrosadicionais,naordemdosar-
gumentos.
if (livro.getTitulo() == null) {
validator.add(
new I18nMessage("titulo", "campo.obrigatorio", "título"));
}
if (livro.getPreco() == null) {
validator.add(
new I18nMessage("preco", "campo.obrigatorio", "preco"));
} else if (livro.getPreco().compareTo(BigDecimal.ZERO) < 0) {
validator.add(
new I18nMessage("preco", "campo.maior.que", "preço", 0));
}
if (livro.getIsbn() == null) {
validator.add(new I18nMessage("isbn", "campo.obrigatorio", "isbn"));
}
messages.properties:
campo.obrigatorio = {0} deve ser preenchido
campo.maior.que = {0} deve ser maior que {1}
Assim,asmensagens,seforemgeradas,ficariam:
título deve ser preenchido
preço deve ser preenchido
preço deve ser maior que 0
isbn deve ser preenchido
Poroutrolado,sedigitarmosumtextoqualquernoscampos“Pre ço”e“Datade
publicação”,receberemosasmensagens:
preco: ???is_not_a_valid_number???
dataPublicacao: ???is_not_a_valid_date???
73

## Página 82

6.2. Validaçãofluente CasadoCódigo
EsseserrossãoadicionadosautomaticamentepeloVRaptorseovalormandado
narequisi çãonãopuderserconvertidoparaotiponecessário.Nonossocaso,con-
verterumtextoqualquerpara BigDecimalou Calendar.Otextoqueestáentre
???éachavedei18nquepodemosusarparageraramensagemdesseserros.Pode-
moscolocarumamensagemcomessachavenomessages.properties,usando {0}
paraincluirovalorinválido:
is_not_a_valid_number = "{0}" não é um número válido
is_not_a_valid_date = "{0}" não é uma data válida
Ereceberasmensagens:
preco: "dez reais" não é um número válido
dataPublicacao: "hoje a noite" não é uma data válida
Esseserrossãoadicionadosantesdocontrollerserexecutadoe,casovocênão
tenhausadoo validatorparadizerparaondeiremcasodeerro,receberáaex-
ception:
There are validation errors and you forgot to specify where to go.
Please add in your method something like:
validator.onErrorUse(page()).of(AnyController.class).anyMethod();
or any view that you like.
If you didn 't add any validation error, it is possible that a
conversion error had happened.
6.2 V alidação fluente
Outraformadeusarasmensagensinternacionalizadas,fugindoumpoucodosifs,é
usandoavalida çãofluentedoVRaptor.Nela,declaramosoquequeremosqueseja
verdade,ecasosejafalso,oerrodevalida çãoéadicionado. Nessetipodevalida-
ção,usamosaclasse Validations,ondepodemosdeclararváriasvalida ções,e
passamosparaométodo checkingdo validator.
validator.checking(new Validations() {{
// queremos que o titulo não seja null. A ordem dos
// próximos parâmetros é a mesma do construtor de I18nMessage
that(livro.getTitulo() != null, "titulo", "campo.obrigatorio",
7 4

## Página 83

CasadoCódigo Capítulo6. Validandooseudomínio
"título");
// esse método that retorna o resultado da condição,
// assim podemos executar condicionalmente a validação (não podemos
// checar se o preço é maior que zero se ele for nulo)
if (that(livro.getPreco() != null, "preco", "campo.obrigatorio",
"preco"))
that(livro.getPreco().compareTo(BigDecimal.ZERO) > 0,
"preco", "campo.maior.que", "preco", 0);
that(livro.getIsbn() != null, "isbn", "campo.obrigatorio", "isbn");
}});
Reparequeaquicolocamosacondi çãoquequeremosquesejaverdadeira,dife-
rentementedaversãocom ifs.
As duas chaves{{ }} sãonecessáriasnessecódigo,poisestamoscriandouma
classeanônimafilhade Validations,comasvalida çõesdeclaradasemsuainici-
alização.Aschavesexternasdeclaramaclasseanônima,easinternasdeclaramum
blocodeinicializa ção,queéexecutadoantesdoconstrutordaclasse.Outropontoé
que,sevocêestáusandoJava6ou5,asvariáveisusadasdentroda Validations
precisamserdeclaradascomo final.Oresultadofinaldométodo salva,usando
essaformadevalida ção,éoseguinte:
public void salva(final Livro livro ) {
validator.checking(new Validations() {{
that(livro.getTitulo() != null, "titulo", "campo.obrigatorio",
"título");
if (that(livro.getPreco() != null, "preco", "campo.obrigatorio",
"preco"))
that(livro.getPreco().compareTo(BigDecimal.ZERO) > 0,
"preco", "campo.maior.que", "preco", 0);
that(livro.getIsbn() != null, "isbn", "campo.obrigatorio", "isbn");
}});
validator.onErrorRedirectTo(this).formulario();
estante.guarda(livro);
75

## Página 84

6.2. Validaçãofluente CasadoCódigo
result.redirectTo(this).lista();
}
Reparequesempreénecessárioespecificaroquefazercasohajaerrosenesse
casoredirecionamosparao formulario.
Parausaressaformadevalida ção,énecessárioincluirnasbibliotecasdaaplica-
çãooHamcrest.Nonossocaso,adicionandoaoivy.xml:
<dependency org="org.hamcrest" name="hamcrest-core" rev="1.2"
conf="default" />
Erodandoocomando“antresolve”.
Saiba mais: validações poderosas usando Hamcrest
OHamcrestéumabibliotecaparafazermos matchingdeobjetos,muitousada
paratestesdeunidade,paragerarmosasser çõesmaislegíveisemlinguagemnatu-
ral. Nocasodavalida çãofluentedoVRaptor,podemoscomporaschecagensdo
Hamcrestnométodo that:
import static org.hamcrest.Matchers.*;
//...
validator.checking(new Validations() {{
that(livro.getTitulo(), is(notNullValue()));
that(livro.getPreco(), is(allOf(
notNullValue(),
greaterThan(BigDecimal.ZERO)
)));
that(livro.getIsbn(), is(notNullValue()));
}});
Nessecaso,amensagemgeradaéumamensagememlinguagemnatural,mas
eminglês,correspondenteàsvalida çõesusadas. Noentanto,épossívelmudaras
mensagensdevalida çãopassandomaisparâmetros:
that(livro.getTitulo(), is(notNullValue()),
"titulo", "campo.obrigatorio");
Mais informações sobre os matchers possíveis:https://code.google.com/p/
hamcrest/wiki/Tutorial
76

## Página 85

CasadoCódigo Capítulo6. Validandooseudomínio
Parausarosmatchersdohamcrestnoprojeto,énecessárioadicionaradepen-
dênciado hamcrest-library:
<dependency org="org.hamcrest" name="hamcrest-library"
rev="1.2" conf="default" />
6.3 O rganizando melhor as v alidações com o Bean
Validations
Emborao ValidatordoVRaptorajudebastante,acabamosrepetindobastante
códigoaodeclararvalida çõesdasmaneirasvistasacima.Porexemplo,todavezque
umcampoforobrigatório,teremosaslinhas:
if (objeto.getCampo() == null)
validator.add(new I18nMessage("campo", "campo.obrigatorio", "campo"));
//ou
that(objeto.getCampo() != null, "campo", "campo.obrigatorio", "campo");
Éamesmacoisaparaoutrostiposdevalida ção,comoverseumnúmeroémaior
quezero,verseumastringtemnomáximo10caracteres,verseumadataestáno
passadoetc.Essasvalida çõesestãopresentesemquasetodotipodeobjetoquevai
sersalvonobancodedados.Poressemotivo,aoinvésdeficarrepetindoesses ifs,
poderíamosfalarqueumdeterminadocampoéobrigatório,ealguémseencarregar
defazero ifparanós.Tambéméomesmoparaumcampoquedevesermaiorque
zero,ouumcampoquetemqueestarnopassado.
Pararesolveresseproblema,existeumaespecifica çãodoJavachamada B e a n
V alidations.Comela,usamosanota çõesemcimadoscampos,paradeclararasva-
lidaçõesaseremaplicadas.Nocasodo Livroasvalida çõesseriam:
@Entity
public class Livro {
@Id @GeneratedValue
private Long id ;
@NotEmpty
private String isbn ;
@NotEmpty
77

## Página 86

6.3. Organizandomelhorasvalida çõescomoBeanValidations CasadoCódigo
private String titulo ;
@NotNull @DecimalMin ("0.0")
private BigDecimal preco ;
@Past
private Calendar dataPublicacao ;
private String descricao ;
//...
}
Eos ifsparaverificarseocampoestáválidoeadicionaramensagemdevalida-
çãoserãofeitosautomaticamente.TudooquetemosquefazeréindicaraoVRaptor
quequeremosvalidaro Livro,comométodo validatedo validator:
public void salva(Livro livro ) {
validator.validate(livro);
validator.onErrorRedirectTo(this).formulario();
estante.guarda(livro);
result.redirectTo(this).lista();
}
78

## Página 87

CasadoCódigo Capítulo6. Validandooseudomínio
Exemplos de anotações de v alidação do Bean Validati-
ons
Aespecifica çãoBeanValidationspossuialgumasanota çõesjápadro-
nizadasparafazermosasvalida ções,mascadaimplementa çãoestálivre
paraadicionarnovasanota çõeseépossívelcriarmosnovasanota çõesna
nossaprópriaaplica ção.SeusarmosoHibernateValidator,algumasdas
anotaçõespossíveissão:
• Paraobjetosemgeral:@Nulle @NotNull,paragarantirqueum
objetosejaounãonulo,respectivamente
• Parastrings:@Size(min=0, max=20),paravalidarotamanho,
@Pattern(regexp="[0-9]*")paracasarpadrões, @Emaile
@CreditCardNumber,paragarantirquea Stringrepresenta
umemailouumnúmerodecartãodecrédito.
• Para números:@Min(2), @Max(30) e @Range(min=1,
max=40), para definir limites para um número inteiro,
@DecimalMin("0.01") e @DecimalMax("999.99"),
para definir limites para um número decimal e
@Digits(integer=6, fraction=2) para definir a pre-
cisãodaparteinteiraedafracionáriadeumnúmerodecimal.
• Paradatas:@Paste @Future,paradatasnopassadoounofu-
turo.
• Parabooleans:@AssertTruee @AssertFalse,paragarantir
queobooleanéverdadeirooufalso.
Aindaépossívelusarbibliotecasdeterceiros, comoporexemplo
oCaelumStella,quenosdávalida çõesbrasileiras,comoo @CPFeo
@CNPJ.
Assim, podemos concentrar a maioria das validações do nosso modelo no
próprio modelo. Mas nem sempre é possível usar uma validação do Bean
validations,como,porexemplo,sequisermossabersejáexisteumlivrosalvo
79

## Página 88

6.4. Boaspráticasdevalidação CasadoCódigo
nobancocomomesmoISBN.Nessecasoprecisamosnosconectaraobancoefazer
umaconsultaporlivroscomumdeterminadoISBN,masonossomodelo Livro
nãopossuiesseacesso.Logo,devemosfazeressavalida çãousandoasformasvistas
anteriormente.
Asmensagensdevalida çãogeradascomoBeanValidationssãoeminglês. Se
quisermossobrescreveramensagemdevalida ção,temostrêsop ções:
• Pormensagemdireta:
@NotNull(message = "Título precisa ser preenchido" )
private String titulo ;
• Porchavedevalidação
@NotNull(message = "{campo.obrigatorio}")
private String titulo ;
Essachaveprecisaestarnobundle ValidationMessages.properties.
• Genericamenteparaumtipodeanotaçãodevalida ção:
//Se o import é esse:
import javax.validation.constraints.DecimalMin;
PodemosadicionarnoValidationMessages.properties:
javax.validation.constraints.DecimalMin = Deve ser maior que {value}
Épossívelinterpolarnamensagemosvaloresqueestãodentrodaanota çãode
validação.Pudemosusaro {value}poisusamosnaanota ção:
@DecimalMin("0.0")
//que é equivalente a
@DecimalMin(value="0.0")
6.4 B oas práticas de v alidação
OBeanValidationséótimoparaimplementaramaioriadasvalida ções,portanto,
idealmenteummétododocontrollerquesalvaalgonobancodeveriaseralgocomo:
80

## Página 89

CasadoCódigo Capítulo6. Validandooseudomínio
public void salva(Livro livro ) {
validator.validate(livro);
validator.onErrorRedirectTo(this).formulario();
estante.guarda(livro);
result.redirectTo(this).lista();
}
Ouseja: mandavalidaroobjeto;retornaparaoformulárioemcasodeerro;
estandotudook,salvaoobjeto;redirecionaparaalgumapáginadesucesso. Um
métodosimplesdeentenderededarmanuten ção. Qualquervalida çãoadicional
podeserfeitadiretamenteno Livrocomasanota çõesdoBeanValidationssem
precisaralterarocontroller.
Masissonãovairesolvertodasasvalida çõespossíveis,poissóconseguimosvali-
darfacilmenteosdadosdealgumdosatributosdo Livro,entãotemosqueexecutar
avalida çãomanualmente:
public void salva(Livro livro ) {
validator.validate(livro);
if (estante.jaExisteNoBanco(livro.getIsbn())) {
validator.add(new I18nMessage("isbn", "isbn.duplicado"));
}
validator.onErrorRedirectTo(this).formulario();
estante.guarda(livro);
result.redirectTo(this).lista();
}
Quantomaisvalida çõesadicionamosnosmétodosdoscontrollers,maisdifícil
éentenderoqueestáacontecendo.Paramanterocontrolleromaissimplespossí-
vel,podemoscriarnovosvalidators,porexemplo,o LivroValidator,quefaráas
validaçõesespecíficasdolivro.
@Component
public class LivroValidator {
private Validator validator ;
private Estante estante ;
81

## Página 90

6.4. Boaspráticasdevalidação CasadoCódigo
private Editoras editoras ;
public LivroValidator(Validator validator ,
Estante estante , Editoras editoras ) {
this.validator = validator;
this.estante = estante;
this.editoras = editoras;
}
public void validate(Livro livro ) {
validator.validate(livro);
if (estante.existeLivroComTitulo(livro.getTitulo())) {
validator.add(new I18nMessage("titulo", "ja.existe"));
}
if (editoras.concorrentes().contains(livro.getEditora())) {
validator.add(new I18nMessage("editora",
"nao.pode.ser.editora.concorrente"))
}
}
//gere os delegate methods do Validator usando a sua IDE!
public <T> T onErrorRedirectTo (T controller ) {
return validator.onErrorRedirectTo(controller);
}
}
Dessaforma,nossométododocontrollervoltaasersimples,bastandoreceber
um LivroValidatoraoinvésdo ValidatordoVRaptor.
@Resource
public class LivrosController {
private LivroValidator validator ;
public LivrosController(/*...,*/ LivroValidator validator ) {
//...
this.validator = validator;
}
public void salva(Livro livro ) {
validator.validate(livro);
82

## Página 91

CasadoCódigo Capítulo6. Validandooseudomínio
validator.onErrorRedirectTo(this).formulario();
estante.guarda(livro);
result.redirectTo(this).lista();
}
}
Deummodogeral,prefiracontrollerscommenoscódigo,focadosemcontrolar
arequisi ção,emantenhalógicasdenegócioemcomponentesespecializados,ounos
própriosmodelos(comono Livroouna Estante).
83

## Página 93

Capítulo7
IntegraçãoentreSistemasusandoo
VRaptor
Completamosonossocadastrodelivros,comtodasasvalida çõesnecessáriaspara
conseguirmosvendê-lossemproblemas.Essapartedosistemaseráinstaladanuma
redeprotegida,comacessorestritoàspessoasquepodemcadastraroslivros.
Asegundapartedonossosistemaéapartequevaivenderoslivroscadastrados,
ositedalivraria.Essapartedosistemaseráinstaladaemoutroservidor,ecuidará
apenasdaapresenta çãodoslivrosparaacompra.Paraisso,elaprecisarádosdados
doslivroscadastradospeloadmindosistema.
Existemdiversasformasdeintegraressesdoissistemas,desdejogararquivos
numapastadaredeatéusarWebServices,eessaintegra çãodependemuitodecomo
ossistemasforamimplementados. Nonossocaso,comoosdoissistemasusam
VRaptor,existeumaformamaisnatural. Antesdefalarsobreela,vamosvercom
maisdetalhescomoseráessaintegra ção.

## Página 94

CasadoCódigo
Nossosdoissistemassãoo livraria-admin,quecuidarádocadastrodoslivros,
eo livraria-site,quemostraráoslivrosnumsiteparavendê-los.O livraria-sitenão
teráacessoaobancodedados,logo,paraconseguirosdadosdoslivrosteráquecon-
sultaro livraria-admin.Comisso,conseguimosevoluirasduaspartesdosistemain-
dependentemente,tantonocódigoquantonodeploy.Aoatualizaro livraria-admin
nãoprecisamosreiniciaro livraria-siteevice-versa.
Alémdisso,osdoissistemastêmrequisitosdiferentes.O livraria-siteseráaces-
sadopormilharesdepessoasaomesmotempo,enquantoo livraria-adminserá
acessadoapenasporalgumaspessoasquetêmacessoaocadastro.O livraria-admin
precisadeacessoaobancodedados,deumambientetransacional,decontrolede
acesso,enquantoo livraria-siteficaráabertoaopúblicogeral,servindopáginasque
mostramoslivroseguardandooscarrinhosdecomprasdosusuários.Sãorespon-
sabilidadesbemdiferentesquedeveriamserfeitasporsistemasdiferentes.
Ograndeproblemaagoraé: comopassarosdadosdoslivrosdeumsistema
paraooutro? OVRaptoréumframeworkWeb,quenospossibilitaexecutarope-
raçõesdentrodosistemaapartirdeURLsnonossonavegador. Porexemplo,ao
acessarhttp://localhost:8080/livraria-admin/livros/listacaímosnométodo lista
do LivrosController.Aofinaldométodo,émostradaumapáginaquefoige-
radaapartirdo /WEB-INF/jsp/livros/lista.jsp.Opontodepartidaéuma
requisiçãoaumaURLquecome çacom http://,ouseja,estamosusandoumproto-
colochamadoHTTP.
Emgeral,usamosbastanteesseprotocoloquandoestamosnavegandonainter-
net,juntocomasuaversãomaissegura,oHTTPS,paraacessarmospáginasdossites
quevisitamos.Noentanto,podemosusaromesmoHTTPparaacessaroutrosda-
86

## Página 95

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
dos,alémdepáginasWeb,comoimagens,arquivosparadownload,músicas,enfim,
qualquerdadorelevanteparanós.
Usando o protocolo HTTP podemos disponibilizar os dados dos livros no
livraria-admin. Paraisso,precisamoscriarumaURLqueexecutaráumcódigoe
nosdaráessesdadosqueprecisamos. OjeitodefazerissonoVRaptorécriarum
métodonumcontroller:
@Resource
public class IntegracaoController {
public void listaLivros() {
// ...
}
}
TemosaURL /integracao/listaLivrosqueexecutaráométodoe,por
padrão,redirecionaráparaojspcorrespondente.Geralmenteusamosjspsparacriar
páginasHTML,masnessecasoqueremosretornarapenasosdadosdoslivros.Oque
significaretornarosdadosdoslivros?Essesdadosprecisamserpassadosdealguma
formaparaooutrosistema.
Nomundoideal,poderíamospassaruma List<Livro>deumsistemaparao
outro.Porém,essalistaéumobjetoqueresidenamemóriadoservidordo livraria-
admin,enãoépossívelpassarexatamenteesseobjetoparao livraria-site,queé
outraaplica ção,estáemoutroservidor,emoutraJVM.
7 . 1 S erializando os objetos
Senãopodemospassaromesmoobjetodeumladoparaooutro,omelhorque
podemosfazeréextrairosdadosdoobjetoemumformatoqualquereleressesdados
nooutrosistema,transformando-osdevoltaemobjetos.Chamamosesseprocesso,
respectivamente,deserializa çãoedeserializa çãodoobjetoemquestão. Parafazer
isso,precisamosdefinirumformatoqueasduasaplica çõesentendameconsigam
escrevereleroobjeto.
Oformatopodeserqualquercoisa,porexemplo,umarquivotextoformatado
posicionalmente,umarquivobinárionumformatoquevocêmesmoinventououo
objetoserializadocomopróprioJava(com Serializablese Objectstreams).
Umformatobom,noentanto,éumformatoquesejasuportadofacilmentenosdois
sistemas,depreferênciasemquesejaprecisoescrevero parserdesseformato.Melhor
87

## Página 96

7.1. Serializandoosobjetos CasadoCódigo
aindasepuderserconsumidoemqualquerlinguagemdeprograma ção,assimfica-
ríamoslivresparaescreverositecomobementendermos,comoem Ruby on Rails,
Playno Scalaou A S P.
UmdosformatosqueatendeissobeméobomevelhoXML.Conseguimosler
egeraresseformatoemqualquerlinguagemdeprograma çãoquesejausávelem
projetosdeverdade.UmlivrorepresentadoemXMLseriaalgoparecidocom:
<livro>
<isbn>85-336-0292-8</isbn>
<titulo>O Senhor dos Anéis </titulo>
<autor>J. R. R. Tolkien </autor>
<preco>130.00</preco>
</livro>
Porserumformatotãoconhecidoeusado,oVRaptorpossuiumaformafácilde
serializarqualquerobjetoemXML.Oquequeremosémudaroresultadopadrãoe
geraroXML,entãousamoso Result:
@Resource
public IntegracaoController {
private Estante estante ;
private Result result ;
public IntegracaoController(Estante estante , Result result ) {
this.estante = estante;
this.result = result;
}
public void listaLivros() {
List<Livro> livros = estante.todosOsLivros();
result.use(Results.xml()).from(livros, "livros").serialize();
}
}
Assim,aoacessarmosaURL /integracao/listaLivros,nãoveremosmais
umapáginaHTML,esimumXMLparecidocom:
<livros>
<livro>
88

## Página 97

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
<id>1310</id>
<isbn>85-336-0292-8</isbn>
<titulo>O Senhor dos Anéis </titulo>
<autor>J. R. R. Tolkien </autor>
<preco>130.00</preco>
</livro>
<livro>
<id>42</id>
<isbn>9789728839130</isbn>
<titulo>O Guia dos Mochileiros das Galáxias </titulo>
<autor>Douglas Adams </autor>
<preco>90.00</preco>
</livro>
</livros>
Explicandoumpoucomelhorachamada:
// Usar como resultado um xml
result.use(Results.xml())
// a partir do objeto livros, com o nome "livros"
.from(livros, "livros")
// serializa o objeto e joga na resposta.
.serialize();
Essemétodo serialize()podeparecerumpoucoestranhonumprimeiro
momento,masexiste,poisoVRaptortemumaconven çãoparaserializaroobjeto.
Porpadrão,sósãoserializadosatributossimplesdoobjeto,comonúmeros,datas,
enumseStrings.Seoobjetotiveralgumatributoqueseja,porexemplo,umoutro
objetodaaplica çãoouumalista,paraserializarmosesseobjetoprecisamosexplici-
tamenteincluí-lonaserializa ção.Porexemplo,setivermosaclasse Autor:
enum Pais { BRASIL, ESTADOS_UNIDOS, REINO_UNIDO }
class Autor {
private String nome ;
private Calendar dataNascimento ;
private Integer numeroDeLivros ;
private Pais naturalidade ;
private List<Livro> livros;
private Livro ultimoLivro ;
89

## Página 98

7.1. Serializandoosobjetos CasadoCódigo
}
Aoserializarmosumautordaformapadrão:
Autor autor = // busca do banco
result.use(Results.xml()).from(autor).serialize();
Sóserãoserializadososatributossimples:
<autor>
<nome>J. R. R. Tolkien </nome>
<dataNascimento>1892-01-03</dataNascimento>
<naturalidade>REINO_UNIDO</naturalidade>
</autor>
Sequisermosserializar, porexemplo, oúltimolivro, precisamospedirpara
incluí-lo:
result.use(Results.xml()).from(autor).include("ultimoLivro").serialize();
Assim,aserializa çãoficaria:
<autor>
<nome>J. R. R. Tolkien </nome>
<dataNascimento>1892-01-03</dataNascimento>
<naturalidade>REINO_UNIDO</naturalidade>
<ultimoLivro>
<id>233</id>
<isbn>85-336-1165-X</isbn>
<titulo>Silmarillion</titulo>
<autor>J. R. R. Tolkien </autor>
<preco>13.00</preco>
</ultimoLivro>
</autor>
A regra de somente serializar atributos simples vale para o objeto incluído
também, ouseja, oúltimolivrosóteráosatributossimples. Sequisermosin-
cluir um atributo específico do livro, fazemos.include("ultimoLivro",
"ultimoLivro.umAtributo")Sequisermos,também,serializaralistadelivros
desseautor,incluímosocamporespectivo:
90

## Página 99

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
result.use(Results.xml()).from(autor)
.include("ultimoLivro", "livros").serialize();
Aserializa ção:
<autor>
<nome>J. R. R. Tolkien </nome>
<dataNascimento>1876-04-05</dataNascimento>
<naturalidade>REINO_UNIDO</naturalidade>
<livros>
<livro>
<id>233</id>
<isbn>85-336-1165-X</isbn>
<titulo>Silmarillion</titulo>
<autor>J. R. R. Tolkien </autor>
<preco>13.00</preco>
</livro>
<livro>
<id>1310</id>
<isbn>8533613377</isbn>
<titulo>O Senhor dos Anéis - A sociedade do anel </titulo>
<autor>J. R. R. Tolkien </autor>
<preco>60.00</preco>
</livro>
<!-- outros livros -->
</livros>
<ultimoLivro>
<id>233</id>
<isbn>85-336-1165-X</isbn>
<titulo>Silmarillion</titulo>
<autor>J. R. R. Tolkien </autor>
<preco>13.00</preco>
</ultimoLivro>
</autor>
Umaoutrapossibilidadeépedirparaserializaraárvoreinteiradeobjetos,ou
seja,todososatributos,recursivamente,comométodo recursive:
result.use(Results.xml()).from(autor).recursive().serialize();
Nadaseráexcluídodaserializa ção.Muitocuidado,poisissopodegerarrespostas
gigantesepesadas:
91

## Página 100

7.1. Serializandoosobjetos CasadoCódigo
<autor>
...
<ultimoLivro>
...
<editora>
...
<colecoes>
<colecao>
...
<lojas>
...
...
</lojas>
</colecao>
</colecoes>
</editora>
</ultimoLivro>
</autor>
Oupior,seexistisseumciclonessaárvoredeobjetos,porexemplo,seolivro
tivesseumareferênciaparaoautor,arecursãoseriainfinita:
<autor>
<name>J. R. R. Tolkien </name>
...
<ultimoLivro>
<name>Senhor dos Anéis </name>
...
<autor>
<name>J. R. R. Tolkien </name>
...
<ultimoLivro>
<name>Senhor dos Anéis </name>
...
<autor>
<name>J. R. R. Tolkien </name>
...
<ultimoLivro>
<name>Senhor dos Anéis </name>
...
Paraevitarisso,aconteceráumerrocasoexistaumciclonaárvoredeobjetos.
92

## Página 101

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
Emtodocaso,pensemuitobemantesdeusaro .recursive(),poisaresposta
podeficarmaiorqueonecessário.Casoaconfigura çãodoXMLfiquemuitocom-
plicada,considerecriarumaclassequeexpõesomenteosdadosquevocêquerse-
rializar—umDTO(DataTransferObject,dolivroPoEAAdoMartinFowler,ou
http://martinfowler.com/eaaCatalog/dataTransferObject.html).
Voltandoaoresultadoanterior,semo recursive(),cadalivropossuionome
doautor,queéumpoucoredundante,jáqueestamosserializandoolivro.Sequiser-
mosremoveroatributo autordaserializa ção,podemosusarométodo .exclude:
result.use(Results.xml())
.include("ultimoLivro")
.exclude("ultimoLivro.autor")
.serialize();
Assim,arespostaficaria:
<autor>
<nome>J. R. R. Tolkien </nome>
<dataNascimento>1876-04-05</dataNascimento>
<naturalidade>REINO_UNIDO</naturalidade>
<ultimoLivro>
<id>233</id>
<isbn>85-336-1165-X</isbn>
<titulo>Silmarillion</titulo>
<preco>13.00</preco>
</ultimoLivro>
</autor>
7 . 2 R ecebendo os dados no sistema cliente
Umadasvantagensdeexporumservi çodamaneiraacimaéqueoclientedesse
serviçopodeserqualquertipodesistema,escritoemqualquerlinguagemdepro-
gramaçãocomaqualépossívelexecutarumarequisi çãoHTTPeconsumirXML.
EcomoHTTPéumdosprotocolosmaisusadoseXMLéumdosformatosmais
adotados,praticamentetodasaslinguagensdeprograma çãosaberãotrabalharcom
eles.
Nonossocaso,osistemaclienteseráumaaplica çãoJavatambémescritausando
oVRaptor:o livraria-site.Antesdecome çaraintegra ção,vamosescreverapágina
inicialdosite,quemostraráoslivrosnumavitrine.Noprojeto livraria-site,vamos
criaro HomeController:
93

## Página 102

7.2. Recebendoosdadosnosistemacliente CasadoCódigo
@Resource
public class HomeController {
public void inicio() {
}
}
Precisamosmostrarnapáginadessalógicaumalistadelivros,queserácon-
sumidadoservi çodo livraria-admin. Devemoscolocarocódigoqueconsomeo
serviçodentrodométodo inicio? Precisaremostambémdedadosdelivrosna
páginaquemostraolivro,napáginadocarrinhodecompras,napáginadefinaliza-
çãodacompraeemváriasoutras,entãonãovaleapenarepetiressecódigoportodo
canto.
Paraevitaressarepeti ção,vamoscriarumcomponentedosistemaresponsável
poracessarosdadosdoslivros,comofizemosno livraria-admin,um repositóriode
livros.Adiferen çaéque,agora,oacessoaosdadossedápeloservi çodisponibilizado
pelo livraria-admin,enãopelobancodedados. Podemosusaraqui,também,a
Estante,nossorepositóriodelivros.Masparanãocausarconfusões,vamosusar
outraabstra çãoparaumconjuntodelivros: um A c e r v o,quenosdaráacessoaos
livrosdosistema,queestãocadastradosno livraria-admin.
Vamoscriarainterface Acervonoprojeto livraria-site.
public interface Acervo {
List<Livro> todosOsLivros();
}
Precisamostambémtero Livrodoladodosite,jáquetrabalhamoscomobje-
tos,enãocomXMLs,norestodosistema.Aclasse Livronãoprecisasernecessari-
amenteidênticanosdoissistemas,jáquealgunsdadospodemnãofazersentidopara
osite,porexemplo,seguardássemospre çodecusto,margemdelucro,quantidade
emestoqueououtrascoisas. Nonossocaso,podemoscopiaraclasse Livrodo
adminparaosite,jáquevamosusartodososdadosdolivro.Podemos,noentanto,
removerasanota çõesdaJPA,jáquenãovamossalvá-lonobancodedados.
Podemosagoraimplementara homedosite,disponibilizandoalistadelivros
paraajsp:
94

## Página 103

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
@Resource
public class HomeController {
private Acervo acervo ;
private Result result ;
public HomeController(Acervo acervo , Result result ) {
this.acervo = acervo;
this.result = result;
}
public void inicio() {
this.result.include("livros", acervo.todosOsLivros());
}
}
E no JSP padrão ( WEB-INF/jsp/home/inicio.jsp dentro de
livraria-site/src/main/webapp) acrescentar em alguma parte a lista
doslivros:
<h3>Veja as últimas ofertas para você: </h3>
<ul class="livros">
<c:forEach items="${livros}" var="livro">
<li class="livro">${livro.titulo} - R$ ${livro.preco} </li>
</c:forEach>
</ul>
7 . 3 C onsumindo os dados do admin
Comapáginainicialimplementada,precisamosagoraalimentá-lacomosdados
doslivros,quevirãodo livraria-admin.Precisamosimplementaro Acervoconsu-
mindoosservi çosdessesistema.Vamoscriaraclasse AcervoNoAdmin,comoum
componentequeimplementaa Acervo:
package br.com.casadocodigo.livraria.site.servico;
@Component
public class AcervoNoAdmin implements Acervo {
95

## Página 104

7.3. Consumindoosdadosdoadmin CasadoCódigo
@Override
public List<Livro> todosOsLivros() {
//...
}
}
A livraria-adminpossuiumservi çoquecriamospararetornaralistadetodos
oslivros.Esseservi çofoicriadousandooprotocoloHTTP,queéoqueusamosna
Web.Precisamosdealgoqueconsigaconsumirumservi çoHTTP,naURLquenos
retornaoXMLdoslivros.
Sepensarmosnosservi çosWebtradicionais,teríamosquecriarum endpointdo
serviço,queiagerarumdocumentocomtodasasopera çõespossíveise,naaplica ção
cliente,teríamosquecriarváriasclassesparaconseguirconsumiresseservi ço.
Nonossocaso,estamosusandoopróprioVRaptorpraexporesseservi ço, como
sefôssemosusá-lononavegador,usandooprotocoloHTTP.Paraisso,tudooque
precisamosédeumclienteHTTP,queexisteemqualquerlinguagemdeprograma-
çãoqueformosusar.EmJava,existeumjeitofácildefazerumarequisi çãoHTTPe
receberoresultado,usandoaclasse java.net.URL:
URL url = new URL("http://localhost:8080/livraria-admin" +
"/integracao/listaLivros");
InputStream resposta = url.openStream();
Ouseja, passandoaURLdoservi çoquenosretornaalistadelivros, con-
seguimos executar uma requisição a essa URL, recebendo a resposta como um
InputStream.Noentanto,muitascoisaspodemdarerradonomeiodocaminho.
Porexemplo,aURLpodeestarincorreta,podeestarapontandoparaumlugarque
nãoexiste,oservidorpodeestarforadoar,aredepodetercaídoetc.Poressemotivo,
ocódigoacimalan çaexce çõesqueprecisamsertratadas.
try {
URL url = new URL("http://localhost:8080/livraria-admin" +
"/integracao/listaLivros");
InputStream resposta = url.openStream();
} catch (MalformedURLException e ) {
e.printStackTrace();
} catch (IOException e ) {
e.printStackTrace();
}
96

## Página 105

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
Esseéumcódigodemuitobaixonívelparaestarno Acervo,queéumaabstra-
çãodealtonível,entãovamoscriarumcomponenteparanosajudarafazerrequisi-
çõesHTTP,retornando-nosuma Stringcomaresposta.Essecomponenteseráo
ClienteHTTP,comaimplementa çãousando URL.
package br.com.casadocodigo.livraria.site.servico;
public interface ClienteHTTP {
String get(String url );
}
@Component
public class URLClienteHTTP implements ClienteHTTP {
@Override
public String get(String url ) {
try {
URL servico = new URL(url);
InputStream resposta = servico.openStream();
} catch (MalformedURLException e ) {
e.printStackTrace();
} catch (IOException e ) {
e.printStackTrace();
}
}
}
Precisamosagoraconverteressarespostade InputStreampara String.Exis-
temváriosjeitosdefazerisso,emváriasbibliotecasdiferentes.Vamosusaraclasse
com.google.common.io.CharStreams,dabiblioteca G o o g l e G u a v aque já é
dependênciadoVRaptorecontémváriosutilitáriosquemelhoramváriosaspec-
tosdoJava.Essaclasseconseguetransformarum Readernuma String,epara
transformaro InputStreamnum Readerusamoso InputStreamReaderdo
própriojava.
Reader reader = new InputStreamReader(resposta);
String respostaEmString = CharStreams.toString(reader);
Integrandocomorestodocódigo,ficaria:
public String get(String url ) {
try {
97

## Página 106

7.3. Consumindoosdadosdoadmin CasadoCódigo
URL servico = new URL(url);
InputStream resposta = servico.openStream();
Reader reader = new InputStreamReader(resposta);
return CharStreams.toString(reader);
} catch (MalformedURLException e ) {
e.printStackTrace();
} catch (IOException e ) {
e.printStackTrace();
}
}
Esse código ainda não compila, pois precisamos decidir o que fazer caso
ocorram exceptions. Temos dois tipos deException sendo lançadas aqui:
MalformedURLException—quandoaurlnãoéválida, e IOException—
quandoaconteceualgumerrodecomunica çãocomoservidordurantearequisi ção.
A MalformedURLException,nonossocaso,seriaculpadoprogramador,
já que as urls vão vir do código, logo podemos supor que elas só vão aconte-
ceremtempodedesenvolvimentoesimplesmentealan çarmosdentrodealguma
RuntimeException.
} catch (MalformedURLException e ) {
throw new IllegalArgumentException("A url " + url +
" está inválida, corrija-a!" , e);
}
Já aIOExceptionfogedonossocontrolee,sefazpartedonossoprocesso
serecuperardealgumaformacasooservidorestejaforadoar,precisamosdeixar
issonocontratodonossoclientehttp,ouseja,dainterface ClienteHTTP.Lan çar
IOExceptiontalvezsejagenéricodemais—podemosoptarporcriarumaexce ção
maisespecífica,como ServidorIndisponivelException:
public class ServidorIndisponivelException extends RuntimeException {
public ServidorIndisponivelException(String url , Exception e ) {
super("Erro ao fazer requisição ao servidor na url " + url, e);
}
}
public interface ClienteHTTP {
public String get(String url ) throws ServidorIndisponivelException;
}
98

## Página 107

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
Enahoradefazero catch,usamosanossaexce ção:
} catch (IOException e ) {
throw new ServidorIndisponivelException(url, e);
}
A ServidorIndisponivelException está comoRuntimeException
paranãoobrigarmosousuáriodo ClienteHTTP atratá-la. Masdeixamosa
exceção declarada na interface, para que o usuário saiba que tem a opção de
se recuperar desse caso específico. Se quisermos obrigar a sempre tratar esse
caso, trocamos o extends para Exception, mas cuidado que isso pode
gerar muitos métodos que, ou relançam essa exceção declarando o throws
ServidorIndisponivelException,oufazemum try..catchrelançandoa
exceçãodentrodeuma RuntimeException,quetornamocódigobemchatode
mantereevoluir.
7 . 4 T ransformando o XML em objetos
Com o nosso ClienteHTTP implementado, agora nosso código da
AcervoNoAdminestáassim:
@Component
public class AcervoNoAdmin implements Acervo {
private ClienteHTTP http ;
public AcervoNoAdmin(ClienteHTTP http ) {
this.http = http;
}
@Override
public List<Livro> todosOsLivros() {
String url = "http://localhost:8080/livraria-admin" +
"/integracao/listaLivros";
String resposta = http.get(url);
return null ;
}
}
99

## Página 108

7.4. TransformandooXMLemobjetos CasadoCódigo
ArespostaseráumXMLparecidocom:
<livros>
<livro>
<id>1310</id>
<isbn>8533613377</isbn>
<titulo>O Senhor dos Anéis </titulo>
<autor>J. R. R. Tolkien </autor>
<preco>130.00</preco>
</livro>
<livro>
<id>42</id>
<isbn>9789728839130</isbn>
<titulo>O Guia dos Mochileiros das Galáxias </titulo>
<autor>Douglas Adams </autor>
<preco>90.00</preco>
</livro>
</livros>
Precisamosagoraleressaresposta,quecontémumXMLcomalistadelivros,e
transformá-laemobjetos List<Livro>,parapodermosusaressesdadosnores-
tantedosistema.Existemváriasbibliotecasquefazemissoparanós,umadelaséo
XStream,quejávemcomodependênciadoVRaptoreéabibliotecaqueeleusapara
gerareconsumirXMLs(eJSONs).AideiadoXStreaméqueelesejabemsimples
deusar,comomínimodeconfigura ções.
XStream xstream = new XStream();
Object object = xstream.fromXML(resposta);
A conven ção do XStream para conseguir deserializar a resposta
em um objeto é que o nó raiz tenha o nome da classe, ou seja, se
quisermos deserializar um Livro, o nó raiz do XML deveria ser
<br.com.casadocodigo.livraria.modelo.Livro>. A partir daí, sem-
prequepossível,eletentausarosatributosdosobjetoscomonomesdastags.
ParaconseguirconsumiroXMLqueoVRaptorgerou,precisamosconfigurar
issonoXStream,falandoqueonóraiz <livros>éumalistaequeonódecada
elementodalista, <livro>,éum Livro.Fazemosissocomométodo alias:
XStream xstream = new XStream();
xstream.alias("livros", List.class);
xstream.alias("livro", Livro.class);
100

## Página 109

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
Ao pedirmos para o XStream consumir o XML, temos como resposta uma
List<Livro>:
List<Livro> livros = ( List<Livro>) xstream.fromXML(xml);
Nossométodocompletoficaria:
@Override
public List<Livro> todosOsLivros() {
String xml = http.get("http://localhost:8080/livraria-admin" +
"/integracao/listaLivros");
XStream xstream = new XStream();
xstream.alias("livros", List.class);
xstream.alias("livro", Livro.class);
List<Livro> livros = ( List<Livro>) xstream.fromXML(xml);
return livros;
}
Comisso,seconhecermosaURLdalógicadoadminqueretornaalistadeli-
vros,conseguimososdadosdoslivrosnovamenteemobjetosjavae,então,podemos
trabalharcomelesnormalmentenorestodosistema.
7 . 5 A proveitando melhor o protocolo HTTP - REST
Quandopensamosemservi çoswebtradicionais,os Web Services SOAP,paracada
operaçãoqueoservidorsuportar,énecessáriocriarpelomenos4classesnocliente,
semcontarasclassesdemodelointermediáriasqueserãotrafegadasdeumsistema
paraooutro. Issoporqueprecisamosensinaroclienteafazercadaumadasope-
rações,qualéoformatodeentrada,qualéoformatodesaída,entreoutrascoisas.
TudoissoédefinidodentrodeumdocumentochamadodeWSDL(siglaparaWeb
ServicesDescriptionLanguage).
Jánonossocaso,estamosusandooprotocoloHTTPparaimplementaroservi ço,
enãoprecisamoscriarclassesparaensinarosistemaclienteaexecutarumaopera ção
nosistemaservidor.TudooqueprecisamosfoideumclienteHTTP.Issoacontece
porqueoHTTPjádefineumconjuntopequenodeopera çõespossíveisdentrodesse
protocolo.
101

## Página 110

7.5. AproveitandomelhoroprotocoloHTTP-REST CasadoCódigo
Comisso,bastaqueoclientesaibaexecutaressasopera çõeseoservidorsaiba
entenderessasopera çõesfixase,assim,nenhumaclassedeinfraestruturaéneces-
sáriaparaqueumsistemasecomuniquecomooutro.Apesardeesseconjuntode
operaçõesserpequeno,sãoopera çõesuniversais,quesãosuficientesparaimplemen-
tarmosqualquertipodeservi ço.Essasopera ções,tambémchamadasdemétodoou
verbo,são: GET, POST, PUT, DELETE, HEAD, OPTIONS, TRACEe,recentemente,
P A T C H.
Mascomorepresentaraopera çãodelistartodososlivrosdosistema,sendoque
eusótenhoesses8métodosHTTPdisponíveis?AideiadoHTTPéqueessesmé-
todosdevemserobrigatoriamenteexecutadosemum recurso,queéqualqueren-
tidade,dadooupersonagemdosistema.EsserecursoérepresentadoporumaURI
(Unified Resource Identifier,ouidentificadorúnicodeumrecurso).UmaURLéum
tipodeURI,quetambémrepresentaqualéolocalondepodemosencontrarore-
curso(o Léde Location,ouseja,local).
Cadamétodotemumasemânticamuitobemdefinidapossibilitandoque,em
conjunçãocomumrecurso,consigamosrepresentarqualqueropera çãopossíveldo
nossosistema. Usamosdoisdessesmétodosconstantementeenquantonavegamos
naweb:o GET,aoclicarmosemlinksoudigitarmosendere çosdiretamentenona-
vegador,eo POST,aosubmetermosformulários. Aideiaéque,seusarmoscor-
retamenteassemânticasdosmétodos,podemosaproveitartodaainfraestruturada
internet,comoproxies,loadbalancerseoutrosintermediáriosentreoclienteeo
servidor.
AsemânticadosmétodosHTTPsão:
•GET—Retornaasinformaçõesdeumrecurso.Porexemplo, GET /livros
podedevolvertodososlivrosdosistema,e GET /livro/1234,asinforma-
çõesdolivrodeidiguala1234.EssemétodoNÃOPODEalteraroestadodo
recursoemquestãoeéidempotente,ouseja,podeserexecutadoquantasve-
zesfornecessáriosemqueissoafetearesposta.Usandoessefato,osproxies
podemfazero cachedaresposta,evitandoasobrecargadoservidor.Robôsde
buscapodemindexartodooconteúdodeumsiteseguindotodososlinksque
encontramnumapágina,jáqueelesexecutamométodoGETnaURLdolink,
enãoalteramnadanositeemquestão.
•POST—Acrescentainformaçõesemumrecurso.Porexemplo,aofazermos
um POST /livros,passandoosdadosdeumlivro,estamoscriandoum
livronovonosistema. Essemétodomodificaoestadorecursoemquestão,
102

## Página 111

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
podendocriarnovosrecursosenãoéidempotente,ouseja,sefizermosdois
POSTsem /livros,mesmoqueestejamospassandoosmesmosdados,cri-
aremosdoislivros.
•PUT — Substitui as informações de um recurso. Se fizermos PUT
/livro/1234, passandodadosdesselivro, atualizamososseusatributos.
Essemétodomodificaorecursoindicado,substituindoTODASassuasin-
formaçõespelaspassadasnocorpodarequisi ção.Seorecursonãoexistir,ele
poderásercriado.
•P A T C H—TemmesmasemânticadoPUT,excetoquepodemospassarapenas
apartedasinforma çõesquedesejamosalterarnorecurso,quedeveexistir.
Essemétodoémaisrecenteeaindanãoésuportadoemtodososservidores.
•DELETE—Removeorecurso.Porexemplo, DELETE /livro/321 remove
olivrodeid321.Tambéméumaopera çãoidempotente,ouseja,removerduas
vezesorecursodeveteromesmoefeitodefazerissoumaúnicavez.
•HEAD—ParecidocomoGET,masretornaapenasosheadersdaresposta.
•OPTIONS—Retornaasoperaçõespossíveise,possivelmente,algumasme-
tainformaçõesdorecurso.
•TRACE—parafazerDebugging.
PensandonaWeb“humana”,dificilmenteusamostodosessesmétodos,princi-
palmenteporque,pelaespecifica çãodoHTML,osnavegadoressósuportamosmé-
todos GETe POST.Masmesmousandoessesdoismétodosébastanteimportante
usarmosassuassemânticas: GETparaopera çõesquenãomodificamrecursos,e
POSTparaasquemodificam,assimosintermediáriospodemtrabalhardamaneira
correta.
OprotocoloHTTPvaimuitoalémdeapenasmétodoserecursose,seestamos
implementandoumservi çoqueusaascaracterísticasdoHTTPdizemosqueéum
serviçoREST(ouRESTfulwebservice).Issovaidesdeusarmétodoserecursosda
maneiracorretaatéfazernegocia çãodeconteúdoeusarhipermídia.Éumassunto
bastanteextenso,quenãoseráabordadoemdetalhesnesselivro,maspodemosdar
osprimeirospassosnessadire çãocomaajudadoVRaptor.
103

## Página 112

7.6. Usandométodoserecursosdamaneiracorreta CasadoCódigo
7 . 6 U sando métodos e recursos da maneira correta
QuandocriamosumcontrollernoVRaptor,existeumaconven çãoquegeraaURL
decadamétododessecontroller.Porexemplo,nonosso LivrosController:
@Resource
public class LivrosController {
public void lista() {...}
public void salva(Livro livro ) {...}
public void edita(String isbn ) {...}
}
AsURLsdosmétodos lista, salvaeeditaterminamem /livros/lista,
/livros/salvae /livros/edita,respectivamente.Ébastanteusualdarmosos
nomesdosmétodosdeumobjetousandoverbos,afinalestamosexecutandoa ções.
Mas,pensandoemREST,URLs(ouURIs)deveriamdenotarrecursos,quesãosubs-
tantivos,enãoverbos. Masseestamosusandosubstantivos,ondeficamasa ções?
Nosmétodos(ouverbos)HTTP.
Nométodo lista,estamosretornandoasinforma çõesdetodososlivros,então
orecursopodeser /livros.Alistanãoalteranadanosistema,portantoométodo
HTTPéo GET.ParaalterarmosaURLdeummétododocontroller,podemosusar
aanota ção @PathdoVRaptor:
@Path("/livros")
public void lista() {...}
Apartirdomomentoemquefazemosisso,aURL /livros/listajánão
correspondemaisaessemétodo,quedeveráseracessadopor /livrossomente.
Porpadrão,oVRaptoraceitaqualquerverboHTTPnosmétodos(mesmonosque
nãotemo @Path),logo,sequisermosindicarqueessemétodosópodeseracessado
via GET,usamosaanota ção @Get:
@Get @Path ("/livros")
public void lista() {...}
As anotaçõesdemétodosHTTPtambémrecebemaURIcomoparâmetro.Po-
demosfazersimplesmente:
@Get("/livros")
public void lista() {...}
104

## Página 113

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
Jáométodo salvaacrescentaum Livronovoaosistema,logonãopodemos
usaro GET.Orecursoaindaéalistadoslivrosdosistema,entãopodemosusar POST
/livrosparaacessaressemétodo. Assimcomotemoso @Getpararequisi ções
GET,usamoso @Postpararequisi ções POST:
@Post("/livros")
public void salva(Livro livro ) {...}
Reparequetantoométodo listaquantoométodo salvausamamesma
URI,masselecionamosqualmétodoseráinvocadodependendodométodoHTTP
darequisi ção.Nométodo editanãoestamosmaistratandodetodososlivrosdo
sistema,massimdeumlivroespecífico.PraindicarissonumaURI,precisamosque
elacontenhaumainforma çãoqueidentifiqueunicamenteolivro,nonossocaso,o
isbn.Essemétodomostraumformuláriocomosdadosdo Livroparaaedi ção,
entãonãoestamosalterandonadanosistema,ouseja,podemosusarométodo GET.
Comopodemoseditarqualquerumdoslivrosdosistema,precisamosdeuma
URIparacadaumdeles.NãoéviáveldeclararmostodasasURIspossíveisnométodo
docontroller.Precisamosdeclararum templatedeURIquevaicairnométodoedita,
ouseja,umaURIquecontémumavariávelnomeio,queseráoISBNdolivro.Para
declararumavariávelnomeiodeumaURInoVRaptorusamos {}comonomeda
variávelcapturadadentro.Nocasodométodoeditaficaria:
@Get("/livros/{isbn}")
public void edita(String isbn ) {...}
Dessemodo,aoacessarmosaURI /livros/12345,oVRaptorvaiinvocaro
métodoedita,capturandoovalor 12345navariável isbn.Comoométodorecebe
umparâmetrocomessenome,ovalor 12345serápassadoparaométodo.Como
o isbnfazpartedaURI,nãoépossívelinvocaressemétodoviaHTTPsempassar
um isbn,assimnãoprecisamosverificarseesseparâmetrofoipassadomesmona
requisição.Nossométodo editaestáassim:
@Get("/livros/{isbn}")
public void edita(String isbn ) {
Livro livroEncontrado = estante.buscaPorIsbn(isbn);
if (livroEncontrado == null) {
result.notFound();
} else {
result.include(livroEncontrado);
105

## Página 114

7.6. Usandométodoserecursosdamaneiracorreta CasadoCódigo
result.of(this).formulario();
}
}
Oqueacontecesepassarmosum isbn quenãoexiste, porexemplo GET
/livros/bazinga? Omundointeirojáconheceumarespostaapropriadapara
umendere çoquenãoexistenaWeb:afamosapágina404.Essenúmeronadamais
édoqueumdosstatuscodespossíveisdoprotocoloHTTP,esignificaqueorecurso
nãofoiencontrado.Éexatamenteonossocaso,porissoquesimplesmentepodemos
redirecionarparaapágina404dosistemacasoumlivrocomoISBNpassadonão
forencontrado,usandoométodo notFounddo Result.
Setivermosummétodo alteranocontroller,podemostambémrecebero
identificadordoobjetonaURI,jápopulandooobjeto,usandoamesmaconven ção
denomesqueadosparametrosdeformulário.Nessecaso,comoestamosalterando
osdadosdo Livro,podemosusarométodo PUT
@Put("/livros/{livro.isbn}")
public void altera(Livro livro ) {...}
Assimo livrovirácomo isbnpopuladocomovalorpassadonaURI,eo
restodosatributospopuladosusandoocorpodarequisi ção. Damesmaforma,se
quisermosremoverolivro,podemosusarométodo DELETE:
@Delete("/livros/{livro.isbn}")
public void remove(Livro livro ) {...}
PassandoapensarnasURIscomorecursosficamuitomaissimplesparaum
clientedosistemaconsumirosservi çosWeb.NãoémaisnecessárioconheceraURI
detodososmétodosdoservi ço,somenteconhecerasURIscorrespondentesaos
recursoséosuficiente.Sabendoquetemosorecurso /livros,oclientesabeque
GET /livros significaobterosdadosdoslivrose POST /livros significacriar
umlivronovo.Seorecursoéumlivroespecífico, /livros/1234,oclientesabe
queparaobterosdadosdolivrodeveusar GET,paraeditarosdadosdeveusar PUT
(ou PATCHseforeditarapenasalgunscampos)epararemoverolivrodeveusar
%DELETE.
106

## Página 115

CasadoCódigo Capítulo7. IntegraçãoentreSistemasusandooVRaptor
Alterando o link para a edição de livros
Nalistagemdelivrosestamosusandooseguintelink:
<a href="${linkTo[LivrosController].edita }?isbn=${livro.isbn}" >
Modificar
</a>
UsandoorecursodeumamaneiraREST,estamospassandooISBN
diretamentenaurl,enãocomoparâmetro.Nessecaso,podemospassar
parâmetrosparaométododocontrollerqueserãousadosnaforma ção
daurl.Fazemosissousandocolchetes,aoinvésdeparênteses:
<a href="${linkTo[LivrosController].edita[livro.isbn]}">
Modificar
</a>
Essapassagemdeparâmetrossóseráefetivaseeleforusadodireta-
mentenaURL.
Resolvendo conflitos de rotas
Ao criar a rota do método edita, usamos@Get("/livros/{isbn}”).
O problema é que a rota para o método formulário é, implicitamente,
@Path("/livros/formulario"), que também casa com o padrão
@Get("/livros/{isbn}”), com o ISBN valendoformulario. Isso, a
princípio, vai gerar um 404, pois se o método formulário não tem nada ano-
tado, a sua rota tem menos prioridade. Mas caso ele estivesse anotado com
@Get("/livros/formulario"),receberíamosumerro:
There are two rules that matches the uri '/livros/formulario'
with method GET:
[[FixedMethodStrategy: /livros/formulario LivrosController.formulario()
[GET]],
[FixedMethodStrategy: /livros/{isbn} LivrosController.edita(String)
[GET]]]
with same priority. Consider using @Path priority attribute.
Ouseja,elefalaqueométodo formularioeométodo editaconseguem
tratarauri /livros/formulario,comamesmaprioridade. Naúltimafrase,
107

## Página 116

7.7. UsandoRESTnonavegador CasadoCódigo
eledáadicadeusaroatributo prioritydaanota ção @Pathpararesolveressa
ambiguidade.Paraisso,devemosmudarométodoeditapara:
@Get @Path (value="/livros/{isbn}", priority=Path.LOWEST)
public void edita(String isbn ) {...}
Assim,essarotatemamenorprioridade,ea /livros/formularioseráusada
paraométodo formulariodocontroller. CasooISBNfosseumnúmero,essa
configuraçãonãoserianecessária:
@Get("/livros/{isbn}")
public void edita(Long isbn ) {...}
Nessecaso,comooVRaptorsabequeoISBNéumnúmero(Long),elesabe
que a última parte do caminho tem que conter apenas dígitos. Dessa forma,
/livros/1234cainométodoedita,mas /livros/abcddá404direto.
7 . 7 U sando REST no navegador
PensandoemRESTestamosfacilitandoavidadoclientequevaiconsumirosservi-
çosdanossaaplica ção.Masnemsempreessesclientessãooutrasaplica ções.Quando
umapessoaacessaosistemausandoumnavegador,elaéoclientedosistema,usando
onavegadorcomoclienteHTTP.Porisso,podemosaplicarasideiasdoRESTàWeb
humanatambém,paraimplementarmosasintera çõescomousuáriousandoHTML
ejavascript.
Umalimita çãofortedosnavegadoreséquesóconseguimosfazerrequisi ções
GETePOSTnativamente.Issosignificaque,sequisermosfazerumformuláriopara
alterarumlivro,nãoconseguimosfazer:
<form action="/livros/1234" method="PUT">
MasparasimularométodoPUT,oVRaptor(ealgunsoutrosframeworksWeb)
suportareceberumparâmetroamaisnarequisi çãoindicandoqualéométodoreal
quequeremosexecutar. NoVRaptor,devemosdeixaroformuláriocomoPOSTe
passarumparâmetrochamado _methodcomvalor PUT:
<form action="/livros/1234" method="post">
<input type="hidden" name="_method" value="PUT"/>
108

## Página 117

Capítulo8
DownloadeUploaddearquivos
8.1 E nviando arquivos para o servidor : Up l o a d
Quandoimplementamosocadastrodelivros,ficoufaltandoumaparteimportante
parapodermosmostraroslivrosnanossavitrinevirtual:acapadoslivros.Essacapa
seráumaimagemcujouploadvamosfazerparaoservidor,paradepoispodermos
baixá-la.
Paraisso,precisamoscolocarumcamponoformuláriodolivroparaincluirmos
acapa.Comoesseformuláriovaiconterumcampoparaupload,precisamosmudar
oenctypepara multipart/form-data.Alémdisso,criaremosocampodeupload
comoumatag <input>com type="file":
<form action="${linkTo[LivrosController].salva}"
method="post" enctype="multipart/form-data">
...
Capa: <input type="file" name="capa" />
...
</form>

## Página 118

8.1. Enviandoarquivosparaoservidor:Upload CasadoCódigo
Precisamosacrescentarabiblioteca commons-fileuploadea commons-io
paraqueoVRaptorconsigatrataruploadscorretamente.Seestivermosusandoum
servidorcompatívelcomServlet3,essasbibliotecaspodemnãosernecessárias.No
nossocaso,emqueestamosusandooivyparagerenciardependências,precisamos
acrescentarasseguinteslinhasnoivy.xmlerodaro ant resolve:
<dependency org="commons-fileupload" name="commons-fileupload"
rev="1.2.1" conf="default"/>
<dependency org="commons-io" name="commons-io"
rev="1.3.2" conf="default"/>
DoladodoController,pararecebermosacapa,precisamosacrescentarumpa-
râmetroamaisnométodo salva,comomesmonomedoinputecomotipo
UploadedFile:
public class LivrosController {
//...
@Post("/livros")
public void salva(Livro livro , UploadedFile capa ) {
}
}
Esse UploadedFilenosdáoconteúdodoarquivoealgumasinforma çõesque
podemosusarparasalvá-locorretamente:
capa.getFile(); // um InputStream com o conteúdo do arquivo
capa.getFileName(); // o nome do arquivo
capa.getContentType(); // o tipo do arquivo. Ex: image/png
capa.getSize(); // o tamanho do arquivo.
Parasalvaressearquivotemosmuitasop ções.Podemosescolherumapastado
servidoresalvartodasascapasnessapasta.Podemosusarumservidordearquivos
paraisso,comoumFTPouumservi çoexternocomooDropboxouoS3daAmazon.
Podemos,ainda,salvaressearquivodiretonobancodedados.Paranãosepreocupar
comissodoladodoController,vamoscriarumainterfaceresponsávelporsalvar
arquivos,o Diretorio,ondepoderemossalvarumaimagemerecuperá-ladepois.
110

## Página 119

CasadoCódigo Capítulo8. DownloadeUploaddearquivos
public interface Diretorio {
URI grava(Arquivo arquivo );
Arquivo recupera(URI chave );
}
Oquevamosgravaréum Arquivoqueguardaráoconteúdodoarquivojunto
comalgumasmetainforma çõesenosretornaráuma URI,identificandoolocalonde
oarquivofoiarmazenado.Pararecuperá-lo,bastapassaressa URI,querecebemos
devoltao Arquivogravado. Aclasse Arquivoconteráonomedoarquivo,o
conteúdo,otipoeadatademodifica ção:
public class Arquivo {
private String nome ;
private byte [] conteudo;
private String contentType ;
private Calendar dataModificacao ;
public Arquivo(String nome , byte[] conteudo, String contentType ,
Calendar dataModificacao ) {
this.nome = nome;
this.conteudo = conteudo;
this.contentType = contentType;
this.dataModificacao = dataModificacao;
}
//getters
}
Assim,podemosrecebero Diretorionoconstrutordo LivrosController
eguardaroarquivo,salvandoa URIdaimagemno Livro:
public LivrosController(Estante estante , Diretorio imagens ,
Result result , Validator validator ) {
this.estante = estante;
this.imagens = imagens;
this.result = result;
this.validator = validator;
111

## Página 120

8.1. Enviandoarquivosparaoservidor:Upload CasadoCódigo
}
@Transacional
@Post("/livros")
public void salva(final Livro livro , UploadedFile capa )
throws IOException {
validator.validate(livro);
validator.onErrorRedirectTo(this).formulario();
if (capa != null) {
URI imagemCapa = imagens.grava(new Arquivo(
capa.getFileName(),
ByteStreams.toByteArray(capa.getFile()),
capa.getContentType(),
Calendar.getInstance()));
livro.setCapa(imagemCapa);
}
estante.guarda(livro);
result.include("mensagem", "Livro salvo com sucesso!" );
result.redirectTo(this).lista();
}
Paraconseguirmossalvarcorretamentea URIno Livro,vamosadaptá-lapara
salvarcomo String,usandoogettereosetter:
public class Livro {
//...
private String capa ;
public URI getCapa() {
if (capa == null) return null ;
return URI.create(capa);
}
public void setCapa(URI capa ) {
this.capa = capa == null ? null : capa.toString();
}
}
112

## Página 121

CasadoCódigo Capítulo8. DownloadeUploaddearquivos
Parasalvardefatoaimagemdacapa,precisamosdeumaimplementa çãoreal
do Diretorio. Paraquenãosejanecessáriocriarumainfraestruturaadicio-
nal,vamosusarobancodedadosparasalvarosdadosdaimagem. Criaremoso
DiretorioNoBDque,parafuncionar,éprecisoadaptaraclasse Arquivoparavi-
rarumaentidade:
@Entity
public class Arquivo {
@Id @GeneratedValue
private Long id ;
@Lob
private byte [] conteudo;
// para a JPA não reclamar
Arquivo() {}
// resto dos campos e getters
}
@Component
public class DiretorioNoBD implements Diretorio {
private EntityManager manager ;
public DiretorioNoBD(EntityManager manager ) {
this.manager = manager;
}
@Override
public URI grava(Arquivo arquivo ) {
return null ;
}
@Override
public Arquivo recupera(URI chave ) {
return null ;
}
}
113

## Página 122

8.1. Enviandoarquivosparaoservidor:Upload CasadoCódigo
Paraimplementarométodo grava,vamossalvaroarquivonobancodedados.
A URIquevamosadotarcomorespostaserádotipo bd://<id da imagem no
bd>,afinal,estamosgravandooarquivonobancodedados. Assim,seoarquivo
tiveroid1234,a URIserábd://1234.Ométodo gravaficaria:
@Override
public URI grava(Arquivo arquivo ) {
manager.persist(arquivo);
return URI.create("bd://" + arquivo.getId());
}
Comisso,podemosacessaroformuláriodelivrosecadastraracapaparaalgum
deles.
114

## Página 123

CasadoCódigo Capítulo8. DownloadeUploaddearquivos
Bug no VRaptor 3.4.0 a t é3.5.1
SevocêusaoVRaptornasversõesentre3.4.0e3.5.1comoGuicecomo
containerdedependências,podeserquevocêrecebaumerroaofazerum
upload,falandoquenãoépossívelencontrarumconverterparaainter-
face UploadedFile. Pararesolveresseproblema,atualizeparauma
versãomaiorouigualà3.5.2,oucrieaseguinteclassenasuaaplica ção:
@Convert(UploadedFile.class)
public class UploadedFileConverter implements
Converter<UploadedFile> {
private HttpServletRequest request ;
public UploadedFileConverter(HttpServletRequest request ) {
this.request = request;
}
@Override
public UploadedFile convert(String value ,
Class<? extends UploadedFile> type,
ResourceBundle bundle ) {
return type.cast(request.getAttribute(value));
}
}
8.2 R ecuperando os arquivos salvos : Download
Sequisermosmostraracapadolivronalistagem,precisamosconseguiroconteúdo
daimagemapartirda URIquesalvamos. NoHTML,paramostrarumaimagem
usamosatag img:
<img src="<url da imagem>" />
PrecisamosdeumaURLdaaplica çãoquenosretorneacapadolivroedeum
métododecontrollerquevairetornaraimagem.Vamos,então,criarométodo capa
no LivrosController,respondendopela URL /livros/<isbn>/capa:
115

## Página 124

8.2. Recuperandoosarquivossalvos:Download CasadoCódigo
@Get("/livros/{isbn}/capa")
public void capa(String isbn ) {
Livro livro = estante.buscaPorIsbn(isbn);
// retorna a imagem
}
Agora, para retornar os dados da imagem, não basta incluir a imagem no
result.Precisamosquearespostainteiradarequisi çãosejaaimagem.Paraisso,
precisamosfazero Downloaddaimagem.ParafazerumDownloadusandooVRap-
tor,precisamosqueométodoretorneainterface Download:
public Download capa(String isbn ) {
Existemalgumasimplementa çõesde Downloadquepodemosusar,deacordo
comoquetemosemmãos.Nonossocaso,temosaclasse Arquivo,queprecisamos
recuperarusandoa URIsalvanolivro:
@Get("/livros/{isbn}/capa")
public Download capa(String isbn ) {
Livro livro = estante.buscaPorIsbn(isbn);
Arquivo capa = imagens.recupera(livro.getCapa());
}
O Arquivonosdáoconteúdousandoum byte[],portantopodemosusar
aimplementa ção ByteArrayDownloadque,alémdo byte[],tambémrecebeo
contenttypeeonomedoarquivo:
@Get("/livros/{isbn}/capa")
public Download capa(String isbn ) {
Livro livro = estante.buscaPorIsbn(isbn);
Arquivo capa = imagens.recupera(livro.getCapa());
return new ByteArrayDownload(capa.getConteudo(),
capa.getContentType(), capa.getNome());
}
Precisamosimplementarométodo recuperadonossodiretóriodeimagens,
recuperandooarquivo,dadaa URI.Paraisso,podemosverificarseaURIédebanco
dedadosebuscaro Arquivodobancopeloid:
116

## Página 125

CasadoCódigo Capítulo8. DownloadeUploaddearquivos
@Override
public Arquivo recupera(URI chave ) {
if (chave == null) return null ;
// scheme é o protocolo. No caso de bd:// é o bd
if (!chave.getScheme().equals("bd")) {
throw new IllegalArgumentException(chave +
" não é uma URI de banco de dados" );
}
// authority é o que vem depois do bd://
Long id = Long.valueOf(chave.getAuthority());
return manager.find(Arquivo.class, id);
}
Assim,podemosmodificaralistagemdelivrosparaincluiracapa:
<c:forEach items="${livroList}" var="livro">
<li>
<img src="${linkTo[LivrosController].capa[livro.isbn] }"
width="70" height="100">
${livro.titulo} - ${livro.descricao} -
<a href="${linkTo[LivrosController].edita[livro.isbn] }" >
Modificar
</a>
</li>
</c:forEach>
Apesardeatelarenderizarsemproblemas,seolharmosologdoservidor,vere-
mosvárioserrosdotipo:
Caused by: java.lang.NullPointerException
at br.com.casadocodigo.livraria.controlador.
LivrosController.capa(LivrosController.java:89)
117

## Página 126

8.3. OutrasimplementaçõesdeDownload CasadoCódigo
Issoporquealgunslivrosnãopossuemcapa,logo,oarquivoretornadopelo
DiretorioNoBDvemnulo.Paraevitaresseserros,podemosretornarqueaimagem
nãoexistenocontroller,ouseja,retornarum404:
@Get("/livros/{isbn}/capa")
public Download capa(String isbn ) {
Livro livro = estante.buscaPorIsbn(isbn);
Arquivo capa = imagens.recupera(livro.getCapa());
if (capa == null) {
result.notFound();
return null ;
}
return new ByteArrayDownload(capa.getConteudo(),
capa.getContentType(), capa.getNome());
}
Nocasodemudarmosoresult,podemosretornar nullparabloquearodown-
load.Dessaforma,apáginarenderizasemproblemas,eoconsoledoservidorfica
semerros.
8.3 O utras implementações de Download
Além da implementação ByteArrayDownload, que consegue gerar um
Download a partir de um byte[], temos implementações que usam
InputStream e File para gerar o Download. Todas elas possuem um
construtorquerecebeoconteúdo,ocontentTypeeonomedoarquivo:
byte[] capa = //...
return new ByteArrayDownload(capa, "image/png", "capa.png");
InputStream relatorio = //...
return new InputStreamDownload(relatorio, "application/pdf",
"relatorio.pdf");
File notas = //...
return new FileDownload(notas, "text/plain", "notas.txt");
118

## Página 127

CasadoCódigo Capítulo8. DownloadeUploaddearquivos
Porpadrão,oarquivoépassadoparaobrowser,quepodeescolherentremostrar
acaixadediálogodedownloadousimplesmentemostraroarquivodentrodobrow-
ser.Paraimagens,textosepdfsosbrowsersvãosimplesmentemostrarosarquivos
natela.Sequiserfor çarodownload,todosasimplementa çõesde Downloadpos-
suemumconstrutorquerecebeumbooleanparafor çarodownload.Porexemplo,
parafor çarodownloaddasnotas:
File notas = //...
return new FileDownload(notas, "text/plain", "notas.txt", true);
Se quisermos, podemos implementarDownload para um tipo específico
do nosso sistema. Por exemplo, se usarmos a classeArquivo para represen-
tararquivosemváriosmodelosdosistema, podemoscriarumaimplementa ção
ArquivoDownload,delegandoparao ByteArrayDownload:
public class ArquivoDownload implements Download {
private Arquivo arquivo ;
public ArquivoDownload(Arquivo arquivo ) {
this.arquivo = arquivo;
}
public void write(HttpServletResponse response ) throws IOException {
Download download = new ByteArrayDownload(arquivo.getConteudo(),
arquivo.getContentType(), arquivo.getNome());
download.write(response);
}
}
Emseguida,podemossimplificarocódigodocontroller:
@Get("/livros/{isbn}/capa")
public Download capa(String isbn ) {
Livro livro = estante.buscaPorIsbn(isbn);
Arquivo capa = imagens.recupera(livro.getCapa());
if (capa == null) {
result.notFound();
return null ;
119

## Página 128

8.3. OutrasimplementaçõesdeDownload CasadoCódigo
}
return new ArquivoDownload(capa);
}
PodemosusaressamesmaideiaparagerarrelatóriosemPDFouCSV,porexem-
plo,semprecisarmosnospreocuparcomdetalhesdecomojogaressesarquivosna
respostadarequisi ção,paraqueobrowserfa çaodownloadousimplesmenterende-
rizediretamenteoconteúdo.
120

## Página 129

Capítulo9
Cuidandodainfraestruturado
sistema:Interceptors
Noscapítulosanteriores,vimosferramentasquenosajudamnodiaadiadodesen-
volvimentodanossaaplica ção. Usaremosinjeçãodedependências,controllers,o
Result,osjspsdurantetodoodesenvolvimento,acadanovafuncionalidadedo
sistema. Masexistemalgumastarefasqueatingemtodoosistema,oupelomenos
umagrandepartedele.Tarefascomocontroledeacesso,controledetransa ções,log
deerrosetc.Nestecapítuloveremoscomoimplementaressastarefasusandointer-
ceptors.
9.1 E xecutando uma tarefa em v ários pontos do sis -
tema : Transações
Quandoestamostrabalhandocomalgunsbancosdedadosrelacionais,porexemplo,
oMySQLInnoDBouoOracle,sóconseguimosrealizaralgumamudan çanosdados

## Página 130

9.1. Executandoumatarefaemváriospontosdosistema:Transa ções CasadoCódigo
seestivermosdentrodoambientecontroladoquegaranteaatomicidade,aconsistên-
cia,oisolamentoeadurabilidade(ACID)daopera ção:a T r a n s ação.Consequência
dissoéque,nonossosistema,todavezquequisermosalterarosdadosprecisamos
abrirefechar( commitar)umatransa ção,paraqueaaltera çãorealmenteaconte çano
banco.
Na seção4.6resolvemosesseproblemapontualmente,nopróprioDAO:
@Override
public void adiciona(Livro livro ) {
this.manager.getTransaction().begin();
this.manager.persist(livro);
this.manager.getTransaction().commit();
}
Seseguirmosessaestratégia,acadamétododoDAOquealteraosdados,te-
ríamosquerepetirocódigodeiniciartransa ções. Alémdisso,essecódigosóestá
considerandoocaminhofeliz,emqueodadoconseguesersalvonobanco.Transa-
çõespodemfalharporváriosmotivos,comoviola çõesderestri çõesdobanco(como
colunas NOT NULL),porreferênciasinválidas,porfalhasdeconexãoetc,portanto
precisamostrataressecasoefazero rollbackdatransa ção.
Éumcódigobastantecomplicadoequeestariaespalhadoportodoosistema.
Paraevitaressaduplica çãodecódigo,vamospensarnopapeldo LivroDAOnosis-
tema:acessaremodificarosdadosdeumlivronobanco.Ocontroledetransa ções
éumainfraestruturaparaqueamodifica çãodosdadosocorra,nãofazpartedaló-
gicaqueo LivroDAOdeveriaexecutar,nãoésuaresponsabilidade.Alémdisso,se
quisermosadicionarvárioslivrosnamesmatransa ção,jánãopodemosusaresse
código.
Nessecaso,devemos inverter o controleepassarocódigodecontroledastran-
saçõesparaumaclasseespecializadaqueconseguirácuidardissoportodoosistema.
Nocapítulo4,vimosumadasformasdeinversãodecontrole:inje çãodedependên-
cias.Noentanto,inje çãodedependênciasnãovairesolveronossoproblema,pois
atransa çãonãoéumobjetoquepodemosrecebernoconstrutor,esimumcódigo
queprecisaserexecutado em voltadanossalógicadenegócios:um aspectodanossa
aplicação.
A s p e c t oétodorequisitooucódigodeinfraestruturaqueprecisamosexecutar
emváriospontosdanossaaplica ção,comocontroledetransa ção,controledesegu-
rança,loggingeauditoria.Éumconceitobemimportantequeatégerouumtermo
122

## Página 131

CasadoCódigo Capítulo9. Cuidandodainfraestruturadosistema:Interceptors
quandousado: Programação Orientada a Aspectos,ou A O P.Naprática,nãoconse-
guimosdesenvolverumsistemainteirosomenteusandoaspectosmas,noscasosem
queelesseaplicam,possibilitamsolu çõesbastanteelegantes.
OVRaptorpossuiumaferramentaparaimplementaraspectos:os Interceptors.
ElesfuncionamcomoosServletFilters,possibilitandoexecutaralgumalógicaantese
depoisdarequisi ção.Adiferen çaéquecomosInterceptorspodemosrecebercomo
dependênciaqualquercomponentedaaplica ção,entãopodemosaproveitaroque
jáestápronto.Podemospensarqueum Interceptorvaiexecutarlogoantesdo
métododocontrollerelogodepoisdessemétodo.
Paracriarum InterceptorprecisamosimplementarainterfacedoVRaptor
comessenomeeanotá-lacom @Intercepts.Nonossocaso,queremoscriarum
interceptorquecuidarádastransa ções,o TransacoesInterceptor,noprojeto
livraria-admin.
import br.com.caelum.vraptor.interceptor.Interceptor;
import br.com.caelum.vraptor.Intercepts;
@Intercepts
public class TransacoesInterceptor implements Interceptor {
}
Essainterfacepossuidoismétodos: accepts,querecebeoobjetodoVRaptor
querepresentaummétododeController—o ResourceMethod—edeveretornar
um booleanindicandoseessemétododeveounãoserinterceptado;eummétodo
interceptquerecebeapilhadeinterceptors,parapodermoscontinuaraexecu-
çãodométodonomomentonecessário,ousimplesmenteevitarqueométododo
controllersejaexecutado.
Para oTransacoesInterceptor,podemosadotarasolu çãomaissimples
paraométodo accepts:retornar trueeinterceptartodososmétodosdecon-
troller. Já o código de controle de transação deve estar em volta da chamada
aopróximointerceptordapilha. Paracuidardastransa çõesprecisamosdeum
EntityManager,logo,devemosrecebê-lonoconstrutor.
@Intercepts
public class TransacoesInterceptor implements Interceptor {
private EntityManager manager ;
123

## Página 132

9.1. Executandoumatarefaemváriospontosdosistema:Transa ções CasadoCódigo
public TransacoesInterceptor(EntityManager manager ) {
this.manager = manager;
}
@Override
public boolean accepts(ResourceMethod method ) {
return true ;
}
@Override
public void intercept(
InterceptorStack stack ,
ResourceMethod method ,
Object controller ) throws InterceptionException {
//abre a transação antes da execução
manager.getTransaction().begin();
//continua a execução do método do controller
stack.next(method, controller);
//commita a transação após a execução
manager.getTransaction().commit();
}
}
Paracompletaralógicadatransa ção,precisamosfazero rollbackcasohaja
algum problema. Um dos jeitos de fazer isso é envolvendo o código por um
try..finallyese,aofinaldaexecu ção,atransa çãocontinuarativaéporqueela
nãoconseguiuser commitadacomsucesso,portantoprecisamosfazero rollback:
@Override
public void intercept(InterceptorStack stack ,
ResourceMethod method ,
Object controller ) throws InterceptionException {
try {
manager.getTransaction().begin();
stack.next(method, controller);
124

## Página 133

CasadoCódigo Capítulo9. Cuidandodainfraestruturadosistema:Interceptors
manager.getTransaction().commit();
} finally {
if (manager.getTransaction().isActive()) {
manager.getTransaction().rollback();
}
}
}
Poderíamos também fazer umcatch(Exception e) nesse bloco e, só
então, fazer o rollback, mas esse interceptor não tem condição de tra-
tar a exceção e acabaria apenas relançando-a, provavelmente dentro de uma
InterceptionException,criadaespecialmenteparaessefim.Umaboaregraé,
seaclassenãovaifazernadadeútilcomaexce çãoalémderelan çá-la,émelhornem
capturaraexce ção,assimpodemospassaressaresponsabilidadedetrataraexce ção
paraoutraclasse(umoutrointerceptortalvez)ousimplesmentedeixaraparecera
páginadeerro500paraousuário.
9.2 C ontrolando os métodos interceptados
Quando criamos o TransacoesInterceptor, implementamos o método
acceptsretornando true.Issosignificaqueelevaiinterceptar t o d o sosmétodos
decontroller,ouseja,todasasrequisi çõesweb.Masnemsempreissoéodesejável.
Emboraessasolu çãosejasuficienteparaumsistemapoucoacessado,paraumsis-
temacommuitosacessos,criartransa çõesacadarequisi çãopodeserumproblema
edeixarosistemamaislentodoquedeveria.
T r a n s açõessãonecessáriaspararealizaropera çõesquemodificamobancode
dados,masnãosãoobrigatóriasquandofazemosapenasopera çõesdeleitura.Nem
sãonecessáriasquandoestamosapenasmostrandoumformulário.Poressemotivo,
precisamosimplementarométodo acceptsdointerceptorparanãointerceptaros
métodosquenãoprecisamdetransa ção.
Analisandoaassinaturadométodo accepts,temososeguinte:
public boolean accepts(ResourceMethod method ) {...}
Recebemosum ResourceMethod,querepresentaométododocontrollerque
estásendoinvocadonestarequisi ção,eprecisamosretornarumbooleanquedizseo
interceptorvaiserusadoounãonessemétodo.Essainterfacenospossibilitaacessar:
125

## Página 134

9.2. Controlandoosmétodosinterceptados CasadoCódigo
• O método: method.getMethod() retorna um
java.lang.reflect.Method, que é a classe que representa um mé-
todojava. Comele,podemosverificaratributoscomonome,parâmetrose
anotaçõespresentesnométodo.
• O controller: method.getResource().getType() retorna um
Class<?>,queéaclassequerepresentaumaclassejava.Comele,podemos
verificaratributoscomonome,pacoteeanota çõespresentesnaclasse.
Umaformadeimplementarométodo acceptsélistartodososmétodosde
controllerquequeremosinterceptareverificarseo ResourceMethodéumdeles.
Masessalistapodeficarbastanteextensanamedidaemqueoprojetovaicrescendo,
tornandoométodo acceptsbemdifícildemantereevoluir.
Umamaneirademelhoraresseregistroécriandoumaanota çãoparaindicar
queométodoseráinterceptado,nessecaso,seométododeveráserexecutadoden-
trodeumatransa ção. Podemoscriaraanota ção @Transacionalparaessefim.
Paraisso,primeiramentedevemoscriaraclassedaanota ção,usandoapalavrachave
@interface:
public @interface Transacional {
}
Emseguida,precisamosdizeremquelugaresessaanota çãoseráválida,usando
aanota ção @Target.Oslugaresválidosvãodeparâmetroseconstrutoresatéclas-
sesepacotes. Nonossocaso,sóprecisamosdessaanota çãoparamétodos,então
escolhemosessevalornaconfigura çãodo @Target:
@Target(ElementType.METHOD)
public @interface Transacional {
}
Outraconfigura çãonecessáriaéareten çãodaanota ção,ouseja,emquemo-
mentoelapoderáserlida. Definimosissocomaanota ção @Retention,cujos
valorespossíveissão SOURCE,comoqualaanota çãosóvalecomodocumenta-
ção, CLASS,comqueaanota çãopodeserlidaduranteoprocessodecompila ção,
e RUNTIME,comoqualaanota çãopodeserlidaduranteaexecu çãodaaplica ção.
Comoprecisamosleressaanota çãonointerceptor,usamosareten çãode RUNTIME.
126

## Página 135

CasadoCódigo Capítulo9. Cuidandodainfraestruturadosistema:Interceptors
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Transacional {
}
Agorapodemosanotarosmétodosdesejados,porexemplo,ométodo salva
do LivrosController:
@Transacional
@Post("/livros")
public void salva(Livro livro ) {...}
E para implementar o método accepts podemos usar o método
containsAnnotation do ResourceMethod, passando a anota ção
Transacional:
public boolean accepts(ResourceMethod method ) {
return method.containsAnnotation(Transacional.class);
}
Assim, todos os métodos de controller que estiverem anotados com
@Transacional serão interceptados pelo TransacoesInterceptor e,
portanto,rodarãodentrodetransa ções.Essaéamaneiramaisfácildeconfiguraros
métodosinterceptados.
Nocasoespecíficodetransa ções,podemosusaranossainterfaceRESTparade-
finirquaismétodospodemserinterceptados.SeusamososmétodosHTTPcorreta-
mente,sabemosqueasrequisi ções GETnãopodemmodificarosdadosdoservidor,
entãonãodevemrodardentrodetransa ções.Poroutrolado,asrequisi ções POST,
PUTe DELETEsupostamentemodificamoestadodealgumrecurso,portantodevem
rodardentrodetransa ção.
Podemosinterceptartodososmétodosquenãosãoacessíveispor @Get,dis-
pensandoacria çãodeumanovaanota çãoparaessefim:
public boolean accepts(ResourceMethod method ) {
return !method.containsAnnotation(Get.class);
}
127

## Página 136

9.3. Evitandoinstanciaçãodesnecessáriadeinterceptors:@Lazy CasadoCódigo
9.3 E vitando instanciação desnecessária de inter -
ceptors : @Lazy
Osinterceptorsnãoprecisamnecessariamenteseraplicadosemtodasasrequisi ções,
masprecisamosinstanciá-losparachamarométodo accepts,justamentepara
sabersedevemseraplicados. Oproblemaéqueessainstancia çãofazcomqueas
dependênciasdointerceptortambémsejaminstanciadas,easdependênciasdasde-
pendências,eassimsucessivamente.
Esseprocessopodesermuitocaropara,emalgunscasos,nemusarointerceptor.
No caso doTransacoesInterceptor,quedependedeum EntityManager,
possivelmenteestaríamosabrindoumaconexãocomobancodedadosparamostrar
umapáginadeformulárioquenãousanadadobanco.
Pararesolveresseproblema,podemosusaraanota ção @Lazy.Comela,oVRap-
torguardaumainstâncianãofuncionaldointerceptorsóparainvocarométodo
accepts.Assim,elesóinstanciaointerceptorcasoo acceptsretorne true.
@Intercepts @Lazy
public class TransacoesInterceptor implements Interceptor {
//...
public boolean accepts(ResourceMethod method ) {
return method.containsAnnotation(Transacional.class);
}
}
Parafazerissofuncionar,oVRaptorinstanciaoInterceptorpassandonullpara
todasasdependências,portantonemoconstrutornemométodo acceptspodem
usarasdependências,senãoserãolan çadas NullPointerExceptions.Seconse-
guirmosusarapenasométodoparadecidirseointerceptorvaiseraplicado,sejapor
anotaçãoouporverifica çãodeoutrosatributosdométodo,devemosanotá-locom
@Lazy.
Poroutrolado,seointerceptorforaplicadoemtodasasrequisi ções( accepts
retornando truesempre),nãoháganhonenhumemusaro @Lazy,portantoele
nãodeveserusado.
128

## Página 137

CasadoCódigo Capítulo9. Cuidandodainfraestruturadosistema:Interceptors
Usando interceptors para redirecionar a requisição
Os interceptors não são obrigados a chamar o
stack.next(method, controller), que continua a execução
dosinterceptorsatéexecutarométododocontroller. Podemos, por
exemplo, fazer um interceptor de segurança, que redireciona para a
páginadelogincasoousuárionãoestejalogado:
@Override
public void intercept(InterceptorStack stack ,
ResourceMethod method ,
Object controller ) throws InterceptionException {
if (usuarioEstaLogado()) {
stack.next(method, controller);
} else {
result.redirectTo(LoginController.class).login();
}
}
129

## Página 138

9.3. Evitandoinstanciaçãodesnecessáriadeinterceptors:@Lazy CasadoCódigo
Ordem relativ a entre interceptors
Aordememqueosinterceptorssãoexecutadosédeterminadapela
ordememqueelessãolidospeloVRaptor. Essaordemnãoéfixanem
temregrapredefinida. Issofuncionabemnamaioriadoscasos, em
queosinterceptorssãoindependentesentresi,mascasouminterceptor
precisenecessariamenterodarapósooutro,épossívelusarosatributos
beforee afterparafor çarumaordem.
@Intercepts(before=LoggerInterceptor.class,
after=ExceptionInterceptor.class)
public class TransacoesInterceptor implements Interceptor {
...
}
Nesse caso a ordem de execu ção dos interceptor será:
ExceptionInterceptor -> TransacoesInterceptor ->
LoggerInterceptor.
Épossíveltambémfor çaraexecu çãodosinterceptorsemrela çãoaos
interceptorsdoVRaptorquecuidamdoprocessodarequisi ção. Pode-
mosexecutaralgumcódigoantesoudepoisde:
• Definição do método que vai ser executado na requisição:
ResourceLookupInterceptor.class
• InstanciaçãodoController: InstantiateInterceptor.class
• Criação dos parâmetros do método:
ParametersInstantiatorInterceptor.class
• Execução do método do controller:
ExecuteMethodInterceptor.class
ExistemaindaalgunsoutrosinterceptorsdoVRaptorquerealizam
outrasfun ções,conformeveremosnocatálogodeinterceptorsnocapí-
tulo15.
130

## Página 139

CasadoCódigo Capítulo9. Cuidandodainfraestruturadosistema:Interceptors
Outro exemplo de interceptor: Controle de usuários
Nonossosistema,o livraria-admincuidarádocadastrosdoslivrosquevão
servendidosnosite. Essecadastropodealterartotalmentecomoumlivrovaiser
apresentadonosite,portantosópodeserfeitoporpessoasqualificadasparatal.Por
essemotivo,vamoscontrolaroacessodepessoasemgeralaessecadastro,criando
umaformadepessoasseidentificarempararealizaremasopera çõesdesejadas.
Essecontroledeacessogeralmentesedáemdoispassos:primeiro,precisamos
saberqueméousuárioqueestáacessandoosistemae,depois,precisamossaberse
esseusuáriotempermissãoderealizaraopera çãorequerida.Chamamosessesdois
passosde Autenticaçãoe Autorização,respectivamente.
Abaseparaessecontroledeacessoécriarumaclassequerepresentaousuário
dosistema:
public class Usuario {
private String login ;
private String senha ;
// outros atributos, getters e setters
}
Dessaforma,identificamosousuárioqueestáinteragindocomosistema.Outra
parteimportanteéconseguirsaberseousuáriotempermissãoparadeterminadas
operações.Essecontrolepodesertãocomplexoquantosequeira,masnonossocaso
teremossódoistiposdeusuários:admins,quepodemalteraroslivrosenãoadmins
quesópodemvisualizaroslivros.Paraisso,vamosacrescentarumcampo admin
naclasse Usuario:
public class Usuario {
private String login ;
private String senha ;
private boolean admin;
// outros atributos, getters e setters
}
Aotentaracessarosistema,precisamospediraousuárioqueseidentifiquepara
continuar,ouseja,quefa çaologin.Comonãoqueremosficarpedindotodarequi-
131

## Página 140

9.3. Evitandoinstanciaçãodesnecessáriadeinterceptors:@Lazy CasadoCódigo
siçãoparaqueousuárioselogue,precisamosguardarosseusdadosnasessãodo
usuário,apósologin.Paraisso,podemosusarumcomponentedeescopodesessão,
representandoousuáriologadonosistema:
@Component
@SessionScoped
public class UsuarioLogado {
private Usuario usuario ;
public void loga(Usuario usuario ) {
this.usuario = usuario;
}
public boolean isLogado() {
return this .usuario != null;
}
public Usuario getUsuario() {
return usuario;
}
public void desloga() {
this.usuario = null;
}
}
Dessaforma,podemoscriarumcontrollerparaapresentaroformuláriodelogin
erealizaraautentica ção.Essecontrollerbuscaráousuárioemalgumlugar,comopor
exemplo,nobancodedadosounoLDAP.Paraabstrairolugarondeficarãoosusuá-
rios,vamosusarainterface RegistroDeUsuarios. Apósencontrarousuário,
vamosguardarassuasinforma çõesno UsuarioLogado.
@Resource
public class LoginController {
private RegistroDeUsuarios usuarios ;
private UsuarioLogado logado ;
private Result result ;
public LoginController(RegistroDeUsuarios usuarios ,
132

## Página 141

CasadoCódigo Capítulo9. Cuidandodainfraestruturadosistema:Interceptors
UsuarioLogado logado ,
Result result ,
Validator validator ) {
this.usuarios = usuarios;
this.logado = logado;
this.result = result;
}
@Get("/login")
public void formulario() {}
@Post("/login")
public void login(String login , String senha ) {
Usuario usuario = usuarios.comLoginESenha(login, senha);
if (usuario == null) {
validator.add(new I18nMessage("usuario",
"login.ou.senha.invalidos"));
}
validator.onErrorRedirectTo(this).formulario();
logado.loga(usuario);
// ou a página inicial
result.redirectTo(LivrosController.class).lista();
}
@Get("/logout")
public void logout() {
logado.desloga();
result.redirectTo(this).formulario();
}
}
Vouomitiraquiqualvaiseraimplementa çãodo RegistroDeUsuarios,use
amaisapropriadaparaasuasitua ção. Vouomitirtambémoformuláriodelogin,
porbrevidade.
Comnosso LoginControllercriado,precisamosredirecionarparaelesem-
prequeumusuáriotentaracessarocadastrodelivros.Poderíamosiremcadaum
dosmétodoseverificarseousuárioestálogado,masjátemosumaferramentapara
fazeressetipodecódigo:osinterceptors.
133

## Página 142

9.3. Evitandoinstanciaçãodesnecessáriadeinterceptors:@Lazy CasadoCódigo
Nesseinterceptor,seousuárionãoestiverlogado,vamosredirecioná-loparao
formuláriodelogin.Paraissovamosprecisardo UsuarioLogadoedo Result.
@Intercepts
public class AutenticacaoInterceptor implements Interceptor {
private UsuarioLogado usuario ;
private Result result ;
public AutenticacaoInterceptor(UsuarioLogado usuario , Result result ) {
this.usuario = usuario;
this.result = result;
}
public boolean accepts(ResourceMethod method ) {
return // ???
}
public void intercept(InterceptorStack stack ,
ResourceMethod method ,
Object controller ) {
if (usuario.isLogado()) {
stack.next(method, controller);
} else {
result.redirectTo(LoginController.class).formulario();
}
}
}
Faltaimplementarométodo accepts.Paraisso,poderíamoscriarumaanota-
ção @Restrito,porexemplo,paraidentificaraspáginasqueprecisamdelogin,ou
criarumaanota ção @Liberadoparaaspáginasquenãoprecisamdelogin,depen-
dendodonúmerodepáginasqueserãocontroladas.Nonossocaso,oadmininteiro
vaiprecisardelogin,entãoo acceptsseria true.Mas,assim,atéoformuláriode
loginpassarianointerceptorenuncaseriaexecutado.Vamos,então,aceitartodos
oscontrollers,menosodelogin:
public boolean accepts(ResourceMethod method ) {
return !method.getResource().getType().equals(LoginController.class);
}
134

## Página 143

CasadoCódigo Capítulo9. Cuidandodainfraestruturadosistema:Interceptors
Comissonossointerceptordeautoriza çãojáestápronto. Precisamos,ainda,
verseousuáriologadotempermissãodeexecutaraopera çãodesejada.Paraisso,
vamoscriaroutrointerceptor,quecuidadaautoriza ção. Esseinterceptorprecisa
obrigatoriamenterodardepoisdo AutenticacaoInterceptore,casoousuário
nãotenhapermissão,redirecionarparaumapáginafalandoisso. OHTTPjátem
umstatusdeerroparaisso,o 401 -- Unauthorized ,vamosusá-lo.
@Intercepts(after=AutenticacaoInterceptor.class)
public class AutorizacaoInterceptor implements Interceptor {
private UsuarioLogado usuario ;
private Result result ;
public AutorizacaoInterceptor(UsuarioLogado usuario , Result result ) {
this.usuario = usuario;
this.result = result;
}
public boolean accepts(ResourceMethod method ) {
return !method.getResource().getType().
equals(LoginController.class);
}
public void intercept(InterceptorStack stack ,
ResourceMethod method ,
Object controller ) {
if (podeAcessar(method)) {
stack.next(method, controller);
} else {
result.use(Results.http()).sendError(401,
"Você não está autorizado!" );
}
}
private boolean podeAcessar(ResourceMethod method ) {
return // ???
}
}
Precisamosdefiniraestratégiadeautoriza ção,nométodo podeAcessar.Para
facilitar,poderíamoscriarumaanota ção @Adminparalógicasquesópodemser
135

## Página 144

9.3. Evitandoinstanciaçãodesnecessáriadeinterceptors:@Lazy CasadoCódigo
feitasporadministradores,ou @Livreparalógicasquepodemseracessadaspor
todos,dependendodaquantidadedelógicasquecaememcadacaso.Ouaindapo-
demosusarumaconven ção:tudoqueé @Getéliberadoparatodomundo,poisnão
modificanenhumdado(oupelomenosnãodeveria),etodoorestosóéacessível
poradmin.
Parafacilitar,vamosadotaressaconven ção:ousuáriopodeacessarométodose
elefor @Get,ouseelefor admin,quepodeacessartudo:
public boolean podeAcessar(ResourceMethod method ) {
return method.containsAnnotation(Get.class) ||
usuario.getUsuario().isAdmin();
}
Dessaforma,conseguimoscontrolaroacessoaocadastrodelivrossóparausuá-
rioslogados,comasmodifica çõesaoslivrosfeitossomenteporadmins. Existem
diversasferramentasqueauxiliamessecontroledeacessos,comoaespecifica ção
JAASeo Spring Security,quecobremtodososcasospossíveisdeautentica ção
eautoriza çãoejápossuemformaspadronizadasdefazerautentica çãocomLDAP,
ADeoutrastecnologias. Podemosintegrá-lasdeformatransparenteaoVRaptor,
criandocomponentesquerealizamessaintegra ção.
Podemostambémusarosplugins vraptor-authe SACI-VRaptor,quepo-
demseracessadosapartirdodiretóriodepluginsdoVRaptor: https://github.com/
caelum/vraptor-contrib.
136

## Página 145

Capítulo10
Melhorandoodesigndaaplica ção:
ConversoreseTestes
NaOrienta çãoaObjetos,temosumobjetocomoumaabstra çãoqueunedados(atri-
butos)acomportamentos(métodos).Masquandoestamoscriandoumaaplica ção
quesalvadadosnobancodedados,tendemosacriarmuitasclassesquenãotêmne-
nhumcomportamento:apenasumpunhadodeatributoscomgettersesetters,que
sãoapenasacessoresdessesatributos,eomapeamentodaJPA.
Quandofazemosisso,algumaslógicasficamespalhadas,muitasvezesemclasses
*Util,quandopoderíamosagruparessaslógicascomosdadosemqueelassão
aplicadasemclassespequenaseespecializadas.Veremosnestecapítulocomotratar
essetipodeclasseeintegrá-lafacilmenteaoprocessamentodarequisi ção.
Alémdisso,criaressasclassespequenasmelhoraodesigndaaplica çãoedeveria
serfeitoconstantemente.UmaboaferramentaparaissoéousodeTestesautomatiza-
dos,queajudamaidentificarpartesdosistemaqueestãoficandocomplexasdemais
e,seusamosociclodoTestDrivenDevelopment/Design(TDD),osprópriostestes

## Página 146

10.1. Populandoobjetoscomplexosnarequisi ção:Conversores CasadoCódigo
ajudamamelhorarodesigndaaplica ção. Tambémveremosnessecapítulocomo
usarTDDemconjuntocomoscomponentesdoVRaptor.
10.1 P opulando objetos complexos na requisição :
Conversores
Nocapítulo3vimoscomocriarocadastrodelivros,comumformuláriocapazde
preenchertodososatributosdeum Livro.Osatributospreenchidosforam:
public class Livro {
private String isbn ;
private String titulo ;
private String descricao ;
private BigDecimal preco ;
private Calendar dataPublicacao ;
}
Ao criar a classeLivro,escolhemosotipo BigDecimalpararepresentaro
preço,poiseleconseguerepresentarumvalordecimalsemperderprecisão.Masserá
queesse BigDecimaléosuficiente?Imaginequeanossalivrariacresceueagora
vendelivrosimportados.AlgunsdoslivrosvirãodosEstadosUnidos,comopre ço
emdólar,outrosdaInglaterra,comopre çoemlibras,eoutrosaindadaFran ça,com
opre çoemeuro.Agoraaosalvarumlivronosistemacomopre çovalendo 15.90,
comosabemosseeleestáemreais,dólares,librasoueuros?
Damaneiraquerepresentamosopre çonaclasse Livronãoconseguimossaber
isso. Precisamos,portanto,guardarovalordamoedacorrespondenteaopre çodo
livro.Paraissovamoscriarumaenumcomasmoedassuportadaspelosistema:
public enum Moeda {
REAL, DOLAR, EURO, LIBRA
}
Eadicionarumatributoqueguardaamoedanaclasse Livro:
public class Livro {
//...
private Moeda moeda ;
private BigDecimal preco ;
138

## Página 147

CasadoCódigo Capítulo10. Melhorandoodesigndaaplica ção:ConversoreseTestes
//...
}
Agora,aoconsultarmosopre çodolivro,conseguimossaberqualéamoeda
olhandoparaoatributo moeda. Sequisermossomarovalordevárioslivros,por
exemplo,numcarrinhodecompras,precisaremosconsiderarsempreopre çoea
moeda.Todaavezqueolharmosparaopre çodolivroprecisaremosolhartambém
paraamoedaese,emalgumlugardocódigo,esquecermosdefazerisso,podemos
somarumpre çoemreaiscomumpre çoemeurosechegarnumvalorquenãoénem
umacoisanemoutra!
Apesardetermosguardadoamoedanaclasse Livro,moedanãoéumatri-
butodo Livro,éumatributodopre ço!Assimcomonãotemosumatributo mes
nolivroesimumadatadepublica çãoquepossuiummês,deveríamosterumatri-
buto preconolivroque,alémdeguardarovalordopre ço,guardariatambéma
moeda. Parafazerisso,precisamosdeumaclassequeagrupaessesdoisvalores,a
classe Dinheiro:
public class Dinheiro {
private Moeda moeda ;
private BigDecimal montante ;
}
Eopre çodaclasse Livropassaaserdessetipo:
public class Livro {
//...
//-private Moeda moeda;
private Dinheiro preco ;
}
Essaclasse Dinheiroéumaclassequeguardadadosmasnãoéumaclasse
quesalvaríamosnobancodedadoscomoumatabela.Éumaclassequeguardaum
valor,nessecasoumvaloremdinheiro,comoporexemplo R$ 29,90.Doisobje-
tosdotipo Dinheiroquetêmamesma moedaeomesmo montanteguardam
exatamenteomesmovalor.Classesdessetiposãooschamados Value Objects
(http://martinfowler.com/bliki/ValueObject.html),ouseja,classesquerepresentam
valores.
139

## Página 148

10.1. Populandoobjetoscomplexosnarequisi ção:Conversores CasadoCódigo
Ao criar a classeDinheiro,podemosconcentrartodasasopera çõesmonetárias
dentrodela,comosomarpre çosouconverterumpre çoderealparadólar,epodemos
fazerverifica çõesadicionais,comonãopermitirsomarpre çosdemoedasdiferentes.
Parapopularopre çodolivrononossosistemaagoraprecisaríamosdedoiscam-
posnoformulário:
<li>Moeda: <br/>
<input type="text" name="livro.preco.moeda"
value="${livro.preco.moeda}"/></li>
<li>Montante: <br/>
<input type="text" name="livro.preco.montante"
value="${livro.preco.montante}"/></li>
Masolivronãopossuimoedaemontante,elepossuiumpre ço!Oidealéque
ousuáriopossadigitarnocampodepre çoalgocomo“R$52,00”eosistemaconse-
guirsalvaropre çocorrespondente.Mascomofazerisso?Antes,vamosanalisaros
atributos da classeLivro.
public class Livro {
private String isbn ;
private String titulo ;
private String descricao ;
private Calendar dataPublicacao ;
private Dinheiro preco ;
}
Osprimeirosatributossão Stringse,paraserempopulados,bastapegaro
parâmetroquevemdarequisi ção,ouseja,ovalordigitadonoinput.Nestecaso,não
importaoquefoidigitadonoinput,oscampos Stringserãopopuladoscomesse
valor.
Noentanto,osdoisúltimosvaloressãomaiscomplexos: o preco,queéum
Dinheiro,ea dataPublicacao,queéum Calendar.Quandoqueremospo-
pularadatadepublica ção,digitamosumvalornocampocorrespondentedoformu-
lário,porexemplo, 17/06/2013.Essevalorvaiparaoservidorcomoa String
"17/06/2013",masparapoderpassaressevalorparaaclasse Livro,oVRaptor
precisaconverter "17/06/2013"num Calendarquerepresentaessedia.Preci-
samosqueessamesmalógicaseapliquequandodigitarmos R$ 29,90 nocampo
140

## Página 149

CasadoCódigo Capítulo10. Melhorandoodesigndaaplica ção:ConversoreseTestes
“Preço”doformulário,queremosqueoVRaptorconvertaparao Dinheirocom
moeda REALemontante 29.90.
Issoéfeitoatravésdeclassesespecializadasemconverterosparâmetrosdare-
quisiçãoemobjetosquerepresentamessesvalores.Essasclassessão Converters,
ouseja,implementamainterface ConverterdoVRaptoresãoresponsáveispor
converteruma Stringqueveiodarequisi çãoemumtipoespecífico.
Mapeando a classe Dinheiro no Hibernate
Para mapear a classeDinheiro,nãovamoscriarumatabelasepa-
rada,jáque DinheiroéumV alue Object.Aoinvésdissovamosmapeá-
ladentrodatabela Livro,usandoaanota ção @Embedded:
@Entity
public class Livro {
//...
@Embedded
public Dinheiro preco ;
}
Assim, serãocriadasduascolunasnatabelaLivro, a moeda eo
montante.Alémdisso,énecessáriocriarumconstrutorsemargumen-
tosdentrodaclasse Dinheiro,mesmoqueseja protectedparaque
ohibernateconsigainstanciaressaclasseapartirdosdadosdobanco.
OVRaptorpossuiumconjuntodeConvertersjáimplementados,todosnopa-
cote br.com.caelum.vraptor.converter,esãoosuficienteparapopularto-
dosostipossimplesdoJava: String,números, boolean, enumedatas. Esses
conversorespadrãosãosuficientesparaamaioriadosobjetosquepopulamosnare-
quisição,masprecisaremoscriarumpersonalizadoparaanossaclasse Dinheiro.
Paraisso,devemoscriarumaclasseanotada @Convert(Dinheiro.class)que
implementa Converter<Dinheiro>.
import br.com.caelum.vraptor.Convert;
import br.com.caelum.vraptor.Converter;
@Convert(Dinheiro.class)
public class DinheiroConverter
141

## Página 150

10.1. Populandoobjetoscomplexosnarequisi ção:Conversores CasadoCódigo
implements Converter<Dinheiro> {
@Override
public Dinheiro convert(
String value ,
Class<? extends Dinheiro> type,
ResourceBundle bundle ) {
return null ;
}
}
Ainterface ConverterdefineumúnicométodoquedevepegaraStringpas-
sadaeconverternotipodesejado,nocasoo Dinheiro.Paraauxiliaraconversão,
existemoutrosdoisparâmetros,o typequeéaclassedotipodedestino,paraser
usadocasoestejamosconvertendoparaimplementa çõesdeumainterfaceoufilhos
deumaclasse,eo bundleparagerarmensagensdeerrointernacionalizadas.
Para facilitar a implementação desse Converter, vamos usar TDD —
Test Driven Design , criando a classe DinheiroConverterTest dentro de
src/main/test. ParainiciarociclodoTDD,vamoscriarumtestequefalha,
usandoJUnit4:
import static org.junit.Assert.*;
import static org.hamcrest.Matchers.*;
public class DinheiroConverterTest {
@Test
public void converteUmValorEmReais() {
Converter<Dinheiro> converter = new DinheiroConverter();
assertThat(converter.convert("R$ 1,00" , null, null),
is(new Dinheiro(Moeda.REAL, new BigDecimal("1.00"))));
}
}
142

## Página 151

CasadoCódigo Capítulo10.Melhorandoodesigndaaplicação:ConversoreseTestes
Onde aprender TDD?
RecomendofortementequevocêaprendaTDDeadoteapráticanos
sistemasquedesenvolver.Definitivamenteeleaumentaaqualidadedo
softwareescrito.U mexcelentematerialéolivroescritopeloMauricio
Aniche,edisponívelnositedaEditoraCasadoCódigo—http://www.
casadocodigo.com.br.
Paratestar,estamosusandoaDSL(Domain Specific Language)doJUniteos
MatchersdoHamcrestquevimosnocapítulodevalidações (6.2).Nessetestees-
tamosgarantindoqueaconversãodovalor "R$ 1,00"sejao Dinheiroemreal
novalorde 1.00.U s a n d oessaDSLconseguimosleressafraseanterior,eminglês,
ouseja,temosumtestebastantelegível.Aorodaroteste(noEclipse,botãodireito>
RunAs>JUnitTest)vemosqueelefalha:
java.lang.AssertionError:
Expected: is <br.com.casadocodigo.livraria.modelo.Dinheiro@692a3722>
got: null
Essasaídafalaqueesperavaum Dinheiroespecífico,masveio null.Opro-
blemaéqueapenasusandoessamensagemnão conseguimossaberqualéova-
loremdinheiroqueestamosesperando. Paracorrigirissovamosimplementaro
toStringdaclasse Dinheiro.Oformatodesejado,parafacilitaraleitura,pode
ser "Dinheiro(R$ 1.00)". Paranão precisarmosficarfazendoummontede
ifs,podemosmodificara enumde Moedaparaincluirosímbolodecadacons-
tante:
public enum Moeda {
REAL("R$"), DOLAR("US$"),
EURO("€"), LIBRA("£");
private final String simbolo;
private Moeda(String simbolo) {
this.simbolo = simbolo;
}
public String getSimbolo() {
143

## Página 152

10.1.Populandoobjetoscomplexosnarequisição:Conversores CasadoCódigo
return simbolo;
}
}
public class Dinheiro {
//...
@Override
public String toString() {
return String.format("Dinheiro(%s %s)",
moeda.getSimbolo(),
montante
);
}
}
Agora,aorodarmosoteste,veremosaseguintemensagem:
java.lang.AssertionError:
Expected: is <Dinheiro(R$ 1.00)>
got: null
Para fazer o teste passar rapidamente, vamos simplesmente retornar o
Dinheirodesejado:
@Convert(Dinheiro.class)
public class DinheiroConverter
implements Converter<Dinheiro> {
@Override
public Dinheiro convert(
String value,
Class<? extends Dinheiro> type,
ResourceBundle bundle) {
return new Dinheiro(Moeda.REAL, new BigDecimal("1.00"));
}
}
Agora,serodarmosoteste,eleaindafalha,masdestavezcomessamensagem:
java.lang.AssertionError:
Expected: is <Dinheiro(R$ 1.00)>
got: <Dinheiro(R$ 1.00)>
144

## Página 153

CasadoCódigo Capítulo10.Melhorandoodesigndaaplicação:ConversoreseTestes
Ora,esperamosum Dinheirode R$ 1.00eapareceuum Dinheirode R$
1.00. Oquedeuerrado? A p e s a rdeguardaremomesmovalor,são doisobjetos
diferentesnamemória,porissootestefalha.Nossaclasse Dinheiroéum V a l u e
Object,queédefinidaunicamentepelosseusatributos.Ouseja,umdinheiroéigual
aooutrosetemamesmamoedaeomesmomontante.Eparadizerisso,precisamos
implementaro equalseo hashCodedaclasse Dinheiro,depreferênciagerando
essesmétodoscomaajudadasuaIDE.NoEclipse,usamosomenu Source > Generate
hashCode() a n dequals()eselecionamososdoisatributos.
Agora,aorodarmosnovamenteoteste,elepassa!Completamosasegundaparte
dociclodoTDD,fazendootestepassaredevemospassarparaapróximaparte:a
Refatoração.ClaroqueretornardiretooDinheirodeR$1.00nãoéumaimplemen-
taçãorazoável,entãovamosmodificá-laparaconvertervaloresemReal. Primeira
tentativavaiser,seastringcomeçarpor "R$",tentarcriarum BigDecimala
partirdela.
public Dinheiro convert(String value, ...) {
if (value.startsWith("R$")) {
return new Dinheiro(Moeda.REAL,
new BigDecimal(value.replace("R$ ", ""))
);
}
return null;
}
Porém,aorodarmosoteste,recebemosumerro:
145

## Página 154

10.1.Populandoobjetoscomplexosnarequisição:Conversores CasadoCódigo
java.lang.NumberFormatException
at java.math.BigDecimal.<init>(BigDecimal.java:459)
at java.math.BigDecimal.<init>(BigDecimal.java:728)
at br.com.casadocodigo.livraria.conversor.DinheiroConverter
.convert(DinheiroConverter.java:23)
Issoaconteceuporqueoconstrutordo BigDecimalesperaosnúmerosnofor-
mato 1.00,enão 1,00comofoipassado.Pararesolverisso,vamostrocartoda
vírgulaporponto:
@Convert(Dinheiro.class)
public class DinheiroConverter
implements Converter<Dinheiro> {
@Override
public Dinheiro convert(
String value,
Class<? extends Dinheiro> type,
ResourceBundle bundle) {
if (value.startsWith("R$")) {
return new Dinheiro(Moeda.REAL,
new BigDecimal(
value.replace("R$ ", "")
.replace(',', '.')
)
);
}
return null;
}
}
Aorodarmosnovamenteoteste,vemosqueelepassae,seestivermossatisfeitos
comaimplementação,completamosaterceirapartedociclodoTDD.Comoéum
ciclo,precisamosvoltarparaaprimeiraparteeescreverumtestequefalha.Podemos
escreverumtesteparaconvertervaloresemoutramoeda,porexemploemDólar.
@Test
public void converteUmValorEmDolares() {
Converter<Dinheiro> converter = new DinheiroConverter();
146

## Página 155

CasadoCódigo Capítulo10.Melhorandoodesigndaaplicação:ConversoreseTestes
assertThat(converter.convert("US$ 49,95", null, null),
is(new Dinheiro(Moeda.DOLAR, new BigDecimal("49.95"))));
}
Aorodarmosoteste,elefalhacomamensagem:
java.lang.AssertionError:
Expected: is <Dinheiro(US$ 49.95)>
got: null
Amensagemestáclaraosuficiente,então vamosmodificaraimplementação
parafazerotestepassar. U m aimplementação maisdiretaécopiaroifdereaise
transformá-loemdólar:
if (value.startsWith("R$")) {
return new Dinheiro(Moeda.REAL,
new BigDecimal(
value.replace("R$ ", "")
.replace(',', '.')
)
);
} else if (value.startsWith("US$")) {
return new Dinheiro(Moeda.DOLAR,
new BigDecimal(
value.replace("US$ ", "")
.replace(',', '.')
)
);
}
return null;
Aorodarmosostestes,vemosquetantootestedereaisquantoodedólarespas-
sam.Podemosentão,passarparaarefatoração.Secontinuarmoscomocódigodessa
maneirateremosumifparacadamoeda,comumcódigobemparecidodentrode
cada if.Asúnicascoisasquemudamsãoamoedaeosímbolo,ambosacessíveis
pelasconstantesdaenum Moeda.V a m o smodificar,então,parapassarportodasas
constantesda enumetestá-las:
for (Moeda moeda : Moeda.values()) {
if (value.startsWith(moeda.getSimbolo())) {
return new Dinheiro(moeda,
147

## Página 156

10.1.Populandoobjetoscomplexosnarequisição:Conversores CasadoCódigo
new BigDecimal(
value.replace(moeda.getSimbolo(), "")
.replace(',', '.').trim()
)
);
}
}
return null;
Paramanterocomportamentoanterior,adicionamosum trim()pararemover
osespaçosembrancodocomeçoda String.Aorodarostestesvemosqueconti-
nuampassando,entãocompletamosoutrociclo.Paracomeçaroutrociclopodería-
mostestaroutramoeda,masotestenãoiriafalhar,jáqueestamoscontemplando
todasasmoedasnoconverter.
Oscasosfelizes(happy paths)jáforamimplementados,agoraprecisamospen-
sarnoscasospatológicos,porexemplosepassamumvalorquenãoéumdinheiro.
Dojeitoqueestáaimplementaçãoelevaiconverterpara nullnessecaso,masse
deixarmosassimpodemosmascararerros.Quandoa Stringquetentamoscon-
verternão éconversívelparaotipodesejado,precisamossinalizarcomumerro.
AAPIdeconvertersdoVRaptorjápossuiumerroimplementadoparaisso,o
ConversionError.Esseerrojáéautomaticamenteconvertidonumamensagem
devalidação.Podemosmostrá-lonoformuláriosemnenhumcódigoadicional.
Vamos,então,começaroutrociclodoTDD,criandoumtestequeesperaoerro
deconversão:
@Test(expected=ConversionError.class)
public void lancaErroDeConversaoQuandoOValorEhInvalido() {
Converter<Dinheiro> converter = new DinheiroConverter();
converter.convert("noventa pratas!", null, null);
}
Aorodaroteste,recebemosamensagem:
java.lang.AssertionError:
Expected exception: br.com.caelum.vraptor.converter.ConversionError
Parafazerotestepassar,precisamoslançaresseerro,casonãosejapossívelcon-
verter:
148

## Página 157

CasadoCódigo Capítulo10.Melhorandoodesigndaaplicação:ConversoreseTestes
public Dinheiro convert(String value, ...) {
for(Moeda moeda : Moeda.values()) {...}
throw new ConversionError(value + " não é um dinheiro válido");
}
Aorodarmosostestes,vemosqueelespassam.Paramelhorarageraçãodasmen-
sagens,podemosusaroparâmetro bundlequerecebemosnométodo convert,
parapodermosinternacionalizaramensagem.Paraisso,podemosfazer:
throw new ConversionError(
MessageFormat.format(bundle.getString("dinheiro_invalido"), value)
);
Ecolocarachave "dinheiro_invalido"no messages.properties.Ao
rodarmosotesterecebemosuma NullPointerException,poisnãopassamoso
bundle.V a m o scorrigirissomudandootesteparausarobundledemensagens:
@Test(expected=ConversionError.class)
public void lancaErroDeConversaoQuandoOValorEhInvalido() {
Converter<Dinheiro> converter = new DinheiroConverter();
converter.convert("noventa pratas!", null,
ResourceBundle.getBundle("messages"));
}
Aorodaroteste,eleaindafalha,comamensagem:
java.lang.Exception:
Unexpected exception,
expected<br.com.caelum.vraptor.converter.ConversionError>
but was<java.util.MissingResourceException>
...
Caused by: java.util.MissingResourceException:
Can't find resource for bundle java.util.PropertyResourceBundle,
key dinheiro_invalido
...
Ou seja, ele esperava o ConversionError, mas aconteceu uma
MissingResourceException,quedizqueachave dinheiro_invalidonão
foiencontradanobundlepassado.Bastaadicioná-lano messages.properties:
dinheiro_invalido = "{0}" não é um dinheiro válido
149

## Página 158

10.1.Populandoobjetoscomplexosnarequisição:Conversores CasadoCódigo
Agorasim,aorodarmosostestesvemosquetodoselespassam.Outrocasoem
quevaifalharéquandoa Stringcomeçacomumsímbolo,masonúmeroéinvá-
lido:
@Test(expected=ConversionError.class)
public void lancaErroDeConversaoQuandoOMontanteEhInvalido() {
Converter<Dinheiro> converter = new DinheiroConverter();
converter.convert("R$ mil", null,
ResourceBundle.getBundle("messages"));
}
Amensagemdeerroaorodaroteste:
java.lang.Exception:
Unexpected exception,
expected<br.com.caelum.vraptor.converter.ConversionError>
but was<java.lang.NumberFormatException>
...
Caused by: java.lang.NumberFormatException
...
Paracorrigirprecisamosenvolveracriaçãodo BigDecimalnum try..catch
elançarum ConversionErroremvezdeum NumberFormatException:
for (Moeda moeda : Moeda.values()) {
if (value.startsWith(moeda.getSimbolo())) {
try {
return new Dinheiro(moeda,
new BigDecimal(
value.replace(moeda.getSimbolo(), "")
.replace(',', '.').trim()
)
);
} catch (NumberFormatException e) {
throw new ConversionError(
MessageFormat.format(bundle.getString("dinheiro_invalido"),
value)
);
}
}
}
throw new ConversionError(
150

## Página 159

CasadoCódigo Capítulo10.Melhorandoodesigndaaplicação:ConversoreseTestes
MessageFormat.format(bundle.getString("dinheiro_invalido"), value)
);
Essaimplementaçãofazostestespassarem,mascomeçouaficarruim.Vamos,
portanto,refatorá-la,paracompletarociclodoTDD.Paraissovouextrairacriação
do BigDecimalparaummétodo,levandojuntoo try..catch:
@Override
public Dinheiro convert(
String value,
Class<? extends Dinheiro> type,
ResourceBundle bundle) {
for (Moeda moeda : Moeda.values()) {
if (value.startsWith(moeda.getSimbolo())) {
return new Dinheiro(moeda, criaMontante(value, moeda, bundle));
}
}
throw new ConversionError(
MessageFormat.format(bundle.getString("dinheiro_invalido"), value)
);
}
private BigDecimal criaMontante(
String value,
Moeda moeda,
ResourceBundle bundle) {
try {
return new BigDecimal(
value.replace(moeda.getSimbolo(), "")
.replace(',', '.').trim()
);
} catch (NumberFormatException e) {
throw new ConversionError(
MessageFormat.format(bundle.getString("dinheiro_invalido"),
value)
);
}
}
151

## Página 160

10.1.Populandoobjetoscomplexosnarequisição:Conversores CasadoCódigo
Rodandoostestes,elescontinuampassandoepoderíamoscontinuarrefato-
rando,masvamospararporaqui.U múltimocasoqueagentenãocobriuéquando
ousuárionão preencheuovalordedinheiro. Nessecasoa Stringvaivirvazia
e,dojeitoqueestáaimplementação,vailançarum ConversionError.Nãoéa
respostamaisadequada,melhorseriaretornar null,jáqueocamponãofoipreen-
chido.Vamos,então,adicionarumtesteparaisso:
@Test
public void converteStringVaziaEmNull() {
Converter<Dinheiro> converter = new DinheiroConverter();
ResourceBundle bundle = ResourceBundle.getBundle("messages");
assertThat(converter.convert("", null, bundle),
is(nullValue()));
}
Essetestefalhacomamensagem:
br.com.caelum.vraptor.converter.ConversionError:
"" não é um dinheiro válido
Parafazerotestepassar,vamoscolocaressacondiçãodestringvazianocomeço
dométodo convert:
public Dinheiro convert(String value, ...) {
if (Strings.isNullOrEmpty(value)) { return null; }
for (Moeda moeda : Moeda.values()) { ... }
throw new ConversionError(...);
Ostestespassameesgotamososcasosquequeremossuportarnoconverter.Com
oapoiodostestes,agoraconseguimosrefatoraraclasse DinheiroConvertersem
medo.Fazertestesduranteodesenvolvimentoéessencialparaquetenhamossegu-
rançaparaevoluirosistemasemquebrarcomportamentosexistentes.Alémdisso,
aousarmosociclodoTDDconseguimoscriarclassescomumdesignmelhor,mais
simplesdeusare,maisainda,ganhamosumadocumentaçãovivasobreoqueaclasse
faz:bastaleroscasosdeteste.ParasabermaissobreTDD,existeolivro“TestDriven
DesignemJava”porMaurícioAniche,pelaCasadoCódigo,alémdasreferências,
eminglês,“TDDbyExample”doKentBecke“GrowingObjectOrientedSoftware
GuidedbyTests”deNatPryce.
152

## Página 161

CasadoCódigo Capítulo10.Melhorandoodesigndaaplicação:ConversoreseTestes
10.2 Testes de unidade em projetos que usam VRap-
tor
Na seção anterior, vimos como criar testes usando TDD para a classe
DinheiroConverter.Essetipodetestesdeveriaserfeitoparatodasasclassesdo
sistema,paragarantirquecadaunidade(classe,método,funcionalidade)funcione
isoladamente.ComoaplicarissoparaasclassesdeumprojetoqueusaVRaptor?
U mdosgrandespilaresdoVRaptoréainjeçãodedependências,quevimosem
detalhesnocapítulo4. Porcausadisso,amaioriadasclassesdosistemanão de-
pendedenadadoVRaptor: são componentes( @Component)quedependemde
outroscomponentesdaaplicação. Sejuntarmosissoàpraticadesempredepender
deinterfaces,temosclassesindependentesdasimplementações dassuasdependên-
cias.
Comisso,ganhamosdegraçaumamelhortestabilidadedasclasses.Porexemplo,
paratestarmosaclasse AcervoNoAdminquecriamosdentrodo livraria-site,
temoscomodependênciaum ClienteHTTP:
public class AcervoNoAdmin implements Acervo {
private ClienteHTTP http;
public AcervoNoAdmin(ClienteHTTP http) {
this.http = http;
}
public List<Livro> todosOsLivros() {...}
}
EssaclassefazumarequisiçãousandoesseclienteHTTPeesperaumresultado
emxml,queéconvertidoparaumalistadelivros. Paratestaressaclasseisolada-
mente,podemospassarumaimplementaçãofalsadainterfaceClienteHTTPquere-
tornaumxmldeterminado:
@Test
public void converteUmaListaComApenasUmLivro() {
ClienteHTTP http = new ClienteHTTP() {
@Override
public String get(String url) {
return
"<livros>" +
153

## Página 162

10.2.TestesdeunidadeemprojetosqueusamVRaptor CasadoCódigo
"<livro>" +
"<titulo>VRaptor 3</titulo>" +
"<isbn>12345</isbn>" +
"</livro>" +
"</livros>";
}
};
AcervoNoAdmin acervo = new AcervoNoAdmin(http);
List<Livro> livros = acervo.todosOsLivros();
assertThat(livros.size(), is(1));
Livro livro = livros.get(0);
assertThat(livro.getTitulo(), is("VRaptor 3"));
assertThat(livro.getIsbn(), is("12345"));
}
Paraevitaracriação declassesparacadacenáriodetestes,podemosusarfra-
meworksde Mocks,umdosnomesdadosaessasimplementações falsasusadasem
testes.U mdessesframeworkséo Mockito(http://mockito.org),quesimplificariao
testepara:
import static org.mockito.Mockito.*;
//...
@Test
public void converteUmaListaComApenasUmLivro() {
ClienteHTTP http = mock(ClienteHTTP.class);
when(http.get(anyString())).thenReturn(
"<livros>" +
"<livro>" +
"<titulo>VRaptor 3</titulo>" +
"<isbn>12345</isbn>" +
"</livro>" +
"</livros>"
);
//...
}
Seguindoessaideia,podemosfazerotestedamaioriadoscomponentesdaapli-
154

## Página 163

CasadoCódigo Capítulo10.Melhorandoodesigndaaplicação:ConversoreseTestes
cação,usandoqualquertécnicadetestesparaobjetosemgeral.Aexceçãodissosão
osControllers,quegeralmentedependemde Resulte Validator.Essasinter-
facessãoumpoucomaisdifíceisdemockar,poistêmumainterfacefluente:
result.redirectTo(LoginController.class).formulario();
validator.onErrorRedirectTo(this).lista();
Omockdeumadessaschamadas,usandoomockito,seriaalgocomo:
LoginController mockController = mock(LoginController.class);
when(result.redirectTo(LoginController.class)).
thenReturn(mockController);
verify(mockController).formulario();
Senãofizermospelomenosasduasprimeiraslinhas,aexecuçãofalhacomuma
NullPointerException. Seestivermosusandooutrotipoderesultado,como
xmloujson,aconfiguraçãodosmocksficaaindamaisdifícil.Paraevitarisso,po-
demosusarasversões mockadasprovidenciadaspeloVRaptor,quejáignoramas
chamadasdoresultenosdeixaminspecionaralgunstiposdedados.Essesmocksdo
VRaptorficamnopacote br.com.caelum.vraptor.util.testeosprincipais
são:
•MockResult—umresultqueignoraosredirecionamentoseométodouse,
enquantopossibilitaainspeçãodetodososobjetosincluídos:
MockResult result = new MockResult();
//dentro do controller:
result.include("mensagem", "Tudo deu certo!");
//dentro do teste:
assertThat(result.included("mensagem"), is("Tudo deu certo!"));
•MockValidator-umvalidatorqueacumulaasmensagensadicionadase
lançaexceção no validator.onErrorUse(). Assim,podemosverificar
quehouveramerrosdevalidação:
MockValidator validator = new MockValidator();
LivrosController controller = new LivrosController(..., validator);
155

## Página 164

10.2.TestesdeunidadeemprojetosqueusamVRaptor CasadoCódigo
Livro livroSemTitulo = //...
try {
controller.salva(livroSemTitulo);
Assert.fail("Deveria ter dado erro de validação");
} catch (ValidationException e)
assertThat(e.getErrors().size(), is(1));
Message message = e.getErrors().get(0);
assertThat(message.getCategory(), is("titulo"));
}
•MockSerializationResult—igualao MockResult,mastambémper-
miteinspecionarosdadosdeumobjetoserializado:
MockSerializationResult result = new MockSerializationResult();
//no controller
result.use(Results.json()).from(livro).serialize();
//no teste
assertThat(result.serializedResult(), is(
"{\"livro\": { \"titulo\": \"VRaptor 3\", ... }}"
));
•JSR303MockValidator —igual ao MockValidator, mas
também executa as validações do BeanValidations (chamadas ao
validator.validate(objeto)).
Dessemodo,conseguimostambémtestaroscontrollerssemmuitosproblemas
emanterumaboacoberturadetestespelaaplicação.
156

## Página 165

Capítulo11
Próximospassos
Terminamos,aqui,odesenvolvimentodanossalivraria,quefoioprojetoqueusa-
mosparaacompanharesselivroeexpôramaioriadasfuncionalidadesdoVRaptor.
Masnãopodemospararporaqui,poiscadaprojetoquefazemostemcaracterísticas
diferentes,resolveproblemasdiferentes,exigecoisasdiferentes.
ParacontinuaraconhecermaissobreoVRaptor,podemosseguirosseguintes
passos:
•L e i aos apêndicesdeste livro.Nosapêndices,temosumavisãogeraldosplu-
ginsdoVRaptor,queauxiliamodesenvolvimentodeaplicações comoVRap-
tor,umaexposiçãodetodososcontainersdeinjeçãodedependênciassuporta-
dospeloVRaptor,exemplosdecomousarAJAXcomoVRaptoreumpouco
sobreofuncionamentointernodoVRaptor,comseuscomponentesesuas
funções;
•L e i aa documentação do VRaptor. A p e s a rdenão estarcompleta,adocu-
mentação doVRaptor,quepodeserencontradaemhttp://vraptor.caelum.

## Página 166

CasadoCódigo
com.bréumaboareferênciaparavermosasfuncionalidadesdoVRaptor.
Alémdadocumentaçãoexisteolivrodereceitas,comasoluçãoparaalguns
problemascomunsdodia-a-dia;
•Contribua com a documentação do VRaptor. Colocarnopapel(mesmo
quesejadigital)oquevocêconheceajudaaconsolidaroseuconhecimento
eajudaraosoutros. Portanto,escrevaumblogtécnicocomosproblemas
esoluções quevocêadotou,contribuacomumasolução paraolivrodere-
ceitasdoVRaptor,ajudeamelhoraradocumentação existente,emhttps:
//github.com/caelum/vraptor/tree/gh-pages;
•Participe da lista de discussões do VRaptor. Cada vez que aparecer
uma dúvidaou um problema duranteo desenvolvimentodas suas apli-
cações, oumesmosevocêtiversugestões ouquiserchamarumadiscus-
são, acompanhe e mande mensagens para a lista de discussões caelum-
vraptor@googlegroups.com. T e n t a rresolveroproblemadeoutraspessoas
tambémajudabastanteaconhecernovasformasdetrabalharcomoVRap-
toreaprendercadavezmais;
•Crie e responda t ó p i c o sno GUJ.Oguj.com.bréomaiorforumdeJavaem
português,entãosemprequetiverumadúvidaqueenvolva,nãosóoVRaptor,
masqualquerbibliotecaquevocêestiverusandonaaplicação,vocêpodeusar
oconhecimentodascentenasdemilharesdeusuáriosdoGUJ.Pesquisese
jáexisteumtópicoquerespondeasuadúvidae,senãoexistir,crieumnovo
tópico.Nãoseesqueçadepostarstacktraces,casoestejamacontecendoerrose,
sepossível,posteopedaçodocódigoondevocêachaqueestejaacontecendoo
problema.SeotópicoérelacionadoaoVRaptor,useofórumde Ferramentase
bibliotecasbrasileiras.Nãoseesqueçaderetribuirofavoreresponderadúvida
deoutraspessoas!
•Crie e responda perguntas no GUJ.Oguj.com.brpossuiummododeper-
guntaserespostas,ohttp://www.guj.com.br/perguntasquetambémébastante
interessanteparaobtermosarespostaparanossasdúvidas.Sejaencontrando
umaperguntajáexistenteoucriandoumanova.Ganhepontoseorespeitode
outrosdesenvolvedoresrespondendoperguntas!
•Sugira novas funcionalidades e rep or tebugs.Asuaopiniãoémuitoimpor-
tanteparaodesenvolvimentodoVRaptor,então semprequesentirfaltade
158

## Página 167

CasadoCódigo Capítulo11.Próximospassos
algumafuncionalidadeouencontrarumbugnoVRaptor,mandeumamensa-
gemnalistadediscussões dodesenvolvimentodopróprioVRaptor,acaelum-
vraptor-dev@googlegroups.com,paraverseafuncionalidadejáexiste,sejano
VRaptorouemalgumdeseusplugins,eseobugpossuialgumaformadeser
contornado.Sepreferir,podeabrirumticketdenovafuncionalidadeoude
bugdiretamentenorepositóriodoVRaptor,emhttps://github.com/caelum/
vraptor/issues;
•Contribua desenvolvendo pa rao VRaptor.OcódigofontedoVRaptorestá
noGithub,queé,semdúvida,amelhorferramentadecompartilhamento
decódigoquetemosatualmente. U m aótimaformadeentendermelhoro
VRaptoréolhandooseucódigofonte,emhttps://github.com/caelum/vraptor.
OVRaptorpossuiumaótimasuitedetestes,queexemplificammuitobem
ousodecadafuncionalidade,alémdegarantirqueelasestão funcionando.
Comisso,alémdeaprendermaissobreoVRaptor,tambémservederefe-
rênciasobreformasdeescrevertestesemJava. Quandosesentirconfortá-
vel(nãohesiteempostardúvidassobreocódigodoVRaptornalistadede-
senvolvimentocaelum-vraptor-dev@googlegroups.com),escolhaalgumdos
ticketsemhttps://github.com/caelum/vraptor/issueseimplemente-o,abrindo
umForknoGithubemandandoPullRequests.Sevocêjátemumaideiade
funcionalidadeoujáencontrouumbug,podemandarPullRequestsmesmo
queelesnão tenhamsidoreportadosainda. Durantearevisão doseuPull
Request,vocêaindapodeganhardicasdedesign,decomoescrevertestes,de
comocontribuirmelhorparaprojetosopen-source;
•Escreva e divulgue plugins.Conformevistonoapêndicedeplugins,oVRap-
torpossuiummecanismoquefacilitaacriação eadistribuição deplugins.
Então sevocêcriouumconjuntodecomponentesquepodeserreutilizado
paraoutrasaplicações, crieumpluginedivulgue-onorepositóriodeplugins:
https://github.com/caelum/vraptor-contrib.
•Continue lendo e estudando. Mantenha-seatualizadoesejaumdesenvol-
vedorcompleto.Conhecerastécnicasparaimplementarumbomback-end
éessencial,massabercomofazerumfront-endagradávelparasuaaplicação
podeserumgrandediferencialeclaro,otornarumdesenvolvedorcommuito
maisconhecimentoedomíniodoseutrabalho.AEditoraCasadoCódigotem
diversosoutroslivrosquecobremtantooback-endcomoofront-end.Não
deixedeverseéocaminhoadequadoparacontinuarseusestudos.
159

## Página 168

CasadoCódigo
Muitoobrigadoporlerestelivro,esperoqueeletenhateajudadoaconhecerou
seaprofundarnoVRaptor.Osuaopiniãoémuitoimportante,tantoparaestelivro
quantoparaopróprioVRaptor,entãosequisernosdarseufeedbackusealistade
discussãocaelum-vraptor@googlegroups.com.
Muitoobrigado,também,avocêquecontribuiuparaoVRaptor,sejaescrevendo
código,documentação,respondendodúvidasdeoutraspessoas,divulgandoplugins,
ousimplesmenteusaerecomendaoVRaptorparaoutraspessoas.
Agradecimentosespeciaisaosirmão PauloeGuilhermeSilveira,porcriarem
eincentivaremoVRaptorepormechamaremparatrabalharnaCaelumquando
eueraapenasumestudantedeCiênciasdaComputação,aoFabioK u n g ,porsero
grandeevangelistadoVRaptor2,aoOtávioGarciaportermeajudadoacoordenar
odesenvolvimentodoVRaptornosúltimosanos,àCeciFernandes,poraguentar
minhaspiadasruinsdesdeotempodafaculdade,aoPedroMatiello,pelomesmo
motivoeporajudararevisarestelivro,aoAdrianoAlmeida,pormedeixarescrever
esselivro,àminhafamíliaeàminha(futura)esposaMelissaportodooapoio.
=)
160

## Página 169

Capítulo12
Apêndice:Melhorandoa
usabilidadedaaplicaçãocomA J A X
Foi-seotempoemqueosusuáriosapenasseguiamlinksesubmetiamformuláriosna
W e b .Hojeemdia,todomundoesperaqueumaaplicaçãoW e btenhaumainterface
rica,comcomponentesinteligenteseinterações suaves. Issoporquetransferimos
grandepartedasaplicações queeramtipicamenteDesktopparaaW e beprecisamos
manter,emesmomelhorar,ausabilidadedessasaplicações.
Porumtemposesupriuessanecessidadecompequenasaplicações emFlash,
queerambastantelentasetinhammúsicaseanimações totalmentedesnecessárias,
comofamoso“pularintrodução”.Agoraqueamaioriadainternetnão usamais
ofamigeradoInternetExplorer6,temoscondiçãodecriarinterfacesricasusando
apenasoqueobrowsernosdá:HTML,CSSeJavascript,comaajudadealgumas
bibliotecasJavascript,éclaro.
U m adasprincipaisbibliotecasJavascriptéojQuery,quepossuidiversosplugins
ecomponentesvisuaisquefacilitammuitootrabalhodeumdesenvolvedorW e b .

## Página 170

CasadoCódigo
Alémdisso,existembibliotecasparafacilitaraescritadoCSScomooLESSouo
SASS.ParaescreverHTMLemJavatemosoJSPcomJSTLoupodemosusaroutras
ferramentascomoFreemarkerouVelocity.
OVRaptoréumframeworkMVCqueestruturaaformaemqueosControllers
vãotrabalhar,facilitamodesenvolvimentodacamadadeModelocomcomponentes
einjeção dedependênciase,napartedacamadadeVisualização, oVRaptornos
provêformasdeseintegrarfacilmentecomqualquerumadasbibliotecas. Maso
VRaptordeixalivreaescolhadasbibliotecasdevisualização,oquetambémsignifica
queelenãovemcomnenhumadelasporpadrão,alémdoJSPeJSTLdoservidor.
Nessecapítulo,veremosalgumasformasdeinteraçãocomacamadadevisualiza-
ção,usandoabibliotecajavascriptjQuery,masnãoiremosmuitoafundo,poisfoge
doescopodestelivro.OutroslivrosdaCasadoCódigoajudamnessaparte,como
porexemploo“DominandoJavaScriptcomjQuery”,escritopeloPlínioBalduíno.
Importantesalientarquevocê,comodesenvolvedorW e b ,nãoprecisanecessa-
riamenteserumásdeHTML,CSSeJavascript,masémuitoimportanteconhecer
oqueépossívelfazereconseguirtrabalharpelomenoscomobásicodessastecno-
logiasparaque,mesmoqueexistaumdesenvolvedorfront-endnasuaequipe,você
saibacomofazeraintegraçãocomaaplicaçãonoservidor.
O navegador não ro d aJSPs!
Resolvicolocaresse disclaimernolivro,poiséumaconfusãobastantecomum
dedesenvolvedoresJavaquetrabalhamparaaW e b ,principalmentenocomeçoda
carreira.Quandoeditamosaspáginasdosistema,usamosumarquivoJSP,queéo
templatepadrãoparacriarpáginasHTMLemJava.
MasoJSPéapenasumaferramentaparafacilitarageraçãodinâmicadeHTML
doladodoservidor,comousodevariáveis,ifs, forseetc.Noentanto,oJSProda
apenas do lado do servidor,ouseja,éexecutadousandoasvariáveisquepassamos
narequisiçãoegeraumHTML,queéenviadoparaonavegador.Ouseja,quando
vemosapáginanonossobrowser,oqueestamosvendoéoHTMLgeradopeloJSP
correspondente,enãomaisoJSP!
Issosignificaque,umavezqueoHTMLfoiparaonavegador,nãotemosmais
acessoavariáveisnemaestruturasdoJSP.Sequisermosexecutaralgumalógicaque
modificaoselementosdapágina,precisamosusarJavascript,queéalinguagemde
programaçãodisponívelnobrowser.
Paraficarclaro:oJSPéexecutadodoladodoservidorparaproduzirumHTML.
EsteHTMLéenviadoparaonavegadorquefezarequisiçãoeapáginageradaserá
162

## Página 171

CasadoCódigo Capítulo12.Apêndice:MelhorandoausabilidadedaaplicaçãocomAJAX
mostrada.Paramelhorarausabilidadeeinteragircomoselementosdapáginasem
sairdela,precisamosusarJavascript,poisoJSPnãoestámaisdisponível.
12.1 Executanto u m a operação pontual : Remoção
de livros
Nonossosistema,temosumalistagemdelivros,ondeconseguimosveralgumasdas
informações cadastradasnesseslivros.Estalistagemégeradapeloseguintecódigo
JSP:
<h3>Lista de Livros</h3>
<ul>
<c:forEach items="${livroList}" var="livro">
<li>
<img
src="${linkTo[LivrosController].capa[livro.isbn] }"
width="70" height="100"/>
${livro.titulo} - ${livro.descricao} -
<a href="${linkTo[LivrosController].edita[livro.isbn] }">
Modificar
</a>
</li>
</c:forEach>
</ul>
Eproduzalistagemdelivros.
V a m o smodificarestalistagemparaincluirumlinkpararemoçãodolivroem
questão.Esselinkseráincluídoapósolinkdemodificarolivro:
<c:forEach items="${livroList}" var="livro">
<li>
...
<a href="${linkTo[LivrosController].edita[livro.isbn]}">
Modificar
</a>
-
<a href="${linkTo[LivrosController].remove[livro.isbn]}">
Remover
163

## Página 172

12.1.Executantoumaoperaçãopontual:Remoçãodelivros CasadoCódigo
</a>
</li>
</c:forEach>
Paraissofuncionar,precisamoscriaressenovométodonocontroladorseguindo
ainterfaceREST,ouseja,usandoométodohttpDELETEecomaURLdeumlivro
específico:
@Resource
public class LivrosController {
//...
@Delete("/livro/{isbn}")
public void remove(String isbn) {
Livro livro = estante.buscaPorIsbn(isbn);
estante.retira(livro);
}
}
Essenovométodocriaalgunsproblemas:Primeiro,ométodoéDELETEmas
estamosusandoumlink,queexecutaométodoGET.Pelomenosdeveríamosestar
usandoométodoPOST,poisestamosmodificandoalgonoservidor. Osegundo
problemaéque,mesmoqueconsigamosexecutarométodo remove,oquedeve
acontecer,visualmente?Poderíamoslevarparaumapáginadizendoqueoproduto
foiremovidocomsucessooupoderíamosredirecionardevoltaparaalistadelivros,
agoracomolivroemquestãoremovido.Nesteúltimocaso,estamoscarregandoa
páginainteiraparaapenasapagarumdositensdalista.
PodemosmelhoraressausabilidadeusandoJavascript:aoclicarem“Remover”,
fazemosarequisiçãoaoderemoçãodolivroe,sedertudocerto,apagamosalinha
dolivro,semsairdapágina!V a m o sfazerissocomaajudadojQuery,quefacilita
bastanteessetipodeoperações. ComocriamosoprojetousandooVRaptorScaffold,
ojQueryjáestáincluídomas,casotivéssemoscriadooprojetodeoutramaneira,
precisaríamosbaixarojQuery(http://jquery.com/download)eincluí-lonapágina.
Antesdepoderexecutarojavascript,precisamosprepararanossalistagempara
facilitarainteraçãocomoselementos.U mdosjeitosdefazerissoédandoidsou
classesparaoselementosqueserãoimportantesparaanossalógicajavascript.Ids
precisamserúnicosnapágina,ouseja,sópodemoscolocá-losemelementosquenão
164

## Página 173

CasadoCódigo Capítulo12.Apêndice:MelhorandoausabilidadedaaplicaçãocomAJAX
serepetem,comoéocasodalista.Classespodemsercolocadasemvárioselementos,
portantovamosusá-lasnositensdalistaenolinkderemoção:
<ul id="livros">
<c:forEach items="${livroList}" var="livro">
<li class="livro">
...
<a href="${linkTo[LivrosController].edita[livro.isbn] }">
Modificar
</a>
-
<a class="remove"
href="${linkTo[LivrosController].remove[livro.isbn] }">
Remover
</a>
</li>
</c:forEach>
</ul>
Paraadicionarocomportamentoaolinkderemoção,precisamoscolocarcódigo
javascriptoudentrodeumatag <script>dentrodapágina,ouemumarquivo
.jsseparadoquevamosincluirnapágina.Paraficarmaissimples,vamosfazera
primeiraopção:
<script>
...
</script>
EstecódigoprecisarodardepoisqueobrowsertiverlidooHTMLdalista,então
ocolocamosdentrodoblocodeinicializaçãodojQuery:
<script>
$(function() {
//...
});
</script>
Agoraprecisamosadicionarumcomportamentoatodososlinksderemoção.
Eessecomportamentoserádisparadoassimqueclicarmosnolink. Paraisso,va-
mos,dentrodalistagemdelivros( #livros),procurartodososlinksderemoção(
.remove)eexecutarumcódigoaoclicar:
165

## Página 174

12.1.Executantoumaoperaçãopontual:Remoçãodelivros CasadoCódigo
$(function() {
$("#livros .remove").on("click", function() {
});
});
#livrosindicaoelementocomoid livrose .removeindicatodososele-
mentosquetêmaclasse remove.Aofazermos $("#livros .remove")estamos
representandotodososelementosdaclasse removequeestãodentrodoelemento
#livros.Orestodaexpressãodizque,aoclicar( on("click"),vamosexecutara
funçãopassada.
A p e s a rdeserumlink, não queremosqueo Remover saiadapágina,en-
tãoprecisamosindicarquenãoqueremosessecomportamentopadrão,recebendo
umparâmetronafunção querepresentaoeventodocliqueechamandoafunção
preventDefault:
$("#livros .remove").on("click", function(event) {
event.preventDefault();
});
</script>
V a m o scuidarprimeirodapartevisualdaoperação: queremosquealinhado
livrosumaapósaremoção. Dentrodafunçãoquepassamosparatrataroclique,o
objeto thisserefereaoprópriolink.Tudooqueprecisamosfazeréacharalinha
dolivrocorrespondenteaolinkquefoiclicado.Comoolinkestádentrodo lido
livro,podemosusarométodo closest,queprocuraoprimeiropaidoelemento
quebatecomoseletorpassado.ParanãodependerdoelementoHTMLqueusamos,
vamosusaraclasse livro:
$("#livros .remove").on("click", function(event) {
event.preventDefault();
var livro = $(this).closest(".livro");
});
Comoelementodolivroemmãos, podemosescondê-lousandoométodo
fadeOut,quefazcomqueoelementosumaaospoucos:
$("#livros .remove").on("click", function(event) {
event.preventDefault();
166

## Página 175

CasadoCódigo Capítulo12.Apêndice:MelhorandoausabilidadedaaplicaçãocomAJAX
var livro = $(this).closest(".livro");
livro.fadeOut();
});
Pronto,agoraaoclicarnolink,alinhadolivrovaisumir. Masapenasmani-
pulamosoHTMLdobrowser,nadafoienviadoaoservidor.Precisamosexecutara
requisiçãoqueremove,defato,olivro,massemsairdapágina.Atécnicaqueusamos
parafazerissoéoquechamamosdeAJAX,queoriginalmentesignifica A s y n c hro-
nous Javascript A n dXML,ouseja,umarequisição assíncronaqueusaJavascripte
XML,maspodeusaroutrascoisasalémdeXMLparatrafegarosdados,comopor
exemploJSON.
Ocódigonativoparageraressarequisição AJAXnobrowseréumpoucotra-
balhoso,maspodemosusarojQueryparafacilitaressetrabalho,atravésdafunção
$.ajax.Passamosparaessafunçãoumobjetocontendoosatributosdarequisição,
comoaURLaserchamada,ométododarequisiçãoeosparâmetros.Nonossocaso
aURLdarequisiçãoéamesmadolinkqueclicamos,econseguimosacessá-laatravés
doatributo href:
$("#livros .remove").on("click", function(event) {
// ...
$.ajax({
url: $(this).attr("href")
});
});
Porpadrão, essarequisição usaráométodo GET,masprecisamosdométodo
DELETE.Oatributoparamudarométododarequisição éo typeepoderíamos
mudá-lo:
$("#livros .remove").on("click", function(event) {
// ...
$.ajax({
url: $(this).attr("href"),
type: 'DELETE'
});
});
167

## Página 176

12.1.Executantoumaoperaçãopontual:Remoçãodelivros CasadoCódigo
Emboraissosejapossível,nãoésuportadoportodososbrowsers.Paragaran-
tirquevaifuncionar,podemostrocarométodopara POSTeusaroparâmetro
_method: DELETE,quepodemospassaratravésdoatributo data:
$("#livros .remove").on("click", function(event) {
// ...
$.ajax({
url: $(this).attr("href"),
type: 'POST',
data: { _method: "DELETE" }
});
});
Dessaforma,executamosarequisiçãoAJAXquevairemoverolivrodobancode
dados.Comoessarequisiçãoéassíncrona,ocódigonãoficaesperandoelaacabar.
Alémdisso,arequisiçãopodeterminarcomsucessooudaralgumerro.Sequisermos
tratarcadaumdessescasos,precisamoscontinuaraconfiguraçãodo $.ajax.
Paraisso,podemospassarfunções queserãochamadasassimquearequisição
terminarcomsucesso,oucomerro,ousimplesmenteterminar. Chamamosessa
funçãode callback,poisseráchamadaassimquearespostadarequisiçãovoltar:
$.ajax({
url: $(this).attr("href"),
type: 'POST',
data: { _method: "DELETE" }
}).done(function(data, textStatus, jqXHR) {
// executada em caso de sucesso
}).fail(function(jqXHR, textStatus, errorThrown) {
// executada em caso de erro
}).always(function() {
// executada assim que a requisição termina,
// seja com sucesso ou com erro
});
Nonossocaso,sóqueremosremoveralinhadolivrocasoarequisiçãosejacom
sucesso.Emcasodeerro,podemosapenasmandarumamensagemdealertaparao
usuário.Ocódigocompletoficaria:
$("#livros .remove").on("click", function(event) {
event.preventDefault();
168

## Página 177

CasadoCódigo Capítulo12.Apêndice:MelhorandoausabilidadedaaplicaçãocomAJAX
var livro = $(this).closest(".livro");
$.ajax({
url: $(this).attr("href"),
type: 'POST',
data: { _method: "DELETE" }
}).done(function(data, textStatus, jqXHR) {
livro.fadeOut();
}).fail(function(jqXHR, textStatus, errorThrown) {
alert("O Livro não foi removido!");
});
});
Dessaforma,completamosaremoção dolivrousandoAJAX,pelomenosna
partedobrowser.Napartedoservidor,tudooqueprecisamoségerarumaresposta
comsucesso,casoolivrotenhasidoremovido.Nãoprecisamosmostrarumapágina
nemredirecionararequisição.Paraisso,usamosométodo result.nothing().
@Resource
public class LivrosController {
//...
@Delete("/livro/{isbn}")
public void remove(String isbn) {
Livro livro = estante.buscaPorIsbn(isbn);
estante.retira(livro);
result.nothing();
}
}
ReparequeométododoControlleréummétodonormal,não precisadene-
nhumaconfiguração complicadapararesponderumachamadaAJAX.Omáximo
quefizemosfoidizerquenãovamosretornarnenhumresultado,alémdostatusde
169

## Página 178

12.1.Executantoumaoperaçãopontual:Remoçãodelivros CasadoCódigo
sucesso.Mascasoretornássemosalgumresultado,eleestariadisponívelnavariável
datadafunçãopassadaparao donedachamada ajax.
170

## Página 179

Capítulo13
Apêndice:ContainersdeInjeçãode
Dependência
U m adasprincipaiscaracterísticasdoVRaptoréquetodososcomponentesjánas-
cemcominjeção dedependênciasdisponível,demodoqueconseguimosreceber
peloconstrutortodasasclassesdasquaisumcomponenteouumcontrollerdepen-
dem.
Essacaracterísticaétão importantequeospróprioscomponentesinternosdo
VRaptorsão criadosecoordenadosusandoinjeçãodedependências.Noentanto,
fazeressecontroleéalgobastantecomplicadoe,porisso,oVRaptordelegaessa
responsabilidadeparaumcontainerdeinjeção dedependências,queéquemvai
criaregerenciartodososcomponentesdoVRaptoredaaplicação.
Existemvárioscontainersdisponíveisnomercado,cadaumcomumaforma
diferentedeconfiguração,cadaumcomseuconjuntodefuncionalidadesextras.E
paradarmaisopções paraqueoVRaptorseadequemelhoràsuaaplicação,existea
integraçãocomquatrocontainersdiferentes:oPicoContainer,oSpring,oGuicee,

## Página 180

13.1.PicoContainer CasadoCódigo
aindaemfasedetestes,oCDI.
Parainstalarcadaumdessescontainers,sóénecessárioadicionarosjarsdocon-
tainernoclasspath,queoVRaptordetectaocontainerautomaticamente.Éimpor-
tantequenãoexistamjarsdosoutroscontainers,paraqueoVRaptorpossaescolher
ocontainercorreto. Aexceção dessaregraéoCDI,quetemumainstalação um
poucomaiscomplicada,conformeveremosaseguir.
Asclassesquefazemaintegraçãocomoscontainerssechamam Providersno
VRaptor.Nestecapítulo,vamosverascaracterísticaseasfuncionalidadesextrade
cadacontainer.
13.1 PicoContainer
OPicoContainerfoiumdosprimeiroscontainersdeinjeçãodedependênciaque
surgiramemJavaesuaprincipalcaracterísticaéserextremamenteleve. Eleéfo-
cadoapenasnainjeçãodedependênciasefazissodamaneiramaissimplespossível:
registramosimplementações paraoscomponentes,etodaainjeçãoéfeitapelocons-
trutor.
Sefôssemosconfigurá-loparacriarobjetosdonossosistema,essaconfiguração
poderiaser:
MutablePicoContainer container = new DefaultPicoContainer();
// interface implementação
container.addComponent(Acervo.class, AcervoNoAdmin.class);
container.addComponent(ClienteHTTP.class, URLClienteHTTP.class);
Acervo acervo = container.getComponent(Acervo.class);
Paraqueaconfiguraçãosejasimplesassim,asdependênciasprecisamserrece-
bidasnoconstrutor,quetambéméopadrãodoVRaptor.
OProviderdePicoContainer( PicoProvider)foioprimeiroaserimple-
mentadonoVRaptor3,justamenteporseromaissimplesdeconfigurarejáterum
padrãobomaserseguido.Paraconseguirmosimplementarosescopos( request,
sessione application)usamosafuncionalidadedecontainersfilhos(child
containers),naqualosfilhosconseguemusarasdependênciasdopaimasopainão
consegueusarasdependênciasdosfilhos.
Opaidetodoséocontainerdo @ApplicationScoped.Todososoutrosesco-
posconseguemrecebercomodependênciaum @ApplicationScoped,masnãoo
172

## Página 181

CasadoCódigo Capítulo13.Apêndice:ContainersdeInjeçãodeDependência
contrário.U mcomponentenoescopodeaplicaçãopodesercriadoforadeumare-
quisição,portantonãopoderecebercomodependênciaumcomponentedeescopo
derequisiçãooudesessão.Outromotivoéque,mesmoquepudesse,adependência
sóvaleriaparaaprimeirarequisição,apósissoestariadestruídaeocomponentede
escopodeaplicaçãoestariausandocomodependênciaumobjetodestruído.
OproviderdePicoContainernãopossuifuncionalidadesextra,justamentepor-
queelesefocanainjeçãodedependênciaapenas.Poressemotivo,éoprovidermais
rápidodosimplementadosnoVRaptor.
13.2 Spring IoC
OSpringéumframeworkcriadohámaisde10anosparafacilitarodesenvolvimento
deaplicações JavaesuprirasváriasdeficiênciasqueexistiamnoJ2EE(atualJavaEE).
ÉumadasbibliotecasmaisfamosasnomundoJava,principalmenteporserextrema-
mentemodularizadoepossuirmódulosqueresolvemosmaisvariadosproblemas
queenfrentamosaodesenvolveraplicações Java.
Omódulomaisimportanteéo I o C(Inversion o fControl),quecuidadainjeção
dedependências.ÉomódulocentraldoSpring,quecoordenatodososcomponentes
dosoutrosmódulos. ÉtambémomóduloqueoVRaptorusaparaimplementaro
providerdeinjeçãodedependênciasqueusaoSpring.
AssimcomooPicoouoGuice,usaroSpringcomoproviderétotalmentetrans-
parente,nãomudanadadousodoVRaptor,dacriaçãodoscomponentesoudain-
jeção peloconstrutor.Noentanto,porrodardentrodoSpring,temosapossibili-
dadedeusarqualquerumdosmódulosdoSpringintegradosautomaticamentecom
oscomponentescriadospeloVRaptor,evice-versa.Bastaconfigurarosmódulose
componentesnoSpringeelesjáficamdisponíveisparainjeçãodedependênciasnos
componentesdoVRaptor.
Podemosusaralgumasdasanotações doSpringautomaticamente,semaneces-
sidadedeconfigurações adicionais.Éocasodo @Autowired,quehabilitaainjeção
viasetter,atributoouinitmethod:
@Component
public class MeuComponenteNoVRaptor {
@Autowired
private Estante estante;
173

## Página 182

13.2.SpringIoC CasadoCódigo
@Autowired
public void setAcervo(Acervo acervo) {...}
@Autowired
public void inicializa(Result result, Validator validator) {...}
}
OSpringfoicriadonumaépocaemqueoJavaeraapenasumaferramentapara
transformargrandesquantidadesdeXMLemstacktraces,portantoseumeioprin-
cipaldeconfiguração éumXMLondedefinimosocontextodaaplicação. Para
queessaconfiguraçãoseintegreautomaticamentecomoVRaptor,precisamoscriá-
lanumarquivochamado applicationContext.xmlnoclasspath(ex. pasta
src/main/resources).
U m aboaconfiguraçãoquepodemoscolocarnessexmléaquehabilitaacriação
decomponentesviaanotações, aumentandobastanteaprodutividadediminuindo
consideravelmenteanecessidadedeeditaroarquivodeconfigurações:
<?xml version="1.0" encoding="UTF-8"?>
<beans
xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:context="http://www.springframework.org/schema/context"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context-3.0.xsd"
>
<context:component-scan base-package="br.com.casadocodigo.livraria"/>
</beans>
Assim,podemoscriareconfigurarcomponentesusandoasanotações doSpring,
porexemplo,usando @Repositoryou @Service. Mas,aocriarcomponentes
usandooSpring,vocêestásujeitoaosseuspadrões: nenhumainjeçãoéautomáticae,
mesmoquesejapeloconstrutor,éprecisoanotaradependênciacom @Autowired.
Oescopopadrãoéo“singleton”,equivalenteao @ApplicationScopeddoVRap-
tor,entãosequisermosmudaroescopousamosaanotação @Scope.
174

## Página 183

CasadoCódigo Capítulo13.Apêndice:ContainersdeInjeçãodeDependência
Paraexemplificaraintegração comumdosmódulosdoSpring,vamosusaro
Spring Transaction,quehabilitaousodaanotação @Transactionalparacon-
trolarastransações nosmétodosdoscomponentes.Assim,seeuestounumDAOe
queroumatransaçãoemvoltadométodo salva,faríamos:
@Component
public class JPALivroDAO implements LivroDAO {
@Transactional
public void salva(Livro livro) {
manager.persist(livro);
}
}
Se formos executar mais de uma operação no banco de dados, na classe
EstanteNoBancoDeDadosqueusao LivroDAO,poderíamosusarnovamentea
anotação @Transactional:
@Component
public class EstanteNoBancoDeDados implements Estante {
@Transactional
public void guarda(Livro livro) {
livroDao.adiciona(livro);
estoqueDao.entrada(livro);
}
}
Nessecaso,oSpringsabequenãoprecisaabrirumatransaçãodentrodeoutra
eapenasabreatransação maisexterna. Paraquetudoissofuncione,precisamos
indicarno applicationContext.xmlquevamosusarospringtransactionale
queelevaiserconfiguradoatravésdeanotações:
<?xml version="1.0" encoding="UTF-8"?>
<beans
...
xmlns:tx="http://www.springframework.org/schema/tx"
xsi:schemaLocation="...
http://www.springframework.org/schema/tx
http://www.springframework.org/schema/tx/spring-tx-3.0.xsd">
175

## Página 184

13.2.SpringIoC CasadoCódigo
...
<tx:annotation-driven />
</beans>
Existemváriasmaneiraspossíveisdeseabrirecommitarumatransaçãocomo
bancodedados,cadaumadependendodatecnologiaqueusamosparasecomuni-
carcomele.Nonossocaso,precisamosfalarparaoSpringgerenciarastransações
usandoaJPA.EjáqueoSpringvaicontrolarastransações, precisamosqueeletam-
bémcontroleaaberturaeofechamentodos EntityManagers.
<tx:annotation-driven />
<bean id="transactionManager"
class="org.springframework.orm.jpa.JpaTransactionManager">
<property name="entityManagerFactory" ref="emFactory" />
</bean>
<bean id="emFactory"
class="org.springframework.orm.jpa.LocalEntityManagerFactoryBean">
<property name="persistenceUnitName" value="default"/>
</bean>
Dessaforma,precisamosmudarainjeçãodo EntityManagerparaserano-
tadacom @PersistenceContext.Nessecaso,vamosmudarainjeçãoporatri-
buto. Alémdisso,paratermosacessoao EntityManager parafazerconsul-
tasaobancodedados, precisamosgarantirqueeleestarádisponível,usandoo
@Transactional.Comoparaconsultasnãoprecisamosmodificarobanco,usa-
mosoatributo readonly:
@Transactional(readonly=true)
@Component
public class JPALivroDAO implements LivroDAO {
@PersistenceContext
private EntityManager manager;
@Transactional // para que ele não seja readonly nesse caso
@Override
176

## Página 185

CasadoCódigo Capítulo13.Apêndice:ContainersdeInjeçãodeDependência
public void adiciona(Livro livro) {
if (livro.getId() == null) {
this.manager.persist(livro);
} else {
this.manager.merge(livro);
}
}
@Override
public List<Livro> todos() {
return this.manager
.createQuery("select l from Livro l", Livro.class)
.getResultList();
}
@Override
public Livro buscaPorIsbn(String isbn) {
try {
return this.manager
.createQuery("select l from Livro l "
+ " where l.isbn = :isbn", Livro.class)
.setParameter("isbn", isbn)
.getSingleResult();
} catch (NoResultException e) {
return null;
}
}
}
PodemosusaresseequalqueroutromódulodoSpring,emconjuntocomos
componentescriadospeloVRaptor,pois,aousá-locomoSpringcomocontainer,
todososcomponentesdoVRaptoredasuaaplicaçãosãoregistradoscomobeansdo
Spring.AúnicadiferençaparaumbeannormaldoSpringsãoosescoposgerencia-
dospelasanotações doVRaptoreainjeçãoporconstrutorporpadrão.
AdesvantagememusaroSpringéque,porcontertantosmódulosefuncionali-
dades,ainjeçãodedependênciasébemmaislentaquenoGuiceounoPico,portanto
senãoforusarnenhumadasfuncionalidadesadicionaisdoSpring,oGuiceeoPico
sãoopções maisrápidas.
177

## Página 186

13.3.GoogleGuice CasadoCódigo
13.3 Google Guice
OGuice(pronunciadocomo‘juice’)éumabibliotecadeinjeção dedependências
disponibilizadapeloGoogleemhttps://code.google.com/p/google-guice/.OGuice
seaproveitadosistemadetiposdojavaparatornarsuaconfiguraçãoeoseuusomais
simples.Desdeaversão3.4doVRaptoréoproviderpadrãodoVRaptor.
AconfiguraçãodoGuicesedápormódulos,onderegistramosquaissãoasim-
plementações decadaumadasinterfacesqueusaremosnosistema. Paraanossa
livraria,seriaalgodotipo:
public class LivrariaModule extends AbstractModule {
@Override
protected void configure() {
bind(Estante.class).to(EstanteNoBancoDeDados.class);
bind(LivroDAO.class).to(JPALivroDAO.class);
bind(LivrosController.class);
//...
}
}
Aousaressaconfiguração,oGuiceobrigaqueospontosdeinjeçãosejamano-
tadoscom @Inject. Portanto,deveríamosanotartodososconstrutorescom
@Inject.ParapoderconseguirumainstânciacriadaegerenciadapeloGuice,cri-
amosuminjector:
Injector injector = Guice.createInjector(new LivrariaModule());
LivrosController controller =
injector.getInstance(LivrosController.class);
OproviderdoGuiceparaoVRaptor,noentanto,normalizaainjeçãodoGuice
parausarospadrões doVRaptor,comoosescoposeainjeçãoautomáticapelocons-
trutor. MaspodemosusarqualqueroutrorecursodoGuice,assimcomofizemos
comoSpring,jáqueoVRaptorrodadentrodoambientedeinjeçãodedependên-
ciasdoGuice.
ParainstalarumafuncionalidadeadicionaldoGuice,precisamosestendero
GuiceProviderdoVRaptoreconfiguraromoduloadicional:
public class CustomProvider extends GuiceProvider {
178

## Página 187

CasadoCódigo Capítulo13.Apêndice:ContainersdeInjeçãodeDependência
@Override
protected Module customModule() {
return new Module {
public void configure(Binder binder) {
// para manter o comportamento padrão do VRaptor
binder.install(super.customModule());
binder.install(new OutroModulo());
//...
}
};
}
}
ParaqueoVRaptoruseessaconfiguração,precisamosregistrarnoweb.xml:
<context-param>
<param-name>br.com.caelum.vraptor.provider</param-name>
<param-value>br.com.pacote.do.CustomProvider</param-value>
</context-param>
Mesmopossuindofuncionalidadesadicionais,quepodemserencontradasem
https://code.google.com/p/google-guice/wiki/Motivation,oGuicepossuiumaper-
formancemuitoparecidacomadoPico,sendoumaopçãodeproviderbastantevan-
tajosa.
13.4 CDI
OCDIéaespecificação doJavaquedizrespeitoàInjeção deDependênciasefoi
introduzidanojavaparaservidoresnoJavaEE6epossibilitaoacessodequalquer
classeatodososrecursosdosservidoresdeaplicaçãoqueantessóeramacessíveisa
EJBs.
EmclassesgerenciadaspeloCDI,podemosacessarEJBsdoservidor,usando
aanotação @EJB,receberum EntityManagerconfigurado,usandoaanotação
@PersistenceContext,acessaralgumrecursodoservidorcomooagendadorde
tarefas TimerService,comaanotação @Resource,eassimpordiante.
Podemos,ainda,usaroCDIemmodostandalone,ouseja,foradoservidorde
179

## Página 188

13.4.CDI CasadoCódigo
aplicação,comaajudadoW e l d ,suaimplementaçãodereferência.Assim,podemos
usá-loemaplicações webnormais,instaladasnoT o m c a tounoJetty.
OproviderdoCDIparaVRaptoraindanãofoioficialmentelançado,poisfaltam
algunsúltimosdetalhesparafacilitaroseuusoemaplicações feitascomoVRaptor.
Issoporqueeleobrigaquetodasasclassestenhamumconstrutorsemargumentos,
quetodoprojetotenhaumarquivochamado beans.xmlnapasta META-INFe
algumasoutrasexigências.
Maisinformações sobreesseproviderestão em: https://github.com/caelum/
vraptor-cdi-provider
Escolhaoproviderquemaisseadequaaoseuprojetoe,casováapenasusara
injeção dedependênciasdoVRaptor,todasasimplementações mantêmomesmo
comportamentocasovocêuseasanotações doVRaptor.
180

## Página 189

Capítulo14
Apêndice:PluginsparaoVRaptor
OVRaptoréumframeworkW e bMVCqueseconcentrabastantenapartedocon-
troller,ouseja,emtratarrequisições edispará-lasparaalgumdosControllersdasua
aplicação.Noentanto,oVRaptorrodadentrodeumcontainerdeinjeçãodedepen-
dências,ondevocêconseguecriardiversoscomponentesqueinteragementresipara
conseguirexecutartodaalógicadasuaaplicação.
Essaarquiteturadecomponentesfacilitabastanteoreúsodecomponentes,então
conseguimosusarasmesmassoluções desegurança,transações, controledeambi-
entes,relatóriosentrediversasaplicações diferentes.
Eparafacilitarocompartilhamentodessescomponentes,oVRaptorpossuiuma
funcionalidadeparacriareusarplugins,quesãoconjuntosdeclassesqueresolvem
algumproblemaepodemseradicionadosfacilmenteemqualqueraplicação. U m a
vezcriadooplugin,bastaadicionaroseujaraoclasspathetodososseuscomponen-
tespodemserusados.
Foicriado,também,umcatálogodetodosospluginsdoVRaptor,algunsque
nasceramdeprojetosdaprópriaCaelumeoutrosfeitospelacomunidadedeusuá-

## Página 190

14.1.VRaptorJPA CasadoCódigo
rios. EstecatálogoqueestádisponívelnoGithubemhttps://github.com/caelum/
vraptor-contribcontendoreferênciasaosrespectivosprojetosdospluginsnoGithub.
Nessecapítulo,vamosveralgunsdessesplugins,osoficiaiseosmaisutilizados,
masapartirdocatálogopodemosveradocumentaçãodecadapluginparaobteras
suasinformações deuso.
14.1 VRaptor JP A
Éopluginresponsávelporcriaregerenciaro EntityManagerparaquepossamos
executarasoperações nobancodedadosusandoaJPA.Ocódigofontedesteplugin
podeserencontradoemhttps://github.com/caelum/vraptor-jpa.
EstepluginestavadentrodojardoVRaptoratéaversão3.4,masfoiextraídona
versão3.5paratornarojardoVRaptormaissimplesedesacopladodoplugin.Para
usá-loprecisamosdoseujar,queestánorepositóriodoMavenepodemosusá-lo
declarandoasuadependênciaealgumadasimplementações daJPAnopom.xml:
<dependency>
<groupId>br.com.caelum.vraptor</groupId>
<artifactId>vraptor-jpa</artifactId>
<version>1.0.0</version>
</dependency>
<!-- Hibernate, OpenJPA ou alguma outra implementação da JPA -->
Oubaixeojardiretodorepositóriodomaven:
http://repo1.maven.org/maven2/br/com/caelum/vraptor/vraptor-jpa/
Comessepluginpodemossimplesmenterecebero EntityManagernocons-
trutordoscomponentesquesecomunicarãocomobancodedados:
@Component
public class LivroDAO {
private EntityManager manager;
public LivroDAO(EntityManager manager) {
this.manager = manager;
}
public void salva(Livro livro) {
182

## Página 191

CasadoCódigo Capítulo14.Apêndice:PluginsparaoVRaptor
this.manager.persist(livro);
}
}
Este EntityManagerseráabertoaocomeçodarequisiçãoefechadoaofinal
dela.Oplugintambémabreumatransaçãoaocomeçodarequisiçãoeautomatica-
mentefazo commitsetudodercertoouo rollbackcasoexistaalgumerrode
validaçãooualgumaexceptionlançada.
Parausaresteplugintambéménecessáriohaverum persistence.xmlcom
umapersistenceunitchamada default:
<?xml version="1.0" encoding="UTF-8"?>
<persistence xmlns="http://java.sun.com/xml/ns/persistence"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://java.sun.com/xml/ns/persistence
http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd"
version="2.0">
<persistence-unit name="default" transaction-type="RESOURCE_LOCAL">
<!-- Dados de conexão com o banco de dados -->
</persistence-unit>
</persistence>
Comoo EntityManagervivedurantearequisição,sópodeserusadoemcom-
ponentesquesão @RequestScoped(oescopopadrão),ou @PrototypeScoped
quesão usados em componentesde escopo de requisição. Caso seja necessá-
riousarum EntityManager emcomponentesdeoutrosescopos, recebaum
EntityManagerFactorynoconstrutorecontroleaaberturaeofechamentodo
EntityManagermanualmente,deacordocomasnecessidadesdocomponente.
14.2 VRaptor Hibernate e VRaptor Hibernate 4
Assimcomooplugin VRaptor JP A,estepluginestavadentrodojardoVRaptore
foiextraídoparaumpluginàpartenaversão3.5doVRaptor.Éopluginresponsável
porcriaregerenciara SessiondoHibernateparaacessarmosobancodedados.
ComooHibernatemudoubastanteasuaAPIdaversão3paraaversão4,temosdois
pluginsdiferentes,umparacadaversão:
183

## Página 192

14.2.VRaptorHibernateeVRaptorHibernate4 CasadoCódigo
•VRaptorHibernate:https://github.com/caelum/vraptor-hibernateparaaver-
são3doHibernate.Parausá-loadicioneaseguintedependêncianopom.xml:
<dependency>
<groupId>br.com.caelum.vraptor</groupId>
<artifactId>vraptor-hibernate</artifactId>
<version>1.0.0</version>
</dependency>
Oubaixe-odiretamentedomaven:
http://central.maven.org/maven2/br/com/caelum/vraptor/
vraptor-hibernate/
•VRaptor Hibernate 4: https://github.com/garcia-jj/
vraptor-plugin-hibernate4 para a versão 4 do Hibernate. Para usá-lo
adicioneaseguintedependêncianopom.xml:
<dependency>
<groupId>br.com.caelum.vraptor</groupId>
<artifactId>vraptor-plugin-hibernate4</artifactId>
<version>1.0.2</version>
</dependency>
Oubaixe-odiretamentedomaven:
http://central.maven.org/maven2/br/com/caelum/vraptor/
vraptor-plugin-hibernate4/
Ofuncionamentodessesdoispluginséidênticoebemparecidocomoplugin
daJPA:U m aSessionéabertaaoiníciodarequisiçãoefechadaaofinal.T a m b é m
éabertaumatransação aoiníciodarequisição efeitoocommitourollbackdela
aofinal,assimcomonoplugindaJPA.Parausá-lo,bastarecebera Sessionno
construtordocomponentedesejado:
@Component
public class LivroDAO {
private Session session;
public LivroDAO(Session session) {
this.session = session;
184

## Página 193

CasadoCódigo Capítulo14.Apêndice:PluginsparaoVRaptor
}
public void salva(Livro livro) {
this.session.save(livro);
}
}
T a m b é mé necessário ter o hibernate.cfg.xml ou o
hibernate.properties no classpath, para configurar as credenciais do
bancoeoutrosparâmetrosdoHibernate.
14.3 VRaptor Environment
Praticamentetodaaplicação quedesenvolvemoséexecutadaempelomenosdois
ambientesdiferentes:amáquinadodesenvolvedoreoservidordeprodução. Isso
quandonãoexistemoutrosambientescomotestes,QA,homologação,pré-produção,
entreoutros.Agrandemaioriadocódigodaaplicaçãodeveriarodardomesmojeito
independentedoambientequeestamosusando.
Noentanto,algumasconfigurações precisamserdiferentesemcadaambiente.
Talvezomaisóbviosejaobancodedados:nãoqueremosusaromesmobancode
produção enquantoestamosdesenvolvendoaaplicação. Alémdisso,precisamser
diferentesascredenciaisusadasparaenviare-mails,oendereçodealgumserviço
queaaplicaçãousa,presençaounãodecache,entreoutros.
Parafacilitaressamudançadeambientespodemosusaroplugin VRaptor En-
vironment,comocódigofonteedocumentação em: https://github.com/caelum/
vraptor-environment
Parainstalá-lo,assimcomoosoutros,colocamosasuadependêncianopom.xml:
<dependency>
<groupId>br.com.caelum.vraptor</groupId>
<artifactId>vraptor-environment</artifactId>
<version>1.1.4</version>
</dependency>
Oubaixandoojarem:
http://central.maven.org/maven2/br/com/caelum/vraptor/
vraptor-environment
Comessepluginnoclasspath,precisamosinformaremqualambienteestamos,
comoseguinteparâmetronoweb.xml:
185

## Página 194

14.3.VRaptorEnvironment CasadoCódigo
<context-param>
<param-name>br.com.caelum.vraptor.environment</param-name>
<param-value>development</param-value>
</context-param>
Nessecaso,configuramosoambiente development,ouseja,oambientede
desenvolvimento.Assim,paramudaroambiente,editamosoweb.xml,oumelhor,
sobrescrevemosesseparâmetrodiretamentenoservidordeprodução.Cadaservidor
temumamaneiradesobrescreverumcontext-paramdaaplicação.Porexemplo,no
T o m c a tenoJetty:
http://tomcat.apache.org/tomcat-6.0-doc/config/context.html#Context_
Parameters
http://wiki.eclipse.org/Jetty/Reference/override-web.xml
Com isso podemos criar um arquivo properties no classpath (pasta src
ou src/main/resources em geral) com o nome do ambiente, contendo
todas as configurações deste ambiente. No nosso exemplo, criaríamos o
development.properties,comalgumasconfigurações:
email.suporte = dev@livraria.com
servidor.smtp = localhost:25
url.admin = http://localhost:8080/livraria-admin
E parausara configuração do ambiente,recebemosnoconstrutora classe
Environment,quepossuiométodo getqueacessaumadasconfigurações:
@Component
public class AcervoNoAdmin implements Acervo {
private ClienteHTTP http;
private String urlAdmin;
public AcervoNoAdmin(ClienteHTTP http, Environment env) {
this.http = http;
this.urlAdmin = env.get("url.admin");
}
@Override
public List<Livro> todosOsLivros() {
String xml = http.get(urlAdmin + "/integracao/listaLivros");
186

## Página 195

CasadoCódigo Capítulo14.Apêndice:PluginsparaoVRaptor
//...
}
}
T a m b é mépossívelresgataralgumarquivodeconfiguração queestejanuma
pastacomonomedoambientedentrodoclasspath. Nonossocaso,sequiser-
mosacessaroarquivo admin.cfg.xmldedesenvolvimento,quedeveestarem
src/main/resources/development/admin.cfg.xmlpodemosusar:
URL cfg = env.getResource("admin.cfg.xml");
Estepluginaindaseintegracomoutrospluginscomoo VRaptor S i m p l eMai le
o VRaptor Hibernate,jáquequasesempreprecisamosdeconfigurações específicas
porambienteparaeles.
14.4 VRaptor SimpleMaile VRaptor Freemarker
U m atarefabastantecomumaaplicações W e béenviare-mailsaosseususuários,
sejaparaavisarqueumacontafoicriada,enviardadosdeumacompra,promoções,
notificações etc.Paraqueissosejapossível,precisamosdeumservidorSMTPparao
enviodee-mail,comcredenciaisválidas,umendereçodee-mailparausarmoscomo
origem(campo From).
Oplugin VRaptor S i m p l eMai ltemcomoobjetivofacilitaracriaçãoeoenvio
dee-mailsnaaplicação. Oseucódigofonteeumaótimadocumentaçãoestãoem
https://github.com/caelum/vraptor-simplemailepodeserinstaladousandoadepen-
dência:
<dependency>
<groupId>br.com.caelum.vraptor</groupId>
<artifactId>vraptor-simplemail</artifactId>
<version>1.2.1</version>
</dependency>
Paracompletaraconfiguraçãodopluginprecisamosacrescentaraoarquivode
configuraçãodoambiente(porexemploo development.properties)asseguin-
teschaves:
vraptor.simplemail.main.server = localhost
vraptor.simplemail.main.port = 25
vraptor.simplemail.main.tls = false
187

## Página 196

14.4.VRaptorSimpleMaileVRaptorFreemarker CasadoCódigo
vraptor.simplemail.main.from = no-reply@livraria.com
#se for necessário fazer autenticação:
vraptor.simplemail.main.username = meu-usuario
vraptor.simplemail.main.password = minha-senha
Agora,paraenviarume-mailusamosocomponente MailereusamosaAPI
javax.mailparacriá-lo:
@Resource
public class ComprasController {
private Mailer mailer;
public ComprasController(Mailer mailer) {
this.mailer = mailer;
}
@Post
public void finaliza(Compra compra) {
//...
Email email = new SimpleMail();
email.setSubject("Compra efetuada com sucesso!");
email.addTo(compra.getUsuario().getEmail());
email.setMsg("Seu pedido de Compra no valor de " +
compra.getValor() + " foi finalizado com sucesso!");
mailer.send(email);
}
}
Épossívelaindaenviarume-maildeformaassíncronausandoo AsyncMailer,
assimarequisiçãonãoficaparadaesperandooe-mailserenviado.
Porém,sequisermosenviarume-mailumpoucomaiselaborado,comhtmle
imagens,nãoémuitopráticocriá-lodentrodeumcódigoJava.Poressemotivo,o
SimpleMailseintegracomoplugin VRaptor Freemarker,noqualpodemosusar
templatesdoFreemarkerparacriarocorpodoe-mail.Paraisso,recebemosocom-
ponente TemplateMailer:
@Resource
public class ComprasController {
private Mailer mailer;
188

## Página 197

CasadoCódigo Capítulo14.Apêndice:PluginsparaoVRaptor
private TemplateMailer templates;
public ComprasController(Mailer mailer, TemplateMailer templates) {
this.mailer = mailer;
this.templates = templates;
}
@Post
public void finaliza(Compra compra) {
//...
Email email = this.templates
.template("compraFinalizada.ftl")
.with("compra", compra)
.to(compra.getCliente().getNome(),
compra.getCliente().getEmail());
mailer.send(email);
}
}
Para mais informações sobre o VRaptor Freemarker: https://github.com/
caelum/vraptor-freemarker
14.5 Agendamento de tarefas : VRaptor Ta s k s
QuandoestamosdesenvolvendoaplicaçõesW e b ,amaioriadotrabalhoéfeitodentro
derequisições HTTP.Masalgumasvezesprecisamosexecutartarefasnaaplicação
quenãoserãodisparadasporumusuáriointeragindocomosistemanonavegador,
esimumatarefaqueprecisaserdisparadapelaprópriaaplicação.
Issoacontecequandoprecisamosenviarume-mailparaousuário2horasdepois
dacompraouquandoprecisamosconsumirdadosdeumserviçoacada5minutos,
porexemplo.Paraexecutaressetipodetarefaagendadaouperiódica,temosuma
bibliotecabastantefamosaemJava:oQuartz,comaqualpodemoscriar Tasks,que
podemosagendarparaseremexecutadas.
ParapodermosaproveitartodoopoderdoQuartzjuntocomainjeçãodede-
pendênciasqueoVRaptornosdá,foicriadooplugin VRaptor TaskspeloWilliam
Pivotto,epodeserencontradoemhttps://github.com/wpivotto/vraptor-tasks.Esse
plugintemumaótimadocumentação napáginadogithub,então vouapenasdar
189

## Página 198

14.5.Agendamentodetarefas:VRaptorT a s k s CasadoCódigo
algunsexemplosdoqueépossívelfazercomele.
Para criar tarefas periódicas, que não dependem de componentes
@RequestScope, devemos criar uma Task e anotá-lacom @Scheduled,
configurandoafrequência.
@ApplicationScoped //ou @PrototypeScoped
@Scheduled(cron="0 */5 * * * ?")
public class Sincronizador implements Task {
public Sincronizador(ClienteHTTP http) {...}
public void execute() {
// sincroniza com um serviço qualquer...
}
}
Casoatarefaprecisedecomponentesdeescopoderequisição,criamosumcon-
trollereanotamososmétodosquequeremosagendarcom @Scheduled:
@Resource
public EnviadorDeEmailController {
public EnviadorDeEmailController(
UsuarioRepository usuarios,
Mailer mailer) {
//...
}
@Scheduled(cron="0 0 * * * ?")
public void avisaSobreCadastro() {
List<Usuario> avisaveis = usuarios.queNaoPreencheramCadastro();
// manda email pra todos
}
}
Nessecaso,tododiaàmeia-noiteumatarefaexecutaráumarequisiçãoquecairá
nessemétodo,assimtodososcomponentes @RequestScopedestarãodisponíveis.
Aindaépossívelagendartarefasemtempodeexecução,gerenciaremonitoraras
tarefasjáagendadas.
190

## Página 199

CasadoCódigo Capítulo14.Apêndice:PluginsparaoVRaptor
14.6 Controle de usuários : VRaptor SACI
Na seção 9.3 vimos como criar uma infraestrutura de controle de usuá-
rios no sistema, com um novo modelo Usuario e dois interceptors: o
AutenticacaoInterceptorparaverificarseousuárioestálogadoounão eo
AutorizacaoInterceptorparaverseousuáriotempermissãodeacessarore-
cursodesejado.
Noentanto,essecontroledeusuáriospodeserbastantecomplicado,porexem-
plo,sequisermoscriarpapéis(Roles),oudefinirumahierarquiadeusuários,se-
gundoaqualcadaumtempermissãodeacessarumpedaçodasfuncionalidadesdo
sistema.
Para facilitar esse controle, o Diego Maia (bronx) criou um plugin cha-
mado VRaptor SACI, quepode ser encontradoem: https://github.com/bronx/
SACI-VRaptoretemumaótimadocumentaçãodesuasfuncionalidades.
Parausaresseplugin,precisamosterumaformadeidentificarousuáriologado.
Podemosusarumusuárionobancodedados,comofizemosnaseção9.3,ouusar
algomaiscomplexocomoLDAPouADparaisso.
Tínhamoscriadoaseguinteclasse:
@Component
@SessionScoped
public class UsuarioLogado {
private Usuario usuario;
public void loga(Usuario usuario) {
this.usuario = usuario;
}
public boolean isLogado() {
return this.usuario != null;
}
public Usuario getUsuario() {
return usuario;
}
public void desloga() {
this.usuario = null;
191

## Página 200

14.6.Controledeusuários:VRaptorSACI CasadoCódigo
}
}
ParaadaptaressaclasseaoVRaptorSACI,precisamosqueelaimplementeain-
terface Profile,quedefinetrêsmétodos: isLoggedIn,quedeveretornar true
seousuárioestálogado, getRoles,quedeveretornarospapéisouaspermissões
dousuário,e getAccessLevelquedefineoníveldeacessodousuário,paraper-
missões hierárquicas.
Adaptandoaclasse UsuarioLogadoparaessainterface,vamosrenomearo
métodoisLogadopara isLoggedIneimplementarosoutrosmétodosdeacordo
comonossomodelo:
@Component
@SessionScoped
public class UsuarioLogado implements Profile {
private Usuario usuario;
public void loga(Usuario usuario) {
this.usuario = usuario;
}
public Usuario getUsuario() {
return usuario;
}
public void desloga() {
this.usuario = null;
}
@Override
public boolean isLoggedIn() {
return this.usuario != null;
}
@Override
public List<String> getRoles() {
// Só temos dois tipos de usuário: admin e não admin:
if (usuario.isAdmin()) {
return Arrays.asList("admin");
} else {
192

## Página 201

CasadoCódigo Capítulo14.Apêndice:PluginsparaoVRaptor
return Collections.emptyList();
}
}
@Override
public int getAccessLevel() {
// Não usamos permissões hierárquicas, então vamos retornar 0
return 0;
}
}
Feitoisso,não precisamosmaisdosinterceptorsquehavíamoscriado,poiso
SACIjáfazaautenticação eaautorização. Masparaelefuncionarcorretamente,
precisamosindicarqualéapáginadelogin,paraeleredirecionarcasoousuárionão
estejalogado.Nonossocaso,apáginadeloginestánométodo formulariodo
LoginController,queprecisaseranotadocom @LoginPage:
@Resource
public class LoginController {
//...
@LoginPage
@Get("/login")
public void formulario() {}
}
AgoraoqueprecisamosfazeréindicarparaoSACIquaismétodosprecisam
serautenticados.Existemduasmaneirasdefazerisso.Aprimeiraéquandoapenas
precisamosqueousuárioestejalogadoparaacessarocontroller.Paraisso,usamosa
anotação @LoggedInnummétododocontrollerounaprópriaclassedocontroller,
sequisermosquetodososmétodossejamautenticados.
Asegundamaneiraédefinindoocontroledeacessoaométodoouaocontroller,
usandoumaoumaisroles(comaanotação @Role)ouoníveldeacesso(coma
anotação @AccessLevel).Nonossocaso,queremosqueo LivrosController
sejaautenticadototalmente,masapenasalgunsmétodosprecisamseracessadossó
peloadmin,entãoaconfiguraçãoseria:
@LoggedIn
@Resource
193

## Página 202

14.7.Criandooseupróprioplugin CasadoCódigo
public class LivrosController {
@Get("/livros/formulario")
public void formulario() { ... }
@Get("/livros")
public List<Livro> lista() { ... }
@Role("admin")
@Post("/livros")
public void salva(Livro livro) { ... }
//...
}
14.7 Criando o s e upróprio plugin
Muitasvezesdesenvolvemosumasoluçãolegalqueprecisaserreutilizadaentredi-
versosprojetosdasuaempresa,ousimplesmentequeremoscompartilharessasolu-
çãocomoutrosdesenvolvedores.ParaqueoVRaptorconsidereessasoluçãocomo
umplugin,precisamosagrupartodososseuscomponentesemumprojetoseparado,
paragerarmosumjar.
ParaqueessejarsejaregistradoautomaticamentenoVRaptor,eleprecisater
dentrodeleoarquivo META-INF/br.com.caelum.vraptor.packagescomo
pacotebasedoplugindentrodessearquivo.V a m o ssuporquequeremostransformar
onossoserviçodearquivosquedesenvolvemosnaseção8emumplugin.
Esse serviço écomposto de duas classes básicas,o Diretorio e o
Arquivo, e uma implementação que salva os arquivos no banco de da-
dos, o DiretorioNoBD. Então vamos extraí-las para um projeto à parte,
usando um pacote mais genérico. Esse pacote precisa ser colocado den-
tro do arquivo META-INF/br.com.caelum.vraptor.packages dentro de
src/main/resources.
vraptor-arquivos/
- src/main/java
- br.com.casadocodigo.arquivos
- Arquivo.java
- Diretorio.java
- DiretorioNoBD.java
194

## Página 203

CasadoCódigo Capítulo14.Apêndice:PluginsparaoVRaptor
- src/main/resources
- META-INF
- br.com.caelum.vraptor.packages
Edentrodoarquivochamado br.com.caelum.vraptor.packagescoloca-
mos:
br.com.casadocodigo.arquivos
Agorabastagerarumjarcomtodosessesarquivosetemosumplugin! Se
colocarmoso vraptor-arquivos.jaremqualquerprojetocomoVRaptor,o
DiretorioNoBDjáseráregistradocomocomponenteepoderemosreceberum
Diretorionoconstrutordequalquerclassedaaplicação.
Seoobjetivoforcompartilharesseplugin:
•crieumprojetonogithub,porexemploemhttps://github.com/seu-usuario/
seu-plugin;
•subaosarquivosdoprojetoparaláusandocomandosdegitemlinhadeco-
mandoopróprioprogramadogithub;
•escrevaumarquivoREADME.mdexplicandocomousaroseuplugin;
•Entreemhttps://github.com/caelum/vraptor-contribesigaasinstruções para
incluirseupluginnalista;
•Divulgue o seu plugin na lista de emails do VRaptor caelum-
vraptor@googlegroups.com;
•Sejareconhecidoportodos=)
195

## Página 205

Capítulo15
Apêndice:Funcionamentointerno
doVRaptor
OVRaptorrodainteiramentedentrodocontainerdeinjeçãodedependências.Isso
significaquetodocomponentedoVRaptoréumaclassegerenciadaepodesersubs-
tituidapelaaplicação,casoelaimplementeumcomponentecomamesmainterface.
NestecapítuloveremoscomofuncionaoVRaptor,desdeainicializaçãodoser-
vidoratéotratamentoderequisições, mostrandooscomponentesresponsáveispor
algumasdasfuncionalidadesecomopoderíamossobrescrevertaiscomponentes.
15.1 Inicialização d oServidor
OpontodeentradadoVRaptoréofiltrocomomesmonome,queregistramosno
web.xml(ouéregistradoautomaticamentesevocêusaServlet3):
<filter>
<filter-name>vraptor</filter-name>

## Página 206

15.1.InicializaçãodoServidor CasadoCódigo
<filter-class>br.com.caelum.vraptor.VRaptor</filter-class>
</filter>
T o d oocódigodainicializaçãodoVRaptoréiniciadopelométodo initdofil-
tro.Comotudorodadentrodeumcontainerdeinjeçãodedependências,aprimeira
coisafeitaéadecisãodequalvaiseroproviderusado:
BasicConfiguration config = new BasicConfiguration(servletContext);
init(config.getProvider());
Para essa escolha, a preferênciaépelo parâmetro do web.xml chamado
br.com.caelum.vraptor.provider,quedeveapontarparaaclassequeimple-
mentatodaalógicadeinjeçãodedependências.Ousomaiscomumdesseparâmetro
équandoqueremospersonalizarumpequenopedaço,comono GuiceProvider,
parainstalarmosummódulo:
package br.com.minhaapp.infra;
public class CustomProvider extends GuiceProvider {
@Override
protected Module customModule() {
return new Module {
public void configure(Binder binder) {
// para manter o comportamento padrão do VRaptor
binder.install(super.customModule());
binder.install(new OutroModulo());
//...
}
};
}
}
ParaqueoVRaptoruseessaconfiguração,precisamosregistrarnoweb.xml:
<context-param>
<param-name>br.com.caelum.vraptor.provider</param-name>
<param-value>br.com.minhaapp.infra.CustomProvider</param-value>
</context-param>
198

## Página 207

CasadoCódigo Capítulo15.Apêndice:FuncionamentointernodoVRaptor
Casoesseparâmetronãoexista,procuramosporclassesdosprovidersnoclass-
path,quesódeveriamexistirseojardoproviderestivernoprojeto.Poressemotivo,
nãoénecessárianenhumaconfiguraçãoadicionalparausarumproviderespecífico,
somenteojarnoclasspathbasta.Noentanto,existeumaordemparatestarosprovi-
ders:Spring,GuiceePico.Seoprojetotivermaisdeumdosprovidersnoclasspath,
essaordemfaráodesempate.
Opróximopassoéainicializaçãodoprovider,queenvolveoregistrodetodos
oscomponentesdoVRaptore,emseguida,detodososcomponentesdaaplicação.
OregistrodoscomponentesdoVRaptoréfeitousandoaclasse BaseComponents,
quecontémummapagigantequeligamasinterfacesdoscomponentesdoVRaptor
àssuasimplementações padrão,noescopocorreto:
public class BaseComponents {
private final static Map<Class<?>, Class<?>> APPLICATION_COMPONENTS =
classMap(
EncodingHandlerFactory.class, EncodingHandlerFactory.class,
AcceptHeaderToFormat.class, DefaultAcceptHeaderToFormat.class,
//...
);
private static final Map<Class<?>, Class<?>> REQUEST_COMPONENTS =
classMap(
MethodInfo.class, DefaultMethodInfo.class,
LogicResult.class, DefaultLogicResult.class,
PageResult.class, DefaultPageResult.class,
//...
);
//...
}
Jáoregistrodoscomponentesdaaplicaçãoéfeitoapartirdeumscandetodas
asclassesqueestãoem WEB-INF/classesecontémanotações doVRaptor,como
@Component, @Resourcee @Intercepts.Oscannãoéfeitoemtodasasclasses
doclasspathporqueissoébastanteineficiente,jáqueteríamosquepassarportodas
asclassesdetodososjarsqueestãonoclasspatheque,namaiorpartedoscasos,não
têmnadaavercomoVRaptor.
Alémdisso,oVRaptorpassaportodasasclassesqueestão abaixodospaco-
tesregistradosnoparâmetro br.com.caelum.vraptor.packagesdoweb.xml.
199

## Página 208

15.1.InicializaçãodoServidor CasadoCódigo
Nessecasoaprocuraéportodooclasspath,enãosomenteem WEB-INF/classes.
Sealgumalgumcomponenteaserregistradoestiverdentrodeumjar,elesóserá
escaneadoseoseupacotebaseestivernesseparâmetrodepackages. Outrama-
neiraderegistrarumcomponentequeestádentrodeumjarécolocarumarquivo
META-INF/br.com.caelum.vraptor.packagescontendoopacotebasedas
classesdessejar,comoéfeitonospluginsdoVRaptor.
Esse scan éfeito, por padrão, dinamicamentena inicialização do servidor,
usando a biblioteca Scannotation. No entanto, em algumas versões do JBoss
queusamumsistemadearquivosvirtualparagerenciarasaplicações deploya-
das,essescannão funcionacorretamente. Nessecasotemosqueusaroscanes-
tático,quegeraumaclassequecontémocódigo deregistrodetodososcom-
ponentesdaaplicação. Estaclasseégeradainvocandoométodomaindaclasse
VRaptorStaticScanning. Issodeveserfeitoduranteoprocessodebuildda
aplicação,poiségeradoum .classnapasta WEB-INF/classesqueélidopelo
VRaptornainicializaçãodoservidor.
ExemplodecomofazerissousandooAnt,nobuild.xml:
<path id="build.classpath">
<fileset dir="${webapp.dir}/WEB-INF/lib" includes="*.jar" />
</path>
<target name="vraptor-scanning" depends="compile">
<java classpathref="build.classpath"
classname="br.com.caelum.vraptor.scan.VRaptorStaticScanning"
fork="true">
<arg value="${webapp.dir}/WEB-INF/web.xml" />
<classpath refid="build.classpath" />
<classpath path="${webapp.dir}/WEB-INF/classes" />
</java>
</target>
ExemplodecomofazerissousandooMaven,nopom.xml:
<plugin>
<groupId>org.codehaus.mojo</groupId>
<artifactId>exec-maven-plugin</artifactId>
<version>1.2.1</version>
<configuration>
<mainClass>
br.com.caelum.vraptor.scan.VRaptorStaticScanning
</mainClass>
200

## Página 209

CasadoCódigo Capítulo15.Apêndice:FuncionamentointernodoVRaptor
<arguments>
<argument>${basedir}/src/main/webapp/WEB-INF/web.xml</argument>
</arguments>
</configuration>
<executions>
<execution>
<phase>process-classes</phase>
<goals>
<goal>java</goal>
</goals>
</execution>
</executions>
</plugin>
Ocódigodeinicializaçãodosproviders,apósdecidirquaissãoasclassesquede-
vemserregistradas,éumadaspartesmaiscomplicadasdofuncionamentointerno
doVRaptor,poisprecisamosnormalizarocomportamentodosprovidersparausar
asconvenções doVRaptor(comoescopoderequestporpadrãoeinjeçãopelocons-
trutor).Alémdissoénecessárioimplementarouconfigurarosescoposcorretamen-
tesepermitirqueclassesdaaplicação(oudeplugins)sobrescrevamcomponentes
internosdoVRaptor.
Porserbastantecomplexo,voufalaraquidascaracterísticasprincipaisdecada
umdoscontainers:
•PicoProvider:écriadoumcontainer( MutablePicoContainer)paracon-
trolaroescopodeaplicaçãoetodososoutrosescopossãocriadoscomocon-
tainersfilhos.Ainicializaçãoefinalizaçãodecadaescopoéfeitapelopróprio
VRaptor. Ocontroledeimplementações doscomponenteséfeitoporma-
pasdeinterfaceparaimplementação,duranteoregistrodoscomponentes.Os
componentesdoVRaptorsãoregistradosprimeiro,assimumcomponenteda
aplicaçãosobrescreveaentradadomapa.A p ó safasedoregistro,osescopos
sãocriadosapartirdessesmapas.
•SpringProvider: o VRaptor procura um ApplicationContext do
Spring que jáesteja registrado, assim consegue aproveitarconfigurações
doSpringquetenhamsidoregistradasnum ContextLoaderListener,
por exemplo. Se não encontrar, o VRaptor procura por um arquivo
applicationContext.xmlnoclasspathparaaconfiguração inicial. Se
tambémnãoforencontrado,oVRaptorcriaum ApplicationContextem
201

## Página 210

15.2.Definindoospapéisdoscomponentes:estereótipos CasadoCódigo
branco.ApartirdaíoVRaptorusaaAPIprogramáticadoSpringpararegis-
traroscomponentes,usandoosescoposdopróprioSpring.Parapermitira
sobrescrita,todososcomponentesdoVRaptorsãoregistradoscomoinfraes-
truturaetodososcomponentesdaaplicaçãosãoregistradoscomoprimários.
Assim,sehouvermaisdeumcomponenteimplementandoumainterface,o
daaplicaçãotempreferência.
•GuiceProvider:écriadoum Modulechamado VRaptorAbstractModule,
queregistratodososcomponentesdoVRaptoredefinetodososescopos,
quesão implementadospelopróprioVRaptor.Então écriadoumsegundo
Modulequeregistratodososcomponentesdaaplicaçãoesobrescreveopri-
meiro. Assim,seexistiremduasimplementações damesmainterface,ada
aplicaçãosobrescreveadoVRaptor.
15.2 Definindoos papéisd o scomponentes : estereó -
tipos
A p ó soregistrodetodososcomponentesnoprovideraconteceadefiniçãodosseus
papéis:quaisserãooscontrollers,quaisserãointerceptors,quaisserãocomponentes
comuns.Essadefiniçãoéfeitapelaanotaçãoqueregistraaclasse:oestereótipo.Os
estereótiposexistentesnoVRaptorsão:
•@Resource:definequeaclasseseráumcontrolleretratarárequisições.
•@Intercepts:defineum Interceptor,compossibilidadedeconfigura-
çãodaordemrelativaentreinterceptors.
•@Component:umcomponentecomumdosistema.
•@Convert:defineum Converter,queconverteparâmetrosderequisição
emobjetos.
•@Deserializes: define um Deserializer que, dado um
Content-Type,devetransformarocorpodarequisiçãoemobjetos.
Ocomportamentodecadaumdessesestereótiposédefinidoporcomponentes
queimplementam StereotypeHandler,quetratamcadaumadasclassesdurante
ainicializaçãodoservidor.Sequisermos,épossívelcriarnovosestereótiposnaapli-
cação,comseusrespectivoshandlers,ouatécriarumhandlerparaumestereótipo
202

## Página 211

CasadoCódigo Capítulo15.Apêndice:FuncionamentointernodoVRaptor
padrãodoVRaptor.Sequisermos,porexemplo,criarumalistadetodososcontrol-
lersdosistema,podemoscriarumhandlerparaoestereótipo @Resource:
@Component
@ApplicationScoped
public class ListaDeControllers implements StereotypeHandler {
private List<Class<?>> controllers = new ArrayList<>();
public Class<? extends Annotation> stereotype() {
return Resource.class;
}
public void handle(Class<?> type) {
controllers.add(type);
}
}
Paracriarumestereótiponovo,bastaanotaraanotação doestereótipocom
@StereotypedoVRaptor,ecriarohandlerrespectivo. T o d a sasanotações com
@Stereotyperegistramcomponentesparainjeção dedependênciasautomatica-
mente.
Comoesses StereotypeHandlersdefinemcomportamentosimportantesda
aplicação,elesenvolvemoutroscomponentes,quepodemsersobrescritospelaapli-
cação,senecessáriofor.Parasabermosoqueépossívelfazercomcadaestereótipo,
vamosvercadaumemdetalhes.
@Component
Esseestereótipoapenasregistraocomponenteparaainjeçãodedependências,
nãopossuicomportamentosadicionais.
@Convert
Ocomportamentoédadopelo ConverterHandler,quevalidaseaclasseano-
tadaémesmoum Converterearegistranocomponente Converters,queéo
catálogodetodososconvertersdosistema.
O componente Converters é implementado pela classe
DefaultConverters etempormétodoprincipalo to. Se quisermosuma
instânciadoconverterde Date,fazemos:
Converter<Date> converter = converters.to(Date.class);
203

## Página 212

15.2.Definindoospapéisdoscomponentes:estereótipos CasadoCódigo
Aordemdebuscadosconvertersdápreferênciaparaconvertersregistradospela
aplicação,mascasohajaalgumproblemadeprioridade,podemossobrescreveresse
componentepararesolverambiguidades:
@Component @ApplicationScoped
public class CustomConverters extends DefaultConverters {
//delega o construtor
@Override
public <T> Converter<T> to(Class<T> clazz) {
if (clazz.equals(Date.class))
return container.instanceFor(MeuDateConverterMaroto.class);
return super.to(clazz);
}
}
@Deserializes
Esseestereótiporecebealistadecontenttypesqueaclasseécapazdedeserializar:
@Deserializes({"application/json", "text/javascript"})
public class JsonDeserialization implements Deserializer { ... }
Oseu StereotypeHandleréo DeserializesHandler,quefuncionade
formabastantesimilarao ConverterHandler:recebeum Deserializersno
construtor,emontaocatálogodedeserializers,quemapeiacontenttypesaclasses
queosdesserializam.
OVRaptorjápossuiimplementações quedeserializamJSONeXML,supor-
tando tambémvendortypes, comopor exemplo application/atom+xml e
application/vnd.myapp+json.ParaformatosdiferentesdeXMLeJSONpo-
demosimplementarumdeserializerpróprioeanotá-locom @Deserializes,pas-
sandoocontent-typesuportado.
@Intercepts
O @Interceptsétratadopelo InterceptorStereotypeHandler,que
registrao Interceptorencontradono InterceptorRegistry.Essecompo-
nenteorganizaosinterceptorsemumaordemquerespeitaasrestriçõesquepodemos
passaraodeclararo Interceptor:
204

## Página 213

CasadoCódigo Capítulo15.Apêndice:FuncionamentointernodoVRaptor
@Intercepts(before=X.class, after={M.class, N.class})
public class A implements Interceptor { ... }
Nessecaso,elegaranteumaordememqueo Arodedepoisdo Medo N,mas
antesdo X.Ordenspossíveisseriam M => N => A => Xe N => M => A =>
X.OsinterceptorstambémsãoordenadosemrelaçãoaosinterceptorsdoVRaptor
e,senadafordito,ointerceptordaaplicaçãoexecutadepoisdeencontrarométodo
docontrollerqueseráexecutadonarequisiçãoeantesdeexecutarométododocon-
troller.
A implementação padrão desse registro de interceptors é o
TopologicalSortedInterceptorRegistry, que ordena os interceptors
usandoaordemtopológicadefinidapelo beforeeo after.Seporacasohouver
umciclodedependênciaentreosinterceptors,essaimplementação identificana
inicializaçãoegeraumerro.
@Resource
Éoestereótipoprincipal,jáquedefineosControllersdaaplicação,eétratado
pelo ResourceHandler,queinteragecomdoiscomponentes:o RoutesParser,
queextrairotasapartirdeumcontrollereo Router,queguardatodasasrotasdo
sistemaepossibitatantoageraçãodeumaURLdadoummétododocontrollerou
abuscadeummétododocontrollerapartirdeumaURLeummétodoHTTP.
A implementação padrão do RoutesParser é a
PathAnnotationRoutesParser, que define as rotas usando as anotações
quecolocamosnocontroller,como @Path, @Gete @Post.Essaimplementação
éaquedefineaconvençãodeURL /nomeDoController/nomeDoMetodo.Essa
etodasasclassesdoVRaptorquedefinemconvenções foramfeitasparaserem
facilmentesobrescritas.
Ébastantedifícilimplementarum RoutesParserdozero,masébastantefácil
mudaraformacomqueaimplementaçãopadrão funciona,poiselapossuivários
métodos protectedquesãousadosduranteoalgoritmodecriaçãoderotas.U m
exemplodemudançaésequisermosmudaraconvençãoparacolocar /adminantes
doscontrollersqueestãonopacoteterminadoem .admin:
@Component @ApplicationScoped
public class AdminRoutesParser extends PathAnnotatedRoutesParser {
// delega o construtor
205

## Página 214

15.2.Definindoospapéisdoscomponentes:estereótipos CasadoCódigo
@Override
protected String extractControllerNameFrom(Class<?> type) {
String controllerName = super.extractControllerNameFrom(type);
if (type.getPackage().getName().endsWith(".admin")) {
return "admin/" + controllerName;
}
return controllerName;
}
}
Como criamos um componente na aplicação que implementa o
RoutesParser,elasobrescreveráaimplementação doVRaptor. Dessemodo,a
convenção padrão passa a ser /admin/nomeDoController/nomeDoMetodo
se o pacote terminar com .admin. Podemos sobrescrever outros métodos
protecteddessaclasse,comoporexemplo:
•String defaultUriFor(String controllerName, String
methodName): dadoonomedocontrollerjátratadoeonomedomé-
todo,retornaraURLpadrão.
•protected boolean isEligible(Method javaMethod): decide se
vaisergeradaounãoumarotaparaométodo.Porpadrãoretornatruepara
métodospúblicosquenãosãoestáticosenemsãoosmétodosde Object.
•protected String[] getURIsFor(Method javaMethod,
Class<?> type): dado o métodoe a classe do controller, retorna a
lista de URIsque devem chegarnesse método. Podemos, por exemplo,
chamaressemétodono superemodificarasURIsdealgumaforma.
•protected EnumSet<HttpMethod> getHttpMethods(AnnotatedElement
annotated):dadauma Class<?>ouum Method,retornarosmétodos
HTTPsuportados.Essemétodosóé protectedapartirdoVRaptor3.5.2.
•protected List<Route> registerRulesFor(Class<?>
baseType): dada a classe do controller, retorna todas as rotas possí-
veis. U mRouterepresentatodaaconfiguração deumarota,comoURI,
métodohttpeparâmetrosrecebidosnaURI.Podemosconstruirumarota
usandoobuilderdisponívelapartirdo Router:
206

## Página 215

CasadoCódigo Capítulo15.Apêndice:FuncionamentointernodoVRaptor
Route route = router
.builderFor("/minha-rota")
.with(EnumSet.of(HttpMethod.GET))
.withPriority(Path.DEFAULT)
.is(classDoController, method)
.build()
Existemmuitaspossibilidadesdemudança,casotenhaalgumadúvidaouidéia
queestejadifícildeadaptarusandoessesmétodos,mandeumamensagemnalista
dedesenvolvimentodoVRaptor:caelum-vraptor-dev@googlegroups.com.
15.3 Tratamento de Requisições
Comtodososestereótipostratados,oVRaptorterminasuainicializaçãoeoservidor
estáprontoparatratarrequisições. Cadarequisiçãotemcomopontodeentradao
filtrodoVRaptor(aclasse VRaptor).
Oprimeirocomponenteaserusadoéo StaticContentHandler,usadopara
decidirsearequisiçãoéparaumarquivoestáticoe,então,nãotratararequisição.A
implementaçãopadrãoverificaapenasseaURIrepresentaumarquivoqueestána
aplicação,comoumjavascriptouumcss,maspodemosusaressecomponentepara
ignoraroutrasURLs,jáqueadeclaraçãodeumfiltronãopossuimeiosdeexcluir
URLs.
SefordecididoqueessarequisiçãovaisertratadapeloVRaptor,oproviderde
injeção dedependênciaséacionadoe,então, inicializaoescopodestarequisição.
Paraexecutardefatoarequisição, éusadoocomponente RequestExecution.
Essecomponentepoderiafazerqualquercoisa,dentrodoambientedeinjeção de
dependênciasdoVRaptor,masaimplementaçãopadrãosimplesmentepegatodos
os Interceptorsregistradosnosistemaeosadicionano InterceptorStack,
naordemdefinidapelo beforee afterdecada Interceptor.
Essa InterceptorStackcontrolatodaapilhadeexecuçãodosinterceptors
eéexatamenteoobjetoquerecebemosdentrodométodo interceptsdeum
Interceptorparachamarmoso stack.next(method, instance). Osin-
terceptorssósãoexecutadoscasoométodo acceptsretorne true.
Apartírdaí,todotrabalhoéfeitoporinterceptors,quecontrolamospassosda
requisiçãoealgumasdasfuncionalidadesopcionaisdoVRaptor,comodownloade
upload.Veremosopapeldecada InterceptordoVRaptoraseguir.
207

## Página 216

15.4.CatálogodeInterceptors CasadoCódigo
15.4 Catálogo de Interceptors
V a m o sveraseguirtodososinterceptorspadrão, numadasordenspossíveisde
execução dessesinterceptors. Comoaordemétopológica, ouseja, apenasres-
peitaasrestrições de beforee after,não fixandoaordemdeinterceptorsin-
dependentesentresi. Osinterceptorsdaaplicação emgeralsão inseridosentreo
ResourceLookupInterceptoreo ExecuteMethodInterceptor,maspode-
mosmudarsuaordemparaqualquerlugar,desdequenãosecrieumciclodede-
pendências.
ResourceLookupInterceptor
Esseéointerceptorqueprocuraométododecontrollerqueseráexecutadonessa
requisição.Paraissoeleusaocomponente UrlToResourceTranslator,queex-
traiinformações darequisiçãoeprocurao ResourceMethodno Router,usando
ométodo parse.EssemétodoprocuraporrotasquetratamaURIdarequisiçãoe,
dentreelas,asquetratamométodoHTTPdarequisição.
Nesseprocesso,várioserrospodemacontecer:
•NenhumarotatrataaURI: ResourceNotFoundException
•ExistealgumarotaquetrataaURI,masnão nométodoHTTPpassado:
MethodNotAllowedExceptioncomalistademétodosHTTPpossíveisna
URI.
•ExistemaisdeumarotatrataamesmaURIemétodoHTTP,namesmaprio-
ridade: IllegalStateException,dizendoquaissãoasrotasconflitantes.
Esseerroédaaplicação,epodeserajustadocomoatributo priorityda
anotação @Path:
@Path(value = "/{rotaMuitoGenerica}", priority=Path.LOWEST)
Setudodercerto,o ResourceMethodéguardadodentrodocomponente
MethodInfo,paraserusadoemtodososoutrospontosdosistema,earequisição
continuanormalmente.
Em caso de erros, existem dois componentes que os tratam: o
ResourceNotFoundHandler e o MethodNotAllowedHandler, que por
padrão retornamosHTTP status404 e405,respectivamente,epodemserso-
brescritospor componentesda aplicação, caso não seja esse o comportamento
desejado.
208

## Página 217

CasadoCódigo Capítulo15.Apêndice:FuncionamentointernodoVRaptor
ExceptionHandlerInterceptor
Éointerceptorqueimplementaafuncionalidadedetratamentodeexceções do
VRaptor.Podemoscolocarnocomeçodeummétododocontroller:
result.on(MinhaException.class)
.redirectTo(MeuController.class)
.metodo();
Assimse,duranteorestodarequisiçãoa MinhaExceptionforlançada,are-
quisiçãoseráredirecionadaparao MeuController.metodo().
InstantiateInterceptor
Éointerceptorqueinstanciaocontrollereodeixadisponívelnosegundopa-
râmetrodo stack.nextounoúltimoparâmetrodométodo intercepts.Esse
interceptornãofaznadaseainstânciadocontrollerjáestiverpreenchida.
Portanto,sequisermosinstanciarocontrollerdealgumaoutraforma,deve-
moscriaruminterceptor before=InstantiateInterceptor.classepas-
sar a instancia criada para o método stack.next, ou se quisermos usar
a instancia do controller para alguma coisa, devemos criar um interceptor
after=InstantiateInterceptor.classeusaro Objectquerecebemosno
últimoparâmetrodométodo intercepts.
FlashInterceptor
Implementaoescopoimplícitochamadode Flash.Esseéoescopoemquecolo-
camosumobjetoqueserádisponibilizadonapróximarequisição,apósumredirect,
porexemplo.Existemduasmaneirasdeusaresseescopo.Aprimeiraéseincluirmos
objetosno Resultantesdeumredirect:
result.include("umObjeto", objeto);
result.redirectTo(this).outroMetodo();
Todososobjetosincluidos,nessecaso,serãocolocadosna HttpSessionecon-
sumidosnapróximarequisição,paraseremreincluidosno Result.Outramaneira
deusaresseescopoépassandoargumentosparaométodoredirecionado:
result.redirectTo(this).outroMetodo(umParametro, outroParametro);
209

## Página 218

15.4.CatálogodeInterceptors CasadoCódigo
Esses parâmetros são usados para preencher a URI de redireciona-
mento e serão passados para o outroMetodo na próxima requisição. Ou
seja, ao invésde usar os parâmetros da requisição para criar os parâmetros
do outroMetodo, serão usados exatamente os objetos umParametro e
outroParametro.Essasegundamaneiraéimplementadapelo LogicResulte
pelo ParametersInstantiatorInterceptor.
MultipartInterceptor
Esseinterceptoréoresponsávelpelouploaddearquivosepossuiduasimple-
mentações: o CommonsUploadMultipartInterceptor,baseadonabiblioteca
commons-fileuploadeo Servlet3MultipartInterceptor,queusaaimple-
mentaçãodeuploaddeservidorescompatíveiscomServlet3.Aimplementaçãoé
selecionadadeacordocomoclasspathdaaplicação.
Se existir o jar do commons-fileupload, a implementação
CommonsUploadMultipartInterceptor é usada. Senão, o VRap-
tor verifica a versão de Servlet usada e, caso seja a 3, a implementação
Servlet3MultipartInterceptor éusada. Em últimocaso, éusada uma
terceiraimplementaçãochamada NullMultipartInterceptorquenuncaserá
usada( acceptssempreretorna false)eéimpressoumlogfalandoquenão
existenenhumabibliotecadeuploaddisponível.
Asduasimplementações funcionaisdo MultipartInterceptorrecebemo
componente MultipartConfig,quedefineduasconfigurações: otamanhomá-
ximodeuploads,queporpadrão é2MBeumapastatemporária,ondeosuplo-
adspoderão sersalvos. Podemossobrescreveressasconfigurações criandoum
@Componentqueimplementa MultipartConfignaaplicação.
ParametersInstantiatorInterceptor
É oresponsávelporinstanciarosparâmetrosdosmétodosdocontroller,de
acordocomosparâmetrosquevieramnarequisição. Paraissoelecoordenavários
tiposdeinstanciaçãodeparâmetros.Ospassosexecutadosnesseinterceptorsão:
•Normalizaçãodeparâmetros:semandarmosparâmetrosquecontém“[]”,o
VRaptoradicionaíndicesnessesparâmetros.Dessaforma,semandarmos:
objeto.lista[].atributo=a
objeto.lista[].atributo=b
objeto.lista[].atributo=c
210

## Página 219

CasadoCódigo Capítulo15.Apêndice:FuncionamentointernodoVRaptor
Osparâmetrosserãonormalizadospara:
objeto.lista[0].atributo=a
objeto.lista[1].atributo=b
objeto.lista[2].atributo=c
•ProcuraporparâmetrosquedevemvirdoHeaderHTTPusandoaanotação
@HeaderParam,comoem:
@Get("/uri")
public void metodo(@HeaderParam("User-Agent") String agent) {
// ...
}
Esseparâmetroéadicionadocomoumatributodarequisição.
•U s odoflash: seexistiremparâmetrossalvosnoflash,elesserão usadosda
maneiraquevieram.
•Parsingdosparâmetrosdarequisição: Senãoexistiremparâmetrosdoflash,
elesserãoinstanciadospelocomponente ParametersProvider.Seocor-
reremerrosdeconversãonessepasso,elesserãoadicionadosao Validator,
obrigandoométododocontrolleratrataresseserros.
•Disponibilização dosparâmetros: aofinal,osparâmetrossão incluídosno
MethodInfo,paraseremusadosnospróximoscomponentes.
Ocomponente ParametersProvideréoresponsávelporpegartodosospa-
râmetrosdarequisiçãoeinstanciarosparâmetrosdométododocontrollerqueserá
executadonarequisição. EssainstanciaçãoéfeitausandoaconvençãodoVRaptor
parapreenchê-los:
parametro=valor
objeto.atributo=valor
objeto.filho.atributo=valor
lista[0]=valor
lista[0].atributo=valor
Essa instanciação éfeitachamandoo construtorsem argumentose, então,
usandoosgettersesettersrespectivos. ParatransformaraStringparaosobjetos
decadaatributosão usadosos Convertersqueforamregistrados. OVRaptor
211

## Página 220

15.4.CatálogodeInterceptors CasadoCódigo
aindasuportasetaratributosapósaconversão,entãopodemospassarparâmetros
parecidoscom:
pessoa=PessoaFisica
pessoa.cpf=111111111111
pessoa.nome=Joao
Setivermosumconverterpara Pessoa,queinstanciauma PessoaFisicaou
uma PessoaJuridicadeacordocomoparâmetroqueveio,ocpfeonomeserão
populadosapósessaconversão.
Caso queira modificar os parâmetros de alguma ma-
neira, ou simplesmente usá-los, crie um interceptor que roda
after=ParametersInstantiatorInterceptor.class, receba
MethodInfonoconstrutoreuseométodo info.getParameters().
Existemduasimplementações de ParametersProvider,umausandoabi-
blioteca OGNL( OgnlParametersProvider)eoutrausandoabiblioteca IOGI(
IogiParametersProvider).Aimplementaçãocom OGNLfoiaprimeiracriadae
eraapadrãoatéaversão3.4doVRaptor.Aimplementaçãoqueusao IOGIsuporta,
alémdocomportamentopadrão,ousodeconstrutorparapopularosatributosein-
jeçãodedependênciasnoconstrutordasclassesquesãoparâmetrosdemétodosde
controller.
Ambasasimplementações podemserpersonalizadas,sobrescrevendocompo-
nentes.NocasodoOGNLusandoopróprio OgnlParametersProvidereseus
métodosprotectedeocomponente OgnlFacadeenocasodoIOGIsobrescrevendo
o VRaptorInstantiator.Comoesseprocessodeinstanciaçãoébastantecom-
plexo,nãovoutentarexplicá-loaqui,masocódigodessasclassesérazoavelmente
legível,principalmenteseusarmosostestesdeunidadesparaentenderoscompor-
tamentospossíveis.
Sefornecessário,usealistadedesenvolvimentodoVRaptorcaelum-vraptor-
dev@googlegroups.comparapostardúvidaseterumadireçãosobrequaléamelhor
maneiradefazersobrescritas.
DeserializingInterceptor
É ointerceptorqueinstanciaosparâmetroscasoométododocontrollerfor
anotadocom @Consumes,passandoumalistadecontent-types. Paraencontrar
o Deserializerapropriado,usaocomponente Deserializerse,casonão
exista,retornaostatus415-UnsupportedMediaT y p e .
212

## Página 221

CasadoCódigo Capítulo15.Apêndice:FuncionamentointernodoVRaptor
MethodV alidatorInterceptor
ValidaosparâmetrosdométodousandoBeanValidations,porexemplo:
@Post("/uri")
public void metodo(@NotNull String parametro) {...}
ExecuteMethodInterceptor
Esseinterceptorusaosartefatosproduzidospelosoutrosinterceptorsparaexe-
cutardefatoométododocontroller.A p ó saexecução,oretornodométodoéin-
cluídono MethodInfoparaserusadonospróximosinterceptors.
Outra característicaimportanteéque, quandofazemosvalidações nosmé-
todos do controller e chamamos os métodosde redirecionamento do valida-
tor,como validator.onErrorRedirectTo(this).formulario(), élan-
çada uma ValidationException para evitar que o resto do métodoseja
executado, em caso de erros. Poresse motivo, esse interceptorgaranteque a
ValidationExceptiontenhasidolançadaemcasodeerrose,senãofor,lança
umaexceptiondizendo:
There are validation errors and you forgot to specify where to go.
Please add in your method something like:"
validator.onErrorUse(page()).of(AnyController.class).anyMethod();
or any view that you like.
If you didn't add any validation error, it is possible that a
conversion error had happened.
Nagrandemaioriadoscasos,esseerroaconteceporcausadeerrosdeconver-
sãoquenãoforamtratados,portantosempreverifiqueosparâmetrospassadosna
requisiçãocasoaconteçaesseerro.
DownloadInterceptor
Éointerceptorqueescreveosdadosparadownloadnarespostademétodosdo
controllerqueretornam Downloadoualgumobjetoquerepresentadados,como
File, InputStreamou byte[].
OutjectResult
Incluino Resultoretornodométododocontroller,usandoumnomedado
pelocomponente TypeNameExtractor, quetransformanomesdeclassesem
213

## Página 222

15.4.CatálogodeInterceptors CasadoCódigo
nomedeobjetos.AconvençãodoVRaptorparaissoéonomedaclassecomapri-
meiraminúscula,paratipossimples,eonomedaclasseseguidode List.
@Get("/uri")
public Livro metodo() { ... }
// equivalente a result.include("livro", retornoDoMetodo);
@Get("/uri")
public List<Livro> metodo() { ... }
// equivalente a result.include("livroList", retornoDoMetodo);
Essaconvenção podesermudadasobrescrevendoo TypeNameExtractor.
Cuidado,poisessecomponenteéusadotambémemoutroslugares.
ForwardT oDefaultViewInterceptor
Éoúltimointerceptordapilha. Seuobjetivoéredirecionarparaajsppadrão
casoo Resultnãotenhasidousadoparaalteraroresultado.Esseinterceptornão
chama stack.next,entãonãoadiantacriarinterceptorsquerodemdepoisdele.
Paramudaraconvenção docaminhodaJSPpadrão, podemossobrescrevero
componente PathResolver.Asuaimplementaçãopadrãotambémfoifeitapara
sersobrescritafacilmente,semterqueimplementartodooalgoritmo.Porexemplo,
sequisermostrocardejspparavelocity,podemoscriarocomponente:
@Component
public class VelocityPathResolver extends DefaultPathResolver {
//delega o construtor
@Override
protected String getExtension() {
return "vm";
}
@Override
protected String getPrefix() {
return "/WEB-INF/vms/"
}
}
214

## Página 223

CasadoCódigo Capítulo15.Apêndice:FuncionamentointernodoVRaptor
15.5 Mais informações sobre o funcionamento d o
VRaptor
OVRaptorpossuiumasuítedetestesbastanteabrangenteelegível,feitaparagarantir
ofuncionamentoesperadodoscomponentes,mastambémparadocumentarcada
umadasfuncionalidadesimplementadas.
Outramaneiradeentendermelhorofuncionamentoétentandoimplementar
algumafuncionalidadeparaoVRaptor. Pull Requestsesugestões defuncionalida-
dessãomuitobemvindasesãoótimasmaneirasdeaprenderadesenvolvercódigos
bastantediferentesdoqueagentefaznodiaadiadeaplicações. U mcódigodefra-
mework/bibliotecatemdesafiosúnicosebastanteinteressanteseissoaumentaoseu
conhecimento.
ContribuaparaoVRaptorouparaqualqueroutrabibliotecaopensourceque
vocêusanassuasaplicações, esetorneumdesenvolvedormelhor,alémdeserreco-
nhecidopordesenvolvedoresnomundointeiro.
215